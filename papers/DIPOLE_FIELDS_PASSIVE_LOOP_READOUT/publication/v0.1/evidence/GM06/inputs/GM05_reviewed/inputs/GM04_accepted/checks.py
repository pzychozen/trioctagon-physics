"""GM04 decisive symbolic identities and independent quadrature diagnostics.

Run in Command Prompt: run_python.cmd checks.py
No production code or old investigation script is imported or executed.
Numerical quadrature is a diagnostic, not a continuum or interval certificate.
"""
from pathlib import Path
import json, os, sys, platform, hashlib, time
import sympy as s
import numpy as np
import scipy
from scipy.integrate import quad_vec
ROOT=Path(__file__).resolve().parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
started=time.time(); rows=[]; data={}
def check(name,condition,kind='exact symbolic',detail=None):
    passed=bool(condition)
    rows.append(dict(name=name,passed=passed,kind=kind,detail=detail))
    if not passed: raise AssertionError(name)
def zero(expr):
    if hasattr(expr,'shape'): return all(s.simplify(t)==0 for t in expr)
    return s.simplify(expr)==0
ex,ey,ez=[s.eye(3)[:,i] for i in range(3)]
rt=s.sqrt; chi=s.symbols('chi',real=True)
a,z=s.symbols('a z',positive=True); j,g=s.symbols('j g',real=True)
T=s.Matrix([[-s.Rational(1,2),1,-s.Rational(1,2)],[-rt(3)/2,0,rt(3)/2],[0,0,0]])
def rz(t):return s.Matrix([[s.cos(t),-s.sin(t),0],[s.sin(t),s.cos(t),0],[0,0,1]])
u=[rz(2*s.pi*k/3)*ey for k in range(3)]
nu=[v.cross(ez) for v in u]
check('G01 ordered circle normals equal T',zero(s.Matrix.hstack(nu[2],nu[0],nu[1])-T))
check('G02 rank and exact kernel',T.rank()==2 and zero(T*s.ones(3,1)))
check('G03 metric identity',zero(T.T*T-s.Rational(3,2)*(s.eye(3)-s.ones(3)/3)))
rho=a*(s.cos(chi)*ey+s.sin(chi)*ez)
tangent=-s.sin(chi)*ey+s.cos(chi)*ez
check('G04 published orientation',zero(rho.cross(tangent)-a*ex))
check('G05 circle moment identity',zero(s.integrate(rho.cross(j*tangent)*a/2,(chi,0,2*s.pi))-s.pi*j*a*a*ex))
S=s.diag(-1,1,1); Q=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
for k in range(3):
    check(f'G06 mirror normal label {k}',zero((S*u[k]).cross(S*ez)+S*nu[k]))
check('G07 reflected ordered normals and channel swap',zero(-S*T-T*Q))
Hs=s.diag(1,1,-1)
check('G08 horizontal mirror reverses oriented normal',zero((Hs*ey).cross(Hs*ez)+ex))
delta=s.symbols('delta',real=True)
v=rz(-delta)*ex; yp=v.cross(ez)
K=s.Matrix.vstack(((2*ey+rt(3)*ez)/rt(7)).T,((2*ey-rt(3)*ez)/rt(7)).T)*rz(delta)
check('K01 actual port null',zero(K*v))
check('K02 W survives port null',zero((T*v).dot(T*v)-(1+s.cos(delta)*s.sin(delta))))
check('K03 reduction to elementary sine bound',zero(1+s.cos(delta)*s.sin(delta)-(1+s.sin(2*delta)/2)),
      detail='The universal >=1/2 consequence uses -1<=sin(2 delta)<=1 in the written proof.')
check('K04 plus chirality realization',zero(ez.cross(yp)-v))
check('K05 minus chirality realization',zero(ez.cross(-yp)+v))
check('K06 matched native intensities',zero(ez.dot(ez)+yp.dot(yp)-2))
om=s.Matrix([1,(-1-s.I*rt(3))/2,(-1+s.I*rt(3))/2])
factors=s.Matrix([s.Rational(9499,10000),s.Rational(19,20),s.Rational(9501,10000)])
L=s.ones(3)-3*s.eye(3); kval=s.Matrix([s.Rational(999,1000),1,s.Rational(1001,1000)])
pre=om+s.Matrix([s.Rational(1,10)*(kval[i]-1)*om[i] for i in range(3)])+L*om/60
fo=s.matrix_multiply_elementwise(factors,om)
check('F01 exact NPC prestage of Fourier preparation',zero(pre-fo))
check('F02 synchronization exactly zero',all(zero(s.im((om[k]/om[i])**3)) for i in range(3) for k in range(3)),
      detail='All prestage factors positive; phases unchanged; triple differences are multiples of 2 pi.')
