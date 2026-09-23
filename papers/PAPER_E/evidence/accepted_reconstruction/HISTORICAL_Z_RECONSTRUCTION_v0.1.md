# Historical Z manifold and six-gap reconstruction v0.1

**Codex source reconstruction and bounded verification — 23 September 2026.** Author/design testimony: Hilmir Frímann Halldórsson, supplied work order. Scientific lead named in that order: GPT. This is a new Codex analysis, not a new GPT or Claude acceptance and not a publication paper.

**Disposition.** The scalar third harmonic, direct vector construction, alternate displays and spike diagnostic are recovered. A third harmonic has three maxima and three minima under the stated frozen-input assumptions. Its direct macro embedding places those extrema in three vertical pairs, with a nontrivial upper/lower visiting order. The actual default 12-clock samples do **not** hit those extrema. No historical map from these mathematical coordinates to six physical/reference-scaffold gap locations was found in the bounded source closure. The six-gap identification remains open; no coordinates have been invented.

A significant provenance recovery is numerical: the two preserved spike CSV packages reproduce exactly in Z coordinates and the complete saved velocity sequence, including nonfinite positions, when the inspected staged source is run with **`lambda_phase=0`**. Their summaries omit that parameter. The current default `0.001` gives different results. This recovers effective settings consistent with the saved data, not an original execution environment or an identified original source commit.

## Evidence, execution and reading convention

The operative request is the supplied [work order](<C:/Users/Notandi/.codex/attachments/b5afed30-cd45-433a-9827-b8dc0a06b689/Pasted text.txt>). Present author recollection is evidence of intended design, not a mathematical theorem. Source statements below are distinguished from **derivations in this report**, **new numerical checks**, and **interpretations**. “Z energy” remains historical terminology.

Primary source root is [kernel_TO](C:/TORMENT/TRIOCTAGON_new/kernel_TO), here abbreviated **K**. **H** denotes the preserved [committed-core snapshot](C:/TORMENT/TRIOCTAGON_new/reconstruction/recursive_state_archaeology/codex_verification_I/source_snapshots/model_core.py). The existing [source-to-model report](C:/TORMENT/TRIOCTAGON_new/reconstruction/KERNEL_SOURCE_TO_MODEL.md), especially §§3, 5, 7 and 16, is earlier evidence; it has not been replaced or edited. The accepted scaffold definition is [Paper D v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md), §§5–7 and 15–20. Paper B's accepted channel-area interpretation is used within its existing scope.

Source anchors:

| Source | Functions / lines inspected for this reconstruction |
|---|---|
| [K/model_core.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/model_core.py:35) | Parameters and state; `phase_lock_step` 133; `advance_phi` 164; `update_z` 169; `step` 246; `run` 268 |
| [K/geometry_3d.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_3d.py:4) | Cylinder 4; torus 25; direct stored-vector extraction 60 |
| [K/geometry_embeddings.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_embeddings.py:6) | `TorusConfig` 6; alternate cylinder 12; alternate torus 19 |
| [K/definitions.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/definitions.py:22) | J 22/30; chirality sign/commit 50–96; direction metric 117; stabilization 181; full metric 263; entropy variant 340 |
| [K/z_spike_diagnostic.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/z_spike_diagnostic.py:29) | Run 29; fallback 64; picker 72; export/window/plot 94; CLI 245 |
| [K/toy_3d_triocta.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_3d_triocta.py:80) | Metric 80; J→RSB 102; run 138; channel torus 283; clock helper 327; display 377; scaling 649; selector 685; callbacks 826/848 |
| [K/analysis_tools.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_tools.py:93) | Exact title `Z_vec trajectory`; direct/component plots; separate torus and dual-tetra views |
| [K/toy_ui.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_ui.py:298) | Full metric and components; direct Z selector 376–414, with fallback |
| [K/chirality_lab.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/chirality_lab.py:187) | Z→J fits; finite-difference curvature/torsion 288; sign-branch fits 515; direct plot 868 |
| [K/diagnose_bottom_lid.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/diagnose_bottom_lid.py:63) | Alignment histories and finite-value summaries; no literal bottom-lid geometry |
| [K/side_zchiral_probe.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/side_zchiral_probe.py:33) | Phase-only comparison and polyline turning proxy |
| [K/dual_tetra_mapper.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/dual_tetra_mapper.py:23), [CP windows](C:/TORMENT/TRIOCTAGON_new/kernel_TO/cp_windows.py:37) | Intensity-basis display and sector masks, not a Z-to-gap map |
| [K/run_triocta_structural_3body_probe.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_triocta_structural_3body_probe.py:43), [helpers](C:/TORMENT/TRIOCTAGON_new/kernel_TO/triocta_probe_utils.py:47) | Z-turn event consumer, planar tail directions and six-ray diagnostic |

Imports used during execution were inspected first. The harness imports the preserved core and safe dependencies through a synthetic package name; it does not execute their UI or CLI launch paths. It extracts the unchanged AST function bodies of `run_triocta_once`, `pick_spikes`, and `embed_on_torus`. This handles the old mixture of flat and relative imports without editing a preserved source. No original application is claimed to have launched unchanged. Latent foreclosure is off; no RSB simulation, external-body simulation, corpus scan or parameter sweep is launched. Figure/cache/output writes stay in the new verification directory.

