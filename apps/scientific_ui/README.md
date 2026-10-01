# Trioctagon Scientific UI — v0.1.2 read-only artifact inspection

UI DISPLAYS SCIENCE. PYTHON KERNEL COMPUTES SCIENCE.

This separately installed Windows x86-64 / CPython 3.11 application consumes the
certified kernel through `kernel_physics.api`. It does not bundle or modify the
kernel, Qt, Matplotlib, papers, research or scientific fixtures. The application
source/version and kernel source/version are distinct identities.

P2 adds strict Historical result and attempt-receipt inspection in the same
**D → Records & Reproducibility → Artifacts** area. The inert public parsers from
`trioctagon-historical-protocol==0.1.0` are pinned by
`historical-protocol-artifact.lock.json` to the certified H6A wheel SHA-256
`734ae5d2734ce9b42301b851e23d57c4b9db37ac02b32b0fadff328d4724952f`.
The Historical scientific kernel is neither installed nor imported by this UI.
No Historical provider, issuer, equation replay or cross-kernel comparison is used.

Only Historical result/receipt family schema 1.0.0 is routed. Unknown schemas,
requests, catalogues and provider-build documents are refused. The public Core
envelope probe bounds the inert read and rejects ambiguous/duplicate fields;
Historical literal hints then select one public Historical owning parser.
Original canonical bytes are retained, never normalized or modified.

Five result views show stored step, run, staged Z, EMA H and probability-chart
fields. Run rows 0…N−1 and the historically unstored terminal have separate tabs;
N=0 has no rows and a constructor terminal. Cached constructor readouts retain
HISTORICAL_CONSTRUCTOR_ZERO, distinct from RECOMPUTED. Raw C pairs remain ordered
23,31,12; chart components remain (cu,cx,cy). Neither is labelled physical XYZ.
Exact f64 tokens remain authoritative when decimal precision changes. The EMA
view explicitly shows equal input/output memory tokens and zero memory advances.

Frozen qualifications have a read-only tab. Original artifact claims and current
viewer observations have separate named panels. Schema/digest validity does not
authenticate execution, historical authorship or physical validation. Producer
execution attestation stays UNAVAILABLE, Windows execution binding NOT_PROVEN,
and production attestation NOT ENABLED. LOCAL_CHECK_PASSED is never promoted to
VERIFIED. Historical receipts are explicitly NOT A SCIENTIFIC RESULT (N18).
Historical selection never becomes a Core record, resume/checkpoint, current
state or comparison input (N21). Parsing cannot imply replay or attestation (N34).

Certification runs source and installed/offline UI tests, frozen analysis and
Historical protocol regressions, and relevant Core record tests. Test tools have
a separate environment. Immutable H6A/H6B test artifacts retain their original
identities in `tests/fixtures/historical/manifest.json`; UI tests do not generate
Historical science. The external closeout supplies the certified Windows CMD
launch command and six operator-review files; manual review is a separate step.

UI-P1 adds **D → Artifacts**, alongside Records, Compare, Datasets and Exports.
Load a local file to inspect a canonical DerivedAnalysisRecord or AttemptReceipt.
The separately installed `trioctagon-analysis==0.1.1` loader is pinned by
`analysis-artifact.lock.json` to source `df6295b6b5dc581a0bdec8601bae9cc3e14493bd`
and wheel SHA-256
`90394bd97150bc03630de1cfd8bd868547f1cdb935b1a250b874bbe72320cf18`.
The acquisition tool reconstructs this exact archive from the pinned source and
checks all 32 members. It never resolves analysis from a registry. Install analysis
with `--no-compile`; the viewer checks installed members and module origins before
loading an artifact and refuses extra runtime files, including bytecode caches.

APP04 displays the stored requested fields, in request order, with numeric axes
0/1/2, authoritative f64 tokens and secondary decimal text preserving signed zero.
There are no new scientific calculations, plots, comparisons or execution controls.
Recorded VERIFIED producer claims remain CLAIMED_ONLY; viewer execution verification
is UNAVAILABLE and Windows execution binding remains NOT_PROVEN. A valid receipt is
a refused/failed/cancelled attempt, never a scientific result. Existing legacy
analysis remains a validated session cache, with no external legacy import or conversion.

