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
        draft["observers"] = [{"mode": "preset", "name": "paper_e_ema_v1"}]
        self.assertEqual(r.resolve_draft(draft)["observers"][0]["name"], "paper_e_ema_v1")
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
        draft = example(); draft["topology"] = "unknown"
        with self.assertRaises(ValueError): r.resolve_draft(draft)
        draft = example(); draft["observers"] = [{"mode": "preset", "name": "paper_e_staged_v1"}] * 2
        with self.assertRaises(ValueError): r.resolve_draft(draft)

    def test_incomplete_draft_rejects_malformed_widget_data(self):
        for field, value in (("omega", []), ("k", [1, 2, 3]), ("provenance", {}), ("origin", {}), ("g", True)):
            data = json.loads(r.draft_json(r.blank_draft())); data["draft"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): r.load_draft(json.dumps(data))

    def test_help_has_class_and_source(self):
        classes = {"plain_definition", "historical_provenance", "accepted_claim", "known_qualification", "open_rationale", "research_only_reference"}
        for item in r.help_data()["items"]:
            self.assertIn(item["class"], classes); self.assertTrue(item["source"])


def custom(variant="staged", observer_id="custom-1"):
    value = r.preset_to_custom({"mode": "preset", "name": "paper_e_" + variant + "_v1"})
    value["observer_id"] = observer_id
    return value


