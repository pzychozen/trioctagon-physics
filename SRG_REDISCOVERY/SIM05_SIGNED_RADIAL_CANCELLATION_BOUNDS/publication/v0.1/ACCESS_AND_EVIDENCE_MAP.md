# Evidence and access — SIM05 Part II

Start with the [paper](SRG_SIM05_SIGNED_RADIAL_INTERVALS_v0.1.pdf), [original report](SIM05_REPORT.md), [proofs](MATHEMATICAL_RESULTS.md), [field guide](OUTPUT_FIELD_GUIDE.md) and [schema](evidence/OUTPUT_SCHEMAS.json). The [claim-source map](CLAIM_SOURCE_MAP.csv) traces manuscript equations, theorems, tables, figures and displayed numbers. The external review bundle retains the full-precision transcription ledger and every page render.

## Preserved scientific evidence

`analysis/` contains every original analysis CSV, the original result JSON, pre-output archive and seal, outcome archive and numerical-residual NPZ. No array was downsampled, summary recomputed or figure regenerated. `plots/` contains all six unchanged accepted PNGs. `inputs/` preserves this study's selected original inputs in their original hierarchy. Older manifests describe broader historical submissions and are not the inventory of this edition; [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) is the edition inventory.

The analyst sources under `analyst/` are retained for reading. Exact specifications and fixed fixtures under `received/` define the historical evaluation. These files and the outcome-access log establish the analytic/outcome boundary; paper preparation did not invoke them.

## Review chronology

The root `review/` tree is the inherited ten-member SIM04 review. The complete thirteen-member subsequent SIM05 review is under `review/SIM05/`; its own acceptance is linked above. The inherited and later review sets are not merged or overwritten. Read [this study's subsequent acceptance](review/SIM05/SIM05_GPT_SCIENTIFIC_REVIEW.md). The profile-dominance theorem belongs to the subsequent SIM04 review, not the original SIM04 pre-evaluation assertions.

## Access boundaries and original checker layout

This is an inspectable curated edition, not the complete original execution package. The original analyst/supervisor guards expect the Windows research checkout and original start/baseline records. The SIM04 reviewer expects the extracted original SIM04 submission, original submission ZIP and transport seal, corrected SIM03 candidate ZIP, original SIM04 handoff ZIP and a fresh output directory. The SIM05 reviewer expects the extracted original SIM05 submission and external transport seal; its file-only audits additionally expect the prior SIM04 submission, review and SIM05 handoff. The included scripts were not run during paper preparation. No portability wrapper or execution assurance is supplied.

[HISTORICAL_ACCESS_BOUNDARIES.csv](HISTORICAL_ACCESS_BOUNDARIES.csv) enumerates all 24 unresolved Markdown destinations in retained original documents. Their wording and links were preserved rather than silently repaired. The nested original access maps and manifests retain their earlier, wider scope. Raw study/reviewer ZIPs and transport seals remain local. For the public upstream chain use pinned [SIM03](https://github.com/pzychozen/trioctagon-physics/tree/e1f5115402a05965834493c1254b03118a531c92/SRG_REDISCOVERY/SIM03_DRIVING_GEOMETRY_AND_RESPONSE_ALIGNMENT/publication/v0.1) and the [companion edition](../../../SIM04_FINITE_STEP_COLLECTIVE_SPEED_BOUNDS/publication/v0.1/README.md).

The following original submission members are deliberately omitted here (complete originals remain preserved locally):

- `SIM05_EXECUTION_RECEIPT.md`
- `analyst/build_handback.py`
- `analyst/input_gate.py`
- `analyst/package_review.py`
- `analyst/prepare.py`
- `analyst/read_results.py`
- `analyst/report_values.py`
- `analyst/static_gate.py`
- `analyst/supervise.py`
- `analyst/verify_bundle.py`
- `evidence/BASELINE_BEFORE.json`
- `evidence/COMMAND_RUNTIME_LEDGER.json`
- `evidence/FIGURES_COMPLETE.json`
- `evidence/FIGURES_STARTED.json`
- `evidence/FIGURES_STDERR.txt`
- `evidence/FIGURES_STDOUT.txt`
- `evidence/FIGURE_RESULT.json`
- `evidence/FINAL_QA.json`
- `evidence/FIXTURES_COMPLETE.json`
- `evidence/FIXTURES_PROGRESS.json`
- `evidence/FIXTURES_STARTED.json`
- `evidence/FIXTURES_STDERR.txt`
- `evidence/FIXTURES_STDOUT.txt`
- `evidence/INPUT_GATE.json`
- `evidence/PACKAGING_STARTED.json`
- `evidence/PREPARATION_EVENT.json`
- `evidence/PRESERVATION_AFTER.json`
- `evidence/PRESERVATION_INPUTS.json`
- `evidence/PRIMARY_COMPLETE.json`
- `evidence/PRIMARY_PROGRESS.json`
- `evidence/PRIMARY_RESULT.json`
- `evidence/PRIMARY_STARTED.json`
- `evidence/PRIMARY_STDERR.txt`
- `evidence/PRIMARY_STDOUT.txt`
- `evidence/RECEIVE.json`
- `evidence/STATIC_PREPARATION.json`
- `evidence/VISUAL_QA.json`
- `received/HANDOFF_MANIFEST.json`
- `received/HANDOFF_PREPARATION_QA.json`
- `received/HANDOFF_README.md`
- `received/SRG_SIM05_CODEX_WORK_ORDER_v0.1_20261014.md`
- `received/reference/MATHEMATICAL_RESULTS.md`
- `received/reference/OUTPUT_FIELD_GUIDE.md`
- `received/reference/SIM04_GPT_SCIENTIFIC_REVIEW_v0.1.zip`
- `received/reference/SIM04_REPORT.md`

These include operational start/finish and command records, workstation-heavy preservation inventories, redundant handoff material, transport/packaging helpers and full archive ZIPs. Selected retained code may import omitted operational helpers; inspect it in context rather than treating the curated tree as an execution recipe.
