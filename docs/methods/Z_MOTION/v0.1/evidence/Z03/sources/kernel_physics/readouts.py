"""Raw channel chirality only; no imposed decay envelope or physical face map."""
import numpy as np

from ._response_numeric import complex_vector, product, total


def z_chiral(omega):
    """Re(omega) cross Im(omega); a fresh real three-vector, without normalization.

    Checked real products reject subnormal/overflowing intermediates. Near
    cancellation, a zero or small computed value is not an exact-zero proof.
    """
    v = complex_vector(omega, 3, "omega")
    return np.array([total((product(v[j].real, v[k].imag, "z_chiral product"),
                            -product(v[k].real, v[j].imag, "z_chiral product")),
                           "z_chiral difference")
                     for j, k in ((1, 2), (2, 0), (0, 1))])
