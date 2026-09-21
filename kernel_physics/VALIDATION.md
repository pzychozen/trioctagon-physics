# kernel_physics v0.1 — K1 validation

Created under C:/TORMENT/TRIOCTAGON_new/kernel_physics after confirming that the
target did not exist. All first-party files and the local dependency environment
were created only inside that new directory.

**Complete suite: 41 passed, 0 failed, 0 errors**, in 2.526 seconds.
The count is unittest methods; divisor pairs, phase shifts and lift states are
fixed subcases within those methods. No random scans, long trajectories, atlas,
tuning or historical tests were run.

**No mathematical mismatch or implementation ambiguity with the selected frozen
Paper A/C definitions was found.** Initial radical-expression canonicalization
issues were corrected in the new implementation, without altering a formula or
the frozen sources. Finite tests support implementation fidelity; they do not
replace either paper's analytic proofs.

NO PHYSICAL COUPLING BETWEEN GEOMETRY AND DYNAMICS IS CLAIMED YET.

## Files created and LOC

15 first-party files; the generated .venv dependency tree is additional
and excluded from the source inventory and LOC.

| Python category | Physical LOC |
|---|---:|
| Implementation (package initializer + three modules) | 345 |
| Tests (initializer + three test files) | 416 |
| Total Python | 761 |

Physical LOC includes blank lines, comments and docstrings. Per-file hashes,
line counts and nonblank/noncomment counts are in validation.json.

| First-party file | Role |
|---|---|
| __init__.py | Package identity/version |
| geometry.py | Exact local panels, welding, topology, normals, section and D3h helpers |
| dynamics.py | Immutable parameters, Arg0, simultaneous synchronization, F3 and F_M |
| covering.py | Exact Delta, P and divisor-domain Q |
| tests/__init__.py | Test-package marker |
| tests/test_geometry.py | 16 geometry tests |
| tests/test_dynamics.py | 15 dynamics tests |
| tests/test_covering.py | 10 covering/lift tests |
| README.md | Short usage, formulas and scope boundary |
| requirements.txt | Pinned numerical/symbolic dependencies |
| .gitignore | Excludes local environment and bytecode |
| baseline_manifest.json | Frozen Paper A/C original hashes, sizes and modification times |
| test_run.txt | Complete final test output |
| validation.json | Machine-readable inventory and validation |
| VALIDATION.md | This report |

## Exact definitions implemented

Paper C v0.3.1 §§2–7,9 and Appendix B:

~~~text
w=1; s=sqrt(2)-1; beta=pi/3
P1_beta(u,z)=(-1/2+(1/2-u)cos(beta), (1/2-u)sin(beta), z)
P2_beta(u,z)=(u,0,z)
P3_beta(u,z)=(1/2-(1/2+u)cos(beta), (1/2+u)sin(beta), z)
~~~

The eight printed local vertices are transformed and welded with exact SymPy
radicals in printed material order. All 18 welded coordinates and three face
cycles match the independent transcription of §4 in the tests. Edge incidence
gives 21 edges, three seams, Euler characteristic zero and two nine-edge loops.
For abs(z)<=s/2, the implemented section is the perimeter of the unit equilateral
triangle. Coordinate-derived normals yield a 120-degree separation and 60-degree
interior dihedral. The three §9 generators preserve vertex, edge and whole-face
sets; their relations produce twelve distinct tested actions. No new proof of
the full-group upper bound is claimed.

Paper A v0.5.1 §§1–3,6:

~~~text
Omega_tilde = Omega + eps*Omega*(k-abs(Omega)^2) + g*L3@Omega
L3 = [[-2,1,1],[1,-2,1],[1,1,-2]]
theta_n = Arg0(Omega_tilde_n); Arg0(0)=0
F_n = abs(Omega_tilde_n)*exp(i*(theta_n
      + lambda*sum_(m~n) sin(3*(theta_m-theta_n))))
Delta_M f(n)=f(n+1)+f(n-1)-2f(n)
P[n,n mod d]=1; Q=P/sqrt(M/d) for d dividing M
~~~

Synchronization is simultaneous and amplitude-preserving; lambda zero takes the
direct identity branch without calling Arg0. Signed complex zeros are explicitly
assigned phase zero. The ring uses periodic neighbors and three-periodic k for
every supported M=3q, including states outside the lifted sector.

Exact SymPy predicates check Delta_M P=P Delta_d and Q* Delta_M Q=Delta_d for
(M,d)=(1,1),(2,1),(2,2),(3,3),(6,3),(8,2),(9,3),(12,3),(12,4),(24,3),
including Q*Q=I. The (12,3) compressed integer form is 4L3.
Non-divisor failures are checked at (5,3),(3,2),(7,4),(2,4); no false inference of
non-invariance at the exceptional (3,2) pair is made.

The numerical nonlinear identity F_M(P Omega)=P F3(Omega) is checked at M=3,6,12,24
on fixed nonzero states, and at M=6,12,24 on zero/pre-sync-zero and lambda-zero
cases, with rtol=atol=2e-14. Dynamics checks include a hand-calculated pre-sync
state, known simultaneous phase increments, deterministic repeats, component
amplitude preservation and the L3 spectrum. The pure ring wrap is independently
checked on a non-three-periodic six-component state.

These are exact mathematical formulas evaluated numerically for the nonlinear
map, not a claim of exact floating-point equality. No state normalization,
independent clock, noise or physical parameter calibration is added.

## Frozen convention and exclusions

Global-phase equivariance is tested where pre-sync components are nonzero, and
at lambda zero including zero components. A fixed witness checks that the
nonzero-lambda zero-phase convention must not be advertised as globally phase
equivariant at all zero-component states. This preserves Paper A's discontinuity
qualification; it is not an ambiguity or a change to the paper.

No historical readouts, central-energy law, six-gap mapping, SRG, RSB, meta-shell,
thermodynamics, magnetic/gravitational coupling, wormholes, color physics or
TORMENT behavior are implemented. No global host, cap, inner field or physical
boundary condition is assigned.

## Reproducibility and preservation

Runtime: Python 3.12.14, NumPy 2.3.5,
SymPy 1.14.0. Added dependencies reside in the new .venv, which reuses
the bundled NumPy installation. A standalone environment can install the pinned
requirements. The suite uses standard-library unittest.

Run from the parent directory containing kernel_physics:

~~~powershell
.\kernel_physics\.venv\Scripts\python.exe -B -m unittest discover -s kernel_physics/tests -v
~~~

Both frozen manuscript contents, sizes and modification times match their
pre-implementation records. The implementation and tests import only the new
package, NumPy, SymPy and standard-library modules. No protected kernel or
production tree was inspected or hashed; no integrity claim requiring such
inspection is implied.

~~~ini
KERNEL_PHYSICS_V0_1_CREATED = YES
PAPER_C_GEOMETRY_IMPLEMENTED = YES
PAPER_A_F3_IMPLEMENTED = YES
CYCLE_COVERING_IMPLEMENTED = YES

TESTS_PASS = YES
TEST_COUNT = 41

HISTORICAL_PDFS_TOUCHED = NO
KERNEL_TO_TOUCHED = NO
KERNEL_NEW_TOUCHED = NO
PRODUCTION_TORMENT_TOUCHED = NO

SPECULATIVE_PHYSICS_ADDED = NO
~~~
