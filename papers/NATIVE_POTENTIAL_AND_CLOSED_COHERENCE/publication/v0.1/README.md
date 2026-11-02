# Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map

**Author:** Hilmir Frímann Halldórsson  
**Edition:** Author-authorized repository research edition v0.1, 2 November 2026  
**Status:** Project-internal scientific review completed; author publication approval granted. No external peer review is claimed.

[Final PDF](NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf) · [Editable source](manuscript/main.tex) · [Claim/source ledger](CLAIM_SOURCE_LEDGER.md) · [Publication disposition](PUBLICATION_DISPOSITION.md) · [Finalization report](FINALIZATION_REPORT.md)

The 16-page paper combines strict local descent of the existing native potential with a separate explicit coherent-domain decrease bound. On that finite domain, three intensities and two signed pair areas give autonomous coherence coordinates retaining the potential, every matched edge energy, and the squared prestage increment. Minimum counts are confined to the stated raw-entry dictionaries. No runtime integration or physical-energy identification is made.

## Finalization and evidence

The reviewed mathematics is retained. R1 adds the existing hypothesis `g>0` to the abstract. R2 cites the accepted energy note, Section 8, for the separate 60-degree finite-return sector. Current edition/status wording and attribution reflect completed review and author approval on 2 November 2026. [FINALIZATION_REPORT.md](FINALIZATION_REPORT.md) identifies the exact source changes and final hashes.

The two accepted notes and their existing helper/result pairs are in separate `evidence/` directories. They are archival; **do not execute the scientific helpers as part of the document build**. Source snapshots, the original comma-before-copy, and the correction receipt in `provenance/` are unchanged. The comma was already corrected during preparation; no second edit was made.

`historical/review/` contains unchanged review-stage records: the preparation report, README, ledger, original payload manifest, and old build/inspection receipts. Their review-pending language and earlier filenames describe that historical stage, not the current edition. Their original local/relative references have not been rewritten. The original review ZIP is preserved externally and is not included in this edition. The current publication order is in `provenance/`; a separately downloaded manuscript review was not found, so its operative acceptance and exact edits are recorded by that order.

Fresh final records are under `verification/`: build identity, compiler log, document checks, source diff, and complete final visual inspection. [PAYLOAD_MANIFEST.json](PAYLOAD_MANIFEST.json) lists every edition file except itself, with byte lengths and SHA-256 values. The later actual push/commit and remote-byte verification receipt is maintained externally, avoiding a recursive commit identity.

## Rebuild with installed tools

The complete source consists of ten `.tex` files and uses its own `thebibliography`. No external figures, project modules, or scientific helper execution is required. Use an existing Tectonic installation with its resources already cached. No installation or persistent environment change is part of the build.

Exact preparation-machine command, in Command Prompt:

```bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01\final_edition
python -I -B build_edition.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe --work-dir C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01\build_work
```

For a relocated copy, change the `cd` path and executable path and choose a build directory outside the edition. The wrapper invokes `--only-cached --untrusted --keep-logs --keep-intermediates`, keeps temporary TeX/font files in that external directory, writes the canonical PDF at this edition root, and creates fresh build records. Its Fontconfig settings apply only to the compiler process. The PDF stays alongside `evidence/` so both relative proof-note links resolve. Rebuild a separate working copy if preserving the immutable edition's recorded hashes.

The existing tools used were Tectonic 0.17.0, Poppler 26.07.0, Python 3.11.15 in `torment`, and the existing bundled pypdf 6.10.0. `inspect_edition.py` performs document and byte-provenance checks against an extracted original review package, using `--review-baseline PATH`; it does not execute evidence. Visual page inspection is separate. Rendered PNGs, font caches, intermediate TeX files, and duplicate build PDFs are not part of the publication payload.

To verify the frozen payload without building anything or accessing the original machine:

```bat
python -I -B verify_payload.py
```

This uses only the Python standard library and checks every listed file's bytes against the manifest.

## Scope and rights

This is mathematical repository research with project-internal review, not external peer review or experimental physical validation. The existing repository licensing scope remains unchanged; repository visibility grants no new licence for the scientific material. This publication adds no runtime changes, release/tag, DOI deposit, announcement, or successor investigation.
