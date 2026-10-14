# SRG-SIM01 — GPT scientific review

**Review date:** 14 October 2026  
**Reviewed submission:** Codex, *SRG-SIM01 — Surviving recursive motion simulations*, 13 October 2026  
**Verdict:** **ACCEPTED_WITHIN_BOUNDED_SOURCE_REPLAY_SCOPE**  
**Required report or source revisions:** **None**  
**Research-base decision:** Select historical engine C (`plot_1.py`) for the next work on this surviving motion family. Retain A and B as references. This does not identify C as the missing June toroidal-topology producer or as the complete historical SRG programme.

## 1. What this review accepts

SIM01 reconstructs and records three existing motion programs without replacing their numerical operations. The accepted findings are finite, source-consistent observations: position and velocity feedback, prescribed forcing, damping, C's stored binary force signs, and the difference between the historical displacement detector and a minimal-image displacement measurement.

The original source semantics matter. A processes three 2D centers sequentially with wrapped pairwise forces. B processes eight 3D centers sequentially toward a repeatedly computed arithmetic centroid of stored wrapped positions. C adds retained binary force signs, toggled by random draws when a common incoming-speed gate is open. The tetrahedron templates are drawing offsets, not independently rotating or deforming bodies. C's rules switch between two predefined options; the program does not write new arbitrary update rules.

The report correctly distinguishes the finite runs from asymptotic attractor claims, and keeps the June constant-seeded topology lineage unresolved. Neither pi*e*phi nor a constant-seeded toroidal-shell construction is inserted into these programs.

## 2. Evidence independently examined

### Archive and submitted identities

The uploaded ZIP is **3,859,173 bytes**, SHA-256:

`a3daf4e915b73a6ec4987647732d322623c5a155b8dab436883e30dacbf6a31f`

Its CRC check passes. All **67 payloads** match the manifest; the 68th member is the manifest itself. There are no unmanifested extra files. The separately uploaded report matches the archived report byte-for-byte, SHA-256:

`0a3f19ff7c0bc45c6665f4a780653dd9681e288bfe0b9016e2cda25d11ed9e48`

The manifest and final-QA hashes match the separately supplied package receipt. The five bundled original source/data copies match their recorded identities. Before/after receipts agree for the eleven selected consumed inputs. The Git status records agree.

**Preservation boundary:** these checks inspect the submitted evidence, not the author's live Windows filesystem. The unchanged listing of ten unrelated tracked modifications is not a bytewise preservation census of those modifications. The report and final-QA record preserve that distinction.

### Source extraction

I read all three original source files, their detached numerical versions, and the extraction, instrumentation, preflight, replay and analysis code. A separate static AST comparison confirms unchanged helper expressions, parameters, initialization draw expressions, and numerical update statements after removing the declared trace calls and metadata returns. Sequential update order, logarithmic damping, wrapping, frozen incoming G and C's draw order are retained.

The six observed/unobserved preflight pairs and twelve calls are present in the receipt. I inspected that evidence and the preflight code; **I did not execute the twelve preflight calls again**.

### Independent passive verification

`review_saved_evidence.py` is a new reviewer-written checker, not an invocation of Codex's detached engines or their runner. Every evaluated transition starts afresh from its recorded predecessor and compares a scratch evaluation with its recorded successor. For C, saved outcome bits are also checked against saved random draws. Random-number generation is replayed separately in an isolated RandomState, without evolving motion.

I checked:

- all **2,700 recorded fresh-run transitions**: A 500, B 2,000, C 200;
- all **1,530 adjacent transitions** in the two historical CSVs, retaining file order and recorded destination frame/bit values;
- original initialization and initial/final RNG checkpoints, including C's complete 1,600-draw sequence;
- stored H/G/energy values, wrapping, unwrapped-coordinate accumulation, source detector flags, minimal-image displacements and bit changes;
- the reported speed and separation endpoints and all five supplied plots.

