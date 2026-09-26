"""Independent Paper F v0.2 §§2,5–8,12 and Appendices A/B mathematics.

Only SymPy/mpmath are dependencies. No runtime, verifier, saved expectations,
or file access. Exact jets are formal coefficients, never finite-amplitude
trajectories. Full-map functions independently implement Paper A's equations.
Limiting coefficients are exact geometric sums, never long numerical orbits.
"""
import mpmath as mp
import sympy as sp


_EXACT = None


def exact_algebra():
    """Reconstruct coefficient updates in the three-root quotient algebra.

    t is one q_j; t**3=t/2+S/(3 sqrt(6)), S=sin(3 phi). The trace
    sums over all three roots. This keeps common modes through degree five.
    The amplitude jets are obtained by expanding the defining cubic itself;
    phase jets come from atan and sine series, including denominator changes.
    """
    global _EXACT
    if _EXACT is not None:
        return _EXACT
    a, eps, t, S, h = sp.symbols('a eps t S h', real=True)
    A, M, X, B, D, U0, Us, E, P, Q, R, F, K = sp.symbols(
        'A M X B D U0 Us E P Q R F K', real=True)
    rt6 = sp.sqrt(6)
    relation = t**3-t/2-S/(3*rt6)

    def reduce(value):
        return sp.Poly(sp.expand(value), t).rem(sp.Poly(relation, t)).as_expr().expand()

    def trace(value):
        p = sp.Poly(reduce(value), t)
        return 3*p.nth(0)+p.nth(2)

    def difference_power(value, degree):
        return reduce(sum(sp.binomial(degree,j)*(-value)**(degree-j)*trace(value**j)
                          for j in range(degree+1)))

    s2 = rt6*(t*t-sp.Rational(1,3))
    y, x, v = A*t, M+X*s2, B*t+D*S
    u, w = U0+Us*s2+E*S*t, P*t+Q*S+R*S*s2
    real, imag = 1+h*h*x+h**4*u, h*y+h**3*v+h**5*w
    # g=(1-a)/3 and equal k=1; common coupling is trace minus 3*self.
    real_next = sp.Poly(sp.expand(real+eps*real*(1-real**2-imag**2)),h)
    imag_next = sp.Poly(sp.expand(imag+eps*imag*(1-real**2-imag**2)),h)
    real_coeff = {j:reduce(real_next.nth(j)+(1-a)*(trace(z)/3-z))
                  for j,z in ((2,x),(4,u))}
    imag_coeff = {j:reduce(imag_next.nth(j)+(1-a)*(trace(z)/3-z))
                  for j,z in ((1,y),(3,v),(5,w))}

    def amplitudes(yv,xv,vv,uv,wv):
        py,px,pv,pu,pw = [sp.Poly(reduce(z),t) for z in (yv,xv,vv,uv,wv)]
        return dict(A=py.nth(1), X=sp.expand(px.nth(2)/rt6),
                    D=sp.cancel(pv.nth(0)/S), E=sp.cancel(pu.nth(1)/S),
                    R=sp.cancel(pw.nth(2)/(S*rt6)))

    amp = amplitudes(imag_coeff[1],real_coeff[2],imag_coeff[3],real_coeff[4],imag_coeff[5])
    amp_F = sp.expand((amp['E']+amp['A']*amp['D']).subs(E,F-A*D))
    amp_K = sp.expand((amp['R']-amp['X']*amp['D']).subs({E:F-A*D,R:K+X*D}))
    increment = sp.cancel(amp_K/(2*amp['A'])-K/(2*A))

    # atan(Im/Re) through h^5, reconstructed from atan(z)=z-z^3/3+z^5/5.
    p1 = y
    p3 = reduce(v-x*y-y**3/3)
    p5 = reduce(w-x*v+(x*x-u)*y-y*y*v+x*y**3+y**5/5)
    H1 = reduce(3*(trace(p1)-3*p1))
    H3 = reduce(3*(trace(p3)-3*p3)-sp.Rational(9,2)*difference_power(p1,3))
    # sum_l (p1_l-p1_j)^2 (p3_l-p3_j), including the zero self term.
    mixed = reduce(trace(p1*p1*p3)-p3*trace(p1*p1)-2*p1*trace(p1*p3)
                   +2*p1*p3*trace(p1)+p1*p1*trace(p3)-3*p1*p1*p3)
    H5 = reduce(3*(trace(p5)-3*p5)-sp.Rational(27,2)*mixed
                +sp.Rational(81,40)*difference_power(p1,5))
    sync = amplitudes(H1,-y*H1,H3+x*H1,-y*H3-v*H1,H5+x*H3+u*H1)
    sync_F = sp.expand(sync['E']+sync['A']*D+A*sync['D'])
    sync_K = sp.expand((sync['R']-sync['X']*D-X*sync['D']).subs(R,K+X*D))
    sync_kappa = sp.cancel(sync_K/(2*A)-K*sync['A']/(2*A*A))

    monomials = (A**4,A*A*X,X*X,F)
    def lift(expressions):
        return sp.Matrix([[sp.Poly(sp.expand(z),A,X,F).coeff_monomial(term)
                           for term in monomials] for z in expressions])
    T0 = lift((amp['A']**4,amp['A']**2*amp['X'],amp['X']**2,amp_F))
    Ps = lift((4*A**3*sync['A'],2*A*sync['A']*X+A*A*sync['X'],
               2*X*sync['X'],sync_F))
    ell = lift((increment,))
    ell_s = lift((sync_kappa,))
    one_step = sp.factor((ell_s*T0)[0])
    # Phase-only calculation has p=hq and measures the phase-vector angle.
    isolated = reduce(sp.Rational(81,40)*difference_power(t,5))
    isolated_coefficient = sp.simplify(sp.Poly(isolated,t).nth(2)/(2*sp.sqrt(6)*S))
    _EXACT = dict(a=a,eps=eps,t=t,S=S,A=A,X=X,D=D,E=E,R=R,F=F,K=K,
                  amp=amp,amp_F=amp_F,amp_K=amp_K,increment=increment,
                  sync=sync,sync_F=sync_F,sync_K=sync_K,sync_kappa=sync_kappa,
                  T0=T0,Ps=Ps,ell=ell,ell_s=ell_s,
                  one_step_lambda=one_step,isolated=isolated_coefficient)
    return _EXACT


