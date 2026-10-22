# Comparison with the accepted 3Dtriangles.py study

This comparison follows the independent source, log and movie analysis of plot_1.py. It describes implementation relationships; the historical order of development is not established by directory numbers or current study numbers.

Baseline: [Simulation 02 START_HERE](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_02/START_HERE.md). Its source is OLD_MATERIAL/Simulations_Trash/Simulations_part_2/3Dtriangles.py, SHA-256 4c53678eefd803e93a910b74e7a8096bfd5095e0d09d09c9df0e7cf514b312f1. A byte-identical [comparison copy](originals/3Dtriangles.py) is included here. The accepted study and its evidence have not been revised.

## What is preserved

| Mechanism | 3Dtriangles.py lines | plot_1.py lines | Relationship |
|---|---|---|---|
| Eight centers, three dimensions, period10, DT0.1, velocity scale0.2 | 8–16 | 10–18 | Same numerical constants and random initialization distributions |
| Fixed tetrahedral offsets, faces, alpha0.6 | 19–26, 64–71 | 21–28, 91–97 | Same decorative geometry; neither has angular motion or collision dynamics |
| H, componentwise RPCO, incoming mean-speed GRF | 33–51 | 36–54 | Function bodies are AST-identical after docstrings are removed |
| t=frame*DT | 76 | 102 | Label-driven clock, no accumulated elapsed-time variable |
| Centroid recomputed inside body0–7 loop | 83–88 | 109–113 | Same in-place mixed old/new position dependence |
| Arithmetic mean of wrapped coordinates, then minimal displacement wrapping | 85–87 | 110–112 | Same coordinate sensitivity; neither uses an intrinsic periodic mean |
| Regularized direction denominator norm+0.01 | 88 | 113,120 | Same magnitude regularization |
| Shared GRF/H, velocity addition then RPCO, then position using new velocity | 79–96 | 103–126 | Same order and carried velocity |
| Save followed by show, no state reset or main guard | 107–119 | 155–167 | Both permit state-changing initialization/repeat callbacks |

“AST-identical” is a static parse comparison, not an execution of either source. Both functions called GRF read global velocities, not their positions/t arguments. Both H schedules can be negative; even the no-switch source is not permanently inward-directed.

## What is introduced, removed or changed

| Feature | Simulation 02 | Simulation 03 | Mathematical / evidential consequence |
|---|---|---|---|
| Persistent binary state | Absent | Eight zeros initialized at line152; updated116–117 | Adds eight carried mode bits |
| Random draws after initialization | Absent | Per-body draw if common GRF>0.5; toggle if draw<0.01 | Dynamics additionally depend on the random stream |
| Interaction multiplier | +1 | 1−2*post-gate mode at120 | Reverses the newly added contribution, retaining existing velocity |
| Nominal frame count | 2,000 | 200 | A label pass covers H arguments0–199.9 versus0–19.9 |
| Blitting | True at107 | False at155 | Changes library drawing/initialization paths; not a different force equation |
| MP4 rate | 60fps at113 | 20fps at161 | Movie seconds cannot be compared as equal model time |
| Nominal GUI interval | 50ms | 50ms | Preserved request; actual callback timing still unrecorded |
| Palette | viridis, phase index+frame | viridis or Reds by mode, same phase | Mode display introduced; phase is still not a stable identity color |
| Numeric history | None exported | Timestamped CSV, eight rows per callback,144–147 | Original callbacks and outgoing state are inspectable here |
| Energy | Not computed | Global kinetic diagnostic plus zero potential placeholder,57–61,129 | Adds accounting, not energy feedback |
| “Teleport” tracking | Not computed | Previous-position copy, unsigned-modulo diagnostic, console print | Adds a flawed diagnostic; does not alter motion |
| File/title names | tetrahedral_attractors_animation.mp4 / Toroidal Space | tetrahedral_attractors_logic.mp4 / Energy and Teleport Tracking | Distinguishes source-associated outputs |

No previously implemented motion term is removed from the base centroid/RPCO/GRF update. The binary sign modifies that update. Rendering, frame count and diagnostics also differ; treating mode flipping as the *only* experimental change would be inaccurate.

## A precise conditional relationship

For an identical incoming numerical state and frame label, if every post-gate mode in plot_1.py is zero, its mathematical position/velocity update equals the 3Dtriangles.py update. Both compute the same mixed-state centroids and share the same H, GRF, regularizer, RPCO and wrapping. This is a source-derived conditional identity.

It does not imply identical historical trajectories. Random initial states are unrecovered; plot_1.py consumes additional random numbers; frame schedules and drawing callbacks differ; original runs are not paired controls. No common-initializer comparison or new trajectory run was performed.

## What the evidence improves—and what cannot be inferred

Simulation 02's accepted movie has 2,000 decoded frames at60fps. Its frames13→14 show a relocation consistent with wrapping; later screen movement becomes small. Missing numerical states prevent certification of its exact native displacement or velocity response. Movie association with its source is strong, not a recovered export chain.

Simulation 03 has original numeric evidence. Bq2/body2 is a measured seam with a 0.054654713 native increment; its opening movie relocation has a strong but formally unlinked content correspondence. Bq409/414/418 show boundary crossings and velocity reversals while a mode remains unchanged. A and B also expose repeated label passes and energy bursts at resets. These are findings in these saved records, not demonstrations that Simulation 02 could not exhibit the same mechanisms.

The shorter movie's late movement, clustering, colors or reversals cannot be assigned causally to the binary switch by comparison with a different, much longer, randomly initialized movie. A controlled causal comparison would require a separately authorized study. This checkpoint neither performs nor preauthorizes it.

## Relation to Simulation 01 and the wider reconstruction

The accepted recursive_attractor.py study concerns three centers in two dimensions, pairwise interactions, period2, zero initial velocities and a plain500-sweep loop. Its seed0 replay is explicitly **REPRODUCED**, not historical data for either tetrahedral program. It supplies the methodological lesson that trails, simultaneous positions and callback/update chronology must be distinguished.

This ledger entry keeps moving-center programs separate from fixed-grid SRG, later amplitude-coupled models, production kernels and the earlier path-inheritance screens. Shared names such as H or RPCO do not prove an entire model or physical interpretation is shared.

Open comparative questions are the historical source/export chronology, exact callback histories behind Simulation02's movie, and behavior under a genuinely matched experiment. They remain unresolved here. No further simulation is begun.
