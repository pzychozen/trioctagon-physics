# Codex work order — SIM04 and SIM05 reconstruction manuscript

**Date:** 23 October 2026  
**Assignment:** `SRG_VOLUME_II_SIM04_SIM05_MANUSCRIPT_01`  
**Author / research director:** Hilmir Frímann Halldórsson  
**Scientific lead and reviewer:** GPT  
**Research engineering and manuscript preparation:** Codex  
**Output status:** Candidate manuscript v0.1, for GPT and Hilmir review; not accepted for publication.

## 1. Decision: write these two studies now

Prepare a detailed, self-contained research paper explaining the accepted SIM04 Seed Explorer study and SIM05 Infinity study, including both GPT scientific reviews, their additional findings, and the accepted SIM04 3D addendum.

**This order changes the sequence previously stated in `MODEL_FAMILIES_AND_PAPER_PLAN.md`: draft and review the SIM04/SIM05 paper BEFORE any Tower II construction study.** The older plan remains an unchanged historical planning record. Do not alter it to conceal this change. Tower II is deferred, not a prerequisite for this manuscript and not authorized by this order.

Working title:

> **SRG Simulation Reconstruction — Volume II: Local Geometry and Resonance in Seed Explorer and Infinity**

The volume designation is provisional. The paper's substantive scope is exactly these two programs, not the whole March collection or a completed reconstruction of all SRG. Study numbers identify our investigation order, not a demonstrated historical development sequence.

The immediate objective is understanding: Hilmir should be able to read one coherent account of what exists in each program, how an update works, how the observed organization develops, what the observers measure, and what has and has not been established. Do not assemble an administrative report by concatenating the study documents. Preserve their substance while giving the reader a clear explanatory progression.

## 2. Authority and zero-run boundary

