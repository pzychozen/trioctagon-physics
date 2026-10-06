"""External exact checks for the cubic correspondence; no repository imports/writes."""
from pathlib import Path
import json, hashlib, subprocess, sys
import sympy as S
import mpmath as mp

ROOT=Path(__file__).resolve().parent
REPO=Path('C:/TORMENT/TRIOCTAGON_new/trioctagon-physics')
sys.stdout.reconfigure(encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def protected():
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=REPO).decode().split('\0')
    files={REPO/p for p in tracked if p}
    for rel in ['papers/three_way_reconstruction','kernel_physics','apps/scientific_ui']:
        files.update(p for p in (REPO/rel).rglob('*') if p.is_file())
    return {str(p.relative_to(REPO)):sha(p) if p.is_file() else None for p in sorted(files)}
baseline=ROOT/'integrity_baseline.json'
if not baseline.exists():
    baseline.write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
        'status':subprocess.check_output(['git','status','--short'],cwd=REPO,text=True),
        'files':protected()},indent=2),encoding='utf-8')

checks=[]
def eq(name,expr):
    ok=S.cancel(expr)==0
    checks.append({'name':name,'passed':ok});assert ok,name
def yes(name,ok):
    checks.append({'name':name,'passed':bool(ok)});assert ok,name

p,q,r,s,z,v,w,t,h,a,b,eta,x,Y,al,be,ga=S.symbols('p q r s z v w t h a b eta x Y al be ga')
U=p*s;V=q*r;beta=V**2-6*U*V-3*U**2
alpha=-4*p*p*r*s;gamma=-4*p*q*s*s
D=alpha*z**4+beta*z*z+gamma
I=beta*beta+12*alpha*gamma;J=72*alpha*beta*gamma-2*beta**3
Delta=alpha*gamma*(beta*beta-4*alpha*gamma)**2/16
eq('quartic discriminant vs elliptic discriminant',S.discriminant(D,z)-256*Delta)
eq('elliptic discriminant factor',Delta-p**3*q*r*s**3*(p*s-q*r)**6*(9*p*s-q*r)**2)
eq('c4 c6 discriminant',(I**3-(J/2)**2)/1728-Delta)
eq('factored c4',I-(V+3*U)*(V**3-15*U*V**2+75*U**2*V+3*U**3))

# A simple branch point a is the origin. Eliminate gamma using f(a)=0.
f=al*z**4+be*z*z+ga
fa=S.diff(f,z).subs(z,a);faa=S.diff(f,z,2).subs(z,a)
X=fa/(4*(z-a))+faa/24
ysq=fa**2*f/(64*(z-a)**4)
ii=be**2+12*al*ga;jj=72*al*be*ga-2*be**3
expr=ysq-X**3+ii*X/48+jj/1728
eq('quartic to short Weierstrass',expr.subs(ga,-al*a**4-be*a*a))
eq('inverse z transformation',a+fa/(4*(X-faa/24))-z)
eq('selected 2-torsion x coordinate',-fa/(8*a)+faa/24+be/6)
eq('2-torsion Weierstrass root',(-be/6)**3-ii*(-be/6)/48-jj/1728)
eq('shifted 2-torsion model',(x-be/6)**3-ii*(x-be/6)/48-jj/1728-(x**3-be*x*x/2+(be*be-4*al*ga)*x/16))

# Legendre map with O=(a,0), other roots -a,b,-b.
ff=al*(z*z-a*a)*(z*z-b*b)
c=(b-a)/(b+a);L=c*(z+a)/(z-a);m=c*c
k2=-4*a*a*c*c/(al*(a+b)**2)
eq('quartic Legendre transformation',k2*ff/(z-a)**4-L*(L-1)*(L-m))
eq('Legendre inverse',a*(L+c)/(L-c)-z)
bb=-al*(a*a+b*b);gg=al*a*a*b*b
eq('Legendre j vs quartic j',256*(1-m+m*m)**3/(m*m*(1-m)**2)-16*(bb*bb+12*al*gg)**3/(al*gg*(bb*bb-4*al*gg)**2))

