# B2A conformance and provisional resource review

Classification: **SPECIFICATION**. Test/control success does not change
`WINDOWS_EXECUTION_BINDING = NOT_PROVEN`. R1 remains
`B2A-R1 = BLOCKED_ENVIRONMENT_NOT_AVAILABLE`: no usable disposable Windows guest
was identified and no R1 proof job or new resource measurement was performed.
Production attestation and B2B remain disabled.

## Adversarial cases

Tests in `tests/test_b2a.py` exercise real Windows sharing/DACL behavior and
closed admission/refusal logic. Mock launchers are explicitly TEST_ONLY and
exist only in tests. Full installed-wheel tests are also run outside checkout.
External integration evidence is retained with the B2A closeout.

| Required case | Evidence / qualification |
|---|---|
| Modified analysis before snapshot | Artifact-derived member hash mismatch rejected. |
| Modified snapshot before launch | Mutation injected between copy and freeze is rejected and owned snapshot removed. |
| Active replacement | Real read leases reject write/unlink/replace/rename; an active AppContainer control also rejects write/rename. |
| Wrong Core artifact | Existing exact archive/certification checks plus request/expectation kernel mismatch refusal. |
| Wrong version, matching package name | Closed analysis-version discriminator rejects it. |
| Unexpected import-path module | Exact candidate file and directory inventory rejects it. |
| Editable install | `.egg-link`/startup paths rejected; no installation discovery. |
| Rogue `.pth`/startup hook | Admission rejects it; fixed `._pth` omits site; worker checks startup state. |
| Alternate same-name module | Extra paths and case/path aliases rejected. |
| Unexpected native dependency | **Live strict proof rejects AVG snxhk.dll at startup.** |
| Wrong provider entry point | Closed fixed entry-point schema rejects it. |
| Wrong request digest | Observation binding rejects changed digest and stale nonce. |
| Manifest/member mismatch | Independent pin and exact member/size/hash checks reject it. |
| Unverified approval root | Wrong pin refuses; candidate deployment remains UNAVAILABLE, never a verified approval. |
| Parent changed after request capture | Changed original-byte identity refuses before execution; retained bytes are immutable. |
| Forbidden writable parent | Live AppContainer control denies write access; original data is never written. |
| Network attempt | Zero-capability control cannot connect to a live listener; ordinary control can. Timeout is reported as such, not invented as an access-denied error. |
| Checkout import | Checkout candidates/import roots rejected; fixed worker paths and origin guard exercised by installed unverified controls. |
| Successful output, incomplete attestation | B1 incomplete-claim tests remain; B2A evidence cannot become a DerivedAnalysisRecord. |
| Attestation failure after plausible output | TEST_ONLY launcher writes plausible output then fails; returned observation is discarded. |
| Cleanup failure | Injected failure remains a failure and cannot produce verified output. |

The full protected provider job did **not** reach Python/Core imports or copy
execution because the native gate stopped it first. Successful end-to-end
actual-use binding, kernel participation and payload verification are therefore
UNAVAILABLE. Tests of individual guards and unverified controls do not fill
those evidence-vector items.

## Measurements

All measurements use structural fixtures and the unchanged public loader.
No recurrence, observer, scientific diagnostic, replay or simulation was run.
The initial two-sample fixture has update-index offset 7. Larger controls copy
its stored rows, assign contiguous index metadata and update the structural
native digest; they are not scientific trajectories.

The copied candidate contained approximately 91.5 MB across 3,450 members before
the final documentation/runtime-closure refinement. Its first strict attempt
spent 9.67 seconds preparing/verifying the snapshot and 1.86 seconds cleaning
up, 11.62 seconds overall. It terminated on the third native image. Final
candidate identity and timings are recorded in the closeout, not assumed equal.

Resource-control worker measurements use the copied runtime and installed
preferred Core/dependency artifacts, fixed paths and Python origin checks, but
**do not claim AppContainer/native-gate attestation**. They intentionally measure
the otherwise unreachable public loader/provider behavior separately.

| Samples | Parent bytes | Worker wall seconds | Public load seconds | Copy seconds | Peak working set bytes | Peak sampled private working set bytes | Peak sampled private commit bytes |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 6,102 | 3.715 | 3.113 | 0.00043 | 85,602,304 | 69,124,096 | 106,037,248 |
| 10,000 | 9,703,090 | 7.565 | 6.909 | 0.15258 | 389,816,320 | 365,334,528 | 402,214,912 |
| 40,000 | 38,833,090 | 23.353 | 22.277 | 0.56438 | 1,317,122,048 | 1,283,211,264 | 1,341,005,824 |

`GetProcessMemoryInfo` supplies the extended process working-set/commit counters;
sampling was every approximately 20 ms. `PrivateWorkingSetSize` and
`PrivateUsage` respectively measure private working set and private committed
bytes. Peak total working set is the OS counter; both private peaks are sampled
and can miss short spikes. These figures
include the worker's native libraries/host injection footprint but exclude
coordinator memory and OS-wide/shared-service costs. See
[PROCESS_MEMORY_COUNTERS_EX2](https://learn.microsoft.com/en-us/windows/win32/api/psapi/ns-psapi-process_memory_counters_ex2).

The control observation contained 731 Python origins and was at most 45,709 bytes.
It is neither a fully attested record nor the final full deployment/evidence
bundle. These controls used the corrected verified libffi member; the final
candidate includes that dependency explicitly. No old B1 resource proposal
values are changed.

## Recommendations

| Limit | B1 provisional ceiling | Recommendation | Reason |
|---|---:|---|---|
| Parent input | 64 MiB | **HOLD** | Largest measured input is 38.8 MB. Richer supported observer/provenance shapes and the complete admitted lane remain unmeasured. |
| Sample count | 40,000 | **ACCEPT** as the proposed operational ceiling | The structural ceiling was exercised within provisional time/memory limits. This does not constrain Core record validity or approve deployment. |
| Nesting | 16 | **HOLD** | Current positive structural fixture depth is 7; richer supported shapes need coverage. Parser-limit refusal tests pass. |
| Complete output | 128 KiB | **HOLD** | Control observation fits; a complete accepted attestation/evidence envelope has not been produced. |
| Wall time | 210 seconds | **HOLD** | Control load/copy plus prototype preparation has margin, but the full protected successful path is blocked. |
| Memory | 4 GiB | **HOLD** | Observed worker private peak is 1.34 GB. Coordinator overhead and enforced full-lane peak remain unresolved; sampling is not containment. |
| Primary diagnostic | 1,024 characters | **ACCEPT** | Refusal and cleanup paths retain bounded diagnostics; long injected failure text is truncated without producing a result. |

ACCEPT is a technical recommendation for later review, not production activation.
All ceilings remain provisional. No new kernel/UI behavior or artifact-lock
contract is introduced.

## Validation scope

Run in Command Prompt with `conda activate torment`:

~~~bat
python -B -m pytest analysis/tests -p no:cacheprovider
~~~

The closeout records exact final source/installed counts and relevant existing
Core API/import regressions. Packaging checks inspect the analysis wheel and
the existing selected kernel artifact; root packaging source is unchanged.

**Existing CI does not test the analysis package.** No workflow was modified.
The preserved implementation is disabled proof infrastructure. Source and
installed-wheel suites are run for preservation; a naturally triggered kernel
workflow does not establish analysis coverage or certify Windows binding.
A dedicated analysis CI lane remains a separate review topic. External evidence
bundles and local environment inventories remain outside the repository.
