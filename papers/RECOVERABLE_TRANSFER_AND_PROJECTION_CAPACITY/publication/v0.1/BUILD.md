# Document-only release build

From this edition directory, use Command Prompt with the installed conda environment:

    call conda activate torment
    python -I -B manuscript\build.py --tectonic C:\path\to\tectonic.exe --build-dir C:\outside-edition\new-build

Portable equivalent with existing Python 3.9+ and Tectonic:

    python -I -B manuscript/build.py --tectonic /path/to/tectonic --build-dir /outside/edition/new-build

The unchanged helper requires only Python's standard library. It runs Tectonic with --only-cached --untrusted --keep-logs --keep-intermediates; it rejects build intermediates inside the edition, and defaults to a new system-temporary directory when --build-dir is omitted. All required TeX resources must already be cached. It fixes SOURCE_DATE_EPOCH to 4 November 2026 UTC, scopes Windows font/temp configuration to the child process, writes a source/helper/PDF receipt externally, and copies the built PDF into this edition. Missing cached resources fail rather than trigger installation. The helper performs no scientific imports or scientific workflow execution.

Actual release build: release_01, Python 3.11.15 in conda torment and Tectonic 0.17.0. The build succeeded with zero warnings, undefined references, overfull/underfull boxes or missing-glyph diagnostics. Cached LaTeX2e 2021-11-15 patch level 1, article 2021/10/04 v1.4n, Latin Modern 2015/05/01 v1.6.1, AMS fonts/symbols 2013/01/14 v3.01 were used, as recorded in the compiler log. No package installation or cache download occurred.

Document checks used the existing bundled Python 3.12.14 with pypdf 6.10.0, after activating torment. Rendering used Poppler 26.07.0 at 125 dpi. All 15 final pages were inspected individually. The PDF contains 18 embedded fonts, 68 resolved internal links and 24 valid bookmarks. Font names and program hashes, metadata, source identities and final PDF identity are in verification/DOCUMENT_CHECKS.json, ENVIRONMENT.json and BUILD_RECEIPT.json. Label/page locators and the 51-group/64-label crosswalk were regenerated from the fresh auxiliary file and match the accepted layout.

Only the two supplied approved source replacements were applied; no subsequent source edit or typesetting change was needed. The final PDF has 137,455 bytes and SHA-256 93de8c191549fd0ad70f4cf5df970abfbe0ae37d0f0a8b688cbb128577438f79. Prior reviewed-source and PDF identities are retained separately in SOURCE_IDENTITIES.json. Historical build/visual receipts in the original review archive certify their original artifact only.

The closeout support includes the final compiler log, auxiliary labels, raw build receipt, all 15 page renders, extracted text and document-check scripts. Caches and temporary directories are excluded. Rebuilding with different cached tools can change bytes or pagination and requires a fresh check. The source date stays fixed; actual execution timestamps in receipts record this release run.
