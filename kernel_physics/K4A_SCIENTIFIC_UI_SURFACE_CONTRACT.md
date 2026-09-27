# K4a — Scientific UI surface and interaction contract

Documentation only · audited 2026-09-27 · source `7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e`

## Frozen disposition

```text
STARTING_HEAD = 7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e
K4A_STATUS = PASS
PUBLIC_FACADE_MAPPED = YES (34/34)
UI_WORKSPACES_FROZEN = YES (A-D accepted)
CONTROL_CLASSIFICATION_FROZEN = YES
INPUT_VALIDATION_FROZEN = YES
SLIDER_POLICY_FROZEN = YES
HISTORICAL_PRESET_UI_FROZEN = YES
GEOMETRY_DYNAMICS_SEPARATION = PRESERVED
OBSERVER_FEEDBACK = NO
RESEARCH_ONLY_UI_EXPOSURE = NO
OPTION_B_UI_EXPOSURE = NO
RECORD_PROVENANCE_UX = FROZEN
DATASET_CONTRACT = FROZEN (implementation deferred to K4d)
ERROR_SURFACE = FROZEN
PUBLIC_API_GAPS = 4 optional; 0 first-slice blockers
SCIENTIFICALLY_UNSUPPORTED_UI_IDEAS = Excluded: coupling/physical mappings and listed research controls
RECOMMENDED_UI_ARCHITECTURE = Native Python Qt Widgets + Matplotlib + worker subprocess
UI_PACKAGE_BOUNDARY = SEPARATE_APPLICATION_LAYER
NETWORK_REQUIRED = NO
MODEL_REQUIRED = NO
GPU_REQUIRED = NO
K4B_VERTICAL_SLICE = FROZEN
K4B_SCOPE_DEFINED = YES
PRODUCTION_SOURCE_CHANGED = 0
PACKAGE_SOURCE_CHANGED = 0
EXISTING_TEST_CHANGED = 0
CI_CHANGED = 0
PAPERS_CHANGED = 0
RESEARCH_CHANGED = 0
FIXTURES_CHANGED = 0
FILES_CREATED = 2
FILES_MODIFIED = 0
K4B_READY_FOR_AUTHORIZATION = YES
UI_IMPLEMENTED = NO
DEPENDENCIES_ADDED = 0
PYPI_UPLOAD_AUTHORIZED = NO
PUBLIC_RELEASE_VERSION_BUMP = NO
REGISTRY_NAME_AVAILABILITY_CERTIFIED = NO
GITHUB_RELEASE_AUTHORIZED = NO
```

## Authority, disposition and governing rule

K4A_STATUS = PASS: documentation/interaction contract only. K4 implementation has not started. Authority was audited at source commit 7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e on 2026-09-27, on main with no tracked edits. The 715 starting tracked files and unrelated untracked contents are preserved. This contract creates exactly the Markdown and JSON K4a documents; it changes no code, dependencies, tests, CI, paper, research, fixture, package version or record schema.

UI DISPLAYS SCIENCE. PYTHON KERNEL COMPUTES SCIENCE. The only application-facing scientific import is kernel_physics.api. Existing result attributes and public records are the data contract. Private modules were read to understand enforcement, not authorized as application imports. A renderer may select, format, project and draw returned data; it may not implement recurrence, chirality, observers, accepted geometry construction or accounting equations.

The source of truth for export inventory is api.__all__, not an earlier planned list. K0's ledger supplies definitions/qualifications; its dated “not implemented” and open O01/O03 language is superseded by actual K1–K3 code and K2 final closeout. O01 is quarantined, O03 is closed, and O02 remains OPEN_NONBLOCKING historical rationale. K3 certification belongs to the pinned R3 commit; this documentation does not fabricate an installation certificate for a later commit.

All current public exports are mapped below. Classifications govern supported UI exposure; an ADVANCED feature can be staged after K4b without becoming scientifically unsupported. Historical selection fills visible values only after an explicit action. No fresh form silently chooses scientific inputs.

## CURRENT PUBLIC FACADE MAP

Exact inventory: 34 exports, API 1.0.0, RunRecord/GeometryRecord schemas 1.0.0, ledger 0.1, package 0.1.0. Signature annotations below reflect actual Python signatures; semantic domains are in the validation matrix. Return types owned internally remain accessible through returned objects and their documented fields; the UI must not import their defining private modules.

run readouts: exactly z_chiral. run diagnostics: exactly chiral_area_accounting, intensity_budget, potential, readout_accounting, historical_alignment. The last two require observers. quadratic_form and all history-coordinate helpers are public standalone functions, not additional run-selection strings. Standalone evaluation is an explicit passive-analysis action cached separately against input record digest/sample, never a hidden scrub callback or an insertion into the original record.

| export | signature | workspace | semantics | source | ledger |
| --- | --- | --- | --- | --- | --- |
| Parameters | (*, eps: float, g: float, phase_strength: float, k: tuple) -> None | A | Explicit eps, g, phase_strength and ordered real k triple; no defaults. | kernel_physics/_contract_types.py:70 | A01 |
| State | (*, omega: tuple, update_index: int) -> None | A | Immutable Omega and index: triad has 3 complex entries; ring State has 3q, q>=1. State itself is not restricted to ComplexTriple. | kernel_physics/_contract_types.py:89 | A05,A06,S01 |
| Seed | (*, name: str, omega: tuple, provenance: kernel_physics._contract_types.Provenance) -> None | A | Named complex triple plus provenance; convert explicitly to State with a chosen index before run. | kernel_physics/_contract_types.py:102 | L02,S01 |
| Provenance | (*, kind: str, source_id: str, source_revision: str \| None, locator: str, literal_values: collections.abc.Mapping, notes: str) -> None | A/B/D | Explicit source descriptor and literal spellings; not a proof of scientific truth. | kernel_physics/_contract_types.py:45 | S01,S05 |
| historical_seed | (name: str) -> kernel_physics._contract_types.Seed | A | Only gate_torus_seed_v1; returns Seed with literal values and unresolved-rationale note. | kernel_physics/_presets.py:8 | L02,O02 |
| step | (state: kernel_physics._contract_types.State, parameters: kernel_physics._contract_types.Parameters, *, topology: str) -> kernel_physics._contract_types.State | A | One authoritative update -> new State; UI record-producing One update action uses run(updates=1). | kernel_physics/api.py:23 | A05,A06 |
| z_chiral | (omega) | A/B | Finite complex triple -> raw real chirality vector in channel order (BC,CA,AB), without normalization. | kernel_physics/api.py:27 | B01 |
| Clock | (*, q: int, N: int, t: float, q_step: int) -> None | B | Explicit q,N,t,q_step; observer clock, not a dynamics timestep. | kernel_physics/_contract_types.py:114 | E01 |
| StagedConfig | (*, lambda_vp: float, gamma: float, theta_lock: float, alpha: float, beta: float) -> None | B | Explicit signed finite lambda_vp,gamma,theta_lock,alpha,beta. | kernel_physics/_contract_types.py:131 | E02,E03 |
| EMAConfig | (*, lambda_vp: float, theta_lock: float, alpha: float, beta: float) -> None | B | Explicit signed finite lambda_vp,theta_lock,alpha,beta; no gamma. | kernel_physics/_contract_types.py:147 | E03,E04 |
| EMAState | (*, m: float) -> None | B | Current memory m, \|m\|<=1; retention/innovation coefficient is not configurable. | kernel_physics/_contract_types.py:162 | E04,L04 |
| advance_clock | (clock: kernel_physics._contract_types.Clock, dt) -> kernel_physics._contract_types.Clock | B | New Clock only; q is reduced modulo N after advance, t uses delegated addition. | kernel_physics/api.py:31 | E01 |
| advance_ema | (omega, memory: kernel_physics._contract_types.EMAState) -> kernel_physics._contract_types.EMAState | B | New memory only from supplied Omega; does not step dynamics or clock. | kernel_physics/api.py:36 | E04 |
| observe_staged | (omega, clock: kernel_physics._contract_types.Clock, config: kernel_physics._contract_types.StagedConfig) -> kernel_physics.z_manifold.ZReadout | B | Pure staged observation -> ZReadout; no state/clock advance. | kernel_physics/api.py:41 | E02,E03 |
| observe_ema | (omega, clock: kernel_physics._contract_types.Clock, config: kernel_physics._contract_types.EMAConfig, memory: kernel_physics._contract_types.EMAState) -> kernel_physics.z_manifold.ZReadout | B | Pure observation of current memory -> ZReadout; no memory update. | kernel_physics/api.py:47 | E03,E04 |
| historical_observer | (name: str) -> kernel_physics._contract_types.ObserverRequest | B | Only paper_e_staged_v1 or paper_e_ema_v1; explicit recomputed initialization. | kernel_physics/_presets.py:18 | L03,L04,O02 |
| ObserverRequest | (*, observer_id: str, config: kernel_physics._contract_types.StagedConfig \| kernel_physics._contract_types.EMAConfig, clock: kernel_physics._contract_types.Clock, memory: kernel_physics._contract_types.EMAState \| None, dt: float, initialization: str, provenance: kernel_physics._contract_types.Provenance) -> None | B | Typed passive configuration, clock/memory, dt, initialization and provenance; variant is derived. | kernel_physics/_contract_types.py:176 | S02,E01,E04,E05 |
| ZReadout | (z: float, Z_macro: numpy.ndarray, Z_chiral: numpy.ndarray, Z_total: numpy.ndarray, variant: str, initialization: str = 'recomputed') -> None | B | z,Z_macro,Z_chiral,Z_total,variant,initialization; Z_vec is a read-only alias. UI displays returned values rather than constructing substitute observations. | kernel_physics/z_manifold.py:165 | E03 |
| ResponsePrecisionError | (message): exception type | A/B/D | Public FloatingPointError subclass; failed numerical request, not a scientific zero. | kernel_physics/_response_numeric.py:14 | N01 |
| run | (initial_state: kernel_physics._contract_types.State, parameters: kernel_physics._contract_types.Parameters, *, topology: str, updates: int, parameter_provenance: kernel_physics._contract_types.Provenance, initialization_provenance: kernel_physics._contract_types.Provenance, observers: tuple, readouts: tuple, diagnostics: tuple) -> kernel_physics._records.RunRecord | A/B | Explicit selections and provenance -> immutable complete RunRecord with initial sample plus updates. | kernel_physics/_runner.py:99 | S02,S03 |
| resume | (record: kernel_physics._records.RunRecord, *, updates: int) -> kernel_physics._records.RunRecord | A/D | Append to compatible record with identical source commit/modules, parameters and selection; returns a new record. | kernel_physics/_runner.py:156 | S02 |
| RunRecord | (data) | D | data, to_json(), from_json(text), deterministic_sha256. Constructor accepts a record mapping but UI must not synthesize/edit records. | kernel_physics/_records.py:481 | S03 |
| GeometryRecord | (data) | C/D | Same public record interface; exact geometry, independent from runs; coupling=none. | kernel_physics/_geometry_records.py:249 | S04 |
| get_geometry | (definition_id: str, *, options: collections.abc.Mapping) | C | Only C01 or D03, explicit exact options -> GeometryRecord. | kernel_physics/_geometry_records.py:178 | C01,D03,S04 |
| quadratic_form | (vector) | B | Finite real triple -> signed Q; separate function, not a run diagnostic selection ID. | kernel_physics/api.py:54 | E06 |
| readout_accounting | (readout, *, alpha, beta) | B | ZReadout + explicit alpha,beta -> complete signed blend/norm/Q accounting; no repair. | kernel_physics/api.py:58 | E06 |
| chiral_area_accounting | (omega) | B | Complex triple -> chirality, intensity, Gram/bound/slack quantities and residuals. | kernel_physics/api.py:62 | E07 |
| intensity_budget | (omega, parameters) | B | Complex triple + Parameters -> finite-map accounting including pre-sync prediction; not a next state. | kernel_physics/api.py:66 | E09 |
| potential | (omega, parameters) | B | Complex triple + Parameters -> scalar potential; not guaranteed to decrease per update. | kernel_physics/api.py:71 | E10 |
| historical_alignment | (macro, chiral, total_vector) | B | Three real vectors -> dot conventions and resolution flags at historical threshold 1e-12; unresolved is not orthogonal. | kernel_physics/api.py:76 | E08,L06 |
| direct_history_coordinates | (history, *, key) | B | Copy selected real (n,3) history columns -> x/y/z; Z_total falls back to Z_vec only if absent. | kernel_physics/api.py:80 | E11 |
| cylinder_point | (kappa, q, z, *, N) | B | Explicit kappa,q,z,N -> display point, unrelated to Paper-C shell placement. | kernel_physics/api.py:84 | E11 |
| cylinder_history_coordinates | (history, *, N) | B | kappa,z,phi_index arrays and explicit N -> display coordinates; empty history allowed. | kernel_physics/api.py:88 | E11 |
| history_torus_coordinates | (history, *, R, r_max, N) | B | Nonempty entire history + R,r_max,N -> display coordinates and normalization facts; no runtime inverse. | kernel_physics/api.py:92 | E12,L06 |

## UI WORKSPACE MAP

ACCEPT the four-workspace organization. A and B share one explicit run draft and one immutable selected RunRecord; B owns passive selections, not a second dynamics engine. C has an independent geometry draft and GeometryRecord. D inspects either record type. Every workspace preserves the current record when a draft changes. A persistent identity strip shows selected record type, source commit abbreviation, digest abbreviation and saved/unsaved state; expanded D exposes full values.

Basic disclosure: choose explicit input or deliberately load a named historical example, edit eps/g/phase_strength/updates, inspect submitted k and initial state, then run. Advanced disclosure adds full state/k/provenance and observer configuration. Provenance remains one click away in basic mode. Unsupported controls are not hidden behind an “expert physics” toggle.

