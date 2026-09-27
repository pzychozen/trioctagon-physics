import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from trioctagon_ui import requests as r, worker
from trioctagon_ui.record_views import RecordView, atomic_text, f64
from test_requests import example
from test_worker_contract import record


class RecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.run_json = record(r.run_request(example("1")))
        cls.geometry = record(r.request("geometry", {"definition_id": "C01", "s": None}))

    def test_canonical_save_load_both_kinds(self):
        for text in (self.run_json, self.geometry):
            with self.subTest(kind=json.loads(text)["record_type"]), tempfile.TemporaryDirectory() as directory:
                view = RecordView(text); path = Path(directory) / "record.json"
                view.save(path)
                self.assertEqual(path.read_bytes(), text.encode("utf-8"))
                loaded = record(r.request("load_record", {"record_json": path.read_text(encoding="utf-8")}))
                self.assertEqual(loaded, text)
                self.assertEqual(RecordView(loaded).digest, view.digest)
                self.assertEqual(list(Path(directory).iterdir()), [path])

    def test_loaded_record_and_cache_immutable(self):
        view = RecordView(self.run_json)
        with self.assertRaises(TypeError): view.data["samples"] = []
        with self.assertRaises(TypeError): view.samples[0]["omega"][0]["re"]["f64"] = "0"
        with self.assertRaises(TypeError): view.series["indices"] = []
        with patch("trioctagon_ui.record_views.json.loads", side_effect=AssertionError("reparse")):
            self.assertIs(view.samples, view.samples)
            self.assertIs(view.series, view.series)
            self.assertTrue(view.sample_rows(0))
            self.assertTrue(view.sample_rows(1))

    def test_draft_is_separate_and_raw_json_exact(self):
        view = RecordView(self.run_json); draft = example()
        draft["g"] = "1.25"; r.draft_json(draft)
        self.assertEqual(view.canonical_json, self.run_json)
        self.assertNotIn("ui_request_version", view.data)

    def test_missing_series_not_recomputed(self):
        view = RecordView(self.run_json)
        self.assertEqual(view.missing_series("chirality0"), "not recorded")
        draft = example("0"); draft["readouts"] = ["z_chiral"]
        returned = RecordView(record(r.run_request(draft)))
        self.assertEqual(returned.missing_series("chirality0"), "recorded")
        self.assertEqual(returned.series["chirality0"][0], f64(returned.samples[0]["raw_readouts"]["z_chiral"][0]))

    def test_stored_signed_zero_and_bits(self):
        draft = example("0"); draft["origin"]["seed"] = None
        draft["omega"][0] = ["-0.0", "-0.0"]
        view = RecordView(record(r.run_request(draft)))
        for part in ("re", "im"):
            value = view.series[f"omega0.{part}"][0]
            self.assertEqual(math.copysign(1, value), -1)
            self.assertEqual(value.hex(), view.samples[0]["omega"][0][part]["f64"])
        self.assertTrue(any(row[2] == "-0x0.0p+0" for row in view.sample_rows(0)))

    def test_resume_rejection_original_reason(self):
        from kernel_physics import api
        envelope = r.request("resume", {"record_json": self.run_json, "updates": "1"})
        with patch.object(api, "resume", side_effect=ValueError("implementation module hashes differ")) as called:
            result = worker.respond(envelope)
        self.assertEqual(called.call_count, 1)
        self.assertEqual(result["error"]["message"], "implementation module hashes differ")
        self.assertNotIn("result", result)
        self.assertEqual(RecordView(self.run_json).canonical_json, self.run_json)

    def test_failed_atomic_save_preserves_prior_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"; path.write_text("previous", encoding="utf-8")
            with patch("trioctagon_ui.record_views.os.replace", side_effect=OSError("replace denied")):
                with self.assertRaises(OSError): atomic_text(path, self.run_json)
            self.assertEqual(path.read_text(), "previous")
            self.assertEqual(list(Path(directory).iterdir()), [path])

    def test_corrupt_digest_rejected_by_public_loader(self):
        data = json.loads(self.run_json); data["deterministic_sha256"] = "0" * 64
        result = worker.respond(r.request("load_record", {"record_json": json.dumps(data)}))
        self.assertEqual(result["status"], "failed")
        self.assertNotIn("result", result)


if __name__ == "__main__": unittest.main()
