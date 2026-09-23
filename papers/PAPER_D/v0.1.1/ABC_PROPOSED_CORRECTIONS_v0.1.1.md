# Paper A/B/C: proposed consistency clarifications for GPT review

Codex, 23 September 2026. This is the bounded follow-through requested by §8 of the supplied GPT Paper D review. It compares the **actual current publication manuscripts, generated TeX and published PDFs** at repository HEAD `08c2a79739d540ffe1cab4743284052e2aa7214b`. Their hashes and matching commit-blob identities are in `evidence/abc_inspected_artifacts.json`. No A/B/C file has been edited or recompiled. This is a dependency/wording assessment, not a new global referee certification of those papers.

The canonical compact impact table is appended to the existing `reconstruction/continuity_closeout_20260922/PROJECT_STATUS_RECOVERY.md`, in the entry **2026-09-23 - Paper D v0.1.1: GPT review follow-through and A/B/C consistency impact**. This companion contains the exact proposed prose, keyed to that table; it is not a new master status record. Page locators below are one-based published-PDF pages and agree with printed numbering.

## Paper A - unchanged

**Inspected edition:** *Cycle-Covering Dynamics of a Three-State Nonlinear Kernel*, publication v1.0, 19 pages, frozen scientific manuscript v0.5.1. The exact graph definitions, covering and nonlinear pull-back statements are on pp. 2, 4-9 (§§1-6); the feedback criterion and limitations are on pp. 15-16 (§§10, 12).

No correction is proposed. These statements use graph incidence, residue classes, specified coefficients and the shared zero-amplitude convention. They do not assume a spatial regular hexagon, reference-corner cell, welded octagon or gap length. The recurrence coefficient `g` is not Paper D's geometric `g_gap`. The existing §12 already excludes physical interpretation; §10 already calls its feedback result sufficient and distinguishes it from a physical portal result. The different geometries in D do not change any of these hypotheses or justify rerunning the stability atlas.

## Paper B - two scope/citation clarifications

**Inspected edition:** *Triadic Chirality and Orientation Geometry*, publication v0.1.1, 13 pages. Retain all equations, propositions, theorems, figures and parameter/zero-stratum qualifications.

**B-S1. Insert after §1's paragraph beginning “The geometry is the width-one folded shell of [PC]” (p. 1; that paragraph already specifies the selected carrier).**

> The carrier used here is the particular welded realization of Paper C. The author-clarified reference-scaffold concept permits octagons to supply geometric references without requiring a connected material shell; its aligned six-segment construction is developed separately in Paper D, Sections 4-14. The placements and figures in the present paper remain those of Paper C. Paper D's regular measurement member and fixed-centre shrink are not additional placements adopted here.

**B-S2. Append to §4's final paragraph, after its existing denial of a physical connection or seam-continuity condition (p. 5).**

> The encoding and transport identities (6)-(10) depend on the specified orthonormal frames and their matching, rather than on a seam field law. Paper D's separation of finite faces therefore does not invalidate these identities on their stated vector spaces. Changing a carrier or its centres would still require an explicit placement and point-attachment choice: a free-vector identity alone does not transfer the centres, figures or surface topology to another realization. No such change is made here.

In B-S2, “does not invalidate” is conditional on retaining the stated frames and matching; it is not a proof that arbitrary new frames obey the original spatial symmetry formulas. In particular, §7's spatial action still requires the specified group to carry normals and face labels as stated. The unmarked planar hexagon's `D6` is not silently substituted for the shell's `D3h` or its channel action.

**Leave unchanged:** §§6-9 and 11 (pp. 7-11) already distinguish transported state-vector areas from material areas, channel chirality from an ambient axial vector, and the specified recurrence from physical field, seam and boundary laws. The existing wording “has no imposed decay envelope; it need not decay” remains correct. A display assignment of channel numbers to coordinates in Paper D supplies no additional physical position or energy identification.

## Paper C - three scope/citation clarifications

**Inspected edition:** *Exact Geometry of the Folded Tri-Octagon Module*, publication v1.0, 16 pages, frozen scientific manuscript v0.3.1. Retain every coordinate, metric, theorem and mesh count.

**C-S1. Insert after the first paragraph of §1 (p. 2), which already defines this object as three zero-thickness octagonal panels welded along vertical hinges.**

> This welded realization is one specified geometric object within the broader Tri-Octagon research. The author's later reference-scaffold clarification does not require the octagons to form a connected material surface. Paper D formalizes that reference construction and its conditional coordinate comparison with the present module. The definitions and proofs here continue to concern the welded surface fixed by Sections 2-4.

**C-S2. Append to §8's “Rim decomposition (curve vs enclosed region)” paragraph (p. 11), after the existing distinction between virtual measurement regions and mesh/cap faces.**

> In Paper D's aligned measurement family, these six high vertices give the member with connector length `g_gap = d = s/sqrt(2)`. Its equiangular hexagon has alternating lengths `s,d` and is not the equal-sided member. Paper D, Sections 12-14, distinguishes that planar measurement polygon from this nonplanar nine-edge rim and describes two changes that reach the equal-sided member. Neither is a common rescaling of this welded module. In the fixed-vertical-face-centre shrink of the original width-one module, the six measurement sides become `1/3`, the octagon width becomes `(1+sqrt(2))/3`, and the top height becomes `(1+sqrt(2))/6`; the original seams are lost. Those consequences do not change the width-one definition, rim or mesh of the present paper.

This is a cross-reference to the already accepted derivation, not a new construction or an instruction to modify C. The existing §8 already correctly calls the hexagon **equiangular** and the filled regions virtual. Its area partition subtracts areas; it does not define a residual set by deleting only open triangle interiors. Paper D's D-02 correction therefore does not expose the same set-definition error in C.

**C-S3. Insert after §9's symmetry proof and its scope paragraph (p. 12), before §10.**

> The upper-bound argument above uses the three intrinsic crease components of the welded surface. It therefore remains tied to that surface and is not transferred by name to separated panels or reference frames. Paper D, Section 10, distinguishes the `D6` symmetry of an unmarked regular planar hexagon from its `D3` edge/connector-role symmetry; these are symmetries of different objects from the welded surface studied here.

**Leave unchanged:** §2's regular octagon and local coordinates (pp. 3-4), §5's full-edge closure and annulus proofs (pp. 7-8), §6's triangular-perimeter sections (pp. 8-9), §8's spatial/projection angle distinction (pp. 10-11), and §9's `D3h` theorem (p. 12). C already uses filled polygonal faces in §5 and explicitly convex hulls in §9. Its phrase “fixed centre” in §3 (p. 4) means holding the middle panel fixed during the specified hinged construction; it is not Paper D's simultaneous fixed-centre shrink of all three faces.

## Review boundary

These five proposed additions are **scope/citation clarifications**, not mathematical revisions or changes already applied. No inspected claim requires a mathematical revision as a consequence of the clarified definition. New placements would change the hypotheses of C's seam/topology arguments, not refute the existing statements. Paper A's dynamics, Paper B's declared tangent observable and the accepted SRG reduction/orientation cycle remain intact. The boundary-response interpretation and exact Z-to-gap registration remain unresolved at their existing scopes. References to Paper D should identify the reviewed final edition if and when GPT approves it; v0.1.1 is presently submitted for review.
