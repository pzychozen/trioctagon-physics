# SIM07 — Universe/condensate construction and original-aggregate review

**Date:** 25 October 2026  
**Author and research director:** Hilmir Frímann Halldórsson  
**Scientific reviewer:** GPT  
**Submitted research engineering:** Codex  
**Disposition:** **ACCEPTED_WITHIN_HISTORICAL_SOURCE_AND_ORIGINAL_AGGREGATE_SCOPE**  
**Required scientific revisions:** **None**  
**Status:** Research acceptance only. No new replay, merger study, paper, ledger edit, publication or Git action is authorized or executed by this receipt.

## 1. Decision

The submitted SIM07 construction study accurately explains the selected `GlyphFieldUniverse` implementation, its five experiment drivers, and their five original numerical outputs. Its central finding survives independent source inspection: with a finite horizon, the fusion loop reads coordinates already changed by earlier rows in that same pass, while retaining the incoming adjacency. Without a horizon, the code computes one all-point center and applies a simultaneous displacement. These are different update rules, not merely different radius settings.

The reports properly separate what the original source specifies, what the original CSVs record, what the old narrative asserts, and what remains unavailable. Their figures are plots of recorded aggregates, not invented spatial geometry. The optional replay note remains a proposal, not an implementation or run.

This acceptance does **not** certify a complete historical point trajectory, historical execution environment, numerical order sensitivity in the original run, persistence of particular spatial memberships, or the original note's broader physical interpretations. Those are not required to accept this source/aggregate checkpoint. No scientific defect requiring a revision cycle was found.

## 2. Inputs and independently checked integrity

Submitted ZIP:

- File: `SRG_SIMULATION_STUDY_07_UNIVERSE_CONSTRUCTION_01_REVIEW.zip`.
- Bytes: **571,721**.
- SHA-256: `c807e6134d28bc02307b0e93ed2918e6eb71a5f8bfb94af4d83773dc23afe049`.
- **52 unique file members:** 51 manifested payloads plus `MANIFEST.json`.
- Payload bytes excluding manifest: **1,020,103**.

The external ZIP-identity receipt matches the actual uploaded ZIP and included manifest; CRC passes. Every extracted file matches its corresponding ZIP member, and all 51 listed sizes and SHA-256 values match. There are no missing, extra or duplicate payload paths. The separately uploaded starting guide matches its archived copy.

The seven originals match the exact expected identities in the prior handoff's target-source index. The 10 baseline input snapshots available here match their recorded identities, including the actual previously supplied handoff ZIP. All 12 copied archive members match their supplied parent archive or its nested accepted SIM06 package. The before/after preservation receipt retains those baseline identities consistently.

**Qualification:** I did not access Hilmir's Windows filesystem. These are checks of delivered byte streams and preserved baselines, not a new live audit of the original Windows paths. Codex's preservation and zero-execution statements remain its operational attestations; matching hashes alone cannot prove that no program ran.

References: [payload identities](independent/PAYLOAD_IDENTITIES.json), [full audit](independent/VERIFICATION.json), [submitted baseline](source_package/INPUT_BASELINE.json), [submitted preservation receipt](source_package/PRESERVATION_RECEIPT.json).

## 3. Independent review method and result

The complete **778-line original source** and **170-line original narrative** were read. Source was parsed as text/AST only: it was not imported, compiled for execution, instantiated or called. The reports, source maps, work order, selected earlier context, original CSVs, derived tables, rendering source and both PNGs were inspected.

A newly written, standalone passive auditor independently read all original CSV cells and reproduced the submitted schemas, missing-cell locations, numeric ranges, selected row values, label-change lists, ratio calculations, horizon summaries and reported equalities. It did not execute the submitted inspector, simulator, clustering observer, peak detector, FFT or RNG code.

| Check | Result |
|---|---|
| Main chronology | 200 rows, 15 columns; passes 1–200 exactly once; no state-0 row or missing cells |
| Horizon table | 18 rows, 11 columns; six configurations × three trials; endpoint records, not a time sequence |
| Perturbation table | 7 rows, 7 columns; its one blank is row 2 `decay_time`, retained as missing |
| Frequency table | 6 rows, 7 columns; two modes × three trials |
| Breathing table | 2 rows, 9 columns; static/breathing exported numeric strings exactly agree |
| Complete CSV corpus | **233 data rows, 3,307 cells: 3,291 finite numeric cells, 15 text cells and one blank** |
| Submitted passive summaries | All five schema/range accounts, ten selected rows and three label-change sequences agree |
| Horizon summary CSV | Six configuration-summary rows verified; the renderer reads all 18 original trial rows directly |
| Source-to-output mapping | All five explicit CSV writes and driver settings agree with the report |
| Root-document navigation | All **56 checked relative links** resolve |
| Final figures | Both identities/dimensions match; both inspected at native size |

