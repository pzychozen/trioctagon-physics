"""GM06 exact geometry/measurement controls and corroborating kernel quadrature."""
from pathlib import Path
import os,sys,platform,json,hashlib,time,runpy
import sympy as s
import numpy as np
import scipy
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
ROOT=Path(__file__).resolve().parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
t0=time.time();rows=[]
def zero(v):
    if isinstance(v,s.MatrixBase):return all(s.simplify(x)==0 for x in v)
    return s.simplify(v)==0
def ck(name,value,kind='exact algebra',detail=None):
    passed=bool(value)
    rows.append(dict(name=name,passed=passed,kind=kind,detail=detail))
    assert passed,name
R=s.Rational;rt=s.sqrt;I=s.eye(3);ex,ey,ez=[I[:,i] for i in range(3)]
rz=lambda x:s.Matrix([[s.cos(x),-s.sin(x),0],[s.sin(x),s.cos(x),0],[0,0,1]])
Kc=rt(3)/12+rt(6)/4;ar=rt(7)*Kc/(2*(1+rt(3)/2))
T=s.Matrix([[-R(1,2),1,-R(1,2)],[-rt(3)/2,0,rt(3)/2],[0,0,0]])
u=[rz(2*s.pi*i/3)*ey for i in range(3)]
nu=[x.cross(ez) for x in u]
ck('G01 ordered source normals equal T',zero(s.Matrix.hstack(nu[2],nu[0],nu[1])-T))
ck('G02 exact geometric size bounds',0<Kc<1 and R(1,2)<ar<1)
phi=s.symbols('phi',real=True)
er=s.Matrix([s.cos(phi),s.sin(phi),0]);ep=s.Matrix([-s.sin(phi),s.cos(phi),0])
B=s.Matrix.hstack(er,ez,-ep)
ck('G03 published frame is proper orthonormal',zero(B.T*B-I) and zero(B.det()-1))
Q=B.subs(phi,s.pi/2)
ck('G04 selected receiving circle normal and basis',zero(Q*ex-ey) and zero(Q*ey-ez) and zero(Q*ez-ex))
RR,ww=s.symbols('R width',positive=True)
OR=(RR-ww*Kc)*ez
ck('G05 receiving circle center is R ez',zero(OR+ww*Kc*Q*ey-RR*ez))
vec=s.Matrix(s.symbols('v1 v2 v3',real=True))
ck('G06 registered frames recover ambient vectors',zero(B*(B.T*vec)-vec))
dirs=[s.Matrix([s.cos(-s.pi/2+i*s.pi/3),s.sin(-s.pi/2+i*s.pi/3),0]) for i in range(6)]
rg=rt(3)/6;hg=(rt(2)-1)/2;ag=(1-rt(2)/2)/2
topU=[rg*dirs[2*k]+ez/2 for k in range(3)]
topT=[ag*dirs[(2*k+1)%6]+hg*ez for k in range(3)]
edges=[(topU[k],topT[k]) for k in range(3)]+[(topT[k],topU[(k+1)%3]) for k in range(3)]
ck('G07 upper broken arcs join into a closed six-edge walk',zero(sum((b-a for a,b in edges),s.zeros(3,1))))
tau=s.symbols('tau',real=True)
A=I-tau/rg*s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
loU=[A*(v-ez/2)-ez/2 for v in topU];loB=[A*(v-hg*ez)-hg*ez for v in topT]
ledges=[(loU[k],loB[k]) for k in range(3)]+[(loB[k],loU[(k+1)%3]) for k in range(3)]
ck('G08 lower broken arcs also close for all static tau',zero(sum((b-a for a,b in ledges),s.zeros(3,1))))
ck('G09 upper six vertices are not coplanar',not zero((topU[1]-topU[0]).cross(topU[2]-topU[0]).dot(topT[0]-topU[0])))
ck('G10 loop normals at common point have rank two',T.rank()==2 and zero(T.T*ez) and zero(T*T.T-R(3,2)*s.diag(1,1,0)))
theta=s.symbols('theta',real=True);aa,bb,zz=s.symbols('a b z',positive=True)
source=aa*(s.cos(phi)*ey+s.sin(phi)*ez)
target=zz*ex+bb*(s.cos(theta)*ey+s.sin(theta)*ez)
dot=s.diff(source,phi).dot(s.diff(target,theta))
dist2=s.expand((target-source).dot(target-source))
ck('C01 coaxial tangent pairing is ab cos(phi-theta)',zero(dot-aa*bb*s.cos(phi-theta)))
ck('C02 exact coaxial distance',zero(dist2-(aa**2+bb**2+zz**2-2*aa*bb*s.cos(phi-theta))))
ck('C03 source tangent integrates to zero at axial center',zero(s.integrate(s.diff(source,phi),(phi,0,2*s.pi))))
ck('C04 paired cosine-square integral',zero(s.integrate(s.cos(phi)**2,(phi,-s.pi/2,s.pi/2))-s.pi/2))
ck('C05 denominator positive for nonzero axial separation',zero(aa**2+bb**2+zz**2-2*aa*bb-((aa-bb)**2+zz**2)))
ck('C06 coaxial zero-radius limit has correct coefficient',
   zero((aa/(2*s.pi*bb))*(s.pi*aa*bb/(aa**2+zz**2)**R(3,2))-aa**2/(2*(aa**2+zz**2)**R(3,2))))
