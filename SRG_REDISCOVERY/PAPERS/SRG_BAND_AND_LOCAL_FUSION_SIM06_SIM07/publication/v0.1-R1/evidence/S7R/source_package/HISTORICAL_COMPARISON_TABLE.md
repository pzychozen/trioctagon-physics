# Historical aggregate comparison by column

All data rows are passes 1–200. Exact equality is parsed equality; every listed column passes its frozen criterion in all 200 cells. Maxima are first occurrences on a tie. The pass column is an index, not a scientific metric.

| Column | Exact / 200 | Max absolute error | Worst absolute pass | Max relative error | Worst relative pass |
|---|---:|---:|---:|---:|---:|
| pass | 200 | 0 | 1 | 0 | 1 |
| R_max | 95 | 2.77555756e-16 | 182 | 1.36917619e-15 | 182 |
| R_min | 161 | 1.11022302e-16 | 180 | 1.42178263e-15 | 180 |
| R_mean | 143 | 8.32667268e-17 | 187 | 5.76188632e-16 | 187 |
| R_std | 63 | 2.77555756e-17 | 197 | 6.86195899e-16 | 200 |
| n_resonance_clusters | 200 | 0 | 1 | 0 | 1 |
| n_spatial_clusters | 200 | 0 | 1 | 0 | 1 |
| entropy | 137 | 1.77635684e-15 | 13 | 3.74271598e-16 | 103 |
| mean_grf | 188 | 1.11022302e-16 | 90 | 1.11994162e-16 | 99 |
| top_seed_id | 200 | 0 | 1 | 0 | 1 |
| L_effective | 200 | 0 | 1 | 0 | 1 |
| band_0.1508 | 126 | 1.11022302e-16 | 179 | 7.3837799e-16 | 179 |
| band_0.2440 | 126 | 8.32667268e-17 | 171 | 5.82508485e-16 | 171 |
| band_0.3948 | 121 | 8.32667268e-17 | 160 | 5.89610195e-16 | 160 |
| band_0.6388 | 152 | 5.55111512e-17 | 170 | 3.90753023e-16 | 170 |

Integer criterion: exact equality for pass, n_resonance_clusters, n_spatial_clusters and top_seed_id. Continuous criterion: `abs(replay-historical) <= 1e-12 + 1e-10*abs(historical)`. Relative error uses historical magnitude as denominator; zero/zero is 0, nonzero/zero is null with absolute error retained.

Totals: **800 exact integer cells** (200 pass labels + 600 metrics), **2,200 accepted floating cells** (1,512 exact + 688 near-only). **3,000 cells total; 2,800 non-pass metrics.** No missing/nonfinite cells or schema/pass mismatches.

Reference/capture exports are byte-identical to each other. The historical export is not byte-identical to the replay. Full cell-level values: [HISTORICAL_COMPARISON.json](analysis/HISTORICAL_COMPARISON.json). Criteria were supplied before either initialization in [RUN_SPECIFICATION.json](handoff/RUN_SPECIFICATION.json).
