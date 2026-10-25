# Original evidence and the existing R1 record

This study joins three different kinds of evidence: what the complete program specifies, what the historical aggregate CSV records, and what an existing later reproduction records point by point. A later plot of reproduced coordinates is not an original historical observation. A historical narrative is evidence of an interpretation, not automatic proof of its scientific claims.

## Source identity and provenance

The work order's former archive locator is absent locally:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\research_files\archive_members\Zenodo_research\19023429\simulations.zip\srg_golden_tower_II.py`

Here `simulations.zip` denotes the old extracted directory layout. The unchanged recovered source survives at:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\R0_SOURCE_RECOVERY\selected_sources\MARCH_19023429\srg_golden_tower_II.py`

It matches **34,980 bytes / SHA-256 `147a32be3b6d6aad17ada6ab7be2fbc3994c3363f74d6a2b351fb8eecda80304`**. The [bundled original](original/srg_golden_tower_II.py) is an unchanged copy of that file. Full source lines 1–842 were read, including all drivers. The original output path at line 30 points to a former Linux session; it does not identify the Windows replay environment.

The R0 [audited excerpt](context/R0/audited_golden_core.py), SHA-256 `6b2f0a05df5871abe4fe97a9e56abd233ab55952028ae953a4b7a652fb24d5e8`, supplies an eight-line explanatory/import prefix followed by source lines 31–254. A new **text-only** comparison confirms exact line-content equality. The original uses CRLF and the excerpt LF; this is not a raw substring byte-equality claim. R1's [source provenance](context/R1/SOURCE_PROVENANCE.json) identifies this excerpt as its core. No historical Python module was imported in SIM06.

The 17 selected R1 files in this package independently match their entries in the retained [R1 payload manifest](context/R1/PAYLOAD_MANIFEST.json), by byte count and SHA-256. This was file-identity checking, not a recurrence or RNG rerun. See [the identity receipt](derived/SOURCE_AND_RECORD_IDENTITY.json).

## What the original saved evidence establishes

The [unchanged CSV](original/self_coupled_breathing.csv) is 765 bytes, SHA-256 `67c4aab59b8dd4ac8f46387cf4800fe4408aa54f253afb8481a51c6dfb16a462`. It has seven aggregate rows and no per-pass coordinates, velocities, RNG checkpoints or movie frames. The selected epsilon=1 row reports:

| Column | Historical saved value | Source interpretation |
|---|---:|---|
| L_mean | 11.905260171214326 | Mean of 200 incoming-state bound readouts |
| L_std | .9892193445854098 | Population standard deviation of those readouts |
| L_range | 3.5626358780586127 | Maximum minus minimum readout |
| L_oscillating | True | Output of the source's one-bin power threshold |
| L_dom_freq | .006666666666666667 | 1/150 cycles/pass, the first nonzero bin of its window |
| surviving_bands | 4 | All four completed-state band means exceed .01 |
| R_mean | .5489832686504329 | Completed-state-200 mean absolute resonance |

All seven rows have the same final R_mean and four surviving bands. That equality is a historical aggregate observation. It alone would not prove identical intermediate trajectories or inactive clipping. R1 subsequently addressed those stronger questions for its selected paired runs. The other six rows are retained as historical context, not six additional SIM06 investigations.

The [original narrative](original/The_Golden_Tower_Part_II.md) names Claude collaborating with pzychozen and dates itself March 14, 2026. Lines 26–38 and 85–101 describe a universal, self-sustaining compression oscillation and an independent channel. The source and retained audit support a narrower reading:

| Historical interpretation | Source / retained-evidence distinction |
|---|---|
| Universal 150-pass heartbeat | Source lines 408–418 remove only the mean from 150 samples, then select an FFT bin. R1 found the dominant bin following changed window lengths, including 1/150, 1/300 and 1/550. This does not identify a window-independent oscillator. No spectrum was recomputed here. |
| Independent breathing field | L_p is overwritten as 9(1+epsilon mean|R_(p−1)|). It has no autonomous evolution or independently carried phase. With inactive clipping it is an affine readout. |
| Changing L drives the observed R through compression | In retained selected R1 runs no clipping event occurs; epsilon=0 and 1 give exactly equal saved X/V/R paths for the checked seeds. This path-specific result does not assert that bounds can never matter. |
| Zeta controls a measured lock coupling | The other driver calculates a zeta-based predicted gamma after evolution. That expression is not a coefficient of the class update or an independent measurement of gamma. |
| No new bands proves spectral closure | Assigned labels/frequencies never evolve in this core. Absence of new labels is structurally different from absence of new frequencies in a recorded amplitude signal. |
| Smaller coupling_width means narrower frequency matching (note line 81) | The actual factor is exp(−width log-ratio²): decreasing width broadens the raw frequency preference. Its net normalized effect also depends on the selected neighbors and distances. |
| Horizon-isolated tunneling experiment | That separate driver has band-wide fusion and no unperturbed paired control. Its graph radius alone cannot certify isolation of the full update. This study does not redo its outcome analysis. |

No directly attributable historical coordinate movie or image for this selected 200-pass setting was identified in the retained R0 inventory. The complete script itself has no rendering routine. We neither invent a missing movie nor extend the search into another archive survey. This is a scoped evidence gap, not a claim that no recording ever existed.

## Configuration match and indexing of the existing reproduction

The exact folder was obtained from the retained [R1 raw-data index](context/R1/RAW_DATA_README.md):

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\R1_CLIPPING_AND_SPECTRAL_AUDIT\RUN_01\seed2038_eps1`

