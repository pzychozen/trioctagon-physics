# Exact five-item publication change record

23 September 2026. Codex follow-through to user-relayed GPT approval.

Approval SHA-256 `2607fb4cd3d799b27272ecc8e3d8be8504b360c0d688843b2a9d5758fb1a659b`; approved proposal SHA-256 `2092c59f3e75a03d436b268710f0b195ff83504dbb6944e7308cacec2233124d`. Paper A: no edit. D approved PDF: unchanged `7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf`.

The JSON [exact insertion record](evidence/five_approved_additions.json) retains every original anchor, the approved prose, the inserted prose and baseline source hashes. Only normal inline mathematical typesetting and [PD] citation markers alter the supplied passage formatting. Removing these five paragraphs and the new reference, reversing the version/figure-link and bibliography-navigation edits recovers both entire original manuscripts (apart from terminal whitespace).

## B-S1 - applied at B §1, pp. 1-2

> The carrier used here is the particular welded realization of Paper C. The author-clarified reference-scaffold concept permits octagons to supply geometric references without requiring a connected material shell; its aligned six-segment construction is developed separately in Paper D [PD], Sections 4-14. The placements and figures in the present paper remain those of Paper C. Paper D's regular measurement member and fixed-centre shrink are not additional placements adopted here.

## B-S2 - applied at B §4, p. 5

> The encoding and transport identities (6)-(10) depend on the specified orthonormal frames and their matching, rather than on a seam field law. Paper D's separation of finite faces therefore does not invalidate these identities on their stated vector spaces [PD]. Changing a carrier or its centres would still require an explicit placement and point-attachment choice: a free-vector identity alone does not transfer the centres, figures or surface topology to another realization. No such change is made here.

## C-S1 - applied at C §1, p. 2

> This welded realization is one specified geometric object within the broader Tri-Octagon research. The author's later reference-scaffold clarification does not require the octagons to form a connected material surface. Paper D [PD] formalizes that reference construction and its conditional coordinate comparison with the present module. The definitions and proofs here continue to concern the welded surface fixed by Sections 2-4.

## C-S2 - applied at C §8, p. 11

> In Paper D's aligned measurement family, these six high vertices give the member with connector length $g_{\mathrm{gap}}=d=s/\sqrt2$ [PD]. Its equiangular hexagon has alternating lengths $s,d$ and is not the equal-sided member. Paper D, Sections 12-14, distinguishes that planar measurement polygon from this nonplanar nine-edge rim and describes two changes that reach the equal-sided member. Neither is a common rescaling of this welded module. In the fixed-vertical-face-centre shrink of the original width-one module, the six measurement sides become $1/3$, the octagon width becomes $(1+\sqrt2)/3$, and the top height becomes $(1+\sqrt2)/6$; the original seams are lost. Those consequences do not change the width-one definition, rim or mesh of the present paper.

## C-S3 - applied at C §9, p. 12

> The upper-bound argument above uses the three intrinsic crease components of the welded surface. It therefore remains tied to that surface and is not transferred by name to separated panels or reference frames. Paper D [PD], Section 10, distinguishes the $D_6$ symmetry of an unmarked regular planar hexagon from its $D_3$ edge/connector-role symmetry; these are symmetries of different objects from the welded surface studied here.

## Publication-only changes and retained science

Both editions add [PD], naming the author, full D title, v0.1.1, date and resolvable approved PDF target; no DOI or journal is invented. Companion reference files reproduce their respective complete reference sections.

B uses publication revision v0.1.2. Five figure references acquire `../../` to reuse the existing assets from the nested publication folder. Its builder and style are byte-identical copies of the existing publication workflow; only revision configuration/runtime location changes. No figure assets are copied into the new edition.

C uses publication revision v1.0.1, preserving scientific baseline v0.3.1. The existing Pandoc/TeX adapter reads the retained publication source, accepts [PD], uses explicit existing tool/cache paths and labels the new edition. The bibliography introduction distinguishes existing background sources from D's new comparison, with a descriptive link to the unchanged bibliography. The Appendix A forced page break becomes a space requirement, and the reference block uses 10/12-point typesetting to avoid almost-empty spillover pages. The original equation wrappers, two long-expression line breaks and three table widths remain. C's inherited display block 8 is scaled by the same roughly 0.981 factor as before; no additional equation scaling is introduced.

The new bounded checks recover every original theorem/proposition statement, proof body, measurement, parameter convention and equation from the revised manuscripts. B retains 26 numbered displays and seven statement labels; C retains 28 display blocks and seven theorem labels. B's five figure groups and C's existing tables/assets are unchanged. Existing historical test counts and supporting implementation identities remain prior evidence, not rerun results. Page/annotation/layout checks are publication checks, not independent new proofs.

## Evidence and remaining review boundary

See [bounded verification](evidence/bounded_verification.json), [visual QA](evidence/visual_QA.json), [isolated reproduction](evidence/isolated_reproduction.json) and [preservation/Git receipt](PUBLICATION_RECEIPT.md). GPT's acceptance of D and approval of these five passages do not certify the final B/C PDF bytes or the local execution/package checks. Those new results are separately attributed to Codex. No new mathematical review, Claude investigation or scientific campaign was performed.
