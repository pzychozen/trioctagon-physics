# TL3 — Vesica-to-3D containment shell formalization
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

External read-only mathematical design / recovery · 6 October 2026

**The owner clarification narrows the intended role to a containing shell and possibly one of its sections. It does not yet select a unique shell, rotation, or top circle.** Two minimal lens revolutions already give inequivalent, exactly testable containing solids. Their uppermost sets are points. A circular sweep gives an actual uppermost circle, but adds a path radius and a profile-orientation choice. These distinctions survive exact containment against the unchanged Tri-Octagon.

```text
TOP_CIRCLE_ROLE = CONTAINMENT-SHELL / SECTION DESIGN INTENT
TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED
TL3 = CONDITIONAL MATHEMATICAL CONSTRUCTIONS; NO NATIVE ADOPTION
TL0–TL2 = CLOSED; CONSULTED ONLY
THREE_WAY = PARKED; PAPER_G = CLOSED; GR0–GR2 / CM0 / SA0 = CLOSED
NO PHYSICAL-QUANTUM, DARK-MATTER OR GRAVITY IDENTIFICATION
NO IMPLEMENTATION, SOURCE CHANGE, COMMIT OR PUBLICATION
```

## 1. Authority, evidence and precise meaning of containment

**SOURCE FACT.** The authoritative checkout is [trioctagon-physics](project-source/trioctagon-physics), on `main`, at `82cab10cbe550f58c43163fb8b05fabdad1b05ae`. HEAD, index and existing dirty/untracked status were recorded before this work. The existing scientific-UI changes, local research, tests, publication supplement and `tmp/` material were left in place. The source geometry is [geometry.py](project-source/trioctagon-physics/kernel_physics/geometry.py:16), not a historical display or the separate sibling kernels.

**OWNER DESIGN CLARIFICATION.** The attached [TL3 work order](<supplied-owner-work-orders/TL3_VESICA_CONTAINMENT.txt>) says that the historical top circle is not presently an independent dynamical object, that its intended role is shell/containment around the local module, and that a Vesica construction viewed after a 90° reorientation is relevant. This is new design information. No theorem below upgrades it to recovered historical mathematics or physical evidence.

We call the existing union of **filled polygonal panels** \(S\). A candidate **host solid** is \(K\subset\mathbb R^3\); its **containing shell** is \(\partial K\). Containment means \(S\subset K\), not \(S\subset\partial K\). Contact means \(S\cap\partial K\ne\varnothing\). It does not imply smooth tangency at a polygon vertex, a glued interface, or a force. For a nonconvex host, containing the panel surface need not contain its convex hull or a putative filled core. The native shell has open rims; no interior cap or solid core is added here.

All placements below are explicitly centered at the native symmetry centre \(o\), unless an offset is displayed. This is a conditional registration using the available centre, not a new native attachment law. Arbitrary translated hosts would add another parameter and are outside these minimum-scale claims.

**Evidence convention.** SOURCE FACT refers to surviving source bytes; OWNER DESIGN CLARIFICATION to the supplied intent; EXACT THEOREM and DERIVED IDENTITY to results proved below; STRUCTURAL ANALOGY and HISTORICAL INTERPRETATION do not establish equality; PHYSICAL INTERPRETATION is not adopted; OPEN QUESTION marks remaining choices. Bounded computation is reported separately as NUMERICAL EVIDENCE. Definitions of candidate hosts are conditional mathematical definitions, not recovered source facts.

## 2. Exact fixed shell and its useful containment data

**SOURCE FACT.** [geometry.py](project-source/trioctagon-physics/kernel_physics/geometry.py:16) fixes width one, \(s=\sqrt2-1\), fold angle \(\pi/3\), and

\[
o=(0,\sqrt3/6,0),\qquad e_z=(0,0,1).
\]

The local octagon has vertices

\[
(-1/2,-s/2),(-s/2,-1/2),(s/2,-1/2),(1/2,-s/2),
(1/2,s/2),(s/2,1/2),(-s/2,1/2),(-1/2,s/2).
\]

Its panel maps, at \(\beta=\pi/3\), are

\[
P_1(u,z)=(-1/2+(1/2-u)\cos\beta,(1/2-u)\sin\beta,z),
\]
\[
P_2(u,z)=(u,0,z),\qquad
P_3(u,z)=(1/2-(1/2+u)\cos\beta,(1/2+u)\sin\beta,z).
\]

There are 18 welded vertices, three octagonal faces, and two nine-edge nonplanar rims. The adopted frames in [face_state.py](project-source/trioctagon-physics/kernel_physics/face_state.py:29) derive

\[
n_A=(-\sqrt3/2,1/2,0),\quad n_B=(0,-1,0),\quad
n_C=(\sqrt3/2,1/2,0),\qquad t_i=e_z\times n_i.
\]

The face centres satisfy \(c_i-o=h n_i\), where \(h=\sqrt3/6\). As a set, each centered face is

\[
p=h n_i+u t_i+z e_z,\qquad
|u|\le\tfrac12,\quad |z|\le z_*(u):=\min(\tfrac12,\ell-|u|),
\quad \ell=\tfrac{1+s}{2}=\tfrac1{\sqrt2}.                 \tag{1}
\]

The sign of the material \(u\) coordinate can differ between panel parameterizations; (1) is their common polygonal set.

**DERIVED IDENTITY.** Every centered vertex has the same squared norm

\[
B^2=\frac{13}{12}-\frac{\sqrt2}{2},\qquad B=0.61337309375842841\ldots . \tag{2}
\]

Indeed the two vertex types give \(h^2+s^2/4+1/4=h^2+1/4+s^2/4\). Define their horizontal radii and the top-edge midpoint radius by

