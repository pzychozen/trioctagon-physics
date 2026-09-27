# Trioctagon Scientific UI — local engineering version 0.1.0

UI DISPLAYS SCIENCE. PYTHON KERNEL COMPUTES SCIENCE.

This separately installed Windows x86-64 / CPython 3.11 application consumes the
certified kernel through `kernel_physics.api`. It does not bundle or modify the
kernel, Qt, Matplotlib, papers, research or scientific fixtures. The application
source/version and kernel source/version are distinct identities.

Registry-name availability is not certified. No public release, upload, installer
or frozen executable is authorized. Do not install either project by an assumed
public registry name.

## Exact installation inputs

- Kernel: the **direct wheel** selected in `kernel-artifact.lock.json`, from K3c
  Actions run 36291131581, source `7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e`.
- Runtime: the complete 15-wheel closure in `requirements-win-py311.lock`, with
  every archive SHA-256 enforced. NumPy 2.4.4, SymPy 1.14.0 and mpmath 1.3.0 remain fixed.
- Build: Setuptools 81.0.0 and wheel 0.47.0; archive hashes are in `pyproject.toml`.
- Application: an ordinarily built companion wheel. Its contents include original
  application modules/help, license metadata, and installed lock data only.

The kernel source is a TEMPORARY_CERTIFIED_DEVELOPMENT_ARTIFACT. Actions retention
is not a permanent release channel. Acquisition fails closed if unavailable;
there is no registry or rebuilt-wheel fallback. A later authorized release/K4d
must provide a durable distribution source.

## Acquisition and offline certification

Run tooling using a clean Windows Python 3.11 interpreter. Keep the workspace
outside the checkout. The included verification command acquires exact artifacts
only when `--acquire` is given; all subsequent installs, builds and tests are offline.
GitHub CLI authentication with read access is needed for artifact acquisition.

```powershell
python -B apps/scientific_ui/tests/test_install_launch.py --acquire --source C:\path\trioctagon-physics --workspace C:\temp\trioctagon-ui-acquisition
python -B apps/scientific_ui/tests/test_install_launch.py --certify --source C:\path\trioctagon-physics --workspace C:\temp\trioctagon-ui-acquisition
```

This creates disposable build/runtime environments, copies application sources and
tests outside the checkout, builds the wheel, installs it with the selected kernel,
runs all application tests, and writes JSON/log evidence to the external workspace.
It neither builds the kernel nor writes build output into this repository.

For a manual offline installation into a fresh environment, with the acquired
wheelhouse and built application wheel already available:

```powershell
python -m venv C:\temp\trioctagon-ui
$uiPython = 'C:\temp\trioctagon-ui\Scripts\python.exe'
& $uiPython -I -B -m pip --isolated install --no-index --require-hashes --find-links C:\temp\trioctagon-ui-acquisition\wheelhouse -r apps/scientific_ui/requirements-win-py311.lock
# Verify the kernel lock with the certification tool BEFORE installing this path.
& $uiPython -I -B -m pip --isolated install --no-index --no-deps C:\temp\trioctagon-ui-acquisition\kernel-evidence\direct-wheel\trioctagon_physics-0.1.0-py3-none-any.whl
# Use the exact app_wheel path from latest-certification.json:
$appWheel = (Get-Content C:\temp\trioctagon-ui-acquisition\latest-certification.json -Raw | ConvertFrom-Json).app_wheel
& $uiPython -I -B -m pip --isolated install --no-index --no-deps $appWheel
& $uiPython -I -B -m trioctagon_ui --smoke-test
& $uiPython -I -B -m trioctagon_ui
```

The installed `trioctagon-scientific-ui` launcher is also available in that
environment's Scripts directory. Run from any directory; no PYTHONPATH, editable
install or source checkout is required. Installed lock data is located through
distribution metadata, independently of the launch working directory.

Stage A found a host-specific Conda DLL collision when a venv inherited the broad
`torment` environment: its ICU library shadowed the Windows ICU expected by Qt.
A fresh minimal Python 3.11 environment passed without replacing any wheel or DLL.
Keep GUI dependencies out of `torment`; use a clean interpreter/environment for
the application. Do not delete/rename system or Conda DLLs to force an import.
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
unchanged. All Matplotlib Save Figure actions and their toolbar keyboard entry
are disabled; provenance-aware export belongs to K4d.

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

## K4d deferred scope

Parameter sweeps, substantive multi-record comparison, CSV and provenance-aware
PNG/SVG exports, durable public artifact distribution, release packaging/installers,
and further accessibility certification/polish remain K4d or later. G01 live
streaming/cooperative cancellation, G02 identity/resume-preflight queries, G03
symmetry permutation actions and G04 arbitrary fold-angle geometry remain API gaps.
No new dependencies, kernel changes, research/Option B controls or physical
geometry/dynamics coupling are introduced by K4c.