Import limits are 16 MiB/file, JSON depth 32, 64 accepted analysis artifacts and
128 MiB of retained canonical bytes. Diagnostics are limited to 8 KiB and raw text
previews to 1 MiB, including truncation indicators. Reparse points and remote paths
are refused. No parent or provenance locator is resolved. Absent external expected
identity is shown as unavailable; the observed SHA-256 is not its own independent witness.
These are viewer limits, not provider execution resource limits.

Copy uses retained bytes, owned same-directory staging, flush/fsync, atomic hard-link
publication without replacement and emitted SHA-256 verification. Existing paths,
including the source, are refused. Failure cleanup removes only owned staging;
a published destination is never deleted to hide a verification failure. Filesystems
without hard-link support fail closed. The status is a local UI copy observation,
not an analysis AttemptReceipt. Source files and cached bytes remain unchanged.

Selecting Artifacts isolates Core resume/checkpoint/save and figure/CSV export
sources, including after changing tabs. Explicitly select a Core record in Records
to restore Core actions. The
request/response v2 worker files are unchanged; the existing draft-format version
marker remains 0.1.0 for compatibility, independent of the installed UI version.
Analysis files never enter RecordView, ComparisonView, sweeps or the scientific worker.

On Windows, GUI startup explicitly selects the OS ICU library required by the
locked Qt build, avoiding the incompatible `icuuc.dll` in Conda's DLL search path.
This does not alter Conda, PATH or scientific-worker startup.

The [release identity and draft notes](../../RELEASE_v0.1.0.md) distinguish the
repository/UI candidate from the older certified kernel used by this application.
Registry-name availability is not certified. Do not install either project by an
assumed public registry name. No tag, public release, upload, installer or frozen
executable is created by release preparation.

Only **Windows x86-64 / CPython >=3.11,<3.12** is certified. Other operating
systems/Python versions are NOT CERTIFIED BY v0.1.0. No GPU, LLM or embedding
model is required. Normal installed runtime is offline; initial source/dependency
acquisition is separate. This mathematical research UI claims no experimentally
validated physical theory; see the [scientific boundaries and license scopes](../../README.md).

## Exact installation inputs

- Kernel: the preferred **direct wheel** in `kernel-artifact.lock.json`, from K3c
  Actions run 36291131581, or strictly verified reconstruction of the same source
  `7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e`.
- Analysis: independently reconstructed exact wheel in `analysis-artifact.lock.json`;
  no bundling with the UI or Core, and no version-only substitution.
- Historical protocol: independently reconstructed exact H6A wheel, installed with
  `--no-compile`; the viewer verifies its installed contents and module origins.
- Runtime: the complete 15-wheel closure in `requirements-win-py311.lock`, with
  every archive SHA-256 enforced. NumPy 2.4.4, SymPy 1.14.0 and mpmath 1.3.0 remain fixed.
- Build: Setuptools 81.0.0 and wheel 0.47.0; archive hashes are in `pyproject.toml`.
- Application: an ordinarily built companion wheel. Its contents include original
  application modules/help, license metadata, and installed lock data only.

The preferred kernel archive remains classified as a
TEMPORARY_CERTIFIED_DEVELOPMENT_ARTIFACT in the unchanged lock. Lock v2 accepts
certified reconstruction from the exact frozen K3 source with locked build tools
and the narrow wheel-equivalence v1 contract below. Actions retention is not a
required source of installation bytes. **Do not substitute the root kernel built
at the repository/UI candidate commit:** its source identity differs from this lock.

## Public installation

Install Git and a clean Windows CPython 3.11 x64 interpreter with the `py` launcher.
Use a fresh checkout (or start at the root of an existing clean checkout). Keep
the acquisition/build/install workspace outside it. Run in PowerShell:

