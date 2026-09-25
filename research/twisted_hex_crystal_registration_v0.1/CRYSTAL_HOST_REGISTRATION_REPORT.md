# Twisted hex crystal: historical reconstruction and exact host registration

Codex research packet, 2026-09-25. For GPT/Hilmir review; not adopted into the model.

**Result: Case B, with precise scope.** There is a one-parameter family with exact upper edge-center contacts, canonical apex heights ±1, a smaller and angularly displaced upper footprint, and predicted lower tips lying exactly on the corresponding lower horizontal edges. The lower tips do **not** coincide with their edge centers: their residual is exactly the free parameter \(t>0\). The accepted host does not select \(t\), a unique contraction, a unique angle, the intermediate-ring rule, or face topology.

If *both* upper and lower edge **centers** must coincide, strict upper contraction is impossible in the stated axis-centered planar-similarity family. That stronger requirement is Case D; no extra deformation has been introduced to defeat it. It is not a prohibition on the requested upper-contact/lower-prediction problem.

The historical mesh is faithfully recovered. Its supplied reconstruction note needs a correction: there are six additional primitive–cap crossing segments, besides the six primitive–primitive crossings. The originals remain byte-for-byte preserved.

## 1. Authority and provenance

The authoritative baseline was checked against direct `origin` main:

```
HEAD = main = origin/main = actual remote main
     = 1dca474e09b180664a17f85a0bb2f92967dd18f1
```

The host is the width-one welded realization in:

- `papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md`, §§2–4, 6–9 and Appendix B.
- `kernel_physics/geometry.py`, specifically `LOCAL_OCTAGON`, `panel_point`, `folded_module`, `CENTROID`, and `rotate_c3`.

Their exact SHA-256 identities appear in [HOST_GEOMETRY.json](HOST_GEOMETRY.json); all pre-existing repository files are pinned in [PRESERVATION_BEFORE.json](PRESERVATION_BEFORE.json).

The user explicitly confirmed **“Highest horizontal edge”** in this task. Thus the upper targets are the midpoints of local edges 5–6, not the upper chamfers. Corresponding lower edges are 1–2.

Evidence labels used here:

| Layer | Authority and scope |
|---|---|
| HISTORICAL_AUTHOR_INTENT | Statements attributed to Hilmir by the supplied Claude note, §1. The originating chat was not independently available or searched. |
| HISTORICAL_AS_CODED | The literal preserved `tri_oct.py`, including its rounded constants, NumPy rotations, cap tie-breaking and triangle connectivity. |
| CURRENT_CANONICAL_INTENT | The current work order and the user's direct highest-horizontal-edge clarification. This supersedes old ambiguous choices for the new candidate only. |
| SOURCE FACT | Coordinates or behavior read from those files. |
| DERIVATION | New mathematical reasoning in this report, with executable checks where indicated. |
| NEW ASSUMPTION | The lower-edge-contact subfamily and proposed ring/face rules. These are not recovered historical equations or author-selected constants. |

Original inputs are preserved under [source_evidence](source_evidence/): the work order, `tri_oct.py`, and `twisted_hex_crystal_research_note.md`. No original was edited. No new Claude review was sought. The separate RTM project was not used.

Paper C §8, paragraph beginning “In Paper D's aligned measurement family,” explicitly distinguishes the fixed-center shrink construction from its welded width-one module: the shrink loses the old seams and changes top height. It supplies no crystal contraction/offset law. Neither Paper D's proposal nor its regular-hexagon condition is silently adopted here.

## 2. Historical reconstruction

The supplied script was inspected before execution. Its plotting tail writes an absolute output path and invokes an `os.system` copy. Those statements were not executed. The verifier extracts only the reviewed geometry prefix by AST into `source_evidence/geometry_prefix_executed.py`, checks the preserved source hash, supplies NumPy, and executes that prefix. A separate literal implementation reproduces the primitive arrays bit-for-bit in this runtime.

[HISTORICAL_CRYSTAL.json](HISTORICAL_CRYSTAL.json) records all 18 vertices, binary64 hexadecimal values, primitive/cap/side face indices, ordered rings and apex blocks, cap assignments, dimensions, intersections and predicate outcomes.

