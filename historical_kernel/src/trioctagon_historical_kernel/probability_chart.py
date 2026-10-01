"""Historical naive binary64 abs/square/sum/divide/B-transpose sequence with gradual underflow."""
from dataclasses import dataclass
import sys
import numpy as np
from .constants import BASIS
from .numerics import NumericalFailure
from .types import Triad


@dataclass(frozen=True, slots=True)
class Chart:
    a: tuple
    sum: float
    weights: tuple
    chart: tuple
    classification: str
    square_to_zero: tuple
    subnormal_square: tuple
    normalized_weight_to_zero: tuple
    subnormal_weight: tuple
    subnormal_sum: bool
    warnings: tuple


def probability_chart(omega):
    if type(omega) is not Triad:
        raise TypeError("Historical Triad required")
    values = np.array(omega.values, dtype=np.complex128)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            magnitudes = np.abs(values)
            a = magnitudes**2
            total = np.sum(a)
            weights = a / total if total > 0 else a.copy()
            coordinates = np.array(BASIS).T @ weights
    except FloatingPointError as exc:
        raise NumericalFailure("legacy chart evaluation is nonfinite") from exc
    if not all(np.isfinite(v).all() for v in (magnitudes, a, total, weights, coordinates)):
        raise NumericalFailure("legacy chart output is nonfinite")
    a, weights, coordinates = (tuple(float(x) for x in v) for v in (a, weights, coordinates))
    total = float(total)
    nonzero = tuple(z != 0 for z in omega.values)
    kind = "NORMALIZED_NONZERO" if total > 0 else "NONZERO_INPUT_SQUARED_TO_ZERO" if any(nonzero) else "EXACT_ZERO_INPUT"
    square_zero = tuple(nz and x == 0 for nz, x in zip(nonzero, a))
    sub_square = tuple(0 < x < sys.float_info.min for x in a)
    weight_zero = tuple(x > 0 and total > 0 and w == 0 for x, w in zip(a, weights))
    sub_weight = tuple(0 < w < sys.float_info.min for w in weights)
    sub_sum = 0 < total < sys.float_info.min
    flags = (kind == "NONZERO_INPUT_SQUARED_TO_ZERO", any(square_zero), any(sub_square), any(weight_zero), any(sub_weight), sub_sum)
    names = ("NONZERO_INPUT_ZERO_BRANCH", "SQUARE_UNDERFLOW", "SUBNORMAL_SQUARED_MAGNITUDE", "WEIGHT_UNDERFLOW", "SUBNORMAL_WEIGHT", "SUBNORMAL_SUM")
    return Chart(a, total, weights, coordinates, kind, square_zero, sub_square, weight_zero,
                 sub_weight, sub_sum, tuple(name for name, selected in zip(names, flags) if selected))
