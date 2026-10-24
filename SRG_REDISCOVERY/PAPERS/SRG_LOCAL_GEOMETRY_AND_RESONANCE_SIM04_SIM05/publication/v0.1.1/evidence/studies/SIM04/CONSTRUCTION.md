# SIM04 — construction and mathematical transcription

Status: IN REVIEW, 23 October 2026. This is a reading of all **755 source lines**, not an execution of the original program. Source references `S:Lx–Ly` mean the unchanged [srg_seed_explorer.py](originals/srg_seed_explorer.py); the line-numbered reading copy is [here](analysis/srg_seed_explorer_numbered.txt). SHA-256: `0c8ec661624bd100212b29d75dd184cacf2adbf5d173584e3817460d9fd6ea10`.

## 1. What exists and what is retained

`GlyphField` represents N labeled points in real three-dimensional coordinate space, each with a real resonance scalar. There are no faces, solids, physical containers, masses, assigned physical units, phases or separate trajectory agents in this class. Its source calls the spatial operation a “TGMO analog”; this does not make it a toroidal boundary rule.

| State or configuration | Initialization / role | Source |
| --- | --- | --- |
| `positions`, X ∈ R^(N×3) | Uniform coordinates in `spatial_range`; drives distances and movement | S:L60–65 |
| `resonance`, R ∈ R^N | Uniform in `R_init_range`; drives local exchange and fusion | S:L60–66 |
| `velocities`, V ∈ R^(N×3) | Initially zero; later X_new minus last stored X. Observed, never read by the movement equation | S:L67,174–176 |
| `pass_count`, p | Initially zero; incremented before every update; enters two prescribed schedules | S:L69,139–142 |
| `history` | Copies of X, R, V and p, including pass 0; previous X supplies only V, while full history supplies export | S:L68,82–89,174–178,276–293 |
| Random state | NumPy's process-global RNG, optionally reset by the constructor; X then R draws, then position noise each pass. Not owned by each field or stored in history/CSV | S:L61–66,171–172 |
| N and parameters | Fixed by the deep driver / constructor; other experiment drivers can change them | S:L64,71–80,605 |

The selected deep driver is `GlyphField(50, R_init_range=(0,0.1), spatial_range=(-5,5), seed=2038)` at S:L605, followed by 20 calls at S:L610–611. The CSV initial state lies within those ranges and has V=0. We did not regenerate its initializer. A literal seed identifies the driver's intention, not a verified software environment or saved RNG checkpoint.

## 2. Exact pass, in execution order

Use incoming saved state X,R at pass p−1. Define p as the newly incremented integer, not elapsed seconds. The following equations are a **DERIVED transcription** of the source.

**E1 — incoming geometry and directed neighbors** (S:L91–98,144–145):

\[
d_{ij}=\|X_j-X_i\|_2,\qquad
\mathcal N_i=\operatorname{argsort}(d_{i,:})[1:k+1],\quad k=5.
\]

Set A_ij=1 for those selected indices, zero elsewhere. There is no reciprocity requirement: j in N_i does not imply i in N_j. Both A and d are rebuilt on incoming positions every pass. In the distinct-point record the skipped first index is the zero-distance self and every row has five neighbors. The code literally skips the first sorted entry; it does **not** explicitly remove index i. Coincident points create zero-distance ties, so self can remain selected while a different tied index is skipped. No stable tie policy is specified. The inspected record has no coincident pair or cutoff tie; this edge case was established by source reading, not a new test trajectory.

**E2 — synchronous local position change** (S:L100–109,147–149):

\[
\Delta_i=\frac1{|\mathcal N_i|}\sum_{j\in\mathcal N_i}(X_j-X_i),\qquad
D_i=\alpha\Delta_i+\beta\tanh(\Delta_i),\qquad Y_i=X_i+D_i,
\]

with α=.05, β=.15 and componentwise tanh. If the neighbor set is empty, Δ_i=0. The entire `lap` array is computed before `positions += ...`; the Python loop does not introduce partially updated coordinates. This is a normalized neighbor-average difference, not an unnormalized graph Laplacian. The tanh term saturates componentwise, while the αΔ term is unbounded as a function of Δ. It does not normalize a force direction or damp a carried velocity.

**E3 — synchronous, distance-weighted resonance exchange** (S:L111–124,151–152):

\[
w_{ij}=\frac{(d_{ij}+10^{-8})^{-1}}
 {\sum_{\ell\in\mathcal N_i}(d_{i\ell}+10^{-8})^{-1}},\qquad
Q_i=R_i+\beta\left(\sum_{j\in\mathcal N_i}w_{ij}R_j-R_i\right).
\]