The original axis is \(+Y\), with azimuth \(\operatorname{atan2}(z,x)\). The exact **source literals**, not substituted radicals, are:

| Dimension | Literal value |
|---|---:|
| Ring circumradius \(a\) | 0.27059805 |
| Ring half-height \(b\) | 0.38268343 |
| Apex half-height \(c\) | 0.92387953 |
| Apex radius \(h\) | 0.46868957 |

The source rotates two primitive triangles through 0°, 120°, 240° about the global Y axis. Each primitive's base is a ring diameter. It sorts the rings, assigns each edge to its nearest apex, and renders the six primitives, twelve cap triangles and twelve side triangles.

The radical interpretation in Claude's §3 is well supported as an **idealization**:

\[
s_h=\sin(\pi/8),\quad c_h=\cos(\pi/8),\quad
a=s_h/\sqrt2,\quad b=s_h,\quad c=c_h,\quad h=\sqrt6\,s_h/2.
\]

These expressions round to the four literals. Finite rounded decimals do not uniquely determine exact numbers without a restricted model class. The note's unrestricted “exact, unique” claim is therefore not accepted. The as-coded binary rotations are also not exact algebraic 120° rotations.

### 2.1 Topology and note dispositions

| Item | Independently observed disposition |
|---|---|
| \(V,E,F\) | 18, 60, 30; no duplicate triangles |
| Edge incidence | 30 boundary edges, 30 edges of incidence two; none above two |
| Vertex links | 14 nonmanifold vertices in the literal face complex; listed by index in JSON |
| Boundary | One connected, branching boundary graph, not disjoint simple boundary loops |
| Orientation | Edge-adjacency orientation constraints are consistent; the whole object is not a manifold surface |
| Intersections | **12** crossing face pairs: six primitive–primitive and six primitive–cap |
| Closed/volume | Open and self-intersecting; no enclosed-volume interpretation |
| Symmetry | Full face complex C1; the rounded vertex scaffold is numerically near the ideal D3h scaffold |
| Cap assignment | Per level, source apex-array indices receive 2, 3, 1 caps |
| Exact tie issue | In the exact-rotation idealization, three of six ring-edge nearest-apex choices are ties |
| Edge-length classes | The six length-class counts 12, 6, 12, 18, 6, 6 reproduce Claude's table |

The numerical all-pairs intersection routine tests all 435 triangle pairs, including pairs sharing an edge or a vertex, and removes only the prescribed shared simplex. It uses tolerance \(10^{-10}\), with triangle-membership validation for nearly parallel planes. Five elementary positive/negative intersection probes also pass. It is a numerical diagnostic, not a claim of exact binary-float geometry certification.

The new six primitive–cap crossings are not tolerance noise. An exact counterexample in the radical idealization is:

\[
P=(a,b,0),\quad A=(0,c,h),\quad
Q=(a/2,b,\sqrt3 a/2),\quad B=(\sqrt3 h/2,c,-h/2).
\]
\[
E=\tfrac34P+\tfrac14A=\tfrac34Q+\tfrac14B.
\]

The segment \(PE\) is contained in the primitive through \(P,A,(-a,b,0)\) and the cap through \(P,Q,B\). Beyond \(P\), it is not their shared vertex or a prescribed common edge. Its length is \(s_h/2\). The verifier checks both endpoint equality and squared length exactly. Rotations and reflections of this local configuration cover the other tie-cap choices; the three source-selected tie caps on each level give the six listed crossing pairs. Their floating-point selections are not a C3-invariant face set. The six primitive–primitive segment lengths are \(a=s_h/\sqrt2\), also checked symbolically.

Thus Claude §5's “cap faces vs primitives: touch only at shared vertices/edges” and §12's proposed “no other face crossings” assertion are rejected. This does not invalidate its vertex census, basic source reconstruction, or primitive-crossing result. Its tables for additional unimplemented quad/cap variants were not silently promoted to independently verified results.

Other historical discrepancies remain explicit:

- The note reports an apex-pivot request, but the code rotates about the global axis. An apex with \(x=0,z=h\ne0\) is off that axis.
- The code's apex height is the literal 0.92387953, not 1.
- Actual side triangles are \((t_i,t_{i+1},b_{i+1})\) and \((t_i,b_{i+1},b_{i+2})\). They retain vertical \(t_jb_j\) edges and +2 connections; adjacent two-triangle patches meet at vertices rather than forming a coherent side annulus.
- Nearest-apex floating-point ties introduce a non-C3 cap assignment.
- A skew four-corner boundary is not a planar polygonal face merely because a renderer fills two triangles.

These are historical facts and corrections to the supplied account, not repairs to the original script.

### 2.2 The historical one-scale test fails

For the radical historical apex triple,

\[
\frac{\text{apex-plane height}}{\text{apex-triangle side}}
=\frac{2+\sqrt2}{3}.
\]

For the chosen current host targets that ratio is 1. Their exact difference is \((1-\sqrt2)/3\ne0\). A centered rigid similarity cannot align both height and radial size. The literal-code diagnostic reaches the same conclusion, with its physical radial residual stored in JSON. No historical uniform rescale is used as the new candidate.

## 3. Exact accepted host and targets

Use width one and define

\[
s=\sqrt2-1,\quad d=1-\frac{\sqrt2}{2}=\frac{s}{\sqrt2},
\quad r_0=\frac{\sqrt3}{6},\quad O=(0,r_0,0).
\]

The host axis is \(+z\). Relative to \(O\), outward horizontal normals in C3 order (panels 2, 3, 1) are

\[
n_0=(0,-1),\quad n_1=(\sqrt3/2,1/2),\quad
n_2=(-\sqrt3/2,1/2).
\]

The panel planes are \(n_k\cdot(X_{xy}-O_{xy})=r_0\). The octagon centers are respectively \((0,0,0)\), \((1/4,\sqrt3/4,0)\), and \((-1/4,\sqrt3/4,0)\).

The upper and lower edge centers are

\[
U_k=O+(r_0n_k,\tfrac12),\qquad
L_k=O+(r_0n_k,-\tfrac12).
\]

Each triple is equilateral, with side \(1/2\), circumradius \(r_0\), and centroid on the host axis. Their planes are perpendicular to that axis. There is **zero** angular stagger. Each upper edge has endpoints \(U_k\pm(s/2)(Jn_k,0)\), with the same formula about \(L_k\) below, where \(J(x,y)=(-y,x)\).

All 24 material panel vertices were independently reconstructed from Paper C's coordinate formulas and compared exactly against the unchanged accepted geometry module. Octagon edge lengths, target C3 action, plane equations and center agree exactly. The machine-readable host includes the panel polygons, welded mesh, adjacent chamfer metrics and the unused chamfer-midpoint alternatives.

The relevant host notch has base \(d\), two legs \(s\), vertical rise \(d\), radial rise \(\sqrt3d/2\), and tip angle \(\arccos(3/4)\). Its axial projection has a different angle. Neither the notch nor the octagon half-angle fixes a crystal twist by itself.

## 4. Upper registration and the minimum freedom

Let canonical coordinates have origin zero and upper/lower apex heights ±1. The physical map is

\[
X=O+\sigma x,\qquad \sigma=\tfrac12.
\]

The exact upper contact then forces canonical upper apex radius \(2r_0=1/\sqrt3\). All three upper residual vectors vanish.

If the upper footprint is obtained from the lower by \(\alpha R_\delta\), upper contacts alone leave lower radius and relative phase free. They do not choose \(\alpha,\delta\). Requiring all six corresponding edge centers would force equal radii and equal angular footprints:

\[
\alpha=1,\qquad\delta=0\pmod{2\pi/3},
\]

contrary to strict contraction and a small nonzero offset. This is a bounded no-fit result for these projection, centering and similarity hypotheses, not a universal obstruction to all conceivable crystals.

### 4.1 A one-parameter sufficient construction

**New assumption:** require each predicted lower tip to lie on its corresponding lower horizontal edge. This is stronger than the work order's requirement to *compare* it with the center. It gives a particularly economical exact-fit subfamily:

\[
B_k=L_k-t(Jn_k,0),\qquad 0<t\le s/2.
\]

The upper tips remain \(A_k=U_k\). The lower points are generated by the same planar map for every k; they are not separately optimized or fitted. In centered horizontal coordinates,

