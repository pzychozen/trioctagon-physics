# K2a exact / independent parity validation

**Status: PASS.** Source HEAD `9cf34b207b772639a4a79c2bcb3332d292b4f947`. Conda environment `torment`.

Verification-only publication: 30 new unittest methods. No pre-existing tracked file or local-only test changed. No production repair, tolerance widening, O03 publication, golden fixture, or P5-P8 implementation.

## Validation

- K2a: 30 tests passed.
- Clean isolated tracked suite: 279 tests passed in 183.563 seconds.
- Preserved local-only Option-B suite: 30 tests passed in 0.666 seconds; this does not change support status.
- Detached validation snapshot: `f7a252719283e02a111e47de6a781f74912ed76d`. The eight test/oracle source files match that snapshot byte for byte. Receipts were written after passing validation.
- Every pre-existing tracked file and all four local-only tests were checked against their starting SHA-256 hashes.

```powershell
& 'C:\Users\Notandi\miniconda3\shell\condabin\conda-hook.ps1'
conda activate torment
python -B -m unittest kernel_physics.tests.test_parity_oracle_boundaries kernel_physics.tests.test_parity_p01_p04 kernel_physics.tests.test_parity_p09_p10 kernel_physics.tests.test_parity_p11 -v -f
python -B -m unittest discover -s kernel_physics/tests -t . -p "test_*.py" -v
python -B -m unittest kernel_physics.tests.test_boundary_response kernel_physics.tests.test_srg kernel_physics.tests.test_operating_region kernel_physics.tests.test_boundary_pipeline -v
```

The tracked command ran in the isolated checkout; the local-only command ran afterward in the original working tree. The external K2a receipt collector runs the same four modules with failfast and records bounded aggregates.

## Environment and comparison counts

```json
{
  "python": "3.11.15 | packaged by Anaconda, Inc. | (main, Mar 11 2026, 17:12:15) [MSC v.1942 64 bit (AMD64)]",
  "executable": "C:\\Users\\Notandi\\miniconda3\\envs\\torment\\python.exe",
  "platform": "Windows-10-10.0.26200-SP0",
  "numpy": "2.4.4",
  "sympy": "1.14.0",
  "mpmath": "1.3.0",
  "mpmath_dps": 80
}
```

```json
{
  "HIGH_PRECISION_REFERENCE": 867,
  "EXACT_SYMBOLIC": 3033,
  "EXACT_DISCRETE": 119,
  "BINARY64_TERM_SCALE": 325,
  "HISTORICAL_FIXTURE_TOLERANCE": 2
}
```

Counts are recorded scalar symbolic/numeric comparisons and discrete assertions, not unittest method counts. Historical tolerances are classified separately. Maximum error / allowed bound: **0.065101835882543189081932253394215873**.

## Claims, independent construction and falsifiers

### P1

PASS SUPPORTS: One-step expanded polynomial, simultaneous harmonic-3 synchronization, Arg0 and retained magnitude.

PASS DOES NOT SUPPORT: Multi-step/global behavior, stability or physical interpretation.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: u=2^-52. Phase off: 32u times sum(|w|,|eps*k*w|,|eps*w*|w|^2|,|g*sum(w)|,|3g*w|). Phase on: frozen 64u*|V_j|*(1+|p_j|+|lambda|*(|sin(3Delta1)|+|sin(3Delta2)|)); exact-zero branch explicitly checked.

Fixtures:
- W=(3/8+7i/8,-1/2+i/4,1/8-3i/4); k=(1/2,5/4,3/2)
- eps,g=(1/16,3/16),(-1/32,-1/8); lambda=0,1/4,-1/5; exact zero
- Full-step signed zero: (-0+0i,-1+i,-2+i/2), eps=g=0, lambda=1/4; ordinary-angle and omitted-neighbour mutants
- Spread phases lambda=1/4; sequential/in-place mutant

Falsifiers: sequential phase update = PASS; ordinary-angle signed-zero falsifier = PASS; omitted zero-neighbour falsifier = PASS

### P2

PASS SUPPORTS: Equal-k synchronized scalar reduction, including zero and negative multiplier, with phase off/on.

PASS DOES NOT SUPPORT: Attraction, stability or unequal-k synchronized invariance.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: 32u times the independently expanded pre-sync term sum, including equal-k phase-on fixtures; no absolute floor.

Fixtures:
- w=1/2+i/4,1/2,0 with eps=1/8; w=2 with eps=1; g=1/4,k=(1,1,1),lambda=0,1/4
- Unequal-k witness uses w=1/2+i/4, eps=1/8 and k=(1/2,5/4,3/2)

Falsifiers: unequal k leaves span(e) = PASS

### P3

PASS SUPPORTS: Triad S3 with jointly permuted k, real-parameter conjugation, chirality signs and qualified U(1).

PASS DOES NOT SUPPORT: Ring S3, spatial chirality, or unrestricted phase-on U(1) at pre-sync zeros.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: 128u times independent defining-term scales. Two-runtime-path covariance comparisons sum the scales of both inputs; raw chirality uses the two defining product magnitudes. Phase-on checks additionally use the stricter P1-style multiplicative phase scale.

