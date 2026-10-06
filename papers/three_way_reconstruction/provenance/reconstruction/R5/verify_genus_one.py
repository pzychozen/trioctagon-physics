"""Exact, bounded verification for the Three-Way genus-one report.
Run with Python plus SymPy and mpmath. Writes only its sibling results file.
"""
from pathlib import Path
import json
import sympy as s
from mpmath import mp

t, a, x, z, U, V, n, L = s.symbols("t a x z U V n L")
checks = {}

def check(name, expr):
    checks[name] = s.factor(s.cancel(expr)) == 0
    if not checks[name]:
        raise AssertionError(name)

P = t*x*x*z*z-x*x-z*z+t
ed = U*U+V*V-1-a**4*U*U*V*V
check("Edwards transformation",
      P.subs({t:a*a, x:a*U, z:a*V}, simultaneous=True)+a*a*ed)
check("constant section (1,i)", P.subs({x:1,z:s.I}))
w2=(t*x*x-1)*(x*x-t)
check("quartic equation", w2-(t*x**4-(t*t+1)*x*x+t))
check("quartic from biquadratic",
      (t*x*x-1)**2*z*z-w2-(t*x*x-1)*P)
check("Jacobi quartic",w2/t-(x**4-(t+1/t)*x*x+1))

q=(1-a*a)/(1+a*a)
ell=q*(x-a)/(x+a)
m=q*q
kappa=2*s.I*a*(a*a-1)/(a*a+1)**2
check("Legendre transformation",
      ell*(ell-1)*(ell-m)-kappa*kappa*w2.subs(t,a*a)/(x+a)**4)
check("Legendre inverse",a*(q+ell)/(q-ell)-x)
for name,point,value in [("a",a,0),("minus reciprocal a",-1/a,1),
                         ("reciprocal a",1/a,m)]:
    check("Legendre branch "+name,ell.subs(x,point)-value)

alpha=2*(1+t*t)/(1-t*t)
gamma=4/(1-t*t)
Mx=(1+V)/(1-V)
Mw=Mx/U
mont_res=s.together(gamma*Mw**2-(Mx**3+alpha*Mx**2+Mx))
check("Montgomery substitution",
      mont_res.subs(U**2,(1-V*V)/(1-t*t*V*V)))
check("Montgomery inverse V",(Mx-1)/(Mx+1)-V)
check("Montgomery inverse U",Mx/Mw-U)
check("Montgomery parameter nu",alpha.subs(t*t,1-1/n)-(4*n-2))
j_t=16*(t**4+14*t*t+1)**3/(t*t*(t*t-1)**4)
j_n=16*(16*n*n-16*n+1)**3/(n*(n-1))
j_l=256*(1-L+L*L)**3/(L*L*(1-L)**2)
check("j Legendre",j_l.subs(L,((t-1)/(t+1))**2)-j_t)
check("j Montgomery",256*(alpha*alpha-3)**3/(alpha*alpha-4)-j_t)
check("j nu",j_n.subs(n,1/(1-t*t))-j_t)
check("j t sign",j_t.subs(t,-t)-j_t)
check("j t reciprocal",j_t.subs(t,1/t)-j_t)
check("j nu reflection",j_n.subs(n,1-n)-j_n)
check("j 1728 factor t",j_t-1728-
      16*(t*t+1)**2*(t*t-6*t+1)**2*(t*t+6*t+1)**2/
      (t*t*(t*t-1)**4))
check("j 1728 factor nu",j_n-1728-
      16*(2*n-1)**2*(32*n*n-32*n-1)**2/(n*(n-1)))

al=4*n-2
p=1-al*al/3
qshort=2*al**3/27-al/3
check("Weierstrass discriminant",-16*(4*p**3+27*qshort**2)-256*n*(n-1))
check("Weierstrass j",-1728*4*p**3/( -16*(4*p**3+27*qshort**2)/16)-j_n)
Xp=x+al+1/x
check("two-isogeny",(x**3+al*x*x+x)*(1-1/x**2)**2-
      (Xp**3-2*al*Xp**2+(al*al-4)*Xp))
check("isogenous cubic roots",
      x**3-2*al*x*x+(al*al-4)*x-x*(x-4*n)*(x-4*(n-1)))

check("boundary t0",P.subs(t,0)+(x+s.I*z)*(x-s.I*z))
check("boundary t1",P.subs(t,1)-(x*x-1)*(z*z-1))
check("boundary t-1",P.subs(t,-1)+(x*x+1)*(z*z+1))
check("boundary t infinity",x*x*z*z+1-(x*z-s.I)*(x*z+s.I))
check("group X",P.subs(x,-x)-P)
check("group Y",P.subs(z,-z)-P)
check("group S",P.subs({x:z,z:x},simultaneous=True)-P)
check("group C",x*x*z*z*P.subs({x:1/x,z:1/z},simultaneous=True)-P)
check("translation P",P.subs({x:z,z:-x},simultaneous=True)-P)
beta=(x**4-2*t*x*x+1)**2/((1-t*t)*(x**4-1)**2)
other=beta.subs(x,z)
check("beta swap",
      s.together(other-beta).subs(z**4,((x*x-t)/(t*x*x-1))**2)
      .subs(z**2,(x*x-t)/(t*x*x-1)))

phi=(1+s.sqrt(5))/2
tp=s.simplify((1-phi)/(1+phi))
check("phi t",tp-(2-s.sqrt(5)))
check("phi nu",1/(1-tp*tp)-(s.Rational(1,2)+s.sqrt(5)/4))
check("phi m",((tp-1)/(tp+1))**2-phi**2)
check("phi j",j_t.subs(t,tp)-2048)
for A,B,expected in [
    (9,9,s.Rational(8780093172522724,263900025)),
    (9,1,s.Rational(5927735656804,2401490025))]:
    check(f"exact j {A},{B}",j_t.subs(t,s.Rational(B,A+1))-expected)

mp.dps=100
ph=(1+mp.sqrt(5))/2
examples=[]
for label,A,B in [
    ("(9,9)",mp.mpf(9),mp.mpf(9)),
    ("(9,1)",mp.mpf(9),mp.mpf(1)),
    ("(pi,e)",mp.pi,mp.e),
    ("(phi,1-phi)",ph,1-ph)]:
    tv=B/(A+1)
    nv=1/(1-tv*tv)
    mv=((tv-1)/(tv+1))**2
    jt=16*(tv**4+14*tv*tv+1)**3/(tv*tv*(tv*tv-1)**4)
    jn=16*(16*nv*nv-16*nv+1)**3/(nv*(nv-1))
    jl=256*(1-mv+mv*mv)**3/(mv*mv*(1-mv)**2)
    err=max(abs(jn-jt),abs(jl-jt))/max(1,abs(jt))
    examples.append(dict(pair=label,**{key:mp.nstr(val,85) for key,val in
                    [("t",tv),("nu",nv),("m",mv),("j",jt),
                     ("max_relative_identity_error",err)]}))
    assert err<mp.mpf("1e-90")

result=dict(symbolic_checks=len(checks),all_passed=all(checks.values()),
            checks=checks,decimal_precision=mp.dps,examples=examples)
out=Path(__file__).with_name("verification_results.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(symbolic_checks=len(checks),all_passed=True,
      max_relative_identity_error=max(float(e["max_relative_identity_error"]) for e in examples),
      output=str(out)),indent=2))
