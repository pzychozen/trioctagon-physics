# kernel_physics v0.1 baseline + opt-in response, face view, scaffold and Z observer

## Additive Paper G observations — package 0.2.0

`kernel_physics.api` now additionally exposes `axial_snapshot(omega)` and
`axial_source_budget(before, parameters, *, after=None)`, immutable AxialSnapshot
and AxialSourceBudget, AXIAL_OBSERVATION_API_VERSION="1.0.0" and
AXIAL_OBSERVER_REVISION="AXIAL_M1_V1". See the
[frozen observation contract](K0_AXIAL_OBSERVATION_EXTENSION_v0.1.md).
All previous public signatures and legacy API/schema 1.0.0 remain unchanged.

The passive owner reuses canonical chirality and reports W=T C, Gamma, area
decomposition, signed accounting residuals and all seven finite-step source
terms. It reconstructs predictions without stepping, modifying State or feeding
back into dynamics. Supplied comparison requires index n+1 but does not assert
same-parent provenance. Binary64 observations are not exact-real/interval
certificates or physical magnetic fields; zero-component Arg0 qualifications
remain. Cycle diagnostics, ring, overlays, X01 and UI integration are absent.

The new owner is a mandatory twentieth distributed Python module, included in
the build-input identity and installed verifier, while the fourteen-path legacy
RunRecord identity stays frozen. Old schema-1.0.0 records remain loadable;
cross-commit/module resume still refuses. No UI lock changes or public registry
release accompany this kernel extension. The historical K3 baseline below is
retained as provenance; its package version and artifact identities do not
certify the new 0.2.0 build.

## Software distribution — K3 engineering

The distribution/project metadata name is **trioctagon-physics**; the source
and Python import package remain **kernel_physics**, with supported facade
**kernel_physics.api**. Do not rename or move the import package to match the
repository name. Conceptual future registry usage is:

```text
pip install trioctagon-physics
```

No public registry release is certified or authorized yet, and name
availability must be checked immediately before any future upload. K3b builds
are engineering artifacts; K3c owns isolated installed-package certification
and CI. For an engineering wheel supplied locally, use its explicit path with
pip in a separate environment containing the approved dependencies.

```python
from kernel_physics.api import Parameters, State, step
parameters = Parameters(eps=0.05, g=0.2, phase_strength=0.001, k=(1, 1, 1))
state = State(omega=(0.2+0.3j, -0.4+0.1j, 0.1-0.2j), update_index=0)
next_state = step(state, parameters, topology="triad")
```

Package **0.1.0** is the K3 engineering software distribution version. Public
API **1.0.0**, RunRecord/GeometryRecord schemas **1.0.0**, ledger **0.1** and
paper editions are separate identities. No version bump is implied by K3b.
The initial certification lane is **Windows / CPython >=3.11,<3.12 /
NumPy 2.4.4 / SymPy 1.14.0 / mpmath 1.3.0**. Python 3.12, Linux, macOS and
broad dependency compatibility are not supported claims.

Provenance has two strict modes:

- An exact source Git checkout uses live origin/commit and raw source/paper
  bytes. Dirty, incomplete or broken source evidence fails closed; it cannot
  be bypassed by leaving a manifest in the checkout.
- An installed distribution or provenance-bearing sdist uses the immutable
  `_distribution_provenance.json`. Every capture hashes the current 14
  authoritative .py files and requires equality with the attested source
  bytes. Missing/malformed manifests or changed files fail closed. A containing
  unrelated Git repository does not own the package's provenance. Paper paths
  are source locators; paper text is not included or opened in this mode.

The build-input digest is SHA-256 of canonical UTF-8 manifest JSON, with sorted
keys, compact separators and no nonfinite values, excluding the digest field.
It establishes internal consistency, not cryptographic authorship. The
attested source commit remains distinct from package version and the final
archive SHA-256. Installed `tracked_dirty=false` attests clean build source;
current module integrity is checked independently. Resume still requires the
same commit and module hashes. Older records remain decodable, but a changed
implementation requires an explicit checkpoint run rather than weaker resume.

After K3c certification, supported installed operation must require no Git,
paper/research tree, network, LLM, embedding model or GPU. The package retains
all 19 top-level software modules. `boundary_response`, `srg`, and
`operating_region` remain unsupported v1 internals; `face_state` remains legacy
opt-in. None is loaded by the facade or selectable by Runner. Physical shipping
does not confer supported public API status.

Apache-2.0 applies only to the approved software distribution scope. See the
root LICENSE (standard unmodified text) and LICENSE_SCOPE.md, also included in
distribution license metadata. Papers, research, figures, manuscripts, datasets,
Twisted Hex and parity fixtures/evidence retain their separate existing status.
The artifact allowlist is both a software and licensing boundary.

The in-tree PEP 517 wrapper delegates to Setuptools 81.0.0 and wheel 0.47.0.
Build only from clean tracked source or a validated provenance-bearing sdist,
with already available approved tooling. Supply an output directory outside
the checkout. Metadata preparation, wheel and sdist hooks stage externally;
no build directory, egg-info or generated manifest belongs in source. Runtime
dependencies do not include build tools. Editable installs are outside scope.

The repository verifier can be run as:

```text
python -B tools/verify_distribution.py --source CLEAN_SOURCE --wheel WHEEL --sdist SDIST --report EXTERNAL_REPORT.json
```

It validates exact archive contents, licensing/metadata, manifest and all 19
source/archive hashes. Its optional installed smoke uses an explicitly supplied
Python via `--installed-python`; K3c must supply an isolated environment and
certify that result. No dependency installation or network access is performed
by the verifier.

## Supported public API v1 — K1, 26 September 2026

Use `kernel_physics.api` under the frozen
[K0 authority and contract](K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md)
and [definition ledger](K0_KERNEL_DEFINITION_LEDGER_v0.1.md).
The facade delegates the accepted mathematics. Parameters, state and observer
configuration are explicit, detached immutable values; `phase_strength` is
Paper A's lambda. For example, from this checkout with `conda activate torment`:

