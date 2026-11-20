# Build and verification

The source is ordinary UTF-8 LaTeX with TeX Gyre Pagella and Unicode mathematics. Open Command Prompt with conda available and run:

    conda activate torment
    python -B build_pdf.py
    python -B manuscript_checks.py
    python -B make_crosswalk.py
    python -B verify_document.py

Alternatively run_python.cmd activates torment before the named Python script. The Windows build uses Tectonic on PATH, cached resources, a fixed SOURCE_DATE_EPOCH and recorded source hashes. On a new machine, obtain the TeX bundle with an ordinary Tectonic build before using its cached mode. Poppler supplies page renders; pypdf verifies embedded font streams. No scientific suite is run by these document commands.

Generated files are kept beneath build, output and inspection. The publication commit retains the final build transcript, document records and every inspected page; machine font caches and the duplicate intermediate PDF are excluded. Rerender and visually inspect changed pages after changing the manuscript. Verification scripts do not declare visual approval themselves.

The original GM01–GM03 scientific scripts remain unchanged in evidence. They write result files alongside themselves, so any future scientific replay should use a disposable copy. Such a replay was not needed or executed for this publication.
