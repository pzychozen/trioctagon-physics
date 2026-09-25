# RESEARCH NOTE — 3↑/3↓ TWISTED HEX CRYSTAL (reconstruction from `tri_oct.py` + the originating Claude chat)

Status header

```
CRYSTAL_SOURCE_RECONSTRUCTED     = YES
SYMBOLIC_COORDINATES_RECOVERED   = YES   (exact, unique, single length scale s = sin(pi/8))
TOPOLOGY_CLASSIFIED              = YES   (non-manifold, self-intersecting, open 2-complex — NOT a polyhedron)
FULL_SYMMETRY_CLASSIFIED         = YES   (depends on two rendering choices; see §7)
HANDED_PAIR_PROVED               = YES   (geometric/combinatorial handedness; +1 and -1 twist are enantiomorphs)

HOST_GEOMETRY_SOURCE_AVAILABLE   = NO    (Paper C / accepted Tri-Octagon not present in this chat; RTM host excluded per order)
UPPER_THREE_POINT_REGISTRATION   = NOT_TESTED
LOWER_ALIGNMENT                  = NOT_TESTED
DEFORMATION_REQUIRED_FOR_FIT     = UNKNOWN

PHYSICAL_INTERPRETATION          = NOT_ESTABLISHED
```

Label convention used throughout:
`[AUTHOR]` = AUTHOR_STATED_INTENT (Hilmir, verbatim or near-verbatim from this chat) ·
`[CLAUDE-HIST]` = CLAUDE_HISTORICAL_INTERPRETATION (what Claude did in the chat, accepted or not) ·
`[CODE]` = SOURCE_CODE_FACT · `[DERIV]` = NEW_DERIVATION (proved here) · `[HYP]` = NEW_HYPOTHESIS.

---

## 1. Historical intent recovered from this chat (Task A)

The object was built in this conversation on 2026-03-14 (chat timestamps) in a step-by-step sequence that Hilmir dictated after several failed free-form attempts. The sequence, with who said what:

| Step | What was said / done | Label |
|---|---|---|
| Host | "trioctagon is just a name for the three octagons that are already present" — 3 octagons, V (flat), G and H hinged on V's two parallel edges, folded 60°. Built from `tri.py` (radius 1, fold 60°). Claude re-oriented the octagon so the hinges V0–V1 / V4–V5 are parallel to Y (author: "the object is badly placed if you want to work with it symmetrically forward"). | [AUTHOR] + [CLAUDE-HIST] |
| Helper lines | "create a line with center point between v4-v1 and then another line with a center point between v5-v0. Do not connect v4-v1 to v5-v0." → two chords of V at y = ±sin(π/8), midpoints at x = 0. | [AUTHOR] |
| Gap triangle | "triangle gap that forms at vertices h3-h4-g3-h3, can we create a plane from those vertices? Then move that plane and have side h3-g3 (small triangle) snap to center of v0-v5, without changing its degree?" → the exact gap triangle H3–H4(=G4)–G3, **pure translation**, edge H3–G3 centred on mid(V5,V0). Hilmir confirmed: "yes this exactly what I was trying to explain before." | [AUTHOR] |
| Why that triangle | Earlier (before the step-by-step): "it should remain exact size from the gap it forms from"; "its already roughly 45° because you are working with symmetric octagon structure"; "The small triangles should not shrink, they should keep their form." No numerical reason given — the triangle *is* the gap. | [AUTHOR] |
| Second triangle | "mirror it on v1-v4 center, I think that is °180 Y axis horizontal flip." Claude first reflected across the line y=+sin(π/8) (result outside the octagon), then self-corrected to y → −y (reflection through the octagon's centre line), which Hilmir accepted by moving on. | [AUTHOR] wording; [CLAUDE-HIST] realisation |
| Octagons removed | "we only needed them to construct the exact form of the small triangle and their location and what degree they bend with." Also: "Their x center is at 0. the snap grid is 1 and -1 on the top of the small triangle." | [AUTHOR] |
| Three copies at 120° | "now we copy them just like we did with octagons before. in °120 . x horizontal, y vertical. Just see what happens, choose the edge of the triangle as a boundary of that spin, you already have it marked with a red dot. so it becomes 2×3 = 6 triangles." The "red dot" was the **apex**. | [AUTHOR] |
| Spin axis actually used | Claude rotated about the global Y axis through the origin, stating "The apex is at X=0, so rotating around Y axis through the apex is the same as rotating around the Y axis through the origin." That statement is **false** (the apex has z = h ≠ 0). Hilmir looked at the result and said "yes this is what we want." | [CLAUDE-HIST] — accepted visually, not derived |
| "spin geometry" | The word "spin" is used only as the name of this rotational-copy operation ("boundary of that spin"). No physical meaning was stated. | [AUTHOR] |
| Hexagons | "the center hexagonal formations is the correct step, connecting the edges of the smaller pyramids into a hexagon." | [AUTHOR] |
| Cap faces | "the hexagon doesn't move at all, it connects the vertices to the triangle forming a new plane." Claude implemented: for every hexagon edge, a triangle to the *nearest* apex. Hilmir moved on to the next step (implicit acceptance). | [AUTHOR] intent; [CLAUDE-HIST] rule |
| Twist | "connect the hexagon to the other hexagon, creating a face that is twisted, so instead of connecting mirrored vertice, we connect to the next vertice to the left." | [AUTHOR] |
| Reaction | "this is not what I imagined at first and its ok … accidentally beautiful symmetry that I didn't plan on." He then showed a drawing of a hexagonal antiprism ("maybe it was supposed to be more like this. But I have nothing to base it off of") and said "Don't change anything." | [AUTHOR] |
| "Two hexagons" | Zoomed side (XZ) view: "it creates another tiny hexagon, so currently there are two hexagons." | [AUTHOR] observation — explained in §5 as a projection artefact |

Explicit answers to the Task A questions:

- Why upper/lower triangles: they are the exact gap triangle of the folded tri-octagon, placed on V's two helper chords. Reason = "that is what the gap is". **No numeric reason.** [AUTHOR]
- Why three copies / why 120°: "just like we did with octagons before" (a 120° clone test of the tri-octagon made earlier, which Hilmir had then rejected). Intuitive; no stated reason. [AUTHOR] "I usually just go with my intuition."
- Why the one-step twist: "instead of connecting mirrored vertice, we connect to the next vertice to the left." The *result* was explicitly a surprise. [AUTHOR]
- "Spin geometry": only the copying operation. **No physics stated.**
- Left/right handedness: **never mentioned** by the author. "Left" fixed the direction only relative to an unspecified viewing orientation; the code's +1 (in atan2(z,x) order) is Claude's realisation. [CLAUDE-HIST]
- Dimensions tied to octagon geometry: **never stated numerically**. Everything descends from radius = 1 and fold = 60° through the construction. The one numeric remark, "snap grid is 1 and −1 on the top of the small triangle", does **not** match the code (apex height is cos(π/8) = 0.924, not 1). Open question §11-Q1.

Discrepancies between author words and accepted code (must not be silently reconciled):

1. **Spin axis.** Author: pivot on the apex (red dot). Code: global Y axis. The author accepted the code's picture. → §11-Q2.
2. **Twist edges.** Author: connect top[i] to bottom[i+1] *instead of* top[i]–bottom[i]. Code: the twisted quads contain **both** the +1 diagonals *and* the vertical (mirrored) struts t_{i+1}–b_{i+1} as triangle edges, plus +2 diagonals. See §2/§4. → §11-Q3.
3. **Cap faces.** Author: "connect the vertices to the triangle forming a new plane". Code: nearest-apex rule with exact ties on 3 of 6 edges per ring, broken by floating point → the rendered caps are not C3-symmetric (§7). → §11-Q4.
4. **Second triangle.** Author said "mirror on v1-v4 center"; realised as reflection through the octagon centre line. Accepted.

---

## 2. Source-code construction (`tri_oct.py`, final version in this chat) [CODE]

Literal coordinates:

```
tri_bottom = [( +0.27059805, -0.38268343, 0 ), ( 0, -0.92387953, 0.46868957 ), ( -0.27059805, -0.38268343, 0 )]
tri_top    = [( +0.27059805, +0.38268343, 0 ), ( 0, +0.92387953, 0.46868957 ), ( -0.27059805, +0.38268343, 0 )]
```
Vertex 1 of each is the apex (the "red dot"). tri_top is tri_bottom with y → −y (same sign of z).

1. `rotate_y(P, θ)` for θ ∈ {0°, 120°, 240°} with R = [[c,0,s],[0,1,0],[−s,0,c]] (this maps azimuth φ = atan2(z,x) to φ − θ).
2. Base vertices (index 0 and 2 of every triangle) with y > 0 → `top_bases`, else `bot_bases`; apexes → `top_apexes`/`bot_apexes`. Order of apexes in the arrays: azimuths [90°, 330°, 210°].
3. Rings: `sort_ring` sorts by atan2(z,x) → ring order azimuths [240, 300, 0, 60, 120, 180] (ascending atan2 in (−π, π]).
4. Cap faces: for each ring edge (i, i+1) take the apex minimising distance to the edge midpoint → 6 top + 6 bottom triangles.
5. Twisted sides: for i in 0..5, with t1=top[i], t2=top[i+1], b1=bot[i+1], b2=bot[i+2]: faces (t1,t2,b1) and (t1,b1,b2) → 12 triangles.
6. Rings are drawn as polylines, not faces.

Where it came from (host frame, radius-1 octagon, hinges ∥ Y): gap triangle H3 = (0.2706, 0.9239, 1.1315), H4 = G4 = (0, 0.3827, 1.6002), G3 = (−0.2706, 0.9239, 1.1315); translation (0, −1.3066, −1.1315) puts H3–G3's midpoint on mid(V5,V0) = (0, −0.3827, 0) and H4 at (0, −0.9239, 0.4687).

---

## 3. Canonical symbolic coordinate model (Task C) [DERIV]

Let s = sin(π/8) = ½√(2−√2), c = cos(π/8) = ½√(2+√2). Then, **exactly**:

| literal | exact form | value | abs. error vs literal |
|---|---|---|---|
| 0.38268343 (ring half-height, "b") | s | 0.3826834324 | 2.4e-9 |
| 0.92387953 (apex half-height) | c = (1+√2)·s | 0.9238795325 | 2.5e-9 |
| 0.27059805 (ring circumradius, "a") | s/√2 = (c−s)/2 | 0.2705980501 | 7.3e-11 |
| 0.46868957 (apex radial offset, "h") | (√6/2)·s = √2·s·sin60° | 0.4686895712 | 1.2e-9 |

All four literals are the 8-decimal roundings of these expressions; no other simple candidate (e.g. ±1 apex, √3-based radius) fits to 1e-8. **The reconstruction is unique and one-parameter**: every coordinate is s times an element of ℚ(√2, √3, √6). Origin of each factor: c/s = cot(π/8) = 1+√2 (octagon), c − s = √2·s = half of (octagon circumradius − ring chord) = gap-triangle base, h = (c − s)·sin 60° (the 60° fold).

Canonical frame: origin = centre of the object; **principal axis = +Y** (the octagon hinge direction, "vertical" in the author's usage); azimuth φ = atan2(z, x) measured in the XZ plane; the +z direction is the one the octagons folded toward.

Vertex set (18 points), in units of s:

```
t_k = ( (1/√2) cos φ_k ,  +1     , (1/√2) sin φ_k )   φ_k = 60°·k , k = 0..5      (top ring)
b_k = ( (1/√2) cos φ_k ,  −1     , (1/√2) sin φ_k )                                 (bottom ring)
T_m = ( (√6/2) cos ψ_m ,  1+√2   , (√6/2) sin ψ_m )   ψ_m = 90° + 120°·m , m = 0..2 (top apexes)
B_m = ( (√6/2) cos ψ_m , −(1+√2) , (√6/2) sin ψ_m )                                 (bottom apexes)
```
Top and bottom apexes are **eclipsed** (same azimuths), not staggered — a direct consequence of the y → −y mirror in step "second triangle".

Primitive triangles: P_m^top = (t_{2m}, T_m, t_{2m+3}), P_m^bot likewise. Note the base of each primitive triangle is a **long diagonal** (diameter) of the ring hexagon, not a hexagon edge; the three top bases all pass through the ring centre (0, s, 0).

---

## 4. Vertex / edge / face census (Task B)

Rendering code produces 18 distinct vertices (no duplicates; H4 = G4 identification is already one point), 30 triangles, no duplicated faces:

| set | faces | notes |
|---|---|---|
| primitive triangles | 6 | 3 top, 3 bottom |
| cap faces | 12 | 6 per ring, nearest-apex rule (tie-broken by fp, see §7) |
| twisted side faces | 12 | 6 skew quads split along diagonal t_i–b_{i+1} |
| ring hexagons | 0 (lines) | every ring edge is already an edge of a cap face and of a side face |

Distinct edges: 60. Edge multiplicity: 30 edges lie in exactly 2 faces, 30 in exactly 1 (boundary). Edge-length classes (units of s):

| length /s | exact | count | which |
|---|---|---|---|
| 0.707107 | 1/√2 | 12 | ring hexagon edges |
| 1.414214 | √2 | 6 | primitive-triangle bases (ring diameters) |
| 1.581139 | √(5/2) | 12 | cap face: ring vertex → apex (non-primitive) |
| 2.000000 | 2 | 18 | primitive legs (12) + vertical struts t_j–b_j (6) |
| 2.121320 | 3/√2 | 6 | +1 diagonals t_i–b_{i+1} |
| 2.345208 | √(11/2) | 6 | +2 diagonals t_i–b_{i+2} |

Edge families of the side band [CODE]: each quad (t_i, t_{i+1}, b_{i+1}, b_{i+2}) has boundary edges t_i–t_{i+1} (ring), **t_{i+1}–b_{i+1} (vertical)**, b_{i+1}–b_{i+2} (ring), **b_{i+2}–t_i (+2)**, and interior diagonal **t_i–b_{i+1} (+1)**. So the coded object contains the "mirrored vertex" connections the author said to replace. Adjacent quads share only vertices, never edges: the band is six disjoint skew patches hung between the rings, each spanning 120° of azimuth; the union double-covers the circumference (this is the X-pattern in the front view).

Which entities are genuinely distinct: all 18 vertices, all 30 faces and all 60 edges are geometrically distinct. The only identification made by construction is H4 = G4 (apex). The six ring polylines coincide with existing face edges.

---

## 5. Topology / self-intersection status [DERIV]

Tested with exact segment–triangle intersection on all face pairs sharing ≤ 1 vertex:

- **Primitive triangles self-intersect.** Each pair of top primitives (and each pair of bottom) meets along a segment of length exactly a = s/√2 starting at the ring centre (0, ±s, 0) and running up the plane-intersection line (direction ∝ (3√3, 2√3, 3) for the pair P_0, P_1): 6 crossing segments in total. The three top bases are concurrent at the ring centre.
- Cap faces vs primitives: touch only at shared vertices/edges (no crossing).
- Side band: quads are skew (non-planar) and mutually disjoint except at vertices; no face crossings.
- Rings vs side/caps: coincident edges only.
- Non-manifold: 30 boundary edges (6 verticals, 6 +2-diagonals, 6 ring-vertex→apex edges of the "odd" cap faces, 12 others depending on the cap rule); no edge has > 2 faces in the as-coded object. The boundary graph is a single connected component made of several interlinked loops.
- Orientable? The non-boundary part is a disjoint union of small patches (each cap-pair/side-quad complex is a disc), so it is trivially orientable, but no global closed surface exists.
- Not closed, no interior/exterior, **volume is not defined**. Total face area is well defined per face (primitive area = (√7/2)·s² each, see §6); a total surface area is reported by the companion scripts but has no volumetric meaning.

**Classification:** an *open, non-manifold, self-intersecting 2-dimensional polyhedral complex* (immersed, not embedded; not a simplicial complex because faces cross transversally). It is not a polyhedron, not an antiprism, not a deltahedron. "Twisted hex crystal" should be read as a name, not a class.

The "second, tiny hexagon" [AUTHOR observation]: in the XZ projection (looking down the axis) t_j and b_j coincide; the six +2 diagonals project to two overlapping equilateral triangles (a hexagram) whose overlap is a regular hexagon of circumradius a/√3 = s/√6 ≈ 0.156. In 3D those diagonals are **skew** (they cross in projection at different heights), so the inner hexagon is a projection artefact, not a set of edges of the object. [DERIV]

---

## 6. Exact metric data [DERIV] (units of s; multiply by s = 0.38268 for the code's numbers)

Primitive triangle: sides (2, 2, √2); apex angle arccos(3/4) = 41.41°; base angles arccos(1/(2√2)) = 69.30°; height from base √(7/2) = 1.8708; area √7/2 = 1.3229. Face areas (units of s²): aligned cap 0.8197, tie cap √7/4 = 0.6614, side (t,t,b) 1/√2 = 0.7071, side (t,b,b) 0.7395. Plane makes angle arctan(√3/2) = 40.89° with the axis, i.e. 49.11° with the ring plane; tilt slope dz/dy = √3/2.

Rings: regular hexagons, circumradius = edge = 1/√2, at y = ±1. Ring-to-ring distance 2.

Apex triples: equilateral, side (√6/2)·√3 = 3√2/2 = 2.1213, circumradius √6/2, plane y = ±(1+√2), eclipsed top/bottom.

Cap faces (ring edge + apex): the three "aligned" caps (edge midpoint azimuth = apex azimuth) are isosceles (1/√2, √(5/2), √(5/2)); the three "tie" caps are (1/√2, 2, √(5/2)) and share one leg with a primitive triangle.

Side band: verticals 2; +1 diagonals 3/√2; +2 diagonals √(11/2); quad dihedral twist between the two triangle halves = 2·arctan(…) numeric 34.4° (skew quad, not planar).

Dimensionless invariants relevant to registration (all exact):
- apex-plane offset / apex-triangle side = c/(h√3) = (2+√2)/3 = 1.13807
- apex-plane offset / apex circumradius = c/h = √6(1+√2)/3 = 1.97119
- ring radius / apex radius = a/h = 1/√3
- ring half-height / apex half-height = s/c = √2 − 1
- apex-to-apex (top–bottom, same azimuth) / apex-triangle side = 2c/(h√3) = 2(2+√2)/3 = 2.27614

---

## 7. Symmetry group (Task D) [DERIV]

Tested against all 24 operations of D6h (C6 about Y, σ_h: y→−y, σ_v through apex azimuths, C2′ = σ_h σ_v); results are exact vertex/face-set invariances.

| object | group | order | improper ops present? |
|---|---|---|---|
| vertex set (18 pts) | **D3h** | 12 | yes (σ_h, 3 σ_v, S3) |
| six primitive triangles | **D3h** | 12 | yes |
| rings + caps, **as coded** (fp tie-break) | Cs (σ_h only) | 2 | yes |
| rings + caps, symmetric tie rule (+60° or −60°) | C3h | 6 | yes (σ_h) |
| rings + caps, aligned-only (3 caps/ring) or both-apexes (9/ring) | D3h | 12 | yes |
| side band as 6 skew **quads** (+1 twist) | **D6** (chiral) | 12 | **no** |
| side band as 12 **triangles** (diagonal t_i–b_{i+1}) | C6 (chiral) | 6 | no |
| FULL object **as coded** | **C1** | 1 | — |
| FULL, quad sides + aligned-only or both-apex caps | **D3** (chiral) | 6 | no |
| FULL, triangulated sides + symmetric-tie caps | C3 | 3 | no |

Key points:
1. The one-step twist destroys every mirror and inversion: σ_h, σ_v and S3 all map the +1 band to the −1 band. Only rotations survive. (author's "accidentally beautiful symmetry" = the D3 skeleton.)
2. The **as-coded** render has *no* symmetry at all, for two reasons that are not author intent: (a) the nearest-apex cap rule has exact ties on the edges at azimuth 30°, 150°, 270° (both neighbouring apexes at distance √(5/2)·s… numerically 0.676495); floating point assigned 3 caps to the 330° apex, 2 to 90°, 1 to 210° on both rings; (b) splitting each skew quad along t_i–b_{i+1} removes the C2′ axes.
3. The symmetry the author *saw* and praised is the intrinsic D3 of {vertices, primitives, quad band}. Recommendation: canonicalise with quad sides (or symmetric triangulation) and an explicitly symmetric cap rule (§11-Q4); do **not** treat C1 as the object's symmetry.

---

## 8. Handedness (Task D continued) [DERIV]

Definitions: +1 object = code as written. Mirror image = σ_v(+1) (equivalently σ_h(+1) for the band).

- As quads, σ_v(+1) = σ_h(+1) = the family **(t_i, t_{i+1}, b_{i−1}, b_i)**, i.e. "top edge (i,i+1) over bottom edge (i−1,i)". This is the correct −1 object. Warning: replacing *both* `bot[(i+1)]→bot[(i-1)]` and `bot[(i+2)]→bot[(i-2)]` literally gives (t_i,t_{i+1},b_{i−1},b_{i−2}), a −2 shift, which is **not** the mirror (verified False).
- Explicit −1 code: `b1 = bot_hex[i]; b2 = bot_hex[(i-1)%6]; faces (t2, t1, b1), (t2, b1, b2)` (this is exactly σ_v applied to the +1 triangulation; σ_h gives the same quads with the other diagonal).
- **No proper rotation** (of the 12 candidates in D6, and hence none at all, since any symmetry of the vertex set lies in D3h ⊂ D6h) maps +1 to its mirror image — checked for as-coded, +60-tie, aligned-only and both-apex cap variants. Since the full object's symmetry group contains no improper element, the +1 and −1 twists form an **enantiomorphic pair** (geometric/combinatorial handedness). They are related by a reflection (σ_v or σ_h), not by any rotation. Nothing physical is implied.

---

## 9. Abstract host-registration theorem (Task E) [DERIV]

Data: host centre O; three upper target points S_0, S_1, S_2 (centres of the chosen upper side of each accepted octagon). Crystal upper apexes A_k = (h cos ψ_k, c, h sin ψ_k), ψ_k = 90°+120°k, centre at origin, axis +Y. Sought: X ↦ O + σ R X, σ > 0, R ∈ SO(3), with A_k ↦ S_{π(k)} for some cyclic permutation π.

Let G_S = (S_0+S_1+S_2)/3, d = G_S − O, n = d/|d|, L = |S_i − S_j| (any pair), and ρ_S = circumradius of triangle S.

**Theorem (necessary and sufficient).** An exact fit exists iff
1. S is equilateral: |S_0S_1| = |S_1S_2| = |S_2S_0| = L (then ρ_S = L/√3);
2. the plane of S is perpendicular to d: (S_i − G_S)·d = 0 for all i (equivalently the centroid of S lies on the line through O along the S-plane normal);
3. **one-scale condition** |d| / L = c/(h√3) = (2+√2)/3 ≈ 1.13807 (equivalently |d|/ρ_S = √6(1+√2)/3 ≈ 1.97119).

Then σ = L/(h√3) = L·(√2/3)/s… in absolute units σ = L /( (3√2/2)·s ) = L/(3s/√2); R is the unique proper rotation sending +Y ↦ n and A_0 ↦ direction of (S_{π(0)} − G_S) for the correspondence π whose cyclic order about n matches that of the A_k about +Y (one of the two orientation classes is always realisable because the target's cyclic order is fixed by n and a C2 flip is not allowed, but all three cyclic shifts of that class are equivalent by the crystal's C3).

Proof sketch: (1) is congruence up to one scale; (2)+(3) express that A's centroid sits on the axis at signed height c and its circumradius is h, so the axial/radial ratio is forced; sufficiency: the three conditions determine σ and R and map all three points; necessity: any similarity preserves ratios of the rigid configuration {O, A_0, A_1, A_2}.

Failure diagnostics (Case 3): report (i) equilaterality residual max|L_ij − L̄|/L̄; (ii) tilt angle between S-plane normal and n; (iii) ratio residual (|d|/L) − (2+√2)/3.

**Lower prediction (Task E/F).** Under the same transform the lower apexes are B_k ↦ O − σ c n + σ h R(radial_k) = **2·(projection of S_{π(k)} onto the plane through O ⟂ n) − S_{π(k)}**, i.e. exactly the mirror images of the upper targets through the transverse plane at O. Equivalently: predicted lower apexes are eclipsed with the upper ones. If the accepted host's lower side-centres S′_k are available, compute residual_k = |S′_k − mirror_O,n(S_{π(k)})|. If the host's lower sides are staggered by 60° (antiprism-like host), the residual is ≈ 2·σ·h·sin 30° = σh and the result is CASE 2 by construction, not by error.

Historical note [CODE, informative only, NOT the accepted host]: in the V/G/H tri-octagon of this chat (V flat at z=0, G/H folded to z ≤ 1.6, hinges ∥ Y) the crystal sat with both ring chords **on V** and apexes pointing into the fold pocket (+z). That host has only a mirror plane x = 0 and no C3 about Y, so "upper side centres of the three octagons" is not even a C3-related triple there; the crystal's C3 came from cloning the triangle pair, not from the host. Any host in which the three octagons *are* C3-related about the crystal axis is a later construction (Paper C) and must be tested with the theorem above.

---

## 10. Fit status against the current accepted Tri-Octagon geometry

Not available in this conversation (the only host present is the historical V/G/H build, which is not the accepted model; RTM host excluded by the order). Registration NOT_TESTED; DEFORMATION_REQUIRED_FOR_FIT = UNKNOWN. §9 gives the complete test as three scalar checks plus one predicted-lower comparison; Codex can run it on Paper C coordinates directly.

---

## 11. Exact open questions for Hilmir / GPT

Q1. Apex height: you said "snap grid is 1 and −1 on the top of the small triangle". The code has apex y = cos(π/8) = 0.9239 (from the octagon), not 1. Is 0.9239 correct (gap-derived) or did you intend exactly ±1?
Q2. Spin axis: you asked to spin about the apex (red dot). The code spun about the central Y axis (apex is at z = 0.469 off that axis). You accepted the picture. Which is canonical? (Spinning about the apex would put all six apexes on one line and change everything.)
Q3. Twisted band: you said connect top[i] to bottom[i+1] *instead of* mirrored vertices. The code's twisted quads still contain the vertical struts t_j–b_j and add +2 diagonals. Is the intended band (a) the six skew quads as coded, (b) only the +1 diagonals (a plain hexagonal-antiprism band, 12 triangles t_i,t_{i+1},b_{i+1} / t_{i+1},b_{i+1},b_{i+2}), or (c) something else? (Your later antiprism sketch suggests (b) was the original mental image; you then said "don't change anything".)
Q4. Cap rule: three ring edges per ring are exactly equidistant from two apexes. Options: 3 aligned caps per ring (D3h caps, keeps D3 overall), 6 caps with a fixed +60° or −60° tie rule (C3 overall, adds a second handedness), 9 caps (both apexes), or the fp-accidental assignment (C1). Which is the object?
Q5. "To the left": from which viewpoint? This fixes whether the accepted object is +1 or −1 (they are mirror images; either is fine, but one must be named canonical).
Q6. Is the rendering's triangulation of the skew quads part of the object, or should the sides be stored as 4-gons (bilinear patches)?
Q7. The inner hexagon you saw is a projection artefact (§5). Do you want it promoted to real edges (it would add 6 vertices at radius s/√6 at heights determined by the crossing parameters)?

---

## 12. Recommendation for the Codex verification task

1. Rebuild vertices from the symbolic model (§3) with s = sin(π/8) and assert max |symbolic − literal| < 5e-9 for the four literals, and that all 18 rendered vertices match to 1e-8.
2. Assert edge-length classes and counts of §4; assert the census (18 V / 60 E / 30 F, multiplicities 30×1 + 30×2, no duplicate faces).
3. Reproduce the six primitive-triangle crossing segments (length a = s/√2 each) with an independent triangle–triangle routine; assert no other face crossings.
4. Symmetry: implement the 24 D6h ops; assert the table of §7 (vertex set D3h; as-coded full = C1; quad-band D6; quad+aligned caps = D3). Flag the cap-tie issue by asserting that the three tie distances are equal to 1e-12.
5. Handedness: build −1 as σ_v(+1); assert no proper rotation maps +1 → −1; assert the literal "shift −1 in both indices" is NOT the mirror.
6. Registration: implement §9 as a function `fit(O, S0, S1, S2) → (status, σ, R, residuals, predicted_lower)` and run it on Paper C's upper side-centres; if lower side-centres exist, report the eclipsed-mirror residual. Do not fit the lower points independently.
7. Freeze the canonical object only after Q1–Q6 are answered; until then carry two versions (as-coded, and symmetric-canonical = quad sides + aligned caps) through every test.

Companion scripts used here: `analyze.py` (source-faithful census/intersections), `analyze2.py`, `analyze3.py` (symbolic model, cap variants, symmetry, handedness) — all in outputs.
