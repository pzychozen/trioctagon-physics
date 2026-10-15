# SRG-SIM05 — GPT scientific review
## Signed radial intervals and collective cancellation

**Review date:** 14 October 2026  
**Human research author and owner:** Hilmir Frímann Halldórsson  
**Submission:** Codex, SIM05 bounded saved-profile investigation  
**Verdict:** **ACCEPTED_WITHIN_CONDITIONAL_SIGNED_RADIAL_BOUND_SCOPE**  
**Required scientific, source, report or figure corrections:** **None**

Preserve the submitted report, mathematical results, numerical evidence, figures and this subsequent review together, without changing the accepted originals. This is internal scientific acceptance. It is not approval of an unprepared publication payload or authorization for another experiment.

## 1. The scientific answer

The prescribed signed-radial construction succeeds at the stated task: it materially sharpens the earlier profile bound and yields useful, two-sided sufficient comparisons on the complete saved population. It does so without computing the exact damped readout on source records or using saved outcomes in the analytic functions.

The improvement has two distinct sources. The new within-center intervals discard less scalar-relevant information than a distance between component profiles. Averaging these **signed intervals before taking an absolute value** then retains cancellation across centers. These benefits are measured separately, using the same intervals for the signed/unsigned comparison. The remaining interval uncertainty stays in every bound.

### Aggregate tightness

Here aggregate SD means the square root of the mean over the 200 phases of the population variance or variance bound. It is not the mean phasewise SD, an independent-trial confidence interval, or a prediction-error statistic.

| Upper bound / observed aggregate SD | All five cycles | Four continuation cycles |
|---|---:|---:|
| Inherited P_PROFILE | 3.883053736 | 3.800869157 |
| J=1 unsigned | 2.324953432 | 2.240907187 |
| J=1 signed | 1.143828939 | 1.133502585 |
| J=4 unsigned | 2.252932029 | 2.173890862 |
| J=4 signed | 1.084215139 | 1.078065533 |

The independent calculation gives these J=4 aggregate enclosures:

| View | Lower SD bound | Observed SD | Upper SD bound |
|---|---:|---:|---:|
| All five | 0.008473982478526586 | 0.009236017385892267 | 0.010013829875991781 |
| Four continuation cycles | 0.008504864539739755 | 0.009249450604392176 | 0.009971513892722933 |

Thus the upper aggregate is approximately 8.42% and 7.81% above the respective observed aggregate. This does not mean every pair or every phase is within those percentages. In particular, the reported largest J=4 pair factor is about 223.30, where the observed pair difference is small. The complete unfavorable comparisons remain in the evidence.

**Sources:** submission report, “Full-population tightness”; `analysis/pair_phase_intervals.csv`, `phase_dispersion_intervals.csv`, `bound_summary.csv`, and `RESULTS.json`. These values and their aggregation conventions were independently checked.

## 2. Sufficient conditions: both directions, with the undecided cases retained

The most consequential result is not the aggregate ratio alone. The two-sided variance bounds are narrow enough to establish many strict comparisons with the reference variances.

For J=4:

| View | Reference | Decrease condition passes | Increase condition passes | Neither passes | Actual decrease / increase |
|---|---|---:|---:|---:|---:|
| All five | Incoming | 111 | 56 | 33 | 127 / 73 |
| All five | Pre-damping | 200 | 0 | 0 | 200 / 0 |
| Four continuation cycles | Incoming | 108 | 58 | 34 | 125 / 75 |
| Four continuation cycles | Pre-damping | 198 | 0 | 2 | 200 / 0 |

All individual sufficient-test margins are outside the prescribed ±1e-14 band. “Neither” means both sufficient tests are NOT_ESTABLISHED, not that the underlying change is zero or numerically unresolved. No passing decrease condition coincides with a saved increase, and no passing increase condition coincides with a saved decrease.

The J=1 comparisons also agree with the submitted results: all-five incoming 94 decreases / 49 increases; new-four incoming 97 / 51; damping-stage decreases 193 and 189 respectively. The four-subinterval result therefore improves on a simpler fixed construction that was already informative.

