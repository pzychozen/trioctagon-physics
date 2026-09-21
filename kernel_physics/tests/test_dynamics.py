import cmath
import math
import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import patch

import numpy as np

from kernel_physics.dynamics import DynamicsConfig, L3, arg0, phase_sync, step3, step_ring


class DynamicsTests(unittest.TestCase):
    def test_one_step_against_hand_calculated_pre_sync_state(self):
        # Paper A formula gives X=(1/2+3i/5, 6i/5, -3/5+6i/5).
        omega = np.array([1, 2j, -1+1j])
        cfg = DynamicsConfig(0.1, 0.2, 0.17, (2, 3, 4))
        a, b, c = math.atan2(6, 5), math.pi/2, math.atan2(2, -1)
        expected = [
            cmath.rect(math.sqrt(61)/10, a + 0.17*(math.sin(3*(b-a))+math.sin(3*(c-a)))),
            cmath.rect(6/5, b + 0.17*(math.sin(3*(a-b))+math.sin(3*(c-b)))),
            cmath.rect(3*math.sqrt(5)/5, c + 0.17*(math.sin(3*(a-c))+math.sin(3*(b-c)))),
        ]
        np.testing.assert_allclose(step3(omega, cfg), expected, rtol=2e-15, atol=2e-15)

    def test_one_step_is_deterministic(self):
        omega = [0.5+0.25j, -0.7j, 0.8-0.1j]
        cfg = DynamicsConfig(0.05, 0.2, 0.3, (1, 1.2, 0.8))
        np.testing.assert_array_equal(step3(omega, cfg), step3(omega, cfg))

    def test_phase_sync_preserves_component_amplitudes(self):
        values = np.array([1+2j, -3+0.5j, 0, 0.3-0.2j, 2, -1j])
        for strength in (0.2, -0.1):
            np.testing.assert_allclose(np.abs(phase_sync(values, strength)),
                                       np.abs(values), rtol=2e-15, atol=2e-15)

    def test_simultaneous_sync_on_known_phase_triad(self):
        phase, strength = math.pi/6, 0.2
        state = [1, cmath.rect(2, phase), cmath.rect(3, -phase)]
        # Initial sine sums are (0,-1,+1); no updated phase enters another sum.
        expected = [1, cmath.rect(2, phase-strength), cmath.rect(3, -phase+strength)]
        np.testing.assert_allclose(phase_sync(state, strength), expected, atol=2e-15)

    def test_lambda_zero_is_bitwise_identity_without_arg0(self):
        values = np.array([complex(-0.0, -0.0), 1+2j, -2-3j])
        with patch("kernel_physics.dynamics.arg0", side_effect=AssertionError):
            actual = phase_sync(values, 0)
        self.assertEqual(actual.tobytes(), values.tobytes())
        self.assertFalse(np.shares_memory(actual, values))

    def test_arg0_overrides_all_signed_complex_zeros(self):
        zeros = np.array([complex(x, y) for x in (0.0, -0.0) for y in (0.0, -0.0)])
        angles = arg0(zeros)
        np.testing.assert_array_equal(angles, np.zeros(4))
        self.assertFalse(np.any(np.signbit(angles)))
        np.testing.assert_allclose(arg0([1, 1j, -1j]), [0, math.pi/2, -math.pi/2])

    def test_zero_state_stays_zero(self):
        cfg = DynamicsConfig(0.2, 0.1, 0.3, (1, 2, 3))
        np.testing.assert_array_equal(step3([0, 0, 0], cfg), np.zeros(3))

    def test_nonzero_state_can_reach_zero_before_sync(self):
        cfg = DynamicsConfig(1, 0, 0.2, (0, 1, 1))
        np.testing.assert_array_equal(step3([1, 0, 0], cfg), np.zeros(3))

    def test_global_phase_equivariance_away_from_pre_sync_zeros(self):
        state = np.array([0.5+0.25j, 0.7-0.2j, -0.2+0.3j])
        cfg = DynamicsConfig(0.05, 0.1, 0.23, (1, 1.2, 0.8))
        pre = state + cfg.eps*state*(np.array(cfg.k)-np.abs(state)**2) + cfg.g*np.array(L3)@state
        self.assertTrue(np.all(np.abs(pre) > 0.1))
        for phase in (0.37, 2.1, -2.4):
            factor = cmath.exp(1j*phase)
            np.testing.assert_allclose(step3(factor*state, cfg),
                                       factor*step3(state, cfg), rtol=2e-14, atol=2e-14)

    def test_lambda_zero_equivariance_including_zero_components(self):
        state = np.array([0, 1+1j, -1j])
        cfg = DynamicsConfig(0.2, 0, 0, (1, 2, 3))
        factor = cmath.exp(0.71j)
        np.testing.assert_allclose(step3(factor*state, cfg),
                                   factor*step3(state, cfg), atol=2e-15)

    def test_zero_convention_does_not_claim_general_phase_equivariance(self):
        cfg = DynamicsConfig(0, 0, 0.2, (1, 1, 1))
        phase = math.pi/6
        state = np.array([0, 1, 1])
        shifted = cmath.exp(1j*phase)*state
        expected = [0, cmath.exp(1j*(phase-0.2)), cmath.exp(1j*(phase-0.2))]
        np.testing.assert_allclose(step3(shifted, cfg), expected, atol=2e-15)
        self.assertGreater(np.linalg.norm(step3(shifted, cfg)
                                         - cmath.exp(1j*phase)*step3(state, cfg)), 0.1)

    def test_l3_spectrum(self):
        np.testing.assert_allclose(np.linalg.eigvalsh(L3), [-3, -3, 0], atol=2e-15)

    def test_input_state_and_config_remain_unchanged(self):
        state = np.array([0.5+0.25j, 0.7-0.2j, -0.2+0.3j])
        original = state.copy()
        supplied_k = [1, 2, 3]
        cfg = DynamicsConfig(0.1, 0.2, 0.3, supplied_k)
        supplied_k[0] = 99
        self.assertEqual(cfg.k, (1, 2, 3))
        with self.assertRaises(FrozenInstanceError):
            cfg.g = 4
        result = step3(state, cfg)
        np.testing.assert_array_equal(state, original)
        self.assertFalse(np.shares_memory(result, state))

    def test_invalid_shapes_and_parameters_rejected(self):
        cfg = DynamicsConfig(0.1, 0.2, 0.3, (1, 1, 1))
        for bad in ([1, 2], [1, 2, 3, 4], [[1, 2, 3]]):
            with self.assertRaises(ValueError):
                step3(bad, cfg)
        with self.assertRaises(ValueError):
            step_ring([1, 2, 3, 4], cfg)
        with self.assertRaises(ValueError):
            DynamicsConfig(0, 0, 0, (1, 2))
        with self.assertRaises(ValueError):
            DynamicsConfig(0, np.complex128(1+2j), 0, (1, 2, 3))

    def test_nonfinite_input_is_not_silently_evolved(self):
        cfg = DynamicsConfig(0.1, 0.2, 0.3, (1, 1, 1))
        for bad in (float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                step3([bad, 1, 2], cfg)
            with self.assertRaises(ValueError):
                DynamicsConfig(bad, 0, 0, (1, 2, 3))


if __name__ == "__main__":
    unittest.main()
