# Cycle-Covering Dynamics of a Three-State Nonlinear Kernel


---

## Abstract

Working within the established framework of network quotients, graph fibrations, equitable partitions, and synchrony subspaces [SGP03, DL15, GR01], we study a specific discrete complex coupled-map model and make one embedding relationship exact. We study a three-state nonlinear oscillator map — a Mexican-hat amplitude nonlinearity coupled through the Laplacian of the triangle graph, followed by a harmonic-3 phase-synchronization step — and show that it arises as an **exact invariant reduction** of a larger periodic system on a cycle graph. The mechanism is a graph covering. We prove that for any divisor $d\mid M$ the residue map $p:C_M\to C_d$, $p(n)=n\bmod d$, induces a pull-back $P:\mathbb C^d\to\mathbb C^M$ that intertwines the cycle Laplacians ($\Delta_M P=P\Delta_d$), and that in fact $\Delta_M P=P\Delta_d\iff d\mid M$ for all positive $M,d$. On the pulled-back subspace $V_d=\operatorname{im}P$ the operator $\Delta_M$ **equals** $\Delta_d$ in the scaled residue-indicator basis (via the isometry $Q=P/\sqrt{M/d}$, $Q^\ast\Delta_M Q=\Delta_d$). We give the complete invariance classification: within $1\le d\le M$, $V_d$ is $\Delta_M$-invariant iff $d\mid M$ or $(M,d)=(3,2)$. Specializing to $(M,d)=(12,3)$ gives a four-sheeted graph covering with deck group $\mathbb Z_4$ and $\Delta_{12}\!\restriction_{V_3}=L_3$, the triangle Laplacian; $V_3=\operatorname{span}\{e_0,e_4,e_8\}$. We prove that a natural $M$-ring nonlinear extension with three-periodic coefficients satisfies $F_M(P\Omega)=P\,F_3(\Omega)$ **for every $M$ divisible by three**, under an explicit zero-amplitude phase convention; a numerical cross-check confirms the exact one-step identity to floating-point rounding, independently reproduced, while long trajectories in unrestricted regimes are shown *not* to remain machine-close despite the exact algebra. Linearizing transverse to $V_3$ (for $M=12$) via the real deck-character decomposition $\mathbb R^{24}=U_0\oplus U_2\oplus U_{13}$, we exhibit linearly stable and unstable fixed and periodic regimes with their normal Floquet multipliers; direct nonlinear perturbation experiments confirm the predicted normal decay and growth rates in representative regimes. We record the exact-algebra coincidence with a second, independently defined ring operator, and a **sufficient** compatibility condition under which a $k$-only scalar feedback preserves the reduction. Strongest conclusion: **for every $M$ divisible by three the specified three-state nonlinear map admits an exact invariant pull-back realization on the $M$-cycle; for the $M=12$ realization studied numerically the invariant sector exhibits linearly stable and unstable transverse regimes, with direct perturbations confirming transverse attraction in representative linearly stable regimes.** The reduction machinery is standard network-quotient / synchrony-subspace theory; the contribution is the specific model together with its explicit deck-resolved transverse-stability atlas (§1.4). No novelty or priority is claimed.

**Keywords:** cycle graph, graph covering, discrete Laplacian, invariant subspace, pull-back, deck group, normal Floquet multiplier, nonlinear map reduction.

---

## 1. Introduction

A recurring situation in coupled-oscillator networks is that a small, symmetric subsystem behaves as though embedded in a larger, more regular one. This paper makes one such relationship exact. We begin from a concrete three-state map $F_3:\mathbb C^3\to\mathbb C^3$,
$$
F_3(\Omega)=S_3\!\Big(\Omega+\varepsilon\,\Omega\odot(k-|\Omega|^2)+g\,L_3\Omega\Big),
\qquad
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},
$$
where $\odot$ is entrywise multiplication, $|\Omega|^2$ is entrywise, $k\in\mathbb R^3$ is a fixed **amplitude coefficient** triple (no wavenumber or physical meaning is assigned to it), $\varepsilon,g\in\mathbb R$, and $S_3$ is the phase-only synchronization operator (defined precisely in §6.1 via the zero-amplitude convention below),
$$
\phi_j\ \mapsto\ \phi_j+\lambda\!\!\sum_{i\neq j}\sin\!\big(3(\phi_i-\phi_j)\big),\qquad \Omega_j=r_j e^{i\phi_j},
$$
which leaves each amplitude $r_j$ unchanged. The matrix $L_3$ is simultaneously the Laplacian of the triangle graph $C_3$ and of the complete graph $K_3$ (they coincide on three vertices); its spectrum is $\{0,-3,-3\}$ in the sign convention $(\Delta_M f)(n)=f(n{+}1)+f(n{-}1)-2f(n)$ used throughout.

The central question is structural: **is $F_3$ the shadow of a system on a larger, more uniform graph?** We answer yes, with $C_M$ (any $M$ divisible by three) as the larger graph, and we make "shadow" precise as a graph covering together with the pull-back of functions along it. The $M=12$ realization is then studied numerically for transverse stability.

Contributions:

1. The **pull-back intertwining theorem** for cycle Laplacians (§3): $\Delta_M P=P\Delta_d\iff d\mid M$ (all positive $M,d$), and $Q^\ast\Delta_M Q=\Delta_d$; with the complete invariance classification of $V_d=\operatorname{im}P$.
2. The precise **graph-theoretic status** of the $12\to3$ relationship (§4): a four-sheeted covering, deck group $\mathbb Z_4$, quotient $C_{12}/\langle n\mapsto n{+}3\rangle\cong C_3$ — not a subgraph inclusion.
3. The **Fourier and symmetry decomposition** (§5): $V_3=\operatorname{span}\{e_0,e_4,e_8\}$, exact complement spectrum, and the image of the $C_{12}$ dihedral action as the $S_3$ symmetry of $L_3$.
4. A **nonlinear extension** (§6) proved to satisfy $F_M(P\Omega)=P F_3(\Omega)$ for every $M=3q$, with an explicit zero-amplitude convention, verified numerically and independently reproduced.
5. A **transverse-stability analysis** (§7, $M=12$) using the real deck decomposition, distinguishing linear spectral stability from nonlinear attraction, with representative regimes and (§8) a **direct perturbation experiment** confirming the linear prediction.
6. Two structural addenda: the **exact-algebra coincidence** with a second ring operator (§9) and a **sufficient feedback-compatibility** condition (§10).

Sections 3–5 are elementary and self-contained. Sections 6–8 mix proved invariance with carefully delimited numerical fact. Scope is deliberately conservative: the ring extension is a construction of this paper, and transverse attraction is local and regional, not global (§12).

### 1.2 Established frameworks (background)

The constructions below are standard in network dynamics, and we cite them as background rather than as new results. The invariant sector $V_3$ is a **synchrony subspace** (polydiagonal) of a **balanced / equitable partition** of the cycle [SGP03, GST05, GS06]; the reduction $C_M\to C_3$ is a **graph covering**, equivalently a surjective **graph fibration** [BV02, DL15, NRS16]; the Laplacian identity of Theorem 1 is the **equitable-partition / quotient-(divisor-)matrix identity** of algebraic graph theory [GR01, OYSB13]; and the transverse-stability analysis of §7 uses the **master-stability** framework [PC98] with the symmetry-adapted (irreducible-representation) cluster decomposition of [Pecora14, Sorrentino16]. For the specific regular cycle covers considered here these descriptions coincide: covering $\equiv$ surjective fibration $\equiv$ balanced-coloring quotient $\equiv$ equitable-partition quotient (a synthesis of the groupoid / fibration / balanced-coloring pictures is [GFBC24]). Accordingly the **divisor-case quotient construction** in Theorem 1 (§3) is a cycle specialization of the standard equitable-partition and network-quotient framework [GR01, OYSB13, SGP03, DL15]; the exact converse ($\Delta_M P=P\Delta_d\Rightarrow d\mid M$) and the invariance classification (including the exceptional $(3,2)$ case) are **calculated here**, and no novelty or priority is claimed. The Fourier / deck spectral decomposition of §5 is standard lift / quotient spectral theory [GR01, DF19].

### 1.3 Relation to prior work

