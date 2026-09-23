"""Fixed November SRG and an explicit raw initialization handoff.

This linear transfer initializes, and does not reproduce, Paper-A evolution.
B is unitary/normal, so a right eigenvector supplies the required eigenbra.
Numerical cancellation in extraction is not an exact orthogonality certificate.
"""
from dataclasses import dataclass
import math
import numbers

import numpy as np

from ._response_numeric import (ResponsePrecisionError, bra_dot, checked_real,
                               complex_product, complex_vector, product, scale_complex)
from .boundary_response import RESPONSE_ID, _theta, lens_area_gain

GAUGE_ID = "spectral_projector_maxdiag_positive_v1"


@dataclass(frozen=True, slots=True)
class NovemberParameters:
    eta: float = .423
    gamma: float = .577
    lambda_c: float = .618
    clock_fraction: float = .244


NOVEMBER = NovemberParameters()


@dataclass(frozen=True, slots=True)
class SRGOperators:
    R: np.ndarray
    Z: np.ndarray
    C: np.ndarray
    A: np.ndarray
    B: np.ndarray
    U: np.ndarray


@dataclass(frozen=True, slots=True)
class HelicityMode:
    branch: str
    eigenvalue: complex
    chi: np.ndarray
    pivot: int
    gauge: str = GAUGE_ID


def fourier_basis():
    """Columns f0,f1,f2; f1=(1,conjugate(omega),omega)/sqrt(3)."""
    w = complex(-.5, math.sqrt(3)/2)
    return np.array([[1, 1, 1], [1, w.conjugate(), w],
                     [1, w, w.conjugate()]], complex)/math.sqrt(3)


def fixed_november_srg():
    """Fresh read-only fixed operators, U=B tensor (R Z C); copy to experiment."""
    f0 = fourier_basis()[:, 0]
    p = np.outer(f0, f0.conj())
    q, r, c = math.exp(-NOVEMBER.eta), math.exp(NOVEMBER.gamma), 1-NOVEMBER.lambda_c
    R = q*np.eye(3)+(r-q)*p
    C = c*np.eye(3)+(1-c)*p
    Z = np.diag([1, complex(-.5, -math.sqrt(3)/2), complex(-.5, math.sqrt(3)/2)])
    A = R@Z@C
    alpha, beta = 2*math.pi*NOVEMBER.clock_fraction, math.pi*NOVEMBER.clock_fraction
    B = np.diag([np.exp(-1j*alpha), np.exp(1j*alpha)]) @ np.array(
        [[math.cos(beta), -1j*math.sin(beta)], [-1j*math.sin(beta), math.cos(beta)]])
    U = np.kron(B, A)
    for operator in (R, Z, C, A, B, U):
        operator.setflags(write=False)
    return SRGOperators(R, Z, C, A, B, U)


def helicity_mode(branch):
    """Named eigenvalue and spectral-projector positive-pivot gauge; no eig()."""
    if not isinstance(branch, str) or branch not in ("negative_imag", "positive_imag"):
        raise ValueError("branch must be negative_imag or positive_imag")
    alpha, beta = 2*math.pi*NOVEMBER.clock_fraction, math.pi*NOVEMBER.clock_fraction
    tau = math.cos(alpha)*math.cos(beta)
    sign = -1 if branch == "negative_imag" else 1
    eigenvalue = complex(tau, sign*math.sqrt(1-tau*tau))
    other = eigenvalue.conjugate()
    B = fixed_november_srg().B
    projector = (B-other*np.eye(2))/(eigenvalue-other)
    pivot = int(np.argmax(projector.diagonal().real))  # first index on an exact tie
    chi = projector[:, pivot]/math.sqrt(projector[pivot, pivot].real)
    # This diagonal is real analytically; canonicalize its signed imaginary zero.
    chi[pivot] = complex(chi[pivot].real, 0)
    if (np.linalg.norm(B@chi-eigenvalue*chi) > 2e-14
            or abs(np.vdot(chi, chi).real-1) > 2e-14):
        raise ResponsePrecisionError("fixed helicity construction failed residual checks")
    chi.setflags(write=False)
    return HelicityMode(branch, eigenvalue, chi, pivot)


