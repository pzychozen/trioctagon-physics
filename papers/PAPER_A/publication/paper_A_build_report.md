# Paper A publication build report

Completed 2026-09-21. The 19-page publication PDF faithfully typesets the frozen Paper A v0.5.1. This work performed publication conversion and rendering QA only; no mathematics, citation research, simulations or numerical regressions were reopened.

## Authoritative inputs and freeze authorization

The final citation spot-check explicitly names v0.5.1 and records `PAPER_A_FINAL_CITATION_SPOTCHECK = PASS`, `READY_FOR_PUBLICATION_FREEZE = YES`, and `READY_FOR_TYPESETTING = YES`. It supersedes the candidate status in the manuscript's historical preamble. The selected manuscript was therefore determined from the freeze record, not filename sorting.

The exact six inputs were copied byte-for-byte into `inputs/` and hashed before authoring. The final integrity check found all originals and snapshots unchanged. Original paths and SHA-256 follow:

| Input | SHA-256 |
|---|---|
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md` | `e39b543247c232b59da035cd6f6f190554c18c484bcf1b9482a1ad11c906dcf2` |
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_REFERENCES_v0.2.md` | `b46ce6ef96d520d9b85bf6e4347024b01363254e04f376877e3db536c824a22a` |
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\CODEX_PAPER_A_FINAL_CITATION_SPOTCHECK.md` | `637532a0f36681bd3039f50a2652684af2b1027c6b2a065a0bd2d24502535940` |
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_v0.5_to_v0.5.1_PATCH_LOG.md` | `7e46a3608435fe6aebaeec546d402e7a6b092f46b27e50af789f8f017d6a2a1d` |
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_v0.4_to_v0.5_CITATION_PATCH_LOG.md` | `f533001d78913d01c3867746f4b63ad27cd75fddc80417ca95942baedcc60c05` |
| `C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_LITERATURE_CONTEXT_CORRECTIONS_v0.1.md` | `88c068f879948c6dcf9878785f08cf4ebb9e2832a9f75f0ab5923c149265422d` |

## Publication metadata and permitted additions

Title: **Cycle-Covering Dynamics of a Three-State Nonlinear Kernel**. Sole author: **Hilmir Frímann Halldórsson**. Email: **pzychozen@gmail.com**.

The frozen manuscript supplies no author block. The author supplied the exact name, email and acknowledgement during this task and explicitly requested their inclusion. No affiliation, ORCID, institution, funding, DOI or license was added. These are logged publication metadata additions, not edits to the frozen scientific source. AI systems appear only in the acknowledgement:

> The author used Claude Fable 5.1, GPT-5.6 Sol, and Codex Astra as AI-assisted research tools for mathematical reconstruction, adversarial review, verification, drafting, and publication preparation. All scientific claims, interpretations, and publication decisions remain the responsibility of the author.

The acknowledgement is after Appendix D and before References. The PDF metadata records the publication build date; no historical research date is invented. The user-facing filename is publication edition v1.0, with scientific provenance v0.5.1 retained here.

## Section classification

Every source heading and the administrative preamble are classified below. Scientific caveats, limitations, methodological text, all four appendices, reproducibility paths and the full introduction to References are retained, including mixed historical/context language where omission could narrow the source.

| Source line | Exact heading / block | Classification |
|---|---|---|
| 1 | Cycle-Covering Dynamics of a Three-State Nonlinear Kernel | SCIENTIFIC_BODY |
| 3 | Version/change-history preamble | INTERNAL_PROVENANCE_ONLY |
| 8 | Abstract | SCIENTIFIC_BODY |
| 16 | 1. Introduction | SCIENTIFIC_BODY |
| 43 | 1.2 Established frameworks (background) | SCIENTIFIC_BODY |
| 47 | 1.3 Relation to prior work | SCIENTIFIC_BODY |
| 54 | 1.4 Contribution (what is model-specific) | SCIENTIFIC_BODY |
| 67 | 2. Cycle graphs and pull-back spaces | SCIENTIFIC_BODY |
| 91 | 3. Covering theorem for periodic Laplacians | SCIENTIFIC_BODY |
| 119 | 4. The $C_{12}\to C_3$ reduction | SCIENTIFIC_BODY |
| 121 | 4.1 The covering | SCIENTIFIC_BODY |
| 124 | 4.2 Deck group and quotient | SCIENTIFIC_BODY |
| 142 | 4.3 Degenerate sizes (darts) | SCIENTIFIC_BODY |
| 145 | 5. Fourier and symmetry decomposition | SCIENTIFIC_BODY |
| 164 | 6. Nonlinear extension for every $M$ divisible by three | SCIENTIFIC_BODY |
| 166 | 6.1 The ring map, with an explicit zero-amplitude convention | SCIENTIFIC_BODY |
| 194 | 6.2 Exact reduction for all $M=3q$ | SCIENTIFIC_BODY |
| 217 | 6.3 Numerical cross-check (one-step identity, and a long-trajectory caveat) | SCIENTIFIC_BODY |
| 231 | 6.4 The exceptional $(M,d)=(3,2)$ case | SCIENTIFIC_BODY |
| 235 | 6.5 Closest dynamical neighbours (context) | SCIENTIFIC_BODY |
| 239 | 7. Transverse stability ($M=12$) | SCIENTIFIC_BODY |
| 243 | 7.1 Real deck-character block structure | SCIENTIFIC_BODY |
| 259 | 7.2 Linear spectral test vs nonlinear attraction | SCIENTIFIC_BODY |
| 272 | 7.3 The default attractor | SCIENTIFIC_BODY |
| 281 | 7.4 Representative regimes ($M=12$) | SCIENTIFIC_BODY |
| 296 | 7.5 A fixed-branch crossing, and regional (not global) scope | SCIENTIFIC_BODY |
| 317 | 8. Numerical perturbation verification ($M=12$) | SCIENTIFIC_BODY |
| 336 | 9. Relation to a second ring operator | SCIENTIFIC_BODY |
| 348 | 10. Feedback compatibility (sufficient condition) | SCIENTIFIC_BODY |
| 368 | 11. Discussion | SCIENTIFIC_BODY |
| 374 | 12. Limitations | SCIENTIFIC_BODY |
| 383 | 13. Conclusion | SCIENTIFIC_BODY |
| 389 | Appendix A — Theorem proofs (supplementary) | SCIENTIFIC_APPENDIX |
| 399 | Appendix B — Nonlinear reduction details | SCIENTIFIC_APPENDIX |
| 407 | Appendix C — Numerical methods | SCIENTIFIC_APPENDIX |
| 415 | Appendix D — Reproducibility | SCIENTIFIC_APPENDIX |
| 430 | References | PUBLICATION_REFERENCE |
| 457 | Manuscript audit | INTERNAL_PROVENANCE_ONLY |

## Omission register

Exactly two administrative blocks were omitted. Source line numbers refer to the frozen 508-line manuscript. The quoted payloads below reproduce every omitted line. Markdown horizontal rules were rendered as normal section spacing; this is a presentation adapter, not a textual omission.

### Version/change-history preamble

SOURCE LOCATION = C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md, lines 3-4

CLASSIFICATION = INTERNAL_PROVENANCE_ONLY

REASON = Administrative version and audit history; the scientific qualifications recur in the retained body.

SCIENTIFIC_CONTENT_REMOVED = NO

OMITTED TEXT:

````text
**Draft v0.5.1 (publication-freeze candidate)** — discrete mathematics / nonlinear dynamics manuscript.
Identical to v0.5 except for one residual **P2** wording fix in §1.3: the "invariance under all admissible network dynamics … [SGP03]" sentence is brought into line with the already-corrected §6.2, separating the vector-field synchrony results [SGP03, GST05, GS06] from the explicit smooth-network-map formulation [NRS16]. No other change; see `PAPER_A_v0.5_to_v0.5.1_PATCH_LOG.md`. Built from the frozen mathematics of v0.4 by applying the **citation, attribution, and bibliography** patches of `CODEX_PAPER_A_v0.4_CITATION_AUDIT.md` (P1–P11 attribution narrowings; M1–M3 metadata corrections; removal of two now-unused references from the publication bibliography). **No equation, theorem statement, proof, numerical value, atlas count, Floquet multiplier, model definition, zero-amplitude convention, feedback equation, RSB equation, parameter value, or claim boundary was changed; no simulation or mathematics was rerun.** The patches narrow prior-art wording so that each citation matches exactly what the cited source supports, keeping every self-contained theorem, proof, and calculation owned by this paper. Positioning remains **conservative**: standard machinery is cited as background, the contribution is the specific model plus its explicit deck-resolved transverse-stability atlas, and **no novelty or priority is claimed**. References are collected in `PAPER_A_REFERENCES_v0.2.md`; the per-change record is `PAPER_A_v0.4_to_v0.5_CITATION_PATCH_LOG.md`; superseding corrections to the companion literature notes are in `PAPER_A_LITERATURE_CONTEXT_CORRECTIONS_v0.1.md`. Provenance of the frozen mathematics: v0.2 resolved all fifteen findings of `CODEX_PAPER_A_REFEREE_REPORT_v0.1.md`; v0.3 applied the five RESIDUAL_MINOR corrections of `CODEX_PAPER_A_v0.2_FINAL_SPOTCHECK.md`; v0.4 added literature context (`PAPER_A_v0.3_to_v0.4_LITERATURE_LOG.md`). This remains a self-contained mathematical paper; it makes no physical, historical-design, or systems claim (§12).
````

### Manuscript audit

SOURCE LOCATION = C:\TORMENT\TRIOCTAGON_new\reconstruction\papers\PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md, lines 457-508

CLASSIFICATION = INTERNAL_PROVENANCE_ONLY

REASON = Machine-style citation/audit closeout flags; not part of the scientific argument.

SCIENTIFIC_CONTENT_REMOVED = NO

OMITTED TEXT:

````text
## Manuscript audit

```
PAPER_A_v0_5_1 = COMPLETE (publication-freeze candidate)

