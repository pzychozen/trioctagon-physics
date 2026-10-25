# R1 document-only build instructions

The paper uses manuscript.tex, universe_sections.tex, closing_sections.tex, references.bib and the unchanged PNGs under evidence/. Keep those relative paths.

On this workstation, use Windows Command Prompt in the unpacked revision directory:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONIOENCODING=utf-8
python -B methods\build_pdf.py
python -B methods\render_pdf.py
```

The unchanged document wrapper uses Tectonic 0.17.0. For this R1, its executable/cache were copied from v0.1 into the new build directory. The compiler SHA-256 is 99ffcfdbf1ebf8bdda9e791942e3d06aedb12463fddc33f07de6f5211c8bf08d. Its fallback origin recorded by the wrapper remains the older Volume I document toolchain; R1 intake records the intervening copy. Temporary files and caches stay under build/.

On another machine with Tectonic available:

```bat
mkdir build
tectonic --untrusted --keep-logs --keep-intermediates --outdir build manuscript.tex
```

No scientific input needs to be executed. The editable source and image assets are self-contained. The Windows render helper uses the existing bundled Poppler and pure-Python pypdf under torment; its paths can be adapted to another document runtime. Compiler/fonts/timestamps may change PDF bytes; byte-identical rebuilding is not claimed.

methods/r1_prepare.py is a one-time intake/edit record; do not rerun it against this finished revision. methods/r1_finalize.py performs byte/document checks and packaging only; it refuses to overwrite an existing review ZIP. Neither imports research code. Archived scientific methods remain evidence only.

Rebuilding invalidates the current PDF/page identities and requires new document QA. The final delivered ZIP omits compiler binaries/caches and temporary renders. Final compiler log and bibliography output are retained under qa/.

