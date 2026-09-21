"""Independent, bounded Phase Bridge II verification; no production changes.

Run with conda torment Python: python -I -S -B -X utf8 this_file.py
Only the two result files next to this script are written. Exact predicates and
fixed numerical witnesses supplement the analytic review, not replace it.
No old audit, test suite, trajectory, random scan, or historical code is run.
"""

from pathlib import Path
import hashlib
import itertools
import json
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.append(str(Path(sys.prefix) / "Lib" / "site-packages"))
sys.path.insert(0, str(ROOT))

import numpy as np
import sympy as s
from kernel_physics import dynamics, geometry

BASELINE = "562fbb5d82b1d05937fda4929eca615e6b8991a1"
CLAUDE_SHA = "e9bc4cf19d5292aa26e69095a75f9f7a64280b11292e8e33d2020a3f03e47b57"
CLAUDE_ORIGINAL = Path(r"C:\TORMENT\TRIOCTAGON_new\research\phase_bridge_II\PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md")
CLAUDE_COPY = HERE / CLAUDE_ORIGINAL.name
records = []
details = {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, predicate, kind="SYMBOLIC"):
    ok = bool(predicate)
    records.append({"id": len(records)+1, "name": name, "kind": kind, "pass": ok})
    if not ok:
        raise AssertionError(name)


def zero(matrix):
    return all(s.simplify(s.expand(v)) == 0 for v in matrix)


def near(a, b, atol=3e-13):
    return np.allclose(a, b, rtol=0, atol=atol)


tracked = subprocess.check_output(
    ["git", "ls-tree", "-r", "--name-only", "-z", BASELINE], cwd=ROOT).decode().strip(chr(0)).split(chr(0))
before = {name: (sha(ROOT/name), (ROOT/name).stat().st_mtime_ns) for name in tracked}
baseline_matches = all(subprocess.check_output(
    ["git", "show", BASELINE+":"+name], cwd=ROOT) == (ROOT/name).read_bytes() for name in tracked)
check("All existing tracked files match the specified baseline", baseline_matches, "INTEGRITY")
original_stat = CLAUDE_ORIGINAL.stat()
check("Claude report copy and external original have the recorded identical bytes",
      sha(CLAUDE_COPY) == CLAUDE_SHA == sha(CLAUDE_ORIGINAL)
      and CLAUDE_COPY.read_bytes() == CLAUDE_ORIGINAL.read_bytes(), "INTEGRITY")

I3 = s.eye(3)
J2 = s.Matrix([[0, -1], [1, 0]])
J6 = s.kronecker_product(I3, J2)
O2, O6 = J2.T, J6.T
R = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
T = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
u = s.ones(3, 1)/s.sqrt(3)
x = s.Matrix([1, -1, 0])/s.sqrt(2)
y = s.Matrix([1, 1, -2])/s.sqrt(6)
U = s.Matrix.hstack(u, x, y)
Pb, Pt = u*u.T, I3-u*u.T
L = s.Matrix(dynamics.L3)
ez = s.Matrix([0, 0, 1])
normal_list = [s.Matrix([-s.sqrt(3)/2, s.Rational(1, 2), 0]),
               s.Matrix([0, -1, 0]), s.Matrix([s.sqrt(3)/2, s.Rational(1, 2), 0])]
frames = [s.Matrix.hstack(ez.cross(n), ez) for n in normal_list]
uu, zz = s.symbols("u z", real=True)
panel_derivatives = [s.Matrix(geometry.panel_point(i, uu, zz)).diff(uu) for i in (1, 2, 3)]
check("Reported face frames follow the existing exact panel-coordinate derivatives",
      all(zero(frames[i][:, 0]-panel_derivatives[i])
          and zero(frames[i][:, 0].cross(ez)-normal_list[i]) for i in range(3)))
check("Each outward-normal cross product gives J2 in its orthonormal tangent frame",
      all(zero(B.T*B-s.eye(2)) and zero(n.cross(B[:, 0])-B[:, 1])
          and zero(n.cross(B[:, 1])+B[:, 0]) for B, n in zip(frames, normal_list)))
