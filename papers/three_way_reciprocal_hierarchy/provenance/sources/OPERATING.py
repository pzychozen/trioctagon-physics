"""Opt-in radius-three checks and adapters; the existing step3 law is reused.

The invariant-domain proof is exact arithmetic, not a machine safety theorem.
No incident budget is imposed on an individually valid prepared initial triad.
"""
import math

import numpy as np

from ._response_numeric import (ResponsePrecisionError, checked_array, complex_vector,
                               real_scalar)
from .dynamics import DynamicsConfig, step3
from .srg import handoff_area_response

PROFILE_ID = "triad_eps005_g02_k0to8_radius3_v1"
UNIFORM_INCIDENT_BUDGET = 3*math.sqrt(3)


def _profile(profile):
    if not isinstance(profile, str) or profile != PROFILE_ID:
        raise ValueError(f"profile must explicitly select {PROFILE_ID}")


def _config(config):
    if not isinstance(config, DynamicsConfig):
        raise TypeError("config must be an existing DynamicsConfig")
    if real_scalar(config.eps, "eps") != 1/20 or real_scalar(config.g, "g") != 1/5:
        raise ValueError("the bounded profile requires eps=1/20 and g=1/5")
    real_scalar(config.phase_strength, "phase_strength")
    if len(config.k) != 3 or any(not 0 <= real_scalar(k, "k") <= 8 for k in config.k):
        raise ValueError("the bounded profile requires actual k components in [0,8]")


def bounded_config(*, k, phase_strength):
    """Strict parameter entry before DynamicsConfig's general-purpose coercion."""
    raw = np.asarray(k, dtype=object)
    if raw.shape != (3,):
        raise ValueError("k must be a real triple")
    values = tuple(real_scalar(v, "k") for v in raw)
    strength = real_scalar(phase_strength, "phase_strength")
    config = DynamicsConfig(1/20, 1/5, strength, values)
    _config(config)
    return config


def validate_bounded_triad(state, config, *, profile):
    """Validate the actual state and parameters; return a fresh raw state copy."""
    _profile(profile)
    _config(config)
    vector = complex_vector(state, 3, "state")
    if any(math.hypot(z.real, z.imag) > 3 for z in vector):
        raise ValueError("the bounded profile requires max component modulus <= 3")
    return vector


def validate_uniform_incident_budget(xi):
    """Optional sufficient ||xi||<=3sqrt(3) check, never an individual-state gate."""
    vector = complex_vector(xi, 2, "xi")
    norm = math.hypot(*(v for z in vector for v in (z.real, z.imag)))
    if norm > UNIFORM_INCIDENT_BUDGET:
        raise ValueError("incident norm exceeds the uniform sufficient budget")
    return vector


def initialize_bounded_area(theta, xi, *, config, profile, transfer_count, branch, response):
    """Prepare then validate actual Omega; large valid incident inputs are allowed."""
    _profile(profile)
    _config(config)
    handoff = handoff_area_response(theta, xi, transfer_count=transfer_count,
                                    branch=branch, response=response)
    validate_bounded_triad(handoff.omega, config, profile=profile)
    return handoff


def step_bounded_triad(state, config, *, profile):
    """One EXISTING step3 call, with explicit numerical-failure checks around it.

    No clipping, normalization, extra state, forcing, noise or second recurrence.
    Errors can be conservative; no certification for all finite machine inputs.
    """
    vector = validate_bounded_triad(state, config, profile=profile)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="raise"):
            result = step3(vector, config)
    except (FloatingPointError, OverflowError) as exc:
        raise ResponsePrecisionError(f"existing step3 numerical failure: {exc}") from exc
    result = checked_array(result, "bounded step output")
    if any(math.hypot(z.real, z.imag) > 3 for z in result):
        raise ResponsePrecisionError("computed step escaped the profile; no clipping applied")
    return result
