# Tri-Octagon Mathematical Atlas — Lane-1 Closeout Supplement A

## General cycle operators and pullback domains — A07 / A08 / A09

Date: 2026-09-29. Version: v0.1. External source packet, not a numbered Atlas entry and not a publication.

**A07 = FULL; A08 = FULL; A09 = FULL.** The final independent checker passed 31/31 check records. The authorized existing test file passed 10 tests and 40 subtests. Full before/after integrity comparisons passed.

Scope: independently reconstruct the full accepted domains of these three owners. Atlas 02 remains closed. No other ledger row is reassessed. The prior completeness review and crosswalk remain unchanged; this supplement does not issue a new overall Lane-1 completeness verdict.

Authoritative repository: C:\TORMENT\TRIOCTAGON_new\trioctagon-physics.

Expected and observed HEAD: **34c21830e7e7c4b5f4a5a940d084c37feaf1f82c**.

All sources, papers, prior Atlas, historical kernel and production trees were treated as read-only. Deliverables are external, in C:\Users\Notandi\.codex\reports. Mathematical scalars are complex unless stated otherwise; the star denotes Hermitian adjoint.

## 0. Authority and evidence

| ID | Source | Role |
|---|---|---|
| S1 | [covering.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/covering.py) | A07 lines 20–28, A08 lines 31–37, A09 lines 40–47; validation lines 8–17 |
| S2 | [test_covering.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_covering.py) | Only existing repository test file executed |
| S3 | [Paper A publication v1.0](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/publication/paper_A_publication.md) | Accepted definitions and Theorem 1 in §§2–3; darts in §4.3 |
| S4 | [Paper A mathematical draft v0.5.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md) | Exact current mathematical source identified by K0; accepted analytic converse and invariance proof in §§2–3 |
| S5 | [Paper A proof audit v0.3](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/PAPER_A_PROOF_AUDIT_v0.3.md) | Prior proof/audit record, inspected and not rerun |
| S6 | [Paper A audit v0.2 script](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/verification/paperA/paperA_proof_audit_v0_2.py) | Exact support location; older finite regression, not the new independent checker; not executed |
| S7 | [K0 definition ledger](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md) | PA authority registry and A07–A09 ownership rows |
| S8 | [Current completeness review](C:/Users/Notandi/.codex/reports/TRIOCTAGON_CURRENT_KERNEL_MATHEMATICAL_COMPLETENESS_REVIEW_v0.1.md) | Records the omissions being closed; unchanged |
| S9 | [Current crosswalk](C:/Users/Notandi/.codex/reports/TRIOCTAGON_CURRENT_KERNEL_ATLAS_CROSSWALK_v0.1.json) | Prior coverage/ownership record; unchanged |
| S10 | [Closed Atlas 02](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_3_TO_12_COVERING_SOURCE_PACKET_v0.1.md) | Existing 12→3 / 3q→3 authority, including §7's P-versus-Q counterexample |

K0 explicitly identifies S4 as the mathematical source of S3. S5 calls itself a companion to the older v0.3 draft: it is supporting history, not a competing current manuscript. S4 preserves the accepted mathematics through later citation revisions. The prior paper audit's recorded results are distinguished from this task's new independent checks.

Universal statements below have analytic proofs. Bounded exact calculations are labelled FINITE_AUDIT in the JSON and do not replace those proofs. The checker builds all mathematical expectations before importing current covering.py. The results include all witness matrices, source SHA256 values, and separate test, packaging and integrity receipts.

## 1. A07: cycle operator for every positive size

For \(M\ge1\), index coordinates by \(\mathbb Z_M=\{0,\ldots,M-1\}\), and define
\[
(\Delta_M f)_n=f_{(n+1)\bmod M}+f_{(n-1)\bmod M}-2f_n.
\]
The two neighbour incidences remain separate terms even when their endpoints coincide.

At \(M=1\), both terms are \(f_0\) and cancel the subtraction. At \(M=2\), both neighbours of a vertex are the opposite vertex. Therefore
\[
\Delta_1=[0],\qquad
\Delta_2=\begin{pmatrix}-2&2\\2&-2\end{pmatrix}.
\]
For \(M\ge3\), the two neighbours are distinct; the ordinary negative cycle Laplacian has diagonal \(-2\) and a \(+1\) at each neighbour:
\[
\Delta_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}=L_3,\qquad
\Delta_4=\begin{pmatrix}-2&1&0&1\\1&-2&1&0\\0&1&-2&1\\1&0&1&-2\end{pmatrix}.
\]

