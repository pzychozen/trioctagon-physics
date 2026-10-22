# SRG_SIMULATION_CONSTRUCTION_02

Hilmir, this program places eight moving points in a three-dimensional coordinate space and draws a tetrahedron around each point. The tetrahedra keep their shape and orientation. Their corners do not calculate the movement: the program moves their centers, carrying a velocity from one update to the next.

Each point responds to the average position of all eight points. They move one after another, so a point later in the update sees the positions already changed by earlier points. A prescribed function called H changes the strength and sign of this response with the animation's frame time. A second factor reduces the response when the group is moving faster. Damping then reduces each component of the resulting velocity before the point moves.

A surviving 33.33-second movie strongly matches this source: its filename, displayed title, eight shapes, 2,000 frames and 60 fps agree with the program. The inspected images show early movement, a sudden screen relocation between frames 13 and 14, and much slower visible change later. Several shapes become crowded in the projection, while others remain visibly separated. This is evidence of changing arrangements, not proof that the objects merge or follow a common historical path.

Two details make the movie easy to misread. Colors change every frame, so a color does not permanently identify an object. Also, a point that crosses a coordinate boundary is placed on the opposite side. A large screen jump therefore need not mean a large movement through the periodic coordinate space. The code's arithmetic average of wrapped positions adds another effect: crossing a boundary can also change the target used in subsequent interaction calculations.

The clock needs care too. H receives the animation frame label multiplied by 0.1; the program does not store a continually increasing elapsed-time variable. Animation initialization, saving, and repeated display can call the update again or restart its frame labels while retaining the positions and velocities. The saved movie does not recover the complete callback history.

**This checkpoint explains the existing construction. Neither historical program was run.** Inspection decoded an existing movie and read source/library code. No simulation, search, kernel change, staging, commit, push or publication was performed. Work stops here for GPT and Hilmir's review.

Read the package in this order:

1. [CONSTRUCTION_WALKTHROUGH.md](CONSTRUCTION_WALKTHROUGH.md) — what exists and the complete update, including its exact equations.
2. [TIME_AND_MOVEMENT.md](TIME_AND_MOVEMENT.md) — the clock, changing response, retained velocity and boundary effects.
3. [VISUAL_EVIDENCE.md](VISUAL_EVIDENCE.md) — provenance, inspected frames, observations and limits.
4. [SIMULATION_01_COMPARISON.md](SIMULATION_01_COMPARISON.md) — source differences from the three-attractor program, separated from behavioral claims.

The actual source is copied without alteration in [source/3Dtriangles.py](source/3Dtriangles.py). The comparison source is also included. The unchanged historical movie is [evidence/tetrahedral_attractors_animation.mp4](evidence/tetrahedral_attractors_animation.mp4). Newly extracted inspection sheets and full-resolution stills sit beside it; they are not newly simulated evidence.

[MANIFEST.json](MANIFEST.json) records input and package SHA-256 hashes. [inspection/preservation_after.json](inspection/preservation_after.json) records the comparison with the pre-work baseline. Small inspection scripts are included so the media extraction and source checks can be audited. The ZIP contains the complete review package, excluding only the ZIP itself.

Scientific lead: GPT. Investigator: Codex. Construction checkpoint: 2026-10-22.
