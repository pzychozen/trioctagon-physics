"""Raw Im(conj(Omega_j)*Omega_k) in historical pair order 23,31,12."""
from .numerics import multiply, add
from .types import Triad


def raw_chirality(omega):
    if type(omega) is not Triad:
        raise TypeError("Historical Triad required")
    result = []
    for j, k in ((1, 2), (2, 0), (0, 1)):
        a, b = omega.values[j].conjugate(), omega.values[k]
        # Imaginary component of the historical conjugated product; no unused
        # real component is evaluated, and no cross-product implementation is called.
        result.append(add((multiply(a.real, b.imag, "chirality real-imag"),
                           multiply(a.imag, b.real, "chirality imag-real")), "chirality imaginary sum"))
    return tuple(result)