- **Network quotients and synchrony subspaces.** The subspace $V_3=\{x:x_n=x_{n+3}\}$ is the polydiagonal of the balanced equivalence relation grouping the $M$ ring sites into three residue classes. Balanced synchrony and quotient dynamics are established for admissible vector fields [SGP03, GST05, GS06], with an explicit smooth-network-map formulation in [NRS16]. The $V_3$ used here is one such synchrony subspace; Proposition 2 verifies compatibility for the particular composed map considered here.
- **Graph fibrations.** The residue map $p:C_M\to C_3$ is a surjective graph fibration [BV02], and a fibration relates the network dynamics on total and base graph [DL15, NRS16]. Here the pull-back $P:\mathbb C^3\to V_3\subset\mathbb C^M$ is a linear **bijection from the base space onto $V_3$**, so the intertwining $F_M\circ P=P\circ F_3$ (Proposition 2) **identifies the base dynamics $F_3$ with the restriction $F_M\!\restriction_{V_3}$**. We state it this way, rather than as a loose "conjugacy," because $P$ is a bijection onto the invariant sector but not onto all of $\mathbb C^M$; the identification is of $F_3$ with $F_M$ restricted to $V_3$.
- **Equitable partitions and quotient Laplacians.** The residue partition is equitable; $Q^\ast\Delta_M Q=\Delta_3$ (Theorem 1(iii)) is the quotient-(divisor-)matrix identity, and the eigenvalue inheritance (Theorem 1(iv)) is the standard fact that quotient-matrix eigenvalues form a sub-multiset of the graph's [GR01, OYSB13, Schaub16].
- **Transverse stability.** The tangential / transverse split $U_0\oplus(U_2\oplus U_{13})$ and the block-diagonalization of the normal variational dynamics by deck characters (§7) are the abelian ($\mathbb Z_4$) case of the symmetry-adapted / IRR cluster decomposition [Pecora14, Sorrentino16], built on the master-stability framework [PC98]. Cluster variational stability is treated in [Sorrentino16], and general normal stability including periodic orbits in [ABS96]; the periodic-orbit Floquet calculations below are carried out for this map.

### 1.4 Contribution (what is model-specific)

Given the background above, the contribution is the specific worked instance, not the reduction machinery. The following are model-specific:

1. **The map itself** — a discrete complex state $\Omega\in\mathbb C^M$ combining a Mexican-hat amplitude nonlinearity $\varepsilon\Omega\odot(k-|\Omega|^2)$, cycle-Laplacian coupling $g\Delta_M\Omega$, and a *separate* harmonic-3 phase-synchronization step with three-periodic $k$. We did not locate a near-identical model in a focused literature search (§6.5).
2. **The explicit all-$3\mid M$ reduction** for this coupling, written out with the zero-amplitude convention (§6), and the one-step numerical cross-check.
3. **The deck-resolved transverse-stability atlas** of the $M=12$ realization (§7–§8): the specific stable / unstable fixed and periodic regimes, the crossing $g_\ast=0.4220744431784353$, the specific normal Floquet values, and the direct-perturbation confirmation.
4. **The linear-vs-nonlinear stability delimitation** for this map (§7.2), with the explicit algebraic-decay and transient-growth counterexamples.
5. **The shared-$L_3$-sector observation** relating the map to a second $\Delta_{12}$-based ("RSB") operator (§9), as a statement of shared quotient / equitable-partition algebra only.
6. **The $k$-only feedback compatibility criterion** (§10), a sufficient pull-back condition specialized to this architecture.

These are what a specific worked example contributes. We make **no claim of novelty, priority, or a new theorem or mechanism**: every construction above has a standard home in the cited literature, and the model-specific items are computations and constructions *of this model* rather than new general theory (see §12 and `PAPER_A_LITERATURE_CONTEXT_v0.1.md`).

## 2. Cycle graphs and pull-back spaces

Fix $M\ge1$. Let $C_M$ be the cycle graph on $\mathbb Z_M=\{0,\dots,M-1\}$, edges $\{n,n{+}1\}$ (mod $M$); $C_2$ is the doubled edge and $C_1$ a single loop (a dart/incidence description for these degenerate sizes is given in §4.3). The **cycle Laplacian** $(\Delta_M f)(n)=f(n{+}1)+f(n{-}1)-2f(n)$ is real symmetric circulant; note $\Delta_1=(0)$ and $\Delta_2=\begin{psmallmatrix}-2&2\\2&-2\end{psmallmatrix}$ are the degenerate cases, and the generic first row $(-2,1,0,\dots,0,1)$ describes $\Delta_M$ for $M\ge3$. Its eigenvectors are the Fourier modes $e_j(n)=e^{2\pi ijn/M}$, $j\in\mathbb Z_M$, with
$$
\Delta_M e_j=-4\sin^2\!\big(\pi j/M\big)\,e_j .
\tag{2.1}
$$
In particular $\Delta_3=L_3$ with spectrum $\{0,-3,-3\}$.

**Pull-back for all positive $M,d$.** Define $P:\mathbb C^d\to\mathbb C^M$ by
$$
(Pu)_n=u_{\,n\bmod d},\qquad V_d:=\operatorname{im}P ,
$$
i.e. the $M\times d$ $\{0,1\}$-matrix with $P_{n,\,n\bmod d}=1$. **We do not identify $V_d$ with $\{f:f(n{+}d)=f(n)\}$ outside the divisor case:** for $1\le d\le M$, those two spaces coincide iff $d\mid M$; no shift-fixed characterization is asserted here for $d>M$. (Within $1\le d\le M$: the shift-fixed space has dimension $\gcd(M,d)$ and is always $\Delta_M$-invariant, whereas $\operatorname{im}P$ has dimension $\min(M,d)$ and need not be; e.g. at $(M,d)=(5,3)$, $\operatorname{im}P$ has dimension 3 and is not invariant while $\{f(n{+}3)=f(n)\}$ has dimension 1 and is invariant. The unrestricted "only when $d\mid M$" wording is avoided because it fails for $d>M$ — e.g. $(M,d)=(2,4)$, where $\operatorname{im}P=\mathbb C^2$ and the wrap-by-4 shift is the identity on $\mathbb C^2$, so both spaces are $\mathbb C^2$ although $4\nmid2$.) For $d\mid M$, $q=M/d$, distinct columns of $P$ are orthogonal indicators of the $d$ residue classes, each of squared norm $q$, so
$$
P^\ast P=q\,I_d,\qquad Q:=P/\sqrt q\ \text{ satisfies }\ Q^\ast Q=I_d ,
\tag{2.2}
$$
$Q$ an isometry onto $V_d$ and $QQ^\ast$ the orthogonal projector onto $V_d$. (Here $Q^\ast$ denotes the Hermitian adjoint; $Q$ is real, so $Q^\ast=Q^\top$ — we write $Q^\ast$ to signal the complex inner product.) The pull-back scales norm by
$$
\|P\Omega\|=\sqrt{M/d}\;\|\Omega\|,\qquad\text{in particular }\ \|P\Omega\|=2\|\Omega\|\ \text{ for }(M,d)=(12,3).
\tag{2.3}
$$

## 3. Covering theorem for periodic Laplacians

> **Theorem 1 (pull-back of cycle Laplacians).** Let $M,d\ge1$ and $P,V_d$ as in §2.
>
> **(i) Intertwining.** $\Delta_M P=P\Delta_d\iff d\mid M$ (for all positive $M,d$).
>
> **(ii) Invariance classification (range $1\le d\le M$).** $V_d$ is $\Delta_M$-invariant $\iff d\mid M$ or $(M,d)=(3,2)$. (For $d>M$, $P$ has rank $M$, so $V_d=\mathbb C^M$ is trivially invariant, though $P$ is not an isometric embedding and the intertwining still fails unless $d\mid M$.)
>
> **(iii) Restriction is $\Delta_d$, not merely similar to it.** For $d\mid M$, $Q^\ast Q=I_d$ and $Q^\ast\Delta_M Q=\Delta_d$; the compressed integer form is $P^\ast\Delta_M P=q\,\Delta_d$. For $(M,d)=(12,3)$: $Q^\ast\Delta_{12}Q=L_3$ and $P^\ast\Delta_{12}P=4L_3$. ($Q$ itself is not integer; the *compressed* matrix is.)
>
> **(iv) Fourier form.** For $d\mid M$, $V_d=\operatorname{span}\{e_j: j\equiv0\ (\mathrm{mod}\ q)\}$; pull-back sends the $\mathbb Z_d$ mode $j'$ to the $\mathbb Z_M$ mode $qj'$; eigenvalues agree since $-4\sin^2(\pi qj'/M)=-4\sin^2(\pi j'/d)$.
>
> The linear-algebra statements (i), (iii), (iv) hold for **all positive sizes**, including $d\in\{1,2\}$; the graph-covering language of §4 is stated for $d\ge3$ (or via darts, §4.3).

**Background.** The **divisor-case quotient construction** in Theorem 1 — the forward intertwining $\Delta_M P=P\Delta_d$ for $d\mid M$ and the compression $Q^\ast\Delta_M Q=\Delta_d$ — is a cycle specialization of the standard equitable-partition and network-quotient framework [GR01, OYSB13, SGP03, DL15]. The **exact converse** ($\Delta_M P=P\Delta_d\Rightarrow d\mid M$) and the **invariance classification** (invariant $\iff d\mid M$ or $(M,d)=(3,2)$) are calculated here: the literature supports the forward quotient machinery, not necessarily the complete iff converse plus the exceptional $(3,2)$ classification, and no novelty or priority is claimed. The statement is given with a self-contained proof to fix notation and to make the exact integer form $P^\ast\Delta_M P=q\Delta_d$ explicit. The incidence argument below is the equitable-partition (balanced-coloring) verification made concrete for cycles.