This is **4,230 passive saved-transition evaluations and zero new rollout updates**. It is not a repeat of the Windows execution, a symbolic theorem count, or an independently recovered RNG history for the old CSVs.

Reviewer environment: Python 3.13.5, NumPy 2.3.5. Submission environment: Python 3.11.15, NumPy 2.4.4. Small cross-environment residuals are expected; the reviewer chose an absolute residual acceptance threshold of 1e-13 for these data, rather than requiring binary equality across environments.

| Record | Transitions checked | Maximum position residual | Maximum velocity residual |
|---|---:|---:|---:|
| A replay | 500 | 0 | 5.56e-17 |
| B replay | 2,000 | 0 | 1.12e-16 |
| C replay | 200 | 2.23e-16 | 1.12e-16 |
| First historical CSV | 1,091 | 8.89e-16 | 1.12e-16 |
| Second historical CSV | 439 | 4.45e-16 | 1.12e-16 |

Displayed residuals are rounded upward. The largest H residual is 4.45e-16 (rounded upward); G and source-energy residuals are zero in these comparisons. Full precision is retained in `INDEPENDENT_REVIEW_RESULTS.json`. These finite floating-point residuals support implementation consistency, not exact-real equality.

## 3. The real stateful mechanism in C

C has a genuine feedback loop:

**stored positions and velocities -> centroid and incoming speed gain -> gated stored sign changes -> force and damping -> updated positions and velocities.**

The gain is

\[
G=\frac{1}{1+\frac18\sum_i\|v_i\|}.
\]

It is frozen once per complete update. Its source function's position/time arguments do not enter this value. C then applies the source force-sign multiplier selected by its retained bit.

The submitted run contains **14 bit changes in 1,600 actual draws**, with final bits `[0,1,0,0,1,1,0,1]`. The full random sequence and checkpoints match in the independent passive RNG check.

The gate stayed open for all 200 updates: the source has state-dependent eligibility, but this particular trajectory does not demonstrate repeated opening and closing of that gate. Its sign changes were produced by the random draws while the gate was open. H itself is a prescribed clock function, not an independently evolving memory state.

This is enough to select C as a concrete existing research base. It does not require a new engine or a new physical interpretation.

## 4. The displacement discrepancy is resolved at the observer level

The unchanged source detector computes

\[
J_i=\|(p_i^+-p_i)\bmod10\|,
\]

then tests whether J_i exceeds 1. A minimal-image displacement instead uses

\[
\Delta_i=((p_i^+-p_i+5)\bmod10)-5.
\]

For example, the coordinate change `(-0.001,0,0)` becomes `(9.999,0,0)` under the source detector. Its minimal-image length is 0.001. The detector can therefore report a large jump for a very small movement in a negative coordinate direction, without a boundary crossing.

| Record | Source detector flags | Minimal-image displacements > 1 | Maximum minimal-image step |
|---|---:|---:|---:|
| C replay | 1,509 | 0 | 0.0609975449 |
| First historical CSV | 8,151 | 0 | 0.0615319416 |
| Second historical CSV | 3,129 | 0 | 0.0603808265 |

The seven wrapping crossings in the C replay are another distinct count. The state transition remains unchanged by either readout. No correction to an original file is needed for this accepted historical reconstruction: retain the legacy observer and the correctly identified passive comparison side by side.

The C trajectory figure makes the distinction readable: the wrapped plot breaks at crossings, while the displacement-accumulated plot follows the same recorded motion without artificial box-wide connecting segments. Its unwrapped coordinates are accounting data, not extra evolving state.

## 5. Additional reviewer calculation: compare B and C on the same 200-update prefix

**This is a new passive comparison by GPT, not a result attributed to Codex's completed report, and not a new simulation.** The report correctly cautions against treating the different full-duration baselines as a matched experiment. I instead aligned B's first 200 recorded updates with all 200 C updates.