check("Metric, J and area form are compatible; area matrix is -J and nondegenerate",
      zero(J2**2+s.eye(2)) and zero(J2.T+J2) and zero(J2.T*J2-s.eye(2))
      and zero(O2-s.Matrix([[0, 1], [-1, 0]])) and O2.det() == 1)
q, p, r, t, nu = s.symbols("q p r t nu", real=True)
v, w = s.Matrix([q, p]), s.Matrix([r, t])
check("omega(v,w)=g(Jv,w)=dq wedge dp(v,w)",
      s.expand((J2*v).dot(w)-(q*t-p*r)) == 0)
H = nu*(q*q+p*p)/2
gradH = s.Matrix([s.diff(H, q), s.diff(H, p)])
XH = -nu*J2*v
check("i_X omega=dH fixes the Hamiltonian sign X=-nu Jv",
      zero(O2.T*XH-gradH))
check("Complex Hamiltonian velocity equals -i nu Omega",
      s.expand(XH[0]+s.I*XH[1]+s.I*nu*(q+s.I*p)) == 0)
time = s.symbols("time", real=True)
flow = s.cos(nu*time)*s.eye(2)-s.sin(nu*time)*J2
check("The stated negative-sign rotation solves the Hamiltonian equation",
      zero(flow.diff(time)+nu*J2*flow) and zero(flow.subs(time, 0)-s.eye(2)))
check("The positive-sign generator does not satisfy the same nonzero Hamiltonian convention",
      not zero(O2.T*(nu*J2*v)-gradH))
check("Each oscillator action (q^2+p^2)/2 is conserved",
      s.expand(v.dot(XH)) == 0)
anisotropic_H = (q*q+2*p*p)/2
anisotropic_X = -J2*s.Matrix([s.diff(anisotropic_H,q),s.diff(anisotropic_H,p)])
check("A positive but anisotropic quadratic is not uniform rotation in the fixed complex coordinate",
      s.solve(list(anisotropic_X+nu*J2*v),nu) == [])

nus = s.symbols("nuA nuB nuC", real=True)
freq = s.diag(*nus)
equations = list(R*freq-freq*R)
solution = s.linsolve(equations, nus)
check("C3 covariance of the diagonal free generator is equivalent to equal face frequencies",
      solution == s.FiniteSet((nus[2], nus[2], nus[2])))
general_C3 = Pb+2*Pt
check("A general C3-invariant quadratic need not have a common mode frequency",
      zero(R*general_C3-general_C3*R)
      and general_C3.eigenvals() == {s.Integer(1): 1, s.Integer(2): 2})
arbitrary = s.Matrix(3, 3, s.symbols("m:9"))
check("Equal-frequency scalar generator commutes with every complex linear map",
      zero(arbitrary*(-s.I*nu*I3)-(-s.I*nu*I3)*arbitrary))
mix = s.Matrix([[1, 1, 0], [-1, 1, 0], [0, 0, s.sqrt(2)]])/s.sqrt(2)
eA = s.Matrix([1, 0, 0])
mixed = mix*eA
check("A free-flow unitary can preserve total norm while changing individual face actions",
      zero(mix.T*mix-I3) and mixed.dot(mixed) == eA.dot(eA)
      and mixed[0]**2 != eA[0]**2)

GR = s.kronecker_product(R, s.eye(2))
GV = s.kronecker_product(T, s.diag(-1, 1))
GH = s.kronecker_product(I3, s.diag(1, -1))
elements = [(GR**k*GV**b*GH**c, (-1)**(b+c))
            for k in range(3) for b in range(2) for c in range(2)]
check("All twelve tangent actions obey the determinant-weighted symplectic pullback",
      len({tuple(M) for M, _ in elements}) == 12
      and all(zero(M.T*O6*M-det*O6) for M, det in elements))
check("Horizontal and vertical mirrors square to identity and reverse common phase flow",
      zero(GH**2-s.eye(6)) and zero(GV**2-s.eye(6))
      and zero(GH*J6+J6*GH) and zero(GV*J6+J6*GV))
