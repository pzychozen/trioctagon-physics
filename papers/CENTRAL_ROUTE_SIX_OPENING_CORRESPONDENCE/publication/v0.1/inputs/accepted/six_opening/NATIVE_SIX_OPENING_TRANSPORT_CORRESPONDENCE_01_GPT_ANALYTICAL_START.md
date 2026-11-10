# Six-opening transport correspondence: analytical start

**Task:** NATIVE_SIX_OPENING_TRANSPORT_CORRESPONDENCE_01  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Prepared:** 9 November 2026  
**Status:** Proposed source comparison and new proofs for independent Codex verification.

## 1. Purpose and publication boundary

The accepted central-route assessment establishes that the existing receiver can gain storage before activity reaches the carrier's nearest point to the center, or the cuts of a region that strictly encloses both source profiles. Receiving therefore does not by itself certify a completed spatial circuit. Its five claims C01–C05 remain accepted, with the localized Q01 qualification preserved in the accompanying GPT acceptance record [CR].

This successor asks how the unchanged carrier and its exchange interfaces relate to the six source-defined central opening boundaries. The proposed result is stronger than different names or unaligned pictures: at the inherited registration, every candidate carrier circle is uniformly separated from all six boundaries and from each boundary's individual convex enclosure. The selected C1 therefore supplies no literal central G crossing at which to read its existing point-cut power.

The enclosure is a mathematical bounding set. Introducing it for this proof does not declare a physical aperture or add a closure to the source geometry. This distinction matters: missing a rim alone would not establish that a curve misses an opening's interior.

Once independently checked and accepted, this assessment and CR should form one paper: **Central-Route Accounting and Six-Opening Geometry in the Reciprocal Chiral Exchange Candidate**. The paper can finish the correspondence assessment while stating the additional spatial transport registration that remains to be constructed. Solving that subsequent model is not a prerequisite to writing this paper.

## 2. S01 — recover the common frame and the positive correspondence

### 2.1 Exact central geometry

All formulas first use host width one. Let

\[
r_g=\frac{\sqrt3}{6},\quad O=(0,r_g,0),\quad
d_g=1-\frac{\sqrt2}{2},\quad a_g=\frac{d_g}{2},\quad
h_g=\frac{\sqrt2-1}{2},\quad H_0=\frac12=h_g+d_g.
\tag{S1}
\]

For a world point P, write its centered horizontal part as P_h and its centered height as \(\zeta=(P-O)\cdot e_z\). Cylindrical radius means \(\rho(P)=\|P_h\|\), measured about the vertical axis through O.

In centered coordinates define

\[
\begin{aligned}
e_i&=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3)),\\
g_k&=e_{2k+1},\qquad J(X,Y)=(-Y,X),\\
0&\leq\tau\leq h_g,\qquad A_\tau=I-(\tau/r_g)J,\\
T_i&=(a_g e_i,h_g),& B_i&=(a_g A_\tau e_i,-h_g),\\
U_k&=(r_g e_{2k},H_0),& L_k&=(r_g A_\tau e_{2k},-H_0).
\end{aligned}
\tag{S2}
\]

Ring indices are modulo six; opening indices are modulo three. These are the refined registration family of CG, equations eq:constants and eq:family. Add O to obtain world coordinates. The upper and lower source-defined broken boundaries are

\[
\begin{aligned}
G_k^+&=[U_k,T_{2k+1}]\cup[T_{2k+1},U_{k+1}],\\
G_k^-&=[L_k,B_{2k+1}]\cup[B_{2k+1},L_{k+1}].
\end{aligned}
\tag{S3}
\]

Here brackets in (S3) denote closed segments. MINUS is the reflection of the entire PLUS face complex by \(S=\operatorname{diag}(-1,1,1)\) in centered coordinates. It is not obtained merely by reversing \(\tau\) while retaining the PLUS faces [CG, eq:faces and sec:openings].

These six broken arcs are not six specified filled surfaces with individual normals. The upper and lower arcs assemble into boundary cycles of the central complex; that fact alone gives no aperture flux observable. The static parameter \(\tau\) is not a clock.

### 2.2 Carrier and labels

The paired-gap source fixes

