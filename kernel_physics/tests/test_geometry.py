import unittest
from collections import Counter
from itertools import combinations

import sympy as sp

from kernel_physics.geometry import (
    CENTROID, EDGE_LENGTH, FOLD_ANGLE, LOCAL_OCTAGON, WIDTH, central_section,
    folded_module, panel_point, reflect_horizontal, reflect_vertical, rotate_c3,
)


class GeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mesh = folded_module()

    def assertExact(self, actual, expected):
        self.assertEqual(sp.simplify(actual - expected), 0)

    def assertPoint(self, actual, expected):
        for a, b in zip(actual, expected, strict=True):
            self.assertExact(a, b)

    def test_width_one_normalization(self):
        self.assertEqual(WIDTH, 1)
        self.assertExact(EDGE_LENGTH, sp.sqrt(2) - 1)
        self.assertExact((1 + sp.sqrt(2)) * EDGE_LENGTH, WIDTH)
        self.assertEqual(FOLD_ANGLE, sp.pi / 3)

    def test_local_octagon_has_eight_equal_edges(self):
        self.assertEqual(len(LOCAL_OCTAGON), 8)
        for a, b in zip(LOCAL_OCTAGON, LOCAL_OCTAGON[1:] + LOCAL_OCTAGON[:1]):
            self.assertExact(sum((x - y) ** 2 for x, y in zip(a, b)),
                             (sp.sqrt(2) - 1) ** 2)
        self.assertEqual(max(p[0] for p in LOCAL_OCTAGON)
                         - min(p[0] for p in LOCAL_OCTAGON), 1)

    def test_all_18_vertices_match_printed_table(self):
        # Independent transcription of Paper C §4, not builder output.
        h, r2, r3, r6 = sp.Rational(1, 2), sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
        expected = (
            (0, r3/2, h-r2/2), (-h+r2/4, r6/4, -h),
            (-r2/4, r3/2-r6/4, -h), (-h, 0, h-r2/2),
            (-h, 0, -h+r2/2), (-r2/4, r3/2-r6/4, h),
            (-h+r2/4, r6/4, h), (0, r3/2, -h+r2/2),
            (h-r2/2, 0, -h), (-h+r2/2, 0, -h),
            (h, 0, h-r2/2), (h, 0, -h+r2/2),
            (-h+r2/2, 0, h), (h-r2/2, 0, h),
            (r2/4, r3/2-r6/4, -h), (h-r2/4, r6/4, -h),
            (h-r2/4, r6/4, h), (r2/4, r3/2-r6/4, h),
        )
        self.assertEqual(len(self.mesh.vertices), 18)
        for actual, printed in zip(self.mesh.vertices, expected, strict=True):
            self.assertPoint(actual, printed)
        self.assertFalse(any(x.has(sp.Float) for p in self.mesh.vertices for x in p))

    def test_three_printed_octagonal_face_cycles(self):
        self.assertEqual(self.mesh.faces, (
            (0, 1, 2, 3, 4, 5, 6, 7),
            (3, 8, 9, 10, 11, 12, 13, 4),
            (10, 14, 15, 0, 7, 16, 17, 11),
        ))

    def test_21_edges_and_three_seams(self):
        self.assertEqual(len(self.mesh.edges), 21)
        self.assertEqual(self.mesh.seam_edges, ((0, 7), (3, 4), (10, 11)))
        for a, b in self.mesh.edges:
            self.assertExact(sum((x-y)**2 for x, y in
                                 zip(self.mesh.vertices[a], self.mesh.vertices[b])),
                             (sp.sqrt(2)-1)**2)

    def test_euler_characteristic_zero(self):
        self.assertEqual(self.mesh.euler_characteristic, 0)

    def test_two_nine_edge_boundary_components(self):
        bottom = (0, 1, 2, 3, 8, 9, 10, 14, 15)
        top = (4, 5, 6, 7, 16, 17, 11, 12, 13)
        self.assertEqual(self.mesh.boundary_loops, (bottom, top))
        self.assertTrue(set(bottom).isdisjoint(top))
        edges = {tuple(sorted((loop[i], loop[(i+1) % 9])))
                 for loop in (bottom, top) for i in range(9)}
        self.assertEqual(edges, set(self.mesh.boundary_edges))
        self.assertTrue(all(self.mesh.vertices[i][2] < 0 for i in bottom))
        self.assertTrue(all(self.mesh.vertices[i][2] > 0 for i in top))

    def test_seams_have_opposite_oriented_incidence(self):
        directed = Counter((face[i], face[(i+1) % 8])
                           for face in self.mesh.faces for i in range(8))
        for a, b in self.mesh.seam_edges:
            self.assertEqual(directed[a, b], 1)
            self.assertEqual(directed[b, a], 1)

    def test_symbolic_free_edge_closure_and_nonclosing_angles(self):
        z, beta = sp.symbols("z beta", real=True)
        left = panel_point(1, -sp.Rational(1, 2), z, beta)
        right = panel_point(3, sp.Rational(1, 2), z, beta)
        self.assertPoint(tuple(b-a for a, b in zip(left, right)),
                         (1-2*sp.cos(beta), 0, 0))
        self.assertPoint(tuple(v.subs(beta, sp.pi/3) for v in left),
                         (0, sp.sqrt(3)/2, z))
        self.assertPoint(tuple(v.subs(beta, sp.pi/3) for v in left),
                         tuple(v.subs(beta, sp.pi/3) for v in right))
        for angle in (0, sp.pi/2):
            self.assertNotEqual(sp.simplify((right[0]-left[0]).subs(beta, angle)), 0)

    def test_hinges_fixed_for_general_angle(self):
        z, beta = sp.symbols("z beta", real=True)
        self.assertPoint(panel_point(1, sp.Rational(1, 2), z, beta),
                         (-sp.Rational(1, 2), 0, z))
        self.assertPoint(panel_point(3, -sp.Rational(1, 2), z, beta),
                         (sp.Rational(1, 2), 0, z))

    def test_central_section_is_unit_equilateral_curve(self):
        for height in (0, EDGE_LENGTH/2, -EDGE_LENGTH/2):
            segments = central_section(height)
            self.assertEqual(len(segments), 3)
            for i, (a, b) in enumerate(segments):
                self.assertPoint(b, segments[(i+1) % 3][0])
                self.assertExact(sum((x-y)**2 for x, y in zip(a, b)), 1)
                self.assertEqual(a[2], height)
            # Panel endpoint images must give the same curve.
            actual = {frozenset(segment) for segment in segments}
            panel_sections = {
                frozenset((panel_point(p, -sp.Rational(1, 2), height),
                           panel_point(p, sp.Rational(1, 2), height)))
                for p in (1, 2, 3)
            }
            self.assertEqual(actual, panel_sections)
            center = sp.ImmutableMatrix((0, sp.sqrt(3)/6, height))
            for i, face in enumerate(self.mesh.faces):
                normal = sp.ImmutableMatrix(self.mesh.face_normal(i))
                anchor = sp.ImmutableMatrix(self.mesh.vertices[face[0]])
                self.assertNotEqual(sp.simplify(normal.dot(center-anchor)), 0)

    def test_outward_normals_from_coordinates(self):
        expected = ((-sp.sqrt(3)/2, sp.Rational(1, 2), 0),
                    (0, -1, 0), (sp.sqrt(3)/2, sp.Rational(1, 2), 0))
        for i in range(3):
            self.assertPoint(self.mesh.face_normal(i), expected[i])
            normal = sp.ImmutableMatrix(self.mesh.face_normal(i))
            center = sum((sp.ImmutableMatrix(self.mesh.vertices[v])
                          for v in self.mesh.faces[i]), sp.zeros(3, 1)) / 8
            self.assertTrue(sp.simplify(normal.dot(center-sp.Matrix(CENTROID))) > 0)

    def test_interior_60_and_normal_120_degrees(self):
        for i, j in combinations(range(3), 2):
            self.assertExact(self.mesh.normal_separation(i, j), 2*sp.pi/3)
            self.assertExact(self.mesh.interior_dihedral(i, j), sp.pi/3)

    def test_d3h_generators_preserve_edges_and_whole_faces(self):
        vertices = self.mesh.vertices
        face_sets = {frozenset(f) for f in self.mesh.faces}
        edge_set = set(self.mesh.edges)
        for transform in (rotate_c3, reflect_vertical, reflect_horizontal):
            perm = tuple(vertices.index(transform(p)) for p in vertices)
            self.assertEqual(set(perm), set(range(18)))
            self.assertEqual({frozenset(perm[v] for v in f) for f in self.mesh.faces},
                             face_sets)
            self.assertEqual({tuple(sorted((perm[a], perm[b]))) for a, b in edge_set},
                             edge_set)

    def test_d3h_generator_relations_and_twelve_actions(self):
        vertices = self.mesh.vertices
        identity = tuple(range(18))
        r, v, h = [tuple(vertices.index(fn(p)) for p in vertices)
                   for fn in (rotate_c3, reflect_vertical, reflect_horizontal)]
        compose = lambda a, b: tuple(a[b[i]] for i in range(18))
        r2 = compose(r, r)
        self.assertNotEqual(r, identity)
        self.assertEqual(compose(r, r2), identity)
        self.assertEqual(compose(v, v), identity)
        self.assertEqual(compose(h, h), identity)
        self.assertEqual(compose(v, compose(r, v)), r2)
        self.assertEqual(compose(h, r), compose(r, h))
        actions = {compose(a, compose(b, c))
                   for a in (identity, r, r2) for b in (identity, v)
                   for c in (identity, h)}
        self.assertEqual(len(actions), 12)

    def test_section_domain_and_panel_validation(self):
        for height in (sp.Rational(1, 2), -sp.Rational(1, 2), sp.I):
            with self.assertRaises(ValueError):
                central_section(height)
        with self.assertRaises(ValueError):
            panel_point(4, 0, 0)


if __name__ == "__main__":
    unittest.main()
