# GPT review — NCM-FIXED-GAP-01 v0.1

**Date:** 31 October 2026  
**Disposition:** ACCEPTED as a bounded, conditional geometry investigation. No blocking mathematical repair identified. This does not accept a material-motion law, determine the author's remaining attachment, amend a paper, or authorize publication.

## 1. Reviewed input and scope

Reviewed the supplied REPORT.md, the complete NCM_FIXED_GAP_01_v0.1_REVIEW.zip, scripts, retained coordinate/source definitions, decision matrix, provenance correction, three PNG figure sheets, and associated verification records.

Input ZIP SHA-256:

`926b77316ce7ffe19b2e91a51239caa25683d6e5b02b2d2a1e64483e629bde30`

Report SHA-256:

`bc43cadd16d4235cda17fc42f082e5fa6fe579158ac3ed9ad779687fb4ec9da8`

The report reconstructs the accepted folded host and the separately declared refined central-surface family. It does not identify that refined family as uniquely forced by the host. The stationary supports in its figures are conditional reference/attachment cases, not recovered physical rods.

## 2. Mathematical assessment

### Source reconstruction and angles

The transcription agrees with the retained central source's coordinate and face definitions. The refined meshes have 18 vertices, 42 edges, and 24 triangles; their 12 boundary edges form the six specified two-edge opening arcs. Central opening arcs, filled host-notch measurement triangles, material host panels, and earlier cone proxies remain distinct.

The reported 120-degree separation concerns distinct same-level azimuth bisectors. The 60-degree value concerns the smaller angle between the corresponding unoriented lines. Neither is a new native phase-sector result.

For the two edges of ONE upper opening, use c=r/2-a, b=sqrt(3)r/2=1/4 and vertical rise d. The two spatial vectors have coordinates (c,+b,d) and (c,-b,d) in an orthonormal local basis. Their dot products give the printed formulas directly:

- Top projection: approximately 179.03330923891456 degrees.
- Spatial angle: approximately 80.96358603511995 degrees.

This is a real projection effect. It is not evidence that two distinct openings are nearly opposite, nor that the author's sketch has been identified metrically. No additional sketch measurements are needed or justified by that calculation.

### Stationary line and center

For a centered proper rigid transformation R, preserving a stationary line L=span(ell) as a set requires R ell=+ell or -ell. The plus component consists of rotations about that line. The minus component consists of half-turns about perpendicular axes. A continuous path starting at identity and preserving that same line throughout cannot switch components.

Consequently a quarter-turn ABOUT a fixed support is compatible with one attached line; a quarter-turn that TILTS the support is not. This is purely kinematic and does not specify a rate, force, clearance, or allowable path through fixed surrounding material.

Two nonparallel pointwise-fixed support lines leave only identity. For named nonorthogonal line loci, the only alternatives are identity and the half-turn about their common normal. The report correctly distinguishes these constraints from permuting a collection of lines. An endpoint symmetry is not automatically a permitted continuously constrained path.

For identical same-hand, same-tau copies, a common support-compatible rigid transformation transports all attached features together. Independent movement of every gap is not inherently necessary. This assertion is conditional on the relative pose and attachment constraints; it is not a proof that every arbitrary pose can be registered with fixed supports.

### Relative upper/lower geometry

The lower planar transformation is A_tau=I-xi J, xi=tau/r, so A_tau^T A_tau=(1+xi^2)I. It contains a rotation -atan(xi) and a dilation sqrt(1+xi^2), rather than a pure rotation.

At tau=h the offset is approximately 35.65712982473279 degrees. A common axial rotation adds the same angle to both levels and cannot remove their relative offset. The report's general plane-preservation argument also excludes curing both directed-triad registrations by a favorable common tilt.

The invariant sum of squared centered distances of the 12 distinct boundary vertices is

`M(xi)=M(0)+3(a^2+r^2)xi^2`.

Its strict increase on positive xi proves that distinct nonnegative tau members are not centered rigid poses of one fixed boundary. The report correctly treats them as static members of a geometric family, not frames of an evolution supplied by the native equations.

This does not mean six independent motions are required to change the relative geometry. A coordinated lower-level change would already alter it, but it would change connecting faces and is not a motion defined in the accepted fixed mesh.

### Hands, contacts, and finite regions

