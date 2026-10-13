# Source index — SRG Contribution Geometry v0.1

13 October 2026. The manuscript supplies its own complete proofs. The exact supplement supplies the finite records; this index identifies their accepted provenance.

## Source IDs and exact locators

| ID | Source and status | Locations used |
|---|---|---|
| S1 | SRG-PH04 REPORT.md, accepted private mathematical report | §1 lines5–62 pair geometry; §2 lines63–145 carries and reciprocal action; §3 lines146–203 product/prefix; §4 lines204–268 neighboring pairs; §5 lines269–322 finite scope; §6 lines323–415 certification/execution; §7 lines416–467 three findings; §8 line468 onward interpretation. |
| S2 | SRG_PH04_GPT_SCIENTIFIC_REVIEW_20261013.md, internal assisted scientific decision | §§2–7 verify geometry, prefixes, carries, transition, certification and findings; §8 artifact/failure history; §9 acceptance and bounded manuscript task. Required scientific revisions: none. Not external peer review. |
| S3 | SRG_PH02_MULTIPLICATION_GEOMETRY_01/REPORT.md, accepted earlier private report | §2 lines53–121, equations(2)–(4) labelled convolution and full carry; §3 lines122–172 truncation convention; §5.1 lines220–266 convergence and digit-product bound, especially(11). Source definition §1 is identified in PH04 ledger C01. |
| S4 | SRG_PH03_PRODUCT_MASS_SHELL_01/REPORT.md, accepted earlier private report | §§1–2.1 lines18–99 circle and inverse; §§2.2–3 lines100–198 reciprocal action; §4 through line274 projection limits; §6 lines340–394,(26)–(30), introduced physical dictionary. |
| S5 | PH04 CHECK_RESULTS.json and CLAIM_SOURCE_LEDGER.md | /counts, /scan_schedule, /symbolic_candidate_residuals, /assertion_evaluations_by_category, /data_files; ledger C01–C23 and later scope/history claims. Saved evidence, not executed in manuscript preparation. |
| S6 | SRG Multiplication Geometry: Factor Data, Circle Construction, and Mass-Shell Correspondence, v0.1, Hilmir Frímann Halldórsson | Separate preceding paper; local editable candidate read for identity, notation, bibliography and build context. Eventual edition path recorded there: PAPERS/SRG_MULTIPLICATION_MASS_SHELL/publication/v0.1/. Publication status was not queried or changed. |

PH02/PH03 locators and recorded hashes are inherited through PH04's accepted CLAIM_SOURCE_LEDGER and evidence/SOURCE_EXCERPTS.md. Their excerpt lines were read as source context here; their accepted checkers and historical corpus were not rerun or re-audited. This is manuscript preparation, not a fresh source-recovery workflow.

Manuscript references [1]–[5] correspond to S1,S2,S3,S4,S6. Reference [6] is the inherited external diagnostic: Particle Data Group, *Kinematics*, 2025 update, physical p1, §49.1, equation(49.1), [official PDF](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf). It was originally inspected in PH03; it was not newly downloaded or treated as a source for the digit geometry. The dictionary remains conditional.

## Identities

SHA-256 identifies bytes, not truth or external acceptance. PH04 identities below were compared with the supplied acceptance packet and rechecked after preparation. Earlier PH02/PH03 identities are the values recorded by accepted PH04, not a claim of a new corpus verification.

