# Finalization report — repository research edition v0.1

**Title:** Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map  
**Author:** Hilmir Frímann Halldórsson  
**Review, author approval, and finalization date:** 2 November 2026  
**Status:** Author-authorized repository research edition v0.1; project-internal scientific review completed. Pre-publication finalization checks passed. No external peer review is claimed.

## Reviewed baseline and preservation

The accepted review ZIP was verified against SHA-256 `e2392100a77d1443f3158248d826e67698ce28d2034108d20f545e21020dab2c`. Its 16-page review PDF was verified against `48172f3b82e46352bb727af674aacdc958d278a3685a902299382990dc238083`. Every archive payload entry passed CRC/size/SHA-256 checks and matched the original preparation workspace. A separate baseline was extracted; the original ZIP and preparation workspace were not edited.

The execution workspace is `C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01`; the separate final copy is `final_edition/`. The canonical repository destination is `papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/`. The original checkout has two unrelated modified UI files and 31,494 untracked files. Publication uses an isolated worktree from freshly fetched `origin/main`; the original branch, index, and working files are preserved. Its original HEAD/base is `6aa1daec7a25f51f482ff91743b9f9c3e33f476c`, with no local commits ahead of that fetched main. The destination was absent locally and at the fetched base. No applicable AGENTS.md was found.

The downloaded manuscript review file was not found by the bounded search. The [publication order](provenance/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01_CODEX_WORK_ORDER.md) explicitly records the operative scientific acceptance, R1/R2, and author approval, and makes that absence nonblocking. [PUBLICATION_INPUTS.json](provenance/PUBLICATION_INPUTS.json) records the input identities. No unavailable review was fabricated.

## Exact authorized edits

R1 replaced the single abstract sentence with:

```tex
On the admitted positive in-phase triad branch with \(g>0\), strict normal stability implies strict local descent modulo common phase.
```

The reviewed `main.tex` hash was `8ef4c6c58e8c9561931947b3fb1609ba7a78766ecff70b85e68aff669f72126e`. Applying only R1 gave exactly the supplied reference `ad1ebcd8c475bd69f3adc9fc738a6cb409a5208e2e16e4290256710ec14f7537`. The final main-file identity additionally includes the authorized edition/status/attribution edits.

R2 replaced only the preceding-sector sentence with:

```tex
That domain is distinct from the \(60\)-degree finite-return sector noted in \cite[Section~8]{energy} and from any spatial cone angle.
```

The existing bibliography key resolves to the accepted energy note; its Section 8 discusses that distinction. No bibliography entry was added. R1 is visible on PDF page 1; R2 resolves as `[3, Section 8]` on page 15.

The four active main-file status locations now identify the approved research edition: PDF subject, running header, title edition line, and cover-status paragraph. The title line uses two intentional lines for edition/date. Attribution adds GPT's completed review of this manuscript. The author name is unchanged. The active README and ledger reflect completed review and approval. No global replacement was made in historical records.

Only `manuscript/main.tex` and `manuscript/discussion.tex` differ from the reviewed manuscript. The other eight `.tex` files are byte-identical. The inspected [source diff](verification/MANUSCRIPT_FINALIZATION.diff) contains only these authorized changes. [FINALIZATION_CHANGES.json](verification/FINALIZATION_CHANGES.json) supplies before/after hashes. No theorem statement, proof, parameter, domain, or normalization was altered.

The corrected information note, its original before-copy, the comma receipt, both proof/helper/result sets, and all primary-source snapshots are unchanged from the accepted review package. The one-byte relationship remains valid; no new comma edit was performed. `provenance/SOURCE_MANIFEST.json` remains a historical source-identity record. `historical/review/` preserves the original preparation report, README, ledger, manifest, and build/inspection records verbatim; its old pending-review language is historical. The bibliography's unpublished-note labels still describe the supporting investigation records.

## Rebuild and inspection

Final compiler: Tectonic 0.17.0, existing cached installation. Python: 3.11.15 in `torment`; Poppler: 26.07.0; pypdf: 6.10.0 from the existing bundled libraries. No packages were installed. No persistent environment or repository configuration was changed.

Exact Command Prompt build:

```bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01\final_edition
python -I -B build_edition.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --work-dir C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01\build_work
```

The wrapper passes `--only-cached --untrusted --keep-logs --keep-intermediates`, builds `manuscript/main.tex`, and copies only the canonical final PDF and selected fresh logs/receipt into the edition. Fontconfig settings are process-local and its configuration/cache remain outside the payload. `SOURCE_DATE_EPOCH=1793577600` fixes the document date to 2 November 2026. The exact command/environment/source identities are in [BUILD_RECEIPT.json](verification/BUILD_RECEIPT.json). The original review-output scripts were not used to rebuild a REVIEW-named PDF.

