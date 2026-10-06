# TL4 Measurement cylinder top ring and directional frame recovery
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

Read-only mathematical recovery · 6 October 2026

**The clarified measurement scaffold can be defined precisely without changing the Tri-Octagon.** With its axis along the native \(e_z\), the smallest centered cylinder enclosing the current width-one polygonal surface and its symmetry centre has radius \(R=1/\sqrt3\), half-height \(H=1/2\), diameter \(2/\sqrt3\), and full height 1. Its highest ring is the circle at \(z=H\). It is a measurement reference, not a material boundary or a dynamical variable.

The remembered **~0.544 is not recovered as a geometric normalization** in the inspected sources. The nearby documented number \(0.541196100146197\ldots\) is the circumradius of one width-one octagon, measured from its own face centre. The documented fixed-face-centre hexagon-matching shrink is \((1+\sqrt2)/3\approx0.804738\). Neither is the required cylinder radius.

In top view the three seam-position rays are exactly opposite the three face-centre/normal rays. They add three **directed rays**, but no new **unoriented axes**. Tangent axes form a different, already defined set. The available mathematics identifies these alternatives; it cannot decide which set an unmarked historical recollection intended.

## Scope and evidence

**OWNER DESIGN CLARIFICATION.** The outer cylinder/circle and the 3D Tri-Octagon are primarily measurement geometry; the containing measurement domain includes the centre and the complete polygonal surface. “Top circle” now means its highest circular ring. A separate centered Vesica eye may eventually have orientation or rotation, but its dynamics are not defined. These statements guide the definitions below; they do not alter the accepted geometric coordinates.

**SOURCE FACT.** The authoritative repository [trioctagon-physics](project-source/trioctagon-physics) began and ended at `82cab10cbe550f58c43163fb8b05fabdad1b05ae`, on `main`, with the same index and existing dirty/untracked working-tree material. Current geometry means [geometry.py](project-source/trioctagon-physics/kernel_physics/geometry.py:16) and the separately typed [reference_scaffold.py](project-source/trioctagon-physics/kernel_physics/reference_scaffold.py:1). Historical `kernel_TO` displays are a different authority.

SOURCE FACT identifies a retained definition or record; OWNER DESIGN CLARIFICATION identifies present intent; DERIVED IDENTITY and EXACT THEOREM identify consequences proved here; NUMERICAL EVIDENCE identifies decimal or finite computational checks. OPEN QUESTION marks missing definitions. No physical interpretation, state update, rotation law or wave law is adopted. TL0–TL3 remain closed predecessor records; their earlier unresolved host choices are not rewritten.

## Recovered normalization history

### Two documented scales for the same folded surface

**SOURCE FACT.** [Actual Geometry Specification v0.1](project-source/reconstruction/TRIOCTAGON_ACTUAL_GEOMETRY_SPEC_v0.1.md:1), dated 20 September 2026, exported the folded geometry with octagon **side** \(s_{\rm old}=1\). It states

\[
W_{\rm old}=1+\sqrt2,\quad a_{\rm old}=\frac{1+\sqrt2}{2},\quad
R_{8,\rm old}=\frac{\sqrt{4+2\sqrt2}}2.
\]

Here \(W\) is the octagon's flat-to-flat width and height, \(a=W/2\) is its apothem, and \(R_8\) its circumradius. Thus old side one did **not** mean height one or radius one.

[Specification v0.2](project-source/reconstruction/TRIOCTAGON_ACTUAL_GEOMETRY_SPEC_v0.2.md:1) explicitly records the owner's width-one normalization and the exact conversion

\[
\boxed{x_{\rm current}=(\sqrt2-1)x_{\rm old}}.        \tag{1}
\]

This applies to every coordinate about the same original origin, with no rotation or translation. The symmetry centres scale by the same factor, so it also gives
\(x_{\rm current}-o_{\rm current}=(\sqrt2-1)(x_{\rm old}-o_{\rm old})\).
Lengths multiply by \(\sqrt2-1\), areas by \(3-2\sqrt2\), and angles and incidence remain unchanged. The [normalization receipt](project-source/trioctagon-physics/research_files/verification/actual_geometry/width_1/normalization_history.json) and the archived old/new vertex files preserve this conversion. All 18 exact vertices were independently compared in TL4, and the canonical archived vertex set agrees with the current source.

This is a recovered conversion between **two folded-geometry exports**. It is not a conversion from the historical `kernel_TO` state displays into the physics shell.

### Dimensions with their meanings retained

**SOURCE FACT / DERIVED IDENTITY.** [Paper C v1.0.1 §2](project-source/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md:41) distinguishes octagon side, apothem, width and circumradius. For general width \(W>0\),

\[
s=(\sqrt2-1)W,\quad a=\frac W2,\quad
R_8=\frac{W}{2\cos(\pi/8)}
=W\sqrt{1-\frac{\sqrt2}{2}}.
\tag{2}
\]