def basis_exact():
    e = sp.Matrix([1,1,1])
    return e, sp.Matrix([1,-1,0])/sp.sqrt(2), sp.Matrix([1,1,-2])/sp.sqrt(6)


def one_step_projections():
    """Exact polynomial projections, reduced by c^2+s^2=1 (no sampling)."""
    a,eps,h,c,s = sp.symbols('a eps h c s', real=True)
    e,u,v = basis_exact()
    q,qp = c*u+s*v,-s*u+c*v
    x = e-eps*h*h*q.applyfunc(lambda z:z*z)
    y = a*h*q-eps*h**3*q.applyfunc(lambda z:z**3)
    C = x.cross(y)
    def reduce(z):
        return sp.Poly(sp.expand(z),c).rem(sp.Poly(c*c+s*s-1,c)).as_expr().expand()
    S3,C3 = 3*s-4*s**3,c*(1-4*s*s)
    S6,C6 = 2*S3*C3,1-2*S3*S3
    actual = [reduce(C.dot(qp)),reduce(C.dot(q)),reduce(C.dot(e/sp.sqrt(3)))]
    expected = [sp.sqrt(3)*h*(a-eps*h*h*(2*a+3)/6+eps**2*h**4*(5+C6)/36),
                sp.sqrt(3)*eps**2*h**5*S6/36,
                sp.sqrt(6)*eps*h**3*(2*a-eps*h*h)*C3/12]
    return dict(symbols=(a,eps,h,c,s), residuals=[reduce(x-y) for x,y in zip(actual,expected)],
                leading=-eps**2/(36*a), actual=actual)


def finite_coefficients(n=8, a=sp.Rational(2,5), eps=sp.Rational(1,20)):
    """Two independent exact routes: reconstructed lift and scalar recurrence."""
    alg = exact_algebra()
    T,ell = [z.subs({alg['a']:a,alg['eps']:eps}) for z in (alg['T0'],alg['ell'])]
    z,kap = sp.Matrix([1,0,0,0]),sp.S.Zero
    r,t,f,scalar = a-2*eps,sp.S.Zero,sp.S.Zero,sp.S.Zero
    rows=[]
    for j in range(n):
        kap = sp.simplify(kap+(ell*z)[0])
        scalar += eps**2/(36*a)*(6*f+eps*(2*r-1)*t*t-(r-2*eps)*a**(2*j)*t-a**(4*j))
        rows.append((kap,sp.factor(scalar)))
        z=T*z
        f,t = (r*f+eps**2*t*t-eps*(1+2*a)*a**(2*j)*t/3+a*a**(4*j)/3,
               r*t+a**(2*j))
    return rows