A single simple edge on two vertices has negative Laplacian
\(\begin{psmallmatrix}-1&1\\1&-1\end{psmallmatrix}=\Delta_2/2\).
Substituting that operator changes its spectrum and, for example, the \(6\to2\) intertwining. Keeping diagonal \(-2\) but reducing each off-diagonal 2 to 1 would additionally destroy zero row sums. Neither is an allowed simplification of the accepted convention.

Let \(e_j^{(M)}(n)=\exp(2\pi ijn/M)\), \(j=0,\ldots,M-1\). Direct substitution gives
\[
\Delta_M e_j^{(M)}
=\left(e^{2\pi ij/M}+e^{-2\pi ij/M}-2\right)e_j^{(M)}
=-4\sin^2(\pi j/M)e_j^{(M)}.
\]
Distinct modes are orthogonal: their inner product is a geometric sum whose ratio is different from 1 but has Mth power 1. Each mode has squared norm \(M\); together the \(M\) modes are a basis.

At \(M=1\), only \(j=0\) exists and the spectrum is \(\{0\}\). At \(M=2\), indices \(0,1\) give \(\{0,-4\}\), with vectors \((1,1)\), \((1,-1)\). Both follow from the same formula with the correct indexing.

## 2. Hermitian structure, energy and kernel

Set \(Sf(n)=f(n+1\bmod M)\). The shift is unitary, \(S^\ast=S^{-1}\), including \(S=I\) when \(M=1\). Then
\[
\Delta_M=S+S^\ast-2I=-(S-I)^\ast(S-I).
\]
Its matrix is real symmetric and Hermitian. Applying it to \(\mathbf1_M\) gives zero, so its row sums are zero. For every complex vector \(f\),
\[
\langle f,\Delta_M f\rangle
=-\sum_{n=0}^{M-1}|f_{n+1}-f_n|^2
=-\frac12\sum_{n=0}^{M-1}\sum_{\sigma\in\{-1,+1\}}
 |f_{n+\sigma}-f_n|^2\le0.
\]
All indices wrap. Relabelling the backward list gives the second equality; its factor \(1/2\) compensates for forward/backward duplication.

At \(M=2\), the forward list already has two terms for the same endpoint difference, corresponding to two parallel undirected edges. The energy is \(-2|f_1-f_0|^2\). At \(M=1\), the loop differences are zero. Simple-cycle edge-count wording must be qualified in these degenerate cases.

If \(\Delta_M f=0\), this energy vanishes and each successive difference is zero. Successive steps visit every vertex, so \(f\) is constant. Conversely all constants are in the kernel. Thus, for every positive size,
\[
\ker\Delta_M=\operatorname{span}\{\mathbf1_M\},\quad
\dim_{\mathbb C}\ker\Delta_M=1,\quad \operatorname{rank}\Delta_M=M-1.
\]
At \(M=1\), the entire one-dimensional space consists of constant vectors; there is no exception.

## 3. A08: general residue pullback, rank and kernel

For arbitrary positive \(M,d\), define
\[
P:\mathbb C^d\to\mathbb C^M,\qquad
(Pu)_n=u_{n\bmod d},\qquad P_{n,r}=\mathbf1_{\{n\bmod d=r\}}.
\]
Outside divisibility, the residue function on the chosen representatives is not a homomorphism of cyclic groups. Wrap compatibility must be proved separately.

Nonzero columns are indicators of disjoint nonempty residue fibres, so they are independent. If \(M\ge d\), the first \(d\) rows are \(I_d\), and every column occurs. If \(d>M\), \(P=[I_M\ 0]\). Consequently
\[
\operatorname{rank}P=\min(M,d),\qquad
\dim\ker P=d-\min(M,d)=\max(0,d-M).
\]
For \(M\ge d\), \(P\) is injective. For \(d>M\), it is surjective onto \(\mathbb C^M\), and
\(\ker P=\operatorname{span}\{\delta_M,\ldots,\delta_{d-1}\}\).
Here \(\delta_r\) is the coordinate unit vector, distinct from a Fourier mode. P is not injective in this regime.

Define \(V_d=\operatorname{im}P\), with \(M\) understood. Membership means exactly that entries at representative indices with the same residue modulo \(d\) agree. Its complex dimension is \(\min(M,d)\). The nonzero fibre-indicator columns form an orthogonal basis.

## 4. Column multiplicities and the scalar-normalization obstruction

Write \(M=ad+b\), \(a\ge0\), \(0\le b<d\). There are \(a\) full residue blocks followed by \(0,\ldots,b-1\). Thus for \(0\le r<d\),
\[
c_r=\#\{n:0\le n<M,\ n\bmod d=r\}
=a+\mathbf1_{\{r<b\}}
=1+\left\lfloor\frac{M-1-r}{d}\right\rfloor
=\left\lceil\frac{M-r}{d}\right\rceil.
\]
The floor expression counts indices \(r+td<M\). When \(r\ge M\), its floor is \(-1\), so the count is zero, also as given by the ceiling. No positive-count assumption is hidden.