The [verification script](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/verify_historical_z.py), [machine-readable results](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/verification_results.json) and [execution output](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/verification_execution.txt) are **new Codex re-execution evidence**, not original captured-run files. The results contain source SHA-256 identities and actual runtime versions. The preserved CSVs, original images and old summaries remain in their original folders.

## 1. Exact Z definitions and consumers

Use channel indices 1,2,3 and write Ω=x+iy, κ=‖Ω‖, ρ=κ/(1+κ), q=`phi_index`, N=`d24_steps`, θ=2πq/N. For finite Ω the staged core defines

\[
z=\lambda_{vp}\rho\cos(3(\theta-\theta_{lock}))e^{-\gamma t},\qquad
M=Z_{macro}=z(\cos\theta,\sin\theta,1),
\]
\[
C=Z_{chiral}=(\Im(\bar\Omega_2\Omega_3),\Im(\bar\Omega_3\Omega_1),\Im(\bar\Omega_1\Omega_2)),\qquad
T=Z_{total}=Z_{vec}=\alpha M+\beta C.
\]

Defaults are N=12, clock increment 1, λ_vp=0.618, γ=0.577, θ_lock=0.244 radians, α=1, β=0.5. These are source-selected toy constants, not established physical constants or calibrated measurements. In particular 0.618 is the literal stored decimal, not an exact golden-ratio expression.

| Object | Inputs and exact role | Units assigned; downstream use; historical qualification |
|---|---|---|
| `z` | κ,q,t and three Z constants; state-stored scalar readout, recomputed after Ω | Mathematical scalar, no physical calibration. Feeds identity sign classification and plots/CSV; no return into subsequent Ω in this core. H instead uses the EMA formula below. |
| `Z_macro` | z and clock angle; state-stored readout M | Three plotting coordinates with no recovered ambient-frame map. Feeds blend, alignment and diagnostics. Carries the staged envelope through z. |
| `Z_chiral` | Quadratic relative-phase/area triple C=x×y | Channel-indexed transported-area triple. No imposed decay envelope; need not decay. Feeds blend, diagnostic fits and displays. It can decay, persist or vary on particular Ω trajectories. |
| `Z_total` / `Z_vec` | αM+βC, with legacy alias recorded identically | Direct plotted three-vector and downstream diagnostic input. It is not C alone and is not independently evolved. Used by the optional option-volume probe and external event detector. Neither consumer feeds the inspected Ω recurrence. |
| `J_eff` | `Im(Ω1 conj(Ω2) Ω3)` | Cubic mathematical observable, distinct from C. Canonical `compute_jeff_series` prefers an existing nonempty J history, otherwise computes from Ω. It colors plots, supports chirality diagnostics, enters the viewer's separate RSB parameter handoff, and feeds H's memory. No energy units are assigned. |
| Full `v_rec` | Successive T/M/C, Ω, q and optionally κ; §5 formula | Weighted diagnostic per stored transition. No division by dt or physical space/time calibration. Thresholds/windows/plots only in the spike tool. |
| Other `v_rec` names | Direction angle or absolute spectral-entropy difference | Different diagnostics; do not substitute them for the full metric. Their names alone do not define a common observable. |

The Ω recurrence, before phase synchronization, is

\[
V=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+\delta+g_{coupling}L_3\Omega,
\quad L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
\]

Then phases are changed simultaneously by λ_phase Σ_j sin(3(φ_j−φ_k)), preserving |V_k|; optional complex noise follows. **dt does not multiply this recurrence.** Z constants, α, β and q are absent from the next Ω update. The master step advances Ω, then q, then t by dt, then Z, then cycle/identity labels. `run` records the **pre-step** state: the initial stored Z fields are zero even when Ω is nonzero. Thus the plotted first segment includes an initialization convention; it is not evidence of physical emission from the origin. The final stepped state is not included in that history.

The three alignment histories are unit(T)·unit(M), unit(C)·unit(M), and unit(T)·unit(C). `_unit` returns zero when the norm is below 10^-12, so a stored zero dot in that case means no resolved direction, not geometric orthogonality. Outside that guard these are cosine diagnostics. `dot_vec_macro−dot_vec_chiral` is a diagnostic preference score, not an energy partition. The unused `_mirror_z` helper does not establish a top/bottom placement law.

The viewer's J-to-RSB handoff uses Q=clip(mean|J|/max|J|,0,1), with a denominator fallback, and the sign of its tail mean. It sets α_RSB=0.6(0.3+0.7Q), μ_RSB=0.6+0.2 sign, γ_RSB=0.2(0.5+0.5Q) for a **separate subsequent** RSB run. The optional option-volume diagnostic perturbs cloned Ω, steps clones and tests ‖ΔT‖/ε_norm against a corridor threshold; the retained model state is not modified by those clones. The external three-body probe uses Z turning to trigger velocity reorientation, but supplies its tail directions from q. These are real downstream uses; “readout” here does not mean that every later consumer is only a plot.

**H variant.** In the committed-core snapshot, `update_z` uses

\[
J=\Im(\Omega_1\bar\Omega_2\Omega_3),\quad
m_{new}=0.99m+0.01\frac{J}{1+|J|},\quad
z=\lambda_{vp}\rho\cos(3(\theta-\theta_{lock}))+m_{new}.
\]

The same M,C,T definitions follow. γ is not used in this formula. With |m_initial|≤1 and finite J, memory stays within [-1,1]; no exponential envelope is imposed. The harness checks this variant on identical Ω histories. It is not silently substituted for the staged core.

