# Paper E v0.1.1

**Bounded publication revision for GPT final-byte review.** GPT accepts v0.1's central mathematics within its written hypotheses, with disposition `ACCEPT_WITH_MINOR_REVISIONS`. E-01 through E-04 are implemented here. Final publication approval and author publication authorization have not been supplied for this artifact.

Read [the revised PDF](publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf), [complete manuscript](PAPER_E_Z_MANIFOLD_v0.1.1.md), [exact change record](CHANGE_RECORD.md), [current reference ledger](REFERENCE_LEDGER.md) and [build/reproduction results](BUILD_AND_VERIFICATION.md).

The revision documents the historical NumPy signed-zero phase convention and phase-off bypass, clarifies the channel display at zero, corrects cylinder/torus configurability, fixes Erb to Example 2(iv), printed page 10 of arXiv v1, and narrows one cancellation-attribution sentence. It changes no displayed equation, named theorem/proposition statement, figure, dataset or historical source.

The complete reviewed **90-path predecessor stays in its original parent location byte-for-byte**, including its manuscript, PDF, figures, logs, 89-entry manifest and review-pending metadata as historical records. This directory is the current edition; the parent README records v0.1's earlier status. No bulk archive copy is made. Shared figures, sources, frozen arrays, earlier results and the symbol/theorem sheet are deliberately referenced from the predecessor.

`evidence/gpt_review/` contains the supplied review, checker and results with verified identities. GPT's 27 groups / 147 evaluated conditions remain GPT-attributed; Codex did not rerun that checker. Codex's previous 66 symbolic predicates, 51 package checks and four source replays remain v0.1 evidence. New revision checks are separately recorded in `evidence/codex_revision_checks.json`.

## Reproduction scopes

1. **Read the proof:** the PDF is self-contained; reference and provenance detail is in the ledger. No executable environment is required.
2. **Build the revised paper:** run this directory's `build_publication.py` with existing Pandoc/Tectonic and a populated cache. It consumes shared figure PDFs and does not execute historical code.
3. **Redraw figures:** the parent's `generate_figures.py` uses its frozen NPZ and analytic formulas. This was exercised only in a disposable minimal copy. The original figure bytes remain unchanged.
4. **Check E-01/E-02 and package consistency:** `check_revision.py` runs two inspected standalone function bodies and static AST checks. It executes no model trajectory or GUI.
5. **Optional historical source replay:** the parent's `recover_plot_data.py` has its own declared four-run scope. Compatible existing evidence is reused; it was not rerun for this revision. Other archived scripts retain original dependency assumptions and are not claimed fresh-clone runnable.

See [reproduction details](REPRODUCIBILITY.md). Existing dependencies were reused; none was installed or upgraded. The exact combined proposed publication path set is in `PROPOSED_PUBLICATION_ALLOWLIST.txt`; already-committed reference dependencies are listed separately in `COMMITTED_REFERENCE_DEPENDENCIES.json`. The combined SHA-256 manifest is rooted at the repository, and the predecessor's original manifest is retained unchanged.

The source-map, catalogue and existing recovery record receive narrow append-only dispositions outside the repository. Their appended bytes and before/after identities are documented here; they are not additional publication paths. Six-gap registration remains open, no physical energy law is established, and no historical Z restoration or kernel change follows from this revision.

No staging, commit, push, cleanup, tag, release or DOI operation was performed.