Disjoint column supports yield
\[
P^\ast P=\operatorname{diag}(c_0,\ldots,c_{d-1}),\qquad
\|Pu\|^2=\sum_r c_r|u_r|^2.
\]
If \(b=0\), all counts equal \(M/d\). If \(b>0\), both \(a+1\) and \(a\) occur, so the counts are not uniform. Hence
\[
P^\ast P=qI_d\text{ for a scalar }q
\quad\Longleftrightarrow\quad d\mid M,\qquad q=M/d>0.
\]
In particular \(P^\ast P=(M/d)I_d\) iff \(d\mid M\).

A global scalar \(s\) with \((sP)^\ast(sP)=I_d\) would require \(|s|^2c_r=1\) for every r. This is possible only for uniform positive counts. Columnwise normalization in a nondivisor full-column-rank case would define a different map; it would not restore the accepted intertwining. When \(d>M\), zero columns prevent any isometric embedding of the whole domain.

## 5. Image V versus the cyclic shift-fixed space W

Define separately
\[
W_d=\{f\in\mathbb C^M:f_{n+d\bmod M}=f_n\text{ for every }n\}.
\]
Let \(g=\gcd(M,d)\). The shift by \(d\) has \(g\) orbits, each a congruence class modulo \(g\), of length \(M/g\). Indeed, the least positive \(t\) with \(td=0\bmod M\) is \(M/g\). A fixed vector has one free value per orbit, so
\[
\dim W_d=\gcd(M,d).
\]

For all \(M,d\), \(W_d\subseteq V_d\): indices with the same representative residue modulo \(d\) differ by a multiple of \(d\), so shift invariance equates their entries.
For \(1\le d\le M\), \(\dim V_d=d\); equality requires \(\gcd(M,d)=d\), equivalent to \(d\mid M\). Conversely, divisibility makes wrap by \(M\) preserve residues modulo \(d\), so every vector of \(V_d\) is shift-fixed. Therefore
\[
1\le d\le M:\quad V_d=W_d\quad\Longleftrightarrow\quad d\mid M.
\]

At \((5,3)\),
\[
V_3=\{(a,b,c,a,b)\},\qquad
W_3=\operatorname{span}\{(1,1,1,1,1)\}.
\]
For instance \((0,0,1,0,0)\in V_3\) is not shift-by-3 fixed: indices 2 and \(2+3=0\bmod5\) have different values.

For \(d>M\), \(V_d=\mathbb C^M\). It equals \(W_d\) exactly when \(\gcd(M,d)=M\), i.e. \(M\mid d\), a different direction of divisibility. At \((2,4)\), shift-by-4 is the identity and \(V_4=W_4=\mathbb C^2\), although \(4\nmid2\). Thus no unrestricted shift-fixed characterization or unrestricted equality criterion \(d\mid M\) is asserted.

The shift commutes with \(\Delta_M\), so \(W_d\) is always invariant. That does not imply invariance of the potentially larger \(V_d\).

## 6. Intertwining sufficiency: keep both incidences

Suppose \(d\mid M\). For either sign \(\sigma=\pm1\),
\[
((n+\sigma)\bmod M)\bmod d=(n\bmod d+\sigma)\bmod d.
\]
Wrapping removes a multiple of M, hence a multiple of d. Setting \(r=n\bmod d\) gives
\[
(\Delta_MPu)_n=u_{r+1\bmod d}+u_{r-1\bmod d}-2u_r
=(P\Delta_du)_n.
\]
Therefore \(\Delta_MP=P\Delta_d\).

For \(d=1\), the two terms both equal \(u_0\) and cancel. For \(d=2\), they both equal the opposite coordinate and must both be counted. This is a linear statement valid for every positive divisor pair, independently of graph terminology.

## 7. Intertwining converse for all positive pairs

### 7.1 Nondivisor with \(1\le d\le M\)

Then \(d\ge2\), \(M\ge d+1\), and \(r=M\bmod d\in\{1,\ldots,d-1\}\).
Row zero gives
\[
(\Delta_MPu)_0=u_1+u_{r-1}-2u_0,\qquad
(P\Delta_du)_0=u_1+u_{d-1}-2u_0.
\]
Their difference is \(u_{r-1}-u_{d-1}\). Since \(r-1\ne d-1\), choosing \(u=\delta_{d-1}\) gives \(-1\). This includes \(d=2\), where the second expression retains repeated incidences.

### 7.2 Unseen coordinate with \(d>M\)

