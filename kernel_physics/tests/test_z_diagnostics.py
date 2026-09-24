"""Self-contained K3 proof, numeric and boundary checks; no paper/repository inputs."""
from dataclasses import FrozenInstanceError
import ast
import inspect
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import mpmath as mp
import numpy as np
import sympy as sp

from kernel_physics import readouts, z_diagnostics as d, z_manifold as z
from kernel_physics._response_numeric import ResponsePrecisionError
from kernel_physics.dynamics import DynamicsConfig, step3

EVIDENCE = {"numeric": [], "symbolic": {}, "fixtures": {}}
EPS = np.finfo(float).eps


def norm2(v):
    return math.fsum(float(c)**2 for a in v for c in (complex(a).real, complex(a).imag))


def history(k=(.5, 1., 2.), q=(0, 3, 7), scalar=(.2, -.1, .4)):
    return {"kappa": np.array(k), "phi_index": np.array(q), "z": np.array(scalar)}


def config(eps=.05, g=.2, phase=0, k=(1., 1.2, 1.4)):
    return DynamicsConfig(eps, g, phase, k)


def xyz(value):
    return np.column_stack((value.x, value.y, value.z))


class Checks(unittest.TestCase):
    def close(self, label, actual, expected, scale, factor=96):
        """Absolute allowance = factor * epsilon * actual contributing scale."""
        residual = float(actual) - float(expected)
        allowance = factor * EPS * float(scale)
        EVIDENCE["numeric"].append(dict(label=label, actual=float(actual),
            expected=float(expected), residual=residual, scale=float(scale),
            epsilon=EPS, factor=factor, allowance=allowance))
        self.assertLessEqual(abs(residual), allowance, label)

    def exact(self, label, expression):
        residual = sp.expand(expression)
        EVIDENCE["symbolic"][label] = str(residual)
        self.assertEqual(residual, 0)


class ExactTests(Checks):
    @classmethod
    def setUpClass(cls):
        cls.x = sp.Matrix(sp.symbols("x1:4", real=True))
        cls.y = sp.Matrix(sp.symbols("y1:4", real=True))
        cls.k = sp.symbols("k1:4", real=True)
        cls.eps, cls.g = sp.symbols("eps g", real=True)
        cls.L = sp.Matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
        cls.s = [cls.x[i]**2+cls.y[i]**2 for i in range(3)]
        cls.P = sum((cls.x[i]-cls.x[j])**2+(cls.y[i]-cls.y[j])**2
                    for i in range(3) for j in range(i+1, 3))
        cls.dx = sp.Matrix([cls.eps*(cls.k[i]-cls.s[i])*cls.x[i] for i in range(3)])+cls.g*cls.L*cls.x
        cls.dy = sp.Matrix([cls.eps*(cls.k[i]-cls.s[i])*cls.y[i] for i in range(3)])+cls.g*cls.L*cls.y

    def test_graph_and_full_finite_budget(self):
        x, y = self.x, self.y
        self.exact("Hermitian graph", (x.T*self.L*x)[0]+(y.T*self.L*y)[0]+self.P)
        after = sum((x[i]+self.dx[i])**2+(y[i]+self.dy[i])**2 for i in range(3))
        onsite = 2*self.eps*sum(self.k[i]*self.s[i]-self.s[i]**2 for i in range(3))
        self.exact("finite budget", after-sum(self.s)-onsite+2*self.g*self.P
                   -sum(v**2 for v in (*self.dx, *self.dy)))

    def test_six_real_gradient_components(self):
        potential = self.eps*sum(self.s[i]**2/4-self.k[i]*self.s[i]/2
                                 for i in range(3))+self.g*self.P/2
        for i, (coordinate, increment) in enumerate(zip((*self.x, *self.y), (*self.dx, *self.dy))):
            self.exact(f"real gradient {i}", sp.diff(potential, coordinate)+increment)

    def test_generic_norm_and_full_quadratic_blends(self):
        a, b = sp.symbols("alpha beta", real=True)
        m, c = self.x, self.y
        for label, signs in (("norm", (1, 1, 1)), ("Q", (1, 1, -1))):
            actual = sum(signs[i]*(a*m[i]+b*c[i])**2 for i in range(3))
            predicted = a*a*sum(signs[i]*m[i]**2 for i in range(3))
            predicted += b*b*sum(signs[i]*c[i]**2 for i in range(3))
            predicted += 2*a*b*sum(signs[i]*m[i]*c[i] for i in range(3))
            self.exact(f"generic full {label}", actual-predicted)

    def test_gram_slack_and_equality_examples(self):
        a, b, h = self.x.dot(self.x), self.y.dot(self.y), self.x.dot(self.y)
        area2 = self.x.cross(self.y).dot(self.x.cross(self.y))
        self.exact("Gram", area2-a*b+h*h)
        self.exact("sum of squares slack", (a+b)**2/4-area2-(a-b)**2/4-h*h)
        # A,B,h are real: the two squares vanish iff A=B and h=0.
        for omega in ([1, 1j, 0], [0, 0, 0]):
            r = d.chiral_area_accounting(omega)
            self.assertEqual(r.A, r.B)
            self.assertEqual(r.h, 0)
            self.assertEqual(r.chiral_norm, r.amplitude_bound)

    def test_exact_overshoot(self):
        s = sp.Integer(4)
        increment = 2*(1-s)
        self.assertEqual(increment, -6)
        self.assertEqual(3*(-4)**2-3*2**2, 36)
        self.assertEqual(2*3*(s-s*s), -72)
        self.assertEqual(3*increment**2, 108)
        self.assertEqual(3*(s*s/4-s/2), 6)
        self.assertEqual(3*(sp.Integer(16)**2/4-sp.Integer(16)/2), 168)
        EVIDENCE["symbolic"]["overshoot"] = dict(D=[-6]*3, V_pre=[-4]*3,
            intensity_before=12, intensity_after=48, onsite=-72, remainder=108,
            delta=36, potential_before=6, potential_after=168)


