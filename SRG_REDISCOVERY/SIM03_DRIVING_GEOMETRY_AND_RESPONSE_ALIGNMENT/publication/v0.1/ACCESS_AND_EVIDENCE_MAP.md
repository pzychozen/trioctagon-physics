# Evidence and source access

The paper interprets accepted SIM03 records and subsequent reviewer deductions. No scientific program was executed during manuscript preparation.

## Read the evidence in layers

| Layer | Included material | Scope |
| --- | --- | --- |
| Narrative | [SIM03_REPORT.md](SIM03_REPORT.md) | Accepted original report, unchanged |
| Numerical ledgers | [update budgets](analysis/update_budgets.csv), [cycle summary](analysis/cycle_summary.csv), [results JSON](analysis/RESULTS.json) | Both exact balances and all nine distinct blocks |
| Repeated phase | [phase curves](analysis/repeated_phase_curves.csv), [phase spread](analysis/phase_spread.csv) | All-five and new-four correlated cycle views |
| Labeled comparisons | [same-phase rows](analysis/same_phase_comparisons.csv), [pair summaries](analysis/same_phase_summary.csv), [center distances](analysis/comparison_center_distances.npz) | Seven prescribed pairs; mean/max/RMS distances at three stages |
| Cross-arm context | [comparison rows](analysis/cross_arm_comparisons.csv), [block summaries](analysis/cross_arm_block_summary.csv) | Equal actual update index, REPEATED minus CONTINUOUS |
| Factors and orientation | [factor/stratum table](analysis/factor_stratum_summary.csv), [retention/orientation table](analysis/retention_orientation_summary.csv) | Signed/absolute activity, masks, fixed bins; observational strata |
| Primary decomposition | [center arrays](analysis/center_decomposition.npz) | 14,400 rows; original saved velocities and derived intermediates |
| Definitions | [original C](inputs/accepted_sim02/inputs/sources/source_C.py), [detached C](inputs/accepted_sim02/inputs/detached/engine_C.py), [API](inputs/accepted_sim02/inputs/engine_api.py) | Exact source bytes, for inspection |
| Saved states | [prefix](inputs/accepted_sim02/inputs/runs/C/states.npz), [CONTINUOUS](inputs/accepted_sim02/runs/CONTINUOUS/states.npz), [REPEATED](inputs/accepted_sim02/runs/REPEATED/states.npz) | Complete three accepted state records, untouched |
| Analyst | [decomposition/summary code](analyst/analyze.py), [algebra helper/fixtures](analyst/algebra.py), [plot code](analyst/plot.py) | Accepted program text, not a portable runnable distribution |
| Numerical QA | [QA](evidence/QA.json), [algebra gate](evidence/ALGEBRA_GATE.json), [implementation gate](evidence/IMPLEMENTATION_GATE.json) | Original checks, not new checker execution |
| Schemas | [NPZ fields](evidence/OUTPUT_SCHEMAS.json), [CSV columns](evidence/TABLE_SCHEMAS.json) | Complete field lists, types, dimensions and row counts |
| Review | [scientific review](review/SIM03_GPT_SCIENTIFIC_REVIEW.md), [manifest](review/REVIEW_MANIFEST.json) | Entire seven-member subsequent review preserved |
| Claim provenance | [claim-source map](CLAIM_SOURCE_MAP.csv) | All numbered equations, figures, tables and grouped quantitative statements |

The ten CSV tables have 1,800 update rows; 9 block rows; 1,000 repeated-phase rows; 400 phase-spread rows; 1,400 same-phase comparison rows; 7 pair summaries; 800 cross-arm rows; 4 cross-arm block summaries; 156 factor/stratum rows; and 28 retention/orientation bins. Repeated appearances of the shared prefix are views, not extra observations.

Dataset IDs in the primary NPZ are PREFIX=0, CONTINUOUS=1, REPEATED=2. Center labels are 0–7; actual update n has predecessor S_n and successor S_(n+1). Source frame/time fields retain driving phase. Source bits remain int8 in the prefix and int64 in continuations; analysis-only tags are lossless int8. NPZ files contain no object arrays or pickle requirement.