def infinite_coefficients(a=sp.Rational(2,5),eps=sp.Rational(1,20)):
    alg=exact_algebra()
    T,ell,Ps,ls=[z.subs({alg['a']:a,alg['eps']:eps})
                 for z in (alg['T0'],alg['ell'],alg['Ps'],alg['ell_s'])]
    resolvent=(sp.eye(4)-T).inv()
    z0=sp.Matrix([1,0,0,0])
    return (sp.factor((ell*resolvent*z0)[0]),
            sp.factor(((ls*T*resolvent+ell*resolvent*Ps*T*resolvent)*z0)[0]))


def infinite_scalar(a,r):
    """Sum the scalar recurrence geometrically, separate from the lift."""
    eps,d=(a-r)/2,a*a-r
    T4=1/(1-a**4)
    T2=(T4-2/(1-a*a*r)+1/(1-r*r))/(d*d)
    TA=(T4-1/(1-a*a*r))/d
    Fsum=(eps**2*T2-eps*(1+2*a)*TA/3+a*T4/3)/(1-r)
    return sp.factor(eps**2/(36*a)*(6*Fsum+eps*(2*r-1)*T2-(r-2*eps)*TA-T4))


def finite_closed(n,a,eps):
    """Paper F (39), with finite geometric sums and no fitted coefficients."""
    r,d=a-2*eps,a*a-a+2*eps
    def H(z):
        return sum(z**j for j in range(n))
    rates=(a**4,a*a*r,r*r)
    weights=(eps**2/d**2-eps*(1+2*a)/(3*d)+a/3,
             -2*eps**2/d**2+eps*(1+2*a)/(3*d),eps**2/d**2)
    Fsum=sum(b*(H(rho)-H(r))/(rho-r) for b,rho in zip(weights,rates))
    T2=(H(a**4)-2*H(a*a*r)+H(r*r))/d**2
    TA=(H(a**4)-H(a*a*r))/d
    return sp.factor(eps**2/(36*a)*(6*Fsum+eps*(2*r-1)*T2-(r-2*eps)*TA-H(a**4)))


def basis(phi):
    u=[1/mp.sqrt(2),-1/mp.sqrt(2),mp.mpf(0)]
    v=[1/mp.sqrt(6),1/mp.sqrt(6),-2/mp.sqrt(6)]
    return ([mp.cos(phi)*x+mp.sin(phi)*y for x,y in zip(u,v)],
            [-mp.sin(phi)*x+mp.cos(phi)*y for x,y in zip(u,v)])


def seed(h,phi):
    return [mp.mpc(1,h*q) for q in basis(phi)[0]]


def cross(x,y):
    return [x[j]*y[k]-x[k]*y[j] for j,k in ((1,2),(2,0),(0,1))]


def dot(x,y):
    return mp.fsum(a*b for a,b in zip(x,y))


def chirality(w):
    return cross([z.real for z in w],[z.imag for z in w])


def angle(C,phi):
    q,qp=basis(phi)
    A,B=dot(C,qp),-dot(C,q)
    if A <= 0:
        raise ValueError('Outside the accepted local nonzero angle chart')
    return mp.atan2(B,A)


def presync(w,eps,g):
    return [z+eps*z*(1-abs(z)**2)+g*(sum(w)-3*z) for z in w]


def phase_data(v):
    if any(z==0 for z in v):
        raise ValueError('Paper F oracle requires the nonzero phase chart')
    p=[mp.arg(z) for z in v]
    H=[sum(mp.sin(3*(p[k]-p[j])) for k in range(3) if k!=j) for j in range(3)]
    return p,H


def step(w,eps,g,lam):
    v=presync(w,eps,g)
    if not lam:
        return v
    _,H=phase_data(v)
    return [z*mp.exp(mp.j*lam*b) for z,b in zip(v,H)]


def full_trajectory(h,phi,updates=8):
    if updates != 8:
        raise ValueError('K2c full trajectories are bounded to eight updates')
    w=seed(h,phi)
    rows=[]
    for n in range(1,updates+1):
        w=step(w,mp.mpf(1)/20,mp.mpf(1)/5,mp.mpf(0))
        C=chirality(w)
        rows.append(dict(n=n,state=tuple(w),C=tuple(C),angle=angle(C,phi)))
    return rows


