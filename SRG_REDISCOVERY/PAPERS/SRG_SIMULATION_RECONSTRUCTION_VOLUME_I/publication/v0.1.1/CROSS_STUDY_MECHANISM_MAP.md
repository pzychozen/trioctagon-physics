# Cross-study mechanism map

Research order is not asserted historical development order. Source abbreviations refer to the unchanged copies in [MANUSCRIPT/sources](MANUSCRIPT/sources); original locations and SHA-256 values appear in manuscript Appendix A and the manifest.

| Mechanism | S01 recursive_attractor.py | S02 3Dtriangles.py | S03 plot_1.py |
|---|---|---|---|
| Moving entities | Three2D points (5–11) | Eight3D centers (8–16) | Eight3D centers (10–18) |
| Carried numeric state |12 real position/velocity entries |48 real position/velocity entries |48 reals plus8 binary modes (152) |
| Initial positions |Uniform draws in[-1,1), no seed (10) |Uniform draws in[0,10), no seed (15) |Same distribution (17) |
| Initial velocity |Zero (11) |Components in[-0.1,0.1) (16) |Same distribution (18) |
| Interaction target |Other two points separately (45–51) |Arithmetic mean including self (85) |Same mean (110) |
| Ordered dependence |Updated prefix, old suffix;0→1→2 (43–56) |Updated prefix, old suffix;0→7 (83–96) |Same order (109–126) |
| Direction wrap |TGMO(diff), period2,[-1,1) (35,50) |Period10 displacement into[-5,5) (87) |Same (112) |
| Regularization |norm(diff)+0.001 (51) |norm(diff)+0.01 (88) |Same (113,120) |
| H |Four-term damped trigonometric/exponential formula (16–27) |Same formula (33–42) |Same formula (36–45) |
| H clock |step×0.05, direct500-sweep loop (38–40) |frame×0.1 (76) |frame×0.1 (102) |
| GRF |Absent |1/(1+mean incoming speed), shared (48–51,79) |Same, also gate input (51–54,103,116) |
| Binary sign |Absent |Absent |Post-toggle1−2b; gate GRF>0.5 and draw<0.01 (116–120) |
| Update randomness |None after setup |None after setup |One draw per body if gate open; no draw if closed |
| Velocity |Add0.05HF, then componentwise RPCO (54–55) |Add0.1gHd/(norm+0.01), then RPCO (91–92) |Same with binary sign (123–124) |
| Position |Wrap(x+0.05v_new), period2 (56) |Wrap(x+0.1v_new), period10 (95–96) |Same (125–126) |
| Drawing geometry |Points become connected static trails (64–74) |Fixed tetrahedron offsets; no separate vertex dynamics (19–26,99–102) |Same offsets (21–28,137–141) |
| History |500 post-sweep position snapshots, not fed back (57–62) |No numeric history export |Eight CSV rows after every callback (144–147) |
| Energy |Not computed |Not computed |Global0.5Σ‖v‖²; potential0; no feedback (57–61,129) |
| Teleport diagnostic |Absent |Absent |Unsigned-modulo distance>1; print only (64–71,132–134) |
| Palette |Default static line cycle |viridis((i+frame)%8/8) (102) |Same phase, viridis/Reds by mode (140–141) |
| Callback configuration |No animation callback |2,000 labels,50ms,blit=True (107) |200 labels,50ms,blit=False (155) |
| Movie/export |No source save/export statement |MP4 at 60 fps, save then show (110–119) |CSV plus MP4 at 20 fps, save then show (74–78,158–167) |

The exact formulas are in manuscript Chapters2–4. This table is navigation, not replacement pseudocode.

## What is mathematically shared

H and componentwise RPCO have the same formulas. S02 and S03 additionally share GRF and the centroid movement rule. The accepted S03 static AST comparison verified H/RPCO/GRF function-body identity after docstrings were removed; that checker was not rerun for the manuscript.

Given identical incoming arrays and frame label, if all S03 post-gate modes are zero, its mathematical position/velocity update equals S02's. This is a conditional source identity. Unknown initializers, extra random draws, callback schedules and different presentation settings prevent equating their historical trajectories.

All three preserve velocity and update positions in place. RPCO reduces the candidate components after the drive, not necessarily speed relative to the previous stored velocity. A contribution sign and movement direction are therefore separate.

## What is not interchangeable

The sum of two normalized pairwise directions in S01 is not the direction to the arithmetic centroid in S02/S03. Their dimension, period, regularizer and initializer also differ. No one-factor causal comparison was performed.

S01's original PNG lacks an ordered log; its seed-0 chronology is a reproduction. S02's movie lacks certified numerical states. S03's logs permit measured native displacements and callback counts, but its movie/log run identity remains formally UNLINKED. Different evidence strength is not a proven behavioral difference.

The coordinate measuring framework is not a physical container, tetrahedral faces do not carry the interactions, and none of these source equations supplies a gravity field equation or physical energy calibration.
