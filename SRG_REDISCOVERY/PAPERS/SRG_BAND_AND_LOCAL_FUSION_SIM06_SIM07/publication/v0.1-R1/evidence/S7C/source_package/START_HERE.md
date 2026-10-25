# Universe/condensate: what this original simulation does

Hilmir: the program moves points in three-dimensional space, and each point carries a changing number called resonance. A point first moves toward nearby neighbors. Its resonance is then averaged with theirs, possibly adjusted by assigned frequencies, and multiplied by the H time schedule. After that comes a second movement toward a resonance-weighted center. The important discovery in this source reading is **how that second movement is performed**.

When a horizon is enabled, points move through that second stage **one at a time, in array order**. Each point reads its neighbors' positions as they stand at that moment. A neighbor with an earlier ID may already have moved during this same stage. A later ID has not. The neighbor list itself remains the one selected before either movement stage. This is a precise, ordered construction; replacing the loop with a simultaneous update would change what the program says to calculate. We have not run either version or measured a reordered difference.

Without a horizon, the program instead computes one center from all points and moves them together toward it. Thus switching from a finite horizon to “no horizon” changes both the neighbor cutoff and the fusion rule. The historical comparison cannot be interpreted as changing only a radius.

The main surviving evidence is the original **200-row aggregate record**, not a movie or point-by-point trajectory. The selected driver starts with 120 points in six seeded populations, uses a horizon of 6, assigns four possible frequencies, and enables a prescribed, decaying oscillation of the resonance clipping limit. The program does not grow six populations from an initially unstructured cloud; their six starting locations are supplied.

The saved results remain interesting. The spatial observer's count falls from 49 at pass 1 to 10 at pass 16, then stays at 10 through pass 200. Resonance remains nonuniform, and the movement observer remains below its exact-rest value. But these are summaries: they cannot tell us the paths, shapes, neighbor memberships or individual centers that produced them. The old note's account of six populations and the table's ten threshold-defined groups use different definitions; neither should be silently substituted for the other.

![Original aggregate chronology](figures/F01_original_universe_chronology.png)

This is a new plot of historical numbers. No positions have been reconstructed or invented.

## What is established and what remains open

- **Source construction:** the complete 778-line original was read; all seven named source/evidence files match the supplied hashes. Local fusion uses current positions in ascending ID order, old neighbor selections, and post-H/pre-clipping resonance. Its centers exclude the point itself and have no distance weight.
- **Original observations:** all five CSVs are mapped to their generating drivers. The main chronology has passes 1–200, no initial row, no missing cells and no coordinates. The horizon table has 18 trial/configuration rows, not 18 time steps.
- **Historical qualifications:** all seven perturbation summaries say `DECAYING`, rather than `ABSORBED`; static/breathing summary numbers are identical but do not establish identical trajectories or why the bounds made no recorded difference. Frequency labels are assigned, not discovered. There is no physical energy or ground-state calculation in this engine.
- **Unresolved motion:** no complete Universe coordinate/RNG record or attributable movie was identified through the named recovered material and existing indexes. Actual within-pass order effects, spatial membership and historical independence claims remain unmeasured here.

## Review route

1. [CONSTRUCTION.md](CONSTRUCTION.md): state, exact pass sequence, ordered fusion trace and observer definitions.
2. [ORIGINAL_EVIDENCE.md](ORIGINAL_EVIDENCE.md): every driver/output link, selected initialization sequence, source-versus-narrative claims.
3. [MOTION_AND_GEOMETRY.md](MOTION_AND_GEOMETRY.md): what the aggregate chronology and horizon comparison do and do not demonstrate.
4. [MODEL_RELATIONSHIPS.md](MODEL_RELATIONSHIPS.md): global, band-wide and local centers; frequency/bound differences and creation-history limits.
5. [RECORD_SELECTION_AND_VERIFICATION.md](RECORD_SELECTION_AND_VERIFICATION.md): source identities, passive methods, preservation and package checks.

[REPLAY_DECISION_NOTE.md](REPLAY_DECISION_NOTE.md) is an **optional, unimplemented proposal for review** to recover the missing motion in one source-faithful setting. It is not an instruction to proceed.

**Completed for GPT and Hilmir review. Zero new state updates, RNG draws, imported historical executions, old scientific-checker reruns or Git writes. Originals and accepted work remain unchanged. No merger engine, manuscript, ledger update or next investigation has been started. Stop here.**