incoming_mean_speed, pre_damping_mean_speed and post_mean_speed are different quantities. The first is used by G, the second is mean norm(w), and the third uses saved successors. L is evaluated stably with direct subtraction retained; R is direct norm subtraction with a stable alternative retained. Invalid diagnostics carry masks. CSV blanks/JSON null denote undefined values, not zero. The 1e-12 ratio-reporting floor does not alter any budget identity. Correlated-cycle summaries are population moments, not independent-trial confidence intervals.

## Exact identities and prior work

The accepted original SIM03 submission has 97 members and 12,537,222 bytes, SHA-256 219edf82a5ad646e935623cc21d95f1d009d6a65ea3797dfcc6697ae4106a6f5. The unchanged report has 25,121 bytes, SHA-256 8e298578571d8d5267afb54fc9d28a7c12d805484c4480459ff6a302063fd553.

The subsequent GPT review archive has seven members and 67,409 bytes, SHA-256 10cc6f22fe65cbfb7159cfa9fdccb157ddfdc71f5e5c8da3ad9c41223a413586. Its report has 17,989 bytes, SHA-256 b5c98805ce86ec996f34f050080c23da2d41e6bac156d38153347304d3e239a0. All seven unpacked members are included; neither original ZIP is republished.

Source continuity is pinned to SIM02 commit 36621a283c48edbd6050771a5beddc4dde7cedcf. SIM01 is referenced at 0ecedec5a7d7077740b0d336ba9959dc8f117caf. The external preparation receipt records local checks against those committed reference files; it does not claim a fresh remote-main publication check.

[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) gives the size, SHA-256 and exact archive-member provenance of every retained file, alongside the identities of new editorial files. It excludes itself; the external repository-path manifest covers it and the proposed research-index append.

## Original layout and omission boundary

This curated edition is not the complete original SIM03 submission. Local preparation/transport receipts, Git/dirty-file baselines, environment/path maps, workflow orders, common.py/prepare.py/supervise.py helpers, scratch arrays, caches and earlier full archives are intentionally omitted. The accepted report remains unchanged, so historical links to those omitted local records are not silently retargeted.

In particular, the original report's INPUT_MAP link is replaced as an access route by this edition's provenance manifest; its DOCUMENTATION_LOOKUPS link concerns extrema already identified in the report and retained tables. Its source SIM02 report/paper links refer to the pinned SIM02 edition, not duplicate files here. Its work-order/specification, execution receipt, evidence-guide and external transport-seal links concern the original local submission. Those are not advertised as included publication members.

The retained analyst scripts depend on an omitted workstation-oriented common helper and their original layout. They are exact inspection sources, not executable entry points for this edition. The independent reviewer script requires the extracted full original SIM03 submission and the earlier approved SIM02 paper-review ZIP for provenance checks. It was not rerun and this subset does not claim to satisfy those requirements.

The reviewer made two saved-record reconstruction attempts: 3,600 update evaluations over 1,800 distinct updates, with zero trajectories or RNG calls. The first normalized-ratio conditioning issue and corrected native-unit identity comparison are disclosed in [the execution note](review/REVIEW_EXECUTION_NOTE.json); the [successful results](review/INDEPENDENT_REVIEW_RESULTS.json) report their own per-pass counts. The manuscript makes no cross-environment bitwise-equivalence claim.

## Included original figures and files

All eight PNGs are embedded unchanged. The corrected figure-03 impulse title is the accepted final source; its h curve is explicitly distinguished from the h² used in the exact squared-impulse product. The list below links every retained member, including all review files; the manifest records its identity and provenance.

