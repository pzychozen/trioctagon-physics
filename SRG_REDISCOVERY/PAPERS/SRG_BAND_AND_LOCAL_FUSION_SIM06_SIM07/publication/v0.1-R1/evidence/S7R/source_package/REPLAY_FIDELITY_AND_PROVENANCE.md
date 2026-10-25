# Replay fidelity and provenance

**REPRODUCED · SRG_SIM07_UNIVERSE_REPLAY_01 · 25 October 2026**

Both prescribed executions completed and passed strict recording fidelity. The historical aggregate comparison passed its separately frozen criteria. No tolerance was used for reference/capture state, RNG or metric identity.

## Authority, inputs and extraction

The current [work order](handoff/CODEX_SIM07_UNIVERSE_REPLAY_01_WORK_ORDER.md) and [frozen specification](handoff/RUN_SPECIFICATION.json) authorize this bounded replay. The earlier [acceptance](handoff/context/GPT_ACCEPTANCE_RECEIPT.json) accepts construction and original aggregates; its proposal-era zero-run boundary remains unchanged in its archived context. It was not silently rewritten. See [context index](CONTEXT_INDEX.md).

| Immutable input | Bytes | SHA-256 |
|---|---:|---|
| [Original source](handoff/originals/srg_condensate_breaking.py) | 30,165 | `a645a3bb564a2cae5e2b3ac3744f3f34f559a67132f255b3b0a97d277e68beb5` |
| [Historical full_universe.csv](handoff/originals/full_universe.csv) | 45,093 | `f58acaf40d5bf2eae0110499c5291cea6227a70b2260386db2823821d79c1c50` |
| [Accepted SIM07 archive](handoff/inputs/SIM07_UNIVERSE_GPT_REVIEW_AND_ACCEPTANCE.zip) | 1,199,866 | `f9fc96200aba6056a8a3df82341159deff9f9031ee40eec62e21ae5b0b21635c` |

All 14 payloads listed by the handoff manifest matched. Its seven convenience copies matched the corresponding accepted-archive members; the nested original construction submission matched its recorded identity. The supplied original bytes were sufficient; no recovery search or unrelated archive inventory was required.

The [reference core](methods/reference_core.py) contains only original lines 42–54, 60–266 and 663–758: H, signed RPCO, sampled H_MAX, PHI, the complete class including original observer, and `experiment_full_universe`. Necessary NumPy/pandas/distance imports are supplied. The runner supplies a run-local OUTPUT_DIR. The complete original module, main block, four other drivers and old build/check helpers were not imported or executed. Original source copies are unchanged.

`prepare.py` checked interval text and AST identity of the original definitions before initialization. The sampled H_MAX expression remains exactly as written; it is evaluated when loading the isolated definitions, without a constructor or random call. The exp/log compressor, reductions, NumPy legacy random interface, sorting and fusion loop remain unchanged. See [extraction verification](EXTRACTION_VERIFICATION.json), [preflight](PREFLIGHT.json), and [instrumentation diff](methods/CAPTURE_HOOKS.diff).

## How recording was made nonintrusive

The reference wraps the unchanged `evolve`/`evolve_pass` methods only to record boundary 0, step entries, completed boundary copies and original metrics. It invokes each original method once. The capture uses the same boundary wrapper plus copy-only hooks at documented original source lines. Removing those `REC.*` statements recovers the reference text and AST exactly.

[recorder.py](methods/recorder.py) observes the original `seed`, `normal`, `uniform` and `choice` calls. Each wrapper invokes the original function once, copies its actual returned object and RNG checkpoints, then returns that same object unchanged. No RNG is restored. For capture fusion, a guarded wrapper observes the actual coordinates and weights passed to the original `np.average` call, before calling that operation once. It never returns a substituted center. All retained arrays are copies, not views that can mutate later. Compression flags are passive comparisons from the actual pre-compression Q and selected L; they do not steer the compressor.

The identical reference/capture outcome is an observed check of noninterference here. It is not a general proof about every possible instrumentation or platform. Text/AST inspection, actual operands, independent record readback and complete RNG records provide separate evidence.

## Initialization retained the discarded draws

Both isolated processes executed the original selected driver once:

1. `np.random.seed(1618)`.
2. Six `(20,3)` Gaussian draws, standard deviation 1.5, around the ordered centers `(8,0,0)`, `(-8,0,0)`, `(0,8,0)`, `(0,-8,0)`, `(0,0,8)`, `(0,0,-8)`, followed by vstack.
3. The N=120 constructor with horizon 6, multi_freq=True, breathing=True, seed=None: uniform X, uniform R, then independent frequency choice. The constructor's X/R are subsequently replaced but their random consumption is retained and their arrays are saved.
4. Install the stacked Gaussian positions; draw replacement uniform R in [0,.3). Save boundary 0 with original zero V, pass 0 and empty history.
5. Execute the original `field.evolve(200)` and preserve its endpoint report and CSV export.

Actual frequency counts, in sorted order, are **29, 36, 28, 27** for approximately .1508002933, .244, .3948002933 and .6388002933. Each population contains all four here, but no balancing was imposed. All per-population counts are in [motion summary](analysis/MOTION_SUMMARY.json).

