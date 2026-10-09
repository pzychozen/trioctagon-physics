"""Isolated support for PUB-LT-02; no imports from any project source.
Each record is one named assertion, not a claim to have tested a theorem.
Exact algebra, exact witnesses and finite numerical illustrations are separate.
Owner execution uses cmd.exe / conda torment / python -B.
Portable execution only requires Python, SymPy, NumPy and mpmath.
"""
from pathlib import Path
import sys,os,json,platform,hashlib
import sympy as S
import numpy as np
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
records=[]
def check(name,kind,value,detail):
    ok=bool(value)
    records.append({"name":name,"kind":kind,"passed":ok,"detail":detail})
    if not ok:raise AssertionError(name)
def exact(name,expr,detail):
    check(name,"exact symbolic identity",S.simplify(S.trigsimp(S.expand_trig(expr)))==0,detail)
def small(name,value,tol,detail):
    check(name,"finite numerical illustration",np.isfinite(value) and value<=tol,
          {"observed":float(value),"tolerance":tol,"description":detail})

theta,phi=S.symbols("theta phi",real=True)
R,r,h,a,d=S.symbols("R r h a d",positive=True)
q=R+r*S.cos(theta)
X=S.Matrix([q*S.cos(phi),q*S.sin(phi),r*S.sin(theta)])
Xt=X.diff(theta);Xp=X.diff(phi)
exact("T01 metric theta",Xt.dot(Xt)-r*r,"Derivative of actual three-component chart.")
exact("T01 metric phi",Xp.dot(Xp)-q*q,"Derivative of actual three-component chart.")
exact("T01 metric cross",Xt.dot(Xp),"Orthogonality.")
ss=S.symbols("s",positive=True);nn=S.symbols("n",integer=True,nonnegative=True)
check("T01 component homothety","exact symbolic identity",
      all(S.simplify(v)==0 for v in X.subs({R:R*ss**nn,r:r*ss**nn})-ss**nn*X),
      "Componentwise equality, not a cancellation-prone scalar proxy.")
check("T01 horn collapse","exact symbolic identity",X.subs(theta,S.pi)==S.Matrix([(R-r)*S.cos(phi),(R-r)*S.sin(phi),0]),"At R=r every phi is origin.")
check("T01 spindle rank","exact witness",
      Xp.subs({R:S.Rational(1,2),r:1,theta:2*S.pi/3})==S.zeros(3,1) and
      S.simplify(Xt.dot(Xt).subs(r,1))==1,"a=1/2 seam: phi derivative zero, theta derivative nonzero.")

u=(d*d+r*r-h*h*r*r)/(2*d)
height=r*r-u*u
factor=(((h+1)**2*r*r-d*d)*(d*d-(h-1)**2*r*r))/(4*d*d)
exact("T02 circle height factor",height-factor,"Necessity/sufficiency algebra for real meridian intersections.")
exact("T02 same-side upper tangency",height.subs(d,(h+1)*r),"Outer triangle equality.")
exact("T02 reflected lower tangency",height.subs(d,(h-1)*r),"Inner triangle equality.")
gold=(1+S.sqrt(5))/2
exact("T02 golden lower",(gold-1)/(gold+1)-gold**(-3),"Fixed aspect comparison.")
exact("T02 golden upper",(gold+1)/(gold-1)-gold**3,"Fixed aspect comparison.")
check("T02 fixed aspect three scales","finite numerical illustration",
      (gold.evalf()+1)/(gold.evalf()-1)>3 and (np.e+1)/(np.e-1)<3 and (np.pi+1)/(np.pi-1)<3,
      "a=3: golden adjacent interval admits; e and pi exclude.")
pw=S.Matrix([S.Rational(3,4),0,S.sqrt(15)/4])
xs=S.Matrix([S.Rational(1,2)+S.Rational(1,4),0,S.sqrt(15)/4])
xl=S.Matrix([-(1+2*S.Rational(-7,8)),0,2*S.sqrt(15)/8])
check("T02 actual two-chart witness","exact witness",pw==xs==xl,"Signed q=-3/4 with phi=pi used for larger chart.")
exact("T02 witness small boundary",(pw[0]-S.Rational(1,2))**2+pw[2]**2-1,"Actual body equation.")
check("T02 witness large interior","exact witness",(pw[0]-1)**2+pw[2]**2==1 and S.Integer(1)<4,"Distance squared 1 versus radius squared 4.")
exact("T02 inner sheet body relation",(-q-R)**2+(r*S.sin(theta))**2-r*r-4*R*q,"Signed sheet formula.")

