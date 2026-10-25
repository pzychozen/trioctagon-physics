# SIM06 — Tower II construction and saved-behavior review

**Date:** 24 October 2026  
**Author and research director:** Hilmir Frímann Halldórsson  
**Scientific reviewer:** GPT  
**Submitted research engineering:** Codex  
**Disposition:** **ACCEPTED_WITHIN_HISTORICAL_CONSTRUCTION_AND_FIXED_RECORD_SCOPE**  
**Scientific revisions required:** None.  
**Publication status:** Research review only; no publication, ledger change or next-engine execution authorized by this receipt.

## 1. Decision

The Tower II construction study passes review. The five reports accurately connect the complete original program, its selected original aggregate output, the one pre-existing R1 record, and the three new visualizations made from that record. The distinction between permanently assigned bands and changing spatial neighbor groups is both source-supported and numerically verified.

This acceptance covers the selected `GoldenTowerFieldII` configuration and finite saved trajectory. It does not accept every interpretation in the old narrative, recover a missing historical coordinate record, certify the original execution environment, or retroactively accept the separate R3 submission. No new trajectory, mathematical model, revised dynamics or infinite-time result is introduced.

The most useful additional finding from this review is a direct connectivity check: when the local neighbor selections are considered together with the original code's same-band center dependencies, the resulting point-dependency graph is **weakly connected at every one of the 600 inspected incoming boundaries**. Local graph separation therefore does not imply full separation of the implemented interaction structure. This is a new passive description of delivered coordinates and source-defined relationships, not a new simulation or an alteration to the algorithm.

## 2. Inputs and preservation

The original submission is `SRG_SIMULATION_STUDY_06_TOWER_II_CONSTRUCTION_01_REVIEW.zip`:

- Bytes: **7,909,727**.
- SHA-256: `233ad8fc05afc5ffbc766e2862d1c84c5b032a79172da552429a40dee744e6a7`.
- **74 files:** 73 manifested payloads and `MANIFEST.json`.
- ZIP CRC check passes; every payload's size and SHA-256 matches; no missing or unexplained payload is present.

The [unchanged extracted submission](source_package/START_HERE.md) accompanies this review. Its 43 input copies match the submitted baseline. All 17 delivered R1 files match the retained R1 payload manifest. Six used inputs additionally match byte streams in the previously supplied SIM06 handoff, including the work order and retained R0/R1/R3 context. The standalone uploaded starting guide equals the archived guide.

The original Tower II source is **34,980 bytes**, 842 lines, SHA-256 `147a32be3b6d6aad17ada6ab7be2fbc3994c3363f74d6a2b351fb8eecda80304`. Its identity agrees with the authorized work order. After its eight-line prefix, the R0 audited excerpt has exactly the line content of original lines 31–254; class ASTs also agree. CRLF versus LF prevents calling the excerpt a raw-byte substring; the report correctly distinguishes that.

The old archive locator being absent does not create a source-identity gap here: the recovered R0 copy has the prescribed identity. This review does not independently access the user's Windows checkout. The claim that all 43 live original paths stayed unchanged is Codex's before/after preservation attestation; the matching delivered copies and baselines are what GPT directly verified. Hashes alone cannot establish that no program executed.

All 74 extracted submission files were hashed before and after this review and remained unchanged. Neither their source, figures nor reports were edited.

## 3. What was independently checked

The original 842-line file, the five reports, entry guide, record-selection account, passive inspection and rendering code, figure register, manifests and relevant prior records were read. The copied original simulator, audited core, submitted inspection scripts and earlier scientific checkers were **not imported or run**.

A separately written [passive reviewer](independent_review.py) read the fixed numerical arrays with `allow_pickle=False` and read-only memory mapping. No state constructor, update, noise generation, RNG restoration/draw or spectral audit was used. No calculated successor was propagated. The checks below describe the delivered records; they are not a fresh recurrence-equivalence experiment.