The proper boundary symmetry classifications are consistent with the distinguished tip radii and vertical covariance: C3 for positive tau, D3 at zero. The report does not confuse same boundary sets with same full triangulated surfaces. At zero, the two hands share their boundary sets but differ in band connectivity. Positive-tau opposite hands cannot be properly registered by the admitted centered rotations; reflection remains a different operation.

The radial comparison between any central ring elbow and any host-notch plane is strict over the admitted interval. It excludes placing an ENTIRE central boundary arc into a notch patch by a centered rotation. It does not exclude the source-defined fan-tip contacts at tau=h, which the contact checker verifies explicitly.

The six central arcs share vertices. The accepted mesh supplies no operation for independently rotating each arc while holding all adjacent geometry fixed. No aperture interior, centroid, hinge, or motion law should be added merely to make such a test possible.

## 3. Interpretation that must be retained

- Blue and orange in the figure sheets identify upper and lower arcs of one refined case, not the author's two green/orange whole-model arrangements.
- The top sheet uses conditional planar support lines. The side sheet uses a conditional vertical support. These are alternative attachment cases, not all constraints applied simultaneously.
- The zero and endpoint shape cases are not successive times. Tau is not the native update index or observer time.
- Looking from the opposite side changes projection, not object identity or three-dimensional registration.
- The fixed support is accepted as author intent. Which source feature is attached to it is not uniquely specified by stationarity alone. The report legitimately gives conditional answers rather than inventing that attachment.
- Correcting the earlier moving-axis interpretation does not invalidate the independently proved native coherence/phase bounds. It also does not make those bounds a verified description of the fixed-support geometry.

## 4. Reproduction performed in this review

A fresh sandbox replay directory received byte-identical copies of `geometry_model.py`, `check_geometry.py`, `check_contacts.py`, and `PLAN.md`. Only these NEW static-geometry checkers were run. No native recurrence, observer, previous solver/certificate, repository geometry module, Git command, or application was executed.

Commands:

```text
python -X utf8 -I -B check_geometry.py
python -X utf8 -I -B check_contacts.py
```

Results:

- 104/104 supplied geometry predicate groups passed.
- 7/7 supplied contact/symmetry groups passed.
- All six substantive output JSON documents match the supplied counterparts exactly as parsed JSON: geometry coordinates, gap table, feature-ray angles, symmetry actions, numerical/exact results, and contact results.
- The main checker results also match apart from two metadata fields: Python version and UTC timestamp.
- The scripts and plan were unchanged.
- Review environment: Linux, Python 3.13.5, SymPy 1.14.0. This is not a second Windows certification.

Fourteen additional reviewer checks, written independently of the submitted geometry module, corroborate the printed local edge formulas, similarity identity, norm invariant, radial separation, and sample line actions. They evaluate only static symbolic identities. These counts support verification; they are not counts of independent theorems and do not replace the written arguments.

A first attempt to request a streaming container session was rejected by the environment before replay logs were created. The ordinary non-streaming execution above completed successfully. No scientific failure was waived.

## 5. Package and preservation evidence

The ZIP has 63 members. All 62 files listed by `OUTPUT_HASHES.json` match their listed byte sizes and SHA-256 values; the remaining member is the manifest itself, which intentionally does not hash itself. The separately uploaded report is byte-identical to REPORT.md in the ZIP.

The two separately uploaded overview PNGs are smaller renderings than the packaged images (2047-pixel width versus 3060). They are not byte-identical archive evidence. The archive originals were inspected for this review and retained unchanged. All three original PNG sheets were inspected, including the one-opening projection comparison.

The 140 before/after preservation records agree internally, including the separate before snapshot. Live Windows source paths were not available here and were not re-certified. Hash integrity does not independently establish authorship or execution history.

The received discussion-sketch mismatch is disclosed and does not affect the mathematical predicates. No pixel-derived angle or length enters the geometry.

## 6. Disposition and next-step boundary

Accept the report as a completed geometry-only investigation. No repair order is needed for its principal conclusions. It establishes when common rigid alignment is compatible with specified supports, why some whole-object turns cannot repair an internal twist, and how projection changes apparent angles.

It does not establish that the model dynamically performs any allowed rotation. It also does not require six independent gap motors, demonstrate an energy-emission direction, or choose a hidden central toroid.

No further author explanation is required to accept this report. A more specific mechanical claim would require a feature-to-support attachment or a correspondence supplied by existing model definitions. That missing choice should not be confused with another request for a complete imaginative motion story. No successor experiment, new motion law, paper, or publication is authorized by this review.