| workspace | inputs_and_actions | visible_outputs | boundary | K4b_extent |
| --- | --- | --- | --- | --- |
| A Dynamics Lab | State, Parameters, topology, updates; historical seed; Run, One update, Zero updates, Resume, New run from checkpoint. | Omega Re/Im, update index, requested raw chirality, explicit request summary. | No geometry input; ring has no observer/readout/diagnostic selections. | Triad vertical slice, explicit/preset state, all parameter fields, stored sample table/plots; advanced ring path can follow in K4c. |
| B Observer & Diagnostics Lab | Historical observer selection or explicit configuration; passive diagnostic selections; standalone analysis requests. | z, M/C/T, q/t/m, resolution flags, signed accounting, passive display coordinates. | PASSIVE OBSERVATION / DIAGNOSTIC; no feedback into Omega. | Named staged/EMA presets and diagnostics selection/structured output; custom observer/history tools later. |
| C Geometry Explorer | C01 sections; D03 construction and exact options; request, inspect, save/load. | Exact expressions, coordinate frames, incidence/topology, symmetry qualifications and derived wireframe. | GeometryRecord is independent; mathematical_length is not a physical unit calibration. | C01 and D03 regular(s) with exact integer/rational inputs, rotatable CPU wireframe and exact inspector. |
| D Reproducibility / Records | Save record JSON, Load/validate JSON, save draft separately, inspect metadata, compatible resume or checkpoint action. | Digest, full source identity, 14 module hashes, paper refs, producer segments, validation status. | Digest/structure validity is not scientific replay verification or authentication. | Both record types; portable loading, exact save, clear resume errors and separate draft state. |

## CONTROL CLASSIFICATION

Each row has exactly one of the seven required classes. Context is part of the control ID: an editable draft field and its immutable recorded counterpart are different controls. READ_ONLY output groups expand over every returned field enumerated later. PRIVATE/RESEARCH entries have no executable menu route. Phase is implementation scheduling, not a second control classification.

| control | class | workspace | semantic_reason | phase |
| --- | --- | --- | --- | --- |
| draft.input_mode | PRIMARY | A | Explicit scientific choices, no hidden defaults. | K4b |
| draft.updates | PRIMARY | A | Explicit scientific choices, no hidden defaults. | K4b |
| draft.Parameters.eps | PRIMARY | A | Explicit scientific choices, no hidden defaults. | K4b |
| draft.Parameters.g | PRIMARY | A | Explicit scientific choices, no hidden defaults. | K4b |
| draft.Parameters.phase_strength | PRIMARY | A | Explicit scientific choices, no hidden defaults. | K4b |
| draft.State.omega[*].re | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.State.omega[*].im | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.State.update_index | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.Parameters.k[0] | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.Parameters.k[1] | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.Parameters.k[2] | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.k_equal_lock | ADVANCED | A | Inspect all submitted values; k lock copies a visible scalar into an explicit triple. | K4b |
| draft.topology | ADVANCED | A | Public ring/custom-seed input, not a new recurrence or generator. | K4c |
| draft.ring_size | ADVANCED | A | Public ring/custom-seed input, not a new recurrence or generator. | K4c |
| draft.Seed.name | ADVANCED | A | Public ring/custom-seed input, not a new recurrence or generator. | K4c |
| draft.Seed.omega | ADVANCED | A | Public ring/custom-seed input, not a new recurrence or generator. | K4c |
| preset.gate_torus_seed_v1 | HISTORICAL_PRESET | A/B | Explicitly applied, provenance-labelled literals; rationale remains unresolved where O02 applies. | K4b |
| preset.paper_e_staged_v1 | HISTORICAL_PRESET | A/B | Explicitly applied, provenance-labelled literals; rationale remains unresolved where O02 applies. | K4b |
| preset.paper_e_ema_v1 | HISTORICAL_PRESET | A/B | Explicitly applied, provenance-labelled literals; rationale remains unresolved where O02 applies. | K4b |
| preset.reference_eps_g_k_phase | HISTORICAL_PRESET | A/B | Explicitly applied, provenance-labelled literals; rationale remains unresolved where O02 applies. | K4b |
| draft.readouts.z_chiral | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.diagnostics.chiral_area_accounting | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.diagnostics.intensity_budget | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.diagnostics.potential | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.diagnostics.readout_accounting | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.diagnostics.historical_alignment | ADVANCED | B | Explicit opt-in selectors; display consequences/domain failures before submit. | K4b |
| draft.ObserverRequest.observer_id | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.ObserverRequest.variant | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.Clock.q | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.Clock.N | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.Clock.t | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.Clock.q_step | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.ObserverRequest.dt | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.ObserverRequest.initialization | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.EMAState.m | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.StagedConfig.lambda_vp | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.StagedConfig.gamma | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.StagedConfig.theta_lock | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.StagedConfig.alpha | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.StagedConfig.beta | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.EMAConfig.lambda_vp | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.EMAConfig.theta_lock | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.EMAConfig.alpha | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.EMAConfig.beta | ADVANCED | B | Signed configuration and independent observer state; variant routes to the correct public type. | K4c |
| draft.user_provenance.source_id | ADVANCED | A/B/D | User-entered source descriptions must be visible; edits do not alter an existing record. | K4b |
| draft.user_provenance.source_revision | ADVANCED | A/B/D | User-entered source descriptions must be visible; edits do not alter an existing record. | K4b |
| draft.user_provenance.locator | ADVANCED | A/B/D | User-entered source descriptions must be visible; edits do not alter an existing record. | K4b |
| draft.user_provenance.literal_values | ADVANCED | A/B/D | User-entered source descriptions must be visible; edits do not alter an existing record. | K4b |
| draft.user_provenance.notes | ADVANCED | A/B/D | User-entered source descriptions must be visible; edits do not alter an existing record. | K4b |
| provenance.kind | READ_ONLY | A/B/C/D | Derived from action/public result, not editable claims. Historical edits produce a user-supplied draft retaining origin notes. | K4b |
| historical.provenance | READ_ONLY | A/B/C/D | Derived from action/public result, not editable claims. Historical edits produce a user-supplied draft retaining origin notes. | K4b |
| geometry.construction_provenance | READ_ONLY | A/B/C/D | Derived from action/public result, not editable claims. Historical edits produce a user-supplied draft retaining origin notes. | K4b |
| observer.variant_result | READ_ONLY | A/B/C/D | Derived from action/public result, not editable claims. Historical edits produce a user-supplied draft retaining origin notes. | K4b |
| observer.staged_memory_none | READ_ONLY | A/B/C/D | Derived from action/public result, not editable claims. Historical edits produce a user-supplied draft retaining origin notes. | K4b |
| geometry.definition_id | PRIMARY | C | Only C01/D03. | K4b |
| geometry.D03.s | ADVANCED | C | Exact positive length, distinct from scientific dynamics coefficients. | K4b |
| geometry.C01.section_heights | ADVANCED | C | Exact options with construction-specific fields and constraints. | K4c; K4b only [] sections and regular(s) |
| geometry.D03.construction | ADVANCED | C | Exact options with construction-specific fields and constraints. | K4c; K4b only [] sections and regular(s) |
| geometry.D03.g_gap | ADVANCED | C | Exact options with construction-specific fields and constraints. | K4c; K4b only [] sections and regular(s) |
| geometry.D03.p | ADVANCED | C | Exact options with construction-specific fields and constraints. | K4c; K4b only [] sections and regular(s) |
| geometry.C01.w | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.C01.s | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.C01.beta | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.frames | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.incidence | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.symmetry | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| geometry.resolved_parameters | READ_ONLY | C | Accepted returned geometry facts, not free shape controls. | K4b |
| analysis.quadratic_form.vector | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.readout_accounting.readout | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.readout_accounting.alpha | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.readout_accounting.beta | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.historical_alignment.macro | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.historical_alignment.chiral | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| analysis.historical_alignment.total_vector | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.history | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.key | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.kappa | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.z | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.phi_index | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.q | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.N | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.R | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| display.r_max | ADVANCED | B | Explicit public standalone inputs or selections from stored results; cache analysis separately. | K4c |
| action.run | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.zero_updates | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.one_update | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.resume | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.new_checkpoint_run | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.request_geometry | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.load_record_json | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.save_record_json | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.save_draft_json | PRIMARY | A/C/D | Explicit commands; Save record and Save draft are distinct. | K4b |
| action.observe_staged | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| action.observe_ema | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| action.advance_clock | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| action.advance_ema | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| action.step_preview | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| action.passive_analysis | ADVANCED | A/B | Standalone scratchpad returns new detached values; never alters current RunRecord. | K4c |
| view.sample_index | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.play | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.pause | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.step_forward | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.step_back | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.camera | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.axes | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.series_visibility | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.display_precision | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.playback_rate | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.compare_selection | ADVANCED | A/B/C/D | Presentation-only controls, never science inputs. | K4c; K4b sample index/camera/series |
| view.record.data | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.record.deterministic_sha256 | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.record.implementation | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.record.paper_references | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.record.execution_metadata | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.all_public_result_fields | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.error_details | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.O02_status | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| view.submitted_request | READ_ONLY | A/B/C/D | Every output field listed in the output map inherits READ_ONLY; no record edit widget. | K4b |
| export.csv | ADVANCED | D | Derived export/finite batch description, separate from authoritative public JSON. | K4d; draft JSON in K4b |
| export.png | ADVANCED | D | Derived export/finite batch description, separate from authoritative public JSON. | K4d; draft JSON in K4b |
| export.svg | ADVANCED | D | Derived export/finite batch description, separate from authoritative public JSON. | K4d; draft JSON in K4b |
| dataset.finite_sweep_request | ADVANCED | D | Derived export/finite batch description, separate from authoritative public JSON. | K4d; draft JSON in K4b |
| internal.boundary_response | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.srg | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.operating_region | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.face_state | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.EMA_tau | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.alignment_threshold | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.torus_regularizer | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.arg0_policy | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| internal.C01_arbitrary_beta | INTERNAL_HIDDEN | none | Shipped/internal or fixed definition does not imply an editable supported feature. | excluded |
| research.Twisted Hex Crystal | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.spatial M/C/T registration | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.gate/aperture mappings | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.finite-patch physics interpretations | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.spring/restoring laws | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.EM/Riemann-Silberstein comparisons | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.six-axis physical selector | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.Paper-F normal-form runtime | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.warp research | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.Z feedback | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.mechanical-clock interpretations | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| research.geometry/dynamics coupling | RESEARCH_ONLY | none | Not an executable public-v1 control or accepted physical attachment. | excluded |
| future.live_partial_sample_stream | OPEN / DECISION_REQUIRED | none | Deferred public API capability; no enabled control until separately authorized. | later decision |
| future.D03_symmetry_animation | OPEN / DECISION_REQUIRED | none | Deferred public API capability; no enabled control until separately authorized. | later decision |
| future.polar_input | OPEN / DECISION_REQUIRED | A | Representation-only Python adapter is possible; authoritative real/imaginary entry remains the frozen first mode. | later decision |
| action.cancel_job | PRIMARY | A/B/C/D | Stop the active worker and retain completed records; no partial scientific result is claimed. | K4b |
| draft.observer_selection | ADVANCED | B | Explicitly choose none, staged, EMA or both; no silently attached observer. | K4b |
| view.reset_camera | ADVANCED | A/B/C/D | Display navigation and progressive disclosure never alter scientific requests or records. | K4b |
| view.object_visibility | ADVANCED | A/B/C/D | Display navigation and progressive disclosure never alter scientific requests or records. | K4b |
| view.raw_json | ADVANCED | A/B/C/D | Display navigation and progressive disclosure never alter scientific requests or records. | K4b |
| view.disclosure_level | ADVANCED | A/B/C/D | Display navigation and progressive disclosure never alter scientific requests or records. | K4b |
| preferences.run_warning_threshold | ADVANCED | D | Labelled application safeguards with explicit overrides; never scientific ranges. | K4b |
| preferences.resource_guard | ADVANCED | D | Labelled application safeguards with explicit overrides; never scientific ranges. | K4b |
| preferences.sweep_warning_threshold | ADVANCED | D | Bounded case/sample confirmation preferences only. | K4d |

## INPUT VALIDATION MATRIX

This matrix records enforced software domains, not experimental safety regions. Public real fields have no sign or preferred-value restriction unless explicitly listed. Finite binary64 representability is a software limit; it is not a scientific slider bound. UI text parsing and shape feedback precede a public constructor/function call, and never replace kernel validation. Decimal dynamics text is converted once to binary64 in Python; show the resolved value/hex when precision matters. Keep the original text in draft/session provenance. Geometry decimal text, when allowed by the application grammar, means an explicit exact rational, not a float silently rationalized by the kernel.

For checkpoint/import adaptation, read public record fields; decode documented f64 strings in the Python adapter with float.fromhex and exact integer strings with int after public validation. This is representation adaptation, not a new record writer. Do not import _records._complex/_f64, _geometry_records._decode_exact, or any other private codec.

