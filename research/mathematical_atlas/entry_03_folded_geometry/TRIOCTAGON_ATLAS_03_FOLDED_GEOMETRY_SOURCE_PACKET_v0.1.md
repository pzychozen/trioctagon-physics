# TriOctagon mathematical atlas — Entry 03

**Exact folded geometry · Source packet v0.1 · 29 September 2026**

The current geometry is the union of three filled, zero-thickness regular octagonal panels, rigidly placed and welded along three edges. At the canonical fold it is an embedded, connected, orientable annulus: **18 vertices, 21 edges, 3 faces, two boundary components, genus zero**. Its Euclidean symmetry group, allowing panel permutations, is **exactly D3h, of order 12**. The panels supply a fixed geometry; they do not themselves supply a dynamical or physical position law for Ω.

This is a derivation and evidence packet, not a paper rewrite. The current authority is `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`, frozen at `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`. Atlas 01 and Atlas 02 remain closed. No historical correction queue was applied. Paper B is consulted only for its geometry interface and interpretation boundary.

Companion artifacts: [independent exact checks](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_03_EXACT_CHECKS.py) and [machine-readable results](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_03_EXACT_RESULTS.json).

## 1. Authority and evidence map

References in this packet use the following source IDs. Exact file hashes appear in §15 and in the results JSON. Paper section numbers are more stable than line numbers.

| ID | Source and use |
|---|---|
| C_CODE | [geometry.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py): executable geometry contract, general maps, canonical mesh, normals, central section, symmetry generators. |
| C_PAPER | [Paper C v1.0.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md): §§2–4 local construction; §5 welding, closure, topology; §§6–8 sections and metrics; §9 symmetry; §10 historical separation; §11 limits; Appendices A–B dimensions and rims. |
| C_TESTS | [current geometry tests](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_geometry.py): existing regression coverage, inspected, not counted as newly executed tests. |
| C_ORACLE | [geometry oracle](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/parity_oracles/geometry_oracle.py): independently stored coordinate/permutation expectations, inspected as supporting evidence. |
| C_SYMBOLS | [symbols and identities](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/PAPER_C_SYMBOLS_AND_IDENTITIES_v0.2.md): normalization and identity inventory. |
| C_AUDIT | [proof audit v0.2.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/PAPER_C_PROOF_AUDIT_v0.2.2.md): separation of analytic proofs, executed predicates, and preserved historical export validation. |
| C_SPEC | [actual geometry specification](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/reconstruction/TRIOCTAGON_ACTUAL_GEOMETRY_SPEC_v0.2.md): material order and exact welded coordinates. |
| B_CODE | [face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py:28): mesh-derived centres, normals, vertical, tangent frames. |
| B_PAPER | [Paper B v0.1.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md): §§1–3 geometry carrier and free-vector qualification; §11 physical interpretation limits. |
| DYNAMICS | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py): direct-import boundary inspection only. |
| OLD_3D | [old geometry_3d.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_3d.py): history curves and torus display coordinates. |
| OLD_EMBEDDINGS | [old geometry_embeddings.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_embeddings.py): configurable history embeddings. |
| OLD_TETRA | [old dual_tetra_mapper.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/dual_tetra_mapper.py): two tetrahedral display vertex sets and normalized trajectory. |
| OLD_CURVES | [old analysis_tools.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_tools.py:119): separate diagnostic curves and “throat” display. |

The historical lane below is bounded to these documentary comparisons. It makes no claim to have reconstructed an exhaustive chronology or an undocumented map between old displays and the current shell.

## 2. Width-one regular octagon from first principles

Use local Euclidean coordinates `(u,z)`, with the material vertex order counterclockwise in that plane. Put

\[
w=1,\qquad a=w/2=\tfrac12,\qquad
s=\sqrt2-1,\qquad h=s/2,\qquad
d=a-h=1-\tfrac{\sqrt2}{2}=s/\sqrt2.
\]

Here `a` is the half-width/apothem, `s` the side length, `h` the half-length of a vertical flat, and `d` the chamfer cutback. The width is measured between opposite parallel flats, not between opposite vertices.

Construct the octagon as the intersection of eight half-planes

\[
\mathcal O=\{q\in\mathbb R^2:\nu_j\cdot q\le a,\ j=0,\ldots,7\},
\quad \nu_j=(\cos(\pi+j\pi/4),\sin(\pi+j\pi/4)).
\]

Every support line is at distance `a` from the origin; their normals are spaced by π/4. Rotation by π/4 permutes the half-planes and their successive intersections transitively. This proves equal central angles and equal side lengths for a convex eight-sided polygon: regularity follows from the construction, rather than from a numerical coordinate check. The interior angles are π−π/4=3π/4.

The side adjacent to `u=a` has endpoints `z=±h`, where intersection with the diagonal support gives `a+h=a√2`. Thus `h=a(√2−1)` and `s=2h=√2−1`. Equivalently the diagonal supports are `|u|+|z|≤a+h`, alongside `|u|≤a` and `|z|≤a`.

| Local index | Ordered coordinate `(u,z)` |
|---:|---|
| 0 | `(-a,-h)` |
| 1 | `(-h,-a)` |
| 2 | `(h,-a)` |
| 3 | `(a,-h)` |
| 4 | `(a,h)` |
| 5 | `(h,a)` |
| 6 | `(-h,a)` |
| 7 | `(-a,h)` |

The vertical and horizontal edges have length `2h=s`; a chamfer has displacement `(±d,±d)`, hence length `√2 d=s`. All vertices lie at radius

\[
R=\sqrt{a^2+h^2}=\frac1{\sqrt{2+\sqrt2}}
=\frac{(2-\sqrt2)\sqrt{2+\sqrt2}}2.
\]

The four chord classes, joining vertices separated by `m=1,2,3,4` material steps, are `2R sin(mπ/8)`:

| Steps `m` | Exact chord length |
|---:|---|
| 1 | `s` |
| 2 | `sqrt(2−sqrt(2))` |
| 3 | `1` |
| 4 | `sqrt(4−2sqrt(2))=2R` |

