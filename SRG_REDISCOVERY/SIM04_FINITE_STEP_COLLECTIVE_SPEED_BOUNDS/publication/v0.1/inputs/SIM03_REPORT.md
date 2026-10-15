# SIM03 — Driving, geometry and response alignment

14 October 2026 · Passive analysis for GPT scientific review  
Human research author and owner: Hilmir Frímann Halldórsson  
Scientific direction and subsequent review: GPT · Implementation and analysis: Codex

The saved repeated-drive curves share an impulse-magnitude structure, but magnitude alone does not explain their mean speeds. The distance regularizer is usually close to one; substantial, state-dependent alignment and damping then combine to produce the observed response. In the four new REPEATED cycles, mean alignment contributes 0.0151066 per update to the speed budget, compared with 0.00603029 from the nonnegative squared-impulse term after conversion to speed. Their sum is almost balanced by mean damping loss 0.0211366. These are signed observed-path budget terms, not causal percentages.

Damping reduced labeled velocity differences in every requested comparison. It also reduced phasewise scalar-speed variance in every one of the 200 phases, for both the all-five and new-four views. The second observation is stronger than the vector inequality alone warrants: it is a property of these saved records, not a general scalar-dispersion theorem. Alignment, component orientation and incoming state remain consequential even when scalar speed curves look similar.

The investigation completed one primary pass over exactly **1,800 distinct updates, 14,400 center rows and 43,200 velocity components**. The shared prefix was counted once. Every reconstructed successor velocity component matched its saved counterpart exactly in the executed float64 environment. No trajectory was evolved.

## 1. Source definitions and indexing

The authority is the accepted SIM02 edition associated with commit **36621a283c48edbd6050771a5beddc4dde7cedcf**. The [input map](evidence/INPUT_MAP.json) pins the 21 consumed/copied files by byte count and SHA-256: three state records, original and detached C definitions, engine API, accepted report/reference tables, paper LaTeX and all seven prior scientific-review members. Historical code and checkers were read as text only.

The operative source is [detached engine_C.py](inputs/accepted_sim02/inputs/detached/engine_C.py): lines 23–30 define damping and incoming-speed gain; lines 52–73 give the ordered center update. The original [source_C.py](inputs/accepted_sim02/inputs/sources/source_C.py), [engine API](inputs/accepted_sim02/inputs/engine_api.py), [accepted report](inputs/accepted_sim02/SIM02_REPORT.md), and [paper source](inputs/accepted_sim02/SRG_SIM02_REPEATED_DRIVING_AND_RETAINED_STATE_v0.1.tex), Sections 2, 4, 7 and 8, provide preserved context. The [work order](received/SRG_SIM03_CODEX_WORK_ORDER_v0.1_20261014.md) and [frozen specification](received/SIM03_EXPERIMENT_SPEC_v0.1.json) govern this new analysis.

| Saved record | Updates counted | Saved states | Role |
| --- | --- | --- | --- |
| inputs/runs/C/states.npz | n = 0…199 (200) | 201 | Shared inherited prefix |
| runs/CONTINUOUS/states.npz | n = 200…999 (800) | 801 | Continuous continuation |
| runs/REPEATED/states.npz | n = 200…999 (800) | 801 | Repeated continuation |

Continuation p/v/b checkpoints equal the prefix endpoint. Source float64 p/v and original bit dtypes were retained and loaded read-only with pickle disabled: prefix bits int8, continuation bits int64. Analysis tags use lossless int8 conversion. Prefix state indices are implicit 0…200; no missing array was invented. Saved NaN random-draw slots were not motion failures and were not reevaluated.

Incoming quantities use S_n and the response uses S_(n+1). Repeated cycle c and phase j obey n=200c+j, 0≤j<200. Cycle zero is inherited; continuous segments are blocks, not repeated cycles. Saved H and G are authoritative. G=1/(1+u_in) uses the incoming mean of eight velocity norms before the center loop.