| field | type | enforced_domain | cross_field_rule | error | source |
| --- | --- | --- | --- | --- | --- |
| Parameters.eps | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| Parameters.g | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| Parameters.phase_strength | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| Parameters.k[0] | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| Parameters.k[1] | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| Parameters.k[2] | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | k container exactly shape (3,), no broadcasting; reused by residue class for ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:Parameters; _response_numeric.py:real_scalar |
| State.omega | sequence of numeric complex values | Finite real and imaginary components; no bool/string; exact 1D shape. State: (3q,), q>=1. Seed: (3,). | triad requires exactly 3; ring permits 3,6,9,... . No automatic repeat of a triad seed into a ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:State,Seed,_topology |
| Seed.omega | sequence of numeric complex values | Finite real and imaginary components; no bool/string; exact 1D shape. State: (3q,), q>=1. Seed: (3,). | triad requires exactly 3; ring permits 3,6,9,... . No automatic repeat of a triad seed into a ring. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:State,Seed,_topology |
| State.update_index | integer excluding bool | >=0, no API upper bound. | Constructor-zero requires initial update_index=0. Preserve checkpoint index. | TypeError / ValueError | _contract_types.py:_integer; _runner.py:run,resume |
| run.updates | integer excluding bool | >=0, no API upper bound. | Constructor-zero requires initial update_index=0. Preserve checkpoint index. | TypeError / ValueError | _contract_types.py:_integer; _runner.py:run,resume |
| resume.updates | integer excluding bool | >=0, no API upper bound. | Constructor-zero requires initial update_index=0. Preserve checkpoint index. | TypeError / ValueError | _contract_types.py:_integer; _runner.py:run,resume |
| Seed.name | nonempty string | No additional syntax rule. | Observer IDs unique within one run; named preset IDs are their names. | TypeError / ValueError | _contract_types.py; _runner.py:run |
| ObserverRequest.observer_id | nonempty string | No additional syntax rule. | Observer IDs unique within one run; named preset IDs are their names. | TypeError / ValueError | _contract_types.py; _runner.py:run |
| topology | string enum | triad or ring | Ring run requires observers=(), readouts=(), diagnostics=(). | TypeError / ValueError | _runner.py:run |
| historical_seed.name | string enum | Seed: gate_torus_seed_v1. Observer: paper_e_staged_v1 or paper_e_ema_v1. | Initialization labelled historical must preserve exact seed binary64 values; edited seeds become user_supplied. | TypeError / ValueError | _presets.py; _runner.py:run |
| historical_observer.name | string enum | Seed: gate_torus_seed_v1. Observer: paper_e_staged_v1 or paper_e_ema_v1. | Initialization labelled historical must preserve exact seed binary64 values; edited seeds become user_supplied. | TypeError / ValueError | _presets.py; _runner.py:run |
| Clock.q | integer excluding bool | All signed integers, no min/max. | Initial q retained; advance returns modulo N. q is not update_index. | TypeError | _contract_types.py:Clock; z_manifold.py:advance_clock |
| Clock.q_step | integer excluding bool | All signed integers, no min/max. | Initial q retained; advance returns modulo N. q is not update_index. | TypeError | _contract_types.py:Clock; z_manifold.py:advance_clock |
| Clock.N | integer excluding bool | >=1; no API maximum. | Coordinate-history N must be explicit and consistent with the chosen observer; empty history still validates N. | TypeError / ValueError | _contract_types.py:Clock; api.py; z_diagnostics.py:_history |
| display.N | integer excluding bool | >=1; no API maximum. | Coordinate-history N must be explicit and consistent with the chosen observer; empty history still validates N. | TypeError / ValueError | _contract_types.py:Clock; api.py; z_diagnostics.py:_history |
| Clock.t | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | dt may be negative/zero; not dynamics timestep. Nonzero dt that cannot change t raises a precision error. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py:advance_clock |
| ObserverRequest.dt | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | dt may be negative/zero; not dynamics timestep. Nonzero dt that cannot change t raises a precision error. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py:advance_clock |
| advance_clock.dt | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | dt may be negative/zero; not dynamics timestep. Nonzero dt that cannot change t raises a precision error. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py:advance_clock |
| StagedConfig.lambda_vp | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| StagedConfig.gamma | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| StagedConfig.theta_lock | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| StagedConfig.alpha | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| StagedConfig.beta | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| EMAConfig.lambda_vp | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| EMAConfig.theta_lock | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| EMAConfig.alpha | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| EMAConfig.beta | real scalar | numbers.Real -> finite binary64; no bool, string or complex at API boundary. Signed values and zero allowed; no further scientific range. A nonzero value lost on conversion raises ResponsePrecisionError. | theta_lock in radians, not wrapped to UI range; gamma field does not exist for EMA. Valid inputs do not promise successful envelope/readout numerics. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py; z_manifold.py |
| EMAState.m | real scalar | Finite binary64 in [-1,1], historical bounded-memory profile. | EMA request requires EMAState; staged memory must be None. Constructor-zero EMA requires m=0. | TypeError / ValueError / ResponsePrecisionError | _contract_types.py:ObserverRequest; z_manifold.py:EMAState |
| ObserverRequest.config | public typed objects | StagedConfig or EMAConfig; Clock; EMAState or None; Provenance. | No dict passed as a substitute; adapter constructs explicit types. Variant is derived from config type. | TypeError / ValueError | _contract_types.py:ObserverRequest |
| ObserverRequest.clock | public typed objects | StagedConfig or EMAConfig; Clock; EMAState or None; Provenance. | No dict passed as a substitute; adapter constructs explicit types. Variant is derived from config type. | TypeError / ValueError | _contract_types.py:ObserverRequest |
| ObserverRequest.memory | public typed objects | StagedConfig or EMAConfig; Clock; EMAState or None; Provenance. | No dict passed as a substitute; adapter constructs explicit types. Variant is derived from config type. | TypeError / ValueError | _contract_types.py:ObserverRequest |
| ObserverRequest.provenance | public typed objects | StagedConfig or EMAConfig; Clock; EMAState or None; Provenance. | No dict passed as a substitute; adapter constructs explicit types. Variant is derived from config type. | TypeError / ValueError | _contract_types.py:ObserverRequest |
| ObserverRequest.initialization | string enum | recomputed or historical_constructor_zero | Constructor-zero only at update index 0 with zero EMA memory; raw requested z_chiral remains independently evaluated. | TypeError / ValueError | _runner.py:run,_observe; _contract_types.py:ObserverRequest |
| run.observers | explicit tuples | ObserverRequest tuple; unique string tuples from exact registries. Empty is permitted. | readout_accounting/historical_alignment require observers; all selections empty for ring. | TypeError / ValueError | _runner.py:_selection,run; _records.py registries |
| run.readouts | explicit tuples | ObserverRequest tuple; unique string tuples from exact registries. Empty is permitted. | readout_accounting/historical_alignment require observers; all selections empty for ring. | TypeError / ValueError | _runner.py:_selection,run; _records.py registries |
| run.diagnostics | explicit tuples | ObserverRequest tuple; unique string tuples from exact registries. Empty is permitted. | readout_accounting/historical_alignment require observers; all selections empty for ring. | TypeError / ValueError | _runner.py:_selection,run; _records.py registries |
| Provenance.kind | string enum | user_supplied, historical_preset, accepted_definition, checkpoint | UI derives kind from actual action; accepted_definition geometry is kernel-produced. Named historical observer IDs restricted during run. | TypeError / ValueError | _contract_types.py:Provenance; _runner.py:run |
| Provenance.source_id | nonempty string | No API URI/format restriction. | UI describes actual origin, not invented certification. | TypeError / ValueError | _contract_types.py:Provenance |
| Provenance.locator | nonempty string | No API URI/format restriction. | UI describes actual origin, not invented certification. | TypeError / ValueError | _contract_types.py:Provenance |
| Provenance.source_revision | None or nonempty string | No commit syntax imposed on this descriptor. | Do not confuse descriptor revision with record implementation.commit. | TypeError / ValueError | _contract_types.py:Provenance |
| Provenance.notes | string | May be empty. | Preset modifications preserve original source in notes/session lineage, without retaining an inaccurate historical label. | TypeError | _contract_types.py:Provenance |
| Provenance.literal_values | mapping of strings to strings | Keys nonempty; value strings may be empty. Copied/detached. | Record source spellings; do not substitute displayed rounded values. | TypeError / ValueError | _contract_types.py:Provenance |
| get_geometry.definition_id | C01/D03 string; mapping | Exact required keys only; no unknown/missing options. | Geometry type and construction determine option set below. | TypeError / ValueError | _geometry_records.py:get_geometry,_keys |
| get_geometry.options | C01/D03 string; mapping | Exact required keys only; no unknown/missing options. | Geometry type and construction determine option set below. | TypeError / ValueError | _geometry_records.py:get_geometry,_keys |
| C01.section_heights | list of exact numeric values | Each \|h\| <= (sqrt(2)-1)/2, provably; empty, repeated and ordered heights allowed. | C01 width=1, s=sqrt(2)-1 and beta=pi/3 are fixed, not options. | TypeError / ValueError | _geometry_records.py:get_geometry; geometry.py:central_section |
| D03.construction | string enum | aligned, from_radius, regular, paper_c_member, translate_paper_c_to_regular, shrink_paper_c_at_fixed_centres | aligned: s,g_gap; from_radius: s,p; other four: s. No extra keys. | TypeError / ValueError | _geometry_records.py:_CONSTRUCTIONS,get_geometry |
| D03.s | exact integer/Fraction/allowed SymPy expression | s>0, g_gap>0; p must satisfy p>s/(2*sqrt(3)), not merely p>0. | Only fields belonging to the selected construction. g_gap is geometric reference length, not recurrence g. Undecidable positivity is rejected. | TypeError / ValueError | reference_scaffold.py:_positive,ReferenceScaffold.from_radius |
| D03.g_gap | exact integer/Fraction/allowed SymPy expression | s>0, g_gap>0; p must satisfy p>s/(2*sqrt(3)), not merely p>0. | Only fields belonging to the selected construction. g_gap is geometric reference length, not recurrence g. Undecidable positivity is rejected. | TypeError / ValueError | reference_scaffold.py:_positive,ReferenceScaffold.from_radius |
| D03.p | exact integer/Fraction/allowed SymPy expression | s>0, g_gap>0; p must satisfy p>s/(2*sqrt(3)), not merely p>0. | Only fields belonging to the selected construction. g_gap is geometric reference length, not recurrence g. Undecidable positivity is rejected. | TypeError / ValueError | reference_scaffold.py:_positive,ReferenceScaffold.from_radius |
| geometry exact expressions | exact numeric expression | Integers, reduced rationals, pi, Add/Mul, rational powers, sin/cos in Exact Codec 1 subset; no free symbols, sp.Float, Python float, bool or string directly to API. | Worker parses an application-owned restricted numeric grammar into explicit exact objects; no eval or general sympify(text). API remains final domain validator. | TypeError / ValueError | _geometry_records.py:_exact,_exact_input |
| quadratic_form.vector | finite real shape (3,) | Exact shape, checked real entries; no normalization or clipping by UI. | Historical alignment exposes resolution flags; zero/unresolved is not orthogonality. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:_array,quadratic_form,historical_alignment |
| historical_alignment.macro | finite real shape (3,) | Exact shape, checked real entries; no normalization or clipping by UI. | Historical alignment exposes resolution flags; zero/unresolved is not orthogonality. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:_array,quadratic_form,historical_alignment |
| historical_alignment.chiral | finite real shape (3,) | Exact shape, checked real entries; no normalization or clipping by UI. | Historical alignment exposes resolution flags; zero/unresolved is not orthogonality. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:_array,quadratic_form,historical_alignment |
| historical_alignment.total_vector | finite real shape (3,) | Exact shape, checked real entries; no normalization or clipping by UI. | Historical alignment exposes resolution flags; zero/unresolved is not orthogonality. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:_array,quadratic_form,historical_alignment |
| readout_accounting.readout | ZReadout and explicit real scalars | Public returned readout; alpha,beta finite signed reals. | No repair of a stored blend; accounting may expose residuals. | TypeError / ValueError / ResponsePrecisionError | api.py; z_diagnostics.py:readout_accounting |
| readout_accounting.alpha | ZReadout and explicit real scalars | Public returned readout; alpha,beta finite signed reals. | No repair of a stored blend; accounting may expose residuals. | TypeError / ValueError / ResponsePrecisionError | api.py; z_diagnostics.py:readout_accounting |
| readout_accounting.beta | ZReadout and explicit real scalars | Public returned readout; alpha,beta finite signed reals. | No repair of a stored blend; accounting may expose residuals. | TypeError / ValueError / ResponsePrecisionError | api.py; z_diagnostics.py:readout_accounting |
| observe_*.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| advance_ema.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| z_chiral.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| chiral_area_accounting.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| intensity_budget.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| potential.omega | complex triple | Finite complex shape (3,), no ring aggregate implied. | Relevant public Clock/config/memory/Parameters required. Passive numerical domain can be stricter than State. | TypeError / ValueError / ResponsePrecisionError | api.py; _contract_types.py:_triad |
| direct_history_coordinates.history | mapping; string key | Selected finite real array shape (n,3). Empty (0,3) allowed. | Missing Z_total may use Z_vec; any other missing key raises KeyError. No implicit resampling. | TypeError / ValueError / KeyError / ResponsePrecisionError | z_diagnostics.py:direct_history_coordinates |
| direct_history_coordinates.key | mapping; string key | Selected finite real array shape (n,3). Empty (0,3) allowed. | Missing Z_total may use Z_vec; any other missing key raises KeyError. No implicit resampling. | TypeError / ValueError / KeyError / ResponsePrecisionError | z_diagnostics.py:direct_history_coordinates |
| cylinder_point.kappa | real kappa>=0; finite real z; signed integer q | No upper range; explicit positive integer N. | kappa=0 does not discard scalar z. | TypeError / ValueError / ResponsePrecisionError | api.py:cylinder_point; z_diagnostics.py:cylinder_point |
| cylinder_point.z | real kappa>=0; finite real z; signed integer q | No upper range; explicit positive integer N. | kappa=0 does not discard scalar z. | TypeError / ValueError / ResponsePrecisionError | api.py:cylinder_point; z_diagnostics.py:cylinder_point |
| cylinder_point.q | real kappa>=0; finite real z; signed integer q | No upper range; explicit positive integer N. | kappa=0 does not discard scalar z. | TypeError / ValueError / ResponsePrecisionError | api.py:cylinder_point; z_diagnostics.py:cylinder_point |
| cylinder_history_coordinates.history | mapping with kappa,z,phi_index | Equally sized one-dimensional arrays; nonnegative real kappa, finite real z, integer phi_index (no bool). | Cylinder can be empty; torus must be nonempty. Prepare from one observer/record and label whole-history scope. | TypeError / ValueError / KeyError / ResponsePrecisionError | z_diagnostics.py:_history |
| history_torus_coordinates.history | mapping with kappa,z,phi_index | Equally sized one-dimensional arrays; nonnegative real kappa, finite real z, integer phi_index (no bool). | Cylinder can be empty; torus must be nonempty. Prepare from one observer/record and label whole-history scope. | TypeError / ValueError / KeyError / ResponsePrecisionError | z_diagnostics.py:_history |
| history_torus_coordinates.R | finite real scalars | R > r_max > 0 | Whole supplied history controls normalization; no prefix-by-prefix recomputation during playback. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:history_torus_coordinates |
| history_torus_coordinates.r_max | finite real scalars | R > r_max > 0 | Whole supplied history controls normalization; no prefix-by-prefix recomputation during playback. | TypeError / ValueError / ResponsePrecisionError | z_diagnostics.py:history_torus_coordinates |
| RunRecord.from_json.text | JSON text | Strict keys, versions, canonical integer strings/binary64 hex, exact codec where appropriate, digest, metadata and structural consistency. | Use the public loader; duplicate keys and NaN/Infinity rejected. Loading does not replay scientific equations or verify a cryptographic signature. | TypeError / ValueError (including JSONDecodeError) | _records.py:_parse,_metadata,_Record; _geometry_records.py:GeometryRecord |
| GeometryRecord.from_json.text | JSON text | Strict keys, versions, canonical integer strings/binary64 hex, exact codec where appropriate, digest, metadata and structural consistency. | Use the public loader; duplicate keys and NaN/Infinity rejected. Loading does not replay scientific equations or verify a cryptographic signature. | TypeError / ValueError (including JSONDecodeError) | _records.py:_parse,_metadata,_Record; _geometry_records.py:GeometryRecord |
| Seed.provenance | public Provenance | Required explicit Provenance instance. | All descriptor fields follow the Provenance rows; run applies the historical/checkpoint rules above. | TypeError / ValueError | _contract_types.py:Seed; _runner.py:run |
| run.parameter_provenance | public Provenance | Required explicit Provenance instance. | All descriptor fields follow the Provenance rows; run applies the historical/checkpoint rules above. | TypeError / ValueError | _contract_types.py:Seed; _runner.py:run |
| run.initialization_provenance | public Provenance | Required explicit Provenance instance. | All descriptor fields follow the Provenance rows; run applies the historical/checkpoint rules above. | TypeError / ValueError | _contract_types.py:Seed; _runner.py:run |
| run.initial_state | public State | Required explicit State instance. | Topology rules above apply; step increments update_index and returns a new State. | TypeError / ValueError | _runner.py:run,_step; _contract_types.py:_topology |
| step.state | public State | Required explicit State instance. | Topology rules above apply; step increments update_index and returns a new State. | TypeError / ValueError | _runner.py:run,_step; _contract_types.py:_topology |
| run.parameters | public Parameters | Required explicit Parameters instance. | All four fields follow Parameters rows; no implicit defaults or dictionary substitute. | TypeError | api.py; _runner.py:run,_step |
| step.parameters | public Parameters | Required explicit Parameters instance. | All four fields follow Parameters rows; no implicit defaults or dictionary substitute. | TypeError | api.py; _runner.py:run,_step |
| intensity_budget.parameters | public Parameters | Required explicit Parameters instance. | All four fields follow Parameters rows; no implicit defaults or dictionary substitute. | TypeError | api.py; _runner.py:run,_step |
| potential.parameters | public Parameters | Required explicit Parameters instance. | All four fields follow Parameters rows; no implicit defaults or dictionary substitute. | TypeError | api.py; _runner.py:run,_step |
| resume.record | public RunRecord | Required validated RunRecord instance. | Current commit and module hashes must match; no editable parameter/selection overrides. | TypeError / ValueError | _runner.py:resume |
| advance_clock.clock | public Clock | Required explicit Clock instance. | All four fields follow Clock rows. Observation itself does not advance it. | TypeError | api.py |
| observe_staged.clock | public Clock | Required explicit Clock instance. | All four fields follow Clock rows. Observation itself does not advance it. | TypeError | api.py |
| observe_ema.clock | public Clock | Required explicit Clock instance. | All four fields follow Clock rows. Observation itself does not advance it. | TypeError | api.py |
| observe_staged.config | public StagedConfig | Required explicit StagedConfig instance. | All five fields follow StagedConfig rows. | TypeError | api.py:observe_staged |
| observe_ema.config | public EMAConfig | Required explicit EMAConfig instance. | All four fields follow EMAConfig rows. | TypeError | api.py:observe_ema |
| advance_ema.memory | public EMAState | Required explicit EMAState instance. | Bounded m follows EMAState row; observe_ema does not update memory. | TypeError | api.py |
| observe_ema.memory | public EMAState | Required explicit EMAState instance. | Bounded m follows EMAState row; observe_ema does not update memory. | TypeError | api.py |

