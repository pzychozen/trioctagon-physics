One rigid rotation can align two identical centered copies when their relative pose is allowed by the stationary support. Independent movement of every opening is not inherently required. However, a whole-object rotation cannot remove the source geometry’s relative twist between upper and lower openings while keeping both registered to the same fixed host directions. Changing that relationship would change the geometry relative to its support, and no such motion is supplied by the existing equations. There is also a real projection effect: two edges of one central opening look almost straight from above, but meet at a much smaller angle in space. The sketch’s 45-degree remark was not used as a target. The result is a partial geometric correspondence with exact constraints; the remaining choice is which actual source feature is attached to each stationary line.

# NCM-FIXED-GAP-01 v0.1

31 October 2026. External geometry-only investigation. No Git, application/kernel changes, native execution, motion law, paper amendment or publication.

## Exact angles first

All decimal angles below illustrate exact formulas; none is measured from the sketch.

| Quantity | Exact definition | Degrees |
|---|---|---:|
| Separation of two different upper opening azimuthal bisectors | arccos(−1/2) | 120 |
| Separation of two different lower bisectors at the same tau/hand | arccos(−1/2) | 120 |
| Smaller angle between their unoriented support lines | arccos(1/2) | 60 |
| Maximum source lower-to-upper azimuthal offset | delta_h = atan(sqrt(3)(sqrt(2)−1)) | 35.657129825 |
| Cross-level principal azimuth differences at tau=h | delta_h; 120°−delta_h; 120°+delta_h | 35.657129825; 84.342870175; 155.657129825 |
| Two edges of one upper fan-opening arc, viewed from above | formula below | 179.033309239 |
| The same two edges in 3D | formula below | 80.963586035 |
| Lower fan-opening edge angle at tau=h, in 3D | formula below | 92.819440789 |
| Actual host-notch tip angle | arccos(3/4) | 41.409622109 |
| Host-notch tip angle in axial projection | pi/3 | 60 |
| Host-notch plane inclination to horizontal | atan(2/sqrt(3)) | 49.106605351 |
| Host chamfer edge inclination to horizontal | pi/4 | 45 |

The last exact 45-degree value belongs to an accepted host edge inclination. It is not evidence that the author intended that edge or that a gap should turn by 45 degrees. Likewise the 179-degree value is an angle between the two projected edges of ONE opening, not two different opening bisectors. No agreement with the author’s approximate drawing is claimed.

## 1. Which geometry and which center?

The controlling definitions are the exact folded host in Paper C and the refined central PLUS/MINUS family in CENTRAL, Sections 2, 4 and 5. The refined surface is an additional declared research construction; it is not uniquely forced by the outer octagons. The historical intersecting mesh, actual host, refined surface, and cone proxies are distinct objects.

Use centered coordinates (X,Y,w), with vertical unit vector e_w. The center is the host’s O=(0,r,0) in uncentered Paper C coordinates. Width is one:

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,\quad
a=d/2,\quad h=s/2,\quad H_0=1/2=h+d.
\]

Let

\[
\alpha_i=-\pi/2+i\pi/3,\quad e_i=(\cos\alpha_i,\sin\alpha_i),
\quad n_k=e_{2k},\quad g_k=e_{2k+1}=n_k+n_{k+1},\quad j_k=Jg_k,
\]

where J(X,Y)=(−Y,X), indices i are modulo six and k modulo three. For 0≤tau≤h:

\[
\xi=\tau/r,\quad\delta=\arctan\xi,\quad
A_\tau=I-\xi J=\sqrt{1+\xi^2}\,R_{-\delta},
\]
\[
T_i=(ae_i,h),\quad B_i=(aA_\tau e_i,-h),\quad
U_k=(rn_k,H_0),\quad L_k=(rA_\tau n_k,-H_0).
\]

Tau is a geometric shape parameter, not time. The allowed endpoint changes both lower planar orientation and lower planar scale. It is not a rigid turn of the same fixed mesh.

The source faces are F_i=[T_i,T_(i+1),B_(i+2)], D_i=[T_i,B_(i+2),B_(i+1)], and the two fan triangles [U_k,T_(2k−1),T_(2k)] and [U_k,T_(2k),T_(2k+1)], with the corresponding lower replacements. MINUS is the image of the ENTIRE face complex under S=diag(−1,1,1). Negating tau while retaining the PLUS face list would not be that definition.