Central inversion pairs each vertex and each area element with its negative. Both the vertex centroid and the uniform area centroid are therefore `(0,0)`. The area is the sum of eight triangles of altitude `a` and base `s`:

\[
A_{\mathcal O}=8\frac{as}{2}=4as=2s=2\sqrt2-2.
\]

The local symmetry group is D8 of order 16. Its eight reflection axes are the lines at angles `kπ/8` to the local u-axis (`k=0,…,7`): even `k` passes through opposite side midpoints, odd `k` through opposite vertices. This is the symmetry of **one panel**; it is not the symmetry of the welded assembly. [C_PAPER §2; C_CODE constants]

## 3. Affine panel maps and fold convention

The ambient coordinates `(x,y,z)` are right-handed; `e_z=(0,0,1)`. The middle panel is `M₂(u,z)=(u,0,z)`. The two outer panels start with the reversed local u-direction, `(-u,0,z)`, stacked over the middle panel. This starting configuration is not an unfolded, edge-to-edge strip.

Let `c_L=(-a,0,0)`, `c_R=(a,0,0)` and let `R_z(β)` be the standard positive rotation about z. Then

\[
M_1^\beta=c_L+R_z(\beta)((-u,0,z)-c_L),\qquad
M_3^\beta=c_R+R_z(-\beta)((-u,0,z)-c_R).
\]

Expanding gives exactly `panel_point()`:

\[
\begin{aligned}
M_1^\beta(u,z)&=(-a+(a-u)\cos\beta,(a-u)\sin\beta,z),\\
M_2^\beta(u,z)&=(u,0,z),\\
M_3^\beta(u,z)&=(a-(a+u)\cos\beta,(a+u)\sin\beta,z).
\end{aligned}
\]

Each derivative matrix has orthonormal columns `∂uMᵢ` and `e_z`. Consequently every map is an isometric planar embedding for every real β: local lengths, angles, areas, material order, and z-coordinates are preserved.

The two prescribed hinges are fixed pointwise for all β:

\[
M_1^\beta(a,z)=M_2(-a,z)=(-a,0,z),\qquad
M_3^\beta(-a,z)=M_2(a,z)=(a,0,z),\quad |z|\le h.
\]

The free outer edges have the same z-parameter and identical y-coordinate:

\[
F_1^\beta(z)=(-a+\cos\beta,\sin\beta,z),\quad
F_3^\beta(z)=(a-\cos\beta,\sin\beta,z),
\]

\[
F_3^\beta-F_1^\beta=(1-2\cos\beta,0,0).
\]

Thus the zero x-gap is sufficient for full edge coincidence, not merely a projected closure. On `[0,π]`, strict monotonicity of cosine gives the unique closure `β=π/3`. On all real numbers the closure family is `β=2kπ±π/3`, for integer `k`. This unrestricted statement follows analytically from periodicity and evenness, not from testing several angles.

At the accepted canonical β=π/3,

\[
\begin{aligned}
M_1(u,z)&=(-\tfrac14-\tfrac u2,\tfrac{\sqrt3}4-\tfrac{\sqrt3 u}2,z),\\
M_2(u,z)&=(u,0,z),\\
M_3(u,z)&=(\tfrac14-\tfrac u2,\tfrac{\sqrt3}4+\tfrac{\sqrt3 u}2,z).
\end{aligned}
\]

The third seam is `(0,√3/2,z)`, `|z|≤h`. In the following sections `S=⋃ᵢ Mᵢ(𝒪)` means this canonical surface. [C_PAPER §§3–5, Theorem 2; C_CODE `panel_point`]

## 4. Exact weld, coordinates and incidence

Material images are enumerated by panel 1,2,3 and then local vertex 0,…,7. Two images with exactly equal algebraic coordinates get the same welded index. There is no distance tolerance.

| Welded index | Exact `(x,y,z)` | Material aliases |
| --- | --- | --- |
| 0 | `(0, sqrt(3)/2, 1/2 - sqrt(2)/2)` | P1:v0, P3:v3 |
| 1 | `(-1/2 + sqrt(2)/4, sqrt(6)/4, -1/2)` | P1:v1 |
| 2 | `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` | P1:v2 |
| 3 | `(-1/2, 0, 1/2 - sqrt(2)/2)` | P1:v3, P2:v0 |
| 4 | `(-1/2, 0, -1/2 + sqrt(2)/2)` | P1:v4, P2:v7 |
| 5 | `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` | P1:v5 |
| 6 | `(-1/2 + sqrt(2)/4, sqrt(6)/4, 1/2)` | P1:v6 |
| 7 | `(0, sqrt(3)/2, -1/2 + sqrt(2)/2)` | P1:v7, P3:v4 |
| 8 | `(1/2 - sqrt(2)/2, 0, -1/2)` | P2:v1 |
| 9 | `(-1/2 + sqrt(2)/2, 0, -1/2)` | P2:v2 |
| 10 | `(1/2, 0, 1/2 - sqrt(2)/2)` | P2:v3, P3:v0 |
| 11 | `(1/2, 0, -1/2 + sqrt(2)/2)` | P2:v4, P3:v7 |
| 12 | `(-1/2 + sqrt(2)/2, 0, 1/2)` | P2:v5 |
| 13 | `(1/2 - sqrt(2)/2, 0, 1/2)` | P2:v6 |
| 14 | `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` | P3:v1 |
| 15 | `(1/2 - sqrt(2)/4, sqrt(6)/4, -1/2)` | P3:v2 |
| 16 | `(1/2 - sqrt(2)/4, sqrt(6)/4, 1/2)` | P3:v5 |
| 17 | `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` | P3:v6 |

There are six equivalence classes of size two and twelve of size one. Each of three seams identifies two pairs of endpoints; there are no triple vertex identifications. Therefore `24−6=18` unique vertices. The 24 material labels still exist as labels; they are not 24 distinct spatial points.

