"""GM05 exact source-jump and work checks; no production or prior-suite import."""
from pathlib import Path
import sympy as s
import hashlib,json,platform,sys,os,time
ROOT=Path(__file__).resolve().parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
t0=time.time();rows=[]
def zero(x):
    if hasattr(x,'shape'):return all(s.simplify(v)==0 for v in x)
    return s.simplify(x)==0
def ck(name,cond,kind='exact symbolic',detail=None):
    ok=bool(cond);rows.append(dict(name=name,passed=ok,kind=kind,detail=detail))
    if not ok:raise AssertionError(name)
def norm2(v):return s.expand(v.dot(v))
rt=s.sqrt;R=s.Rational
e=s.ones(3,1);I=s.eye(3);P=I-e*e.T/3;Pi=s.diag(1,1,0)
ex,ey,ez=[I[:,i] for i in range(3)]
T=s.Matrix([[-R(1,2),1,-R(1,2)],[-rt(3)/2,0,rt(3)/2],[0,0,0]])
D=R(2,3)*T.T
alpha,beta,L,a=s.symbols('alpha beta L a',real=True)
wx,wy,vx,vy=s.symbols('wx wy vx vy',real=True)
W=s.Matrix([wx,wy,0]);Wp=s.Matrix([vx,vy,0]);dw=Wp-W
jm=alpha*D*W;jp=alpha*D*Wp;dj=alpha*D*dw
ck('L01 T has rank two and common kernel',T.rank()==2 and zero(T*e))
ck('L02 TD is the planar projector',zero(T*D-Pi))
ck('L03 DT is the zero-sum projector',zero(D*T-P))
ck('L04 D metric on the moment plane',zero(D.T*D-R(2,3)*Pi))
ck('L05 full weight family satisfies target',zero(T*(jm+beta*e)-alpha*W))
ck('L06 family is exhaustive',T.nullspace()==[e])
ck('L07 orthogonal storage split',zero(norm2(jm+beta*e)-R(2,3)*alpha**2*norm2(W)-3*beta**2))
ck('L08 unique minimum coefficient',s.diff(L*norm2(jm+beta*e)/2,beta,2)==3*L,
   detail='With L>0 the beta quadratic is strictly convex; minimum beta=0.')
