from dataclasses import FrozenInstanceError
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

from kernel_physics import dynamics as dy, face_state as fs, geometry as geo
from kernel_physics import operating_region as region, readouts
from kernel_physics.boundary_response import ResponsePrecisionError


class FaceStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mesh = geo.folded_module()
        cls.n = [sp.Matrix(cls.mesh.face_normal(i)) for i in range(3)]
        cls.ez = sp.Matrix([0, 0, 1])
        cls.t = [cls.ez.cross(n) for n in cls.n]
        cls.c = [sum((sp.Matrix(cls.mesh.vertices[v]) for v in face), sp.zeros(3, 1))/8
                 for face in cls.mesh.faces]
        cls.R = sp.Matrix([[-sp.Rational(1, 2), -sp.sqrt(3)/2, 0],
                           [sp.sqrt(3)/2, -sp.Rational(1, 2), 0], [0, 0, 1]])
        cls.P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        cls.x = np.array([.6+.2j, -.3+.4j, .15-.9j])

    def exact(self, value):
        self.assertTrue(all(sp.simplify(x) == 0 for x in value))

    def exact_transport(self, i, j):
        return self.t[i]*self.t[j].T + self.ez*self.ez.T

    def test_exact_source_frames_centres_and_geometry_identity(self):
        expected_n = [sp.Matrix([-sp.sqrt(3)/2, sp.Rational(1, 2), 0]),
                      sp.Matrix([0, -1, 0]), sp.Matrix([sp.sqrt(3)/2, sp.Rational(1, 2), 0])]
        expected_c = [sp.Matrix([-sp.Rational(1, 4), sp.sqrt(3)/4, 0]), sp.zeros(3, 1),
                      sp.Matrix([sp.Rational(1, 4), sp.sqrt(3)/4, 0])]
        frames = fs.face_frames()
        self.assertEqual(frames.face_order, ('A=P1', 'B=P2', 'C=P3'))
        for i in range(3):
            self.exact(self.n[i]-expected_n[i])
            self.exact(self.c[i]-expected_c[i])
            self.exact(self.t[i].cross(self.ez)-self.n[i])
            np.testing.assert_array_equal(frames.normals[i], np.array(self.n[i], float).ravel())
            np.testing.assert_array_equal(frames.centres[i], np.array(self.c[i], float).ravel())
            np.testing.assert_array_equal(frames.tangents[i], np.array(self.t[i], float).ravel())
        self.assertEqual(frames.geometry_sha256, hashlib.sha256(Path(geo.__file__).read_bytes()).hexdigest())

    def test_frames_readonly_fresh_and_input_independent(self):
        first, second = fs.face_frames(), fs.face_frames()
        with self.assertRaises(FrozenInstanceError):
            first.frame_id = 'different'
        for name in ('tangents', 'ez', 'normals', 'centres'):
            a, b = getattr(first, name), getattr(second, name)
            self.assertFalse(a.flags.writeable)
            self.assertFalse(np.shares_memory(a, b))
            with self.assertRaises(ValueError):
                a.flat[0] = 99
            experiment = a.copy(); experiment.flat[0] = 99
            np.testing.assert_array_equal(a, b)

    def test_exact_inverse_isometry_and_ambient_projector(self):
        q, p = sp.symbols('q p', real=True)
        ambient = sp.Matrix(sp.symbols('x y z', real=True))
        for i in range(3):
            v = q*self.t[i]+p*self.ez
            self.assertEqual(sp.simplify(self.t[i].dot(v)+sp.I*self.ez.dot(v)-(q+sp.I*p)), 0)
            self.assertEqual(sp.simplify(v.dot(v)-q*q-p*p), 0)
            projector = self.exact_transport(i, i)
            self.exact(self.t[i]*self.t[i].dot(ambient)+self.ez*self.ez.dot(ambient)-projector*ambient)
            self.exact(projector**2-projector)
            self.exact(projector*self.n[i])
            self.assertEqual(projector.rank(), 2)
            self.assertNotEqual(projector, sp.eye(3))

    def test_roundtrip_norms_tiny_values_and_no_polygon_clipping(self):
        for scale in (1., 10., 1e-250):
            omega = scale*self.x; before = omega.copy()
            faces = fs.decode_to_faces(omega)
            self.assertEqual(faces.shape, (3, 3))
            self.assertEqual(faces.dtype, np.dtype('float64'))
            self.assertTrue(np.all(np.any(faces != 0, axis=1)))
            np.testing.assert_allclose(fs.encode_from_faces(faces)/scale, self.x, rtol=3e-15, atol=0)
            norms = np.array([math.hypot(*row) for row in faces])/scale
            np.testing.assert_allclose(norms, abs(self.x), rtol=3e-15, atol=0)
            np.testing.assert_array_equal(omega, before)
            self.assertFalse(np.shares_memory(omega, faces))
        self.assertGreater(math.hypot(*fs.decode_to_faces([10, 0, 0])[0]), 9.9)

    def test_normal_rejection_has_no_absolute_floor_or_vertical_slack(self):
        for i in range(3):
            for scale in (1., 1e-250):
                vectors = np.zeros((3, 3)); vectors[i] = scale*fs.face_frames().normals[i]
                original = vectors.copy()
                with self.assertRaisesRegex(ValueError, 'normal component'):
                    fs.encode_from_faces(vectors)
                np.testing.assert_array_equal(vectors, original)
        vectors = fs.decode_to_faces([1, 1+1e100j, 1])
        vectors[1, 1] = 1e-250  # pure normal on B; neither q nor huge z provides slack
        with self.assertRaisesRegex(ValueError, 'normal component'):
            fs.encode_from_faces(vectors)
        vectors = fs.decode_to_faces(self.x)
        vectors[0] += 1e-10*fs.face_frames().normals[0]
        with self.assertRaisesRegex(ValueError, 'normal component'):
            fs.encode_from_faces(vectors)

    def test_strict_input_and_index_validation(self):
        for bad in ([1, 2], [[1, 2, 3]], [True, 0, 0], ['1', 0, 0], [np.nan, 0, 0], [np.inf, 0, 0]):
            with self.assertRaises((TypeError, ValueError)):
                fs.decode_to_faces(bad)
        for bad in (np.zeros((3, 2)), np.zeros(9), np.full((3, 3), '0'),
                    np.zeros((3, 3), bool), np.zeros((3, 3), complex),
                    np.full((3, 3), np.inf), np.full((3, 3), np.nan)):
            with self.assertRaises((TypeError, ValueError)):
                fs.encode_from_faces(bad)
        for bad in (True, np.bool_(False), 1., 'A', None, -1, 3):
            with self.assertRaises((TypeError, IndexError)):
                fs.transport(bad, 0)
            with self.assertRaises((TypeError, IndexError)):
                fs.state_area(0, bad, self.x)
        np.testing.assert_array_equal(fs.transport(np.int64(0), np.int64(1)), fs.transport(0, 1))

    def test_zero_signed_zero_and_conservative_conversion_failures(self):
        omega = np.array([complex(-0., -0.), complex(0., -0.), 0j])
        view = fs.FaceState(omega)
        self.assertEqual(view.omega.tobytes(), omega.tobytes())
        np.testing.assert_array_equal(view.vectors, np.zeros((3, 3)))
        np.testing.assert_array_equal(fs.encode_from_faces(view.vectors), np.zeros(3))
        self.assertFalse(np.signbit(view.vectors).any())
        for fn, arg in ((fs.decode_to_faces, [1e-320, 0, 0]),
                        (fs.encode_from_faces, [[0, 0, 1e-320], [0, 0, 0], [0, 0, 0]])):
            with self.assertRaises(ResponsePrecisionError):
                fn(arg)
        with self.assertRaises(ResponsePrecisionError):
            fs.area_triple(1e-170*self.x)

    def test_all_exact_transport_and_ambient_composition_identities(self):
        for i, j in itertools.product(range(3), repeat=2):
            matrix = self.exact_transport(i, j)
            self.exact(matrix*self.t[j]-self.t[i])
            self.exact(matrix*self.ez-self.ez)
            self.exact(matrix*self.n[j])
            self.assertEqual(matrix.rank(), 2)
            self.exact(matrix-self.exact_transport(i, i)*self.R**((i-j) % 3))
        for i, j, k in itertools.product(range(3), repeat=3):
            self.exact(self.exact_transport(i, j)*self.exact_transport(j, k)-self.exact_transport(i, k))

    def test_exact_presync_and_outward_normal_phase_dictionary(self):
        q = sp.symbols('q0:3', real=True); p = sp.symbols('p0:3', real=True)
        eps, g, delta = sp.symbols('eps g delta', real=True)
        k = sp.symbols('k0:3', real=True)
        omega = sp.Matrix([q[i]+sp.I*p[i] for i in range(3)])
        vectors = [q[i]*self.t[i]+p[i]*self.ez for i in range(3)]
        for i in range(3):
            coupling = sum((self.exact_transport(i, j)*vectors[j]-vectors[i]
                            for j in range(3) if j != i), sp.zeros(3, 1))
            updated = vectors[i]+eps*(k[i]-vectors[i].dot(vectors[i]))*vectors[i]+g*coupling
            encoded = self.t[i].dot(updated)+sp.I*self.ez.dot(updated)
            expected = omega[i]+eps*omega[i]*(k[i]-q[i]**2-p[i]**2)+g*(sp.Matrix(dy.L3)*omega)[i]
            self.assertEqual(sp.simplify(sp.expand(encoded-expected)), 0)
            rotated = sp.cos(delta)*vectors[i]+sp.sin(delta)*self.n[i].cross(vectors[i])
            decoded_phase = (q[i]*sp.cos(delta)-p[i]*sp.sin(delta))*self.t[i]+(q[i]*sp.sin(delta)+p[i]*sp.cos(delta))*self.ez
            self.exact(rotated-decoded_phase)

    def test_all_floating_transport_matrices_match_exact_source(self):
        frames = fs.face_frames(); vectors = fs.decode_to_faces(self.x)
        for i, j in itertools.product(range(3), repeat=2):
            actual = fs.transport(i, j)
            np.testing.assert_allclose(actual, np.array(self.exact_transport(i, j), float), rtol=3e-15, atol=3e-16)
            expected = self.x[j].real*frames.tangents[i]+self.x[j].imag*frames.ez
            np.testing.assert_allclose(actual@vectors[j], expected, rtol=3e-15, atol=3e-16)
            self.assertEqual(np.linalg.matrix_rank(actual), 2)
            self.assertFalse(actual.flags.writeable)
        for i, j, k in itertools.product(range(3), repeat=3):
            np.testing.assert_allclose(fs.transport(i, j)@fs.transport(j, k), fs.transport(i, k),
                                       rtol=3e-15, atol=3e-16)

    def test_point_rotation_uses_centroid_axis_and_vectors_use_linear_part(self):
        for i in range(3):
            self.exact(sp.Matrix(geo.rotate_c3(tuple(self.c[i])))-self.c[(i+1) % 3])
            self.exact(self.R*self.t[i]-self.t[(i+1) % 3])
        a, b = self.mesh.vertices[:2]
        self.exact(sp.Matrix(geo.rotate_c3(a))-sp.Matrix(geo.rotate_c3(b))
                   - self.R*(sp.Matrix(a)-sp.Matrix(b)))
        self.assertNotEqual(self.R*self.c[1], self.c[2])  # rotating point B about origin is wrong
        self.exact(self.R*sp.Matrix(geo.CENTROID)-sp.Matrix(geo.CENTROID)
                   + sp.Matrix(geo.rotate_c3((0, 0, 0))))

    def test_isolated_octagon_rotation_is_not_welded_shell_symmetry(self):
        n = self.n[1]
        cross = sp.Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
        rotation = sp.eye(3)+sp.sin(sp.pi/4)*cross+(1-sp.cos(sp.pi/4))*cross**2
        transform = lambda p: tuple(sp.simplify(x) for x in rotation*sp.Matrix(p))
        face = {self.mesh.vertices[i] for i in self.mesh.faces[1]}
        self.assertEqual({transform(v) for v in face}, face)
        self.assertNotEqual({transform(v) for v in self.mesh.vertices}, set(self.mesh.vertices))
        self.assertNotEqual(sp.simplify(rotation*self.t[1]), self.t[1])

    def test_signed_area_exact_and_independent_geometric_comparison(self):
        q = sp.symbols('q0:3', real=True); p = sp.symbols('p0:3', real=True)
        v = [q[i]*self.t[i]+p[i]*self.ez for i in range(3)]
        for i, j in itertools.product(range(3), repeat=2):
            area = self.n[i].dot(v[i].cross(self.exact_transport(i, j)*v[j]))
            self.assertEqual(sp.simplify(area-(q[i]*p[j]-p[i]*q[j])), 0)
        for scale in (1., 1e-140):
            omega = scale*self.x; vectors = fs.decode_to_faces(omega); frames = fs.face_frames()
            for i, j in itertools.product(range(3), repeat=2):
                geometric = frames.normals[i] @ np.cross(vectors[i], fs.transport(i, j)@vectors[j])
                actual = fs.state_area(i, j, omega)
                if i != j:
                    self.assertNotEqual(actual, 0.)
                    np.testing.assert_allclose(actual/(scale*scale), geometric/(scale*scale), rtol=4e-15, atol=1e-16)
                    self.assertEqual(actual, -fs.state_area(j, i, omega))
                else:
                    self.assertEqual(actual, 0.)

    def test_area_delegation_is_bitwise_and_does_not_mutate(self):
        for omega in (self.x.copy(), np.zeros(3), 1e-140*self.x):
            saved = omega.tobytes()
            expected = readouts.z_chiral(omega)
            with patch('kernel_physics.readouts.z_chiral', wraps=readouts.z_chiral) as call:
                actual = fs.area_triple(omega)
                call.assert_called_once_with(omega)
            self.assertEqual(actual.tobytes(), expected.tobytes())
            self.assertEqual(omega.tobytes(), saved)
        with self.assertRaises((TypeError, ValueError)):
            fs.state_area(0, 0, [True, 0, 0])
        with self.assertRaises(ResponsePrecisionError):
            fs.state_area(0, 0, 1e-170*self.x)  # complete readout validation even on diagonal

    def test_spatial_and_channel_permutation_signs_are_separate(self):
        frames = fs.decode_to_faces(self.x)
        A = np.array([[fs.state_area(i, j, self.x) for j in range(3)] for i in range(3)])
        Z = fs.area_triple(self.x)
        vertical = np.diag([-1, 1, 1]); horizontal = np.diag([1, 1, -1])
        swap = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        for r, v, h in itertools.product(range(3), range(2), range(2)):
            G = np.array(self.R**r, float) @ np.linalg.matrix_power(vertical, v) @ np.linalg.matrix_power(horizontal, h)
            P = np.linalg.matrix_power(self.P, r) @ np.linalg.matrix_power(swap, v)
            sign_g, sign_p = round(np.linalg.det(G)), round(np.linalg.det(P))
            transformed = fs.encode_from_faces((P@frames)@G.T)
            Aprime = np.array([[fs.state_area(i, j, transformed) for j in range(3)] for i in range(3)])
            np.testing.assert_allclose(Aprime, sign_g*P@A@P.T, rtol=4e-15, atol=4e-16)
            np.testing.assert_allclose(fs.area_triple(transformed), sign_g*sign_p*P@Z, rtol=4e-15, atol=4e-16)
        for perm in itertools.permutations(range(3)):
            P = np.eye(3)[list(perm)]
            np.testing.assert_allclose(fs.area_triple(P@self.x), round(np.linalg.det(P))*P@Z, atol=3e-16)
        np.testing.assert_allclose(fs.encode_from_faces(frames@horizontal.T), self.x.conj(), atol=3e-16)
        np.testing.assert_allclose(fs.encode_from_faces((swap@frames)@vertical.T), -swap@self.x.conj(), atol=3e-16)
        np.testing.assert_allclose(fs.area_triple(np.exp(.7j)*self.x), Z, atol=3e-16)
        self.assertGreater(np.linalg.norm(np.array(self.R, float)@np.array([1., 0, 0])-self.P@np.array([1., 0, 0])), .5)

    def test_equal_k_covariance_and_unequal_k_qualification(self):
        equal = region.bounded_config(k=[1, 1, 1], phase_strength=.1)
        unequal = region.bounded_config(k=[1, 2, 3], phase_strength=.1)
        for config in (equal, unequal):
            lhs = fs.FaceState(self.P@self.x).step(config).omega
            rhs = self.P@fs.FaceState(self.x).step(config).omega
            if config is equal:
                np.testing.assert_allclose(lhs, rhs, atol=1e-15)
            else:
                self.assertGreater(max(abs(lhs-rhs)), .01)
                permuted = region.bounded_config(k=self.P@config.k, phase_strength=config.phase_strength)
                np.testing.assert_allclose(fs.FaceState(self.P@self.x).step(permuted).omega, rhs, atol=1e-15)

    def test_existing_zero_stratum_phase_qualification(self):
        x = np.array([0, 1, np.exp(.2j)])
        phase = np.exp(.4j)
        for strength in (0., .1):
            config = dy.DynamicsConfig(0., 0., strength, (0., 0., 0.))
            lhs = fs.FaceState(phase*x).step(config).omega
            rhs = phase*fs.FaceState(x).step(config).omega
            gap = max(abs(lhs-rhs))
            if strength:
                self.assertAlmostEqual(gap, .09317017645041971, places=14)
            else:
                np.testing.assert_array_equal(lhs, rhs)
            self.assertEqual(lhs[0], 0.)
        self.assertEqual(dy.arg0([complex(-0., -0.)])[0], 0.)
        nonzero = np.array([.5, 1, np.exp(.2j)])
        config = dy.DynamicsConfig(0., 0., .1, (0., 0., 0.))
        np.testing.assert_allclose(fs.FaceState(phase*nonzero).step(config).omega,
                                   phase*fs.FaceState(nonzero).step(config).omega, atol=5e-16)

    def test_canonical_trajectory_single_call_and_no_automatic_encode(self):
        config = region.bounded_config(k=[1., 1.2208964704604097, 6.35310346037241], phase_strength=.001)
        for profile in (None, region.PROFILE_ID):
            view = fs.FaceState(self.x); raw = self.x.copy(); initial = self.x.tobytes()
            with patch('kernel_physics.face_state.encode_from_faces', side_effect=AssertionError('no round trips')):
                for _ in range(6):
                    previous_omega, previous_faces = view.omega.tobytes(), view.vectors.tobytes()
                    if profile is None:
                        expected = dy.step3(raw, config)
                        with patch('kernel_physics.dynamics.step3', wraps=dy.step3) as step:
                            updated = view.step(config)
                            step.assert_called_once()
                    else:
                        expected = region.step_bounded_triad(raw, config, profile=profile)
                        with patch('kernel_physics.operating_region.step3', wraps=dy.step3) as step:
                            with patch('kernel_physics.operating_region.step_bounded_triad', wraps=region.step_bounded_triad) as adapter:
                                updated = view.step(config, profile=profile)
                                adapter.assert_called_once()
                            step.assert_called_once()
                    self.assertEqual(updated.omega.tobytes(), expected.tobytes())
                    self.assertEqual(view.omega.tobytes(), previous_omega)
                    self.assertEqual(view.vectors.tobytes(), previous_faces)
                    self.assertFalse(updated.omega.flags.writeable or updated.vectors.flags.writeable)
                    view, raw = updated, expected
            self.assertEqual(self.x.tobytes(), initial)

    def test_explicit_face_initialization_and_profile_errors(self):
        faces = fs.decode_to_faces(self.x); saved = faces.copy()
        with patch('kernel_physics.face_state.encode_from_faces', wraps=fs.encode_from_faces) as encode:
            view = fs.FaceState.from_faces(faces)
            encode.assert_called_once_with(faces)
        np.testing.assert_array_equal(view.omega, fs.encode_from_faces(faces))
        np.testing.assert_array_equal(faces, saved)
        self.assertFalse(np.shares_memory(view.vectors, faces))
        config = region.bounded_config(k=[1, 1, 1], phase_strength=0)
        for state, profile in (([4, 0, 0], region.PROFILE_ID), (self.x, 'unknown'), (self.x, False)):
            with patch('kernel_physics.operating_region.step3', side_effect=AssertionError('invalid profile reached recurrence')):
                with self.assertRaises((TypeError, ValueError)):
                    fs.FaceState(state).step(config, profile=profile)
        with self.assertRaises(TypeError):
            view.step(None)
        with self.assertRaises(ValueError):
            view.omega[0] = 1
        with self.assertRaises(ValueError):
            view.vectors[0, 0] = 1

    def test_readme_complete_pipeline_for_equal_and_recorded_unequal_k(self):
        root = Path(__file__).resolve().parents[1]
        blocks = re.findall(r'~~~python\n(.*?)\n~~~', (root/'README.md').read_text(encoding='utf-8'), re.S)
        self.assertEqual(len(blocks), 1)
        namespace = {}
        exec(compile(blocks[0], str(root/'README.md'), 'exec'), namespace)
        records = json.loads(json.dumps(namespace['face_runs'], allow_nan=False))
        self.assertEqual(len(records), 2)
        for record in records:
            self.assertEqual(record['face_view']['frame_id'], fs.FRAME_ID)
            self.assertEqual(record['face_view']['transport_id'], fs.TRANSPORT_ID)
            self.assertEqual(record['face_view']['face_order'], list(fs.FACE_ORDER))
            self.assertEqual(record['face_view']['geometry']['source_sha256'], fs.face_frames().geometry_sha256)
            self.assertNotIn('frame_id', record['initialization'])
            config = dy.DynamicsConfig(**record['downstream']['config'])
            trajectory = record['face_trajectory']
            raw = np.array([complex(*z) for z in record['expected_result']['initial_omega']])
            for index, snapshot in enumerate(trajectory):
                self.assertEqual(snapshot['downstream_step'], index)
                self.assertEqual(raw.tobytes(), np.array([complex(*z) for z in snapshot['omega']]).tobytes())
                np.testing.assert_array_equal(snapshot['vectors'], fs.decode_to_faces(raw))
                np.testing.assert_array_equal(snapshot['area_triple'], readouts.z_chiral(raw))
                if index < record['downstream']['step_count']:
                    raw = region.step_bounded_triad(raw, config, profile=record['downstream']['profile_id'])
            initial_lengths = [math.hypot(*v) for v in trajectory[0]['vectors']]
            np.testing.assert_allclose(initial_lengths, np.full(3, initial_lengths[0]), rtol=3e-15, atol=0)
            last_lengths = [math.hypot(*v) for v in trajectory[-1]['vectors']]
            if len(set(config.k)) == 1:
                np.testing.assert_allclose(last_lengths, np.full(3, last_lengths[0]), rtol=2e-14, atol=0)
            else:
                self.assertGreater(max(last_lengths)-min(last_lengths), .01)


if __name__ == '__main__':
    unittest.main()
