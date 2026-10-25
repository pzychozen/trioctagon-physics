# Original evidence and generating drivers

The seven named originals match every identity in [TARGET_SOURCE_INDEX.json](handoff/TARGET_SOURCE_INDEX.json). This establishes which bytes are being interpreted. Attribution below additionally uses the complete source's explicit CSV writes, field names, driver settings, row counts and the original note's file list. No historical execution environment or missing coordinate path has thereby been recovered.

S means [the original source](original/srg_condensate_breaking.py); N means [its original narrative](original/SRG_Infinity_Part_II_Breaking_The_Condensate.md). CSV data rows are numbered from 1 **excluding the header**; physical file line=data row+1. The [passive inspection results](derived/TABLE_INSPECTION.json) preserve all schemas, ranges, missing cells, label changes and selected raw rows.

## Source-to-output map: all five tables

| Original table | Generating driver / write | Settings and row meaning | Retained schema / limits |
|---|---|---|---|
| [full_universe.csv](original/full_universe.csv) | `experiment_full_universe`, S:663–758; write 757 | **Main record:** N=120, seed 1618, h=6, multi_freq=true, breathing=true; 200 completed passes | 200×15, pass 1…200 once each, no missing cells. Full schema below. No initial state or coordinates. |
| [causal_horizons.csv](original/causal_horizons.csv) | `experiment_causal_horizons`, S:378–497; write 484 | Four seeded 20-point populations; h=[3,5,8,12,20,None], three trials with seeds 42,43,44 each; 100-pass endpoints | 18×11: horizon,trial,n_spatial_clusters,n_resonance_clusters,entropy,separation_ratio,mean_inter_dist,min_inter_dist,mean_intra_spread,intra_uniformity,inter_R_diversity. No missing cells. `999` means None, not a radius of 999. |
| [condensate_perturbation.csv](original/condensate_perturbation.csv) | `experiment_perturbation`, S:273–371; write 358 | N=50, seed 2038; no horizon/frequency option/breathing. Evolve 100; seven kicks to ID 0, each followed by 50 updates at passes 101–150 | 7×7: delta,delta_over_Req,initial_deviation,final_deviation,n_oscillations,decay_time,response_type. One blank: row 2 decay_time. Individual response time series are constructed temporarily but not written. |
| [multi_frequency.csv](original/multi_frequency.csv) | `experiment_multi_frequency`, S:504–576; write 575 | N=60; single vs multi; three trials, seeds 42–44; horizon=None, breathing=false; 150-pass endpoints | 6×7: type,trial,n_bands,dominant_ratio,n_resonance_clusters,entropy,R_max. No missing cells. Detailed band counts/means are printed, not saved in this CSV. |
| [breathing_condensate.csv](original/breathing_condensate.csv) | `experiment_breathing`, S:583–656; write 654 | N=50, seed 2038 reset for each of static/breathing; horizon=None, multi_freq=false; 200 passes | 2×9: type,R_drift,R_diversity,dom_freq,dom_fraction,entropy,R_max,R_std,n_resonance_clusters. No missing cells. These are summaries, not the R_max or L time series. |

All drivers retain alpha=.05, beta=.15, lam_H=.05, k=5 and base_L=9; ordinary constructor ranges are X=[−5,5], R=[0,.3]. Driver-supplied clustered positions replace the uniform X in the two clustered experiments. No driver here uses a hash-derived seed. No interleaved live field instances appear. Seed=None in clustered constructors preserves the explicitly seeded global stream; it does not mean the driver's setup lacked a seed.

## Selected full-universe initialization: draw order matters

The source-faithful setting is recoverable, though actual initialization arrays and historical software versions are not saved. S:675–702 performs these operations in order:

1. Reset global NumPy RNG to 1618.
2. Generate six 20×3 normal clouds, coordinate standard deviation 1.5, around (+8,0,0), (−8,0,0), (0,+8,0), (0,−8,0), (0,0,+8), (0,0,−8); stack them in this order. These are **prescribed population centers**, not measured final geometry.
3. Construct `GlyphFieldUniverse(120,horizon=6,multi_freq=True,breathing=True,seed=None)`. Its ordinary uniform X draw, uniform R draw and frequency-choice draw **all occur**, even though X and R will be replaced. The frequency catalogue/order is the one in S:78–80.
4. Replace positions with the prepared clouds; draw a **fresh** uniform [0,.3] R vector and replace resonance. Retain the constructor's frequencies, zero V and pass 0.
5. Evolve 200 calls, collect metrics and export the complete aggregate history. Per-population analysis and pairwise center-distance statuses are printed afterward but are **not added to the CSV**.

