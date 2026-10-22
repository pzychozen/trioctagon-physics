# Start here: one original three-point simulation

Hilmir, this program builds a small world containing **three moving points**. Each has an X/Y position and an X/Y velocity. The coordinates wrap around a square: crossing one edge returns a point through the opposite edge. These are coordinate rules; the script does not draw a physical container or give the points a size or shape.

The program starts the points at random positions, with zero velocities. It then performs 500 rounds of updates. During each round, each point responds to the other two, a shared time-dependent function changes the response, and logarithmic damping reduces the updated velocity components. The points update one after another, so later points see positions already changed earlier in that round.

Positions and velocities carry forward. A separate position log keeps snapshots for drawing. **Movement never reads that log back.** Once all 500 rounds are complete, the script draws three lines joining the recorded positions and displays one static figure. It has no animation loop and no command to save a PNG, video or trajectory file.

## What we actually inspected

The complete 74-line source was read, including recording and plotting. The surviving **attractors.png** was opened and examined at its original 800×800 resolution.

![Surviving three-trace plot](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/evidence/attractors.png>)

**Caption — original image, copied without alteration.** Three blue, orange and green traces have closely aligned sections, long near-vertical lines near the middle, and curved turns in the upper-right and lower portions. The title and labels match the script's plotting code. This supports a likely association; it does not identify the exact run or establish how the image was saved.

There are no time labels, direction arrows or marked starting points. The long lines are consistent with the way this plotting code can join coordinates across a wrap seam, but their actual generating steps cannot be checked from the PNG alone. We cannot read speed, waiting, blinking or the order in which different points visited a location from this picture.

The bounded check used the existing recovery references and inventories. It found **no supported time-resolved recording or saved position log attributable to this selected script**. Other indexed videos and logs were not substituted for it or claimed to have been watched.

## Read the actual construction

[CONSTRUCTION_WALKTHROUGH.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/CONSTRUCTION_WALKTHROUGH.md>) follows setup → interactions → movement → recording → display, with exact source lines.

The review ZIP includes:

- **source/recursive_attractor.py** — the byte-identical original, not a reconstructed implementation.
- **evidence/attractors.png** — the inspected original image, byte-identical.
- **MANIFEST.json** — paths, hashes, provenance limits and preservation results.
- Both walkthrough documents.

This is one surviving implementation, not a determination of the earliest SRG program or the one behind every recollection. No new run, rebuild, proof extension or environment change was performed.

**One missing evidence item for discussion:** the original ordered position log belonging to this PNG. It would let us inspect the depicted run's chronology directly. This checkpoint stops here.

