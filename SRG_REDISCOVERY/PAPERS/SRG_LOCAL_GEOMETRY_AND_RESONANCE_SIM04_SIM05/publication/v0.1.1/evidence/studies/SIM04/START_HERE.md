# SIM04 — what the seed explorer actually does

Hilmir, this program starts with 50 points scattered in three dimensions. Each point carries a number called resonance. On every pass it moves toward its five nearest neighbors, shares resonance with those neighbors, receives a small pull toward one common resonance-weighted center, and gets a random positional nudge. The neighbors can change as the points move. The program keeps all 50 identities; approaching points are never combined into a new object.

The surviving record shows those points gathering into smaller local groups while their resonance values become more alike. The whole field also becomes less spread out. This combination is the most useful finding: **closer resonance values and a smaller overall spread do not mean that every point has merged into one group.** By the last saved state, the nearest-neighbor network has three disconnected groups when direction is ignored. The global center term still relates those groups to each other.

“Velocity” here means how far a point moved since the previous record. It is not carried momentum: the next movement does not read it. “Coherence” measures how similar the resonance numbers are. An “echo corridor” is a pair whose similarity-and-proximity score exceeds a threshold; detecting it does not add an interaction. The code's geometry label `higher_polyhedra` is already present at initialization because the selected subset has more than seven members. That label is not evidence that an exact polyhedron formed.

The records retain 21 states, passes 0–20, with 50 glyphs each: **1,050 rows**, plus **20 aggregate rows** for passes 1–20. All 240 stored aggregate values match recomputation exactly in the inspection environment. All 3,000 stored velocity components match saved position differences exactly. The deterministic resonance expression matches all 1,000 next-resonance values within **1.39 × 10⁻¹⁷**, evaluated independently at recorded inputs. Position updates include unsaved random increments, so this study does not claim full historical recurrence reproduction or recovery of seed 2038's random stream.

Several episodes make the movement easier to understand:

- The highest-resonance identity changes from glyph 3 to 40 at pass 3, then to 38 at pass 6. Glyph 38 stays highest through pass 20 but continues moving by about 0.986 coordinate units between passes 6 and 20. Staying first in a ranking is different from becoming stationary.
- The first detected echo corridor is **glyphs 5 and 43 at pass 7**. They gradually approach and become more similar; crossing the observer threshold changes the report, not the movement rule.
- At pass 20, the three highest-resonance glyphs, **38, 23 and 8**, lie within 0.068 units of one another. They remain distinct points. The whole field still spans more than eight units between its farthest pair.

![Saved-state overview](figures/F01_recorded_overview.png)

**New visualization of historical data.** No simulation was run. All four figures use the saved CSV states or explicitly identified calculations on those states. No original figure or movie attributable to this selected run was located in the bounded source package; the script contains no plotting or animation code.

Read [CONSTRUCTION.md](CONSTRUCTION.md) for the exact state and update equations, [ORIGINAL_EVIDENCE.md](ORIGINAL_EVIDENCE.md) for chronology and episodes, and [VERIFICATION_AND_LIMITS.md](VERIFICATION_AND_LIMITS.md) for checks, provenance and preservation. The unchanged original program and CSVs are in [originals](originals). [FIGURE_REGISTER.json](FIGURE_REGISTER.json) gives captions, inputs and classifications for the figures. [PROPOSED_LEDGER_ENTRY.md](PROPOSED_LEDGER_ENTRY.md) is a proposal; the canonical ledger was not edited.

The open questions are whether the local groups persist beyond this short record, how much long-term communication remains through the changing graph and global center, and what observations would justify a geometric classification stronger than the current size-based label. No long-time convergence, universal merger, physical gravity, energy conservation or master-equation connection is established here. Those are discussion questions, not permission to begin another experiment.

This is a March 2026 resonance-field program. SIM04 is our study number, not a statement of development order or direct descent from Volume I. The historical March commentary is retained as original writing, with its claims assessed against source and records in this package. The supplied work order governs this study; R0's old experiment proposal is not activated.

**Status: IN REVIEW — 23 October 2026.** Scientific lead: GPT. Author and research director: Hilmir Frímann Halldórsson. Research engineering: Codex. No new run, kernel change, publication or Git write. Stop here for discussion.

Administrative note, separate from SIM04: the completed Volume I publication receipt from the preceding task does exist. Its unchanged Markdown/JSON and delivery identity are copied under [context/publication_receipt](context/publication_receipt). It records commit `63469551eb04c17bfbedb6b8fce057c5890cbba8` and 502 successful fresh remote-byte comparisons. The work order's statement that this receipt was outstanding describes what GPT had then received; this study does not repeat that publication audit or alter its frozen edition.
