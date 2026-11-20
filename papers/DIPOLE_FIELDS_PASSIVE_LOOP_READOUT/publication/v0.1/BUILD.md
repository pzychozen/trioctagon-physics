# Build and verify

In Windows Command Prompt with Conda and Tectonic/Poppler on PATH:

    conda activate torment
    python -B build_document.py
    python -B verify_edition.py

run_python.cmd activates torment before the named script. Python requires pypdf. The builder uses cached TeX resources, fixes SOURCE_DATE_EPOCH, checks references and font embedding, and renders every page. On a new installation, build_document.py --fetch-deps explicitly permits missing TeX bundle downloads.

The editable entry point is manuscript/main.tex. Both diagrams are editable TikZ. The final PDF is output/pdf/GM04_GM06_COMBINED_PAPER_v0.1.pdf. Build commands and all manuscript hashes are in BUILD_RECORD.json.

The portable document verifier checks source identities, preserved mathematical display/table hashes, saved numerical transcription, reviewed wording, label/citation coverage, current metadata and public evidence paths. It does not execute the preserved scientific suites.

Every final page must also be opened and visually inspected. VISUAL_INSPECTION.json binds the completed publication inspection to the exact final PDF and image hashes. Building or verifying alone does not grant a new visual approval. If the PDF changes, regenerate its locators and inspection record.
