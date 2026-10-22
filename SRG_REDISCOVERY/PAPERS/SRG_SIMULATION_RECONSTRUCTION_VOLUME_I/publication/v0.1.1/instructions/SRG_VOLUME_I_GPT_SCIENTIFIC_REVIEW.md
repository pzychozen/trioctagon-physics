# SRG Simulation Reconstruction — Volume I
## GPT scientific and manuscript review

**Date:** 22 October 2026  
**Author / research direction:** Hilmir Frímann Halldórsson  
**Scientific review:** GPT  
**Preparation under review:** Codex, candidate edition 0.1

## Verdict

**ACCEPTED WITH MINOR EDITORIAL REVISIONS.**

The scientific content is accepted within the manuscript's stated reconstruction and provenance scope. I found no substantive correction required in the transcribed update rules, displayed algebraic deductions, or numerical claims independently checked against the supplied records. Two small editorial/reproducibility clarifications should be closed before the publication version is frozen. Neither requires a simulation, a new mathematical investigation, or changes to the historical code.

This is a review verdict, **not publication authorization**, not an update of the Windows canonical ledger, and not permission to begin another simulation. The submitted manuscript remains the unaltered review candidate. Scientific acceptance does not remove its missing-run and movie/log qualifications.

## Plain-language assessment for Hilmir

This volume does the job we intended: it explains how three actual SRG programs were assembled, what they store, the order in which their parts act, and what the surviving pictures and numerical records show. It does not replace them with a tidier invented version of SRG.

The strongest result is that the reader can connect construction to behavior. Carried velocity explains why changing an interaction does not instantly reverse movement. The callback records explain why a driving clock can restart while the moving state continues. The wrapping and detector sections distinguish actual changes of direction from large displayed relocations and misleading warnings. The research preserves both the interesting behavior and the implementation details needed to interpret it.

This is Volume I of the reconstruction, not all of SRG. The unavailable historical chronology remains unavailable; it has not been supplied from recollection or borrowed from another simulation.

## 1. Exact reviewed submission

- Input ZIP: `SRG_SIMULATION_RECONSTRUCTION_VOLUME_I_01_GPT_REVIEW.zip`
- ZIP size: **7,204,482 bytes**
- ZIP SHA-256: `54b91588bfa86966a96e180a1f8021cfd32441bc01c19551659ac9672cd1c3ff`
- Candidate PDF: `MANUSCRIPT/volume_i.pdf`
- PDF size: **3,711,816 bytes**
- PDF SHA-256: `4180aaa47a7f95cfd2fd0b857dc98415339387652f1f0d3107af6a7aeaa979c7`
- Manifest SHA-256: `5e680bf92881aae386a1911d6d3d40785fc7b50ff6e2585d614c380e5787b030`
- Confirmed structure: **52 physical PDF pages; 17 numbered figures; 35 figure assets; 102 claim-matrix entries**.

The PDF has a cover, five Roman-numbered front-matter pages, and printed pages 1–46. Below, printed page numbers are followed by physical PDF page numbers where useful.

## 2. Work independently performed in this review

### Manuscript and source

I read the complete manuscript source, all three original program copies, the claim matrix, figure register, relevant review records, and supporting accepted-study material. I checked the equation transcriptions against the actual order of operations rather than checking only whether their symbols appeared in the code.

I read and assessed all 102 claim entries for scope and supporting locators. Every matrix locator resolves to its stated claim marker. The 102 entries are **not** 102 new theorems or independent experiments.

### Byte identity and figure provenance

- The ZIP CRC check passed for all **109 members**.
- All **108 manifest-listed payloads** match their declared byte lengths and SHA-256 hashes.
- All **374 manifest-listed payloads** in the four supplied accepted-study archives match those archives' declarations: 4 + 28 + 68 + 274. These are payload entries, not 374 separate historical originals.
- All three manuscript source copies match their counterparts in the earlier accepted packages.
- All **35 manuscript image assets** match their declared transformations: 27 are byte-identical copies, and the eight F03/F04 crops match the specified source pixels exactly.
- All **66 external-evidence content identities** were resolved against the supplied accepted packages or included copies/snapshots. For the three historical-source paths, the charter and the canonical ledger, this verifies the corresponding archived content, not the live Windows paths. The canonical-ledger reference matches the included *after* snapshot, not the older separately uploaded ledger.

### Recorded-data inspection

Independent read-only calculations used the already saved S01 arrays/event records and the original S03 CSV rows. They did not advance a simulated state, import an original simulation, draw a random value, or rerun an accepted scientific checker.