class BudgetTests(Checks):
    def test_overshoot_runtime(self):
        cfg = config(eps=1, g=.73, k=(1, 1, 1))
        r = d.intensity_budget([2, 2, 2], cfg)
        np.testing.assert_array_equal(r.increment, [-6]*3)
        np.testing.assert_array_equal(r.diagnostic_pre_sync_prediction, [-4]*3)
        self.assertEqual((r.intensity_before, r.intensity_pre_sync, r.onsite,
                          r.coupling, r.remainder, r.predicted_delta, r.residual),
                         (12, 48, -72, 0, 108, 36, 0))
        self.assertEqual(d.potential([2]*3, cfg), 6)
        self.assertEqual(d.potential([-4]*3, cfg), 168)

    def test_zero_state(self):
        r = d.intensity_budget([0]*3, config())
        self.assertEqual((r.intensity_before, r.onsite, r.coupling, r.remainder,
                          r.predicted_delta, r.observed_delta, r.residual), (0,)*7)
        self.assertEqual(d.potential([0]*3, config()), 0)

    def test_mixed_signed_unequal_high_precision_oracle(self):
        omega = [.2+.3j, -.4+.1j, .1-.2j]
        cfg = config(eps=-.07, g=-.12, k=(-1., 1.2, .4))
        r = d.intensity_budget(omega, cfg)
        with mp.workdps(90):
            v = [mp.mpc(a) for a in omega]
            s = [abs(a)**2 for a in v]
            inc = [mp.mpf(cfg.eps)*(mp.mpf(cfg.k[i])-s[i])*v[i]
                   +mp.mpf(cfg.g)*sum(v[j]-v[i] for j in range(3) if j != i)
                   for i in range(3)]
            p = sum(abs(v[i]-v[j])**2 for i in range(3) for j in range(i+1, 3))
            onsite = 2*mp.mpf(cfg.eps)*sum(mp.mpf(k)*a-a*a for k, a in zip(cfg.k, s))
            coupling = -2*mp.mpf(cfg.g)*p
            remainder = sum(abs(a)**2 for a in inc)
            pot = mp.mpf(cfg.eps)*sum(a*a/4-mp.mpf(k)*a/2 for k, a in zip(cfg.k, s))+mp.mpf(cfg.g)*p/2
            EVIDENCE["fixtures"]["mixed_90dps"] = {name: str(value) for name, value in
                dict(onsite=onsite, coupling=coupling, remainder=remainder, potential=pot).items()}
            for name, expected in (("onsite", onsite), ("coupling", coupling), ("remainder", remainder)):
                self.close(name, getattr(r, name), expected, abs(expected))
            for i in range(3):
                self.close(f"D real {i}", r.increment[i].real, inc[i].real, abs(inc[i]))
                self.close(f"D imag {i}", r.increment[i].imag, inc[i].imag, abs(inc[i]))
            self.close("potential high precision", d.potential(omega, cfg), pot,
                       abs(cfg.eps)*sum(float(a*a/4+abs(k)*a/2) for k, a in zip(cfg.k, s))+abs(float(mp.mpf(cfg.g)*p/2)))
        scale = r.intensity_before+r.intensity_pre_sync+abs(r.onsite)+abs(r.coupling)+r.remainder
        self.close("mixed budget residual", r.residual, 0, scale)

    def test_tiny_state_budget_uses_tiny_scale(self):
        omega = np.array([.2+.3j, -.4+.1j, .1-.2j])*1e-50
        r = d.intensity_budget(omega, config())
        scale = r.intensity_before+r.intensity_pre_sync+abs(r.onsite)+abs(r.coupling)+r.remainder
        self.assertLess(scale, 1e-98)
        self.close("tiny budget", r.residual, 0, scale)

    def test_existing_step_phase_off_and_on(self):
        for omega in ([.2+.3j, -.4+.1j, .1-.2j], [0j, 1+.4j, -.2+.1j]):
            for strength in (0, .11):
                cfg = config(g=0 if omega[0] == 0 else .2, phase=strength)
                r = d.intensity_budget(omega, cfg)
                actual = step3(omega, cfg)
                self.close("step intensity", norm2(actual), r.intensity_pre_sync,
                           norm2(actual)+r.intensity_pre_sync)
                if strength == 0:
                    for a, b in zip(actual, r.diagnostic_pre_sync_prediction):
                        self.close("step real", a.real, b.real, abs(a)+abs(b))
                        self.close("step imag", a.imag, b.imag, abs(a)+abs(b))
                if omega[0] == 0:
                    self.assertEqual(actual[0], 0j)

    def test_phase_changes_potential_without_changing_intensity(self):
        omega = [.2+.3j, -.4+.1j, .1-.2j]
        off, on = config(phase=0), config(phase=.2)
        v0, v1 = step3(omega, off), step3(omega, on)
        self.close("sync intensity", norm2(v0), norm2(v1), norm2(v0)+norm2(v1))
        self.assertGreater(abs(d.potential(v0, off)-d.potential(v1, on)), 1e-5)

    def test_pure_coupling_fixture(self):
        for g in (2/3, .8):
            cfg = config(eps=0, g=g)
            r = d.intensity_budget([1, -1, 0], cfg)
            self.close("coupling fixture", r.observed_delta, ((1-3*g)**2-1)*2,
                       r.intensity_before+r.intensity_pre_sync)
        self.assertGreater(r.observed_delta, 0)

    def test_observation_between_steps_preserves_trajectory(self):
        initial = np.array([.2+.3j, -.4+.1j, .1-.2j])
        for strength in (0., .01):
            cfg = config(phase=strength)
            plain, inspected = initial.copy(), initial.copy()
            clock, memory = z.Clock(q=2), z.EMAState(.3)
            for _ in range(5):
                before = inspected.tobytes()
                d.intensity_budget(inspected, cfg)
                d.potential(inspected, cfg)
                d.chiral_area_accounting(inspected)
                obs = z.observe_ema(inspected, clock, z.EMAConfig(), memory)
                d.readout_accounting(obs, alpha=1, beta=.5)
                d.historical_alignment(obs.Z_macro, obs.Z_chiral, obs.Z_total)
                self.assertEqual(inspected.tobytes(), before)
                plain, inspected = step3(plain, cfg), step3(inspected, cfg)
                np.testing.assert_array_equal(plain, inspected)
            self.assertEqual(clock, z.Clock(q=2))
            self.assertEqual(memory, z.EMAState(.3))


