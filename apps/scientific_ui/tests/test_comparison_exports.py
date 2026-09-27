from copy import deepcopy
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from matplotlib.figure import Figure
from trioctagon_ui import requests, exports
from trioctagon_ui.comparison import ComparisonView, plain
from trioctagon_ui.record_views import RecordView, kernel_lock
from test_requests import example
from test_worker_contract import run_child, ring_example


class ComparisonExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        def record(envelope):
            child, response = run_child(envelope)
            if child.returncode: raise AssertionError(child.stderr)
            return RecordView(response["result"]["canonical_json"])
        a = example("2"); a["readouts"] = ["z_chiral"]; a["diagnostics"] = ["potential"]
        b = example("2"); b["update_index"] = "1"
        cls.a, cls.b = record(requests.run_request(a)), record(requests.run_request(b))
        cls.ring = record(requests.run_request(ring_example()))
        cls.geometry_a = record(requests.geometry_request("C01", {"section_heights": []}))
        cls.geometry_b = record(requests.geometry_request("D03", {"construction": "aligned", "s": "1", "g_gap": "1"}))

    def test_alignment_is_exact_index_intersection_and_no_resampling(self):
        result = ComparisonView(self.a, self.b, (0, 1, 2)).result
        self.assertEqual(tuple(result["indices_only_A"]), (0,)); self.assertEqual(tuple(result["indices_common"]), (1, 2)); self.assertEqual(tuple(result["indices_only_B"]), (3,))
        self.assertEqual({r["update_index"] for r in result["rows"]}, {1, 2})

    def test_only_explicit_shared_channels_and_visible_state_size_mismatch(self):
        result = ComparisonView(self.a, self.ring, (1,)).result
        self.assertTrue(result["state_size_mismatch"])
        self.assertEqual({row["path"].split("]")[0] for row in result["rows"] if row["path"].startswith("omega")}, {"omega[1"})
        with self.assertRaises(ValueError): ComparisonView(self.a, self.ring, (4,))

    def test_missing_chirality_and_diagnostic_remain_not_recorded(self):
        comparison = ComparisonView(self.a, self.b, (0,))
        missing = [r for r in comparison.result["rows"] if r["path"].startswith(("raw_readouts", "diagnostics"))]
        self.assertTrue(missing); self.assertTrue(all(r["B"] is None and r["delta"] is None for r in missing))
        self.assertTrue(any("not recorded" in row[3] for row in comparison.rows()))

    def test_deltas_use_only_stored_values_and_no_ranking_fields(self):
        comparison = ComparisonView(self.a, self.b, (0,))
        row = next(r for r in comparison.result["rows"] if r["path"] == "omega[0].re")
        self.assertEqual(row["delta"], float.fromhex(row["B"]["f64"]) - float.fromhex(row["A"]["f64"]))
        self.assertFalse(set(comparison.result) & {"winner", "score", "rank", "best", "stable", "converged"})
        self.assertIn("DISPLAY_DERIVATION_ONLY", comparison.result["qualification"])

    def test_geometry_side_by_side_contract_and_cross_kind_refusal(self):
        result = ComparisonView(self.geometry_a, self.geometry_b).result
        self.assertEqual(result["metadata"]["A"]["geometry_definition_id"], "C01")
        self.assertEqual(result["metadata"]["B"]["geometry_definition_id"], "D03")
        self.assertIn("symmetry", result["metadata"]["A"]); self.assertNotIn("alignment", result)
        with self.assertRaises(ValueError): ComparisonView(self.a, self.geometry_a)

    def test_comparison_cache_is_immutable_and_records_unchanged(self):
        before = (self.a.canonical_json, self.b.canonical_json)
        comparison = ComparisonView(self.a, self.b, (0,)); comparison.rows(3); comparison.series()
        with self.assertRaises(TypeError): comparison.result["new"] = True
        self.assertEqual(before, (self.a.canonical_json, self.b.canonical_json))

    def test_csv_complex_split_exact_hex_and_sidecar(self):
        with tempfile.TemporaryDirectory() as directory:
            result = exports.export_csv(self.a, Path(directory)/"samples.csv", list(exports.FIELD_GROUPS), {"mode": "all"}, precision=4, kernel_identity=kernel_lock())
            rows = list(csv.DictReader(Path(result["artifact"]).open(encoding="utf-8", newline="")))
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]["omega[0].re.f64_hex"], self.a.samples[0]["omega"][0]["re"]["f64"])
            self.assertIn("omega[0].im.decimal", rows[0]); self.assertEqual(rows[0]["sample_ordinal"], "0")
            side = json.loads(Path(result["sidecar"]).read_text())
            self.assertEqual(side["parent_record_digest"], self.a.digest); self.assertEqual(side["sample_ordinals"], [0, 1, 2])
            self.assertEqual(side["sha256"], hashlib.sha256(Path(result["artifact"]).read_bytes()).hexdigest())
            self.assertEqual(side["kernel_artifact_identity"]["lock_version"], 2)

    def test_csv_inclusive_range_and_ordered_explicit_ordinals(self):
        self.assertEqual(exports.select_samples(self.a, {"mode": "range", "start": 1, "stop": 2}), [1, 2])
        self.assertEqual(exports.select_samples(self.a, {"mode": "ordinals", "ordinals": [2, 0, 2]}), [2, 0, 2])
        for selection in ({"mode": "ordinals", "ordinals": [9]}, {"mode": "range", "start": 2, "stop": 1}):
            with self.assertRaises(ValueError): exports.select_samples(self.a, selection)

    def figure(self):
        figure = Figure(); ax = figure.add_subplot(111, projection="3d"); ax.plot([0, 1], [1, 2], [2, 3]); ax.view_init(31, -47)
        return figure

    def context(self):
        return {"view_type": "test cached geometry", "parents": [exports.parent_identity(self.geometry_a)],
            "display_precision": 8, "visible_series": ["returned object"], "selection": None,
            "geometry_frames": ["explicit frame"], "geometry_objects": [{"object_id": "returned object", "visible": True}]}

    def test_png_svg_provenance_camera_and_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            for extension in ("png", "svg"):
                result = exports.export_image(self.figure(), Path(directory)/("view."+extension), self.context())
                side = json.loads(Path(result["sidecar"]).read_text())
                self.assertEqual(side["artifact_type"], "derived_"+extension); self.assertEqual(side["camera"][0]["elevation"], 31)
                self.assertEqual(side["camera"][0]["azimuth"], -47); self.assertEqual(side["geometry_frames"], ["explicit frame"])
                self.assertEqual(side["sha256"], hashlib.sha256(Path(result["artifact"]).read_bytes()).hexdigest())
                if extension == "svg": self.assertFalse(side["rasterized_layers_detected"])

    def test_comparison_image_retains_two_parents(self):
        comparison = ComparisonView(self.a, self.b, (0,))
        with tempfile.TemporaryDirectory() as directory:
            context = {**self.context(), "view_type": "comparison", "parents": [exports.parent_identity(v) for v in (comparison.a, comparison.b)]}
            result = exports.export_image(self.figure(), Path(directory)/"comparison.png", context)
            self.assertEqual([p["digest"] for p in result["metadata"]["parents"]], [self.a.digest, self.b.digest])

    def test_failed_export_removes_staging_and_partial_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            original_link = os.link; calls = []
            def fail_second(a, b):
                calls.append(b)
                if len(calls) == 2: raise OSError("sidecar publication failed")
                original_link(a, b)
            with patch("trioctagon_ui.exports.os.link", side_effect=fail_second):
                with self.assertRaises(OSError): exports.export_image(self.figure(), Path(directory)/"failed.png", self.context())
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_existing_files_and_dataset_record_directory_are_protected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"record.png"; path.write_text(self.a.canonical_json)
            with self.assertRaises(FileExistsError): exports.export_image(self.figure(), path, self.context())
            self.assertEqual(path.read_text(), self.a.canonical_json)
            (Path(directory)/"sweep-manifest.json").write_text("{}"); (Path(directory)/"records").mkdir()
            with self.assertRaises(ValueError): exports.export_csv(self.a, Path(directory)/"records/out.csv", ["omega"], {"mode": "all"})

    def test_exports_and_comparison_invoke_zero_scientific_jobs(self):
        before = self.a.canonical_json
        with tempfile.TemporaryDirectory() as directory, patch("trioctagon_ui.jobs.JobManager.start", side_effect=AssertionError("Export invoked science")):
            view = ComparisonView(self.a, self.b, (0,)); view.rows(); view.series()
            exports.export_csv(self.a, Path(directory)/"stored.csv", ["omega"], {"mode": "all"})
            exports.export_image(self.figure(), Path(directory)/"stored.svg", self.context())
        self.assertEqual(self.a.canonical_json, before)


if __name__ == "__main__": unittest.main()
