# Tri-Octagon hexagon core derivation v0.1

Codex, 2026-09-23, amended after Hilmir Frímann Halldórsson's author design clarification. **Historical source statements, author clarification and independent derivations are distinct.** The intended object is a six-segment reference scaffold. The earlier filled-hole interpretation is retained only as a separate conditional theorem.

**Corrected result:** the author's intended alternating edge/connector scaffold has an exact realization. With selected edge length s and midpoint radius p in the aligned C3 family proved in §6, the connector length is g=√3p−s/2. It is a regular hexagon exactly when g=s, hence p=√3s/2. The filled planar hole interpretation is impossible under §2's stated assumptions; that is **not an obstruction to the intended scaffold**, whose three connectors are deliberate reference segments. Paper C's top measurement polygon belongs to this same planar family at g/s=1/√2. Changing its placement to g/s=1 would separate its finite faces; no change has been implemented. The independently recovered dual-tetrahedral core in §3 remains a separate construction with an unselected scale relation to s.

## 1. Recovered conditions, and what is not supplied

Source P02 is [Recursive Engines](C:/TORMENT/TRIOCTAGON_new/pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.pdf), printed2025-11-24. Its p2 (1)–(3) supplies

\[
C_i=L(\cos\phi_i,\sin\phi_i),\quad\phi_i=2\pi i/3,\quad L>R,
\]
\[
V_{ik}=C_i+R(\cos(\theta_0+k\pi/4),\sin(\theta_0+k\pi/4)),
\]

followed by a tilt around tangent-axis directions. It does not supply a unique L/R, affine pivot, selected tilt or list of six actual inner boundary segments. Its main text calls a projected core nearly regular (p14 §5.4); AppendixF gives an independent exact regular construction (pp20–22 (29)–(49)). These are retained as different levels of specification.

Let octagon side s>0 and define

\[
R=\frac{s}{2\sin(\pi/8)}=\frac{s}{2}\sqrt{4+2\sqrt2},\qquad
a=\frac{1+\sqrt2}{2}s,\qquad w=2a.
\tag{D1}
\]

No condition fixes the independent tetrahedral scale t. Setting t to a multiple of s would be additional model data.

## 2. Exact obstruction to the filled planar hole interpretation only

**Hypotheses:** finitely many closed filled regular octagons in one Euclidean plane, with pairwise disjoint interiors. The proposed hole is a component of their complement; its six straight boundary segments are actual octagon sides or portions of them, not virtual connector chords. Zero thickness does not mean deleting the polygon interiors for this statement.

At a vertex v of a regular hexagonal hole, the free-space interior angle must be120°. Therefore occupied polygon sectors around v must lie within the complementary240° sector.

If the two bounding rays belong to different octagons, each incident octagon occupies at least135° locally:135° at an octagon vertex,180° if v lies in an edge interior. Since the interiors cannot overlap, they occupy at least270°, exceeding the available240°. Equivalently their free sector is at most90°. A regular hexagonal corner would require at least30° of overlap.

If both rays are adjacent sides of the same octagon, its occupied angle is135° and the adjacent exterior free sector is225°, not120°. Two collinear portions give a straight angle, not a hexagon vertex. Any extra polygon that clips the free sector introduces a boundary ray from a different octagon, reducing to the first case.

Thus such a regular hexagonal hole is impossible. This conclusion is independent of octagon size, centres, orientations and the number of other octagons. It already prevents the stronger requirement that all six exposed lengths equal s.

For P02's **literal shared-orientation** family there is a separate obstruction even if overlaps are allowed: every exposed straight side has an undirected line angle

\[
\theta_0+\pi/8+\pi/2+k\pi/4\pmod\pi.
\]

These directions differ by multiples45°. Consecutive regular-hexagon sides require60° modulo180°, which is not among them. Translation cannot change this. Replacing the shared orientation by a C3-covariant orientation would alter the source conditions and does not remove the non-overlap obstruction above.

**Scope:** this is not a prohibition on overlapping wireframes, selected projected 3D edges, additional connector segments, or different polyhedral constructions. The author has now clarified that the intended construction uses three added gap connectors. Its conditions and positive construction are given in §6. The theorem here remains valid but does not test that intended object.

![Angle obstruction and antipodal convention](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/figures/03_obstruction_and_antipodes.png)

