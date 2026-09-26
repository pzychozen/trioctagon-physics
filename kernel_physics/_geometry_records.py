"""Separate exact geometry records, delegated to the accepted C/D constructors."""
from collections.abc import Mapping
from functools import lru_cache
from fractions import Fraction
import math
import numbers

import sympy as sp

from . import geometry as _c, reference_scaffold as _d
from ._contract_types import Provenance, _provenance_data
from ._records import (_Record, _keys, _choice, _array, _int, _bool, _f64, _canonical,
                       _parse, _encode, _signed, _metadata, _implementation, _producer_environment,
                       _papers, _provenance)

_CONSTRUCTIONS = {"aligned": ("s", "g_gap"), "from_radius": ("s", "p"),
                  "regular": ("s",), "paper_c_member": ("s",),
                  "translate_paper_c_to_regular": ("s",), "shrink_paper_c_at_fixed_centres": ("s",)}


def _exact(value):
    """Encode the allowed exact expression tree in producer SymPy argument order."""
    if isinstance(value, bool) or isinstance(value, (str, float)):
        raise TypeError("geometry requires exact numeric expressions")
    if isinstance(value, numbers.Integral):
        value = sp.Integer(int(value))
    elif isinstance(value, Fraction):
        value = sp.Rational(value.numerator, value.denominator)
    if not isinstance(value, sp.Expr):
        raise TypeError("geometry requires an exact SymPy expression or integer")
    if value.free_symbols or value.has(sp.Float) or value.is_real is not True or value.is_finite is not True:
        raise ValueError("outside the v1 exact numeric record subset")
    if isinstance(value, sp.Integer):
        return {"integer": str(value)}
    if isinstance(value, sp.Rational):
        return {"rational": {"numerator": str(value.p), "denominator": str(value.q)}}
    if value == sp.pi:
        return {"pi": True}
    if isinstance(value, (sp.Add, sp.Mul)):
        return {"add" if isinstance(value, sp.Add) else "mul": [_exact(arg) for arg in value.args]}
    if isinstance(value, sp.Pow) and isinstance(value.exp, sp.Rational):
        return {"pow": {"base": _exact(value.base), "exponent": _exact(value.exp)}}
    if value.func in (sp.sin, sp.cos):
        return {"sin" if value.func == sp.sin else "cos": _exact(value.args[0])}
    raise ValueError("unsupported Exact Codec 1 expression")


@lru_cache(maxsize=4096)
def _decode_cached(text):
    node = _parse(text)
    if not isinstance(node, dict) or len(node) != 1:
        raise ValueError("exact expression must contain one node")
    name, payload = next(iter(node.items()))
    if name == "integer":
        result = sp.Integer(_int(payload))
    elif name == "rational":
        _keys(payload, ("numerator", "denominator"))
        numerator, denominator = _int(payload["numerator"]), _int(payload["denominator"], 1)
        if math.gcd(numerator, denominator) != 1:
            raise ValueError("rational must be reduced")
        result = sp.Rational(numerator, denominator)
    elif name == "pi":
        if payload is not True:
            raise ValueError("invalid pi node")
        result = sp.pi
    elif name in ("add", "mul"):
        args = _array(payload, None, _decode_exact)
        if len(args) < 2:
            raise ValueError("add/mul require at least two arguments")
        result = (sp.Add if name == "add" else sp.Mul)(*args)
    elif name == "pow":
        _keys(payload, ("base", "exponent"))
        exponent = _decode_exact(payload["exponent"])
        if not isinstance(exponent, sp.Rational) or set(payload["exponent"]) - {"integer", "rational"}:
            raise ValueError("power exponent must be an exact rational node")
        result = sp.Pow(_decode_exact(payload["base"]), exponent)
    elif name in ("sin", "cos"):
        result = (sp.sin if name == "sin" else sp.cos)(_decode_exact(payload))
    else:
        raise ValueError("unknown Exact Codec 1 node")
    if result.is_real is not True or result.is_finite is not True:
        raise ValueError("exact expression must be finite and real")
    return result


