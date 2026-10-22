# Publication verification

This is publication-integrity verification, not a new scientific experiment. Saved numerical results were copied and hash-checked, not recomputed.

| Check | Result |
|---|---|
| Accepted baseline | Exact R1 ZIP and PDF match the subsequent GPT closure; 116 archive payloads pass CRC, size and SHA-256 checks. |
| Historical evidence | All 374 payloads in four accepted study manifests pass; all 66 indexed evidence items are included with matching hashes. |
| Scientific comparison | Only main TeX metadata/cover/header, the C07 current-status sentence in section 1.3 and section 6.6 status text differ. Only C07/C102 status/support metadata changes in the current claim registers; all classifications, IDs, source locators and the other 100 records are unchanged. All 16 displayed equation/align environments, source programs, figure includes/assets and bibliography are unchanged. |
| Claims and references | All 102 claim IDs resolve to the same source markers and lines; 63 labels are unique; all label references and 12 bibliography entries resolve. |
| Figures | All 17 numbered figure includes and 35 asset hashes match; the compiler's figure list contains 17 entries. |
| PDF/source consistency | Exact distributed TeX/image/program inputs match the isolated build inputs; build succeeded. Final PDF identity appears in the preparation report and build receipt. |
| PDF quality | 53 pages; zero overfull boxes, undefined references, missing glyph warnings, replacement characters or unresolved question-mark pairs. The accepted abstract underfull warning (badness 1077) remains. |
| Submitted publication PDF comparison | 51 complete pages are pixel-identical and 52 pages have identical extracted text. Only pages 9 and 41 differ in pixels: page 9 contains the exact C07 sentence replacement; page 41 has unchanged source/text with a typesetter table-layout difference. |
| Accepted R1 comparison | Excluding only the running-header strip, 50 body rasters and 50 extracted page bodies match. Cover, C07 and the previously corrected C102 status account for the body-text differences. |
| Visual inspection | All 53 pages compared against the submitted publication. The two changed pages, 9 and 41, inspected at full size; the other 51 complete page rasters match the reviewed submission. No clipping, overlap or unreadable status text observed. Cover, headers and section 6.6 remain unchanged. |
| Evidence links | All active local Markdown links must resolve inside the exact payload, with case-sensitive path checks suitable for GitHub. Local absolute provenance strings and historical archived references are not advertised as live GitHub paths. |
| Publication seal | Complete exact-member manifest and SHA-256 checksums are verified by the read-only checker. The review ZIP's CRC, member list and byte identities are verified separately; ZIP hash is in the external delivery receipt to avoid self-reference. |
| Preservation | Protected file hashes, complete accepted directories, canonical ledger, Git HEAD/index and pre-existing Git entries remain unchanged. Unrelated inventoried file sizes/mtimes are also compared. |

Machine-readable records: [PDF and input comparison](records/pdf_comparison.json), [visual review](records/visual_review.json), [static content/link checks](records/content_checks.json), [preservation](records/preservation_after.json), [build receipt](records/build_receipt.json) and [manifest](PUBLICATION_FILE_MANIFEST.json). Run [the read-only checker](tools/verify_publication.py) from a complete extracted payload to repeat integrity checks.

The pre-PUB-01 submission and GPT review are preserved in [frozen provenance](provenance/pre_PUB01/README.md). The [restricted authored diff](provenance/pre_PUB01/PUB01_AUTHORED_CHANGES.diff) and [closeout](PUBLICATION_STATUS_CLOSEOUT.md) distinguish this status correction from the earlier publication preparation. No scientific acceptance is reopened.

The final publication manifest hashes every payload file except itself. SHA256SUMS.txt hashes all payload files except itself and the manifest; the manifest covers SHA256SUMS.txt. The external preparation receipt supplies the manifest and review-ZIP hashes. No checksum is made self-referential.

No remote publication has happened, so live GitHub links to this new edition cannot yet be tested. Their relative targets are all included in the proposed file list. The proposed post-publication procedure requires a fresh clone of the authorized pushed commit, the same checksum/relative-link checks, and GitHub browser checks of the landing page, PDF, source and original media/logs. Existing external dependency URLs are retained provenance, not newly certified network services.

No fresh dependency download or cross-platform build was attempted. The pinned compiler and copied cache were verified and reused in isolation. No claim is made that an alternate compiler/environment produces byte-identical PDF output.
