# Build and source guide — GEO-ORIGINS-01 v0.1

This is the author-approved, internally reviewed nine-page mathematical/history companion manuscript. The reviewed PDF and TeX are unchanged from the manuscript acceptance; this guide alone supersedes the preparation-time local `BUILD.md` for public distribution.

Read the paper directly at `GEO_ORIGINS01_v0.1.pdf`. Editable inputs are `GEO_ORIGINS01_v0.1.tex`, `references.tex`, `figures/circle_conventions.pdf`, and `figures/shell_and_lengths.pdf`. The figure builder `figures/render_figures.py` uses `figures/geometry_inventory.json` (an unchanged accepted BOUNDARY-11 geometry inventory) and explicit circle formulas. SVG and PNG figure versions are retained. Figures are deterministic schematic presentations, not new physics observations.

For a build, install a compatible TeX/Tectonic toolchain **independently**, then compile the TeX in an external scratch/output directory; do not write build artifacts into the scientific source tree. The original local evidence used cached Tectonic:

```text
tectonic -X compile --only-cached --untrusted --keep-logs --keep-intermediates --outdir <external-output> GEO_ORIGINS01_v0.1.tex
```

The original host's build wrapper (`build_manuscript.py`), environment activation path, font/cache locations and command logs are **private review tooling and are not included in this public edition**. Accordingly the command above is a reproducibility reference, not a claim that this subset reproduces the accepted PDF byte-for-byte on every machine. Font and compiler differences may change PDF bytes.

If regenerating figures using a suitable Python environment, run `python -B figures/render_figures.py` only in an isolated working copy; it may write generated outputs. No kernel, TORMENT, network service, historical quantum experiment or scientific simulation is required. The supplied paper and figure files should not be regenerated or replaced as part of the authorized publication.

The original author's intent, source-attribution and evaluation records are described in the accompanying access guide. No original source PDFs, private chat transcripts, private source maps or machine-specific build logs are redistributed here. The software and scientific-content licensing scopes remain separate; publication does not grant a new blanket scientific reuse licence.
