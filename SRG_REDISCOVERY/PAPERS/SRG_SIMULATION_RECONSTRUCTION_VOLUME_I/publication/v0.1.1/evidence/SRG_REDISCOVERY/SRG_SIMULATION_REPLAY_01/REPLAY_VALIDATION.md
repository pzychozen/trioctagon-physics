# NEW REPLAY — validation and reproducibility
SRG_SIMULATION_REPLAY_01 · 22 October 2026

**Fidelity result:** all 500 instrumented end-of-sweep position snapshots match an execution of the byte-identical sandbox source bit for bit. All six final velocity components also match bit for bit. This verifies reproduction in the recorded environment, not an undocumented historical run or an exact-real theorem.

## Execution and initializer

Exactly one sampled configuration was used: legacy NumPy **RandomState(0)**, sampled as rand(3,2)*2−1. Zero initial velocities and all original constants were retained. Seed 0 is an investigator-selected reproducibility choice required by the work order; it was not recovered from historical evidence.

The six initial coordinates, zero velocities and hexadecimal float representations are in **replay/initial_state.json**. The pre-run selection rules are in **replay/RUN_SPEC.json**.

| Environment item | Recorded value |
|---|---|
| Interpreter | C:\Users\Notandi\miniconda3\envs\torment\python.exe |
| Python | 3.11.15, Anaconda, 64-bit |
| NumPy | 2.4.4 |
| Matplotlib | 3.10.9 |
| Numerical array type | NumPy float64 |
| RNG | Legacy MT19937 / RandomState, seed 0 |
| Plot backend | Agg |
| Full platform/version receipt | replay/environment.json |

Executed in Windows CMD with the requested environment:
~~~bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
python -B C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SRG_SIMULATION_REPLAY_01\replay\run_replay.py
~~~
The instrumented run completed 500 sweeps / 1,500 ordered point updates. The sole second trajectory execution was the expressly permitted seed-0 reference comparison, also 500 sweeps. No alternative seed, parameter sweep, initializer search, further trajectory or continuation was executed.

The run harness refuses to start when its execution receipt or trajectory already exists. Reproduction code is provided for review; it is not an instruction to run another experiment now. **observe_replay.py** and **verify_records.py** only load saved records; they do not advance the model.

## Source and comparison method

Original source SHA-256:
847819ec381e200d9008395175342ec138e52ab3180a4f599b4db1cb91ae42d3

Original attractors.png SHA-256:
72776de5e6228f4c4a0e2ef43d804f479bf8db80af6884e492e9ccbc3053d651

The 74-line source was copied byte for byte to **replay/source/recursive_attractor.py**. The authoritative historical file was read and hashed, never imported or executed in its original location.

The instrumented harness transcribes the same H, RPCO, TGMO, scalar constants, nested loops and arithmetic order. It records arrays by copying them. An interaction contribution is stored in a temporary for observation before being added; the numerical expression and serial addition order are unchanged. Observation-only copies and repeated endpoint calculations do not feed back.

For the independent comparison, the harness calls np.random.seed(0), then compiles and executes the **unchanged copied source bytes** in a separate namespace. Its original top-level setup, 500-sweep dynamics, position_log and plotting statements all run. Matplotlib uses Agg, and plt.show is temporarily a no-op; that handling prevents GUI blocking and does not change numerical state. The reference figure is closed without being saved or presented as new evidence.

The comparison reads position_log and final velocities from that namespace and compares their float64 bit patterns with the instrumented output. It does not compare the instrumentation against a second call to its own update routine.

| Check | Result |
|---|---|
| 500 × 3 × 2 recorded position values | 3,000 float64 bit patterns identical |
| Final three velocity vectors | Six float64 bit patterns identical |
| First position or final-velocity divergence | None |
| Stored reference outputs | replay/reference_comparison.npz |
| Detailed comparison receipt | replay/equivalence.json |
| Execution count receipt | replay/execution_receipt.json |

Intermediate reference velocities are not separately stored or compared at every sweep. The instrumented full velocity chronology is stored, and its input/output continuity is checked. Cross-version/platform bitwise reproduction is not promised; historical software versions and RNG state remain unknown.

## Numerical records and indices

All generated scientific records are marked **NEW REPLAY**. The unaltered historical source copy is identified separately by its hash.