\[
h=\frac1{2\sqrt3},\quad
v=\sqrt{\frac56-\frac{\sqrt2}{2}}=0.35528376285271722\ldots,
\quad w=\frac1{\sqrt3}.
\tag{3}
\]

Here \((\rho,|z|)=(v,1/2)\) are the twelve high vertices, \((w,s/2)\) the six seam vertices, and \((h,1/2)\) the six top/bottom straight-edge midpoints. The entire shell has \(h\le\rho\le w\), \(|z|\le1/2\). Its uppermost set is three straight segments; its side-most set is three vertical seams. Its upper rim is not a circle.

**EXACT THEOREM — convex containment reduction.** For any closed convex host \(K\), the whole \(S\) lies in \(K\) iff its 18 vertices do. Necessity is immediate. Sufficiency follows because every filled octagon is the convex hull of its vertices. Consequently the centered sphere of radius \(B\) is a sharp spherical enclosure. This vertex test will **not** be used without proof for the nonconvex circular sweeps.

## 3. What a quarter-turn does, and what symmetry identifies

**DERIVED IDENTITY.** About the line through \(o\) with unit direction \(a\), a positive quarter-turn is

\[
Q_a p=(a\cdot p)a+a\times p,\qquad p\mapsto o+Q_a(p-o). \tag{4}
\]

This preserves dimension, distances and planarity. It cannot turn a planar curve or filled lens into a containing 3D solid. The vertices of \(S\) have affine rank three, so no rigidly rotated planar lens can contain them all.

The native [\(D_{3h}\) generators](project-source/trioctagon-physics/kernel_physics/geometry.py:166) are a 120° rotation about \(o+\mathbb R e_z\), reflection \(x\mapsto-x\), and reflection \(z\mapsto-z\). For an orthogonal symmetry \(g\),

\[
gQ_a(\alpha)g^{-1}=Q_{\det(g)ga}(\alpha).
\tag{5}
\]

Thus the direction specifying a rotation is axial under reflection; an ordinary profile coordinate is polar. The distinction prevents an incorrect sign rule.

There are three inequivalent **canonical unoriented axis classes** from this frame: \(\mathbb R e_z\), \(\mathbb R n_i\), and \(\mathbb R t_i\). C3 cycles the three faces in either horizontal class. No element of \(D_{3h}\) sends a normal line to a tangent line, or either to the vertical line. The signs of a quarter-turn are conjugate under appropriate reflections. There are also noncanonical continuous choices: horizontal unoriented lines have a fundamental azimuth interval of length \(\pi/6\), bounded by the normal and tangent classes. Tilted lines add an inclination. Threefold symmetry does not identify every horizontal angle.

To make the distinction concrete without selecting an initial plane, **conditionally** start with a horizontal lens whose ordered centreline/chord directions are \((a,b)=(n_i,t_i)\). Its normal is \(e_z\). Then:

| Quarter-turn | New centreline | New chord line | New plane | Equivalence |
|---|---|---|---|---|
| About \(e_z\) | \(t_i\) | \(-n_i\) | Horizontal | Exchanges the two horizontal axis classes; does not lift |
| About \(n_i\) | \(n_i\) | \(e_z\) | Vertical, normal line \(t_i\) | Same class for each \(i\), distinct from the next row |
| About \(t_i\) | \(-e_z\) | \(t_i\) | Vertical, normal line \(n_i\) | Centreline is now vertical |

For the unlabeled equal-circle pair or its lens, signs of the two planar coordinates are symmetries. In this table positive and negative quarter-turns even give the same profile sets. This statement need not hold for labeled circles, directed arcs or oriented frames.

For \(0<q<2\) the centreline and chord are geometrically distinguished short and long directions; exchanging them changes the lens. At \(q=0\) the lens is a disk, so this in-plane distinction disappears. The two vertical planes in the table still differ under the native group; after a lift to a sphere the orientation distinction disappears entirely. Revolving a profile can erase part of its frame information: spinning it about a selected axis removes the initial meridian choice. Equal containing radii therefore do not prove equal attachments.

**OPEN QUESTION.** The owner has not supplied an initial registered plane, a pivot line, the ordered roles of its two axes, or an active rotation versus a changed viewing direction. “90° from the earlier view” alone determines none of these.

## 4. The retained planar objects, including their degeneracies

**SOURCE FACT.** H02/H03 in [TL0](project-source/research/TL0_top_layer_recovery_20261006/TL0_TOP_LAYER_CIRCLE_RECOVERY.md) come from [Vesica Delay, pp.1,9](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/VESICA_DELAY.txt). With radius \(r>0\), separation \(0\le d\le2r\), and \(q=d/r\), use planar coordinates \((u,w)\) and set

\[
\mathcal D_\pm=\{(u,w):(u\mp d/2)^2+w^2\le r^2\},\qquad
\mathcal L=\mathcal D_+\cap\mathcal D_-.
\tag{6}
\]

The intersection is equivalently

\[
(|u|+d/2)^2+w^2\le r^2.                              \tag{7}
\]

For \(0<q<2\), the parents intersect at \((0,\pm r\sqrt{1-q^2/4})\). The chord has length \(2r\sqrt{1-q^2/4}\); the lens half-width along the centreline is \(r(1-q/2)\). The two boundary arcs are

\[
u=\pm\bigl(\sqrt{r^2-w^2}-d/2\bigr),\qquad
|w|\le r\sqrt{1-q^2/4}.                              \tag{8}
\]

The centreline is \(w=0\), the chord line is \(u=0\). With \(\theta=\arccos(q/2)\), each inward arc subtends \(2\theta\); the lens perimeter is \(4r\theta\), and its area is \(r^2(2\theta-\sin2\theta)\).

