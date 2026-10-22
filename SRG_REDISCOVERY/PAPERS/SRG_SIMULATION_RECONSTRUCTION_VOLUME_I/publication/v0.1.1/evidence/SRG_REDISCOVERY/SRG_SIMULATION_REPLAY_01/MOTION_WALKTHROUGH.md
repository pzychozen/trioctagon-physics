# NEW REPLAY — motion walkthrough
SRG_SIMULATION_REPLAY_01 · 22 October 2026

This account follows one seed-0 trajectory of the original three-point program. It explains recorded movement, not a recovered historical run, a path-inheritance proof or a physical identification of the interaction.

## How the original construction was replayed

The authority is the byte-identical [sandbox source](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:1>), lines 1–74. NumPy and Matplotlib are the original dependencies. Setup at [lines 5–11](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:5>) gives three two-dimensional positions, zero initial velocities, 500 sweeps and dt=0.05. The only new initializer choice is the legacy seed 0 required by this work order.

| Point index | Initial X | Initial Y | Initial velocity |
|---|---:|---:|---|
| 0 / Attractor 1 | 0.0976270078546495 | 0.43037873274483895 | (0,0) |
| 1 / Attractor 2 | 0.20552675214328775 | 0.08976636599379373 | (0,0) |
| 2 / Attractor 3 | −0.15269040132219058 | 0.29178822613331223 | (0,0) |

The names 0, 1 and 2 retain array identity. They do not designate a permanent leader or follower.

[H(t), lines 16–27](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:16>), supplies one shared, time-only gain for each sweep. It is not an accumulated path memory. [Lines 45–51](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:45>) subtract each other point's current position, wrap that difference, divide by its norm plus 0.001 and add the two contributions. Both other points participate; self-comparison is skipped.

[Lines 54–56](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:54>) then add the interaction increment to the existing velocity, apply componentwise logarithmic damping, move using dt times that damped velocity, and wrap the resulting position. The exact original NumPy operations and constants were retained.

The position array changes immediately:

| Moving point | What its calculation sees |
|---|---|
| 0 | Points 1 and 2 before this sweep's moves |
| 1 | Point 0 after its move; point 2 before its move |
| 2 | Points 0 and 1 after their moves |

The observer records copies only; none feeds back into these calculations. The original [lines 57–62](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/replay/source/recursive_attractor.py:57>) supply end-of-sweep positions for plotting; the new observer additionally records all intermediate point updates and all velocities.

## Reading the chronology

**step** is the original zero-based loop index, 0–499. **Sweep number** is step+1. **Sₙ** means the state after n complete sweeps, with S₀ the original initializer. **Event ID** is 3×step+point+1: event 1 updates point 0, event 2 point 1, event 3 point 2; event 1500 completes S₅₀₀.

The recorded t and H describe the clock used for that sweep. Thus S₁ was produced using t=0, and S₅₀₀ using t=24.95. These are model-clock arguments, not video timestamps. No invented within-sweep time is assigned to the three sequential moves.

The contact sheets have four columns: before point 0, after point 0, after point 1, after point 2. Each row retains fixed axes. The first column uses the **upcoming** sweep's clock; its event number identifies the last completed move. Repeated boundary snapshots across rows therefore have the same positions but a new upcoming clock.

The full precision records are **replay/trajectory.npz**, **states.csv** and **within_sweep.jsonl**. JSONL line number equals event ID. **selected_events.csv** contains the 18 actual updates in the two inspected windows. Numbers below are rounded for reading.

## Window 1 — the first three complete sweeps

**Selection:** steps 0, 1 and 2, chosen before the run. **Locators:** events 1–9, S₀–S₃; within_sweep.jsonl lines 1–9.

![NEW REPLAY: first three sweeps](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/visuals/opening_sequence.png>)

The first row makes the order concrete. These are the position arrays actually read before each point moved:

| Event / moving point | Input position of P0 | Input position of P1 | Input position of P2 |
|---|---|---|---|
| 1 / P0 | (0.097627, 0.430379) | (0.205527, 0.089766) | (−0.152690, 0.291788) |
| 2 / P1 | **(0.091899, 0.417776)** | (0.205527, 0.089766) | (−0.152690, 0.291788) |
| 3 / P2 | **(0.091899, 0.417776)** | **(0.194666, 0.102361)** | (−0.152690, 0.291788) |

Bold entries have already changed during the sweep. P0 moves down and slightly left. P1 moves up and left. P2 moves mostly right. Their first native increments are approximately (−0.005728,−0.012602), (−0.010860,+0.012595) and (+0.014857,−0.000239).

P0's first interaction sum is about (−0.570665,−1.433338). Its pre-damping velocity is (−0.128400,−0.322501); damping reduces that to (−0.114561,−0.252047). The latter velocity is retained. On the next sweep it is the incoming velocity, not zero.

Rows two and three show the same actual 0→1→2 dependency while those retained velocities continue to change. After three sweeps the positions are:

| State | P0 | P1 | P2 |
|---|---|---|---|
| S₃ / event 9 | (0.069625,0.375318) | (0.156272,0.144779) | (−0.089119,0.289637) |

All three move immediately in this run. This is an observation of these first sweeps, not a test of a separate waiting criterion.

## Window 2 — a near-meeting, with different retained velocities