def _decode_exact(node):
    return _decode_cached(_canonical(node))


def _exact_data(value):
    if isinstance(value, (tuple, list)):
        return [_exact_data(item) for item in value]
    return _exact(value)


def _exact_input(value):
    # Validate without rebuilding: requested expression trees remain provenance.
    _exact(value)
    if isinstance(value, numbers.Integral):
        return sp.Integer(int(value))
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return value


def _object(oid, kind, dim, frame, data):
    return {"object_id": oid, "kind": kind, "dimension": str(dim), "frame_id": frame, "data": data}


def _coordinates(frames):
    return {"exact_codec_version": "1", "frames": {
        name: {"dimension": str(dim), "origin": _exact_data([0] * dim),
               "axes": _exact_data([[int(i == j) for j in range(dim)] for i in range(dim)]),
               "units": "mathematical_length"} for name, dim in frames.items()}}


def _paper_c(heights):
    mesh = _c.folded_module()
    data = {"vertices": _exact_data(mesh.vertices), "edges": _encode(mesh.edges),
            "seam_edges": _encode(mesh.seam_edges), "boundary_edges": _encode(mesh.boundary_edges),
            "boundary_loops": _encode(mesh.boundary_loops), "euler_characteristic": str(mesh.euler_characteristic),
            "faces": [{"face_index": str(i), "panel_id": str(i + 1), "label": "ABC"[i],
                       "vertex_indices": _encode(face), "normal": _exact_data(mesh.face_normal(i))}
                      for i, face in enumerate(mesh.faces)]}
    objects = [_object("shell", "oriented_mesh", 3, "paper_c_cartesian", data)]
    for i, height in enumerate(heights):
        objects.append(_object(f"section:{i}", "section_curve", 3, "paper_c_cartesian",
                               {"height": _exact(height), "segments": _exact_data(_c.central_section(height))}))
    transforms = (("C3", _c.rotate_c3, {"axis_origin": _exact_data(_c.CENTROID), "axis_direction": _exact_data((0, 0, 1))}),
                  ("sigma_v", _c.reflect_vertical, {"plane": "x=0"}),
                  ("sigma_h", _c.reflect_horizontal, {"plane": "z=0"}))
    generators = [{"name": name, "vertex_permutation": [str(mesh.vertices.index(transform(v))) for v in mesh.vertices],
                   **description} for name, transform, description in transforms]
    return {"resolved_parameters": {"w": _exact(_c.WIDTH), "s": _exact(_c.EDGE_LENGTH), "beta": _exact(_c.FOLD_ANGLE)},
            "coordinates": _coordinates({"paper_c_cartesian": 3}), "objects": objects,
            "symmetry": {"group": "D3h", "qualification": "Accepted shell point transforms about the centroid axis.",
                         "generators": generators}}


