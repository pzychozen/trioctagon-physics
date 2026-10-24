# SIM04 — performed checks, limits and preservation

Status: IN REVIEW. Scope: one historical source, two linked CSVs, directly associated March commentary and existing recovery/accepted-study context. No simulation, original import, fresh random draw, seed search, parameter sweep, package installation or scientific-kernel execution occurred.

## 1. Methods and exact comparison coverage

[inspect_saved_records.py](inspect_saved_records.py) reads the original-copy CSVs through Python `csv.DictReader` and converts numeric strings with `float`, retaining their order. NumPy/SciPy expressions are transcribed independently from the read source. Every transition comparison starts from the **stored** incoming X,R. Computed endpoints are never propagated to another pass. The original file is parsed with `ast` as text for the source-structure index; it is never imported, executed or evaluated as code.

| Check | Coverage | Maximum discrepancy / result | Acceptance rule |
| --- | --- | --- | --- |
| Archive/source/data byte identity | Selected four archive members, existing extracted files and R0 copies | All SHA-256 hashes match | Exact bytes |
| Trajectory schema/order/keys | All 1,050 rows | Pass 0..20 × IDs 0..49; no duplicate/missing keys | Exact order/schema |
| Finite values | Both CSVs in full | No nonfinite numeric values | All finite |
| Initialization V | All 150 components at pass 0 | All zero | Exact zero |
| Saved V versus X_p−X_(p−1) | 3,000 components, all 20 transitions | **0.0** | Absolute error ≤10⁻¹² |
| Recomputed aggregate values | 12 values × 20 metric rows = 240 | **0.0** for every value | Floating values ≤10⁻¹²; IDs/counts exact |
| Conditional resonance expression E3–E7 | 1,000 values at recorded inputs, all 20 transitions | **1.3877787807814457 × 10⁻¹⁷** | Absolute error ≤10⁻¹² |
| Neighbor cutoff ambiguity | All 50 rows × 21 state graphs | Minimum fifth/sixth neighbor distance gap 8.7980×10⁻⁵; no cutoff ties | Report actual gap, no tolerance-based relabeling |
| Coincidence in saved states | All pair distances × 21 states | Minimum 0.004007735677; no exact coincidence | Direct distance reading |
| RPCO clip activation | 1,000 preclip expressions | Zero lower / upper clip activations | Compare literal log input with ±9 |
| Sampled H normalization | 20 declared 20,000-point grids | All 4.500000000001 | Actual source sampling, no continuous-maximum claim |

Full metric values, comparison tolerances and errors are in [checks.json](analysis/checks.json), [metric_comparisons.csv](analysis/metric_comparisons.csv), and [transition_checks.csv](analysis/transition_checks.csv). “0.0” means exact equality of parsed/recomputed doubles in this environment, not a claim about real arithmetic or bitwise reproduction of the historical environment.

The 10⁻¹² tolerance is an absolute numerical agreement criterion, not a physical error model. All discrete counts/IDs are compared exactly. No tolerance was adjusted to obtain the result. No error threshold is used to certify the unsaved random increments.

## 2. Position residual and the limit of recurrence attribution

For each saved transition independently, calculate E1–E5 at X_(p−1),R_(p−1), then form

\[
\epsilon^{\rm residual}_{p,i}=X^{\rm saved}_{p,i}-\big(Y_i+F_i\big).
\]

The source places a Gaussian position increment at exactly that point. Over all **3,000 residual components**, the observed mean is −0.000104266069, population standard deviation 0.010015489535, RMS 0.010016032250 and maximum absolute component 0.036804528893. These have a scale compatible with the source's σ=.01. This is **not** a Gaussianity test, recovery of a random stream or proof that every discrepancy came from that draw. CSV arithmetic, original-environment differences or an unrecorded source difference would also reside in this residual. We do not fill in an inferred RNG state or simulate an endpoint from it.

The local displacement term's RMS vector norm falls from 0.25048727 at the first transition to the late values retained in `transition_checks.csv`; the global fusion term is smaller in this record. That is a decomposition at recorded inputs, not an ablation experiment or a causal estimate of the trajectory without one term. The residual is retained per glyph and pass in [position_residuals.csv](analysis/position_residuals.csv).

Resonance agreement is **conditional on recorded positions and parameters**. It strongly supports the stated exchange, ordering and resonance operations; it does not independently reconstruct the missing stochastic position chronology. No “exact recurrence reproduction” claim is made.

## 3. Inspection environment and reproducible use

The authorized record inspection used Windows Command Prompt and `conda activate torment`: Python 3.11.15, NumPy 2.4.4, SciPy 1.17.1, Matplotlib 3.10.9. Exact Python/platform information is saved in `analysis/checks.json`. No packages were installed or updated. `-B` prevents Python bytecode writes; the plotting script sets its Matplotlib cache inside this study directory.

