"""Paper F independent exact checks. No evolution APIs, old verifiers, or writes.

Universal component algebra t**3=t/2+sigma/(3*sqrt(6)) reconstructs the
coefficient maps; prior stdout is never used as the calculation oracle.
The two-seed CSV is inspected as immutable finite evidence, not replayed.
"""
from pathlib import Path
import ast
import csv
import hashlib
import json
import math
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "research/GATE_TORUS_INVESTIGATION_v0.1"
checks = []
rt = S.sqrt
e = S.ones(3, 1)
u = S.Matrix([1,-1,0])/rt(2)
v = S.Matrix([1,1,-2])/rt(6)
E = S.Matrix.hstack(u,v)
L = e*e.T-3*S.eye(3)
a,r,ep,lam,g = S.symbols("a r epsilon lambda g", real=True)
h,t,sigma = S.symbols("h t sigma")
c,s = S.symbols("c s", real=True)
q = c*u+s*v
qp = -s*u+c*v

def simp(z):
    return S.factor(S.cancel(z))

def circle(z):
    return simp(S.rem(S.expand(z),c*c+s*s-1,c))

def check(name, value, circular=False):
    vals = list(value) if isinstance(value,S.MatrixBase) else [value]
    fn = circle if circular else simp
    residual = [fn(x) for x in vals]
    good = all(x == 0 for x in residual)
    checks.append({"id":name,"passed":good,"residuals":[str(x) for x in residual]})
    print('CHECK '+name+': '+str(good),file=sys.stderr,flush=True)
    if not good:
        raise AssertionError((name,residual))

def truth(name, condition, details=None):
    checks.append({"id":name,"passed":bool(condition),"details":details})
    if not condition:
        raise AssertionError((name,details))

# Universal three-root algebra. Trace is sum over all three channel entries.
polynomial = t**3-t/2-sigma/(3*rt(6))

def red(z):
    return S.expand(S.rem(S.expand(z),polynomial,t))

def trace(z):
    z=red(z)
    return simp(3*z.coeff(t,0)+z.coeff(t,2))

def angle_part(z):
    # coefficient along q(phi+pi/2) is angle_part(z)*cos(3phi)
    return simp(red(z).coeff(t,2)/rt(6))