```powershell
git clone https://github.com/pzychozen/trioctagon-physics
Set-Location trioctagon-physics
$source = (Get-Location).Path
$work = Join-Path $env:TEMP ('tri-ui-' + [guid]::NewGuid().ToString('N').Substring(0,8))
py -3.11 -m venv "$work/bootstrap"
$bootstrapPython = Join-Path $work 'bootstrap/Scripts/python.exe'
& $bootstrapPython -I -B "$source/apps/scientific_ui/tests/test_install_launch.py" --acquire --source $source --workspace $work
& $bootstrapPython -I -B "$source/apps/scientific_ui/tests/test_install_launch.py" --certify --source $source --workspace $work
$certification = Get-Content "$work/latest-certification.json" -Raw | ConvertFrom-Json
$uiPython = $certification.installed_runtime
& $uiPython -I -B -m trioctagon_ui --smoke-test
& $uiPython -I -B -m trioctagon_ui
```

Check each command succeeds before continuing. After a release tag exists, check
out that approved tag before acquisition/certification. Source and dependency
acquisition may use the network. `--acquire` first tries the locked preferred
Actions artifact when GitHub CLI/access is available. Missing `gh`, missing `gh`
authentication, unavailable/expired artifacts or retrieval failure without received
files permit exact-source reconstruction. Git is still required. For a public
repository, that Git source fetch does not need a GitHub token. Received malformed
identity, corrupt downloaded/cached evidence or a partial failed download remains
fatal; inspect it rather than rebuilding around failed verification.

Acquisition also performs a forced reconstruction from the exact locked source
even when the preferred archive is selected, preserving certification coverage of
both routes. It builds that kernel externally with locked tools and verifies its
origin, commit, manifest, all stable members and RECORD. All builds/installs after
dependency/source acquisition use the locked local wheelhouse with `--no-index`.
`--certify` creates disposable build/runtime environments, copies application
sources/tests outside the checkout, builds the UI wheel, installs the selected
kernel, runs the application suite and writes external JSON/log evidence.
No build output belongs in the repository.

While the repository is private, Git source acquisition still requires authorized
access. Local/offline fallback testing does **not** prove anonymous access to the
private endpoint. A final anonymous public-endpoint acquisition/install smoke is
required after visibility changes and before announcement.

For a separate manual offline installation after the commands above, use the
**actual verified selection** in `kernel-selection.json`. Its relative path may
identify either the preferred wheel or a reconstructed wheel; do not assume the
preferred directory exists. The certification above verifies that selection
before these installation commands:

```powershell
& $bootstrapPython -I -B -m venv "$work/manual"
$uiPython = Join-Path $work 'manual/Scripts/python.exe'
$selection = Get-Content "$work/kernel-selection.json" -Raw | ConvertFrom-Json
$kernelWheel = Join-Path $work $selection.relative_path
$analysisWheel = Join-Path $work 'analysis-wheelhouse/trioctagon_analysis-0.1.1-py3-none-any.whl'
$historicalProtocolWheel = Join-Path $work 'historical-wheelhouse/trioctagon_historical_protocol-0.1.0-py3-none-any.whl'
$appWheel = $certification.app_wheel
& $uiPython -I -B -m pip --isolated install --no-index --require-hashes --find-links "$work/wheelhouse" -r "$source/apps/scientific_ui/requirements-win-py311.lock"
& $uiPython -I -B -m pip --isolated install --no-index --no-deps $kernelWheel
& $uiPython -I -B -m pip --isolated install --no-index --no-deps --no-compile $analysisWheel $historicalProtocolWheel
& $uiPython -I -B -m pip --isolated install --no-index --no-deps $appWheel
& $uiPython -I -B -m trioctagon_ui --smoke-test
& $uiPython -I -B -m trioctagon_ui
```

The installed `trioctagon-scientific-ui` launcher is also available in that
environment's Scripts directory. Run from any directory; no PYTHONPATH, editable
install or source checkout is required. Installed lock data is located through
distribution metadata, independently of the launch working directory.