The final audit records 3,446 successful low-level checks, many of which are ordinary per-cell finiteness checks; this is **not** a count of independent experiments or mathematical proofs. Initial comparator assumptions about metadata, missing-cell representation and the six-row summary CSV were corrected in the independent auditor. Their history is retained under [audit development](independent/audit_development/README.md). No submitted scientific file was changed to make a check pass.

References: [audit method](independent/review_sim07.py), [verification](independent/VERIFICATION.json), [schema/ranges](independent/SCHEMAS_AND_RANGES.json), [findings](independent/FINDINGS.json), [source map](independent/SOURCE_MAP.json), [numbered source excerpts](independent/SOURCE_READBACK.md).

## 4. The actual construction is correctly recovered

The selected engine carries positions, one real resonance array, fixed assigned frequencies, the pass counter, configuration and RNG state. Stored velocity is a completed displacement used by an observer, not momentum consumed by the next movement. The literal `gamma_srg=.08699` is assigned but unused; this engine does not retain Infinity's second real channel.

One pass consists of:

1. Increment the pass and copy incoming positions for the displacement diagnostic.
2. Build distances and directed selections from incoming positions. A finite horizon uses a strict radius filter followed by a cap of five nearest non-self neighbors. Empty rows are possible. `None` removes the radius filter but retains the cap.
3. Apply simultaneous local movement from an unweighted neighbor-position average and a componentwise `tanh` term.
4. Exchange incoming amplitudes synchronously using normalized inverse-distance weights; optionally adjust those weights by ordinary squared frequency differences and apply each point's supplied frequency sine. Empty/guard-skipped rows skip the exchange and that sine.
5. Apply the common scheduled H multiplier.
6. Apply finite-horizon ordered local fusion or no-horizon simultaneous global fusion, using post-H/pre-compression amplitudes.
7. Apply signed log/exp clipping with the selected prescribed bound; add decaying positional noise; record displacement and aggregate observations.

The reports retain the subtle but important details: two normalization stages in the frequency kernel; a strict `>1e-10` second-normalization guard; direct self-exclusion in the neighbor selection; absolute weights in a center but signed resonance in its displacement coefficient; no distance weights in the fusion center; and post-update observation. `_record(adj,dists)` receives old adjacency and distances but does not read those arguments.

### Ordered coordinates, frozen selections

During finite-horizon fusion, rows are visited in ascending index order. At row i, an earlier selected row j may already have its fusion displacement, while a later selected row still has its post-local-movement coordinate. The neighbor set itself is not recomputed. The amplitude array stays fixed throughout this stage.

The supplied symbolic read/write trace correctly exhibits possible indirect dependencies through earlier writes. Direct self-exclusion does not rule out indirect dependence on one's own earlier coordinate through another row. It does not establish that such paths caused a particular nonzero effect in the missing historical trajectory.

No reordered update was evaluated, and none is needed to identify which array the original source reads. Replacing this loop with a simultaneous vectorized operation would be a model change, not an archival correction.

### The horizon has a narrower meaning than a physical propagation limit

A direct selected pair lies within the specified radius **at the incoming boundary**. That constraint is not rechecked after the local movement or earlier fusion writes. Several selected links can relay dependence within the ordered stage. Consequently the source is not a one-hop-per-pass physical speed-limit construction.

For fixed incoming selections in the finite-horizon branch, no band-wide or global data-derived center bridges disconnected weak components. This differs from Tower II. It is a conditional description of dependencies, not evidence that the six seeded populations are disconnected components or permanently independent. Common schedules, shared RNG bookkeeping and all-field observers must not be confused with an extra state-dependent center.

Source anchors: original lines 60–103, 105–153, 155–203 and 205–266. See [construction](source_package/CONSTRUCTION.md).

## 5. What the original 200-row record establishes

The selected full-universe driver sets N=120, seed 1618, horizon 6, multi-frequency enabled and prescribed breathing enabled. It supplies six initial 20-point Gaussian populations centered on the positive and negative coordinate axes. It then consumes the ordinary constructor's uniform position and resonance draws and assigned-frequency draw, replaces the positions, draws replacement amplitudes, and advances 200 passes. The apparently discarded constructor draws matter to faithful future reproduction.

Those six initial populations are an input arrangement, not six spatial groups discovered by an initially unstructured field. The source note's population descriptions and the CSV's threshold-defined groups answer different questions.

| Saved pass | Spatial observer count | Amplitude-gap count | Minimum magnitude | Mean magnitude | Maximum magnitude | Mean GRF |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 49 | 2 | .016266423 | .152135728 | .289449182 | .830615833 |
| 16 | 10 | 1 | .065993224 | .148956413 | .210481398 | .961797403 |
| 20 | 10 | 1 | .066921251 | .146822502 | .204801852 | .973228288 |
| 200 | 10 | 4 | .077696148 | .144070881 | .200645840 | .994912594 |

