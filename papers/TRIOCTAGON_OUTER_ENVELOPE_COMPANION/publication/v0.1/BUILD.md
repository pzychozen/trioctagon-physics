# Publication document-only Windows build

Use a short external extraction directory and Windows Command Prompt. Python work uses the existing `torment` Conda environment. Do not execute the preserved scientific scripts during manuscript reproduction. No dependency install or update is needed in the authoring host.

The delivered source was built with existing Tectonic 0.17.0 using its existing cache, `--only-cached --untrusted`, and external intermediates. Actual commands, timestamps, source hashes and executable version are in `verification/final_build/BUILD_RECEIPT.json`. Compiler stdout, stderr and the actual TeX log are adjacent. Python, OS and document-package versions are in `verification/ENVIRONMENT.json`.

From an extracted, fresh working copy of this manuscript:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
cd /d C:\TORMENT\OE_REBUILD\manuscript
python -B helpers\make_tables.py
python -B build.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --build-dir C:\TORMENT\OE_REBUILD\build
python -B helpers\verify_document.py --build-dir C:\TORMENT\OE_REBUILD\build --render
```

Adapt only the local extraction/build/tool paths. `--build-dir` must be outside the manuscript source root. Tectonic must already have the required packages/fonts in its cache. If it does not, stop instead of enabling downloads or installing packages under this commission.

The table helper reads saved JSON and expressions only. Its SymPy use parses expressions, compares their coefficients with saved arrays and emits LaTeX; it does not import the original scientific modules or perform hull/root/sign calculations. `build.py` sets a fixed document date, keeps temporary/cache configuration external, and records the actual raw source/PDF identities. `verify_document.py` inspects the PDF, fonts, labels and preserved inputs, then optionally renders the pages with Poppler at 145 dpi.

These checks do not replace visual inspection. Inspect every newly rendered page after any source change and make a fresh inspection record bound to its new PDF hash. The supplied `VISUAL_INSPECTION.json` applies only to this delivered PDF. Do not carry its PASS result forward to a modified build. Byte-identical PDFs are not promised across platforms, compiler versions or font/cache versions.

New hand-authored LaTeX/Python/Markdown sources use UTF-8. Windows-generated tables and JSON retain the native writer's CRLF convention; raw line-ending counts are recorded in `verification/NEW_TEXT_INVENTORY.json`. No text normalization occurs after the final build. All inherited files, including their CRLF/LF choices, remain unchanged and are hashed as bytes.

`verification/submission/build_history/` contains actual earlier compiler logs and receipts, including cached italic-font failures resolved through upright theorem styling, followed by layout and bookmark fixes. Only the final build is the delivered manuscript. Cache files, font binaries, executables and transient TeX intermediates are not in this package.

The publication record is in `verification/final_build/`. The two permitted build-helper status/date replacements and exact new metadata assertion are documented under `provenance/publication/`. The fixed `SOURCE_DATE_EPOCH` retains the manuscript preparation date; actual start/finish and client dates are recorded independently. Publication used the unchanged table helper in a separate scratch copy and compared all seven resulting table files byte-for-byte; the approved edition table files were not rewritten.

The unchanged `helpers/package_review.py` is historical and must not be used to produce a current publication disposition. The new `helpers/package_publication.py` checks current records and produces the publication payload manifest (and optionally a documentary payload ZIP). External commit/push/CI receipts are produced after publication and remain outside the committed payload.
