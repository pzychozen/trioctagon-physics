"""Passive Paper-E diagnostics and explicitly named historical display adapters.

Only supplied data are inspected. No recurrence, clock or EMA advancement occurs.
Binary64 checked products and compensated sums reject nonfinite and nonzero
subnormal intermediates; different polynomial degrees have different ranges.
A rounded zero residual is not an exact certificate. No clipping is performed.
"""
from dataclasses import dataclass
import math

import numpy as np

from . import readouts
from ._response_numeric import (
    checked_real, complex_vector, product, real_scalar, scale_complex, total,
)
from .dynamics import DynamicsConfig, L3
from .z_manifold import Clock, ZReadout, blend_vectors, clock_angle


def _freeze(value):
    result = np.array(value, copy=True)
    result.setflags(write=False)
    return result


def _seal(record, names):
    for name in names:
        object.__setattr__(record, name, _freeze(getattr(record, name)))


def _real(value, name):
    return checked_real(real_scalar(value, name), name)


def _array(value, name, *, shape=None, ndim=None):
    raw = np.asarray(value, dtype=object)
    if (shape is not None and raw.shape != shape
            or ndim is not None and raw.ndim != ndim):
        raise ValueError(f"{name} has an invalid shape")
    result = np.empty(raw.shape, dtype=float)
    for index in np.ndindex(raw.shape):
        result[index] = _real(raw[index], name)
    return result


def _square(x):
    return product(x, x, "square")


def _dot(x, y, signs=(1, 1, 1)):
    return total((sign * product(a, b, "dot term")
                  for a, b, sign in zip(x, y, signs)), "dot sum")


def _norm(v):
    return checked_real(math.hypot(*(float(x) for x in v)), "norm",
                        nonzero=any(x != 0 for x in v))


def _divide(a, b, name):
    return checked_real(a / b, name, nonzero=(a != 0))


def _difference(a, b):
    return total((a, -b), "difference")


def _complex_sum(values):
    values = tuple(values)
    return complex(total((v.real for v in values), "real sum"),
                   total((v.imag for v in values), "imaginary sum"))


def quadratic_form(vector):
    """Signed Q(v)=v1^2+v2^2-v3^2 for a finite real (3,) vector."""
    v = _array(vector, "vector", shape=(3,))
    return _dot(v, v, (1, 1, -1))


@dataclass(frozen=True, slots=True, eq=False)
class ReadoutAccounting:
    alpha: float
    beta: float
    variant: str
    initialization: str
    supplied_z: float
    macro_norm_squared: float
    chiral_norm_squared: float
    total_norm_squared: float
    weighted_macro: float
    weighted_chiral: float
    cross_term: float
    predicted_norm_squared: float
    norm_residual: float
    blend_residual: np.ndarray
    q_macro: float
    q_chiral: float
    q_total: float
    q_weighted_macro: float
    q_weighted_chiral: float
    q_cross_term: float
    q_prediction: float
    q_residual: float
    macro_relation_residual: float

    def __post_init__(self):
        _seal(self, ("blend_residual",))


