"""Atlas 06: external, read-only source audit and independent observer checks.

Run with conda torment Python, -B. No historical module or runner is imported.
Only the two hash-bound update_z method bodies execute in a minimal namespace.
Analytical proofs are in the accompanying packet; runtime checks are witnesses,
not proofs of universal floating-point accuracy or historical system behavior.

Usage:
  python -B THIS_FILE --evidence-dir EXTERNAL_DIR
  python -B THIS_FILE --evidence-dir EXTERNAL_DIR --finalize-integrity
  python -B THIS_FILE --evidence-dir EXTERNAL_DIR --capture before
Capture after with the same option when all source/test activity is complete.
The initial investigation used the identical capture algorithm in an external
helper; its before/after JSON files are accepted and independently compared here.
"""
from __future__ import annotations

import argparse
import ast
import copy
from dataclasses import FrozenInstanceError, fields
from datetime import datetime, timezone
import hashlib
import inspect
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import patch

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
ROOT = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
ROOTS = {
    "current": ROOT,
    "old": Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO"),
    "torment_kernel": Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric\torment_service\kernel"),
    "torment_checkout": Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric"),
}
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "TRIOCTAGON_ATLAS_06_EXACT_RESULTS.json"
DEFAULT_EVIDENCE = Path(r"C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas06_20260929_aomyfjvw")
GROUPS = ("EXACT_ALGEBRA", "EXACT_BOUNDS", "EXACT_SYMMETRY", "RUNTIME/API",
          "PRECISION/FALSIFIER", "HISTORICAL_REPLAY", "INTEGRITY")
