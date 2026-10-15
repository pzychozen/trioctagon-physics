# SRG-SIM04 — Finite-step collective-speed bounds

Research report v0.1 · 14 October 2026 · Submitted for GPT scientific review

Human research author and owner: Hilmir Frímann Halldórsson. Scientific direction and proposed fixed refinements: GPT. Independent mathematical verification, implementation and bounded saved-data analysis: Codex.

## Answer

The existing vector bound is valid on the complete prescribed population, but substantially overestimates the observed differences in collective mean speed. Retaining signed component information tightens it only modestly. The prescribed sorted-absolute-component profile bound gives a much stronger result: its aggregate standard-deviation upper bound is **3.88305 times** the observed value across all five cycles and **3.80087 times** across the four continuation cycles, compared with **18.4623** and **15.6041** for the vector bound.

That improvement does **not** certify phasewise dispersion nonincrease. The best analytic variance bound exceeds both reference variances at every phase in both views. The saved damping-stage variance nevertheless decreases at all 200 phases in each view. A sufficient condition that is not established does not imply expansion. After the profile refinement, mean residual slack is concentrated in projecting component differences to speed differences and in discarding signed cancellation across centers, rather than in the derivative interval estimate itself.

These statements concern the five recorded histories and fixed one-step inequalities. They do not establish convergence, a universal scalar contraction, or a mean-speed-only predictive law. The analysis made no new motion update.

## Sources, population and information boundary

All 13 required source files matched their supplied sizes, SHA-256 hashes, published manifest entries where applicable, and committed Git blobs at SIM03 checkpoint `e1f5115402a05965834493c1254b03118a531c92`. Their exact identities and roles are in [INPUT_MAP.json](evidence/INPUT_MAP.json). The decisive saved array is [center_decomposition.npz](inputs/analysis/center_decomposition.npz), 5,030,162 bytes, SHA-256 `28d312bfcd2941b87c8d51710f9b5fa1619ec7f1df325d7257083b462aba6b1a`. It was copied unchanged.

The source damping and gain definitions are in the retained [original C source](inputs/inputs/accepted_sim02/inputs/sources/source_C.py), lines 49 and 54; sequential centroid geometry and the velocity update are at lines 110–123. The retained [detached C core](inputs/inputs/accepted_sim02/inputs/detached/engine_C.py), lines 24, 29 and 60 onward, supplies the corresponding definitions. These programs were read as text, never imported or executed. [SIM03 report §§1, 5](inputs/SIM03_REPORT.md) and [GPT review §§4.3–5.2](inputs/review/SIM03_GPT_SCIENTIFIC_REVIEW.md) establish the inherited interpretation and indexing caveat. The [SIM04 mathematical specification](received/SIM04_MATHEMATICAL_SPEC_v0.1.md) proposes the refinements; [MATHEMATICAL_RESULTS.md](MATHEMATICAL_RESULTS.md) records the independent proofs written before evaluation.

The selected population is PREFIX dataset 0, updates 0–199, and REPEATED dataset 2, updates 200–999: **1,000 distinct updates and 8,000 labeled-center records**. The inherited prefix is counted once. Joins use `(dataset_id, update_index, center)`, not file order; cycle is `c=floor(n/200)` and phase is `j=n mod 200`. [selected_record_map.csv](analysis/selected_record_map.csv) retains original record identities. The complete input still contains CONTINUOUS records, but those records were excluded from scientific evaluation. No raw motion states or centroids were reconstructed.

All ten unordered cycle pairs were evaluated once: `(1,0), (2,0), (2,1), (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (4,3)`. At 200 phases this gives **2,000 pair/phase comparisons and 16,000 labeled-center pairs**. `all_five` uses all ten pairs; `new_four` reuses the six pairs with both cycle indices positive. Their 400 view/phase summaries are not another 1,200 bound evaluations.

