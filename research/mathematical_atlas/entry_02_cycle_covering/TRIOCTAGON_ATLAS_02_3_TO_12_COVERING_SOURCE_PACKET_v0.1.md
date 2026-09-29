# TriOctagon Mathematical Atlas — Entry 02
# 3 → 12 cycle covering: source packet v0.1

Date: 2026-09-29. Mode: read-only reconstruction and independent exact checks. Current authority: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, frozen at `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`.

**The current construction is a four-sheeted graph covering `C12 → C3`, together with a state pullback `C³ → C¹²` that repeats a three-component vector four times.** The ring Laplacian and the specified nonlinear ring map restrict exactly to the three-node model on that repeated-coordinate sector. The construction does not assert that a triangle is a subgraph of the twelve-cycle or that the entire twelve-state system is globally attracted to that sector.

This is an Atlas source packet, not a replacement manuscript. It uses the accepted publication and current code; earlier support documents supply context only where consistent with that authority. Atlas 01 remains closed. Its provenance investigation and correction queue are not reopened or applied.

## 1. Source and notation crosswalk

| Source | Role in this packet | Exact locator |
|---|---|---|
| A01 `covering.py` | Current matrix definitions | `cycle_laplacian`, `pullback_matrix`, `isometric_pullback` |
| A02 `dynamics.py` | Current nonlinear map and zero convention | `L3`, `arg0`, `phase_sync`, `_advance`, `step3`, `step_ring` |
| A03 accepted Paper A | Analytic authority and scope | §§2–6; §7.1 real deck decomposition; §§7–8 stability limits; §12 limitations |
| A04 proof audit; A05 current covering tests | Existing verification evidence | Compression, Fourier/deck and reduction checks; not rerun as repository tests here |
| A06 accepted Paper F | Real transverse plane/basis | §2 eq. (6), lines 67–76 |
| A07/A08 reconstruction and verification | Supporting derivations/data | Covering tower; independent normal-stability methodology and numerical evidence |
| A09/A10 existing verification code/oracle | Definition comparison | Read as source, not imported or executed |
| H01–H03 historical code/documents | Bounded comparison lane | Old 12-sector clock; explicit old 15°/24-node and dodecagon motifs |

Absolute links and byte hashes for all these identifiers appear in §13 and in the JSON results. In formulas, `*` means Hermitian adjoint. Standard Euclidean/Hermitian inner products are used, without division by the number of sites.

Here **Q means the covering isometry P/2**. It is not Atlas 01's base-space transverse projector `I−eeᵀ/3`. We call that projector `Π_base`. Fourier vectors are denoted `f_j`; Paper A calls them `e_j`. They must not be confused with coordinate unit vectors `δ_n`.

## 2. The two graphs, the residue map and four sheets

For N=3 or 12, `C_N` is the undirected simple graph with vertex set `Z_N={0,…,N−1}` and edges `{n,n+1 mod N}`. Each vertex has two distinct neighbors, `n−1` and `n+1` modulo N. In particular, `C3` has the three edges `{0,1}`, `{1,2}`, `{2,0}`: it is exactly the triangle `K3`.

The sign convention is the **negative-semidefinite** cycle Laplacian:

`(Δ_N f)(n)=f(n+1)+f(n−1)−2f(n)`.

Equivalently `Δ_N=A_N−2I`, or `−B_N B_Nᵀ` using an oriented incidence matrix B. This is the negative of the positive-semidefinite graph Laplacian convention `D−A`. A01 implements this same convention, retaining incidence multiplicity for its additional N=1,2 cases; those degenerate cases are not needed for this entry.

Define the graph map and its contravariant state map:

`p:Z_12 → Z_3,  p(n)=n mod 3`,

`P:C³ → C¹²,  (PΩ)_n=Ω_(n mod 3)`.

The graph arrow points **12 → 3**; the pullback of functions points **3 → 12**. In increasing site order,

`P(a,b,c)ᵀ=(a,b,c, a,b,c, a,b,c, a,b,c)ᵀ`,

so P is the 12×3 matrix consisting of four vertically stacked `I3` blocks.

At any n, the two neighbors project to `(p(n)−1) mod3` and `(p(n)+1) mod3`, which are the two distinct neighbors of p(n). This includes the wrap: at n=0, sites 11 and 1 project to 2 and 1; at n=11, sites 10 and 0 project to 1 and 0. Thus p is a graph homomorphism **locally bijective on neighborhoods**, the covering property. [A03 §4.1, line 120.]

