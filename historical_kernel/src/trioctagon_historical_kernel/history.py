"""N pre-update samples and a separate terminal; fresh constructor caches only."""
from dataclasses import dataclass
from .constants import KProfile, Readout
from .types import Triad, Clock, Memory, Observation, ZERO_OBSERVATION
from . import dynamics, clock, ema_z, staged_z


@dataclass(frozen=True, slots=True)
class Sample:
    update_index: int
    omega: Triad
    clock: Clock
    observation: Observation | None
    memory: Memory | None


@dataclass(frozen=True, slots=True)
class History:
    rows: tuple[Sample, ...]
    terminal: Sample


def _run(omega, profile, updates, readout, control=None):
    if type(omega) is not Triad or type(profile) is not KProfile or type(readout) is not Readout:
        raise TypeError("Historical state/profile/readout types required")
    if type(updates) is not int or updates < 0:
        raise ValueError("updates must be a nonnegative integer, without bool")
    memory = Memory() if readout is Readout.EMA else None
    observation = None if readout is Readout.NONE else ZERO_OBSERVATION
    current = Sample(0, omega, Clock(), observation, memory)
    rows = []
    for index in range(updates):
        if control is not None:
            control(index)
        rows.append(current)
        updated = dynamics.step(current.omega, profile)
        advanced_clock = clock.advance(current.clock)
        if readout is Readout.EMA:
            memory = ema_z.advance_ema(updated, memory)
            observation = ema_z.observe_ema(updated, advanced_clock, memory)
        elif readout is Readout.STAGED:
            observation = staged_z.observe_staged(updated, advanced_clock)
        current = Sample(index + 1, updated, advanced_clock, observation, memory)
        if control is not None:
            control(index + 1)
    return History(tuple(rows), current)


def run(omega, profile, updates, readout):
    return _run(omega, profile, updates, readout)