P1_APPLIED = YES   (Theorem 1: divisor-case = standard; converse + (3,2) classification calculated here — §1.2/§3)
P2_APPLIED = YES   (discrete-time map: SGP03/GST05/GS06 fields + NRS16 maps; Field04 removed; Arg_0 owned here — §6.2 and §1.3)
P2_RESIDUAL_FIX = YES   (§1.3 network-quotients sentence brought into line with §6.2 — v0.5.1)
P3_APPLIED = YES   (master-stability roles split: PC98 framework vs Pecora14/Sorrentino16 decomposition — §1.2/§1.3/§7.1)
P4_APPLIED = YES   (Floquet precedent narrowed: Sorrentino16 cluster + ABS96 normal; periodic-orbit Floquet ours — §1.3)
P5_APPLIED = YES   (lift spectrum: general IRR vs abelian one-dim characters here — §5)
P6_APPLIED = YES   (harmonic-3: all-m claim withdrawn; HMM93/AS92 as context; cluster count not derived from them — §6.1)
P7_APPLIED = YES   (coupled-map context: Kaneko globally coupled maps; Field04 -> NRS16; search-limitation kept — §6.5)
P8_APPLIED = YES   (g*: "transverse -1 crossing"; ABS96 removed from period-doubling; blowout OS94 vs bubbling ABS94 distinct — §7.5)
P9_APPLIED = YES   (perturbation: Schaub16 illustration; measured rates ours — §8)
P10_APPLIED = YES  (RSB: mechanism [GR01,SGP03], not unrestricted full-operator theorem — §9/§11)
P11_APPLIED = YES  (adaptive-coupling clause [Sorrentino16] deleted; SGP03/Schaub16 kept — §10)

