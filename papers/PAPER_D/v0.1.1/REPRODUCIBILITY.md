# Rebuilding and checking Paper D v0.1.1

Use an existing Python installation with the versions in `requirements.txt`. This package has no historical-source or kernel import. `PAPER_D_PYTHON_PATH`, if needed, names an existing third-party library directory; it must not point at a source archive or supply replacement science modules.

Set `PAPER_D_PANDOC` and `PAPER_D_TECTONIC` to existing executables and `PAPER_D_TEX_CACHE` to an already populated Tectonic resource cache. `build.ps1` runs figure/manuscript checks, the bounded definition check and the complete Markdown-to-TeX-to-PDF builder. `build_publication.py` may also be called directly when using the unchanged supplied figures. It uses Tectonic's `--only-cached` mode. No installation or network source retrieval is part of the build.

The builder writes only inside this revision directory. It never writes the parent v0.1 sources, PDF or logs. For a later independent reproduction, copy these revision files to a separate scratch directory first; retain the delivered manifests and captured outputs for comparison.

The final revision was built with existing Python 3.12.14, Pandoc 3.11 and Tectonic 0.17.0. Exact executable hashes and `SOURCE_DATE_EPOCH` are in `publication/build_record.json`. No new full independent rebuild is claimed in this bounded revision: the parent's independent rebuild remains prior evidence, while this revision records its own build, structural fidelity, bounded checks and all-page visual QA.

`verify_package.py` only reads the revision SHA-256 manifest and explicit allowlist. It does not run the science, regenerate figures, stage paths or contact Git. `SHA256SUMS.txt` excludes itself to avoid self-reference. The explicit combined publication list additionally names all preserved v0.1 paths; validate those with the parent's existing manifest.

The 42 display-math bodies are preserved by the Pandoc conversion. The builder only changes display wrappers and two table column widths; the manuscript itself sets a smaller font around the reference block. All nine diagrams and their coordinate source are unchanged. Counts and final layout disposition are in `evidence/qa_final.json`.