Each run has 211 recorded random-interface calls: one seed call, ten value-producing initialization calls and 200 noise-return calls. This counts distribution/API calls, not underlying generator words. Before/after checkpoints include all MT19937 words, generator name, position, Gaussian-cache flag and cached float bits. The arbitrary process state before seed is retained but excluded from equality; every deterministic checkpoint beginning after seed agrees. Initialization arrays and call ordering are preserved under [reference random records](runs/A_REFERENCE/random/) and [capture random records](runs/B_CAPTURE/random/).

## Actual environment and budget

Python and all scientific utilities ran through Windows Command Prompt with the existing `torment` environment. No dependency was installed or changed. [ENVIRONMENT.json](ENVIRONMENT.json) records the full Python/platform/build information: NumPy **2.4.4**, pandas **3.0.3**, SciPy **1.17.1**, Matplotlib **3.10.9**. These are this replay's dependencies; the original historical environment is unknown.

| Execution | UTC window on 25 October | PID | Initializations | Attempted/completed updates | Exit |
|---|---|---:|---:|---:|---:|
| A_REFERENCE | 10:07:29–10:07:40 | 30012 | 1 | 200 / 200 | 0 |
| B_CAPTURE | 10:07:51–10:08:02 | 3312 | 1 | 200 / 200 | 0 |
| Total | | | **2** | **400 / 400** | |

The [durable ledger](CALL_BUDGET.jsonl) writes initialization and step entry before execution and completion after recording, flushing and syncing every event. [Reference process receipt](PROCESS_A_REFERENCE.json), [capture process receipt](PROCESS_B_CAPTURE.json) and run receipts retain full command, PID, timestamps and status. The second run was launched only after successful reference completion. There were no smoke updates, warm-ups, retries, restarts or partial calls. Both driver endpoint printouts are retained: [reference stdout](A_REFERENCE_STDOUT.txt), [capture stdout](B_CAPTURE_STDOUT.txt). Stderr is empty in both.

## Strict recording-fidelity outcome

[FIDELITY_VERIFICATION.json](analysis/FIDELITY_VERIFICATION.json) reports PASS with no discrepancy:

- 201 contiguous boundaries per run, 120 unique stable IDs each: 24,120 point-state rows per run.
- Every X/R/V/frequency/configuration/pass array matches in dtype, shape and raw bytes, including signed zeros. All states are finite and frequencies/configuration remain fixed.
- Every completed displacement matches `X[p]−X[p−1]` exactly, and boundary-0 V is zero.
- All original metric keys/order, integer values and floating bit patterns agree over 200 rows; `metrics.npz` and row-level JSON readback both confirm this. The two exported CSV byte streams are identical.
- The entire deterministic RNG checkpoint sequence and all actual returned arrays agree. Initialization mapping and boundary/noise checkpoint continuity pass.
- Capture has 200 incoming graphs, 24,000 ascending fusion row visits, all actual stage operands, actual noise arrays and original observer memberships/linkages.
- Passive bookkeeping confirms incoming/completed state identities, selected IDs, actual Q weights and each read's identity with the earlier row's saved post-write coordinate or later row's Y coordinate. The stored noise exactly produces the recorded position increment from Z.

An additional [passive observer readback](analysis/SUPPLEMENTAL_READBACK.json) recalculates 12 existing aggregate quantities from saved states, yielding exact binary agreement for 2,400 cells. It does not call the engine, rerun clustering, re-draw noise or propagate any trajectory. The source's actual spatial memberships are used directly.

## Separate historical comparison

The original and reproduced tables both have the exact expected 15-column order, 200 rows and pass labels 1–200. No initial-state observer row was inserted. Four integer-valued columns comprise **800 cells**, of which 200 are pass labels and 600 are scientific metrics; all match exactly. Eleven continuous columns comprise **2,200 cells**, all satisfying

`abs(replay − historical) <= 1e−12 + 1e−10 * abs(historical)`.

There are **3,000 total cells and 2,800 non-pass metric cells**. Exact parsed equality is 2,312 total cells: 800 integer cells plus 1,512 continuous cells. The other 688 continuous cells are near-equal, not exact. No missing/nonfinite cell occurs. Maximum absolute discrepancy is 1.7763568394002505e−15 in entropy (first maximum at pass 13); column-specific maximum relative errors and worst passes are in the [comparison table](HISTORICAL_COMPARISON_TABLE.md), [column summary](analysis/HISTORICAL_COLUMN_SUMMARY.json), and [full cell-level result](analysis/HISTORICAL_COMPARISON.json). At historical zero, relative error is defined as 0 if both are zero, otherwise null with the absolute discrepancy retained. The observed historical columns contain no problematic zero denominator.

The historical CSV bytes and replay CSV bytes differ. Float parsing uses Python's CSV reader and `float`; exact equality and the declared near-equality criterion are reported separately from serialization. The original environment was not recovered and no cause for each last-bit difference is asserted. **Complete aggregate acceptance does not identify these new coordinates with an unavailable historical trajectory.** All new movement evidence remains REPRODUCED.