improper_rotation = GR*GH
check("An improper D3h element need not be an involution: C3 times horizontal mirror has order six",
      not zero(improper_rotation**2-s.eye(6)) and zero(improper_rotation**6-s.eye(6)))

# Real gradient parent, independently differentiated.
a = s.Matrix(s.symbols("a0:3", real=True))
b = s.Matrix(s.symbols("b0:3", real=True))
z = a+s.I*b
eps, g = s.symbols("eps g", real=True)
ks = s.symbols("k0:3", real=True)
V = eps*sum((a[i]**2+b[i]**2)**2/4-ks[i]*(a[i]**2+b[i]**2)/2 for i in range(3))
V += g*sum((a[i]-a[j])**2+(b[i]-b[j])**2 for i in range(3) for j in range(i+1, 3))/2
A = s.Matrix([eps*z[i]*(ks[i]-a[i]**2-b[i]**2) for i in range(3)])+g*L*z
gradient = s.Matrix([s.diff(V, a[i])+s.I*s.diff(V, b[i]) for i in range(3)])
check("Paper-A amplitude/coupling increment is exactly the negative real gradient",
      zero(A+gradient))

# Complete relative-equilibrium types for three identical third-harmonic phases.
ph = s.Matrix(s.symbols("phi0:3", real=True))
K = s.symbols("K", real=True)
f = s.Matrix([sum(s.sin(3*(ph[j]-ph[i])) for j in range(3) if j != i) for i in range(3)])
D = (K*f).jacobian(ph)
potential = sum(s.cos(3*(ph[j]-ph[i]))/3 for i in range(3) for j in range(i+1, 3))
check("Phase force is a gradient and has zero total angular increment",
      zero(f-s.Matrix([s.diff(potential, t) for t in ph])) and s.simplify(sum(f)) == 0)
check("General phase Jacobian has off-diagonals 3K cos(3 delta) and zero row sums",
      all(s.simplify(D[i,j]-3*K*s.cos(3*(ph[j]-ph[i]))) == 0
          for i in range(3) for j in range(3) if i != j) and zero(D*s.ones(3,1)))
stable_reps = [s.Matrix([0, 2*s.pi*k1/3, 2*s.pi*k2/3]) for k1 in range(3) for k2 in range(3)]
check("All nine third-harmonic synchronized relative branches have Jacobian 3K L3",
      len(stable_reps) == 9 and all(zero(f.subs(dict(zip(ph, v))))
          and zero(D.subs(dict(zip(ph, v)))-3*K*L) for v in stable_reps))
check("Third-harmonic synchronized transverse eigenvalues are -9K,-9K",
      (3*K*L).eigenvals() == {s.Integer(0): 1, -9*K: 2})
cancel_state = s.Matrix([0, 2*s.pi/9, 4*s.pi/9])
anti_state = s.Matrix([0, 0, s.pi/3])
cancel_D = D.subs(dict(zip(ph, cancel_state)))
anti_D = D.subs(dict(zip(ph, anti_state)))
check("A cancelling equilibrium exists with nonzero pairwise sine terms",
      zero(f.subs(dict(zip(ph, cancel_state)))) and s.sin(3*(cancel_state[1]-cancel_state[0])) != 0)
check("Antipodal 2+1 equilibria in theta=3phi have transverse eigenvalues -3K,9K",
      zero(f.subs(dict(zip(ph, anti_state))))
      and anti_D.eigenvals() == {s.Integer(0): 1, -3*K: 1, 9*K: 1})
check("Splay in theta=3phi has transverse eigenvalues 9K/2,9K/2",
      zero(cancel_D+s.Rational(3,2)*K*L))
h = s.symbols("h", real=True)
check("Phase-only Euler has synchronous transverse multiplier 1-9hK",
      zero(U.T*(I3+h*3*K*L)*U-s.diag(1, 1-9*h*K, 1-9*h*K)))