The source reconstruction checks 18 vertices, 42 edges and 24 triangular faces per refined case. All 12 boundary edges are exactly the edges of the six arcs below.

### The six central openings

| Label | Actual broken boundary | Adjacent fan tips | Height | PLUS azimuth |
|---|---|---|---|---|
| G+0 | U0—T1—U1 | U0,U1 | h through H0 | −30° |
| G+1 | U1—T3—U2 | U1,U2 | h through H0 | 90° |
| G+2 | U2—T5—U0 | U2,U0 | h through H0 | 210° |
| G−0 | L0—B1—L1 | L0,L1 | −H0 through −h | −30°−delta |
| G−1 | L1—B3—L2 | L1,L2 | −H0 through −h | 90°−delta |
| G−2 | L2—B5—L0 | L2,L0 | −H0 through −h | 210°−delta |

The symbols +/− in G identify upper/lower, not hand. In MINUS, the same labeled upper azimuth theta becomes pi−theta; the lower azimuth becomes pi−theta+delta. Thus MINUS reverses the lower offset relative to the upper direction set. Labels are retained under reflection rather than silently reordered.

[GAP_TABLE.md](GAP_TABLE.md) gives all 24 case-specific rows at tau=0,h for both hands, including exact source vertex labels and numerical directions. [GEOMETRY_COORDINATES.json](GEOMETRY_COORDINATES.json) retains exact expressions and display coordinates.

**No source-defined filled triangular interior or “own center” is assigned to these broken arcs.** The top-to-top closing segment is absent. A triangle centroid, aperture normal or local hinge would be a new definition. Both whole configurations can share O without each individual opening possessing its own admitted center.

### Separate host-notch patches

The six finite host measurement triangles are

\[
N_{k,\sigma}(\lambda,\zeta)=
\left(2r-\frac{\sqrt3d}{2}\lambda\right)g_k+
\zeta j_k+\sigma(h+d\lambda)e_w,
\quad0\leq\lambda\leq1,\quad|\zeta|\leq d\lambda/2 .
\]

Their three vertices use (lambda,zeta)=(0,0),(1,−d/2),(1,d/2). Their planes are

\[
g_k\cdot(X,Y)+\sigma(\sqrt3/2)w=2r+(\sqrt3/2)h.
\]

These are finite measurement regions, not added cap material. Their directions stay fixed as tau varies. The exact upper fan/notch azimuth match does not make the sets coincide. For tau<h the lower fans are strictly inside the corresponding notch-plane inequalities; at tau=h only appropriate lower fan tips contact finite notch vertices. No positive-area coincidence follows.

The author’s latest description refers to top triangular gaps. The sketch alone does not uniquely identify those with G+ arcs rather than N+ notch regions; both are retained here. The green outlines are not used to replace either source definition.

## 2. What the apparent angles mean

The source azimuthal bisectors are horizontal directions about O. All three on a level have dot product −1/2 with one another. They are therefore 120 degrees apart as directed rays, or 60 degrees apart when each is extended to an unoriented 180-degree line. There is no pair of distinct same-level bisector rays almost 180 degrees apart.

For the PLUS cross-level sets, differences modulo 360 are −delta and ±120°−delta. Since 0≤delta≤35.657129825°<60°, the three principal separations are delta, 120°−delta and 120°+delta. MINUS has the same multiset, with label order reversed.

An actual 3D ray to a boundary point is a different diagnostic. For example O→T1 and O→T3 have angle 60°, despite their azimuths differing by 120°. The complete matrices for O→T_(2k+1) and O→B_(2k+1) are in [FEATURE_RAY_ANGLES.json](FEATURE_RAY_ANGLES.json) and GAP_TABLE.md. They use actual boundary vertices, not invented aperture centers or flow directions.

### A concrete near-straight projection

For G+_k, subtract the actual elbow T_(2k+1). Write c=r/2−a and b=sqrt(3)r/2=1/4. Its incident edge vectors are

\[
v_\pm=cg_k\pm b j_k+d e_w.
\]

Hence