\[
\begin{gathered}
u_j=R_z(2\pi j/3)(0,1,0)=g_{(j+1)\bmod3},\\
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\qquad
a_c=\frac{K_c}{1+\sqrt3/2},\qquad R_c=\frac{\sqrt7}{2}a_c,\\
\Gamma_j(\theta)=O+K_cu_j+
R_c(\cos\theta\,u_j+\sin\theta\,e_z).
\end{gathered}
\tag{S4}
\]

Each candidate circle meets its two finite host-notch measurement triangles at
\(P_j^\sigma=O+a_cu_j+\sigma a_ce_z\). Those triangles are the central source's \(N_{(j+1)\bmod3,\sigma}\), not its G boundaries [PG, eq:triangles, eq:contacts and thm:circle; CG, eq:notch]. Only \(j=0\) is instantiated in the retained reciprocal candidate. Proving a geometric fact for all three choices does not instantiate three carriers.

The positive label correspondence in the reference PLUS convention is:

| Carrier candidate | Direction | Host pair and upper G bisector label | Stationary native support line |
| --- | --- | --- | --- |
| \(j=0\), selected C1 | \(u_0=g_1\) | \(N_1^\pm\), upper \(G_1^+\) | Channel 2 |
| \(j=1\), geometric alternative | \(u_1=g_2\) | \(N_2^\pm\), upper \(G_2^+\) | Channel 3 |
| \(j=2\), geometric alternative | \(u_2=g_0\) | \(N_0^\pm\), upper \(G_0^+\) | Channel 1 |

The last column means the exact positioned, unoriented line identity
\[
n_i=-g_{i-1},\quad c_i-O=-r_g g_{i-1},\quad
c_i+\mathbb Rn_i=O+\mathbb Rg_{i-1}.
\tag{S5}
\]
It does not place channel i at its same-direction opening. The native face center is on the opposite ray. The fixed-yaw source also combines raw pair-area components:
\[
f_\pm=\frac{G}{\sqrt7}
\left[\sqrt2(\chi_1+\chi_2)\pm\sqrt3\chi_3\right],
\quad \chi=a\times b,\quad G=\kappa_{\rm in}\lambda_g>0.
\tag{S6}
\]
There is no one-channel/one-opening power allocation in these formulas [AX, eq:axismatch; RX, eq:drive; CR, C01].

Upper G and N have a common azimuthal bisector in PLUS. Lower G instead carries the horizontal similarity \(A_\tau=\sqrt{1+(\tau/r_g)^2}R_{-\delta}\), with \(\delta=\arctan(\tau/r_g)\); the host N is fixed. MINUS retains the reflected labels, with \(Sg_k=g_{(-k-1)\bmod3}\). The selected \(g_1\) is fixed by this reflection. Direction agreement and the label dictionary are established correspondences; set equality and energetic passage require separate arguments.

## 3. S02 — enclose each actual G boundary

Define only for this proof
\[
\mathcal H_k^\sigma=\operatorname{conv}(G_k^\sigma).
\tag{S7}
\]
This is the triangle spanned by that individual arc's three vertices. Every upper hull stays in \(h_g\leq\zeta\leq H_0\); every lower hull stays in \(-H_0\leq\zeta\leq-h_g\). Reflect each hull for MINUS. We never take the convex hull mixing upper and lower arcs.

The matrix identity
\[
A_\tau^TA_\tau=\left(1+\frac{\tau^2}{r_g^2}\right)I
\]
gives the uniform horizontal dilation bound
\[
\|A_\tau v\|\leq D_*\|v\|,\qquad
D_*=\sqrt{1+(h_g/r_g)^2}=\sqrt{10-6\sqrt2}.
\tag{S8}
\]
Reflection preserves both \(\rho\) and \(|\zeta|\). Thus every ring elbow has \(\rho\leq D_*a_g\), \(|\zeta|=h_g\); every fan tip has \(\rho\leq D_*r_g\), \(|\zeta|=H_0\).

Set
\[
\Phi(P)=\rho(P)-\frac35|\zeta(P)|.
\tag{S9}
\]
On either fixed height halfspace, \(|\zeta|=\sigma\zeta\), so \(\Phi\) is a convex norm minus a linear function. The following two strict vertex bounds are enough:
\[
D_*a_g-\frac35h_g<\frac3{50},\qquad
D_*r_g-\frac35H_0<\frac3{50}.
\tag{S10}
\]
For completeness, use the positive rational radical enclosures
\[
1.4142<\sqrt2<1.4143,\quad
1.7320<\sqrt3<1.7321,\quad
2.4494<\sqrt6<2.4495,\quad
2.6457<\sqrt7<2.6458.
\tag{S11}
\]
Each is certified by squaring its endpoints. They give \(D_*<1231/1000\). Substitution in (S10) leaves margins at least
\[
\frac{79601}{20000000}>0,\qquad
\frac{277849}{60000000}>0,
\]
respectively. The portable preparatory checker records the exact rational operations.