| Planar object | What is supplied | What it does not specify |
|---|---|---|
| Parent circles / disks \(\mathcal D_\pm\) | Two complete equal circles and their interiors | Whether the host should use their intersection, union, convex hull or one selected parent |
| Filled overlap \(\mathcal L\) | A definite compact convex profile with two reflection axes | Its placement in 3D or a lift axis |
| Lens boundary \(\partial\mathcal L\) | The two inward arcs (8) | An extrusion needs end caps; a sweep may cover interior surfaces if its axis cuts the profile |
| Intersection chord | A definite line segment for \(0<q<2\) | No enclosing planar area or 3D volume by itself |

At \(q=0\), the parents coincide and the lens is the whole disk. The limiting chord is a diameter, but there is no distinguished intersection chord: the two circles have become identical. At \(q=2\), the overlap and its chord reduce to a point while the parents remain two tangent disks. A zero-area overlap must not silently be replaced with their union.

The host constructions below use the filled overlap and then take the boundary of the resulting solid. Retaining the parent pair instead is possible, but a Boolean/envelope choice would be an extra adoption; no source selects all such alternatives. A single centered disk, giving a sphere or cylinder, is already covered by \(q=0\). Rotating the chord about its centreline gives a disk, about itself a segment, and extruding it once gives at most a planar rectangle. Those operations alone do not contain the nonplanar shell.

For 3D hosts we denote the absolute parent-profile scale by **\(R\)**, setting \(r=R\), \(d=qR\). This is not a claim that the initializer's particular input radius is spatially attached to the shell. It is precisely the additional scale needed for this candidate placement. Write

\[
c=1-q^2/4,\quad a=1-q/2,\quad b=1+q/2,
\qquad c=ab.
\tag{9}
\]

## 5. Minimal convex 3D lifts and sharp containment

### 5.1 The two revolutions are different

Let \(e\) be the selected unit axis through \(o\). For a centered spatial point \(p\), define \(z_e=p\cdot e\), \(\rho_e=\sqrt{\|p\|^2-z_e^2}\).

**Conditional definition / DERIVED IDENTITY — centreline revolution:** rotating the lens about the line joining its parent centres gives

\[
K_{\rm C}(R,q,e)=\{p:\rho_e^2+(|z_e|+qR/2)^2\le R^2\}
=\overline B(qRe/2,R)\cap\overline B(-qRe/2,R).        \tag{10}
\]

It is an intersection of two balls, a spherical lens. Revolve (7) with \(u=z_e\), \(|w|=\rho_e\) to prove the formula.

**Conditional definition / DERIVED IDENTITY — chord-axis revolution:** rotating about the chord line instead gives

\[
K_{\rm H}(R,q,e)=\{p:(\rho_e+qR/2)^2+z_e^2\le R^2\}. \tag{11}
\]

Here \(w=z_e\), \(|u|=\rho_e\). It is a filled convex body with pointed axial ends when \(q>0\), not a ring torus. Revolving full parent circles instead of the inward lens arcs would be a different construction and can create a self-overlapping parametrized surface.

Both (10) and (11) are convex: expand their inequalities as \(\|p\|^2+qR|z_e|\le cR^2\) and \(\|p\|^2+qR\rho_e\le cR^2\). They have nonempty interior for \(q<2\), boundaries homeomorphic to a sphere, and reduce to the same ball at \(q=0\). At \(q=2\), each overlap lift is a point. Neither is a torus for any \(0\le q<2\).

The extra data required, beyond the planar shape and scale, are the centre registration, **which of the two axes is revolved**, and that axis's ambient direction. No extrusion depth or path radius is needed. This is the sense in which these are two minimal 3D lifts; it is not a uniqueness theorem choosing between them.

### 5.2 Exact minimum scales for every fixed axis

For \(K\ge0\), \(M\ge0\), \(0\le q<2\), define

\[
\Phi_q(M,K)=\frac{qM+\sqrt{q^2M^2+4cK}}{2c}.          \tag{12}
\]

For a nonzero test point this is the unique positive root of \(cR^2-qMR-K=0\).

**EXACT THEOREM.** With \(p_j\) the 18 centered native vertices, put

\[
M_{\rm C}(e)=\max_j|p_j\cdot e|,\qquad
M_{\rm H}(e)=\max_j\sqrt{B^2-(p_j\cdot e)^2}.
\]

Then, for either lift and any fixed axis,

\[
S\subset K_{\rm C}\iff R\ge\Phi_q(M_{\rm C}(e),B^2),\qquad
S\subset K_{\rm H}\iff R\ge\Phi_q(M_{\rm H}(e),B^2).  \tag{13}
\]

**Proof.** At vertex \(j\), the inequality is exactly \(cR^2-qRM_j-B^2\ge0\). It holds for all vertices precisely when it holds for the largest \(M_j\). Solve the quadratic, and apply convex containment. A maximizing vertex lies on the host boundary at equality, so reducing \(R\) fails. For \(q>0\) contacts are exactly the maximizing vertices: the defining convex function is strictly convex, so any nontrivial convex combination of distinct vertices has strict inequality. At \(q=0\), all 18 vertices contact the sphere. Thus these are contact enclosures, generally not smooth tangent fits. ∎

| Unoriented axis class | \(M_{\rm C}\) | \(M_{\rm H}\) | Centreline \(R_{\min}\) at \(q=1\) | Chord \(R_{\min}\) at \(q=1\) |
|---|---:|---:|---:|---:|
| \(e_z\) | \(1/2\) | \(1/\sqrt3\) | 1.116114601615535 | 1.190991707147847 |
| \(n_i\) | \(1/\sqrt3\) | \(\sqrt{3/8}\) | 1.190991707147847 | 1.225745733596897 |
| \(t_i\) | \(1/2\) | \(B\) | 1.116114601615535 | 1.226746187516857 |

