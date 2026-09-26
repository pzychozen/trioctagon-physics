"""Independent Paper E definitions (1),(2),(8),(13),(15)–(28),(33)–(40).

Accounting is exact six-real-coordinate algebra. Each numeric comparison uses
the sum of absolute defining terms returned here, before calling its target.
"""

import mpmath as mp
import sympy as sp


def exact_state(w):
    return [sp.Rational(complex(v).real) + sp.I*sp.Rational(complex(v).imag) for v in w]


def chiral(w):
    return sp.Matrix([sp.re(v) for v in w]).cross(sp.Matrix([sp.im(v) for v in w]))


def defined(*terms):
    return sp.simplify(sum(terms)), sp.simplify(sum(sp.Abs(t) for t in terms))


@mp.workdps(80)
def number(x):
    x = sp.sympify(x)
    if x.is_Rational:
        return mp.mpf(int(x.p))/int(x.q)
    if x.is_real:
        return mp.mpf(str(sp.N(x, 90)))
    return mp.mpc(number(sp.re(x)), number(sp.im(x)))


@mp.workdps(80)
def staged(w, q, N, t, amplitude, gamma, lock):
    v = [mp.mpc(mp.mpf(complex(z).real), mp.mpf(complex(z).imag)) for z in w]
    kappa = mp.sqrt(sum(abs(z)**2 for z in v))
    theta = 2*mp.pi*(q % N)/N
    harmonic = mp.mpf(amplitude)*kappa/(1+kappa)*mp.cos(3*(theta-mp.mpf(lock)))
    return harmonic*mp.exp(-mp.mpf(gamma)*mp.mpf(t))


def readout_terms(m, c, t, z, alpha, beta):
    m, c, t = [list(map(sp.Rational, v)) for v in (m,c,t)]
    z, alpha, beta = map(sp.Rational, (z,alpha,beta))
    result = {}
    for prefix, signs in (("", (1,1,1)), ("q_", (1,1,-1))):
        mm = [s*v*v for s,v in zip(signs,m)]
        cc = [s*v*v for s,v in zip(signs,c)]
        tt = [s*v*v for s,v in zip(signs,t)]
        wm = [alpha**2*v for v in mm]
        wc = [beta**2*v for v in cc]
        cross = [2*alpha*beta*s*x*y for s,x,y in zip(signs,m,c)]
        names = (("macro_norm_squared","chiral_norm_squared","total_norm_squared",
                  "weighted_macro","weighted_chiral","cross_term","predicted_norm_squared","norm_residual") if not prefix else
                 ("q_macro","q_chiral","q_total","q_weighted_macro","q_weighted_chiral","q_cross_term","q_prediction","q_residual"))
        expressions = (mm,cc,tt,wm,wc,cross,wm+wc+cross,tt+[-v for v in wm+wc+cross])
        result.update({name: defined(*terms) for name,terms in zip(names,expressions)})
    result["macro_relation_residual"] = defined(*(v*v for v in m),-2*z*z)
    for j in range(3):
        result[f"blend_residual:{j}"] = defined(t[j],-alpha*m[j],-beta*c[j])
    return result


def gram_terms(w):
    w = exact_state(w)
    x,y = [sp.re(v) for v in w],[sp.im(v) for v in w]
    c = chiral(w)
    A,B,h = sum(v*v for v in x),sum(v*v for v in y),sum(a*b for a,b in zip(x,y))
    c2 = c.dot(c)
    slack = (A-B)**2/4+h*h
    return {
        "A": defined(*(v*v for v in x)), "B": defined(*(v*v for v in y)),
        "h": defined(*(a*b for a,b in zip(x,y))), "intensity": defined(A,B),
        "chiral_norm": defined(sp.sqrt(c2)), "chiral_norm_squared": defined(*(v*v for v in c)),
        "gram_product": defined(A*B), "h_squared": defined(h*h),
        "gram_rhs": defined(A*B,-h*h), "gram_residual": defined(c2,-A*B,h*h),
        "amplitude_bound": defined(A/2,B/2), "slack_sum_of_squares": defined((A-B)**2/4,h*h),
        "observed_slack": defined((A+B)**2/4,-c2),
        "slack_residual": defined((A+B)**2/4,-c2,-slack),
        **{f"chiral:{j}": defined(x[(j+1)%3]*y[(j+2)%3],-x[(j+2)%3]*y[(j+1)%3]) for j in range(3)},
    }


