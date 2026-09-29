"""Independent Supplement F exact reconstruction; no historical verifier imports.

Universal analytic proofs reside in the companion packet, not predicate counts.
Run in conda torment with -B; --output and --scratch are required external paths.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
REPO = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mathematics(sp):
    rows, expressions, proofs = [], {}, {}
    def ck(group, name, value, evidence="EXACT_SYMBOLIC", **detail):
        rows.append(dict(group=group,name=name,passed=bool(value),
                         evidence=evidence,detail=detail))
    def zero(value):
        if isinstance(value,sp.MatrixBase):
            return all(zero(x) for x in value)
        return sp.factor(sp.expand(value)) == 0
    def save(name,value):
        expressions[name] = (value.tolist() if isinstance(value,sp.MatrixBase) else value)
    rt2,rt3,rt6 = sp.sqrt(2),sp.sqrt(3),sp.sqrt(6)
    e=sp.ones(3,1);u=sp.Matrix([1,-1,0])/rt2;v=sp.Matrix([1,1,-2])/rt6
    E=sp.Matrix.hstack(u,v);P=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    T=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
    PV=E.T*P*E;TV=E.T*T*E
    ck("F02_GROUP_ACTION","oriented_orthonormal_basis",
       zero(E.T*E-sp.eye(2)) and zero(e.T*E) and zero(u.cross(v)-e/rt3))
    ck("F02_GROUP_ACTION","permutation_matrices_relations",
       zero(PV-sp.Matrix([[-sp.Rational(1,2),-rt3/2],[rt3/2,-sp.Rational(1,2)]]))
       and TV==sp.diag(-1,1) and PV**3==sp.eye(2)
       and TV**2==sp.eye(2) and zero(TV*PV*TV-PV.inv()))
    J=-sp.eye(2)
    ck("F02_GROUP_ACTION","conjugation_commutes_and_extends",
       J*PV==PV*J and J*TV==TV*J and zero((J*PV**2)**6-sp.eye(2))
       and zero(J*PV**2-sp.Matrix([[sp.Rational(1,2),-rt3/2],[rt3/2,sp.Rational(1,2)]])))
    group3=[(PV**i)*(TV**j) for i in range(3) for j in range(2)]
    group6=group3+[J*g for g in group3]
    orbit=lambda k,extra,mod=12: sorted({(sgn*k+4*i+6*j)%mod
        for i in range(3) for sgn in [1,-1] for j in (range(2) if extra else [0])})
    # Reflection is k -> 6-k; add its offset independently for D3.
    def orb(k,extra=False,mod=12):
        return sorted({(k+4*i+6*j)%mod for i in range(3) for j in (range(2) if extra else [0])}
                      |{(6-k+4*i+6*j)%mod for i in range(3) for j in (range(2) if extra else [0])})
    orbits3=[orb(0),orb(1),orb(3)]
    ck("F02_GROUP_ACTION","oriented_and_projective_orbits",
       orbits3==[[0,2,4,6,8,10],[1,5,9],[3,7,11]]
       and [orb(0,True),orb(1,True)]==[list(range(0,12,2)),list(range(1,12,2))]
       and [orb(0,mod=6),orb(1,mod=6)]==[[0,2,4],[1,3,5]],
       "FINITE_ENUMERATION",D3=orbits3,D6=[orb(0,True),orb(1,True)])
    stabilizers={name:[i for i,g in enumerate(group) if zero(g*q-q)]
        for name,group,q in [("D3_u",group3,sp.Matrix([1,0])),
                            ("D3_v",group3,sp.Matrix([0,1])),
                            ("D6_u",group6,sp.Matrix([1,0])),
                            ("D6_v",group6,sp.Matrix([0,1]))]}
    ck("F02_ISOTROPY","stabilizer_orders", [len(stabilizers[k]) for k in stabilizers]==[1,2,2,2],
       "FINITE_ENUMERATION",stabilizers=stabilizers)
    x,y,z,aa,bb,cc,dd=sp.symbols("x y z alpha beta gamma delta",real=True)
    real_u=sp.Matrix([x,x,z]);imag_u=sp.Matrix([y,-y,0])
    real_v=sp.Matrix([aa,aa,cc]);imag_v=sp.Matrix([bb,bb,dd])
    cu=real_u.cross(imag_u);cv=real_v.cross(imag_v)
    ck("F02_ISOTROPY","full_state_fixed_spaces",
       T*real_u==real_u and -T*imag_u==imag_u
       and T*real_v==real_v and T*imag_v==imag_v
       and 3-(sp.eye(3)-T).rank()==2 and 3-(sp.eye(3)+T).rank()==1,
       real_u=str(real_u),imag_u=str(imag_u),real_v=str(real_v),imag_v=str(imag_v))
    ck("F02_ISOTROPY","chirality_formulas_and_orthogonality",
       cu==y*sp.Matrix([z,z,-2*x]) and cv==(aa*dd-cc*bb)*sp.Matrix([1,-1,0])
       and zero(cu.dot(cv)))
    a,eps,r,h=sp.symbols("a epsilon r h",real=True)
    g=(1-a)/3
    def amp(R,I):
        norm=R.multiply_elementwise(R)+I.multiply_elementwise(I)
        return (R+eps*R.multiply_elementwise(e-norm)+g*(e*sum(R)-3*R),
                I+eps*I.multiply_elementwise(e-norm)+g*(e*sum(I)-3*I))
    ru,iu=amp(real_u,imag_u);rv,iv=amp(real_v,imag_v)
    ck("F02_ISOTROPY","polynomial_update_preserves_fixed_spaces",
       zero(T*ru-ru) and zero(T*iu+iu) and zero(T*rv-rv) and zero(T*iv-iv))
    c,s=sp.symbols("c s",real=True)
    def circle(p):
        return sp.factor(sp.rem(sp.expand(p),c*c+s*s-1,c))
    q=u*c+v*s;qp=-u*s+v*c
    S=3*s-4*s**3;C=4*c**3-3*c
    q2=q.applyfunc(lambda qj:qj*qj)
    q3=q.applyfunc(lambda qj:qj**3)
    chir=(e-eps*h*h*q2).cross(a*h*q-eps*h**3*q3)
    AC=rt3*h*(a-eps*h*h*(2*a+3)/6+eps**2*h**4*(6-2*S*S)/36)
    BC=rt3*eps**2*h**5*(2*S*C)/36
    DC=rt6*eps*h**3*(2*a-eps*h*h)*C/12
    for name,actual,expected in [("A_C",chir.dot(qp),AC),("B_C",chir.dot(q),BC),
                                  ("D_C",chir.dot(e/rt3),DC)]:
        ck("F03_ONE_STEP",name,circle(actual-expected)==0)
        save(name,expected)
    ck("F03_ONE_STEP","e_cross_q",all(circle(t)==0 for t in e.cross(q)-rt3*qp))
    I3=sum(t**3 for t in q)
    discriminant=(q[0]-q[1])*(q[1]-q[2])*(q[2]-q[0])
    ck("F03_HARMONIC_SELECTION","invariants_sixfold",
       circle(I3-S/rt6)==0 and circle(discriminant-C/rt2)==0
       and circle(4*rt3*I3*discriminant-2*S*C)==0)
    xx,yy=sp.symbols("xx yy")
    dimensions={}
    for degree in [2,4,6]:
        coeff=sp.symbols(f"d0:{degree+1}")
        polynomial=sum(coeff[i]*xx**i*yy**(degree-i) for i in range(degree+1))
        perm=polynomial.subs({xx:-xx-yy,yy:xx},simultaneous=True)-polynomial
        trans=polynomial.subs({xx:yy,yy:xx},simultaneous=True)+polynomial
        equations=sp.Poly(perm,xx,yy).coeffs()+sp.Poly(trans,xx,yy).coeffs()
        mat,_=sp.linear_eq_to_matrix(equations,coeff)
        dimensions[degree]=len(coeff)-mat.rank()
    ck("F03_HARMONIC_SELECTION","homogeneous_degree_exclusion",
       dimensions=={2:0,4:0,6:1},dimensions=dimensions)
    leading=-eps**2/(36*a)
    ck("F03_ONE_STEP","signed_angle_H5",
       leading.subs({eps:sp.Rational(1,20),a:sp.Rational(2,5)})==-sp.Rational(1,5760))

    # Universal three-root algebra, derived from elementary symmetric sums.
    t,S0=sp.symbols("t S")
    root=t**3-t/2-S0/(3*rt6)
    def red(p,var=t):
        rel=var**3-var/2-S0/(3*rt6)
        return sp.expand(sp.rem(sp.expand(p),rel,var))
    def trace(p,var=t):
        p=red(p,var)
        return sp.expand(3*p.coeff(var,0)+p.coeff(var,2))
    s2=rt6*(t*t-sp.Rational(1,3))
    def components(p):
        p=red(p)
        return tuple(sp.factor(x) for x in (p.coeff(t,0)+p.coeff(t,2)/3,
                                            p.coeff(t,1),p.coeff(t,2)/rt6))
    ck("F03_FINITE_JETS","root_trace_and_product_identities",
       trace(t)==0 and trace(t*t)==1 and zero(trace(t**3)-S0/rt6)
       and zero(red(t*s2)-t/rt6-S0/3)
       and zero(red(s2*s2)-sp.Rational(1,3)+s2/rt6-sp.sqrt(sp.Rational(2,3))*S0*t)
       and zero(red(t**5)-t/4-5*S0/(18*rt6)-S0*s2/18))
    A,M,X,B,D,U0,Us,E0,Pj,Qj,Rj=sp.symbols("A M X B D U0 Us E Pjet Qjet R")
    yy0=A*t;xx0=M+X*s2;vv=B*t+D*S0
    uu=U0+Us*s2+E0*S0*t;ww=Pj*t+Qj*S0+Rj*S0*s2
    real=1+h*h*xx0+h**4*uu
    imag=h*yy0+h**3*vv+h**5*ww
    newreal=sp.expand(real+eps*real*(1-real**2-imag**2)+g*(trace(real)-3*real))
    newimag=sp.expand(imag+eps*imag*(1-real**2-imag**2)+g*(trace(imag)-3*imag))
    derived_vectors={name:red(poly.coeff(h,degree)) for name,poly,degree in [
        ("y",newimag,1),("x",newreal,2),("v",newimag,3),("u",newreal,4),("w",newimag,5)]}
    LI=lambda zz:red(a*zz+(1-a)*trace(zz)/3)
    LR=lambda zz:red((a-2*eps)*zz+(1-a)*trace(zz)/3)
    vector_expected=dict(y=LI(yy0),x=LR(xx0)-eps*yy0**2,
        v=LI(vv)-eps*(2*xx0*yy0+yy0**3),
        u=LR(uu)-eps*(3*xx0**2+2*yy0*vv+xx0*yy0**2),
        w=LI(ww)-eps*(2*xx0*vv+2*uu*yy0+xx0**2*yy0+3*yy0**2*vv))
    for name in derived_vectors:
        ck("F03_FINITE_JETS","complete_channel_"+name,
           zero(red(derived_vectors[name]-vector_expected[name])))
    dc={name:components(polynomial) for name,polynomial in derived_vectors.items()}
    amps=dict(A=dc["y"][1],M=dc["x"][0],X=dc["x"][2],
              B=dc["v"][1],D=sp.cancel(dc["v"][0]/S0),
              U0=dc["u"][0],Us=dc["u"][2],E=sp.cancel(dc["u"][1]/S0),
              Pjet=dc["w"][1],Qjet=sp.cancel(dc["w"][0]/S0),R=sp.cancel(dc["w"][2]/S0))
    for name,val in amps.items():
        save("jet_"+name,sp.factor(val))
        ck("F03_FINITE_JETS","scalar_closure_"+name,not val.has(t,S0,h))
    F,K=sp.symbols("F K")
    ampF=sp.factor((amps["E"]+amps["A"]*amps["D"]).subs(E0,F-A*D))
    ampK=sp.factor((amps["R"]-amps["X"]*amps["D"]).subs({E0:F-A*D,Rj:K+X*D}))
    inc=sp.factor(ampK/(2*amps["A"])-K/(2*A))
    ampFexpected=(a-2*eps)*F-eps*(rt6*X**2+(1+2*a)*A*A*X/3+a*A**4/(3*rt6))
    incexpected=-eps*F/(a*rt6)+eps*(2*(a-2*eps)-1)*X**2/(6*a)+eps*(a-4*eps)*A*A*X/(6*a*rt6)-eps**2*A**4/(36*a)
    ck("F03_FINITE_JETS","F_K_cancellation_and_increment",
       zero(ampF-ampFexpected) and zero(inc-incexpected))
    save("F_prime",ampF);save("K_prime",ampK);save("kappa_increment",inc)

    # Derive phase expansion from atan(I/R) and simultaneous sine differences.
    p1=yy0
    p3=red(vv-xx0*yy0-yy0**3/3)
    p5=red(ww-xx0*vv+(xx0**2-uu)*yy0-yy0**2*vv+xx0*yy0**3+yy0**5/5)
    ellroot=sp.Symbol("ellroot")
    diff1=p1.subs(t,ellroot)-p1
    diff3=p3.subs(t,ellroot)-p3
    H1=red(3*(trace(p1)-3*p1))
    H3=red(3*(trace(p3)-3*p3)-sp.Rational(9,2)*trace(diff1**3,ellroot))
    H5=red(3*(trace(p5)-3*p5)-sp.Rational(27,2)*trace(diff1**2*diff3,ellroot)
           +sp.Rational(81,40)*trace(diff1**5,ellroot))
    changes=dict(y=H1,x=red(-yy0*H1),v=red(H3+xx0*H1),
                 u=red(-yy0*H3-vv*H1),w=red(H5+xx0*H3+uu*H1))
    ph={name:components(val) for name,val in changes.items()}
    dA=ph["y"][1];dX=ph["x"][2];dD=sp.cancel(ph["v"][0]/S0)
    dE=sp.cancel(ph["u"][1]/S0);dR=sp.cancel(ph["w"][2]/S0)
    dF=sp.factor(dE+dA*D+A*dD)
    dK=sp.factor((dR-dX*D-X*dD).subs(Rj,K+X*D))
    dk=sp.factor(dK/(2*A)-K*dA/(2*A*A))
    phase_expectations={"A":(dA,-9*A),"X":(dX,9*A*A/rt6),"D":(dD,-3*A*X),
        "E":(dE,9*A*D),"F":(dF,-3*A*A*X),
        "K":(dK,-9*K-3*X*A**3/rt6+sp.Rational(47,16)*A**5),
        "kappa":(dk,-3*X*A*A/(2*rt6)+sp.Rational(47,32)*A**4)}
    for name,(got,expected) in phase_expectations.items():
        ck("F06_ONE_STEP_LAMBDA","derived_phase_"+name,zero(got-expected))
        save("phase_delta_"+name,got)
    one_lambda=sp.factor(dk.subs({A:a,X:-eps/rt6}))
    ck("F06_ONE_STEP_LAMBDA","full_composed_derivative",
       zero(one_lambda-eps*a*a/4-sp.Rational(47,32)*a**4)
       and one_lambda.subs({a:sp.Rational(2,5),eps:sp.Rational(1,20)})==sp.Rational(99,2500))
    save("one_step_lambda",one_lambda)
    iso5=red(sp.Rational(81,40)*trace((ellroot-t)**5,ellroot))
    # s2 projection onto q_perp is cos(3phi); S*cos(3phi)=sin(6phi)/2.
    isolated=sp.factor(components(iso5)[2]/(2*S0))
    ck("FALSIFIERS","isolated_phase_is_different",isolated==sp.Rational(243,160)
       and isolated!=sp.Rational(99,2500),"NEGATIVE_FALSIFIER")
    save("isolated_phase_coefficient",isolated)

    # Coefficient lift is extracted, not entered as an expected matrix.
    monomials=[A**4,A*A*X,X*X,F]
    extract=lambda p:sp.Matrix([[sp.expand(p).coeff(F,1) if j==3 else
        sp.Poly(sp.expand(p),A,X,F).coeff_monomial(mon)
        for j,mon in enumerate(monomials)]])
    lift_values=[amps["A"]**4,amps["A"]**2*amps["X"],amps["X"]**2,ampF]
    T0=sp.Matrix.vstack(*(extract(p) for p in lift_values))
    ell=extract(inc)
    ps_values=[4*A**3*dA,2*A*dA*X+A*A*dX,2*X*dX,dF]
    Ps=sp.Matrix.vstack(*(extract(p) for p in ps_values))
    ells=extract(dk)
    ck("F06_RESOLVENT_DERIVATIVE","lift_reconstruction",
       zero(T0*sp.Matrix(monomials)-sp.Matrix(lift_values))
       and zero((ell*sp.Matrix(monomials))[0]-inc)
       and zero(Ps*sp.Matrix(monomials)-sp.Matrix(ps_values))
       and zero((ells*sp.Matrix(monomials))[0]-dk))
    for name,val in [("T0",T0),("ell",ell),("Ps",Ps),("ell_s",ells)]:
        save(name,val)
    z0=sp.Matrix([1,0,0,0])
    Ta=T0.subs(eps,(a-r)/2)
    ella=ell.subs(eps,(a-r)/2)
    # Lower triangular exact elimination derives both parameter expressions.
    zsum=(sp.eye(4)-Ta).inv()*z0
    ksum=sp.factor((ella*zsum)[0])
    derivative=sp.factor((ells*Ta*zsum+ella*(sp.eye(4)-Ta).inv()*Ps*Ta*zsum)[0])
    save("kappa_infinity_parameter",ksum)
    save("limiting_lambda_derivative_parameter",derivative)
    values={a:sp.Rational(2,5),r:sp.Rational(3,10)}
    ck("F04_INFINITE_SUM","exact_H5_sum",ksum.subs(values)==sp.Rational(13375,1107936648))
    ck("F06_RESOLVENT_DERIVATIVE","exact_H5_limiting_derivative",
       derivative.subs(values)==sp.Rational(34494041501,849664304944))
    save("kappa_infinity_H5",ksum.subs(values))
    save("limiting_lambda_derivative_H5",derivative.subs(values))
    # Full cross-product projection verifies K/(2A), retaining every common mode.
    s2vec=rt6*(q2-e/3)
    yvec=A*q;xvec=M*e+X*s2vec;vvec=B*q+D*S*e
    uvec=U0*e+Us*s2vec+E0*S*q;wvec=Pj*q+Qj*S*e+Rj*S*s2vec
    num3=-(e.cross(vvec)+xvec.cross(yvec)).dot(q)
    num5=-(e.cross(wvec)+xvec.cross(vvec)+uvec.cross(yvec)).dot(q)
    ck("F03_FINITE_JETS","angular_projection_complete_jets",
       circle(num3)==0 and circle(num5-rt3*(Rj-X*D)*S*C)==0)
    # Arbitrary-index geometric convolution identity: represent x^n and y^n
    # by independent symbols, avoiding any finite-n inference.
    p_rate,q_rate,pn,qn=sp.symbols("p_rate q_rate p_to_n q_to_n")
    conv=(pn-qn)/(p_rate-q_rate)
    nextconv=(p_rate*pn-q_rate*qn)/(p_rate-q_rate)
    ck("F03_FINITE_JETS","arbitrary_index_convolution",
       zero(nextconv-q_rate*conv-pn),
       proof="p^n,q^n independent: C_(n+1)=q C_n+p^n; C_0=0")
    n=sp.symbols("n",integer=True,positive=True)
    ck("F03_RATE_COLLISIONS","divided_difference_limit",
       sp.limit((p_rate**n-q_rate**n)/(p_rate-q_rate),p_rate,q_rate)==n*q_rate**(n-1))
    # Independently sum scalar t/f forcing, then compare with derived resolvent.
    epsar=(a-r)/2;d=a*a-r
    T4=1/(1-a**4)
    T2=(T4-2/(1-a*a*r)+1/(1-r*r))/d**2
    TA=(T4-1/(1-a*a*r))/d
    fsum=(epsar**2*T2-epsar*(1+2*a)*TA/3+a*T4/3)/(1-r)
    scalar_sum=sp.factor(epsar**2/(36*a)*(6*fsum+epsar*(2*r-1)*T2-(r-2*epsar)*TA-T4))
    ck("F04_INFINITE_SUM","scalar_geometric_sum_equals_resolvent",zero(scalar_sum-ksum))
    N=4*a**3*r*r+3*a**3*r-4*a**3+a*a*r*r-4*a*a+4*a*r*r-a-2*r*r-3*r+2
    printed=-(a-r)**2*N/(288*a*(1+a)*(1+a*a)*(1-r)**2*(1+r)*(1-a*a*r))
    ck("F04_INFINITE_SUM","parameter_rational_cancellation",zero(scalar_sum-printed))
    ck("F04_INFINITE_SUM","coefficient_lift_rates",
       zero(sp.Matrix(list(Ta.diagonal()))-sp.Matrix([a**4,a*a*r,r*r,r])))
    save("scalar_infinite_sum",scalar_sum)
    collision_pairs=[(sp.Rational(1,2),sp.Rational(1,4)),
                     (sp.Rational(1,2),sp.Rational(1,16)),
                     (sp.Rational(1,2),0),(sp.Rational(1,2),1)]
    collision_bad=[]
    for av,rv0 in collision_pairs:
        ev=(av-rv0)/2
        tk=fk=kap=sp.Integer(0);zstate=z0
        for index in range(7):
            incscalar=ev**2/(36*av)*(6*fk+ev*(2*rv0-1)*tk**2-(rv0-2*ev)*av**(2*index)*tk-av**(4*index))
            inclift=(ella.subs({a:av,r:rv0})*zstate)[0]
            if not zero(incscalar-inclift):collision_bad.append([str(av),str(rv0),index])
            kap+=incscalar
            fk,tk=(rv0*fk+ev**2*tk**2-ev*(1+2*av)*av**(2*index)*tk/3+av**(4*index+1)/3,
                   rv0*tk+av**(2*index))
            zstate=Ta.subs({a:av,r:rv0})*zstate
    ck("F03_RATE_COLLISIONS","polynomial_recurrences_at_collisions",not collision_bad,
       "FINITE_ENUMERATION",pairs=[list(map(str,p)) for p in collision_pairs],
       steps=7,failures=collision_bad)
    ck("F03_RATE_COLLISIONS","a_zero_not_polynomial_claim",
       sp.denom(sp.factor(-epsar**2/(36*a))).has(a),
       "NEGATIVE_FALSIFIER")
    # Direct exact finite iteration of Taylor coefficients, not model states.
    state={A:sp.Integer(1)}
    jet_symbols=[A,M,X,B,D,U0,Us,E0,Pj,Qj,Rj]
    keys=["A","M","X","B","D","U0","Us","E","Pjet","Qjet","R"]
    state.update({sym:sp.Integer(0) for sym in jet_symbols[1:]})
    finite=[];zs=z0;kacc=sp.Integer(0)
    aa0,rr0=values[a],values[r];ee0=(aa0-rr0)/2
    for index in range(1,9):
        state={sym:sp.factor(amps[key].subs(state).subs({a:aa0,eps:ee0}))
               for sym,key in zip(jet_symbols,keys)}
        kj=sp.factor((state[Rj]-state[X]*state[D])/(2*state[A]))
        kacc+= (ella.subs(values)*zs)[0]
        zs=Ta.subs(values)*zs
        finite.append(kj)
        ck("F03_FINITE_JETS",f"full_jet_vs_lift_n{index}",zero(kj-kacc))
    save("finite_H5_coefficients",finite)
    ck("FALSIFIERS","eight_coefficients_do_not_equal_infinity",
       finite[-1]!=ksum.subs(values),"NEGATIVE_FALSIFIER",
       exact_difference=str(sp.factor(finite[-1]-ksum.subs(values))))

    # Real derivative/gauge embedding before substituting H5.
    lam=sp.Symbol("lambda",real=True)
    L=e*e.T-3*sp.eye(3)
    scalar_x,scalar_y,delta=sp.symbols("scalar_x scalar_y delta",real=True)
    scalar_real=scalar_x+eps*scalar_x*(1-scalar_x**2-scalar_y**2)
    scalar_imag=scalar_y+eps*scalar_y*(1-scalar_x**2-scalar_y**2)
    local=sp.Matrix([scalar_real,scalar_imag]).jacobian([scalar_x,scalar_y]).subs({scalar_x:1,scalar_y:0})
    ck("F05_GAUGE_SPECTRUM","onsite_real_derivative",local==sp.diag(1-2*eps,1))
    emb=sp.zeros(6,5);emb[:3,:3]=sp.Matrix.hstack(e,u,v);emb[3:,3:]=E
    extraction=sp.zeros(5,6);extraction[0,:3]=e.T/3
    extraction[1:3,:3]=E.T;extraction[3:,3:]=E.T
    realJ=(1-2*eps)*sp.eye(3)+g*L
    imagJ=(sp.eye(3)+3*lam*L)*(sp.eye(3)+g*L)
    fullJ=sp.diag(realJ,imagJ)
    gaugeJ=sp.simplify(extraction*fullJ*emb)
    targetJ=sp.diag(1-2*eps,a-2*eps,a-2*eps,a*(1-9*lam),a*(1-9*lam))
    ck("F05_GAUGE_SPECTRUM","five_coordinate_composed_jacobian",zero(gaugeJ-targetJ))
    save("gauge_jacobian",gaugeJ)
    spectrum=[sp.Rational(9,10),sp.Rational(3,10),sp.Rational(3,10),sp.Rational(2,5),sp.Rational(2,5)]
    ck("F05_GAUGE_SPECTRUM","H5_spectrum",
       list(gaugeJ.subs({a:aa0,eps:ee0,lam:0}).diagonal())==spectrum)
    def valuation(value,p):
        numerator,denominator=map(int,sp.fraction(value));ans=0
        while numerator%p==0:numerator//=p;ans+=1
        while denominator%p==0:denominator//=p;ans-=1
        return ans
    ck("F05_NONRESONANCE","all_degree_valuation_ingredients",
       [valuation(x,5) for x in spectrum]==[-1]*5,
       valuations=[-1]*5,proof_owner="packet: total degree d gives valuation -d, target -1")
    ck("F05_LINEARIZATION_HYPOTHESES","H5_attracting_invertible_quotient",
       all(0<x<1 for x in spectrum) and sp.prod(spectrum)!=0
       and zero(extraction*emb-sp.eye(5)))
    ck("FALSIFIERS","original_map_not_holomorphic",
       local.subs(eps,ee0)[0,0]!=local.subs(eps,ee0)[1,1],
       "NEGATIVE_FALSIFIER",reason="real and imaginary derivatives at 1 differ")
    ck("FALSIFIERS","common_phase_is_removed",
       zero(imagJ*e-e) and 1 not in spectrum,"NEGATIVE_FALSIFIER")
    mm=sp.Rational(9,10);rr=sp.Rational(3,10);av=sp.Rational(2,5)
    low=mm**9;up=rr/mm**3
    lm=sp.factor((1-up/av)/9);lp=sp.factor((1-low/av)/9)
    ck("F06_RESONANCE_INTERVAL","all_degree_interval_inequalities",
       0<rr<low<av<up<mm<1 and up*up<rr and rr/mm**2<low and up<mm**8,
       proof_owner="packet: exhaustive aggregate exponent cases")
    ck("F06_RESONANCE_INTERVAL","exact_endpoints",
       lm==-sp.Rational(7,2187) and lp==sp.Rational(12579511,3600000000)
       and rr==mm**3*av*(1-9*lm) and av*(1-9*lp)==mm**9)
    historical_b=av*(1-sp.Rational(9,1000))
    candidates=[mm**i*rr**(4-i) for i in range(5)]
    ck("F06_RESONANCE_INTERVAL","historical_lambda_all_degree_reduction",
       historical_b==sp.Rational(991,2500) and valuation(historical_b,5)==-4
       and all(v!=historical_b for v in candidates) and lm<sp.Rational(1,1000)<lp,
       candidates_after_times_10000=[str(v*10000) for v in candidates],
       target_after_times_10000=str(historical_b*10000),
       proof_owner="packet: valuation leaves exactly five possibilities")
    ck("F06_UNIFORM_ANALYTICITY","majorant_bound",
       4*sp.Rational(19,20)**28<1,
       eta="1/4",q="19/20",N=27,ratio=str(4*sp.Rational(19,20)**28),
       boundary="only an ingredient of Appendix-D argument, not a proof by predicate")
    eta,rho,degree=sp.symbols("eta rho degree",positive=True)
    proofs.update({
        "F04_ANALYTIC_BRIDGE":"Written proof: invariant local chart, parity, normalized nonzero denominator, fixed complex h-disk, Weierstrass and Cauchy coefficient extraction.",
        "F05_NONRESONANCE":"Written all-degree valuation argument; numeric valuation predicates are ingredients only.",
        "F05_LINEARIZATION_HYPOTHESES":"External theorem application after real-coordinate complexification; uniqueness gives equivariance and real slice.",
        "F06_UNIFORM_ANALYTICITY":"Written finite homological elimination and uniform geometric majorant on compact parameter subintervals.",
        "F06_RESONANCE_INTERVAL":"Written exhaustive cases m^i r^j b^k; endpoint and inequality checks are ingredients."
    })
    # Logical counterexample to interchanging pointwise real limits/Taylor jets.
    nn=sp.Symbol("n",positive=True)
    badfamily=nn*h**6/(1+nn*h*h)
    ck("F04_ANALYTIC_BRIDGE","pointwise_limit_is_insufficient",
       sp.expand(sp.series(badfamily,h,0,6).removeO()).coeff(h,4)==0
       and sp.limit(badfamily,nn,sp.oo)==h**4,
       "NEGATIVE_FALSIFIER",family="n h^6/(1+n h^2)",complex_poles="±i/sqrt(n)")
    ck("FALSIFIERS","symmetry_does_not_fix_coefficient",
       dimensions[6]==1 and leading.subs(eps,0)==0 and leading.subs(eps,1)!=0,
       "NEGATIVE_FALSIFIER",reason="same symmetry, different recurrence parameters")
    ck("FALSIFIERS","oriented_D3_wrong_orbit_claims",
       len(orbits3)==3 and len(orb(3))==3,"NEGATIVE_FALSIFIER")
    ck("FALSIFIERS","finite_resonance_search_is_insufficient",
       sp.Rational(1,2)**13==sp.Rational(1,8192)
       and not any(sp.Rational(1,2)**i*sp.Rational(1,8192)**j in
                   [sp.Rational(1,2),sp.Rational(1,8192)]
                   for d0 in range(2,13) for i in range(d0+1) for j in [d0-i]),
       "NEGATIVE_FALSIFIER",spectrum=["1/2","1/8192"],first_resonance_degree=13)
    ck("FALSIFIERS","first_order_does_not_determine_second_order",
       sp.diff(lam**2,lam).subs(lam,0)==0 and sp.diff(lam**2,lam,2)==2,
       "NEGATIVE_FALSIFIER",reason="adding c lambda^2 preserves value and first derivative")
    ck("FALSIFIERS","isotropy_orthogonality_excludes_universal_local_axis",
       cu.subs({x:1,z:1,y:1}).dot(cv.subs({aa:1,bb:1,cc:0,dd:1}))==0
       and cu.subs({x:1,z:1,y:1})!=sp.zeros(3,1)
       and cv.subs({aa:1,bb:1,cc:0,dd:1})!=sp.zeros(3,1),
       "NEGATIVE_FALSIFIER",proof_owner="packet: near-identity limiting circle diffeomorphism")
    un,vn=sp.symbols("a_to_2n r_to_n")
    tn=(un-vn)/d
    force=epsar**2*tn*tn-epsar*(1+2*a)*un*tn/3+a*un*un/3
    bs=[epsar**2/d**2-epsar*(1+2*a)/(3*d)+a/3,
        -2*epsar**2/d**2+epsar*(1+2*a)/(3*d),epsar**2/d**2]
    ck("F03_FINITE_JETS","arbitrary_index_three_rate_forcing",
       zero(force-bs[0]*un**2-bs[1]*un*vn-bs[2]*vn**2))
    save("forcing_b",bs)
    ck("F06_RESOLVENT_DERIVATIVE","composed_one_step_matches_lift",
       zero((ells*T0*z0)[0]-one_lambda)
       and zero((ell*z0)[0]-leading))
    # Differentiate the inverse identity, without an assumed geometric fit.
    M0=(sp.eye(4)-Ta).applyfunc(sp.factor)
    R0=M0.inv().applyfunc(sp.factor)
    ck("F06_RESOLVENT_DERIVATIVE","differentiated_inverse_identity",
       zero((M0*R0-sp.eye(4)).applyfunc(sp.cancel)),
       identity="Rdot=R0 Ps T0 R0; M0 Rdot=(M0 R0) Ps T0 R0=Ps T0 R0",
       method="exact inverse residual plus associative differentiation of M R=I")
    print("Independent group, complete jets, phase and resolvent algebra constructed.",flush=True)
    return rows,expressions,proofs



def make_integrity(args):
    # Full regular-file path/content fingerprints are made AFTER the
    # independent and API checks. Only .git internals are excluded.
    baseline = json.loads(args.fingerprint_before.read_text(encoding="utf-8"))
    external_before = json.loads(args.external_before.read_text(encoding="utf-8"))
    git_before = json.loads(args.git_before.read_text(encoding="utf-8"))
    after, tree_summary, git_after = {}, {}, {}
    aggregate = lambda files: hashlib.sha256(json.dumps(
        files,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    for label, record in baseline.items():
        root = Path(record["root"])
        started = datetime.now(timezone.utc).isoformat()
        files = {}
        for path in sorted(root.rglob("*")):
            rel = path.relative_to(root)
            if path.is_file() and ".git" not in rel.parts:
                h = hashlib.sha256()
                with path.open("rb") as handle:
                    for chunk in iter(lambda: handle.read(1048576), b""):
                        h.update(chunk)
                files[rel.as_posix()] = h.hexdigest()
        after[label] = dict(root=str(root),start_utc=started,
            end_utc=datetime.now(timezone.utc).isoformat(),
            count=len(files),tree_sha256=aggregate(files),files=files)
        before_files = record["files"]
        tree_summary[label] = dict(
            root=str(root),before_count=len(before_files),after_count=len(files),
            before_sha256=aggregate(before_files),after_sha256=aggregate(files),
            unchanged=before_files==files,
            added=sorted(set(files)-set(before_files)),
            removed=sorted(set(before_files)-set(files)),
            modified=[p for p in before_files.keys() & files.keys()
                      if before_files[p]!=files[p]])
        if label in git_before:
            def git(*a):
                return subprocess.check_output(
                    ["git","--no-optional-locks","-C",str(root),*a],text=True).strip()
            git_after[label] = dict(head=git("rev-parse","HEAD"),
                tracked_status=git("status","--porcelain","--untracked-files=no"))
        print(f"fingerprint after: {label} {len(files)} {aggregate(files)}",flush=True)
    external_after = {group:{p:digest(p) for p in paths}
                      for group,paths in external_before.items()}
    snapshot_path = args.integrity_receipt.resolve().with_suffix(".after.json")
    with snapshot_path.open("x",encoding="utf-8") as handle:
        json.dump(after,handle,indent=2)
    external_summary = {group:dict(count=len(paths),unchanged=paths==external_after[group],
                                  before_sha256=aggregate(paths),
                                  after_sha256=aggregate(external_after[group]))
                        for group,paths in external_before.items()}
    receipt = dict(
        passed=all(v["unchanged"] for v in tree_summary.values())
               and external_before==external_after and git_before==git_after,
        method="All regular file relative paths and SHA256 contents; .git components excluded; Git HEAD/tracked status separately",
        tree_summary=tree_summary,external_summary=external_summary,
        git_before=git_before,git_after=git_after,
        before_manifest=dict(path=str(args.fingerprint_before.resolve()),sha256=digest(args.fingerprint_before)),
        after_manifest=dict(path=str(snapshot_path),sha256=digest(snapshot_path)),
        external_before_manifest=dict(path=str(args.external_before.resolve()),sha256=digest(args.external_before)),
        external_after=external_after,
        commits_by_this_task=0,pushes_by_this_task=0,publication=False)
    with args.integrity_receipt.open("x",encoding="utf-8") as handle:
        json.dump(receipt,handle,indent=2)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=REPO)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--scratch",type=Path,required=True)
    parser.add_argument("--test-receipt",type=Path)
    parser.add_argument("--packaging-receipt",type=Path)
    parser.add_argument("--integrity-receipt",type=Path)
    parser.add_argument("--fingerprint-before",type=Path)
    parser.add_argument("--external-before",type=Path)
    parser.add_argument("--git-before",type=Path)
    args=parser.parse_args()
    if not sys.dont_write_bytecode:
        parser.error("-B is required")
    repo=args.repo.resolve();output=args.output.resolve();scratch=args.scratch.resolve()
    for path in (output,scratch):
        if path.is_relative_to(repo) or path.is_relative_to(Path(r"C:\TORMENT").resolve()):
            parser.error("output and scratch must be external")
    if output.exists():
        parser.error("no overwrite: output already exists")
    generate=any([args.fingerprint_before,args.external_before,args.git_before])
    if generate:
        if not all([args.fingerprint_before,args.external_before,args.git_before,args.integrity_receipt]):
            parser.error("integrity generation requires all before manifests and receipt destination")
        for p in (args.integrity_receipt.resolve(),args.integrity_receipt.resolve().with_suffix(".after.json")):
            if p.exists() or p.is_relative_to(repo) or p.is_relative_to(Path(r"C:\TORMENT").resolve()):
                parser.error("new integrity receipt/after manifest must be unused external paths")
    scratch.mkdir(parents=True,exist_ok=True)
    run=Path(tempfile.mkdtemp(prefix="supplement_f_",dir=scratch))
    for key in ["TMP","TEMP","TMPDIR","MPLCONFIGDIR","PYTHONPYCACHEPREFIX"]:
        os.environ[key]=str(run)
    tempfile.tempdir=str(run)
    import sympy as sp
    rows,expressions,proofs=mathematics(sp)
    independent_count=len(rows)
    # All independent mathematics exists before opening any prior validation.
    support=repo/"papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form"
    prior_path=support/"PAPER_F_v0.2_VALIDATION.json"
    prior=json.loads(prior_path.read_text(encoding="utf-8"))
    formal=prior["verification"]["formal_coefficients"]
    for name,prior_key in [("kappa_infinity_H5","default_kappa"),
                           ("limiting_lambda_derivative_H5","default_lambda_derivative")]:
        # Only numeric rational strings are compared; no source expression eval.
        rows.append(dict(group="SOURCE_PARITY",name=name+"_prior_comparison",
            evidence="ORACLE_VERSUS_PAPER_ONLY",
            passed=str(expressions[name])==formal[prior_key],
            detail=dict(comparison_loaded_after_independent_math=True,
                        prior_value=formal[prior_key])))
    forbidden=[name for name in sys.modules
               if "paper_f_oracle" in name or "paper_f_exact_checks" in name]
    rows.append(dict(group="SOURCE_PARITY",name="no_prior_engine_import",
        evidence="EXACT_SYMBOLIC",passed=not forbidden,
        detail=dict(forbidden_modules=forbidden,independent_records_before_comparison=independent_count)))
    head=subprocess.check_output(["git","--no-optional-locks","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    rows.append(dict(group="INTEGRITY",name="expected_head",evidence="EXACT_SYMBOLIC",
                     passed=head==HEAD,detail=dict(expected=HEAD,actual=head)))
    if generate:
        make_integrity(args)
    receipts={}
    for name,p in [("test",args.test_receipt),("packaging",args.packaging_receipt),("integrity",args.integrity_receipt)]:
        if p:
            data=json.loads(p.read_text(encoding="utf-8"))
            receipts[name]=dict(path=str(p.resolve()),sha256=digest(p),data=data)
            rows.append(dict(group="INTEGRITY",name=name+"_receipt",
                evidence="BINARY64_RUNTIME_WITNESS" if name=="test" else "EXACT_SYMBOLIC",
                passed=data.get("passed") is True,detail=dict(path=str(p.resolve()))))
    source_paths=[
        repo/"kernel_physics/dynamics.py",repo/"kernel_physics/readouts.py",
        repo/"kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md",
        repo/"kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.md",
        repo/"kernel_physics/tests/parity_oracles/paper_f_oracle.py",
        repo/"kernel_physics/tests/test_parity_p07_p08.py",
        repo/"papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md",
        support/"PAPER_F_THEOREM_AND_PROVENANCE_LEDGER_v0.2.md",
        support/"PAPER_F_SOURCE_CENSUS.md",support/"PAPER_F_LITERATURE_REVIEW_v0.1.md",
        support/"paper_f_exact_checks_v0_2.py",prior_path,
        support/"reviews/CLAUDE_PAPER_F_ADVERSARIAL_REVIEW_v0.1.md",
        repo/"research/GATE_TORUS_INVESTIGATION_v0.1/CHIRAL_TRANSVERSE_REPORT.md",
    ]
    legacy=support.parent/"GATE_TORUS_INVESTIGATION_v0.1"
    source_paths.extend(legacy/p for p in ["TRANSVERSE_AXIS_FALSIFICATION_REPORT.md",
        "CLAUDE_GENERIC_TRANSVERSE_HARMONICS_REVIEW.md","TRANSVERSE_NORMAL_FORM_CLOSEOUT.md"])
    reports=Path(r"C:\Users\Notandi\.codex\reports")
    source_paths.extend(reports/p for p in [
        "TRIOCTAGON_CURRENT_KERNEL_MATHEMATICAL_COMPLETENESS_REVIEW_v0.1.md",
        "TRIOCTAGON_CURRENT_KERNEL_ATLAS_CROSSWALK_v0.1.json",
        "TRIOCTAGON_LANE1_SUPPLEMENT_A_GENERAL_CYCLE_PULLBACK_SOURCE_PACKET_v0.1.md"])
    group_counts={}
    for row in rows:
        item=group_counts.setdefault(row["group"],dict(total=0,passed=0))
        item["total"]+=1;item["passed"]+=int(row["passed"])
    complete=all(row["passed"] for row in rows) and len(receipts)==3
    payload=dict(scope=["F02","F03","F04","F05","F06"],passed=all(r["passed"] for r in rows),
                 check_count=len(rows),checks=rows,expressions=expressions,
                 analytic_proofs=proofs,python=sys.version,sympy=sp.__version__,
                 generated_utc=datetime.now(timezone.utc).isoformat(),
                 checker_sha256=digest(__file__),repo=str(repo),head=head,
                 check_groups=group_counts,closeout_ready=complete,
                 owner_status={name:("FULL" if complete else "HOLD_PENDING_RECEIPTS_OR_FAILURE")
                               for name in ["F02","F03","F04","F05","F06"]},
                 analytic_proofs_certified_by_predicate_count=False,
                 analytic_proof_owner="companion written packet; all-degree and interchange arguments are separately reviewed",
                 receipts=receipts,source_sha256={str(p):digest(p) for p in source_paths},
                 preserved_verifier=dict(executed=False,imported=False,
                     recorded_predicates=prior["verification"]["total"],
                     predicates_merged_into_new_count=False),
                 focused_test_status=receipts.get("test",{}).get("data",{}).get("status","NOT_SUPPLIED"),
                 prior_atlas_07_08_runtime_caveat="UNRESOLVED_NOT_INVESTIGATED",
                 no_other_ledger_rows_reassessed=True)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x",encoding="utf-8") as f:
        json.dump(payload,f,indent=2,default=str)
    print(json.dumps(dict(passed=payload["passed"],check_count=len(rows),
                         failed=[r["name"] for r in rows if not r["passed"]])))
    return 0 if payload["passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