| Base node r | Fiber `p⁻¹(r)` | Pullback value at all four sites |
|---|---|---|
| 0 | `{0,3,6,9}` | a |
| 1 | `{1,4,7,10}` | b |
| 2 | `{2,5,8,11}` | c |

Every base node has **four preimages**. This, and not the number of base nodes, is the sheet count. Write a ring site uniquely as `n=r+3ℓ`, `r∈{0,1,2}`, `ℓ∈{0,1,2,3}`. Moving forward gives

`(0,ℓ)→(1,ℓ)→(2,ℓ)→(0,ℓ+1 mod4)`.

A complete traversal of the base triangle moves a lifted path to the next sheet; four such traversals return it to its starting ring site. Consequently this is one connected 12-cycle, not four disconnected triangle copies. As an independent check, `trace(A12³)=0`: the ring contains no triangle subgraph.

An optional regular-polygon vertex drawing makes the angles explicit. Set `z_n=exp(2πin/12)`. Then `z_n⁴=exp(2πi p(n)/3)`. This is a concrete vertex realization of the map. It is a chosen Euclidean drawing of an abstract graph; no physical length, spatial embedding of the kernel, or historical angular construction is implied.

## 3. Deriving `Δ12 P = P Δ3` and `Δ3=L3`

For any Ω∈C³ and r=n mod3,

```
(Δ12 PΩ)_n
  = Ω_((n+1 mod12) mod3) + Ω_((n−1 mod12) mod3) − 2Ω_r
  = Ω_((r+1) mod3) + Ω_((r−1) mod3) − 2Ω_r
  = (Δ3 Ω)_r
  = (P Δ3 Ω)_n.
```

The second equality uses `3 | 12`, so taking the ring wrap does not change the residue modulo three. Since this holds at every site for every Ω, it is an operator identity.

On C3 the two neighbors of r are all the other vertices. Therefore

```
Δ3 = [ −2   1   1 ]
     [  1  −2   1 ] = eeᵀ − 3I = L3,   e=(1,1,1)ᵀ.
     [  1   1  −2 ]
```

It follows that `L3 e=0` and `L3 w=−3w` whenever `eᵀw=0`. Its spectrum is `0,−3,−3`. On the lifted sector, Δ12 has exactly this matrix in the orthonormal residue basis constructed below; it does not acquire a factor four in its eigenvalues. [A01; A02 line 12; A03 §§2–3.]

The same residue argument works for `C_(3q)→C3` for every positive integer q. Thus twelve is a valid realization and the size studied in the accepted normal-stability work; this proof does not privilege twelve among all multiples of three. [A03 §§6.2,12.]

## 4. Deck group, base symmetry and full ring symmetry

A **deck transformation** is a graph automorphism τ of C12 with `p∘τ=p`: it moves vertices within fibers and acts trivially on base labels.

Every C12 automorphism has the form `n→n+a` or `n→a−n` modulo12. This follows by choosing the image of vertex 0 (12 choices) and then which of its two neighbors is the image of vertex 1; adjacency fixes all subsequent images.

For rotations, `p(n+a)=p(n)` for all n iff `a≡0 mod3`. A reflection would need `a−n≡n mod3` for every n: n=0 requires a≡0, while n=1 then requires −1≡1 mod3, impossible. Hence

`Deck(p)={id,+3,+6,+9}=⟨+3⟩ ≅ Z4`.

Translation by three has order four, acts freely, and cycles through every fiber. This makes the cover regular, and the graph quotient is `C12/Deck(p)≅C3`. [A03 §4.2.]

| Group/action | Size | What it does |
|---|---:|---|
| Base rotations `Z3` | 3 | Permute base labels cyclically |
| Full base automorphisms `D3≅S3` | 6 | All permutations of the triangle; preserve L3 |
| Deck group `⟨+3⟩≅Z4` | 4 | Permute the four copies of each base node, leaving its label fixed |
| Full ring automorphisms `D12` in Paper A's convention | 24 | Twelve rotations and twelve reflections of C12 |

Let `R:n→n+1` and `K:n→−n`. Then `R¹²=K²=id`, `KRK=R⁻¹`, and the map to base permutations sends `R→(0 1 2)`, `K→(1 2)`. Its kernel is the deck group and its image is all S3:

`1 → Z4 → D12 → S3 → 1`.

The one-step ring rotation R has order twelve but induces a base rotation of order three. Separately `R⁴`, of order three, also induces the base +1 rotation because 4≡1 mod3. It is not a deck transformation. In a regular twelve-gon drawing, R is 30°, R³ (the deck generator) is 90°, and R⁴ is 120°. These are different actions. [A03 §§5, lines 158–160.]

