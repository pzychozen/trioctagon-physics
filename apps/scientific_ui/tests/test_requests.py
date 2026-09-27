import json
import math
import unittest
from trioctagon_ui import requests as r


def example(updates="1"):
    draft = r.apply_reference(r.apply_seed(r.blank_draft()), "0.001")
    draft.update(update_index="0", updates=updates)
    return draft


class RequestTests(unittest.TestCase):
    def test_blank_is_incomplete(self):
        draft = r.blank_draft()
        self.assertEqual(draft["observers"], [])
        self.assertEqual(draft["diagnostics"], [])
        with self.assertRaises(ValueError): r.resolve_draft(draft)

    def test_numeric_text_and_signed_zero(self):
        self.assertEqual(r.number(" -0.0 ").hex(), "-0x0.0p+0")
        self.assertEqual(r.number("1.25e2"), 125)

    def test_nonfinite_malformed_bool_and_underflow(self):
        for value in ("NaN", "Infinity", "-Infinity", "bad", "true", "1e-9999", "1e9999", True, 1, ""):
            with self.subTest(value=value), self.assertRaises(ValueError): r.number(value)

    def test_soft_range_never_limits_request(self):
        draft = example(); draft["eps"] = "-23.123456789"
        draft = r.mark_edited(draft, "eps")
        self.assertEqual(float.fromhex(r.resolve_draft(draft)["eps"]), -23.123456789)

    def test_counts(self):
        self.assertEqual(r.integer("+100000"), 100000)
        for value in ("-1", "1.5", "true", True, ""):
            with self.subTest(value=value), self.assertRaises(ValueError): r.integer(value)

    def test_equal_k_explicit_triple(self):
        draft = r.equal_k(example(), "-2.75")
        self.assertEqual(draft["k"], ["-2.75"] * 3)
        self.assertIsNone(draft["origin"]["parameters"])

    def test_historical_fill_and_edit_origin(self):
        draft = example()
        self.assertEqual(draft["origin"]["seed"], "gate_torus_seed_v1")
        self.assertEqual(draft["origin"]["parameters"], "L01")
        edited = r.mark_edited(draft, "omega")
        self.assertIsNone(edited["origin"]["seed"])
        self.assertIn("gate_torus_seed_v1", edited["origin"]["changes"][0])
        self.assertEqual(draft["origin"]["seed"], "gate_torus_seed_v1")

    def test_observer_diagnostic_constraints(self):
        draft = example(); draft["diagnostics"] = ["readout_accounting"]
        with self.assertRaisesRegex(ValueError, "observer"): r.resolve_draft(draft)
        draft["observers"] = ["paper_e_ema_v1"]
        self.assertEqual(r.resolve_draft(draft)["observers"], draft["observers"])
        draft["diagnostics"] = ["boundary_response"]
        with self.assertRaises(ValueError): r.resolve_draft(draft)

    def test_exact_rational_grammar(self):
        self.assertEqual(str(r.rational("2/6")), "1/3")
        self.assertEqual(str(r.rational("-2/-3")), "2/3")
        for value in ("0", "-2", "1/0", "0.5", "sqrt(2)", "__import__('os')", True):
            with self.subTest(value=value), self.assertRaises(ValueError): r.rational(value)

    def test_envelope_roundtrip_and_override_snapshot(self):
        draft = example("8")
        envelope = r.run_request(draft, 0)
        self.assertEqual(draft["updates"], "8")
        self.assertEqual(envelope["payload"]["resolved"]["updates"], "0")
        self.assertEqual(r.validate_envelope(json.loads(json.dumps(envelope))), envelope)

    def test_draft_roundtrip_blank_and_complete(self):
        for draft in (r.blank_draft(), example()):
            self.assertEqual(r.load_draft(r.draft_json(draft)), draft)
        data = json.loads(r.draft_json(example())); data["resolved"]["eps"] = "0x0.0p+0"
        with self.assertRaises(ValueError): r.load_draft(json.dumps(data))

    def test_unsupported_scope_and_duplicate_selection(self):
        draft = example(); draft["topology"] = "ring"
        with self.assertRaises(ValueError): r.resolve_draft(draft)
        draft = example(); draft["observers"] = ["paper_e_staged_v1"] * 2
        with self.assertRaises(ValueError): r.resolve_draft(draft)

    def test_incomplete_draft_rejects_malformed_widget_data(self):
        for field, value in (("omega", []), ("k", [1, 2, 3]), ("provenance", {}), ("origin", {}), ("g", True)):
            data = json.loads(r.draft_json(r.blank_draft())); data["draft"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): r.load_draft(json.dumps(data))

    def test_help_has_class_and_source(self):
        classes = {"plain_definition", "historical_provenance", "accepted_claim", "known_qualification", "open_rationale", "research_only_reference"}
        for item in r.help_data()["items"]:
            self.assertIn(item["class"], classes); self.assertTrue(item["source"])


if __name__ == "__main__": unittest.main()
