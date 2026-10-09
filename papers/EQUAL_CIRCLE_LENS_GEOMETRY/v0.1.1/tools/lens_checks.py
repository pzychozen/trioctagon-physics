"""Paper-only verification; transcribed mathematics, no project-runtime imports."""
from pathlib import Path
import sys, os, json, platform, hashlib
import sympy as s
import mpmath as mp
mp.mp.dps=90
OUT=Path(__file__).resolve().parents[1]/"evidence"
records=[]
def record(name,kind,passed,detail):
    records.append(dict(id=name,kind=kind,passed=bool(passed),detail=detail))
def zero(name,expr):
    reduced=s.simplify(s.trigsimp(s.expand_trig(expr)))
    record(name,"symbolic identity",reduced==0,{"residual":str(reduced)})
def limit(name,expr,var,point,expected,dir="+"):
    value=s.simplify(s.limit(expr,var,point,dir=dir))
    record(name,"limit",s.simplify(value-expected)==0,{"evaluated":str(value),"expected":str(expected)})
def close(name,value,expected,tol="1e-65"):
    error=abs(value-expected)
    record(name,"numerical illustration",error<mp.mpf(tol),
           {"value":mp.nstr(value,75),"expected":mp.nstr(expected,75),"absolute_residual":mp.nstr(error,12),"tolerance":tol})
t,r,u,e=s.symbols("theta r u epsilon",positive=True,real=True)
P=4*r*t
A=r*r*(2*t-s.sin(2*t))
J=A/P**2
Jp=s.cos(t)*(s.sin(t)-t*s.cos(t))/(4*t**3)
f=u-s.sin(s.pi*u)/s.pi
zero("L01.arc_speed_squared",(s.diff(r*s.cos(t),t))**2+(s.diff(r*s.sin(t),t))**2-r*r)
for end,pp,aa in [(0,0,0),(s.pi/2,2*s.pi*r,s.pi*r*r)]:
    zero("L01.P_endpoint_"+str(end),P.subs(t,end)-pp)
    zero("L01.A_endpoint_"+str(end),A.subs(t,end)-aa)
for tv in ["0.02","0.6","1.2"]:
    rv=mp.mpf("1.7");tv=mp.mpf(tv);dv=2*rv*mp.cos(tv)
    area=4*mp.quad(lambda x:mp.sqrt(rv*rv-x*x),[dv/2,rv])
    close("L01.independent_area_integral_"+str(tv),area,rv*rv*(2*tv-mp.sin(2*tv)))
zero("L02.normalization",A.subs(t,s.pi*u/2)/(s.pi*r*r)-f)
zero("L02.derivative",s.diff(f,u)-(1-s.cos(s.pi*u)))
zero("L02.cubic_series",s.series(f,u,0,7).removeO()-(s.pi**2*u**3/6-s.pi**4*u**5/120))
limit("L02.inverse_absolute",u*u/s.diff(f,u),u,0,2/s.pi**2)
zero("L03.J_derivative",s.diff(J,t)-Jp)
zero("L03.h_derivative",s.diff(s.sin(t)-t*s.cos(t),t)-t*s.sin(t))
limit("L03.J_tangent",J,t,0,0)
zero("L03.J_disk",J.subs(t,s.pi/2)-1/(4*s.pi))
P1=P.subs({r:s.Rational(1,2),t:s.pi/3});A1=A.subs({r:s.Rational(1,2),t:s.pi/3})
P2=P.subs({r:s.Rational(1,3),t:s.pi/2});A2=A.subs({r:s.Rational(1,3),t:s.pi/2})
zero("L03.equal_P",P1-P2)
record("L03.unequal_A","exact witness",s.simplify(A2-A1).is_positive,
       {"A1":str(A1),"A2":str(A2),"difference":str(s.simplify(A2-A1)),
        "proof_note":"Strict positivity also follows from J monotonicity at pi/3<pi/2 and equal positive P."})
matrix=s.Matrix([P,A]).jacobian([r,t])
zero("L04.jacobian",matrix.det()-16*r*r*s.cos(t)*(s.sin(t)-t*s.cos(t)))
JA=1/P**2;JP=-2*A/P**3;TA=JA/Jp;TP=JP/Jp;K=J/(t*Jp)
limit("L04.det_tangent",matrix.det()/t**3,t,0,16*r*r/3)
limit("L04.det_disk",matrix.det().subs(t,s.pi/2-e)/e,e,0,16*r*r)
zero("L04.J_series",s.series(J,t,0,7).removeO()-(t/12-t**3/60+t**5/630))
limit("L04.JA_tangent",JA*t*t,t,0,1/(16*r*r))
limit("L04.JP_tangent",JP,t,0,-1/(24*r))
limit("L04.thetaA_tangent",TA*t*t,t,0,3/(4*r*r))
limit("L04.thetaP_tangent",TP,t,0,-1/(2*r))
limit("L04.K_tangent",K,t,0,1)
limit("L04.disk_quadratic",(1/(4*s.pi)-J.subs(t,s.pi/2-e))/e**2,e,0,1/s.pi**3)
limit("L04.disk_Jp",Jp.subs(t,s.pi/2-e)/e,e,0,2/s.pi**3)
limit("L04.K_disk",e*K.subs(t,s.pi/2-e),e,0,s.pi/4)
pp,aa=s.symbols("P A",positive=True)
zero("L04.absolute_area_partial",s.diff(aa/pp**2,aa)-1/pp**2)
zero("L04.absolute_perimeter_partial",s.diff(aa/pp**2,pp)+2*aa/pp**3)
zero("L04.relative_area_coefficient",(aa*s.diff(aa/pp**2,aa))/(aa/pp**2)-1)
zero("L04.relative_perimeter_coefficient",(pp*s.diff(aa/pp**2,pp))/(aa/pp**2)+2)