| File | Contents and precision |
|---|---|
| replay/trajectory.npz | Lossless binary float64 positions and velocities, shape (501,3,2), including S₀; step/t/H arrays of length 500; event_id 1–1500; event_positions (1500,3,2); native event increments; integer position-wrap lattice shifts |
| replay/states.csv | 1,503 rows: 501 states × 3 points, with coordinates/velocities printed to 17 significant digits; state 0 has blank last-update clock fields |
| replay/within_sweep.jsonl | 1,500 records, one per point update, in native order; JSONL line number = event ID; Python float serialization round-trips binary64 |
| replay/selected_events.jsonl and .csv | Exact selected observations for events 1–9 and 502–510; CSV is a compact flattened view, not replacement dynamics |
| replay/observation_summary.json | Counts, recorded extrema, transparent window selection and selected input/output values |
| replay/record_checks.json | Saved-record consistency results and visual-inspection scope |

Each within-sweep record contains the full three-point input position and velocity arrays, the two other-point indices, raw and wrapped interaction differences, their contributions, net force, incoming/pre-damping/outgoing velocity, native increment, raw updated position, wrapped position, lattice shift and complete post-event positions. Clock values remain those actually calculated by the original floating-point expression step*dt.

No initial timestamp or within-sweep time was invented. State n>0 was produced by step n−1; t and H arrays are indexed by the step. Event e updates point (e−1) mod 3 in step floor((e−1)/3). End-of-sweep state n corresponds to event 3n.

The saved-record checker verified all event input arrays against the preceding recorded state, all unchanged point rows, carried-velocity continuity, every end-of-sweep snapshot, clock consistency, and CSV float round-trips. It also rechecked fidelity using the saved reference arrays, without re-executing either trajectory. Its 13 assertions passed.

## Visuals and what was actually inspected

The required static paths follow the source's 500-post-sweep-sample joining convention. The seam-aware version uses the same samples and omits only connectors identified by recorded position-wrap lattice changes. No changes were omitted in this run because there were no wrap events. **visuals/NO_POSITION_WRAP.txt** records that absence; no hypothetical wrap illustration was fabricated.

The two 12-panel contact sheets show consecutive recorded states in update order, with fixed axes within each sheet. Each has one before-sweep panel and three after-point panels per row. They were examined top to bottom and left to right. The two path plots and the distance/movement plot were also opened and inspected. All five PNGs are labeled NEW REPLAY.

The optional self-contained HTML viewer embeds the exact recorded data. Its point positions are selected from stored event states, without interpolation or a model integrator. Playback milliseconds are a display setting and do not redefine source dt. Browser painting may skip refreshes during Play; single-event controls address the complete recorded sequence.

**UI limitation:** the browser tool refused file:// preview under its URL policy. No server or alternate-surface workaround was used. The HTML's embedded records and event targets were checked, but interactive controls/playback were not GUI-validated. The inspected PNG sequences are the primary evidence; no claim of having watched all 1,500 events as a movie is made.

The rendering/observation helper was invoked twice, the second time to make the optional viewer use the already selected event IDs directly. Both invocations read the same saved data only. The simulation harness was invoked once, containing the one instrumented execution and one identical-seed reference execution.

There are zero position-wrap events and zero force comparisons with nonzero lattice shifts. TGMO still executes and can introduce rounding at the last bits even without a lattice shift. The maximum observed native-versus-screen displacement residual is about 1.36×10⁻¹⁶. The records are floating-point observations, not interval-certified real arithmetic.

## Preservation and package

Before writing, the new task directory was absent. The small baseline covered the work order, original source, original image, and the preceding construction review's two Markdown documents and manifest, plus Git HEAD, index hash and all 216 pre-existing porcelain entries.

Git HEAD: 170e638ecc0438f911c4ceb8091ffb1b574652fe

The six protected hashes, HEAD and index remain unchanged, and the pre-existing status entries are preserved. The sole additional status entry is the new untracked SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/ directory. The completed preservation receipt and hashes are in **MANIFEST.json**. This is a scoped preservation check, not a repository-wide audit.

The review ZIP includes the three review documents, scripts/template, unchanged sandbox source, full records and reference check, all five inspected PNGs, no-wrap notice, optional HTML viewer and checksums. Matplotlib's task-local font cache is excluded; no environment libraries or unrelated archives are bundled. Manifest self-hashing and ZIP self-inclusion are excluded to avoid circular checksums.

No original source, old image, prior review, kernel, accepted paper or unrelated working file was changed. No dependency installation, staging, commit, push or publication occurred. **This checkpoint ends with this one replay and its fidelity check.**