def one_step_angle(h,phi,lam):
    return angle(chirality(step(seed(h,phi),mp.mpf(1)/20,mp.mpf(1)/5,lam)),phi)


def full_derivative(h,phi):
    """Analytic derivative of full finite-amplitude map and atan2 observable."""
    v=presync(seed(h,phi),mp.mpf(1)/20,mp.mpf(1)/5)
    _,H=phase_data(v)
    dv=[mp.j*b*z for b,z in zip(H,v)]
    x,y=[z.real for z in v],[z.imag for z in v]
    dx,dy=[z.real for z in dv],[z.imag for z in dv]
    C=chirality(v)
    dC=[a+b for a,b in zip(cross(dx,y),cross(x,dy))]
    q,qp=basis(phi)
    A,B,Ad,Bd=dot(C,qp),-dot(C,q),dot(dC,qp),-dot(dC,q)
    return (A*Bd-B*Ad)/(A*A+B*B)


def isolated_derivative(h,phi):
    """Different observable: angle of the phase vector p=hq under phase only."""
    q,qp=basis(phi)
    H=[sum(mp.sin(3*h*(q[k]-q[j])) for k in range(3) if k!=j) for j in range(3)]
    return dot(H,qp)/h


def evaluation_allowances(h,phi,lam):
    """A-priori one-step error propagation on rounded inputs, before runtime.

    u=2^-52 conservatively bounds binary64 basic-operation relative errors.
    gamma_32 covers <32 operations per expanded real/imag amplitude component,
    including modulus/square. Elementary functions receive a two-u allowance;
    gamma_8 covers phase arithmetic and polar reconstruction. This is a bounded
    numerical error model, not a proof about every vendor libm implementation.

    Propagate rectangular component errors, using the exact atan2 differential
    (|x|dy+|y|dx)/|z|^2, then product errors through C. The angular separation
    of vectors within distance d of length r is at most asin(d/r). Dot/basis
    rounding and atan2 evaluation are accounted separately. No runtime value
    or discrepancy enters these allowances.
    """
    u=mp.mpf(2)**-52
    def gamma(n):
        return n*u/(1-n*u)
    def norm(x):
        return mp.sqrt(dot(x,x))
    w=[mp.mpc(complex(z)) for z in seed(h,phi)]
    eps,g,l=mp.mpf(float(.05)),mp.mpf(float(.2)),mp.mpf(float(lam))
    v=presync(w,eps,g)
    p,H=phase_data(v)
    component=[]
    argerr=[]
    raderr=[]
    for j,z in enumerate(w):
        terms=[z,eps*z,-eps*z*abs(z)**2,-2*g*z]+[g*w[k] for k in range(3) if k!=j]
        ex=gamma(32)*sum(abs(t.real) for t in terms)
        ey=gamma(32)*sum(abs(t.imag) for t in terms)
        radius=abs(v[j])
        distance=mp.sqrt(ex*ex+ey*ey)
        if radius<=distance:
            raise ValueError('Roundoff ball leaves nonzero phase chart')
        argerr.append((abs(v[j].real)*ey+abs(v[j].imag)*ex)/(radius-distance)**2
                      +2*u*abs(p[j]))
        raderr.append((abs(v[j].real)*ex+abs(v[j].imag)*ey+ex*ex+ey*ey)/(radius-distance)
                      +2*u*radius)
    out=[z*mp.exp(mp.j*l*b) for z,b in zip(v,H)]
    for j in range(3):
        sins=[mp.sin(3*(p[k]-p[j])) for k in range(3) if k!=j]
        # sin is globally 1-Lipschitz. gamma_8 covers subtraction, *3,
        # summation and a conservative elementary-function allowance.
        Herr=sum(3*(argerr[k]+argerr[j])+gamma(8)*(3*abs(p[k]-p[j])+abs(sins[i]))
                 for i,k in enumerate(k for k in range(3) if k!=j))
        terr=argerr[j]+abs(l)*Herr+gamma(8)*(abs(p[j])+abs(l)*sum(abs(s) for s in sins))
        theta=p[j]+l*H[j]
        cs,sn=abs(mp.cos(theta)),abs(mp.sin(theta))
        radius=abs(v[j])
        ex=raderr[j]*(cs+terr)+radius*(sn+terr)*terr+gamma(8)*radius*(cs+terr)
        ey=raderr[j]*(sn+terr)+radius*(cs+terr)*terr+gamma(8)*radius*(sn+terr)
        component.append((ex,ey))
    C=chirality(out)
    Cerr=[]
    for j,k in ((1,2),(2,0),(0,1)):
        xj,yj=abs(out[j].real),abs(out[j].imag)
        xk,yk=abs(out[k].real),abs(out[k].imag)
        exj,eyj=component[j]
        exk,eyk=component[k]
        propagated=xj*eyk+yk*exj+exj*eyk+xk*eyj+yj*exk+exk*eyj
        Cerr.append(propagated+gamma(4)*(xj*yk+xk*yj+propagated))
    q,qp=basis(phi)
    A,B=dot(C,qp),-dot(C,q)
    length=mp.sqrt(A*A+B*B)
    plane_errors=[dot(Cerr,[abs(x) for x in vector]) for vector in (qp,q)]
    evaluation=mp.asin(norm(plane_errors)/length)
    # Each basis component is rounded once from the 80-digit convention.
    dot_errors=[(gamma(8)+u)*sum((abs(c)+dc)*abs(b) for c,dc,b in zip(C,Cerr,vector))
                for vector in (qp,q)]
    angle_evaluation=mp.asin(norm(dot_errors)/(length-norm(plane_errors)))
    angle_evaluation+=2*u*(abs(mp.atan2(B,A))+evaluation+angle_evaluation)
    return dict(binary64_evaluation=evaluation,angle_evaluation=angle_evaluation,
                rounded_input_angle=angle(C,phi),minimum_presync_modulus=min(map(abs,v)),
                state_component_bounds=component)


