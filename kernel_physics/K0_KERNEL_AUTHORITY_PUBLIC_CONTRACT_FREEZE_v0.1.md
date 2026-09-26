# K0 kernel authority and public contract freeze v0.1

Date: 2026-09-26. Scope: engineering contract only. This document and
[the definition ledger](K0_KERNEL_DEFINITION_LEDGER_v0.1.md) are the complete K0 packet.
The existing `kernel_physics/` documentation location is used alongside the
accepted implementation receipts; no competing documentation tree is created.

## 1. Disposition and authority

```text
STARTING_HEAD = 2b70485c1fd0044baf90e0df361182165c1b9315
STARTING_ORIGIN_MAIN = 2b70485c1fd0044baf90e0df361182165c1b9315
STARTING_REMOTE_MAIN = 2b70485c1fd0044baf90e0df361182165c1b9315
BRANCH = main
TRACKED_PREFLIGHT = CLEAN (index and worktree)
K0_STATUS = PASS (contract freeze, not implementation or parity certification)
PAPER_RUNTIME_CONTRADICTION_FOUND = NO
UNRESOLVED_AUTHORITY_COLLISION = NO
MATH_CHANGE_REQUIRED_FOR_PUBLIC_API = NO
OPTIONAL_MODULE_DECISION = AWAITING_GPT_HILMIR_DECISION
K1_SCOPE_DEFINED = YES
```

The ledger has 75 definition families: CORE=24, OPTIONAL=27,
RESEARCH_ONLY=13, HISTORICAL=8, OPEN=3. These are grouped ownership entries,
not function counts. Authority ledger, public API, state ownership, Runner,
both schemas, import boundary and P1–P12 plan are frozen. K1 is ready for
authorization of the base scope; optional-module support still requires the
explicit decision in section 10. No K1 implementation has started.

Repository: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`. The remote branch was
read with `git ls-remote origin refs/heads/main`, independently of the local
tracking ref. Pre-existing untracked files are not an authority override and
must remain untouched. They include four predecessor tests, local gate/torus
and Paper-F research, `research_files/`, `research_notes/`, `Claude outputs/`,
`CORPUS_CONSOLIDATION_REPORT.md`, and Paper F's local preservation inventory.

Precedence is accepted Papers A–F and publication evidence, current owning
runtime, accepted verification, then historical/research evidence. The ledger
pins editions and exact owning symbols. Preparation-time pending/publication
language is dated evidence: it does not override the current work order or
`K1_K2_K3_PARITY_CLOSEOUT.md`'s scoped acceptance. That older K1/R1–K3 sequence
is a different task series from this K0 and its proposed facade K1/K2.

No stop gate was found in the inspected authority chain. Specific apparent
conflicts are already resolved by accepted records:

* Paper E's historical signed-zero phase behavior is provenance, not authority
  to replace modern `arg0`. Its v0.1.1 revision and the K2 receipt explicitly
  distinguish same-state observer parity from historical trajectory equivalence.
* Paper B accepts an optional tangent-vector representation on Paper C frames.
  It supplies no assignment of an amplitude or chirality to a shell point,
  field, surface interpolation, or physical coupling. Its Appendix A explicitly
  treats transitive helper imports as execution dependencies, not physics.
* `z_diagnostics.intensity_budget` computes the accepted accounting increment;
  it is not a second state evolution API. Its prediction must never become the
  Runner's next state. Only `step3`/`step_ring` own advancement.
* Historical defaults in `Clock`, `StagedConfig`, `EMAConfig`, `EMAState` and
  display helpers are documented and accepted in their named historical scope.
  The public constructors below remove implicit selection, without editing them.
* Common U(1) equivariance for nonzero phase strength is qualified by nonzero
  pre-sync entries. S3 covariance permutes `k` with the state; fixed unequal `k`
  does not generally have the full S3 symmetry. These are published qualifications.

The open register in section 11 records known, bounded omissions. None asks an
implementer to resolve a mathematical contradiction or invent an accepted law.
Discovering such a contradiction later changes the disposition to HOLD.

## 2. Supported v1 surface for K1

Namespace: **`kernel_physics.api`**, to be created only in K1. Existing internal
modules and their imports remain available but are not the UI compatibility
contract. Public API version and both record schemas start at **1.0.0**; this
Markdown specification's version is 0.1. No facade exists at K0 closeout.

Names below are frozen. Keyword-only construction avoids positional traps.
Public value types own detached immutable values; conversion to existing
runtime types supplies every field explicitly. They do not evaluate equations.
`Parameters` retains the established field name `phase_strength` (Paper A's
lambda) and produces one existing `DynamicsConfig`. No epsilon, coupling,
phase strength, `k`, seed, clock, or observer coefficient has a public default.

```python
Parameters(*, eps: Real, g: Real, phase_strength: Real, k: RealTriple)
State(*, omega: ComplexVector, update_index: int)
Seed(*, name: str, omega: ComplexTriple, provenance: Provenance)
historical_seed(name: str) -> Seed
step(state: State, parameters: Parameters, *, topology: Literal["triad", "ring"]) -> State
z_chiral(omega: ComplexTriple) -> RealTriple

Clock(*, q: int, N: int, t: Real, q_step: int)
StagedConfig(*, lambda_vp: Real, gamma: Real, theta_lock: Real, alpha: Real, beta: Real)
EMAConfig(*, lambda_vp: Real, theta_lock: Real, alpha: Real, beta: Real)
EMAState(*, m: Real)
advance_clock(clock: Clock, dt: Real) -> Clock
advance_ema(omega: ComplexTriple, memory: EMAState) -> EMAState
observe_staged(omega: ComplexTriple, clock: Clock, config: StagedConfig) -> ZReadout
observe_ema(omega: ComplexTriple, clock: Clock, config: EMAConfig, memory: EMAState) -> ZReadout
historical_observer(name: Literal["paper_e_staged_v1", "paper_e_ema_v1"]) -> ObserverRequest
ObserverRequest(*, observer_id: str, config: StagedConfig | EMAConfig,
                clock: Clock, memory: EMAState | None, dt: Real,
                initialization: Literal["recomputed", "historical_constructor_zero"],
                provenance: Provenance)

run(initial_state: State, parameters: Parameters, *, topology: Literal["triad", "ring"],
    updates: int, parameter_provenance: Provenance, initialization_provenance: Provenance,
    observers: tuple[ObserverRequest, ...], readouts: tuple[str, ...],
    diagnostics: tuple[str, ...]) -> RunRecord
resume(record: RunRecord, *, updates: int) -> RunRecord

