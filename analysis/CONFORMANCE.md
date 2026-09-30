# B1 conformance and deferred enforcement

Tests use handcrafted structurally valid Core records, not new simulations.
Only the public RunRecord loader is called. TEST_ONLY mock attestation exists
under `tests/support.py` to exercise inert claim codecs and persistence; it is
not shipped in the runtime wheel and does not enable a production coordinator.

## A0 N01–N30 coverage

| Boundary | B1 evidence | Remaining B2 responsibility |
|---|---|---|
| N01 wrong family | Parent/model family and raw-dict rejection. | None for this structural rule. |
| N02 incompatible schema | Public-loader/API/schema and triad-only rejection. | Installed loader binding. |
| N03 original bytes altered | Exact input identity mismatch. | Protected input delivery throughout a real job. |
| N04 canonical bytes altered | Environment-only edit preserves native digest but fails full parent binding. | Protected snapshot custody. |
| N05 wrong semantic digest | Public native validation and reference mismatch. | No authorship/replay inference. |
| N06 wrong producer | Build mismatch rejected even with equal version label. | Verify installed build in reality. |
| N07 unverified producer | Missing required check rejected; coordinator always refuses issuance. | Real attestation mechanism. |
| N08 operation/version | Only recorded APP04 revision 1 accepted. | No recompute enablement implied. |
| N09 provider/build | Closed registry/allowlist validation. | Actual executable binding. |
| N10 authority/catalogue | Changed hash, status override and descriptor semantics rejected. | Deploy independently approved root. |
| N11 external data | Initial APP04 rejects any external input. | Future external-data profiles are out of scope. |
| N12 sample/index | Bounds, type and exact expected-index tests. | None for copy semantics. |
| N13 missing field | Whole-request receipt; no smaller-subset success; malformed declared diagnostic fails parent validation. | None for copy semantics. |
| N14 forbidden selection | Wildcards, duplicate paths, observer fields and component remaps rejected. | None for copy semantics. |
| N15 Historical under Core | Historical provider identity rejected. | No historical implementation. |
| N16 Experimental/Core confusion | Unimplemented profiles/families rejected. | No experimental implementation. |
| N17 mutation | Immutable bytes/references, detached trees, no parent path/write API. | OS capability/write-prevention proof is not supplied by Python immutability. |
| N18 implicit recomputation | Forbidden public scientific functions patched to fail; copying/missing-data handling calls none. | UI selection wiring is out of scope. |
| N19 resume/checkpoint | Operation/parameter rejection. | Existing Core routes remain unchanged. |
| N20 conversion | Unknown cross-domain conversion request rejected. | No conversion provider. |
| N21 origins/kernel | Missing origin/snapshot evidence and wrong selection claims rejected. | Actual origin/closure observation and prevention. |
| N22 false kernel attribution | Parent commit cannot substitute for selected kernel; invalid role rejected. | Verify archive/member evidence in a live snapshot. |
| N23 stale result | Request/payload/attempt/completion correlations checked. | Live IPC custody/replay prevention. |
| N24 wrong copied value | Sign-token change rejected despite numerical zero equivalence. | None for stored-copy comparison. |
| N25 attestation gap | B1 cannot label its evidence verified; incomplete B2 claims rejected. | Enforced immutable execution snapshot throughout the job. |
| N26 resources/effects | Finite policy structure, explicit parser/copy budgets, fixed effects and single-lane concurrency. | OS time/memory/effect enforcement and deployment limit approval. |
| N27 cancellation/failure | Pre-work cancellation and provider exceptions yield only receipts. | Live long-running cancellation and publication race when B2 has successful jobs. |
| N28 persistence | NTFS collision, fsync/rename failure, concurrent identical writer, corrupt/noncanonical load tests. | No multi-member experimental transaction is implemented. |
| N29 legacy inflation | Legacy cache/sidecar objects fail new record schema. | Future UI wording/typed adapter; no retroactive attestation. |
| N30 overclaim | Altered qualification/status and extra sharpness quantity rejected. | Reader trust display must retain scientific/verification distinction. |

“B1 conformance passes” means the implemented structural/copy/refusal/storage
boundaries pass. It does **not** mean the deferred runtime/sandbox/authentication
parts of N17/N21/N25/N26/N27 have been implemented.

## Positive cases

Full accounting; raw-chirality-only; +0 and -0 token distinction; positive/
negative residuals; vector/field order; nonzero index offset; old-source parent;
pretty versus canonical input-byte identities; execution metadata excluded by
native digest but included by canonical-byte hash; strict record claim roundtrip;
offline parent-copy validation; immutable request/record views.

Golden tests independently freeze canonical UTF-8 bytes and all framed digest
preimages. Package tests statically enforce the sole public loader import/call,
exclude test-only mocks from runtime source, and verify a fresh headless import
loads no kernel or UI.

## Existing boundaries

Relevant existing public-API/export and static import-boundary regression tests
are run separately. Source-byte preservation checks cover every original Core,
UI, paper, Atlas, lock and navigation file. Root kernel build membership is
checked by its existing build backend and a separately built kernel wheel.
The new analysis wheel is tested from an external installation and inspected
for exact package membership; neither kernel nor UI is bundled into it.

No workflow rewrite is required. A main push normally triggers the existing
kernel-distribution certification workflow. The scientific UI workflow is
path-filtered to UI/workflow changes, which B1 does not make.
