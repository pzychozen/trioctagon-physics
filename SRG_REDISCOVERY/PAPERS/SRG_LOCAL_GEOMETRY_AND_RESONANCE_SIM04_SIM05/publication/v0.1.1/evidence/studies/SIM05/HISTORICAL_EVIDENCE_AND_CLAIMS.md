# Historical evidence and claim audit

## Preserved attribution chain

**ORIGINAL:** [srg_infinity.py](originals/srg_infinity.py), [srg_infinity_asymptotic.csv](originals/srg_infinity_asymptotic.csv), and [SRG_Infinity_Seeds.md](originals/SRG_Infinity_Seeds.md) are unchanged copies. They match the reviewed R0 copies, the handoff ZIP members, the resolved extracted originals and the selected members of `research_files/sources/Zenodo_research/19023429/simulations.zip`. The archive SHA-256 is `731b980fa2f09a8f433c4ff92bd0fcbb455e563790bdf85c556b111b36abd477`. [Selected origin records](context/SELECTED_ORIGIN_RECORDS.json) retain exact original paths and hashes; [archive verification](context/march_archive_verification.json) is retained context and the three selected members were independently matched here.

| Input | Bytes | SHA-256 |
|---|---:|---|
| srg_infinity.py | 33529 | 742e40f1b4326f3ea5c8c88bd59aec7ee5a2bb942755a0fbc1861ce7c5eddf9d |
| srg_infinity_asymptotic.csv | 70327 | 116159914e9b1ee844d4e2992af3859bb6cf0eb1cf6472d09265cd2ae1bc6ed7 |
| SRG_Infinity_Seeds.md | 7040 | d105b46d734d1adb7babb65d469340862cdc07ff0abb172a3126aec153c6845d |

**ATTRIBUTED:** The CSV filename, schema, selected source driver (282–349), accompanying account, and present replay agreement strongly connect it to the 50-point seed-2038 asymptotic experiment. The script and note carry March 14, 2026 labels and Claude/pzychozen attribution. These are artifact statements, not independent certification of execution date or software environment. The full historical RNG state and dependency versions remain **MISSING/AMBIGUOUS**.

No original Infinity movie, image or full per-point trajectory is identified in this selected evidence chain. The retained March archive inventory contains 38 source/data/text members and no original image/movie. This is a scoped inventory result, not a claim that no such evidence exists anywhere. The GPT SIM04 review figure is later analysis of SIM04 data, not an Infinity recording. Every figure in this study is newly generated and labeled accordingly.

## What the original table permits us to check

**OBSERVED IN HISTORICAL DATA:** 200 finite rows, in saved order, with unique consecutive pass labels 1–200 and 21 columns. There is one aggregate row per selected pass, without animation callbacks. It does not contain pass-0 state or the complete 50-point arrays. Original row order and number formatting are preserved in the original copy. [Historical checks](analysis/historical_checks.json) and [per-column comparison](analysis/historical_replay_columns.csv) are derived evidence.

The ratio, coherence and maximum-versus-leading-amplitude identities reproduce exactly as parsed. H differs by at most 2.23e−16 in the current numerical environment. `matter_energy = 50*(R_std²+R_mean²)` agrees within 6.67e−16. Because R_mean means mean absolute R whereas R_std uses signed R, this last equality is conditional on a common sign (or negligible opposite-sign contribution at recorded precision); it must not be asserted as an unconditional identity for arbitrary states. Together with positive leading values it supports the positive regime, but the aggregate record cannot reconstruct all signs and amplitudes independently. The replay directly records positivity.

On all 179 consecutive transitions whose leading ID is unchanged, the distance between its saved coordinates reproduces its GRF exactly via `1/(1+distance)`. When the ID changes, subtracting consecutive leading coordinates follows different points and is not a velocity. Counts and IDs are integral and within their source domains. All 4,000 non-pass metric comparisons are retained, including the small discrepancies; there is no fitting to the historical values.

## Claim-by-claim disposition

