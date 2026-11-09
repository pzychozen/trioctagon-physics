# Document build and inspection

The preceding receiving/recovery edition's LaTeX layout and build helper were used as read-only precedents. Only copied document sources were adapted. No scientific suite, simulation or repository module was run.

The corrected publication01 build used Tectonic 0.17.0 with Python 3.11.15 in the `torment` environment. See `verification/build_receipt.json` for the exact command, executable paths, SOURCE_DATE_EPOCH, actual UTC completion time, every TeX/helper hash and PDF identity. The helper uses `--only-cached --untrusted --keep-logs --keep-intermediates`; shell escape is not enabled. Build/log/temp/font-cache directories are outside this edition.

From this edition directory, in Command Prompt:

```bat
call conda activate torment
python -I -B manuscript\build.py --tectonic C:\path\to\tectonic.exe --build-dir C:\path\to\fresh-external-build
```

Supply an existing compatible Tectonic/cache; no font or TeX distribution is included. Preparation date is fixed to 9 November 2026. A fresh build must receive its own refreshed hashes and inspection record rather than inheriting this receipt.

The successful final log has no undefined reference/citation, missing glyph, overfull/underfull box or other warning. Earlier failed editorial attempts and their concrete font/subscript resolutions are documented in `verification/BUILD_HISTORY.json`; they are not final-build receipts.

The exact final PDF was rendered with Poppler at 125 dpi, and every one of its 15 pages was inspected individually. `verification/VISUAL_INSPECTION.json` binds each observation and PNG hash to the final PDF. Actual PNGs are in `renders/final/` at the external publication closeout root. Text, font embedding, bookmarks, internal destinations, six citations and four retained commit-pinned link targets were checked with pypdf 6.10.0. This task did not freshly retrieve those historical remote links. The pypdf library was read from the bundled runtime while Python ran in `torment`.

## Publication editorial build

E01–E05 were applied as seven exact substitutions in five TeX files. The build helper and all 59 display bodies are unchanged. The corrected PDF was built at 2026-11-09T16:24:13.569660+00:00; 133392 bytes; SHA-256 `a8d29f230cc57f9a7aa113de770fc1c510110176e446650dafbec8ce0e0289a9`. All 15 corrected pages were inspected; all 18 optional numbered citations were checked directly against retained primary sources. The build history preserves earlier preparation attempts and appends this editorial build. Original pending-review wording in the PDF is historical; the dated publication status and exact review/GO resolve that stage.
