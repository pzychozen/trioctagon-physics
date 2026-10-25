# Codex work order — SIM06 Tower II: original construction and saved behavior

**Date:** 24 October 2026  
**Assignment:** `SRG_SIMULATION_STUDY_06_TOWER_II_CONSTRUCTION_01`  
**Author / research director:** Hilmir Frímann Halldórsson  
**Scientific lead / reviewer:** GPT  
**Research engineering:** Codex  
**Deliverable status:** For GPT and Hilmir review; not publication authority.

## 1. Scientific direction

Reconstruct **one original program**, `srg_golden_tower_II.py`, and explain what its `GoldenTowerFieldII` construction actually does. Begin from the complete historical source and its own selected driver, not from a new matrix formulation, a desired constant, a physical interpretation, or a modified control experiment.

Hilmir has reaffirmed the objective: recover the old simulations, understand how their constructions were assembled and what they do, without bending their mathematics toward a preferred story. The original source is the baseline even where a comment, observer or historical explanation is misleading. Record a defect or ambiguity; do not repair it silently and call the repaired program historical SRG.

The SIM04/SIM05 publication is finished. It does not need to be reopened to make room for Tower II. Study number SIM06 identifies review order, not a proven development chronology.

## 2. Authority, scope and zero-update boundary

Authoritative Windows repository:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Write new work only under a new, non-overwriting workspace:

`SRG_REDISCOVERY\SRG_SIMULATION_STUDY_06_TOWER_II\CONSTRUCTION_01\`

Use Windows CMD and the existing environment. Do not change dependencies.

**New state-update budget: ZERO.** This order authorizes source reading, source-output attribution, fixed saved-record inspection and visualizations of existing coordinates. It does not authorize a new trajectory, smoke/preflight simulation, RNG sampling, replay extension, seed sweep, ablation, altered model or import of an historical module with executable side effects. Do not rerun the old R0/R1/R2/R3 experiment orders or their scientific checkers.

New passive inspection code may load fixed arrays and calculate descriptive geometry, graph summaries and plots for this one selected existing trajectory. It must never call a field constructor or update, regenerate noise, import the simulator, or feed a calculated successor into the next step. Label any new measurement DERIVED FROM the identified existing records. Reuse accepted measurements when they already answer the question; do not repeat an audit merely to create a new receipt.

Historical sources, accepted reports, recorded trajectories, canonical ledger, published Volumes I/II, physics kernel and production memory system stay unchanged. No Git writes, publication, kernel/UI work, cleanup of unrelated files, or replacement of an accepted edition. A scoped input baseline is sufficient; do not repeat the preceding 27,348-file publication audit.

## 3. Exact original and source identity

The retained R0 source inventory identifies:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\research_files\archive_members\Zenodo_research\19023429\simulations.zip\srg_golden_tower_II.py`

The `simulations.zip` component above is an already-extracted source directory in the recorded archive layout. R0 also contains the unchanged copy:

`selected_sources/MARCH_19023429/srg_golden_tower_II.py`

Expected full original identity:

- Bytes: **34,980**.
- SHA-256: `147a32be3b6d6aad17ada6ab7be2fbc3994c3363f74d6a2b351fb8eecda80304`.

Verify the supplied/local source against that identity, then read the **whole file**, including constructors, helper functions, observers and original drivers. The R0 report is a navigation aid, not a replacement for reading the source. Its prior experiment proposals are historical text only.

The earlier R0 excerpt has SHA-256 `6b2f0a05df5871abe4fe97a9e56abd233ab55952028ae953a4b7a652fb24d5e8`; after its eight-line prefix it preserves original lines 31–254. The existing R1 run uses that excerpt. Verify this identity relationship by text/AST comparison only if needed for attribution; do not execute it.

