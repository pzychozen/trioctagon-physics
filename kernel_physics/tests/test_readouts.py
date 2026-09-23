import unittest

import numpy as np

from kernel_physics.boundary_response import ResponsePrecisionError
from kernel_physics.readouts import z_chiral
from kernel_physics.srg import fourier_basis


class ReadoutTests(unittest.TestCase):
    def test_raw_fourier_orientations_and_scaling(self):
        F = fourier_basis()
        for j, sign in enumerate((0, -.5, .5)):
            np.testing.assert_allclose(z_chiral(F[:, j]), sign*F[:, 0].real, atol=1e-15)
            scalar = 2-.7j
            np.testing.assert_allclose(z_chiral(scalar*F[:, j]), abs(scalar)**2*sign*F[:, 0].real, atol=2e-15)

    def test_hand_calculated_cross_product_and_immutability(self):
        omega = np.array([1+4j, 2+5j, 3+6j]); original = omega.copy()
        np.testing.assert_array_equal(z_chiral(omega), [-3, 6, -3])
        np.testing.assert_array_equal(omega, original)
        self.assertFalse(np.shares_memory(z_chiral(omega), omega))
        self.assertFalse(np.signbit(z_chiral([0, complex(-0., -0.), 0])).any())

    def test_tiny_readout_is_scaled_and_nonzero(self):
        state = 1e-140*fourier_basis()[:, 1]
        result = z_chiral(state)
        self.assertTrue(np.all(result != 0))
        np.testing.assert_allclose(result/1e-280, -fourier_basis()[:, 0].real/2, rtol=3e-15, atol=0)

    def test_precision_and_input_failures(self):
        for scale in (1e-170, 1e200):
            with self.assertRaises(ResponsePrecisionError):
                z_chiral(scale*fourier_basis()[:, 1])
        for bad in ([1, 2], [True, 2, 3], ['1', '2', '3'], [1, np.inf, 3]):
            with self.assertRaises((TypeError, ValueError)):
                z_chiral(bad)


if __name__ == '__main__':
    unittest.main()