### The two remaining damping-stage cases

The four-continuation view does not establish the decrease condition at phases **17 and 57**:

| Phase | Pre-damping variance | Observed post variance | J=4 upper variance | Decrease margin |
|---|---:|---:|---:|---:|
| 17 | 2.1503489935648794e-5 | 1.4456889790840702e-5 | 3.1766671751416666e-5 | -1.0263181815767872e-5 |
| 57 | 1.9862074055878104e-7 | 1.887795458905935e-7 | 2.1670916353369462e-7 | -1.808842297491358e-8 |

Both saved comparisons decrease. The upper enclosure remains too large to establish that decrease through the specified sufficient test. These are genuine limitations of this fixed bound, not contrary motion, missing samples, or a reason to change the partition after seeing the results. The smallest passing all-five damping-stage margin is approximately 4.667115994392145e-8 at phase 199.

“Establish” or “certificate” here refers to a real-valued sufficient inequality evaluated numerically at the declared tolerances. **The implementation is float64, not formal outward-rounded interval certification.** The report makes that distinction explicitly. It should remain in any later explanation.

**Sources:** report, “Sufficient decrease and increase, kept separate from actual change”; complete `phase_dispersion_intervals.csv` and `RESULTS.json` condition counts, phase lists and extrema. All were independently checked.

## 3. Mathematical review

I read the supplied mathematical specification and Codex’s complete `MATHEMATICAL_RESULTS.md`, and checked the derivations directly. No replacement formula or additional numerical resolution is required.

### 3.1 Squared-component coordinates give a monotone derivative

For nonnegative component magnitude s, write

\[
b(s)=1+\log(1+s),\qquad d(s)=s/b(s),\qquad F(p)=\|d(p)\|_2.
\]

The project’s established derivative is

\[
k(s)=\frac{b(s)-s/(1+s)}{b(s)^2}>0,\qquad k'(s)<0.
\]

For

\[
\Phi(z)=\frac{z}{b(\sqrt z)^2},
\]

the chain rule gives, for z>0,

\[
\Phi'(z)=\vartheta(\sqrt z),\qquad
\vartheta(s)=\frac{k(s)}{b(s)}.
\]

The right derivative at z=0 is one. Also

\[
\vartheta'(s)=\frac{k'(s)}{b(s)}-
\frac{k(s)}{(1+s)b(s)^2}<0.
\]

Consequently Phi is increasing and concave on the nonnegative half-line. The submitted proof handles zero by the limiting derivative rather than substituting a denominator epsilon. Numerical derivative sampling is not used as the proof.

### 3.2 Signed Darboux intervals and nesting

For paired profile components, x=p² and y=q²,

\[
\Phi(x)-\Phi(y)=(x-y)\times
\text{the average of }\Phi'\text{ on }[\min(x,y),\max(x,y)].
\]

The endpoint bounds for J=1 and the four left/right endpoint averages for J=4 correctly bound that derivative average. The sign of x-y determines which product is the lower endpoint. Taking minima/maxima of the two signed products handles both orientations correctly.

Summing **signed** component intervals encloses F(p)²-F(q)². Refining the same monotone partition from one to four subintervals nests the intervals. The five derivative slots on a zero-length component interval are retained as specified; its contribution is exactly zero. The calculations use squared-component coordinates, not new time steps.

### 3.3 The denominator envelopes are valid without exact endpoint readouts

The lower envelope follows from b(p_alpha)≤b(max p). Concavity gives the upper envelope:

\[
\sum_{\alpha=1}^3\Phi(p_\alpha^2)
\le3\Phi(\|p\|^2/3).
\]

Therefore

\[
L(p)=\frac{\|p\|}{b(\max p)}\le F(p)
\le\frac{\|p\|}{b(\|p\|/\sqrt3)}=U(p).
\]

Unless p=q=0, the denominator F(p)+F(q) has a strictly positive lower bound. The extrema of the four numerator/denominator endpoint quotients give a valid signed quotient enclosure, including when the numerator interval straddles zero.