## 2. Third-harmonic six-extrema theorem

**Derivation, with its necessary hypotheses.** Freeze κ,t and parameters, and let θ vary continuously over a full turn. Put A=λ_vp ρ exp(−γt). If A>0, differentiating f(θ)=A cos(3(θ−θ_lock)) gives

\[
f'=-3A\sin(3(\theta-\theta_{lock})),\qquad
f''=-9A\cos(3(\theta-\theta_{lock})).
\]

There are exactly three maxima at θ_lock+2πj/3 and three minima at θ_lock+(2j+1)π/3, j=0,1,2 modulo 2π. Values are +A,−A alternately, at spacings π/3. A<0 swaps the maximum/minimum labels. A=0 is constant and has no six isolated extrema. A change of θ_lock translates the angular pattern. The positive finite exponential factor changes magnitude, not extrema of this **frozen angular function**.

This is not a theorem that evolving time-series maxima remain at those angles: κ and t change between recorded samples. Even a chosen continuous interpolation with changing envelope would require differentiating that envelope too. No such interpolation law is being added to the discrete model.

For N=12,

\[
z_q/A=\cos(\pi q/2-3\theta_{lock})
=(c,s,-c,-s,c,s,-c,-s,c,s,-c,-s),
\quad c=\cos(3\theta_{lock}),\ s=\sin(3\theta_{lock}).
\]

The clock samples the continuous extrema exactly **iff θ_lock is an integer multiple of π/6**, modulo equivalent periods. Then six sectors reach extrema and the other six are zeros. At the default 0.244 radians, c≈0.74384 and s≈0.66836 (exact floating values in results); the sequence is `++--` repeated three times. No sample reaches ±1 in units of A. Near 15° both adjacent positive samples are similar, as are the negative samples; exactly at θ_lock=π/12 they form equal-height two-sector plateaus. It would be wrong to label all twelve sector samples six exactly attained extrema.

In H, freezing the current Ω and incoming memory adds a θ-independent offset m_new. Angular extrema keep their positions, but their values are m_new±λ_vpρ. One set is above zero and the other below only if |m_new|<|λ_vpρ|. A sufficiently large memory offset removes top/bottom sign alternation entirely. Along an actual run Ω and memory evolve, so neither equal extrema nor fixed vertical pairs is guaranteed.

![Frozen harmonic and direct macro extrema; labels 0–5 follow increasing clock angle. No scaffold coordinates appear.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/01_harmonic_and_macro.png)

The theorem supports mathematical compatibility with “three upper plus three lower,” but is not a registration theorem.

## 3. Direct Z_vec geometry and the zig-zag

`history_Zvec_to_xyz` simply returns the three columns of the selected stored vector. It does not construct a torus, use κ as a radial coordinate, attach a face or compute a gap location. Only the default total key falls back to the legacy alias in this geometry helper.

**Macro geometry, derived here.** Because M=z(cosθ,sinθ,1),

\[
M_1^2+M_2^2=M_3^2,\qquad \|M\|=\sqrt2|z|.
\]

M lies on a double cone in these mathematical plotting coordinates. Negative z reverses both horizontal components: its displayed azimuth is θ+π, not θ. For frozen A and the pure third harmonic,

\[
M(\theta+\pi)=(M_1(\theta),M_2(\theta),-M_3(\theta)).
\]

Consequently the six continuous signed extrema project onto **three** horizontal directions θ_lock+2πj/3. Define U_j=A(cos(θ_lock+2πj/3),sin(θ_lock+2πj/3),1) and L_j with the same first two coordinates and last coordinate −A. In increasing clock angle the sequence is

\[
\boxed{U_0\to L_2\to U_1\to L_0\to U_2\to L_1\to U_0.}
\]

This is an exact nontrivial upper/lower order for the **frozen extrema**, not recovered gap coordinates. The source does not interpolate its clock through those extrema. At generic default 12-sector sampling the macro instead has twelve signed directions: six above and six below, paired horizontally between q and q+6 when A is frozen. Its six horizontal azimuths are 0°,30°,120°,150°,240°,270° for the default sign pattern. Actual radius/amplitude changes spoil equal point-pair heights but leave each sector's direction fixed while its scalar sign persists.

Another useful exact identity for frozen A is

\[
M_1={A\over2}[\cos(4\theta-3\theta_{lock})+\cos(2\theta-3\theta_{lock})],\quad
M_2={A\over2}[\sin(4\theta-3\theta_{lock})-\sin(2\theta-3\theta_{lock})].
\]

Thus a multi-arm projection already exists in M. It does not require C, a scaffold collision, a particle emitter or a physical energy field. The continuous planar polar curve is a three-petal rose; the sampled 3D polyline and its changing amplitudes produce the familiar star-like connections. The continuous macro obeys C3 covariance under θ→θ+2π/3 at fixed A. A time-dependent finite trajectory need not be exactly C3 symmetric.