def project_bra(psi, bra):
    """Generic (bra-dagger tensor I3) projection; NO H1 or unit-norm promise.

    No overlap threshold is used. Checked products and compensated sums do not
    certify relative accuracy near cancellation; a computed zero can be rounded.
    """
    state = complex_vector(psi, 6, "psi").reshape(2, 3)
    h = complex_vector(bra, 2, "bra")
    return np.array([bra_dot(h, state[:, j], "bra projection") for j in range(3)])


def extract_helicity(psi, branch):
    """H1 extraction using only a named fixed-B eigenmode, on the full input space."""
    mode = helicity_mode(branch)
    return project_bra(psi, mode.chi)


def _transfer_count(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Integral):
        raise TypeError("transfer_count must be a nonnegative integer, not a boolean")
    if value < 0:
        raise ValueError("transfer_count must be nonnegative")
    return int(value)


def _cycle_gain(n):
    q, r, c = math.exp(-NOVEMBER.eta), math.exp(NOVEMBER.gamma), 1-NOVEMBER.lambda_c
    D = r*q*q*c*c
    m, j = divmod(n, 3)
    try:
        cycles = checked_real(D**m, "SRG cycle gain", nonzero=True)
    except OverflowError as exc:
        raise ResponsePrecisionError("transfer count exceeds normal cycle-gain range") from exc
    return product(cycles, (1, q, q*q*c)[j], "SRG cycle gain"), j


@dataclass(frozen=True, slots=True)
class HandoffResult:
    omega: np.ndarray
    theta: float
    xi: tuple[complex, complex]
    transfer_count: int
    branch: str

    def metadata(self):
        """JSON-ready initialization receipt; caller records downstream config too."""
        return {"response_id": RESPONSE_ID, "source_id": "november_fixed_srg",
                "source_parameters": {"eta": NOVEMBER.eta, "gamma": NOVEMBER.gamma,
                                      "lambda_c": NOVEMBER.lambda_c,
                                      "clock_fraction": NOVEMBER.clock_fraction,
                                      "alpha": "2*pi*0.244", "beta": "pi*0.244"},
                "tensor_order": "helicity_major_C2_tensor_C3", "branch": self.branch,
                "gauge": GAUGE_ID, "theta": self.theta,
                "xi": [[z.real, z.imag] for z in self.xi],
                "transfer_count": self.transfer_count, "normalization": "none"}


def handoff_area_response(theta, xi, *, transfer_count, branch, response):
    """Explicit option -> raw initial triad via the reviewed scalar/cycle formula.

    n=0 means no SRG application. This is not a downstream recurrence counter.
    Nonzero subnormal intermediate products/gains are outside the numerical
    domain even when some differently scaled evaluation could remain finite.
    """
    if not isinstance(response, str) or response != RESPONSE_ID:
        raise ValueError(f"response must explicitly select {RESPONSE_ID}")
    t = _theta(theta)
    incident = complex_vector(xi, 2, "xi")
    n = _transfer_count(transfer_count)
    mode = helicity_mode(branch)
    result = np.zeros(3, dtype=np.complex128)
    if t != 0 and np.any(incident != 0):
        overlap = bra_dot(mode.chi, incident, "incident overlap")
        if overlap != 0:  # literal calculated zero only, never a tolerance
            gain = lens_area_gain(t)
            bn, j = _cycle_gain(n)
            amplitude = scale_complex(gain, overlap, "boundary overlap amplitude")
            amplitude = scale_complex(bn, amplitude, "transferred amplitude")
            amplitude = complex_product(amplitude, complex(mode.eigenvalue**n), "helicity phase")
            result = np.array([complex_product(amplitude, complex(z), "initial component")
                               for z in fourier_basis()[:, j]])
    result.setflags(write=False)
    return HandoffResult(result, t, tuple(complex(z) for z in incident), n, branch)
