# SIM05 fields, units, masks and exact joins

[OUTPUT_SCHEMAS.json](evidence/OUTPUT_SCHEMAS.json) enumerates every exact NPZ field/dtype/shape and CSV column/row count. This guide defines their meaning. All paths in the schema are relative to the SIM05 root. Numerical arrays are float64 unless the schema specifies an integer, Boolean or Unicode metadata type; none is an object/pickle array. CSV/JSON are UTF-8. Speeds and squared speeds use native numerical units, without an SI calibration. Bounds and radii are deterministic analytic enclosures, not confidence intervals.

## Population and keys

The ten ordered pair IDs 0–9 denote `(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)`. All signed quantities are c minus d. Pair/phase row r=200*pair_id+phase, phase 0–199. Center-pair row s=8*r+center, center 0–7. A final dimension 3 denotes profile components in ascending absolute-value order; no center is relabeled. Node dimension 5 denotes fractions 0,.25,.5,.75,1 in squared-component coordinates. Four-quotient dimension 4 has the order specified below.

`join_map.csv` has 16,000 rows. Keys identify both canonical pair/phase/center order and `input_pair_source_row`, `input_center_source_row`, `outcome_center_source_row` in the unchanged SIM04 NPZ files. Explicit dictionary joins verify complete unique keys, not incidental file order. `inputs/analysis/selected_record_map.csv` is retained unchanged for original update/center identities: dataset 0 at cycle 0 and dataset 2 at cycles 1–4, update_index=200*cycle+phase. The population represents 1,000 saved updates and 8,000 distinct centers; those states were not reconstructed.

`phase_dispersion_intervals.csv` orders all_five phases 0–199 then new_four phases 0–199. `view`, `phase`, `cycles` and `pairs` identify each row. All_five has m=5 and ten unordered pairs; new_four m=4 and six reused pairs. QA `view_phase_row` follows this order.

## Archive layout and outcome boundary

`PRE_OUTPUT_INTERVALS.npz` contains `center__*` arrays (16,000 rows), `pair__*` arrays (2,000 rows), and `view__*` arrays (400 rows). It was hashed before outcomes. Its view arrays contain the analytic variance intervals; later CSV SD bounds are square roots of these sealed values, with no fitted change. Pair and center keys are included.

`center_intervals_and_outcomes.npz` retains the same center analytic fields plus `outcome__signed_speed_difference` and `outcome__individual_abs_speed_difference`, joined from the accepted saved records. These speed-unit fields are δ_i and abs(δ_i). It does not evaluate D/F. The original full accepted input NPZ files are copied unchanged, but only the logged allowlist was read for analytic evaluation.

## Center fields (omit prefix center__)

| Field | Meaning | Units |
|---|---|---|
| profile_c, profile_d, P_center | Unchanged stored profiles p,q and prior P_i | speed |
| x, y | p²,q² componentwise | speed squared |
| h | (p−q)(p+q), signed squared-component difference | speed squared |
| h_residual | h−(x−y), raw algebra residual | speed squared |
| nodes_z | Five fixed nodes between min(x,y) and max(x,y) | speed squared |
| theta_nodes | θ(sqrt(nodes_z)); all slots evaluated, including ties | dimensionless in native convention |
| L_p, U_p, L_q, U_q | Analytic norm envelopes m/b(M), m/b(m/sqrt(3)) | speed |
| denominator_lo, denominator_hi | L_p+L_q, U_p+U_q | speed |
| norm_difference_lo, norm_difference_hi | L_p−U_q, U_p−L_q | speed |
| both_zero | Both profiles identically zero; no quotient evaluated | Boolean |
| pair_phase_row, center | Explicit canonical row mapping | integer |

For each resolution J=1 or 4, prefix `J1_` or `J4_` is followed by:

| Suffix | Meaning | Units/type |
|---|---|---|
| theta_lo, theta_hi | Lower/upper Darboux average of derivative weights, per component | dimensionless |
| component_num_lo, component_num_hi | min/max of h times both derivative averages | speed squared |
| numerator_lo, numerator_hi | Signed sums of three component numerator endpoints | speed squared |
| four_quotients | N_lo/D_lo, N_lo/D_hi, N_hi/D_lo, N_hi/D_hi, in that order; all zero for both-zero case | speed |
| quotient_lo, quotient_hi | Minimum and maximum of four quotients | speed |
| raw_lo_original, raw_hi_original | Intersection of quotient and norm-difference envelopes before inversion handling | speed |
| raw_lo, raw_hi | Raw pre-P endpoints after prescribed outward hull, if needed | speed |
| raw_hull_flag | Original raw lower endpoint exceeded upper by a positive gap≤1e−12 | Boolean |
| raw_lo_from_quotient, raw_hi_from_quotient | Quotient endpoint selected at raw intersection; true includes a tie, identifiable from retained candidate values | Boolean |
| effective_lo_original, effective_hi_original | Raw interval intersected with [−P_i,P_i], before inversion handling | speed |
| lo, hi | Effective endpoints after prescribed outward hull, if needed | speed |
| effective_hull_flag | Positive effective inversion≤1e−12 | Boolean |
| roundoff_flag | Either raw or effective hull flag | Boolean |
| P_active_lo, P_active_hi | Prior endpoint strictly tightens corresponding raw endpoint | Boolean |
| P_tie_lo, P_tie_hi | Prior endpoint equals raw endpoint exactly | Boolean |
| midpoint, radius | (lo+hi)/2, (hi−lo)/2 | speed |
| raw_midpoint, raw_radius | Same for raw pre-P endpoints | speed |
| sign, raw_sign | +1 if lower>1e−12, −1 if upper<−1e−12, 0 otherwise; affected hull flags force 0 | integer classification |

The active endpoint comparisons refer to the intersection before any hull. All candidates and original inverted endpoints remain available. A positive inversion>1e−12 aborts, and underflow/overflow/invalid arithmetic raises. No production inversion occurred. The finite predeclared hull policy is not formal outward-rounded interval arithmetic and adds no fitted padding. An unresolved sign does not mean the true value is zero.

## Pair fields and aggregations

Pair keys are `pair_id, cycle_c, cycle_d, phase, update_c, update_d`. `P_PROFILE` is the inherited pair comparator, verified against mean(P_center), without reevaluating the old P formula. For each J, `RADIAL_J_UNSIGNED` and `RADIAL_J_SIGNED` alias the effective `J*_unsigned_upper` and `J*_signed_upper`.

Each J-prefix has the following pair aggregates; prefixing the suffix with `raw_` uses the raw pre-P center intervals instead:

| Suffix | Definition | Units |
|---|---|---|
| lo, hi | Mean center endpoints, collective signed interval | speed |
| midpoint, mean_radius, mean_abs_midpoint | Means of μ_i, ε_i and abs(μ_i) | speed |
| signed_upper | max(abs(mean(lo)),abs(mean(hi))) | speed |
| unsigned_upper | Mean max(abs(center lo),abs(center hi)) | speed |
| signed_lower | Zero if collective interval contains zero, otherwise smaller endpoint magnitude | speed |
| cancellation | unsigned_upper−signed_upper | speed |
| midpoint_identity_residual | signed_upper−(abs(midpoint)+mean_radius) | speed |
| unsigned_identity_residual | unsigned_upper−(mean_abs_midpoint+mean_radius) | speed |
| cancellation_identity_residual | cancellation−(mean_abs_midpoint−abs(midpoint)) | speed |

Further pair diagnostics (effective only): `positive_centers`, `negative_centers`, `unresolved_centers` count the eight sign classifications; `mixed_resolved_signs` reports at least one +1 and one −1. `collective_sign` applies the same endpoint threshold to the collective interval, forcing unresolved if any center had a hull flag. `roundoff_centers` and `prior_active_centers` count the corresponding center flags. `raw_to_effective_unsigned/signed` subtract the effective upper from the raw upper, retaining their signed floating values.

After sealing, `signed_collective_difference` is math.fsum of the eight saved signed center differences divided by 8, and `observed_S` is its absolute value. `accepted_signed_collective_difference` is the separately reduced accepted pair-CSV readout; `collective_reduction_residual` preserves their last-bit difference. `prior_reference_residual` compares inherited P to the accepted pair CSV. `observed_Tnorm` is the mean of the saved individual absolute differences.

`gap_P_to_unsigned4`, `gap_unsigned4_to_signed4`, `gap_signed4_to_S` and `gap_P_to_S` are the raw speed-unit differences named. `gap_telescope_residual` is the last gap minus the sum of the first three. `refinement_signed_J1_to_J4` and `refinement_unsigned_J1_to_J4` subtract J=4 from J=1. `J*_radius_minus_remaining_slack` equals mean_radius−(signed_upper−observed_S), and may have either sign.