| Recalled feature | Supported mechanism and limit |
|---|---|
| Large repeated arms | Macro harmonic, clock directions and changing radii already generate them. Demonstrated by β=0 and the component figures. |
| Upper/lower excursions | Sign of z gives macro height. The six frozen extrema alternate; default twelve samples instead have paired signs. βC can change the total's height sign. |
| Fine branching / split arms | Successive radii and polyline connections can branch visually even in M; changing C translates/deforms each macro point by βC. No topological branching of a smooth manifold has been proved. |
| Finite diagnostic spikes | Large ΔM/ΔC, phase jumps, or the clock term; definitions and examples in §5. Large turning alone is a different diagnostic. |
| Large excursions / numerical blowup | Nonlinear Ω growth can enlarge C quadratically. A bounded scalar macro does not bound the blend. Overflow/NaN is a numerical failure, not infinite physical energy. |
| Handedness/asymmetry | Relative phases and C, plus initialization, unequal k, angle convention and possible EMA offset. No universal ambient handedness classification follows. |

The term “manifold” is retained from source usage. A discrete trajectory plus a line plot is not by itself a proved differentiable manifold or attractor.

![Direct components on one common coordinate scale. Viewer-default settings, 300 stored points. Macro already supplies the large arms.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/02_direct_components.png)

## 4. Torus and display alternatives

Keep four maps separate:

| Map | Source definition | Information and relation |
|---|---|---|
| A: cylinder-like readout | (κ cosθ, κ sinθ, z) | Uses κ,q,z; not direct T. `geometry_3d` and the alternate cylinder hardcode 12 in θ. |
| B: history-normalized torus | r=r_max κ/(1+κ); H_z=max_history|z|+10^-9; χ=πz/(2H_z); ((R+r cosχ)cosθ,(R+r cosχ)sinθ,r sinχ) | Display transform of A's scalar inputs, conditioned on whole-history H_z and chosen R,r_max. The alternate version accepts `n_sectors`; the primary helper hardcodes 12. Defaults agree exactly in the verification. |
| C: direct vector | T=αM+βC | Depends on channel phase information missing from A/B. It is generally a different observable. |
| Viewer channel torus | For each j, fixed azimuth a_j=2πj/3, b_j=argΩ_j, r_j=.6[1+.4 log(1+|Ω_j|)]; ((2+r_j cos b_j)cos a_j,(2+r_j cos b_j)sin a_j,r_j sin b_j) | Three separate channel curves. Uses neither q nor scalar z nor T. Tube radius varies with channel magnitude. |

For fixed known H_z, R>r_max>0, κ>0 and the displayed χ interval, A→B has a conditional inverse: horizontal radius s_B gives u=s_B−R, r=√(u²+Z_B²), χ=atan2(Z_B,u), κ=r/(r_max−r), z=2H_zχ/π and θ from the horizontal azimuth. At κ=0 information is lost; without H_z there is no universal pointwise inverse. B uses the whole selected history, so extending or truncating that history can move previously plotted points. It is not an intrinsic new state evolution or a global coordinate change on the full Ω state space.

A concrete obstruction to identifying C with A/B is Ω_a=(1,1,1) and Ω_b=(1,i,1). Both have κ=√3 and, at the same q,t, the same staged z. But C_a=0 and C_b=(-1,0,1). Thus their direct totals differ when β≠0, although A/B agree. For β=0, M can be computed from κ,q,z, but z=0 collapses all M to zero and erases information. That also fails to give a global invertible equivalence.

The 3D viewer overlays T, M or C at the **origin** on axes also containing the channel torus. It applies a single retrospective scalar per chosen mode:

\[
Z_{display}=\frac{0.85\times0.6}{Q_{0.99}(\{\|Z_n\|:\|Z_n\|>10^{-12},\ \text{finite}\})}\,Z,
\]

with fallback denominator 1 when needed. It is uniform scaling, not a rotation/translation into six slots. Each radio selection (`total`, `macro`, `chiral`, `off`) gets its own scale; small C may therefore look large when selected alone. `off` hides the overlay. The trail slider limits the **channel-torus** lines, while the Z overlay is drawn from its full stored series. The viewer also uses a compressed axes box (1,1,0.6), whereas the new figures use equal coordinate units.

The separate elevation readout is atan2(T_3,√(T_1²+T_2²)+10^-12), with scalar fallback. Strong-Δ bar coloring thresholds √((Δκ)²+(Δelevation)²) at half its run maximum and assigns the event to q[n+1]. These are diagnostic bars, not gap crossings. `gap_bottom` and `gap_top` position UI controls between panels. The independent `compute_phi_index` helper uses arg(meanΩ), which is not the master clock counter. The RSB halo consists of toroidal band rings; the inspected return-key mismatch can leave its expected `E_final` absent. None supplies a six-gap registration.

The viewer's noise slider adds measurement noise to saved κ, scalar z and observed J **after** the Ω and direct-vector histories have been computed. It does not set the core's optional `omega_noise_sigma`. Direct M/C/T and the channel-torus curves therefore remain unchanged by that measurement-noise path, while scalar plots, J coloring and diagnostics consuming the altered histories can change. This distinction prevents an apparent mismatch between two displays from being misidentified as an additional Z evolution law; all new runs here have both noise paths off.

![A, B and C evaluated on one history. Equal units within each panel; their coordinate scales differ and are labelled.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/04_distinct_embeddings.png)

## 5. Spike-diagnostic mathematics and recovered diagnostic settings

For successive stored samples n,n+1 and selected Z key K,

