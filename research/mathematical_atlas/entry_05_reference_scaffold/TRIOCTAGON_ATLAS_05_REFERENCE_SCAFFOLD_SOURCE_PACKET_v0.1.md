# TriOctagon Mathematical Atlas — Entry 05

**Reference scaffold and alternating-hexagon geometry — source packet v0.1**  
Prepared 29 September 2026. Read-only reconstruction at current baseline `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`.

The accepted construction is a two-parameter Euclidean reference scaffold: three covariantly aligned regular octagons specify three selected edges, whose intervening connectors form an alternating equiangular hexagon. Regularity is the additional equation $g_{\mathrm{gap}}=s$. The planar octagon-centre radius is $L=p+a$; the vertical-face centre radius is $p$. These two realizations share the selected-edge horizontal coordinates, not their complete embeddings.

Paper C enters through one exact member and a specified rigid coordinate map. Its connector length is positive even though its finite vertical faces share seams. Both accepted regularization operations remove those seams. The special shrink fixes vertical centres and lowers the top plane; it does not fix planar octagon centres.

```text
PAPER_D_REFERENCE_SCAFFOLD != PAPER_C_MATERIAL_SHELL
g_gap IS A GEOMETRIC LENGTH
g_gap != recurrence coupling g
OMEGA_TO_GAP_INTERFACE = OPEN / UNSPECIFIED
```

This is an external source packet, not a revision to Paper D or a new physical model. Atlas 01–04 remain closed. Their provenance questions and correction queues were not reopened. No historical system was launched, no missing construction file was recreated, and no state-to-gap coupling was introduced.

## Authority and evidence lanes

The primary authorities are [the scaffold module](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/reference_scaffold.py), [Paper D v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md), and [its current tests](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_reference_scaffold.py). Equation/section locators below refer to that exact Paper-D file. All consulted source identities appear in the results JSON and the source register at the end of this packet.

| Lane | What it establishes | Limit |
|---|---|---|
| Independent derivation | Exact Euclidean identities, domains, convexity and counterexamples | Mathematical consequences of the explicitly stated construction |
| Current API parity | Frozen implementation matches those independently formed coordinates and contracts | Scoped scaffold tests, not recertification of the whole kernel |
| Paper-C/B interface comparison | The specified coordinate bridge and existing face-state attachment | No replacement shell and no new attachment |
| Bounded historical comparison | Only Paper-D/census sources and directly identified historical functions | A surviving display is not a recovered registration with gap cells |
| Integrity | Before/after path-and-content fingerprints and Git HEAD/status checks | File content inventory excludes `.git`; Git is inspected separately |

The manuscript cites an earlier implementation commit and earlier Paper-C records. For this packet the user-specified frozen current checkout is authoritative. Current accepted Paper-C v1.0.1 and Paper-B v0.1.2 are used only for the explicit interfaces below.

## 1. Side-normalized regular octagon

Let $s>0$ be an octagon **side length**, and write $b=s/2$. Bisecting a centre-to-side isosceles triangle gives

\[
\tan(\pi/8)=\frac{s/2}{a}=\sqrt2-1,
\qquad
a=\frac{s}{2\tan(\pi/8)}=\frac{1+\sqrt2}{2}s.
\]

The opposite-flat width and circumradius are consequently

\[
w=2a=(1+\sqrt2)s,\qquad
R_{\rm oct}=\frac{s}{2\sin(\pi/8)}
=\frac{s}{\sqrt{2-\sqrt2}}=\frac{s}{2}\sqrt{4+2\sqrt2}.
\]

In particular $R_{\rm oct}^2=a^2+b^2=(2+\sqrt2)s^2/2$. Side length, apothem, width and circumradius are four different quantities.

The current local vertex order is counterclockwise:

\[
\mathcal V_s=((a,-b),(a,b),(b,a),(-b,a),
(-a,b),(-a,-b),(-b,-a),(b,-a)).
\]

The outline is the union of the eight consecutive closed segments, including the last-to-first segment. The filled octagon is the planar convex region

\[
\mathcal O_s=\operatorname{conv}\mathcal V_s
=\{x:n_j\cdot x\le a,\ j=0,\ldots,7\},
\quad n_j=(\cos(j\pi/4),\sin(j\pi/4)).
\]

Intersecting successive support lines independently recovers the vertices above. Their consecutive differences have squared norm $s^2$: the slanted sides use $a-b=s/\sqrt2$. Rotation by $\pi/4$ carries each vertex to the next. The area is $2(1+\sqrt2)s^2$.

Atlas-03/Paper-C width one means $w_0=1$, hence $a_0=1/2$ and $s_0=\sqrt2-1$. It does **not** mean $s=1$. Paper D admits arbitrary positive $s$; the current `geometry.py` material module retains its width-one normalization. Source: Paper D §4, equations (1)–(2a); `Octagon`.

## 2. Covariant directions and the meaning of each radius

Take indices modulo three and define

