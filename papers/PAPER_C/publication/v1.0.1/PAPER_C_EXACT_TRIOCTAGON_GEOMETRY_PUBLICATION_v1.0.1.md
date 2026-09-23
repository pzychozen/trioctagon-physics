# Exact Geometry of the Folded Tri-Octagon Module


This paper gives the exact closed-form geometry of a single rigid module: three identical regular octagonal panels welded along vertical hinge edges and folded into a **polyhedral surface with boundary** (informally, an open lateral shell). Everything is coordinates, lengths, and angles in closed form, independently recomputed from the construction. The width $w=1$ is a **normalization only** and carries no physical meaning. The paper makes **no** physical, quantum-mechanical, particle, propulsion, memory-system, or symmetry-as-physics claim, and it does not use the historical "$D_{24}$" or "$\mathbb Z_{24}$" descriptions, which refer to different (concentric) constructions and are addressed only to separate them from the welded surface (§10).


Authoritative construction input: `TRIOCTAGON_ACTUAL_GEOMETRY_SPEC_v0.2.md` and the width-1 verification package `verification/actual_geometry/width_1/`. The analytic results below are **supported** by `verification/paperC/paperC_geometry_audit_v0_2_1.py`, which executes **51 symbolic/combinatorial regression predicates across all 19 numbered coverage groups** the referee identified (no tautological or expected-minus-itself checks). These finite checks **supplement, but do not replace, the analytic proofs**: this is an execution count of finite predicates, not a count of independent theorems, and the general-angle closure solution family and the full $D_{3h}$ upper bound remain analytic proofs (§§5, 9). See §10 and the companion `PAPER_C_PROOF_AUDIT_v0.2.2.md`, which separates analytic proof from executed regression from preserved historical validation.

---

## Abstract

Three identical regular octagons, each normalized to flat-to-flat width $1$ (edge $s=\sqrt2-1$), admit an exact symmetric folded realization. The middle panel is held fixed; the two outer panels are attached along the middle panel's vertical hinge edges in a reversed local orientation and rotated by a fold magnitude $\beta=60^\circ$ about those hinges. The two free outer-panel edges then coincide, completing a third seam alongside the two prescribed hinges and producing a welded lateral shell with $V=18$ vertices, $E=21$ edges, and $F=3$ octagonal faces, Euler characteristic $\chi=0$, one connected component, three vertical seam edges, and **two open nine-edge boundary rims** ($9s+9s$). The shell is a connected, compact, orientable $2$-manifold with boundary and two boundary components; applying $\chi=2-2g-b$ gives $g=0$, so it is an **annulus (a sphere with two disjoint open discs removed)**, **not** a punctured torus — the vanishing $\chi$ alone does not classify it, and the boundary is the deciding datum. Every horizontal cross-section through the central band ($|z|\le s/2$) meets the shell in the **perimeter** of an equilateral triangle of side exactly $1$ (the enclosed planar region, to which area/inradius/circumradius belong, is that filled triangle). The interior dihedral along each hinge is $60^\circ$ and the angle between outward face normals is $120^\circ$. The twelve chamfer boundary edges have exact $45^\circ$ inclination to the horizontal, while the panel planes themselves are vertical. The spatial notch at each rim tip has tip angle $\arccos(3/4)\approx41.4096^\circ$, distinct from its axial projection, which is equilateral and therefore $60^\circ$. The exact Euclidean symmetry group of the welded shell surface is $D_{3h}$ (order $12$). All coordinates and derived quantities are available in closed form.

---

## 1. Introduction

The object of study is a single geometric module: a **folded three-octagon polyhedral surface with boundary** (informally, an open lateral *shell*). It is built from three congruent regular octagonal panels of zero thickness, welded edge-to-edge along vertical hinge lines and folded so that their far edges meet. The polygonal construction is polyhedral [RS72, Cox73]; §5 establishes that this particular object is a piecewise-linear surface with boundary (the polygon union alone does not establish the local manifold hypotheses — those are verified for this object in §5). The result is a short open-ended prism-like band whose lateral wall is made of the three octagons. We take "surface" or "polyhedral surface" as the formal term and retain "shell" only where it aids readability.

This welded realization is one specified geometric object within the broader Tri-Octagon research. The author's later reference-scaffold clarification does not require the octagons to form a connected material surface. Paper D [PD] formalizes that reference construction and its conditional coordinate comparison with the present module. The definitions and proofs here continue to concern the welded surface fixed by Sections 2-4.

This paper does one thing: it states the construction unambiguously and derives, in closed form, every coordinate, length, angle, area, and topological invariant of the resulting mesh, then verifies each independently from the coordinates. Three cautions are built into the presentation from the start.

- **The width is a normalization.** We set the octagon flat-to-flat width (equivalently the side of the central equilateral cross-section) to $w=1$. This fixes a unit; it is **not** a physical scale, and nothing in this paper depends on the choice beyond overall scaling.
- **Three distinct angles must not be conflated.** The *fold magnitude* ($\beta=60^\circ$, the rotation applied to each outer panel from its reversed stacked-flat start), the *interior dihedral* ($60^\circ$, the wedge angle between two adjacent panels measured inside the shell), and the *outward-normal separation* ($120^\circ$, the angle between the two outward face normals) are related but different quantities (§7).
- **A spatial angle is not its projection.** The notch angle in $3$-space, $\arccos(3/4)$, differs from the $60^\circ$ one measures in the axial projection (§8).

Sections 2–4 fix the octagon, the hinged construction, and the exact coordinates. Sections 5–8 derive the topology, the central-band cross-section, the dihedral/normal relations, and the wall/notch geometry. Section 9 establishes the symmetry group; §10 records verification and separates the welded surface from older, different constructions; §§11–12 give limitations and the conclusion.

### 1.1 Relation to established results

The general tools used here are standard, and we cite them as background rather than as new results. Regular-polygon metric relations are elementary Euclidean geometry [Cox73, Cox69]; folding rigid polygonal panels about hinge/crease lines is the setting of geometric folding and rigid-origami theory [DO07, Tachi09]; the object is a polyhedral (piecewise-linear) surface with boundary [RS72]; the Euler characteristic and the classification of compact orientable surfaces with boundary via $\chi=2-2g-b$ are standard topology [Massey91, GX13, Hatcher02]; the interior-dihedral / outward-normal angle conventions are standard Euclidean geometry [Cox73], and the Schoenflies point group $D_{3h}\cong D_3\times C_s$ is standard point-group theory [Cotton90, AH94]; and exact/robust arithmetic for geometric predicates is the exact-computation paradigm of computational geometry [Yap97, KMPSY08, Shewchuk97]. In every case the cited source supplies the *general* framework, terminology, or theorem; the hypotheses, coordinates, and results **for this specific surface are established here**.

### 1.2 Contribution (what is model-specific)

