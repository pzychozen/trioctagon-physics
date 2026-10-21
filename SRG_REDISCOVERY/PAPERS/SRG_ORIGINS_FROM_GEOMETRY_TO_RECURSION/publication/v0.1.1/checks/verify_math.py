"""Standalone exact-algebra checks. No imports of project or historical modules.
Run from the revision directory: conda activate torment; python checks/verify_math.py
Writes only checks/MATH_RESULTS.json. Written domain/coverage proofs are in the draft.
"""
from pathlib import Path
from fractions import Fraction
import datetime, json, math, sys
import sympy as s
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(name, condition, evidence):
    passed = bool(condition)
    checks.append(dict(name=name, passed=passed, evidence=str(evidence)))
    if not passed:
        raise AssertionError(name)
def zero(name, expr):
    val = s.simplify(s.trigsimp(expr))
    check(name, val == 0, val)

t = s.symbols('t', positive=True)
q = s.symbols('q', positive=True)
G = 1/(s.exp(t)-1)
Gp = -s.exp(t)/(s.exp(t)-1)**2
S = s.exp(-t)/(1-s.exp(-t))**2
zero('differentiate_closed_G', s.diff(G,t)-Gp)
zero('weighted_sum_equals_negative_derivative', S+Gp)
zero('geometric_closed_form_substitution', q/(1-q)-G.subs(t,-s.log(q)))
zero('q_derivative_weighted_modes', q*s.diff(q/(1-q),q)-q/(1-q)**2)
e_gap = s.symbols('e_gap', positive=True)  # exp(t)-1 > 0 for t>0
gp_gap = -(e_gap+1)/e_gap**2
zero('derivative_positive_gap_parameterization', gp_gap.subs(e_gap,s.exp(t)-1)-Gp)
check('positive_t_derivative_negative', gp_gap.is_negative is True, 'e_gap=exp(t)-1>0; -(e_gap+1)/e_gap**2<0')
check('positive_t_weighted_sum_positive', (-gp_gap).is_positive is True, '(e_gap+1)/e_gap**2>0, and S=-Gp checked exactly')

# Independent rational coefficient recursion for reciprocal of (exp(t)-1)/t.
# This calculation uses Fraction and factorial only, before comparison with CAS.
a = [Fraction(1)]
for k in range(1,9):
    a.append(-sum(a[j]/math.factorial(k-j+1) for j in range(k)))
expected = [Fraction(1),Fraction(-1,2),Fraction(1,12),Fraction(0),Fraction(-1,720),Fraction(0),Fraction(1,30240),Fraction(0),Fraction(-1,1209600)]
check('independent_rational_coefficient_recurrence', a == expected, list(map(str,a)))
poly = sum(s.Rational(v.numerator,v.denominator)*t**(k-1) for k,v in enumerate(a))
zero('CAS_series_agrees_with_independent_recurrence', s.series(G,t,0,8).removeO()-poly)
expected_gp = -1/t**2+s.Rational(1,12)-t**2/240+t**4/6048
zero('derivative_Laurent_coefficients_through_t4', s.series(Gp,t,0,6).removeO()-expected_gp)
zero('weighted_Laurent_coefficients_through_t4', s.series(S,t,0,6).removeO()+expected_gp)
zero('positive_finite_part_limit', s.limit(Gp+1/t**2,t,0,dir='+')-s.Rational(1,12))
zero('negative_finite_part_limit', s.limit(S-1/t**2,t,0,dir='+')+s.Rational(1,12))
x = s.symbols('x', nonnegative=True)
zero('continuum_bulk_integral', s.integrate(x*s.exp(-t*x),(x,0,s.oo))-1/t**2)
check('Bernoulli_B2', s.bernoulli(2) == s.Rational(1,6), s.bernoulli(2))
zero('continued_zeta_value', s.zeta(-1)+s.bernoulli(2)/2)
zero('closed_form_reflection', G.subs(t,-t)+1+G)
C = G+s.Rational(1,2)
zero('centered_coth_identity', C-s.coth(t/2).rewrite(s.exp)/2)
zero('centered_oddness', C.subs(t,-t)+C)
zero('derivative_evenness', Gp.subs(t,-t)-Gp)
zero('composite_chain_rule_minus', s.diff(G.subs(t,-t),t)+Gp)
Reg = G-1/t+s.Rational(1,2)
zero('regular_part_oddness', Reg.subs(t,-t)+Reg)
zero('regular_part_removable_value', s.limit(Reg,t,0))
zero('regular_derivative_at_zero', s.limit(Reg/t,t,0)-s.Rational(1,12))
half = -s.diff(1/(2*s.sinh(t/2)),t)
zero('retained_half_integer_constant', s.limit(half-1/t**2,t,0)-s.Rational(1,24))
zero('retained_half_integer_t2', s.series(half,t,0,4).removeO()-(1/t**2+s.Rational(1,24)-7*t**2/1920))
zero('retained_equilateral_ratio', (s.sqrt(3)/6)**2-s.Rational(1,12))
h = s.symbols('h', positive=True)  # h = 1/N for asymptotics only
finite = s.cot(s.pi*h/2)/(2*s.pi*h)-1/(s.pi*h)**2
zero('retained_finite_cycle_expansion_20', s.series(finite,h,0,6).removeO()-(-s.Rational(1,12)-s.pi**2*h**2/720-s.pi**4*h**4/30240))
N = s.symbols('N', positive=True, integer=True)
zero('retained_inverse_trace_limit_15', s.limit((1-N**-2)/12,N,s.oo)-s.Rational(1,12))

