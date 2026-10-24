# SIM05 — independent GPT review

Start with [SIM05_GPT_SCIENTIFIC_REVIEW.md](SIM05_GPT_SCIENTIFIC_REVIEW.md).

Verdict: ACCEPTED within the bounded source-and-finite-replay scope. The SIM04 historical 3D addendum is also accepted. No simulator updates, Git operations, source corrections, ledger edits or publication were performed by GPT.

The full unchanged submission is under `source_package/`. New audit outputs are `verification.json`, `integrity.json`, `findings.json`, `supplemental_checks.json` and the three small CSV tables. `independent_audit.py` and `supplemental_checks.py` retain the offline calculations. They never import the simulator or call its update method. The supplemental script can additionally compare the earlier uploaded SIM04 ZIP when its original sandbox path exists; that optional environmental comparison is already recorded in the results.

The independent audit takes an input directory and a separate output directory as command-line arguments. It reads fixed saved states and writes only its own review outputs. It decodes recorded RNG checkpoints to check existing noise, not to advance a new simulation. Re-execution is not needed to read this review.

The new findings are: the 238 final echo detections are precisely all pairs within the five components; the 44 candidate points exclude exactly the six-point component; and component-uniform R/D amplitudes are conditionally preserved even while the geometry changes. See the report for the exact premises and limits.

No next simulation or publication authority is implied by this review. The agreed route remains one bounded representative Tower II study, then the March reconstruction manuscript.
