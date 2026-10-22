# SRG simulation research ledger

Scientific lead: GPT. Author/research direction: Hilmir Frímann Halldórsson. Research engineer: Codex. Initialized 2026-10-22 from the [research charter](RESEARCH_CHARTER_v0.1.md) and accepted study packages; this is a linked index, not a new archive inventory.

Paths below are relative to SRG_REDISCOVERY unless linked absolutely. “Accepted baseline” follows the user's charter; it is not a new independent approval. File bytes and evidence class are distinct: an ORIGINAL artifact can have only an ATTRIBUTED source/run relationship. Current filesystem dates and directory numbers do not establish development chronology.

| ID | Target | Review state | Main package |
|---|---|---|---|
| SIM01 | recursive_attractor.py | ACCEPTED BASELINE per charter | [Construction01](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/START_HERE.md), [Replay01](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/START_HERE.md) |
| SIM02 | 3Dtriangles.py | ACCEPTED BASELINE per charter | [Construction02](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_02/START_HERE.md) |
| SIM03 | plot_1.py | **IN REVIEW — GPT/Hilmir** | [Study03](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_STUDY_03_PLOT1/START_HERE.md) |

## SIM01 — three centers, pairwise interaction

**Source:** OLD_MATERIAL/Simulations_Trash/Simulations_part_2/recursive_attractor.py; SHA256 847819ec381e200d9008395175342ec138e52ab3180a4f599b4db1cb91ae42d3. No additional historical source alias confirmed in the focused recovered index. Package copies are preserved copies, not independent versions. No source seed/version/date declaration establishes the historical run.

**Original evidence:** OLD_MATERIAL/Simulations_Trash/Simulations_part_2/attractors.png, 800×800 PNG, SHA256 72776de5e6228f4c4a0e2ef43d804f479bf8db80af6884e492e9ccbc3053d651. ORIGINAL/ATTRIBUTED: title/content support association; original seed and ordered numerical chronology are missing.

**Construction:** Three 2D positions plus three 2D velocities; random positions in [-1,1), velocities initially zero. Sum of two wrapped pairwise displacement responses with denominator norm+0.001. H and componentwise RPCO; in-place order 0,1,2; DT=0.05; 500 direct loop sweeps with t=0–24.95; period 2 wrapping. Positions/velocities carry, post-sweep position history is saved in memory. Static connected trails and plt.show; no source CSV or movie export. No later random draws in the source.

**Accepted reproduced evidence:** SRG_SIMULATION_REPLAY_01 uses one new legacy seed 0, 500 sweeps, 501 boundary states and 1,500 within-sweep events. This is REPRODUCED, not a restoration of attractors.png's lost run. Its same-seed reference check matched all 500 position snapshots and final velocities bit for bit. Numerical records:

- replay/states.csv: SHA256 4cdc156fd4cc777220528805a85dee65298b8c44b723e3766a65809ffb6b6ff9.
- replay/trajectory.npz: SHA256 b14901adc4612a3e557615fd0833f58ccb953d3f84f8823f1121a5bef5b0c5e1.
- replay/within_sweep.jsonl: SHA256 af43911ab0dc3fa7bda5ae96e418ccac1e93da30839124abeb6a3514cb4b80ff.

These paths are inside SRG_SIMULATION_REPLAY_01; its MANIFEST.json and REPLAY_VALIDATION.md retain full provenance. Nothing from that replay was rerun for SIM03.

**Observed anchors / limits:** In the accepted seed 0 replay, points 1/2 approach to about 4.42435e-5 after sweep 169, then separate to about 0.001583 at 170; point 0 moves the other way along the same visible diagonal. No position seam crossing occurs in its 1,500 point updates. Largest native increment about 0.03457; final velocities remain nonzero. Overlapping trails do not establish simultaneous coincidence or delayed route inheritance. The historical PNG alone does not establish these chronology claims.

**Relationships:** Preserves H/RPCO names into the later-studied family, but pairwise 2D motion differs from centroid 3D motion. Path-inheritance compatibility/initializer studies remain separate conditional screens, not substitutes for this reconstruction or proofs of remembered behavior.

## SIM02 — eight centers, centroid interaction

**Source:** OLD_MATERIAL/Simulations_Trash/Simulations_part_2/3Dtriangles.py; SHA256 4c53678eefd803e93a910b74e7a8096bfd5095e0d09d09c9df0e7cf514b312f1. No additional historical source alias confirmed in the focused index; source date/seed/export environment unrecovered.

**Original evidence:** OLD_MATERIAL/Simulations_Trash/Simulations_part_1/tetrahedral_attractors_animation.mp4; SHA256 4f90ce9fc384b134b68b5a64424ef3e05d364153d4e70efdd1596c0b8c937dd3. H.264 movie, 2,000 decoded frames, 60 fps, 33.333 s. ORIGINAL/ATTRIBUTED: filename/title/geometry match source; exact generating source/run chain and numeric states are missing. Accepted copy/inspection in SRG_SIMULATION_CONSTRUCTION_02/evidence.

**Construction:** Eight 3D positions/velocities, 48 real entries. Random positions [0,10), velocity components [-0.1,0.1); no subsequent randomness or binary modes. Sequential 0–7 arithmetic centroid of mixed old/new wrapped coordinates, minimal displacement wrapping, norm+0.01, shared H and incoming-speed GRF, RPCO after drive, DT=0.1. Period 10; fixed tetrahedral display offsets. Frame labels 0–1999 drive H, GUI interval 50 ms, blit=True, movie 60 fps. Save/show/repeat can mutate state beyond encoded-frame count. No numeric log or trajectory-memory feedback; display colors cycle by index+frame.

