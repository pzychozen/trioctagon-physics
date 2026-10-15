# SIM04 evidence and access guide

Start with [SIM04_REPORT.md](SIM04_REPORT.md), then the pre-evaluation [proofs](MATHEMATICAL_RESULTS.md). The report is a research handback for GPT review, not a publication manuscript. Nothing here grants a new licence or authorization for another computation.

## Source chain

The required edition is SIM03 publication/v0.1 at checkpoint `e1f5115402a05965834493c1254b03118a531c92`. [INPUT_MAP.json](evidence/INPUT_MAP.json) retains the exact repository paths, roles, sizes, SHA-256 values and Git blob identities. All 13 original files and their local copies passed initial and final preservation checks. Their unchanged bundled paths and identities follow.

| Bundled path | Bytes | SHA-256 |
|---|---|---|
| `inputs/PUBLICATION_MANIFEST.json` | 14362 | `99a748d6da10d4f76b634ea45f75e72cecc0e1b24c7f302b9133e682d03717c6` |
| `inputs/ACCESS_AND_EVIDENCE_MAP.md` | 10743 | `0f39c84b7406818af93c555fdb8e30bd4bb207d5b873c4e11425341190e7c542` |
| `inputs/SIM03_REPORT.md` | 25121 | `8e298578571d8d5267afb54fc9d28a7c12d805484c4480459ff6a302063fd553` |
| `inputs/review/SIM03_GPT_SCIENTIFIC_REVIEW.md` | 17989 | `b5c98805ce86ec996f34f050080c23da2d41e6bac156d38153347304d3e239a0` |
| `inputs/SRG_SIM03_DRIVING_GEOMETRY_AND_RESPONSE_ALIGNMENT_v0.1.tex` | 34123 | `324fdb98539f63f7b71a940b9aee3eed1ddfd43fb9fbd96f347288fd62966e23` |
| `inputs/analysis/center_decomposition.npz` | 5030162 | `28d312bfcd2941b87c8d51710f9b5fa1619ec7f1df325d7257083b462aba6b1a` |
| `inputs/analysis/repeated_phase_curves.csv` | 1087584 | `f9c92ce0a91a90df669f78e7ff68d715ff8545d41f655ed09e9bfd227314be1e` |
| `inputs/analysis/phase_spread.csv` | 950494 | `5a61f26d261321e9a5bae2866b237637699c1cb623dd261ef0d3417f074331db` |
| `inputs/evidence/OUTPUT_SCHEMAS.json` | 7421 | `0da830ca03539d2e31511aae8180e1460e729a18ef7615a0e62204a361fa504b` |
| `inputs/evidence/TABLE_SCHEMAS.json` | 19328 | `e9777672bf632deec418b5bc20c69f1e93047c9a5b8895fa4a154b1f76865e73` |
| `inputs/analyst/analyze.py` | 30969 | `d09534c2b0d52653630ce379749830f256656589ca3e58039183adb2e4ec4166` |
| `inputs/inputs/accepted_sim02/inputs/detached/engine_C.py` | 2875 | `05866296f874c5ec462426cf39bfd3518d8d9b3ea9274cb0f4915811532d395b` |
| `inputs/inputs/accepted_sim02/inputs/sources/source_C.py` | 5711 | `e13b92df8ac6df78cfee75b95dacea3b106e96bd5be9bf798cdcf39ccc5bc75c` |

The published SIM03 manifest is included as an unchanged historical inventory. It covers a broader edition than these 13 selected files; the remaining historical files are intentionally not duplicated. It is not the SIM04 bundle manifest. The nested historical access maps likewise retain their original context; follow this guide for the bounded SIM04 access map. The stored C sources and old analyst script are inspection material, not executable entry points for this handback.

## Mathematical and numerical evidence

The unchanged `received/` files contain the fixed work order, experiment specification, 14 fixture groups, mathematical specification, source identity map, and the supplied SIM03 closeout/next-math context. Their original handoff manifest is retained. The redundant handoff ZIP remains local but is excluded from the review archive.

[MATHEMATICAL_GATE.json](evidence/MATHEMATICAL_GATE.json), [ALGEBRA_FIXTURES.json](evidence/ALGEBRA_FIXTURES.json), [OUTCOME_ISOLATION_CANARY.json](evidence/OUTCOME_ISOLATION_CANARY.json) and [IMPLEMENTATION_GATE.json](evidence/IMPLEMENTATION_GATE.json) establish the pre-primary gates. The implementation gate freezes scientific scripts and the proof/specification files. Later report and packaging scripts read completed outputs only.

The sealed [PRE_OUTPUT_BOUNDS.npz](analysis/PRE_OUTPUT_BOUNDS.npz), its [seal](analysis/PRE_OUTPUT_BOUNDS_SEAL.json) and [DATA_ACCESS_LOG.json](evidence/DATA_ACCESS_LOG.json) separate analytic bounds from successor joins. The pure evaluator is [bounds.py](analyst/bounds.py). The one-shot worker is [analyze.py](analyst/analyze.py), its aggregation is [summarize.py](analyst/summarize.py), and [supervise.py](analyst/supervise.py) rejects existing start markers. Do not rerun these stages as part of reading the handback.

[OUTPUT_FIELD_GUIDE.md](OUTPUT_FIELD_GUIDE.md) defines every field family, native unit, mask, denominator and locator; [OUTPUT_SCHEMAS.json](evidence/OUTPUT_SCHEMAS.json) enumerates exact columns/dtypes/shapes. Its guide path is relative to the SIM04 root. The selected-record map provides explicit original identifiers. The pair table contains all 2,000 comparisons; center_pair_bounds.npz retains all 16,000 center pairs and outcome diagnostics; the dispersion table contains all 400 view/phase rows. RESULTS.json and both summary CSVs retain full-population quantiles with interpolation locators, categories and conditions. NUMERICAL_RESIDUALS.npz and NUMERICAL_QA.json retain all 59 signed residual arrays and extrema.

All inputs needed to inspect/recompute these fixed summaries from stored intermediates are included. The operational preservation guard intentionally expects the original Windows checkout and accepted checkpoint; this is not a claim that executing the historical entry points or the entire guarded workflow is portable. Archive verification is independent of that checkout and does not execute scientific code.

## Figures and operations

The six new PNGs are in `plots/`; [VISUAL_QA.json](evidence/VISUAL_QA.json) records direct inspection of every figure. Existing SIM03 figures were not regenerated. [SIM04_EXECUTION_RECEIPT.md](SIM04_EXECUTION_RECEIPT.md), stage STARTED/COMPLETE/progress records, captured stdout/stderr, the command/runtime ledger, and before/after baseline records preserve execution and source continuity. Operational local paths are provenance for private review, not public download links.

## Package verification

`MANIFEST.json` hashes every review-archive member except itself. The external `SIM04_TRANSPORT_SEAL.json` hashes the ZIP, covers its manifest identity and archive audit, and records the final aggregate size and post-packaging preservation check. The seal is intentionally outside the archive whose identity it asserts. The review archive excludes the original ZIP, cache/tmp contents, fonts, old archives and unrelated files. The filesystem aggregate-size cap still counts local excluded files.

To verify transport without executing any analysis, run the new standard-library-only `analyst/verify_bundle.py` in CMD with `torment` active and `python -B`. It accepts a ZIP path, checks safe unique member names, CRC, the manifest and all member hashes, and prints a compact result. It writes no files and does not import old or scientific code. It does not authenticate a ZIP against an independently supplied hash; compare its result to the separately supplied transport seal.
