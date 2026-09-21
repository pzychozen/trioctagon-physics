# Paper A — Symbols and Theorems (quick reference) v0.3
Companion to `PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.3.md` (freeze candidate). Carries the v0.2 content with the spot-check corrections F01 (shift-space scoped to $1\le d\le M$), F09 (full-vs-transverse wording), F14 (the two reflections). One-page glossary and theorem statements stripped of proof.

## Symbols

| Symbol | Meaning |
|---|---|
| $C_M$ | cycle graph on $\mathbb Z_M$, edges $\{n,n{+}1\}$ mod $M$; $C_1$ loop, $C_2$ doubled edge (dart description for these) |
| $\Delta_M$ | cycle Laplacian $(\Delta_M f)(n)=f(n{+}1)+f(n{-}1)-2f(n)$; $\Delta_1=(0)$, $\Delta_2=\big[\begin{smallmatrix}-2&2\\2&-2\end{smallmatrix}\big]$; eigenvalues $-4\sin^2(\pi j/M)\le0$ |
| $L_3$ | $\Delta_3=\big[\begin{smallmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{smallmatrix}\big]$; triangle=complete graph on 3 nodes; spectrum $\{0,-3,-3\}$ |
| $e_j$ | Fourier mode $e_j(n)=e^{2\pi ijn/M}$ |
| $P$ | pull-back $(Pu)_n=u_{\,n\bmod d}$, defined for **all** positive $M,d$; $M\times d$ $\{0,1\}$-matrix |
| $V_d$ | $\operatorname{im}P$ (dim $\min(M,d)$). **For $1\le d\le M$, equal to the shift-fixed space $\{f(n{+}d)=f(n)\}$ iff $d\mid M$** (no shift-fixed characterization asserted for $d>M$) |
| $q$ | $M/d$ (divisor case) |
| $Q$ | $P/\sqrt q$ (divisor case); isometry $Q^\ast Q=I_d$; $QQ^\ast$ = orthogonal projector onto $V_d$. $Q$ real, so $Q^\ast=Q^\top$ (adjoint notation signals the complex inner product) |
| norm relation | $\|P\Omega\|=\sqrt{M/d}\,\|\Omega\|$; for $(12,3)$: $\|P\Omega\|=2\|\Omega\|$ |
| $p$ | covering $p:C_M\to C_d$, $p(n)=n\bmod d$ (graph language for $d\ge3$; darts for $d\le2$) |
| $\mathrm{Deck}(p)$ | $(12,3)$: $\langle n\mapsto n{+}3\rangle=\{0,3,6,9\}\cong\mathbb Z_4$ |
| $N(n)$ | open neighbourhood $\{n{-}1,n{+}1\}$ |
| $\Omega$ | complex state ($\mathbb C^3$ or $\mathbb C^M$); $\Omega_n=r_ne^{i\phi_n}$ |
| $\operatorname{Arg}_0$ | zero-amplitude convention: $\operatorname{Arg}_0(z)=\arg z$ ($z\neq0$), $0$ ($z=0$); makes $F_M$ global |
| $\varepsilon,g,\lambda$ | amplitude rate, coupling strength, synchronization strength |
| $k$ | **amplitude coefficient** (three-periodic); default $(1,\,1.22089647,\,6.35310346)$. Not a wavenumber |
| $F_M$ | $M$-ring map (6.1): $\varepsilon$-Mexican-hat + $g\Delta_M$ + harmonic-3 neighbour sync $S_M$ (via $\operatorname{Arg}_0$; identity when $\lambda=0$) |
| $\chi$ | chirality amplitude $\|\operatorname{Re}\Omega\times\operatorname{Im}\Omega\|$ of a reduced orbit |
| $T$ | realified deck generator (translation by 3) on $\mathbb R^{24}$ |
| $E_0,E_2,E_{13}$ | real deck projectors $\tfrac14(I+T+T^2+T^3)$, $\tfrac14(I-T+T^2-T^3)$, $I-E_0-E_2$; ranks $6,6,12$ |
| $U_0,U_2,U_{13}$ | $\operatorname{range}E_0$ (=realification of $V_3$, tangential), $\operatorname{range}E_2$, $\operatorname{range}E_{13}$; $\mathbb R^{24}=U_0\oplus U_2\oplus U_{13}$ |
| $\rho_\perp$ | normal Floquet multiplier (spectral radius of transverse monodromy over $U_2\oplus U_{13}$); per-step $\rho_\perp^{1/p}$ |
| $d_\perp(t)$ | transverse distance $\|(I-QQ^\ast)\Omega(t)\|$ |
| $g_\ast$ | fixed-branch transverse $-1$ crossing $0.4220744431784353$ (in $U_2$; canonical $k$, $\varepsilon{=}0.05$, $\lambda{=}0.001$) |

## Theorems and propositions

**Theorem 1 (pull-back of cycle Laplacians), all positive $M,d$.**
(i) $\Delta_M P=P\Delta_d\iff d\mid M$.
(ii) Invariance classification for $1\le d\le M$: $V_d=\operatorname{im}P$ is $\Delta_M$-invariant $\iff d\mid M$ or $(M,d)=(3,2)$. (For $d>M$, $V_d=\mathbb C^M$ trivially.)
(iii) For $d\mid M$: $Q^\ast Q=I_d$, $Q^\ast\Delta_M Q=\Delta_d$, $P^\ast\Delta_M P=q\Delta_d$ (compressed matrix integer; $Q$ not integer). $(12,3)$: $Q^\ast\Delta_{12}Q=L_3$.
(iv) $V_d=\operatorname{span}\{e_j:j\equiv0\ (q)\}$; modes $j'\mapsto qj'$; eigenvalues agree.
Graph-covering language for $d\ge3$ (darts for $d\le2$).

**Corollary (graph status of $12\to3$).** 4-sheeted covering, deck $\mathbb Z_4$; $C_3\cong C_{12}/\langle+3\rangle$; $C_3$ **not** a subgraph of $C_{12}$; $V_3=p^\ast\mathbb C^3$, $\Delta_{12}\!\restriction_{V_3}=L_3$.

**Fourier/symmetry.** $V_3=\operatorname{span}\{e_0,e_4,e_8\}$; spec $\{0,-3,-3\}$; complement (exact) $\{-2+\sqrt3\,(\times2),-1\,(\times2),-2\,(\times2),-2-\sqrt3\,(\times2),-4\}$; $V_3$ = deck-fixed space; $D_{12}$ acts on $V_3$ as $S_3$ (the $n\mapsto-n$ reflection induces $(1\;2)$; the $n\mapsto2-n$ reflection, fixing $(a,b,a)$, induces $(0\;2)$ — see §6.4). The one-step $C_{12}$ rotation induces the base $C_3$ rotation; the order-3 subgroup $\langle R^4\rangle$ also lifts the base rotation (no subgraph).

**Proposition 2 (exact nonlinear reduction), every $M=3q$.** With $k$ three-periodic and the $\operatorname{Arg}_0$ convention, $V_3$ is $F_M$-invariant and $F_M(P\Omega)=P F_3(\Omega)$. Key modular identity: $\{(n{-}1)\bmod3,(n{+}1)\bmod3\}=\mathbb Z_3\setminus\{n\bmod3\}$ for every $3\mid M$ (not special to 12). Simultaneous updates required. **Exact reduction: all $3\mid M$. Stability atlas: $M=12$ only.**

**Full real linearization decomposition ($M=12$).** $\mathbb R^{24}=U_0\oplus U_2\oplus U_{13}$ (dims $6,6,12$) via $E_0,E_2,E_{13}$; tangential block $U_0$ (realification of $V_3$), transverse restriction $U_2\oplus U_{13}$. Equivariance (not mere invariance) forbids normal/tangent mixing. The complex $\pm i$ characters are separate only after complexification; in the real Jacobian they combine into $U_{13}$.

**Linear vs nonlinear stability.** $\rho_\perp<1$ ⇒ normal variational dynamics exponentially asymptotically stable (linearly transversely stable). $\rho_\perp>1$ ⇒ linearly transversely unstable. $\rho_\perp=1$ ⇒ linear test inconclusive. No "iff"; avoid "contractive" (spectral radius $<1$ need not give Euclidean per-step contraction — the stable $g{=}0.2,\lambda{=}0.5$ orbit has $\rho_\perp=0.99130$ but Euclidean op-norm $1.03263>1$). Unit-multiplier example with algebraic attraction: $z^+=z(1-\varepsilon|z|^2)$.

**Representative regimes ($M=12$).** default fixed $\rho_\perp=0.9489$ stable; high-$\chi$ period-2 $0.9913$ stable; period-2 $1.1342$ unstable; period-8 $2.4167$ unstable; fixed $1.0942$ unstable; $g{=}\lambda{=}0$ neutral $1$ (inconclusive). $g_\ast=0.4220744432$ transverse $-1$ crossing in $U_2$. Atlas: coarse 190 (96 stable/40 unstable/1 neutral/53 unresolved); all 379 (150/132/1/96) — a sampled region, not an area fraction.

**Direct perturbation.** measured normal log-rates match prediction, e.g. $g{=}0.2,\lambda{=}0.001$: $-0.0524316131$ (measured) vs $-0.0524316123$ (predicted); $g{=}0.1,\lambda{=}0.3$: $+0.0629728673$ vs $+0.0629728672$. Stable regimes decay (negative rate); unstable depart.

**Corollary 3 (SUFFICIENT compatibility for $k$-only feedback).** If, with typed inputs (scalar $z$ with equal scalar read-outs on lifted states — **no $P$ applied to a scalar**; or $x\in\mathbb C^3$ with compatible lift), $k_{\mathrm{eff}}^{M}(P\Omega,\eta_M)=P k_{\mathrm{eff}}^3(\Omega,\eta_3)$ on $V_3$, then the reduction is preserved. **Sufficient, not iff.** Preservation of $V_3$ $\neq$ equality to a specified $F_3$ (a scalar using unnormalized $\|P\Omega\|=2\|\Omega\|$ preserves $V_3$ but changes the induced feedback). Compatibility bears on invariance only; transverse boundaries can move.

## Claim discipline (what this paper does NOT say)

- Not "nature uses 3–12–24 geometry"; not "explains quantum mechanics"; not "the three-node map was historically designed as a ring" (the ring is a 2026 construction); no physical scale/particle/spacetime/measured-phenomenon claim; no TORMENT/systems claim (§9 = shared algebra only).
- Exact reduction generalizes to every $3\mid M$; the stability atlas does **not** (it is $M=12$-specific).
- $V_3$ attraction is local/regional with explicit counterexamples; no global-basin, complete-bifurcation, or "iff" stability claim.
