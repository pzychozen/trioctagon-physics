# Execution and reproduction record

**15 November 2026 · NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01**

All work was performed in the fresh external directory `C:/TORMENT/NRD01/run_20261115_01`. The canonical physics checkout was read only. No application testing was necessary for this analytical order, and no TORMENT production directory was accessed.

## Actual environment

Python was invoked from **Windows Command Prompt**, using the task's `run_python.cmd`, whose first action is `call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment`. The active executable was `C:/Users/Notandi/miniconda3/envs/torment/python.exe`, Python 3.11.15, with SymPy 1.14.0. UTF-8 and no-bytecode settings were applied only to the task process; `GIT_OPTIONAL_LOCKS=0` prevented optional index refresh. No package installation, dependency update, environment modification or global Git setting was made.

`records/ENVIRONMENT.json` records the actual interpreter, platform, Conda prefix and timestamp. PowerShell was used for initial file inventory, safe ZIP extraction, text reading and copying task-owned output files; it was not used to bypass the requested Conda environment for Python.

## Commands and order

The initial ZIP was opened using the Windows .NET ZIP API, its member destinations checked to remain within the fresh task `packet/` directory, and extracted there. Subsequent Python audit independently checked all member bytes, names, supplied manifest entries and source identities. The following commands were executed through the Conda-activating `.cmd` wrapper, from the external task root:

```bat
run_python.cmd audit.py prepare
run_python.cmd audit.py before
run_python.cmd source_gate.py
run_python.cmd run_exact.py
run_python.cmd finalize.py
run_python.cmd review\checks\run_exact.py review\checks
run_python.cmd source_gate.py
run_python.cmd audit.py after
run_python.cmd package_review.py
```

The source gate was additionally rerun while refining bounded search filtering. Exact `rg` argument arrays, output counts and raw-output fingerprints are in `records/SEARCH_LOG.json`. The initial broad cycle/rate patterns also matched the substring “rate” in “separate”; word boundaries corrected that irrelevant noise. Only relevant deduplicated source excerpts are distributed. Search outputs are source-navigation evidence, not exhaustive novelty certificates.

The first source-gate invocation failed because `docs/RESEARCH_INDEX.md` did not exist as a Git blob at the pinned checkpoint. The actual local index was recovered and explicitly inventoried as a local file. The first resource-runner invocation failed at import because psutil was absent; no symbolic child had started. The runner was replaced with standard-library ctypes calls to Windows `GetProcessMemoryInfo`, with no installation. `records/RECOVERED_FAILURES.json` preserves both failures and their resolutions.

After the monitor recovery, the exact symbolic worker completed successfully. Its source and outputs are retained under `checks/initial_completed/`. The output paths were then made portable, and the final delivered standalone runner/checker were executed once more, successfully. The same 60 distinct predicates passed; this is not reported as 120 results. `checks/RUN_RECORD.json` binds the final worker/runner source hashes and records actual time and peak observed working set. The 300-second wall limit and 768 MiB process working-set limit were enforced by the parent process. There were no aborted, inconclusive or failed mathematical checks. The negative controls pass by detecting a deliberately false identity.

## Reproduce only the new exact algebra

Extract the review ZIP, open Command Prompt in its root, then run:

```bat
conda activate torment
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
python -B checks\run_exact.py checks\recheck
```

The standalone Windows runner writes fresh results into `checks/recheck/`, preserving the reviewed outputs. It needs only Python, SymPy and the Windows process-memory API. `checks/exact_check.py` is also readable without execution. The `execution/` orchestration files are historical task-specific provenance with absolute original locators; they are not needed for algebra reproduction and should not be run as a general installer. The original initial-run runner imports the task audit module; the final portable runner does not.

The new checker reconstructs the response from the Cartesian derivative, performs exact rational polynomial division and coefficient matching, proves the pair-difference identities, checks orientations and step powers, and rejects stage reversal. It uses the **same SymPy arithmetic backend as the proposal**, though a separately written algebraic organization. No claim of independent arithmetic implementation is made. Its generic symbolic radius variables are algebraic indeterminates, not numerical native-branch fixtures.

D1's border, branch framework and rate coefficient are inherited from the preserved accepted texts. There is no full D1 state-jet solve, finite-root check, continuation tube, native trajectory, historical verifier, spectral scan, broad survey or radius optimization. The qualitative common-neighborhood, divisibility and positivity claims are proved in `PROOF_REPORT.md`; a finite identity list is not a substitute for them.

## Preservation and packaging

The before/after repository snapshots compare HEAD, branch, refs, local configuration, raw index, staged and unstaged differences, status, and SHA-256 identities of **31,508 modified or untracked files**. Raw unrelated file inventories remain private outside the review ZIP; the distributed records retain their digest, count and comparison result. Tracked content changes are also covered by the unchanged staged/unstaged differences. Ignored files and global filesystem metadata are not claimed as a complete machine snapshot. Consumed local source files are separately checked at closeout.

The incoming ZIP is preserved unchanged under `incoming/`. Its 32 members, 31 self-excluding manifest entries and 18 source records were verified. All 13 records with canonical repository paths were matched against **local** Git objects at `ae2c02c80c49dfcf266d3b27ebd21be76a938de1`; this is not a fresh GitHub-byte audit. The other source identities are authenticated packet-member identities, not invented remote checks. The 11 additional later/navigation files are individually inventoried by origin.

`MANIFEST.json` excludes itself and identifies every other delivered file by raw size and SHA-256. The external ZIP sidecar authenticates the finished archive. The final audit reopens every member, checks exact manifest membership, safe case-unique paths, CRC, byte length and SHA-256, then verifies the unchanged nested incoming packet and all consumed sources. Hashes authenticate bytes, not mathematical truth. No PDF, figure or manuscript was generated; no repository write, commit, push or publication occurred.
