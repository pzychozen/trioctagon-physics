# Research edition build and verification

Run from **Windows Command Prompt**, using the existing environment. No package installation or persistent configuration change is needed. The editable bibliography uses `thebibliography` in `references.tex`; no separate BibTeX invocation is needed.

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
cd /d C:\path\to\extracted\review
python -B helpers\make_tables.py
python -B build.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --build-dir ..\companion-build
python -B helpers\verify_document.py --build-dir ..\companion-build
```

The Tectonic path above is the existing executable used for this Windows build. A relocated machine may supply its own **already available, cached** Tectonic executable via `--tectonic`. If it is on PATH the option may be omitted. No historical machine path inside the preserved evidence is a build dependency. Build source and evidence links are relative to the edition directory.

The helper retains `--only-cached --untrusted --keep-logs --keep-intermediates`; it does not fetch TeX packages or enable shell escape. Windows font configuration and temporary font caches are written only to the external build directory. `SOURCE_DATE_EPOCH` is fixed to 11 November 2026 UTC. The canonical PDF is written into the edition; intermediate `.aux`, `.log`, font caches and temporary files stay in the specified external directory. Do not distribute those cache/font files.

`make_tables.py` compares saved terminal values as exact fractions and transcribes them to LaTeX. It never executes the scientific checker. `verify_document.py` reads the finished PDF and TeX records, verifies references, metadata, embedded fonts, relative evidence links, input hashes and transcription, then uses the available Poppler `pdftoppm` to render all pages at 145 dpi. It must run without Python's `-O` flag. Render checks complement manual inspection; they do not replace it.

For a new build, use a fresh extracted copy or move the prior `verification/pages/` directory outside the edition before rendering a document with fewer pages. After any source change, rerender and inspect **every page of the actual final PDF**, then renew hashes and inspection records. The supplied final inspection applies only to the exact finalized PDF hash. Rebuilding a copy changes its verification records, so its publication manifest will no longer describe that working copy.

The finalized research edition is author-authorized for repository publication. The actual final execution used Tectonic 0.17.0, Windows Python 3.11.15 in `torment`, and the build command preserved in `verification/BUILD_RECEIPT.json`. The actual final PDF has seven A4 pages, 39 resolved labels, four cited bibliography entries and 17 embedded fonts. The delivery includes compiler messages and the final TeX log as text records, rather than temporary compiler outputs.

Historical scientific code in the evidence tree is preserved for provenance. It is not part of this document build and was not rerun for the note.