This table describes graph/Laplacian symmetries. The **fixed-parameter nonlinear map** need not have all of them: unequal three-periodic k preserves the deck group but generally breaks a one-site rotation and some reflections. Base S3 and full ring D12 become fixed-parameter symmetries when k and other site data are invariant under those permutations; otherwise they describe covariance when parameters are permuted as well. The exact checks include a concrete unequal-k counterexample to full rotation symmetry.

## 5. `V3=im(P)`: coordinates, basis and projection

```
V3 = {(a,b,c,a,b,c,a,b,c,a,b,c) : a,b,c∈C}
   = {f∈C¹² : f(n+3)=f(n) for every n}
   = Fix(T),   (Tf)(n)=f(n+3 mod12).
```

It has **complex dimension three**, hence real dimension six. Its real-valued part has real dimension three. “Three-periodic” means period dividing three; constant functions are included.

For r=0,1,2 let `b_r=δ_r+δ_(r+3)+δ_(r+6)+δ_(r+9)`. These are the three columns of P, disjoint residue indicators. Thus

`⟨b_r,b_s⟩=4δ_rs`.

They are an orthogonal basis; `b_r/2` is an orthonormal basis. The orthogonal projection Π onto V3 is

`Π=PP*/4=QQ*`,

`(Πf)_(r+3ℓ)=(f_r+f_(r+3)+f_(r+6)+f_(r+9))/4`.

It averages **within each residue fiber**, not across all twelve sites. The inverse of P on V3 extracts a,b,c; it also equals `P*/4` there. P is a bijection C³→V3, not onto all of C¹². A general off-sector state has information discarded by this fiber average.

## 6. Fourier reconstruction and the Paper F connection

Define the unnormalized C12 Fourier modes

`f_j(n)=exp(2πijn/12), j=0,…,11`.

The geometric series gives `⟨f_j,f_k⟩=12δ_jk`, so these twelve vectors form an orthogonal basis. Direct neighbor substitution gives

`Δ12 f_j = [exp(2πij/12)+exp(−2πij/12)−2] f_j`

`             = −4 sin²(πj/12) f_j`.

The deck generator satisfies

`T f_j(n)=f_j(n+3)=exp(πij/2) f_j(n)=i^j f_j(n)`.

Thus a mode is deck-fixed exactly when `i^j=1`, i.e. `j≡0 mod4`. Therefore

`V3=span_C{f_0,f_4,f_8}`.

No other modes enter: they have a nontrivial deck character. This also proves that V3 is the complexification of its real-valued repeated-coordinate subspace. [A03 §5.]

For the base let `ω=exp(2πi/3)` and let its modes be

`h̃0=(1,1,1)`, `h̃1=(1,ω,ω²)`, `h̃2=(1,ω²,ω)`.

Then `P h̃0=f0`, `P h̃1=f4`, `P h̃2=f8`. The common mode has eigenvalue 0; the two base transverse modes, each with zero coordinate sum, have eigenvalue −3. Their lifted modes also have eigenvalue −3.

Paper F uses the **real** plane `V=e⊥⊂R³` and basis

`u=(1,−1,0)/sqrt2`, `v=(1,1,−2)/sqrt6`.

These satisfy `u·v=0`, `||u||=||v||=1`, `u×v=e/sqrt3`. Let the normalized transverse Fourier vector be `h1=h̃1/sqrt3`, and set

`a=(sqrt3−i)/(2sqrt2)`.

Then exactly

`h1=a(u+i v)`, `h2=conjugate(h1)=conjugate(a)(u−i v)`.

This is a unitary change of complex basis, not a new geometric sector. Consequently:

- The common base complex line is `C e` (one complex/two real dimensions).
- The base transverse complex plane is `span_C{u,v}=span_C{h1,h2}` (two complex/four real dimensions).
- Paper F's plane V itself is two-dimensional **over R**. For general complex perturbations, both real and imaginary parts can lie in it.
- Under Q, `Q(e/sqrt3)`, Qu and Qv are orthonormal and lie inside V3. Qu,Qv span the real lifted base-transverse plane; f4,f8 span its complexification.

**These base-transverse directions are tangential to the lifted three-state sector. They are not the normal directions from V3 into the other nine complex dimensions of C12.** This resolves the two different uses of “transverse” in Paper F and Paper A.

## 7. Why `Q=P/sqrt4=P/2` is an isometry

Each coordinate is repeated four times, so

