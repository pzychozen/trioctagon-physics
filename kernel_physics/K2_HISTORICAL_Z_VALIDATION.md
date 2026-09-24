# K2 historical Z observer: implementation and validation

Task: MK-K2_HISTORICAL_Z_OBSERVER_v0.1. Prepared by Codex, 24 September 2026.
**GPT implementation review: pending. Claude implementation review: not performed.**

The optional module implements the staged K exponential-envelope observer first,
then the separately named H committed-EMA observer. Both are downstream readouts
of supplied Omega. No new recurrence, feedback path or geometric registration is
introduced. The source equations are recovered definitions; the proofs below are
the accepted Paper-E mathematics and its explicit implementation reasoning.

## Authority, baseline and bounded scope

Authoritative checkout:
C:\TORMENT\TRIOCTAGON_new\trioctagon-physics.
Source target: its kernel_physics package. Interpreter only:
C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe.

STARTING_HEAD and FINAL_HEAD are both
2b336f247aa2c24cd7596a1fc733a7b948fdb840, on main; its parent is
c60e4cfa9b3e5247f522a6036657c4d6fac75da1.
Entry tracked worktree/index were clean. The existing four local-only predecessor
test files remain unchanged and unstaged. Current K1 acceptance is established
by the published commit and the supplied GPT identity review; preserved pending
text inside K1 artifacts is not treated as current review status.

This task reads local pinned blobs, without a new remote/publication operation.
GPT's supplied K1 identity review did not independently rerun the Windows
checkpoint suites; those older runs remain Codex-attributed. This K2 report
contains fresh Codex Windows measurements, not GPT or Claude acceptance.

Seven controlling inputs were verified both by BASE Git blob ID and by local
byte equality to that blob before use:

| Input | Verified Git blob | Raw SHA-256 |
|---|---|---|
| papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md | 137fb77e0b7d5021d8de1987effd16d70280278a | a79bc29d991c3af8bba546f0bc5e1ff7a6bbe5501d8adf2ef6d19c66b362978d |
| papers/PAPER_E/evidence/source_snapshots/staged/model_core.py | 5db0dce7de4e3fb55084a4ae638d539b94d36db9 | ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6 |
| papers/PAPER_E/evidence/source_snapshots/committed_ema/model_core.py | 469b8df958f8c2f005395a205471fa0307b3ef7b | cd173dd818bd20983e23a72c2195b513eb3d72ae0446db8239c65657fd7d17b2 |
| papers/PAPER_E/evidence/source_snapshots/staged/phase_triad_sync.py | 924559d9cbda217cdd7f02082fb143c9cd2d0e26 | 15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6 |
| kernel_physics/readouts.py | aed43915b9d74e0ae6c0394ebad8960736565e31 | 3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9 |
| kernel_physics/_response_numeric.py | b38ad67f9c2352e055a4a8eaefbf928747c29afb | cc33f797e76f7dbeff6fbd58ab52003fde2acbadf35ae299d827b4b55ba29655 |
| kernel_physics/dynamics.py | 4283c9929fa8b0df18234a23ea9adf4ebce98510 | ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4 |

Paper E v0.1.1 sections 3-9 and 19-20 control equations (1), (2), (39), (40),
constructor rows and recording order. The phase helper was read only for its
compatibility boundary. No historical package was imported. The two extracted
update_z bodies and their harness are retained in the JSON, not installed.

Exactly five persistent output paths are authorized: z_manifold.py,
tests/test_z_manifold.py, K2_HISTORICAL_Z_VALIDATION.md,
K2_HISTORICAL_Z_VALIDATION.json and README.md, all under kernel_physics.
No initializer, dependency, existing test or protected module was changed.

## Complete proposed API

Signatures below are captured from the actual implementation. Names are in
kernel_physics.z_manifold; required configuration arguments make law selection
explicit. Arrays are detached and read-only against ordinary mutation; these
flags are not a security boundary.

