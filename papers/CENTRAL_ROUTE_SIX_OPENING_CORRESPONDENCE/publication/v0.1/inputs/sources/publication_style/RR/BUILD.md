# Build and document verification

The delivered PDF is the frozen manuscript-review candidate. Rebuilding creates an artifact whose identity and pages must be checked again; it does not silently replace reviewed bytes.

The document-only manuscript/build.py adapts the supplied P4 helper in this new directory. It uses an existing Tectonic executable with --only-cached and --untrusted, no shell escape, and an external build/log directory. No package or font installation is required.

From this edition directory in Command Prompt:

    call conda activate torment
    python -I -B manuscript\build.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --build-dir C:\TORMENT\TRIOCTAGON_new\research\NATIVE_CAPACITY_RECEIVING_RECOVERY_PAPER_01\rebuild

The actual final build used Tectonic 0.17.0 and conda torment Python 3.11.15. SOURCE_DATE_EPOCH is 5 November 2026 UTC, the manuscript preparation date; the receipt separately records the actual build instant. Fontconfig settings are generated only in the external build directory and refer to installed Windows fonts.

verification/BUILD_RECEIPT.json records the actual command, engine/interpreter versions, source/helper identities and final PDF hash. The final main.log, main.aux, compiler.txt and original receipt are in review_support/final_build in the review ZIP. There are no final warnings, undefined references/citations, missing-glyph messages, or underfull/overfull boxes.

The first successful build had 14 pages because a redundant concluding summary occupied an otherwise empty page. Removing that nonessential summary produced the final 13-page document. No accepted mathematical statement or proof step was removed. All final pages were rendered again and individually inspected after the rebuild.

Document extraction, metadata, navigation and font checks used bundled Python 3.12.14 with pypdf 6.10.0, invoked with conda torment activated. Poppler pdftoppm 26.07.0 rendered every final page at 125 dpi. All 16 distinct PDF font resources are embedded. All 73 source labels, six bibliography entries, four immutable edition links and 28 bookmark page targets resolve. External links are checked as embedded immutable URLs; no fresh remote request is claimed.

verification/VISUAL_REVIEW.json binds each inspected image and its finding to the exact final PDF. The full image files and render receipt remain in the review package, outside the compact edition. Full-page visual inspection is separate from text extraction and source fidelity.

No scientific code is executed by the build helper. The accepted fourteen-group evidence and its historical independent replay remain unchanged. These document checks do not constitute GPT/author acceptance of the manuscript.
