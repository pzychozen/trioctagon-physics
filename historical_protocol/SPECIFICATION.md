# H6A Historical protocol / schema implementation

## Frozen authority

This implements accepted H5 including its independent-kernel amendment. Accepted
final H5 report byte SHA-256:
`615fa946afc57d41e3239bc2ece5f67112e20dba1d04aed7a9379aa15ff27699`.
H4 report: `0416c59017c86183df891148d4e4c0228330dc9444a34cbd1582a331c99eeac5`.
H4 exact constants source: `55fd3efa1c2ef0cd61848637a217d988a487e2ce647041c5bfcff4e0deaea37d`.
Independent amendment: `402ef742f1c35aa43df2df8365e1ebc62fd9fcd0b6729b140f4746f35784cb60`.

The immutable `data/authority.json` records the accepted H0–H4, A0/B1/UI-P1,
amendment, H5, constants-source and five historical source identities. These were
verified against the retained H5 source manifest before materialization. Absolute
paths are absent. `data/constants.json` contains the exact frozen binary64 tokens;
it does not run a k selector or derive constants from irrational values.
`data/comparison.json` pins the H2/H3/current-baseline evidence with the explicit
COMPARISON_REFERENCE_ONLY role.

`CURRENT_STEP3_REUSE_ALLOWED = NO_FOR_HISTORICAL_REFERENCE_IMPLEMENTATION`.
The future implementation strategy is CLEAN_INDEPENDENT_REIMPLEMENTATION. H6A
contains no Historical equations. H2 expected agreement remains acceptance
evidence for future independent H6B conformance, not permission for delegation.

## Closed owners

Every object rejects additional/missing fields and wrong discriminator types.
Integers are schema-owned nonnegative exact Python/JSON integers, never booleans.
Scientific leaves use finite canonical `{"f64":"<float.hex token>"}` objects.
Raw floats, NaN/Infinity, alternative spellings, duplicate keys, malformed UTF-8,
unpaired surrogates, BOMs and untyped integers are rejected by the unchanged codec.
Signed zero is preserved. Caller-supplied finite byte/depth limits bound parsing.

| Owner | Family / schema |
| --- | --- |
| HProtocol | TRIOCTAGON_HISTORICAL_ANALYSIS_PROTOCOL / integer 1 |
| Catalogue | TRIOCTAGON_HISTORICAL_ANALYSIS_CATALOGUE / 1.0.0 |
| Request | TRIOCTAGON_HISTORICAL_ANALYSIS_REQUEST / 1.0.0 |
| DerivedRecord | TRIOCTAGON_HISTORICAL_DERIVED_ANALYSIS_RECORD / 1.0.0 |
| AttemptReceipt | TRIOCTAGON_HISTORICAL_ANALYSIS_ATTEMPT_RECEIPT / 1.0.0 |
| AuthorityPacket | TRIOCTAGON_HISTORICAL_AUTHORITY_PACKET / 1.0.0 |
| ConstantsPacket | TRIOCTAGON_HISTORICAL_CONSTANTS_PACKET / 1.0.0 |
| ResourcePolicy | TRIOCTAGON_HISTORICAL_RESOURCE_POLICY / 1.0.0 |
| ProviderBuild | TRIOCTAGON_HISTORICAL_PROVIDER_BUILD / 1.0.0 |

All relevant owners fix HISTORICAL, H4_COMPATIBILITY_V1 and
INDEPENDENT_HISTORICAL_REFERENCE_1. Request has exactly family/schema/body/digest;
its digest excludes its own field. Inputs are one EXPLICIT_RAW_TRIAD of three
complex channels. Request constants and numerical-policy literals are exact
operation/selector projections. No parent, source/module execution target,
service, geometry, forcing, noise, arbitrary provider or plugin is accepted.

Exactly five revision-1 descriptors exist:

| Operation | Payload owner | Structural obligations |
| --- | --- | --- |
| historical.triad.step.inspect | StepPayload / H_STEP_1 | One update, exact input/constants/k binding, output triad; no clock/history/readout |
| historical.triad.run.inspect | RunPayload / H_RUN_1 | N requested/completed rows 0..N−1, distinct terminal N, q/index relation, constructor markers/positive-zero cache, readout selector, H memory count |
| historical.readout.staged_z.inspect | StagedPayload / H_STAGED_1 | RECOMPUTED and USER_SUPPLIED_CLOCK, bounded q/t, no history/memory |
| historical.readout.ema_z.inspect | EMAPayload / H_EMA_1 | Same clock convention, token-identical memory echo, zero memory-update count, supplied-memory qualification |
| historical.probability_chart.inspect | ChartPayload / H_CHART_1 | Fixed cu/cx/cy basis/order, domains, three zero classes, stage flags, ordered applicable warnings |