\[
B_{k,xy}-O_{xy}=(I-(t/r_0)J)(A_{k,xy}-O_{xy}).
\]

Consequently the upper structure is the contracted, rotated image of the lower:

\[
\boxed{\alpha(t)=\frac{r_0}{\sqrt{r_0^2+t^2}}=\cos\delta,\qquad
\delta(t)=\arctan(t/r_0).}
\]

Here \(0<\alpha<1\), \(0<\delta\le\arctan(\sqrt3s)<\pi/3\). The family includes arbitrarily small offsets. “Slight” has not been assigned an author-selected numerical threshold.

The radius/angle relation is **derived conditional on the added lower-edge-contact rule**. The particular value of \(t\) is not derived from the host. Without that rule there is a larger vertex family; for small angular offsets, remaining on the inward side of the corresponding plane requires \(\alpha\ge\cos\delta\), with other panel inequalities also to be respected. The one-parameter boundary-contact family is an existence witness, not an exhaustive enumeration of every possible crystal.

In particular, 22.5° is not selected by these equations. The octagonal constants enter the edge length and admissible interval; they do not prescribe the point within it.

### 4.2 Lower result and handedness

\[
|B_k-L_k|=t,\qquad \operatorname{dist}(B_k,\text{lower edge }k)=0.
\]

Thus `LOWER_ALIGNMENT = RESIDUAL`, with exact residual \(t\) at every tip. The lower triangle is rotated by \(-\delta\) relative to the upper, although the host's own target triangles are eclipsed.

`TWIST_MINUS` is the exact image of `TWIST_PLUS` under the host symmetry \(x\mapsto-x\), applied to vertices and faces together. It changes the sign of the offset and of the band step after reindexing. It is not obtained by naively negating two historical indices. Both hands have identical contact residuals and clearance. The host selects neither.

## 5. Intermediate rings and a clean face proposal

This section is a **new candidate rule**, not a uniquely recovered crystal definition.

Use the host central-band heights \(z=\pm s/2\). Put the upper regular ring at radius \(d/2\), half the host notch base, with vertices at

\[
\theta_i=-\pi/2+i\pi/3,\quad
T_i=(\tfrac d2\cos\theta_i,\tfrac d2\sin\theta_i,\tfrac s2)
\]

relative to \(O\). Define the lower ring by the same horizontal map as the lower apexes and reflection of z:

\[
B_i^{\rm ring}=\big((I-(t/r_0)J)T_{i,xy},-s/2\big).
\]

Canonical coordinates are twice these physical centered coordinates. The ring heights/radius reuse actual host measurements; their use as crystal ring placement and their phase relative to the apexes are declared design assumptions. They are not consequences of the three upper contacts.

As a useful comparison, normalizing the radical historical octagon's flat width \(2c_h\) to one would yield ring radius \(d/2\) and half-height \(s/2\) too. That observation does not rescue its apex fit: its apex radius would be \(\sqrt3d/2\ne r_0\). The new candidate also changes ring phase, lower-footprint transformation and cap topology. It does not retain the old exact primitive gap triangles as faces, and is not a common rescaling of them.

The proposed open face complex contains:

1. Six genuine next-vertex band boundaries
   \[
   Q_i=(T_i,T_{i+1},B^{\rm ring}_{i+2},B^{\rm ring}_{i+1}).
   \]
   Each is triangulated as \((T_i,T_{i+1},B^{\rm ring}_{i+2})\) and
   \((T_i,B^{\rm ring}_{i+2},B^{\rm ring}_{i+1})\). This removes the accidentally retained vertical struts and makes neighboring patches share band edges.
2. For each upper apex k, two triangles over ring edges \((2k-1,2k)\) and \((2k,2k+1)\). The lower fan rule is identical. Each apex is radially aligned with the middle ring vertex. No nearest-point selection or floating-point tie is used.
3. No internal ring-diameter primitive faces. They remain in the historical object, not in this new surface.

The +1 cross-ring edges implement the band connection; the +2 edges are expressly **tessellation diagonals**, not separately requested structural struts. The six quads are skew throughout the admitted interval: the stored determinant is proportional to \(2t-1\), while \(t\le s/2<1/2\). They are not claimed to be planar faces. A bilinear patch interpretation or another diagonal choice would be a different face construction, not a silently equivalent mesh.

