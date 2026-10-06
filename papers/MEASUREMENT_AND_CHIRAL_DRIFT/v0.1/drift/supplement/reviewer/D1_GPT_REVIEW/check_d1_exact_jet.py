"""Independent substitution audit of the displayed D1 jet, through eta^3.

Uses the original two-stage map, not Codex's verifier. Exact coefficients
are in Q(sqrt(3))(h), with separate real and imaginary series components.
This checks the formula in the report; it does not replay interval certificates.
"""
from __future__ import annotations
import json
import time
from pathlib import Path
import sympy as s

start = time.time()
h = s.Symbol('h', real=True)
K = s.QQ.algebraic_field(s.sqrt(3)).frac_field(h)
Z, O = K.zero, K.one
H = K.from_sympy(h)
Q = lambda a,b=1: K.from_sympy(s.Rational(a,b))
rt3=K.from_sympy(s.sqrt(3))
DEG=3

def scalar(x=0):
    return [K.from_sympy(s.sympify(x))] + [Z]*DEG

def add(a,b): return [x+y for x,y in zip(a,b)]
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def scale(a,c): return [x*c for x in a]
def mul(a,b):
    return [sum((a[j]*b[n-j] for j in range(n+1)), Z) for n in range(DEG+1)]
def power(a,n):
    out=scalar(1)
    for _ in range(n): out=mul(out,a)
    return out

def ca(a,b): return (add(a[0],b[0]),add(a[1],b[1]))
def cs(a,b): return ca(a,(neg(b[0]),neg(b[1])))
def cm(a,b): return (sub(mul(a[0],b[0]),mul(a[1],b[1])), add(mul(a[0],b[1]),mul(a[1],b[0])))
def cscale(a,c): return (scale(a[0],c),scale(a[1],c))
def conj(a): return (a[0],neg(a[1]))
def cpow(a,n):
    out=(scalar(1),scalar())
    for _ in range(n): out=cm(out,a)
    return out

def cexpi(t):
    assert t[0] == Z
    return (sub(scalar(1),scale(power(t,2),Q(1,2))), sub(t,scale(power(t,3),Q(1,6))))

def norm2(a): return add(mul(a[0],a[0]),mul(a[1],a[1]))
def unit_cube(a):
    norm=norm2(a)
    assert norm[0]==O
    x=sub(norm,scalar(1))
    inv=scalar(1)
    for n in range(1,4):
        inv=add(inv,scale(power(x,n), K.from_sympy(s.binomial(-s.Rational(3,2),n))))
    p3=cpow(a,3)
    return (mul(p3[0],inv),mul(p3[1],inv))

# Coefficients transcribed from D1 report section 3, kept distinct from
# the independently implemented map above and below.
d=H*3-O
P=108*H**3+27*H**2+828*H-760
Qp=54*H**3-270*H**2-261*H+592
U=972*H**5+2025*H**4+12744*H**3+96570*H**2+132*H+64568
W=972*H**5-8667*H**4+112212*H**3-521514*H**2+98412*H-206440
u1=-(3*H+2)/d
v1=rt3*(3*H-10)/(3*d)
u2edge=-P/(6*d**3)
u2mid=-Qp/(3*d**3)
v2edge=-rt3*(3*H-10)*(45*H-68)/(2*d**3)
u3edge=-U/(6*d**5)
v3edge=rt3*W/(18*d**5)
nu3=-rt3*(33*H**2-240*H+688)/(3*d**3)
ws=[
    ([O,u1,u2edge,u3edge],[Z,v1,v2edge,v3edge]),
    ([O,Z,u2mid,Z],[Z,-2*v1,Z,-2*v3edge]),
    ([O,-u1,u2edge,-u3edge],[Z,v1,-v2edge,v3edge])]
ks=[ [O,Q(-1),Z,Z], scalar(1), [O,O,Z,Z] ]
nu=[Z,Z,Z,nu3]

# Original amplitude/coupling step in z_i = (1/sqrt2) q_i w_i.
ps=[]
for i in range(3):
    onsite=sub(ks[i],scale(norm2(ws[i]),Q(1,2)))
    coupling=cscale(ws[i],Q(-2))
    for j in range(3):
        if j==i: continue
        sign=1 if (j-i)%3==1 else -1
        turn=(scalar(-s.Rational(1,2)),[sign*rt3/2,Z,Z,Z])
        coupling=ca(coupling,cm(turn,ws[j]))
    a=ca((mul(ws[i][0],onsite),mul(ws[i][1],onsite)),cscale(coupling,Q(1,6)))
    ps.append(ca(ws[i],cscale(a,H)))

# Original synchronizer evaluated at its actual prestage, then rotate
# comparison state by h*nu. q_i^3=1 removes reference phases in sine(3dphi).
unit=[unit_cube(p) for p in ps]
kicks=[]
for i in range(3):
    di=scalar()
    for j in range(3):
        if j!=i: di=add(di,cm(unit[j],conj(unit[i]))[1])
    kicks.append(scale(di,Q(1,30)))

checks=[]
for i in range(3):
    rr=cs(cm(ps[i],cexpi(scale(kicks[i],H))),cm(ws[i],cexpi(scale(nu,H))))
    for part in range(2):
        for n in range(DEG+1):
            ok=(rr[part][n]==Z)
            checks.append({'name':f'native_residual_site_{i}_{"re" if part==0 else "im"}_eta{n}', 'pass':bool(ok)})
            if not ok: print('NONZERO',i,part,n,K.to_sympy(rr[part][n]),flush=True)
for n in range(4):
    checks.append({'name':f'gauge_eta{n}','pass': bool(sum((w[1][n] for w in ws),Z)==Z)})
coef=s.sqrt(3)*(33*h**2-240*h+688)/(3*(1-3*h)**3)
checks += [
 {'name':'nu3_equals_displayed_formula','pass': bool(s.simplify(K.to_sympy(nu3)-coef)==0)},
 {'name':'generator_coefficient','pass': bool(s.simplify(coef.subs(h,0)-688*s.sqrt(3)/3)==0)},
 {'name':'h_derivative','pass': bool(s.simplify(s.diff(coef,h).subs(h,0)-1984*s.sqrt(3))==0)}
]
report={'audit':'Independent exact substitution of D1 displayed cubic jet into original native equations',
        'domain':'formal eta jet; rational h away from h=1/3; report supplies analytic extension at h=0',
        'checked_degree':3,'checks':checks,'passed':sum(x['pass'] for x in checks),
        'total':len(checks),'elapsed_seconds':time.time()-start,
        'nu3':str(coef),'not_done':'No replay of D1 verifier or interval certificates; no new branch/parameter investigation.'}
Path(__file__).with_name('exact_jet_check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['passed','total','elapsed_seconds','nu3']},indent=2))
assert all(x['pass'] for x in checks)
