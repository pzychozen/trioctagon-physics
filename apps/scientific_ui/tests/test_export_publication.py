"""Real Windows filesystem contracts; cross-token acceptance is a separate gate."""
from contextlib import ExitStack
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trioctagon_ui import axial_exports, exports
from trioctagon_ui import _export_publication as pub
from trioctagon_ui.axial_artifacts import AxialAnalysisView


CACHE = Path(__file__).parent / "fixtures/axial_export_cache.json"
CACHE_SHA = "96025b48de29f13b6577551a476542a9baaf44078405f1096ff170eb73c3b420"


def cached_view():
    raw = CACHE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == CACHE_SHA
    return AxialAnalysisView.from_saved(raw)


def no_science():
    from trioctagon_ui.qt_runtime import prepare_qt
    prepare_qt()
    from kernel_physics import api
    stack = ExitStack()
    for name in ("axial_snapshot", "axial_source_budget", "step", "run", "resume"):
        stack.enter_context(patch.object(api, name, side_effect=AssertionError("Export called science")))
    stack.enter_context(patch("trioctagon_ui.jobs.JobManager.start", side_effect=AssertionError("Export submitted science")))
    stack.enter_context(patch("trioctagon_ui.worker.execute", side_effect=AssertionError("Export called worker")))
    return stack


class ExportPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.target = self.folder / "sample.csv"
        self.sidecar = self.folder / "sample.csv.provenance.json"

    def pair(self, writer=None):
        return exports.stage_export(self.target, "derived_csv", writer or (lambda stream: stream.write(b"a,b\r\n1,2\r\n")), {"test": "cached bytes"})

    def test_destination_parent_exclusive_files_and_single_links(self):
        with pub.publication(self.target, self.sidecar) as owned:
            self.assertEqual(len({v.path for v in owned}), 2)
            for item in owned:
                self.assertEqual(item.path.parent, self.folder.resolve())
                self.assertTrue(item.path.is_file())
                with self.assertRaises(FileExistsError): item.path.open("xb")
                item.stream.write(b"owned"); item.publish()
        self.assertEqual(set(self.folder.iterdir()), {self.target, self.sidecar})
        self.assertTrue(all(p.stat().st_nlink == 1 for p in self.folder.iterdir()))

    def test_exclusive_scratch_collision_and_unicode_destination(self):
        collision = self.folder / ".trioctagon-collision.tmp"
        collision.write_bytes(b"independent scratch")
        target = self.folder / "axial-Þ-😀.json"
        with patch.object(pub.secrets, "token_hex", side_effect=["collision", "fresh"]):
            axial_exports.export_json(cached_view(), target)
        self.assertEqual(collision.read_bytes(), b"independent scratch")
        self.assertEqual(target.read_bytes(), CACHE.read_bytes())
        self.assertEqual(set(self.folder.iterdir()), {collision, target})

    def test_stream_construction_failure_closes_and_discards_owned_file(self):
        with patch.object(pub.os, "fdopen", side_effect=OSError("stream construction fault")):
            with self.assertRaisesRegex(OSError, "stream construction fault"): self.pair()
        self.assertEqual(list(self.folder.iterdir()), [])

    def test_exact_json_csv_and_no_hard_link_or_science(self):
        view = cached_view()
        expected = io.StringIO(newline="")
        out = csv.writer(expected); out.writerow(("field", "display_value", "exact_stored_token")); out.writerows(view.rows(17))
        with no_science(), patch.object(os, "link", side_effect=AssertionError("Hard links forbidden")):
            axial_exports.export_json(view, self.folder / "cache.json")
            result = axial_exports.export_csv(view, self.target)
        self.assertEqual((self.folder / "cache.json").read_bytes(), view.canonical_json.encode("utf-8"))
        self.assertEqual(self.target.read_bytes(), expected.getvalue().encode("utf-8"))
        self.assertEqual(json.loads(self.sidecar.read_bytes())["sha256"], hashlib.sha256(self.target.read_bytes()).hexdigest())
        self.assertEqual(result["metadata"]["axial_observation"], axial_exports.provenance(view))

    def test_images_equal_direct_cached_render_and_hashes(self):
        import matplotlib
        from matplotlib.figure import Figure
        figure = Figure(); figure.add_subplot().plot([0, 1], [2, 3])
        view = cached_view()
        # Fix renderer metadata only for comparison of successive identical
        # renders. Production image options and serialization remain unchanged.
        with no_science(), patch.dict(os.environ, SOURCE_DATE_EPOCH="0"), matplotlib.rc_context({"svg.hashsalt": "export-contract"}):
            for ext in ("png", "svg"):
                # Filename rendering is the predecessor export contract. SVG
                # text-mode newline translation must match it byte-for-byte.
                expected = self.folder / ("direct." + ext); figure.savefig(expected, format=ext)
                target = self.folder / ("cached." + ext)
                result = axial_exports.export_plot(view, figure, target)
                self.assertEqual(target.read_bytes(), expected.read_bytes())
                self.assertEqual(result["metadata"]["sha256"], hashlib.sha256(expected.read_bytes()).hexdigest())
                self.assertEqual(json.loads(Path(result["sidecar"]).read_bytes()), result["metadata"])

    def test_preexisting_primary_or_sidecar_untouched(self):
        for collision in (self.target, self.sidecar):
            with self.subTest(collision=collision):
                collision.write_bytes(b"independent-existing")
                with self.assertRaises(FileExistsError): self.pair()
                self.assertEqual(collision.read_bytes(), b"independent-existing")
                self.assertEqual(list(self.folder.iterdir()), [collision])
                collision.unlink()

    def test_concurrent_primary_or_sidecar_creation_never_overwritten_or_removed(self):
        original = pub._OwnedFile.publish
        for collision in (self.target, self.sidecar):
            with self.subTest(collision=collision):
                def race(item):
                    if item.destination == collision: collision.write_bytes(b"independent-race")
                    original(item)
                with patch.object(pub._OwnedFile, "publish", race), self.assertRaises(FileExistsError): self.pair()
                self.assertEqual(collision.read_bytes(), b"independent-race")
                self.assertEqual(list(self.folder.iterdir()), [collision])
                collision.unlink()

    def test_writer_flush_hash_and_publication_faults_remove_owned_files(self):
        def fail_writer(stream):
            stream.write(b"partial"); raise OSError("writer fault")
        with self.assertRaisesRegex(OSError, "writer fault"): self.pair(fail_writer)
        self.assertEqual(list(self.folder.iterdir()), [])
        for owner, name in ((pub._OwnedFile, "flush"), (exports.hashlib, "sha256"), (pub._OwnedFile, "publish")):
            with self.subTest(fault=name), patch.object(owner, name, side_effect=OSError(name + " fault")):
                with self.assertRaisesRegex(OSError, name + " fault"): self.pair()
            self.assertEqual(list(self.folder.iterdir()), [])

    def test_second_publication_failure_rolls_back_owned_primary(self):
        original = pub._OwnedFile.publish
        def second(item):
            if item.destination == self.sidecar: raise OSError("second publication fault")
            original(item)
        with patch.object(pub._OwnedFile, "publish", second), self.assertRaisesRegex(OSError, "second publication fault"): self.pair()
        self.assertEqual(list(self.folder.iterdir()), [])

    def test_held_ownership_prevents_primary_replacement_during_pair(self):
        original = pub._OwnedFile.publish
        blocked = []
        def second(item):
            if item.destination == self.sidecar:
                with self.assertRaises(PermissionError): self.target.unlink()
                with self.assertRaises(PermissionError): self.target.write_bytes(b"replacement")
                blocked.append(True)
                self.sidecar.write_bytes(b"independent")
            original(item)
        with patch.object(pub._OwnedFile, "publish", second), self.assertRaises(FileExistsError): self.pair()
        self.assertEqual(blocked, [True])
        self.assertEqual(list(self.folder.iterdir()), [self.sidecar])
        self.assertEqual(self.sidecar.read_bytes(), b"independent")

    def test_cleanup_failure_reports_owned_survivor_preserves_unrelated_file(self):
        original_publish, original_discard = pub._OwnedFile.publish, pub._OwnedFile.discard
        def second(item):
            if item.destination == self.sidecar:
                self.sidecar.write_bytes(b"independent"); raise OSError("publication fault")
            original_publish(item)
        def cleanup(item):
            if item.destination == self.target: raise OSError("injected deletion failure")
            original_discard(item)
        with patch.object(pub._OwnedFile, "publish", second), patch.object(pub._OwnedFile, "discard", cleanup):
            with self.assertRaisesRegex(OSError, "cleanup incomplete.*injected deletion failure") as caught: self.pair()
        self.assertIn(str(self.target), str(caught.exception))
        self.assertIn("publication fault", str(caught.exception.__cause__))
        self.assertEqual(self.sidecar.read_bytes(), b"independent")
        self.assertEqual(self.target.read_bytes(), b"a,b\r\n1,2\r\n")
        self.assertEqual(set(self.folder.iterdir()), {self.target, self.sidecar})

    def test_axial_json_race_and_flush_failure_leave_no_owned_survivor(self):
        view = cached_view(); target = self.folder / "cache.json"
        original = pub._OwnedFile.publish
        def race(item): target.write_bytes(b"independent"); original(item)
        with patch.object(pub._OwnedFile, "publish", race), self.assertRaises(FileExistsError): axial_exports.export_json(view, target)
        self.assertEqual(target.read_bytes(), b"independent"); target.unlink()
        with patch.object(pub._OwnedFile, "flush", side_effect=OSError("flush fault")), self.assertRaises(OSError): axial_exports.export_json(view, target)
        self.assertEqual(list(self.folder.iterdir()), [])


if __name__ == "__main__": unittest.main()
