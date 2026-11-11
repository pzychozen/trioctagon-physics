# NATIVE_TURNING_CAPTURE_01 review return

Read `RESULT_SUMMARY.md`, then `NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md`. The source-by-source gate is `PRIOR_WORK_COMPARISON.md`; per-claim status and exact locators are in `CLAIM_LEDGER.json`. Original packet files and reference sources remain unchanged under `received/`, `packet/` and `sources/`.

The primary result is certified entry of the original exact seed at update 50. It is a new investigative result returned for review, not a publication or a declaration of external acceptance. No new manuscript is included.

## Checking without generating another trajectory

From **Windows Command Prompt**, activate the user's existing environment and change to an extracted copy of this run:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
cd /d C:\path\to\extracted\review
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
python -B scripts\check_certificate.py
python -B scripts\check_certificate.py negative-controls
```

The checker uses only the standard library and the archived `data/CERTIFICATE.json`. Run it without Python's `-O` option: its exact validation predicates use assertions. It never imports the generator, native module or historical arithmetic scripts. The first command verifies 50 linked enclosures, all positive prestages, early turning and terminal membership; the second checks five deliberately invalid certificates. Neither is another native parameter/seed search. These commands rewrite their result JSON in the extracted copy, so the preserved delivered hashes describe the original execution.

## Generation and historical commands

`scripts/explore.py` documents the one-seed numerical target selection; `scripts/generate_certificate.py` reconstructs the connected dyadic certificate from the exact seed, using only the archived numerical choice of N and rational terminal direction. `scripts/prepare.py` records how source preservation was performed at the original absolute paths; it is provenance, not a portable replay prerequisite. Historical source scripts under `sources/` and `packet/inputs/reference/` were read, not executed.

At the original run path, `run_python.cmd scripts\execute.py scripts\check_certificate.py` activates torment in Command Prompt, runs the checker, and records measured start/end times, script hashes, exit status and stdout/stderr paths. The original wrapper intentionally records its original absolute working directory. Use the commands above for a relocated extracted copy.

`logs/INITIAL_EXECUTIONS.json` distinguishes the initial tool-observed commands from later executions recorded automatically by `scripts/execute.py`. Exact scientific data are under `data/`. `logs/PRESERVATION_AUDIT.json` verifies unchanged inputs and read-only sources at closeout. No environment package was installed.

## Archive integrity

`REVIEW_MANIFEST.json` hashes all review members other than itself. `DELIVERY_AUDIT.json` records an actual preliminary archive reopening and byte/hash verification of every payload member; it excludes itself and the subsequently created final manifest to avoid circular hashes. The external `NATIVE_TURNING_CAPTURE_01_FINAL_DELIVERY_AUDIT.json` records a second reopening and verification of **every member of the final ZIP**, including those two records, and the final archive SHA-256. The `.zip.sha256` sidecar independently supplies the final archive hash. Packaging checks are not scientific theorem counts.
