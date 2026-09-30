# Detached analysis protocol v1 — normative Stage B1 specification

Authority: reviewed architecture and A0 freeze; B1 order of 30 September 2026.
All names below are now allocated for this distribution. B2 execution attestation
and production resource approval remain unavailable.

## 1. Namespaces and scope

| Item | Frozen value |
|---|---|
| Distribution / version | `trioctagon-analysis` / `0.1.0` |
| Import package | `trioctagon_analysis` |
| Protocol | `TRIOCTAGON_ANALYSIS_PROTOCOL` / integer `1` |
| Catalogue | `TRIOCTAGON_ANALYSIS_CATALOGUE` / `1.0.0` |
| Request | `TRIOCTAGON_ANALYSIS_REQUEST` / `1.0.0` |
| Derived record | `TRIOCTAGON_DERIVED_ANALYSIS_RECORD` / `1.0.0` |
| Attempt receipt | `TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT` / `1.0.0` |
| Operation | `core.app04.recorded_chirality_accounting.inspect` / integer revision `1` |
| Provider | `core.app04.recorded_copy` / integer revision `1` |
| Codec | `TRIOCTAGON_CANONICAL_JSON_1` |
| Profile implemented | `CORE` |
| Reserved, rejected profiles | `HISTORICAL`, `EXPERIMENTAL_ANALYSIS` |
| Reserved, unimplemented family | `TRIOCTAGON_EXPERIMENTAL_RECORD` |

The root kernel distribution, API 1.0.0, RunRecord 1.0.0, GeometryRecord 1.0.0 /
Exact Codec 1, UI request/response v2, existing artifact lock, and Core
resume/checkpoint semantics are unchanged. No subclass or new key is added to
RunRecord. Reusing a formula or renderer cannot promote Historical/Experimental
authority.

## 2. Exact canonical JSON bytes

Encoding is UTF-8, without BOM or trailing newline. Objects use `,` and `:` with
no insignificant whitespace. Keys are ordered by Unicode scalar value
lexicographically (not UTF-16 code-unit order). Arrays preserve order.

Strings retain their Unicode content without NFC/NFD normalization. Encode
quotation mark as `\"`, backslash as `\\`, and backspace/form-feed/newline/
carriage-return/tab as `\b`, `\f`, `\n`, `\r`, `\t`. Other U+0000–U+001F controls
use lowercase six-byte `\u00hh` escapes. Do not escape solidus. All other valid
Unicode scalars, including U+2028/U+2029 and non-BMP characters, are literal UTF-8.
Unpaired surrogates/invalid UTF-8 are rejected.

JSON null and booleans use `null`, `true`, `false`. Booleans are never integers.
JSON floating-point tokens, NaN and Infinity are rejected everywhere in these
scientific protocol documents. Integers use base-10 canonical digits at
explicitly schema-typed paths only; no leading zeros, decimal point, exponent or
negative integer zero. Current protocol counters/revisions/limits are
nonnegative or positive according to their schema. Large Core update indices
are retained as Core's canonical decimal **strings**.

Binary64 is exactly `{"f64":"<token>"}`. The token must decode to finite binary64
and round-trip identically through Python binary64 `float.hex()`, as the existing
Core codec requires. No alternate spelling, extra key or decimal normalization.
`0x0.0p+0` and `-0x0.0p+0` remain distinct. Finite subnormal **stored tokens** are
preserved; the inspector does not redo scientific intermediate-domain checks.

Duplicate keys are rejected at every depth. The parser has fixed internal
duplicate/number validation callbacks; there is no caller-supplied object hook,
class reconstruction, eval, expression parsing or custom deserializer.
Untrusted byte parsing requires an explicit positive byte/depth budget and
checks nesting before JSON decoding. Byte decoding of model documents is followed
by their closed schema validation; raw integers cannot become implicitly typed.
In-memory constructors are for already bounded caller-owned data.