The contribution is **not** any of the standard background just listed — not the regular-octagon formulas, the Euler characteristic, the surface-classification theorem, the vertex-link manifold criterion, the dihedral-angle convention, $D_{3h}$ group theory, or the exact-arithmetic methodology. The model-specific contribution is the **exact closed-form construction and complete geometric characterization of this particular three-octagon polyhedral surface**, namely: the $18$ exact welded vertices (§4); the general-$\beta$ closure relation and its $\beta=\tfrac{\pi}{3}$ solution (§5); the topology and annulus classification *for this surface*, with its hypotheses verified (§5); the exact equilateral central section (§6); the exact interior-dihedral and outward-normal values (§7); the chamfer-edge geometry (§6); the spatial and projected notch geometry (§8); the rim/hexagon decomposition (§8); and the proof that the exact Euclidean symmetry group of this surface is $D_{3h}$, with a matching upper bound (§9). A focused literature search did not locate a close precedent for this specific three-octagon polyhedral surface; its novelty is therefore left unresolved and **no priority claim is made**.

## 2. Normalization and the regular octagon

We work with a regular octagon of zero thickness, normalized so that its **flat-to-flat width** (the distance between a pair of opposite edges) is $w=1$. To avoid the single most common error — silently changing which measure is "the size" — we distinguish four different size measures of a regular octagon and give each in closed form. Standard regular-polygon metric relations supply these identities [Cox73]; we simply choose the normalization $w=1$, under which the octagon edge is $s=\sqrt2-1$. That value is elementary background under the chosen normalization, not a contribution.

Let the octagon have edge length $s$. For a regular octagon,
$$
w \;=\; (1+\sqrt2)\,s \qquad(\text{flat-to-flat width}).
$$
Setting $w=1$ gives the fundamental constant of the whole construction,
$$
\boxed{\,s=\sqrt2-1\,}\qquad\bigl(s=1/(1+\sqrt2),\ \ s(1+\sqrt2)=1\bigr).
$$
The four measures, all in the $w=1$ normalization:

| Quantity | Symbol | Exact value | Numerical |
|---|---|---|---|
| edge length | $s$ | $\sqrt2-1$ | $0.41421356\ldots$ |
| apothem (inradius, center→edge) | $a$ | $\tfrac12$ | $0.5$ |
| **flat-to-flat width** | $w=2a$ | $1$ | $1$ |
| vertex radius (circumradius, center→vertex) | $R$ | $\tfrac{s}{2}\sqrt{4+2\sqrt2}=\tfrac{(2-\sqrt2)\sqrt{2+\sqrt2}}{2}$ | $0.54119610\ldots$ |

The apothem follows from $a=\tfrac{s}{2}\cot(\pi/8)=\tfrac{s}{2}(1+\sqrt2)=\tfrac12$, and the circumradius from $R=\tfrac{s}{2}\csc(\pi/8)$. The interior angle at every vertex is $135^\circ$. A quantity used repeatedly below is the **chamfer cutback**
$$
d=\frac{s}{\sqrt2}=1-\frac{\sqrt2}{2}=0.29289321\ldots,
$$
the distance a $45^\circ$ corner edge advances along each flat direction.

**Local coordinates.** Place the octagon in a local frame $(u,z)$ with the two vertical flats at $u=\pm\tfrac12$ and the two horizontal flats at $z=\pm\tfrac12$; the four corners are chamfered by $45^\circ$ cuts. The eight vertices, in the material order used throughout, are
$$
\begin{array}{llll}
v_0=(-\tfrac12,\,-\tfrac{s}{2}), & v_1=(-\tfrac{s}{2},\,-\tfrac12), & v_2=(\tfrac{s}{2},\,-\tfrac12), & v_3=(\tfrac12,\,-\tfrac{s}{2}),\\[2pt]
v_4=(\tfrac12,\,\tfrac{s}{2}), & v_5=(\tfrac{s}{2},\,\tfrac12), & v_6=(-\tfrac{s}{2},\,\tfrac12), & v_7=(-\tfrac12,\,\tfrac{s}{2}),
\end{array}
$$
where $\tfrac{s}{2}=-\tfrac12+\tfrac{\sqrt2}{2}=\tfrac{\sqrt2-1}{2}$. All eight edges have length $s$; the four edges $v_0v_1,\,v_2v_3,\,v_4v_5,\,v_6v_7$ are the $45^\circ$ chamfers. The two vertical edges $v_3v_4$ (at $u=\tfrac12$) and $v_7v_0$ (at $u=-\tfrac12$) are the **hinge edges**; each has length $s$ and spans $|z|\le s/2$.

## 3. The three-face hinged construction

Hinged rigid-panel constructions — polygonal panels joined along hinge/crease lines and folded — are standard objects in geometric folding and rigid-origami theory [DO07, Tachi09]. The three-octagon assembly studied here is the specific construction defined below; the cited works establish the general setting and vocabulary, not this assembly, its closure, or its properties.

Take three congruent copies of the octagon of §2, labelled $P_1$ (left), $P_2$ (middle), $P_3$ (right). Embed them in $\mathbb R^3$ with coordinates $(x,y,z)$; the fold axis (prism axis) is $z$, and folding happens in the $xy$-plane.

1. **Stacked-flat reference.** All three panels start coplanar in the plane $y=0$. The middle panel keeps its local orientation, $P_2^{0}(u,z)=(u,\,0,\,z)$. The two outer panels start in the **reversed local-$u$** orientation, $P_1^{0}(u,z)=P_3^{0}(u,z)=(-u,\,0,\,z)$; i.e. each outer panel is laid over the middle panel with its local $u$-axis reversed. (This reversed start is what makes the subsequent fold magnitude $60^\circ$; see §7.)
2. **Fixed centre.** $P_2$ is held fixed for the entire construction.
3. **Hinge attachment.** $P_1$ is attached to the middle panel's **left** vertical edge and $P_3$ to its **right** vertical edge:
$$
H_1=\{(-\tfrac12,\,0,\,z):|z|\le s/2\},\qquad
H_2=\{(\tfrac12,\,0,\,z):|z|\le s/2\}.
$$
Each hinge is a segment of length $s$, shared over its full length before and after folding.
4. **Fold.** Rotate each outer panel about its hinge line (an axis parallel to $z$) by the fold magnitude $\beta$, in opposite senses. With hinge feet $c_1=(-\tfrac12,0,0)$ and $c_2=(\tfrac12,0,0)$ and $R_z(\cdot)$ the rotation about the $z$-direction,
$$
P_1^{\beta}=c_1+R_z(\beta)\,(P_1^{0}-c_1),\qquad
P_3^{\beta}=c_2+R_z(-\beta)\,(P_3^{0}-c_2).
$$
5. **Fold magnitude.** Take $\beta=60^\circ$. At this value the two far edges close (Theorem 2, §5) and the shell is complete.

This is a kinematic description of the final configuration, not a claim of collision-free physical motion: the reversed stacked start overlaps the middle panel, and the intermediate stages intersect. No physical motion is asserted.

## 4. Exact coordinate realization

Carrying out §3 with $\beta=60^\circ$ gives the closed-form panel maps (derived directly from $R_z(\pm60^\circ)$; independently verified in Appendix C):
$$
\begin{aligned}
P_1'(u,z)&=\bigl(-\tfrac14-\tfrac{u}{2},\ \tfrac{\sqrt3}{4}-\tfrac{\sqrt3}{2}u,\ z\bigr),\\
P_2'(u,z)&=(u,\ 0,\ z),\\
P_3'(u,z)&=\bigl(\tfrac14-\tfrac{u}{2},\ \tfrac{\sqrt3}{4}+\tfrac{\sqrt3}{2}u,\ z\bigr).
\end{aligned}
$$
Each map is an isometry, so each placed panel is still a regular octagon with edges $s$ and interior angles $135^\circ$ (verified). Evaluating at the eight local vertices and welding coincident images gives the **18 welded vertices** of the shell. The exact table (zero-based welded index; material aliases showing the welds):