\[
\cos\gamma_{\rm top}=\frac{c^2-b^2}{c^2+b^2},\qquad
\cos\gamma_{\rm spatial}=\frac{c^2-b^2+d^2}{c^2+b^2+d^2}.
\]

Here c≈−0.002109042, so the top projection almost flattens the V. The exact arccosines give 179.033309239° and 80.963586035°. For the lower V,

\[
\cos\gamma_{\rm lower}=
\frac{(1+\xi^2)(c^2-b^2)+d^2}
{(1+\xi^2)(c^2+b^2)+d^2}.
\]

It reaches 92.819440789° at tau=h. The top angle stays the same because the planar lower map is a similarity. Reflection to MINUS preserves these angles.

At tau=0, T_(2k+1) and B_(2k+1) project to the same top-view point but differ in height by 2h. Whole upper/lower arcs likewise have coincident top projections while remaining disjoint in 3D. Looking from the opposite side does not remove this ambiguity: changing the viewing direction to its opposite reflects screen coordinates and leaves projection-coincidence predicates unchanged.

## 3. Stationary supports: exact permissible rotations

For this section an attached support condition means that the SAME centered transformation R applied to the geometric configuration must preserve a specified stationary line L=span(ell). A line merely drawn in the world can remain stationary while an unattached body rotates freely; its presence alone imposes no constraint on that body. This attachment distinction is left explicit.

Let ell be unit length and R in SO(3).

**Locus only:** R(L)=L if and only if R ell=ell or R ell=−ell.

- R ell=ell: any rotation about L; it fixes every point of L and both directed rays.
- R ell=−ell: a half-turn about some axis perpendicular to L. It preserves the line as a set and exchanges its two rays.

Proof: a centered orthogonal map sends a unit vector spanning L to ±ell. The + case is its SO(2) action on the perpendicular plane. The − case has eigenvalue −1; a proper 3D rotation has that eigenvalue only at angle pi, and its +1 axis is perpendicular to ell.

**Fixed endpoints/rays:** fixing nonzero endpoints on both sides, or each directed ray, requires R ell=ell. With a rigid centered rotation there is no additional sliding or endpoint-distance freedom.

**Continuous support preservation:** along a continuous path beginning at identity, the sign in R(t)ell=±ell cannot change. Only the rotation-about-L component is reachable while L remains fixed throughout. A half-turn that exchanges its rays can be an allowed endpoint registration without being reachable by such a continuously constrained path.

A 90-degree rotation ABOUT the fixed line is allowed by the single-line condition. A 90-degree turn that TILTS that same line fails it. No particular turn angle has been imposed as the desired motion.

### More than one stationary line

If two nonparallel lines are fixed pointwise, R is identity. If two individually named, nonorthogonal lines are preserved only as sets, their spanning unit vectors u,v obey u·v≠0; preservation of their dot product forces their signs to agree. The only possibilities are identity and the half-turn about u×v. For two perpendicular lines there are four possibilities: identity and half-turns about either line or their common normal.

For the three planar lines L_k=span(g_k), every pair is nonorthogonal. Preserving each individually allows only identity and R_w(pi). The latter reverses all three directed rays and does not register the directed upper gap triad to itself. Thus a self-registration of the directed triad AND all three individually fixed lines is identity.

Allowing the COLLECTION of three lines to be permuted is a different condition: R_w(120°) then works and permutes all three gaps together. It does not fix each named support separately. Three pointwise-fixed nonparallel support directions leave identity only.

## 4. Two definitions of alignment and their results

### A. Azimuth/bisector registration

This compares source directions about O, with explicit gap labels or an allowed permutation. It does not compare heights, lengths, boundary sets, or an aperture interior.

For same-hand copies with the same tau and an axial relative pose theta, R_w(theta) aligns all six directions and their attached finite boundaries simultaneously. It preserves the vertical support pointwise. No independent gap turning is needed for this case. If the host belongs to the rotating copy, it moves with that copy; this must not be confused with preserving contacts to a separate stationary host.

For registration of ALL six bisectors to the fixed host direction sets at a common orientation, an axial rotation beta must satisfy, for PLUS,

\[
\beta=0\pmod{120^\circ},\qquad
\beta-\delta=0\pmod{120^\circ}.
\]

