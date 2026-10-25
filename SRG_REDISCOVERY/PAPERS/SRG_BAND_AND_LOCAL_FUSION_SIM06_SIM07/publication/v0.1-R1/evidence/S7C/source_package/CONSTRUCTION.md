# The complete Universe construction

The program evolves indexed points, not rigid bodies, spacetime cells or containers. Each has a position X_i and real amplitude R_i. Neighbor selection controls local motion and exchange; a second movement stage uses either local centers in a specific order or one global center. Frequencies are labels chosen during initialization, and the clipping limit is a prescribed function of the pass counter.

**S** denotes the unchanged [srg_condensate_breaking.py](original/srg_condensate_breaking.py): 30,165 bytes, 778 lines, SHA-256 `a645a3bb564a2cae5e2b3ac3744f3f34f559a67132f255b3b0a97d277e68beb5`. Line numbers below refer to that exact file. All equations are static transcription; no transition was evaluated.

## State, initialization and retained information

S:60–96 constructs X in R^(N×3), R in R^N, V=0 and pass_count=0. If supplied, `seed` resets NumPy's global RNG; X is drawn first from the requested uniform spatial interval and R second from the requested uniform amplitude interval. Defaults are X in [−5,5] and R in [0,.3]. With multi_freq enabled, the constructor next draws each frequency independently from

\[
\mathcal F=\{.244,\ .244\phi,\ .244\phi^2,\ .244/\phi\},\qquad \phi=(1+\sqrt5)/2.
\]

Allocation is not balanced and does not guarantee every spatial population contains every label. With multi_freq disabled, frequencies are all .244 and no frequency-choice draw is made. Frequencies never evolve inside the class. There is no separate band_id array, dark channel or complex phase.

| Parameter / stored item | Constructor role | Source |
|---|---|---|
| horizon | None by default; finite value changes graph selection **and fusion branch** | S:61–72; 105–125; 178–192 |
| multi_freq / breathing | Both false by default | S:61–87 |
| alpha, beta | .05 local linear movement; .15 tanh movement and amplitude averaging | S:90–91; 147; 168 |
| lam_H | .05 prescribed H multiplier | S:92; 173–176 |
| k_neighbors | At most five selected non-self neighbors | S:93; 120–123 |
| base_L | 9; determines prescribed clipping schedule | S:87; 98–103 |
| gamma_srg | .08699 stored, **never read elsewhere in this file** | S:94 |
| V | Last completed displacement; read by GRF observer, never as momentum | S:68; 202; 244 |
| metrics_history | One aggregate record after each completed pass; no initial row; no full X/R/V snapshots | S:96; 203–266 |

Continuation requires X, R, pass count, fixed frequencies/configuration and RNG state. V and metrics report the past; they do not steer the next pass. L is calculated when needed, not separately carried. There are no physical units, explicit dt, spatial boundaries, wrapping, velocity damping, action or energy functional in this class. Initialization ranges are not later walls.

## One complete pass, in source order

Let incoming state be X=X_(p−1), R=R_(p−1). S:156–158 increments p, sets t=float(p) and copies old_pos=X for the later displacement diagnostic. Every driver uses direct calls/loops; there is no animation callback or repeated-frame clock.

**1. Incoming neighborhood, S:105–125 and 160.** Compute Euclidean d_ij=||X_j−X_i|| with squareform(pdist(X)). For finite horizon h, candidates satisfy d_ij<h strictly; self is explicitly removed. For None, all non-self indices are candidates. From these, `argsort` chooses up to five nearest. A finite horizon is therefore a radius filter followed by a nearest-five cap, not an all-points-within-radius graph. Equal-distance ties inherit NumPy sort behavior. Empty rows remain empty. Unlike Tower II's unrestricted slice, this implementation explicitly excludes self in both branches.

The binary directed graph and incoming distances are computed **once per pass**. Subsequent loops obtain selected IDs using `np.where(adj[i]>0)`, hence ascending ID order, not distance order. They do not rebuild the graph after movement.

**2. Simultaneous local movement, S:162–168.**

\[
\ell_i=|N_i|^{-1}\sum_{j\in N_i}(X_j-X_i),\qquad
Y_i=X_i+.05\ell_i+.15\tanh(\ell_i).
\]

An empty N_i gives ell_i=0. All lap values are calculated from incoming X before the array addition. tanh is componentwise. This position average has neither amplitude nor inverse-distance weights.

**3. Synchronous amplitude exchange and optional sine, S:127–153 and 171.** Start R_new=R.copy(). For nonempty N_i, first normalize inverse-distance weights:

\[
u_{ij}=(d_{ij}+10^{-8})^{-1},\qquad \bar u_{ij}=u_{ij}/\sum_{j\in N_i}u_{ij}.
\]

If multi_freq is false, W=bar_u. If true, form

\[
v_{ij}=\bar u_{ij}\exp[-5(\omega_j-\omega_i)^2],\qquad s_i=\sum_jv_{ij}.
\]

