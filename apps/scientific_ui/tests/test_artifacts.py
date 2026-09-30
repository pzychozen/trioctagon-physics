"""Read-only integration tests; all stored producer claims are TEST_ONLY fixtures."""
from contextlib import ExitStack
from dataclasses import FrozenInstanceError
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QT_OPENGL", "software")
from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from trioctagon_ui import artifact_loading as loading
from trioctagon_ui.analysis_identity import analysis_lock, verify_analysis_wheel, verify_installed_analysis
from trioctagon_ui.artifact_views import DerivedArtifactView, AttemptReceiptView

FIXTURES = Path(__file__).parent / "fixtures"


class ArtifactLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ui-artifacts-")
        self.root = Path(self.temp.name)
        self.library = loading.ArtifactLibrary()

    def tearDown(self):
        self.temp.cleanup()

    def load(self, name="derived"):
        return self.library.load(FIXTURES / (name + ".json"))

    def mutated(self, edit):
        data = json.loads((FIXTURES / "derived.json").read_bytes())
        edit(data)
        path = self.root / "invalid.json"
        path.write_bytes(json.dumps(data, sort_keys=True, separators=(",", ":")).encode())
        return path

    def test_exact_approved_archive_and_installed_identity(self):
        lock = analysis_lock()
        identity = verify_installed_analysis()
        self.assertEqual(identity.version, "0.1.1")
        self.assertEqual(identity.approved_archive_sha256, "90394bd97150bc03630de1cfd8bd868547f1cdb935b1a250b874bbe72320cf18")
        self.assertEqual(identity.source_commit, "df6295b6b5dc581a0bdec8601bae9cc3e14493bd")
        self.assertEqual(len(lock["member_manifest"]), 32)
        wheel = Path(os.environ["TRIOCTAGON_UI_ANALYSIS_WHEEL"])
        self.assertEqual(verify_analysis_wheel(wheel, lock), identity.approved_archive_sha256)
        changed = self.root / wheel.name; changed.write_bytes(wheel.read_bytes() + b"unapproved")
        with self.assertRaisesRegex(ValueError, "archive identity"):
            verify_analysis_wheel(changed, lock)

    def test_installed_content_and_closure_mismatch_fail_before_analysis_import(self):
        from importlib import metadata
        dist = metadata.distribution("trioctagon-analysis")
        real = Path.read_bytes
        target = Path(dist.locate_file("trioctagon_analysis/__init__.py"))
        def altered(path):
            return b"mismatch" if path == target else real(path)
        with patch.object(Path, "read_bytes", altered):
            with self.assertRaisesRegex(ValueError, "content mismatch"):
                self.load()
        with patch.object(Path, "rglob", return_value=iter(())):
            with self.assertRaisesRegex(ValueError, "closure mismatch"):
                self.load()

    def test_derived_canonical_immutable_and_separate_trust_dimensions(self):
        item = self.load(); view = DerivedArtifactView(item)
        self.assertEqual(item.raw, (FIXTURES / "derived.json").read_bytes())

        # A protocol counter is an arbitrary-length decimal string. Keep this
        # valid, internally rebound TEST_ONLY claim out of an unbounded QLabel.
        from trioctagon_analysis.requests import Request
        from trioctagon_analysis.provider import CopyPayload
        from trioctagon_analysis.attestation import ProducerEvidence
        from trioctagon_analysis.records import DerivedAnalysisRecord, semantic_result_digest
        data = item.document.to_dict()
        data["request"]["selection"]["expected_update_index"] = "1" * 20000
        data["result"]["update_index"] = "1" * 20000
        request, payload = Request(data["request"]), CopyPayload(data["result"])
        data["request_digest"] = request.identity.to_dict()
        data["producer"].update(request=request.identity.to_dict(), payload=payload.identity.to_dict())
        evidence = ProducerEvidence(data["producer"])
        data["completion"].update(request=request.identity.to_dict(), payload=payload.identity.to_dict(), evidence=evidence.identity.to_dict())
        data["semantic_result_digest"] = semantic_result_digest(data).to_dict()
        path = self.root / "long-counter.json"; path.write_bytes(DerivedAnalysisRecord(data).to_bytes())
        summary = DerivedArtifactView(self.library.load(path)).sample_summary
        self.assertLessEqual(len(summary.encode()), loading.MAX_DISPLAY_DIAGNOSTIC_BYTES)
        self.assertIn("truncated", summary)
        self.assertEqual(item.sha256, hashlib.sha256(item.raw).hexdigest())
        with self.assertRaises(FrozenInstanceError): item.sha256 = "changed"
        with self.assertRaises(TypeError): view.panels["Parent"]["availability"] = "changed"
        self.assertIn("UNAVAILABLE", view.panels["Parent"]["availability"])
        self.assertEqual(view.panels["Producer"]["viewer_independent_verification"], "UNAVAILABLE")
        self.assertEqual({v["state"] for v in view.panels["Producer"]["recorded_verification_vector"].values()}, {"VERIFIED"})
        self.assertIn("NOT_PROVEN", view.qualification)
        self.assertIn("CLAIMED_ONLY", view.qualification)
        self.assertIn("not supplied", view.panels["Integrity"]["external_expected_sha256"])
        self.assertEqual(view.panels["Participating kernel"]["roles"], ("parent_validation",))

    def test_all_sixteen_fields_twenty_rows_and_exact_signed_tokens(self):
        item = self.load(); view = DerivedArtifactView(item)
        data = item.document.to_dict()
        rows = view.rows()
        self.assertEqual(len(rows), 20)
        self.assertEqual(list(dict.fromkeys(r[0] for r in rows)), data["request"]["selection"]["fields"])
        self.assertEqual([r[1] for r in rows[:6]], ["0", "1", "2"] * 2)
        self.assertEqual(rows[0][3:], ("-0x0.0p+0", "-0"))
        self.assertEqual(rows[1][3:], ("0x0.0p+0", "0"))
        by_field = {r[0]: r for r in rows}
        self.assertTrue(by_field["D.gram_residual"][4].startswith("-"))
        self.assertFalse(by_field["D.slack_residual"][4].startswith("-"))
        self.assertEqual([r[:4] for r in rows], [r[:4] for r in view.rows(3)])
        self.assertEqual(item.raw, (FIXTURES / "derived.json").read_bytes())

    def test_requested_subset_order_axes_and_no_computation(self):
        view = DerivedArtifactView(self.load("subset"))
        self.assertEqual([r[0] for r in view.rows()], ["D.slack_residual"] + ["S.raw_readouts.z_chiral"] * 3 + ["D.A"])
        self.assertEqual([r[1] for r in view.rows()], ["", "0", "1", "2", ""])
        self.assertIn("Scientific recomputation: none", view.sample_summary)

    def test_receipt_strict_separate_type_and_bounded_diagnostic(self):
        item = self.load("receipt"); self.assertIsInstance(item, loading.LoadedAttemptArtifact)
        view = AttemptReceiptView(item)
        self.assertEqual(view.heading, "Analysis attempt receipt — REFUSED")
        self.assertFalse(hasattr(view, "rows"))
        with self.assertRaises(TypeError): DerivedArtifactView(item)
        from trioctagon_analysis.records import AttemptReceipt
        value = item.document.to_dict(); value.update(diagnostic="€" * 10000, diagnostic_limit=10000)
        path = self.root / "long.json"; path.write_bytes(AttemptReceipt(value).to_bytes())
        long = AttemptReceiptView(self.library.load(path))
        self.assertLessEqual(len(long.panels["Diagnostic"].encode()), 8192)
        self.assertIn("truncated", long.panels["Diagnostic"])

    def test_receipt_failed_and_cancelled_states_are_not_result(self):
        from trioctagon_analysis.records import AttemptReceipt
        base = self.load("receipt").document.to_dict()
        for outcome, category in (("FAILED", "INVALID_SCHEMA"), ("CANCELLED", "CANCELLED")):
            value = dict(base, outcome=outcome, category=category)
            value["checks"] = {k: dict(v, state="FAILED") for k, v in base["checks"].items()}
            path = self.root / (outcome + ".json"); path.write_bytes(AttemptReceipt(value).to_bytes())
            self.assertIn(outcome, AttemptReceiptView(self.library.load(path)).heading)

    def test_noncanonical_malformed_and_conflicting_envelopes_never_cached(self):
        raw = (FIXTURES / "derived.json").read_bytes()
        for data in (raw + b"\n", json.dumps(json.loads(raw), indent=2).encode(), b"{", b'{}',
                b'{"family":"TRIOCTAGON_DERIVED_ANALYSIS_RECORD","record_type":"KERNEL_RUN_RECORD"}',
                b'{"family":"MYSTERY","schema":"1.0.0"}', b'{"family":"X","family":"Y"}'):
            with self.subTest(data=data[:70]):
                path = self.root / "refused.json"; path.write_bytes(data)
                with self.assertRaises(Exception): self.library.load(path)
                self.assertEqual(self.library.items, ())

    def test_strict_owner_rejects_schema_profile_provider_operation_digests_and_weaker_vector(self):
        edits = [lambda d: d.update(schema="2.0.0"), lambda d: d.update(profile="HISTORICAL"),
            lambda d: d["request"].update(operation="unknown.operation"),
            lambda d: d["request"]["provider"].update(id="unknown.provider"),
            lambda d: d["semantic_result_digest"].update(sha256="0" * 64),
            lambda d: d["producer"]["checks"]["execution_snapshot_bound"].update(state="UNAVAILABLE"),
            lambda d: d["producer"]["checks"]["execution_snapshot_bound"].update(state="FAILED")]
        for edit in edits:
            with self.assertRaises(Exception): self.library.load(self.mutated(edit))
        self.assertEqual(self.library.items, ())

    def test_external_identity_is_optional_but_never_self_certified(self):
        path = FIXTURES / "derived.json"; digest = hashlib.sha256(path.read_bytes()).hexdigest()
        with self.assertRaises(ValueError): self.library.load(path, expected_sha256="0"*64, identity_source="separately supplied manifest")
        with self.assertRaises(ValueError): self.library.load(path, expected_sha256=digest)
        item = self.library.load(path, expected_sha256=digest, identity_source="explicit test manifest")
        self.assertEqual(item.external_expected_sha256, digest)

    def test_regular_local_file_size_depth_and_reparse_guards(self):
        with self.assertRaises(ValueError): self.library.load(self.root)
        huge = self.root / "huge.json"
        with huge.open("wb") as stream: stream.truncate(loading.MAX_INPUT_FILE_BYTES + 1)
        with self.assertRaisesRegex(ValueError, "16 MiB"): self.library.load(huge)
        deep = self.root / "deep.json"; deep.write_bytes(b'{"a":' + b'['*33 + b'0' + b']'*33 + b'}')
        with self.assertRaises(Exception): self.library.load(deep)
        target = FIXTURES / "derived.json"; original = Path.lstat
        def reparse(path):
            value = original(path)
            if path == target:
                from types import SimpleNamespace
                return SimpleNamespace(st_mode=value.st_mode, st_file_attributes=0x400)
            return value
        with patch.object(Path, "lstat", reparse):
            with self.assertRaisesRegex(ValueError, "Reparse"): self.library.load(target)
        with self.assertRaises(ValueError): loading.local_path(r"\\server\share\artifact.json")

    def test_cache_count_quota_dedup_and_byte_budget(self):
        from trioctagon_analysis.records import AttemptReceipt
        item = self.load("receipt")
        self.assertIs(item, self.load("receipt"))
        base = item.document.to_dict()
        for n in range(1, 64):
            path = self.root / f"{n}.json"; path.write_bytes(AttemptReceipt(dict(base, attempt_id=f"TEST_ONLY_{n}")).to_bytes())
            self.library.load(path)
        self.assertEqual(len(self.library.items), 64)
        with self.assertRaisesRegex(ValueError, "cache is full"): self.load()
        library = loading.ArtifactLibrary()
        with patch.object(loading, "MAX_RETAINED_ANALYSIS_BYTES", len(item.raw)-1):
            with self.assertRaisesRegex(ValueError, "cache is full"): library.load(FIXTURES / "receipt.json")
        self.assertEqual(library.retained_bytes, 0)
        self.assertEqual(loading.MAX_RETAINED_ANALYSIS_BYTES, 128*1024*1024)

    def test_copy_retained_exact_bytes_after_source_changes_and_collision_refusal(self):
        source = self.root / "source.json"; source.write_bytes((FIXTURES / "derived.json").read_bytes())
        item = self.library.load(source); source.write_bytes(b"changed after capture")
        dest = self.root / "copy.json"; observation = loading.copy_artifact(item, dest)
        self.assertEqual(dest.read_bytes(), item.raw)
        self.assertEqual(observation.sha256, item.sha256)
        self.assertEqual(observation.status, "LOCAL_UI_BYTE_COPY_VERIFIED")
        with self.assertRaises(FileExistsError): loading.copy_artifact(item, dest)
        with self.assertRaises(FileExistsError): loading.copy_artifact(item, source)
        self.assertEqual(source.read_bytes(), b"changed after capture")

    def test_copy_io_failures_clean_only_owned_staging(self):
        item = self.load("receipt"); raw = item.raw
        unrelated = self.root / ".trioctagon-ui-copy-unrelated"; unrelated.write_bytes(b"preserve")
        for call in ("fsync", "link"):
            with patch.object(loading.os, call, side_effect=OSError("injected failure")):
                with self.assertRaises(OSError): loading.copy_artifact(item, self.root / "copy.json")
            self.assertEqual(set(self.root.iterdir()), {unrelated})
            self.assertEqual(item.raw, raw)
        self.assertEqual(unrelated.read_bytes(), b"preserve")

    def test_distinct_source_occurrences_and_full_byte_identity(self):
        item = self.load()
        other = self.root / "same-bytes.json"; other.write_bytes(item.raw)
        second = self.library.load(other)
        self.assertEqual(second.sha256, item.sha256)
        self.assertNotEqual(second.source, item.source)
        self.assertIs(second, self.library.load(other))
        with self.assertRaises(FileExistsError): loading.copy_artifact(second, other)

    def test_failed_emitted_hash_check_preserves_published_destination(self):
        item = self.load(); destination = self.root / "published.json"; read = Path.read_bytes
        def mismatch(path):
            return b"injected post-publication mismatch" if path == destination else read(path)
        with patch.object(Path, "read_bytes", mismatch):
            with self.assertRaisesRegex(OSError, "Published copy"): loading.copy_artifact(item, destination)
        self.assertEqual(destination.read_bytes(), item.raw)
        self.assertEqual(list(self.root.iterdir()), [destination])

    def test_copy_publish_race_never_replaces_destination(self):
        item = self.load(); destination = self.root / "race.json"; real = os.link
        def collision(src, dst):
            Path(dst).write_bytes(b"other writer")
            return real(src, dst)
        with patch.object(loading.os, "link", collision):
            with self.assertRaises(FileExistsError): loading.copy_artifact(item, destination)
        self.assertEqual(destination.read_bytes(), b"other writer")
        self.assertEqual(list(self.root.iterdir()), [destination])

    def test_core_hints_only_and_no_legacy_external_fallback(self):
        for family in ("KERNEL_RUN_RECORD", "GEOMETRY_RECORD"):
            path = self.root / "core.json"; raw = json.dumps({"record_type":family,"schema_version":"1.0.0"}).encode()
            path.write_bytes(raw); candidate = self.library.load(path)
            self.assertIsInstance(candidate, loading.CoreArtifactCandidate)
            self.assertEqual(candidate.raw, raw)
        path.write_bytes(b'{"result_kind":"analysis","analysis_type":"legacy"}')
        with self.assertRaisesRegex(ValueError, "UNKNOWN / UNSUPPORTED"): self.library.load(path)
        self.assertEqual(self.library.items, ())


class ArtifactUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication
        cls.qt = QApplication.instance() or QApplication([])
        cls.events = []; cls.audit_active = True
        def audit(event, args):
            if cls.audit_active and event in ("socket.connect", "socket.getaddrinfo", "urllib.Request"):
                cls.events.append(event); raise RuntimeError("Artifact UI attempted network")
        sys.addaudithook(audit)

    @classmethod
    def tearDownClass(cls):
        cls.audit_active = False
        if cls.events: raise AssertionError(cls.events)
        if os.environ.get("TRIOCTAGON_UI_EVIDENCE"):
            (Path(os.environ["TRIOCTAGON_UI_EVIDENCE"])/"artifact-action-audit.json").write_text(json.dumps({
                "network_attempts":cls.events, "load_select_copy_scientific_calls":0,
                "provider_execution_control_present":False,"windows_execution_binding":"NOT_PROVEN"}),encoding="utf-8")

    def setUp(self):
        from trioctagon_ui.app import MainWindow
        self.w = MainWindow()
        self.w.tabs.setCurrentIndex(3); self.w.repro_tabs.setCurrentWidget(self.w.artifacts)

    def tearDown(self):
        self.w.close(); self.w.deleteLater(); self.qt.processEvents()

    def test_artifacts_subtab_controls_and_help(self):
        from PySide6.QtWidgets import QPushButton
        w = self.w
        self.assertEqual([w.tabs.tabText(i).split(" — ")[0] for i in range(4)], list("ABCD"))
        self.assertEqual([w.repro_tabs.tabText(i) for i in range(5)], ["Records","Compare","Datasets","Exports","Artifacts"])
        self.assertEqual([b.text() for b in w.artifacts.findChildren(QPushButton)], ["Load Artifact","Copy canonical artifact bytes"])
        for name in ("artifacts","derived_artifact","attempt_receipt","legacy_analysis","producer_claim","app04_copy","analysis_execution","exact_tokens"):
            self.assertIn("df6295", w._help(name))
            self.assertIn(w._help(name), w.artifacts.help_text.toPlainText())

    def test_load_select_copy_calls_no_scientific_boundary_and_keeps_core_selection(self):
        from test_worker_contract import run_child
        from test_requests import example
        from trioctagon_ui import requests
        child, response = run_child(requests.run_request(example("1")))
        self.assertEqual(child.returncode, 0, child.stderr)
        w = self.w; w._completed(response)
        before = (w.current, w.current_run, w.current_geometry, w.analysis_current, len(w.records))
        comparison_counts = (w.compare_a.count(), w.compare_b.count())
        with ExitStack() as stack:
            boundaries = [stack.enter_context(patch.object(w.jobs, "start", side_effect=AssertionError("scientific job")))]
            # The strict records codec imports inert payload schemas from provider;
            # trap every executable provider/coordinator/B2 entry point separately.
            from trioctagon_analysis import provider
            boundaries.append(stack.enter_context(patch.object(provider, "copy_recorded", side_effect=AssertionError("provider execution"))))
            for name in ("coordinator", "b2a_worker", "b2a_windows", "b2a_snapshot"):
                self.assertNotIn("trioctagon_analysis." + name, sys.modules)
            item = w.artifacts.load_path(FIXTURES / "derived.json"); self.assertIsNotNone(item, w.artifacts.status.text())
            self.assertFalse(w.resume_button.isEnabled()); self.assertFalse(w.checkpoint_button.isEnabled())
            w._resume(); w._prepare_checkpoint(); w._save_record(); w._export_csv()
            with self.assertRaisesRegex(ValueError, "no figure"): w._image_source()
            w.artifacts.select(len(w.artifacts.entries)-1)
            with tempfile.TemporaryDirectory() as d:
                copied = Path(d)/"copy.json"; self.assertIsNotNone(w.artifacts.copy_to(copied))
                self.assertEqual(copied.read_bytes(), item.raw)
            for boundary in boundaries: boundary.assert_not_called()
        self.assertEqual((w.current, w.current_run, w.current_geometry, w.analysis_current, len(w.records)), before)
        self.assertEqual((w.compare_a.count(), w.compare_b.count()), comparison_counts)
        self.assertEqual(w.artifacts.table.rowCount(), 20)
        w.repro_tabs.setCurrentIndex(3)
        with self.assertRaisesRegex(ValueError, "no figure"): w._image_source()
        w.repro_tabs.setCurrentIndex(0); self.assertFalse(w.checkpoint_button.isEnabled())
        w._history_selected(0); self.assertTrue(w.checkpoint_button.isEnabled())

    def test_failed_load_preserves_valid_selection_and_receipt_has_no_result(self):
        panel = self.w.artifacts
        item = panel.load_path(FIXTURES / "derived.json"); self.assertIsNotNone(item, panel.status.text())
        before = (panel.current, panel.history.currentRow(), panel.heading.text())
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"bad.json"; path.write_bytes(b'{"family":"UNKNOWN"}')
            self.assertIsNone(panel.load_path(path))
        self.assertEqual((panel.current, panel.history.currentRow(), panel.heading.text()), before)
        receipt = panel.load_path(FIXTURES / "receipt.json"); self.assertIsNotNone(receipt, panel.status.text())
        self.assertEqual(panel.table.rowCount(), 0)
        self.assertTrue(panel.result_area.isHidden())
        self.assertEqual(panel.heading.text(), "Analysis attempt receipt — REFUSED")

    def test_legacy_session_cache_stays_legacy(self):
        from trioctagon_ui.record_views import AnalysisView
        # Only a pre-validated cache handle is exposed, never arbitrary JSON import.
        cached = AnalysisView({"result_kind":"analysis","analysis_type":"test-only","parent_digest":None,"data":{}})
        panel = self.w.artifacts
        panel.add_session("LEGACY DETACHED ANALYSIS", cached); panel.select(0)
        self.assertIs(panel.current, cached)
        self.assertIn("Legacy detached analysis", panel.heading.text())
        self.assertIn("not independently verified", panel.qualification.text())
        self.assertFalse(panel.copy_button.isEnabled())
        self.assertTrue(panel.result_area.isHidden())
        self.assertEqual(panel.library.items, ())

    def test_raw_preview_byte_bound_and_saved_bytes_unchanged(self):
        self.w.artifacts.load_path(FIXTURES / "receipt.json")
        from trioctagon_analysis.records import AttemptReceipt
        value = json.loads((FIXTURES / "receipt.json").read_bytes())
        value.update(diagnostic="€" * 400000, diagnostic_limit=400000)
        raw = AttemptReceipt(value).to_bytes()
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"long.json"; path.write_bytes(raw)
            item = self.w.artifacts.load_path(path); self.assertIsNotNone(item)
            preview = self.w.artifacts.raw.toPlainText()
            self.assertLessEqual(len(preview.encode()), loading.MAX_RAW_TEXT_PREVIEW_BYTES)
            self.assertIn("truncated", preview)
            self.assertEqual(item.raw, raw)

    def test_core_artifact_routing_uses_only_existing_v2_load_record(self):
        w = self.w
        with patch.object(w, "_submit") as submit:
            candidate = loading.CoreArtifactCandidate("KERNEL_RUN_RECORD", b'{}')
            w._load_artifact_core(candidate)
            envelope = submit.call_args.args[0]
            self.assertEqual(envelope["operation"], "load_record")
            self.assertEqual(envelope["ui_request_version"], 2)
        self.assertEqual(w.artifacts.library.items, ())

    def test_failed_core_handoff_preserves_artifact_selection(self):
        w = self.w
        item = w.artifacts.load_path(FIXTURES / "derived.json")
        with patch.object(w, "_submit"):
            w._load_artifact_core(loading.CoreArtifactCandidate("KERNEL_RUN_RECORD", b'{}'))
        w._failed({"operation":"load_record", "message":"TEST_ONLY invalid Core structure", "exception_class":"ValueError"})
        self.assertIs(w.artifacts.current, item)
        self.assertTrue(w._artifact_context_active())
        self.assertIs(w.repro_tabs.currentWidget(), w.artifacts)
        self.assertIn("invalid Core structure", w.artifacts.status.text())
        w._artifact_core_pending = True
        w._cancelled()
        self.assertFalse(w._artifact_core_pending)
        self.assertIs(w.artifacts.current, item)