The surface retains three peaks above, three below, two hexagonal rings and a twist. It is deliberately open; no top/bottom plate was added merely to obtain a conventional closed polyhedron.

### 5.1 Topology and embedding proof

For either hand:

| Quantity | Result |
|---|---|
| V, E, F | 18, 42, 24 |
| Boundary | 12 edges in two simple six-edge loops |
| Nonmanifold edges / vertices | 0 / 0 |
| Euler characteristic | 0 |
| Orientability | Orientable |
| Connectedness | One face-edge-connected surface |
| Closed/open | Open annulus |
| Self-intersections | None, by the family argument below; also none in all 276 face-pair checks per illustrated hand |
| Symmetry | C3 |
| Handedness | Mirror-related chiral pair; no host preference |

To verify the band throughout the parameter interval, let \(a,b>0\) be upper/lower ring radii and \(\lambda\in(0,1)\) the fractional distance down the band. In the frame of upper vertex i, its section alternates

\[
S_i=(1-\lambda)a e_0+\lambda b e_{\pi/3-\delta},\quad
D_i=(1-\lambda)a e_0+\lambda b e_{2\pi/3-\delta},\quad S_{i+1}=R_{\pi/3}S_i,
\]

where \(e_\theta=(\cos\theta,\sin\theta)\). Direct expansion, checked symbolically, gives

\[
\det(S_i,D_i)=\tfrac{\sqrt3}{2}(\lambda b)^2+
\lambda(1-\lambda)ab\sin\delta>0,
\]
\[
\det(D_i,S_{i+1})=\tfrac{\sqrt3}{2}((1-\lambda)a)^2+
\lambda(1-\lambda)ab\sin\delta>0.
\]

The vectors are positive combinations of rays spanning less than π. These inequalities place \(D_i\) strictly between \(S_i\) and \(S_{i+1}\) in angle. The section is therefore a simple star-shaped twelve-edge polygon; successive sectors do not overlap. Every interior-height band section is embedded.

Above and below the band, each two-triangle fan lies in its own 120° azimuth sector. Different fans meet only at their prescribed ring endpoints, and the cap slabs do not overlap the band interior. Thus the whole surface is embedded for the stated interval. The combinatorial vertex-link and orientation checks then establish the open annulus classification.

### 5.2 Clearance and exact symmetry scope

All apexes lie on their designated host panels. Every ring vertex is strictly inside all three inward halfspaces because

\[
(\tfrac d2)^2\left[1+(\tfrac{s}{2r_0})^2\right]<r_0^2.
\]

The lower-tip tangential bound places it on the actual finite horizontal edge; the other panel inequalities are strict. Since each triangle has at most one panel-contact apex and every other vertex is strictly inward, its interior cannot cross a host panel plane. This gives an exact no-penetration statement for the entire family. The host itself remains an open shell, not a recovered physical container or solid.

For the full Euclidean point-group upper bound, the vertex covariance has equal horizontal eigenvalues and a distinct larger vertical eigenvalue. The verifier checks this separation over the full interval using an exact upper bound on the horizontal value. Thus every symmetry preserves the vertical axis. Unequal upper/lower radii forbid reversal of z. The upper apex triple permits at most planar D3; the lower triple's phase \(\delta\), with \(0<\delta<\pi/3\), eliminates every common reflection. C3 remains and preserves the proposed faces. Hence each hand has no improper symmetry and is not properly congruent to its mirror. This is geometric chirality only.

## 6. Bounded verification, figures and reproduction

Final outcomes:

- Historical/source and diagnostic predicates: **17/17 PASS**.
- Host registration, symbolic identities/inequalities, topology and witness predicates: **70/70 PASS**.
- One exact algebraic illustrated witness and its mirror; **no parameter sweep**.
- Six research figures generated from the stored output coordinates.
- No model evolution or scientific-source regeneration.

These are 87 executed predicates, some overlapping or grouped, **not** 87 independent mathematical theorems. The quantified embedding and symmetry claims have the arguments in §5; numerical pair checks do not replace them.