From the repository root, these inspect the copies / regenerate only historical-data plots:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
python -B SRG_REDISCOVERY\SRG_SIMULATION_STUDY_04_SEED_EXPLORER\inspect_saved_records.py
python -B SRG_REDISCOVERY\SRG_SIMULATION_STUDY_04_SEED_EXPLORER\plot_historical_records.py
```

They write their analysis/figure outputs only under this study directory; use a copied review directory if retaining its sealed output identity. They do not import `originals/srg_seed_explorer.py`. Do not substitute its main entry point, which would launch several experiment families. `prepare_evidence.py` and `finalize_review.py` are packaging/provenance utilities with existing-output guards, not simulation launchers.

No dependence on a live web service is needed to inspect the source, data, equations, plots or numerical receipts. Original source line locations are indexed in [source_structure.json](analysis/source_structure.json), with a complete numbered reading copy. The originals are included with original byte identities. Neighbor edges, echo-pair rows, graph membership and the episode diagnostics are retained rather than being hidden behind figures.

## 4. New observer definitions and visual QA

The historical source exports no neighbor-history table, weak/strong component counts, all-pass geometry labels, turn-angle ranking or decomposition of source terms. Those are **new observations/calculations on historical data**, distinctly named in this package. Weak graph components ignore edge direction; strong components require directed paths both ways. Edges at a saved pass use that pass's distances, and are not interpolated across unsaved substeps. The last-state graph supports a diagnostic only, not evidence of a performed pass 21.

All four PNG figures were visually inspected for readable labels, unclipped content and consistent interpretation. F02 retains fixed axes in both projections and a fixed resonance color scale. Pair distances use genuine 3D coordinates; projecting two points onto the same screen position does not imply contact. Straight segments and steps in figures are display conventions between discrete records. No original rendering is recreated or claimed. SVG companions are provided for inspection/export.

The source can compute different behavior on negative resonance, coincident positions or empty neighborhoods. Those cases are transcribed from code, not claimed to occur here or newly simulated. No original media was found for this run in the bounded March package; R0's unrelated media inventories do not establish one.

## 5. Provenance and interpretation limits

**ORIGINAL:** unchanged source, CSVs and historical commentary. **ATTRIBUTED:** their strongly supported source/run association. **OBSERVED:** values and patterns in this saved window, including explicitly new diagnostics of those values. **DERIVED:** exact mathematical transcription and conditional algebraic calculations. **HYPOTHESIS:** proposed persistence, stability or geometric interpretations not established here. **MISSING/AMBIGUOUS:** execution fingerprint, original RNG state/software environment and an attributable original movie. No new **REPRODUCED** category is used.

No finite record here proves long-time convergence, universal attraction, a conservation law, physical energy, intelligence, a torus, a physical force/container or a zeta/master-equation coupling. “Seed,” “coherence,” “lock” and “higher_polyhedra” must be read through their actual definitions. A persistent rank is not a stopped point, and near-contact is not entity fusion.

A later replay would require a separate decision. If GPT and Hilmir choose one, a useful narrowly scoped purpose would be to test whether the observed neighbor partitions persist and how the global fusion contribution behaves, saving every state, graph, deterministic term and realized noise increment. The first replay should record the exact unchanged source hash, environment and RNG checkpoint at initialization and each pass. Its length, seed and outputs should be fixed in a new order; it would be a new run, not the recovered historical run. **No such replay was prepared or executed here.**

## 6. Preservation, ledger and publication context

All writes for this assignment are confined to `SRG_REDISCOVERY/SRG_SIMULATION_STUDY_04_SEED_EXPLORER`, which was absent at the initial check. [PRESERVATION_BASELINE.json](PRESERVATION_BASELINE.json), its comparison-context supplement and [PRESERVATION_RECEIPT.json](PRESERVATION_RECEIPT.json) identify the exact originals/context inspected and their before/after hashes. This is a scoped preservation check, not a re-audit of the whole repository. Original source/data/archive, R0 evidence, prior publication receipts, accepted comparison material and canonical ledger remain unchanged. No Git staging, commit, push, publication or kernel/UI modification was performed.

The cumulative ledger is unchanged. [PROPOSED_LEDGER_ENTRY.md](PROPOSED_LEDGER_ENTRY.md) is an unaccepted proposal for review. The old R0 tower experiment proposal is not an instruction for this assignment and was not run.

The attached work order's publication qualification is administrative: the prior `V1_PUBLISH/PUBLICATION_RECEIPT.json` now supplied under `context/publication_receipt/` records all 502 fresh remote files matching the accepted payload at commit `63469551eb04c17bfbedb6b8fce057c5890cbba8`. That receipt and its delivery identity are preserved; SIM04 did not rerun or broaden the publication check. Its historical CI observation is not presented as today's CI status. The accepted Volume I payload and manuscript-status text were not modified.

The review ZIP includes a manifest of all package members except that manifest itself. Its independent ZIP hash and receipt hash are recorded in adjacent `DELIVERY_RECEIPT.json`, avoiding a circular self-hash. The raw accepted originals, methods, outputs, figures and narrative documents are packaged together. Stop after this review package; no SIM05 was selected.
