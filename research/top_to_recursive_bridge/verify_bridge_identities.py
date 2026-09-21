"""First geometry-to-state bridge only; no historical or production execution.

Run with the conda torment Python: python -I -S -B -X utf8 this_file.py
Writes results only beside this script. Imports kernel_physics read-only.
Finite predicates supplement the proofs in TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md.
"""

import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
# With -S, load packages without running site startup or .pth hooks.
sys.path.append(str(Path(sys.prefix) / "Lib" / "site-packages"))
sys.path.insert(0, str(ROOT))

import numpy as np
import sympy as s
from kernel_physics import dynamics, geometry


records = []
details = {}


def check(name, predicate, kind="EXACT"):
    result = bool(predicate)
    records.append({"id": len(records) + 1, "name": name,
                    "kind": kind, "pass": result})
    if not result:
        raise AssertionError(name)


def zero(matrix):
    return all(s.simplify(v) == 0 for v in matrix)


def near(a, b, atol=3e-13):
    return np.allclose(a, b, rtol=0, atol=atol)


def cross_matrix(n):
    return s.Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]],
                     [-n[1], n[0], 0]])


manifest = json.loads((HERE / "source_manifest.json").read_text(encoding="utf-8"))
protected = [r for r in manifest["sources"] if r["role"].startswith(
    ("frozen_baseline", "kernel_physics"))]


def unchanged():
    return all(hashlib.sha256(Path(r["path"]).read_bytes()).hexdigest()
               == r["sha256"] for r in protected)


check("Recorded frozen manuscripts and kernel files match initial hashes", unchanged(),
      "PROVENANCE")
I = s.eye(3)
R = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
T = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
module = geometry.folded_module()
centers = [sum((s.Matrix(module.vertices[j]) for j in face), s.zeros(3, 1)) / 8
           for face in module.faces]
check("Actual face centers cycle A=P1 -> B=P2 -> C=P3 under geometric C3",
      all(zero(s.Matrix(geometry.rotate_c3(tuple(centers[i]))) - centers[(i + 1) % 3])
          for i in range(3)))
check("Vertical mirror swaps actual faces A,C and fixes B",
      all(zero(s.Matrix(geometry.reflect_vertical(tuple(centers[i]))) - centers[2-i])
          for i in range(3)))
check("Horizontal mirror fixes each actual face center",
      all(zero(s.Matrix(geometry.reflect_horizontal(tuple(c))) - c) for c in centers))
check("D3 generator relations R^3=T^2=I and TRT=R^-1",
      zero(R**3-I) and zero(T**2-I) and zero(T*R*T-R**2))

u = s.Matrix([1, 1, 1]) / s.sqrt(3)
x = s.Matrix([1, -1, 0]) / s.sqrt(2)
y = s.Matrix([1, 1, -2]) / s.sqrt(6)
U = s.Matrix.hstack(u, x, y)
Pb = u*u.T
Pt = I-Pb
L = s.Matrix(dynamics.L3)
check("Balanced fixed space is exactly one real dimension",
      (R-I).nullspace() == [s.Matrix([1, 1, 1])])
check("Balanced/transverse frame is orthonormal", zero(U.T*U-I))
check("Orthogonal projectors have ranks 1,2 and resolve identity",
      zero(Pb**2-Pb) and zero(Pt**2-Pt) and zero(Pb*Pt)
      and zero(Pb+Pt-I) and Pb.rank() == 1 and Pt.rank() == 2)
check("Balanced projector equals C3 group average", zero(Pb-(I+R+R**2)/3))
check("Actual kernel L3 equals negative three times transverse projector",
      zero(L+3*Pt))
check("Actual face-sharing adjacency has L3 as its unweighted negative Laplacian",
      all(len(set(module.faces[i]) & set(module.faces[j])) == 2
          for i in range(3) for j in range(i+1, 3))
      and zero(s.ones(3)-3*I-L))
variables = s.symbols("m:9")
M = s.Matrix(3, 3, variables)
commutant, _ = s.linear_eq_to_matrix(list(M*R-R*M)+list(M*T-T*M), variables)
check("Full face-permutation commutant has dimension two, spanned by Pb,Pt",
      9-commutant.rank() == 2 and zero(Pb*R-R*Pb) and zero(Pt*T-T*Pt))
skew_commutant, _ = s.linear_eq_to_matrix(
    list(M*R-R*M)+list(M*T-T*M)+list(M+M.T), variables)
check("No nonzero full-D3-equivariant real skew generator on the face channels",
      skew_commutant.rank() == 9)
g = s.symbols("g", real=True)
check("Coupling-only balanced/transverse multipliers are 1 and 1-3g",
      zero(I+g*L-Pb-(1-3*g)*Pt))

