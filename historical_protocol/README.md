# Historical analysis protocol 0.1.0

`trioctagon-historical-protocol` is the H6A pure protocol distribution. Its import
package is `trioctagon_historical_protocol`. It depends on `trioctagon-analysis==0.1.1`
only for unchanged generic canonical codec, validation and digest infrastructure.
Supported interpreter: CPython 3.11.

This package parses and serializes immutable Historical claims. It supplies the
five closed payload owners, request/result/receipt/catalogue schemas, frozen
authority and literal constants, and inert resource-policy/provider-build types.
It contains no scientific kernel, computation dispatcher, success issuer,
coordinator, build admission or runtime provider allowlist. There is no application
command or Historical run endpoint in H6A.

The only result issuance-class literal is
`UNATTESTED_HISTORICAL_RECONSTRUCTION`. Parsing it does not issue a result from
computation, prove equations, authenticate a producer, or approve a build. Reading
`LOCAL_CHECK_PASSED` checks consistency of the stored claim; it does not perform
the claimed installation scan. Producer execution attestation remains UNAVAILABLE,
Windows execution binding NOT_PROVEN, and production attestation disabled.

The default resource policy remains MEASUREMENT_REQUIRED_BEFORE_ADMISSION with
null manifest and null limits. No real catalogue or provider build is admitted.
Future Historical mathematics must be independently implemented from the frozen
historical authority. Current scientific functions and `kernel_TO` are not runtime
dependencies. Current-kernel identities appear only as comparison references.

An inert reader supplies its own finite parsing limits:

```python
from trioctagon_historical_protocol.codec import ParseLimits
from trioctagon_historical_protocol.records import DerivedRecord

# Caller chooses max_bytes/max_depth for its reading context; these are not
# computation-admission limits. raw is already acquired artifact bytes.
record = DerivedRecord.from_bytes(raw, ParseLimits(max_bytes, max_depth))
detached_data = record.to_dict()
```

`Request.validate_context` checks identity consistency with caller-provided schema
objects. It does not trust or locally admit those objects. Receipt context can be
checked the same way when the request is nonnull. No artifact can authorize its
own execution. Source locators are display strings and are never opened.

See [SPECIFICATION.md](SPECIFICATION.md) for the H5 bindings and
[CONFORMANCE.md](CONFORMANCE.md) for test scope and the full N01–N40 disposition.
All complete claims in `tests/fixtures/TEST_ONLY_*` are synthetic. None of those
fixtures, tests or certification tools is installed in the runtime wheel.

From the repository directory in an activated `torment` Command Prompt, the
Windows certification command is:

```bat
python -I -B historical_protocol\tools\certify_distribution.py --source . --workspace C:\path\to\new-external-certification-directory
```

The workspace must be new and outside the checkout. Use `--precommit` only for a
local candidate; CI certifies committed inputs. Certification acquires hashed
tooling and the existing exactly pinned Core test artifact, then builds/tests
offline in isolated external virtual environments. It runs the complete existing
Core analysis suite unchanged. Existing disabled B2 prototype regression tests do
not constitute a new B2 proof. Dedicated CI retains both exact wheels, input/member
manifests and test evidence. No release or tag is produced.
