# Record selection, passive reproduction and preservation

Assignment: SRG_SIMULATION_STUDY_06_TOWER_II_CONSTRUCTION_01, 24 October 2026. Authority is the user's request to execute the attached [work order](WORK_ORDER.md). Historical reports, code comments and original narrative recommendations are source material; their proposed next experiments were not treated as current instructions.

## Locations and evidence selection

Repository: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`.

New workspace: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SRG_SIMULATION_STUDY_06_TOWER_II\CONSTRUCTION_01`.

Original source/CSV/narrative were read from `SRG_REDISCOVERY\R0_SOURCE_RECOVERY\selected_sources\MARCH_19023429` under that repository. The former archive locator is recorded as missing, with the exact-hash R0 copy used instead. The principal numerical input is `SRG_REDISCOVERY\R1_CLIPPING_AND_SPECTRAL_AUDIT\RUN_01\seed2038_eps1`, identified through the retained raw-data index. Configuration and provenance are explained in [ORIGINAL_EVIDENCE_AND_EXISTING_REPLAY.md](ORIGINAL_EVIDENCE_AND_EXISTING_REPLAY.md).

All 601 boundaries of this **one** selected record are included. Seventeen original R1 files are copied; the configuration also lists two counterfactual arrays, deliberately not copied or analyzed here. Prior eps0/eta0/H-off controls remain report context. No fresh control analysis was performed. Selected R2 baseline tables are unchanged context, labeled eps0 and justified only where R1's prior exact equality permits reuse.

Display selection is explicit: full-field snapshots 0,20,100,200,400,600; band-0 detail at 20,200,600; three lowest band-0 IDs 4,8,9; movement windows 0–20,20–200,200–600. No seed, parameter or candidate trajectory was searched. Supplemental graph membership tables use states 0,20,50,100,200,400,599. All graph counts use incoming boundaries 0–599; final state 600 receives geometry only. No hypothetical pass 601 is supplied.

## New code and reproduction

| File | Function / execution status |
|---|---|
| intake_inputs.py | Initial source/input copying and scoped baseline. Executed once; intentionally refuses overwrite. Not a simulator. |
| add_inputs.py | Adds cited historical CSV/narrative and prior context copies; existing identical inputs are not rewritten. Executed for intake. |
| read_text.py | Numbered text inspection utility. Reads files only. |
| inspect_saved_records.py | Reads fixed arrays with mmap_mode='r', allow_pickle=False; verifies selected file hashes and excerpt line content; derives descriptive band/graph/motion tables. Executed. |
| render_saved_figures.py | Draws saved coordinates and derived tables. Executed, then adjusted for full normalized-point visibility and clearer ID legends; final three images inspected. |
| finalize_review.py | Document/package checks and scoped source preservation; creates manifest, ZIP and ZIP-identity receipt. No scientific recurrence or RNG work. |

To reproduce only the new passive tables/figures, use Windows **Command Prompt** in the package directory with the existing environment:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONIOENCODING=utf-8
python -B inspect_saved_records.py
python -B render_saved_figures.py
```

These commands overwrite only this package's derived tables/figures. They do not advance a state, restore RNG checkpoints or regenerate noise. Running the copied original source, the audited core, old experiment scripts or historical checkers is neither needed nor authorized by this checkpoint. No environment dependencies were changed.

The passive inspection used Python 3.11.15, NumPy 2.4.4 and SciPy 1.17.1. The figure register records Matplotlib's version, scales and inputs. Those are the inspection environment, not a claim about the original historical runtime. New graph summaries use the retained source's distance/sort convention with that environment; exact-tie sorting is not silently repaired.

## Scope of preservation and checks

[INPUT_BASELINE.json](INPUT_BASELINE.json) records the original absolute locator, package-relative copy, byte count and SHA-256 for each of the **43 used inputs**. [PRESERVATION_RECEIPT.json](PRESERVATION_RECEIPT.json) rechecks each original and copied input against that baseline. This is a scoped check, not a repeated repository/publication audit. Historical sources, accepted reports, published editions, canonical ledger, kernels and unrelated work were not edited; only the new workspace was written.

[DOCUMENT_QA.json](DOCUMENT_QA.json) reports new-document links and required deliverables; [VISUAL_INSPECTION.json](VISUAL_INSPECTION.json) records inspection of all three final PNGs at their actual saved sizes. These are document/identity checks, not reruns of earlier scientific audits. [MANIFEST.json](MANIFEST.json) lists the included payload files with byte counts and SHA-256. The manifest excludes itself and the generated ZIP/identity receipt to avoid self-reference; the ZIP includes the manifest, and the outer [REVIEW_ZIP_IDENTITY.json](REVIEW_ZIP_IDENTITY.json) identifies the ZIP and verifies its entries.

Execution boundary: **0 new state updates; 0 RNG draws; 0 historical module imports; 0 old scientific checker executions; 0 Git writes/publication actions.** No constructor, recurrence step, noise regeneration, FFT audit, seed sweep or altered model was executed. The copied historical code is evidence, not an invoked dependency.

The earlier scientific results are retained with their original scopes. Only new descriptive geometry/graph results and new static renderings are claimed for SIM06. Delivery ends this task for GPT and Hilmir review.