Let \(p\) denote the distance from the symmetry centre to a face centre, \(g_{\rm gap}\) a reference connector length, and \(\rho_6\) the six-point top measurement polygon's circumradius. The current folded family has

\[
p=\frac{W}{2\sqrt3},\qquad g_{\rm gap}=\frac{s}{\sqrt2},\qquad
\rho_6=\sqrt{p^2+s^2/4}
=W\sqrt{\frac56-\frac{\sqrt2}{2}}.                   \tag{3}
\]

| Quantity | Current width-one value | Meaning |
|---|---:|---|
| \(s\) | \(\sqrt2-1=0.414213562373095\ldots\) | One octagon side |
| \(a\) | \(1/2\) | Octagon apothem; also vertical half-height |
| \(W=2a\) | 1 | Flat-to-flat width; full height; central triangle side |
| \(R_8\) | \(\sqrt{1-\sqrt2/2}=0.541196100146197\ldots\) | Circumradius about an individual face centre |
| \(2R_8\) | \(1.082392200292394\ldots\) | Octagon vertex-to-opposite-vertex diameter |
| \(p\) | \(1/(2\sqrt3)=0.288675134594813\ldots\) | Face-centre radius; central triangle apothem |
| \(g_{\rm gap}\) | \(1-\sqrt2/2=0.292893218813452\ldots\) | Top measurement connector; also the chamfer cutback |
| \(\rho_6\) | \(\sqrt{5/6-\sqrt2/2}=0.355283762852717\ldots\) | Circumradius of the alternating top hexagon |
| \(R_{\min}\) | \(1/\sqrt3=0.577350269189626\ldots\) | Cylinder radius required by the full shell |
| \(2R_{\min}\) | \(2/\sqrt3=1.154700538379252\ldots\) | Cylinder diameter |
| \(H_{\min}\), \(2H_{\min}\) | \(1/2\), 1 | Cylinder half-height and full height |

The circumradius \(R_8\) and cylinder radius \(R_{\min}\) have different centres and different defining extrema. Substituting the former for the latter excludes the seams. The much smaller \(\rho_6\) encloses the six high points, not the full surface.

| Same welded geometry in retained units | Octagon side | Width / full height | Minimum cylinder radius | Half-height |
|---|---:|---:|---:|---:|
| Earlier export, \(s=1\) | 1 | \(1+\sqrt2\) | \((1+\sqrt2)/\sqrt3\approx1.393846850117352\) | \((1+\sqrt2)/2\approx1.207106781186548\) |
| Current export and kernel, \(W=1\) | \(\sqrt2-1\) | 1 | \(1/\sqrt3\) | \(1/2\) |
| General width chart | \((\sqrt2-1)W\) | \(W\) | \(W/\sqrt3\) | \(W/2\) |

For comparison with a source using an octagon circumradius \(R_8\), substitute \(W=2R_8\cos(\pi/8)\) in this table. This is an exact **local length conversion**. It gives a global conversion only if that source actually describes the same folded arrangement.

### The remembered decimal

**SOURCE FACT / OPEN QUESTION.** Text searches across the current geometry/Paper C/Paper D definitions, old and canonical geometry exports, reconstruction reports, retained historical paper extracts and `kernel_TO` geometry files did not recover **0.544 as a top-circle radius, cylinder radius, height or hexagon-matching factor**. Literal nearby matches in unrelated numerical tables do not supply geometric provenance. The documented nearby geometric value is \(R_8=0.541196100146197\ldots\), which rounds to 0.541, not 0.544, at three decimal places.

It is therefore possible that the recollection concerns \(R_8\), but TL4 does **not** identify the remembered number with it. Unindexed drawings or unrecovered original scripts could contain other conventions. No radius or factor is adopted from numerical closeness alone.

## The hexagon matching calculation and its actual scope

**SOURCE FACT.** The [retained hexagon derivation §6](project-source/research/GPT_proof/TRIOCTAGON_HEXAGON_CORE_DERIVATION_v0.1.md:244), formalized in [Paper D v0.1.1 §§4–14](project-source/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md), describes three selected length-\(s\) edges plus three deliberate gap connectors. It is a reference construction. The matching law was derived from an owner clarification in September 2026; it was not recovered as an equation in the inspected 2025 papers.

In a radial/tangential frame \((u_i,t_i)\) with 120° spacing, its endpoints are

\[
A_i=p u_i-\frac{s}{2}t_i,\qquad B_i=p u_i+\frac{s}{2}t_i.
\]

Direct subtraction gives

\[
B_i-A_i=s t_i,\qquad
A_{i+1}-B_i=\left(\sqrt3p-\frac s2\right)R_{60}t_i,
\]

so

\[
g_{\rm gap}=\sqrt3p-s/2,\qquad
\text{regular hexagon}\iff g_{\rm gap}=s\iff p=\sqrt3s/2.
\tag{4}
\]

