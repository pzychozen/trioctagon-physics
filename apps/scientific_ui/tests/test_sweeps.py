from copy import deepcopy
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6.QtWidgets import QApplication
from trioctagon_ui import sweeps, requests
from trioctagon_ui.jobs import JobManager
from trioctagon_ui.record_views import kernel_lock
from test_requests import example, custom
from test_worker_contract import ring_example, run_child


def spin(predicate, timeout=60):
    deadline = time.monotonic() + timeout
    while not predicate() and time.monotonic() < deadline:
        QApplication.processEvents(); time.sleep(.01)
    if not predicate(): raise AssertionError("Dataset did not reach expected state")


class SweepTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.qt = QApplication.instance() or QApplication([])

    def plan(self, dimensions=None, base=None, **kwargs):
        return sweeps.make_plan(base or example("1"), dimensions or {"g": {"values": [".1", ".2"]}}, kernel_lock(), **kwargs)

    def controller(self, directory, plan=None):
        jobs = JobManager(); control = sweeps.SweepController(jobs)
        control.create(plan or self.plan(), directory)
        self.addCleanup(lambda: jobs.cancel() if jobs.busy else None)
        return control, jobs

    def test_inclusive_decimal_expansion_and_resolved_preview(self):
        rows = sweeps.expand_dimension({"start": "0.10", "stop": "0.30", "count": "3"})
        self.assertEqual([r["text"] for r in rows], ["0.10", "0.20", "0.30"])
        self.assertEqual([r["f64"] for r in rows], [float(v).hex() for v in (.1, .2, .3)])
        with self.assertRaises(ValueError): sweeps.expand_dimension({"start": "0", "stop": "1", "count": "1"})

    def test_duplicate_binary64_values_preserve_order_and_spelling(self):
        rows = sweeps.expand_dimension({"values": ["0.1", ".10", ".2"]})
        self.assertEqual([r["same_binary64_as"] for r in rows], [None, 0, None])
        self.assertEqual(len(self.plan({"g": {"values": ["0.1", ".10"]}})["cases"]), 2)

    def test_stable_dimension_order_case_ids_and_uuid_free_digest(self):
        a = self.plan({"k1": {"values": ["1", "2"]}, "eps": {"values": [".1", ".2"]}})
        b = self.plan({"eps": {"values": [".1", ".2"]}, "k1": {"values": ["1", "2"]}})
        self.assertEqual(a, b)
        self.assertEqual([c["substituted_values"] for c in a["cases"]], [{"eps": x, "k1": y} for x in (".1", ".2") for y in ("1", "2")])
        c = a["cases"][0]; x = sweeps.case_request(a["specification"]["base_draft"], c["substituted_values"])
        y = sweeps.case_request(a["specification"]["base_draft"], c["substituted_values"])
        self.assertNotEqual(x["request_id"], y["request_id"])
        self.assertEqual(sweeps.request_identity(x), sweeps.request_identity(y))
        self.assertTrue(c["case_id"].endswith(c["request_sha256"][:12]))

    def test_counts_warning_thresholds_and_controlled_resource_override(self):
        self.assertEqual(self.plan()["total_requested_samples"], 4)
        self.assertFalse(self.plan({"g": {"values": [".1"] * 100}})["confirmation_required"])
        self.assertTrue(self.plan({"g": {"values": [".1"] * 101}})["confirmation_required"])
        self.assertTrue(self.plan(base=example("50000"))["confirmation_required"])
        with self.assertRaisesRegex(ValueError, "GUARD"): self.plan(case_guard=1)
        with self.assertRaisesRegex(ValueError, "acknowledge"): self.plan(case_guard=10001)
        self.assertEqual(self.plan(case_guard=10001, override_ack=True)["case_count"], 2)

    def test_fixed_output_configuration_frozen_snapshot_and_l01_transition(self):
        base = example("1"); base["observers"] = [custom("ema", "e")]; base["diagnostics"] = ["potential"]
        plan = self.plan(base=base); base["observers"][0]["clock"]["N"] = "20"
        self.assertEqual(plan["fixed_configuration"]["observers"][0]["clock"]["N"], "12")
        first = sweeps.case_request(plan["specification"]["base_draft"], plan["cases"][0]["substituted_values"])["payload"]["draft"]
        self.assertIsNone(first["origin"]["parameters"]); self.assertEqual(first["origin"]["seed"], "gate_torus_seed_v1")
        for name in ("omega", "topology", "updates", "observers"):
            with self.assertRaises(ValueError): self.plan({name: {"values": ["1"]}})

    def test_ring_boundary_uses_existing_public_constraints(self):
        plan = self.plan(base=ring_example()); self.assertEqual(plan["fixed_configuration"]["topology"], "ring")
        draft = ring_example(); draft["readouts"] = ["z_chiral"]
        with self.assertRaises(ValueError): self.plan(base=draft)

    def test_manifest_identity_and_atomic_update(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = self.plan(); sweeps.save_manifest(directory, plan)
            path = Path(directory) / "sweep-manifest.json"; original = path.read_bytes()
            self.assertEqual(sweeps.load_manifest(path), plan)
            bad = deepcopy(plan); bad["cases"][0]["request_sha256"] = "0" * 64
            with self.assertRaises(ValueError): sweeps.validate_manifest(bad)
            with patch("trioctagon_ui.record_views.os.replace", side_effect=OSError("injected atomic failure")):
                with self.assertRaises(OSError): sweeps.save_manifest(directory, plan)
            self.assertEqual(path.read_bytes(), original)

    def test_two_complete_records_and_verified_continuation(self):
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory); controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c["status"] for c in controller.manifest["cases"]], ["completed"] * 2)
            before = {c["record_path"]: (Path(directory) / c["record_path"]).read_bytes() for c in controller.manifest["cases"]}
            with patch.object(jobs, "start", wraps=jobs.start) as start:
                controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c.args[0]["operation"] for c in start.call_args_list], ["load_record", "load_record"])
            self.assertEqual(before, {p: (Path(directory) / p).read_bytes() for p in before})

    def test_missing_and_tampered_records_require_public_validation_then_rerun(self):
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory); controller.start(); spin(lambda: not controller.active)
            cases = controller.manifest["cases"]
            (Path(directory) / cases[0]["record_path"]).unlink()
            path = Path(directory) / cases[1]["record_path"]
            value = json.loads(path.read_text()); value["parameters"]["g"]["f64"] = "0x0.0p+0"; path.write_text(json.dumps(value))
            with patch.object(jobs, "start", wraps=jobs.start) as start:
                controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c.args[0]["operation"] for c in start.call_args_list].count("run"), 2)
            self.assertTrue(all(c["requires_rerun_reason"] for c in cases))
            self.assertTrue(all(c["status"] == "completed" for c in cases))

    def test_valid_record_wrong_request_cannot_be_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory); controller.start(); spin(lambda: not controller.active)
            a, b = controller.manifest["cases"]
            a.update(record_path=b["record_path"], record_digest=b["record_digest"], record_source_commit=b["record_source_commit"])
            controller.start(); spin(lambda: not controller.active)
            self.assertIn("request mismatch", a["requires_rerun_reason"])

    def test_failure_is_recorded_and_later_case_runs(self):
        plan = self.plan({"eps": {"values": ["1e308", ".05"]}}, base=example("3"))
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory, plan); controller.start(); spin(lambda: not controller.active)
            a, b = controller.manifest["cases"]
            self.assertEqual(a["status"], "failed"); self.assertTrue(a["error"]["exception_class"]); self.assertEqual(b["status"], "completed")

    def test_stop_after_failure_leaves_not_run_case(self):
        plan = self.plan({"eps": {"values": ["1e308", ".05"]}}, base=example("3"), stop_after_failure=True)
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory, plan); controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c["status"] for c in controller.manifest["cases"]], ["failed", "not_run"])

    def test_cancel_preserves_completed_and_marks_remaining(self):
        plan = self.plan({"g": {"values": [".1", ".2", ".3"]}})
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory, plan)
            controller.record_ready.connect(lambda _: controller.cancel())
            controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c["status"] for c in controller.manifest["cases"]], ["completed", "not_run", "not_run"])
            controller.record_ready.disconnect(); controller.start()
            spin(lambda: controller.phase == "run" and jobs.busy)
            controller.cancel(); spin(lambda: not controller.active and not jobs.busy)
            self.assertEqual([c["status"] for c in controller.manifest["cases"]], ["completed", "cancelled", "not_run"])

    def test_orphan_reconciliation_requires_public_record_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory); controller.start(); spin(lambda: not controller.active)
            case = controller.manifest["cases"][0]; case.update(status="running", record_path=None, record_digest=None, record_source_commit=None)
            with patch.object(jobs, "start", wraps=jobs.start) as start:
                controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c.args[0]["operation"] for c in start.call_args_list], ["load_record", "load_record"])
            self.assertEqual(case["status"], "completed")

    def test_manifest_persistence_failure_stops_before_next_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            controller, jobs = self.controller(directory)
            before = (Path(directory)/"sweep-manifest.json").read_bytes(); errors = []
            controller.persistence_failed.connect(errors.append)
            with patch("trioctagon_ui.sweeps.save_manifest", side_effect=OSError("disk unavailable")), patch.object(jobs, "start", side_effect=AssertionError("worker ran after persistence failure")):
                controller.start(); spin(lambda: not controller.active)
            self.assertEqual(len(errors), 1); self.assertEqual(errors[0]["message"], "disk unavailable")
            self.assertEqual((Path(directory)/"sweep-manifest.json").read_bytes(), before)

    def test_visible_provenance_request_mismatch_refused(self):
        draft = example("0"); draft["observers"] = [custom("ema", "explicit")]
        envelope = requests.run_request(draft); child, response = run_child(envelope)
        self.assertEqual(child.returncode, 0, child.stderr)
        record = json.loads(response["result"]["canonical_json"])
        self.assertTrue(sweeps.record_matches_request(record, envelope, kernel_lock()["source_commit"]))
        changed = deepcopy(draft); changed["provenance"]["notes"] = "Different visible notes"
        with self.assertRaisesRegex(ValueError, "provenance"): sweeps.record_matches_request(record, requests.run_request(changed), kernel_lock()["source_commit"])
        changed = deepcopy(draft); changed["observers"][0]["provenance"]["source_id"] = "Different observer origin"
        with self.assertRaisesRegex(ValueError, "provenance"): sweeps.record_matches_request(record, requests.run_request(changed), kernel_lock()["source_commit"])


if __name__ == "__main__": unittest.main()
