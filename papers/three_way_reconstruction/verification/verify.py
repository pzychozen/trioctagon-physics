"""Exact identities, finite monodromy, and 100-digit consistency checks.
Run with Python containing sympy and mpmath. Only writes results in this directory.
"""
from pathlib import Path
import json, platform
import sympy as S
import mpmath as mp

OUT=Path(__file__).resolve().parent
A,B,y,x,u,z,t,a,h,s,nu,M,W=S.symbols('A B y x u z t a h s nu M W')
c=A+1; D=y*y-B*y+A; N=A*y*y-B*y+1; Delta=c*c-B*B
F=N/D; T=(c*y-B)/(B*y-c); lam=(A-1)**2/Delta
H=c*(y*y+1)-2*B*y; beta=H**2/(Delta*(y*y-1)**2)
checks=[]
def check(name, value):
    ok=S.cancel(S.factor(value))==0
    checks.append({'name':name,'passed':bool(ok)})
    if not ok: raise AssertionError((name,S.factor(value)))
check('reciprocity',F*F.subs(y,1/y)-1)
check('plus-one identity',N+D-H)
check('minus-one identity',N-D-(A-1)*(y*y-1))
check('resultant',S.resultant(N,D,y)-(A-1)**2*Delta)
check('critical polynomial',S.diff(F,y)-(A-1)*(-B*y*y+2*c*y-B)/D**2)
check('sensitivity A',S.diff(F,A)-(y*y-1)*(y*y-B*y+1)/D**2)
check('sensitivity B',S.diff(F,B)-(A-1)*y*(y*y-1)/D**2)
check('T involution',T.subs(y,T)-y)
check('R commutes T',T.subs(y,1/y)-1/T)
check('equal value involution',F.subs(y,T)-F)
check('quotient reciprocal invariant',beta.subs(y,1/y)-beta)
check('quotient T invariant',beta.subs(y,T)-beta)
check('marked fiber identity',beta-lam-4*N*D/(Delta*(y*y-1)**2))
check('output to quotient',beta-lam*((F+1)/(F-1))**2)
check('lambda boundary',lam-1-(B*B-4*A)/Delta)
check('nu lambda boundary',c*c/Delta-lam-4*A/Delta)
check('cancel positive lock',F.subs(B,c)-(A*y-1)/(y-A))
check('cancel negative lock',F.subs(B,-c)-(A*y+1)/(y+A))
check('constant positive',F.subs(A,1)-1)
check('constant negative',F.subs({A:-1,B:0})+1)
C,v0=S.symbols('C v0'); NC=A*y*y-B*y+C
check('historical C extension failure',NC*y*y*NC.subs(y,1/y)-D*y*y*D.subs(y,1/y)-(C-1)*(A*(y**4+1)-B*(y**3+y)+(C+1)*y*y))
check('equal level factorization',N.subs(y,v0)*D-N*D.subs(y,v0)-(A-1)*(v0-y)*(c*(v0+y)-B*(v0*y+1)))
check('B reflection',F.subs(B,-B)-F.subs(y,-y))
check('coefficient inversion',F.subs({A:1/A,B:B/A}, simultaneous=True)-1/F)
# Parametrize coherent roots by source scale a and level k.
k=S.symbols('k'); coeff={A:(a+1/a+k)/(a+1/a-k),B:2*(a-1/a)/(a+1/a-k)}
us=a*(y-1)/(y+1); rs=us+1/us
check('coherent normal form',F.subs(coeff, simultaneous=True)-(rs+k)/(rs-k))
check('normalized R',us.subs(y,1/y)+us)
check('normalized T',us.subs(y,T).subs(coeff, simultaneous=True)-1/us)
bu=(u+1/u)**2/4
check('Belyi derivative',S.diff(bu,u)-(u**4-1)/(2*u**3))
check('source beta',beta.subs(coeff, simultaneous=True)-bu.subs(u,us))
nv=c*c/Delta
check('parameter Jacobian',S.det(S.Matrix([[S.diff(lam,A),S.diff(lam,B)],[S.diff(nv,A),S.diff(nv,B)]]))-8*B*c*(A-1)/Delta**3)
Q=(x**4-2*t*x*x+1)**2/((1-t*t)*(x**4-1)**2)
check('Q one branch',(Q-1)-(t*(x**4+1)-2*x*x)**2/((1-t*t)*(x**4-1)**2))
check('Q nu branch',(Q-1/(1-t*t))-4*x*x*(1-t*x*x)*(x*x-t)/((1-t*t)*(x**4-1)**2))
check('Q sign equivalence',Q.subs({t:-t,x:S.I*x}, simultaneous=True)-Q)
check('Q reciprocal',Q.subs(x,1/x)-Q)
check('Q parity',Q.subs(x,-x)-Q)
check('dihedral B zero',Q.subs(t,0).subs(x,S.I*x)-Q.subs(t,0))
check('dihedral c zero',S.limit(Q,t,S.oo)+4*x**4/(x**4-1)**2)
# Scaling identities, h=1/sqrt(L).
L=S.symbols('L',positive=True); f=F.subs({A:L,B:L,y:x*x}, simultaneous=True)
check('bulk error',f+x*x-(x**6+1)/(x**4+L*(1-x*x)))
Ph=((s*s+2)+2*h*s+h*h*s*s)/(-s+h*(1+h*s)**2)
fh=F.subs({A:1/h**2,B:1/h**2,y:1+h*s}, simultaneous=True)
check('intermediate exact',(fh+1)/h-Ph)
check('intermediate limit',S.limit(Ph,h,0)+s+2/s)
check('intermediate first correction',S.limit((Ph+s+2/s)/h,h,0)+3+2/s**2)
Rh=-s/(1+h*s); Jh=(h*s+2)/(s-h)
check('intermediate R',Ph.subs(s,Rh)+Ph/(1-h*Ph))
check('intermediate T',Ph.subs(s,Jh)-Ph)
check('intermediate commuting involutions',Rh.subs(s,Jh)-Jh.subs(s,Rh))
check('intermediate derivative',S.diff(Ph,s)-(1-h*h)*(2+2*h*s-s*s)/(-s+h*(1+h*s)**2)**2)
tau,zet,eta=S.symbols('tau zet eta')
Fy=F.subs({A:L,B:L}, simultaneous=True)
check('thin limit',S.limit(Fy.subs(y,1+tau/L),L,S.oo)-(1+tau)/(1-tau))
check('inner limit',S.limit(L*Fy.subs(y,zet/L),L,S.oo)-(1-zet))
check('outer limit',S.limit(Fy.subs(y,L*eta)/L,L,S.oo)-eta/(eta-1))
check('inner reciprocal limit',S.limit(1/(L*Fy.subs(y,zet/L)),L,S.oo)-1/(1-zet))
check('outer reciprocal limit',S.limit(L/Fy.subs(y,L*eta),L,S.oo)-(eta-1)/eta)
check('thin reciprocal limit',S.limit(1/Fy.subs(y,1+tau/L),L,S.oo)-(1-tau)/(1+tau))
betaL=beta.subs({A:L,B:L}, simultaneous=True);lambdaL=lam.subs({A:L,B:L}, simultaneous=True)
check('bulk quotient limit',S.limit(2*betaL/L,L,S.oo)-((y-1)/(y+1))**2)
check('thin quotient limit',S.limit((2*betaL/L).subs(y,1+tau/L),L,S.oo)-1/tau**2)
check('intermediate quotient limit',S.limit(betaL.subs({L:1/h**2,y:1+h*s}, simultaneous=True),h,0)-(s+2/s)**2/8)
check('inner quotient marked gap',S.limit(betaL.subs(y,zet/L)-lambdaL,L,S.oo)-2*(1-zet))
check('outer quotient marked gap',S.limit(betaL.subs(y,L*eta)-lambdaL,L,S.oo)-2*(1-1/eta))
check('large L marked gap',nv.subs({A:L,B:L})-lam.subs({A:L,B:L})-4*L/(2*L+1))
# Elliptic equations reduced modulo the curve, no numerical substitution.
E=t*x*x*z*z-x*x-z*z+t
for name, subs in [('X',{x:-x}),('Y',{z:-z}),('S',{x:z,z:x})]:
    check('curve symmetry '+name,E.subs(subs, simultaneous=True)-E)
