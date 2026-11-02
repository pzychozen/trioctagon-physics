# Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map

**Author-authorized repository research edition v0.1**  
Hilmir Frímann Halldórsson · 2 November 2026

Project-internal scientific and manuscript review completed; author publication approval granted. No external peer review is claimed.

[Read the final PDF](NATIVE_PHASE_SPATIAL_v0.1.pdf). The paper establishes exact common-phase reconstruction, corrected overlap accumulation, stationary support-axis correspondence, and the fixed-label, state-independent proper-rotation theorem on the admitted domain. It assigns no material feature or body-motion law.

- [Editable manuscript](manuscript/main.tex): all nine LaTeX sources and document-only build/check utilities; bibliography in `references.tex`.
- [Claim/source ledger](CLAIM_SOURCE_LEDGER.md): accepted dependencies, domains and exact source identities.
- `evidence/phase/` and `evidence/spatial/`: nine unchanged proof/helper/result/source-identity members. Do not execute these to build the manuscript.
- `provenance/`: unchanged compact primary snapshots and source manifest, the preparation order and [publication order](provenance/publication_work_order.md). The separately named GPT manuscript review was unavailable in the bounded local lookup; the publication order supplies the operative acceptance and complete cleanup. No historical review has been reconstructed.
- [Finalization report](FINALIZATION_REPORT.md), [publication disposition](PUBLICATION_DISPOSITION.md), and `verification/`: fresh final-edition document, source-byte, bibliography and every-page visual checks.
- [Payload manifest](PAYLOAD_MANIFEST.json): exact edition paths, byte lengths and SHA-256 values, excluding the manifest itself.
- `historical/preparation/`: original preparation README, ledger, report, manifest, package check, utilities and inspection receipts, preserved byte-for-byte and identified by [historical locations](verification/HISTORICAL_LOCATIONS.json). Their draft/pending labels and old paths describe the earlier review package, not this final edition. The old PDF and ZIP remain external and are not duplicated here. Historical preparation utilities are records, not the publication workflow.

## Build

No accepted scientific helper, project module, geometry constructor, native step or observer is part of the build. From this edition root, use an already installed Tectonic with the standard TeX resources in its cache:

```bat
call conda activate torment
python -I -B manuscript\build.py --tectonic C:\path\to\tectonic.exe
```

The script uses `--only-cached --untrusted`, resolves source and output paths relative to the edition, and writes `NATIVE_PHASE_SPATIAL_v0.1.pdf` beside `evidence/`. Process-local font configuration, caches and temporary files remain under `build/`; it installs nothing and changes no persistent environment setting. Tectonic resolves references and the embedded `thebibliography` through normal passes. Alternatively compile `manuscript/main.tex` from its directory with a standard installed LaTeX toolchain and place the PDF at the edition root. Toolchain differences can change PDF bytes.

The optional document checker uses an existing `pypdf` installation:

```bat
python -I -B manuscript\verify_document.py
```

This optional checker is a preparation-machine audit: it expects the original source paths recorded in the source manifest and the local rebuild's log and receipt. The portable manuscript can be compiled independently of that audit.

An existing additional site-packages directory may be supplied with `--python-packages PATH`; no installation occurs. The publication copy checks the final edition name/status and writes new audit outputs under `verification/`. `manuscript/check_reference_links.py` makes read-only HTTP HEAD requests for the bibliography links. Neither source preparation nor scientific calculations are prerequisites. The original versions under `historical/preparation/` retain their review targets and are historical only.

Fresh final PDF, source hashes, tool versions, page count and verification outcomes are recorded in `verification/DOCUMENT_CHECKS.json`, `verification/build_receipt.json` and `verification/VISUAL_INSPECTION.json`. The precommit disposition records author approval and finalization; the later external publication receipt connects this immutable payload to the actual commit and verified remote bytes without a recursive self-identity. Repository visibility does not broaden the repository's existing licensing scope.