These maxima follow by inserting the exact panel vertices. The verification file records the attaining indices. Equal numbers in this table do not identify the corresponding surfaces or axes. For all axes, \(q=0\) gives \(R_{\min}=B\). For fixed \(q<2\) the minimum is finite. At tangency \(q=2\) no finite scale can contain \(S\); (13) diverges as that endpoint is approached.

### 5.3 Top, bottom, sides and parallels

For the **vertical-axis** versions of (10) and (11):

| Property | Centreline revolution \(K_{\rm C}\) | Chord revolution \(K_{\rm H}\) |
|---|---|---|
| Horizontal section of the solid | Disk of radius \(\sqrt{R^2-(|z|+qR/2)^2}\) | Disk of radius \(\sqrt{R^2-z^2}-qR/2\) |
| Height domain | \(|z|\le Ra\) | \(|z|\le R\sqrt c\) |
| Uppermost / lowermost set | One point at \(z=\pm Ra\) | One point at \(z=\pm R\sqrt c\) |
| Maximum horizontal extent | Equator circle, radius \(R\sqrt c\) | Equator circle, radius \(Ra\) |
| Boundary section at an interior height | One circle | One circle |
| Special locus for \(q>0\) | Two spherical caps meet along equator | Two pointed ends; equatorial parallel is widest |

Thus an interior-height “top parallel” can be named, but its height must be supplied. There is a family of circles, not an independently selected top member of positive radius. The equatorial circle is distinguished by symmetry and maximum width; it is not the uppermost set.

For other axis orientations, circular parallels are perpendicular to \(e\), not generally horizontal. Exact extremal information is still available. For a unit direction \(d_0\), let \(D=|d_0\cdot e|\), \(P=\sqrt{1-D^2}\). The support functions (maximum of \(d_0\cdot p\)) are

\[
H_{\rm C}(d_0)=
\begin{cases}R-(qR/2)D,&D\ge q/2,\\R\sqrt c\,P,&D\le q/2,\end{cases}
\quad
H_{\rm H}(d_0)=
\begin{cases}R-(qR/2)P,&P\ge q/2,\\R\sqrt c\,D,&P\le q/2.\end{cases}       \tag{14}
\]

To prove (14), maximize a linear functional on the circular meridian arc and check whether the unconstrained point lies in its retained half-plane. Otherwise the maximizer is at the equator of (10) or tip of (11). Set \(d_0=\pm e_z\) for top/bottom and use horizontal \(d_0\) for side supports. These strictly convex bodies have a unique supporting point in each fixed direction. For a horizontal axis, their generic horizontal sections are lens/oval curves rather than circles. Changing camera direction cannot change this.

### 5.4 Extrusion: another valid lift, with a necessary depth datum

Choose an orthonormal frame \((a_0,b_0,c_0)\), with centreline \(a_0\), chord \(b_0\), and extrusion direction \(c_0\). A finite **capped** extrusion is

\[
K_{\rm P}=\{p:(|p\cdot a_0|+qR/2)^2+(p\cdot b_0)^2\le R^2,
\quad |p\cdot c_0|\le H\}.                           \tag{15}
\]

Sweeping only the boundary gives an open side wall; the two lens caps must also be included to give \(\partial K_{\rm P}\). Infinite extrusion is not a bounded containment shell.

**EXACT THEOREM.** For \(q<2\), containment is equivalent to

\[
H\ge H_{\min}:=\max_j|p_j\cdot c_0|,\qquad
R\ge \max_j\Phi_q\bigl(|p_j\cdot a_0|,
(p_j\cdot a_0)^2+(p_j\cdot b_0)^2\bigr).             \tag{16}
\]

This follows from the same quadratic calculation and convexity. There are two independently required scales. If an aspect ratio \(H=\tau R\), \(\tau>0\), is stipulated, the sharp single scale is the maximum of the radial bound in (16) and \(H_{\min}/\tau\). No native source selects \(\tau\). Equality gives cap and/or side contact; strict inequalities give clearance. At \(q=2\) the overlap extrusion is only a line segment and cannot contain \(S\).

For \(c_0=e_z\), top and bottom extremal sets are the filled lens caps at \(\pm H\); their perimeters are not circles unless \(q=0\). Every intermediate horizontal boundary section is the same lens boundary. Side extrema are vertical segments over the support points of the planar lens. For arbitrary orientation the support function is

\[
H_{\rm P}(d_0)=H_{\mathcal L}(d_0\cdot a_0,d_0\cdot b_0)+H|d_0\cdot c_0|, \tag{17}
\]

where \(H_{\mathcal L}(A,B)=R\sqrt{A^2+B^2}-(qR/2)|A|\) when \(|A|/\sqrt{A^2+B^2}\ge q/2\), and otherwise \(R\sqrt c\,|B|\); it is zero at \((A,B)=(0,0)\). Equation (17) specifies all top/bottom/side extremal sets, including flat cap and segment cases. This host is not singled out by a quarter-turn.

## 6. Circular sweeps: a literal top circle costs an extra datum

### 6.1 General sweep versus two exactly analyzed circular choices

A prescribed path \(\gamma(s)\) and orthonormal cross-section frame \((a(s),b(s))\) define a sweep

\[
K=\bigcup_s\{\gamma(s)+u a(s)+w b(s):(u,w)\in\mathcal L_{R,q}\}. \tag{18}
\]

Closed-path frame matching, end caps for an open path, scale along the path, and possible self-overlap all need definitions. An unspecified sweep therefore has no single containment inequality, minimum scale or top set. Equation (18) is a specification template, not another completely determined candidate.

For a bounded comparison with the historical torus, specialize to the circle

\[
\gamma(\phi)=o+L(\cos\phi,\sin\phi,0),\quad L\ge0,
\quad (e_r(\phi),e_z)
\tag{19}
\]

