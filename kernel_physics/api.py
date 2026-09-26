"""Supported v1 facade under K0. Option-B modules and FaceState are not exposed."""
from ._contract_types import (Parameters, State, Seed, Provenance, Clock, StagedConfig,
                              EMAConfig, EMAState, ObserverRequest, ZReadout,
                              _require, _triad, _values, _integer)
from ._response_numeric import ResponsePrecisionError, real_scalar as _real
from ._presets import historical_seed, historical_observer
from ._records import RunRecord
from ._geometry_records import GeometryRecord, get_geometry
from ._runner import run, resume, _step
from . import readouts as _readouts, z_manifold as _z, z_diagnostics as _d

__all__ = (
    "Parameters", "State", "Seed", "Provenance", "historical_seed", "step", "z_chiral",
    "Clock", "StagedConfig", "EMAConfig", "EMAState", "advance_clock", "advance_ema",
    "observe_staged", "observe_ema", "historical_observer", "ObserverRequest", "ZReadout",
    "ResponsePrecisionError", "run", "resume", "RunRecord", "GeometryRecord", "get_geometry",
    "quadratic_form", "readout_accounting", "chiral_area_accounting", "intensity_budget",
    "potential", "historical_alignment", "direct_history_coordinates", "cylinder_point",
    "cylinder_history_coordinates", "history_torus_coordinates",
)


def step(state: State, parameters: Parameters, *, topology: str) -> State:
    return _step(state, parameters, topology=topology)


def z_chiral(omega):
    return _readouts.z_chiral(_triad(omega, "omega"))


def advance_clock(clock: Clock, dt) -> Clock:
    _require(clock, Clock, "clock")
    return Clock(**_values(_z.advance_clock(clock._native(), _real(dt, "dt"))))


def advance_ema(omega, memory: EMAState) -> EMAState:
    _require(memory, EMAState, "memory")
    return EMAState(m=_z.advance_ema(_triad(omega, "omega"), memory._native()).m)


def observe_staged(omega, clock: Clock, config: StagedConfig) -> ZReadout:
    _require(clock, Clock, "clock")
    _require(config, StagedConfig, "config")
    return _z.observe_staged(_triad(omega, "omega"), clock._native(), config._native())


def observe_ema(omega, clock: Clock, config: EMAConfig, memory: EMAState) -> ZReadout:
    _require(clock, Clock, "clock")
    _require(config, EMAConfig, "config")
    _require(memory, EMAState, "memory")
    return _z.observe_ema(_triad(omega, "omega"), clock._native(), config._native(), memory._native())


def quadratic_form(vector):
    return _d.quadratic_form(vector)


def readout_accounting(readout, *, alpha, beta):
    return _d.readout_accounting(readout, alpha=_real(alpha, "alpha"), beta=_real(beta, "beta"))


def chiral_area_accounting(omega):
    return _d.chiral_area_accounting(_triad(omega, "omega"))


def intensity_budget(omega, parameters):
    _require(parameters, Parameters, "parameters")
    return _d.intensity_budget(_triad(omega, "omega"), parameters._native())


def potential(omega, parameters):
    _require(parameters, Parameters, "parameters")
    return _d.potential(_triad(omega, "omega"), parameters._native())


def historical_alignment(macro, chiral, total_vector):
    return _d.historical_alignment(macro, chiral, total_vector)


def direct_history_coordinates(history, *, key):
    return _d.direct_history_coordinates(history, key=key)


def cylinder_point(kappa, q, z, *, N):
    return _d.cylinder_point(kappa, _integer(q, "q"), z, N=_integer(N, "N", minimum=1))


def cylinder_history_coordinates(history, *, N):
    return _d.cylinder_history_coordinates(history, N=_integer(N, "N", minimum=1))


def history_torus_coordinates(history, *, R, r_max, N):
    return _d.history_torus_coordinates(history, R=_real(R, "R"), r_max=_real(r_max, "r_max"),
                                         N=_integer(N, "N", minimum=1))