The checks cover the S01 recorded near-contact, largest increment, wrap counters, sampled H sign changes and nonzero final velocities; the S03 row/block and label counts; kinetic and incoming-GRF accounting; recorded position-increment consistency; toggle and turn counts; detector/seam counts; extrema and closest-pair examples; and the cited body-5/body-7 episodes.

The original all-500-state source-equivalence assertion remains the accepted replay's recorded check; I did not execute the old program again to repeat it. Likewise, the manuscript correctly retains the limited coverage of the earlier sampled full velocity-equation audit. This review did not convert that sample into a new exhaustive force audit.

### PDF and presentation

I rendered all 52 pages at 130 dpi and visually inspected every page, including all figures, tables, captions, equations and front/back matter. The full manuscript text and LaTeX were also read. Selected dense equation/table pages were expanded for closer inspection. No clipped equations, missing figures, broken glyphs, unresolved reference markers or overlapping text were found. There are 63 unique labels with no unresolved label references in the source.

The supplied final typesetting log has zero overfull boxes, zero undefined-reference messages and one underfull warning. I read that log; I did not rebuild the PDF or download the typesetter. The visual appearance of the candidate is acceptable apart from the small copyediting items below. Small multi-frame panels are appropriate for their expressly qualitative claims; exact measurements are given in the text and records rather than inferred from those small pictures.

## 3. Scientific assessment by part

### S01 — Chapter 2, printed pp. 4–12

Equations (2.1)–(2.9) preserve the time-only H function, both uses of the period-two wrap, norm-plus-0.001 regularization, componentwise RPCO, and the mixed old/new positions in the sequential update. The observation list is not misrepresented as a simultaneous update buffer or a route read back by the dynamics.

The historical PNG and the accepted seed-0 reproduction remain distinct. The reproduction's minimum recorded end-of-sweep pair separation is at state 169, bodies 1/2, approximately `0.0000442435132788`; the surrounding recorded gaps are approximately `0.00149607869215` and `0.00158335361603`. The stated largest native increment, `0.0345666628741`, occurs at event 20. The saved record has zero position and force-wrap shifts and seven sampled H sign changes. All final velocity vectors remain nonzero. These readbacks agree with the manuscript.

The chapter does not turn overlapping traces into a recovered leader/follower episode or turn a finite record into an asymptotic convergence result.

### S02 — Chapter 3, printed pp. 13–18

Equations (3.1)–(3.8) match the original sequentially recalculated arithmetic centroid, once-per-callback incoming GRF, frame-label H, retained velocity, damping and wrapping. H is not accidentally counted twice. The tetrahedral offsets remain display geometry, not force-bearing vertices.

The centroid discontinuity calculation is sound: one positive period-10 coordinate crossing contributes `−10/8` to the arithmetic mean, in addition to ordinary motion. The manuscript does not substitute a different torus mean or assign an invented native displacement to the historical frame-13-to-14 relocation.

Its discussion of animation callbacks is appropriately qualified: the locally inspected Matplotlib version supplies a compatible explanation, not a certified historical backend/version or callback trace.

### S03 — Chapter 4, printed pp. 19–34

The switch equation uses the post-toggle mode, respects the short-circuit RNG gate, and reverses the new interaction contribution rather than resetting stored velocity. H and the common incoming GRF are correctly placed. The logs are read in physical callback order, not sorted or deduplicated by repeated frame labels.

The independent CSV readback agrees with the main quantitative anchors:

| Quantity | Log A | Log B |
|---|---:|---:|
| Rows / callbacks | 8,736 / 1,092 | 3,520 / 440 |
| Label-zero blocks | 12 | 6 |
| Between-block toggles | 79 | 33 |
| Detector would-flags | 8,151 | 3,129 |
| Actual seam body events | 22 | 7 |
| Maximum native increment | 0.061531941627 | 0.060380826470 |
| K just before first 199→0 reset | 0.000922772193 | 0.000721816994 |
| K just after that reset | 0.479749698621 | 0.473368801859 |

Body 5 in B changes mode at callback 7 but still has a positive outgoing radial component at callbacks 7 and 8; it becomes negative at callback 9. Recalculation using the observed mixed-state centroid reproduces Table 4.3. Body 7's crossings at callbacks 409, 414 and 418 occur with mode 1 throughout the stated 400–420 window. The manuscript distinguishes these finite events from a universal switching delay or a proven periodic orbit.