rho=s.symbols('rho',nonnegative=True)
diskxi=rho*(s.cos(theta)*ex+s.sin(theta)*ey)
avg=lambda f:s.integrate(s.integrate(f*rho,(rho,0,bb)),(theta,0,2*s.pi))/(s.pi*bb**2)
ck('D01 centered disk first moment vanishes',zero(avg(diskxi)))
ck('D02 disk second moment',zero(avg(diskxi*diskxi.T)-bb**2*s.diag(1,1,0)/4))
ck('D03 Taylor disk coefficient is b^2/4',zero(avg(diskxi.dot(diskxi))/2-bb**2/4))
W=s.Matrix([rt(3)/200000000,R(57,400000),0]);alpha=s.symbols('alpha',real=True)
j=alpha*R(2,3)*T.T*W
expected=alpha*rt(3)*s.Matrix([-28501,2,28499])/600000000
ck('N01 reviewed minimum source weights',zero(j-expected))
ck('N02 reviewed source moment',zero(T*j-alpha*W))
Jratio=rt(3)*57002/85500
ck('N03 sum of absolute weights relative to alpha Wy',zero(Jratio-(rt(3)*57002/600000000)/(R(57,400000))))
ck('N04 ratio is below 6/5',Jratio<R(6,5))
q=R(1,100)
bound=R(144,5)*q/(1-q)**4+R(36,5)*q*q*((1-2*q)**-5+(1-3*q)**-5)
ck('N05 rational far-distance relative error is below 1/3',bound<R(1,3),detail=str(bound))
qq=s.symbols('q',nonnegative=True)
ck('N06 each error summand increases with width/distance',
   all(zero(s.diff(qq**p/(1-c*qq)**n,qq)-
            qq**(p-1)*(p+(n-p)*c*qq)/(1-c*qq)**(n+1))
       for p,c,n in [(1,1,4),(2,2,5),(2,3,5)]))
ck('N07 ez dipole field has negative y component',
   zero(((3*ez*ez.T-I)*W).dot(ey)+W[1]) and W[1]>0)
ck('N08 conjugate launch flips every source mean',zero(R(2,3)*T.T*(-W)+j/alpha))
sample_ratio_bound=R(64000000,1024**2)*(R(2,97**3)+R(3,97**2)+R(1,97))
ck('N09 rational 1024-sample sign bound at R=100w',sample_ratio_bound<R(2,3),
   detail='Uses a=b>w/2, a=b<w, delta>97w, J/(abs(alpha)Wy)<6/5, pi^2<10: '+str(sample_ratio_bound))

