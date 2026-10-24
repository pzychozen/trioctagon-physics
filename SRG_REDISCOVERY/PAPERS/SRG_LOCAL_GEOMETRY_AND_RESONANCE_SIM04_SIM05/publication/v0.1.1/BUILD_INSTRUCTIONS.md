# Build the manuscript only

The editable sources are `manuscript.tex` and `references.tex`. Figures are unchanged PNG assets under `figures/`. No evidence script is required to build the paper.

Use Windows Command Prompt and the existing environment, as requested:

```bat
conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\PAPERS\SRG_LOCAL_GEOMETRY_AND_RESONANCE_SIM04_SIM05\draft\v0.1.1
python -B build_document.py
```

The supplied script defaults to the existing Codex Tectonic executable on this host. Override its location with `set SRG_TECTONIC=C:\path\to\tectonic.exe` if the installed version changes. It uses a private candidate cache, runs Tectonic with `--untrusted` (no shell escape), writes a separate build directory, extracts PDF text, checks embedded fonts, and renders every page with the bundled Poppler. It imports only document tooling, not NumPy or any evidence code.

The delivered ZIP deliberately excludes compiler caches. On another machine, use a configured TeX system with XeLaTeX, fontspec, TeX Gyre Pagella/Heros, Latin Modern Mono, amsmath/amsthm, geometry, graphicx, booktabs, tabularx/longtable, pdflscape, caption, xcolor, fancyhdr, enumitem and hyperref. Run XeLaTeX sufficiently many times to resolve references; the bibliography is `references.tex`, with no external bibliography service. Alternatively use:

```bat
tectonic -X compile --untrusted --keep-logs --reruns 2 manuscript.tex
```

Tectonic may fetch missing typesetting dependencies into its cache. The local build helper's `--fetch-tex-dependencies` switch permits that same document-only operation; ordinary subsequent builds are offline. R1 was built offline, using a private copy of the preserved sibling v0.1 compiler cache. The helper's only R1 change is that cache-copy source. For a portable build, use the direct Tectonic command with a configured private cache instead.

All figures, tables and numerical claims come from retained accepted inputs. Do **not** run historical programs, replay tools, independent scientific checkers or prior random-checkpoint verification to rebuild this manuscript. `prepare_r1.py` records the one-time R1 input intake and literal approved patch; it refuses to overwrite an existing intake. Earlier intake and packaging scripts are preserved under `provenance/v0.1/` for inspection and were not executed. The current `finalize_r1.py` checks document/file identities and packages the candidate; it does not calculate scientific results or invoke Git.

Page rendering and file hashes are environment-specific reproducibility records. The accepted review ZIP identifies the exact delivered PDF bytes; a later compiler/environment may produce different PDF metadata or layout without changing the source. Any edited candidate needs a new visual page inspection before delivery.
