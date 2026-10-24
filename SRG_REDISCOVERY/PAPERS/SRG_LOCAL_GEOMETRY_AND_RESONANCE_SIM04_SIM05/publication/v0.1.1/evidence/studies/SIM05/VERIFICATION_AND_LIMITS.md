# Verification, preservation and limits

**Disposition:** SIM05 complete for GPT review; no acceptance or publication claimed. The user instructed us to follow the separate work order. That file was read first and controls this assignment. The embedded copy was independently hashed and proved byte-identical; the handoff's notes and historical claims remain evidence, not authority to expand scope.

## Checks actually performed

| Gate | Result and retained evidence |
|---|---|
| Historical identities | All3 originals match R0, handoff, resolved extracted originals and actual selected archive members; PREPARATION.json and selected origin records |
| Isolated source | Exact normalized slices43–55,61–275 plus required imports; H/RPCO/class/H_MAX AST match; original33529-byte file preserved |
| Pre-run checks | Syntax, exact slices/hash, required dependency availability and `torment` environment only; **zero smoke advances** |
| Budget | Two fresh sequential processes, reference then capture, exactly200 calls each;400 total; no retries or extra seeds |
| External recording | Arrays copied at each boundary; no recording RNG draws; after-recording RNG unchanged; all initial/before/after states retained |
| Reference equality | Bitwise X,R,D,V,pass and all complete RNG arrays at all201 boundaries; all200 metric dictionaries serialize identically; REFERENCE_EQUIVALENCE.json |
| Complete capture | 10,050 unique ordered glyph records; exact NPZ and round-trippable CSV;200 metric rows |
| Historical table | 200 finite ordered rows; identities/GRF checks; 4,000 metrics compared per column and pass; max error3.35288e−14 |
| Conditional field calculation | R,D max absolute error0 against saved next arrays, each calculation restarted from saved incoming state |
| Observer staging | New-position/old-adjacency curvature and old-distance/new-R echoes recomputed; all metrics within6.67e−16 absolute |
| Position decomposition | Zero reconstruction discrepancy; residual definition makes this algebraic, not independent noise verification |
| Clip/sign audit | R lower/upper0/0; D lower/upper3/0; no R or D sign changes |
| SIM04 addendum | Original saved states only; all16 weak-component memberships and retained30-edge/no-crossing checks agree;16 covariance records and240 fixed-pair records |
| Figures | Seven PNGs visually inspected; SVG companions; equal axes for 3D, declared IDs/selection/centroid/orientation; no surfaces inferred |
| Preservation | Scoped before/after SHA-256 comparison of inspected inputs, with exact file count and outcome in PRESERVATION_FINAL.json |
| Package | Root payload manifest, ZIP byte readback, links in new review documents, and external ZIP receipt; PACKAGE_VALIDATION.json / DELIVERY_RECEIPT.json |

Tolerances were declared in the inspection code before calculations: absolute1e−12 for offline field/metric checks, and historical near-comparison absolute1e−12 plus relative1e−10. No threshold was adjusted to make an analysis pass. Bitwise reference equality uses array dtype, shape and bytes, including signed-zero distinctions; identical finite metric JSON preserves identical floating representations. Timestamps are excluded.

Both runs use the same unchanged numerical body and external boundary recorder; their agreement establishes repeatability and that this recording path does not disturb the stream. It is not an independently implemented solver proof. The offline stage/observer transcription is a separate conditional calculation and does not create another trajectory. Source expressions and statement order were never replaced by that transcription.

## How to inspect without spending another simulation budget

Run from this extracted study directory in Windows Command Prompt:

```cmd
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
python -B verify_package.py
```

This verifier reads the delivered manifest, state/metric/RNG records and receipts; it does not import the original or advance a field. The new data scripts `analyze_saved.py` and `detail_and_figures.py` can regenerate offline tables/figures from saved records, but doing so rewrites derived files and changes the sealed package manifest. For ordinary review, use the supplied outputs and read-only verifier.

Actual trajectory commands were `run_bounded.py --check` and then the one-shot `run_bounded.py --execute`, under the same CMD/conda environment. The parent invoked two fresh `python -B ... --worker` processes. The runner deliberately refuses execution when RUN_BUDGET.json already exists; each worker also refuses an existing output directory. The budget is exhausted. Do not remove these guards to rerun within this assignment.

`prepare.py` records the one-time provenance/core extraction. It is retained for audit, not a portable required review step: its original Windows input paths are intentional. The finalizer makes package metadata only and contains no simulation calls. Original source and excluded experiment functions can be inspected as text.

## Evidence dictionary

- **ORIGINAL:** preserved historical file bytes; does not independently prove the source's narrative.
- **ATTRIBUTED:** source/data association supported by filenames, schema, archive and numerical agreement; exact old runtime remains unknown.
- **OBSERVED IN HISTORICAL DATA:** a value or relationship obtained from retained numerical records, with the records' scope.
- **REPRODUCED:** this new fixed-seed, same-source execution, even where historical metrics match.
- **DERIVED:** an equation consequence or offline calculation from specified saved inputs.
- **HYPOTHESIS:** interpretation or possible further question beyond established results.
- **MISSING/AMBIGUOUS:** absent historical full arrays, RNG/environment or experiment-specific raw output; no invented replacement.

The historical CSV cannot recover every glyph trajectory, every D sign, component geometry or exact old random stream. Present agreement is close, not a claim of bitwise historical reproduction. Other experiment claims remain source-only or attributed notes. No memory-death, golden-structure, zeta, anatomy or alternative configuration was executed. No probability law, asymptotic theorem, causal gamma ablation or physical identification is inferred from this single finite replay.

Late noise residuals are small and heterogeneous in scale because sigma changes with pass. An aggregate residual standard deviation is not a test that the original randomness was Gaussian. Complete current RNG checkpoints are supplied so the current computation can be audited without relabeling residuals as recorded draw arrays.

## Preservation scope

All writes are confined to this new SIM05 directory, including plotting cache. The initial core/input baseline and a supplemental context baseline cover only files actually used, not a fresh whole-repository audit. Existing historical sources, accepted packages, the canonical ledger snapshot and inspected publication receipt/map remain unchanged. Existing preserved context documents may contain relative links to their original full packages; their byte-preserved copies are contextual excerpts, not newly rewritten standalone editions. New root review links are separately checked.

The root manifest excludes only itself, the root delivery receipt, the root validation receipt, the root output ZIP and the explicitly non-evidence plotting cache. These exclusions use exact relative paths, not a blanket basename filter; nested historical receipts/manifests remain payload. The ZIP is fully read back and every included member compared with its listed hash. Its own identity is recorded externally to avoid circular hashing.

Git HEAD and tracked/index status are checked read-only at completion. No stage, commit, push, force-push, remote audit, kernel change, dependency installation or accepted-checker rerun was made. The package stops for scientific review.