## SLIDER MATRIX

Every proposed slider has direct numeric text entry, keyboard operation, an accessible name/value, and a visible domain label. The intervals and steps below are UI policy, never new kernel limits. Typing outside a soft range keeps the value, offers expand/recenter, and does not clamp or snap it. Merely loading a value between ticks must not round it. A drag sets a new explicit draft value; Apply/Run submits it only after review. Sliders do not launch recurrence/geometry on every pointer event.

No scientific fields are preselected on a new blank session. Optional “Load historical reference” actions expose every filled value and its source; geometry example C01 with [] sections or D03 regular with s=1 is similarly explicit. UI example updates=100, camera, palette and playback speed are presentation/UX defaults, not historical laws. The matrix freezes starting visible intervals, not an assertion that every value inside them can be evaluated without overflow or precision failure.

Visible intervals are symmetric around zero for signed coefficients where useful, wide enough to include the cited examples, and use decimal steps that let a pointer reach the historical markers. Count intervals use integer ticks. Positive geometry/display intervals are modest inspection windows, not claimed stability regions. The proposed 100 updates is an opt-in example fill; no blank scientific field is submitted automatically. All unbounded scientific quantities remain constrained only by their documented software representability, labelled SCIENTIFIC_RANGE = UNBOUNDED / NOT SPECIFIED beyond any explicit domain above.

K4b implements sliders for eps/g/phase_strength, each k component and updates; Omega can begin as numeric real/imaginary fields. Observer, exact-geometry and history sliders are K4c work. Geometry ticks produce exact integer/rational/symbolic inputs in the Python adapter; they never pass a float into get_geometry or rationalize a kernel output. The height bound uses the returned canonical resolved parameter and documented central-band constraint, with the kernel performing final validation.

| candidate | scientific_domain | initial_visible_range | step | numeric_text_entry | historical_or_example_marker | log_control | range_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eps | finite signed real | [-0.1,0.1] | 0.001 | Required; retains off-tick/out-of-soft-range values | .05 | No: signed/zero domain | DISPLAY_RANGE_ONLY |
| g | finite signed real | [-0.5,0.5] | 0.005 | Required; retains off-tick/out-of-soft-range values | .2 | No: signed/zero domain | DISPLAY_RANGE_ONLY |
| phase_strength | finite signed real | [-0.05,0.05] | 0.001 | Required; retains off-tick/out-of-soft-range values | 0 and .001 (named reference choices) | Optional later signed-log zoom, never ordinary log across zero | DISPLAY_RANGE_ONLY |
| k[0],k[1],k[2] and equal-k control | finite signed real | [-2,2] | 0.01 | Required; retains off-tick/out-of-soft-range values | 1 (L01 reference) | No mandatory log | DISPLAY_RANGE_ONLY |
| Omega real/imaginary components | finite signed real/imaginary parts | [-1,1] per field | 0.01 | Required; retains off-tick/out-of-soft-range values | Named seed component markers only when selected | Optional magnitude-view log later; never log signed components | DISPLAY_RANGE_ONLY |
| updates | integer >=0 | [0,1000] | 1 | Required; retains off-tick/out-of-soft-range values | None: 100 is an explicitly labelled UI example, not historical science | Optional later coarse count zoom | DISPLAY_RANGE_ONLY |
| Clock.N | integer >=1 | [1,48] | 1 | Required; retains off-tick/out-of-soft-range values | 12 | No | DISPLAY_RANGE_ONLY |
| Clock.q / q_step | signed integers | q [-24,24]; q_step [-12,12] | 1 | Required; retains off-tick/out-of-soft-range values | q=0; q_step=1 | No | DISPLAY_RANGE_ONLY |
| Clock.t / dt | finite signed reals | t [-1,10]; dt [-0.2,0.2] | t 0.1; dt 0.001 | Required; retains off-tick/out-of-soft-range values | t=0; dt=.1 | No: negative/zero are valid | DISPLAY_RANGE_ONLY |
| lambda_vp / staged gamma | finite signed reals | [-1,1] | 0.001 | Required; retains off-tick/out-of-soft-range values | .618 / .577 | No positive-only restriction | DISPLAY_RANGE_ONLY |
| theta_lock | finite real radians | [-pi,pi] for display navigation | 0.001 rad | Required; retains off-tick/out-of-soft-range values | .244 | No; retain entered winding, do not wrap input | DISPLAY_RANGE_ONLY |
| alpha / beta | finite signed reals | [-2,2] | 0.01 | Required; retains off-tick/out-of-soft-range values | 1 / .5 | No | DISPLAY_RANGE_ONLY |
| EMA memory m | finite real, \|m\|<=1 | [-1,1] | 0.01 | Required; retains off-tick/out-of-soft-range values | 0 | No | ENFORCED_HISTORICAL_PROFILE_DOMAIN |
| D03 s / g_gap | exact positive values | s [1/10,3]; g_gap [1/100,3] | 1/100 as exact rational | Required; retains off-tick/out-of-soft-range values | s=1 and regular g_gap=s are explicit example/construction, not physical defaults | Later positive log control useful; numeric exact entry remains authority | DISPLAY_RANGE_ONLY |
| D03 p | exact p>s/(2*sqrt(3)) | [1/100,3], validation may reject part of range for current s | 1/100 exact rational | Required; retains off-tick/out-of-soft-range values | No historical marker | Later positive log optional | DISPLAY_RANGE_ONLY |
| C01 section height h | exact \|h\|<=s/2 | [-s/2,s/2] from the canonical public record resolved s | s/100; integer tick -50..50 resolved to exact expression in Python | Required; retains off-tick/out-of-soft-range values | h=0 is a section example | No | ENFORCED_GEOMETRY_DOMAIN; tick spacing is display convenience |
| history R / r_max | finite real R>r_max>0 | R [0.1,5]; r_max [0.1,2] | 0.1 | Required; retains off-tick/out-of-soft-range values | R=2,r_max=1 (L06 display convention) | Later positive log optional, retain cross-field validation | DISPLAY_RANGE_ONLY |
| display kappa / z | kappa>=0; z finite signed | kappa [0,2]; z [-1,1] | 0.01 | Required; retains off-tick/out-of-soft-range values | None | Positive-only kappa log can help later, with a separate zero control | DISPLAY_RANGE_ONLY |

## HISTORICAL PRESET MATRIX

USER VALUE and HISTORICAL PRESET VALUE are distinct visible badges. Applying a preset copies explicit public values into the draft and records the returned/cited provenance. Editing any field makes the affected configuration user-supplied; retain preset origin and changed-field list in the session and truthful provenance notes. Never leave an edited seed labelled gate_torus_seed_v1. Kernel validation checks that historical seed's literal Omega; UI honesty must also cover observer/parameter provenance beyond what the kernel happens to enforce.

O02 explanatory text: “Historical preset. Recorded provenance known. Original design rationale unresolved.” No claims of physical optimality, preferred scientific coupling or natural constants. .618 is a literal, not a golden-ratio substitution; .244 is a lock angle here, not the excluded SRG clock_fraction. Phase strength lambda, observer lambda_vp and geometry g_gap keep distinct labels.

| preset_or_literal | exact_visible_values | source_and_materialization | qualification |
| --- | --- | --- | --- |
| gate_torus_seed_v1 | (0.2+0.3j,-0.4+0.1j,0.1-0.2j) | api.historical_seed; returned provenance source revision 3d9e2c24f2cd9207242e16559558c6adabb21c04; L02 | Binary64 replay values; exact rational reading in Paper F is a separate algebraic scope. No seed normalization. |
| paper_e_staged_v1 | lambda_vp=.618, gamma=.577, theta_lock=.244, alpha=1, beta=.5; q=0,N=12,t=0,q_step=1,dt=.1; memory=None; initialization=recomputed | api.historical_observer; L03/L04 | Named run preset, not constructor-zero replay; original lock rationale O02. |
| paper_e_ema_v1 | lambda_vp=.618, theta_lock=.244, alpha=1, beta=.5; q=0,N=12,t=0,q_step=1,dt=.1,m=0; initialization=recomputed | api.historical_observer; L03/L04 | No gamma. Fixed EMA innovation .01 is not a UI parameter. |
| L01 reference parameter fill | eps=.05,g=.2,k=(1,1,1); explicit choice of phase_strength=0 or .001 | UI assembly of public Parameters + explicit Provenance citing K0 ledger L01 and accepted experiment evidence; there is no historical_parameters API registry. | Reference convenience, not a new kernel preset ID or hidden default; O02 remains open for eps/g. |
| Historical constructor-zero mode | Initial observer z and M/C/T stored as zero; zero EMA memory; initial update index 0 | ObserverRequest.initialization=historical_constructor_zero; E05 | Advanced explicit replay option; requested raw chirality can be nonzero at that same initial sample. |
| L06 display conventions | alignment threshold 1e-12, torus regularizer 1e-9; explicit display R=2,r_max=1,N=12 | Public returned flags/HistoryTorus metadata; read-only fixed thresholds | Threshold/regularizer are not tunable UI laws. Whole-history normalization and floating inverse qualifications remain visible. |

## Complex-state and k-vector editors

Authoritative editable state representation is an ordered array of real/imaginary numeric pairs, resolved once to Python complex values. The triad editor shows Omega0, Omega1, Omega2. An advanced ring editor shows all 3q components with exact row count; it never silently repeats, normalizes, projects or pads a seed. Preserve update_index separately. Seed selection uses the public helper, and preset provenance remains available beside the fields.

Magnitude/phase is useful as an optional derived read-only view in the first implementation. A later polar-input mode may be an explicit representation adapter in Python (r>=0, phase in radians, preview the resulting real/imag pair and retain both entry form and resolved values); it cannot be a second live source of State. At exact zero, display phase as undefined/Arg0 convention explained rather than suggesting a measurable phase. Do not use a frontend conversion to overwrite saved binary64 pairs. Read-only formatting/conversion is not a substitute for public scientific outputs.