Skipping discarded constructor draws would change the stream. Simulating just an initializer to discover its arrays is outside this order. There is no stored exact frequency membership, starting X/R, RNG checkpoint, intermediate fusion center or environment receipt. Source choices are attributed configuration, not metadata independently certified by each CSV row. The source/output mapping is strong; exact numerical replay equivalence was not tested here.

The full table's 15 columns are pass; R_max,R_min,R_mean,R_std; n_resonance_clusters,n_spatial_clusters; entropy,mean_grf,top_seed_id,L_effective; and band_0.1508,band_0.2440,band_0.3948,band_0.6388. All observer values describe the completed pass, including noise for X/V. L_effective records the prescribed value used at that pass. The frequency column names are rounded display labels for exact assigned frequencies. This record contains no X/Y/Z coordinates or graph memberships despite the note calling it a “trajectory” at N:165.

## Horizon driver: endpoint geometry summaries with important distinctions

S:388–413 supplies four Gaussian populations around the listed tetrahedral corners. Each trial resets seed 42+trial **inside each horizon setting**, draws the four clouds, constructs a default field with seed=None (consuming discarded uniform X/R draws), replaces X and draws replacement R, then performs 100 updates. multi_freq and breathing remain false.

Rows 1–3,4–6,7–9,10–12,13–15 correspond to finite h=3,5,8,12,20; rows 16–18 to None. Every finite-horizon endpoint records five average-linkage spatial groups; every None endpoint records four. Mean pair distance between the **four original ID-block centers** ranges 13.87555–14.25550 across finite rows and 8.22412–9.17227 for None. Those are real recorded separation statistics. They support substantial finite-time separation without requiring reconstruction of coordinates.

The old note says the initial geometry was preserved because fusion was too weak (N:41). The supplied starting centers, the remaining separation and the different branches are known. Complete geometry preservation and a causal explanation of the distance changes are not established by endpoint summaries. In particular, h=20 still uses ordered local fusion, while None uses all-point global fusion; this is not a one-variable cutoff experiment with otherwise identical rules.

Per trial, all stored values other than h are exactly identical as CSV strings for h=5,8,12,20. This is an equality of **reported summaries**, not proof of identical states or neighbor histories. The nearest-five cap helps explain why “large radius” need not mean all-to-all local exchange; the actual selected graphs are absent.

The `mean_intra_spread` calculation is `np.std(final_pos[idx])` (S:436–442), pooling all coordinates of a population around a single scalar mean. It is **not** radius about that population's 3D center. It can contain differences between the center's x,y,z coordinates and need not be invariant under arbitrary spatial translation/rotation. Therefore `separation_ratio = mean_inter_dist/(mean_intra_spread+1e−8)` should not be promoted to a clean inter-center/within-cloud-radius ratio. This limitation does not invalidate the separately saved mean/min inter-center distances. Population-label uniformity/diversity likewise uses the original 20-ID blocks, not the hierarchical cluster memberships.

## Supporting experiments: what the recorded words mean

**Perturbation, S:278–369.** The 100-pass X/R arrays are saved temporarily, but uniformity is only asserted by a print of R_equilibrium[0]. Before each kick the driver restores X/R, zeros V, clears history and resets p=100. It **does not restore the RNG state**, so successive kick strengths use successive noise segments. Delta is added to ID 0; no “following” or restoring mechanism is inserted. `initial_deviation` is the deviation after the **first** post-kick update (p=101), not the instantaneous kick. `final_deviation` is its absolute value after 50 updates (p=150). `decay_time` is the first sampled deviation below 10% of that first post-update deviation, and not a fitted time constant or a guarantee it stays below.

| Delta | First recorded deviation | Final absolute deviation | Saved decay time | Saved response / peak count |
|---:|---:|---:|---:|---|
| .01 | .01222235 | .000852428 | 15 | DECAYING / 1 |
| .05 | .04614415 | .00746410 | blank: threshold not reached | DECAYING / 0 |
| .1 | .08854641 | .00477875 | 25 | DECAYING / 0 |
| .5 | .42776445 | .00657757 | 18 | DECAYING / 0 |
| 1 | .85178699 | .00686862 | 17 | DECAYING / 0 |
| 2 | 1.69983209 | .02730187 | 17 | DECAYING / 0 |
| 5 | 4.24396737 | .07148756 | 17 | DECAYING / 0 |

Every final deviation is smaller than its first recorded value. None meets the source's ABSORBED test `final < .001*max_recorded_deviation`. Its `n_oscillations` is the count of peaks of **absolute deviation** above .001, not a spectral mode count; one saved peak occurs at delta=.01. Response classification tests ABSORBED first, then >3 peaks, then final>.5*initial, then DECAYING. The temporary response histories are missing, so these observer summaries cannot be independently recomputed. The original claim of absorption “of any size,” no excitation spectrum, and an infinitely strong RPCO restoring force exceeds these seven finite responses.

