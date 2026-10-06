"""Exact identities and two numerical witnesses for the reciprocal hierarchy.
Writes only beside this script. It does not modify or import repository code.
"""
from pathlib import Path
import json, sys, hashlib, subprocess
import sympy as S
import mpmath as mp

ROOT = Path(__file__).resolve().parent
REPO = Path('C:/TORMENT/TRIOCTAGON_new/trioctagon-physics')
sys.stdout.reconfigure(encoding='utf-8')
baseline_path = ROOT / 'integrity_baseline.json'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def protected():
    paths = []
    for relative in ['papers/three_way_reconstruction', 'kernel_physics', 'apps/scientific_ui']:
        paths += [p for p in (REPO / relative).rglob('*') if p.is_file()]
    return {str(p.relative_to(REPO)): sha(p) for p in sorted(paths)}

if not baseline_path.exists():
    baseline_path.write_text(json.dumps({
        'head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
        'status': subprocess.check_output(['git','status','--short'],cwd=REPO,text=True),
        'files': protected(),
    }, indent=2), encoding='utf-8')

A,B,C,D,y,u,z,v,p,q,r,s,w = S.symbols('A B C D y u z v p q r s w')
checks=[]
def eq(name, expression):
    passed = S.cancel(expression) == 0
    checks.append({'name':name,'passed':passed})
    assert passed,name
def yes(name, passed):
    checks.append({'name':name,'passed':bool(passed)})
    assert passed,name

polys={
    2:A*y**2-B*y+1,
    3:A*y**3-B*y**2-C*y+1,
    4:A*y**4-B*y**3-C*y**2-D*y+1,
}
for n,N in polys.items():
    Q=S.expand(y**n*N.subs(y,1/y));F=N/Q
    W=S.expand(S.diff(N,y)*Q-N*S.diff(Q,y))
    eq(f'n={n} reciprocal',F.subs(y,1/y)*F-1)
    eq(f'n={n} critical reversal',y**(2*n-2)*W.subs(y,1/y)-W)
    eq(f'n={n} plus lock numerator',(N-Q).subs(y,1))
    eq(f'n={n} minus-one parity',(N-(-1)**n*Q).subs(y,-1))
    eq(f'n={n} discriminant reversal',S.discriminant(N,y)-S.discriminant(Q,y))

N=polys[3];Q=y**3-C*y**2-B*y+A
a=B-A*C;b=C-A*B;c=3*(A*A-1)+B*B-C*C;h=A*A-1
q2=a*y*y+b*y+h
q1=b*y*y+(h+B*B-C*C)*y+b
q0=h*y*y+b*y+a
E=q2*u*u+q1*u+q0
eq('cubic difference factorization',N.subs(y,u)*Q-N*Q.subs(y,u)-(u-y)*E)
eq('cubic critical polynomial',S.diff(N,y)*Q-N*S.diff(Q,y)-(a*(y**4+1)+2*b*(y**3+y)+c*y*y))
eq('cubic +1 factor',N-Q-(y-1)*((A-1)*(y*y+y+1)+(C-B)*y))
eq('cubic -1 factor',N+Q-(y+1)*((A+1)*(y*y-y+1)-(B+C)*y))
H=A*A+A*C-B-1
eq('cubic resultant',S.resultant(N,Q,y)-(A-B-C+1)*(A+B-C-1)*H**2)
eq('cubic zero discriminant',S.discriminant(N,y)-(-27*A*A+18*A*B*C+4*A*C**3+4*B**3+B*B*C*C))
pp=A+B-C-1;qq=3*A-3-B+C;rr=3*A+3+B+C;ss=A+1-B-C
yy=(1+z)/(1-z)
eq('cubic Cayley normal form',S.cancel(((N-Q)/(N+Q)).subs(y,yy))-z*(pp*z*z+qq)/(rr*z*z+ss))
eq('cubic Cayley cancellation determinant',pp*ss-qq*rr+8*H)
eq('cubic cyclic coefficient equation',9*pp*ss-qq*rr+8*(3*A*C+B*B-3*B-C*C))
eq('Cayley normalization hyperplane',rr+ss-pp-qq-8)
wn=p*z**3+q*z;wd=r*z*z+s
K=p*(r*z*z+s)*v*v+(p*s-q*r)*z*v+s*(p*z*z+q)
eq('Cayley residual quadratic',wn.subs(z,v)*wd-wn*wd.subs(z,v)-(v-z)*K)
J=p*r*z**4+(3*p*s-q*r)*z*z+q*s
eq('Cayley critical polynomial',S.diff(wn,z)*wd-wn*S.diff(wd,z)-J)
eq('Cayley critical discriminant',S.discriminant(J,z)-16*p*q*r*s*(p*s-q*r)**2*(9*p*s-q*r)**2)
Delta=-4*p*p*r*s*z**4+(q*q*r*r-6*p*q*r*s-3*p*p*s*s)*z*z-4*p*q*s*s
eq('cubic closure discriminant',S.discriminant(K,v)-Delta)
eq('closure quartic discriminant',S.discriminant(Delta,z)-256*p**3*q*r*s**3*(p*s-q*r)**6*(9*p*s-q*r)**2)
branch=-4*r**3*s*w**4+(q*q*r*r+18*p*q*r*s-27*p*p*s*s)*w*w-4*p*q**3
eq('cubic branch polynomial',S.discriminant(wn-w*wd,z)-branch)
eq('cyclic closure square',Delta.subs(q,9*p*s/r)+4*p*p*s/r*(r*z*z-3*s)**2)
aa,kap=S.symbols('aa kap',nonzero=True)
ww=wn/wd
# On qr=9ps, a^2=3s/r, kappa=3pa/r. Substitute s=ra^2/3.
cyc=S.cancel(ww.subs({q:3*p*aa*aa,s:r*aa*aa/3}))
eq('cyclic cubic coordinate', (cyc-3*p*aa/r)/(cyc+3*p*aa/r)-((z-aa)/(z+aa))**3)