The intersections with [L(p)-U(q), U(p)-L(q)] and with the inherited [-P_i,P_i] are justified because each interval contains the same unknown difference. No independence or simultaneous attainability of the bounding endpoints is required. Both-zero and identical-profile cases give exact zero intervals. The report retains raw intervals and every prior-intersection flag; it does not conceal the prior bound behind the new construction.

### 3.4 Collective cancellation and uncertainty are separated correctly

For a center interval [l_i,r_i]=mu_i±epsilon_i,

\[
\Delta u\in[\overline l,\overline r],\qquad
B_J=|\overline\mu|+\overline\epsilon,
\qquad U_J=\overline{|\mu|}+\overline\epsilon.
\]

Their difference is exactly

\[
U_J-B_J=\overline{|\mu|}-|\overline\mu|\ge0.
\]

This measures the additional gain from signed averaging **of the same enclosures**. It does not assume the interval midpoints are the true speed differences. The residual average radius remains in B_J.

The absolute lower bound is zero for a collective interval containing zero and otherwise is the smaller endpoint magnitude. Thus

\[
A_J\le|\Delta u|\le B_J\le U_J\le P.
\]

The stated J=4 versus J=1 lower/upper ordering follows from interval nesting. No strict inequality is required as a theorem. The predeclared small-inversion hull policy was tested synthetically; no actual-record inversion or hull event occurred.

### 3.5 Complete-pair population bounds

For m cycle values,

\[
\operatorname{Var}(u)=\frac1{m^2}\sum_{c>d}(u_c-u_d)^2.
\]

Squaring the nonnegative pair lower and upper bounds gives the stated two-sided variance enclosure. All ten unordered pairs are used for all-five; the six continuation-only pairs are reused for new-four. The denominators are **25 and 16**, not ten and six. Joint attainability of all pair endpoints is not claimed or needed for validity; it remains a possible source of conservatism.

Comparing the upper enclosure with the reference variance yields a sufficient decrease condition. Comparing the lower enclosure yields a separate sufficient increase condition. Failure of one does not establish the other. Those proofs agree with the implementation and the report.

## 4. What produces the measured improvement

At J=4, the average fixed gap decomposition over all 2,000 pair/phase comparisons is:

| Gap | Mean, native speed units |
|---|---:|
| P - unsigned J=4: center enclosure improvement | 0.01390157699 |
| Unsigned - signed J=4: benefit of signed averaging | 0.01431546678 |
| Signed J=4 - observed: remaining upper slack | 0.0006798073141 |
| P - observed: total preceding slack | 0.02889685108 |

Both within-center scalar information and collective signed averaging contribute materially. The signed J=1 aggregate factors are already about 1.14 and 1.13, compared with unsigned J=4 factors above two. Thus merely refining derivative intervals does not account for the principal improvement.

The midpoint cancellation gain exceeds 1e-12 at 1,998 comparisons. Both positive and negative center signs are established at 1,998 J=4 comparisons. Center-level signs are resolved for 15,951 of 16,000 center pairs; collective signs remain unresolved at 55 of 2,000 comparisons. Those different levels of resolution are not conflated.

The mean collective radius falls from approximately 0.001251712327 at J=1 to 0.000682317956 at J=4. That nonzero uncertainty remains in the result. The prior-P intersection changes only nine J=4 center intervals; the raw aggregate factors are essentially the same as the intersected factors. The improvement is not merely a fallback to P.

None of these inequality gaps is a causal percentage of the motion. A better bound changes our mathematical comparison, not the trajectory, damping law or collective dynamics.

**Sources:** report, “What produces the improvement, and what remains uncertain?”; `gap_summary.csv`, `bound_summary.csv`, `pair_phase_intervals.csv`, and `RESULTS.json` counts. The complete distributions, raw/effective comparisons and top-five locators were checked.

## 5. Independent numerical verification and exact accounting

The reviewer-written `review_sim05_saved_evidence.py` does not import or execute the submitted analyst, fixture code, scientific checkers, engine or historical scripts. It independently implements the specified formulas with a batched calculation and a separate algebraic evaluation of theta. All operations are confined to copied submitted data and a new reviewer output directory.