Stage A found a Conda ICU DLL collision; UI-P1 selects the required Windows system
ICU explicitly during GUI startup. Certification still uses fresh, isolated venvs.
Do not delete/rename system or Conda DLLs to force an import.
Keep the disposable workspace path short on Windows hosts without long-path
support: the published Qt wheel contains deeply nested supporting files.

## First run and four workspaces

The scientific session starts blank. Run is disabled until required inputs are
valid. Applying the named seed, an explicitly chosen L01 parameter fill, and the
separate labelled example-count action is a convenient first run. Each is a user
action, never an invisible default. Advanced disclosure exposes all Omega real/
imaginary fields, k0/k1/k2, the initial index and editable source descriptors.
The equal-k helper copies the entered value visibly into all three fields.

A — Dynamics: inspect the explicit request, submit zero/one/N updates, inspect
stored Omega/chirality plots, complex planes and the exact selected-sample table.
The topology is explicit: triad or ring. Slider ranges are DISPLAY_RANGE_ONLY;
typed off-tick/out-of-range values are retained without clamping or normalization.

**Accepted v0.1 known issue:** numeric sliders may react to mouse-wheel events
and replace a precisely typed parameter value with a slider tick value. Before
Run, verify the visible/resolved request values. Completed records remain immutable
and retain the values actually used. The risk of an unintended experiment is real;
typed-value retention does not prevent a later wheel event from changing it.

B — Observers & Diagnostics: add multiple independent named/custom observers, or leave the list empty. All
readouts/diagnostics initially remain unselected. Accounting/alignment selections
require an explicit observer; the UI never silently attaches one. Results are
passive, preserve signs/residuals/flags, and do not feed back into Omega.

C — Geometry: explicitly choose C01 with an ordered exact section-height list or one of the six supported D03 constructions. Enter the exact options required by that construction. Exact record data appears in an inspector;
the separate CPU wireframe evaluates returned exact nodes and uses returned
incidence/order. Rotate/pan/zoom with the plot toolbar/mouse, reset the camera, or
toggle object visibility. Separate coordinate frames have separate axes.
No Omega-to-shell attachment, welding, new intersections or physical coupling exists.

D — Records & Reproducibility: inspect the digest, original inputs, repository,
commit, API/schema/ledger/package versions, 14 module hashes, paper references,
producer environment and canonical raw JSON. History retains previous completed
and loaded records. Draft edits never mutate recorded history.

## Save, load, resume and checkpoint

Save current record writes the exact worker-validated canonical JSON atomically;
no pretty-print rewrite, added fields or new digest is generated. Load record
uses a public loader in the worker. Structure/digest validity is not scientific
replay certification or producer authentication. Producer and viewer environments
are distinct. Before a current public result, runtime source identity is unknown;
expected artifact and installed distribution version are shown separately.

Save/load draft is APPLICATION DATA, NOT A KERNEL RECORD. It retains original
spellings, resolved binary64 hex values, preset origins and change notes. V1 draft documents migrate in memory to v2 named-observer descriptors, preserving provenance and values; future saves use v2. Raw v1 worker IPC is rejected.
It does not run science when opened. Edited historical inputs lose their historical
label. O02 remains unresolved; .05/.2/.244 are not claimed scientifically optimal.

Resume submits only the selected RunRecord and explicit additional updates to
`api.resume`. Parameters/observers cannot be overridden. An incompatible source/
module identity produces the original kernel error. Resume with zero updates is
a real continuation operation, not a read-only compatibility probe.

Prepare new checkpoint draft copies the selected sample's stored bits/index.
Choose parameters/outputs, explicitly acknowledge selected observer initialization,
then Run checkpoint draft. This calls a new `api.run`, recording parent digest/
sample lineage in checkpoint provenance. It does not claim to resume old history.

## Worker and request contract