```python
from kernel_physics.api import Parameters, State, step

parameters = Parameters(eps=0.05, g=0.2, phase_strength=0.001, k=(1, 1, 1))
state = State(omega=(0.2+0.3j, -0.4+0.1j, 0.1-0.2j), update_index=0)
next_state = step(state, parameters, topology="triad")
```

These example values are explicit choices, not public defaults. Named presets
are `gate_torus_seed_v1`, `paper_e_staged_v1` and `paper_e_ema_v1`; their original
selection rationale remains O02 `OPEN_NONBLOCKING`.

`run`/`resume` return `RunRecord` (`KERNEL_RUN_RECORD` 1.0.0), with independent
observer snapshots and passive diagnostics. `get_geometry("C01", options={
"section_heights": []})` or `get_geometry("D03", options={"construction":
"regular", "s": 1})` returns a separate exact `GeometryRecord`
(`GEOMETRY_RECORD` 1.0.0), always with `coupling="none"`. Both provide
`to_json`/`from_json` and an immutable encoded `data` view. Loading never runs
equations. Record production uses strict live source provenance or verified packaged
provenance as described above; loading remains portable. Resume requires the
same commit and module hashes. Binary64 and exact symbolic trees retain their respective codecs;
cross-platform numerical replay is qualified by K0.

**O01 is resolved as Option B:** `boundary_response`, `srg`, and
`operating_region` are preserved but unsupported by the initial v1 facade.
The API and Runner neither expose nor load them. `FaceState` remains outside
the facade; `_response_numeric` remains shared numerical support. Existing
internal opt-in callers and predecessor tests are preserved. The earlier
K0-time OPEN entry remains historical. O03 golden-fixture publication and
the independent P1–P11 program remain deferred to K2.

## Current convergence status - 24 September 2026

**K1/R1, K2 and K3 are accepted and published within their contracted scopes.**
The implementation baseline is `d2b1cbeca807ae33117f02f697e5eff0b4b1ca96`.
See [K1-K3 parity closeout](K1_K2_K3_PARITY_CLOSEOUT.md) for the authoritative
scope map, evidence, source location and remaining obligations.

That checkpoint passed 207 local / 177 published-package test methods. The
30 local-only predecessor methods remain a separate publication obligation.
Six-gap registration and the broader reconstruction remain open.
Preparation-time K3 candidate/pending language later in this README and in
frozen receipts is superseded by the checkpoint's scoped acceptance, not erased.

**Paper C exact local geometry + Paper A exact abstract dynamics.**

**NO PHYSICAL COUPLING BETWEEN THEM IS CLAIMED YET.**

This is a separate, minimal Python package. Geometry and dynamics do not import
each other. There is no framework, server, plugin system, memory architecture or
historical-kernel dependency.

## Authoritative location

~~~text
CHECKOUT: C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
SOURCE:   C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\kernel_physics
PYTHON:   C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe
~~~

The sibling directory supplies only the existing interpreter for these commands;
it is not the source edit target. Run from the checkout so imports resolve to the
source above. The [K1 validation record](K1_REFERENCE_SCAFFOLD_VALIDATION.md)
records actual executable, versions, resolved imports and test IDs. Its task ID
`MK-K1_REFERENCE_SCAFFOLD_v0.1` distinguishes this packet from the original
Paper-A/C implementation also called K1.

## Frozen definitions

- Paper C: PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md,
  §§2–7,9 and Appendix B.
- Paper A: PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md,
  §§1–3 and §6.

The source paths and original SHA-256 hashes are in baseline_manifest.json.
Neither paper was modified. The original baseline opened no historical PDF or
kernel source. K2 reads only the seven pinned Paper-E/current-package inputs
listed in its separate validation record.

## Modules

- **geometry.py**: SymPy exact coordinates, w=1, s=sqrt(2)-1, general-angle
  panel maps and the canonical beta=pi/3 weld. folded_module() returns an
  immutable mesh with 18 vertices, 21 edges, three octagonal faces, three seams
  and two nine-edge boundary loops, preserving Paper C's vertex/face ordering.
  Normals are computed from the oriented faces. central_section(height) returns
  three unit segments for abs(height)<=s/2: a curve, not a filled cap.
  rotate_c3, reflect_vertical and reflect_horizontal are the exact D3h
  generators about the centroid axis and the planes x=0, z=0.
- **reference_scaffold.py**: separately selected pure exact geometry from
  Paper D v0.1.1 §§4–14, including closed half-planes, complete reference
  octagons and the published vertical family. No default geometry changes.
- **dynamics.py**: immutable DynamicsConfig(eps, g, phase_strength, k),
  step3 and step_ring. phase_strength is Paper A's lambda;
  k is a real amplitude-coefficient triple. All parameters are explicit.
- **covering.py**: exact immutable cycle Laplacians, residue pullback P for all
  positive M,d, and Q=P/sqrt(M/d) for divisor cases. Sizes 1 and 2 retain
  incidence multiplicity. No isometry or intertwining is claimed for non-divisors.
- **boundary_response.py**: explicitly chosen `lens_area_norm_v1` area-norm
  response, stable area/gain evaluation and raw helicity-major preparation.
- **srg.py**: fixed November operators, named positive-pivot helicity modes,
  extraction and an explicit transfer-count initialization handoff.
- **operating_region.py**: named radius-three profile validation and adapters
  around the existing `DynamicsConfig`/`step3`, without a second recurrence.
- **readouts.py**: raw `z_chiral` only. `_response_numeric.py` supplies private
  strict-input and precision checks for these opt-in modules.
- **z_manifold.py**: explicitly selected Paper-E staged-envelope and committed-EMA
  observers, immutable clocks and explicit memory updates. No recurrence or
  geometry import; raw chirality delegates to `readouts.z_chiral`.