and constant cross-section scale \(R\). This adds **path radius \(L\)**. The two symmetry-aligned lens orientations in that meridian plane are distinct:

\[
K_{\rm A}:\quad(\rho-L)^2+(|z|+qR/2)^2\le R^2
\quad\text{(parent centres in the axial/vertical direction)},           \tag{20}
\]
\[
K_{\rm R}:\quad(|\rho-L|+qR/2)^2+z^2\le R^2
\quad\text{(parent centres in the radial direction)}.                  \tag{21}
\]

Here \(\rho\ge0\), \(z=(p-o)\cdot e_z\). A 90° change of the **profile** in its meridian plane interchanges these choices; it is not a symmetry of the complete registered configuration. At \(q=0\) both give the standard circular tube \((\rho-L)^2+z^2\le R^2\). At \(L=0\), (20) and (21) reduce exactly to the vertical versions of (10) and (11).

These inequalities also describe the solid swept when the original cross-section crosses the axis: reflected negative radial coordinates add no points beyond the positive-radial portion. In that case the whole parametrized generating boundary need not equal the boundary of the swept solid. We always mean the latter.

### 6.2 Exact full-panel containment, including interior edge contacts

**EXACT THEOREM.** Let the three test types be

\[
(\rho_0,Z_0)=(h,1/2),\qquad (\rho_1,Z_1)=(v,1/2),
\qquad (\rho_2,Z_2)=(w,s/2),
\quad D_i^2=(\rho_i-L)^2+Z_i^2.
\tag{22}
\]

For \(0\le q<2\), the sharp scales for the *entire unchanged shell* are

\[
R_{{\rm A},\min}=\max_{i=0,1,2}\Phi_q(Z_i,D_i^2),\qquad
R_{{\rm R},\min}=\max_{i=0,1,2}\Phi_q(|\rho_i-L|,D_i^2). \tag{23}
\]

Containment holds exactly for \(R\ge R_{\min}\). Equality gives the attaining physical test points and their D3h copies as contacts. These include the top-edge **midpoints**, which are not mesh vertices.

**Proof, including the nonconvex issue.** Use (1). For fixed \(u\), both constraints increase with \(|z|\), so take \(|z|=z_*(u)\), then use reflection to take \(u\ge0\). On \(0\le u\le s/2\), \(z_*=1/2\) and \(\rho=\sqrt{h^2+u^2}\) runs monotonically from \(h\) to \(v\). Both constraint expressions are convex functions of \(\rho\) there, so their maxima occur at the two endpoints.

On \(s/2\le u\le1/2\), \(z_*=\ell-u\). For the axial-centres case, discard terms constant in \(u\) and consider

\[
f(u)=(\sqrt{h^2+u^2}-L)^2+(\ell-u)^2+qR(\ell-u).
\]

Its second derivative is \(4-2Lh^2/(h^2+u^2)^{3/2}\), increasing with \(u\), and its first derivative at \(s/2\) is \(s-1-Ls/v-qR<0\). It can only decrease and then increase; it has no interior maximum.