# Quadrature checks use the actual finite loop radius. They corroborate the proof,
# and are not used as interval certificates for a continuum sign statement.
af=float(ar);kf=float(Kc);basis=np.eye(3)
exn,eyn,ezn=basis
un=[np.array([float(v) for v in q]) for q in u]
jnum=np.array([float(v) for v in j.subs(alpha,1)])
source_indices=[2,0,1]
loops=[(kf*un[k],un[k],ezn,jnum[i]) for i,k in enumerate(source_indices)]
def field(points,which,n=192,curl=False):
    points=np.atleast_2d(points)
    ang=np.arange(n)*(2*np.pi/n)
    out=np.zeros_like(points,dtype=float)
    for center,e1,e2,weight in which:
        rho=af*(np.cos(ang)[:,None]*e1+np.sin(ang)[:,None]*e2)
        tangent=-np.sin(ang)[:,None]*e1+np.cos(ang)[:,None]*e2
        for start in range(0,len(points),256):
            pts=points[start:start+256]
            delta=pts[:,None,:]-(center+rho)[None,:,:]
            d=np.linalg.norm(delta,axis=2)
            if curl:
                integ=np.cross(tangent[None,:,:],delta)/d[:,:,None]**3
            else:
                # Subtraction integrates to zero analytically and reduces cancellation.
                inv=1/d-1/np.linalg.norm(pts-center,axis=1)[:,None]
                integ=tangent[None,:,:]*inv[:,:,None]
            out[start:start+len(pts)]+=weight*af/(2*n)*integ.sum(axis=1)
    return out
def contour(center,e1,e2,b,which,n):
    angle=np.arange(n)*(2*np.pi/n)
    pts=center+b*(np.cos(angle)[:,None]*e1+np.sin(angle)[:,None]*e2)
    tang=-np.sin(angle)[:,None]*e1+np.cos(angle)[:,None]*e2
    return (2/b)*np.mean(np.sum(field(pts,which,n)*tang,axis=1))
def disk_flux(center,e1,e2,b,which,n=128,nr=20):
    nodes,weights=leggauss(nr);tt=(nodes+1)/2;weights=weights/2
    angle=np.arange(n)*(2*np.pi/n)
    ring=np.cos(angle)[:,None]*e1+np.sin(angle)[:,None]*e2
    pts=center+b*np.sqrt(tt)[:,None,None]*ring[None,:,:]
    H=field(pts.reshape(-1,3),which,n,True).reshape(nr,n,3)
    normal=np.cross(e1,e2)
    return float(np.dot(weights,np.mean(H@normal,axis=1)))
coax=[]
for zval in [2.,4.,8.]:
    C=2*af*af+zval*zval;coupling=2*af*af
    angular,quaderr=quad(lambda t:np.cos(t)/np.sqrt(C-coupling*np.cos(t)),0,2*np.pi,
                         epsabs=1e-13,epsrel=1e-12)
    exactquad=angular/(2*np.pi)
    source_single=[(np.zeros(3),eyn,ezn,1.)]
    c=np.array([zval,0.,0.])
    value=contour(c,eyn,ezn,af,source_single,192)
    diskval=disk_flux(c,eyn,ezn,af,source_single)
    central=af**2/(2*(af**2+zval*zval)**1.5)
    finite_bound=1.5*af**4/zval**5
    lower=af**2/(2*(zval*zval+4*af*af)**1.5)
    upper=af**2/(2*zval**3)
    ck('Q01 coaxial positive exact-kernel check z='+str(zval),lower<value<upper,'quadrature')
    ck('Q02 coaxial double/single integral agreement z='+str(zval),abs(value-exactquad)<2e-13,'quadrature')
    ck('Q03 coaxial Stokes disk agreement z='+str(zval),abs(value-diskval)<2e-13,'quadrature')
    ck('Q04 finite-radius center error bound z='+str(zval),abs(value-central)<finite_bound,'quadrature')
    ck('Q05 center vector is zero z='+str(zval),np.linalg.norm(field(c,source_single))<1e-16,'quadrature')
    coax.append(dict(z_over_width=zval,radius_over_width=af,contour=value,center_curl_component=central,
        center_vector=field(c,source_single).tolist(),single_integral=exactquad,quad_error=quaderr,
        disk_flux=diskval,center_error_bound=finite_bound,positive_lower_bound=lower,
        actual_body_center=c-kf*eyn,body_center_vector=field(c-kf*eyn,source_single).tolist()))
    coax[-1]['actual_body_center']=coax[-1]['actual_body_center'].tolist()
ck('Q13 coaxial circle center differs from the body center readout',
   all(np.linalg.norm(q['body_center_vector'])>1e-8 for q in coax),'quadrature')