There is no solution in this filled, interior-disjoint, actual-side-only planar class. The figure illustrates that conditional obstruction. The new figures in §6 illustrate the different, author-clarified scaffold and do not purport to be counterexamples to this theorem.

## 3. Source-supported exact dual core

P02 (29)–(34), PDFp20, defines at unit scale the tetrahedron with vertices

\[
v_1=(1,1,1),\ v_2=(1,-1,-1),\ v_3=(-1,1,-1),\ v_4=(-1,-1,1),
\quad T_-=-T_+.
\]

We introduce the explicit homogeneous scale t>0 solely to track units. Put

\[
n=(1,1,1)/\sqrt3,\ e_1=(1,-1,0)/\sqrt2,\ e_2=(1,1,-2)/\sqrt6,
\quad \Pi(x)=(x\cdot e_1,x\cdot e_2).
\tag{D2}
\]

The frame is orthonormal. The projected vertex tv₁ is zero and the others are

\[
p_1=t(\sqrt2,\sqrt{2/3}),\quad
p_2=t(-\sqrt2,\sqrt{2/3}),\quad
p_3=t(0,-2\sqrt{2/3}).
\tag{D3}
\]

Each pairwise squared distance is8t², so Δ₊=conv{p₁,p₂,p₃} is equilateral with side2√2t. The opposite tetrahedron projects to Δ₋=−Δ₊. The union of their edges is the regular hexagram described by P02 (43)–(49). This recovers a core; it does not place it inside finite octagon panels.

### Central intersection hexagon

**Independent derivation from those source coordinates:** write h=2√2t/3. Intersecting the six triangle half-planes gives

\[
H_k=h(\cos(k\pi/3),\sin(k\pi/3)),\quad k=0,\ldots,5.
\tag{D4}
\]

Explicitly, after factoring t/3,

\[
(2\sqrt2,0),\ (\sqrt2,\sqrt6),\ (-\sqrt2,\sqrt6),\
(-2\sqrt2,0),\ (-\sqrt2,-\sqrt6),\ (\sqrt2,-\sqrt6).
\]

For dₖ=Hₖ₊₁−Hₖ (indices modulo6),

\[
|d_k|^2=h^2,\qquad
\frac{(-d_{k-1})\cdot d_k}{h^2}=-\frac12,\qquad
\sum_{k=0}^{5}d_k=0.
\tag{D5}
\]

These prove six equal sides, six120° interior angles and exact closure. Rotation byπ/3 permutes the vertices, as does reflection y↦−y. Its full planar symmetry group is D6 (order12), including C3 and D3 subgroups.

\[
\text{side}=\text{circumradius}=h=\frac{2\sqrt2}{3}t,\quad
\text{inradius}=\frac{\sqrt3}{2}h=\sqrt{2/3}\,t,\quad
\text{area}=\frac{3\sqrt3}{2}h^2=\frac{4\sqrt3}{3}t^2.
\tag{D6}
\]

The six hexagon sides lie along the **projected triangle** edges. They are not recovered octagon boundary sides. Requiring h=s would select `t=3s/(2√2)`, but the source never imposes this identification; it leaves L and α wholly undetermined.

### The other central hexagon

The eight tetrahedral halfspaces give

\[
T_+\cap T_-=\{x:|x_1|+|x_2|+|x_3|\le t\}
=\operatorname{conv}\{\pm te_1^{\rm cart},\pm te_2^{\rm cart},\pm te_3^{\rm cart}\}.
\tag{D7}
\]

Projecting this regular octahedron gives the regular hexagon

\[
H'_k=\sqrt{2/3}\,t\bigl(\cos(\pi/6+k\pi/3),\sin(\pi/6+k\pi/3)\bigr).
\tag{D8}
\]

Its side/circumradius is√(2/3)t, inradius t/√2. It is rotated30° relative to H and has side ratio√3/2. Thus

\[
\Pi(T_+\cap T_-)\ne\Pi(T_+)\cap\Pi(T_-).
\]

Both are exact, but they answer different geometric questions. A common “inner hexagon” label does not identify them.

![Two exact core hexagons and dimensions](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/figures/02_exact_core_dimensions.png)