Independent k0/k1/k2 fields are always inspectable. Equal-k mode is a convenience to fill all three from one typed value; enabling it when entries differ requires choosing the value explicitly. Disabling it preserves the current triple. No average or preferred k is inferred. The actual submitted Parameters.k tuple, including unequal values, is shown before run. k is an amplitude coefficient triple, not a wave vector or spatial axis selector.

## OUTPUT / VISUALIZATION MAP

Tables and charts are views of returned data. Any result not requested/stored is marked “not recorded”; do not call science during repaint to fill the gap. The user may explicitly request a separate passive analysis against a stored triad, producing a cache with parent digest, sample indices, input/configuration and function name. Such a cache is not a RunRecord. Playback then consumes stored/cached display data only.

All fields of each diagnostic/result below must remain inspectable, even when only a subset is plotted initially. There is no new public export for these internal result class names: consume attributes of public function results or public record dictionaries. Finite precision qualifications and resolution booleans accompany plotted numbers.

GeometryRecord validates the optional render member's shape/types, not a mathematical proof that its floats equal the exact nodes. The producer currently emits exact data without render. Build a detached display payload from the validated exact data in the Python adapter; treat any supplied render values as labelled derived data, never authority. Allowed adapter operations are exact-node reconstruction, numerical evaluation at an explicit display precision, row/series formatting and camera projection. No vertex construction, geometry intersections, welding, topology inference or recurrence formulas are implemented in a viewer.

| quantity | source | visual_form | qualification | capability_class |
| --- | --- | --- | --- | --- |
| Omega and update index | RunRecord.samples[*].omega/update_index | Re/Im time series, one complex plane per channel, exact value table | Use stored component pairs; x-axis is update index, not Clock.t. No interpolation labelled as a computed state. | SUPPORTED_FROM_PUBLIC_RECORD |
| Raw chirality C | samples[*].raw_readouts.z_chiral or explicit api.z_chiral result | Cx/Cy/Cz time series, vector glyph, channel-space 3D trace | Raw (BC,CA,AB) pseudovector; no normalization, ambient field or shell position. Not available for ring run selections. | SUPPORTED_FROM_PUBLIC_RECORD |
| Observer scalar and vectors | samples[*].observer_results[id].z,Z_macro,Z_chiral,Z_total,variant,initialization | Scalar/vector series and paired decomposition tables | Historical constructor-zero row stays labelled; raw C and stored observer Z_chiral are distinct selections. | SUPPORTED_FROM_PUBLIC_RECORD |
| Observer clock/memory | samples[*].observer_states[id].q,t,m,observer_update_count | Read-only state timeline/table | Do not regenerate t from dt*index or q from index. Independent observers have independent clocks. | SUPPORTED_FROM_PUBLIC_RECORD |
| Norm/intensity views | chiral_area_accounting.intensity/chiral_norm; intensity_budget.component_intensities/intensity_before; readout_accounting.*_norm_squared | Time series with exact field provenance | Prefer requested public fields. Optional sqrt of an existing nonnegative public intensity is a labelled display conversion in Python; do not silently recompute a missing diagnostic. | SUPPORTED_FROM_PUBLIC_RECORD |
| Channel magnitude/phase presentation | Stored Omega pairs; existing public component intensities where selected | Optional magnitude/phase view | Representation-only Python view conversion; prefer public intensity fields when present. Not a new norm/phase diagnostic or physical observable; preserve original bits. | DISPLAY_DERIVATION_ONLY |
| All passive accounting fields | Full result dataclass fields listed below, or stored diagnostic dictionaries | Tables, signed terms/residual plots, resolution badges | Keep signs and flags; do not clamp small residuals or label zero as proof of exact equality. Pre-sync prediction never feeds step. | SUPPORTED_FROM_PUBLIC_RECORD |
| Q(vector) | api.quadratic_form on explicitly selected returned vector | Scalar/table, optional cached series | Standalone explicit analysis, not a run diagnostic ID or physical energy. | SUPPORTED_DIRECTLY |
| Direct M/C/T path | api.direct_history_coordinates on columns assembled from one record/observer | x/y/z trajectory in labelled observer-vector coordinates | Column assembly is formatting; coordinates come from the public helper. | SUPPORTED_DIRECTLY |
| Cylinder/scalar-history torus | api.cylinder_point/cylinder_history_coordinates/history_torus_coordinates | Separate display-coordinate view | History assembly is explicit. kappa may be a labelled Python display conversion sqrt(stored public intensity); if absent request passive analysis explicitly. No private state_norm import. Torus normalization over entire selected history, cached once. | SUPPORTED_DIRECTLY |
| C01 shell and sections | GeometryRecord.objects plus coordinates/resolved_parameters/symmetry | Exact expression inspector, incidence tables, 3D wireframe/section segments | 18 vertices,21 edges,3 oriented octagonal faces,3 seam edges,18 boundary edges,2 boundary loops,Euler=0. No invented caps, volume or dynamics colouring. | SUPPORTED_FROM_PUBLIC_RECORD |
| D03 scaffold | GeometryRecord.objects with distinct frame_id and object roles | Planar polygons/halfplane boundaries, 3D vertical reference frames, exact metrics | 12 objects: octagon, scaffold, support triangle,3 corner cells,3 planar frames,3 vertical frames. E/G roles, D3/C3 and conditional unlabelled D6 retained. | SUPPORTED_FROM_PUBLIC_RECORD |
| Geometry numeric view payload | Allowed exact expression trees in public record data | Detached numeric vertices/segments plus camera projection and precision tag | get_geometry does not populate optional render. Python adapter evaluates only serialized exact values for drawing; does not reconstruct geometry. Never modify/re-sign GeometryRecord to insert view data. | DISPLAY_DERIVATION_ONLY |
| Record trust/provenance | Public data, deterministic_sha256, execution_metadata | Structured inspector plus optional canonical raw JSON | Record content validation is separate from current implementation compatibility and scientific replay. | SUPPORTED_FROM_PUBLIC_RECORD |

| returned_type | fields | control_class | source |
| --- | --- | --- | --- |
| ReadoutAccounting | alpha, beta, variant, initialization, supplied_z, macro_norm_squared, chiral_norm_squared, total_norm_squared, weighted_macro, weighted_chiral, cross_term, predicted_norm_squared, norm_residual, blend_residual, q_macro, q_chiral, q_total, q_weighted_macro, q_weighted_chiral, q_cross_term, q_prediction, q_residual, macro_relation_residual | READ_ONLY | kernel_physics/z_diagnostics.py:82 |
| ChiralAreaAccounting | chiral, A, B, h, intensity, chiral_norm, chiral_norm_squared, gram_product, h_squared, gram_rhs, gram_residual, amplitude_bound, slack_sum_of_squares, observed_slack, slack_residual | READ_ONLY | kernel_physics/z_diagnostics.py:145 |
| HistoricalAlignment | d_TM, d_CM, d_TC, macro_resolved, chiral_resolved, total_resolved, TM_resolved, CM_resolved, TC_resolved, threshold | READ_ONLY | kernel_physics/z_diagnostics.py:186 |
| IntensityBudget | component_intensities, intensity_before, increment, diagnostic_pre_sync_prediction, intensity_pre_sync, pair_distance_sum, onsite, coupling, remainder, predicted_delta, observed_delta, residual | READ_ONLY | kernel_physics/z_diagnostics.py:237 |
| Coordinates | x, y, z | READ_ONLY | kernel_physics/z_diagnostics.py:306 |
| HistoryTorus | x, y, z, r, chi, z_max, H_z, regularizer, R, r_max, N, normalization | READ_ONLY | kernel_physics/z_diagnostics.py:369 |
| ZReadout | z, Z_macro, Z_chiral, Z_total, variant, initialization | READ_ONLY | kernel_physics/z_manifold.py:165 |

## GEOMETRY-DYNAMICS SEPARATION and 3D requirements

Omega dynamics != geometry coordinate. Chirality != geometry field. RunRecord != GeometryRecord. No accepted Omega-to-shell-placement dictionary exists. A side-by-side layout displays “Independent geometry — no dynamic attachment” beside C and “Channel/observer coordinates — not physical placement” beside dynamics vectors. VISUAL COEXISTENCE != SCIENTIFIC COUPLING. Selection/linking by sample index must not create a relation with geometry vertices.

C01 faces are oriented panels with open boundaries; D03 frame hulls are separate closed reference sets, not a welded solid. Frontend triangulation solely for filling an already returned face is a display tessellation, not new incidence, physics or volume; wireframe is sufficient for K4b. Use object IDs/returned edges/face cycles and coordinate frame labels. Axis arrows/camera changes are presentation. Expose normal/fold angle distinctions and the scaffold's role-preserving symmetry qualifications. A Paper-C member comparison is finite-face geometry only; it never supplies Omega attachment.

D03 generated hull vertices are cyclic (reference_scaffold.ConvexHull contract); drawing successive returned vertices and the closing segment is display adaptation, not a new convex-hull algorithm. Prefer explicit returned outline/selected_edges/connectors where provided. Show halfplane normals/offsets in the inspector; do not solve intersections in the UI to regenerate the scaffold. Imported shape/digest validation alone does not certify the producer's geometric claims.

The first geometry view is CPU-rendered wireframe with rotation, pan/zoom, reset camera, labelled axes and a complete exact/vertex/edge table alternative. Matplotlib mplot3d is suitable for this small first view, not a claim of unrestricted solid-model visualization: depth-order/occlusion limits must be visible in planning. K4c can add a richer renderer after measured needs, with an equivalent CPU/table fallback; GPU/model/network must remain unnecessary for supported use.

| proposed_3D_element | class | source_or_disposition |
| --- | --- | --- |
| C01 shell vertices, edges, oriented panel cycles, seams and requested section curves | EXACT_GEOMETRY | Returned exact coordinates/incidence; displayed floating projection is a derived view. |
| D03 octagon/scaffold/hulls/planar and vertical frames | EXACT_GEOMETRY | Returned object data and separate coordinate frames; no joining distinct objects. |
| Raw chirality arrow/path and observer M/C/T traces | DERIVED_DISPLAY | Public numerical vectors in labelled channel/observer coordinate space. |
| Cylinder and history-torus point/path output | DERIVED_DISPLAY | Public display helpers; entire-history normalization; no inverse or mechanical interpretation. |
| Camera, axes, grid, selection highlight, decorative guide torus | DECORATIVE | Visual aids only, switchable; guide surface never presented as material occupied by Omega. |
| Twisted crystal, EM/RS field, warp/spring/finite-patch models | RESEARCH_ONLY | No executable control or authoritative rendering claim. |
| Omega on shell vertices; chirality field painted over panels; geometry feeding dynamics | UNSUPPORTED_MAPPING | No accepted dictionary/coupling; excluded. |

## Run, playback, comparison and immutability contract

Run submits a frozen request snapshot to api.run once. Zero updates returns one initial sample including explicitly requested initial observations/diagnostics. One update returns two samples. n updates returns n+1 samples; initial update_index need not be zero for an explicit checkpoint. Each selected observer advances once after each new Omega; diagnostics stay passive. If any requested operation fails, no complete record is accepted; the prior completed record and editable draft survive unchanged. Selecting fewer diagnostics after a precision error is a new explicit request, not an automatic retry with hidden outputs removed.

Resume calls api.resume(record, updates=n) with no parameter/config overrides. It returns a new immutable record with unchanged sample prefix, no duplicated junction sample, continuation parent digest and new producer segment. Resume with zero updates preserves samples but still creates continuation/metadata: it is not a read-only identity probe. Current source commit and module hashes must match. Environment changes are recorded but do not promise cross-platform bitwise reproduction. Preserve every parent record separately.

“New run from checkpoint state” copies the selected stored binary64 Omega and update_index through the public State constructor, supplies the new explicit Parameters/selections and checkpoint Provenance, and calls run. Put the parent digest and selected sample in provenance source_id/locator/literal_values and UI lineage; do not invent or insert initialization.parent_digest, which run does not currently populate. Observer clocks/memory must be explicitly preserved or reinitialized in the new draft. A parameter edit never alters or masquerades as continuation of the old record.

Playback is play/pause/forward/back/scrub over stored sample ordinals; show the actual update_index. Sample selection is O(1) over a cached view, without repeated record.data parsing or kernel calls. Distinguish playback speed (frames per wall-clock second) from Clock.dt and dynamics updates. Do not fabricate intermediate scientific samples. Resume produces a new digest/cache; a torus display is recalculated once on explicit view preparation for the new entire history, never silently renormalized during scrubbing. Display-only decimation may be labelled with the sampling rule and selected exact sample values; never truncate authoritative exports.

Comparison uses separate immutable records with a request/provenance difference panel. Support two parameter sets, seeds, phase_strength=0 versus nonzero, compatible update-index alignment, and separate geometry requests. Ring versus triad comparison is only on comparable recorded quantities; no ring chirality or lifted-sector identification is inferred. Different lengths/indices/observer clocks are shown, not silently resampled. Descriptive differences have no “better trajectory” score. Explicit scientific replay is a separate later operation, not loading or playback; compare against source/environment-qualified expectations, not an invented universal tolerance.

## RECORD / PROVENANCE UX

Four distinct states: Draft configuration; Completed current record; Loaded validated record; Modified draft derived from record. Controls affect only Draft. A completed or loaded record remains labelled by its original parameters and source. Running a modified draft creates a new record and keeps the prior record. Use “Save RunRecord JSON”, “Save GeometryRecord JSON” and “Save draft configuration” as separate commands. Dirty draft and unsaved completed-record badges are independent. Saving never edits record content; cancellation/failure never overwrites the last complete record.

Use api.RunRecord.from_json or api.GeometryRecord.from_json to validate imports in a worker, and preserve the canonical returned to_json text for export. Verify deterministic_sha256 via that loader, not a second frontend hash implementation. The digest excludes execution_metadata and itself; it is not the SHA of the whole file, a signature, proof of origin, or a mathematical replay certificate. Never show “certified” solely because a user-loaded record has a valid self-consistent digest. Use statuses “Structure/digest valid”, “Producer claims inspected”, “Current resume compatibility not checked”, “Resume accepted/rejected” and optional later “Explicit replay checked”.