Fixtures:
- All six permutations of W and unequal k, lambda=0,1/4; fixed-k swap fails
- Conjugation; symbolic rational unit-circle parameterization plus -1; binary rotation .6+.8i
- Pre-sync-zero U(1) counterexample with eps=g=0 and lambda=1/4; chirality raw, conjugated and rotated

Falsifiers: fixed unequal k permutation = PASS; phase-on global U1 false at pre-sync zero = PASS

### P4

PASS SUPPORTS: Exact cycle multiplicity and P/Q domains on stated fixtures; one-step P lifts and off-sector ring wrap.

PASS DOES NOT SUPPORT: Long-time ring/triad closeness, sector attraction or nonlinear Q lifting. M=3 is a self-path sanity fixture.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: 128u times expanded pre-sync addends, including coupling, checked also on captured pre-sync vectors. Phase-on outputs additionally use the P1-style multiplicative phase scale. Two-path P-lift comparisons sum both independent scales; M=3 is self-path only.

Fixtures:
- Cycle sizes 1,2,3,4,5,6,12,24; repeated incidences retained
- Pairs (M,d)=(1,1),(2,1),(2,2),(3,3),(6,3),(12,3),(24,3),(6,2),(3,2),(5,3),(2,3),(1,4)
- P lifts at M=3,6,12,24 with spread, one zero, all zero, lambda=0,1/4, plus unrestricted wrap fixtures
- Q substitution at M=12 with factor 1/2; ring M=4,5 rejection

Falsifiers: (3,2) invariant image is not intertwining = PASS; Q is not nonlinear lifting operator = PASS

### P9

PASS SUPPORTS: Paper E observer identities, literal .01 operation order, constructor distinction and passive updates.

PASS DOES NOT SUPPORT: Physical interpretation of observer constants or mathematical saturation strictly below one in binary64.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: Exact/hand identities and literal bitwise comparisons; retained historical scalar max(2e-14*|reference|,2e-15); macro cone/norm residual <=8u*z^2. No other absolute floor.

Fixtures:
- Hand state (3,4i,0), norm=5, rho=5/6, theta=t=lock=0, amplitude=3, alpha=2,beta=1/2
- Retained mpmath scalar fixtures from test_z_manifold.py; 80-digit references, existing 2e-14 relative/2e-15 absolute rule
- Cubic +/-1, dyadic complex and zero; literal .01 fixture (1,1,i), J=1,j=1/2,m=0; old m=-1/2,1/4,1
- Marked constructor zeros versus nonzero recomputation; eight-update API trajectories with both observers and all five diagnostics

Falsifiers: constructor zero differs from recomputed row zero = PASS; literal .01 differs from 1-.99 = PASS

### P10

PASS SUPPORTS: Exact accounting/gradient identities, bounded residuals, passive diagnostics and qualified displays.

PASS DOES NOT SUPPORT: Finite-step Lyapunov descent, trajectory validity, physical state or history-independent displays.

Oracle: independent exact SymPy/discrete reconstruction and 80-digit mpmath where numeric.

Bound: 256u times the independently reconstructed sum of absolute defining terms; exact-zero branches have bound zero. No residual clipping or universal epsilon.

Fixtures:
- Symbolic six-real-coordinate norm/Q/Gram/slack/gradient/intensity identities
- Dyadic, near-collinear (1+i,1+i,1+(1+2^-26)i), and zero states; exact independent negative-gradient budget
- Consistent signed and deliberately inconsistent supplied readouts; potential overshoot (2,2,2)->(-4,-4,-4), 6->168
- Alignment at .5e-12,1e-12,2e-12; detached direct display; hand cylinder; one- and two-row history torus; scalar-display information loss

Falsifiers: unresolved is not exact zero = PASS; extended history moves an old point = PASS; scalar display loses chirality = PASS; negative gradient is not finite-step descent = PASS; nonzero rounded Gram residual not clamped = PASS; inconsistent records retained = PASS

### P11

PASS SUPPORTS: Exact C coordinates/topology/sections and existing D3h actions; exact D sets, frames, roles and constructions.

PASS DOES NOT SUPPORT: Any Omega-to-geometry mapping, a new symmetry engine, or new geometry definitions.

Oracle: printed tables and exact symbolic identities.

Bound: Exact SymPy symbolic/discrete comparison only, no floating approximation or rationalization.

Fixtures:
- Printed C 18 coordinates, 21 edges, three oriented faces, seams and two nine-edge loops; normals/dihedrals
- Central heights -s/2,0,s/4,s/2 and outside/complex/unknown domain rejection; known generator permutations and twelve actions
- D symbolic positive s,gap; exact octagon, shoelace area, circumradii; s=2,gap=1 closed sets/support/corners
- Complete frames s=3/2,gap=5/4; regular s=2 actions/roles; canonical C member s=sqrt(2)-1 translation and shrink
- Substitution-first 1/(1+sqrt(x)), positive x specialized at 1, in side/gap/full frames/support; float rejection

