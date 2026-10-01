# Independent Historical TORMENT kernel

`trioctagon-historical-kernel` 0.1.0 owns the H4/H5 Historical mathematical
reference implementation. It is independent of current `kernel_physics`, archived
`kernel_TO` and production TORMENT. Supported certification target is Windows x64,
CPython 3.11, NumPy 2.4.4, and the exact accepted Historical protocol 0.1.0 wheel.

Pure scientific modules have no protocol dependency. `api` exports explicit
Historical `Triad`, `Clock`, `Memory`, `KProfile`, `Readout` and five mathematical
operations. State is raw and immutable. The only k values, phase strength, harmonic,
clock progression and readout coefficients are the frozen Historical literals.

```python
from trioctagon_historical_kernel.api import Triad, KProfile, Readout, step, run

initial = Triad((.2+.3j, -.4+.1j, .1-.2j))
updated = step(initial, KProfile.SCALED)
history = run(initial, KProfile.SCALED, 2, Readout.STAGED)
```

The protocol adapter constructs only H6A payloads. The separate local issuer
requires an explicitly pinned external admission bundle. No admission catalogue,
provider build, measured policy or allowlist is embedded in this wheel. Importing
the package never admits an execution or starts a service. There is no UI change.

The local issuer runs one isolated worker at a time, assigns a Windows memory Job
before the computation handshake, observes process memory/wall use, validates the
complete canonical candidate and publishes its name without replacement. Failed,
cancelled or incomplete attempts return only bounded Historical receipts. Windows
resource limits are not B2 protection or execution attestation.

Results retain UNATTESTED_HISTORICAL_RECONSTRUCTION, producer attestation
UNAVAILABLE, Windows execution binding NOT_PROVEN and production attestation
disabled. Actual unprotected before/after installed-byte checks do not identify
loaded instructions. B2 and P2 remain separate.

See the specification and certification evidence for numerical conventions,
frozen-fixture coverage, runtime acceptance, measurement policy and exact local
admission identities. Test-only pins and example claims are not real admission.
