# Tower II construction, source and execution order

The simulated objects are indexed points, not rigid bodies or containers. Each row retains its identity while its position and resonance change. “Tower” refers to the assigned frequency catalogue; it does not construct a spatial tower. Two relationships operate at once: a changing local neighbor graph, and permanent band membership used for a separate, band-wide movement.

**S** below means the unchanged [complete original source](original/srg_golden_tower_II.py), SHA-256 `147a32be3b6d6aad17ada6ab7be2fbc3994c3363f74d6a2b351fb8eecda80304`. All source ranges use its original one-based lines. This transcription describes operations; it was not executed as a simulator.

## What is initialized and retained

| Item | Selected historical setting / role | Source |
|---|---|---|
| Positions X | 80×3 real array, uniform draws in [−5,5]; drawn first | S:62–73 |
| Resonance R | 80 real scalars, uniform draws in [0,.3]; drawn after X | S:62–73 |
| Velocity V | Initially zero; overwritten by the completed position difference | S:72; 215 |
| Pass p and RNG state | p=0 initially; optional legacy NumPy seed resets global RNG; later positional draws continue that stream | S:66–73; 130; 213 |
| Band catalogue | B=4, phi=(1+sqrt(5))/2; indices [−2,−1,0,1]; frequencies .244 phi^n | S:31–35; 75–78 |
| Band identity | Construct i mod 4 for i=0…79, shuffle once, attach its catalogue frequency to each point; 20 points per band | S:80–84 |
| Local movement/exchange | alpha=.05, beta=.15, k=5 | S:98–103 |
| Frequency preference | Selected coupling_width=2, rather than constructor default 3 | S:63; 87; 393–397 |
| Additional mixing | nonlinear_strength eta=.001; four phi-ratio targets and sum/difference matches | S:65; 88; 169–188 |
| H schedule strength | lambda_H=.05 | S:101; 192–194 |
| Resonance bound | Base L0=9, initially L=9; selected breathing=true and epsilon=1 | S:90–102; 392–397 |
| Horizon | None in selected configuration; optional finite radius exists in class | S:64; 96; 111–127 |
| Stored observers | metrics_history, band_history, L_history, first-lock dictionary | S:104–109; 218–254 |

The general catalogue construction first sets `half = n_bands // 2`, then uses `list(range(-half, half + 1))[:n_bands]` (S:76–77). The floor is taken before negation; preserve that order for odd B. The selected B=4 yields [−2,−1,0,1]. These source choices are not measured physical constants. Band labels and natural frequencies are assigned once in this selected driver. The tunneling driver changes labels during its separate setup; that is not the selected recurrence.

The state needed to continue this particular calculation is X, R, p, configuration/assigned labels and the NumPy RNG state. V and histories are recorded outputs. L is recalculated from R before every enabled pass, so it is not an additional independent degree of freedom. Original histories contain aggregate observer records, not full X/V/R trajectories. R1 later captured those arrays separately.

## One pass in ordinary language

The program increments the pass counter. It reads the old resonance to choose the clipping limit, and the old positions to choose neighbors. It calculates every local position displacement before applying them together. It then calculates new resonance from the incoming resonance values, including frequency preference and several additive terms. H supplies a common time-dependent multiplier.

With that updated, still unclipped resonance, it computes one weighted spatial center for each band. Each point moves toward or away from its band's center according to its **signed** resonance. It clips resonance, adds the prescribed random positional displacement and records what happened. Neither “lock” nor “survival” changes this sequence.

## Exact selected recurrence

Use incoming state X=X_(p−1), R=R_(p−1). The pass label is incremented to integer p, and t=float(p). The symbols Y, B, Q and Z below name temporary stages; they do not introduce new evolving fields.

**1. Clock and breathing, S:130–138.**

\[
L_p=9\left(1+\epsilon\frac1{80}\sum_i|R_i|\right),\qquad \epsilon=1.
\]

The appended L-history row labeled p reads **state p−1**. Disabled breathing leaves L unchanged at 9 and does not append L-history rows. The selected driver has no continuous timestep or callback: one call advances the integer clock once. The 200-pass driver stops because its loop ends.

**2. Geometry and simultaneous local position movement, S:111–127; 140–148.**

Compute d_ij=||X_j−X_i||. With no horizon, neighbors are the indices in `np.argsort(dists[i])[1:6]`; adjacency is binary and directed. Subsequent `np.where(adj[i]>0)` traverses selected indices in ascending ID order. The unrestricted routine assumes the first sorted element is self; coincident-position/equal-distance ties inherit NumPy sorting behavior. Do not silently replace that with an explicit self filter. The optional horizon branch instead explicitly removes self, accepts only d<h and selects up to five.

