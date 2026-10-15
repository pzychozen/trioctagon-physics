# SIM04 output fields, units and masks

This guide accompanies [OUTPUT_SCHEMAS.json](evidence/OUTPUT_SCHEMAS.json), which enumerates every exact NPZ field name, dtype and shape and every CSV column and row count. Formula definitions are in [MATHEMATICAL_RESULTS.md](MATHEMATICAL_RESULTS.md). Files use UTF-8 JSON/CSV; NPZ contains numeric/bool arrays without objects or pickle. Native speed and squared-speed units are distinguished; none is an SI calibration. Indices/counts, geometry normalization, gains, derivative coefficients and ratios are dimensionless in the inherited numerical convention. H and h are native source scalars; h=|0.1H| acts as the impulse scale.

## Keys, ordering and orientation

The ordered pair list is `(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)`, with pair_id 0–9. Pair/phase row r=`200*pair_id+phase`. All signed differences use c minus d. A center-pair row q=`8*r+center` has center 0–7 and three components in the inherited coordinate order. No center identities are matched or sorted. Profile sorting acts only on the three absolute components of one center velocity.

`selected_record_map.csv`: 8,000 rows ordered cycle, phase, center. `selected_row` is the zero-based selected order; `source_row` is the original NPZ row; `record_id` and `update_row` are original identifiers. `dataset_id` is 0 for cycle 0 and 2 for cycles 1–4; `update_index=200*cycle+phase`; `source_frame` is the stored source schedule index. These are metadata, not newly evolved states. Original input schemas are retained in `evidence/INPUT_MAP.json` and `inputs/evidence/`.

`cycle_phase_speeds.csv`: 1,000 rows ordered cycle/phase, containing incoming, pre_damping and post collective mean speeds (mean of eight norms, speed units). `phase_dispersion_bounds.csv` is ordered all_five phases 0–199, then new_four phases 0–199. Each view has m=5 or 4 cycles and ten or six unordered pairs. QA `view_phase_row` uses that order.

## Pre-output NPZ and pair fields

`PRE_OUTPUT_BOUNDS.npz` is sealed before outcomes. Its complete contents are also retained in `center_pair_bounds.npz`, followed by outcome diagnostics. Prefix `pair__` denotes a 2,000-element array; `center__` denotes 16,000 rows, with final dimension 3 for component vectors. `pair__pair_id/cycle_c/cycle_d/phase/update_c/update_d` are the keys just defined. The pair scalar fields have the same definitions as corresponding columns in `pair_phase_bounds.csv`.

| Field(s), ignoring prefix | Meaning | Units |
|---|---|---|
| OMEGA_COARSE, GAMMA_SOURCE, T_TRIANGLE, Q_VECTOR, K_COMPONENT, P_PROFILE, BEST_PRE | Seven fixed analytic pair bounds | speed |
| V, J | Mean norms of Δv, Δa | speed |
| best_is_K | K≤P; ties select K, otherwise P | Boolean |
| T_minus_Q | Raw triangle inequality slack | speed |
| Gamma_c_given_d, Gamma_d_given_c | Two source-factor expansions before minimum | speed |
| Rg | Mean norm of g_c−g_d | dimensionless |
| qbar_c, qbar_d | Mean norm of signed normalized geometry in each history | dimensionless |
| G_c, G_d, abs_delta_G | Stored incoming-speed gain and its absolute difference | dimensionless gain |
| H_c, H_d, h | Stored common driving value and abs(0.1H_c) | native source scalar |
| delta_v, delta_a, delta_w | Centerwise signed vector differences | speed |
| v_distance, a_distance, Q_center | Norms of preceding three vectors | speed |
| K_center, P_center, T_center | Center contributions to K, P, T | speed |
| difference_alignment | 2 Δv·Δa | speed squared |
| difference_cosine | Δv·Δa/(norm(Δv) norm(Δa)) | dimensionless |
| difference_cosine_valid | Both norm factors strictly positive; no near-zero ratio floor is imposed on this directional diagnostic | Boolean |
| alignment_residual | norm(Δw)²−norm(Δv)²−norm(Δa)²−2Δv·Δa | speed squared |
| triangle_slack | norm(Δv)+norm(Δa)−norm(Δw) | speed |
| contains_zero | Signed closed component interval contains 0, inclusive of endpoints | Boolean, three components |
| ell | Nearest absolute magnitude to 0 in that interval | speed |
| kappa | k(ell), signed-interval derivative maximum | dimensionless |
| profile_c, profile_d | Ascending absolute components of stored w | speed |
| lambda | k(min(profile_c,profile_d)) componentwise | dimensionless |
| profile_distance | Norm of profile_c−profile_d before derivative weighting | speed |
| g_c, g_d | (1−2bit)d/(norm(d)+0.01) from saved d and bit | dimensionless normalized geometry |
| pair_phase_row, center | Explicit center-to-pair key | integer |

An invalid difference_cosine is NaN only where its Boolean mask is false. There are no such cases in the selected population. Analytic bounds contain no NaN. `best_is_K` chooses a whole pair-average bound; it is not a per-center mixture of K and P.