def historical_and_symmetry():
    check("F1.L3 sign and entries",L-S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]]))
    check("F1.common eigenspace",L*e)
    check("F1.transverse eigenspace",L*E+3*E)
    check("F4.orthonormality",E.T*E-S.eye(2))
    check("F4.transversality",e.T*E)
    check("F4.orientation",u.cross(v)-e/rt(3))
    check("F4.quarter turn",e.cross(q)-rt(3)*qp)
    P=S.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    T=S.Matrix([[0,1,0],[1,0,0],[0,0,1]])
    RP=S.Matrix([[-S.Rational(1,2),-rt(3)/2],[rt(3)/2,-S.Rational(1,2)]])
    ST=S.diag(-1,1)
    check("F4.cyclic generator +120 degrees",E.T*P*E-RP)
    check("F4.transposition phi maps pi-phi",E.T*T*E-ST)
    check("F4.D3 relations",RP**3-S.eye(2))
    check("F4.reflection involution",ST**2-S.eye(2))
    check("F4.reflection conjugates inverse",ST*RP*ST-RP.T)
    R6=-RP**2  # conjugation times squared 3-cycle
    check("F4.extended rotation +60 degrees",R6-S.Matrix([[S.Rational(1,2),-rt(3)/2],[rt(3)/2,S.Rational(1,2)]]))
    check("F4.D6 order-six relation",R6**6-S.eye(2))
    # exact modular orbit enumeration, phi=k*pi/6
    def orbits(mod, generators):
        remaining=set(range(mod)); answer=[]
        while remaining:
            found={min(remaining)}
            while True:
                extra={f(x)%mod for f in generators for x in found}
                if extra <= found: break
                found |= extra
            answer.append(sorted(found));remaining-=found
        return answer
    d3=orbits(12,[lambda k:k+4,lambda k:6-k])
    d6=orbits(12,[lambda k:k+2,lambda k:6-k])
    projective=orbits(6,[lambda k:k+4,lambda k:-k])
    truth("F6.oriented D3 has THREE orbits",sorted(map(len,d3))==[3,3,6],d3)
    truth("F6.oriented D6 has TWO orbits",sorted(map(len,d6))==[6,6],d6)
    truth("F6.projective D3 has TWO orbits",sorted(map(len,projective))==[3,3],projective)
    phi=S.symbols('phi',real=True)
    for name,expr in [
        ("psi rotation 60",S.sin(6*(phi+S.pi/3))-S.sin(6*phi)),
        ("psi reflection odd",S.sin(6*(S.pi-phi))+S.sin(6*phi)),
        ("elevation rotation 120",S.cos(3*(phi+2*S.pi/3))-S.cos(3*phi)),
        ("elevation conjugation odd",S.cos(3*(phi+S.pi))+S.cos(3*phi)),
        ("elevation reflection odd",S.cos(3*(S.pi-phi))+S.cos(3*phi))]:
        check("F5."+name,S.expand_trig(expr).expand().trigsimp())
    alpha,beta,x1,x2,y1,y2=S.symbols('alpha beta x1 x2 y1 y2',real=True)
    xi=S.Matrix([x1,x2,-x1-x2]);eta=S.Matrix([y1,y2,-y1-y2])
    xx=alpha*e+xi;yy=beta*e+eta
    cross=xx.cross(yy)
    check("F2.exact chirality decomposition",cross-e.cross(alpha*eta-beta*xi)-xi.cross(eta))
    check("F2.first term transverse",e.dot(e.cross(alpha*eta-beta*xi)))
    check("F2.second term longitudinal",xi.cross(eta)-xi.cross(eta).dot(e)*e/3)
    for label,mat in [('P',P),('T',T)]:
        check("F2.channel axial transformation "+label,(mat*xx).cross(mat*yy)-mat.det()*mat*cross)
    check("F2.common phase invariance",
          (c*xx-s*yy).cross(s*xx+c*yy)-cross,True)
    check("F2.conjugation reverses C",xx.cross(-yy)+cross)
    # Historical seed is a specified exact example, not a chosen direction theorem.
    seed=S.Matrix([S.Rational(1,5)+3*S.I/10,-S.Rational(2,5)+S.I/10,S.Rational(1,10)-S.I/5])
    mean=sum(seed)/3
    rotation=(-1-2*S.I)/rt(5)
    rotated=(rotation*seed).expand(complex=True)
    w=rt(5)/30
    xis=rotated.applyfunc(S.re)-w*e
    etas=rotated.applyfunc(S.im)
    cp=w*e.cross(etas);cl=xis.cross(etas)
    check("F3.mean",mean-(-1+2*S.I)/30)
    check("F3.phase rotation",rotation*mean-w)
    check("F3.phase unit modulus",S.expand_complex(rotation*S.conjugate(rotation))-1)
    check("F3.rotated real transverse",xis-rt(5)*S.Matrix([S.Rational(7,150),S.Rational(13,150),-S.Rational(2,15)]))
    check("F3.rotated imaginary transverse",etas-7*rt(5)*S.Matrix([-1,1,0])/50)
    check("F3.tangent chirality",cp-S.Rational(7,300)*S.Matrix([-1,-1,2]))
    check("F3.longitudinal chirality",cl-S.Rational(7,75)*e)
    check("F3.relative distance squared", (xis.dot(xis)+etas.dot(etas))/(3*w*w)-20)
    # Exact isotropy subspaces, with chirality formulas for arbitrary amplitudes.
    x,y,z,aa,bb,cc,dd=S.symbols('x y z aa bb cc dd',real=True)
    za=S.Matrix([x+S.I*y,x-S.I*y,z])
    zb=S.Matrix([aa+S.I*bb,aa+S.I*bb,cc+S.I*dd])
    check("F6.u-type stabilizer T times conjugation",T*za.conjugate()-za)
    check("F6.v-type stabilizer T",T*zb-zb)
    ca=za.applyfunc(S.re).cross(za.applyfunc(S.im))
    cb=zb.applyfunc(S.re).cross(zb.applyfunc(S.im))
    check("F6.u chirality formula",ca-y*S.Matrix([z,z,-2*x]))
    check("F6.v chirality formula",cb-(aa*dd-cc*bb)*S.Matrix([1,-1,0]))
    check("F7.orthogonality for whole invariant subspaces",ca.dot(cb))
    # Source cubic equivariance and synchronized invariance, without evolution.
    def polynomial_source(z):
        return z+ep*z.multiply_elementwise(e-z.multiply_elementwise(z.conjugate()))+g*L*z
    generic=xx+S.I*yy
    check("F1.synchronized manifold",polynomial_source((x+S.I*y)*e)-(1+ep*(1-x*x-y*y))*(x+S.I*y)*e)
    for label,mat in [('P',P),('T',T)]:
        check("F4.amplitude equivariance "+label,polynomial_source(mat*generic)-mat*polynomial_source(generic))
    check("F4.amplitude conjugation",polynomial_source(generic.conjugate())-polynomial_source(generic).conjugate())
    return {'D3_oriented_root_orbits_k_pi_over_6':d3,'D6_oriented_root_orbits':d6,
        'D3_projective_orbits_k_mod_6':projective,'historical_seed':[str(x) for x in seed],
        'historical_rotation':str(rotation),'tangent_C':[str(x) for x in cp],
        'longitudinal_C':[str(x) for x in cl],'relative_sync_distance':'2*sqrt(5)',
        'classification':'specified exact case study; not universal selector or global asymptotic theorem'}

