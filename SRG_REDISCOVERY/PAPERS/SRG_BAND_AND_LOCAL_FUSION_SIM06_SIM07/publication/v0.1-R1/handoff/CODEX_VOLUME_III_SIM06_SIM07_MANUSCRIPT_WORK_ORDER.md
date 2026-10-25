# Codex work order — Tower II and Universe reconstruction manuscript

**Date:** 25 October 2026  
**Assignment:** `SRG_VOLUME_III_SIM06_SIM07_MANUSCRIPT_01`  
**Author and research director:** Hilmir Frímann Halldórsson  
**Scientific lead and reviewer:** GPT  
**Research engineering and manuscript preparation:** Codex  
**Output:** Candidate v0.1 for GPT/Hilmir review; not publication-approved.

## 1. Decision: write the completed studies now

Prepare a detailed, self-contained research manuscript from the accepted SIM06 Tower II construction study and SIM07 Universe construction plus finite replay, incorporating all three GPT reviews and their accepted additional findings.

Working title:

> **SRG Simulation Reconstruction — Volume III: Band-Wide and Ordered Local Fusion in Tower II and Universe**

The volume number is provisional. The substantive scope is these two original programs and their specified evidence, not all historical SRG or the entire March collection.

**This order changes the sequence in earlier handoffs: draft and review this paper now, BEFORE any BreathingField/field-merger study.** Preserve those earlier plans unchanged as historical records. The merger remains an explicitly deferred construction, not an unstated prerequisite, an accepted result, or authority to launch another investigation.

Hilmir has delegated the immediate research choice while feeling unwell. The scientific reason for choosing a manuscript is that both selected studies have reached acceptance with no required scientific corrections. Another simulation is not needed to explain their results. Do not require Hilmir to select chapters, reconstruct dates, recall parameters, or supply material already in the enclosed archives.

The paper must explain what the original code calculated, how its retained outputs arose, and how the two constructions differ. Mathematical exposition should clarify those operations, not repair the historical dynamics, fit a preferred story, or invent a single canonical SRG model.

## 2. Scope, workspace, and zero-execution boundary