**Multi-frequency, S:514–575.** Single-frequency rows 1–3 have n_bands=1 and dominant_ratio=1 by assignment. Multi rows 4–6 retain four labels and final band-mean ratios 1.10766886,1.27975898,1.05919374. Golden spacing is inserted in the constructor. Labels do not mutate or disappear; n_bands counts unique fixed assignments, without a survival threshold. The modest finite ratios are useful amplitude observations, not proof of coexistence “at infinity” or spatial sub-condensates. Switching multi_freq also consumes an extra initialization draw and enables a sine, so differences cannot isolate the frequency kernel alone. The note's individual band means are not present in this six-row summary.

**Breathing, S:594–654.** Both rows have exactly identical stored numeric strings: R_max=.17915880037997323, R_std=.019352317339809178, diversity=.1292866900777187, four resonance-gap groups, among other summaries. The final amplitude spread is nonzero. R_drift is std/mean of the final **10 R_max values**, not an individual trajectory drift. Unlike Tower II's mean-only spectrum, this driver fits a quadratic to all 200 R_max values, subtracts it, then takes an rFFT of residual rows 51–200. The saved first-bin frequency 1/150 and fraction .91888455 are historical calculations, **not rerun here** and not an autonomous-oscillator diagnosis.

The equality supports “no difference in these reported summaries.” It does not establish all-state equality, absence of clipping, or that decay of the bound caused the null difference. A fresh clipping/FFT experiment is neither performed nor needed for this construction account. The bound is an amplitude limit, and its imposed oscillation has a decaying envelope; it is not the location of a moving wall.

## Historical claims and evidence: compact register

| Claim / original locator | Source operation / original row | Supported narrower result | Unresolved or contradicted extension |
|---|---|---|---|
| “Uniform condensate / ground state” (N:10,99) | S:284 prints one R value as uniform; breathing rows 1–2 have R_std=.0193523 | Finite configurations can have slowly changing maxima and reduced spread | No physical energy functional, universal common amplitude or infinite-time ground-state proof |
| “All perturbations absorbed; no ringing” (N:20–33,126) | Perturbation rows 1–7; source classifiers 318–340 | All final deviations lower than initial recorded deviations | All seven labels are DECAYING; one peak, one missing decay time; neither all sizes nor excitation-spectrum claim tested |
| “Initial geometry preserved, horizons enrich it” (N:39–43) | Horizon rows 1–18; global/local switch 178–192 | Five versus four threshold groups and finite population-center separation | Missing shapes/memberships; change also switches fusion, so no isolated radius causation |
| “Four frequencies emerge/coexist at infinity” (N:49–62) | S:78–83; multi rows 4–6 | Four supplied labels present at 150 passes, modest final mean ratios | No evolving frequency labels, unbounded-time evidence or recovered band-shaped spatial groups |
| “Breathing had zero effect because it died out” (N:68) | Breathing rows 1–2; S:98–103 | All exported numeric summaries agree | Cause, intermediate-state identity and clipping activation unavailable |
| “Six independent seeds” (N:76–91) | S:677–689 supplies six ID populations; full row 200 records 10 spatial groups, 4 resonance groups | The source retains six original populations; the observer counts are measured under different definitions | No contradiction needs to be concealed: six input populations ≠ ten average-linkage groups. Independence is not certified by either count |
| “C3 dim, minimum separation 10.2, diversity .236” (N:80–91) | Source prints six-ID-block summaries and distances at 712–755; they are not CSV columns | These quantities are attributable **narrative reports** of the driver’s print-style analysis | Raw population data/stdout/coordinates absent; cannot independently confirm figures or infer a symmetry-breaking fixed point |
| “Same initial conditions” for populations (N:91) | S:687–699 draws different positions, R and labels for each population | Shared sampling prescription/operators | Not identical realized initial arrays; differing endpoints do not alone prove a phase transition |

This register preserves the useful historical observations while keeping source-defined measurements separate from interpretations.

## Missing evidence and attribution boundary

The named R0 copies, retained source inventory, csv_evidence_summary.json and saved_data_checks.json supplied no explicit locator to a complete Universe coordinate/RNG history, original movie or later reproduced trajectory. R0 §5.2 already records aggregate-only limits; [BOUNDED_RECOVERY.json](derived/BOUNDED_RECOVERY.json) and [retained index excerpts](derived/RETAINED_INDEX_EXCERPTS.json) document this bounded follow-up. We did not survey the repository or another archive, and did not borrow Tower II/Infinity coordinates. The former archive-member source locator is absent, but the exact recovered original exists and matches its prescribed hash.

No pre-existing Universe reproduction is claimed in this package. All new numerical work is transparent reading, summarizing or plotting of the five fixed historical CSVs. Source/header and note dates are March 14, 2026; they are not verified execution timestamps. The original library versions and full runtime history remain unresolved.