| Name | Actual signature | Source line |
|---|---|---|
| Clock | (q: int = 0, N: int = 12, t: float = 0.0, q_step: int = 1) -> None | 46 |
| StagedConfig | (lambda_vp: float = 0.618, gamma: float = 0.577, theta_lock: float = 0.244, alpha: float = 1.0, beta: float = 0.5) -> None | 90 |
| EMAConfig | (lambda_vp: float = 0.618, theta_lock: float = 0.244, alpha: float = 1.0, beta: float = 0.5) -> None | 202 |
| EMAState | (m: float = 0.0) -> None | 214 |
| ZReadout | (z: float, Z_macro: numpy.ndarray, Z_chiral: numpy.ndarray, Z_total: numpy.ndarray, variant: str, initialization: str = 'recomputed') -> None | 164 |
| ConstructorZeroRecord | (omega: numpy.ndarray, clock: kernel_physics.z_manifold.Clock, config: kernel_physics.z_manifold.StagedConfig \| kernel_physics.z_manifold.EMAConfig) -> None | 268 |
| clock_angle | (clock) | 66 |
| advance_clock | (clock, dt) | 75 |
| state_norm | (omega) | 103 |
| saturated_norm | (omega) | 110 |
| staged_scalar | (omega, clock, config) | 127 |
| macro_vector | (z, clock) | 145 |
| blend_vectors | (macro, chiral, *, alpha, beta) | 153 |
| observe_staged | (omega, clock, config) | 197 |
| cubic_j | (omega) | 226 |
| normalized_cubic | (omega) | 233 |
| advance_ema | (omega, memory) | 240 |
| ema_scalar | (omega, clock, config, memory) | 254 |
| observe_ema | (omega, clock, config, memory) | 262 |
| historical_constructor_zero | (omega, clock, config) | 295 |

ZReadout additionally exposes the read-only Z_vec property as an alias of
Z_total, not another independently stored state. ConstructorZeroRecord contains
validated omega, clock and config, plus initialized memory=EMAState(0) and a
marked zero readout. It has no step method.

StagedConfig contains literal lambda_vp=0.618, gamma=0.577, theta_lock=0.244,
alpha=1, beta=0.5. EMAConfig has the same harmonic/blend defaults but no gamma.
No algebraic golden-ratio replacement or geometry-derived coefficients are used.
The historical memory coefficient is fixed locally as tau_meta=0.01, with
retention computed as 1.0-tau_meta, exactly as the source expression orders it.

Clock holds integer q, N and q_step, rejecting booleans; N must be positive.
Angle evaluation reduces q modulo N using integers, then evaluates
2*pi*((q mod N)/N) in binary64. q itself retains the supplied integer until
advance_clock returns (q+q_step) mod N. dt is a required explicit argument,
not a recurrence parameter. N=12 and q_step=1 are the named historical defaults.

## Equations, implementation and independent checks

| Source / equation | Implementation | Independent test methods / evidence |
|---|---|---|
| E (1): kappa, rho, sector angle | state_norm, saturated_norm, Clock, clock_angle | ClockTests; stable_small_large_norm_and_raw_scale; saturation_rounding_to_endpoints_is_allowed |
| K update_z; E (2): staged scalar | StagedConfig, staged_scalar, observe_staged | literal_defaults; hand_state_and_direct_chirality_delegation; signed_coefficients_gamma_zero_and_envelope; fixed_high_precision_scalar_oracle |
| E (2), (8): macro and blend | macro_vector, blend_vectors, ZReadout | exact_macro_cone_and_norm; alpha_beta_selection_and_alias; common_state_exact_total_cancellation |
| E (13): C and cyclic ordering | sole runtime calculation remains readouts.z_chiral | exact_cross_product_order; direct delegation spy and exact hand C=(-3,6,-3) |
| H update_z; E (15), (39): cubic and one update | cubic_j, normalized_cubic, advance_ema | common_phase_counterexample_and_first_update; mixed_signed_cubic_hand_values; one_two_updates_against_exact_rationals |
| E (39)-(40): current memory / bounded profile | EMAState, ema_scalar, observe_ema | endpoint_memories_and_invalid_domain; pure_observation_does_not_consume_memory; zero_omega_retains_memory; exact_ema_unrolling_weights_and_persistent_input |
| E 3.3: constructor and pre-step rows | historical_constructor_zero; explicit external loops | InitializationTests; separately executed README example |
| E 3.2-3.3: no feedback | no dynamics/geometry dependency in observer | clean_process_import_boundary; observers_leave_same_recurrence_trajectory_exactly_unchanged |
| Existing strict numeric contract | unchanged _response_numeric helpers | PrecisionTests; clock_range_and_stagnation_failures; full decomposition delegation failure |
| Actual source update_z bodies | read-only AST extraction, separate temporary harness | six fixed fixtures per variant; all fields recorded in JSON |

