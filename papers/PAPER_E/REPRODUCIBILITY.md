# Reproducibility and execution scope

All commands below run from `papers/PAPER_E/`. The package never needs to import or edit the current installed kernel. The publication PDF can be rebuilt using the supplied figure PDFs without executing any historical source.

## Minimal verification

`python -B package_tools.py verify` checks every listed SHA-256 and the exact public-file allowlist. It does not stage anything. It expects this folder in its repository-relative location. `SHA256SUMS.txt` uses paths relative to Paper E and may also be checked with a standard SHA-256 utility.

`python -B check_symbolic.py` performs 66 exact predicates with SymPy and writes only `evidence/symbolic_results.json`. It imports no kernel. The written proofs remain the authority for hypotheses, extrema classification, inequalities and historical scope.

`python -B inspect_package.py` checks source-copy identities, frozen replay-data identities/equalities, approved B/D identities, manuscript structure, complete equation retention, PDF page count, embedded figure count and build-log layout failures. It writes `evidence/package_checks.json`. It does not regenerate data or figures. The authoring execution additionally used Poppler rendering and visual inspection of all manuscript pages; that human/model-visible inspection is recorded separately rather than falsely inferred from text extraction.

## Figures without simulation

`python -B generate_figures.py` uses the supplied `evidence/plot_data.npz` plus analytic formulas to produce the 11 PDF/SVG/PNG figure sets and figure manifest. It does not import historical source or run a parameter sweep. Each figure's caption states its input and normalization. The source-generated examples are finite samples; the analytic figures are plots of the exact stated functions, not polygonal substitutes for their proofs.

The supplied plot data are therefore sufficient to redraw the scientific figures. Their hash is checked before acceptance. Rebuilding compressed arrays or SVG metadata on another platform need not reproduce container bytes even if numerical arrays agree; compare arrays and record the new build identity rather than overwriting approved provenance without attribution.

## Optional four fixed source replays

`python -B recover_plot_data.py` is an optional data-regeneration step, already executed once for this manuscript. It reads only the copied source snapshots, loads an isolated synthetic Python package, and writes the NPZ and its result record. It executes four fixed runs: baseline, EMA baseline, subcritical and critical. It does not execute the GUI, full diagnostics wrappers, RSB, optional cloned probes or parameter scans. Python bytecode writes are disabled. The source snapshots and original saved CSVs remain unchanged.

The critical run intentionally reaches the historically saved numerical failure. Overflow/invalid warnings are recorded, not repaired by clipping or changed equations. Exact array comparison uses `equal_nan=True`. Finite events exclude nonfinite metrics. Metric indices are aligned to endpoint rows, so first nonfinite metric endpoint 1278 precedes first nonfinite Z row 1279. The subcritical run remains finite. The raw saved CSVs contain no original execution log; the new results must be labelled deterministic re-execution output.

`prepare_evidence.py` is an authoring-time preservation-copy utility and requires the original workspace layout. The prior `evidence/accepted_reconstruction/verify_historical_z.py` is an unchanged historical verification artifact with original-workspace path assumptions; it is **not** the portable Paper E entry point and should not be run as a new sweep.

## Build the complete paper

Set `PAPER_E_PANDOC` and `PAPER_E_TECTONIC` to existing executables and `PAPER_E_TEX_CACHE` to a populated Tectonic resource cache. Then run `python -B build_publication.py`. The build is cached/offline and does not install a TeX environment or rebuild earlier papers. It preserves all Markdown prose, 40 displayed equation bodies and 11 figure references through an inspected Pandoc AST. Tables receive explicit column widths; display wrappers preserve numbering and prevent overrun. The generated LaTeX is included.

This execution used Python 3.12.14, NumPy 2.5.3, Matplotlib 3.10.7, SymPy 1.14.0, Pandoc 3.11 and Tectonic 0.17.0. Exact executable hashes are in `publication/build_record.json`. Matplotlib and SymPy were loaded from existing local dependencies; no environment is copied into the proposed package. `runtime.py` optionally accepts a platform-path-separated `PAPER_E_PYTHON_PATH` pointing at existing library directories. It confines Matplotlib's writable cache to `.build/`.

Example PowerShell invocation after selecting existing tools:

```powershell
$env:PAPER_E_PANDOC = 'C:\path\to\pandoc.exe'
$env:PAPER_E_TECTONIC = 'C:\path\to\tectonic.exe'
$env:PAPER_E_TEX_CACHE = 'C:\path\to\populated\tectonic-cache'
python -B build_publication.py
```

`SOURCE_DATE_EPOCH` is fixed to 23 September 2026. Fonts use cached TeX Gyre Pagella and Latin Modern resources. The generated local font configuration/cache stays under `.build/`. PDF-byte identity is recorded for the actual build; a changed toolchain warrants a separately attributed artifact and visual review, not a claim of identical bytes.

## Preservation and allowlist

The authoring baseline was captured before replays/figure execution. `package_tools.py finalize` compares 512 protected pre-existing files and Git HEAD/index/outside status with that baseline, then writes the receipt, explicit allowlist and manifest. It is local closeout machinery, not a prerequisite for a reader to rebuild the paper. The baseline lives in `.build/` and is not silently recreated if present.

Run `finalize` only after all intended public edits, then `verify`. The manifest excludes itself to avoid a self-hash cycle. The allowlist is an inventory, not Git staging. No publication operation is included in any script.
