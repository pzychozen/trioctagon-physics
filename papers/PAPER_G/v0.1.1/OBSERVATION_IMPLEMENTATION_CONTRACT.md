# Axial Observables: file-level implementation contract v0.1

4 October 2026. **DESIGN ONLY - LOCAL REVIEW DRAFT.** No implementation or installation is authorized by this document. Mathematical authority: accepted M1 v0.2, M2 final corrections and repaired M3. Paper G v0.1.1 is the explanatory manuscript, not a new runtime certificate.

## 1. Inspected baseline and architecture decision

Repository HEAD: `64ddea159e0e69888926aa21fa281e42f5dd50b4`. Inspection used current source, not an assumed UI architecture. `kernel_physics/api.py` exposes `z_chiral`, `chiral_area_accounting` and `intensity_budget`; it does not expose W, Gamma or the M1 source decomposition. `worker.execute` dispatches `passive_analysis` to `worker.passive_analysis`. `requests.analysis_request` validates its closed input vocabulary. `record_views.AnalysisView` freezes a detached application result. The window methods `_request_analysis`, `_completed`, `_select_analysis`, `_sample_changed` and `analysis_cache` in `app.py` provide the existing asynchronous/cached path. `jobs.py` supplies the isolated worker lifecycle. Scientific equations belong behind the facade, never in drawing callbacks.

The separate `analysis/README.md` describes `trioctagon-analysis` 0.1.1, APP04 recorded-data copying and a closed verified execution lane. It is **not** the passive scratchpad. No B2 coordinator, attestor, approval root, verified issuance, Historical execution or detached protocol extension belongs to this feature. Existing artifact-inspection panels remain separate.

Choose one small pure owner, `kernel_physics/axial_observables.py`, with additive exports in `kernel_physics.api`. Initial use is an explicit analysis of immutable triad samples, not a Runner observer selection or new RunRecord field. Retain the current Runner, recurrence, scheduling, staged Z, EMA, ring, seed, checkpoint and resume behavior. This boundary permits a usable release without changing their state or schema.

## 2. Proposed file changes in a later authorized software change

Paths below are repository-relative; **none is changed by Paper G preparation**.

| File | Bounded future responsibility |
|---|---|
| `kernel_physics/axial_observables.py` (new) | Pure binary64 snapshot, budget and cycle-measurement functions; immutable result types; numerical policy; fixed Paper B T. Imports existing `readouts`, `z_diagnostics`, `_response_numeric` and `dynamics.L3/arg0` as appropriate. Never calls `step3`, `_runner`, services or UI. |
| `kernel_physics/api.py` | Export types and three functions below; validate public `State`/`Parameters` and triad inputs using established facade conventions. No private research imports. |
| `kernel_physics/K0_AXIAL_OBSERVATION_EXTENSION_v0.1.md` (new), `K0_KERNEL_DEFINITION_LEDGER_v0.1.md`, `K4A_SCIENTIFIC_UI_SURFACE_CONTRACT.{md,json}`, `README.md` | Accepted additive AX01 snapshot, AX02 source budget, AX03 finite residual definitions, AX04 static-reference metadata entries, with equation/source/test ownership. Preserve frozen legacy entries and record ledger identity. Mark proposed acceptance pending until software review. |
| `kernel_physics/__init__.py`, `_build_backend.py`, `tools/verify_distribution.py` | New package version, explicit inclusion of the observation owner, installed artifact verification and new build-input identity as detailed in section 8. No regeneration of old source manifests. |
| `kernel_physics/tests/test_axial_observables.py` (new), existing `test_public_contract.py`, `test_import_boundaries.py`, `test_distribution_provenance.py` | Scientific witness, public surface, precision, immutability, import and package tests. |
| `apps/scientific_ui/src/trioctagon_ui/requests.py` | Add closed `axial_snapshot`, `axial_source_budget`, `axial_cycle_residuals` analysis kinds and exact field validation. Keep request/response envelope v2, existing kinds and exact-token limits unchanged. |
| `apps/scientific_ui/src/trioctagon_ui/worker.py` | Facade-only execution; parent parsing, actual sample selection, adjacency and parameter binding, new-operation identity metadata. Reuse `lossless` floats/complex values and error class reporting. |
| `apps/scientific_ui/src/trioctagon_ui/axial_views.py` (new), `app.py`, `plots.py` | State/budget panes, signed history and planar W plots, explicit analyse button and immutable cached playback. `app.py` wires selection/jobs/cache; formulas stay in the kernel owner. |
| `apps/scientific_ui/src/trioctagon_ui/axial_artifacts.py` (new), `record_views.py`, `exports.py` | Strict versioned application-only result codec, cache view, JSON/CSV and PNG/SVG sidecar export. Distinct file family, no `DerivedAnalysisRecord` or scientific replay attestation. |
| `apps/scientific_ui/src/trioctagon_ui/axial_reference.py` (new), `help.json` | Static M2/M3 model labels, applicability checks using declared expressions, reference-card formatting, limits. Reads only packaged inert data. |
| `apps/scientific_ui/reference/axial_m3_v0.1.json` (new) | Explicitly selected exact-model certificate excerpt: model, rational endpoints/weights, bounds, source digests, corrected theorem and exclusions. No executable payload. Redistribution admission required with the later software work order. |
| UI `__init__.py`, `pyproject.toml`, `kernel-artifact.lock.json`, `requirements-win-py311.lock`, `README.md` | New UI version and tested pair, package static resource, regenerate release-specific lock only after certification. No silent repin in this task. |
| UI `tests/test_axial_views.py`, `tests/test_axial_artifacts.py` (new), existing `test_requests.py`, `test_worker_contract.py`, `test_records.py`, `test_comparison_exports.py`, `test_ui.py`, `test_install_launch.py` | Closed protocol, reader, noninterference, display, cancellation, export and installed-pair tests. |