class K4cRequestTests(unittest.TestCase):
    def test_request_v2_rejects_obsolete_transport(self):
        envelope = r.run_request(example())
        self.assertEqual(envelope["ui_request_version"], 2)
        envelope["ui_request_version"] = 1
        with self.assertRaises(ValueError): r.validate_envelope(envelope)

    def test_v1_draft_migration_preserves_provenance_and_values(self):
        draft = example(); draft["observers"] = [{"mode": "preset", "name": n} for n in r.OBSERVER_NAMES]
        data = json.loads(r.draft_json(draft)); data["ui_request_version"] = 1
        data["draft"]["observers"] = list(r.OBSERVER_NAMES); data["resolved"]["observers"] = list(r.OBSERVER_NAMES)
        migrated = r.load_draft(json.dumps(data))
        self.assertEqual(migrated, draft)
        self.assertEqual(json.loads(r.draft_json(migrated))["ui_request_version"], 2)
        data["resolved"]["g"] = "0x0.0p+0"
        with self.assertRaises(ValueError): r.load_draft(json.dumps(data))

    def test_ring_rows_blank_not_repeated_and_explicit_discard(self):
        draft = example(); draft["topology"] = "ring"
        bigger = r.resize_ring(draft, 2)
        self.assertEqual(bigger["omega"][:3], draft["omega"])
        self.assertEqual(bigger["omega"][3:], [["", ""]] * 3)
        self.assertIsNone(bigger["origin"]["seed"])
        self.assertIn("no seed repetition", bigger["origin"]["changes"][-1])
        with self.assertRaises(ValueError): r.apply_seed(bigger)
        with self.assertRaises(ValueError): r.resolve_draft(bigger)
        bigger["omega"][3] = ["1", "0"]
        with self.assertRaisesRegex(ValueError, "Confirm"): r.resize_ring(bigger, 1)
        self.assertEqual(len(r.resize_ring(bigger, 1, discard_confirmed=True)["omega"]), 3)
        too_large = r.blank_draft(); too_large["topology"] = "ring"; too_large["omega"] = [["", ""]] * 3003
        with self.assertRaisesRegex(ValueError, "row-count resource guard"): r.load_draft(r.draft_json(too_large))

    def test_ring_passive_refusal_and_shape(self):
        draft = example(); draft["topology"] = "ring"
        self.assertEqual(r.resolve_draft(draft)["topology"], "ring")
        for key, value in (("observers", [{"mode": "preset", "name": r.OBSERVER_NAMES[0]}]), ("readouts", ["z_chiral"]), ("diagnostics", ["potential"])):
            changed = json.loads(json.dumps(draft)); changed[key] = value
            with self.assertRaisesRegex(ValueError, "Ring requires"): r.resolve_draft(changed)
        draft["omega"].append(["0", "0"])
        with self.assertRaises(ValueError): r.resolve_draft(draft)

    def test_custom_both_variants_unique_ids_and_roundtrip(self):
        draft = example(); draft["observers"] = [custom("staged", "a"), custom("ema", "b")]
        resolved = r.resolve_draft(draft)
        self.assertEqual([o["observer_id"] for o in resolved["observers"]], ["a", "b"])
        self.assertEqual(r.load_draft(r.draft_json(draft)), draft)
        draft["observers"][1]["observer_id"] = "a"
        with self.assertRaisesRegex(ValueError, "unique"): r.resolve_draft(draft)

    def test_custom_blank_and_constructor_zero_domains(self):
        for variant in ("staged", "ema"):
            with self.assertRaises(ValueError): r.resolve_observer(r.blank_observer(variant))
        value = custom("ema"); value["initialization"] = "historical_constructor_zero"; value["memory"]["m"] = ".1"
        with self.assertRaisesRegex(ValueError, "zero initial memory"): r.resolve_observer(value)
        value["memory"]["m"] = "0"; draft = example(); draft["observers"] = [value]; draft["update_index"] = "1"
        with self.assertRaisesRegex(ValueError, "update index zero"): r.resolve_draft(draft)
        value["memory"]["m"] = "2"
        with self.assertRaises(ValueError): r.resolve_observer(value)

    def test_preset_conversion_visible_origin_and_no_theta_wrap(self):
        value = custom(); self.assertEqual(value["mode"], "custom")
        self.assertEqual(value["origin"], "paper_e_staged_v1")
        self.assertIn("CUSTOM", value["provenance"]["notes"])
        value["config"]["theta_lock"] = "50.25"
        self.assertEqual(float.fromhex(r.resolve_observer(value)["config"]["theta_lock"]), 50.25)

    def test_exact_accepted_forms_and_reduced_power(self):
        for text in ("1", "-2/3", "pi", "(1+2)*3", "2^(1/2)", "2**(-2/4)", "sin(pi/2)", "cos(pi)-1"):
            with self.subTest(text=text): self.assertIsInstance(r.exact_expression(text), dict)
        self.assertEqual(r.exact_expression("2^(-2/4)")["pow"]["exponent"], {"rational": {"numerator": "-1", "denominator": "2"}})

    def test_exact_forbidden_syntax_and_resource_guards(self):
        for text in ("0.5", "1e2", "x", "sqrt(2)", "__import__('os')", "a.b", "[1]", "sin pi", "2^pi", "1," ):
            with self.subTest(text=text), self.assertRaises(ValueError): r.exact_expression(text)
        for text, error in (("1" * 2049, "length"), ("1+" * 130 + "1", "token"), ("(" * 34 + "1" + ")" * 34, "depth"), ("1" * 65, "digit"), ("2^65", "power")):
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error): r.exact_expression(text)
        with self.assertRaisesRegex(ValueError, "growth"): r.exact_expression("((123456789^64)^64)^64")

    def test_geometry_option_matrix_and_section_order(self):
        envelope = r.geometry_request("C01", {"section_heights": ["0", "1/2", "0"]})
        self.assertEqual(envelope["payload"]["fields"]["section_heights"], ["0", "1/2", "0"])
        for construction, fields in r.D03_FIELDS.items():
            values = {"construction": construction, **{k: "1" for k in fields}}
            self.assertEqual(set(r.geometry_request("D03", values)["payload"]["exact_nodes"]), set(values))
            with self.assertRaises(ValueError): r.geometry_request("D03", {**values, "extra": "1"})

    def test_passive_forms_require_explicit_sources(self):
        self.assertEqual(r.analysis_request("quadratic_form", {"vector": ["1", "2", "3"]})["operation"], "passive_analysis")
        with self.assertRaises(ValueError): r.analysis_request("potential", {})
        with self.assertRaises(ValueError): r.analysis_request("direct_history_coordinates", r.analysis_template("direct_history_coordinates"))


if __name__ == "__main__": unittest.main()