The first condition is upper, the second lower. They are compatible only at tau=0 in the admitted interval. For MINUS the second sign reverses and the same conclusion holds. The exact compensation beta=delta aligns the PLUS lower directions but shifts all upper ones by delta. A rigid turn preserves the relative mismatch.

This obstruction does not depend on refusing to try a favorable tilt. Mapping the three upper direction vectors onto their horizontal target triad forces their plane to remain horizontal. An orthogonal map restricted to that plane preserves the angular relation of the two triads, possibly reversing its sign. It cannot turn two distinct triads into the single same target triad.

Correcting that mismatch while keeping the upper directions fixed would require the lower three directions to change RELATIVE to the upper geometry. It need not mean six independent motions: a coordinated lower-level change would already alter the relation. Such a change is not a common rigid transformation of the fixed source surface.

### B. Finite broken-boundary registration

This compares the actual connected segments and their named source vertices. For a declared point/arc correspondence, the exact requirements are

\[
R^TR=I,\quad\det R=1,\quad Rp_j=q_{\pi(j)},\quad
R\ell_a=\varepsilon_a\ell_a,
\]

with arc incidence preserved, center fixed, and epsilon_a selected according to the endpoint convention. A direction-only predicate normalizes and drops information and therefore cannot substitute for these equations.

All dot products p_i·p_j must match q_pi(i)·q_pi(j), including radial norms. Conversely, equality of these centered Gram matrices defines an isometry on the span. For rank three its orientation must be proper; for lower rank one must choose a proper extension that also satisfies the support conditions. This gives a finite exact compatibility test, not a parameter search.

For identical copies with target pose P, all unlabelled boundary registrations are R=P H where H is a proper symmetry of the source boundary set. The source boundary group is C3 for positive tau and D3 at zero. Restrict H to the permitted label action, then test R ell=±ell. If all six gap labels and upper/lower assignments must remain fixed, H is identity. This tests any supplied pose without inventing one.

Why these groups suffice: upper fan tips have a common distinct radial norm and centroid H0 e_w (sum 3H0 e_w); at positive tau lower tip norms are larger and cannot be interchanged with them. A proper self-map therefore fixes e_w and cyclically permutes the upper tip triangle, leaving only three axial turns. At zero the six fan tips have covariance diag(r²/2,r²/2,H0²). Its unique vertical eigenvalue forces every symmetry to preserve the vertical axis as a set; height-swapping half-turns add the other three proper symmetries. Boundary corners and radial norms prevent an extra hidden continuous symmetry.

### Different tau cannot be fixed by any centered rigid rotation

Sum squared distances from O over the 12 DISTINCT vertices of the six boundary arcs. Directly,

\[
M(\xi)=M(0)+3(a^2+r^2)\xi^2.
\]

This is invariant under every centered rotation, even if labels are permuted. Since tau≥0 and a,r>0, distinct tau values have distinct M. Thus tau=0 and tau=h are not two poses of one rigid boundary. The source’s lower dilation is an exact obstruction independent of viewing direction or support.

Removing the lower offset alone leaves its scale factor sqrt(1+xi²). Mapping the lower vertices all the way to the zero member would additionally require an in-plane contraction. Moving lower vertices relative to fixed upper vertices also changes the connecting band triangles. No source hinges or independent gap rotors authorize that deformation.

### Hands and upper/lower exchange

At zero, Q=diag(−1,1,−1) is a proper same-hand endpoint symmetry. It maps G+_k to the reversed G−_(-k−1), and maps all actual faces correctly. It preserves the vertical line as a set but exchanges its ends. It fixes the horizontal Y support pointwise. Thus its support status depends on the stated attachment, not on a picture of a moving cone.

At positive tau Q cannot register the source family to itself: it would put the larger lower radius at the upper height where the family always has radius a. A body can of course be rotated into that different pose; it is not a registration to the declared canonical upper/lower family.

At tau=0 PLUS and MINUS have identical opening boundary sets, but different band triangulations. No proper symmetry of their common vertex set maps those full face complexes to one another. At positive tau even their complete six-arc boundary sets are not properly congruent at the fixed registration: preserving the upper triad allows only rotations modulo 120°, whereas matching the opposite lower twists requires 2delta=0 modulo 120°, impossible for 0<delta≤35.657129825°. The mirror S maps them exactly but has determinant −1, so it is not an admitted rigid rotation.

