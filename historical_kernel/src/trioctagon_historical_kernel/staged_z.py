"""Independent staged K readout with mandatory finite positive envelope evaluation."""
import math
from .constants import GAMMA
from .numerics import checked, multiply, NumericalFailure
from .response import harmonic, observe


def observe_staged(omega, clock):
    scalar = harmonic(omega, clock)
    exponent = multiply(-GAMMA, clock.t, "staged envelope exponent")
    try:
        envelope = math.exp(exponent)
    except OverflowError as exc:
        raise NumericalFailure("staged envelope overflow") from exc
    envelope = checked(envelope, "staged envelope", nonzero=True)
    return observe(omega, clock, multiply(scalar, envelope, "staged scalar"))