M1_APPLIED = YES   (GFBC24: I. Stewart, IJBC 34(7):2430014, 2024, 41 pp)
M2_APPLIED = YES   (DL15: JEMS 17(12), issue 12 not 11)
M3_APPLIED = YES   (DF19: Dalfó, Fiol, Širáň; 50(4):419–426)

FIELD04_REMOVED_FROM_PUBLICATION_BIBLIOGRAPHY = YES
STEWART07_REMOVED_FROM_PUBLICATION_BIBLIOGRAPHY = YES

POSITIONING = CONSERVATIVE
NOVELTY_CLAIMED = NO
PRIORITY_CLAIMED = NO

MATHEMATICS_CHANGED = NO
NUMERICS_CHANGED = NO
THEOREM_STATEMENTS_CHANGED = NO
PROOFS_CHANGED = NO
MODEL_CHANGED = NO
ATLAS_COUNTS_CHANGED = NO
FLOQUET_MULTIPLIERS_CHANGED = NO
ZERO_AMPLITUDE_CONVENTION_CHANGED = NO
FEEDBACK_EQUATION_CHANGED = NO
RSB_EQUATIONS_CHANGED = NO
PARAMETER_VALUES_CHANGED = NO
CLAIM_BOUNDARIES_CHANGED = NO
SIMULATION_RERUN = NO
SOURCE_MODIFIED = NO
KERNEL_MODIFIED = NO

HISTORICAL_DESIGN_CLAIMED = NO
PHYSICAL_CLAIM_MADE = NO
TORMENT_CLAIM_MADE = NO