| $i$ | aliases | $x$ | $y$ | $z$ |
|---:|---|---:|---:|---:|
| 0 | $P_1.v_0=P_3.v_3$ | $0$ | $\tfrac{\sqrt3}{2}$ | $\tfrac12-\tfrac{\sqrt2}{2}$ |
| 1 | $P_1.v_1$ | $-\tfrac12+\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt6}{4}$ | $-\tfrac12$ |
| 2 | $P_1.v_2$ | $-\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt3}{2}-\tfrac{\sqrt6}{4}$ | $-\tfrac12$ |
| 3 | $P_1.v_3=P_2.v_0$ | $-\tfrac12$ | $0$ | $\tfrac12-\tfrac{\sqrt2}{2}$ |
| 4 | $P_1.v_4=P_2.v_7$ | $-\tfrac12$ | $0$ | $-\tfrac12+\tfrac{\sqrt2}{2}$ |
| 5 | $P_1.v_5$ | $-\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt3}{2}-\tfrac{\sqrt6}{4}$ | $\tfrac12$ |
| 6 | $P_1.v_6$ | $-\tfrac12+\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt6}{4}$ | $\tfrac12$ |
| 7 | $P_1.v_7=P_3.v_4$ | $0$ | $\tfrac{\sqrt3}{2}$ | $-\tfrac12+\tfrac{\sqrt2}{2}$ |
| 8 | $P_2.v_1$ | $\tfrac12-\tfrac{\sqrt2}{2}$ | $0$ | $-\tfrac12$ |
| 9 | $P_2.v_2$ | $-\tfrac12+\tfrac{\sqrt2}{2}$ | $0$ | $-\tfrac12$ |
| 10 | $P_2.v_3=P_3.v_0$ | $\tfrac12$ | $0$ | $\tfrac12-\tfrac{\sqrt2}{2}$ |
| 11 | $P_2.v_4=P_3.v_7$ | $\tfrac12$ | $0$ | $-\tfrac12+\tfrac{\sqrt2}{2}$ |
| 12 | $P_2.v_5$ | $-\tfrac12+\tfrac{\sqrt2}{2}$ | $0$ | $\tfrac12$ |
| 13 | $P_2.v_6$ | $\tfrac12-\tfrac{\sqrt2}{2}$ | $0$ | $\tfrac12$ |
| 14 | $P_3.v_1$ | $\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt3}{2}-\tfrac{\sqrt6}{4}$ | $-\tfrac12$ |
| 15 | $P_3.v_2$ | $\tfrac12-\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt6}{4}$ | $-\tfrac12$ |
| 16 | $P_3.v_5$ | $\tfrac12-\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt6}{4}$ | $\tfrac12$ |
| 17 | $P_3.v_6$ | $\tfrac{\sqrt2}{4}$ | $\tfrac{\sqrt3}{2}-\tfrac{\sqrt6}{4}$ | $\tfrac12$ |

The three outward-oriented octagonal faces are
$$
P_1=(0,1,2,3,4,5,6,7),\quad P_2=(3,8,9,10,11,12,13,4),\quad P_3=(10,14,15,0,7,16,17,11).
$$
These coordinates are the primary object of the paper; renders and projection drawings are secondary and never override them.

## 5. Mesh topology and boundary

The welds are exactly the three shared vertical edges (seams):
$$
\underbrace{P_1.v_3v_4=P_2.v_0v_7}_{H_1,\ x=-1/2},\quad
\underbrace{P_2.v_3v_4=P_3.v_0v_7}_{H_2,\ x=1/2},\quad
\underbrace{P_1.v_0v_7=P_3.v_3v_4}_{\text{apex},\ (0,\sqrt3/2)} .
$$

> **Theorem 1 (topology).** The welded shell has
> $$
> F=3,\quad V=18,\quad E=21,\quad \chi=V-E+F=0,
> $$
> one connected component, three seam edges (each shared by two faces), and $18$ boundary edges forming **two disjoint nine-edge loops**.

**Proof.** Three octagons carry $3\times8=24$ material vertices and $3\times8=24$ edges. Each of the three seams welds one vertical edge of one panel to one vertical edge of another; a vertical edge has two endpoints, so each seam merges two vertex pairs and one edge pair. Thus
$$
V=24-3\cdot2=18,\qquad E=24-3\cdot1=21,\qquad \chi=18-21+3=0 .
$$
The three welds connect $P_1\!-\!P_2$, $P_2\!-\!P_3$, and $P_1\!-\!P_3$, so the panel adjacency graph is connected: one component. Each panel has two vertical edges (both welded) and six non-vertical edges (unwelded); the $3\times6=18$ unwelded edges are the boundary edges, each in exactly one face (the other $3$ edges lie in two faces each). Tracing incidences, the boundary edges split by the sign of $z$: the six vertices at $z=+\tfrac12$ together with the three tips at $z=+\tfrac{s}{2}$ form one nine-edge loop, and the mirror set at $z<0$ forms the other. $\blacksquare$

> **Theorem 2 (closure, general fold angle).** Let the fold magnitude range over $0\le\beta\le\pi$, with the general-angle panel maps (derived by rotating the reversed start $(-u,0,z)$ about the hinge feet $c_1,c_2$)
> $$
> P_1^\beta(u,z)=\Bigl(-\tfrac12+\bigl(\tfrac12-u\bigr)\cos\beta,\ \bigl(\tfrac12-u\bigr)\sin\beta,\ z\Bigr),\quad
> P_3^\beta(u,z)=\Bigl(\tfrac12-\bigl(\tfrac12+u\bigr)\cos\beta,\ \bigl(\tfrac12+u\bigr)\sin\beta,\ z\Bigr).
> $$
> The two free outer edges (at $u=-\tfrac12$ for $P_1$, $u=+\tfrac12$ for $P_3$) are
> $$
> F_1^\beta(z)=\bigl(-\tfrac12+\cos\beta,\ \sin\beta,\ z\bigr),\qquad
> F_3^\beta(z)=\bigl(\tfrac12-\cos\beta,\ \sin\beta,\ z\bigr),
> $$
> so $F_3^\beta(z)-F_1^\beta(z)=(1-2\cos\beta,\,0,\,0)$. On the domain $0\le\beta\le\pi$ the unique closure is $\beta=\tfrac{\pi}{3}$, giving the single seam
> $$
> F_1=F_3=\{(0,\tfrac{\sqrt3}{2},z):|z|\le s/2\}.
> $$
> (For unrestricted real $\beta$ the full solution set is $\beta=2k\pi\pm\tfrac{\pi}{3}$, $k\in\mathbb Z$; the $-\tfrac{\pi}{3}$ branch gives the reflected configuration at $y=-\tfrac{\sqrt3}{2}$.)