The coherent outward face cycles, omitting the repeated closing index, are

```text
P1: (0,1,2,3,4,5,6,7)
P2: (3,8,9,10,11,12,13,4)
P3: (10,14,15,0,7,16,17,11)
```

Every consecutive pair, including last-to-first, is an edge. The complete **undirected** edge list is below. A sorted pair has no implied orientation. All 21 edges have length `s`.

| Edge | Incidence | Class |
| --- | --- | --- |
| `(0, 1)` | 1 | boundary |
| `(0, 7)` | 2 | seam |
| `(0, 15)` | 1 | boundary |
| `(1, 2)` | 1 | boundary |
| `(2, 3)` | 1 | boundary |
| `(3, 4)` | 2 | seam |
| `(3, 8)` | 1 | boundary |
| `(4, 5)` | 1 | boundary |
| `(4, 13)` | 1 | boundary |
| `(5, 6)` | 1 | boundary |
| `(6, 7)` | 1 | boundary |
| `(7, 16)` | 1 | boundary |
| `(8, 9)` | 1 | boundary |
| `(9, 10)` | 1 | boundary |
| `(10, 11)` | 2 | seam |
| `(10, 14)` | 1 | boundary |
| `(11, 12)` | 1 | boundary |
| `(11, 17)` | 1 | boundary |
| `(12, 13)` | 1 | boundary |
| `(14, 15)` | 1 | boundary |
| `(16, 17)` | 1 | boundary |

Name the seams `H₁=(3,4)` between P1/P2, `H₂=(10,11)` between P2/P3, and `H₃=(0,7)` between P1/P3. These are the only edges of incidence two; the other eighteen form the boundary. Starting from 24 material edge incidences, each seam merges one pair: `E=24−3=21`. [C_PAPER §§4–5; C_CODE `folded_module`, `_incidence`]

## 5. Embedded surface and topology

Counts alone do not determine a surface type. Here the manifold and embedding hypotheses can be checked explicitly.

The three panel planes are vertical supporting planes of the equilateral triangular cylinder described in §8. Two distinct planes intersect in exactly one vertical corner-line. On that line each relevant octagon occupies precisely `−h≤z≤h`; this follows from its vertical local flat. Thus pairwise face intersections are exactly their prescribed seams. There is no triple intersection: the three plane equations are `nᵢ·(p−O)=√3/6` and `Σnᵢ=0`, which would sum to `0=√3/2`. There are no additional intersections in the canonical assembly.

Every face interior has a disk neighbourhood. Two half-disks at a seam interior glue to a disk; a boundary edge interior has a half-disk neighbourhood. For a vertex link, connect its previous and next edge-neighbours within each incident face. Twelve single-panel vertices give a one-edge interval. The six seam endpoints `{0,3,4,7,10,11}` give a connected two-edge path with three link vertices. Every vertex link is an interval, with no branching or disconnected pieces. Hence all eighteen vertices are boundary vertices and S is an embedded 2-manifold with boundary. These are polygonal links; triangulating faces preserves their interval type.

S is compact as a finite union of closed bounded polygons. Its panel adjacency graph is the triangle P1–P2–P3–P1, and its edge graph is connected. Each seam is traversed once in each direction by its two incident outward face cycles; these cycles define a coherent orientation.

The boundary graph has degree two at every one of its eighteen vertices and consists of precisely the two loops in §6. Thus `b=2`. Now, and only after these hypotheses,

\[
V=18,\ E=21,\ F=3,\quad \chi=V-E+F=0,
\qquad 0=2-2g-b=2-2g-2,
\]

so `g=0`. The surface is an **annulus**, equivalently a cylinder or a sphere with two open discs removed. It has no cap faces. A closed torus has `b=0,g=1`; a torus with two discs removed has `χ=−2`. Neither describes this mesh. In particular `χ=0` alone is not evidence for a torus. [C_PAPER §5, Theorems 1 and 1b]

## 6. Both exact boundary loops

Trace edges of incidence one; their degree-two adjacency leaves a unique continuation once a direction is chosen. The current API starts each component at its smallest vertex index, then takes its smaller neighbour. This gives

```text
lower: (0,1,2,3,8,9,10,14,15)
upper: (4,5,6,7,16,17,11,12,13)
```

In this canonical indexing both are also the induced boundary orientations of the outward face cycles. The ordered coordinates, including the implicit last-to-first closure, are:

| Position | Lower index / coordinate | Upper index / coordinate |
| --- | --- | --- |
| 1 | 0 / `(0, sqrt(3)/2, 1/2 - sqrt(2)/2)` | 4 / `(-1/2, 0, -1/2 + sqrt(2)/2)` |
| 2 | 1 / `(-1/2 + sqrt(2)/4, sqrt(6)/4, -1/2)` | 5 / `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` |
| 3 | 2 / `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` | 6 / `(-1/2 + sqrt(2)/4, sqrt(6)/4, 1/2)` |
| 4 | 3 / `(-1/2, 0, 1/2 - sqrt(2)/2)` | 7 / `(0, sqrt(3)/2, -1/2 + sqrt(2)/2)` |
| 5 | 8 / `(1/2 - sqrt(2)/2, 0, -1/2)` | 16 / `(1/2 - sqrt(2)/4, sqrt(6)/4, 1/2)` |
| 6 | 9 / `(-1/2 + sqrt(2)/2, 0, -1/2)` | 17 / `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` |
| 7 | 10 / `(1/2, 0, 1/2 - sqrt(2)/2)` | 11 / `(1/2, 0, -1/2 + sqrt(2)/2)` |
| 8 | 14 / `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` | 12 / `(-1/2 + sqrt(2)/2, 0, 1/2)` |
| 9 | 15 / `(1/2 - sqrt(2)/4, sqrt(6)/4, -1/2)` | 13 / `(1/2 - sqrt(2)/2, 0, 1/2)` |