## Outcomes, gaps and pair ratios

`outcome__` fields occur only in `center_pair_bounds.npz` after the seal: `post_delta_velocity=y_c−y_d`, `post_profile_delta=p(y_c)−p(y_d)`, their norms `post_signed_distance` and `post_profile_distance`, `signed_speed_difference=||y_c||−||y_d||`, and its absolute value `individual_abs_speed_difference`. All are in speed units; vectors have three components. They use saved successors, never a new D(w) evaluation.

In `pair_phase_bounds.csv`, `signed_collective_difference` is post collective mean speed c minus post collective mean speed d, and `observed_S` is its absolute value. In real arithmetic this equals the mean signed center speed difference; the implementation subtracts the separately reduced means, so last-bit differences from another reduction order are possible. `Zsigned`, `Zprofile` and `Tnorm` are the center means of the corresponding post distances and absolute speed differences. `Zstar` is Zsigned when best_is_K, otherwise Zprofile. Each `gap_A_to_B` is A−B, without clipping; Q_to_S is Q−S. `gap_telescope_residual` is Q−S minus the sum of the four adjacent saved gaps.

For any family F, `F_gap=F−S`, `F_utilization=S/F`, and `F_factor_over_outcome=F/S`. `F_utilization_valid` requires F≥1e−12; `F_factor_valid` requires S≥1e−12. For F=K/P/BEST, `F_improvement=Q−F`, `F_over_Q=F/Q` with Q≥1e−12 and the corresponding `F_over_Q_valid`. Invalid CSV ratios are blank, invalid JSON summary values are null; mask columns are explicit. Ratios are dimensionless, gaps and improvements are speed. Exact zero is counted separately from denominator masking. No output ratio is capped.

## Dispersion and conditions

For each stage (`incoming`, `pre_damping`, `post`), `stage_variance` is the centered ddof=0 variance of cycle collective speeds, `stage_pair_variance` is the independently formed complete unordered-pair sum divided by m², and `stage_SD=sqrt(stage_variance)`. For each F, `F_variance_upper=Σ F_cd²/m²` and `F_SD_upper` is its square root. The BEST pair minimum is taken before squaring/summing.

`F_variance_gap` and `F_SD_gap` subtract the corresponding actual post outcome from the bound. Utilization is actual/bound and factor is bound/actual, each with explicit `_valid` masks. Variance ratios use denominator≥1e−24; SD ratios use denominator≥1e−12. Variance and variance gaps are in squared-speed units; SD and SD gaps are in speed units. The ratio of aggregate SDs is separate from phasewise ratios or the ratio of variances.

`incoming_condition_margin` and `pre_damping_condition_margin` equal reference variance−BEST variance upper. `_actual_margin` equals reference variance−post variance. Each `_class` is PASS for margin>1e−14, NOT_ESTABLISHED for margin<−1e−14, UNRESOLVED otherwise. For the actual margin only, these encode observed decrease/increase/unresolved. A NOT_ESTABLISHED sufficient condition is not an actual-expansion claim. Exact-zero margin counts are retained in RESULTS separately.

## Summaries, residuals and locators

`bound_summary.csv` contains all seven families for all_pairs, new_four_pairs, ten individual pair families, and both dispersion views. `metric` distinguishes bound, outcome, gap, utilization and factor (with variance_/SD_ prefixes for views). `proof_slack_summary.csv` contains the six primary slack metrics and K/P/BEST improvement and over_Q metrics for the same pair groups, plus center alignment, cosine and triangle-slack distributions. Scope/family/metric/units identify each row. `count` is finite unmasked observations, `masked` is excluded observations, `exact_zero` counts exactly zero among resolved values. Means use math.fsum; quantiles use NumPy linear interpolation at 0, .05, .5, .95 and 1. Locator columns contain JSON with the two bracketing original keys and upper interpolation weight. Interpolated quantiles need not equal a single observation.

`phase_bound_means.csv` contains each phase's arithmetic mean across all ten unique pairs, for each bound, observed S, T−Q and the five Q-based gap metrics. `RESULTS.json` preserves these conventions, aggregate sqrt(mean variance), nested factor categories ≤2/≤5/≤10, exact-zero and unresolved counts, condition classes, fixed top-five rankings, alignment/interval/winner counts, stage times and the pre-output seal. Categories are cumulative and descriptive, not statistical thresholds.

`NUMERICAL_RESIDUALS.npz` retains every equality residual and signed inequality excess checked during the single pass. Each exact field has its axes, tolerance, kind, min/max signed values and min/max/max-absolute locators in [NUMERICAL_QA.json](evidence/NUMERICAL_QA.json). For an inequality named A_minus_B, the excess is A−B; a negative value satisfies A≤B. `negative_gap_*` is the negative of the named raw gap. Selected input arrays use (cycle,phase,center,component); pair, center and view axes follow the row mappings above. Equality residuals pass if absolute magnitude≤tolerance; inequality excesses pass if≤tolerance. All tests have zero relative tolerance. These are floating evaluations, not outward-rounded interval certificates.
