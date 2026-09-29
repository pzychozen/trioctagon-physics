"""Atlas 09: exact profile proof obligations and current API witnesses.
Read-only; no historical execution; optional test/integrity receipts are separate.
Run with -B; --output and --scratch are required external paths; no overwrite.
"""
from __future__ import annotations
import argparse, ast, cmath, hashlib, importlib, json, math, os, subprocess, sys, tempfile, traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
EXPECTED_HEAD="34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
DEFAULT_REPO=Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
PROTECTED=[Path(r"C:\TORMENT"),DEFAULT_REPO,Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO"),Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric")]
CHECKS=[]
WITNESSES={}


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


def rejects(name, function, expected=(TypeError, ValueError), group="API_VALIDATION"):
    try:
        function()
    except Exception as exc:
        record(group, name, isinstance(exc, expected),
               dict(exception=type(exc).__name__, message=str(exc)), "API_contract")
        return exc
    record(group, name, False, "No exception", "API_contract")
    return None


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


def independent_math():
    """Definitions and exact expectations constructed before any current API import."""
    import sympy as s
    R=s.Rational
    rho,k,a=s.symbols("rho k a",real=True)
    oi,oj,ol=s.symbols("oi oj ol",complex=True)
    original=oi+R(1,20)*(k-rho**2)*oi+R(1,5)*(-2*oi+oj+ol)
    reduced=(R(3,5)+k/20-rho**2/20)*oi+(oj+ol)/5
    g="EXACT_PROFILE_ALGEBRA"
    exact(g,"L3 coefficient rewrite",original-reduced)
    exact(g,"a lower and upper endpoints",
          s.Matrix([(R(3,5)+k/20).subs(k,0)-R(3,5),
                    (R(3,5)+k/20).subs(k,8)-1]))
    exact(g,"positive coefficient decomposition",
          R(3,5)+k/20-rho**2/20-(R(3,20)+k/20+(9-rho**2)/20))
    record(g,"minimum coefficient positive",R(3,20)>0,
           "k>=0 and 9-rho^2>=0 on 0<=rho<=3",kind="exact_inequality")
    exact(g,"coupling cap",(3+3)/s.Integer(5)-R(6,5))
    fa=rho*(a-rho**2/20);f=fa.subs(a,1)
    exact(g,"monotone in a derivative",s.diff(fa,a)-rho)
    exact(g,"f derivative",s.diff(f,rho)-(1-3*rho**2/20))
    star=s.sqrt(R(20,3));maximum=4*s.sqrt(15)/9;cap=R(6,5)+maximum
    record(g,"critical point in open interval",0<star<3,kind="exact_inequality")
    exact(g,"critical point derivative zero",s.diff(f,rho).subs(rho,star))
    exact(g,"critical point value",f.subs(rho,star)-maximum)
    exact(g,"both endpoint values",s.Matrix([f.subs(rho,0),f.subs(rho,3)-R(33,20)]))
    record(g,"critical point beats endpoints",maximum>R(33,20)>0,kind="exact_inequality")
    # Provides a global maximum certificate without relying solely on stationary points.
    exact(g,"global maximum factor certificate",
          maximum-f-(rho-star)**2*(rho+2*star)/20)
    g="EXACT_INVARIANCE"
    exact(g,"strict bound via rational squared difference",
          R(81,25)-maximum**2-R(187,675))
    record(g,"rational difference strictly positive",R(187,675)>0,kind="exact_inequality")
    record(g,"uniform cap strictly below three",cap<3,kind="exact_inequality")
    margin=3-cap
    exact(g,"exact margin",margin-(R(9,5)-4*s.sqrt(15)/9))
    t,phase,strength=s.symbols("t phase strength",real=True)
    amp=s.symbols("amp",nonnegative=True)
    phased=amp*s.exp(s.I*(phase+strength*t))
    exact(g,"phase preserves squared modulus",
          phased*s.conjugate(phased)-amp**2)
    exact(g,"zero-amplitude phase convention",phased.subs(amp,0))
    extremizer=s.Matrix([star,3,3])
    pre=s.Matrix([(R(3,5)+R(8,20)-v*v/20)*v+
                 sum(extremizer[j] for j in range(3) if j!=i)/5
                 for i,v in enumerate(extremizer)])
    exact(g,"attained first component cap",pre[0]-cap)
    record(g,"extremizer all pre-sync components positive",
           all(v>0 for v in pre),kind="exact_inequality")
    record(g,"other extremizer components no larger",all(v<=cap for v in pre),kind="exact_inequality")
    # Equal positive phases make every sine increment zero for every finite strength.
    exact(g,"aligned-phase sine sums zero",2*s.sin(3*(0-0)))
    WITNESSES["exact_theorem"]=dict(
        domain="D3={Omega in C^3: max_i |Omega_i|<=3}",
        hypotheses="eps=1/20, g=1/5, 0<=k_i<=8, finite real phase_strength, no forcing/noise",
        one_step="F3(D3) subset D_B with B=6/5+4sqrt(15)/9<3; B is attained",
        induction="Base Omega_0 in D3. If Omega_n in D3, the same admitted config gives Omega_(n+1) in D_B subset D3. Thus all integer n>=0; D_B bound applies from n=1.",
        cap_exact=str(cap),cap_decimal=float(cap),margin_exact=str(margin),margin_decimal=float(margin),
        extrema=[str(x) for x in pre],
        scope="Exact theorem; no assertion of contraction, convergence, physical meaning or indefinite machine success.")
    g="PRECISION/FALSIFIERS"
    common=t*(R(7,5)-t*t/20)
    exact(g,"balanced common-coordinate multiplier",s.diff(common,t).subs(t,0)-R(7,5))
    exact(g,"common-line expansion at t=1",common.subs(t,1)-R(27,20))
    record(g,"expansion exceeds one",R(27,20)>1,kind="exact_inequality")
    exact(g,"nonzero balanced fixed point",common.subs(t,s.sqrt(8))-s.sqrt(8))
    exact(g,"origin fixed",common.subs(t,0))
    normalized=t*(R(7,5)-t*t/60)
    exact(g,"normalized balanced fixed amplitude",normalized.subs(t,s.sqrt(24))-s.sqrt(24))
    J=R(4,5)*s.eye(3)+R(1,5)*s.ones(3)
    exact(g,"pre-sync Jacobian common direction",J*s.ones(3,1)-R(7,5)*s.ones(3,1))
    exact(g,"pre-sync Jacobian transverse direction",
          J*s.Matrix([1,-1,0])-R(4,5)*s.Matrix([1,-1,0]))
    outside=s.Matrix([10,0,0])
    plain=s.Matrix([(R(3,5)-v*v/20)*v+
                    sum(outside[j] for j in range(3) if j!=i)/5
                    for i,v in enumerate(outside)])
    exact(g,"radius-ten extension falsifier",plain-s.Matrix([-44,2,2]))
    record(g,"self coefficient can be negative outside profile",R(3,5)-R(100,20)<0,kind="exact_inequality")

    g="EXACT_INCIDENT_BUDGET"
    # Atlas 08 identities are hypotheses here, not re-derived SRG physics.
    gain,overlap,bn,N=s.symbols("G overlap b_n N",nonnegative=True)
    amplitude=gain*overlap*bn/s.sqrt(3)
    exact(g,"exact initialized component amplitude",amplitude*s.sqrt(3)-gain*overlap*bn)
    exact(g,"uniform bound deficit decomposition",
          N-gain*overlap*bn-((1-gain)*N+gain*(N-overlap)+gain*overlap*(1-bn)))
    budget=3*s.sqrt(3)
    exact(g,"uniform equality at full gain zero count aligned mode",
          amplitude.subs({gain:1,overlap:budget,bn:1})-3)
    excess=s.symbols("excess",positive=True)
    exact(g,"any larger norm-only budget fails in aligned equality case",
          (budget+excess)/s.sqrt(3)-3-excess/s.sqrt(3))
    record(g,"norm six exceeds uniform budget",6>budget,kind="exact_inequality")
    # G(pi/6)^2 < 1/3; with norm-six aligned incident, component <2<3.
    angle=s.pi/6;area=(2*angle-s.sin(2*angle))/s.pi
    record(g,"small-aperture exact area below one third",0<area<R(1,3),kind="exact_inequality")
    record(g,"small-aperture large-incident component below three",
           12*area<9,kind="exact_inequality")
    # xi=chi+6 chi_other gives norm sqrt37 and overlap 1.
    record(g,"small-overlap incident over budget",s.sqrt(37)>budget,kind="exact_inequality")
    record(g,"small-overlap component admitted",1/s.sqrt(3)<3,kind="exact_inequality")
    # exp(eta)>1+eta, so q<1000/1423; exact rational comparison suffices.
    record(g,"attenuation rational upper bound below required threshold",
           4*R(1000,1423)**2<3,kind="exact_inequality")
    x0,y0,x1,y1=s.symbols("x0 y0 x1 y1",real=True)
    z0,z1=x0+s.I*y0,x1+s.I*y1
    exact(g,"complex-two-vector norm has four real components",
          z0*s.conjugate(z0)+z1*s.conjugate(z1)-(x0*x0+y0*y0+x1*x1+y1*y1))
    WITNESSES["incident_budget_proof"]=dict(
        premise="Atlas 08: ||Omega||=G |chi^dagger xi| b_n; max component=||Omega||/sqrt3; G,b_n<=1 and ||chi||=1",
        sufficient="||xi||<=3sqrt3",sharpness="theta=pi/2,n=0,xi=(3sqrt3)chi",
        not_necessary="xi=6chi at theta=pi/6; xi=chi+6chi_other at theta=pi/2; xi=6chi at theta=pi/2,n=1",
        dimensional_correction="Two complex entries have four real components, not six.",
        scope="Exact mathematical admission only; numerical evaluation may fail first.")
    return dict(cap=float(cap),star=float(star),budget=float(budget))