ck('L09 explicit three weights',zero(jm-alpha*s.Matrix([(-wx-rt(3)*wy)/3,2*wx/3,(-wx+rt(3)*wy)/3])))
cc=s.Matrix(s.symbols('cA cB cC',real=True))
ck('L10 lift uses only projected channel area',zero(D*T*cc-(cc-(e.dot(cc)/3)*e)))
ck('L11 z component cannot be represented',zero(D*ez) and zero((T*D)*ez))
err=s.Matrix(s.symbols('eA eB eC',real=True))
jold=jm+err
ck('J01 arbitrary vector mismatch survives jump',zero(jold+dj-jp-err))
ck('J02 aggregate mismatch survives jump',zero(T*(jold+dj)-alpha*Wp-(T*jold-alpha*W)))
ck('J03 increment has zero common mode',zero(e.dot(dj)))
ck('J04 initial match propagates across a jump',zero(jm+dj-jp))
ck('J05 initial common offset is preserved',zero(jm+beta*e+dj-(jp+beta*e)))
ck('J06 minimum norm increment family',zero(norm2(dj+beta*e)-norm2(dj)-3*beta**2))
ck('J07 target reset differs from increment on mismatched data',zero((jp-jold)-dj+err))
ck('J08 resetting common offset removes its stored energy',zero(L*(norm2(jp+beta*e)-norm2(jp))/2-3*L*beta**2/2))
chi=s.symbols('chi',real=True)
q1,q2,q3,h1,h2,h3=s.symbols('q1 q2 q3 h1 h2 h3',real=True)
means=s.Matrix([q1,q2,q3]);shift=s.Matrix([h1,h2,h3])
profiles=means+s.Matrix([s.sin(chi)+2*s.cos(2*chi),s.cos(chi)-s.sin(3*chi),2*s.cos(4*chi)])
mean_of=lambda v:s.integrate(v,(chi,0,2*s.pi))/(2*s.pi)
ck('P01 preprofiles have prescribed means',zero(mean_of(profiles)-means))
ck('P02 uniform jump preserves all zero-mean profiles',zero((profiles+shift)-(means+shift)-(profiles-means)))
work=s.integrate(norm2(profiles+shift)-norm2(profiles),(chi,0,2*s.pi))*L/(4*s.pi)
ck('E01 profile-level energy increment',zero(work-L*(means.dot(shift)+norm2(shift)/2)))
ck('E02 midpoint work identity',zero(L*(means.dot(shift)+norm2(shift)/2)-L*((means+(means+shift))/2).dot(shift)))
ck('E03 matched endpoint mean energy',zero(L*norm2(jm)/2-L*alpha**2*norm2(W)/3))
ck('E04 matched signed energy change',zero(L*(jm.dot(dj)+norm2(dj)/2)-L*alpha**2*(norm2(Wp)-norm2(W))/3))
ck('E05 mismatch work term',zero(L*(jold.dot(dj)+norm2(dj)/2)-L*alpha**2*(norm2(Wp)-norm2(W))/3-L*alpha*err.dot(D*dw)))
ck('E06 common offset does not change jump work',zero(L*((jm+beta*e).dot(dj)+norm2(dj)/2)-L*(jm.dot(dj)+norm2(dj)/2)))
ck('C01 zero change produces zero increment and work',zero(dj.subs({vx:wx,vy:wy})))
ck('C02 full reversal is opposite weights',zero(jm.subs({wx:-wx,wy:-wy})+jm))
flip=-2*jm
ck('C03 reversal between matched endpoints has zero net work',zero(L*(jm.dot(flip)+norm2(flip)/2)))
ck('C04 removal to zero extracts mean energy',zero(L*(jm.dot(-jm)+norm2(jm)/2)+L*alpha**2*norm2(W)/3))
# Reproduce the ordinary native Fourier jump, not a surrogate interpolation.
om=s.Matrix([1,(-1-s.I*rt(3))/2,(-1+s.I*rt(3))/2])
k=s.Matrix([R(999,1000),1,R(1001,1000)]);Lap=e*e.T-3*I
F=om+s.Matrix([R(1,10)*(k[i]-1)*om[i] for i in range(3)])+Lap*om/60
fac=s.Matrix([R(9499,10000),R(19,20),R(9501,10000)])
ck('F01 exact Fourier prestage factors',zero(F-s.matrix_multiply_elementwise(fac,om)))
ck('F02 all factors positive and triple-angle kicks vanish',all(x>0 for x in fac) and all(zero(s.im((om[j]/om[i])**3)) for i in range(3) for j in range(3)))
def chir(q):return s.re(q).cross(s.im(q))
W0=T*chir(om);W1=s.simplify(T*chir(F))
expected=s.Matrix([rt(3)/200000000,R(57,400000),0])
ck('F03 launch starts dipole-silent',zero(W0))
ck('F04 exact nonzero native endpoint',zero(W1-expected) and norm2(W1)>0)
jF=s.simplify(alpha*D*W1)
expectedj=alpha*rt(3)*s.Matrix([-28501,2,28499])/600000000
ck('F05 signed three-loop launch weights',zero(jF-expectedj))
ck('F06 launch aggregate moment',zero(s.pi*a*a*T*jF-s.pi*a*a*alpha*expected))
ck('F07 exact empty-launch work',zero(L*norm2(jF)/2-L*alpha**2*R(270750001,40000000000000000)))
ck('F08 conjugate launch has opposite moment and equal work',zero(T*chir(s.conjugate(F))+W1) and zero(norm2(-jF)-norm2(jF)))
dI=s.simplify(sum(s.Abs(F[i])**2 for i in range(3))-3)
ck('E07 Fourier native intensity change',zero(dI+R(14624999,50000000)))
aligned=e+s.Matrix([R(1,10)*(k[i]-1) for i in range(3)])
ck('E08 aligned control changes native intensity but no loop target',zero(T*chir(aligned)) and zero(norm2(aligned)-3-R(1,50000000)))
ck('E09 hidden raw-C initialization has nonzero common storage',zero(chir(om)+rt(3)*e/2) and zero(norm2(alpha*chir(om))*L/2-9*L*alpha**2/8))
# Port-null exact controls; no fictional claim that the two states are F-adjacent.
delta=s.symbols('delta',real=True)
rz=lambda t:s.Matrix([[s.cos(t),-s.sin(t),0],[s.sin(t),s.cos(t),0],[0,0,1]])
v=rz(-delta)*ex
K=s.Matrix.vstack(((2*ey+rt(3)*ez)/rt(7)).T,((2*ey-rt(3)*ez)/rt(7)).T)*rz(delta)
cx=ez;cy=v.cross(ez)
ck('K01 opposite states have equal intensity',zero(norm2(cx)+norm2(cy)-2))
ck('K02 opposite chiralities and zero old ports',zero(cx.cross(cy)-v) and zero(K*v) and zero(K*(-v)))
ck('K03 port-null W has a positive uniform lower bound',zero(norm2(T*v)-(1+s.sin(2*delta)/2)))
seeds=alpha*D*T*v
ck('K04 opposite static initialization targets',zero(seeds-alpha*P*v) and zero(T*seeds-alpha*T*v))
ck('K05 static empty no-change cannot repair target mismatch',zero(alpha*D*(T*v-T*v)) and not zero(T*v))
ck('K06 equal seed work for opposite invisible states',zero(L*norm2(seeds)/2-L*alpha**2*(1+s.sin(2*delta)/2)/3))
# Symmetry, retained orientation and a counterexample to symmetry without linearity.
u=[rz(2*s.pi*i/3)*ey for i in range(3)];nu=[v.cross(ez) for v in u]
ck('S01 ordered normals',zero(s.Matrix.hstack(nu[2],nu[0],nu[1])-T))
S=s.diag(-1,1,1);Tm=-S*T;Dm=R(2,3)*Tm.T
ck('S02 transported mirror gives the same signed scalar weights',zero(Dm*(-S*W)-D*W))
RR=rz(2*s.pi/3)
ck('S03 cyclic symmetry forbids a nonzero invariant linear functional',s.det((RR-I)[:2,:2])!=0)
poly=lambda v:s.expand(v[0]**3-3*v[0]*v[1]**2)
ck('S04 cubic common mode survives cyclic symmetry',zero(poly(RR*W)-poly(W)))
ck('S05 cubic common mode has required mirror parities',zero(poly(-W)+poly(W)) and zero(poly(-S*W)-poly(W)))
ck('S06 common-mode energy still excludes that alternative from minimum',zero(norm2(jm+poly(W)*e)-norm2(jm)-3*poly(W)**2))
# Exact RX exchange derivative witness.
mu=s.symbols('mu',positive=True)
ca=ez;cb=ex;port=s.Matrix([1,1])
wport=s.simplify(K.subs(delta,0).T*port)
adot=mu*wport.cross(cb);bdot=-mu*wport.cross(ca)
Cdot=s.simplify(adot.cross(cb)+ca.cross(bdot));Wdot=T*Cdot
ck('T01 actual RX can change W between native jumps',zero(T*ca.cross(cb)-ex) and zero(Wdot+8*mu/rt(7)*ex))
ck('T02 constant means then fail continuous target tracking',zero(-alpha*Wdot-8*alpha*mu/rt(7)*ex))
ck('T03 jump cannot repair an accumulated tracking error',zero(T*(jm+err+dj)-alpha*Wp-T*err))
# Dimensions and geometry are retained as symbolic inputs; no SI fit made.
wc=s.symbols('width',positive=True)
Kc=rt(3)/12+rt(6)/4;radius=rt(7)*Kc/(2*(1+rt(3)/2))
ck('G01 geometric radius and length positive',Kc>0 and radius>0)
ck('G02 centers are distinct and normals unit',all(not zero(Kc*u[i]-Kc*u[j]) for i in range(3) for j in range(i)) and all(zero(norm2(n)-1) for n in nu))
ck('G03 minimum is unique among signed lifts but zero sum is not positivity',sum([int(v<0) for v in [-28501,2,28499]])==1,
   detail='For alpha>0 the A current is negative and B,C positive; signs are oriented circulation, not negative storage.')
