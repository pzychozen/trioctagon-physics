"""Generic exact signs/trace/section algebra only; no native-map evaluator."""
import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parent
results = []
def check(name, expression, purpose):
    values = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residuals = [sp.simplify(sp.expand(value)) for value in values]
    assert all(value == 0 for value in residuals), (name, residuals)
    results.append({'identity': name, 'result': 'PASS', 'purpose': purpose, 'residual': 'exactly zero'})

a = sp.symbols('a', positive=True, real=True)
b, c, d, e = sp.symbols('b c d e', real=True)
z = sp.Matrix([a, b + sp.I*c, d + sp.I*e])
real = sp.Matrix([a, b, d])
imag = sp.Matrix([0, c, e])
H = z * z.conjugate().T
SG = real*real.T + imag*imag.T
AG = real*imag.T - imag*real.T
check('H = S_G - i A_G', H - (SG - sp.I*AG), 'Check the source area/conjugation orientation independently.')
M = sp.Matrix(3, 3, sp.symbols('m0:9', real=True))
u = sp.symbols('u0:3')
U = sp.diag(*u)
check('(M H)_11 = z_1 (M z)_1 for the positive-real anchor', (M*H)[0, 0] - a*(M*z)[0], 'Check the numerator and normalization convention in the retained kappa formula.')
overlap = (z.conjugate().T * U * M * z)[0]
check('z^dagger U M z = tr(U M H)', overlap - sp.trace(U*M*H), 'Check trace order and absence of an incorrect conjugation.')
check('tr(U M H) = sum_i u_i (M H)_ii', sp.trace(U*M*H) - sum(u[i]*(M*H)[i, i] for i in range(3)), 'Check the explicit diagonal overlap formula.')
ap = sp.symbols('ap', positive=True, real=True)
bp, cp, dp, ep = sp.symbols('bp cp dp ep', real=True)
zp = sp.Matrix([ap, bp + sp.I*cp, dp + sp.I*ep])
kappa = sp.symbols('kappa', nonzero=True)
Bsec = (z.conjugate().T*zp)[0]
check('overlap(kappa z_next) = kappa B_sec', (z.conjugate().T*(kappa*zp))[0] - kappa*Bsec, 'Check the multiplicative overlap-to-section correction; no argument-branch claim is delegated to algebra.')
h0, h1, h2, h3, k0, k1, k2, B, initial = sp.symbols('h0 h1 h2 h3 k0 k1 k2 B initial', nonzero=True)
# For unit h, conjugate(h)=1/h. All following expressions explicitly use that identity.
check('changed-section factors cancel in overlap', (h0/h1*kappa)*(h1/h0*B) - kappa*B, 'Check the opposing h factors and signs in kappa_h and B_sec,h.')
check('three formal factors leave only endpoint h ratio', (h0/h1*k0)*(h1/h2*k1)*(h2/h3*k2) - h0/h3*k0*k1*k2, 'Check finite-product endpoint orientation; the report proves arbitrary length by induction/cancellation.')
check('changed-section initial and output factors recover the same state', (initial/h0)*(h0/h3*k0*k1*k2)*h3 - initial*k0*k1*k2, 'Check reconstructed-state cancellation, including the initial phase.')

result = {
    'status': 'PASS', 'checks': results,
    'python_executable': sys.executable, 'python_version': sys.version, 'sympy_version': sp.__version__,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'limits': 'Generic symbolic matrix and scalar identities only. No native parameters, nonlinear native-step implementation, repository imports, state evaluations, trajectories, solves, or old helper executions. Domain bounds, argument branches, convergence and all-step claims are justified in the written proof, not by this check count.',
}
target = ROOT / 'exact_algebra_results.json'
with target.open('x', encoding='utf-8') as stream:
    json.dump(result, stream, indent=2)
    stream.write('\n')
print(json.dumps({'status': result['status'], 'identities_checked': len(results), 'python': sys.version.split()[0], 'sympy': sp.__version__, 'scope': result['limits']}, indent=2))
