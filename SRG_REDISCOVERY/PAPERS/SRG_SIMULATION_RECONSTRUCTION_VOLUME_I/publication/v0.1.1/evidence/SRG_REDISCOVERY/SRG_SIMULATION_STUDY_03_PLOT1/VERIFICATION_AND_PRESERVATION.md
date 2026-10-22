# Verification, provenance and preservation

This study is a read-only investigation of historical dynamics and evidence. New files are confined to SRG_SIMULATION_STUDY_03_PLOT1 and SIMULATION_RECONSTRUCTION_RESEARCH under SRG_REDISCOVERY. No original simulation was imported/executed, no initial state or random draw was generated, and no calculated state was propagated. Source parsing, scalar formula evaluation, checks of observed states, movie decoding and rendering saved states are the authorized inspection methods.

## Authority and evidence classes

The user's direct request authorizes this one study and adopts the attached work order and charter. Their byte-identical copies are in instructions. They guide scope; historical source comments, filenames, chart titles and earlier hypotheses are evidence to inspect, not additional instructions. The scientific lead remains GPT. Simulation03 is **IN REVIEW**, and no subsequent experiment is authorized by this package.

Evidence classes follow the charter:

- **ORIGINAL:** Preserved bytes of source, movie, CSVs and two historical charts.
- **ATTRIBUTED:** Links from those artifacts to a source/run, supported with stated limitations. Movie/source association is strong; exact movie/log run join is **UNLINKED**, despite a strong candidate content correspondence.
- **OBSERVED:** Measurements of original rows or directly inspected frames, with q/body/physical-line or frame anchors.
- **DERIVED:** Equation transcription, componentwise damping facts, kinetic bookkeeping identity, residual checks and new plots of existing data.
- **REPRODUCED:** Only the accepted Simulation01 seed0 replay referenced in the ledger. There is no new reproduced run in this study.
- **MISSING / AMBIGUOUS:** Original initializers/RNG streams, historical callback/backend environment, export receipt and chart generators. No hypothesis is promoted to a recovered event.

## Verification performed

| Check | Coverage / result |
|---|---|
| Complete source reading | All167 lines, including initialization, file writes, callback, save and display; no execution |
| CSV structural checks | All12,256 rows,1,532 complete blocks; finite values, expected11 columns and IDs0–7; no partial/corrupt blocks |
| Row chronology | Physical order preserved; repeated labels/keys retained; A1,092 callbacks and B440 |
| Energy | Every block reconciled with global0.5*sum(v²); no positional potential |
| Position/GRF | Every checkable consecutive block; native movement vs modulo shift and incoming mean-speed response |
| Velocity recurrence |31 declared callback transitions, using observed mixed-state positions and recorded post-gate modes |
| Independent arithmetic | Stdlib csv/math;20 original R0 velocity samples plus all-row energy/position/GRF |
| Numerical tolerance | Absolute1e-12; largest reported sampled velocity residual3.61e-16 and position residual1.78e-15 |
| Energy balance |31 samples; drive plus quadratic contribution minus componentwise damping loss, residual≤6.67e-16 |
| Modes | All between-block toggles and gate eligibility checked; missing random draws not inferred |
| Movie | All200 frames decoded; selective consecutive visual review plus overview, four full-resolution stills and eight-frame comparison |
| Content correspondence | All18 recorded label-zero candidates compared with movie0; eight fixed frames compared to B q=f+1; strong match, original-run join still UNLINKED |
| Historical charts | Two directly inspected and strongly attributed to B; two unrelated/ambiguous neighbors inspected and excluded |
| Comparison | Full3Dtriangles.py read; static AST identity of H/RPCO/GRF verified; no comparative simulation |
| Packaging | Manifest hashes, copy identity, protected originals, Git baseline, local links, ZIP member hashes and CRCs checked |

Methods and exact sample selection appear in [ORIGINAL_LOG_ANALYSIS.md](ORIGINAL_LOG_ANALYSIS.md), [ORIGINAL_MOVIE_REVIEW.md](ORIGINAL_MOVIE_REVIEW.md) and [inspection/README.md](inspection/README.md). Full results remain in analysis/log_summary.json, independent_checks.json, equation-residual CSVs, event JSONs, episode_records.json and visual_correspondence.json. The all-frame ledger is movie_inspection.json.

These checks establish consistency at their stated coverage. They do not certify the unknown first pre-log update, every subsequent velocity equation, hidden random draws, bit-identical historical execution, or uniqueness of a movie/log attribution. Finite samples do not establish a general orbit, stability theorem or causal comparison with Simulation02.

