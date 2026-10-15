# SRG-SIM04 — GPT scientific review
## Finite-step collective-speed bounds

**Review date:** 14 October 2026  
**Human research author and owner:** Hilmir Frímann Halldórsson  
**Submission:** Codex, SIM04 bounded saved-intermediate investigation  
**Verdict:** **ACCEPTED_WITHIN_CONDITIONAL_FINITE_STEP_BOUND_SCOPE**  
**Required scientific, source, report or figure corrections:** **None**

Preserve the submitted report and numerical evidence unchanged together with this subsequent review. This decision is scientific acceptance, not approval of an as-yet-unprepared publication payload or authorization for another experiment.

## 1. Scientific answer

The baseline vector inequality is valid but loose for the scalar quantity it is meant to bound. The fixed signed-component derivative refinement adds comparatively little; the sorted-absolute-component profile refinement makes a substantial improvement. Neither provides a phasewise certificate of scalar-dispersion nonincrease on the tested population.

This is a useful result with two distinct parts: an improvement in the mathematical bound and an explicit identification of its remaining limitations. Failure to meet a sufficient condition does not imply expansion. The submitted report handles this distinction correctly.

The aggregate standard-deviation figures below are **square roots of phase-averaged population variances or variance upper bounds**, not averages of phasewise standard deviations and not confidence limits from independent trials.

| Quantity | All five cycles | Four continuation cycles |
|---|---:|---:|
| Observed post-damping aggregate SD | 0.009236017385892267 | 0.009249450604392176 |
| Q vector aggregate SD upper bound | 0.17051791440079614 | 0.14432976491387062 |
| Q / observed | 18.46227732975655 | 15.604144622961115 |
| K signed-component aggregate SD upper bound | 0.16736120042652045 | 0.14088588785718578 |
| K / observed | 18.1204943033303 | 15.23181147540644 |
| P profile aggregate SD upper bound | 0.03586395181360574 | 0.03515595152503629 |
| P / observed | 3.8830537357353645 | 3.8008691573899753 |

All seven prescribed families, including the coarse/source/triangle forms and BEST_PRE, were checked. The six-pair new-four view reuses already evaluated pair families from the ten-pair all-five view.

The information-use boundary is important. These bounds use the recorded incoming velocities and **realized sequential intermediates**, including impulses and pre-damping vectors. They do not consult saved outcomes in their analytic functions. They are not a new mean-speed-only prediction from initial state, a reconstructed source update, or a test of arbitrary unseen configurations.

**Sources:** submission report “Answer,” “Tightness across the full population”; `analysis/pair_phase_bounds.csv`, `phase_dispersion_bounds.csv`, `bound_summary.csv`, `RESULTS.json`; independently checked below.

## 2. Archive, handoff and source continuity

The supplied `SIM04_GPT_REVIEW.zip` is **21,653,622 bytes**, SHA-256:

`d3be3e9829181378f1e0e3af696d5cfe8de98c8a697ee59677c0edd5036e2987`

Its **95 members are 94 manifested payloads plus MANIFEST.json**. CRC, path safety, exact and case-insensitive name uniqueness, no-symlink checks, exact manifest coverage, all sizes and all SHA-256 identities pass. The extracted review inputs match the archived bytes. The separate report and execution receipt match their archive copies. The external transport seal matches the archive and manifest identities.

Accepted report: **18,458 bytes**, SHA-256:

`b95abdb7aecfbe38b7e340035497db6bc5801719aec257ce30a65344bcdaaf2f`

All **13 selected upstream files** match the previously approved corrected SIM03 repository-only candidate ZIP byte-for-byte, their supplied input map, and independently calculated canonical Git blob IDs. The scientific reference is SIM03 commit `e1f5115402a05965834493c1254b03118a531c92`. This review did not query current remote main; no current-repository claim is substituted for that pinned-source comparison.

All 11 retained handoff members match the supplied original SIM04 handoff. The twelve frozen scientific/proof/specification files match the implementation gate. The before/after and post-packaging baselines agree, including the ten unrelated dirty tracked files, physical Git index, index entries, research index and source-specific licensing/attribute records.