`||PΩ||²=4||Ω||²`, `P*P=4I3`.

Set `Q=P/2`. Then

`Q*Q=I3`,

`Q*Δ12Q=(P*/2)Δ12(P/2)=(1/4)P*PΔ3=Δ3=L3`.

The unscaled compression is `P*Δ12P=4L3`. The scaled basis removes the redundant fourfold counting in the inner product; it does not alter the restricted operator's eigenvalues or require a new coupling g.

The factor 2 is the square root of the **fiber size**. It is not a two-sheet cover, a length conversion, a physical amplification law, a new geometric dimension, or a dynamical phase harmonic. With normalized Fourier vectors, `Q(h̃_j/sqrt3)=f_(4j)/sqrt12`.

The linear isometry Q and nonlinear pullback P serve different purposes. In general `F12(QΩ)≠QF3(Ω)` with the same cubic coefficients, because Q changes each local amplitude by 1/2. An exact counterexample is `Ω=(1,0,0)`, ε=1, g=λ=0, k=0. Then `F3(Ω)=0`, while `F12(QΩ)=P(3/8,0,0)≠0`. Q is the correct normalized linear basis, whereas the accepted nonlinear identity uses P.

## 8. Nonlinear intertwining, stage by stage

Use the fixed finite real parameters ε,g,λ and base triple `k^(3)=(k0,k1,k2)`. Define `k^(12)=P k^(3)`; this need not be a constant triple. All sites use the same functional rule and the same parameters ε,g,λ.

The adopted ring map has a pre-sync step

`A_N(z)_n=z_n+ε z_n(k_n−abs(z_n)²)+g(Δ_N z)_n`,

followed by S_N. With `w=A_N(z)`, set

`r_n=abs(w_n)`, `p_n=Arg0(w_n)`,

`H_n=sin(3(p_(n−1)−p_n))+sin(3(p_(n+1)−p_n))`,

`(S_N w)_n=r_n exp(i[p_n+λH_n])`.

Neighbors wrap modulo N. All p and H values are taken from the **same pre-sync state**, so the update is simultaneous. `Arg0(z)=arg(z)` for z≠0 and `Arg0(0)=0`. At λ=0 the implementation directly defines S_N as the identity. These are the current adopted formulas; their historical harmonic selection is outside this entry. [A02; A03 §6.1.]

For z=PΩ, each componentwise factor repeats:

`abs(PΩ)²=P(abs(Ω)²)`,

`(PΩ)⊙(Pk−abs(PΩ)²)=P[Ω⊙(k−abs(Ω)²)]`.

Together with the linear identity already proved,

`A12(PΩ)=P A3(Ω)`.

Let `w=A3(Ω)`. Its lifted copy has identical amplitudes and identical Arg0 values within every fiber. At site n, the two ring neighbors represent exactly the two other base nodes. Therefore

`H12(Arg0(Pw))=P H3(Arg0(w))`,

and the componentwise exponential reconstruction gives

`S12(Pw)=P S3(w)`.

Composing these equalities proves

**`F12(PΩ)=P F3(Ω)` for every Ω∈C³ under these definitions.**

The result identifies the three-node map with the restriction of F12 to V3. It neither reconstructs general off-sector ring states from three numbers nor says the complement evolves independently under the nonlinear map.

### Conditions, edge cases and explicit limits

| Ingredient | Required compatibility for this construction | What the exact checks establish |
|---|---|---|
| Onsite map | Same pointwise cubic at corresponding sites; same ε | Polynomial identity in six arbitrary real base coordinates and symbolic ε,g,k |
| Site coefficients | `k12=Pk3`, including the wrap | Unequal entries within the base triple are allowed; a nonperiodic k can break sector invariance |
| Graph coupling | Cycle nearest neighbors, same g, covering local bijection | Exact matrix identity, including n=0 and 11 |
| Phase synchronizer | Same adopted law and λ; two ring neighbors; simultaneous update | Symbolic phase-field and reconstruction identities |
| Zeros | Identical deterministic Arg0 at corresponding copies | All eight possible zero/nonzero support masks preserve the expression identity; copy-dependent zero phases can break it |
| λ=0 | S is directly identity | No phase extraction/reconstruction is needed |
| Arithmetic | Exact field operations for the theorem | Floating-point evaluation remains subject to rounding/overflow; no indefinite trajectory-closeness claim |

