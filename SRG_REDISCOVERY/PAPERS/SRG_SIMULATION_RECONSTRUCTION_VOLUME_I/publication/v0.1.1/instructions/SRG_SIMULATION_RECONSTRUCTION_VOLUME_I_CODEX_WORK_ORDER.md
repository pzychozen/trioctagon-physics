# CODEX WORK ORDER — SRG_SIMULATION_RECONSTRUCTION_VOLUME_I_01

**Scientific lead:** GPT  
**Research engineer and manuscript preparation:** Codex  
**Author / research direction:** Hilmir Frímann Halldórsson  
**Date:** 22 October 2026  
**Mode:** Evidence-based synthesis and **review-draft preparation only**  
**Repository:** `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`  
**All new output confined to:**
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SIMULATION_RECONSTRUCTION_RESEARCH\VOLUME_I_01`

## Scientific decision and purpose

The first three source-led simulation studies have been reviewed. Prepare the **first substantial research volume** based on them, without starting Simulation 04 or another mathematics/trajectory experiment.

**Working volume title:** *SRG Simulation Reconstruction — Volume I: Three-Point Attraction and Eight-Body Tetrahedral Dynamics*.

This is **Volume I of an ongoing reconstruction**, **not** a claim that all SRG simulations, gravity, or a theory of everything have been reconstructed. Preserve the distinctive experimental SRG constructions, their actual state-update rules, original visual and numerical evidence, and the exact relationship between equations, stored trajectories, animation and observed behavior. The reader should be able to understand what was built, how it works and what each studied experiment genuinely shows.

User preference: detailed research; start each major chapter with an accessible explanation, then provide full technical equations, source locators, figures, measured values, and caveats. Do not use Hilmir's recollections as exact event specifications. No new questions to Hilmir are needed for this bounded draft.

## Existing authority — use; do not rediscover

1. **Research charter:** `SRG_REDISCOVERY\SIMULATION_RECONSTRUCTION_RESEARCH\RESEARCH_CHARTER_v0.1.md`, together with the handed-off charter copy. Use its ORIGINAL / ATTRIBUTED / OBSERVED / REPRODUCED / DERIVED / HYPOTHESIS / MISSING conventions.
2. **Cumulative study ledger:** `SRG_REDISCOVERY\SIMULATION_RECONSTRUCTION_RESEARCH\SIMULATION_STUDY_LEDGER.md`.
3. **SIM01 — `recursive_attractor.py`:** `SRG_SIMULATION_CONSTRUCTION_01` and `SRG_SIMULATION_REPLAY_01` packages; historical `attractors.png`; separately labeled seed-0 reproduction and its saved state/callback records.
4. **SIM02 — `3Dtriangles.py`:** `SRG_SIMULATION_CONSTRUCTION_02` package and source-attributed 2,000-frame `tetrahedral_attractors_animation.mp4`.
5. **SIM03 — `plot_1.py`:** `SRG_SIMULATION_STUDY_03_PLOT1` package, original program, source-attributed 200-frame `tetrahedral_attractors_logic.mp4`, two original CSV logs, historical charts, detailed analysis and verification scripts.
6. **Supplementary context only where directly relevant:** R0 source recovery, FOUNDATIONS_01, equation/operator lineage, prior accepted research and the separate path-inheritance investigations. Those papers must not be presented as evidence that a historical simulation produced a particular event unless they establish it.

**Review status:** GPT's latest scientific review accepts SIM03 **within its evidence and provenance qualifications**. Its ledger snapshot was created while the study was IN REVIEW; update the canonical ledger to record the review acceptance **without altering historical source or evidence classifications**. SIM01 and SIM02 remain accepted baselines. Do not mislabel the original SIM01 PNG as the seed-0 replay, and do not certify the SIM03 movie and CSV as the same historical run; their correspondence remains **strong but formally UNLINKED**.

Locate and check each reference, exact filenames, figures and hashes from the existing packages before citing it. No broad archive re-audit or searching for another simulator.

## Manuscript research content — required

### A. Scope, history and evidence method

Explain the scientific objective and study-selection method. Treat study numbers as **research order**, not necessarily creation chronology. Distinguish original code, likely associated original media, newly reproduced runs, sampled verification, derivation and speculation. Explain missing seeds, missing frame-to-update provenance, reused filenames, repeated callbacks, and why attractive plots alone do not certify movement chronology.

### B. Simulation 01 — three interacting points

Reconstruct the full historical setup and execution order: three 2D positions and carried velocities, independent random initial positions, initial velocities zero, pairwise wrapped relative-displacement response, the actual time argument and H, componentwise logarithmic damping, in-place update order 0→1→2, boundary wrapping, internal position history and final **static** drawing. Transcribe the original equations with parameter values and correct ordered state dependence.

Separate the original `attractors.png` (**original, attributed; missing ordered log/seed**) from the **new seed-0 reproduction** (**reproduced; 500 updates; validated against the unchanged source**). Describe the near-contact and subsequent separation around sweep 169 from the reproduced record only. Explain overlap of visible traces versus simultaneous occupancy and why no delayed path-inheritance episode was established. Note the absence of wrap crossings **in that reproduced run**, not as a general property of the program.

### C. Simulation 02 — eight 3D tetrahedral centers

Explain that fixed tetrahedral offsets are **display shapes**, not moving force-bearing vertices. Reconstruct eight moving centers, retained velocities, sequentially recomputed arithmetic centroid, actual periodic coordinate handling, norm regularization, GRF / H / RPCO placement, animation callback and frame-label relationships, and the original movie evidence. Include a source-faithful discussion of how wrapping a coordinate can both create a large screen relocation and shift the arithmetic centroid driving future updates. Do **not** infer a measured underlying displacement from a movie without the missing ordered numerical record. Distinguish source-derived possibilities from what specific inspected frames support.

### D. Simulation 03 — binary response switching and logged history

Explain the per-body binary sign mode, stochastic toggle gate, carried velocity, centroid, shared GRF, H and damping. Discuss **delayed physical-direction reversal after a sign switch** with the original logged example (body 5 at callbacks 7–9 in the shorter log). Explain the actual CSV schema, callback order and repeated frame labels, including how the state persists when the prescribed H clock label restarts.

Preserve the original evidence counts accurately: **1,092** eight-body callbacks / **8,736** rows in log A, **440** callbacks / **3,520** rows in log B; **200** encoded movie frames. The movie-to-log-B candidate correspondence is compelling but remains **UNLINKED**. Distinguish recorded `K = 0.5 Σ‖v_i‖²` (with zero potential placeholder) from physical conserved energy or the other kernel's potential. Explain the recorded energy/drive bursts at clock resets, without claiming spontaneous energy creation.

Present the source teleport detector's negative-modulo defect versus actual coordinate seam crossings. At checkable transitions, the reported diagnostic would flag **8,151** body events in log A and **3,129** in log B, while actual seam crossings number **22** and **7**. These are two different counting criteria, not measured physical teleportation. Discuss the body-7 seam/reversal episode and the effect of wrapped-coordinate centroid averaging. Use exact record anchors and limitations for all case studies.

### E. Synthesis — mechanisms and genuine distinctions

Provide a comparison with explicit source support for: state dimensions; individual pairwise versus arithmetic-centroid interaction; update ordering; fixed render geometry versus movement rules; time step versus prescribed H argument versus GUI/movie cadence; velocity persistence/damping; GRF feedback; stochastic binary sign; wrap effects; logging and plotting; observed versus inferred collective behavior.

Analyze how source order, state retention and measurement choices change the interpretation of each experiment. Where an exact algebraic identity from existing source and evidence is useful, show its derivation and conditions, with a separate boxed plain-language explanation. Do not force these three simulators into one universal formula, assert that the later study is historically newer solely by study numbering, or reinterpret simulation energy as gravity.

### F. Open questions and scientific boundary

Include a clearly bounded research agenda: missing historical run identities, original time theory/equation lineage, whether path inheritance ever appears in a **specific source-verified chronology**, update-order and wrapping artifacts, and the later geometric/amplitude/neighbor-change simulation families still to be studied. The earlier path-inheritance compatibility/initializer results are **separate limited analyses**, not a discovered replay or a no-go theorem for historical SRG. Mark a future gravity/attractor-energy comparison as a research question, not a result. State explicitly that **Volume I does not finish the project**.

## Evidence and visual requirements

- Every nontrivial mathematical assertion must identify the original program and line range or an accepted proof location; every measured numerical claim must identify a record/row, callback or frame, package document and evidence class. Maintain a **claim-to-evidence matrix**, including caveats.
- All figures must have substantive captions: original versus reproduced versus derived plot, exact origin, relevant axes/units, and what the image **cannot** establish. Select meaningful figures from existing packages; do not create a deceptive combined trajectory that joins separate runs.
- Cite original source/data hashes via package manifests; link large media and logs by relative repository paths rather than duplicating every movie, frame and CSV into the manuscript directory.
- Perform editorial consistency checks for labels, figure references, equation numbering, units, terminology, count reconciliations and claims. Do not silently 'fix' source history; publish a correction note in draft if an earlier account needs qualification.
- Write approachable explanations first, then substantive reproducible mathematical detail. No screenshot collage masquerading as a research chapter.

## Required deliverables (review candidates only)

Create inside `...\SIMULATION_RECONSTRUCTION_RESEARCH\VOLUME_I_01`:

1. `START_HERE.md` — 1–2 pages for Hilmir: what the first three simulations are, what is established, most revealing distinctions, and what remains unknown.
2. `MANUSCRIPT/` — high-detail **Volume I manuscript source** (LaTeX preferred), figure assets chosen from existing evidence, references and a **candidate PDF**, if build tools are present. Aim for a substantive and readable paper/chapter, not an artificial page count. If PDF construction is blocked, deliver the complete source and report the limitation; do not fake a PDF.
3. `CLAIM_EVIDENCE_MATRIX.md` — each major claim, label (ORIGINAL / etc.), exact source, support, limitations and manuscript location.
4. `FIGURE_AND_MEDIA_REGISTER.md` — every chosen figure, its provenance/hash/original location, alterations (crop, resize, overlay), caption and source/run attribution limits.
5. `CROSS_STUDY_MECHANISM_MAP.md` — precise side-by-side state/update mechanism map and version differences, without invented chronology.
6. `OPEN_QUESTIONS_AND_NEXT_VOLUMES.md` — unresolved evidence and later simulation families, without authorizing any new experiment.
7. `REVIEW_REPORT.md` and `MANIFEST.json` — scientific and editorial checks, PDF rendering review/page inspection if available, figure/link/reference checks, file hashes, origin preservation and exact Git state.
8. `SRG_SIMULATION_RECONSTRUCTION_VOLUME_I_01_GPT_REVIEW.zip` — all manuscript and review deliverables, **not** massive repeated source/movie data already anchored in accepted study packages.

Update the **existing canonical** `SIMULATION_STUDY_LEDGER.md` minimally for SIM03's GPT acceptance and a clearly marked Volume I **DRAFT / IN REVIEW** entry. Retain its earlier provenance and existing links. No separate overarching research charter rewrite.

## Permitted operations and hard stop

**Allowed:** read existing sources and evidence; reuse accepted figures; perform read-only static checks and editorial calculations; build and inspect a candidate manuscript PDF; create the new draft/review files; verify hashes and archive integrity. Use Windows CMD (`conda activate torment`) for any local checks/build steps; document them. Read-only inspection of existing data is fine; **no original simulation execution, new trajectory, seed, parameter sweep or scientific checker rerun** unless separately authorized.

**Prohibited:** changing original scripts, simulation rules, kernel_physics, TORMENT production memory, previous papers, accepted study packages or unrelated working material; auto-correcting historical data; staging, committing, pushing, uploading to GitHub, tagging, releasing or publishing. Do not erase or reorganize other research directories. Record existing status entries at start and require no loss or alteration at finish. File hashing/manifest checks must identify exact coverage rather than implying a complete repository certification.

**Stop after delivering the high-detail draft and review ZIP.** GPT and Hilmir will read and decide whether it is scientifically sound, whether the manuscript needs revision, and whether a **separate explicitly approved GitHub publication** should follow. The next simulation and the conceptual time-equation study remain parked until that review.

**Final question for this assignment:** Can a reader reconstruct, from authentic source and attributed evidence, **what these three historical SRG simulators actually calculated and displayed, why their behaviors differ, and what we can and cannot conclude**—without relying on lost memories, speculative physics or new equations?