Test method names above are suffixes of test_z_manifold class-qualified IDs.
The full IDs, successes and outputs are retained in the companion. Unit tests
require only the package and existing dependencies; they read no papers, Git
metadata, source snapshot tree or private sibling source.

### 1. Macro cone and norm

For any finite real z and theta, M=z(cos(theta),sin(theta),1). Therefore
M1^2+M2^2-M3^2=z^2(cos(theta)^2+sin(theta)^2-1)=0 and
||M||^2=z^2(cos(theta)^2+sin(theta)^2+1)=2*z^2.
These are exact identities for M, including the EMA macro and z=0. They do not
hold automatically for arbitrary T=alpha*M+beta*C. Exact symbolic checks use
SymPy; floating residual checks use 8*machine_epsilon*z^2, not an exact-zero claim.

### 2. Frozen third-harmonic extrema and sampling

For f(theta)=A*cos(3*(theta-ell)), with amplitude A held constant,
f'=-3*A*sin(3*(theta-ell)) and f''=-9*A*cos(3*(theta-ell)).
If A is nonzero, all critical angles are theta=ell+k*pi/3; there are six residues
in a full turn. f=A*(-1)^k and f''=-9*A*(-1)^k there. For A>0, even k give
maxima and odd k minima; for A<0 the labels reverse. For A=0 the function is
constant and there are no six isolated extrema. For H with memory frozen, adding
m changes the levels but not these critical angles; it need not leave three
positive and three negative heights.

At N=12, theta_q=pi*q/6 hits an extremum exactly when
pi*q/2-3*ell is an integer multiple of pi. This is equivalent to
ell in (pi/6)Z. The nonzero rational default 0.244 is not such a multiple.
The sampled sequence is (c,s,-c,-s) repeated three times,
c=cos(3*ell), s=sin(3*ell), not exact continuous extrema. These statements hold
for frozen amplitude; evolving kappa, time and memory do not inherit fixed
temporal extrema. No physical D24 group label is assigned to the clock.

### 3. Channel-area identity and distinct cubic J

Writing Oj=xj+i*yj gives
conj(Oj)*Ok=(xj*xk+yj*yk)+i*(xj*yk-yj*xk).
C therefore lists (x2*y3-x3*y2, x3*y1-x1*y3, x1*y2-x2*y1)=x cross y,
ordered (BC,CA,AB). The runtime does not copy that formula: it delegates to the
existing checked readouts.z_chiral. Raw C has no imposed decay envelope; it need
not decay.

The scalar J=Im(O1*conj(O2)*O3) is cubic, and its product acquires e^(i*chi)
under a common phase. For Omega=(1,1,1) and (i,i,i), C=0 in both while J=0 and
J=1 respectively. The latter gives j=1/2 and first memory 0.005 from zero.
This disproves a general common-phase invariance claim for the H memory input.

### 4. Exact bounded-memory reasoning

Let a=99/100 and j_k=J_k/(1+|J_k|). Iterating
m_n=a*m_(n-1)+(1-a)*j_n proves by induction
m_n=a^n*m_0+(1-a)*sum(k=1..n, a^(n-k)*j_k).
The induction substitutes the n formula into the next update and appends j_(n+1).
All weights are nonnegative and sum to
a^n+(1-a)*(1-a^n)/(1-a)=1. With |m_0|<=1 and finite J_k, |j_k|<1,
so |m_n|<=1 exactly. This is the adopted bounded historical profile, enforced
on initial EMAState values without clipping. Constant nonzero j_* gives
m_n=a^n*m_0+(1-a^n)*j_* and tends to j_*, not generally to zero.