Analytic functions accept only stored incoming velocity, impulse, pre-damping velocity, geometric difference, H, G and bit values. They have no outcome lookup. All bounds were saved and sealed before successor velocities or numerical reference readouts were joined. [PRE_OUTPUT_BOUNDS.npz](analysis/PRE_OUTPUT_BOUNDS.npz) has SHA-256 `5df03134e083e9879458eb8a0d560c3c1e9bd91f6a57b6d8c367e0a3ed749e6f`; the [seal](analysis/PRE_OUTPUT_BOUNDS_SEAL.json) and [access log](evidence/DATA_ACCESS_LOG.json) preserve this ordering. Outcome independence is an information-use boundary: the bounds still condition on realized sequential intermediates.

## Checked mathematics

Let brackets denote the average over eight labeled centers. For each history, `v` is incoming velocity, `a` the saved impulse, `w=v+a`, and `y` the saved successor. The inherited component rule is

\[
D(x)=\frac{x}{1+\log(1+|x|)},\qquad y=D(w).
\]

The source uses `g=(1−2 bit)d/(||d||+0.01)`, `a=αGg`, `α=0.1H`, and `G=1/(1+u)`, where `u=〈||v||〉`. Thus bit 0 has positive sign and bit 1 negative sign; `||g||<1`. H is common across cycles at each phase. These source equivalences were checked against the stored fields without recomputing H or changing bits. Native units are retained; no physical unit calibration is asserted.

For histories c>d write Δ for c minus d, `V=〈||Δv||〉`, `J=〈||Δa||〉`, `R_g=〈||Δg||〉`, `q̄_c=〈||g_c||〉`, and `h=|α|`. The measured target is `S=|〈||y_c||−||y_d||〉|`. The seven fixed families are:

| ID | Formula |
|---|---|
| OMEGA_COARSE | `(1+h)V+h min(G_c,G_d)R_g` |
| GAMMA_SOURCE | `min{V+h[\|ΔG\|q̄_c+G_d R_g], V+h[\|ΔG\|q̄_d+G_c R_g]}` |
| T_TRIANGLE | `V+J` |
| Q_VECTOR | `〈\|\|Δw\|\|〉` |
| K_COMPONENT | `〈\|\|κ ⊙ Δw\|\|〉` |
| P_PROFILE | `〈\|\|λ ⊙ [p(w_c)−p(w_d)]\|\|〉` |
| BEST_PRE | `min(K_COMPONENT,P_PROFILE)` per pair, before squaring |

Here `p(w)` sorts the three absolute components in ascending order. Put `b=1+log(1+s)` and

\[
k(s)=\frac{b-s/(1+s)}{b^2},\qquad D'(x)=k(|x|).
\]

For a signed component interval, κ is k at its nearest magnitude to zero; κ=1 if the interval contains zero. For profile components, `λ=k(min(p_c,p_d))`. Differentiation gives `k'(s)=[2s−(s+2)b]/[(1+s)^2b^3]<0`: setting `J_0=(s+2)b−2s` gives `J_0(0)=2` and `J_0'=log(1+s)+1/(1+s)>0`. Hence these coefficients are interval derivative maxima. This is a proof, not derivative-grid sampling.

Mean-value and triangle inequalities establish

\[
S\le Q\le T\le\Gamma\le\Omega,
\qquad S\le K\le Q,\qquad S\le P\le Q.
\]

The profile result uses sign/permutation invariance of the damped **scalar norm**, plus the fact that sorted matching minimizes Euclidean distance between nonnegative component lists. It neither relabels centers nor rotates trajectories. Arbitrary rotations are not damping symmetries: equal-norm axis and equal-component vectors generally have different damped norms. No universal ordering of K and P was assumed.

Cross-history difference alignment obeys

\[
\|\Delta v+\Delta a\|^2=\|\Delta v\|^2+\|\Delta a\|^2+2\Delta v\cdot\Delta a.
\]

