"""Isolated symbolic checks for NATIVE_ENERGY_RESPONSE_01.

No repository imports, native-state evaluations, roots, or trajectories.
The written proof, not these checks, establishes the continuous-domain claims.
"""

import json
from pathlib import Path
import sys

import sympy as sp


results = []


def check(name, residual, purpose):
    entries = list(residual) if isinstance(residual, sp.MatrixBase) else [residual]
    simplified = [sp.factor(sp.cancel(value)) for value in entries]
    passed = all(value == 0 for value in simplified)
    results.append({"name": name, "passed": passed, "purpose": purpose})
    if not passed:
        raise AssertionError((name, simplified))


r = sp.Matrix(sp.symbols("r1 r2 r3", positive=True))
g, lam = sp.symbols("g lam", real=True)
eps = sp.symbols("eps", real=True, nonzero=True)
k = sp.Matrix(sp.symbols("k1 k2 k3", real=True))
one = sp.ones(3, 1)
eye = sp.eye(3)
L = one * one.T - 3 * eye
R = sp.diag(*r)
M = sum(r) * R.inv() - one * one.T
H_general = eye + eps * sp.diag(*[k[i] - r[i] ** 2 for i in range(3)]) + g * L
fixed_sub = {k[i]: r[i] ** 2 - g * (L * r)[i] / (eps * r[i]) for i in range(3)}
H = eye - g * M
P = R.inv() * H * R
K = R * (eye - H) * R
A_general = H_general - 2 * eps * R ** 2
d = 1 - 9 * lam
J = (eye + 3 * lam * L) * P

check("fixed_profile_H", H_general.subs(fixed_sub) - H,
      "The fixed equations imply H = I - g M3.")
check("row_sum_and_kernel", (P * one - one).col_join(K * one),
      "P fixes common phase and K annihilates it.")

q = sp.Matrix(sp.symbols("q1 q2 q3", real=True))
phi = sp.Matrix(sp.symbols("phi1 phi2 phi3", real=True))
polar = eps * sum(q[i] ** 4 / 4 - k[i] * q[i] ** 2 / 2 for i in range(3))
polar += g / 2 * sum(q[i] ** 2 + q[j] ** 2 - 2 * q[i] * q[j] * sp.cos(phi[i] - phi[j])
                     for i in range(3) for j in range(i + 1, 3))
at_profile = {**dict(zip(q, r)), **dict.fromkeys(phi, 0)}
polar_hessian = sp.hessian(polar, list(q) + list(phi)).subs(at_profile)
check("polar_amplitude_hessian", polar_hessian[:3, :3] - (eye - A_general),
      "Differentiate the native potential to check B = I - A.")
check("polar_phase_hessian", polar_hessian[3:, 3:] - K,
      "Differentiate the native potential to check its phase Hessian K.")
check("mixed_hessian_zero", polar_hessian[:3, 3:],
      "The mixed amplitude/phase quadratic terms vanish at alignment.")
check("weighted_Dirichlet_form", (phi.T * K * phi)[0] -
      g * sum(r[i] * r[j] * (phi[i] - phi[j]) ** 2
              for i in range(3) for j in range(i + 1, 3)),
      "Check the edge-once normalization of K.")
check("P_K_self_adjointness", P.T * K - K * P,
      "Check that P is self-adjoint for the inherited potential form.")
check("triad_J_decomposition", J - d * P - 3 * lam * one * (one.T * P),
      "Check synchronization-after-prestage order and the common-phase term.")
check("J_K_contraction_identity", J.T * K * J - d ** 2 * P.T * K * P,
      "Check the exact quadratic phase-change reduction.")

alpha = sp.symbols("alpha", real=True)
check("amplitude_decrement", alpha ** 2 * (1 - alpha) - (1 - alpha) -
      (1 - alpha) * (alpha ** 2 - 1),
      "Check the amplitude eigenmode coefficient; strict signs are proved in the note.")

ell = 3 * lam
s1, s2, s3 = sum(r), r[0] * r[1] + r[0] * r[2] + r[1] * r[2], sp.prod(r)
cycle = J[0, 1] * J[1, 2] * J[2, 0] - J[1, 0] * J[2, 1] * J[0, 2]
cycle_factor = (g ** 2 * ell * s1 ** 3 +
                (g ** 2 * (1 - 2 * ell) - g * ell) * s1 * s2 +
                (3 * g * ell - g + ell) * s3)
vandermonde = (r[0] - r[1]) * (r[0] - r[2]) * (r[1] - r[2])
check("cycle_factorization", cycle - g * ell * d * vandermonde * cycle_factor / s3 ** 2,
      "Independently check the inherited rational factorization and its sign convention.")
radius = sp.symbols("radius", positive=True)
K0 = g * (9 * g - 1) + ell * (1 - 3 * g) ** 2
check("cycle_factor_at_equal_radii", cycle_factor.subs(dict.fromkeys(r, radius)) - radius ** 3 * K0,
      "Check the coefficient used in the weak-heterogeneity comparison.")

x, y, onsite_k = sp.symbols("x y onsite_k", real=True)
xy = sp.Matrix([x, y])
onsite = eps * ((x ** 2 + y ** 2) ** 2 / 4 - onsite_k * (x ** 2 + y ** 2) / 2)
check("Cartesian_onsite_hessian", sp.hessian(onsite, [x, y]) -
      eps * ((x ** 2 + y ** 2 - onsite_k) * sp.eye(2) + 2 * xy * xy.T),
      "Independently differentiate the block used for the whole-segment curvature bound.")
curvature = sp.Rational(1, 10) * (3 * sp.Rational(11, 10) ** 2 - sp.Rational(999, 1000)) + 3 * sp.Rational(1, 60)
coefficient = 1 - curvature / 2
check("finite_domain_curvature", curvature - sp.Rational(3131, 10000),
      "Check the exact upper-curvature constant.")
check("finite_domain_decrease_coefficient", coefficient - sp.Rational(16869, 20000),
      "Check the exact unit-step Taylor coefficient.")

S, area, angle = sp.symbols("S area angle", real=True)
pair_after = (S + sp.I * area) * (sp.cos(angle) + sp.I * sp.sin(angle))
check("pair_rotation_real_part", sp.re(sp.expand(pair_after)) - (S * sp.cos(angle) - area * sp.sin(angle)),
      "Check the area sign for conj(Omega_i) Omega_j and delta_j - delta_i.")

report = {
    "task": "NATIVE_ENERGY_RESPONSE_01",
    "status": "PASS",
    "python": sys.version,
    "executable": sys.executable,
    "sympy_version": sp.__version__,
    "scope": "Exact symbolic response/potential identities and exact rational constants only.",
    "limitations": "No native evaluations, roots, trajectories, interval runtime certificates, or numerical tests. The written proof supplies domain, signs, and nonlinear remainder arguments.",
    "curvature": str(curvature),
    "decrease_coefficient": str(coefficient),
    "checks": results,
}
output = Path(__file__).resolve().with_name("exact_algebra_results.json")
with output.open("x", encoding="utf-8") as handle:
    json.dump(report, handle, indent=2)
    handle.write("\n")
print(f"PASS: exact symbolic identities; curvature={curvature}; decrease={coefficient}")
print(f"Python: {sys.executable}; SymPy: {sp.__version__}")
print(output)