Request v2: `ui_request_version`, `request_id`, `operation`, `payload`.
Operations: run, resume, new_checkpoint_run, geometry, load_record, passive_analysis. Run/checkpoint
payloads contain original draft strings and matching resolved hex values. Resume
contains canonical parent JSON and update text; geometry contains definition_id, fields (original exact spellings), and matching exact_nodes; load contains record_json. Unsupported payload keys fail.

Response v2: `ui_response_version`, matching request_id/operation, status, and
either result (result_kind=record, canonical_json, record_type, deterministic_sha256, source_commit,
produced_current), a detached analysis result described below, or error (exception_class, original message, action, traceback).
Import/network/isolation audit fields accompany the response. The controller
rejects incomplete, mismatched and cancelled responses and preserves child stderr.

One subprocess uses an absolute interpreter with `-I -B -m trioctagon_ui.worker`
from its unrelated temporary job directory. IPC is UTF-8 JSON files with atomic
publication, never pickle, shell commands, HTTP or sockets. The worker imports no
GUI stack and performs science through the public facade only. Plots/sample
selection use a detached cache and invoke no worker/science.

## Responsiveness and troubleshooting

The job panel shows state, elapsed time and requested samples, without fabricated
percentage progress. Above 10,000 samples an explicit application warning appears;
it is not a kernel limit. Cancel terminates the worker, then kills it after a
bounded grace period if needed. Previous records survive failures/cancellation.

Errors retain exception class, message, operation/request ID and technical details.
ResponsePrecisionError is not interpreted as zero or stable decay. No automatic
scientific fallback occurs. Missing series display “not recorded.” A display-only
failure leaves exact record inspection/export available.

Normal runtime is offline and needs no model, Torch, TensorFlow, Transformers,
CUDA or GPU renderer. Audit hooks reject Python network attempts. No CDN/static
web service exists. Qt Widgets/Matplotlib Agg and table alternatives support CPU
use. Keyboard-accessible controls and text/table alternatives are tested with a
real Qt application; this is not a claim of completed assistive-technology certification.

License boundaries and exact dependency notices are in LICENSE_SCOPE.md and
THIRD_PARTY_NOTICES.md. Qt remains LGPL-governed and replaceable; its actual wheel
notice omission and supplemental license texts are recorded. No dependency binary
is bundled or relicensed Apache-2.0.

## Ring editing

Advanced Dynamics selects triad/ring and UI row count q (state_size=3q). The UI
row guard is q=1..1000, a resource guard rather than a kernel domain. Increasing
q adds blank real/imaginary rows; reducing q requires confirmation if nonblank
rows would be discarded. Topology changes retain all values and completed records.
A triad with more than three rows remains visibly incompatible until explicitly
resized. Historical triad seed fill is unavailable for q>1 and is never repeated.
Ring run refuses all passive selections. Use the explicit clear action to remove
them. Ring chirality is unsupported, not inferred. Visibility can show any stored
channel; default channels 0–2 are a labelled subset and all channels remain in tables.

## Custom observer descriptors

Add staged/EMA custom observers as blank fields, or add either historical preset.
Each custom descriptor has mode, observer_id, variant, clock (q,N,t,q_step), dt,
initialization, config, memory, provenance and origin. Staged config contains
lambda_vp/gamma/theta_lock/alpha/beta; EMA omits gamma and requires memory.m.
All numeric fields retain text and resolved hex; clock integers retain exact values.
IDs are unique. No field is silently filled for a newly added custom observer.
Preset rows show their literal values read-only. Explicit conversion copies those
values, retains the historical origin note, and changes the claim to CUSTOM /
USER-SUPPLIED before editing. Observer provenance records every input spelling.

Clock dt is not a dynamics timestep. N>=1; q/q_step may be signed. Public memory
requires |m|<=1. Constructor-zero run initialization requires update_index=0 and
EMA m=0. Kernel constructors/runner remain final authority. No theta wrapping,
retention/innovation control, clock sharing or observer feedback is introduced.

## Detached passive scratchpad and result schema