check('curve symmetry C',x*x*z*z*E.subs({x:1/x,z:1/z}, simultaneous=True)-E)
curve_z2=(x*x-t)/(t*x*x-1)
quartic=t*x**4-(t*t+1)*x*x+t
check('Jacobi quartic',(t*x*x-1)**2*curve_z2-quartic)
U,V=S.symbols('U V'); al=2*(1+t*t)/(1-t*t); gam=4/(1-t*t)
check('Edwards scaling',E.subs({x:a*U,z:a*V,t:a*a}, simultaneous=True)-a*a*(a**4*U*U*V*V-U*U-V*V+1))
mv=(1+V)/(1-V); nn=mv/U
expr=gam*nn**2-mv**3-al*mv**2-mv
check('Montgomery map',expr.subs(U**2,(1-V*V)/(1-t*t*V*V)))
q0=(1-a*a)/(1+a*a); ell=q0*(x-a)/(x+a); m=q0*q0
kappa=2*S.I*a*(a*a-1)/(a*a+1)**2
check('Legendre map',kappa*kappa*quartic.subs(t,a*a)/(x+a)**4-ell*(ell-1)*(ell-m))
alpha=4*nu-2; p=1-alpha*alpha/3; q=2*alpha**3/27-alpha/3
check('short p',p+(16*nu*nu-16*nu+1)/3)
check('short q',q-2*(2*nu-1)*(32*nu*nu-32*nu-1)/27)
check('Weierstrass discriminant',-16*(4*p**3+27*q*q)-256*nu*(nu-1))
jt=16*(t**4+14*t*t+1)**3/(t*t*(t*t-1)**4)
jn=16*(16*nu*nu-16*nu+1)**3/(nu*(nu-1))
mm=((t-1)/(t+1))**2; jm=256*(1-mm+mm*mm)**3/(mm*mm*(1-mm)**2)
check('j t nu',jt-jn.subs(nu,1/(1-t*t)))
check('j t Legendre',jt-jm)
check('j enhanced factor',jt-1728-16*(t*t+1)**2*(t*t-6*t+1)**2*(t*t+6*t+1)**2/(t*t*(t*t-1)**4))
Mp=M+alpha+1/M; wp2=(M**3+alpha*M*M+M)*(1-1/M**2)**2
check('two isogeny',wp2-Mp*(Mp-alpha-2)*(Mp-alpha+2))
check('boundary t one',E.subs(t,1)-(x*x-1)*(z*z-1))
check('boundary t negative one',E.subs(t,-1)+(x*x+1)*(z*z+1))
phi=(1+S.sqrt(5))/2
check('golden j',jt.subs(t,2-S.sqrt(5))-2048)
check('nine nine j',jt.subs(t,S.Rational(9,10))-S.Rational(8780093172522724,263900025))
check('nine one j',jt.subs(t,S.Rational(1,10))-S.Rational(5927735656804,2401490025))

