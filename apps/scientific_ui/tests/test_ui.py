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
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMessageBox
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
        [w._add_observer({"mode": "preset", "name": n}) for n in r.OBSERVER_NAMES]
        self.assertTrue(w.output_checks["readout_accounting"].isEnabled())
        self.assertEqual([o["name"] for o in w._gather()["observers"]], list(r.OBSERVER_NAMES))
        w.output_checks["readout_accounting"].setChecked(True)
        w.draft["observers"] = []; w._refresh_observers(); w._validity()
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
        w._submit(r.request("geometry", {"definition_id": "D03", "fields": {"construction": "regular", "s": "1.0"}, "exact_nodes": {}}))
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
            child, response = run_child(r.geometry_request(definition, {"section_heights": []} if definition == "C01" else {"construction": "regular", "s": s}))
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


    def test_ring_switch_rows_confirmation_and_passive_clear(self):
        w = self.window; self.filled(); original = w._gather()["omega"]
        w._add_observer({"mode": "preset", "name": r.OBSERVER_NAMES[0]})
        w.topology_combo.setCurrentText("ring")
        self.assertFalse(w.run_button.isEnabled()); self.assertIn("Ring requires", w.validation.text())
        self.assertEqual(len(w.draft["observers"]), 1)
        self.assertFalse(w.output_checks["z_chiral"].isEnabled())
        w.clear_passive.click(); self.assertTrue(w.run_button.isEnabled())
        w.q_spin.setValue(2)
        self.assertEqual(len(w.omega_edits), 6)
        self.assertEqual(w._gather()["omega"][:3], original)
        self.assertEqual(w._gather()["omega"][3:], [["", ""]] * 3)
        self.assertFalse(w.seed_button.isEnabled()); self.assertFalse(w.run_button.isEnabled())
        w.omega_edits[5][0].setText(".7")
        with patch("trioctagon_ui.app.QMessageBox.question", return_value=QMessageBox.StandardButton.No): w.q_spin.setValue(1)
        self.assertEqual(w.q_spin.value(), 2); self.assertEqual(w.omega_edits[5][0].text(), ".7")
        with patch("trioctagon_ui.app.QMessageBox.question", return_value=QMessageBox.StandardButton.Yes): w.q_spin.setValue(1)
        self.assertEqual(len(w.omega_edits), 3)
        w.topology_combo.setCurrentText("triad"); self.assertTrue(w.run_button.isEnabled())

    def test_custom_editor_blank_full_fields_and_preset_conversion(self):
        w = self.window; w.add_ema.click()
        self.assertEqual(w.observer_fields["clock.N"].text(), "")
        self.assertEqual(w.observer_fields["memory.m"].text(), "")
        self.assertIn("config.theta_lock", w.observer_fields)
        self.assertNotIn("config.gamma", w.observer_fields)
        w.observer_fields["observer_id"].setText("user-ema")
        self.assertEqual(w.draft["observers"][0]["observer_id"], "user-ema")
        w.remove_observer.click(); self.assertEqual(w.draft["observers"], [])
        w._add_observer({"mode": "preset", "name": "paper_e_staged_v1"})
        self.assertTrue(w.observer_fields["config.gamma"].isReadOnly())
        self.assertNotIn("converted", w.observer_fields["provenance.notes"].text())
        self.assertEqual(w.observer_fields["provenance.source_id"].text(), "paper_e_staged_v1")
        w.convert_observer.click()
        self.assertIn("converted", w.observer_fields["provenance.notes"].text())
        self.assertFalse(w.observer_fields["config.gamma"].isReadOnly())
        w.observer_fields["clock.q_step"].setText("-3")
        self.assertEqual(w.draft["observers"][0]["clock"]["q_step"], "-3")
        self.assertEqual(w.draft["observers"][0]["mode"], "custom")
        self.assertIn("paper_e_staged", w.draft["observers"][0]["origin"])

    def test_playback_rate_ordinal_actual_index_and_no_worker(self):
        w = self.window; draft = example("2"); draft["update_index"] = "7"
        child, response = run_child(r.run_request(draft)); self.assertEqual(child.returncode, 0, child.stderr)
        w._completed(response); before = w.current.canonical_json
        with patch.object(w.jobs, "start", side_effect=AssertionError("playback started science")):
            w.playback_rate.setValue(60); w.play_button.click()
            spin_until(lambda: w.sample.value() >= 1, timeout=5)
            w.pause_button.click(); self.assertFalse(w.play_timer.isActive())
            w.sample.setValue(1); w.back_button.click(); self.assertEqual(w.sample.value(), 0)
            w.forward_button.click(); self.assertEqual(w.sample.value(), 1)
            self.assertIn("update_index=8", w.sample_label.text())
            self.assertIn("Clock.dt", w.playback_rate.accessibleName())
        self.assertEqual(w.current.canonical_json, before)

    def test_series_visibility_and_precision_preserve_record(self):
        from test_worker_contract import ring_example
        w = self.window; child, response = run_child(r.run_request(ring_example()))
        self.assertEqual(child.returncode, 0, child.stderr); w._completed(response); before = w.current.canonical_json
        self.assertEqual(w.plots.channels.count(), 6)
        self.assertEqual(w.plots.channels.item(5).checkState(), Qt.CheckState.Unchecked)
        with patch.object(w.jobs, "start", side_effect=AssertionError("presentation started science")):
            w.plots.channels.item(0).setCheckState(Qt.CheckState.Unchecked)
            w.plots.channels.item(5).setCheckState(Qt.CheckState.Checked)
            w.precision.setValue(3); spellings = [w.sample_table.item(i, 2).text() for i in range(w.sample_table.rowCount())]
            w.precision.setValue(17)
            self.assertEqual(spellings, [w.sample_table.item(i, 2).text() for i in range(w.sample_table.rowCount())])
        self.assertEqual(w.current.canonical_json, before)
        self.assertIn("5", w.plots.visibility_label.text())

    def test_detached_analysis_cache_never_becomes_record_history(self):
        w = self.window; w._completed(self.response); parent = w.current
        w.analysis_kind.setCurrentText("quadratic_form")
        w.analysis_inputs.setPlainText(json.dumps({"vector": ["1", "2", "3"]}))
        w.analysis_button.click(); spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        self.assertEqual(len(w.analysis_cache), 1); self.assertEqual(len(w.records), 1)
        self.assertIs(w.current, parent); self.assertGreater(w.analysis_table.rowCount(), 0)
        w._select_record(parent); self.assertEqual(len(w.analysis_cache), 1)
        self.assertIsNone(w.analysis_current.result["parent_digest"])

    def test_explicit_stored_source_history_plot_and_table(self):
        from test_requests import custom
        w = self.window; draft = example("2"); draft["observers"] = [custom("staged", "s")]
        draft["diagnostics"] = ["intensity_budget"]
        child, response = run_child(r.run_request(draft)); self.assertEqual(child.returncode, 0, child.stderr)
        w._completed(response)
        w.history_kind.setCurrentText("history_torus_coordinates"); w.history_observer.setCurrentText("s")
        w.kappa_source.setCurrentText("intensity_budget.intensity_before")
        for key, text in (("N", "12"), ("R", "2"), ("r_max", "1")): w.history_fields[key].setText(text)
        w.history_button.click(); spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        result = w.analysis_current.result
        self.assertEqual(result["data"]["normalization"], "entire_supplied_history")
        self.assertIsNotNone(w.history_plot.marker)
        with patch.object(w.jobs, "start", side_effect=AssertionError("history recomputed")):
            w.sample.setValue(1); w.precision.setValue(5); w.analysis_history.setCurrentIndex(0)
            self.assertEqual(tuple(v[0] for v in w.history_plot.marker.get_data_3d()), tuple(v[1] for v in w.analysis_current.coordinates))
        self.assertEqual(len(w.analysis_cache), 1)
        self.assertTrue(any(w.analysis_table.item(i, 0).text().startswith("data.x") for i in range(w.analysis_table.rowCount())))

    def test_c01_section_order_repeats_and_d03_enablement(self):
        w = self.window; w.geometry_combo.setCurrentIndex(1)
        for text in ("0", "1/10", "0"):
            w.section_input.setText(text); w.add_section.click()
        self.assertEqual(w._geometry_envelope()["payload"]["fields"]["section_heights"], ["0", "1/10", "0"])
        w.geometry_button.click(); spin_until(lambda: not w.jobs.busy)
        self.assertEqual(w.jobs.state, "completed", w.error_details.toPlainText())
        self.assertEqual(sum(o["kind"] == "section_curve" for o in w.current.data["objects"]), 3)
        self.assertEqual(w.geometry_view.objects.count(), len(w.current.data["objects"]))
        w.section_heights.setCurrentRow(1); w.remove_section.click()
        self.assertEqual(w.section_heights.count(), 2)
        w.geometry_combo.setCurrentIndex(2)
        for name, fields in r.D03_FIELDS.items():
            w.construction_combo.setCurrentText(name)
            self.assertEqual({k for k, edit in w.geometry_fields.items() if edit.isEnabled()}, set(fields))
            for key in fields: w.geometry_fields[key].setText("5" if key == "p" else "1")
            self.assertTrue(w.geometry_button.isEnabled())
        self.assertFalse(w.add_section.isEnabled())

    def test_toolbar_has_no_export_or_save_shortcut(self):
        from trioctagon_ui.plots import ViewToolbar
        toolbars = self.window.findChildren(ViewToolbar)
        self.assertGreaterEqual(len(toolbars), 5)
        for toolbar in toolbars:
            self.assertNotIn("Save", [v[0] for v in toolbar.toolitems])
            self.assertIsNone(toolbar.save_figure())

    def test_response_v2_analysis_cannot_masquerade_as_record(self):
        request = r.analysis_request("quadratic_form", {"vector": ["1", "2", "3"]})
        child, response = run_child(request); self.assertEqual(child.returncode, 0, child.stderr)
        validate_response(response, request)
        for changes in ({"result_kind": "record"}, {"canonical_json": "{}"}, {"parent_digest": "forged"}):
            bad = deepcopy(response); bad["result"].update(changes)
            with self.assertRaises(ValueError): validate_response(bad, request)


    def test_k4d_dataset_preview_run_continue_and_draft_isolation(self):
        w = self.window; self.filled(); w.numeric["updates"].setText("1")
        self.assertEqual([w.repro_tabs.tabText(i) for i in range(w.repro_tabs.count())], ["Records", "Compare", "Datasets", "Exports", "Artifacts"])
        w.sweep_dimensions.setPlainText('{"g":{"values":[".1",".2"]}}'); w.sweep_build.click()
        self.assertEqual(w.sweep_plan["case_count"], 2); self.assertEqual(w.sweep_plan["total_requested_samples"], 4)
        before = deepcopy(w.sweep_plan); w.numeric["eps"].setText(".04"); self.assertEqual(w.sweep_plan, before)
        with tempfile.TemporaryDirectory() as directory:
            w.dataset_directory.setText(directory); w.sweep_start.click()
            spin_until(lambda: not w.sweep_controller.active)
            self.assertEqual([c["status"] for c in w.sweep_controller.manifest["cases"]], ["completed", "completed"])
            self.assertIn("2 / 2", w.dataset_progress.text()); self.assertEqual(len(w.records), 2)
            with patch.object(w.jobs, "start", wraps=w.jobs.start) as start:
                w.sweep_continue.click(); spin_until(lambda: not w.sweep_controller.active)
            self.assertEqual([c.args[0]["operation"] for c in start.call_args_list], ["load_record", "load_record"])
            self.assertEqual(len(w.records), 2)

    def test_k4d_sweep_cancel_preserves_current_record_and_blocks_manual_jobs(self):
        w = self.window; w._completed(self.response); parent = w.current; self.filled(); w.numeric["updates"].setText("100000")
        w.sweep_dimensions.setPlainText('{"g":{"values":[".1",".2"]}}'); w.sweep_build.click()
        with tempfile.TemporaryDirectory() as directory, patch("trioctagon_ui.app.QMessageBox.question", return_value=QMessageBox.StandardButton.Yes):
            w.dataset_directory.setText(directory); w.sweep_start.click(); spin_until(lambda: w.jobs.busy)
            self.assertFalse(w.run_button.isEnabled()); w.sweep_cancel.click(); spin_until(lambda: not w.sweep_controller.active and not w.jobs.busy)
            self.assertEqual([c["status"] for c in w.sweep_controller.manifest["cases"]], ["cancelled", "not_run"])
            self.assertIs(w.current, parent)

    def test_k4d_comparison_and_export_actions_use_cached_records(self):
        w = self.window; w._completed(self.response)
        child, response = run_child(r.run_request(example("2"))); self.assertEqual(child.returncode, 0, child.stderr); w._completed(response)
        w.compare_a.setCurrentIndex(1); w.compare_b.setCurrentIndex(2); w.compare_channels.setText("[0,1,2]")
        with tempfile.TemporaryDirectory() as directory, patch.object(w.jobs, "start", side_effect=AssertionError("comparison/export invoked kernel")):
            w.compare_button.click(); self.assertGreater(w.compare_table.rowCount(), 0)
            self.assertFalse(set(w.comparison.result) & {"winner", "score"})
            w.csv_groups["omega"].setChecked(True)
            for action, name in ((w.csv_button, "stored.csv"), (w.png_button, "compare.png"), (w.svg_button, "compare.svg")):
                w.export_view.setCurrentText("Comparison series")
                with patch("trioctagon_ui.app.QFileDialog.getSaveFileName", return_value=(str(Path(directory)/name), "")): action.click()
                self.assertTrue((Path(directory)/name).exists(), w.error_details.toPlainText())
                side = json.loads((Path(directory)/(name+".provenance.json")).read_text())
                if name != "stored.csv": self.assertEqual(len(side["parents"]), 2)

    def test_k4d_keyboard_reduced_motion_and_noncolour_series(self):
        w = self.window; w._completed(self.response); w.show(); w.tabs.setCurrentIndex(3)
        actions = (w.sweep_build, w.sweep_start, w.sweep_continue, w.sweep_cancel, w.sweep_load,
            w.compare_button, w.compare_a, w.compare_b, w.csv_button, w.png_button, w.svg_button)
        for action in actions:
            self.assertTrue(action.accessibleName()); self.assertNotEqual(action.focusPolicy(), Qt.FocusPolicy.NoFocus)
        w.repro_tabs.setCurrentIndex(3); w.png_button.setFocus(); QApplication.processEvents()
        self.assertIs(QApplication.focusWidget(), w.png_button)
        before = w.current.canonical_json; w.reduced_motion.setChecked(True); w.playback_rate.setValue(60); w.play_button.click()
        self.assertFalse(w.play_timer.isActive()); w.forward_button.click(); self.assertEqual(w.sample.value(), 1)
        self.assertEqual(w.current.canonical_json, before)
        lines = w.plots.figures[0].axes[0].lines[:3]
        self.assertEqual(len({(line.get_linestyle(), line.get_marker()) for line in lines}), 3)
        self.assertGreater(w.sample_table.rowCount(), 0)


if __name__ == "__main__": unittest.main()
