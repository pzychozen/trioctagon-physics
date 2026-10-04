"""Paper G sections 2-3: passive checked-binary64 axial observations.

No advancement, feedback, I/O or proof certification. Pre-sync values are
algebraic reconstructions, not recorded intermediates. See K0 axial extension.
"""
from dataclasses import dataclass, fields
import math

from . import z_diagnostics
from ._response_numeric import (checked_real, complex_vector, product, total,
                                scale_complex)
from .dynamics import L3, arg0

AXIAL_OBSERVATION_API_VERSION = "1.0.0"
AXIAL_OBSERVER_REVISION = "AXIAL_M1_V1"
_SOURCE = "PAPER_G_V0.1.1_SECTIONS_2_3"
_POLICY = "CHECKED_BINARY64_AXIAL_V1"
_T = ((-.5, 1., -.5), (-math.sqrt(3)/2, 0., math.sqrt(3)/2), (0., 0., 0.))


@dataclass(frozen=True, slots=True)
class _Accounting:
    chiral: tuple
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


@dataclass(frozen=True, slots=True)
class _SnapshotResiduals:
    area_cross: tuple
    SC: tuple
    reconstruction: tuple
    W_z: float
    gram: float
    bilinear: float
    decomposition: float


@dataclass(frozen=True, slots=True)
class AxialSnapshot:
    revision: str
    source_definition: str
    numeric_policy: str
    S: tuple
    A: tuple
    C: tuple
    Gamma: float
    C_parallel: tuple
    C_perp: tuple
    W: tuple
    intensity: float
    C_norm: float
    W_norm: float
    chiral_area_accounting: _Accounting
    residuals: _SnapshotResiduals


@dataclass(frozen=True, slots=True)
class _Area:
    A: tuple
    C: tuple
    W: tuple
    Gamma: float


@dataclass(frozen=True, slots=True)
class _Term:
    name: str
    A: tuple
    C: tuple
    W: tuple
    Gamma: float


@dataclass(frozen=True, slots=True)
class _PreSync:
    omega: tuple
    S: tuple
    A: tuple
    phases: tuple
    delta: tuple
    d: tuple


@dataclass(frozen=True, slots=True)
class _Parameters:
    eps: float
    g: float
    phase_strength: float
    k: tuple


@dataclass(frozen=True, slots=True)
class AxialSourceBudget:
    revision: str
    source_definition: str
    numeric_policy: str
    before_index: int
    after_index: int | None
    resolved_parameters: _Parameters
    before_snapshot: AxialSnapshot
    amplitude_terms: tuple
    pre_sync_prediction: _PreSync
    phase_terms: tuple
    predicted_after: _Area
    congruence_residual: _Area
    pair_rotation_residual: _Area
    actual_after_snapshot: AxialSnapshot | None
    comparison_residuals: _Area | None
    comparison_status: str
    qualification: str


def _sum(values):
    return total(values, "axial sum")


def _mul(x, y):
    return product(x, y, "axial product")


def _sub(x, y):
    return _sum((x, -y))


def _dot(x, y):
    return _sum(_mul(a, b) for a, b in zip(x, y))


def _matrix(function):
    return tuple(tuple(function(i, j) for j in range(3)) for i in range(3))


def _add(*matrices):
    return _matrix(lambda i, j: _sum(a[i][j] for a in matrices))


def _scale(value, matrix):
    return _matrix(lambda i, j: _mul(value, matrix[i][j]))


def _mm(a, b):
    return _matrix(lambda i, j: _sum(_mul(a[i][k], b[k][j]) for k in range(3)))


def _sa(omega):
    x, y = tuple(z.real for z in omega), tuple(z.imag for z in omega)
    S = _matrix(lambda i, j: _sum((_mul(x[i], x[j]), _mul(y[i], y[j]))))
    A = _matrix(lambda i, j: _sub(_mul(x[i], y[j]), _mul(y[i], x[j])))
    return S, A


def _attach(c):
    return tuple(_dot(row, c) for row in _T), _sum(c)


def _area(A):
    # Linear extraction from an area term; C snapshots use canonical readouts.
    C = (A[1][2], A[2][0], A[0][1])
    W, Gamma = _attach(C)
    return _Area(A, C, W, Gamma)


def _term(name, A):
    r = _area(A)
    return _Term(name, r.A, r.C, r.W, r.Gamma)


def _difference(actual, predicted):
    # Subtract each representation directly; do not hide roundoff by extracting
    # every comparison from the area-matrix residual alone.
    return _Area(_matrix(lambda i, j: _sub(actual.A[i][j], predicted.A[i][j])),
                 tuple(_sub(x, y) for x, y in zip(actual.C, predicted.C)),
                 tuple(_sub(x, y) for x, y in zip(actual.W, predicted.W)),
                 _sub(actual.Gamma, predicted.Gamma))