def readout_accounting(readout, *, alpha, beta):
    """Inspect stored M,C,T without repairing them; retain all signed terms.

    The macro relation uses the supplied z, including constructor-zero records.
    Total zero is valid and does not establish zero state or physical energy.
    """
    if not isinstance(readout, ZReadout):
        raise TypeError("readout must be ZReadout")
    a, b = _real(alpha, "alpha"), _real(beta, "beta")
    m = _array(readout.Z_macro, "M", shape=(3,))
    c = _array(readout.Z_chiral, "C", shape=(3,))
    t = _array(readout.Z_total, "T", shape=(3,))
    z = _real(readout.z, "supplied z")
    mm, cc, tt = (_dot(v, v) for v in (m, c, t))
    aa, bb = _square(a), _square(b)
    twice_ab = product(2, product(a, b, "alpha beta"), "twice alpha beta")
    wm, wc = product(aa, mm, "weighted M"), product(bb, cc, "weighted C")
    cross = product(twice_ab, _dot(m, c), "norm cross")
    prediction = total((wm, wc, cross), "norm prediction")
    blended = blend_vectors(m, c, alpha=a, beta=b)
    blend_residual = [_difference(x, y) for x, y in zip(t, blended)]
    qm, qc, qt = (quadratic_form(v) for v in (m, c, t))
    qwm, qwc = product(aa, qm, "weighted Q(M)"), product(bb, qc, "weighted Q(C)")
    qcross = product(twice_ab, _dot(m, c, (1, 1, -1)), "Q cross")
    qp = total((qwm, qwc, qcross), "full Q prediction")
    return ReadoutAccounting(
        a, b, readout.variant, readout.initialization, z, mm, cc, tt, wm, wc,
        cross, prediction, _difference(tt, prediction), blend_residual,
        qm, qc, qt, qwm, qwc, qcross, qp, _difference(qt, qp),
        _difference(mm, product(2, _square(z), "2 z squared")),
    )


@dataclass(frozen=True, slots=True, eq=False)
class ChiralAreaAccounting:
    chiral: np.ndarray
    A: float
    B: float
    h: float
    intensity: float
    chiral_norm: float
    chiral_norm_squared: float
    gram_product: float
    h_squared: float
    gram_rhs: float
    gram_residual: float
    amplitude_bound: float
    slack_sum_of_squares: float
    observed_slack: float
    slack_residual: float

    def __post_init__(self):
        _seal(self, ("chiral",))


def chiral_area_accounting(omega):
    """Delegate raw C once, then report Gram identity and sharp-bound slack."""
    v = complex_vector(omega, 3, "omega")
    c = readouts.z_chiral(v)
    a, b, h = _dot(v.real, v.real), _dot(v.imag, v.imag), _dot(v.real, v.imag)
    intensity = total((a, b), "intensity")
    c2 = _dot(c, c)
    ab, hh = product(a, b, "A B"), _square(h)
    gram = _difference(ab, hh)
    bound = product(0.5, intensity, "amplitude bound")
    half_difference = product(0.5, _difference(a, b), "half A-B")
    slack = total((_square(half_difference), hh), "sum of squares slack")
    observed = _difference(_square(bound), c2)
    return ChiralAreaAccounting(
        c, a, b, h, intensity, _norm(c), c2, ab, hh, gram,
        _difference(c2, gram), bound, slack, observed, _difference(observed, slack),
    )


@dataclass(frozen=True, slots=True)
class HistoricalAlignment:
    d_TM: float
    d_CM: float
    d_TC: float
    macro_resolved: bool
    chiral_resolved: bool
    total_resolved: bool
    TM_resolved: bool
    CM_resolved: bool
    TC_resolved: bool
    threshold: float = 1e-12


def historical_alignment(macro, chiral, total_vector):
    """Historical threshold convention; unresolved zero is not orthogonality.

    Stable hypot replaces the old naive norm. At exactly 1e-12, resolve.
    Numerical cosine bounds are not clipped or certified.
    """
    units, flags = [], []
    for v, name in ((macro, "macro"), (chiral, "chiral"), (total_vector, "total")):
        v = _array(v, name, shape=(3,))
        norm = _norm(v)
        resolved = norm >= 1e-12
        flags.append(resolved)
        units.append([_divide(x, norm, "unit component") for x in v]
                     if resolved else [0., 0., 0.])
    m, c, t = units
    mr, cr, tr = flags
    return HistoricalAlignment(_dot(t, m), _dot(c, m), _dot(t, c),
                               mr, cr, tr, tr and mr, cr and mr, tr and cr)


