"""The explicitly chosen lens_area_norm_v1 toy response, not recovered physics.

P(theta, xi) = sqrt((2 theta-sin(2 theta))/pi) (xi tensor f0).
Tensor order is helicity-major. No normalization, random replacement or clipping.
Nonzero subnormal results/products raise ResponsePrecisionError; exact input
zeros return canonical complex zero after ALL inputs have been validated.
"""
import math

import numpy as np

from ._response_numeric import (ResponsePrecisionError, checked_real, complex_vector,
                               product, real_scalar, scale_complex)

RESPONSE_ID = "lens_area_norm_v1"


def _theta(value):
    theta = real_scalar(value, "theta")
    if not 0 <= theta <= math.pi/2:
        raise ValueError("theta must be in [0, pi/2]")
    return theta


def theta_from_lens(radius, separation):
    """Equal-radius lens chart; rounding of input separation is not invertible."""
    r = real_scalar(radius, "radius")
    d = real_scalar(separation, "separation")
    if r <= 0 or d < 0:
        raise ValueError("radius must be positive and separation nonnegative")
    ratio = d/r  # avoids overflow in 2*r for a valid large-radius lens
    if not 0 <= ratio <= 2:
        raise ValueError("separation must be <= 2*radius")
    if d != 0 and ratio == 0:
        raise ResponsePrecisionError("separation/radius underflow; use theta or higher precision")
    half_ratio = product(ratio, .5, "lens separation ratio")
    return math.acos(half_ratio)


def _small_factor(t):
    """I(t)/t^3 through degree ten; same degree-13 area Taylor polynomial."""
    if t < 1e-8:
        # The relative omitted correction is <= t^2/5, below binary64 rounding.
        # Do not evaluate t*t where that irrelevant correction can underflow.
        return 4/(3*math.pi)
    z = t*t
    coefficients = [(-1)**(j+1)*2**(2*j+1)/math.factorial(2*j+1)
                    for j in range(1, 7)]
    value = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        value = coefficient+z*value
    return value/math.pi


def lens_area_fraction(theta):
    """Area/parent-disk area; positive subnormal or lost area raises explicitly."""
    t = _theta(theta)
    if t == 0:
        return 0.0
    if t == math.pi/2:
        return 1.0
    if t < .1:
        mantissa, exponent = math.frexp(t)
        value = math.ldexp(_small_factor(t)*mantissa**3, 3*exponent)
    else:
        value = (2*t-math.sin(2*t))/math.pi
    return checked_real(value, "lens area", nonzero=True)


def lens_area_gain(theta):
    """Evaluate sqrt(I) directly: representable gain need not imply usable I."""
    t = _theta(theta)
    if t == 0:
        return 0.0
    if t == math.pi/2:
        return 1.0
    if t < .1:
        mantissa, exponent = math.frexp(t)
        power, odd = divmod(3*exponent, 2)
        value = math.ldexp(math.sqrt(_small_factor(t)*mantissa**3*2**odd), power)
    else:
        value = math.sqrt(lens_area_fraction(t))
    return checked_real(value, "lens gain", nonzero=True)


def prepare_area_response(theta, xi):
    """Return a fresh raw complex128 six-vector; arbitrary incident helicity.

    Numerical domain: gain and each nonzero real/imaginary product must remain
    normal binary64. Exact zero is tested componentwise, never via norm squared.
    """
    t = _theta(theta)
    incident = complex_vector(xi, 2, "xi")
    if t == 0 or np.all(incident == 0):
        return np.zeros(6, dtype=np.complex128)
    gain = lens_area_gain(t)
    result = np.empty(6, dtype=np.complex128)
    for i, value in enumerate(incident):
        scaled = scale_complex(gain, complex(value), "prepared amplitude")
        block = complex(product(scaled.real, 1/math.sqrt(3), "prepared component"),
                        product(scaled.imag, 1/math.sqrt(3), "prepared component"))
        result[3*i:3*i+3] = block
    return result
