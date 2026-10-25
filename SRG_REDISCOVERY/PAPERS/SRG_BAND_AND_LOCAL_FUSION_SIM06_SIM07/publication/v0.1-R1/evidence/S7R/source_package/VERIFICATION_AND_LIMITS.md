# Verification and limits

**Completed bounded replay; returned for GPT and Hilmir review. No further scientific execution authorized here.**

## Gates and evidence

| Gate | Result | Evidence |
|---|---|---|
| Original and accepted-package identities | PASS | [Extraction/input verification](EXTRACTION_VERIFICATION.json), [handoff manifest](handoff/HANDOFF_MANIFEST.json), [intake receipt](INTAKE_RECEIPT.json) |
| Source extraction and capture hook removal | Exact original definition AST; exact reference recovery after hook removal | [Reference](methods/reference_core.py), [capture](methods/capture_core.py), [diff](methods/CAPTURE_HOOKS.diff), [preflight](PREFLIGHT.json) |
| Required dependencies before initialization | Present in existing torment; no environment changes | [Environment](ENVIRONMENT.json) |
| Execution budget | 2 initializations, 400 attempted/completed updates, no failures/retries | [Durable ledger](CALL_BUDGET.jsonl), [A process](PROCESS_A_REFERENCE.json), [B process](PROCESS_B_CAPTURE.json) |
| Reference/capture fidelity | PASS; no discrepancy | [Full fidelity result](analysis/FIDELITY_VERIFICATION.json) |
| Historical aggregates | All 3,000 cells satisfy frozen criteria; 2,312 exactly equal after parsing | [Full comparison](analysis/HISTORICAL_COMPARISON.json), [readable per-column table](HISTORICAL_COMPARISON_TABLE.md) |
| Independent passive aggregate readback | 2,400 cells / 12 quantities exactly agree from stored states | [Readback](analysis/SUPPLEMENTAL_READBACK.json), [cell results](analysis/observer_readback.csv) |
| Captured stage consistency | Incoming/completed identities, noise, weights, ascending visits and earlier/later reads pass | [Fidelity result](analysis/FIDELITY_VERIFICATION.json), [actual-read accounting](analysis/ordered_read_accounting.csv) |
| Visual inspection | Six final figures inspected; no blocking layout or evidence-label issue | [Figure register](FIGURE_REGISTER.json), [visual receipt](VISUAL_INSPECTION.json) |
| Protected material | Exact before/after fileset and byte preservation | [Baseline](INPUT_BASELINE.json), [preservation receipt](PRESERVATION_RECEIPT.json) |
| Packaging | Exact payload sizes/hashes and fresh ZIP-member readback | [Payload manifest](MANIFEST.json); external ZIP identity supplied beside archive |

Low-level checks are bookkeeping, not independent experiments. The two complete runs are recordings of one configuration for fidelity, not a statistical sample or independent validation of the model.

## Reproducible inspection without another run

All methods are inside [methods](methods/). The sequence used was passive intake, passive extraction/environment check, static preflight, one reference launch, one capture launch, passive verification, passive analyses, rendering, written review and final preservation/package verification. [ACTION_RECORD.md](ACTION_RECORD.md) records corrections confined to passive metadata/presentation. No failed scientific attempt was discarded.

Use the [schema](RECORD_SCHEMA.md) to read NPZ files with `allow_pickle=False`. The passive `verify_records.py` compares saved records and frozen original CSV. `analyze_records.py` computes geometry and graph descriptions from saved values; `supplemental_readback.py` computes source observer quantities from saved states and aligns same-boundary memberships. `render_figures.py` plots records only, with no advancing callbacks. The historical comparison uses exactly the handoff's formula and denominators, without changing a tolerance after seeing results.

`launch_run.py` and `run_once.py` are supplied to make the performed method reviewable. **Do not rerun them:** the scientific budget is consumed. They refuse an existing process receipt or prior initialization attempt. Further execution would require a separate decision, not interpretation of included code as fresh authority.

All actual random return arrays and complete RNG states are retained. There was no independent RNG regeneration or restorative replay to repair missing evidence. There was no missing capture requiring a third run. Files are divided into immutable handoff inputs, execution methods/receipts, complete run records, passive analyses, and static figures with plotted-data references. Temporary Matplotlib cache files are excluded from the ZIP, explicitly listed as exclusions; they are not scientific inputs or records.

## Limits that remain

1. **Historical attribution:** the original table is aggregate evidence. Even matching every cell within its frozen tolerance does not recover the original point coordinates, historical dependency versions, machine or RNG provenance. All captured geometry is REPRODUCED.
2. **Finite time and one setting:** this establishes only seed 1618, this initialization/order, horizon 6, assigned frequencies, prescribed breathing and 200 passes in the recorded environment. No limit theorem, general robustness or alternative parameter behavior follows.
3. **Order:** actual earlier writes enter later centers with nonzero contributions. No reverse-order or simultaneous control was evaluated, so no causal difference between those trajectories is measured.
4. **Group definitions:** fixed population labels, frequency labels, directed graph components and average-linkage observer groups differ. Stable observer member sets after pass 16 do not imply stopped motion, point merging or permanent independence.
5. **Clipping and schedules:** no clip activates here, but the original compressor is evaluated and no operation is removed. This does not explain other drivers' static/breathing equality or constitute a breathing-off comparison. H is prescribed in time; its small late floating multiplier is not a physical memory measurement.
6. **Geometry/display:** equal world axes and fixed camera are disclosed; close views use fixed translations and stated differing ranges; projection can overlap points. Lines join actual sampled states only. No fitted solids, missing surfaces, interpolated dynamics or shape classifier was introduced.
7. **Physical interpretation:** the original printed labels `SEPARATE`, `MERGED`, “independently evolving,” “living” and “condensate” are source descriptions or threshold labels. They do not establish a new force, energy, ground state, spacetime model or physical universe.

Protected hashes prove byte preservation within the stated scope. They do not prove non-execution; execution limits are supported separately by the methods, durable call ledger, process receipts and action attestation. The scope includes the entire pre-existing accepted construction directory and the actual attached handoff ZIP, not a whole-repository inventory.

No other engine, simulation setting, parameter/seed search, manuscript, ledger edit, kernel modification, Git write or publication was undertaken. Stop for GPT and Hilmir's review.