def _state_parameters(omega, config):
    if not isinstance(config, DynamicsConfig):
        raise TypeError("config must be DynamicsConfig")
    # Validate stored values, not the pre-construction inputs already coerced.
    eps, g = _real(config.eps, "eps"), _real(config.g, "g")
    _real(config.phase_strength, "phase_strength")
    k = _array(config.k, "k", shape=(3,))
    v = complex_vector(omega, 3, "omega")
    s = [total((_square(z.real), _square(z.imag)), "component intensity") for z in v]
    pair_terms = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        pair_terms.append(total((_square(_difference(v[i].real, v[j].real)),
                                 _square(_difference(v[i].imag, v[j].imag))),
                                "pair distance squared"))
    return v, eps, g, k, s, total(pair_terms, "P")


@dataclass(frozen=True, slots=True, eq=False)
class IntensityBudget:
    component_intensities: np.ndarray
    intensity_before: float
    increment: np.ndarray
    diagnostic_pre_sync_prediction: np.ndarray
    intensity_pre_sync: float
    pair_distance_sum: float
    onsite: float
    coupling: float
    remainder: float
    predicted_delta: float
    observed_delta: float
    residual: float

    def __post_init__(self):
        _seal(self, ("component_intensities", "increment",
                     "diagnostic_pre_sync_prediction"))


def intensity_budget(omega, config):
    """Unforced finite-map accounting. Prediction is not an evolved state.

    D is built from its defining terms using the imported existing L3.
    No dt, forcing, phase operation or advancement occurs here.
    """
    v, eps, g, k, s, pairs = _state_parameters(omega, config)
    increments = []
    for i in range(3):
        graph = _complex_sum(scale_complex(coef, z, "L3 term")
                             for coef, z in zip(L3[i], v))
        onsite_increment = scale_complex(
            product(eps, _difference(k[i], s[i]), "onsite coefficient"),
            v[i], "onsite increment")
        increments.append(_complex_sum((onsite_increment,
                                        scale_complex(g, graph, "graph increment"))))
    prediction = [_complex_sum((z, d)) for z, d in zip(v, increments)]
    before = total(s, "intensity before")
    after = total((_square(z.real) for z in prediction), "pre real intensity")
    after = total((after, *(_square(z.imag) for z in prediction)), "intensity pre")
    onsite_terms = [_difference(product(ki, si, "k s"), _square(si))
                    for ki, si in zip(k, s)]
    onsite = product(2, product(eps, total(onsite_terms, "onsite sum"),
                                "eps onsite"), "onsite")
    coupling = product(-2, product(g, pairs, "g P"), "coupling")
    remainder = total((_square(c) for d in increments for c in (d.real, d.imag)),
                      "increment norm squared")
    predicted_delta = total((onsite, coupling, remainder), "predicted delta")
    observed_delta = _difference(after, before)
    return IntensityBudget(s, before, increments, prediction, after, pairs,
                           onsite, coupling, remainder, predicted_delta,
                           observed_delta, _difference(observed_delta, predicted_delta))


def potential(omega, config):
    """Real scalar potential, distinct from intensity, z, T and pre-sync state.

    Its six-real-coordinate negative gradient is D. A unit-size discrete update
    or subsequent phase synchronization need not decrease this potential.
    """
    _, eps, g, k, s, pairs = _state_parameters(omega, config)
    terms = [_difference(_square(product(.5, si, "half s")),
                         product(product(.5, ki, "half k"), si, "half k s"))
             for si, ki in zip(s, k)]
    onsite = product(eps, total(terms, "potential onsite sum"), "onsite potential")
    graph = product(product(.5, g, "half g"), pairs, "graph potential")
    return total((onsite, graph), "potential")


@dataclass(frozen=True, slots=True, eq=False)
class Coordinates:
    """Detached read-only real x/y/z columns; no geometry attachment."""
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray

    def __post_init__(self):
        _seal(self, ("x", "y", "z"))


