# Preparation report — NATIVE_PHASE_SPATIAL_PAPER_01

**Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map**  
**Review draft v0.1 — awaiting GPT/author manuscript review**  
2 November 2026, Atlantic/Reykjavik

## Outcome

The complete companion manuscript combines both accepted investigations, including the branch-resolved overlap correction and its analytic nonidentity witness. It gives the exact positioned-axis correspondence, complete decoded step, universal proper-rotation theorem, corrected observer dependencies and interpretation limits. No substantive mathematical contradiction or missing assumption was found during assembly. The author is not asked to assign a material feature to complete this review draft.

Final PDF: **13 pages**, A4, **138693 bytes**.  
File: `NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf`  
SHA-256: `8eb97758c893254827d984bc32d6893fcf866b5cd6639876e35d9014520853a6`.

Build, document checks, all-page visual inspection and source preservation: **PASS**. The portable ZIP carries this same inspected PDF; no concrete unresolved preparation issue remains.

## Sources and preservation

All new files are confined to `C:/TORMENT/TRIOCTAGON_new/research/NATIVE_PHASE_SPATIAL_PAPER_01`. The fresh workspace was unoccupied. Applicable ancestor instruction paths were checked; no applicable local AGENTS.md was present. No subagents were used.

The 24 source/evidence files actually used were copied into the compact `evidence/` and `provenance/` layout. Original paths, versions, locators and hashes are in `provenance/source_manifest.json` and the source ledger. Both accepted proof hashes match the work order. Copies and original inputs were checked again after preparation and remain byte-identical. The hash-matched fixed-gap report and its available acceptance review were reused; no archive reconstruction or audit was necessary.

The bounded lookup did not supply separate local phase/spatial GPT review files. The current order explicitly records both accepted dispositions and every operative correction; this is the recorded acceptance source. The published predecessor and primary files were read from the retained publication worktree. The original checkout was neither queried with Git nor synchronized. Reference commit `634ff13b666604d5caed11cc3731dcb5a863ff6c` identifies reading sources only.

The predecessor's `manuscript/main.tex` supplied the established paper style. Its document build/check utilities were read and adapted into new document-only utilities in this workspace; they were not executed in place. Primary scientific snapshots are flat under `provenance/primary/`; unrelated archives, PDFs and duplicate source hierarchies were omitted.

## Required corrections

| Requested correction | Incorporated location |
| --- | --- |
| “full-state relation” replaces “physical-state relation” | Theorem 3.2, `manuscript/reconstruction.tex`. |
| Analytic witness distinguished from numerical native-step evaluation; acknowledge analytic differentiation of F | §4 and Appendix A, `overlap.tex` and `witness.tex`. |
| Section-changed overlap unit factor normalized explicitly | §4.1 equation (4.9), `B_sec,h/abs(B_sec,h)`. |
| Separate memory update from current-memory observation | §7.1 and Table 3, `observations.tex`; source functions `advance_ema`, `ema_scalar`, `observe_ema` read without execution. |

Notation is reconciled with Ψ, F-hat and κ as requested. Norm, native phase, observer angle, raw chirality, coherence, relative areas/phases, complex prestage and decoded vectors are distinct. Cover, metadata and README state the review status. Author attribution includes the correct accents; no affiliation, ORCID, funding, DOI or external peer review is invented.

The exact frame and dependency tables supply the needed static information; no new diagram or figure was necessary. No geometry builder, trajectory or observer was run for illustration.

## Toolchain and actual document commands

- Windows Command Prompt with `call conda activate torment`; Python **3.11.15** at `C:\Users\Notandi\miniconda3\envs\torment\python.exe`.
- Existing cached **Tectonic 0.17.0** at `C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe`.
- Bundled Poppler **26.07.0**, `pdftoppm.exe` and `pdfinfo.exe`, under `C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin`.
- Existing bundled **pypdf 6.10.0**, loaded through its existing site-packages directory for document extraction/checking. No package installation or persistent environment change occurred.

The PDF skill's creation marker ran successfully once before authoring. Source-copy and compilation commands were:

```bat
call conda activate torment
python -I -B C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_SPATIAL_PAPER_01\prepare_sources.py
python -I -B C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_SPATIAL_PAPER_01\manuscript\build.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe
```

The copy command passed. Initial compiler attempts identified an undefined Arg macro and an uncached small italic text-font variant in a mathematical theorem sentence. The macro was declared and the quantifier sentence moved to ordinary theorem prose; no resource was installed. Two underfull table-cell warnings were repaired by ragged-right row labels. The final build exited **0**, with normal reference-resolving passes and **no undefined citations/references, missing glyphs, overfull or underfull boxes, or LaTeX/package warnings**. The cached resources sufficed.

The final build uses only process-local `FONTCONFIG_FILE`, `FONTCONFIG_PATH`, `SOURCE_DATE_EPOCH`, `TMP` and `TEMP`; new font cache and temporary files stay under `build/`. A portable reproduction may have different PDF bytes with another document toolchain, without implying a scientific change.

Rendering and metadata inspection used:

```text
pdfinfo NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf
pdftoppm -r 120 -png NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf renders/page
```

An initial 110-dpi draft render preceded the final 120-dpi inspection. `pdftotext` was unavailable, so text extraction used existing pypdf instead. No extraction claim relies on that unavailable command.

```bat
python -I -B manuscript\verify_document.py --python-packages C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages
python -I -B manuscript\check_reference_links.py
```

Both commands completed successfully in the activated environment. The first checks document structure, fonts, metadata, citations, references, local/internal links, source bytes and required editorial changes; the second checks external bibliography URL availability with HTTP HEAD, not a literature search or Git operation. All six external URLs returned HTTP 200. All 64 internal PDF links resolved, all four local evidence/reference links exist, and all 21 used fonts are embedded. These counts describe document checks, not scientific results.

## Final visual inspection

Every one of the 13 pages was rendered and directly visually inspected, including cover, author accents, theorem blocks, all equations, all three tables, page transitions, appendix and references. No clipped/overlapping content, missing glyphs or unreadable table entries were found. Two final wording refinements kept the EMA's literal 0.01 with its sentence and clarified pointwise versus finite-sum representative cancellation. They affected only pages 7, 10 and 11; all three were visually inspected again. The other ten final page PNGs are byte-identical to the initially inspected renders.

`inspection/VISUAL_INSPECTION.json` records the final PDF hash, all page image hashes and per-page inspection notes. Rendered PNGs remain in `renders/` in the workspace and are excluded from the compact review ZIP. Their record is an account of the actual visual review, not an automated substitute for it. The final delivered PDF is the inspected PDF.

## Package and stopping status

The package includes the PDF, complete LaTeX/bibliography sources and document utilities, unchanged phase/spatial evidence, compact primary snapshots, source manifest, claim ledger, README, this preparation report and final inspection/build records. `PACKAGE_MANIFEST.json` hashes every payload member except itself; the checksum of the final archive is recorded in the adjacent `.zip.sha256` file. Members, sizes, hashes, safe relative paths, CRCs and the PDF/inspection identity are checked once after final assembly. No scientific code is executed during packaging.

No accepted source or repository file was edited. No project import, native step, trajectory, parameter scan, new numerical test, old scientific helper rerun, geometry construction, observer advance, certificate/publication re-audit, package installation, Git command, push, release or DOI deposit occurred. The local/source checks and HTTP availability checks concern this manuscript only.

**Unresolved issue:** none identified for this manuscript preparation. The draft awaits GPT/author review of the assembled paper. No material attachment has been selected and no successor investigation or publication action has been started.
