"""Exact Paper-D tests; printed-coordinate oracle is independent of the builder."""

import ast
from dataclasses import FrozenInstanceError
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import unittest

import sympy as sp

from kernel_physics import reference_scaffold as rs


def point(values):
    return tuple(sp.expand(sp.radsimp(sp.simplify(x))) for x in values)


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b, strict=True))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b, strict=True))


def det(a, b):
    return a[0]*b[1] - a[1]*b[0]


def edges(vertices):
    return tuple(zip(vertices, vertices[1:] + vertices[:1]))


def edge_set(vertices):
    return {frozenset((point(a), point(b))) for a, b in edges(vertices)}


def rotate(v, angle):
    x, y = v
    return point((sp.cos(angle)*x-sp.sin(angle)*y,
                  sp.sin(angle)*x+sp.cos(angle)*y))


def oracle(s, g_gap):
    # Independent transcription of printed Paper D v0.1.1 equation (11).
    r3 = sp.sqrt(3)
    p = (s+2*g_gap)/(2*r3)
    return ((p, -s/2), (p, s/2),
            ((s-g_gap)/(2*r3), (s+g_gap)/2),
            (-(2*s+g_gap)/(2*r3), g_gap/2),
            (-(2*s+g_gap)/(2*r3), -g_gap/2),
            ((s-g_gap)/(2*r3), -(s+g_gap)/2))


class ReferenceScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s, cls.g_gap = sp.symbols('s g_gap', positive=True)
        cls.model = rs.ReferenceScaffold(cls.s, cls.g_gap)
        cls.h = cls.model.vertices
        cls.d = tuple(sub(b, a) for a, b in edges(cls.h))
        cls.r3 = sp.sqrt(3)

    def assertExact(self, actual, expected=0):
        self.assertEqual(sp.simplify(actual-expected), 0)

    def assertPoint(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for a, b in zip(actual, expected):
            self.assertExact(a, b)

    def test_printed_equation_11_oracle(self):
        for actual, expected in zip(self.h, oracle(self.s, self.g_gap)):
            self.assertPoint(actual, expected)

    def test_radial_and_tangent_frames(self):
        for i, (u, t) in enumerate(zip(rs.RADIAL, rs.TANGENT)):
            phi = 2*sp.pi*i/3
            self.assertPoint(u, (sp.cos(phi), sp.sin(phi)))
            self.assertPoint(t, (-sp.sin(phi), sp.cos(phi)))
            self.assertExact(dot(u, u), 1)
            self.assertExact(dot(t, t), 1)
            self.assertExact(dot(u, t))
            self.assertExact(det(u, t), 1)

    def test_directed_edges_connectors_and_closure(self):
        for i in range(3):
            self.assertPoint(self.d[2*i], tuple(self.s*x for x in rs.TANGENT[i]))
            self.assertPoint(self.d[2*i+1], tuple(self.g_gap*x for x in
                                               rotate(rs.TANGENT[i], sp.pi/3)))
        self.assertPoint(tuple(sum(v[j] for v in self.d) for j in range(2)), (0, 0))
        self.assertEqual(self.model.edge_roles, ('E', 'G')*3)
        self.assertEqual(self.model.outline[::2], self.model.selected_edges)
        self.assertEqual(self.model.outline[1::2], self.model.connectors)

    def test_positive_lengths_turns_and_interior_angles(self):
        for k in range(6):
            lengths = self.model.side_lengths
            self.assertExact(dot(self.d[k], self.d[k]), lengths[k]**2)
            self.assertExact(dot(self.d[k-1], self.d[k]), lengths[k-1]*lengths[k]/2)
            self.assertExact(det(self.d[k-1], self.d[k]), self.r3*self.s*self.g_gap/2)
            self.assertTrue(sp.simplify(det(self.d[k-1], self.d[k])).is_positive)
            self.assertExact(dot(tuple(-v for v in self.d[k-1]), self.d[k]) /
                             (lengths[k-1]*lengths[k]), -sp.Rational(1, 2))

    def test_radius_parameterization_is_exact(self):
        self.assertExact(self.r3*self.model.p-self.s/2, self.g_gap)
        inverse = rs.ReferenceScaffold.from_radius(self.s, (self.s+2*self.g_gap)/(2*self.r3))
        self.assertEqual(inverse, self.model)

    def test_circumcircle_shoelace_and_dissection_area(self):
        for v in self.h:
            self.assertExact(dot(v, v), (self.s**2+self.s*self.g_gap+self.g_gap**2)/3)
            self.assertExact(dot(v, v), self.model.circumradius_squared)
        shoelace = sum(det(a, b) for a, b in edges(self.h))/2
        dissection = self.r3*((self.s+2*self.g_gap)**2-3*self.g_gap**2)/4
        self.assertExact(shoelace, self.model.area)
        self.assertExact(dissection, self.model.area)

    def test_every_vertex_all_halfplanes_and_exact_active_edges(self):
        planes = self.model.support_halfplanes + self.model.connector_halfplanes
        for k, v in enumerate(self.h):
            self.assertIs(self.model.filled_hexagon.contains(v), True)
            active = {j for j, hp in enumerate(planes) if hp.slack(v) == 0}
            i = k//2
            expected = {i, 3+((i-1) % 3 if k % 2 == 0 else i)}
            self.assertEqual(active, expected)
            for j, hp in enumerate(planes):
                if j not in active:
                    self.assertTrue(hp.slack(v).is_positive)
        for i, (a, b) in enumerate(self.model.selected_edges):
            self.assertExact(self.model.support_halfplanes[i].slack(a))
            self.assertExact(self.model.support_halfplanes[i].slack(b))
        for i, (a, b) in enumerate(self.model.connectors):
            self.assertExact(self.model.connector_halfplanes[i].slack(a))
            self.assertExact(self.model.connector_halfplanes[i].slack(b))

    def test_connector_retention_apex_and_outer_leg_exclusion(self):
        t = sp.symbols('t', real=True, nonnegative=True)
        # A bounded parameter is explicit: t in [0,1] is proved by a convex
        # combination of endpoint slacks, not assumed by SymPy for arbitrary t.
        for i, (b, a) in enumerate(self.model.connectors):
            middle = tuple((x+y)/2 for x, y in zip(b, a))
            self.assertIs(self.model.filled_hexagon.contains(middle), True)
            hp = self.model.connector_halfplanes[i]
            self.assertExact(hp.slack(tuple((1-t)*x+t*y for x, y in zip(b, a))))
            v = self.model.support_vertices[i]
            self.assertExact(hp.slack(v), -self.r3*self.g_gap/2)
            self.assertIs(self.model.filled_hexagon.contains(v), False)
            for endpoint in (b, a):
                leg = tuple((x+y)/2 for x, y in zip(endpoint, v))
                self.assertExact(hp.slack(leg), -self.r3*self.g_gap/4)
                self.assertIs(self.model.filled_hexagon.contains(leg), False)

    def test_support_triangle_and_equilateral_corner_cells(self):
        v = self.model.support_vertices
        for actual, expected in zip(self.model.support_triangle.vertices, v):
            self.assertPoint(actual, expected)
        self.assertExact(self.model.W, 2*self.r3*self.model.p)
        for i, vertex in enumerate(v):
            for j, hp in enumerate(self.model.support_halfplanes):
                self.assertExact(hp.slack(vertex), 0 if j in (i, (i+1) % 3) else 3*self.model.p)
        for a, b in edges(v):
            self.assertExact(dot(sub(a, b), sub(a, b)), self.model.W**2)
        for i, cell in enumerate(self.model.corner_cells):
            for actual, expected in zip(cell.vertices, (self.model.B[i], v[i], self.model.A[(i+1) % 3])):
                self.assertPoint(actual, expected)
            for a, b in edges(cell.vertices):
                self.assertExact(dot(sub(a, b), sub(a, b)), self.g_gap**2)

    def test_global_convex_support_nonoverlap_certificate(self):
        # The three corner barycentric thresholds exceed 1/2, so two corner
        # cells cannot overlap. Positive leftover support lengths give six edges.
        threshold = 1-self.g_gap/self.model.W
        self.assertExact(threshold-sp.Rational(1, 2), self.s/(2*self.model.W))
        self.assertTrue(sp.simplify(threshold-sp.Rational(1, 2)).is_positive)
        self.assertExact(self.model.W-2*self.g_gap, self.s)
        self.assertIs(self.model.filled_hexagon.contains((0, 0)), True)
        self.assertTrue(all(hp.slack((0, 0)).is_positive for hp in self.model.filled_hexagon.halfplanes))

    def test_regular_member_metrics_and_unknown_equality(self):
        m = rs.ReferenceScaffold.regular(self.s)
        self.assertIs(m.is_regular, True)
        self.assertEqual(m.side_lengths, (self.s,)*6)
        self.assertExact(m.p, self.r3*self.s/2)
        self.assertExact(m.q_H, m.p)
        self.assertExact(m.circumradius_squared, self.s**2)
        self.assertExact(m.area, 3*self.r3*self.s**2/2)
        self.assertIs(self.model.is_regular, None)
        self.assertExact(self.model.regularity_residual, self.g_gap-self.s)
        self.assertExact(self.model.p-self.model.q_H, (self.g_gap-self.s)/(2*self.r3))
        self.assertIs(rs.ReferenceScaffold(self.s, 2*self.s).is_regular, False)

    def test_c3_covariance_and_reflection(self):
        for k, v in enumerate(self.h):
            self.assertPoint(rotate(v, 2*sp.pi/3), self.h[(k+2) % 6])
        reflection = lambda v: point((v[0], -v[1]))
        for edge_class in (self.model.selected_edges, self.model.connectors):
            reflected = {frozenset(reflection(v) for v in e) for e in edge_class}
            self.assertEqual(reflected, {frozenset(point(v) for v in e) for e in edge_class})

    def test_regular_d6_role_d3_and_traversal_c3(self):
        m = rs.ReferenceScaffold.regular(1);vertices = tuple(point(v) for v in m.vertices)
        perms = set();role_preserving = [];oriented_role = []
        for reflected in (False, True):
            for k in range(6):
                image = [rotate((v[0], -v[1]) if reflected else v, k*sp.pi/3) for v in vertices]
                perm = tuple(vertices.index(v) for v in image);perms.add(perm)
                e_images = {frozenset((perm[2*i], perm[2*i+1])) for i in range(3)}
                if e_images == {frozenset((2*i, 2*i+1)) for i in range(3)}:
                    role_preserving.append(perm)
                    if not reflected:oriented_role.append(perm)
        self.assertEqual((len(perms), len(role_preserving), len(oriented_role)), (12, 6, 3))
        fixed_labels = [p for p in role_preserving if all(
            {p[2*i], p[2*i+1]} == {2*i, 2*i+1} for i in range(3))]
        self.assertEqual(fixed_labels, [tuple(range(6))])
        self.assertEqual({frozenset(rotate(v, sp.pi/3) for v in e) for e in m.selected_edges},
                         {frozenset(point(v) for v in e) for e in m.connectors})
        centres = {point(v) for v in m.planar_centres}
        self.assertNotEqual({rotate(v, sp.pi/3) for v in centres}, centres)

    def test_exact_nonregular_witnesses(self):
        for side, gap in ((2, 1), (sp.Rational(2, 3), sp.Rational(5, 4)), (sp.sqrt(2), 1)):
            m = rs.ReferenceScaffold(side, gap)
            for a, b in zip(m.vertices, oracle(sp.sympify(side), sp.sympify(gap))):
                self.assertPoint(a, b)
            self.assertIs(m.is_regular, False)
            self.assertNotEqual({rotate(v, sp.pi/3) for v in m.vertices}, {point(v) for v in m.vertices})

    def test_octagon_metrics_edges_and_filled_outline_distinction(self):
        o = rs.Octagon(self.s)
        self.assertExact(o.a, (1+sp.sqrt(2))*self.s/2)
        self.assertExact(o.w, 2*o.a)
        self.assertExact(o.b, self.s/2)
        self.assertEqual(len(o.vertices), 8)
        self.assertEqual(o.outline[-1], (o.vertices[-1], o.vertices[0]))
        self.assertIsInstance(o.filled, rs.ConvexHull)
        self.assertEqual(o.filled.vertices, o.vertices)
        for a, b in o.outline:
            self.assertExact(dot(sub(b, a), sub(b, a)), self.s**2)
            self.assertExact(dot(a, a), o.R_oct**2)
        self.assertTrue(sp.simplify(sum(det(a, b) for a, b in o.outline)).is_positive)

    def test_complete_planar_frames_and_inward_outline_reversal(self):
        frames = self.model.planar_frames
        for i, frame in enumerate(frames):
            self.assertPoint(frame.vertices[5], self.model.A[i])
            self.assertPoint(frame.vertices[4], self.model.B[i])
            for a, b in edges(frame.vertices):
                self.assertExact(dot(sub(b, a), sub(b, a)), self.s**2)
            for k, v in enumerate(frame.vertices):
                self.assertPoint(rotate(v, 2*sp.pi/3), frames[(i+1) % 3].vertices[k])
            average = tuple(sum(v[j] for v in frame.vertices)/8 for j in range(2))
            self.assertPoint(average, self.model.planar_centres[i])
        self.assertExact(self.model.L-self.model.p, self.model.octagon.a)
        self.assertExact(rs.ReferenceScaffold.regular(self.s).L, (1+sp.sqrt(2)+self.r3)*self.s/2)

    def test_vertical_family_full_domain_and_top_height(self):
        xi, z = sp.symbols('xi z', real=True)
        for i, frame in enumerate(self.model.vertical_frames):
            self.assertPoint(self.model.vertical_point(i, xi, z),
                             (self.model.p*rs.RADIAL[i][0]+xi*rs.TANGENT[i][0],
                              self.model.p*rs.RADIAL[i][1]+xi*rs.TANGENT[i][1], z))
            self.assertPoint(tuple(sum(v[j] for v in frame.vertices)/8 for j in range(3)),
                             self.model.vertical_centres[i])
            for actual, expected in zip(self.model.top_selected_edges[i], (self.model.A[i], self.model.B[i])):
                self.assertPoint(actual[:2], expected)
                self.assertExact(actual[2], self.model.octagon.a)
            for a, b in edges(frame.vertices):
                self.assertExact(dot(sub(b, a), sub(b, a)), self.s**2)

    def test_paper_c_rigid_formula_and_finite_vertex_edge_sets(self):
        from kernel_physics import geometry
        s = sp.sqrt(2)-1;m = rs.paper_c_member(s);mesh = geometry.folded_module()
        self.assertExact(m.octagon.a, sp.Rational(1, 2))
        self.assertExact(m.p, 1/(2*self.r3))
        self.assertExact(m.g_gap/m.s, 1/sp.sqrt(2))
        xi, z = sp.symbols('xi z', real=True)
        for i, panel in enumerate((3, 1, 2)):
            self.assertPoint(rs.paper_c_rigid_map(m.vertical_point(i, xi, z), s),
                             geometry.panel_point(panel, xi, z))
            mapped = tuple(point(rs.paper_c_rigid_map(v, s)) for v in m.vertical_frames[i].vertices)
            old = tuple(point(geometry.panel_point(panel, x, z)) for x, z in geometry.LOCAL_OCTAGON)
            self.assertEqual(mapped, old[3:]+old[:3])
            self.assertEqual(set(mapped), {point(mesh.vertices[v]) for v in mesh.faces[panel-1]})
            self.assertEqual(edge_set(mapped), edge_set(old))
        self.assertEqual(len(m.vertices), 6)
        self.assertEqual(tuple(map(len, mesh.boundary_loops)), (9, 9))
        self.assertGreater(len({mesh.vertices[v][2] for v in mesh.boundary_loops[1]}), 1)

    def test_translation_and_shrink_have_distinct_consequences(self):
        old = rs.paper_c_member(self.s)
        moved = rs.translate_paper_c_to_regular(self.s)
        shrunk = rs.shrink_paper_c_at_fixed_centres(self.s)
        lam = sp.symbols('lambda', positive=True)
        solution = sp.solve(self.r3*old.p-lam*self.s/2-lam*self.s, lam)
        self.assertEqual(solution, [rs.PAPER_C_SHRINK_FACTOR])
        self.assertExact(moved.p-old.p, (2-sp.sqrt(2))*self.s/(2*self.r3))
        self.assertEqual(moved.s, old.s)
        self.assertExact(moved.octagon.a, old.octagon.a)
        self.assertExact(shrunk.p, old.p)
        self.assertExact(shrunk.s, rs.PAPER_C_SHRINK_FACTOR*self.s)
        self.assertIs(shrunk.is_regular, True)
        for i in range(3):
            centre = old.vertical_centres[i]
            for before, after in zip(old.vertical_frames[i].vertices, shrunk.vertical_frames[i].vertices):
                self.assertPoint(sub(after, centre), tuple(rs.PAPER_C_SHRINK_FACTOR*x for x in sub(before, centre)))
        # Shrinking about fixed planar centres would move the selected midpoint.
        self.assertTrue(sp.simplify(old.L-rs.PAPER_C_SHRINK_FACTOR*old.octagon.a-old.p).is_positive)

    def test_width_one_fixed_centre_shrink(self):
        m = rs.shrink_paper_c_at_fixed_centres(sp.sqrt(2)-1)
        for length in m.side_lengths:
            self.assertExact(length, sp.Rational(1, 3))
        self.assertExact(m.p, 1/(2*self.r3))
        self.assertExact(m.W, 1)
        self.assertExact(m.octagon.w, (1+sp.sqrt(2))/3)
        self.assertExact(m.octagon.a, (1+sp.sqrt(2))/6)
        self.assertExact(m.area, self.r3/6)
        self.assertExact(m.circumradius_squared, sp.Rational(1, 9))
        self.assertTrue((sp.Rational(1, 2)-m.octagon.a).is_positive)

    def test_global_similarity_preserves_gap_ratio(self):
        c = sp.symbols('c', positive=True)
        scaled = rs.ReferenceScaffold.from_radius(c*self.s, c*self.model.p)
        self.assertExact(scaled.g_gap/scaled.s, self.g_gap/self.s)
        self.assertExact(scaled.area, c*c*self.model.area)
        self.assertEqual(rs.paper_c_member(self.s).is_regular, False)

    def test_plane_intersection_distance_decomposition_and_attaining_pair(self):
        # Parameterization p=(a+delta)/sqrt(3) enforces the printed domain.
        delta, X, Y = sp.symbols('delta X Y', nonnegative=True)
        z, zp = sp.symbols('z zp', real=True)
        a = rs.Octagon(self.s).a
        m = rs.ReferenceScaffold.from_radius(self.s, (a+delta)/self.r3)
        local = m.octagon.vertices
        self.assertPoint(tuple((x+y)/2 for x, y in zip(local[0], local[1])), (a, 0))
        self.assertPoint(tuple((x+y)/2 for x, y in zip(local[4], local[5])), (-a, 0))
        for i in range(3):
            j = (i+1) % 3
            self.assertPoint(m.vertical_point(i, self.r3*m.p, z),
                             m.vertical_point(j, -self.r3*m.p, z))
            d = sub(m.vertical_point(i, a-X, z), m.vertical_point(j, -a+Y, zp))
            self.assertExact(dot(d, d), delta**2+delta*(X+Y)+(X-Y)**2+X*Y+(z-zp)**2)
            # (a,0),(-a,0) lie on the finite side segments, so the bound is attained.
            dmin = sub(m.vertical_point(i, a, 0), m.vertical_point(j, -a, 0))
            self.assertExact(dot(dmin, dmin), delta**2)
        old = rs.paper_c_member(self.s)
        for z0 in (-self.s/2, 0, self.s/2):
            self.assertPoint(old.vertical_point(0, a, z0), old.vertical_point(1, -a, z0))
        moved = rs.translate_paper_c_to_regular(self.s)
        self.assertExact(self.r3*moved.p-moved.octagon.a, (2-sp.sqrt(2))*self.s/2)
        shrunk = rs.shrink_paper_c_at_fixed_centres(sp.sqrt(2)-1)
        self.assertExact(self.r3*shrunk.p-shrunk.octagon.a, (2-sp.sqrt(2))/6)

    def test_exact_input_types_and_rejected_domains(self):
        self.assertEqual(rs.ReferenceScaffold(Fraction(1, 3), 2).s, sp.Rational(1, 3))
        for value in (True, False, sp.true, 1.0, sp.Float(1), '1', 1+0j, None, [1], float('nan')):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                rs.ReferenceScaffold(value, 1)
            with self.subTest(gap=value), self.assertRaises((TypeError, ValueError)):
                rs.ReferenceScaffold(1, value)
        for value in (0, -1, sp.oo, -sp.oo, sp.nan, sp.zoo, sp.I, sp.Symbol('x'), sp.Symbol('r', real=True)):
            with self.subTest(value=value), self.assertRaises(ValueError):
                rs.Octagon(value)
        for radius in (0, -1, self.s/(2*self.r3), self.s/(4*self.r3), sp.Symbol('p', positive=True)):
            with self.subTest(radius=radius), self.assertRaises(ValueError):
                rs.ReferenceScaffold.from_radius(self.s, radius)
        with self.assertRaises(TypeError):
            rs.ReferenceScaffold(self.s+sp.Float('.1'), 1)

    def test_membership_unknown_and_coordinate_index_validation(self):
        x = sp.symbols('x', real=True)
        self.assertIs(self.model.filled_hexagon.contains((x, 0)), None)
        for bad in (True, 0.0, '0'):
            with self.assertRaises(TypeError):self.model.vertical_point(bad, 0, 0)
        for bad in (-1, 3):
            with self.assertRaises(IndexError):self.model.planar_point(bad, 0, 0)
        with self.assertRaises(ValueError):self.model.filled_hexagon.contains((0, 0, 0))
        with self.assertRaises(ValueError):self.model.vertical_point(0, sp.I, 0)
        with self.assertRaises(TypeError):rs.paper_c_rigid_map((0, 0, 0.0), 1)
        with self.assertRaises(ValueError):rs.HalfPlane((0, 0), 1)

    def test_immutable_representations_and_input_preservation(self):
        vertices = [[0, 0], [1, 0], [0, 1]]
        h = rs.ConvexHull(vertices);vertices[0][0] = 8
        self.assertEqual(h.vertices[0], (0, 0))
        normal = [1, 0];hp = rs.HalfPlane(normal, 1);normal[0] = 7
        self.assertEqual(hp.normal, (1, 0))
        for obj, attr, val in ((self.model, 's', 2), (rs.Octagon(1), 's', 2),
                               (h, 'vertices', ()), (hp, 'offset', 2),
                               (self.model.filled_hexagon, 'halfplanes', ())):
            with self.assertRaises(FrozenInstanceError):setattr(obj, attr, val)
        with self.assertRaises(TypeError):self.h[0][0] = 3
        self.assertEqual(rs.ReferenceScaffold(self.s, self.g_gap), self.model)
        self.assertEqual(hash(rs.ReferenceScaffold(self.s, self.g_gap)), hash(self.model))
        self.assertEqual(rs.ReferenceScaffold(self.s, self.g_gap).vertices, self.h)

    def test_runtime_import_boundary_and_no_hidden_model_import(self):
        tree = ast.parse(Path(rs.__file__).read_text())
        imported = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
        imported |= {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
        self.assertEqual(imported, {'dataclasses', 'fractions', 'sympy'})
        code = ('import sys; import kernel_physics.reference_scaffold as r; '
                'r.ReferenceScaffold.regular(1).vertical_frames; '
                'assert not any(n in sys.modules for n in '
                '["kernel_physics.geometry", "kernel_physics.dynamics", '
                '"kernel_physics.face_state", "kernel_physics.readouts"])')
        result = subprocess.run([sys.executable, '-B', '-c', code], cwd=Path(rs.__file__).parents[1],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_existing_geometry_and_dynamics_remain_deterministic(self):
        import numpy as np
        from kernel_physics import geometry, dynamics
        mesh = geometry.folded_module()
        omega = np.array([.2+.1j, -.4+.3j, .1-.2j]);original = omega.copy()
        cfg = dynamics.DynamicsConfig(eps=.05, g=.2, phase_strength=.001, k=(1., 1., 1.))
        before = dynamics.step3(omega, cfg)
        for m in (rs.ReferenceScaffold.regular(1), rs.paper_c_member(1), rs.shrink_paper_c_at_fixed_centres(1)):
            m.vertical_frames;m.planar_frames;m.filled_hexagon.contains((0, 0))
        self.assertEqual(mesh, geometry.folded_module())
        self.assertEqual(before.tobytes(), dynamics.step3(omega, cfg).tobytes())
        self.assertEqual(original.tobytes(), omega.tobytes())


class SymbolicDomainRegressionTests(unittest.TestCase):
    """R1: specialize returned coordinates before checking their identities.

    Do not use the older point() normalizer or simplify a symbolic difference
    before substitution: either could hide a newly introduced singularity.
    """

    @classmethod
    def setUpClass(cls):
        cls.x = sp.Symbol('x', positive=True)
        cls.length = 1/(1+sp.sqrt(cls.x))
        cls.half = sp.Rational(1, 2)

    def assertSpecializedPoint(self, returned, expected, symbol=None, value=1):
        symbol = self.x if symbol is None else symbol
        # First operation on each returned coordinate is the valid substitution.
        specialized = tuple(c.subs(symbol, value) for c in returned)
        self.assertEqual(len(specialized), len(expected))
        for actual, target in zip(specialized, expected):
            self.assertIs(actual.is_real, True)
            self.assertIs(actual.is_finite, True)
            self.assertFalse(actual.has(sp.nan, sp.zoo, sp.oo, -sp.oo, sp.Float))
            # Compare only after checking the specialized point's actual domain.
            self.assertEqual(sp.simplify(actual-target), 0)

    def assertSpecializedPoints(self, returned, expected, **kwargs):
        self.assertEqual(len(returned), len(expected))
        for actual, target in zip(returned, expected):
            self.assertSpecializedPoint(actual, target, **kwargs)

    def test_regular_composite_length_substitution_first(self):
        self.assertIs(self.length.is_real, True)
        self.assertIs(self.length.is_finite, True)
        self.assertIs(self.length.is_positive, True)
        m = rs.ReferenceScaffold.regular(self.length)
        self.assertSpecializedPoint(m.vertices[0], (sp.sqrt(3)/4, -sp.Rational(1, 4)))
        self.assertSpecializedPoints(m.vertices, rs.ReferenceScaffold.regular(self.half).vertices)
        self.assertSpecializedPoints(m.vertices, oracle(self.half, self.half))

    def test_nonregular_composite_side_substitution_first(self):
        m = rs.ReferenceScaffold(self.length, 1)
        self.assertSpecializedPoints(m.vertices, rs.ReferenceScaffold(self.half, 1).vertices)
        self.assertSpecializedPoints(m.vertices, oracle(self.half, sp.S.One))

    def test_nonregular_composite_gap_substitution_first(self):
        m = rs.ReferenceScaffold(1, self.length)
        self.assertSpecializedPoints(m.vertices, rs.ReferenceScaffold(1, self.half).vertices)
        self.assertSpecializedPoints(m.vertices, oracle(sp.S.One, self.half))

    def test_generated_symbolic_vertices_self_membership(self):
        for m in (rs.ReferenceScaffold.regular(self.length),
                  rs.ReferenceScaffold(self.length, 1), rs.ReferenceScaffold(1, self.length)):
            region = m.filled_hexagon
            for v in m.vertices:
                # This asks about the symbolic returned point, not just its x=1 image.
                self.assertIs(region.contains(v), True)

    def test_complete_planar_frames_composite_length(self):
        m = rs.ReferenceScaffold.regular(self.length)
        rebuilt = rs.ReferenceScaffold.regular(self.half)
        self.assertSpecializedPoints(m.planar_centres, rebuilt.planar_centres)
        for actual, target in zip(m.planar_frames, rebuilt.planar_frames):
            self.assertIsInstance(actual, rs.ConvexHull)
            self.assertSpecializedPoints(actual.vertices, target.vertices)
        self.assertSpecializedPoints(m.octagon.filled.vertices, rebuilt.octagon.filled.vertices)

    def test_vertical_local_coordinate_substitution_first(self):
        m = rs.ReferenceScaffold.regular(1)
        for i in range(3):
            actual = m.vertical_point(i, self.length, -self.length)
            expected = m.vertical_point(i, self.half, -self.half)
            self.assertSpecializedPoint(actual, expected)
        self.assertSpecializedPoint(m.vertical_point(0, self.length, 0),
                                    (sp.sqrt(3)/2, self.half, sp.S.Zero))

    def test_planar_local_coordinate_substitution_first(self):
        m = rs.ReferenceScaffold.regular(1)
        for i in range(3):
            actual = m.planar_point(i, self.length, -self.length)
            expected = m.planar_point(i, self.half, -self.half)
            self.assertSpecializedPoint(actual, expected)
        self.assertSpecializedPoint(m.planar_point(0, 0, self.length),
                                    ((1+sp.sqrt(2)+sp.sqrt(3))/2, self.half))

    def test_rigid_map_local_coordinate_substitution_first(self):
        actual = rs.paper_c_rigid_map((self.length, -self.length, self.length), 1)
        expected = rs.paper_c_rigid_map((self.half, -self.half, self.half), 1)
        self.assertSpecializedPoint(actual, expected)
        self.assertSpecializedPoint(rs.paper_c_rigid_map((self.length, 0, 0), 1),
                                    (sp.sqrt(3)/4, sp.Rational(1, 4)+(1+sp.sqrt(2))/(2*sp.sqrt(3)), sp.S.Zero))

    def test_support_vertices_corner_cells_and_boundaries(self):
        m = rs.ReferenceScaffold(1, self.length)
        rebuilt = rs.ReferenceScaffold(1, self.half)
        self.assertSpecializedPoints(m.support_vertices, rebuilt.support_vertices)
        self.assertSpecializedPoints(m.support_triangle.vertices, rebuilt.support_triangle.vertices)
        for cell, target in zip(m.corner_cells, rebuilt.corner_cells):
            self.assertSpecializedPoints(cell.vertices, target.vertices)
        for group, targets in ((m.selected_edges, rebuilt.selected_edges),
                               (m.connectors, rebuilt.connectors), (m.outline, rebuilt.outline)):
            for actual, target in zip(group, targets):
                self.assertSpecializedPoints(actual, target)
        for hp, target in zip(m.filled_hexagon.halfplanes, rebuilt.filled_hexagon.halfplanes):
            self.assertSpecializedPoint((*hp.normal, hp.offset), (*target.normal, target.offset))

    def test_vertical_reference_frames_centres_and_top_edges(self):
        m = rs.ReferenceScaffold(self.length, 1)
        rebuilt = rs.ReferenceScaffold(self.half, 1)
        self.assertSpecializedPoints(m.vertical_centres, rebuilt.vertical_centres)
        for frame, target in zip(m.vertical_frames, rebuilt.vertical_frames):
            self.assertSpecializedPoints(frame.vertices, target.vertices)
        for edge, target in zip(m.top_selected_edges, rebuilt.top_selected_edges):
            self.assertSpecializedPoints(edge, target)

    def test_named_paper_c_constructions_composite_length(self):
        for factory in (rs.paper_c_member, rs.translate_paper_c_to_regular,
                        rs.shrink_paper_c_at_fixed_centres):
            with self.subTest(factory=factory.__name__):
                m, rebuilt = factory(self.length), factory(self.half)
                self.assertSpecializedPoints(m.vertices, rebuilt.vertices)
                self.assertSpecializedPoints(m.vertical_centres, rebuilt.vertical_centres)
                for frame, target in zip(m.vertical_frames, rebuilt.vertical_frames):
                    self.assertSpecializedPoints(frame.vertices, target.vertices)
                self.assertIs(m.filled_hexagon.contains(m.vertices[0]), True)
        original = rs.paper_c_member(self.length)
        numeric = rs.paper_c_member(self.half)
        mapped = rs.paper_c_rigid_map(original.vertical_frames[0].vertices[0], self.length)
        self.assertSpecializedPoint(mapped, rs.paper_c_rigid_map(numeric.vertical_frames[0].vertices[0], self.half))

    def test_second_exact_witness_no_parameter_special_case(self):
        rho = sp.Symbol('rho', positive=True)
        side = 1/(2+sp.sqrt(rho))
        m = rs.ReferenceScaffold.regular(side)
        self.assertSpecializedPoints(m.vertices, oracle(sp.Rational(1, 4), sp.Rational(1, 4)),
                                     symbol=rho, value=4)
        self.assertIs(m.filled_hexagon.contains(m.vertices[0]), True)


if __name__ == '__main__':
    unittest.main()
