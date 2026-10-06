"""Exact V4 quotient and chart checks; no scans or repository mutations."""
from pathlib import Path
import json,hashlib,subprocess
import sympy as sp
ROOT=Path(__file__).resolve().parent
REPO=Path("C:/TORMENT/TRIOCTAGON_new/trioctagon-physics").resolve()
assert not ROOT.is_relative_to(REPO)
def status():
    return {"head":subprocess.check_output(["git","-C",str(REPO),"rev-parse","HEAD"],text=True).strip(),
            "status":subprocess.check_output(["git","-C",str(REPO),"status","--porcelain=v1"],text=True)}
before=status()
L=sp.symbols("L",positive=True)
y,u,v,z,eta,tau,s,h=sp.symbols("y u v z eta tau s h",nonzero=True)
a=sp.sqrt(2*L+1); k=2*(L-1)/a; b=k*k
N=lambda y:L*y*y-L*y+1
D=lambda y:y*y-L*y+L
F=lambda y:N(y)/D(y)
T=lambda y:((L+1)*y-L)/(L*y-L-1)
U=lambda y:a*(y-1)/(y+1)
Y=lambda u:(a+u)/(a-u)
q=lambda y:4*((L+1)*(y*y+1)-2*L*y)**2/((2*L+1)*(y*y-1)**2)
qu=lambda u:(u+1/u)**2
C=4*(L+1)**2/(2*L+1)
checks={
"cayley_inverse":U(Y(u))-u,
"R_normal_form":U(1/y)+U(y),
"T_normal_form":U(T(y))-1/U(y),
"F_normal_form":F(Y(u))-(u+1/u+k)/(u+1/u-k),
"quotient_normal_form":q(Y(u))-qu(u),
"quotient_R_invariant":q(1/y)-q(y),
"quotient_T_invariant":q(T(y))-q(y),
"quotient_observable":F(y)+1/F(y)-2*(q(y)+b)/(q(y)-b),
"centered_quotient":q(y)-b-16*N(y)*D(y)/((2*L+1)*(y*y-1)**2),
"quotient_derivative":sp.diff(qu(u),u)-2*(u**2-1)*(u**2+1)/u**3,
"branch_u_1":qu(sp.Integer(1))-4,
"branch_u_i":qu(sp.I),
"axis_quotient":q(0)-C,
"axis_quotient_derivative":sp.diff(q(y),y).subs(y,0)+16*L*(L+1)/(2*L+1),
"axis_minus_zero_pole_level":C-b-16*L/(2*L+1),
"x_V4_quotient_factor":q(y)-4*((L+1)*(y+1/y)-2*L)**2/((2*L+1)*((y+1/y)**2-4)),
"zero_pole_threshold":b-4-4*L*(L-4)/(2*L+1),
"bulk_quotient_limit":sp.limit(q(y)/(2*L),L,sp.oo)-((y-1)/(y+1))**2,
"lock_quotient_limit":sp.limit(q(1+tau/L)/(2*L),L,sp.oo)-1/tau**2,
"intermediate_quotient_limit":sp.limit(q(1+h*s).subs(L,h**-2),h,0)-(s+2/s)**2/2,
"inner_centered_quotient_limit":sp.limit(q(z/L)-b,L,sp.oo)-8*(1-z),
"outer_centered_quotient_limit":sp.limit(q(L*eta)-b,L,sp.oo)-8*(1-1/eta),
"bulk_to_lock_coordinate":sp.limit(L*(T(y)-1),L,sp.oo)-(y+1)/(y-1),
"inner_T_exact_lock_coordinate":L*(T(z/L)-1)+(L+z)/(L+1-z),
"outer_T_exact_lock_coordinate":L*(T(L*eta)-1)-(L*eta+1)/(L*eta-1-1/L),
"inner_outer_quotient_match":8*(1-1/eta)-8*(1-z).subs(z,1/eta),
"inner_origin_orbit":T(0)-L/(L+1),
"outer_infinity_orbit":sp.limit(T(y),y,sp.oo)-(L+1)/L
}
for name,expression in checks.items():
    assert sp.cancel(expression)==0,name
# Degree and simple-zero/pole evidence for the non-rational x lift.
x=sp.symbols("x")
num,den=sp.fraction(sp.cancel(T(x*x)))
assert sp.degree(num,x)==2 and sp.degree(den,x)==2
assert sp.discriminant(num,x)!=0 and sp.discriminant(den,x)!=0
assert sp.factor(sp.resultant(num,den,x))!=0
after=status()
assert before==after
result={"scope":"Exact algebra and requested chart limits only; no parameter scans.",
"checks_passed":list(checks),"nonrational_x_lift_evidence_checked":True,
"repository_before":before,"repository_after":after,"repository_unchanged":True,
"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
"sympy_version":sp.__version__}
(ROOT/"V4_quotient_results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({"result":"PASS","symbolic_checks":len(checks),
"repository_unchanged":True,"quotient":"(u+1/u)^2","branch_values":[0,4,"infinity"]}))