# Natural Montgomery/Edwards transformations after selecting square roots.
AM,UM,VM=S.symbols('AM UM VM')
xe=UM/VM;ye=(UM-1)/(UM+1)
ed=(AM+2)*xe*xe+ye*ye-1-(AM-2)*xe*xe*ye*ye
num=S.together(ed).as_numer_denom()[0]
eq('Montgomery to twisted Edwards',S.rem(S.Poly(num,VM),S.Poly(VM**2-(UM**3+AM*UM**2+UM),VM)).as_expr())
eq('Edwards inverse U',(1+ye)/(1-ye)-UM)
eq('Edwards inverse V',(1+ye)/((1-ye)*xe)-VM)

# Normalize to t=qr/(ps).
H=t*t-6*t-3;Dt=-4*z**4+H*z*z-4*t
It=H*H+192*t;ct=H*(576*t-H*H)
delT=t*(t-1)**6*(t-9)**2
eq('normalized discriminant',(It**3-ct**2)/1728-delT)
eq('normalized c4 factor',It-(t+3)*(t**3-15*t*t+75*t+3))
A4=-It/48;A6=-ct/864
Px=(t+3)**2/12;Py=-(t-1)**2/2
eq('explicit 3-torsion point on Weierstrass',Py**2-Px**3-A4*Px-A6)
slope=(3*Px**2+A4)/(2*Py)
eq('3-torsion doubling x',slope*slope-2*Px-Px)
eq('3-torsion doubling y',slope*(Px-(slope*slope-2*Px))-Py+Py)
eq('3-division polynomial',3*Px**4+6*A4*Px*Px+12*A6*Px-A4*A4)
PX=(V+3*U)**2/12;PY=-U*(V-U)**2/2
eq('general coefficient 3-torsion point',PY**2-PX**3+I*PX/48+J/1728)

# The correspondence algebra gives exact S3 actions.
K=(z*z+1)*v*v+(1-t)*z*v+z*z+t
W=z*(z*z+t)/(z*z+1)
third=W-z-v
def modK(expr):
    num=S.cancel(expr).as_numer_denom()[0]
    return S.rem(S.Poly(num,v,domain=S.QQ.frac_field(t,z)),S.Poly(K,v,domain=S.QQ.frac_field(t,z))).as_expr()
eq('transposition preserves correspondence',modK(K.subs(v,third)))
eq('cycle preserves correspondence',modK(K.subs({z:v,v:third},simultaneous=True)))
eq('second sheet same value',modK(v*(v*v+t)/(v*v+1)-W))
eq('third sheet same value',modK(third*(third*third+t)/(third*third+1)-W))
eq('ordered triple sum',z+v+third-W)
eq('ordered triple pair sum',modK(z*v+v*third+third*z-t))
eq('ordered triple product',modK(z*v*third-W))
eq('residual discriminant',S.discriminant(K,v)-Dt)
eq('eta relation',modK((2*(z*z+1)*v+(1-t)*z)**2-Dt))
eq('reciprocal lift preserves relation',K.subs({z:-z,v:-v},simultaneous=True)-K)
eq('reciprocal lift negates eta',(2*((-z)**2+1)*(-v)+(1-t)*(-z))+(2*(z*z+1)*v+(1-t)*z))

# Identify tau(O) with the explicit 3-torsion point using a critical root b.
T=b*b*(b*b+3)/(b*b-1);aa=2*b/(b*b-1)
fpa=S.diff(Dt,z).subs(z,aa);fppa=S.diff(Dt,z,2).subs(z,aa)
etaP=b*(2*b*b+3-t)
eq('branch origin from critical root',Dt.subs({z:aa,t:T},simultaneous=True))
eq('tau(O) x is P',((fpa/(4*(b-aa))+fppa/24)-Px).subs(t,T))
eq('tau(O) y is P',((-fpa*etaP/(8*(b-aa)**2))-Py).subs(t,T))