The final PDF was rasterized with the installed `pdftoppm.exe -r 110 -png` to external `rendered/page-01.png` through `page-16.png`. Every final page was opened and visually inspected. There were no clipped equations, overflowing tables, broken glyphs, misleading mathematical line breaks, blank pages, header collisions, or legibility defects. The paper remains **16 pages**; no page-count change occurred. [VISUAL_INSPECTION.json](verification/VISUAL_INSPECTION.json) ties every viewed page to its PNG hash and the final PDF hash. The active research-edition headers, cover status, abstract g>0, and new citation were inspected directly.

`inspect_edition.py --review-baseline <execution workspace>\review_baseline` checked the final PDF/source identities, 89 unique labels, 67 reference uses, all citations against 4 bibliography entries, all 18 embedded font subsets, local evidence links, ledger labels, both exact edits, and the unchanged archival bytes. PDF text extraction elides some inter-glyph spaces; the R1/R2 presence checks normalize whitespace and are corroborated by visual inspection. All checks are PASS in [DOCUMENT_CHECKS.json](verification/DOCUMENT_CHECKS.json). The final compiler log has no unresolved references/citations, missing characters, overfull/underfull boxes, or LaTeX/package warnings.

The clean publication worktree initially hit Windows path-length errors in unrelated tracked historical material. A retry using command-local `git -c core.longpaths=true worktree add` completed successfully; no permanent configuration change was made. Existing root `.gitattributes` already uses `* -text` to preserve artifact bytes, so no new attributes file is necessary. Staged/committed bytes will be compared to the frozen allowlist before the normal push.

## Final identities and package boundary

Canonical PDF: `NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf`; **16 pages**, **142267 bytes**.

SHA-256: `0f710dbf732ce4ec227a98650f3a774f7ba6cdab0ca8120df9859ac326ddcc01`.

| Final editable source | SHA-256 |
| --- | --- |
| `manuscript/appendix.tex` | `5b0f806a27ecb8cfc839effdc7be887244dddfd6c0abca2bc951fb53b14d61da` |
| `manuscript/coordinates.tex` | `f244a48b9203c5a4d703097635d6b745ed7b0f2e072602e86bce0f13784e0137` |
| `manuscript/discussion.tex` | `4c57c971af213524b21dc13660c0019949acdb4b411ec42c64498f1104b84024` |
| `manuscript/finite.tex` | `c07bb1df62d1782d9a3dc0c05b7a027e8d9e71e4da5c840ef1239bcb1e615c8b` |
| `manuscript/local.tex` | `9493c63d067af8d20dddc3824b9901508567183fc78e0d4d57bc730a84f23e99` |
| `manuscript/main.tex` | `11fc3e2206e76aaa968ff7ab65c3defd7ba462f50ac613f7c248480c9a7cdd0c` |
| `manuscript/minimum.tex` | `d72e2221ddeb512a5e40d0418dbfab19a0b030091b4331b0b50aaa57dd91f3f7` |
| `manuscript/references.tex` | `5486eb2e59954b472ae13f1668e3ad9cbebb358a2bca3f63db0a1fa86017920f` |
| `manuscript/retention.tex` | `49f56d2a404e35c96186f1d53468f3541d04ba565a8c284f14997744e49a2060` |
| `manuscript/setting.tex` | `f0b3113ce197085b6175e7a8b738d37c9f6f8785f67b0376341353757940edfe` |

The [payload manifest](PAYLOAD_MANIFEST.json) records the exact edition file list, sizes, and hashes, excluding itself. The edition contains the complete ten-file source, canonical PDF, current records/utilities, historical review records, the namespaced evidence, source snapshots, and operative orders. Rendered PNGs, font caches, TeX intermediates, duplicate build PDFs, and machine-local scratch files remain outside the committed payload.

The paper landing README and one root README entry provide discovery without rewriting surrounding content or licensing. The pre-commit [publication disposition](PUBLICATION_DISPOSITION.md) records approval and passed finalization. Actual commit, push success, every-file remote verification, and final closeout archive identities belong in the later external receipt; no resulting commit identity is inserted into its own payload.

No scientific helpers, project runtime imports, native steps, trajectories, root/profile solves, parameter searches, prior certificates, or observer advances were run. No runtime integration, release/tag, DOI deposit, announcement, or new investigation was undertaken. There is no unresolved content or document-layout issue at this pre-publication stage.