\[
d_Z=\|Z^K_{n+1}-Z^K_n\|,\quad
d_\phi=\left|\operatorname{wrap}_{[-\pi,\pi)}\arg\left({1\over3}\sum_j\Omega_{n+1,j}\bar\Omega_{n,j}\right)\right|,
\]
\[
d_q=\mathbf1[q_{n+1}\ne q_n],\quad d_\kappa=|\kappa_{n+1}-\kappa_n|,\qquad
v_n=\sqrt{(w_Zd_Z)^2+(w_\phi d_\phi)^2+(w_qd_q)^2+(w_\kappa d_\kappa)^2}.
\]

Defaults are (1,1,0.5,0). The phase term is **phase of the mean complex product**, not mean of channel phase changes. Missing/short optional histories contribute zero. At a zero mean product the numeric angle convention is not a resolved physical phase. A normal one-sector clock increment gives d_q=1 at every step, including 11→0, so the diagnostic has a 0.5 floor even for stationary Z and Ω. Changing the selected Z key changes only the d_Z term; common phase/clock terms can make all three components look “spiky.”

No division by dt occurs. The weights mix an uncalibrated displacement with dimensionless phase and sector terms. It is not a physical velocity. The directional alternative in `vrec_geom_direction` is acos(unit Z_n·unit Z_{n+1}), returning NaN at norms ≤10^-9. It is not the polyline curvature angle between ΔZ vectors used by `side_zchiral_probe` either. The 3D viewer prefers the direction metric; its exception fallback recursively calls its own wrapper instead of the imported full metric, which may ultimately yield an empty diagnostic. This bug is preserved, not exercised or fixed.

Verified separating witnesses: a radial move (1,0,0)→(10,0,0) has full v=9 and direction angle 0; (10^-8,0,0)→(-10^-8,0,0) has v=2×10^-8 and angle π; a clock-only change with constant Z has v=0.5 and angle 0. These use zero/missing other terms. Large directional turns near cancellation do not imply large displacement.

**Exact export chain.** `run_triocta_once` creates a normalized seeded complex Gaussian state; direct Z columns feed the full metric; the picker selects finite values ≥ an absolute threshold or a finite-value quantile. Index j in v corresponds to centre row j+1, time `arange(steps)[j+1]*dt`. The series CSV has a blank/NaN first v. Each spike exports an inclusive clipped ±window interval (default 25); overlapping windows are intentionally duplicated. The 3D scatter highlights row j+1 within its last-N view (default 500). There is no equal-axis treatment in the original plot.

Two implementation traps matter. `pick_spikes` computes its threshold from its argument but selects indices from global `v_rec_series`; the writer sets that global correctly. Independent use can access a stale or absent global. Also `default_k_triplet(float(k3_scale))` passes the CLI number into a **mode-name** argument. An unmatched mode falls back to `theta_scaled`; therefore this CLI's `k3_scale` is ignored by the recurrence although logged. The harness confirms identical Ω for labels 0.1 and 2.0. The viewer genuinely multiplies k[2] after selecting `theta_soft`; the side probe instead uses k=(1,1,k3). Their k3 labels are not interchangeable. Quantile thresholds with ties can select every sample; “99th percentile” does not guarantee exactly 1% events.

**Preserved evidence audited.** The two five-file packages in [vrec_ts_subcritical](C:/TORMENT/TRIOCTAGON_new/kernel_TO/vrec_ts_subcritical) and [vrec_ts_critical](C:/TORMENT/TRIOCTAGON_new/kernel_TO/vrec_ts_critical) contain the series, repeated-window CSV, summary and two images. Both summaries state seed 2158500047, ε=0.0005, k3 label 0.1, dt=0.02776, 2000 samples, threshold 0.8, window 25; coupling is 0.664 or 0.667. Neither records λ_phase or a full source hash.

| Check | g=0.664, “subcritical” | g=0.667, “critical” |
|---|---:|---:|
| Preserved finite v≥0.8 count | 26 | 1277 |
| Preserved finite direct-Z rows | 2000 | 1279 |
| Preserved window rows checked against centre/clip formula | 1026, all agree | 64827, all agree |
| Current default λ_phase=0.001: finite event count | 27 | 1244 |
| Current default: finite direct-Z rows | 2000 | 1246 |
| Explicit phase-off rerun: event count | 26 | 1277 |
| Phase-off: maximum Z error on jointly finite rows | 0 | 0 |
| Phase-off: maximum v error on jointly finite rows | 0 | 0 |
| Phase-off: whole Z/v arrays, including NaN positions | Equal | Equal |

Both initial J values match. With the current default, the first Z discrepancy already occurs at row 1. Disabling only phase synchronization reproduces the complete saved Z and v arrays exactly under the present runtime; it is a strong effective-configuration recovery. An inspected earlier [17766958 core](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17766958/model_core.py:68) lacks the triad synchronization step. That is corroborating lineage, not proof that this exact file produced the saved CSVs. No source version or omitted metadata was silently filled in.

The phase-off comparison also has zero maximum J error on jointly finite rows. The CSV time grids exactly equal the writer's `arange(2000)*0.02776`; this is checked separately from the core's repeated floating additions of dt.

For new default λ_phase=0.001 reruns, the critical case first has nonfinite Z at zero-based row 1246 and nonfinite Ω at 1247. Its maximum finite full v is dominated by d_Z≈6.45276×10^56; d_φ≈π, d_q=1. The subcritical maximum uses d_Z≈0.972683, d_φ≈3.140380, d_q=1, so phase dominates its squared sum. In that run phase-plus-clock alone exceeds 0.8 on 25 transitions and d_Z alone on only 3, while total finite events number 27. In the critical run those separate counts are 1245 and 934; they are not subsets of finite full-v counts once other terms overflow. Counts always specify the finiteness convention.