For a **zero pre-sync amplitude**, its phase is conventionally 0 and its own output is 0. Its assigned phase still enters its nonzero neighbors' increments, so the shared zero convention matters. It preserves the lift algebra without making the map differentiable there. For λ≠0 the extension is generally discontinuous at zero pre-sync components; derivative/Floquet analysis is restricted to orbits avoiding them. Source `arg0` treats every exact complex zero identically, including signed IEEE zeros. [A03 lines 182–186 and Appendix B.3.]

The supplied falsifiers distinguish necessary features of the stated theorem from arbitrary modifications:

- An unweighted all-pairs phase sum over **twelve** sites produces four times the base drift on a lifted state. The current ring is nearest-neighbor, with no extra division by four.
- A sequential phase sweep changes the map. With initial base phases `(0,π/6,0)` and λ=π/6, a left-to-right ring sweep fails both the lift equality and three-periodicity.
- Taking k nonperiodic can break the lift already in the onsite step.
- Replacing P by Q with otherwise unchanged parameters fails for the cubic counterexample in §7.
- Assigning a different artificial phase to one zero copy can make neighboring nonzero copies disagree.

These are concrete counterexamples, not a claim that every violation must fail for every degenerate parameter/state. For example k is irrelevant when ε=0. The packet establishes the current sufficient structural conditions and does not attempt a classification of all accidental equalities or compensating alternative models.

## 9. The complement: all missing directions

The orthogonal complement is

`W=V3⊥={z∈C¹² : Σ_(ℓ=0)^3 z_(r+3ℓ)=0 for r=0,1,2}`.

These are three independent complex constraints, so `dim_C W=9`, `dim_R W=18`. Every state splits uniquely as `z=Πz+(I−Π)z`. The normal deviation `(I−Π)z` measures disagreement among copies of each base coordinate; it is not the base plane `e⊥`.

In sheet coordinates `n=r+3ℓ`, an explicit orthonormal basis of the fiber-zero-sum space uses

`b2=(1,−1,1,−1)/2`,

`bc=(1,0,−1,0)/sqrt2`, `bs=(0,1,0,−1)/sqrt2`.

For each r, place any one of these four-entry vectors on its fiber and zero on the other two fibers. The resulting nine vectors form a complex orthonormal basis of W. Their real and imaginary copies form an 18-vector real basis.

Equivalently W is spanned by Fourier modes `j∈{1,2,3,5,6,7,9,10,11}`:

| j | Laplacian eigenvalue μ_j | Deck eigenvalue i^j | Accepted real block |
|---:|---|---|---|
| 0 | 0 | 1 | U0 |
| 1 | −2+sqrt3 | i | U13 |
| 2 | −1 | −1 | U2 |
| 3 | −2 | −i | U13 |
| 4 | −3 | 1 | U0 |
| 5 | −2−sqrt3 | i | U13 |
| 6 | −4 | −1 | U2 |
| 7 | −2−sqrt3 | −i | U13 |
| 8 | −3 | 1 | U0 |
| 9 | −2 | i | U13 |
| 10 | −1 | −1 | U2 |
| 11 | −2+sqrt3 | −i | U13 |

This is the exact Laplacian spectrum, not the full nonlinear Jacobian spectrum. The nonlinear onsite derivative depends on the state and the phase-stage derivative contributes additional factors.

## 10. Accepted real deck-character decomposition and stability scope

Identify C¹² with R²⁴, using coordinates `(x0,…,x11,y0,…,y11)`. Realify the deck shift as `T_R=diag(T,T)` and define

`E0=(I+T_R+T_R²+T_R³)/4`,

`E2=(I−T_R+T_R²−T_R³)/4`,

`E13=I−E0−E2=(I−T_R²)/2`.

They are mutually orthogonal symmetric projections, with ranks 6,6,12. Thus

`R²⁴=U0 ⊕ U2 ⊕ U13`, `U_a=range(E_a)`.

| Block | Real dimension | Meaning |
|---|---:|---|
| U0 | 6 | Realification of V3, tangent to the lifted three-state dynamics; fixed by T_R |
| U2 | 6 | Normal directions with shift-by-three sign reversal; underlying Fourier indices 2,6,10 |
| U13 | 12 | Remaining normal directions; shift by six reverses sign; indices 1,3,5,7,9,11 |

The two non-real deck characters i and −i are separate eigenspaces for the complex-linear Laplacian. The **full derivative is real-linear**, since the cubic term depends on complex conjugates. It need not preserve those two physical-complex eigenspaces separately. Their real isotypic combination U13 is the accepted normal block. For example, at the all-ones state with k=(1,1,1), ε=1/20 and g=λ=0,

