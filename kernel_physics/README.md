# kernel_physics v0.1 baseline + opt-in lens_area_norm_v1

**Paper C exact local geometry + Paper A exact abstract dynamics.**

**NO PHYSICAL COUPLING BETWEEN THEM IS CLAIMED YET.**

This is a separate, minimal Python package. Geometry and dynamics do not import
each other. There is no framework, server, plugin system, memory architecture or
historical-kernel dependency.

## Frozen definitions

- Paper C: PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md,
  §§2–7,9 and Appendix B.
- Paper A: PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md,
  §§1–3 and §6.

The source paths and original SHA-256 hashes are in baseline_manifest.json.
Neither paper was modified. No historical PDF or kernel source was opened.

## Modules

- **geometry.py**: SymPy exact coordinates, w=1, s=sqrt(2)-1, general-angle
  panel maps and the canonical beta=pi/3 weld. folded_module() returns an
  immutable mesh with 18 vertices, 21 edges, three octagonal faces, three seams
  and two nine-edge boundary loops, preserving Paper C's vertex/face ordering.
  Normals are computed from the oriented faces. central_section(height) returns
  three unit segments for abs(height)<=s/2: a curve, not a filled cap.
  rotate_c3, reflect_vertical and reflect_horizontal are the exact D3h
  generators about the centroid axis and the planes x=0, z=0.
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
The complete modern suite now passes **95 tests (75 predecessor + 20 face-view)**.
The added face-view tests and final execution receipts are recorded in the same reviewed
[attachment note](../../research/GPT_proof/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md).

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
No J_eff/EMA/macro-Z interpretation, central-energy law, six-gap mapping, RSB,
portal/field recursion, meta-shell, recursive thermodynamics, magnetic coupling,
gravity, wormholes, physical color/quark interpretation or production TORMENT
behavior is implemented. These remain explicit outstanding interfaces/features.
The SRG orientation cycle is not Paper-A evolution. This adopted finite-dimensional
face view supplies no physical field, units, phase generator, surface interpolation,
seam condition or justified mode selection. The broader reconstruction is unfinished.