This exact proof is not a certificate for all binary64 intermediates.
Floating saturation may round j to +/-1 or rho to 1; such rounded endpoints
are accepted. The memory bound does not bound T independently of Omega because
C is quadratic and raw Omega is not normalized.

### 5. Observer independence

The existing step3 reads only its supplied Omega and DynamicsConfig. K2 imports
neither dynamics nor any geometry and returns new clock/memory/readout values.
For two runs with equal initial Omega and identical recurrence configuration,
the next Omega is the same function of the same input. Induction establishes
equal trajectories at every subsequent step, regardless of observer coefficients,
clock or memory. The test separately compares exact stored arrays across five
updates with staged/EMA observers, different dt, signed weights and both
phase_strength=0 and 0.001. It invokes the same existing step3, not a copy.
This is an implementation equality for identical stored inputs and operations;
it is not complete historical-source trajectory parity.

## Update ownership, initialization and examples

A staged observation evaluates only K; an EMA observation uses current memory
and does not evaluate J or advance memory. advance_ema computes J and performs
one update, returning a new immutable state. An H post-update observation uses
that returned state once. Repeating an observation changes nothing.

The historical constructor factory validates finite complex shape-(3,) Omega,
Clock and the explicitly named configuration, then returns zero z/M/C/T and
zero memory with initialization=historical_constructor_zero. It deliberately does
not compute kappa, J or C. For the nonzero hand state, a separate modern observation
returns actual C=(-3,6,-3); the constructor-zero convention is not a formula.

The README's new backtick-fenced example records n=3 current rows, then calls
step3, advance_clock, staged observation, advance_ema once and EMA observation.
It records all initial Omega, recurrence parameters, observer parameters,
clock fields, initial memory, tau_meta, dt and sampling/initialization metadata.
Rows 0,1,2 are pre-step rows; the final step-3 state lies outside history.
The complete executed example, metadata and three output rows are in JSON.
The prior tilde-fenced Python pipeline is byte-for-byte unchanged.

Minimal selection examples:

~~~python
from kernel_physics.z_manifold import (
    Clock, StagedConfig, EMAConfig, EMAState,
    observe_staged, advance_ema, observe_ema,
)
omega = (1+4j, 2+5j, 3+6j)
clock = Clock(q=0, N=12, t=1, q_step=1)
k = observe_staged(omega, clock, StagedConfig())
next_memory = advance_ema(omega, EMAState(m=0))
h = observe_ema(omega, clock, EMAConfig(), next_memory)
# h again with the same inputs is the same readout, not another memory update.
~~~

## Numerical contract and limits

1. Input vectors require shape (3,) and finite numeric complex components;
   strings/booleans/nonfinite values are rejected. Real scalars reject complex
   values, strings, booleans and arrays. Validation precedes zero products.
   Config/state objects are frozen; output vectors are detached and read-only.
2. state_norm uses math.hypot on six real components. Representable normal norms
   at 1e-200 and 1e200 are preserved rather than squared away or overflowed.
   A genuinely unrepresentable norm, or nonzero subnormal checked norm, raises.
   This does not normalize the supplied Omega or clip its raw scale.
3. Products use existing checked product/complex_product helpers, sums use
   existing math.fsum-based total. Cubic multiplication is left-associated
   (O1*conj(O2))*O3. Zero-valued real product operands can short-circuit only
   after input validation; other underflowing products are not replaced by zero.
   Near cancellation, neither a computed small value nor zero certifies exact
   algebraic cancellation or relative accuracy.
4. Scalar evaluation uses lambda_vp*rho, then cosine, then exp(-gamma*t) for K.
   Harmonic subtraction and multiplication by three are checked; cosine is
   evaluated in binary64. The exp argument, overflow, underflow-to-zero and
   subnormal result are checked explicitly. Even zero scalar amplitude does not
   bypass envelope evaluation. No high-precision runtime fallback is introduced.
5. J, scalar, C and blend have different stage limits. The pure H readout can
   succeed where its separate cubic update would fail. beta=0 never suppresses
   delegated C computation in a full readout. Overflowing weighted terms fail
   before any attempted cancellation; tiny nonzero checked products fail
   conservatively. Failure leaves previous Omega, config, clock and memory intact.