This differs from SIM03's within-history `2v·a`. Q uses the stored Δw directly; T discards alignment by separating the norms.

For m scalar speeds, population variance is `Σ_{c>d}(u_c−u_d)^2/m²`, so any pair bound B gives `Var(u⁺)≤W_B=Σ B_cd²/m²`. The denominators are 25 and 16, not the unordered pair counts. For ε≥0, `B≤ε` suffices for the corresponding speed difference≤ε; `W_B≤ε²` suffices for SD≤ε. Comparing W_B separately with incoming variance or pre-damping variance gives sufficient conditions for the corresponding nonincrease. They depend on the realized inputs and cannot be iterated into a long-time theorem without further hypotheses.

## Tightness across the full population

Aggregate SD means `sqrt(mean_j variance_j)`, not mean phasewise SD. The following values are transcribed from completed [RESULTS.json](analysis/RESULTS.json); tables and arrays retain full float64 values.

| Family | All_five SD upper | Factor | New_four SD upper | Factor |
|---|---|---|---|---|
| OMEGA_COARSE | 0.203388833 | 22.02127 | 0.171469934 | 18.5383913 |
| GAMMA_SOURCE | 0.174866311 | 18.9330859 | 0.148457564 | 16.0504197 |
| T_TRIANGLE | 0.174573887 | 18.9014247 | 0.148169009 | 16.0192227 |
| Q_VECTOR | 0.170517914 | 18.4622773 | 0.144329765 | 15.6041446 |
| K_COMPONENT | 0.1673612 | 18.1204943 | 0.140885888 | 15.2318115 |
| P_PROFILE | 0.0358639518 | 3.88305374 | 0.0351559515 | 3.80086916 |
| BEST_PRE | 0.0358639518 | 3.88305374 | 0.0351559515 | 3.80086916 |

Observed incoming / pre-damping / post-damping aggregate SD is **0.00960406461 / 0.0128717164 / 0.00923601739** for all_five, and **0.00924945577 / 0.0128269730 / 0.00924945060** for new_four. Near equality of incoming and outgoing averages in the continuation view retains SIM03's one-step indexing constraint; it is not evidence of regulation.

Across individual pair/phase comparisons, factor-over-outcome distributions are:

| Family / S | Minimum | p05 | Median | p95 | Maximum |
|---|---|---|---|---|---|
| Q_VECTOR | 2.47459866 | 4.5524649 | 15.4768029 | 181.038876 | 146936.473 |
| K_COMPONENT | 2.45217 | 4.54317812 | 15.4045884 | 180.882425 | 146748.117 |
| P_PROFILE | 1.46588627 | 1.87353264 | 4.64616925 | 43.546681 | 42300.9828 |
| BEST_PRE | 1.46588627 | 1.87353264 | 4.64616925 | 43.546681 | 42300.9828 |

For Q, 0/135/605 of 2,000 comparisons lie within factors 2/5/10. For K the counts are 0/135/607; for P and BEST they are 179/1,083/1,559. Every factor and utilization denominator is resolved, and no pair outcome or bound is exactly zero. These nested descriptive categories are not significance levels. The complete seven-family statistics, including signed gaps, utilization and linear-quantile bracketing locators, appear in [bound_summary.csv](analysis/bound_summary.csv).

Phasewise SD factors also vary substantially. Q ranges from **7.45462 to 80.9244** in all_five and **5.98245 to 85.6565** in new_four. BEST ranges from **2.32558 to 14.3725** and **2.04164 to 24.4290**, respectively. BEST lies within factors 2/5/10 at 0/164/199 of 200 all_five phases and 0/162/197 new_four phases. All 400 phase denominators are resolved, with no zero observed variance. Variance-factor categories are stored separately and must not be confused with SD factors.

