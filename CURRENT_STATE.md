# Publication checkpoint - 23 September 2026

Latest local publication editions: [Paper B v0.1.2](papers/PAPER_B/publication/v0.1.2/README.md), [Paper C v1.0.1](papers/PAPER_C/publication/v1.0.1/README.md), and [accepted Paper D v0.1.1](papers/PAPER_D/v0.1.1/README.md). [Paper A](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf) is unchanged.

GPT accepted D's stated scientific scope and approved exactly five B/C scope/citation additions. B/C's preexisting mathematical content, coordinates, proofs, equations and figures are retained. C's publication label v1.0.1 is distinct from its preserved scientific manuscript v0.3.1. [Exact changes, checks, preservation and the combined proposed publication allowlist](papers/publication_updates/20260923_BC_scope/README.md) identify this local checkpoint. D's approved PDF was not rebuilt. No staging, commit, push, release, tag or DOI was performed.

Predecessors remain reachable: [B v0.1.1](papers/PAPER_B/publication/v0.1.1/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.1.pdf), [C v1.0](papers/PAPER_C/publication/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf), [D v0.1](papers/PAPER_D/README.md). The original archive manifests are frozen baseline receipts, not manifests of these later publication additions; use the combined checkpoint manifest for the proposed changes.

The publication clarification does not implement a reference-scaffold placement, restore historical Z/torus behavior or define a physical gap response. The current boundary/SRG preparation and face-state option remain as recorded in their existing implementation records. The older snapshot below retains its dated scope and is not a current claim that subsequent implementation/publication work never occurred.

---

## Earlier repository snapshot (preserved)

# Current scientific state and handoff

Snapshot date: 2026-09-21. Packaging is archival/transfer only.

## Authoritative reading order

1. [Paper C v0.3.1](papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md) supplies the exact local folded shell.
2. [Paper A v0.5.1](papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md) supplies the abstract three-state nonlinear dynamics.
3. [kernel_physics](kernel_physics/README.md) implements those separate mathematical baselines.
4. [First-bridge derivation](research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md) and [unresolved interface assumptions](research/top_to_recursive_bridge/UNRESOLVED_INTERFACE_ASSUMPTIONS.md) identify the frontier.

The publication subfolders also preserve both v1.0 PDFs and their existing
publication Markdown/TeX sources. The frozen research manuscripts retain the
detailed provenance and companion references. Packaging made no scientific edits
and does not supersede any source.

## Frozen status

```ini
PAPER_A = FROZEN
PAPER_C = FROZEN
KERNEL_PHYSICS = CLEAN
KERNEL_TEST_BASELINE = 41 PASSED
FIRST_GEOMETRY_TO_STATE_BRIDGE = COMPLETE
FIRST_BRIDGE_VERIFICATION = 51 / 51 PASSED
KERNEL_MODIFIED_BY_BRIDGE_WORK = NO
```

“Complete” means the scoped first-bridge investigation and its conditional results
are complete. It does not mean the physical/dynamical encoding has been derived.
The 41 tests and 51 predicates are the existing recorded executions, not new
packaging runs; the latter comprise 40 symbolic/combinatorial, 9 numerical
(including 2 expected counterexamples), and 2 preservation predicates.

## Exact results and remaining interface

```ini
GEOMETRY_TO_REAL_THREE_CHANNELS = EXACT
C3_BALANCED_DECOMPOSITION = EXACT
L3_PROJECTOR_IDENTITY = EXACT
THREE_ORIENTED_TANGENT_PLANES = EXACT
TANGENT_SPACE_COMPLEX_STRUCTURE = EXACT_GIVEN_ORIENTATION
GEOMETRY_TO_C3 = CONDITIONAL_KINEMATIC_CONSTRUCTION
THREE_COMPLEX_DYNAMICAL_AMPLITUDES_DERIVED = NO
SCALAR_PERIMETER_SINGLE_HARMONIC_ROUTE = OBSTRUCTED_UNDER_TESTED_ASSUMPTIONS
PHYSICAL_OBSERVABLE = UNRESOLVED
DYNAMICAL_PHASE_GENERATOR = UNRESOLVED
C3_TO_C3xC2_LIFT = DEFERRED
TOP_TO_RECURSION_HANDOFF = DEFERRED
PHYSICAL_ENCODING_READY_FOR_IMPLEMENTATION = NO
```

The exact balanced/transverse identity is

$$ u=\frac{(1,1,1)^T}{\sqrt3}, \qquad P_\perp=I-uu^T, \qquad L_3=-3P_\perp. $$

On each oriented face tangent plane, with outward unit normal $n_i$,

$$ J_i v=n_i\times v, \qquad J_i^2=-I. $$

Here $v$ is tangent, so $n_i\cdot v=0$. The square identity applies to that
two-dimensional plane, not all of ambient three-space. The direct sum of the
three planes admits a geometric identification with $\mathbb C^3$. A physical
observable and dynamical phase generator have not been selected or derived.

The scalar-perimeter obstruction concerns one common Fourier harmonic per
octagon perimeter with scalar continuity imposed along all welded seam edges.
That ansatz leaves one real coefficient. It does not exclude other field types,
interface laws, or mode constructions. The report states the assumptions and
separates analytic proofs from finite checks.

