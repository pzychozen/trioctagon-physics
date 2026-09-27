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
from test_requests import example, custom


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
        draft = example("1"); draft["observers"] = [{"mode": "preset", "name": n} for n in r.OBSERVER_NAMES]
        draft["diagnostics"] = list(r.DIAGNOSTICS); draft["readouts"] = ["z_chiral"]
        with patch.object(api, "historical_observer", wraps=api.historical_observer) as called:
            data = json.loads(record(r.run_request(draft)))
            self.assertEqual([c.args[0] for c in called.call_args_list], list(r.OBSERVER_NAMES))
        self.assertEqual(set(data["samples"][0]["diagnostics"]), set(r.DIAGNOSTICS))

    def test_geometry_route_c01_and_d03(self):
        from kernel_physics import api
        for definition, s in (("C01", None), ("D03", "2/3")):
            with self.subTest(definition=definition), patch.object(api, "get_geometry", wraps=api.get_geometry) as call:
                data = json.loads(record(r.geometry_request(definition, {"section_heights": []} if definition == "C01" else {"construction": "regular", "s": s})))
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
        payload.update(record_json=self.parent, sample_index="1", observer_reset="reinitialize_selected")
        with patch.object(api, "run", wraps=api.run) as call:
            new = json.loads(record(r.request("new_checkpoint_run", payload)))
            self.assertEqual(call.call_count, 1)
        self.assertEqual(new["initialization"]["kind"], "checkpoint")
        self.assertEqual(new["initialization"]["provenance"]["source_id"], data["deterministic_sha256"])
        self.assertIsNone(new["continuation"])

    def test_error_envelope_and_child_stderr(self):
        envelope = r.request("geometry", {"definition_id": "D03", "fields": {"construction": "regular", "s": "1.0"}, "exact_nodes": {}})
        child, response = run_child(envelope)
        self.assertEqual(child.returncode, 1)
        self.assertEqual(response["error"]["exception_class"], "ValueError")
        self.assertIn("Unsupported exact token", response["error"]["message"])
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


def ring_example():
    draft = example("1"); draft["topology"] = "ring"; draft["origin"]["seed"] = None
    draft["omega"] = [[".1", ".2"], [".2", "-.1"], ["-.3", ".1"], [".25", "0"], ["0", ".15"], ["-.2", "-.1"]]
    return draft


def analysis_cases():
    draft = example("0"); observer = custom("staged"); ema = custom("ema")
    params = {k: draft[k] for k in ("eps", "g", "phase_strength", "k")}
    return {
        "step_preview": {"state": {"omega": draft["omega"], "update_index": "0"}, "parameters": params, "topology": "triad"},
        "advance_clock": {"clock": observer["clock"], "dt": observer["dt"]},
        "advance_ema": {"omega": draft["omega"], "memory": ema["memory"]},
        "observe_staged": {"omega": draft["omega"], "clock": observer["clock"], "config": observer["config"]},
        "observe_ema": {"omega": draft["omega"], "clock": ema["clock"], "config": ema["config"], "memory": ema["memory"]},
        "quadratic_form": {"vector": ["1", "2", "3"]},
        "readout_accounting": {"readout": {"z": "1", "Z_macro": ["1", "0", "1"], "Z_chiral": ["0", ".5", "0"], "Z_total": ["1", ".25", "1"], "variant": "staged", "initialization": "recomputed"}, "alpha": "1", "beta": ".5"},
        "chiral_area_accounting": {"omega": draft["omega"]},
        "intensity_budget": {"omega": draft["omega"], "parameters": params},
        "potential": {"omega": draft["omega"], "parameters": params},
        "historical_alignment": {"macro": ["1", "0", "1"], "chiral": ["0", ".5", "0"], "total_vector": ["1", ".25", "1"]},
        "cylinder_point": {"kappa": "1", "q": "-2", "z": "-.5", "N": "12"}}