def scalar_reference(state,k,strength):
    """Independent component law, not a call to L3, step3 or phase_sync."""
    pre=[(3/5+k[i]/20-abs(z)**2/20)*z+sum(state[j] for j in range(3) if j!=i)/5
         for i,z in enumerate(state)]
    if strength==0:
        return pre
    phases=[0 if z==0 else cmath.phase(z) for z in pre]
    return [0j if z==0 else cmath.rect(abs(z),phases[i]+strength*sum(
        math.sin(3*(phases[j]-phases[i])) for j in range(3) if j!=i))
        for i,z in enumerate(pre)]


def static_audit(repo):
    tree=ast.parse((repo/"kernel_physics"/"operating_region.py").read_text(encoding="utf8"))
    fns={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
    calls=lambda name:[(n.lineno,ast.unparse(n.func)) for n in ast.walk(fns[name]) if isinstance(n,ast.Call)]
    for name in ("initialize_bounded_area","step_bounded_triad","validate_bounded_triad","validate_uniform_incident_budget"):
        WITNESSES.setdefault("source_calls",{})[name]=sorted(calls(name))
    stepcalls=[name for _,name in calls("step_bounded_triad")]
    record("DELEGATION/OWNERSHIP","one step3 call site",
           stepcalls.count("step3")==1,stepcalls,"source_AST")
    names=[name for _,name in calls("initialize_bounded_area")]
    record("DELEGATION/OWNERSHIP","initializer has no optional incident-budget call",
           "validate_uniform_incident_budget" not in names,names,"source_AST")
    ordered=[n.value.func.id for n in fns["initialize_bounded_area"].body
             if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name)]
    record("DELEGATION/OWNERSHIP","initializer source prechecks and actual validation",
           ordered==["_profile","_config","validate_bounded_triad"],ordered,"source_AST")
    # Audit public runner's transitive imports without importing/running it.
    graph={}
    for path in (repo/"kernel_physics").glob("*.py"):
        imports=set()
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8-sig"))):
            if isinstance(node,ast.ImportFrom):
                if node.level==1:
                    imports.update([node.module.split(".")[0]] if node.module else [x.name for x in node.names])
                elif node.module and node.module.startswith("kernel_physics."):
                    imports.add(node.module.split(".")[1])
                elif node.module=="kernel_physics":
                    imports.update(x.name for x in node.names)
            elif isinstance(node,ast.Import):
                imports.update(x.name.split(".")[1] for x in node.names if x.name.startswith("kernel_physics."))
        graph[path.stem]=imports
    for root in ("api","_runner"):
        seen=set();todo=[root]
        while todo:
            nextnode=todo.pop()
            for dependency in graph.get(nextnode,set())-seen:
                seen.add(dependency);todo.append(dependency)
        record("DELEGATION/OWNERSHIP",root+" has no reachable bounded-profile option",
               "operating_region" not in seen,sorted(seen),"source_AST")