**Proof of (i) — equitable-partition / incidence argument.** Attach to each vertex $n$ two directed incidences, toward $n{+}1$ and toward $n{-}1$, retained even when endpoints coincide. Suppose $d\mid M$. Partition vertices by residue mod $d$; every vertex in class $a$ has incidence destinations $a{+}1$ and $a{-}1$ (mod $d$). Hence for the residue-indicator columns of $P$ the aggregate adjacency row is independent of the representative $n$ and equals the corresponding row of the $d$-cycle adjacency (with multiplicity); subtracting $2I$ gives $\Delta_M P=P\Delta_d$. Conversely, if $d\nmid M$ write $r=M\bmod d$, $1\le r\le d-1$; comparing row $0$ of $\Delta_M P$ and $P\Delta_d$ leaves the nonzero functional $u_{r-1}-u_{d-1}$ (choose $u$ supported at $d-1$), so the identity fails. For $d>M$ pick $u$ supported at the unseen coordinate $M$: $Pu=0$ while $P\Delta_d u\neq0$. Hence $\Delta_M P=P\Delta_d\iff d\mid M$. $\qquad\blacksquare$

**Proof of (ii) — analytic converse (boundary-row cases).** Divisor pairs: $V_d=\operatorname{im}P$ is invariant by (i) ($\Delta_M P=P\Delta_d$ gives $\Delta_M\operatorname{im}P\subseteq\operatorname{im}P$). $d>M$: $\operatorname{rank}P=M$ so $V_d=\mathbb C^M$. Conversely, if $1\le d\le M$ and $d\nmid M$ (so $d\ge2$), write $r=M\bmod d\in[1,d-1]$; compare the two same-fibre vertices $0$ and $d$.
- If $M\ge d+2$, vertex $d$ is interior, and $(\Delta_M Pu)_0=u_1+u_{r-1}-2u_0$ while $(\Delta_M Pu)_d=u_1+u_{d-1}-2u_0$. Since $r-1\neq d-1$ these differ; choosing $u$ supported at $d-1$ gives unequal values on one fibre, so $\Delta_M Pu\notin\operatorname{im}P$: **not invariant.**
- If $M=d+1$, both $0,d$ are at the wrap; the rows become $-u_0+u_1$ and $-u_0+u_{d-1}$, equal for all $u$ iff $d=2$, i.e. $(M,d)=(3,2)$, where directly $\Delta_3(a,b,a)=(b{-}a,\,2a{-}2b,\,b{-}a)\in\operatorname{im}P$: **invariant.** For $d>2$ pick $u_1\neq u_{d-1}$: not invariant.

These exhaust $1\le d\le M$, giving invariance $\iff d\mid M$ or $(M,d)=(3,2)$. At $(3,2)$ the induced operator in $(a,b)$ coordinates is $\begin{psmallmatrix}-1&1\\2&-2\end{psmallmatrix}\neq\Delta_2$, consistent with the intertwining failing there. $\qquad\blacksquare$