**Proof.** Each $P_i^\beta$ has orthonormal $u,z$ derivative columns, hence is an isometric planar embedding, and fixes its hinge pointwise for **every** $\beta$ (substituting $u=\tfrac12$ in $P_1^\beta$ gives $(-\tfrac12,0,z)=H_1$, and $u=-\tfrac12$ in $P_3^\beta$ gives $(\tfrac12,0,z)=H_2$). The two free edges are parametrized by the **same** $z\in[-\tfrac{s}{2},\tfrac{s}{2}]$, and their $y$-coordinates coincide identically ($\sin\beta$) while their $z$-coordinates agree pointwise; therefore the vanishing of the $x$-gap $1-2\cos\beta$ is not merely a necessary condition but implies **full edge coincidence**. On $0\le\beta\le\pi$, $\cos$ is strictly decreasing, so $1-2\cos\beta=0$ has the sole root $\beta=\tfrac{\pi}{3}$ (where $\cos\beta=\tfrac12$, $\sin\beta=\tfrac{\sqrt3}{2}$); the unrestricted-$\beta$ family follows from periodicity and evenness of $\cos$. At $\beta=\tfrac{\pi}{3}$ the maps reduce to the printed $P_1',P_3'$ of §4. $\blacksquare$

The earlier draft's "$1-2\cos\beta$ vanishes iff $\beta=60^\circ$" was **false without a stated domain** (e.g. $\beta=\tfrac{5\pi}{3}$ also closes, at $y=-\tfrac{\sqrt3}{2}$); the corrected statement fixes the fold-magnitude domain and establishes the $y,z$ agreement that makes the zero $x$-gap a genuine coincidence.

> **Theorem 1b (surface type).** The shell is a connected, compact, orientable $2$-manifold with boundary, with $b=2$ boundary components; hence by $\chi=2-2g-b$ it has genus $g=0$ and is an **annulus/cylinder — equivalently a sphere with two disjoint open discs removed.** It is not a torus, and not a punctured torus.

**Proof.** The classification of compact orientable surfaces with boundary and the formula $\chi=2-2g-b$ are standard [Massey91, GX13]. For a two-dimensional simplicial triangulation, the standard PL surface criterion requires each vertex link to be a PL circle or a PL closed interval, corresponding respectively to interior and boundary vertices [RS72, Exercise 2.21(1)]. These sources supply the general theorem and criterion; the actual vertex links and hypotheses **for this surface** are established here (below, every vertex link is an arc, so all $18$ vertices are boundary vertices). The classification formula requires those hypotheses, which we verify before applying it.
- **Compact.** $S$ is a finite union of closed bounded polygonal faces.
- **Manifold with boundary (vertex links).** A point in a face interior has a disk neighbourhood. An interior point of a seam edge is shared by exactly two faces whose half-disks glue along the seam into a full disk (the nonzero dihedral is not a topological singularity). An interior point of a boundary edge (one face) has a half-disk neighbourhood. At each vertex the link is a single arc (interval): the $12$ single-panel vertices have a one-edge link, and at each of the six seam-endpoint vertices ($0,3,4,7,10,11$) the two incident face-corners share the seam edge, giving a three-vertex/two-edge link path — an interval, not a branching or disconnected link. So every point has a neighbourhood homeomorphic to a disk or half-disk: a manifold with boundary. The face planes meet only along their seam corner-lines (no spurious intersections), so $S$ is embedded.
- **Connected.** The face-adjacency graph is a triangle ($P_1\!-\!P_2\!-\!P_3\!-\!P_1$); the $1$-skeleton is connected.
- **Orientable.** The three face cycles traverse every shared seam edge in **opposite** directions, so they induce a coherent orientation.
- **Boundary.** $b=2$: the two nine-edge rims of Theorem 1, each a degree-two cycle, one wholly at $z>0$ and one wholly at $z<0$.

Only now apply $\chi=2-2g-b$: $0=2-2g-2$ gives $g=0$. A genus-$0$ surface with two boundary circles is an annulus/cylinder, i.e. a sphere with two disjoint open discs removed. $\blacksquare$

**Open lateral shell, deciding datum.** The vanishing $\chi$ does **not** by itself indicate a torus: a torus is the *closed* ($b=0$) genus-$1$ surface, whereas a torus with two open discs removed has $g=1,b=2,\chi=-2\ne0$. The boundary count is what distinguishes the cases. The shell is exactly the three side walls of a triangular prism-like band with both ends open; no cap faces close the two rims.

## 6. Central-band geometry

> **Theorem 3 (principal cross-section).** Let $T$ be the **filled** equilateral triangle with corners
> $$
> C_1=(-\tfrac12,0),\quad C_2=(\tfrac12,0),\quad C_3=(0,\tfrac{\sqrt3}{2}).
> $$
> For every height $|z_0|\le s/2$, the shell meets the plane $z=z_0$ in the **triangle perimeter**,
> $$
> S\cap\{z=z_0\}=\partial T\times\{z_0\},
> $$
> a closed curve of three unit segments and zero planar area. The **enclosed** planar region is $T$, with side exactly $1$, altitude $\tfrac{\sqrt3}{2}$, area $\tfrac{\sqrt3}{4}$, inradius $\tfrac{\sqrt3}{6}$, and circumradius $\tfrac{\sqrt3}{3}$; these belong to $T$, not to the zero-thickness section curve.

**Proof.** For $|z_0|\le s/2$ each panel is full-width there (the section cuts the central rectangular band of each octagon, between its chamfers). Panel $P_2$ contributes the segment $[C_1,C_2]$; the folded panels $P_1,P_3$ contribute $[C_3,C_1]$ and $[C_2,C_3]$, where $C_3=(0,\tfrac{\sqrt3}{2})$ is the closed far seam of Theorem 2. Their union is $\partial T$. The interior point $(0,\tfrac{\sqrt3}{6},z_0)$ (the centroid) lies in $T$ but is **not** on $S$, confirming the section is the boundary curve, of planar measure zero — not a filled region. The side lengths $|C_1C_2|=|C_2C_3|=|C_3C_1|=1$ follow from the coordinates; the altitude is the point-to-line distance from $C_3$ to $C_1C_2$, the area the shoelace value $\tfrac{\sqrt3}{4}$, and the inradius/circumradius the area-over-semiperimeter and $abc/4A$ values — all computed from the corner coordinates. $\blacksquare$

**Central-band height.** The band of each octagon between its upper and lower chamfers spans $|z|\le s/2$, so its height is
$$
2\cdot\tfrac{s}{2}=s=\sqrt2-1 .
$$
This is the length of each hinge/seam edge and the height of the equilateral-section region.

**$45^\circ$ chamfer-edge inclination.** Above the band ($s/2<|z|\le\tfrac12$) each panel narrows through its four $45^\circ$ chamfer edges. In local coordinates a chamfer edge advances equal amounts $d=\tfrac{s}{\sqrt2}$ along $u$ and along $z$ (slope $1$). Folding is a rotation about a $z$-axis and preserves $z$, so every folded chamfer boundary edge still has equal vertical rise and horizontal run,
$$
|\Delta z|=\sqrt{\Delta x^2+\Delta y^2}=d,
$$
i.e. **exact $45^\circ$ inclination to the horizontal** (verified for all twelve chamfer edges). This is an *edge* inclination: each panel plane is itself **vertical** (its normal has zero $z$-component), so its plane inclination to the horizontal is $90^\circ$, not $45^\circ$; and the virtual notch plane (§8) has yet another inclination, $\arctan(2/\sqrt3)$. We therefore say "$45^\circ$ chamfer-edge inclination," never "$45^\circ$ wall."