6. Clock time addition must remain finite; a nonzero requested dt with
   t_next==t raises explicitly. Very fine sector fractions beyond the normal
   binary64 domain also fail rather than silently claiming zero angle.
   q is handled as an integer, including the tested 400-digit periodic index.
7. Exact finite rho<1 and |j|<1 are mathematical statements, not strict
   machine-interior certificates. Rounded endpoints are valid. No arbitrary
   tolerance changes the formula or state. There is no universal all-finite-input
   machine-safety, exact phase-reduction or cross-platform bitwise certificate.
8. With gamma>0 and t increasing to positive infinity the exact K envelope tends
   to zero; finite-time numerical underflow is rejected, not interpreted as a
   physical zero. Signed gamma/time are allowed. C has no imposed decay envelope.
   H contains no gamma and does not inherit that envelope.

The mathematical exact cancellations in tests are deliberately constructed.
For Omega=(1,i,-1), C=(1,0,1); at q=0, lambda_vp=0 and current m=1,
M=(1,0,1). alpha=1,beta=-1 gives T=0 with nonzero Omega and nonzero macro/C.
It does not make zero total a zero-state diagnostic or an energy law.

## Source-body parity and compatibility boundary

Only the exact pinned AST update_z method from each historical model_core was
compiled. The annotation name ModelState was supplied as SimpleNamespace;
dummy self.p/state fields and historical kappa=np.linalg.norm were provided.
No expression in either body was replaced, and no unrelated historical method
or runtime package was imported.

Six fixtures per variant cover the hand state, a mixed state and its conjugate,
common imaginary channels, zero Omega with nonzero memory, and a lock override.
They use positive/negative coefficients, varied N/q/time, gamma=0 and signed gamma.
The JSON records source hashes/line spans/executed bodies, every parameter,
Omega, before/after memory, z/M/C/T, actual differences and harness source.
The H comparison performs precisely one modern advance_ema followed by
observe_ema. Source and modern outputs agree within rtol=2e-14, atol=2e-15;
the largest observed field difference in these fixtures is 0.0.

This is a bounded same-state comparison, not a parameter sweep or proof of
all-input numerical identity. The historical phase helper uses np.angle's
signed-zero extension; modern arg0 is preserved. No phase-enabled historical
trajectory parity is claimed. Such a claim would require nonzero relevant
pre-sync components and appropriate tolerance. No saved spike dataset was replayed.

## Actual execution and preserved development history

| Record | Suite | Methods | Result | Failures/errors/skips | Seconds |
|---|---|---:|---|---|---:|
| 01_baseline.json | baseline | 134 | PASS | 0/0/0 | 54.245710 |
| 02_focused.json | focused | 37 | FAIL_RETAINED | 1/0/0 | 0.349916 |
| 03_focused.json | focused | 37 | PASS | 0/0/0 | 0.305568 |
| 04_export.json | export | 141 | PASS | 0/0/0 | 52.720032 |
| 05_local.json | local | 171 | PASS | 0/0/0 | 52.931546 |
| 06_export.json | export | 141 | PASS | 0/0/0 | 52.249571 |
| 07_local.json | local | 171 | PASS | 0/0/0 | 52.745402 |

All final local/export failures, errors and skips are zero. Final IDs reconcile:
the 134 baseline local methods are retained plus the 37 K2 methods; the export
contains the same K2 methods plus the 104 tracked K1/predecessor methods.
The 39 accepted K1/R1 methods remain present in both final suites.
The excluded local modules contain exactly 4+8+9+9=30 methods.

The first focused K2 run had one new-test oracle failure: exact comparison of
hypot(3e200,4e200) with literal 5e200 ignored binary64 input rounding.
The corrected oracle uses a 70-digit calculation from the actual supplied
binary64 values. The runtime was not changed for that test correction.
The failed run, test identity and traceback remain in chronological JSON history.
A later strict whitespace check found one extra blank line at runtime EOF.
Only that final newline was removed; AST identity is recorded, and final
local/export suites were rerun against the exact final source bytes. Earlier
successful runs and hashes are retained as earlier execution records.