Choose \(u=\delta_M\in\mathbb C^d\), which exists but is unseen by P. Then \(Pu=0\), so \(\Delta_MPu=0\).
Row \(M-1\) of \(P\Delta_du\) is nonzero because its forward neighbour in the base is M. Its value is 1 except at \((M,d)=(1,2)\), where both incidences reach coordinate 1 and its value is 2. The diagonal contributes zero since \(u_{M-1}=0\).

Thus \(P\Delta_du\ne0\) for every \(d>M\). Together with §6,
\[
\boxed{\Delta_MP=P\Delta_d\quad\Longleftrightarrow\quad d\mid M
\quad\text{for all }M,d\ge1.}
\]
This converse is analytic, not inferred from enumeration.

## 8. Complete classification of invariant images

An \(M\times d\) matrix has all columns in \(V_d\) iff its rows on each residue fibre agree. Hence invariance is equivalent to this fibre condition for \(\Delta_MP\). The checker uses precisely that criterion.

For \(d>M\), the image is all of \(\mathbb C^M\), so invariance is trivial. Divisor pairs are invariant by §6. Now assume \(1\le d\le M\), \(d\nmid M\), \(r=M\bmod d\ne0\), and compare same-fibre vertices 0 and d.

If \(M\ge d+2\), vertex d is interior:
\[
(\Delta_MPu)_0=u_1+u_{r-1}-2u_0,\qquad
(\Delta_MPu)_d=u_1+u_{d-1}-2u_0.
\]
Choosing \(u=\delta_{d-1}\) makes the outputs differ by \(-1\). They are not fibre-constant, so the image is not invariant.

If \(M=d+1\), both vertices are at the wrap:
\[
(\Delta_MPu)_0=-u_0+u_1,\qquad
(\Delta_MPu)_d=-u_0+u_{d-1}.
\]
For \(d>2\), choose \(u=\delta_1\); these differ. If \(d=2\), they agree for all u, and \(M=3\). Here the only repeated fibre is \(\{0,2\}\), and
\[
P(a,b)=(a,b,a),\qquad
\Delta_3P(a,b)=(b-a,\,2a-2b,\,b-a)\in V_2.
\]
All cases have now been exhausted:
\[
\boxed{V_d\text{ invariant under }\Delta_M
\quad\Longleftrightarrow\quad
d>M\ \text{or}\ d\mid M\ \text{or}\ (M,d)=(3,2).}
\]
Within \(1\le d\le M\), the last two alternatives are the complete classification. No attraction or nonlinear-stability conclusion is made.

## 9. The invariant exception is not intertwining

At \((3,2)\), the induced matrix in coordinates \((a,b)\) is
\[
K=\begin{pmatrix}-1&1\\2&-2\end{pmatrix},\qquad \Delta_3P=PK.
\]
This differs from the accepted \(\Delta_2=\begin{psmallmatrix}-2&2\\2&-2\end{psmallmatrix}\).
For \(u=(0,1)\), \(\Delta_3Pu=(1,-2,1)\) but \(P\Delta_2u=(2,-2,2)\).
Equivalently,
\[
\Delta_3P-P\Delta_2=\begin{pmatrix}1&-1\\0&0\\1&-1\end{pmatrix}\ne0.
\]
Invariance and intertwining with the prescribed base operator are distinct.

The nonsymmetry of K is consistent with self-adjointness of the restriction: these coordinates are not orthonormal. Their Gram matrix is \(G=P^\ast P=\operatorname{diag}(2,1)\), and
\(GK=K^\ast G=\begin{psmallmatrix}-2&2\\2&-2\end{psmallmatrix}\).
This observation does not extend A09 to nondivisor inputs.

## 10. A09: divisor isometry and orthogonal projection

Assume \(d\mid M\), \(q=M/d\). Each fibre has q entries, so
\[
P^\ast P=qI_d,\qquad Q=P/\sqrt q,\qquad Q^\ast Q=I_d,\qquad
\|Pu\|=\sqrt q\,\|u\|.
\]
The accepted Q is defined only under this divisor contract. Its entries are exact algebraic numbers, not necessarily integers. The positive square root fixes the normalization.

Let \(E=QQ^\ast=(1/q)PP^\ast\). Then \(E^\ast=E\), \(E^2=E\), and its image is \(V_d\), so it is the orthogonal projector onto \(V_d\). Explicitly,
\[
E_{n,m}=\frac1q\mathbf1_{\{n\bmod d=m\bmod d\}},\qquad
(Ef)_n=\frac1q\sum_{t=0}^{q-1}f_{r+td},\quad r=n\bmod d.
\]
The projector replaces each fibre by its arithmetic mean.

