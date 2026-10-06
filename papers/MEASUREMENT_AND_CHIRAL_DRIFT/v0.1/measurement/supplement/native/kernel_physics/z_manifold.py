"""Opt-in Paper-E readouts; never a recurrence, geometry map or feedback law.

Binary64/complex128 evaluation reuses the conservative response precision
contract. Intermediate nonzero subnormals, overflow and lost nonzero products
raise ResponsePrecisionError. Successful scalar evaluation does not guarantee
that cubic, chirality or blended-vector evaluation will succeed.
"""
from dataclasses import dataclass, field
import math
import numbers

import numpy as np

from . import readouts
from ._response_numeric import (
    ResponsePrecisionError, checked_real, complex_product, complex_vector,
    product, real_scalar, total,
)


def _integer(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Integral):
        raise TypeError(f"{name} must be an integer, excluding booleans")
    return int(value)


def _require(value, cls, name):
    if not isinstance(value, cls):
        raise TypeError(f"{name} must be {cls.__name__}")
    return value


def _freeze(values):
    result = np.array(values, copy=True)
    result.setflags(write=False)
    return result


def _real_vector(values, name):
    raw = np.asarray(values, dtype=object)
    if raw.shape != (3,):
        raise ValueError(f"{name} must have shape (3,)")
    return _freeze([checked_real(real_scalar(v, name), name) for v in raw])


@dataclass(frozen=True, slots=True)
class Clock:
    """Explicit clock; q stays integer. Historical N=12, q_step=1.

    q is retained as supplied; angle evaluation first reduces q modulo N
    using integer arithmetic. This periodic evaluation never changes Omega.
    """
    q: int = 0
    N: int = 12
    t: float = 0.0
    q_step: int = 1

    def __post_init__(self):
        for name in ("q", "N", "q_step"):
            object.__setattr__(self, name, _integer(getattr(self, name), name))
        if self.N <= 0:
            raise ValueError("N must be positive")
        object.__setattr__(self, "t", real_scalar(self.t, "t"))


def clock_angle(clock):
    """2*pi*(q mod N)/N; no conversion of a huge raw q to binary64."""
    _require(clock, Clock, "clock")
    q = clock.q % clock.N
    ratio = q / clock.N
    ratio = checked_real(ratio, "clock sector fraction", nonzero=(q != 0))
    return product(2.0 * math.pi, ratio, "clock angle")


def advance_clock(clock, dt):
    """Return a new clock; dt is explicit (historical runner used 0.1)."""
    _require(clock, Clock, "clock")
    dt = real_scalar(dt, "dt")
    t = total((clock.t, dt), "clock time addition")
    if dt != 0 and t == clock.t:
        raise ResponsePrecisionError("nonzero dt lost: clock time did not advance")
    return Clock((clock.q + clock.q_step) % clock.N, clock.N, t, clock.q_step)


def _config_reals(config, names):
    for name in names:
        object.__setattr__(config, name, real_scalar(getattr(config, name), name))


@dataclass(frozen=True, slots=True)
class StagedConfig:
    """Literal K defaults; signed finite coefficients are allowed."""
    lambda_vp: float = 0.618
    gamma: float = 0.577
    theta_lock: float = 0.244
    alpha: float = 1.0
    beta: float = 0.5

    def __post_init__(self):
        _config_reals(self, ("lambda_vp", "gamma", "theta_lock", "alpha", "beta"))


def state_norm(omega):
    """Stable six-real-component hypot, retaining raw state scale."""
    v = complex_vector(omega, 3, "omega")
    return checked_real(math.hypot(*(float(c) for z in v for c in (z.real, z.imag))),
                        "state norm", nonzero=bool(np.any(v != 0)))


def saturated_norm(omega):
    """rho=kappa/(1+kappa); floating rho may round to 1."""
    kappa = state_norm(omega)
    denominator = total((1.0, kappa), "rho denominator")
    return checked_real(kappa / denominator, "rho", nonzero=(kappa != 0))


def _harmonic(omega, clock, config):
    rho = saturated_norm(omega)
    theta = clock_angle(clock)
    angle = product(3.0, total((theta, -config.theta_lock), "lock difference"),
                    "harmonic angle")
    cosine = checked_real(math.cos(angle), "harmonic cosine")
    return product(product(config.lambda_vp, rho, "harmonic amplitude"),
                   cosine, "harmonic scalar")


def staged_scalar(omega, clock, config):
    """K scalar, left-associated checked products and an explicit envelope.

    No envelope bypass is made for zero amplitude; its numerical evaluation
    still has to succeed. No finite-time underflow is labelled exact decay.
    """
    _require(config, StagedConfig, "config")
    _require(clock, Clock, "clock")
    harmonic = _harmonic(omega, clock, config)
    exponent = product(-config.gamma, clock.t, "envelope exponent")
    try:
        envelope = math.exp(exponent)
    except OverflowError as exc:
        raise ResponsePrecisionError("exponential envelope overflow") from exc
    envelope = checked_real(envelope, "exponential envelope", nonzero=True)
    return product(harmonic, envelope, "staged scalar")


def macro_vector(z, clock):
    """Fresh read-only M=z*(cos(theta),sin(theta),1), without normalization."""
    z = checked_real(real_scalar(z, "z"), "z")
    theta = clock_angle(clock)
    return _freeze([product(z, math.cos(theta), "macro x"),
                    product(z, math.sin(theta), "macro y"), z])