def one_step():
    q2=q.applyfunc(lambda z:z*z);q3=q.applyfunc(lambda z:z**3)
    re=e-ep*h*h*q2;im=a*h*q-ep*h**3*q3
    cv=re.cross(im)
    sin3=3*s-4*s**3;cos3=c*(1-4*s*s);sin6=2*sin3*cos3
    symmetric_cubic=sum(z**3 for z in q)
    alternating_cubic=(q[0]-q[1])*(q[1]-q[2])*(q[2]-q[0])
    check('F5.symmetric cubic sin3',symmetric_cubic-sin3/rt(6),True)
    check('F5.alternating cubic cos3',alternating_cubic-cos3/rt(2),True)
    check('F5.degree-six invariant product',4*rt(3)*symmetric_cubic*alternating_cubic-sin6,True)
    cos6=1-2*sin3*sin3
    expectedA=rt(3)*h*(a-ep*h*h*(2*a+3)/6+ep**2*h**4*(5+cos6)/36)
    expectedB=rt(3)*ep**2*h**5*sin6/36
    expectedD=rt(6)*ep*h**3*(2*a-ep*h*h)*cos3/12
    check("F5.exact one-step A",cv.dot(qp)-expectedA,True)
    check("F5.exact one-step B",cv.dot(q)-expectedB,True)
    check("F5.exact one-step D",cv.dot(e/rt(3))-expectedD,True)
    return {'A':str(expectedA),'B':str(expectedB),'D':str(expectedD),
        'psi_convention':'atan2(C dot (-q), C dot q_perp); positive u-to-v',
        'leading_angle':str(-ep**2/(36*a))}