Convexity now proves, uniformly in k, \(\sigma\), hand and \(0\leq\tau\leq h_g\),
\[
\boxed{\Phi(Q)\leq\frac3{50}\quad
\text{for every }Q\in\mathcal H_k^\sigma.}
\tag{S12}
\]
The non-strict displayed bound suffices, although the vertex argument is strict. An equivalent direct argument writes a hull point as a convex combination of the elbow and two tips: if the total tip weight is t, then \(|\zeta|=h_g+d_gt\) and \(\rho\leq D_*[(1-t)a_g+t r_g]\).

## 4. S03 — carrier separation and a true Euclidean lower bound

Since \(K_c>R_c\), every point of each circle satisfies
\[
\rho(\Gamma_j(\theta))=K_c+R_c\cos\theta,\qquad
\zeta(\Gamma_j(\theta))=R_c\sin\theta.
\]
Let \(L_*=\sqrt{34}/5=\sqrt{1+(3/5)^2}\). Cauchy–Schwarz gives
\[
\Phi(\Gamma_j(\theta))
=K_c+R_c\cos\theta-\frac35R_c|\sin\theta|
\geq K_c-L_*R_c.
\tag{S13}
\]

The exact rational estimates from (S11) imply
\[
K_c>\frac{756}{1000},\quad R_c<\frac{537}{1000},
\quad L_*<\frac{1167}{1000}.
\]
Consequently
\[
\begin{aligned}
\Delta_*&:=K_c-L_*R_c-\frac3{50}\\
&>\frac{756}{1000}
-\frac{1167}{1000}\frac{537}{1000}-\frac3{50}
=\frac{69321}{1000000}>0.
\end{aligned}
\tag{S14}
\]
Combining (S12)–(S14) excludes intersections with both the hull and the actual rim.

The margin in (S14) initially measures a difference in \(\Phi\), not a Euclidean distance. To obtain a distance bound, observe for arbitrary P,Q that
\[
|\Phi(P)-\Phi(Q)|
\leq\|P_h-Q_h\|+\frac35|\zeta(P)-\zeta(Q)|
\leq L_*\|P-Q\|.
\tag{S15}
\]
Therefore the proposed uniform theorem is
\[
\boxed{
\operatorname{dist}(\Gamma_j,\mathcal H_k^\sigma)
\geq\frac{\Delta_*}{L_*}
>\frac{297}{5000}=0.0594.
}
\tag{S16}
\]
The final rational comparison follows from
\[
\frac{69321}{1000000}
-\frac{297}{5000}\frac{1167}{1000}
=\frac3{2500000}>0.
\]
The exact expression \(\Delta_*/L_*\) is approximately 0.060972; this is itself a lower bound, not a computation of the true minimum distance. No optimized clearance is claimed.

If every geometric coordinate is scaled by one common width \(w>0\), the lower bound becomes \(297w/5000\). This is geometric scaling, not a physical length or energy calibration. The theorem is uniform over the specified static family and both hands.

In particular,
\[
\Gamma_j^{-1}(G_k^\sigma)=\varnothing,\qquad
\Gamma_j^{-1}(\mathcal H_k^\sigma)=\varnothing.
\tag{S17}
\]
Every finite B source/receiver support is a subset of the selected circle, so its spatial image is also separated. Increasing its arclength support does not move that support off the circle. Arclength width and tube radius remain distinct.

The proof also excludes any subsequently declared aperture that is wholly contained in the corresponding individual hull. It says nothing universal about arbitrary nonplanar spanning surfaces, a different carrier registration, or a separately specified thick structure. No such surface or thickness is selected here.

## 5. S04 — consequences for the existing transport account