A request/import may be noncompact valid JSON and is canonicalized by its typed
model. Content-addressed persisted DerivedAnalysisRecord bytes **must already
equal** their canonical encoding. Core parents may be pretty printed: preserve
their original input bytes separately from public canonical serialization.

Seven independent golden byte vectors in `tests/fixtures/golden_vectors.json`
freeze Unicode order, escaping, typed integers, arrays and signed zero. Invalid
vectors exercise duplicates, untyped numbers, nonfinite values and invalid text.

## 3. Exact digest preimages and scopes

For each **new canonical-content** digest, the exact preimage is:

~~~text
ASCII("TRIOCTAGON") || 0x00 || ASCII(SCOPE) || 0x00 || ASCII("V1") || 0x00 || canonical_bytes
~~~

There is no BOM, newline, length prefix or terminal separator. Scope labels
contain only their fixed uppercase ASCII/underscore names. `V1` binds the codec
specified above. The digest is lowercase SHA-256 hex of that complete preimage.
Ten golden preimages/hashes freeze all allocated content scopes.

Digest objects have exactly `scope`, `algorithm = "SHA-256"`, `codec` and
`sha256`. Python digest classes are distinct immutable types; equality and
consuming APIs distinguish their scope even when hex strings coincide.

| Scope / type | Definition |
|---|---|
| INPUT_BYTE_DIGEST / InputByteDigest | Ordinary SHA-256 of exact retained input bytes; codec `RAW_BYTES`. |
| PARENT_SEMANTIC_DIGEST / ParentSemanticDigest | Unchanged, publicly validated native Core `deterministic_sha256`; codec `KERNEL_RUN_RECORD_1.0.0_NATIVE`. The analysis package does not compute or rename it as its own digest. |
| PARENT_CANONICAL_BYTE_DIGEST / ParentCanonicalByteDigest | Ordinary SHA-256 of the complete public `RunRecord.to_json()` UTF-8 bytes, including execution metadata/native digest; codec `KERNEL_RUN_RECORD_1.0.0_CANONICAL_UTF8`. |
| PRODUCER_BUILD_IDENTITY / ProducerBuildIdentity | Domain-separated approved build descriptor: source/content/revision, distribution archive/build inputs, provider/member inventory and dependency/runtime policies. |
| REQUEST_DIGEST / RequestDigest | Domain-separated complete validated request body. No transport filename, attempt nonce or timestamp. |
| SEMANTIC_RESULT_DIGEST / SemanticResultDigest | Domain-separated closed projection specified below. |
| FULL_ARTIFACT_DIGEST / FullArtifactDigest | Ordinary SHA-256 of every finalized artifact byte; codec `RAW_BYTES`; stored externally, never inside the bytes it hashes. |

The three byte-hash scopes deliberately retain A0's exact-byte SHA-256
definitions; their separation is type/label based, not a modified preimage.
The native Core semantic digest also remains unchanged. Domain framing applies
to new application **content** identities, not these raw/native exceptions.

Additional framed scopes are CATALOGUE_DIGEST, DESCRIPTOR_DIGEST, POLICY_DIGEST,
MANIFEST_DIGEST, APPROVAL_ROOT_DIGEST, RESULT_PAYLOAD_DIGEST and
ATTESTATION_EVIDENCE_DIGEST. Their owning strict model or approved manifest
supplies canonical bytes. A low-level hash helper does not validate a manifest's
truth or approve its content.

The semantic-result projection contains family/schema/Core profile, request
digest, catalogue digest, producer build identity, participating kernel selection
and roles, complete typed parent references, authority/status assertions,
qualification, reproducibility and warnings. It includes the validated
CopyPayload's complete canonical JSON as a **JSON string** under
`result_payload`; encode that string with the same escaping rules. This explicit
choice avoids a second untyped numeric interpretation of payload counters.
Array order, input-byte provenance and exact stored token strings remain bound.

