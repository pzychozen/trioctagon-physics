# Exact construction of GlyphFieldInfinity

**ORIGINAL / DERIVED.** All line numbers below refer to the unchanged [837-line original](originals/srg_infinity.py). The full script was read as text. It was never imported or launched. Only [the mechanically verified core](audited_core.py) was executed; [CORE_IDENTITY.json](CORE_IDENTITY.json) records original ranges 43–55 and 61–275, required imports, LF normalization and AST equality.

## What exists and what persists

The selected constructor at lines 287–288 creates N=50 points, X in real N×3 coordinates, real arrays R and D of length N, a real N×3 displacement array V, integer pass p, parameters and NumPy's global RNG. In order, it resets the RNG with seed 2038, draws X uniformly from [−5,5), draws R independently from [0,.3), draws another independent uniform array on [0,.3) and multiplies it by .01 to initialize D, then sets V=0 and p=0 (70–82). Initial D is not `.01*R`.

Parameters (85–91): alpha=.05, beta=.15, lambda_H=.05, L=9, k=5, omega=.244, gamma=.08699; the offset is pi/2 (79). Machine constants include distance regularizer 1e−8, fusion-center weight regularizer 1e−8, RPCO epsilon 1e−9, angle denominator 1e−10 and observer-specific guards below. No physical units or mass calibration are supplied.

X,R,D,p and the RNG determine the successor. V is overwritten with the latest displacement and is used by observers only. `metrics_history` accumulates 200 dictionaries. `seed_history` and `grf_history` are allocated but never populated by this class (94–96); no complete per-glyph history is saved by the original selected driver. The replay's state recorder is external.

The domain has no coordinate wrapping, collision surface, fixed spatial boundary or toroidal distance. The initialization box is a draw range. The Euclidean measuring coordinates do not act as a material container.

## One update in exact execution order

Write the incoming boundary as (X,R,D,p−1), and the new pass as p. Define

\[
H(t)=2e^{-t/2}\cos t+e^{-3t/10}\sin t+\tfrac32e^{-7t/10}+e^{-2t/5},
\quad M=\max_{t\in\operatorname{linspace}(0,100,50000)}|H(t)|+10^{-12}.
\]

The sampled normalization M is computed once (43–55), and equals 4.500000000001 in this execution. A pass advances the counter by exactly one (162–165). There is no animation callback, repeated frame label, accumulated floating `dt`, or seconds conversion. H uses t=p; D's H uses p+pi/2. These schedules depend explicitly on pass, without reading saved history.

**1. Incoming graph and simultaneous local motion (98–112, 167–171).** Let d_ij=||X_j−X_i||. Each row takes `argsort(d_i)[1:6]`; A_ij=1 for those five selections. The graph is directed. Skipping the first sorted index assumes it is self; exact coincident points could violate that assumption. The selected replay has no self selections or fifth/sixth cutoff ties. A no-neighbor row has zero Laplacian. For a nonempty row,

\[
\Delta_i=\frac1{|N_i|}\sum_{j\in N_i}(X_j-X_i),\qquad
Y_i=X_i+.05\Delta_i+.15\tanh\Delta_i.
\]

Tanh acts componentwise. All local increments use the same incoming X. This differs from the ordered in-place body updates in Volume I. Componentwise tanh is also not generally rotation-equivariant; the later rotation-invariant shape measurements do not make the dynamics rotation-invariant.

**2. Two-field local and cross exchange (114–137, 173–174).** The distances and both amplitude arrays are still incoming values, although X has already been moved. Define normalized weights

\[
w_{ij}=\frac{(d_{ij}+10^{-8})^{-1}}{\sum_{k\in N_i}(d_{ik}+10^{-8})^{-1}},\qquad
c_p=.08699\sin(.244p+\pi/2).
\]

For each nonempty neighbor row,

\[
Q_i=R_i+.15\left(\sum_jw_{ij}R_j-R_i\right)+.01c_pD_i,
\quad
E_i=D_i+.075\left(\sum_jw_{ij}D_j-D_i\right)+.01c_pR_i.
\]

Both are copies updated from the old arrays. No earlier loop row feeds another row. If the row has no neighbors, the early `continue` skips its cross term as well: Q_i=R_i and E_i=D_i. The literal gamma is an imposed coefficient, not an inferred coupling. Cross terms use .244 **radians/pass**; the later sine uses .244 **cycles/pass** through multiplication by 2pi. These two periods must not be equated.

**3. Separate H factors (176–183).**

\[
U_i=Q_i[1+.05H(p)/M],\qquad Z_i=E_i[1+.05H(p+\pi/2)/M].
\]

Shifting a damped sum also shifts its exponential envelopes. Two real amplitude arrays with these schedules are not thereby orthogonal phases or a complex oscillator.

**4. Global fusion (185–190).**

\[
C=\frac{\sum_i(|U_i|+10^{-8})Y_i}{\sum_i(|U_i|+10^{-8})},\qquad
F_i=.03U_i(C-Y_i),\qquad T_i=Y_i+F_i.
\]