`D F(h)=(19/20)h−(1/20)conjugate(h)`.

A unit i-character vector therefore produces a −i-character component of norm 1/20. The exact script verifies this without numerical tolerance. This does not contradict commuting with the real deck action; it shows why complex-linearity must not be assumed. [A03 §7.1.]

Why do the real blocks decouple to first order? Three-periodic k and site-independent update rules imply **global deck equivariance** `F12(Tz)=T F12(z)`, even off V3. At a smooth on-sector state x, Tx=x, differentiation gives

`DF12(x) T_R = T_R DF12(x)`.

Hence DF commutes with the three real projectors and preserves their ranges. Merely knowing that V3 is invariant would not prove absence of normal-to-tangent coupling; equivariance supplies that stronger result. The checks establish exact off-sector deck equivariance separately for the polynomial and phase stages, and verify a symbolic homogeneous-state Jacobian as an additional illustration.

For that homogeneous special case, the independent exact Jacobian blocks are

`J_rad=(1−2ε)I+gΔ12`,

`J_phase=(I+3λΔ12)(I+gΔ12)`.

This check uses k=(1,1,1) and Ω=(1,…,1). It does not stand in for Paper A's heterogeneous canonical-k numerical atlas.

For a fixed point, the normal spectral radius comes from the restriction of J to `U2⊕U13`. For a period-p orbit it comes from the **p-step normal monodromy product**, with per-step factor `ρ_perp^(1/p)`. A radius below one gives exponential decay of the normal variational dynamics; above one gives linear transverse instability; equal to one is inconclusive about nonlinear attraction. Spectral radius below one does not require Euclidean operator norm below one or rule out transient growth.

Paper A §§7–8 reports local/regional stable and unstable cases and direct perturbation evidence. For example its default fixed regime has `ρ_perp≈0.948919213`, while a period-two regime has `ρ_perp≈0.991295319`; it also reports fixed and periodic unstable cases. These are **quoted existing source results**, not newly regenerated Floquet values. No global basin or attraction claim follows. An exact simple falsifier is ε=λ=0,g=1: the normal j=6 mode is multiplied by −3 each step, although the lifted sector remains exactly invariant.

## 11. Historical comparison lane — no retrofitted equivalence

Classification vocabulary in this lane is restricted to the work order's five statuses. `HISTORICAL_PRECURSOR` means an older documented motif, not a proven causal design path to the 2026 covering construction. The current paper explicitly dates the ring extension as a new mathematical construction and disclaims a historical M-ring design claim. [A03 §12, line 374.]

| Comparison | Classification | Source/evidence | Relationship and limit |
|---|---|---|---|
| Current `3×4=12` | EXACT_CURRENT_MATH | Fiber table and P above; A03 §4 | Three base coordinates × four copies. Four is the sheet count; this equality is derived directly from p. |
| Earlier `3×4=12` intuition as the reason for the current realization | OPEN | Motif supplied in the work order; no explicit earlier covering map established in this lane | Numerical factorization alone does not document the historical choice or identify old geometric objects with fibers. |
| Old 12-sector clock | HISTORICAL_PRECURSOR | H01 lines 42–44, 164–166, 183 | `d24_steps=12`, index advanced modulo12, angle `2π index/12`. This is a single evolving clock label, not a twelve-component spatial state. |
| Clock index set Z12 versus current ring vertices Z12 | STRUCTURAL_ANALOGY | H01 and A03 | The finite cyclic labels can be matched as sets/groups, but that does not supply twelve site amplitudes, the ring Laplacian, P, or a dynamical equivalence. |
| Old 15°/24-node lattice versus current C12 | STRUCTURAL_ANALOGY | H02 pp. 3–4 and Appendix C p. 24 | The old explicit formula uses `ϑ_k=ϑ0+πk/12`, k∈Z24. A regular C12 drawing has 30° steps. Node counts and actions must be specified before comparing them. |
| Three 120° arms versus base C3 and deck Z4 | STRUCTURAL_ANALOGY | H02 Appendix C pp. 24–25 | The 120° motif resembles a threefold orientation. In the current ring drawing, a 120° shift is R⁴ and induces a base rotation; the deck generator R³ is 90° and stays within fibers. No old-arm-to-fiber identification is established. |
| D24 name versus Paper A's D12 of order24 | COINCIDENCE | H02; H03 p. 5; A03 §5 | The numeral/name alone cannot identify the action. H03 explicitly discusses a dodecagon with 12 rotations; H02 discusses a 24-node/15° circle. This packet uses explicit node counts, generators and group orders, without applying a correction to either document. |
| Old dodecagon symmetry as an abstract graph action | STRUCTURAL_ANALOGY | H03 p. 5 and current R,K | Once the same twelve-cycle is explicitly chosen, both have the abstract dihedral action with 12 rotations and 12 reflections. That group-level identification does not identify old state variables or dynamics with the current covering map. |
| Current tower `C24→C12→C3` | EXACT_CURRENT_MATH | A07 diagram; independent exact composition check | Explicit maps n mod12 and n mod3 compose to n mod3; the pullback matrices compose correspondingly. This is an available abstract covering construction. |
| Identifying the old D24 physical/geometric object with that tower's C24 | OPEN | No complete state/edge/dynamics map supplied by H02 to the accepted F12 construction | Having an explicit abstract tower does not prove that the historical angular/perimeter geometry realizes it. No old source is retrofitted. |