### Boundaries cannot become the finite notch patches

An arc is not a filled finite triangle. Even if one asks only to put its entire boundary into the host notch, a centered radial obstruction remains. Every opening arc contains its ring elbow, whose squared radius is at most

\[
a^2(1+(h/r)^2)+h^2=\frac{15}{2}-\frac{21\sqrt2}{4}.
\]

Every point on any host-notch plane has squared radius at least

\[
\frac{(2r+\sqrt3 h/2)^2}{7/4}
=\frac{19}{84}+\frac{\sqrt2}{14},
\]

which is strictly larger. The plane-distance lower bound also applies to its finite triangle. A centered rotation preserves the elbow’s radius; it cannot place the entire central broken arc into any notch patch. The admitted endpoint contacts at tau=h involve fan tips, not the much nearer ring elbows.

## 5. Fixed contacts and independent gap movement

If the three upper fan tips must remain registered to their exact stationary host contacts as a set, their sum forces the vertical direction to remain fixed and their equilateral arrangement permits only axial multiples of 120°. If their labels are individually fixed, only identity remains. A continuous path preserving that exact contact set is constant. This is a conditional geometric restriction, not a claim that the contacts are welded.

Each central arc shares fan-tip vertices with its neighbors. Turning one gap independently while holding the rest of the mesh fixed is therefore not an operation defined on this mesh. It would require changing shared vertices, adjacent fans and/or band faces, or specifying an additional attachment and joint. A failed rigid-registration test identifies that requirement; it does not supply the missing deformation or a physical law.

## 6. Decision matrix

| Question / interpretation | Decision | Reason |
|---|---|---|
| All six bisectors and finite arcs between same-tau, same-hand copies with a permitted common pose | Conditional yes | One common rigid transform suffices; verify support, pose and label conditions |
| Arbitrary axial pose difference with just the attached vertical support fixed pointwise | Exact yes, geometrically | R_w(theta) fixes that line and transports all attached features together; fixed-host contacts are a separate condition |
| Upper and lower azimuths simultaneously registered to the SAME fixed host triad at tau=0 | Exact yes | Both direction sets already agree, with axial permutations allowed if labels permit |
| Same demand at positive tau | Exact no | Two direction congruences conflict by delta; at h it is 35.657129825° |
| All three individually fixed planar bisector lines AND self-registration of the directed gap set | Identity only | The other support-preserving endpoint is R_w(pi), which reverses the directed triad |
| Zero-member upper/lower exchange using Q | Conditional yes at endpoint | Actual faces and arcs match; vertical endpoints swap; continuous path and retained contacts are stronger restrictions |
| Positive-tau upper/lower swap to a canonical member | Exact no | Unequal upper/lower radii |
| Finite boundaries at distinct tau values | Exact no | Strictly different centered squared-radius sum |
| PLUS versus MINUS opening boundaries at zero | Exact yes as unlabelled sets | Boundaries coincide; full triangulated meshes still differ |
| PLUS versus MINUS complete finite boundary sets at positive tau, by a proper centered transform | Exact no | Upper-triad constraint conflicts with opposite lower twists |
| Whole central arc becomes a finite host-notch region | Exact no | Different set types and a strict ring-elbow radial obstruction |
| Viewpoint change creates apparent overlap/near-straightness | Exact yes for projections | Explicit top-view examples and opposite-camera comparison |
| Viewpoint change produces actual 3D registration | Exact no | It changes only the projection map |
| Arbitrary coordinated independent gap turns in the fixed mesh | Undefined as an admitted operation | Shared boundary vertices and adjacent faces would need a new deformation/attachment definition |
| Existing native or Z equations cause the operation | No supplied correspondence | They update channel state/readouts, not tau, gap vertices or pose |
| A unique interpretation of each red support as a specific geometric attachment | Undefined | The conversation sketch deliberately does not specify that mapping |

## 7. Both sides, visualizations and separate configurations