| Check | Result |
|---|---|
| Input record schema | 601 X/V/R boundaries, states 0–600; 80 persistent rows per boundary; **48,080 point-state records** |
| Array finiteness | All 11 delivered numerical arrays finite |
| Band configuration | Four fixed bands of 20 IDs; one fixed stored frequency per band |
| Displacement identity | **144,000 V components** exactly equal successive saved X differences; initial V is zero |
| Recorded compressor output | `actual_rpc_output` exactly equals `R[1:]` |
| Saved positional decomposition | `positions_at_rpc + noise` exactly equals `X[1:]`, using delivered noise only |
| Whole-field descriptions | All **601** rows agree with independent fixed-state geometry/observer calculations |
| Band descriptions | All **2,404** band rows agree |
| Selected IDs | All **1,803** rows for IDs 4, 8 and 9 agree; their selection is the first three IDs of band 0 |
| Local graph descriptions | All **600** incoming-state graph rows agree: weak/strong counts, same/cross-band selections, and induced within-band graph counts |
| Local selection accounting | **240,000** directed nearest-neighbor selections described; zero self selections and zero fifth/sixth cutoff ties |
| Membership snapshots | All seven supplied component-membership snapshots and all selected-ID neighbor rows agree |
| Lock observer | Recomputed from saved R only: band 2 at pass 3, band 3 at 4, band 1 at 5, band 0 at 7 |
| Original epsilon=1 aggregate | Mean R, mean/std/range of L and surviving-band count agree; no FFT repeated |
| Figures | All three saved PNGs inspected at full delivered size; numeric coordinate limits and declared normalization checked |

The graph reviewer uses broadcast coordinate differences and its own graph traversals, rather than invoking the submitted `pdist`/SciPy graph-analysis sequence. The smallest observed fifth/sixth distance gap is about **3.806 × 10⁻⁸**, and the minimum distance between distinct points is about **2.007 × 10⁻⁴**. The reported graph structure is not resting on a tie at the neighbor cutoff in these records.

Across **32,490** compared descriptive scalar quantities, the maximum absolute discrepancy is **3.553 × 10⁻¹⁵**, consistent with different floating-point evaluation arrangements. This count is verification coverage, not independent statistical trials. The independent spatial-variance decomposition residual is at most **5.552 × 10⁻¹⁵**. The submitted residual uses a reused radius squared and a different evaluation order; its slightly different roundoff value is not a contradiction.

Machine-readable details: [VERIFICATION.json](independent/VERIFICATION.json), [FINDINGS.json](independent/FINDINGS.json), and [input identities](independent/INPUT_IDENTITIES.json).

## 4. Source review: the construction is represented faithfully

### 4.1 The state and initialization

The selected source creates 80 points with positions X and one real scalar R each. It assigns four frequency-band labels, exactly 20 points per label, by shuffling a balanced assignment. Frequencies are **supplied** by `.244 * phi**n`, with indices −2, −1, 0, 1. Labels and assigned frequencies do not evolve in the selected driver. Neither a spatial tower nor a new frequency catalogue is generated by that assignment.

The evolving inputs are positions, resonance, pass number and RNG state, with fixed configuration/labels. Stored V is the completed displacement, not an inertial input. L is recalculated from incoming R; it is not an independent carried oscillator. The selected original driver uses width 2 rather than the constructor default 3, and the report preserves that difference.

Source anchors: original lines 62–109 and 376–398.

### 4.2 Local geometry, local movement and amplitude exchange

Neighbors come from the incoming positions. With no horizon the code sorts a full distance row and takes entries 1–5; it does not explicitly remove self first. The report correctly retains the general coincident-position caveat rather than silently replacing the source selection. All inspected rows in this selected record do select five distinct other IDs.

All local displacements use the same incoming coordinates, then apply together. The position average is not the resonance-weighted inverse-distance average. Amplitude weights combine inverse distance and a log-frequency-ratio preference. The raw-weight guard, sine placement, and additive-mixing ordering are transcribed correctly.

In particular, the additional phi-ratio and sum/difference matches **add** donor-amplitude contributions. They do not create or mutate frequency labels, and they do not subtract a compensating amount from a donor. At a fixed incoming geometry/frequency assignment and pass, these additional expressions are linear in incoming R. This source reading does not make the complete moving system linear, because geometry and weights evolve.

Source anchors: original lines 111–127 and 140–190.

### 4.3 Band-wide fusion is a separate relationship

After local movement and H modulation, the source calculates one weighted center for each band:

\[
c_b=\frac{\sum_{i\in I_b} (|Q_i|+10^{-8})Y_i}{\sum_{i\in I_b}(|Q_i|+10^{-8})},
\qquad
Z_i=Y_i+0.02Q_i(c_b-Y_i).
\]