def perm(*cycles):
    p=list(range(8))
    for cyc in cycles:
        for i,n in enumerate(cyc):p[n-1]=cyc[(i+1)%len(cyc)]-1
    return tuple(p)
def mul(p,q):return tuple(p[q[i]] for i in range(8))
perms=[perm((1,4),(2,3),(5,8),(6,7)),perm((1,3),(2,4),(5,7),(6,8)),perm((1,7),(2,8)),perm((1,8),(2,7),(3,4),(5,6))]
ident=tuple(range(8)); group={ident}; todo=[ident]
while todo:
    p0=todo.pop()
    for q0 in perms:
        pq=mul(p0,q0)
        if pq not in group:group.add(pq);todo.append(pq)
assert len(group)==16 and mul(mul(mul(perms[0],perms[1]),perms[2]),perms[3])==ident
assert len({g[0] for g in group})==8

mp.mp.dps=100
def fm(A,B,y):return (A*y*y-B*y+1)/(y*y-B*y+A)
pairs=[(9,9),(9,1),(mp.pi,mp.e),((1+mp.sqrt(5))/2,(1-mp.sqrt(5))/2),(2,4),(-2,mp.mpf('.5')),(0,2),(-1,2),(1,0),(2,mp.mpf('2.999999')),(2,-4),(5,-1)]
pts=[mp.mpc('.3','.4'),mp.mpc('-1.2','.7'),mp.mpc('2.1','-.2'),mp.mpc('.1','1.3')]
errors=[]
for aa,bb in pairs:
    aa,bb=mp.mpf(aa),mp.mpf(bb);dd=mp.sqrt((aa+1)**2-bb*bb);rho=(aa+1+bb)/dd;kk=2*(aa-1)/dd
    for yy in pts:
        uu=rho*(yy-1)/(yy+1);rr=uu+1/uu
        value=fm(aa,bb,yy);normal=(rr+kk)/(rr-kk)
        errors.append(abs(value-normal)/max(1,abs(value),abs(normal)))