N4=polys[4];Q4=y**4-D*y**3-C*y*y-B*y+A
H4=A**3+A*A*C-A*A+A*B*D-2*A*C-A*D*D-A-B*B+B*D+C+1
eq('quartic resultant',S.resultant(N4,Q4,y)-(A-B-C-D+1)*(A+B-C+D+1)*H4**2)
eq('quartic +1 factor',N4-Q4-(y*y-1)*((A-1)*(y*y+1)+(D-B)*y))
eq('quartic -1 polynomial',N4+Q4-((A+1)*(y**4+1)-(B+D)*(y**3+y)-2*C*y*y))
a4=B-A*D;b4=2*C*(1-A);c4=-3*A*B+B*C-C*D+3*D;d4=4*A*A+2*B*B-2*D*D-4
W4=a4*(y**6+1)+b4*(y**5+y)+c4*(y**4+y*y)+d4*y**3
eq('quartic critical polynomial',S.diff(N4,y)*Q4-N4*S.diff(Q4,y)-W4)
tau=S.symbols('tau')
crit_reduced=a4*tau**3+b4*tau**2+(c4-3*a4)*tau+d4-2*b4
eq('quartic critical reciprocal reduction',W4-y**3*crit_reduced.subs(tau,y+1/y))
# Compact Bezout formula covers the requested quartic correspondence without expansion.
coeff=S.Poly(N4,y).all_coeffs()[::-1];rev=list(reversed(coeff))
E4=0
for i in range(5):
    for j in range(i):
        E4+=(coeff[i]*rev[j]-coeff[j]*rev[i])*(u*y)**j*sum(u**(i-j-1-k)*y**k for k in range(i-j))
eq('quartic residual cubic Bezout formula',N4.subs(y,u)*Q4-N4*Q4.subs(y,u)-(u-y)*E4)
F4=N4/Q4
eq('quartic decomposable subfamily',F4.subs({B:0,D:0})-(A*y**4-C*y*y+1)/(y**4-C*y*y+A))
special=S.cancel(F4.subs({A:-1,B:0,D:0}))
eq('quartic V4 deck minus',special.subs(y,-y)-special)
eq('quartic V4 deck inversion i',special.subs(y,S.I/y)-special)