u,v = s.symbols('u v', real=True)
RT,rho = s.symbols('R_T rho_T', positive=True)
Q = s.Matrix([[s.cos(v),-s.sin(v),0],[s.sin(v),s.cos(v),0],[0,0,1]])
Cp = s.Matrix([RT+rho*s.cos(u),0,rho*s.sin(u)])
Cm = s.Matrix([-(RT+rho*s.cos(u)),0,rho*s.sin(u)])
T = s.Matrix([(RT+rho*s.cos(u))*s.cos(v),(RT+rho*s.cos(u))*s.sin(v),rho*s.sin(u)])
for j in range(3):
    zero(f'positive_profile_sweep_coordinate_{j}', (Q*Cp-T)[j])
    zero(f'negative_profile_sweep_coordinate_{j}', (Q*Cm-T.subs(v,v+s.pi))[j])
for i in range(3):
    for j in range(3):
        zero(f'rotation_orthogonality_{i}{j}', (Q.T*Q-s.eye(3))[i,j])
zero('rotation_determinant_plus_one', Q.det()-1)
zero('rotation_preserves_squared_norm', (Q*Cp).dot(Q*Cp)-Cp.dot(Cp))
zero('meridional_surface_equation_under_positive_radial_factor', (RT+rho*s.cos(u)-RT)**2+(rho*s.sin(u))**2-rho**2)
Mx = s.diag(-1,1,1)
check('mirror_determinant_minus_one', Mx.det() == -1, Mx.det())
check('mirror_maps_profile', Mx*Cp == Cm, Mx*Cp)
check('halfturn_maps_profile', Q.subs(v,s.pi)*Cp == Cm, Q.subs(v,s.pi)*Cp)
probe = s.Matrix([0,1,0])
check('mirror_and_halfturn_differ_off_plane', Mx*probe != Q.subs(v,s.pi)*probe, [list(Mx*probe),list(Q.subs(v,s.pi)*probe)])
check('projection_counterexample', list(T.subs({u:0,v:s.pi/2})) == [0,RT+rho,0], T.subs({u:0,v:s.pi/2}))
d = s.symbols('d', positive=True)
zero('ring_condition_implies_positive_radial_lower_bound_identity', (RT+rho*s.cos(u)).subs(RT,rho+d)-(d+rho*(1+s.cos(u))))
check('disjoint_profiles_gap', (2*RT-2*rho).subs(RT,rho+d).is_positive, '2(R_T-rho_T)=2d>0')
# Surface coverage is a written azimuth-range argument, not certified by point sampling.
coverage = {'type':'written proof, draft section 5.5','premise':'R_T>rho_T>0 makes azimuth unique modulo 2pi', 'ranges':['[0,pi]','[pi,2pi]'], 'claim':'union full surface; only shared boundary circles; endpoints alone insufficient'}

mp.mp.dps=80
spots=[]
for ts in ['0.001','0.000001']:
    z=mp.mpf(ts)
    weighted=mp.exp(z)/mp.expm1(z)**2
    rem=weighted-1/z**2
    scaled=(rem+mp.mpf(1)/12)/z**2
    check('high_precision_t2_correction_'+ts, abs(scaled-mp.mpf(1)/240)<z**2/5000, mp.nstr(scaled,60))
    spots.append(dict(t=ts,finite_remainder=mp.nstr(rem,65),scaled_t2_correction=mp.nstr(scaled,65)))
for ts in ['0.25','1','5']:
    z=mp.mpf(ts); val=-mp.exp(z)/mp.expm1(z)**2
    check('negative_derivative_spot_'+ts, val<0, mp.nstr(val,50))

result=dict(status='PASS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),python=sys.version,
            executable=sys.executable,sympy=s.__version__,mpmath=mp.__version__,precision_decimal_digits=80,
            checks=checks,check_count=len(checks),spot_checks=spots,written_coverage_argument=coverage,
            limits=['No historical simulations, project imports, or earlier test suites executed.',
                    'Uniform convergence, analytic-domain and coverage proofs are written arguments, not numerical certification.',
                    'Checks do not establish an author-intended analytic/geometric map or a physical model.'])
(ROOT/'checks/MATH_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f"PASS: {len(checks)} checks; exact algebra primary, 80-digit spots secondary.")