Always visible: record kind, source commit abbreviation, digest abbreviation, saved status, and passive/separate-geometry badges. Expandable: full repository/commit, package/API/schema/ledger versions, 14 implementation module path/hash entries, parameter/initialization/observer or construction provenance, all paper reference IDs/editions/paths/hashes, exact inputs, and every execution environment/segment (Python, NumPy, SymPy, mpmath, platform, architecture, byteorder and optional timestamp). Producer environment is not the viewer environment. Imported timestamps are not authenticated by the deterministic digest.

Current package version can be read using standard installed distribution metadata. There is no public standalone current source/provenance query; until a current public operation returns a record, show current source identity as unknown rather than reading private manifest internals or presenting a loaded record's identity as the runtime's. Resume itself is authoritative about compatibility. Package version 0.1.0 alone is insufficient. The future UI should use an installed certified kernel artifact, not the changing repository checkout, because provenance refuses a dirty tracked source and source commits affect resume identity.

Render unavailable/missing data explicitly. When a loaded record lacks a requested series, show “not recorded”; a view operation cannot insert it. Plain canonical JSON is available beside structured fields. Full exact expressions and codec spellings remain inspectable even when table/chart labels use rounded decimals. Record loading is portable without Git, papers or network; new production still requires valid current source or installed provenance.

## Data flow and reproducible UI request

Frozen flow: controls -> immutable UI request snapshot -> Python input/representation adapter in worker -> kernel_physics.api -> returned State/RunRecord/GeometryRecord -> detached view model -> render only. No renderer state is a scientific authority. Source/implementation metadata comes from public records; application job IDs and app version stay in the UI envelope. The application never imports a private scientific module, calls eval on input, normalizes an Omega, or constructs an alternative next state from a diagnostic prediction.

Maintain a versioned UI/session request, outside kernel schemas. Fields: ui_request_version, operation (run/resume/geometry/passive_analysis), state (ordered real/imag entry strings and explicit index), parameters (all four fields with explicit k triple), topology, updates, ordered observer requests with config/clock/memory/dt/initialization/provenance, readouts, diagnostics, parameter and initialization provenance, and for geometry an independent definition_id/options request. A resume request carries the parent canonical record/digest reference and updates only; edited parameters are not permitted in that operation. A passive-analysis request identifies parent digest, sample indices, function and explicit arguments. Empty lists are explicit, converted to API tuples in Python.

Retain both original input spellings and the resolved numeric request shown before execution. The adapter rejects NaN/Infinity, malformed numbers and detectable nonzero decimal underflow to zero; conversion to binary64 is explicit, not silent coercion of API strings. Reproduction from saved records uses their documented hex float encoding to preserve signed zero and exact stored bits. Geometry request numbers use a small tagged exact grammar (integer/rational plus the allowed numeric pi/add/mul/rational-power/sin/cos nodes); text entry is translated to that grammar in Python with bounded expression complexity. No arbitrary expression evaluation/import/call is accepted.

Session-only fields include view/camera/series selections, draft origin, parent digest/sample index, app version and user file references. They never become extra RunRecord/GeometryRecord keys. The UI envelope may evolve independently under its own version. Chart rows and numeric exact-geometry conversion are formatting/representation adapters, not reasons to change the public facade. Validate returned records with their public loaders before marking a worker result complete. Save the canonical record independently from the draft request.

## EXPORT / DATASET CONTRACT

DATASET_CONTRACT = FROZEN_DESIGN; IMPLEMENTATION = DEFERRED_TO_K4d. K4b includes public record JSON and explicit draft/session request JSON. Later presentation exports are separate files with a sidecar or embedded reference identifying parent record digest, source commit, selected fields/indices, formatting/precision, display normalization and application version. A screenshot must never appear to be a new authoritative kernel artifact.

Future sweeps accept one or more explicit finite parameter value lists, one explicit seed/state, topology, update count and selected outputs. A range specification must first expand to a visible finite ordered list with exact endpoint/count policy and resolved binary64 values; no open-ended “until stable” search. Product size is calculated before submission; enumeration order and case IDs are stable and independent of execution scheduling. Each case calls public run and returns a separate complete record or a failure entry. Failed/cancelled cases are not silently dropped or replaced by zeros. No scientific score chooses a winner.

Sweep manifest is application/session data: schema/version, app version, all explicit expanded requests, source artifact/commit identity, environment, row/case count estimates, ordered case IDs, per-case record digest and path, result status or original error/cancellation, and any presentation export references. Do not label it a new kernel record. Dataset continuation may skip an already verified completed case only when the explicit request/record identity matches; it never resumes a failed partial RunRecord.

| export | authority | required_label_and_content | phase |
| --- | --- | --- | --- |
| RunRecord JSON | Authoritative public kernel artifact | Canonical api.RunRecord.to_json output, untouched deterministic digest/metadata. | K4b |
| GeometryRecord JSON | Authoritative public kernel artifact | Canonical api.GeometryRecord.to_json output; exact data remains authoritative. | K4b |
| UI request/config JSON | Application/session data | Explicit choices, representation spellings/resolved values and app version; not a kernel record. | K4b |
| CSV samples | Derived presentation | One row per selected stored sample with index/observer IDs; split complex re/im columns; no scientific recomputation; sidecar with parent digest and field units/codec/precision. Full-precision numeric or hex companions when needed. | K4d |
| PNG/SVG | Derived presentation | Record digest/source, selected sample/range, axes, projection/normalization and display precision; no physical interpretation implied. SVG may contain rasterized layers; identify them. | K4d |
| Finite sweep manifest + record collection | Application manifest plus authoritative per-case records | Explicit Cartesian product, status of every requested case, deterministic enumeration and exact input/record links. | K4d |

## Run bounds, responsiveness and cancellation

The runner appends every sample in memory, then encodes/validates/canonicalizes the complete record. _Record.data reparses and freezes its JSON on each access; cache one detached view model rather than repeatedly accessing it per frame. Resume parses/copies the full prior record before appending. Record size depends on state width, observers and diagnostic selection; there is no streaming API, fixed scientific update ceiling, trustworthy percentage-progress callback, or built-in partial-result cancellation.

Freeze initial UI policy (software safeguards, not scientific domains): one active computation job; visible estimate n+1 samples for new runs, existing_samples+n for resume; explicit confirmation above 10,000 total samples; for future sweeps, confirmation above 100 cases or 100,000 total samples. Display a conservative “size depends on selected outputs” warning rather than fabricate a byte/time estimate. These thresholds are labelled adjustable application preferences. Never silently clamp updates, delete output fields, truncate record samples, impose a kernel limit, or infer convergence. A large-file/expression parsing guard must identify itself as a UI resource guard with an explicit controlled override path, not a scientific domain rejection.

Use a worker subprocess for every computational/record-load job. UI shows job state (validating/running/completed/failed/cancelled), elapsed wall time and requested sample count; no fake completion percentage. Cancellation terminates only the active worker, with a bounded grace period followed by kill if necessary; treat its staged files as incomplete and never as a saved record. Completed prior records remain intact. Cancellation racing completion is resolved by accepting only one terminal state after validating a complete response; a cancelled job cannot later replace the current selection. Public run is not silently chunked into multiple resumes: that would change continuation/execution metadata and record identity.

Worker response is a typed application envelope with request/job ID, operation, success/failure/cancelled status, canonical completed-record artifact reference or result, and original exception type/message. Use UTF-8 request/response files or framed stdio, no pickle, arbitrary commands or shell evaluation. Stage output to a job-owned temporary file and publish the completed file atomically only after validation. The worker is launched with an absolute installed Python and installed companion entry point under -I -B from an unrelated directory; no source checkout/PYTHONPATH import trick. Keep the companion package initializer inert so the worker imports no Qt/Matplotlib/model/GPU subsystem. Core numerical versions remain the certified pins; GUI dependency resolution may not upgrade them.

| execution_model | determinism_provenance | cancellation_crash_isolation | simplicity_Windows | decision |
| --- | --- | --- | --- | --- |
| UI thread / same process | Public API still authoritative, but long run blocks event loop. | Cannot safely interrupt arbitrary scientific call; crash affects UI. | Simplest initial code, unacceptable responsiveness. | Reject for computations; keep rendering/event handling here. |
| Worker thread | Same address space and environment; return records unchanged. | Cooperative cancel unsupported by run; forced thread termination unsafe, shared crash/memory risk. | Suitable later for small I/O, not a complete run cancellation strategy. | Do not choose as scientific job boundary. |
| Worker subprocess | Explicit request/response and public records; source identity comes from kernel, not IPC. | Kill isolates failed/incomplete job; prior records survive. | Windows-supported process launch, more protocol/error handling, directly testable. | RECOMMENDED; one job process initially. |

## ERROR SURFACE

Translate errors into field/action-specific text while preserving exception class, original message, operation and submitted request ID in expandable/copyable technical details. UI prevalidation may highlight a field; kernel rejection is final. ResponsePrecisionError must be handled before generic FloatingPointError. No automatic clipping, normalization, new seed, changed selection, precision downgrade or fallback geometry/observer may turn a failed request into success. Show the failed draft beside the last valid record.

| error_or_condition | public_trigger | human_surface | recovery_without_changing_science |
| --- | --- | --- | --- |
| TypeError | Wrong numeric/type/container/public object, bool-as-int, geometry float/string, non-text JSON | Name the field and expected type; retain original message. | Correct explicit input/adapter representation. |
| ValueError | Invalid domain/shape/topology/selection, duplicate ID, unknown preset/geometry/option/schema, noncanonical codec/digest | Explain exact rejected constraint and submitted value. | Edit draft or load a supported valid record; no silent substitution. |
| ResponsePrecisionError (FloatingPointError subclass) | Lost nonzero conversion, checked underflow/subnormal/overflow, clock dt lost, observer/diagnostic numerical domain | Requested evaluation exceeds supported numeric domain; do not call it zero or stable decay. | Change inputs or explicitly submit a different output selection; original request remains failed. |
| FloatingPointError / OverflowError | Dynamics arithmetic/serialization numerical failure, nonfinite result | Identify operation and original numerical failure. | No partial record, no hidden normalization; preserve previous record. |
| KeyError | Missing requested history key or malformed adapter input | Missing named data/key, including absent historical series. | Select recorded data or make explicit analysis request. |
| JSONDecodeError (ValueError), schema/digest failure | Malformed/duplicate-key/nonfinite JSON, unsupported record/schema, modified deterministic content | File was not accepted; structure/digest validation failed, with details. | Keep previous selection; import valid file. Never re-sign altered content. |
| FileNotFoundError / OSError / installed-provenance ValueError | Missing manifest/file, tampered installed bytes, dirty/incomplete source evidence | Current installation/source provenance unavailable or inconsistent; distinguish from invalid scientific parameters. | Repair/reinstall an authorized certified artifact outside the scientific request; loaded old records may still decode. |
| resume incompatibility ValueError | Current commit or module hashes differ from recorded implementation | Resume rejected: source revision/module identity mismatch; show record identity and available current identity, retaining original reason. | Explicit New run from checkpoint; never downgrade to version-only matching. |
| AttributeError on record edit | Public immutable record rejects mutation | Application defect if UI attempts record edits. | Create a new draft; preserve record. |
| Worker exit/crash/MemoryError/user cancellation | No complete validated response | Show failed/cancelled job and available stderr, not a scientific success or empty trajectory. | Retry only explicitly; preserve completed artifacts and draft. |

## PUBLIC API GAP ANALYSIS

Four optional future public API gaps are recorded; zero block the first useful UI. Formatting preferences are not API gaps. Absence of a scientific coupling is a substantive unsupported mapping, not permission to create an adapter that supplies one. All stop gates are clear for the recommended first slice: correct authority, clean tracked baseline, no required science/API change, no executable quarantined/research feature, no required network, and no identified license conflict in the proposed separated architecture. Exact third-party artifact/module/license inventory remains a K4b packaging gate before bundling, not a claim already certified in K4a.

| id | classification | capability | evidence | disposition |
| --- | --- | --- | --- | --- |
| G01 | PUBLIC_API_GAP | Live sample streaming, percent progress, cooperative cancellation, recovery of partial run. | run/resume are synchronous and return complete records; no callback/cancel token. | Use process cancellation/indeterminate progress. No first-slice blocker; do not patch kernel. |
| G02 | PUBLIC_API_GAP | Read-only current source/implementation identity and resume preflight before any production. | No public implementation/provenance query export; resume(0) creates a new record. | Show unknown until public result; resume catches authoritative mismatch. No private manifest access. |
| G03 | PUBLIC_API_GAP | Animated explicit D03 symmetry permutation action. | D03 record generator.vertex_permutation is None. | Show descriptive symmetry metadata only. A later bounded API decision is needed for a scientific action, not inferred frontend geometry. |
| G04 | PUBLIC_API_GAP | Arbitrary fold-angle C03 record/interactive folding as accepted geometry. | Facade exposes fixed C01 and D03 only; internal panel_point is not a public record operation. | Keep C01 beta read-only. Later separate exposure decision; no first-slice blocker. |
| F01 | DISPLAY_DERIVATION_ONLY | Chart rows, complex-pair decoding, human labels and exact-node numeric view conversion. | Public records carry all required values; representation adapter suffices. | Not an API gap; no core change. |
| F02 | SUPPORTED_FROM_PUBLIC_RECORD | Playback, saved-sample comparison, structured provenance and CSV extraction. | Records contain samples, inputs and provenance. | No new kernel methods needed. |
| F03 | SUPPORTED_DIRECTLY | Triad runs, passive observers, C01/D03 production, record JSON, compatible resume. | All available through the 34-export facade. | Useful K4b is possible without modifying public API. |
| F04 | DISPLAY_DERIVATION_ONLY | UI finite sweep enumerator, draft presets and checkpoint lineage envelope. | Finite repeated public calls and request metadata, not a new scientific rule. | Defer orchestration to K4d; no need for a batch kernel API. |
| U01 | SCIENTIFICALLY_UNSUPPORTED | Omega/shell placement, chirality geometry field, geometry/dynamics feedback. | No accepted coupling dictionary/law. | Exclude, not an engineering API gap to fill. |
| U02 | SCIENTIFICALLY_UNSUPPORTED | Physical/mechanical meaning for clock, torus trajectory, potential, frame colouring, six-axis selector or research models. | Not established by current public-v1 science. | No executable control/claim; explanatory research links only in a later separately labelled scope. |