P02 p22's plane-mirror wording does not follow from AppendixF's point inversion. For a viewing plane perpendicular to n, reflection x↦x−2(x·n)n satisfies Π(reflect x)=Π(x); point inversion satisfies Π(−x)=−Π(x). Only the latter gives the opposite triangle in this construction.

## 4. Tilt family versus Paper C

This section is **Codex's conditional comparison**, not a recovered historical parameter selection. It does not propose a new model.

Let uᵢ=(cosφᵢ,sinφᵢ,0), tᵢ=(−sinφᵢ,cosφᵢ,0), e_z=(0,0,1). Introduce an affine tangent-axis pivot Pᵢ=p uᵢ. For a planar point Cᵢ+x uᵢ+y tᵢ, rigid rotation by α around that axis gives

\[
F_i=[p+(L-p+x)\cos\alpha]u_i+y t_i-(L-p+x)\sin\alpha\,e_z.
\tag{D9}
\]

The supporting planes have normals and offsets

\[
n_i=\sin\alpha\,u_i+\cos\alpha\,e_z,\qquad
n_i\cdot F_i=p\sin\alpha,
\quad n_i\cdot n_j=(3\cos^2\alpha-1)/2\ (i\ne j).
\tag{D10}
\]

For0<α<π/2 the three planes meet at Q=(0,0,p tanα). Their pairwise intersection lines are concurrent. A horizontal section of the infinite halfspace chamber can be triangular; projecting concurrent lines does not turn them into the three sides of a nondegenerate triangle. Finite octagon panels need additional contact checks before those supporting-plane sections can be called physical boundaries. Existing Layer-0 corrections explicitly demonstrate this distinction.

P02's literal matrix rotation is p=0. Choosing p=L or an inner-edge pivot is an extra interpretation. Likewise, the C3-covariant finite-panel model uses orientation θ₀+φᵢ+kπ/4, whereas P02 (2) uses shared θ₀+kπ/4. These are not silently merged.

Paper C's final supporting planes are vertical and enclose an equilateral central section; their pairwise intersection lines are parallel. They have no finite triple intersection. Consequently a generic concurrent tilt configuration cannot be a rigid coordinate transform of the Paper-C planes.

### An explicit conditional realization

There is nevertheless an exact map at the **additional boundary choice α=π/2**, if one first allows the C3-covariant orientations and selects p=a/√3. This establishes a possible mathematical relationship, not historical provenance.

Use octagon local coordinates

\[
\mathcal O=\{(\pm a,\pm s/2),(\pm s/2,\pm a)\}.
\]

Choose the original radial/tangential local coordinates `(x,y)=(-z,u)` for (u,z)∈O. This is the covariant octagon phase θ₀=π/8 moduloπ/4. Starting from any L>R, rotate byπ/2 around Pᵢ and apply the common vertical translation `(L−p)e_z`. Equation(D9) becomes

\[
\widetilde F_i(u,z)=p u_i+u t_i+z e_z.
\]

Then the rigid transformation

\[
M_i(u,z)=R_z(\pi/6)\widetilde F_i(u,z)+(0,a/\sqrt3,0)
\tag{D11}
\]

gives, for i=0,1,2 respectively, Paper-C panels3,1,2:

\[
P_1=(-a/2-u/2,\sqrt3a/2-\sqrt3u/2,z),\quad
P_2=(u,0,z),\quad
P_3=(a/2-u/2,\sqrt3a/2+\sqrt3u/2,z).
\tag{D12}
\]

The independent verifier compares all eight vertex images per panel exactly. Final panel centre-radius about the centroid is p=a/√3; original planar centre-radius L remains arbitrary and is removed from the final placement by the translation. No collision-free deployment or historical90° fold selection is asserted. Paper C's own **hinge fold magnitude** is60° from its reversed stacked start, a different motion and angle from α in this comparison.

The actual module has18 welded vertices,21 edges,3 faces,3 shared seams and two nonplanar9-edge boundary cycles. Its central section side is w=(1+√2)s. Its six high-rim vertices bound a **measurement** hexagon with alternating sides

\[
s,\quad d=s/\sqrt2,\quad s,\quad d,\quad s,\quad d.
\]

All its angles are120°, but d≠s for s>0. The d segments are partition chords, not extra mesh edges. Neither the actual9-edge rim nor this unequal6-edge measurement polygon proves H2. These are Paper C's existing results, retained without amendment.