def difference_envelope(h,phi,delta):
    """Independent finite-amplitude target and predeclared FD uncertainty.

    Truncation is the actual high-precision central-difference bias. Input
    quantization is evaluated independently, including the rounded divisor.
    Finite subtraction/division and separate angle errors are propagated with
    the triangle inequality. A 1e-60 guard covers 80-digit oracle arithmetic;
    the gates also check these quantities independently at 100 digits.
    """
    derivative=full_derivative(h,phi)
    plus,minus=one_step_angle(h,phi,delta),one_step_angle(h,phi,-delta)
    central=(plus-minus)/(2*delta)
    ap,am=evaluation_allowances(h,phi,delta),evaluation_allowances(h,phi,-delta)
    rounded_delta=mp.mpf(float(delta))
    rounded=(ap['rounded_input_angle']-am['rounded_input_angle'])/(2*rounded_delta)
    quantization=abs(rounded-central)
    u=mp.mpf(2)**-52
    gamma4=4*u/(1-4*u)
    arithmetic=gamma4*(abs(ap['rounded_input_angle'])+abs(am['rounded_input_angle'])
                        +ap['binary64_evaluation']+am['binary64_evaluation']
                        +ap['angle_evaluation']+am['angle_evaluation'])/(2*rounded_delta)
    roundoff=(ap['binary64_evaluation']+am['binary64_evaluation'])/(2*rounded_delta)+quantization+arithmetic
    angle_uncertainty=(ap['angle_evaluation']+am['angle_evaluation'])/(2*rounded_delta)
    truncation=abs(central-derivative)
    guard=mp.mpf('1e-60')/delta
    total=truncation+roundoff+angle_uncertainty+guard
    isolated=isolated_derivative(h,phi)
    # A deliberately conservative envelope around the WRONG leading law:
    # its exact phase-only finite-h correction plus all full-map uncertainty.
    isolated_leading=mp.mpf(243)/160*h**4*mp.sin(6*phi)
    isolated_allowance=abs(isolated-isolated_leading)+total
    return dict(derivative=derivative,oracle_centered_difference=central,
                truncation_allowance=truncation,roundoff_allowance=roundoff,
                input_quantization_allowance=quantization,fd_arithmetic_allowance=arithmetic,
                angle_evaluation_allowance=angle_uncertainty,oracle_precision_allowance=guard,
                total_envelope=total,isolated_finite_h_derivative=isolated,
                isolated_leading=isolated_leading,isolated_envelope=isolated_allowance,
                oracle_falsifier_margin=abs(derivative-isolated_leading)-isolated_allowance,
                per_angle_allowances=(ap,am))