PAPER = "papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md"
SNAPSHOTS = {
    "staged": ("papers/PAPER_E/evidence/source_snapshots/staged/model_core.py",
               "ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6"),
    "ema": ("papers/PAPER_E/evidence/source_snapshots/committed_ema/model_core.py",
            "cd173dd818bd20983e23a72c2195b513eb3d72ae0446db8239c65657fd7d17b2"),
}
SOURCE_FILES = [
    "kernel_physics/z_manifold.py", "kernel_physics/_response_numeric.py",
    "kernel_physics/readouts.py", "kernel_physics/dynamics.py",
    "kernel_physics/tests/test_z_manifold.py", PAPER,
    "papers/PAPER_E/check_symbolic.py", "papers/PAPER_E/evidence/symbolic_results.json",
    "papers/PAPER_E/evidence/source_provenance.json",
    "papers/PAPER_E/v0.1.1/check_revision.py",
    "papers/PAPER_E/evidence/accepted_reconstruction/verify_historical_z.py",
    "kernel_physics/tests/test_parity_p09_p10.py",
    "kernel_physics/tests/parity_oracles/paper_e_oracle.py",
    "kernel_physics/_runner.py", "kernel_physics/tests/test_runner_records.py",
    "kernel_physics/z_diagnostics.py",
    "research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md",
] + [entry[0] for entry in SNAPSHOTS.values()]


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def inventory_digest(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_external(path):
    path = Path(path).resolve()
    if any(path == r.resolve() or r.resolve() in path.parents for r in ROOTS.values()):
        raise ValueError("Outputs must stay outside all protected trees")
    return path


def git(root, *args):
    return subprocess.check_output(
        ["git", "--no-optional-locks", "-C", str(root), *args], text=True).strip()


def capture(evidence, phase):
    evidence = safe_external(evidence)
    evidence.mkdir(parents=True, exist_ok=True)
    records, git_state = {}, {}
    for label, root in ROOTS.items():
        start = datetime.now(timezone.utc).isoformat()
        files = {}
        for p in sorted(root.rglob("*")):
            rel = p.relative_to(root)
            if p.is_file() and ".git" not in rel.parts:
                files[rel.as_posix()] = sha(p)
        records[label] = dict(root=str(root), start_utc=start,
                             end_utc=datetime.now(timezone.utc).isoformat(),
                             count=len(files), tree_sha256=inventory_digest(files), files=files)
        if label in ("current", "torment_checkout"):
            git_state[label] = dict(head=git(root, "rev-parse", "HEAD"),
                                   tracked_status=git(root, "status", "--porcelain", "--untracked-files=no"))
        print(label, len(files), records[label]["tree_sha256"], flush=True)
    (evidence / (phase + ".json")).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    (evidence / ("git_" + phase + ".json")).write_text(json.dumps(git_state, indent=2) + "\n", encoding="utf-8")


class Audit:
    def __init__(self):
        self.checks = {g: [] for g in GROUPS}
        self.details = {}

    def check(self, group, name, predicate, detail=None):
        row = dict(name=name, passed=bool(predicate))
        if detail is not None:
            row["detail"] = detail
        self.checks[group].append(row)
        if not row["passed"]:
            print("FAIL:", group, name, detail, flush=True)
        return row["passed"]

    def raises(self, name, kind, fn, group="PRECISION/FALSIFIER"):
        try:
            fn()
        except kind as exc:
            return self.check(group, name, True, type(exc).__name__ + ": " + str(exc))
        except Exception as exc:
            return self.check(group, name, False, "Unexpected " + repr(exc))
        return self.check(group, name, False, "No exception")

    def exact(self, group, name, expression):
        import sympy as s
        values = list(expression) if isinstance(expression, (s.MatrixBase, list, tuple)) else [expression]
        residues = [s.simplify(s.trigsimp(s.expand(v))) for v in values]
        return self.check(group, name, all(v == 0 for v in residues),
                          {"residuals": [str(v) for v in residues]})


def mathematical_checks(a):
    import sympy as s
    E, B, Y = "EXACT_ALGEBRA", "EXACT_BOUNDS", "EXACT_SYMMETRY"
    th, ell, z, lam, r, chi, m, b, alpha, beta = s.symbols(
        "theta ell z lambda r chi m b alpha beta", real=True)
    kap = s.symbols("kappa", nonnegative=True, finite=True)
    rho = kap / (1 + kap)
    a.check(B, "rho_nonnegative_and_strict_complement", rho.is_nonnegative and (1/(1+kap)).is_positive)
    a.exact(B, "one_minus_rho_positive_witness", 1-rho-1/(1+kap))
    a.exact(B, "rho_derivative_positive_witness", s.diff(rho, kap)-1/(1+kap)**2)
    a.exact(E, "rho_inverse", rho/(1-rho)-kap)
    a.check(B, "rho_zero_and_infinite_limit", rho.subs(kap, 0) == 0 and s.limit(rho, kap, s.oo) == 1)
    a.exact(E, "rho_asymptotic_gap", (1-rho)-1/(1+kap))
    amp = s.symbols("A", real=True)
    h = amp*s.cos(3*(th-ell))
    a.exact(Y, "harmonic_third_turn", h.subs(th, th+2*s.pi/3)-h)
    a.exact(B, "harmonic_squared_bound_witness", amp**2-h**2-amp**2*s.sin(3*(th-ell))**2)
    for k in range(6):
        a.exact(E, "harmonic_zero_" + str(k), h.subs(th, ell+s.pi/6+k*s.pi/3))
        a.exact(E, "harmonic_stationary_" + str(k), s.diff(h, th).subs(th, ell+k*s.pi/3))
        a.exact(E, "harmonic_extremum_value_" + str(k), h.subs(th, ell+k*s.pi/3)-(-1)**k*amp)
    sectors = [s.cos(3*ell), s.sin(3*ell), -s.cos(3*ell), -s.sin(3*ell)]*3
    a.exact(E, "twelve_sector_pattern", [s.cos(3*(q*s.pi/6-ell))-sectors[q] for q in range(12)])
    gamma, t = s.symbols("gamma t", real=True, finite=True)
    envelope = s.exp(-gamma*t)
    a.check(B, "finite_real_exponential_positive", envelope.is_positive)
    a.exact(E, "staged_t_zero", (h*envelope).subs(t, 0)-h)
    a.exact(E, "staged_gamma_zero", (h*envelope).subs(gamma, 0)-h)
    gp = s.symbols("gamma_positive", positive=True)
    a.check(B, "envelope_limits_by_gamma_sign", s.limit(s.exp(-gp*t), t, s.oo) == 0 and
            s.limit(s.exp(gp*t), t, s.oo) == s.oo)
    M = s.Matrix([z*s.cos(th), z*s.sin(th), z])
    a.exact(E, "macro_cone", M[0]**2+M[1]**2-M[2]**2)
    a.exact(E, "macro_norm_squared", M.dot(M)-2*z*z)
    a.exact(Y, "macro_scalar_reversal", M.subs(z, -z)+M)
    R = s.Matrix([[s.cos(chi), -s.sin(chi), 0], [s.sin(chi), s.cos(chi), 0], [0, 0, 1]])
    a.exact(Y, "macro_rotation_at_fixed_scalar", M.subs(th, th+chi)-R*M)
    Mf = M.subs(z, h)
    a.exact(Y, "staged_frozen_third_turn", Mf.subs(th, th+2*s.pi/3)-R.subs(chi, 2*s.pi/3)*Mf)
    a.exact(Y, "ema_frozen_third_turn", M.subs(z,h+m).subs(th,th+2*s.pi/3)-R.subs(chi,2*s.pi/3)*M.subs(z,h+m))
    x = s.Matrix(s.symbols("x1:4", real=True))
    y = s.Matrix(s.symbols("y1:4", real=True))
    w = x+s.I*y
    C = x.cross(y)
    P = s.expand(w[0]*s.conjugate(w[1])*w[2])
    K, J = s.re(P).expand(), s.im(P).expand()
    independent_J = x[0]*x[1]*y[2]+y[0]*y[1]*y[2]+y[0]*x[1]*x[2]-x[0]*y[1]*x[2]
    independent_K = x[0]*x[1]*x[2]+y[0]*y[1]*x[2]-y[0]*x[1]*y[2]+x[0]*y[1]*y[2]
    a.exact(E, "independent_cubic_real_expansion", K-independent_K)
    a.exact(E, "independent_cubic_imag_expansion", J-independent_J)
    subs = {v:r*v for v in list(x)+list(y)}
    a.exact(Y, "cubic_real_degree_three", J.subs(subs, simultaneous=True)-r**3*J)
    a.exact(Y, "cubic_conjugation", J.subs({v:-v for v in y}, simultaneous=True)+J)
    a.exact(Y, "cubic_global_sign", J.subs({v:-v for v in list(x)+list(y)}, simultaneous=True)+J)
    a.exact(Y, "chirality_real_degree_two", C.subs(subs, simultaneous=True)-r*r*C)
    a.exact(Y, "chirality_conjugation", C.subs({v:-v for v in y}, simultaneous=True)+C)
    xr, yr = x*s.cos(chi)-y*s.sin(chi), x*s.sin(chi)+y*s.cos(chi)
    a.exact(Y, "chirality_common_phase", xr.cross(yr)-C)
    kr, jr = s.symbols("K J", real=True)
    phase_product = (s.cos(chi)+s.I*s.sin(chi))*(kr+s.I*jr)
    a.exact(Y, "cubic_pair_common_phase", [s.re(phase_product)-(kr*s.cos(chi)-jr*s.sin(chi)),
                                          s.im(phase_product)-(kr*s.sin(chi)+jr*s.cos(chi))])
    # Each channel occurs once; exactly one is conjugated.
    a.exact(Y, "cubic_outer_channel_swap", s.im(s.expand(w[2]*s.conjugate(w[1])*w[0]))-J)
    permutation_values = {}
    ww = [1+4*s.I, 2+5*s.I, 3+6*s.I]
    for p in itertools.permutations(range(3)):
        Pi = s.zeros(3)
        for row,col in enumerate(p):
            Pi[row,col] = 1
        a.exact(Y, "chirality_permutation_"+"".join(str(k+1) for k in p),
                (Pi*x).cross(Pi*y)-Pi.det()*Pi*C)
        permutation_values["".join(str(k+1) for k in p)] = int(s.im(ww[p[0]]*s.conjugate(ww[p[1]])*ww[p[2]]))
    a.details["cubic_permutation_witness"] = permutation_values
    a.check(Y, "cubic_not_permutation_invariant", len(set(permutation_values.values())) > 1)
    u, v = s.Matrix(s.symbols("u1:4",real=True)), s.Matrix(s.symbols("v1:4",real=True))
    a.exact(E, "blend_joint_linearity", alpha*(M+u)+beta*(C+v)-(alpha*M+beta*C)-(alpha*u+beta*v))
    j = s.symbols("j", positive=True)
    jp = j/(1+j)
    a.exact(B, "normalized_cubic_strict_positive_branch_gap", 1-jp-1/(1+j))
    a.exact(E, "normalized_cubic_positive_inverse", jp/(1-jp)-j)
    a.exact(E, "normalized_cubic_negative_inverse", (-jp)/(1-jp)+j)
    a.check(B, "normalized_cubic_positive_branch", jp.is_positive and (1/(1+j)).is_positive)
    a.exact(Y, "normalized_cubic_odd_branches", -j/(1+j)+jp)
    aa, tau = s.Rational(99,100), s.Rational(1,100)
    update = aa*m+tau*b
    a.exact(E, "ema_increment_form", update-(m+tau*(b-m)))
    a.exact(B, "ema_upper_bound_slack", 1-update-(aa*(1-m)+tau*(1-b)))
    a.exact(B, "ema_lower_bound_slack", 1+update-(aa*(1+m)+tau*(1+b)))
    n = s.symbols("n", integer=True, nonnegative=True)
    closed = b+aa**n*(m-b)
    a.exact(E, "constant_innovation_closed_form_initial", closed.subs(n,0)-m)
    a.exact(E, "constant_innovation_closed_form_recurrence", closed.subs(n,n+1)-(aa*closed+tau*b))
    a.exact(E, "constant_innovation_fixed_point", update.subs(m,b)-b)
    a.exact(Y, "ema_joint_sign_covariance", update.subs({m:-m,b:-b}, simultaneous=True)+update)
    a.check(B, "forgetting_factor", 0 < aa < 1 and s.limit(aa**n,n,s.oo)==0)
    for endpoint in [-1,1]:
        a.exact(B, "endpoint_distance_"+str(endpoint), endpoint-update.subs(m,endpoint)-tau*(endpoint-b))
    a.exact(E, "ema_frozen_height_extrema", [(h+m).subs(th,ell)-m-amp,
                                            (h+m).subs(th,ell+s.pi/3)-m+amp])
    a.details["proof_scope"] = "Symbolic residuals/slack factorizations supplement the packet's quantified proofs; numerical samples do not prove universal bounds."


def runtime_checks(a):
    import numpy as np
    import mpmath as mp
    from kernel_physics import z_manifold as z, dynamics as d
    R, F = "RUNTIME/API", "PRECISION/FALSIFIER"
    w = np.array([1+4j,2+5j,3+6j])
    saved = w.tobytes()
    c, cfg, ecfg, mem = z.Clock(), z.StagedConfig(), z.EMAConfig(), z.EMAState(.25)
    out = z.observe_staged(w,c,cfg)
    eout = z.observe_ema(w,c,ecfg,mem)
    a.check(R, "six_real_hand_norm", z.state_norm(w)==math.sqrt(91))
    a.check(R, "hand_chirality", tuple(out.Z_chiral)==(-3.,6.,-3.))
    a.check(R, "hand_cubic", z.cubic_j(w)==141.)
    newc, newm = z.advance_clock(c,.125), z.advance_ema(w,mem)
    a.check(R, "all_operations_leave_omega_bytes", w.tobytes()==saved)
    a.check(R, "clock_memory_objects_unchanged", c==z.Clock() and mem.m==.25 and newc is not c and newm is not mem)
    a.check(R, "clock_not_an_omega_update", "omega" not in inspect.signature(z.advance_clock).parameters)
    a.check(R, "step3_has_no_dt_clock_memory_parameter", list(inspect.signature(d.step3).parameters)==["omega","config"])
    a.check(R, "ema_has_no_gamma_field", "gamma" not in [f.name for f in fields(z.EMAConfig)])
    a.check(R, "literal_defaults", (c.N,c.q_step,c.q,c.t,cfg.lambda_vp,cfg.gamma,cfg.theta_lock,cfg.alpha,cfg.beta)==
            (12,1,0,0.,.618,.577,.244,1.,.5))
    a.check(R, "signed_finite_configs_accepted", z.StagedConfig(-2,-3,-4,-5,-6).gamma==-3.)
    a.check(R, "huge_raw_q_integer_reduction", z.clock_angle(z.Clock(q=12*10**400+3))==math.pi/2)
    a.check(R, "raw_q_retained_but_angle_periodic", z.Clock(q=-1).q==-1 and
            z.clock_angle(z.Clock(q=-1))==z.clock_angle(z.Clock(q=11)))
    a.check(R, "negative_step_and_zero_dt", z.advance_clock(z.Clock(q=0,N=7,q_step=-2),0)==z.Clock(5,7,0,-2))
    a.check(R, "negative_dt_and_step_three", z.advance_clock(z.Clock(6,7,2,3),-.25)==z.Clock(2,7,1.75,3))
    for N,step in [(1,0),(12,0),(12,1),(12,4),(12,-8),(7,100)]:
        residues={(k*step)%N for k in range(N)}
        a.check(R, f"clock_orbit_N{N}_step{step}",len(residues)==N//math.gcd(N,step))
    a.check(R, "Z_vec_is_total_object", out.Z_vec is out.Z_total)
    a.check(R, "readout_arrays_detached_readonly", all(not v.flags.writeable and not np.shares_memory(v,w)
            for v in (out.Z_macro,out.Z_chiral,out.Z_total)))
    a.raises("readout_field_frozen",FrozenInstanceError,lambda:setattr(out,"z",3),R)
    a.raises("readout_array_ordinary_write_fails",ValueError,lambda:out.Z_total.__setitem__(0,3),R)
    supplied=np.array([1.,2.,3.])
    rec=z.ZReadout(0,supplied,supplied,supplied,"ema")
    supplied[0]=9
    a.check(R,"readout_copies_each_input",rec.Z_macro[0]==1 and not np.shares_memory(rec.Z_macro,rec.Z_total))
    a.check(F,"manual_readout_does_not_assert_formula_consistency",rec.z==0 and rec.Z_macro[2]==3)
    with patch.object(z,"advance_ema",side_effect=AssertionError), patch.object(z,"advance_clock",side_effect=AssertionError), patch.object(d,"step3",side_effect=AssertionError):
        pure=z.observe_ema(w,c,ecfg,mem)
        pure_k=z.observe_staged(w,c,cfg)
    a.check(R,"observers_call_no_advancement",pure.z==eout.z and pure_k.z==out.z)
    with patch.object(z,"advance_clock",side_effect=AssertionError), patch.object(d,"step3",side_effect=AssertionError):
        memory_only=z.advance_ema(w,mem)
    a.check(R,"memory_update_calls_no_clock_or_dynamics",memory_only.m==newm.m)
    with patch.object(z,"state_norm",side_effect=AssertionError), patch.object(z,"cubic_j",side_effect=AssertionError), patch.object(z.readouts,"z_chiral",side_effect=AssertionError):
        zero=z.historical_constructor_zero(w,c,cfg)
        zero_h=z.historical_constructor_zero(w,c,ecfg)
        hugezero=z.historical_constructor_zero([complex(sys.float_info.max,sys.float_info.max)]*3,c,cfg)
    a.check(R,"constructor_zero_no_scientific_evaluation",zero.readout.z==zero_h.readout.z==hugezero.readout.z==zero.memory.m==0.)
    a.check(R,"constructor_zero_marker_and_copy",zero.readout.initialization=="historical_constructor_zero" and
            not np.shares_memory(zero.omega,w) and not zero.omega.flags.writeable)
    a.check(F,"constructor_zero_differs_from_recomputed",out.z!=0 and not np.array_equal(out.Z_chiral,zero.readout.Z_chiral))
    a.check(F,"ema_observation_independent_of_t",z.observe_ema(w,z.Clock(t=1000),ecfg,mem).z==eout.z)
    a.check(F,"zero_omega_can_have_nonzero_ema_macro",z.observe_ema([0]*3,c,ecfg,z.EMAState(.5)).z==.5)
    late=z.observe_staged(w,z.Clock(t=10),cfg)
    a.check(F,"chiral_not_exponentially_enveloped",np.array_equal(late.Z_chiral,out.Z_chiral) and late.z!=out.z)
    real=np.ones(3,dtype=complex)
    a.check(F,"common_phase_changes_J_but_not_C",z.cubic_j(real)==0 and z.cubic_j(1j*real)==1 and
            np.array_equal(z.readouts.z_chiral(real),z.readouts.z_chiral(1j*real)))
    a.check(F,"J_zero_does_not_imply_C_zero",z.cubic_j([1,1j,0])==0 and tuple(z.readouts.z_chiral([1,1j,0]))==(0.,0.,1.))
    dc=d.DynamicsConfig(1,0,0,(1,1,1))
    changed=d.step3([2j]*3,dc)
    a.check(F,"J_not_generally_conserved_by_step3",tuple(changed)==(-4j,)*3 and z.cubic_j([2j]*3)==8 and z.cubic_j(changed)==-64)
    literal=z.advance_ema([1,1,1j],z.EMAState()).m
    alternate=(1.-.99)*.5
    a.check(F,"literal_point01_not_one_minus_float_point99",literal==.005 and literal.hex()!=alternate.hex(),
            dict(adopted_hex=literal.hex(),alternate_hex=alternate.hex()))
    a.check(F,"rho_can_round_to_one",z.saturated_norm([1e200,0,0])==1.)
    a.check(F,"jhat_can_round_to_both_endpoints",z.normalized_cubic([1e100j,1,1e100])==1 and
            z.normalized_cubic([-1e100j,1,1e100])==-1)
    a.check(F,"rounded_memory_endpoint_can_persist",z.advance_ema([1e100j,1,1e100],z.EMAState(1)).m==1)
    a.check(F,"angle_fraction_can_round_to_one",z.clock_angle(z.Clock(10**40-1,10**40))==2*math.pi)
    with mp.workdps(80):
        stable=z.state_norm([3e200,4e200,0])
        exact_binary_norm=mp.sqrt(mp.mpf(3e200)**2+mp.mpf(4e200)**2)
        norm_error=abs(mp.mpf(stable)-exact_binary_norm)
        a.check(R,"stable_hypot_avoids_naive_squaring",norm_error<=mp.mpf(math.ulp(stable)) and
                z.state_norm([1e-200,0,0])==1e-200,
                dict(actual=stable,exact_binary_input_norm=mp.nstr(exact_binary_norm,35),
                     absolute_error=mp.nstr(norm_error,20),bound_one_ulp=math.ulp(stable)))
    a.check(R,"zero_evaluation_exact",z.staged_scalar([0]*3,c,cfg)==0 and z.normalized_cubic([0]*3)==0)
    # This floating residual is not relabelled as an exact mathematical zero.
    trigzero=z.staged_scalar([1,0,0],z.Clock(1),z.StagedConfig(theta_lock=0,gamma=0))
    a.check(F,"ideal_trig_zero_can_be_nonzero_float",trigzero!=0,dict(binary64_value=trigzero,ideal_value="0"))
    pe=z.ResponsePrecisionError
    failure_cases=[
        ("exp_overflow",lambda:z.staged_scalar([1,0,0],z.Clock(t=-1000),z.StagedConfig(gamma=1))),
        ("exp_underflow_zero",lambda:z.staged_scalar([1,0,0],z.Clock(t=1000),z.StagedConfig(gamma=1))),
        ("exp_subnormal",lambda:z.staged_scalar([1,0,0],z.Clock(t=710),z.StagedConfig(gamma=1))),
        ("zero_amplitude_does_not_bypass_exp",lambda:z.staged_scalar([0]*3,z.Clock(t=1000),z.StagedConfig(gamma=1))),
        ("clock_lost_dt",lambda:z.advance_clock(z.Clock(t=1e300),1)),
        ("clock_t_overflow",lambda:z.advance_clock(z.Clock(t=sys.float_info.max),sys.float_info.max)),
        ("huge_N_fraction_underflow",lambda:z.clock_angle(z.Clock(1,10**400))),
        ("subnormal_state_norm",lambda:z.state_norm([1e-320,0,0])),
        ("finite_components_norm_overflow",lambda:z.state_norm([complex(sys.float_info.max,sys.float_info.max)]*3)),
        ("cubic_intermediate_overflow",lambda:z.cubic_j([1e200,1e200,1j])),
        ("cubic_product_underflow",lambda:z.cubic_j([1e-110,1e-110,1e-110j])),
        ("cubic_left_pair_fails_before_zero_third",lambda:z.cubic_j([.1,1e-310,0])),
        ("beta_zero_still_evaluates_C",lambda:z.observe_staged([1e200,1e200j,0],c,z.StagedConfig(beta=0))),
        ("alpha_zero_still_evaluates_macro_law",lambda:z.observe_staged([1,0,0],z.Clock(t=-1000),z.StagedConfig(gamma=1,alpha=0))),
        ("blend_intermediate_overflow_before_cancellation",lambda:z.blend_vectors([1e308,0,0],[1e308,0,0],alpha=2,beta=-2)),
        ("blend_nonzero_subnormal",lambda:z.blend_vectors([1e-200,0,0],[0]*3,alpha=1e-200,beta=0)),
    ]
    for name,fn in failure_cases:
        a.raises(name,pe,fn)
    for name,fn,kind in [
        ("clock_bool_rejected",lambda:z.Clock(q=True),TypeError),
        ("clock_noninteger_rejected",lambda:z.Clock(q=1.),TypeError),
        ("clock_nonpositive_N",lambda:z.Clock(N=0),ValueError),
        ("nonfinite_config",lambda:z.StagedConfig(gamma=float("inf")),ValueError),
        ("nonfinite_omega",lambda:z.state_norm([float("nan"),0,0]),ValueError),
        ("out_of_interval_memory",lambda:z.EMAState(1.1),ValueError),
        ("zero_weight_invalid_vector_still_rejected",lambda:z.blend_vectors([0]*3,[float("nan"),0,0],alpha=1,beta=0),ValueError),
        ("wrong_variant_config_rejected",lambda:z.observe_staged(w,c,ecfg),TypeError),
    ]:
        a.raises(name,kind,fn)
    large=np.array([1e110]*3,dtype=complex)
    a.check(F,"observe_ema_does_not_need_cubic_domain",math.isfinite(z.observe_ema(large,c,ecfg,z.EMAState()).z))
    a.raises("same_state_advance_ema_cubic_overflow",pe,lambda:z.advance_ema(large,z.EMAState()))
    a.check(R,"failures_leave_original_inputs",w.tobytes()==saved and mem.m==.25 and c==z.Clock())
    # Independent mpmath scalar reference from six real values, with exact binary inputs.
    receipts=[]
    fixtures=[([.3+.7j,-.4+.2j,.1-.8j],z.Clock(5,17,.7),z.StagedConfig()),
              ([2-.5j,-.3-1j,.7+.4j],z.Clock(-2,9,-.3),z.StagedConfig(lambda_vp=-.8,gamma=-.4,theta_lock=-.2))]
    with mp.workdps(80):
        for idx,(omega,clock,conf) in enumerate(fixtures):
            k=mp.sqrt(sum(mp.mpf(float(v.real))**2+mp.mpf(float(v.imag))**2 for v in omega))
            theta=2*mp.pi*(clock.q%clock.N)/clock.N
            expected=mp.mpf(conf.lambda_vp)*k/(1+k)*mp.cos(3*(theta-mp.mpf(conf.theta_lock)))*mp.exp(-mp.mpf(conf.gamma)*mp.mpf(clock.t))
            actual=z.staged_scalar(omega,clock,conf)
            error=abs(mp.mpf(actual)-expected)
            bound=max(mp.mpf(2e-14)*abs(expected),mp.mpf(2e-15))
            row=dict(fixture=idx,reference=mp.nstr(expected,45),actual=actual,
                     absolute_error=mp.nstr(error,20),allowed_bound=mp.nstr(bound,20),
                     rule="max(2e-14*abs(reference),2e-15); retained P9 fixture tolerance")
            a.check(R,"mp80_independent_scalar_"+str(idx),error<=bound,row)
            receipts.append(row)
    a.details["high_precision_receipts"]=receipts
    # Same recurrence with different caller-managed passive observer schedules.
    params=d.DynamicsConfig(.05,.2,.001,(1,1.2,1.4))
    starts=np.array([.2+.3j,-.4+.1j,.1-.2j])
    bare=starts.copy()
    observed=[starts.copy() for _ in range(3)]
    clocks=[z.Clock() for _ in range(3)]
    memory=z.EMAState()
    trajectories=True
    for _ in range(8):
        bare=d.step3(bare,params)
        for i,dt in enumerate([.1,.7,-.2]):
            observed[i]=d.step3(observed[i],params)
            clocks[i]=z.advance_clock(clocks[i],dt)
            if i<2:
                z.observe_staged(observed[i],clocks[i],cfg)
            else:
                memory=z.advance_ema(observed[i],memory)
                z.observe_ema(observed[i],clocks[i],ecfg,memory)
            trajectories &= bare.tobytes()==observed[i].tobytes()
    a.check(R,"different_observer_dt_preserves_recurrence_bytes",trajectories)
    tree=ast.parse((ROOT/"kernel_physics/z_manifold.py").read_text())
    imports=[ast.unparse(n) for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom))]
    a.check(R,"observer_direct_import_boundary",all(not any(k in line for k in
        ("dynamics","z_diagnostics","geometry","model_core","torment")) for line in imports),imports)
    code="import sys,json; sys.path.insert(0,"+repr(str(ROOT))+"); import kernel_physics.z_manifold; print(json.dumps(sorted(sys.modules)))"
    modules=json.loads(subprocess.check_output([sys.executable,"-B","-c",code],text=True))
    a.check(R,"fresh_process_observer_import_isolation",not any(n in modules for n in
        ("kernel_physics.dynamics","kernel_physics.z_diagnostics","kernel_physics.geometry","model_core")),
        [n for n in modules if n.startswith("kernel_physics")])
    a.details["no_physical_position_definition"]="Source contract and signatures define observer coordinates only; this is a semantic boundary, not a numerically testable physical theorem."