def potential_expression(w, eps, g, k):
    s = [sp.expand_complex(v*sp.conjugate(v)) for v in w]
    pairs = sum(sp.expand_complex((w[i]-w[j])*sp.conjugate(w[i]-w[j])) for i,j in ((0,1),(0,2),(1,2)))
    return sp.expand(eps*sum(si**2/4-ki*si/2 for si,ki in zip(s,k)) + g*pairs/2)


def intensity_terms(w, eps, g, k):
    w = exact_state(w)
    eps,g = map(sp.Rational,(eps,g))
    k = list(map(sp.Rational,k))
    s = [sp.expand_complex(v*sp.conjugate(v)) for v in w]
    # Independently obtain the increment as the negative six-real gradient.
    x,y = sp.symbols("x0:3",real=True),sp.symbols("y0:3",real=True)
    variables = [x[j]+sp.I*y[j] for j in range(3)]
    potential = potential_expression(variables,eps,g,k)
    substitution = {**dict(zip(x,map(sp.re,w))),**dict(zip(y,map(sp.im,w)))}
    delta = [(-sp.diff(potential,x[j])-sp.I*sp.diff(potential,y[j])).subs(substitution) for j in range(3)]
    pre = [sp.expand(w[j]+delta[j]) for j in range(3)]
    pair_terms = [sp.expand_complex((w[i]-w[j])*sp.conjugate(w[i]-w[j])) for i,j in ((0,1),(0,2),(1,2))]
    onsite_terms = [2*eps*k[j]*s[j] for j in range(3)]+[-2*eps*si**2 for si in s]
    coupling_terms = [-2*g*p for p in pair_terms]
    remainder_terms = [sp.expand_complex(v*sp.conjugate(v)) for v in delta]
    after_terms = [sp.expand_complex(v*sp.conjugate(v)) for v in pre]
    change_terms = onsite_terms+coupling_terms+remainder_terms
    result = {"intensity_before": defined(*s), "intensity_pre_sync": defined(*after_terms),
              "pair_distance_sum": defined(*pair_terms), "onsite": defined(*onsite_terms),
              "coupling": defined(*coupling_terms), "remainder": defined(*remainder_terms),
              "predicted_delta": defined(*change_terms),
              "observed_delta": defined(*after_terms,*[-v for v in s]),
              "residual": defined(*after_terms,*[-v for v in s+change_terms]),
              "potential": defined(*[eps*si**2/4 for si in s],*[-eps*ki*si/2 for ki,si in zip(k,s)],*[g*p/2 for p in pair_terms])}
    for j in range(3):
        dterms = [eps*k[j]*w[j],-eps*s[j]*w[j],g*sum(w),-3*g*w[j]]
        result[f"component_intensities:{j}"] = defined(s[j])
        result[f"increment:{j}"] = defined(*dterms)
        result[f"diagnostic_pre_sync_prediction:{j}"] = defined(w[j],*dterms)
    return result


@mp.workdps(80)
def torus(kappa, q, z, N, R, rmax):
    height = max(abs(mp.mpf(v)) for v in z)+mp.mpf(1e-9)
    result,scales = [],[]
    for k,sector,scalar in zip(kappa,q,z):
        theta = 2*mp.pi*(sector%N)/N
        r = mp.mpf(rmax)*mp.mpf(k)/(1+mp.mpf(k))
        chi = mp.pi*mp.mpf(scalar)/(2*height)
        terms = ((mp.mpf(R)*mp.cos(theta),r*mp.cos(chi)*mp.cos(theta)),
                 (mp.mpf(R)*mp.sin(theta),r*mp.cos(chi)*mp.sin(theta)),
                 (r*mp.sin(chi),))
        result.append([sum(t) for t in terms])
        scales.append([sum(abs(v) for v in t) for t in terms])
    return result,scales