## Help, naming and qualifications source map

Every help item carries one class below plus a pinned source/definition ID. Friendly wording is paired with exact terminology: Phase strength (phase_strength), coupling g, Omega state, raw chirality, geometric gap (g_gap). Do not label k as wavenumber, potential as physical energy, dt as dynamics timestep, or a history torus as mechanical motion. Never invent marketing/scientific quantities such as quantum power or warp intensity.

Use concise original help based on these sources, not a bundled copy of excluded paper/research content. A reference ID/path/hash can be displayed offline from the record without opening the paper. Opening an external source is an optional explicit user action, never needed for computation. Paper editions and hashes are pinned in record metadata; source links do not imply automatic licensing to redistribute papers, figures or historical datasets.

| help_class | example | authority |
| --- | --- | --- |
| plain mathematical definition | Parameters, Omega, one map update, raw chirality, exact construction roles | api.py, owning modules; K0 ledger A01/A05/A06/B01/C01/D03 and accepted paper references. |
| historical provenance | Known seed/eps/g/lock/observer literal values | _presets.py; ledger L01-L04/L06; K2 final closeout O02/O03. |
| accepted claim | Stored geometry incidence, raw chirality identity, passive accounting meaning | K0 ledger C04/B01/E06-E10; accepted P1-P12 parity closeout; returned facts. |
| known qualification | U(1) nonzero pre-sync qualification; unequal-k symmetry; potential need not decrease; unresolved alignment | K0 authority section 1 and ledger A04/E08/E10; z_diagnostics.py docstrings. |
| open rationale | Why eps=.05,g=.2, seed and lock=.244 were originally chosen | K2_PARITY_FINAL_CLOSEOUT.md O02 OPEN_NONBLOCKING; never infer motives from later consequences. |
| research-only idea | Twisted crystal, EM/RS, warp, spring and geometry coupling concepts | Excluded ledger/research class; no executable control or accepted-law tooltip. |

## ARCHITECTURE COMPARISON

These are engineering judgments from the audited requirements, not performance benchmarks or popularity rankings. Native means PySide6 Qt Widgets + Matplotlib for the recommendation; Tkinter is a lighter native option but less attractive for the intended rich record tables/control surface. Browser means a local, asset-bundled UI with a Python service and worker. Hybrid means a desktop shell/web renderer plus Python, exemplified by Electron; no framework is installed or prototyped here.