Each rim contains six vertices at `z=±a` and three seam tips at `z=±h`; each has nine edges of length `s`, so `L_lower=L_upper=9s`. Each is a nonplanar curve: three of its high vertices are noncollinear in `z=±a`, and a tip has a different height. The axial projection is the triangle perimeter, with each side partitioned `d,s,d`, since `2d+s=1`; its projected perimeter is 3.

The horizontal reflection `H:(x,y,z)↦(x,y,−z)` exchanges the rims isometrically, so they are congruent. It reverses the induced boundary orientation. For example H sends the lower sequence to `(7,6,5,4,13,12,11,17,16)`, which is the upper cycle in reverse up to a cyclic shift. The proper half-turns `R^k V H` also exchange the rims and preserve their induced orientations. [C_CODE `boundary_loops`; C_PAPER Appendix B and §8]

## 7. Oriented normals, centres and handedness

For the chosen counterclockwise material cycles the oriented normal is `∂uMᵢ × ∂zMᵢ`, not its negative. At general β,

\[
n_1^\beta=(-\sin\beta,\cos\beta,0),\quad
n_2=(0,-1,0),\quad
n_3^\beta=(\sin\beta,\cos\beta,0).
\]

They have unit length. At β=π/3 the geometry data are

| Panel | Area/vertex centre `cᵢ` | Outward unit normal `nᵢ` | Unit tangent `tᵢ=∂uMᵢ=e_z×nᵢ` |
|---|---|---|---|
| P1 | `(-1/4, sqrt(3)/4, 0)` | `(-sqrt(3)/2, 1/2, 0)` | `(-1/2, -sqrt(3)/2, 0)` |
| P2 | `(0,0,0)` | `(0,-1,0)` | `(1,0,0)` |
| P3 | `(1/4, sqrt(3)/4, 0)` | `(sqrt(3)/2, 1/2, 0)` | `(-1/2, sqrt(3)/2, 0)` |

Put `O=(0,√3/6,0)`. Since `cᵢ=O+(√3/6)nᵢ`, these normals point away from the triangular axis. Each `(tᵢ,e_z,nᵢ)` is a positively oriented orthonormal frame. Normalizing the cross product of the first two edge directions in each face cycle gives the same normals, which is how the API computes them.

The three normals are coplanar and satisfy exactly

\[
n_1+n_2+n_3=0,\qquad n_i\cdot n_j=-\tfrac12\ (i\ne j),
\qquad n_1\times n_2=n_2\times n_3=n_3\times n_1
=\tfrac{\sqrt3}{2}e_z.
\]

Thus their span has dimension two. They are not an orthogonal 3D basis. The ordering P1,P2,P3 fixes the positive cyclic cross-product sign; it does not supply three Ω channels by itself.

The outward-normal separation is `arccos(−1/2)=120°`; the interior wedge between adjacent panel half-planes is its supplement, 60°. The fold magnitude 60° is measured from the reversed stacked start. Measured from the co-directional unfolded strip, the hinge rotation magnitude is 120°. These three conventions must be kept distinct even when two numerical values coincide. [C_PAPER §7; C_CODE `face_normal`, `normal_separation`, `interior_dihedral`]

## 8. Central section: curve and enclosed measurement region

The local support inequalities give the full horizontal width of a panel at height z:

\[
w(z)=\begin{cases}
1,& |z|\le h,\\
1+s-2|z|,& h\le |z|\le a,
\end{cases}
\]

with no points for `|z|>a`. Therefore every plane `z=z₀` with `|z₀|≤h` intersects each panel in a whole unit-width segment. Define

\[
A=(-\tfrac12,0,z_0),\quad B=(\tfrac12,0,z_0),\quad
C=(0,\tfrac{\sqrt3}{2},z_0).
\]

P2 contributes AB, P3 contributes BC, and P1 contributes CA. `central_section(z₀)` returns exactly these three endpoint pairs, in that order. The intersection is the closed **curve** `∂T×{z₀}`, where T is the filled equilateral triangle in xy. It has three unit edges, perimeter 3 and **zero planar area**. Its enclosed virtual region T has

\[
\text{altitude}=\tfrac{\sqrt3}{2},\quad
A_T=\tfrac{\sqrt3}{4},\quad r_T=\tfrac{\sqrt3}{6},\quad
R_T=\tfrac{\sqrt3}{3},\quad \text{centroid}=(0,\tfrac{\sqrt3}{6},z_0).
\]

The area follows from base times altitude/2 or shoelace; the inradius is area/semiperimeter; the circumradius is the distance to any corner. The centroid is not on any panel plane, so there is no filled cross-sectional face or cap. The planar symmetry of the section curve and its enclosed triangle is D3. At z₀=0 the full D3h acts on the section, with horizontal reflection acting pointwise; at a nonzero height that reflection exchanges opposite-height sections.

The central band has height `2h=s`. Immediately above or below it the panels narrow, leaving three separated segments instead of the whole triangle perimeter. Thus the full-width triangular-section statement has exactly the closed central-band domain. The API also requires the height to be provably real and provably in that band; it rejects an undecidable symbolic height rather than silently extending the theorem. [C_PAPER §6, Theorem 3; C_CODE `central_section`]

## 9. Exact metric inventory and measurement distinctions

All lengths use the normalized width `w=1`. Uniform rescaling by a positive width multiplies lengths by w and areas by w²; the width supplies no physical length unit.