def blend_vectors(macro, chiral, *, alpha, beta):
    """Fresh read-only alpha*M+beta*C; validate both vectors even at zero weight."""
    alpha = real_scalar(alpha, "alpha")
    beta = real_scalar(beta, "beta")
    m = _real_vector(macro, "macro")
    c = _real_vector(chiral, "chiral")
    return _freeze([total((product(alpha, x, "macro blend"),
                           product(beta, y, "chiral blend")), "total blend")
                    for x, y in zip(m, c)])


@dataclass(frozen=True, slots=True, eq=False)
class ZReadout:
    """Detached arrays resist ordinary mutation, not a security boundary."""
    z: float
    Z_macro: np.ndarray
    Z_chiral: np.ndarray
    Z_total: np.ndarray
    variant: str
    initialization: str = "recomputed"

    def __post_init__(self):
        object.__setattr__(self, "z", checked_real(real_scalar(self.z, "z"), "z"))
        for name in ("Z_macro", "Z_chiral", "Z_total"):
            object.__setattr__(self, name, _real_vector(getattr(self, name), name))
        if self.variant not in ("staged", "ema"):
            raise ValueError("variant must be staged or ema")
        if self.initialization not in ("recomputed", "historical_constructor_zero"):
            raise ValueError("unknown initialization marker")

    @property
    def Z_vec(self):
        """Compatibility alias of Z_total, with no separate writable storage."""
        return self.Z_total


def _observe(omega, clock, config, z, variant):
    macro = macro_vector(z, clock)
    # Deliberately evaluate C even when beta=0: the full decomposition promises C.
    chiral = readouts.z_chiral(omega)
    blended = blend_vectors(macro, chiral, alpha=config.alpha, beta=config.beta)
    return ZReadout(z, macro, chiral, blended, variant)


def observe_staged(omega, clock, config):
    """Pure K observation; advances neither clock nor Omega."""
    return _observe(omega, clock, config, staged_scalar(omega, clock, config), "staged")


@dataclass(frozen=True, slots=True)
class EMAConfig:
    """H harmonic/blend configuration. There is deliberately no gamma field."""
    lambda_vp: float = 0.618
    theta_lock: float = 0.244
    alpha: float = 1.0
    beta: float = 0.5

    def __post_init__(self):
        _config_reals(self, ("lambda_vp", "theta_lock", "alpha", "beta"))


@dataclass(frozen=True, slots=True)
class EMAState:
    """Adopted historical bounded profile: finite |m|<=1, normally m=0."""
    m: float = 0.0

    def __post_init__(self):
        m = real_scalar(self.m, "m")
        if abs(m) > 1:
            raise ValueError("the bounded historical profile requires |m|<=1")
        object.__setattr__(self, "m", m)


def cubic_j(omega):
    """J=Im(O1*conj(O2)*O3), with two left-associated checked complex products."""
    v = complex_vector(omega, 3, "omega")
    pair = complex_product(complex(v[0]), complex(v[1]).conjugate(), "cubic pair")
    return complex_product(pair, complex(v[2]), "cubic triple").imag


def normalized_cubic(omega):
    """J/(1+abs(J)); rounded results may equal +/-1."""
    j = cubic_j(omega)
    denominator = total((1.0, abs(j)), "cubic normalization denominator")
    return checked_real(j / denominator, "normalized cubic", nonzero=(j != 0))


def advance_ema(omega, memory):
    """Exactly one pure H update using the newly committed Omega.

    The source innovation is literal 0.01, not 1-float(0.99).
    No clock or recurrence update is performed.
    """
    _require(memory, EMAState, "memory")
    innovation = normalized_cubic(omega)
    tau_meta = 0.01
    m = total((product(1.0 - tau_meta, memory.m, "EMA retention"),
               product(tau_meta, innovation, "EMA innovation")), "EMA sum")
    return EMAState(m)


def ema_scalar(omega, clock, config, memory):
    """H scalar from CURRENT memory. No cubic evaluation or memory update."""
    _require(config, EMAConfig, "config")
    _require(clock, Clock, "clock")
    _require(memory, EMAState, "memory")
    return total((_harmonic(omega, clock, config), memory.m), "EMA scalar")


def observe_ema(omega, clock, config, memory):
    """Pure H observation from current memory, without an implicit EMA update."""
    return _observe(omega, clock, config,
                    ema_scalar(omega, clock, config, memory), "ema")


@dataclass(frozen=True, slots=True, eq=False)
class ConstructorZeroRecord:
    """Historical stored row zero, explicitly distinct from recomputation.

    Validates raw Omega, clock and named configuration. Both source constructors
    store zero memory and zero readouts; no cubic, norm or chirality is evaluated.
    The immutable config/clock fields retain the replay inputs, not a new runner.
    """
    omega: np.ndarray
    clock: Clock
    config: StagedConfig | EMAConfig
    memory: EMAState = field(init=False)
    readout: ZReadout = field(init=False)

    def __post_init__(self):
        _require(self.clock, Clock, "clock")
        if not isinstance(self.config, (StagedConfig, EMAConfig)):
            raise TypeError("config must explicitly select StagedConfig or EMAConfig")
        omega = _freeze(complex_vector(self.omega, 3, "omega"))
        variant = "staged" if isinstance(self.config, StagedConfig) else "ema"
        zero = np.zeros(3)
        object.__setattr__(self, "omega", omega)
        object.__setattr__(self, "memory", EMAState())
        object.__setattr__(self, "readout", ZReadout(
            0.0, zero, zero, zero, variant, "historical_constructor_zero"))


def historical_constructor_zero(omega, clock, config):
    """Return the marked historical zero row; this is not a formula observation."""
    return ConstructorZeroRecord(omega, clock, config)
