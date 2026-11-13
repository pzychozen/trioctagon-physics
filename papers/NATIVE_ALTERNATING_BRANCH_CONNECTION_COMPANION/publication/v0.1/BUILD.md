# Build the authorized research edition

Use a fresh copy of this edition for a rebuild so that the received publication artifact remains unchanged. This is a document build, not scientific recertification.

From Windows Command Prompt in the edition root:

```bat
conda activate torment
python -B build.py --tectonic "C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe" --build-dir "C:\TORMENT\TRIOCTAGON_new\research\AB_PUBLICATION_DOCUMENT_REBUILD"
python -B helpers\verify_document.py --build-dir "C:\TORMENT\TRIOCTAGON_new\research\AB_PUBLICATION_DOCUMENT_REBUILD"
```

The executable path identifies the existing cached Tectonic 0.17.0 used for this final Windows build. Another machine may supply its existing cached executable. Retain `--only-cached --untrusted`, the `torment` environment requirement and external build-directory protections. No package installation, network downloads, shell escape or persistent configuration change is needed or authorized by this build guide.

The source date and reproducible PDF metadata date remain 12 November 2026. The build receipt separately records the actual finalization/authorization date, 13 November 2026, actual execution timestamps, commands, source hashes and output identity. Temporary TeX files and fontconfig caches stay outside the edition; no font binaries or caches are included in the publication payload.

The accepted `tables/certificate.tex` and its generator remain byte-identical to the reviewed manuscript. The unchanged generator reads only retained JSON and performs exact-rational transcription checks. During finalization it was run in a separate documentary scratch copy, and the generated table matched the accepted raw bytes before the new verification record was adopted. If regenerating on another platform, compare raw bytes before replacing the table; CRLF must not silently become LF. No scientific engine is imported by this helper.

E01 corrects `helpers/verify_document.py` to hash `(ROOT/n).read_bytes()`, explicitly declaring its raw-byte basis. The helper also asserts the legitimately authorized research-edition metadata instead of the historical pending-review subject. All font, reference, link, text, layout and environment checks are retained. `verification/E01_FINAL_WINDOWS_VERIFICATION.json` confirms equality of the final helper hashes, build receipt and actual source bytes for all three TeX inputs.

The final Windows build produced 13 A4 pages, 18 embedded fonts, 75 resolved labels and six bibliography keys, with no relevant compiler warnings or unresolved references. All final pages were rendered with the existing Poppler tool:

```bat
pdftoppm -r 145 -png NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION_v0.1.pdf PAGE_OUTPUT_PREFIX
```

Every complete page was then visually inspected. The current inspection record binds the exact final PDF; images are in the external closeout. A PDF change requires a fresh build record, crosswalk and all-page inspection. Automatic text/font checks are not a substitute for that inspection.

Historical scientific scripts and replay instructions under `evidence/branch/` are preserved provenance. None was run for this publication. The original manuscript archive and its preparation records remain unchanged in the closeout; the new `PUBLICATION_MANIFEST.json` inventories this actual edition.
