from copy import deepcopy
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QT_OPENGL", "software")
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
from trioctagon_ui.app import MainWindow
from trioctagon_ui import requests as r
from trioctagon_ui.jobs import validate_response
from trioctagon_ui.geometry_view import geometry_lines
from trioctagon_ui.record_views import RecordView
from test_requests import example
from test_worker_contract import run_child


def spin_until(predicate, timeout=60):
    deadline = time.monotonic() + timeout
    while not predicate() and time.monotonic() < deadline:
        QApplication.processEvents(); time.sleep(.01)
    if not predicate(): raise AssertionError("Qt condition did not complete within bound")


class UITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network_attempts = []; cls.audit_active = True
        def audit(event, args):
            if cls.audit_active and event in ("socket.connect", "socket.getaddrinfo", "urllib.Request"):
                cls.network_attempts.append(event)
                raise RuntimeError("UI interaction attempted network activity")
        sys.addaudithook(audit)
        cls.qt = QApplication.instance() or QApplication([])
        child, cls.response = run_child(r.run_request(example("1")))
        if child.returncode: raise AssertionError(child.stderr)

    @classmethod
    def tearDownClass(cls):
        cls.audit_active = False
        report = {"runtime_network_attempts": cls.network_attempts, "real_qt_interactions": True,
                  "model_imports": [n for n in sys.modules if n.startswith(("torch", "tensorflow", "transformers"))]}
        if os.environ.get("TRIOCTAGON_UI_EVIDENCE"):
            (Path(os.environ["TRIOCTAGON_UI_EVIDENCE"]) / "ui-interaction-audit.json").write_text(json.dumps(report), encoding="utf-8")
        if cls.network_attempts or report["model_imports"]: raise AssertionError(report)

    def setUp(self):
        self.window = MainWindow()

    def tearDown(self):
        if self.window.jobs.busy:
            self.window.jobs.cancel(); spin_until(lambda: not self.window.jobs.busy)
        self.window.close(); self.window.deleteLater(); QApplication.processEvents()

    def filled(self):
        self.window.seed_button.click(); self.window.reference_phase.click(); self.window.counts_button.click()

    def test_four_workspaces_blank_and_explicit_fills(self):
        w = self.window
        self.assertEqual([w.tabs.tabText(i).split(" — ")[0] for i in range(4)], list("ABCD"))
        self.assertFalse(w.run_button.isEnabled()); self.assertFalse(w.jobs.busy)
        self.assertEqual(w._gather(), r.blank_draft())
        w.seed_button.click(); w.reference_phase.click()
        self.assertFalse(w.run_button.isEnabled())
        w.counts_button.click(); self.assertTrue(w.run_button.isEnabled())
        self.assertIn("HISTORICAL PRESET", w.origin_label.text())
        w.numeric["g"].setText("0.125")
        self.assertIsNone(w._gather()["origin"]["parameters"])

    def test_slider_retains_precision_outside_range_and_keyboard(self):
        w = self.window; control = w.numeric["g"]
        control.setText("0.12345678901234567")
        self.assertEqual(control.text(), "0.12345678901234567")
        control.setText("2.5"); self.assertIn("outside soft range", control.note.text())
        self.assertEqual(control.text(), "2.5")
        control.slider.setValue(control.slider.maximum())
        self.assertEqual(float(control.text()), .5)
        w.show(); w.numeric["eps"].edit.setFocus(); QApplication.processEvents()
        self.assertEqual(w.numeric["eps"].edit.focusPolicy(), Qt.FocusPolicy.StrongFocus)
        self.assertNotEqual(w.run_button.focusPolicy(), Qt.FocusPolicy.NoFocus)
        self.assertTrue(w.numeric["eps"].edit.accessibleName())
        for action in (w.run_button, w.seed_button, w.cancel_button, w.geometry_button, w.save_button):
            self.assertTrue(action.accessibleName())

    def test_observer_diagnostic_enablement(self):
        w = self.window
        self.assertFalse(any(check.isChecked() for check in w.output_checks.values()))
        self.assertFalse(w.output_checks["readout_accounting"].isEnabled())
        w.observer_combo.setCurrentIndex(3)
        self.assertTrue(w.output_checks["readout_accounting"].isEnabled())
        self.assertEqual(w._gather()["observers"], list(r.OBSERVER_NAMES))
        w.output_checks["readout_accounting"].setChecked(True)
        w.observer_combo.setCurrentIndex(0)
        self.assertTrue(w.output_checks["readout_accounting"].isChecked())
        self.assertFalse(w.run_button.isEnabled())

    def test_job_completion_failure_and_sample_display(self):
        w = self.window; self.filled(); states = []
        w.jobs.state_changed.connect(states.append)
        w.one_button.click(); self.assertTrue(w.jobs.busy); self.assertTrue(w.cancel_button.isEnabled())
        spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        self.assertEqual(states, ["validating", "running", "completed"])
        original = w.current; self.assertEqual(len(original.samples), 2)
        with patch.object(w.jobs, "start", side_effect=AssertionError("sample invoked worker")):
            w.sample.setValue(1); QApplication.processEvents()
            self.assertGreater(w.sample_table.rowCount(), 0)
            self.assertEqual(w.raw_json.toPlainText(), original.canonical_json)
        w._submit(r.request("geometry", {"definition_id": "D03", "s": "1/0"}))
        spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "failed")
        self.assertIs(w.current, original)
        self.assertIn("ValueError", w.error_details.toPlainText())
        self.assertIn("stderr", w.error_details.toPlainText())

    def test_cancel_keeps_complete_record_one_terminal_state(self):
        w = self.window; w._completed(self.response); original = w.current
        terminal = []; w.jobs.state_changed.connect(lambda s: terminal.append(s) if s in ("completed", "failed", "cancelled") else None)
        w.jobs.start(r.run_request(example("100000")))
        w.cancel_button.click() if w.cancel_button.isEnabled() else w.jobs.cancel()
        spin_until(lambda: not w.jobs.busy)
        self.assertEqual(terminal, ["cancelled"])
        self.assertIs(w.current, original)
        self.assertFalse(w.jobs.directory.exists())
        w.jobs.cancel(); self.assertEqual(terminal, ["cancelled"])

    def test_cancel_completion_race_discards_even_complete_staging(self):
        w = self.window; w._completed(self.response); original = w.current
        envelope = r.run_request(example("0")); w.jobs.start(envelope)
        staging = deepcopy(self.response)
        staging["request_id"] = envelope["request_id"]
        w.jobs.response_path.write_text(json.dumps(staging), encoding="utf-8")
        w.jobs.cancel(); spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "cancelled"); self.assertIs(w.current, original)

    def test_partial_or_wrong_response_not_accepted(self):
        request = r.run_request(example("0")); response = deepcopy(self.response)
        response["request_id"] = request["request_id"]
        validate_response(response, request)
        for field in ("canonical_json", "source_commit", "deterministic_sha256"):
            bad = deepcopy(response); del bad["result"][field]
            with self.assertRaises(ValueError): validate_response(bad, request)
        for change in ({"status": "running"}, {"request_id": "wrong"}, {"runtime_network_attempts": ["socket.connect"]}):
            with self.assertRaises(ValueError): validate_response({**response, **change}, request)
        for field in ("imports", "isolated", "runtime_network_attempts"):
            bad = deepcopy(response); del bad[field]
            with self.assertRaises(ValueError): validate_response(bad, request)

    def test_save_load_resume_and_checkpoint_with_real_workers(self):
        w = self.window; self.filled(); w._completed(self.response)
        parent = w.current
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            with patch("trioctagon_ui.app.QFileDialog.getSaveFileName", return_value=(str(path), "JSON")):
                w._save_record()
            self.assertEqual(path.read_text(encoding="utf-8"), parent.canonical_json)
            self.assertIn("Saved", w.identity.text())
            with patch("trioctagon_ui.app.QFileDialog.getOpenFileName", return_value=(str(path), "JSON")):
                w._load_record()
            spin_until(lambda: not w.jobs.busy)
            self.assertEqual(w.current.digest, parent.digest)
        w.resume_updates.setText("1"); w.resume_button.click()
        spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        self.assertEqual(len(w.current.samples), 3)
        self.assertEqual(w.current.data["continuation"]["parent_digest"], parent.digest)
        self.assertIn("Public resume accepted", w.trust.text())
        resumed = w.current; w.sample.setValue(1); w._prepare_checkpoint()
        w.checkpoint_reset.setChecked(True); w.zero_button.click()
        spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        self.assertIsNone(w.current.data["continuation"])
        self.assertEqual(w.current.data["initialization"]["provenance"]["source_id"], resumed.digest)

    def test_checkpoint_requires_explicit_reset_and_preserves_parent(self):
        w = self.window; self.filled(); w._completed(self.response); original = w.current
        w.sample.setValue(1); w._prepare_checkpoint()
        self.assertFalse(w.run_button.isEnabled())
        self.assertEqual(w.checkpoint["sample_index"], "1")
        w.checkpoint_reset.setChecked(True); self.assertTrue(w.run_button.isEnabled())
        with patch.object(w.jobs, "start") as start:
            w.zero_button.click()
            self.assertEqual(start.call_args.args[0]["operation"], "new_checkpoint_run")
        self.assertIs(w.current, original)

    def test_geometry_both_independent_and_exact_tree(self):
        w = self.window
        for definition, s in (("C01", None), ("D03", "2/3")):
            child, response = run_child(r.request("geometry", {"definition_id": definition, "s": s}))
            self.assertEqual(child.returncode, 0, child.stderr)
            view = RecordView(response["result"]["canonical_json"])
            before = view.canonical_json; w._completed(response); QApplication.processEvents()
            self.assertEqual(w.current.canonical_json, before)
            self.assertGreater(w.geometry_tree.topLevelItemCount(), 0)
            self.assertEqual(w.geometry_view.objects.count(), len(view.data["objects"]))
            self.assertTrue(any(lines for _, _, lines in geometry_lines(view)))
            w.geometry_view.objects.item(0).setCheckState(Qt.CheckState.Unchecked)
            w.geometry_view.reset.click(); self.assertEqual(w.current.canonical_json, before)
        labels = "\n".join(label.text() for label in w.findChildren(QLabel))
        self.assertIn("Independent geometry — no dynamic attachment", labels)
        self.assertIn("Channel/observer coordinates — not physical placement", labels)


if __name__ == "__main__": unittest.main()
