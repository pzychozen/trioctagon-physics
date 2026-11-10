# Independent GPT subreview: T03, T06, T07 and D01

Date: 2026-11-10 (Atlantic/Reykjavik)

## Disposition

**No mathematical blocker found in T03, T06 or T07 at their stated assumptions. D01 is correct and should be carried into the manuscript as an explicit sufficiency/necessity clarification. No candidate equation needs changing.** This review examines the algebra, finite-jump account and activity argument. Full mild well-posedness and trace justification are covered by the separate functional review; the power and activity statements here use those stated regularity results.

Sources read: submitted `upload/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_PROOF_REVIEW.md`, especially R3, R6 and R7; submitted analytical start N12–N14 and N18–N24; retained `sources/RX/candidate.tex`, `power.tex`, `hybrid.tex` and `accounts.tex`. The source files were compared directly. No original scientific test suite or published investigation was rerun.

## T03: signs, coefficients, storage and dimensions

The near boundary law `a = sqrt(2) kappa JQ - b` and `J*J = I` give

\[
\langle Q,\mathcal F\rangle
=-\kappa^2\|Q\|^2+\sqrt2\kappa\langle JQ,b\rangle
=-\tfrac12(\|a\|^2-\|b\|^2)=-P_N.
\]

At the far boundary, `d = sqrt(2) C*zeta - c` gives

\[
\dot H_G=\sqrt2\langle C^*\zeta,c\rangle-\|C^*\zeta\|^2
=\tfrac12(\|c\|^2-\|d\|^2)=P_G.
\]

These match the transport stock increment `P_N - P_G`. The original native factor one-half is retained: `J_f x = 2 f` makes native power `-eta_N f.y`, while the carrier source and old receiver cancel the remaining original powers. Thus the total includes old receiver storage once, plus the new transport and receiving stores, with no missing sink. No norm-contraction assumption on C enters this cancellation.

The proposed abstract dimensions are consistent with the retained RX units. The wave square has units `U^2/(L T)` and is integrated against `d xi ds d ell` of units `T L^2`, giving `U^2 L`. The new receiving weight `beta_G` has units `G_o^2 T`, distinct from old `beta_R`, and its stock also has units `U^2 L`. Both terms of the added carrier force have units `U/T`. This establishes commensurability, not SI calibration or material energy density.

The receiving store need not increase monotonically. Empty lines with `C*zeta_0 != 0` give initially negative receiving power. Accordingly the manuscript can claim release back into the traveling state, but should not label the store an irreversible load or infer a full backward-flow theorem from conservation.

## T06 and D01: hybrid count and zero coupling

The source tuple, simultaneous prestage and synchronization conventions are unchanged. A native jump changes x alone. The post-jump endpoint count `t_a < t_j <= t_b` therefore yields exactly `Delta H_total = B_N`, with no impulse in the other states. Finite-step existence follows from a finite native image followed by the global exchange stage. This does not assert an infinite-step bound or continuity across singular prestages.

At `kappa = 0`, the added carrier force vanishes for every prepared new state; the old RX subsystem is exactly recovered. The near reflection `a = -b` has zero net interface power, so the added subsystem conserves its own prepared stock and can still evolve.

**D01 is valid.** If n is normal to the selected carrier plane, then `zeta_0(X) = (0,h(X)n)` is in `ker C*` for any nonzero square-integrable h. With empty lines and zero coupling, the waves remain zero and zeta remains equal to this nonzero preparation. All new interface powers and time derivatives vanish despite positive stored receiving energy. Empty added states are therefore sufficient, not necessary, for inactivity. The analytical start already uses only the sufficient condition; the necessity-sounding work-order sentence is the affected text.

For positive coupling the changed carrier force changes the coupled trajectory. The unchanged form of the native and old-receiver equations does not automatically carry earlier credit, capacity, recovery or convergence theorems into this extension.

## T07: latency, receiving and return

With empty added states, characteristics give `c = 0` before `theta_-`, hence zero zeta and d there; they then give `b = 0` before `2 theta_-`. The receiving stock is zero through the first endpoint by continuity. The immediate launch term `-kappa^2 Q` is correctly distinguished from the delayed incoming-return term.

For the declared preload `Q_0=(P,0)`, `P>0`, with `x_0=z_0=0`, native x stays zero because both f and its derivative vanish there. The old receiver remains dynamically active. Before the incoming return, retained H1 tents and the constant H1 carrier preparation give short-time carrier H1 continuity. One-dimensional embedding supplies uniform positivity `p>P/2` and a bound `|Q|<=2P` after choosing a small positive epsilon.

The scalar receiving equation decouples from the vector Gram block and has a positive integrating factor. Every strict delay sublevel above the attained minimum contains a positive-product-measure patch, including when the minimum is at a G endpoint or elbow. Its positive scalar forcing persists on a nonzero time interval and proves `H_G(t)>0` for each `theta_-<t<theta_-+epsilon`.

The return estimate is correctly normalized. The ratio of the far-effort upper bound to the direct scalar lower bound is

\[
\frac{8 a_o^2 M L\,\varepsilon}{\beta_G\delta_w^2}<\frac12
\]

under the stated `epsilon < beta_G delta_w^2/(16 a_o^2 M L)`. For `2 theta_-<t<2 theta_-+epsilon`, channels with `theta(s,X)<t/2` consequently have the strictly negative scalar return bound in R7.10. That sublevel has positive product measure, giving a nonzero incoming V-valued return trace a.e. in the interval. No assertion about a prescribed trace at the threshold is required.

## Essential manuscript qualifications

- This example is funded by carrier preload. It is not native empty-launch supply, native credit, capacity-sized receiving or recovery.
- Receiving is proved somewhere in the G-indexed field, without equal/simultaneous allocation to all six labels or a physical aperture-flux conclusion.
- Nonzero incoming b alone does not establish nonzero projected `J*b`, positive net carrier work or native credit. Keep that distinction.
- Empty line/nonzero launch corner data are handled as a mild energy solution. The temporary H1 carrier argument does not imply global H1 transport compatibility.
- Abstract endpoint delays and return traces do not establish the central/outward/curved-return physical route, physical placement of the receiving state, or a calibrated clock.

The current proof already contains these qualifications. Manuscript preparation may proceed if the complete review accepts the complementary functional claims.