# Cancellation at a fixed reciprocal point can reverse its continued lock value.
for name,NN,QQ,point,expected in [
    ('odd cancellation at +1',2*y**3-y*y-2*y+1,y**3-2*y*y-y+2,1,-1),
    ('odd cancellation at -1',2*y**3-y+1,y**3-y*y+2,-1,1),
    ('even cancellation at +1',2*y**3-3*y*y+1,y**3-3*y+2,1,1),
]: eq(name,S.cancel(NN/QQ).subs(y,point)-expected)

# Exact witnesses establish nonempty generic open sets for n=3 and n=4.
mp.mp.dps=100
witnesses=[]
for n,sub in [(3,{A:2,B:3,C:5}),(4,{A:2,B:3,C:5,D:7})]:
    NN=polys[n].subs(sub);QQ=S.expand(y**n*NN.subs(y,1/y))
    WW=S.expand(S.diff(NN,y)*QQ-NN*S.diff(QQ,y))
    VV=S.discriminant(NN-w*QQ,y)
    yes(f'n={n} witness no cancellation',S.resultant(NN,QQ,y)!=0)
    yes(f'n={n} witness simple critical points',S.degree(WW,y)==2*n-2 and S.discriminant(WW,y)!=0)
    yes(f'n={n} witness distinct branch values',S.degree(VV,w)==2*n-2 and S.discriminant(VV,w)!=0)
    roots=S.nroots(WW,n=85,maxsteps=300)
    f=S.lambdify(y,NN/QQ,'mpmath');wf=S.lambdify(y,WW,'mpmath');nf=S.lambdify(y,NN,'mpmath')
    crit=[mp.mpc(str(S.re(t)),str(S.im(t))) for t in roots]
    vals=[f(t) for t in crit]
    probes=[mp.mpc('0.37','0.29'),mp.mpc('-1.7','0.4'),mp.mpc('2.2','-0.8')]
    reciprocity_error=max(abs(f(1/t)*f(t)-1) for t in probes)
    residual=max(abs(wf(t))/(1+sum(abs(mp.mpf(str(c))*t**i) for i,c in enumerate(S.Poly(WW,y).all_coeffs()[::-1]))) for t in crit)
    yes(f'n={n} numerical reciprocity residual',reciprocity_error<mp.mpf('1e-90'))
    yes(f'n={n} numerical critical residual',residual<mp.mpf('1e-75'))
    witnesses.append({'n':n,'parameters':{str(k):int(v) for k,v in sub.items()},
        'critical_polynomial':str(WW),'critical_discriminant':str(S.discriminant(WW,y)),
        'branch_polynomial':str(S.factor(VV)),'branch_discriminant':str(S.discriminant(VV,w)),
        'max_reciprocity_error':mp.nstr(reciprocity_error,12),
        'max_normalized_critical_residual':mp.nstr(residual,12),
        'minimum_branch_separation':mp.nstr(min(abs(a-b) for i,a in enumerate(vals) for b in vals[i+1:]),12),
        'critical_points':[mp.nstr(t,35) for t in crit],
        'critical_values':[mp.nstr(t,35) for t in vals]})

exact_count=sum('numerical' not in c['name'] for c in checks)
result={'python':sys.version,'sympy':S.__version__,'mpmath':mp.__version__,
        'working_precision':100,'root_precision':85,'exact_checks':exact_count,
        'numerical_checks':len(checks)-exact_count,'checks':checks,'witnesses':witnesses,
        'generic_genus':{str(n):int(1+S.factorial(n)*(n-3)/2) for n in [2,3,4]}}
(ROOT/'verification_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
base=json.loads(baseline_path.read_text())
yes('protected files unchanged',protected()==base['files'])
yes('repository HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()==base['head'])
yes('repository status unchanged',subprocess.check_output(['git','status','--short'],cwd=REPO,text=True)==base['status'])
(ROOT/'integrity_result.json').write_text(json.dumps({'protected_files':len(base['files']),
    'protected_files_unchanged':True,'head_unchanged':True,'status_unchanged':True},indent=2),encoding='utf-8')
print(json.dumps({'exact_checks':exact_count,'numerical_checks':result['numerical_checks'],
    'protected_files':len(base['files']),'witnesses':witnesses},indent=2))
