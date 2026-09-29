"""Read-only Atlas-07 algebra, API, display and ownership audit.

No historical/production module execution. No source writes. An explicit new
--output file outside protected trees is required; existing files are refused.
The checker can reside in a repository: all output/scratch locations are
explicit and independent of __file__. Use Python -B (conda torment).
Optional --integrity-dir and --test-receipt are documentary evidence inputs,
separate from scientific checks. Their absence is reported, not invented.
"""
from __future__ import annotations
import argparse
import ast
from contextlib import ExitStack
from dataclasses import fields, FrozenInstanceError
from datetime import datetime, timezone
import hashlib
import inspect
import json
import math
import os
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
BASE = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
EXPECTED_HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
PROTECTED = [BASE, Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO"),
             Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric")]
GROUPS = ("EXACT_ALGEBRA", "EXACT_BOUNDS", "EXACT_FALSIFIER", "API/PRECISION",
          "DISPLAY/INFORMATION_LOSS", "OWNERSHIP", "INTEGRITY")
SOURCES = {
    "DIAG": "kernel_physics/z_diagnostics.py",
    "TEST": "kernel_physics/tests/test_z_diagnostics.py",
    "E": "papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md",
    "Z": "kernel_physics/z_manifold.py",
    "C": "kernel_physics/readouts.py",
    "D": "kernel_physics/dynamics.py",
    "NUM": "kernel_physics/_response_numeric.py",
    "RUN": "kernel_physics/_runner.py",
    "RECORDS": "kernel_physics/_records.py",
    "RUN_TEST": "kernel_physics/tests/test_runner_records.py",
    "P9_P10": "kernel_physics/tests/test_parity_p09_p10.py",
    "ORACLE": "kernel_physics/tests/parity_oracles/paper_e_oracle.py",
    "SYMBOLIC": "papers/PAPER_E/check_symbolic.py",
    "SYMBOLIC_RECEIPT": "papers/PAPER_E/evidence/symbolic_results.json",
    "E_REVISION": "papers/PAPER_E/v0.1.1/check_revision.py",
    "D_POTENTIAL": "papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md",
    "A04": "research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md",
    "A01": "research/mathematical_atlas/entry_01_complex_triad/TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md",
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def external(path, repo):
    p = Path(path).resolve()
    for r in [*PROTECTED, repo]:
        r = r.resolve()
        if p == r or r in p.parents:
            raise ValueError("Output/scratch must be outside protected source trees: " + str(p))
    return p


def discover_repo():
    for parent in Path(__file__).resolve().parents:
        if (parent / "kernel_physics/z_diagnostics.py").is_file():
            return parent
    return BASE


class Audit:
    def __init__(self):
        self.groups = {g: [] for g in GROUPS}
        self.details = {}

    def check(self, group, name, condition, evidence=None):
        row = {"name": name, "passed": bool(condition)}
        if evidence is not None:
            row["evidence"] = evidence
        self.groups[group].append(row)
        if not row["passed"]:
            print("FAIL", group, name, evidence, flush=True)
        return row["passed"]

    def exact(self, group, name, expression):
        import sympy as s
        items = list(expression) if isinstance(expression, (list, tuple, s.MatrixBase)) else [expression]
        residuals = [s.simplify(s.trigsimp(s.expand(x))) for x in items]
        return self.check(group, name, all(x == 0 for x in residuals),
                          {"exact_residuals": list(map(str, residuals))})

    def raises(self, group, name, exception, call):
        try:
            call()
        except exception as error:
            return self.check(group, name, True, type(error).__name__ + ": " + str(error))
        except Exception as error:
            return self.check(group, name, False, "Unexpected " + repr(error))
        return self.check(group, name, False, "No exception")

    def bounded(self, group, name, actual, expected, scale, factor=256):
        import mpmath as mp
        import sympy as s
        with mp.workdps(90):
            def number(x):
                x = s.sympify(x)
                return mp.mpc(mp.mpf(str(s.N(s.re(x), 95))), mp.mpf(str(s.N(s.im(x), 95))))
            reference = number(expected)
            actual_mp = mp.mpc(complex(actual))
            scale_mp = number(scale).real
            bound = factor * mp.mpf(2)**-52 * scale_mp
            error = abs(actual_mp-reference)
            return self.check(group, name, scale_mp >= 0 and error <= bound, dict(
                actual=str(actual), reference=mp.nstr(reference, 35),
                absolute_error=mp.nstr(error, 22), scale=mp.nstr(scale_mp, 22),
                factor=factor, epsilon="2^-52", allowed_bound=mp.nstr(bound, 22),
                scope="Bounded fixture tolerance, no universal forward-error theorem"))


def exact_checks(a):
    import sympy as s
    A, B, F = "EXACT_ALGEBRA", "EXACT_BOUNDS", "EXACT_FALSIFIER"
    x, y = s.Matrix(s.symbols("x1:4", real=True)), s.Matrix(s.symbols("y1:4", real=True))
    alpha, beta = s.symbols("alpha beta", real=True)
    G = s.diag(1,1,-1)
    blend = alpha*x+beta*y
    a.exact(A, "full_euclidean_blend", blend.dot(blend)-alpha**2*x.dot(x)-beta**2*y.dot(y)-2*alpha*beta*x.dot(y))
    a.exact(A, "full_signed_Q_blend_including_QM", (blend.T*G*blend)[0]-alpha**2*(x.T*G*x)[0]-beta**2*(y.T*G*y)[0]-2*alpha*beta*(x.T*G*y)[0])
    z, theta = s.symbols("z theta", real=True)
    macro = s.Matrix([z*s.cos(theta), z*s.sin(theta), z])
    a.exact(A, "macro_law_implies_Q_zero", (macro.T*G*macro)[0])
    a.exact(A, "macro_law_implies_norm_relation", macro.dot(macro)-2*z**2)
    a.exact(F, "omitting_nonzero_QM_is_wrong", (2*s.Matrix([1,2,3])).dot(G*(2*s.Matrix([1,2,3])))+16)
    u, v = s.symbols("u v", nonnegative=True)
    cosine = s.symbols("cosine", real=True)
    weighted_norm2 = u*u+v*v+2*u*v*cosine
    a.exact(B, "triangle_bound_slack", (u+v)**2-weighted_norm2-2*u*v*(1-cosine))
    a.exact(B, "reverse_triangle_bound_slack", weighted_norm2-(u-v)**2-2*u*v*(1+cosine))
    a.details["triangle_bound_hypotheses"] = "u=|alpha| ||M||, v=|beta| ||C||; cosine between weighted nonzero vectors lies in [-1,1]; zero vectors by continuity."
    c = x.cross(y)
    aa, bb, hh = x.dot(x), y.dot(y), x.dot(y)
    intensity = aa+bb
    a.exact(A, "gram_determinant", c.dot(c)-aa*bb+hh**2)
    a.exact(B, "sharp_chiral_slack_SOS", intensity**2/4-c.dot(c)-(aa-bb)**2/4-hh**2)
    r = s.symbols("r", real=True)
    a.exact(A, "raw_chiral_scaling", (r*x).cross(r*y)-r*r*c)
    # Both squared residuals vanish iff A=B and h=0; give zero/nonzero witnesses.
    for scale in [s.Integer(0),s.Integer(1),s.Rational(7,3)]:
        xx, yy = s.Matrix([scale,0,0]), s.Matrix([0,scale,0])
        a.exact(B, "sharp_equality_scale_"+str(scale), xx.cross(yy).dot(xx.cross(yy))-(xx.dot(xx)+yy.dot(yy))**2/4)
    norm = s.sqrt(x.dot(x))
    unit = x/norm
    a.exact(A, "normalization_derivative_off_zero", unit.jacobian(x)-(s.eye(3)-unit*unit.T)/norm)
    eta=s.symbols("eta",positive=True)
    a.exact(F,"opposite_directions_small_displacement",s.sqrt((2*eta)**2)-2*eta)
    a.details["direction_falsifier"]="T+=eta e2, T-=-eta e2: displacement=2eta ->0, unit-direction separation=2."
    eps,g=s.symbols("eps g",real=True)
    k=s.symbols("k1:4",real=True)
    L=s.ones(3)-3*s.eye(3)
    w=x+s.I*y
    si=[x[i]**2+y[i]**2 for i in range(3)]
    pairs=sum((x[i]-x[j])**2+(y[i]-y[j])**2 for i,j in ((0,1),(0,2),(1,2)))
    herm=(s.conjugate(w).T*L*w)[0]
    a.exact(A,"hermitian_graph_equals_minus_P",herm+pairs)
    dx=s.Matrix([eps*(k[i]-si[i])*x[i] for i in range(3)])+g*L*x
    dy=s.Matrix([eps*(k[i]-si[i])*y[i] for i in range(3)])+g*L*y
    after=sum((x[i]+dx[i])**2+(y[i]+dy[i])**2 for i in range(3))
    onsite=2*eps*sum(k[i]*si[i]-si[i]**2 for i in range(3))
    remainder=dx.dot(dx)+dy.dot(dy)
    a.exact(A,"full_finite_intensity_budget",after-sum(si)-onsite+2*g*pairs-remainder)
    nonlinear=s.Matrix([(k[i]-si[i])*w[i] for i in range(3)])
    graph=L*w
    cross=s.re((s.conjugate(nonlinear).T*graph)[0]).expand()
    a.exact(A,"remainder_full_cross_terms",remainder-eps**2*sum(si[i]*(k[i]-si[i])**2 for i in range(3))
            -g**2*((L*x).dot(L*x)+(L*y).dot(L*y))-2*eps*g*cross)
    potential=eps*sum(si[i]**2/4-k[i]*si[i]/2 for i in range(3))+g*pairs/2
    for i,(coord,inc) in enumerate(zip(list(x)+list(y),list(dx)+list(dy))):
        a.exact(A,"negative_real_gradient_"+str(i),s.diff(potential,coord)+inc)
    completed=eps*sum((si[i]-k[i])**2 for i in range(3))/4+g*pairs/2
    a.exact(A,"completed_square_parameter_constant",completed-potential-eps*sum(ki**2 for ki in k)/4)
    a.details["potential_constant_scope"]="Algebraic completed-square comparison; no distinct completed-square formula was located in the preserved Atlas 01-06 packets. Paper D (35) and Paper E (37) use the same expanded normalization."
    a.check(F,"exact_overshoot",(-6,12,48,-72,0,108,36,6,168)==
            (2*(1-4),3*4,3*16,2*3*(4-16),0,3*36,48-12,3*(16//4-4//2),3*(256//4-16//2)))
    a.details["overshoot"]=dict(omega=[2,2,2],eps=1,g=0,k=[1,1,1],phase_strength=0,
        D=[-6,-6,-6],pre_sync=[-4,-4,-4],I_before=12,I_after=48,onsite=-72,coupling=0,remainder=108,delta_I=36,V_before=6,V_after=168)
    a.exact(F,"pure_coupling_growth_polynomial",((1-3*g)**2-1)*2-6*g*(3*g-2))
    # Exact adopted phase operation, independently evaluated at a simple state.
    phases=[0,s.pi/6,0]
    newph=[phases[i]+s.pi/6*sum(s.sin(3*(phases[j]-phases[i])) for j in range(3) if i!=j) for i in range(3)]
    a.exact(A,"phase_witness_updated_angles",[newph[0]-s.pi/6,newph[1]+s.pi/6,newph[2]-s.pi/6])
    pair=lambda ph:sum(2-2*s.cos(ph[i]-ph[j]) for i,j in ((0,1),(0,2),(1,2)))
    a.exact(A,"phase_witness_pair_before",pair(phases)-(4-2*s.sqrt(3)))
    a.exact(A,"phase_witness_pair_after",pair(newph)-2)
    a.check(F,"phase_stage_can_increase_graph_potential", (s.sqrt(3)-1).is_positive)
    a.details["phase_witness"]="Unit magnitudes; phases (0,pi/6,0), strength pi/6 -> (pi/6,-pi/6,pi/6). P:4-2sqrt(3)->2; Delta potential=g(sqrt(3)-1)>0 for g>0."
    kap=s.symbols("kappa",nonnegative=True,finite=True)
    rm,reg=s.symbols("rmax regularizer",positive=True)
    zmax=s.symbols("zmax",nonnegative=True,finite=True)
    rr=rm*kap/(1+kap)
    a.exact(B,"torus_radius_strict_gap",rm-rr-rm/(1+kap))
    a.check(B,"torus_radius_gap_positive",(rm/(1+kap)).is_positive)
    a.exact(B,"torus_angular_strict_gap",s.pi/2-s.pi*zmax/(2*(zmax+reg))-s.pi*reg/(2*(zmax+reg)))
    a.check(B,"torus_angle_gap_positive",(s.pi*reg/(2*(zmax+reg))).is_positive)
    R,chi,rad=s.symbols("R chi radius",real=True)
    major=R+rad*s.cos(chi)
    coords=s.Matrix([major*s.cos(theta),major*s.sin(theta),rad*s.sin(chi)])
    a.exact(A,"torus_horizontal_radius_squared",coords[0]**2+coords[1]**2-major**2)
    a.exact(A,"torus_meridional_radius_squared",(major-R)**2+coords[2]**2-rad**2)
    a.exact(A,"torus_inverse_kappa_identity",rr/(rm-rr)-kap)
    H=s.symbols("Hz",positive=True)
    a.exact(A,"torus_inverse_height_identity",2*H*(s.pi*z/(2*H))/s.pi-z)
    a.exact(A,"inverse_radial_derivative",s.diff(rad/(rm-rad),rad)-rm/(rm-rad)**2)
    a.exact(F,"torus_zero_kappa_keeps_major_angle",coords.subs(rad,0)-s.Matrix([R*s.cos(theta),R*s.sin(theta),0]))
    a.exact(F,"cylinder_zero_kappa_keeps_height",s.Matrix([kap*s.cos(theta),kap*s.sin(theta),z]).subs(kap,0)-s.Matrix([0,0,z]))
    wa=s.Matrix([1,1,1]); wb=s.Matrix([1,s.I,1])
    ca=s.re(wa).cross(s.im(wa)); cb=s.re(wb).cross(s.im(wb))
    a.exact(F,"common_state_same_intensity",sum(s.expand_complex(q*s.conjugate(q)) for q in wa)-sum(s.expand_complex(q*s.conjugate(q)) for q in wb))
    a.exact(F,"common_state_different_C",cb-ca-s.Matrix([-1,0,1]))


def api_checks(a,root):
    import numpy as np
    import sympy as s
    from kernel_physics import z_diagnostics as d, z_manifold as z, dynamics
    from kernel_physics._response_numeric import ResponsePrecisionError as PE
    A,DIS,OWN="API/PRECISION","DISPLAY/INFORMATION_LOSS","OWNERSHIP"
    a.details["module_inventory"]={
        "functions":{name:str(inspect.signature(obj)) for name,obj in vars(d).items()
                     if inspect.isfunction(obj) and not name.startswith("_") and obj.__module__==d.__name__},
        "records":{name:[f.name for f in fields(getattr(d,name))] for name in
                   ("ReadoutAccounting","ChiralAreaAccounting","HistoricalAlignment","IntensityBudget","Coordinates","HistoryTorus")}}
    def q(v): return sum(sign*x*x for sign,x in zip((1,1,-1),v))
    def dot(v,w): return sum(x*y for x,y in zip(v,w))
    def norm2(v): return dot(v,v)
    # Derive every accounting field independently from supplied rational data.
    fixtures=[
        ("signed",s.Rational(3,4),[s.Rational(1,2),s.Rational(-1,4),s.Rational(3,4)],[-1,s.Rational(1,8),s.Rational(1,2)],[s.Rational(5,4),s.Rational(-17,32),s.Rational(11,8)],2,s.Rational(-1,4)),
        ("inconsistent",s.Integer(1),[1,2,3],[0,1,0],[8,0,1],1,1),
        ("scalar_residual_blindness",s.Integer(1),[1,0,1],[0,0,0],[-1,0,-1],1,0),
        ("all_residuals_blind_to_Mz",s.Integer(1),[1,0,-1],[0,0,0],[1,0,-1],1,0),
    ]
    for label,zs,m,c,t,al,be in fixtures:
        weighted_m=al**2*norm2(m); weighted_c=be**2*norm2(c); cross=2*al*be*dot(m,c)
        prediction=weighted_m+weighted_c+cross
        qcross=2*al*be*sum(sign*x*y for sign,x,y in zip((1,1,-1),m,c))
        qp=al**2*q(m)+be**2*q(c)+qcross
        expected=dict(alpha=al,beta=be,supplied_z=zs,macro_norm_squared=norm2(m),chiral_norm_squared=norm2(c),
            total_norm_squared=norm2(t),weighted_macro=weighted_m,weighted_chiral=weighted_c,cross_term=cross,
            predicted_norm_squared=prediction,norm_residual=norm2(t)-prediction,
            q_macro=q(m),q_chiral=q(c),q_total=q(t),q_weighted_macro=al**2*q(m),q_weighted_chiral=be**2*q(c),
            q_cross_term=qcross,q_prediction=qp,q_residual=q(t)-qp,macro_relation_residual=norm2(m)-2*zs**2)
        expected_blend=[t[i]-al*m[i]-be*c[i] for i in range(3)]
        readout=z.ZReadout(float(zs),list(map(float,m)),list(map(float,c)),list(map(float,t)),"staged")
        receipt=d.readout_accounting(readout,alpha=float(al),beta=float(be))
        a.check(A,label+"_all_accounting_fields",all(s.Rational(getattr(receipt,n))==value for n,value in expected.items()) and
                list(map(s.Rational,receipt.blend_residual))==expected_blend and receipt.variant=="staged" and receipt.initialization=="recomputed",
                {n:str(value) for n,value in expected.items()})
    observed=z.observe_ema([1,-1j,-1],z.Clock(),z.EMAConfig(lambda_vp=0,alpha=1,beta=-1),z.EMAState(-1))
    a.check(A,"attainable_pointwise_cancellation",np.array_equal(observed.Z_macro,observed.Z_chiral) and
            np.any(observed.Z_macro) and np.array_equal(observed.Z_total,[0]*3))
    # Gram fields from an independent exact state.
    w=np.array([.375+.875j,-.5+.25j,.125-.75j])
    x=[s.Rational(v.real) for v in w]; y=[s.Rational(v.imag) for v in w]
    c=s.Matrix(x).cross(s.Matrix(y)); aa,bb,hh=norm2(x),norm2(y),dot(x,y); ii=aa+bb; c2=c.dot(c)
    ref=dict(A=aa,B=bb,h=hh,intensity=ii,chiral_norm_squared=c2,gram_product=aa*bb,h_squared=hh**2,
             gram_rhs=aa*bb-hh**2,gram_residual=0,amplitude_bound=ii/2,
             slack_sum_of_squares=(aa-bb)**2/4+hh**2,observed_slack=ii**2/4-c2,slack_residual=0)
    area=d.chiral_area_accounting(w)
    a.check(A,"all_gram_polynomial_fields",all(s.Rational(getattr(area,k))==v for k,v in ref.items()) and
            list(map(s.Rational,area.chiral))==list(c))
    a.bounded(A,"chiral_norm_square_root",area.chiral_norm,s.sqrt(c2),s.sqrt(c2),96)
    near=d.chiral_area_accounting([1+1j,1+1j,1+(1+2**-26)*1j])
    a.check(A,"gram_residual_unclamped",near.gram_residual!=0,
            dict(gram_rhs=near.gram_rhs,gram_residual=near.gram_residual,observed_slack=near.observed_slack))
    # Derive a signed-parameter budget before asking the implementation.
    eps,g=s.Rational(-1,16),s.Rational(-1,8); kk=[s.Rational(-1),s.Rational(5,4),s.Rational(1,2)]
    exact_w=s.Matrix([x[i]+s.I*y[i] for i in range(3)])
    si=[x[i]**2+y[i]**2 for i in range(3)]
    pair=sum(s.expand_complex((exact_w[i]-exact_w[j])*s.conjugate(exact_w[i]-exact_w[j])) for i,j in ((0,1),(0,2),(1,2)))
    inc=[s.expand(eps*(kk[i]-si[i])*exact_w[i]+g*sum(exact_w[j]-exact_w[i] for j in range(3) if j!=i)) for i in range(3)]
    pre=[s.expand(exact_w[i]+inc[i]) for i in range(3)]
    abs2=lambda value:s.expand_complex(value*s.conjugate(value))
    before=sum(si); after=sum(map(abs2,pre))
    onsite=2*eps*sum(kk[i]*si[i]-si[i]**2 for i in range(3)); coupling=-2*g*pair; remainder=sum(map(abs2,inc))
    pot=eps*sum(si[i]**2/4-kk[i]*si[i]/2 for i in range(3))+g*pair/2
    cfg=dynamics.DynamicsConfig(float(eps),float(g),.125,tuple(map(float,kk)))
    budget=d.intensity_budget(w,cfg)
    values=dict(intensity_before=before,intensity_pre_sync=after,pair_distance_sum=pair,onsite=onsite,
                coupling=coupling,remainder=remainder,predicted_delta=onsite+coupling+remainder,observed_delta=after-before,residual=0)
    a.check(A,"all_signed_budget_scalar_fields",all(s.Rational(getattr(budget,k))==v for k,v in values.items()))
    for name,expected in (("component_intensities",si),("increment",inc),("diagnostic_pre_sync_prediction",pre)):
        actual=getattr(budget,name)
        a.check(A,"budget_"+name,all(s.Rational(complex(v).real)+s.I*s.Rational(complex(v).imag)==want for v,want in zip(actual,expected)))
    a.check(A,"potential_exact_dyadic",s.Rational(d.potential(w,cfg))==pot)
    overcfg=dynamics.DynamicsConfig(1,0,0,(1,1,1))
    over=d.intensity_budget([2]*3,overcfg)
    a.check(A,"requested_overshoot_g_zero",tuple(over.increment)==(-6,)*3 and tuple(over.diagnostic_pre_sync_prediction)==(-4,)*3 and
            (over.onsite,over.coupling,over.remainder,over.intensity_before,over.intensity_pre_sync,over.residual)==(-72,0,108,12,48,0) and
            d.potential([2]*3,overcfg)==6 and d.potential([-4]*3,overcfg)==168)
    for length,flag in ((math.nextafter(1e-12,0),False),(1e-12,True),(math.nextafter(1e-12,1),True)):
        alignment=d.historical_alignment([length,0,0],[1,0,0],[1,0,0])
        a.check(A,"threshold_"+repr(length),(alignment.macro_resolved,alignment.TM_resolved,alignment.CM_resolved,
                alignment.chiral_resolved,alignment.total_resolved,alignment.TC_resolved)==(flag,flag,flag,True,True,True) and
                (alignment.d_TM,alignment.d_CM,alignment.d_TC)==(float(flag),float(flag),1.) and alignment.threshold==1e-12)
    tiny=d.historical_alignment([1e-13,0,0],[1,0,0],[1,0,0])
    orth=d.historical_alignment([0,1,0],[1,0,0],[1,0,0])
    a.check(A,"unresolved_parallel_is_not_orthogonality",tiny.d_TM==orth.d_TM==0 and not tiny.TM_resolved and orth.TM_resolved)
    # No recurrence is called inside a diagnostic; compare once against canonical output separately.
    basecfg=dynamics.DynamicsConfig(.05,.2,0,(1,1.2,1.4))
    syncfg=dynamics.DynamicsConfig(.05,.2,.2,(1,1.2,1.4))
    w0=np.array([.2+.3j,-.4+.1j,.1-.2j])
    pre0=dynamics.step3(w0,basecfg); post0=dynamics.step3(w0,syncfg)
    for i in range(3):
        a.bounded(A,"phase_magnitude_"+str(i),abs(post0[i])**2,abs(pre0[i])**2,abs(pre0[i])**2+abs(post0[i])**2,96)
    a.check(A,"phase_can_change_potential",abs(d.potential(pre0,basecfg)-d.potential(post0,syncfg))>1e-5)
    later0=dynamics.step3(pre0,basecfg); later1=dynamics.step3(post0,basecfg)
    a.check(A,"phase_can_affect_later_magnitudes",not np.allclose(abs(later0),abs(later1),rtol=1e-12,atol=0))
    a.details["phase_runtime"]=dict(potential_without_sync=d.potential(pre0,basecfg),potential_with_sync=d.potential(post0,syncfg))
    # Display domains and exact information distinctions.
    xyz=lambda o:np.column_stack((o.x,o.y,o.z))
    hist=lambda k,q,zs:dict(kappa=np.asarray(k),phi_index=np.asarray(q,dtype=object),z=np.asarray(zs))
    arr=np.arange(6.).reshape(2,3)
    direct=d.direct_history_coordinates({"Z_total":arr,"Z_vec":np.ones((2,3))})
    a.check(DIS,"direct_default_and_fallback",np.array_equal(xyz(direct),arr) and
            np.array_equal(xyz(d.direct_history_coordinates({"Z_vec":arr})),arr))
    a.check(DIS,"direct_explicit_key",np.array_equal(xyz(d.direct_history_coordinates({"custom":arr},"custom")),arr))
    a.check(DIS,"direct_empty_shaped_history",xyz(d.direct_history_coordinates({"Z_total":np.empty((0,3))})).shape==(0,3))
    a.raises(DIS,"malformed_present_does_not_fallback",ValueError,lambda:d.direct_history_coordinates({"Z_total":[1,2],"Z_vec":arr}))
    a.raises(DIS,"explicit_missing_key_no_fallback",KeyError,lambda:d.direct_history_coordinates({"Z_vec":arr},"other"))
    a.raises(DIS,"bare_empty_direct_list_wrong_shape",ValueError,lambda:d.direct_history_coordinates({"Z_total":[]}))
    cyl=d.cylinder_point(0,7,-3)
    a.check(DIS,"cylinder_zero_kappa_retains_height",tuple(cyl)==(0.,0.,-3.))
    a.check(DIS,"cylinder_empty_allowed",xyz(d.cylinder_history_coordinates(hist([],[],[]))).shape==(0,3))
    for qv,n in ((4,7),(-3,7),(10**100+2,7)):
        expected=[2*s.cos(2*s.pi*(qv%n)/n),2*s.sin(2*s.pi*(qv%n)/n),s.Rational(-2,5)]
        actual=d.cylinder_point(2,qv,-.4,N=n)
        for j in range(3):
            a.bounded(DIS,f"cylinder_custom_N_{qv}_axis{j}",actual[j],expected[j],2 if j<2 else s.Rational(2,5),128)
    h=hist([.5,1,2],[1,3,8],[.1,-.2,.8])
    torus=d.history_torus_coordinates(h,R=3,r_max=.8)
    a.check(DIS,"torus_metadata",(torus.z_max,torus.H_z,torus.regularizer,torus.R,torus.r_max,torus.N,torus.normalization)==
            (.8,.8+1e-9,1e-9,3.,.8,12,"entire_supplied_history"))
    # Independent ideal map uses exact binary inputs, including the literal regularizer.
    ideal_H=max(s.Rational(float(value)) if value>=0 else -s.Rational(float(value)) for value in h["z"])+s.Rational(1e-9)
    for i,(kv,qv,zv) in enumerate(zip(h["kappa"],h["phi_index"],h["z"])):
        rr=s.Rational(.8)*s.Rational(float(kv))/(1+s.Rational(float(kv)))
        chi=s.pi*s.Rational(float(zv))/(2*ideal_H)
        theta=2*s.pi*(qv%12)/12
        reference=[(3+rr*s.cos(chi))*s.cos(theta),(3+rr*s.cos(chi))*s.sin(theta),rr*s.sin(chi)]
        for j in range(3):
            a.bounded(DIS,f"mp90_torus_row{i}_axis{j}",xyz(torus)[i,j],reference[j],3+rr if j<2 else rr,256)
        X,Y,Z=xyz(torus)[i]
        u=math.hypot(X,Y)-torus.R; recovered_r=math.hypot(u,Z)
        recovered_k=recovered_r/(torus.r_max-recovered_r)
        recovered_z=2*torus.H_z*math.atan2(Z,u)/math.pi
        a.bounded(DIS,f"conditional_inverse_kappa_{i}",recovered_k,float(kv),2*float(kv),256)
        a.bounded(DIS,f"conditional_inverse_z_{i}",recovered_z,float(zv),2*abs(float(zv)),256)
    zero_h=hist([0,0],[0,3],[-3,4])
    tzero=d.history_torus_coordinates(zero_h)
    a.check(DIS,"torus_zero_kappa_loses_z_in_XYZ",tzero.z.tolist()==[0.,0.] and tzero.r.tolist()==[0.,0.])
    a.check(DIS,"torus_zero_kappa_retains_angle",not np.array_equal(xyz(tzero)[0],xyz(tzero)[1]))
    a.check(DIS,"full_torus_record_keeps_chi",tzero.chi[0]<0<tzero.chi[1] and tzero.H_z==4+1e-9)
    allzero=d.history_torus_coordinates(hist([0,1],[0,1],[0,0]))
    a.check(DIS,"regularizer_all_zero_history",allzero.H_z==1e-9 and np.array_equal(allzero.chi,[0,0]))
    short=hist([1],[1],[.2]); longer=hist([1,1],[1,2],[.2,2])
    first=d.history_torus_coordinates(short); extended=d.history_torus_coordinates(longer)
    a.check(DIS,"future_excursion_changes_earlier_display",first.H_z!=extended.H_z and
            not np.array_equal(xyz(first)[0],xyz(extended)[0]) and all(short[k][0]==longer[k][0] for k in short))
    a.details["history_dependence"]=dict(before_xyz=xyz(first)[0].tolist(),after_xyz=xyz(extended)[0].tolist(),
        before_H=first.H_z,after_H=extended.H_z,earlier_input=dict(kappa=1,q=1,z=.2))
    oa=z.observe_staged([1,1,1],z.Clock(q=2,t=.3),z.StagedConfig())
    ob=z.observe_staged([1,1j,1],z.Clock(q=2,t=.3),z.StagedConfig())
    ha=hist([math.sqrt(3)],[2],[oa.z]); hb=hist([math.sqrt(3)],[2],[ob.z])
    a.check(DIS,"accepted_common_state_information_loss",oa.z==ob.z and np.array_equal(oa.Z_macro,ob.Z_macro) and
            tuple(oa.Z_chiral)==(0,0,0) and tuple(ob.Z_chiral)==(-1,0,1) and not np.array_equal(oa.Z_total,ob.Z_total) and
            np.array_equal(xyz(d.cylinder_history_coordinates(ha)),xyz(d.cylinder_history_coordinates(hb))) and
            np.array_equal(xyz(d.history_torus_coordinates(ha)),xyz(d.history_torus_coordinates(hb))))
    rounded=d.history_torus_coordinates(hist([1e20],[0],[1e20]))
    a.check(A,"rounded_torus_endpoints_allowed",rounded.r[0]==rounded.r_max and rounded.H_z==rounded.z_max and rounded.chi[0]==math.pi/2)
    collapsed=d.history_torus_coordinates(hist([1e-20],[0],[0]))
    a.check(A,"positive_minor_radius_can_disappear_from_XYZ",collapsed.r[0]>0 and tuple(xyz(collapsed)[0])==(2.,0.,0.),
            dict(r=float(collapsed.r[0]),xyz=xyz(collapsed).tolist()))
    # Ordinary display/diagnostic failures: no changed policy, no clipping.
    failure_cases=[
        ("quadratic_overflow",PE,lambda:d.quadratic_form([1e200,0,0])),
        ("quadratic_underflow",PE,lambda:d.quadratic_form([1e-200,0,0])),
        ("quartic_potential_overflow",PE,lambda:d.potential([1e100,0,0],basecfg)),
        ("quartic_gram_underflow",PE,lambda:d.chiral_area_accounting([1e-100,1e-100j,0])),
        ("budget_high_degree_overflow",PE,lambda:d.intensity_budget([1e100,0,0],basecfg)),
        ("history_dynamic_range_loss",PE,lambda:d.history_torus_coordinates(hist([1,1],[0,0],[1e-200,1e200]))),
        ("cylinder_nonzero_subnormal",PE,lambda:d.cylinder_point(sys.float_info.min,1,0)),
        ("alignment_norm_overflow",PE,lambda:d.historical_alignment([1.1e308]*3,[1,0,0],[1,0,0])),
        ("nonfinite_vector",ValueError,lambda:d.quadratic_form([float("nan"),0,0])),
        ("bool_real_rejected",TypeError,lambda:d.quadratic_form([True,0,0])),
        ("empty_torus_rejected",ValueError,lambda:d.history_torus_coordinates(hist([],[],[]))),
        ("bad_torus_domain",ValueError,lambda:d.history_torus_coordinates(h,R=1,r_max=1)),
        ("negative_kappa_rejected",ValueError,lambda:d.cylinder_point(-1,0,0)),
        ("float_sector_rejected",TypeError,lambda:d.cylinder_point(1,1.,0)),
        ("invalid_N_even_empty",ValueError,lambda:d.cylinder_history_coordinates(hist([],[],[]),N=0)),
        ("shape_mismatch",ValueError,lambda:d.cylinder_history_coordinates(hist([1],[0,1],[0]))),
        ("config_type",TypeError,lambda:d.intensity_budget(w,object())),
    ]
    for name,kind,call in failure_cases:
        a.raises(A,name,kind,call)
    large_obs=z.observe_staged([1e100,1e100j,0],z.Clock(),z.StagedConfig())
    a.check(A,"observer_can_succeed_outside_diagnostic_domain",np.all(np.isfinite(large_obs.Z_total)))
    a.raises(A,"observer_readout_accounting_quartic_failure",PE,lambda:d.readout_accounting(large_obs,alpha=1,beta=.5))
    a.check(A,"manual_record_not_formula_validation",d.Coordinates([1],[2,3],["raw"]).z.tolist()==["raw"])
    # Full ordinary-call ownership and forbidden-call instrumentation.
    saved_w=w.tobytes(); saved_h={k:v.tobytes() for k,v in h.items()}; saved_read=tuple(v.tobytes() for v in (observed.Z_macro,observed.Z_chiral,observed.Z_total))
    with ExitStack() as stack:
        for module,names in ((dynamics,("step3","step_ring","_advance","phase_sync")),(z,("advance_clock","advance_ema"))):
            for name in names:
                stack.enter_context(patch.object(module,name,side_effect=AssertionError("forbidden "+name)))
        call_results=[d.quadratic_form([1,2,3]),d.readout_accounting(observed,alpha=1,beta=-1),
            d.chiral_area_accounting(w),d.intensity_budget(w,basecfg),d.potential(w,basecfg),
            d.historical_alignment(observed.Z_macro,observed.Z_chiral,observed.Z_total),
            d.direct_history_coordinates({"Z_total":[observed.Z_total]}),d.cylinder_point(1,0,2),
            d.cylinder_history_coordinates(h),d.history_torus_coordinates(h)]
    a.check(OWN,"every_public_function_calls_no_advancement",len(call_results)==10)
    a.check(OWN,"successful_calls_preserve_inputs",w.tobytes()==saved_w and saved_h=={k:v.tobytes() for k,v in h.items()} and
            saved_read==tuple(v.tobytes() for v in (observed.Z_macro,observed.Z_chiral,observed.Z_total)))
    arrays=[budget.component_intensities,budget.increment,budget.diagnostic_pre_sync_prediction,area.chiral,
            call_results[1].blend_residual,direct.x,direct.y,direct.z,torus.x,torus.y,torus.z,torus.r,torus.chi,cyl]
    a.check(OWN,"all_returned_arrays_readonly_detached",all(not ar.flags.writeable and not np.shares_memory(ar,w) for ar in arrays))
    a.raises(OWN,"array_write_rejected",ValueError,lambda:torus.x.__setitem__(0,0))
    a.raises(OWN,"field_write_rejected",FrozenInstanceError,lambda:setattr(budget,"remainder",0))
    before_direct=direct.x.copy(); arr[0,0]=99
    a.check(OWN,"direct_input_mutation_does_not_change_result",np.array_equal(direct.x,before_direct) and not np.shares_memory(direct.x,arr))
    a.raises(OWN,"failure_does_not_repair_history",ValueError,lambda:d.history_torus_coordinates(h,R=0))
    a.check(OWN,"failed_calls_preserve_inputs",saved_h=={k:v.tobytes() for k,v in h.items()} and saved_w==w.tobytes())
    tree=ast.parse((root/SOURCES["DIAG"]).read_text())
    forbidden={"step3","step_ring","_advance","phase_sync","advance_clock","advance_ema"}
    calls={n.func.id if isinstance(n.func,ast.Name) else getattr(n.func,"attr","") for n in ast.walk(tree) if isinstance(n,ast.Call)}
    a.check(OWN,"static_transitive_boundary_entry_calls",not calls.intersection(forbidden),sorted(calls))
    a.details["call_boundary"]="Diagnostics call validators/checked arithmetic, raw z_chiral, pure blend_vectors and clock_angle. DynamicsConfig/L3 are imported; no recurrence is called. Runtime instrumentation complements source inspection."
    code="import sys,json; sys.path.insert(0,"+repr(str(root))+"); import kernel_physics.z_diagnostics; print(json.dumps(sorted(sys.modules)))"
    modules=json.loads(subprocess.check_output([sys.executable,"-B","-c",code],text=True))
    a.check(OWN,"fresh_import_no_historical_production_or_geometry_modules",not any(n.startswith(("kernel_TO","torment","openai","anthropic")) for n in modules) and
            not any(n in modules for n in ("kernel_physics.geometry","kernel_physics.face_state","kernel_physics.reference_scaffold")))
    runner_checks(a)


def runner_checks(a):
    from kernel_physics import api, dynamics, z_manifold as z, z_diagnostics as d, _runner, _records
    O="OWNERSHIP"
    params=api.Parameters(eps=.05,g=.2,phase_strength=.001,k=(1.,1.2,1.4))
    initial=api.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0)
    provenance=api.Provenance(kind="user_supplied",source_id="Atlas07",source_revision=None,
        locator="independent bounded diagnostic passivity check",literal_values={},notes="No physical interpretation")
    observer=api.historical_observer("paper_e_staged_v1")
    kwargs=dict(topology="triad",parameter_provenance=provenance,initialization_provenance=provenance,readouts=())
    diagnostics=("chiral_area_accounting","intensity_budget","potential","readout_accounting","historical_alignment")
    a.check(O,"actual_runner_diagnostic_inventory",_records._DIAGNOSTICS==diagnostics and
            _records._OBSERVER_DIAGNOSTICS==("readout_accounting","historical_alignment"))
    plain=json.loads(api.run(initial,params,updates=3,observers=(),diagnostics=(),**kwargs).to_json())
    observed=json.loads(api.run(initial,params,updates=3,observers=(observer,),diagnostics=diagnostics,**kwargs).to_json())
    a.check(O,"runner_diagnostics_do_not_change_omega_records",[r["omega"] for r in plain["samples"]]==[r["omega"] for r in observed["samples"]])
    events=[]; original={n:getattr(d,n) for n in diagnostics}; original_step=dynamics.step3
    def fn(name):
        def call(*args,**kw):
            events.append(name)
            return original[name](*args,**kw)
        return call
    def step(*args):
        events.append("step3")
        return original_step(*args)
    with ExitStack() as stack:
        stack.enter_context(patch.object(dynamics,"step3",side_effect=step))
        for name in diagnostics:
            stack.enter_context(patch.object(d,name,side_effect=fn(name)))
        api.run(initial,params,updates=1,observers=(observer,),diagnostics=diagnostics,**kwargs)
    a.check(O,"diagnostics_sample_initial_then_each_new_state",events==list(diagnostics)+["step3"]+list(diagnostics),events)
    # The prediction is forward from each sampled state, not last transition output.
    coherent=True
    for row in observed["samples"]:
        omega=[_records._complex(v) for v in row["omega"]]
        coherent &= row["diagnostics"]["intensity_budget"]==_records._encode(d.intensity_budget(omega,params._native()))
    a.check(O,"budget_from_each_stored_state",coherent)
    before=(initial,observer)
    with patch.object(d,"potential",side_effect=api.ResponsePrecisionError("intentional diagnostic failure")),patch.object(_runner,"RunRecord",wraps=api.RunRecord) as record:
        a.raises(O,"requested_diagnostic_failure_aborts_run",api.ResponsePrecisionError,
                 lambda:api.run(initial,params,updates=1,observers=(observer,),diagnostics=("potential",),**kwargs))
    a.check(O,"failure_returns_no_partial_record_and_preserves_inputs",record.call_count==0 and (initial,observer)==before)
    tiny=api.State(omega=(1e-200,0j,0j),update_index=0)
    a.check(O,"no_diagnostic_zero_update_can_succeed",len(api.run(tiny,params,updates=0,observers=(),diagnostics=(),**kwargs).data["samples"])==1)
    a.raises(O,"same_state_requested_diagnostic_fails",api.ResponsePrecisionError,
             lambda:api.run(tiny,params,updates=0,observers=(),diagnostics=("intensity_budget",),**kwargs))


def inventory_digest(files):
    return hashlib.sha256(json.dumps(files,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def integrity_checks(a,folder,root):
    if folder is None:
        a.details["integrity"]={"status":"NOT_REQUESTED","scope":"Scientific checks do not imply a before/after filesystem audit."}
        return
    names=("before.json","after.json","git_before.json","git_after.json","prior_artifacts_before.json")
    evidence={n:json.loads((folder/n).read_text(encoding="utf-8")) for n in names}
    before,after=evidence["before.json"],evidence["after.json"]
    tree_summary={}
    for name in ("current","old","torment_kernel","torment_checkout"):
        b,c=before[name],after[name]
        a.check("INTEGRITY",name+"_valid_inventory_hashes",b["count"]==len(b["files"]) and c["count"]==len(c["files"]) and
                inventory_digest(b["files"])==b["tree_sha256"] and inventory_digest(c["files"])==c["tree_sha256"])
        added=sorted(c["files"].keys()-b["files"].keys()); removed=sorted(b["files"].keys()-c["files"].keys())
        changed=sorted(k for k in b["files"].keys()&c["files"].keys() if b["files"][k]!=c["files"][k])
        a.check("INTEGRITY",name+"_unchanged",not added and not removed and not changed)
        tree_summary[name]={k:b[k] for k in ("root","count","tree_sha256","start_utc","end_utc")}
        tree_summary[name].update(after_sha256=c["tree_sha256"],after_count=c["count"],after_start=c["start_utc"],
                                 after_end=c["end_utc"],added=added,removed=removed,changed=changed)
    gb,ga=evidence["git_before.json"],evidence["git_after.json"]
    a.check("INTEGRITY","git_heads_and_tracked_status_unchanged",gb==ga)
    a.check("INTEGRITY","expected_current_head",gb["current"]["head"]==ga["current"]["head"]==EXPECTED_HEAD)
    paper_names=[p for p in before["current"]["files"] if any(p.startswith("papers/PAPER_"+letter+"/") for letter in "ABCDEF")]
    a.check("INTEGRITY","papers_A_F_file_bytes_unchanged",all(before["current"]["files"][p]==after["current"]["files"].get(p) for p in paper_names) and
            not any(any(p.startswith("papers/PAPER_"+letter+"/") for letter in "ABCDEF") and p not in before["current"]["files"] for p in after["current"]["files"]),
            {"files":len(paper_names)})
    prior=evidence["prior_artifacts_before.json"]
    a.check("INTEGRITY","prior_external_Atlas01_to06_artifacts_unchanged",all(sha(p)==h for p,h in prior.items()),{"files":len(prior)})
    a.check("INTEGRITY","bounded_source_registry_matches_inventories",all(before["current"]["files"][rel]==after["current"]["files"][rel]==sha(root/rel) for rel in SOURCES.values()))
    a.details["integrity"]=dict(status="COMPARED",method="Per-file SHA256; sorted compact JSON path/hash-map SHA256; all regular files including ignored/untracked except .git components; sequential scans, no timestamp/ACL/empty-directory/git-internal claim",
        trees=tree_summary,git_before=gb,git_after=ga,evidence_directory=str(folder),evidence_sha256={n:sha(folder/n) for n in names},
        prior_artifact_sha256=prior,papers_A_F_count=len(paper_names),
        action_record=dict(COMMITS=0,PUSHES=0,ATLAS_07_PUBLISHED="NO",scope="Actions in this Atlas-07 execution, not inferred solely from content hashes"))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=discover_repo())
    parser.add_argument("--output",type=Path,required=True,help="A NEW JSON file outside protected source trees; never overwritten")
    parser.add_argument("--scratch",type=Path,required=True,help="External temporary/cache directory")
    parser.add_argument("--integrity-dir",type=Path,help="Optional before/after inventory evidence; read only")
    parser.add_argument("--test-receipt",type=Path,help="Optional externally captured focused pytest receipt")
    parser.add_argument("--additional-test-receipt",type=Path,action="append",default=[],help="Preserve other test attempts without merging their counts")
    parser.add_argument("--atlas06-packet",type=Path,default=Path(r"C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md"))
    args=parser.parse_args()
    root=args.repo.resolve(); output=external(args.output,root); scratch=external(args.scratch,root)
    if output.exists():
        parser.error("Refusing to overwrite an existing result: "+str(output))
    if output==Path(__file__).resolve():
        parser.error("Output cannot be the checker source")
    scratch.mkdir(parents=True,exist_ok=True)
    for key,value in (("MPLCONFIGDIR",scratch/"mpl"),("XDG_CACHE_HOME",scratch/"cache"),("TMP",scratch),("TEMP",scratch)):
        os.environ[key]=str(value)
    sys.path.insert(0,str(root))
    audit=Audit()
    exact_checks(audit)
    api_checks(audit,root)
    integrity_checks(audit,args.integrity_dir,root)
    if args.test_receipt:
        receipt=json.loads(args.test_receipt.read_text(encoding="utf-8"))
        audit.check("API/PRECISION","focused_repository_test_assertions_passed",receipt["returncode"]==0)
        audit.details["focused_tests"]={"receipt_path":str(args.test_receipt),"sha256":sha(args.test_receipt),**receipt}
    else:
        audit.details["focused_tests"]={"status":"NOT_SUPPLIED"}
    audit.details["additional_test_attempts"]=[{"receipt_path":str(p),"sha256":sha(p),**json.loads(p.read_text(encoding="utf-8"))} for p in args.additional_test_receipt]
    attempts=([audit.details["focused_tests"]] if args.test_receipt else [])+audit.details["additional_test_attempts"]
    runtime_caveat=any("fatal exception" in receipt.get("stderr","").lower() for receipt in attempts)
    if runtime_caveat:
        audit.details["unresolved_runtime_caveat"]="Pytest reported passing assertions and zero exit status, but stderr reported Windows fatal exception/access violation. Receipts are retained; no clean-runtime certification or root-cause attribution is made."
    counts={g:{"total":len(rows),"passed":sum(row["passed"] for row in rows),"failed":sum(not row["passed"] for row in rows)} for g,rows in audit.groups.items()}
    failed=sum(r["failed"] for r in counts.values()); total=sum(r["total"] for r in counts.values())
    import sympy,numpy,mpmath
    result=dict(atlas="07",version="0.1",created_utc=datetime.now(timezone.utc).isoformat(),
        status=("PASS_WITH_RUNTIME_CAVEAT" if runtime_caveat else "PASS") if not failed else "FAIL",
        scientific_check_status="PASS" if not failed else "FAIL",total=total,passed=total-failed,failed=failed,group_counts=counts,
        runtime=dict(python=sys.version,executable=sys.executable,sympy=sympy.__version__,numpy=numpy.__version__,mpmath=mpmath.__version__),
        repository=str(root),expected_head=EXPECTED_HEAD,checker_sha256=sha(__file__),
        sources={key:dict(path=str(root/rel),sha256=sha(root/rel)) for key,rel in SOURCES.items()},
        atlas06_boundary=dict(path=str(args.atlas06_packet),sha256=sha(args.atlas06_packet),
            packaging_constraint="Atlas06 checker is left unchanged; it requires external execution/output at its own directory. Atlas07 does not inherit that output-location coupling."),
        checks=audit.groups,details=audit.details,
        reproducibility=dict(output=str(output),scratch=str(scratch),overwrite_policy="exclusive-create; no overwrite option",
            source_location_independent=True,integrity_evidence_optional=True))
    if not failed and args.integrity_dir:
        result["required_closeout"]=dict(CURRENT_REPO_CHANGED="NO",OLD_KERNEL_CHANGED="NO",TORMENT_CHANGED="NO",
            PAPERS_A_F_CHANGED="NO",COMMITS=0,PUSHES=0,ATLAS_07_PUBLISHED="NO")
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x",encoding="utf-8") as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False)
        stream.write("\n")
    print(json.dumps({k:result[k] for k in ("status","total","passed","failed","group_counts")},indent=2))
    return int(bool(failed))


if __name__=="__main__":
    raise SystemExit(main())