ck('Q06 empty source contour is zero',contour(np.array([4.,0,0]),eyn,ezn,af,[(np.zeros(3),eyn,ezn,0.)],64)==0.,'quadrature')
original=contour(np.array([4.,0,0]),eyn,ezn,af,[(np.zeros(3),eyn,ezn,1.)],128)
negative=contour(np.array([4.,0,0]),eyn,ezn,af,[(np.zeros(3),eyn,ezn,-1.)],128)
reverse=contour(np.array([4.,0,0]),eyn,-ezn,af,[(np.zeros(3),eyn,ezn,1.)],128)
ck('Q07 source reversal flips contour',abs(original+negative)<1e-16,'quadrature')
ck('Q08 measured orientation reversal flips contour',abs(original+reverse)<1e-16,'quadrature')
native=[]
for radius in [100.,200.]:
    c=np.array([0.,0.,radius])
    vals=[contour(c,ezn,exn,af,loops,n) for n in [64,128,256]]
    disk=disk_flux(c,ezn,exn,af,loops)
    leading=-af**2*float(W[1])/(4*radius**3)
    J=float(np.sum(np.abs(jnum)))
    error=J*(6*af**2*kf/(radius-kf)**4+1.5*af**4/(radius-kf-af)**5
              +1.5*af**4/(radius-kf-2*af)**5)
    conjugate=contour(c,ezn,exn,af,[(x,y,z,-w) for x,y,z,w in loops],128)
    ck('Q09 native sign and proved envelope R='+str(radius),
       vals[-1]<0 and abs(vals[-1]-leading)<error<abs(leading)/3,'quadrature')
    ck('Q10 quadrature refinement agreement R='+str(radius),
       max(abs(v-vals[-1]) for v in vals)<abs(leading)*1e-8,'quadrature')
    ck('Q11 native Stokes agreement R='+str(radius),abs(disk-vals[-1])<abs(leading)*1e-8,'quadrature')
    ck('Q12 conjugate produces exact opposite sample R='+str(radius),abs(conjugate+vals[1])<abs(leading)*1e-12,'quadrature')
    native.append(dict(R_over_width=radius,receiving_radius=af,normal=[0,1,0],contour_by_N=dict(zip([64,128,256],vals)),
       disk_flux=disk,leading_component=leading,absolute_error_bound=error,
       conjugate=conjugate,center_vector=field(c,loops).tolist(),
       disk_clearance_lower_bound=radius-kf-2*af,complete_disk_delay_upper_bound=radius+kf+2*af))
    if radius==100.:
        count=1024;delta=radius-kf-2*af
        fsecond=af*J/2*(2*af**2/delta**3+3*af/delta**2+1/delta)
        samplebound=2*np.pi**2*fsecond/(3*af*count**2)
        sampled=contour(c,ezn,exn,af,loops,count)
        ck('Q14 certified finite-sampling bound resolves the native sign at R=100w',
           samplebound<abs(leading)*2/3,'bound evaluation')
        ck('Q15 finite sample agrees with high-resolution integral check',
           abs(sampled-vals[-1])<samplebound and sampled<0,'quadrature')
        native[-1]['discrete_sensor_benchmark']=dict(N=count,value=sampled,
            ideal_sample_quadrature_error_bound=samplebound,continuous_sign_margin=abs(leading)*2/3)

runpy.run_path(str(ROOT/'inputs/order/GM05_REVIEW_CONTROLS.py'))
ck('R01 all six supplied GM05 offset corrections pass',True,'review-control script')
src=json.loads((ROOT/'SOURCE_VERIFICATION.json').read_text('utf-8'))
ck('V01 all 24 primary bytes and blobs match',all(
    hashlib.sha256((ROOT/r['saved_as']).read_bytes()).hexdigest()==r['sha256'] and
    hashlib.sha1(b'blob '+str(r['bytes']).encode()+b'\0'+(ROOT/r['saved_as']).read_bytes()).hexdigest()==r['git_blob']
    for r in src['sources']),'byte identity')
result=dict(status='PASS',checks=len(rows),results=rows,environment=dict(conda=os.environ['CONDA_DEFAULT_ENV'],
    python=sys.version,platform=platform.platform(),sympy=s.__version__,numpy=np.__version__,scipy=scipy.__version__),
    geometry=dict(Kc=kf,radius_over_width=af),coaxial=coax,native=native,
    rational_far_bound=str(bound),rational_far_bound_decimal=float(bound),
    rational_sample_ratio_bound=str(sample_ratio_bound),runtime_seconds=time.time()-t0,
    scope='Written arguments establish finite-radius strict sign and the all-R>=100w certificate; floating quadrature only corroborates selected values. No production or historical suite imported.')
(ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','geometry','rational_far_bound_decimal','native','runtime_seconds']},indent=2))