The side turns are 60°, and the selected-edge and connector classes remain distinct. The generic polygon has circumradius \(\sqrt{p^2+s^2/4}\), selected-line offset \(p\), and connector-line offset \((2s+g_{\rm gap})/(2\sqrt3)\). Calling both offsets one hexagon apothem would be incorrect unless the polygon is regular.

**DERIVED IDENTITY.** At the original folded placement \(p_0=a_0/\sqrt3\), shrink each face's local coordinates about its own fixed vertical face centre by a factor \(\lambda\). The new side is \(\lambda s_0\), while \(p_0\) stays fixed. Matching gives

\[
\sqrt3p_0-\lambda s_0/2=\lambda s_0
\quad\Longrightarrow\quad
\boxed{\lambda=\frac{1+\sqrt2}{3}=0.804737854124365\ldots .}
\tag{5}
\]

At original width one,

\[
s'=g'_{\rm gap}=1/3,\quad p'=p_0=1/(2\sqrt3),\quad
W'=\lambda,\quad a'=H'=\lambda/2,\quad \rho'_6=1/3.
\tag{6}
\]

Thus the factor is **0.804738**, the new full width/height is **0.804738**, the new half-height is **0.402369**, and the regular hexagon side/circumradius is **1/3**. These are four typed quantities, not interchangeable measurements. [The current named function](project-source/trioctagon-physics/kernel_physics/reference_scaffold.py:364) implements this separate reference construction, not a change to `geometry.folded_module()`.

An alternative keeps each octagon's size fixed and translates its centre outward to \(p_* =\sqrt3s_0/2\). Both operations lose the original shared seams. Neither is a unit conversion of the original welded surface. A common global scaling sends \((p,s,g_{\rm gap})\) to \(c(p,s,g_{\rm gap})\), preserving \(g_{\rm gap}/s=1/\sqrt2\), so it cannot regularize the original hexagon.