| Quantity | Exact value | Meaning |
|---|---|---|
| Local face width and height | `1, 1` | Opposite-flat distances in the panel |
| Apothem / circumradius | `1/2`, `1/sqrt(2+sqrt(2))` | Local centre-to-flat / centre-to-vertex |
| Chamfer cutback | `d=s/sqrt(2)` | Both local horizontal and vertical step |
| One face area | `2s` | Intrinsic material area |
| Total material area | `6s` | Sum over three panels; also canonical union area because intersections are edges |
| One seam / all seams | `s`, `3s` | Physical mesh edge lengths in this geometric model |
| One rim / total boundary | `9s`, `18s` | Intrinsic curve lengths, equal to sums of ambient straight-edge lengths |
| Sum of unique edge lengths | `21s` | Each welded seam counted once |
| Sum of face perimeters | `24s=18s+2(3s)` | Each seam counted twice |
| Pairwise panel-centre Euclidean distance | `1/2` | Ambient chord between centres |
| Pairwise panel-centre intrinsic surface distance | `1` | Atlas-derived consequence; proof below |
| Centre-to-axis distance | `sqrt(3)/6` | Ambient radial offset of each face centre |
| Seam-to-axis distance | `sqrt(3)/3` | Ambient radial offset of each vertical seam |
| Central-band height / tip levels | `s`, `z=±h` | Canonical triangular section band |
| High/low rim flat levels | `z=±1/2` | Their tip-to-flat vertical difference is d |
| Ambient x, y, z bounds | `[-1/2,1/2]`, `[0,sqrt(3)/2]`, `[-1/2,1/2]` | Box dimensions `1 × sqrt(3)/2 × 1` |
| Fold from reversed start | `60°` | Rotation magnitude β |
| Interior dihedral / outward-normal angle | `60° / 120°` | Complementary wedge/normal conventions |
| Chamfer edge / panel plane to horizontal | `45° / 90°` | Twelve sloping boundary edges; every panel plane is vertical |

The uniform-area centroid of S is O because the three congruent panel areas have centres cᵢ whose average is O. The welded vertex centroid is also O. This is an area/vertex centre, not a centroid of an enclosed volume: the shell is open.

For the extra intrinsic distance statement, parametrize the triangle perimeter by arclength `ℓ mod 3`. The surface is a subset of that perimeter times z, with metric `dℓ²+dz²` within panels and by unfolding across seams. The three panel centres lie at successive edge midpoints, one unit apart in shortest circular arclength. Any surface curve between two centres has length at least that one-unit change. The z=0 perimeter path through the shared seam achieves length `1/2+1/2=1`. The ambient chord `1/2` cuts through the empty interior and is not a surface path.

For every chamfer edge, rigid folding preserves its vertical step d and horizontal run d, so its inclination is exactly 45°. This does not imply a 45° panel plane. [C_PAPER §§2,6–8, Appendix A; centre/bounds quantities also derived directly from §4 coordinates]

### 9.1 Spatial notches and projected notches

At the upper far-seam tip `A=V₇`, the actual boundary neighbours are `B=V₆` and `C=V₁₆`. Their edge vectors are

\[
e_1=B-A=d(-\tfrac12,-\tfrac{\sqrt3}{2},1),\qquad
e_2=C-A=d(\tfrac12,-\tfrac{\sqrt3}{2},1).
\]

The two boundary legs have length s and the virtual connector BC has length d. Since `e₁·e₂=3s²/4`, the spatial tip angle is `arccos(3/4)≈41.4096221093°`; direct base-angle evaluation gives `arccos(√2/4)≈69.2951889454°`. The other five tips are congruent by the canonical symmetries and are independently checked from their own neighbours.

Dropping z gives an equilateral projected triangle with all sides d and all angles 60°. The cross product is

\[
e_1\times e_2=d^2(0,1,\tfrac{\sqrt3}{2}).
\]

Consequently the **virtual** spatial notch triangle and its projection have areas

\[
A_{\mathrm{notch}}=\tfrac{\sqrt7}{8}s^2,\qquad
A_{\mathrm{notch,proj}}=\tfrac{\sqrt3}{8}s^2.
\]

The notch plane has inclination `arctan(2/√3)≈49.1066053509°` to horizontal. The notch plane, panel plane and chamfer edge are different objects. Only the two notch legs are mesh edges; the base and filled triangle are measurement constructs. [C_PAPER §8, Theorem 5]

### 9.2 Virtual rim hexagon

The six high vertices `(5,6,16,17,12,13)` form a planar equiangular hexagon at `z=1/2` when joined by virtual connectors across the notches. Its edge lengths alternate `s,d,s,d,s,d` and all six interior angles are 120°. It is not regular because `s≠d`. Its area is

\[
A_{\mathrm{hex}}=\tfrac{\sqrt3}{4}(1-3d^2)
=-\tfrac{7\sqrt3}{8}+\tfrac{3\sqrt6}{4}.
\]

Projection partitions the filled triangle into this hexagon and three equilateral corner notches, with disjoint interiors because `0<d<1/2`:

\[
A_{\mathrm{hex}}+3A_{\mathrm{notch,proj}}=\tfrac{\sqrt3}{4}.
\]

The nonplanar nine-edge rim, the planar six-vertex measurement hexagon, and the enclosed projected triangle are therefore three distinct objects. None supplies a cap face. The corresponding lower measurements follow by H. Paper D's alternative measurement constructions are outside this entry; no shrink or seam change is performed. [C_PAPER §8]

## 10. Symmetry generators, complete actions and exact group

Write `y_c=√3/6`. The three public transformations are

\[
\begin{aligned}
R(x,y,z)&=(-\tfrac x2-\tfrac{\sqrt3}{2}(y-y_c),\quad
y_c+\tfrac{\sqrt3}{2}x-\tfrac12(y-y_c),\quad z),\\
V(x,y,z)&=(-x,y,z),\\
H(x,y,z)&=(x,y,-z).
\end{aligned}
\]

They are, respectively, `rotate_c3()`, `reflect_vertical()` and `reflect_horizontal()`. R rotates 120° about the vertical line through O. V reflects through x=0, and H through z=0.

The following tuples give the image of vertices `0,1,…,17` in order:

```text
R: (3, 8, 9, 10, 11, 12, 13, 4, 14, 15, 0, 7, 16, 17, 1, 2, 5, 6)
V: (0, 15, 14, 10, 11, 17, 16, 7, 9, 8, 3, 4, 13, 12, 2, 1, 6, 5)
H: (7, 6, 5, 4, 3, 2, 1, 0, 13, 12, 11, 10, 9, 8, 17, 16, 15, 14)
```