The scratchpad operation selector creates an explicit JSON form whose scientific
values are blank strings. Edit JSON as data, or explicitly copy visible Dynamics
or selected observer fields. Sources are explicit scratchpad input or an explicitly
selected stored triad sample, visibly identified by parent digest/sample ordinal.
Stored sample selection replaces Omega/index only; other fields remain explicit.
The separate Dynamics Step preview button calls api.step and produces detached
application data. One update continues to call api.run(updates=1) and creates a record.

Supported standalone actions: step_preview; advance_clock; advance_ema;
observe_staged; observe_ema; quadratic_form; readout_accounting;
chiral_area_accounting; intensity_budget; potential; historical_alignment; and
cylinder_point. Standalone observe functions recompute a readout; their public
signatures do not offer constructor-zero replay. Cylinder point requires explicit
kappa/q/z/N, with no hidden N=12. Vector/accounting inputs are explicit supplied
values, not silently recomputed or repaired.

Passive request payload: analysis_type, inputs, source. Source is {mode:explicit}
or {mode:record,record_json,sample_index}. Each analysis has an exact input-field
matrix implemented by analysis_template. Completed detached result fields are:
result_kind=analysis, analysis_type, parent_digest, parent_source_commit,
sample_index, inputs, data, qualification. Parent fields are null when absent;
whole-history analyses use sample_index=null and list all selected sample ordinals.
Float results use {f64:float.hex()}, complex results use re/im, arrays become lists,
and public dataclasses retain named fields. No private codec is used.

Detached current-public-API analysis is not a RunRecord, GeometryRecord or replay
certificate. Parent source identity is context, not an independently exposed
current implementation identity. Analyses have an immutable cache separate from
record history, with lineage visible in workspace D and every result field in the
workspace B table. Selecting a record never deletes or modifies that cache.

## History coordinates and playback

Explicitly select a RunRecord and a recorded observer. Direct history selects
Z_macro/Z_chiral/Z_total and calls the corresponding public history helper once.
Cylinder/torus inputs use stored observer scalar z and stored observer-state q as
phi_index. N is explicit. Kappa is only a labelled DISPLAY_DERIVATION_ONLY square
root of recorded chiral_area_accounting.intensity or intensity_budget.intensity_before.
The chosen diagnostic must exist for every sample and be nonnegative. Its exact
parent path is retained; missing diagnostics are never recomputed.

History torus additionally requires explicit R/r_max with R>r_max>0. Its returned
normalization, z_max, H_z, regularizer, R, r_max and N appear alongside coordinate
tables. The entire supplied stored history is normalized once. Playback only moves
a marker through cached coordinates; it never normalizes prefixes or interpolates.
Observer-vector coordinates are not physical placement; no shell overlay exists.

Play/Pause/Back/Forward/scrub operate on sample ordinals using a Qt timer. Actual
stored update_index is shown separately. Playback rate is frames per wall-clock
second, unrelated to Clock.dt, update count or physical time. Display significant
digits affect tables only; original hexadecimal spelling and plot values remain
unchanged. All raw Matplotlib Save Figure actions and their toolbar keyboard entry remain
disabled. Workspace D now provides controlled exports with mandatory provenance sidecars.

## Exact geometry entry

The grammar accepts integers, rational arithmetic, pi, parentheses, + - * /,
rational powers using ^ or **, and sin/cos calls. Example: 2^(1/2)+sin(pi/2).
Division and negative exponents are adapted as exact nodes; rational exponents
are reduced. No floats, variables, arbitrary functions, Python execution,
general sympify or parse_expr are used. Tagged nodes are reconstructed only by
explicit SymPy Integer/Rational/pi/Add/Mul/Pow/sin/cos constructors in the worker.

Application resource guards: 2048 characters, 256 tokens, parse depth 32, 64 digits
per integer literal, and absolute reduced power numerator/denominator <=64.
An additional conservative representation-growth budget of 4096 bounds composed integer/rational powers. These are application resource protections, not scientific domain assertions.
Public get_geometry validates the final exact domain.