The spatial observer reaches ten groups at pass 16 and reports ten at every remaining saved pass: **185 consecutive observations**. It uses average-linkage clustering cut at distance 2.0. This is not the update's nearest-neighbor graph, and constant counts do not establish constant membership, shape, separation, motion or independence.

The main record contains positive amplitude minima, unequal extrema and `mean_grf<1` at every saved pass. The source defines GRF as the mean of `1/(1+||V_i||)`. Its being below one supports some nonzero completed displacement at each recorded pass. It does not recover directions, individual speeds or their arithmetic mean, and the reciprocal of the mean cannot be substituted for a mean speed.

At the endpoint, the recorded signed standard deviation is .040448472 and mean magnitude .144070881; their ratio is **.280753973**. The amplitudes remain appreciably nonuniform. The plot of this ratio falls early, reaches its recorded minimum **.252568769 at pass 13**, then ends higher. The record does not support monotonic relative equalization across its entire duration.

### Particularly useful observer example

At pass 20, the report says **one resonance cluster**, while maximum magnitude is **3.060341 times** minimum magnitude. This is not a contradiction. The source sorts magnitudes and counts adjacent gaps greater than five percent of the largest magnitude. No qualifying adjacent gap does not mean the two endpoints are equal. Many smaller gaps can span a broad range.

This directly explains a historical label from its own source and saved numbers; no hypothetical trajectory or revised detector is needed.

References: [original full table](source_package/original/full_universe.csv), [motion/evidence account](source_package/MOTION_AND_GEOMETRY.md), [independent values](independent/FINDINGS.json).

## 6. Horizon comparison and the limits of the old geometry statistics

All 15 finite-horizon endpoint rows report five average-linkage groups; the three no-horizon rows report four. Mean pair separation of the four **original population centers** is approximately 13.88–14.26 in finite settings and 8.22–9.17 with `None`. These are positive, useful original spatial summaries.

For each trial, all saved fields other than horizon are exactly identical as CSV strings at h=5,8,12,20. This establishes equality of those summaries, not coordinate equality or identical graph histories. The no-horizon sentinel 999 is a serialization convention, not radius 999.

The switch from finite h to `None` also switches fusion branches. Thus the comparison cannot isolate a radius-only causal effect. The nearest-five cap remains active even with `None`; amplitude exchange does not become all-to-all simply because fusion uses a global center.

### The flattened-coordinate spread is not a cloud radius

The submitted report correctly flags `np.std(final_pos[idx])` in the horizon driver. With no axis specified, it treats every x, y and z entry as one scalar list. It does not measure distance around the cloud's vector center.

A short exact identity makes the issue transparent. Let a population have n points x_i in R^3, vector center mu, scalar m=(mu_x+mu_y+mu_z)/3, and squared radius of gyration Rg²=(1/n) sum_i ||x_i−mu||². The squared flattened population standard deviation is

**s_flat² = Rg²/3 + [(mu_x−m)²+(mu_y−m)²+(mu_z−m)²]/3.**

Expand each coordinate difference as `(x_id−mu_d)+(mu_d−m)`; the cross term vanishes because the deviations from each coordinate mean sum to zero. The first term is the true centered spatial spread divided by three; the second depends on the vector center's components.

This is an additional **source-derived explanatory identity**, not a numerical recomputation of unavailable geometry. It explains why moving an unchanged cloud by an arbitrary vector can change this old spread measure. The reported average over four populations and its separation ratio inherit that qualification. The independently recorded inter-center distances remain meaningful. Do not silently replace the historical statistic and relabel the replacement as original evidence.

Source: original lines 422–445. See [original evidence account](source_package/ORIGINAL_EVIDENCE.md).

## 7. Other historical outputs: useful observations retained, stronger labels corrected

**Perturbations.** All seven retained response labels are `DECAYING`, and each final absolute deviation is smaller than its first recorded post-kick deviation. Final/first ratios range from about .00806 to .16176. One response has one peak of absolute deviation; one has no recorded time at which it first fell below the 10% threshold. The actual response arrays and their maxima are not saved, so this review does not independently recompute the `ABSORBED` classifier. The CSV plainly does not report that label. The driver's X/R/clock reset also does not reset RNG state between kick sizes. The record supports finite reduction, not absorption of all sizes under identical noise or a proof of an excitation spectrum.

**Frequency comparison.** Four catalogue values are assigned independently at initialization when enabled; they do not evolve. The six-row table records final ratios of band means, but the retained count of labels is not an independently tested survival process. Enabling the option also consumes a frequency-choice draw and activates a per-label sine; it is not a controlled change only to the weighting kernel. The supplied golden spacing is an implementation choice, not a spacing discovered in the record.