[Figure 1](plots/01_baseline_and_observed_SD.png) shows Q and observed SD in native speed units; [Figure 2](plots/02_fixed_refinements.png) compares the refinements on a labeled log scale; [Figure 6](plots/06_phasewise_tightness.png) shows all phasewise SD factors. No phase was removed or chosen for a favorable result.

## Alignment, refinement and remaining slack

There are 5,463 negative and 10,537 positive difference-alignment terms among the 16,000 center pairs; none is zero or cosine-unresolved. The mean direct triangle gap T−Q is **0.00424024257** in speed units, median **0.00116382628**, maximum **0.105668904**. Keeping combined vectors helps, but its aggregate tightening is modest compared with the profile refinement: the SD factors for T and Q are 18.9014 versus 18.4623 (all_five), and 16.0192 versus 15.6041 (new_four). [Figure 3](plots/03_difference_alignment.png) retains the full phase range and all center-pair alignment values.

K reduces Q by a mean **0.00227118738**, with median K/Q **0.995974441**. Of 48,000 signed component intervals, **23,992 contain zero** and therefore require κ=1. P reduces Q by a mean **0.116641488**, with median P/Q **0.306095461**. P is strictly smaller than K in all 2,000 recorded comparisons, so BEST=P throughout this population. This empirical ordering is not claimed as a theorem.

To locate residual inequality slack, saved successors supply `Z_signed=〈||Δy||〉`, `Z_profile=〈||p(y_c)−p(y_d)||〉` and `T_norm=〈| ||y_c||−||y_d|| |〉`. Choose Z_star from the branch that supplied BEST. Since increasing D preserves the order of nonnegative components, `p(D(w))=D(p(w))`; thus `S≤T_norm≤Z_star≤BEST≤Q`. The exact gap telescopes as

\[
Q-S=(Q-BEST)+(BEST-Z_\star)+(Z_\star-T_{\rm norm})+(T_{\rm norm}-S).
\]

| Gap | Mean across 2,000 pairs (speed units) |
|---|---|
| Total Q−S | 0.145538339 |
| Q−BEST: fixed refinement | 0.116641488 |
| BEST−Z_star: derivative estimate | 0.00263557546 |
| Z_star−T_norm: norm projection | 0.0119444242 |
| T_norm−S: signed center cancellation | 0.0143168514 |

The final two mean gaps exceed the residual derivative gap. Profile matching removes much of the vector discrepancy that scalar speed does not distinguish; even then, a distance between profiles can exceed the difference between their norms, and taking absolute values center by center loses signed cancellation. These are identified losses of information in the inequalities, not causal percentages of motion. [Figure 4](plots/04_proof_slack_ladder.png) shows the complete phase means.

Representative extreme locators were selected by the fixed diagnostic rankings, after retaining the full population:

| Quantity | (cycle c, cycle d, phase j) | Value |
|---|---|---:|
| Largest Q−S | (2,0,5), updates 405 and 5 | 1.1254207808115604 |
| Largest BEST−Z_star | (2,0,1) | 0.05899917062588489 |
| Largest Z_star−T_norm | (4,2,9) | 0.12320524071275633 |
| Largest T_norm−S | (4,0,6) | 0.11768658788687206 |
| Largest BEST/S | (4,0,105), updates 905 and 105 | 42300.98284458008 |

At the last locator, S is `3.87406512848687e-7`, Q is `0.056924146724421004`, and BEST is `0.0163876762538909`. The large factor reflects a very small but resolved scalar difference; it is neither masked nor capped. At (2,0,5), Q=`1.1618082771343823`, BEST=`0.11745732878532064`, S=`0.03638749632282179`.

## Sufficient conditions versus observed variance changes

For each reference r, define `M_r=Var_r−W_BEST`. PASS requires `M_r>1e−14`, NOT_ESTABLISHED requires `M_r<−1e−14`, and the remaining tolerance band is UNRESOLVED. Independently, the actual margin is `Var_r−Var_post`, with the same tolerance and a separate classification.