| Generator | Face action | Seam action | Rim action | Ambient determinant / induced surface orientation |
|---|---|---|---|---|
| R | `P1→P2→P3→P1` | `H1→H2→H3→H1` | Each rim to itself | `+1`, preserved |
| V | `P1↔P3`, P2 fixed | `H1↔H2`, H3 fixed | Each rim to itself | `−1`, reversed |
| H | Every face fixed as a set | Every seam fixed, endpoints exchanged | Upper/lower exchanged | `−1`, reversed |

R and V preserve the sign of z and therefore do not exchange seam endpoints between the upper and lower rims. V reverses each fixed rim's induced cycle direction; H reverses direction while exchanging rims. Each generator sends whole face cycles to face cycles, up to cyclic shift and possibly reversal. Because every face is the convex hull of its cycle, these are symmetries of filled faces, not only of a vertex cloud.

The relations are

\[
R^3=V^2=H^2=I,\quad VRV=R^{-1},\quad HR=RH,\quad HV=VH.
\]

The twelve distinct maps are `R^k V^a H^b`, `k∈{0,1,2}`, `a,b∈{0,1}`; compositions act rightmost first. Their determinant is `(-1)^(a+b)`. The JSON gives every element's vertex, face, seam, rim and orientation action.

| Elements | Count | Orientation | Rim exchange |
|---|---:|---|---|
| `I,R,R²` | 3 | Preserving | No |
| `R^k V H` | 3 | Preserving, half-turns about horizontal axes | Yes |
| `R^k V` | 3 | Reversing, vertical reflections | No |
| `H,RH,R²H` | 3 | Reversing, horizontal reflection / rotoreflections | Yes |

For an orthogonal spatial map A, outward normal directions transform as polar geometric vectors `n↦An`. The cross product of pushed-forward tangent vectors transforms as `det(A)An`. Thus the induced surface orientation relative to the outward convention is preserved precisely by the six determinant-+1 elements. This accounts for both face-cycle and induced boundary-cycle signs.

**Upper bound, excluding larger groups.** In the topological interior of S, the points with no planar neighbourhood are exactly the three seam interiors. Any Euclidean symmetry must permute their closures: three equal parallel vertical segments. It fixes their midpoint centroid O and preserves their common unoriented vertical direction. In centred coordinates it has block form `(r,z)↦(Br,εz)`, where `B∈O(2)` and `ε=±1`. The seam-midpoint footprints are an equilateral triangle, so B has only six possibilities. Hence there are at most `6×2=12` Euclidean symmetries. The twelve exhibited maps realize the bound:

\[
\operatorname{Sym}(S)=D_3\times C_s\cong D_{3h},\qquad |\operatorname{Sym}(S)|=12.
\]

This is the symmetry of the unlabelled surface; it permits panel permutations. A demand to fix material labels would define a smaller group. The vertex set happens to have the same group, with a separate proof: its covariance about O is `diag((1+s²)/12,(1+s²)/12,(2+s²)/12)`. The distinct vertical eigenvalue fixes the vertical axis, and the seam tips again give the six planar possibilities. Neither the local D8 symmetry nor a historical D24 label enlarges the canonical surface group. Exact 30° and 45° whole-shell rotations fail the vertex-preservation test. [C_PAPER §9, Theorem 6; C_CODE symmetry functions]

## 11. Precisely what survives at general real β

| Property | Arbitrary real β | Canonical β=π/3 |
|---|---|---|
| Three affine panel maps | Defined | Defined |
| Each panel's intrinsic metric, regularity, area and height | Preserved | Preserved |
| Two prescribed hinges | Coincident pointwise | Coincident pointwise |
| Third free-edge seam | Only when `cosβ=1/2` | Closed |
| Sum of panel material areas | `6s`, with material multiplicity | `6s`, also union area |
| V and H as symmetries of the union of images | Yes | Yes, within D3h |
| Exactly 18 welded vertices, 21 edges, annulus | No general assertion | Proved |
| Equilateral full-width central section | No general assertion | Proved on `abs(z)≤h` |
| Three normals sum to zero | Only when `cosβ=1/2` | Yes |
| Embedded assembly without panel overlap | Not guaranteed | Proved |
| Full D3h and its canonical orientation convention | Not generally inherited | Proved |

The general normal relations are `n₁·n₂=n₂·n₃=−cosβ`, `n₁·n₃=cos(2β)` and `Σnᵢ=(0,2cosβ−1,0)`. They are material-oriented normals; “outward” requires the appropriate closed geometry and winding convention.

Three exact examples delimit the claims:

1. At `β=π/2` the free-edge gap is `(1,0,0)`. The actual pairwise weld gives 20 vertices, 22 edges, three faces, two seams and one boundary loop. This single example refutes universal inheritance of the canonical counts and two-rim annulus. It is not a classification of every nonclosing angle.
2. At `β=0` all three images coincide in one planar octagon, with eight unique spatial vertices. Their summed material area remains `6s`, but their union area is `2s`. Therefore even an overlap-free family cannot be asserted.
3. At `β=−π/3` the third seam closes in the y-reflected configuration. With the original material cycles, `nᵢ·(cᵢ−O_ref)=−√3/6`, so those oriented normals are inward. Outward cycles would have to be reversed for that branch. No source cycle is edited here.

`panel_point()` supports the algebraic β family. `folded_module()` has no β argument and always builds the accepted canonical shell. This entry makes no claim about a collision-free physical folding motion. [C_PAPER Theorem 2 and limits; C_CODE docstrings]

## 12. Paper B interface boundary and Ω

The exact data imported from geometry are the ordered centres cᵢ, normals nᵢ, common `e_z`, and the tangent construction `tᵢ=e_z×nᵢ`. B_CODE obtains these from `folded_module()`, averaging each eight-vertex cycle for its centre and calling `face_normal()` for its normal. Its panel labels are `A=P1`, `B=P2`, `C=P3`. These are precisely the frames in §7.