An empty-neighbor row keeps R_i. Although E3 is called after the position array has become Y, it reads the retained **incoming** d,A and **incoming** resonance. It does not read Y. It creates a separate `R_new` array and reads old R for every row. The 10⁻⁸ denominator offset keeps inverse distances finite at coincidence. For a nonempty row, Q_i=.85R_i+.15 weighted-neighbor-mean; this is a convex average at the default β. Directed row-normalized averaging does not generally preserve the unweighted sum of R.

**E4 — prescribed pass response** (S:L32–47,154–158):

\[
H(t)=2e^{-0.5t}\cos t+e^{-0.3t}\sin t+1.5e^{-0.7t}+e^{-0.4t},
\]
\[
M_p=\max_{t\in\operatorname{linspace}(0,10p,20000)}|H(t)|+10^{-12},
\quad m_p=1+0.05\,H(p)/M_p,\quad U_i=m_pQ_i.
\]

`compute_Hmax(t * 0.05 * 200)` recomputes a sampled normalization on every pass. The numbers .05 and 200 define the sampling endpoint; they do not make the actual pass clock dt=.05 or advance it to 10p. H is evaluated at t=p. The code reads no history to produce H or M_p. All 20 evaluated normalization values are 4.500000000001, with the sampled maximum at t=0; this is a finite sampling result, not a proof of a continuous supremum for all future horizons. At pass 1 m_p≈1.02993328; at pass 4 it is ≈0.99875828. The schedule can increase or reduce resonance. It is not an inferred memory feedback law.

**E5 — one global weighted center and synchronous fusion** (S:L160–163):

\[
c=\frac{\sum_i(|U_i|+10^{-8})Y_i}{\sum_i(|U_i|+10^{-8})},\qquad
F_i=0.03U_i(c-Y_i),\qquad Z_i=Y_i+F_i.
\]

The center uses post-diffusion Y and post-memory U, before sinusoidal modulation and RPCO. Despite the comment “cluster centers,” there is exactly **one** weighted average over all N points, with no cluster detection. The vectorized addition uses this single center for every row. Positive U gives an inward contribution, negative U reverses its direction, zero U gives no fusion displacement. `abs(U)+1e-8` weights the center but the signed U scales each point's displacement. Even when the local graph is disconnected, this global term still depends on all points. No points are merged or removed.

**E6 — sinusoidal resonance factor** (S:L165–166):

\[
s_p=1-0.001\sin(2\pi\,0.244p),\qquad B_i=s_pU_i.
\]

This factor is always between .999 and 1.001. It acts on resonance only, after the fusion displacement. `theta_lock=.244` enters with 2π, i.e. as a prescribed cycles-per-pass parameter. It is not a measured locking frequency. The separately stored `lambda_vp=.618` does not enter this expression.

**E7 — exact signed logarithm / clipping / exponential** (S:L38–43,168–169):

\[
R_i^+=\operatorname{sgn}(B_i)
\exp\left[\operatorname{clip}\big(\log(|B_i|+10^{-9}),-9,9\big)\right].
\]

For nonzero B, this bounds the output magnitude between e⁻⁹ and e⁹; zero maps to zero because `sign(0)=0`. Away from clipping it equals sign(B)(|B|+10⁻⁹), up to floating-point evaluation. It is not exactly identity, and a negative input stays negative. It does not map −a to +1/a. The `mode="signed"` argument is declared but never read; there is no second mode in this implementation. No clipping is active in the 1,000 recorded transition evaluations, but the +10⁻⁹ operation remains.

**E8 — additive position noise, observed velocity, then history** (S:L171–178):

\[
X_i^+=Z_i+\eta_i,\qquad
\eta_{ia}\mathrel{\sim}_{\text{source}}\mathcal N(0,0.01^2),\qquad
V_i^+=X_i^+-X_i^{\text{last history}}.
\]

The distribution notation describes the call in the source; it is not a recovered random draw sequence. In the selected fresh-field driver, last history is precisely pass p−1. Then `_record_state` appends copies of the post-noise X, post-RPCO R, diagnostic V and p. There is no spatial modulo, clamp or box boundary. The initialization range [-5,5] is a sampling range only. Noise in X influences later resonance indirectly because later neighbor distances are rebuilt; there is no direct resonance-noise draw. E8's computed V never enters E1–E7.