Metadata comparisons never replay a recurrence, recompute t, advance EMA, calculate
magnitudes, sum weights, normalize or multiply the basis. The chart validators
compare stored a/sum/weights/input-zero predicates to their stored flags and class.
Self-consistent but scientifically wrong finite claims can parse. Tests explicitly
exercise this limitation.

## Result, evidence and receipt

The result envelope contains exactly family/schema/protocol/profile/contract/
implementation_policy/issuance_class/request/contract_bundle/provider_binding/
payload/qualifications/assurance/execution_evidence/completion/
semantic_result_digest/metadata. Each bundle member is independently strict and
all request/catalogue/descriptor/packet/build/policy references must agree.
Fixed qualifications deny production replay, physical geometry and validation.
Current-kernel role is NOT_USED with empty scientific_delegations.

Assurance separates SCHEMA_AND_BINDINGS_VALID (equations_replayed false),
HISTORICAL_RECONSTRUCTION_CLAIM (math verification NOT_PERFORMED), and execution
attestation UNAVAILABLE / NOT_PROVEN / false. Success evidence has seven exact
LOCAL_CHECK_PASSED claims with typed references/fixed reasons; the last check is
always UNAVAILABLE/null/B2_WINDOWS_EXECUTION_BINDING_NOT_PROVEN. No Historical
success check permits VERIFIED. Before/after member inventories must agree with
the build claim; numeric libraries agree with its dependency declarations.
Parsing performs no installation scan, monitoring, execution or attestation.

The only success class is UNATTESTED_HISTORICAL_RECONSTRUCTION. A schema-valid
complete claim requires a structurally measured policy and consistent resource
observations. Canonical request/aggregate output/embedded manifest sizes, nesting,
run counts and claimed observed limits are compared to that policy. This does not
prove real measurements or original submission byte size from its digest; future
ingestion/enforcement/admission belong to H6B. The default remains pending/null/null.

Persisted results and receipts require exact canonical bytes without trailing
newline. Requests can canonicalize permitted whitespace. Source locators are
sorted, unique display metadata restricted to known reference IDs and never read.
An original submitted byte hash is an inert claim when original bytes are absent.

Receipts have the separate Historical family and exactly the H5 field set. Outcomes
are REFUSED/FAILED/CANCELLED, never COMPLETE; cancellation category and outcome
agree. The request/digest pair is both null or a valid bound request. Unknown
operations therefore cannot survive as executable names. Optional external
context consistency is separate from parsing. Progress is a bounded count only
for a valid run which reached computation; no partial scientific payload is
allowed. Diagnostics are bounded by UTF-8 bytes. A passed payload check is permitted
only for a complete staged candidate followed by persistence failure/cancellation;
only its scoped digest appears, never numerical values. H5's 23 failure categories
are frozen in errors.CATEGORIES. Parser validation errors additionally distinguish
INVALID_SCHEMA/INVALID_CODEC; no coordinator exists to issue failure receipts.

## Digests and package boundary

The fourteen Historical content types are owned solely by this package. V1
framing is `TRIOCTAGON || NUL || scope || NUL || V1 || NUL || canonical bytes`.
SHA-256 covers that preimage. Existing INPUT_BYTE_DIGEST/FULL_ARTIFACT_DIGEST use
raw bytes and the latter remains external. Core registries/scopes are untouched.

Semantic identity uses the exact H5 closed projection implemented in records:
fixed family/profile/protocol/contract/policy/class; request/catalogue/descriptor/
authority/constants/resource/build/payload digests; provider binding, comparison
evidence, qualifications and assurance. Metadata, attempt/completion, detailed
execution observations and the semantic digest itself are excluded. Display
relocation changes full bytes without changing scientific semantic identity.

Hash dependency order is acyclic: source/report hashes and opaque manifest leaves;
authority/constants/build/resource policy; descriptors/catalogue; request/payload;
local observations/evidence; semantic projection and complete artifact. Basis
digest excludes itself, request digest excludes itself, descriptors never refer
back to catalogue, evidence never refers to completion, and the full artifact hash
is never embedded. Golden vectors exercise all fourteen scopes and fixed claims.

Fresh-process import auditing proves the exact generic Core closure is limited to
its package initializer, envelope, codec, errors, schema and digests. Historical
code does not import Core requests/results/providers or any scientific module.
Cross-family tests import Core owners separately to prove rejection in both import
orders. Core's entire existing compatibility suite runs unchanged in its own lane.
No public envelope dispatcher or UI integration is required or supplied in H6A.