| Historical claim / locator in note | Relevant source and evidence | Present disposition |
|---|---|---|
| Central claim: all 50 share R=.176329, one uniform condensate | CSV p200: maximum .17632905865276288, mean .15120339574262398, std .020441937084602013 | **Contradicted for exact whole-field uniformity.** Mean differs and variance is positive. The replay resolves distinct, internally similar components; it does not turn missing historical geometry into original evidence. |
| §1: ~.05% final-ten drift is a true fixed point | Source 296–303 calls a population coefficient of variation “drift”; R_max final-ten CV=.00050336848 (0.05034%); Rg CV=.0121913831 (1.219%) | **Finite observable stability only.** CV is neither endpoint drift nor a convergence proof. It does not establish stationary coordinates, an infinite-time limit or a uniform field. |
| §1: top seed stabilizes | Source 305–308 tests the set of top IDs in last 20 rows | Historical last20 IDs are **3, 11, 31, 32, 45**. Rank persistence occurs over other finite windows; this particular set is not a singleton. |
| §1: coherence ~.865, 238 corridors, 44 candidates | Source 207–268 and endpoint CSV | **Supported as defined observers.** A count of 44 threshold candidates is not 44 autonomous bodies or all 50 points; 238 echo scores are unordered pair threshold hits, not graph edges. |
| §§1–2: H is ignition, no longer fuel; memory death proves indefinite self-sustaining behavior | Selected H decays, but source retains other terms. Separate memory experiment 477–540 uses seed42, 50+50 passes | **Partly source-supported, broader conclusion unsupported.** Small direct H is established; indefinite autonomous persistence is not. No raw seed42 history supplied. No memory-death experiment was executed here. |
| §2 dark-field change after memory removal | `dark_at_50` copied at line531 after pass100 | **Observer defect:** both dark “50” and “100” energies read the same final array; printed zero change follows by construction. R50 and X50 were correctly copied earlier. |
| §3 triaxial ellipsoid and polyhedral superposition | Eigengeometry 356–470 selects top12 by absolute R, forms angle windows and an amplitude-scaled inertia-like tensor | **Historical interpretation.** Unequal moments describe a sampled tensor, not an ellipsoidal surface. Broad, overlapping windows are not a polyhedron fit or proof of multiple solids. No selected-run original plot/printed table survives here. |
| §4 seed body of 13 with flat radial profile proves uniform condensate | Anatomy 708–815 uses radius=25th percentile of distance to top point, then body distance<2radius; fits three forms | **Subset and observer dependent.** The code comment about two standard deviations is inaccurate. A possibly flat selected body cannot prove whole-field uniformity. Fit success, minimum RMSE and large fitted width do not establish an underlying law. Raw fit outputs are absent. |
| §5 dark squared-sum ratio is small and declines | Historical ratio from .000122546 at p1 to .0000371209 at p200 | **Small endpoints supported; monotone decline false:** 96 of 199 transitions increase. Ratio is not pointwise D/R or a physical energy fraction. Positive dark_energy rules out D identically zero in each saved aggregate row. |
| §5 phase orthogonality decouples channels; RPCO suppresses the weaker field | Coupling 114–137 explicitly connects fields; both use exactly the same signed RPCO | **Not supplied by the equations.** No relative normalization selects the stronger field. The offset alone supplies neither complex phase orthogonality nor a decoupling theorem. Three lower D clips in replay amplify magnitude to a floor. |
| §6 golden proportions / angle matches | Golden experiment 547–619 uses N80, seed1618, 150 passes and spatial interval [−6,6); other geometry observer uses selected field | **Distinct experiment and heuristic matches.** No raw full history for that experiment is provided. Loose ratio tolerances and azimuth observations do not show an emergent golden law. No phi appears in the selected movement or fusion expression. |
| Zeta-tier mechanism | Zeta experiment 626–701 uses N60, seed1202, 200 passes; post-run events compare `.05*H/M` to supplied zeta values | **Postprocessing hypothesis.** It does not estimate the literal dynamic gamma=.08699 or insert a zeta-dependent movement law. No execution here. |
| §7 proposed perturbations, horizons and different channels | Historical proposals | **HYPOTHESIS / future suggestions only.** None is part of this assignment. |

## Static observer issues that matter mathematically

The top12 eigengeometry observer subtracts their arithmetic center, then sets `weighted_pos = relative * top_R[:,None]` (source 440; tensor loop 442–445). Forming the quadratic tensor from these vectors weights squared position terms by **R²**, not by R as conventional point masses would. It is an internally defined descriptor, not automatically the mass inertia of this field.

For any vectors u_i, its tensor is `I=Σ(||u_i||² identity−u_i u_iᵀ)`. If M=Σu_i u_iᵀ has eigenvalues μ1≥μ2≥μ3≥0, the ordered moments are I1=μ1+μ2, I2=μ1+μ3, I3=μ2+μ3. Therefore `I1≤I2+I3≤2I2`. The source's strict `I1/(I2+1e−10)>2` “PROLATE” branch cannot occur for this positive semidefinite construction in exact arithmetic. A line-like set instead has I1≈I2 and small I3, which enters its “OBLATE” ratio branch. These source labels should not be used as geometric certification. No source correction or synthetic engine run was used to establish this identity.

The angle observer compares angles to several fixed values with ±10° windows, which overlap. Its pair distances use adjacent sorted distances and broad golden-ratio proximity windows. Those operations describe chosen comparisons, with neither a fitted point-to-vertex correspondence nor a null-model assessment. The anatomy fits additionally require SciPy optimization and sklearn, but these driver imports and fits were not executed.

The original main (822–837) runs the selected asymptotic field, eigengeometry, memory death, golden structure, zeta tower and anatomy. Import-time output-directory creation is at 36–37. Executing that launcher would exceed this work order. All excluded functions were reviewed as source only.
