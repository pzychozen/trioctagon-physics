"""Exact algebra only for NATIVE_CLOSED_INFORMATION_01.

No repository imports, native-step implementation/evaluation, or trajectories.
Domain membership, fibres, closure, and minimality are proved in the note.
"""

import json
from pathlib import Path
import sys

import sympy as sp


checks = []


def check(name, residual, purpose):
    entries = list(residual) if isinstance(residual, sp.MatrixBase) else [residual]
    reduced = [sp.simplify(sp.expand_complex(value)) for value in entries]
    passed = all(value == 0 for value in reduced)
    checks.append({"name": name, "passed": passed, "purpose": purpose})
    if not passed:
        raise AssertionError((name, reduced))


s1 = sp.symbols("s1", positive=True)
p, q, x, ya = sp.symbols("p q x ya", real=True)
C12, C13 = p + sp.I * x, q + sp.I * ya
S23 = (p * q + x * ya) / s1
A23 = (p * ya - x * q) / s1
check("anchored_pair_product", sp.conjugate(C12) * C13 / s1 - (S23 + sp.I * A23),
      "Check the S23 and A23 reconstruction signs.")

s2, s3 = (p ** 2 + x ** 2) / s1, (q ** 2 + ya ** 2) / s1
representative = sp.Matrix([sp.sqrt(s1), C12 / sp.sqrt(s1), C13 / sp.sqrt(s1)])
H_formula = sp.Matrix([
    [s1, sp.conjugate(C12), sp.conjugate(C13)],
    [C12, s2, S23 - sp.I * A23],
    [C13, S23 + sp.I * A23, s3],
])
check("Hermitian_reconstruction", H_formula - representative * representative.H,
      "Check H = z z-dagger, with H_ij = conjugate(C_ij), using the modulus identities.")

real_part = sp.Matrix(sp.symbols("q1 q2 q3", real=True))
imag_part = sp.Matrix(sp.symbols("p1 p2 p3", real=True))
omega_symbolic = real_part + sp.I * imag_part
SG = real_part * real_part.T + imag_part * imag_part.T
AG = real_part * imag_part.T - imag_part * real_part.T
check("source_matrix_convention", omega_symbolic * omega_symbolic.H - (SG - sp.I * AG),
      "Independently check the source convention H = S_G - i A_G.")

N = sp.Matrix(3, 3, sp.symbols("n0:9", real=True))
check("skew_trace_vanishes", sp.trace(N * AG * N.T),
      "Any real N annihilates the skew contribution to this trace.")
check("trace_equals_squared_norm", sp.trace(N * (SG - sp.I * AG) * N.T) -
      ((N * real_part).T * (N * real_part))[0] -
      ((N * imag_part).T * (N * imag_part))[0],
      "Check the quadratic-form identity used to retain the prestage-increment norm.")

theta_i, theta_j = sp.symbols("theta_i theta_j", real=True)
normalized_Hji = sp.exp(sp.I * (theta_j - theta_i))
check("transposed_phase_entry", sp.im(normalized_Hji ** 3) - sp.sin(3 * (theta_j - theta_i)),
      "Check that the ji entry supplies the native phase-kick sign.")

ri, rj, rl = sp.symbols("ri rj rl", positive=True)
t, u, v = sp.symbols("t u v", real=True)
g = sp.Rational(1, 60)
delta_edge_il = (ri - rl) ** 2 + 2 * ri * rl * (1 - sp.cos(t)) - (ri - rl) ** 2
delta_edge_jl = (rj - rl) ** 2 + 2 * rj * rl * (1 - sp.cos(t)) - (rj - rl) ** 2
check("zero_or_one_entry_witness", g * (delta_edge_il + delta_edge_jl) / 2 -
      g * rl * (ri + rj) * (1 - sp.cos(t)),
      "Check the static potential difference with the retained pair unchanged.")
check("real_only_missing_pair", rj * rl * (sp.cos(u - v) - sp.cos(u + v)) -
      2 * rj * rl * sp.sin(u) * sp.sin(v),
      "Check the omitted real coherence difference in the two-real-entry witness.")
edge_minus = rj ** 2 + rl ** 2 - 2 * rj * rl * sp.cos(u + v)
edge_plus = rj ** 2 + rl ** 2 - 2 * rj * rl * sp.cos(u - v)
check("real_only_energy_obstruction", g * (edge_minus - edge_plus) / 2 -
      2 * g * rj * rl * sp.sin(u) * sp.sin(v),
      "Check the exact static potential difference at the fixed graph coefficient.")

report = {
    "task": "NATIVE_CLOSED_INFORMATION_01",
    "status": "PASS",
    "python": sys.version,
    "executable": sys.executable,
    "sympy_version": sp.__version__,
    "scope": "Symbolic coherence identities, generic real-matrix trace identity, and static analytic witness differences only.",
    "limitations": "No native-step calls or implementations, trajectories, profile solves, sampled domains, old helper runs, or floating-point certificates. Continuous-domain and minimality claims are supplied by the written proof.",
    "checks": checks,
}
output = Path(__file__).resolve().with_name("exact_algebra_results.json")
with output.open("x", encoding="utf-8") as handle:
    json.dump(report, handle, indent=2)
    handle.write("\n")
print("PASS: reconstruction, coherence signs, trace/norm identity, static energy witnesses")
print(f"Python: {sys.executable}; SymPy: {sp.__version__}")
print(output)