- **face_state.py**: opt-in tangent-vector view at the existing face centres,
  with raw Omega canonical, named frames/transport and delegated signed areas.
  This adapter imports geometry/dynamics; neither base module imports the view.

The implemented dynamics are

~~~text
L3 = [[-2,1,1], [1,-2,1], [1,1,-2]]
Omega_tilde = Omega + eps*Omega*(k-abs(Omega)^2) + g*L3@Omega
theta_n = Arg0(Omega_tilde_n), with Arg0(0)=0
F(Omega)_n = abs(Omega_tilde_n) * exp(i * (
    theta_n + lambda * sum_{m~n} sin(3*(theta_m-theta_n))))
~~~

All phase increments use the same pre-synchronization vector. At three nodes the
two neighbors are the other two nodes; on the ring they are the periodic
neighbors, including wrap-around. step_ring requires M=3q and repeats k
by residue class. It evolves unrestricted ring states, not just lifted states.
When lambda is zero, synchronization returns a copy directly, without invoking
phase extraction or reconstructing polar coordinates.

Geometry and linear covering identities use exact symbolic arithmetic.
Dynamics use NumPy complex128; nonlinear lift identities are checked to stated
roundoff tolerances, not asserted as bitwise equal. Nonfinite input is rejected;
numerical overflow is not a physical prediction. There is no timestep parameter,
automatic state normalization, random noise, or hidden state.

Paper A's nonzero-lambda extension is generally discontinuous when pre-sync
components vanish. Global-phase equivariance tests cover nonzero pre-sync
components, and the lambda-zero case including zeros. No unrestricted
equivariance claim is made for the zero-component extension.

## Run the focused tests

Use the existing environment, which remains at its original location. These
commands work in Windows CMD and install or upgrade nothing:

~~~bat
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
"C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe" -B -m unittest discover -s kernel_physics/tests -v
~~~

Verified environment: Python 3.12.14, NumPy 2.3.5, SymPy 1.14.0, mpmath 1.3.0.
The environment reuses bundled NumPy and the existing local SymPy dependency.
Tests use only fixed
inputs: printed coordinates, hand-calculated steps, exact matrix identities and
selected nonlinear lifts at M=3,6,12,24. There is no atlas, scan or parameter tuning.
The unchanged VALIDATION.md, validation.json and test_run.txt record the original
41-test baseline. The predecessor boundary/SRG closeout records 75 passing tests
in [its implementation report](../../research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md).
The earlier local suite passed **95 tests (75 predecessor + 20 face-view)**.
The face-view tests and that execution receipt are recorded in the same reviewed
[attachment note](../../research/GPT_proof/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md).
On 24 September 2026, K1 rediscovered and passed those same **95 local baseline
tests**, before adding scaffold tests. Four existing untracked test files contain
30 of them; they match the preceding publication baseline and remain unchanged.
Only 65 predecessor tests are tracked at the base commit. Thus 95 is a measured
local count, not a claim about fresh-clone coverage. The submitted K1 local suite
passed **122/122 tests (95 preserved + 27 original scaffold tests)**. Those tests
did not detect the symbolic-domain defect subsequently reported by GPT. The R1
correction and new substitution-first regression results are recorded separately
in the R1 section of the validation records; the earlier runs remain preserved.
The corrected R1 local suite passes **134/134 tests: 95 predecessor + 27 original
K1 + 12 new R1 methods**, including all four pre-existing untracked test files. Exact
IDs, stdout and preservation results are in the [K1 record](K1_REFERENCE_SCAFFOLD_VALIDATION.md)
and its [machine-readable companion](K1_REFERENCE_SCAFFOLD_VALIDATION.json).

## Explicit Paper-D reference scaffold

Import this module explicitly; `geometry.folded_module()` and the existing
`FaceState` still use the unchanged Paper-C welded realization.

```python
import sympy as sp
from kernel_physics.reference_scaffold import (
    ReferenceScaffold, paper_c_member, shrink_paper_c_at_fixed_centres,
)

s, g_gap = sp.symbols("s g_gap", positive=True)
scaffold = ReferenceScaffold(s, g_gap)  # p=(s+2*g_gap)/(2*sqrt(3))
regular = ReferenceScaffold.regular(sp.Rational(1, 3))
assert regular.filled_hexagon.contains((0, 0)) is True
original = paper_c_member(sp.sqrt(2)-1)  # width one; g_gap/s=1/sqrt(2)
shrunk = shrink_paper_c_at_fixed_centres(original.s)
assert shrunk.side_lengths == (sp.Rational(1, 3),)*6
```

`ReferenceScaffold.from_radius(s,p)` checks the equivalent strict positive-gap
domain. Lengths accept exact Python integers/Fractions and exact finite real
SymPy expressions, including positive symbolic `s,g_gap`. Floats, strings,
booleans, nonfinite/complex lengths and nonpositive or undecidable domains are
rejected; no floats are silently rationalized. `.is_regular` returns `None` when
the equality is undecidable; `.regularity_residual` retains `g_gap-s`.
Half-plane membership similarly returns `True`, `False` or `None`.

R1 keeps symbolic denominators untransformed by `radsimp(symbolic=False)` in the
new coordinate helper, while retaining exact numerical radical simplification.
For example, the admitted length `1/(1+sqrt(x))`, `x>0`, remains valid at `x=1`:
returned coordinates are specialized first and agree with construction at side
`1/2`. This is a correction to representation, not a restriction excluding that
input or a change to Paper-D geometry. The targeted regressions are not a universal
certificate for arbitrary SymPy expressions. Genuinely undecidable membership
still returns `None`, and invalid/nonfinite inputs remain rejected.

`Octagon.vertices`, `.outline` (eight closed-cycle segments) and `.filled`
(closed convex hull) distinguish points, boundary and filled mathematical set.
`ReferenceScaffold.vertices` is exactly `(A0,B0,A1,B1,A2,B2)`, with E/G roles
retained. `.filled_hexagon` uses the six closed inequalities of equation (16a):
connectors remain boundary; support apices and outer corner legs are excluded.
`.support_triangle`, `.corner_cells`, `.planar_frames` and `.vertical_frames`
are immutable convex-hull prescriptions, not welded meshes or material claims.