Paper B explicitly chooses an optional mathematical representation using these three oriented tangent planes. Acknowledging that accepted map does not make the bare Paper C geometry a dynamical state. The vectors in Paper B are free vectors on the selected planes, not a field defined at every point of the bounded octagonal faces. Their magnitude need not keep an endpoint inside a panel. Its §11 supplies no physical length unit, physical field law, seam continuity law or rim boundary conditions.

The geometry's vertices and centres are fixed by width and fold, independently of Ω. The reviewed geometry API takes no Ω argument, and geometry.py and dynamics.py have no direct imports of each other. These static observations are narrowly stated; they are not a proof that no other repository module can combine the two. Paper B is already an explicit example of an optional mathematical interface.

```text
PAPER_C_GEOMETRY != OMEGA_DYNAMICS
NO_PHYSICAL_POINT_ATTACHMENT_FROM_OMEGA
```

The second flag means no accepted physical position law is supplied by this geometry contract. It does not deny Paper B's mathematical free-vector representation. No encode/decode/transport formula or derivation is included in this entry. [B_CODE lines 28–36, `face_frames`; B_PAPER §§2–3 and §11]

## 13. Bounded historical comparison lane

| Documentary item | Observed object / comparison | Classification | Relation to the current shell |
|---|---|---|---|
| C_CODE and C_PAPER | Three exact regular panel images, three welds, two rims, 18 vertices | EXACT_CURRENT_MATH | Defines and proves the present object. |
| OLD_TETRA `_base_tetra_vertices`, `dual_tetra_vertices` | Four vertices `(1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1)` and their negatives, scaled | HISTORICAL_PRECURSOR | Earlier recoverable geometric display. Its eight vertices and tetrahedral construction do not give the three octagonal faces or their incidence. “Precursor” here is contextual, not a proved derivation chain. |
| OLD_3D / OLD_EMBEDDINGS torus coordinates | A history-dependent trajectory with `φ=2π·phi_index/12`, varying minor radius and cross-sectional angle, mapped by toroidal coordinate formulas | HISTORICAL_PRECURSOR | Demonstrates a torus-like display mechanism. A curve drawn with toroidal coordinates is not evidence that the current welded surface is a torus. |
| OLD_3D `history_Zvec_to_xyz`, OLD_CURVES `plot_Z_components_trajectory_3d` | Stored `Z_macro`, `Z_chiral`, `Z_total` diagnostics rendered as spatial curves | HISTORICAL_PRECURSOR | A trajectory visualization family, with no octagon-face incidence or weld law in these functions. These are three named diagnostics, not automatically three material panels or three Ω channels. |
| The number “three” in those diagnostic curves and current panel count | Equal small integer count, without a documented geometric map | COINCIDENCE | This observation alone supports no identification of curves with panels. |
| OLD_TETRA `map_history_to_dual_tetra`; OLD_CURVES `plot_dual_tetra_trajectory` | `(c_x,c_y,c_u)` trajectory, normalized by its maximum radius and multiplied by `throat_radius`; plotting label “Dual-tetra throat” | STRUCTURAL_ANALOGY | A surrounding/display-region motif can resemble a passage, but `throat_radius` is a plotting scale. It supplies no manifold or genus computation for S. |
| Old concentric three-octagon Z24/D24 diagrams, as explicitly distinguished in C_PAPER §10 | Nested planar arrangements and angular labels | HISTORICAL_PRECURSOR | Documentary separation exists in the accepted current paper. It does not provide an isometry, weld quotient or symmetry-preserving map into S. No exhaustive re-audit of the old drawings is claimed here. |
| Proposed identification of any old torus, dual tetrahedral “throat” or concentric diagram with the canonical shell | A required explicit map preserving the relevant geometric structure is absent from the consulted lane | OPEN | No undocumented transformation is supplied or inferred. |

The historical sources are read as evidence of the objects they actually construct. Their terminology does not override the current coordinates, incidence, boundary count, or group proof. No harmonic-three lineage, old arithmetic correction, or cycle-covering argument is reopened.

## 14. Independent checks, falsifiers and reproducibility

The companion script starts with eight equal-distance support lines, solves their intersections, rotates reversed panel placements about hinge feet, and welds exact algebraic coordinates. Its reference construction does not import kernel code or the existing geometry oracle. Printed coordinates and face cycles are checked as a separate specification comparison. A separate API_PARITY block executes only geometry.py through `runpy`, with Python bytecode writing disabled, and compares that API with the independent reconstruction.

**Executed result: 84/84 predicates PASS, 0 FAIL.**

| Group | Passed / total |
| --- | --- |
| API_PARITY | 7 / 7 |
| EXACT_MATH | 59 / 59 |
| FALSIFIER | 8 / 8 |
| INTEGRITY | 6 / 6 |
| INTERFACE_GEOMETRY | 1 / 1 |
| SOURCE_BOUNDARY | 3 / 3 |

Recorded run: `2026-09-29T06:20:48.371307+00:00`; Python `3.11.15`, SymPy `1.14.0`, interpreter `C:\Users\Notandi\miniconda3\envs\torment\python.exe`.

These totals are predicates grouped by purpose, not a claim of that many independent mathematical theorems. No existing test-suite run or earlier paper audit count is included. Source-boundary and integrity checks are not labelled geometric proofs. The new script does not alter scientific or production source.

Meaningful negative checks verify that the shell is not a closed torus; the welded points are not 24 distinct vertices; the normals are not an orthogonal spatial basis; the rims are nonplanar; the virtual hexagon is not regular; 30°/45° whole-shell rotations fail; π/2 does not close; β=0 overlaps; the reflected closing branch reverses the material outward convention; and an interior section centroid is absent from the shell. Several related falsifications share one predicate. API checks also reject outside-band, nonreal and undecidable section heights.

