# Zero state: vertices and surface are different questions

At t=0, alpha=1 and delta=0. The lower ring aligns with the upper ring and
the three lower apices align vertically with the upper apices. There is
no strict contraction or footprint twist. The inherited shifted-index
band triangulation remains present; this analysis does not repair it.

## Exact symmetry groups

The covariance axis is distinct even at zero, so every Euclidean symmetry
preserves the vertical axis, possibly reversing it. Ring and apex levels
remain distinguished. The aligned equilateral apex triangles restrict the
horizontal action to D3. Combining these six horizontal actions with the
two height actions gives exactly D3h, order 12, for the vertex set. The
script constructs and checks all 12 exact vertex permutations, not a
numerical search over candidate rotation angles.

Only six operations preserve the actual triangle set F_plus: three axial
C3 rotations and three half-turns combining a horizontal reflection and
height reversal. All have determinant +1. Thus its Euclidean face-complex
symmetry is D3, order 6, with no improper isometry. F_minus has the conjugate
group and the same conclusion. Because no whole triangle pair is coplanar
and all actual folds remain visible, these are properties of the surface
itself, not merely of invisible diagonal markings on planar faces.

The zero vertex set is achiral. Each zero surface is still chiral.
Consequently zero does not erase the surface's handed connectivity.

## Degeneracy, coplanarity and embedding

All 24 triangle areas are strictly positive at zero. Exact cross-product
and plane tests over all 276 distinct triangle pairs find **no coplanar
whole triangle pair within either mesh**. This does not say that pieces
of opposite-hand meshes cannot occupy a common plane or overlap.

At an interior band height, the exact consecutive determinants specialize
to sqrt(3) a^2 lambda^2/2 and sqrt(3) a^2 (1-lambda)^2/2, both positive.
The interleaved six-point orbits trace a simple star-shaped 12-gon. At the
end levels it collapses only to the existing six-edge ring, not to a
degenerate triangle. Cap fans stay in their own upper/lower slabs and
three angular sectors. They meet the band along their prescribed ring
edges. This proves embedding including zero. The supplementary numerical
all-pair test found 0 unexpected intersections among 276 pairs at tolerance
1e-10; it is explicitly a numerical cross-check of the exact argument.

## An exact witness that the two limits differ

Use the common signed labels from `SIGNED_FAMILY_IDENTITIES.md`.
The point

\[
W=(2T_0+5T_1+11B_2)/18
=\left(\frac{\sqrt3(2-\sqrt2)}9,
\frac1{36}-\frac{\sqrt2}{72},\frac{1-\sqrt2}9\right)
\]

is strictly inside F_plus face 0, (T0,T1,B2). Exact plane and barycentric
membership tests put it in **none** of the 24 F_minus triangles. In the
only containing plane among those triangles, the barycentric coordinate
X=-10/9 is negative, so that plane's triangle does not contain it.
The two limits are therefore distinct closed subsets of space. The
centroid of face 0 would not be a valid witness: it happens to belong to
both surfaces. The final certificate uses W and records its exact values.

## What can pass through zero continuously?

All 18 signed vertex positions vary affinely through zero. Their nonzero
sets have opposite chirality and their common zero set is achiral:

```text
VERTEX_SCAFFOLD_CONTINUITY = YES
VERTEX_CHIRALITY_REVERSAL = YES
ZERO_VERTEX_SYMMETRY = D3h, ORDER 12
ZERO_FACE_SYMMETRY = D3, ORDER 6, FOR EACH HAND SEPARATELY
```

Keeping **one** face list fixed makes every triangle vary continuously.
There is a local embedded deformation through zero: the finite zero
triangulation is embedded and nondegenerate, disjoint simplices have
positive separation, and incident noncoplanar faces have separated local
links. Sufficiently small vertex perturbations retain these properties.
No full negative-interval embedding theorem for this separate fixed-list
extension is asserted or needed here.

That local extension is **not** the prescribed mirrored family: the latter
uses F_plus on positive t and its reflected F_minus on negative t in the
common labels. Its two zero limits differ by W, so no assignment of one
zero surface makes it continuous. Continuing fixed F_plus through zero
does not reverse the zero surface's chirality. This is why a local
fixed-connectivity deformation and a mirror-to-mirror passage must not
be conflated.

```text
FIXED_FACE_LIST_LOCAL_EMBEDDED_CONTINUATION_THROUGH_ZERO = YES
PRESCRIBED_MIRRORED_SURFACE_FAMILY_CONTINUOUS_AT_ZERO = NO
SURFACE_CHIRALITY_REVERSAL = NO, FOR THE PRESCRIBED MIRRORED FAMILY
ZERO_VERTEX_HANDEDNESS = UNDEFINED / ACHIRAL
ZERO_FACE_HANDEDNESS = STILL_DEFINED / CHIRAL
```

No connectivity was changed in the candidate or atlas, and neither hand
was selected. The shared zero object is a vertex scaffold reference, not
a newly achiral common face mesh.