def api_checks(repo,refs):
    import numpy as np
    from dataclasses import asdict,FrozenInstanceError
    from unittest.mock import patch
    op=importlib.import_module("kernel_physics.operating_region")
    dy=importlib.import_module("kernel_physics.dynamics")
    sr=importlib.import_module("kernel_physics.srg")
    br=importlib.import_module("kernel_physics.boundary_response")
    num=importlib.import_module("kernel_physics._response_numeric")
    fs=importlib.import_module("kernel_physics.face_state")
    PE=num.ResponsePrecisionError
    pid="triad_eps005_g02_k0to8_radius3_v1"
    config=op.bounded_config(k=[1,2,3],phase_strength=.2)
    validate=lambda state,cfg=config,profile=pid:op.validate_bounded_triad(state,cfg,profile=profile)
    step=lambda state,cfg=config:op.step_bounded_triad(state,cfg,profile=pid)
    initialize=lambda theta,xi,n=0,branch="negative_imag",cfg=config:op.initialize_bounded_area(
        theta,xi,config=cfg,profile=pid,transfer_count=n,branch=branch,response="lens_area_norm_v1")
    record("API_VALIDATION","exact profile identifier",op.PROFILE_ID==pid,op.PROFILE_ID,"API_contract")
    record("API_VALIDATION","stored eps g k and phase",
           asdict(config)==dict(eps=.05,g=.2,k=(1.,2.,3.),phase_strength=.2),
           asdict(config),"API_contract")
    for module in (op,dy,sr,br,num,fs):
        record("API_VALIDATION","authoritative import "+module.__name__,
               Path(module.__file__).resolve().is_relative_to(repo),str(module.__file__),"source_identity")
    for bad in (None,"","default",False,123):
        rejects("profile rejects "+repr(bad),lambda bad=bad:validate([0,0,0],profile=bad),ValueError)
    rejects("profile required keyword",lambda:op.validate_bounded_triad([0,0,0],config),TypeError)
    for cfg in (None,dict(eps=.05,g=.2,k=[1,2,3],phase_strength=0)):
        rejects("config instance required "+repr(cfg),lambda cfg=cfg:validate([0,0,0],cfg),TypeError)
    for eps,g in ((.1,.2),(.05,.3),(np.nextafter(.05,1),.2),(.05,np.nextafter(.2,1))):
        cfg=dy.DynamicsConfig(eps,g,0,(1,1,1))
        rejects(f"stored eps/g exact comparison {eps},{g}",lambda cfg=cfg:validate([0,0,0],cfg),ValueError)
    for k in ([-1,0,0],[0,0,8.000000000000002],[True,1,2],["1",1,2],[1+0j,1,2],
              [math.inf,1,2],[math.nan,1,2],[1,2],[[1,2,3]],np.array([[1],[2],[3]])):
        rejects("strict raw k "+repr(k),lambda k=k:op.bounded_config(k=k,phase_strength=0))
    for strength in (True,np.bool_(True),"0.2",.2+0j,math.inf,math.nan,np.array(.2)):
        rejects("strict raw phase "+repr(strength),lambda strength=strength:op.bounded_config(k=[1,1,1],phase_strength=strength))
    # General config conversion has already erased the original types.
    coerced=dy.DynamicsConfig("0.05","0.2",False,(True,"2",3))
    got=validate([0,0,0],coerced)
    record("API_VALIDATION","stored config accepts already-coerced values",
           np.all(got==0) and coerced.k==(1.,2.,3.) and coerced.phase_strength==0,
           asdict(coerced),"API_contract")
    for bad in ([True,0,0],["1",0,0],[math.nan,0,0],[complex(0,math.inf),0,0],[1,2],[[1,2,3]]):
        rejects("strict state "+repr(bad),lambda bad=bad:validate(bad))
    rejects("one component just over three",lambda:validate([np.nextafter(3.,4.),0,0]),ValueError)
    source=np.array([3,-3j,3]);saved=source.copy();saved_cfg=asdict(config)
    returned=validate(source)
    record("API_VALIDATION","individual moduli equal three accepted",np.array_equal(returned,source),kind="API_contract")
    record("PRECISION/FALSIFIERS","Euclidean norm above three can be admitted",
           np.linalg.norm(returned)>3 and max(abs(returned))==3,dict(norm=float(np.linalg.norm(returned))),"counterexample")
    record("DELEGATION/OWNERSHIP","validation fresh copy and source unchanged",
           not np.shares_memory(returned,source) and np.array_equal(source,saved),kind="API_contract")
    rejects("frozen config cannot be rebound",lambda:setattr(config,"g",.3),FrozenInstanceError)
    # Call order checked with process-local wrappers; no source mutation.
    events=[]
    actual_profile,actual_config,actual_vector=op._profile,op._config,op.complex_vector
    def profile_check(*args):events.append("profile");return actual_profile(*args)
    def config_check(*args):events.append("config");return actual_config(*args)
    def vector_check(*args):events.append("vector");return actual_vector(*args)
    with patch.object(op,"_profile",side_effect=profile_check),patch.object(op,"_config",side_effect=config_check),patch.object(op,"complex_vector",side_effect=vector_check):
        validate([1,0,0])
    record("DELEGATION/OWNERSHIP","state validator profile then config then vector",events==["profile","config","vector"],events,"instrumentation")

    near("API_VALIDATION","uniform budget stored expression",op.UNIFORM_INCIDENT_BUDGET,3*math.sqrt(3),0,0)
    incident=np.array([op.UNIFORM_INCIDENT_BUDGET,0]);budget_return=op.validate_uniform_incident_budget(incident)
    record("API_VALIDATION","uniform equality admitted and copied",np.array_equal(incident,budget_return)
           and not np.shares_memory(incident,budget_return),kind="API_contract")
    rejects("one-ulp budget excess",lambda:op.validate_uniform_incident_budget([np.nextafter(op.UNIFORM_INCIDENT_BUDGET,math.inf),0]),ValueError)
    complex_incident=np.array([1+2j,3+1j])
    budget_complex=op.validate_uniform_incident_budget(complex_incident)
    near("API_VALIDATION","four-real norm witness",math.hypot(1,2,3,1),math.sqrt(15),0,0)
    record("API_VALIDATION","complex incident accepted",np.array_equal(budget_complex,complex_incident),kind="API_contract")
    for bad in ([True,0],["1",0],[1],[1,2,3],[[1,2]],[math.inf,0],[1+math.nan*1j,0]):
        rejects("budget strict incident "+repr(bad),lambda bad=bad:op.validate_uniform_incident_budget(bad))
    modes={branch:sr.helicity_mode(branch).chi for branch in ("negative_imag","positive_imag")}
    examples=[]
    for branch,chi in modes.items():
        xi=op.UNIFORM_INCIDENT_BUDGET*chi
        handoff=initialize(math.pi/2,xi,branch=branch)
        near("EXACT_INCIDENT_BUDGET",branch+" equality initialization",abs(handoff.omega),np.full(3,3.),rtol=3e-15,atol=0)
        record("API_VALIDATION",branch+" equality actual gate",max(math.hypot(z.real,z.imag) for z in handoff.omega)<=3,
               dict(incident_norm=math.hypot(*(v for z in xi for v in (z.real,z.imag))),
                    components=[[float(z.real),float(z.imag)] for z in handoff.omega]),"binary64_witness")
        other=modes["positive_imag" if branch=="negative_imag" else "negative_imag"]
        cases=[("smaller gain",math.pi/6,6*chi,0),
               ("smaller overlap",math.pi/2,chi+6*other,0),
               ("transfer attenuation",math.pi/2,6*chi,1)]
        for label,theta,xi,n in cases:
            norm=math.hypot(*(v for z in xi for v in (z.real,z.imag)))
            with patch.object(op,"validate_uniform_incident_budget",side_effect=AssertionError("optional budget must not be called")):
                result=initialize(theta,xi,n,branch)
            item=dict(branch=branch,case=label,theta=theta,n=n,incident_norm=norm,
                      max_component=max(math.hypot(z.real,z.imag) for z in result.omega))
            examples.append(item)
            record("EXACT_INCIDENT_BUDGET",branch+" admitted over-budget "+label,
                   norm>op.UNIFORM_INCIDENT_BUDGET and item["max_component"]<=3,item,"binary64_witness")
    WITNESSES["large_incident_admitted_examples"]=examples
    rejects("actual over-radius initialization rejected",lambda:initialize(math.pi/2,[10,0]),ValueError)
    rejects("budget-admitted input may fail response precision",lambda:initialize(1e-20,[1e-300,0]),PE,"PRECISION/FALSIFIERS")
    # Exact call order and returning the original HandoffResult, not its validation copy.
    events=[];holder={};actual_handoff=op.handoff_area_response;actual_validate=op.validate_bounded_triad
    def prepared(*args,**kwargs):
        events.append("handoff");holder["result"]=actual_handoff(*args,**kwargs);return holder["result"]
    def admission(*args,**kwargs):
        events.append("actual_state");return actual_validate(*args,**kwargs)
    with patch.object(op,"_profile",side_effect=profile_check),patch.object(op,"_config",side_effect=config_check),patch.object(op,"handoff_area_response",side_effect=prepared),patch.object(op,"validate_bounded_triad",side_effect=admission):
        final=initialize(.3,[1,0])
    record("DELEGATION/OWNERSHIP","initialization call order",
           events==["profile","config","handoff","actual_state","profile","config"],events,"instrumentation")
    record("DELEGATION/OWNERSHIP","initializer returns original immutable receipt",
           final is holder["result"] and not final.omega.flags.writeable,kind="API_contract")
    with patch.object(op,"handoff_area_response",side_effect=AssertionError("must reject config before handoff")):
        rejects("bad config before handoff",lambda:initialize(0,[0,0],cfg=dy.DynamicsConfig(.1,.2,0,(1,1,1))),ValueError)

    for k in ((0,0,0),(8,8,8),(0,8,4)):
        for strength in (0,.2,-.7):
            cfg=op.bounded_config(k=k,phase_strength=strength)
            for label,state in (("extremizer",[refs["star"],3,3]),("mixed",[.6+.2j,-.4+1j,.3j])):
                answer=step(state,cfg)
                near("EXACT_INVARIANCE",f"independent scalar {k} {strength} {label}",answer,scalar_reference(state,k,strength))
                record("EXACT_INVARIANCE",f"one-step component bound {k} {strength} {label}",
                       max(abs(answer))<=refs["cap"]+2e-15,
                       dict(max_component=float(max(abs(answer))),cap=refs["cap"]),"binary64_witness")
                record("DELEGATION/OWNERSHIP",f"same existing step {k} {strength} {label}",
                       np.array_equal(answer,dy.step3(state,cfg)),kind="binary64_witness")
    extrema_cfg=op.bounded_config(k=[8,8,8],phase_strength=.2)
    attained=step([refs["star"],3,3],extrema_cfg)
    near("EXACT_INVARIANCE","attained full-map bound",attained[0].real,refs["cap"],rtol=2e-15,atol=0)
    near("PRECISION/FALSIFIERS","balanced common line expands",step([1,1,1],extrema_cfg),np.full(3,27/20),rtol=2e-15,atol=0)
    near("PRECISION/FALSIFIERS","second interior fixed state",
         step(np.full(3,math.sqrt(8)),extrema_cfg),np.full(3,math.sqrt(8)),rtol=3e-15,atol=0)
    near("PRECISION/FALSIFIERS","plain radius-ten counterexample",
         dy.step3([10,0,0],op.bounded_config(k=[0,0,0],phase_strength=0)),[-44,2,2],0,0)
    rejects("profile rejects radius-ten state",lambda:step([10,0,0]),ValueError)
    unrestricted=dy.DynamicsConfig(.1,.3,0,(9,-1,2))
    record("PRECISION/FALSIFIERS","general dynamics permits other configuration",
           np.all(np.isfinite(dy.step3([4,0,0],unrestricted))),asdict(unrestricted),"counterexample")
    rejects("same config outside optional profile",lambda:validate([0,0,0],unrestricted),ValueError)
    # One call, same config object, detached input, unchanged source bytes/config.
    source=np.array([1+.2j,.3-.4j,-.5j]);saved=source.copy()
    with patch.object(op,"step3",wraps=dy.step3) as delegated:
        answer=step(source)
    record("DELEGATION/OWNERSHIP","wrapper calls existing step3 exactly once",delegated.call_count==1,kind="instrumentation")
    called_state,called_cfg=delegated.call_args.args
    record("DELEGATION/OWNERSHIP","same config and detached state delegated",
           called_cfg is config and not np.shares_memory(called_state,source),kind="instrumentation")
    record("DELEGATION/OWNERSHIP","original state and config unchanged",
           np.array_equal(source,saved) and asdict(config)==saved_cfg,kind="API_contract")
    record("DELEGATION/OWNERSHIP","fresh writable wrapper result",
           answer.flags.writeable and not np.shares_memory(answer,source),kind="API_contract")
    priorerr=np.geterr().copy();seen={}
    def one_call(value,cfg):seen["policy"]=np.geterr().copy();return dy.step3(value,cfg)
    with patch.object(op,"step3",side_effect=one_call):
        step(source)
    record("DELEGATION/OWNERSHIP","all four floating exceptions enabled during call",
           seen["policy"]==dict(divide="raise",over="raise",under="raise",invalid="raise"),seen,"instrumentation")
    record("DELEGATION/OWNERSHIP","errstate restored on success",np.geterr()==priorerr,kind="API_contract")
    for label,mocked in (("escaped",np.array([np.nextafter(3.,4.),0,0])),
                         ("nonfinite",np.array([math.nan,0,0])),
                         ("infinite",np.array([math.inf,0,0])),
                         ("subnormal",np.array([5e-320+0j,0,0]))):
        with patch.object(op,"step3",return_value=mocked) as delegated:
            exc=rejects("output "+label+" rejected without clipping",lambda:step(source),PE,"PRECISION/FALSIFIERS")
        record("DELEGATION/OWNERSHIP","mocked "+label+" still only one call",delegated.call_count==1,kind="instrumentation")
        if label=="subnormal":
            record("PRECISION/FALSIFIERS","output error attributed after step",
                   exc is not None and str(exc).startswith("bounded step output") and exc.__cause__ is None,
                   str(exc),"API_contract")
    failure=FloatingPointError("Atlas09 deliberate step failure")
    with patch.object(op,"step3",side_effect=failure):
        exc=rejects("delegated numerical error wrapped",lambda:step(source),PE,"PRECISION/FALSIFIERS")
    record("PRECISION/FALSIFIERS","step error cause retained",exc is not None and exc.__cause__ is failure
           and str(exc).startswith("existing step3 numerical failure"),str(exc),"API_contract")
    record("DELEGATION/OWNERSHIP","errstate restored after failure",np.geterr()==priorerr,kind="API_contract")
    with patch.object(op,"step3",side_effect=AssertionError("invalid input reached recurrence")):
        rejects("over-radius state fails before delegation",lambda:step([4,0,0]),ValueError)
    tinycfg=op.bounded_config(k=[1,1,1],phase_strength=0)
    tiny=[1e-154,0,0]
    record("PRECISION/FALSIFIERS","tiny state passes admission",
           np.array_equal(validate(tiny,tinycfg),tiny),kind="API_contract")
    plain=dy.step3(tiny,tinycfg)
    record("PRECISION/FALSIFIERS","plain tiny step can be finite",np.all(np.isfinite(plain)),kind="binary64_witness")
    exc=rejects("admitted exact-small state underflow is not escape",lambda:step(tiny,tinycfg),PE,"PRECISION/FALSIFIERS")
    record("PRECISION/FALSIFIERS","tiny failure names square",
           exc is not None and "underflow encountered in square" in str(exc),str(exc),"API_contract")
    zero=step([0,0,0],tinycfg)
    record("API_VALIDATION","exact zero remains canonical",
           np.all(zero==0) and not np.signbit(zero.real).any() and not np.signbit(zero.imag).any(),kind="API_contract")
    huge=op.bounded_config(k=[1,1,1],phase_strength=1e308)
    rejects("finite huge phase may overflow",lambda:step([1,np.exp(1j*math.pi/3),np.exp(1j*math.pi/3)],huge),PE,"PRECISION/FALSIFIERS")
    # Phase strength changes phases, then later coupled magnitudes, while first moduli agree.
    cfg0=op.bounded_config(k=[1,2,3],phase_strength=0)
    cfg1=op.bounded_config(k=[1,2,3],phase_strength=.2)
    first0,first1=step(source,cfg0),step(source,cfg1)
    near("EXACT_INVARIANCE","first phase stage preserves moduli",abs(first0),abs(first1))
    gap=float(max(abs(abs(step(first0,cfg0))-abs(step(first1,cfg1)))))
    record("PRECISION/FALSIFIERS","phase strength affects later coupled magnitudes",gap>1e-4,
           dict(second_step_modulus_gap=gap),"counterexample")
    # FaceState interface only: preserve canonical Omega; no encode/decode feedback.
    view=fs.FaceState(source);view_omega=view.omega.tobytes();view_vectors=view.vectors.tobytes()
    with patch.object(fs,"encode_from_faces",side_effect=AssertionError("derived face vectors must not feed back")):
        with patch.object(op,"step3",wraps=dy.step3) as delegated:
            with patch.object(op,"step_bounded_triad",wraps=op.step_bounded_triad) as bounded:
                next_view=view.step(config,profile=pid)
    record("DELEGATION/OWNERSHIP","FaceState explicit profile delegates once each",
           delegated.call_count==1 and bounded.call_count==1,kind="instrumentation")
    record("DELEGATION/OWNERSHIP","FaceState canonical one-step bytes",
           next_view.omega.tobytes()==dy.step3(source,config).tobytes(),kind="binary64_witness")
    record("DELEGATION/OWNERSHIP","FaceState old snapshots immutable",
           view.omega.tobytes()==view_omega and view.vectors.tobytes()==view_vectors
           and not next_view.omega.flags.writeable and not next_view.vectors.flags.writeable,kind="API_contract")
    with patch.object(op,"step_bounded_triad",side_effect=AssertionError("plain branch must not select profile")):
        with patch.object(dy,"step3",wraps=dy.step3) as delegated:
            plain_view=view.step(config)
    record("DELEGATION/OWNERSHIP","FaceState default stays plain",delegated.call_count==1
           and np.array_equal(plain_view.omega,next_view.omega),kind="instrumentation")
    for profile in (False,"unknown"):
        rejects("FaceState invalid explicit profile "+repr(profile),lambda profile=profile:view.step(config,profile=profile),ValueError)
    with patch.object(fs,"_decode",side_effect=PE("Atlas09 deliberate post-step decode failure")):
        with patch.object(op,"step3",wraps=dy.step3) as delegated:
            rejects("post-step face decode can fail",lambda:view.step(config,profile=pid),PE,"PRECISION/FALSIFIERS")
    record("DELEGATION/OWNERSHIP","post-decode failure retains old canonical snapshot",
           delegated.call_count==1 and view.omega.tobytes()==view_omega and view.vectors.tobytes()==view_vectors,
           kind="instrumentation")
    return {m.__name__:dict(path=str(Path(m.__file__).resolve()),sha256=sha(m.__file__)) for m in (op,dy,sr,br,num,fs)}