The shell is one local module. No global host, physical rim boundary conditions,
upper/lower complex doubling, or recursive dynamics are defined by this package.
Historical Vesica, quantum, and SRG material is indexed as secondary provenance,
not admitted into the modern kernel.

## Phase Bridge II

```ini
PHASE_BRIDGE_II = INDEPENDENTLY_REVIEWED
PHASE_BRIDGE_II_VERIFICATION = 53 / 53 PASSED

SYMPLECTIC_STRUCTURE = EXACT
HAMILTONIAN_PHASE_FLOW = CONDITIONAL_ON_ISOTROPIC_H_AND_NU
ANTI_SYMPLECTIC_MIRRORS = EXACT

PAPER_A_PRESYNC_EULER_PARENT = EXACT
CONTINUOUS_SPLITTING = CONDITIONAL_SMALL_H_NONZERO_DOMAIN
THIRD_HARMONIC_KURAMOTO_STRUCTURE = VERIFIED_WITH_CORRECTED_CLASSIFICATION

Z_CHIRAL_TRANSFORMATION_LAWS = EXACT
J_EFF_DETERMINED_BY_Z_CHIRAL = NO

L3_U3_CENTRALIZER = U(1) x U(2)
L3_SU3_CENTRALIZER = S(U(1) x U(2))

PHYSICAL_FACE_OBSERVABLE = UNRESOLVED
PHYSICAL_FREQUENCY_SCALE = UNRESOLVED
PHYSICAL_ENCODING_READY_FOR_KERNEL = NO
```

## Phase Bridge III

The [accepted synthesis](research/phase_bridge_III/PHASE_BRIDGE_III_ACCEPTED_RESULTS.md)
governs these scoped research results. The 73 predicates are the recorded
verification, not a new freeze-time execution; physical interpretation remains unresolved.

```ini
PHASE_BRIDGE_III = ACCEPTED_AND_FROZEN
PHASE_BRIDGE_III_VERIFICATION = 73 / 73 PASSED

ACTION_ANGLE = ACCEPTED_EXACT
PAPER_A_POLAR_PARENT = ACCEPTED_EXACT
H1_CANONICAL_EMBEDDING = ACCEPTED_WITH_ASSUMPTION
H1_INTEGRABILITY = ACCEPTED_EXACT_WITH_SCOPE
H1_TRICHOTOMY = ACCEPTED_WITH_SURVIVAL_DOMAIN_QUALIFICATION
COMMUTATOR_RANK_THEOREM = ACCEPTED_EXACT

GENERAL_LOCAL_CLOCK_THRESHOLD = ACCEPTED_EXACT_WITH_HYPOTHESES
120_DEGREE_THRESHOLD = ABS_ALPHA_EQUALS_4_SQRT_14

INVARIANT_MANIFOLDS = ACCEPTED_WITH_ASSUMPTION
ACTION_TRANSFER_BALANCE = ACCEPTED_EXACT

NONLINEAR_POST_THRESHOLD_DESTINATION = NUMERICAL_OBSERVATION
SUBCRITICALITY = UNRESOLVED

LOCAL_CLOCK_CHIRALITY = ACCEPTED_WITH_ASSUMPTION
SPONTANEOUS_CHIRALITY = UNRESOLVED

FIXED_FREQUENCY_SU3_STRUCTURE = ACCEPTED_EXACT
LOCAL_CLOCK_SYMMETRY = ACCEPTED_WITH_ASSUMPTION

KNOWN_OSCILLATOR_EQUIVALENCE = AFFINE_CLOCK_AND_K_ZERO_ONLY
NOVELTY_SCOPE = UNRESOLVED

PHYSICAL_FACE_OBSERVABLE = UNRESOLVED
PHYSICAL_TIME_SCALE = UNRESOLVED
EXTRA_RECURSIVE_STATE = UNRESOLVED
PHYSICAL_INTERPRETATION_READY = NO

READY_TO_MODIFY_KERNEL_PHYSICS = NO
```

## Archival integrity and execution scope

- Every copied scientific artifact is byte-identical to its original. Paths,
  line endings, scientific text, PDFs, and recorded outputs were not transformed.
- SOURCE_MANIFEST.md and archive_manifest.json map repository copies to originals
  and their hashes. SHA256SUMS.txt covers repository files except itself and Git
  internals; the Git commit identifies the checksum file.
- `python -B tools/verify_archive.py` checks this package using only the Python
  standard library. It executes no scientific source or historical code.
- The complete kernel includes its source, tests, pinned requirements, and
  validation records. Local `.venv` packages and bytecode are excluded.
- The copied bridge script still checks absolute original paths from its copied
  source manifest. Its original Windows execution command and imports are
  preserved. It is an archival script, not promised portable on a fresh clone.
  Do not rewrite it or rerun it merely to validate packaging.
- Original scientific documents contain local paths and references to earlier
  work outside this selected archive. Use this handoff's repository-relative
  links and SOURCE_MANIFEST.md to locate included artifacts; excluded historical
  material is identified in supporting_research/INDEX.md.
- Publication build reports and manifests describe their original build trees;
  compiler caches, temporary renders, intermediate AST files, and historical
  execution packages are intentionally not copied. PDFs were not regenerated.

No new license, physical interpretation, second bridge, or production-system
change is introduced by this archival snapshot.
