# Access and evidence map

This map belongs to the curated SIM01 edition. Paths below resolve from this edition root unless explicitly described as historical or local-only. Accepted reports, figures, data and review records have not been rewritten.

## Reading and review paths

Start with [SIM01_REPORT.md](SIM01_REPORT.md) for the reconstruction and finite observations. Read [review/SIM01_GPT_SCIENTIFIC_REVIEW.md](review/SIM01_GPT_SCIENTIFIC_REVIEW.md) for subsequent acceptance and the reviewer-only B/C prefix comparison. That unchanged review uses two original path conventions:

- Its references to sources/, detached/, runs/, data/ and evidence/ mean this edition root.
- Its bare reviewer filenames mean review/: [INDEPENDENT_REVIEW_RESULTS.json](review/INDEPENDENT_REVIEW_RESULTS.json), [ARCHIVE_REVIEW.json](review/ARCHIVE_REVIEW.json), [review_saved_evidence.py](review/review_saved_evidence.py) and [REVIEW_MANIFEST.json](review/REVIEW_MANIFEST.json).

There are three distinct manifests. The [review manifest](review/REVIEW_MANIFEST.json) covers the four other review files. The unchanged [submission manifest](evidence/SUBMISSION_REVIEW_MANIFEST.json) historically covers all 67 payloads in the original 68-member submission; it is retained as provenance and does not claim that every original member is present here. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) is the exact inventory of this curated edition, except itself. The external REPOSITORY_PATH_MANIFEST.json additionally covers this edition manifest and the proposed index file.

## Source-to-edition mapping

The historical path column is relative to the owner's OLD_MATERIAL directory. Those locations are provenance references, not promised public directories.

| Engine | Historical relative path | Byte-preserved source | Detached copy |
|---|---|---|---|
| A | Simulations_Trash/Simulations_part_2/recursive_attractor.py | [source_A.py](sources/source_A.py) | [engine_A.py](detached/engine_A.py) |
| B | Simulations_Trash/Simulations_part_2/3Dtriangles.py | [source_B.py](sources/source_B.py) | [engine_B.py](detached/engine_B.py) |
| C | Simulations_Trash/Simulations_part_1/plot_1.py | [source_C.py](sources/source_C.py) | [engine_C.py](detached/engine_C.py) |

The two data/ files preserve OLD_MATERIAL/Simulations/CSV/[PLOT_1_tetrahedral_states_20250712_015421.csv](data/PLOT_1_tetrahedral_states_20250712_015421.csv) and [tetrahedral_states_20250712_015647.csv](data/tetrahedral_states_20250712_015647.csv). Exact original identities also appear in [SELECTED_INPUT_IDENTITIES.json](received/SELECTED_INPUT_IDENTITIES.json).

Inspect original programs as text: importing their top-level modules can initialize random state, run motion, launch a GUI or write files. The detached numerical copies retain the source operators; [EXTRACTION_MAP.json](evidence/EXTRACTION_MAP.json) and [prepare_detached.py](prepare_detached.py) document extraction.

## Saved records and retained execution evidence

Each runs/A, runs/B and runs/C directory contains states.npz, initial_state.npz, RNG_INITIAL.json, RNG_FINAL.json, RUN_RESULT.json, OBSERVATIONS.json and observations.csv. C additionally contains [switch_events.csv](runs/C/switch_events.csv).

State index 0 is initial; state k+1 follows update k. H, G, source frame/time, draws, energy and detector arrays are indexed per update. The NPZ preserves raw wrapped positions, raw displacements, minimal-image displacements and the accumulated unwrapped view. NaN marks an inapplicable observable or undrawn slot, not a nonfinite position/velocity state. Initial RNG metadata includes checkpoints before and after original initialization; source seed 2038 is the declared modern replay seed.

The evidence directory retains [preflight results](evidence/PREFLIGHT_RESULTS.json), the [12-call ledger](evidence/PREFLIGHT_CALL_LEDGER.json), [replay supervision](evidence/REPLAY_SUPERVISION.json), [observations](evidence/REPLAY_OBSERVATIONS.json), [saved-log verification](evidence/SAVED_RECORD_LOCAL_VERIFICATION.json), [input identities](evidence/INPUTS_BEFORE.json) and [original final QA](evidence/FINAL_QA.json). The latter two refer to the original study workspace and include local paths; see the disposition's owner review item. They were not regenerated for publication.

All five scientific plots are preserved. Numerical code retained for inspection comprises prepare_detached.py, engine_api.py, preflight.py, worker_replay.py, supervise_replays.py, analyze_replays.py and check_saved_records.py. The last imports the included received/inspect_saved_records.py and reads received/SAVED_RECORD_INSPECTION.json plus the two included historical CSVs.

## Checker compatibility and local-only references

The unchanged reviewer checker explicitly requires a root REVIEW_MANIFEST.json and exactly that manifest's complete input tree. Its original instruction therefore targets the original 68-member submission, **not this edition root or review/**. Passing this curated edition unchanged would fail its inventory assertion. All scientific data it examines are preserved here, but no compatibility wrapper or amended checker has been introduced.

The original SIM01_GPT_REVIEW.zip (SHA-256 a3daf4e915b73a6ec4987647732d322623c5a155b8dab436883e30dacbf6a31f) remains an owner-held local review artifact. It is not a public download in this edition. The review's archived-check results concern that submission. Requests for the complete original execution/checking context should go to the owner; public access is not asserted.

The main routine of received/inspect_saved_records.py additionally expects unrelated curvature/glyph/embedding CSVs when used independently. Those are outside this edition. The accepted check_saved_records.py used only its inspect_log function on the two selected records. Likewise, historical preparation/finalization scripts and execution guards refer to their original directory layout. Retained runner code is explanatory execution evidence, not an instruction to rerun or overwrite the preserved outputs.

Omitted submission members are three duplicate console summaries; STARTED.json and PROGRESS.json for A/B/C; finalize_review.py; the original execution work order; the selection-review prose; and the earlier selection-package manifest. Their execution details are represented by the retained final results and ledgers. Their identities remain in the historical submission manifest. No scientific array, accepted plot, accepted report or GPT-review member is omitted.

R0/TA0 context, selected-input references to Downloads, the June topology PDF lineage, the full historical Simulations.zip and unrelated source/data families remain local-only. Curvature Adjusted_DT is not supplied as an input to A/B/C. These are explicit access boundaries, not broken public downloads or newly reconstructed sources.

The repository's existing [licence scope](../../../../LICENSE_SCOPE.md) is an unchanged repository dependency outside the proposed payload. No fonts, movies, caches, environment dumps, chat exports, full private archives or unrelated work orders are part of this edition.