That center uses **every member of the band**, not just the current five neighbors. It is computed once for that band before the inner displacement loop. Bands are disjoint, so this is not a continuously recomputed whole-field centroid and not Infinity's one-global-center stage. A horizon in the optional local-neighbor routine would not by itself restrict this band-wide stage.

The weight uses absolute Q, while the displacement coefficient uses signed Q. The descriptive inward-pull interpretation is appropriate to the positive inspected path, not to every possible input. Singleton bands skip the stage; the selected bands all contain 20 points.

Source anchors: original lines 192–209. This review accepts the transcription; it did not run a fusion or recurrence oracle.

### 4.4 Observers are not instructions

First lock means the first recorded crossing of a coherence threshold together with a mean-amplitude threshold. No state update reads that lock-time label. Survival is a count of qualifying bands, not deletion or persistence of a newly created entity. GRF is a reciprocal-displacement observer, not an extra force in the selected core.

The source's five drivers are correctly mapped as separate experiments. Reading the other drivers does not validate their reported outcomes or authorize running them. The master-equation driver's zeta-based expression is computed after evolution; it does not enter this class's recurrence. The supplied frequency preferences, by contrast, do enter the recurrence. These are distinct uses of mathematical expressions in the historical file.

Source anchors: original lines 218–254, 262–368, 480–588, 596–744 and 752–842.

## 5. The key behavior: two kinds of membership

The strongest descriptive result is that **assigned band membership and local graph membership do not coincide**.

At saved state 20, the six weak local components have sizes **14, 6, 10, 8, 10 and 32**. Every component contains at least one member of every assigned band. A band color is therefore not a spatial component label.

At state 200, the local graph has nine weak components. Band 0 also has nine pieces in its induced local graph, while all 20 band-0 points still contribute to the single band-0 fusion center. Of 400 local selections at that boundary, 138 are same-band and 262 are cross-band. State 200 is the endpoint of the historical-configuration comparison window; its graph is also the incoming graph for the already recorded extension pass 201, not evidence of an extra historical pass.

At incoming boundary **599**, which drives recorded pass **600**, the local graph has three weak components:

| Local component size | Band 0 | Band 1 | Band 2 | Band 3 | Band-0 IDs in the component |
|---:|---:|---:|---:|---:|---|
| 41 | 1 | 20 | 0 | 20 | 62 |
| 22 | 2 | 0 | 20 | 0 | 25, 74 |
| 17 | 17 | 0 | 0 | 0 | 4, 8, 9, 11, 12, 15, 17, 18, 20, 31, 34, 45, 55, 57, 66, 67, 70 |

Thus all of bands 1 and 3 share one local component, all of band 2 lies in another, and band 0 spans all three. At this boundary 353 selections are same-band, but 47 remain cross-band. There is no claim here about a graph used by an unrecorded update 601.

The same source rule explains why local disconnection does not eliminate interaction: every band-0 member still contributes to its shared center. No new connecting force was introduced by the reconstruction.

### Additional passive finding: combined dependencies remain weakly connected

For each incoming boundary 0–599, the reviewer formed an **analysis-only** graph consisting of (a) the actual local selections and (b) all ordered distinct pairs of members of the same band, representing their shared-center dependencies. This does not replace the recurrence, add edges to the simulator, or claim that the fusion stage is a new physical pair force.

This union has **one weak component at all 600 inspected boundaries**. Its strong-component count ranges from 1 to 3, and is 2 at boundary 599. Therefore the valid statement is weak connectivity—connectivity when arrow direction is ignored—not universal two-way directed reachability.

This graph is a structural description of source dependencies, not a complete state-variable Jacobian or a measurement of influence magnitude. It proves neither physical signal transmission, synchronization, effective numerical sensitivity at every edge, nor persistence beyond the inspected record.

The new table is [combined_dependency_graph.csv](independent/combined_dependency_graph.csv). At boundary 599, the three band-0 subsets in the table above give a particularly direct explanation of the weak bridge between the three local components.

## 6. Contraction does not mean four spatial components or stopped motion

The radius of gyration measures typical distance from the arithmetic whole-field center. The submitted descriptive radii reproduce:

| Saved state | Whole-field radius | Band-0 radius | Mean completed displacement | Evidence window |
|---:|---:|---:|---:|---|
| 0 | 5.261566081 | 5.114513940 | 0, initialized | Initial reproduced state |
| 20 | 4.292701509 | 4.217704510 | 0.0559531333 | Historical-configuration comparison |
| 200 | 1.352830056 | 1.289887749 | 0.0144031669 | Comparison endpoint |
| 600 | 0.0549954406 | 0.0174950920 | 0.00252415096 | Later R1 extension |

The whole-field radius is 74.29% smaller at state 200 than at initialization, and 98.95% smaller at state 600. These are finite endpoint comparisons, not a monotonicity or convergence theorem.

The accepted decomposition is a measurement identity:

\[
R_g^2=W+B,
\]

where W is the point-count-weighted within-band spatial variance and B is the variance of the arithmetic band centers. These centers are descriptive quantities, not the amplitude-weighted fusion centers.

The between-center share is approximately **3.78%** initially, **6.66%** at state 200 and **96.65%** at state 600. Both within-band variance and between-center variance have decreased in absolute magnitude. The late dominance of B means that the now very small remaining spread is mostly between compact band centers; it does **not** mean the centers have been moving farther apart.

In the extension, band-0 radius decreases about **73.73-fold** from state 200 to 600, while its center shifts only about 0.096678 between those endpoints. That is why center translation and internal concentration need separate descriptions. Source-defined band affiliation is not interchangeable with a nearest-neighbor component even when the bands are compact.

The last 100 completed updates retain nonzero mean displacements; at pass 600 the maximum individual displacement is approximately **0.00468384019**. Marker overlap on the fixed world view does not mean deletion, merger of IDs or an exact fixed point.

## 7. Lock timing and breathing: the useful historical corrections

### Lock timing

The saved amplitudes independently reproduce first locks at passes 3, 4, 5 and 7 for bands 2, 3, 1 and 0. The first weak local-graph split occurs only at saved state 10. All four bands therefore register their source-defined lock **before** that first spatial-graph separation, and before later contraction is complete.

This is a concrete distinction between amplitude coherence and geometry. The first-lock record is not a stop instruction or evidence that each label has become a compact isolated body.

### Breathing

The implementation overwrites the bound at pass p from the incoming amplitudes:

\[
L_p=9\bigl(1+\operatorname{mean}|R_{p-1}|\bigr)
\]

for the selected epsilon=1 case. It is a log-amplitude clipping limit, not a spatial wall, a coordinate scale, or an independent second field. It can matter to later evolution when clipping is effective; the source design is not generally inert.

The **retained R1 result**, not a newly executed control here, is that clipping was inactive and enabled/disabled paired trajectories agreed for its tested settings. The selected delivered diagnostics record zero clipping events throughout. This review checked the affine incoming-state readout against saved R but did not rerun a compressor audit or paired control.

The historical source's spectral window contains 150 samples after dropping the first 50 L values. Its recorded dominant frequency is 1/150 cycles/pass. The retained R1 audit demonstrates first-bin tracking across changed window lengths and the insufficiency of the old 1% test. In exact mean-zero arithmetic, the largest of 75 non-DC powers is at least 1/75 of their total, already greater than 1%; that retained argument explains why the source flag cannot by itself discriminate an oscillator from a nonconstant trend. This is not a new spectral result or a universal denial of oscillation in SRG.

The present package properly corrects the historical narrative without editing the original source or original note.

## 8. Original versus reproduced evidence remains separated

The original seven-row CSV is aggregate evidence. For the epsilon=1 row, independent passive comparison with the selected records gives:

| Quantity | Existing-record value |
|---|---:|
| State-200 mean absolute R | 0.5489832686504329 |
| Mean L over passes 1–200 | 11.905260171214326 |
| Population standard deviation of L | 0.9892193445854100 |
| Range of L | 3.5626358780586127 |
| Surviving bands | 4 |

The historical values agree; the standard-deviation difference is only final-rounding scale. The frequency/oscillation columns were read and interpreted from the prior audit, not freshly recalculated.

The 601 point-level boundaries are an **existing later R1 reproduction**. States 0–200 use the historical setting; states 201–600 are R1's longer continuation. Neither close aggregate agreement nor matching a recovered source hash certifies missing historical coordinates or a lost historical execution environment. The reports and figures consistently respect this boundary.

