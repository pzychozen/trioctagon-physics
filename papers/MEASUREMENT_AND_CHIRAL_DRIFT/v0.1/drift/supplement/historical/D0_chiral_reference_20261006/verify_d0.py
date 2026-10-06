# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""D0: exact reference checks; no unequal-branch solve or trajectory.

Run: python -X utf8 -B verify_d0.py
Only this lane's D0_RESULTS.json is written. Baseline is retained, not reset.
Native complex128 comparisons are separate from 100-digit transcriptions.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
sys.dont_write_bytecode = True
import sympy as sp
import mpmath as mp
import numpy as np

ROOT = Path('project-source')
REPO = ROOT/'trioctagon-physics'
OUT = Path(__file__).resolve().parent
assert OUT == ROOT/'research/D0_chiral_reference_20261006'
RESULT = OUT/'D0_RESULTS.json'
record = json.loads(RESULT.read_text(encoding='utf8'))
checks = []
expressions = {}
numerics = {}
sha = lambda b: hashlib.sha256(b).hexdigest()

def check(name, value, kind='EXACT SYMBOLIC CHECK', details=None):
    checks.append(dict(name=name, passed=bool(value), evidence=kind, details=details))
def eq(a, b=0):
    return sp.cancel(sp.expand(a-b)) == 0
def meq(a, b):
    return a.shape == b.shape and all(sp.simplify(x-y) == 0 for x,y in zip(a,b))
