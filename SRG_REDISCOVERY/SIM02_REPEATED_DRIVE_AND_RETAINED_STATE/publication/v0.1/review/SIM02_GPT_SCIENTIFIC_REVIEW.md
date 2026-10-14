# SRG-SIM02 — GPT scientific review

**Review date:** 14 October 2026  
**Submission:** Codex, *SRG-SIM02: repeated driving renews motion while the carried state continues to change*  
**Verdict:** **ACCEPTED_WITHIN_BOUNDED_PAIRED_CONTINUATION_SCOPE**  
**Required scientific, source or report revisions:** **None**  
**New rollout updates performed by this review:** **Zero**

> The driving waveform returned, but the labeled dynamical state did not. Between the two arms, the same realized draws and bit history accompanied substantially different motion under the different clock schedules.

## 1. Decision and accepted result

SIM02 answers its declared finite experimental question using the existing C operator. Both arms inherit the same accepted S_200 and complete RNG checkpoint. CONTINUOUS supplies frames 200 through 999; REPEATED supplies four further passes through frames 0 through 199. Positions, velocities, bits and RNG are carried forward. No replacement engine, force definition, additional seed or state-reset control was introduced.

The accepted findings are renewed speed responses in REPEATED, progressively lower block-average speeds in CONTINUOUS, changing same-phase labeled states within REPEATED, and exact cross-arm agreement of draw values, their update/center assignments, retained bits and boundary RNG checkpoints. These are findings for one paired continuation, not population statistics or an asymptotic classification.

The reported execution is 1,604 started and completed source calls: four disposable preflight calls and 800 new updates in each arm. The inherited 200 updates are not rerun or counted as two independent observations. Both arms end at S_1000, after update index 999.

## 2. What I independently checked

### Submission identity and source preservation

The uploaded archive is **4,244,315 bytes**, SHA-256:

`bd722daf23dccc336d53bf59ae96ad5f65ee0706a1fba61380e4d113316af2e0`

CRC, safe paths, duplicate names, case collisions and extracted-byte identities pass. All **121 manifested payloads** match their sizes and hashes; the **122nd member** is the manifest. The extracted archive payload totals 9,664,825 bytes. The report is 17,601 bytes, SHA-256:

`caba12187e8498220d6cecef7cd2cd9063a65a53f0706b236de67fe64925e787`

All nine independently pinned accepted artifacts match their work-order anchors and the retained publication manifest. All ten copied accepted inputs match the submitted before/after identities. The embedded work order is byte-identical to the separately available issued work order. The frozen experiment specification and five frozen implementation/analysis scripts retain their recorded identities.

I read original C, the unchanged accepted detached C and observation API, and the SIM02 preparation, restoration, worker, supervisor, analysis and closeout code. The new worker uses the existing operator; its comparison against CONTINUOUS is an assertion, not a mechanism for forcing REPEATED's draws or bits to match. The separate processes restore the pristine branch, not a disposable preflight successor. No boundary reset or reseed is present in the continuation loop.

The accepted NPZ stores int8 bits, whereas native C uses dtype=int. The validated lossless widening to int64 on this Windows execution is appropriate; source and accepted checkpoint bytes remain unchanged.

### Independent saved-transition and RNG checks

`review_sim02_saved_evidence.py` is reviewer-written. It does not import any submitted engine, API, worker, supervisor or analysis module. Each scratch calculation starts from its recorded predecessor, evaluates one source-form successor using the recorded draws, and compares with the saved successor. No calculated successor becomes the predecessor of another evaluation.

The review checked **all 1,600 new continuation transitions** and **four saved preflight transitions**, with **zero inherited SIM01 transition evaluations** and **zero rollout updates**. The preflight pair successors are byte-identical within each observed/unobserved pair; full RNG checkpoints and sequential before/after snapshots agree with the stated execution.

| Saved transitions | Count | Maximum position residual | Maximum velocity residual | Maximum H residual |
|---|---:|---:|---:|---:|
| CONTINUOUS continuation | 800 | 0 | 1.735e-18 | 4.337e-19 |
| REPEATED continuation | 800 | 3.470e-18 | 1.111e-16 | 4.441e-16 |

Residuals in this table are rounded upward. Incoming G and source-energy residuals are zero. Full precision, including preflight residuals, is in `INDEPENDENT_REVIEW_RESULTS.json`. The review used absolute tolerance 1e-13 for cross-environment arithmetic checks, not exact-real equality. Reviewer environment: Python 3.13.5 / NumPy 2.3.5. Submission environment: Python 3.11.15 / NumPy 2.4.4.

RNG replay was separate from motion. Isolated reviewer RandomState objects reproduced 6,400 scalar values per arm and eight values per preflight fixture: **12,832 reviewer RNG values**, none supplied to a new model rollout. The accepted 1,600-draw prefix was not regenerated. Complete checkpoint verification includes the 624 keys, internal position and Gaussian-cache fields, at S_200, S_400, S_600, S_800 and S_1000 for each arm, plus each preflight's post-call checkpoint.

