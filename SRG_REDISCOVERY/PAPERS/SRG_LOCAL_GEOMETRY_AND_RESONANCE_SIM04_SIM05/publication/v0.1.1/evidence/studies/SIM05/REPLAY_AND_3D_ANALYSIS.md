# Faithful replay and finite 3D behavior

**REPRODUCED / DERIVED, not an original historical full-state record.** The exact selected constructor, fixed seed2038 and all defaults ran for 200 passes in each of two fresh sequential Python processes. The reference and captured executions match bit for bit in initial state, all 200 boundaries, source metric outputs and every complete NumPy MT19937 checkpoint. This is a same-environment repeatability and external-recording check, not two independent trials. The separately written offline stage calculations address arithmetic/staging correctness.

Python 3.11.15, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.10.9; Windows CMD, conda `torment`. Full configuration and core hash are in [ENVIRONMENT.json](ENVIRONMENT.json); [RUN_BUDGET.json](RUN_BUDGET.json) records all 400 calls. Neither the original launcher nor any other simulation was executed.

## Exact records and comparison

[Captured NPZ](replay/captured/states_and_rng.npz) holds 201×50 X,R,D,V boundary states, pass indices, full boundary RNG keys/position/cached-normal state and explicit before/after checkpoints. [Readable glyph table](replay/captured/glyph_states.csv) has 10,050 records with stable row IDs. [Metrics](replay/captured/metrics.csv) preserve all 200 source observations. The corresponding reference NPZ and JSON are retained.

Of 4,200 pass-plus-metric scalar comparisons to the historical table, 2,985 are exactly equal as parsed, including all 200 pass labels; hence 2,785/4,000 non-pass entries are exact. All entries satisfy `abs(diff)≤1e−12+1e−10*abs(historical)`. The largest absolute difference is 3.3528735343679728e−14 in top-seed curvature at pass109. Integer IDs and both count columns match exactly at every pass. [Every comparison](analysis/historical_replay_per_pass.csv) is retained. This very close agreement strengthens source/run attribution without recovering original RNG provenance or proving every lost original coordinate matched.

## What each stage contributes

Each offline calculation starts from the saved incoming arrays. None of its computed endpoints is fed into a subsequent calculation. [Intermediate terms](analysis/intermediate_terms.npz) retain every local increment, field exchange, cross term, H effect, pre/post-RPCO value, actual intermediate fusion center and fusion increment, clipping/sign flag, and position residual. [Stage summaries](analysis/stage_summary.csv) report RMS and discrepancies per pass.

Conditional R and D outputs agree **exactly** with all saved endpoints. Independently recomputed, correctly staged source metrics differ by at most 6.67e−16. Position decomposition has zero reconstruction discrepancy, but this last check is algebraic because the residual is defined as observed X minus deterministic stages. It is not an independent test of the actual random draws. Complete RNG checkpoints preserve the random-stream context; the residual arrays are not labeled captured noise draws.

| RMS over all 200 passes and 50 glyphs | R channel | D channel |
|---|---:|---:|
| Local exchange increment | .00193125 | .0000125632 |
| Cross increment | .000000916849 | .0000936760 |
| H increment | .000363688 | .000000744239 |
| R-only sine increment | .000108243 | Not present |

The cross increment is about 7.46 times D's local-exchange RMS, but only .000475 times R's local-exchange RMS over the complete run. These aggregate ratios hide the late regime: over passes181–200, local R and D differences have become tiny, and cross/local RMS ratios are about 2245 and 21522. Absolute late cross RMS remains approximately 9.35e−7 in R and 9.11e−5 in D. These are path-specific stage budgets, not causal comparisons against a gamma-zero run. [Window table](analysis/stage_windows.csv) preserves early/late definitions and exact values.

The cross coefficient changes sign at passes7,20,33,46,58,71,84,97,110,123,136,149,161,174,187,200 relative to the preceding pass. Both incoming channels remain positive, so the signs of their cross increments follow this coefficient. This alternating contribution is distinct from a field changing sign.

![Stage contributions](figures/F03_SIM05_stages.png)

H is still the source function at late passes. In the final20 updates its multipliers round to one in this environment, making the measured H increments exactly zero. Log plots omit these zero values; disappearing lines do not prove that H is mathematically zero. Cross-coupling, R sine, local motion, global fusion, RPCO offsets and positive noise scale continue. At pass200 sigma=1/300. Earlier H effects remain embedded in the state and later geometry; a small direct late term does not erase that history.

## The second field: small, structured and not extinguished