def derive_jets():
    print('STAGE universal component jets',file=sys.stderr,flush=True)
    A,M,X,B,D,U0,Us,Ec,P,Q,Rc=S.symbols('A M X B D U0 Us E P Q R')
    s2=rt(6)*(t*t-S.Rational(1,3))
    y=A*t;x=M+X*s2;vv=B*t+D*sigma
    uu=U0+Us*s2+Ec*sigma*t;ww=P*t+Q*sigma+Rc*sigma*s2
    # Truncated convolution avoids generating terms of degree 6--15 that the
    # proof never uses. This does not alter a retained Taylor coefficient.
    def multiply(left,right):
        result={}
        for j,z in left.items():
            for k,w in right.items():
                if j+k<=5: result[j+k]=result.get(j+k,0)+z*w
        return {j:red(z) for j,z in result.items()}
    real={0:S.Integer(1),2:x,4:uu};imag={1:y,3:vv,5:ww}
    real2=multiply(real,real);imag2=multiply(imag,imag)
    force={j:red((1 if j==0 else 0)-real2.get(j,0)-imag2.get(j,0)) for j in range(6)}
    nre=multiply(real,force);nim=multiply(imag,force)
    amp_re={j:red(real.get(j,0)+ep*nre.get(j,0)) for j in range(6)}
    amp_im={j:red(imag.get(j,0)+ep*nim.get(j,0)) for j in range(6)}
    # Coupling is linear: use trace over the three formal channel roots.
    rx=red(amp_re[2]+(1-a)*(trace(x)-3*x)/3)
    rv=red(amp_im[3]+(1-a)*(trace(vv)-3*vv)/3)
    ru=red(amp_re[4]+(1-a)*(trace(uu)-3*uu)/3)
    rw=red(amp_im[5]+(1-a)*(trace(ww)-3*ww)/3)
    aa=a*A
    xx=simp(rx.coeff(t,2)/rt(6))
    dd=simp(trace(rv)/(3*sigma))
    ee=simp(ru.coeff(t,1)/sigma)
    rr=simp(rw.coeff(t,2)/(rt(6)*sigma))
    FF,KK=S.symbols('F K')
    replace={Ec:FF-A*D,Rc:KK+X*D}
    fbar=simp((ee+aa*dd).subs(replace))
    kbar=simp((rr-xx*dd).subs(replace))
    increment=simp(kbar/(2*aa)-KK/(2*A))
    check("F8.derived X recurrence",xx-((a-2*ep)*X-ep*A*A/rt(6)))
    check("F8.derived common imaginary mode",dd-(D-ep*(2*A*X/3+A**3/(3*rt(6)))))
    check("F8.derived F recurrence",fbar-((a-2*ep)*FF-ep*(rt(6)*X*X+(1+2*a)*A*A*X/3+a*A**4/(3*rt(6)))))
    truth("F8.common/isotropic pieces cancel from increment",not increment.has(M,B,D,U0,Us,P,Q,KK))
    check("F8.no h3 in-plane drift",angle_part(vv)+M*angle_part(y)-trace(y)/3*angle_part(x))
    # Universal component identity matches actual q components on the unit circle.
    actual_sigma=3*s-4*s**3
    for j in range(3):
        check("F8.universal cubic root "+str(j),polynomial.subs({t:q[j],sigma:actual_sigma}),True)
    p1=y;p3=red(vv-x*y-y**3/3)
    p5=red(ww-x*vv+(x*x-uu)*y-y*y*vv+x*y**3+y**5/5)
    def difference_sum(power):
        return red(sum(S.binomial(power,k)*(-p1)**(power-k)*trace(p1**k) for k in range(power+1)))
    H1=red(3*(trace(p1)-3*p1))
    H3=red(3*(trace(p3)-3*p3)-S.Rational(9,2)*difference_sum(3))
    mixed=red(trace(p1*p1*p3)-p3*trace(p1*p1)-2*p1*trace(p1*p3)
        +2*p1*p3*trace(p1)+p1*p1*trace(p3)-3*p1*p1*p3)
    H5=red(3*(trace(p5)-3*p5)-S.Rational(27,2)*mixed+S.Rational(81,40)*difference_sum(5))
    dx=red(-y*H1);dv=red(H3+x*H1);du=red(-y*H3-vv*H1);dw=red(H5+x*H3+uu*H1)
    dA=simp(H1.coeff(t,1));dX=simp(dx.coeff(t,2)/rt(6))
    dD=simp(trace(dv)/(3*sigma));dE=simp(du.coeff(t,1)/sigma)
    dR=simp(dw.coeff(t,2)/(rt(6)*sigma))
    dF=simp(dE+dA*D+A*dD)
    dK=simp(dR-dX*D-X*dD).subs(Rc,KK+X*D)
    phase_inc=simp(dK/(2*A)-KK*dA/(2*A*A))
    check("F14.phase tangent coefficient",dA+9*A)
    check("F14.phase real quadratic coefficient",dX-9*A*A/rt(6))
    check("F14.phase F correction",dF+3*A*A*X)
    check("F14.phase angular correction",phase_inc-(S.Rational(47,32)*A**4-3*A*A*X/(2*rt(6))))
    # For phases initialized at h*q, the quintic phase increment is different.
    isolated=simp(angle_part(S.Rational(81,40)*difference_sum(5))/(2*sigma))
    check("F13.isolated phase-angle 243/160",isolated-S.Rational(243,160)*A**5)
    # Derive coefficient matrices from the polynomial maps, do not hard-code them.
    def row(expr):
        poly=S.Poly(simp(expr),A,X,FF)
        basis=[(4,0,0),(2,1,0),(0,2,0),(0,0,1)]
        truth('F8.closed monomial span '+str(len(checks)),all(k in basis for k,_ in poly.terms()))
        return [poly.coeff_monomial(k) for k in basis]
    T0=S.Matrix([row(aa**4),row(aa*aa*xx),row(xx*xx),row(fbar)])
    ell=S.Matrix([row(increment)])
    PS=S.Matrix([row(4*A**3*dA),row(2*A*dA*X+A*A*dX),row(2*X*dX),row(dF)])
    ellS=S.Matrix([row(phase_inc)])
    # Change independent parameters to a,r only after source derivation.
    subep={ep:(a-r)/2}
    T0=T0.subs(subep);ell=ell.subs(subep)
    print('STAGE coefficient resolvent',file=sys.stderr,flush=True)
    check('F8.lift is lower triangular',S.Matrix([T0[i,j] for i in range(4) for j in range(i+1,4)]))
    rhs=S.Matrix([1,0,0,0])
    # The lift is lower triangular. Exact forward substitution cancels each
    # intermediate rational function before forming the next one, avoiding
    # the unnecessary expression swell of a fully expanded generic inverse.
    def resolvent_solve(rhs_vector):
        answer=[]
        for i in range(4):
            numerator=rhs_vector[i]+sum(T0[i,j]*answer[j] for j in range(i))
            answer.append(simp(numerator/(1-T0[i,i])))
        return S.Matrix(answer)
    resolvent_state=resolvent_solve(rhs)
    correction_state=resolvent_solve((PS*T0*resolvent_state).applyfunc(simp))
    check('F9.exact forward solve residual',(S.eye(4)-T0)*resolvent_state-rhs)
    check('F14.exact derivative solve residual',(S.eye(4)-T0)*correction_state-PS*T0*resolvent_state)
    kin=simp((ell*resolvent_state)[0])
    kd=simp((ellS*T0*resolvent_state+ell*correction_state)[0])
    truth('boundary.headline expressions depend only on a,r',kin.free_symbols.union(kd.free_symbols)<={a,r})
    defaults={a:S.Rational(2,5),r:S.Rational(3,10)}
    default_k=simp(kin.subs(defaults));default_d=simp(kd.subs(defaults))
    check("F9.exact limiting rational",default_k-S.Rational(13375,1107936648))
    check("F14.exact limiting lambda derivative",default_d-S.Rational(34494041501,849664304944))
    # Independent scalar geometric sum of the arbitrary-n recurrence.
    delta=a*a-r;eps=(a-r)/2
    ts=(1/(1-a**4)-2/(1-a*a*r)+1/(1-r*r))/delta**2
    ats=(1/(1-a**4)-1/(1-a*a*r))/delta
    fs=(eps**2*ts-eps*(1+2*a)*ats/3+a/(3*(1-a**4)))/(1-r)
    ksum=simp(eps**2/(36*a)*(6*fs+eps*(2*r-1)*ts-(r-2*eps)*ats-1/(1-a**4)))
    check("F9.scalar sum equals independently derived lift",kin-ksum)
    rn,an,rho,power_rho=S.symbols('r_to_n a_to_2n rho rho_to_n')
    check("F8.arbitrary-index t identity",(a*a*an-r*rn)/delta-r*(an-rn)/delta-an)
    check("F8.arbitrary-index convolution",(rho*power_rho-r*rn)/(rho-r)-r*(power_rho-rn)/(rho-r)-power_rho)
    b1=eps**2/delta**2-eps*(1+2*a)/(3*delta)+a/3
    b2=-2*eps**2/delta**2+eps*(1+2*a)/(3*delta)
    b3=eps**2/delta**2
    tt=(an-rn)/delta
    check("F8.three-rate forcing",eps**2*tt**2-eps*(1+2*a)*an*tt/3+a*an**2/3-(b1*an**2+b2*an*rn+b3*rn**2))
    seed_values={A:1,X:0,FF:0}
    one=simp(increment.subs(seed_values))
    one_phase=simp(phase_inc.subs({A:a,X:-ep/rt(6)}))
    check("F5.one-step amplitude angle from independent lift",one+ep**2/(36*a))
    check("F14.one-step default coefficient",one_phase.subs({a:S.Rational(2,5),ep:S.Rational(1,20)})-S.Rational(99,2500))
    elevation=-(-ep/rt(6)+lam*dX.subs(A,a))/rt(3)
    check('F14.one-step signed elevation',elevation-(ep-9*lam*a*a)/(3*rt(2)))
    return {'method':'independent universal three-root component algebra; no old verifier imported',
        'amplitude_X':str(xx),'amplitude_F':str(fbar),'angular_increment':str(increment),
        'phase_delta_X':str(dX),'phase_delta_F':str(dF),'phase_angular_increment':str(phase_inc),
        'T0':[[str(z) for z in row] for row in T0.tolist()],
        'Psync':[[str(z) for z in row] for row in PS.tolist()],
        'ell':[str(z) for z in ell],'ell_sync':[str(z) for z in ellS],
        'kappa_infinity_parameter_general':str(kin),'lambda_derivative_parameter_general':str(kd),
        'default_kappa':str(default_k),'default_kappa_80_digits':str(S.N(default_k,80)),
        'default_lambda_derivative':str(default_d),'default_lambda_derivative_80_digits':str(S.N(default_d,80)),
        'one_step_phase_coefficient':str(one_phase),'four_rates':['a**4','a**2*r','r**2','r'],
        'limiting_scope':'formal coefficient sum for |a|,|r|<1,a!=0; actual local angle requires analytic hypotheses'}

