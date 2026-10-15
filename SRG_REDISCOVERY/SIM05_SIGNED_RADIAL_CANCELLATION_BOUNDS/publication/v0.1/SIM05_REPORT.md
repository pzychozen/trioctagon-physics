# SRG-SIM05 — Signed radial intervals and collective cancellation

Research report v0.1 · 14 October 2026 · For GPT scientific review

Human research author and owner: Hilmir Frímann Halldórsson. Scientific direction and proposed construction: GPT. Independent mathematical verification, implementation and bounded saved-data analysis: Codex.

## Scientific answer

Keeping signed radial information materially improves the conditional collective-speed bound. With the prescribed four subintervals, the aggregate SD upper bound is **1.08422 times** observed SD for all five cycles and **1.07807 times** for the four continuation cycles. The inherited P factors are 3.88305 and 3.80087. Much of the improvement comes specifically from postponing absolute values until after averaging the same center intervals: the J=4 unsigned factors are still 2.25293 and 2.17389.

The new bounds establish useful finite-step sufficient conditions in **both directions**. At J=4 they certify damping-stage variance decrease at all 200 all_five phases and 198 of 200 new_four phases. Relative to incoming variance, they certify 111 decreases and 56 increases for all_five, and 108 decreases and 58 increases for new_four. Each remaining phase has neither sufficient test passing. No certificate contradicts the saved actual direction.

This is an improvement in bounds on a known scalar readout of realized inputs. It does not strengthen the model's damping, alter a trajectory, establish full-state contraction, or prove long-time convergence. The remaining uncertainty is retained rather than replaced by an exact evaluation of the response.

## Provenance and exact scope

SIM04's accepted submission and complete subsequent GPT review remain unchanged. The accepted submission ZIP is 21,653,622 bytes, SHA-256 `d3be3e9829181378f1e0e3af696d5cfe8de98c8a697ee59677c0edd5036e2987`; the ten-member reviewer ZIP is 138,546 bytes, SHA-256 `b2dbaf8d327e354ea04d3726c15a77d3e0bdeda09abaf35de954492fc38e17dd`. The source gate checked all 12 specified SIM04 files and their inspected schemas. It also matched every accepted submission member to the original local file. The full reviewer archive and its ten manifest-covered contents are included unchanged in this handback; its verifier was not run.

The input is the sealed [SIM04 PRE_OUTPUT_BOUNDS.npz](inputs/analysis/PRE_OUTPUT_BOUNDS.npz), SHA-256 `5df03134e083e9879458eb8a0d560c3c1e9bd91f6a57b6d8c367e0a3ed749e6f`. Only its 12 permitted key/profile/P fields were read analytically. Existing `profile_c`, `profile_d`, `P_center` and `P_PROFILE` were reused. No upstream center reconstruction, original velocity/position array, engine or old checker was evaluated.

The authority chain is explicit: [SIM04 mathematical results](inputs/MATHEMATICAL_RESULTS.md) supplies the damping derivative and scalar-profile facts; the later [GPT profile-dominance theorem](review/ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md) establishes universal weak P≤K, beyond the original report's empirical ordering. That theorem is inherited here and is not retroactively inserted into SIM04. The new signed-radial proposal is [SIM05 mathematical specification](received/SIM05_MATHEMATICAL_SPEC_v0.1.md); its independent proof check is [MATHEMATICAL_RESULTS.md](MATHEMATICAL_RESULTS.md). [INPUT_MAP.json](evidence/INPUT_MAP.json) supplies every source path, hash, role and schema.