D is positive in every captured state; no R or D sign changes occur. Across all 201 states D ranges from 6.8798343e−5 to .0031323365. This includes the initial state, which has not yet been compressed. The three lower-bound events are all D at glyph12: passes16,17,18. Pre-RPCO values are .0001213000190, .0000701496654, .0000981461348; each outputs exp(−9)=.0001234098041. R has no lower/upper activations; D has no upper activations. [Clip event table](analysis/clipping_events.csv).

At pass200, individual D/R ratios span .0043810–.0081661 (roughly .44–.82%). The square-root ratio of total squares is .00609269. The source's squared-sum ratio is only .0000371209 (about .003712%); these statistics are different. D has very small within-component spread and different component means. The endpoint's positive small magnitude does not establish monotonic suppression, phase orthogonality or a physical dark-matter fraction.

![Second field](figures/F04_SIM05_second_field.png)

## Components, global coupling and motion

Graph components refer to adjacency reconstructed from each saved X; that graph drives the **next** update. Weak components ignore edge direction; strong components require reachability in both directions. These are graph properties, distinct from the source seed-candidate filter and echo-pair counter.

| First saved pass with weak count | Count | Sizes in stable label order |
|---:|---:|---|
| 0 | 1 | 50 |
| 5 | 2 | 44,6 |
| 21 | 3 | 11,33,6 |
| 30 | 4 | 11,23,10,6 |
| 33 | 5 | 11,13,10,10,6 |

The five-way partition persists through pass200. Strong components continue changing; fixed weak membership does not freeze the directed internal graph. The smallest fifth/sixth neighbor cutoff gap is 2.35194e−8, with no self edges or cutoff ties in the captured states. Exact neighbor arrays and component labels are supplied.

| Final weak component (full IDs in data) | N | Mean R | Mean D | Spatial diameter |
|---|---:|---:|---:|---:|
| Contains ID0 | 11 | .146059866 | .001054256 | .0225866 |
| Contains ID3 and final leader31 | 13 | .176329059 | .000820165 | .0261401 |
| Contains ID4 | 10 | .157485460 | .000689956 | .0267620 |
| Contains ID7 | 10 | .144195035 | .001177508 | .0280647 |
| IDs10,15,27,30,33,47 | 6 | .107404758 | .000775994 | .0179343 |

All five are compact relative to whole-field diameter3.84314, but they are separate points, not merged entities. The population variance decomposition gives R total variance .000417872792 and within-group variance 2.75e−20. For D, more than 99.999999% of the final variance is between component means. Finite near-equality within each group explains why the whole field can retain substantial spread. It does not prove exact consensus or permanent separation.

Global fusion reads all five groups. Local disconnection therefore does not make their complete dynamics independent. The actual intermediate center is retained in the data but not plotted; no endpoint weighted center is substituted. Whole-field Rg changes from5.38637 at pass0 to1.83889 at pass200. Final covariance fractions are .434617,.354187,.211196, showing spread in all three directions without establishing a surface or named solid.

![Geometry and motion](figures/F05_SIM05_geometry_and_motion.png)

The longest uninterrupted leading-ID interval is ID3 at passes68–101: it travels .606589 in summed saved-step length and .524948 between endpoints. The final leading ID31 holds only passes196–200 and travels .040128 in those four increments. Mean displacement at pass200 is .00949221; maximum displacement is .0159962. Rank stability and small amplitude variation coexist with movement. Changes in the leading coordinate stream must not be mistaken for individual jumps when the ID changes.

## 3D selection and rendering conventions

The whole field uses passes0,20,100,200 with common [−5.5,5.5] bounds on all axes. The two close views select final components containing the highest-|R| and lowest-R points, with fixed membership traced backward. The 13-point set is an actual component from pass33 onward, so its pass20 view is explicitly a retrospective subset. The six-point set is an actual component from pass5 onward. No other close-group search or extra group view was performed.

![Two selected groups](figures/F02_SIM05_selected_groups.png)

Close views subtract each group's arithmetic centroid and divide by its own Rg. All use the same coordinate orientation and equal axes, without PCA alignment or changing identity assignment. Colors identify fixed glyph IDs, except the explicitly labeled field-amplitude heatmap and final-component scatter. Lines in diagnostic charts connect discrete samples; they do not supply unseen within-pass trajectories. Overlapping projected markers are a scale/projection effect. There are no coordinate seams or wrapping operations in this program. Figure data and conventions are indexed in [FIGURE_REGISTER.md](FIGURE_REGISTER.md).