b=s.symbols('offset',real=True)
rho=a*(s.cos(chi)*ey+s.sin(chi)*ez);tangent=-s.sin(chi)*ey+s.cos(chi)*ez
current=s.cos(chi);J0=s.integrate(current*tangent*a,(chi,0,2*s.pi))
mcenter=s.integrate(rho.cross(current*tangent)*a/2,(chi,0,2*s.pi))
morigin=s.integrate((b*ey+rho).cross(current*tangent)*a/2,(chi,0,2*s.pi))
ck('G04 nonuniform centered moment need not equal global moment',zero(mcenter) and zero(morigin-b*ey.cross(J0)/2) and zero(morigin-s.pi*a*b*ex/2))
manifest=json.loads((ROOT/'SOURCE_VERIFICATION.json').read_text('utf-8'))
ck('V01 primary bytes and Git blobs match accepted identities',all(
    hashlib.sha256((ROOT/r['saved_as']).read_bytes()).hexdigest()==r['sha256'] and
    hashlib.sha1(b'blob '+str(r['bytes']).encode()+b'\0'+(ROOT/r['saved_as']).read_bytes()).hexdigest()==r['git_blob']
    for r in manifest['sources']),'byte identity')
result=dict(status='PASS',checks=len(rows),results=rows,environment=dict(conda=os.environ['CONDA_DEFAULT_ENV'],
    python=sys.version,sympy=s.__version__,platform=platform.platform()),runtime_seconds=time.time()-t0,
    exact_controls=dict(W_fourier=[str(v) for v in W1],j_fourier_over_alpha=[str(s.simplify(v/alpha)) for v in jF],
        launch_work_over_L_alpha2=str(R(270750001,40000000000000000)),
        launch_work_decimal=str(s.N(R(270750001,40000000000000000),16)),
        native_delta_I=str(dI),rx_interjump_Wdot=[str(v) for v in Wdot]),
    scope='Exact algebra checks plus written continuum/minimization/source arguments; no native orbit or production execution.')
(ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','runtime_seconds','exact_controls']},indent=2))