C01 height rows preserve order and duplicates. Its w/s/beta stay read-only. The
viewer draws returned section segments and never solves intersections. D03 options:
aligned(s,g_gap), from_radius(s,p), regular(s), paper_c_member(s),
translate_paper_c_to_regular(s), shrink_paper_c_at_fixed_centres(s). Only the relevant
fields are enabled and submitted. g_gap is geometric reference length, distinct
from dynamics coupling g. Symmetry metadata stays descriptive; no inferred action
or arbitrary fold angle is exposed. Axes/object visibility and camera controls
change presentation only.

## Finite datasets and continuation

Workspace D retains Records and adds Compare, Datasets and Exports within the four
primary scientific workspaces. Dataset creation freezes a complete new-run draft.
Explicitly rebuild the plan to incorporate later draft edits. Only eps, g,
phase_strength, k0, k1 and k2 can vary; State, topology, updates and all passive
selections remain fixed. Ring drafts must already satisfy the public constraints.

Enter dimension JSON as {"g":{"values":["0.1","0.2"]}} or an explicit range
{"eps":{"start":"0.01","stop":"0.05","count":"3"}}. Numeric inputs are text.
Ranges require count>=2 and expand under Decimal precision 50 / ROUND_HALF_EVEN,
using start+(stop-start)*i/(count-1); endpoint spellings are retained. The preview
shows every spelling, binary64 hex and duplicate-resolved-value reference. Nothing
is deduplicated. Dimension order is eps/g/phase_strength/k0/k1/k2, preserving each
list's order within the Cartesian product.

Case count and cases*(updates+1) sample count are exact orchestration counts.
Above 100 cases or 100,000 samples, execution requires confirmation. The default
10,000-case UI RESOURCE GUARD is not a scientific domain limit; explicitly raise
the guard and acknowledge the override to permit up to 100,000 cases. Individual
range expansion has a 100,000-value resource cap. No silent clamping occurs.

TRIOCTAGON_UI_SWEEP_MANIFEST version 1 contains app version, spec_sha256, the frozen
specification (base draft, dimension specs/expanded values, kernel lock, failure
policy and resource guard), fixed configuration, counts and every case. Each case
has stable case-ordinal-requesthash ID, request_sha256, substituted/resolved values,
status, record path/digest/source, error and rerun reason. SHA-256 uses UTF-8 JSON
with sorted keys and compact separators. Case request identity contains operation,
draft and resolved payload, excluding the transient worker UUID. Changes to L01
parameter literals clear inaccurate reference labels; unchanged seed provenance
remains visible.

Execution uses one existing JobManager and ordinary v2 run requests sequentially.
One failure is recorded and later cases run, unless the visible frozen policy says
to stop after the first failure. Progress is completed/total cases; individual
kernel runs remain indeterminate. Cancel terminates the active worker, marks its
case cancelled and remaining cases not_run, preserving completed records.

New datasets require an empty chosen directory. sweep-manifest.json is atomically
updated after terminal cases; records/ contains separate complete canonical public
RunRecords. Continue validates the manifest/request identities and uses worker
load_record before skipping any saved case. Stored parameters, State, outputs and
observer config/clock/memory must match the request, as must digest and source.
Missing/tampered/mismatched records are visibly marked for rerun. An orphan complete
record is reconciled only after explicit continuation and public validation, never
from its filename alone. No partial record or automatic scientific retry is saved.

## Descriptive comparison

Select exactly two records from completed/loaded/dataset history. Cross-kind
comparison is refused. Run comparison shows metadata and selections side-by-side,
indices only in A/common/only in B, and stored A/B/B-A values. Only exact common
update_index values align. Enter shared Omega channel indices explicitly; differing
state sizes remain visible and no ring-sector equivalence is inferred. Missing
chirality/diagnostic/observer data remains not recorded. Deltas are
DISPLAY_DERIVATION_ONLY, with no ranking, winner or physical interpretation.
Geometry comparison presents definitions/options/resolved parameters, objects,
frames, incidence, symmetry and construction provenance in separate camera panels.

## Derived CSV and image exports