For radial centres, on each side of \(\rho=L\), the corresponding function has the same second derivative with \(L\) replaced by \(L'=L-\sigma qR/2\), \(\sigma=\operatorname{sign}(\rho-L)\). If \(L'\ge0\), its derivative has the preceding pattern and is negative at the left endpoint of the full chamfer interval; its formula cannot have an interior local maximum on a subinterval. If \(L'<0\), its second derivative is strictly positive. At \(\rho=L\) the derivative jumps upward, never producing a local maximum. Hence the chamfer endpoints suffice. Vertical seams are already covered by the maximum in \(|z|\). All three faces give the same meridian test. Expanding the constraints at (22) gives exactly the three quadratic roots (23). The listed points belong to \(S\), so the threshold is sharp. ∎

For (20), the high-vertex constraint dominates the seam-vertex constraint: they have equal original \(\|p\|^2=B^2\), while \(v<w\) and \(1/2>s/2\). Therefore define

\[
K(L)=\max\{(L-h)^2+1/4,(L-v)^2+1/4\}.
\]

Then

\[
R_{{\rm A},\min}=\Phi_q(1/2,K(L)),\qquad
K(L)=\begin{cases}(L-v)^2+1/4,&L\le(h+v)/2,\\
(L-h)^2+1/4,&L\ge(h+v)/2.\end{cases}                 \tag{24}
\]

At the switch both point types contact. At \(q=L=0\), all original vertices contact, as expected. For positive \(L\) the standard tube case is already a counterexample to using only the 18 vertices: for \(L>(h+v)/2\), the six midpoints determine its minimum thickness.

### 6.3 Topology, top parallels and the orientation-dependent hole condition

| Feature | Axial-centres sweep (20) | Radial-centres sweep (21) |
|---|---|---|
| Highest / lowest height | \(z=\pm Ra\) | \(z=\pm R\sqrt c\) |
| Extremal sets for \(L>0\) | Circles of radius \(L\) | Circles of radius \(L\) |
| Outer equatorial radius | \(L+R\sqrt c\) | \(L+Ra\) |
| Open central hole | \(L>R\sqrt c\) | \(L>Ra\) |
| Inner equatorial radius when positive | \(L-R\sqrt c\) | \(L-Ra\) |
| Horizontal solid sections | \(\max(0,L-b_z)\le\rho\le L+b_z\), \(b_z=\sqrt{R^2-(|z|+qR/2)^2}\) | Same interval with \(b_z=\sqrt{R^2-z^2}-qR/2\) |

When the hole inequality is strict, the solid is a solid torus and its boundary is an embedded topological torus (possibly with crease circles when \(q>0\)). The cross-section is a disk separated from the axis, so the revolution is a disk times a circle; this supplies the topology proof. At equality the inner equatorial circle collapses to an axial pinch point, and the boundary is not a surface manifold there. When the axis passes through the profile's interior, the swept solid is ball-like and its boundary is topologically a sphere, with possible nonsmooth axial points. This follows by rotating the truncated positive-radial meridian disk whose boundary meets the axis in an interval. It must not be confused with retaining a self-overlapping full spindle-torus parametrization.

At generic interior heights a toroidal boundary section has **two** circles, inner and outer, not one. At maximum height these meet in the unique uppermost circle, radius \(L\). For (21) and \(q>0\) that circle comes from the pointed lens tip and is a crease. At \(L=0\) it reduces to a point. At \(q=2\), either sweep is only the path circle; it cannot contain \(S\).

**EXACT THEOREM — a useful orientation distinction.** A vertical-axis axial-centres sweep can both contain \(S\) and retain an open toroidal hole iff

\[
0\le q<1,\qquad
L>\frac{1/3}{\,2h-q/(2\sqrt c)\,}.                  \tag{25}
\]

In that domain the allowed scales are \(R_{{\rm A},\min}\le R<L/\sqrt c\). To prove this, test the containment quadratics at the excluded upper endpoint \(R=L/\sqrt c\): each demands

\[
\bigl(2\rho_i-q/(2\sqrt c)\bigr)L>\rho_i^2+1/4,
\qquad \rho_i=h,v.
\]

The \(h\) coefficient is positive iff \(q<1\). In this range its lower bound on \(L\) dominates the \(v\) bound: \((\rho^2+1/4)/(2\rho-q/(2\sqrt c))\) decreases on \([h,v]\). Thus (25) is necessary and sufficient. In particular, the ordinary \(q=1\) Vesica **cannot** produce an open-hole containing torus by (20), although it can contain the shell after the hole has closed. This is a theorem about this specified host and registration, not about all Vesica constructions.

For the radial-centres sweep the exact open-hole criterion is simply

\[
\max_i\Phi_q(|\rho_i-L|,D_i^2)<L/a.                 \tag{26}
\]

It is feasible for every \(q<2\). For example, any \(L>w\) suffices: then \(L>\rho_i\), and inserting \(R=L/a\) reduces the strict condition to
\(L>a(\rho_i^2+Z_i^2)/(2\rho_i)\). The largest of the three ratios is \(w\), attained by the midpoint type. Thus choosing \(L>w\) leaves a nonempty scale interval. No parameter fitting is involved.

**NUMERICAL EVIDENCE, four bounded fixtures.** The exact formulas give:

| Cross-section choice | \(q\) | \(L\) | Sharp \(R_{\min}\) | Signed inner equatorial radius at that scale |
|---|---:|---:|---:|---:|
| Axial centres | 0.5 | 2 | 1.979496767520241 | +0.083360496380672 |
| Axial centres | 1 | 2 | 2.418828039883769 | −0.094766529925463 |
| Radial centres | 1 | 2 | 3.494559439573057 | +0.252720280213471 |
| Circular tube | 0 | 2 | 1.782872063540758 | +0.217127936459242 |

The negative signed value means the geometric section reaches the axis, not a negative physical radius. The complete inequalities use \(\rho\ge0\). All four thresholds contact the native top/bottom edge midpoints. Their differing outcomes prove that orientation is material to this geometric design problem.

These toroidal hosts contain the panel surface but leave \(o\) in the hole. If “containment of the core” is intended to include \(o\) or a filled convex hull, an open-hole torus fails that stronger requirement. This is an additional owner choice, not a reason to fill the native openings without authorization.

## 7. Shell, profile, axis and “top circle” are separate objects

**DERIVED IDENTITY / OPEN QUESTION.** The candidates can now be distinguished precisely:

| Construction | Contains the unchanged shell? | Minimum scale | Literal nonzero uppermost circle? |
|---|---|---|---|
| Rigid 90° reorientation of planar objects | No | None | No containing shell exists |
| Chord rotation / single chord extrusion | No 3D enclosure | None | A disk boundary is not a containing 3D shell |
| Capped lens extrusion | Yes for \(q<2\) and (16) | Two scales, or one after choosing an aspect ratio | No for \(q>0\) with vertical extrusion; at \(q=0\) the top set is a disk with circular rim |
| Centreline lens revolution | Yes for \(q<2\) and (13) | Exact, for fixed \(q,e,o\) | No; top point, circular interior parallels if axis vertical |
| Chord lens revolution | Yes for \(q<2\) and (13) | Exact, for fixed \(q,e,o\) | No; top point, circular interior parallels if axis vertical |
| Specified circular lens sweep | Yes for \(q<2\) and (23) | Exact, for fixed \(q,L,o,e_z\) and profile orientation | Yes for \(L>0\); topology additionally depends on hole condition |

The **complete shell** is the whole \(\partial K\); a **generating profile** is its meridian input; an **axis** is the line used in the operation; a **parallel** is a selected constant-height circular subset; an **equator** is the reflection plane's section; and a **top circle**, when it exists here, is the maximum-height parallel. These terms cannot be exchanged.

The clarified historical phrase could consistently mean a convenient parallel of a containing shell. It could also mean the uniquely highest circle of a circular sweep. Neither reading is yet selected. A pictured circle seen “from the top” could instead be a projection/silhouette, which is not the same thing as a spatial cross-section. No evidence currently identifies the original upper nine-edge rim with any of these circles.

## 8. Source comparison and the de Broglie / quarter-turn search

The historical comparison is limited to the named TL0 records and their relevant surviving formulas; it does not reopen their physics or a general archaeology census.

| Source object | Relationship to the candidates above | What is not justified |
|---|---|---|
| **H02/H03**, [Vesica Delay pp.1,9](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/VESICA_DELAY.txt) | **Exact equality** of planar parent/lens geometry (6)–(8), after choosing a planar rigid frame. The prose mentions perception spheres but explicitly models the geometry by two circles. | No recovered 3D centreline/chord revolution, attachment axis, or absolute enclosing scale follows from that wording. |
| **H04**, [VPQW §13, Eq.15](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/VPQW.txt:210) | **Possible lineage / structural analogy**: proposes toroidal coordinates following Vesica material. | Its displayed \(a^{-2}\partial_\theta^2+b^{-2}\partial_\phi^2+\partial_r^2\) does not specify an embedded host or the sweep (19). |
| **H15**, [fixed torus frame](project-source/kernel_TO/toy_3d_triocta.py:573) | **Exact standard-torus formula** for \(q=0\), \(L=2,R=0.6\), after a conditional translation aligning display origin with \(o\). It has a genuine highest circle, radius 2 at height 0.6. | This is not a containing host for the present shell in that registration: its inner radius 1.4 exceeds the shell's maximum horizontal radius \(w\). The whole shell lies in its central-hole region. Enclosing it in a plot is not containing it in the solid tube. |
| **H16**, [RSB halo](project-source/kernel_TO/toy_3d_triocta.py:520) | **Exact family of display parallels** on the larger torus \(L=2.02,R=0.63\), sampled at band-midpoint minor angles. | A finite set of circles is not a complete boundary. RSB energies set colour, not this geometry; no shell attachment is supplied. |
| **H24**, [host specifications, H-H](project-source/reconstruction/HOST_GEOMETRY_CANDIDATE_SPECIFICATIONS_v0.1.md:114) | **Closest match of intended role**: local module within a larger circular/Vesica construction. The present owner clarification makes containment an appropriate formal question. | Still no equality with one specific TL3 solid. The lift, registration, scale and named section were unspecified. |
| [Conditional Gate/Torus placement, §6](project-source/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md:309) | **Exact quarter-turn-and-placement formula**, discussed next. It is a genuine geometric comparator. | It places multiple rotated/scaled module copies around a circle. It does not derive a Vesica-containing host for the one unchanged central module. |

The Gate/Torus formula is

\[
X_j(p)=c(\phi_j)+\lambda_j F(\phi_j)Q_x(\pi/2)(p-o),
\quad F=[e_r,e_\phi,e_z],
\quad Q_x=\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix},
\]

