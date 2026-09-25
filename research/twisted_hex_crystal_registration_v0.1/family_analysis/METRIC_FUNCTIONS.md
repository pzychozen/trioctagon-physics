# Exact metric functions and the six-contact skeleton

New Codex derivations from the preserved coordinate and face functions.
Use physical units and the constants in `TWISTED_HEX_FAMILY_ANALYSIS.md`.
For the mirrored surface family use u=|t| and q=u/r. Every expression in
this note is EXACT_CLOSED_FORM. The area minimizer is separately
EXACT_IMPLICIT with a rigorous isolating interval. Decimal values in the
other notes are illustrations of exact results, not NUMERIC_ONLY claims.

## Six-contact skeleton

Write the upper contacts \(U_k=(rn_k,H)\), lower contacts
\(B_k=(rn_k-tJn_k,-H)\), and O=(0,0,0). Use the two triangle cycles
and three corresponding spokes: six vertices and nine edges. O is a
reference, not an extra asserted strut.

| Quantity | Exact expression |
|---|---|
| Upper triangle side | 1/2 |
| Lower triangle side | \(\sqrt{1/4+3t^2}\) |
| Corresponding U_k--B_k spoke | \(\sqrt{1+t^2}\) |
| U_k--B_(k+1) diagonal | \(\sqrt{5/4+t^2-t/2}\) |
| U_k--B_(k-1) diagonal | \(\sqrt{5/4+t^2+t/2}\) |
| Distance O--U_k | \(1/\sqrt3\) |
| Distance O--B_k | \(\sqrt{1/3+t^2}\) |
| Upper triangle area | \(\sqrt3/16\) |
| Lower triangle area | \(\sqrt3/16+3\sqrt3t^2/4\) |

Let L_k=(rn_k,-H) be the lower host edge center, and
G_-=(0,0,-H). The planar triangle (G_-,L_k,B_k) is right at L_k,
with perpendicular legs r and |t| and area r|t|/2. The vertical/tangent
triangle (U_k,L_k,B_k) is also right at L_k, with legs 1 and |t| and
area |t|/2. These triangles collapse at zero; this is not a degeneration
of any actual mesh face.

The signed horizontal determinant is
\(\kappa=\det(rn_k,rn_k-tJn_k)=-rt\). With upper centroid
G_+=(0,0,H), the ordered auxiliary tetrahedron (O,G_+,U_0,B_0)
has oriented volume \(-rt/12\). This is a four-point determinant,
not an enclosed volume of the open surface.

Same-level lengths, corresponding spokes and unsigned areas are even.
Kappa, the auxiliary oriented volume and the difference of the two
cross-diagonal squared lengths are odd. The two diagonal classes swap
under reflection; each separately need not be even with fixed labels.

At t=0 the two triangles are congruent and aligned, spokes have length 1,
cross-diagonals have length sqrt(5)/2, and both odd measures vanish.
At |t|=U, the lower side is \(\sqrt{5/2-3\sqrt2/2}\), spoke
\(\sqrt{7/4-\sqrt2/2}\), and |kappa|=rU. The corresponding edge
endpoint is attained without mesh-face degeneration.

## All actual mesh edge classes

The table gives **squared lengths**, avoiding any tolerance grouping.
Vertex and edge membership lists are in `METRICS_EXACT.json`.

| ID | Edge role | Squared length | Count |
|---|---|---|---:|
| E0 | Upper ring | \(a^2\) | 6 |
| E1 | Cross-ring +1 strut | \(s^2+a^2(1+q^2-\sqrt3q)\) | 6 |
| E2 | Band +2 tessellation diagonal | \(s^2+a^2(3+q^2-\sqrt3q)\) | 6 |
| E3 | Upper apex to middle ring vertex | \((r-a)^2+d^2\) | 3 |
| E4 | Upper apex to outer fan vertex | \(r^2+a^2-ra+d^2\) | 6 |
| E5 | Lower ring | \(a^2(1+q^2)\) | 6 |
| E6 | Lower apex to middle ring vertex | \((r-a)^2(1+q^2)+d^2\) | 3 |
| E7 | Lower apex to outer fan vertex | \((r^2+a^2-ra)(1+q^2)+d^2\) | 6 |

Total: 42 edges. The +2 edges are triangulation edges, not a recovered
independent request for physical struts. The other diagonal of each skew
band quad is a corresponding-index T_(i+1)--B_(i+1) segment, of squared
length \(s^2+a^2q^2\); it is a distance diagnostic, not a new mesh edge.

The general same-level apex-to-ring squared distance is
\(d^2+\rho^2(r^2+a^2-2ra\cos(k\pi/3))\), k=0..5, where
rho=1 above and rho=sqrt(1+q^2) below. The ring radii are a and
\(a\sqrt{1+q^2}\); apex radii are r and \(r\sqrt{1+q^2}\).
Thus ring/apex radius ratio a/r is built in on both levels. It does not
select a member. Another aspect ratio is full height divided by lower
apex diameter, \(1/(2\sqrt{r^2+u^2})\), strictly decreasing for u>0.

## Four face-area classes and total area

Let P_j denote squared triangle area, with six faces in each class:

\[
P_0=\frac{a^2s^2+a^4(\sqrt3/2-q)^2}{4},
\]
\[
P_1=\frac{a^2(1+q^2)s^2+
a^4(\sqrt3(1+q^2)/2-q)^2}{4},
\]
\[
P_2=\frac{a^2[4d^2+3(r-a)^2]}{16},\qquad
P_3=\frac{a^2(1+q^2)[4d^2+3(r-a)^2(1+q^2)]}{16}.
\]

P0 and P1 are the alternating band triangles. P2 and P3 are upper and
lower fan triangles. Each formula is checked against direct cross products
of the imported vertices. The total triangulated area is
\(S(u)=6(\sqrt{P_0}+\sqrt{P_1}+\sqrt{P_2}+\sqrt{P_3})\).
This is the area of this specific diagonal choice, not of an unspecified
smooth interpolation or a different split of the skew quads.

## Selected fold-plane angles and covariance

For a face f=(i,j,k), let N_f=(v_j-v_i) cross (v_k-v_i). Along each selected
interior edge with incident faces f,g use

\[
\vartheta=\arccos\frac{|N_f\cdot N_g|}{\|N_f\|\|N_g\|}
\quad\hbox{in }[0,\pi/2].
\]

This is an **unoriented angle between planes**, not a claimed solid interior
dihedral or a signed fold angle. The selected edges (0,8), (0,7), (0,12),
(6,15) represent band diagonal, band strut, upper fan rib, and lower fan
rib. Exact rational-algebraic functions for cos squared are supplied in
`METRICS_EXACT.json`; their equality conditions are in the search record.

For the band quad (T0,T1,B2,B1), the scalar triple product is
\(({-7\sqrt3+5\sqrt6})/8\,(u-1/2)\). It never vanishes on [0,U].
No planar quadrilateral face can replace those two triangles implicitly.

The centroid is O. The covariance \((1/18)\sum_i v_iv_i^T\) has eigenvalues

\[
\lambda_x=\lambda_y=(2+(u/r)^2)(d^2/24+r^2/12),\qquad
\lambda_z=(2s^2+1)/12.
\]

The vertical eigenvalue exceeds the horizontal value even at U, and hence
throughout the interval. Horizontal multiplicity is present identically;
there is no extra three-way degeneracy. These exact formulas are also
checked directly from all 18 vertices.