def chart(r,a,th,ph):
    return np.array([(a*r+r*np.cos(th))*np.cos(ph),(a*r+r*np.cos(th))*np.sin(ph),r*np.sin(th)])
maxerr=0.;cases=0
for hh in [1.25,2.,3.5]:
    lo=(hh-1)/(hh+1);hi=(hh+1)/(hh-1)
    for aa in [lo,(lo+1)/2,1.,(1+hi)/2,hi]:
        sg=1 if aa>=1 else -1
        c1=aa;c2=sg*aa*hh;dist=abs(c2-c1)
        l=(dist*dist+1-hh*hh)/(2*dist)
        uu=c1+np.sign(c2-c1)*l;zz=np.sqrt(max(0,1-l*l))
        # Recover original signed meridian angles, then same spatial meridian.
        th1=np.arctan2(zz,uu-aa)
        th2=np.arctan2(zz,sg*uu-aa*hh)
        p1=chart(1,aa,th1,0)
        p2=chart(hh,aa,th2,0 if sg==1 else np.pi)
        maxerr=max(maxerr,float(np.linalg.norm(p1-p2)));cases+=1
small("T02 full-chart intersection roundtrip",maxerr,2e-7,{"cases":cases,"includes":"L, U and horn for each h; both actual charts evaluated"})
rng=np.random.default_rng(10092026)
margin_violation=-np.inf;bodycases=0
for aa in [.1,.5,.95]:
    for rn,rm in [(1,1.2),(1,2),(2,7)]:
        for _ in range(120):
            th=rng.uniform(0,2*np.pi);rad=rn*np.sqrt(rng.uniform())
            rho=aa*rn+rad*np.cos(th);z=rad*np.sin(th)
            if rho<0:continue
            dm=np.hypot(rho-aa*rm,z)
            margin_violation=max(margin_violation,dm-(rm-(1-aa)*(rm-rn)));bodycases+=1
check("T02 body margin sample","finite numerical illustration",margin_violation<=1e-12,
      {"points":bodycases,"max_excess_over_proved_bound":margin_violation,"scope":"Random interior points; analytic triangle proof supplies universal assertion."})

ur,ui,vr,vi,p=S.symbols("ur ui vr vi p",real=True)
U=ur+S.I*ui;V=vr+S.I*vi
c0=(S.Abs(U)**2+S.Abs(V)**2)/2;c1=(S.Abs(U)**2-S.Abs(V)**2)/2;c2=-S.re(U*S.conjugate(V))
amp=U*S.cos(p)-V*S.sin(p)
exact("T03 complex intensity expansion",S.expand_complex(amp*S.conjugate(amp))-(c0+c1*S.cos(2*p)+c2*S.sin(2*p)),"Four independent real amplitude components.")
exact("T03 modulation identity",c0*c0-c1*c1-c2*c2-S.im(U*S.conjugate(V))**2,"General complex pair.")
ca,cb,cc=S.symbols("a b c",real=True)
mat=S.Matrix([[1,S.cos(2*v),S.sin(2*v)] for v in [ca,cb,cc]])
exact("T03 determinant",mat.det()-4*S.sin(cb-ca)*S.sin(cc-cb)*S.sin(cc-ca),"General known phases, correct row order.")
cv=S.Matrix(S.symbols("c0 c1 c2",real=True))
special=mat.subs({ca:0,cb:S.pi/4,cc:S.pi/2});pv=special*cv
check("T03 three-sample inverse","exact symbolic identity",
      S.Matrix([(pv[0]+pv[2])/2,(pv[0]-pv[2])/2,pv[1]-(pv[0]+pv[2])/2])==cv,
      "Recovers all three coefficients.")