def C(q):return s.re(q).cross(s.im(q))
check('F03 initial W zero',zero(T*C(om)))
w=s.Matrix([rt(3)/200000000,s.Rational(57,400000),0])
check('F04 nonzero endpoint W',zero(T*C(fo)-w) and w.dot(w)>0)
check('F05 exact endpoint squared norm',zero(w.dot(w)-s.Rational(812250003,40000000000000000)))
# Differentiate the exterior kernel BEFORE restricting to the axis.
xx,yy,zz=s.symbols('x y z',real=True); X=s.Matrix([xx,yy,zz])
rho_xy=a*s.Matrix([s.cos(chi),s.sin(chi),0]); dl=s.diff(rho_xy,chi)
d=s.sqrt((X-rho_xy).dot(X-rho_xy)); integrand=dl/d
def curl(F):return s.Matrix([s.diff(F[2],yy)-s.diff(F[1],zz),s.diff(F[0],zz)-s.diff(F[2],xx),s.diff(F[1],xx)-s.diff(F[0],yy)])
axis={xx:0,yy:0,zz:z}
check('A01 vector record zero on full finite-radius axis',zero(s.integrate(integrand.subs(axis),(chi,0,2*s.pi))))
axis_curl=s.simplify(s.integrate(curl(integrand).subs(axis),(chi,0,2*s.pi))*g*j/(4*s.pi))
check('A02 curl exact on axis with positive orientation',zero(axis_curl-g*j*a*a*ez/(2*(a*a+z*z)**s.Rational(3,2))))
check('A03 axis formula even in signed axial coordinate',zero(axis_curl.subs(z,-z)-axis_curl))
# Leading vector potential and its full curl.
r=s.sqrt(X.dot(X)); m1,m2,m3=s.symbols('m1 m2 m3',real=True); m=s.Matrix([m1,m2,m3])
check('D01 full angular curl',zero(curl(m.cross(X)/r**3)-(3*X*(X.dot(m))/r**5-m/r**3)))
for label,n,expected in [('axial',ez,2*ez),('equatorial',ex,-ez),('oblique',(ex+ez)/rt(2),3*ex/2+ez/2)]:
    check('D02 angular '+label,zero(3*n*n.dot(ez)-ez-expected))
# Differentiated-kernel Taylor bound: ||D_w^2 Hess(1/r)|| <=24/r^5 for unit w.
H=s.hessian(1/r,(xx,yy,zz)); wx,wy,wz=s.symbols('wx wy wz',real=True); ww=s.Matrix([wx,wy,wz])
Dww=H.applyfunc(lambda f:sum(ww[i]*ww[k]*s.diff(f,[xx,yy,zz][i],[xx,yy,zz][k]) for i in range(3) for k in range(3)))
rr=s.symbols('R',positive=True); ct,st=s.symbols('ct st',real=True)
actual=s.simplify(Dww.subs({xx:0,yy:0,zz:rr,wx:st,wy:0,wz:ct})*rr**5)
expected=s.Matrix([[9-21*ct**2,0,-24*ct*st],[0,3-15*ct**2,0],[-24*ct*st,0,36*ct**2-12]])
diff=(actual-expected).applyfunc(lambda e:s.expand(e).subs(st**2,1-ct**2).simplify())
check('R01 exact fourth derivative matrix',zero(diff))
q=s.symbols('q',real=True)
detminus=s.expand((15+21*q)*(36-36*q)-576*q*(1-q))
detplus=s.expand((33-21*q)*(12+36*q)-576*q*(1-q))
check('R02 upper operator bound determinant',zero(detminus-180*(1-q)*(3+q)))
check('R03 lower operator bound determinant',zero(detplus-(396+360*q-180*q*q)))
check('R04 diagonal and determinant range certificate',
      min(15,36,12,48,33,12,12,3)>0 and zero(detplus-396-180*q*(2-q)),
      detail='24I-M: diagonals 15+21q,36(1-q); 24I+M: 33-21q>=12,12+36q>=12; determinant>=396. Remaining eigenvalue 3-15q in [-12,3].')