Full outcomes are in [HISTORICAL_CRYSTAL.json](HISTORICAL_CRYSTAL.json) and [REGISTRATION_VALIDATION.json](REGISTRATION_VALIDATION.json). [EXECUTION_EVIDENCE.json](EXECUTION_EVIDENCE.json) records actual commands, versions, stdout, exit codes and product identities. The stdout is Codex's new verification execution, not an original historical captured run.

The displayed witness is
\[
t=s/4,\quad \alpha=2/\sqrt{13-6\sqrt2}\simeq0.9412709411,\quad
\delta\simeq19.73389846^\circ.
\]
It is chosen only to draw a legible family member. Neither this t nor its angle is claimed as a solution selected by the host or the author.

Figures:

- [01: host targets](01_host_targets.png)
- [02: historical and proposed geometry](02_historical_vs_canonical.png)
- [03: upper registration](03_upper_registration.png)
- [04: lower prediction and residual](04_lower_prediction.png)
- [05: both handed versions](05_twist_plus_minus.png)
- [06: full host embedding](06_full_host_embedding.png)

Run from this folder with Python, NumPy and SymPy available:

```text
python -B verify_crystal_geometry.py
python -B verify_host_registration.py
```

Matplotlib is needed only for:

```text
python -B render_figures.py
```

The host verifier needs the authoritative repository paths two levels above this folder. Exact runtime versions and the reused, pre-existing dependency location are recorded in execution evidence. No environment or large archive is copied into the packet.

## 7. Preservation and review disposition

[FINAL_PRESERVATION.json](FINAL_PRESERVATION.json) compares the original 589 tracked and 2,177 untracked file identities, all three supplied external inputs, HEAD and index bytes. All originals are preserved. New files are confined to this folder. `SHA256SUMS.txt` records packet identities and excludes only itself.

No kernel, accepted paper, historical original, previous research packet or publication record was edited. Nothing was staged, committed or pushed.

The useful review decisions are narrow: whether the proposed lower-edge-contact condition and ring/fan construction represent the intended visible form, and whether a parameter should subsequently be specified. No such choice has been made on the author's behalf. Exact lower-center coincidence is unavailable under strict contraction in this family; that limit is already resolved and needs no wider search.

```
HOST_SOURCE = Paper C publication v1.0.1 §§2–4,6–9; kernel_physics/geometry.py
HISTORICAL_OBJECT_RECONSTRUCTED = YES
CANONICAL_HEIGHT_FIXED_TO_1 = YES (HALF_HEIGHT)
HOST_UPPER_TARGETS_EXTRACTED = YES (USER_CONFIRMED_HIGHEST_HORIZONTAL_EDGES)
HOST_LOWER_TARGETS_EXTRACTED = YES

TOP_FOOTPRINT_CONTRACTION_ALPHA = r0/sqrt(r0^2+t^2)
TOP_FOOTPRINT_OFFSET_DELTA = +/-atan(t/r0)
PARAMETER_DOMAIN = 0<t<=(sqrt(2)-1)/2
ALPHA_DERIVED_FROM_HOST = NO (relation derived; unique value not selected)
DELTA_DERIVED_FROM_HOST = NO (relation derived; unique value not selected)

UPPER_REGISTRATION = EXACT
LOWER_ALIGNMENT = RESIDUAL (exactly t from centers; exactly on edges)
TWIST_PLUS_FIT = EXACT_UPPER_AND_LOWER_EDGE_CONTACTS
TWIST_MINUS_FIT = EXACT_UPPER_AND_LOWER_EDGE_CONTACTS
CANONICAL_TOPOLOGY = PROPOSED_OPEN_ORIENTABLE_EMBEDDED_ANNULUS; V18 E42 F24
CANONICAL_SYMMETRY = C3; MIRROR_PAIR
FIT_CLASS = B (conditional sufficient family; not unique host-selected geometry)
STRONGER_ALL_SIX_CENTERS_REQUIREMENT = D_WITH_STRICT_CONTRACTION
PHYSICAL_INTERPRETATION = NOT_ESTABLISHED
HEAD_CHANGED = NO
STAGED = NO
COMMITTED = NO
PUSHED = NO
```