so \(FQ_xe_z=-e_\phi\). It explicitly supplies the axis, multiplication order, frame, path and scale. Its illustrative \(L=3\), twelve placements, \(\lambda=1/4\), and tube-radius calculation concern those copies. They are not imposed on TL3. This is a previously recorded conditional quarter-turn, not evidence that the unspecified older “de Broglie flip” was that operation.

**SOURCE FACT — bounded recovery result.** The search inspected the DMQPF/Vesica/VPQW support extracts; the 46-document P0 text collection; the phase-3 historical paper extracts; earlier top-to-recursive extracts; the phase-2 primary-PDF text extracts; relevant prior host/lineage records; and historical Python geometry/display files. Searches included `de Broglie`, `broglie`, `flip`, `rotation`, quarter-turn, and 90° variants. Primary-text checks distinguished these hits:

- [DMQPF, p.2](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/DMQPF.txt:50) calls \(\lambda\) a de Broglie wavelength in the scalar correction containing \(1+\sin(\lambda/r)\). It does not give a spatial rotation. The previously retained [provenance audit, §E](project-source/reconstruction/CODEX_HOST_GEOMETRY_VERIFICATION_v0.1.md:253) also records its March carry-forward; that is a formula lineage, not a flip map.
- Vesica Delay's \(\theta=90^\circ\) is the **coincident-circle shape endpoint** \(d=0\), not a rigid rotation in 3D.
- [D24–CP's 90° passage](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/D24_CP.txt:82) concerns an abstract transverse helicity/flavour plane. It does not register a Vesica plane to \(n_i,t_i,e_z\). No physics claims in that passage are accepted by TL3.
- The [fixed-SRG helicity flip](project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/FIXED_SRG.txt:158) is a two-level operator \(\exp(-i\beta\sigma_x)\), not an ambient rotation of the lens.
- The existing face decoding has \(D_i(i\Omega_i)=n_i\times D_i(\Omega_i)\), a 90° tangent-vector rotation about a face normal. This follows from \(D_i(q+ip)=q t_i+p e_z\), \(n_i\times t_i=e_z\). It rotates a decoded vector, not the fixed panel or an attached host; it contains no de Broglie identification.
- The Gate/Torus formula above is a specified geometric quarter-turn, but has the different placement purpose explicitly stated in its source.

**OPEN QUESTION.** No exact transformation identified as the claimed de Broglie/Vesica flip was located in those inspected sources. The missing mathematical definition is an initial profile embedding \(E:\mathbb R^2\to\mathbb R^3\), pivot line and signed rotation \(Q\), clarification of an active transform versus a viewing change, and the subsequent lift operation. The term “de Broglie” adds no specified map between these objects. This is a source-limited recovery result; unindexed drawings or unprovided recollections are not ruled out. No textbook quantum construction was substituted for the missing map.

**HISTORICAL INTERPRETATION.** H24 is therefore the closest match in purpose; H02/H03 supply the exact planar input; H15 supplies an exact precedent for a highest circular parallel; and the Gate/Torus report supplies an explicit but different quarter-turn placement. There is no recovered identity chaining all four into one construction.

## 9. What TL1/TL2 contribute, and what they cannot choose

**INFORMATION-INTERFACE RESULT, retained from [TL1](project-source/research/TL1_lens_srg_identifiability_20261006/TL1_LENS_SRG_INITIALIZER_IDENTIFIABILITY.md) and [TL2](project-source/research/TL2_lens_ratio_conditioning_20261006/TL2_CONDITIONING_OF_LENS_RATIO_RECOVERY.md).** For fixed nonzero extraction factor, the initializer determines \(q=d/r\) through its scalar gain. Common scaling \((r,d)\mapsto(\alpha r,\alpha d)\) leaves the canonical initial state unchanged. The exact zero-output exceptions remain as classified there.

Thus it may provide a **shape parameter** for a separately adopted lens host, but supplies neither \(R\), nor \(L\), nor an extrusion depth, rotation axis, initial plane, translation, section height or attachment law. TL2's inverse conditioning does not create any of these missing channels. A minimum-scale rule such as (13) is a possible geometric design rule once a lift and registration are chosen; it is not a radius recovered from \(\Omega_0\). Choosing equality also chooses zero clearance. A positive clearance margin would be another design condition.

**PHYSICAL INTERPRETATION.** None is established by these containment identities. They neither identify quantum mechanics with a rotated lens nor derive a wavelength, material boundary, dark-matter structure or gravitational geometry. They also do not prohibit a future model from supplying additional geometric or physical data explicitly.

## 10. Verification and preservation

The external [verification script](project-source/research/TL3_vesica_containment_20261006/verify_tl3.py) and [results](project-source/research/TL3_vesica_containment_20261006/TL3_RESULTS.json) retain **35/35 passing checks**, distinct from all predecessor counts. They cover exact native vertex/frame identities, axis symmetry distinctions, quarter-turn formulas, containment quadratics, the chamfer derivative reduction, and bounded numerical fixtures. Two initial verifier comparisons tested expression syntax rather than symbolic equality; changing those assertions to simplify the difference resolved them without changing any mathematical formula or source.

Six fixed \(q=1\) revolution thresholds were checked with 80-digit arithmetic, including failure below the sharp scale. Four circular-sweep fixtures were additionally tested on 16,441 full-panel points each; these support the written endpoint proof and do not replace it. One extrusion fixture and the \(q=0\) spherical limit were checked. No parameter sweep, trajectory, UI, historical simulation or predecessor verification suite was run.

Before/after file inventories hash relative path plus SHA-256 content for **16,021 protected files**, excluding Git internals and only this new external output lane. All six protected root fingerprints, HEAD, full short status and index fingerprint agree:

| Protected root | Files | Before/after result |
|---|---:|---|
| `trioctagon-physics` | 8,571 | Identical |
| Historical `kernel_TO` | 401 | Identical |
| Separate `kernel_torment` | 15 | Identical |
| Separate sibling `kernel_physics` | 4,162 | Identical |
| Existing external `research` artifacts | 548 | Identical, excluding only this new lane |
| Existing `reconstruction` artifacts | 2,324 | Identical |

The JSON contains complete starting status, before/after aggregate hashes, contact indices, numeric results and this report's final hash. The scientific kernel, UI, Papers A–G, Atlas, parked/closed lanes, fixtures, historical originals and unrelated working-tree material were not modified. No staging, commit, push, tag or release occurred.

## 11. Final answers and the single next derivation

1. **Does the clarification reduce “top circle” to a containment-shell cross-section?** It narrows the intended role sufficiently to study that interpretation. It does not prove which shell, section or projected outline was meant, and does not formalize a distinct historical circle.

2. **What is the minimal mathematically defined compatible 3D lift?** Either of the two lens revolutions (10)–(11), after specifying its axis and registration, gives a closed containing boundary without a new depth or path-radius parameter. Neither is uniquely forced. A quarter-turn alone never suffices.

3. **What orientation datum is required?** The original plane and ordered centreline/chord roles, a pivot/rotation if reorientation is intended, then the lift axis and registration relative to \(o,e_z,n_i,t_i\). Normal, tangent and vertical canonical axis classes are inequivalent under D3h.

4. **Which lifts contain the exact Tri-Octagon?** Both revolutions for \(q<2\) at (13); capped extrusion at (16); and either specified circular sweep at (23). The lens tangency endpoint \(q=2\) supplies no containing volume. The historical fixed torus with radii 2 and 0.6 does not contain the current shell under centered coaxial registration.

5. **Is there a canonical/minimum scale?** There is a sharp minimum for each fully specified family, shape, orientation and registration. There is no family-independent native scale selection, no supplied clearance rule, and no scale recovered from the initializer.

6. **Does a literal circular top section arise?** The vertical convex revolutions have circular interior parallels but top points. The circular sweeps with \(L>0\) have genuine highest circles. Their extra path radius is indispensable. The current shell's own upper rim remains noncircular.

7. **What does shape without scale contribute?** A recoverable \(q\), under TL1's nonzero-extraction hypotheses, can index the candidate shape. It does not supply host scale, placement, axis, path or a physical interpretation.

8. **Which history is closest?** H24 matches the clarified role; H02/H03 exactly supply the profile. H15 matches a circular-sweep formula only in the disk limit and is a display, not the required enclosure. No single historical object is recovered as the selected host.

9. **What needs owner clarification?** Which planar object is used; which initial frame and 90° operation were intended; centreline revolution versus chord revolution versus a path sweep; whether a hole is allowed and whether the centre/filled core must also be contained; and whether “top circle” means highest parallel, selected latitude, equator or top-view outline. These are definitional choices, not arithmetic gaps.

10. **ONE justified next derivation:** after the owner selects one lift and the intended containment meaning, solve its **minimum-scale orientation problem** over the native D3h equivalence classes, using the exact contact bounds derived here. For a selected minimal revolution this is \(\min_{[e]\in\mathbb{RP}^2/D_{3h}}\Phi_q(M(e),B^2)\), including the attaining orientations and contact sets. Do not select a lift by doing that optimization across incompatible meanings of “host.” No further calculation is started in TL3.

**TL3 stops at this mathematical design/recovery checkpoint.**
