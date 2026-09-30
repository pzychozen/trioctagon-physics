# B2A Windows execution-binding proof

Classification: **SPECIFICATION** for disabled proof infrastructure.

B2A engineering outcome on 30 September 2026: **NOT_PROVEN**.
The normal B1 coordinator remains closed. No B2B activation is implemented.

~~~text
WINDOWS_EXECUTION_BINDING = NOT_PROVEN
B2A-R1 = BLOCKED_ENVIRONMENT_NOT_AVAILABLE
PRODUCTION_ATTESTATION_ENABLED = NO
READY_FOR_B2B = NO
~~~

R1 identified no usable disposable Windows guest; it did not execute the
provider or resolve deployment approval. The implementation is preserved only
as disabled proof infrastructure, with its executable behavior unchanged from
the retained B2A candidate. Preservation does not repeat the proof or certify
the mechanism. See the [artifact classifications](README.md#preservation-classification).

## Concrete blocker

A Windows loader-event probe observed native startup modules from
`C:\Program Files\AVG\Antivirus`, including `snxhk.dll`, `aswhook.dll` and
additional AVG components. The strict proof attempt admitted the pinned
interpreter image and pinned Windows `ntdll.dll`, then refused `snxhk.dll`
before allowing that load event to continue. The provider did not execute,
no payload was accepted and no DerivedAnalysisRecord was created.

This is an unapproved-closure finding, not an assertion that AVG is malicious.
Antivirus settings, its files, and its allowlists were not changed. Vendor
injection is not silently reclassified as an approved runtime dependency.
The trace demonstrates why a fresh directory and isolated interpreter flags
alone do not establish the requested statement.

## Compared approaches

| Approach | Assessment |
|---|---|
| Fresh copied tree plus pre/post hashes | Useful inventory evidence; a mutation-and-restore interval can evade scans. Insufficient alone. |
| Read-only file attribute | Does not provide an execution or member-set security boundary. Rejected as protection. |
| Directory/file DACLs | Prevent ordinary writes and new members. Need a distinct restricted job identity, retained handles and path checks; trusted-owner privileges are outside an adversarial-owner claim. |
| No-write/no-delete read-sharing handles | Prevent conflicting writes, replacement and deletion while held. Do not alone stop new directory members, alternate imports or network activity. |
| `-I -S -B` and fixed `python311._pth` | Remove ambient Python path/site/cache authority. Do not close native DLL lookup or prevent host startup injection. |
| Fresh zero-capability AppContainer | Separates the job's access rights, restricts network access and can deny child processes. Actual host-native closure must still be checked. |
| Python import-origin observation | Binds source/extension origins for the reviewed worker. A final `sys.modules` scan alone misses transient native loads. |
| Windows native debug events | Allow an external coordinator to inspect loader events while the target is suspended. Unexpected native images cause termination; no permissive fallback. |
| Post-completion scan | Supplementary check only; it cannot repair missing continuous protection or a rejected native load. |

The implemented candidate combines a copied artifact-derived tree, restrictive
DACLs, retained read-sharing handles, fixed interpreter/import paths, a
zero-capability AppContainer, Python origin checks and native load-event gating.
The host finding prevents claiming that this combination has completed the
end-to-end proof.

Windows documents the sharing controls used by `ReadLease` in
[CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew).
The implementation keeps handles for every copied member and directory for
the attempt duration; directories also receive DACL protection. It rejects
reparse points, hard-linked files, path traversal, reserved names, case aliases,
unexpected files and unexpected directories.

The child receives a new AppContainer SID, zero capabilities, no inherited
handles, a filtered environment and a child-process restriction. Only owned
staging objects receive ACL changes. The OS-control probe confirmed an
AppContainer token with capability count zero, denied writes to protected
locations, denied child creation, and no connection to a broker listener that
accepted an ordinary control connection. See Microsoft's
[AppContainer launch model](https://learn.microsoft.com/en-us/windows/win32/secauthz/implementing-an-appcontainer)
and [process attributes](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute).

Native image paths come from debugger-provided file handles. They are compared
to individually pinned members, leased and hashed before the coordinator
continues the event. A rejected event terminates the worker and drains exit
events. The OS suspends the affected process for these events; this is stronger
evidence than polling its module list. See
[debugging events](https://learn.microsoft.com/en-us/windows/win32/debug/debugging-events)
and [LOAD_DLL_DEBUG_INFO](https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-load_dll_debug_info).
This is not a malware-proof native-code sandbox or proof against a compromised
OS, administrator or trusted coordinator.

## Expected identities and approval

The kernel is the **preferred exact artifact** named by the existing
`apps/scientific_ui/kernel-artifact.lock.json`, with SHA-256
`8f7c8a3e3c8f84e0f07344e8deae633d07b17aec9f05e8559791994e91ac9c36`.
The existing wheel-equivalence verifier checked its 25 stable members, optional
witness, complete RECORD, provenance, source identity and original certification
evidence. Its 27-member archive was neither rewritten nor reconstructed.

NumPy 2.4.4, SymPy 1.14.0 and mpmath 1.3.0 wheels use the existing dependency
lock's hashes. Python 3.11.15 and its selected runtime dependencies come from
independently retrieved Anaconda package archives, verified against retained
archive pins and their package member manifests. The candidate is constructed
from these archive bytes, not by blessing the current arbitrary installation.
An initial launch failure exposed missing `zlib.dll` that an ordinary launch
had resolved through the Conda environment; explicit closure construction
corrected the prototype. The `_ctypes` import also requires the actual `ffi.dll`
name from the verified libffi package.

The analysis/attestor candidate is built from the bounded local analysis source
into an external wheel. Its exact archive and member identities are retained
before candidate installation. Uncommitted candidate source uses a content
identity, not a false assertion that the B1 Git commit contains B2A code.

The expected snapshot includes every admitted member's size/hash, exact import
roots, interpreter, fixed provider entry point, artifact authorities, kernel
selection and separately listed Windows OS members. OS entries are individually
pinned under the explicitly trusted-host-OS premise; this is not an independent
certification of Windows itself. No directory wildcard admits vendor DLLs.

An externally retained expectation pin and B1 ApprovalRoot candidate bind these
choices. **Deployment approval remains pending GPT/Hilmir review.** A candidate
pin's consistency is not promoted to `catalogue_approved = VERIFIED`.
`HASH != SIGNATURE` and `HASH != AUTHORSHIP` remain explicit.
No expected manifest is generated from the candidate being validated.

## Proof interfaces and custody

- `b2a_snapshot` implements strict expectations, independent-pin admission,
  exact tree validation, fresh copied snapshots, DACLs, leases and owned cleanup.
- `b2a_windows` contains the narrow Win32 primitives and fresh AppContainer
  launcher. It supports Windows x86-64 only.
- `b2a_worker` is a fixed structural-copy worker with fixed import roots and
  an origin-checking finder. It uses the existing public provider and loader;
  it does not import private kernel APIs. Audit checks supplement OS restrictions.
- `b2a_proof` checks request/root/kernel bindings, immutable input custody and
  native load events. It returns B2A proof evidence only and cannot issue a
  normal verified result. Plausible output is discarded after failure.
- Proof evidence can use the existing NTFS no-replacement publication primitives
  with a distinct `sha256-<digest>.b2a.json` identity. It is not loaded through
  DerivedAnalysisRecord.

The proof vector has the B2A spelling `actual_imports_bound`. This corresponds
to B1's `actual_imports_origins_bound`; the B1 schema is not renamed or changed.
The other seven check names are shared. Each state is explicit. In the observed
strict attempt, member/build/input checks succeeded, native imports failed,
and execution/kernel/payload completion remained unavailable.

Only the trusted coordinator launches the fixed Python worker. No scientific
provider shell or tool process is added. Acquisition/build tools run outside
the job and are enumerated in the retained preparation scripts. OS-control and
resource-control jobs are labeled **UNATTESTED_B2A_*_CONTROL** and cannot establish
the execution-binding claim. They do not pass through a relaxed attestation path.

## Remaining review boundary

The current host cannot pass the closed native-origin gate as configured.
A separately reviewed execution environment or complete admitted native-closure
design is needed before repeating the proof. No automatic vendor allowlist,
security-software exclusion, fallback environment or bypass is supplied.

Approval deployment, the full successful native/Python/Core origin chain,
complete effect confinement, OS-enforced resource limits and successful-path
custody still require evidence. The prototype's sampled private-memory threshold
and wall watchdog are provisional test controls, not OS memory containment.

[Conformance and resource review](B2A_CONFORMANCE.md) separates tested refusals,
unverified controls and checks blocked by the startup finding.
Production attestation remains disabled and readiness for B2B is **NO**.