class ReadoutTests(Checks):
    def test_both_variants_and_constructor_markers(self):
        omega, clock = [.2+.3j, -.4+.1j, .1-.2j], z.Clock(q=2, t=.3)
        values = [z.observe_staged(omega, clock, z.StagedConfig()),
                  z.observe_ema(omega, clock, z.EMAConfig(), z.EMAState(.2)),
                  z.historical_constructor_zero(omega, clock, z.StagedConfig()).readout]
        for obs in values:
            r = d.readout_accounting(obs, alpha=1, beta=.5)
            self.assertEqual((r.variant, r.initialization), (obs.variant, obs.initialization))
            self.close("macro Q", r.q_macro, 0, r.macro_norm_squared)
            self.close("macro norm relation", r.macro_relation_residual, 0,
                       r.macro_norm_squared+2*obs.z**2)
            self.close("norm identity", r.norm_residual, 0,
                       r.total_norm_squared+abs(r.weighted_macro)+abs(r.weighted_chiral)+abs(r.cross_term))
            self.close("full Q", r.q_residual, 0,
                       r.total_norm_squared+abs(r.q_weighted_macro)+abs(r.q_weighted_chiral)+abs(r.q_cross_term))

    def test_generic_noncone_and_signed_weights(self):
        m, c, a, b = np.array([1., 2., 3.]), np.array([-2., 1., 4.]), -2., .5
        obs = z.ZReadout(7, m, c, a*m+b*c, "ema")
        r = d.readout_accounting(obs, alpha=a, beta=b)
        self.assertEqual(r.q_macro, -4)
        self.assertEqual(r.q_weighted_macro, -16)
        self.assertEqual(r.q_residual, 0)
        self.assertEqual(r.norm_residual, 0)
        self.assertNotEqual(r.macro_relation_residual, 0)
        np.testing.assert_array_equal(r.blend_residual, [0]*3)

    def test_pure_components_perpendicular_and_cancellation(self):
        for a, b in ((1, 0), (0, -2), (2, 3)):
            m, c = np.array([2., 0, 0]), np.array([0., 3, 0])
            r = d.readout_accounting(z.ZReadout(2, m, c, a*m+b*c, "staged"), alpha=a, beta=b)
            self.assertEqual(r.cross_term, 0)
            self.assertEqual(r.norm_residual, 0)
        # Actual accepted EMA observation with M=C=(-1,0,-1), alpha=1,beta=-1.
        omega = [1, -1j, -1]
        obs = z.observe_ema(omega, z.Clock(), z.EMAConfig(lambda_vp=0, alpha=1, beta=-1), z.EMAState(-1))
        np.testing.assert_array_equal(obs.Z_total, [0]*3)
        self.assertTrue(np.any(obs.Z_macro))
        self.assertTrue(np.any(obs.Z_chiral))
        r = d.readout_accounting(obs, alpha=1, beta=-1)
        self.assertEqual(r.total_norm_squared, 0)
        self.assertEqual(r.norm_residual, 0)

    def test_inconsistent_supplied_record_is_not_repaired(self):
        obs = z.ZReadout(1, [1, 2, 3], [0, 1, 0], [8, 0, 1], "staged")
        before = obs.Z_total.tobytes()
        r = d.readout_accounting(obs, alpha=1, beta=1)
        self.assertNotEqual(r.norm_residual, 0)
        self.assertNotEqual(r.q_residual, 0)
        np.testing.assert_array_equal(r.blend_residual, [7, -3, -2])
        self.assertEqual(obs.Z_total.tobytes(), before)

    def test_chirality_delegation_and_parallel_slack(self):
        omega = [1+2j, 2+4j, -3-6j]
        with patch.object(readouts, "z_chiral", wraps=readouts.z_chiral) as call:
            r = d.chiral_area_accounting(omega)
        self.assertEqual(call.call_count, 1)
        self.assertEqual(r.chiral_norm, 0)
        self.assertGreater(r.intensity, 0)
        self.assertGreater(r.slack_sum_of_squares, 0)
        self.assertEqual(r.gram_residual, 0)
        self.assertEqual(r.slack_residual, 0)

    def test_mixed_chiral_gram_oracle_and_no_clamp(self):
        v = np.array([.2+.3j, -.4+.1j, .1-.2j])
        r = d.chiral_area_accounting(v)
        oracle = np.cross(v.real, v.imag)
        for actual, expected in zip(r.chiral, oracle):
            self.close("area component", actual, expected, abs(actual)+abs(expected))
        self.close("Gram", r.gram_residual, 0, r.chiral_norm_squared+abs(r.gram_product)+r.h_squared)
        self.close("slack", r.slack_residual, 0,
                   r.amplitude_bound**2+r.chiral_norm_squared+r.slack_sum_of_squares)
        # Fixed nearly parallel fixture gives a signed rounded Gram difference.
        near = np.array([1+1j, 1+1j, 1+(1+2**-26)*1j])
        r = d.chiral_area_accounting(near)
        self.assertEqual(r.gram_rhs, r.gram_product-r.h_squared)
        self.assertEqual(r.gram_residual, r.chiral_norm_squared-r.gram_rhs)
        EVIDENCE["fixtures"]["near_parallel_gram"] = dict(gram=r.gram_rhs, residual=r.gram_residual)

    def test_alignment_threshold_and_resolution(self):
        for length, expected in ((math.nextafter(1e-12, 0), False),
                                 (1e-12, True), (math.nextafter(1e-12, 1), True)):
            r = d.historical_alignment([length, 0, 0], [1, 0, 0], [1, 0, 0])
            self.assertEqual(r.macro_resolved, expected)
            self.assertEqual(r.TM_resolved, expected)
            self.assertEqual(r.d_TM, float(expected))
        tiny = d.historical_alignment([1e-13, 0, 0], [1, 0, 0], [1, 0, 0])
        orth = d.historical_alignment([0, 1, 0], [1, 0, 0], [1, 0, 0])
        self.assertEqual(tiny.d_TM, orth.d_TM)
        self.assertFalse(tiny.TM_resolved)
        self.assertTrue(orth.TM_resolved)
        zero = d.historical_alignment([1, 0, 0], [1, 0, 0], [0]*3)
        self.assertFalse(zero.total_resolved)
        self.assertFalse(zero.TC_resolved)

    def test_alignment_stable_large_and_rejections(self):
        r = d.historical_alignment([1e200]*3, [1, 0, 0], [1e200]*3)
        self.close("stable alignment", r.d_TM, 1, 1)
        for invalid in ([math.inf, 0, 0], [math.nan, 0, 0], [True, 0, 0], [1j, 0, 0]):
            with self.assertRaises((TypeError, ValueError)):
                d.historical_alignment(invalid, [1, 0, 0], [1, 0, 0])


