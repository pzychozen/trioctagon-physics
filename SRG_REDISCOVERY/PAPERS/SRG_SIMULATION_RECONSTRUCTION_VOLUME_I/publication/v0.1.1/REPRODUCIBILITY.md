# Inspecting and building this edition

This guide applies to the proposed publication payload. Appendix B in the manuscript retains the accepted review edition's preparation history, including its old workspace path. The commands here use an independent copy of this publication directory.

## Inspect without running a simulation

From this edition's root in Windows Command Prompt:

```bat
conda activate torment
python -B tools\verify_publication.py
```

The checker uses Python's standard library. It reads manifests, ZIP members, source text, image hashes and links; it does not import historical programs, advance state, recompute scientific findings, acquire dependencies or write files. Its final manifest check requires the complete publication directory. The [recorded verification](PUBLICATION_VERIFICATION.md) describes the checks actually completed for this preparation.

The [evidence index](EXTERNAL_EVIDENCE_INDEX.md) provides local access to every indexed supporting item. Complete study payloads and their original manifests are preserved under `evidence/SRG_REDISCOVERY/`. Their original inspection and replay scripts are evidence of the accepted methods, not an instruction to execute them. Existing CSV/NPZ/JSONL files can be inspected directly. Repeated frame labels and row order must be preserved.

The [accepted R1 archive](provenance/accepted_editorial_v0.1.1.zip) and [editorial closure](provenance/editorial_closure/CLOSURE_MANIFEST.json) allow offline comparison with the reviewed edition. Archived review documents retain local-workspace references as historical context. They are not current GitHub evidence links; current links are in this edition's evidence index.

## Optional manuscript-only rebuild

Keep the distributed edition intact. Copy `MANUSCRIPT`, `tools` and `records` to a short independent path, for example `C:\SRG_V1_BUILD`. A short path avoids Windows path-length problems in downloaded TeX cache filenames. Use Windows x86-64, Python 3.11 and Command Prompt with the requested conda environment:

```bat
conda activate torment
cd /d C:\SRG_V1_BUILD
python -B tools\acquire_typesetter.py
python -B tools\build_pdf.py
```

If conda is not on PATH on the author's workstation, activation can instead use:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
```

The acquisition script obtains Tectonic 0.17.0 from its official release. It writes `build/toolchain/tectonic.exe` and a provenance receipt. The builder expects that path. Skip acquisition if an existing compiler matches the executable SHA-256 below. The first acquisition needs network access; the first build may fetch missing TeX dependencies. Compiler binaries and caches are deliberately excluded from the publication payload.

- Compiler executable: `99ffcfdbf1ebf8bdda9e791942e3d06aedb12463fddc33f07de6f5211c8bf08d`.
- Official Windows archive: `f61ce51f0b0ade1015b7de7ef368541c5424e9756ecbd0d7af97d6d48030845f`.
- [Recorded release provenance](records/typesetter_provenance.json).

The builder writes the new PDF and TeX intermediates under `MANUSCRIPT`, a build receipt under `records`, and local caches under `build`. It executes only the typesetter. All eight section files, references, 17 figure includes and 35 PNG assets are required. A compatible XeLaTeX installation is a separate alternative route; cross-environment PDF byte identity is not promised.

This preparation reused a verified compiler and a separate copy of the accepted cache in a short, isolated build directory. The published source inputs were compared byte for byte with the build inputs. The resulting PDF, receipt and typesetting logs are included. Fresh compiler download and a clean-network installation were not retested.

## PDF inspection method

The retained `tools/inspect_pdf.py` records the original workstation's Poppler/Python dependency paths. It is a reproducibility reference, not a portable prerequisite for the standard-library checker. For another installation, use its own Poppler `pdftoppm -r 110 -png MANUSCRIPT/volume_i.pdf page` and a PDF text extractor. Inspect the cover and all running headers, confirm 53 pages and 17 numbered figures, and compare body text and pixels against the accepted PDF after excluding only the running-header region. The supplied visual-review receipt states the actual comparison and inspection coverage.
