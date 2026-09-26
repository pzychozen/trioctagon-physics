"""P12 exact serialization and delegated construction checks, not P11 parity."""
import copy
from fractions import Fraction
import json
import unittest
from unittest.mock import patch

import sympy as sp

from kernel_physics import api as a, geometry as c, reference_scaffold as d
from kernel_physics import _geometry_records as g, _records as codec


def unpack(record):
    return json.loads(record.to_json())


class GeometryRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shell = a.get_geometry("C01", options={"section_heights": [0, c.EDGE_LENGTH/2, 0]})
        cls.scaffold = a.get_geometry("D03", options={"construction": "regular", "s": 1})

    def test_shell_delegates_to_accepted_constructor(self):
        with patch.object(c, "folded_module", wraps=c.folded_module) as owner:
            record = a.get_geometry("C01", options={"section_heights": []})
        owner.assert_called_once()
        mesh = c.folded_module()
        data = unpack(record)["objects"][0]["data"]
        self.assertEqual(data["vertices"], g._exact_data(mesh.vertices))
        for key in ("edges", "seam_edges", "boundary_edges", "boundary_loops"):
            self.assertEqual(data[key], codec._encode(getattr(mesh, key)))
        self.assertEqual(data["euler_characteristic"], str(mesh.euler_characteristic))

    def test_face_and_panel_indices_and_normals_are_distinct(self):
        mesh = c.folded_module()
        faces = unpack(self.shell)["objects"][0]["data"]["faces"]
        self.assertEqual([f["face_index"] for f in faces], ["0", "1", "2"])
        self.assertEqual([f["panel_id"] for f in faces], ["1", "2", "3"])
        self.assertEqual([f["label"] for f in faces], list("ABC"))
        for i, face in enumerate(faces):
            self.assertEqual(face["vertex_indices"], codec._encode(mesh.faces[i]))
            self.assertEqual(face["normal"], g._exact_data(mesh.face_normal(i)))

    def test_sections_preserve_requested_order_and_repetitions(self):
        data = unpack(self.shell)
        self.assertEqual([obj["object_id"] for obj in data["objects"]], ["shell", "section:0", "section:1", "section:2"])
        for obj, height in zip(data["objects"][1:], (0, c.EDGE_LENGTH/2, 0)):
            self.assertEqual(obj["kind"], "section_curve")
            self.assertEqual(obj["data"]["segments"], g._exact_data(c.central_section(height)))
        self.assertEqual(data["objects"][1]["data"], data["objects"][3]["data"])

    def test_shell_permutations_are_existing_transform_actions(self):
        mesh = c.folded_module()
        symmetry = unpack(self.shell)["symmetry"]
        self.assertEqual(symmetry["group"], "D3h")
        for generator, transform in zip(symmetry["generators"], (c.rotate_c3, c.reflect_vertical, c.reflect_horizontal)):
            expected = [str(mesh.vertices.index(transform(v))) for v in mesh.vertices]
            self.assertEqual(generator["vertex_permutation"], expected)
        self.assertEqual(symmetry["generators"][0]["axis_origin"], g._exact_data(c.CENTROID))

    def test_all_six_scaffold_constructions_delegate(self):
        cases = [("aligned", {"s": 1, "g_gap": sp.Rational(2, 3)}, d.ReferenceScaffold, "__init__"),
                 ("from_radius", {"s": 1, "p": 1}, d.ReferenceScaffold, "from_radius"),
                 ("regular", {"s": 1}, d.ReferenceScaffold, "regular"),
                 ("paper_c_member", {"s": sp.sqrt(2)-1}, d, "paper_c_member"),
                 ("translate_paper_c_to_regular", {"s": 1}, d, "translate_paper_c_to_regular"),
                 ("shrink_paper_c_at_fixed_centres", {"s": 1}, d, "shrink_paper_c_at_fixed_centres")]
        for name, options, owner, method in cases:
            with self.subTest(name=name):
                if method == "__init__":
                    expected = d.ReferenceScaffold(**options)
                    with patch.object(d, "ReferenceScaffold", wraps=d.ReferenceScaffold) as delegate:
                        record = a.get_geometry("D03", options={"construction": name, **options})
                        delegate.assert_called_once_with(**options)
                else:
                    function = getattr(owner, method)
                    expected = function(**options)
                    with patch.object(owner, method, wraps=function) as delegate:
                        record = a.get_geometry("D03", options={"construction": name, **options})
                        delegate.assert_called_once_with(**options)
                data = unpack(record)
                self.assertEqual(data["objects"][1]["data"]["vertices"], g._exact_data(expected.vertices))
                self.assertEqual(data["resolved_parameters"], {key: g._exact(getattr(expected, key)) for key in ("s", "g_gap", "p", "L")})
                self.assertEqual(data["options"]["construction"], name)

    def test_scaffold_serializes_all_closed_objects_and_frames(self):
        scaffold = d.ReferenceScaffold.regular(1)
        data = unpack(self.scaffold)
        objects = {o["object_id"]: o for o in data["objects"]}
        self.assertEqual(len(objects), 12)
        local = objects["octagon"]["data"]
        self.assertEqual(local["vertices"], g._exact_data(scaffold.octagon.vertices))
        self.assertEqual(local["filled_generators"], g._exact_data(scaffold.octagon.filled.vertices))
        region = objects["scaffold"]["data"]
        for key in ("vertices", "outline", "selected_edges", "connectors", "side_lengths", "area", "circumradius_squared", "q_H", "W", "regularity_residual"):
            self.assertEqual(region[key], g._exact_data(getattr(scaffold, key)))
        for key in ("support_halfplanes", "connector_halfplanes"):
            self.assertEqual(region[key], [{"normal": g._exact_data(h.normal), "offset": g._exact(h.offset), "relation": "le"} for h in getattr(scaffold, key)])
        self.assertEqual(objects["support_triangle"]["data"]["vertices"], g._exact_data(scaffold.support_triangle.vertices))
        for i in range(3):
            self.assertEqual(objects[f"corner_cell:{i}"]["data"]["vertices"], g._exact_data(scaffold.corner_cells[i].vertices))
            for kind in ("planar", "vertical"):
                frame = objects[f"{kind}_frame:{i}"]["data"]
                self.assertEqual(frame["frame_index"], str(i))
                self.assertEqual(frame["vertices"], g._exact_data(getattr(scaffold, kind + "_frames")[i].vertices))
                self.assertEqual(frame["centre"], g._exact_data(getattr(scaffold, kind + "_centres")[i]))
                if kind == "vertical":
                    self.assertEqual(frame["top_selected_edge"], g._exact_data(scaffold.top_selected_edges[i]))

    def test_scaffold_symmetry_retains_roles_and_comparison_is_qualified(self):
        regular = unpack(self.scaffold)["symmetry"]
        self.assertEqual((regular["regular_unlabelled_group"], regular["role_preserving_group"], regular["traversal_preserving_group"]), ("D6", "D3", "C3"))
        member = unpack(a.get_geometry("D03", options={"construction": "paper_c_member", "s": 1}))
        self.assertIsNone(member["symmetry"]["regular_unlabelled_group"])
        self.assertTrue(all(item["vertex_permutation"] is None for item in member["symmetry"]["generators"]))
        self.assertEqual(member["construction_provenance"]["literal_values"]["frame_to_panel"], "(P3,P1,P2)")
        self.assertIn("finite faces only", member["construction_provenance"]["literal_values"]["rigid_comparison"])
        self.assertNotIn("rigid_comparison", unpack(self.scaffold)["construction_provenance"]["literal_values"])

    def test_exact_codec_whitelist_roundtrip(self):
        values = [sp.Integer(-100), sp.Rational(-2, 3), sp.pi, 1+sp.sqrt(2), 3*sp.pi,
                  sp.Pow(5, sp.Rational(-1, 3)), sp.sin(sp.Rational(1, 3)), sp.cos(sp.pi/7)]
        for value in values:
            with self.subTest(value=value):
                tree = g._exact(value)
                self.assertEqual(g._decode_exact(tree), value)
                self.assertEqual(g._exact(g._decode_exact(tree)), tree)
        self.assertEqual(g._exact(sp.pi), {"pi": True})
        self.assertEqual(g._exact(sp.Rational(-2, 3)), {"rational": {"numerator": "-2", "denominator": "3"}})
        self.assertEqual(g._exact(Fraction(-2, 3)), g._exact(sp.Rational(-2, 3)))
        self.assertEqual(g._decode_exact({"rational": {"numerator": "2", "denominator": "1"}}), 2)

    def test_original_option_trees_are_retained_separately_from_resolved_parameters(self):
        requested = sp.Add(sp.Integer(2), sp.Integer(-1), evaluate=False)
        record = unpack(a.get_geometry("D03", options={"construction": "regular", "s": requested}))
        self.assertEqual(record["options"]["s"], g._exact(requested))
        self.assertEqual(g._decode_exact(record["resolved_parameters"]["s"]), 1)
        self.assertNotEqual(record["options"]["s"], record["resolved_parameters"]["s"])

    def test_unsupported_exact_inputs_are_rejected_without_rationalization(self):
        for value in (True, "sqrt(2)", 1.0, sp.Float(1), sp.Symbol("s", positive=True), sp.oo, sp.I, sp.exp(1), sp.log(2)):
            with self.subTest(value=value), self.assertRaises((ValueError, TypeError)):
                a.get_geometry("D03", options={"construction": "regular", "s": value})
        symbolic = d.ReferenceScaffold.regular(sp.Symbol("s", positive=True))
        self.assertTrue(symbolic.s.is_positive)

    def test_exact_decoder_rejects_unknown_code_and_bad_nodes(self):
        nodes = [{"symbol": "s"}, {"float": "1"}, {"eval": "__import__('os')"}, {"pi": False},
                 {"integer": "01"}, {"integer": 1}, {"rational": {"numerator": "2", "denominator": "4"}},
                 {"rational": {"numerator": "1", "denominator": "-2"}}, {"add": []},
                 {"pow": {"base": {"integer": "2"}, "exponent": {"pi": True}}},
                 {"pow": {"base": {"integer": "-1"}, "exponent": {"rational": {"numerator": "1", "denominator": "2"}}}},
                 {"sin": {"pi": True}, "display": "0"}]
        for node in nodes:
            with self.subTest(node=node), self.assertRaises((ValueError, TypeError)):
                g._decode_exact(node)

    def test_unknown_options_and_invalid_domains(self):
        cases = [("unknown", {}), ("C01", {}), ("C01", {"section_heights": [], "beta": sp.pi/4}),
                 ("C01", {"section_heights": [1]}), ("C01", {"section_heights": [0.0]}),
                 ("D03", {"construction": "unknown", "s": 1}), ("D03", {"construction": "regular"}),
                 ("D03", {"construction": "regular", "s": 0}),
                 ("D03", {"construction": "regular", "s": -1}),
                 ("D03", {"construction": "from_radius", "s": 1, "p": sp.Rational(1, 10)}),
                 ("D03", {"construction": "regular", "s": 1, "g_gap": 1})]
        for definition, options in cases:
            with self.subTest(definition=definition, options=options), self.assertRaises((TypeError, ValueError)):
                a.get_geometry(definition, options=options)

    def test_roundtrip_is_inert_and_exact(self):
        with patch.object(c, "folded_module", side_effect=AssertionError), patch.object(c, "central_section", side_effect=AssertionError), patch.object(d, "ReferenceScaffold", side_effect=AssertionError):
            for record in (self.shell, self.scaffold):
                self.assertEqual(a.GeometryRecord.from_json(record.to_json()).to_json(), record.to_json())
                self.assertEqual(record.data["coupling"], "none")
                self.assertNotIn("omega", record.data)
                self.assertNotIn("first_update_index", record.data["execution_metadata"])
                with self.assertRaises(TypeError):
                    record.data["objects"][0]["data"]["vertices"][0][0]["integer"] = "9"

    def test_record_rejects_malformed_fields_shapes_roles_and_dynamic_attachment(self):
        mutations = [lambda x: x.update(omega=[]), lambda x: x.update(coupling="attached"),
                     lambda x: x.update(schema_version="1.1.0"), lambda x: x.update(paper_id="D"),
                     lambda x: x["objects"][0].update(dimension="2"),
                     lambda x: x["objects"][0]["data"]["vertices"].pop(),
                     lambda x: x["objects"][0]["data"]["faces"][0].update(panel_id="0"),
                     lambda x: x["objects"][0]["data"]["faces"][0]["vertex_indices"].__setitem__(0, "18"),
                     lambda x: x["objects"][1].update(kind="filled_cap"),
                     lambda x: x["symmetry"]["generators"][0]["vertex_permutation"].__setitem__(0, "99"),
                     lambda x: x["coordinates"].update(exact_codec_version="2"),
                     lambda x: x["resolved_parameters"].update(w=g._exact(2))]
        for mutation in mutations:
            data = unpack(self.shell)
            mutation(data)
            with self.subTest(mutation=mutation), self.assertRaises((TypeError, ValueError)):
                a.GeometryRecord(codec._signed(data))
        for mutation in (lambda x: x["objects"][1]["data"]["support_halfplanes"][0].update(relation="lt"),
                         lambda x: x["objects"][1]["data"].update(edge_roles=["G", "E"]*3),
                         lambda x: x["objects"][1]["data"].update(is_regular="true"),
                         lambda x: x["objects"][6]["data"].update(frame_index="3")):
            data = unpack(self.scaffold)
            mutation(data)
            with self.assertRaises((TypeError, ValueError)):
                a.GeometryRecord(codec._signed(data))

    def test_record_preserves_supplied_tree_order_without_reconstruction(self):
        data = unpack(self.shell)
        tree = {"add": [{"integer": "1"}, {"integer": "-1"}]}
        data["objects"][0]["data"]["vertices"][0][0] = tree
        text = codec._canonical(codec._signed(data))
        self.assertEqual(a.GeometryRecord.from_json(text).to_json(), text)

    def test_optional_render_has_matching_shapes_and_never_replaces_exact(self):
        data = unpack(self.shell)
        exact = copy.deepcopy(data["objects"][0]["data"])

        def render(value):
            if isinstance(value, dict) and len(value) == 1 and next(iter(value)) in ("integer", "rational", "pi", "add", "mul", "pow", "sin", "cos"):
                return codec._encode(float(g._decode_exact(value).evalf(30)))
            if isinstance(value, dict):
                return {key: render(item) for key, item in value.items()}
            if isinstance(value, list):
                return [render(item) for item in value]
            return value

        data["objects"][0]["render"] = {"precision_bits": "100", "data": render(exact)}
        record = a.GeometryRecord(codec._signed(data))
        self.assertEqual(unpack(record)["objects"][0]["data"], exact)
        data["objects"][0]["render"]["data"]["vertices"][0].pop()
        with self.assertRaises(ValueError):
            a.GeometryRecord(codec._signed(data))

    def test_geometry_digest_and_duplicate_key_rejection(self):
        data = unpack(self.shell)
        digest = self.shell.deterministic_sha256
        data["execution_metadata"]["platform"] = "other"
        self.assertEqual(a.GeometryRecord(data).deterministic_sha256, digest)
        data["construction_provenance"]["notes"] += "changed"
        with self.assertRaises(ValueError):
            a.GeometryRecord(data)
        self.assertNotEqual(a.GeometryRecord(codec._signed(data)).deterministic_sha256, digest)
        with self.assertRaises(ValueError):
            a.GeometryRecord.from_json('{"record_type":"GEOMETRY_RECORD","record_type":"GEOMETRY_RECORD"}')