## 7. Dihedral and normal-angle relations

The interior-dihedral and outward-normal angle conventions used here — the interior wedge between two faces, and its supplement, the angle between outward face normals — are standard [Cox73, §10.7]. The convention is background; the specific values $60^\circ$ and $120^\circ$ below come from this surface's coordinates (§4), not from the literature.

Three angles occur here and must be kept separate.

- **Fold magnitude $\beta=60^\circ$.** This is the rotation applied to each outer panel about its hinge, measured from the **reversed stacked-flat start** (§3). The reversed start places the outer panel's far-edge direction antiparallel to the middle panel (at $180^\circ$ in the $xy$-plane, relative to the outward middle direction); a rotation of $\beta=60^\circ$ brings it to the closed apex. Equivalently, measured from the *unfolded coplanar* configuration (outer panel co-directional with the middle panel, at $0^\circ$), the rotation about the hinge is $180^\circ-60^\circ=120^\circ$. The magnitude "$\pm60^\circ$" names the fold from the reversed start, and this is why the reversed local-$u$ orientation is part of the construction.
- **Interior dihedral $=60^\circ$.** Along each hinge the two adjacent panels meet at an interior wedge angle — the angle, measured inside the shell, between the two half-planes. This equals the interior angle of the equilateral cross-section, $60^\circ$.
- **Outward-normal separation $=120^\circ$.** The angle between the two outward face normals is the supplement of the interior dihedral, $180^\circ-60^\circ=120^\circ$.

> **Theorem 4 (dihedral/normal).** Let $n_1,n_2,n_3$ be the outward unit normals of $P_1,P_2,P_3$. For each adjacent pair,
> $$
> n_i\cdot n_j=-\tfrac12,\qquad\text{so the outward normals separate by }120^\circ,
> $$
> and the interior dihedral along each hinge is the supplement, $60^\circ$.

**Proof.** From the coordinates of §4, the outward normals are (up to the common orientation away from the prism axis through $(0,\tfrac{\sqrt3}{6})$)
$$
n_2=(0,-1,0),\quad n_1=(-\tfrac{\sqrt3}{2},\tfrac12,0),\quad n_3=(\tfrac{\sqrt3}{2},\tfrac12,0),
$$
each pair having dot product $-\tfrac12$. The interior wedge is measured between the inward rays and equals $\arccos(\tfrac12)=60^\circ$, the supplement of $\arccos(-\tfrac12)=120^\circ$. $\blacksquare$

The earlier request, in the pre-normalization history, for a "$120^\circ$ interior dihedral" is an angle-convention statement: $120^\circ$ is the outward-normal separation, and the interior dihedral is its supplement $60^\circ$. No geometry differs; only the label. This paper reports the interior dihedral as $60^\circ$ and the normal separation as $120^\circ$, consistently.

## 8. Chamfer notch and rim geometry

Above each rim tip the two flanking chamfer edges form a spatial **notch**. Take the upper apex tip $A=V_7=(0,\tfrac{\sqrt3}{2},\tfrac{s}{2})$ and its two actual boundary neighbours $B=V_6$ and $C=V_{16}$ (the high vertices at $z=\tfrac12$). The two incident boundary-edge vectors, computed exactly as differences of the §4 coordinates, are
$$
e_1=B-A=d\bigl(-\tfrac12,-\tfrac{\sqrt3}{2},1\bigr),\qquad
e_2=C-A=d\bigl(\tfrac12,-\tfrac{\sqrt3}{2},1\bigr),\qquad d=\tfrac{s}{\sqrt2}.
$$

> **Theorem 5 (notch).** Each notch is a triangle with side lengths $s,s,d$, tip angle
> $$
> \alpha_{\mathrm{notch}}=\arccos\!\Bigl(\tfrac34\Bigr)\approx41.4096221093^\circ,
> $$
> and base angles $\arccos\!\bigl(\tfrac{\sqrt2}{4}\bigr)=\tfrac{\pi-\arccos(3/4)}{2}\approx69.2951889454^\circ$. Its **axial projection** (dropping the $z$-component) is an equilateral triangle of side $d$ with $60^\circ$ angles. The notch plane meets the horizontal at $\arctan(2/\sqrt3)\approx49.1066053509^\circ$, and the areas are
> $$
> A_{\mathrm{notch,\,spatial}}=\tfrac{\sqrt7}{8}\,s^2,\qquad
> A_{\mathrm{notch,\,projected}}=\tfrac{\sqrt3}{8}\,s^2 .
> $$

**Proof.** From the exact vectors above,
$$
|e_1|^2=|e_2|^2=d^2\bigl(\tfrac14+\tfrac34+1\bigr)=2d^2=s^2,\qquad
e_1-e_2=(-d,0,0),\qquad
e_1\cdot e_2=d^2\bigl(-\tfrac14+\tfrac34+1\bigr)=\tfrac32 d^2=\tfrac34 s^2,
$$
so the two legs have length $s$, the base $|e_1-e_2|=d$, and the tip cosine is $\dfrac{e_1\cdot e_2}{|e_1||e_2|}=\dfrac{3}{4}$. The base angle is computed directly (not inferred from the angle sum): at $B$ the incident notch edges are $-e_1$ (toward $A$) and $e_2-e_1$ (toward $C$), and
$$
\frac{(-e_1)\cdot(e_2-e_1)}{s\,d}=\frac{\sqrt2}{4}=\sin\!\tfrac{\alpha_{\mathrm{notch}}}{2},
$$
symmetrically at $C$; both base angles are the unique acute $\arccos(\tfrac{\sqrt2}{4})$. Dropping $z$ gives $e_1^\perp=d(-\tfrac12,-\tfrac{\sqrt3}{2})$, $e_2^\perp=d(\tfrac12,-\tfrac{\sqrt3}{2})$ with $|e_1^\perp|=|e_2^\perp|=|e_1^\perp-e_2^\perp|=d$: the projection is equilateral, all $60^\circ$. The cross product $e_1\times e_2=d^2(0,1,\tfrac{\sqrt3}{2})$ gives $A_{\mathrm{spatial}}=\tfrac12|e_1\times e_2|=\tfrac{\sqrt7}{4}d^2=\tfrac{\sqrt7}{8}s^2$ and $A_{\mathrm{projected}}=\tfrac12|e_1^\perp\times e_2^\perp|=\tfrac{\sqrt3}{4}d^2=\tfrac{\sqrt3}{8}s^2$; its normal $(0,1,\tfrac{\sqrt3}{2})$ has horizontal-to-vertical component ratio $2/\sqrt3$, so the notch-plane inclination is $\arctan(2/\sqrt3)$. $\blacksquare$