The drive–damping identity, equations (4.7)–(4.9), is algebraically correct. Expand the candidate velocity's squared norm and subtract the nonnegative componentwise damping loss. The result is accounting for the implemented kinetic diagnostic, not a newly introduced physical potential or conservation theorem.

The detector analysis correctly distinguishes a negative coordinate difference passed through unsigned modulo, a coordinate seam, and a native movement increment. The wording “would flag” appropriately avoids claiming to possess the missing original console transcript.

The sampled movie/log agreement remains strong but formally **UNLINKED**. Image similarity is not promoted to a recovered export chain, unique run identity, or certification of all frames. Original charts with mixed horizontal axes are preserved and explained, not silently repaired.

### Synthesis, agenda and appendices

The conditional S02/S03 equality with identical incoming arrays/frame and all post-gate modes zero is correct as a mathematical update identity. It is not presented as equality of unknown historical runs. The RPCO sign/magnitude statements and the H envelope have their required qualifications. The text does not infer a forever-decaying drive from a clock whose labels restart.

Study numbering remains research order, not invented creation history. The separate path-inheritance screens, later SRG families, time-equation lineage and future gravity comparison remain distinct. No scientific expansion is required to finish this volume.

## 4. Minor revisions before the publication version is frozen

### E01 — Remaining joined words/numbers in appendix prose and Table B.1

**Severity:** editorial only; no change to any value, equation or evidence.

Locations in the submitted source:

- `MANUSCRIPT/sections/07_provenance.tex`, lines 36, 44, 51, 58 and 64: restore spacing in `800 by800`, `60fps`, `20fps`, `rows /1,092` and `rows /440`.
- `MANUSCRIPT/sections/08_reproducibility.tex`, lines 29, 31, 32 and 34: change `All2,000`, `relations;31`, `independent20` and `All18` to normally spaced text.

These occur on printed pp. 40–41 and 43 (physical PDF pp. 46–47 and 49). Check the same prose-level spacing pattern in the human-readable registers, without altering hashes, source filenames, IDs, formulas or original evidence. The large historical charts themselves should remain unchanged.

**Closure:** rebuild the manuscript and inspect the affected pages. Page numbers may change; update generated references and review receipts accordingly.

### E02 — Make the first-build prerequisite explicit in the PDF's instructions

**Severity:** reproducibility documentation; no change to science or tool behavior.

Appendix B.2, printed p. 44 (physical PDF p. 50), gives `python -B tools\build_pdf.py`. In a fresh extracted archive, `build/toolchain/tectonic.exe` is absent by design, and the builder expects that exact executable path. The manuscript README already mentions the supplied acquisition script, so this is not a missing tool or an unrecoverable project. The prerequisite should also appear in the PDF and immediately beside the README command block.

State explicitly that a fresh Windows copy first obtains the pinned compiler using the supplied `python -B tools\acquire_typesetter.py`, then runs `python -B tools\build_pdf.py`. Existing workspaces with the compiler present can skip acquisition. Explain that first-time dependency acquisition needs network access and that the excluded build cache is not part of the review ZIP. Keep any alternative XeLaTeX route separately labeled; do not claim cross-environment byte identity.

**Closure:** clarify the instructions and confirm they agree with the existing scripts. No simulation or historical checker is needed; no toolchain redesign is requested.

## 5. What is not independently certified here

I did not inspect the live Windows checkout, verify its current HEAD/index, or independently certify all 397 protected source files at their live paths. Those preservation results remain Codex's recorded checks. I did verify the supplied archive bytes and the earlier accepted-package contents described above, and read the authorized ledger diff. The diff records SIM03's acceptance and Volume I's draft entry without changing the underlying historical evidence classification.

I did not recover the original random seeds, missing movies' numerical histories, historical GUI event traces, or the exact S03 export chain. I did not rerun the original simulation programs, scientific checkers, movie renderer, compiler acquisition or LaTeX build. The included review calculations operate only on supplied bytes and recorded states.

## 6. Decision after this review

Retain the candidate and its exact identities. Close E01–E02 in a separately identifiable corrected candidate, preserving scientific statements, original evidence, source copies and accepted packages. The correction is a small manuscript closeout, **not another research investigation**.

A final corrected edition, its refreshed hashes and the narrow diff should receive closure review before a separate publication action. No publication, commit, push, ledger mutation or next simulation has been performed or authorized by this report.

**Bottom line:** Volume I has a sound experimental reconstruction at its stated scope. Its remaining work is editorial finish and clear build instructions—not more simulations, new gravity premises or another reconstruction of the same results.