omega = (-1+s.I*s.sqrt(3))/2
F = s.Matrix.hstack(*(s.Matrix([1, omega**(-m), omega**(-2*m)])/s.sqrt(3)
                      for m in range(3)))
check("Unitary Fourier basis diagonalizes R with 1,omega,omega^2",
      zero(F.conjugate().T*F-I)
      and zero(R*F-F*s.diag(1, omega, omega**2)))
r = s.Matrix(s.symbols("r0:3", real=True))
c = F.conjugate().T*r
check("Fourier coefficients of a real channel vector obey c0 real,c2=conj(c1)",
      s.simplify(c[0]-s.conjugate(c[0])) == 0
      and s.simplify(c[2]-s.conjugate(c[1])) == 0)
Jt = (R-R**2)/s.sqrt(3)
check("Transverse J is skew, kills u, and squares to -Pt",
      zero(Jt+Jt.T) and zero(Jt*u) and zero(Jt**2+Pt))
check("Transverse J sends x to y and y to -x", zero(Jt*x-y) and zero(Jt*y+x))
check("C3 is the 120-degree sample of an abstract transverse rotation group",
      zero(R-Pb-s.cos(2*s.pi/3)*Pt-s.sin(2*s.pi/3)*Jt))
check("Vertical mirror reverses the transverse complex orientation", zero(T*Jt*T+Jt))
a, b, csk = s.symbols("a b c", real=True)
Kodd = s.Matrix([[0, -a, -b], [a, 0, -csk], [b, csk, 0]])
check("Every real 3-by-3 skew matrix is singular", s.expand(Kodd.det()) == 0)

# Three genuine spatial tangent planes, distinguished from dynamical phase planes.
ez = s.Matrix([0, 0, 1])
normals = [s.Matrix(module.face_normal(i)) for i in range(3)]
frames = [s.Matrix.hstack(ez.cross(n), ez) for n in normals]
J2 = s.Matrix([[0, -1], [1, 0]])
J6 = s.kronecker_product(I, J2)  # interleaved qA,pA,qB,pB,qC,pC
check("Each actual face frame is an oriented orthonormal tangent frame",
      all(zero(B.T*B-s.eye(2)) and zero(B.T*n)
          and zero(B[:, 0].cross(B[:, 1])-n) for B, n in zip(frames, normals)))
check("Outward-normal cross product acts as J2 on each face tangent plane",
      all(zero(cross_matrix(n)*B-B*J2)
          and zero(cross_matrix(n)**2-(n*n.T-I)) for n, B in zip(normals, frames)))
check("Direct sum of the three oriented tangent planes admits orthogonal J6",
      zero(J6.T+J6) and zero(J6**2+s.eye(6)))
Arot = s.Matrix([[-s.Rational(1, 2), -s.sqrt(3)/2, 0],
                 [s.sqrt(3)/2, -s.Rational(1, 2), 0], [0, 0, 1]])
Av = s.diag(-1, 1, 1)
Ah = s.diag(1, 1, -1)


def induced(A, perm):
    result = s.zeros(6)
    for i, j in enumerate(perm):
        result[2*j:2*j+2, 2*i:2*i+2] = frames[j].T*A*frames[i]
    return result.applyfunc(s.simplify)


Rc = induced(Arot, [1, 2, 0])
Tv = induced(Av, [2, 1, 0])
Th = induced(Ah, [0, 1, 2])
check("Geometric C3 permutes tangent complex coefficients without a phase offset",
      zero(Rc-s.kronecker_product(R, s.eye(2))) and zero(Rc*J6-J6*Rc))
check("Horizontal mirror conjugates each tangent coefficient",
      zero(Th-s.kronecker_product(I, s.diag(1, -1))) and zero(Th*J6+J6*Th))
check("Vertical mirror acts as minus conjugation plus A,C swap",
      zero(Tv-s.kronecker_product(T, s.diag(-1, 1))) and zero(Tv*J6+J6*Tv))

# Circulation topology from the existing face complex; no old geometry audit run.
edges = list(module.edges)
d1 = s.zeros(len(module.vertices), len(edges))
d2 = s.zeros(len(edges), len(module.faces))
for k, (v, w) in enumerate(edges):
    d1[v, k], d1[w, k] = -1, 1
for j, face in enumerate(module.faces):
    for v, w in zip(face, face[1:]+face[:1]):
        e = tuple(sorted((v, w)))
        d2[edges.index(e), j] += 1 if (v, w) == e else -1
check("Cellular boundary-of-boundary vanishes", zero(d1*d2))
check("Graph cycle dimension four reduces to shell homology dimension one",
      d1.rank() == 17 and d2.rank() == 3
      and len(edges)-d1.rank() == 4 and len(edges)-d1.rank()-d2.rank() == 1)