def spectrum():
    # Differentiate the real on-site cubic before substituting synchronized state.
    x,y=S.symbols('real imag',real=True)
    local=S.Matrix([x+ep*x*(1-x*x-y*y),y+ep*y*(1-x*x-y*y)])
    jac=local.jacobian([x,y]).subs({x:1,y:0})
    check('F10.on-site Jacobian',jac-S.diag(1-2*ep,1))
    JR=(1-2*ep)*S.eye(3)+g*L
    JI=(S.eye(3)+3*lam*L)*(S.eye(3)+g*L)
    real_chart=S.Matrix.hstack(e,u,v)
    real_extract=S.Matrix.vstack(e.T/3,u.T,v.T)
    J5=S.diag(real_extract*JR*real_chart,E.T*JI*E)
    expected=S.diag(1-2*ep,1-2*ep-3*g,1-2*ep-3*g,(1-3*g)*(1-9*lam),(1-3*g)*(1-9*lam))
    check('F10.five-coordinate gauge Jacobian',J5-expected)
    fixed={ep:S.Rational(1,20),g:S.Rational(1,5),lam:0}
    numbers=[simp(J5[j,j].subs(fixed)) for j in range(5)]
    truth('F10.specialized multipliers',numbers==[S.Rational(9,10),S.Rational(3,10),S.Rational(3,10),S.Rational(2,5),S.Rational(2,5)])
    valuations=[]
    for idx,z in enumerate(numbers):
        num,den=S.fraction(z)
        val=S.factorint(num).get(5,0)-S.factorint(den).get(5,0)
        valuations.append(val);check('F11.valuation index '+str(idx),val+1)
    degree=S.symbols('degree',integer=True,positive=True)
    return {'jacobian':[[str(x) for x in row] for row in J5.tolist()],
        'multipliers':[str(x) for x in numbers],'v5':valuations,
        'all_degree_proof':'additivity gives -sum(alpha)=-d; target -1; equality implies d=1, excluded; zero exponents and multiplicities do not change sum',
        'external_theorem':'Abate, Proposition 5.10 and Theorem 5.15, printed pp.35-36',
        'gauge_dimension':5,'removed_phase_eigenvalue':1}