| Source | Bytes | SHA-256 |
|---|---:|---|
| PH04/REPORT.md | 35259 | eacdd636777900a541b87b2790666d21ef9435fb475e6354fb30f257c91225e0 |
| PH04/CLAIM_SOURCE_LEDGER.md | 11285 | 7fb0cf899d6401bebe58fde5798785ea56e0b688505f9ee216a42959c83977e5 |
| PH04/CHECK_RESULTS.json | 5823 | 65646dbebd416512d3530062ceae156a9004d1c7d013be8ba4c204d4414e1767 |
| S2 scientific review | 14912 | d057d58d4ce4f56d6f8d970bcabb0377bdefc7fb1dc19e47c1d732fb46fc64f6 |
| SRG_PH02_MULTIPLICATION_GEOMETRY_01/REPORT.md | 33124 | 7c78df86d2cb0f59418066e1003fdb436f5a09dde5b73a04049f7b2e033ebec8 |
| SRG_PH02_MULTIPLICATION_GEOMETRY_01/CHECK_RESULTS.json | 750233 | 67eca393c80bf2f552a7c0bfefc78dc11c75f2af347d2a9bcdd8e113a1fbf0dc |
| SRG_PH03_PRODUCT_MASS_SHELL_01/REPORT.md | 25826 | 64de52ca37025e58b07ceef52c4fe6de036b0e12b85310b5884d61776565ef4f |
| SRG_PH03_PRODUCT_MASS_SHELL_01/CHECK_RESULTS.json | 18844 | a729e7becab78b510121297862c916761e1d95916fefaefa5c75c1933504fff5 |
| S6 original editable candidate | 43587 | ab26a5d07d6da65026199b971378ec40e57441bfa02ba2ab6e6bc06331272bd2 |

## Seven frozen public data members

Each occurs at the root of data/SRG_PH04_EXACT_TABLES_v0.1.zip. D1–D7 are used in the claim ledger.

| ID / member | Bytes | SHA-256 |
|---|---:|---|
| D1 / constant_certificates.json | 71151 | 4b0a7bf1d547447597beeedf39d57c0ba77042b1e6546c8e6beacff0d8485e34 |
| D2 / profiles.json | 192482 | 188d1702223fbe378cbf83e1486c898b85f4998a3ef0911520d5942ae41f7ec4 |
| D3 / pairs.json | 5492578 | 209f76e31d3349aa153d66f783d4d84b481ac4ce89c00ffeeaef3a8080312012 |
| D4 / triples_and_blocks.json | 1164684 | ea87e595b692d9cd5cdd7ebe49000e08902cf2d8b45f59b9a70da53ca8cd62b4 |
| D5 / ranked_summaries.json | 1665355 | 1e61fd88689b8edd1301412aa8895a4e905188e1d1c9884c18517320ca8a0087 |
| D6 / anchor_carries_and_terms.json | 28799 | 298274bca44678d84053ca47019981429b59ed11b01d1f064cbb1b89b89459a3 |
| D7 / findings.json | 57514 | 3014e175879bbe793756fda047874adfb904ff2cfe448bb30d5f21fbb13b3934 |

## Four frozen figures

F1–F4 identify file order; manuscript figure order is F3,F1,F2,F4. They were copied without regeneration, cropping or scientific recalculation.

| ID / candidate path | Bytes | SHA-256 |
|---|---:|---|
| F1 / figures/01_imbalance_by_depth.png | 107095 | c67f805acac3d876edc87c438d7d2a328003efa904ef2df0476f1a89df29f84d |
| F2 / figures/02_relative_contributions.png | 157609 | 070195b296bcf9106420aa2fd5ec40b5c5a56ee194d89f61a1d879e364051b6d |
| F3 / figures/03_legal_carry_circle.png | 117234 | 3630e2df42fc8d09ef05177295d065f07c1321c058b7c1aa6b4af8fee86eca0a |
| F4 / figures/04_normalized_pair_geometry.png | 112945 | 6ae4384f57e95d20a1a303d15016d43a42385d1fc19bcd2a50667b0803feee86 |

## Provenance and reuse boundary

Raw inputs retain pi,e,phi,gamma labels and canonical decimal convention. The adjacent-summand circle is the PH04 representation choice. General identities, certified prefix results, finite ranks and physical assignments are distinguished in the 32-claim ledger.

The acceptance packet and private reader-error history govern this task's scope and provenance; they are not new scientific literature or a licence grant. The final corrected PH04 checker and its failed predecessor remain private evidence, not public runtime dependencies. No new blanket reuse licence or software-licence coverage for research is introduced.