For center i, the temporary geometry is the full saved predecessor position array with rows below i replaced by saved successor positions. The arithmetic centroid is recomputed with the source full-array NumPy mean. Its displacement from P^-_i is wrapped componentwise into [-5,5), then regularized by adding 0.01 to its norm. With saved successor bit sign s_i, the original grouping is

\[
f_i=(d_i/(\|d_i\|+0.01))H s_i,\quad
a_i=0.1f_iG,\quad w_i=v_i+a_i,\quad
D(w)_\alpha=\frac{w_\alpha}{1+\log(1+|w_\alpha|)}.
\]

This recovers sequential rather than simultaneous geometry: earlier centers have already moved when later centers are visited. Every temporary array was rebuilt from saved positions. No calculated position or velocity was passed to another center or update. Both the sign of H and the successor bit enter the impulse. The centroid remains the historical wrapped arithmetic convention; no circular mean or relabeling was substituted.

## 2. Two exact budgets, with different units

For one center define I=‖a‖², A=2v·a and L=‖w‖²−‖D(w)‖². Expanding ‖v+a‖² gives

\[
\|D(w)\|^2-\|v\|^2=I+A-L.
\]

I≥0 measures squared impulse, A is signed alignment and L≥0 is squared-speed damping loss. I alone is not the net forcing increment. None is physically calibrated energy or work. With ℓα=log(1+|wα|), the stable form

\[
L=\sum_\alpha w_\alpha^2\frac{\ell_\alpha(2+\ell_\alpha)}{(1+\ell_\alpha)^2}
\]

follows by subtracting the reciprocal squared damping factor from one. Stable and direct forms were retained separately without clipping.

For the **actual mean-speed curve**, write r=‖v‖, m=‖w‖, t=‖D(w)‖. Rationalizing m−r gives

\[
B=\frac{I}{m+r},\qquad C=\frac{A}{m+r},\qquad
R=m-t=\frac{L}{m+t},\qquad
u_{n+1}-u_n=\overline B+\overline C-\overline R.
\]

The overbar averages eight centers. Observed successor norms come from saved velocities; internal identities against D(w) are checked separately. Mean squared speed, square of mean speed and RMS speed are distinct. Taking a square root of the squared-speed ledger would not recover the mean-speed budget.

When m+r=0, v=w=a=0 and B=C=0. When m+t=0, w=D(w)=0 and R=0, even if v was nonzero. Inconsistent zero denominators are errors. Cosine, retention and component concentration have validity masks. No arbitrary epsilon enters the identities. No actual center had an undefined diagnostic or zero budget denominator. The separate 1e-12 reporting floor masks poorly resolved ratios without altering raw budgets.

The nine distinct 200-update ledgers retain signs and absolute activity. “Σ mean |C|” sums the centerwise absolute-activity mean over updates, not the absolute value of the final signed sum. Display values are rounded; CSVs retain precision.

| Record / block | Σ mean B | Σ mean C | Σ mean R | Σ mean \|C\| | Observed Δu |
| --- | --- | --- | --- | --- | --- |
| PREFIX / 0 | 1.187233 | 2.890278 | 4.170859 | 3.767033 | -0.09334836 |
| CONTINUOUS / 1 | 2.837191e-05 | 0.001158221 | 0.01064483 | 0.004747486 | -0.009458236 |
| CONTINUOUS / 2 | 2.342773e-10 | 2.28846e-06 | 0.00211981 | 9.565392e-06 | -0.002117522 |
| CONTINUOUS / 3 | 3.257191e-15 | 2.355972e-09 | 0.0009233655 | 2.707962e-08 | -0.0009233631 |
| CONTINUOUS / 4 | 3.008447e-20 | -5.962361e-12 | 0.0005189253 | 6.643186e-11 | -0.0005189253 |
| REPEATED / 1 | 1.177904 | 3.172199 | 4.348652 | 3.726599 | 0.001450748 |
| REPEATED / 2 | 1.336903 | 2.771514 | 4.111875 | 3.946698 | -0.003458018 |
| REPEATED / 3 | 1.120049 | 3.299693 | 4.416184 | 3.654532 | 0.003558535 |
| REPEATED / 4 | 1.189379 | 2.8419 | 4.032588 | 3.255953 | -0.001309347 |