The saved nonfinite tail is part of the evidence, not a reason to call the whole trajectory a stable attractor. The new execution log retains overflow warnings. The harness handles those results explicitly: JSON uses null for missing finite statistics and string nonfinite markers where necessary. Early harness iterations exposed an overly broad finite-bound assertion and JSON nonfinite serialization; those harness issues were corrected without changing any source or tolerance in an original checker.

![New reruns at the preserved settings but current default synchronization. Left diagnostic ordinate is explicitly clipped at 4; right plots show first 400 points, with finite threshold events marked. These are not mislabeled reproductions of the original phase-off runs.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/03_preserved_settings_spikes.png)

Other reached diagnostics do not add a physical spike law: `edge_map` trims at the first nonfinite Ω/κ/J row before summarizing; `diagnose_bottom_lid`'s misleadingly named finite-prefix helper trims to the **last** finite row and does not remove possible interior nonfinite holes. `chirality_lab` fits J from Z and from regularized finite-difference curvature/torsion; its `U_geom=chi_geom**2` is a fitted diagnostic, not a recovered potential or conservation law. Its derivatives use mean stored dt, unlike full v_rec. `estimate_z_stabilization_time` compares prefix means with a tail-mean direction and returns an early qualifying index; it does not require remaining settled thereafter. None of these tests proves a stationary physical energy structure.

## 6. Bounded parameter dependence and apparent stationarity

The verification uses 17 runs of 300 samples around viewer settings, one corresponding EMA run, three 2000-sample current-default spike runs (including the k3-label identity check), and two phase-off diagnostic reproductions: **23 fixed runs, no adaptive parameter search**. Ω initialization is explicitly seeded, source noise is off and all run inputs are in the script. `run(seed=...)` alone merely annotates metadata; it does not seed the source's optional global-noise generator.

Viewer baseline: ε=.05, g=.2, λ_phase=.001, dt=.05, seed42, k=(1,1.104941840306724,2.52053634379122), remaining Z defaults from §1. The CLI/core default scaled k is instead (1,1.2208964704604097,6.35310346037241). These differences are retained.

| Parameter | Mechanism and bounded observation |
|---|---|
| ε | Scales local cubic/radial update, not the whole step. Perturbations .045/.055 change Ω and peak direct norm slightly (about .25660/.26098 versus .25879). Large amplitudes can overshoot. |
| g_coupling | Multiplies L3. Around zero, with ε=0, transverse factor is 1−3g; near 2/3 it approaches −1. The cubic, unequal k and synchronization alter actual stability, so 2/3 is not asserted as a universal threshold. The preserved .664/.667 pair shows the local contrast directly. |
| k and k3 | Unequal channel gains change amplitudes and relative evolution. Genuine viewer k3 multipliers .9/1.1 give peak direct norms .25696/.26062. The spike CLI's logged value is inactive (§5). |
| λ_phase | Changes relative phases after the radial/coupling step. Baseline 0/.002 differs only modestly from .001 over 300 samples, but is decisive for exact saved-run reproduction and late unstable evolution. |
| θ_lock | Shifts scalar harmonic relative to q and C; .344 changes the baseline direct history by maximum norm about .07338. It is not a recovered scaffold-placement angle. |
| λ_vp | Linear macro amplitude. Increasing by 20% changes T by max .04731 with Ω bitwise unchanged. |
| γ | Controls the staged envelope. Setting γ=0 preserves Ω and leaves repeated macro excursions; last-60-sample maximum ΔT is .83047, versus .00078194 for γ=.577. H has no such envelope. |
| α,β | Readout mixing only. α=0 isolates weighted C; β=0 isolates M; doubling β doubles the departure from M. No recurrence changes. |
| dt / ordering | Changes historical t and z envelope per iteration, but not Ω. Doubling dt to .1 leaves Ω bitwise identical and lowers the final-window ΔT maximum to about 7.36×10^-7. Saved rows are pre-step; the CLI exports its nominal evenly spaced time grid. |
| Seed | Changes the initial complex state. Seed43 changes T by max .08622 in this fixture. It is not a general ensemble conclusion. |

At the baseline, max‖M‖=.23656861, max‖C‖=.12614494 and max‖T‖=.25878878. The final C norm is about 1.39×10^-17 here; this is numerical behavior of one run, not proof that chirality must decay. Macro and total still have final norm about 7.17×10^-5. A plotted history accumulates all earlier excursions even as the current point approaches the origin. That alone can make a visually stationary star persist on screen.

With fixed κ, γ=0 and C settled, clock cycling gives repeated geometry rather than a fixed state. With EMA, memory offsets the repeated geometry: the same Ω history produces final ‖T‖≈1.27899 and last-window maximum ΔT≈.89402, versus the decaying staged case. Those alternatives explain why a recollection of persistent geometry cannot determine which core variant ran. Per-mode percentile display rescaling further masks absolute shrinkage. No asymptotic attractor theorem is claimed from these finite runs.

For finite Ω, γt≥0 and finite λ_vp,

