"""Strict binary64 contracts shared only by the opt-in response adapters.

Nonzero subnormal outputs/intermediate products are deliberately rejected.
This conservative domain avoids silently labelling loss of precision as zero;
it is not a certification of cancellation accuracy for all finite inputs.
"""
import math
import numbers
import sys

import numpy as np


class ResponsePrecisionError(FloatingPointError):
    """The requested evaluation exceeds this adapter's numerical domain."""


def real_scalar(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Real):
        raise TypeError(f"{name} must be a real numeric scalar (no bool/string/complex)")
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be finite in binary64") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite in binary64")
    if result == 0 and value != 0:
        raise ResponsePrecisionError(f"{name} lost a nonzero value during conversion")
    return result


def complex_vector(value, length, name):
    raw = np.asarray(value, dtype=object)
    if raw.shape != (length,):
        raise ValueError(f"{name} must have shape ({length},)")
    result = np.empty(length, dtype=np.complex128)
    for i, item in enumerate(raw):
        if isinstance(item, (bool, np.bool_)) or not isinstance(item, numbers.Complex):
            raise TypeError(f"{name} components must be numeric, without booleans or strings")
        try:
            z = complex(item)
        except (ValueError, OverflowError) as exc:
            raise ValueError(f"{name} must be finite in complex128") from exc
        if not math.isfinite(z.real) or not math.isfinite(z.imag):
            raise ValueError(f"{name} must have finite components")
        if z == 0 and item != 0:
            raise ResponsePrecisionError(f"{name} lost a nonzero component during conversion")
        result[i] = z
    return result


def checked_real(value, name, *, nonzero=False):
    if not math.isfinite(value):
        raise ResponsePrecisionError(f"{name}: nonfinite numerical result")
    if value == 0:
        if nonzero:
            raise ResponsePrecisionError(f"{name}: nonzero result underflowed to zero")
        return 0.0
    if abs(value) < sys.float_info.min:
        raise ResponsePrecisionError(f"{name}: subnormal result needs higher precision")
    return value


def product(a, b, name):
    if a == 0 or b == 0:
        return 0.0
    # Use Python binary64 multiplication so failures are raised through our
    # contract, not emitted first as NumPy warnings outside an errstate block.
    return checked_real(float(a)*float(b), name, nonzero=True)


def total(values, name):
    try:
        value = math.fsum(values)
    except OverflowError as exc:
        raise ResponsePrecisionError(f"{name}: sum overflow") from exc
    # No tolerance-based zeroing: cancellation may produce zero in binary64.
    return checked_real(value, name)


def complex_product(a, b, name):
    return complex(total((product(a.real, b.real, name), -product(a.imag, b.imag, name)), name),
                   total((product(a.real, b.imag, name), product(a.imag, b.real, name)), name))


def scale_complex(scale, value, name):
    return complex(product(scale, value.real, name), product(scale, value.imag, name))


def bra_dot(bra, vector, name):
    terms = [complex_product(complex(a).conjugate(), complex(b), name)
             for a, b in zip(bra, vector)]
    return complex(total((z.real for z in terms), name), total((z.imag for z in terms), name))


def checked_array(values, name):
    result = np.array(values, copy=True)
    for value in result.flat:
        checked_real(float(value.real), name)
        checked_real(float(value.imag), name)
    result[result == 0] = 0  # canonical whole-component zero; never a threshold
    return result