| Record / block | Σ mean I | Σ mean A | Σ mean L | Σ mean \|A\| | Observed Δ mean ‖v‖² |
| --- | --- | --- | --- | --- | --- |
| PREFIX / 0 | 0.9430391 | 3.122963 | 4.078665 | 3.461072 | -0.01266249 |
| CONTINUOUS / 1 | 7.782766e-07 | 3.493432e-05 | 0.0002364419 | 0.0001275844 | -0.0002007293 |
| CONTINUOUS / 2 | 2.374353e-12 | 2.353319e-08 | 1.867045e-05 | 9.532333e-08 | -1.864691e-05 |
| CONTINUOUS / 3 | 2.084007e-17 | 1.321006e-11 | 5.28337e-06 | 1.710737e-10 | -5.283356e-06 |
| CONTINUOUS / 4 | 1.408412e-22 | -2.857771e-14 | 2.214443e-06 | 3.067644e-13 | -2.214443e-06 |
| REPEATED / 1 | 0.9506586 | 3.368227 | 4.318831 | 3.542748 | 5.477738e-05 |
| REPEATED / 2 | 0.9685248 | 3.077183 | 4.045808 | 3.513942 | -0.0001005116 |
| REPEATED / 3 | 0.9285071 | 3.506204 | 4.434607 | 3.583298 | 0.0001036736 |
| REPEATED / 4 | 0.960043 | 2.844371 | 3.80447 | 2.996429 | -5.617255e-05 |

Small signed alignment in late CONTINUOUS blocks is retained, including negative values. Boundary differences close under the original 1e-10 telescoping tolerance; the largest residual is 5.27e-16. [Full block ledger](analysis/cycle_summary.csv) · [all update budgets](analysis/update_budgets.csv) · [actual-speed budget figure](plots/01_actual_speed_budgets.png).

## 3. Normalization supports a common magnitude structure, with exceptions

The source impulse gives the derived factorization

\[
h=0.1|H|,\quad q_i=\frac{\|d_i\|}{\|d_i\|+0.01},\quad
\|a_i\|=hGq_i,\quad \overline I=h^2G^2\overline{q^2}.
\]

Distance suppression is separated from prescribed drive and instantaneous gain. Direction remains in A and orientation-dependent damping. The update table retains h, h², G, G² and mean(q²) separately, with factorization residuals.

| Records | min | p05 | p25 | median | p75 | p95 | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ALL | 0.7996594 | 0.9907515 | 0.9953367 | 0.9974005 | 0.9980709 | 0.9985683 | 0.9987295 |
| PREFIX | 0.9873948 | 0.9917775 | 0.9968068 | 0.9975036 | 0.9981944 | 0.99859 | 0.9986171 |
| CONTINUOUS | 0.9906516 | 0.9909055 | 0.9962748 | 0.9973605 | 0.997855 | 0.9985531 | 0.9985808 |
| REPEATED | 0.7996594 | 0.9813017 | 0.994822 | 0.9973618 | 0.9980664 | 0.9986845 | 0.9987295 |

Fractions reaching each prespecified suppression threshold:

| Records | q ≥ 0.90 | q ≥ 0.99 | q ≥ 0.999 |
| --- | --- | --- | --- |
| ALL | 0.9979167 | 0.9671528 | 0 |
| PREFIX | 1 | 0.999375 | 0 |
| CONTINUOUS | 1 | 1 | 0 |
| REPEATED | 0.9953125 | 0.92625 | 0 |

Across all records, 96.7153% of centers have at most 1% magnitude suppression, but none reach the 0.1% threshold. In REPEATED, 92.625% reach the 1% threshold. Near-unity normalization is frequent, not uniform.

