# Inert test fixtures

`axial_export_cache.json` is the byte-preserved explicit-input snapshot created
with the certified UI 0.2.0 / kernel K during the 2026-10-05 external export-access
investigation (`harmless-cache.axial.json`). SHA-256:
`96025b48de29f13b6577551a476542a9baaf44078405f1096ff170eb73c3b420`.
It is an unauthenticated saved observation, used only to exercise export of a
retained cache without scientific recomputation. It is not the user's affected
file and is not packaged in the UI wheel. Its scientific authority is unchanged.

`axial_old_run.json` is a byte-preserved copy of the K-G0 `kernel_physics/tests/fixtures/axial_v1/old_run.json` fixture at certified kernel commit `3f42d4e56afd973c397ce4c557b66183a71a6044`. It tests passive observation of an older record while preserving strict cross-implementation resume refusal. It is not packaged in the UI wheel.

Synthetic TEST_ONLY claims from the approved analysis codec. Recorded VERIFIED vectors are mock claims, never evidence of production attestation. The fixture parent is intentionally absent from the UI session. `derived.json` stores all 16 APP04 fields (20 numeric leaves); `subset.json` stores an ordered subset, including signed zero and small signed residuals. No fixture is packaged in the UI wheel.
