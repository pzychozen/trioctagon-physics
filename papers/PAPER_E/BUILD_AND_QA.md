# Paper E build and bounded validation

Date: 23 September 2026. Attribution: new Codex paper preparation and artifact verification. Scientific acceptance: **PENDING_GPT**. No new Claude review was requested or represented.

## Final manuscript build

- Complete 23-section manuscript plus references, approximately 10,500 whitespace-delimited words.
- Final publication PDF: **28 A4 pages**, author metadata present, 40 numbered displayed equations and 11 figures.
- Markdown -> Pandoc JSON AST -> complete LaTeX -> cached/offline Tectonic PDF.
- All 40 display bodies survive the transformation exactly. All displays fit at their natural mathematical font size; no equation required the wrapper's scale-down branch.
- Final TeX log has no overfull boxes, underfull boxes or missing-character warnings. Benign package notices concern unicode-math command selection and caption hyperlink behavior with the intentionally nonfloating figure layout.
- Actual build stdout, TeX log, tool identities and PDF/source hashes are in `publication/`; these are newly generated build records.

Final PDF SHA-256: `0d2a1e0b40d96f39c3929ad3c0a3c833b7eebebffc336b452ea9e1004f88880d`.

## Visual inspection

All 28 pages of the final PDF were rendered with Poppler at 100 dpi and inspected in four contact sheets. Figure-heavy pages and the references were also inspected at individual-page size. The eleven source figure PNGs were inspected together. The final review confirms readable equations and tables, captions kept with figures, consistent page numbering, visible axis labels, and no clipped text or missing glyphs.

Layout corrections made during authoring: replaced an unbreakable reference path with the exact path in the separate ledger; moved the four-display figure after its conditional inverse to reduce unused page area; placed the third-axis labels inside each 3D panel to prevent neighbouring panel backgrounds from clipping them. These are presentation corrections only. The fixed numerical replay data were not regenerated for these corrections.

The final contact sheets and full-page rasters are QA intermediates under ignored `.build/`, not publication paths. Full vector figure PDFs and SVGs, plus PNG previews, are included in the public package. Their captions distinguish analytic curves, algebraic illustrations and numerical trajectories. No scientific comparison uses the viewer's percentile scaling.

## Mathematical and data verification

`check_symbolic.py`: **66/66 exact symbolic predicates passed**. These check specified trigonometric/polynomial identities and the exact potential-increase witness. The written proofs provide the remaining inequality, extrema, branch and historical hypotheses. A predicate count is not a theorem count.

Four fixed source-body replays generated the figure data. The preserved subcritical and critical series agree exactly in Z coordinates, full v and J after parsing CSV numbers, treating corresponding NaNs as equal. Recovered phase strength is zero. Finite threshold-event counts are 26 and 1277. Critical first nonfinite Z/J row is 1279; first nonfinite full-statistic endpoint is 1278. The subcritical series remains finite. Overflow warnings are retained as part of the critical run's provenance, not repaired or relabelled as physical behavior.

The earlier **63-check, 23-configuration** result record is included unchanged and reused. Its tests were not relabelled new tests or rerun as another sweep. Its source verification script remains an evidence artifact with original-layout assumptions.

`inspect_package.py`: **51/51 bounded artifact checks passed** for the final build. This includes source-copy hashes, earlier and new result integrity, frozen-data identity, baseline/EMA equality of Ω, both saved-run comparisons, expected event/failure indices, 23-section and 40-equation structure, 11 complete figure sets, build hashes, natural-size equations and unchanged approved B/D PDF hashes. The inspection script reads arrays and artifacts; it does not execute science.

## Preservation and Git boundary

The final preservation receipt compares **512 pre-existing files** to the pre-execution baseline, including previous papers, kernels and original diagnostic evidence. It also compares Git HEAD, the full index identity and status outside Paper E. All are required to remain unchanged by `package_tools.py finalize` before the manifest is emitted.

Starting and final local HEAD: `505821a77c3aa1df89a2c400c65ba33149e635c8`.

Tracked/index status remains clean. Existing outside-Paper-E untracked files remain intentionally untouched. Paper E is a new untracked package; `.build/` is ignored. The explicit proposed allowlist and SHA-256 manifest include only public files under `papers/PAPER_E/`. No staging, commit, push, remote fetch, cleanup, kernel adoption, earlier-paper rebuild or publication action was performed.

The preservation receipt and manifest are the final machine-readable closeout records. The manifest excludes itself; all other public files, including the proposed allowlist and this report, are hashed. The remaining scientific items are the six-gap spatial registration and original saved-run environment/commit attribution. No physical energy law is claimed.