def _paper_d(construction, options):
    constructors = {"aligned": _d.ReferenceScaffold, "from_radius": _d.ReferenceScaffold.from_radius,
                    "regular": _d.ReferenceScaffold.regular, "paper_c_member": _d.paper_c_member,
                    "translate_paper_c_to_regular": _d.translate_paper_c_to_regular,
                    "shrink_paper_c_at_fixed_centres": _d.shrink_paper_c_at_fixed_centres}
    scaffold = constructors[construction](**options)
    octagon = scaffold.octagon
    local = {key: _exact(getattr(octagon, key)) for key in ("s", "a", "w", "R_oct", "b")}
    local.update(vertices=_exact_data(octagon.vertices), outline=_exact_data(octagon.outline),
                 filled_generators=_exact_data(octagon.filled.vertices))
    objects = [_object("octagon", "closed_polygon", 2, "octagon_local", local)]
    region = {key: _exact_data(getattr(scaffold, key)) for key in (
        "vertices", "selected_edges", "connectors", "outline", "side_lengths", "area", "circumradius_squared",
        "q_H", "W", "regularity_residual")}
    region.update(edge_roles=list(scaffold.edge_roles), is_regular=scaffold.is_regular,
                  radial=_exact_data(_d.RADIAL), tangent=_exact_data(_d.TANGENT))
    for key in ("support_halfplanes", "connector_halfplanes"):
        region[key] = [{"normal": _exact_data(h.normal), "offset": _exact(h.offset), "relation": "le"}
                       for h in getattr(scaffold, key)]
    objects.append(_object("scaffold", "closed_halfplane_region", 2, "paper_d_planar", region))
    objects.append(_object("support_triangle", "closed_hull", 2, "paper_d_planar",
                           {"vertices": _exact_data(scaffold.support_triangle.vertices)}))
    for i, hull in enumerate(scaffold.corner_cells):
        objects.append(_object(f"corner_cell:{i}", "closed_hull", 2, "paper_d_planar", {"vertices": _exact_data(hull.vertices)}))
    for kind, dim, frame in (("planar", 2, "paper_d_planar"), ("vertical", 3, "paper_d_cartesian")):
        for i, (centre, hull) in enumerate(zip(getattr(scaffold, kind + "_centres"), getattr(scaffold, kind + "_frames"))):
            data = {"frame_index": str(i), "centre": _exact_data(centre), "vertices": _exact_data(hull.vertices)}
            if kind == "vertical":
                data["top_selected_edge"] = _exact_data(scaffold.top_selected_edges[i])
            objects.append(_object(f"{kind}_frame:{i}", "closed_reference_frame", dim, frame, data))
    return {"resolved_parameters": {key: _exact(getattr(scaffold, key)) for key in ("s", "g_gap", "p", "L")},
            "coordinates": _coordinates({"octagon_local": 2, "paper_d_planar": 2, "paper_d_cartesian": 3}),
            "objects": objects, "symmetry": {"group": "D3", "qualification": "E/G roles preserved; frames are separate closed reference sets.",
                "generators": [{"name": name, "vertex_permutation": None} for name in ("C3", "role_preserving_reflection")],
                "regular_unlabelled_group": "D6" if scaffold.is_regular is True else None,
                "role_preserving_group": "D3", "traversal_preserving_group": "C3"}}


def get_geometry(definition_id: str, *, options: Mapping):
    _choice(definition_id, ("C01", "D03"))
    if not isinstance(options, Mapping):
        raise TypeError("options must be an explicit mapping")
    options = dict(options)
    if definition_id == "C01":
        _keys(options, ("section_heights",))
        heights = _array(options["section_heights"], None, _exact_input)
        encoded_options = {"section_heights": _exact_data(heights)}
        construction = _paper_c(heights)
        paper = "C"
        literals = {"w": "1", "beta": "pi/3", "normal_separation": "2*pi/3", "interior_dihedral": "pi/3"}
    else:
        if "construction" not in options:
            raise ValueError("missing construction")
        name = _choice(options["construction"], _CONSTRUCTIONS)
        _keys(options, ("construction", *_CONSTRUCTIONS[name]))
        exact_options = {key: _exact_input(options[key]) for key in _CONSTRUCTIONS[name]}
        encoded_options = {"construction": name, **{key: _exact(value) for key, value in exact_options.items()}}
        construction = _paper_d(name, exact_options)
        paper = "D"
        literals = {"construction": name}
        if name == "paper_c_member":
            literals.update(rigid_comparison="finite faces only; paper_c_rigid_map(point,s)", frame_to_panel="(P3,P1,P2)")
    implementation = _implementation()
    provenance = Provenance(kind="accepted_definition", source_id=definition_id,
        source_revision=implementation["commit"], locator="kernel_physics/" + ("geometry.py" if paper == "C" else "reference_scaffold.py"),
        literal_values=literals, notes="Exact accepted construction; no dynamic attachment. Original and resolved parameters are separate.")
    data = {"record_type": "GEOMETRY_RECORD", "schema_version": "1.0.0", "api_version": "1.0.0",
            "geometry_definition_id": definition_id, "ledger_version": "0.1", "paper_id": paper,
            "options": encoded_options, "construction_provenance": _provenance_data(provenance),
            "paper_references": _papers((paper,)), "implementation": implementation,
            "execution_metadata": _producer_environment(), "coupling": "none", **construction}
    return GeometryRecord(_signed(data))


