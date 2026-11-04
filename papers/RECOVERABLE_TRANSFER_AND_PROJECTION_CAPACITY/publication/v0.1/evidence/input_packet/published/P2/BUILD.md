# Document-only build

Build from this edition directory. On the author's Windows system, use Command Prompt:

    call conda activate torment
    python -I -B manuscript\build.py --tectonic C:\path\to\tectonic.exe --build-dir C:\outside-edition\new-build-directory

On another system, use an existing Python 3.9+ interpreter and Tectonic:

    python -I -B manuscript/build.py --tectonic /path/to/tectonic --build-dir /outside/edition/new-build-directory

Omitting --build-dir creates a new system-temporary directory. The helper rejects a build directory inside the edition. It requires only Python's standard library, builds all local TeX sources and bibliography, writes intermediates and logs externally, then copies the resulting PDF into this edition. Use a new external build directory for each attempt. The helper records final source, helper and PDF hashes after a successful build.

The exact production tools were Python 3.11.15 in conda environment torment; Tectonic 0.17.0; cached LaTeX2e 2021-11-15 patch level 1; article class 2021/10/04 v1.4n; Latin Modern package/font definitions 2015/05/01 v1.6.1; AMS fonts/symbols package 2013/01/14 v3.01. All 18 fonts referenced by the PDF are embedded. Their names and embedded-stream hashes are recorded in verification/DOCUMENT_CHECKS.json. No fonts are redistributed as separate build files.

Tectonic runs with --only-cached and --untrusted. There is no shell escape, scientific import, scientific replay, model simulation, Git operation or package installation. A pre-existing TeX resource cache with the listed packages and fonts is required. Missing resources cause a build failure; the helper does not fetch them. Cached Tectonic is sufficient on the production host. A different cache/compiler may alter PDF bytes or pagination, so a new build requires its own checks rather than reuse of this edition's verification records.

SOURCE_DATE_EPOCH is set to 3 November 2026 UTC. Windows font configuration and temporary paths are scoped to the child process and external build directory; the helper changes no persistent configuration.

The editorial closeout used the unchanged build helper in a separate research copy. Its fresh closeout_01 build succeeded on the first attempt with zero warnings. Only the supplied MC-01 abstract sentence changed; no typesetting adjustment was necessary. The historical build_01/build_02 records of the original submission remain in its unchanged review archive and do not verify this revised PDF.

Document inspection used bundled Python 3.12.14 with pypdf 6.10.0. Rendering used Poppler pdftoppm 26.07.0 at 125 dpi. Every one of the ten final pages was visually inspected; the exact PDF and render hashes are recorded. The build itself does not depend on these inspection tools.

The delivery support directory retains the fresh final compiler log, auxiliary labels and raw receipt, environment versions, input/preservation records, document-only inspection scripts and all final page renders. None are imports for the scientific argument.
