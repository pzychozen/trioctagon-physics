# Paper D reference and evidence ledger

Prepared 2026-09-23. This ledger uses the pre-existing reconstruction rather than a new historical corpus screen. Paths are evidence locators, not build dependencies. SHA-256 values and relevant function anchors are in `evidence/source_provenance.json`. Paper D's exact geometry and figures build entirely from files inside this package plus declared third-party tools.

| ID | Reference and locator | Verification / allowed use |
|---|---|---|
| R1 | Euclid, Elements IV.15 and corollary; D. E. Joyce online edition, Clark University. https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV15.html | Page directly read 2026-09-23; regular-hexagon construction and equality of side and radius. Paraphrase only; manuscript proof is displayed independently. |
| R2 | H. S. M. Coxeter, Introduction to Geometry, second edition, unabridged paperback, Wiley Classics Library, April 1989, ISBN 9780471504580. https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/introduction-to-geometry-978-0-471-50458-0 | Publisher metadata and table of contents directly checked 2026-09-23. Regular Polygons p26, Isometry in the Euclidean Plane p39, Similarity in the Euclidean Plane p67. General background only; no full-text theorem or page-specific proof attributed to uninspected pages. |
| I1 | `research/GPT_proof/HISTORICAL_TRIOCTAGON_GEOMETRY_LINEAGE_v0.1.md` | Current report read. Prior 46-path/45-content coverage retained with its limits; chronology and exact historical page/equation pointers reused. |
| I2 | `research/GPT_proof/TRIOCTAGON_HEXAGON_CORE_DERIVATION_v0.1.md`, §6 | Accepted aligned scaffold derivation. §§1–4 retain dual-core, filled-hole and conditional Paper-C comparisons. No earlier suite rerun. |
| I3 | `research/GPT_proof/E8_ANTIPODAL_SIGN_AND_HOST_RECONSTRUCTION_v0.1.md` | Current accepted defect and interface scope. No new root search or exact-base proof campaign. |
| I4 | `research/GPT_proof/historical_host_v0_1/author_scaffold_clarification/author_request.txt` | Author's 2026-09-23 clarification. Original bytes copied as small provenance evidence, no historical date reassignment. |
| I5 | `trioctagon-physics/papers/PAPER_C/publication/paper_C_final.tex`, v0.3.1 | Published local-module reference at commit 08c2a79739d540ffe1cab4743284052e2aa7214b. Conditional rigid-coordinate identity from I2, unchanged A/B/C. |
| I6 | `reconstruction/KERNEL_SOURCE_TO_MODEL.md`, CURRENT SNAPSHOT and §16 | Existing bounded static trace and version/caller differences; v0.1.1 corrects the attribution to a tentative Z/torus association and an author-adopted assisted relay. |
| I7 | `research/GPT_proof/TOY_MODEL_SPECIFICATION_AND_PROOF_CATALOGUE_v0.1.md`, B33 and Part I | 59 scoped entries, not 59 theorems; unchanged executable specification; prior 95-test local checkpoint separately attributed. |
| H1 / P01 | `pdfs_old/TriOctagon_E8-SU3-Geometry.pdf`; printed 2025-10-29 | Prior I1 inspection: pp4–6 (1)–(6), p12 §8, p18 §11. Root-octet, independent-fold and representation claims; no new PDF rereading. |
| H2 / P02 | `pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.pdf`; printed 2025-11-24 | Prior I1/I2 inspection: p2 (1)–(3), pp20–22 (29)–(49). Shared-global-orientation octagons, unspecified hinge placement, distinct dual-tetrahedron construction. |
| H3 / P03 | `pdfs_old/Recursive_SRG_Evolution_qutrip_opperator_dual_core_geometry_computational_interpretation.pdf`; printed 2025-11-24 | Prior I1 inspection: p26 Fig2. Projected triangular-overlap core; same printed date does not order conceptual priority. |
| H4 / P19 | `pdfs_old/FB_recursion/Forward_Backward_recursion.pdf`; printed 2025-12-04 | Prior I1 inspection: p37 §19.3, offsets 0,+20,-20 degrees; not uniform 24 rays. |
| H5 / P05 | `pdfs_old/TriOcta_violations.pdf`; printed 2025-11-05 | Prior I1 inspection: p5, phase rotation distinct from real-space rotation. |

Internal and historical titles have not been assigned journal, DOI or external-publication metadata. Bibliography entries are archival/project references with stated versions. `bibliography.bib` records the same identities; the Markdown manuscript uses human-readable IDs so that it remains readable without a citation engine.

## Source-versus-derivation boundary

The exact length condition is author clarification plus current derivation, not an old PDF equation. The supplied GPT review accepts v0.1 with minor revisions; Codex has implemented those in v0.1.1, whose GPT review remains pending. Old Claude reports and their corrections remain prior evidence; no new Claude session or review substitution occurred. The original `../evidence/author_recollection.txt` is preserved, with an unchanged revision copy at `evidence/author_adopted_reply_as_saved.txt`. It records an adopted relay of assisted wording and a tentative Z/torus association, not independent spontaneous recall, source verification or a physical energy law.

The construction diagrams are the unchanged v0.1 exact-formula renderings. There are no historical simulation images or newly generated trajectories. The preserved 31-predicate script/results/stdout remain in the parent v0.1 package; the original script is not modified or rerun. The 42-predicate suite remains prior evidence. This revision reruns the 12 manuscript checks against the unchanged figure inputs and adds four bounded definition-check groups; the supplied GPT 17-group results remain separately attributed and were not rerun.

## Current-paper consistency follow-through

`evidence/abc_inspected_artifacts.json` records the actual A v1.0 (scientific source v0.5.1), B v0.1.1 and C v1.0 (scientific source v0.3.1) manuscripts, TeX and PDFs, their page counts and hashes, and equality to their commit blobs at `08c2a79739d540ffe1cab4743284052e2aa7214b`. Exact proposed locations and wording are in `ABC_PROPOSED_CORRECTIONS_v0.1.1.md`; the single compact impact table is appended to the existing recovery record. No A/B/C artifact is revised here.