The factor \(\sqrt q\) compensates for repeated coordinates in squared norm. It is not a change to local nonlinear amplitudes, a new coupling, or a physical length conversion. For q=1, \(P=Q=I\).

## 11. Compression and degenerate bases

From intertwining, \(\Delta_MQ=Q\Delta_d\); multiplying by \(Q^\ast\) yields
\[
\boxed{Q^\ast\Delta_MQ=\Delta_d},\qquad
\boxed{P^\ast\Delta_MP=q\Delta_d}.
\]

For d=1, \(q=M\), \(P=\mathbf1_M\), \(Q=\mathbf1_M/\sqrt M\).
Since \(\Delta_M\mathbf1_M=0\), both compressions are the \(1\times1\) zero matrix, as required by \(\Delta_1=0\). The projector is \(\mathbf1_M\mathbf1_M^\ast/M\).

For d=2, \(M=2q\), and \(Pu=(a,b,a,b,\ldots)\). Each site's two incidences reach the opposite residue, so the output alternates \(2b-2a\) and \(2a-2b\). Thus
\[
Q^\ast\Delta_{2q}Q=\begin{pmatrix}-2&2\\2&-2\end{pmatrix},\qquad
P^\ast\Delta_{2q}P=q\begin{pmatrix}-2&2\\2&-2\end{pmatrix}.
\]
This includes q=1, where \(P=Q=I_2\).

As the closed Atlas-02 consistency specialization only,
\[
(M,d)=(12,3),\ q=4,\ Q=P/2,\quad
Q^\ast\Delta_{12}Q=L_3,\quad P^\ast\Delta_{12}P=4L_3.
\]
The C12 representation theory and normal-stability analysis are not repeated.

## 12. General divisor Fourier form