- [SIM03_REPORT.md](SIM03_REPORT.md)
- [plots/01_actual_speed_budgets.png](plots/01_actual_speed_budgets.png)
- [plots/02_phase_budget_terms.png](plots/02_phase_budget_terms.png)
- [plots/03_normalization_and_gain.png](plots/03_normalization_and_gain.png)
- [plots/04_alignment_and_cancellation.png](plots/04_alignment_and_cancellation.png)
- [plots/05_damping_retention_orientation.png](plots/05_damping_retention_orientation.png)
- [plots/06_phase_velocity_differences.png](plots/06_phase_velocity_differences.png)
- [plots/07_scalar_dispersion_balance.png](plots/07_scalar_dispersion_balance.png)
- [plots/08_cross_arm_context.png](plots/08_cross_arm_context.png)
- [analysis/cross_arm_block_summary.csv](analysis/cross_arm_block_summary.csv)
- [analysis/cross_arm_comparisons.csv](analysis/cross_arm_comparisons.csv)
- [analysis/cycle_summary.csv](analysis/cycle_summary.csv)
- [analysis/factor_stratum_summary.csv](analysis/factor_stratum_summary.csv)
- [analysis/phase_spread.csv](analysis/phase_spread.csv)
- [analysis/repeated_phase_curves.csv](analysis/repeated_phase_curves.csv)
- [analysis/retention_orientation_summary.csv](analysis/retention_orientation_summary.csv)
- [analysis/same_phase_comparisons.csv](analysis/same_phase_comparisons.csv)
- [analysis/same_phase_summary.csv](analysis/same_phase_summary.csv)
- [analysis/update_budgets.csv](analysis/update_budgets.csv)
- [analysis/center_decomposition.npz](analysis/center_decomposition.npz)
- [analysis/comparison_center_distances.npz](analysis/comparison_center_distances.npz)
- [analysis/RESULTS.json](analysis/RESULTS.json)
- [analyst/algebra.py](analyst/algebra.py)
- [analyst/analyze.py](analyst/analyze.py)
- [analyst/plot.py](analyst/plot.py)
- [evidence/QA.json](evidence/QA.json)
- [evidence/ALGEBRA_GATE.json](evidence/ALGEBRA_GATE.json)
- [evidence/OUTPUT_SCHEMAS.json](evidence/OUTPUT_SCHEMAS.json)
- [evidence/TABLE_SCHEMAS.json](evidence/TABLE_SCHEMAS.json)
- [evidence/IMPLEMENTATION_GATE.json](evidence/IMPLEMENTATION_GATE.json)
- [inputs/accepted_sim02/inputs/detached/engine_C.py](inputs/accepted_sim02/inputs/detached/engine_C.py)
- [inputs/accepted_sim02/inputs/sources/source_C.py](inputs/accepted_sim02/inputs/sources/source_C.py)
- [inputs/accepted_sim02/inputs/engine_api.py](inputs/accepted_sim02/inputs/engine_api.py)
- [inputs/accepted_sim02/inputs/runs/C/states.npz](inputs/accepted_sim02/inputs/runs/C/states.npz)
- [inputs/accepted_sim02/runs/CONTINUOUS/states.npz](inputs/accepted_sim02/runs/CONTINUOUS/states.npz)
- [inputs/accepted_sim02/runs/REPEATED/states.npz](inputs/accepted_sim02/runs/REPEATED/states.npz)
- [review/ARCHIVE_REVIEW.json](review/ARCHIVE_REVIEW.json)
- [review/INDEPENDENT_REVIEW_RESULTS.json](review/INDEPENDENT_REVIEW_RESULTS.json)
- [review/REVIEW_EXECUTION_NOTE.json](review/REVIEW_EXECUTION_NOTE.json)
- [review/REVIEW_MANIFEST.json](review/REVIEW_MANIFEST.json)
- [review/review_sim03_saved_evidence.py](review/review_sim03_saved_evidence.py)
- [review/SIM03_GPT_SCIENTIFIC_REVIEW.md](review/SIM03_GPT_SCIENTIFIC_REVIEW.md)
- [review/VISUAL_REVIEW.json](review/VISUAL_REVIEW.json)