Midpoint/vertical-centre radius `p`, planar-centre radius `L=p+a`, and `g_gap`
remain distinct. The CCW planar octagon traverses its inward side B-to-A; the
selected edge runs A-to-B. `paper_c_rigid_map` maps the starting vertical frames
0,1,2 to existing Paper-C panels P3,P1,P2 at width one, with a three-vertex cyclic
offset in the local outline. Six top measurement points are not the nine-edge
nonplanar rim. Unmarked regular-hexagon D6 reduces to D3 for E/G classes and C3
when traversal is also preserved; fixed individual labels are a stricter marking.
The full three-frame arrangement does not acquire the hexagon's 60-degree symmetry.

`translate_paper_c_to_regular(s)` preserves size and top height while moving each
vertical centre outward. `shrink_paper_c_at_fixed_centres(s)` starts only from the
Paper-C family and scales local coordinates by `(1+sqrt(2))/3` at fixed vertical
centres, lowering the top plane. This factor is not an arbitrary-p or fixed-planar-
centre rule. The new module imports only SymPy and standard-library modules.
It supplies only this bounded Paper-D geometry. K1/R1 received scoped GPT acceptance
and was published in commit `2b336f247aa2c24cd7596a1fc733a7b948fdb840` on
24 September 2026. Pending-review text in its preserved validation artifacts is
a preparation-time snapshot superseded by that commit's scoped acceptance record.
The separately selected K2 observer below does not change scaffold geometry.

## Explicit research initialization option

This adopts a mathematical toy response under A1–A4, not a recovered DMQPF law.
The response is never selected by the existing dynamics automatically:

~~~python
from dataclasses import asdict
import hashlib
from pathlib import Path
import platform
import sys

import numpy as np
import sympy
import kernel_physics
from kernel_physics.boundary_response import RESPONSE_ID, theta_from_lens
from kernel_physics.face_state import FaceState, area_triple
from kernel_physics.operating_region import (
    PROFILE_ID, bounded_config, initialize_bounded_area, step_bounded_triad,
)

def face_snapshot(view, downstream_step):
    return {"downstream_step": downstream_step,
            "omega": [[float(z.real), float(z.imag)] for z in view.omega],
            "vectors": view.vectors.tolist(),
            "area_triple": area_triple(view.omega).tolist()}

lens_input = {"radius": 1.0, "separation": 1.2}
theta = theta_from_lens(**lens_input)
config = bounded_config(k=(1.0, 1.2208964704604097, 6.35310346037241),
                        phase_strength=0.001)
handoff = initialize_bounded_area(
    theta, (0.6+0.2j, -0.3+0.4j), config=config, profile=PROFILE_ID,
    transfer_count=1, branch="negative_imag", response=RESPONSE_ID,
)
view = FaceState(handoff.omega)  # retains a copy of raw Omega; vectors are derived
face_trajectory = [face_snapshot(view, 0)]
step_count = 4
for downstream_step in range(step_count):
    view = view.step(config, profile=PROFILE_ID)  # selected wrapper, one step3 call
    face_trajectory.append(face_snapshot(view, downstream_step+1))
omega = view.omega
chirality = area_triple(omega)

module_root = Path(kernel_physics.__file__).resolve().parent
run_record = {
    "lens_input": lens_input,
    "initialization": handoff.metadata(),
    "downstream": {"profile_id": PROFILE_ID, "config": asdict(config),
                   "step_count": step_count},
    "face_view": view.metadata(),
    "face_trajectory": face_trajectory,
    "code_identity": {
        "package_version": kernel_physics.__version__,
        "module_sha256": {name: hashlib.sha256((module_root/name).read_bytes()).hexdigest()
                          for name in ("__init__.py", "_response_numeric.py",
                                       "boundary_response.py", "srg.py", "operating_region.py",
                                       "dynamics.py", "readouts.py", "geometry.py", "face_state.py")},
    },
    "environment": {"python": platform.python_version(), "numpy": np.__version__,
                    "sympy": sympy.__version__, "executable": sys.executable},
    "expected_result": {
        "initial_omega": [[float(z.real), float(z.imag)] for z in handoff.omega],
        "final_omega": [[float(z.real), float(z.imag)] for z in omega],
        "final_z_chiral": chirality.tolist(),
    },
}

# Same initialization, now with equal k; this is the configuration of Claude's
# displayed attachment fixture. Keep its downstream configuration separate.
equal_config = bounded_config(k=(1., 1., 1.), phase_strength=0.001)
equal_view = FaceState(handoff.omega)
equal_trajectory = [face_snapshot(equal_view, 0)]
for downstream_step in range(step_count):
    equal_view = equal_view.step(equal_config, profile=PROFILE_ID)
    equal_trajectory.append(face_snapshot(equal_view, downstream_step+1))
equal_record = {
    **run_record,
    "downstream": {"profile_id": PROFILE_ID, "config": asdict(equal_config),
                   "step_count": step_count},
    "face_trajectory": equal_trajectory,
    "expected_result": {"initial_omega": run_record["expected_result"]["initial_omega"],
                        "final_omega": equal_trajectory[-1]["omega"],
                        "final_z_chiral": equal_trajectory[-1]["area_triple"]},
}
face_runs = [run_record, equal_record]
~~~

`run_record` is JSON-ready. `HandoffResult.metadata()` describes initialization
only; the enclosing record supplies the actual downstream `eps`, `g`, `k` and
`phase_strength`, profile ID and separate downstream step count. Reconstruct the
initial triad from the recorded theta, xi, response, transfer count and branch
under the recorded source/gauge conventions. `initial_omega` is an expected
replay result, not an additional preparation input. The package version is the
baseline label; the module hashes identify the actual saved implementation,
without implying a Git commit. Python, NumPy and SymPy are the evaluation versions for
this pipeline. Replay comparisons use `rtol=2e-14, atol=2e-15`, not a promise of
bitwise equality across environments.