z = s.symbols("z", real=True)
check("Right local seam of each panel equals left seam of next panel for every z",
      all(zero(s.Matrix(geometry.panel_point(i+1, s.Rational(1, 2), z))
               -s.Matrix(geometry.panel_point((i+1) % 3+1, -s.Rational(1, 2), z)))
          for i in range(3)))
theta = s.symbols("theta", real=True)
check("Opposite first-harmonic perimeter traces have cos-minus,sin-plus signs",
      s.trigsimp(s.cos(s.pi-theta)+s.cos(theta)) == 0
      and s.trigsimp(s.sin(s.pi-theta)-s.sin(theta)) == 0)


def seam_constraints(n):
    result = s.zeros(6)
    for i in range(3):
        j = (i+1) % 3
        result[2*i, 2*i] = 1
        result[2*i, 2*j] = -(-1)**n
        result[2*i+1, 2*i+1] = 1
        result[2*i+1, 2*j+1] = -(-1)**(n+1)
    return result


C1 = seam_constraints(1)
nb = s.Matrix([0, 1, 0, 1, 0, 1])
check("First-harmonic welded scalar continuity leaves one real coefficient",
      C1.rank() == 5 and C1.nullspace() == [nb])
check("First-harmonic continuous subspace is not invariant under phase rotation",
      not zero(C1*J6*nb))
C2 = seam_constraints(2)
na = s.Matrix([1, 0, 1, 0, 1, 0])
check("Even-harmonic opposite-edge sign case also leaves one real coefficient",
      C2.rank() == 5 and C2.nullspace() == [na])

# Check exactly the hypothesis distinction needed from secondary source section 13.
Kmix = s.diag(J2, 2*J2)
v = s.Matrix([1, 0, 1, 0])
check("Spanning invariant phase planes need not have a common phase frequency",
      zero(Kmix+Kmix.T)
      and zero(Kmix**2-s.diag(-1, -1, -4, -4)))
check("A mixed-frequency vector does not lie in any invariant real two-plane",
      s.Matrix.hstack(v, Kmix*v, Kmix**2*v, Kmix**3*v).rank() == 4)
Jpolar = Kmix*s.diag(1, 1, s.Rational(1, 2), s.Rational(1, 2))
check("Polar normalization supplies complex structure given an invertible skew K",
      zero(Jpolar**2+s.eye(4)) and zero(Jpolar+Jpolar.T))
E6 = s.cos(theta)*s.eye(6)+s.sin(theta)*J6
check("Stated quadrature phase rotations preserve the real norm",
      zero((E6.T*E6-s.eye(6)).applyfunc(s.trigsimp)))
coeffs = s.Matrix(s.symbols("qA pA qB pB qC pC", real=True))
complex_coeffs = s.Matrix([coeffs[2*i]+s.I*coeffs[2*i+1] for i in range(3)])
rotated = J6*coeffs
check("One chosen quadrature per real channel realizes multiplication by i",
      zero(s.Matrix([rotated[2*i]+s.I*rotated[2*i+1] for i in range(3)])
           -s.I*complex_coeffs)
      and s.simplify((complex_coeffs.conjugate().T*complex_coeffs)[0]
                     -coeffs.dot(coeffs)) == 0)

# Short, fixed-state compatibility checks; no trajectories, scans, or atlas.
Rn = np.array(R, dtype=float)
Lnp = np.array(L, dtype=float)
Pbnp, Ptnp = np.array(Pb, dtype=float), np.array(Pt, dtype=float)
state = np.array([1+.3j, -.4+.9j, .7-.2j])
conf = dynamics.DynamicsConfig(eps=0, g=.2, phase_strength=0, k=(1, 1, 1))
check("Read-only kernel coupling agrees with balanced/transverse split",
      near(dynamics.step3(state, conf), Pbnp@state+.4*Ptnp@state), "NUMERICAL")
conf = dynamics.DynamicsConfig(eps=.04, g=.1, phase_strength=.07, k=(1, 1, 1))
check("Equal-k full reference map respects C3 on a fixed nonsingular state",
      near(dynamics.step3(Rn@state, conf), Rn@dynamics.step3(state, conf)), "NUMERICAL")
check("Phase synchronizer preserves the already-supplied amplitudes",
      near(np.abs(dynamics.phase_sync(state, .17)), np.abs(state)), "NUMERICAL")
check("Zero-strength synchronizer takes the exact identity branch",
      np.array_equal(dynamics.phase_sync(state, 0), state), "NUMERICAL")
cycle_state = np.exp(2j*np.pi*np.arange(3)/3)
check("In-phase and 120-degree phase patterns both have zero sync increment",
      near(dynamics.phase_sync(np.ones(3, dtype=complex), .2), np.ones(3))
      and near(dynamics.phase_sync(cycle_state, .2), cycle_state), "NUMERICAL")