Exclude only the result's own digest, full byte digest, approval deployment/
attestation execution receipt, timestamps, actual environment and other volatile
completion facts from that semantic projection. Those remain included in the
full artifact bytes. Producer build/kernel identities remain included. Two
different producer environments can therefore have the same semantic identity
but different full byte identities. Different original parent formatting changes
the request and semantic result because original-byte provenance is deliberately
bound; this is not a mathematical-answer equivalence hash.

Job evidence binds request and payload; the outer artifact binds that evidence.
No object contains its own full-byte hash. Referenced manifests do not need a
self-hash slot. Hash cycles are prohibited.

**HASH != AUTHORSHIP. HASH != SIGNATURE.** A reader can check self-consistency
without authenticating an origin or replaying equations. Recomputed hashes on a
forged self-consistent artifact do not establish a real historical execution.

## 4. Closed models and integer ownership

Every model rejects extra/missing fields. Frozen canonical bytes are the owned
state; `data` is recursively immutable and `to_dict()` is detached.
The implementation's closed schema declarations are part of this specification:

| Module/type | Fields and enforced relationships |
|---|---|
| catalogue.Descriptor | Exact operation/revision/domain/support/profile/lifecycle, provider builds, parent family/schema/API/triad shape, selection, 16 paths, vector axes, output schema, authority, statuses, qualification, assumptions, numerical/reproducibility/effect/failure rules, resource policy. All scientific/effect fields must equal the frozen APP04 descriptor. |
| catalogue.Catalogue | Family/schema and exactly one descriptor. No dynamic operation or provider discovery. |
| common.ProducerBuild | Distribution/version, fixed provider/revision/entry point, source repository/revision/content, actual archive/build inputs, dependency/runtime policy digests, sorted unique safe relative members with byte size/hash. |
| common.KernelSelection | Distribution/version, source repository/revision, lock byte hash, actual archive byte hash, exact/preferred versus reconstruction classification, stable-member and certification manifests. Actual archive is never replaced with a preferred archive's label. |
| common.ResourcePolicy | PROPOSED/APPROVED, proposal identity, exact logical bounds, nullable finite deployment limits. APPROVED requires every limit; existence of this claim is not application deployment approval. |
| approval.ApprovalRoot | Exact catalogue/descriptor digests, provider/build allowlist, accepted attestor build, dependency/runtime/resource policies, kernel selection, deployment approval receipt and non-authorship qualification. |
| requests.ParentReference | Source role, native family/schema, semantic/original/canonical identities and original implementation source claims. |
| requests.Selection | Nonnegative integer ordinal, canonical expected update-index string, 1–16 unique ordered allowlisted fields. |
| requests.Request | Family/schema/protocol, catalogue/descriptor, operation/revision/profile, provider, one parent, selection, empty parameters, empty external inputs, resource policy and kernel selection. No status override. |
| provider.CopyPayload | Own schema, ordinal/update-index, ordered field/path/value rows, recomputation NOT_PERFORMED, numerical/reproducibility labels. This is an unattested payload, not a success record. |
| attestation.ProducerEvidence | Method, request/attempt/approval binding, nullable actual build/attestor/environment/installation/snapshot/import/kernel/payload evidence, kernel roles, recomputation label and eight-check vector. |
| records.DerivedAnalysisRecord | Core family/schema/profile, embedded catalogue/approval/request, request digest, parents, producer evidence, authority/statuses, exact payload, qualification/reproducibility/warnings, semantic digest and complete completion evidence. |
| records.AttemptReceipt | Nullable valid request/digest, optional submitted-byte identity, attempt, refusal/failure/cancel outcome, terminal stage, stable error category, completed checks/vector, available producer evidence, bounded diagnostic and non-success staging disposition. |

Integer paths are supplied by these validators: protocol version, revisions,
ordinals, member sizes, logical/resource limits and diagnostic bound. No other
application/scientific numeric field may silently become a JSON number.