`transfer_count` counts SRG applications before initialization, not downstream
updates. Both `negative_imag` and `positive_imag` use
`spectral_projector_maxdiag_positive_v1`; no eigensolver column order is used.
`project_bra` is a generic projection; only named `extract_helicity` promises H1.
The literal November constants and gauge appear in `handoff.metadata()`.
The six arrays returned by `fixed_november_srg()` are read-only against ordinary
in-place edits, as are `chi` and the handoff's `omega`. Use an explicit `.copy()`
for writable experiments. These flags are not a security boundary; no cache is
introduced.

Raw magnitude and phase are retained. Every input is validated before the exact
zero shortcut, using componentwise zero checks; zero aperture/incident input
returns canonical raw zero. There is no normalization, clipping, RNG or seed.
Use `bounded_config` for strict real-scalar entry before constructing the existing
general `DynamicsConfig`. Already-constructed configs are checked by their actual
stored values; coercions performed previously by general APIs cannot be undone.

The bounded profile checks eps=1/20, g=1/5, actual real k in [0,8], and the actual
initial component moduli <=3. Forcing/noise are absent from the reused recurrence.
The optional `validate_uniform_incident_budget` implements ||xi||<=3sqrt(3), a
sharp uniform sufficient condition, not a necessary condition on an individual
preparation. Larger xi with sufficiently small aperture/overlap may be accepted.
The guarantee is exact-arithmetic boundedness, not attraction or machine safety.

Numerical domain: finite binary64/complex128 inputs of the declared shapes;
scalars reject strings, booleans, complex values and arrays. Vectors reject
strings/booleans and nonfinite components. Nonzero subnormal outputs or checked
intermediate products raise `ResponsePrecisionError` (a `FloatingPointError`).
Exact zeros remain valid. Area/gain evaluation, preparation, handoff, bounded
stepping and readouts have different numerical evaluation limits. For example,
theta=1e-120 has a usable gain/preparation and n=0 handoff for xi=(1,0), although
its area raises a precision failure. Successful preparation or handoff does not
guarantee a later step or readout will succeed.

Named square-underflow probes on the pinned interpreter use state `(a,0,0)`,
k=(1,1,1), phase_strength=0: a=1e-100, 1e-140 and 1e-150 succeed, while a=1e-154,
1e-160 and 1e-200 raise at `np.abs(state)**2` inside the unchanged `step3`.
The adapter retains `under="raise"`; plain `step3` returns finite values for
these six fixtures under the interpreter's default underflow policy. The square
scale is `sqrt(sys.float_info.min) = 1.4916681462400413e-154`, approximately the
component magnitude whose square reaches the smallest normal binary64 value.
It is **not a universal necessary or sufficient lower bound** on components or
intermediate operations. Exact zeros, inexact underflow, cancellation, other
products and operation order matter; these probes impose no new mathematical
input restriction. Extremely small readout products or very large phase
increments can also fail explicitly. No underflow detection is removed, and the
adapter never clips the existing step.

No tolerance converts a small overlap to zero. Compensated sums still cannot
certify relative accuracy near cancellation; a computed zero need not be an
exact orthogonality proof. Large transfer counts can exceed the normal cycle-gain
range, and intermediate precision failures can reject a result that a differently
scaled or higher-precision algorithm could evaluate. No all-finite-input machine
certificate is claimed. The small-angle truncation and gain factorization,
tested numerical domain and precise limits are documented in the report.

## Opt-in folded-face state view

`FRAME_ID="face_center_tangent_ez_v1"` and
`TRANSPORT_ID="c3_matched_zero_phase_v1"` name the adopted conventions. Face order
is explicitly **0=A=P1, 1=B=P2, 2=C=P3**. `face_frames()` obtains centres and
outward normals from the existing exact `geometry.folded_module()` and returns
fresh read-only arrays. With positive ez=(0,0,1), t_i=ez cross n_i is fixed. An
isolated octagon's 45-degree rotation is not a global welded-shell symmetry.

`decode_to_faces(omega)` returns fresh real shape-(3,3) vectors
Re(Omega_i)t_i+Im(Omega_i)ez. These are free vectors attached at the centres,
with raw magnitude preserved, even when their tips lie outside the polygons.
`encode_from_faces(v)` accepts only real finite shape-(3,3) inputs and rejects
substantive normal components. Its relative tangency test is
`abs(sum(n_k*v_k)) <= 8*sys.float_info.epsilon*sum(abs(n_k*v_k))`, for k=x,y,
evaluated after scaling participating coordinates to avoid overflow/underflow.
There is no absolute tolerance or slack from the vertical component. A pure
normal vector is rejected however small; only residuals within the stated
frame-roundoff allowance can be discarded. This is not a small-state zero test.

Exact D and E are inverse on the tangent-state space; D E on unrestricted ambient
vectors is only a projector. Production encoding rejects normal data instead of
offering that ambient projection. Floating round trips/norms are tested with
scaled comparisons (`rtol=3e-15`, no absolute tolerance for nonzero tiny states).
For example 1e-250-scaled states survive conversion; nonzero subnormal checked
products/results raise `ResponsePrecisionError`. The readout and bounded step
keep their own stricter stage limits. Exact zero is valid. Signed zeros of the
canonical Omega are retained; decoded whole-vector zeros are canonical zeros.

`transport(i,j)` accepts integer indices 0–2 (excluding booleans), source j to
destination i, and returns read-only T_ij=t_i t_j^T+ez ez^T. It has rank two as
an ambient matrix. T_ij=Pi_i R_ij; its tangent restriction agrees with the
matched C3 rotation's **linear part**. T_ij T_jk=T_ik also holds as an exact
ambient matrix identity. Attached points rotate about the centroid axis
(0,sqrt(3)/6,0) using `geometry.rotate_c3`; free vectors use the linear part.
No adjustable phases, seam transport law or mesh motion are supplied.

