# Paper B publication package, draft v0.1

The main deliverables are the [complete manuscript](PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_DRAFT_v0.1.md) and the [publication PDF](publication/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_DRAFT_v0.1.pdf). The [symbol/theorem sheet](PAPER_B_SYMBOLS_AND_THEOREMS_v0.1.md), [references](PAPER_B_REFERENCES_v0.1.md), and [reference ledger](PAPER_B_REFERENCE_LEDGER_v0.1.md) accompany them.

This is a saved review draft. It is not uploaded, published, committed or frozen. The validation report records scientific scope, production checks and the unresolved bibliographic locator BIB-01 separately.

## Rebuild

Use Python 3.12 in an isolated environment with requirements.txt, Pandoc 3.11 and Tectonic 0.17.0. The figure generator and algebra checker import only the existing geometry module for exact coordinate comparison; they do not execute the recurrence or UI.

Run build.ps1 with -PythonExecutable pointing to that environment, or run these scripts in order:

1. check_manuscript_algebra.py
2. generate_figures.py
3. build_publication.py
4. verify_publication.py

The local build reuses the existing Paper C Pandoc/Tectonic executables read-only. By default it locates them relative to this checkout, under the project-level reconstruction/publication/paper_C/build directory. To use another installation, set PAPER_B_PANDOC and PAPER_B_TECTONIC to executable paths and PAPER_B_TEX_CACHE_SOURCE to a populated Tectonic resource-cache directory.

build_publication.py copies that resource cache into this package's ignored .build directory before compilation. It invokes Tectonic with --only-cached and writes no resources back to Paper C. The included paper_B_final.tex also permits direct compilation from this package directory with an appropriately configured Unicode TeX installation; the measured local build uses the pinned tools and TeX Gyre Pagella fonts.

The local run used the existing Python 3.12.14 interpreter, reading SymPy 1.14.0 from its environment. New plotting/PDF dependencies were installed only into .build/plotdeps. The scripts find that directory when present. No dependency was installed into an existing kernel environment. The requirements file records the actual packages used; tool executable hashes are in publication/build_record.json. No binary tooling or TeX cache is proposed for Git.

## Reproducibility and receipts

SOURCE_DATE_EPOCH is fixed to 2026-09-23 UTC. Vector figure PDFs use a fixed timestamp; the PNG previews are deterministic with the pinned dependencies. The preserved source, generated TeX and vector figures are the complete scientific build inputs. Publication logs describe the final successful build.

The bounded checker covers 25 groups of exact algebra, including all 27 ambient transport compositions. A group count is not a theorem proof count. No scientific suite, parameter sweep or trajectory campaign is part of this task.

evidence/source_inputs.json gives hashes for the 17 selected source and implementation inputs. evidence/preservation_baseline.json.gz.b64 is the gzip/base64-encoded start-of-task JSON baseline of 253 protected paths and the two repositories' Git status. It is preserved as a compact receipt and is decoded by closeout.py.

The final SHA256SUMS.txt covers every proposed package file other than itself. PROPOSED_GIT_ALLOWLIST.txt lists exact repository-relative paths, including itself and the checksum file. Files under .build are disposable local build intermediates and visual-QA renders; they are intentionally excluded from the allowlist. No blanket directory staging command is supplied.

To verify the saved package without changing any file, run check_package.py. Rebuilding may change tool-version receipt text if a different Python distribution is used. After intentionally editing a draft, regenerate the package manifest with closeout.py only after completing the required verification; do not confuse a regenerated checksum with scientific acceptance.

The [Codex publication validation report](CODEX_PAPER_B_PUBLICATION_VALIDATION_v0.1.md) and [preservation/status receipt](PAPER_B_PRESERVATION_AND_STATUS_v0.1.md) state what was actually checked. No new independent Claude review or joint acceptance is asserted.