Finite computations establish the exact listed identities and combinatorial predicates. The full real-angle closure family, quantified all-height section result, manifold classification and complete symmetry upper bound rely on the analytic arguments above. Group enumeration alone is a lower bound; Euler arithmetic alone is not a classification theorem. Absence of a physical Ω law is an interpretation of the reviewed contract and its explicit limits, not a numerical falsifier of all imaginable physical theories.

Run with the user's conda environment:

```powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_03_EXACT_CHECKS.py `
  --output C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_03_EXACT_RESULTS.json
```

This reproduces mathematics and source/API checks without an integrity attestation. To attach the captured before/after inventory comparison, add:

```powershell
  --integrity-dir C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas03_20260929_528qdnad
```

The delivered run used the `torment` interpreter directly, with `-B`, so it did not depend on interactive shell activation. The JSON records interpreter, Python/SymPy versions, script hash, source hashes, all check outcomes, full mesh lists and every group action. Re-running later checks the then-present sources; matching the frozen baseline and captured inventory remains a separate requirement. Retain the external inventory files if the optional integrity comparison must be reproduced.

## 15. Integrity and deliverable closeout

Outputs are under `C:/Users/Notandi/.codex/reports`, outside every protected tree. Full before/after file-content fingerprints cover the current repository, old kernel and the **entire production checkout**, with the copied production kernel also reported as a nested scope.

For each scope, the inventory maps every relative POSIX-form file path to the SHA-256 of its bytes. It includes ignored and untracked files, excludes `.git` administrative contents, and hashes the canonical JSON map using sorted keys and compact separators. This fingerprints file names and content, not access times, modification times, ACLs or empty directories. Symlink/reparse metadata are not separately certified. The snapshots are read sequentially, not as an atomic filesystem snapshot; their start/end times are retained in the results. Equal maps show no net content/path changes over the captured intervals.

| Scope | Before / after file count | Before SHA-256 | After SHA-256 | Changed paths |
| --- | --- | --- | --- | --- |
| current | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | 0 |
| old | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | 0 |
| torment_kernel | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | 0 |
| torment_checkout | 173908 / 173908 | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | 0 |

Inventory intervals (UTC):

| Scope | Before interval | After interval |
| --- | --- | --- |
| current | 2026-09-29T05:53:30.368064+00:00 to 2026-09-29T05:53:36.064279+00:00 | 2026-09-29T06:17:52.836271+00:00 to 2026-09-29T06:17:57.238945+00:00 |
| old | 2026-09-29T05:53:36.068292+00:00 to 2026-09-29T05:53:36.444510+00:00 | 2026-09-29T06:17:57.245105+00:00 to 2026-09-29T06:17:57.532025+00:00 |
| torment_kernel | 2026-09-29T05:53:36.448024+00:00 to 2026-09-29T05:53:36.479804+00:00 | 2026-09-29T06:17:57.535897+00:00 to 2026-09-29T06:17:57.561966+00:00 |
| torment_checkout | 2026-09-29T05:53:36.484318+00:00 to 2026-09-29T05:55:39.859475+00:00 | 2026-09-29T06:17:57.566051+00:00 to 2026-09-29T06:20:01.556138+00:00 |

The current HEAD is the frozen baseline above. Production HEAD is `a06edcc5c9df5d3b56405085d9f2942b768dc203`. Both had clean tracked status before and after, checked with Git optional locks disabled. The tracked-status command deliberately did not classify untracked files; those files were covered by the full content inventories. No Git mutation command was issued.

Consulted-source SHA-256 register:

| ID | SHA-256 |
| --- | --- |
| C_CODE | `18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf` |
| C_PAPER | `5a0cbdae4aaf689cfe1f5b29305960e90c88e26d0db28834802ef70fc16549fb` |
| C_TESTS | `7f85feaa93466c79858904131400e1903142f606ffb8976c9f32c77355964f6c` |
| C_ORACLE | `bcd004a2b98a650c419212103353a550206288f18b8795f4fdba18ea29c736bd` |
| C_SYMBOLS | `2c22fd11af1114115c5e795b40bc0730d9049646a57a615bad5d75bddca86290` |
| C_AUDIT | `89c454ae67aebf3a3b415c51655e5476299882b43c9d76fe6726ada16588018a` |
| C_SPEC | `4578873c8a56b318487b7dc237444d3d8ecdd2c5d0f2d0c74b9a4906f987fe4b` |
| B_CODE | `be9d1e25a6f368e644ecfa9b1af70ba9382599e8b4d43d529d1783004d86ded7` |
| B_PAPER | `fb4575120470e8d7143ebc1f475ee4635caf9f39f21f88308960308fb259e150` |
| DYNAMICS | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |
| OLD_3D | `b6803b3a02f5240a5cb00a3dbc9cf403c2e762de713146aa3848996738772400` |
| OLD_EMBEDDINGS | `5e5a12d0b352fe353aea84d47b598c4288d9d679ee8d83003c25e210a0ec4c4e` |
| OLD_TETRA | `14845223bbfa0c0f17df2781ee4a0ebba9befeee5f374bb01a4647242dbedf9f` |
| OLD_CURVES | `3be6de46c7060b6e797bc6801de002c5b59374957a3ef1a9fd37d51b11b20106` |

Delivered checks-script SHA-256: `76929a2a0c58ae81eab3319d316be5876f4fb0e3bf771ccdbbceb752a762f275`.

Delivered results-JSON SHA-256: `6694ecf54262d847b5a1958311c7634adacaff687270e40bc9239016875ec241`. The packet omits a self-hash to avoid a circular dependency. Snapshot paths and their hashes are recorded in the JSON.

```text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
PAPER_C_GEOMETRY != OMEGA_DYNAMICS
NO_PHYSICAL_POINT_ATTACHMENT_FROM_OMEGA
```

The change flags refer to the captured full file-content/path comparison and source checks; commit and push counts refer to actions performed for this work order. No source document, historical correction, production module, or repository placement was changed. Atlas 03 ends with this external source packet and its reproducible evidence.
