"""Static frame, phase-action and orientation algebra; no project/native/observer code."""
import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parent
sqrt = sp.sqrt
R = sp.Rational
ez = sp.Matrix([0, 0, 1])
r = sqrt(3)/6
origin = sp.Matrix([0, r, 0])
centres = [sp.Matrix([-R(1,4), sqrt(3)/4, 0]), sp.zeros(3,1), sp.Matrix([R(1,4), sqrt(3)/4, 0])]
normals = [sp.Matrix([-sqrt(3)/2, R(1,2), 0]), sp.Matrix([0,-1,0]), sp.Matrix([sqrt(3)/2,R(1,2),0])]
tangents = [sp.Matrix([-R(1,2),-sqrt(3)/2,0]), sp.Matrix([1,0,0]), sp.Matrix([-R(1,2),sqrt(3)/2,0])]
supports = [sp.Matrix([sqrt(3)/2,-R(1,2),0]), sp.Matrix([0,1,0]), sp.Matrix([-sqrt(3)/2,-R(1,2),0])]
checks = []

def check(name, residuals, purpose):
    flat = []
    for residual in residuals:
        flat.extend(list(residual) if isinstance(residual, sp.MatrixBase) else [residual])
    reduced = [sp.simplify(sp.trigsimp(sp.expand(value))) for value in flat]
    assert all(value == 0 for value in reduced), (name, reduced)
    checks.append({'identity': name, 'result': 'PASS', 'residual': 'exactly zero', 'purpose': purpose})

check('Fixed-gap trigonometric directions equal the transcribed g_k', [supports[k] - sp.Matrix([sp.cos(-sp.pi/2+(2*k+1)*sp.pi/3), sp.sin(-sp.pi/2+(2*k+1)*sp.pi/3), 0]) for k in range(3)], 'Corroborate label order and planar orientation without constructing geometry.')
check('n_i = -g_(i-1) and c_i - O = r n_i', [value for i in range(3) for value in (normals[i]+supports[i], centres[i]-origin-r*normals[i])], 'Verify the positioned-axis match, not just a parallel-direction match.')
check('Right-handed orthonormal tangent frames and tangent projector', [value for n,t in zip(normals,tangents) for value in (t-ez.cross(n), n.dot(n)-1, t.dot(t)-1, t.dot(ez), n.cross(t)-ez, n.cross(ez)+t, t*t.T+ez*ez.T-(sp.eye(3)-n*n.T))], 'Fix the rotation sign and decoder inverse/projection domain.')

q,p,chi = sp.symbols('q p chi', real=True)
phase_residuals = []
for n,t in zip(normals,tangents):
    vector = q*t+p*ez
    multiplied = (q*sp.cos(chi)-p*sp.sin(chi))*t+(q*sp.sin(chi)+p*sp.cos(chi))*ez
    phase_residuals.append(multiplied-(sp.cos(chi)*vector+sp.sin(chi)*n.cross(vector)))
check('Complex multiplication equals the signed tangent-plane rotation', phase_residuals, 'Check the phase action for arbitrary real q, p and chi on all three frames.')

def cross_matrix(n):
    return sp.Matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])

def rodrigues(n,angle):
    return sp.cos(angle)*sp.eye(3)+sp.sin(angle)*cross_matrix(n)+(1-sp.cos(angle))*n*n.T

point = sp.Matrix(sp.symbols('X Y Z', real=True))
affine_residuals = []
for c,n,g in zip(centres,normals,supports):
    rn = rodrigues(n,chi)
    rg = rodrigues(g,-chi)
    affine_residuals.extend([rn-rg, c+rn*(point-c)-(origin+rg*(point-origin))])
check('Normal-axis rotation equals opposite signed support-axis rotation, including affine origin', affine_residuals, 'Check the line-position and directed-angle conventions for based endpoints.')

gram = []
for i in range(3):
    for j in range(i+1,3):
        vi = sp.cos(chi)*tangents[i]+sp.sin(chi)*ez
        vj = sp.cos(chi)*tangents[j]+sp.sin(chi)*ez
        gram.extend([tangents[i].dot(tangents[j])+R(1,2), vi.dot(vj)-tangents[i].dot(tangents[j])-R(3,2)*sp.sin(chi)**2])
check('First admitted witness: pairwise Gram changes by (3/2) sin(chi)^2', gram, 'Verify the necessary condition chi = 0 or pi modulo 2 pi; no native step is evaluated.')

V = sp.Matrix.hstack(*[(t+ez)/sqrt(2) for t in tangents])
det_expected = 3*sqrt(6)/8
check('Second admitted witness: nonzero oriented volume changes sign at a half-turn', [V.det()-det_expected, (-V).det()+det_expected], 'Corroborate full rank and the proper-orientation obstruction at chi = pi.')
assert det_expected.is_positive is True

qr = sp.Matrix(sp.symbols('q1:4', real=True))
pr = sp.Matrix(sp.symbols('p1:4', real=True))
a12 = qr[0]*pr[1]-pr[0]*qr[1]
a13 = qr[0]*pr[2]-pr[0]*qr[2]
a23 = qr[1]*pr[2]-pr[1]*qr[2]
check('Raw channel chirality is (a23, -a13, a12)', [qr.cross(pr)-sp.Matrix([a23,-a13,a12])], 'Keep the historical channel-area sign convention distinct from ambient axial projection.')

record = {
    'status': 'PASS',
    'checks': checks,
    'second_witness_determinant': str(det_expected),
    'second_witness_determinant_positive': True,
    'python_executable': sys.executable,
    'python_version': sys.version,
    'sympy_version': sp.__version__,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'limits': 'Static exact algebra with directly transcribed frame constants and symbolic q, p, chi only. No repository import, native map, geometry constructor, observer update, old helper, historical checker, trajectory or parameter scan. The universal quantifier and domain admissibility are proved in the written note, not established by a check count.',
}
with (ROOT / 'exact_algebra_results.json').open('x', encoding='utf-8') as out:
    json.dump(record, out, indent=2)
    out.write('\n')
print(json.dumps({'status': 'PASS', 'identity_groups': len(checks), 'second_witness_determinant': str(det_expected), 'python': sys.version.split()[0], 'sympy': sp.__version__}, indent=2))
