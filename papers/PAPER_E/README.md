# Paper E: the historical Z manifold

**Scientific review draft v0.1, 23 September 2026. Author: Hilmir Frímann Halldórsson. Preparation: Codex. GPT review: PENDING_GPT.**

The 28-page manuscript distinguishes the staged scalar harmonic, macro cone, channel-area chirality, direct blend, alternate displays, diagnostics and EMA variant. Six-gap spatial attachment remains open. No physical energy law is inferred. The manuscript is complete for the requested review; it is not yet authorized for publication.

Start with [the publication PDF](publication/PAPER_E_Z_MANIFOLD_v0.1.pdf), [complete Markdown](PAPER_E_Z_MANIFOLD_v0.1.md), [symbol/theorem sheet](SYMBOLS_AND_THEOREMS.md) and [reference ledger](REFERENCE_LEDGER.md). The generated [LaTeX](paper_E_v0.1.tex) contains the complete manuscript, not a shortened PDF-only version. [References](references.bib) are also supplied in BibTeX.

## Evidence and checks

- `evidence/accepted_reconstruction/`: unchanged primary report, original 63-check result file, earlier preservation receipt and verification script. These are prior Codex evidence, not a new review.
- `evidence/source_snapshots/`: unchanged staged core/helpers and separate committed EMA snapshot. Their exact original paths and hashes appear in `evidence/source_provenance.json`.
- `evidence/preserved_runs/`: the two supplied series CSVs and summaries, preserved byte-for-byte. No large window archives or environments are replicated.
- `evidence/plot_data.npz`: newly generated, explicitly attributed data from four fixed source-body replays. The result file verifies exact Z, full-statistic and J equality for both saved configurations, with equal NaN positions.
- `check_symbolic.py` and `evidence/symbolic_results.json`: 66 exact symbolic predicates. The manuscript supplies the proofs and their hypotheses; the predicate count is not a theorem count.
- `generate_figures.py` and `figures/`: 11 reproducible figures, each as PDF, SVG and PNG. They use analytic formulas and the frozen plot data, with no viewer percentile scaling.
- `publication/`: final PDF, actual build stdout/log and build identities. Build output is new Codex output, not an original historical captured run.

The prior 23-configuration numerical study was reused without another sweep. Four fixed replays were executed for this package. These counts refer to different tasks and must not be added into an invented count of independently accepted theorems.

## Boundary and preservation

The only authored location is this Paper E directory. The protection receipt covers 512 existing files, including the tracked repository, historical and modern kernels, Papers A-D, the original saved diagnostic packages, the accepted reconstruction and its evidence. Its SHA-256 comparison also checks that HEAD, index and status outside Paper E are unchanged. `PROPOSED_GIT_ALLOWLIST.txt` is an explicit proposed path inventory only; creating it does not stage files or authorize publication.

`SHA256SUMS.txt` covers all public package files except itself. The allowlist includes the manifest. Temporary AST, font cache, raster QA pages and preservation baseline live in the ignored `.build/` folder. No cleanup, staging, commit, push, tag, release or DOI operation is part of this task.

See [reproducibility instructions](REPRODUCIBILITY.md), [the build and QA record](BUILD_AND_QA.md), [the exit disposition](EXIT_STATUS.json) and [the protection receipt](PRESERVATION_RECEIPT.json). The original execution environment/commit of the old runs and the six-gap registration remain unresolved. Neither prevents review of the defined Z mathematics.