counter_plane = s.Matrix([1, s.I, -1-s.I])
check("A transverse complex vector need not be an equal-amplitude 120-degree splay state",
      zero(u.T*counter_plane) and s.simplify(counter_plane[0]*s.conjugate(counter_plane[0])
          -counter_plane[2]*s.conjugate(counter_plane[2])) != 0)
check("Cyclic 120-degree eigenstates are not fixed vectors of the cyclic permutation",
      not zero(R*s.Matrix([1, (-1+s.I*s.sqrt(3))/2, (-1-s.I*s.sqrt(3))/2])
               -s.Matrix([1, (-1+s.I*s.sqrt(3))/2, (-1-s.I*s.sqrt(3))/2])))

# Chirality is computed as a real polynomial, not imported from historical code.
def Z(values):
    return s.Matrix([s.re(v) for v in values]).cross(s.Matrix([s.im(v) for v in values]))


def monomials(values):
    return s.Matrix([s.conjugate(values[i])*s.prod(values[j] for j in range(3) if j != i)
                     for i in range(3)])


def jeff(values):
    return s.expand(s.im(values[0]*s.conjugate(values[1])*values[2]))


Z0 = a.cross(b)
P = s.expand(z[0]*s.conjugate(z[1])*z[2])
J = s.expand(s.im(P))
alpha = s.symbols("alpha", real=True)
shift = (s.cos(alpha)+s.I*s.sin(alpha))*z
check("Z equals Im(conj Omega_j Omega_k) in the stated component order",
      zero(Z0-s.Matrix([s.im(s.conjugate(z[1])*z[2]),s.im(s.conjugate(z[2])*z[0]),s.im(s.conjugate(z[0])*z[1])])) )
check("Z is invariant under every common phase shift", zero((Z(shift)-Z0).applyfunc(s.trigsimp)))
check("Z and J_eff are conjugation-odd", zero(Z(s.conjugate(z))+Z0) and s.simplify(jeff(s.conjugate(z))+J) == 0)
permutations = [s.eye(3)[list(perm), :] for perm in itertools.permutations(range(3))]
check("Z is a channel pseudovector under all six permutations",
      all(zero(Z(M*z)-M.det()*M*Z0) for M in permutations))
check("Horizontal and vertical spatial mirrors send Z to -Z and T Z",
      zero(Z(s.conjugate(z))+Z0) and zero(Z(-T*s.conjugate(z))-T*Z0))
check("The complex cubic has phase weight +1; real J mixes with its real part",
      s.trigsimp(s.expand(jeff(shift)-s.cos(alpha)*J-s.sin(alpha)*s.re(P))) == 0)
check("Cubic monomials permute as a triple under every channel permutation",
      all(zero(monomials(M*z)-M*monomials(z)) for M in permutations))
check("J_eff is generally not cyclic-invariant", jeff(R*s.Matrix([1,s.I,1])) != jeff(s.Matrix([1,s.I,1])))
check("Horizontal and vertical spatial mirrors send J_eff to -J_eff and +J_eff",
      s.simplify(jeff(s.conjugate(z))+J) == 0 and s.simplify(jeff(-T*s.conjugate(z))-J) == 0)
loop = z[0]*s.conjugate(z[1])*z[1]*s.conjugate(z[2])*z[2]*s.conjugate(z[0])
check("The proposed scalar-amplitude loop product is real nonnegative, with identically zero imaginary part",
      s.expand(loop-s.prod(a[i]**2+b[i]**2 for i in range(3))) == 0
      and s.simplify(s.im(loop)) == 0)
check("Cyclic sum of pairwise imaginary products equals the sum of Z components",
      s.simplify(sum(s.im(s.conjugate(z[i])*z[(i+1)%3]) for i in range(3))-sum(Z0)) == 0)
witness = s.Matrix([1,s.I,1])
check("Nonzero-Z witness: same Z for Omega and i Omega, different J_eff",
      zero(Z(witness)-Z(s.I*witness)) and not zero(Z(witness))
      and jeff(witness) == -1 and jeff(s.I*witness) == 0)
