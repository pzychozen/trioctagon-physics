# Twisted Hex Crystal: final bounded family analysis

Date: 2026-09-25. Author of this analysis and execution: Codex, under Hilmir's
explicit work order preserved as `WORK_ORDER.txt`. This is new mathematical
analysis of the existing candidate, not recovered historical mathematics or
a new independent Claude review.

The entire research object is retained. The host admits a continuous family;
several members satisfy explicit additional geometric conditions. Those
conditions select different values. None is an author choice, a host-imposed
choice, a physical optimum, or a replacement for visual selection.

## Controlling evidence and definitions

The source of coordinates and faces is the unchanged parent
`verify_host_registration.py`, functions `canonical_points` and
`candidate_faces`, read together with `CANONICAL_CRYSTAL_CANDIDATE.json` and
`HOST_GEOMETRY.json`. The latter records its exact accepted Paper C and kernel
geometry source identities. This analysis imports these functions without
calling either original build. It preserves four distinct records:

| Record | Status |
|---|---|
| HISTORICAL_AUTHOR_INTENT | Hilmir's intuitive 3-up/3-down object and confirmed highest-horizontal-edge contacts |
| HISTORICAL_AS_CODED | Original source and reconstructed intersecting face list, unchanged |
| CURRENT_CANONICAL_FAMILY | Previously proposed clean open annulus, with explicitly new ring and face rules |
| VISUAL_RESEARCH_TOOL | Existing nine-sample atlas and offline viewer, unchanged; no member or hand selected |

Here “canonical family” names the existing candidate record; it does not
designate a canonical value of its free parameter. Its ring rule remains a
new assumption not forced by the six contact conditions. Its embedded mesh
is a proposed research surface, not a kernel adoption.

All formulas below use centered physical width-one host coordinates. Set

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,\quad
a=d/2,\quad h=s/2,\quad H=1/2,\quad U=s/2.
\]

The signed domain is \(-U\le t\le U\); write \(u=|t|\), \(q=u/r\).
Canonical-coordinate lengths are twice physical lengths and areas four
times physical areas. Heights stay fixed; no parameter is time.

## Results

The lower footprint is an isotropic dilation by
\(\sqrt{1+(t/r)^2}\) followed by rotation \(-\arctan(t/r)\).
The inverse contraction has \(\alpha=1/\sqrt{1+(t/r)^2}\).
All upper contacts stay fixed and all lower contacts remain exactly on their
specified host edges. Signed reflection exchanges the hands.

Corresponding-index interpolation has the requested polar law
\(I-\lambda(t/r)J\). That law is not the cross-section of the actual
shifted-index triangulation. Its actual intermediate section has two
six-point orbits, generally forming a star-shaped 12-gon. The distinction is
proved in [SIGNED_FAMILY_IDENTITIES.md](SIGNED_FAMILY_IDENTITIES.md).

The six-contact skeleton has explicit side, spoke and cross-diagonal
lengths, right triangles, and an odd determinant \(-rt\). These are
ordinary geometric invariants; no enclosed-volume or physical meaning is
assigned to the annulus. Complete formulas appear in
[METRIC_FUNCTIONS.md](METRIC_FUNCTIONS.md).

There are eight edge-length functions and four face-area functions for the
specified triangulation. Exact, bounded comparisons give:

| Condition | Positive magnitude; both signs are included |
|---|---:|
| Minimum of the specified triangulated surface area | 0.026934166314686... |
| Equality of band-diagonal and cross-strut unoriented plane angles | 0.025433046570630... |
| Cross-ring strut equals lower apex-to-outer-ring edge | 0.197797486048842... |
| Footprint angle equals the existing octagonal half-angle \(\pi/8\) | \(r(\sqrt2-1)=0.119573155869...\) |

The area minimum is unique for the magnitude parameter and gives two
mirror members. The angle root satisfies \(48u^3-28u^2+40u-1=0\).
The edge equality satisfies a quadratic over the radical coefficient field.
Each is defined or rigorously isolated in
[SPECIAL_MEMBER_SEARCH.md](SPECIAL_MEMBER_SEARCH.md) and its JSON companion.
The last equality is an external named-angle comparison, not an internal
contact constraint. No triangle-area equality occurs at positive magnitude;
no whole-surface equi-edge/equi-area member occurs even at zero. Every
six-face area orbit is of course equal internally for every member, by the
already imposed symmetry.