All 30 rows with q<0.90 occur at REPEATED center 1, n=485…514 (cycle 2, phases 85…114). The minimum q=0.7996594476 is at n=498, center 1: ‖d‖=0.0399150, H=−0.0118167, G=0.946462 and ‖a‖=0.000894345. This is about 20.0% suppression relative to hG at a small absolute impulse, not evidence that the strongest early-phase impulses lose that fraction. [Located exceptions](evidence/DOCUMENTATION_LOOKUPS.json) · [normalization/gain figure](plots/03_normalization_and_gain.png).

The figure's factor panel explicitly plots h, G² and mean(q²); the exact squared-impulse identity uses h². Gain is a deterministic dependency, not independent confirmation:

\[
|G(u)-G(\widetilde u)|=
\frac{|u-\widetilde u|}{(1+u)(1+\widetilde u)}
\le |u-\widetilde u|,\qquad u,\widetilde u\ge0.
\]

This follows by subtracting reciprocals. The incoming-index source-form G check had zero residual; stable-summary recomputation differs by at most 2.22e-16 because of reduction order. Observed G or G² is a multiplier at a recorded state, not a no-gain trajectory experiment.

## 4. Alignment is substantial and signed; averages hide activity

For nonzero v and a, cosine = (v·a)/(‖v‖‖a‖), so A=2r‖a‖cosine. A positive cosine reinforces incoming motion and a negative one opposes it; zero vectors carry an invalid cosine mask.

New REPEATED means are I=0.00475967, A=0.0159950 and L=0.0207546 in squared-speed units; B=0.00603029, C=0.0151066 and R=0.0211366 in speed units. Positive alignment is larger on average than B, while 2,227 of 6,400 centers have negative alignment. C and A have the same sign but different weights.

These totals sum centers over each record. Cancellation is 1−|signed total|/absolute total; it includes cancellation across time as well as centers.

| Records | Σ A | Σ \|A\| | A cancellation | Σ C | Σ \|C\| | C cancellation | Negative centers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PREFIX | 24.98371 | 27.68858 | 0.09768903 | 23.12222 | 30.13626 | 0.2327441 | 572 |
| CONTINUOUS | 0.0002796629 | 0.001021439 | 0.726207 | 0.009284093 | 0.03805663 | 0.7560453 | 3137 |
| REPEATED | 102.3679 | 109.0913 | 0.06163151 | 96.68245 | 116.6703 | 0.1713188 | 2227 |

Per-update signed/absolute totals and within-update cancellation are also retained. CONTINUOUS has tiny late forcing: the reporting floor masks 294 update A-cancellation ratios and 115 C-cancellation ratios; PREFIX and REPEATED have zero masks. Raw positive-denominator values remain available. An undefined or masked ratio is not perfect cancellation. [Alignment/cancellation figure](plots/04_alignment_and_cancellation.png).

Prespecified sign and bit-change strata are observational. H=0 is empty, with undefined means:

| All-record stratum | Centers | Mean ‖a‖ | Mean A | Mean C | Mean cosine |
| --- | --- | --- | --- | --- | --- |
| H_positive | 8416 | 0.02335383 | 0.01514877 | 0.0144104 | 0.3300464 |
| H_negative | 5984 | 0.001095837 | -2.342444e-05 | -0.0002446415 | -0.07468725 |
| H_zero | 0 | undefined | undefined | undefined | undefined |
| bit_changed | 164 | 0.01845921 | -0.01358054 | -0.02276277 | -0.1919334 |
| bit_unchanged | 14236 | 0.01405423 | 0.00910221 | 0.008678495 | 0.1659328 |

Saved bit changes total 14 in the prefix, 75 in CONTINUOUS and 75 in REPEATED. In REPEATED, changed-bit rows have mean C=−0.0312923, versus +0.0156568 on unchanged rows. This does not isolate a bit-change effect: histories, incoming velocities, geometry and phase differ. The [factor/stratum table](analysis/factor_stratum_summary.csv) retains every dataset and block, including joint H-sign/bit strata. Cosines are shown alongside impulse magnitudes so weak impulses are not mistaken for large contributions.

## 5. Damping guarantees and observed comparisons

For s=|x|, differentiation gives

