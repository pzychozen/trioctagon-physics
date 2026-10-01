"""Independently implemented H5 strict response primitives, separate from recurrence/chart."""
import math
import sys


class NumericalFailure(FloatingPointError):
    """The complete requested evaluation is outside its frozen numerical domain."""


def finite(value, name):
    if type(value) not in (float, int):
        raise TypeError(name + " requires an explicit real scalar, without booleans")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(name + " is not finite binary64") from exc
    if not math.isfinite(result):
        raise ValueError(name + " is not finite binary64")
    return result


def checked(value, name, *, nonzero=False):
    if not math.isfinite(value):
        raise NumericalFailure(name + ": nonfinite result")
    if value == 0:
        if nonzero:
            raise NumericalFailure(name + ": nonzero result rounded to zero")
        return 0.0
    if abs(value) < sys.float_info.min:
        raise NumericalFailure(name + ": nonzero subnormal result")
    return value


def multiply(left, right, name):
    if left == 0 or right == 0:
        return 0.0
    return checked(float(left) * float(right), name, nonzero=True)


def add(terms, name):
    try:
        result = math.fsum(terms)
    except (OverflowError, ValueError) as exc:
        raise NumericalFailure(name + ": sum is not representable") from exc
    return checked(result, name)


def complex_multiply(left, right, name):
    rr = multiply(left.real, right.real, name)
    ii = multiply(left.imag, right.imag, name)
    ri = multiply(left.real, right.imag, name)
    ir = multiply(left.imag, right.real, name)
    return complex(add((rr, -ii), name), add((ri, ir), name))


def stable_norm(omega):
    from .types import Triad
    if type(omega) is not Triad:
        raise TypeError("Historical Triad required")
    coordinates = tuple(component for z in omega.values for component in (z.real, z.imag))
    return checked(math.hypot(*coordinates), "six-real norm", nonzero=any(x != 0 for x in coordinates))
