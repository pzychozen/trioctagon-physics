# Focused final artifact-check execution

Date: 3 November 2026.

The submitted 100-member editorial-closeout ZIP was checked for identity, safe unique paths and CRC, then extracted into a separate review directory. No submitted file was changed. The final PDF was independently rendered at 130 dpi. The revised title page was visually inspected; the other nine complete render images matched the corresponding previously inspected images byte-for-byte.

The exact MC-01 source diff, approved corrected main.tex, remaining nine TeX files, build helper, protected evidence, label/crosswalk records and refreshed build/PDF/source identities were compared directly. The supplied historical Windows preservation record was checked for internal consistency. No scientific code or supplied helper ran, and the manuscript was not recompiled here.

Two reviewer-workflow issues were resolved before final acceptance:

1. The initial PDF-text sentence comparison used plain characters, while pypdf extracted the fi in specified as a Unicode ligature. NFKC normalization of extracted text resolved that representation difference. The exact source-byte and PDF-byte identity checks were unaffected.
2. When recording the final comparisons, the local temporary page-08 PNG was found truncated. Page 8 was rendered again from the unchanged verified PDF into a fresh file; the complete PNG passed image verification and was byte-identical to the previously inspected original page 8. The incomplete temporary PNG was replaced by that complete render. No PDF or source change was involved.

The final run of verify_closeout.py passed all 270 document/evidence assertions. These assertions are not scientific algebraic checks and do not change the historical count of 25 distinct identities.

Independent review lanes found no material source-continuity, status or provenance issue. Author approval of the review and exact correction was already supplied; it is not being requested again. The final disposition is recorded in NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_FINAL_ACCEPTANCE.md.

The acceptance ZIP contains the receipt, machine-readable verification results, read-only review script, this execution record, exact accepted PDF and independently rendered corrected title page. Its manifest covers every other member. The full scientific/evidence edition remains in the separately identified user-supplied closeout ZIP, avoiding another nested copy here.