**Selection:** smallest simultaneous torus separation among the 500 end-of-sweep records and the three unordered point pairs; ties use earliest state, then pair order. This descriptive rule was fixed before the run. It selected P1/P2 at S₁₆₉. The inspected window is steps 167–169, events 502–510, with the incoming state at event 501.

![NEW REPLAY: near-meeting in actual update order](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/visuals/closest_pair_sequence.png>)

At the center sweep, step 168, t=8.4 and H≈0.09211406. The recorded input arrays are:

| Event / moving point | Input position of P0 | Input position of P1 | Input position of P2 |
|---|---|---|---|
| 505 / P0 | (−0.616916,−0.493081) | (−0.612788,−0.488968) | (−0.613851,−0.490021) |
| 506 / P1 | **(−0.618936,−0.495102)** | (−0.612788,−0.488968) | (−0.613851,−0.490021) |
| 507 / P2 | **(−0.618936,−0.495102)** | **(−0.612342,−0.488524)** | (−0.613851,−0.490021) |

P0 moves farther down-left even though its current interaction sum points up-right. Its incoming velocity is about (−0.047484,−0.047507); the positive response reduces that motion, but does not reverse it during this update. Its outgoing velocity remains (−0.040387,−0.040422).

P1 and P2 move up-right. Their current interaction sums both point down-left, but their carried positive velocities survive the update and damping. P1's outgoing velocity is about (0.008924,0.008872); P2's is about (0.030815,0.030547). **The direction of today's interaction alone does not tell us today's movement: the incoming velocity matters.**

After P2 moves, the two positions are close enough that the green marker largely covers the orange marker at this image scale. Both points still have separate records:

| Completed state | P1–P2 distance | What the next frames clarify |
|---|---:|---|
| S₁₆₈ / event 504 | 0.001496078692 | Approaching the close observation |
| S₁₆₉ / event 507 | 0.0000442435133 | Nearly overlapping markers, distinct coordinates and velocities |
| S₁₇₀ / event 510 | 0.001583353616 | The pair has separated again |

This minimum is scoped to the **recorded end-of-sweep states**. It is not a proof of the closest possible continuous-time encounter, nor a claim of exact collision or coincidence. We do not interpolate an unrecorded meeting.

The same diagonal can therefore contain overlapping trails, a close pair moving up-right, and a third point moving down-left. It is not enough to infer a common itinerary or a following mechanism from the final line picture.

## Wrapping and the apparent long diagonal

The predeclared first-boundary-crossing window has **no event to inspect** in this run. All 1,500 raw updated positions remain inside the native square, and all 3,000 interaction comparisons have zero lattice shift. The wrapping functions were nevertheless executed exactly as in the source; they were not removed.

Recorded coordinates range approximately from X=−0.707514 to 0.205527 and Y=−0.583649 to 0.430379. No position jumps across a domain edge.

The largest native increment is event 20, P1 in step 6 (t≈0.30): approximately (−0.0253510,+0.0234985), length **0.03456666287**. The corresponding displayed-coordinate change agrees up to normal floating-point rounding. Across the entire run, the maximum residual between the screen change and the native increment is about 1.36×10⁻¹⁶.

![NEW REPLAY: seam-aware paths](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/visuals/seam_aware_paths.png>)

The seam-aware drawing omits a connector whenever a recorded update wraps to another coordinate cell. Here it removes none. Its curves therefore match the source-style drawing. The long diagonal is an accumulation of many recorded moves, **not one enormous step or a wrap connector in this run**.

Both drawings still connect discrete samples by straight segments. They do not certify the intervening continuous path. Unlike a trajectory jump, marker occlusion can simply hide one color behind another: event 507 is an observed example in our rendering. No point was removed from the state.

## What the full record adds

![NEW REPLAY: simultaneous separation and native increments](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_REPLAY_01/visuals/movement_over_time.png>)

The upper graph measures simultaneous separation at each completed sweep; the lower graph measures each point's actual dt×outgoing-velocity increment. They show repeated approach and separation and generally smaller later movement, details obscured by the accumulated trails.

The stored gain changes sign seven times in this finite run. H is still the original prescribed time function, not a learned response. The interaction, incoming velocity and damping all remain present; no ablation or alternative run was used to attribute a whole episode to a single component.

At S₅₀₀, the three positions are approximately (−0.629388,−0.506839), (−0.663740,−0.537922) and (−0.590551,−0.467473). Their velocities remain nonzero. Stopping after 500 sweeps is the source's loop limit, not a detected equilibrium.

## Evidence limits and stopping point

The complete source-style static drawing omits the initial state, matching the original position_log convention. The frame sheets and optional HTML viewer additionally show the captured initial state and within-sweep observations. All plotted vertices and current-point markers come from saved records; arrows and line joins are visual connections, not invented intermediate states.

Both sheets were inspected in chronological panel order, together with the complete path and time plots. The HTML contains all recorded events, but its controls were not browser-validated: the tool rejected local-file preview, and no workaround was used. The inspected PNGs provide the required reviewable chronology without executing Python.

This replay uses a new fixed initializer; it does not reproduce or explain the exact generating history of the surviving original PNG. No gravity, path inheritance, permanent leader roles, trail memory or hidden mechanism is inferred. **The single authorized trajectory and its fidelity comparison are complete. No next simulation or work order follows.**