The checks also cover all 1,600 returned-state journal rows, all 12,800 new rollout draw-stream rows, branch/boundary state signatures, frame schedules, draw masks and offsets, bit transitions, energy, raw/minimal displacements, detector values and the lift consistency checks.

### Analysis and figure checks

All 57 arrays in `analysis/comparison_arrays.npz` were independently reconstructed from saved data. The maximum comparison-array residual is recorded in the result JSON. All eight analysis CSV files were checked across the two reviewer scripts; the supplementary script performs only saved-array readouts, with no transition evaluations or RNG draws. I visually inspected all six supplied figures, including their legends, inherited-prefix markings, cycle boundaries and incoming/post-update index conventions. No figure or report correction is required.

## 3. The strongest matched comparison

The draw gate remained open in both arms for all 800 new updates. Each therefore consumed eight scalar draws per update, in the same center order, from the same initial checkpoint. All 6,400 cross-arm value pairs and their update/center assignments match exactly. Each arm underwent the same 75 new toggles, and their complete bit histories agree. Their final bits are `[0,1,0,1,0,1,0,0]`.

Nevertheless, positions and velocities first differ at **S_201**, immediately following the first changed clock input. At that update the shared incoming G is 0.9853316764949968, while H is 0.002636728742286805 in CONTINUOUS and 4.5 in REPEATED. The intervention changes H; subsequent changes to geometry, velocities and G are consequences of the coupled evolution.

**Additional reviewer observation, not attributed to Codex's report:** the first new toggle is later, at **update 202, center 1**, producing **S_203**. Neither update 200 nor 201 toggles any bit in either arm. Thus the trajectory divergence begins before the first new sign-switch event. This was read from the accepted new arrays, with no new motion. `ADDITIONAL_READOUTS.json` records it.

The appropriate conclusion is that random-stream or sign-switch-history mismatch does not explain this cross-arm difference. It is a schedule-dependent effect in the unchanged system, conditional on this initial state and realized native stream. This does not remove the stochastic rule from C or establish that its influence is irrelevant in other realizations.

## 4. Size and form of the response

| New 200-update block | CONTINUOUS mean speed | REPEATED mean speed |
|---|---:|---:|
| Updates 200–399 | 0.008811537 | 0.103946551 |
| Updates 400–599 | 0.004189443 | 0.098578750 |
| Updates 600–799 | 0.002796353 | 0.105028978 |
| Updates 800–999 | 0.002105524 | 0.100533001 |

These are averages of post-update mean speeds, not mean vector velocities. The inherited block is excluded from this table.

At S_1000, mean speeds are 0.00186863975472 and 0.0151286038860. **Reviewer-calculated endpoint ratio: 8.09605.** Averaging all 800 new post-update responses instead gives 0.00447571433016 and 0.102021819974, a **reviewer-calculated ratio of 22.79453**. The latter includes the renewed pulses, whereas the endpoint samples the weak-driving end of a cycle. Neither ratio is a physical efficiency or statistical performance measure.

REPEATED's four new speed peaks are approximately 0.5364, 0.5531, 0.5565 and 0.5672. Its five phase-aligned speed curves, including the inherited curve, exhibit similar but not identical envelopes. This descriptive similarity is visible in `plots/04_repeated_speed.png`; no synchronization theorem or convergence fit is asserted.

The labeled-center mean periodic distance between the arms at successive new boundaries is 1.27674, 1.82510, 2.53453 and 2.85106. At S_1000 the maximum corresponding-center distance is 6.57355. This is a toroidal labeled-position comparison, not a rotation/permutation-invariant shape comparison.

## 5. Source-derived explanation for similar speed envelopes and different configurations

This paragraph is a reviewer derivation from the inspected update, not a new empirical experiment.

Let d_i be C's sequentially evaluated minimal-image displacement toward the current arithmetic centroid, and let s_i be its selected sign, +1 or -1. The increment added to velocity **before damping** has mathematical form

\[
\delta v_i=0.1\,G\,H(t)\,s_i\frac{d_i}{\|d_i\|+0.01}.
\]

Consequently, in the real-valued interpretation of the source expressions,

\[
\|\delta v_i\|=0.1\,G\,|H(t)|\frac{\|d_i\|}{\|d_i\|+0.01}.
\]

The sign bit reverses this increment but does not alter its norm when d_i, G and H are fixed. When the distance is large compared with 0.01, normalization also makes the increment magnitude weakly dependent on that distance. Repeating H can therefore impose a recognizable magnitude envelope while the directions and configurations differ.