`analysis/`, `historical_kernel/`, `historical_protocol/`, production TORMENT and old paper directories are outside this implementation plan. The lens/SRG preparation facade is a separate task. No UI control implies that unsupported preparation modules are supported.

## 3. Pure API and immutable return contracts

All signatures below are proposed, not callable today. Use keyword-only optional relationships, explicit scientific parameters and no new mathematical defaults.

```python
AXIAL_OBSERVATION_API_VERSION = "1.0.0"   # separate passive-operation contract
AXIAL_OBSERVER_REVISION = "AXIAL_M1_V1"

axial_snapshot(omega: ComplexTriple) -> AxialSnapshot
axial_source_budget(before: State, parameters: Parameters, *,
                    after: State | None) -> AxialSourceBudget
axial_cycle_residuals(first: State, middle: State, last: State, *,
                     direction_floor: float) -> AxialCycleResiduals
```

The three operations accept exactly three finite complex entries. They reject booleans, object/string coercions, length mismatches, NaN/infinity and ring aggregates. Scientific scalars are finite real numbers; no restriction to the M2 parameters applies to general M1 observations. Arrays are copied on ingress and results use frozen dataclasses with tuples (nested tuples for matrices), not writable views into input arrays. Public errors remain `TypeError` for wrong kinds, `ValueError` for domain/shape/adjacency and `ResponsePrecisionError` for unrepresentable numerical operations. Cancellation occurs at worker job boundaries, never halfway through appending a result.

**AxialSnapshot fields:** `revision`, `S[3][3]`, `A[3][3]`, `C[3]`, `Gamma`, `C_parallel[3]`, `C_perp[3]`, `W[3]`, `intensity`, `C_norm`, `W_norm`, `accounting`, `residuals`, `numeric_policy`. S and A use M1 CE01. C is the existing `readouts.z_chiral` result, not an independently signed convention. Reuse `z_diagnostics.chiral_area_accounting` for existing fields. Return signed residuals for `A + cross_matrix(C)`, `SC`, the reconstruction of C, `W_z`, `e2(S)-|C|^2`, `I^2-|Omega.dot(Omega)|^2-4|C|^2`, and `|C|^2-(2|W|^2+Gamma^2)/3`. `cross_matrix` means the standard matrix sending v to C cross v. Do not use a Hermitian dot for `Omega.dot(Omega)`.

**AxialSourceBudget fields:** `revision`, `before_index`, `after_index|null`, `parameters_f64`, `before_snapshot`, `amplitude_terms`, `pre_sync_prediction`, `phase_terms`, `predicted_after_observables`, `actual_after_snapshot|null`, `comparison_status`, `residuals`, `provenance_labels`. Each named area term contains its full A matrix plus its corresponding C, W and Gamma. Terms are:

| Name | Exact defining expression |
|---|---|
| `onsite_first` | epsilon (D A + A D) |
| `coupling_first` | g (L A + A L) |
| `onsite_squared` | epsilon^2 D A D |
| `mixed` | epsilon g (D A L + L A D) |
| `coupling_squared` | g^2 L A L |
| `phase_existing_area` | A_tilde * (cos(d) - 1), elementwise |
| `phase_symmetric_pair` | S_tilde * sin(d), elementwise |

D is evaluated at the supplied before state; L is the canonical triad Laplacian. The diagnostic may evaluate the amplitude expression to obtain `pre_sync_prediction` (complex triple, S_tilde, A_tilde, Arg0 phases, delta and d). This is explicitly **reconstructed accounting data**, not a recorded intermediate. It computes no new `State`, appends no sample and owns no trajectory. Only the existing explicit `step_preview`/`api.step` action may return an advanced state. The budget checks congruence against term sums and pair rotation; it must include squared and mixed contributions even at small coefficients.

`after=None` yields `PREDICTION_ONLY` and null comparison residuals. If supplied, `after.update_index` must equal `before.update_index+1`; otherwise reject. The API alone cannot prove the two states came from the same run; the worker requires the same parsed parent, explicit sample ordinals and unchanged parent parameters. A scratchpad pair is labelled `USER_SUPPLIED_ADJACENT_PAIR`, never recorded. Comparison residuals are actual-minus-predicted A/C/W/Gamma and the full signed budget residual. They do not claim componentwise state parity from phase-invariant quantities. Missing states remain missing; no hidden stepping or interpolation fills gaps.

**AxialCycleResiduals fields:** `revision`, `indices`, `W_reversal_vector`, `W_reversal_norm`, `Gamma_reversal`, `full_two_step_vector`, `full_two_step_norm`, `phase_adjusted_norm`, `fitted_phase|null`, `relative_residuals`, `W_direction_status`, `direction_threshold`, `evidence_class`. Require indices n,n+1,n+2; no guessed lag based on ordinal. Define:

- reversal vector `W(middle)+W(first)` and signed scalar `Gamma(middle)+Gamma(first)`;
- full-state residual vector `last.omega-first.omega` and its Euclidean norm;
- adjusted residual `min_theta ||last-exp(i theta)*first||_2`, theta = arg(first^dagger last) when that inner product is nonzero;
- if that product is zero, the minimum is `hypot(||first||,||last||)` and phase is null (nonunique); if both states are zero the norm is zero and phase remains null;
- relative norms divide by the maximum of the relevant two norms only when that maximum is positive; otherwise report null plus `ZERO_SCALE`, keeping absolute residuals. Gamma normalization uses the maximum absolute pair value. No 0/0, clipping or fabricated phase.

These are proposed diagnostic definitions, not M1 theorems about arbitrary data. Small adjusted residual with a large unadjusted residual indicates a relative recurrence, not a full two-cycle. Never replace them by one generic “periodic” Boolean.

## 4. Numerical policy and tests before implementation admission

Use the established checked binary64 conversion/products/compensated sums and `ResponsePrecisionError` semantics from `_response_numeric.py`; a nonzero subnormal intermediate, loss to zero where the checker can detect it, overflow, or unsupported precision is an explicit refusal. Mathematical formulas have a larger domain than this conservative numerical implementation. Literal zeros remain legal, and Arg0(0)=0 is honoured. Do not divide by component intensity or reconstruct phases using a global Gram formula. Pair budgets evaluate Arg0 directly from the reconstructed complex pre-sync state. Do not silently clamp signed residuals or cross-product terms.

For diagnostic direction only, use `tau_dir=max(direction_floor,128*u*intensity)`, where u=2^-53 and the required caller-supplied `direction_floor` is finite and nonnegative in squared-amplitude units. `W_norm<=tau_dir` means `UNRESOLVED_AT_DISPLAY_SCALE`; all raw components remain accessible. The policy and selected floor appear in exports. It is a visualization threshold, not a theorem, physical threshold or change in the state.

Bounded fixture acceptance: choose exact/symbolic and 100-digit references at ordinary magnitudes with `|Omega_i|<=3`, `|epsilon|<=1/10`, `|g|<=1/4`, `|lambda|<=1/2`, `|k_i|<=7`. For each algebraic residual r, precompute the appropriate scale as the sum of absolute participating terms, and require `|r|<=512*u*max(1,scale)`; for canonical-step comparisons involving trig use `2048*u*max(1,scale)`. These are proposed **fixture** tolerances, not uniform forward-error theorems over every accepted float. Test extreme domains by explicit refusal/representability assertions rather than weakening the tolerances. Freeze fixtures and justified tolerances before code changes; a failed bound requires a recorded witness and review, not an automatic threshold increase.