\[
\ell_i=\begin{cases}|N_i|^{-1}\sum_{j\in N_i}(X_j-X_i),&N_i\ne\varnothing,\\0,&N_i=\varnothing,\end{cases}
\qquad Y_i=X_i+.05\ell_i+.15\tanh(\ell_i).
\]

tanh acts componentwise. All lap values use the incoming positions; the vectorized addition is simultaneous. This local movement does not use V or resonance. There is no wrapping, reflection or spatial rescaling. The initialization box is not a later boundary.

**3. Resonance exchange, then imposed sine, then additive mixing, S:151–190.**

For each row, use the same incoming distances and incoming resonance:

\[
a_{ij}=\frac{\exp[-2\{\log(\omega_j/\omega_i)\}^2]}{d_{ij}+10^{-8}},\qquad
W_{ij}=a_{ij}/\sum_{j\in N_i}a_{ij}.
\]

An empty neighbor row, or raw weight sum **<10^−10**, skips this whole row's exchange, sine and additional mixing; it keeps B_i=R_i. It does not skip the later H, fusion, clipping or noise. The position stage is already complete, so a weight-underflow skip does not undo its local movement.

For an active row, in source order:

\[
B_i=\left[R_i+.15\left(\sum_{j\in N_i}W_{ij}R_j-R_i\right)\right]
\left[1+.01\sin(2\pi\omega_i p)\right]+M_i.
\]

Here the following expression transcribes the **additions after the sine**:

\[
\begin{split}
M_i={}&\sum_{\substack{j\in N_i\\|\omega_i-\omega_j|>.01}}\eta R_j
\left[\sum_{q\in\{-2,-1,1,2\}}
 e^{-5\{\log(\omega_i/\omega_j)-\log(\phi^q)\}^2}\right.\\
&\left.\quad+\frac12\sum_{f\in\mathcal F}\left(
\mathbf1_{|\omega_i+\omega_j-f|/f<.2}+
\mathbf1_{|\omega_i-\omega_j|>.01}\mathbf1_{\left||\omega_i-\omega_j|-f\right|/f<.2}
\right)\right],\qquad\eta=.001.
\end{split}
\]

The catalogue F contains the four assigned frequencies. Every qualifying match adds a contribution; matching does not choose a new frequency, create a band or subtract a compensating donor loss. The outer frequency-difference guard applies to all these additions. The inner difference-frequency guard is retained even though it repeats that condition here. Source arithmetic traverses neighbor IDs, then powers in [−2,−1,1,2], then the catalogue, testing sum before difference. R_new is a copy, with every right-hand side reading old R. No point receives a neighbor's newly computed R during this pass.

Golden frequency spacing and golden-ratio preference are explicitly inserted. For frozen geometry and assigned frequencies these additional terms are linear in incoming R; the source's “nonlinear mixing” label does not make them products of evolving amplitudes. The full coupled construction is state-dependent because positions, weights, fusion and possibly clipping change.

**4. Prescribed H multiplier, S:37–46; 192–194.**

\[
H(t)=2e^{-.5t}\cos t+e^{-.3t}\sin t+1.5e^{-.7t}+e^{-.4t},
\quad Q_i=B_i\left(1+.05\frac{H(p)}{H_{\max}}\right).
\]

H_max is defined by the original 50,000-point sample of |H| over [0,100], plus 10^−12, evaluated once at module load. Prior retained records report 4.500000000001. SIM06 did not reevaluate it or import that module. The current pass evaluates H(p), not a memory convolution over the trajectory. H decays with elapsed pass number but is not inferred from the moving points.

**5. Band-wide fusion, before clipping, S:196–206.**

For I_b={i:band_i=b}, if |I_b|≥2:

\[
c_b=\frac{\sum_{i\in I_b}(|Q_i|+10^{-8})Y_i}{\sum_{i\in I_b}(|Q_i|+10^{-8})},\qquad
Z_i=Y_i+.02Q_i(c_b-Y_i).
\]

The center is calculated once per band before its inner loop. It is not recomputed after each row's displacement. Bands are disjoint; earlier band updates do not enter another band's center. A singleton band skips this stage (Z_i=Y_i). The weights use |Q| but the movement coefficient uses signed Q. Negative Q pushes away; Q>50 overshoots the center. In the retained selected run Q is positive and below 50, as already established by R2; that conditional fact is not a global property of the code.

All members participate, irrespective of their local graph component or horizon separation. This is not Infinity's single global-center rule. “Band-local” means within a label class, not local in space.

**6. Signed resonance bound, noise, displacement and observers, S:42–44; 208–216.**