The historical lane intentionally does not evaluate the old weighting arithmetic, repair documents, infer physical interpretations, or revisit harmonic-three provenance.

## 12. Independent exact verification and how to reproduce it

Deliverables:

- [TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py>)
- [TRIOCTAGON_ATLAS_02_EXACT_RESULTS.json](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_02_EXACT_RESULTS.json>)

The script builds the Laplacians independently as negative incidence Gram matrices, P as a block repetition matrix, Fourier vectors using exact roots of unity, and the real projectors from the deck shift. It does not import `kernel_physics`, the old kernel, production modules, or existing verification scripts. Source files are read only for hashes and a static AST comparison of the L3 literal. All mathematical checks use exact SymPy expressions; there are no floating tolerances or Monte Carlo assertions.

**Result: 58/58 checks PASS**, using SymPy 1.14.0 in `C:\Users\Notandi\miniconda3\envs\torment\python.exe`. The machine-readable result labels mathematical identities, special cases, counterexamples, source attestations and integrity attestations separately: EXACT_COUNTEREXAMPLE=7, EXACT_IDENTITY=41, EXACT_SPECIAL_CASE=3, INTEGRITY_ATTESTATION=4, SOURCE_ATTESTATION=3.

Script SHA-256: `6be53b07eff99ca8ff38754d97837d0184c9b3062cc1091e6ee914e3e347a706`. Results SHA-256: `06fa4dbf12b02283e5912e2bc6469ba26ae43baa22529410806d989ca405177a`.

| Scientific target | Check groups / supporting proof |
|---|---|
| Graphs, covering and sheets | Fibers; local bijection at every vertex; no triangle subgraph; §2 proof |
| Linear intertwining/isometry | Incidence Laplacian, `Δ12P=PΔ3`, `P*P`, Q compression and projector |
| Deck/base/full symmetry | Exhaustive 24 graph automorphisms, exact four-element kernel, six base actions, generator relations |
| V3 and Fourier | Full exact Fourier Gram matrix, all twelve eigenvalues/characters, selected 0/4/8 modes, normalized lift |
| Paper F relationship | Orthonormal u,v, their complex Fourier conversion, lifted vectors lie inside V3 |
| Nonlinear lift | General symbolic pre-sync polynomial, formal identical Arg0 inputs, phase-field/reconstruction identity, all zero-support masks |
| Normal space | Explicit nine-complex-vector basis, projectors and real ranks, off-sector equivariance, exact special-case derivative |
| Limits | Counterexamples for nonperiodic k, replacing P with Q, all-pairs multiplicity, sequential sweep, copy-dependent zero phases, full rotation with unequal k, and global attraction |
| Historical distinction | Exact current 24→12→3 tower checked; no assertion that it is the old D24 geometry |

The symbolic phase checks treat phase extraction as a shared deterministic scalar operation and then verify the phase law for arbitrary representatives and nonnegative radii. The all-state theorem, including zeros, follows from the stage-by-stage proof in §8; no claim is made that a finite list of numerical trajectories proves it. The homogeneous derivative example is explicitly a special case, and the existing numerical stability atlas is cited without being rerun.

To rerun the mathematical checks from PowerShell while preserving the delivered JSON:

```powershell
conda activate torment
python -B 'C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py' --output 'C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_02_RERUN.json'
```

Such a standalone rerun reports tree integrity as `NOT_CHECKED`. The delivered JSON additionally attaches this task's full before/after inventories, through `--integrity-dir C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas02_20260929_78c5m374`. That option verifies the supplied snapshots; it does not collect fresh fingerprints. Mathematical checks remain reproducible without those temporary inventories, given the documented source tree and `torment` environment.

