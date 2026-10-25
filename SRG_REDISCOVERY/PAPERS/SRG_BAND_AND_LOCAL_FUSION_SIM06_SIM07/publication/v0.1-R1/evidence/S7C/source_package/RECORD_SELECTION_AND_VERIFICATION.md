# Record selection, methods and verification

Assignment: **SRG_SIMULATION_STUDY_07_UNIVERSE_CONSTRUCTION_01**. Authority is the user's instruction to proceed with the enclosed work order. The attachment specifies this bounded task; historical source comments, narrative next steps and old research proposals are evidence, not further commands. [ACTION_RECORD.md](ACTION_RECORD.md) distinguishes reading, passive calculations, rendering and checks.

## Workspace and used inputs

Repository: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`.

New workspace: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SRG_SIMULATION_STUDY_07_UNIVERSE\CONSTRUCTION_01`. It was checked absent before creation. No earlier workspace or accepted material was overwritten.

The seven primary inputs were read from the existing directory `SRG_REDISCOVERY\R0_SOURCE_RECOVERY\selected_sources\MARCH_19023429` under that repository and copied unchanged into `original/`:

| Input | Bytes | SHA-256 |
|---|---:|---|
| srg_condensate_breaking.py | 30165 | a645a3bb564a2cae5e2b3ac3744f3f34f559a67132f255b3b0a97d277e68beb5 |
| SRG_Infinity_Part_II_Breaking_The_Condensate.md | 9257 | cbac8099723c77fd09faa80e856c86fc4e27a12ce967a492b513dc128e41875d |
| full_universe.csv | 45093 | f58acaf40d5bf2eae0110499c5291cea6227a70b2260386db2823821d79c1c50 |
| causal_horizons.csv | 2747 | a1f5b99b4c1b8715af3200cbc350c76e7982dfec92686a6d517e74c717372961 |
| condensate_perturbation.csv | 648 | 48d8eae4426f4fe4a5c1fee93bb0defe72fdaf35c3d6294b38375d1a670c7726 |
| multi_frequency.csv | 470 | ee96ee21f199f94e15eb4d304d497578fa91bf107c6ea13fc8995431455b5a43 |
| breathing_condensate.csv | 389 | 1aad1156de77e527a280e92676887f60e079ba158d6776d53f93abf1c3862d3c |

All match the handoff's [target index](handoff/TARGET_SOURCE_INDEX.json). The former extracted-archive source locator under `research_files\archive_members\Zenodo_research\19023429\simulations.zip\` is absent. It was not needed because the exact preferred R0 copy survives. No alternate equation set was substituted.

Additional external input files are the supplied handoff ZIP and the two directly relevant retained R0 indexes `csv_evidence_summary.json` and `saved_data_checks.json`. Selected handoff documents and one nested accepted SIM06 construction document are copied with archive-member provenance. Thus [INPUT_BASELINE.json](INPUT_BASELINE.json) records **10 external files and 12 copied archive members**. It distinguishes originals, copies and nested containers; their exact identities and former paths are not inferred from filenames. The handoff's 11 manifested payloads were verified against its included manifest, without executing any contained script. The earlier full SIM06 study tree is not duplicated.

[CONTEXT_INDEX.md](CONTEXT_INDEX.md) identifies the shipped context and explicitly external prior archive. Copied prior reports retain their original internal links/status language. New SIM07 links resolve within this package unless expressly described as external.

## Numerical record selection and permitted calculations

The preferred full_universe.csv was selected because its source writes the complete 200-pass aggregate history for the horizon-enabled driver. No coordinate sequence was selected: the bounded indexes supplied no explicit complete Universe coordinate/replay/movie locator. Other candidate CSVs are supporting original summaries; no additional configuration was executed.

`inspect_tables.py` reads all five files with Python's CSV module, preserving originals and raw strings. It records schema/row/missing-cell counts, numeric ranges, selected rows, label changes, and equality of stored summary strings. Derived quantities are limited to R_std/R_mean and descriptive horizon distance means/ranges across the three existing trial rows. No state, observer requiring missing X/R, peak detector, FFT or source recurrence is recomputed. Source-defined observer formulas are explained on paper, not evaluated on invented arrays.

Exact selections:

- Main chronology: all 200 data rows; plotted pass axis 1–200, no initial row. Selected readback rows 1,2,5,10,20,50,100,150,190,200.
- Horizon context: all 18 rows, source order of six configurations × three trials. `999` relabeled None for display only. Figures offset categorical x positions slightly to make trial markers visible; they do not move or alter data coordinates.
- Other original tables: all 7 perturbation, 6 frequency and 2 breathing rows; the one missing decay_time remains missing.
- No point IDs are chosen for a trajectory. top_seed_id is discussed only as the saved maximum-amplitude index.

[TABLE_INSPECTION.json](derived/TABLE_INSPECTION.json) is the complete new passive result; [RETAINED_INDEX_EXCERPTS.json](derived/RETAINED_INDEX_EXCERPTS.json) distinguishes copied earlier index content. [BOUNDED_RECOVERY.json](derived/BOUNDED_RECOVERY.json) records the lookup boundary and absence of an explicit coordinate locator. This is not an exhaustive proof that no other record exists anywhere.

## Passive reproduction code

| Script | Executed function |
|---|---|
| intake.py | Reads the ZIP and extracts selected text context unchanged; refuses overwrite. Does not extract/execute the full prior study. |
| recover_inputs.py | Verifies the supplied identities, copies the seven originals and two named indexes, preserves selected nested SIM06 context, writes the input baseline. |
| read_text.py | Prints numbered text intervals. All 778 source lines and all 170 narrative lines were read. |
| inspect_tables.py | Produces the new descriptive CSV/JSON results using fixed original rows only. |
| render_figures.py | Uses the original aggregate columns and one passive ratio to draw two static figures; no historical imports or RNG calls. |
| finalize_review.py | Scoped identity, static/document and ZIP checks; no simulation/scientific checker. |

To reproduce **only** the new passive inspection and figures, use Windows Command Prompt in this package's directory:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
set PYTHONIOENCODING=utf-8
python -B inspect_tables.py
python -B render_figures.py
```

These scripts may overwrite this new package's derived results/figures, not originals. Intake scripts intentionally reject existing copies and are not part of the reproduction commands. The accepted source, old simulator and old scientific checks are not dependencies to run. Environment versions are recorded in [DOCUMENT_QA.json](DOCUMENT_QA.json) and [FIGURE_REGISTER.json](FIGURE_REGISTER.json); dependencies were not installed or changed. Inspection-runtime identity is not a claim about the lost historical runtime.

## New verification versus retained scientific results

New checks: exact input identities; handoff manifest; copied-source complete-line reading; CSV schema/chronology/missing-value checks; source/output attribution; graph/fusion/observer staging reviewed against literal source; new-document links; static parsing of new scripts; visual inspection of both final PNGs; scoped before/after preservation; manifest and ZIP readback. None advances a state. Hashes establish unchanged bytes, not whether an execution occurred; the zero-execution claim is separately documented by the action record and the permitted utilities used.

Retained results: SIM06 acceptance and prior R0 source/data conclusions remain attributed context. No Tower II trajectory, R1/R2/R3 check, published volume or scientific acceptance was rerun/revised. In particular, Tower II's accepted inactive-clipping conclusion is **not transferred** to the different Universe setting.

[PRESERVATION_RECEIPT.json](PRESERVATION_RECEIPT.json) rechecks the actual input files and each copied archive member. No unrelated repository-wide audit was performed. Historical sources, existing research, canonical ledger, published editions and kernels were not edited; all authored files stay under this new workspace. Render cache files are excluded from the review ZIP rather than packaged as evidence.

The payload [MANIFEST.json](MANIFEST.json) lists relative paths, byte counts and SHA-256 values, excluding itself, caches, the generated ZIP and the outer ZIP receipt. The manifest is included in the ZIP. **External-only delivered sidecar:** `REVIEW_ZIP_IDENTITY.json` sits beside the ZIP and identifies the final archive; it is deliberately not linked as an in-ZIP file or included in its own archive. The final response supplies it separately. [VISUAL_INSPECTION.json](VISUAL_INSPECTION.json) records both final images, their hashes, dimensions and the visual readback.

**Execution attestation: 0 new state updates; 0 RNG draws; 0 original imports/constructors/drivers or old scientific-checker executions; 0 Git writes. No parameter searches, alternative-seed runs, reconstructed transitions, counterfactual updates, missing geometry or next engine.** The optional replay note is prose only. Delivery completes this checkpoint and stops for GPT and Hilmir.