For each of the five primary upper families and four raw upper diagnostic families, `family_gap=family−observed_S`, `family_factor=family/observed_S`, and `family_utilization=observed_S/family`. Factor validity requires observed_S≥1e−12; utilization validity requires family≥1e−12. Corresponding `_factor_valid` and `_utilization_valid` masks are explicit. Invalid ratios are blank in CSV and null in JSON summaries, not zero. Ratios are dimensionless and are not clipped. No actual pair upper ratio was unresolved; signed lower bounds can be zero and are not assigned an inverse tightness factor.

## View/phase dispersion fields

For each stage (`incoming`,`pre_damping`,`post`), `_variance` is centered ddof=0 variance of the accepted scalar speeds, `_SD` its square root, and `_pair_variance` is the complete-pair sum of squared speed differences divided by m². `_pair_identity_residual` subtracts centered variance from pair variance; `_reference_residual` compares to the accepted SIM04 variance. `P_variance_reference_residual` compares the new aggregation of existing P to its accepted aggregate.

For each primary or raw upper family, `_variance_upper` is sum of squared pair uppers divided by m²; `_SD_upper` is its square root. `J1_variance_lower` and `J4_variance_lower` sum squared corresponding signed pair lower bounds divided by m², and `J*_SD_lower` takes square roots. Raw-family names retain the `upper` word, e.g. `J4_raw_signed_upper_variance_upper`. Squaring occurs after pair aggregation, never centerwise in place of a pair bound.

`family_variance_gap/SD_gap` subtract the respective actual post variance/SD from its upper bound. `_factor` is bound/actual, `_utilization` actual/bound; `_valid` masks use denominator≥1e−24 for variance and≥1e−12 for SD. Variance fields and margins have squared-speed units; SD fields have speed units; ratios are dimensionless. No bound or gap is clipped. Phasewise factors are distinct from ratios of aggregate SDs.

`reference_actual_margin` is reference variance−post variance and `_actual_class` is DECREASE above 1e−14, INCREASE below −1e−14, UNRESOLVED otherwise. For J=1/4 and reference incoming/pre_damping, `J*_reference_decrease_margin=V_ref−W_upper`, `J*_reference_increase_margin=W_lower−V_ref`. Their independent `_class` columns are PASS above 1e−14, NOT_ESTABLISHED below −1e−14, UNRESOLVED in the closed band. Failure of one condition never supplies the other condition's classification. All values and all phases remain in the table.

## Summary tables and numerical QA

`bound_summary.csv` contains five primary and four raw upper families for all_pairs, new_four_pairs, ten individual pair families, and both dispersion views. Each row identifies scope/family/metric/units, count/masked/exact_zero, min/p05/median/p95/max/mean, and quantile locators. `gap_summary.csv` contains the three-step gap ladder, total gap, resolution improvements, signed lower bounds, midpoints, radii, cancellation, raw/effective differences and radius-minus-slack, for the same pair groups. Means use math.fsum; quantiles are linear. Locator objects record lower/upper bracketing source keys and upper interpolation weight. An interpolated quantile is not claimed to be one exact observed row.

`phase_interval_means.csv` records complete phase curves of arithmetic means over all ten unique pairs, distinct from dispersion/variance aggregation. `RESULTS.json` preserves these summaries, nested factor≤2/≤5/≤10 categories checked through native-unit products, sign/prior/refinement/hull counts, aggregate sqrt(mean phase variance), two-sided margin statistics and PASS phase lists, exact-zero/unresolved counts, and fixed top-five extreme locators. All source populations are dependent saved histories; these are descriptive, not independent-trial statistics.

`NUMERICAL_RESIDUALS.npz` retains all 96 signed check arrays. For an inequality residual A_minus_B, nonpositive means A≤B; `negative_gap` negates the named gap. Equality residuals are compared in absolute value. Every array's kind, shape, axes, tolerance, signed minima/maxima and max-absolute locator are in [NUMERICAL_QA.json](evidence/NUMERICAL_QA.json). Scalar native checks use 1e−12, variance 1e−14, and relative tolerance is zero. Numerator fixture checks use 1e−12 in squared-speed units. No positive numerical inequality excess occurred in production. This evidence verifies floating consistency with the real-valued proofs; it is not a formal interval-arithmetic certificate.