Catalogue creation returns a **candidate**, not an approved deployment.
ApprovalRoot is an application-owned data interface. B1 does not ship a
provider-generated approval root or a local accept-anything root. Its future
trusted installation/approval process is B2/UI work.

## 5. Evidence, attestation and the closed B1 gate

Keep PARENT_IDENTITY, PRODUCER_IDENTITY, KERNEL_USED_BY_PRODUCER and
AUTHORITY_IDENTITY independent. Parent source commit is never an analysis
producer identity. Version strings, GUI text, filenames, a mutable checkout
and an inferred current kernel are insufficient.

The check vector has exactly: catalogue_approved, build_evidence_accepted,
installed_content_verified, execution_snapshot_bound, actual_imports_origins_bound,
inputs_verified, payload_validated, participating_kernel_verified. Each state is
VERIFIED, FAILED, NOT_APPLICABLE or UNAVAILABLE with a reason and an evidence
manifest reference where VERIFIED. All eight are applicable to APP04 success.
A successful-record **claim** requires all eight VERIFIED and complete matching
build/kernel/request/root/payload/completion bindings. Parsing those claims is
not performing those checks.

`UNAVAILABLE_B1` producer evidence cannot contain a VERIFIED state.
`SnapshotAttestor` is an interface only. `SnapshotBindingRequest` requires
fixed absolute Windows runtime/import paths, closure identity and the accepted
trusted-host/reviewed-provider threat model. No implementation is shipped.

B2 must demonstrate a fresh protected per-job snapshot, prevention of executable
write/replacement for the job duration, exact runtime/provider/kernel closure,
actual module-origin checks and no network/import fallback. Hash scans alone
are insufficient. Trusted OS, coordinator and host user plus reviewed admitted
provider code are assumed; hostile administrator/host compromise is outside
that assurance. B1 does not claim any of this is already proved.

The public B1 coordinator has no attestor injection or success branch:
unapproved policies refuse immediately; otherwise bounded public parent
validation and exact copy may run, after which issuance unconditionally refuses
with `B1_VERIFIED_LANE_DISABLED`. There is one active attempt per process lane;
concurrent submissions receive a resource refusal. Accepted cancellation before
work yields only a receipt. Exceptions yield bounded failure/refusal receipts.
No record is silently replaced and no failure returns a previous successful
payload.

Tests construct unmistakably labeled TEST_ONLY mock evidence exclusively under
`tests/` to exercise inert record schemas/persistence. Those fixtures are not
distributed in the wheel, and cannot open the production coordinator.

## 6. APP04 parent, copy and missing-data contract

Require bytes of a publicly loadable RunRecord 1.0.0/API 1.0.0, triad, state size
`"3"`. No raw dict, GeometryRecord, derived/experimental record or ring, including
a three-state ring. Preserve valid old-source records and record validator
selection separately. Core loading validates structure/digest, not replay.

The sole runtime kernel import is `from kernel_physics import api` in
`ParentSnapshot`, and the sole call is `api.RunRecord.from_json`. Use the public
record's serialization and digest. Kernel role is `parent_validation`;
scientific recomputation is `NOT_PERFORMED`.

At ordinal o, S means `samples[o]`; D means
`S.diagnostics.chiral_area_accounting`. Exact ordered selection universe:

~~~text
S.raw_readouts.z_chiral
D.chiral
D.A
D.B
D.h
D.intensity
D.chiral_norm
D.chiral_norm_squared
D.gram_product
D.h_squared
D.gram_rhs
D.gram_residual
D.amplitude_bound
D.slack_sum_of_squares
D.observed_slack
D.slack_residual
~~~

Two whole three-vectors plus fourteen scalars, maximum 20 numeric leaves.
A raw and diagnostic chirality vector are distinct paths; never reconcile or
substitute them. Each result row contains the selected field name, exact
`/samples/o/...` source path and copied value. Copy order and signed zeros/
residuals unchanged. Require selected ordinal's stored update index to match
the explicit expected string; ordinal and recurrence index are not interchangeable.