class K4cWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        draft = example("2"); draft["observers"] = [custom("staged", "s"), custom("ema", "e")]
        draft["diagnostics"] = ["chiral_area_accounting", "intensity_budget"]
        cls.parent = record(r.run_request(draft))
        cls.source = {"mode": "record", "record_json": cls.parent, "sample_index": "1"}

    def test_ring_public_run_routes_explicit_six_components(self):
        from kernel_physics import api
        with patch.object(api, "run", wraps=api.run) as call:
            data = json.loads(record(r.run_request(ring_example())))
        self.assertEqual(call.call_count, 1); self.assertEqual(call.call_args.kwargs["topology"], "ring")
        self.assertEqual(data["state_size"], "6"); self.assertEqual(len(data["samples"][0]["omega"]), 6)
        self.assertEqual(call.call_args.kwargs["observers"], ())

    def test_custom_multi_observer_clock_memory_literal_routing(self):
        from kernel_physics import api
        draft = example("0"); draft["observers"] = [custom("staged", "s"), custom("ema", "e")]
        draft["observers"][0]["clock"].update(q="-3", N="7", t="-0.0", q_step="-2")
        draft["observers"][1]["memory"]["m"] = "-0.125"
        with patch.object(api, "run", wraps=api.run) as call:
            record(r.run_request(draft))
        staged, ema = call.call_args.kwargs["observers"]
        self.assertEqual((staged.clock.q, staged.clock.N, staged.clock.q_step), (-3, 7, -2))
        self.assertEqual(staged.clock.t.hex(), "-0x0.0p+0")
        self.assertEqual(ema.memory.m, -.125)
        self.assertEqual(ema.provenance.literal_values["memory.m"], "-0.125")
        self.assertEqual(staged.provenance.kind, "user_supplied")

    def test_all_standalone_routes_and_lossless_named_results(self):
        from kernel_physics import api
        for name, inputs in analysis_cases().items():
            public_name = "step" if name == "step_preview" else name
            with self.subTest(name=name), patch.object(api, public_name, wraps=getattr(api, public_name)) as call:
                response = worker.respond(r.analysis_request(name, inputs))
                self.assertEqual(response["status"], "completed", response.get("error"))
                self.assertEqual(call.call_count, 1)
                result = response["result"]
                self.assertEqual(result["result_kind"], "analysis")
                self.assertIsNone(result["parent_digest"])
                self.assertNotIn("source_commit", result)
                self.assertIsInstance(result["data"], (dict, list))
                self.assertEqual(result["inputs"]["request"], inputs)

    def test_custom_constructor_zero_routes_to_public_record(self):
        draft = example("0"); draft["observers"] = [custom("staged", "s"), custom("ema", "e")]
        for observer in draft["observers"]: observer["initialization"] = "historical_constructor_zero"
        data = json.loads(record(r.run_request(draft)))
        self.assertEqual({v["initialization"] for v in data["samples"][0]["observer_results"].values()}, {"historical_constructor_zero"})

    def test_stored_sample_analysis_lineage_and_state_selection(self):
        from kernel_physics import api
        inputs = r.analysis_template("chiral_area_accounting")
        with patch.object(api, "chiral_area_accounting", wraps=api.chiral_area_accounting) as call:
            response = worker.respond(r.analysis_request("chiral_area_accounting", inputs, source=self.source))
        self.assertEqual(response["status"], "completed", response.get("error"))
        data = json.loads(self.parent); result = response["result"]
        self.assertEqual(result["parent_digest"], data["deterministic_sha256"])
        self.assertEqual(result["sample_index"], 1)
        self.assertEqual([z.real.hex() for z in call.call_args.args[0]], [z["re"]["f64"] for z in data["samples"][1]["omega"]])

    def test_direct_all_vector_keys_and_cylinder_torus_history(self):
        from kernel_physics import api
        cases = [("direct_history_coordinates", {"observer_id": "s", "key": key}) for key in ("Z_macro", "Z_chiral", "Z_total")]
        cases += [(name, {"observer_id": "e", "kappa_source": path, "N": "12", **({"R": "2", "r_max": "1"} if name == "history_torus_coordinates" else {})}) for name in ("cylinder_history_coordinates", "history_torus_coordinates") for path in r.KAPPA_SOURCES]
        for name, inputs in cases:
            with self.subTest(name=name, inputs=inputs), patch.object(api, name, wraps=getattr(api, name)) as call:
                response = worker.respond(r.analysis_request(name, inputs, source=self.source))
                self.assertEqual(response["status"], "completed", response.get("error"))
                self.assertEqual(call.call_count, 1)
                result = response["result"]; self.assertEqual(len(result["data"]["x"]), 3)
                self.assertIsNone(result["sample_index"])
                self.assertEqual(result["parent_source_commit"], kernel_lock()["source_commit"])
                if name == "history_torus_coordinates":
                    self.assertEqual(result["data"]["normalization"], "entire_supplied_history")
                    self.assertTrue(all(k in result["data"] for k in ("z_max", "H_z", "regularizer", "R", "r_max", "N")))

    def test_missing_history_source_refused_no_diagnostic_fallback(self):
        from kernel_physics import api
        draft = example("1"); draft["observers"] = [custom("staged", "s")]
        source = {"mode": "record", "record_json": record(r.run_request(draft)), "sample_index": "0"}
        with patch.object(api, "chiral_area_accounting", side_effect=AssertionError("forbidden recomputation")):
            response = worker.respond(r.analysis_request("cylinder_history_coordinates", {"observer_id": "s", "kappa_source": r.KAPPA_SOURCES[0], "N": "12"}, source=source))
        self.assertEqual(response["status"], "failed"); self.assertIn("not recorded", response["error"]["message"])

    def test_c01_sections_and_all_d03_public_constructions(self):
        from kernel_physics import api
        with patch.object(api, "get_geometry", wraps=api.get_geometry) as call:
            data = json.loads(record(r.geometry_request("C01", {"section_heights": ["0", "1/10", "0"]})))
        self.assertEqual(len(call.call_args.kwargs["options"]["section_heights"]), 3)
        self.assertEqual(sum(o["kind"] == "section_curve" for o in data["objects"]), 3)
        for construction, fields in r.D03_FIELDS.items():
            with self.subTest(construction=construction), patch.object(api, "get_geometry", wraps=api.get_geometry) as call:
                data = json.loads(record(r.geometry_request("D03", {"construction": construction, **{k: "5" if k == "p" else "1" for k in fields}})))
                self.assertEqual(call.call_args.kwargs["options"]["construction"], construction)
                self.assertEqual(set(call.call_args.kwargs["options"]), {"construction", *fields})
                self.assertEqual(data["coupling"], "none")

    def test_exact_nodes_verified_against_text_and_public_validation(self):
        envelope = r.geometry_request("D03", {"construction": "regular", "s": "2^(1/2)+sin(pi/2)"})
        self.assertEqual(worker.respond(envelope)["status"], "completed")
        envelope["payload"]["exact_nodes"]["s"] = {"integer": "9"}
        self.assertEqual(worker.respond(envelope)["status"], "failed")
        self.assertEqual(worker.respond(r.geometry_request("D03", {"construction": "regular", "s": "-1"}))["status"], "failed")
        rejected = worker.respond(r.geometry_request("C01", {"section_heights": ["1/2"]}))
        self.assertEqual(rejected["status"], "failed")
        self.assertEqual(rejected["error"]["message"], "height must lie in [-s/2, s/2]")


if __name__ == "__main__": unittest.main()