exact("T03 abstract ambiguity plus",S.expand_complex((S.cos(p)-S.I*S.sin(p))*(S.cos(p)+S.I*S.sin(p)))-1,"Abstract pairs only, no restricted-family realization asserted.")
check("T03 singular congruent phases","exact symbolic identity",mat.subs({cb:ca+S.pi}).det().simplify()==0,"Known-phase distinction modulo pi.")
beta=S.symbols("beta",real=True)
exact("T03 one-shell blink",S.cos((S.pi/2-beta)+beta),"Whole pattern factor vanishes.")
testph=np.array([0,.01,1.2]);M=np.c_[np.ones(3),np.cos(2*testph),np.sin(2*testph)]
nearly=np.array([0,1e-7,1.2]);Mn=np.c_[np.ones(3),np.cos(2*nearly),np.sin(2*nearly)]
check("T03 conditioning illustration","finite numerical illustration",np.linalg.cond(Mn)>np.linalg.cond(M)>1,
      {"condition_2_at_0.01":float(np.linalg.cond(M)),"condition_2_at_1e-7":float(np.linalg.cond(Mn)),"scope":"No universal noise/optimization theorem."})

C,alpha=S.symbols("C alpha",real=True)
D=(X-S.Matrix([C,0,0])).dot(X-S.Matrix([C,0,0]))
Dformula=R*R+r*r+C*C+2*R*r*S.cos(theta)-2*C*q*S.cos(phi)
exact("T03 Gaussian distance",D-Dformula,"Actual 3D norm versus source expansion.")
exact("T04 azimuth reflection",Dformula.subs(phi,-phi)-Dformula,"Algebra supporting written reflection proof.")
x=S.symbols("x",real=True)
l1,l2,l3=S.symbols("l1 l2 l3",real=True)
vander=S.Matrix([[ll**i for ll in [l1,l2,l3]] for i in range(3)])
exact("T04 Vandermonde illustration",vander.det()-(l2-l1)*(l3-l1)*(l3-l2),"Three-exponent algebra; general independence is proved in manuscript.")
lam=2*.13*.8*(2+.5)*1.3**np.arange(7)
check("T04 unique extreme exponent illustration","finite numerical illustration",
      max(lam[i]+lam[j] for i in range(7) for j in range(7) if (i,j)!=(6,6))<2*lam[6],
      "Finite ordered example supports, but does not certify, analytic extreme-diagonal argument.")

exact("T05 area integral",S.integrate(r*(R+r*S.cos(theta)),(theta,0,2*S.pi))*2*S.pi-4*S.pi**2*R*r,"Ring sign q>0 assumed.")
exact("T05 homothetic area",r*ss**nn*(R*ss**nn+r*ss**nn*S.cos(theta))-ss**(2*nn)*r*q,"Pullback measure scaling.")
Z0=S.symbols("Z0",positive=True);P=S.symbols("P",nonnegative=True)
exact("T05 normalized pullback equality",(P/(ss**(2*nn)*Z0))*(ss**(2*nn)*r*q)-(P/Z0)*(r*q),"Z0>0 explicitly.")
xx,yy,zz=S.symbols("x y z",real=True)
Q=(xx*xx+yy*yy+zz*zz+R*R-r*r)**2-4*R*R*(xx*xx+yy*yy)
exact("T05 polynomial vanishes",Q.subs({xx:X[0],yy:X[1],zz:X[2]},simultaneous=True),"Actual chart substituted.")
check("T05 distinct ambient extension witness","exact witness",Q.subs({xx:0,yy:0,zz:0,R:2,r:1})==9,"Ring reference, h=1.")
vec=S.Matrix([xx,yy,zz])
exact("T05 reference pullback norm",(ss**nn*vec-S.Matrix([C,0,0])).dot(ss**nn*vec-S.Matrix([C,0,0]))-
      ss**(2*nn)*(vec-S.Matrix([C*ss**(-nn),0,0])).dot(vec-S.Matrix([C*ss**(-nn),0,0])),"Exact centre/precision rescaling.")