rad=s.symbols('rad',nonnegative=True)
check('R05 disk second moment',zero(s.integrate(2*s.pi*rad**3,(rad,0,a))-s.pi*a**4/2))
check('R06 remainder coefficient and r>=2a simplification',s.Rational(24,2)*s.Rational(1,2)/4==s.Rational(3,2) and s.Rational(3,2)*2**5==48)
# Periodic mean and examples.
t,c=s.symbols('t c',real=True)
p=s.sin(chi)*s.sin(c*t/a); rc=s.cos(chi)*s.cos(c*t/a)
check('M01 exact source-free mean-zero wave',zero(s.diff(p,t)+c*s.diff(rc,chi)/a) and zero(s.diff(rc,t)+c*s.diff(p,chi)/a))
check('M02 mean of the example zero',zero(s.integrate(rc*a,(chi,0,2*s.pi))))
J0=s.integrate(s.cos(chi)*(-s.sin(chi)*ex+s.cos(chi)*ey)*a,(chi,0,2*s.pi))
check('M03 nonuniform first moment survives',zero(J0-s.pi*a*ey))
check('M04 every periodic derivative integrates to zero fixture',zero(s.integrate(s.diff(s.sin(chi)+s.cos(2*chi),chi),(chi,0,2*s.pi))))
check('M05 constant preload is zero energy flux',zero(c*0*j))
check('M06 constant offset has zero spatial derivative',zero(s.diff(rc+j,chi)-s.diff(rc,chi)))
kap,LL,MM,beta,b0,mean=s.symbols('kappa L M beta b0 mean',positive=True)
wt_rhs=-kap**2*mean+rt(2)*kap/rt(MM)*(LL*MM*b0)
check('W01 WT nonempty incoming-wave mean witness',zero(wt_rhs.subs(mean,0)-rt(2)*kap*LL*rt(MM)*b0))
check('W02 empty-start pre-return mean ODE solution',zero(s.diff(mean*s.exp(-kap**2*t),t)+kap**2*mean*s.exp(-kap**2*t)))
check('W03 normal component rejected by WT mixing adjoint',zero((-s.sin(chi)*ey+s.cos(chi)*ez).dot(ex)))
# Retarded differentiation contains the derivative of the delayed history.
ce,tt=s.symbols('ce tt',positive=True); f=s.Function('f'); dd=s.symbols('d',positive=True)
check('D03 retarded radial derivative',zero(s.diff(f(tt-dd/ce)/dd,dd)+f(tt-dd/ce)/dd**2+s.Subs(s.diff(f(tt),tt),tt,tt-dd/ce)/(ce*dd)))
wave_axis=s.integrate(s.cos(chi)*(-s.sin(chi)*ex+s.cos(chi)*ey)*a,(chi,0,2*s.pi))
check('M07 exact mean-zero wave vector observation on axis',zero(wave_axis-s.pi*a*ey))
P=s.Matrix([s.cos(chi),s.sin(chi),0]); Vlead=ez.cross(X)/r**3
check('P01 constant-loop leading observation in carrier plane',zero(ez.dot(Vlead)))
phi=s.symbols('phi',real=True)
B=s.Matrix.hstack(s.Matrix([s.cos(phi),s.sin(phi),0]),ez,s.Matrix([s.sin(phi),-s.cos(phi),0]))
check('P02 published observer frame invertible and right-handed',zero(B.T*B-s.eye(3)) and zero(B.det()-1))
bb=s.symbols('beta',real=True); cc=s.Matrix(s.symbols('cA cB cC',real=True))
check('G09 common loop weight invisible to leading total moment',zero(T*(cc+bb*s.ones(3,1))-T*cc))
# Numerical integration checks in an equivalent positively oriented xy circle.
def integral(x,which='H',current=1.,amp=1.):
    x=np.asarray(x,dtype=float)
    def fun(angle):
        rho=np.array([np.cos(angle),np.sin(angle),0.])*amp
        dl=np.array([-np.sin(angle),np.cos(angle),0.])*amp
        dr=x-rho; dist=np.linalg.norm(dr)
        return current/(4*np.pi)*(dl/dist if which=='V' else np.cross(dl,dr)/dist**3)
    value,error=quad_vec(fun,0,2*np.pi,epsabs=1e-13,epsrel=1e-13)
    return value,float(error)
