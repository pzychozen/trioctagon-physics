"""Paper A §§1–3,6: polynomial and 80-digit cycle-map definitions.

The polynomial is expanded into defining addends. L3 is ee^T-3I; the
general cycle is a shift plus its transpose minus 2I, including sizes 1,2.
No runtime constants, helpers, code generation, or research are used.
"""

import mpmath as mp
import sympy as sp


def cycle(n):
    shift = sp.ImmutableMatrix(n, n, lambda i, j: int(j == (i + 1) % n))
    return shift + shift.T - 2 * sp.eye(n)


def pullback(m, d):
    return sp.ImmutableMatrix(m, d, lambda i, j: int(i % d == j))


def polynomial(w, eps, g, k):
    w = sp.Matrix(w)
    lap = sp.ones(3) - 3 * sp.eye(3) if len(w) == 3 else cycle(len(w))
    return sp.Matrix([sp.expand(w[j] + eps * k[j % 3] * w[j]
                     - eps * w[j]**2 * sp.conjugate(w[j])
                     + g * (lap * w)[j]) for j in range(len(w))])


def number(value):
    if isinstance(value, (mp.mpf, mp.mpc)):
        return value
    value = complex(value)
    return mp.mpc(mp.mpf(value.real), mp.mpf(value.imag))


@mp.workdps(80)
def presync(omega, eps, g, k):
    """Return V and fixed sum of magnitudes of expanded defining addends.

    At n=3 the coupling addends are g*sum(w) and -3*g*w_j;
    otherwise they are g*w_left, g*w_right and -2*g*w_j.
    """
    w = [number(v) for v in omega]
    e, c = mp.mpf(eps), mp.mpf(g)
    result, scales = [], []
    for j, v in enumerate(w):
        onsite = [v, e * mp.mpf(k[j % 3]) * v, -e * v * abs(v)**2]
        coupling = ([c * sum(w), -3 * c * v] if len(w) == 3 else
                    [c * w[(j - 1) % len(w)], c * w[(j + 1) % len(w)], -2*c*v])
        terms = onsite + coupling
        result.append(sum(terms))
        scales.append(sum(abs(t) for t in terms))
    return result, scales


@mp.workdps(80)
def synchronize(values, strength):
    """All angles come from one immutable input vector, Arg0(0)=0."""
    v = tuple(number(x) for x in values)
    p = tuple(mp.arg(x) if x else mp.mpf(0) for x in v)
    lam = mp.mpf(strength)
    result, scales = [], []
    for j, z in enumerate(v):
        sins = [mp.sin(3 * (p[l] - p[j]))
                for l in ((j - 1) % len(v), (j + 1) % len(v))]
        scale = abs(z) * (1 + abs(p[j]) + abs(lam) * sum(abs(s) for s in sins))
        result.append(abs(z) * mp.exp(mp.j * (p[j] + lam * sum(sins))) if z else mp.mpc(0))
        scales.append(scale)
    return result, scales


@mp.workdps(80)
def step(omega, eps, g, k, strength):
    v, pre_scales = presync(omega, eps, g, k)
    if strength == 0:
        return v, pre_scales
    return synchronize(v, strength)


def chirality(w):
    x = sp.Matrix([sp.re(v) for v in w])
    y = sp.Matrix([sp.im(v) for v in w])
    return x.cross(y)


@mp.workdps(80)
def chiral_reference(w):
    w = [number(v) for v in w]
    terms = [(w[j].real*w[k].imag, -w[k].real*w[j].imag)
             for j, k in ((1, 2), (2, 0), (0, 1))]
    return [sum(t) for t in terms], [sum(abs(x) for x in t) for t in terms]
