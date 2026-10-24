# E01–E03 disposition — candidate v0.1.1 / editorial R1

24 October 2026. Prepared for GPT and Hilmir review. GPT's v0.1 review accepts the scientific core subject to these corrections; this document records their implementation, not final manuscript acceptance or publication authority.

| Item | Implemented correction | Exact source anchor | Impact and retained material |
|---|---|---|---|
| E01 | §7.1 now states that both selected drivers report mean absolute R. C19 states the same and separates std(R) and the coherence guards. | [S4](evidence/originals/SIM04/srg_seed_explorer.py) 623–625, 637–641; [S5](evidence/originals/SIM05/srg_infinity.py) 245–249. Guards: S4 268–274; S5 225–226. | Corrects two prose descriptions only. Eq.23, signed-field standard deviation and genuine coherence-branch difference retained. Positive recorded fields make the previously quoted mean values unchanged. No data calculation. |
| E02 | Appendix B now says each relative vector is multiplied by its amplitude magnitude, absolute R. Locator and C27 include local magnitude selection and tensor assembly. | S5 361–371, especially 362/368, and 440–445. | Quadratic R_i² weighting and accepted principal-moment inequality/prolate conclusion retained. No tensor or eigengeometry execution. |
| E03 | Appendix A S5 sine/compression range is190–195; noise/displacement/recording is198–205. C20 S4 echo range is618–620. | S5 sine191, compression194–195; scale198, draw199, displacement202, recording205. S4 distances618–619 and echo call620. | Navigation only. Equations9,21,22, coefficients, update order and observer staging unchanged. |

The two source files above retain their accepted SHA-256 identities. The source excerpts were read as text, never imported. The exact source/claim changes match the supplied `PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch`; there was no global replacement of “signed.” Signed RPCO, signed fusion coefficients and std(R) remain intact.

## Exact diff and housekeeping

- [SOURCE_CORRECTIONS_ONLY.patch](SOURCE_CORRECTIONS_ONLY.patch) is byte-identical to GPT's proposed patch and changes only the two specified files.
- [DIFF_FROM_v0.1.patch](DIFF_FROM_v0.1.patch) is the complete unified diff for `manuscript.tex` and `CLAIM_EVIDENCE_MATRIX.md`. Its three additional TeX changes are the PDF subject, running header and cover version/date: candidate v0.1.1 / editorial R1 / 24 October 2026.
- [DOCUMENT_ONLY_DIFF_FROM_v0.1.patch](DOCUMENT_ONLY_DIFF_FROM_v0.1.patch) includes authored source, guide, index, notes, build instructions and document-tool changes. [FILE_CHANGE_REGISTER.json](FILE_CHANGE_REGISTER.json) lists retained/changed/added/relocated files and exact old/new hashes, including regenerated metadata and the rebuilt PDF. Diff and manifest self-identities are handled externally to avoid circular hashes.
- The only change to the inherited build helper is its private-cache copy source, now the completed sibling v0.1 cache. A new R1 finalizer replaces the former Git-aware packaging helper; no Git command is invoked. Historical tools are retained unchanged under `provenance/v0.1/` for audit, not execution.
- Version/status and R1 links were synchronized in the starting guide, editorial notes, evidence index, build instructions and package receipts. No frozen study text or historical manifest was harmonized to the new status.

## Retention and stop

The complete four-proposition section, every equation/align block, ten figure assets, bibliography, numerical result passages and both required immutable scientific input archives are unchanged. The old v0.1 directory is preserved in full. The new PDF was rebuilt, rendered and inspected page by page; document checks and preservation comparisons are recorded separately from the retained earlier scientific checks.

New simulation/update calls: **0**. Scientific checker executions: **0**. RNG draws: **0**. New statistics, estimates or figures: **0**. Kernel, ledger, Volume I and accepted-source edits: **0**. Git commands and publication actions: **0**. No Tower II or next investigation. Stop for GPT and Hilmir review.
