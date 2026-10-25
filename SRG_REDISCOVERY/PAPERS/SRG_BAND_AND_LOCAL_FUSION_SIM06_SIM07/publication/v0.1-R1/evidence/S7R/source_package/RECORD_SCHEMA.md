# Record schema — REPRODUCED seed-1618 Universe

Binary NPZ arrays are authoritative. Load with `numpy.load(path, allow_pickle=False)` and retain each array's declared dtype and shape. NPZ compression is lossless. JSON and CSV are readable companions. Coordinates and amplitudes have no specified physical units. Time is the integer pass counter; there is no separate time-step duration. Nothing in a record feeds the next source update.

## Boundaries and original observers

Each run has `runs/<run>/boundaries/boundary_000.npz` through `boundary_200.npz`. Boundary 0 follows the driver's replacement X/R draws; metrics are still empty. Every file contains:

| Key | Shape / dtype | Meaning |
|---|---|---|
| pass | scalar int64 | Completed pass, 0–200 |
| ids | (120,) int64 | Stable original row IDs, 0–119 |
| X, V | (120,3) float64 | World position and last completed displacement; V=0 at boundary 0 |
| R | (120,) float64 | Signed real amplitude |
| frequencies | (120,) float64 | Fixed original independent frequency choices |
| configuration_json | scalar Unicode | All ten original stored configuration values, repeated at each boundary |
| rng_* | See below | Complete legacy RNG state at this boundary |

There are 201 boundaries, or 24,120 point-state rows per run. Each run's `point_states.csv` is a complete readable companion derived afterward from these saved arrays (boundary, ID, diagnostic population, frequency, X, signed R, V). Binary arrays remain authoritative. There are only 200 historical/completed metric rows. `metrics.npz` preserves one array per original metric column, in original order; `metrics.json` preserves row keys and original integer/float values; `full_universe.csv` is the unchanged original export operation. No boundary-0 observer row is inserted. Endpoint stdout is retained at root as `<run>_STDOUT.txt`.

## Random stream and actual returned values

`random/CALLS.json` indexes call metadata in source order. Each `call_<index>_<kind>.npz` includes complete before/after RNG states and, except seed, the actual returned `value` copied before it is returned unchanged to the source. All random calls are invoked once. No state is restored and no return is regenerated.

Indices: 0 seed; 1–6 Gaussian population blocks (20,3); 7 discarded constructor X (120,3); 8 discarded constructor R (120,); 9 frequency choice (120,); 10 replacement R (120,); 11–210 noise for passes 1–200 (120,3). All returned arrays here are float64. Seed is counted separately from value-producing draws. The initial population array is exactly the stack of calls 1–6 and is also boundary-0 X.

For prefixes `rng_`, `before_`, `after_`, `pass_before_`, `pass_after_`, `noise_before_`, `noise_after_`:

- `name`: scalar Unicode generator name.
- `words`: complete (624,) uint32 MT state.
- `position`, `has_gauss`: scalar int64.
- `cached_gaussian`: scalar float64, including its raw bit pattern even if cache flag is zero.

Only call-0 **before-seed** RNG state is excluded from cross-process fidelity; all checkpoints beginning with the deterministic seed result must agree exactly. Pass-boundary checkpoints and noise-before/after checkpoints describe the same stream with no other intervening draws.

## Capture pass records

`runs/B_CAPTURE/stages/pass_001.npz` through `pass_200.npz` refer to incoming boundary p−1 and completed boundary p. No pass-201 graph/update is evaluated. For all padded arrays k=5; meaningful entries are the first `neighbor_count[i]` slots in ascending selected-ID order. Padded IDs are −1; padded floats are zero and **not observations**. `fusion_valid` masks center/read validity for empty rows. All floating arrays are float64 unless NumPy records a scalar of the same precision; observer membership uses SciPy's original integer dtype. Linkage is (119,4) float64.

| Group | Keys / shapes | Interpretation |
|---|---|---|
| Incoming | incoming_X (120,3), incoming_R (120,), adjacency/distances (120,120) | Actual boundary values and source's once-computed graph/distances |
| Selection | neighbor_count (120,) int64, empty_rows (120,) bool | Strict radius <6, up to five non-self neighbors |
| Local movement | lap, Y (120,3) | Actual simultaneous local difference average and post-local coordinates |
| Coupling | coupling_distance_weights, coupling_frequency_factors, coupling_weighted_pre_guard, coupling_final_weights (120,5) | Actual first normalized weights, frequency multipliers, pre-guard weights, second normalized weights |
| Coupling guards | coupling_weight_sum (120,), coupling_guard_visited/passed, coupling_active (120,) bool | Strict >1e−10 guard; empty rows never visit it |
| Coupling outputs | coupling_R_neighbor, coupling_row_result, B (120,) | Actual weighted neighbor scalar, row result, installed post-coupling R |
| H | H, H_factor scalars; Q (120,) | Actual H and multiplier; post-H, pre-compression amplitude retained unchanged during fusion |
| Fusion visits | fusion_visit_order (120,) int64, fusion_ids (120,5), fusion_valid (120,) bool | All 120 visits per pass, including skipped rows |
| Fusion reads | fusion_reads (120,5,3), fusion_weights/fusion_Q_neighbors (120,5) | Coordinates and weight operands passed to original np.average; associated Q values |
| Fusion writes | fusion_center, fusion_before, fusion_after, Z (120,3) | Actual center; row before/after write; complete post-fusion coordinates |
| Compression | pre_compression_R, post_compression_R, compression_magnitude, compression_log_magnitude (120,); L scalar | Actual inputs/output and passive evaluation of log(abs(Q)+1e−9) for flagging; no alternative amplitude update |
| Compression flags | clipping_lower/upper, compression_zero_input (120,) bool | Strict log comparison with ±L; zero distinguished from a nonzero input raised to the lower floor |
| Noise | noise (120,3), noise_scale scalar; noise_before/after RNG | Actual returned Gaussian array, prescribed scale and complete checkpoints |
| Completed | completed_X/R/V | Exact copies at completed boundary |
| Observer | observer_membership (120,), observer_linkage (119,4), observer_metric_json scalar Unicode | Existing linkage/fcluster result captured when computed; original metrics row |

`fusion_before[i]` is Y_i because its own row has not yet been written; selected neighbor values may already differ from Y_j when j<i. Neighbor selection never changes within the pass. `fusion_reads` and weights are copied from the actual arguments of the single original np.average evaluation. The global NumPy wrapper is guarded so unrelated average calls are untouched. Recording adds no synthetic center to the evolution.

`CALL_BUDGET.jsonl` is the durable append/flush/fsync ledger outside the engine. Initialization entry precedes the driver call; initialization completion follows boundary-0 saving. Step entry precedes the single original step call; completion follows recording. Failed calls would remain attempted. `PROCESS_*.json` separately captures process command, PID, exit code and timestamps. There is no retry/resume path.

## Inspection versus scientific execution

Only `launch_run.py`/`run_once.py` execute the two prescribed drivers; **do not rerun them**. Methods such as `verify_records.py`, later analysis and figure rendering read the retained arrays only. Reproducibility code is supplied for review, not authority to spend another initialization. Relative links inherited in `handoff/context` resolve within the enclosed acceptance archive as described by its README; new reports point to current package paths.