The R2 context tables identify epsilon=0. The study correctly discloses that using their initial summary alongside epsilon=1 relies on R1's prior paired equality. The reviewer independently recovered the initial radius/mean directly from the selected arrays, so those displayed starting values also have a direct saved-array check.

The retained R3 report explicitly returns its own work for GPT review. SIM06 correctly retains that qualification. This acceptance does not silently promote R3's separate control results or theorem package to a new accepted stage.

## 9. Figure and document review

All three PNGs were opened and inspected at their delivered pixel sizes. No clipping, unreadable legend, hidden plotting-scale change or blocking label collision was found.

- **F01:** six snapshots use fixed ±5.5 spatial limits and equal aspect. The labels distinguish the comparison window from the extension. The absence of resolved late points on this large scale is correctly qualified as marker overlap.
- **F02:** the upper panels center band 0 and divide by its own instantaneous radius; the actual radius is printed. All plotted coordinates fit the declared common normalized limits. The lower three-ID views use different but declared world-coordinate spans, equal axis aspect, saved-point markers and endpoint conventions. The connecting lines are reading guides, not integration or interpolated trajectories. This is the most immediately useful figure for seeing the distinction between movement and within-band concentration.
- **F03:** the two length contributions are square roots of variances; the caption correctly says their **squares**, not radii, add. The L-versus-R panel discloses two axes and the incoming/outgoing offset. Graphs use incoming states 0–599, and completed displacement curves use passes 1–600. The extension boundary is visible.

One nonblocking packaging observation remains: `RECORD_SELECTION.md` links to `REVIEW_ZIP_IDENTITY.json`, which it also identifies as an **external** final-ZIP receipt. That receipt is not in the uploaded archive. The included manifest is complete and verified, and this review independently hashes the original ZIP, so no scientific or payload-integrity claim depends on that absent sidecar. When preparing a future self-contained edition, label this as an external-only record or attach it separately. No present scientific revision or rerun is required. The submitted files have not been changed to fix this historical packaging link.

## 10. Reconstruction implications and stopping decision

This study successfully supplies the missing construction-and-behavior account. It adds a genuine source-defined distinction to the family map: a position-dependent local neighbor structure coexists with a fixed-label band-center structure. The geometry follows from both, not from band names alone.

It is now possible to explain how Tower II is related to Seed Explorer and Infinity without claiming that it is merely the same program with different pictures. The local position rule is shared, but frequency-weighted exchange, ordered added mixing, per-band fusion and the optional bound readout are substantive differences. The configurations and durations differ, so comparing outcomes is not a controlled one-factor experiment.

The historical creation map remains appropriately cautious. The original header and narrative preserve stated intentions and dates; neither establishes a complete development chronology. The reconstructed code/evidence chain answers what this program calculated. Missing history should remain explicit rather than replaced by a smooth invented story.

**Decision:** close the SIM06 Tower II construction checkpoint as accepted. No additional Tower II trajectory, correction to the published Volume II, automatic Volume III manuscript or full-study repetition of Tower I is needed to close it.

The remaining variant map identifies two different unresolved operations: Universe/condensate's in-place local fusion, and BreathingField's field-merger initialization/clock/RNG inheritance. Of those, **the local in-place fusion is the next most directly relevant construction question**, because the distinction between a genuine local center and the all-band center is now concrete. This is a recommendation for the next bounded decision, not an execution authorization or a new work order in this review.

The present task stops with the accepted reports, independent review and discussion of the actual saved behavior.

## Review artifacts

- [Independent verification results](independent/VERIFICATION.json).
- [Additional fixed-record findings](independent/FINDINGS.json).
- [Combined local/band dependency counts](independent/combined_dependency_graph.csv).
- [Independent passive review method](independent_review.py).
- [Source and record input identities](independent/INPUT_IDENTITIES.json).
- [Submitted construction](source_package/CONSTRUCTION.md), [evidence account](source_package/ORIGINAL_EVIDENCE_AND_EXISTING_REPLAY.md), [motion/geometry](source_package/MOTION_AND_GEOMETRY.md), [relationships](source_package/MODEL_RELATIONSHIPS.md), [record selection](source_package/RECORD_SELECTION.md).

**Review execution boundary:** zero new simulation/state updates; zero RNG draws; zero historical or submitted scientific-script executions; zero new scientific figures; zero Git, kernel, ledger or publication changes. The review performs source reading, hashing, descriptive fixed-record calculations and inspection of existing figures only.