These are checks of submitted files and preservation receipts, **not independent access to the author's Windows filesystem**. The original submission, accepted source arrays and all six figures remain unchanged.

## 3. Mathematical review

### 3.1 Source-separated and vector hierarchy

The submitted derivations correctly establish

\[
S\le Q\le T\le\Gamma\le\Omega,
\]

under the common-phase source assumptions. In particular, both decompositions of \(G_cg_c-G_dg_d\) give valid source-separated bounds, and choosing the expansion with coefficient \(\min(G_c,G_d)\), together with \(|\Delta G|\le V\) and \(\overline{\|g\|}\le1\), gives the claimed coarse form. The gain depends on **incoming** mean speed. Neither the sign of H nor successor bits are discarded from the vector impulses.

The cross-history identity

\[
\|\Delta v+\Delta a\|^2=\|\Delta v\|^2+\|\Delta a\|^2+2\Delta v\cdot\Delta a
\]

is correctly distinguished from SIM03's within-history \(2v\cdot a\). The numerical Q uses the stored combined-vector difference, avoiding a cancellation-prone square-root reconstruction.

### 3.2 The interval derivative bound is valid

With \(b=1+\log(1+s)\),

\[
k(s)=\frac{b-s/(1+s)}{b^2},\qquad
k'(s)=\frac{2s-(s+2)b}{(1+s)^2b^3}<0.
\]

