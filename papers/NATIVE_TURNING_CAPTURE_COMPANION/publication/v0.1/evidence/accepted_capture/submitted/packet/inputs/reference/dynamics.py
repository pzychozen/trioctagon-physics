"""Paper A §§1,6 deterministic nonlinear map in complex128 arithmetic.

There is no clock, dt, noise, normalization step, geometry input or extra state.
The mathematical formula is exact; numerical evaluation has rounding/overflow.
"""

from dataclasses import dataclass
from math import isfinite

import numpy as np

L3 = ((-2, 1, 1), (1, -2, 1), (1, 1, -2))


def _finite_real(value, name: str) -> float:
    if np.iscomplexobj(value):
        raise ValueError(f"{name} must be a finite real number")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite real number") from exc
    if not isfinite(result):
        raise ValueError(f"{name} must be a finite real number")
    return result


@dataclass(frozen=True, slots=True)
class DynamicsConfig:
    """Fixed real parameters; k is an amplitude-coefficient triple.

    phase_strength is Paper A's lambda. No default physical parameters.
    """

    eps: float
    g: float
    phase_strength: float
    k: tuple[float, float, float]

    def __post_init__(self):
        for name in ("eps", "g", "phase_strength"):
            object.__setattr__(self, name, _finite_real(getattr(self, name), name))
        values = tuple(_finite_real(v, "k component") for v in self.k)
        if len(values) != 3:
            raise ValueError("k must have exactly three real coefficients")
        object.__setattr__(self, "k", values)


def _state(values) -> np.ndarray:
    state = np.array(values, dtype=np.complex128, copy=True)
    if state.ndim != 1 or len(state) < 3:
        raise ValueError("state must be a one-dimensional complex vector of size >=3")
    if not np.all(np.isfinite(state)):
        raise ValueError("state must contain finite components")
    return state


def arg0(values) -> np.ndarray:
    """Componentwise Arg for nonzero entries; +0 for every exact complex zero.

    Signed IEEE zeros do not select a phase at zero.
    """
    values = np.asarray(values, dtype=np.complex128)
    return np.where(values == 0, 0.0, np.angle(values))


def phase_sync(values, phase_strength: float) -> np.ndarray:
    """Simultaneous harmonic-3 neighbor synchronization on a cycle of size >=3.

    For size three, the two cyclic neighbors are precisely the other two nodes.
    lambda=0 returns a copy directly, without phase extraction/reconstruction.
    """
    state = _state(values)
    strength = _finite_real(phase_strength, "phase_strength")
    if strength == 0:
        return state
    phases = arg0(state)
    increment = strength * (
        np.sin(3 * (np.roll(phases, 1) - phases))
        + np.sin(3 * (np.roll(phases, -1) - phases))
    )
    with np.errstate(over="raise", invalid="raise"):
        result = np.abs(state) * np.exp(1j * (phases + increment))
    result[state == 0] = 0j
    return result


def _advance(state: np.ndarray, config: DynamicsConfig) -> np.ndarray:
    coefficients = np.tile(config.k, len(state) // 3)
    with np.errstate(over="raise", invalid="raise"):
        if len(state) == 3:
            coupling = np.asarray(L3) @ state
        else:
            coupling = np.roll(state, 1) + np.roll(state, -1) - 2 * state
        updated = (state + config.eps * state * (coefficients - np.abs(state) ** 2)
                   + config.g * coupling)
    return phase_sync(updated, config.phase_strength)


def step3(omega, config: DynamicsConfig) -> np.ndarray:
    """F_3: pre-sync amplitude map followed by the simultaneous synchronizer."""
    state = _state(omega)
    if len(state) != 3:
        raise ValueError("step3 requires exactly three components")
    return _advance(state, config)


def step_ring(omega, config: DynamicsConfig) -> np.ndarray:
    """F_M for M=3q; k is repeated by residue class, including the wrap."""
    state = _state(omega)
    if len(state) % 3:
        raise ValueError("step_ring requires M divisible by three")
    return _advance(state, config)