Its [configuration](records/R1_seed2038_eps1/configuration.json) matches the selected historical driver: seed 2038, N=80, B=4, X range [−5,5], R range [0,.3], k=5, alpha=.05, beta=.15, lambda_H=.05, L_base=9, **width=2**, eta=.001, horizon=None, breathing=true, epsilon=1, initial pass=0. The requested duration is the deliberate difference: **600 instead of 200 passes**. There is no change of engine at boundary 200.

| Record | Index meaning |
|---|---|
| X.npy, V.npy, R.npy | Row s is the completed state after s updates; s=0…600. X/V shapes 601×80×3; R 601×80. |
| Q.npy | Row k is post-H, pre-RPCO resonance during pass k+1. Fusion consumes this resonance. |
| positions_at_rpc.npy | Post-fusion, pre-noise coordinates at the RPCO interception stage; 600×80×3. |
| actual_rpc_output.npy | Actual signed RPCO result for each pass, 600×80. |
| noise.npy | Previously captured positional noise draws; included as historical R1 records, not regenerated. |
| L_used.npy, incoming_mean_abs_R.npy | Row k belongs to pass k+1 and reads incoming state k. |
| band_id.npy, natural_freq.npy | Fixed labels/frequencies for stable point IDs 0…79. |
| pass_diagnostics.csv | R1's retained 600 per-pass observer/diagnostic rows; reused rather than reaudited. |
| rng_initial.json, rng_final.json | Existing checkpoints included unchanged; not restored or sampled. |
| source_lock_times.json | Band 2 at pass 3, band 3 at 4, band 1 at 5, band 0 at 7: first threshold crossings, not motion stops. |

States 0–200 are **existing reproduced coordinates under the historical configuration**, not recovered original coordinates. The R1 completed-state-200 mean is exactly the displayed historical .5489832686504329. That is supporting aggregate agreement; the missing historical coordinates and RNG stream prevent a new assertion of bitwise historical trajectory recovery. States 201–600 are explicitly a later R1 extension. No simulation or extension was performed for this package.

## Earlier explanations retained without rerunning them

| Source | Scoped retained result / qualification |
|---|---|
| [R1 report](context/SRG_R1_REPORT.md) | Seeds 2038/42, epsilon 0/1, 600 passes: paired X/V/R/Q/noise equal; clipping inactive; L changes without effective feedback. Retained spectral-window critique. SIM06 uses only seed2038_eps1 as its principal coordinate record. |
| [R2 report](context/SRG_R2_REPORT.md) and [seed2038 summary](context/R2_seed2038/summary.json) | Eta=0 paired controls removed more than 99% of baseline net mean-resonance gain in those runs, while compaction persisted. Along-baseline budget: phi additions +1.4673904, sum +.2863984, difference +.4555357, exchange −.1704234, sine −.0156507, H +.0073086, RPCO offset ~6e−7; net +2.0305595. These budgets describe the path, not isolated causal shares. |
| Same R2 baseline | Q range .0232153…3.0240005, no empty/guard rows, fusion coefficient .0004643….0604800. Fusion did not increase whole-field Rg² in those 600 saved stages; local movement and noise did increase it in some stages. This does not establish monotonic total motion or a universal theorem. |
| [R3 report](context/SRG_R3_REPORT.md), [mathematical review](context/R3/MATHEMATICAL_REVIEW.md) | Further eta=0, H-off controls left final mean changes −.19990% / +.15538% for the two seeds; H accounts for most residual amplification in that changed-control comparison. Passive division by the H-product is not an actual H-off path. Conditional centroid/variance results are prior work, not new SIM06 proofs. **The retained R3 report explicitly returns itself for GPT review and claims no R3 acceptance.** |

R2's supplied baseline geometry tables identify **seed2038_eps0**, not eps1. They are included as prior context; reuse for the selected coordinates relies on R1's already established exact paired equality. Only the state-0 whole-field radius and initial mean R are reused from that summary; later whole-field radii and means come directly from the selected eps1 R1 diagnostics. New band decomposition and graph descriptions use the selected eps1 X array itself. No other trajectory was loaded for fresh analysis.

All old reports retain their historical proposed actions and “new run” descriptions unchanged. Those refer to their own earlier assignments and grant no authority to execute them here.