One center reads all points at the post-local, post-H stage, before sine and RPCO. Locally disconnected graph components still participate in this center. Positive U pulls toward C; negative U reverses the increment, and sufficiently large positive U could overshoot. Neither sign nor a convex-combination bound is enforced by the source. D affects same-pass positions through its cross contribution to Q, then U, then both center weights and the point's fusion strength. There is no separate D-position force. Stored endpoint weighted centers would not reproduce this intermediate C; the exact recomputed centers are in the intermediate archive.

**5. R-only sine (192–193).** Set P_i=U_i[1−.001 sin(2pi·.244p)]. D has no analogous multiplier; its pre-RPCO input remains Z_i.

**6. Signed RPCO (49–53, 195–197).**

\[
\mathcal C(x)=\operatorname{sgn}(x)\exp\{\operatorname{clip}[\log(|x|+10^{-9}),-9,9]\},\qquad
R'_i=\mathcal C(P_i),\quad D'_i=\mathcal C(Z_i).
\]

Zero maps to zero. Nonzero outputs have magnitudes between exp(−9) and exp(9); the lower boundary can amplify a small magnitude. On an unclipped input the exact-real formula reduces to x+1e−9 sgn(x), rather than general logarithmic damping. The two channels have identical independent bounds, with no winner-selection normalization. Sign is preserved through the compressor, though exchange can change it.

**7. Noise, displacement, observations (199–205).**

\[
\sigma_p=.01/(1+.01p),\qquad X'_i=T_i+\eta_i,
\quad\eta_i\sim\mathrm{Normal}(0,\sigma_p^2I_3),\qquad V'_i=X'_i-X_i.
\]

Exactly one `(50,3)` NumPy normal draw is requested per selected pass. V is a displacement over one native pass, not an integrated momentum. R/D exchange and positions feed later graph calculations. Observations and the retained history do not feed movement.

## All 21 CSV columns and their timing

Lines 139–160 and 207–268 define the observations. Write s_i=||V'_i||, g_i=1/(1+s_i), r_max=max|R'|, r_mean=mean|R'|, r_std=population std of signed R'. Let b=argmax|R'| (first index on a tie).

| Output | Exact operational definition |
|---|---|
| pass | Updated integer p |
| R_max, R_mean, R_std | r_max, r_mean, r_std respectively |
| dark_energy, matter_energy | sum(D'²), sum(R'²); sums of squared real amplitudes |
| dark_matter_ratio | sum(D'²)/(sum(R'²)+1e−12) |
| Rg | sqrt(mean ||X'−mean(X')||²), arithmetic centroid |
| coherence | 1−r_std/(r_mean+1e−8) if r_mean>1e−12; otherwise 0 |
| n_echo_corridors | Number of unordered i<j with [1−|R'_i−R'_j|/(r_max+1e−8)] exp(−d_ij/3)>.85; **incoming d** |
| n_infinity_seeds | Count where |R'_i|/(r_max+1e−10)>.66 and curvature_i>.012 |
| top_seed_id, top_seed_R | b and signed R'_b |
| top_seed_grf, mean_grf | g_b and mean(g_i); not 1/(1+mean(s_i)) |
| top_seed_curvature, mean_curvature | Curvature at b and arithmetic average over i |
| H_value | H(p) |
| top_seed_x, top_seed_y, top_seed_z | Coordinates of X'_b |

Curvature is the population standard deviation of angles in radians between every unordered pair of neighbor vectors X'_j−X'_i. The denominator is `||v1||*||v2||+1e−10`, the cosine is clipped to [−1,1], and rows with fewer than two neighbors return zero. It uses **new X with old A**. Its `dists` argument is unused. The code computes standard deviation despite a comment mentioning variance. This is an angle-spread diagnostic, not a recovered metric-curvature tensor.

The selected driver (282–349) calculates final-ten coefficient-of-variation summaries and a final-twenty top-ID set, prints threshold-based interpretations, and exports the 200 metric rows. “Energy,” “curvature,” “seed,” “echo,” “fusion” and “tunneling” are source names; no action principle, physical potential, mass shell, gravitational law or phase dynamics is supplied here.

## Conditional mathematics, without replacing the update

Let W be the incoming row-stochastic weight matrix and g=.01c_p. For nonempty rows the pre-H fields are `(I+.15(W−I))R+gD` and `(I+.075(W−I))D+gR`. When both channels are positive and unclipped, their next values have those respective H factors, the R-only sine factor, and the positive RPCO epsilon offset. When c_p<0 the joint block operator contains negative cross entries. SIM04's single-channel convex-range argument therefore cannot automatically be promoted to this two-field evolution.

For positive U, fusion alone obeys `mean(F)=.03·1e−8(mean(Y)−C)` by substituting the weighted-center definition. This is a small but nonzero centroid shift, not a physical conservation law. Directed local motion and noise remain separate. The changing squared-amplitude totals likewise are diagnostics: local mixing is not generally doubly stochastic, and cross terms, schedules and clipping alter them. [The ordered squared-amplitude budget](analysis/squared_amplitude_stages.csv) records each actual stage without a causal ablation.

The once-sampled H normalization and exponentially decaying H share the setting of [the retained R3 mathematical review](context/accepted_math/R3_MATHEMATICAL_REVIEW.md). Its finite positive H-product result does not prove an Infinity fixed point: cross-coupling, sine, offsets, fusion and noise remain, and the coupled state keeps changing. No prior theorem or accepted checker was rerun.