The stored initial positions and velocities are bitwise equal. The supplied frame sequence, DT and H values over that common prefix agree. The non-switching parts of the inspected numerical source implement the same force/damping update. The two trajectories are identical through their first update. They first differ at stored state 2, following update index 1, where C first toggles bodies 0 and 6.

| Passive measurement after 200 updates | B | C |
|---|---:|---:|
| Mean minimal-image pair distance | 3.7404453227 | 4.7695105805 |
| Mean speed | 0.0161650372 | 0.0148866862 |

The mean minimal-image distance between corresponding B and C centers at that point is **1.4971661268** coordinate units.

Thus both stored runs slow down, but their spatial arrangements differ substantially on an equal update horizon. The trajectory difference starts at the first sign-switch event, rather than being an artifact of comparing B's 2,000 updates with C's 200.

This comparison concerns one initial condition and one realized switching sequence. It does not isolate each flip's individual effect, establish a statistical advantage, or prove an asymptotic attractor. Subsequent changes to geometry and G are part of the coupled successor dynamics, not independent controls.

## 6. Clocks and finite settling

The historical CSVs contain repeated and decreasing frame labels while state evolution continues. Since the forcing is H(0.1*frame), a frame restart resets the argument of the decaying forcing curve; it is not merely a relabeling of time. The report appropriately distinguishes call order, supplied frame argument and movie playback.

The fresh replays deliberately use each index once. They are source-faithful numerical replays with a declared scheduling choice, not reconstructions of every unknown animation callback invocation in the original save/show sessions.

In B, motion remains measurable late in the run even after H is extremely small. This is consistent with retained velocity and the specified damping; the finite record alone does not establish where the system ultimately settles. No new long-time theorem is asserted here.

## 7. Decision and next boundary

**SIM01 is complete. Select C; keep A and B as reference records. No required mathematical or manuscript corrections were found.** The original detector issue was correctly reported rather than silently repaired.

The immediate project step is to preserve this completed report, its evidence and this review in the GitHub research record before another research phase, following the author's publication-before-continuation rule. This review is not permission to push, change licensing, edit original simulations, or publish the entire private archive.

After that checkpoint, my preferred next experimental question is one concrete source-schedule comparison: how does C differ when the original 0–199 frame sequence repeats, versus when the same total number of update calls uses a continuously increasing frame argument? Initial state and RNG should be matched and the original update kept unchanged. That would examine the clock-reset mechanism already visible in historical records, rather than inventing a new SRG evolution. **This is a recommendation only; no such run or new execution work order is included here.**

The June topology producer, pi*e*phi scale experiments, and a pendulum/vesica time mapping remain distinct questions. They have not been answered or implemented by selecting C.

## 8. Review materials and reproduction

This reviewer package contains:

- `SIM01_GPT_SCIENTIFIC_REVIEW.md` — this decision;
- `review_saved_evidence.py` — independent read-only checker;
- `INDEPENDENT_REVIEW_RESULTS.json` — full passive-check results and additional prefix comparison;
- `ARCHIVE_REVIEW.json` — package and preservation-evidence checks;
- `REVIEW_MANIFEST.json` — identities of the four files above.

The original 68-member submission is not duplicated or changed. To rerun only the passive review after extracting that original submission, use Windows CMD with actual local paths:

```bat
conda activate torment
python -B "<review directory>\review_saved_evidence.py" --bundle-root "<extracted original SIM01 review bundle>" --output-dir "<separate review output directory>"
```

The checker rejects output directories inside the input bundle. It uses NumPy but does not import the historical programs, detached engines, preflight, or rollout runners.

Source references for the findings are the submitted `SIM01_REPORT.md` sections “Actual motion, state and equations”, “Finite motion and feedback”, and “Saved logs, clocks and observer provenance”; `sources/source_A.py`, `source_B.py`, `source_C.py`; the three `runs/*/states.npz` records; and the two `data/*.csv` files. Reviewer-specific findings are explicitly separated above.
