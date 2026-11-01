# Reading map and non-duplication guide

Paths below are **members inside the named evidence ZIP**, unless a path begins with `reading/` or `reviews/`. Extract only into a new external working directory. Never run old helpers as part of this order.

## Z01 — two-state observation comparison

`evidence/NCM_Z_01_v0.1_REVIEW.zip`:

- `REPORT.md`, `START_HERE.md`, `TYPED_CORRESPONDENCE.md`.
- `OBSERVATIONS.json`, `GAP_COMPARISON.json`, `INITIAL_STATE_LEDGER.json`.
- `inputs/retained.motion.json`, `inputs/parent_run_record.json`.
- `source_snapshots/observer.py`, `z.py`, `readouts.py`, `dynamics.py`, `central.tex`, `host.tex`, `motion.tex`, `paperE.md`, `attachment.tex` (read as text).
- `figures/01_top.png`, `figures/02_side.png`.
- `SOURCE_MANIFEST.json`, `INTEGRITY.json`, `INPUT_VERIFICATION.json`, `checks_results.json` and preserved logs.

Its 0→1 pair is not the five-state run's 0→1 pair.

## Z02 — a separately admitted five-state history

`evidence/NCM_Z_02_v0.1_REVIEW.zip`:

- `REPORT.md`, `START_HERE.md`, `ADMISSION_AND_PLAN.json`, `ADMISSION_FREEZE_RECEIPT.json`.
- `inputs/SELECTED_HISTORY.json` and `ORIGINAL_TOKEN_LEDGER.json`.
- `OBSERVATIONS.json`, `GAP_COMPARISON.json`, `TRANSITIONS.json`, `ATTRIBUTION.json`, `HIGH_PRECISION.json`.
- `accepted_sources/` for the actual observer, central geometry and related source snapshots.
- `figures/01_top.png`, `figures/02_opposite_sides.png`, `figures/03_index_diagnostics.png`.
- `SOURCE_MANIFEST.json`, `PORTABLE_VERIFICATION.json`, `checks_results.json`, `CORRECTIONS.json`.

The input's original member is NOMINAL_CROSSCHECK.json in the archived central-geometry numerical audit. Provenance is already documented; do not regenerate the radical entrance or run that producer. No second history search is needed.

## Z03 — source accounting of that same five-state history

`evidence/NCM_Z_03_v0.1_REVIEW.zip`:

- `REPORT.md`, `START_HERE.md`, `SOURCE_CROSSWALK.md`, `SOURCE_EXCERPTS.txt`, `SOURCES.json`, `NUMERIC_POLICY.json`.
- `STATE_SNAPSHOTS.json`: endpoints, norms, area matrices, readout and radius.
- `NATIVE_INTENSITY_BUDGET.json`: parent/child hierarchy and saved-after residuals.
- `NATIVE_CHIRAL_BUDGET.json`: five amplitude and two phase area terms.
- `FROZEN_Z_SOURCE_BUDGET.json`: signed displacement contributions and residuals.
- `RADIAL_TRANSVERSE_ACCOUNTING.json`: fine/coarse radial and transverse accounts.
- `PASSIVE_PRESTAGES.json`: earlier reconstructed diagnostics, not extra saved states.
- `sources/kernel_physics/{dynamics,readouts,axial_observables,z_diagnostics}.py` and `sources/papers/PAPER_G/v0.1.1/source/paper_g.tex`.
- `figures/01_intensity.png`, `figures/02_transverse.png`, `figures/03_radial_balance.png`.
- `PRIMARY_EVALUATIONS.jsonl`, `COUNTS.json`, `CHECKS.json`, `PORTABLE_VERIFICATION.json`, `RESIDUAL_SUMMARY.json` and preservation records.
- `packet/NCM_Z_03_Packet_v0.1/inputs/SELECTED_HISTORY.json`: exact copy of Z02's same admitted file.

Use the `80` and `120` run keys as documented; prefer retained 120-digit strings for rounded Z03 tables, without treating the approximately 100-digit historical source as an exact native trajectory. Do not recompute fields from their formulas.

## Reviewer notes

`reviews/NCM_Z_01_GPT_REVIEW.md`: acceptance, ordered-stage clarification and phase/envelope corollaries.

`reviews/NCM_Z_02_GPT_REVIEW.md`: acceptance; separate elementary mirror-height, clock-sign, transverse and same-state macro-difference deductions; limited cross-platform replay.

`reviews/NCM_Z_03_GPT_REVIEW.md`: acceptance; exact budget semantics, readout composition, all four spans, finite residual limits and inference on later positive onsite contributions.

The accompanying three GPT evidence ZIPs document those prior checks. Their scripts are not execution instructions for this documentary task. No review inference should be silently upgraded to an independently new experiment or a physical mechanism.

## Avoiding duplicate evidence

Z03 already contains an earlier Z02 archive, and Z02 contains earlier material. The direct three review ZIPs in this task packet are supplied for accessibility and identity. They are not independent experiments. Keep original archives unchanged; do not recursively extract them all or count duplicate checks/states again.

The packet intentionally omits unrelated cone/return publication packages. Relevant definitions and geometry context are already embedded in the reviewed Z studies. Any historical publication status remains what the original receipt states; no current repository status is assumed.