This identity concerns the pre-damping increment, not the norm of the complete successor velocity. Retained velocity is added, damping acts componentwise, G depends on incoming speed, and the sequential geometry changes. Those features prevent an inference that the output speeds must agree or that geometry and bits do not matter. The useful distinction is simply **similar scalar response does not require the same dynamical state**.

## 6. What the same-phase comparison establishes

The requested comparison sets contain eight rows of cycle pairs but seven unique pairs, because (1,0) occurs in both sets. At 200 phases per pair, that is **1,400 unique same-phase comparisons**, not 1,600 independent observations.

No tested phase pair has exact equality of positions, velocities or the bit vector. No pair meets the declared near-repeat rule: position mean and maximum residuals <=1e-12, velocity mean and maximum residuals <=1e-12, with bits equal. The minimum phasewise mean position differences for the four successive-cycle pairs are approximately 0.96069, 0.72406, 1.12204 and 1.10393. These failures are not merely residuals just above a numerical cutoff.

The result is restricted to the tested pair sets, labeled centers, five recorded cycles and this diagnostic tolerance. It is not an exhaustive all-lag recurrence search, a quotient-space shape classification, or a proof of nonrecurrence for all future times.

Equal cross-arm draws at equal actual updates must not be confused with equal draws across different cycles at equal driving phase. Within REPEATED, the random stream keeps advancing, and bits and geometry continue changing. This design does not separately identify their cycle-to-cycle causal contributions or demonstrate learned memory. It does establish that restarting the driving waveform is not the same as restarting the recorded state.

## 7. Observer and preservation boundaries

The legacy displacement detector remains an observer, not a force or transition rule. The new CONTINUOUS and REPEATED records have 6,400 and 5,511 legacy flags respectively, but zero minimal-image steps above length 1. Genuine coordinate-wrap body-updates number 0 and 27. Maximum minimal-image step norms are approximately 0.00201864 and 0.06080875. The maximum lift consistency residual is 1.341e-15, below the specified 1e-12 tolerance, and every component increment is below half the box. No physical teleportation or unwrapped evolving state follows.

Submitted before/after receipts agree for all ten protected unrelated modified files, accepted inputs, HEAD, tracked status, Git-index bytes and index entries. The frozen scripts and supplied logs support the claimed call accounting and resource caps. **I reviewed the submission, not the author's live Windows filesystem or an independently observed execution.**

The post-archive `SIM02_TRANSPORT_SEAL.json` is deliberately external to the ZIP and was not uploaded here. I independently verified the received archive and every contained payload; the missing external seal does not block scientific acceptance. The exact final local aggregate including excluded caches, temporary files and that external seal is not independently inspected by this review. The recorded process limits pass, and the received archive and extracted payload are each far below the cap. No rerun is requested to address this evidence boundary.

## 8. Disposition

**SIM02 is scientifically complete within its bounded paired-continuation scope. No required revisions remain.** Preserve the submitted report, figures, state arrays and execution evidence unchanged, together with this review. The new first-toggle observation and explanatory norm identity belong to the reviewer record; they do not require rewriting Codex's accepted report.

The next administrative step is a bounded publication preparation using the already established research-edition practice. This review is not permission to commit, push, change licensing, run more cycles, add controls or begin SIM03. No new experiment is necessary to accept or explain this result. Preserve SIM02 before moving to another research phase.

## 9. Review files and passive reproduction

This separate reviewer package contains this decision, two independent checking/readout scripts, their two result files, the archive review and a manifest covering the other six files. It does not duplicate or modify the 122-member submission.

To reproduce the **passive review only**, extract the original SIM02 submission without changing it, keep the original ZIP, and choose a separate output directory. Windows CMD:

```bat
conda activate torment
python -B "<review directory>\review_sim02_saved_evidence.py" --bundle-root "<extracted SIM02 submission>" --archive "<original SIM02_GPT_REVIEW.zip>" --output-dir "<separate review output>"
python -B "<review directory>\review_sim02_readouts.py" --bundle-root "<extracted SIM02 submission>" --output-dir "<separate review output>"
```

These are independent reviewer commands, not instructions to rerun SIM02's exhausted workers. The first performs recorded-transition evaluations and isolated RNG verification; the second reads saved arrays only.

**Submission-relative source basis:** `SIM02_REPORT.md`; `EXPERIMENT_SPEC.json`; `inputs/sources/source_C.py`; `inputs/detached/engine_C.py`; `inputs/engine_api.py`; `prepare.py`; `support.py`; `worker.py`; `supervise.py`; `analysis/analyze.py`; `closeout.py`; `runs/*/states.npz`, journals, draw streams and RNG checkpoints; `analysis/RESULTS.json`, comparison arrays and CSVs; `evidence/*`; the six supplied plots. The pinned SIM01 work order and copied accepted inputs establish the inherited checkpoint and source identity. Reviewer-derived observations are explicitly identified above.
