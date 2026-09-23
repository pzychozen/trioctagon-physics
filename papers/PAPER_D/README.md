# Paper D: Tri-Octagon Reference-Scaffold Geometry

**Complete review draft v0.1, 23 September 2026.** Author: Hilmir Frímann Halldórsson. Scientific lead: GPT. Preparation, exact formalization and bounded source trace: Codex. Full-paper GPT review remains pending. No new Claude review or joint acceptance is claimed.

Main deliverables:

- `PAPER_D_REFERENCE_SCAFFOLD_DRAFT_v0.1.md`: full self-contained manuscript.
- `publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.pdf`: publication-quality review PDF.
- `paper_D.tex`: complete generated LaTeX source.
- `SYMBOLS_AND_THEOREMS.md`, `REFERENCE_LEDGER.md`, `bibliography.bib`, `UNRESOLVED_ITEMS.md`.
- `figures/`: nine exact-coordinate construction figures, each vector PDF/SVG and PNG preview.
- `evidence/`: 12 new manuscript/figure predicate results, source identities, fidelity/QA records, and a small byte-preserved accepted predecessor packet.
- `REPRODUCIBILITY_MANIFEST.json`, `PRESERVATION_RECEIPT.md`, `evidence/preservation_receipt.json`, `SHA256SUMS.txt` and `PROPOSED_GIT_ALLOWLIST.txt`.

The accepted four-page note remains untouched under `research_notes/reference_scaffold/`. Paper D is a longer review paper, not a replacement source map. The current snapshot and bounded functionality disposition are in the existing workspace `reconstruction/KERNEL_SOURCE_TO_MODEL.md`; the existing catalogue links to it and the recovery record records this handoff.

## Reading scope

Geometry is proved under tangent alignment and positive-length assumptions. The Paper-C comparison is exact at the measurement-polygon level; regular tuning changes finite-face incidence. Historical Z/torus maps are source-supported, but their registration with reference gap cells remains unresolved. The author's new reply narrows the recollection to that display family. Angular emission, RSB, portal and grid mechanisms remain separately identified and unrestored. No physical energy law or new kernel option is introduced.

## Build with existing dependencies

Use Python 3.12 with the versions in `requirements.txt`, Pandoc 3.11, Tectonic 0.17.0 and an already populated Tectonic cache. Poppler `pdftoppm` is used for page-render QA. The build performs no installation or network scientific-data retrieval. Dependencies may be in an existing environment or supplied as third-party library paths; no project kernel is imported.

```powershell
.\build.ps1 -Python C:\tools\python.exe `
  -Pandoc C:\tools\pandoc.exe -Tectonic C:\tools\tectonic.exe `
  -TexCache C:\tools\tectonic-cache
```

Optional `-PythonLibraryPath` takes the platform-separated directories of existing third-party libraries. The command first generates the nine diagrams, runs only `verify_manuscript.py`, then builds the complete Markdown/TeX/PDF. It writes generated outputs within this paper directory and `.build/`. It does not execute `evidence/accepted_scaffold/verify_scaffold.py`, import model code, or fetch historical PDFs. The saved manuscript, geometry transcription and evidence make the public build independent of the full research archive.

The accepted predecessor results are 31/31 predicates from the earlier run. The separate prior 42-predicate host/core suite and 95-test modern local checkpoint are documented historical evidence, not rerun here. New verification stdout is separately attributed and captured; it is not a historical run log.

To verify delivered bytes, run `python verify_package.py`. To render a rebuilt PDF for inspection, run `pdftoppm -png -r 110 publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.pdf .build/page`. Review every page. The supplied manifest describes the delivered files; rebuilding may change tool metadata or logs, so a changed manifest result must be explained rather than overwritten as if the original artifact matched.

## Publication boundary

The explicit proposed allowlist contains only this paper's public files. Local `.build/` evidence, tool caches, page previews and maintainer-only preservation tooling are excluded. It does not include an environment, the historical corpus, source snapshots beyond the four small accepted scaffold files, or Papers A/B/C. The three continuity records are authorized workspace edits outside this repository and are listed separately in the preservation receipt.

No paths are staged; no commit, push, tag, release or DOI is created. Publication requires completion of review and later author authorization. The checked published baseline is `08c2a79739d540ffe1cab4743284052e2aa7214b`; local modern tests and published-file presence are separately enumerated in `evidence/source_provenance.json`.

