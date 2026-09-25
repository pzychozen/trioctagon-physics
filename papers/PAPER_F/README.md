# Paper F publication package

**Scientific source: accepted v0.2. Publication build completed for GPT/Hilmir PDF inspection. GitHub publication is not authorized.**

- Public manuscript: `PAPER_F_PUBLICATION_v0.2.md`
- Final typesetting source: `paper_F_v0.2.tex`
- PDF: `PAPER_F_PUBLICATION_v0.2.pdf` (22 pages)
- Bibliography: `BIBLIOGRAPHY.md` and `references.bib`
- Attribution and earlier evidence: `SUPPLEMENTARY_RECONSTRUCTION_RECORD.md`
- Exact support selection and reasons: `records/support_allowlist.json`
- Full delivery status: `PUBLICATION_CHECKPOINT.md`

The public paper preserves all 106 display-math blocks and 64 equation tags from the controlling source, with the complete Theorem 8 and Appendix D argument. The editorial conversion moves review/build history into the supplement, removes the unrelated observer-lock literal from the paper, and supplies one intrinsic symmetry figure. It does not change the science.

## Reproduce in a copy

Copy only the paths in `PUBLICATION_ALLOWLIST.txt` into a separate workspace, retaining their repository-relative layout. Run from the copied `papers/PAPER_F` directory. These commands intentionally write outputs into that copy; use new empty directories for each isolated run.

The execution record pins Python 3.12.14, SymPy 1.14.0, Matplotlib 3.11.2, NumPy 2.5.3, Pillow 12.3.0 and pypdf 6.19.0. The verifier needs SymPy; the figure needs SymPy, NumPy and Matplotlib; PDF inspection needs pypdf, Pillow and Poppler. Exact dependency versions are recorded in `records/reproducibility_manifest.json`.

```text
python -B -X utf8 prepare_publication.py
python -B -X utf8 generate_figure.py
python -B -X utf8 verify_isolated.py ABSOLUTE_NEW_VERIFICATION_DIRECTORY
```

The verifier copies exactly four inputs to a fresh repository-shaped tree, statically reads two source snapshots and consumes the saved 18-row CSV. It imports no kernel module and evolves no model state. All 131 predicates reproduce the accepted v0.2 data. New stdout is clearly separated from the original validation.

Set the environment variables below to existing tools/cache, then build:

```text
PAPER_F_PANDOC = absolute path to Pandoc 3.11
PAPER_F_TECTONIC = absolute path to Tectonic 0.17.0
PAPER_F_TEX_CACHE = absolute path to a populated compatible Tectonic cache
PAPER_F_SYSTEM_FONTS = system font directory (default C:/Windows/Fonts)

python -B -X utf8 build_publication.py ABSOLUTE_NEW_BUILD_DIRECTORY
python -B -X utf8 inspect_pdf.py ABSOLUTE_RENDER_DIRECTORY --poppler ABSOLUTE_PATH_TO_PDFTOPPM
```

The build copies source inputs to a new workspace, runs Pandoc with explicit backslash-math support, and compiles with Tectonic's `--only-cached` option. It uses TeX Gyre Pagella text/math fonts from the cache and fixes `SOURCE_DATE_EPOCH=1790294400`. The tool identities and cache inventory are in the records. A newly installed Tectonic requires its resources to be populated separately before this offline build. Binaries, font caches, environments and third-party source PDFs are intentionally not included.

Two fresh build directories produced identical TeX and PDF bytes. A separate copied-source run reproduced the manuscript, bibliography, fidelity files and all four figure exports/inputs byte-for-byte.

## Verify identities

`SHA256SUMS.txt` hashes every proposed publication file except itself. Its own identity is recorded in the returned checkpoint receipt outside that manifest when needed. `PUBLICATION_ALLOWLIST.txt` enumerates exact repository-relative paths; it is a proposal, not staging authorization. `PUBLICATION_ALLOWLIST.md` gives the role of every path.

`records/preflight.json` is an intentionally **local-only** preservation inventory of unrelated working files. It is excluded from the publication allowlist. It is retained locally to substantiate preservation, not copied into the proposed package.

All original research records and predecessor editions remain at their original paths unchanged. No accepted kernel, test, paper or continuity file was edited. Nothing was staged, committed or pushed.
