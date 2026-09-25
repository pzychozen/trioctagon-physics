# Signed vertices, face lists and exact sections

New Codex derivation, 2026-09-25, of the unchanged verified candidate.
Constants and units are defined in `TWISTED_HEX_FAMILY_ANALYSIS.md`.
Let \(J(x,y)=(-y,x)\), \(e_i=(\cos\theta_i,\sin\theta_i)\),
\(\theta_i=-\pi/2+i\pi/3\), and \(n_k=e_{2k}\).

## One signed vertex convention

\[
T_i=(ae_i,h),\quad B_i(t)=(aA(t)e_i,-h),\quad
U_k=(rn_k,H),\quad L_k(t)=(rA(t)n_k,-H),
\quad A(t)=I-(t/r)J.
\]

The script imports these coordinates from `canonical_points(t)` rather
than substituting another ring rule. Index blocks are T:0..5, B:6..11,
U:12..14, L:15..17. The name B for the lower ring here is distinct from the
lower apex named B in the six-contact skeleton report.

With horizontal reflection \(R=\operatorname{diag}(-1,1)\),
\(RJR=-J\), hence \(RA(t)R=A(-t)\). Reflection permutes indices
\(i\mapsto-i\pmod6\), \(k\mapsto-k\pmod3\) within each block.
Thus the signed vertex sets are exact mirror images. Vertices depend
affinely on t and pass continuously through their common zero set.

`F_plus` is the original face list. In these common signed vertex labels,
`F_minus` is its image under the same block permutation. Using `F_plus`
unchanged at negative t would not reproduce the original mirrored variant.
Both lists are recorded in `SIGNED_AND_SECTION_DATA.json`.

## Footprint polar law

Since \(J^T=-J\) and \(J^2=-I\),

\[
A(t)^TA(t)=(1+(t/r)^2)I,\qquad
A(t)=\sqrt{1+(t/r)^2}\,R_{-\arctan(t/r)}.
\]

This proves isotropic scaling and rotation for every signed t, including
zero. With \(\delta(t)=\arctan(t/r)\), the footprint rotates by
\(-\delta\); the PLUS/MINUS labels keep their existing source convention.
The inverse contraction is \(\alpha(t)=\cos\delta(t)>0\). Alpha is even;
delta is odd. Nonzero magnitude has strict contraction; zero does not.

The lower apex \(rn_k-tJn_k\) lies on the host line \(n_k\cdot x=r\).
Its signed edge offset is \(-t\) along \(Jn_k\), with \(|t|\le s/2\).
The endpoint is an edge endpoint, not a failed contact. Upper apices remain
fixed. All squared center residuals are t squared.

## Corresponding-index interpolation

For \(0\le\lambda\le1\) and \(z=h(1-2\lambda)\), interpolating
T_i to B_i gives

\[
M=(1-\lambda)I+\lambda A=I-\lambda(t/r)J,
\quad \rho=a\sqrt{1+(\lambda t/r)^2},
\quad \phi=-\arctan(\lambda t/r).
\]

It maps an entire planar circle to a circle and a regular six-point ring to
a similar regular hexagon. It describes the corresponding-index affine
scaffold (and a ruled surface if those polygon points are joined). No such
T_i--B_i struts were added to the accepted candidate.

## Actual triangulated band sections

For PLUS, the actual faces are
\((T_i,T_{i+1},B_{i+2})\) and \((T_i,B_{i+2},B_{i+1})\).
At an interior height the section consists of segments
\(S_iD_i\) and \(D_iS_{i+1}\), where

\[
S_i=(1-\lambda)ae_i+\lambda aA(u)e_{i+1},\qquad
D_i=(1-\lambda)ae_i+\lambda aA(u)e_{i+2}.
\]

For m=1,2, set \(\beta_m=m\pi/3\) and

\[
C_m=(1-\lambda)I+\lambda R_{\beta_m}(I-qJ)=c_mI+b_mJ,
\]
\[
c_m=1-\lambda+\lambda(\cos\beta_m+q\sin\beta_m),\quad
b_m=\lambda(\sin\beta_m-q\cos\beta_m).
\]

Each orbit is a regular six-point set with radius
\(a\sqrt{c_m^2+b_m^2}\) and relative angle
\(\operatorname{atan2}(b_m,c_m)\). The union generally has twelve
vertices, with alternating segment types, and C6 sectional symmetry. It
is not generally a regular dodecagon or one regular hexagon. At t=0 and
lambda=1/2 its two squared radii are \(3a^2/4\) and \(a^2/4\), an
exact counterexample to identifying it with the corresponding-index law.
At lambda=0 or 1 pairs merge to the appropriate ring. MINUS sections are
reflections of PLUS at magnitude u; both the index-step angle and the
footprint twist reverse.

For completeness, put \(b=a\sqrt{1+q^2}\) and
\(\delta=\arctan q\). The consecutive oriented determinants are

\[
\det(S_i,D_i)=\frac{\sqrt3}{2}(\lambda b)^2+
\lambda(1-\lambda)ab\sin\delta,
\]
\[
\det(D_i,S_{i+1})=\frac{\sqrt3}{2}((1-\lambda)a)^2+
\lambda(1-\lambda)ab\sin\delta.
\]

They are positive throughout the interior section, also at delta=0.
The cyclic angular ordering within consecutive 60-degree orbit sectors
gives a simple star-shaped polygon; a common azimuth offset can be absorbed
in the sector origin. Thus the band is embedded, including the zero limit.
This reuses and explicitly extends the existing exact section proof; it
does not substitute a smooth surface for the polygonal one. Cap slices are
separate triangle fans in the disjoint upper/lower slabs and azimuth sectors.

All laws in this note are geometric deformation identities. They do not
describe time, a trajectory, flow or a physical field.