def historical_checks(a):
    import numpy as np
    from kernel_physics import z_manifold as z
    H="HISTORICAL_REPLAY"
    prov=json.loads((ROOT/"papers/PAPER_E/evidence/source_provenance.json").read_text())
    provenance={r["copy"]:r["sha256"] for r in prov["copies"]}
    traces={}
    for label,(relative,expected_sha) in SNAPSHOTS.items():
        path=ROOT/relative
        matched=sha(path)==expected_sha==provenance[relative.removeprefix("papers/PAPER_E/")]
        a.check(H,label+"_snapshot_sha256_and_provenance",matched,dict(path=str(path),sha256=sha(path)))
        if not matched:
            continue  # Never execute an unbound changed body.
        tree=ast.parse(path.read_text(encoding="utf-8-sig"))
        cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=="TriOctaPhaseLockModel")
        methods={n.name:n for n in cls.body if isinstance(n,ast.FunctionDef)}
        # Only this observer update executes. No class, module imports, old
        # recurrence, runner, cycle, identity, noise or optional subsystem runs.
        node=copy.deepcopy(methods["update_z"])
        node.returns=None
        for arg in list(node.args.args)+list(node.args.kwonlyargs):
            arg.annotation=None
        ns={"np":np}
        exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),str(path),"exec"),ns)
        update_z=ns["update_z"]
        step_source=ast.unparse(methods["step"])
        a.check(H,label+"_step_order_static",step_source.index("self.phase_lock_step") <
                step_source.index("self.advance_phi") < step_source.index("state.t += dt") <
                step_source.index("self.update_z"))
        run_source=ast.unparse(methods["run"])
        a.check(H,label+"_stored_readout_before_step_static",
                run_source.index("history['z'][i] = state.z") < run_source.index("self.step(state, dt=dt)"))
        phase_source=ast.unparse(methods["phase_lock_step"])
        a.check(H,label+"_omega_committed_by_phase_lock_step","state.Omega = Omega_next" in phase_source)
        state_cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=="ModelState")
        defs={n.target.id:n.value for n in state_cls.body if isinstance(n,ast.AnnAssign)}
        a.check(H,label+"_constructor_scalar_zero_literals",all(isinstance(defs[k],ast.Constant) and defs[k].value==0
                for k in ("z","z_mem","phi_index","t")))
        a.check(H,label+"_constructor_vector_zero_factories",all("np.zeros(3" in ast.unparse(defs[k])
                for k in ("Z_macro","Z_chiral","Z_vec")))
        a.check(H,label+"_dt_absent_from_omega_step","dt" not in {n.id for n in ast.walk(methods["phase_lock_step"]) if isinstance(n,ast.Name)})
        pars=SimpleNamespace(d24_steps=12,lambda_vp=.618,gamma=.577,theta_lock=.244,z_alpha=1.,z_beta=.5)
        model=SimpleNamespace(p=pars)
        omega=np.array([.375+.875j,-.5+.25j,.125-.75j])
        state=SimpleNamespace(Omega=omega.copy(),phi_index=0,t=0.,z=0.,z_mem=0.,
                              Z_macro=np.zeros(3),Z_chiral=np.zeros(3),Z_vec=np.zeros(3))
        state.kappa=lambda:float(np.linalg.norm(state.Omega))
        clock=z.Clock()
        memory=z.EMAState()
        rows=[]
        for n in range(1,7):
            # Bounded prescribed states, not an old integrated simulation.
            state.Omega=omega*(1+n/8)+np.array([.01j*n,-.02*n,.03j*n])
            clock=z.advance_clock(clock,.125)
            state.phi_index, state.t=clock.q,clock.t
            update_z(model,state)
            if label=="staged":
                out=z.observe_staged(state.Omega,clock,z.StagedConfig())
            else:
                memory=z.advance_ema(state.Omega,memory)
                out=z.observe_ema(state.Omega,clock,z.EMAConfig(),memory)
            actual=np.r_[out.z,out.Z_macro,out.Z_chiral,out.Z_total]
            old=np.r_[state.z,state.Z_macro,state.Z_chiral,state.Z_vec]
            # Fixed componentwise historical fixture tolerance, not universal.
            bounds=np.maximum(2e-14*np.abs(old),2e-15)
            error=np.abs(actual-old)
            a.check(H,f"{label}_bounded_observer_row_{n}",np.all(error<=bounds),
                    dict(max_absolute_error=float(max(error)),max_bound_fraction=float(max(error/bounds))))
            if label=="ema":
                a.check(H,f"ema_memory_row_{n}",abs(memory.m-state.z_mem)<=max(2e-14*abs(state.z_mem),2e-15))
            rows.append(dict(row=n,q=clock.q,t=clock.t,z=out.z,m=state.z_mem))
        traces[label]=rows
        if label=="ema":
            body=ast.unparse(methods["update_z"])
            a.check(H,"historical_H_memory_before_scalar",
                    body.index("state.z_mem =") < body.index("state.z ="))
            a.check(H,"historical_H_gamma_unused","gamma" not in {n.attr for n in ast.walk(methods["update_z"]) if isinstance(n,ast.Attribute)})
            # Changing committed input distinguishes a stale-state innovation.
            st=SimpleNamespace(Omega=np.ones(3)*1j,phi_index=1,t=.1,z_mem=0.,
                               Z_macro=np.zeros(3),Z_chiral=np.zeros(3),Z_vec=np.zeros(3))
            st.kappa=lambda:float(np.linalg.norm(st.Omega))
            update_z(model,st)
            a.check(H,"new_committed_omega_innovation_witness",st.z_mem==.005 and
                    z.advance_ema(np.ones(3),z.EMAState()).m==0.)
    a.details["historical_replay"]=dict(scope="Only hash-bound update_z bodies; six prescribed post-commit states per variant, plus one changed-innovation witness. Step/run/constructor inspected as AST only.",tolerance="componentwise max(2e-14*abs(snapshot_reference),2e-15)",rows=traces)


