"""Symbolic closeout only. No kernel imports, model evolution, or writes.

Run with the existing interpreter and -B. JSON is emitted to stdout; the
execution wrapper records it alongside the preflight/preservation receipt.
All recurrences below are formal coefficient identities, not trajectories.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
checks = []
e = sp.ones(3, 1)
sqrt6 = sp.sqrt(6)
c, s = sp.symbols('c s', real=True)
a, r, ep, lam = sp.symbols('a r epsilon lambda', real=True)
q = sp.Matrix([c/sp.sqrt(2)+s/sqrt6, -c/sp.sqrt(2)+s/sqrt6, -2*s/sqrt6])
qperp = sp.Matrix([-s/sp.sqrt(2)+c/sqrt6, s/sp.sqrt(2)+c/sqrt6, -2*c/sqrt6])
S = 3*s-4*s**3  # sin(3 phi)
C = c*(1-4*s*s)  # cos(3 phi)
S6 = 2*S*C


def circle(expr):
    return sp.factor(sp.rem(sp.expand(expr), c*c+s*s-1, c))


def had(x, y):
    return x.multiply_elementwise(y)


def power(x, k):
    return x.applyfunc(lambda z: z**k)


def verify(name, residual):
    values = list(residual) if isinstance(residual, sp.MatrixBase) else [residual]
    reduced = [sp.factor(circle(z)) for z in values]
    ok = all(z == 0 for z in reduced)
    checks.append({'name': name, 'passed': ok, 'residuals': [str(z) for z in reduced]})
    if not ok:
        raise AssertionError((name, reduced))


def first_lambda(expr):
    return sp.expand(expr).coeff(lam, 0)+lam*sp.expand(expr).coeff(lam, 1)


def vector_first_lambda(v):
    return v.applyfunc(first_lambda)


def source_evidence():
    result = {}
    for name in ('dynamics.py', 'readouts.py'):
        path = REPO/'kernel_physics'/name
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        tree = ast.parse(text)
        wanted = {'_advance', 'phase_sync', 'step3', 'z_chiral'}
        bodies = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in wanted:
                bodies[node.name] = {'line': node.lineno, 'end_line': node.end_lineno,
                                     'body': ast.get_source_segment(text, node)}
        result[name] = {'path': str(path), 'bytes': len(raw),
                        'sha256': hashlib.sha256(raw).hexdigest(), 'functions': bodies}
    return result


def coefficient_proof():
    tvec = sqrt6*(power(q, 2)-e/3)
    verify('orthonormal seed basis and orientation',
           sp.Matrix([q.dot(q)-1, q.dot(qperp), sum(q), sum(qperp)]) )
    verify('oriented quarter turn', e.cross(q)-sp.sqrt(3)*qperp)
    verify('q cubed', power(q, 3)-q/2-S*e/(3*sqrt6))
    verify('s q product', had(tvec, q)-q/sqrt6-S*e/3)
    verify('s squared product', power(tvec, 2)-e/3+tvec/sqrt6-sp.sqrt(sp.Rational(2,3))*S*q)
    verify('q fifth', power(q, 5)-q/4-5*S*e/(18*sqrt6)-S*tvec/18)
    verify('sixfold angular projection', S*tvec.dot(qperp)-S6/2)

    # Complete jets, including common modes. Coefficient identities for arbitrary
    # amplitudes establish an induction, without advancing any model state.
    A, M, X, B, D, U0, Us, E, P, Q, R = sp.symbols('A M X B D U0 Us E P Q R')
    Y = A*q
    Xv = M*e+X*tvec
    V = B*q+D*S*e
    U = U0*e+Us*tvec+E*S*q
    W = P*q+Q*S*e+R*S*tvec
    h = sp.symbols('h')
    xx, uu, yy, vv, ww = sp.symbols('xx uu yy vv ww')
    real = 1+h*h*xx+h**4*uu
    imag = h*yy+h**3*vv+h**5*ww
    # Source on-site cubic; coupling is exactly linear and added below.
    sr = sp.expand(real+ep*real*(1-real**2-imag**2))
    si = sp.expand(imag+ep*imag*(1-real**2-imag**2))
    scalar_expected = {
        'real h2': ((1-2*ep)*xx-ep*yy**2, sr.coeff(h, 2)),
        'real h4': ((1-2*ep)*uu-ep*(3*xx**2+2*yy*vv+xx*yy**2), sr.coeff(h, 4)),
        'imag h1': (yy, si.coeff(h, 1)),
        'imag h3': (vv-ep*(2*xx*yy+yy**3), si.coeff(h, 3)),
        'imag h5': (ww-ep*(2*xx*vv+2*uu*yy+xx**2*yy+3*yy**2*vv), si.coeff(h, 5)),
    }
    for name, (expected, actual) in scalar_expected.items():
        verify('cubic jet '+name, actual-expected)
    LI = lambda z: a*z+(1-a)*sum(z)*e/3
    LR = lambda z: (a-2*ep)*z+(1-a)*sum(z)*e/3
    # In all symbolic derivations r=a-2 epsilon; substitute only at comparison.
    xp = LR(Xv)-ep*power(Y, 2)
    vp = LI(V)-ep*(2*had(Xv,Y)+power(Y, 3))
    up = LR(U)-ep*(3*power(Xv,2)+2*had(Y,V)+had(Xv,power(Y,2)))
    wp = LI(W)-ep*(2*had(Xv,V)+2*had(U,Y)+had(power(Xv,2),Y)+3*had(power(Y,2),V))
    Mp = (1-2*ep)*M-ep*A*A/3
    Xp = (a-2*ep)*X-ep*A*A/sqrt6
    Bp = a*B-ep*(2*A*M+2*A*X/sqrt6+A**3/2)
    Dp = D-ep*(2*A*X/3+A**3/(3*sqrt6))
    Ep = (a-2*ep)*E-ep*(sqrt6*X*X+2*A*D+A*A*X/3)
    Rp = a*R-ep*(2*X*D+2*A*E/sqrt6+A*X*X/3+3*A*A*D/sqrt6)
    verify('full x2 recurrence', xp-Mp*e-Xp*tvec)
    verify('full y3 recurrence with common imaginary mode', vp-Bp*q-Dp*S*e)
    # For U and W, projection removes irrelevant isotropic/common pieces.
    # More robust extraction: transverse U has Us*s + E*S*q. E is obtained
    # by a symbolic polynomial-basis comparison after subtracting the s part.
    Usp = (a-2*ep)*Us-ep*(6*M*X-3*X*X/sqrt6+2*A*B/sqrt6+A*A*M/sqrt6+A*A*X/6)
    U0p = (1-2*ep)*U0-ep*(3*M*M+X*X+2*A*B/3+A*A*M/3+A*A*X/(3*sqrt6))
    verify('full x4 recurrence includes generated harmonic', up-U0p*e-Usp*tvec-Ep*S*q)
    verify('y5 angular recurrence', wp.dot(qperp)-Rp*S6/2)
    remaining=wp-Rp*S*tvec
    Pnext=circle(remaining.dot(q))
    Qnext=sp.cancel(circle(sum(remaining))/(3*S))
    verify('full y5 harmonic closure', remaining-Pnext*q-Qnext*S*e)
    assert not Pnext.has(c,s) and not Qnext.has(c,s)
    c3 = e.cross(V)+Xv.cross(Y)
    c5 = e.cross(W)+Xv.cross(V)+U.cross(Y)
    verify('no h3 in-plane drift', c3.dot(-q))
    verify('h5 angle extraction', c5.dot(-q)-sp.sqrt(3)*(R-X*D)*S6/2)
    F, K = sp.symbols('F K')
    Fp = (a-2*ep)*F-ep*(sqrt6*X*X+(1+2*a)*A*A*X/3+a*A**4/(3*sqrt6))
    verify('gauge-invariant reduced F', Ep+a*A*Dp-Fp.subs(F,E+A*D))
    L = -ep*F/(a*sqrt6)+ep*(2*(a-2*ep)-1)*X*X/(6*a)+ep*(a-4*ep)*A*A*X/(6*a*sqrt6)-ep**2*A**4/(36*a)
    verify('angular increment from complete jets', (Rp-Xp*Dp)/(2*a*A)-(R-X*D)/(2*A)-L.subs(F,E+A*D))
    return {'variables': (A,M,X,B,D,U0,Us,E,P,Q,R), 'vectors': (Y,Xv,V,U,W),
            'tvec': tvec, 'increment': L, 'F_recurrence': Fp}


def all_n_proof():
    eps = (a-r)/2
    den = a*a-r
    x, z, f = sp.symbols('t A2 f')
    # x=t_n, z=a^(2n), f=f_n. Algebraic recurrence, no model evolution.
    delta = eps**2/(36*a)*(6*f+eps*(2*r-1)*x*x-(r-2*eps)*z*x-z*z)
    forcing = eps**2*x*x-eps*(1+2*a)*z*x/3+a*z*z/3
    bn = [eps**2/den**2-eps*(1+2*a)/(3*den)+a/3,
          -2*eps**2/den**2+eps*(1+2*a)/(3*den), eps**2/den**2]
    u,v = sp.symbols('u v')
    verify('three-rate forcing decomposition', forcing.subs({x:(u-v)/den,z:u})-(bn[0]*u*u+bn[1]*u*v+bn[2]*v*v))
    # Indefinite exponent is represented by independent monomials, proving the
    # closed solution algebraically for any n, instead of fitting finite data.
    verify('t_n solution recurrence', (a*a*u-r*v)/den-r*(u-v)/den-u)
    rho, rn, rhon = sp.symbols('rho r_to_n rho_to_n')
    verify('geometric convolution identity', (rho*rhon-r*rn)/(rho-r)-r*(rhon-rn)/(rho-r)-rhon)
    polys = [sp.Integer(2),
        2*a**4-2*a**3+4*a*a*r-2*a*r-3*a+2*r*r-r,
        2*a**8-2*a**7+4*a**6*r-4*a**5*r-3*a**5+6*a**4*r*r-a**4*r+4*a**4-4*a**3*r*r-2*a**3*r+2*a**3+4*a*a*r**3-2*a*a*r*r-2*a*a*r-3*a*a-2*a*r**3+a*r*r+2*a*r+2*r**4-r**3-3*r*r]
    deltas = []
    # Only three formal coefficient substitutions to cross-check the original
    # reported formulas; the all-n proof above does not depend on this range.
    tv,zv,fv = sp.Integer(0),sp.Integer(1),sp.Integer(0)
    for k, poly in enumerate(polys, 1):
        val = sp.factor(delta.subs({x:tv,z:zv,f:fv}))
        verify('Claude exact Delta '+str(k), val+(a-r)**2*poly/(288*a))
        deltas.append(str(val))
        tv,zv,fv = sp.expand(r*tv+zv),sp.expand(a*a*zv),sp.expand(r*fv+forcing.subs({x:tv,z:zv}))
    T2=(1/(1-a**4)-2/(1-a*a*r)+1/(1-r*r))/den**2
    AT=(1/(1-a**4)-1/(1-a*a*r))/den
    A4=1/(1-a**4)
    fs=(eps**2*T2-eps*(1+2*a)*AT/3+a*A4/3)/(1-r)
    kin=sp.factor(eps**2/(36*a)*(6*fs+eps*(2*r-1)*T2-(r-2*eps)*AT-A4))
    N=4*a**3*r*r+3*a**3*r-4*a**3+a*a*r*r-4*a*a+4*a*r*r-a-2*r*r-3*r+2
    proposed=-(a-r)**2*N/(288*a*(1+a)*(1+a*a)*(1-r)**2*(1+r)*(1-a*a*r))
    verify('independently summed kappa infinity matches proposed expression', kin-proposed)
    default=sp.factor(kin.subs({a:sp.Rational(2,5),r:sp.Rational(3,10)}))
    verify('default rational reduced exactly', default-sp.Rational(13375,1107936648))
    return {'proof_method':'coefficient induction and geometric convolution, not fitted',
            'delta_n_plus_1':str(delta), 'f_forcing':str(forcing),
            'forcing_rate_coefficients':[str(sp.factor(x)) for x in bn],
            'rates':[str(a**4),str(a*a*r),str(r*r),str(r)],
            'Claude_Delta_1_to_3':deltas, 'kappa_infinity':str(kin),
            'default_exact':str(default), 'default_80_digits':str(sp.N(default,80))}


def phase_composition(jets):
    A,M,X,B,D,U0,Us,E,P,Q,R=jets['variables']
    Y,Xv,V,U,W=jets['vectors']
    # atan(I/R) jet, followed by sin(3*(p_l-p_j)); no phase API is called.
    p1=Y
    p3=V-had(Xv,Y)-power(Y,3)/3
    p5=W-had(Xv,V)+had(power(Xv,2)-U,Y)-had(power(Y,2),V)+had(Xv,power(Y,3))+power(Y,5)/5
    S1=3*(sum(p1)*e-3*p1)
    J3=sp.Matrix([sum((p1[k]-p1[j])**3 for k in range(3)) for j in range(3)])
    Jmix=sp.Matrix([sum((p1[k]-p1[j])**2*(p3[k]-p3[j]) for k in range(3)) for j in range(3)])
    J5=sp.Matrix([sum((p1[k]-p1[j])**5 for k in range(3)) for j in range(3)])
    S3=3*(sum(p3)*e-3*p3)-sp.Rational(9,2)*J3
    S5=3*(sum(p5)*e-3*p5)-sp.Rational(27,2)*Jmix+sp.Rational(81,40)*J5
    verify('phase S1', S1+9*A*q)
    beta=B-A*M-A*X/sqrt6-A**3/6
    sigma=-9*beta+sp.Rational(81,4)*A**3
    verify('phase S3 isotropic transverse', S3-sigma*q)
    dY=S1
    dX=-had(Y,S1)
    dV=S3+had(Xv,S1)
    dU=-had(Y,S3)-had(V,S1)
    dW=S5+had(Xv,S3)+had(U,S1)
    dA=-9*A
    dXs=9*A*A/sqrt6
    dD=-3*A*X
    dE=9*A*D
    dR=-9*R+9*X*D-3*A*X*X+9*A*A*D/sqrt6-3*X*A**3/sqrt6+sp.Rational(47,16)*A**5
    verify('sync x2 scalar update', dX-3*A*A*e-dXs*jets['tvec'])
    verify('sync common y3 coefficient', sum(dV)/3-dD*S)
    verify('sync x4 generated harmonic', dU-( -A*sigma+9*A*B)*power(q,2)-dE*S*q)
    verify('sync y5 angular coefficient', dW.dot(qperp)-dR*S6/2)
    verify('isolated phase-angle 243/160 reproduced with its own input',
           sp.Rational(81,40)*J5.dot(qperp)-sp.Rational(243,160)*A**5*S6)
    verify('sync gauge-invariant F change', dE+dA*D+A*dD+3*A*A*X)
    dsync=sp.Rational(47,32)*A**4-3*X*A*A/(2*sqrt6)
    verify('sync angular increment with denominator change',
           (dR-dXs*D-X*dD)/(2*A)-(R-X*D)*dA/(2*A*A)-dsync)
    # Explicit source-composed one-step jets for an independent projection.
    repl={A:a,M:-ep/3,X:-ep/sqrt6,B:-ep/2,D:-ep/(3*sqrt6),U0:0,Us:0,E:0,P:0,Q:0,R:0}
    newY=(Y+lam*dY).subs(repl)
    newX=(Xv+lam*dX).subs(repl)
    newV=(V+lam*dV).subs(repl)
    newU=(U+lam*dU).subs(repl)
    newW=(W+lam*dW).subs(repl)
    cp1=e.cross(newY)
    cp3=vector_first_lambda(e.cross(newV)+newX.cross(newY))
    cp5=vector_first_lambda(e.cross(newW)+newX.cross(newV)+newU.cross(newY))
    k1=-ep**2/(36*a)+lam*(ep*a*a/4+sp.Rational(47,32)*a**4)
    verify('composed one-step tangent', cp1-sp.sqrt(3)*a*(1-9*lam)*qperp)
    verify('composed one-step no h3 in-plane component', cp3.dot(-q))
    verify('composed one-step h5 angular numerator',cp5.dot(-q)-first_lambda(sp.sqrt(3)*a*(1-9*lam)*k1)*S6)
    out=(ep-9*lam*a*a)/(3*sp.sqrt(2))
    verify('composed one-step leading signed out-of-plane angle',
           cp3.dot(e/sp.sqrt(3))-first_lambda(sp.sqrt(3)*a*(1-9*lam)*out)*C)
    # Prove and sum the first-order lambda coefficient lift. Its state holds
    # Taylor monomials A^4,A^2 X,X^2,F, not Omega or trajectory samples.
    T0=sp.Matrix([[a**4,0,0,0],[-ep*a*a/sqrt6,a*a*r,0,0],
                  [ep**2/6,-2*r*ep/sqrt6,r*r,0],
                  [-ep*a/(3*sqrt6),-ep*(1+2*a)/3,-ep*sqrt6,r]])
    Psync=sp.Matrix([[-36,0,0,0],[9/sqrt6,-18,0,0],[0,18/sqrt6,0,0],[0,-3,0,0]])
    ell=sp.Matrix([[-ep**2/(36*a),ep*(r-2*ep)/(6*a*sqrt6),ep*(2*r-1)/(6*a),-ep/(a*sqrt6)]])
    ellphase=sp.Matrix([[sp.Rational(47,32),-3/(2*sqrt6),0,0]])
    z0=sp.Matrix([1,0,0,0])
    resolvent=(sp.eye(4)-T0).inv()
    base=sp.factor((ell*resolvent*z0)[0].subs(ep,(a-r)/2))
    derivative=sp.factor(((ellphase*T0*resolvent+ell*resolvent*Psync*T0*resolvent)*z0)[0].subs(ep,(a-r)/2))
    vals={a:sp.Rational(2,5),r:sp.Rational(3,10)}
    defbase=sp.factor(base.subs(vals))
    defder=sp.factor(derivative.subs(vals))
    verify('lift resolvent matches zero-lambda theorem',defbase-sp.Rational(13375,1107936648))
    N=4*a**3*r*r+3*a**3*r-4*a**3+a*a*r*r-4*a*a+4*a*r*r-a-2*r*r-3*r+2
    verify('symbolic lift resolvent matches all-n expression',
           base+(a-r)**2*N/(288*a*(1+a)*(1+a*a)*(1-r)**2*(1+r)*(1-a*a*r)))
    # Scalar polynomial checks of the lift, independent of matrix inversion.
    AA,XX,FF=sp.symbols('AA XX FF')
    zb=sp.Matrix([AA**4,AA**2*XX,XX**2,FF])
    abar=a*AA
    xbar=r*XX-ep*AA*AA/sqrt6
    fbar=r*FF-ep*(sqrt6*XX*XX+(1+2*a)*AA*AA*XX/3+a*AA**4/(3*sqrt6))
    verify('amplitude coefficient lift algebra',
           sp.Matrix([abar**4,abar*abar*xbar,xbar*xbar,fbar])-T0*zb)
    zs=sp.Matrix([(AA*(1-9*lam))**4,(AA*(1-9*lam))**2*(XX+9*lam*AA*AA/sqrt6),
                  (XX+9*lam*AA*AA/sqrt6)**2,FF-3*lam*AA*AA*XX])
    verify('sync coefficient lift algebra', vector_first_lambda(zs)-(sp.eye(4)+lam*Psync)*zb)
    return {'order':'exact in epsilon,g; first order in lambda, through chirality h5',
            'tangent_multiplier':str(a*(1-9*lam)),
            'one_step_in_plane_kappa':str(k1),
            'one_step_signed_out_of_plane_h2_cos3phi':str(out),
            'one_step_default_lambda_coefficient':str((ep*a*a/4+sp.Rational(47,32)*a**4).subs({a:sp.Rational(2,5),ep:sp.Rational(1,20)})),
            'phase_only_angle_coefficient_reported':'243/160; different observable and input chart',
            'sync_chirality_increment':str(dsync),
            'T0':[[str(x) for x in row] for row in T0.tolist()],
            'Psync':[[str(x) for x in row] for row in Psync.tolist()],
            'ell':[str(x) for x in ell], 'ellphase':[str(x) for x in ellphase],
            'kappa_infinity_lambda_derivative':str(derivative),
            'default_derivative_exact':str(defder),
            'default_derivative_80_digits':str(sp.N(defder,80))}


def main():
    for value in (sp.Rational(9,10),sp.Rational(3,10),sp.Rational(2,5)):
        numerator,denominator=sp.fraction(value)
        valuation=sp.factorint(numerator).get(5,0)-sp.factorint(denominator).get(5,0)
        verify('exact target 5-adic valuation '+str(value),valuation+1)
    jets=coefficient_proof()
    alln=all_n_proof()
    phase=phase_composition(jets)
    receipt=json.loads((HERE/'TRANSVERSE_NORMAL_FORM_RESULTS.json').read_text(encoding='utf-8'))
    preserved=[]
    for path, old in receipt['preflight']['protected'].items():
        raw=Path(path).read_bytes()
        actual={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
        ok=actual['sha256']==old['sha256'] and actual['bytes']==old['bytes']
        preserved.append({'path':path,'unchanged':ok,**actual})
        if not ok:
            raise AssertionError(('protected identity changed',path))
    forbidden=[x for x in sys.modules if x=='kernel_physics' or x.startswith('kernel_physics.')]
    if forbidden:
        raise AssertionError(('kernel module imported',forbidden))
    result={'task':'RESEARCH_TRANSVERSE_NORMAL_FORM_CLOSEOUT_v0.1',
            'runtime':{'python':sys.version,'executable':sys.executable,'sympy':sp.__version__},
            'all_n':alln,'phase_composition':phase,'checks':checks,
            'passed':sum(x['passed'] for x in checks),'total':len(checks),
            'source_evidence':source_evidence(),'protected_reconciliation':preserved,
            'kernel_modules_imported':forbidden,'model_evolution_calls':0,
            'model_trajectories':0,'numeric_parameter_sweeps':0,
            'nonresonance':{'spectrum':['9/10','3/10','3/10','2/5','2/5'],
              'all_target_5_adic_valuations':[-1,-1,-1,-1,-1],
              'degree_d_monomial_valuation':'-d',
              'contradiction_for_d_ge_2':'-d != -1; repeated eigenspaces only aggregate exponents'},
            'theorem_reference':{'author':'Marco Abate','title':'Discrete holomorphic local dynamical systems',
              'locator':'Theorem 5.15, printed p.36 (PDF page 38)',
              'url':'https://pagine.dm.unipi.it/abate/articoli/artric/files/DiscHolLocDynSys.pdf'}}
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=='__main__':
    main()
