# Paper II v0.1 — access, reproduction and evidence

## Included in this repository edition

- The [accepted PDF](PAPER_II_PAIRED_DRIVING_EXTERIOR_IDENTIFIABILITY_v0.1.pdf), [main TeX entry](manuscript.tex) and eight companion TeX files; all nine sources and the PDF retain their accepted bytes.
- Five computed figure sets under `figures/` (PDF, PNG and SVG), their `FIGURE_DATA_LEDGER.json`, six data files and `data/SOURCE_INDEX.json`.
- Three standalone manuscript-reproduction helpers and a [portable guide](BUILD.md). Their file I/O closure is within this selected edition. They do not depend on private manuscript inputs or import either project kernel.
- [Source-asset identities](SOURCE_ASSET_INDEX.json), [edition manifest](PUBLICATION_MANIFEST.json), [checksums](SHA256SUMS.txt) and the [publication disposition](PUBLICATION_DISPOSITION.md).

The inherited geometric predecessor is [Paper I v0.1.1](../../../PAIRED_GAP_GEOMETRY_OBSERVATION/publication/v0.1.1/README.md), published at commit `88ee0550f851507c159f4443c999b6f3ae39097d`. The unchanged manuscript bibliography provides its commit-pinned repository URL. This guide does not promise that later changes to a moving branch reproduce an older edition.

## What is retained privately rather than published here

The original SRG-05–08 reports, their historical work orders, internal GPT reviews, full source snapshots, selected-claim ledger, manuscript development logs, all-page review records and Git/preservation measurements remain owner-side review evidence. Bibliographic entries describing these as unpublished retained sources are accurate. Repository publication of this paper does not publish every cited private source or grant unrestricted reuse of them.

`data/SOURCE_INDEX.json` binds the six included data copies to their original private-review-relative `source` locators. Those locators are provenance strings, not public links or executable requirements. `SOURCE_ASSET_INDEX.json` likewise identifies selected source members without pretending the entire private archive is an included public supplement. Every actual `\input`, `\includegraphics` and the three reproduction helpers' data dependencies is supplied.

No rough sketch, private chat export, private review ZIP, user-account path, credentials, font file, compiler or cache is selected for publication. Native code is discussed mathematically, not installed by this edition. The generic Windows system-font fallback in the unchanged optional build helper is not a private-account path or a bundled font.

## Evidence and scope

The final internal review accepted the 33-page supplied artifact, 18 mapped claims and all 26 manuscript-local checks, with no required revisions. The check counts and page review are retained evidence, not new executions performed to publish this directory. Full proofs control the universal mathematical claims; finite numerical summaries retain their stated non-interval qualifications.

Author authorization permits publishing this edition after internal review. It does not establish external peer review, empirical physical validation, algorithmic/quantum advantage, a DOI, an affiliation or a new license. Publication CI concerns the repository distribution checks, not peer review of the paper.

Only the [existing software-license scope](../../../../../LICENSE_SCOPE.md) applies as already stated by the repository; the scientific material is not automatically Apache-2.0 licensed.