| Authority / property | Required witness and negative control |
|---|---|
| CE01 Gram and signs | Exact (1,i,1), real triples, zero state; swap pair order or A sign must fail. C must agree with existing public chirality. |
| CE02 attachment | Actual Paper B C3, horizontal/vertical mirrors; carry k under dynamical relabelling. Test rank two, C reconstruction, planar W; N-substitution and transpose errors fail. No arbitrary fixed-unequal-k symmetry assertion. |
| CE04 finite step | Generic complex state with epsilon and g nonzero; compare all five terms and cofactor identity including singular M. Dropping epsilon*g or g^2 must fail. |
| CE05 phase/boundary | Nonzero common-real states, actual zero-component exception `(1,-1,0)*exp(i*pi/6)`, normalization with unit phase, resonant lambda=pi/2 and alpha=pi/6; branch-cut-adjacent, exact-zero and zero-torque witnesses. No divide-by-zero closure. |
| CE08 entrance | Unit-component entrance with norm squared 3 and initial W=0/Gamma nonzero; exact b-product reference, unequal/uniform k, b_i=0 separately. Norm-nine substitution must fail. |
| CE06 nonclosure | Same-A states (1,i,1) and (2,i/2,2), distinct output area factors. Prevent A-only cache keys. |
| Derived residual definitions | Exact identical pairs, conjugate cycle pairs, nonzero relative-phase rotation, zero overlap and zero state. A relative cycle must not be displayed as full-state periodic. |
| M2 applicability | Same requested exact model but different resolved bits shown distinctly; any epsilon/g/k edit disables overlay. No certified mu range or general solver implied. |
| M3 proof card | Locked inert resource, exact rational parsing, N301, q per TWO steps, H-equation, normalization and final limits; altered digest/endpoint, N300 or norm-nine cards rejected as the accepted reference. |
| Noninterference | In the same installed pair/environment, identical seed/params/selection with analyses off versus on must have byte-identical canonical RunRecords and raw trajectory samples. Enabling display must not change observer schedules, clocks, resume segments or raw readouts. |
| UI execution boundary | Spy/patch advancement APIs: loading, selecting, scrubbing, plotting and exporting call none; only explicit experiment/preview advances. Cancelling/error retains parent digest, prior records and previous caches. Worker imports no Qt, plotting backend, models, research scripts or databases. |
| Record and export closure | Refuse unsupported source schemas, ring parents, missing indices and parameter substitutions; reject duplicate keys, nonfinite values and unknown artifact versions. Round-trip immutable app export; distinct family from attested artifacts. |

## 5. Worker, history and user-visible behavior

Views 1 and 2 are one cohesive first release. Select a saved current-model triad, select a sample or history and explicitly request Axial Observables. The worker parses the parent through `api.RunRecord.from_json`; neither GUI extraction nor a file extension bypasses that validator. For stored analysis the worker obtains Omega, update indices and resolved scientific parameters from the parent. Draft controls cannot override them. Explicit scratchpad mode has no parent and labels every supplied value as such.

For a history, compute snapshots of already stored samples. Preserve actual update indices for parity; never infer even/odd from row number after decimation. Cache by parent digest, selected ordinals, actual input float encodings, observation revision and installed implementation identity. Distinguish sample ordinal from update index in every view. Source-budget pairs require actual n,n+1, even if adjacent visible rows skip updates. With absent intermediate samples show `NEXT_SAMPLE_NOT_RECORDED`, no residual, and an optional explicitly selected prediction. A panel must not call `step_preview` automatically to fill it.

View 1 displays S/A/C/Gamma, parallel/perpendicular area, W components/norm, accounting residuals, signed even/odd histories and planar W. Geometry arrows use Paper B frames and explicitly stated anchor/scale, no field lines. View 2 presents seven signed area terms, transformed W/Gamma contributions, reconstructed pre-sync prediction and optional actual-next comparison. Input and after indices remain visible. Recompute-from-stored-state is labelled as new analysis, not an observer recorded by the old producer.

