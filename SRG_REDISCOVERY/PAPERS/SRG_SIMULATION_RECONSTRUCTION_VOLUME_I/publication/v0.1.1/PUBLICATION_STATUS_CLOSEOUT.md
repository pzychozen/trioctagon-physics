# PUB-01 publication-status closeout

Hilmir, the remaining status mismatch is corrected. C07 now says: **“Scientific and editorial review is complete; publication requires separate authorization.”** The C07 and C102 claim-register entries agree with that status and cite the preserved editorial closure and publication work order. The science is unchanged. This is still edition v0.1.1.

**PUB-01: corrected; narrow final status/identity check pending.** Scientific acceptance and E01/E02 closure remain in force. Publication still requires separate owner authorization.

## Restricted changes

- MANUSCRIPT/sections/01_scope.tex: replace only the C07 sentence on lines 104–105. The preceding ledger history, line count and C07 marker are retained.
- CLAIM_EVIDENCE_MATRIX.md and records/claims.json: change only C07/C102 administrative status/support wording. The other 100 records, all 102 IDs, classifications and manuscript locations are unchanged.
- tools/verify_publication.py: explicitly require those exact sentence/record replacements, the unchanged rest of section 1.3 and the unchanged section 6.6. All existing scientific-content, source, figure, evidence, link and manifest checks remain. The matrix is independently restricted to the two corresponding rows.
- MANUSCRIPT/README.md, PUBLICATION_PREPARATION_REPORT.md, PUBLICATION_VERIFICATION.md and PUBLICATION_APPROVAL_CHECKLIST.md: refresh only the descriptions of the allowed changes, actual PDF/check results and final-review boundary.

Generated records refreshed: MANUSCRIPT/volume_i.pdf; records/build_receipt.json, pdf_structure.json, pdf_comparison.json, visual_review.json, content_checks.json, preservation_after.json, modified_copies.json, typeset.log and typeset_console.txt; provenance/PUBLICATION_CHANGES.diff; SHA256SUMS.txt; PUBLICATION_FILE_MANIFEST.json. New provenance preserves the supplied order/review and pre-correction records. Exact staging/file lists and archive identities are supplied in the closeout review ZIP.

The [compact authored diff](provenance/pre_PUB01/PUB01_AUTHORED_CHANGES.diff) is against the submitted publication. The [cumulative publication diff](provenance/PUBLICATION_CHANGES.diff) is against accepted R1. Old receipts and the previous PDF are retained in the [frozen record archive](provenance/pre_PUB01/submitted_publication_records.zip); the original 60,467,308-byte submission ZIP remains unchanged in its original workspace.

## Verified outcome

The corrected [PDF](MANUSCRIPT/volume_i.pdf) has **53 pages, 17 figures and 102 mapped claims**. It is **3,712,962 bytes**, SHA-256 **56489c2a4702ca05686cf47bd91faf6cf1981126f48191b8fb5b2b40aea61b9a**. The full current payload is sealed by the [manifest](PUBLICATION_FILE_MANIFEST.json); the external delivery receipt gives the final manifest and distinct closeout-ZIP identities.

Compared with the submitted publication, 51 full pages are pixel-identical and 52 have identical extracted text. Pages 9 and 41 were inspected at full resolution. Only page 9 changes text, by the requested sentence; page 41 has unchanged source/text with a typesetter table-layout difference. No page-count change, clipping or overlap was observed. All claim source locators remain valid, including C07 line 105 and C102 line 99.

All 16 displayed equation/align environments, 17 figure includes, 35 images, three source programs and 374 accepted study payloads retain their bytes/content. The formally UNLINKED movie/log qualification remains. Accepted R1, earlier studies, canonical ledger, prior preparation workspace, existing root/SRG READMEs, kernels and unrelated material remain unchanged; preservation and static check receipts are refreshed.

No simulation, trajectory generation, scientific checker, dependency experiment or new research was run. No staging, commits, pushes, releases or publication occurred. Return only for the requested narrow final status and identity check.