def _point(value, dimension):
    return _array(value, dimension, _decode_exact)


def _points(value, size, dimension):
    return _array(value, size, lambda v: _point(v, dimension))


def _segments(value, size, dimension):
    return _array(value, size, lambda v: _points(v, 2, dimension))


def _indices(value, size, bound):
    indices = _array(value, size, lambda v: _int(v, 0))
    if any(index >= bound for index in indices) or len(set(indices)) != len(indices):
        raise ValueError("invalid or repeated vertex indices")
    return indices


def _render(exact, rendered):
    if isinstance(exact, dict) and len(exact) == 1 and next(iter(exact)) in (
            "integer", "rational", "pi", "add", "mul", "pow", "sin", "cos"):
        _f64(rendered)
    elif isinstance(exact, dict):
        _keys(rendered, exact)
        for key in exact:
            _render(exact[key], rendered[key])
    elif isinstance(exact, list):
        _array(rendered, len(exact), lambda v: v)
        for item, display in zip(exact, rendered):
            _render(item, display)
    elif type(exact) is not type(rendered) or exact != rendered:
        raise ValueError("render must preserve nonnumeric metadata")


class GeometryRecord(_Record):
    """GEOMETRY_RECORD 1.0.0, with inert Exact Codec 1 trees as authority."""
    __slots__ = ()

    @staticmethod
    def _validate(data):
        _keys(data, ("record_type", "schema_version", "api_version", "geometry_definition_id", "ledger_version", "paper_id",
                    "options", "resolved_parameters", "construction_provenance", "paper_references", "implementation",
                    "coordinates", "objects", "symmetry", "coupling", "deterministic_sha256", "execution_metadata"))
        if data["record_type"] != "GEOMETRY_RECORD" or data["coupling"] != "none":
            raise ValueError("wrong or coupled geometry record")
        _metadata(data)
        definition = _choice(data["geometry_definition_id"], ("C01", "D03"))
        paper = "C" if definition == "C01" else "D"
        if data["paper_id"] != paper:
            raise ValueError("definition/paper mismatch")
        provenance = _provenance(data["construction_provenance"])
        if provenance.kind != "accepted_definition" or provenance.source_id != definition:
            raise ValueError("geometry construction provenance mismatch")
        if [p["source_id"] for p in data["paper_references"]] != ["P" + paper]:
            raise ValueError("geometry paper reference mismatch")
        options = data["options"]
        if paper == "C":
            _keys(options, ("section_heights",))
            heights = _array(options["section_heights"], None, _decode_exact)
            resolved_keys = ("w", "s", "beta")
            frames = {"paper_c_cartesian": 3}
        else:
            if not isinstance(options, dict) or "construction" not in options:
                raise ValueError("missing construction")
            construction = _choice(options["construction"], _CONSTRUCTIONS)
            _keys(options, ("construction", *_CONSTRUCTIONS[construction]))
            for key in _CONSTRUCTIONS[construction]:
                _decode_exact(options[key])
            resolved_keys = ("s", "g_gap", "p", "L")
            frames = {"octagon_local": 2, "paper_d_planar": 2, "paper_d_cartesian": 3}
        _keys(data["resolved_parameters"], resolved_keys)
        for value in data["resolved_parameters"].values():
            _decode_exact(value)
        if paper == "C":
            for key, expected_value in (("w", _c.WIDTH), ("s", _c.EDGE_LENGTH), ("beta", _c.FOLD_ANGLE)):
                if _decode_exact(data["resolved_parameters"][key]) != expected_value:
                    raise ValueError("noncanonical shell parameters")
            if any((sp.Abs(height) <= _c.EDGE_LENGTH / 2) != sp.true for height in heights):
                raise ValueError("section height outside the closed central band")
        else:
            if any(_decode_exact(value).is_positive is not True for value in data["resolved_parameters"].values()):
                raise ValueError("scaffold resolved parameters must be positive")
            if any(_decode_exact(options[key]).is_positive is not True for key in _CONSTRUCTIONS[construction]):
                raise ValueError("scaffold options must be positive")
        coords = data["coordinates"]
        _keys(coords, ("frames", "exact_codec_version"))
        if coords["exact_codec_version"] != "1":
            raise ValueError("unsupported exact codec version")
        _keys(coords["frames"], frames)
        for frame, dim in frames.items():
            value = coords["frames"][frame]
            _keys(value, ("dimension", "origin", "axes", "units"))
            if value["dimension"] != str(dim) or value["units"] != "mathematical_length":
                raise ValueError("frame dimension or units mismatch")
            if _point(value["origin"], dim) != [sp.Integer(0)] * dim:
                raise ValueError("frame origin must be Cartesian origin")
            axes = _points(value["axes"], dim, dim)
            if axes != [[sp.Integer(i == j) for j in range(dim)] for i in range(dim)]:
                raise ValueError("frame axes must be ordered standard basis")
        if paper == "C":
            expected = [("shell", "oriented_mesh", 3, "paper_c_cartesian")]
            expected.extend((f"section:{i}", "section_curve", 3, "paper_c_cartesian") for i in range(len(heights)))
        else:
            expected = [("octagon", "closed_polygon", 2, "octagon_local"),
                        ("scaffold", "closed_halfplane_region", 2, "paper_d_planar"),
                        ("support_triangle", "closed_hull", 2, "paper_d_planar")]
            expected.extend((f"corner_cell:{i}", "closed_hull", 2, "paper_d_planar") for i in range(3))
            expected.extend((f"planar_frame:{i}", "closed_reference_frame", 2, "paper_d_planar") for i in range(3))
            expected.extend((f"vertical_frame:{i}", "closed_reference_frame", 3, "paper_d_cartesian") for i in range(3))
        objects = _array(data["objects"], len(expected), lambda v: v)
        for obj, (oid, kind, dim, frame) in zip(objects, expected):
            _keys(obj, ("object_id", "kind", "dimension", "frame_id", "data"), ("render",))
            if (obj["object_id"], obj["kind"], obj["dimension"], obj["frame_id"]) != (oid, kind, str(dim), frame):
                raise ValueError("object identity, order or closed-set role mismatch")
            value = obj["data"]
            if oid == "shell":
                _keys(value, ("vertices", "edges", "faces", "seam_edges", "boundary_edges", "boundary_loops", "euler_characteristic"))
                _points(value["vertices"], 18, 3)
                for key, size, width in (("edges", 21, 2), ("seam_edges", 3, 2), ("boundary_edges", 18, 2), ("boundary_loops", 2, 9)):
                    _array(value[key], size, lambda v: _indices(v, width, 18))
                if _int(value["euler_characteristic"]) != 0:
                    raise ValueError("invalid shell Euler characteristic")
                for i, face in enumerate(_array(value["faces"], 3, lambda v: v)):
                    _keys(face, ("face_index", "panel_id", "label", "vertex_indices", "normal"))
                    if (face["face_index"], face["panel_id"], face["label"]) != (str(i), str(i + 1), "ABC"[i]):
                        raise ValueError("face/panel/label mismatch")
                    _indices(face["vertex_indices"], 8, 18)
                    _point(face["normal"], 3)
            elif kind == "section_curve":
                _keys(value, ("height", "segments"))
                if value["height"] != options["section_heights"][int(oid.split(":")[1])]:
                    raise ValueError("section order/height mismatch")
                _segments(value["segments"], 3, 3)
            elif oid == "octagon":
                _keys(value, ("vertices", "outline", "filled_generators", "s", "a", "w", "R_oct", "b"))
                _points(value["vertices"], 8, 2)
                _points(value["filled_generators"], 8, 2)
                _segments(value["outline"], 8, 2)
                for key in ("s", "a", "w", "R_oct", "b"):
                    _decode_exact(value[key])
            elif oid == "scaffold":
                _keys(value, ("vertices", "selected_edges", "connectors", "outline", "side_lengths", "edge_roles",
                              "support_halfplanes", "connector_halfplanes", "area", "circumradius_squared", "q_H", "W",
                              "regularity_residual", "is_regular", "radial", "tangent"))
                _points(value["vertices"], 6, 2)
                for key, size in (("selected_edges", 3), ("connectors", 3), ("outline", 6)):
                    _segments(value[key], size, 2)
                _array(value["side_lengths"], 6, _decode_exact)
                if value["edge_roles"] != ["E", "G"] * 3:
                    raise ValueError("invalid E/G roles")
                for key in ("radial", "tangent"):
                    _points(value[key], 3, 2)
                for key in ("area", "circumradius_squared", "q_H", "W", "regularity_residual"):
                    _decode_exact(value[key])
                if value["is_regular"] is not None:
                    _bool(value["is_regular"])
                for key in ("support_halfplanes", "connector_halfplanes"):
                    for halfplane in _array(value[key], 3, lambda v: v):
                        _keys(halfplane, ("normal", "offset", "relation"))
                        _point(halfplane["normal"], 2)
                        _decode_exact(halfplane["offset"])
                        if halfplane["relation"] != "le":
                            raise ValueError("halfplane must be closed")
            elif kind == "closed_hull":
                _keys(value, ("vertices",))
                _points(value["vertices"], 3, dim)
            else:
                _keys(value, ("frame_index", "centre", "vertices", *(("top_selected_edge",) if dim == 3 else ())))
                if value["frame_index"] != oid.split(":")[1]:
                    raise ValueError("frame index mismatch")
                _point(value["centre"], dim)
                _points(value["vertices"], 8, dim)
                if dim == 3:
                    _points(value["top_selected_edge"], 2, dim)
            if "render" in obj:
                _keys(obj["render"], ("precision_bits", "data"))
                _int(obj["render"]["precision_bits"], 1)
                _render(value, obj["render"]["data"])
        symmetry = data["symmetry"]
        _keys(symmetry, ("group", "qualification", "generators", *(("regular_unlabelled_group", "role_preserving_group",
                                                                  "traversal_preserving_group") if paper == "D" else ())))
        if not isinstance(symmetry["qualification"], str) or not symmetry["qualification"]:
            raise ValueError("missing symmetry qualification")
        if paper == "C":
            if symmetry["group"] != "D3h":
                raise ValueError("wrong shell group")
            for i, generator in enumerate(_array(symmetry["generators"], 3, lambda v: v)):
                _keys(generator, ("name", "vertex_permutation", *(("axis_origin", "axis_direction") if i == 0 else ("plane",))))
                if generator["name"] != ("C3", "sigma_v", "sigma_h")[i]:
                    raise ValueError("wrong shell generator order")
                _indices(generator["vertex_permutation"], 18, 18)
                if i == 0:
                    if tuple(_point(generator["axis_origin"], 3)) != _c.CENTROID:
                        raise ValueError("wrong shell centroid axis")
                    if _point(generator["axis_direction"], 3) != [0, 0, 1]:
                        raise ValueError("wrong shell axis direction")
                elif generator["plane"] != ("x=0" if i == 1 else "z=0"):
                    raise ValueError("wrong mirror plane")
        else:
            regular = objects[1]["data"]["is_regular"] is True
            if (symmetry["group"], symmetry["role_preserving_group"], symmetry["traversal_preserving_group"],
                    symmetry["regular_unlabelled_group"]) != ("D3", "D3", "C3", "D6" if regular else None):
                raise ValueError("wrong scaffold symmetry roles")
            for generator, name in zip(_array(symmetry["generators"], 2, lambda v: v), ("C3", "role_preserving_reflection")):
                _keys(generator, ("name", "vertex_permutation"))
                if generator["name"] != name or generator["vertex_permutation"] is not None:
                    raise ValueError("unsupported scaffold action array")
