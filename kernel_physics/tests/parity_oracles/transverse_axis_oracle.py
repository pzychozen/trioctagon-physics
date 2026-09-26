"""Independent P5 cross product and bounded P6 Paper F (26)–(27) algebra.

The one-step A angle is from the preserved AX report §3, with positive h
and its stated nonzero local branch. No generic-seed or lambda-jet oracle.
"""
import mpmath as mp
import sympy as sp


@mp.workdps(80)
def cross_reference(omega):
    x = [mp.mpf(complex(v).real) for v in omega]
    y = [mp.mpf(complex(v).imag) for v in omega]
    pairs = [(x[j]*y[k],x[k]*y[j]) for j,k in ((1,2),(2,0),(0,1))]
    return tuple(a-b for a,b in pairs), tuple(abs(a)+abs(b) for a,b in pairs)


def symbolic_cross(w):
    return sp.Matrix([sp.re(v) for v in w]).cross(sp.Matrix([sp.im(v) for v in w]))


def equal_k_polynomial(w,eps,g,kappa=sp.Integer(1)):
    """Printed phase-off component polynomial, only for the P6 subspaces."""
    return sp.Matrix([sp.expand((1-3*g+eps*kappa)*v-eps*v**2*sp.conjugate(v)+g*sum(w)) for v in w])


def a_one_step(h):
    h = sp.sympify(h)
    x = 1-h*h/40
    y = h*(sp.Rational(2,5)-h*h/40)/sp.sqrt(2)
    return sp.Matrix([x+sp.I*y,x-sp.I*y,1]), y*sp.Matrix([1,1,-2+h*h/20])


@mp.workdps(80)
def a_one_step_angle(h):
    h = mp.mpf(h)
    return mp.atan(mp.sqrt(2)*h*h/(20*(6-h*h/10)))


@mp.workdps(80)
def projective_angle(a,b):
    a,b = tuple(mp.mpf(v) for v in a),tuple(mp.mpf(v) for v in b)
    if not any(a) or not any(b):
        raise ValueError("zero chirality has no projective direction")
    cross = [a[j]*b[k]-a[k]*b[j] for j,k in ((1,2),(2,0),(0,1))]
    return mp.atan2(mp.sqrt(sum(v*v for v in cross)),abs(sum(x*y for x,y in zip(a,b))))


@mp.workdps(80)
def signed_elevation(c):
    c = tuple(mp.mpf(v) for v in c)
    if not any(c):
        raise ValueError("zero chirality has no elevation")
    longitudinal = sum(c)/mp.sqrt(3)
    transverse = [v-sum(c)/3 for v in c]
    return mp.atan2(longitudinal,mp.sqrt(sum(v*v for v in transverse)))
