# Historical TORMENT and the Trioctagon Physics Kernel

**Lineage, Mathematical Equivalence, and Structural Divergence**

Version 0.1, 1 October 2026. **ACCEPTED REPOSITORY PUBLICATION.**

Author: Hilmir Frímann Halldórsson. The author has accepted the manuscript
scientifically and editorially and authorized this repository publication.
Codex assisted with source review, drafting, inert-data preparation, figures and
typesetting. This is not Paper G, has not been externally peer reviewed, and
claims no DOI. It is mathematical reconstruction and bounded numerical comparison,
not physical validation or a production-kernel replacement.

## Current publication

- [Publication PDF - v0.1](publication/KERNEL_HISTORY_AND_COMPARISON_v0.1.pdf)
- [Editable publication manuscript - v0.1](source/KERNEL_HISTORY_AND_COMPARISON_v0.1.md)
- [Generated publication TeX](source/KERNEL_HISTORY_AND_COMPARISON_v0.1.tex)
- [Author disposition, publication scope and access limitations](evidence/PUBLICATION_DISPOSITION_v0.1.md)
- [Publication verification and final PDF hash](evidence/publication_checks.json)
- [Exact textual/status changes](evidence/publication_text_changes.json)
- [Complete commit path list](evidence/PUBLICATION_PATHS.txt)
- [Publication build receipt](evidence/build_record_publication.json)
- [Claim/source map](evidence/SOURCE_MAP.md)
- [Included inert figure/table excerpt](evidence/figure_table_data.json)
- [Authority identities](evidence/authority_identities.json) and [P3 source identities](evidence/source_identities.json)

The accepted review predecessor is preserved as the
[review PDF](publication/KERNEL_HISTORY_AND_COMPARISON_v0.1_DRAFT.pdf), with SHA-256
`40f0e16c47efe993041627fd7bbd42fe9b3e9c9406d7d3db8af5eeba95c8556d`.
Its [manuscript](source/KERNEL_HISTORY_AND_COMPARISON_v0.1_DRAFT.md), generated TeX,
[review notes](evidence/REVIEW_NOTES.md), build receipts and
[editorial clarification receipt](evidence/editorial_clarification_review.json)
retain their historical wording. Their local-review and permission-pending labels
describe the predecessor stage and are superseded for this publication by the
author disposition above. The PDF and manuscript linked first are the current edition.

## Scope and evidence access

The paper distinguishes production TORMENT, the independent Historical reference
and the current physics kernel. It explains H0-H6B lineage, equations, profile
choices, geometry and runtime boundaries, and P3's finite independent-kernel
results. Same-coefficient recurrence agreement is separate from coefficient-driven
behavior, observers, constructor semantics and excluded production functionality.
Scientific baseline: `9c9e579e97aac0cdc7524b0d05430d0d76e39ce4`.

Author approval covers repository publication of this manuscript and its included
derived excerpts and figures. It does **not** make the complete local H/P3 authority
packets, installed-wheel evidence or trajectory population public. The included
excerpt supports rebuilding the shown figures and PDF, not independently reproducing
all scientific executions. No additional local H/P3 evidence is copied into this edition.

The excerpt, figure manifest and original receipts are preserved byte-for-byte,
including the local-review labels they carried when created. Those labels are
historical provenance; the publication disposition records the later approval.
The software Apache-2.0 license does not automatically apply to this manuscript,
figures, research data or local reports; see [LICENSE_SCOPE.md](../../LICENSE_SCOPE.md).
Repository visibility does not grant a new blanket reuse license.

The separately named POST-P3 CONTINUITY HANDOFF was not found during the original
bounded source search. Its central scientific claims were checked directly against
P3 in the draft preparation. That continuity-document gap remains recorded; this
publication step does not reopen the audits or claim that the missing file was recovered.

## Rebuild in Command Prompt with the torment environment

From the repository root, use the existing paper toolchain. These commands use
the author's already installed local tools; they install nothing. Supply the
appropriate locations on another machine. Use a copied offline cache and a fresh
external workspace; the builder refuses to replace an existing workspace.

```bat
conda activate torment
set "PAPER_HISTORY_PANDOC=C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\pandoc\pandoc-3.11\pandoc.exe"
set "PAPER_HISTORY_TECTONIC=C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe"
set "PAPER_HISTORY_TEX_CACHE=%USERPROFILE%\.codex\reports\kernel_history_paper_20261001\tectonic-cache"
python -I -B papers\KERNEL_HISTORY_AND_COMPARISON\source\build_publication.py --workspace "%USERPROFILE%\.codex\reports\kernel_history_paper_20261001\publication-reader-build-01"
```

The existing Markdown -> Pandoc AST -> LaTeX -> Tectonic workflow uses 11-point
TeX Gyre Pagella on A4 and the unchanged vector figures. Tectonic uses
`--only-cached`; missing cached resources fail rather than download packages.
Disposable logs, renders and font caches belong in the external workspace.
Edit the publication Markdown and rebuild rather than editing generated TeX.

`source/make_figures.py` can render the included inert excerpt using the existing
NumPy/Matplotlib environment. It was not run during publication finalization;
figures and data remain identical to the accepted review. `source/prepare_evidence.py`
requires the separately available local P3 packet and only reads inert JSON.
Neither script makes the full local evidence accessible from this repository.

After a future meaningful edit, render and visually inspect every PDF page.
`publication_checks.json` describes the identified publication PDF, not future
rebuilds. Finalization checked status-only changes, unchanged mathematics/data/figures,
document links, build output and all 12 pages; it did not rerun scientific kernels.