class DisplayTests(Checks):
    def test_direct_selection_fallback_and_explicit_key(self):
        a, b = np.arange(6.).reshape(2, 3), np.ones((2, 3))
        h = {"Z_total": a, "Z_vec": b, "chosen": a+3}
        np.testing.assert_array_equal(xyz(d.direct_history_coordinates(h)), a)
        np.testing.assert_array_equal(xyz(d.direct_history_coordinates({"Z_vec": b})), b)
        np.testing.assert_array_equal(xyz(d.direct_history_coordinates(h, "chosen")), a+3)
        with self.assertRaises(KeyError):
            d.direct_history_coordinates(h, "absent")

    def test_direct_empty_no_alias_and_invalid_no_fallback(self):
        h = {"Z_total": np.arange(6.).reshape(2, 3)}
        r = d.direct_history_coordinates(h)
        h["Z_total"][0, 0] = 99
        self.assertEqual(r.x[0], 0)
        self.assertFalse(np.shares_memory(r.x, h["Z_total"]))
        self.assertEqual(xyz(d.direct_history_coordinates({"Z_total": np.empty((0, 3))})).shape, (0, 3))
        for invalid in ([[1, 2]], [1, 2, 3], [[1, 2, math.nan]], [[True, 2, 3]], [["1", 2, 3]], [[1j, 2, 3]]):
            with self.assertRaises((TypeError, ValueError)):
                d.direct_history_coordinates({"Z_total": invalid, "Z_vec": np.zeros((1, 3))})

    def test_cylinder_landmarks_zero_height_custom_sectors(self):
        np.testing.assert_array_equal(d.cylinder_point(2, 0, -3), [2, 0, -3])
        np.testing.assert_array_equal(d.cylinder_point(0, 7, 4), [0, 0, 4])
        for q, n in ((3, 12), (4, 7), (-3, 7), (10**80+2, 7)):
            actual = d.cylinder_point(2, q, -.4, N=n)
            theta = 2*math.pi*(q % n)/n
            for a, b in zip(actual, (2*math.cos(theta), 2*math.sin(theta), -.4)):
                self.close("cylinder oracle", a, b, abs(a)+abs(b))

    def test_cylinder_history_empty_shapes_and_types(self):
        h = history()
        for n in (12, 7):
            r = d.cylinder_history_coordinates(h, N=n)
            for i, row in enumerate(xyz(r)):
                np.testing.assert_array_equal(row, d.cylinder_point(h["kappa"][i], int(h["phi_index"][i]), h["z"][i], N=n))
        empty = history((), (), ())
        self.assertEqual(xyz(d.cylinder_history_coordinates(empty)).shape, (0, 3))
        for invalid in (history(q=(0, 1)), history(q=(0., 1., 2.)),
                        history(k=(-1, 2, 3)), history(scalar=(0, math.inf, 0)),
                        history(q=(False, True, False))):
            with self.assertRaises((TypeError, ValueError)):
                d.cylinder_history_coordinates(invalid)
        for n in (0, -1, True, 12., "12"):
            with self.assertRaises((TypeError, ValueError)):
                d.cylinder_history_coordinates(empty, N=n)

    def test_torus_oracle_metadata_default_and_custom(self):
        h = history()
        for n in (12, 7):
            r = d.history_torus_coordinates(h, N=n)
            hz = max(abs(h["z"]))+1e-9
            self.assertEqual((r.z_max, r.H_z, r.regularizer, r.R, r.r_max, r.N, r.normalization),
                             (.4, hz, 1e-9, 2., 1., n, "entire_supplied_history"))
            for i, (k, q, scalar) in enumerate(zip(h["kappa"], h["phi_index"], h["z"])):
                with mp.workdps(80):
                    theta = 2*mp.pi*int(q)/n
                    minor = mp.mpf(float(k))/(1+mp.mpf(float(k)))
                    chi = mp.pi*mp.mpf(float(scalar))/(2*mp.mpf(hz))
                    expected = ((2+minor*mp.cos(chi))*mp.cos(theta),
                                (2+minor*mp.cos(chi))*mp.sin(theta), minor*mp.sin(chi))
                    # Coordinate scale includes its radius, not a universal floor.
                    for j, value in enumerate(expected):
                        scale = 2+float(minor) if j < 2 else float(minor)
                        self.close(f"torus n={n} row={i} axis={j}", xyz(r)[i, j], value, scale)

    def test_history_dependence_and_zero_kappa_degeneracy(self):
        a = d.history_torus_coordinates(history(k=(1,), q=(1,), scalar=(.2,)))
        b = d.history_torus_coordinates(history(k=(1, 1), q=(1, 2), scalar=(.2, 2.)))
        self.assertGreater(abs(a.z[0]-b.z[0]), .1)
        self.assertNotEqual(a.H_z, b.H_z)
        h = history(k=(0, 0), q=(0, 0), scalar=(-3, 4))
        r = d.history_torus_coordinates(h)
        np.testing.assert_array_equal(xyz(r), [[2, 0, 0], [2, 0, 0]])
        np.testing.assert_array_equal(d.cylinder_history_coordinates(h).z, [-3, 4])
        zero = d.history_torus_coordinates(history(scalar=(0, 0, 0)))
        self.assertEqual(zero.H_z, 1e-9)
        np.testing.assert_array_equal(zero.chi, [0]*3)

    def test_torus_rejects_empty_invalid_domain_and_shapes(self):
        with self.assertRaises(ValueError):
            d.history_torus_coordinates(history((), (), ()))
        for R, r in ((1, 1), (0, 1), (2, 0), (2, -1), (True, 1), (2, "1"), (math.inf, 1)):
            with self.assertRaises((TypeError, ValueError)):
                d.history_torus_coordinates(history(), R=R, r_max=r)
        for h in (history(scalar=(1, 2)), history(k=(-1, 0, 1)), history(q=(0., 1., 2.)),
                  history(scalar=(0, math.nan, 0)), history(k=((1, 2, 3),))):
            with self.assertRaises((TypeError, ValueError)):
                d.history_torus_coordinates(h)

    def test_saturation_and_regularizer_rounding_visible(self):
        r = d.history_torus_coordinates(history(k=(1e20,), q=(0,), scalar=(1e20,)))
        self.assertEqual(r.r[0], r.r_max)
        self.assertEqual(r.H_z, r.z_max)
        self.assertEqual(r.chi[0], math.pi/2)
        EVIDENCE["fixtures"]["rounded_torus_boundary"] = dict(r=float(r.r[0]),
            H_z=r.H_z, z_max=r.z_max, chi=float(r.chi[0]), xyz=xyz(r).tolist())

    def test_conditional_inverse_independent_oracle(self):
        h = history(k=(.5, 1., 2.), q=(1, 3, 8), scalar=(.1, -.2, .8))
        r = d.history_torus_coordinates(h, R=3, r_max=.8)
        for i, (X, Y, Z) in enumerate(xyz(r)):
            s = math.hypot(X, Y)
            u = s-r.R
            radius = math.hypot(u, Z)
            theta, chi = math.atan2(Y, X), math.atan2(Z, u)
            self.assertGreater(radius, 0)
            self.assertLess(radius, r.r_max)
            k = radius/(r.r_max-radius)
            scalar = 2*r.H_z*chi/math.pi
            self.close("inverse kappa", k, h["kappa"][i], abs(k)+h["kappa"][i], 256)
            self.close("inverse scalar", scalar, h["z"][i], abs(scalar)+abs(h["z"][i]), 256)
            expected_angle = 2*math.pi*int(h["phi_index"][i])/12
            self.close("inverse angle cos", math.cos(theta), math.cos(expected_angle), 1, 128)

    def test_common_state_information_loss(self):
        oa, ob, clock, cfg = [1, 1, 1], [1, 1j, 1], z.Clock(q=2, t=.3), z.StagedConfig()
        a, b = z.observe_staged(oa, clock, cfg), z.observe_staged(ob, clock, cfg)
        self.assertEqual(z.state_norm(oa), z.state_norm(ob))
        self.assertEqual(a.z, b.z)
        np.testing.assert_array_equal(a.Z_macro, b.Z_macro)
        np.testing.assert_array_equal(a.Z_chiral, [0, 0, 0])
        np.testing.assert_array_equal(b.Z_chiral, [-1, 0, 1])
        self.assertFalse(np.array_equal(a.Z_total, b.Z_total))
        ha = history(k=(z.state_norm(oa),), q=(clock.q,), scalar=(a.z,))
        hb = history(k=(z.state_norm(ob),), q=(clock.q,), scalar=(b.z,))
        np.testing.assert_array_equal(xyz(d.cylinder_history_coordinates(ha)), xyz(d.cylinder_history_coordinates(hb)))
        np.testing.assert_array_equal(xyz(d.history_torus_coordinates(ha)), xyz(d.history_torus_coordinates(hb)))


