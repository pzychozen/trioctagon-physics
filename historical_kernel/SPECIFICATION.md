# Independent Historical TORMENT v0.1

Authority is the accepted H4/H5 packet, including the independent-kernel amendment,
and the exact H6A protocol wheel `734ae5d2734ce9b42301b851e23d57c4b9db37ac02b32b0fadff328d4724952f`.
The source-equation/function/test mapping is `tools/conformance_map.json`. H6B does
not amend Historical mathematics or execute archived source files.

The pure `api` accepts immutable Historical types. It exposes triad step, fresh
run, staged inspection, current-memory EMA inspection and probability chart.
Dynamics uses the same pre-update state in all three terms. Phase uses original
angles simultaneously, canonical exact-zero angles and harmonic three. Only the
three literal k profiles are supported. There is no dt factor, forcing, noise,
normalization, feedback, arbitrary harmonic, selector or production state.

Numerical policy has three distinct domains. Recurrence uses NumPy binary64
finite arithmetic with gradual underflow. Response primitives independently use
the strict H5 normal-or-allowed-zero product/sum policy, `math.fsum`, checked
four-product complex multiplication, stable six-real norm and the frozen
left associations. Chart arithmetic deliberately uses naive abs, square, sum,
divide-if-positive and basis transpose multiplication, with ordered underflow
flags and no stabilization. Overflow/nonfinite results fail the operation.

Fresh runs start at q=0, t=+0 and m=+0. Every update advances Omega, then q and
repeated binary64 t+.1, then selected H memory exactly once from new Omega, then
observation. There are N pre-update rows and a separate terminal. Constructor K/H
observations are literal zero caches, including chirality; standalone inspection
always recomputes. EMA inspection never evaluates J or advances memory.

The protocol adapter supports exactly the five H6A descriptors. Generic codec,
digests and validation come from the accepted protocol and the narrow generic
Core closure. They perform no scientific delegation. Pure mathematics imports
neither protocol records nor current/old/production science.

The local issuer is an explicit API requiring `LocalIssuer(admission_path,
admission_sha256)`. The byte pin comes from trusted local configuration. A request
cannot select it. Every request must match the external catalogue, build and
resource policy. Complete installed inventories and the numerical environment
are checked before and after computation. Inventories describe unprotected
installed bytes, not loaded instructions. Floating-point controls are read, not
silently repaired; nearest-even and gradual-subnormal modes are required.

One request occupies the process-local lane. The isolated worker uses `-I -B` and
an installed venv. Windows venv launcher and actual interpreter share a resource
Job; explicit worker assignment at the ready gate closes the launcher-creation
race. Aggregate private-commit allocation is capped by the Job. The parent also
observes the sum of both processes' peak working set and peak private commit;
this is conservative and can double count resident private pages. Wall time starts
before request parsing and is checked through publication completion. Complete
artifacts are staged and fsynced by the worker and rebound by the parent. Only
then does the parent authorize the worker's atomic hard link, which never replaces
an existing file. Publication stays within the supervised Job/deadline. If the
worker stalls before or after linking, the parent terminates the Job and removes
only this attempt's own link. Tests exercise both cases. Use a responsive local
filesystem for staging/cleanup; this is not a hard real-time Windows guarantee.

Failures return only an AttemptReceipt with bounded diagnostic and progress;
staged candidates are discarded. Output limits include the full record, request,
bundle, evidence and terminal. Manifest caps apply separately to embedded build,
installation observation and execution evidence. The admission bootstrap has a
separate 4 MiB parser cap and depth 64, never a computation admission policy.

Results are `UNATTESTED_HISTORICAL_RECONSTRUCTION`. The seven local checks refer to
actual schema/context/build/installation/payload/independence observations.
Execution-snapshot attestation remains UNAVAILABLE, Windows execution binding
NOT_PROVEN and production attestation false. B2 and P2 are not resumed.

Resource-job and floating-point API references:
[Windows job information](https://learn.microsoft.com/en-us/windows/win32/api/jobapi2/nf-jobapi2-queryinformationjobobject),
[job completion notifications](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_associate_completion_port),
[`_controlfp_s`](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/controlfp-s).
