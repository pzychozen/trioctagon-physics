"""Bounded symbolic verification: the two intermediate-chart involutions.
No parameter scans; no repository writes or production imports.
"""
from pathlib import Path
import hashlib,json,subprocess
import sympy as sp

ROOT=Path(__file__).resolve().parent
REPO=Path("C:/TORMENT/TRIOCTAGON_new/trioctagon-physics").resolve()
assert not ROOT.is_relative_to(REPO)
def status():
    return {"head":subprocess.check_output(["git","-C",str(REPO),"rev-parse","HEAD"],text=True).strip(),
            "status":subprocess.check_output(["git","-C",str(REPO),"status","--porcelain=v1"],text=True)}
before=status()
L,y,u,h,s=sp.symbols("L y u h s")
N=lambda v:L*v*v-L*v+1
D=lambda v:v*v-L*v+L
F=lambda v:N(v)/D(v)
T=lambda v:((L+1)*v-L)/(L*v-(L+1))
R=lambda v:-v/(1+h*v)
J=lambda v:(h*v+2)/(v-h)
Q=lambda v:-v+h*(1+h*v)**2
P=lambda v:(v*v+2+2*h*v+h*h*v*v)/Q(v)
W=lambda v:-v-2/v
checks={
"level_set_factorization":N(u)*D(y)-N(y)*D(u)-(L-1)*(u-y)*((L+1)*(u+y)-L*(u*y+1)),
"finite_y_involution":T(T(y))-y,
"finite_y_value_preservation":F(T(y))-F(y),
"chart_original_inversion":(1/(1+h*s)-1)/h-R(s),
"chart_original_inversion_square":R(R(s))-s,
"original_inversion_output":P(R(s))-P(s)/(-1+h*P(s)),
"chart_same_value_involution":(T(1+h*s).subs(L,h**-2)-1)/h-J(s),
"chart_same_value_square":J(J(s))-s,
"chart_same_value_preservation":P(J(s))-P(s),
"finite_involutions_commute":R(J(s))-J(R(s)),
"finite_delta_transform":(T(1+y)-1)-(y+2)/(L*y-1),
"original_inversion_limit":sp.limit(R(s),h,0)+s,
"same_value_involution_limit":sp.limit(J(s),h,0)-2/s,
"same_value_first_correction":sp.limit((J(s)-2/s)/h,h,0)-(1+2/s**2),
"limiting_same_value_symmetry":W(2/s)-W(s),
"unshifted_limit_involution_finite_error":sp.limit((P(2/s)-P(s))/h,h,0)-(2/s**2-s*s/2),
"limiting_original_oddness":W(-s)+W(s),
"profile_derivative":sp.diff(P(s),s)-(1-h*h)*(2+2*h*s-s*s)/Q(s)**2,
"involution_derivative":sp.diff(J(s),s)+(h*h+2)/(s-h)**2,
"fixed_point_polynomial":(J(s)-s)*(s-h)+(s*s-2*h*s-2),
"limit_stationary_derivative":sp.diff(W(s),s)-(-1+2/s**2),
"positive_stationary_value":W(sp.sqrt(2))+2*sp.sqrt(2),
"negative_stationary_value":W(-sp.sqrt(2))-2*sp.sqrt(2)
}
for name,expr in checks.items():
    assert sp.cancel(expr)==0,name
c=sp.sqrt(2+h*h)
for point in [h-c,h+c]:
    assert sp.simplify(point*point-2*h*point-2)==0
    assert sp.simplify(sp.diff(J(s),s).subs(s,point)+1)==0
after=status()
assert before==after
result={"scope":"Symbolic algebra only; no parameter scans.",
"symbolic_checks_passed":list(checks),
"fixed_points_and_derivative_checked":True,
"repository_before":before,"repository_after":after,"repository_unchanged":True,
"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
"sympy_version":sp.__version__}
(ROOT/"intermediate_involution_results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({"checks":len(checks),"fixed_point_checks":"PASS","repository_unchanged":True,
"original_R":str(R(s)),"same_value_J":str(J(s)),"result":"PASS"}))