# Isogeny and target discriminant curve.
crit=p*r*z**4+(3*p*s-q*r)*z*z+q*s
Fw=z*(p*z*z+q)/(r*z*z+s)
Bw=-4*r**3*s*w**4+(V*V+18*U*V-27*U*U)*w*w-4*p*q**3
eq('target branch discriminant',S.discriminant(p*z**3-w*r*z*z+q*z-w*s,z)-Bw)
eq('explicit 3-isogeny',crit**2*D/(r*z*z+s)**4-Bw.subs(w,Fw))
chi=crit*(2*p*(r*z*z+s)*v+(p*s-q*r)*z)/(r*z*z+s)**2
# normalized Vandermonde expression, with the same sign convention
eq('Vandermonde quotient coordinate',modK((z-v)*(z-third)*(v-third)-(z**4+(3-t)*z*z+t)*(2*(z*z+1)*v+(1-t)*z)/(z*z+1)**2))
Lt=t*t+18*t-27
delPrime=t**3*(t-1)**2*(t-9)**6
Iprime=Lt*Lt+192*t**3
eq('quotient elliptic discriminant',t**3*(Lt*Lt-64*t**3)**2-delPrime)
jE=It**3/delT;jQ=Iprime**3/delPrime
hh=t*(t-9)**2/(t-1)**2
jH=(h+27)*(h+3)**3/h;jHq=(h+27)*(h+243)**3/h**3
eq('X03 source j',jE-jH.subs(h,hh))
eq('X03 quotient j',jQ-jHq.subs(h,hh))
eq('dual 3-isogeny parameter',jH.subs(h,729/h)-jHq)
eq('X03 j1728 factor',jH-1728-(h*h+18*h-27)**2/h)
eq('forget 2-torsion map derivative',S.diff(hh,t)-(t-9)*(t+3)**2/(t-1)**3)
eq('elliptic order-three value',hh+27-(t+3)**3/(t-1)**2)
k=S.symbols('k')
f1=S.together(jH.subs(h,k)-jH).as_numer_denom()[0]
f2=S.together(jHq.subs(h,k)-jHq).as_numer_denom()[0]
gcd=S.gcd(S.Poly(f1,k,domain=S.QQ.frac_field(h)),S.Poly(f2,k,domain=S.QQ.frac_field(h))).monic().as_expr()
eq('oriented j pair generically determines h',gcd-(k-h))

# ABC expressions and preserved exceptional equations.
A,B,C=S.symbols('A B C')
pp=A+B-C-1;qq=3*(A-1)-B+C;rr=3*(A+1)+B+C;ss=A+1-B-C
UU=(A-C)**2-(B-1)**2;VV=(3*A+C)**2-(B+3)**2
HH=A*A+A*C-B-1;KK=3*A*C+B*B-3*B-C*C
eq('U in ABC',pp*ss-UU);eq('V in ABC',qq*rr-VV)
eq('cancellation determinant ABC',VV-UU-8*HH)
eq('cyclic condition ABC',VV-9*UU-8*KK)
eq('X03 parameter in ABC',(VV/UU)*(VV/UU-9)**2/(VV/UU-1)**2-VV*KK**2/(UU*HH**2))
eq('cyclic quartic factor',D.subs(q,9*p*s/r)+4*p*p*s/r*(r*z*z-3*s)**2)
eq('q zero nodal quartic',D.subs(q,0)+p*p*s*z*z*(4*r*z*z+3*s))
eq('r zero nodal quartic',D.subs(r,0)+p*s*s*(3*p*z*z+4*q))
eq('both zero reducible quartic',D.subs({q:0,r:0})+3*p*p*s*s*z*z)
eq('cyclic target branch collision',Bw.subs(q,9*p*s/r)+4*r**3*s*(w*w-27*p*p*s/r**3)**2)

# Riemann-Hurwitz, stated separately from algebraic identities.
yes('S3 closure RH',6*(-2+4*S.Rational(1,2))==0)
yes('C3 quotient RH',0==3*0)
yes('four fixed points of transposition RH',2*(-2)+4==0)
yes('original cubic RH',3*(-2)+4==-2)

