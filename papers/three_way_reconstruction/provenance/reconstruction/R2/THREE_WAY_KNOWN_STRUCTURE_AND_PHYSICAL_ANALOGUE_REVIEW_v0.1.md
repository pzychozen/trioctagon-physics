# Three-Way: known structure and physical analogue review v0.1

Date: 2026-10-05  
Scope: read-only mathematical identification and bounded literature comparison.  
Authority: the diagonal minus-sign family specified in the work order, with real \(L>0\). All covering-space statements use its extension to the complex projective line.

## 1. Executive conclusion

**The reduced Three-Way quotient is exactly a standard, rigid Klein-four quotient of the Riemann sphere.** In suitable coordinates its normalized quotient map is

\[
\boxed{\beta(u)=\frac{(u^2+1)^2}{4u^2}
=\left(\frac{u+u^{-1}}2\right)^2.}
\]

It has degree four, deck group \(V_4\), branch values \(0,1,\infty\), and ramification partition \((2,2)\) above each. It is a Belyi map, a composition of the Joukowski map with squaring, and the quotient giving the spherical orbifold \(S^2(2,2,2)\). These are exact identifications, proved below; they do not identify a physical theory.

The quotient cover is independent of \(L\). Its zero/pole fiber moves to

\[
\boxed{\lambda_L=\frac{(L-1)^2}{2L+1}.}
\]

Away from \(L=1,4\), the three labeled branch values and this marked value give an exact point of \(M_{0,4}\). The marked value reaches \(0\) at \(L=1\), reaches \(1\) at \(L=4\), and approaches \(\infty\) as \(L\to\infty\). The fixed cover remains smooth throughout. At \(L=1\), the original rational function additionally becomes constant by cancellation.

**One exact structural realization occurs in established physics at a precisely limited level:** the complexified Bloch spectral curve of a uniform one-dimensional nearest-neighbor chain, quotiented by energy reflection, has exactly this \(V_4\) cover. A selected squared-energy level has exactly the marked-fiber role of \(\lambda_L\). This is classification **A for that spectral quotient with a marked level**. The identification is derived here from the standard dispersion relation; it is not a claim that the cited literature identifies Three-Way, or that Three-Way already specifies that physical system.

No complete physical identification of the original \(x\)-family is established. In particular, no physical meaning for \(F_L\), no dynamics, and no interpretation of the additional \(x\)-cover follow from the spectral equivalence. Gauge-theory, conformal-field-theory, scattering, fluid, and exceptional-point comparisons give smaller exact intersections, classified individually below.

The large-\(L\) charts partly resolve the marked fiber approaching the branch value at infinity. They are **not all confined to that neighborhood**: the intermediate chart retains the finite quotient geometry, including the shoulders. The full \(x\)-cover also carries an additional moving branch value.

The strong spectral identification and the missing physical dictionary meet the work order's stop conditions. This report stops at identification and comparison; it develops no physical model.

## 2. Accepted object, provenance, and evidence standard

The functions under examination are

\[
f_L(x)=\frac{Lx^4-Lx^2+1}{x^4-Lx^2+L},
\qquad
y=x^2,\qquad
F_L(y)=\frac{Ly^2-Ly+1}{y^2-Ly+L}.
\]

This review continues Sections 13–14 of the existing external [large-\(L\) analysis](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/THREE_WAY_LARGE_L_SCALING_ANALYSIS_v0.1.md). It does not reopen the earlier sign-provenance inquiry, substitute the plus-sign family, or import the later speculative physical interpretation.

The earlier analysis already derived the equal-value involution, the \(V_4\) quotient, its branch fibers, the extra branch value in \(x\), and the chart limits. Their repetition here establishes the dictionary needed for literature comparison; they are not claimed as new findings of this review.

“Proof” below means an explicit algebraic or covering-space argument. Source citations establish the standard terminology and the external physical examples. The Three-Way-to-source identifications are calculations in this review unless expressly attributed otherwise. Symbolic checks support the calculations; they are not substitutes for proofs or experimental evidence.

## 3. Exact normal form and mathematical species

Put

\[
a=\sqrt{2L+1},\qquad
u=a\frac{y-1}{y+1},\qquad
y=\frac{a+u}{a-u},\qquad
k=\frac{2(L-1)}a.
\]

For every \(L>0\), this is a nonsingular Möbius change of source coordinate. Direct substitution gives

\[
R(y)=\frac1y\ \longleftrightarrow\ u\mapsto-u,
\qquad
T(y)=\frac{(L+1)y-L}{Ly-(L+1)}
\ \longleftrightarrow\ u\mapsto\frac1u.
\]

Consequently \(R^2=T^2=1\), \(RT=TR\), and the source group is

\[
G=\{u,-u,u^{-1},-u^{-1}\}\cong V_4.
\]

With \(r=u+u^{-1}\),

\[
\boxed{F_L(y)=\frac{r+k}{r-k}},\qquad
\mathcal Q_L=r^2,\qquad
\boxed{\beta_L(y)=\frac{\mathcal Q_L(y)}4=\beta(u)}.
\]

The factorization is

\[
\mathbb P^1_y
\xrightarrow[\deg1]{u}
\mathbb P^1_u
\xrightarrow[\deg2]{r=u+u^{-1}}
\mathbb P^1_r
\xrightarrow[\deg2]{r^2/4}
\mathbb P^1_\beta.
\]

For \(L\ne1\), \(F_L\) is a Möbius coordinate on the intermediate \(r\)-sphere. Its degree in \(y\) is two; its degree in \(x\) is four. **The degree-four Belyi quotient is \(\beta_L\), not \(F_L\).** At \(L=1\), \(F_L\equiv1\) after cancellation, while \(\beta_L\) still has degree four.