The retained exchange system uses \(q=\eta_N f(x)-\eta_Rz\), the two distributed profiles B, \(y=B^*p\), and the local carrier identity
\[
e_t+j_s=pBq,\qquad
e=\frac12(p^2+r_c^2),\qquad j=cpr_c.
\tag{S18}
\]
Its native, carrier and receiver powers already match. Native F jumps preserve the carrier and receiver and add the actual native storage increment. These are completed results [RX; CR, C01 and C03].

For a literal G crossing on the unchanged C1, one would need a carrier parameter s whose embedded point belongs to the relevant G boundary, or to an explicitly specified aperture. Equation (S17) supplies no such parameter for the source-defined G or their individual hulls. Existing N contact powers, regional ball-cut powers, and distributed interface work therefore cannot be renamed as six G crossing powers.

The conclusion is **absence of an inherited G-resolved transport account**, not a calculated zero for physical flow through six apertures. The source has no such aperture/current observable to evaluate. The count of two ports versus six G labels is also not a dimension-based impossibility theorem: an explicitly supplied map could distribute two inputs among six outputs. None is selected by the present equations.

The distinction is visible in the exact roles:

| Existing quantity or object | Supplied meaning | Further identification needed for six-opening transport |
| --- | --- | --- |
| Stationary lines and decoded arrows | Exact state/support correspondence | An energetic path or transport observable attached to that geometry |
| \(G_k^\sigma\) | Central broken boundary arcs | A declared receiving/crossing set and orientation if a surface flux is intended |
| \(N_1^\pm\) and contact centers | Actual intersections of selected C1 with finite host measurement patches | A spatial relation to the central G, beyond shared labels |
| \(B\), \(B^*\), \(f\), \(z\) | Matched distributed exchange on two carrier arcs | A G-resolved spatial transfer or loading map with a compatible balance |
| \(j(s,t)\) | Oriented one-dimensional cut power | A specified cut parameter or justified ambient field/control-surface interpretation |
| C6 exterior records | Conditional, unloaded observations away from C1 | A loading/energy law before they can represent receiving |

The inherited C6 history map can, under its own history and regularity assumptions, be evaluated at fixed points away from C1. The proposed separation ensures that points of these G/hulls satisfy that geometric condition. This permits an observation comparison; it does not turn C6 into the receiver or supply an off-circle energy flux [CC, eq:C6; RX, accounts and interpretation].

Thus noncontact is compatible with possible observation, nonlocal coupling, or a later spatial extension. The present local reversible exchange can also coexist with a larger outward–around–inward route and transfer elsewhere. This assessment does not impose a choice between those goals.

## 6. S05 — completion criterion and combined-paper integration

The present task is complete when the independent review has established or corrected: the exact source dictionary; the individual-hull envelope; the uniform carrier separation; and the bounded transport implication. A conditional or negative direct-crossing result is a complete answer to this correspondence question.

For an actual six-opening transport construction, the next substantive addition would have to state what spatial set receives or is crossed, how the existing state supplies its transport/loading quantity, and how the resulting work joins the existing balance. This packet selects none of the possible mechanisms. The source comparison itself requires no new author geometry decision.

The combined paper should retain the accepted central-route account and its receiving-before-activity result, then add the reviewed six-opening geometry. It should distinguish four conclusions: an existing embedding, exact transfer accounting, the new direct-crossing obstruction, and the additional registration still needed for the intended spatial circuit.

Carry Q01 exactly: strict containment gives a positive gap for enclosing cuts, while a smaller region's cuts can also have a delay when they lie inside the source-free gap. Failed containment is not a universal no-delay claim. Retain C05's conditional phase-information scope, the distinction between port signs and characteristic senses, and the restrictions on reusing autonomous-F reconstruction during exchange.

Earlier RX/CC source snapshots contain historical open questions. Their missing-feedback and same-trajectory-credit statements are superseded where the current handoff and accepted later results say so. This new assessment does not reopen them. Later receiving/recovery after native updates and preload remains a separate open question.

## 7. Evidence status and source use

S01–S05 are proposed verification items. Internal source review and exact rational corroboration support submission; they are not an external Codex acceptance or an experimental test. No new carrier trajectory or physical parameter fit is needed for these geometric proofs.

SOURCE_LEDGER.md resolves CR, CG, PG, AX, RX and CC to exact preserved files and equation labels. SOURCE_IDENTITIES.json binds all retained sources and the unchanged complete central-route acceptance package. The figure illustrates the radial envelope; the inequalities, not the plotted samples, prove the result.
