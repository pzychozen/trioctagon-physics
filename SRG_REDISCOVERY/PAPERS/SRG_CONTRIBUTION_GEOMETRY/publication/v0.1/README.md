# SRG Contribution Geometry
## Exact Prefixes, Carry Lattices, and Neighboring-Pair Transformations

**Hilmir Frímann Halldórsson — v0.1 — 13 October 2026**

Manuscript and exact twelve-file publication candidate awaiting GPT manuscript-and-payload review. PH04's underlying analysis is accepted within its declared mathematical scope; that internal acceptance is not acceptance or publication of this new paper.

[Read the manuscript](SRG_CONTRIBUTION_GEOMETRY_v0.1.pdf) · [Editable LaTeX](manuscript/SRG_CONTRIBUTION_GEOMETRY_v0.1.tex) · [Exact-data guide](data/README.md)

The paper starts with the actual raw contributions **0.48, 0.508 and 0.1704** in the factor-labelled master multiplication. Using two neighboring summands as the segments of a circle diameter makes three operations visible:

- A legal elementary carry preserves their sum and circle radius, while its integer lattice generally changes their product.
- Reciprocal scaling preserves the product and can deliberately balance the lengths.
- Moving to the next overlapping pair follows an exact scale-plus-reciprocal law, generally changing the invariant product.

Complete proofs cover raw-prefix permanence, the legal balance condition, positive-block telescoping, the unique global raw maximum at depth 3, and the universal canonical-adjacent imbalance bound 1/19. The saved scan through 64 input places supplies precisely delimited finite rankings and zero cases. It does not establish an infinite closest-pair theorem. No physical dynamics is introduced.

## Contents and reading

The PDF has 20 pages, 45 numbered equations, four accepted figures and six formal theorem/proposition statements. Three figure pages are landscape so the original legends remain readable. The LaTeX depends only on its four declared relative PNG paths and standard typesetting packages; it uses no shell escape, absolute-path runtime dependency or standalone font.

The exact candidate has twelve paths: PDF, TeX, this README, SOURCE_INDEX, CLAIM_SOURCE_LEDGER, EVIDENCE_SUMMARY, four PNG files, the data README, and one data ZIP. The [source index](SOURCE_INDEX.md) identifies inherited sources; the [claim ledger](CLAIM_SOURCE_LEDGER.md) distinguishes definitions, general deductions, finite facts and conditional interpretation. The [evidence summary](EVIDENCE_SUMMARY.md) records the limits of the accepted arithmetic and this preparation.

The [data ZIP](data/SRG_PH04_EXACT_TABLES_v0.1.zip) contains exactly seven original PH04 JSON files. They and all four PNGs are byte-identical to the accepted artifacts. The data guide maps their retained original report locators to this manuscript. No accepted checker was rerun.

## Editing and building

Run the existing Tectonic compiler from the manuscript directory using the arguments: -X compile --untrusted SRG_CONTRIBUTION_GEOMETRY_v0.1.tex. For a fully cached installation add --only-cached; this edition was built using the existing cached compiler without installing packages. A reviewer may direct build products to a separate review folder. Neither the exact-data ZIP nor any historical program is executed to typeset the paper.

## Authorship, scope and reuse

Hilmir Frímann Halldórsson is the human author. GPT assisted with mathematical proposals and scientific review; Codex performed the accepted PH04 analysis and prepared this exposition, source records and artifact QA under the author's direction. These tools are not coauthors.

This separate follow-on preserves SRG-I, Origins, the preceding multiplication manuscript and the reserved SRG-II scope. No new blanket reuse licence is granted. Software licensing is not extended to research; existing source-specific notices remain with their sources. The proposed data supplement does not itself assign or expand a licence.
