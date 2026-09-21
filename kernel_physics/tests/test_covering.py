import unittest

import numpy as np
import sympy as sp

from kernel_physics.covering import cycle_laplacian, isometric_pullback, pullback_matrix
from kernel_physics.dynamics import DynamicsConfig, L3, step3, step_ring


class CoveringTests(unittest.TestCase):
    DIVISORS = ((1, 1), (2, 1), (2, 2), (3, 3), (6, 3), (8, 2),
                (9, 3), (12, 3), (12, 4), (24, 3))

    def test_degenerate_cycles_retain_incidence_multiplicity(self):
        self.assertEqual(cycle_laplacian(1), sp.zeros(1))
        self.assertEqual(cycle_laplacian(2), sp.Matrix([[-2, 2], [2, -2]]))

    def test_divisor_intertwining_exactly(self):
        for m, d in self.DIVISORS:
            with self.subTest(M=m, d=d):
                p = pullback_matrix(m, d)
                self.assertEqual(cycle_laplacian(m)*p-p*cycle_laplacian(d),
                                 sp.zeros(m, d))

    def test_q_isometry_and_compression_exactly(self):
        for m, d in self.DIVISORS:
            with self.subTest(M=m, d=d):
                q = isometric_pullback(m, d)
                self.assertEqual(sp.simplify(q.H*q), sp.eye(d))
                self.assertEqual(sp.simplify(q.H*cycle_laplacian(m)*q),
                                 cycle_laplacian(d))

    def test_twelve_three_restriction_is_the_printed_l3(self):
        p, q = pullback_matrix(12, 3), isometric_pullback(12, 3)
        printed = sp.Matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
        self.assertEqual(q.H*cycle_laplacian(12)*q, printed)
        self.assertEqual(p.H*cycle_laplacian(12)*p, 4*printed)
        self.assertEqual(cycle_laplacian(3), sp.Matrix(L3))
        self.assertEqual(printed.eigenvals(), {-3: 2, 0: 1})

    def test_residue_pullback_including_d_greater_than_m(self):
        self.assertEqual(pullback_matrix(6, 3)*sp.Matrix([2, 5, 7]),
                         sp.Matrix([2, 5, 7, 2, 5, 7]))
        self.assertEqual(pullback_matrix(2, 4),
                         sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]]))

    def test_nondivisor_intertwining_fails_without_invariance_claim(self):
        # (3,2) is deliberately included: intertwining fails even though
        # the exceptional image subspace is invariant in Paper A.
        for m, d in ((5, 3), (3, 2), (7, 4), (2, 4)):
            with self.subTest(M=m, d=d):
                p = pullback_matrix(m, d)
                self.assertNotEqual(cycle_laplacian(m)*p-p*cycle_laplacian(d),
                                    sp.zeros(m, d))
                with self.assertRaises(ValueError):
                    isometric_pullback(m, d)

    def test_nonlinear_lift_at_six_twelve_and_twenty_four(self):
        state = np.array([0.5+0.25j, -0.7+0.2j, 0.3-0.6j])
        cfg = DynamicsConfig(0.07, 0.13, 0.31, (0.9, 1.2, 0.7))
        for m in (3, 6, 12, 24):
            with self.subTest(M=m):
                p = np.array(pullback_matrix(m, 3), dtype=float)
                np.testing.assert_allclose(step_ring(p@state, cfg),
                                           p@step3(state, cfg), rtol=2e-14, atol=2e-14)

    def test_nonlinear_lift_at_zero_and_zero_pre_sync_components(self):
        cases = (
            ([0, 1, 1], DynamicsConfig(0, 0, 0.2, (1, 1, 1))),
            ([1, 0, 0], DynamicsConfig(1, 0, 0.2, (0, 1, 1))),
            ([0, 0, 0], DynamicsConfig(0.1, 0.2, 0.3, (1, 2, 3))),
            ([0, 1+1j, -1j], DynamicsConfig(0.1, 0.2, 0, (1, 2, 3))),
        )
        for m in (6, 12, 24):
            for state, cfg in cases:
                with self.subTest(M=m, state=state, strength=cfg.phase_strength):
                    p = np.array(pullback_matrix(m, 3), dtype=float)
                    np.testing.assert_allclose(step_ring(p@state, cfg),
                                               p@step3(state, cfg), rtol=2e-14, atol=2e-14)

    def test_ring_evolves_off_sector_state_with_periodic_wrap(self):
        cfg = DynamicsConfig(0, 0.25, 0, (1, 1, 1))
        np.testing.assert_array_equal(step_ring([1, 2, 3, 4, 5, 6], cfg),
                                      [2.5, 2, 3, 4, 5, 4.5])

    def test_cycle_size_validation(self):
        for size in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                cycle_laplacian(size)
            with self.assertRaises(ValueError):
                pullback_matrix(12, size)


if __name__ == "__main__":
    unittest.main()