examples=[]
for name,(aa,bb) in zip(['9,9','9,1','pi,e','phi,1-phi'],pairs[:4]):
    aa,bb=mp.mpf(aa),mp.mpf(bb);delta=(aa+1)**2-bb*bb;tt=bb/(aa+1);vv=1/(1-tt*tt);mm=((tt-1)/(tt+1))**2
    j1=16*(tt**4+14*tt*tt+1)**3/(tt*tt*(tt*tt-1)**4);j2=16*(16*vv*vv-16*vv+1)**3/(vv*(vv-1));j3=256*(1-mm+mm*mm)**3/(mm*mm*(1-mm)**2)
    vals=dict(a=(aa+1+bb)/mp.sqrt(delta),k=2*(aa-1)/mp.sqrt(delta),lambda_=(aa-1)**2/delta,nu=vv,t=tt,m=mm,j=j1,j_relative_error=max(abs(j1-j2),abs(j1-j3))/abs(j1))
    examples.append(dict(name=name,**{k:mp.nstr(v,101) for k,v in vals.items()}))
scaling=[]
for ll in [mp.mpf('1e4'),mp.mpf('1e8'),mp.mpf('1e12')]:
    hh=1/mp.sqrt(ll);sslist=[-3,-mp.sqrt(2),mp.mpf('-.5'),mp.mpf('.5'),mp.sqrt(2),3]
    es=[abs((fm(ll,ll,1+hh*ss)+1)/hh+ss+2/ss) for ss in sslist]
    db=ll**(-mp.mpf('0.25'));dl=ll**(-mp.mpf('0.75'))
    scaling.append(dict(L=mp.nstr(ll),intermediate_max_error=mp.nstr(max(es),20),error_over_h=mp.nstr(max(es)/hh,20),bulk_overlap_relative_error=mp.nstr(abs((fm(ll,ll,1+db)+1)/(-db)-1),20),lock_overlap_relative_error=mp.nstr(abs((fm(ll,ll,1+dl)+1)/(-2/(ll*dl))-1),20)))
result=dict(python=platform.python_version(),sympy=S.__version__,mpmath=mp.__version__,precision_digits=mp.mp.dps,exact_checks=checks,exact_count=len(checks),monodromy=dict(order=len(group),transitive=True,product_identity=True),normal_form_cases=len(errors),max_normal_form_relative_error=mp.nstr(max(errors),20),historical_examples=examples,scaling=scaling)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:result[k] for k in ['exact_count','monodromy','normal_form_cases','max_normal_form_relative_error','scaling']},indent=2))
