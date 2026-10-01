"""Simultaneous fixed harmonic-three phase law, with H4 canonical exact-zero semantics."""
import numpy as np
from .constants import HARMONIC, PHASE_STRENGTH
from .numerics import NumericalFailure
from .types import Triad


def synchronize(omega):
    if type(omega) is not Triad:
        raise TypeError("Historical Triad required")
    v = np.array(omega.values, dtype=np.complex128)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            angles = np.angle(v)
            angles[v == 0] = 0.0
            # Fixed other-channel indices; both differences use the original phases.
            left = np.sin(HARMONIC * (angles[[2, 0, 1]] - angles))
            right = np.sin(HARMONIC * (angles[[1, 2, 0]] - angles))
            new_angles = angles + PHASE_STRENGTH * (left + right)
            result = np.abs(v) * np.exp(1j * new_angles)
            result[v == 0] = 0j
    except FloatingPointError as exc:
        raise NumericalFailure("phase evaluation is nonfinite") from exc
    if not np.isfinite(result).all():
        raise NumericalFailure("phase output is nonfinite")
    return Triad(tuple(complex(z) for z in result))
