# Build and verification — v0.2

The editable document consists of GEO_ORIGINS01_v0.2.tex, history.tex, retained_mathematics.tex, references.tex and the two figure PDFs. The new opening and retained mathematical account are separate source files. No kernel, TORMENT installation, private archive or original chat record is needed to compile the paper.

Use a working copy with an existing compatible Tectonic/LaTeX toolchain. The accepted build used Tectonic 0.17.0 and existing offline resources, with SOURCE_DATE_EPOCH=1792368000. Create a separate output directory and run:

    tectonic -X compile --only-cached --untrusted --keep-logs --keep-intermediates --outdir <external-output> GEO_ORIGINS01_v0.2.tex

The preamble uses Latin Modern, T1 font encoding, geometry, needspace, AMS packages, booktabs, tabularx, array, graphicx, xcolor, fancyhdr and hyperref. These must already be available in the compatible installation/cache. Standalone font files and the local build cache are not distributed. Compiler/font differences may change page breaks or PDF bytes; the manifest identifies the published artifact.

Verify the pristine publication's bytes with an existing Python 3 installation:

    python -B tools/verify_publication.py

The standard-library verifier checks only declared file identities and checksums. It does not execute the scientific kernels, historical studies or mathematical suites. Keep reconstructed outputs separate from the published edition.

The two original figure sets, geometry_inventory.json and figures/render_figures.py are unchanged from v0.1. The original figure helper is supplied for provenance and optional static reconstruction in an isolated working copy with existing NumPy/Matplotlib. It overwrites figure outputs and uses a relative build/mpl-cache directory outside its figures folder; choose an isolated copy with a writable parent before invoking it. It was not rerun for v0.2. No scientific simulation is needed to read or rebuild this document.

The completed edition was inspected on every page. The checks performed for this editorial expansion compared all retained mathematical text/equations, validated the stated half-π substitution and existing normalization arithmetic, closed references and dependencies, and checked publication scope. No historical experiment, classifier or native trajectory was repeated.