The existing asynchronous job queue, cancellation and complete-result handling remain. A completed immutable analysis may append to `analysis_cache` only after all validation. Plot callbacks read the cache. Exporting or changing display precision reads the same cached raw floats. Parent JSON, deterministic digest, lineage and stored observer state never change.

## 6. Model-qualified overlays and static reference card

First release includes a read-only M3 card with exact epsilon=1/20, g=1/5, exact-decimal k, lambda=exact lambda_c+1/200, the algebraic entrance with squared norm three, exact rational trap/weights, N=301 sufficient entry, q<=4789/5000 per two updates, chart bounds, separate H-Krawczyk proof and nonzero W/Gamma. It records final accepted source hashes and says `ARCHIVED_EXACT_MODEL_CERTIFICATE`. Authentication of bytes and mathematical verification of inequalities are separate displayed facts. No user-supplied Python is executed and loading the card performs no trajectory or verifier replay.

A later View 3 shows the accepted M2 interval lambda_c and c and the numerical critical direction/prefactor, with the square-root leading term. Only an explicitly selected M2 reference definition enables the overlay. Epsilon/g/k must correspond to the declared exact model; show those requested expressions separately from their resolved binary64 hex values. A generic imported RunRecord whose only evidence is matching rounded floats can be compared as `NUMERICAL_MODEL_MATCH_ONLY`, not declared the exact certified model. Editing any of the three parameter families turns applicability off. Lambda is the comparison coordinate, not a universal magnetic threshold. No solver/scan or hidden parameter slider rounding is added.

UI expression support for this panel should use a **closed named reference token**, e.g. `M3_LAMBDA_C_PLUS_1_OVER_200`, carrying the exact-source ID and a documented resolution policy. Do not pass its text to Python `eval`, extend the geometry parser with arbitrary symbols or relabel a decimal lambda as exact lambda_c. Preserve current draft literal strings and resolved hex arrays for the actual run. A user-triggered numerical experiment calls the unchanged `run` path with those resolved numbers. It never inherits M3's interval guarantee; approximate trap distance is labelled `NOMINAL_REFERENCE_DISTANCE` even if a rounded point plots inside a displayed box. M2 and M3 appear as separate results with no claimed continuation curve.

## 7. App artifact, inputs and export identity

New file family: `TRIOCTAGON_AXIAL_OBSERVATION`, `schema_version="0.1.0"`; proposed suffix `.axial.json`. This is an application calculation record, **not** a RunRecord, GeometryRecord, DerivedAnalysisRecord, AttemptReceipt or attestation. It is not resumable. Store:

```text
artifact_type, schema_version, observation_api_version, observer_revision,
analysis_kind, evidence_class="FLOATING_OBSERVATION",
parent {deterministic_sha256, canonical_bytes_sha256, source_commit} | null,
selection [{sample_ordinal, update_index}],
input_policy, requested_expressions, resolved_inputs_hex,
implementation {distribution, version, source_commit, build_input_sha256,
                installed_owner_sha256, installed_facade_sha256},
numeric_policy {precision, direction_floor, residual_definitions_revision},
data, reference_comparison | null, qualification, content_sha256
```

Use existing lossless float wrappers (`{"f64": float.hex()}`) and immutable structures. `content_sha256` covers deterministic canonical JSON excluding itself and optional display/time fields; reject duplicate keys, unknown fields, invalid lengths and nonfinite values. Hashes bind bytes, not trusted execution. The record carries a clear unauthenticated-local-computation qualification; no `verified=true`. Parent digest and current installed identity are separate. The existing worker's generic qualification says current identity is not independently exposed: for **new axial kinds** add actual installed provenance fields and matching qualification rather than copying that inaccurate sentence or changing old cached results.

CSV includes update indices, component names, signs, evidence class and an adjacent JSON provenance sidecar. PNG/SVG sidecars identify the immutable result digest, selected view/range, scale/anchor and source record. The static reference certificate is a different bundled inert object; do not mix its proof status with a floating artifact. Loaded `.axial.json` is an untrusted displayed result unless its original bytes and provenance are established; importing it never launches a worker computation.

## 8. Versions, provenance closure and installed pair

