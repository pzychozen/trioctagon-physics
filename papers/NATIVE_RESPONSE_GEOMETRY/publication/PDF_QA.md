# Publication PDF quality review

Research publication v0.1: **38 A4 pages**, 413084 bytes.

Final SHA-256: `eeb72e2c0351c5e749210d681d7ac227f6f72fa1e345d92725a2f9ac5298aaff`.

The revised PDF was rendered anew in full using Poppler at 110 dpi. All 38 pages were visually inspected in five contact sheets. PDF pages 1, 9, 20, 21, 22, 26, 31, 32, 37 and 38 also received full-page inspection: title/abstract, terminology note, Section 14 boundaries, Section 15 citations, publication wording, GR1/L13 plus-sign record, ledger status, Appendix C reconciliation and both bibliography pages. The five unchanged schematics remain clear in the new page layouts. No clipping, overlap, missing glyph, broken table row or unreadable equation was found.

The 38-page result has one title page, one contents page and 36 Arabic-numbered pages. The added contextual discussion and references account for the increase from 36 PDF pages. Running headers consistently say Research publication v0.1. The title page has the qualified N >= 9 statement and a separate six-ring sentence. Six contextual references appear as [14]-[19]; their citations and DOI/author links render correctly.

The final compiler log contains no TeX errors, unresolved citations/references, missing characters, overfull boxes or duplicate page anchors. All 38 pages pass the automated safe-bounds/text diagnostics in `pdf_qa_results.json`. These diagnostics support, and do not replace, visual inspection. The PDF retains selectable text, vector diagrams and live references; no tagged-accessibility certification is claimed.

Fresh page renders and text were written outside the repository to `C:/TORMENT/TRIOCTAGON_new/research/NRG_publication_revision_qa_20261006/`, as recorded in the render command. All 85 existing paper-lane `tmp/` files were left byte-for-byte unchanged and excluded from the proposed commit allowlist. No cleanup was attempted.

Reproduce with an existing Poppler installation and `python -B verification/qa_pdf.py --output-dir /path/to/fresh/external/preview-directory`, using pdfplumber and Pillow. This is visual/editorial QA, not external peer review. Final publication approval remains pending.