\[
D'(x)=\frac{1+\log(1+s)-s/(1+s)}{[1+\log(1+s)]^2},
\qquad 0<D'(x)\le1,\quad D'(0)=1.
\]

The numerator is positive since 1−s/(1+s)>0. Denominator minus numerator is log(1+s)+log²(1+s)+s/(1+s)≥0. Applying the scalar mean-value bound and summing coordinate squares proves

\[
\|D(w)-D(\widetilde w)\|_2\le\|w-\widetilde w\|_2.
\]

This bounds the damping stage for fixed pre-damping vectors. Geometry, forcing, gain, bits and position wrapping lie outside it. D'(0)=1 precludes a uniform contraction factor below one near zero; no full-update contraction theorem follows.

All seven authorized pairs were compared at every phase: 1,400 pair/phase rows and 11,200 labeled-center pairs. “Mean distance” averages eight center distances, then 200 phases; “mean post RMS” averages per-phase center RMS. “Largest” maximizes over centers and phases. Scalar-speed difference RMS is across phases and is separate.

| Cycle pair | Mean incoming distance | Mean pre-damping distance | Mean post distance | Largest post center distance | Mean post RMS distance | Scalar-speed difference RMS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 vs 0 | 0.1433319 | 0.1750052 | 0.1428673 | 1.205036 | 0.1600567 | 0.01211771 |
| 2 vs 1 | 0.1112228 | 0.1327503 | 0.1112083 | 1.13708 | 0.1375307 | 0.01845248 |
| 3 vs 2 | 0.08921319 | 0.106435 | 0.089198 | 1.182808 | 0.1146647 | 0.0187917 |
| 4 vs 3 | 0.1331624 | 0.1584242 | 0.133211 | 1.142243 | 0.1457565 | 0.01336461 |
| 2 vs 0 | 0.1519019 | 0.1827459 | 0.1514587 | 1.209363 | 0.1670784 | 0.01569866 |
| 3 vs 0 | 0.1516627 | 0.1829323 | 0.1512113 | 1.204507 | 0.1667915 | 0.01259893 |
| 4 vs 0 | 0.1296725 | 0.1551466 | 0.1292411 | 1.202324 | 0.1420911 | 0.0145514 |

Every center damping comparison contracted. Largest signed post-distance minus pre-damping distance was −1.28905e-5, pair (4,3), phase 138, center 0. Mean-distance damping ratios ranged from 0.678176 to 0.990632; no mean/max/RMS ratio was masked. Yet forcing increased mean labeled-vector distance from incoming to pre-damping in 134–154 of 200 phases per pair. Damping suppresses differences introduced or retained before it; this does not show full-update contraction. [All three-stage distances](analysis/same_phase_comparisons.csv) · [pair summaries](analysis/same_phase_summary.csv) · [figure](plots/06_phase_velocity_differences.png).

### Scalar-speed similarity requires a separate calculation

D is componentwise and not rotation invariant. For r>0,

\[
\|D((r,0,0))\|=\frac r{1+\log(1+r)},\quad
\left\|D\left(\frac r{\sqrt3}(1,1,1)\right)\right\|
=\frac r{1+\log(1+r/\sqrt3)}.
\]

Equal incoming norms can yield unequal outgoing norms. This deterministic analytic example involved no rotated trajectory. Vector nonexpansion does not imply scalar dispersion must fall.

The actual population spreads treat cycles as correlated records, not independent trials:

| Cycles | RMS phase SD incoming | RMS phase SD pre-damping | RMS phase SD post | Mean post range | Mean post speed |
| --- | --- | --- | --- | --- | --- |
| all_five | 0.009604065 | 0.01287172 | 0.009236017 | 0.01650301 | 0.1021115 |
| new_four | 0.009249456 | 0.01282697 | 0.009249451 | 0.01547516 | 0.1020218 |

“RMS phase SD” is the root mean square of 200 population standard deviations across cycles; it does not substitute RMS speed for actual mean speed. New-four post-speed SD reaches 0.0432153 at phase 13: similarity is not identity. Budget-curve spreads retain their respective units:

