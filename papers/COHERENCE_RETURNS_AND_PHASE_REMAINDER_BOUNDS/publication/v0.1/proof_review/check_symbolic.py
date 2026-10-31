"""New exact algebra checks only. No native map, old script or solver is executed.

The continuous sector argument is proved in SECTOR_60_REVIEW.md. These checks
support its arithmetic and endpoint identities; they are not a certificate.
"""
from pathlib import Path
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
R = s.Rational
checks = []
def check(name, actual, expected=True):
    ok = bool(s.simplify(actual - expected) == 0) if expected is not True else bool(actual)
    checks.append({'name': name, 'passed': ok, 'actual': str(actual), 'expected': str(expected)})
    if not ok:
        raise AssertionError(name)

eps, g, lam = R(1,10), R(1,60), R(1,300)
kmin, K = R(999,1000), R(1001,1000)
amin, A = 1+eps*kmin-2*g, 1+eps*K-2*g
check('minimum diagonal coefficient', amin, R(31997,30000))
check('maximum diagonal coefficient', A, R(32003,30000))
check('positive self coefficient on B3', amin-9*eps, R(4997,30000))
check('sharp envelope peak squared below 49/25', 40*A**3/27 < R(49,25))
check('looser peak squared', 40*R(27,25)**3/27, R(5832,3125))
check('looser peak margin', R(49,25)-R(5832,3125), R(293,3125))
check('upper-envelope derivative minimum on [0,3/2]', A-3*eps*R(3,2)**2, R(11753,30000))
check('individual minimum derivative on [0,3/2]', amin-3*eps*R(3,2)**2, R(11747,30000))
check('T(3/2) below 3/2', R(3,2)*(1+eps*(K-R(3,2)**2)) < R(3,2))
check('T(sqrt K) equals sqrt K', s.sqrt(K)*(1+eps*(K-K)), s.sqrt(K))
check('self coefficient on returning block', amin-eps*K, R(14497,15000))
check('maximum off-diagonal phase weight', 3*lam, R(1,100))
check('minimum phase diagonal weight', 1-6*lam, R(49,50))
d = s.symbols('d', real=True)
w = lam*s.sin(3*d)/d
check('continuous equal-phase weight', s.limit(w,d,0), 3*lam)
check('positive endpoint weight is zero', w.subs(d,s.pi/3), s.Integer(0))
check('negative endpoint weight is zero', w.subs(d,-s.pi/3), s.Integer(0))
check('signed weights are even', s.simplify(w-w.subs(d,-d)), s.Integer(0))
n = s.symbols('n', integer=True)
check('branch changes leave harmonic sine unchanged', s.expand_trig(s.sin(3*(d+2*s.pi*n)))-s.sin(3*d), s.Integer(0))
x,y,z,a,b = s.symbols('x y z a b', real=True)
check('convex update equals difference update', (1-a-b)*x+a*y+b*z-(x+a*(y-x)+b*(z-x)), s.Integer(0))
L = eps*(3*K-kmin)+3*g
check('aligned Hessian upper bound', L, R(313,1250))
check('aligned potential descent coefficient', 1-L/2, R(2187,2500))
check('prestage perturbation lower bound', eps*(kmin-K)-3*g, -R(251,5000))
check('prestage perturbation upper bound', eps*K, R(1001,10000))
c = eps*K + 2*lam*(1+eps*K)
check('one-step chord coefficient', c, R(53717,500000))
check('three-step multiplier chord bound', 3*c, R(161151,500000))
check('quarter-phase chord is outside bound', (3*c)**2 < 2)
# Retained scalar counterexample: verify the printed rational identity, not F.
r1, r2 = R(43,80), R(2947693,5120000)
check('retained second amplitude arithmetic', r1*(1+eps*(1-r1*r1)), r2)
check('retained repeated-scale comparator', R(43,40)*r1, R(1849,3200))
check('projector counterexample amplitudes differ', r2 != R(1849,3200))
out = {'kind':'exact algebra and endpoint identities, not a numerical existence certificate',
       'native_F_evaluations':0, 'old_scientific_scripts_executed':0,
       'python':sys.version, 'sympy':s.__version__, 'checks':checks,
       'phase_bound_degrees_formatting_only':str(s.N(2*s.asin(R(161151,1000000))*180/s.pi,20)),
       'continuous_sign_proof':'For |d|<=pi/3, x=3d lies in [-pi,pi]; sin(x)/x is nonnegative and <=1. Endpoints give zero, the limit at zero is one. See written proof.'}
(ROOT/'proof_review/SYMBOLIC_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} exact algebra checks passed; native F evaluations: 0; old scientific scripts: 0.')
print('Angle, ordinary formatting only:',out['phase_bound_degrees_formatting_only'],'degrees')