## 13. Exact source register

Hashes identify the local artifacts inspected. Source locators above distinguish accepted code/publication authority from historical and supporting material. Existing cached PDF text used in the historical lane was accepted only after its original PDF hash matched the current historical file; no new PDF content was inferred from file names.

| ID | Exact local source | SHA-256 |
|---|---|---|
| A01 | [covering.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/covering.py>) | `5e6af1b665ece26cbc44bc63a85e08ff9bdf897c7efb2a03ef96f3a6cec550cf` |
| A02 | [dynamics.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py>) | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |
| A03 | [paper_A_publication.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/publication/paper_A_publication.md>) | `5fc388072d344c10d201b8eff255226b861014ff980e64c06811ae973bf7cd55` |
| A04 | [PAPER_A_PROOF_AUDIT_v0.3.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/PAPER_A_PROOF_AUDIT_v0.3.md>) | `61a3beb822fccd7e100215009e40ae9b9b6594df5fd92d6968fd48f25c7bac12` |
| A05 | [test_covering.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_covering.py>) | `8bf14c738bb240322a456502afbc32749b8420c80f3d810b7cfea3b8af418fdb` |
| A06 | [PAPER_F_PUBLICATION_v0.2.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md>) | `8c9419b20a0899857e68f4b191e7321cfc99f5286f149504f5d82a3e75db4fd5` |
| A07 | [EXACT_3_12_24_STRUCTURE_v0.1.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/reconstruction/EXACT_3_12_24_STRUCTURE_v0.1.md>) | `9083ba87570bff91c2437f6472f30b9acd48ed2333c39b89f651b6e06139b7cb` |
| A08 | [CODEX_PHASE3V_PORTAL_AND_12RING_VERIFICATION_v0.1.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/reconstruction/CODEX_PHASE3V_PORTAL_AND_12RING_VERIFICATION_v0.1.md>) | `1efbd83912b87303da81cae582647a9118483c81f74e8c9ff885560ad415a3ec` |
| A09 | [paperA_proof_audit_v0_2.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/verification/paperA/paperA_proof_audit_v0_2.py>) | `57d3977edf2c72ee497ebdb8b238fb065a788ac93772f74f3ae08ce9b54bce87` |
| A10 | [paper_a_oracle.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/parity_oracles/paper_a_oracle.py>) | `c174d3d7f5f86527bdd0e1840057d4c78fe24ff75a653934440cc7ed279eb4c1` |
| H01 | [model_core.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/model_core.py>) | `ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6` |
| H02 | [TriOctagon_D24-CP-Octant-Ridge.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOctagon_D24-CP-Octant-Ridge.pdf>) | `b340663e298eb6932a1be35ea1b7ced69edc29e6a72991c3df4c49e9d7b3edae` |
| H03 | [TriOcta_violations.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOcta_violations.pdf>) | `f3c5e0030edc82b233585d40c7dd42ae4046a4c5a81576e798511b4eeee5af87` |


## 14. Integrity and final disposition

Before/after SHA-256 inventories cover all regular-file bytes in the current repository, historical kernel_TO tree and production kernel. The **entire enclosing production checkout** is also included. Files under `.git` are excluded; ignored/untracked content is included. Empty directories, timestamps and ACLs are not part of this content fingerprint. Paths are root-relative with POSIX separators; the tree digest hashes the UTF-8 compact sorted JSON dictionary `{relative_path: SHA256(file_bytes)}`.

| Scope | Files before / after | Before SHA-256 | After SHA-256 | Changed paths |
|---|---:|---|---|---:|
| current | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | 0 |
| old | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | 0 |
| torment_kernel | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | 0 |
| torment_checkout | 173908 / 173908 | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | 0 |


Every scope has zero added, removed and modified file paths. Git HEAD and tracked status were read with optional locks disabled. Current HEAD remains the frozen baseline. Production HEAD remains `a06edcc5c9df5d3b56405085d9f2942b768dc203`; both tracked working trees were clean before and at completion. This is not a claim that there were no pre-existing untracked files. Full per-file inventories and their UTC intervals are retained in the external scratch directory cited in §12; the JSON records the interval and summary for each scope.

All three deliverables are in `C:\Users\Notandi\.codex\reports`, outside the protected source trees. Only external report/check/result and scratch evidence files were created. No project source, paper, historical file, test, or production file was changed; no repository test suite, simulation, build or Git network operation was run.

```text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
```

Atlas 02 is complete within the requested source-packet scope. STOP after reporting.
