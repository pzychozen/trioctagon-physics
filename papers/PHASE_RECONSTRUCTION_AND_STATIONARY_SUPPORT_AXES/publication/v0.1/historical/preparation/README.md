# Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map

**Review draft v0.1 — awaiting GPT/author manuscript review**  
Hilmir Frímann Halldórsson · 2 November 2026

The underlying phase and spatial results have project-internal acceptance. This assembled paper is a review draft, not a publication or repository adoption. It establishes the mathematical phase-to-decoder correspondence without assigning a named material feature to an arrow.

Start with `NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf`. The package also contains:

- `manuscript/`: complete relative-path LaTeX sources, the bibliography in `references.tex`, and document-only build/check utilities. No figure asset or scientific generation step is required.
- `CLAIM_SOURCE_LEDGER.md`: theorem/equation labels, accepted dependencies, domains and actual source identities.
- `evidence/phase/` and `evidence/spatial/`: unchanged proof notes, existing helpers/results and source records. **Do not run these to build the paper.**
- `provenance/`: supplied order, compact primary-source snapshots and original path/version/hash manifest. Separate acceptance reviews were not locally available; their operative acceptance and corrections are expressly recorded in the order.
- `inspection/`: final document checks, visual-inspection receipt, extracted text, bibliography HTTP checks and compiler receipt/logs. Rendered page PNGs remain in the original workspace and are intentionally omitted from this compact ZIP.
- `PREPARATION_REPORT.md`: corrections, actual commands, final PDF identity and inspection outcome.
- `PACKAGE_MANIFEST.json`: member sizes and SHA-256 hashes, excluding its own self-hash. The ZIP checksum is alongside the archive, outside it.

## Build

No accepted scientific helper, repository module, geometry constructor, native step or observer is part of the build. From the package root, use an already installed Tectonic with the required standard TeX resources available in its cache:

```bat
call conda activate torment
python -I -B manuscript\build.py --tectonic C:\path\to\tectonic.exe
```

The script uses `--only-cached --untrusted`, resolves source and output paths relative to the package, and writes the final PDF at the package root. It uses process-local font configuration and temporary paths under `build/`; it does not install anything or persistently modify the environment. Tectonic resolves the bibliography and references through normal passes. The bibliography is ordinary `thebibliography` source, so no external bibliography database is missing.

Alternatively, any suitably installed standard LaTeX toolchain can compile `manuscript/main.tex` from its directory with the normal reference-resolving passes. Preserve the package layout when placing the PDF at the root so relative evidence hyperlinks resolve. Font/toolchain differences may change PDF bytes; the delivered PDF's identity is recorded separately.

The optional document checker uses an existing `pypdf` installation:

```bat
python -I -B manuscript\verify_document.py
```

An existing additional site-packages directory may be supplied with `--python-packages PATH`; no installation occurs. `manuscript/check_reference_links.py` performs read-only HTTP HEAD requests for the bibliography links. Rebuilding needs no source recollection or network request. `prepare_sources.py` and `package_review.py` document this preparation in its original workspace; they are not prerequisites for compiling the portable manuscript.

All four requested editorial/table corrections are incorporated in the manuscript, while the accepted evidence remains byte-preserved. Stop at manuscript review: publication, Git operations, release and DOI deposit require a separate decision and are not performed here.