\[
R_{p,i}=\operatorname{sgn}(Q_i)\exp\left(\operatorname{clip}\left[\log(|Q_i|+10^{-9}),-L_p,L_p\right]\right),
\]
\[
X_{p,i}=Z_i+\xi_{p,i},\qquad
\xi_{p,i}\text{ is drawn by the original }\mathrm{Normal}(0,.01/(1+.01p))\text{ call},
\qquad V_{p,i}=X_{p,i}-X_{p-1,i}.
\]

These are source noise semantics, **not draws made by this inspection**. The saved noise arrays are included unchanged. RPCO preserves sign, maps zero to zero and boosts very small nonzero magnitudes when the lower bound applies. Inside both bounds its real-arithmetic expression is Q+10^−9 sign(Q), not exactly the identity. L acts only here, after the position fusion has already used Q. It can affect later positions through the next resonance-dependent fusion and feedback, if clipping matters. There is no separate friction multiplier on V. Decreasing noise standard deviation is a schedule, not velocity damping.

## What the observers mean

S:218–250 uses |R| within each band to report mean, maximum, standard deviation, count, assigned frequency/index, and coherence

\[
C_b=1-\frac{\operatorname{std}(|R_{I_b}|)}{\operatorname{mean}(|R_{I_b}|)+10^{-10}}.
\]

First lock records the first pass with C_b>.7 **and** mean |R_b|>.01. Later decreases do not erase that record. Survival counts bands whose mean |R_b|>.01; no point or band is deleted. The original band record stores mean_GRF_b=mean_(i in I_b)[1/(1+||V_i||)], an observer, not a feedback gain. R1 additionally records the whole-field mean of these reciprocals. Original global metrics store mean/max |R| and surviving-band count. There is no mechanical energy, action or conserved physical momentum defined by this class. R1's squared-resonance sum is explicitly an added diagnostic, not historical energy accounting.

## Driver, timing and complete-file map

`experiment_self_coupled_breathing()` (S:376–472) constructs N=80, B=4, seed=2038 for each epsilon in [0,.1,.5,1,2,5,10], width=2, with breathing enabled iff epsilon>0. All other options retain the constructor defaults. It calls `evolve(200)` (S:398). We select epsilon=1; no other epsilon was studied anew.

The mean/std/range of L use all 200 incoming-state readouts. The spectrum uses `L_values[50:]`: pass labels 51–200, reading R states 50–199. The variable `L_detrended` only has its mean removed. After a std>10^−8 guard, the source selects the largest non-DC rFFT power and calls it oscillating if that bin exceeds 1% of total power (S:407–418). Frequencies are cycles/pass, with bin spacing 1/150. End-of-run survival and mean R instead read **completed state 200** (S:432–445). The CSV is written at S:452–453. The success message at S:459–461 overinterprets its observer.

| Complete-file section read | Implemented role; bounded study treatment |
|---|---|
| S:1–30 | Historical intent, author/date, imports, warning filter, absolute original output directory. Not a recovered execution timestamp. |
| S:31–254 | Constants, helpers, complete class, observers and finite evolution loop; reconstructed above. |
| S:262–368 | Master-equation driver: several band counts/trials, then zeta-based predicted gamma and lock-time comparisons. Zeta/LOCK_PRODUCT do not enter the class update. Its predicted gamma is not an independently measured dynamical coupling. No new analysis of that experiment. |
| S:376–472 | Selected seven-setting breathing driver; epsilon=1 historical anchor. |
| S:480–588 | Enhanced spontaneous-generation driver with different band count/mixing settings and peak observers. Assigned labels remain fixed. Its line-552 `f_tower % .5` is not generally the correct folding alias for a real sampled sinusoid. No new spectral audit performed. |
| S:596–744 | Separate cluster/bridge/horizon setup, band changes during setup, 50 settling passes, then R perturbation and 100 passes. No unperturbed paired trajectory in this driver; unrestricted same-band fusion also defeats a strict local-horizon interpretation. No outcome reanalysis. |
| S:752–821 | Separate band-count/width phase-diagram driver; observer summary, not a new SIM06 sweep. |
| S:828–842 | Main dispatch calls the five drivers. No animation/rendering section exists; outputs are tabular files and printed text. This dispatch was never run. |

Everything in this selected core that explicitly depends on elapsed time is tied to p: the assigned-frequency sine, H(p), and decreasing noise scale. The local graph, weights, position movement, band centers, bound readout and observers use the current or staged state. They can change over time because the state changes, not because their coefficients are fitted to elapsed time. Histories and first-lock entries preserve observations without steering subsequent movement.
