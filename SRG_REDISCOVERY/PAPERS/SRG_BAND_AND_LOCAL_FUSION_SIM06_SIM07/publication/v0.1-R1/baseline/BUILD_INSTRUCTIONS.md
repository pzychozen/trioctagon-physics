# Document-only build instructions

The editable paper consists of [manuscript.tex](manuscript.tex), [universe_sections.tex](universe_sections.tex), [closing_sections.tex](closing_sections.tex), [references.bib](references.bib) and 11 unchanged PNGs under evidence/*/source_package/figures. Keep this relative layout.

## Rebuild on the current workstation

Open Windows **Command Prompt**, change to this candidate directory, and activate the existing environment:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONIOENCODING=utf-8
python -B methods\build_pdf.py
python -B methods\render_pdf.py
```

The compiler wrapper uses Tectonic 0.17.0, copied unchanged into build/toolchain from the existing Volume I R1 document toolchain if not already present. Its SHA-256 is 99ffcfdbf1ebf8bdda9e791942e3d06aedb12463fddc33f07de6f5211c8bf08d. It confines temporary document/cache/font files to build/. Missing document dependencies may be downloaded by Tectonic. No research engine is imported.

The PDF renderer uses the workstation’s bundled Poppler pdftoppm and pure-Python pypdf, imported under torment. Exact executable/module roots appear in the small wrapper. The --extract-only option extracts PDF text without rerendering. Old extra page images can remain locally after a shorter build; only pages 1 through the current PDF count are reviewed.

## Portable source route

On another machine with Tectonic installed, open CMD at the unpacked package root and run:

```bat
mkdir build
tectonic --untrusted --keep-logs --keep-intermediates --outdir build manuscript.tex
```

The generated build/manuscript.pdf is a document rebuild. The bibliography and figures are self-contained; no external research directory or scientific array is needed. Tectonic handles bibliography passes. Compiler/fonts can affect pagination and PDF bytes; byte-identical rebuild is not claimed. The delivered PDF’s exact identity is recorded separately.

The current workstation wrapper’s fallback compiler path is a convenience, not an evidence dependency. Compiler binaries, caches and temporary page renders are intentionally excluded from the review ZIP. Final compiler logs and bibliography output are in qa/.

## Methods boundary

- build_pdf.py and render_pdf.py are document operations.
- review_integrity.py checks hashes, archive membership and document references only.
- package_review.py packages an already reviewed candidate and verifies archive-member bytes.
- Intake/read/layout scripts preserve the preparation record. Do not rerun one-time intake or layout scripts against the finished source.
- Scientific methods in the accepted nested archives are historical evidence. **Do not execute them for a document rebuild.**

A rebuilt PDF requires renewed page QA and identities before being substituted for this candidate. No simulation or scientific verification is part of these instructions.

