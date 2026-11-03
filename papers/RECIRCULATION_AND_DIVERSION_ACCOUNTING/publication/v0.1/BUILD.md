# Document-only rebuild

Use a separate writable copy of this edition, an existing Tectonic installation and its populated cache. From the edition directory run:

```text
python manuscript/build.py --tectonic PATH_TO_EXISTING_TECTONIC
```

The standard-library helper uses --only-cached and --untrusted; no TeX shell escape, network package fetching, installation or project imports. It writes temporary files to build/ and emits [RECIRCULATION_AND_DIVERSION_ACCOUNTING_v0.1.pdf](RECIRCULATION_AND_DIVERSION_ACCOUNTING_v0.1.pdf). The fixed source epoch is 3 November 2026 UTC, the actual edition/build date. Exact byte reproduction also depends on matching cached TeX, font and compiler versions. No font files are redistributed; fonts are embedded in the PDF.

With an existing Poppler installation, create a renders directory and run:

```text
pdftoppm -r 125 -png RECIRCULATION_AND_DIVERSION_ACCOUNTING_v0.1.pdf renders/page
```

Inspect every page after any rebuild. This edition was checked with Tectonic 0.17.0, existing Poppler and existing bundled pypdf; see [build receipt](verification/BUILD_RECEIPT.json), [document checks](verification/DOCUMENT_CHECKS.json), [fidelity review](verification/FIDELITY_REVIEW.md) and [visual inspection](verification/VISUAL_INSPECTION.json). The final compiler log has machine paths normalized; the external closeout retains the raw build log/receipt. Scientific source helpers and historical checkers are not build dependencies.
