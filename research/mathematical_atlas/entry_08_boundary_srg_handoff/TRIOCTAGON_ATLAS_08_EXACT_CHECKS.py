"""Atlas 08: independent algebra, bounded API witnesses, optional external receipts.

Run with python -B. --output and --scratch must be external; output is exclusive.
No tests are launched by this checker. No historical/production code is imported.
The optional --test-receipt and --integrity-directory report separate evidence.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import traceback

EXPECTED_HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
DEFAULT_REPO = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
PROTECTED = [Path(r"C:\TORMENT"), DEFAULT_REPO,
             Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO"),
             Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric")]
BRANCHES = ("negative_imag", "positive_imag")
CHECKS = []
WITNESSES = {}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def record(group, name, condition, evidence=None, kind="exact_symbolic"):
    item = dict(group=group, name=name, passed=bool(condition), kind=kind)
    if evidence is not None:
        item["evidence"] = evidence
    CHECKS.append(item)


def exact(group, name, value):
    import sympy as sp
    vals = list(value) if isinstance(value, sp.MatrixBase) else [value]
    residuals = [sp.simplify(sp.expand(v)) for v in vals]
    record(group, name, all(v == 0 for v in residuals),
           {"residuals": [str(v) for v in residuals]})


def near(group, name, actual, expected, rtol=2e-14, atol=2e-15):
    import numpy as np
    a, b = np.asarray(actual), np.asarray(expected)
    error = float(np.max(np.abs(a-b))) if a.size else 0.0
    record(group, name, np.allclose(a, b, rtol=rtol, atol=atol),
           dict(max_absolute_error=error, rtol=rtol, atol=atol),
           kind="binary64_witness")


def rejects(name, function, expected=(TypeError, ValueError), group="API/PRECISION"):
    try:
        function()
    except Exception as exc:
        record(group, name, isinstance(exc, expected),
               dict(exception=type(exc).__name__, message=str(exc)), "API_contract")
        return exc
    record(group, name, False, "No exception", "API_contract")
    return None


def canonical_zero(name, arr):
    import numpy as np
    record("API/PRECISION", name,
           np.all(arr == 0) and not np.signbit(arr.real).any()
           and not np.signbit(arr.imag).any(), kind="API_contract")


def independent_math():
    """Construct all symbolic expectations before importing the current API."""
    import sympy as s
    t = s.symbols("t", real=True)
    I = (2*t-s.sin(2*t))/s.pi
    g = "EXACT_LENS_GEOMETRY"
    exact(g, "area endpoints", s.Matrix([I.subs(t, 0), I.subs(t, s.pi/2)-1]))
    exact(g, "first derivative", s.diff(I, t)-4*s.sin(t)**2/s.pi)
    exact(g, "second derivative positive in open interval",
          s.diff(I, t, 2)-4*s.sin(2*t)/s.pi)
    coeffs = [s.Rational(4,3), -s.Rational(4,15), s.Rational(8,315),
              -s.Rational(4,2835), s.Rational(8,155925), -s.Rational(8,6081075)]
    poly = sum(a*t**(2*j) for j,a in enumerate(coeffs))/s.pi
    exact(g, "degree-13 Taylor polynomial",
          s.series(I,t,0,15).removeO()-t**3*poly)
    exact(g, "first omitted area coefficient",
          s.limit((I-t**3*poly)/t**15,t,0)-s.Rational(16,638512875)/s.pi)
    exact(g, "leading area limit", s.limit(I/t**3,t,0)-4/(3*s.pi))
    exact(g, "leading gain limit squared",
          s.limit(I/t**3,t,0)-(s.sqrt(4/(3*s.pi)))**2)
    R,theta = s.symbols("R theta", positive=True)
    sector = R**2*theta
    triangle = R**2*s.sin(2*theta)/2
    exact(g, "two segments divided by full disk area",
          2*(sector-triangle)/(s.pi*R**2)-I.subs(t,theta))
    # Bound is valid for 0<=t<=1/10 by decreasing alternating sine terms.
    bound = s.Rational(16,638512875)/s.pi/s.Integer(10)**15
    WITNESSES["lens_series"] = dict(factor_polynomial=str(poly),
        first_omitted_area_coefficient=str(s.Rational(16,638512875)/s.pi),
        absolute_truncation_bound_at_point_one=str(s.N(bound,25)),
        monotonicity_proof="I'=4 sin(theta)^2/pi; positive for 0<theta<pi/2",
        convexity_proof="I''=4 sin(2 theta)/pi; positive for 0<theta<pi/2")

    g = "EXACT_FOURIER_SRG"
    w = -s.Rational(1,2)+s.I*s.sqrt(3)/2
    F = s.Matrix([[1,1,1],[1,s.conjugate(w),w],[1,w,s.conjugate(w)]])/s.sqrt(3)
    f0 = F[:,0]
    S = s.Matrix([[0,0,1],[1,0,0],[0,1,0]])  # (Sx)_k=x_(k-1)
    exact(g, "cube-root convention", w**3-1)
    exact(g, "F is unitary", F.H*F-s.eye(3))
    exact(g, "source f2 is conjugate f1", F[:,2]-s.conjugate(F[:,1]))
    exact(g, "forward shift eigenvalues 1,w,wbar", S*F-F*s.diag(1,w,s.conjugate(w)))
    P=f0*f0.H
    exact(g, "balanced projector", P-s.ones(3)/3)
    exact(g, "P0 complementary orthogonal projector", P*P-P)
    q,r,c=s.symbols("q r c", positive=True)
    RR=r*P+q*(s.eye(3)-P);CC=P+c*(s.eye(3)-P)
    Z=s.diag(1,s.conjugate(w),w)
    A=RR*Z*CC
    W=s.Matrix([[0,0,r*c],[q,0,0],[0,q*c,0]])
    exact(g, "R diagonal in source Fourier basis", F.H*RR*F-s.diag(r,q,q))
    exact(g, "C diagonal in source Fourier basis", F.H*CC*F-s.diag(1,c,c))
    exact(g, "Z advances source Fourier index", Z*F-F*S)
    exact(g, "A weighted Fourier cycle", F.H*A*F-W)
    D=r*q*q*c*c
    exact(g, "three transfers are scalar", W**3-D*s.eye(3))
    z=s.symbols("z", real=True)
    exact(g, "A determinant", W.det()-D)
    cp = W.charpoly()
    exact(g, "A characteristic polynomial", cp.as_expr().subs(cp.gen,z)-(z**3-D))
    exact(g, "singular values squared",
          W.H*W-s.diag(q*q,q*q*c*c,r*r*c*c))
    exact(g, "normality obstruction",
          W*W.H-W.H*W-s.diag(r*r*c*c-q*q,q*q-q*q*c*c,q*q*c*c-r*r*c*c))
    for n in range(10):
        m,j=divmod(n,3)
        expected=D**m*(1,q,q*q*c)[j]*s.eye(3)[:,j]
        exact(g, f"cycle induction witness n={n}", W**n*s.eye(3)[:,0]-expected)
    v=s.symbols("v", nonzero=True, real=True)
    ev=s.Matrix([1,q/v,q*q*c/v**2])
    exact(g, "A eigenvector when v cubed equals D",
          (W*ev-v*ev)*v**2-s.Matrix([D-v**3,0,0]))
    alpha,beta=s.symbols("alpha beta",real=True)
    B=s.diag(s.cos(alpha)-s.I*s.sin(alpha),s.cos(alpha)+s.I*s.sin(alpha))*s.Matrix([
        [s.cos(beta),-s.I*s.sin(beta)],[-s.I*s.sin(beta),s.cos(beta)]])
    tau=s.cos(alpha)*s.cos(beta)
    exact(g, "B unitarity", B.H*B-s.eye(2))
    exact(g, "B normality", B.H*B-B*B.H)
    exact(g, "B determinant one", B.det()-1)
    exact(g, "B trace", s.trace(B)-2*tau)
    cp = B.charpoly()
    exact(g, "B characteristic polynomial",
          cp.as_expr().subs(cp.gen,z)-(z*z-2*tau*z+1))
    # Pauli construction makes gauge proof independent of API eigenvector formula.
    hx,hy,hz=s.symbols("hx hy hz",real=True)
    H=s.Matrix([[hz,hx-s.I*hy],[hx+s.I*hy,-hz]])
    delta=s.symbols("delta",positive=True)
    norm_h2=hx**2+hy**2+hz**2
    exact("EXACT_SPECTRAL_GAUGE","H squared scalar",H**2-norm_h2*s.eye(2))
    def gauge_exact(name,value):
        # Work on delta>0, delta^2=hx^2+hy^2+hz^2. Reduce polynomial
        # numerators modulo that relation; denominators are nonzero here.
        vals=list(value) if isinstance(value,s.MatrixBase) else [value]
        residuals=[]
        for entry in vals:
            numerator=s.cancel(entry).as_numer_denom()[0]
            residuals.append(s.rem(s.expand(numerator),delta**2-norm_h2,delta))
        exact("EXACT_SPECTRAL_GAUGE",name,s.Matrix(residuals))
    hh={hx:s.cos(alpha)*s.sin(beta),hy:s.sin(alpha)*s.sin(beta),
        hz:s.sin(alpha)*s.cos(beta)}
    exact("EXACT_SPECTRAL_GAUGE","Pauli reconstruction",B-(tau*s.eye(2)-s.I*H.subs(hh)))
    exact("EXACT_SPECTRAL_GAUGE","delta squared is one minus tau squared",
          (hx**2+hy**2+hz**2).subs(hh)+tau**2-1)
    tau0=s.symbols("tau0",real=True)
    BB=tau0*s.eye(2)-s.I*H
    projectors=[]
    for sign in (-1,1):
        lam=tau0+sign*s.I*delta;mu=tau0-sign*s.I*delta
        projector=(s.eye(2)-sign*H/delta)/2
        projectors.append(projector)
        gauge_exact(f"projector polynomial sign {sign}",
              (BB-mu*s.eye(2))-(lam-mu)*projector)
        gauge_exact(f"projector idempotence sign {sign}",
              projector**2-projector)
        gauge_exact(f"projector eigenrelation sign {sign}",
              BB*projector-lam*projector)
        gauge_exact(f"projector Hermitian sign {sign}",
              projector.H-projector)
        gauge_exact(f"projector rank-one trace/det sign {sign}",
              s.Matrix([s.trace(projector)-1,projector.det()]))
    exact("EXACT_SPECTRAL_GAUGE","complementary projectors",
          projectors[0]+projectors[1]-s.eye(2))
    # Generic chi coordinates; norm and contraction identities reduce to sums of squares.
    x,y=s.symbols("x y",real=True)
    xx=s.Matrix([x,y]);ff=s.Matrix([1,1,1])/s.sqrt(3)
    exact("EXACT_HANDOFF","tensor preparation norm factor",
          (s.kronecker_product(xx,ff).H*s.kronecker_product(xx,ff))[0]-(x*x+y*y))
    # Kronecker block expansion of full-space left-eigenbra identity.
    b00,b01,b10,b11,h0,h1,lam=s.symbols("b00 b01 b10 b11 h0 h1 lam",real=True)
    bgen=s.Matrix([[b00,b01],[b10,b11]])
    E=s.kronecker_product(s.Matrix([[h0,h1]]),s.eye(3))
    diff=E*s.kronecker_product(bgen,W)-lam*W*E
    residual=s.kronecker_product(s.Matrix([[h0*b00+h1*b10-lam*h0,
                                          h0*b01+h1*b11-lam*h1]]),W)
    exact("EXACT_HANDOFF","full-space intertwining residual equals eigenbra residual",diff-residual)
    a0,a1,b0,b1=s.symbols("a0 a1 b0 b1",complex=True)
    chi=s.Matrix([a0,a1]);xi=s.Matrix([b0,b1])
    overlap=(chi.H*xi)[0]
    gram=(chi.H*chi)[0]*(xi.H*xi)[0]-s.conjugate(overlap)*overlap
    wedge=a0*b1-a1*b0
    exact("BOUNDS","complex Cauchy-Schwarz two-dimensional identity",
          gram-s.conjugate(wedge)*wedge)
    for j in range(3):
        exact("BOUNDS",f"Fourier component modulus j={j}",
              s.Matrix([F[k,j]*s.conjugate(F[k,j])-s.Rational(1,3) for k in range(3)]))
    return dict(F=F,W=W,B=B,alpha=alpha,beta=beta,poly=poly,t=t)


def api_witnesses(repo, refs):
    import numpy as np
    import mpmath as mp
    from dataclasses import FrozenInstanceError
    from unittest.mock import patch
    br=importlib.import_module("kernel_physics.boundary_response")
    sr=importlib.import_module("kernel_physics.srg")
    num=importlib.import_module("kernel_physics._response_numeric")
    modules=(br,sr,num)
    for module in modules:
        record("API/PRECISION",f"authoritative import {module.__name__}",
               Path(module.__file__).resolve().is_relative_to(repo), str(module.__file__),"source_identity")
    PE=num.ResponsePrecisionError
    h=lambda theta,xi,n=0,branch=BRANCHES[0]:sr.handoff_area_response(
        theta,xi,transfer_count=n,branch=branch,response="lens_area_norm_v1")
    mp.mp.dps=500
    angle_fixtures=[1e-100,1e-12,np.nextafter(1e-8,0),1e-8,np.nextafter(1e-8,1),
                    .001,np.nextafter(.1,0),.1,np.nextafter(.1,1),.7,math.pi/2]
    errors=[]
    for t in angle_fixtures:
        tt=mp.mpf(float(t));area=(2*tt-mp.sin(2*tt))/mp.pi
        gain=mp.sqrt(area)
        ea=float(abs(mp.mpf(br.lens_area_fraction(t))/area-1))
        eg=float(abs(mp.mpf(br.lens_area_gain(t))/gain-1))
        errors.append(dict(theta=float(t),area_relative_error=ea,gain_relative_error=eg))
        record("API/PRECISION",f"500-digit area/gain t={t!r}",
               ea<1e-14 and eg<6e-15,errors[-1],"high_precision_witness")
    WITNESSES["area_gain_accuracy"]=errors
    for fn in (br.lens_area_fraction,br.lens_area_gain):
        near("API/PRECISION",fn.__name__+" endpoints",[fn(0),fn(math.pi/2)],[0,1],0,0)
    near("API/PRECISION","small factor polynomial",
         br._small_factor(.07),float(refs["poly"].subs(refs["t"],.07)),rtol=1e-15,atol=0)
    near("API/PRECISION","lens chart endpoints",
         [br.theta_from_lens(2,4),br.theta_from_lens(2,0)],[0,math.pi/2],0,0)
    near("API/PRECISION","large radius avoids 2r overflow",br.theta_from_lens(1e308,1e308),math.pi/3)
    record("API/PRECISION","near tangency survives representable separation",
           br.theta_from_lens(1,np.nextafter(2,0))>0,kind="binary64_witness")
    small=1e-120;sm=mp.mpf(small);gm=mp.sqrt((2*sm-mp.sin(2*sm))/mp.pi)
    rejects("small witness area not representable",lambda:br.lens_area_fraction(small),PE)
    near("API/PRECISION","small witness direct gain",br.lens_area_gain(small)/float(gm),1,3e-15,0)
    prep=br.prepare_area_response(small,[1,0])
    near("API/PRECISION","small preparation survives",prep[:3]/float(gm),
         np.ones(3)/math.sqrt(3),3e-15,0)
    record("FALSIFIERS","area availability is not gain availability",
           np.all(prep[:3].real>0),dict(theta=small,gain=br.lens_area_gain(small),
             prepared_component=float(prep[0].real)),"counterexample")
    xi=np.array([.6+.2j,-.3+.4j]);saved=xi.copy();t=.7
    p=br.prepare_area_response(t,xi)
    near("API/PRECISION","preparation tensor order",p,
         br.lens_area_gain(t)*np.kron(xi,np.ones(3)/math.sqrt(3)))
    near("BOUNDS","raw preparation norm",np.linalg.norm(p),br.lens_area_gain(t)*np.linalg.norm(xi))
    near("API/PRECISION","preparation complex scaling",br.prepare_area_response(t,2j*xi),2j*p)
    near("API/PRECISION","preparation real scaling",br.prepare_area_response(t,-3*xi),-3*p)
    canonical_zero("preparation zero theta",br.prepare_area_response(0,[-1,-1j]))
    canonical_zero("preparation zero xi bypasses unusable gain",
                   br.prepare_area_response(np.nextafter(0.,1.),[0,0]))
    tiny=br.prepare_area_response(math.pi/2,[1e-300,0])
    near("FALSIFIERS","squared norm underflow does not define xi zero",
         tiny[:3]/1e-300,np.ones(3)/math.sqrt(3),2e-15,0)
    record("API/PRECISION","preparation inputs unchanged, output fresh",
           np.array_equal(xi,saved) and not np.shares_memory(xi,p),kind="API_contract")

    F=np.asarray(refs["F"].evalf(),dtype=complex)
    q,r,c=math.exp(-.423),math.exp(.577),.382
    D=r*q*q*c*c
    W=np.array([[0,0,r*c],[q,0,0],[0,q*c,0]])
    A=F@W@F.conj().T
    alpha,beta=2*math.pi*.244,math.pi*.244
    # Independent Pauli expansion, rather than multiplying the source factors.
    hx,hy,hz=math.cos(alpha)*math.sin(beta),math.sin(alpha)*math.sin(beta),math.sin(alpha)*math.cos(beta)
    tau=math.cos(alpha)*math.cos(beta);delta=math.sqrt(hx*hx+hy*hy+hz*hz)
    H=np.array([[hz,hx-1j*hy],[hx+1j*hy,-hz]])
    B=tau*np.eye(2)-1j*H
    U=np.kron(B,A)
    ops=sr.fixed_november_srg()
    near("API/PRECISION","source Fourier order",sr.fourier_basis(),F)
    for name,ref in (("A",A),("B",B),("U",U)):
        near("API/PRECISION",name+" independently reconstructed",getattr(ops,name),ref)
    near("API/PRECISION","U determinant",np.linalg.det(ops.U),D**2,2e-14,0)
    # All positive weights <1; symbolic proof for rc is recorded in the packet.
    record("BOUNDS","fixed weighted-cycle contraction",0<q<1 and 0<q*c<1 and 0<r*c<382/423<1,
           dict(q=q,qc=q*c,rc=r*c,D_cycle=D),"binary64_witness")
    record("FALSIFIERS","A is not normal at fixed literals",
           np.linalg.norm(A@A.conj().T-A.conj().T@A)>.1,kind="counterexample")
    record("FALSIFIERS","A and U are not unitary",
           np.linalg.norm(A.conj().T@A-np.eye(3))>.1 and np.linalg.norm(U.conj().T@U-np.eye(6))>.1,
           kind="counterexample")
    record("API/PRECISION","fixed adopted defaults",
           (sr.NOVEMBER.eta,sr.NOVEMBER.gamma,sr.NOVEMBER.lambda_c,sr.NOVEMBER.clock_fraction)==(.423,.577,.618,.244),
           kind="API_contract")
    rejects("frozen November record",lambda:setattr(sr.NOVEMBER,"eta",1),FrozenInstanceError)
    for name in ("R","Z","C","A","B","U"):
        arr=getattr(ops,name)
        record("API/PRECISION",name+" returned read-only",not arr.flags.writeable,kind="API_contract")
        rejects(name+" in-place assignment refused",lambda arr=arr:arr.__setitem__((0,0),999),ValueError)
    modes={}
    with patch("numpy.linalg.eig",side_effect=AssertionError("eigensolver ordering forbidden")):
        for branch in BRANCHES:
            modes[branch]=sr.helicity_mode(branch)
    for idx,branch in enumerate(BRANCHES):
        mode=modes[branch];sign=(-1,1)[idx]
        lam=tau+sign*1j*delta
        projector=(np.eye(2)-sign*H/delta)/2
        pivot=int(np.argmax(np.diag(projector).real))
        chi=projector[:,pivot]/math.sqrt(projector[pivot,pivot].real)
        near("EXACT_SPECTRAL_GAUGE",branch+" Pauli-projector chi",mode.chi,chi)
        near("EXACT_SPECTRAL_GAUGE",branch+" eigenvalue",mode.eigenvalue,lam)
        near("EXACT_SPECTRAL_GAUGE",branch+" eigenvector",B@mode.chi,lam*mode.chi)
        near("EXACT_SPECTRAL_GAUGE",branch+" eigenbra same lambda",mode.chi.conj()@B,lam*mode.chi.conj())
        near("EXACT_SPECTRAL_GAUGE",branch+" norm",np.vdot(mode.chi,mode.chi),1)
        record("EXACT_SPECTRAL_GAUGE",branch+" gauge and pivot",
               mode.pivot==idx==pivot and mode.chi[pivot].real>0 and mode.chi[pivot].imag==0
               and not mode.chi.flags.writeable and mode.gauge=="spectral_projector_maxdiag_positive_v1",
               dict(pivot=pivot,chi=[[float(z.real),float(z.imag)] for z in mode.chi]),"API_contract")
        E=np.kron(mode.chi.conj()[None,:],np.eye(3))
        for n in (0,1,2,3,7):
            near("EXACT_HANDOFF",f"full 3x6 operator identity {branch} n={n}",
                 E@np.linalg.matrix_power(U,n),lam**n*np.linalg.matrix_power(A,n)@E)
        for n in (0,1,2,3,7,10):
            mm,j=divmod(n,3);bn=D**mm*(1,q,q*q*c)[j]
            for source_index,incident in enumerate((xi,np.array([1,0]),np.array([2j,-.7]))):
                result=h(t,incident,n,branch).omega
                direct=E@np.linalg.matrix_power(U,n)@(br.lens_area_gain(t)*np.kron(incident,F[:,0]))
                formula=br.lens_area_gain(t)*np.vdot(mode.chi,incident)*lam**n*bn*F[:,j]
                near("EXACT_HANDOFF",f"shortcut versus direct {branch} n={n} xi={source_index}",result,direct)
                near("EXACT_HANDOFF",f"closed form {branch} n={n} xi={source_index}",result,formula)
                exactnorm=br.lens_area_gain(t)*abs(np.vdot(mode.chi,incident))*bn
                near("BOUNDS",f"norm identity {branch} n={n} xi={source_index}",np.linalg.norm(result),exactnorm)
                near("BOUNDS",f"max-component equality {branch} n={n} xi={source_index}",
                     max(abs(result)),exactnorm/math.sqrt(3))
                record("BOUNDS",f"incident norm bound {branch} n={n} xi={source_index}",
                       np.linalg.norm(result)<=bn*np.linalg.norm(incident)+2e-15,kind="binary64_witness")
        perpendicular=np.array([-mode.chi[1].conjugate(),mode.chi[0].conjugate()])
        canonical_zero(branch+" literal calculated overlap zero",h(t,perpendicular,7,branch).omega)
        tiny=h(math.pi/2,1e-250*mode.chi,0,branch).omega
        near("FALSIFIERS",branch+" tiny unthresholded overlap",tiny.real/1e-250,
             np.ones(3)/math.sqrt(3),2e-14,0)
        record("FALSIFIERS",branch+" tiny overlap stays nonzero",np.all(tiny.real!=0),kind="counterexample")
        other=modes[BRANCHES[1-idx]].chi
        ov=num.bra_dot(mode.chi,other,"Atlas08 mode overlap witness")
        WITNESSES.setdefault("other_branch_calculated_overlap",{})[branch]=[ov.real,ov.imag]
    near("EXACT_SPECTRAL_GAUGE","named branches orthogonal to roundoff",
         np.vdot(modes[BRANCHES[0]].chi,modes[BRANCHES[1]].chi),0,0,1e-15)
    # Generic six-vector, not restricted to the preparation subspace.
    psi=np.array([1+.3j,-.4,.2j,.8,-.7j,.1+.2j])
    bra=np.array([.3j,.4])/0.5
    generic=sr.project_bra(psi,bra)
    near("API/PRECISION","generic bra block expansion",generic,bra[0].conjugate()*psi[:3]+bra[1].conjugate()*psi[3:])
    near("API/PRECISION","projection linear in state",sr.project_bra(2j*psi,bra),2j*generic)
    near("API/PRECISION","projection conjugate-linear in bra",sr.project_bra(psi,2j*bra),-2j*generic)
    record("BOUNDS","unit-bra contraction witness",np.linalg.norm(generic)<=np.linalg.norm(psi),kind="binary64_witness")
    E0=np.kron([[1,0]],np.eye(3));lam=modes[BRANCHES[0]].eigenvalue
    mismatch=np.linalg.norm(E0@U-lam*A@E0)
    record("FALSIFIERS","generic non-eigen bra lacks named reduction",mismatch>.1,
           dict(full_operator_residual=float(mismatch)),"counterexample")
    near("FALSIFIERS","nonunit bra may amplify",sr.project_bra(np.r_[F[:,0],np.zeros(3)],[2,0]),2*F[:,0])
    near("FALSIFIERS","raw handoff has no normalization",h(.7,2*xi).omega,2*h(.7,xi).omega)
    near("EXACT_HANDOFF","n=0 no transfer",h(t,xi).omega,
         br.lens_area_gain(t)*np.vdot(modes[BRANCHES[0]].chi,xi)*F[:,0])
    result=h(.4,[2+.3j,1j],np.int64(2),BRANCHES[1]);data=result.metadata()
    expected=dict(response_id="lens_area_norm_v1",source_id="november_fixed_srg",
        source_parameters=dict(eta=.423,gamma=.577,lambda_c=.618,clock_fraction=.244,
                               alpha="2*pi*0.244",beta="pi*0.244"),
        tensor_order="helicity_major_C2_tensor_C3",branch=BRANCHES[1],
        gauge="spectral_projector_maxdiag_positive_v1",theta=.4,xi=[[2.,.3],[0.,1.]],
        transfer_count=2,normalization="none")
    record("API/PRECISION","complete initialization metadata",data==expected,data,"API_contract")
    record("API/PRECISION","JSON ready and fresh metadata",json.loads(json.dumps(data))==data
           and result.metadata() is not data,kind="API_contract")
    record("API/PRECISION","handoff output read-only",not result.omega.flags.writeable,kind="API_contract")
    # Monkeypatch is process-local; no file changes, no downstream step execution.
    dyn=importlib.import_module("kernel_physics.dynamics")
    with patch.object(dyn,"step3",side_effect=AssertionError("must not call downstream recurrence")):
        value=h(t,xi,2)
    record("FALSIFIERS","handoff does not invoke downstream step3",
           np.all(np.isfinite(value.omega)),kind="call_boundary_witness")
    WITNESSES["fixed_parameters_derived"] = dict(q=q,r=r,c=c,D_cycle=D,tau=tau,delta=delta,
        eigenvalues=[[tau,-delta],[tau,delta]],weight_singular_values=[q,q*c,r*c])

    for bad in (True,np.bool_(True),"0.2",.2+0j,np.array(.2),[.2]):
        rejects("strict theta rejects "+repr(bad),lambda bad=bad:br.lens_area_gain(bad),TypeError)
    for bad in (-.1,math.pi,math.inf,math.nan):
        rejects("theta domain "+repr(bad),lambda bad=bad:br.prepare_area_response(bad,[0,0]),ValueError)
    for bad in ([True,0],["1",0],[np.inf,0],[1],[1,2,3],[[1,0]], [complex(1,math.nan),0]):
        rejects("strict xi rejects "+repr(bad),lambda bad=bad:br.prepare_area_response(0,bad))
    for radius,sep in ((0,0),(-1,0),(1,-1),(1,3),(math.inf,1),(1,math.nan)):
        rejects(f"lens domain r={radius} d={sep}",lambda radius=radius,sep=sep:br.theta_from_lens(radius,sep),ValueError)
    rejects("lens nonzero ratio lost",lambda:br.theta_from_lens(1e308,1e-300),PE)
    rejects("lens half ratio subnormal",lambda:br.theta_from_lens(1,sys.float_info.min),PE)
    for bad in (-1,1.,True,np.bool_(True),"1"):
        rejects("zero handoff still rejects count "+repr(bad),lambda bad=bad:h(0,[0,0],bad))
    for branch in ("first","",None,0):
        rejects("zero handoff still rejects branch "+repr(branch),lambda branch=branch:h(0,[0,0],0,branch),ValueError)
    rejects("missing explicit response",lambda:sr.handoff_area_response(0,[0,0],transfer_count=0,branch=BRANCHES[0]),TypeError)
    for bad in ("default","",None,True):
        rejects("wrong response "+repr(bad),lambda bad=bad:sr.handoff_area_response(0,[0,0],transfer_count=0,branch=BRANCHES[0],response=bad),ValueError)
    rejects("zero theta does not bypass bad xi",lambda:h(0,[np.nan,0]),ValueError)
    rejects("zero xi does not bypass bad theta",lambda:h(-1,[0,0]),ValueError)
    canonical_zero("handoff theta zero",h(0,[-1,-1j],10**400).omega)
    canonical_zero("handoff xi zero",h(np.nextafter(0.,1.),[0,0],10**400).omega)
    rejects("nonzero handoff subnormal product",lambda:h(1e-20,[1e-300,0]),PE)
    rejects("nonzero handoff long-cycle underflow",lambda:h(.7,[1,0],10000),PE)
    huge=rejects("huge integer exponent conversion guarded",lambda:h(.7,[1,0],10**400),PE)
    WITNESSES["huge_count_failure"]=None if huge is None else str(huge)
    rejects("gain nonzero subnormal",lambda:br.lens_area_gain(1e-210),PE)
    rejects("area nonzero subnormal",lambda:br.lens_area_fraction(1e-103),PE)
    rejects("preparation product underflow",lambda:br.prepare_area_response(1e-20,[1e-300,0]),PE)
    rejects("generic intermediate overflow",lambda:sr.project_bra(np.full(6,1e308),[2,2]),PE)
    # Exact final generic result would be zero: 2*1e308 - 2*1e308.
    rejects("finite exact resummed result can fail intermediate",
            lambda:sr.project_bra(np.r_[np.full(3,1e308),np.full(3,-1e308)],[2,2]),PE)
    # Sum accepts literal calculated zero; compensated summation cannot undo product rounding.
    aa=1.+2.**-27;bb=1.-2.**-27
    cancelled=num.bra_dot([aa,1],[bb,-1],"rounded cancellation")
    from fractions import Fraction
    true_overlap=Fraction(aa)*Fraction(bb)-1
    record("FALSIFIERS","calculated zero need not be exact orthogonality",
           cancelled==0 and true_overlap!=0,
           dict(calculated=[cancelled.real,cancelled.imag],exact_binary_input_dot=str(true_overlap)),
           "exact_rational_counterexample")
    # Identifies stages; does not establish a universal maximum n for all inputs.
    cycle_samples={}
    for n in (960,963,964,965,966,968,969):
        try:
            gain,j=sr._cycle_gain(n)
            cycle_samples[str(n)]=dict(gain=gain,j=j)
        except PE as exc:
            cycle_samples[str(n)]=dict(exception=type(exc).__name__,message=str(exc))
    WITNESSES["selected_cycle_precision_edges"]=cycle_samples
    handoff_samples={}
    for n in (963,964,965,968,969):
        try:
            value=h(.7,[1,0],n).omega
            handoff_samples[str(n)]=dict(omega=[[float(z.real),float(z.imag)] for z in value])
        except PE as exc:
            handoff_samples[str(n)]=dict(exception=type(exc).__name__,message=str(exc))
    WITNESSES["selected_handoff_precision_edges_theta07_xi10_negative"]=handoff_samples
    return {m.__name__:dict(path=str(Path(m.__file__).resolve()),sha256=sha(m.__file__)) for m in modules}


def source_manifest(repo):
    paths=[repo/"kernel_physics"/n for n in (
        "boundary_response.py","srg.py","_response_numeric.py","readouts.py","dynamics.py",
        "operating_region.py","README.md","tests/test_boundary_response.py",
        "tests/test_srg.py","tests/test_boundary_pipeline.py")]
    notes=repo.parent/"research"/"GPT_proof"
    paths += [notes/n for n in (
        "GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md",
        "CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md",
        "CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md",
        "CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md",
        "CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md",
        "CODEX_BOUNDARY_RESPONSE_FINISH_RESULTS.json")]
    return {str(p):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in paths if p.is_file()}


def integrity_receipt(directory):
    if directory is None:
        return dict(status="NOT_SUPPLIED",separate_from_scientific_predicates=True)
    directory=Path(directory)
    read=lambda name:json.loads((directory/name).read_text(encoding="utf8"))
    before,after=read("before.json"),read("after.json")
    gb,ga=read("git_before.json"),read("git_after.json")
    scopes={};passed=True
    for key,left in before.items():
        right=after[key]
        recompute=lambda v:hashlib.sha256(json.dumps(v["files"],sort_keys=True,separators=(",",":")).encode()).hexdigest()
        same=left["root"]==right["root"] and left["files"]==right["files"]
        valid=all(recompute(x)==x["tree_sha256"] and len(x["files"])==x["count"] for x in (left,right))
        scopes[key]=dict(root=left["root"],before_count=left["count"],after_count=right["count"],
                         before_sha256=left["tree_sha256"],after_sha256=right["tree_sha256"],
                         unchanged=same,manifests_valid=valid,
                         before_start_utc=left["start_utc"],after_end_utc=right["end_utc"])
        passed &= same and valid
    papers=lambda rec:{p:h for p,h in rec["current"]["files"].items()
                       if any(p.startswith("papers/PAPER_"+x+"/") for x in "ABCDEF")}
    prior=read("prior_atlas_before.json")
    prior_after={p:sha(p) if Path(p).is_file() else None for p in prior}
    prior_ok=prior==prior_after
    passed &= gb==ga and prior_ok and papers(before)==papers(after)
    receipts={}
    for name in ("before.json","after.json","git_before.json","git_after.json","prior_atlas_before.json"):
        receipts[name]=dict(path=str(directory/name),sha256=sha(directory/name))
    return dict(status="PASS" if passed else "FAIL",separate_from_scientific_predicates=True,
        scopes=scopes,git_before=gb,git_after=ga,git_unchanged=gb==ga,
        papers_A_F=dict(count=len(papers(before)),unchanged=papers(before)==papers(after)),
        prior_external_atlas=dict(count=len(prior),unchanged=prior_ok,before=prior,after=prior_after),
        receipts=receipts,limitation="Full regular-file path/content inventory, excludes .git internals, timestamps and ACLs; Git HEAD/tracked status separately compared.")


def read_test_receipt(path):
    if path is None:
        return dict(status="NOT_SUPPLIED")
    data=json.loads(Path(path).read_text(encoding="utf8"))
    valid=sha(data["stdout_file"])==data["stdout_sha256"] and sha(data["stderr_file"])==data["stderr_sha256"]
    data["receipt_sha256"]=sha(path)
    data["logs_verified"]=valid
    data["status"]="PASS_WITH_RUNTIME_CAVEAT" if data["returncode"]==0 and data["runtime_anomaly"] and valid else (
        "PASS" if data["returncode"]==0 and not data["stderr_bytes"] and valid else "REVIEW")
    return data


def external(path,repo):
    resolved=path.expanduser().resolve()
    for root in [repo,*PROTECTED]:
        if resolved==root.resolve() or resolved.is_relative_to(root.resolve()):
            raise ValueError(f"Must be external to protected trees: {resolved}")
    return resolved


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=None)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--scratch",type=Path,required=True)
    parser.add_argument("--integrity-directory",type=Path)
    parser.add_argument("--test-receipt",type=Path)
    args=parser.parse_args()
    repo=args.repo
    if repo is None:
        repo=next((p for p in [Path.cwd(),*Path.cwd().parents]
                   if (p/"kernel_physics"/"srg.py").is_file()),DEFAULT_REPO)
    repo=repo.resolve()
    if not (repo/"kernel_physics"/"srg.py").is_file():
        parser.error("No current kernel_physics/srg.py at --repo")
    try:
        output=external(args.output,repo);scratch=external(args.scratch,repo)
        if output.exists() or args.output.is_symlink():
            parser.error("Refusing to overwrite --output; choose a new external filename")
        if output==scratch or output in scratch.parents:
            parser.error("--output must be a file distinct from the scratch directory")
    except ValueError as exc:
        parser.error(str(exc))
    # No scientific imports or scratch creation have occurred before path refusal.
    scratch.mkdir(parents=True,exist_ok=True)
    run=Path(tempfile.mkdtemp(prefix="atlas08_",dir=scratch))
    output.parent.mkdir(parents=True,exist_ok=True)
    original_dontwrite=sys.dont_write_bytecode
    sys.dont_write_bytecode=True
    os.environ.update(PYTHONDONTWRITEBYTECODE="1",MPLCONFIGDIR=str(run/"mpl"),
                      XDG_CACHE_HOME=str(run/"cache"),TEMP=str(run),TMP=str(run))
    sys.path.insert(0,str(repo))
    start=datetime.now(timezone.utc).isoformat()
    sources=source_manifest(repo)
    head=subprocess.check_output(["git","--no-optional-locks","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    result=dict(schema="TRIOCTAGON_ATLAS_08_EXACT_RESULTS/0.1",created_utc=start,
                repo=str(repo),head=head,expected_head=EXPECTED_HEAD,head_matches=head==EXPECTED_HEAD,
                checker_sha256=sha(__file__),scratch=str(run),sources=sources,
                command=sys.argv,python=sys.version,executable=sys.executable,
                launched_with_bytecode_disabled=original_dontwrite)
    try:
        refs=independent_math()
        result["imported_sources"]=api_witnesses(repo,refs)
        import numpy, sympy, mpmath
        result["versions"]=dict(numpy=numpy.__version__,sympy=sympy.__version__,mpmath=mpmath.__version__)
    except Exception:
        result["unexpected_exception"]=traceback.format_exc()
    result["scientific_checks"]=CHECKS
    result["counts_by_group"]=dict(Counter(x["group"] for x in CHECKS))
    result["counts_by_kind"]=dict(Counter(x["kind"] for x in CHECKS))
    result["scientific_summary"]=dict(total=len(CHECKS),passed=sum(x["passed"] for x in CHECKS),
        failed=sum(not x["passed"] for x in CHECKS))
    result["witnesses"]=WITNESSES
    result["source_files_unchanged_during_checker"]=sources==source_manifest(repo)
    result["integrity"]=integrity_receipt(args.integrity_directory)
    result["focused_tests"]=read_test_receipt(args.test_receipt)
    success=not result.get("unexpected_exception") and all(x["passed"] for x in CHECKS)
    result["scientific_status"]="PASS" if success else "FAIL"
    result["status"]=("PASS_WITH_RUNTIME_CAVEAT" if success and result["focused_tests"]["status"]=="PASS_WITH_RUNTIME_CAVEAT"
                      else result["scientific_status"])
    if result["focused_tests"]["status"]=="REVIEW":
        result["status"]="REVIEW"
    if not result["source_files_unchanged_during_checker"] or result["integrity"]["status"]=="FAIL" or head!=EXPECTED_HEAD:
        result["status"]="FAIL"
    result["completed_utc"]=datetime.now(timezone.utc).isoformat()
    # Exclusive creation also prevents a race after the initial existence check.
    with output.open("x",encoding="utf8",newline="\n") as f:
        json.dump(result,f,indent=2,ensure_ascii=False,allow_nan=False);f.write("\n")
    print(json.dumps(dict(status=result["status"],summary=result["scientific_summary"],output=str(output))))
    return 0 if result["status"] in ("PASS","PASS_WITH_RUNTIME_CAVEAT") else 1


if __name__=="__main__":
    raise SystemExit(main())
