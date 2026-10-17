"""Real Windows filesystem contracts; cross-token acceptance is a separate gate."""
from contextlib import ExitStack, contextmanager
import ctypes
from ctypes import wintypes
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import shutil
import uuid
import unittest
from unittest.mock import patch

from trioctagon_ui import axial_exports, exports
from trioctagon_ui import _export_publication as pub
from trioctagon_ui.axial_artifacts import AxialAnalysisView


CACHE = Path(__file__).parent / "fixtures/axial_export_cache.json"
CACHE_SHA = "96025b48de29f13b6577551a476542a9baaf44078405f1096ff170eb73c3b420"


def native_record(case, **data):
    """Optional evidence sink; assertions remain active without a recorder."""
    root = os.environ.get('TRIOCTAGON_UI_EVIDENCE')
    if root:
        path = Path(root) / 'native-path-regressions.jsonl'
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps({'case': case, 'pid': os.getpid(), **data}) + '\n')


def native_aliases(folder):
    """Require real native aliases. No fallback or filesystem setting changes."""
    api = ctypes.WinDLL('kernel32', use_last_error=True)
    def spelling(name, value):
        call = getattr(api, name)
        call.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
        call.restype = wintypes.DWORD
        buf = ctypes.create_unicode_buffer(32768)
        count = call(str(value), buf, len(buf))
        if not count or count >= len(buf): raise ctypes.WinError(ctypes.get_last_error())
        return Path(buf.value)
    short = spelling('GetShortPathNameW', folder)
    long = spelling('GetLongPathNameW', short)
    assert short != long, 'Native short alias unavailable: defining regression blocked'
    assert short.samefile(long) and short.resolve() == long.resolve()
    def chain(path):
        return [{'name': str(p), 'device': p.lstat().st_dev, 'inode': p.lstat().st_ino,
                 'attributes': p.lstat().st_file_attributes}
                for p in (path, *path.parents)]
    native_record('native-alias', short=str(short), long=str(long), samefile=True,
                  raw_chain=chain(short), canonical_chain=chain(short.resolve()))
    return short, long


@contextmanager
def alias_fixture():
    parent = Path(tempfile.gettempdir()).resolve()
    folder = parent / ('shell-ci02-native-fixture-' + uuid.uuid4().hex)
    folder.mkdir()  # Ordinary inherited-security directory, not TemporaryDirectory.
    try:
        yield native_aliases(folder)
    finally:
        resolved = folder.resolve()
        assert resolved.parent == parent and resolved.name.startswith('shell-ci02-native-fixture-')
        shutil.rmtree(resolved)