[Top/bottom sheet](figures/01_top_and_bottom.png) shows all six boundaries for PLUS zero, PLUS h and MINUS h from both vertical viewing directions. Red lines in this sheet are the CONDITIONAL planar supports span(g_k), not inferred rods. Their opposite halves are fully drawn.

[Side/opposite-side/oblique sheet](figures/02_side_and_oblique.png) shows the same cases from −Y, +Y and an oblique direction. Here the red line is the CONDITIONAL vertical support span(e_w). It remains fixed. Both near and far edges are retained in transparent technical projection. Blue/orange distinguish upper/lower; gray filled patches are actual finite notch measurement triangles. No central opening interior is filled.

[Projection-angle sheet](figures/03_projection_angle_comparison.png) compares one actual broken arc in top projection and in its true edge plane. SVG versions accompany all PNGs.

These are static cases, not a proposed path through tau. The two support examples are distinct conditional attachments, not combined constraints silently read from the sketch. Both have the exact common center and source width. The circle is the projected original enclosing sphere, radius sqrt(13/12−sqrt(2)/2), recovered from the host vertices.

For two simultaneous copies, registration is a relation between two geometric sets. For one copy in different poses, it is a comparison between alternatives. The geometry does not equate simultaneous superposition with fast switching; no rate, clock, duty cycle, exposure model or material overlap law has been introduced.

## 8. Provenance correction

NCM-DUAL-01 prescribed moving cone-pair axes through x/y/z stations. Its 60°/120° midpoint angles, rigid comparator, and 3/6/12-leg return distinctions belong to those trial paths and, where stated, added marks and repeating extensions. They are not verified results about stationary supports or the six actual opening arcs.

The previous conversational interpretation that the “stick” should itself turn is not used here. The current author request and work order control: the support is stationary. Prior cone proxies were shorthand for model parts, not individual triangular openings.

The native coherence-return and fixed-parameter bounds have their own equations and hypotheses. Correcting the motivating geometric interpretation neither proves those theorems false nor makes them a verified account of this fixed-support geometry. No manuscript, published PDF, historical report or publication receipt was changed.

## 9. Verification and limitations

The final geometry checker passed 104 finite/exact predicate groups, and a separate finite-contact/symmetry check passed seven more, with zero failures (111 check records total, not 111 independent theorems). The latter verifies actual finite-notch vertex contacts in both hands and the zero-tip covariance used in the boundary-symmetry classification. It uses fresh transcription from the source equations, SymPy exact arithmetic and static numerical displays. It does not execute the repository geometry or dynamics modules. The bounds and classification arguments above are written proofs; finite checks corroborate specified examples rather than replace the general arguments.

The first checker pass recorded six false-negative coordinate matches because equivalent radicals had different factored/expanded string representations. An exact zero-difference diagnostic confirmed the mismatch was in key representation. Expanded radical keys corrected it; the successful rerun and the initial failed records are retained. Opposite-camera equivalence is checked by the exact reflection identity rather than sampled pairs. No result was waived to obtain a pass.

The received sketch is 313×291, 7,706 bytes, SHA-256 2164a97e3cc31c363eef0fe59c4ea714bddf01cc66b52b8d9a1ec3f16561d983. It differs from the image hash named in the order. The author supplied this image directly after the unavailable file was identified; its exact bytes are retained, and no measured angle depends on it. The author’s clarification that 45° was conversational is retained.

Source identity, protected-file before/after checks, actual command exits, figure QA, and archive integrity are recorded separately in the closeout. No global absence of possible motion is claimed. The source-derived geometry permits rigid reorientation under stated constraints, but does not choose a native trajectory, physical flow or a unique attachment.

## Recommendation

**(b) Partial correspondence requiring a defined attachment.** The source-supported relation worth retaining is the coordinated threefold opening geometry, its lower rotation/dilation, and the exact stationary-line stabilizer. It already tells us when a single rigid operation works and when it cannot work.

The single smallest author-dependent distinction is: **which named source feature, if any, is required to stay registered to each red support line?** For example, an azimuthal direction and a fixed boundary point impose different constraints; a G arc and an N patch are different objects. No more precise sketch angle or complete motion story is needed. The line’s stationarity is accepted and is not being asked again. No next investigation, motion law, software change or paper follows automatically.
