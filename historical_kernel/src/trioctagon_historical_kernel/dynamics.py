"""Raw deterministic unforced triad recurrence. No time multiplier or readout feedback."""
import numpy as np
from .constants import K, KProfile, EPSILON, COUPLING
from .numerics import NumericalFailure
from .phase import synchronize
from .types import Triad


def step(omega, profile):
    if type(omega) is not Triad or type(profile) is not KProfile:
        raise TypeError("Historical Triad and explicit KProfile required")
    state = np.array(omega.values, dtype=np.complex128)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            graph = np.array(((-2, 1, 1), (1, -2, 1), (1, 1, -2))) @ state
            radial = EPSILON * state * (np.array(K[profile]) - np.abs(state)**2)
            before_phase = state + radial + COUPLING * graph
    except FloatingPointError as exc:
        raise NumericalFailure("triad recurrence is nonfinite") from exc
    if not np.isfinite(before_phase).all():
        raise NumericalFailure("pre-phase state is nonfinite")
    return synchronize(Triad(tuple(complex(z) for z in before_phase)))