def direct_history_coordinates(history, key="Z_total"):
    """Copy stored (n,3) vectors, defaulting to Z_vec only if Z_total is absent."""
    if not isinstance(key, str):
        raise TypeError("key must be a string")
    if key not in history:
        if key == "Z_total" and "Z_vec" in history:
            key = "Z_vec"
        else:
            raise KeyError(key)
    values = _array(history[key], key, ndim=2)
    if values.shape[1] != 3:
        raise ValueError("direct history must have shape (n,3)")
    return Coordinates(values[:, 0], values[:, 1], values[:, 2])


def cylinder_point(kappa, q, z, *, N=12):
    """Scalar cylinder (kappa*cos(theta),kappa*sin(theta),z), theta from K2.

    N=12 is historical compatibility; custom N is explicit parameterization.
    """
    kappa, z = _real(kappa, "kappa"), _real(z, "z")
    if kappa < 0:
        raise ValueError("kappa must be nonnegative")
    theta = clock_angle(Clock(q=q, N=N))
    return _freeze([product(kappa, math.cos(theta), "cylinder x"),
                    product(kappa, math.sin(theta), "cylinder y"), z])


def _history(history, N, *, nonempty=False):
    # Validate N even for an empty history.
    Clock(N=N)
    k = _array(history["kappa"], "kappa", ndim=1)
    z = _array(history["z"], "z", ndim=1)
    raw_q = np.asarray(history["phi_index"], dtype=object)
    if raw_q.ndim != 1 or len(k) != len(z) or len(k) != len(raw_q):
        raise ValueError("history requires equally sized one-dimensional arrays")
    if np.any(k < 0):
        raise ValueError("kappa must be nonnegative")
    if nonempty and not len(k):
        raise ValueError("torus history must be nonempty")
    angles = [clock_angle(Clock(q=q, N=N)) for q in raw_q]
    return k, z, angles


def cylinder_history_coordinates(history, *, N=12):
    """Empty histories allowed; no scalar height is lost at kappa=0."""
    k, z, angles = _history(history, N)
    return Coordinates([product(v, math.cos(a), "cylinder x") for v, a in zip(k, angles)],
                       [product(v, math.sin(a), "cylinder y") for v, a in zip(k, angles)],
                       z)


@dataclass(frozen=True, slots=True, eq=False)
class HistoryTorus:
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    r: np.ndarray
    chi: np.ndarray
    z_max: float
    H_z: float
    regularizer: float
    R: float
    r_max: float
    N: int
    normalization: str = "entire_supplied_history"

    def __post_init__(self):
        _seal(self, ("x", "y", "z", "r", "chi"))


def history_torus_coordinates(history, *, R=2., r_max=1., N=12):
    """Whole-history scalar torus; adopted display domain R>r_max>0.

    Literal 1e-9 regularizer and actual rounded H_z are returned. Saturation can
    round r to r_max and H_z to z_max. Strict inverse hypotheses are not
    guaranteed by a successful floating result. There is no runtime inverse.
    """
    R, r_max = _real(R, "R"), _real(r_max, "r_max")
    if not R > r_max > 0:
        raise ValueError("adapter requires R > r_max > 0")
    k, z, angles = _history(history, N, nonempty=True)
    z_max = max(abs(float(v)) for v in z)
    regularizer = 1e-9
    height = total((z_max, regularizer), "history normalization")
    radii, chis, xs, ys, zs = [], [], [], [], []
    for amplitude, scalar, theta in zip(k, z, angles):
        rho = _divide(amplitude, total((1., amplitude), "rho denominator"), "rho")
        radius = product(r_max, rho, "minor radius")
        chi = product(math.pi / 2, _divide(scalar, height, "height ratio"), "chi")
        major = total((R, product(radius, math.cos(chi), "minor horizontal")), "major")
        xs.append(product(major, math.cos(theta), "torus x"))
        ys.append(product(major, math.sin(theta), "torus y"))
        zs.append(product(radius, math.sin(chi), "torus height"))
        radii.append(radius)
        chis.append(chi)
    return HistoryTorus(xs, ys, zs, radii, chis, z_max, height, regularizer,
                        R, r_max, int(N))