def integrity(a,evidence):
    missing=[name for name in ("before.json","after.json","git_before.json","git_after.json") if not (evidence/name).is_file()]
    if missing:
        a.details["integrity_pending"]=missing
        return False
    before=json.loads((evidence/"before.json").read_text())
    after=json.loads((evidence/"after.json").read_text())
    table={}
    for key in ROOTS:
        b,c=before[key],after[key]
        a.check("INTEGRITY",key+"_before_inventory_digest",inventory_digest(b["files"])==b["tree_sha256"] and len(b["files"])==b["count"])
        a.check("INTEGRITY",key+"_after_inventory_digest",inventory_digest(c["files"])==c["tree_sha256"] and len(c["files"])==c["count"])
        added=sorted(set(c["files"])-set(b["files"]))
        removed=sorted(set(b["files"])-set(c["files"]))
        changed=sorted(k for k in b["files"].keys() & c["files"].keys() if b["files"][k]!=c["files"][k])
        a.check("INTEGRITY",key+"_all_regular_file_bytes_unchanged",not added and not removed and not changed)
        table[key]={k:b[k] for k in ("root","count","tree_sha256","start_utc","end_utc")}
        table[key].update(after_count=c["count"],after_sha256=c["tree_sha256"],
                          after_start_utc=c["start_utc"],after_end_utc=c["end_utc"],
                          added=added,removed=removed,changed=changed)
    gb=json.loads((evidence/"git_before.json").read_text())
    ga=json.loads((evidence/"git_after.json").read_text())
    a.check("INTEGRITY","git_head_and_tracked_status_unchanged",gb==ga)
    a.check("INTEGRITY","current_head_matches_work_order",gb["current"]["head"]==ga["current"]["head"]==HEAD)
    a.check("INTEGRITY","source_hashes_match_before_after_manifests",all(
        before["current"]["files"][f]==after["current"]["files"][f]==sha(ROOT/f) for f in SOURCE_FILES))
    a.check("INTEGRITY","deliverables_external",all(safe_external(p)==p.resolve() for p in
        (Path(__file__),OUTPUT,HERE/"TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md")))
    a.details["integrity"]=dict(
        method="SHA256 each regular file except .git path components; inventory digest SHA256 sorted compact JSON mapping relative POSIX paths to file hashes; timestamps/ACLs/empty directories/git internals not claimed",
        trees=table,git_before=gb,git_after=ga,evidence_directory=str(evidence),
        evidence_sha256={n:sha(evidence/n) for n in ("before.json","after.json","git_before.json","git_after.json")},
        execution_actions={"commits":0,"pushes":0,"scope":"This Atlas-06 execution; action record, not inferred solely from filesystem hashes"})
    return True