# Exact finite-patch comparison. Coordinates are copied as formulas from the
# documented patch parameterization; no kernel is imported or executed.
R=S.Matrix([[-S.Rational(1,2),-S.sqrt(3)/2,0],[S.sqrt(3)/2,-S.Rational(1,2),0],[0,0,1]])
M=S.diag(-1,1,-1);Id=S.eye(3)
yes('patch rotation order 3',R**3==Id);yes('patch halfturn order 2',M*M==Id)
yes('patch S3 conjugation',S.simplify(M*R*M-R**2)==S.zeros(3))
u0=S.Matrix([0,1,0]);v0=S.Matrix([-1,0,0]);ez=S.Matrix([0,0,1])
for j in range(3):
    uj=R**j*u0;vj=R**j*v0
    yes(f'patch radial reflection {j}',S.simplify(M*uj-R**((-j)%3)*u0)==S.zeros(3,1))
    yes(f'patch transverse reflection {j}',S.simplify(M*vj+R**((-j)%3)*v0)==S.zeros(3,1))
states=[(j,sgn) for j in range(3) for sgn in [1,-1]]
def actR(pair):return ((pair[0]+1)%3,pair[1])
def actM(pair):return ((-pair[0])%3,-pair[1])
def Phi(pair):j,sgn=pair;return (j,(j+sgn)%3)
yes('six distinct ordered sheet pairs',len({Phi(s0) for s0 in states})==6)
yes('rotation equivariant incidence',all(Phi(actR(s0))==tuple((i+1)%3 for i in Phi(s0)) for s0 in states))
yes('halfturn equivariant incidence',all(Phi(actM(s0))==tuple((-i)%3 for i in Phi(s0)) for s0 in states))

# Independent numerical substitution in birational/isogeny equations at t=17.
mp.mp.dps=100;tt=mp.mpf(17);HHt=tt*tt-6*tt-3
curve=lambda z0:-4*z0**4+HHt*z0*z0-4*tt
cc=mp.sqrt(7+4*mp.sqrt(2));aaN=2*cc/(cc*cc-1)
fpaN=-16*aaN**3+2*HHt*aaN;fppaN=-48*aaN**2+2*HHt
iN=HHt**2+192*tt;cN=HHt*(576*tt-HHt**2)
probes=[mp.mpc('0.4','0.7'),mp.mpc('1.3','-0.2'),mp.mpc('-0.6','0.8')]
errs=[]
for zz in probes:
    ee=mp.sqrt(curve(zz));xx=fpaN/(4*(zz-aaN))+fppaN/24;yy=-fpaN*ee/(8*(zz-aaN)**2)
    errorW=abs(yy*yy-(xx**3-iN*xx/48-cN/864))
    ww=zz*(zz*zz+tt)/(zz*zz+1);chiN=(zz**4+(3-tt)*zz*zz+tt)*ee/(zz*zz+1)**2
    Bval=-4*ww**4+(tt*tt+18*tt-27)*ww*ww-4*tt**3
    errorQ=abs(chiN*chiN-Bval)
    errs.append({'weierstrass_absolute_residual':mp.nstr(errorW,15),'isogeny_absolute_residual':mp.nstr(errorQ,15)})
    assert errorW<mp.mpf('1e-90') and errorQ<mp.mpf('1e-90')

res={'python':sys.version,'sympy':S.__version__,'mpmath':mp.__version__,
    'exact_checks':len(checks),'checks':checks,'numerical_precision':100,
    'numerical_sample_t':17,'numerical_residuals':errs,
    'normal_form':{'c4':str(It),'c6':str(ct),'Delta':str(delT),
    'X03_parameter':str(hh),'j_source':str(jH),'j_quotient':str(jHq),
    'torsion3_x':str(Px),'torsion3_y':str(Py)},
    'scope':'Exact identities and finite actions; geometric moduli proofs are in the report.'}
(ROOT/'verification_results.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
base=json.loads(baseline.read_text())
assert protected()==base['files']
assert subprocess.check_output(['git','status','--short'],cwd=REPO,text=True)==base['status']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()==base['head']
(ROOT/'integrity_result.json').write_text(json.dumps({'protected_files':len(base['files']),
    'unchanged':True,'head_unchanged':True,'status_unchanged':True},indent=2),encoding='utf-8')
print(json.dumps({'exact_checks':len(checks),'numerical_residuals':errs,'protected_files':len(base['files'])},indent=2))
