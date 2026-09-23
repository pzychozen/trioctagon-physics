# Bounded reproduction of the scope revisions

The builds typeset B v0.1.2 and C publication v1.0.1 only. They do not rerun algebra, geometry, old simulations, kernel tests or figure generation. D's accepted PDF is verified by hash and is never rebuilt by this workflow. The existing manuscript execution counts retain their historical attribution.

## Existing external prerequisites

The actual check used Windows, Python 3.12.14 with `pypdf`, Pandoc 3.11 and Tectonic 0.17.0. No dependency was installed or upgraded. Existing TeX resource caches and system fonts are external build prerequisites, not source archives. Tectonic is invoked with `--only-cached`. Nothing from these environments belongs to the allowlist.

Actual tool locations (substitute equivalent existing tools for another checkout):

- Python: `C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`
- Pandoc: `C:/TORMENT/TRIOCTAGON_new/reconstruction/publication/paper_C/build/tools/pandoc/pandoc-3.11/pandoc.exe`
- Tectonic: `C:/TORMENT/TRIOCTAGON_new/reconstruction/publication/paper_C/build/tools/tectonic/tectonic.exe`
- B TeX cache: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/.build/tectonic-cache`
- C TeX cache: `C:/TORMENT/TRIOCTAGON_new/reconstruction/publication/paper_C/build/tectonic-cache`
- System fonts: `C:/Windows/Fonts`; publication typefaces also resolve from cached TeX resources.

Set `PAPER_B_PANDOC`, `PAPER_B_TECTONIC`, `PAPER_B_TEX_CACHE` and the corresponding three `PAPER_C_` variables to these explicit prerequisites. Builders use no historical-source or kernel import path. `SOURCE_DATE_EPOCH=1790121600` is selected by the builders. The actual tool hashes are in each edition's `build_record.json` and the isolated receipt.

## Commands

From the repository root, with the existing Python executable selected:

```powershell
python -B -X utf8 papers/PAPER_B/publication/v0.1.2/build_publication.py
python -B -X utf8 papers/PAPER_C/publication/v1.0.1/build_publication.py
python -B -X utf8 papers/publication_updates/20260923_BC_scope/verify_revisions.py
```

These commands rebuild the specified new editions and their attributed build evidence. `verify_revisions.py` writes only this packet's bounded result. For read-only final delivery hashes, use `verify_package.py` instead. Do not invoke the older general `build.ps1`, geometry checkers, or figure generators for this bounded revision.

For the minimal isolated replay, from the repository root with the six prerequisite variables above set:

```powershell
python -B -X utf8 papers/publication_updates/20260923_BC_scope/reproduce_isolated.py
```

The replay reads exactly eight committed baseline inputs with `git show 08c2a79739d540ffe1cab4743284052e2aa7214b:<path>`: the two preceding publication manuscripts, five existing B PDF figures, and C's companion bibliography. Their explicit identities are in `evidence/isolated_reproduction.json`. It copies the exact combined proposed list into a fresh ignored `.build/isolated_*` directory and runs both builders and the bounded verifier there. It does not copy the whole checkout, environments or research archives. Source/search environment overrides are removed. The only paths outside that copy used by the builds are the declared third-party tools, resource caches, runtime and system fonts.

The isolated PDFs and generated TeX must match the delivered bytes. The D reference target must exist inside the isolated copy and match its approved hash. Logs under `evidence/isolated_*` are new captured Codex re-execution output, distinct from all preserved predecessor evidence. The final metadata/receipt synchronization is checked separately and does not rebuild the papers. This is a replay with existing tools and cached resources, not a fresh-install or different-platform reproducibility claim.

Visual QA used existing Poppler `pdftoppm` at 110 dpi and PIL contact sheets. All final B/C pages were inspected; reference blocks and C-S2 were also inspected as full pages. Render previews stay in ignored scratch space.