**Observed anchors / mathematical limits:** Movie frames 13→14 relocate a shape, consistent with wrapping; late screen movement is small. Missing numeric history prevents exact velocity/jump or full callback certification. Source proves carried velocity, coordinate-dependent centroid and componentwise damping; it does not establish equilibrium, physical gravity or a bound collective object.

**Relationships:** Compared with SIM01 after independent construction study. SIM03 shares the centroid update and H/RPCO/GRF bodies, adds stochastic mode signs and logging, and changes nominal frame count/blitting/video rate. Study number does not assert historical precedence.

## SIM03 — binary response switching and original logs

**Source:** OLD_MATERIAL/Simulations_Trash/Simulations_part_1/plot_1.py; SHA256 e13b92df8ac6df78cfee75b95dacea3b106e96bd5be9bf798cdcf39ccc5bc75c. 167 lines; no additional historical source alias confirmed in focused index. Filename dates of logs suggest 2025-07-12 but do not establish timezone, source revision or export pairing.

**Original evidence and hashes:**

| Artifact / original location | SHA256 | Attribution |
|---|---|---|
| part_1/tetrahedral_attractors_logic.mp4 under OLD_MATERIAL/Simulations_Trash | 0289d8e5a084e53f536183ad87d83b4a4c5ab972851bb61922a699406623203a |200frames,20fps,10s; strong source association; exact run join UNLINKED |
| part_1/PLOT_1_tetrahedral_states_20250712_015421.csv under OLD_MATERIAL/Simulations_Trash | 6e6fc49be7dbb5ecf77aa1fbeaf5106df12c04ef3c63c29ee84c693f2ed70e74 |A:8,736rows/1,092callbacks; strong equation/schema attribution |
| OLD_MATERIAL/Simulations/CSV/tetrahedral_states_20250712_015647.csv | 051f8ad8be54794fcf54171a316d9931cc65b43349634799f446c53eb1b9afe8 |B:3,520rows/440callbacks; strong equation/schema attribution |
| part_1/Tetrahedron_7_position_trace_with_teleport_events.png | bf6dfb6ec1da4a9ceb56c9107b654671492576945a1b62426625b18ec99fe798 |Historical postprocessing strongly attributed to B; chart generator missing |
| part_1/Tetrahedron_7_GRF_over_time.png | 8f3c93d74ec1c03f97d70320b5c760953dca805b3bd3f1e967d54d6789a5b137 |Same limitation; Energy is global, despite body7 title |

Last two part_1 paths also mean OLD_MATERIAL/Simulations_Trash/Simulations_part_1. LogA identical-byte aliases are OLD_MATERIAL/Simulations/CSV/PLOT_1_tetrahedral_states_20250712_015421.csv and OLD_MATERIAL/Simulations_Trash/Simulations_part_3/PLOT_1_tetrahedral_states_20250712_015421.csv; not independent runs.

**Construction:** SIM02's 48 real state entries plus 8 binary modes, initially 0. Same random coordinate/velocity initialization; gated fresh draw per body if GRF>0.5, toggle if draw<0.01. Post-toggle sign multiplies the centroid interaction before adding it to carried velocity. Same sequential order, period 10, DT=0.1, H/RPCO/GRF. Labels 0–199, 50 ms GUI, blit=False, 20 fps MP4. CSV records post-sweep positions/velocities/modes/global K and incoming GRF, eight rows per callback. Unsigned-modulo “teleport” diagnostic only prints; no feedback. No saved routes or physical potential.

**Observed anchors:** Repeated 0–199 passes retain state; A's 1,092 and B's 440 callbacks cannot be reduced to 200 updates. B body 5 flips at q7, line63 and has outward radial velocity by q9, line79. B body 7 crosses X at q409/414/418, lines3281/3321/3353 while mode1 persists over q400–420. Largest checked native increments A=0.061532/B=0.060381; seams 22/7; detector would flag 8,151/3,129. A's closest pair 2/7 at q602, lines4820/4825, d=0.111913, has aligned slow velocities at that instant. No path-inheritance claim.

**Verification / unresolved:** All-row energy/position/GRF checks and 31 sampled velocity transitions agree within 1e-12; independent check of 20 R0 samples included. All 200 movie frames decoded, with selective consecutive visual review. Eight sampled movie images closely match B q=f+1, but exact source/run/export linkage remains UNLINKED. Historical body7 charts apparently mix Step trace axes with callback event axes. Missing initializer/RNG, backend history and chart generators remain explicit. No new simulation was run.

**Review:** IN REVIEW. Current package, equations, source/evidence copies, scripts and preservation records reside in SRG_SIMULATION_STUDY_03_PLOT1. See its ORIGINAL_LOG_ANALYSIS.md, ORIGINAL_MOVIE_REVIEW.md and MANIFEST.json. No acceptance or publication is implied by ledger inclusion.

## Boundary and next checkpoint

No next simulation is selected here. GPT and Hilmir review SIM03 first. Fixed-grid, glyph/echo, amplitude-coupled and production-kernel models remain distinct. Accepted papers and indexes are preserved; eventual publication is a separately approved task.
