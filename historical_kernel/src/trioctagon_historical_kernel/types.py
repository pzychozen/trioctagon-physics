"""Small immutable scientific types; no protocol records or mutable NumPy state."""
from dataclasses import dataclass
import math
from .numerics import finite


@dataclass(frozen=True, slots=True)
class Triad:
    values: tuple[complex, complex, complex]

    def __post_init__(self):
        if type(self.values) is not tuple or len(self.values) != 3:
            raise TypeError("Historical state is an explicit tuple of three complex values")
        if any(type(z) is not complex for z in self.values):
            raise TypeError("Historical channels must be explicit Python complex values")
        if any(not math.isfinite(x) for z in self.values for x in (z.real, z.imag)):
            raise ValueError("Historical state must be finite binary64")


@dataclass(frozen=True, slots=True)
class Clock:
    q: int = 0
    t: float = 0.0

    def __post_init__(self):
        if type(self.q) is not int or not 0 <= self.q < 12:
            raise ValueError("Historical clock sector must be an integer in 0..11")
        value = finite(self.t, "clock time")
        if value < 0:
            raise ValueError("Historical time must be nonnegative")
        object.__setattr__(self, "t", value)


@dataclass(frozen=True, slots=True)
class Memory:
    value: float = 0.0

    def __post_init__(self):
        value = finite(self.value, "memory")
        if abs(value) > 1:
            raise ValueError("Historical memory requires abs(m) <= 1")
        object.__setattr__(self, "value", value)


@dataclass(frozen=True, slots=True)
class Observation:
    z: float
    M: tuple[float, float, float]
    C: tuple[float, float, float]
    T: tuple[float, float, float]


ZERO_OBSERVATION = Observation(0.0, (0.0,)*3, (0.0,)*3, (0.0,)*3)