The calculation represents the same 1,000 saved updates and 8,000 distinct centers, with the inherited prefix counted once and CONTINUOUS excluded. All ten c>d cycle pairs have phases 0–199: (1,0), (2,0), (2,1), (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (4,3). The single pass evaluated **2,000 pair/phase comparisons, 16,000 center pairs, 48,000 component pairs and 240,000 derivative-node slots**, then 400 dispersion summaries. J=1 reused the endpoint nodes of J=4. The new_four summaries reused six pair families, with no additional primary evaluation. [join_map.csv](analysis/join_map.csv) retains explicit keys and input/outcome source-row identities.

All analytic center, pair and population intervals were sealed before numeric outcomes or scalar references were loaded. [PRE_OUTPUT_INTERVALS.npz](analysis/PRE_OUTPUT_INTERVALS.npz) is 14,846,155 bytes, SHA-256 `e677d5bec55fee9b6a47cd6c8c148d3177e6ae9741926f6ca1ba8f29f8b2bc20`. The [seal](analysis/PRE_OUTPUT_INTERVALS_SEAL.json) records zero outcome joins at that point; the [access log](evidence/DATA_ACCESS_LOG.json) records subsequent reads. This is an auditable information boundary, not a claim of blinding to earlier reports.

## Checked construction

For one labeled center let p,q be the ascending absolute-component profiles and let P_i be its inherited valid bound. For the proof only, write b(s)=1+log(1+s), d(s)=s/b(s), and F(p)=norm(d(p)). The desired signed difference is δ_i=F(p)−F(q). Production never evaluates d or F on saved records.

Define Φ(z)=z/b(sqrt(z))². Independent differentiation gives

\[
\Phi'(z)=\vartheta(\sqrt z),\qquad
\vartheta(s)=\frac{b(s)-s/(1+s)}{b(s)^3}=\frac{k(s)}{b(s)}.
\]

The right derivative at zero is 1. Since k>0 and k'<0, θ'=k'/b−k/[(1+s)b²]<0. Thus Φ is increasing and concave. This analytic argument is checked before fixtures; numerical sampling is not its proof.

For each component, use x=p², y=q² and h=(p−q)(p+q). Five fixed nodes uniformly partition [min(x,y),max(x,y)] in the **squared-component coordinate**. At J=1, the endpoint θ values bound its integral average. At J=4, the four right/left endpoint averages give lower/upper Darboux bounds. Multiplication by signed h and summation across components give a numerator interval [N⁻,N⁺] for F(p)²−F(q)². Positive and negative component changes remain signed.

Without computing F, use

\[
L(p)=\frac{\|p\|}{b(\max p)},\qquad
U(p)=\frac{\|p\|}{b(\|p\|/\sqrt3)},\qquad L(p)\le F(p)\le U(p).
\]

The lower inequality follows from monotonic b; the upper follows from Jensen's inequality for concave Φ. Unless both profiles are zero, the positive denominator F(p)+F(q) lies in [L(p)+L(q),U(p)+U(q)]. The extrema of the four numerator/denominator endpoint quotients enclose δ_i. Intersect with [L(p)−U(q),U(p)−L(q)] to obtain the **raw** radial interval, then with [−P_i,P_i] to obtain the **effective** interval [l_i,r_i]. Both-zero inputs give [0,0] directly, without epsilon or invalid division. Equal profiles give a zero numerator and exact zero interval. All nodes are retained even for zero-length component intervals.

With midpoint μ_i=(l_i+r_i)/2 and radius ε_i=(r_i−l_i)/2, the collective interval is [mean(l_i),mean(r_i)]. Its signed-averaging upper bound and the unsigned alternative are

\[
B_J=|\overline\mu_J|+\overline\epsilon_J,
\qquad U_J=\overline{|\mu_J|}+\overline\epsilon_J.
\]

Their exact difference is `U_J−B_J=mean(abs(μ_J))−abs(mean(μ_J))`. The absolute lower bound A_J is zero when the collective interval contains zero and otherwise its lesser endpoint magnitude. Therefore

\[
A_J\le |\Delta u|\le B_J\le U_J\le P,
\quad A_4\ge A_1,\quad B_4\le B_1,\quad U_4\le U_1.
\]

The five primary families are P_PROFILE, RADIAL_1_UNSIGNED (U₁), RADIAL_1_SIGNED (B₁), RADIAL_4_UNSIGNED (U₄), and RADIAL_4_SIGNED (B₄). Raw pre-P variants are retained separately. No strict improvement was assumed, and no additional resolution or outcome-selected family was introduced.

For m cycles the complete unordered-pair identity is `Var(u)=Σ_{c>d}(u_c−u_d)²/m²`. Summing squared A and B gives two-sided variance bounds W⁻≤Var(u⁺)≤W⁺, using denominators 25 and 16. Joint attainability of all endpoints is not required for validity and is not claimed. `V_ref−W⁺>0` suffices for decrease; `W⁻−V_ref>0` suffices for increase. The fixed numerical passing margin is greater than 1e−14. For any declared ε≥0, B≤ε also suffices for a pair difference≤ε, and W⁺≤ε² for SD≤ε; no ε is fitted here.

## Full-population tightness

Aggregate SD is **sqrt(mean phase variance)**, not mean phasewise SD. Native speed units are retained, without physical calibration. Observed post aggregate SD is 0.009236017385892267 (all_five) and 0.009249450604392176 (new_four).

| Upper family | All_five aggregate SD | Factor | New_four aggregate SD | Factor |
|---|---|---|---|---|
| P_PROFILE | 0.03586395181 | 3.883053736 | 0.03515595153 | 3.800869157 |
| RADIAL_1_UNSIGNED | 0.02147331032 | 2.324953432 | 0.02072716033 | 2.240907187 |
| RADIAL_1_SIGNED | 0.01056442397 | 1.143828939 | 0.01048427617 | 1.133502585 |
| RADIAL_4_UNSIGNED | 0.02080811938 | 2.252932029 | 0.02010729615 | 2.173890862 |
| RADIAL_4_SIGNED | 0.01001382988 | 1.084215139 | 0.009971513893 | 1.078065533 |

The J=4 aggregate lower SD bounds are 0.008473982478526586 and 0.008504864539739755; J=1 gives 0.007886312643840824 and 0.007895369319349829. These are deterministic enclosures, not confidence intervals or uncertainty from independent trials.

| Pair upper / observed S | Min | p05 | Median | p95 | Max |
|---|---|---|---|---|---|
| P_PROFILE | 1.46588627 | 1.873532636 | 4.646169246 | 43.54668098 | 42300.98284 |
| RADIAL_1_UNSIGNED | 1.007378211 | 1.375578143 | 3.058701314 | 30.97683254 | 25045.17703 |
| RADIAL_1_SIGNED | 1.004239847 | 1.00808575 | 1.0535436 | 2.011753634 | 452.972779 |
| RADIAL_4_UNSIGNED | 1.004643053 | 1.348626058 | 3.023093258 | 30.28224331 | 24997.16849 |
| RADIAL_4_SIGNED | 1.00292217 | 1.004928354 | 1.029527549 | 1.493862562 | 223.2978573 |

Every pair upper-bound factor/utilization denominator is resolved; there are no exact-zero outcomes or primary upper bounds. Within descriptive factors 2/5/10, J=1 signed has 1,899/1,977/1,985 pairs; J=4 signed has 1,945/1,985/1,991 of 2,000. Inherited P has 179/1,083/1,559. These categories are cumulative reporting aids, not acceptance gates or significance levels. Native-unit products are used for category comparisons, and no large ratio is capped.

Both signed resolutions lie within factor 2 of observed SD at **every phase in both views**. J=4 phasewise SD factors range from 1.00402148 to 1.36075418 in all_five and 1.00375448 to 1.48234203 in new_four. Both maxima occur at phase 17. J=4 strictly improves both signed and unsigned upper bounds by more than 1e−12 at all 2,000 pair comparisons, but signed averaging of J=1 already does most of the tightening. [Figure 1](plots/01_profile_unsigned_signed.png), [Figure 2](plots/02_fixed_resolution_enclosures.png) and [Figure 6](plots/06_full_phase_tightness.png) retain every phase. Full raw/effective distributions and locators are in [bound_summary.csv](analysis/bound_summary.csv) and [RESULTS.json](analysis/RESULTS.json).

## What produces the improvement, and what remains uncertain?

For the same J=4 intervals, signed averaging reduces the upper bound by a mean **0.01431546678** in speed units, median 0.008538304795, maximum 0.11769237204125564. The gain exceeds 1e−12 at 1,998 comparisons and is exactly zero at two. These are midpoint cancellation gains, not a claim that the midpoint equals the true difference.

J=1 establishes positive/negative center signs for 7,929/7,924 center pairs, leaving 147 unresolved. J=4 gives 7,981/7,970, leaving 49 unresolved. Both signs are established among the eight centers at 1,996 J=1 pairs and 1,998 J=4 pairs. Collective signs are positive/negative/unresolved in 964/943/93 J=1 pairs and 982/963/55 J=4 pairs. A sign requires an interval endpoint beyond ±1e−12; an interval crossing zero is not assigned the midpoint's sign.

The mean collective radius falls from **0.001251712327** at J=1 to **0.000682317956** at J=4. J=4's median radius is 0.0000994962152 and its maximum is 0.01011231467. It remains explicitly in B. The J=4 mean remaining upper slack, 0.000679807314, is close to the mean radius, but they need not agree row by row: `B−S=mean(ε)+abs(mean(μ))−abs(mean(δ))`. [Figure 3](plots/03_cancellation_and_uncertainty.png) separates cancellation from uncertainty.

The exact post-join gap ladder separates within-center improvement from signed averaging:

\[
P-S=(P-U_4)+(U_4-B_4)+(B_4-S).
\]

| Gap (native speed) | Mean | Median | p95 | Maximum |
|---|---|---|---|---|
| P−U₄: center enclosure | 0.01390157699 | 0.004991515722 | 0.06691931802 | 0.1500841112 |
| U₄−B₄: signed averaging | 0.01431546678 | 0.008538304795 | 0.04283661142 | 0.117692372 |
| B₄−S: remaining slack | 0.0006798073141 | 9.767924517e-05 | 0.004159961151 | 0.01082813538 |
| P−S: total | 0.02889685108 | 0.01510545101 | 0.1104557572 | 0.2376134341 |

These gaps locate information losses in inequalities, not causal shares of motion. [Figure 4](plots/04_fixed_gap_ladder.png) shows their complete phase means. The full distributions and extrema are retained in [gap_summary.csv](analysis/gap_summary.csv).

The prior-P intersection is not the main source of tightening. It changes endpoints at 148 of 16,000 J=1 center pairs (143 pair comparisons) and only nine J=4 center pairs (nine comparisons). The other 15,852 and 15,991 raw intervals are unchanged. Mean raw-to-effective signed-upper reductions are 6.936185055e−6 and 1.924201954e−8. Raw J=4 aggregate SD factors are 1.084215973 (all_five) and 1.078065533 (new_four), essentially the effective factors shown above. Neither effective unsigned nor signed bound equals P, even within 1e−12, at any recorded pair. Raw intervals, every intersection endpoint and active/tied endpoint flags remain available; no raw result has been replaced by only its final intersection.

Representative fixed extrema are:

| Quantity | (c,d,j) | Value |
|---|---|---:|
| Largest P−U₄ | (4,2,9) | 0.1500841112152928 |
| Largest U₄−B₄ | (4,0,6) | 0.11769237204125564 |
| Largest B₄−S | (4,0,7) | 0.01082813538092775 |
| Largest B₄/S | (4,0,5) | 223.29785726515752 |

At the last locator, S=`3.54320366678304e−5` and B₄=`0.00791189786646702`: aggregate tightness does not imply uniformly small pair factors. At (4,0,105), S=`3.8740651284912067e−7` and B₄=`4.802671705279898e−5`, still a resolved factor 123.96982358296971. These unfavorable comparisons remain in every summary.

## Sufficient decrease and increase, kept separate from actual change

Both tests compare the signed variance enclosure with each reference independently. PASS requires margin>1e−14; NOT_ESTABLISHED requires margin<−1e−14; the closed tolerance band is UNRESOLVED. Actual change uses V_ref−V_post and the corresponding DECREASE/INCREASE/UNRESOLVED labels.

| View | J | Reference | Decrease PASS | Increase PASS | Neither PASS | Actual decrease / increase |
|---|---|---|---|---|---|---|
| all_five | 1 | incoming | 94 | 49 | 57 | 127 / 73 |
| all_five | 1 | pre_damping | 193 | 0 | 7 | 200 / 0 |
| all_five | 4 | incoming | 111 | 56 | 33 | 127 / 73 |
| all_five | 4 | pre_damping | 200 | 0 | 0 | 200 / 0 |
| new_four | 1 | incoming | 97 | 51 | 52 | 125 / 75 |
| new_four | 1 | pre_damping | 189 | 0 | 11 | 200 / 0 |
| new_four | 4 | incoming | 108 | 58 | 34 | 125 / 75 |
| new_four | 4 | pre_damping | 198 | 0 | 2 | 200 / 0 |

All individual test margins are outside the tolerance band, with no exact zero. “Neither” in this table means both sufficient tests are NOT_ESTABLISHED, not a tolerance-unresolved margin. No decrease PASS coincides with an actual increase, nor an increase PASS with an actual decrease. In particular, the existing incoming increases remain present and are often certified by the new lower bound.

For all_five, the smallest J=4 damping-stage decrease margin is **4.667115994392145e−8**, at phase 199. For new_four, the only nonpassing J=4 decrease phases are **17 and 57**:

| new_four phase | Pre-damping variance | Post variance | J=4 upper variance | Decrease-test margin |
|---|---:|---:|---:|---:|
| 17 | 2.1503489935648794e−5 | 1.4456889790840702e−5 | 3.1766671751416666e−5 | −1.0263181815767872e−5 |
| 57 | 1.9862074055878104e−7 | 1.887795458905935e−7 | 2.1670916353369462e−7 | −1.808842297491358e−8 |

Both have an actual damping-stage decrease; failure of the sufficient comparison does not reverse that observation. Full two-sided margins and actual changes are in [phase_dispersion_intervals.csv](analysis/phase_dispersion_intervals.csv). [Figure 5](plots/05_two_sided_conditions.png) displays both resolutions and both reference stages on a labeled symmetric-log scale; its display transition at 1e−8 does not change the 1e−14 classification threshold.

## Verification, preservation and conclusion

The independent proof check preceded the **14 fixed synthetic groups**, which passed **816 assertions**. The fixtures made 41 pure pair calls and 65 synthetic reference-D array calls covering 1,560 scalar components, including the prescribed variance and isolation cases. No D/F evaluation occurred on saved records. The single primary pass passed **96 signed numerical check arrays**, including raw/effective containment, nesting, averaging identities, complete-pair variance identities and both sufficient-condition directions. No interval inversion or positive inequality excess occurred.

The inherited P mean and P reference values match exactly. Actual stage variances match their accepted references exactly; the largest complete-pair variance identity residual is 8.673617379884035e−19. Subtracting separately reduced accepted collective means differs from the new mean of signed center differences by at most 9.71445146547012e−17; this residual is retained, explaining last-digit changes in some factor summaries. The gap-telescope maximum absolute residual is 2.7755575615628914e−17. [NUMERICAL_QA.json](evidence/NUMERICAL_QA.json) supplies every signed extremum and exact locator; [NUMERICAL_RESIDUALS.npz](analysis/NUMERICAL_RESIDUALS.npz) retains all values. Absolute tolerances remain 1e−12 for native interval/speed identities and 1e−14 for variance, with zero relative tolerance and no clipping. This is not formal outward-rounded interval certification.

Supervised fixture, primary and figure wall times were **1.297 s, 7.984 s and 6.172 s**, below their 60/300/120 s caps. Each ran once; no retry, extra resolution or presentation correction occurred. All six figures were inspected. A file-only metadata-print KeyError was resolved before input preparation and before any fixture or scientific execution; its event record is retained. [SIM05_EXECUTION_RECEIPT.md](SIM05_EXECUTION_RECEIPT.md) and the external transport seal record exact execution, archive and size accounting.

The accepted SIM04 submission, full GPT review, 97 protected SIM04 files, repository index and ten unrelated modified tracked files remain unchanged. Actual local HEAD is the pinned SIM03 checkpoint `e1f5115402a05965834493c1254b03118a531c92`; no remote state or SIM04 publication is asserted. No trajectory, centroid reconstruction, RNG operation, old checker, engine, model change, paper build or Git write occurred.

The signed-radial method is worth retaining as a conditional finite-step comparison: it removes much of the earlier scalar-projection and center-cancellation overestimate and establishes both decrease and increase conditions without requiring a desired direction. Its limits are visible in the unresolved collective signs, the two new_four damping phases without a certificate, and large relative errors at near-cancelling pairs. It remains conditioned on realized profiles, with algebraic uncertainty rather than statistical confidence. No higher resolution or follow-on experiment has been launched. Handback is for GPT scientific review.
