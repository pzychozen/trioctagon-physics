# Relative evidence index

Extract the delivered review ZIP with directories intact. The manuscript's citations resolve to the convenient unchanged copies below. The two immutable input archives contain the full studies and prior methods; no personal Windows directory is needed to substantiate the paper.

## Immutable accepted inputs

**A4:** [SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip](evidence/inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip), 1,372,925 bytes, SHA-256 `1a10bb9c2ad94789efc6d16d7a579a5e60346275ed8c44ac4a386e7799879025`.

**A5:** [SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip](evidence/inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip), 9,425,603 bytes, SHA-256 `ae4fe33903410b211544f8f17cf4b79473b983bf4920c26c4406b27f55d37736`.

The full supplied outer handoff was identity checked. Its manifest and input manifest are retained under `evidence/`; the outer wrapper is not duplicated in this ZIP. A5 already contains the complete original SIM05 submission as `source_package/`; a second copy of that submission ZIP is deliberately omitted from delivery. The working copy is preserved locally.

## Convenient unchanged copies

- [SIM04 source](evidence/originals/SIM04/srg_seed_explorer.py), [full historical state CSV](evidence/originals/SIM04/deep_trajectory.csv), [historical metrics](evidence/originals/SIM04/pass_metrics.csv), [historical note](evidence/originals/SIM04/SRG_Deep_Analysis.md).
- [SIM05 source](evidence/originals/SIM05/srg_infinity.py), [historical metrics](evidence/originals/SIM05/srg_infinity_asymptotic.csv), [historical note](evidence/originals/SIM05/SRG_Infinity_Seeds.md).
- [SIM04 scientific review](evidence/reviews/SIM04/SIM04_GPT_SCIENTIFIC_REVIEW.md), [source review with reviewed derivations](evidence/reviews/SIM04/source_review.md), [independent results](evidence/reviews/SIM04/independent_data/independent_checks.json), [variance decomposition](evidence/reviews/SIM04/independent_data/fixed_final_partition_variance.json).
- [SIM05 scientific review](evidence/reviews/SIM05/SIM05_GPT_SCIENTIFIC_REVIEW.md), [verification](evidence/reviews/SIM05/verification.json), [findings](evidence/reviews/SIM05/findings.json), [endpoint membership](evidence/reviews/SIM05/final_components.csv), [supplemental results](evidence/reviews/SIM05/supplemental_checks.json).
- [SIM04 geometry addendum](evidence/studies/SIM05/SIM04_3D_ADDENDUM.md), [independent covariance readback](evidence/reviews/SIM05/SIM04_geometry_rechecked.csv), [normalized pair changes](evidence/reviews/SIM05/SIM04_normalized_pair_changes.csv).
- Accepted explanations are under `evidence/studies/SIM04/` and `evidence/studies/SIM05/`; selected saved analysis tables are under `evidence/tables/SIM05/`.

These convenient copies preserve original text, including links relative to their original package structure. Where such an inherited link does not resolve in the convenience tree, open the same document inside A4 or A5 with its complete original structure. New manuscript citations, the claim matrix and this index point to existing delivered paths. Do not rewrite accepted documents merely to change their links.

## Exact archive locations for the complete record

In **A4**, use `START_HERE.md`, `CONSTRUCTION.md`, `ORIGINAL_EVIDENCE.md`, `VERIFICATION_AND_LIMITS.md`, `originals/`, `analysis/`, `figures/` and its manifest. Its retained scripts are inspection methods from the accepted study.

In **A5**:

- `SIM05_GPT_SCIENTIFIC_REVIEW.md`, `verification.json`, `findings.json`, `supplemental_checks.json`, `final_components.csv`: accepted GPT review and additional findings.
- `source_package/START_HERE.md`, `source_package/CONSTRUCTION.md`, `source_package/HISTORICAL_EVIDENCE_AND_CLAIMS.md`, `source_package/REPLAY_AND_3D_ANALYSIS.md`, `source_package/SIM04_3D_ADDENDUM.md`, `source_package/VERIFICATION_AND_LIMITS.md`: complete submitted study.
- `source_package/replay/captured/`: saved replay arrays, metrics, ordered per-point states and RNG checkpoints. `source_package/replay/reference/`: retained reference outputs. Prior methods are at `source_package/audited_core.py`, `source_package/run_bounded.py`, `source_package/analyze_saved.py`, `source_package/detail_and_figures.py`, and `source_package/verify_package.py`; independent review methods are the top-level `independent_audit.py` and `supplemental_checks.py`.
- `source_package/analysis/`: complete fixed-record analysis, including field geometry, graph summaries, selected groups, clipping, stage summaries and SIM04 normalized pairs.
- `source_package/context/SIM04_GPT_REVIEW/`: complete accepted earlier review, independent results, source review and six-point figure.
- `source_package/figures/`: original accepted PNG/SVG assets; unchanged copies selected for this manuscript are under `figures/` beside the PDF.
- `source_package/ENVIRONMENT.json`, `CORE_IDENTITY.json`, `REFERENCE_EQUIVALENCE.json`, `RUN_BUDGET.json` and original manifest: reproducibility identities and already closed execution budget.

See [ARCHIVE_MEMBER_INDEX.json](ARCHIVE_MEMBER_INDEX.json) for the exact member names and stored sizes. This is a file inventory of the two specified inputs, not a new survey of historical archives. Prior science scripts are included unchanged **for inspection**; no current authorization to execute them is implied.

## Source identity anchors

| Source | SHA-256 |
|---|---|
| `originals/SIM04/srg_seed_explorer.py` | `0c8ec661624bd100212b29d75dd184cacf2adbf5d173584e3817460d9fd6ea10` |
| `originals/SIM05/srg_infinity.py` | `742e40f1b4326f3ea5c8c88bd59aec7ee5a2bb942755a0fbc1861ce7c5eddf9d` |

These names in the table are relative to `evidence/`. Full input identities are in [INPUT_BASELINE.json](INPUT_BASELINE.json), [HANDOFF_BASELINE.json](HANDOFF_BASELINE.json), and [PRESERVATION_RECEIPT.json](PRESERVATION_RECEIPT.json). The final candidate manifest is scoped separately and does not claim to inventory the entire repository.
