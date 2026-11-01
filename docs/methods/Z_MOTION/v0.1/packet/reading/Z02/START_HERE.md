# NCM-Z-02 v0.1 — retained-history answer

**No nearest-opening switch survives freezing in the selected five-state window.** Frozen Z stays nearest G+0 at indices 0, 1, 2, 3 and 4. Scheduled Z has three resolved endpoint switches: G+0 → G−2 at 1→2, G−2 → G−0 at 2→3, and G−0 → G+1 at 3→4. In the specified native → envelope → clock accounting, each switch occurs at the clock replacement.

The admitted input is the already-saved NOMINAL_CROSSCHECK.json from the central-geometry numerical audit: five full triad states and four consecutive spans. It was computed previously at 120-decimal precision and saved as up to 100-significant-digit strings. Its file and source-member hashes match the historical manifest. This is a different initialization and fixed native parameter tuple from NCM-Z-01, not a continuation of that two-state fixture.

The entire 0–4 window, preset, geometry and tolerances were frozen in ADMISSION_AND_PLAN.json before opening calculations. Three distinct candidate artifacts totaling 19,361 bytes were read. No native states were generated or reconstructed.

The frozen points still change position and chord direction. Their radius decreases through index 3, then increases at index 4. From 1→2 the frozen point moves closer to the center while becoming farther from its nearest boundary. An unchanged nearest label is a coarse result, not stationary native behavior.

All ten primary F/S placements lie inside the original enclosing sphere. None lies on a central boundary or finite notch patch. The outward ray through F1 hits N+0; this is a direction test, not a point contact or passage. There are no unresolved nearest-arc ties or high-precision classification disagreements. This short, deliberately constructed historical nominal example does not establish behavior for other states, parameters or longer windows.

Validation: **246 assertions passed**, all 18 primary/intermediate readouts checked with independent 80-decimal formulas, and five numerical ledgers reproduced byte-for-byte in a separate packaged-input run. Ten monitored original files remain unchanged. The margin condition m>2||S−F|| supplies a numerical stability diagnostic at indices 0 and 1; failure at the later indices is inconclusive by itself.

- [Full report](REPORT.md), [frozen admission plan](ADMISSION_AND_PLAN.json), [identity/time receipt](ADMISSION_FREEZE_RECEIPT.json)
- [Top view](figures/01_top.png), [opposite side views](figures/02_opposite_sides.png), [complete index diagnostics](figures/03_index_diagnostics.png)
- [Observation ledger](OBSERVATIONS.json), [all six boundaries and notches](GAP_COMPARISON.json), [every transition](TRANSITIONS.json), [ordered attribution](ATTRIBUTION.json)
- [Standalone calculation](analyze.py), [tests](checks_results.json), [80-decimal comparisons](HIGH_PRECISION.json), [portable verification](PORTABLE_VERIFICATION.json)

Command Prompt and the existing torment environment were used offline. Native evaluations: zero. EMA updates: zero. No Git, model/application/kernel edits, new motion law or publication. The investigation stops here.