`area_triple(omega)` delegates bit for bit to `z_chiral`.
`state_area(i,j,omega)` selects the corresponding signed component, with zero
diagonal and antisymmetry; it evaluates the full readout even for a diagonal
request, retaining its validation/precision failures. Geometrically this is
n_i dot (v_i cross (T_ij v_j)), the existing symplectic form transported into
plane i. This is signed **state-vector area**, not physical surface area.
The triple (A_BC,A_CA,A_AB) is channel-indexed, not an ambient axial vector.
For a shell spatial symmetry G with face permutation P:
`A'=det(G) P A P^T`, `Z'=det(G)det(P) P Z`.
For a pure channel permutation, `Z'=det(P)PZ`; keep that sign separate from
spatial parity. Horizontal mirror: conjugate Omega and negate Z. Vertical
mirror: -P conjugate Omega (A/C swap) and PZ. Common phase leaves Z unchanged.

`FaceState(omega)` retains raw Omega and derived vectors read-only against
ordinary mutation. `.step(config)` invokes existing plain `step3` once;
`.step(config, profile=PROFILE_ID)` invokes the selected bounded wrapper, which
itself calls `step3` once. It then decodes the returned Omega without re-encoding
the previous vectors. Thus canonical trajectories are bitwise equal to the
**same recurrence on the same stored Omega**. Exact mathematical conjugacy
F_face=D F_TO E is distinct from that implementation equality and from rounded
encode/decode accuracy. Use `FaceState.from_faces(v)` only for explicit initial
conversion; it performs one rounded encoding. A later decode failure can reject
a view after recurrence evaluation, without modifying the prior view.

View metadata records face order, frame/transport IDs and geometry identity;
it does not alter `HandoffResult.metadata()`. The combined example retains the
existing initialization receipt and separate downstream profile/config/count.
It records both the original unequal-k run and an equal-k run. Initial Fourier
magnitudes agree across faces; equality persists to roundoff in the equal-k
fixture but not generally under unequal-k evolution. Fixed-label C3 covariance
requires equal k; otherwise k must be permuted too. Common-phase equivariance
still has the existing nonzero-pre-sync qualification when phase_strength is
nonzero: Arg0(0)=0 is a convention at a vector with no direction. At zero phase
strength the direct branch remains valid, including zero components.

## Scope boundary

The shell is one local module. No global host, caps, interior field, assigned
physical boundary conditions or privileged physical M=12 geometry is introduced.
The geometric coordinate z is not a historical kernel readout.

The named initialization option, raw Z_chiral and this geometric view extend the
baseline. The view adds coordinates and interpretation, with no second law.
K2 separately implements the source cubic scalar, explicit EMA memory and macro-Z
observer below, with no physical energy interpretation or feedback. No central-energy
law, six-gap mapping, RSB, portal/field recursion, meta-shell, recursive thermodynamics,
magnetic coupling, gravity, wormholes, physical color/quark interpretation or
production TORMENT behavior is implemented. Those interfaces remain outstanding.
The SRG orientation cycle is not Paper-A evolution. This adopted finite-dimensional
face view supplies no physical field, units, phase generator, surface interpolation,
seam condition or justified mode selection. The broader reconstruction is unfinished.

## Optional Paper-E historical Z observers (K2)

K2 is accepted and published at 022fa5147bbf4184bd9e41b6330bf5dfc90759d9. Its preserved preparation-time records remain unchanged; that scoped acceptance supersedes their pending-review text. Its
[validation report](K2_HISTORICAL_Z_VALIDATION.md) and
[full JSON companion](K2_HISTORICAL_Z_VALIDATION.json) retain the actual local,
package-export and source-body checks, including development failures. The fresh
starting suite passed 134/134 methods; published K1 has 104 methods. The four
local-only predecessor files still contribute 30 local methods and are not part
of a package export. K2 adds 37 self-contained methods; these counts count test
methods, not theorems. K1's four non-README artifacts remain unchanged.

Import `z_manifold` explicitly. `StagedConfig` selects Paper E equation (2):
literal lambda_vp=0.618, gamma=0.577, theta_lock=0.244, alpha=1, beta=0.5.
`EMAConfig` selects equation (39), with the same harmonic/blend defaults but no
gamma field. Signed finite coefficients are allowed. The two laws are never
chosen by an implicit variant default.

- `Clock(q=0, N=12, t=0.0, q_step=1)`, `clock_angle(clock)` and
  `advance_clock(clock, dt)` keep the integer sector and time explicit.
  Angles reduce q modulo N in integer arithmetic before binary64 evaluation.
  No helper hardcodes 12 instead of using N. The historical dt=0.1 is only a
  clock increment; it never enters the existing nonlinear/coupling recurrence.
- `state_norm(omega)` uses six-real-component hypot; `saturated_norm(omega)`
  applies kappa/(1+kappa) only to the scalar formula, never to Omega.
- `staged_scalar(omega, clock, config)` and
  `observe_staged(omega, clock, config)` apply the exponential envelope only to
  the scalar/macro. Raw C has no imposed decay envelope; it need not decay.
- `cubic_j(omega)` computes Im(O1*conj(O2)*O3);
  `normalized_cubic(omega)` gives J/(1+abs(J)). This cubic is distinct from
  quadratic channel area and is not generally common-phase invariant.
- `EMAState(m=0.0)` adopts finite |m|<=1. `advance_ema(omega, memory)` performs
  exactly one update using literal tau_meta=0.01 and retention 1.0-tau_meta.
  `ema_scalar(omega, clock, config, memory)` and
  `observe_ema(omega, clock, config, memory)` use CURRENT memory without updating
  it. Readout repetition advances nothing. Zero Omega does not erase memory.
- `macro_vector(z, clock)` and `blend_vectors(macro, chiral, *, alpha, beta)`
  construct M and T. A `ZReadout` contains z, Z_macro, Z_chiral, Z_total,
  variant and initialization. `Z_vec` aliases Z_total. Fresh detached arrays
  resist ordinary in-place edits; read-only flags are not a security boundary.
