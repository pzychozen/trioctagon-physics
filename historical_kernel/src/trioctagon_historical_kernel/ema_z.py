"""Independent H observation and separate, explicitly invoked memory advancement."""
from .constants import INNOVATION, RETENTION
from .numerics import complex_multiply, add, checked, multiply
from .response import harmonic, observe
from .types import Triad, Memory


def cubic_j(omega):
    if type(omega) is not Triad:
        raise TypeError("Historical Triad required")
    a, b, c = omega.values
    pair = complex_multiply(a, b.conjugate(), "left-associated cubic pair")
    return complex_multiply(pair, c, "left-associated cubic triple").imag


def advance_ema(omega, memory):
    if type(memory) is not Memory:
        raise TypeError("Historical Memory required")
    j = cubic_j(omega)
    f = checked(j / add((1.0, abs(j)), "cubic saturation denominator"), "saturated cubic", nonzero=j != 0)
    retained = multiply(RETENTION, memory.value, "EMA retention")
    innovation = multiply(INNOVATION, f, "EMA literal .01 innovation")
    return Memory(add((retained, innovation), "EMA update sum"))


def observe_ema(omega, clock, memory):
    """Inspect CURRENT memory; intentionally contains no cubic or advancement call."""
    if type(memory) is not Memory:
        raise TypeError("Historical Memory required")
    scalar = add((harmonic(omega, clock), memory.value), "H scalar plus current memory")
    return observe(omega, clock, scalar)