At zero, the vertex set has \(D_{3h}\) symmetry (order 12), while either
inherited face complex has chiral \(D_3\) symmetry (order 6). Its triangles
are nondegenerate; no two whole triangles are coplanar. The zero mesh is
embedded. The two reflected face lists have different geometric supports at
zero, so the prescribed mirrored surface family does not join continuously
there. Vertices do. Holding one face list fixed gives a local continuous
embedded deformation through zero, but its negative side is not the
prescribed mirror surface. See [ZERO_STATE_ANALYSIS.md](ZERO_STATE_ANALYSIS.md).

At one fixed full-height axial pitch, copies have no joins for nonzero
magnitude and only three isolated apex contacts at zero. No boundary loops
match. The test does not classify other pitches or invent a lattice; see
[STACKING_EXPLORATION.md](STACKING_EXPLORATION.md).

## Relation to standard forms

These are invariant comparisons, not historical identifications or novelty
claims. At zero the *nine-edge six-apex skeleton* is the edge graph and
geometric realization of a right equilateral triangular prism. At nonzero
magnitude the two apex triangles have unequal size and a relative rotation;
it is not a translated congruent-base prism. Calling that skeleton
“twisted-prism-like” does not identify the 18-vertex surface with a prism.

The actual mesh has vertices on four levels, 24 triangles, 42 edges and two
six-edge boundaries. It is an open triangulated annulus, not a closed
antiprism or a two-plane convex prismatoid. Its band alone has vertices on
two planes, but that does not prove equality with the convex hull surface.
Affine corresponding-point rulings are a separate interpolation scaffold;
they are not the inherited band's triangulation. No permanent new formal
name is needed.

## Verification and limits

`family_exact_checks.py` imports the preserved geometry and independently
derives direct vertex metrics, reflections, section identities, pair-root
tables, zero symmetries and an exact separating witness. Exact algebraic
root isolation and rational outward square-root intervals support the root
claims. Positive Bernstein coefficients prove strict area convexity over
an interval containing the admitted domain. A numerical all-triangle-pair
intersection check at zero supplements, and does not replace, the section
and cap proof. `family_validation.json` records the actual predicate count;
that count is bookkeeping, not a theorem count.

No recurrence runs, kernel edits, parameter sweep, host edits, historical
repairs or accepted-paper changes are used. Previously generated execution
logs and viewer QA retain their earlier attribution and limitations. The
HTML browser-layout check was not newly certified in this task.

`PRESERVATION_BEFORE.json` pins the starting 589 tracked and 2237 untracked
files, including the 60 existing files in this lane. Publication preparation
compares all of them byte-for-byte and verifies both pre-existing lane hash
manifests. New verification output is kept in this subfolder. Publication
status is governed by the separate receipt, not inferred from these local
saves. A whitespace failure requires a stop with no normalization or new
exception.

## Freeze disposition

```text
TWISTED_HEX_RESEARCH_OBJECT = PRESERVE
SIGNED_FAMILY_DERIVED = YES
CROSS_SECTION_LAW_DERIVED = YES, WITH INTERPOLATION/MESH DISTINCTION
ZERO_STATE_CLASSIFIED = YES
DISTINGUISHED_t_FOUND = YES, UNDER THE EXPLICIT CONDITIONS ABOVE
NO_INTRINSIC_t_SELECTION_FOUND = NO, IN THAT LIMITED MATHEMATICAL SENSE
HOST_OR_AUTHOR_SELECTED_t = NONE
ANY_VALUE_DESIGNATED_PREFERRED = NO
ANY_HANDEDNESS_DESIGNATED_PREFERRED = NO
SIMPLE_AXIAL_REPEAT_FOUND = NO, FOR A JOINED REPEAT AT THE TESTED PITCH
FAMILY_PHYSICAL_INTERPRETATION = NOT_ESTABLISHED
RUNTIME_KERNEL_ROLE = NONE
GEOMETRICAL_FORM_SEARCH = CLOSED_AFTER_THIS_ORDER
```

The “NO” in `NO_INTRINSIC_t_SELECTION_FOUND` records actual conditional
geometric special members. It does not assert a unique natural or mandated
selection. The continuous family and visual-selection tool remain useful
in their entirety, independently of these special values. No further form
search or implementation packet follows from this closeout.