mp.mp.dps=60
def hist(k,q,z,H,R=mp.mpf(2),rmax=mp.mpf(1),M=12):
    th=2*mp.pi*(q%M)/M;rr=rmax*k/(1+k);chi=mp.pi*z/(2*H)
    return (R+rr*mp.cos(chi))*mp.cos(th),(R+rr*mp.cos(chi))*mp.sin(th),rr*mp.sin(chi),chi
def hinv(pt,H):
    X,Y,Z,_=pt;rho=mp.sqrt(X*X+Y*Y);rr=mp.sqrt((rho-2)**2+Z*Z)
    chi=mp.atan2(Z,rho-2)
    return rr/(1-rr),2*H*chi/mp.pi,mp.atan2(Y,X)%(2*mp.pi)
maxerr=mp.mpf(0)
for kval in [mp.mpf(".001"),mp.mpf(".4"),mp.mpf(1),mp.mpf(100)]:
    for qv in [-13,0,4,29]:
        for zv in [mp.mpf("-1.7"),mp.mpf(0),mp.mpf(".8")]:
            H=mp.mpf(2)+mp.mpf("1e-9")
            k2,z2,t2=hinv(hist(kval,qv,zv,H),H)
            errphase=abs(mp.e**(1j*t2)-mp.e**(1j*2*mp.pi*(qv%12)/12))
            maxerr=max(maxerr,abs(kval-k2),abs(zv-z2),errphase)
small("T06 history XYZ inverse",float(maxerr),1e-50,"48 positive-radius point roundtrips; known H,R,rmax,M.")
Hz=mp.mpf(3)+mp.mpf("1e-9")
pzero1=hist(mp.mpf(0),2,mp.mpf(1),Hz);pzero2=hist(mp.mpf(0),2,mp.mpf(-2),Hz)
check("T06 XYZ zero scalar fibre","exact-domain numerical witness",pzero1[:3]==pzero2[:3] and pzero1[3]!=pzero2[3],"Another row fixes max |z|=3; richer chi differs.")
small("T06 rich record scalar at zero",float(abs(2*Hz*pzero2[3]/mp.pi+2)),1e-50,"Actual stored chi and H, even at kappa=0.")
check("T06 cylinder zero fibre","exact witness",S.Matrix([0,0,1])!=S.Matrix([0,0,2]) and
      0*S.cos(S.pi/3)==0*S.cos(2*S.pi/3),"Height retained, different admissible azimuths collapse.")
hbefore=mp.mpf(1)+mp.mpf("1e-9");hafter=mp.mpf(2)+mp.mpf("1e-9")
check("T06 append generally moves point","finite numerical illustration",
      hist(mp.mpf(1),1,mp.mpf(".5"),hbefore)[:3]!=hist(mp.mpf(1),1,mp.mpf(".5"),hafter)[:3],
      "Same stored nonzero scalar and radius, larger whole-history maximum.")
check("T06 append exceptions","exact-domain numerical witness",
      hist(mp.mpf(0),1,mp.mpf(".5"),hbefore)[:3]==hist(mp.mpf(0),1,mp.mpf(".5"),hafter)[:3] and
      hist(mp.mpf(1),1,mp.mpf(0),hbefore)[:3]==hist(mp.mpf(1),1,mp.mpf(0),hafter)[:3],
      "Zero kappa and zero scalar cases are separate exceptions.")

rc=S.symbols("rc",positive=True);ct=S.symbols("ct",real=True)
exact("T06 negative wireframe equation",(-R-rc*ct-R)**2+rc**2*(1-ct**2)-(rc**2+4*R*rc*ct+4*R**2),"Signed u branch, true cylindrical radius |u|.")
cosreq=(r*r-4*R*R-rc*rc)/(4*R*rc)
exact("T06 re-entry signed projection",R+rc*cosreq-(r*r-rc*rc)/(4*R),"Branch consistency.")
exact("T06 re-entry lower cosine factor",4*R*rc*(cosreq+1)-(r*r-(rc-2*R)**2),"Phase existence iff |rc-2R|<=r.")
check("T06 exact nonzero wireframe witness","exact witness",
      (S.Rational(7,5)-2)**2==S.Rational(3,5)**2 and
      S.Rational(3,5)*(1+S.Rational(2,5)*S.Rational(35,3))==S.Rational(17,5),
      "Omega=-(exp(35/3)-1), x=-7/5, radius17/5; nonzero, not a radius-only proxy.")