class ContractTests(Checks):
    def test_input_validation_and_stored_config(self):
        for omega in ([True, 0, 0], ["1", 0, 0], [math.inf, 0, 0], [math.nan, 0, 0], [1, 2]):
            for fn in (lambda v: d.intensity_budget(v, config()),
                       lambda v: d.potential(v, config()), d.chiral_area_accounting):
                with self.assertRaises((ValueError, TypeError)):
                    fn(omega)
        for v in ([True, 0, 0], [1j, 0, 0], ["1", 0, 0], [0, math.nan, 0], [[1, 2, 3]]):
            with self.assertRaises((TypeError, ValueError)):
                d.quadratic_form(v)
        self.assertEqual(d.quadratic_form([1, 2, 3]), -4)
        for field, value in (("eps", True), ("g", "1"), ("k", (1, False, 2)), ("phase_strength", math.inf)):
            cfg = config()
            object.__setattr__(cfg, field, value)
            with self.assertRaises((TypeError, ValueError)):
                d.intensity_budget([1, 2, 3], cfg)
        # Constructor coercion has already happened; validate actual stored floats.
        self.assertEqual(d.potential([0]*3, DynamicsConfig(True, "0", 0, (1, 1, 1))), 0)
        with self.assertRaises(TypeError):
            d.intensity_budget([1, 2, 3], object())
        for weight in (True, "1", 1j, math.nan):
            with self.assertRaises((TypeError, ValueError)):
                d.readout_accounting(z.ZReadout(0, [0]*3, [0]*3, [0]*3, "staged"), alpha=weight, beta=0)

    def test_degree_range_and_underflow_failures(self):
        for magnitude in (1e200, 1e-200):
            with self.assertRaises(ResponsePrecisionError):
                d.intensity_budget([magnitude, 0, 0], config())
            with self.assertRaises(ResponsePrecisionError):
                d.quadratic_form([magnitude, 0, 0])
        with self.assertRaises(ResponsePrecisionError):
            d.potential([1e100, 0, 0], config())
        with self.assertRaises(ResponsePrecisionError):
            d.chiral_area_accounting([1e-100, 1e-100j, 0])
        # K2 observation can succeed where quartic diagnostic arithmetic cannot.
        obs = z.observe_staged([1e100, 1e100j, 0], z.Clock(), z.StagedConfig())
        self.assertTrue(np.isfinite(obs.Z_total).all())
        with self.assertRaises(ResponsePrecisionError):
            d.readout_accounting(obs, alpha=1, beta=.5)
        with self.assertRaises(ResponsePrecisionError):
            d.history_torus_coordinates(history(k=(1, 1), q=(0, 0), scalar=(1e-200, 1e200)))
        with self.assertRaises(ResponsePrecisionError):
            d.cylinder_point(sys.float_info.min, 1, 0)
        with self.assertRaises(ResponsePrecisionError):
            d.historical_alignment([1.1e308]*3, [1, 0, 0], [1, 0, 0])

    def test_detached_readonly_and_failure_atomicity(self):
        v = np.array([.2+.3j, -.4+.1j, .1-.2j])
        before = v.tobytes()
        budget = d.intensity_budget(v, config())
        area = d.chiral_area_accounting(v)
        obs = z.observe_staged(v, z.Clock(), z.StagedConfig())
        accounting = d.readout_accounting(obs, alpha=1, beta=.5)
        h = history()
        original = {k: a.tobytes() for k, a in h.items()}
        direct = d.direct_history_coordinates({"Z_total": [obs.Z_total]})
        cylinder, torus = d.cylinder_history_coordinates(h), d.history_torus_coordinates(h)
        arrays = [budget.component_intensities, budget.increment, budget.diagnostic_pre_sync_prediction,
                  area.chiral, accounting.blend_residual, direct.x, direct.y, direct.z,
                  cylinder.x, cylinder.y, cylinder.z, torus.x, torus.y, torus.z, torus.r, torus.chi,
                  d.cylinder_point(1, 0, 2)]
        for array in arrays:
            self.assertFalse(array.flags.writeable)
            self.assertFalse(np.shares_memory(array, v))
            with self.assertRaises(ValueError):
                array.flat[0] = 99
        with self.assertRaises(FrozenInstanceError):
            budget.remainder = 0
        for fn in (lambda: d.readout_accounting(obs, alpha=math.inf, beta=0),
                   lambda: d.history_torus_coordinates(h, R=0),
                   lambda: d.intensity_budget(v, object())):
            with self.assertRaises((ValueError, TypeError)):
                fn()
        self.assertEqual(before, v.tobytes())
        self.assertEqual(original, {k: a.tobytes() for k, a in h.items()})

    def test_runtime_import_and_call_boundary(self):
        tree = ast.parse(inspect.getsource(d))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported.add(node.module or ".")
        self.assertEqual(imported, {"dataclasses", "math", "numpy", ".", "_response_numeric", "dynamics", "z_manifold"})
        forbidden = {"step3", "step_ring", "_advance", "phase_sync", "advance_clock", "advance_ema"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
                self.assertNotIn(name, forbidden)
        self.assertFalse(any(name.startswith(("step", "run")) for name in vars(d)))
        root = Path(__file__).resolve().parents[2]
        code = (
            "import sys,json; import kernel_physics; "
            "assert 'kernel_physics.z_diagnostics' not in sys.modules; "
            "import kernel_physics.z_diagnostics as d; "
            "print(json.dumps({'loaded':list(sys.modules),'path':d.__file__}))"
        )
        proc = subprocess.run([sys.executable, "-B", "-c", code], cwd=root,
                              capture_output=True, text=True, check=True)
        data = json.loads(proc.stdout)
        self.assertTrue(Path(data["path"]).resolve().is_relative_to(root/"kernel_physics"))
        for name in ("kernel_physics.geometry", "kernel_physics.reference_scaffold", "kernel_physics.face_state"):
            self.assertNotIn(name, data["loaded"])
        self.assertFalse(any(n.startswith(("kernel_TO", "torment", "openai", "anthropic")) for n in data["loaded"]))
        EVIDENCE["fixtures"]["clean_process"] = dict(command=code, stdout=proc.stdout, stderr=proc.stderr, returncode=proc.returncode)

    def test_forbidden_runtime_functions_are_not_invoked(self):
        from contextlib import ExitStack
        from kernel_physics import dynamics
        with ExitStack() as stack:
            for module, names in ((dynamics, ("step3", "step_ring", "_advance", "phase_sync")),
                                  (z, ("advance_clock", "advance_ema"))):
                for name in names:
                    stack.enter_context(patch.object(module, name, side_effect=AssertionError("forbidden call")))
            v = [.2+.3j, -.4+.1j, .1-.2j]
            d.intensity_budget(v, config())
            d.potential(v, config())
            d.chiral_area_accounting(v)
            obs = z.observe_staged(v, z.Clock(), z.StagedConfig())
            d.readout_accounting(obs, alpha=1, beta=.5)
            d.historical_alignment(obs.Z_macro, obs.Z_chiral, obs.Z_total)
            d.direct_history_coordinates({"Z_total": [obs.Z_total]})
            d.cylinder_point(1, 0, 2)
            d.cylinder_history_coordinates(history())
            d.history_torus_coordinates(history())


if __name__ == "__main__":
    unittest.main()
