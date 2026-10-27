# Publication verification - v0.1

**PASS - pre-commit document and payload checks, 27 October 2026.**

The [machine-readable receipt](records/PUBLICATION_VERIFICATION.json) records checks against accepted FB02 attempt_002. The [exact manuscript diff](records/MANUSCRIPT_PUBLICATION.diff) and [explicit substitutions](records/PUBLICATION_REPLACEMENTS.json) limit changes to edition labels and source-access/provenance text. Replaying those substitutions reproduces every byte of the publication manuscript; no other sentence was changed.

- All 32 numbered equation blocks and A1-A4 are byte-identical. The equation/source map is byte-identical; the standalone appendix matches the integrated appendix. E01, O01, qualifications and unresolved statements are retained.
- All 295 files in FB01 and both FB02 attempts retain their original bytes and inventory. Unrelated Git status is unchanged. The existing SRG index change is append-only.
- The 17-page PDF was rendered and all pages visually inspected. All equation-page vector graphics match the accepted PDF, and mathematical rendering code/layout metrics are unchanged. Formula glyphs are vector outlines; exact editable TeX remains in Markdown. PDF text extraction alone is not the equation verification.
- All 29 source IDs and source metadata/identities are retained. Fifteen exact sources are accessible at the pinned existing commit, and their live GitHub bytes match the accepted SHA-256 values. Fourteen exact snapshots and unchanged review evidence are included. Both retained classical links resolve.
- Current publication links and PDF destinations resolve to their declared targets. Historical paths inside unchanged evidence are preserved as provenance; the publication source guide supplies current access.
- Windows Command Prompt with `conda activate torment` was used. No simulations, scientific project imports, kernel changes, model changes or package installations were performed.

PDF SHA-256: `5e563f5e9279138342edd3097cd3a63a2cb4ec91ad1a8d3a0b81127dbd4ed033`

The [payload manifest](PUBLICATION_MANIFEST.json) lists all publication files (excluding the manifest itself) and both necessary repository index files. Git staging and remote-content checks are performed after this record is frozen. The post-push receipt is kept outside the publication payload to avoid a self-referential commit identity; this pre-commit receipt does not itself certify a completed push.