READY_FOR_FINAL_CITATION_SPOTCHECK = YES
READY_FOR_TYPESETTING = YES
```
````

## Typesetting and fidelity

A4 pages, 24 mm margins, 11 pt TeX Gyre Pagella body and Pagella Math. The unchanged `\setminus` notation uses the STIX Two Math glyph fallback. Latin Modern Mono is used for literal code/paths, including its explicit bold face. All used PDF fonts are embedded. Existing equation labels are preserved; no numbering is invented. Long displays are width-fitted without changing tokens. The §7.4 table has a landscape page; the other four tables use 9.3 pt type. References use 10.3 pt ragged-right text. No scientific figures were required or invented.

The Markdown reader explicitly recognizes lists immediately following prose, so literal source list markers do not leak into the PDF. The generated LaTeX adds anchors, clickable citation tags and DOI links without changing displayed source text. Code paths may wrap while preserving their exact characters.

The fidelity check reverses only the documented presentation adapters and compares the entire retained document syntax tree against the frozen source's parsed content. All retained prose, emphasis, formal statements, proofs, inline equations, display expressions, headings, table cells and bibliography entries compare exactly. DOI link targets match the existing source strings; no network validation or new citation audit was performed.

| Structural item | Frozen / publication count |
|---|---|
| Formal statements | 3: Theorem 1, Proposition 2, Corollary 3 |
| Display equation blocks | 20 / 20 |
| Inline math nodes | 724 / 724 |
| Explicit equation labels | 8: 2.1, 2.2, 2.3, 6.0, 6.1a, 6.1b, 6.2, 10.1 |
| Tables | 5 / 5; body rows 4, 5, 6, 4, 6 |
| Main numbered sections | 13 / 13 |
| Scientific appendices | 4 / 4 |
| Source headings retained | 36 including title, abstract, subsections and references |
| Publication references | 20 / 20, all cited |
| Required figures | 0 / 0 |
| Internal link annotations | 93, all destinations resolve |
| Unique DOI targets | 20, all match frozen bibliography |

The body/reference entries were not expanded or rewritten from the companion ledger. The paper's established claims, limitations and historical annotations remain exactly where supplied. The only additional heading is the user-approved Acknowledgements.

## Page-by-page visual QA

Direct visual inspection of all page PNGs rendered by Poppler at scale-to 1400; final pages 1-18 pixel-identical to the reviewed pages, page 19 reinspected.

| Page | Result | Inspection |
|---|---|---|
| 1 | PASS | Exact title, accents in author name, email, abstract, keywords, inline math and citations. |
| 2 | PASS | Introduction, matrix, phase update and contribution list; no clipping. |
| 3 | PASS | Literature-context paragraphs and numbered contribution list; links and emphasis. |
| 4 | PASS | Definitions, equations (2.1)-(2.3), theorem opening and page transition. |
| 5 | PASS | Remaining theorem clauses, proofs, matrices, proof-end squares and qualifications. |
| 6 | PASS | Covering/deck notation and all four rows of the first table. |
| 7 | PASS | Fourier spectrum, radicals, Arg convention and equations (6.0), (6.1a), (6.1b). |
| 8 | PASS | Explicit caveat list, Proposition 2, proof, wrap-around expression (6.2), set-difference glyph. |
| 9 | PASS | Five-row numerical cross-check table, scientific notation and retained qualifications. |
| 10 | PASS | Real projectors, direct sum, U-sector subscripts and Floquet notation. |
| 11 | PASS | Linear-test caveats, moduli and deliberately open space before landscape page. |
| 12 | PASS | Landscape eight-column/six-row table; every value, header and qualification legible. |
| 13 | PASS | Crossing value, spectral notation, four-row atlas table, unresolved-sample caveats. |
| 14 | PASS | Six-row perturbation table, signed rates/exponents, tensor-state equation and prose. |
| 15 | PASS | Corollary 3, equation (10.1), proof and full three-item caution list. |
| 16 | PASS | Discussion, all limitations and conclusion; complete text retained. |
| 17 | PASS | Appendices A-C, inline set difference, matrices, scientific notation and code text. |
| 18 | PASS | Remaining Appendix C, all Appendix D paths, exact acknowledgement; no clipped paths. |
| 19 | PASS | All 20 bibliography entries, diacritics, tags and DOI strings; no trailing reference-only page. |

All final page characters lie inside the page bounds. There are no missing glyphs, overfull boxes, undefined references or content-affecting build warnings. Four underfull-paragraph spacing notices remain (LaTeX lines 197-199, 449-450, 683-684, 716-717); the affected pages were visually checked and the text is complete and legible. These notices do not indicate clipping or lost content.

```ini
TITLE_PAGE = PASS
ABSTRACT = PASS
HEADINGS = PASS
EQUATIONS = PASS
TABLES = PASS
REFERENCES = PASS
PAGE_BREAKS = PASS
HYPERLINKS = PASS
NO_CLIPPING = PASS
NO_MISSING_GLYPHS = PASS
NO_RAW_MARKDOWN = PASS
NO_BUILD_WARNINGS_AFFECTING_CONTENT = PASS
```

## Reproducibility and checksums

Tools: Pandoc 3.11; Tectonic 0.17.0; Python 3.12.14; QA extraction with pypdf 6.10.0 and pdfplumber 0.11.9; page rendering with bundled Poppler. The portable Windows executables and the complete fetched TeX cache remain in `build/tools/` and `build/tectonic-cache/`. Official release download URLs/checksums are recorded in `build/tools/*_download.json`. No research program is imported or run.

Rebuild from any PowerShell working directory, using Python 3.12 with pypdf and pdfplumber installed (the bundled runtime used here is shown):

```powershell
& 'C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_A\build.ps1' -PythonExecutable 'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
```

The build uses only the frozen snapshots and publication files. It sets `SOURCE_DATE_EPOCH` to the fixed 2026-09-21 build date and uses Tectonic `--only-cached`; no network resource fetch is needed for this retained build. The standalone LaTeX file also remains available. The verification script additionally checks the originals at their recorded absolute paths; a moved standalone archive can still build, but that original-workspace integrity check requires the originals to remain accessible.

An actual cached-only rebuild completed successfully and reproduced the same PDF SHA-256. This is byte-identical PDF rebuild evidence on the recorded toolchain, not a claim that Markdown bytes equal PDF bytes.

Generated LaTeX SHA-256: `54afe1de03942af818f4cde0de96dd75f74d790540adabf0da4e63026755a1b0`.

Final PDF SHA-256: `25798a39db0577b6a42444b6ecdf89706d36750f61a7c21f02d89f0651fe98c1`.

`paper_A_source_manifest.sha256` records 390 frozen/publication/tool/cache files. `paper_A_pdf_manifest.sha256` records the public PDF. Build logs, syntax-tree fidelity evidence, page renders, font embedding checks, visual QA and the rebuild comparison are under `build/`.

## Delivery and Zenodo status

Delivered the publication PDF, standalone LaTeX and reproducible build scripts, input/source/PDF manifests, this report, and `PAPER_A_ZENODO_METADATA_DRAFT.md`. The metadata names Hilmir Frímann Halldórsson as the sole creator. The license remains UNDECIDED. No DOI, affiliation or funding was invented. No upload or external publication action was performed. The artifact is ready for the author's PDF spot-check and a later Zenodo package.

```ini
PAPER_A_PUBLICATION_PDF = COMPLETE

AUTHORITATIVE_SOURCE_IDENTIFIED = YES
AUTHORITATIVE_SOURCE_VERSION = v0.5.1
SOURCE_HASH_RECORDED = YES

SCIENTIFIC_CONTENT_CHANGED = NO
MATHEMATICS_CHANGED = NO
THEOREMS_CHANGED = NO
PROOFS_CHANGED = NO
NUMERICS_CHANGED = NO
CITATIONS_CHANGED = NO

INTERNAL_PROVENANCE_OMISSIONS = 2
SCIENTIFIC_OMISSIONS = 0

PDF_BUILD = PASS
PDF_PAGE_COUNT = 19

TITLE_PAGE_QA = PASS
ABSTRACT_QA = PASS
EQUATION_RENDERING_QA = PASS
TABLE_RENDERING_QA = PASS
REFERENCE_RENDERING_QA = PASS
PAGE_BREAK_QA = PASS
GLYPH_QA = PASS

PUBLICATION_SOURCE_REPRODUCIBLE = YES

FINAL_PDF_SHA256 = 25798a39db0577b6a42444b6ecdf89706d36750f61a7c21f02d89f0651fe98c1

ZENODO_METADATA_DRAFT_CREATED = YES

READY_FOR_HUMAN_PDF_SPOTCHECK = YES
READY_FOR_ZENODO_AFTER_SPOTCHECK = YES

SOURCE_FILES_MODIFIED = NO
KERNEL_TOUCHED = NO
```
