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
The topology is visibly fixed to triad. Slider ranges are DISPLAY_RANGE_ONLY;
typed off-tick/out-of-range values are retained without clamping or normalization.

B — Observers & Diagnostics: choose None, either named observer, or Both. All
readouts/diagnostics initially remain unselected. Accounting/alignment selections
require an explicit observer; the UI never silently attaches one. Results are
passive, preserve signs/residuals/flags, and do not feed back into Omega.

C — Geometry: explicitly choose C01 with sections [] or D03 regular(s). Enter
positive integer/rational s for D03. Exact record data appears in an inspector;
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
spellings, resolved binary64 hex values, preset origins and change notes.
It does not run science when opened. Edited historical inputs lose their historical
label. O02 remains unresolved; .05/.2/.244 are not claimed scientifically optimal.

Resume submits only the selected RunRecord and explicit additional updates to
`api.resume`. Parameters/observers cannot be overridden. An incompatible source/
module identity produces the original kernel error. Resume with zero updates is
a real continuation operation, not a read-only compatibility probe.

Prepare new checkpoint draft copies the selected sample's stored bits/index.
Choose parameters/outputs, explicitly acknowledge named observer reinitialization,
then Run checkpoint draft. This calls a new `api.run`, recording parent digest/
sample lineage in checkpoint provenance. It does not claim to resume old history.

## Worker and request contract

Request v1: `ui_request_version`, `request_id`, `operation`, `payload`.
Operations: run, resume, new_checkpoint_run, geometry, load_record. Run/checkpoint
payloads contain original draft strings and matching resolved hex values. Resume
contains canonical parent JSON and update text; geometry contains definition_id
and optional exact s text; load contains record_json. Unsupported payload keys fail.

Response v1: `ui_response_version`, matching request_id/operation, status, and
either result (canonical_json, record_type, deterministic_sha256, source_commit,
produced_current) or error (exception_class, original message, action, traceback).
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

## Deferred controls

K4c: ring editing, custom observers/clocks/memory, general exact geometry options/
sections, history displays and full stored-sample playback. K4d: finite sweeps,
comparison and CSV/PNG/SVG export workflows. Research/quarantined controls, new
scientific formulas and geometry/dynamics coupling remain excluded.