polynomial_map = s.Matrix(list(Z0)+[J])
variables = list(a)+list(b)
Jac = polynomial_map.jacobian(variables)
point = dict(zip(variables, [1,2,1,1,1,-1]))
Jac_at = Jac.subs(point)
minor_cols, minor_value = next((cols, Jac_at[:,cols].det())
    for cols in itertools.combinations(range(6),4) if Jac_at[:,cols].det() != 0)
check("Four polynomials (Zx,Zy,Zz,J_eff) have a full-rank Jacobian witness",
      Jac_at.rank() == 4 and minor_value != 0)
details["algebraic_independence_witness"] = {"a": [1,2,1], "b": [1,1,-1],
    "minor_variables": [str(variables[i]) for i in minor_cols], "minor_determinant": str(minor_value)}

# Centralizer: all complex matrices first, then unitary/determinant constraints.
check("Orthonormal balanced/transverse frame diagonalizes the actual L3",
      zero(U.T*U-I3) and zero(U.T*L*U-s.diag(0,-3,-3)))
Dspec = s.diag(0,-3,-3)
commutator = arbitrary*Dspec-Dspec*arbitrary
centralizer_solution = s.linsolve(list(commutator), list(arbitrary))
expected_solution = s.FiniteSet((arbitrary[0,0],0,0,0,arbitrary[1,1],arbitrary[1,2],0,arbitrary[2,1],arbitrary[2,2]))
check("General complex commutant is exactly a 1-by-1 plus 2-by-2 block",
      centralizer_solution == expected_solution)
d0, v00, v01, v10, v11 = s.symbols("d0 v00 v01 v10 v11")
block = s.Matrix([[d0,0,0],[0,v00,v01],[0,v10,v11]])
check("Special-unitary condition on the commuting blocks is d0 det(V)=1",
      s.expand(block.det()-d0*(v00*v11-v01*v10)) == 0)
subV = s.Matrix([[v00,v01],[v10,v11]])
check("Unitary block condition separates into |d0|^2=1 and V dagger V=I2",
      zero(block.conjugate().T*block-s.diag(s.conjugate(d0)*d0,subV.conjugate().T*subV)))

# Fixed numerical fixtures for the h-family; no time integration or parameter scan.
Ln = np.asarray(L,dtype=float)
zn = np.array([1.0,1.2*np.exp(1j*np.pi/6),1.4*np.exp(1j*np.pi/3)])
epsilon, coupling, strength = .05,.1,1/7
kn = np.array([1.,2.,3.])


def amplitude_field(v):
    return epsilon*v*(kn-np.abs(v)**2)+coupling*Ln@v


def phase_force(v):
    ph = np.angle(v)
    return np.array([sum(np.sin(3*(ph[j]-ph[i])) for j in range(3) if j != i) for i in range(3)])


def phase_field(v):
    return 1j*strength*v*phase_force(v)


def dA(v,direction):
    return epsilon*((kn-2*np.abs(v)**2)*direction-v**2*np.conjugate(direction))+coupling*Ln@direction


def dB(v,direction):
    ph=np.angle(v)
    dph=np.imag(direction/v)
    df=np.array([sum(3*np.cos(3*(ph[j]-ph[i]))*(dph[j]-dph[i])
                     for j in range(3) if j != i) for i in range(3)])
    return 1j*strength*(direction*phase_force(v)+v*df)


An=amplitude_field(zn)
Bn=phase_field(zn)
F=An+Bn
Cn=-.5*strength**2*zn*phase_force(zn)**2
error_coefficient=dB(zn,An)+Cn-.5*(dA(zn,F)+dB(zn,F))
rows=[]
for step in [.01,.005,.0025,.00125]:
    config=dynamics.DynamicsConfig(step*epsilon,step*coupling,step*strength,tuple(kn))
    actual=dynamics.step3(zn,config)
    intermediate=zn+step*An
    independent=intermediate*np.exp(1j*step*strength*phase_force(intermediate))
    assert np.min(np.abs(intermediate))>.9
    assert near(actual,independent)
    taylor=zn+step*F+.5*step**2*(dA(zn,F)+dB(zn,F))
    residual=(actual-taylor)/step**2
    rows.append({"h":step,"kernel_formula_max_error":float(np.max(np.abs(actual-independent))),
                 "local_Taylor_comparison_error":float(np.linalg.norm(actual-taylor)),
                 "coefficient_error":float(np.linalg.norm(residual-error_coefficient))})