Only if **s_i>10^−10** does the code renormalize W=v/s_i and continue; otherwise it skips this row. This is a guard after the first distance normalization, with equality taking the skip branch. It is not Tower II's guard on unnormalized distance/frequency products. No extra guard is applied to the initial inverse-distance normalization.

For an active row,

\[
B_i=R_i+.15\left(\sum_j W_{ij}R_j-R_i\right).
\]

When multi_freq is true, multiply B_i by 1+.01 sin(2pi omega_i p). When false, that multiplication is absent. Empty/guard-skipped rows keep B_i=R_i and skip the sine. Every right-hand side reads incoming R; the newly computed R_new is installed only after the loop. Distances still come from incoming X even though the position array is already Y. There are no Tower II phi-ratio, sum-frequency or difference-frequency additions. Phi determines the supplied label catalogue; the exchange kernel uses an ordinary squared frequency difference, not a log ratio.

**4. Common prescribed H modulation, S:42–54; 173–176.**

\[
H(t)=2e^{-.5t}\cos t+e^{-.3t}\sin t+1.5e^{-.7t}+e^{-.4t},\qquad
Q_i=B_i\left[1+.05H(p)/H_{\max}\right].
\]

H_max is defined once at module load by the maximum of |H| on the original 50,000-point linspace over [0,100], plus 10^−12. SIM07 did not execute that expression. H uses elapsed integer passes, not state history or a memory convolution. The cosine/sine in H take t as their radian argument; the assigned-frequency sine contains 2pi and treats omega as cycles/pass. The source's omega notation does not eliminate that distinction.

**5. Fusion uses Q before clipping, S:178–192.** This is the central branch distinction.

For a finite horizon, set Y^(0)=Y and visit i=0,…,N−1. Let Y^(i) mean the coordinate array immediately before row i. Reuse the old selected set N_i. If it is nonempty:

\[
c_i^{(i)}=\frac{\sum_{j\in N_i}(|Q_j|+10^{-8})Y_j^{(i)}}{\sum_{j\in N_i}(|Q_j|+10^{-8})},
\quad
Y_i^{(i+1)}=Y_i^{(i)}+.03Q_i(c_i^{(i)}-Y_i^{(i)}).
\]

All other rows are unchanged. Empty rows are unchanged by fusion. The result is Z=Y^(N). This notation describes the ordered writes; it is not an executed auxiliary model.

For horizon=None the code instead calculates one center, including all points,

\[
c=\frac{\sum_j(|Q_j|+10^{-8})Y_j}{\sum_j(|Q_j|+10^{-8})},\qquad
Z_i=Y_i+.03Q_i(c-Y_i),
\]

and applies the vectorized addition once. The center is not recomputed for each row.

In both branches the center weights use absolute resonance, while the displacement coefficient uses its sign. Negative Q pushes away. An inward-pull description is conditional on positive Q and does not itself prove bounded steps or convergence. Local centers have **no distance weighting** and directly exclude i; global centers include it. The finite branch selects at most five neighbors, not every member of a detected spatial cluster or frequency class.

**6. Prescribed bound, signed compressor, noise, diagnostic, S:98–103; 194–203.**

\[
L(p)=\begin{cases}9[1+.3\sin(2\pi .244p)e^{-.01p}],&\text{breathing enabled},\\9,&\text{otherwise},\end{cases}
\]
\[
R_{p,i}=\operatorname{sgn}(Q_i)\exp\{\operatorname{clip}[\log(|Q_i|+10^{-9}),-L(p),L(p)]\},
\]
\[
X_{p,i}=Z_i+\xi_{p,i},\qquad \xi_{p,i}\sim\mathrm{Normal}(0,.01/(1+.01p)),\qquad
V_{p,i}=X_{p,i}-X_{p-1,i}.
\]

The distribution describes the original call, not draws made here. RPCO preserves sign and sends exact zero to zero; its lower bound can amplify tiny nonzero inputs. In the inactive region its real-arithmetic expression is Q+10^−9 sign(Q), not an exact identity. L is a log-amplitude limit, not a membrane in coordinate space. It depends only on p; unlike Tower II, no shared mean R enters it. The declining noise scale is not a friction law on V. Finally `_record(adj,dists)` runs on the completed arrays.

## Line-by-line local fusion read/write trace

| Source | Reads / snapshot behavior | Write / consequence |
|---|---|---|
| S:158 | `old_pos = self.positions.copy()` | Incoming X snapshot retained only for V |
| S:160 | Incoming positions | One adjacency/distance pair, fixed for this pass |
| S:163–168 | Incoming positions until all lap rows exist | One simultaneous position addition makes Y |
| S:171–176 | Incoming R, then post-exchange result | Installs Q; no R changes during fusion loop |
| S:181–183 | i ascending; old adj row | Empty selections skip the whole local fusion write |
| S:184–187 | `self.positions[nbrs]` reads the **current** array; integer advanced indexing creates a new selected array for this call. Absolute Q[nbrs]+1e−8 provides weights | `np.average` returns a new three-component center, not a persistent view or a center cached for later rows |
| S:188 | Current row i, Q_i, freshly computed center | Only position row i changes in place |
| Next i | Earlier IDs may now contain fusion-updated positions; later IDs still contain post-local Y | New center can read earlier writes without any graph recomputation |