| Term | All-five RMS phase SD | New-four RMS phase SD |
| --- | --- | --- |
| I | 0.001007226 | 0.0004168106 |
| A | 0.007433397 | 0.007203979 |
| L | 0.005581124 | 0.005586061 |
| B | 0.004050072 | 0.002116269 |
| C | 0.008653725 | 0.007729164 |
| R | 0.003967491 | 0.003928355 |

In the new-four view, A varies much more than I in squared-speed units, and C more than B in speed units. Together with L/R compensation, this prevents a complete explanation using the common impulse-magnitude envelope alone. [Phase budget curves](plots/02_phase_budget_terms.png).

Here u_pre denotes mean ‖w‖, distinct from incoming u used by G. Since u_post=u_pre−mean(R), population moments across cycles at fixed phase obey

\[
\operatorname{Var}(u_{post})=\operatorname{Var}(u_{pre})
+\operatorname{Var}(\overline R)
-2\operatorname{Cov}(u_{pre},\overline R).
\]

Averages of these phasewise moments are:

| Cycles | Mean Var(pre) | Mean Var(R) | Mean Cov(pre,R) | Mean Var(post) |
| --- | --- | --- | --- | --- |
| all_five | 0.0001656811 | 1.574099e-05 | 4.805903e-05 | 8.530402e-05 |
| new_four | 0.0001645312 | 1.543197e-05 | 4.720544e-05 | 8.555234e-05 |

Positive covariance is large enough for post-damping scalar variance to be lower in **200/200 phases in both views**, with zero increases. Maximum balance residual is 2.82e-18. This documents compensation of pre-damping scalar differences by loss, not causal variance attribution. New-four incoming and post RMS phase SD are almost equal (about 0.00924945), whereas pre-damping is larger (0.0128270). The measured reduction is explicitly pre-damping to post-damping. [Full means/ranges/population SDs](analysis/phase_spread.csv) · [variance-balance figure](plots/07_scalar_dispersion_balance.png).

### Retention depends on magnitude and component distribution

For m>0, retention=t/m and χ=Σwα⁴/(Σwα²)², with 1/3≤χ≤1. These are descriptive readouts, not a new memory or complexity score.

| Records | Median m | Median retention | Median χ |
| --- | --- | --- | --- |
| PREFIX | 0.04156769 | 0.9731756 | 0.4465243 |
| CONTINUOUS | 0.003305768 | 0.9980693 | 0.3401005 |
| REPEATED | 0.04125278 | 0.9744527 | 0.4295257 |

Retention spans 0.651157…0.998986 and χ spans 0.333333557…0.996537. Predeclared joint bins use m boundaries [0,.01,.05,.1,.25,.5,1,∞] and χ boundaries [1/3,.45,.6,.8,1], with 1e-12 endpoint inclusion slack. All 28 bins, including four empty m≥1 bins, are retained.

Within 0.25≤m<0.5, mean retention is 0.832506 in the lowest χ bin and 0.763123 in the highest. Mean m is 0.374305 versus 0.409516, so even this comparison does not hold magnitude fixed. The analytic example establishes that orientation can matter; the records show its co-occurrence with magnitude variation, not its isolated effect. [Joint table](analysis/retention_orientation_summary.csv) · [retention/orientation figure](plots/05_damping_retention_orientation.png).

## 6. CONTINUOUS context and interpretive limit

The 800 comparisons use equal actual update indices, REPEATED minus CONTINUOUS. Mean-speed differences average saved responses over each block; budget differences sum 200 update means.

| Block | Mean speed difference | Σ mean ΔB | Σ mean ΔC | Σ mean ΔR |
| --- | --- | --- | --- | --- |
| 1 | 0.09513501 | 1.177875 | 3.171041 | 4.338007 |
| 2 | 0.09438931 | 1.336903 | 2.771511 | 4.109755 |
| 3 | 0.1022326 | 1.120049 | 3.299693 | 4.41526 |
| 4 | 0.09842748 | 1.189379 | 2.8419 | 4.032069 |