get_geometry(definition_id: str, *, options: Mapping) -> GeometryRecord
RunRecord.to_json() -> str
RunRecord.from_json(text: str) -> RunRecord
GeometryRecord.to_json() -> str
GeometryRecord.from_json(text: str) -> GeometryRecord
```

`ZReadout` is a detached result with the existing `z`, `Z_macro`, `Z_chiral`,
`Z_total`, `variant`, `initialization` fields; `Z_vec` is a read-only alias.
The public precision exception is the existing `ResponsePrecisionError`, imported
directly from `_response_numeric`, never via boundary-response activation.
`Provenance` is the serializable descriptor in section 5, not a science object.

The chirality name is **`z_chiral`**, preserving current vocabulary; no competing
`chirality` implementation or normalization is introduced. `step` delegates
exactly once to `step3` for triads or `step_ring` for rings, preserving raw scale.
Ring size must be a multiple of three; repeated `k` remains owned by `step_ring`.
Ring runs do not accept three-channel observers/readouts/diagnostics in v1.

Public passive functions also retain these existing names and arguments:
`quadratic_form(vector)`, `readout_accounting(readout, *, alpha, beta)`,
`chiral_area_accounting(omega)`, `intensity_budget(omega, parameters)`,
`potential(omega, parameters)`, `historical_alignment(macro, chiral, total_vector)`.
They delegate to `z_diagnostics`. Direct display functions retain their names,
but require explicit `key`, `N`, `R`, and `r_max` wherever applicable:
`direct_history_coordinates(history, *, key)`, `cylinder_point(kappa,q,z,*,N)`,
`cylinder_history_coordinates(history,*,N)`,
`history_torus_coordinates(history,*,R,r_max,N)`. They return separate display
results; they are not Runner diagnostics or Geometry Records.

Raw `FaceState`, encoders, transport, and low-level covering/geometry operations
remain ledgered accepted facilities. The first facade does not expose a stepping
`FaceState`, a spatial State field, or arbitrary symbolic transformation APIs.
Paper B's raw area identity is covered by `z_chiral`; Paper C/D constructions are
exposed through Geometry Records. A later public face-view adapter requires a
separate bounded scope, including its optional transitive imports. This is an
engineering exposure limit, not rejection of Paper B. No scientific file needs
editing to implement this surface.

Named seed registry v1 contains only `gate_torus_seed_v1`:
`(0.2+0.3j, -0.4+0.1j, 0.1-0.2j)`, from the saved gate/torus experiment and
Paper F's historical example. It returns recorded literal values and source
provenance, not a claim that the seed's original motivation is known. There is
no default seed or generator. The two historical observer presets explicitly
materialize `.618`, `.244`, `alpha=1`, `beta=.5`, `N=12`, `q=0`, `t=0`,
`q_step=1`, `dt=.1`, `initialization="recomputed"`; staged adds `gamma=.577`
and `memory=None`, EMA adds `m=0` and no gamma. These are named run presets,
not a claim to reproduce the historical constructor-zero row. The preset's
observer ID is its preset name; duplicate IDs must be changed explicitly by
constructing a new request. No SRG/profile preset is selected by these helpers.

### Validation

Public numeric input rejects strings, booleans (including NumPy booleans),
nonfinite values and complex values in real fields. Shape is exact: triad `(3,)`,
ring `(3q,)`, real triple `(3,)`; no flattening or broadcasting. Counts are
nonnegative integers excluding bool; `N` is a positive integer and `q/q_step`
are signed integers. `dt` is explicitly finite real, including zero/negative
values as allowed by the existing clock; it is never a recurrence timestep.
EMA memory must satisfy the existing `abs(m)<=1` profile. Observer configurations
allow the existing signed finite coefficients; no positivity is invented.

The facade validates before existing coercive constructors and copies caller
arrays. It adds no tiny-state threshold, clipping, scaling, phase repair or
normalization. It preserves each delegated operation's precision policy and
exception; a state accepted by dynamics can be outside a requested readout's
numeric domain. All output float components must be finite for serialization.
Failure produces no partial next state or successful Run Record. Types fail
with `TypeError`, invalid shapes/domains/IDs with `ValueError`, and existing
numeric failures remain `FloatingPointError`/`ResponsePrecisionError`.

Unknown schema versions, definition IDs, preset IDs, options, readout/diagnostic
names, duplicate observer IDs and duplicate JSON keys are rejected. No silent
fallback to a different geometry or observer is allowed. Empty selections are
explicit tuples; no optional facility is enabled by omission.

## 3. State ownership and effects

| Object | Ownership | Existing behavior | Public protection |
|---|---|---|---|
| `L3`, exact bases, geometry constants, symmetry definitions, IDs | Immutable definition | Tuples/exact values; generated numeric basis arrays can be writable | Never return writable shared definition storage |
| `DynamicsConfig`, observer configs, geometry options, named presets | Immutable configuration | Frozen dataclasses; historical literals exist as described above | Explicit constructors; full provenance and values serialized |
| Omega and update index | Evolving run state | Dynamics returns a fresh writable complex128 array; no internal count | New detached `State` per step; index increments exactly once |
| `Clock.q`, `Clock.t` | Evolving observer state | Frozen `Clock`; `advance_clock` returns a new object, modulo-N q | Independent clock snapshots; never infer q from recurrence index |
| `Clock.N`, `Clock.q_step` | Immutable observer configuration | Stored in each current Clock | Persist configuration separately and validate snapshot consistency |
| `EMAState.m` | Evolving observer memory | Frozen scalar; `advance_ema` returns a new state | One explicit update with newly committed Omega |
| Raw chirality, norms, observer result, accounting, display coordinates | Derived | Pure functions; fresh/read-only arrays as documented | Never persisted as input to dynamics; result storage is not state ownership |
| `FaceState.omega` / `.vectors` | Canonical value / derived view | Frozen object; `.step` returns a new FaceState and calls existing step once | No automatic encode/decode cycle; outside initial facade surface |
| Exact Paper C/D objects | Immutable geometry definitions/results | Frozen dataclasses with exact tuples; pure properties | Separate Geometry Record; no dynamic state reference |
| `ConstructorZeroRecord` | Historical result plus initialization snapshot | Stores zero readouts/memory without computing formulas | Mark explicitly; never confuse with recomputed observation |
| SRG `transfer_count` | Initialization provenance | Counts linear transfer applications before Omega initialization | Not recurrence index, clock q, or EMA update count |

No inspected public operation mutates caller-owned state or explicit observer
state. Pure readers include `arg0`, readouts, observation, diagnostics, geometry
properties and frame/transport conversions. Returning-new-state operations are
`step3`, `step_ring`, `advance_clock`, `advance_ema`, and `FaceState.step`.
Frozen NumPy-containing records resist ordinary mutation; array write flags
are not a security boundary. Public snapshots must not share writable storage.

## 4. Runner semantics

The Runner is the only supported orchestration layer combining recurrence,
observer advancement, requested diagnostics, and recording. Independent pure
read/advance primitives remain callable. No geometry is accepted by `run`.

1. Validate the entire request before execution. Copy the initial State,
   parameters, observer configuration/clock/memory and provenance. Preserve a
   supplied nonzero update index for explicit checkpoints; a seed normally
   starts at index zero. No SRG count is inferred.
2. Record the supplied initial state. `recomputed` observes it without advancing
   clock or EMA. `historical_constructor_zero` delegates to the existing named
   operation and stores its marker, zero memory and zero observer result. It is
   allowed only at index zero; supplied EMA memory must be `m=0`, and staged
   memory must be None. Requested raw chirality is still a
   separately computed result, so it need not equal constructor-zero `Z_chiral`.
   Evaluate all requested raw readouts and passive diagnostics for this initial
   sample with the same rules used for subsequent samples.
3. For each requested update, call the existing recurrence once. Increment the
   recurrence index once. For each selected observer in request order, advance
   its clock once using its explicit `dt`; advance EMA once using the **new**
   Omega if and only if that observer is EMA. Observe using those new values.
4. Evaluate requested passive diagnostics and append the complete sample.
   No diagnostic result influences step acceptance, parameters or later Omega.
   A numeric exception aborts the request; caller snapshots remain unchanged.
5. `updates=0` is a valid one-sample record. Reading a record, calling observation
   again, exporting, or rendering does not perform any update.

Allowed raw readouts: `"z_chiral"`. Allowed Runner diagnostic IDs:
`"chiral_area_accounting"`, `"intensity_budget"`, `"potential"`,
`"readout_accounting"`, `"historical_alignment"`. The last two require at least
one observer and are keyed by observer ID. `intensity_budget` at index n means
the passive hypothetical increment **from Omega_n**; it is not a claim that
the record contains Omega_(n+1). Others inspect the state/readouts of that row.
Store every result field, including resolution flags and signed residuals.

For multiple observers there is one recurrence and independent clocks/memories;
no shared EMA update is accidentally applied twice. Observe after advancement
even when `dt=0`; the clock's q_step semantics are unchanged. Clock t is built by
repeated delegated addition, never replaced by `initial_t + n*dt` for replay.

**Restart:** `resume` validates a complete record, uses its last exact binary64
Omega and observer snapshots, and continues with identical parameters and
selection. It preserves the prefix and appends only new indices; it does not
reapply constructor-zero initialization or an EMA innovation at the junction.
It records the parent deterministic digest and the resume environment. No
parameters, dt or observer variant may change within a v1 record. Branching
with changed parameters requires a new `run` with explicit checkpoint provenance.
Resume also requires the same recorded source revision and implementation
module hashes; use a new checkpoint run when changing implementation. Numerical
library/platform changes may be recorded as a new execution segment, with the
replay qualification below. The junction snapshot remains byte-preserved.

**Replay:** decoding/restoring is pure. Verification replay calls `run` from the
initial checkpoint with its recorded selection and compares each stored row;
it is an explicit action, never a side effect of `from_json`. Match exact
serialized binary64 values in a matching numerical environment where they
reproduce; across platforms use the gate-specific tolerances, not a promise of
universal bitwise identity. Environment mismatch is reported, not repaired.

## 5. KERNEL_RUN_RECORD 1.0.0

The following is a normative JSON object contract. Required means the key is
present even for an empty list/map. No geometry coordinates or frame attachment
are permitted. Array ordering is semantically significant; object key ordering
is not. The canonical writer sorts keys, emits UTF-8, no insignificant spaces,
and no NaN/Infinity. A digest is SHA-256 of canonical deterministic content,
excluding the digest field itself and `execution_metadata`.

| Required key | Type and meaning |
|---|---|
| `record_type` | Literal `KERNEL_RUN_RECORD` |
| `schema_version`, `api_version` | Both `1.0.0` |
| `ledger_version` | `0.1`; fixes the interpretation of definition IDs |
| `topology`, `state_size` | `triad`/`ring`; validated integer size |
| `parameters` | `eps`, `g`, `phase_strength`, ordered three-element `k`, each binary64 |
| `parameter_provenance` | Provenance descriptor; no inferred default |
| `initialization` | `kind` = `explicit`/`historical_seed`/`checkpoint`; `provenance`; initial `update_index` and Omega; optional `preset_id` only for named seed, `parent_digest` only for checkpoint |
| `selection` | Ordered `readouts`, `diagnostics`, and `observer_ids`; valid unique names |
| `observers` | Ordered descriptors: ID, variant, all config values, initial q/t/m, N/q_step, dt, initialization marker, provenance. Staged memory is null; EMA has m. |
| `samples` | Ordered nonempty sample array, specified below |
| `definition_ids` | Sorted unique IDs from the ledger for every used definition/preset/result/schema |
| `paper_references` | Sorted source IDs with edition, repository-relative path and raw SHA-256 |
| `implementation` | Repository URL, full commit ID, package version, API version; sorted relative module paths and raw SHA-256 values; `tracked_dirty` boolean |
| `execution_metadata` | Ordered segments: first/last update indices, Python/NumPy/SymPy/mpmath versions, platform/architecture/byte order; timestamp optional |
| `deterministic_sha256` | Digest as defined above |
| `continuation` | Null for new run; otherwise parent deterministic digest and junction index |

Each sample requires `update_index`, `omega`, `observer_states`, `raw_readouts`,
`observer_results`, `diagnostics`. Indices are contiguous integers starting at
the initialization index. Omega has exactly `state_size` entries. Observer maps
have exactly the selected IDs: each state has `q`, `t`, `m` (null for staged)
and `observer_update_count` (zero at a fresh initialization, then increments by
one per explicit observer advancement; restart preserves it). N/q_step are in
the descriptor. Results carry all six named ZReadout fields; the alias Z_vec is
not separately serialized. Raw readout maps and diagnostic maps have exactly
the requested keys. Observer-specific diagnostics are nested by observer ID.
No unrequested derived arrays are generated merely to fill a record.

**Numeric codec:** a binary64 scalar is `{"f64":"<Python float.hex string>"}`;
signed zero is preserved. Complex128 is `{"re":<f64>,"im":<f64>}`. Ordinary
integers, including counters, are canonical decimal **strings** with the field
schema identifying their integer type (no plus sign or leading zero, except
zero itself). Booleans remain JSON booleans. Numeric arrays are nested lists
with shape prescribed by the field; no endian-dependent binary blob, implicit
complex string, or Python pickle. Deserialize using `float.fromhex` and strict
shape/domain checks. Display decimal rounding never replaces stored values.
Historical decimal source spellings are provenance strings, distinct from their
converted binary64 values. Exact symbolic geometry uses the separate codec below.

`Provenance` requires `kind` (`user_supplied`, `historical_preset`,
`accepted_definition`, `checkpoint`), `source_id`, `source_revision` (nullable
when unknown), `locator`, `literal_values` (map, possibly empty), and `notes`.
Unknown original motivation is explicitly stated; an arbitrary user seed must
not be assigned historical provenance. Source revision identifies evidence,
not necessarily the current execution commit. No machine-local absolute path
is needed in the deterministic content. Environment facts are never evidence
that a mathematical claim is true. No random timestamp or generated UUID is
required to identify a deterministic run.

**Diagnostic payloads:** use current dataclass field names/types exactly as
listed in `z_diagnostics.py` and the K3 API table (ledger E06–E11); scalars,
complex increment arrays, vectors and booleans use this codec. `potential` is a
scalar. Unresolved alignment retains both its numeric convention and flags.
No field is renamed to physical energy, force or flux.

**Round-trip and compatibility:** decode/encode preserves deterministic values,
ordering, signed zeros, exact counters, definitions, and provenance. Structural
validation includes equality of initialization and first sample, observer key
sets, config/variant/memory compatibility, shape, digest, contiguous indices,
and field allowlists. It does not silently recompute or certify supplied
diagnostic values. Equation checking is an explicit parity/replay operation.
Unknown fields fail in v1; a future additive schema needs an explicitly supported
minor version. Semantic/ordering/codec changes require a major version. A patch
can clarify documentation without changing accepted bytes. Migrations are
explicit versioned operations and preserve the original record.

## 6. GEOMETRY_RECORD 1.0.0

`get_geometry` requires one of the stable IDs `C01` (Paper C canonical shell) or
`D03` (Paper D reference scaffold). These IDs refer to this ledger version and
are never rebound. Paper D never replaces the shell implicitly.

Paper C options are exactly `{"section_heights": [...]}`; an empty list requests
no sections. Width is exactly one and fold angle exactly pi/3; there is no free
shell beta, global scaling, cap, or new variant. Each requested height must be
provably within the existing closed central band. General `panel_point` maps
remain accepted internal definitions, not a free geometry-family generator.

Paper D options select exactly one `construction`: `aligned` with s/g_gap,
`from_radius` with s/p, `regular` with s, `paper_c_member` with s,
`translate_paper_c_to_regular` with s, or `shrink_paper_c_at_fixed_centres` with s.
They delegate to the corresponding existing constructors. Record the original
construction/options as well as resolved s/g_gap/p/L. `g_gap` is a length,
distinct from dynamics g. Closed filled regions, outlines and reference frames
are separate objects, not welded material. Paper-D symmetry metadata preserves
E/G roles even for the regular member.

| Required key | Meaning |
|---|---|
| `record_type`, `schema_version`, `api_version` | `GEOMETRY_RECORD`, `1.0.0`, `1.0.0` |
| `geometry_definition_id`, `ledger_version`, `paper_id` | C01 or D03; `0.1`; C or D |
| `options`, `resolved_parameters` | Explicit exact requested and derived parameters |
| `construction_provenance`, `paper_references`, `implementation` | Exact source/edition and current module hashes/revision; same provenance conventions as Run Record |
| `coordinates` | Dimension, right-handed Cartesian axes where 3D, coordinate units=`mathematical_length`, named frame, origin, orientation, exact codec version |
| `objects` | Deterministically ordered mesh/region/frame/section objects, defined below |
| `symmetry` | Named accepted transforms, origin/axis, exact vertex permutations where available, role-preservation qualification |
| `coupling` | Literal `none`; explicitly no Omega, chirality or observer attachment |
| `deterministic_sha256` | Canonical content hash, excluding itself and execution metadata |
| `execution_metadata` | Producer versions/platform; non-scientific |

C objects contain exact vertices in `folded_module` order; zero-based edges,
oriented face cycles, seam edges, boundary edges, boundary loops, normals,
Euler characteristic and explicitly requested section segments. Each face has
`face_index` 0–2 and **separate** `panel_id` 1–3 with `panel_id=face_index+1`;
labels A/B/C correspond to P1/P2/P3. Loops omit repeated closure vertices.
Sections are curves, never filled caps. Supply C3, vertical-mirror and
horizontal-mirror vertex permutations by applying existing transforms to exact
vertices; record the centroid axis `(0,sqrt(3)/6,0)`, x=0 and z=0 planes. No
ad hoc rotational formula is allowed in the serializer.

D objects contain ordered alternating vertices, selected edges/connectors and
E/G roles, outline, support and connector halfplanes (`normal dot x <= offset`),
closed hexagon region, support-triangle generators, three corner-cell hulls,
complete local octagon metrics/vertices/outline/filled hull, radial/tangent
frames, planar/vertical centres and complete frames, top selected edges,
side lengths, area, circumradius squared and regularity result. Each has a
stable object ID and its own dimension/frame; frames use indices 0–2. Preserve
generator order; do not weld touching objects. Paper-C rigid-map metadata is
only a finite-face comparison when the selected input is the Paper-C member;
the known frame-to-panel permutation is `(P3,P1,P2)`. Translation and shrink
options are distinct operations, with separate returned parameters.

The `objects` container is an array. Every entry has exactly `object_id`,
`kind`, `dimension`, `frame_id`, and `data`. Its deterministic order and payload
keys are fixed as follows (integer indices use the integer codec):

| Selection / object IDs in order | Kind, dimension, frame | Required data keys |
|---|---|---|
| C: `shell` | `oriented_mesh`, 3, `paper_c_cartesian` | `vertices`, `edges`, `faces`, `seam_edges`, `boundary_edges`, `boundary_loops`, `euler_characteristic`; each face is `{face_index,panel_id,label,vertex_indices,normal}` |
| C: `section:0`, `section:1`, ... in requested height order | `section_curve`, 3, `paper_c_cartesian` | `height`, `segments` (each two exact 3D points); repeated heights are preserved as separate requests |
| D: `octagon` | `closed_polygon`, 2, `octagon_local` | `vertices`, `outline`, `filled_generators`, `s`, `a`, `w`, `R_oct`, `b` |
| D: `scaffold` | `closed_halfplane_region`, 2, `paper_d_planar` | `vertices`, `selected_edges`, `connectors`, `outline`, `side_lengths`, `edge_roles`, `support_halfplanes`, `connector_halfplanes`, `area`, `circumradius_squared`, `q_H`, `W`, `regularity_residual`, `is_regular`, `radial`, `tangent`; each halfplane is `{normal,offset,relation:"le"}` |
| D: `support_triangle`, `corner_cell:0`, `corner_cell:1`, `corner_cell:2` | `closed_hull`, 2, `paper_d_planar` | `vertices` (ordered generators) |
| D: `planar_frame:0`, `planar_frame:1`, `planar_frame:2` | `closed_reference_frame`, 2, `paper_d_planar` | `frame_index`, `centre`, `vertices` (complete octagon hull generators) |
| D: `vertical_frame:0`, `vertical_frame:1`, `vertical_frame:2` | `closed_reference_frame`, 3, `paper_d_cartesian` | `frame_index`, `centre`, `vertices`, `top_selected_edge` |

Closed polygon/hull vertex lists close implicitly; outline/segment fields use
point pairs, whereas C mesh edges use vertex indices. Do not mix these two
representations. C face labels are exactly A/B/C in face order. All D frame
payloads delegate to the existing properties listed in the ledger. Preserve
`is_regular` as true/false/null: exact inputs are not permission to convert an
undecidable symbolic result to false. The optional render payload for each
object is named `render`,
added alongside the five mandatory object fields, and contains `precision_bits`
and a binary64 copy of that object's numeric `data` fields with the same shapes;
indices, strings, booleans and relation markers remain unchanged. Exact `data`
always remains present. No display coordinates are added to a Run Record.

`coordinates` contains `frames`, keyed by the frame IDs above, each with
`dimension`, `origin`, `axes`, and `units`, plus `exact_codec_version="1"`.
Axes are the ordered standard Cartesian basis for that coordinate system;
local octagon axes are named x/y, Paper C material section coordinates use the
returned global x/y/z. `symmetry` contains `group`, `qualification`, and
`generators`: C has C3/sigma_v/sigma_h with exact vertex permutations and the
axis/plane descriptions above; D names its C3 rotation and role-preserving
reflection, with `vertex_permutation=null` in v1. D also records
`regular_unlabelled_group="D6"`
only for a regular member and `role_preserving_group="D3"`,
`traversal_preserving_group="C3"`; a null unlabelled group otherwise makes no
extra maximal-group assertion. These are accepted symmetry descriptions, not
new transform implementations. No D action array is computed in v1.

**Exact codec 1:** whitelist expression tree nodes `integer` (decimal string),
`rational` (coprime signed numerator/positive denominator), `pi`, `add`, `mul`,
`pow` (exact rational exponent), and `sin`/`cos` on exact arguments. Real exact
numeric expressions only for renderable v1 records: no floats, strings parsed
as code, free symbols, infinities, arbitrary functions, or `eval`/`sympify` of
untrusted text. Constructors still accept the existing provable symbolic
domains internally; the v1 **serializable/renderable subset** requires exact
numeric options. Rejection of a symbolic record is not a mathematical rejection
of that accepted symbolic construction. Optional binary64 render coordinates
use the object-level `render` payload
defined above and are **derived**, never authority. Exact tree nodes carry no
arbitrary display-string fields.
The writer uses the pinned SymPy tree argument order; compatibility does not
promise identical canonical trees across different SymPy versions. A record's
tree round-trips exactly and names its producer version.

Coordinates needed to render are returned, so a UI need not rebuild any
construction. Numerical render coordinates are evaluated from the exact data;
their explicit precision metadata cannot replace exact input/output values.
Loading records validates schema, codec, indices, dimensions, closed-set roles,
definition and digest; it neither calls a recurrence nor regenerates geometry.
An optional validation replay delegates to the existing construction. Unknown
versions and fields follow the Run Record version policy.

## 7. Imports and layer boundaries

Arrows below mean **imports**, not scientific causation. Current direct internal
edges, read statically from source, are:

| Module | Internal dependencies |
|---|---|
| `dynamics`, `covering`, `geometry`, `reference_scaffold`, `_response_numeric` | None |
| `readouts` | `_response_numeric` |
| `z_manifold` | `readouts`, `_response_numeric` |
| `z_diagnostics` | `readouts`, `_response_numeric`, `dynamics` (Config/L3 only), `z_manifold` (read-only helpers/types) |
| `boundary_response` | `_response_numeric` |
| `srg` | `_response_numeric`, `boundary_response` |
| `operating_region` | `_response_numeric`, `dynamics`, `srg` |
| `face_state` | `_response_numeric`, `dynamics`, `geometry`, `operating_region`, `readouts` |
| `__init__` | None; only `__version__="0.1.0"` |

No current kernel runtime import of research/papers was found. Dynamics and
geometry import neither each other nor the adapter. Observers do not import
dynamics or geometry. Diagnostics' constant/configuration import is allowed;
calling recurrence or observer advancement there is forbidden. The conceptual
layer diagram is therefore a partial order, not a mandatory chain of imports.

The explicit Paper-B adapter is the known mixed-dependency leaf. It derives
frames at import and transitively loads operating_region/SRG/boundary_response.
This is **not** an unknown physics coupling, but it means eager public re-export
would load facilities the caller did not select. K1 avoids that dependency by
not importing/re-exporting FaceState. It must not split or repair that module in
K0 or the proposed K1. Test-only imports of optional modules in existing
`test_readouts.py` and `test_face_state.py` are preserved and are not proof of
v1 support. Package-level import stays minimal.

Permitted new dependencies: `api` exports types/functions; `_runner` imports
accepted dynamics/readouts/observers/diagnostics and record helpers;
`_geometry_records` imports geometry/reference_scaffold; `_records` and
`_contract_types` use serialization/validation and accepted types as needed;
`_presets` stores explicit evidence-backed literals only. Runtime must never
import research, paper execution helpers, historical snapshots, UI, or tools.
UI imports `kernel_physics.api`, never internal science as a public contract.
Dynamic loading cannot be used to evade these rules.

P12's automated boundary test must parse **all** runtime ASTs, resolve relative
imports (including `from . import ...`), check forbidden direct/transitive edges,
and inspect importlib/dynamic-import uses against an allowlist. In a clean
subprocess, import the public API and each opt-in path and inspect `sys.modules`.
Patch forbidden advancement functions during observations/diagnostics and
assert they are never invoked. Assert exactly one delegated recurrence per
step. This supplements static dependency checks; it does not prove arbitrary
Python code incapable of side effects. No import repairs were made in K0.

## 8. Caller hazard register

| ID | Current behavior and correct meaning | Public protection |
|---|---|---|
| H01 | `geometry.panel_point` takes 1–3; face normals and FaceState take 0–2; D frames 0–2 map to P3/P1/P2 for the C comparison | Separate named fields, no generic `index`; validate integers excluding bool; serialize mapping |
| H02 | SRG count precedes initialization; zero means no SRG transfer | Keep `transfer_count` solely in initialization provenance; separate recurrence/observer counters |
| H03 | Observation is pure; advance functions return new values | Distinct names/types; Runner's explicit schedule and P12 call spies |
| H04 | `dt` advances observer t; Paper A is a discrete map without dt | ObserverRequest-only dt; never scale eps/g by it |
| H05 | D rejects float, nested SymPy Float, bool and string; unknown predicates can return None | Exact input codec and tri-state results; never rationalize floats silently |
| H06 | FaceState is a Paper-C-frame-specific kinematic view; canonical Omega survives stepping | No view in dynamic State; no automatic re-encoding; initial facade exclusion |
| H07 | History torus normalizes by maximum over the entire supplied history; appending data can move previous plotted points | Separate explicitly named batch display result with H_z/z_max/R/r_max/N/regularizer metadata; never restart state |
| H08 | DynamicsConfig coercion accepts inputs strict adapters reject; adapters reject some intermediate subnormals/overflow | Public validation before coercion; preserve operation-specific errors; no all-finite-input promise |
| H09 | Nonzero-lambda phase extension uses Arg0(0)=0, may be discontinuous, and lacks unrestricted U(1) symmetry there | State zero convention and qualified P3 cases; no invented continuity |
| H10 | Unequal k breaks fixed-parameter S3 symmetry | Record ordered k; test joint state/parameter covariance |
| H11 | Read-only NumPy flags are reversible by determined callers; arrays can alias without copying | Detached snapshots and serialization; no security claim |
| H12 | Constructor-zero Z is stored historical data, not a formula readout | Explicit marker; raw chirality separately named; never advance to manufacture row zero |
| H13 | `direct_history_coordinates` falls back to Z_vec only if Z_total is absent, not malformed | Preserve exact selection/failure rule; export one canonical Z_total field |
| H14 | C is a channel pseudovector; transport has rank two on ambient vectors; shell rotation acts on points about centroid | No spatial chirality field; no use of transport as a point transform |
| H15 | Negative-gradient increment does not imply finite-step potential descent; residuals are not certificates | Passive accounting only, full squared remainder, no clamping/controller |
| H16 | `.618`, `.577`, `.244`, N=12, dt=.1 and experimental seeds are literals, not derived laws | Explicit named presets with exact source spellings and binary values |
| H17 | `isometric_pullback` needs d dividing M; general residue P exists outside that domain | Preserve validation; no nonlinear lift with Q substituted for P |
| H18 | Exact C section is three segments, not a filled triangle; D regions are closed sets, not shell faces | Object kinds and boundary/filled roles in Geometry Record |

## 9. P1–P12 parity gates (planned, not executed)

Test filenames below are future locations under `kernel_physics/tests/`.
`test_*.py` references in the existing-evidence column are existing files in that
directory unless a full different path is given. A test that calls the same
implementation twice is a delegation/regression check, not an independent oracle.
For numerical bounds below `u=2**-52`; do not use a large absolute floor to hide
tiny nonzero values. Each failure must identify its fixture, quantity and bound.
In a term-scale bound the scale is the sum of absolute defining addends from
the independent oracle, evaluated at the fixture inputs, before inspecting the
runtime discrepancy. Exact zero cases receive explicit branch/zero checks.

| Gate / accepted claim | Runtime ownership | Independent oracle and existing evidence | Exactness / pass condition | Future location / failure meaning |
|---|---|---|---|---|
| P1 one-step recurrence, order and zero convention | `dynamics.step3/phase_sync/arg0` | Paper A §6.1; existing `test_dynamics.py` hand step, simultaneous sync and signed-zero tests | Independent SymPy rational pre-sync expression; phase-off exact ideal expression, binary result within 32u times term scale; phase-on 80-digit trig oracle on bounded nonzero fixtures within 64u scale; exact branch behavior at zero | `test_parity_p01_p04.py`; equation/order/branch mismatch |
| P2 synchronized manifold | `step3`, `L3` | Paper F F1, k=(1,1,1); general equal-k direct substitution | Exact symbolic L3 e=0 and scalar map; binary tests within 32u term scale including common zero; no claim for unequal k | Same; synchrony/parameter error |
| P3 S3, conjugation, U(1) | `step3`, `z_chiral` | Paper B §§7,9; `test_face_state.py` parity/parameter tests; `test_dynamics.py` zero qualifications | Exact polynomial identities phase-off; all six permutations jointly permute k; conjugation for real parameters; U(1) on nonzero pre-sync stratum or lambda=0 globally. Bounded binary comparisons 128u term scale, plus a counterexample to global nonzero-lambda U(1) at zeros | Same; wrong sign, labels, or overbroad symmetry claim |
| P4 covering | `cycle_laplacian`, `pullback_matrix`, `isometric_pullback`, `step_ring` | Paper A §§2–3,6; `test_covering.py` all 10 methods | Exact matrix identities for divisors, incidence multiplicity for sizes 1/2, nondivisor witnesses; nonlinear lift uses P at M=3,6,12,24 within 128u term scale including zeros and unrestricted ring wrap | Same; covering/domain/wrap drift, not unrestricted long-time machine closeness |
| P5 388-row saved trajectory | `step3`, `advance_clock`, `advance_ema`, observations/readouts | Local `research/GATE_TORUS_INVESTIGATION_v0.1/TRAJECTORIES.csv`, `REPORT.md` §4, `RESULTS.json`, `investigate.py` | Hash and exactly 388 rows first; two 96-step runs at lambda=0/.001, seed/presets per report; preserve row order, clocks, initialization and state/readout columns. Omega and order-one observer scalars/vectors: absolute+relative bound 1e-12 on these bounded fixtures; counters/markers exact; all finite. Near-zero C and accounting residuals use the scale-sensitive rule below, not the blanket bound. Require bitwise same-environment Runner versus step-only control. Do not compare research registration/display_M as kernel science | `test_parity_p05_p06.py`; orchestration/record regression. Fixture publication prerequisite O03 |
| P6 18-row falsification | `step3`, `z_chiral` | Tracked Paper-F support `TRANSVERSE_AXIS_FALSIFICATION.csv` and report; two seeds e+i*.001*u/v, eight updates, eps=.05,g=.2,k=1,lambda=0 | Exact fixture hash/count, reconstruct states/C within 1e-13 absolute + 1e-12 relative; recompute projective angles using recorded orientation/validity convention within 1e-12 rad using stable atan2 of cross-norm/dot; preserve nonzero-valid flags, mutual pi/2 separation within 1e-12. Numeric zeros are not proofs; do not import research runner | Same; lost isotropy, seed/order/sign error |
| P7 Paper F generic-seed predictions | `step3`, `z_chiral` | Paper F F5,F8,F9,F12 / exact verifier; exact one-step projections, finite-n jet coefficients, kappa-infinity=13375/1107936648 at historical parameters | Symbolic projection/jet identities exact. Generic phi=+/-pi/12, h=.02 and .01, eight steps; compare C and signed angle to independent 80-digit full-map oracle within 1e-13 C and 256u radians; require the predicted opposite signs/sign reversal wherever the independent predicted magnitude exceeds four times that angle bound. Compare jets to exact coefficients separately; retain O(h^6) remainder, never assert truncated series exactly equals finite-amplitude output or certify infinity from 8 steps | `test_parity_p07_p08.py`; coefficient/angle-convention drift; no new F subsystem |
| P8 first lambda derivative | `step3` full composition, `z_chiral` | Paper F theorem 8, Appendix D, F13–F14; exact verifier | Exact symbolic derivative: one-step 99/2500, limiting 34494041501/849664304944 under stated hypotheses. Independent high-precision differentiated full-map check; binary centered finite differences only as bounded corroboration on nonzero chart, multiple deltas, estimated truncation+roundoff envelope. Do not fit away a mismatch or use isolated-phase 243/160 as the full coefficient | Same; wrong composition/observable/derivative scope |
| P9 observer identities and passive updates | `z_manifold` and delegated C | Paper E (1),(2),(8),(13),(15),(39),(40); `test_z_manifold.py` (37 existing methods), K2 receipt | Exact cone/norm/harmonic/EMA rational identities; existing mpmath fixtures/tolerances retained; macro residual <=8u*z^2; literal .01 innovation and constructor-zero semantics checked independently. Same Omega sequence with/without observations must be bitwise identical | `test_parity_p09_p10.py`; observer state or historical-definition drift |
| P10 accounting and display qualifications | `z_diagnostics` | Paper E (16)–(28),(33)–(38); existing 36 methods and K3 receipt | Exact norm/Q/Gram/slack/gradient/budget identities; numeric residual <=256u times sum of absolute defining terms on bounded fixtures, plus existing degree-sensitive underflow/overflow rejection tests. Inconsistent supplied records stay inconsistent; explicit overshoot and history-dependence witnesses | Same; omitted terms, clipping, state feedback, or display information loss hidden |
| P11 accepted C geometry and D option | `geometry`, `reference_scaffold` | C printed coordinate/face tables and D (1)–(29); `test_geometry.py` 16 methods; `test_reference_scaffold.py` 39 including R1 | Exact symbolic coordinate/edge/face/section equality, 18/21/3 mesh, 3 seams, 2 nine-edge loops, Euler 0, 12 D3h actions; D closed-halfplane and full frame identities, role-preserving symmetry and substitution-first regressions. No floats in exact interface | `test_parity_p11.py`; geometry/index/closed-set/type drift |
| P12 software contract | Public facade/Runner/records; delegated authorities | This document; existing purity/import spies and frozen-data tests are partial precedents | Exact no-mutation/delegation/count tests; explicit signatures/no historical defaults; clean-process import graph; repeat observation inert; zero-update and restart-prefix equivalence; both schema round-trips, malformed inputs, signed zeros, large counters, exact codec and separate records. No research imports or geometry/observer feedback | `test_public_contract.py`, `test_runner_records.py`, `test_geometry_records.py`, `test_import_boundaries.py`; engineering contract failure |

For P5, compare raw C both to the saved C and to an independent high-precision
cross product of each candidate Omega. For cyclic component (j,k), use
`64*u*(abs(x_j*y_k)+abs(x_k*y_j))` for evaluation roundoff; when comparing
two differing trajectories add the exact high-precision difference of their
cross products to that bound. This separates state drift from readout drift
and does not require a numerically unresolved late sign to be preserved.
Accounting residuals use P10's term scales; historical alignment flags use
the stated threshold, not exact-zero inference.

P8's adaptive finite-difference envelope is computed from an independent
high-precision oracle before judging runtime values; it cannot be selected from
runtime discrepancy. Exact derivative identities are the controlling gate.
P7/P8 analytic locality, nonresonance and limit interchange remain proofs in the
accepted Paper F; finite tests cannot certify those theorems. Existing evidence
reports 131 exact Paper-F predicates, not a newly executed K0 test suite.

Fixture identities freshly read in K0 (no trajectories regenerated):

* P5 local CSV: 388 rows, SHA-256
  `eeed672b1cb20321dfc85a2f4753c93d4fe1b9345a5cede4f5e12532537a4a38`.
* P6 tracked CSV:
  `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION.csv`,
  18 rows, SHA-256
  `fb2b2a71fd99c536dc7e490c6a2e201b2a0b22ee533820870dff5ee516c468dc`.

## 10. OPTIONAL-module decision package

These existing explicitly chosen constructions are classified OPTIONAL. Their
inclusion in the **new supported v1 facade** remains OPEN; an optional runtime
module already being tracked does not settle that product/support decision.

| Module | Complete significant contents / dependencies / callers | Provenance and support risk |
|---|---|---|
| `boundary_response.py` | RESPONSE_ID; theta_from_lens; lens_area_fraction/gain; prepare_area_response; ResponsePrecisionError re-export. Private numeric helper dependency; imported by srg; local response/pipeline tests; tracked readouts/face tests use helper exports | Explicitly adopted `lens_area_norm_v1`: area-norm toy preparation, not a law of A–F or shell boundary condition. Inclusion risks implied physical attachment and conservative small-number domain confusion. Quarantine removes public preparation convenience, not core recurrence/chirality. |
| `srg.py` | NovemberParameters/NOVEMBER; SRGOperators; fourier_basis; fixed_november_srg; GAUGE_ID; HelicityMode/helicity_mode; project_bra; extract_helicity; HandoffResult/metadata; handoff_area_response. Depends on boundary_response/numeric helpers; operating_region imports handoff; tracked readout tests use Fourier basis; local SRG/pipeline tests | Fixed historical November operators and reviewed conditional reduction; not Paper-A evolution. Inclusion commits to gauge, branches, tensor order, transfer counts and literal provenance. Quarantine removes supported initialization route but leaves explicit user-supplied Omega available. |
| `operating_region.py` | PROFILE_ID; UNIFORM_INCIDENT_BUDGET; bounded_config; validate_bounded_triad; validate_uniform_incident_budget; initialize_bounded_area; step_bounded_triad. Depends on dynamics/srg/numeric helpers; FaceState imports it and optionally calls bounded step; local profile/pipeline tests and tracked face tests | Adopted radius-three sufficient profile at eps=1/20,g=1/5,k in [0,8]. Wraps one step3. Exact boundedness is not machine safety/convergence. Inclusion risks presenting the profile as the full recurrence domain. Quarantine requires documenting that FaceState's profile path is outside new supported v1. |

The package README's predecessor links resolve outside this repository to
`C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md`.
Targeted inspection confirms the user's adopted toy option, conditional SRG
reduction and scoped profile, including retraction of radius-ten and very-long-
trajectory safety claims. That is predecessor evidence, not an A–F theorem or
new support decision. Paper B Appendix A explicitly says inclusion of these
transitive helper modules does not adopt a physical subsystem. There is no
second recurrence to promote. Repository tracked callers were located with
`git grep`; untracked research consumers are not supported-runtime callers.

The local-only predecessor tests are present and their bytes freshly match the
published closeout's identities:

| Path under `kernel_physics/tests/` | Methods (static census only) | SHA-256 |
|---|---:|---|
| `test_boundary_pipeline.py` | 4 | `e820c5ea52c3d53f580cac1427d97935a45a8c35ea10da120b00447c437f64c9` |
| `test_boundary_response.py` | 8 | `6d95629e69ebc0d80c9d16f39286b4c26ce1f4a47c05346cb49b467365cfefe7` |
| `test_operating_region.py` | 9 | `c873358fcf618bc62a8b0277660cc19fa057273f14c169a521e09d5683d33c35` |
| `test_srg.py` | 9 | `a74119c3211e7f790a99a0f3eba2574bffaa45482e8a7a3b9ff5a597f28fed59` |

Coverage includes high-precision lens evaluation, exact-zero/underflow handling,
strict types, SRG operators and gauge, full-space extraction, direct transfer
comparison, raw metadata, actual-state bounds, sufficient-versus-necessary
budget, signed-zero behavior, sole step3 delegation, and composed pipeline.
The current static census is 177 tracked plus 30 local-only method definitions.
The **207/207 local and 177/177 isolated passes are predecessor results** from
`K1_K2_K3_PARITY_CLOSEOUT.md`, not fresh executions.

**Option A — support.** Authorize explicit facade wrappers, publish the four
unchanged predecessor tests after bounded provenance/dependency review, and
freeze their accepted option/profile/gauge identifiers, counts and failure
semantics. Add integration/delegation/import/initialization-record coverage;
run both full local and clean published-package checks in K1/K2. Do not add the
option implicitly to `run`; initialization stays separate. This extends the
K1 file/symbol allowlist and needs explicit approval of that extension.

**Option B — quarantine.** Formally declare these three modules unsupported by
v1; preserve files and local tests. They must not be imported by the initial
facade/Runner. Existing internal direct callers remain legacy opt-in surface,
including FaceState's profile path, outside new compatibility guarantees. Do
not remove the shared `_response_numeric` helper: raw chirality and observers
already depend on it. K2 verifies that the facade cannot activate quarantine.
This leaves the completeness/publication obligation documented, not erased.

Neither choice is made here. Pending the decision, K1's base allowlist below
does not expose or activate these candidates; this temporary decision boundary
is not a declaration that Option B has been selected.

## 11. OPEN items and research exclusions

| ID | Classification / unresolved item | Disposition and adjudicator |
|---|---|---|
| O01 | OPEN: v1 support of boundary_response/srg/operating_region | Await GPT/Hilmir A or B (or explicit base-only deferral); no silent choice |
| O02 | OPEN: original rationale for eps=.05, g=.2, historical seed, and observer lock .244 | Literal values and current ownership are known. Original motivation is not fabricated; preserve Paper F's provenance-open statements. No blocker for explicit presets. |
| O03 | OPEN: publication/packaging of P5 local golden fixture and its minimal provenance | K2 release prerequisite; review and authorize a bounded fixture copy/receipt separately, not all gate/torus research. K0 pins bytes only. |

There is no OPEN accepted formula, recurrence owner, index meaning or observer
update order in this freeze. If one is found, stop under SG3/SG4/SG5/SG10;
this document does not authorize interpretation or correction. Optional-module
publication and historical rationale are deliberately bounded decisions, not
unclassified mathematics.

RESEARCH_ONLY exclusions: spatial registration of M/C/T, gate/aperture
assignments, finite-patch exposure, restoring/spring laws, EM and
Riemann–Silberstein comparisons, physical fields, toroidal physical motifs,
Paper-F normal forms/linearization as runtime, six-axis physical selectors,
historical spatial-alignment narratives, Twisted Hex Crystal and its family,
warp/physics investigations, diagnostic spike thresholds as controllers, Z
feedback, mechanical clocks, Paper-A feedback/stability experiments as new
runtime, historical viewer percentile scaling, and inferred physical units.
Accepted historical torus **display** helpers remain OPTIONAL passive adapters;
that does not admit toroidal physics. Diagnostic alignment's threshold remains
HISTORICAL and cannot become a dynamics law. Research assets are preserved.

## 12. Exact proposed K1 authorization boundary

Create only these production files under `kernel_physics/`:

| New file | Responsibility |
|---|---|
| `api.py` | Supported exports and thin delegation functions with explicit signatures |
| `_contract_types.py` | Detached public values and input/provenance validation |
| `_runner.py` | Section 4 schedule, restart, no equations |
| `_records.py` | RunRecord, numeric codec, schema validation, canonical hashing |
| `_geometry_records.py` | GeometryRecord, exact codec and delegated C/D serialization |
| `_presets.py` | Only named seed/observer presets above and their literal provenance |

Create the four P12 test files in section 9. Minimal documentation edit allowed
in K1: `kernel_physics/README.md`, to link this freeze and show public imports
and explicit construction. Do not change `__init__.py` merely to re-export the
facade. No dependency installation/change, package restructure, UI, CLI,
visualizer, alternate recurrence, geometry family, or research import is needed.

Authoritative **untouched** files: every existing `kernel_physics/*.py`, including
dynamics, covering, geometry, face_state, readouts, reference_scaffold,
z_manifold, z_diagnostics, numeric helpers and the three candidate option
modules; every existing test; accepted paper source/PDF; research and evidence.
Facade implementation can be completed without editing any mathematics file.
Any later proposed modification requires exact justification and new scope.

K1 must add meaningful tests for explicit constructors, correct delegated
selection, input isolation, one-step counting, multiple independent observers,
row-zero modes, zero updates, restart/replay, schema failure cases, exact record
round-trips, indexing, separate geometry, and import boundaries. K1 must pass
P12 and relevant existing regression tests in an isolated tracked export;
record local-only coverage separately. K2 implements the P1–P11 independent
parity suite at the filenames above, with O03 resolved before a portable P5
claim. K1 may use existing oracle fixtures but cannot claim all gates completed.
Option A requires a separately amended file/test/symbol allowlist; Option B
requires its explicit support disposition, not deletion. No implementation is
authorized by completion of this K0 documentation task alone.

## 13. K0 verification and publication boundary

K0 used `conda activate torment` through its PowerShell hook. Read-only Python
inspection reported Python 3.11.15, NumPy 2.4.4, SymPy 1.14.0, mpmath 1.3.0,
at `C:/Users/Notandi/miniconda3/envs/torment/python.exe`. This differs from the
predecessor execution environment and is not represented as a repeat of it.
Python was run with `-B`; no scientific module or research runner was executed
for a trajectory, and no test suite was run. Static AST method counts, CSV row
counts, hashes, import inspection and document consistency checks are fresh
K0 observations, not test passes.

The only K0 file additions are this document and the ledger. Final validation
requires `git diff --check`, manual review of both staged new-file diffs, an
exact two-file staged allowlist, unchanged starting source/test/research/paper
blobs and unchanged predecessor hashes. Commit message:
`freeze kernel authority and public contract for K0`. Publish by an ordinary
fast-forward push to the existing main only after those checks and a matching
remote preflight; never force, reset, clean or include unrelated untracked data.
The final Git commit identifies this packet; it is intentionally not embedded
inside its own content. Runtime, tests, published research, accepted papers and
Twisted Hex research remain unchanged. No geometry, coupling, feedback or
hidden historical default is created by K0.