Authoritative repository:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Research root:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY`

Create a new candidate directory, for example:

`SRG_REDISCOVERY\PAPERS\SRG_LOCAL_GEOMETRY_AND_RESONANCE_SIM04_SIM05\draft\v0.1\`

If that directory already contains work, inspect it and choose a new non-overwriting draft revision. Never overwrite an accepted or frozen edition. Use Windows CMD and the existing environment for approved document operations.

**New simulation/update budget: ZERO.** The earlier 400-call Infinity allowance was exhausted and closed; it does not carry forward. Do not import or run historical simulators, replay drivers, reference/capture code, parameter studies, seed trials, ablations, Tower programs, or numerical verification scripts that regenerate scientific results. Do not draw another random sequence or advance a state.

Permitted operations are reading accepted source and saved outputs, checking input/file identities, transcribing already reviewed equations and proofs, selecting existing results and figures, typesetting, compiling the manuscript, rendering pages for visual inspection, and checking citations, links and document integrity. A purely presentational re-export from an already supplied plotted-data table is permissible when needed for legibility; it must not add measurements, a new estimator or a new scientific claim.

No kernel, UI, production-memory, historical-source, accepted-study, canonical-ledger, or published-Volume-I changes. No staging, commits, pushes, release, publication or integration. No new archive survey. Keep all outputs in the new draft workspace. Source refinements here mean improved explanation, not changes to the historical algorithms.

## 3. Inputs and how to use them

The supplied handoff contains two immutable input ZIPs:

1. `inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip` — the original SIM04 submission, its source and historical CSVs, explanatory documents, figures, checks and provenance.
2. `inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip` — the accepted SIM05 review and independent findings; `source_package/` contains Codex's unchanged SIM05 submission. Its `source_package/context/SIM04_GPT_REVIEW/` contains the accepted SIM04 GPT review, its additional figure and reviewed calculations.

`INPUT_MANIFEST.json` identifies the exact supplied archives. The Windows originals remain authoritative; use matching local accepted files rather than making unnecessary duplicate working copies. The enclosed archives provide a self-contained fallback and exact review inputs. Check the specific inputs, not the whole repository.

Read at minimum:

- SIM04: `START_HERE.md`, `CONSTRUCTION.md`, `ORIGINAL_EVIDENCE.md`, `VERIFICATION_AND_LIMITS.md`, `FIGURE_REGISTER.json`, original script and CSVs.
- SIM04 GPT review: `SIM04_GPT_SCIENTIFIC_REVIEW.md`, `source_review.md`, relevant `independent_data/` results and `additional_figure/` data.
- SIM05: `CONSTRUCTION.md`, `HISTORICAL_EVIDENCE_AND_CLAIMS.md`, `REPLAY_AND_3D_ANALYSIS.md`, `SIM04_3D_ADDENDUM.md`, `VERIFICATION_AND_LIMITS.md`, figure register and the exact original source.
- SIM05 GPT review: `SIM05_GPT_SCIENTIFIC_REVIEW.md`, `verification.json`, `findings.json`, `final_components.csv` and `supplemental_checks.json`.
- `MODEL_FAMILIES_AND_PAPER_PLAN.md` only for scoped relationships and inherited context; its next-task sequencing is superseded by this order.

Original source determines what the code implements. Original records and accepted replay records determine what was recorded. Accepted reviews supply the reviewed interpretation, proof assumptions, additional findings and acceptance boundaries. If these appear inconsistent, record the exact discrepancy in the editorial notes; do not silently repair a source, invent a reconciliation or launch a new experiment. Omit or qualify an unresolved claim while continuing the supported manuscript.

## 4. Required reading structure

Write a full explanatory research manuscript, not a short summary. There is no page quota: use the length needed for complete construction and understandable evidence, without padding or repeated caveat lists.

### A. Abstract and reader's orientation

State the reconstruction question, the two programs, the two different evidence situations, the principal observations and the finite scope. Begin the main text with a short explanation of what a moving point and its resonance values are in these programs. Explain the central distinction between spatial compactness, amplitude agreement and local connectivity before introducing all notation.

Give the reader an early, clearly labeled visual overview. Explain that nearby or overlapping markers are distinct points, not newly merged bodies. Include a compact glossary and a reading route for the conceptual account versus the exact mathematics.

### B. Evidence and reconstruction method

Distinguish ORIGINAL, ATTRIBUTED, OBSERVED IN HISTORICAL DATA, REPRODUCED, DERIVED and UNRESOLVED. Define those terms once, then use them consistently in claims, tables and captions.

SIM04 has 21 historical state boundaries, passes 0–20, totaling 1,050 point rows and 20 metric rows. Its unsaved positional random increments remain unresolved. Its new visualizations come from original saved coordinates, not from a recovered original movie.

SIM05 has original source, historical aggregate evidence and a separately authorized 200-pass replay with 201 captured state boundaries. The complete five-group trajectory is REPRODUCED evidence. Agreement with 4,000 historical metric values supports attribution, but does not certify the lost original environment or reconstruct a historical movie.

Summarize retained checks; do not rerun them. Distinguish reference/capture repeatability from GPT's independent conditional-equation and RNG-checkpoint verification. Use exact comparison denominators: 2,785/4,000 metric entries are exactly equal; the 200 pass labels bring the table-wide count to 2,985/4,200. All 4,000 metrics satisfy the recorded tolerance.

### C. Seed Explorer: complete construction, then behavior

Define its state, initialization, directed five-neighbor selection, normalized weights, simultaneous local movement and resonance exchange, pass-dependent H normalization, global weighted-center fusion, R sine schedule, signed RPCO and positional noise in actual execution order.

Show which quantities persist and are consumed by the next step. The stored velocity is a displacement diagnostic, not carried momentum. The historical H/memory terminology does not establish reading of saved trajectory history. Separate evolving quantities from observer-only labels and reports.

Explain the historical sequence and the six-point component, including amplitude ranking versus organization, stable ranking with continued movement, local separation with remaining global coupling, and the finite record boundary. Incorporate the accepted 3D addendum here, not as an unrelated new simulation.

### D. Infinity: complete construction, then behavior

Define X, R, D, pass and RNG state; diagnostic velocity; local weights; distinct R and D mixing; shared cross-channel terms; two H schedules; R-weighted fusion; R-only sine schedule; separate signed RPCO and decaying positional noise. Provide clear stage notation so incoming and outgoing arrays cannot be confused.

The literal `.08699` is an active supplied parameter through the specified cross-coupling coefficient; it is not derived by the program. The `.244` in the cross schedule is in radians per pass, while the R sine uses `.244` cycles per pass through `2*pi`. Preserve this distinction.

Explain the five-group replay, membership persistence in the observed window, continuing motion, positive small D, clipping events, stage contributions and observer outputs. Do not equate a small field with an inactive one. Late direct H effects rounding to zero do not remove earlier H-dependent history.

### E. Geometry and the meaning of the observers

Define local directed graph, weak versus strong components, diameter, radius of gyration, within-group spread and between-group differences. Explain that local graph disconnection does not remove the global fusion coupling. State what measurement establishes a claim instead of relying on a picture alone.

Explain the actual timing of each observer. In Infinity, the accepted endpoint echo calculation uses pass-199 distances with pass-200 amplitudes; those states have the same partition. Curvature uses updated positions with incoming neighbor selections. Do not replace these with a more intuitive but different observer.

Include the audited interpretations of seeds, echo corridors, coherence, diagnostic energy and historical shape classifications. Keep concise corrections in the narrative and detailed label/claim audits in an appendix. Do not turn these implementation interpretations into physical identifications.

### F. Reviewed mathematical results

Develop the already reviewed results as readable propositions, lemmas or identities, each with hypotheses, a proof, an explanation and a scope boundary. Clearly distinguish exact real-arithmetic statements from finite-record observations and approximate agreement.

Required results:

1. **Smallest isolated five-neighbor component.** With five distinct non-self neighbors per point and no cross-component selections, a weakly isolated component contains at least six points. A six-member component has 30 directed internal selections. This explains a rule-imposed minimum, not a universal sixfold solid or a requirement for five groups.
2. **SIM04 positive unclipped averaging.** State positivity, inactive clipping and the positive common-gain assumption explicitly. Present the reviewed common gain/offset normalization and nonexpansion of its normalized amplitude interval. Explain why this is not unweighted-mean conservation, guaranteed raw-variance monotonicity, whole-field consensus, or an H-off trajectory.
3. **SIM04 fusion centroid identity.** Preserve the positive-resonance assumption, absolute-value caveat and source offset. Explain the near-zero mean displacement of this stage without claiming a physical conservation law for the complete update.
4. **Infinity component-uniformity preservation.** For a locally closed group with nonempty neighbor rows and identical R and D across members, show the common two-field update from the accepted review. Explain why internal geometry can change without breaking exact agreement under these conditions. The replay is near this set, not exactly on it; do not claim convergence, eternal closure or an exact reduction of the full moving-point system.

Use the accepted derivations and their actual indexing. Expanded explanatory proofs are welcome; new unreviewed theorems, strengthened generalizations and speculative laws are outside this manuscript assignment.

### G. Comparison, interpretation and limits

Use one precise comparison table for the shared construction and differences. Explain why these two models belong in one comparative paper without asserting that one is a verified chronological successor, an equivalent system, or a controlled experiment differing only by D.

Their initial X draws agree, but initial R range, additional D draws/random-stream consumption, noise schedule, H normalization and observer staging differ. Similar component identities do not isolate a cause. Stage-contribution measurements along one trajectory are not ablations.

Mention Volume I only to orient the reader. Tower II, other March variants, January fixed-grid work, the complex-linear operator, URF and the physics/memory kernels are outside the paper's substantive claims. A brief source-supported context paragraph is sufficient; do not insert their theorems or unfinished studies.

End with what is now understood, what remains unresolved and a bounded future-work paragraph. Do not present a long new experimental program as necessary to finish this paper.

## 5. Findings that must not be lost during synthesis

These are accepted evidence-backed content, not suggestions to recompute:

- SIM04: contraction and narrower amplitudes coexist with separation of the local graph. The six-point group is the final bottom six in resonance, remains connected internally and is compact; high amplitude is not a synonym for organization.
- SIM04: the six-point group shrinks and deforms. Normalized identity-preserving pair distances change, while all three covariance directions retain positive spread. Six points and a complete graph do not establish a named solid.
- SIM04: the normalized averaging deduction, group-level variance decomposition, ranking/motion distinction and centroid identity are part of the accepted review, not merely optional commentary.
- Infinity: final groups contain 11, 13, 10, 10 and 6 distinct points. Membership persists from pass 33 through 200 in the recorded replay, without implying fixed internal neighbor selections or infinite-time persistence.
- Infinity: the 238 endpoint echoes are exactly all internal unordered pairs of those five groups: 55+78+45+45+15. Pair-mask agreement, not only equality of totals, supports the interpretation. The historical aggregate number alone does not recover the partition.
- Infinity: the 44 final candidates are precisely the complement of the six-point low-R group. All points pass the curvature condition; the R cutoff excludes six. These are candidate points in four groups, not 44 separate bodies.
- Infinity: D remains positive and nonzero; three lower clipping events raise its small positive magnitude to the floor. Independent compression is not winner-takes-all competition between the fields.
- Infinity: continued motion, continuing cross-coupling and late near-uniformity within groups are compatible. The tiny endpoint differences defining the highest-R identity are not a leadership variable in the update.
- Both models: all points retain their identities and all local groups remain linked through the source's global center term. Geometry feeds interactions and interactions modify subsequent geometry, but this is not established as a unique or universal definition of all SRG.

Do not claim a polyhedron, phase orthogonality, dark matter, condensate, gravitational law, physical energy conservation, causal path inheritance or derivation of the master constant unless the scoped accepted sources actually establish it. They do not establish those identifications here. Retain historical terminology as quoted terminology with an operational definition.

## 6. Figures and source-linked claims

Reuse the accepted four SIM04 figures, its GPT six-point figure, and the relevant seven SIM05 figures, including the SIM04 geometry companion. Select and arrange rather than include every image reflexively. A conceptual flow schematic is optional and must be visibly conceptual, not a new scientific result.

Each caption must identify model, data origin, run/pass window, selected IDs where relevant, coordinate scaling/normalization, metric or observer timing, and the exact supported conclusion. Keep fixed scales or clearly disclose changes; use equal spatial aspect ratios. Avoid interpreting late marker overlap as merger. Preserve source image bytes when copying; any presentational derivative must have its input and change recorded.

Use source-relative links and normal manuscript citations/equation references, not chat-only citation tokens or personal Windows paths as the reader's only evidence access. A concise claim-evidence matrix must map each main quantitative or mathematical claim to source lines, saved output location or reviewed derivation, plus its evidence class and limitation. Reuse existing bibliography entries only after checking them in the supplied material; do not invent citations or launch an unrelated literature search.

Apply the accepted SIM04 source-locator corrections in the new manuscript only. Do not rewrite sealed study documents. Do not repeat its overstatement that a nested historical delivery receipt is included: the earlier packaging omission and the independently resolved Volume I publication receipt are distinct facts. Keep publication administration out of the scientific main text.

## 7. Deliverables

Return one clearly named review ZIP and a separately accessible PDF, containing:

1. `manuscript.pdf` and editable `manuscript.tex`, with bibliography, figure assets and a short build instruction.
2. `START_HERE.md`: plain-language synopsis, manuscript reading route, principal results, exact candidate status and any unresolved editorial issue.
3. `CLAIM_EVIDENCE_MATRIX.md` and `FIGURE_REGISTER.json`: a compact navigable record of evidence, assumptions and inputs.
4. `EDITORIAL_AND_VERIFICATION_NOTES.md`: how both accepted reviews were incorporated, retained numerical results, document checks and any discrepancies. Clearly separate old scientific checks from checks performed for this draft.
5. Necessary unchanged evidence or immutable input archives with a usable relative index. The review must not require access to an untracked Windows directory to substantiate its main claims.
6. A scoped manifest and preservation receipt for the delivered candidate and the accepted inputs actually used.

Do not include cache files, temporary page renders, duplicate builds or unrelated research in the final ZIP. Keep working renders locally for page inspection.

## 8. Completion gate and stop

Before returning, inspect every rendered manuscript page for legibility, clipping, equations, tables, captions and references. Check that every main claim has an evidence locator, every proposition states its conditions, the two recurrences remain distinct, and the paper distinguishes historical evidence from the replay throughout. Confirm that no scientific script or state update was run and that no existing protected file was changed.

The draft should let a reader reconstruct each algorithm on paper without guessing its stage order and understand the observed behavior without memorizing internal project codes. It should explain the results positively, not merely list what they fail to prove.

**STOP after delivering the manuscript for GPT and Hilmir review.** Do not start Tower II, a new numerical question, publication preparation or a Git action. The next decision follows review of this paper, not an automatic expansion of scope.
