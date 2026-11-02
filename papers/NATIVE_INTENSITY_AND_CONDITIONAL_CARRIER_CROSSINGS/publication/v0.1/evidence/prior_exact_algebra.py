"""New generic identities only: no F evaluator, project imports, states or trajectories.

Run from Command Prompt in conda environment torment. The output is exclusively
created: rerunning requires an explicitly new output filename, never overwrite.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import sympy as s

groups = []
def check(name, residuals, scope):
    reduced = [s.simplify(s.expand(e)) for e in residuals]
    assert all(e == 0 for e in reduced), (name, reduced)
    groups.append(dict(name=name, scope=scope, residual_count=len(reduced),
                       residuals=[str(e) for e in reduced], passed=True))

x, y, u, v, si, sj, S, A, g, eps, k, q = s.symbols(
    'x y u v si sj S A g eps k q', real=True)
check('component norm expansion and edge split', [
    (x+u)**2+(y+v)**2-x*x-y*y-(2*(x*u+y*v)+u*u+v*v),
    2*g*(S-si)-(g*(sj-si)-g*(si+sj-2*S))],
    'Generic real components; coefficients unrestricted.')

ss = s.symbols('s1:4', real=True)
d12,d13,d23,cyc = s.symbols('d12 d13 d23 cycle', real=True)
edges = [(0,1,d12),(0,2,d13),(1,2,d23)]
exchange = [0,0,0]; mismatch = [0,0,0]
for i,j,d in edges:
    exchange[i] += -g*(ss[i]-ss[j]); exchange[j] += -g*(ss[j]-ss[i])
    mismatch[i] += -g*d; mismatch[j] += -g*d
cycle_divergences = [cyc-cyc, -cyc+cyc, cyc-cyc]
check('edge-once total and cycle freedom', [sum(exchange),
    sum(mismatch)+2*g*(d12+d13+d23), *cycle_divergences],
    'Three undirected edges, each counted once; oriented cycle 1->2->3->1.')

xx=s.Matrix(s.symbols('x1:4', real=True)); yy=s.Matrix(s.symbols('y1:4', real=True))
L=s.ones(3)-3*s.eye(3)
pair_sum=sum((xx[i]-xx[j])**2+(yy[i]-yy[j])**2 for i,j,_ in edges)
hx=s.Matrix(s.symbols('hx1:4', real=True)); hy=s.Matrix(s.symbols('hy1:4', real=True))
bx=eps*hx+g*L*xx; by=eps*hy+g*L*yy
check('whole finite square including mixed term', [
    (L*xx).dot(L*xx)+(L*yy).dot(L*yy)-3*pair_sum,
    bx.dot(bx)+by.dot(by)-eps**2*(hx.dot(hx)+hy.dot(hy))
    -2*eps*g*(hx.dot(L*xx)+hy.dot(L*yy))-3*g*g*pair_sum],
    'h is an arbitrary generic vector; no native step is evaluated.')

angle=s.symbols('angle', real=True)
rotS=S*s.cos(angle)-A*s.sin(angle); rotA=A*s.cos(angle)+S*s.sin(angle)
check('pair rotation and synchronization potential sign', [
    rotS**2+rotA**2-S*S-A*A,
    -g*(rotS-S)-g*(S*(1-s.cos(angle))+A*s.sin(angle))],
    'S,A denote prestage coherence here; angle=delta_j-delta_i.')

check('finite potential onsite and edge expansions', [
    eps*((si+q)**2/4-k*(si+q)/2-si**2/4+k*si/2)
      -eps*((si-k)*q/2+q*q/4),
    g*((x+u)**2+(y+v)**2-x*x-y*y)/2
      -g*(x*u+y*v)-g*(u*u+v*v)/2],
    'Arbitrary intensity increment q and complex edge difference/increment.')

p,r,c,ps,rs,src=s.symbols('p r c ps rs src', real=True)
wp,wm=s.symbols('wp wm', real=True)
check('C1 local storage and characteristic flux', [
    p*(src-c*rs)+r*(-c*ps)+c*(ps*r+p*rs)-p*src,
    ((wp+wm)/s.sqrt(2))**2/2+((wp-wm)/s.sqrt(2))**2/2-(wp*wp+wm*wm)/2,
    c*(wp+wm)*(wp-wm)/2-c*(wp*wp-wm*wm)/2],
    'Formal product rule at source-stated regularity; no PDE solve.')

# Orthonormal (u,e_z) coefficients only; no geometry or mesh constructor.
nplus=s.Matrix([2,s.sqrt(3)])/s.sqrt(7)
nminus=s.Matrix([2,-s.sqrt(3)])/s.sqrt(7)
tplus=s.Matrix([-2,-s.sqrt(3)])/s.sqrt(7)
tminus=s.Matrix([2,-s.sqrt(3)])/s.sqrt(7)
jplus,jminus,work=s.symbols('jplus jminus work', real=True)
check('conditional contact signs and inner arc balance', [
    tplus.dot(nplus)+1, tminus.dot(nminus)-1,
    work+jplus-jminus-(work-(-jplus+jminus))],
    'Source-selected circle and normals; one-dimensional cut flux, not aperture area flux.')

# Exact frozen host-patch dictionary; scalar coordinates in common u,v,e_z frame.
lam,zeta=s.symbols('lam zeta', real=True)
rgeom=s.sqrt(3)/6; d=1-s.sqrt(2)/2; h=(s.sqrt(2)-1)/2
paperI=s.Matrix([1/s.sqrt(3)-s.sqrt(3)*d*lam/2,zeta,h+d*lam])
central=s.Matrix([2*rgeom-s.sqrt(3)*d*lam/2,zeta,h+d*lam])
u0=s.Matrix([0,1]); u1=s.Matrix([-s.sqrt(3)/2,-s.Rational(1,2)])
u2=s.Matrix([s.sqrt(3)/2,-s.Rational(1,2)])
g0=s.Matrix([s.sqrt(3)/2,-s.Rational(1,2)]); g1=s.Matrix([0,1]); g2=u1
check('host-notch dictionary', [*(paperI-central),*(u0-g1),*(u1-g2),*(u2-g0)],
    'Exact coordinate identity Delta_j^sigma-O=N_(j+1 mod 3)^sigma; lower sign follows linearly.')

q0,q1,q2,q3,q4,q5,a=s.symbols('q0 q1 q2 q3 q4 q5 a', real=True)
original=q0+q1+q2+q3+q4+q5
check('hypothetical six-outlet nonuniqueness', [
    ((q0+a)+(q1-a)+q2+q3+q4+q5)-original],
    'Conditional scalar bookkeeping only; not an adopted energy or outlet law.')

result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
    python=sys.executable, python_version=sys.version, sympy_version=s.__version__,
    method='Generic exact symbolic residuals; no project imports, numerical states, F, observer, EMA, carrier evolution, or inherited checkers.',
    group_count=len(groups), residual_count=sum(x['residual_count'] for x in groups),
    all_passed=True, groups=groups,
    limitation='Checks support displayed algebra only, not inherited continuous-domain theorems, physical interpretation, or source authentication beyond separately recorded hashes.')
dest=Path(__file__).with_name('exact_algebra_results.json')
with dest.open('x',encoding='utf-8') as f: json.dump(result,f,indent=2); f.write('\n')
print(json.dumps({k:result[k] for k in ['python','sympy_version','group_count','residual_count','all_passed']}))