check("Scaled actual kernel step matches independently formed S_h(A_h) at all four fixed h values",
      len(rows)==4 and all(row["kernel_formula_max_error"]<3e-13 for row in rows), "NUMERICAL")
ratios=[rows[i]["local_Taylor_comparison_error"]/rows[i+1]["local_Taylor_comparison_error"] for i in range(3)]
check("Local comparison errors scale quadratically and approach the derived coefficient",
      all(3.9<r<4.1 for r in ratios) and rows[-1]["coefficient_error"] < .003*np.linalg.norm(error_coefficient), "NUMERICAL")
details["splitting_fixture"]={"h_results":rows,"successive_error_ratios":ratios,
    "predicted_error_coefficient_norm":float(np.linalg.norm(error_coefficient)),
    "comparison":"second-order Taylor expansion of the exact flow; not an integrated reference trajectory"}
unit=dynamics.DynamicsConfig(epsilon,coupling,0,tuple(kn))
check("Actual frozen pre-sync step is A_1=I+A on the fixed fixture",
      near(dynamics.step3(zn,unit),zn+An), "NUMERICAL")
singular=np.array([0,1,np.exp(.2j)])
shift_angle=.4
singular_error=float(np.max(np.abs(dynamics.phase_sync(np.exp(1j*shift_angle)*singular,.1)
    -np.exp(1j*shift_angle)*dynamics.phase_sync(singular,.1))))
check("Arg0 zero stratum prevents an unrestricted global-U1 claim for the frozen synchronizer",
      singular_error>.05, "NUMERICAL_COUNTEREXAMPLE")
details["zero_stratum_U1_counterexample_error"]=singular_error

check("All pre-existing repository file bytes and modification times remain unchanged",
      all((sha(ROOT/name),(ROOT/name).stat().st_mtime_ns)==value for name,value in before.items()), "INTEGRITY")
check("Claude original remains unchanged in bytes and modification time",
      sha(CLAUDE_ORIGINAL)==CLAUDE_SHA and CLAUDE_ORIGINAL.stat().st_mtime_ns==original_stat.st_mtime_ns,
      "INTEGRITY")

payload={"baseline":BASELINE,"claude_report_sha256":CLAUDE_SHA,"predicate_count":len(records),
    "passed":sum(r["pass"] for r in records),"failed":sum(not r["pass"] for r in records),
    "runtime":{"python":sys.version.split()[0],"sympy":s.__version__,"numpy":np.__version__},
    "execution_scope":"This script only; read-only geometry/dynamics calls; no old tests, random scans, ODE trajectory integration or historical code.",
    "claude_prior_execution_provenance":"UNRESOLVED: original written assertion and user-reported conversation differ; no inference made.",
    "preexisting_repository_files_protected":len(tracked),"predicates":records,"details":details}
(HERE/'phase_bridge_II_results.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+chr(10),encoding='utf-8')
lines=["PHASE BRIDGE II INDEPENDENT VERIFICATION", "", "Finite predicates are not a theorem count.",
       payload["execution_scope"], ""]
lines += [f'{r["id"]:02d} PASS [{r["kind"]}] {r["name"]}' for r in records]
lines += ["",json.dumps(details,indent=2,ensure_ascii=False),"",
          f'PREDICATES_PASSED = {payload["passed"]}',f'PREDICATES_FAILED = {payload["failed"]}']
output=chr(10).join(lines)+chr(10)
(HERE/'phase_bridge_II_results.txt').write_text(output,encoding='utf-8')
print(output)