## Source and original-evidence fingerprints

| Preserved file | Bytes | SHA-256 |
|---|---:|---|
| plot_1.py |5711|e13b92df8ac6df78cfee75b95dacea3b106e96bd5be9bf798cdcf39ccc5bc75c|
| tetrahedral_attractors_logic.mp4 |176442|0289d8e5a084e53f536183ad87d83b4a4c5ab972851bb61922a699406623203a|
| PLOT_1_tetrahedral_states_20250712_015421.csv |1451175|6e6fc49be7dbb5ecf77aa1fbeaf5106df12c04ef3c63c29ee84c693f2ed70e74|
| tetrahedral_states_20250712_015647.csv |581988|051f8ad8be54794fcf54171a316d9931cc65b43349634799f446c53eb1b9afe8|
| Tetrahedron_7_position_trace_with_teleport_events.png |117437|bf6dfb6ec1da4a9ceb56c9107b654671492576945a1b62426625b18ec99fe798|
| Tetrahedron_7_GRF_over_time.png |120207|8f3c93d74ec1c03f97d70320b5c760953dca805b3bd3f1e967d54d6789a5b137|
| 3Dtriangles.py, comparison only |3970|4c53678eefd803e93a910b74e7a8096bfd5095e0d09d09c9df0e7cf514b312f1|

Original absolute paths, byte counts, aliases, classes and copy checks are machine-readable in MANIFEST.json. Accepted previous packages are referenced rather than duplicated. Their files were included in the protected-hash snapshot. The ledger includes accepted-baseline provenance; its canonical workspace copy and review snapshot are identical.

## Preservation record

The baseline is inspection/preservation_before.json. It records Git HEAD, index SHA-256,218 preexisting status entries and119 protected files, including selected originals, log aliases, supplied instructions and all files in the three previous construction/replay packages. Two historical chart originals were added to the protected list before copying them.

Baseline HEAD: 170e638ecc0438f911c4ceb8091ffb1b574652fe.

Baseline index SHA-256: ff88a675346bdf5aba858329039f400af037fceea1eaa6334586d681c4dbfb4f.

The final result is recorded in [preservation_after.json](analysis/preservation_after.json). It requires all119 protected hashes/sizes to match, every original copy to match, HEAD/index to remain unchanged, and all218 prior status entries to remain present without alteration. The only permitted added status entries are:

    ?? SRG_REDISCOVERY/SIMULATION_RECONSTRUCTION_RESEARCH/
    ?? SRG_REDISCOVERY/SRG_SIMULATION_STUDY_03_PLOT1/

This combines byte-level protection for the selected evidence/prior packages with Git status/index checks. It is not represented as a complete pre/post hash of every unrelated untracked repository file. No writes were directed outside the two new study workspaces. The kernel and accepted research were not edited; no staging, commit, push or publication occurred.

## Reproducibility and delivery

Python inspection used Command Prompt with conda activate torment, as requested. Environment versions and the installed Matplotlib source hash are recorded. Historical dependency versions remain unknown. The five data-inspection scripts are self-contained relative to the package and can be run on a separate extracted copy. Frame-sheet typography uses a named Windows font; regenerated rendering may differ with dependency/font versions.

MANIFEST.json hashes every delivered payload file except itself and the ZIP, avoiding self-reference. ZIP creation then compares every archived member, including the manifest, with its current file bytes and checks CRCs. The manifest records the expected ZIP member count and an archive policy; verify_delivery.py independently checks the completed archive. Extracted originals stay byte-identical to the repository evidence.

The original MP4 is only176,442 bytes; the largest original input is the1,451,175-byte logA. Full decoded stills/contact sheets dominate this review package. MANIFEST.json records actual file sizes and the largest payload file. Nothing is uploaded. Future publication should select useful sheets/stills and avoid repeatedly duplicating derivative media; exact export provenance remains a publication caveat regardless of file size. GitHub hosting limits/policy were not researched or certified during this offline source study.

## Scientific review checkpoint

The record now supports a specific account of carried velocity, stochastic contribution signs, label-clock resets, global kinetic accounting, coordinate-sensitive centroid response and misleading teleport/display diagnostics. It leaves original-run attribution and long-time/causal claims explicitly unresolved.

GPT and Hilmir should review the documents and original evidence before accepting this entry or choosing another simulation. The cumulative ledger marks this study **IN REVIEW**. No next experiment or publication has begun.