def saved_evidence():
    path=OLD/'TRANSVERSE_AXIS_FALSIFICATION.csv'
    rows=list(csv.DictReader(path.open(encoding='utf-8',newline='')))
    truth('F7.saved row count',len(rows)==18)
    by={name:[r for r in rows if r['seed']==name] for name in ['A','B']}
    for name, rr in by.items():
        truth('F7.saved indices '+name,[int(x['row']) for x in rr]==list(range(9)))
    residuals=[]
    for row in rows:
        real=[float(row[f'Omega{j}_real']) for j in range(3)]
        imag=[float(row[f'Omega{j}_imag']) for j in range(3)]
        calc=[real[1]*imag[2]-real[2]*imag[1],real[2]*imag[0]-real[0]*imag[2],real[0]*imag[1]-real[1]*imag[0]]
        residuals.append(max(abs(calc[j]-float(row['C_'+xyz])) for j,xyz in enumerate('xyz')))
    truth('F7.readout residual on saved states',max(residuals)<1e-18, max(residuals))
    truth('F7.all recorded directions valid',all(r['direction_valid']=='True' for r in rows))
    maxA=max(float(x['projective_angle_own_initial_rad']) for x in by['A'])
    maxB=max(float(x['projective_angle_own_initial_rad']) for x in by['B'])
    mutual=max(abs(float(x['mutual_projective_angle_rad'])-math.pi/2) for x in rows)
    truth('F7.saved mutual orthogonality',mutual==0,mutual)
    return {'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'classification':'preserved binary64 evidence, not a new model run','rows':rows,
        'row_count':18,'updates_per_seed_recorded':8,'new_updates':0,
        'max_A_drift_rad':maxA,'max_B_drift_rad':maxB,
        'min_C_norm':min(float(x['C_norm']) for x in rows),
        'max_readout_residual':max(residuals),'mutual_angle_max_error_rad':mutual}