Current installed target is **not repository main**. Inspected `kernel-artifact.lock.json` v2 selects kernel distribution `trioctagon-physics==0.1.0`, source `7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e`, direct wheel SHA-256 `8f7c8a3e3c8f84e0f07344e8deae633d07b17aec9f05e8559791994e91ac9c36`, build input `38fa7c1721dffb0822bfdb1f1952db8a50394ceafbf10666201ad17450d2f453`. The admitted reconstructed wheel SHA-256 is `280dad0d7439124002590c6f908ae59169fc9ab6f7f42b2f97c067024036603e`. UI source declares `trioctagon-scientific-ui==0.1.2`. These identities cannot certify new exports. Lock provenance identifies a temporary development artifact; no public-release claim follows.

**Bounded proposed version policy:** kernel package 0.2.0 and UI package 0.2.0, with explicit new `AXIAL_OBSERVATION_API_VERSION=1.0.0` and observer revision. Retain the legacy core `api_version=1.0.0`, RunRecord/GeometryRecord schemas 1.0.0 and record `ledger_version=0.1` because no operation, source definition or serialized field in those contracts changes. The reviewed K0 extension adds the passive operation surface; it does not redefine old IDs. This is a deliberate additive compatibility design, not an accidental omission of versioning. If reviewers require a core API minor bump instead, that is a separate compatibility decision: `_VERSION` currently conflates API and both schemas, so blind replacement would reject old records. Do not make that replacement in the bounded implementation.

The frozen 14-path `_records._MODULES` and `_build_backend.MODULES` identify the legacy execution/record closure. Keep them and A--F paper references unchanged for legacy RunRecords. The new observation module must instead be admitted in `_build_backend.PYTHON_FILES`/`INPUTS`, the full wheel file list and installed-byte verification; the new observation artifacts explicitly bind its hash and the complete build-input identity. This separation is justified by execution: the Runner never invokes the passive owner. It must not conceal participation in a new observation result. Existing `api.py` is already in the legacy closure, so its changed facade bytes will honestly change new-build identity; no old digest is reused. The distribution verifier must check the added owner as a mandatory stable member, not optional unchecked data. All actual import dependencies of the new owner must be included in its observation identity.

Update explicit file-list expectations in `_build_backend.py`, `tools/verify_distribution.py` and their tests after reviewing the new import closure. Admit the new static UI JSON in setuptools package data and the installed UI integrity list. The software license scope must be reviewed for any copied paper reference data; do not broaden `LICENSE_SCOPE.md` automatically. A new UI lock is generated from the exact newly tested wheel and commit, with full RECORD/member verification and reconstruction equivalence if still used. Do not paste a new hash into the old K3 certification. `analysis-artifact.lock.json` and `historical-protocol-artifact.lock.json` remain untouched.

Compatibility gates include: loading existing v1 records still preserves their bytes and accepted/refused source semantics; resume under mismatched implementation still refuses exactly as before; same-pair runs with observations on/off are identical; missing/mismatched observation revision or wheel yields a clear incompatibility error before analysis. No fallback to an arbitrary checkout import, registry-latest package or dynamic research script.

Use existing installed Windows test entry points after building a new clean, separately authorized source artifact, with fresh external directories:

```bat
conda activate torment
python -I -B apps\scientific_ui\tests\test_install_launch.py --acquire --source <new-authorized-source> --workspace <new-external-acquire>
python -I -B apps\scientific_ui\tests\test_install_launch.py --certify --source <new-authorized-source> --workspace <new-external-certification>
```

Run `python -I -B -m trioctagon_ui --smoke-test` inside the isolated certified installation, not merely the development conda import path. The existing pure kernel/UI unittest modules plus new tests above are the relevant checks; TORMENT service tests are not. Exact commands for test import paths remain those of the inspected repository harness and must be recorded with the later software execution results, not represented as already run now.

## 9. Cohesive implementation sequence and admission gates

1. Freeze the modest binary64 fixtures and operation/result schema, then implement the pure owner, facade and package inclusion together. Review signs, zero-component behavior and precision failures before wiring displays.
2. Deliver Views 1--2, cache/export lineage and static M3 card in one installed release, with worker noninterference and the actual new kernel/UI pair certified. This is the first usable result; no empty framework-only milestone is needed.
3. Add View 3 finite comparison and qualified M2 overlay using the same result/cache path after its proposed residual definitions are approved. Keep user-triggered experiments explicit and bounded; no M4 or continuation solver is needed.

Remaining review decisions are the proposed diagnostic tolerances/direction policy, the explicit additive version strategy and redistribution of the inert reference excerpt. There is no scientific blocker requiring another M1--M3 audit. Implementation remains pending a separate work order; this document makes its files, contracts, tests and packaging obligations concrete.