| View | Reference | Sufficient PASS | Actual decrease | Actual increase | Actual unresolved |
|---|---|---|---|---|---|
| all_five | incoming | 0 | 127 | 73 | 0 |
| all_five | pre_damping | 0 | 200 | 0 | 0 |
| new_four | incoming | 0 | 125 | 75 | 0 |
| new_four | pre_damping | 0 | 200 | 0 | 0 |

All four sufficient-condition sets have **0 PASS, 200 NOT_ESTABLISHED and 0 UNRESOLVED**, with no exact zero. Nevertheless, both views have a saved damping-stage decrease at every phase. Incoming-to-post dispersion increases at 73 all_five phases and 75 new_four phases, so a blanket incoming-to-post contraction claim would also contradict the actual saved measurements.

The largest (closest to passing) sufficient margins occur at phase 199: `−1.3540336988438423e−5` and `−1.3572609174649653e−5` for all_five incoming and pre-damping comparisons; `−1.2481835866108834e−5` and `−1.2503943645601236e−5` for new_four. These are well outside the tolerance band. [Figure 5](plots/05_sufficient_condition_margins.png) plots every sufficient and actual margin. Actual margins can appear close to zero on that shared variance scale; the signed table, not apparent line overlap, determines their classification.

## Verification, execution and limits

The analytic gate passed, followed by exactly **14 fixed fixture groups and 607 assertions**. Fixtures include zeros, sign/permutation symmetries, equal-norm unequal-profile vectors, difference cancellation, center cancellation, pair-variance normalization and an outcome-isolation canary. They are deterministic constructed inputs, not a random validation set. The reference D operator was used only there: 33 array calls covering 792 scalar components, plus two scalar reference expressions. It was never evaluated on saved production records.

The single primary pass passed all **59 numerical check arrays**. All three stage-speed readouts matched the accepted reference CSV exactly. Maximum absolute source-factor residual was `5.551115123125783e−17`; the G check was `2.220446049250313e−16`; difference alignment was `1.4432899320127035e−15`; the largest population-pair variance identity residual was `8.673617379884035e−19`. All observed pair and variance bounds held within the fixed tolerances. This is float64 verification, not certified interval arithmetic.

Raw signed residuals are preserved. In particular, `T_norm−S=−8.673617379884035e−19` at (4,3,130) is floating roundoff within the 1e−12 speed tolerance; it was not clipped. The gap-telescope maximum absolute residual is `2.220446049250313e−16`. [NUMERICAL_QA.json](evidence/NUMERICAL_QA.json) gives every signed extremum and locator, and [NUMERICAL_RESIDUALS.npz](analysis/NUMERICAL_RESIDUALS.npz) retains all residual values. Variance checks use 1e−14 absolute tolerance; other native-speed/component and dimensionless fixture checks use 1e−12, with zero relative tolerance. Ratios require speed denominators≥1e−12 or variance denominators≥1e−24.

The supervised fixture gate, primary pass and figure stage took **0.546 s / 2.016 s / 2.250 s**, against caps of 60 / 300 / 120 s. Each ran once, with no retry or presentation correction. A NumPy header-reader compatibility issue was resolved during file-only preparation, before any fixture or data evaluation; its original event is retained. All six new figures were visually inspected. [SIM04_EXECUTION_RECEIPT.md](SIM04_EXECUTION_RECEIPT.md) records the exact counts, environment, operational events and preservation boundary. The external transport seal records the final aggregate file total against the 268,435,456-byte cap.

The report establishes that Q is a correct but loose upper envelope here, that K adds little on these signed intervals, and that the fixed profile symmetry materially improves the envelope without supplying a contraction certificate. Remaining norm-projection and center-cancellation slack explains why a valid component-aware bound can still fail the sufficient comparisons. This is conditional finite-step mathematics on one saved population; it is not a fitted law or evidence of universal behavior. No additional investigation is initiated. The complete evidence is returned for GPT scientific review.