def source_bodies():
    result={}
    for name in ['dynamics.py','readouts.py']:
        p=ROOT/'kernel_physics'/name
        raw=p.read_bytes();txt=raw.decode('utf-8-sig')
        tree=ast.parse(txt);bodies={}
        for node in ast.walk(tree):
            if isinstance(node,ast.FunctionDef) and node.name in ['phase_sync','_advance','step3','z_chiral']:
                bodies[node.name]={'line':node.lineno,'body':ast.get_source_segment(txt,node)}
        result[name]={'sha256':hashlib.sha256(raw).hexdigest(),'path':str(p),'functions':bodies}
    return result

def revision_v02_checks(formal):
    """Exact revision checks; all-degree completeness is a separate analytic proof."""
    m0, r0, a0 = S.Rational(9,10), S.Rational(3,10), S.Rational(2,5)
    parameter = S.symbols('lambda_revision', real=True)
    b = a0*(1-9*parameter)
    lower = S.solve(m0**3*b-r0, parameter)[0]
    upper = S.solve(b-m0**9, parameter)[0]
    check('v02.resonance negative exact value',lower+S.Rational(7,2187))
    check('v02.resonance positive exact value',upper-S.Rational(12579511,3600000000))
    check('v02.degree-four endpoint equation',m0**3*b.subs(parameter,lower)-r0)
    check('v02.degree-nine endpoint equation',b.subs(parameter,upper)-m0**9)
    lo, hi = m0**9, r0/m0**3
    truth('v02.endpoint ordering',lower<0<upper and -lower<upper)
    truth('v02.spectrum ordering on interval',0<r0<lo<a0<hi<m0<1)
    truth('v02.two b factors below r',hi**2<r0)
    truth('v02.adjacent pure m powers',m0**9==lo and m0**8>hi)
    truth('v02.adjacent r over m powers',r0/m0**2<lo and r0/m0**3==hi)
    truth('v02.fixed m powers cannot reach r',
          all(S.factorint(z.p).get(5,0)-S.factorint(z.q).get(5,0)==-1 for z in [m0,r0]),
          'v5(m^i)=-i versus v5(r)=-1 excludes i>=2; i=1 has m!=r')
    historic = S.Rational(1,1000)
    bh = simp(b.subs(parameter,historic))
    check('v02.historical b exact',bh-S.Rational(991,2500))
    truth('v02.historical lambda inside symmetric interval',abs(historic)<-lower)
    vh = S.factorint(bh.p).get(5,0)-S.factorint(bh.q).get(5,0)
    check('v02.historical b valuation',vh+4)
    # For target b, i+j+4k=4. Nonlinear candidates have k=0, i+j=4.
    five = []
    for i in range(5):
        value=m0**i*r0**(4-i)
        truth('v02.historical valuation residual case '+str(i),value!=bh,
              {'i':i,'j':4-i,'k':0,'monomial':str(value),'target':str(bh)})
        five.append(str(value))
    # Explicitly finite corroboration, never the source of all-degree completeness.
    finite={}
    for name,par in [('negative_endpoint',lower),('positive_endpoint',upper),('historical',historic)]:
        bz=simp(b.subs(parameter,par));hits=[]
        for i in range(13):
            for j in range(13-i):
                for k in range(13-i-j):
                    degree=i+j+k
                    if degree<2:continue
                    value=m0**i*r0**j*bz**k
                    for target,tval in [('m',m0),('r',r0),('b',bz)]:
                        if value==tval:hits.append({'target':target,'i':i,'j':j,'k':k,'degree':degree})
        finite[name]={'degree_cap':12,'hits':hits}
    truth('v02.finite corroboration degree four',{'target':'r','i':3,'j':0,'k':1,'degree':4} in finite['negative_endpoint']['hits'])
    truth('v02.finite corroboration degree nine',{'target':'b','i':9,'j':0,'k':0,'degree':9} in finite['positive_endpoint']['hits'])
    truth('v02.finite historical corroboration',not finite['historical']['hits'])
    # An explicit uniform-contraction proof replaces the unsupported majorant phrase.
    contraction=S.Rational(19,20); minimum=S.Rational(1,4); order=28
    truth('v02.uniform high-order contraction bound',contraction**order<minimum,
          {'q':str(contraction),'eta':str(minimum),'order':order,
           'ratio':str(contraction**order/minimum)})
    kin=S.sympify(formal['kappa_infinity_parameter_general'],locals={'a':a,'r':r})
    N=4*a**3*r**2+3*a**3*r-4*a**3+a**2*r**2-4*a**2+4*a*r**2-a-2*r**2-3*r+2
    closed=-(a-r)**2*N/(288*a*(1+a)*(1+a*a)*(1-r)**2*(1+r)*(1-a*a*r))
    check('v02.signed-domain closed expression unchanged',kin-closed)
    collision=simp(kin.subs(r,a*a))
    check('v02.collision continuous value',S.limit(kin,r,a*a)-collision)
    truth('v02.collision example finite',collision.subs(a,S.Rational(1,2)).is_finite is True)
    negative=simp(kin.subs({a:-S.Rational(1,2),r:-S.Rational(1,4)}))
    truth('v02.negative parameter formal example finite',negative.is_finite is True)
    # The jet coefficients are polynomial; kappa already has a genuine a=0 pole at n=1.
    jet_A,jet_X,jet_F=S.symbols('A X F')
    actual_increment=S.sympify(formal['angular_increment'],
        locals={'a':a,'epsilon':ep,'A':jet_A,'X':jet_X,'F':jet_F})
    k1=simp(actual_increment.subs({jet_A:1,jet_X:0,jet_F:0}).subs(ep,(a-r)/2))
    check('v02.kappa1 denominator qualification',k1+(a-r)**2/(144*a))
    truth('v02.kappa not claimed polynomial at a zero',S.denom(S.factor(k1)).has(a))
    return {
      'all_degree_proof_class':'ANALYTIC_PROOF: manuscript section 12.2; finite enumeration is corroboration only',
      'aggregate_resonance_equation':'target in {m,r,b} equals m^i*r^j*b^k, i+j+k>=2',
      'all_degree_cases':[
        'j>=1: product<=r, strict at total degree>=2; cannot reach any target.',
        'j=0, target m: any b factor is below m; pure m powers of degree>=2 are below m.',
        'j=0, target b: a b factor permits only excluded degree one; remaining family b=m^i, i>=2.',
        'j=0, target r: k>=2 excluded by hi^2<r; k=1 gives b=r/m^i, i>=1; k=0 excluded by valuations.',
        'Adjacent-power inequalities exclude all remaining family members in lo<b<hi.'],
      'b_interval':[str(lo),str(hi)],'lambda_interval':[str(lower),str(upper)],
      'symmetric_radius':str(-lower),'negative_endpoint_degree':4,'positive_endpoint_degree':9,
      'negative_endpoint_80_digits':str(S.N(lower,80)),'positive_endpoint_80_digits':str(S.N(upper,80)),
      'historical_lambda':str(historic),'historical_b':str(bh),'historical_five_candidates':five,
      'finite_enumeration':finite,'uniform_iteration_ratio':str(contraction**order/minimum),
      'collision_value_general':str(collision),'negative_formal_example':str(negative),
      'evidence_classes':['EXECUTABLE_EXACT_IDENTITY','FINITE_ENUMERATION','ANALYTIC_PROOF'],
      'new_model_runs':0}

def main():
    data={'symmetry_and_history':historical_and_symmetry(),'one_step':one_step(),
        'formal_coefficients':derive_jets(),'local_spectrum':spectrum(),
        'saved_numerical_evidence':saved_evidence(),'accepted_source_bodies':source_bodies()}
    data['revision_v02']=revision_v02_checks(data['formal_coefficients'])
    truth('boundary.no accepted kernel module imported',not any(x=='kernel_physics' or x.startswith('kernel_physics.') for x in sys.modules))
    data.update({'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),
        'runtime':{'python':sys.version,'sympy':S.__version__,'executable':sys.executable},
        'PAPER_F_DEPENDS_ON_THETA_LOCK':False,'new_model_runs':0,'old_verifier_executions':0,
        'status':'EXACT_CHECKS_COMPLETE_NOT_PUBLICATION_ACCEPTANCE'})
    print(json.dumps(data,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