![Tilt and local shell comparison](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/figures/04_tilt_and_local_shell.png)

**Classification:** D, a distinct specified construction. A (component of a larger historical host), B (intended replacement), and C (the same historical geometry in other coordinates) are not established by the sources. Equation(D11) is a conditional realization in an extended family, with every added assumption displayed. It does not establish a larger host or an E8 placement.

## 5. Verification and stop boundary

[verify_exact.py](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/verify_exact.py) uses exact halfspace vertex enumeration and independently transcribed coordinates; it imports no kernel or historical script. The complete bounded geometry/sign suite has42 passing predicates, including exact side lengths, angle cosines, closure, core intersections, plane identities, Paper-C vertex-set correspondence and mesh counts. Homogeneous checks at t=1 or s=1 extend by the displayed scaling identities. The figures are numerical drawings of those formulas, not the proofs.

That earlier suite concerns §§1–4. Its projected dual-core scale is still not fixed by octagon s in the historical PDFs. The filled planar hole is excluded only under §2's precise assumptions. The author's subsequent clarification supplies a different intended construction, proved below; it does not alter the earlier sources, tests or artifacts. The whole historical-host and E8 identifications remain unestablished.

## 6. Author-clarified six-segment reference scaffold: exact derivation

### Attribution and explicit alignment assumption

**Author design clarification — Hilmir Frímann Halldórsson, 2026-09-23:** the three regular octagons are geometric reference frames. Three selected octagon edges alternate with three straight gap connectors. The design condition is equal edge and connector lengths, with the intended 60° exterior turns. This is current author testimony, not an equation recovered from a 2025 PDF. The [preserved request](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/author_request.txt) records it in full.

**Codex derivation:** C3 symmetry alone gives three equal selected edges and three equal connectors, but does not force six 120° interior angles. We now specify the alignment that does. All coordinates in this section are a constructive formalization of the clarified design, not a claim to have recovered the unique historical coordinates or a new model adoption.

In the top reference plane put

\[
\phi_i=2\pi i/3,\quad u_i=(\cos\phi_i,\sin\phi_i),\quad
t_i=(-\sin\phi_i,\cos\phi_i),\quad i=0,1,2.
\]

Let s>0 and p>s/(2√3). Select the three edges tangent to the circle of midpoint radius p, with endpoints

\[
A_i=p u_i-\frac{s}{2}t_i,\qquad B_i=p u_i+\frac{s}{2}t_i,
\quad E_i:A_i\to B_i,\quad G_i:B_i\to A_{i+1}.
\tag{S1}
\]

Indices are modulo3. The selected edges lie on the lines uᵢ·x=p. This tangent alignment and its C3-covariant orientations are explicit assumptions; they are not silently inserted into P02's shared-global-orientation equation (2). The chain is exactly E_A,G_AB,E_B,G_BC,E_C,G_CA.

### Lengths, turns, closure and regularity

For R₆₀ the planar rotation through +π/3, direct substitution gives

\[
B_i-A_i=s t_i,\qquad
A_{i+1}-B_i=\left(\sqrt3p-\frac{s}{2}\right)R_{60}t_i.
\tag{S2}
\]

Thus

\[
g=\sqrt3p-s/2>0,\qquad
\frac{g}{s}=\sqrt3\frac{p}{s}-\frac12,\qquad
p=\frac{s+2g}{2\sqrt3}.
\tag{S3}
\]

In chain order the six vertices are

\[
\begin{split}
H_0&=(p,-s/2),&H_1&=(p,s/2),\\
H_2&=((s-g)/(2\sqrt3),(s+g)/2),&H_3&=(-(2s+g)/(2\sqrt3),g/2),\\
H_4&=(-(2s+g)/(2\sqrt3),-g/2),&H_5&=((s-g)/(2\sqrt3),-(s+g)/2).
\end{split}
\tag{S4}
\]

Write dₖ=Hₖ₊₁−Hₖ and ℓₖ=(s,g,s,g,s,g)ₖ. Equation(S2) proves, exactly,

\[
|d_k|=\ell_k,\quad
\frac{(-d_{k-1})\cdot d_k}{\ell_{k-1}\ell_k}=-\frac12,\quad
\det(d_{k-1},d_k)=\frac{\sqrt3}{2}sg>0,\quad
\sum d_k=0.
\tag{S5}
\]