**Breathing comparison.** All exported numeric strings agree between the static/breathing summary rows. Neither full coordinate paths nor clipping-activation histories accompany them. Their equality does not establish why the bound made no reported difference. The first nonzero spectral bin in the source's 150-sample tail is not by itself an autonomous period; no FFT was rerun here. The Universe bound is prescribed from the pass counter, unlike Tower II's algebraic mean-resonance readout. The earlier Tower II inactivity result cannot simply be transferred to Universe.

The original narrative remains preserved as historical writing. The reports identify which strong statements it adds beyond the saved measurements without discarding the narrower measured observations.

References: [all five driver/output mappings and claim audit](source_package/ORIGINAL_EVIDENCE.md), [original narrative](source_package/original/SRG_Infinity_Part_II_Breaking_The_Condensate.md), [original CSVs](source_package/original/).

## 8. Figure and presentation review

Both figures were opened and inspected at native size:

- **F01**, 1560×1320: all 200 original aggregate rows; amplitudes, assigned-frequency means, two distinct group counters, reciprocal-displacement readout, prescribed clipping limit and relative amplitude spread. The six-population reference is explicitly identified as a source input, not a recovered geometric measurement.
- **F02**, 1560×672: all 18 horizon trial rows; the horizon axis is categorical, trials are not trajectories, `None` is explicitly distinguished, and the global/local branch division is marked. Population-center distances are not mislabeled as complete geometry.

Both figures are readable; no blocking clipping, misleading reconstructed positions or hidden rescaling was found. The existing figures were not regenerated. Their absolute source evidence and transformations agree with the rendering code and register.

[Figure register](source_package/FIGURE_REGISTER.json) · [independent visual receipt](GPT_VISUAL_REVIEW.json).

## 9. Creation history and comparison

The source and note explicitly state an intention to investigate how to add structure to an earlier “condensate” interpretation. That is genuine evidence of stated research motivation. It is not independent proof of exact execution dates, unique ancestry, the premise that the earlier Infinity run was uniform, or which surviving file was invented first.

The recovered mechanism map is now clearer:

- Seed Explorer/Infinity: one global center in the selected constructions.
- Tower II: centers shared across fixed assigned bands, possibly spanning local groups.
- Universe with a finite horizon: centers of selected neighbors, recomputed as positions are overwritten in order.
- Universe with no horizon: one global center again.

These comparisons describe actual source operations. They need no new physical identification or forced universal equation. Universe's one-amplitude construction and absence of an active gamma term also prevent treating it as simply the previous two-field Infinity run resumed with a radius switch.

## 10. Scope closure and next decision

**Close CONSTRUCTION_01 as accepted.** The lack of coordinates is an explicitly documented evidence boundary, not a defect in the reports. No corrective rerun is required.

For the broader goal of understanding actual motion, however, I recommend **one separately ordered source-faithful replay of the already selected full-universe setting before leaving SIM07**. This is a targeted way to fill the principal missing evidence, not a new model or an expansion to another archive family.

The submitted proposal is appropriately bounded in concept: two 200-update executions, reference and observed capture, at the same single historical setting; 400 total calls and only the two prescribed initializations. Preserve the complete original draw order, including discarded constructor X/R draws, fixed assigned frequencies, ordered fusion and the original observers. Record incoming neighbors, post-local positions, pre-fusion amplitudes, local centers/writes, completed state and RNG checkpoints. Do not substitute simultaneous fusion or run a reordered counterfactual merely to demonstrate an order effect.

A future order must define exact acceptance comparisons and historical tolerances **before execution**. It must not spend a third run on recovery, extend beyond pass 200, search seeds/parameters, or demand six groups. Results remain REPRODUCED even if aggregate agreement is close. The existing proposal neither recovers the original random stream nor authorizes execution on its own.

**No replay order is activated by this receipt.** No replay harness or simulator has been executed in this review. The agreed outer boundary remains this Universe construction, then the separately reviewed field-merger construction, followed by synthesis/paper decision. There is no reason to reopen either published volume or start a new theoretical program here.

## 11. Deliverables and non-execution statement

This review used archive inspection, hashes, text/AST reading, passive original-table summaries, exact algebra on an observer definition, and inspection of two existing images. **New state updates: 0. RNG draws/restorations: 0. Historical imports: 0. Submitted inspector/checker executions: 0. Reconstructed coordinate arrays: 0. New plots: 0. Git/publication/kernel changes: 0.**

The original ZIP, external identity receipt and unchanged extracted submission are preserved in this review package. The new review and independent results are separate. Acceptance does not silently rewrite the source, its old explanatory note, the submission's review-status wording or previous accepted studies.
