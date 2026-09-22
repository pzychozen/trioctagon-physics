"""Independent, deterministic Phase III checks; no kernel imports or old suites.

Run with python -B verify_phase_bridge_III.py. Writes only the two adjacent
results files. Symbolic predicates, numerical checks, and observations are
reported separately. This is verification code, not a kernel implementation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASELINE = "899d0fa900dc0d0ab8406e889908e47468d343db"
TRACKED_DIGEST = "9ce79620e720e538e0295374ca1a504fecc5c6e0c9957cb0418a842ca6bacb80"
ORIGINAL_HASH = "d19178a45b44f422a0f9f5c38494c79778914be846f3e2eddb118e29baa68f95"
CLAUDE_HASH = "bd051995d03cec556ac291575249164755c23351ef1102a3af34a3cb373c8a5c"
checks: list[dict] = []
observations: dict = {}


def check(name, predicate, kind="symbolic", detail=None):
    checks.append(dict(name=name, kind=kind, passed=bool(predicate), detail=detail))


def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(v) == 0 for v in expr)
    return sp.simplify(expr) == 0


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def preservation():
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    records = {p: digest(ROOT / p) for p in tracked if p}
    aggregate = hashlib.sha256("".join(f"{p}\0{records[p]}\n" for p in sorted(records)).encode()).hexdigest()
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip()
    check("frozen_tracked_content_preserved", aggregate == TRACKED_DIGEST, "integrity", {"files": len(records), "sha256": aggregate})
    check("baseline_head_preserved", head == BASELINE, "integrity", head)
    check("original_phase_III_preserved", digest(HERE / "PHASE_BRIDGE_III_RECURSIVE_TIME_ACTION_ANGLE.md") == ORIGINAL_HASH, "integrity")
    check("claude_copy_byte_identical", digest(HERE / "PHASE_BRIDGE_III_CLAUDE_ADVERSARIAL_REVIEW.md") == CLAUDE_HASH, "integrity")
    external = ROOT.parent / "research/phase_bridge_III_claude_review/PHASE_BRIDGE_III_CLAUDE_ADVERSARIAL_REVIEW.md"
    if external.exists():
        check("external_claude_preserved", digest(external) == CLAUDE_HASH, "integrity")
    observations["frozen_hashes"] = {"tracked": records, "original": ORIGINAL_HASH, "claude": CLAUDE_HASH}


def symbolic_threshold_and_manifolds():
    eps, g, K, k, alpha, r = sp.symbols("eps g K k alpha r", real=True, nonzero=True)
    rs = sp.symbols("r1:4", positive=True)
    ph = sp.symbols("p1:4", real=True)
    radial = sp.Matrix([
        eps * rs[i] * (k - rs[i]**2)
        + g * (sum(rs[j] * sp.cos(ph[j] - ph[i]) for j in range(3) if j != i) - 2 * rs[i])
        for i in range(3)])
    angular = sp.Matrix([
        g * sum(rs[j] / rs[i] * sp.sin(ph[j] - ph[i]) for j in range(3) if j != i)
        + K * sum(sp.sin(3 * (ph[j] - ph[i])) for j in range(3) if j != i)
        + alpha * rs[i]**2 / 2
        for i in range(3)])
    field = radial.col_join(angular)
    angles = [0, 2 * sp.pi / 3, 4 * sp.pi / 3]
    sub = dict(zip(rs, [r] * 3)) | dict(zip(ph, angles))
    jac = field.jacobian(rs + ph).subs(sub).applyfunc(sp.simplify)
    T = sp.diag(r, r, r, 1, 1, 1)
    normalized = (T.inv() * jac * T).subs(k, r**2 + 3 * g / eps).applyfunc(sp.simplify)
    L = sp.ones(3) - 3 * sp.eye(3)
    S = sp.Matrix(3, 3, lambda i, j: sp.sin(angles[j] - angles[i]))
    P = sp.eye(3) - sp.ones(3) / 3
    expected = (-2 * eps * r**2 * sp.eye(3) - g * L / 2).row_join(-g * S).col_join(
        (r**2 * alpha * sp.eye(3) + g * S).row_join((-g / 2 + 3 * K) * L))
    check("N1_full_field_jacobian_matches_blocks", zero(normalized - expected))
    check("N1_splay_skew_matrix_square", zero(S * S + 9 * P / 4))
    lam = sp.symbols("lam", real=True)
    a, d, c = -2 * eps * r**2 + 3 * g / 2, 3 * g / 2 - 9 * K, r**2 * alpha
    tau, D = a + d, a * d - 9 * g**2 / 4
    predicted = lam * (lam + 2 * eps * r**2) * ((lam**2 - tau * lam + D)**2 + (3 * g * c / 2)**2)
    charpoly = normalized.charpoly()
    # SymPy's charpoly generator does not retain a supplied symbol's assumptions.
    check("N1_full_six_dimensional_characteristic_polynomial", zero(charpoly.as_expr().subs(charpoly.gen, lam) - predicted))
    aa, dd, gg, cc, ww = sp.symbols("a d g c w", real=True)
    poly_iw = (sp.I * ww)**2 - (aa + dd) * sp.I * ww + aa * dd - 9 * gg**2 / 4 + sp.I * 3 * gg * cc / 2
    check("N1_imaginary_root_real_equation", zero(sp.re(poly_iw) - (aa * dd - 9 * gg**2 / 4 - ww**2)))
    check("N1_imaginary_root_imag_equation", zero(sp.im(poly_iw) - (3 * gg * cc / 2 - (aa + dd) * ww)))
    tt, DD, bb = sp.symbols("tau D b", real=True)
    A1, A2, A3, A4 = -2 * tt, tt**2 + 2 * DD, -2 * tt * DD, DD**2 + bb**2
    check("N1_routh_hurwitz_second_minor", zero(A1 * A2 - A3 + 2 * tt * (tt**2 + DD)))
    check("N1_routh_hurwitz_third_minor", zero(A1 * A2 * A3 - A3**2 - A1**2 * A4 - 4 * tt**2 * (tt**2 * DD - bb**2)))
    witness = {eps: 1, g: 1, K: 1, r: sp.sqrt(3)}
    cstar2 = (tau**2 * (4 * a * d / (9 * g**2) - 1)).subs(witness)
    check("N1_witness_alpha_squared_224", zero(cstar2 / 9 - 224))
    check("N1_witness_frequency", zero(D.subs(witness) - sp.Rational(63, 2)))
    for sign, tag in [(0, "synchronous"), (1, "splay_plus"), (-1, "splay_minus")]:
        ss = dict(zip(rs, [r] * 3)) | dict(zip(ph, [sign * p for p in angles]))
        shift = 0 if sign == 0 else 3 * g
        check(f"N4_{tag}_radial_invariance", zero(radial.subs(ss) - sp.ones(3, 1) * r * (eps * (k - r**2) - shift)))
        check(f"N4_{tag}_equal_angular_rates", zero(angular.subs(ss) - sp.ones(3, 1) * alpha * r**2 / 2))
    # Arbitrary real phase velocities represent both K and local-clock terms.
    xs, ys, rates = sp.symbols("x1:4", real=True), sp.symbols("y1:4", real=True), sp.symbols("w1:4", real=True)
    zz = sp.Matrix([xs[i] + sp.I * ys[i] for i in range(3)])
    cart = sp.Matrix([eps * zz[i] * (k - xs[i]**2 - ys[i]**2) + g * (L * zz)[i] + sp.I * rates[i] * zz[i] for i in range(3)])
    Ndot = sp.expand(sum(sp.re(sp.conjugate(zz[i]) * cart[i]) for i in range(3)))
    growth = eps * sum((xs[i]**2 + ys[i]**2) * (k - xs[i]**2 - ys[i]**2) for i in range(3))
    edges = sum((xs[i] - xs[j])**2 + (ys[i] - ys[j])**2 for i in range(3) for j in range(i + 1, 3))
    check("N4_total_action_balance_identity", zero(Ndot - growth + g * edges))
    check("N4_phase_terms_absent_from_balance", all(sp.diff(Ndot, w) == 0 for w in rates))
    omega0 = sp.symbols("omega0", real=True)
    cg = sp.Matrix([(eps * k + sp.I * omega0) * zz[i] - (eps - sp.I * alpha / 2) * (xs[i]**2 + ys[i]**2) * zz[i] + g * (L * zz)[i] for i in range(3)])
    affine = cart.subs({rates[i]: omega0 + alpha * (xs[i]**2 + ys[i]**2) / 2 for i in range(3)})
    check("oscillator_equivalence_K_zero", zero(affine - cg))
    extra_at_point = sp.I * K * (sp.sin(3 * sp.pi / 6) + sp.sin(0))
    check("nonzero_K_extra_term_counterexample", zero(extra_at_point - sp.I * K) and not zero(extra_at_point))


def threshold_fixtures():
    rows = []
    for ep, gg, KK, kk in [(1, 1, 1, 6), (1, .8, .5, 5), (.7, 1.3, 2, 9), (2, .5, .25, 4)]:
        R = kk - 3 * gg / ep
        a, d = -2 * ep * R + 1.5 * gg, 1.5 * gg - 9 * KK
        tau, D = a + d, a * d - 2.25 * gg**2
        astar = abs(tau) * np.sqrt(4 * D / (9 * gg**2)) / R
        def spectral_abscissa(al):
            # Real 6x6 matrix assembled independently from the differentiated blocks.
            theta = np.arange(3) * 2 * np.pi / 3
            S = np.sin(theta[None, :] - theta[:, None])
            L = np.ones((3, 3)) - 3 * np.eye(3)
            J = np.block([[-2 * ep * R * np.eye(3) - gg * L / 2, -gg * S],
                          [R * al * np.eye(3) + gg * S, (-gg / 2 + 3 * KK) * L]])
            eig = np.linalg.eigvals(J)
            eig = np.delete(eig, np.argmin(abs(eig)))  # Known common-phase zero only.
            return float(max(eig.real)), eig
        lo, elo = spectral_abscissa(.99 * astar)
        at, eat = spectral_abscissa(astar)
        hi, ehi = spectral_abscissa(1.01 * astar)
        frequency = abs(eat[np.argmax(eat.real)].imag)
        label = f"{ep}_{gg}_{KK}_{kk}"
        check(f"N1_fixture_{label}_crossing", R > 0 and tau < 0 and D > 0 and lo < 0 < hi and abs(at) < 1e-10, "numerical")
        check(f"N1_fixture_{label}_frequency", abs(frequency - np.sqrt(D)) < 1e-10, "numerical")
        rows.append(dict(eps=ep, g=gg, K=KK, k=kk, r_squared=R, a=a, d=d, alpha_threshold=astar,
                         frequency=frequency, below_abscissa=lo, at_abscissa=at, above_abscissa=hi))
    observations["threshold_fixtures"] = rows


def h1_and_monodromy():
    rho, phi, nu = sp.symbols("rho phi nu", real=True)
    v, S = sp.Function("v")(rho), sp.Function("S")(phi)
    F, U = sp.Function("F")(rho), sp.Function("U")(phi)
    Q = F - nu * U
    M = sp.Function("G")(Q) / (1 - rho)
    f, w = nu * (1 - rho) * S, v
    derivatives = {sp.diff(F, rho): v / (1 - rho), sp.diff(U, phi): S}
    check("N2_first_integral_derivative", zero((sp.diff(Q, rho) * f + sp.diff(Q, phi) * w).subs(derivatives)))
    check("N3_multiplier_divergence", zero((sp.diff(M * f, rho) + sp.diff(M * w, phi)).subs(derivatives)))
    B = sp.Function("B")(rho, phi)
    divergence = sp.diff(B / (1 - rho) * f, rho) + sp.diff(B / (1 - rho) * w, phi)
    check("N3_general_multiplier_transport_equation", zero((1 - rho) * divergence - (f * sp.diff(B, rho) + v * sp.diff(B, phi))))
    check("N3_contraction_sign", zero(M * f - nu * S * sp.Function("G")(Q)) and zero(-M * v + sp.Function("G")(Q) * v / (1 - rho)))
    ydot = sp.diff(-sp.log(1 - rho), rho) * f
    check("H1_log_chart_vector_field", zero(ydot - nu * S))
    check("H1_divergence_log_identity", zero(sp.diff(f, rho) + sp.diff(w, phi) - sp.diff(sp.log(1 - rho), rho) * f))
    # Historical S form; a domain exit is detected from an exact separation
    # of variables plus a controlled scalar quadrature, not an ODE solver.
    y0 = -np.log(.99)
    source = lambda p: np.sin(.2 + 2 * np.sin(p))
    initial_phase = 1.5 * np.pi
    short_int, err = quad(source, initial_phase, initial_phase + .1, epsabs=1e-13)
    mean_int, mean_err = quad(source, 0, 2 * np.pi, epsabs=1e-13)
    check("N2_positive_mean_early_lower_exit", mean_int > 0 and y0 + short_int < -1e-3 and err < 1e-10, "numerical")
    # |S|<=1 ensures every partial turn integral >= -2pi. For v=1000,
    # even this coarse bound is positive; positive mean makes later turns safer.
    check("N2_same_forcing_fast_warp_survives", y0 - 2 * np.pi / 1000 > 0 and mean_int > 0, "numerical")
    zero_source = lambda p: np.sin(np.pi / 2 * np.sin(p))
    zero_segment, zerr = quad(zero_source, np.pi, 2 * np.pi, epsabs=1e-13)
    zero_mean, zmerr = quad(zero_source, 0, 2 * np.pi, epsabs=1e-13)
    check("N2_zero_mean_early_exit_counterexample", abs(zero_mean) < 1e-12 and y0 + zero_segment < 0, "numerical")
    # On the extended rho<1 domain with v=1 this same zero-mean orbit
    # returns exactly by the primitive identity; its negative-rho excursion
    # is precisely why it is not a closed orbit in the historical interior.
    observations["h1_domain_counterexamples"] = dict(rho_initial=.01, positive_case_phi_initial=initial_phase,
        positive_mean=mean_int, initial_short_integral=short_int, quadrature_error_bound=err,
        slow_v_1_y_after_segment=y0 + short_int, fast_v_1000_lower_y_bound=y0 - 2 * np.pi / 1000,
        zero_mean=zero_mean, zero_case_halfturn_integral=zero_segment,
        zero_case_extended_rho_after_halfturn=1 - np.exp(-(y0 + zero_segment)))
    # Exact H1: S=0, v=1+rho, rho0=1/2. T=4pi/3 and shear=T.
    n = sp.symbols("n", integer=True, nonnegative=True)
    shear = 4 * sp.pi / 3
    monodromy = sp.Matrix([[1, 0], [shear, 1]])
    check("N6_exact_jordan_characteristic", zero(monodromy.charpoly().as_expr() - (monodromy.charpoly().gen - 1)**2))
    check("N6_exact_nonsemisimple", (monodromy - sp.eye(2)).rank() == 1 and zero((monodromy - sp.eye(2))**2))
    dt = sp.symbols("delta", real=True)
    disturbed = sp.Matrix([[1, dt], [shear, 1]])
    lam = sp.symbols("lam")
    check("N6_square_root_perturbation_law", zero(disturbed.charpoly(lam).as_expr() - ((lam - 1)**2 - shear * dt)))
    data = []
    for sign in [-1, 1]:
        perturb = sign * np.finfo(float).eps
        mat = np.array([[1., perturb], [float(shear), 1.]])
        eig = np.linalg.eigvals(mat)
        split = float(max(abs(eig - 1)))
        predicted = np.sqrt(abs(float(shear) * perturb))
        check(f"N6_machine_scale_splitting_{sign}", abs(split / predicted - 1) < 1e-7 and abs(np.trace(mat) - 2) < 1e-14 and abs(np.linalg.det(mat) - 1) < 2e-15, "numerical")
        data.append(dict(perturbation=perturb, eigenvalues=[[float(z.real), float(z.imag)] for z in eig],
                         max_split=split, predicted_split=predicted, trace=float(np.trace(mat)), determinant=float(np.linalg.det(mat))))
    observations["jordan_controlled_perturbations"] = data


def quotient_rhs(t, y, alpha):
    actions = np.exp(y[:3])
    radii = np.sqrt(2 * actions)
    phases = np.array([0., y[3], y[4]])
    delta = phases[None, :] - phases[:, None]
    # Diagonal cosine includes the self term: subtract 3*g, not 2*g.
    radial_over_r = 6 - radii**2 + (np.cos(delta) @ radii) / radii - 3
    rates = (np.sin(delta) @ radii) / radii + np.sin(3 * delta).sum(axis=1) + 1 + alpha * (actions - 1.5)
    return np.r_[2 * radial_over_r, rates[1:] - rates[0]]


def branch_errors(y):
    actions = np.exp(y[:3])
    relative = np.exp(1j * y[3:])
    roots = np.exp(1j * np.array([2 * np.pi / 3, 4 * np.pi / 3]))
    syn = max(float(max(abs(actions - 3))), float(max(abs(relative - 1))))
    plus = max(float(max(abs(actions - 1.5))), float(max(abs(relative - roots))))
    minus = max(float(max(abs(actions - 1.5))), float(max(abs(relative - np.conj(roots)))))
    return np.array([syn, plus, minus])


def quotient_cartesian_checks():
    L = np.ones((3, 3)) - 3 * np.eye(3)
    for index, (actions, phases, alpha) in enumerate([
            ([.5, 2., 4.5], [0., .3, -1.2], 2.),
            ([1.4, 1.6, 1.5], [0., 2.1, 4.2], 15.),
            ([3., 3., 3.], [0., .01, -.02], 25.)]):
        actions, phases = np.array(actions), np.array(phases)
        z = np.sqrt(2 * actions) * np.exp(1j * phases)
        delta = phases[None, :] - phases[:, None]
        zdot = z * (6 - abs(z)**2) + L @ z + 1j * z * (np.sin(3 * delta).sum(axis=1) + 1 + alpha * (actions - 1.5))
        I_dot = np.real(np.conj(z) * zdot)
        phase_dot = np.imag(zdot / z)
        from_cartesian = np.r_[I_dot / actions, phase_dot[1:] - phase_dot[0]]
        from_quotient = quotient_rhs(0., np.r_[np.log(actions), phases[1:]], alpha)
        check(f"N5_quotient_cartesian_derivative_{index}", np.max(abs(from_cartesian - from_quotient)) < 1e-12, "numerical")


def quotient_runs():
    threshold = 4 * np.sqrt(14)
    base = np.r_[np.log([1.5] * 3), 2 * np.pi / 3, 4 * np.pi / 3]
    direction = np.array([.4, -.3, -.1, .7, -.5])
    fixtures = [("above_005", threshold + .05, base + .01 * direction),
                ("above_025", threshold + .25, base + .01 * direction),
                ("above_100", threshold + 1., base + .01 * direction),
                ("below_small", threshold - .05, base + .01 * direction),
                ("below_large", threshold - .05, base + .2 * direction),
                ("below_inphase", threshold - .05, np.r_[np.log([3.] * 3), 0., 0.] + .01 * direction)]
    runs = []
    for label, alpha, y0 in fixtures:
        solutions = []
        for precision, rtol, atol, max_step in [("standard", 2e-12, 2e-14, .1), ("tight", 5e-14, 5e-16, .05)]:
            def arrived(t, y):
                return min(branch_errors(y)) - 1e-8
            arrived.terminal = True
            arrived.direction = -1
            sol = solve_ivp(lambda t, y: quotient_rhs(t, y, alpha), (0., 2400.), y0,
                            method="DOP853", rtol=rtol, atol=atol, max_step=max_step,
                            events=arrived, dense_output=True)
            endpoint = sol.y[:, -1]
            errors = branch_errors(endpoint)
            idx = int(np.argmin(errors))
            destination = ["in_phase", "splay_plus", "splay_minus"][idx] if errors[idx] < 2e-8 else "unresolved_at_horizon"
            sample = sol.sol(np.linspace(0., sol.t[-1], 2001))
            # Confirm a further finite interval at tighter settings after arrival.
            tail = solve_ivp(lambda t, y: quotient_rhs(t, y, alpha), (0., 5.), endpoint,
                             method="DOP853", rtol=2e-12, atol=2e-14, max_step=.1)
            tail_error = float(branch_errors(tail.y[:, -1])[idx])
            row = dict(label=label, alpha=alpha, precision=precision, initial_log_action_relative_phase=y0.tolist(),
                       initial_branch_errors=branch_errors(y0).tolist(), rtol=rtol, atol=atol, max_step=max_step,
                       time_horizon=2400., termination_time=float(sol.t[-1]), nfev=sol.nfev,
                       solver_success=bool(sol.success and tail.success), destination=destination,
                       final_branch_errors=errors.tolist(), final_actions=np.exp(endpoint[:3]).tolist(),
                       final_relative_phases_wrapped=np.angle(np.exp(1j * endpoint[3:])).tolist(),
                       minimum_sampled_action=float(np.min(np.exp(sample[:3]))),
                       sampled_max_splay_departure=float(max(branch_errors(sample[:, j])[1] for j in range(sample.shape[1]))),
                       five_unit_tail_error=tail_error)
            runs.append(row)
            solutions.append(sol)
            check(f"N5_{label}_{precision}_solver_and_arrival", sol.success and tail.success and destination != "unresolved_at_horizon" and tail_error < 2e-8, "numerical")
            print(f"{label} {precision}: {destination}; t={sol.t[-1]:.6f}; tail={tail_error:.3g}", flush=True)
        pair = runs[-2:]
        check(f"N5_{label}_tolerance_destination_agreement", pair[0]["destination"] == pair[1]["destination"], "numerical")
        # Threshold arrival time is ill-conditioned for an oscillatory error
        # envelope near 1e-8; compare trajectories at common times instead.
        common_times = np.linspace(0., min(s.t[-1] for s in solutions), 10001)
        sampled = [s.sol(common_times) for s in solutions]
        difference = max(float(np.max(abs(np.exp(sampled[0][:3]) - np.exp(sampled[1][:3])))),
                         float(np.max(abs(np.exp(1j * sampled[0][3:]) - np.exp(1j * sampled[1][3:])))))
        check(f"N5_{label}_tolerance_trajectory_agreement", difference < 1e-3, "numerical", {"maximum_action_or_phasor_difference": difference, "common_time_samples": 10001})
    observations["quotient_runs"] = runs
    observations["N5_observed_outcomes"] = {r["label"]: r["destination"] for r in runs if r["precision"] == "tight"}


def main():
    start = datetime.now(timezone.utc)
    preservation()
    symbolic_threshold_and_manifolds()
    threshold_fixtures()
    h1_and_monodromy()
    quotient_cartesian_checks()
    print("Symbolic and controlled checks complete; beginning deterministic quotient fixtures.", flush=True)
    quotient_runs()
    counts = {k: sum(c["kind"] == k for c in checks) for k in sorted({c["kind"] for c in checks})}
    result = dict(provenance={"started_utc": start.isoformat(), "finished_utc": datetime.now(timezone.utc).isoformat(),
                             "baseline": BASELINE, "python": platform.python_version(), "numpy": np.__version__,
                             "scipy": scipy.__version__, "sympy": sp.__version__, "script_sha256": digest(Path(__file__)),
                             "command": "python -B research/phase_bridge_III/verify_phase_bridge_III.py",
                             "random_draws": 0, "imports_frozen_kernel": False, "old_suites_executed": False,
                             "claude_checks_reexecuted": False},
                  predicate_count=len(checks), passed=sum(c["passed"] for c in checks), failed=sum(not c["passed"] for c in checks),
                  predicate_kinds=counts, checks=checks, observations=observations)
    (HERE / "phase_bridge_III_results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["Phase Bridge III: independent execution record", json.dumps(result["provenance"], indent=2),
             f"Computed predicates: {result['passed']} / {len(checks)} passed; failed={result['failed']}",
             "These are finite regression/symbolic predicates, not independent theorems.",
             "Counts by kind: " + json.dumps(counts)]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} [{c['kind']}] {c['name']}" for c in checks]
    for label in ["threshold_fixtures", "h1_domain_counterexamples", "jordan_controlled_perturbations", "N5_observed_outcomes", "quotient_runs"]:
        lines += ["\n" + label, json.dumps(observations[label], indent=2)]
    (HERE / "phase_bridge_III_results.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"RESULT: {result['passed']}/{len(checks)} passed; {result['failed']} failed", flush=True)
    return int(result["failed"] != 0)


if __name__ == "__main__":
    sys.exit(main())
