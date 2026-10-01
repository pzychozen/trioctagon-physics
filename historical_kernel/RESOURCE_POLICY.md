# Measured local policy

No operational budgets are hardcoded into the scientific wheel. An external,
trusted, byte-pinned admission specifies the limits for its exact installation.

The measurement matrix is N=0,1,2,64 for all three profiles and all three readouts.
N=256 and N=1024 are attempted only after the earlier matrix leaves sufficient
temporary-envelope headroom. Bounded step, staged, EMA and chart operations are
also measured, with zero, tiny and extreme-finite inputs. Numerical refusal is
retained as failure, never shortened success. Negative-test measurements cover
malformed/oversized input, memory, wall, output and manifest exhaustion, concurrent
requests, cancellation, result binding, tampering and publication failure.

The initial Windows pilot stopped at its expansion guard: NumPy import dominated
the conservative resident-plus-private memory metric. The measured 36-cell maximum
was 932,995,072 bytes; an isolated NumPy import probe measured 866,676,736 bytes.
The temporary measurement envelope was therefore expanded to 4 GiB, still with
one request at a time and a one-quarter-envelope escalation gate. This does not
change mathematics or constitute a selected operational budget.

Each final measurement records canonical request/payload/evidence/full-artifact
bytes, depth, monotonic end-to-end wall time, combined worker/launcher memory,
startup, both installation scans, and serialization/binding cost. Intermediate
pilot measurements are not substituted for exact-candidate certification.

The selection table retained in `measurement-manifest.json` records observed
maximum, selected limit, exact ratio and reason for every field:

| Field | Selection rule |
|---|---|
| max_updates | 1024 only after the complete matrix passes; no extrapolation |
| input_bytes | 4x maximum, round up to KiB |
| output_bytes | 4x largest complete artifact, round up to MiB |
| json_depth | measured maximum plus four containers |
| wall_milliseconds | 4x slowest observation, round up to seconds |
| memory_bytes | 2x conservative peak, round up to 64 MiB |
| diagnostic_bytes | 4x longest observed failure diagnostic, round up to 32 bytes |
| manifest_bytes | 4x largest embedded build/evidence object, round up to 4 KiB |

These margins cover bounded fixed-schema variation, cold startup and serialization
variation for this local inspection workload. A slower machine can refuse a request;
the policy is not a promise that every finite input succeeds. Numerical domain checks
remain independent. The issuer enforces caps before publication, and the final
admitted smoke proof rechecks the largest selected run. Local filesystem calls and
unprotected observations do not establish a hard real-time or B2 execution guarantee.