At row i, its own coordinate has not yet had its fusion write; earlier rows write only their own indices. If j<i and j belongs to N_i, the center for i uses j's already updated coordinate. If k belongs to N_j, j's previous center may itself have read k. Symbolically, the i-center contains a weighted term

\[
Y_j+.03Q_j\bigl(c_j^{(j)}-Y_j\bigr)
\]

in place of the unupdated Y_j. This displays a possible chain k→j→i within the ordered stage. An indirect self-dependence can also occur if i belonged to N_j, even though i is directly excluded from its own center. No invented numerical configuration, reordered calculation or measured nonzero effect is claimed. Cancellations, zero coefficients or special configurations can make an ordering difference vanish.

## What “horizon” restricts

A finite h restricts the **incoming selections** used by local position averaging, amplitude exchange and local fusion. Those pairs are not re-tested after local movement or after earlier fusion writes. Each direct selected pair obeyed d<h at the incoming boundary, but dependency through several selected links can span farther than h and can pass through earlier updated rows. Thus the rule is not a one-hop-per-pass propagation law or a physical speed limit.

For a fixed incoming selection structure, the finite-horizon state updates have no global data-derived center or mean-R feedback. Components with no intervening selected links lack such direct state-dependency bridges during that pass, unlike Tower II's same-band centers. This is a conditional structural statement; the aggregate tables do not reveal whether particular components satisfy it or remain separate later. Their motion can change future selections. Common H(p), L(p) and noise scale are prescribed schedules, not distant-point data signals. Global observers read all points but are not fed back. A shared RNG stream is a reproducibility dependency, not an amplitude-dependent communication mechanism.

## Observers, not update instructions

S:205–259 receives incoming adj/dists but **does not use either argument**. It reads completed R, X, V, fixed frequencies and p:

- Resonance clusters: sort |R| descending, count adjacent gaps whose absolute size exceeds .05 max|R|, then add one (S:209–214). This is not frequency count, phase synchronization or a fitted spatial cluster. A count of one does not require all values equal.
- Spatial clusters: SciPy average-linkage hierarchy of completed positions, cut at distance 2.0 (S:216–223). This is not the update's horizon/nearest-five graph, nor the driver's original population labels. With N<2 it returns one. Finite horizons can leave rows with fewer than five neighbors, so the earlier unrestricted minimum-six component argument cannot be imported.
- Entropy: P_i=|R_i|/sum|R|, then −sum P_i log(P_i+10^−12), or zero for zero sum (S:225–231). This dimensionless amplitude-distribution statistic is not thermodynamic energy or evidence of information destruction.
- Band outputs: mean |R| for each fixed frequency present, keys formatted to four decimals (S:233–241). No per-band counts, spatial membership or individual amplitudes are exported here.
- `top_seed_id`: argmax|R|, first index on a tie; a winner label, not a leader trajectory. `mean_grf`: mean of 1/(1+||V_i||), not 1/(1+mean speed) (S:243–255).
- R_max/min/mean use |R|; R_std uses **signed R**, not |R| (S:248–251). L_effective recomputes the same prescribed L(p); this call changes no state. Metrics do not stop, delete, merge or relabel points.

## Complete-file map and driver boundaries

| Lines | Content read in full | Role |
|---|---|---|
| 1–36 | Header, imports, warning filter, historical absolute output directory | Dated intentions and import-time side effects; no plotting section |
| 42–54 | H, signed RPCO, sampled H_max, phi | Exact helpers used by this engine |
| 60–153 | Constructor, L schedule, neighborhood and amplitude helpers | State/configuration and incoming selections |
| 155–203 | Full pass | Sequence transcribed above |
| 205–266 | Observers, evolve loop, DataFrame export | Aggregate recording only |
| 273–371 | `experiment_perturbation` | Build 100 passes, reset X/R/V/history/p and kick ID 0; seven 50-pass responses; RNG not reset between kicks |
| 378–497 | `experiment_causal_horizons` | Four supplied populations, six horizon settings × three trials, 100-pass endpoints |
| 504–576 | `experiment_multi_frequency` | Two frequency modes × three trials, 150-pass endpoints |
| 583–656 | `experiment_breathing` | Static/breathing pair, 200 passes, tail and spectral summaries |
| 663–758 | `experiment_full_universe` | Selected 120-point, horizon-6, seed-1618 aggregate chronology, 200 passes |
| 765–778 | Main block | Calls all five drivers; not executed here |

[ORIGINAL_EVIDENCE.md](ORIGINAL_EVIDENCE.md) gives driver overrides, output lines and raw-row attribution. No original driver, class, helper or observer was executed in this investigation.
