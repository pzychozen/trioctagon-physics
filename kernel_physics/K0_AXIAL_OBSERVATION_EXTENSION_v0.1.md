# K-G0 / K-G1 axial observation extension v0.1

Scientific authority: accepted Paper G v0.1.1, sections 2–3. PDF SHA-256
`453f0f966c7b912995e477334f018032331bbc45910d8eecdd04187ee7e52b3b`.
This additive passive contract is separate from legacy K0 execution/record IDs.

## Frozen public contract

Package 0.2.0; AXIAL_OBSERVATION_API_VERSION="1.0.0";
AXIAL_OBSERVER_REVISION="AXIAL_M1_V1". Legacy API/schema 1.0.0 and ledger 0.1
remain unchanged. Existing public signatures and the fourteen record identity
paths remain unchanged. Changed facade/version bytes honestly change identity.

- AX01: `api.axial_snapshot(omega) -> AxialSnapshot`, exactly three finite
  numeric complex components under existing strict facade conversion.
- AX02: `api.axial_source_budget(before: State, parameters: Parameters, *,
  after: State | None = None) -> AxialSourceBudget`.

The immutable result types are public through api; nested dataclasses are value
containers, not additional public constructors. All vectors/matrices are tuples.
Snapshot fields: revision, source_definition, numeric_policy, S, A, C, Gamma,
C_parallel, C_perp, W, intensity, C_norm, W_norm, chiral_area_accounting,
residuals. The nested accounting preserves existing scalar A/B/h meanings;
snapshot A is the antisymmetric matrix. Residuals include A+cross(C), SC,
reconstructed-C, W_z, e2(S)-C², I²-|Omega.dot(Omega)|²-4C² and
C²-(2W²+Gamma²)/3. The dot is bilinear, not Hermitian.

Budget fields: revision, source_definition, numeric_policy, before_index,
after_index, resolved_parameters, before_snapshot, amplitude_terms,
pre_sync_prediction, phase_terms, predicted_after, congruence_residual,
pair_rotation_residual, actual_after_snapshot, comparison_residuals,
comparison_status, qualification. Each term has name/A/C/W/Gamma. Pre-sync data
includes omega/S/A/phases/delta/d. Prediction and each residual contain A/C/W/Gamma.
The five amplitude terms and two phase terms use the exact names/expressions in
the work order. The returned prediction is the complete budget sum; independent
congruence and pair-rotation evaluations supply signed consistency residuals.
Comparison is actual-minus-predicted; no comparison yields null, not zero.

Only the canonical readouts.z_chiral implementation supplies snapshot C (through
z_diagnostics.chiral_area_accounting). T is the fixed Paper B tangent-column
matrix, not the normal matrix N. Gamma=e^T C; C_parallel=(Gamma/3)e;
C_perp=C-C_parallel; C=(2/3)T^T W+(Gamma/3)e. There is no factor 1/2 in A/C.

## Domains and guarantees

No defaults for scientific parameters. State must be a triad; after, when
supplied, must have index before.index+1. Status is PREDICTION_ONLY or
SUPPLIED_ADJACENT_PAIR. The latter establishes index adjacency only, not a common
record parent; a future worker must establish that provenance separately.

The owner imports only pure numeric/readout helpers, existing L3 and Arg0.
No calls to step3/step_ring/phase_sync/api.step, Runner, clock or EMA advancement;
no RNG, I/O, records, geometry or research imports. It returns no State and
feeds nothing back to the model. Source accounting reconstructs the defined
one-step expressions; it is not a stored intermediate or a trajectory operation.

All seven finite-step terms are retained, with d_ij=delta_j-delta_i and all
delta evaluated from the same reconstructed pre-sync state. Arg0(0)=0 remains;
there is no global Gram closure or full-map common-phase invariance assertion
through zero components. Snapshot common-phase invariance is an exact algebraic
identity, evaluated with rounding. Conjugation reverses C/W/Gamma.

The numerical policy is CHECKED_BINARY64_AXIAL_V1: existing checked products and
compensated sums; explicit ResponsePrecisionError on nonfinite or nonzero
subnormal numerical results/detectable loss to zero. Wrong kinds use TypeError;
invalid shapes/domains use ValueError. The accepted numerical domain is narrower
than the real mathematical domain. No clipping, cancellation certification,
physical magnetic units, field interpretation, interval proof or M3 certificate
is supplied by these binary64 calculations.

## K-G0 independent authorities and test freeze

`tests/fixtures/axial_v1/reference.json` was generated before implementation by
the standalone 100-digit mpmath matrix/pair-product oracle alongside it, with no
kernel imports. SHA-256:
`4811190a7612444783676629bcff5b929eb3b69d933054e29dd00a40a5f18d34`.
The generator refuses to overwrite it. Algebraic witnesses, mutation/omission
controls and frozen outputs test signs, reconstruction, phase order, finite
terms, singular M, zeros, branch cuts and state insufficiency independently of
the observer. `old_api.json` and `old_run.json` come from the unchanged pinned
0.1.0 installation; original-installation resume was checked externally.

Freeze tolerance factors at 512*u for algebraic comparisons, 2048*u for
trigonometric/direct-step comparisons, u=2^-53. Compare scalar reference values
using max(1,|reference|); zero budget residuals use the independently frozen sum
of absolute before/term entries. These are bounded fixture allowances, not a
global error theorem. Common-phase/dynamic fixtures use ordinary magnitudes.
Explicit b_i=0 and pi/2 resonance boundary cases lie outside the proposed ordinary
parameter box and are separately labelled. Any failure is investigated, not
fixed by refreshing fixtures or increasing tolerances.

## Distribution and compatibility

Distribute the new owner as a mandatory build/wheel member, independently bound
by the full build-input manifest and installed-byte verification. Do not add it
to the frozen fourteen-path RunRecord module set. Extend the runtime manifest's
closed build-input vocabulary without extending RunRecord serialized fields.
Old records load canonically; resume still requires exact commit/module identity.
Old records resume under their old installation, not under a different candidate.
New candidate records resume under that candidate. Noninterference compares
canonical records within the same installed build/environment, not across
different provenance identities.

No UI/worker/lock or application artifact change belongs to this kernel release.
Cycle residuals, direction normalization, phase fitting, M2 overlays, static
cards, ring/S01, X01, M4, physical validation and continuation claims are deferred.