## 3. Active parameters, numerical offsets and unused names

| Name / value | Actual use |
| --- | --- |
| α=.05 | E2 linear position diffusion |
| β=.15 | Both E2 tanh displacement and E3 resonance exchange |
| `lam_H`=.05 | E4 multiplier |
| `k_neighbors`=5 | E1 selection; each row can select fewer for small N |
| `theta_lock`=.244 | E6 prescribed sine |
| `rpco_L`=9 | E7 log magnitude clip |
| `lambda_vp`=.618; `gamma_srg`=.0870 | Stored at S:L74–75, unused by the evolution; the former is varied by another driver without entering the recurrence |
| `echo_threshold`=.85 | Observer only, S:L80,135 |
| Fusion .03; sine amplitude .001; noise σ=.01 | Hard-coded at S:L162,166,172 |
| 10⁻⁸ | Inverse-distance exchange regularizer; center weight offset; echo normalization; coherence normalization; radial-spread observer denominator |
| 10⁻⁹ | RPCO magnitude offset |
| 10⁻¹² | Added to sampled H maximum; separate near-zero std criterion in coherence |
| 10⁻¹⁰ | Angle denominator offset |
| Echo spatial scale 3; top-quartile percentile 75 | Observer settings, not movement coefficients |

`ConvexHull`, `Delaunay`, `defaultdict` and `json` are imported but unused. In particular there is no hull or triangulation calculation behind the geometry labels. `oct_angles=[90,180]` is assigned but the next expression repeats its literals. These names do not add operative mechanisms.

## 4. What the observers calculate

**Ranked seeds** (S:L185–204): sort by descending |R|, retain up to five indices, then return rank, ID, position, signed resonance and norm of diagnostic V. No state is changed. A “top seed” in the deep driver is simply `argmax(abs(R))`, not an object that steers the others. Other drivers apply different extra emergence thresholds; `find_proto_seeds` itself has none.

**Coherence** (S:L268–274): population std σ_R, with value 1 if σ_R<10⁻¹²; otherwise

\[
C=1-\frac{\sigma_R}{\operatorname{mean}|R|+10^{-8}}.
\]

Despite the comment “normalized variance,” this uses **standard deviation**. It has no phase variables and is not a correlation or synchronization measurement; it can be negative on other inputs. It does not enter the dynamics.

**Echo corridors** (S:L126–137): inspect every unordered pair i<j, not merely graph edges. With supplied distances d,

\[
E_{ij}=\left(1-\frac{|R_i-R_j|}{\max_k R_k+10^{-8}}\right)e^{-d_{ij}/3};
\quad\text{report pair if }E_{ij}>.85.
\]

The denominator uses max(R), not max(|R|). Scores are not explicitly clipped; sign and near-zero issues outside the positive saved run should not be hidden by a similarity label. The deep driver rebuilds distances on the **post-update** X at S:L618–620, so its reported corridors use post-noise geometry and post-RPCO R. They are never read by `evolve_pass`.

**Geometry classifier** (S:L206–266): retain all |R_i| at least the 75th percentile. With m selected points, center them on their arithmetic mean and compute pair angles

\[
\theta_{ij}=\arccos\operatorname{clip}\left(
\frac{(X_i-\bar X)\cdot(X_j-\bar X)}{\|X_i-\bar X\|\|X_j-\bar X\|+10^{-10}},-1,1\right)
\frac{180}{\pi}.
\]

For m<4 return `sub-critical`. For 4≤m≤5 return `tetrahedral` if mean|θ−109.47°|<30°, else `amorphous`. For 6≤m≤7 return `octahedral` if min(mean(min(|θ−90°|,|θ−180°|)),90)<25°, else `transitional`. For m>7 return **`higher_polyhedra` unconditionally**, along with angle/radius summaries. It checks no face structure, equal edge lengths or polyhedral fit. The selected N=50 record has m=13 at every pass, so its label cannot discriminate initial scatter from later clustering. The deep driver calls this classifier only at the endpoint; our all-pass evaluation is explicitly new observation.

**Deep-driver metrics** (S:L613–650): mean|R|, max|R|, std(R), arithmetic-centroid radius

\[
R_g=\sqrt{N^{-1}\sum_i\|X_i-\bar X\|^2},\qquad
K_{\text{source}}=N^{-1}\sum_i\|V_i\|^2.
\]