The construction is convex: it is the equilateral support triangle with three disjoint corner triangles cut off, as established below. Therefore the six angles in(S5) are the polygon's interior angles, not merely local angles of a self-intersecting chain. This proves an equiangular hexagon with alternating positive lengths. Equal sides are necessary for regularity and, with these proved angles, sufficient. Consequently

\[
\boxed{\text{regular hexagon}\iff g=s\iff p=p_*:=\sqrt3s/2.}
\tag{S6}
\]

For arbitrary positive s,g the circumradius squared is (s²+sg+g²)/3 and the area is √3(s²+4sg+g²)/4. At g=s the circumradius and side are s, the inradius is √3s/2, and the area is 3√3s²/2. The unmarked polygon has D3 symmetry in general and D6 at g=s. A 60° rotation exchanges the E and G roles: it is **not** a symmetry of the role-marked chain or the complete three-frame construction. Those retain D3 in this realization.

![Alternating edge and connector family](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/figures/01_alternating_scaffold.png)

### The three triangular gaps

Let Vᵢ be the intersection of uᵢ·x=p and uᵢ₊₁·x=p; for example V₀=(p,√3p). Their three supporting lines bound an equilateral triangle of side

\[
W=2\sqrt3p=s+2g.
\tag{S7}
\]

At each corner, the triangle with vertices (Bᵢ,Vᵢ,Aᵢ₊₁) is equilateral with side g: the two legs along the selected-edge extensions both have length √3p−s/2, and the connector is its third side. Since W−2g=s>0, these corner triangles have disjoint interiors and leave a positive segment of length s on each supporting side. Cutting them from the support triangle gives exactly(S4). At g=s the support side is3s, with three side-s corner triangles and the regular central hexagon.

These are well-defined **reference gap cells** and straight connectors. This construction does not assert that the cells are complete components of physical empty space, filled triangular faces, or a material tiling. In the vertical-face realization they lie in the top measurement plane; in the planar-frame realization below they are outside the inward-facing octagon interiors. Nothing requires the connectors to be original octagon sides.

### Complete regular-octagon reference figures

Existence does not rely on using only three abstract line segments. One explicit planar completion uses the regular octagon vertex set O from §4 and centres Cᵢ=L uᵢ:

\[
\mathcal O_i=\{(p+a)u_i+xu_i+yt_i:(x,y)\in\mathcal O\},\qquad L=p+a.
\tag{S8}
\]

The local side x=−a, y∈[−s/2,s/2] is exactly Eᵢ. Each complete reference figure is a regular octagon of side s and apothem a; its orientation rotates covariantly with i. The centre placement giving the regular derived hexagon is

\[
L_*=a+p_*=(1+\sqrt2+\sqrt3)s/2.
\tag{S9}
\]

This is an explicit realization, not a uniqueness claim, recovered historical placement, or identification with P02's literal equation (2). Here p is the selected-edge midpoint radius; L is the **planar octagon centre** radius. They must not be interchanged.

![Complete reference octagons](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/figures/02_complete_octagon_reference_frames.png)

### Precise relationship to Paper C, and the parameter change

Use the already established centred vertical-face representation

\[
F_i(u,z)=p u_i+u t_i+z e_z,\qquad (u,z)\in\mathcal O.
\tag{S10}
\]

Now p is also the radius of the **vertical face centres**, distinct from L in(S8). The top side of each face is z=a, u∈[−s/2,s/2]; its horizontal endpoints are Aᵢ,Bᵢ. Applying the rigid map(D11) at p₀=a/√3 gives the existing Paper-C coordinates(D12). Thus its six-point top measurement polygon is exactly the member

\[
p_0=\frac{a}{\sqrt3}=\frac{(1+\sqrt2)s}{2\sqrt3},\qquad
g_0=\sqrt3p_0-s/2=s/\sqrt2.
\tag{S11}
\]

This establishes the shared **measurement-polygon family**, without identifying every historical geometry with the Paper-C welded surface. To obtain g=s while retaining the size, shape and orientation of each vertical octagon, translate face i outward by Δp uᵢ, where

\[
\Delta p=p_*-p_0=\frac{(2-\sqrt2)s}{2\sqrt3}>0,
\qquad\frac{p_*}{p_0}=\frac{3}{1+\sqrt2}\approx1.242640687.
\tag{S12}
\]