check("120-degree Fourier state is transverse, not the balanced mode",
      near(Pbnp@cycle_state, np.zeros(3)) and near(Ptnp@cycle_state, cycle_state), "NUMERICAL")
psi = .4
check("Common phase equivariance holds at a fixed nonzero synchronizer state",
      near(dynamics.phase_sync(np.exp(1j*psi)*state, .1),
           np.exp(1j*psi)*dynamics.phase_sync(state, .1)), "NUMERICAL")
zero_state = np.array([0, 1, np.exp(.2j)])
zero_error = float(np.max(np.abs(
    dynamics.phase_sync(np.exp(1j*psi)*zero_state, .1)
    -np.exp(1j*psi)*dynamics.phase_sync(zero_state, .1))))
check("Arg0 singular stratum does not supply global U1 equivariance",
      zero_error > .05, "NUMERICAL_COUNTEREXAMPLE")
details["zero_stratum_equivariance_error"] = zero_error
unequal = dynamics.DynamicsConfig(eps=.04, g=.1, phase_strength=.07, k=(1, 2, 3))
unequal_error = float(np.max(np.abs(
    dynamics.step3(Rn@state, unequal)-Rn@dynamics.step3(state, unequal))))
check("Fixed unequal amplitude coefficients need not preserve geometric C3 symmetry",
      unequal_error > .01, "NUMERICAL_COUNTEREXAMPLE")
details["unequal_k_C3_error"] = unequal_error

# Analytic checks of the nature of the increment, not a new stability analysis.
qs = s.Matrix(s.symbols("q0:3", real=True))
ps = s.Matrix(s.symbols("p0:3", real=True))
ks = s.symbols("k0:3", real=True)
eps = s.symbols("eps", real=True)
energy = eps*sum((qs[i]**2+ps[i]**2)**2/4
                 -ks[i]*(qs[i]**2+ps[i]**2)/2 for i in range(3))
energy += g*sum((qs[i]-qs[j])**2+(ps[i]-ps[j])**2
                for i in range(3) for j in range(i+1, 3))/2
gradq = s.Matrix([s.diff(energy, qi) for qi in qs])
gradp = s.Matrix([s.diff(energy, pi) for pi in ps])
incq = s.Matrix([eps*qs[i]*(ks[i]-qs[i]**2-ps[i]**2) for i in range(3)])+g*L*qs
incp = s.Matrix([eps*ps[i]*(ks[i]-qs[i]**2-ps[i]**2) for i in range(3)])+g*L*ps
check("Paper-A pre-sync increment is a real negative gradient",
      zero(gradq+incq) and zero(gradp+incp))
ph = s.symbols("phi0:3", real=True)
phase_potential = sum(s.cos(3*(ph[j]-ph[i]))/3
                      for i in range(3) for j in range(i+1, 3))
sync_force = s.Matrix([sum(s.sin(3*(ph[j]-ph[i])) for j in range(3) if j != i)
                       for i in range(3)])
check("Harmonic-3 increment is a phase gradient with zero summed increment",
      zero(s.Matrix([s.diff(phase_potential, p) for p in ph])-sync_force)
      and s.simplify(sum(sync_force)) == 0)
check("Recorded frozen manuscripts and kernel files remain unchanged", unchanged(),
      "PROVENANCE")

details.update({"face_order": ["P1", "P2", "P3"],
                "face_centers": [str(v.T) for v in centers],
                "face_normals": [str(v.T) for v in normals],
                "cell_boundary_ranks": [d1.rank(), d2.rank()],
                "first_harmonic_continuity_rank": C1.rank(),
                "python": sys.version.split()[0], "sympy": s.__version__,
                "numpy": np.__version__, "protected_hash_record_count": len(protected)})
payload = {"scope": "First bridge only; conditional models are explicitly labelled",
           "predicate_count": len(records), "passed": sum(r["pass"] for r in records),
           "failed": sum(not r["pass"] for r in records), "predicates": records,
           "details": details}
(HERE / "bridge_symbolic_results.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
lines = ["GEOMETRY TO STATE: FIRST-BRIDGE VERIFICATION", "",
         "Predicates supplement analytic proofs; this is not a theorem count.",
         "No kernel changes; no historical execution; no trajectories or scans.", ""]
lines += [f'{r["id"]:02d} PASS [{r["kind"]}] {r["name"]}' for r in records]
lines += ["", json.dumps(details, indent=2, ensure_ascii=False), "",
          f'PREDICATES_PASSED = {payload["passed"]}',
          f'PREDICATES_FAILED = {payload["failed"]}']
output = "\n".join(lines)+"\n"
(HERE / "bridge_symbolic_results.txt").write_text(output, encoding="utf-8")
print(output)
