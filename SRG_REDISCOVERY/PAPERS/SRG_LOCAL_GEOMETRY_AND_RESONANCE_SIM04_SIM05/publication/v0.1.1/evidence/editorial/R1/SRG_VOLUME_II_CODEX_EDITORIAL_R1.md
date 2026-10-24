# Codex — Volume II bounded manuscript correction R1

**Assignment:** `SRG_VOLUME_II_SIM04_SIM05_EDITORIAL_R1`  
**Author / research director:** Hilmir Frímann Halldórsson  
**Scientific lead / reviewer:** GPT  
**Date:** 23 October 2026  
**Goal:** correct the reviewed v0.1 manuscript; return one new candidate for review. **No publication authority.**

## 1. Starting point and verdict

GPT has accepted the scientific core of the 30-page SIM04/SIM05 manuscript, including all four propositions and the ten retained figures. Three bounded transcription/navigation corrections are required for final manuscript acceptance. Read `SRG_VOLUME_II_v0.1_GPT_MANUSCRIPT_REVIEW.md` and `SOURCE_READBACK_EXCERPTS.md` in this review package.

Authoritative repository:
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Existing candidate (preserve unchanged):
`SRG_REDISCOVERY/PAPERS/SRG_LOCAL_GEOMETRY_AND_RESONANCE_SIM04_SIM05/draft/v0.1/`

Expected starting PDF SHA-256:
`1f625a35c76446769b473d01affc480c46f3a8738f9f43baef2b2e6313927f5d`

Expected starting TeX SHA-256:
`8a7c5747d77e4bfc62035381afbae236d0a1fbc9be29d5a22218bf07a717712c`

Expected starting review ZIP SHA-256:
`8eedae1f6b85519fed3053d592c1ca64d038135d4b9cf69fb1a8c2fbf52cc95c`

Use a fresh sibling `draft/v0.1.1/` (or a clearly named non-overwriting candidate if occupied). Windows checkout remains authoritative. Use Windows CMD and the existing environment for document operations.

## 2. Required fixes — no broader rewrite

### E01 — §7.1: both selected drivers report mean absolute R

The v0.1 paragraph incorrectly calls SIM04's mean signed and contrasts it with Infinity's absolute mean. S4 lines 623–625 and 637–641 show the selected driver reports mean(abs(R)), max(abs(R)), and std(R). S5 lines 245–249 also report mean(abs(R)).

Correct the prose and C19. Keep the genuine difference in coherence special-case branches. Keep Eq. (23), standard deviation of the signed field, and all recorded numerical values unchanged. The fields are positive in the accepted records, so no reanalysis is required.

### E02 — Appendix B: use magnitude, not signed R, in the tensor input description

S5 lines 361–371 define R=abs(field.resonance) and top_R=R[top_idx]; line 440 uses that top_R. Change “signed R” to “amplitude magnitude |R|” and extend the locator to include the local definition and tensor assembly at 440–445. Clarify C27's source anchor.

Keep the quadratic R_i^2 weighting and the accepted principal-moment inequality/prolate-branch conclusion. This does not authorize running the eigengeometry driver.

### E03 — source locator repairs

- Appendix A, S5 “R sine; signed compression”: **190–195**, not 192–197.
- Appendix A, S5 “Noise; displacement; recording”: **198–205**, not 199–205.
- Claim matrix C20, selected S4 echo call/timing: **618–620**, not 618–619.

The supplied `PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch` gives the exact source-backed changes against the identified v0.1. It has not been applied. Read and implement it in the new candidate; there is no instruction to run `git apply` or any Git write. Preserve the original candidate and prior evidence copies.

**Do not replace “signed” globally.** Signed RPCO, signed fusion coefficients, and std(R) are correct. Only the two identified mean/tensor descriptions change.

## 3. Permitted document housekeeping

Update the new candidate's version/date/status consistently in the cover, headers, PDF metadata, guide, editorial notes and package metadata. Keep it a candidate for GPT and Hilmir review, not publication accepted. Record E01–E03 and state that numerical conclusions, four propositions and figure bytes are unchanged.

Rebuild the PDF using document-only tooling, render and inspect every page, check equations/tables/captions and links, and regenerate the new candidate's scoped manifests, build receipt and preservation evidence. Do not mutate the copied accepted studies or their historical manifests to harmonize status language.

Changing line breaks/page count due to the corrected prose is acceptable. Do not undertake a layout redesign or add prose, results or figures unrelated to the three corrections. A complete document-only diff should distinguish source corrections from version and evidence-index housekeeping.

## 4. Non-negotiable boundary

- New simulation/update calls: **0**.
- New RNG draws or scientific checker executions: **0**.
- New scientific statistics, estimates, plots, sweeps or ablations: **0**.
- No source algorithm changes, frozen-study edits, canonical-ledger changes, Volume I edits, kernel/UI/memory work or Tower II work.
- No staging, commit, push, release, publication preparation or publication.
- Do not rerun earlier verification to “make sure.” Reuse the accepted evidence and compare immutable file identities only.

## 5. Return and stop

Return a new candidate PDF and one self-contained review ZIP with editable TeX/bibliography, unchanged selected figures and required evidence/immutable input archives. Include:

1. `CORRECTION_DISPOSITION.md` with E01–E03, source locators and impact statements.
2. `DIFF_FROM_v0.1.patch` covering manuscript and evidence-matrix changes, with housekeeping clearly identified.
3. Updated starting guide, editorial notes, document/page checks, scoped manifest and preservation receipt.
4. An explicit statement that the four propositions, numerical results, figure assets and both immutable input archives were retained, with zero scientific executions.

Stop for GPT and Hilmir review. The next decision is acceptance of this manuscript, not another simulation.