Missing requested optional data refuses the entire request with
`MISSING_RECORDED_FIELD`; no partial success, smaller-subset retry or recomputation.
A declared diagnostic missing required fields fails public parent validation.
No norms, subtractions, normalization, tolerance comparison, epsilon cleanup,
theorem/equality/sharpness score, observer update or physical mapping is computed.
`D.chiral_norm` is allowed because it is already a stored value.

Successful claim qualification is exactly the fixed text in `constants.py`:
recorded data copied without scientific recomputation; structure/digests validated
without replay; floating residuals are not exact certificates; channel chirality
is not physical placement or calibrated energy. Atlas 07's prior Windows runtime
caveat remains hash-bound context and is not resolved by B1.

## 7. Persistence, cancellation and recovery

For an already finalized inert DerivedAnalysisRecord:

1. Validate the record and obtain its complete canonical bytes.
2. Compute external FULL_ARTIFACT_DIGEST.
3. Create a new exclusive temporary file in the **same destination directory**.
4. Write complete bytes, flush the Python buffer, and fsync the writable handle.
5. Publish with Windows `MoveFileExW` using `MOVEFILE_WRITE_THROUGH` only.
   No REPLACE_EXISTING, COPY_ALLOWED, cross-volume or delayed-reboot fallback.
6. Final name is `sha256-<full lowercase digest>.json`.
7. If another writer already created the final name, independently verify size,
   complete hash and exact bytes. Identical content is idempotent reuse; differing
   content is a refusal and remains untouched.
8. Clean up only the exact owned temporary file. Never delete a preexisting
   destination to make a retry succeed.

Publication is qualified for an existing application-owned directory on a local
fixed NTFS volume without reparse-point ancestors. Unsupported filesystem/path/
permission behavior fails closed. B1 provides no weaker portability fallback.
Import/codec work can remain headless; NTFS publication is platform-specific.

The rename is the commit boundary. Before it, no final artifact is visible;
temporary files are never accepted as successful records. After it, a complete
immutable object exists. A lost acknowledgement after commit must be recovered
by content-address validation, not by rewriting that object. Single-file
publication avoids a JSON/sidecar pair transaction. This is not a claim of
unconditional hardware/power-loss durability. Load checks filename, exact-byte
digest, schema and canonical bytes; missing/truncated/corrupt objects are refused.

The full hash is represented by the filename and returned StoredArtifact, not
inside the JSON. `load_record` checks a separately typed FullArtifactDigest;
a parent/input digest with identical hex is not accepted as a substitute.

Reference semantics:
[Python Windows rename behavior](https://docs.python.org/3.11/library/os.html#os.rename)
and [Microsoft MoveFileExW flags](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw).
Local tests cover collisions, concurrent identical writers, failure before
rename/fsync, canonicality and later corruption. They do not prove B2's
execution-snapshot binding.

## 8. Legacy, resources and non-goals

Legacy passive caches, AnalysisView and export sidecars remain under their
existing contracts. Reject them as new DerivedAnalysisRecords. Future UI
wording should identify “Legacy detached analysis; producer not independently
verified under the new analysis protocol.” No in-place migration.

New record loads are typed inert claims. Present “Core derived inspection;
copied from recorded sample; scientific recomputation: none” with parent and
separately verified-or-unverified producer evidence. B1 supplies no UI adapter
implementation and no producer-authentication badge.

Finite byte/depth/sample/output/diagnostic checks use caller-selected explicit
budgets. The resource-policy model also binds time/memory requirements; **B1 does
not implement OS-enforced time/memory limits**. These and execution protection
remain B2 prerequisites. The measured proposal is not enabled policy. A valid
Core record outside a proposed operational envelope remains a valid Core record;
the boundary may eventually refuse an operation under an approved resource
policy, never declare the scientific schema invalid on that basis.

No recomputation descriptor, historical provider, experimental engine, API
endpoint, UI integration, workflow rewrite, release or tag modification is part
of B1.