The handoff contains unchanged R0/R1/R2/R3 context reports and the exact source inventory, but **does not contain the full Tower II original or the R1 raw trajectories**. Use the already recovered Windows material. Locate any needed package through the existing R0 manifest/R1 report and earlier retained archives, not a new whole-corpus survey. If a required source or record is genuinely absent, record its exact missing locator; do not substitute an approximate engine or ask Hilmir to remember its contents.

## 4. One historical configuration and one existing trajectory

### Historical anchor

R0 identifies `self_coupled_breathing.csv` and the source's study at lines 382–418 as seven epsilon settings with N=80, B=4, seed=2038 and 200 passes. Read those lines to recover the actual function name, exact options and output staging.

For detailed construction, select the **epsilon=1 historical configuration** from that original study. Record all source parameters, including the selected coupling width rather than substituting a constructor default. Keep the rest of the seven-row historical CSV as original context; do not create seven new studies.

### Existing coordinate evidence

The completed, accepted R1 study is at:

`SRG_REDISCOVERY\R1_CLIPPING_AND_SPECTRAL_AUDIT\`

Its report describes an existing seed-2038, epsilon=1, breathing-enabled trajectory with N=80, B=4, coupling width 2, mixing strength .001, no horizon, and 600 passes. It retains 601 full X/V/R boundaries and per-pass state/stage/noise records under `RUN_01/seed*_eps*/`; obtain the exact directory name from the existing raw-data index rather than guessing it.

Use **only that one existing enabled trajectory** for the principal motion/geometry account. First verify its source/configuration provenance against the historical selected configuration. The first 200 updates provide the natural comparison window; states 201–600 are a clearly identified later R1 extension, not original 200-pass evidence. If configurations differ, disclose the mismatch and do not present the R1 trajectory as a matching reproduction of the historical setting.

Read prior R1/R2/R3 conclusions to avoid rediscovering completed work. Disabled-breathing, eta=0 and H-off trajectories are labeled **prior controls**, not the original selected run and not new tasks. Their conclusions may be cited with their original scope; no fresh control analysis or execution is required.

If the one selected full record is unavailable, complete the source and original-aggregate study honestly, identify which visual questions remain unsupported, and return a bounded replay proposal with exact source, driver, seed, pass count and capture-equivalence plan. **Do not execute that proposal under this order.**

## 5. Required construction walkthrough

Explain the program in ordinary language before giving equations. The reader should understand one pass without having to memorize research IDs. Identify which objects are evolving, which are assigned once, which are recorded, and which are only names in the commentary.

Read and verify these source-map leads against the original:

- Initial X and R, shuffled band assignments, assigned tower frequencies, pass and RNG state; diagnostic V and stored histories. In particular, establish whether band membership and natural frequencies evolve or remain assigned.
- Nearest-neighbor selection, optional horizon and skipped/underflow rows. Explain which limits apply to local exchange and which do not constrain band-wide fusion.
- Simultaneous local position movement, geometry/frequency-dependent resonance weights, and the exact order of local exchange, frequency modulation and additional mixing terms. Distinguish inserted frequency relations from a frequency measured after the run.
- H schedule, per-band weighted center, signed fusion coefficient, clipping and positional noise, in source execution order. Do not import the single global-center formula from Infinity into this different program.
- Optional breathing readout L: which state it reads, when it is overwritten, and through which operation it can affect the next state. Do not interpret a clipping parameter as a geometric container.
- Observers: per-band coherence, survival, first-lock records, GRF and reported spectrum. A recorded lock or observer threshold must not be promoted to a dynamical instruction.

Keep the source's actual settings, constants, guards, ordering and arithmetic meaning. No parameter fitting, new normalization of the evolving state, new force, invented phase or replacement update is permitted. A normalized plot is only a plot and must be labeled as such.

## 6. Observe the existing geometry before theorizing about it

Answer these concrete questions from the chosen fixed records:

1. What moves in three dimensions, and how do assigned bands occupy that space? Do points with the same label necessarily form one spatial/local-neighbor group? Show the answer rather than assuming it from the word "tower."
2. How do whole-field size, within-band spread and between-band separation evolve? Explain what the existing data actually retain. Distinguish motion of a band center from deformation around it.
3. Which visually distinct episodes can be located in the original aggregate window and the existing reproduced coordinates? Describe two or three examples with stable point IDs, exact pass boundaries and evidence labels.
4. Which mechanisms change as the positions change, and which quantities remain prescribed? Attach the explanation to the observed stages; do not infer causality merely from a correlation or an along-trajectory budget.

Prefer a small useful visual set: a fixed-scale whole-field sequence colored by assigned band; a readable selected-band or selected-point sequence; and existing diagnostics aligned with the geometry. Use equal spatial aspect, disclose changing scale/normalization, retain stable identities and distinguish assigned bands from graph components. No named solid, animation interpolation or emergent oscillation should be inferred from a label or a convenient camera projection.

A movie is optional only if it re-renders saved coordinates without advancing or interpolating a trajectory. Static panels are sufficient. Never present R1 plots as original historical renderings.

## 7. Earlier results are context, not the new assignment

R1 already reports inactive clipping in its selected paired runs and the limitations of the first-bin spectral interpretation. R2/R3 already examine explicitly changed controls and conditional mathematical explanations. Preserve those exact conclusions with their source/configuration qualifiers; do not rerun, strengthen or republish their proofs as newly discovered SIM06 results.

The task here is the missing **construction-and-behavior account**: connect the full original, the original aggregate outputs, the already available coordinate record and those previously reviewed explanations. New theorem development is not required for completion.

A brief comparison with SIM04 and Infinity should identify shared operations and actual differences only after Tower II is understood on its own. Do not force a three-model unifying equation. A brief source-grounded note may identify how Tower I, Universe/condensate and BreathingField differ, using the existing R0 inventory; no separate full investigations of those variants are commissioned.

## 8. Creation history and remaining reconstruction boundary

Include a compact construction-history map with distinct columns for:

- What the code demonstrably shares or changes.
- Dated source statements or comments about the intended idea.
- Saved evidence attributable to that implementation.
- Chronology or causal claims that remain unresolved.

A shared header date, filename, class name or study number is not proof of invention order. Do not infer an author's intention solely from a parameter name. The long-term aim of understanding how SRG was created includes faithfully reporting such gaps.

After this one representative study, recommend whether the remaining March variants contain a genuinely different unresolved mechanism or are adequately covered by the comparison map. Do not automatically open every filename, promise that all SRG has been reconstructed, or begin Volume III. The next decision follows GPT/Hilmir's discussion of this study.

## 9. Deliverables and stop

Return a compact review ZIP with:

- `START_HERE.md`: readable synopsis, what is original/reproduced/derived, what was learned and the exact stop.
- `CONSTRUCTION.md`: full selected recurrence, state/parameter roles, update order and original driver attribution.
- `ORIGINAL_EVIDENCE_AND_EXISTING_REPLAY.md`: original CSV/narrative versus existing R1 records, configuration match/gaps, no new-run claim.
- `MOTION_AND_GEOMETRY.md`: two or three explainable episodes and a small set of readable saved-record visuals with inputs and plotted-data references.
- `MODEL_RELATIONSHIPS.md`: concise comparison and creation-history map, not a speculative universal theory.
- A scoped manifest, used-input identities/preservation receipt, record-selection specification and any new passive inspection code. Include the unchanged selected historical source/CSV and enough exact used records or precise verified local/archive references for GPT to review without requiring Hilmir to find them again.

Read all figures at final size. Separate retained scientific checks from new passive measurements and document checks. Record **zero new state updates and zero RNG draws** explicitly. Do not enlarge the report with irrelevant publication baselines or duplicate old audits.

**STOP for GPT and Hilmir review.** No new simulation, mathematical work order, manuscript, commit, publication or next historical engine is automatically authorized by delivery.