def save(a):
    counts={g:dict(total=len(v),passed=sum(r["passed"] for r in v),
                   failed=sum(not r["passed"] for r in v)) for g,v in a.checks.items()}
    total=sum(c["total"] for c in counts.values())
    failed=sum(c["failed"] for c in counts.values())
    result=dict(atlas="06",version="0.1",created_utc=datetime.now(timezone.utc).isoformat(),
                authoritative_root=str(ROOT),required_head=HEAD,python=sys.version,
                python_executable=sys.executable,script_sha256=sha(__file__),
                status="PASS" if not failed and "integrity" in a.details else "INCOMPLETE" if not failed else "FAIL",
                total=total,passed=total-failed,failed=failed,group_counts=counts,
                source_sha256={f:sha(ROOT/f) for f in SOURCE_FILES},checks=a.checks,details=a.details)
    import sympy,numpy,mpmath
    result["library_versions"]=dict(sympy=sympy.__version__,numpy=numpy.__version__,mpmath=mpmath.__version__)
    if result["status"]=="PASS":
        result["required_flags"]=dict(CURRENT_REPO_CHANGED="NO",OLD_KERNEL_CHANGED="NO",TORMENT_CHANGED="NO",COMMITS=0,PUSHES=0)
    safe_external(OUTPUT).write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("status","total","passed","failed","group_counts")},indent=2),flush=True)
    return 1 if failed else 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir",type=Path,default=DEFAULT_EVIDENCE)
    parser.add_argument("--capture",choices=("before","after"))
    parser.add_argument("--finalize-integrity",action="store_true")
    args=parser.parse_args()
    safe_external(HERE)
    if args.capture:
        capture(args.evidence_dir,args.capture)
        return 0
    sys.path.insert(0,str(ROOT))
    a=Audit()
    if args.finalize_integrity:
        previous=json.loads(OUTPUT.read_text(encoding="utf-8"))
        # Refuse to relabel old checks after a source or checker change.
        if previous["script_sha256"]!=sha(__file__) or any(sha(ROOT/f)!=v for f,v in previous["source_sha256"].items()):
            raise RuntimeError("Checker or source changed: rerun the scientific checks first")
        a.checks=previous["checks"]
        a.checks["INTEGRITY"]=[]
        a.details=previous["details"]
        a.details.pop("integrity_pending",None)
    else:
        mathematical_checks(a)
        runtime_checks(a)
        historical_checks(a)
    integrity(a,args.evidence_dir)
    log=args.evidence_dir/"pytest.txt"
    if log.is_file():
        a.details["focused_repository_tests"]=dict(path=str(log),sha256=sha(log),output=log.read_text(encoding="utf-8-sig"),
            command="python -B -X utf8 -m pytest -q -p no:cacheprovider kernel_physics/tests/test_z_manifold.py kernel_physics/tests/test_runner_records.py -k 'not diagnostic'",
            environment="conda torment; PYTHONDONTWRITEBYTECODE=1; PYTEST_DISABLE_PLUGIN_AUTOLOAD=1")
    return save(a)


if __name__=="__main__":
    raise SystemExit(main())