maxerr=0.
for label in [0,2*np.pi/3,4*np.pi/3]:
    for mag in [0,.1,3,1000,np.expm1(35/3)]:
        for ang in [0,.7,np.pi,5.1]:
            rc0=.6*(1+.4*np.log1p(mag));u0=2+rc0*np.cos(ang)
            X0=u0*np.cos(label);Y0=u0*np.sin(label);Z0=rc0*np.sin(ang)
            u1=X0*np.cos(label)+Y0*np.sin(label)
            rc1=np.hypot(u1-2,Z0);mag1=np.expm1((rc1/.6-1)/.4)
            om1=mag1*complex(u1-2,Z0)/rc1;om0=mag*np.exp(1j*ang)
            maxerr=max(maxerr,abs(om1-om0)/max(1,mag))
small("T06 signed labelled channel inverse",maxerr,3e-14,"60 point roundtrips including negative u, zero convention, three labels.")
check("T06 large modulus not forced crossing","finite numerical illustration",
      2+3.4>0 and 2-3.4<0,"Same radius, phase0 versus phasepi.")
maxres=0.
for rv in np.linspace(3.4,4.6,101):
    cv=(.6**2-4*2**2-rv**2)/(4*2*rv)
    ang=np.arccos(np.clip(cv,-1,1));uu=2+rv*np.cos(ang);zz=rv*np.sin(ang)
    maxres=max(maxres,abs((abs(uu)-2)**2+zz*zz-.6**2))
    assert uu<0
small("T06 re-entry actual spatial equation",maxres,2e-14,"101 radius/phase pairs across full admitted band, includes endpoints.")

tt=S.symbols("t",real=True)
delta=S.Rational(1,10)*S.sin(5*tt)
rtpoint=S.Matrix([(R+r*S.cos(tt)+delta)*S.cos(tt),(R+r*S.cos(tt)+delta)*S.sin(tt),r*S.sin(tt)]).subs(tt,S.pi/2)
check("T07 perturbed curve actual point","exact witness",rtpoint==S.Matrix([0,R+S.Rational(1,10),r]),
      "All three components evaluated, not claiming sampled t-grid includes pi/2.")
rtmetric=(S.sqrt(rtpoint[0]**2+rtpoint[1]**2)-R)**2+rtpoint[2]**2
exact("T07 actual spatial tube distance",rtmetric-r*r-S.Rational(1,100),
      "Actual cylindrical radius of evaluated curve with positive R; differs from torus radius squared.")
floor=np.maximum(np.array([0.,1e-14,1e-12,1.]),1e-12)
check("Display energy floor fibres","finite numerical illustration",floor[0]==floor[1]==floor[2] and floor[3]>floor[2],"Log transform cannot undo floor.")
check("Display brightness clipping fibres","finite numerical illustration",
      np.clip(0.,.15,1)==np.clip(.1,.15,1) and np.clip(2.,.15,1)==np.clip(3.,.15,1),"Separate lower and upper saturation.")
vectors=np.array([[1.,0.,0.],[0,2,0],[0,0,4.]])
denom=np.percentile(np.linalg.norm(vectors,axis=1),99);scale=.85*3/denom
small("Display percentile scale inverse",float(np.max(abs((scale*vectors)/scale-vectors))),1e-14,"Known actual scalar scale and Cartesian frame only.")

out={"status":"PASS","assertions":len(records),"records":records,
 "scope":"New isolated manuscript checks only. No old suites replayed; no runtime imports. Counts are named assertions, not independent theorems or novelty evidence.",
 "environment":{"python":sys.version,"executable":sys.executable,"conda_default_env":os.environ.get("CONDA_DEFAULT_ENV"),
 "platform":platform.platform(),"sympy":S.__version__,"numpy":np.__version__,"mpmath":mp.__version__},
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/"evidence/CHECK_RESULTS.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"status":out["status"],"assertions":len(records),"by_kind":{k:sum(v["kind"]==k for v in records) for k in sorted(set(v["kind"] for v in records))}}))