Choose explicit stored CSV field groups and all samples, an inclusive ordinal
range, or an ordered explicit ordinal list (repetitions retained). Each selected
sample produces one row with ordinal/update_index. Stored f64 leaves have decimal
and exact .f64_hex columns; complex components stay separate .re/.im paths. Missing
leaves are marked not recorded. No hidden recomputation or decimation occurs.

Every CSV has a .csv.provenance.json sidecar containing schema version 1, artifact
filename/SHA256, parent digest/source/type, exact sample and field selection,
column semantics, formatting policy, app version and kernel artifact identity.

PNG/SVG export selects an already-created cached record/history/geometry/comparison
figure. The .png.provenance.json or .svg.provenance.json sidecar contains artifact
hash/type, parent digest(s)/source commit(s), view/selection/visible series,
precision, camera elevation/azimuth/limits, geometry frames/object visibility and
analysis lineage where relevant. Comparison exports reference both parents.
SVG reports detectable rasterized layers and makes no exact-symbolic-geometry claim.

Artifacts and sidecars are staged together. Success is reported only after both
are published. Publication refuses existing destinations, including concurrent
ones; failure removes staging and any newly published pair member. Filesystems
must support same-directory hard-link publication. Existing scientific records are
never overwritten. Dataset records/ is not a derived-export destination.

## Lock v2 and certified source reconstruction

Preferred acquisition verifies the exact original K3 direct archive SHA and locked
K3 evidence. Unavailable CLI/authentication/artifact retrieval permits exact-source
reconstruction. Received metadata identity failures, partial failed downloads and
downloaded/cached artifacts failing verification remain fatal; no rebuild around
corrupt evidence. Registry kernel resolution remains forbidden.

Wheel equivalence v1 freezes 25 stable paths, their SHA256 and byte sizes. These
include all 19 Python files, all 14 record-identity modules, the mandatory provenance
manifest and distribution/license metadata. Exactly one member is optional:
trioctagon_physics-0.1.0.dist-info/build_input.sha256. If present it must be exactly
64 ASCII bytes equal to the mandatory manifest digest. The file witnesses the
PEP 517 prepared-metadata handoff; the underlying provenance is never optional.

RECORD is parsed as CSV. Exactly one row must cover each actual wheel member;
SHA256 URL-safe hashes and sizes must match, with the standard empty self-row.
The verification-only core projection removes only the optional witness row,
retains the self-row, sorts triples by path, and hashes compact UTF-8 JSON. Core
SHA256 is 6b4a00e32cb818dda250ab1496a04a55106e39e252a200fae546a81250bac01a.
No other metadata variance or wheel post-processing is allowed.

Acquisition always exercises forced reconstruction: external detached checkout at
7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e, exact origin and clean source, approved
Setuptools 81.0.0 / wheel 0.47.0 archive hashes, existing frozen backend/verifier,
and full equivalence validation. Offline certification installs both the selected
and reconstructed kernel and runs the isolated scientific worker with matching
source identity. The full UI suite runs once; the second GUI-free smoke needs only
the locked numeric closure. Acquisition alone may access exact wheels/GitHub/git.
All builds/installations after acquisition use --no-index and the locked wheelhouse.

## Accessibility and release boundary

All K4d actions are keyboard-reachable and have accessible names. Reduced motion
stops/prevents timer playback while manual Back/Forward/scrub remain available;
changing rate cannot start animation. Labels, line styles and markers supplement
colour, and plots retain text/table alternatives. Programmatic acceptance is not
Windows assistive-technology certification; a manual release audit is still required.

G01 live streaming/cooperative cancellation, G02 standalone identity/resume-preflight,
G03 symmetry permutation actions and G04 arbitrary fold-angle geometry remain gaps.
No scientific worker/API/kernel schema change, new dependency, research/Option B
surface, observer feedback or geometry/dynamics coupling is introduced. Public
release, PyPI upload, GitHub Release, installer/frozen executable/MSIX and public
version bump require separate human authorization.