For \(d\mid M\), \(q=M/d\), and \(j'=0,\ldots,d-1\),
\[
(Pe_{j'}^{(d)})(n)
=\exp(2\pi ij'(n\bmod d)/d)
=\exp(2\pi i(qj')n/M)
=e_{qj'}^{(M)}(n).
\]
Removing a multiple of d changes the exponent by an integer multiple of \(2\pi i\).
The indices \(0,q,\ldots,(d-1)q\) are distinct modulo M, so these d orthogonal lifted modes span the d-dimensional image:
\[
V_d=\operatorname{span}_{\mathbb C}\{e_j^{(M)}:0\le j<M,\ q\mid j\}.
\]
Their eigenvalues agree:
\[
-4\sin^2(\pi qj'/M)=-4\sin^2(\pi j'/d).
\]
For normalized modes, \(Q(e_{j'}^{(d)}/\sqrt d)=e_{qj'}^{(M)}/\sqrt M\).

At d=1 only the constant mode occurs. At d=2, the constant and alternating modes map to indices 0 and \(q=M/2\); the latter is \((-1)^n\) on the even ring, with eigenvalue \(-4\). Degenerate incidence conventions are retained.

The checker corroborates these identities exactly in polynomial quotients by \(z^M-1\) and \(z^d-1\) for bounded sizes; it does not rely on approximate complex exponentials. The argument above is the all-size proof.

## 13. Graph-covering terminology boundary

For \(d\mid M\), \(d\ge3\), both cycles are ordinary simple cycles. Each vertex's two distinct neighbours map bijectively to the two distinct neighbours of its image. The residue map is surjective with q vertices per fibre, hence an ordinary q-sheet covering.

For d=1,2, use the loop/doubled-edge convention. Attach darts \((n,+),(n,-)\) at each vertex, with reversal
\((n,+)\leftrightarrow(n+1\bmod M,-)\).
The map \((n,\sigma)\mapsto(n\bmod d,\sigma)\) respects reversal under divisibility and is bijective on the two darts at each vertex.

At size 1 the two darts are the ends of a single loop, of degree two. At size 2 they describe two parallel undirected edges. Their incidence counts give the matrices already derived. The linear algebra remains valid regardless of whether one adopts multigraph terminology. No nondivisor residue map, including (3,2), is promoted to one of these coverings.

## 14. Retained nonlinear P-versus-Q boundary

This paragraph cites closed Atlas 02 §7; it is not a new A06 proof or reassessment. P is the exact nonlinear state pullback in the accepted divisor recurrence lift. Q is the Hilbert-space isometry for linear compression.

Atlas 02's counterexample takes \(\Omega=(1,0,0)\), \(\varepsilon=1\), \(g=\lambda=0\), \(k=0\), with \(Q=P/2\) for \(12\to3\):
\[
F_3(\Omega)=0,\qquad F_{12}(Q\Omega)=P(3/8,0,0)\ne0=QF_3(\Omega).
\]
Scaling changes the cubic amplitude. Linear compression does not authorize replacing P by Q in the recurrence. The authorized existing covering test file includes nonlinear regressions; running that file does not reopen the closed nonlinear proof.

## 15. Current implementation contract

| Property | Observed contract and verification |
|---|---|
| Positive sizes | Python operator.index protocol; zero and negative integers rejected |
| Bool handling | Built-in True and False explicitly rejected by isinstance(value, bool) |
| Nonintegers | Floats, including 1.0, strings and None rejected with ValueError; no truncation |
| Integer protocol | Custom __index__ object and SymPy Integer accepted; not restricted to one concrete integer type |
| Other scalar types | Behavior follows operator.index after the built-in bool check; no universal rejection claim for every third-party boolean-like object |
| Shapes | Δ: M×M; P and divisor Q: M×d |
| Representation | SymPy ImmutableDenseMatrix in this environment; exact integer Δ/P entries and exact algebraic Q entries |
| Dtypes | SymPy matrices have no NumPy dtype; no floating-point normalization is introduced |
| Fresh-object behavior | Repeated representative calls return distinct immutable objects; assignment raises TypeError; changing a mutable copy leaves the original unchanged |
| P | One entry 1 per row, other entries 0; no hidden normalization; d>M and nondivisor inputs accepted |
| Q | Both sizes validated, then divisibility gate; every audited nondivisor rejected with ValueError |
| Degenerate cycles | Additive incidence updates yield Δ1=0 and off-diagonal 2 at size 2 |

Fresh mutable construction is converted to an immutable result; there is no writable-array contract. The checker records actual object type, shape, identity separation and mutation isolation. Exact API parity is checked on all \(1\le M,d\le12\) after independent expectations are complete. The implementation file is hashed before and after loading.

## 16. Exact finite witnesses

The JSON witnesses object stores fully expanded \(\Delta_M,\Delta_d,P,P^\ast P,\Delta_MP,P\Delta_d\), residuals, and divisor Q/compression matrices for all seven pairs below. Block notation here gives compact explicit matrices.

### 16.1 Divisors

\[
P_{12,3}=\begin{pmatrix}I_3\\I_3\\I_3\\I_3\end{pmatrix},\quad
P^\ast P=4I_3,\ Q=P/2,\quad
P^\ast\Delta_{12}P=4\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
\]
\[
P_{6,2}=\begin{pmatrix}1&0\\0&1\\1&0\\0&1\\1&0\\0&1\end{pmatrix},
\quad P^\ast P=3I_2,\ Q=P/\sqrt3,\quad
P^\ast\Delta_6P=\begin{pmatrix}-6&6\\6&-6\end{pmatrix}.
\]
\[
P_{4,1}=\begin{pmatrix}1\\1\\1\\1\end{pmatrix},\quad
P^\ast P=[4],\ Q=P/2,\quad
\Delta_4P=P\Delta_1=0,\ Q^\ast\Delta_4Q=[0].
\]

### 16.2 Nondivisor (5,3)

\[
P=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\1&0&0\\0&1&0\end{pmatrix},
\quad P^\ast P=\operatorname{diag}(2,2,1),\quad
\Delta_5P-P\Delta_3=\begin{pmatrix}0&1&-1\\0&0&0\\0&0&0\\0&0&0\\1&0&-1\end{pmatrix}.
\]
For \(u=(0,0,1)\), \(Pu=(0,0,1,0,0)\) and
\(\Delta_5Pu=(0,1,-2,1,0)\). Equal input entries at indices 0 and 3 become unequal, showing noninvariance. \(W_3\) has dimension 1; \(V_3\) has dimension 3.

### 16.3 Invariant, nonintertwining (3,2)

\[
P=\begin{pmatrix}1&0\\0&1\\1&0\end{pmatrix},\quad
P^\ast P=\operatorname{diag}(2,1),\quad
\Delta_3P=\begin{pmatrix}-1&1\\2&-2\\-1&1\end{pmatrix},\quad
P\Delta_2=\begin{pmatrix}-2&2\\2&-2\\-2&2\end{pmatrix}.
\]
The induced matrix is K from §9, not \(\Delta_2\). Q is rejected.

### 16.4 Unseen coordinates

\[
P_{2,4}=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},
\quad P^\ast P=\operatorname{diag}(1,1,0,0),\quad
\Delta_2P-P\Delta_4=\begin{pmatrix}0&1&0&-1\\1&0&-1&0\end{pmatrix}.
\]
Here \(V_4=\mathbb C^2=W_4\), but \(P\delta_2=0\) and \(P\Delta_4\delta_2=(0,1)\ne0\). Rank is 2, nullity is 2.
\[
P_{1,2}=[1\ \ 0],\quad P^\ast P=\operatorname{diag}(1,0),\quad
\Delta_1P=[0\ \ 0],\quad P\Delta_2=[-2\ \ 2].
\]
Here \(V_2=\mathbb C\), rank 1, nullity 1, and \(P\Delta_2\delta_1=2\), retaining the repeated incidence.

| Pair | Rank | Nullity | Counts | V invariant? | Intertwines? | Accepted Q? |
|---|---:|---:|---|---|---|---|
| (12,3) | 3 | 0 | (4,4,4) | Yes | Yes | Yes |
| (6,2) | 2 | 0 | (3,3) | Yes | Yes | Yes |
| (5,3) | 3 | 0 | (2,2,1) | No | No | No |
| (3,2) | 2 | 0 | (2,1) | Yes | No | No |
| (2,4) | 2 | 2 | (1,1,0,0) | Yes, whole space | No | No |
| (1,2) | 1 | 1 | (1,0) | Yes, whole space | No | No |
| (4,1) | 1 | 0 | (4) | Yes | Yes | Yes |

## 17. Independent checker and finite evidence

The checker forms a forward-difference matrix \(B=S-I\) and \(\Delta=-B^\ast B\), independently of the production neighbour-addition loop. P is constructed by stacking identity blocks and a partial block, independently of the production row-assignment loop. All independent expectations and mathematical checks precede the explicit file import of covering.py.

| Group | Searchable named records |
|---|---|
| EXACT_CYCLE_LAPLACIAN | matrix_M1, matrix_M2, matrix_M3, matrix_M4, degenerate_spectra, structure_dirichlet |
| EXACT_PULLBACK_STRUCTURE | rank_nullity_gram, shift_fixed |
| EXACT_INTERTWINING | intertwining_iff_divisor, boundary_witness |
| EXACT_INVARIANCE | invariance_classification, invariance_boundary_witness, exception_3_2_induced_operator |
| EXACT_ISOMETRY_COMPRESSION | isometry_projection_compression, 12_3_consistency |
| FOURIER | root_of_unity_eigenvectors, divisor_mode_pullback, degenerate_base_modes |
| API_PARITY | independent_exact_expectations, integer_protocol_and_builtin_bool_handling, exact_immutable_fresh_matrices, source_content_unchanged_during_import |
| FALSIFIERS | 5_3_image_not_shift_fixed_and_not_invariant, 2_4_whole_image_but_no_intertwining, simple_edge_changes_6_2_intertwining, nonuniform_global_normalization_fails |
| INTEGRITY | expected_head, external_paths_and_no_bytecode, integrity_receipt, test_receipt, packaging_receipt |

The bounded domain is \(1\le M,d\le12\), 144 ordered pairs; branch-specific properties apply only under their stated hypotheses. Divisor checks use the divisor subset. The structure audit covers 12 sizes. The 144 count is the enclosing domain, not the eligible count for every branch. These records are explicitly FINITE_AUDIT, not universal proofs or theorem counts.

The invariance test checks same-fibre row equality in \(\Delta_MP\). It does not use the invalid shortcut \(P^+P=I\), which merely tests full column rank and would pass at noninvariant (5,3). There is no pseudoinverse tolerance.

The Fourier audit checks polynomial residuals modulo \(z^M-1\), and pullback residuals modulo \(z^d-1\). For each bounded size this is an exact identity at all corresponding roots. The universal conclusions belong to the analytic arguments in §§1–13.

## 18. Packaging, execution and separate receipts

Environment: conda torment; Python 3.11.15; SymPy 1.14.0. Bytecode writing is disabled with -B. The checker requires --output and --scratch, resolves them externally, rejects an existing output, and uses fresh external cache/temp directories. --repo is explicit or uses the documented authoritative default. It never derives output locations from the checker file's own directory.

Example mathematical/API rerun using new unused destinations:

~~~powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_LANE1_SUPPLEMENT_A_GENERAL_CYCLE_PULLBACK_CHECKS.py --repo C:\TORMENT\TRIOCTAGON_new\trioctagon-physics --output C:\Users\Notandi\.codex\reports\supplement_a_new_run.json --scratch C:\Users\Notandi\AppData\Local\Temp\supplement_a_new_run
~~~

Without receipts such a run may pass mathematics/API checks but deliberately reports HOLD_PENDING_RECEIPTS_OR_FAILURE for closeout readiness. The final run supplies separate --test-receipt, --packaging-receipt and --integrity-receipt inputs.

To generate a new integrity receipt after mathematical/API checking, also provide --fingerprint-before, --external-before and --git-before task-start manifests. The checker performs full after fingerprints and writes the external receipt plus after manifest with exclusive-create semantics. It can alternatively ingest an existing integrity receipt. Each receipt and SHA256 is embedded in the results; these are local audit records, not cryptographic signatures.

The final checker passed all **31 check records**, with **closeout_ready=true**. A count was not chosen as a target; it is the number of emitted records after the required coverage and receipts were implemented.

The final checker also ran successfully from an external read-only relocated file, with output and scratch elsewhere. Its original and relocated content hashes match. Nine packaging checks passed: missing output, missing scratch, protected output, protected scratch, bytecode-enabled invocation, successful relocation, existing-output refusal, preservation of existing output bytes, and unchanged relocation directory.

Only S2 was executed as an existing repository test: **10 passed, 40 subtests passed; exit 0; stderr empty**. Pytest plugin autoload and its cache provider were disabled. --basetemp and temporary/cache environment variables pointed externally. The test file contains both linear and nonlinear regressions; no broad suite or Paper-A support audit was run.

All task receipts and raw logs are under:

C:\Users\Notandi\AppData\Local\Temp\trioctagon_supplement_a_20260929_35892fb603

The results embed the compact receipts, so their content remains reviewable without opening the raw 38 MB full-tree inventories.

## 19. Claim-to-owner closeout

| Owner | Omission in prior completeness review | Sections closing it | Independent corroboration |
|---|---|---|---|
| A07 | Positive-size cycle domain, particularly multiplicity at sizes 1/2 | §§1–2: matrices, spectra, Dirichlet identity, self-adjointness and kernel; §13: graph boundary | matrix_M1/M2/M3/M4; degenerate_spectra; structure_dirichlet; degenerate_base_modes; simple_edge_changes_6_2_intertwining; API parity |
| A08 | All-positive M,d and d>M rank/noninjectivity | §§3–4: rank, kernel, nullity and counts; §16 unseen-coordinate examples | rank_nullity_gram; boundary_witness; 2_4_whole_image_but_no_intertwining; API parity |
| A08 | Nondivisor wrap converse | §§6–7: analytic iff proof, split into d≤M and d>M | intertwining_iff_divisor; boundary_witness; exact witness residuals |
| A08 | Image versus cyclic shift-fixed space | §5: orbit dimension, restricted equality criterion and d>M distinction | shift_fixed; (5,3) and (2,4) falsifiers |
| A08 | Exceptional invariant (3,2) without intertwining | §§8–9: complete invariance proof and induced K≠Δ2 | invariance_classification; invariance_boundary_witness; exception_3_2_induced_operator |
| A09 | General divisor normalization/compression, degenerate bases included | §§4,10–12: exact normalization domain, norms, projector, compression and Fourier map | isometry_projection_compression; nonuniform_global_normalization_fails; degenerate_base_modes; divisor_mode_pullback; API divisor gate; 12_3_consistency |
| A09 | Retain already-closed cubic P/Q boundary | §14 quotes Atlas 02's existing exact counterexample | Closed S10 §7 retained, no new nonlinear proof claimed |

~~~text
A07 = FULL
A08 = FULL
A09 = FULL
~~~

These are the supplement's coverage determinations, supported by the analytic proofs and passing exact/API/test/integrity evidence. No other ledger row is reassessed. The old review and crosswalk are retained unchanged, and the supplement is not Atlas 10 or a publication.

## 20. Integrity record

Full fingerprints include every regular-file relative path and SHA256 content under each root. Only .git internal paths are excluded; Git HEAD and tracked status are separately captured using optional locks disabled. Equal manifests establish unchanged file/path sets as well as unchanged contents.

| Tree | Files before/after | Matching SHA256 of canonical path→content-hash map |
|---|---:|---|
| Current repository | 7,803 / 7,803 | eb913f8b685be59b18ed9cbf1656b06e3d7dcb617b6579e3ec60fc27753dc1df |
| Old kernel_TO | 401 / 401 | cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd |
| TORMENT production kernel subtree | 64 / 64 | 8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41 |
| Full TORMENT production checkout | 173,908 / 173,908 | 3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4 |

The production kernel subtree is intentionally also included in the full checkout. Root paths and complete manifests are recorded in the integrity receipt. The current repository fingerprint includes all Papers A–F and the published Atlas tree. Separately, all 27 external prior Atlas files and all four completeness-review deliverables have matching before/after fingerprints. Git HEAD and tracked status match for current and production repositories.

~~~text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
PAPERS_A_F_CHANGED = NO
PRIOR_ATLAS_CHANGED = NO
COMPLETENESS_REVIEW_CHANGED = NO
COMMITS = 0
PUSHES = 0
PUBLICATION = NO
~~~

The task stops with these three external deliverables. No source, paper or prior record was patched.