\[
\|M\|\le\sqrt2|\lambda_{vp}|,\qquad
\|C\|=\|x\times y\|\le\|x\|\|y\|\le\tfrac12\kappa^2,\qquad
\|T\|\le|\alpha|\|M\|+|\beta|\kappa^2/2.
\]

Thus the blend has no uniform amplitude bound inherited from ρ alone. Conversely Ω growth does not force C growth: on the real balanced line with equal k and no forcing, C=0. For k=1, ε=.05, real balanced channel amplitude a obeys a_next=a[1+.05(1−a²)]. Starting at a=10 gives an explicit finite-step increasing-magnitude witness. It is a deliberately labelled mathematical example, not a claimed historical run. For γ<0 or backward t, even the macro envelope can grow; the bounded claim above includes its sign/time hypothesis.

![Envelope, EMA memory and blend comparisons. Each panel uses equal coordinate units but its own labelled range; this is not the old viewer's percentile scaling.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/05_envelope_memory_blend.png)

## 7. Chirality's contribution and its limits

Paper B's identity C=ReΩ×ImΩ is used as a **channel-indexed transported-area triple**. Writing components as plotting coordinates in the old viewer does not supply an ambient geometric transport into octagon faces or gap normals.

Exact consequences are C(e^{iχ}Ω)=C(Ω), C(conjΩ)=−C(Ω), and C(sΩ)=|s|²C(Ω) for a common complex scalar s. The cubic J is not invariant under common phase rotation: Ω1 conjΩ2 Ω3 gains e^{iχ}. J sign therefore cannot be used as the sign of every component of C or as a universal handedness label for T.

For fixed M and Ω,

\[
T(\beta)-T(0)=\beta C,\qquad
T_{conj}=\alpha M-\beta C,
\]

because κ, q,t and hence the staged M are unchanged by conjugation. This is pointwise reflection about αM in the arithmetic blend, **not automatically one spatial reflection of the whole curve**. It also does not apply without qualification to H's scalar memory, whose J-driven offset reverses when Ω and initial memory are conjugated/reversed consistently. Ordinary channel permutations are likewise not automatically the ambient 120° rotation applied to macro plotting coordinates; unequal k further break recurrence permutation equivariance.

At a repeated clock sector, varying C gives a translated family around the macro point; these can split a visible arm. A constant C produces a constant translation, not new branches. A C contribution with sufficiently large third component can reverse the total's top/bottom label, and a C nearly opposite αM can create rapid changes of direction near a small total norm. Threefold symmetry survives only with the required joint covariance of both components; it is not guaranteed by the blend notation.

In the first 400 points of the critical-setting default rerun, M shows the star arms while weighted C makes an elongated approximately opposite-direction excursion. T contains both, visibly splitting and stretching the connections. Later large d_Z comes from the growing C contribution while the finite macro remains bounded. This is component evidence for this run, not a theorem that all fine branches or all high-v events are chiral. The independent phase/clock terms remain present in each diagnostic comparison.

![Critical-setting component separation on one common coordinate scale, first 400 stored samples.](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/figures/06_critical_component_separation.png)

**Qualitative image limit.** The referenced rough author image was not present in this work-order attachment directory, which contains only `Pasted text.txt`; no pixel-level comparison or original-run identification is claimed. The exact title “Z_vec trajectory” is recovered in `analysis_tools.plot_Zvec_trajectory_3d`. The new direct M/T figures naturally show a central multi-arm/star pattern; C alone in the baseline does not. This is qualitative agreement with the written recollection. The preserved subcritical last-500-point image instead magnifies a tiny nearly linear late tail, showing why run window and autoscaling matter. No parameters were fitted to a picture.

## 8. Six-gap registration result

**SIX_GAP_REGISTRATION = NOT_FOUND within the inspected source and diagnostic closure.** The viewer does have a display-only overlay of a scaled Z curve and a torus, but this does not warrant classifying a six-gap map as `DISPLAY_ONLY`: no six corresponding gap anchors are identified even in that overlay.

The accepted Paper-D planar scaffold has E_i=A_i→B_i and G_i=B_i→A_{i+1}, with A_i=p u_i−(s/2)t_i, B_i=p u_i+(s/2)t_i, g_gap=√3p−s/2>0. Equal g_gap=s yields the regular hexagon. Its six **alternating edges/connectors**, its six vertices, the three reference corner cells, and the newly recalled three upper/three lower 3D gaps are not interchangeable sets. Paper D does not supply a 3D lift with six gap centres, heights, normals and a map from T. Paper C's welded local module remains a different specified realization. Nothing in this report adopts new scaffold geometry into code.

The bounded source examination found:

| Candidate evidence | Actual object; registration disposition |
|---|---|
| Primary geometry helpers | Scalar cylinder/torus or direct vector extraction; no gap parameters or attachment call. |
| 3D viewer selectors, scale, torus and halo | Uniform origin-centred overlay, three channel azimuths and RSB band rings; no octagon/notch/rim coordinates. UI “gap” variables are panel layout. |
| `diagnose_bottom_lid` | Cosine preference diagnostics only; no bottom-lid surface or upper/lower slot definitions. |
| CP windows | Sector centres 3 and 9 with half-width1: {2,3,4,8,9,10}. Six marked sectors in two windows are not three upper and three lower spatial gaps. |
| Dual-tetra display | Permutes intensity-basis coordinates (c_u,c_x,c_y) into (c_x,c_y,c_u) and scales by the history maximum norm; draws opposite tetrahedra. It neither uses T nor defines six gap crossings. |
| Tangent-corridor and semantic diagnostics reached from `run_sim` | Clock/intensity-basis jumps, clustering and CP masks. The tangent helper even uses a separate XY formula (R+ρ cosθ)(cosθ,sinθ), not B's χ(z). No gap-placement transformation follows. |
| External three-body “six-ray” probe | Nearest planar multiples of π/3 for body velocity azimuths. Bodies move in a reflecting box; at Z-turn events their velocities are reset to three planar q-based directions. This is neither direct T position nor upper/lower scaffold ports. |
| Preserved spike images/series/windows | Direct T and times/diagnostics; no host geometry, six anchor coordinates or transform metadata. |

The source call edges and parameter omissions were followed far enough to recover both saved diagnostic series without adding a source search campaign. No relevant historical figure in these reached outputs resolves the attachment. This is a bounded negative finding, not a proof that no lost construction ever existed. The source-to-model record already distinguishes missing original construction files from current geometry; their contents have not been recreated.

The precise missing interface is a specification of six reference positions (or their defining cells/curves), upper/lower labels, clock-to-slot ordering, and whether direct T is drawn there or passed through a placement map. Only the first discrimination is asked in §10; a complete new model specification is not requested from the author.

## 9. Gap relative to the modern implementation

The current [modern dynamics](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:1) explicitly has no historical clock, dt or Z state. [readouts.z_chiral](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:1) does implement raw C with guarded numerical products. That existing component is acknowledged: `MODERN_IMPLEMENTATION_HAS_HISTORICAL_Z=NO` means **the historical composite clock/scalar/M/T system is absent**, not that the modern implementation contains no chirality readout.

Modern folded-face geometry and the face-state representation are implemented; the accepted boundary/SRG option and orientation cycle remain intact. They do not supply the absent historical q,t,z,memory/blend trajectory or its six-gap registration. No Z restoration, alternative source map, new dynamics, geometry adoption, gap-energy law or change to Papers A/B/C/D was made.

Verification result: **63 named computational checks passed**, encompassing recurrence/readout witnesses, historical ordering and aliases, dot products, no-feedback equalities, EMA formula, embedding agreement, spike-window alignment, full phase-off saved-array parity, counterexamples and finite-domain bounds. The harmonic proof and missing-registration disposition are written mathematical/source arguments, not extra computational predicates. Twenty-three fixed numerical runs are finite demonstrations, not proofs of global stability or attractors.

The six figure files are generated by the one script; all were visually inspected, with equal coordinate units and explicit finite windows/scales. Figure 3 clips only the diagnostic plot ordinate, labels that choice, and retains the complete numeric results. It does not conceal the nonfinite tail in the report.

Reproduction from the project root using the existing dependency directory (no installation needed in this environment):

```powershell
& 'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -X utf8 `
  'research\GPT_proof\historical_z_manifold_v0.1\verify_historical_z.py' `
  --deps 'trioctagon-physics\papers\PAPER_B\.build\plotdeps'
```

Do not rerun `--baseline` over the preserved before-record: the script refuses replacement. A later rerun regenerates only the new verification outputs; it does not modify its scientific sources. [Preservation receipt](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/preservation_receipt.json) verifies the before-record of **499 existing files**, including all tracked repository paths, top-level staged-kernel Python sources, both original diagnostic packages, the committed-core snapshot and continuity/source records. HEAD, index entries and full repository status are compared before/after. The package is outside the Git repository; publication state remains unchanged at `505821a77c3aa1df89a2c400c65ba33149e635c8`. No staging, commit, push, cleanup or paper edits occurred.

## 10. Exact remaining author question and stop boundary

**Did the Z curve itself define the six visual gap anchors, or was it transformed into separately drawn upper/lower scaffold gaps?**

This asks only about the remaining attachment interface. The equations, diagnostic settings and alternative displays do not need to be reconstructed again. No new design begins before that interface is identified or supplied as an explicit new convention.

```text
THIRD_HARMONIC_SIX_EXTREMA = PROVED
  Scope: nonzero amplitude, frozen kappa/time angular function; default samples are not exact extrema.
DIRECT_Z_VEC_MECHANISM = RECOVERED
SPIKE_MECHANISM = RECOVERED
  Scope: source diagnostic and finite-run mechanisms, including numerical overflow; no universal stability claim.
Z_MACRO_ROLE = CLOCK_HARMONIC_ARMS_AND_SIGNED_HEIGHT_WITH_STAGED_ENVELOPE
Z_CHIRAL_ROLE = CHANNEL_AREA_DEFORMATION_AND_POSSIBLE_LARGE_EXCURSIONS
Z_TOTAL_ROLE = ALPHA_MACRO_PLUS_BETA_CHIRAL_DIRECT_READOUT
TORUS_RELATION = CONDITIONAL_SCALAR_DISPLAY_TRANSFORM_DISTINCT_FROM_DIRECT_TOTAL
SIX_GAP_REGISTRATION = NOT_FOUND
PHYSICAL_ENERGY_INTERPRETATION = NOT_PROVED
MODERN_IMPLEMENTATION_HAS_HISTORICAL_Z = NO
  Scope: composite historical mechanism; modern raw Z_chiral does exist.
AUTHOR_MEMORY_REQUIRED = ONE_FOCUSED_QUESTION
```