The independent fixture review covers all **14 groups**, their **15 vector cases**, the standalone interval/hull/mask cases, the five-cycle variance fixture, reversal/symmetry/zero tests and the output-isolation canary. It made **41 pure synthetic pair evaluations** and **65 synthetic reference-D array evaluations covering 1,560 components**. The 816 stored submission assertion records were checked for internal consistency. The reviewer’s own fixture implementation performs 759 recorded numerical comparisons plus logical checks; it is not falsely counted as a second execution of Codex’s 816 assertions.

One successful primary reviewer pass then covered:

| Item | Coverage |
|---|---:|
| Represented distinct saved updates | 1,000 |
| Represented distinct center records | 8,000 |
| Unique pair/phase evaluations | 2,000 |
| Labeled-center pairs | 16,000 |
| Component pairs | 48,000 |
| Derivative-node slots | 240,000 |
| Subsequent outcome joins | 2,000 pair/phase rows |
| All-five/new-four view/phase summaries | 400 |

J=1 reuses the J=4 endpoints. New-four reuses the six appropriate pair families. No extra source-state reconstruction or CONTINUOUS comparison is introduced.

### Information-use separation

Only the 12 permitted key/profile/P fields were loaded into the analytic stage. The independently computed center, pair and view arrays were fingerprinted in `REVIEW_PREOUTPUT_FINGERPRINTS.json` **before the outcome join**. The pure formula has no saved-outcome argument or lookup. The submitted code, frozen identities, seal and access log support the same ordering.

This is dataflow separation, not a claim of reviewer blinding: the report and prior results had already been read. The profiles themselves are realized sequential intermediates. They contain enough information to evaluate the exact scalar response; this task deliberately bounds it without doing that evaluation. It is not a forecast from mean speed or initial state alone.

### Coverage and numerical agreement

The reviewer checked all **176 pre-output fields**, all **86 center/outcome fields**, and all **96 numerical residual arrays**, including submitted signed extrema and their exact locators. The six CSV tables were checked in full:

| Table | Rows |
|---|---:|
| pair_phase_intervals.csv | 2,000 |
| phase_dispersion_intervals.csv | 400 |
| join_map.csv | 16,000 |
| bound_summary.csv | 576 |
| gap_summary.csv | 288 |
| phase_interval_means.csv | 200 |

The primary tables were independently reconstructed. Summary statistics and JSON result sections were then recomputed from independently checked primitive submission rows. This keeps large dimensionless quotient conditioning separate from native-speed numerical error. Ratios were checked through their unamplified products, with exact validity masks and raw quotient discrepancies retained. Quantiles use the declared linear method, with stable bracketing locators. Counts, category membership, passing phase lists and unfavorable extremes agree.

| Comparison | Largest absolute reviewer discrepancy |
|---|---:|
| Analytic pair fields | 2.7755575615628914e-17 |
| Analytic view/variance fields | 8.673617379884035e-19 |
| Analytic center fields (maximum occurs in theta nodes) | 7.771561172376096e-16 |
| Recomputed residual arrays (maximum occurs in theta differences) | 8.881784197001252e-16 |

Reviewer environment: **Python 3.13.5, NumPy 2.3.5, Linux**. Submission environment: **Python 3.11.15, NumPy 2.4.4, Windows**. These are cross-environment numerical-consistency results, not bitwise-equivalence claims. The fixed native tolerances are unchanged: 1e-12 for interval/speed quantities and 1e-14 for variance checks, with zero relative tolerance. All checks pass. There was **one primary reviewer pass, no failed stage and no retry**.

The numerical verifier's elapsed time was approximately 1.756 seconds, excluding archive/text/visual review. Full details are in `INDEPENDENT_REVIEW_RESULTS.json`.

## 6. Archive identity and preservation boundary

The submitted `SIM05_GPT_REVIEW.zip` is **49,349,864 bytes**, SHA-256:

`2642946067cccea5c19bceea9e7f89db40d780c57c93d31f58e17e6d3515454d`

