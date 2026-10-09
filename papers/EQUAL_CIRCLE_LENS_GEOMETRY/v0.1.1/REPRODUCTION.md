# Reproduction of the lens mathematical supplement

The delivered PDF, TeX, bibliography, six figure families and original numerical data are fixed edition artifacts. Work in a disposable copy of this edition folder when reproducing; scripts can overwrite generated files. Python support uses only stated formulas and imports no project runtime or historical source. No scientific simulation is needed.

From that copy, use an existing Python 3 environment with SymPy, NumPy, mpmath and Matplotlib. The owner used Command Prompt and `conda activate torment`; that environment name is not required for these public scripts. Relevant recorded versions: Python 3.11.15, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.4.4, Matplotlib 3.10.9. This is a reproduction description, not a new environment certification.

```text
python -I -B tools/lens_checks.py
python -I -B tools/make_figures.py
```

The supplied evidence directory exists for script output. The checker writes `evidence/CHECK_RESULTS.json`; figure generation writes the figures/data and its generator record. Execution records may contain the executing machine's interpreter path: inspect them before any later redistribution. The retained public `evidence/AUTHOR_CHECK_SUMMARY.json` omits those machine details and identifies its actual origin. Finite checks do not replace proofs. This preparation did not run either figure generator or rerun the accepted lens checker.

Compile from the edition directory using an existing Tectonic installation, keeping `figures/` and `references.bib` beside `manuscript.tex`:

```text
tectonic -X compile --keep-logs --keep-intermediates --outdir build manuscript.tex
```

Create `build` first if your toolchain requires it. A XeLaTeX/BibTeX workflow is also possible; run XeLaTeX, BibTeX and two more XeLaTeX passes against manuscript.tex. Engine, font and library versions can change PDF bytes. The accepted/public PDF is identified by hash, not a promise of cross-host byte equality. Render and inspect any regenerated PDF before using it.

No source file or script needs private absolute paths. Historical evidence is referenced through SOURCE_REFERENCES.json, not executed. The manuscript's references to full logs, private review packets or original source collections describe the preserved owner-side supplement; those collections are deliberately absent from this public subset.

The two public Python files are environment-only derivatives of the accepted support scripts: the owner-specific conda assertion was removed and conda metadata uses `.get`. Formulas, cases, numerical precision and tolerances are unchanged. Original scripts remain preserved in the accepted edition. The PDF, TeX, bibliography, all figure files and data are byte-identical to that edition.
