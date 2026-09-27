import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from trioctagon_ui import requests as r
from trioctagon_ui import worker
from trioctagon_ui.record_views import kernel_lock
from test_requests import example


def run_child(envelope):
    with tempfile.TemporaryDirectory(prefix="ui-worker-test-") as directory:
        root = Path(directory)
        (root / "request.json").write_text(json.dumps(envelope), encoding="utf-8")
        result = subprocess.run([sys.executable, "-I", "-B", "-m", "trioctagon_ui.worker", "--request",
            str(root / "request.json"), "--response", str(root / "response.json")], cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=90)
        response = json.loads((root / "response.json").read_text(encoding="utf-8"))
        return result, response


def record(envelope):
    response = worker.respond(envelope)
    if response["status"] != "completed":
        raise AssertionError(response["error"])
    return response["result"]["canonical_json"]


class WorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = record(r.run_request(example("1")))

    def test_only_worker_imports_public_kernel(self):
        package = Path(worker.__file__).parent
        for file in package.glob("*.py"):
            for node in ast.walk(ast.parse(file.read_text(encoding="utf-8"))):
                if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("kernel_physics"):
                    self.assertEqual(file.name, "worker.py")
                    self.assertEqual(node.module, "kernel_physics")
                    self.assertEqual([n.name for n in node.names], ["api"])
                if isinstance(node, ast.Import):
                    self.assertFalse(any(n.name.startswith("kernel_physics") for n in node.names))
            text = file.read_text(encoding="utf-8")
            self.assertNotIn("shell=True", text)
            self.assertNotIn("import pickle", text)
            self.assertNotIn("eval(", text)

    def test_inert_initializer(self):
        result = subprocess.run([sys.executable, "-I", "-B", "-c",
            "import trioctagon_ui,sys; assert not any(n.startswith(('PySide6','matplotlib','kernel_physics')) for n in sys.modules)"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_installed_child_no_gui_or_models_or_network(self):
        child, response = run_child(r.run_request(example("0")))
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(response["imports"]["gui"], [])
        self.assertEqual(response["imports"]["models"], [])
        self.assertEqual(response["runtime_network_attempts"], [])
        self.assertTrue(response["isolated"])
        self.assertEqual(response["result"]["source_commit"], kernel_lock()["source_commit"])

    def test_run_zero_one_n_routing(self):
        from kernel_physics import api
        for n in (0, 1, 3):
            with self.subTest(n=n), patch.object(api, "run", wraps=api.run) as call:
                data = json.loads(record(r.run_request(example(str(n)))))
                self.assertEqual(call.call_count, 1)
                self.assertEqual(call.call_args.kwargs["updates"], n)
                self.assertEqual(len(data["samples"]), n + 1)

    def test_named_observers_all_diagnostics_route(self):
        from kernel_physics import api
        draft = example("1"); draft["observers"] = list(r.OBSERVER_NAMES)
        draft["diagnostics"] = list(r.DIAGNOSTICS); draft["readouts"] = ["z_chiral"]
        with patch.object(api, "historical_observer", wraps=api.historical_observer) as called:
            data = json.loads(record(r.run_request(draft)))
            self.assertEqual([c.args[0] for c in called.call_args_list], list(r.OBSERVER_NAMES))
        self.assertEqual(set(data["samples"][0]["diagnostics"]), set(r.DIAGNOSTICS))

    def test_geometry_route_c01_and_d03(self):
        from kernel_physics import api
        for definition, s in (("C01", None), ("D03", "2/3")):
            with self.subTest(definition=definition), patch.object(api, "get_geometry", wraps=api.get_geometry) as call:
                data = json.loads(record(r.request("geometry", {"definition_id": definition, "s": s})))
                self.assertEqual(call.call_count, 1)
                self.assertEqual(data["geometry_definition_id"], definition)
                self.assertEqual(data["coupling"], "none")

    def test_load_routes_canonical_parent(self):
        self.assertEqual(record(r.request("load_record", {"record_json": self.parent})), self.parent)

    def test_resume_routes_without_overrides(self):
        from kernel_physics import api
        with patch.object(api, "resume", wraps=api.resume) as call:
            text = record(r.request("resume", {"record_json": self.parent, "updates": "1"}))
            self.assertEqual(call.call_count, 1)
            self.assertEqual(call.call_args.kwargs, {"updates": 1})
        old, new = json.loads(self.parent), json.loads(text)
        self.assertEqual(new["samples"][:len(old["samples"])], old["samples"])
        self.assertEqual(new["continuation"]["parent_digest"], old["deterministic_sha256"])

    def test_checkpoint_route_and_lineage(self):
        from kernel_physics import api
        data = json.loads(self.parent); sample = data["samples"][1]
        draft = example("0")
        draft["omega"] = [[repr(float.fromhex(pair[k]["f64"])) for k in ("re", "im")] for pair in sample["omega"]]
        draft["update_index"] = sample["update_index"]; draft["origin"]["seed"] = None
        payload = r.run_request(draft)["payload"]
        payload.update(record_json=self.parent, sample_index="1", observer_reset="reinitialize_named")
        with patch.object(api, "run", wraps=api.run) as call:
            new = json.loads(record(r.request("new_checkpoint_run", payload)))
            self.assertEqual(call.call_count, 1)
        self.assertEqual(new["initialization"]["kind"], "checkpoint")
        self.assertEqual(new["initialization"]["provenance"]["source_id"], data["deterministic_sha256"])
        self.assertIsNone(new["continuation"])

    def test_error_envelope_and_child_stderr(self):
        envelope = r.request("geometry", {"definition_id": "D03", "s": "1/0"})
        child, response = run_child(envelope)
        self.assertEqual(child.returncode, 1)
        self.assertEqual(response["error"]["exception_class"], "ValueError")
        self.assertIn("denominator", response["error"]["message"])
        self.assertIn("ValueError", child.stderr)
        self.assertEqual(response["request_id"], envelope["request_id"])

    def test_precision_error_is_not_generic_or_zero(self):
        from kernel_physics import api
        with patch.object(api, "run", side_effect=api.ResponsePrecisionError("explicit precision domain")):
            response = worker.respond(r.run_request(example()))
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["error"]["exception_class"], "ResponsePrecisionError")
        self.assertNotIn("result", response)

    def test_resolved_tamper_and_extra_resume_fields_rejected(self):
        envelope = r.run_request(example()); envelope["payload"]["resolved"]["g"] = "0x0.0p+0"
        self.assertEqual(worker.respond(envelope)["status"], "failed")
        envelope = r.request("resume", {"record_json": self.parent, "updates": "1", "parameters": {}})
        self.assertEqual(worker.respond(envelope)["status"], "failed")


if __name__ == "__main__": unittest.main()
