# Review entry point — NATIVE_CAPACITY_RECEIVING_RECOVERY_01

Disposition from this independent investigation: **established unchanged**, awaiting GPT review.

1. Read NATIVE_CAPACITY_RECEIVING_RECOVERY_01_PROOF.md. It states all hypotheses and quantifiers, proves the same-trajectory receiving/recovery certificate and states its interpretation limits.
2. Read NATIVE_CAPACITY_RECEIVING_RECOVERY_01_CLAIM_SOURCE_LEDGER.md and CLAIM_CROSSWALK.json for PR01–PR23 coverage, exact published source labels and artifact bindings.
3. Inspect exact_checks.py, EXACT_ALGEBRA_RESULTS.json and EXACT_CHECK_EXECUTION.json. The 14 groups are finite exact checks; the functional-analytic proof is supplied in prose.
4. Inspect INPUT_VERIFICATION.json, SOURCE_IDENTITIES.json, INPUT_BASELINE.json, INPUT_PRESERVATION.json and DOCUMENT_CHECKS.json for the explicitly bounded identity/preservation checks.
5. Read COMPLETION_REPORT.md for the outcome and stopping point. All exact compact supplied inputs are under inputs/, including the issued work order, source assessment, P1–P4 sources, accepted prior review records and current continuity.

The archive's PACKAGE_MANIFEST.json lists every other file by exact size and SHA-256. The final ZIP's adjacent checksum and post-write verification receipt are external by design; including a final archive hash inside itself would create a circular identity requirement.

The independently written algebra can be replayed with Python and SymPy, directing results to a separate scratch directory:

    python -I -B exact_checks.py --output-dir PATH_TO_SEPARATE_SCRATCH_DIRECTORY

Compare the scientific group payloads; runtime metadata legitimately changes between executions. Do not count replayed groups as additional independent discoveries. No numerical integration, parameter scan or source script is needed.

Do not execute inputs/preparation/check_route.py or inherited scientific suites as part of this packet verification. They are retained as original formulation/history, not represented as new independent checks. audit_and_package.py records this delivery's local bounded verification and packaging procedure; it uses the original Windows input paths and is not a portable mathematical prerequisite.

No manuscript or publication is included or authorized. The accepted publications and historical records retain their original bytes and status. Stop after reviewing this investigation; further research requires a separate order.