The **two regular alternatives are**, however, similar to each other: in centered coordinates the fixed-centre-shrunk configuration equals \(\lambda\) times the outward-translated configuration. This follows from \(\lambda p_*=p_0\) and \(s'=\lambda s_0\). It does not make either alternative similar to the original welded arrangement.

| Configuration starting from original width one | Top hexagon circumradius | Whole vertical-frame cylinder radius | Half-height | Current welded shell? |
|---|---:|---:|---:|---|
| Original folded member | \(\rho_6\approx0.355284\) | \(1/\sqrt3\approx0.577350\) | \(1/2\) | Yes |
| Fixed-centre shrink | \(1/3\) | \(\sqrt{6+2\sqrt2}/6\approx0.495211\) | \((1+\sqrt2)/6\approx0.402369\) | No; separate faces |
| Fixed-size outward translation | \(\sqrt2-1\) | \(\sqrt{(5-3\sqrt2)/2}\approx0.615370\) | \(1/2\) | No; separate faces |

The radius formulas use the full finite faces, not just the six top endpoints. The shrink is relevant to identifying a **regular reference hexagon**. It does not justify shrinking the unchanged current shell to fit a preferred cylinder, and its smaller half-height cannot enclose the current shell.

“Fixed centre” also appears in Paper C's hinge construction, where the middle panel is held fixed while folding. That operation is different from (5), which fixes all three already placed face centres and shrinks their individual faces. Shrinking about the reference family's **planar** octagon centres is different again; those lie at radius \(L=p+a\), not \(p\).

## Measurement cylinder and highest ring

### Definition

Use the current native symmetry centre

\[
o=(0,\sqrt3/6,0),\qquad e_z=(0,0,1).
\]

For \(x\in\mathbb R^3\), write
\(z=(x-o)\cdot e_z\) and \(\rho=\|(I-e_ze_z^T)(x-o)\|\). Define

\[
\boxed{C(R,H)=\{x:\rho\le R,\ |z|\le H\},\quad R>0,\ H>0,}
\tag{7}
\]

where **\(H\) is half-height**. The full height is \(2H\). Its highest circular ring is

\[
\boxed{\Gamma_+(R,H)=
\{o+R(\cos\phi\,e_x+\sin\phi\,e_y)+H e_z:0\le\phi<2\pi\}.}
\tag{8}
\]

Here \(e_x=(1,0,0)=t_B\), \(e_y=(0,1,0)\) fix an azimuth convention; the circle itself is independent of that choice. The measurement domain includes its interior and the centre. Its lateral cylindrical surface, upper disk, upper ring, and vertical axis are distinct subsets. A plotted wireframe can represent the domain without making its lines material. The upper disk is the full maximum-height set of (7); (8) is its circular boundary and is the owner's specified “top circle.”

The centered cylinder has no distinguished horizontal azimuth of its own. The registered Tri-Octagon supplies the face and tangent labels. No \(R_n\), \(H_n\), force, response law or changing cylinder is introduced.

### Sharp enclosure of the actual surface and centre

**EXACT THEOREM.** For the native width-one surface \(S\),

\[
\boxed{S\subset C(R,H)\iff R\ge1/\sqrt3\text{ and }H\ge1/2.}
\tag{9}
\]

The same condition encloses \(S\cup\{o\}\), and even the convex hull of that set.

**Proof.** In the native face frames each centered filled octagon is

\[
x-o=p n_i+u t_i+z e_z,\quad p=1/(2\sqrt3),\quad
|u|\le1/2,\quad |z|\le\min(1/2,1/\sqrt2-|u|).
\tag{10}
\]

Therefore \(\rho^2=p^2+u^2\le1/12+1/4=1/3\), with equality on the three vertical seams; and \(|z|\le1/2\), with equality on the three upper and three lower short edges. Both bounds are attained, proving necessity and sufficiency independently. The point \(o\) has \(\rho=z=0\). Since the cylinder is convex, it also contains the convex hull whenever it contains the surface. ∎

At the minimum dimensions, the shell contacts the cylinder's lateral surface along the seams \(|z|\le s/2\), and contacts its upper/lower disks along the short horizontal edges. It **does not touch the highest ring itself**: all points of the shell at \(z=1/2\) have \(\rho\le\rho_6<1/\sqrt3\). The equality of the cylinder's top height and shell's top height does not identify their boundaries.

These are sharp minima for a cylinder centered at \(o\) with axis \(e_z\). No optimization over tilted or displaced cylinders is being claimed. If a finite core region larger than the point \(o\) is later specified outside the shell's convex hull, it needs its own bound; no such region is supplied in TL4.

### Hexagonal footprints and complete reference figures

For a centered horizontal polygon \(P\) placed at height \(z_0\), let \(\rho_P\) be its largest vertex radius. Its filled polygon and outline have the same sharp centered disk bound \(R\ge\rho_P\). Enclosing it together with the unchanged shell requires exactly

\[
R\ge\max(1/\sqrt3,\rho_P),\qquad H\ge\max(1/2,|z_0|).
\tag{11}
\]

A footprint alone specifies no 3D height. If it is placed at \(z=0\), its height requirement is zero; a nondegenerate cylinder may have arbitrarily small positive half-height unless other objects must also be enclosed.

| Retained footprint | Circumradius / required planar \(R\) | Height and normalization status |
|---|---|---|
| Current alternating top measurement hexagon | \(\rho_6=\sqrt{5/6-\sqrt2/2}\) | Six high endpoints at \(z=1/2\); connectors are measurement segments |
| General accepted aligned hexagon | \(\sqrt{(s^2+s g_{\rm gap}+g_{\rm gap}^2)/3}\) | Planar chart at zero, or top chart at \(z=a\), must be stated |
| Regular member at side \(s\) | \(s\); apothem \(\sqrt3s/2\) | No unique absolute \(s\) selected by regularity |
| Fixed-centre-shrink regular hexagon | \(1/3\) | Its own top plane is \(z=(1+\sqrt2)/6\) |
| Fixed-size-translation regular hexagon | \(\sqrt2-1\) | Its own top plane remains \(z=1/2\) |
| Historical projected triangle-intersection hexagon | \((2\sqrt2/3)t\) | Independent tetrahedral scale \(t\); no supplied conversion to shell width |
| Historical projection of the tetrahedra's 3D intersection | \(\sqrt{2/3}\,t\) | Different hexagon, rotated 30° in the retained projection chart |

The first five rows follow from the source coordinate definitions and (4). The last two are the separate exact dual-core constructions retained in [the hexagon derivation §3](project-source/research/GPT_proof/TRIOCTAGON_HEXAGON_CORE_DERIVATION_v0.1.md:60). Their side equals circumradius because they are regular. Their apothems are respectively \(\sqrt{2/3}\,t\) and \(t/\sqrt2\). Projection of an intersection and intersection of projections are not interchangeable. Neither source imposes a match between \(t\) and the current \(s\). For example, matching their sides to \(s\) would require two different extra choices, \(t=3s/(2\sqrt2)\) or \(t=\sqrt{3/2}s\).

For the full current [reference scaffold](project-source/trioctagon-physics/kernel_physics/reference_scaffold.py:181), one must also state **which reference objects** are being enclosed:

\[
p=\frac{s+2g_{\rm gap}}{2\sqrt3},\quad a=\frac{(1+\sqrt2)s}{2},\quad L=p+a.
\]

| Object in that family | Exact radial bound | Half-height when centered as defined |
|---|---|---|
| Six-endpoint hexagon and filled reference region | \(\sqrt{p^2+s^2/4}\) | 0 in planar chart; \(a\) if placed at its top plane |
| Support triangle including the three gap cells | \(2p\) | Same plane convention |
| Three complete vertical octagon frames | \(\sqrt{p^2+a^2}\) | \(a\) |
| Three complete planar octagon frames | \(\sqrt{(p+2a)^2+s^2/4}\) | 0 |

For vertical frames, the maximum occurs at local \(|u|=a\). For planar frames, an outer flat endpoint has local coordinates \((a,\pm s/2)\); it exceeds the other candidate \((s/2,\pm a)\) by squared-radius difference \(2L(a-s/2)>0\). Convexity then covers the filled polygons. The support triangle's vertices are at radius \(2p\). These proofs explain why the small central hexagon's circumcircle cannot be used as the enclosing circle of all the octagonal reference figures.

At original width one, adding the current top hexagon or its support triangle does not enlarge (9). Adding a separately drawn regular hexagon of side \(1/3\) also does not enlarge it, but such a hexagon is not the unchanged shell's actual six-point top chain. This distinction preserves the owner's measurement intent without deforming the shell.

## Top projection and the horizontal direction sets

### The exact image of the current surface

Define the top projection relative to \(o\) by

\[
\pi_z(x)=(e_x\cdot(x-o),e_y\cdot(x-o)).              \tag{12}
\]

Applying it to (10) removes \(z\), leaving the full segment \(p n_i+u t_i\), \(-1/2\le u\le1/2\), for each face. Thus

\[
\boxed{\pi_z(S)=\text{the perimeter of an equilateral triangle of side 1}.}
\tag{13}
\]

It is **not a filled hexagon or filled triangle**. The filled triangle is the convex hull of that image, a separate measurement region. Either complete nine-edge rim also projects onto the same triangle perimeter. By contrast, the highest subset \(S\cap\{z=1/2\}\) projects onto only three short length-\(s\) segments. Joining their six endpoints by three extra chords yields the alternating measurement hexagon. Those chords are not projected extra edges of the native surface.

### Rays and axes

Take azimuth from the current \(+x=t_B\) direction toward \(+y\). The source normals are

\[
n_A=(-\sqrt3/2,1/2,0),\quad n_B=(0,-1,0),\quad
n_C=(\sqrt3/2,1/2,0),\qquad t_i=e_z\times n_i.
\tag{14}
\]

A directed ray distinguishes \(v\) from \(-v\). An unoriented line/axis \(\mathbb Rv\) identifies them. All the horizontal vectors lie in a two-dimensional plane; “three axes” here means three distinguished lines, not three linearly independent coordinates.

| Distinguished object | Directed horizontal azimuths | Unoriented axis set |
|---|---|---|
| Outward face normals \(n_i\) | 30°, 150°, 270° | 30°, 90°, 150° modulo 180° |
| Face-centre rays \(c_i-o=p n_i\) | Exactly the preceding set | Same |
| Rays to projected seams / triangle corners | 90°, 210°, 330° | Same normal-axis set |
| Face tangents \(t_i\) | 0°, 120°, 240° | 0°, 60°, 120° modulo 180° |
| Directed connector edges of the CCW reference chain | 60°, 180°, 300° | Same tangent-axis set |
| Outward connector normals and corner-gap bisectors | 90°, 210°, 330° | Same normal-axis set |
| Vertices of a regular aligned reference hexagon | 0°, 60°, 120°, 180°, 240°, 300° | Same tangent-axis set |

**Proof of the opposite-ray statements.** The native triangle's corner opposite face \(i\) is \(-2p n_i\). Hence the three corner rays are \(-n_i\), even though no new line is introduced. Each physical seam itself runs vertically along \(e_z\); in top projection it becomes a point. A ray from the centre to that point is not the seam's spatial tangent.

For the aligned reference family, (4) gives connector direction \(R_{60}t_i\). As an unordered triple, \(\{R_{60}t_i\}=\{-t_i\}\), and similarly \(\{R_{60}n_i\}=\{-n_i\}\). A corner cell has endpoints on the adjacent selected-edge extensions and a connector opposite its apex; its symmetry bisector follows the same corner ray. Thus the three gaps have already specified directional data; they add reference segments and rays, not an independent geometric frame.

The **current alternating** hexagon's vertex directions are a further distinct object. If \(\alpha_i\) is a normal azimuth, then

\[
\arg A_i=\alpha_i-\gamma,\quad \arg B_i=\alpha_i+\gamma,
\qquad \gamma=\arctan\frac{s}{2p}.                  \tag{15}
\]

At the current width-one member, \(\gamma=\arctan(\sqrt3(\sqrt2-1))\approx35.657130^\circ\), so these six rays are not regularly spaced and are generally six distinct unoriented axes. At regularity \(p=\sqrt3s/2\), \(\gamma=30^\circ\); only then do the six vertex rays collapse to the three tangent axes with both directions present. Distinguishing edge directions from vertex rays avoids assigning the regular reference hexagon's directions to the unmodified top polygon.

The normal and tangent **axis sets** differ by 30° as unordered triples and are inequivalent under the native D3h symmetry. They are both already determined by (14). Reversing a normal gives an additional directed ray on an existing axis; turning it by 90° gives its tangent, a different line but no new free parameter.

**OPEN QUESTION.** If the remembered “three additional directions” means three directions between the face-centre rays, the seam/gap rays \(-n_i\) are an exact match to that description. If it means the opposite three vertices of a regular measurement hexagon, they are \(-t_i\) relative to the chosen \(t_i\) triple. If it means tangent versus normal lines, those are genuinely different distinguished line sets, already supplied by the frame. No surviving marked diagram or explicit identification selects among these meanings. The separately projected historical dual-core hexagons likewise need a registration before their azimuths can be identified with the native frame.

![Top and side projections of the unchanged shell and a separately identified regular reference hexagon](project-source/research/TL4_measurement_frame_20261006/TL4_MEASUREMENT_VIEWS.png)

**Static geometric illustration.** Left: the native shell projects to the blue triangle perimeter; the dashed inner chain is the top measurement hexagon, and the green circle is the projected measurement top ring. Centre: the same shell seen along a face normal, inside the side projection of its minimum cylinder. Right: the separate regular side-\(1/3\) reference hexagon, with its tangent-axis rays. The right panel does not replace the native geometry. Coordinates use the same original width-one unit throughout.

## Viewpoint and active orientation

### Top and side views of the fixed object

A view frame with orthonormal screen axes \(a_0,b_0\) and sight direction \(c_0=a_0\times b_0\) gives orthographic coordinates

\[
\pi_{a_0,b_0}(x)=(a_0\cdot(x-o),b_0\cdot(x-o)).       \tag{16}
\]

Top view uses \((e_x,e_y)\). A side view along the face-normal line \(n_B\) uses \((t_B,e_z)\), giving \((x,z)\) in centered coordinates. The two views erase different coordinates; neither changes \(S\).

For completeness, the side image can be characterized exactly. At fixed \(z\), let
\(U(z)=\min(1/2,1/\sqrt2-|z|)\), for \(|z|\le1/2\). The projected intervals of the three panels are

\[
[-U,U],\quad[-1/4-U/2,-1/4+U/2],\quad[1/4-U/2,1/4+U/2].
\]

They overlap because \(U\ge s/2>1/6\). Their union is therefore

\[
\pi_{t_B,e_z}(S)=\{(x,z):|z|\le1/2,\quad |x|\le1/4+U(z)/2\}. \tag{17}
\]

This is a filled, nonregular octagonal projection, with corners \((\pm1/2,\pm s/2)\) and \((\pm1/(2\sqrt2),\pm1/2)\). The top image (13) and side image (17) are different images of precisely the same surface. The measurement cylinder projects to a disk from the top and a rectangle from the side. Its top ring projects to a circle in the first view and a horizontal segment in the second.

More generally, orthogonal projection obeys

\[
\|\pi_{a_0,b_0}(x)-\pi_{a_0,b_0}(y)\|^2
=\|x-y\|^2-|(x-y)\cdot c_0|^2.                      \tag{18}
\]

Depth is lost and apparent lengths/angles can change. Euclidean distances and angles of the actual object do not. Perspective images add camera-distance and focal-length choices; none is needed for the orthographic recovery here.

### Vesica-plane and quarter-turned Vesica-plane views

Represent a centered lens by

\[
E(u,v)=o+u a_0+v b_0,\qquad
(|u|+d/2)^2+v^2\le r^2,
\quad c_0=a_0\times b_0.                            \tag{19}
\]

The face-on eye view \(\pi_{a_0,b_0}E=(u,v)\) recovers the planar lens. To exhibit a quarter-turn without selecting a spin axis, **conditionally** use a rotation \(Q\) about the centreline \(a_0\):
\(Qa_0=a_0\), \(Qb_0=c_0\), \(Qc_0=-b_0\). Then:

- An **active** rotation of the eye gives \(E_Q(u,v)=o+u a_0+v c_0\). The measurement shell and cylinder are fixed. In the old face-on view this rotated lens projects to \((u,0)\).
- A **viewpoint change only**, from screen \((a_0,b_0)\) to \((a_0,c_0)\), leaves the original eye fixed and also projects it to \((u,0)\).
- Rotating both the eye and its face-on camera frame gives \(\pi_{Qa_0,Qb_0}E_Q=(u,v)\): the image is unchanged despite the eye's changed orientation relative to the fixed shell.

In matrix form, if \(A=[a_0\ b_0]\), these are \(A^TQA=\operatorname{diag}(1,0)\), \((QA)^TA=\operatorname{diag}(1,0)\), and \((QA)^TQA=I_2\). For any proper rotation, \(Q^TQ=I\) preserves the eye's internal lengths, but its relation to the fixed measurement frame can change. A passive coordinate change applies \(Q^T\) to **every** object's coordinates and changes no relative geometry.

Consequently seeing another form does not determine whether the eye moved or the camera moved. A 90° angle without a pivot, axis and active/passive convention is insufficient. Equation (19) and this example do not select an intended axis or a rotation law.

## Historical displays and current reference coordinates

**SOURCE FACT.** The historical [Recursive Engines §1](project-source/trioctagon-physics/research_files/verification/phase3_host_feedback/paper_text_pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.txt:26) uses octagon circumradius \(R_8\), a different centre-circle radius \(L>R_8\), a shared planar orientation, and a proposed tilt. It fixes no numerical \(L/R_8\), enclosing cylinder height, or top ring. The cited `tri.py` and `center3.py` are not recovered in the inspected tree. A local change from \(R_8\) to \(W\) units via (2) cannot fill in those missing global choices or turn the shared-orientation placement into the current folded shell.

The current reference scaffold instead has radial directions \(u_i=(\cos(2\pi i/3),\sin(2\pi i/3))\), a vertical face-centre radius \(p\), and a distinct planar octagon-centre radius \(L=p+a\). Its Paper-C member matches the current shell only after the explicit rigid registration

\[
M(x)=R_z(\pi/6)x+(0,a/\sqrt3,0),\qquad p=a/\sqrt3.   \tag{20}
\]

This is the source's [paper_c_rigid_map](project-source/trioctagon-physics/kernel_physics/reference_scaffold.py:344). Frame indices \(0,1,2\) map to panels \(P_3,P_1,P_2\). With \(s=\sqrt2-1\), no scale factor is needed; the two coordinate descriptions have the same width-one length unit. Generic reference-family members or its complete planar octagons are different point sets, even when their input side length is the same.

| Historical display | Retained values or formula | Relation to a fixed measurement cylinder |
|---|---|---|
| [Cylindrical history plot](project-source/kernel_TO/geometry_3d.py:4) | \((\kappa\cos\phi,\kappa\sin\phi,Z)\), \(\phi=2\pi q_{\rm clock}/12\) | A sampled state/history curve, with no fixed \(R,H\) supplied |
| [History torus chart](project-source/kernel_TO/geometry_3d.py:25) | Major radius default 2; minor radius \(r_{\max}\kappa/(1+\kappa)\), default \(r_{\max}=1\); history-normalized minor angle | Its changing coordinates do not set the present cylinder scale |
| [Three-anchor torus chart](project-source/kernel_TO/toy_3d_triocta.py:283) | Major radius 2; \(r_j=0.6[1+0.4\log(1+|\Omega_j|)]\) | State-dependent display radii; not a fixed enclosing tube |
| [Fixed torus wireframe](project-source/kernel_TO/toy_3d_triocta.py:573) | Major radius 2, minor radius 0.6 | Highest torus ring: radius 2, height 0.6. Its **envelope cylinder** has radius 2.6, half-height 0.6 |
| [RSB halo](project-source/kernel_TO/toy_3d_triocta.py:520) | Sampled parallels with radii based on \(2.02\) and \(0.63\) | The complete carrier torus has envelope cylinder radius 2.65, half-height 0.63; the finite sampled rings need not reach its extrema |
| [Dual-tetra display](project-source/kernel_TO/dual_tetra_mapper.py:14) | Default tetrahedral scale 1.5, trajectory throat-radius normalization 1.0 | Separate display and history normalization; neither calibrates the folded width |

For the torus wireframe, \(\rho=2+0.6\cos\chi\), \(z=0.6\sin\chi\); therefore \(\max\rho=2.6\), \(\max|z|=0.6\), and the highest ring occurs at \(\chi=\pi/2\), where \(\rho=2\). This proves that its highest ring is **not** the highest ring of its envelope cylinder. The same calculation gives the halo carrier dimensions. These are display-coordinate lengths, not physical units.

No recovered source identifies their absolute display unit with the current octagon width. Even a chosen similarity cannot make the historical wireframe's envelope cylinder equal the **minimum** current cylinder in both dimensions: matching radii needs multiplier \(5/(13\sqrt3)\), whereas matching half-heights needs \(5/6\). Their aspect ratios differ. An overlay or a match of just one length would be an additional registration choice, not recovered normalization.

The historical Vesica radius \(r=0.5\) retained in Vesica Delay is likewise a planar profile convention, not an outer cylinder radius. The initializer retains \(d/r\) under TL1's nonzero-factor hypotheses; it supplies no conversion from that profile's radius to the measurement width. Improved ratio conditioning in TL2 does not change that missing scale correspondence.

## Vesica eye orientation without dynamics

**OWNER DESIGN CLARIFICATION.** The eye is a separate centered oriented construction that may eventually rotate relative to the measurement Tri-Octagon. The measurement cylinder remains fixed.

For a nondegenerate unequal-axis lens, \(0<d/r<2\), its placement needs a plane **and an in-plane centreline direction**. A unit normal alone leaves an undetermined in-plane angle. One convenient representation is an orthonormal frame

\[
Q=[a_0\ b_0\ c_0]\in SO(3),\qquad c_0=a_0\times b_0, \tag{21}
\]

with \(a_0\) the parent-centre direction and \(b_0\) the chord direction. It has three orientation degrees of freedom. The centre is already specified as \(o\); the shape ratio and absolute eye scale remain separate from orientation and from cylinder dimensions.

If only the unlabeled, unoriented geometric lens matters, the frame overrepresents it: half-turns about each frame axis preserve the set. Its generic orientation space is therefore \(SO(3)/D_2\), where \(D_2=\{I,R_{a_0}(\pi),R_{b_0}(\pi),R_{c_0}(\pi)\}\). This is a discrete identification, so there are still three continuous orientation degrees of freedom. Labeling the parent circles or choosing a directed plane normal removes some identifications; a fully marked right-handed frame retains all of \(SO(3)\).

At \(d=0\), the overlap is a disk and its in-plane orientation is unobservable: an unoriented plane normal in \(\mathbb{RP}^2\) suffices, or a directed normal in \(S^2\) if explicitly marked. At tangency \(d=2r\), the overlap alone is a point and carries no geometric orientation; the **retained parent-circle pair** would still carry directional information. These statements concern different marked objects and must not be combined.

A distinguished unit axis would suffice only for an axially symmetric object, or after adopting a restriction that supplies the missing in-plane alignment. Neither restriction is selected here. The frame (21) is a kinematic specification, not a spin axis, angular velocity, evolution equation, probability amplitude or emission pattern. The shell's existing discrete symmetry can identify equivalent registrations; it does not force a continuous rotation law.

## Verification and preservation

[The bounded external verifier](project-source/research/TL4_measurement_frame_20261006/verify_tl4.py) records **45/45 passing checks** in [TL4_RESULTS.json](project-source/research/TL4_measurement_frame_20261006/TL4_RESULTS.json). These include the 18-vertex archived scale conversion, agreement with current source coordinates, cylinder extrema, normal/seam and connector/tangent identities, reference shrink and translation relations, projection identities, and before/after preservation checks. The written interval and convexity arguments establish full-set results; the checks supplement them. The static figure was visually inspected for readable labels and correct separation of the three constructions.

The protected before/after inventory covers **16,024 files** across the authoritative repository, historical `kernel_TO`, separate `kernel_torment`, separate sibling `kernel_physics`, existing external research, and reconstruction. All path/content fingerprints match. HEAD, index fingerprint and complete short working-tree status also match. This new external lane is the only excluded output directory. Existing predecessor reports, kernels, UI, papers, fixtures, historical exports and unrelated working-tree material remain unchanged. No repository write, staging or commit occurred. No historical display, simulation or predecessor verification suite was executed; only the two pure current geometry modules were imported, with bytecode disabled.

## Final answers

1. **What is the cylinder and top ring?** The static centered measurement domain (7), with axis \(e_z\), and its highest circular rim (8). It includes the centre; no material or dynamical interpretation follows.

2. **What dimensions are correct?** For the unchanged width-one shell, radius \(1/\sqrt3\), diameter \(2/\sqrt3\), half-height \(1/2\), full height 1. The earlier side-one folded export uses radius \((1+\sqrt2)/\sqrt3\) and full height \(1+\sqrt2\); multiply its coordinates by \(\sqrt2-1\) to obtain the current values. Reference alternatives and historical displays have their separate dimensions tabulated above.

3. **Is ~0.544 recovered, and what does it measure?** No matching geometric quantity was recovered. The nearby \(0.541196\ldots\) is one octagon's circumradius. The recovered hexagon-matching factor is \(0.804738\ldots\), not ~0.544. The remembered value remains unresolved.

4. **Which three directions appear in top view?** Three outward normal/face-centre rays and three opposite seam/gap rays are exact. Tangents supply another already defined triple. Regular-hexagon vertex rays follow the tangent axes; the current alternating hexagon's endpoint rays differ.

5. **Old directions or additional axes?** The seam/gap triple is the opposite direction on the existing three normal axes. Tangent axes are different lines but are derived from the existing frame. Projection creates neither new spatial dimensions nor new independent orientation data. The owner's intended remembered triple is not uniquely identified without a marked reference.

6. **Viewpoint versus active orientation?** Top/side/eye projections erase different components of a fixed object. An active rotation changes the eye's orientation relative to the fixed scaffold while preserving its internal distances. A passive frame change changes coordinates of every object without changing relative geometry. Similar-looking images alone cannot distinguish these operations.

7. **Minimum eye orientation data?** Generically, a plane normal plus an in-plane centreline direction, conveniently an \(SO(3)\) frame modulo the geometric lens's discrete symmetries. A lone axis is insufficient for a generic lens. Shape, scale and any labels remain separate choices.

8. **What remains owner-defined?** Which eye object is retained (overlap or parent pair), its shape and scale relative to the measurement scaffold, its labels and initial frame, and which historical direction set was intended. Before any actual rotation or wave model could be studied, its independent kinematic/dynamical law and observables would also have to be specified. TL4 supplies none of those laws.

**TL4 stops at this recovery checkpoint.** The measurement cylinder is static; no spin dynamics, probability/wave law, quantum identification, dark-matter claim or gravity continuation is introduced.