**Proof of (iii)–(iv).** From (i), $\Delta_M Q=Q\Delta_d$; left-multiplying by $Q^\ast$ and using (2.2) gives $Q^\ast\Delta_M Q=\Delta_d$, an equality of $d\times d$ matrices with the integer entries of $\Delta_d$ (equivalently $P^\ast\Delta_M P=q\Delta_d$). For (iv), $P e^{(d)}_{j'}(n)=e^{2\pi ij'(n\bmod d)/d}=e^{2\pi i(qj')n/M}=e^{(M)}_{qj'}(n)$, so $P$ carries $\mathbb Z_d$-modes onto $\mathbb Z_M$-modes indexed in $q\mathbb Z_M$, with equal eigenvalues by (2.1). $\qquad\blacksquare$

These statements are analytic. A finite regression check (`paperA_proof_audit_v0_2.py`) corroborates them: the intertwining holds with exact zero error for all divisor pairs $M\le90$; it fails for every non-divisor $\le60$; the invariance classification via the correct test $(I-PP^{+})\Delta_M P=0$ matches "$d\mid M$ or $(3,2)$" over $1\le d\le M\le40$ with no mismatch; $Q^\ast Q=I_3$, $Q^\ast\Delta_{12}Q=L_3$, $P^\ast\Delta_{12}P=4L_3$, and $\|P\Omega\|=2\|\Omega\|$ hold exactly. Regression evidence corroborates; it does not replace the proofs above.

## 4. The $C_{12}\to C_3$ reduction

### 4.1 The covering
Specialize $(M,d)=(12,3)$, $q=4$. The residue map $p:C_{12}\to C_3$, $p(n)=n\bmod3$, is a **graph covering**: it is a homomorphism, and it is bijective on the open neighbourhood $N(n)=\{n{-}1,n{+}1\}$ of every vertex (the two neighbours map to the two residues $\neq p(n)$). Each fibre $p^{-1}(r)=\{r,r{+}3,r{+}6,r{+}9\}$ has four vertices: **four sheets.**

### 4.2 Deck group and quotient
Every automorphism of $C_{12}$ is $n\mapsto n{+}a$ or $n\mapsto a{-}n$. The rotations with $p\circ\tau=p$ are exactly $a\in\{0,3,6,9\}$; a reflection would need $a-n\equiv n\ (3)$ for all $n$, impossible ($n=0$ forces $a\equiv0$, then $n=1$ needs $-1\equiv1\ (3)$). Hence
$$
\mathrm{Deck}(p)=\langle n\mapsto n{+}3\rangle=\{0,3,6,9\}\cong\mathbb Z_4 ,
$$
acting transitively on each fibre (regular covering), so $C_3\cong C_{12}/\langle n\mapsto n{+}3\rangle$, quotient edges $\{01,12,20\}=K_3=C_3$.

| Statement | Truth | Reason |
|---|---|---|
| $C_3$ **subgraph** of $C_{12}$ | **FALSE** | $C_{12}$ has girth 12; adjacency cube has zero trace (no closed 3-walks) |
| $C_3$ **quotient** of $C_{12}$ | **TRUE** | $C_{12}/\langle+3\rangle=K_3=C_3$ |
| $C_{12}$ **covers** $C_3$ | **TRUE** | 4-sheeted covering; deck group $\mathbb Z_4$ |
| $C_3$-dynamics on an **invariant subspace** of $\mathbb C^{12}$ | **TRUE** | $V_3=p^\ast\mathbb C^3=\operatorname{im}P$, invariant by Theorem 1 |

Compound statement: **$C_{12}\xrightarrow{4:1}C_3$ is a covering, and $\mathbb C^{12}\supseteq V_3=p^\ast\mathbb C^3$ carries $\Delta_{12}\!\restriction_{V_3}=L_3$.**

**Terminology crosswalk.** For a regular cover of an undirected cycle the following describe the *same* object and coincide for the specific regular cycle covers considered here: a **graph covering** (4-sheeted, deck group $\mathbb Z_4$), a surjective **graph fibration** [BV02, DL15, NRS16], a **balanced-coloring / synchrony-subspace quotient** [SGP03, GST05, GS06], and an **equitable-partition / quotient-(divisor-)matrix** reduction [GR01, OYSB13]. A synthesis tying groupoids, fibrations, and balanced colorings together is [GFBC24]. We take "covering" as the primary term and cite any of these frameworks interchangeably below; the equivalence is specific to this regular-cycle setting and is not claimed in general.

### 4.3 Degenerate sizes (darts)
The graph-covering language above uses ordinary open neighbourhoods and is valid for $d\ge3$; in particular $C_{12}\to C_3$ is an ordinary simple-graph covering with no qualification. For $C_1$ (loop) and $C_2$ (doubled edge) one uses a dart/incidence description: darts $(n,+),(n,-)$ with reversal $(n,+)\leftrightarrow(n{+}1,-)$, and dart map $(n,\pm)\mapsto(n\bmod d,\pm)$; for $d\mid M$ this respects reversal and is bijective on the two darts at each vertex, giving a multigraph covering. The linear-algebra theorem (§3) does not depend on adopting graph terminology at these degenerate sizes.

## 5. Fourier and symmetry decomposition

**Background.** The spectral splitting below is standard covering-graph / lift spectral theory. In general a regular cover's spectrum decomposes over the **irreducible representations** of the deck group; for the **abelian** regular cover considered here ($\mathbb Z_4$) those representations are one-dimensional characters $e^{\pi i j/2}$, so the deck-fixed modes span the pull-back sector and inherit the base eigenvalues [GR01, DF19]. The explicit $C_{12}$ values are worked out here for completeness.

By Theorem 1(iv) with $q=4$,
$$
V_3=\operatorname{span}\{e_0,e_4,e_8\},\qquad
\operatorname{spec}\big(\Delta_{12}\!\restriction_{V_3}\big)=\{0,-3,-3\}=\operatorname{spec}L_3 .
$$
These are exactly the deck-fixed modes: $e_j(n{+}3)=e^{\pi ij/2}e_j(n)$, and $e^{\pi ij/2}=1\iff j\in\{0,4,8\}$. The orthogonal complement carries the **exact** spectrum
$$
\{\,-2+\sqrt3\ (\times2),\ -1\ (\times2),\ -2\ (\times2),\ -2-\sqrt3\ (\times2),\ -4\ (\times1)\,\},
$$
(the values $-4\sin^2(\pi j/12)$ for $j\in\{1,2,3,5,6,7,9,10,11\}$; the smallest-magnitude value is exactly $-2+\sqrt3$, not the rounded $-0.268$).

**Symmetry.** $\Delta_{12}$ commutes with the dihedral group $D_{12}$ of order $24$ (rotation $n\mapsto n{+}1$, reflection $n\mapsto-n$). Restricted to $V_3$ these act as the symmetries of $L_3$: the rotation induces the cyclic $3$-permutation of $C_3$, the reflection $n\mapsto-n$ induces the transposition $(1\;2)$ on residues $0,1,2$ (it sends $(0,1,2)\mapsto(0,2,1)$; the *different* reflection $n\mapsto2-n$, which fixes vectors $(a,b,a)$, induces $(0\;2)$ — see §6.4), and complex conjugation preserves $V_3$ while swapping $e_4\leftrightarrow e_8$ (an antilinear operation on the complex function space, not a deck transformation). The image of $D_{12}$ on $V_3$ is the full $S_3\cong D_3$ that stabilizes $L_3$; the kernel of the quotient action is the four-element deck group.

The one-step $C_{12}$ rotation induces the one-step base $C_3$ rotation under the quotient. Separately, the order-three subgroup generated by $R^4$ (rotation by $4$) maps isomorphically onto the base cyclic rotation ($p(n{+}4)=p(n){+}1$), giving a subgroup lift of the same cyclic action; together with a reflection it realizes a $D_3$ subgroup with the same image. None of this makes $C_3$ a subgraph of $C_{12}$ (§4).

## 6. Nonlinear extension for every $M$ divisible by three

### 6.1 The ring map, with an explicit zero-amplitude convention

Adopt the site-independent, deterministic phase convention
$$
\operatorname{Arg}_0(z)=\begin{cases}\arg z,& z\neq0,\\[2pt]0,& z=0,\end{cases}
\tag{6.0}
$$
and define the **$M$-ring map** $F_M:\mathbb C^M\to\mathbb C^M$ by
$$
\Omega\ \longmapsto\ \tilde\Omega=\Omega+\varepsilon\,\Omega\odot(k-|\Omega|^2)+g\,\Delta_M\Omega,
\tag{6.1a}
$$
$$
\big(F_M\Omega\big)_n=\tilde r_n\,\exp\!\Big(i\big[\operatorname{Arg}_0(\tilde\Omega_n)+\lambda\!\!\sum_{m\sim n}\!\sin 3\big(\operatorname{Arg}_0(\tilde\Omega_m)-\operatorname{Arg}_0(\tilde\Omega_n)\big)\big]\Big),
\tag{6.1b}
$$
where $\tilde r_n=|\tilde\Omega_n|$, $m\sim n$ ranges over the two ring neighbours $\{n{-}1,n{+}1\}$, and $k\in\mathbb R^M$ is **three-periodic** ($k_{n+3}=k_n$). When $\lambda=0$, $S_M$ is defined directly as the identity (no phase is invoked). The synchronization changes phases only and preserves every amplitude.

Consequences of (6.0), stated explicitly:
- $F_M$ is **globally defined** on $\mathbb C^M$.
- For $\lambda\neq0$ the extension is **generally discontinuous** at states with zero pre-synchronization components (a vanishing $\tilde\Omega_n$ has no genuine phase, yet its assigned value $0$ enters neighbours' updates; e.g. $\tilde v_\delta=(\delta e^{i\alpha},1,1)$ has, as $\delta\to0$, a nonzero neighbour tending to $e^{i\lambda\sin3\alpha}$, whose limit depends on $\alpha$). $\operatorname{Arg}_0$ is a *mathematical* convention distinct from IEEE signed-zero behaviour in floating point.
- The **exact pull-back identity (Prop. 2) still holds**, because the same deterministic convention is applied at corresponding residue copies.
- **Jacobian/Floquet statements are restricted to orbits whose pre-synchronization components are all nonzero.** Every representative orbit used in §7–§8 satisfies this comfortably (minimum pre-sync amplitude $>0.948$).

For $M=3$ the two neighbours $\{n{-}1,n{+}1\}$ of any node are the two other nodes, so $S_3$ is the all-pairs synchronization of §1 and $F_3$ is the reference three-node map.

**Background (coupling family).** The phase term $\sin 3(\phi_i-\phi_j)$ is a higher-harmonic phase coupling. Higher-harmonic coupling occurs in phase-oscillator clustering studies [HMM93], with symmetry-based phase-locking context in [AS92]. Here the three residue classes are the network partition whose invariance is verified in Proposition 2; we do not derive the cluster count from those citations, which concern specific (first / second) harmonics rather than a general all-$m$ theorem. This places the *coupling family* only; it is not itself novel, and it is not a claim about the specific combined map, whose closest dynamical neighbours are discussed in §6.5.

### 6.2 Exact reduction for all $M=3q$

> **Proposition 2.** Let $M=3q$, $q\ge1$, and $k$ three-periodic. With the convention (6.0),
> $$
> F_M(P\Omega)=P\,F_3(\Omega)\qquad\text{for all }\Omega\in\mathbb C^3,
> $$
> so $V_3\subset\mathbb C^M$ is $F_M$-invariant and $F_M\!\restriction_{V_3}\cong F_3$.

**Proof.** Let $f=P\Omega\in V_3$. *Pointwise term:* $k=Pk^{(3)}$ and entrywise operations act residue-classwise on pulled-back vectors, so $\varepsilon f\odot(k-|f|^2)=P\big(\varepsilon\Omega\odot(k^{(3)}-|\Omega|^2)\big)$. *Coupling:* $g\Delta_M(P\Omega)=P(g\Delta_3\Omega)=P(gL_3\Omega)$ by Theorem 1(i). Hence $\tilde f=P\tilde\Omega\in V_3$ with $\tilde\Omega=\Omega+\varepsilon\Omega\odot(k^{(3)}-|\Omega|^2)+gL_3\Omega$. *Synchronization:* $\tilde f\in V_3$, and for every $n$ (including the wrap), divisibility gives the modular identity
$$
\{((n{-}1)\bmod M)\bmod3,\ ((n{+}1)\bmod M)\bmod3\}=\mathbb Z_3\setminus\{n\bmod3\}.
\tag{6.2}
$$
So the two ring-neighbour contributions equal the two all-other-node contributions of $S_3$ evaluated at residue $n\bmod3$. All increments use the single pre-synchronization vector $\tilde f$ (a **simultaneous**, not sequential, update), and amplitudes are restored unchanged; hence $F_M(P\Omega)=P F_3(\Omega)$. At any zero pre-sync component the common convention (6.0) is applied identically at all copies of the residue, preserving the identity. $\qquad\blacksquare$

**Background.** Balanced synchrony and quotient dynamics are established for admissible vector fields [SGP03, GST05, GS06], and explicitly for smooth network maps in [NRS16]; graph-fibration semiconjugacy is the continuous-time background [DL15]. Proposition 2 verifies the corresponding compatibility for this composed update, including the shared zero-amplitude convention (6.0) — whose discontinuous-at-zero $\operatorname{Arg}_0$ handling is proved here, not inherited from those sources. The model-specific ingredient is the elementary verification that the harmonic-3 neighbour term is admissible for this ring — the neighbour-residue identity (6.2), the local-bijectivity / balance condition made explicit. As in §1.3, $P$ is a bijection onto $V_3$, so the identity says $F_3$ equals $F_M\!\restriction_{V_3}$; we avoid the looser word "conjugacy."

The modular identity (6.2) holds for **every** $M$ divisible by three, $M=3$ included — there is nothing special about $M=12$ (contrary to a claim in an earlier draft). The argument uses simultaneous updates; a sequential/in-place phase sweep, using already-modified neighbours, defines a different map to which it does not apply. The reference synchronization is simultaneous (all pairwise differences are formed from one phase vector), so it matches.

**Two distinct scopes, to be kept separate:**
- **Exact invariance / reduction:** every $M$ divisible by three.
- **Transverse-stability atlas (§7–§8):** $M=12$ only. Larger rings have different transverse modes and are not studied here.

### 6.3 Numerical cross-check (one-step identity, and a long-trajectory caveat)

The reference $F_3$ is a specific implementation, so we confirm the reduction against it. Independent checks (referee reproduction, direct cyclic matrices, simultaneous phase updates, source loaded only after re-derivation):

| test | error measure | value |
|---|---|---|
| one-step $F_{12}(P\Omega)$ vs lifted reference, 50 runs (seeds 3,17,101,2026,8675309) | max per-component | $5.53\times10^{-15}$ |
| free 600-step trajectories, defaults, 5 seeds | max per-component | $2.13\times10^{-15}$ |
| free 600-step trajectories, $(g,\lambda)=(0.2,0.5)$, 5 seeds | max per-component | $3.82\times10^{-15}$ |
| one-step generalization, $M=3,6,9,\dots,30,63$ | max per-component | $2.61\times10^{-16}$ |
| free 600-step over **all** random parameter cases | max per-component | $4.94$; Euclidean max $11.09$ |

The error measure is the maximum per-component (infinity-norm) discrepancy, **not** a Euclidean norm. The last row is stated deliberately: **an exact one-step algebraic identity does not guarantee indefinitely close floating-point trajectories in unrestricted dynamical regimes** — tiny implementation-order differences are amplified in sensitive parameter regions (the worst case here is $g\approx0.0076,\lambda\approx0.637$, whose one-step discrepancy is nonetheless bounded by the first row). This forward divergence is a numerical-analysis caveat, not a refutation of the exact algebra; the selected default and high-$\lambda$ regimes do reproduce closely. The read-only import of the reference map wrote no bytecode to the source tree.

### 6.4 The exceptional $(M,d)=(3,2)$ case

Theorem 1(ii) admits one non-divisor invariant image: $(3,2)$. Here $2\nmid3$, so $p(n)=n\bmod2$ is **not** a covering, and $V_2=\operatorname{im}P=\{(a,b,a)\}$ is not a pulled-back $C_2$-sector; it is nonetheless the fixed space of the node reflection $n\mapsto2-n$ (the transposition $(0\;2)$, which fixes vectors $(a,b,a)$; distinct from the $n\mapsto-n$ reflection of §5, which is $(1\;2)$) of $L_3$, and $L_3$-invariant for that symmetry reason. This illustrates that **invariant subspaces of $\Delta_M$ can arise from symmetry without a covering**; only the $d\mid M$ subspaces are the pull-back sectors of Theorem 1. The induced operator there is $\begin{psmallmatrix}-1&1\\2&-2\end{psmallmatrix}\neq\Delta_2$, consistent with intertwining failing.

### 6.5 Closest dynamical neighbours (context)

The genre of the full map is a **complex coupled map with cluster states**. The nearest cited neighbours are Kaneko's globally coupled maps [Kaneko90] (discrete-time cluster states, but with real logistic maps rather than a complex Mexican-hat amplitude step plus a *separate* harmonic-3 phase synchronization), and the discrete-time network-map framework [NRS16]; Stuart–Landau / Ginzburg–Landau ring models are a continuous-time relative of the amplitude part. **We did not locate a near-identical model in the focused literature search** — the particular combination of a complex Mexican-hat amplitude nonlinearity, cycle-Laplacian coupling, and a separate harmonic-3 phase step was not found as a studied model. We record this as an *unresolved* novelty status, not a novelty claim (§12; `PAPER_A_LITERATURE_CONTEXT_v0.1.md`).

## 7. Transverse stability ($M=12$)

We ask whether $V_3$ is not merely invariant but attracting for $M=12$: do nearby twelve-dimensional states collapse onto the reduced sector?

### 7.1 Real deck-character block structure

Over $\mathbb R$ (identify $\mathbb C^{12}\cong\mathbb R^{24}$), let $T$ be the realified deck generator (translation by three). At a nonsingular on-sector point $x$ ($Tx=x$), differentiating the deck **equivariance** $F_{12}(Tx)=TF_{12}(x)$ gives $DF_{12}(x)\,T=T\,DF_{12}(x)$; equivariance (not mere invariance of $V_3$) is what forbids normal-to-tangent mixing. Define the real orthogonal projectors
$$
E_0=\tfrac14(I+T+T^2+T^3),\quad
E_2=\tfrac14(I-T+T^2-T^3),\quad
E_{13}=I-E_0-E_2,
$$
with ranks $6,6,12$, giving
$$
\mathbb R^{24}=U_0\oplus U_2\oplus U_{13},\qquad U_0=\operatorname{range}E_0=\text{realification of }V_3 .
$$
$U_0$ is **tangential** (reproduces the three-node dynamics); $U_2\oplus U_{13}$ is the 18-dimensional **transverse** (normal) space whose real Jacobian block decides transverse stability. Over $\mathbb C$ the $i$ and $-i$ characters are separate eigenspaces linked by reality; **in the real Jacobian they combine into the single block $U_{13}$** (a real-linear derivative can mix the complex Fourier sectors 1 and 3, so they are not individually invariant — e.g. at $\Omega=(1,\dots,1)$, $g=\lambda=0$, the cubic derivative sends a character-1 unit vector to a character-3 component of norm $0.05$). The projectors are orthogonal, so there is no first-order normal/tangent leakage (measured $\lesssim10^{-14}$).

**Background.** The original master-stability framework — block-diagonalizing the variational dynamics transverse to the synchronous state — provides the background [PC98]; the symmetry-adapted / irreducible-representation cluster decomposition that this deck-character block-diagonalization instantiates (the abelian $\mathbb Z_4$ case) follows the framework of [Pecora14, Sorrentino16]. The method is standard; only the explicit real-character pairing $U_{13}$ and the numeric blocks below are specific to this ring.

### 7.2 Linear spectral test vs nonlinear attraction

Two regimes are distinguished; conflating them is an error we avoid.
- **Fixed point.** For a fixed point of $F_3$, the transverse Jacobian $J\!\restriction_{U_2\oplus U_{13}}$ has moduli deciding the **linear** verdict.
- **Period-$p$ orbit.** The correct object is the **normal Floquet multiplier** $\rho_\perp$, the spectral radius of the transverse monodromy $\prod_{s=1}^{p}J_s\!\restriction_{U_2\oplus U_{13}}$; per-step factor $\rho_\perp^{1/p}$. Fixed-point (single-step) language must not be used for periodic regimes.

**The linear test is not an iff criterion for nonlinear attraction.** Precisely:
- $\rho_\perp<1$: the normal variational dynamics are exponentially asymptotically stable (**linearly transversely stable**); the orbit's transverse linearization decays exponentially.
- $\rho_\perp>1$: the orbit is **linearly transversely unstable**.
- $\rho_\perp=1$: the linear test alone is **inconclusive** about nonlinear attraction.

We therefore do **not** write "attracting iff all multipliers $<1$", and we avoid the word *contractive* (which would require a proved operator norm $<1$ in a stated norm). Two facts make the distinction concrete. (a) Within this map family, at $k=0$, $g=\lambda=0$, $\varepsilon>0$, each site obeys $z^+=z(1-\varepsilon|z|^2)$: the derivative at $0$ is the identity (every multiplier equals $1$), yet all small amplitudes decrease monotonically to $0$ at the **algebraic** rate $|z_n|\sim(2\varepsilon n)^{-1/2}$ — attraction without exponential rate, unresolved by the linear test. (b) Spectral radius $<1$ does not imply Euclidean per-step contraction: the stable $g=0.2,\lambda=0.5$ period-2 orbit has normal monodromy spectral radius $0.9912953186$ but Euclidean operator norm $1.0326263720>1$ in an orthonormal normal basis, so some perturbations grow transiently over one period before decaying. Our terminology is accordingly: *linearly transversely stable*, *normal variational decay*, *numerically observed transverse attraction*.

### 7.3 The default attractor

At defaults the reduced trajectory is a fixed point in $V_3$. The tangential ($U_0$) moduli and the transverse ($U_2$, $U_{13}$) moduli are (independently recomputed):
$$
U_0:\ (0.07264,0.08864,0.33013,0.42951,0.68095,1),\quad
U_2:\ (0.11947,0.17736,0.47305,0.48865,0.73101,0.85127),
$$
with largest $U_{13}$ modulus $0.94892$. Every **transverse** modulus ($U_2\cup U_{13}$) is $<1$: $V_3$ is **linearly transversely stable** at defaults. The single unit modulus lies in the tangential block $U_0$ and is the neutral global-phase direction of the three-node system itself (not a transverse direction). (The proof-audit companion labels this list "tangential moduli", not "transverse".)

### 7.4 Representative regimes ($M=12$)

$V_3$ is linearly transversely stable over a substantial sampled region, not everywhere. Six regimes ($\rho_\perp$ = $p$-step normal Floquet radius; $\chi=\|\operatorname{Re}\Omega\times\operatorname{Im}\Omega\|$; independently reproduced at seeds 0,19,407):

| $g$ | $\lambda$ | type | $p$ | $\chi$ | $\rho_\perp$ | $\rho_\perp^{1/p}$ | linear verdict |
|---|---|---|---|---|---|---|---|
| 0.2 | 0.001 | fixed | 1 | $\approx0$ | 0.948919213 | 0.948919213 | **stable** (default) |
| 0.2 | 0.5 | period-2 | 2 | 1.558108 | 0.991295319 | 0.995638146 | **stable** (high-$\chi$; op-norm $>1$, transient growth) |
| 0.1 | 0.3 | period-2 | 2 | 1.677188 | 1.134220618 | 1.064997943 | unstable |
| 0 | 0.4 | period-8 | 8 | 2.66357 | 2.416706689 | 1.116613805 | unstable |
| 0.3 | 0.5 | fixed | 1 | $\approx0$ | 1.094226451 | 1.094226451 | unstable |
| 0 | 0 | fixed, free phases | 1 | initial-dependent | 1 | 1 | neutral (linear test inconclusive) |

Neither high $\chi$ nor stronger synchronization alone predicts transverse stability: instability occurs at $\chi\approx0$ (the $g{=}0.3,\lambda{=}0.5$ fixed point) and stability coexists with sizable $\chi$ (the $g{=}0.2,\lambda{=}0.5$ orbit). The neutral case requires **$g=\lambda=0$**: setting $g=0$ alone does *not* decouple phases or imply neutrality — the $\lambda$-dependent phase coupling remains, and the table's own $g{=}0,\lambda{=}0.4$ row is a transversely unstable period-8 orbit ($\rho_\perp=2.4167$). At $g=0$ different phase basins can realize different $\chi$ without changing the period or normal multiplier; that is not decoupling.

### 7.5 A fixed-branch crossing, and regional (not global) scope

On the positive in-phase fixed branch there is a transverse instability onset. Solving $\varepsilon r_i(k_i-r_i^2)+g(\Delta_3 r)_i=0$ for the positive in-phase radii (crossing solution $\approx(1.62613,1.63733,1.93169)$, residual $2.3\times10^{-16}$) and setting the lowest eigenvalue of the projected normal radial operator to $-1$ gives
$$
g_\ast=0.4220744431784353\qquad(\text{canonical }k,\ \varepsilon=0.05,\ \lambda=0.001),
$$
a **transverse $-1$ eigenvalue crossing in the real character-2 block ($U_2$) of the selected positive in-phase reduced fixed branch**, near the $\lambda=0.001$ slice (eigenvalue slope $\approx-3.97$, nonzero; a full-map finite-difference normal radius at the crossing is $0.9999999999996$; nearby sampled reduced orbits remain on that branch to $<8.1\times10^{-16}$). It is not a longitudinal loss mislabeled as transverse, and it is not a basin claim. The separately located stationary-branch crossing $\lambda\approx0.42844590$ at $g=0.2$ occurs on a branch already longitudinally unstable there (largest tangential modulus $1.238$, sampled attractor period-2), and is **not** promoted to an attractor boundary.

**Terminology.** We use the description "transverse $-1$ crossing / loss of transverse stability" (a transverse period-doubling-type instability of the synchrony sector). We deliberately do **not** relabel it a *blowout* or a *bubbling / riddling* bifurcation: the blowout setting [OS94] and the distinct bubbling / riddling setting [ABS94] both concern a **chaotic** invariant set losing transverse stability, which is not the fixed-branch situation studied here. The plain description already fits and is retained.

Atlas evidence (authoritative rows; one coarse grid with adaptive refinement, **not** two independent grids or area fractions):

| stability label | coarse grid (190) | all samples incl. coarse (379) |
|---|---|---|
| stable | 96 | 150 |
| unstable | 40 | 132 |
| boundary / neutral | 1 | 1 |
| unresolved | 53 | 96 |

Adaptive refinement concentrates samples at transitions, so $150/379$ is **not** the area fraction of a stable region; we describe a *substantial sampled stable region* only, with $32$ stable samples at $\chi>0.1$. The $37$ retained edge brackets are **numerical evidence for transitions, not proof of smooth codimension-one boundaries everywhere**. At the numerically located $g_\ast$ crossing, the computed eigenvalue slope is approximately $-3.97$ and is nonzero to the reported numerical precision (the root tolerance is numerical precision, not an interval-certified error bound). No global-basin or complete-bifurcation claim is made; unresolved samples remain unresolved.

## 8. Numerical perturbation verification ($M=12$)

**Background.** Near-cluster numerical evolution is illustrated in [Schaub16, §III.B.2 and Fig. 3]. The normal perturbations and measured decay / growth rates below are our own tests of this map; no citation is needed to justify the measured rates.

Lift a reduced state and add a transverse perturbation, $\Omega^{12}=P\Omega^{3}+\varepsilon_\perp\xi$, $\xi\in U_2\oplus U_{13}$ (real 18-dimensional normal space), advance the full $F_{12}$ (never forced back into $V_3$), and measure $d_\perp(t)=\|(I-QQ^\ast)\Omega(t)\|$. Independently initialized at a retained orbit point plus a dominant normal Floquet direction, amplitudes $10^{-7},10^{-5}$, 1800 steps, period-stroboscopic fits restricted to $10^{-10}<d_\perp<10^{-4}$ and to distances $\ge100\times$ the simultaneously advanced control's sector error (saturation and roundoff-floor samples excluded). Measured normal log-rates match the variational prediction:

| $g,\lambda$ | perturbation | predicted log-rate | measured log-rate | fitted step range |
|---|---|---|---|---|
| 0.2, 0.001 | $10^{-5}$ | $-0.05243161232$ | $-0.05243161307$ | 8–207 |
| 0.2, 0.5 | $10^{-5}$ | $-0.004371394220$ | $-0.004371394222$ | 8–406 (every 2nd) |
| 0.1, 0.3 | $10^{-7}$ | $+0.06297286724$ | $+0.06297286730$ | 8–108 (every 2nd) |
| 0, 0.4 | $10^{-7}$ | $+0.11030071763$ | $+0.11030071784$ | 16–56 (every 8th) |
| 0.3, 0.5 | $10^{-7}$ | $+0.09004767578$ | $+0.09004767572$ | 8–76 |
| 0, 0 | $10^{-7}$ | $\approx0$ | $\approx0$ | 8–207 |

Eleven of the twelve runs give an admissible fit; the largest rate error across those fits is $1.64\times10^{-8}$. The period-8 run at amplitude $10^{-5}$ has only one usable unsaturated stroboscopic sample under the strict cutoff, so no slope is reported from it (its $10^{-7}$ companion supplies the check). The two stable regimes ($g{=}0.2,\lambda{=}0.001$ and $0.2,0.5$) show **negative** rates (normal decay); the unstable regimes show positive rates and depart into off-sector attractors. Unperturbed lifted controls remain in $V_3$ to $\sim10^{-15}$: the exact invariant sector does not spontaneously break in exact arithmetic, and infinitesimal transverse errors grow precisely where the transverse linearization predicts.

These are the corrected baseline perturbation values; an earlier draft mixed the baseline and a later feedback experiment (different amplitudes, durations, and floors), and reversed two rate columns. The two experiments are kept separate here, and every figure is drawn from a named data row with its parameters, seed, amplitude, direction, duration, and error definition (Appendix D).

## 9. Relation to a second ring operator

A second, independently defined operator carries the same $L_3$ on its three-periodic phase sector: a spectral-branching ("RSB") phase Laplacian built directly from $\Delta_{12}$. Its full state space is the tensor product
$$
\mathbb C^{3}_{\text{channel}}\otimes\mathbb C^{12}_{\text{phase}}\otimes\mathbb C^{2}_{\text{helicity}},
$$
on which channel and helicity operations act on spectator factors and the phase Laplacian is $\Delta_{12}$. The **preserved sector** of the default update ($\alpha=0$) is accordingly $\mathbb C^{3}\otimes V_3\otimes\mathbb C^{2}$; the phase Laplacian commutes with the residue pull-back, so on nonzero admissible states the full Hamiltonian intertwines with the $M=3$ Hamiltonian under the lifted phase map. Because the source normalizes its state, a full **normalized**-step identity uses the isometry $Q$ on the phase factor (i.e. $Q\otimes\text{id}$ factors), not an unscaled nonlinear $P$-identity; and the domain excludes the zero state, where a normalization fallback (raising without an RNG, or a random RNG fallback) produces a generically non-three-periodic normalized state. The optional dominant-index contraction ($\alpha>0$) selects a single band via a one-hot mask, breaking the deck symmetry — hence breaking the sector — including under adaptive entropy scaling.

Discipline: this is **shared exact algebra** (both ring operators contain $L_3$ as their three-periodic sector because both are built from $\Delta_{12}$, exactly as Theorem 1 predicts), **not** an identity between the three-complex-variable oscillator map and the 72-complex-component RSB evolution. They never share a state vector; nothing more is asserted.

**Background.** The shared phase-Laplacian sector uses the standard quotient / synchrony mechanism [GR01, SGP03]; §9 establishes the particular comparison for the two operators considered here. The literature supports the mechanism, not an unrestricted full-operator theorem or any RSB-specific result, and nothing beyond the shared quotient algebra of this pair is claimed.

## 10. Feedback compatibility (sufficient condition)

Suppose feedback modifies **only** the amplitude coefficient $k$, through an effective coefficient depending on read-out/auxiliary data.

> **Corollary 3 (sufficient compatibility condition for $k$-only feedback).** Suppose the auxiliary/read-out variables admit compatible lifts such that on $V_3$
> $$
> k_{\mathrm{eff}}^{M}\big(P\Omega,\ \eta_M\big)=P\,k_{\mathrm{eff}}^{3}\big(\Omega,\ \eta_3\big),
> \tag{10.1}
> $$
> where inputs are typed as follows: either an oscillator argument $x\in\mathbb C^3$ with a compatible lifted state/read-out, or a **scalar** read-out $z$ with equal scalar read-outs on lifted states (in which case $P$ is **not** applied to $z$). Then $V_3$ remains invariant under the feedback-augmented $F_M$, and $F_M(P\Omega)=P F_3(\Omega)$ continues to hold.

**Proof.** The only change to $F_M$ is $k\rightsquigarrow k_{\mathrm{eff}}^{M}(P\Omega,\eta_M)$ in (6.1a). By (10.1) this equals $P k_{\mathrm{eff}}^3(\Omega,\eta_3)$, itself three-periodic and pulled back; the proof of Proposition 2 applies verbatim. $\qquad\blacksquare$

**Background.** Corollary 3 is a specialization of the standard principle that a coupling or modification respecting the balanced (equitable) partition preserves the synchrony subspace [SGP03, Schaub16]. The $k$-only condition (10.1) is the explicit, model-specific form of that principle for this architecture; no stronger general theorem is needed, and it is stated as sufficient, not necessary (caution 1).

Three cautions keep this in proportion.
1. **Sufficient, not iff.** (10.1) is a sufficient one-step condition for this architecture; it is **not** necessary. Counterexample to a necessity claim: with $k_{\mathrm{eff}}^{M}=Pk_{\mathrm{eff}}^3+b$ for non-periodic $b$ and a compensating feedback term $-\varepsilon\Omega\odot b$ before synchronization, the map is unchanged so the reduction is exact although (10.1) fails; likewise arbitrary coefficients differing only on zero coordinates leave the pre-sync map unchanged. The earlier companion's "iff" wording is withdrawn.
2. **Preservation of $V_3$ $\neq$ equality to a specified $F_3$.** A common scalar depending on the **unnormalized** norm $\|P\Omega\|=\sqrt{M/3}\,\|\Omega\|=2\|\Omega\|$ (for $M=12$; the required factor is $\sqrt{12/3}=2$, not an "undefined sector count") preserves $V_3$ while generally inducing a *different* three-node feedback; invariance and equality-to-$F_3$ are distinct. Read-out normalization must be matched for equality.
3. **Compatibility bears on invariance only; transverse boundaries can move.** A compatible feedback can preserve the sector yet change transverse derivatives. One recovered scalar-amplitude law (all effective coefficients of each machine multiplied by one common real scalar) is compatible under a consistent lift and empirically shifts the low-$\lambda$ fixed-branch boundary slightly toward instability (bracketed $g\in[0.421,0.4215]$ vs no-feedback $0.42207$) — a **local** shrinkage; across matched samples some transverse factors improve and others worsen, $167$ matched comparisons retain an unresolved side, and the net global change of the stable region is **undetermined**. This section is a compatibility criterion, not a physical-portal result.

## 11. Discussion

The paper isolates one exact structure: a three-state nonlinear oscillator is the restriction to an invariant subspace $V_3$ of an $M$-ring map (any $M$ divisible by three), where $V_3$ is the pull-back of functions along the covering $C_M\to C_3$. The linear backbone (Theorem 1) is elementary and general — $\Delta_M P=P\Delta_d\iff d\mid M$, with $Q^\ast\Delta_M Q=\Delta_d$. The nonlinear content (Proposition 2) rests on the modular identity (6.2), which holds for every $M=3q$. The dynamical content (§7–§8, $M=12$) is that $V_3$ is linearly transversely stable over a substantial sampled region, established by the real deck-character decomposition and confirmed by direct perturbation, with explicit unstable and neutral counterexamples and the linear/nonlinear distinction respected throughout.

Three features make the result more than a curiosity: the reduction is *exact* (one-step identity to rounding, identical in exact arithmetic); the full real linearization is *structured* by the deck group into $U_0\oplus U_2\oplus U_{13}$, with tangential block $U_0$ and transverse restriction $U_2\oplus U_{13}$; and the same $L_3$-in-$\Delta_{12}$ phenomenon recurs in a second, independently built operator (§9), via the standard quotient / synchrony mechanism [GR01, SGP03] applied to the particular pair compared there.

## 12. Limitations

- **The ring extension is a construction of this paper**, a 2026 mathematical object. We do **not** claim any pre-existing three-node system was historically designed as an $M$-ring, nor that any $M$ is privileged beyond the arithmetic $3\mid M$.
- **Transverse attraction is local and regional** ($M=12$), with explicit unstable and neutral counterexamples; no global basin, complete bifurcation diagram, or longitudinal-stability theorem is claimed. Unresolved samples remain unresolved. At $\rho_\perp=1$ the linear test is inconclusive.
- **No physical interpretation.** $\Omega$, $z$, $\chi$, $k$, and the graphs are abstract; no physical scale, particle, spacetime, or measured phenomenon is claimed.
- **No systems claim.** §9 asserts only shared algebra between two mathematical operators, not dynamical identity, and no production/memory-system claim.
- **Feedback compatibility is a sufficient criterion**, not a portal result; the recovered scalar law's global stability effect is undetermined.
- **No novelty/priority claim.** §§3–5 are elementary standard theory — network quotients, graph fibrations, equitable partitions, synchrony subspaces, master-stability / cluster-synchronization (§1.2–1.4; `PAPER_A_LITERATURE_CONTEXT_v0.1.md`). The model-specific content is the §§6–10 constructions and the §7–§8 transverse-stability atlas, whose novelty is recorded as **unresolved**, never asserted; a literature-context pass is not a novelty determination.

## 13. Conclusion

Strongest supportable conclusion: **for every $M$ divisible by three, the specified three-state nonlinear map admits an exact invariant pull-back realization on the $M$-cycle with three-periodic coefficients; for the $M=12$ realization studied numerically here, the invariant sector exhibits linearly stable and unstable transverse regimes, and direct nonlinear perturbations confirm transverse attraction in representative linearly stable regimes.** The reduction is a graph covering $C_M\xrightarrow{}C_3$ with pull-back $V_3$, on which the ring Laplacian equals the triangle Laplacian and the ring nonlinear map equals the three-node map; for $M=12$ the full real linearization block-decomposes by the deck group $\mathbb Z_4$ into $U_0\oplus U_2\oplus U_{13}$, with tangential block $U_0$ and transverse restriction $U_2\oplus U_{13}$ linearly stable over a substantial sampled region. We claim nothing about nature, quantum mechanics, or the historical origin of the three-node map.

---

## Appendix A — Theorem proofs (supplementary)

**A.1 Sizes.** (2.1) follows from circulant diagonalization for $M\ge3$; the degenerate Laplacians are $\Delta_1=(0)$ and $\Delta_2=\begin{psmallmatrix}-2&2\\2&-2\end{psmallmatrix}$. Theorem 1(i),(iii),(iv) hold at all positive sizes (P01 boundary table: $d=1$ constant column annihilated by $\Delta_M$; $M=d=2$ identity lift; etc.).

**A.2 Exactness of $Q^\ast\Delta_M Q=\Delta_d$.** From (i), $\Delta_M Q=Q\Delta_d$; left-multiply by $Q^\ast$ and use $Q^\ast Q=I_d$. The compressed matrix $q^{-1}P^\ast\Delta_M P$ is integer ($=\Delta_d$); $Q$ itself need not be integer.

**A.3 Regularity/fixed space.** For a regular covering the pull-back subspace equals the deck-fixed space; §5 verifies this for $(12,3)$ via $e^{\pi ij/2}=1\iff j\in\{0,4,8\}$.

**A.4 Converse.** The boundary-row argument (§3, proof of (ii)) is the analytic classification; $(3,2)$ is the sole non-divisor invariant image in $1\le d\le M$, a symmetry fixed space, not a covering sector.

## Appendix B — Nonlinear reduction details

**B.1 Stage-by-stage commutation.** Pointwise term: residue-classwise action on pulled-back vectors. Coupling: Theorem 1(i). Synchronization: the modular identity (6.2), valid for every $M=3q$ including the wrap. Composition gives $F_M\circ P=P\circ F_3$ (Prop. 2). Simultaneous updates are essential; a sequential sweep defines a different map.

**B.2 Neighbour-residue identity.** $\{((n{-}1)\bmod M)\bmod3,\,((n{+}1)\bmod M)\bmod3\}=\mathbb Z_3\setminus\{n\bmod3\}$ for every $n$ and every $M$ with $3\mid M$. This is the sole nonlinear-specific ingredient; it is **not** special to $M=12$.

**B.3 Zero-amplitude convention.** (6.0) makes $F_M$ global; the reduction is preserved because the identical deterministic convention is applied at all residue copies. Jacobian/Floquet claims use only orbits with nonzero pre-sync components.

## Appendix C — Numerical methods

**C.1 Regression audit** (`paperA_proof_audit_v0_2.py`, pure math, no implementation import): 20/20 checks corroborating (not replacing) the analytic proofs — intertwining exact for all divisor pairs $M\le90$ and failing for every non-divisor $\le60$; the **invariance classification via $(I-PP^{+})\Delta_M P=0$** matching "$d\mid M$ or $(3,2)$" over $1\le d\le M\le40$; the $(5,3)$ demonstration that the old $P^{+}P=I$ check was not an invariance test; $Q^\ast Q=I_3$, $Q^\ast\Delta_{12}Q=L_3$, $P^\ast\Delta_{12}P=4L_3$, $\|P\Omega\|=2\|\Omega\|$; $V_3=\operatorname{span}\{e_0,e_4,e_8\}$ with exact complement spectrum $\{-2\pm\sqrt3,\dots\}$; the real projectors $E_0,E_2,E_{13}$ with ranks $6,6,12$; the modular identity (6.2) for $M\in\{3,\dots,63\}$; and the $z^+=z(1-\varepsilon|z|^2)$ counterexample (unit multiplier, algebraic decay $|z_N|=7.07\times10^{-3}$ matching $(2\varepsilon N)^{-1/2}$).

**C.2 Reduction check** (`paperA_reduction_check.py`, read-only reference import, `sys.dont_write_bytecode=True`, zero `.pyc` written): one-step and free-trajectory discrepancies as in §6.3 (max per-component / infinity-norm). The referee's independent reproduction (fourth-order finite-difference Jacobian, direct cyclic matrices, source loaded only after re-derivation) gives one-step $5.53\times10^{-15}$, defaults 600-step $2.13\times10^{-15}$, high-$\lambda$ $3.82\times10^{-15}$, generalization $2.61\times10^{-16}$, and the unrestricted-regime caveat ($4.94$ per-component / $11.09$ Euclidean).

**C.3 Stability/perturbation numerics.** Transverse Jacobians computed analytically in radial/tangential coordinates and cross-checked against a fourth-order central-difference stencil (largest multiplier difference under $h$-refinement $5.20\times10^{-10}$); trajectory classification periods 1–64 at relative residual $<10^{-10}$; unresolved states never assigned fixed-point Jacobians; perturbation fits stroboscopic, pre-saturation, with the strict cutoffs of §8. The stability atlas and perturbation data are the Phase-3V reproduction and the referee reproduction; this paper re-derives the algebra and the reduction independently and cites those data rather than regenerating the atlas.

## Appendix D — Reproducibility

**Authoritative derivations and data (project-relative to `TRIOCTAGON_new/`):**
- `reconstruction/EXACT_3_12_24_STRUCTURE_v0.1.md` — Theorem 1, Fourier form, tower, nonlinear extension.
- `reconstruction/CLAUDE_PHASE3_HOST_FEEDBACK_AND_3_12_24_RECOVERY_v0.1.md` — parent report.
- `reconstruction/CODEX_PHASE3V_PORTAL_AND_12RING_VERIFICATION_v0.1.md` — independent reproduction: covering/fibre/deck; reduction; transverse-stability atlas; direct perturbations; **feedback compatibility in its §9, with the feedback experiments in its §15** (corrected from an earlier miscitation).
- `reconstruction/papers/CODEX_PAPER_A_REFEREE_REPORT_v0.1.md` — the referee report driving this revision, and `verification/paperA_referee/` — its data (`reference_summary.json`, `reference_crosscheck.csv`, `preservation_result.json`).
- `reconstruction/MASTER_RESEARCH_RECONSTRUCTION_MAP_v0.1.md`, `MASTER_EQUATION_LINEAGE_v0.1.md`, `MASTER_PUBLICATION_ROADMAP_v0.1.md` — provenance/scope (Paper A entry).

**Verification code (this paper):** `verification/paperA/paperA_proof_audit_v0_2.py` and `verification/paperA/paperA_reduction_check.py` (copies of the publication-specific scripts; the earlier copies under `verification/master_research_map/` are retained unchanged). Parent verification `verification/phase3_host_feedback/phase3_structure_checks.py` and Phase-3V data `verification/phase3v_portal_12ring/`.

**Reference implementation (read-only, definitions only):** `kernel_TO/model_core.py` (`TriOctaPhaseLockModel.phase_lock_step` = (6.1a); $L_3$), `kernel_TO/phase_triad_sync.py` (the synchronization $S$; simultaneous, matching (6.1b)), `kernel_TO/rsb_model.py` (the second ring operator, §9), `kernel_TO/constants_selector.py` (the amplitude coefficient $k$). Full sha256 content hashes are in `verification/master_research_map/hashes.tsv` (not modified); no source file was modified, and no hard-coded container path is assumed — scripts derive the project root or take it as an argument.

---

## References

Full metadata (with DOIs and the verification note) is in the companion `PAPER_A_REFERENCES_v0.2.md`. All references are literature context / positioning; none supports a mathematical step of the frozen result. (Field04 and Stewart07, cited in v0.4, became unused after the v0.5 attribution patches and are removed from this publication bibliography; they remain in the reference ledger.)

- **[SGP03]** Stewart, Golubitsky, Pivato. Symmetry groupoids and patterns of synchrony in coupled cell networks. *SIAM J. Appl. Dyn. Syst.* 2(4):609–646, 2003. DOI 10.1137/S1111111103419896.
- **[GST05]** Golubitsky, Stewart, Török. Patterns of synchrony in coupled cell networks with multiple arrows. *SIAM J. Appl. Dyn. Syst.* 4(1):78–100, 2005. DOI 10.1137/040612634.
- **[GS06]** Golubitsky, Stewart. Nonlinear dynamics of networks: the groupoid formalism. *Bull. Amer. Math. Soc.* 43(3):305–364, 2006. DOI 10.1090/S0273-0979-06-01108-6.
- **[GFBC24]** I. Stewart. Groupoids, Fibrations, and Balanced Colorings of Networks. *Int. J. Bifurcation and Chaos* 34(7):2430014, 2024 (41 pp). DOI 10.1142/S0218127424300143.
- **[BV02]** Boldi, Vigna. Fibrations of graphs. *Discrete Math.* 243(1–3):21–66, 2002. DOI 10.1016/S0012-365X(00)00455-6.
- **[DL15]** DeVille, Lerman. Modular dynamical systems on networks. *J. Eur. Math. Soc.* 17(12):2977–3013, 2015. DOI 10.4171/JEMS/577.
- **[NRS16]** Nijholt, Rink, Sanders. Graph fibrations and symmetries of network dynamics. *J. Differential Equations* 261(9):4861–4896, 2016. DOI 10.1016/j.jde.2016.07.013.
- **[GR01]** Godsil, Royle. *Algebraic Graph Theory.* Springer GTM 207, 2001. DOI 10.1007/978-1-4613-0163-9.
- **[OYSB13]** O'Clery, Yuan, Stan, Barahona. Observability and coarse graining of consensus dynamics through the external equitable partition. *Phys. Rev. E* 88(4):042805, 2013. DOI 10.1103/PhysRevE.88.042805.
- **[Schaub16]** Schaub, O'Clery, Billeh, Delvenne, Lambiotte, Barahona. Graph partitions and cluster synchronization in networks of oscillators. *Chaos* 26(9):094821, 2016. DOI 10.1063/1.4961065.
- **[PC98]** Pecora, Carroll. Master stability functions for synchronized coupled systems. *Phys. Rev. Lett.* 80(10):2109–2112, 1998. DOI 10.1103/PhysRevLett.80.2109.
- **[Pecora14]** Pecora, Sorrentino, Hagerstrom, Murphy, Roy. Cluster synchronization and isolated desynchronization in complex networks with symmetries. *Nat. Commun.* 5:4079, 2014. DOI 10.1038/ncomms5079.
- **[Sorrentino16]** Sorrentino, Pecora, Hagerstrom, Murphy, Roy. Complete characterization of the stability of cluster synchronization in complex dynamical networks. *Sci. Adv.* 2(4):e1501737, 2016. DOI 10.1126/sciadv.1501737.
- **[ABS96]** Ashwin, Buescu, Stewart. From attractor to chaotic saddle: a tale of transverse instability. *Nonlinearity* 9(3):703–737, 1996. DOI 10.1088/0951-7715/9/3/006.
- **[ABS94]** Ashwin, Buescu, Stewart. Bubbling of attractors and synchronisation of chaotic oscillators. *Phys. Lett. A* 193(2):126–139, 1994. DOI 10.1016/0375-9601(94)90947-4.
- **[OS94]** Ott, Sommerer. Blowout bifurcations: the occurrence of riddled basins and on-off intermittency. *Phys. Lett. A* 188(1):39–47, 1994. DOI 10.1016/0375-9601(94)90114-7.
- **[HMM93]** Hansel, Mato, Meunier. Clustering and slow switching in globally coupled phase oscillators. *Phys. Rev. E* 48(5):3470–3477, 1993. DOI 10.1103/PhysRevE.48.3470.
- **[AS92]** Ashwin, Swift. The dynamics of $n$ weakly coupled identical oscillators. *J. Nonlinear Sci.* 2(1):69–108, 1992. DOI 10.1007/BF02429852.
- **[DF19]** Dalfó, Fiol, Širáň. The spectra of lifted digraphs. *J. Algebraic Combin.* 50(4):419–426, 2019. DOI 10.1007/s10801-018-0862-y.
- **[Kaneko90]** Kaneko. Clustering, coding, switching, hierarchical ordering, and control in a network of chaotic elements. *Physica D* 41(2):137–172, 1990. DOI 10.1016/0167-2789(90)90119-A.

---