CONTINUOUS's mean B and C over 800 updates are 3.55e-8 and 1.45e-6, while mean R is 1.78e-5. Its late weak forcing and continued damping contrast with recurring REPEATED drive. All 6,400 cross-arm center comparisons also satisfy damping nonexpansion; largest signed excess is −6.90e-6. [Full distances and budget differences](analysis/cross_arm_comparisons.csv) · [cross-arm figure](plots/08_cross_arm_context.png).

These are two accepted histories with shared initial evidence, not independently randomized mechanism controls. The decomposition explains exact observed balances and shows how similar scalar responses coexist with different labeled velocities. It does not establish generic-initial-state robustness, irrelevance of retained state, learned memory, asymptotic classification or physical calibration.

One unresolved mathematical question is sufficient: **Under what explicit magnitude-and-alignment conditions would the coupled forcing-and-damping map bound phasewise scalar mean-speed dispersion?** The damping vector inequality alone is insufficient. No further experiment starts here.

## 7. Verification and execution boundary

Input identities/schema/schedules, nine fixed algebra fixtures and deterministic schema/analytic checks passed before the primary pass. Tolerances remained fixed: 1e-12 for component reconstruction, center/update identities and bounds; 1e-10 for block telescoping. Saved-successor checks and internal identities are separate:

| Check | Maximum absolute residual | Locator (dataset, n, center/component where applicable) |
| --- | --- | --- |
| velocity_residual | 0 | PREFIX, 0, 0, 0 |
| square_saved_residual | 2.220446e-16 | PREFIX, 4, 2 |
| square_internal_residual | 2.220446e-16 | PREFIX, 4, 2 |
| speed_saved_residual | 2.220446e-16 | PREFIX, 3, 1 |
| speed_internal_residual | 2.220446e-16 | PREFIX, 3, 1 |
| L_stable_minus_direct | 1.665335e-16 | PREFIX, 4, 2 |
| R_stable_minus_direct | 2.220446e-16 | PREFIX, 10, 5 |
| update_saved_speed_residual | 1.110223e-16 | REPEATED, 407 |
| update_saved_square_residual | 8.326673e-17 | REPEATED, 804 |
| update_I_factor_residual | 2.775558e-17 | REPEATED, 200 |
| update_G_residual | 2.220446e-16 | PREFIX, 24 |

[Complete QA](evidence/QA.json) retains signed extrema, bound margins, masks, locators and stable/direct alternatives. Factorization maxima are 1.67e-16 for impulse norm and 1.11e-16 for I; gain-difference identity maximum is 2.78e-16. No unmasked nonfinite primary quantity occurred.

The single supervised extraction-and-summary run took **26.594 seconds** against its 300-second cap (worker internal time 25.766 seconds). Eight-figure production plus one permitted terminology correction took **10.516 seconds** against the combined 120-second cap. The correction changed “Force magnitude” to “Impulse magnitude” for hGq using completed tables only; the final figure was reinspected. A separate report-locator lookup over completed SIM03 outputs took 0.063 seconds with no source reconstruction. Document assembly and archive verification are not additional primary passes.

Execution totals: **one primary pass; 1,800/1,800 updates and 14,400/14,400 centers started/completed; zero engine calls, new updates, initializations, RNG samples/restorations, old-checker runs or old-preflight reanalyses**. No scientific retry or relaxed tolerance occurred.

All 21 selected originals and copies, HEAD, Git index, known unrelated modified tracked files, research index and licence-scope document are covered by bounded checks in the [execution receipt](SIM03_EXECUTION_RECEIPT.md). There were no Git writes or changes to accepted science. The [evidence guide](EVIDENCE_README.md) describes tables, masks and access boundaries. Final archive identity and output bytes including the ZIP are recorded outside the archive in [the transport seal](SIM03_TRANSPORT_SEAL.json); the limit is 268,435,456 bytes.

The passive investigation is complete for GPT scientific review. No follow-on execution or publication has been initiated.
