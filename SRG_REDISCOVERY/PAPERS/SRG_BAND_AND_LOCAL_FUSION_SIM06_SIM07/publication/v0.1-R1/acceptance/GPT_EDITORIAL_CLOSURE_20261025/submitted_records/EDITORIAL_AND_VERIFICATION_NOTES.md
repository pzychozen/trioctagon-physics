# Volume III R1 editorial and verification notes

## Authority and supplied files

The user directly authorized correction of E01-E02 only and required CMD from the first read. The supplied SRG_SIM06_SIM07_MANUSCRIPT_CODEX_HANDOFF_20261025.zip is byte-identical to the original drafting handoff and contains its original manuscript work order. No separate R1 order is present in that archive. The separate SOURCE_READBACK_E01_E02.md supplies the correction locations and supporting source/date excerpts.

This was sufficient for the two corrections; no wider instructions were inferred. The supplied readback was checked against the unchanged original copies and acceptance documents as text, without imports or scientific execution.

## E01: distinguish diagnostic from aggregation

Before: Section 10.1 called one whole-field average “Both sources' GRF observer.”

After: the shared pointwise definition is stated explicitly. Equation (32) gives Universe's mean over all N rows and Tower II's mean over each nonempty assigned band G_b. The prose explicitly states that Tower II's global metrics do not record a whole-field GRF. The mean-of-reciprocals interpretation and no-force-law qualification remain.

Evidence: [Tower II source](evidence/S6/source_package/original/srg_golden_tower_II.py), lines 223-237 and 244-250; [Universe source](evidence/S7C/source_package/original/srg_condensate_breaking.py), lines 243-255. No GRF values were calculated. Existing claim-matrix row C34 remains valid, with these explicit aggregation scopes.

Change is confined to the original closing_sections.tex lines 11-15. Equation number 32 and all later equation numbers are unchanged. Physical PDF page 28 / printed page 27 was inspected.

## E02: correct one review date

The s7creview BibTeX entry now says 25 October instead of 24 October. This agrees with [the review](evidence/S7C/SIM07_GPT_SCIENTIFIC_REVIEW.md), line 3, and [the acceptance receipt](evidence/S7C/GPT_ACCEPTANCE_RECEIPT.json), line 2. The separate Tower II review's 24 October date is unchanged.

Only references.bib line 6 changes. Physical PDF page 33 / printed page 32, reference [11], was inspected.

## Document checks and preservation

The exact unified diff is [R1_EXACT_DIFF.patch](R1_EXACT_DIFF.patch); byte identities for the changed sources are in [R1_SOURCE_CHANGE_RECORD.json](R1_SOURCE_CHANGE_RECORD.json). Root-level administrative records, build outputs and package identities are new R1 artifacts, not further manuscript corrections.

The prior 206-member review payload was checked against its unchanged ZIP before editing and rechecked after. The existing v0.1 directory was read only. All 158 extracted evidence copies, the three full accepted archives, and 11 PNG figures are unchanged. Preservation is scoped to actual supplied inputs, previous review payload and copied supporting files; no whole-repository audit is claimed.

New validation consists only of file hashes, source-diff checks, compilation, PDF text/navigation checks, page rendering/visual inspection and review-ZIP member readback. Old scientific tests were not run. New PDF page renders are document QA, not new scientific figures. Compiler output retains the existing minor spacing warnings; no new warning was introduced.

The prior title/header version and Appendix B's historical PowerShell-deviation disclosure are intentionally retained. That paragraph describes the original v0.1 preparation; **this R1 used CMD from its first read throughout**. The original disclosure was not rewritten to claim retroactive compliance.

## Package layout and stop

Current manuscript, evidence navigation and new R1 records live at the package root. baseline/ contains unchanged old root records and source/PDF snapshots; inherited links inside those snapshots retain their old package-root context. handoff/ and evidence/ are exact copies. The new external REVIEW_ZIP_IDENTITY.json hashes the completed review ZIP and is not inside it.

No simulation, RNG operation, scientific checker, graph/geometry/FFT recomputation, figure generation, merger investigation, kernel modification or Git/publication action occurred. E01-E02 are implemented and submitted for GPT/Hilmir review; scientific acceptance is not self-declared.