- `historical_constructor_zero(omega, clock, config)` returns a
  `ConstructorZeroRecord` with validated Omega/clock/config, zero memory and
  the marked zero readout. It intentionally evaluates no norm, cubic or C.
  A modern recomputed observation of that same Omega computes its actual C.

The following optional example records exactly three pre-step rows. The final
post-step state lies outside that history, as in the source. It does not restore
a historical runner, phase helper, noise, forcing, cycle or identity machinery.

```python
from dataclasses import asdict
import numpy as np
from kernel_physics.dynamics import DynamicsConfig, step3
from kernel_physics.z_manifold import (
    Clock, StagedConfig, EMAConfig, historical_constructor_zero,
    advance_clock, advance_ema, observe_staged, observe_ema,
)

omega = np.array([.2+.3j, -.4+.1j, .1-.2j])
dynamics = DynamicsConfig(eps=.05, g=.2, phase_strength=0, k=(1, 1.2, 1.4))
clock = Clock(q=0, N=12, t=0, q_step=1)
staged = StagedConfig(lambda_vp=.618, gamma=.577, theta_lock=.244, alpha=1, beta=.5)
ema = EMAConfig(lambda_vp=.618, theta_lock=.244, alpha=1, beta=.5)
dt, requested_rows = .1, 3
initial_k = historical_constructor_zero(omega, clock, staged)
initial_h = historical_constructor_zero(omega, clock, ema)
memory, out_k, out_h = initial_h.memory, initial_k.readout, initial_h.readout
metadata = {
    "initial_omega": [[v.real, v.imag] for v in omega],
    "dynamics": asdict(dynamics), "initial_clock": asdict(clock),
    "staged_config": asdict(staged), "ema_config": asdict(ema),
    "initial_memory": memory.m, "tau_meta": .01, "dt": dt,
    "requested_rows": requested_rows, "sampling": "historical_pre_step",
    "initialization": "historical_constructor_zero",
}
def observation(value):
    return {"z": value.z, "Z_macro": value.Z_macro.tolist(),
            "Z_chiral": value.Z_chiral.tolist(), "Z_total": value.Z_total.tolist(),
            "variant": value.variant, "initialization": value.initialization}
history = []
for _ in range(requested_rows):
    history.append({"omega": [[v.real, v.imag] for v in omega],
                    "clock": asdict(clock), "memory": memory.m,
                    "staged": observation(out_k), "ema": observation(out_h)})
    omega = step3(omega, dynamics)
    clock = advance_clock(clock, dt)
    out_k = observe_staged(omega, clock, staged)
    memory = advance_ema(omega, memory)
    out_h = observe_ema(omega, clock, ema, memory)
# history has rows 0,1,2; omega/clock/memory/out_k/out_h now describe step 3.
```

The existing earlier tilde-fenced pipeline remains byte-for-byte unchanged.
This example reuses the current recurrence. The historical np.angle signed-zero
extension is not installed: modern arg0 is unchanged. Source-body parity is
same-state parity; no complete phase-enabled historical trajectory is certified.

K2 accepts finite binary64/complex128 values of the declared shapes, excluding
strings and booleans. Clock fields q, N and q_step must be integers, with N>0.
Time and coefficients are finite reals; an explicit nonzero dt entirely lost
to rounding raises ResponsePrecisionError. Checked nonzero subnormal results
and intermediate products are conservatively rejected. Cubic multiplication is
left-associated; sums use the existing compensated helper. Exponential overflow,
underflow-to-zero and subnormal envelopes raise explicitly, even at zero amplitude.
Full readouts always compute C, including at beta=0, so a successful scalar does
not guarantee a successful decomposition.

Finite exact rho and |j| are less than one; binary64 saturation can round to the
endpoints, which are accepted. No clipping, tolerance-based zeroing, high-precision
runtime fallback or universal numerical certificate is supplied. The fixed
source-body comparisons use rtol=2e-14, atol=2e-15; bitwise equality across
platforms is not promised. The bounded memory proof does not bound total Z
independently of Omega, and persistent nonzero cubic input need not decay.

Observer outputs do not feed Omega or Paper-C/Paper-D geometry. The clock is
not mean channel phase or a physical D24 group assignment. Six-gap spatial
registration remains open; the separate K3 diagnostic candidate is described below.

## Optional Paper-E mathematical diagnostics (K3)

K1/R1 and K2 are accepted and published; K3 is a candidate pending GPT
implementation review. See [K3 validation](K3_MATHEMATICAL_DIAGNOSTICS_VALIDATION.md)
and its [full execution evidence](K3_MATHEMATICAL_DIAGNOSTICS_VALIDATION.json).
The measured entry baseline is 171 local methods and 141 published methods;
the four unchanged local-only files contain 30 methods and remain a separate
publication obligation. K3 adds 36 methods, counting tests rather than theorems.

Import `z_diagnostics` explicitly. It is passive and is not imported by the base
package or any existing module. Its actual public functions are:

| Function | Supplied inputs and result |
|---|---|
| `quadratic_form(vector)` | Finite real (3,) vector; signed Q(v), not a norm or certificate. |
| `readout_accounting(readout, *, alpha, beta)` | Stored K2 ZReadout; immutable ReadoutAccounting with full weighted norm/Q terms, vector/scalar residuals, supplied-z macro relation and variant/initialization. |
| `chiral_area_accounting(omega)` | Finite complex (3,) state; ChiralAreaAccounting, delegating raw C once, Gram terms, norm, bound and slack. |
| `historical_alignment(macro, chiral, total_vector)` | Three finite real (3,) vectors; HistoricalAlignment with three conventional dots and vector/pair resolution flags. |
| `intensity_budget(omega, config)` | Finite complex (3,) state and existing DynamicsConfig; IntensityBudget including D, diagnostic_pre_sync_prediction, full remainder and residual. |
| `potential(omega, config)` | Same inputs; scalar potential with negative gradient equal to D in six real coordinates. |
| `direct_history_coordinates(history, key="Z_total")` | Real (n,3) stored vectors; Coordinates. Z_vec fallback only if default Z_total is absent. Empty (0,3) is valid. |
| `cylinder_point(kappa, q, z, *, N=12)` | Nonnegative kappa, integer q/N with N>0, real z; read-only (3,) point. |
| `cylinder_history_coordinates(history, *, N=12)` | Equal 1D kappa/phi_index/z arrays; Coordinates; empty is valid. |
| `history_torus_coordinates(history, *, R=2., r_max=1., N=12)` | Nonempty scalar history, R>r_max>0; HistoryTorus with coordinates, r/chi and actual whole-history normalization metadata. |