Alternatively, hold the vertical face centres fixed at p₀ and shrink each octagon uniformly about its own centre by λ=(1+√2)/3≈0.804737854. Then s′=λs, a′=λa and √3p₀−s′/2=s′. This shrink rule applies to(S10); shrinking the planar figures about their different centres in(S8) also moves their selected-edge midpoints and must not reuse that rule. A uniform scaling of the **whole arrangement**, including its centre spacings, leaves g/s unchanged and cannot perform the tuning.

### Structural consequences: no silent geometry adoption

For adjacent vertical supporting planes in(S10), their intersection line requires local face coordinates u=+√3p and u=−√3p. A finite regular octagon has |u|≤a. At p₀=a/√3 those are actual full side seams, with z∈[−s/2,s/2]. At p*=√3s/2,

\[
\sqrt3p_*-a=\frac{(2-\sqrt2)s}{2}>0,
\tag{S13}
\]

so the supporting planes still intersect but **the finite faces are pairwise disjoint**. This is not a statement that infinite planes have separated.

The minimum distance between adjacent finite faces is δ=√3p−a for p≥p₀. To see this, write u=a−X on one face and v=−a+Y on the next, with X,Y≥0. Their squared separation is

\[
\delta^2+\delta(X+Y)+(X-Y)^2+XY+(\Delta z)^2\ \ge\ \delta^2.
\tag{S14}
\]

Equality is attained at u=a,v=−a and equal z within the central side intervals. Hence(S13) is also the positive minimum separation at the regular-scaffold placement. The fixed-centre shrink alternative likewise loses the seams because p₀>a′/√3.

| Property | Existing Paper C | Hypothetical translated member at p* |
|---|---|---|
| Octagon shape and size | Regular, side s | The same |
| Top reference ratio | g/s=1/√2 | g/s=1 |
| Shared seams | Three | None |
| Distinct vertices / edges / faces, counting only octagons | 18 / 21 / 3 | 24 / 24 / 3 |
| Surface and boundaries if faces are filled | Annulus; two nine-edge boundary cycles | Three separate disks; three eight-edge cycles |
| Added top connectors | Measurement chords | Reference lines; no material strips or mesh edges introduced |
| Derived top polygon | Equiangular, unequal alternating sides | Regular hexagon; still a derived scaffold |

Within this fixed-orientation family, original welding and g=s cannot both hold with the same regular octagons. This is a scoped consequence, not a prohibition on other scaffolds or later design choices. The current kernel, Paper C, published meshes and geometry implementation retain their existing definitions.

![Paper C placement consequences](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/figures/03_Paper_C_placement_consequences.png)

### Targeted source check, verification and remaining limits

The [targeted follow-up record](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/TARGETED_SCAFFOLD_SOURCE_CHECK.md) records another text screen across all46 PDF paths and visual inspection of116 selected pages. P02 p25 §G.7 explicitly describes a spatial scaffold; P01 p14 §9.2 presents phase-matching rather than mechanical flow. Those support the modeling philosophy, not the specific length law. P02 p3 §1.5's physical-substrate wording remains documented as a different source formulation. No exact alternating E/G prescription, g=s condition or matching shrink/spacing law was located in the inspected historical passages and diagrams. Absence from this bounded search is not proof of absence from all past work.

The new [verify_scaffold.py](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/verify_scaffold.py) records **31/31 exact supporting predicates**, separately from the unchanged earlier42-predicate suite. It checks positive symbolic s,g, all vertices/turns, reference gap cells, complete octagon frames, the Paper-C coordinate identity, placement/shrink rules, finite-face separation and both mesh counts. [Results](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/scaffold_exact_results.json) and [new Codex stdout](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/scaffold_exact_stdout.txt) are attributed as current verification, not original historical runs or a Claude review. The symbolic identities and displayed argument are the proof; the numerical figures illustrate them.

**Disposition:** the author-clarified scaffold is mathematically realized and its regularity condition proved. The filled-planar-hole theorem is valid and inapplicable to that target. No source-supported identification with the separately scaled dual-tetrahedral core, E8 projection, SU(3)/E6 representation, phase lattice or SRG/RSB evolution follows merely from the new regular hexagon. Whether to expose a reference-scaffold option or change any implementation is a **later design decision**; none is made here.
