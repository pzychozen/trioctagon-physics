# Simulation 03: eight centers that can change their response

Hilmir, this program makes eight moving centers in three dimensions. It draws a tetrahedron around each center, but the corners and faces do not calculate the motion. Each center carries its position, velocity and a switch with two settings. The centers take turns responding to the average position of the group.

The switch reverses the **new interaction contribution**, not the velocity already being carried. The saved records show this distinction clearly. In the shorter log, center 5 changes its switch at callback 7. It first slows while still moving toward the group center, and moves away by callback 9. There is a delay because its previous velocity survives the switch. These are recorded events, not a new simulation.

Three other findings are especially useful:

- **The clock repeatedly starts over while the centers continue.** The longer file contains 1,092 updates and the shorter one 440, although the animation has only 200 numbered frames. Both files repeatedly return from label 199 to label 0, often followed by another zero. This restores a strong H value and is accompanied by renewed motion and increased recorded energy.
- **The source's “teleport” warnings do not reliably identify large movements.** Its distance calculation turns small negative coordinate changes into values near ten. Across the checkable transitions, it would report 8,151 body events in the longer log and 3,129 in the shorter one. Actual coordinate-boundary crossings number 22 and 7. No checked native increment exceeds 0.062 coordinate units.
- **Some striking back-and-forth behavior is real, but its large displayed jumps are coordinate wrapping.** In the shorter file, center 7 crosses the X boundary at callbacks 409, 414 and 418 while retaining the same switch setting. Its X velocity changes sign between crossings. Averaging wrapped coordinates changes the interaction target around these boundaries; no wall, collision or extra teleport mechanism is present.

The original ten-second movie survives. It shows an early screen relocation, several changes between the ordinary palette and red shades, and slower visible motion later. Colors also cycle with every frame, so a pale or suddenly red shape must not be mistaken for a new object or an instantaneous velocity reversal.

Eight fixed movie frames closely match images drawn from the shorter log's already-recorded states, with candidate correspondence **movie frame f → log B callback f+1**. This is substantial content evidence. The original export receipt and complete provenance are missing, so the formal original-run join remains **UNLINKED**. No movie measurement here silently inherits a CSV value as established ground truth.

The two old center-7 charts also strongly match the shorter log. Their traces use repeated frame labels while event markers use callback indices. That mixed axis makes the drawing misleading. The originals are preserved, and a separate diagnostic figure shows how that layout arises.

**What is in this package**

| Read | Purpose |
|---|---|
| [CONSTRUCTION.md](CONSTRUCTION.md) | The complete program, its state and exact update equations |
| [ORIGINAL_LOG_ANALYSIS.md](ORIGINAL_LOG_ANALYSIS.md) | Ordered callbacks, consistency checks and measured episodes with CSV line references |
| [TIME_SWITCH_AND_MOVEMENT.md](TIME_SWITCH_AND_MOVEMENT.md) | Clock resets, switching, damping, energy accounting and coordinate effects |
| [ORIGINAL_MOVIE_REVIEW.md](ORIGINAL_MOVIE_REVIEW.md) | Original movie, frame sheets, attribution tests and historical-chart findings |
| [SIMULATION_02_COMPARISON.md](SIMULATION_02_COMPARISON.md) | Differences from 3Dtriangles.py after independent study of plot_1.py |
| [VERIFICATION_AND_PRESERVATION.md](VERIFICATION_AND_PRESERVATION.md) | Methods, bounds, checks, hashes and remaining uncertainty |

Start visually with [the original movie](originals/tetrahedral_attractors_logic.mp4), [the movie overview](visuals/movie_overview.png), [the shorter log's chronology](visuals/B_chronology.png), and [center 7's boundary-crossing window](visuals/B_body7_seam_window.png). The latter two are new plots of original recorded data, not new simulated trajectories.

The cumulative [research ledger snapshot](ledger/SIMULATION_STUDY_LEDGER.md) preserves Simulations 01 and 02 as the accepted baseline supplied by the charter and marks this study **IN REVIEW**. Its canonical copy is in the new SIMULATION_RECONSTRUCTION_RESEARCH workspace; the ZIP contains an identical snapshot.

No historical program was run or imported. No fresh random state, simulation, parameter search, kernel change or publication was made. All original files and prior study packages were preserved. This checkpoint stops for GPT and Hilmir's scientific review.

Scientific lead: GPT. Research engineer: Codex. Date: 2026-10-22.
