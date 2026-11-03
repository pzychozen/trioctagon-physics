"""Standalone symbolic identities only: no time stepping, sampling, or project imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []

def check(name, expression, locator):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residuals = [s.trigsimp(s.expand(e)) for e in entries]
    passed = all(e == 0 for e in residuals)
    checks.append({'name': name, 'proof_locator': locator, 'pass': passed,
                   'exact_residuals': [str(e) for e in residuals]})
    if not passed:
        raise AssertionError((name, residuals))

def cross_matrix(v):
    return s.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

a = s.Matrix(s.symbols('a1:4', real=True))
b = s.Matrix(s.symbols('b1:4', real=True))
x = a.col_join(b)
K = s.Matrix(2, 3, s.symbols('K0:6', real=True))
y = s.Matrix(s.symbols('y_plus y_minus', real=True))
z = s.Matrix(s.symbols('z_plus z_minus', real=True))
alpha, beta = s.symbols('alpha_N beta_R', positive=True)
etaN, etaR = s.symbols('eta_N eta_R', nonnegative=True)
mu = etaN/(2*alpha)
C = a.cross(b)
f = K*C
J = f.jacobian(x)
w = K.T*y
xdot = -mu*J.T*y
check('chiral_jacobian', J-K*(-cross_matrix(b)).row_join(cross_matrix(a)), 'A1')
check('degree_two_euler', J*x-2*f, 'A1')
check('transpose_signs', J.T*y-b.cross(w).col_join(w.cross(a)), 'A1')
check('core_vector_form', xdot-(mu*w.cross(b)).col_join(-mu*w.cross(a)), 'A1')
PN = etaN*(f.dot(y))
PR = etaR*(z.dot(y))
check('native_power', alpha*x.dot(xdot)+PN, 'A2')
check('receiver_power', beta*z.dot(etaR*y/beta)-PR, 'A2')
check('total_power_cancellation', -PN+(PN-PR)+PR, 'A2')
check('reversing_involution_finite_feedback', xdot.xreplace({yi: -yi for yi in y})+xdot, 'B2')
D = a.dot(a)-b.dot(b)
S = a.dot(b)
I = x.dot(x)
check('Z2_real_invariant', s.Matrix([D]).jacobian(x).dot(xdot), 'B3')
check('Z2_imaginary_invariant', s.Matrix([2*S]).jacobian(x).dot(xdot), 'B3')
check('intensity_chirality_identity', I**2-(D**2+4*S**2)-4*C.dot(C), 'B3')
theta = s.symbols('theta', real=True)
ac = s.cos(theta)*a-s.sin(theta)*b
bc = s.sin(theta)*a+s.cos(theta)*b
check('common_phase_chiral_invariance', ac.cross(bc)-C, 'B4')
Q = s.BlockMatrix([[s.cos(theta)*s.eye(3), -s.sin(theta)*s.eye(3)],
                   [s.sin(theta)*s.eye(3), s.cos(theta)*s.eye(3)]]).as_explicit()
limit_matrix = s.BlockMatrix([[s.zeros(3), mu*cross_matrix(w)],
                              [-mu*cross_matrix(w), s.zeros(3)]]).as_explicit()
check('common_phase_vector_field_equivariance', limit_matrix*Q-Q*limit_matrix, 'B4')
eps, q = s.symbols('epsilon_c q', positive=True)
tent = (1-q/eps)/eps
check('tent_unit_integral', 2*s.integrate(tent, (q, 0, eps))-1, 'A3')
check('tent_squared_norm', 2*s.integrate(tent**2, (q, 0, eps))-2/(3*eps), 'A3')
check('tent_derivative_squared_norm', 2*s.integrate(s.diff(tent,q)**2, (q,0,eps))-2/eps**3, 'A3')
phi, yaw = s.symbols('phi delta_g', real=True)
gain = s.symbols('kappa_in_lambda_g', positive=True)
Rz = s.Matrix([[s.cos(yaw), -s.sin(yaw), 0], [s.sin(yaw), s.cos(yaw), 0], [0,0,1]])
normals = s.Matrix([[0,2,s.sqrt(3)], [0,2,-s.sqrt(3)]])/s.sqrt(7)
Kreg = gain*normals*Rz
ae = s.Matrix([1,s.cos(phi),1])
be = s.Matrix([0,s.sin(phi),0])
fe = Kreg*ae.cross(be)
fexpected = gain*s.sin(phi)/s.sqrt(7)*s.Matrix([-2*s.sin(yaw)+s.sqrt(3), -2*s.sin(yaw)-s.sqrt(3)])
check('coherent_nonzero_drive_formula', fe-fexpected, 'B1')
check('nonzero_port_difference', fe[0]-fe[1]-2*s.sqrt(3)*gain*s.sin(phi)/s.sqrt(7), 'B1')
W = s.symbols('W', positive=True)
wd = s.Matrix([0,0,-W])
ade = mu*wd.cross(be)
bde = -mu*wd.cross(ae)
phase_deriv = [(ae[i]*bde[i]-be[i]*ade[i])/(ae[i]**2+be[i]**2) for i in range(3)]
check('outward_boundary_phase_span', phase_deriv[1]-phase_deriv[0]-2*mu*W*s.cos(phi), 'C4')
yrealize = s.Matrix([-s.sqrt(7)*W/(2*s.sqrt(3)*gain), s.sqrt(7)*W/(2*s.sqrt(3)*gain)])
check('accessible_vertical_feedback', Kreg.T*yrealize-wd, 'C4')

# Exact finite-step polynomial identity. Synchronization preserves moduli;
# no native recurrence, Arg routine, or time trajectory is executed here.
epn, gn = s.symbols('epsilon_native g_native', real=True)
ks = s.symbols('k1:4', real=True)
LN = s.ones(3)-3*s.eye(3)
si = [a[i]**2+b[i]**2 for i in range(3)]
ha = s.Matrix([(ks[i]-si[i])*a[i] for i in range(3)])
hb = s.Matrix([(ks[i]-si[i])*b[i] for i in range(3)])
da, db = epn*ha+gn*LN*a, epn*hb+gn*LN*b
dpre = da.col_join(db)
edges = sum((a[i]-a[j])**2+(b[i]-b[j])**2 for i in range(3) for j in range(i+1,3))
claimed = 2*epn*sum(si[i]*(ks[i]-si[i]) for i in range(3))-2*gn*edges+dpre.dot(dpre)
check('native_full_finite_square_identity', (x+dpre).dot(x+dpre)-I-claimed, 'C1')
fullsquare = epn**2*(ha.dot(ha)+hb.dot(hb))+2*epn*gn*(ha.dot(LN*a)+hb.dot(LN*b))+gn**2*((LN*a).dot(LN*a)+(LN*b).dot(LN*b))
check('full_square_keeps_mixed_term', dpre.dot(dpre)-fullsquare, 'C1')
check('edge_once_graph_square', (LN*a).dot(LN*a)+(LN*b).dot(LN*b)-3*edges, 'C1')
native_q = s.Matrix([s.Rational(9999,10000),1,s.Rational(10001,10000)])
fixed_k = s.Matrix([s.Rational(999,1000),1,s.Rational(1001,1000)])
check('aligned_exact_native_prestage', s.ones(3,1)+s.Rational(1,10)*(fixed_k-s.ones(3,1))-native_q, 'C2')
check('aligned_exact_native_increment', native_q.dot(native_q)-3-s.Rational(1,50000000), 'C2')
tau = s.symbols('tau', real=True)
q1,q2,q3 = s.symbols('q1 q2 q3', positive=True)
om_limit = s.Matrix([q1*s.cosh(mu*W*tau)-s.I*q2*s.sinh(mu*W*tau),
                    q2*s.cosh(mu*W*tau)+s.I*q1*s.sinh(mu*W*tau), q3])
check('hybrid_fast_limit_exact_formula', s.diff(om_limit,tau)-s.I*mu*W*cross_matrix(s.Matrix([0,0,1]))*om_limit, 'C4')

m, fplus, fminus, t = s.symbols('m f_plus f_minus t', real=True)
fzero = s.Matrix([fplus,fminus])
ylead = etaN*t*m*fzero
zlead = etaN*etaR*t**2*m*fzero/(2*beta)
check('short_time_native_coefficient', s.integrate(-etaN*fzero.dot(ylead),(t,0,t))+etaN**2*t**2*m*fzero.dot(fzero)/2, 'B1')
check('short_time_receiver_coefficient', beta*zlead.dot(zlead)/2-etaN**2*etaR**2*t**4*m**2*fzero.dot(fzero)/(8*beta), 'B1')

result = {
    'generated_utc': datetime.now(timezone.utc).isoformat(),
    'python': sys.executable, 'python_version': sys.version, 'sympy_version': s.__version__,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'method': 'Exact symbolic expansion, differentiation, integration and trigonometric simplification. No numerical samples, trajectories, PDE discretization, fitted parameters, project-module imports, or historical helpers.',
    'limitations': 'These identities supplement the written proof. They do not prove the solution concept, analytic remainders, continuation, domain-exit limit, or physical interpretation.',
    'checks': checks, 'all_pass': all(v['pass'] for v in checks)
}
(HERE/'exact_algebra_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_pass': result['all_pass'], 'checks_executed': len(checks), 'sympy': s.__version__}))