def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args]).decode('utf8')
def inventory(path):
    rows = {}; size = 0
    for p in sorted(path.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(path).parts and not p.is_relative_to(OUT):
            b=p.read_bytes(); rows[p.relative_to(path).as_posix()]=sha(b); size+=len(b)
    return dict(files=len(rows),bytes=size,sha256=sha(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()))

fresh = ROOT/'research/FRESH_EYES_SCIENTIFIC_REVIEW_20261006'
expected = {
 'FRESH_EYES_SCIENTIFIC_REVIEW_v0.1.md':'65dc00967ccdecc1c513bd8b3046568f475894ae0b960db314e1c0575c75b90d',
 'fresh_eyes_checks.py':'807e79cf4bda818835d19bc072b5802d23fff312dddc96c7df0ab26e7dca6d2d',
 'fresh_eyes_checks_output.txt':'92314cd236004d47cc3216aca509414cc05b062ed33605897f01fda7792eb31e'}
manifest = {p.name:sha(p.read_bytes()) for p in sorted(fresh.iterdir()) if p.is_file()}
for name,digest in expected.items():
    check('predecessor identity '+name, manifest[name]==digest, 'SOURCE / BYTE CHECK')
note=(fresh/'FRESH_EYES_RECONCILIATION_NOTE_v0.1.md').read_text(encoding='utf8')
check('note manifest contains all three original digests',all(v in note for v in expected.values()),'SOURCE / BYTE CHECK')

# Section B: rational Laurent identities, before specializing a Bloch phase.
a,b,c,g,ell,z=sp.symbols('a b c g ell z',nonzero=True)
D=sp.Matrix([[-2,1,1/z],[1,-2,1],[z,1,-2]])
R=sp.diag(a,b,c); total=a+b+c
H=sp.eye(3)+g*(D-sp.diag(*[(total-3*r)/r for r in [a,b,c]]))
P=R.inv()*H*R
Jsum=P+ell*D; Jnat=(sp.eye(3)+ell*D)*P
B2=lambda M:sp.expand((sp.trace(M)**2-sp.trace(M*M))/2)
V=(a-b)*(a-c)*(b-c)/(a*b*c)
chi=g*ell*(ell-g)*V
Gamma=g*ell*(ell*(1+3*g)-g)*V
trsum=sp.trace(Jsum); bsum=B2(Jsum); dsum=sp.factor(Jsum.det())
trnat=sp.trace(Jnat); bnat=B2(Jnat)
dnat=sp.factor((sp.eye(3)+ell*D).det()*P.det())
check('additive trace inversion even',eq(trsum,trsum.subs(z,1/z)))
check('additive B2 inversion even',eq(bsum,bsum.subs(z,1/z)))
check('additive determinant odd part is chi',eq(dsum-dsum.subs(z,1/z),chi*(z-1/z)))
check('native trace inversion even',eq(trnat,trnat.subs(z,1/z)))
check('native B2 odd part is minus Gamma',eq(bnat-bnat.subs(z,1/z),-Gamma*(z-1/z)))
check('native determinant inversion even',eq(dnat,dnat.subs(z,1/z)))
h,gh,lh=sp.symbols('h ghat ellhat',real=True)
K=(Jsum-sp.eye(3)).subs({g:h*gh,ell:h*lh}).applyfunc(lambda v:sp.cancel(v/h))
ts=trsum.subs({g:h*gh,ell:h*lh}); bs=bsum.subs({g:h*gh,ell:h*lh}); ds=dsum.subs({g:h*gh,ell:h*lh})
check('generator trace rescaling',eq(sp.trace(K),(ts-3)/h))
check('generator B2 rescaling',eq(B2(K),(bs-2*ts+3)/h**2))
check('generator determinant rescaling',eq(K.det(),(ds-bs+ts-1)/h**3))
chihat=gh*lh*(lh-gh)*V
check('generator determinant odd part persists',eq(K.det()-K.det().subs(z,1/z),chihat*(z-1/z)))
expressions['section_B']={'chi':str(chi),'Gamma':str(Gamma),'rescaled_native_Im_B2_over_sin':'-h*(chi_hat+3*h*ghat**2*ellhat**2*Vand/(a*b*c))','rescaled_native_Im_det_over_sin':'chi_hat+3*h*ghat**2*ellhat**2*Vand/(a*b*c)'}
fixture={a:sp.Rational(4,5),b:1,c:sp.Rational(13,10),g:sp.Rational(1,5),ell:sp.Rational(3,100),z:sp.I}
check('Section B exact numerical fixture middle coefficient zero',eq(sp.im(bsum.subs(fixture))))
check('Section B exact numerical fixture determinant nonzero',eq(sp.im(dsum.subs(fixture)),chi.subs(fixture)) and chi.subs(fixture)!=0)
numerics['section_B_fixture']={ 'Im_B2':str(sp.simplify(sp.im(bsum.subs(fixture)))), 'Im_det':str(sp.simplify(sp.im(dsum.subs(fixture)))) }

# Native potential normalization and finite descent qualifications.
xx=sp.symbols('x0:3',real=True); yy=sp.symbols('y0:3',real=True)
kk=sp.symbols('k0:3',real=True); eps=sp.symbols('eps',real=True)
rho=[xx[i]**2+yy[i]**2 for i in range(3)]
pot=eps*sum(rho[i]**2/4-kk[i]*rho[i]/2 for i in range(3)) + g*sum((xx[i]-xx[j])**2+(yy[i]-yy[j])**2 for i,j in [(0,1),(0,2),(1,2)])/2
L=sp.ones(3)-3*sp.eye(3)
increment=sp.Matrix([eps*xx[i]*(kk[i]-rho[i])+g*(L*sp.Matrix(xx))[i] for i in range(3)]+[eps*yy[i]*(kk[i]-rho[i])+g*(L*sp.Matrix(yy))[i] for i in range(3)])
check('six-coordinate negative potential gradient',meq(increment,-sp.Matrix([sp.diff(pot,v) for v in xx+yy])))
onsite=eps*((xx[0]**2+yy[0]**2)**2/4-kk[0]*(xx[0]**2+yy[0]**2)/2)
q=sp.Matrix([xx[0],yy[0]])
check('onsite Hessian exact formula',meq(sp.hessian(onsite,[xx[0],yy[0]]),eps*((rho[0]-kk[0])*sp.eye(2)+2*q*q.T)))
theta=sp.symbols('t0:3',real=True); la=sp.symbols('lambda',real=True)
U=-la*sum(sp.cos(3*(theta[j]-theta[i])) for i,j in [(0,1),(0,2),(1,2)])/3
kick=sp.Matrix([la*sum(sp.sin(3*(theta[j]-theta[i])) for j in range(3) if i!=j) for i in range(3)])
check('phase increment negative gradient',meq(kick,-sp.Matrix([sp.diff(U,t) for t in theta])))
weighted=sp.zeros(3)
for i,j in [(0,1),(0,2),(1,2)]:
    edge=sp.zeros(3,1); edge[i]=1; edge[j]=-1
    weighted+=3*la*sp.cos(3*(theta[j]-theta[i]))*edge*edge.T
check('phase Hessian weighted graph formula',meq(sp.hessian(U,theta),weighted))
check('phase kicks sum to zero',sp.trigsimp(sum(kick))==0)
check('triad Laplacian norm equals three',set((-L).eigenvals())=={sp.Integer(0),sp.Integer(3)})
zcart=sp.Matrix([xx[i]+sp.I*yy[i] for i in range(3)])
pre=zcart+sp.Matrix([increment[i]+sp.I*increment[i+3] for i in range(3)])
check('prestage total imaginary pairing vanishes',sp.simplify(sp.im((sp.conjugate(zcart).T*pre)[0]))==0)
check('nonzero input can reach zero prestage',pre.subs(dict(zip(xx,[1,1,2]))|dict(zip(yy,[0,0,0]))|dict(zip(kk,[0,0,0]))|{eps:1,g:0})==sp.Matrix([0,0,-6]))

# Complete local real Jacobian at the selected twisted reference, derived
# directly from the cubic prestage and then the derivative of synchronization.
A=sp.sqrt(2)/2; ph=2*sp.pi/3
eh=h; gg=h/6; lam=h/30
C=sp.zeros(3); Q=sp.zeros(3)
for j in range(3):
    for shift in [-1,1]:
        C[j,(j+shift)%3]+=gg*sp.cos(ph)
        Q[j,(j+shift)%3]+=gg*sp.sin(shift*ph)
C+=(1+gg)*sp.eye(3)
Jpre=(C-2*eh*A*A*sp.eye(3)).row_join(-Q).col_join(Q.row_join(C))
J=(sp.diag(sp.eye(3),sp.eye(3)+3*lam*L)*Jpre).applyfunc(sp.expand)
dh=(J-sp.eye(6)).applyfunc(lambda v:sp.cancel(v/h))
qphase=sp.Matrix([0]*3+[A]*3)
gauge=sp.Matrix([[0]*3+[1/(3*A)]*3])
border=dh.row_join(-qphase).col_join(gauge.row_join(sp.zeros(1)))
bd=sp.factor(border.det(method='domain-ge'))
check('full rescaled seven-real-variable border determinant',eq(bd,-(3*h-1)**2/1600))
check('border h=0 nonzero',eq(bd.subs(h,0),-sp.Rational(1,1600)))
check('border interval endpoint bound',eq(bd.subs(h,sp.Rational(1,4)),-sp.Rational(1,25600)))
check('common phase only exact kernel in reference generator',dh.subs(h,0).rank()==5 and meq(dh*qphase,sp.zeros(6,1)) and eq((gauge*qphase)[0],1))
vplus=sp.Matrix([sp.exp(sp.I*ph*j).expand(complex=True) for j in range(3)])
check('triad twisted Laplacian eigenvector',meq(L*vplus,-3*vplus))
check('reference amplitude and prestage factor',eq(1-3*sp.Rational(1,6),A*A) and eq(1+h*(1-A*A)-3*h/6,1))
Da=1-3*h/4; Db=1+h/4; X=h/4; sigma=1-3*h/10
M=sp.diag(1,sigma)*sp.Matrix([[Da,-sp.I*X],[sp.I*X,Db]])
check('nonzero Fourier modes have mixed terms',X!=0)
check('transverse determinant at multiplier one',eq((M-sp.eye(2)).det(),h*h*(3*h-1)/40))
mu=sp.symbols('mu')
cp=sp.factor((mu*sp.eye(2)-M).det())
expected_char=(mu-1)*(mu-(1-h))*cp**2
check('full real characteristic polynomial',eq(J.charpoly(mu).as_expr(),expected_char))
for sign in [1,-1]:
    v=sp.conjugate(vplus) if sign<0 else vplus
    embed=sp.diag(v,v)
    block=M if sign>0 else sp.conjugate(M)
    check('direct full-to-Fourier intertwiner '+str(sign),meq(J*embed,embed*block))
K0=dh.subs(h,0)
expected_gen=[0,-1,(-8+sp.sqrt(74))/20,(-8-sp.sqrt(74))/20]
check('generator characteristic with saddle directions',eq(K0.charpoly(mu).as_expr(),mu*(mu+1)*(mu**2+sp.Rational(4,5)*mu-sp.Rational(1,40))**2))
kappa=sp.Matrix([-1,0,1])
check('chosen perturbation direction three distinct and zero sum',sum(kappa)==0 and len(set(kappa))==3)
check('chosen oriented Vandermonde equals two',(kappa[0]-kappa[1])*(kappa[1]-kappa[2])*(kappa[2]-kappa[0])==2)
expressions['reference']={'eps_hat':'1','g_hat':'1/6','lambda_hat':'1/30','ell_hat':'1/10','kbar':'1','A_squared':'1/2','kappa':[-1,0,1],'h_domain':'0 < h <= 1/4','transverse_characteristic':str(cp),'bordered_rescaled_determinant':str(bd),'generator_eigenvalues':[str(t) for t in expected_gen],'generator_multiplicities':[1,1,2,2]}

# Low-order selection: the only alternating cubics are Vandermonde;
# no symmetric linear term on the zero-sum plane permits quartic drift.
x0,x1=sp.symbols('x0 x1'); xs=[x0,x1,-x0-x1]
vand=(xs[0]-xs[1])*(xs[1]-xs[2])*(xs[2]-xs[0])
swap=lambda p:sp.expand(p.subs({x0:x0,x1:-x0-x1},simultaneous=True))
cyclic=lambda p:sp.expand(p.subs({x0:-x0-x1,x1:x0},simultaneous=True))
check('Vandermonde transforms with orientation sign',eq(cyclic(vand),vand) and eq(swap(vand),-vand))
dims={}
for degree in range(5):
    cs=sp.symbols('c:'+str(degree+1)); pol=sum(cs[j]*x0**j*x1**(degree-j) for j in range(degree+1))
    equations=sp.Poly(cyclic(pol)-pol,x0,x1).coeffs()+sp.Poly(swap(pol)+pol,x0,x1).coeffs()
    mat=sp.linear_eq_to_matrix(equations,cs)[0]
    dims[degree]=len(cs)-mat.rank()
check('alternating Taylor dimensions degrees zero through four',dims=={0:0,1:0,2:0,3:1,4:0})
expressions['alternating_dimensions']=dims

# Import only the actual pure dynamics module, with bytecode disabled.
spec=importlib.util.spec_from_file_location('d0_native_dynamics',REPO/'kernel_physics/dynamics.py')
native=importlib.util.module_from_spec(spec);sys.modules[spec.name]=native;spec.loader.exec_module(native)
cfg=native.DynamicsConfig(.1,.1/6,.1/30,(1.,1.,1.))
ref=np.array([complex(sp.N(A*v,18)) for v in vplus])
actual=native.step3(ref,cfg)
check('native complex128 reference fixed state',np.max(np.abs(actual-ref))<2e-15,'NUMERICAL EVIDENCE',float(np.max(np.abs(actual-ref))))
zerostate=np.array([0,1+2j,-.7+.3j]); roots=np.exp(2j*np.pi*np.array([1,2,1])/3)
check('Arg0 signed zeros equal zero',np.array_equal(native.arg0(np.array([complex(0.,-0.),complex(-0.,0.)])),[0.,0.]),'NATIVE NUMERICAL CHECK')
check('sync conjugation on zero stratum',np.allclose(native.phase_sync(np.conj(zerostate),.13),np.conj(native.phase_sync(zerostate,.13)),rtol=0,atol=3e-15),'NUMERICAL EVIDENCE')
check('sync local Z3 on zero stratum',np.allclose(native.phase_sync(roots*zerostate,.13),roots*native.phase_sync(zerostate,.13),rtol=0,atol=4e-15),'NUMERICAL EVIDENCE')
w=np.array([0,1,1],dtype=complex); rot=np.exp(1j*np.pi/6)
defect=float(np.max(np.abs(native.phase_sync(rot*w,.1)-rot*native.phase_sync(w,.1))))
check('arbitrary common phase fails on zero stratum',defect>.09,'NUMERICAL EVIDENCE',defect)
cfg0=native.DynamicsConfig(1,0,.1,(0,0,0))
check('native nonzero-input prestage-zero witness',np.allclose(native.step3([1,1,2],cfg0),[0,0,-6],rtol=0,atol=2e-15),'NATIVE NUMERICAL CHECK')
sample=np.array([.8+.2j,-.3+.7j,1.1-.5j]); kval=np.array([1.,1.2,.9])
cfgs=native.DynamicsConfig(.03,.02,.04,tuple(kval))
for indices,name in [([2,0,1],'translation'),([0,2,1],'reflection')]:
    idx=np.array(indices); other=native.DynamicsConfig(.03,.02,.04,tuple(kval[idx]))
    check('joint native '+name+' covariance',np.allclose(native.step3(sample[idx],other),native.step3(sample,cfgs)[idx],rtol=0,atol=2e-15),'NUMERICAL EVIDENCE')
check('complete native conjugation',np.allclose(native.step3(np.conj(sample),cfgs),np.conj(native.step3(sample,cfgs)),rtol=0,atol=2e-15),'NUMERICAL EVIDENCE')

# 100-digit checks only at eta=0. Finite differences differentiate the full
# native formula, not a pre-separated amplitude/phase surrogate.
mp.mp.dps=100
Amp=mp.sqrt(mp.mpf('0.5')); phi=2*mp.pi/3
unit=[mp.exp(1j*phi*j) for j in range(3)]
reference=[Amp*u for u in unit]
def mpsync(state,lam):
    angles=[mp.arg(w) if w else mp.mpf(0) for w in state]
    kicks=[lam*sum(mp.sin(3*(angles[j]-angles[i])) for j in range(3) if i!=j) for i in range(3)]
    return [state[i]*mp.exp(1j*kicks[i]) for i in range(3)]
def mpstep(state,step):
    pre=[state[i]+step*state[i]*(1-abs(state[i])**2)+(step/6)*(sum(state)-3*state[i]) for i in range(3)]
    return mpsync(pre,step/30)
def localmap(vec,step):
    state=[unit[j]*(Amp+vec[j]+1j*vec[j+3]) for j in range(3)]
    image=mpstep(state,step)
    local=[image[j]/unit[j]-Amp for j in range(3)]
    return mp.matrix([mp.re(v) for v in local]+[mp.im(v) for v in local])
ref_checks=[]
for step in [mp.mpf(1)/4,mp.mpf(1)/10,mp.mpf(1)/100]:
    residual=max(abs(x-y) for x,y in zip(mpstep(reference,step),reference))
    ref_checks.append({'h':mp.nstr(step,20),'fixed_residual':mp.nstr(residual,12)})
    check('100-digit fixed branch h='+mp.nstr(step,20),residual<mp.mpf('1e-95'),'NUMERICAL EVIDENCE',mp.nstr(residual,12))
eta_fd=mp.mpf('1e-30'); step=mp.mpf(1)/10
Jfd=mp.matrix(6,6)
for j in range(6):
    vp=mp.matrix(6,1);vm=mp.matrix(6,1);vp[j]=eta_fd;vm[j]=-eta_fd
    col=(localmap(vp,step)-localmap(vm,step))/(2*eta_fd)
    for i in range(6):Jfd[i,j]=col[i]
exactJ=mp.matrix([[mp.mpf(str(sp.N(J[i,j].subs(h,sp.Rational(1,10)),105))) for j in range(6)] for i in range(6)])
jerr=max(abs(Jfd[i,j]-exactJ[i,j]) for i in range(6) for j in range(6))
check('100-digit complete real Jacobian finite difference',jerr<mp.mpf('1e-57'),'NUMERICAL EVIDENCE',mp.nstr(jerr,15))
numerics['reference_checks']=ref_checks
numerics['jacobian_fd']={'dps':100,'step':'1/10','real_coordinate_difference':'1e-30','max_error':mp.nstr(jerr,15)}
numerics['native_fixed_residual']=float(np.max(np.abs(actual-ref)))

current={'head':git('rev-parse','HEAD').strip(),'branch':git('branch','--show-current').strip(),'status':git('status','--porcelain=v1'),'index_sha256':sha(git('ls-files','--stage','-z').encode()),'staged':git('diff','--cached','--name-only'),'roots':{name:inventory(ROOT/name) for name in record['baseline']['roots']}}
for key in ['head','branch','status','index_sha256','staged']:
    check('preservation '+key,current[key]==record['baseline'][key],'PRESERVATION CHECK')
for name in current['roots']:
    check('preservation bytes '+name,current['roots'][name]==record['baseline']['roots'][name],'PRESERVATION CHECK')
record.update({'verdict':'PASS_WITH_QUALIFICATIONS' if all(c['passed'] for c in checks) else 'HOLD','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'expressions':expressions,'numerics':numerics,'predecessor_manifest':manifest,'after':current,'source_manifest':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in [REPO/'kernel_physics/dynamics.py',REPO/'kernel_physics/readouts.py',REPO/'kernel_physics/z_diagnostics.py']},'script_sha256':sha(Path(__file__).read_bytes()),'scope':'No nonzero-eta branch solved; no drift coefficient evaluated; no trajectories; no scans.'})
report=OUT/'D0_CHIRAL_REFERENCE_AND_RECONCILIATION.md'
if report.exists():record['report_sha256']=sha(report.read_bytes())
RESULT.write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':record['verdict'],'passed':record['passed'],'total':record['total'],'failed':[c for c in checks if not c['passed']],'border':str(bd),'numerics':numerics,'protected_files':sum(x['files'] for x in current['roots'].values())},indent=2))