Its **107 members are 106 manifested payloads plus MANIFEST.json**. CRC, safe relative paths, exact and case-insensitive name uniqueness, no symlinks, complete manifest coverage, byte sizes and SHA-256 identities pass. The extracted files match their archive members. The separately uploaded report and execution receipt match their archived copies. The transport seal matches the archive and manifest identities.

Accepted report: **19,618 bytes**, SHA-256:

`3c45f8d97239cba2b31fe7fba8b7b8a5ffcbee72f0099a13d107b0a669ba9c1e`

All **12 selected SIM04 files** match the actual earlier accepted SIM04 archive. All **12 retained handoff members** match the supplied original SIM05 handoff. The full **ten-member SIM04 scientific review** matches the earlier reviewer archive, whose nine-payload manifest also passes. The inherited P-dominance theorem remains attributed to that earlier review, rather than being inserted into SIM04 or claimed as a new SIM05 discovery.

The 97 recorded protected SIM04 identities match the supplied original archive, archive file and transport seal. All 34 included input/review copies agree with their preservation map. The initial, final and post-packaging repository records agree, including the ten unrelated dirty tracked files and empty staging. The twelve frozen proof/code/specification files match their recorded hashes.

**These checks verify supplied files and receipts, not independent access to the owner's Windows filesystem.** No current remote-main or SIM04/SIM05 publication claim is made. The last pinned scientific repository checkpoint remains SIM03 commit `e1f5115402a05965834493c1254b03118a531c92`.

`ARCHIVE_REVIEW.json` and `PRESERVATION_RECORD_REVIEW.json` retain these checks.

## 7. Figures and presentation

All six original figures were displayed and inspected individually. The plotting code was read and its source columns checked against the verified tables. Figures 1, 2 and 6 identify logarithmic scales; Figure 5 identifies its symmetric-log scale and distinguishes its 1e-8 display transition from the 1e-14 numerical decision tolerance.

The complete 0–199 phase range is retained. Figures 3 and 4 distinguish mean inequality gaps from dispersion aggregates and causal attribution. Figure 1 visibly separates the unsigned bound from the much tighter signed one; Figure 2 shows retained lower and upper uncertainty rather than presenting only a fitted central curve. Figure 5 displays both decrease and increase comparisons. No figure regeneration or correction is required.

`VISUAL_REVIEW.json` lists the inspected original PNG identities and notes. No scientific image was altered in this review.

## 8. Decision and next boundary

**Accept SIM05 within conditional signed-radial-bound scope.** The requested improvement is supported: scalar-specific signed intervals yield substantially tighter bounds and useful two-sided sufficient comparisons without demanding that the dynamics contract.

Do not describe the result as an 8% guarantee for every pair, generic prediction accuracy, external physical validation, full-state contraction, a universal incoming-to-post decrease, or long-time convergence. Do not treat the two nonpassing damping phases as failed simulations. Do not increase the number of subintervals merely to turn 198/200 into 200/200.

My recommended next preservation step is one coherent account of **SIM04 and SIM05 together**: the original bound, its measured information loss, the inherited profile-dominance theorem, and the signed-radial remedy with both its successful comparisons and remaining limits. This review does not start that manuscript/publication task or another numerical investigation. Accepted local results must not be represented as already published.

### Review execution boundary

This review generated **zero new trajectories, engine/API calls, raw source-state or centroid reconstructions, RNG operations, exact D/F evaluations on actual saved records, executions of supplied scientific scripts, repository writes or paper builds**. New numerical work was the independent fixed-fixture and saved-profile bound verification counted above. File hashing, metadata/receipt comparison and visual inspection are recorded separately. No formal interval-arithmetic upgrade, additional partition level or new numerical family was introduced.

Reproduction uses the included new reviewer script, the extracted original SIM05 submission, and its supplied external transport seal; the file-only archive audit additionally uses the prior SIM04 submission, prior SIM04 scientific review and original SIM05 handoff. Use a fresh output directory; the numerical reviewer refuses to overwrite its start marker. Inclusion of review code is not a request to rerun a completed review.
