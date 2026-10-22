# CODEX WORK ORDER — SRG_SIMULATION_STUDY_03_PLOT1

**Date:** 22 October 2026  
**Scientific lead:** GPT  
**Research engineer:** Codex  
**Mode:** Single-simulation historical construction + original media/data analysis  
**Authoritative repository:** `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`  
**New output directory:** `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SRG_SIMULATION_STUDY_03_PLOT1`

## Purpose

Study **one** original SRG simulation in comprehensive depth, to reconstruct how its experimental world was built, what it demonstrably did, and how it differs from the already reviewed three-attractor and eight-tetrahedron programs. We are building a source-led, eventual GitHub research edition of all surviving SRG simulations. **Do not turn this into another path-inheritance proof or a broad inventory.**

### Selected historical target

Primary source:

`SRG_REDISCOVERY\OLD_MATERIAL\Simulations_Trash\Simulations_part_1\plot_1.py`

Prior research identifies this as an **eight-body tetrahedral/centroid simulation** using a group-speed factor and a **per-body binary response rule** that can flip with a probabilistic gate. Unlike the `3Dtriangles.py` version just reviewed, it has its own original visual output and logged numerical evidence.

Read the actual source before relying on this summary. Do not assume directory name/date establishes which version was created first.

### Specific existing evidence to recover and inspect

1. Historical movie declared by the source: `tetrahedral_attractors_logic.mp4` (verify the actual location and exact linkage; the program declares 200 animation labels and a 20 FPS MP4 output).
2. Historical saved logs, as indexed in `SRG_REDISCOVERY\R0_SOURCE_RECOVERY\SRG_R0_REPORT.md` §5.1 and `saved_data_checks.json`:
   - `PLOT_1_tetrahedral_states_20250712_015421.csv` — retained R0 evidence reports **8,736 rows / 1,092 eight-object callback blocks**.
   - `tetrahedral_states_20250712_015647.csv` — retained R0 evidence reports **3,520 rows / 440 callback blocks**.
3. Nearby notes, any status/energy/teleport visual output or source-declared artifacts **only if attributable to this exact program**.
4. Comparison baseline: the accepted `SRG_SIMULATION_CONSTRUCTION_02` package and `3Dtriangles.py`, plus `SRG_SIMULATION_REPLAY_01` solely for method/context.

**Crucial evidence caution:** the R0 report records repeated `(Step,Tetrahedron)` keys in the CSVs. These may reflect repeated GUI or save callbacks. **Never sort by frame number and discard duplicates or invent a unique trajectory chronology.** Treat original physical row order, callback blocks and any reset frame labels as distinct. The file `tetrahedral_states_curvature_20250712_062601.csv` was previously traced to a different and incompletely recovered rule: DO NOT use it as if `plot_1.py` generated it.

## Stage 1 — Recover what was actually built

Read the complete `plot_1.py`, including import-time side effects, initialization, random calls, update loop, callback scheduling, logging, animation, and file outputs. Return a plain-language construction walkthrough with exact line locations.

Identify separately:

- State of each moving center (positions, velocities, additional binary mode or sign, and any persistent energy/flags).
- Tetrahedral drawing geometry versus the variables that actually affect movement.
- Initialization and stochastic source; whether any fixed seed survives.
- Centroid recomputation and **in-place order** of eight updates.
- Wrapped positions versus wrapped displacement used in the force; whether the centroid is the arithmetic average of already wrapped coordinates.
- Shared H(frame×DT), group response factor (GRF), componentwise RPCO, and exact placement of factors in the update.
- Binary state transition: when/why a response can switch, what random draw gates it, whether it changes sign of interaction, and how/when its value is recorded.
- Exactly what “energy” and “teleport tracking” mean in the actual source and logs; do not import a physical-energy definition.
- Numerical callback invocations versus nominal frame labels, GUI frames and encoded movie frames.

State any source-code ambiguities or historical dependency limitations explicitly. **Never change the program merely to simplify its analysis.**

## Stage 2 — Examine ORIGINAL evidence first

Open the historical movie; inspect actual frames, preferably all encoded frames for counting and selective frame-by-frame review for transitions, with captioned contact sheets and original full-resolution stills. Extract video metadata, title and labels. Check attribution based on filename **plus** content and source declarations. Preserve the movie byte-identically.

Read the two existing CSVs in source row order and establish:

- Actual schema, per-row state fields, object identities and whether velocities/energy/mode/teleport flags are available.
- Number of complete eight-object callback blocks and partial/corrupt blocks, if any.
- Frame-label repetition and callback order; do **not** equate label 0 with a unique state or discard repeated labels.
- Whether the logged position increments, recorded velocities and binary signs agree with the historical recurrence at checkable samples; independently recheck a modest declared sample from the R0 evidence without altering source.
- Which segments, if any, genuinely show large native increments, coordinate seam wrapping, sudden changes, paired movement, reversal or sign switching. Report magnitudes and indices, not just attractive screenshots.
- Whether a particular historical movie can actually be joined to a specific CSV chronology; if this linkage is unprovable, report **UNLINKED** rather than pairing them by convenience.

If a log is too large for full manual inspection, write **read-only analysis scripts** over copied files, with deterministic selection and record checks. Script execution may analyze historical data; it must not advance a simulated state or rerun the original application. Include full method and selection criteria.

## Stage 3 — Explain what the evidence says

Write the findings in two layers:

**For Hilmir:** Explain how the eight centers respond to their group center, how the optional rule flip affects motion, why colored/transparent tetrahedra can mislead, and whether apparent rapid/teleport-like events are actual numerical jumps or periodic-coordinate display transitions. Avoid technical jargon unless defined.

**For the scientific record:** Provide exact update equations transcribed from code and in execution order; observational measurements tied to original CSV rows/movie frames; quantitative consistency/uncertainty; changes of clock/frame callbacks; proof-level deductions only where truly established; and explicit unresolved questions. Keep observations separate from interpretation.

Compare with `3Dtriangles.py` **only after** studying `plot_1.py` on its own. Carefully distinguish the per-body stochastic reversal and logging from the related version's deterministic no-switch rules. Any striking motion or apparent 'teleportation' must be traced to evidence, not user recollection.

## Deliverables

Produce a GPT review ZIP under the new study directory with at least:

- `START_HERE.md` — approachable explanation of this original simulation and its most interesting source-supported evidence.
- `CONSTRUCTION.md` — step-by-step source walkthrough; original mathematical operators and execution order.
- `ORIGINAL_MOVIE_REVIEW.md` — source linkage, frame and rendering observations, original visual evidence.
- `ORIGINAL_LOG_ANALYSIS.md` — actual schemas, ordered callbacks, verified calculations, notable episodes with exact record references.
- `TIME_SWITCH_AND_MOVEMENT.md` — time labels/callback history, stochastic binary-state rule, H/GRF/RPCO and coordinate wrapping.
- `SIMULATION_02_COMPARISON.md` — what changes from `3Dtriangles.py` and what does *not* follow without further testing.
- `VERIFICATION_AND_PRESERVATION.md` — checks, limitations, source hashes and preservation.
- `MANIFEST.json`, byte-identical source/media/data copies or manifest-referenced originals, inspectable frame sheets/stills, and reproducible read-only inspection scripts with their outputs.

Also initialize or update the **cumulative simulation research ledger** from already accepted Simulation 01 and 02 evidence; append Simulation 03 as **IN REVIEW**, not as an accepted scientific result. This should be a short linked index, **not** another archive sweep. Keep it inside `SRG_REDISCOVERY` in a named simulation-reconstruction workspace; preserve existing papers and indexes.

Use Git-friendly paths, stable names, and relevant compressed or checksum-referenced evidence. Avoid duplicating very large media in multiple directories without purpose. Report if eventual GitHub file-size limits or missing provenance would affect publication packaging.

## Constraints and stop condition

- Original scripts, recordings, logs, research papers, kernel and unrelated files are immutable during this assignment.
- **No new simulation, no fresh random seed, no rewrite of the dynamics, no parameter scan, no behavioral optimization.** Read-only calculation over already existing numerical evidence is authorized.
- Do not run/import an old script if doing so would create random states, mutate data or launch animation. Use safely isolated parsing of source.
- No physics-kernel or production-memory modifications. Keep moving-particle, fixed-grid and later amplitude-coupled models separate.
- Do not claim the movie and CSV belong to the same actual run without evidence.
- No staging, commit, push, GitHub upload or publication yet. Preserve Git HEAD, index and existing working tree entries; record new paths and hashes.
- Stop at one coherent simulation package. Return it for **GPT and Hilmir review before any replay or the next simulation**.

## Primary question

**When the historical eight-body program allowed individual centers to reverse their response, what did that rule actually do in the saved experiment, and how do its time labels, real callback sequence, periodic positions and observed movie motion fit together?**

This is a simulation-construction/recovery task, **not** a test of whether SRG already proves gravity or a theory of everything.