The isolated export contained 29 files: BASE_COMMIT's tracked package, with only
the two new K2 Python files and candidate README overlaid. It excluded all four
local-only predecessor tests, papers, environments and historical sources.
No staging was used. Runtime imports were asserted under the export, with no
fallback to either live Windows source copy. The tested export was removed only
after its complete results and manifest were copied into the K2 JSON.

Python 3.12.14, NumPy 2.3.5 and SymPy 1.14.0 were used; mpmath supplies test-only
70-digit oracles. No dependency was installed or upgraded. The run harness
records imports, environment, every ID, successful ID, full output, elapsed
time and tested source/test/README hashes. It invokes unchanged unittest
discovery and TextTestRunner with -B, at the declared local/export working roots.

## Preservation, hashes and stopping boundary

The bounded inventory contains **34 protected paths**: the current tracked
package except README, the four local-only tests, and the four specific Paper-E
manuscript/source inputs outside the package. All before/after hashes match.
All other tracked bytes remain unchanged, checked by Git status/diff; the real
index matches its entry snapshot. Outside-allowlist status remains unchanged.
The earlier K1 checkpoint temporary report and evidence were not modified.

Strict no-index whitespace checks on all five K2 paths pass with no inherited
whitespace exception, no staging and no Git configuration change. A no-index
exit of 1 with no findings denotes differing file content from NUL, not an error;
the checks reject findings or stderr. All final checks are retained in JSON.

| Final artifact | SHA-256 |
|---|---|
| kernel_physics/z_manifold.py | 97ebdbb37103e736d2ae86c272541c458a5b585e1889e6d14ff056b316494f4f |
| kernel_physics/tests/test_z_manifold.py | c16b56503d93edf450fc1dee9fa0e5cdc5d91ad57c6ff94d261394b53cf955d6 |
| kernel_physics/README.md | d9d3a4fd51d59c5c48372918ef4beb3a74e5ca3751f323bd046354e02cde3973 |

The finalized report SHA-256 is recorded in the JSON; no report self-hash is embedded.

The companion JSON retains the complete records; it is not a summary substitute.
Its SHA-256 is external, not a recursively embedded self-hash. No K1 validation
artifact or original validation receipt was edited. No new scientific issue
remains unresolved within this bounded implementation packet; numerical-domain
limits above remain explicit. GPT must review the actual files before acceptance.

~~~text
TASK = MK-K2_HISTORICAL_Z_OBSERVER_v0.1
STARTING_HEAD = 2b336f247aa2c24cd7596a1fc733a7b948fdb840
FINAL_HEAD = 2b336f247aa2c24cd7596a1fc733a7b948fdb840
STAGED_Z_OBSERVER = IMPLEMENTED_AND_TESTED
EMA_Z_OBSERVER = SEPARATE_NAMED_VARIANT_IMPLEMENTED_AND_TESTED
CLOCK_AND_EMA_ADVANCEMENT = EXPLICIT_PURE_OPERATIONS
HISTORICAL_INITIALIZATION_DISTINCTION = EXPLICIT_MARKED_CONSTRUCTOR_ZERO_RECORD
RAW_CHIRALITY_DELEGATION = EXISTING_READOUTS_Z_CHIRAL
SOURCE_BODY_PARITY = 12_FIXED_SAME_STATE_COMPARISONS_PASS
LOCAL_TESTS = 171/171_FINAL_PASS
PACKAGE_EXPORT_TESTS = 141/141_FINAL_PASS
LOCAL_ONLY_30_TESTS = PRESERVED_NOT_PUBLISHED
K1_ARTIFACTS_EXCEPT_AUTHORIZED_README_EDIT = UNCHANGED
OMEGA_DYNAMICS_CHANGED = NO
Z_FEEDBACK_TO_OMEGA = NO
SIX_GAP_REGISTRATION = STILL_OPEN
K3_STARTED = NO
STAGING_COMMIT_PUSH = NO
GPT_IMPLEMENTATION_REVIEW = PENDING
CLAUDE_IMPLEMENTATION_REVIEW = NOT_PERFORMED
~~~