Authoritative repository:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Research root:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY`

Suggested new, non-overwriting candidate workspace:

`SRG_REDISCOVERY\PAPERS\SRG_BAND_AND_LOCAL_FUSION_SIM06_SIM07\draft\v0.1\`

Check whether that directory already contains work; use a new revision directory rather than overwriting anything. Confine output and temporary document-build work to the new workspace. Use **Windows CMD throughout**, with the existing `torment` environment as needed. The prior PowerShell-reading deviation is disclosed in the accepted SIM07 review; do not repeat it or rewrite its historical record.

**Scientific execution budget is ZERO:**

- No simulator imports, constructors, state updates, fresh initializations, RNG draws/restorations, reference/capture runs, seed searches, reordered alternatives, ablations, parameter sweeps, or longer trajectories.
- No numerical scientific-checker reruns, new graph/cluster calculations, new geometry statistics, new FFTs, or regeneration of accepted scientific results. The earlier 400-update replay allowance is exhausted and closed.
- No field-merger source study or execution, Tower I study, new archive survey, new theoretical program, or unrelated literature search.
- No historical-source, accepted-study, canonical-ledger, kernel, UI, memory-system, or published-Volume-I/II changes. No staging, commits, push, tag, release, repository publication, or integration.

Permitted work: read source and accepted results, inspect existing images, hash and compare files, transcribe reviewed equations, expand already reviewed arguments in prose, arrange existing tables, compile document sources, render pages, and check citations and document integrity. Reusing accepted plotted values for a strictly presentational re-export is permitted only for legibility; preserve the old image, record its input and transformation, and introduce no new measurement, interpolation claim, fitted geometry, or scientific result.

Read archived methods as text only. Their inclusion is not permission to execute them. If a claim cannot be substantiated from accepted material, qualify or omit it and record the issue; do not quietly launch the missing calculation. Do not change historical code to make its terminology sound correct.

## 3. Immutable inputs and precedence

The handoff includes three complete accepted review archives:

| Key | Archive | Accepted scope |
|---|---|---|
| S6 | `inputs/SIM06_TOWER_II_GPT_REVIEW_AND_ACCEPTANCE.zip` | Historical construction and fixed saved-record study of Tower II; includes the unchanged submitted source, R1 records, reports, figures and GPT additional findings |
| S7C | `inputs/SIM07_UNIVERSE_GPT_REVIEW_AND_ACCEPTANCE.zip` | Universe original-source and original-aggregate construction study; includes all five original CSVs and the historical narrative |
| S7R | `inputs/SIM07_UNIVERSE_REPLAY_GPT_REVIEW_AND_ACCEPTANCE.zip` | Accepted source-faithful finite Universe replay, complete records, six figures and GPT additional findings |

`INPUT_MANIFEST.json` records actual archive identities. `INPUT_READING_INDEX.md` gives exact archive-member paths for required reading; `ARCHIVE_CONTENT_INDEX.json` lists members and sizes. Matching existing Windows inputs may be reused without unnecessary additional copies. The enclosed archives provide a complete fallback and must remain byte-identical.

The originals determine implemented operations. Original records determine what historically survives. Accepted capture records determine reproduced behavior. Accepted reviews provide corrected interpretation, verification scope and additional findings. A source comment or historical narrative is not evidence that its physical or dynamical interpretation is true. If accepted prose and the source appear inconsistent, document the exact discrepancy rather than silently reconciling it.

**Do not promote retained R3 material from review-status to accepted science.** SIM06 explicitly does not retroactively accept the separate R3 submission. R0–R3 context is reusable only with its existing status, source, configuration and qualifiers attached.

Read the three complete GPT reviews, not only the starting guides. In particular:

- S6: `SIM06_GPT_SCIENTIFIC_REVIEW.md`; `source_package/CONSTRUCTION.md`, `MOTION_AND_GEOMETRY.md`, `ORIGINAL_EVIDENCE_AND_EXISTING_REPLAY.md`, `MODEL_RELATIONSHIPS.md`, `RECORD_SELECTION.md`; `independent/FINDINGS.json`, `combined_dependency_graph.csv`, `VERIFICATION.json`; original source and figure register.
- S7C: `SIM07_GPT_SCIENTIFIC_REVIEW.md`; all five construction/evidence reports; `independent/FINDINGS.json`, `SOURCE_READBACK.md`; original source, five tables, narrative and figure register.
- S7R: `SIM07_REPLAY_GPT_SCIENTIFIC_REVIEW.md`; `source_package/MOTION_AND_GROUPS.md`, `ORDERED_FUSION_TRACE.md`, `REPLAY_FIDELITY_AND_PROVENANCE.md`, `VERIFICATION_AND_LIMITS.md`, `RECORD_SCHEMA.md`; `independent/FINDINGS.json`, `GRAPH_COUNTS.csv`, `ORDERED_READ_COUNTS.csv`, and three independent audit records; figure register and supplied plotted-data tables.

## 4. Reader-first manuscript structure

Write an explanatory research paper, not an administrative receipt and not a concatenation of reports. No page quota and no artificial proposition quota apply. Use sufficient space to make the two algorithms reconstructible on paper, including the subtle ordering and guards. Put detailed provenance and label audits in appendices where that improves the narrative.

### A. Orientation: different meanings of a group

Start with ordinary language: an indexed point has three coordinates and a real resonance value. Its row identity persists. Explain why a point's assigned band, original population, local-neighbor component, spatial-observer group, and membership in a center calculation are different relations. Diagnostic velocity records a completed displacement in both models; it is not carried momentum.

State the paper's positive question: how do band-wide centers and ordered local centers connect geometry and amplitude evolution, and how do saved observations reveal those constructions? Include an early figure, a compact glossary, and separate conceptual and exact-mathematics reading routes.

### B. Evidence and historical construction

Define ORIGINAL, ATTRIBUTED, OBSERVED IN HISTORICAL DATA, REPRODUCED, DERIVED and UNRESOLVED once. Apply them consistently to claims, captions and tables.

Tower II uses an unchanged 842-line source and the original seven-row `self_coupled_breathing.csv`. The selected historical setting is N=80, four bands, seed 2038, epsilon=1, coupling width 2, no horizon, 200 passes. Its already existing R1 record has **601 boundaries, 0–600**. Separate the historical-configuration comparison window 0–200 from the later R1 extension 201–600; do not imply original 600-pass coordinates were recovered. SIM06 performed passive analysis, not another run.

Universe uses an unchanged 778-line source, narrative, and five original numerical outputs totaling 233 rows. Its main chronology has **200 rows, passes 1–200**, without original individual coordinates. The selected replay uses seed 1618, N=120, six supplied populations of 20 points, horizon 6, assigned frequencies, prescribed breathing and 200 passes. Its reference/capture records have 201 boundaries. Both executions are one setting with recording-fidelity validation, not independent trials or a 400-pass single trajectory.

Explain the initialization draw-order issue: supplied Gaussian populations, constructor draws subsequently overwritten, assigned-frequency draw, replacement amplitudes, and later noise must retain their source order. Do not reconstruct those draws again for the manuscript.

Source headers and narrative statements may establish attributed motivation or stated dates. They do not establish a complete authorship/execution chronology. Study numbers are investigation order. Preserve the original contributor attribution without inventing a development story.

### C. Tower II: exact construction before behavior

Give a complete stage map with source lines. Preserve initial fixed bands/frequencies, the shuffled 20-per-band allocation, incoming neighbor selection, componentwise local movement, log-frequency-ratio weighting, its raw-weight guard, imposed frequency sine, additive phi-ratio and sum/difference contributions in actual order, common H multiplier, once-per-band weighted centers, signed fusion coefficient, signed compressor, decaying noise, diagnostic V and observer recording.

Use the accepted stage notation or an explicitly mapped consistent notation. Do not swap pre-H, post-H, pre-clipping and final amplitudes. Preserve absolute center weights versus signed displacement. Explain that a band center includes all its members regardless of current local components, is calculated once before that band's inner writes, and is distinct from both one global center and a sequentially recomputed local center. Do not silently change the no-horizon self-sorting assumption or finite-horizon guard.

Explain the actual role of inserted frequency labels, additive mixing, H and the overwritten bound. Distinguish the code's label 'nonlinear mixing' from the accepted statement about linearity in incoming R at frozen geometry/frequencies; do not infer linearity of the full moving system. The master-equation driver's post hoc calculation is not a recurrence term.

### D. Tower II: recorded behavior

Connect fixed-scale spatial views, band-normalized detail and identifiable point paths to the accepted records. Explain early multi-band local groups, late concentration, center motion versus internal spread, continuing displacement, and lock thresholds versus geometry.

Include the accepted extra finding: the **analysis-only union of local selections and same-band center dependencies is weakly connected at all 600 inspected incoming boundaries**. State what that graph means and what it does not mean: not added interactions, not a complete state-variable Jacobian, not measured influence strength, not universal strong connectivity or physical propagation.

Anchor the late example at **boundary 599 supplying pass 600**, not an unrecorded 601st update. Its 41/22/17 local components are spanned by band 0, with ID 62 in the first and IDs 25/74 in the second. Use the exact accepted membership table.

The spatial variance decomposition distinguishes descriptive arithmetic band centers from weighted fusion centers. The between-center share rises from roughly 3.78% initially to 96.65% at state 600 while both within- and between-band variance decrease. Do not describe that share increase as band centers moving farther apart. Lock times 3,4,5,7 precede the first weak local-graph split at state 10.

### E. Universe: exact construction and original-output attribution

Describe the full source, selected driver and separate experiment drivers without executing any. The horizon applies a strict distance eligibility test followed by at most five selected neighbors; finite-horizon rows can be empty. The original populations are not a coupling label. Frequencies are assigned, not evolved. This is a single-amplitude engine, not Infinity's two-field trajectory resumed.

Preserve simultaneous initial position movement; incoming-R exchange; inverse-distance normalization followed by the optional ordinary squared-frequency-difference factor and second-normalization guard; sine placement and skipped rows; H; ordered fusion; prescribed clipping bound; noise; V; completed-state observers. The optional frequency kernel is not Tower II's log-ratio kernel or its additive mixing rule.

In the finite-horizon fusion branch, neighbor identities are frozen from incoming positions, resonance is fixed at the post-H/pre-clipping stage, and ascending-ID writes update one position at a time. Local centers exclude self, use amplitude-magnitude weights without distance weights, and read current coordinates. In the `None` branch the center is all-point and computed once before simultaneous motion. Changing horizon to `None` changes the fusion branch as well as eligibility; do not claim a radius-only control.

Explain which original output belongs to which driver. The horizon table contains configuration/trial endpoints, not a trajectory; the perturbation labels are DECAYING; equal static/breathing summaries do not prove coordinate equality. Preserve original numbers and distinguish supplied interpretations from supported observations.

### F. Universe replay: motion and actual ordered reads

Use the accepted snapshots and episodes to explain what the reproduction adds beyond aggregates. Describe six input populations, four assigned frequencies, the ten later observer groups, the local selection graph, and continued motion separately.

Required details include stable observer memberships from passes 16–200, same-boundary graph/observer mismatch in both directions, point 97's brief cross-population contact, link loss while still inside the horizon because five closer neighbors take the selected places, and actual earlier-written coordinates read by later fusion rows.

The accepted row-6 example at pass 16 reads IDs 2 and 5 after their writes, and IDs 11,16,18 before theirs. The supplied actual-operand decomposition shows an earlier-write contribution; it is **not** a measured trajectory difference between ascending, reversed and simultaneous models. No such counterfactual was run.

Keep graph boundaries precise: captured incoming graphs are 0–199, supplying updates 1–200. The ten/13/14 observer/weak/strong comparison is at **boundary 199**, not a newly measured final-boundary graph. Paths between saved samples are sampled polylines, not a continuous-time law or evidence of an assigned explorer role.

### G. Observers, bounds and reviewed mathematics

Explain why labels such as lock, resonance cluster, breathing, fusion and condensate do not substitute for their implemented definitions. Amplitude-gap groups, average-linkage groups, graph components and bands are not interchangeable. The original velocity-dependent GRF is a mean of reciprocals, not a reciprocal of the mean speed or a physical force.

Retain the following reviewed mathematical explanations, with their actual scope:

1. The point-count-weighted spatial decomposition `Rg^2 = within + between` for assigned bands, using arithmetic descriptive centers.
2. The ordered local-center read/write expression using actual earlier row outputs and later post-local coordinates. Expand the accepted algebra and explain indirect dependencies, but do not introduce a new general convergence/order-sensitivity theorem.
3. The already reviewed pooled-coordinate variance identity `s_flat^2 = Rg^2/3 + sum_d(mu_d-m)^2/3`, where `m` is the scalar mean of the three center components. Give the accepted short proof and explain origin dependence. Do not replace the old measurement and label the replacement original evidence.
4. Other already accepted conditional arguments may be retained with direct review locators. Do not transplant Volume II's unrestricted minimum-six conclusion to arbitrary horizon-filtered graphs: empty or short rows are possible here.

Tower II's L is an incoming-mean-amplitude readout, while Universe's L is a prescribed function of the pass. Neither is a spatial container. The tested inactive-clipping conclusions have different evidence: retained R1 controls for Tower II versus recorded pointwise activation checks for the one Universe replay. Do not infer a Universe breathing-off experiment or universal irrelevance of compression. Inside the positive unclipped regime, the source log/exp expression has the reviewed epsilon effect in exact arithmetic; do not silently remove it from the original update.

### H. Comparison, origin account and finish line

Use one precise comparison table: state, initialization, carried information, neighbor selection, amplitude weighting/mixing, center definition, write ordering, schedules, noise, bounds, observers and evidence windows. A brief reference to published global-center models provides context; do not reopen their experiments.

The Tower II and Universe runs differ in initial geometry, N, seeds, assigned labels, interactions, schedules and duration. They are **not a controlled one-factor experiment**. A difference in observed contraction cannot be attributed solely to band-wide versus local fusion. Source differences establish different algorithms; recorded trajectories show their behavior under the specified settings.

Separate 'what the code calculates' from 'why the historical author tried it'. Use the source/note's stated motivations where available, preserving attribution. Unknown chronology stays unknown. The manuscript should not turn the old original-source corrections into a hostile or dismissive account, nor repeat physical claims unsupported by the records.

End with what is understood and the remaining evidence limits. State that the BreathingField merger is **deferred and outside this volume**. This paper does not depend on it. No new experiment list is required to make the paper complete. A compact reconstruction coverage/status appendix is useful, but must be compiled only from supplied context; do not survey the wider archive to fill it.

## 5. Quantitative and interpretation anchors that must survive synthesis

These are existing accepted results to cite, not new calculation requests. Read the corresponding review before rounding/transcribing.

### Tower II

- 601 saved boundaries and 48,080 point-state records; new SIM06 update budget was zero.
- Historical comparison setting stops at 200; 201–600 is the later R1 extension.
- State-20 local components: 14,6,10,8,10,32; each contains every band.
- Boundary-599 components: 41,22,17; band 0 spans all three. Combined structural graph weakly connected at all 600 inspected boundaries; strong component count varies.
- Whole-field Rg: 5.261566081 initially, 1.352830056 at state 200, 0.0549954406 at state 600. Nonzero late movement remains.
- Band IDs/frequencies are supplied. First-lock thresholds are observer events, not stop instructions. The retained 150-sample first-bin spectral qualification is not proof of a self-sustaining heartbeat and not a claim that all SRG oscillation is impossible.

### Universe construction and replay

- Original numerical corpus: five CSVs, 233 rows; main chronology has 200 rows and 15 columns.
- Historical replay comparison: **3,000 cells including 200 pass labels**, hence **2,800 non-pass metric cells**. All 800 integer cells exact; all 2,200 continuous cells within `1e-12 + 1e-10*abs(original)`. Exactly 2,312/3,000 parsed cells agree; remaining 688 differ slightly. Maximum discrepancy about 1.78e-15. Reference/capture exports agree byte-for-byte; the historical/replay CSVs do not.
- Exactly two prescribed initializations and 400 updates in the earlier replay; 201 boundaries and 24,120 point rows per run. These are recording-fidelity twins, not independent trials.
- Ten observer groups retain their member sets over 185 observations, passes 16–200. Sizes: 10,10,20,9,11,20,9,11,13,7. All 120 points still move at pass 200; mean completed step about .005118790595.
- Same-boundary comparison at 199: ten observer groups, 13 weak and 14 strong local components. At boundary 16 P0 is two observer groups but one local component; P1 is one observer group but three local components. Neither partition universally refines the other.
- Cross-population selections: 39 selects97 in passes1–3; 97 selects34 in1–6; 97 selects39 in1–8. Three unique directed pairs, 17 selection visits. None in the captured input graphs for passes9–200. First absent distances remain below6 because closer selections occupy the five slots.
- Point97's sampled path length is about8.119170932; no assigned pathfinder role or physical trajectory identification follows.
- 24,000 fusion row visits and120,000 recorded selected-coordinate reads; 60,118 earlier-written and59,882 later-unwritten reads. Explain the counts, rather than treating them as independent experiments.
- Zero clipping activation in24,000 captured point updates; this is one finite replay, not a general statement or a newly executed paired control.
- P3 endpoint pooled std about3.238809712 versus centered Rg .066949097 and diameter .166308988. Preserve the old statistic and explain the difference.
- At historical pass20, the amplitude-gap observer reports one group despite a max/min ratio about3.060341. That count does not mean amplitude equality.

Do not add an energy minimum, physical gravity, conserved momentum, phase orthogonality, emergent frequency catalogue, universal law, exact solid, infinite-time conclusion or necessary master-constant derivation. These are not established by the accepted evidence. Avoid repeating the exclusions so often that the positive explanation becomes unreadable.

## 6. Figures, evidence, and document quality

Reuse the three accepted Tower II figures, the six accepted Universe replay figures, and the two original-aggregate Universe plots where they add information. Select and arrange rather than include every panel by reflex. No fixed figure count is imposed. Fixed world-scale overviews and properly disclosed centered/normalized detail should remain readable at the final PDF size. Do not obscure the difference between point markers overlapping and points actually merging.

Copy accepted image bytes unchanged wherever possible. Captions must identify model, historical versus reproduced data, exact pass/boundary window, labels/IDs, omitted projection coordinates, normalization and the supported conclusion. Mark Tower II extension material visibly. If a figure spans a landscape page, inspect the actual rotated PDF—not a cropped text-extraction thumbnail.

Provide clear source-relative paths, normal manuscript citations and stable equation references. No chat-only citation tokens or Windows-only access as the reader's sole evidence. Preserve original source line anchors; the prior accepted corrections are not a request for a new global line-number audit. A claim–evidence matrix must point to exact original source ranges, retained data tables, recorded episode operands or accepted review derivations. State historical versus reproduced origin on each major claim.

A conceptual dependency/ordering schematic may be typeset from the accepted construction if explicitly labeled conceptual. It must not masquerade as an observed spatial configuration. No generated illustrative physics scene is required.

Document checks are new; numerical validation is retained. Say that plainly in the editorial notes. Do not report old tests as newly run. Retain the original contributor attribution and distinguish internal GPT review from external peer review.

## 7. Required deliverables

Return one clearly named candidate review ZIP and a separately accessible PDF:

1. `manuscript.pdf`, editable `manuscript.tex`, bibliography and selected figure assets, with document-only build instructions.
2. `START_HERE.md`: short explanation for Hilmir, conceptual reading route, principal conclusions, candidate status and any genuine editorial issue. No need for him to read technical manifests first.
3. `CLAIM_EVIDENCE_MATRIX.md`, `FIGURE_REGISTER.json`, and `EVIDENCE_INDEX.md` with usable relative links and exact archive-member locators.
4. `EDITORIAL_AND_VERIFICATION_NOTES.md`: incorporation of all three reviews, original/reproduced distinctions, retained checks, document checks performed now, and any discrepancy.
5. `RECONSTRUCTION_SCOPE_AND_REMAINING_GAPS.md`: SIM06/SIM07 complete within their reviewed scopes; Volumes I/II remain frozen; merger explicitly deferred; no claim that every historical SRG family is reconstructed. This records the changed sequence without editing old plans.
6. Necessary unchanged supporting files and the three immutable input archives, or an equally complete self-contained evidence layout with exact parent/member identities. Do not rely on an untracked local path. Avoid including duplicate extracted copies of every replay array in addition to the full archive unless actually needed.
7. Scoped manifest, used-input preservation receipt and page/document QA record. Provide an external ZIP-identity sidecar beside the ZIP; do not put a receipt inside an archive claiming to hash that same archive.

Keep compiler caches, temporary renders and unrelated work out of the delivered ZIP. Preserve working renders locally. Baseline the actual inputs used and relevant protected output paths; do not manufacture another whole-repository audit or assert live filesystem coverage beyond what was checked.

## 8. Completion gate and stop

Inspect every rendered PDF page for readable equations, tables, figures, captions, bibliography and navigation. Confirm that a reader can reconstruct each selected update on paper without guessing snapshot timing, guards, sign conventions or loop order. All substantive comparative statements must distinguish a source difference from a measured one-factor causal effect.

Confirm exact preservation of accepted source/data/figures and input archives. Return the candidate even if an optional explanatory claim has to be omitted for lack of support; record that issue instead of opening more research. A genuine contradiction in a central accepted claim must be surfaced explicitly for GPT review, not silently patched.

**STOP after manuscript delivery for GPT and Hilmir review.** No merger study, fresh simulation, publication preparation, commit or next-engine assignment follows automatically. The next work is reviewing and closing this manuscript; a fresh-chat handoff can then preserve this completed block and its explicitly deferred item.

This order authorizes drafting and document operations only. It does not declare the new manuscript accepted or grant publication authority.