| Proposed identification | Exact standard object and equivalence | Degree / ramification | Verdict and source |
|---|---|---|---|
| \(\mathbb P^1/V_4\) | The displayed Möbius coordinate conjugates the source action to sign and inversion; \(\beta\) separates its orbits. | Degree 4; three exceptional orbits of size 2. | Exact quotient; proof in Section 4; [S1](https://arxiv.org/pdf/1311.2529), [S2](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1701/kallio.pdf). |
| Sphere-to-sphere branched cover | The rational function \((u^2+1)^2/(4u^2)\). | Degree 4, total ramification 6, source and target genus 0. | Exact. |
| Signature \((2,2,2)\) | Three target branch values, with local index 2 everywhere above them. | Full partition is \((2,2)\) over each value. | Exact; the signature is not a list of three individual source points. |
| Belyi map | Branch values already normalized to \(0,1,\infty\). | Passport \((2^2,2^2,2^2)\). | Exact after source coordinate change and target scaling; [S1](https://arxiv.org/pdf/1311.2529). |
| Joukowski composition | \(J(u)=(u+u^{-1})/2\), followed by \(z\mapsto z^2\). | Degrees \(2\times2=4\). | Exact; the unnormalized Joukowski formula is [S5](https://shepherd.caltech.edu/Ae101/old/brad/ae101/notes/BradNotes.pdf), Eq. 17.29. |
| Spherical orbifold | Target sphere with cone orders \(2,2,2\). | Orbifold Euler characteristic \(1/2>0\); universal orbifold cover is the sphere with group \(V_4\). | Exact; [S2](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1701/kallio.pdf). |
| Invariant-theory quotient | \(\mathbb C(u)^G=\mathbb C(\beta)\). | Field extension degree 4. | Exact; elementary proof below. |

These are equivalences of covers with source and target coordinates allowed to change independently. They do **not** establish dynamical conjugacy of self-maps by one common Möbius transformation.

The normalized \(\beta\) has rational coefficients. When \(L\) is transcendental, the formula in the original \(y\)-coordinate need not have algebraic coefficients; its complex cover nevertheless has the displayed model over \(\mathbb Q\).

## 4. Orbits, ramification, invariant theory, and rigidity

The equation \(\beta(u)=b\) becomes

\[
u^4+(2-4b)u^2+1=0.
\]

A generic root therefore generates the entire fiber
\(\{u,-u,u^{-1},-u^{-1}\}\). Since this fiber has four points, \(\beta\) is the quotient map, rather than merely a function constant on some orbits.

Its derivative and exceptional fibers are

\[
\beta'(u)=\frac{u^4-1}{2u^3},
\]

| Quotient value | Source points | Stabilizer | Three-Way meaning |
|---|---|---|---|
| \(0\) | \(u=i,-i\) | \(u\mapsto-1/u\) | \(F_L=-1\), provided \(L\ne1\). |
| \(1\) | \(u=1,-1\) | \(u\mapsto1/u\) | Critical pair of \(F_L\); regular shoulders for \(L>4\); double zero/pole at \(L=4\). |
| \(\infty\) | \(u=0,\infty\) | \(u\mapsto-u\) | \(y=1,-1\), where the reduced \(F_L=1\). |

Each listed point has local degree two, including the two poles of \(\beta\). There is no other ramification. Riemann–Hurwitz gives

\[
-2=4(-2)+6.
\]

Because \(\beta\) is invariant and has degree four, the field inclusions
\(\mathbb C(\beta)\subseteq\mathbb C(u)^G\subseteq\mathbb C(u)\)
are equalities at the invariant-field step: the group already supplies four distinct automorphisms over \(\mathbb C(\beta)\). On the punctured source, the corresponding invariant ring is

\[
\mathbb C[u,u^{-1}]^G=\mathbb C[u^2+u^{-2}]=\mathbb C[\beta].
\]

One should not instead invoke invariants of \(\mathbb C[u]\), since inversion does not preserve that polynomial ring.

A monodromy triple is, up to sheet labeling,

\[
(12)(34),\qquad(13)(24),\qquad(14)(23).
\]

Their product is the identity and they generate a transitive \(V_4\). A transitive triple of double transpositions with product one must use exactly these three distinct nonidentity elements. Thus this passport has a single cover up to isomorphism with labeled target branch values. The unmarked cover is rigid and already belongs to the standard classification of three-point covers. The covering/permutation correspondence and Galois-cover language are standard in [Sijsling–Voight, Introduction and Section 6](https://arxiv.org/pdf/1311.2529).

For the orbifold,

\[
\chi_{\rm orb}=2-3\left(1-\frac12\right)=\frac12.
\]

Its coarse underlying surface is a sphere. It is not a torus and not the four-cone-point orbifold \(S^2(2,2,2,2)\). The literature explicitly identifies \(S^2/V_4\) with the three-cone-point orbifold in [Kalliongis–Ohashi, p. 49](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1701/kallio.pdf). A spherical metric can be supplied mathematically; no physical metric or length scale is thereby selected.

## 5. The marked fiber and the exact \(M_{0,4}\) statement

For \(L\ne1\), zeros satisfy \(r=-k\) and poles satisfy \(r=k\). Hence their union, with multiplicities, is the single fiber

\[
\beta=\lambda_L,\qquad
\lambda_L=\frac{k^2}{4}=\frac{(L-1)^2}{2L+1}.
\]

For \(L>0\), this is a regular four-point fiber precisely when \(L\notin\{1,4\}\). \(T\) exchanges equal-type partners; \(R\) exchanges zeros with poles.

Label the target points by the ordered tuple
\((\infty,0,1,\lambda_L)\). With the convention

\[
\operatorname{cr}(z_1,z_2;z_3,z_4)
=\frac{(z_1-z_3)(z_2-z_4)}
{(z_1-z_4)(z_2-z_3)},
\]

its cross-ratio is exactly \(\lambda_L\). Thus the **decorated target**, forgetting the source-coordinate embedding and zero/pole labels, determines

\[
[\infty,0,1,\lambda_L]\in M_{0,4}
\cong\mathbb P^1\setminus\{0,1,\infty\}.
\]

The standard moduli identification is [Mnev, Section 2.8.7, Eq. 209](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf). The specific substitution \(\lambda=\lambda_L\) is the exact Three-Way identification proved here.

Several distinctions matter:

- The three-branch cover is fixed. A fourth **marked target value** moves; it is not a fourth branch value of \(\beta\).
- \(L>0\) traces a real locus, rather than the whole complex moduli space.
- \(\lambda_L\) forgets the sign of \(k\), hence the distinction between the two marked signed levels \(r=\pm k\). It also forgets the original \(y\)- and \(x\)-coordinate choices.
- With branch labels forgotten, the usual six cross-ratio transforms further identify configurations. We keep the three branch labels because their Three-Way meanings differ.
- The \(V_4\) acting on source points is the deck group. The familiar \(V_4\) kernel in the permutation action on four cross-ratio labels is a statement about labels; the roles must not be conflated.

The loss of information is explicit:

\[
\lambda'_L=\frac{2(L-1)(L+2)}{(2L+1)^2},
\qquad
L=1+\lambda\pm\sqrt{\lambda(\lambda+3)}.
\]

For \(0<\lambda<1\), both inverse values are positive, one below \(1\) and one between \(1\) and \(4\). For \(\lambda>1\), only the plus sign gives \(L>0\). Therefore the marked quotient alone is not a one-to-one parametrization of the original family.

## 6. What the three collisions mean

| Parameter | Marked value | Exact event | What does not follow |
|---|---:|---|---|
| \(L=1\) | \(0\) | The formal marked fiber becomes \(2[i]+2[-i]\); zero and pole factors cancel and \(F_L\equiv1\). | A singular underlying quotient sphere or a physical transition. |
| \(L=4\) | \(1\) | The marked fiber becomes \(2[1]+2[-1]\); zeros and poles separately become double. | An exceptional point of a physical operator, a massless particle, or a topology change of the source sphere. |
| \(L\to\infty\) | \(\infty\) | The marked fiber tends to \(2[0]+2[\infty]\) on the fixed \(u\)-sphere. | A finite-\(L\) degeneration of the cover. |

At \(L=1+\epsilon\),

\[
\lambda_L=\frac{\epsilon^2}{3+2\epsilon}
=\frac{\epsilon^2}{3}+O(\epsilon^3).
\]

The real parameter path touches this boundary value to second order. “Zero/pole fiber” at \(L=1\) refers only to the limiting/formal marked divisor: the reduced constant map has no zeros or poles.

At \(L=4\),

\[
F_4(y)=\frac{(2y-1)^2}{(y-2)^2},
\qquad
\lambda_L-1=\frac{L(L-4)}{2L+1}
=\frac49(L-4)+O((L-4)^2).
\]

Both quadratics in \(y\) have discriminant \(L(L-4)\). Thus, except for the cancellation at \(L=1\), the roots are nonreal for \(0<L<4\), double at \(L=4\), and real and positive for \(L>4\).

The exact local normal form is visible without asymptotic assumptions:

\[
\beta(u)-1=\frac{(u-u^{-1})^2}{4}
=(u-1)^2+O((u-1)^3)
\]

near \(u=1\), and likewise near \(u=-1\). Consequently a regular inverse pair splits as the square root of \(\lambda-1\). This is a **discriminant crossing of a moving fiber through an existing critical value**. Two critical values of the fixed cover are not colliding.

At infinity use \(\mu=1/\lambda_L\). Then

\[
\mu=\frac{2L+1}{(L-1)^2}\sim\frac2L,
\qquad
\frac1{\beta(u)}=\frac{4u^2}{(1+u^2)^2}.
\]

The marked points therefore satisfy

\[
u\sim\pm\frac{\sqrt\mu}{2},
\qquad
u\sim\pm\frac{2}{\sqrt\mu}.
\]

This is ordinary order-two ramification at the two points above the target infinity.

In the compactification \(\overline M_{0,4}\), the limits \(\lambda=0,1,\infty\) are its three boundary points. The stable marked target can be represented by two rational components meeting at a node, with the four labels split two and two. This is a degeneration of the **marked configuration**; it does not make our original fixed rational map nodal. See [Mnev, Eq. 214 and Example 2.63](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf). Constructing an admissible-cover compactification would be a separate task.

There is also the excluded endpoint \(L\to0^+\), where \(\lambda_L\to1\). It does not add a new branch value.

## 7. The large-\(L\) charts in quotient language

The exact formula needed for comparison is

\[
\beta_L(y)=
\frac{[(L+1)(y^2+1)-2Ly]^2}
{(2L+1)(y^2-1)^2}.
\]

Writing \(N=Ly^2-Ly+1\) and \(D=y^2-Ly+L\), it also gives

\[
\boxed{\beta_L(y)-\lambda_L
=\frac{4ND}{(2L+1)(y^2-1)^2}.}
\]

The already-established chart limits, now normalized to the Belyi coordinate, are:

| Chart | Fixed coordinate | Quotient limit |
|---|---|---|
| Inner \(x=O(L^{-1/2})\) | \(\zeta=Ly\) | \(\beta_L-\lambda_L\to2(1-\zeta)\). |
| Ordinary bulk | \(y\ne\pm1\) | \(\beta_L/(L/2)\to[(y-1)/(y+1)]^2\). |
| Intermediate | \(s=\sqrt L(y-1)\ne0\) | \(\beta_L\to(s+2/s)^2/8=W(s)^2/8\). |
| Thin lock | \(\tau=L(y-1)\ne0\) | \(\beta_L/(L/2)\to1/\tau^2\). |
| Outer \(x=O(L^{1/2})\) | \(\eta=y/L\ne0\) | \(\beta_L-\lambda_L\to2(1-1/\eta)\). |

The limits are locally uniform on compact chart sets avoiding the displayed exclusions. These are substitutions into one rational map, not evidence for extra physical sectors.

For fixed bulk \(y\ne\pm1\), \(u\) grows as \(\sqrt L\); the thin lock chart has \(u\sim\tau/\sqrt{2L}\). They approach the two points \(u=\infty\) and \(u=0\) above the target infinity. The equal-value involution \(u\mapsto1/u\) exchanges these ends. In the original coordinates,

\[
L[T(y)-1]\longrightarrow\frac{y+1}{y-1},
\]

which identifies the bulk and lock quotient limits exactly.

The intermediate chart instead gives

\[
u=\frac{\sqrt{2L+1}\,s/\sqrt L}{2+s/\sqrt L}
\longrightarrow\frac{s}{\sqrt2}.
\]

It retains the finite quotient map. Its shoulders \(s=\pm\sqrt2\) are the preimages of \(\beta=1\). The involution \(s\mapsto2/s\) is the limit of the exact \(T\)-action, as established in the preceding report. It is not a new physical duality.

The original inversion exchanges inner and outer charts by \(\eta=1/\zeta\), and their centered quotient limits agree. Under \(T\), entire inner/outer chart regions map to neighborhoods tending to \(\tau=-1,+1\). Their fine structure is not resolved by the leading thin-lock coordinate alone; no new finer chart is introduced here.

There is an additional reason the entire atlas cannot be described by \(\lambda\) alone. The branch points of \(x\mapsto y=x^2\) have quotient image

\[
\boxed{\nu_L=\beta_L(0)=\beta_L(\infty)
=\frac{(L+1)^2}{2L+1}},
\qquad
\nu_L-\lambda_L=\frac{4L}{2L+1}\longrightarrow2.
\]

Thus two distinct distinguished values of the full construction approach target infinity: the marked zero/pole value \(\lambda_L\), and the extra branch value \(\nu_L\). In the inner chart, \(\zeta=0\) gives \(\beta-\lambda\to2\); the outer endpoint \(y=\infty\) gives the same value. The centered limits retain the finite separation that an uncentered limit would erase.

**Answer to the local-resolution question:** the zero/pole collision at target infinity has the exact quadratic local resolution displayed in Section 6. Bulk/lock and inner/outer charts describe approaches to that region, with extra data from the \(x\)-cover. The intermediate chart resolves the finite part between the two source ends. Calling all five charts only a local resolution of one marked point would discard this distinction.

## 8. Established mathematical comparisons

The exact species in Sections 3–4 is standard; it is not a new unmarked rational cover. The family adds a moving marked fiber, a particular source/output coordinate choice, and a further branched lift.

The moduli statement concerns configurations of target points. It must be distinguished from another familiar construction using four marked points:

\[
w^2=z(z-1)(z-\lambda).
\]

For \(\lambda\notin\{0,1,\infty\}\), this is a degree-two cover branched over four points and has genus one, since Riemann–Hurwitz gives \(2g-2=-4+4=0\). It is **a different cover** from our degree-four, genus-zero \(\beta\). This distinction explains how the same four-point moduli coordinate can appear in elliptic spectral geometry without making Three-Way itself an elliptic curve or a torus. The corresponding auxiliary elliptic curve appears explicitly in [Gaiotto, Eq. 2.9](https://arxiv.org/pdf/0904.2715).

At the collision, the inverse-fiber square-root law is also the ordinary local fold normal form of a simple critical point. That local equivalence supplies a mathematical bifurcation description. A global physical catastrophe model would additionally require a specified state space and equations.

## 9. Physical-framework comparison

Classification is assigned **once per explicitly scoped candidate**:
A = exact structural match; B = partial structural match; C = analogy only; D = no demonstrated structural match; E = unresolved.

An A classification identifies a mathematical object present within a physical framework. It does not by itself identify Three-Way as a physical theory.

| Candidate framework | Exact shared structure | Missing structure or mismatch | Class | Worth pursuing? |
|---|---|---|---|---|
| Uniform nearest-neighbor chain: complexified spectral quotient with a selected squared-energy level | Same \(V_4\), same degree-four map, same three branch values, same moving marked-fiber role. | A Three-Way interpretation of \(F_L\), its real plotting contour, and the \(x\)-lift is not supplied by this equivalence. | **A**, at the stated spectral-quotient scope | Yes: the strongest bounded dictionary question. |
| General determinant-one Floquet/transfer-matrix spectral curve | Reciprocal multipliers and the degree-two relation \(r=u+u^{-1}\). | A general trace function need not have energy-reflection symmetry; the full \(V_4\) and Three-Way parameter role do not follow. | **B** | Only after a specific operator is fixed. |
| Joukowski potential-flow construction | Exact \(u+u^{-1}\) conformal map. | Squared quotient and marked spectral role are not the physical flow construction; boundary conditions, potential, circulation, and units are absent. | **B** | Low priority. |
| Four-point conformal-field-theory kinematics | Exact four-marked-sphere cross-ratio coordinate. | Correlators, conformal weights, central charge, operator data, and this particular \(V_4\) cover are unspecified. | **B** | Useful as a moduli comparison only. |
| Class-S \(SU(2)\), \(N_f=4\) spectral/gauge geometry | Four-punctured sphere; cross-ratio enters coupling moduli. | The spectral curve, differential, periods, and gauge theory are additional data; the relevant double cover has different degree/genus. | **B** | Defer physical identification. |
| Original \(N=2\) Seiberg–Witten \(SU(2)\) solution | Branch-point collisions and singular parameter values of a spectral family. | Its genus-one curve varies and degenerates; our quotient is fixed and a marked fiber moves. No charge/period dictionary. | **B** | Useful to prevent conflating two degenerations. |
| Exceptional-point physics | Exact local square-root branching of inverse solutions. | No Three-Way non-Hermitian operator, eigenvector coalescence, or defective Jordan structure has been identified. | **B** | Local comparison only. |
| Four-particle CHY scattering formulation | Four marked points modulo Möbius transformations give \(M_{0,4}\). | Momentum constraints, polarization, scattering equations and amplitude measure are absent; no fixed \(V_4\) spectral quotient is established. | **B** | Low priority without a scattering dictionary. |
| A string-orbifold compactification realizing this entire decorated construction | No complete realization established in the checked sources. | Matching target, fields, consistency conditions, marked-level role, and \(x\)-cover would all need evidence. | **E** | Stop at the evidence limit. |
| Calling \(L=4\) an RG critical point or topological phase transition solely because roots coalesce | No RG flow, phase invariant, or thermodynamic singularity is supplied. | The shared claim is threshold terminology, not a demonstrated physical mechanism. | **C** | Do not pursue on that basis. |

The survey is bounded, not an exhaustive nonexistence theorem. In particular, the E classification does not claim that no future realization could exist. String compactification entered only as a checked quotient-geometry candidate, not as the starting interpretation.

### 9.1 The exact spectral-quotient identification

A uniform infinite chain with on-site energy \(E_0\) and real hopping \(t_h>0\) has the standard stationary equation

\[
(E-E_0)\psi_n=-t_h(\psi_{n+1}+\psi_{n-1}).
\]

Its Bloch dispersion is documented in [Tong, Section 2.1.1, Eqs. 2.2–2.5](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate2.pdf).

The following identification is our calculation. Allow a complex nonzero multiplier \(u\), put \(\psi_n=u^n\), and obtain

\[
\epsilon:=\frac{E_0-E}{t_h}=u+u^{-1}=r,
\qquad
\boxed{\frac{(E-E_0)^2}{4t_h^2}=\beta(u).}
\]

The source involutions are exactly \(u\mapsto u^{-1}\) and \(u\mapsto-u\). The first preserves \(\epsilon\); the second changes its sign. On lattice states they arise from spatial inversion and the alternating transformation \(\psi_n\mapsto(-1)^n\psi_n\). The latter anticommutes with the shifted nearest-neighbor Hamiltonian \(H-E_0\). These commuting operations therefore give the same \(V_4\) on the complexified spectral curve.

Select the signed level

\[
E_*(L)=E_0-t_h k(L).
\]

The pair of reflected energies has squared value \(\lambda_L\), so its four multiplier solutions satisfy exactly

\[
u^4+(2-4\lambda_L)u^2+1=0.
\]

The matching includes the cover, the action, the branch structure, and the parameter's role as a **marked spectral level in a fixed system**. \(L\) here reparametrizes the selected level; it does not vary the hopping Hamiltonian.

Under this dictionary,

\[
F_L=\frac{\epsilon+k(L)}{\epsilon-k(L)}.
\]

That equality is an exact scalar-function identity. It does not establish that \(F_L\) is a Green function, scattering amplitude, response, probability, or other prescribed observable. Nor does it account for the additional \(x\)-cover.

For propagating real-momentum Bloch states, \(u=e^{ipd}\) lies on the unit circle. Original real \(x\) instead gives real \(u=a(x^2-1)/(x^2+1)\). The contours coincide only at \(u=\pm1\). Thus even the real-domain interpretation requires work: much of the real Three-Way graph would lie on a spectral continuation, rather than on propagating states of this infinite chain.

### 9.2 What \(L=4\) means in the compared theories

For the matched chain,

\[
k(4)=2,\qquad E_*(4)=E_0-2t_h.
\]

It is exactly a band-edge crossing of the **selected spectral level**. The reflected level simultaneously reaches the opposite edge. The transition from nonreal unit-circle multipliers to real reciprocal multipliers is the same discriminant crossing as in Three-Way. This statement follows from the preceding dictionary and the standard band bounds; it is not a phase transition of a varying Hamiltonian.

In determinant-one transfer-matrix language, the multiplier equation \(u^2-r u+1=0\) has repeated roots when \(r^2=4\). The general reciprocal-multiplier framework is described in [Tong, Eqs. 2.18–2.19 and the following discussion](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate2.pdf). A transfer-matrix degeneracy should not automatically be called an exceptional point of the physical Hamiltonian.

Exceptional points require operator information in addition to the square-root eigenvalue law. [Heiss, Section 2, Eqs. 4, 6–7 and 10](https://arxiv.org/pdf/1210.7536) exhibits coalescing eigenvectors and a defective Jordan form. Those data are absent here.

In the original Seiberg–Witten example, the curve

\[
Y^2=(X-1)(X+1)(X-U)
\]

itself degenerates at distinguished \(U\). Periods and charge data give the massless-state interpretation; a collision alone does not. See [Seiberg–Witten, Eq. 6.6 and Sections 5.4–5.5](https://arxiv.org/pdf/hep-th/9407087).

In class-S gauge geometry, the four-puncture cross-ratio enters a coupling-moduli description, with an auxiliary elliptic curve and Seiberg–Witten differential. The weak-coupling descriptions at puncture-collision limits rely on that additional theory. See [Gaiotto, Eqs. 2.7–2.12, pp. 14–15](https://arxiv.org/pdf/0904.2715). No such coupling interpretation of Three-Way \(L\) is established.

### 9.3 Limits of the other comparisons

The potential-flow match uses exactly the Joukowski coordinate, but does not specify a Three-Way fluid problem; [Sturtevant, Section 17.2, Eq. 17.29](https://shepherd.caltech.edu/Ae101/old/brad/ae101/notes/BradNotes.pdf).

Four-point CFT and CHY scattering use marked-sphere kinematics, but supply different dynamical ingredients. The references checked are [Mnev, Section 7.5.1](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf) and [Cachazo–He–Yuan, Eqs. 1, 3–4 and 7](https://arxiv.org/pdf/1307.2199). Shared moduli do not identify their correlators or amplitudes with \(F_L\).

The checked institutional abstract of the original string-orbifold paper concerns quotients of flat tori by discrete groups. It does not establish our spherical quotient plus moving marked fiber as a compactification: [Dixon–Harvey–Vafa–Witten, abstract](https://collaborate.princeton.edu/en/publications/strings-on-orbifolds/). The full paper was not used to support further claims.

## 10. The quotient versus the branched \(x\)-lift

The precise map is a tower of branched covers:

\[
\mathbb P^1_x\xrightarrow[\deg2]{y=x^2}
\mathbb P^1_y\xrightarrow[\deg4]{\beta_L}
\mathbb P^1_\beta.
\]

The first step is a quadratic Kummer cover with function field
\(\mathbb C(y)(\sqrt y)\), branched at \(y=0,\infty\). This is the standard square-root-cover language; see [Stacks Project, Section 9.24, Lemma 9.24.1](https://stacks.math.columbia.edu/tag/09I6).

The composite \(\widehat\beta_L(x)=\beta_L(x^2)\) has degree eight and four distinct branch values for every finite \(L>0\):

| Target value | Ramification partition |
|---|---|
| \(0\) | \((2,2,2,2)\) |
| \(1\) | \((2,2,2,2)\) |
| \(\infty\) | \((2,2,2,2)\) |
| \(\nu_L=(L+1)^2/(2L+1)>1\) | \((2,2,1,1,1,1)\) |

The total ramification is \(4+4+4+2=14=2(8)-2\), as required for a degree-eight map between spheres. In particular, this composite cannot become a Belyi map merely by Möbius changes of coordinates: it has four distinct branch values.

A rational lift of \(T\) would require a rational function \(g(x)\) satisfying

\[
g(x)^2=
\frac{(L+1)x^2-L}{Lx^2-(L+1)}.
\]

The right side has distinct simple zeros and poles for \(L>0\). A rational square has only even orders. Therefore such a lift does not exist.

Equivalently, pulling the double cover back along \(T\) moves its branch divisor from \(\{0,\infty\}\) to
\(\{L/(L+1),(L+1)/L\}\); these are different. This is a precise pullback comparison. Merely composing \(x^2\) with \(\beta_L\) should be called a **composite cover**, not an unspecified categorical pullback. Pulling back the function \(\beta_L\) by \(x^2\) is of course valid function notation.

There remains a different global group on \(x\):

\[
H=\{x,-x,x^{-1},-x^{-1}\}\cong V_4,
\qquad
v=x^2+x^{-2}.
\]

The composite factors as

\[
\widehat\beta_L(x)
=\frac{[(L+1)v-2L]^2}{(2L+1)(v^2-4)}.
\]

A generic eight-point fiber comprises two \(H\)-orbits. It is not one orbit of a group of eight deck transformations: the mixed ramification indices above \(\nu_L\) exclude a Galois cover. Indeed its deck group is exactly \(H\), since it contains these four automorphisms, its order divides eight, and order eight is excluded.

“Branched cover over the coarse orbifold quotient” is acceptable with this qualification. The composite is not an unramified orbifold cover of \(S^2(2,2,2)\): it adds ramification above the ordinary point \(\nu_L\).

“Spin structure” is not warranted. A spin structure on a complex curve is a square root of its canonical line bundle, not the adjoining of a square root of a coordinate; compare [Mnev, Section 6.3.1, Eq. 813](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf). No spin, fermion, or covering-space physics follows from the obstruction to lifting \(T\).

The full decorated target has the extra datum \(\nu_L\). Consequently the four-point coordinate \(\lambda_L\) classifies only the reduced marked quotient, not all of the lifted construction.

## 11. Physical-dictionary requirements

A physical model does not universally require every item below. A lattice model, for example, need not posit a spacetime metric or a Lagrangian. It does require a specified state space, physical quantities, predictive laws, and a way to compare observables with observations. Additional requirements depend on the claimed theory.

| Mathematical item | What Three-Way currently supplies | What a physical identification must supply |
|---|---|---|
| \(x\) | Real plotting coordinate; complex rational-map coordinate. | Its physical role, domain, units, and relation to a preparation or measurement. |
| \(y=x^2\) | Exact quotient by parity, with a branched two-to-one map. | Whether sign removal is a physical symmetry, a redundancy, or only a coordinate choice. |
| \(L>0\) | Dimensionless coefficient; a marked-fiber path after normalization. | Whether it denotes a spectral selection, coupling, control variable, or scale; an independently justified calibration. |
| \(F_L\) | A meromorphic function with known divisor and reciprocal pairing. | A defined observable, amplitude, response, or state quantity, with normalization and measurement meaning. |
| \(\mathcal Q=4\beta\) | An orbit-separating algebraic invariant. | A physical quantity or an explicitly unobservable quotient coordinate. |
| Branch values | Exact critical-value and ramification data. | Which physical degeneracies they represent, if any, and the operator/equations establishing that interpretation. |
| Zeros and poles | Exact vanishing/divergence orders of this rational function. | Whether a measured response actually has those zeros/poles; admissible domains and any limiting prescription. |
| Involutions | Exact algebraic transformations with specified effects on \(F_L\). | Their action on physical states and observables, and whether they preserve dynamics. |

| Additional requirement | Present in the accepted construct? | Needed clarification |
|---|---|---|
| Units and calibrated dimensional constants | No physical assignment. Mathematical coordinates can be treated as dimensionless. | Supply units and independent scales where measurements require them. |
| Metric | Complex structure is present; no selected physical metric. | Necessary for claims about distances, causal geometry, or spacetime dynamics. |
| Action/Lagrangian or Hamiltonian | Absent. | Supply an appropriate predictive law; not necessarily all three formulations. |
| Time evolution | Absent. | Required for dynamical predictions, or explain a strictly stationary model. |
| Fields and state variables | No physical assignments. | Specify configuration/state space, admissibility, and preparation. |
| Conserved quantities | Algebraic invariants only. | Establish conservation under stated evolution; group invariance alone is insufficient. |
| Boundary/initial conditions | No physical ones. | Specify those needed to select physical solutions. |
| Coupling interpretation | No derived interpretation of \(L\) as a coupling. | Distinguish changing a system from selecting a level in a fixed system. |
| Observables and probabilities | No operational dictionary. | Define measurement rules and, where relevant, positivity/unitarity/probability normalization. |
| Predictions and calibration | Mathematical identities and asymptotic results; no calibrated physical predictions. | Derive testable consequences using independently specified parameters. |

The spectral match supplies a possible mathematical dictionary for \(u,r,\beta,\lambda\) inside an already-defined chain. It does not fill these rows automatically for Hilmir's original construction.

## 12. What is known, what this review adds, and what can be claimed

**Already in the preceding Three-Way analysis:** the rational normal form, the exact second involution, its intermediate-chart limit, the quotient orbit structure, the \(L=4\) root threshold, the nonliftability of \(T\), the extra \(x\)-branch value, and the leading quotient chart limits.

**Established mathematics identified here:** the rigid degree-four \(V_4\) Belyi map, its invariant field, the spherical \((2,2,2)\) orbifold, and the marked-target interpretation through \(M_{0,4}\). These identifications should not be presented as newly discovered mathematical species.

**New within this review relative to the preceding report:** the explicit cross-ratio/moduli boundary interpretation; the separation between degeneration of a marking and degeneration of a cover; the literature-supported spectral-quotient dictionary and its limitations; the correction of loose pullback/spin language; and the physical requirements audit. No claim of research-priority novelty is made.

Three-Way can presently claim a fully specified rational geometry with exact symmetries, divisors, branch data, real thresholds, and controlled asymptotic charts. It cannot presently claim a physical brane, dark-matter boundary, universe, spacetime geometry, RG flow, physical duality, or topological phase merely from these data. The mathematical sphere/orbifold classification also does not classify a separately chosen surface of revolution.

For verification, this review independently ran **21 exact symbolic checks**, all passing, covering the normal form, two coordinate involutions, centered quotient identity, discriminants, marked-value derivatives, additional branch value, all five chart limits, and local collision coefficients. The checks ran in memory using SymPy 1.14; no new implementation or parameter scan was added. The proofs above are the reproducible mathematical content. Source PDFs were inspected at the cited locations, with rendered-page checks for the Bloch dispersion, cross-ratio moduli statement, and Joukowski formula.

No repository files, kernels, UI code, papers, or commits were changed. The earlier external analysis was left unchanged.

## 13. Most promising next question and stopping point

The most useful next question is narrowly operational:

> In the already-matched nearest-neighbor spectral problem, is there an independently defined observable or boundary-value quantity whose value is exactly \(F_L=(\epsilon+k)/(\epsilon-k)\), and does its natural domain explain the original \(x\)-coordinate and its branched lift?

That is a question for a separate bounded study. Choosing an arbitrary observable to reproduce \(F_L\) would only repackage the algebra. A meaningful dictionary should explain why this function, this real domain, this parameter role, and this additional cover are selected by the physical problem.

The present work stops here because the unmarked quotient is already classified, an exact reduced spectral equivalence has been found, and advancing to physical identification would require structures absent from Three-Way. The result supports a precise mathematical identity and a concrete literature connection; it does not validate a physical interpretation.

## 14. References and claim-source ledger

Page numbers below are printed page numbers unless identified as PDF pages. Access date: 2026-10-05. Source IDs distinguish external support from this report's own transformations and proofs.

| ID | Source, author(s), year, stable identifier | Exact location used | Claim supported / boundary of use |
|---|---|---|---|
| S1 | Jeroen Sijsling and John Voight, *On computing Belyi maps* (2014), Publications mathématiques de Besançon, no. 1, 73–131. [DOI 10.5802/pmb.5](https://doi.org/10.5802/pmb.5); [arXiv:1311.2529](https://arxiv.org/pdf/1311.2529). | Preprint Introduction, pp. 1–2; Section 6, “Galois Belyi maps,” beginning p. 37. | Belyi definition, permutation-triple description, Galois quotient terminology. Our specific formula, passport uniqueness and field calculation are proved here. |
| S2 | John Kalliongis and Ryo Ohashi, *Finite actions on the Klein four-orbifold and prism manifolds* (2017), Comment. Math. Univ. Carolin. 58(1), 49–68. [DOI 10.14712/1213-7243.2015.193](https://doi.org/10.14712/1213-7243.2015.193); [paper](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1701/kallio.pdf). | Introduction, p. 49; preliminary orbifold discussion, p. 50. | The orientation-preserving \(V_4\) quotient of the sphere is the orbifold with three order-two cone points. Prism-manifold results are not used as a Three-Way interpretation. |
| S3 | Pavel Mnev, *Lecture Notes on Conformal Field Theory* (Notre Dame, Fall 2022 lecture notes). [University PDF](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf). | Sections 2.8.6–2.8.7, pp. 57–60, Eqs. 207–209 and 214; Section 7.5.1, pp. 199–200; Section 6.3.1, pp. 163–164, Eq. 813. | Four-point moduli and compactification; four-point CFT comparison; distinction between a spin bundle and a coordinate square-root cover. |
| S4 | David Tong, *Solid State Physics* (Cambridge, Lent Term 2017). [Full notes](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate.pdf); [Chapter 2](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate2.pdf). | Section 2.1.1, pp. 27–29, Eqs. 2.1–2.5; Floquet discussion, pp. 39–41, Eqs. 2.18–2.19 and following multiplier classification. | Standard chain dispersion and reciprocal transfer multipliers. The \(V_4\), normalized quotient and Three-Way marked-level identification are derived in this review, not attributed to Tong. |
| S5 | Bradford Sturtevant, *Fluid Mechanics: Lecture notes for Ae/Me/APh 101* (Caltech, 2001; hosted revision dated 2026). [University PDF](https://shepherd.caltech.edu/Ae101/old/brad/ae101/notes/BradNotes.pdf). | Section 17.2, p. 145, Eq. 17.29. | Exact Joukowski transformation and its fluid-mechanics context. Only the direct-map formula is used; the adjacent printed inverse formula is not relied upon. |
| S6 | Davide Gaiotto, *N=2 dualities* (2009 preprint; JHEP 08 (2012) 034). [arXiv:0904.2715](https://arxiv.org/pdf/0904.2715); [DOI 10.1007/JHEP08(2012)034](https://doi.org/10.1007/JHEP08%282012%29034). | pp. 14–15, Eqs. 2.7–2.12 and accompanying coupling-moduli discussion. | Four-punctured-sphere cross-ratio, auxiliary elliptic curve, SW differential, and qualification of the coupling-moduli identification. |
| S7 | Nathan Seiberg and Edward Witten, *Electric-Magnetic Duality, Monopole Condensation, and Confinement in N=2 Supersymmetric Yang-Mills Theory* (1994), Nucl. Phys. B426, 19–52; erratum B430, 485–486. [arXiv:hep-th/9407087](https://arxiv.org/pdf/hep-th/9407087); [DOI 10.1016/0550-3213(94)90124-4](https://doi.org/10.1016/0550-3213%2894%2990124-4). | Preprint Section 6, p. 35, Eq. 6.6; Sections 5.4–5.5. | Genus-one spectral family and the additional ingredients behind a massless-state interpretation. |
| S8 | W. D. Heiss, *The physics of exceptional points* (2012), J. Phys. A 45, 444016. [arXiv:1210.7536](https://arxiv.org/pdf/1210.7536); [DOI 10.1088/1751-8113/45/44/444016](https://doi.org/10.1088/1751-8113/45/44/444016). | Section 2, pp. 3–4, Eqs. 4, 6–7 and 10. | Square-root eigenvalue branching, coalescing eigenvectors and defective operator structure; only the local branching has been matched. |
| S9 | Freddy Cachazo, Song He and Ellis Ye Yuan, *Scattering of Massless Particles in Arbitrary Dimension* (2013 preprint; Phys. Rev. Lett. 113 (2014) 171601). [arXiv:1307.2199](https://arxiv.org/pdf/1307.2199); [DOI 10.1103/PhysRevLett.113.171601](https://doi.org/10.1103/PhysRevLett.113.171601). | pp. 1–2, Eqs. 1, 3–4 and 7. | Scattering equations and amplitudes on punctured spheres modulo Möbius transformations; no Three-Way amplitude identification. |
| S10 | Lance Dixon, Jeffrey A. Harvey, Cumrun Vafa and Edward Witten, *Strings on Orbifolds* (1985), Nucl. Phys. B261, 678–686. [DOI 10.1016/0550-3213(85)90593-0](https://doi.org/10.1016/0550-3213%2885%2990593-0); [Princeton institutional record](https://collaborate.princeton.edu/en/publications/strings-on-orbifolds/). | Institutional abstract. Full text not used. | Establishes the flat-torus quotient starting point of that paper, not a realization of the Three-Way spherical quotient. |
| S11 | The Stacks Project Authors, *The Stacks Project*, living reference. [Section 9.24, tag 09I6](https://stacks.math.columbia.edu/tag/09I6); [Lemma 9.24.1, tag 09DX](https://stacks.math.columbia.edu/tag/09DX). | Section opening and Lemma 9.24.1. | Kummer-extension terminology for adjoining roots. The specific branch-divisor and nonliftability proofs are supplied here. |

No cited source is claimed to name Three-Way or to establish Hilmir's intended physical interpretation. The exact connection is the displayed mathematics; its physical scope remains the one explicitly stated.