def file_identity(path):
    info = path.stat()
    return info.st_dev, info.st_ino


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

    def pair(self, writer=None, target=None):
        return exports.stage_export(target if target is not None else self.target, "derived_csv", writer or (lambda stream: stream.write(b"a,b\r\n1,2\r\n")), {"test": "cached bytes"})

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
        for spelling in (0, 1):
            for kind in ('primary', 'sidecar'):
                with self.subTest(spelling=spelling, kind=kind), alias_fixture() as aliases:
                    target = aliases[spelling] / 'race.csv'
                    collision = target if kind == 'primary' else target.with_suffix('.csv.provenance.json')
                    expected = collision.resolve(); hits = []; identities = []
                    def race(item):
                        if item.destination == expected:
                            hits.append(1); collision.write_bytes(b'independent-race')
                            identities.append(file_identity(collision))
                        original(item)
                    with patch.object(pub._OwnedFile, 'publish', race), self.assertRaises(FileExistsError): self.pair(target=target)
                    self.assertEqual(hits, [1]); self.assertEqual(file_identity(collision), identities[0])
                    self.assertEqual(collision.read_bytes(), b'independent-race')
                    self.assertEqual(list(aliases[spelling].iterdir()), [collision])
                    native_record('pair-race', spelling=spelling, kind=kind, hits=len(hits), independent_identity=identities[0], preserved=True)

    def test_missed_injection_is_detected_and_next_fixture_is_independent(self):
        previous = None
        for missed in (True, False):
            with alias_fixture() as aliases:
                folder = aliases[0]; target = folder / 'isolated.csv'
                self.assertEqual(list(folder.iterdir()), [])
                if previous is not None: self.assertFalse(previous.exists())
                expected = target.resolve() if not missed else target.resolve().with_name('wrong.csv')
                hits = []; original = pub._OwnedFile.publish
                def race(item):
                    if item.destination == expected: hits.append(1); target.write_bytes(b'independent')
                    original(item)
                with patch.object(pub._OwnedFile, 'publish', race):
                    if missed:
                        self.pair(target=target)
                        with self.assertRaises(AssertionError): self.assertEqual(hits, [1])
                    else:
                        with self.assertRaises(FileExistsError): self.pair(target=target)
                        self.assertEqual(hits, [1]); self.assertEqual(target.read_bytes(), b'independent')
                native_record('fixture-isolation', deliberately_missed=missed, hits=len(hits), detected=True)
                previous = aliases[1]
        self.assertFalse(previous.exists())

    def test_writer_flush_hash_and_publication_faults_remove_owned_files(self):
        def fail_writer(stream):
            stream.write(b"partial"); raise OSError("writer fault")
        with self.assertRaisesRegex(OSError, "writer fault"): self.pair(fail_writer)
        self.assertEqual(list(self.folder.iterdir()), [])
        for owner, name in ((pub._OwnedFile, "flush"), (exports.hashlib, "sha256"), (pub._OwnedFile, "publish")):
            with self.subTest(fault=name), patch.object(owner, name, side_effect=OSError(name + " fault")) as fault:
                with self.assertRaisesRegex(OSError, name + " fault"): self.pair()
                self.assertEqual(fault.call_count, 1)
            self.assertEqual(list(self.folder.iterdir()), [])

    def test_second_publication_failure_rolls_back_owned_primary(self):
        original = pub._OwnedFile.publish
        for spelling in (0, 1):
            with self.subTest(spelling=spelling), alias_fixture() as aliases:
                target = aliases[spelling] / 'second.csv'; expected = target.with_suffix('.csv.provenance.json').resolve(); hits = []
                def second(item):
                    if item.destination == expected: hits.append(1); raise OSError('second publication fault')
                    original(item)
                with patch.object(pub._OwnedFile, 'publish', second), self.assertRaisesRegex(OSError, 'second publication fault'): self.pair(target=target)
                self.assertEqual(hits, [1]); self.assertEqual(list(aliases[spelling].iterdir()), [])
                native_record('second-publication', spelling=spelling, hits=len(hits), rollback=True)

    def test_held_ownership_prevents_primary_replacement_during_pair(self):
        original = pub._OwnedFile.publish
        for spelling in (0, 1):
            with self.subTest(spelling=spelling), alias_fixture() as aliases:
                target = aliases[spelling] / 'held.csv'; side = target.with_suffix('.csv.provenance.json'); expected = side.resolve()
                hits = []; blocked = []; identities = []
                def second(item):
                    if item.destination == expected:
                        hits.append(1)
                        before = file_identity(target)
                        with self.assertRaises(PermissionError): target.unlink()
                        blocked.append('unlink')
                        with self.assertRaises(PermissionError): target.write_bytes(b'replacement')
                        blocked.append('write'); self.assertEqual(file_identity(target), before)
                        side.write_bytes(b'independent'); identities.append(file_identity(side))
                    original(item)
                with patch.object(pub._OwnedFile, 'publish', second), self.assertRaises(FileExistsError): self.pair(target=target)
                self.assertEqual(hits, [1]); self.assertEqual(blocked, ['unlink', 'write'])
                self.assertEqual(list(aliases[spelling].iterdir()), [side]); self.assertEqual(side.read_bytes(), b'independent')
                self.assertEqual(file_identity(side), identities[0])
                native_record('held-file', spelling=spelling, hits=len(hits), blocked=blocked, independent_identity=identities[0])

    def test_cleanup_failure_reports_owned_survivor_preserves_unrelated_file(self):
        original_publish, original_discard = pub._OwnedFile.publish, pub._OwnedFile.discard
        for spelling in (0, 1):
            with self.subTest(spelling=spelling), alias_fixture() as aliases:
                target = aliases[spelling] / 'cleanup.csv'; side = target.with_suffix('.csv.provenance.json')
                expected_primary, expected_side = target.resolve(), side.resolve(); hits = []; cleanups = []; identities = []
                def second(item):
                    if item.destination == expected_side:
                        hits.append(1); side.write_bytes(b'independent'); identities.extend([file_identity(target), file_identity(side)])
                        raise OSError('publication fault')
                    original_publish(item)
                def cleanup(item):
                    if item.destination == expected_primary: cleanups.append(1); raise OSError('injected deletion failure')
                    original_discard(item)
                with patch.object(pub._OwnedFile, 'publish', second), patch.object(pub._OwnedFile, 'discard', cleanup):
                    with self.assertRaisesRegex(OSError, 'cleanup incomplete.*injected deletion failure') as caught: self.pair(target=target)
                self.assertEqual(hits, [1]); self.assertEqual(cleanups, [1])
                self.assertIn(str(expected_primary), str(caught.exception)); self.assertIn('publication fault', str(caught.exception.__cause__))
                self.assertEqual(side.read_bytes(), b'independent'); self.assertEqual(target.read_bytes(), b'a,b\r\n1,2\r\n')
                self.assertEqual([file_identity(target), file_identity(side)], identities)
                self.assertEqual(set(aliases[spelling].iterdir()), {target, side})
                native_record('cleanup-fault', spelling=spelling, hits=len(hits), cleanup_hits=len(cleanups), identities=identities, canonical_message=True)

    def test_axial_json_race_and_flush_failure_leave_no_owned_survivor(self):
        view = cached_view(); target = self.folder / "cache.json"
        original = pub._OwnedFile.publish
        hits=[]
        def race(item): hits.append(1); target.write_bytes(b"independent"); original(item)
        with patch.object(pub._OwnedFile, "publish", race), self.assertRaises(FileExistsError): axial_exports.export_json(view, target)
        self.assertEqual(hits,[1])
        self.assertEqual(target.read_bytes(), b"independent"); target.unlink()
        with patch.object(pub._OwnedFile, "flush", side_effect=OSError("flush fault")) as fault:
            with self.assertRaises(OSError): axial_exports.export_json(view, target)
            self.assertEqual(fault.call_count,1)
        self.assertEqual(list(self.folder.iterdir()), [])


if __name__ == "__main__": unittest.main()