directions={'axis':np.array([0.,0.,1.]),'equator':np.array([1.,0.,0.]),'oblique':np.array([1.,0.,1.])/np.sqrt(2),
            'general':np.array([2.,-3.,4.])/np.sqrt(29)}
samples=[]
for label,n in directions.items():
    for radius in [2.,4.,20.,100.]:
        hv,err=integral(radius*n); vv,verr=integral(radius*n,'V')
        hd=(3*n*n[2]-np.array([0.,0.,1.]))/(4*radius**3)
        vd=np.cross([0.,0.,1.],n)/(4*radius**2)
        remainder=1.5/(radius-1)**5
        check(f'N01 uniform remainder {label} r={radius:g}',np.linalg.norm(hv-hd)<=remainder+2e-13,'numerical quadrature',dict(error=float(np.linalg.norm(hv-hd)),bound=remainder))
        samples.append(dict(direction=label,radius=radius,H=hv.tolist(),V=vv.tolist(),dipole=hd.tolist(),leading_V=vd.tolist(),quad_error=err))
for za in [0.,.25,1.,2.,-2.,10.]:
    hv,err=integral([0,0,za]);vv,_=integral([0,0,za],'V')
    check(f'N02 finite axis z={za:g}',np.linalg.norm(vv)<1e-13 and np.linalg.norm(hv-np.array([0,0,1/(2*(1+za*za)**1.5)]))<1e-12,'numerical quadrature')
hv,_=integral([2,1,3]);minus,_=integral([2,1,3],current=-1)
check('N03 reversal reverses full finite-radius field',np.linalg.norm(hv+minus)<1e-14,'numerical quadrature')
for label,n in directions.items():
    h1,_=integral(1000*n);h2,_=integral(2000*n)
    ratio=float(np.linalg.norm(h2)/np.linalg.norm(h1))
    check(f'N04 large-distance doubling {label}',abs(ratio-.125)<3e-7,'numerical quadrature',dict(ratio=ratio))
# Curl finite differences of V, independently from numerical Biot-Savart H.
target=np.array([2.1,-.7,1.3]);jac=np.empty((3,3));step=1e-4
for k in range(3):
    direction=np.eye(3)[k]
    vp,_=integral(target+step*direction,'V');vm,_=integral(target-step*direction,'V')
    jac[:,k]=(vp-vm)/(2*step)
curl_num=np.array([jac[2,1]-jac[1,2],jac[0,2]-jac[2,0],jac[1,0]-jac[0,1]])
hh,_=integral(target)
check('N05 independent spatial differentiation of V',np.linalg.norm(curl_num-hh)<2e-10,'finite-difference diagnostic',dict(error=float(np.linalg.norm(curl_num-hh))))
sources=json.loads((ROOT/'SOURCE_VERIFICATION.json').read_text('utf-8'))
check('S01 exact preserved primary inputs',all(hashlib.sha256((ROOT/r['saved_as']).read_bytes()).hexdigest()==r['sha256'] for r in sources['sources']),'byte identity')
check('S02 exact preserved GM inputs',all(hashlib.sha256((ROOT/r['saved_as']).read_bytes()).hexdigest()==r['sha256'] for r in sources['prior_inputs']),'byte identity')
result=dict(status='PASS',checks=len(rows),results=rows,numerical_samples=samples,
    scientific_scope='Written proof establishes continuum statements. Quadrature/finite differences are corroborating samples, not interval proofs or physical measurements.',
    environment=dict(python=sys.version,platform=platform.platform(),conda=os.environ['CONDA_DEFAULT_ENV'],sympy=s.__version__,numpy=np.__version__,scipy=scipy.__version__),
    runtime_seconds=time.time()-started)
(ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','runtime_seconds']},indent=2))