(The earlier draft's displayed "$e_1$-type" vector was not an incident edge difference — for that vector $|v|^2-s^2=s/4\ne0$; the exact vectors above replace it. The notch identities themselves are unchanged.)

**Spatial angle $\ne$ projected angle.** This is the key distinction: the true three-dimensional notch angle is $\arccos(3/4)\approx41.41^\circ$, while its shadow in the axial ($xy$) plane is the equilateral $60^\circ$. A drawing that shows only the axial projection therefore reads $60^\circ$ and hides the actual $41.41^\circ$ spatial opening. The notch plane meets the horizontal at $\arctan(2/\sqrt3)\approx49.1066^\circ$.

**Rim decomposition (curve vs enclosed region).** Each open rim is a nonplanar nine-edge **closed curve** of edge length $s$, perimeter $9s$; it is not contained in the plane $z=\pm\tfrac12$ (its corner tips sit at $z=\pm\tfrac{s}{2}$). Its axial **projection** is the perimeter of the triangle $T$, each side split $d,s,d$ (with $2d+s=1$) — again a curve of zero planar area. The associated **enclosed** projected regions decompose $T$: the six high rim vertices, in cyclic order $(5,6,16,17,12,13)$, bound a central equiangular hexagon (six $120^\circ$ angles, sides alternating $s,d$), and the three corners of $T$ are cut off by the three projected notch triangles (equilateral, side $d$; disjoint interiors since $0<d<\tfrac12$). The hexagon area, by shoelace and equivalently by removing the three corner triangles, is
$$
A_{\mathrm{hexagon}}=\tfrac{\sqrt3}{4}\bigl(1-3d^2\bigr)=\tfrac{\sqrt3(3+4\sqrt2)}{8}s^2=-\tfrac{7\sqrt3}{8}+\tfrac{3\sqrt6}{4},
$$
and the partition of the enclosed region is exact:
$$
A_{\mathrm{hexagon}}+3\,A_{\mathrm{notch,\,projected}}=\tfrac{\sqrt3}{4}=A_{T}.
$$
These are **virtual enclosed measurement regions**, not mesh or cap faces: the rim curve itself has planar area zero, and the shell has no caps. The lower rim follows by the reflection $z\mapsto-z$.

In Paper D's aligned measurement family, these six high vertices give the member with connector length $g_{\mathrm{gap}}=d=s/\sqrt2$ [PD]. Its equiangular hexagon has alternating lengths $s,d$ and is not the equal-sided member. Paper D, Sections 12-14, distinguishes that planar measurement polygon from this nonplanar nine-edge rim and describes two changes that reach the equal-sided member. Neither is a common rescaling of this welded module. In the fixed-vertical-face-centre shrink of the original width-one module, the six measurement sides become $1/3$, the octagon width becomes $(1+\sqrt2)/3$, and the top height becomes $(1+\sqrt2)/6$; the original seams are lost. Those consequences do not change the width-one definition, rim or mesh of the present paper.

## 9. Symmetry

$D_{3h}$ is a standard Schoenflies point group: order $12$, with a $C_3$ principal axis, three $C_2'$ axes, three vertical mirror planes $\sigma_v$, a horizontal mirror plane $\sigma_h$, and two $S_3$ operations, and $D_{3h}\cong D_3\times C_s$ [Cotton90, AH94]. That is the group's standard description and terminology. The theorem below is the separate, model-specific statement that **this particular surface realizes exactly $D_{3h}$**; it is proved here by a lower bound (twelve exhibited symmetries) and a matching upper bound, not quoted from the group tables.

> **Theorem 6 (symmetry group).** The Euclidean symmetry group of the unlabelled welded surface $S$ (equivalently of its geometric face complex) is $\operatorname{Sym}(S)=D_3\times C_s\cong D_{3h}$, of order $12$.

**Proof — lower bound (twelve symmetries).** Three generators, each an isometry mapping the three octagonal **faces** (each the convex hull of its vertex cycle) onto faces:
- $C_3$: rotation by $120^\circ$ about the vertical axis through the cross-section centroid $(0,\tfrac{\sqrt3}{6})$. It cyclically permutes the panels and the seams $C_1\to C_2\to C_3\to C_1$.
- $\sigma_v$: reflection through $x=0$; fixes $P_2$ and swaps $P_1\leftrightarrow P_3$.
- $\sigma_h$: reflection through $z=0$; swaps the top and bottom rims (each octagon is symmetric about $z=0$).
Since each generator maps each octagon's vertex cycle onto another octagon's vertex cycle and a face is the convex hull of its cycle, the generators map **whole faces** to faces (and edges to edges). $\langle C_3,\sigma_v\rangle\cong D_3$ (order $6$); adjoining $\sigma_h$, which commutes with both, gives $D_3\times\{E,\sigma_h\}=D_{3h}$ of order $12$, elements $\{E,2C_3,3\sigma_v,\sigma_h,2S_3,3C_2'\}$, with $S_3=\sigma_h C_3$.

**Proof — upper bound (no further symmetries).** In the topological interior of $S$ the points lacking a flat (planar) neighbourhood are exactly the interiors of the three non-flat seams (face interiors are flat; a two-face seam wedge is not; the embedding argument of Theorem 1b excludes any other coincidences). These three intrinsic crease components close to three **equal, parallel, vertical segments** $K_i=\{(C_i,z):|z|\le\tfrac{s}{2}\}$. Any Euclidean symmetry of $S$ must permute $\{K_1,K_2,K_3\}$; hence it preserves their common (unoriented) vertical direction and fixes their midpoint centroid $O_c=(0,\tfrac{\sqrt3}{6},0)$. In coordinates centred at $O_c$ it therefore has the block form $(r,z)\mapsto(Br,\varepsilon z)$ with $B\in O(2)$, $\varepsilon\in\{+1,-1\}$. The three midpoint footprints form an equilateral triangle, so $B$ is one of its six planar dihedral symmetries; $\varepsilon$ is independent. Thus $|\operatorname{Sym}(S)|\le 6\times2=12$. The twelve maps above are distinct and all preserve $S$, so the bounds meet:
$$
\operatorname{Sym}(S)=D_3\times C_s\cong D_{3h},\qquad |\operatorname{Sym}(S)|=12. \qquad\blacksquare
$$

This is the symmetry of the unlabelled surface/face complex (panel permutation allowed), not a claim that material labels are fixed. The **finite 18-vertex set** has the same group here, but by its own argument, not automatically: its centroid is $O_c$ and its covariance matrix in centred coordinates is $\operatorname{diag}\bigl(\tfrac{1+s^2}{12},\tfrac{1+s^2}{12},\tfrac{2+s^2}{12}\bigr)$, whose distinct vertical eigenvalue forces every vertex-set symmetry to preserve the vertical axis; the six vertices at $|z|=\tfrac{s}{2}$ (footprints $C_1,C_2,C_3$) then give the same $6\times2$ bound, and the twelve maps realize it. The group is $D_{3h}$, not a higher cyclic or dihedral group, and specifically **not** the historical $D_{24}$ (see §10). The independent audit confirms $C_3^3=\mathrm{id}$ pointwise, $C_3\ne\mathrm{id}$, $\sigma_v^2=\sigma_h^2=\mathrm{id}$, the conjugation $\sigma_vC_3\sigma_v=C_3^{-1}$, the commutation $\sigma_hC_3=C_3\sigma_h$, and the face/edge permutation action (§10, Appendix C).

The upper-bound argument above uses the three intrinsic crease components of the welded surface. It therefore remains tied to that surface and is not transferred by name to separated panels or reference frames. Paper D [PD], Section 10, distinguishes the $D_6$ symmetry of an unmarked regular planar hexagon from its $D_3$ edge/connector-role symmetry; these are symmetries of different objects from the welded surface studied here.

## 10. Verification and historical separation

Exact arithmetic and robust geometric predicates are standard tools for avoiding floating-point ambiguity in computational geometry [Yap97, KMPSY08, Shewchuk97]; the verification here uses exact symbolic arithmetic in that spirit. These references support the *methodology*, not the specific predicate suite. The verification is stated in three cleanly separated registers (see `PAPER_C_PROOF_AUDIT_v0.2.2.md`): **analytic proofs** (Theorems 1, 1b, 2–6, in the text), **executed regression predicates** (finite symbolic/combinatorial checks), and **preserved historical/export validation** (the read-only width-1 package). These are not merged into a single "check count."

**Executed regression (this paper).** `verification/paperC/paperC_geometry_audit_v0_2_1.py` reconstructs the shell from the octagon and the general-angle fold transforms and executes **51 predicates, all PASS, spanning all 19 numbered coverage groups**. These finite checks **supplement** the analytic proofs; they do not replace them. Described faithfully by what each predicate actually executes:

- **(1–2)** apothem as support-line distance and the circumradius radical chain; octagon area by shoelace with the identity chain $4as=2(1+\sqrt2)s^2=8(\sqrt2-1)a^2=2(\sqrt2-1)w^2$ and refutation of the bad apothem formula.
- **(3)** symbolic free-edge gap and $y,z$ agreement; the exact restricted solve on $[0,\pi]$ (unique $\beta=\tfrac\pi3$); and finite checks at two closing-angle representatives and one non-closing angle. **The complete unrestricted solution family is proved analytically in Theorem 2.**
- **(4)** hinges fixed for all $\beta$ (symbolic) and map isometry.
- **(5)** connectivity of the $1$-skeleton and panel-adjacency triangle.
- **(6)** interval vertex links and edge incidence.
- **(7)** coherent orientation via each directed edge used once and each seam traversed oppositely.
- **(8)** Euler characteristic, two degree-two boundary components, and the genus arithmetic $g=(2-b-\chi)/2=0$ — **used alongside** the analytic manifold/orientability/boundary proof of Theorem 1b (the surface hypotheses themselves are proved there, not asserted by these counts).
- **(9)** projected endpoint comparisons for $P_1$ and $P_2$, centroid exclusion (the section is a curve, not a region), and width-formula evaluations at $z=h$ and $z=a$. **The quantified all-height cross-section and the maximal-band statement are proved analytically in §6.**
- **(10–12)** coordinate-derived triangle altitude (point-to-line), shoelace area, inradius, and circumradius.
- **(13)** the co-directional-strip $120^\circ$ rotation reproducing the final $P_1'$.
- **(14–16)** the exact notch vectors, tip cosine $\tfrac34$, derived base cosine $\tfrac{\sqrt2}{4}$, three projected sides $=d$, plane inclination $\arctan(2/\sqrt3)$, and spatial/projected areas.
- **(17)** the hexagon's alternating sides, six $120^\circ$ angle cosines, exact area, and the partition identity $A_{\mathrm{hex}}+3A_{\mathrm{notch,proj}}=\tfrac{\sqrt3}{4}$.
- **(18–19)** $C_3^3=\mathrm{id}$ pointwise, $C_3\ne\mathrm{id}$, reflection squares, the $D_3$ conjugation and $\sigma_h$-commutation relations, and the face/edge permutation action of each generator.
- plus the regression against the authoritative spec welded-coordinate table.

Every predicate executes a real computation on reconstructed data — **no literal-`True` and no expected-minus-itself checks**. The suite does **not** by itself prove the complete closure family, the quantified all-$z$ section / maximal-band statement, the interior-dihedral theorem, the boundary sign separation, the chamfer-edge theorem, or the full $D_{3h}$ upper bound; each of those is the analytic argument of §§5–9 (finite sampling does not prove them). The v0.1 harness, by contrast, advertised "46/46 independent checks" but contained $3$ tautological and $10$ weak predicates and left $19$ coverage groups untested; that claim is withdrawn.

**Preserved historical/export validation.** The read-only width-1 package records **26 construction entries and 46 export-validation predicates**. Of the 26 construction entries, **24 execute conditions and two are informational PASS records** (a printed dihedral cosine and a printed closure-gap expression, each without a comparison; the value is tested by a neighbouring record). The export validator reads the serialized OBJ/CSV/JSON **without importing the builder**, but its predicates overlap in purpose: they combine direct numerical geometry checks, exact scaling/serialization consistency, metadata/status validation (one predicate merely reads the 26 builder statuses), and archive-hash preservation. They are **not 72 mathematically independent confirmations**; the total is a useful, partly overlapping record set, and its historical files are unchanged.

**Historical separation (brief).** The welded folded shell of this paper is a specific object and should not be conflated with older, different constructions:
- Concentric three-octagon "$\mathbb Z_{24}$/$D_{24}$" pictures are *not* this welded shell; they describe a different (nested, planar) arrangement and a different symmetry label. The symmetry group established here is $D_{3h}$ (§9).
- The folded shell has **18 actual welded vertices**, not a uniform $24$-point angular lattice; the count follows from the three seam welds (§5).
- Earlier projection drawings (which show the $60^\circ$ axial notch and the concentric outline) do not override the exact coordinates of §4; where a projection and the coordinates disagree, the coordinates govern. This is recorded to keep the labels straight, not to dispute the older diagrams as diagrams.

## 11. Limitations

- **The unit width is a normalization, not a physical scale.** All lengths scale uniformly with the chosen unit; no metric, material, or physical dimension is attached.
- **Zero thickness.** Panels are ideal zero-thickness polygons; no material, offset, or self-intersection-avoiding motion is modelled. The stacked-flat start overlaps, and intermediate fold stages intersect; no collision-free physical folding is asserted.
- **Open shell, no volume.** The shell has two open rims; no enclosed volume is assigned.
- **No inner geometry.** Only the three-panel outer shell is treated. Any inner mechanism is out of scope.
- **No physical/interpretive content.** No quantum, particle, propulsion, spacetime, memory-system, or symmetry-as-physics claim is made or implied; the geometry stands alone.

## 12. Conclusion

Three regular octagonal panels, each normalized to flat-to-flat width $1$ (edge $s=\sqrt2-1$), admit an exact symmetric folded realization whose welded lateral shell has $V=18$, $E=21$, $F=3$, Euler characteristic $0$, one connected component, three vertical seams, and **two open nine-edge boundaries** ($9s$ each). As a connected, compact, orientable $2$-manifold with boundary and two boundary components, it has genus $0$ and is an **annulus — a sphere with two disjoint open discs removed** — not a closed polyhedron and not a (punctured) torus: the boundary is the deciding datum. Every horizontal section through the central band meets the shell in the **perimeter** of an equilateral triangle of side exactly $1$ (area, inradius, and circumradius belong to the enclosed filled triangle, not to the section curve); the interior dihedral is $60^\circ$ and the outward-normal separation is $120^\circ$; the twelve chamfer boundary edges have exact $45^\circ$ inclination to the horizontal while the panel planes are vertical; the spatial notch angle is $\arccos(3/4)\approx41.4096^\circ$, distinct from its equilateral $60^\circ$ axial projection; and the exact Euclidean symmetry group of the surface is $D_{3h}$, established with both a twelve-element realization and a matching upper bound. All coordinates and derived angles are available in closed form. The analytic results are supported by $51$ executed symbolic/combinatorial regression predicates spanning $19$ numbered coverage groups; these finite checks supplement, but do not replace, the analytic proofs. No physical interpretation is claimed.

---

## Appendix A — Exact dimension table (normalization $w=1$)

| Quantity | Exact | Numerical |
|---|---:|---:|
| octagon edge $s$ | $\sqrt2-1$ | $0.414213562373095$ |
| flat-to-flat width $w$ | $1$ | $1$ |
| apothem | $\tfrac12$ | $0.5$ |
| circumradius $R$ | $\tfrac{(2-\sqrt2)\sqrt{2+\sqrt2}}{2}$ | $0.541196100146197$ |
| chamfer cutback $d$ | $1-\tfrac{\sqrt2}{2}$ | $0.292893218813452$ |
| hinge / seam length | $\sqrt2-1$ | $0.414213562373095$ |
| central-band height | $\sqrt2-1$ | $0.414213562373095$ |
| principal equilateral side | $1$ | $1$ |
| principal equilateral altitude | $\tfrac{\sqrt3}{2}$ | $0.866025403784439$ |
| principal equilateral inradius | $\tfrac{\sqrt3}{6}$ | $0.288675134594813$ |
| principal equilateral circumradius | $\tfrac{\sqrt3}{3}$ | $0.577350269189626$ |
| interior dihedral | $60^\circ$ | $60$ |
| outward-normal separation | $120^\circ$ | $120$ |
| chamfer-edge inclination to horizontal | $45^\circ$ | $45$ |
| panel-plane inclination to horizontal | $90^\circ$ | $90$ |
| notch tip angle | $\arccos(3/4)$ | $41.4096221093$ |
| notch base angles | $\tfrac{\pi-\arccos(3/4)}{2}$ | $69.2951889454$ |
| notch plane vs horizontal | $\arctan(2/\sqrt3)$ | $49.1066053509$ |
| rim perimeter (each) | $9(\sqrt2-1)$ | $3.72792206135786$ |
| total boundary length | $18(\sqrt2-1)$ | $7.45584412271571$ |
| octagon area | $2\sqrt2-2$ | $0.82842712474619$ |
| principal equilateral area | $\tfrac{\sqrt3}{4}$ | $0.433012701892219$ |
| spatial notch area | $\tfrac{\sqrt7}{8}(\sqrt2-1)^2$ | $0.0567423949557361$ |
| projected notch area | $\tfrac{\sqrt3}{8}(\sqrt2-1)^2$ | $0.0371466171425345$ |

## Appendix B — Boundary loops (welded indices)

Top rim ($z>0$): $4\to5\to6\to7\to16\to17\to11\to12\to13\to4$.
Bottom rim ($z<0$): $0\to1\to2\to3\to8\to9\to10\to14\to15\to0$.
Each is a $9$-cycle of edges of length $s$; the two loops are disjoint and are exchanged by $\sigma_h$.

## Appendix C — Independent audit summary

`verification/paperC/paperC_geometry_audit_v0_2_1.py` (pure sympy; no source, kernel, or builder import) reconstructs the shell from the octagon and the **general-angle** fold transforms and executes **51 regression predicates across all 19 numbered coverage groups** (§10), all PASS, including the regression against the authoritative welded coordinate table. Every predicate is a real computation on reconstructed data (no literal-`True`, no expected-minus-itself); nested-radical equalities use sympy's exact symbolic prover. The count is an execution count of finite symbolic/combinatorial predicates that **supplement** the analytic proofs — it is **not** a count of independent theorems. Several results are owned by the analytic arguments, not by these finite checks: the complete closure solution family (§5), the quantified all-$z$ section and maximal-band statement (§6), the interior-dihedral relation (§7), the boundary sign separation (§5), the chamfer-edge inclination (§6), and the full-group $D_{3h}$ upper bound (§9). v0.2.1 changed only two predicate names and several descriptions from v0.2; the predicate logic is unchanged. The original `paperC_geometry_audit.py` (v0.1) and `paperC_geometry_audit_v0_2.py` (v0.2) are preserved unchanged.

---

## References

The existing background references and their verification note remain in the companion [bibliography](../../PAPER_C_REFERENCES_v0.2.md). These references supply background and terminology, not a model-specific theorem of this paper. The added [PD] reference identifies the approved scaffold comparison and its separate construction.

- **[Cox73]** H. S. M. Coxeter. *Regular Polytopes.* 3rd ed., Dover, 1973. ISBN 0-486-61480-8.
- **[Cox69]** H. S. M. Coxeter. *Introduction to Geometry.* 2nd ed., John Wiley & Sons, 1969.
- **[DO07]** E. D. Demaine, J. O'Rourke. *Geometric Folding Algorithms: Linkages, Origami, Polyhedra.* Cambridge University Press, 2007. DOI 10.1017/CBO9780511735172.
- **[Tachi09]** T. Tachi. "Simulation of Rigid Origami." In R. J. Lang (ed.), *Origami 4: Fourth International Meeting of Origami Science, Mathematics, and Education*, A K Peters, 2009, pp. 175–187.
- **[Massey91]** W. S. Massey. *A Basic Course in Algebraic Topology.* Springer GTM 127, 1991. ISBN 978-0-387-97430-9.
- **[GX13]** J. Gallier, D. Xu. *A Guide to the Classification Theorem for Compact Surfaces.* Springer, Geometry and Computing 9, 2013. DOI 10.1007/978-3-642-34364-3.
- **[Hatcher02]** A. Hatcher. *Algebraic Topology.* Cambridge University Press, 2002. ISBN 978-0-521-79540-1.
- **[RS72]** C. P. Rourke, B. J. Sanderson. *Introduction to Piecewise-Linear Topology.* Springer, Ergebnisse der Mathematik 69, 1972; 1982 revised Study Edition printing, DOI 10.1007/978-3-642-81735-9.
- **[Cotton90]** F. A. Cotton. *Chemical Applications of Group Theory.* 3rd ed., Wiley, 1990. ISBN 0-471-51094-7.
- **[AH94]** S. L. Altmann, P. Herzig. *Point-Group Theory Tables.* Clarendon Press, Oxford, 1994.
- **[Yap97]** C. K. Yap. "Towards exact geometric computation." *Comput. Geom.* **7**(1–2):3–23, 1997. DOI 10.1016/0925-7721(95)00040-2.
- **[KMPSY08]** L. Kettner, K. Mehlhorn, S. Pion, S. Schirra, C. Yap. "Classroom examples of robustness problems in geometric computations." *Comput. Geom.* **40**(1):61–78, 2008. DOI 10.1016/j.comgeo.2007.06.003.
- **[Shewchuk97]** J. R. Shewchuk. "Adaptive precision floating-point arithmetic and fast robust geometric predicates." *Discrete Comput. Geom.* **18**(3):305–363, 1997. DOI 10.1007/PL00009321.

---

**[PD]** Hilmir Frímann Halldórsson. *Tri-Octagon Reference-Scaffold Geometry: Exact Construction of an Alternating Hexagonal Core*. Paper D, revision v0.1.1, 23 September 2026. Accepted publication artifact, prepared for repository publication. [Approved v0.1.1 PDF](../../../PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf).