Source facts: [Matplotlib backends](https://matplotlib.org/stable/users/explain/figure/backends.html) document QtAgg and PNG/SVG output; [mplot3d limitations](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html) explain why it is not an unrestricted 3D renderer. [Qt accessibility](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAccessibleWidget.html) and [QProcess](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QProcess.html) support the proposed native widget/process design. [Plotly offline/MIT overview](https://plotly.com/javascript/is-plotly-free/) and its [actual source license](https://github.com/plotly/plotly.js/blob/main/LICENSE) support the browser candidate. [Electron's overview](https://www.electronjs.org/docs/latest) describes its bundled Chromium/Node architecture; [its license](https://github.com/electron/electron/blob/main/LICENSE) does not replace dependency notices.

| criterion | A_native_Python | B_local_browser_Python | C_hybrid_shell_web |
| --- | --- | --- | --- |
| Scientific plotting | Matplotlib QtAgg supports interactive scientific plots and image/vector export. | SVG plots via locally bundled Plotly.js or equivalent; worker returns data only. | Same web plotting options; additional desktop bridge. |
| 3D ability | mplot3d handles the small initial wireframe; advanced occlusion/picking needs a later renderer decision. | WebGL scene libraries can support richer interaction; mandatory software/table fallback needed to avoid GPU requirement. | Rich web renderer possible, with the same fallback requirement. |
| Slider/control ergonomics | Qt Widgets offers native focus, numeric fields, sliders and tables; direct numeric fallback is natural. | HTML form controls and keyboard semantics; custom widgets need accessibility discipline. | HTML controls plus desktop menus/dialog integration. |
| Offline packaging | Local wheels/assets; no HTTP service, browser or CDN required. | All assets bundled and locally served; no Internet needed, but loopback HTTP and browser lifecycle remain runtime components. | Bundled browser engine or system webview plus Python; offline asset packaging possible. |
| Windows packaging | CPython 3.11 x64 + PySide6 Essentials/Shiboken + Matplotlib candidates; first release can be an installed companion, not a frozen executable. | Python local service/worker and supported installed browser; ports, origin policy and launch management add obligations. | Electron includes Chromium/Node plus Python; Tauri/WebView2 adds another toolchain/runtime deployment decision. |
| Dependency weight | Larger than 80 KB kernel, bounded to GUI application; exclude Qt Addons/WebEngine/QtQuick3D from first slice. No measured final bundle size claimed. | Potentially lean app assets if system browser reused; plotting/server dependencies and browser installation still count. | Highest likely bundle/toolchain complexity for Electron; other shells require concrete measurement rather than assumed savings. |
| Licensing | Qt/PySide component licensing + Matplotlib and transitive notices require a separate app inventory; dynamically replaceable LGPL libraries only for selected path. | MIT Plotly.js is an option, with transitive asset/server licenses still enumerated. | Electron project license plus Chromium/Node/third-party notices; Qt WebEngine alternative adds Qt and Chromium obligations. |
| Testability | Python request/worker integration tests, widget/keyboard tests and plot snapshots; subprocess protocol separable. | Browser automation/DOM accessibility tests plus Python service/IPC tests. | Browser tests plus shell/bridge/installer tests. |
| Accessibility | Standard Qt Widgets and explicit accessible names; charts need table/text alternatives and Windows assistive-technology verification. | Semantic HTML can be strong; canvas/WebGL must have equivalent tables/descriptions. | Web accessibility plus native shell/focus behavior must be tested together. |
| Future extension | Separate view adapters permit richer 3D and batch/comparison tools without core change. | Strong complex web scene ecosystem; networking/asset lifecycle remains application work. | Desktop integrations possible but unnecessary for the first audited surface. |
| Python API isolation | Worker subprocess through public facade; stdio/files require no sockets. | Python worker behind a local broker; browser never computes science. | Python worker through audited IPC bridge; no direct renderer science. |
| Adjudication | RECOMMENDED for K4b: few accepted geometry objects, strict offline/no-GPU baseline, record-heavy workflow and process cancellation. | Viable alternative if browser delivery becomes a requirement; loopback transport is not a zero-socket application and must be disclosed. | Defer: shell/engine distribution cost adds no required first-slice capability. |

## FRONTEND LICENSE / PACKAGE IMPLICATIONS

The application is a separate distribution boundary. Nothing in the kernel's existing LICENSE_SCOPE.md automatically grants an application or paper-content license. No dependency/license file is changed here. The chosen native architecture has a viable documented module/licensing route; K4a does not certify a particular future binary bundle. K4b must lock exact artifacts and review their included modules/notices before bundling; if that actual selection conflicts with the approved scope, stop instead of adding a GPL-only module or changing license silently.

Qt explicitly distinguishes LGPL-capable components from GPL-only parts. Its published obligations include library notices, corresponding-source provision and user replacement/relinking rights. Use those as packaging requirements, not a claim that the dependency becomes Apache-2.0. Sources: [Qt licensing](https://doc.qt.io/qt-6/licensing.html), [Qt for Python licensing](https://doc.qt.io/qtforpython-6.10/commercial/index.html), and [Qt's LGPL obligations](https://www.qt.io/development/open-source-lgpl-obligations). Matplotlib's license and bundled third-party notices are documented in its [license page](https://matplotlib.org/stable/project/license.html). Qt WebEngine's distinct alternative burden is documented [here](https://doc.qt.io/qtforpython-6/overviews/qtwebengine-licensing.html).

Read-only package metadata checked on 2026-09-27 shows candidate Windows x64 wheels for PySide6-Essentials 6.11.2 (cp310-abi3, Python >=3.10,<3.15) and Matplotlib 3.11.2 (cp311, Python >=3.11). This is feasibility evidence, not an installed compatibility test or an approved final lock. [PySide6-Essentials metadata](https://pypi.org/project/PySide6-Essentials/) and [Matplotlib metadata](https://pypi.org/project/matplotlib/). Resolve/pin the complete compatible app wheelhouse in K4b while retaining numpy==2.4.4, sympy==1.14.0, mpmath==1.3.0 and Windows CPython >=3.11,<3.12. A conflict must not expand the kernel's support lane.

| component | license_basis | redistribution_NOTICE_bundle_requirements | boundary_decision |
| --- | --- | --- | --- |
| Certified kernel artifact | Existing software-only Apache-2.0 scope | Retain LICENSE/LICENSE_SCOPE.md and distribution metadata; pin exact artifact/hash/source identity, not version alone. | Unchanged; no GUI dependencies or assets enter its wheel/sdist. |
| New companion application source | Proposed separate Apache-2.0 software-only application scope; requires K4b authorization, not an automatic extension of current scope | New app LICENSE/scope notices apply only to newly authorized application software. Do not relicense papers/fixtures/help source documents. | Local project name is provisional, not a registry claim. |
| PySide6 Essentials / Shiboken / Qt Core, Gui, Widgets | Community packages offer LGPL/GPL alternatives; select an audited LGPL-compatible module/runtime set | Retain required license/copyright notices, prominent library-use notice, corresponding-source availability and replacement/relinking/installation rights. Inventory actual DLLs/plugins/tools and third-party components. No blanket assumption that every Qt module is LGPL. | Choose dynamic/replaceable library packaging; no Qt Addons/WebEngine/QtQuick3D or static/fused bundle in K4b. Exact inventory precedes redistribution. |
| Matplotlib and bundled rendering/fonts | Matplotlib license is PSF-based; bundled components have their own notices | Retain license/copyright and applicable bundled notices; summarize changes if modifying library code. Inventory actual Agg/FreeType/fonts and transitive wheels. | Use unmodified library; PNG/SVG output remains presentation, not a relicensed scientific figure dataset. |
| Qt/plotting dependencies and assets | Per-artifact license inventory, not inferred from a parent dependency | Record distribution/version/hash, license text/notice paths, redistributable content and source obligations in app lock/notices. | No dependencies downloaded or bundled by K4a. |
| Browser alternative Plotly.js | MIT source license for open-source plotly.js | Retain copyright/license; enumerate bundled/transitive libraries/fonts and omit network-dependent maps/services. | Not selected or installed; source LICENSE governs chosen artifact, not unrelated commercial products. |
| Hybrid Electron or Qt WebEngine | Electron project permissive license plus dependency terms; Qt WebEngine has Qt and Chromium licensing | Preserve actual full third-party notices and source obligations for the selected distribution. | Not selected; no blanket “all Apache” claim. |
| Papers/research/fixtures/historical assets | Excluded from automatic kernel Apache scope | Link metadata or write original concise help; obtain separate authorization before redistributing protected text/figures/datasets. | No paper/research bundling in K4b. |

## RECOMMENDED ARCHITECTURE

Choose A: a separate native Python scientific application using PySide6 Qt Widgets, Matplotlib QtAgg for plots and initial CPU mplot3d wireframes, plus a worker subprocess using kernel_physics.api only. This is the final K4b architecture recommendation. It is justified by the current small exact geometry, explicit numeric forms, substantial provenance/record inspection, no need for a browser/server, direct Windows widget/process support, and ability to keep essential rendering off a GPU. A richer 3D renderer can later consume the same public-record view model after an independent performance/license decision; K4a does not choose a future renderer merely for visual prestige.

UI_PACKAGE_BOUNDARY = SEPARATE_APPLICATION_LAYER. It may live in this repository under apps/scientific_ui while using its own pyproject, dependency lock, tests, license scope and CI. Do not add an optional GUI extra to the kernel pyproject or expand the ~80 KB kernel archive. A companion wheel/installed launcher is the initial delivery form; a self-contained desktop executable/installer is deferred until license/source/replaceability and clean-launch evidence are ready. The local working name trioctagon-scientific-ui / import namespace trioctagon_ui reserves no registry name.

NETWORK_REQUIRED = NO, including no required local HTTP listener for the recommended design. Use local stdio/files for worker IPC, installed assets/fonts, CPU plotting and original help. No CDN, telemetry, automatic update request, cloud account, model, GPU or remote service is part of essential operation. Offline installation uses a previously prepared verified wheelhouse; artifact acquisition is separate from normal runtime. Future CPU fallback/table accessibility is mandatory even if an optional 3D renderer uses acceleration.

Run the GUI in an application environment with a locked installed kernel wheel; the worker imports the companion transport/adapter and public kernel, not GUI modules. Locks retain the frozen core numerical pins. UI source commit/app version and kernel artifact source commit are separate identities. Start with the exact certified K3c-R3 artifact (source 7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e, chosen archive SHA-256 recorded in kernel-artifact.lock.json); never resolve a same-version package from an unverified registry name. The first UI must remain usable from outside this repository. Normal application edits must not make kernel source provenance dirty.

Use an absolute interpreter/argument list and asynchronous worker output signals so the event loop remains responsive. The design relies on documented [QProcess I/O and lifecycle](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QProcess.html) or equivalent [Python subprocess facilities](https://docs.python.org/3.11/library/subprocess.html), not a shell command composed from user input. K4b decides exact packaging artifacts after its bounded lock/license preflight; no implementation was made in this phase.

## K4B VERTICAL SLICE

ACCEPT the proposed run/inspect/save-load slice plus an independent minimal geometry explorer, with explicit limits below. A plot of stored samples is essential in K4b, not deferred entirely to K4c. Basic sample selection is included; full playback/advanced 3D/presentation comparison comes later. A minimal B workspace exposes named observers and diagnostic choices with returned tables; the complete custom-clock/config/history scratchpad is K4c. The controls remain mapped and scheduled, not reclassified as unsupported.

K4b excludes sweeps, scientific replay certification, advanced ring editing, custom observer scratchpads, history torus UI, full D03 construction selector, C01 section sliders, filled/advanced 3D scenes, public release/installer creation and all research/quarantined controls. No API gap above blocks this useful slice. Do not expand it by implementing mathematics or promoting private helpers.

| step | scope | acceptance |
| --- | --- | --- |
| 1 Launch offline | Installed companion from unrelated directory; read locked kernel metadata; four labelled workspace destinations. | No repository import path, network/model/GPU requirement; clear app versus kernel identity. |
| 2 Construct draft | Real/imag triad State, explicit index and eps/g/phase_strength/k triple; labelled optional historical fills; explicit updates and selections. | No hidden scientific defaults; all submitted fields/provenance inspectable; linked-k writes an explicit triple. |
| 3 Run once in worker | Zero/one/bounded multi-update via run, optional named staged/EMA observers and all five supported diagnostics. | One API operation per job; original errors shown; ring controls not enabled until their complete K4c path exists. |
| 4 Inspect and plot | Stored Omega Re/Im and requested raw chirality vs update index, per-channel complex-plane plots, sample selector and structured diagnostic tables. | No kernel call on sample selection/repaint; values trace to record paths; charts have table/text alternatives. |
| 5 Reproduce | Structured record/provenance inspector, exact JSON save/load, separate draft save, compatible resume and explicit checkpoint/new-run action. | Digest validation distinguished from scientific replay; immutable prior records and unsaved-state distinction. |
| 6 Independent geometry | C01 with explicit [] sections and D03 regular(s) with exact positive integer/rational entry; CPU rotatable wireframe, exact expressions and object/incidence tables; save/load GeometryRecord JSON. | No Omega/geometry coupling, no floats into exact kernel options, no changed record to attach render cache. |
| 7 Responsive failure/cancel | One active worker; cancel can discard incomplete job; clear failure details and retained previous record. | No UI freeze, fake percent progress, partial-success record or lost child stderr. |
| 8 Client acceptance | Installed/offline launch, request routing, no-recompute playback, import boundary, keyboard/table access and preservation tests. | No new science oracle, P1-P12 duplication, kernel edit or distribution-CI change. |

## K4 PHASING

Keep four phases because each has a concrete usable outcome; avoid further administrative subphases. K4a freezes this contract only. K4b authorization starts from the commit containing exactly these two documents, reported as FINAL_HEAD at closeout; no guessed future SHA is embedded in a self-referential document. K4b begins with the compatible artifact/license lock, then implements the vertical slice. K4c implements the remaining supported controls and scientific views; K4d adds bounded batch/comparison/export work.

Kernel CI stays unchanged as an independent gate. Propose a separate .github/workflows/scientific-ui.yml for application install/launch, request/API contracts, presentation and accessibility checks. It consumes an explicit certified kernel artifact and records both kernel and UI identities. UI tests do not add GUI dependencies to kernel-distribution.yml. An ordinary K4a main push still triggers existing kernel CI; that is not a reason to rewrite it or run an additional broad local suite for these documents.

Recommend completing the private/local K4b usability slice before a coordinated public application launch, to validate the human interface. A separately authorized public kernel release could happen independently; it is not a prerequisite for local UI development because a verified wheel already exists. K4a/K4b authorization does not include PyPI upload, version bump, registry claim, or GitHub release. UI work must not delay or silently trigger an independent release decision.

| phase | deliverable | exit_condition |
| --- | --- | --- |
| K4a | Two surface/interaction/architecture documents | Exact public map, bounds and exclusions; preservation checks; normal docs commit. |
| K4b | Installed local companion vertical slice | Triad/record plots, named passive selectors, minimal separate geometry, save/load/resume/checkpoint, responsive worker and app tests. |
| K4c | Complete supported interactive views | Advanced ring/custom observers/history displays, C/D options/sections, stored-sample playback and appropriately qualified 3D. |
| K4d | Bounded dataset/comparison/exports | Explicit finite batch manifest, side-by-side descriptive comparisons, CSV/PNG/SVG provenance, packaging/accessibility polish. |

## K4B CHANGE ALLOWLIST PROPOSAL

Proposal for a later work order, not permission to create these files in K4a: create only the exact new paths below; modify zero existing tracked paths, including both K4a documents and every kernel/test/CI/license file. The apps/scientific_ui root does not currently exist. Keep builds, downloaded wheels, full third-party source bundles, screenshots, environments and generated runtime artifacts outside Git; a later work order can explicitly add a necessary test-asset path after review. The proposed list contains no kernel implementation, new scientific oracle, fixture update, README rewrite or cleanup.

Proposed next implementation starting HEAD is the completed K4a documentation commit (FINAL_HEAD = ORIGIN_MAIN after the authorized normal push). It is an actual commit to be returned, not a future hash guessed before commit. K4b authorization must confirm this starting identity and approve the companion license/artifact choices; no additional K4a implementation or release is authorized by this proposal.

| new_path | purpose |
| --- | --- |
| apps/scientific_ui/pyproject.toml | Companion-only packaging/entry point; no kernel metadata change. |
| apps/scientific_ui/README.md | Offline install/launch, scope, explicit input workflow and troubleshooting. |
| apps/scientific_ui/LICENSE | Application software license only after K4b authorization. |
| apps/scientific_ui/LICENSE_SCOPE.md | Narrow app scope; preserve parent paper/research exclusions. |
| apps/scientific_ui/THIRD_PARTY_NOTICES.md | Audited Qt/Matplotlib/transitive notices and source/replaceability instructions. |
| apps/scientific_ui/requirements-win-py311.lock | Exact app/core compatible dependency pins and hashes; no kernel pin drift. |
| apps/scientific_ui/kernel-artifact.lock.json | Certified kernel archive filename/hash/commit and provenance receipt identity. |
| apps/scientific_ui/src/trioctagon_ui/__init__.py | Inert application package initialization; no automatic GUI imports in worker. |
| apps/scientific_ui/src/trioctagon_ui/__main__.py | Installed application entry point. |
| apps/scientific_ui/src/trioctagon_ui/app.py | Qt shell/workspaces and draft/current-record state. |
| apps/scientific_ui/src/trioctagon_ui/requests.py | Versioned UI request/type/representation validation and explicit public-object construction. |
| apps/scientific_ui/src/trioctagon_ui/worker.py | Only public scientific API routing and typed response/error envelope. |
| apps/scientific_ui/src/trioctagon_ui/jobs.py | Process lifecycle, cancellation and completed-artifact handoff. |
| apps/scientific_ui/src/trioctagon_ui/record_views.py | Public-record formatting, detached tables, trust/status and immutable save/load UX. |
| apps/scientific_ui/src/trioctagon_ui/geometry_view.py | Exact-node display adaptation and independent returned-geometry wireframe; no constructors/formulas. |
| apps/scientific_ui/src/trioctagon_ui/plots.py | Stored-sample/complex-plane plots and sample selector only. |
| apps/scientific_ui/src/trioctagon_ui/help.json | Original concise, source-classified help without copied research/publication assets. |
| apps/scientific_ui/tests/test_requests.py | Field/provenance/selection and no-clamping request checks. |
| apps/scientific_ui/tests/test_worker_contract.py | Actual public-call routing, imported boundary, error/cancel and identity behavior. |
| apps/scientific_ui/tests/test_records.py | Portable record views/save/load, exact binary64 handling and immutable drafts. |
| apps/scientific_ui/tests/test_ui.py | Keyboard/focus/accessibility and bounded render/interaction checks. |
| apps/scientific_ui/tests/test_install_launch.py | Installed/offline Windows launch from outside checkout. |
| .github/workflows/scientific-ui.yml | Separate application CI; existing kernel workflow remains byte-identical. |

## Future UI test plan

Kernel scientific correctness stays in the existing P1-P12 and software tests. UI contract tests may invoke the public API as the authority and compare submitted arguments or returned record text; do not duplicate formulas or independent mathematical oracles in application/frontend code. Snapshot differences are presentation regressions, not new parity certificates. Accessibility is an acceptance requirement, not a theme preference.

| test_class | checks | explicit_non_claim |
| --- | --- | --- |
| UI UNIT | No hidden defaults; numeric fallback/out-of-range soft-range behavior; linked k exact tuple; draft/record separation; source-classified help; all editable fields accounted for. | No recurrence/observer/geometry formula implemented in tests. |
| UI ↔ API CONTRACT | One correct public call per explicit job; tuple/object construction; triad/ring restrictions; selections/provenance/order; returned values displayed unchanged; no private/quarantine import. | Science oracle remains kernel tests. |
| RENDER SNAPSHOT | Known returned record projects/table-formats correctly; labels, object IDs and selection; geometry and dynamics visibly separate; repaint/scrub invokes no API. | No geometry correctness inferred from pixels; fixed camera/theme/font for snapshots. |
| INSTALL / LAUNCH | Windows/CPython 3.11 installed companion with verified kernel wheel and pinned core deps, outside checkout; worker origins installed; network blocked; no GPU/model import required. | App support does not broaden kernel lane. |
| REPRODUCIBILITY | Public JSON import/export preserves canonical text/digest; floats preserve bits; producer versus viewer environment; resume failure retains original reason; changed draft creates new run; invalid JSON not repaired. | Valid digest is not an authentication or automatic replay result. |
| ACCESSIBILITY | Keyboard all actions/sliders/text alternatives, focus order, visible validation, screen-reader names, contrast/non-colour signals, table equivalents for every chart/3D view and reduced motion. | Qt accessibility support alone is not evidence the app is accessible; test on Windows. |
| RESPONSIVENESS / CANCELLATION | Long mocked/API jobs cannot freeze GUI; original stderr preserved; cancellation/completion race; no incomplete records published; previous complete record survives. | No invented percentage progress or resumable partial kernel result. |

## Pinned local evidence and validation

All source citations refer to the audited starting commit. API/runtime/schema facts come from current code; definitions/qualifications from the accepted ledger and later closeout; tests were inspected as evidence, not rerun or modified. External technology/license pages were read on 2026-09-27; their URLs support architecture feasibility, not a frozen dependency lock. Actual library redistribution inventory belongs to K4b.

K4a validation: parse JSON; verify exact 34-export coverage, one control class per ID, all mandatory sections and matched Markdown/JSON content; verify every starting tracked file's raw SHA-256 and unrelated untracked bytes; require only the two new documents; git diff --check. No broad numerical/installation test rerun is required for this documentation-only phase. All K4a stop gates are clear for the bounded recommendation. Final commit/push identities are returned externally to avoid embedding the document's own commit hash.

| path | SHA256_at_audited_HEAD | pinned_source |
| --- | --- | --- |
| kernel_physics/api.py | 6b3f2b4f2f6846147c74a3ee0dd2605830a590d68b368a73895a8f191f27a1c3 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/api.py) |
| kernel_physics/_contract_types.py | 4e7dbdfaad9bc231d932d88bae5a8a9e565b4b80754a678f9a25f9faa1190903 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_contract_types.py) |
| kernel_physics/_presets.py | cd8ff8c412391aa51a19d842dee4445537aac19d573412bac33b54f7da0d2e84 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_presets.py) |
| kernel_physics/_runner.py | 3a9f3ce718b1600f445bf963b968b9dbb3c41b03e6f2acf15239e2ae1512bcf6 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_runner.py) |
| kernel_physics/_records.py | aa82d39cfc92a9d8f58ffd87342186ddf67134c4590f41e475327f0396bb5785 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_records.py) |
| kernel_physics/_geometry_records.py | 7313d6bcea2e03615a0ac5ceec177d7abd9bc695e1a2ac6d9b8aa629838c1f60 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_geometry_records.py) |
| kernel_physics/dynamics.py | ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/dynamics.py) |
| kernel_physics/readouts.py | 3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/readouts.py) |
| kernel_physics/z_manifold.py | 97ebdbb37103e736d2ae86c272541c458a5b585e1889e6d14ff056b316494f4f | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/z_manifold.py) |
| kernel_physics/z_diagnostics.py | db6c5d87fcecd492ac76fbc3cbcd6b71520d2ab4c9bbe4b1686c138aa0549d09 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/z_diagnostics.py) |
| kernel_physics/_response_numeric.py | cc33f797e76f7dbeff6fbd58ab52003fde2acbadf35ae299d827b4b55ba29655 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/_response_numeric.py) |
| kernel_physics/geometry.py | 18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/geometry.py) |
| kernel_physics/reference_scaffold.py | 39723db1d5e808fa8aeb3585eb47ac4b1cbc01310e07e9171b6d6e04111c4aaf | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/reference_scaffold.py) |
| kernel_physics/K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md | 9f21446519b857710dc60265c07c8677736bacf85481095476b747644f00f5c1 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md) |
| kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md | 2301c40fe3117a72b98998caaf7818a2d8bcf6b7c0a10f05daef0c8c82b1c0d4 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md) |
| kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md | b0e6894748f4c662381bd25cc23f2a74c8dcdccb2981d8f20fb4b5024536a3f6 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md) |
| kernel_physics/tests/test_public_contract.py | 48ede752030a81b97363011d40b0f12e186b22ed7d97b85bebcd48c9f67850f7 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/tests/test_public_contract.py) |
| kernel_physics/tests/test_runner_records.py | 2b95ca7f03b0942739e3f511b729f9e730c0a8a22c65809f7ddb9508f64b3e0e | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/tests/test_runner_records.py) |
| kernel_physics/tests/test_geometry_records.py | cc92e556f1d19ab9310ae91c37ed32c45f7dedc2b0c79b0ad27ce6110f9f3bfc | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/kernel_physics/tests/test_geometry_records.py) |
| LICENSE_SCOPE.md | 5da42df1c921eef7a244e15b4b06060d8be70ff13832b3714f48196d084c4449 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/LICENSE_SCOPE.md) |
| pyproject.toml | 50f0d464fbaa8d800bec4afd659a81fc41f4a6f3368c1fc7a67bbc6a82f74939 | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/pyproject.toml) |
| .github/workflows/kernel-distribution.yml | 07f723dccc3e5e4424284050a9f7fd8a238c8d9a5365a774551094a07f4a480d | [source](https://github.com/pzychozen/trioctagon-physics/blob/7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e/.github/workflows/kernel-distribution.yml) |