def sources(repo):
    names=["operating_region.py","dynamics.py","srg.py","boundary_response.py","_response_numeric.py",
           "face_state.py","readouts.py","README.md","_runner.py","api.py",
           "K0_KERNEL_DEFINITION_LEDGER_v0.1.md",
           "tests/test_operating_region.py","tests/test_boundary_pipeline.py","tests/test_face_state.py",
           "tests/test_runner_records.py","tests/test_import_boundaries.py"]
    paths=[repo/"kernel_physics"/n for n in names]
    note=repo.parent/"research"/"GPT_proof"
    paths += [note/n for n in ["TOY_MODEL_SPECIFICATION_AND_PROOF_CATALOGUE_v0.1.md",
                              "CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md",
                              "CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md",
                              "CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md",
                              "CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md",
                              "GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md"]]
    prior=Path(r"C:\Users\Notandi\.codex\reports")
    paths += [prior/"TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md",
              prior/"TRIOCTAGON_ATLAS_08_BOUNDARY_SRG_HANDOFF_SOURCE_PACKET_v0.1.md",
              prior/"TRIOCTAGON_ATLAS_08_EXACT_RESULTS.json"]
    return {str(p):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in paths if p.is_file()}


def test_inventory(repo):
    inventory={}
    for name in ("test_operating_region.py","test_boundary_pipeline.py","test_face_state.py","test_runner_records.py"):
        rel="kernel_physics/tests/"+name;p=repo/rel
        result=subprocess.run(["git","--no-optional-locks","-C",str(repo),"ls-files","--error-unmatch",rel],capture_output=True)
        inventory[rel]=dict(path=str(p),present=p.is_file(),sha256=sha(p) if p.is_file() else None,
                            tracked=result.returncode==0)
    return inventory


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--scratch",type=Path,required=True)
    parser.add_argument("--integrity-directory",type=Path)
    parser.add_argument("--test-receipt",type=Path)
    args=parser.parse_args()
    repo=args.repo or next((p for p in [Path.cwd(),*Path.cwd().parents]
                           if (p/"kernel_physics"/"operating_region.py").is_file()),DEFAULT_REPO)
    repo=repo.resolve()
    if not (repo/"kernel_physics"/"operating_region.py").is_file():
        parser.error("--repo must contain current kernel_physics/operating_region.py")
    try:
        output=external(args.output,repo);scratch=external(args.scratch,repo)
        if output.exists() or args.output.is_symlink():
            parser.error("Refusing to overwrite --output; choose a new external filename")
        if output==scratch or output in scratch.parents:
            parser.error("--output must be a file distinct from scratch directory")
    except ValueError as exc:
        parser.error(str(exc))
    scratch.mkdir(parents=True,exist_ok=True)
    run=Path(tempfile.mkdtemp(prefix="atlas09_",dir=scratch))
    output.parent.mkdir(parents=True,exist_ok=True)
    bytecode_flag=sys.dont_write_bytecode;sys.dont_write_bytecode=True
    os.environ.update(PYTHONDONTWRITEBYTECODE="1",TEMP=str(run),TMP=str(run),
                      MPLCONFIGDIR=str(run/"mpl"),XDG_CACHE_HOME=str(run/"cache"))
    sys.path.insert(0,str(repo))
    before=sources(repo)
    head=subprocess.check_output(["git","--no-optional-locks","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    result=dict(schema="TRIOCTAGON_ATLAS_09_EXACT_RESULTS/0.1",
                created_utc=datetime.now(timezone.utc).isoformat(),repo=str(repo),
                head=head,expected_head=EXPECTED_HEAD,head_matches=head==EXPECTED_HEAD,
                checker_sha256=sha(__file__),scratch=str(run),command=sys.argv,
                python=sys.version,executable=sys.executable,launched_with_bytecode_disabled=bytecode_flag,
                sources=before,test_inventory=test_inventory(repo),
                historical_runtime_caveat="Atlas 07/08 Windows anomaly remains OPEN; not investigated by this checker.")
    try:
        refs=independent_math()
        static_audit(repo)
        result["imported_sources"]=api_checks(repo,refs)
        import numpy,sympy
        result["versions"]=dict(numpy=numpy.__version__,sympy=sympy.__version__)
    except Exception:
        result["unexpected_exception"]=traceback.format_exc()
    result["scientific_checks"]=CHECKS
    result["counts_by_group"]=dict(Counter(v["group"] for v in CHECKS))
    result["counts_by_kind"]=dict(Counter(v["kind"] for v in CHECKS))
    result["scientific_summary"]=dict(total=len(CHECKS),passed=sum(v["passed"] for v in CHECKS),
                                      failed=sum(not v["passed"] for v in CHECKS))
    result["witnesses"]=WITNESSES
    result["source_files_unchanged_during_checker"]=before==sources(repo)
    result["integrity"]=integrity_receipt(args.integrity_directory)
    result["focused_tests"]=read_test_receipt(args.test_receipt)
    success=not result.get("unexpected_exception") and bool(CHECKS) and all(v["passed"] for v in CHECKS)
    result["scientific_status"]="PASS" if success else "FAIL"
    result["status"]=result["scientific_status"]
    if success and result["focused_tests"]["status"]=="PASS_WITH_RUNTIME_CAVEAT":
        result["status"]="PASS_WITH_RUNTIME_CAVEAT"
    if result["focused_tests"]["status"]=="REVIEW":
        result["status"]="REVIEW"
    if not result["source_files_unchanged_during_checker"] or head!=EXPECTED_HEAD or result["integrity"]["status"]=="FAIL":
        result["status"]="FAIL"
    result["completed_utc"]=datetime.now(timezone.utc).isoformat()
    with output.open("x",encoding="utf8",newline="\n") as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write("\n")
    print(json.dumps(dict(status=result["status"],summary=result["scientific_summary"],output=str(output))))
    return 0 if result["status"] in ("PASS","PASS_WITH_RUNTIME_CAVEAT") else 1


if __name__=="__main__":
    raise SystemExit(main())