Falsifiers: section is not filled cap h=1/2 - sqrt(2)/2 = PASS; section is not filled cap h=0 = PASS; section is not filled cap h=-1/4 + sqrt(2)/4 = PASS; section is not filled cap h=-1/2 + sqrt(2)/2 = PASS; closed region differs from open-corner subtraction = PASS; unmarked D6 does not preserve E/G roles = PASS; complete frames do not acquire D6 = PASS; translations are not one common rigid translation = PASS; translation differs from fixed-centre shrink = PASS

### ORACLE_IMPORT_BOUNDARY

PASS SUPPORTS: All four oracle modules obey the explicit import whitelist and simple dynamic-loader exclusions.

PASS DOES NOT SUPPORT: A general Python sandbox or proof of the mathematical definitions.

Oracle: static AST inspection.

Bound: Exact AST allowlist and explicit escape exclusions.

Fixtures:
- Every *.py in parity_oracles, including __init__.py; AST import/relative import/dynamic-load checks

Falsifiers: None applicable; explicit exact/discrete checks.

## Worst normalized numerical cases

| Gate | Quantity / fixture | Absolute error | Scale | Allowed bound | Error / bound |
|---|---|---:|---:|---:|---:|
| P1 | component[2]; direct phase 0.25 | 2.029728523146616989930927342324176e-16 | 2.0763662622664205264724616524417446 | 2.9506939288615122428502412112177134e-14 | 0.0068788175665842846270850522157706073 |
| P2 | component[0]; negative multiplier lambda=0.25 | 4.8985871965894128286950561178335864e-16 | 15.0 | 1.0658141036401502788066864013671875e-13 | 0.0045960990569170754686349293175832524 |
| P3 | component[2]; chirality rotation | 5.5511151231257827021181583404541016e-17 | 0.53125000000000005551115123125782702 | 1.5099033134902130527483201128058767e-14 | 0.0036764705882352937334868426902572926 |
| P4 | component[20]; off-sector periodic wrap m=24 | 2.0855739416187324462044741013139605e-16 | 0.91249635475539357422701746105377878 | 2.5934706251160650203559540075667052e-14 | 0.008041633174562743367854417536357382 |
| P9 | component[1]; macro 8u residual fixture 0 | 5.7740785351711684392796637634185787e-20 | 0.00049929732370223688159220204946908123 | 8.869302158527092700385488823206281e-19 | 0.065101835882543189081932253394215873 |
| P10 | component[0]; history torus length=2 point=1 | 3.0536716407953272774938525140651829e-16 | 1.0000000002617993876682497589827961 | 5.6843418875689587120419318977314792e-14 | 0.0053720759609364403023305878808716354 |

P11 is entirely exact. Numeric scales are reconstructed before runtime discrepancies are inspected. The JSON retains the runtime/reference values for each worst normalized case.

## Independence and preservation

- `kernel_physics/tests/parity_oracles/__init__.py`: no imports
- `kernel_physics/tests/parity_oracles/geometry_oracle.py`: collections, sympy
- `kernel_physics/tests/parity_oracles/paper_a_oracle.py`: mpmath, sympy
- `kernel_physics/tests/parity_oracles/paper_e_oracle.py`: mpmath, sympy

The oracle AST gate rejects forbidden/relative imports and obvious dynamic import/exec routes. No oracle imports the kernel, research, accepted-paper implementation, or Paper-F verifier. Numeric Paper E increments are obtained independently by differentiating the six-real potential. Paper C uses printed coordinates and independently known vertex permutations; the twelve actions compose only the existing runtime generators.

Pre-existing production/tests/papers/research/K0/K1/Option-B changes: **0**. O03 published: **NO**. The accepted degree-sensitive numeric domain tests remain unchanged and passed in the full tracked suite.

## Nonblocking numerical observations

- Negative synchronized multiplier with lambda=.25 reconstructs -4+4.898587196589413e-16j, within the original 32u bound.
- Near-collinear Gram residual remains nonzero and unclamped.
- Literal .01*(1/2) differs bitwise from (1-.99)*(1/2).
- Extending the history torus changes an earlier point.
- No frozen mathematical tolerance failed or was widened.

## Exact new-file list

- `kernel_physics/K2A_EXACT_INDEPENDENT_PARITY_VALIDATION.json`
- `kernel_physics/K2A_EXACT_INDEPENDENT_PARITY_VALIDATION.md`
- `kernel_physics/tests/parity_oracles/__init__.py`
- `kernel_physics/tests/parity_oracles/geometry_oracle.py`
- `kernel_physics/tests/parity_oracles/paper_a_oracle.py`
- `kernel_physics/tests/parity_oracles/paper_e_oracle.py`
- `kernel_physics/tests/test_parity_oracle_boundaries.py`
- `kernel_physics/tests/test_parity_p01_p04.py`
- `kernel_physics/tests/test_parity_p09_p10.py`
- `kernel_physics/tests/test_parity_p11.py`

K2b is ready for a separate authorization. Its proposed starting HEAD is the publication commit containing this receipt, to be reported after the normal fast-forward push.