`kinetic_energy` has no mass, factor 1/2 or elapsed-time conversion. Here it is mean squared displacement per pass. No potential, action, energy balance, conservation law or energy feedback is implemented. The metrics also include corridor count, coherence and the top-ranked ID, signed R and three coordinates. They are measured after each pass, after noise and history recording. The separately computed `dists` at S:L618 is unused because the next line recomputes distances.

## 5. Complete driver and output coverage

| Source section | What it would execute / export; read but not run |
| --- | --- |
| S:L1–29 | Header dated 2026-03-14; imports; suppress warnings globally; create an absolute `/sessions/.../Claude_SRG_Analysis` directory at import time. This is why even import was excluded. |
| S:L32–293 | Helpers, state evolution and observers described above |
| S:L300–372 | Ten seed-family configurations × three trials, using `trial*1000 + hash(label)%1000`; hash-dependent seed, not portable without realized seed / process hash information. Export `seed_family_classification.csv`; count only ranked top-five signed R>.1. |
| S:L379–454 | N=3..50 sweep × five trials, then R_max `arange(.01,1.01,.02)` at N=20 × five trials. The comment says “binary search,” but the actual loop is a sweep. Emergence is the chosen rule C>.5 and top signed R>.15. Exports `minimal_seed_conditions.csv` and `R_init_phase_sweep.csv`. |
| S:L461–592 | Two separated clusters, rings, and competing preheated glyphs; exports `multi_seed_interactions.csv`. “Independent/merged” uses distance between top two ranked glyphs versus separation/3, not connectivity of all points. Other labels are scenario names or which ID wins the resonance ranking. |
| S:L599–675 | Selected 50-point / seed-2038 / 20-pass driver. Exports all history to `deep_trajectory.csv`, then 20 metric dictionaries to `pass_metrics.csv`; prints final top three and geometry. |
| S:L682–726 | Sweeps α, β, unused `lambda_vp`, L and k on 30-point fields for 12 passes; exports `parameter_sensitivity.csv`. No results from these runs were newly verified here. |
| S:L733–755 | `__main__` launches all five experiment families in that order. It is not a safe single-run entry point for this assignment. |

The multi-cluster drivers overwrite initialization and append another pass-0 history at S:L479–482 and L531–534. The competing scenario overwrites fields without rerecording them (S:L562–570), which would affect its first diagnostic V. These are source-level distinctions in other drivers, not defects to impose on the selected deep record. Deep exploration constructs a fresh field once, uses no manual overwrites, and has exactly one initial history block. Although earlier main-driver experiments would consume random numbers, its constructor explicitly resets the global RNG to 2038.

Trajectory export at S:L276–293 iterates history order, then IDs 0..N−1, producing `Pass,Glyph_ID,X,Y,Z,Resonance,VX,VY,VZ`. `index=False` suppresses a dataframe index column. The aggregate labels `p+1` at S:L638 align with actual pass_count only for this fresh 20-iteration driver. There is no animation callback or rendering timer, no plotting import/call, no movie export, and no plot whose look can be inferred from the source. The console narratives are reports of observer outputs, not additional state transitions.

## 6. Short comparison with accepted Volume I

This comparison follows the independent SIM04 recovery. The unchanged accepted [mechanism map](context/VOLUME_I_CROSS_STUDY_MECHANISM_MAP.md) supplies earlier source locations; study order does not assert lineage.

| Aspect | Volume I | Selected March program |
| --- | --- | --- |
| Retention | All three programs carry velocity into the next drive/damping step | X and R drive the next pass; V records the last displacement |
| Interaction | Three-point pairwise directions; later eight-point arithmetic centroid with speed response | Directed five-neighbor position/resonance exchanges plus one global resonance-weighted center |
| Order | Per-body in-place updates, old suffix / updated prefix | Entire stage synchronous; distinct stages deliberately read different snapshots |
| H clock | Step×.05 or callback frame×.1; multiplies velocity drive | Same H formula, integer pass; sampled normalization; multiplies R |
| Randomness | Initial draws; third program adds gated binary flips | Initial draws and additive positional Gaussian draw each pass |
| Bounds | Wrapped direction and coordinates | No spatial wrap/clamp; signed resonance magnitude clip only |
| RPCO name | Componentwise candidate velocity divided by 1+log(1+|v|) | Sign-preserving exponential of clipped log(|R|+ε); different mathematics |
| Recorded “energy” | Third program: .5Σ||v||² | Mean ||X_p−X_(p−1)||², no physical calibration |

These are implementation differences. They do not by themselves prove a hierarchy of physical models, a shared attractor, or a master-equation mechanism.
