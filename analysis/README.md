# Detached analysis protocol — Stage B1

`trioctagon-analysis` 0.1.0 is a separate headless distribution. It implements
protocol v1, strict immutable catalogue/request/derived-record/attempt codecs,
scoped digests, and the bounded APP04 **recorded-data copy** provider.

**The production verified execution lane is closed.** The coordinator always
returns an AttemptReceipt. B1 does not deploy an approval root, establish a
protected Windows execution snapshot, attest actual imports, enable a UI action,
or recompute science. B2 requires separate review and implementation.

## What is available

- `ParentSnapshot` validates retained bytes using only
  `kernel_physics.api.RunRecord.from_json` and binds original bytes, complete
  canonical bytes and the native semantic digest separately.
- `copy_recorded` returns an **unattested CopyPayload**, preserving selected
  canonical tokens. It never issues a successful analysis record.
- `DerivedAnalysisRecord` is a strict **inert claim codec**. Constructing or
  loading a syntactically consistent evidence claim does not verify it.
  `verify_parent_copy` checks copied tokens against an available immutable parent;
  it still does not attest the historical producer.
- `attempt_inspection` has no injectable attestor, developer bypass or successful
  record return. Even fully populated approval data ends in a B1 refusal.
- `persist_record` stores an existing inert record claim as one content-addressed
  file on qualified local Windows NTFS. Persistence is not scientific execution
  or evidence authentication.

No Historical or Experimental-analysis profile is implemented.
`TRIOCTAGON_EXPERIMENTAL_RECORD` is reserved only. Legacy UI caches and sidecars
are unchanged and are not new analysis records.

## Installation and tests

The protocol/data modules have no third-party runtime dependency and import no
kernel or UI at startup. The copy provider needs an explicitly selected compatible
Core installation/source available in the caller's environment. This distribution
does **not** resolve or install an arbitrary kernel from a registry.

From the repository root in Command Prompt:

~~~bat
conda activate torment
python -B -m pytest analysis/tests -p no:cacheprovider
~~~

The test suite's source-path setting loads `analysis/src`. From this checkout,
`python -m pytest` also has the repository on its import path for public Core
loading. Installed-package validation must instead explicitly select the kernel
installation under test; it must not infer producer identity from the checkout.

Build with the existing locked Setuptools 81.0.0 / wheel 0.47.0 tooling. Build
from an external copy of `analysis/` when preserving checkout cleanliness, since
Setuptools may create build/egg-info working files. The wheel contains only
`trioctagon_analysis`, installed specifications/golden vectors, and distribution
metadata/licenses. Tests, fixture
records and mock attestation are not runtime package members.

[Specification](SPECIFICATION.md) defines the exact codec, digest and trust
contracts. [Conformance map](CONFORMANCE.md) distinguishes B1 checks from
unimplemented B2 enforcement. [Resource proposal](RESOURCE_LIMIT_PROPOSAL.md)
is measured planning evidence, **not an approved production policy**.

Scientific research, simulation, replay, recomputation, release publication and
Core/UI changes remain outside scope. The B2A addition below is disabled proof
infrastructure only; further execution/activation needs separate authorization.

## B2A proof addendum

[B2A Windows proof](B2A_WINDOWS_PROOF.md) adds a separate refusal-only proof
harness. Its current outcome is **NOT_PROVEN**: unapproved AVG native startup
injection prevents the closed execution path from reaching the provider.
[B2A conformance/resource review](B2A_CONFORMANCE.md) distinguishes the real
refusal from unverified OS/resource controls. The B1 codecs and normal
coordinator remain unchanged; no production activation or B2B is implemented.

The preserved disposition is:

~~~text
B1 = PASS
B2A_PROOF_HARNESS = PRESERVE
WINDOWS_EXECUTION_BINDING = NOT_PROVEN
B2A-R1 = BLOCKED_ENVIRONMENT_NOT_AVAILABLE
PRODUCTION_ATTESTATION_ENABLED = NO
READY_FOR_B2B = NO
~~~

The strict gate refused unapproved `C:\Program Files\AVG\Antivirus\snxhk.dll`
before provider execution. This is not a maliciousness claim or an approval of
AVG. R1 identified no usable disposable Windows guest and launched no proof job.

### Preservation classification

Paths below are relative to `analysis/`. These classifications describe reusable
source/specifications; external evidence, machine inventories, runtime downloads,
candidate archives and temporary snapshots are not repository artifacts.

| Artifact | Classification |
|---|---|
| `README.md` | SPECIFICATION |
| `pyproject.toml` | PROOF_INFRASTRUCTURE |
| `B2A_WINDOWS_PROOF.md` | SPECIFICATION |
| `B2A_CONFORMANCE.md` | SPECIFICATION |
| `src/trioctagon_analysis/b2a_snapshot.py` | PROOF_INFRASTRUCTURE |
| `src/trioctagon_analysis/b2a_windows.py` | WINDOWS_ATTESTATION_PROTOTYPE |
| `src/trioctagon_analysis/b2a_worker.py` | PROOF_INFRASTRUCTURE |
| `src/trioctagon_analysis/b2a_proof.py` | EVIDENCE_ONLY_COORDINATOR |
| `tests/test_b2a.py` | TEST_SUPPORT |

No production attestor is implemented. The normal coordinator always refuses
verified issuance, while the proof coordinator only returns non-production
evidence with binding NOT_PROVEN. Failed or incomplete attestation has no fallback
to ordinary APP04 issuance. The inert claim codec remains distinct from actual
producer attestation. Preservation does not resume proof execution or authorize UI
work, APP04 recomputation, Historical providers or Research Lab engines.
