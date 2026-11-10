# Building the research edition

Title: Spatial Observation and Causal Transport with Storage in the Reciprocal Chiral Exchange Candidate  
Author: Hilmir Frímann Halldórsson (pzychozen)  
Version: v0.1, prepared 10 November 2026, Atlantic/Reykjavik  
Status: Research edition v0.1 — project-internal review complete; author-authorized for repository publication.

The complete manuscript content is self-contained in this edition: `main.tex`, `sections/`, the editable `references.tex` bibliography, and the two vector figures in `figures/`. Compilation reads no content from Downloads or unrelated historical workspaces.

Open **Command Prompt**, activate the requested environment, and work in this edition directory:

```bat
conda activate torment
python build.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --build-dir C:\path\outside\edition\build
```

Use an existing cached Tectonic installation elsewhere if needed; quote paths containing spaces when typing directly in Command Prompt. Omitting `--build-dir` creates a fresh system temporary directory. The helper rejects intermediates inside the edition. Its recorded version is Tectonic 0.17.0. It uses `--only-cached --untrusted --keep-logs --keep-intermediates`; it does not fetch TeX packages or enable shell escape. An existing populated TeX cache is required.

The canonical output is `SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf`. `SOURCE_DATE_EPOCH` is fixed to 10 November 2026; the external receipt records actual UTC build times separately. It also hashes every TeX file and figure PDF consumed. The original submission build is retained as `verification/build08/` in the unchanged review archive. Publication requires a fresh corrected build and a new hash-bound document/visual record; the original build08 receipt does not certify revised bytes. Fonts use available Latin Modern assets; theorem bodies and equation prose are upright, with a bold Gram matrix and upright dimensional symbols. All final font resources are embedded.

The supplied figures are sufficient for compilation. To regenerate the editable PDF/SVG figures and PNG previews in the same activated environment:

```bat
python figures\render_figures.py
```

This uses existing Matplotlib 3.10.9 and deterministic metadata/hash salt. It draws abstract account and support diagrams; it performs no trajectory simulation or scientific-suite replay. The recorded Python is 3.11.15 in `torment`, with pypdf 7.0.0 for document inspection. No dependency was installed for this task.

The original document-check scripts and Windows environment records are preserved in the unchanged review archive. For publication, refresh their status expectations and working/output paths, run them against the new corrected build, then render and individually inspect every final page. Do not reuse build08 or its page-inspection record to certify revised bytes. Record the actual compiler, renderer, PDF digest, page count, reference checks and visual disposition in the new publication verification records. Rendering alone is not visual inspection.

The final publication build is now recorded in `verification/publication_build01/`; `verification/BUILD_EXECUTION.json` records the actual Windows command and successful exit. `verification/DOCUMENT_CHECKS.json` and `verification/VISUAL_INSPECTION.json` certify the final 25-page PDF. See `ACCESS_MAP.md` for the public evidence layout and local closeout contents. The historical build08 and Linux reviewer build are distinct retained evidence.