def axial_snapshot(omega):
    """Observe one triad; return detached immutable values, never a new state."""
    v = tuple(complex(z) for z in complex_vector(omega, 3, "omega"))
    accounting = z_diagnostics.chiral_area_accounting(v)
    C = tuple(float(x) for x in accounting.chiral)
    frozen = _Accounting(**{f.name: C if f.name == "chiral" else getattr(accounting, f.name)
                            for f in fields(accounting)})
    S, A = _sa(v)
    W, Gamma = _attach(C)
    third = checked_real(Gamma/3, "Gamma/3", nonzero=Gamma != 0)
    parallel = (third,)*3
    perpendicular = tuple(_sub(c, third) for c in C)
    reconstructed = tuple(_sum((_mul(2/3, _dot(tuple(row[i] for row in _T), W)), third)) for i in range(3))
    cross = ((0., -C[2], C[1]), (C[2], 0., -C[0]), (-C[1], C[0], 0.))
    C2, W2 = _dot(C, C), _dot(W, W)
    e2 = _sum(_sub(_mul(S[i][i], S[j][j]), _mul(S[i][j], S[j][i]))
              for i, j in ((0, 1), (0, 2), (1, 2)))
    bilinear_real = _sum(_sub(_mul(z.real, z.real), _mul(z.imag, z.imag)) for z in v)
    bilinear_imag = _mul(2., _sum(_mul(z.real, z.imag) for z in v))
    residuals = _SnapshotResiduals(
        _add(A, cross), tuple(_dot(row, C) for row in S),
        tuple(_sub(x, y) for x, y in zip(reconstructed, C)), W[2], _sub(e2, C2),
        _sum((_mul(frozen.intensity, frozen.intensity), -_mul(bilinear_real, bilinear_real),
              -_mul(bilinear_imag, bilinear_imag), -_mul(4., C2))),
        _sub(C2, checked_real(_sum((_mul(2., W2), _mul(Gamma, Gamma)))/3, "decomposition")))
    return AxialSnapshot(AXIAL_OBSERVER_REVISION, _SOURCE, _POLICY, S, A, C, Gamma,
                         parallel, perpendicular, W, frozen.intensity, frozen.chiral_norm,
                         checked_real(math.hypot(*W), "W norm"), frozen, residuals)


def axial_source_budget(omega, config, *, before_index, after_omega=None, after_index=None):
    """Algebraic one-step area accounting; facade owns State/Parameters checks.

    This reconstructs only the pre-sync complex expression and post-sync area
    identities. It does not invoke a dynamics update or return an evolved State.
    """
    before = axial_snapshot(omega)
    v = tuple(complex(z) for z in omega)
    eps, g, strength = config.eps, config.g, config.phase_strength
    D = _matrix(lambda i, j: _sub(config.k[i], before.S[i][i]) if i == j else 0.)
    M = _add(_matrix(lambda i, j: 1. if i == j else 0.), _scale(eps, D), _scale(g, L3))
    A = before.A
    terms = (
        _term("onsite_first", _scale(eps, _add(_mm(D, A), _mm(A, D)))),
        _term("coupling_first", _scale(g, _add(_mm(L3, A), _mm(A, L3)))),
        _term("onsite_squared", _scale(_mul(eps, eps), _mm(_mm(D, A), D))),
        _term("mixed", _scale(_mul(eps, g), _add(_mm(_mm(D, A), L3), _mm(_mm(L3, A), D)))),
        _term("coupling_squared", _scale(_mul(g, g), _mm(_mm(L3, A), L3))))
    pre = []
    for i in range(3):
        onsite = scale_complex(eps, scale_complex(D[i][i], v[i], "onsite"), "onsite")
        coupled = complex(_dot(L3[i], tuple(z.real for z in v)), _dot(L3[i], tuple(z.imag for z in v)))
        coupled = scale_complex(g, coupled, "coupling")
        pre.append(complex(_sum((v[i].real, onsite.real, coupled.real)),
                           _sum((v[i].imag, onsite.imag, coupled.imag))))
    pre = tuple(pre)
    S_tilde, A_tilde = _sa(pre)
    phases = tuple(checked_real(float(x), "Arg0") for x in arg0(pre))
    delta = tuple(_mul(strength, _sum(checked_real(math.sin(_mul(3., _sub(phases[j], phases[i]))), "phase sine")
                                   for j in ((i-1) % 3, (i+1) % 3))) for i in range(3))
    d = _matrix(lambda i, j: _sub(delta[j], delta[i]))
    cos = _matrix(lambda i, j: checked_real(math.cos(d[i][j]), "pair cosine"))
    sin = _matrix(lambda i, j: checked_real(math.sin(d[i][j]), "pair sine"))
    phase_terms = (
        _term("phase_existing_area", _matrix(lambda i, j: _mul(A_tilde[i][j], _sub(cos[i][j], 1.)))),
        _term("phase_symmetric_pair", _matrix(lambda i, j: _mul(S_tilde[i][j], sin[i][j]))))
    amplitude_sum = _add(A, *(t.A for t in terms))
    predicted = _area(_add(amplitude_sum, *(t.A for t in phase_terms)))
    # M is symmetric; congruence needs no inverse, including singular M.
    congruence = _area(_mm(_mm(M, A), M))
    pair = _area(_matrix(lambda i, j: _sum((_mul(A_tilde[i][j], cos[i][j]), _mul(S_tilde[i][j], sin[i][j])))))
    actual = None if after_omega is None else axial_snapshot(after_omega)
    return AxialSourceBudget(AXIAL_OBSERVER_REVISION, _SOURCE, _POLICY, before_index,
        after_index, _Parameters(eps, g, strength, tuple(config.k)), before, terms,
        _PreSync(pre, S_tilde, A_tilde, phases, delta, d), phase_terms, predicted,
        _difference(congruence, _area(amplitude_sum)), _difference(pair, predicted),
        actual, None if actual is None else _difference(actual, predicted),
        "PREDICTION_ONLY" if actual is None else "SUPPLIED_ADJACENT_PAIR",
        "Binary64 reconstruction of exact model identities; no advancement, stored intermediate, "
        "same-parent provenance, interval certificate or physical field claim.")