def Jmp(x):
    return (2*x-mp.sin(2*x))/(16*x*x) if x else mp.mpf(0)
def inverse(p,a):
    """Exact-model, paper-only mp scalar demonstration; no clipping/fitting.

    Finite precision evaluates inequalities in the current mp context. A caller
    with uncertain boundary data must supply an error model, not a tolerance here.
    """
    p,a=mp.mpf(p),mp.mpf(a)
    if not mp.isfinite(p) or not mp.isfinite(a) or p<0 or a<0:raise ValueError("finite nonnegative data required")
    if p==0 and a==0:return {"branch":"tangent_nonidentifiable"}
    if p<=0 or a<=0 or a>p*p/(4*mp.pi):raise ValueError("outside exact lens data image")
    if a==p*p/(4*mp.pi):
        return {"branch":"coincident","theta":mp.pi/2,"r":p/(2*mp.pi),"d":mp.mpf(0)}
    target=a/p**2;lo=mp.mpf(0);hi=mp.pi/2
    for _ in range(280):
        mid=(lo+hi)/2
        if Jmp(mid)<target:lo=mid
        else:hi=mid
    theta=(lo+hi)/2;radius=p/(4*theta)
    return {"branch":"interior","theta":theta,"r":radius,"d":2*radius*mp.cos(theta),"bracket":(lo,hi)}
for k,(rv,tv) in enumerate([(mp.mpf("0.5"),mp.pi/3),(mp.mpf("4"),mp.mpf("0.00000001")),
                            (mp.mpf("1.3"),mp.pi/2-mp.mpf("0.000001"))]):
    pv=4*rv*tv;av=rv**2*(2*tv-mp.sin(2*tv));out=inverse(pv,av)
    for var,expected in [("theta",tv),("r",rv),("d",2*rv*mp.cos(tv))]:
        close(f"L03.inverse_{k}_{var}",out[var],expected,"1e-60")
pv=mp.mpf(7);disk=inverse(pv,pv*pv/(4*mp.pi))
close("L03.inverse_disk_theta",disk["theta"],mp.pi/2)
close("L03.inverse_disk_radius",disk["r"],pv/(2*mp.pi))
close("L03.inverse_disk_separation",disk["d"],mp.mpf(0))
record("L03.tangent_branch","exact witness",inverse(0,0)["branch"]=="tangent_nonidentifiable",inverse(0,0))
bad=[(-1,1),(1,-1),(0,1),(1,0),(1,1),(mp.inf,1),(1,mp.nan)]
rejected=[]
for pair in bad:
    try:inverse(*pair)
    except ValueError:rejected.append(tuple(map(str,pair)))
record("L03.domain_rejection","numerical illustration",len(rejected)==len(bad),{"rejected":rejected,"expected_cases":len(bad)})
# Exact complex tensor and nontrivial linear readout witness.
fv=s.Rational(2,5);xi=s.Matrix([1+2*s.I,-3+s.I]);f0=s.ones(3,1)/s.sqrt(3)
v=s.kronecker_product(xi,f0);psi=s.sqrt(fv)*v
norm=lambda x:(s.conjugate(x).T*x)[0]
zero("L05.tensor_norm",norm(psi)-fv*norm(xi))
B=s.Matrix([[1,s.I,0,0,2,0],[0,0,1,1,0,-s.I]])
zero("L05.linear_intensity",norm(B*psi)-fv*norm(B*v))
record("L05.nonzero_multiplier","exact witness",s.simplify(norm(B*v)).is_positive,{"m":str(s.simplify(norm(B*v)))})
zero("L05.unknown_multiplier_witness",s.Rational(1,4)*4-s.Rational(1,2)*2)
zero("L05.zero_multiplier",norm(s.zeros(2,6)*psi))
separation_weight=s.exp(-(2*r)**2/(4*r*r))
record("L06.gaussian_not_area","exact witness",s.simplify(separation_weight).is_positive,
       {"Gaussian_at_tangency":str(separation_weight),"area_fraction_at_tangency":str(f.subs(u,0))})
OUT.mkdir(exist_ok=True)
result={"task":"PUB-LT-01","role":"New isolated manuscript support; not theorem totals, independent review, or kernel certification",
        "versions":{"python":sys.version,"executable":sys.executable,"platform":platform.platform(),
                    "sympy":s.__version__,"mpmath":mp.__version__,"mp_dps":mp.mp.dps,"conda_env":os.environ.get("CONDA_DEFAULT_ENV")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "counts":{"total":len(records),"passed":sum(x["passed"] for x in records),"failed":sum(not x["passed"] for x in records)},
        "checks":records}
(OUT/"CHECK_RESULTS.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(result["counts"]))
for x in records:
    if not x["passed"]:print(json.dumps(x))
raise SystemExit(0 if all(x["passed"] for x in records) else 1)
