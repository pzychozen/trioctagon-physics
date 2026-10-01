"""Fixed twelve-sector clock and repeated binary64 .1 addition; never modifies Omega."""
from .constants import PI, SECTORS, DT
from .numerics import checked, multiply, add, NumericalFailure
from .types import Clock


def angle(clock):
    if type(clock) is not Clock:
        raise TypeError("Historical Clock required")
    q = clock.q % SECTORS
    fraction = checked(q / SECTORS, "sector fraction", nonzero=q != 0)
    return multiply(2.0 * PI, fraction, "clock angle")


def advance(clock):
    if type(clock) is not Clock:
        raise TypeError("Historical Clock required")
    time = add((clock.t, DT), "repeated time addition")
    if time == clock.t:
        raise NumericalFailure("nonzero clock increment was lost")
    return Clock((clock.q + 1) % SECTORS, time)
