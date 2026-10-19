# Paper II v0.1 — reproduction from a separate writable copy

The accepted PDF is `PAPER_II_PAIRED_DRIVING_EXTERIOR_IDENTIFIABILITY_v0.1.pdf` (33 pages), SHA-256
`c376ce81534a34778c10d856282cefe1678e9d0af3943df64715513fbb41a4d5`.
Publication preserves that supplied compiled artifact. Running a reproduction helper may overwrite files in its working directory; never run it in the immutable publication edition or a protected source tree.

## Prerequisites and source closure

Copy the nine root TeX files, complete `figures/` and `data/` directories, and `tools/build.py`, `tools/check_manuscript.py`, `tools/render_figures.py` into an isolated writable directory, preserving relative paths. These are the complete local typesetting/check/figure dependencies. The private `input/`, review archives, intake/sealing tools and publication closeout are not required.

Use an already available Python environment, an existing Tectonic 0.17-compatible compiler and a populated offline cache. The original manuscript checks used Python 3.11.15, SymPy 1.14.0 and NumPy 2.4.4; the internal review also replayed those checks on a different recorded environment. This is not a cross-platform build certification. Optional static figure reproduction also needs Matplotlib. No package, compiler, cache, dependency or font binaries are supplied here.

The TeX dependencies include article, amsmath/amssymb, unicode-math/fontspec, lmodern, geometry, mathtools, booktabs, array, graphicx, xcolor, fancyhdr, needspace and hyperref. Fonts are TeX Gyre Pagella (text and math) and Latin Modern Mono, resolved through the existing toolchain/cache. Do not copy system font files into a redistributed archive.

## Typeset

Activate your existing environment in Windows CMD. Set `PAPER_II_TECTONIC` to the actual existing compiler executable and `PAPER_II_TEX_CACHE` to the actual populated offline cache directory. In the isolated copy:

```bat
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUTF8=1
python -X utf8 -B tools\build.py
```

The unchanged helper copies the specified cache into its local `cache/`, uses process-local temporary/font-cache settings, and requests `--only-cached --untrusted`. It records numbered compiler console/build files. It does not install missing prerequisites. The helper writes `build/manuscript.pdf` and copies it over the root PDF filename in that writable copy. Identical source need not produce identical PDF bytes across toolchains; do not substitute a rebuild for the accepted artifact silently.

## Manuscript-local checks and optional static figures

Ensure `cache/` and `evidence/` exist in the writable copy. In Windows CMD:

```bat
if not exist cache mkdir cache
if not exist evidence mkdir evidence
python -X utf8 -B tools\check_manuscript.py
```

This verifies displayed identities, the single printed polynomial substitution, fixed-data transcription and reference/dependency closure. It is not an instruction to run the native kernel, old research suites, reception quadrature, a benchmark or a carrier evolution.

Optional redraw, using the unchanged selected data:

```bat
python -X utf8 -B tools\render_figures.py
```

The renderer overwrites the five computed figure sets and figure ledger in the writable copy. Rebuild afterward and visually inspect every resulting page. No prior all-page review automatically applies to a changed PDF. Five underfull-paragraph notices and recorded package-definition notices occurred in the accepted build; those are not overfull clipping, missing characters or unresolved references.

The edition contains the necessary reproduction inputs, not all private archival evidence. `data/SOURCE_INDEX.json` records old source locations; its `path` entries are the included data files, whereas `source` entries identify their retained history. See [access and evidence](ACCESS_AND_EVIDENCE_MAP.md) for that distinction.