The submitted proof uses \(J(s)=(s+2)b-2s\), \(J(0)=2\), and \(J'(s)=\log(1+s)+1/(1+s)>0\). This is a valid analytic monotonicity proof. The derivative at zero is one. The nearest absolute value to zero on each signed component interval therefore supplies its true derivative maximum, including a value of one when that interval crosses zero.

The resulting K inequality is a **fixed pre-damping vector** bound, not a full-state contraction theorem.

### 3.3 The profile refinement is valid

The source applies the same odd scalar damping function to every component. Consequently the damped scalar norm is invariant under coordinate signs and permutations. Sorting absolute components within each center is legitimate for that scalar readout, but is not arbitrary rotation invariance or center relabeling.

The nonnegative mean-value bound and sorted-matching argument prove \(S\le P\le Q\). No evolution array is replaced by a sorted profile. The equal-input-norm axis/diagonal fixture correctly shows why arbitrary rotations and a generic scalar contraction conclusion remain invalid.

### 3.4 Population aggregation and sufficient conditions are correct

For m scalar responses,

\[
\operatorname{Var}(u)=\frac1{m^2}\sum_{c>d}(u_c-u_d)^2.
\]

The denominators are 25 and 16 for the all-five and new-four views, not the numbers of unordered pairs. All pairs required for these identities are present. Taking the smaller valid pair bound **before squaring and aggregation** is valid and outcome-independent.

The epsilon conditions and the two separate reference-variance conditions are sufficient, not necessary. The float64 checks use prescribed absolute tolerances; they are not certified interval arithmetic.

**Proof sources:** `MATHEMATICAL_RESULTS.md`, §§1–6; original source definitions; frozen mathematical specification. No external theory was used to replace the submitted formulation.

## 4. Independent numerical verification and its boundary

`review_sim04_saved_evidence.py` is newly written reviewer code. It reads, but never imports or executes, Codex's analyst, fixture, scientific-checker or historical engine scripts. It never forms a new position or velocity successor by evolving C. D itself is evaluated only on the supplied deterministic synthetic fixtures, never on actual stored trajectory records.

One complete reviewer pass checked:

| Review population | Coverage |
|---|---:|
| Selected updates | 1,000: prefix 200, REPEATED 800 |
| Selected center records | 8,000 |
| Unique analytic pair/phase evaluations | 2,000 |
| Labeled-center pairs | 16,000 |
| Saved-outcome pair/phase joins | 2,000 |
| View/phase summaries | 400 |
| Fixed fixture groups | 14 |
| Synthetic fixture pair calls, including canary | 29 |
| Synthetic D array calls / scalar components | 33 / 792 |
| Additional scalar fixture reference expressions | 2 |

CONTINUOUS source rows are excluded from scientific evaluation. The shared prefix is counted once. The new-four view creates no additional primary pair evaluation.

The reviewer recomputed all fields in the sealed 53-field pre-output archive, the additional six outcome fields in the 59-field center-pair archive, the seven bound families, source-factor checks, alignment identities, complete-pair variance normalization, margins, classifications and inequality gaps. All **59 submitted numerical residual arrays** and their extrema were checked. Seven CSV tables were checked, including all 560 bound-summary rows and all 147 proof-slack-summary rows; quantiles, interpolation locators, descriptive categories, aggregate values and ranked extreme locators agree.

The analytic reviewer function has no outcome input. Reviewer bound fingerprints were written before the numerical outcome join. This is a dataflow separation, **not a claim of reviewer blinding**: the report and figures had already been read. The submitted code, file seal and access log also consistently place the production outcome join after the pre-output seal.

Reviewer environment: Python **3.13.5**, NumPy **2.3.5**, Linux. Submission environment: Python **3.11.15**, NumPy **2.4.4**, Windows. The largest difference among the independently recomputed primary pair-bound values is approximately **1.39×10^-17**; the largest component-bound discrepancy is **5.56×10^-17**, rounded upward. Derivative coefficients differ by at most **4.45×10^-16**, rounded upward. These are numerical-consistency statements, not cross-platform bitwise equivalence.

Native-unit checks retain absolute tolerance 1e-12; variance checks use 1e-14. Ratio fields are checked through their products in native units, with validity masks exact and raw quotient discrepancies retained. Summary formulas are recomputed from the independently validated stored primitive tables, avoiding an inappropriate native-speed tolerance on a large dimensionless quotient. There were **no failed reviewer stages or repeat passes**. Full results are in `INDEPENDENT_REVIEW_RESULTS.json`.

The submitted fixture receipt has 14 groups and 607 assertions; the reviewer inspected those stored assertions and independently evaluated the same fixed fixture inputs. These are not 607 newly proved theorems or independent experiments.

## 5. What the measured improvement tells us

The vector bound charges for directional differences that the scalar speed can discard. K tightens Q only modestly; **23,992 of 48,000 signed component intervals contain zero**, where its slope coefficient must be one. P removes sign/permutation differences invisible to the scalar damping norm and makes the major improvement.

P is strictly below K in all 2,000 recorded pair/phase comparisons. Median P/Q is approximately 0.306095; its aggregate SD factors are approximately 3.883 and 3.801 rather than 18.462 and 15.604. That is a bound improvement, not stronger damping, a changed trajectory or a performance gain of the model.

Cross-history alignment is real and retained, but accounts for a smaller part of the tightening in these inequalities. There are 5,463 negative and 10,537 positive difference-alignment center pairs. The mean T-minus-Q gap is approximately 0.00424024 in speed units. This does not negate SIM03's substantial within-history alignment contributions; the two calculations answer different questions.

## 6. Why the remaining overestimate matters

The exact saved-output gap ladder passes. Across the complete 2,000 pair/phase population:

| Gap | Mean in native speed units |
|---|---:|
| Q − S | 0.1455383388714982 |
| Q − BEST: fixed refinement | 0.11664148779341293 |
| BEST − Z*: derivative interval estimate | 0.0026355754561056257 |
| Z* − Tnorm: profile-distance to norm-difference step | 0.011944424209146131 |
| Tnorm − S: absolute values discard signed center cancellation | 0.014316851412833492 |

The last two gaps exceed the residual derivative gap **on average over this population**. This localizes remaining information loss in the bound, not causal shares of the dynamics. In particular, a component-profile distance can exceed the difference of the two profile norms, and averaging individual absolute speed differences can exceed the absolute collective difference.

Very large tightness factors are not suppressed. At (4,0,105), S is about 3.8741×10^-7 while BEST is about 0.0163877. This explains a factor around 42,301 without a zero or unresolved denominator. No clipping, phase selection or fitted factor was used.

**Sources:** report “Alignment, refinement and remaining slack”; all seven-family tables; preserved output arrays and independently checked summaries.

## 7. No sufficient nonincrease certificate—and no false inference of expansion

All four sets of sufficient comparisons give **0 PASS, 200 NOT_ESTABLISHED, 0 UNRESOLVED**. Their nearest-to-passing margins are around −1.25×10^-5 to −1.36×10^-5, far outside the 1e-14 tolerance band.

The actual saved behavior is separate:

| View | Reference stage | Actual variance decreases | Actual variance increases |
|---|---|---:|---:|
| All five cycles | Incoming | 127 | 73 |
| All five cycles | Pre-damping | 200 | 0 |
| Four continuation cycles | Incoming | 125 | 75 |
| Four continuation cycles | Pre-damping | 200 | 0 |

Thus the observed damping-stage decrease is compatible with failure of this sufficient test. A blanket claim that the entire incoming-to-post step reduces phasewise scalar dispersion would also be contradicted by the measured increase phases, not merely unsupported by the bounds. None of these counts proves or disproves convergence over longer times.

The earlier incoming/outgoing phase-average indexing caveat remains intact. A nearly unchanged phase-averaged spread is not a new stabilization theorem.

## 8. Additional reviewer theorem: P weakly dominates K for these definitions

During proof review I derived a further mathematical relationship, documented in full in [ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md](ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md):

\[
\boxed{P_i\le K_i\ \text{for every center},\quad P\le K,\quad BEST\_PRE=P.}
\]

This is a **new reviewer deduction**, not a claim attributed to Codex's report. The result uses the already proved monotonicity of k and an exchange inequality for the weighted cost

\[
C(a,b)=k(\min(a,b))^2(a-b)^2.
\]

Its nonpositive mixed derivative makes sorted matching minimize this weighted cost; replacing signed components by magnitudes cannot exceed the original signed-interval cost. Together these give the weak ordering. Strictness is not universal, although it is observed in all submitted pair comparisons.

The submitted choice not to assert a universal ordering was conservative, not incorrect. No report, formula, table, figure or source correction is required. The theorem explains why BEST does not improve on P under these specific definitions; it does not make P tight or supply any missing nonincrease certificate. No new numerical population or family was evaluated to obtain this proof.

## 9. Figures and presentation

All six original PNG figures were displayed and inspected individually. I read the plot code and checked its plotted column choices against the verified data. The phase range is complete. Log axes in Figures 2 and 6 are identified. Pair means are not confused with variance aggregates; Figure 3 labels cross-history difference alignment; Figure 4 distinguishes inequality slack from causal attribution. Figure 5's small actual margins can look near zero on the shared scale, but the report explicitly points to the signed numerical classifications.

No figure correction or regeneration is required. Identities and review notes appear in `VISUAL_REVIEW.json`. No font files or regenerated scientific plots are included in this reviewer package.

## 10. Decision and next boundary

**Accept SIM04 within conditional finite-step-bound scope.** It answers the agreed question: the baseline is correct but loose, profile information materially improves it, and the remaining norm-projection and center-cancellation losses prevent the specified sufficient certificates. The actual dynamics are unchanged.

Preserve the completed report, proofs, numerical evidence, figures and this review before starting another scientific task. A future explanation should distinguish the submitted empirical ordering from the additional reviewer weak-dominance theorem. Do not rewrite the accepted report merely to insert the later result.

This review is internal GPT-assisted scientific review, not external peer review, journal acceptance or independent laboratory execution. It makes no Git write, licence grant, publication-payload approval or automatic follow-on authorization. No failure of the mathematical model is inferred from the failure of these particular sufficient conditions.

## 11. Reviewer files and reproducibility

The package contains this review, the additional theorem, the independent verifier and results, archive review, pre-output reviewer fingerprints, visual review, execution note, start receipt and a manifest. Reproduction requires the extracted SIM04 submission, its original ZIP and transport seal, the previously approved SIM03 corrected candidate ZIP, and the original SIM04 handoff ZIP. The script's command-line arguments identify those explicit inputs and require a separate fresh output directory.

Reproduction is not requested as part of accepting this review. The script refuses to overwrite an existing review start or results record. Its pass generated no new dynamics or random samples and did not execute supplied science code. The source archives themselves remain unchanged.
