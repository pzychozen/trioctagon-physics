"""Explicit, detached public values. Mathematical evaluation stays in its owner."""
from collections.abc import Mapping
from dataclasses import dataclass, fields
import numbers
from types import MappingProxyType

import numpy as np

from . import dynamics as _dynamics, z_manifold as _z
from ._response_numeric import complex_vector, real_scalar


def _integer(value, name, *, minimum=None):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Integral):
        raise TypeError(f"{name} must be an integer, excluding bool")
    value = int(value)
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def _text(value, name, *, empty=False):
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")
    if not empty and not value:
        raise ValueError(f"{name} must be nonempty")
    return value


def _require(value, cls, name):
    if not isinstance(value, cls):
        raise TypeError(f"{name} must be {cls.__name__}")
    return value


def _values(value):
    return {f.name: getattr(value, f.name) for f in fields(value)}


def _triad(values, name):
    return tuple(complex(z) for z in complex_vector(values, 3, name))


@dataclass(frozen=True, slots=True, kw_only=True)
class Provenance:
    kind: str
    source_id: str
    source_revision: str | None
    locator: str
    literal_values: Mapping
    notes: str

    def __post_init__(self):
        _text(self.kind, "kind")
        if self.kind not in ("user_supplied", "historical_preset", "accepted_definition", "checkpoint"):
            raise ValueError("unknown provenance kind")
        for name in ("source_id", "locator"):
            _text(getattr(self, name), name)
        _text(self.notes, "notes", empty=True)
        if self.source_revision is not None:
            _text(self.source_revision, "source_revision")
        if not isinstance(self.literal_values, Mapping):
            raise TypeError("literal_values must be a map of source spellings")
        copy = {_text(k, "literal name"): _text(v, "literal spelling", empty=True)
                for k, v in self.literal_values.items()}
        object.__setattr__(self, "literal_values", MappingProxyType(copy))


@dataclass(frozen=True, slots=True, kw_only=True)
class Parameters:
    eps: float
    g: float
    phase_strength: float
    k: tuple

    def __post_init__(self):
        for name in ("eps", "g", "phase_strength"):
            object.__setattr__(self, name, real_scalar(getattr(self, name), name))
        raw = np.asarray(self.k, dtype=object)
        if raw.shape != (3,):
            raise ValueError("k must have shape (3,)")
        object.__setattr__(self, "k", tuple(real_scalar(v, "k component") for v in raw))

    def _native(self):
        return _dynamics.DynamicsConfig(**_values(self))


@dataclass(frozen=True, slots=True, kw_only=True)
class State:
    omega: tuple
    update_index: int

    def __post_init__(self):
        raw = np.asarray(self.omega, dtype=object)
        if raw.ndim != 1 or len(raw) < 3 or len(raw) % 3:
            raise ValueError("omega must have shape (3q,), q >= 1")
        object.__setattr__(self, "omega", tuple(complex(z) for z in complex_vector(raw, len(raw), "omega")))
        object.__setattr__(self, "update_index", _integer(self.update_index, "update_index", minimum=0))


@dataclass(frozen=True, slots=True, kw_only=True)
class Seed:
    name: str
    omega: tuple
    provenance: Provenance

    def __post_init__(self):
        _text(self.name, "name")
        _require(self.provenance, Provenance, "provenance")
        object.__setattr__(self, "omega", _triad(self.omega, "omega"))


@dataclass(frozen=True, slots=True, kw_only=True)
class Clock:
    q: int
    N: int
    t: float
    q_step: int

    def __post_init__(self):
        object.__setattr__(self, "q", _integer(self.q, "q"))
        object.__setattr__(self, "N", _integer(self.N, "N", minimum=1))
        object.__setattr__(self, "q_step", _integer(self.q_step, "q_step"))
        object.__setattr__(self, "t", real_scalar(self.t, "t"))

    def _native(self):
        return _z.Clock(**_values(self))


@dataclass(frozen=True, slots=True, kw_only=True)
class StagedConfig:
    lambda_vp: float
    gamma: float
    theta_lock: float
    alpha: float
    beta: float

    def __post_init__(self):
        for name, value in _values(self).items():
            object.__setattr__(self, name, real_scalar(value, name))

    def _native(self):
        return _z.StagedConfig(**_values(self))


@dataclass(frozen=True, slots=True, kw_only=True)
class EMAConfig:
    lambda_vp: float
    theta_lock: float
    alpha: float
    beta: float

    def __post_init__(self):
        for name, value in _values(self).items():
            object.__setattr__(self, name, real_scalar(value, name))

    def _native(self):
        return _z.EMAConfig(**_values(self))


@dataclass(frozen=True, slots=True, kw_only=True)
class EMAState:
    m: float

    def __post_init__(self):
        m = real_scalar(self.m, "m")
        # The accepted type owns the bounded-memory domain.
        native = _z.EMAState(m=m)
        object.__setattr__(self, "m", native.m)

    def _native(self):
        return _z.EMAState(m=self.m)


@dataclass(frozen=True, slots=True, kw_only=True)
class ObserverRequest:
    observer_id: str
    config: StagedConfig | EMAConfig
    clock: Clock
    memory: EMAState | None
    dt: float
    initialization: str
    provenance: Provenance

    def __post_init__(self):
        _text(self.observer_id, "observer_id")
        if not isinstance(self.config, (StagedConfig, EMAConfig)):
            raise TypeError("config must be an explicit public observer configuration")
        _require(self.clock, Clock, "clock")
        _require(self.provenance, Provenance, "provenance")
        if isinstance(self.config, EMAConfig):
            _require(self.memory, EMAState, "memory")
        elif self.memory is not None:
            raise ValueError("staged memory must be None")
        object.__setattr__(self, "dt", real_scalar(self.dt, "dt"))
        _text(self.initialization, "initialization")
        if self.initialization not in ("recomputed", "historical_constructor_zero"):
            raise ValueError("unknown initialization marker")
        if self.initialization == "historical_constructor_zero" and self.memory is not None and self.memory.m != 0:
            raise ValueError("constructor-zero requires zero initial memory")

    @property
    def variant(self):
        return "staged" if isinstance(self.config, StagedConfig) else "ema"


def _provenance_data(value):
    _require(value, Provenance, "provenance")
    result = _values(value)
    result["literal_values"] = dict(value.literal_values)
    return result


def _topology(state, topology):
    _require(state, State, "state")
    _text(topology, "topology")
    if topology not in ("triad", "ring"):
        raise ValueError("topology must be triad or ring")
    if topology == "triad" and len(state.omega) != 3:
        raise ValueError("triad topology requires exactly three components")


ZReadout = _z.ZReadout