All record arrays are detached and read-only against ordinary writes, not a
security boundary. Real inputs reject bool/string/complex/nonfinite values;
states reject bool/string/nonfinite values and wrong shapes. DynamicsConfig is
validated by its stored fields; coercions performed earlier cannot be undone.
These checked binary64 operations reject nonzero subnormal intermediates,
nonfinite results and lost nonzero products/divisions. Exact zeros remain valid.
Quadratic, quartic and weighted diagnostics have different representable ranges;
a successful K2 observation does not guarantee successful K3 accounting.

The alignment convention alone maps norms below 1e-12 to unresolved directions;
equality at the threshold resolves. It uses stable hypot, with explicit
precision failures, rather than the old naive norm. A conventional zero with
an unresolved input is not orthogonality. No cosine clamp or other threshold
zeroing is applied. Supplied inconsistent readouts retain their residuals.
The full Q prediction retains alpha^2 Q(M), even for numerical macro vectors.

The intensity budget includes the full squared increment, not only first-order
terms. For nonnegative g the first-order coupling term is nonpositive, but
neither intensity nor potential must decrease under the unit-size finite map.
The exact balanced overshoot raises intensity 12 to 48 and potential 6 to 168.
The scalar potential is distinct from intensity, pre-sync state, scalar z and
total T; none is assigned physical-energy units. Phase synchronization preserves
intensities exactly mathematically, up to numerical rounding, and may change
the graph part of the potential.

The cylinder preserves z at zero kappa; the torus then loses height information.
The torus uses the maximum absolute z over the ENTIRE supplied history plus
literal 1e-9. Appending a larger excursion moves an earlier unchanged state.
Returned z_max/H_z/regularizer/R/r_max/N/normalization identify the actual map.
N=12 is historical compatibility; custom N is an explicit parameterization,
not a claim that the old geometry_3d routines honored a changed sector count.
The adapter adopts R>r_max>0. Rounded saturation may reach r_max and H_z may
equal z_max: successful evaluation does not certify the strict inverse domain.
No runtime inverse or direct-total reconstruction from scalar displays is added.

This executable example uses existing step3 for the actual state and observes
it afterward. Its diagnostic prediction is only accounting data.

```python
import json
from dataclasses import asdict
import numpy as np
from kernel_physics.dynamics import DynamicsConfig, step3
from kernel_physics.z_manifold import (
    Clock, StagedConfig, advance_clock, observe_staged, state_norm,
)
from kernel_physics.z_diagnostics import (
    intensity_budget, potential, readout_accounting, chiral_area_accounting,
    historical_alignment, direct_history_coordinates,
    cylinder_history_coordinates, history_torus_coordinates,
)

k3_initial = np.array([.2+.3j, -.4+.1j, .1-.2j])
k3_config = DynamicsConfig(eps=.05, g=.2, phase_strength=.01, k=(1, 1.2, 1.4))
k3_clock_before = Clock()
k3_observer = StagedConfig()
k3_budget = intensity_budget(k3_initial, k3_config)
k3_omega = step3(k3_initial, k3_config)
k3_clock = advance_clock(k3_clock_before, .1)
k3_readout = observe_staged(k3_omega, k3_clock, k3_observer)
k3_history = {
    "kappa": np.array([state_norm(k3_omega)]),
    "phi_index": np.array([k3_clock.q]),
    "z": np.array([k3_readout.z]),
    "Z_total": np.array([k3_readout.Z_total]),
}
k3_example_output = {
    "inputs": {"omega": k3_initial, "dynamics": asdict(k3_config),
               "clock": asdict(k3_clock_before), "observer": asdict(k3_observer)},
    "operations": ["inspect unforced pre-sync budget", "existing step3 once",
                   "explicit clock advance by .1", "K2 staged observation",
                   "passive K3 accounting and three independent displays"],
    "omega_after_existing_step3": k3_omega,
    "clock_after": asdict(k3_clock),
    "budget": asdict(k3_budget),
    "potential_before": potential(k3_initial, k3_config),
    "potential_after": potential(k3_omega, k3_config),
    "readout": asdict(k3_readout),
    "accounting": asdict(readout_accounting(k3_readout, alpha=1, beta=.5)),
    "area": asdict(chiral_area_accounting(k3_omega)),
    "alignment": asdict(historical_alignment(
        k3_readout.Z_macro, k3_readout.Z_chiral, k3_readout.Z_total)),
    "direct": asdict(direct_history_coordinates(k3_history)),
    "cylinder": asdict(cylinder_history_coordinates(k3_history)),
    "torus": asdict(history_torus_coordinates(k3_history)),
}
def k3_json_value(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return [value.real, value.imag]
    raise TypeError(type(value).__name__)

print(json.dumps(k3_example_output, default=k3_json_value, indent=2))
```

K3 does not step Omega, advance clock/EMA, add forcing, restore historical
signed-zero phase evolution, or attach vectors to geometry. Conditional inverse
and information-loss arguments are proof/tests only. Three-channel tube curves,
spikes, percentile scaling, turning consumers, six-gap anchors, UI and physical
gap-energy laws remain deferred. The broader reconstruction is not complete.