\[
u_i=(\cos(2\pi i/3),\sin(2\pi i/3)),\qquad
t_i=Ju_i,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Thus

\[
(u_0,u_1,u_2)=((1,0),(-1/2,\sqrt3/2),(-1/2,-\sqrt3/2)).
\]

Each pair $(u_i,t_i)$ is positively oriented orthonormal: $u_i\cdot t_i=0$, $\det(u_i,t_i)=1$. Rotation $R_{120}$ sends both members of pair $i$ to pair $i+1$, and $\sum_i u_i=\sum_i t_i=0$.

| Object | Position/direction | Meaning |
|---|---|---|
| Radial direction | $u_i$ | Unit vector, not a centre |
| Selected-edge direction | $t_i=Ju_i$ | Unit tangent, positively traversed |
| Planar selected-edge midpoint | $p u_i$ | Radius $p$ |
| Complete planar octagon centre | $L u_i=(p+a)u_i$ | Radius $L$ |
| Vertical face centre | $(p u_i,0)$ | Horizontal and spatial centre radius $p$ |
| Vertical top-edge midpoint | $(p u_i,a)$ | Horizontal radius $p$, height $a$ |

Putting three centres on an equilateral triangle does not by itself establish these selected-edge directions. The finite frames must rotate covariantly too. The aligned tangent prescription is an explicit part of this construction. Source: Paper D §5, equations (3)–(4).

## 3. Endpoints, chain and directed connectors

With side length $s$ and midpoint radius $p$, the selected edge $E_i$, directed along $t_i$, has endpoints

\[
A_i=p u_i-\frac{s}{2}t_i,\qquad
B_i=p u_i+\frac{s}{2}t_i.
\]

The ordered chain is

\[
A_0\xrightarrow{E_0}B_0\xrightarrow{G_0}A_1
\xrightarrow{E_1}B_1\xrightarrow{G_1}A_2
\xrightarrow{E_2}B_2\xrightarrow{G_2}A_0.
\]

For $i=0$, direct subtraction yields

\[
A_1-B_0=left(-\frac{3p}{2}+\frac{\sqrt3s}{4},
\frac{\sqrt3p}{2}-\frac{s}{4}\right)
=\left(\sqrt3p-\frac{s}{2}\right)
\left(-\frac{\sqrt3}{2},\frac12\right).
\]

The final unit vector is $R_{60}t_0$. Covariance therefore proves for every $i$

\[
B_i-A_i=s t_i,\qquad
A_{i+1}-B_i=\left(\sqrt3p-\frac{s}{2}\right)R_{60}t_i.
\]

The connectors are measurement/construction segments. Completing the chain does not install material strips between faces. Source: Paper D §6, equations (5)–(8).

## 4. Positive gap domain and collapsed boundary

Define the geometric connector length by

\[
g_{\rm gap}=\sqrt3p-\frac{s}{2}>0
\quad\Longleftrightarrow\quad p>\frac{s}{2\sqrt3}.
\]

Its inverse is $p=(s+2g_{\rm gap})/(2\sqrt3)$. These are equivalent parameterizations of the accepted domain $s>0,g_{\rm gap}>0$. In subsequent metric equations **$g$ abbreviates $g_{\rm gap}$ only**; the dynamics coefficient is written $g_{\rm coupling}$.

`ReferenceScaffold(s, g_gap)` requires provably positive exact arguments. `from_radius(s,p)` requires the resulting gap to be provably positive too. Merely declaring $p$ positive does not prove this inequality. Exact symbolic input of undecidable sign is rejected rather than silently imposing an extra domain.

At the separately examined limit $g=0$, $p=s/(2\sqrt3)$ and $B_i=A_{i+1}$. The six-entry list has only three distinct points. The connectors vanish; the remaining selected edges bound an equilateral triangle of side $s$. The corner cells collapse, the area is $\sqrt3s^2/4$, and the circumradius is $s/\sqrt3$. This is not a six-positive-edge hexagon and is not accepted by the runtime constructors.

For $p<s/(2\sqrt3)$, the coefficient in the directed connector formula is negative. Its absolute value would be the Euclidean segment length, but this reverses the established directed-edge convention. No accepted-domain extension or regularity claim below the boundary is made here.

## 5. The alternating convex equiangular hexagon

In terms of $s,g>0$, the vertices $H_0,\ldots,H_5=(A_0,B_0,A_1,B_1,A_2,B_2)$ are

\[
\begin{aligned}
H_0&=(p,-s/2),&H_1&=(p,s/2),\\
H_2&=((s-g)/(2\sqrt3),(s+g)/2),&H_3&=(-(2s+g)/(2\sqrt3),g/2),\\
H_4&=(-(2s+g)/(2\sqrt3),-g/2),&H_5&=((s-g)/(2\sqrt3),-(s+g)/2).
\end{aligned}
\]

Let $d_k=H_{k+1}-H_k$. The successive unit directions are $R_{60}^k t_0$, with lengths $\ell_k=(s,g,s,g,s,g)_k$. Hence for every corner

\[
d_{k-1}\cdot d_k=\frac12\ell_{k-1}\ell_k,
\qquad \det(d_{k-1},d_k)=\frac{\sqrt3}{2}sg>0.
\]

Every exterior turn is $+\pi/3$, and every interior angle is $2\pi/3$. Closure follows by summing the consecutive differences. Global convexity is established by the bounded closed-half-plane construction in §7 below, not assumed from local turns alone: exactly these six vertices are feasible intersections of adjacent boundary lines, and all six lengths are positive.

The polygon is consequently equiangular for all admitted parameters. It is regular exactly when its alternating side lengths coincide:

\[
g=s\quad\Longleftrightarrow\quad p=p_*:=\frac{\sqrt3}{2}s.
\]

As a falsifier, $s=2,g=1$ retains the specified $C_3$ covariance and all six turns but has two distinct side lengths. Threefold symmetry is insufficient for regularity. Source: Paper D §§7–8, equations (9)–(11).

## 6. Circumcircle, area, perimeter and incircle

Orthogonality of $u_i,t_i$ immediately gives the common vertex radius

\[
R_H^2=p^2+\frac{s^2}{4}=\frac{s^2+sg+g^2}{3}.
\]

The perimeter is $3(s+g)$. The shoelace sum independently gives

\[
\mathcal A_H=\frac{\sqrt3}{4}(s^2+4sg+g^2).
\]

Selected-edge support lines have unit outward normals $u_i$ and distance $p$. Connector lines have unit normals $v_i=R_{60}u_i$ and distance

\[
q_H=v_i\cdot B_i=\frac p2+\frac{\sqrt3s}{4}
=\frac{2s+g}{2\sqrt3}.
\]

To test an incircle, let an interior centre $c$ have equal distance $r$ from the three selected-edge lines. Then $u_i\cdot c=p-r$ for all $i$. Summing gives $r=p$; since the $u_i$ span the plane, $c=0$. Tangency to the connectors now requires $p=q_H$, or

\[
p-q_H=\frac{g-s}{2\sqrt3}=0.
\]

Thus the generic alternating polygon is cyclic but has no incircle tangent to all six sides. At regularity,

\[
R_H=s,\quad r_H=p=q_H=\frac{\sqrt3s}{2},\quad
\operatorname{perimeter}=6s,\quad \mathcal A_H=\frac{3\sqrt3}{2}s^2,
\]

and $H_k=s(\cos(-\pi/6+k\pi/3),\sin(-\pi/6+k\pi/3))$. Source: Paper D §8, equations (12)–(14).

## 7. Support triangle, equilateral corner cells and closed cuts

The three selected-edge inequalities enclose the support triangle

\[
\mathcal T=\{x:u_i\cdot x\le p\ (i=0,1,2)\}.
\]

The intersection of lines $i,i+1$ is

\[
V_i=p(u_i+\sqrt3t_i).
\]

Their consecutive distances are $W=2\sqrt3p=s+2g$; thus $\mathcal T$ is equilateral. Define its three closed corner cells

\[
K_i=\operatorname{conv}(B_i,V_i,A_{i+1}).
\]

Every side of every $K_i$ has length $g$; the cells are equilateral for **all** $s,g>0$, not only at regularity. Each lies within distance $g$ along the two sides adjacent to its support-triangle vertex. Because $2g<W$, the cells cannot meet: the barycentric weight of their respective apex is at least $1-g/W>1/2$, and two distinct apex weights cannot both exceed $1/2$.

The retained closed hexagon is exactly

\[
\mathcal H=\{x:u_i\cdot x\le p,\ v_i\cdot x\le q_H,
\ i=0,1,2\}.
\]

This is an intersection of six closed half-planes. It is convex, bounded by $\mathcal T$, and contains the origin strictly. Checking all pairwise boundary-line intersections gives only $A_i,B_i$ as feasible vertices. Each has exactly its two adjacent inequalities active. This also proves the global convexity used in §5 without circular reliance on a drawing.

Boundary treatment matters. The actual removal is

\[
\mathcal H=\mathcal T\setminus
\bigcup_i\bigl(\mathcal T\cap\{x:v_i\cdot x>q_H\}\bigr).
\]

The connector base $B_iA_{i+1}$ remains, including endpoints. The apex $V_i$ and the outer leg portions beyond those endpoints are removed. Indeed

\[
q_H-v_i\cdot V_i=-\frac{\sqrt3g}{2}<0,
\quad q_H-v_i\cdot[(1-t)B_i+tV_i]=-t\frac{\sqrt3g}{2}<0
\quad(0<t\le1),
\]

and the same formula holds on the other leg. Removing only each cell's ordinary planar interior would incorrectly leave its apex and outer legs; removing the entire closed cell would incorrectly remove the connector base. The half-plane definition is the precise accepted operation.

An independent area derivation follows:

\[
\mathcal A_H=\frac{\sqrt3}{4}W^2-3\frac{\sqrt3}{4}g^2
=\frac{\sqrt3}{4}(s^2+4sg+g^2).
\]

At regularity $W=3s$, and the triangle consists of the central regular hexagon plus three side-$s$ equilateral corner cells, with their shared boundaries accounted for as above. Source: Paper D §9, equations (15)–(16b).

## 8. What the exact representation classes mean

| Current object | Mathematical meaning | Executable scope |
|---|---|---|
| `ConvexHull(vertices)` | The convex hull of supplied exact generators in two or three dimensions | Stores a frozen tuple; validates count and dimensions, not a hull algorithm |
| `HalfPlane(normal, offset)` | Closed set $n\cdot x\le b$; slack $b-n\cdot x$ | Nonzero exact normal; normalization to unit length is not required |
| `HalfPlaneIntersection(halfplanes)` | Intersection of the supplied closed inequalities | `contains` returns true, false, or undecidable `None` |
| `Octagon.outline`, `ReferenceScaffold.outline` | Cyclic ordered line segments | Boundary representation, not filled area |
| `Octagon.filled`, support triangle, corner cells | Supplied convex regions | Generated vertices here are correctly ordered and nondegenerate |
| `filled_hexagon` | All six closed support constraints | Preserves connector boundary while excluding corner apexes |
| `planar_frames`, `vertical_frames` | Convex regions in their respective affine planes | Reference figures; no mesh welding or solid Boolean operation |

`ConvexHull` does not compute extreme vertices, test noncollinearity, or insist that arbitrary 3D generators be coplanar. Three collinear supplied points are accepted, and it has no `contains` method. These limitations do not affect the independently proven octagons and triangles generated here, but prevent interpreting the class name as a general geometric solver.

For membership, one provably negative slack gives false; all provably nonnegative slacks give true; otherwise the result is `None`. Boundary slack zero is included. A non-unit normal scales the slack, so only with the unit normals used above is the offset an origin-to-line distance.

The exact scalar boundary accepts integers, fractions and provably real finite SymPy expressions. Booleans, floating inputs (including embedded `Float`), strings, non-real/infinite data and undecidable positive lengths are rejected. Frozen records prevent assignment after creation. Composite positive expressions such as $1/(1+\sqrt{x})$, $x>0$, remain finite when specialized at $x=1$; the tests exercise substitution before later simplification. These are implementation contracts, separated from the Euclidean proofs.

## 9. Symmetry of the polygon, roles, traversal and complete frames

Here $D_n$ denotes the dihedral group of order $2n$. Rotation $R_{120}$ acts on vertex indices by $k\mapsto k+2$; reflection across the $x$-axis acts by $k\mapsto1-k$, modulo six. Both preserve the selected-edge/connector classes.

| Object | $s\ne g$, positive | $s=g$ |
|---|---|---|
| Unmarked six-point polygon | $D_3$, order 6 | $D_6$, order 12 |
| Polygon preserving edge/connector roles | $D_3$ | $D_3$ |
| Role-preserving symmetry also preserving cyclic traversal orientation | $C_3$ | $C_3$ |
| Three complete planar octagon frames retained as constituents | $D_3$ | $D_3$ |

Why the generic upper bound? Any polygon isometry induces an automorphism of its six-cycle. Unequal alternating side lengths forbid the three odd cyclic shifts and the three role-exchanging reflections. Exactly the six indicated actions remain. At regularity all twelve cycle symmetries are realized, but a 60° rotation sends selected edges to connectors. Restoring the roles therefore removes the extra symmetries. Reflections reverse traversal; the remaining positively traversed role-preserving subgroup is the three rotations. Here roles label the two classes, not three individually fixed face identities.

For the complete planar frames, their three distinct centres form an equilateral triangle. A constituent-preserving isometry must permute those centres, so it has at most six possibilities. All six are realized by the frame construction; its full symmetry is $D_3$, even when the derived hexagon is regular. A 60° rotation fails already on the centre set.

The vertical realization needs its own ambient qualifier. Its horizontal/top measurement structure has the same $D_3$ role symmetry. If one forgets the distinguished top and retains only three complete unoriented vertical octagons in 3D, reflection $z\mapsto-z$ also preserves them. It commutes with the six horizontal actions, giving twelve symmetries ($D_3\times C_2$, often denoted $D_{3h}$). The centre plane and its triangle give an upper bound of $6\times2$. This is a direct geometric consequence of that differently marked 3D object, not the role-marked D03 symmetry record or an extra 60° horizontal rotation. Source for the accepted planar hierarchy: Paper D §10; the script separately checks the vertical horizontal-plane reflection.

## 10. Complete planar octagons and $L=p+a$

Place the centre of frame $i$ at $C_i=L u_i$, $L=p+a$, and map local coordinates by

\[
\Phi_i(x,y)=(L+x)u_i+y t_i,\qquad (x,y)\in\mathcal O_s.
\]

The matrix with columns $(u_i,t_i)$ is orthogonal with determinant one, so the full image is a regular side-$s$ octagon with eight corresponding edges. Its inward local side $x=-a,\ -s/2\le y\le s/2$ maps to $p u_i+y t_i$, exactly the selected edge.

There is an orientation distinction: the local counterclockwise octagon outline goes from vertex 4, $(-a,b)$, to vertex 5, $(-a,-b)$, so this side is traversed $B_i\to A_i$. The central measurement polygon instead traverses it $A_i\to B_i$. The undirected edge is identical; the two adjacent planar regions lie on opposite sides.

At regularity the complete planar centre radius is $L_*=(\sqrt3+1+\sqrt2)s/2$, whereas the selected-edge midpoint radius is only $p_*=\sqrt3s/2$. Substituting $L$ for $p$ in the gap formula would add a spurious term $\sqrt3a$. Source: Paper D §11, equations (17)–(18).

## 11. Separate vertical-frame realization

The same local filled octagon can instead be embedded as

\[
F_i(\xi,z)=(p u_i+\xi t_i,z),\qquad (\xi,z)\in\mathcal O_s.
\]

Its centre is $(p u_i,0)$ and its unit normal is $(u_i,0)$, since $(t_i,0)\times e_z=(u_i,0)$. The local map is an isometry. The full eight-vertex outline and filled face lie in the vertical plane $u_i\cdot(x,y)=p$.

The selected top edge is $z=a$, $-s/2\le\xi\le s/2$. Its endpoints are $(A_i,a)$ and $(B_i,a)$, so projecting horizontally recovers exactly the planar measurement hexagon. Its full three-dimensional midpoint has distance $\sqrt{p^2+a^2}$ from the origin; $p$ denotes its horizontal radius, not that spatial distance.

The counterclockwise local octagon order traverses its top edge from $(b,a)$ to $(-b,a)$, again $B_i\to A_i$. The selected measurement traversal goes the other way. Planar and vertical complete frames have different centres and different ambient planes; only the stated local octagon and selected horizontal data are shared. No material attachment follows merely from constructing these reference faces. Source: Paper D §12, equation (19).

## 12. Exact Paper-C member

Adjacent vertical supporting planes meet where their respective tangent coordinates are $\xi=+\sqrt3p$ and $\xi'=-\sqrt3p$. The local octagon's right/left full side edges lie at $\xi=\pm a$ with $-s/2\le z\le s/2$. Therefore full side coincidence occurs at

\[
p_0=\frac a{\sqrt3}=\frac{1+\sqrt2}{2\sqrt3}s.
\]

Substituting into the connector formula gives

\[
g_0=\sqrt3p_0-\frac s2=a-\frac s2=\frac s{\sqrt2},
\qquad \frac{g_0}{s}=\frac1{\sqrt2}\ne1.
\]

This is precisely `paper_c_member(s)`. It is an alternating, nonregular hexagon for every positive side length. At width one,

\[
s_0=\sqrt2-1,\quad a_0=\frac12,\quad
p_0=\frac1{2\sqrt3},\quad g_0=\frac{\sqrt2-1}{\sqrt2}.
\]

The comparison concerns three related objects: the actual Paper-C welded material faces; their six top-edge endpoints joined as a measurement polygon; and the Paper-D vertical aligned family at $p=p_0$. Their coordinate equivalence is specified next. The measurement polygon is not one of the material annulus's nonplanar nine-edge rims, and its connectors are not extra mesh edges. Source: Paper D §12, equations (20)–(22); current `paper_c_member`.

## 13. Rigid map and face-label permutation

The accepted affine map, for exact finite real $(x,y,z)$ and $s>0$, is

\[
M_s(x,y,z)=\left(\frac{\sqrt3}{2}x-\frac12y,
\frac12x+\frac{\sqrt3}{2}y+\frac a{\sqrt3},z\right).
\]

It is a rotation by $\pi/6$ about the vertical axis followed by translation $(0,a/\sqrt3,0)$. The linear part satisfies $R^TR=I$ and $\det R=1$, so it preserves all finite-face distances, incidence and orientations. It changes coordinates, not $s$ or $p$.

To verify the entire finite-face equivalence, use the side-$s$ scaled Paper-C parameterizations

\[
\begin{aligned}
P_1(\xi,z)&=(-a/2-\xi/2,\sqrt3a/2-\sqrt3\xi/2,z),\\
P_2(\xi,z)&=(\xi,0,z),\\
P_3(\xi,z)&=(a/2-\xi/2,\sqrt3a/2+\sqrt3\xi/2,z),
\end{aligned}
\]

each on the same domain $\mathcal O_s$. Substitution gives

\[
M_s F_0=P_3,\qquad M_s F_1=P_1,\qquad M_s F_2=P_2
\quad\text{when }p=p_0.
\]

Thus D-frame indices $(0,1,2)$ correspond to C labels $(P_3,P_1,P_2)$, or zero-based C face indices $(2,0,1)$. Because these identities hold for arbitrary local coordinates on the same filled domain, they prove full face, outline and vertex-set equivalence, not merely equality of supporting planes. The local vertex lists differ only by a cyclic starting point. API checks additionally compare every mapped width-one vertex set and undirected edge set against the actual frozen `folded_module()` faces.

For arbitrary $s$, this is the uniformly scaled Paper-C family. Only $s=s_0=\sqrt2-1$ gives the actual width-one `geometry.py` object without a scale change. Although `paper_c_rigid_map` accepts any exact point, the finite-face comparison theorem requires the starting scaffold $p=p_0$ with matching local side length. Applying the same rigid map to a regular scaffold does not turn it into the welded Paper-C member. Source: Paper D §12, equation (21); current map and geometry code.

## 14. Fixed-size outward radial translation

Keep $s$, $a$, orientations and all local coordinates fixed while moving from $p_0$ to $p_*=\sqrt3s/2$. Then

\[
\Delta p=p_*-p_0=\frac{2-\sqrt2}{2\sqrt3}s>0,
\qquad F_i^{\rm new}(\xi,z)-F_i^{\rm old}(\xi,z)=(\Delta p\,u_i,0).
\]

The three displacement vectors are different and sum to zero. Their centre triangle grows, so this is not one common translation or a single rigid motion of the assembly. Each constituent frame individually undergoes a rigid translation. The corresponding planar centre radius also increases by $\Delta p$ because $a$ stays fixed.

Selected edges retain length $s$, connectors increase from $s/\sqrt2$ to $s$, and the top height stays $a$ (width-one height $1/2$). Full side seams disappear: the planes still intersect, but the finite octagons stop short of their intersection lines. `translate_paper_c_to_regular(s)` returns the new regular scaffold without mutating any Paper-C object. Source: Paper D §13.1, equation (23).

## 15. Fixed-centre shrink: precise reconstruction and terminology

Start specifically from $p_0=a/\sqrt3$. Fix each **vertical face centre** $(p_0u_i,0)$ and scale both local coordinates:

\[
F_i^{\rm shrink}(\xi,z)=(p_0u_i+\lambda\xi t_i,\lambda z),
\qquad s'=\lambda s,\quad a'=\lambda a.
\]

Regularity requires the newly computed connector length to equal the new selected side:

\[
\sqrt3p_0-\frac{\lambda s}{2}=\lambda s
\quad\Longrightarrow\quad
\lambda=\frac{2a}{3s}=\frac{1+\sqrt2}{3}\in(0,1).
\]

The width-one substitution is exact:

\[
s'=g'=\frac{(1+\sqrt2)(\sqrt2-1)}{3}=\frac13,
\quad p'=\frac1{2\sqrt3},\quad
a'=\frac{1+\sqrt2}{6},\quad w'=\frac{1+\sqrt2}{3}.
\]

The resulting regular hexagon has $W'=1$, $R_H'=1/3$, incircle radius $\sqrt3/6$, perimeter $2$, and area $\sqrt3/6$. Its top height has decreased from $1/2$ to $(1+\sqrt2)/6$.

| Quantity or wording | Actual behavior under this operation |
|---|---|
| Fixed-centre | The three vertical centres $(p_0u_i,0)$ stay fixed |
| Fixed selected-edge midpoint radius $p$ | The three horizontal projections of top-edge midpoints stay at $p_0u_i$ |
| Three-dimensional top midpoint | Moves vertically from height $a$ to $\lambda a$ |
| Top endpoints | Move tangentially and vertically; not fixed |
| Planar centre radius $L=p+a$ | Changes to $L'=p_0+\lambda a$ |
| Planar complete-frame centres | Move inward by $(1-\lambda)a u_i$ in the associated planar realization |
| Entire construction | Not a global similarity: the centre triangle remains fixed while individual faces shrink |

Shrinking about the original **planar** centres $L_0u_i=(p_0+a)u_i$ is a different operation. Its inward-edge midpoint radius becomes

\[
p_{\rm planar}'=L_0-\lambda a=p_0+(1-\lambda)a.
\]

At the special factor above, its gap-minus-side residual is

\[
\sqrt3p_{\rm planar}'-\frac{\lambda s}{2}-\lambda s
=\sqrt3(1-\lambda)a>0.
\]

It therefore does not produce the claimed regular member. This exact falsifier prevents treating the two meanings of “centre” interchangeably.

Nor is the special factor universal. For an arbitrary initial fixed radius $p$, regularity would instead require $\lambda(p)=2\sqrt3p/(3s)$. It may even exceed one. Starting at an already regular $p=p_*$ requires factor one, whereas applying $(1+\sqrt2)/3$ breaks regularity. This diagnostic formula does not add an API operation or generalize the current named shrink constructor.

A common global scale change $(p,s)\mapsto(cp,cs)$ gives $g\mapsto cg$ and preserves $g/s$; it cannot tune a nonregular member into a regular one.

**Source-wording reconciliation.** Paper D §§11–13 and the current `ReferenceScaffold`/shrink docstrings agree: $p$ is the selected-edge and vertical-centre radius; $L$ is the planar-centre radius; both $\xi$ and $z$ scale during shrink. The earlier `research_notes/reference_scaffold/note_source.json` uses compact local-variable notation and sometimes short geometric `g`; these do not identify it with the recurrence coefficient. Its §7 statement that no scaffold placement or fixed-centre shrink option exists records an earlier implementation state. The frozen current module now exposes those explicit constructors; `geometry.py` still supplies its original material realization. This is a dated implementation-status distinction, recorded without editing any document or reopening a correction queue. Source: Paper D §13.2–§14.1, equations (24)–(27), and current shrink docstring.

## 16. Finite-face separation and its exact domain

For adjacent **finite filled vertical octagons**, define the signed expression

\[
\delta_{\rm face}=\sqrt3p-a=g-\frac{s}{\sqrt2}.
\]

It is the actual minimum Euclidean separation when $p\ge p_0=a/\sqrt3$ (equivalently $g\ge s/\sqrt2$); it is positive for $p>p_0$. It is not the distance between the infinite supporting planes, which intersect, and it is not the top connector length.

An explicit lower-bound-and-attainment proof fixes the domain. For any points on adjacent faces, write their tangent coordinates as $\xi=a-X$ and $\xi'=-a+Y$, with $X,Y\ge0$, and let their heights be $z,z'$. When $p=(a+\delta)/\sqrt3$ and $\delta\ge0$, direct expansion gives

\[
\|F_i(a-X,z)-F_{i+1}(-a+Y,z')\|^2
=\delta^2+\delta(X+Y)+(X-Y)^2+XY+(z-z')^2
\ge\delta^2.
\]

Equality is achieved by $X=Y=0$ and any common height in $[-s/2,s/2]$. These are actual points on the full vertical side edges, so the bound is sharp. By cyclic symmetry it applies to all three face pairs.

At $p=p_0$, those sides coincide as full seams and the minimum is zero, although $g=s/\sqrt2>0$. At any regular member with side $s$,

\[
\delta_{\rm regular}=\frac{2-\sqrt2}{2}s>0.
\]

For the width-one fixed-centre shrink, measured with its new apothem, the separation is

\[
\sqrt3p_0-a'=a_0-a'=\frac{2-\sqrt2}{6}>0.
\]

There is a meaningful domain caution within the allowed scaffold family: $0<g<s/\sqrt2$ gives a negative signed expression, not a negative distance. In this range the plane-intersection points at $\xi=\pm\sqrt3p,z=0$ lie inside both finite octagons, because $\sqrt3p<a$. The actual distance is zero. For example $g=s/2$ is an exact admitted scaffold with this property. The separation proposition is therefore used with its stated $p\ge p_0$ qualifier, rather than extrapolating a negative formula. This follows directly from the accepted coordinates; it does not assert that the intersecting family is an embedded material shell.

At the original member, welding coincident octagon edges gives 18 vertices, 21 edges and 3 faces, with three seams and the accepted annular topology. After either regularization, only three disjoint octagonal disks remain: 24 vertices, 24 edges, 3 faces, no seams, and three eight-edge boundaries. The original has two nine-edge boundaries. The independent script recounts vertices, edges and seams from the finite exact coordinates; the annulus and boundary descriptions are retained from accepted Paper C/Paper D, not reclassified by a new topology engine. Source: Paper D §14.2, equations (28)–(29).

## 17. Paper-C/Paper-D dictionary and accepted bridges

| Topic | Paper C | Paper D | Exact bridge or boundary |
|---|---|---|---|
| Basic object | One specified welded annular material realization | Three octagon reference frames and derived planar regions | Different mathematical objects |
| Local octagon | Width-one finite regular octagon | Arbitrary side-$s$ regular octagon | Same shape; equality of size requires $s=\sqrt2-1$ |
| Global coordinates | Fixed accepted folded placement | Planar frames or separate vertical family | $M_s$ maps the vertical $p=p_0$ member to scaled C faces |
| Face labels | $P_1,P_2,P_3$ | Frames $0,1,2$ | Permutation $(0,1,2)\mapsto(P_3,P_1,P_2)$ |
| Normals and tangent frames | Accepted oriented face normals/tangents | $(u_i,0)$ and $(t_i,e_z)$ | Rotate by $\pi/6$ and apply the same permutation at the matching member |
| Top six endpoints | Measurement data on the material faces | Vertices of an alternating hexagon at height $a$ | Rigid equality at $p=p_0$; $g/s=1/\sqrt2$ |
| Material outline | Two nonplanar nine-edge boundary cycles | Frame outlines plus a planar six-segment measurement outline | The measurement chain is not a material rim |
| Mesh incidence | Welded vertex/edge/face data and seams | Independent convex reference sets | At $p_0$, reference faces coincide on the C seams; constructors do not perform welding |
| Support triangle and corner cells | Not faces of the accepted annular mesh | Explicit closed planar reference regions | They may be constructed from the measurement data; no automatic material filling |
| Continuous parameters | Fixed normalized material definition | Positive $s,g$ (or admissible $s,p$) | Choosing another D member changes the reference placement |
| Regularization | No replacement definition is made | Two explicit operations make $g=s$ | Both lose the original finite-face seams |
| Face-state attachment | Paper B/current `face_state.py` attach state to the accepted C tangent frames | No gap-cell state input or transport law | An isometric coordinate bridge is not an implemented new attachment |

The dictionary preserves both facts: there is an exact finite-face bridge at a specified member, and `PAPER_D_REFERENCE_SCAFFOLD != PAPER_C_MATERIAL_SHELL`. No changes to `FoldedModule`, its topology, or its transport definitions follow from this atlas entry.

## 18. State interface, record semantics and the two different g symbols

The scaffold module constructs geometry from exact length parameters. Its direct imports are `dataclasses`, `fractions` and `sympy`. The inspected constructors, point maps and region methods take no $\Omega$, `FaceState`, chirality, trajectory, recurrence clock or energy input. An isolated process constructing vertical frames from this module imports none of `geometry`, `dynamics`, `face_state` or `readouts` as a side effect. Static inspection of those current interface modules supplies no scaffold-to-gap attachment.

Paper D §16.5 explicitly retains the existing C-face tangent representation

\[
D(\Omega)_i=(\Re\Omega_i)\tau_i+(\Im\Omega_i)e_z.
\]

Its domain, inverse/projector qualifications and evolution semantics belong to the accepted Paper-B/C interface. A possible geometric rotation/permutation of tangent frames does not automatically define a map into a support triangle, a corner cell or a connector length. No such accepted direct map is present in the inspected scaffold contract. The bounded conclusion is **OPEN / UNSPECIFIED**, not a claim that no conceivable future map exists.

| Property | $g_{\rm gap}$ | $g_{\rm coupling}$ |
|---|---|---|
| Mathematical role | Connector length $\sqrt3p-s/2$ | Coefficient of a state-valued recurrence increment, including the $L_3\Omega$ coupling term |
| Units supplied by current geometry record | `mathematical_length` | No geometric length calibration or SI length assignment |
| Domain | Exact, provably positive in the accepted scaffold API | Real recurrence parameter; zero coupling is admitted |
| Response to geometric similarity | Becomes $c g_{\rm gap}$ when lengths scale by $c$ | No implied change from scaling a separate geometry object |
| Implementation owner | `ReferenceScaffold.g_gap` | `DynamicsConfig.g` |
| Connection between the two | No accepted equation, coercion or update path | No accepted gap-conditioned rule |

The check suite explicitly contrasts rejection of `ReferenceScaffold(1,0)` with acceptance of a zero-coupling dynamics configuration, and tests linear scaling of geometric gap length. These implementation witnesses support the distinct contracts; they do not claim that unequal domains alone prove every possible semantic distinction. The defining formulas, parameter ownership, record units and absence of an attachment provide the substantive evidence.

The D03 geometry-record factory in `_geometry_records.py` makes the distinction public. It records:

- resolved parameters `s`, `g_gap`, `p`, `L`, separately from requested expressions;
- an octagon `closed_polygon`, scaffold `closed_halfplane_region`, support/corner `closed_hull` objects, and separate `closed_reference_frame` objects;
- three selected inequalities and three connector inequalities, all relation `le`;
- role-preserving `D3`, traversal-preserving `C3`, and regular unlabelled `D6` only when regularity is established;
- frame units `mathematical_length`, `coupling: "none"`, and provenance stating no dynamic attachment.

These record statements were inspected directly; the API checks in the companion script concern the exact scaffold objects themselves. No record field is interpreted as a field equation, force, conserved energy or material solid. Paper D's discussion of a pre-synchronization potential is a separate state-space result, not a geometric gap-energy identification.

## 19. Bounded historical comparison ledger

This lane uses only Paper D's own referenced history, the existing [old/new archaeology census](C:/Users/Notandi/.codex/reports/TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md), and the specifically identified old code functions below. Older PDF statements are carried through Paper D/census rather than represented as a fresh PDF audit. No new corpus search or historical repair was performed. Printed dates identify documentary claims, not discovery priority; dates are left unspecified for code where not established by this bounded inspection.

| Source / locator | Claim actually supported | Classification | Relation to this scaffold |
|---|---|---|---|
| Current Paper D §§4–14 and `reference_scaffold.py` | Aligned endpoints, positive connectors, exact hexagon/triangle/cell and tuning formulas | EXACT_CURRENT_MATH | The construction re-derived in §§1–16 |
| Author clarification, 23 September 2026, as preserved in Paper D §§2–3 | Octagons intended as reference generators; selected edges/connectors clarify the proposed geometry | AUTHOR_RECOLLECTION | Design testimony precedes the current formalization; the modern gap equation is not backdated to 2025 |
| Adopted Z/torus relay, Paper D §16.1 | Tentative association with an old Z-vector or torus scene | AUTHOR_RECOLLECTION | Adopted assisted wording is not independent verification of the remembered mechanism |
| `kernel_TO/geometry_3d.py::history_Zvec_to_xyz`; `toy_3d_triocta.py::_get_Z_scaled` | Stored Z components become a plotted curve with a whole-history scale | HISTORICAL_PRECURSOR | A real surviving display pathway; no endpoint/corner-cell input in the inspected functions |
| Same Z display and the present corner cells | A specific spatial registration, frame transform or call chain between them | OPEN | Required coordinate witness is absent from the bounded record |
| `geometry_3d.py::history_to_torus_xyz` | Norm, mod-12 clock and scalar history determine a torus curve | HISTORICAL_PRECURSOR | A distinct display map, not a triangular-cell map |
| `toy_3d_triocta.py::embed_on_torus` | Three channels use fixed azimuths and their own phases/amplitudes | HISTORICAL_PRECURSOR | Concrete channel display; different inputs from the clock/scalar torus |
| Threefold channel/torus appearance compared with three reference frames | Both can exhibit threefold organization | STRUCTURAL_ANALOGY | Shared count/symmetry is insufficient to identify coordinates or dynamics |
| H1, printed 29 October 2025, as cited in Paper D §3 and Appendix C | Earlier folding and tetrahedral-aperture/E6 language existed | HISTORICAL_PRECURSOR | Does not supply the later finite Paper-C coordinates or current gap map |
| H2, printed 24 November 2025, p.2, as cited in Paper D §3 | Three translated octagons at one global orientation and a tilt direction | HISTORICAL_PRECURSOR | Centre placement does not supply covariant edge alignment; axis direction does not supply hinge location |
| H2 pp.20–22, H3 p.26, and surviving `dual_tetra_mapper.py` | Opposite tetrahedra and a body-diagonal central projection/display are documented | HISTORICAL_PRECURSOR | A separately scaled central-core construction |
| Two regular central tetrahedral hexagons versus the regular scaffold hexagon, Paper D §17.1 | Abstract similarities can relate regular hexagons | STRUCTURAL_ANALOGY | No distinguished scale $t(s)$ or model registration is thereby recovered |
| Tetrahedral aperture as the actual scaffold gap region | A specified domain, scale, orientation and incidence-preserving identification | OPEN | Projection/intersection order must be fixed; no accepted identification supplied |
| E8/E6 organizational wording, Paper D §§17.2–18 | A possible correspondence needs a specified carrier, action and map | OPEN | Current Euclidean scaffold is complete without that correspondence |
| Missing `tri.py`, `center2.py`, `center3.py`, Blender construction, Paper D §3 | Earlier targeted work did not locate these original construction files | OPEN | No reconstruction here is labelled recovered; no absolute claim of global nonexistence |

The directly read surviving display formulas sharpen those classifications:

1. `history_Zvec_to_xyz` uses stored `Z_total` (with legacy `Z_vec` fallback). The viewer's `_get_Z_scaled` uses the 99th percentile of finite norms above $10^{-12}$, fallback denominator one, and multiplier $0.85\times0.6$. This normalizes a displayed history; it does not update the triad or use $s,p,g$.
2. The clock/scalar torus uses $r=r_{\max}\kappa/(1+\kappa)$, $\varphi=2\pi q/12$ and $\chi=(\pi/2)z/(\max_{\rm history}|z|+10^{-9})$, then $((R+r\cos\chi)\cos\varphi,(R+r\cos\chi)\sin\varphi,r\sin\chi)$. The whole-history denominator is a display operation, not a causal autonomous gap state.
3. The channel torus instead takes azimuth $2\pi j/3$, minor angle $\arg\Omega_j$, and tube radius $0.6(1+0.4\log(1+|\Omega_j|))$. It does not use the scalar history or clock of item 2.

These are source-supported maps to displays. Their use as evidence for gap geometry stops at the missing registration. Paper D also distinguishes genuinely stateful historical portal, RSB and field mechanisms; no claim that all historical mechanisms are passive is made here, and those separate systems are not re-audited or restored.

For tetrahedral terminology, retain the exact distinction already printed in Paper D §17.1. With $T_-=-T_+$, scale $t>0$, and orthogonal projection $P$ perpendicular to $(1,1,1)$, the intersection $P(T_+)\cap P(T_-)$ has regular-hexagon side $2\sqrt2t/3$. The projection $P(T_+\cap T_-)$ has side $\sqrt{2/3}\,t$, rotated by 30°; its side ratio to the first is $\sqrt3/2$. These are two different operations. This packet cites the accepted comparison without rerunning its earlier proof suite or supplying an invented $t$-to-$s$ relation.

For E8/E6, the boundary is equally limited. Paper D retains the need for an explicit E6 carrier/action and an exact certificate for the particular 60-ray base claim, distinct from an isometry/conjugacy statement about complete root sets. None becomes a scaffold map through shared threefold or sixfold appearance. This packet adds no root search, projection campaign or retrospective repair.

## 20. Independent exact checks, API parity and falsifiers

The companion [Python checks](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_05_EXACT_CHECKS.py) first derive octagon vertices by intersecting eight support lines, and scaffold endpoints by independently intersecting selected and connector lines. The Euclidean reference lane runs before importing `reference_scaffold`. No API-generated coordinates are used as its expected answers.

The script then checks all six edges, turns, inequalities and feasible line intersections; derives area by shoelace and by triangle subtraction; solves the three-support incircle equations; enumerates regular dihedral actions and role/traversal restrictions; verifies arbitrary-local-coordinate face identities; solves the shrink condition; proves finite-face distance identities; and counts exact vertex/edge coincidences. The $g=0$ limit is explicitly separated from positive-domain runtime tests.

Only after forming those reference results does it compare the current API's vertices, frames, half-planes, metrics, named operations and Paper-C finite-face edge sets. Strict exact inputs, positivity, unknown membership/regularity, immutability and symbolic specialization are distinct contract checks. Source hashes and tree-integrity predicates form further groups. These are executable symbolic checks and finite witnesses accompanying the proofs in this packet, not a claim that passing assertions alone constitute every proof.

| Falsifier | Exact witness or argument |
|---|---|
| $C_3$ does not imply regularity | $s=2,g=1$ has $C_3$ but unequal adjacent lengths and no 60° invariance |
| Regular unmarked $D_6$ does not preserve roles | Rotation by 60° sends every selected edge to a connector |
| Paper-C member is not regular | $g_0/s=1/\sqrt2$ |
| Positive gap is not positive finite-face separation | At the C member, $g_0>0$ but $\delta=0$; at $g=s/2$, faces intersect |
| Reference frames need not be connected | Both regularizations produce three disjoint finite octagonal disks |
| Radial tuning is not common rigid translation | Displacements $\Delta p u_i$ differ and centre distances increase |
| Special shrink factor is not universal | Already regular $p=p_*$ requires factor one, not $(1+\sqrt2)/3$ |
| Fixed planar and vertical centres are different | Fixed planar centres leave positive gap-minus-side residual $\sqrt3(1-\lambda)a$ |
| Geometry gap is not recurrence coupling | Definitions, record units, independent owners, zero-domain and scaling witnesses differ |
| Reference geometry does not automatically attach state | Explicit module inputs/import isolation and Paper-D open-interface statement |

The isolated record of exact formulas, source hashes, all predicate results and full integrity comparisons is [the JSON results](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_05_EXACT_RESULTS.json). It preserves symbolic values rather than silently converting them to floating coordinates.

Reproduce in the requested environment, writing only to an external destination:

```powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_05_EXACT_CHECKS.py --output C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_05_EXACT_RESULTS_rerun.json
```

The completed run below used the `torment` environment interpreter directly. The optional `--integrity-dir` reads the captured before/after evidence; it does not silently capture a new “before” inventory after the work. Without that argument, the mathematical/API/source checks run and tree integrity is explicitly `NOT_ATTACHED`.

## Verification record and integrity closeout

Final exact-check run: **68/68 passed; zero failed**. Timestamp: `2026-09-29T07:21:04.904006+00:00`. Interpreter: `C:\Users\Notandi\miniconda3\envs\torment\python.exe`; Python `3.11.15`, SymPy `1.14.0`.

| Check group | Passed | Total |
|---|---:|---:|
| API_CONTRACT | 5 | 5 |
| API_EXACT | 9 | 9 |
| EXACT_FALSIFIER | 8 | 8 |
| EXACT_GEOMETRY | 34 | 34 |
| EXACT_LIMIT | 1 | 1 |
| INTERFACE_BOUNDARY | 4 | 4 |
| SOURCE_INTEGRITY | 1 | 1 |
| TREE_INTEGRITY | 6 | 6 |

The separate current-source test run completed with **39 tests and 37 subtests passed** in 64.83 seconds. It used the same `torment` interpreter with `-B -X utf8 -m pytest -q -p no:cacheprovider kernel_physics/tests/test_reference_scaffold.py`, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, and the authoritative repo as working directory. Cache and bytecode writing were disabled. This is a fresh scaffold-only run, not the historical 95-test checkpoint mentioned in Paper D.

All reported checks are exact symbolic/finite predicates. An initial external checker comparison of two algebraically equal incircle-radius expressions used structural equality and was corrected to symbolic equality; no scientific source or expected geometric value was changed. The final pass uses that repaired comparison.

The inventories cover every enumerated file, including ignored and untracked files, under each named tree except `.git`. Each file is read in 1 MiB chunks and SHA-256 hashed. The tree digest is SHA-256 of the UTF-8 JSON mapping from relative POSIX paths to file hashes, with sorted keys and compact separators. Additions, removals and byte changes are compared explicitly. This fingerprints paths and contents, not filesystem timestamps or permissions. Git HEAD and tracked status are checked separately with `--no-optional-locks`; the clean-status claim is limited to tracked status.

| Scope | Files before / after | Identical before and after SHA-256 | Changed paths |
|---|---:|---|---:|
| current | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | 0 |
| old | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | 0 |
| torment_kernel | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | 0 |
| torment_checkout | 173908 / 173908 | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | 0 |

| Scope | Protected root | Before interval (UTC) | After interval (UTC) |
|---|---|---|---|
| current | `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics` | 2026-09-29T06:55:02.117499+00:00 to 2026-09-29T06:55:06.515711+00:00 | 2026-09-29T07:14:22.137855+00:00 to 2026-09-29T07:14:26.516625+00:00 |
| old | `C:\TORMENT\TRIOCTAGON_new\kernel_TO` | 2026-09-29T06:55:06.528824+00:00 to 2026-09-29T06:55:06.815215+00:00 | 2026-09-29T07:14:26.516625+00:00 to 2026-09-29T07:14:26.802586+00:00 |
| torment_kernel | `C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric\torment_service\kernel` | 2026-09-29T06:55:06.819218+00:00 to 2026-09-29T06:55:06.848306+00:00 | 2026-09-29T07:14:26.802586+00:00 to 2026-09-29T07:14:26.831403+00:00 |
| torment_checkout | `C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric` | 2026-09-29T06:55:06.851303+00:00 to 2026-09-29T06:57:15.677536+00:00 | 2026-09-29T07:14:26.831403+00:00 to 2026-09-29T07:16:42.976695+00:00 |

The copied production kernel is separately fingerprinted as a nested scope; its files are also included in the full production checkout inventory. The current HEAD is the requested frozen baseline. Production HEAD remained `a06edcc5c9df5d3b56405085d9f2942b768dc203`. Both recorded tracked-status strings were empty before and after. No commit or push command was performed.

```text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
```

Full before/after inventory locations and inventory-file hashes are preserved in the JSON `integrity.snapshot_files` entry. They are external scratch evidence; the compact tree identities, timestamps, counts and per-scope comparisons are retained in the delivered JSON itself.

## Consulted source register

These hashes identify the consulted bytes. Historical PDF claims remain indirect as labelled in §19; a hash of Paper D does not turn those into a fresh PDF inspection.

| Source key | Local source | SHA-256 |
|---|---|---|
| D_CODE | [reference_scaffold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/reference_scaffold.py) | `39723db1d5e808fa8aeb3585eb47ac4b1cbc01310e07e9171b6d6e04111c4aaf` |
| D_PAPER | [PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md) | `7bc87de09400ba1a37d5dc9ab7be38c9a978be31bb35ece56102d29ee2e5d25b` |
| D_TESTS | [test_reference_scaffold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_reference_scaffold.py) | `50f2c49b285ab3937219035c9e4c5b664d40c6a7b391e6e0a9ffb04a67cfa618` |
| D_COORDINATES | [geometry_coordinates.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/geometry_coordinates.py) | `45d2ec653420bb7dcfe0091eabdbc331dd9f32c3b3a4b0ba15d11bff13b739af` |
| D_SYMBOLS | [SYMBOLS_AND_THEOREMS.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/SYMBOLS_AND_THEOREMS.md) | `93911abe1eab5a396c0b62099a3358231ee7529970630ad41284e212c6f1ed10` |
| EARLIER_NOTE | [note_source.json](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_notes/reference_scaffold/note_source.json) | `e4047e63b41f3a67362ddfea4be7d923b7202b3988faeebcffa955424a6459f8` |
| GEOMETRY_RECORDS | [_geometry_records.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_geometry_records.py) | `7313d6bcea2e03615a0ac5ceec177d7abd9bc695e1a2ac6d9b8aa629838c1f60` |
| C_CODE | [geometry.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py) | `18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf` |
| C_PAPER | [PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md) | `5a0cbdae4aaf689cfe1f5b29305960e90c88e26d0db28834802ef70fc16549fb` |
| B_CODE | [face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py) | `be9d1e25a6f368e644ecfa9b1af70ba9382599e8b4d43d529d1783004d86ded7` |
| B_PAPER | [PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md) | `fb4575120470e8d7143ebc1f475ee4635caf9f39f21f88308960308fb259e150` |
| DYNAMICS | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py) | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |
| READOUTS | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py) | `3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9` |
| CENSUS | [TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md](C:/Users/Notandi/.codex/reports/TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md) | `353512d19901d306b40c34a5d7443773ecb5fa172a87f1b7e101eacad0cae6a7` |
| OLD_VIEWER | [toy_3d_triocta.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_3d_triocta.py) | `3792d0d97bd7e0beed157586453ea71a3828e6a79a4ed8638787163cb490ee05` |
| OLD_3D | [geometry_3d.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_3d.py) | `b6803b3a02f5240a5cb00a3dbc9cf403c2e762de713146aa3848996738772400` |
| OLD_TETRA | [dual_tetra_mapper.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/dual_tetra_mapper.py) | `14845223bbfa0c0f17df2781ee4a0ebba9befeee5f374bb01a4647242dbedf9f` |

## Delivered artifact identities

| Artifact | SHA-256 |
|---|---|
| Independent checks Python | `ef9fb48d598164c40e491595664f36d2ddda5c7c716d263417a5f771d2108f70` |
| Exact results JSON | `5d31ef5bafadd9c1f3e123903cbd1c8cb621ce946e22916825ff436c6e90726e` |

The packet does not embed its own recursively changing hash. Its two companion identities bind the delivered verification result to the exact external script. All three requested deliverables are in `C:\Users\Notandi\.codex\reports`, outside the protected trees.

Atlas 05 closes the reconstruction of the current reference-scaffold construction. The state-to-gap and historical registration interfaces remain explicitly open. No source correction, dynamics change, commit or push is part of this closeout.

