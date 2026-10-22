# Construction walkthrough: recursive_attractor.py

This is a three-point motion program followed by a static drawing stage. Its world, its evolving state and its picture are different parts of the construction.

All line numbers below refer to the complete, byte-identical [packaged source](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:1>), **source/recursive_attractor.py**. The authoritative original is **SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_2/recursive_attractor.py** in the repository. No line was executed or imported during this inspection.

## A. Set up the world

[Lines 1–14](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:1>) import NumPy for arrays, random initialization and numerical functions, and Matplotlib pyplot for the eventual figure. There are no local imports or external input files. No dependency installation or version change was needed for this review.

The simulated objects are three rows in two arrays:

| Native name | What it contains | Role |
|---|---|---|
| positions | Three pairs of X/Y coordinates | Where the points currently are |
| velocities | Three pairs of velocity components | Motion retained from earlier updates |
| position_log | Initially an empty list | Recorded positions for the final drawing |

There are no separately simulated triangles, surfaces, trail objects or role assignments. Array indices 0, 1 and 2 identify the points throughout; the legend later calls them Attractor 1, 2 and 3.

The setup is explicit:
~~~python
timesteps = 500
dt = 0.05
num_attractors = 3
positions = np.random.rand(num_attractors, 2) * 2 - 1
velocities = np.zeros((num_attractors, 2))
~~~
These statements are at lines 5–11, with comments and blank lines between them. NumPy supplies six pseudorandom coordinates using its current random-generator state. Scaling puts each coordinate in [-1,1). The comments abbreviate this as [-1,1]; the implemented wrapping also chooses the half-open interval. No seed is set, no original initial array is saved separately, and there are no additional random draws in the movement loop.

The boundary rule is [TGMO, lines 33–35](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:33>):
~~~python
return np.mod(pos + 1.0, 2.0) - 1.0
~~~
It wraps each coordinate with period two. An opposite edge is a continuation in these coordinates, not a reflecting wall. The script uses this rule for both relative comparisons and updated positions. It does not render a three-dimensional torus.

There are 500 complete rounds, each using dt=0.05. The clock supplied to the response function runs from 0 to 24.95 in increments of 0.05; the 500 increments amount to 25 model-time units. The source supplies no physical unit or conversion to viewing time.

## B. Decide what influences movement

[H(t), lines 16–27](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:16>) is called a “REFU memory curve” in its comment. Operationally, it is a prescribed function of the current scalar time. It combines exponentially weighted cosine and sine terms with two more decaying exponentials. Its four amplitude/decay pairs are defined and used inside H.

At the start of each round, [lines 38–40](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:38>) compute t=step*dt and h_val=H(t) once. All three points use that same h_val. H does not read previous positions, another point's itinerary or position_log. Its size and sign multiply the current interaction response; the name “memory curve” does not make it a stored history.

For each point i, [lines 43–51](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:43>) reset net_force to a zero two-vector and visit the other two indices. Self-comparison is skipped. Each contribution is built in this order:

1. Subtract this point's current position from the other point's current position.
2. Apply TGMO to that difference. Interactions therefore compare positions through the wrapped coordinates, including across opposite edges. At an exact half-period tie, the modulo rule selects −1 in that coordinate.
3. Divide the wrapped difference by its Euclidean length plus 0.001, and add it to net_force.

The 0.001 keeps the denominator nonzero even for coincident positions; such a pair contributes the zero vector. Each contribution is a distance-adjusted direction toward the other point before the common gain is applied. No mass, collision size, learned rule or saved route enters this calculation. The variable is named net_force, but the source supplies no physical calibration identifying it with gravity or another physical force.

All declared parameters and helper functions in this small script have operative uses. In particular, new_positions is not unused and is not a simultaneous-update buffer: it collects copies for recording, as described below.

## C. Advance the points in their actual order

A round begins with the existing positions and velocities. The inner loop runs **0, then 1, then 2**. It overwrites the position array immediately:

| Point being updated | Other positions used by its interaction sum |
|---|---|
| 0 | Old positions of 1 and 2 |
| 1 | New position of 0; old position of 2 |
| 2 | New positions of 0 and 1 |

Each point's own position remains its incoming position until its own movement line. This table is a symbolic reading of the code, not a generated trajectory. The common clock does not change between these three updates.

The three operative movement lines are [54–56](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:54>):
~~~python
velocities[i] += dt * h_val * net_force
velocities[i] = RPCO(velocities[i])
positions[i] = TGMO(positions[i] + dt * velocities[i])
~~~
First, the newly calculated response is **added to the velocity already carried by that point**. Zero velocity is an initialization condition, not something restored every round.

Second, [RPCO, lines 29–31](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:29>), divides each velocity component by 1+log(1+its absolute value). This reduces the magnitude of a nonzero component and preserves its sign. It operates on X and Y separately, not by dividing the entire vector by a function of its length. The damping is applied after the response has been added.

Third, the point moves using that damped velocity multiplied by dt, then its new position is wrapped. The next point's interaction sees this changed position. After point 2 is finished, the round ends. The next round starts from these updated arrays.

There is no waiting gate, event-triggered freeze, role switch or convergence-based stop in this script. The loop stops after the declared 500 rounds. The point's velocity carries dynamical history; that is separate from storing an ordered route.

## D. Record what happened

At the start of a round, [line 42](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:42>) creates an empty new_positions list. Immediately after a point moves, [line 57](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:57>) appends **positions[i].copy()** to that list. The copy freezes the coordinates so later mutations cannot rewrite that saved value.

After all three points have moved, [line 59](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:59>) appends their three copied positions to position_log. Although the copies were taken one by one, later points do not overwrite earlier points' rows. The completed entry therefore contains the positions at the end of that whole round.

[Line 62](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:62>) converts the accumulated list to an array. If the script completes normally, its shape is (500,3,2): 500 post-round observations, three stable point indices and two coordinates.

| Retained or recorded item | What actually happens |
|---|---|
| Current positions and velocities | Persist as the next round's dynamical inputs |
| step, t, h_val | Advance or are recalculated for each round |
| net_force, diff | Recalculated for each point/comparison |
| new_positions | Recreated each round solely to assemble the record |
| position_log | Accumulates positions; is read later only by the plot |
| Initial positions | Not included as a separate first log entry |
| Velocity/force/time histories | Not appended or exported |

Log entry 0 belongs to the round that evaluates H at t=0, **after** all three points have moved. Entry 499 belongs to the last round, which evaluates H at t=24.95. These associations follow from loop order; the log has no explicit timestamp column.

Nothing in the movement calculation reads position_log or the old new_positions lists. There is also **no file export of this in-memory log**. Its existence during execution does not establish that a historical trajectory file survives.

## E. Turn the log into a picture

The rendering section is [lines 64–74](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:64>). It runs only after the numerical loop has completed.

A new figure is requested at 8×8 inches. For each point, this line takes its 500 recorded X/Y pairs:
~~~python
plt.plot(position_log[:, i, 0], position_log[:, i, 1], label=f'Attractor {i+1}')
~~~
This is [line 67](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/source/recursive_attractor.py:67>). It joins successive stored coordinates into one plotted line per point—499 connecting segments if all 500 observations are present. The unlogged initial position is not an extra first vertex. The drawing adds straight connections between samples; those display connections are not additional simulated states.

Lines 68–73 set the matching title, X/Y labels, legend, grid and equal coordinate scaling. No color, point marker, start/end marker, arrow, time annotation or fading rule is specified. The three displayed colors depend on Matplotlib's active style/color cycle. No fixed X/Y limits are specified; the displayed axis extent is not the definition of the simulated coordinate domain.

**This program has no animation loop, frame callback, interval setting or video writer.** Line 74 calls plt.show() once. A plotting backend may provide a window with viewing controls, but this script does not attach callbacks that advance the three points while the figure is displayed. The full history is already drawn.

The plot uses stored **wrapped** coordinates directly. If consecutive observations lie on opposite sides of a seam, plt.plot still connects them with an ordinary line across the flat axes. The script neither splits that line at the seam nor unwraps coordinates. Such a long displayed connector need not represent travel through every interior point on that line.

There is no savefig, CSV/NumPy export or other explicit output-file write in the complete source. It therefore does not establish how attractors.png was saved. A manual figure save or a different wrapper is possible, but neither is documented here.

The setup, simulation and display calls are at top level, with no main guard. Importing the file would execute them. The review did not import it. A future reproduction would require NumPy, Matplotlib and an appropriate display backend; exact regeneration of this PNG would additionally require its actual run state and relevant rendering configuration. No environment reproduction or new run was attempted.

## F. Connect the source to what is actually visible

**Inspected evidence:** the original attractors.png, opened in full at 800×800 pixels. Its byte-identical copy is **evidence/attractors.png**. No crops, enhancement, new plots, extracted video frames or interpolation were made.

![Inspected original static plot](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_01/evidence/attractors.png>)

**Caption.** Three colored traces on X/Y axes; matching title and legend; closely aligned upper curves; long near-vertical central connections; separate curved turns and branches. This is one static image, with no temporal annotations. The image is likely associated with the selected script; exact source-run identity and saving method remain unknown.

| Visible feature | Source connection | What cannot be read from it |
|---|---|---|
| Title “Recursive Attractor Trajectories under REFU/TGMO/RPCO” | Exact title at line 68 | A title alone does not prove which execution produced the PNG |
| Blue, orange and green lines labeled Attractor 1–3 | Three plot calls and labels, lines 66–71; no explicit colors | Stable legend labels do not assign leader/follower roles |
| Closely aligned curves between roughly (0.14,0.99) and the upper-right region | Each line connects one point's recorded positions, line 67 | Apparent overlap does not establish equal states, traversal direction or visit order |
| Small turns near X≈0.65–0.74, Y≈0.45–0.58; distinct lower branches around Y≈−0.55 to −1 | Curved appearance comes from successive line segments | Individual update times or exact coordinates are not recoverable reliably from these pixels |
| Long near-vertical lines around X≈0.08–0.14, spanning near Y=−1 to +1 | Wrapped stored positions, line 56, are connected without seam splitting, line 67 | Seam joins are a supported explanation the code permits, not a verified identification of these specific transitions |
| Grid, X/Y labels and axis ticks extending beyond some occupied coordinates | Lines 69–73; no fixed plot limits | Display margins are not new space accessible to the simulated points |

Coordinate descriptions are approximate readings of the image, not digitized data. No motion, blinking or timed jump was observed: the inspected evidence is static.

For any apparent jump, this source distinguishes three things. A wrapped coordinate can change abruptly at an edge; the rendering can join the resulting endpoints across the flat picture; and a timed display could introduce observation effects. The first two mechanisms exist in this script. The third has no simulation-animation machinery here. With no associated timed record, this inspection cannot decide which event another recollection refers to, and does not dismiss it as a plotting effect.

### Bounded check for a recording or saved log

The prior recovery was used as a locator, not as a replacement for the source or image:

- **SRG_PATH_HISTORICAL_EVIDENCE.md**, H1 at line 19, associates this script with this image and reports no located three-point numeric log or seed.
- **SRG_PATH_EQUATION_MAP.md**, E1, identifies the same recurrence and position-only plotting output.
- **R0_SOURCE_RECOVERY/source_manifest.json**, entries beginning at lines 1017 and 1031, indexes the selected PNG and script with hashes matching today's originals. Its indexed video entries provide no supported link to this script.
- **R0_SOURCE_RECOVERY/data_inventory.json** indexes three same-folder numeric text outputs: refu_memory_curve.txt, rpco_field_values.txt and tgmo_orbit_values.txt. Their listed columns are t/H(t), X/Y/Field and X/Y/Z respectively; they are not an indexed three-point ordered position_log. The selected script does not load any of them.
- **R0_SOURCE_RECOVERY/SRG_R0_REPORT.md**, §5.1, links the documented trajectory CSVs to other models, including eight-body recordings. They were not attached to this program.

These were targeted reads of existing indexes and provenance descriptions. No new archive inventory was made. No video was played or claimed to have been watched, and no unrelated trajectory rows were treated as evidence for this script. No authentic time-resolved record directly attributable to this selected program was found in this bounded check. That does not prove that no such record exists elsewhere.

## G. Execution order is not development history

The 74 source lines establish the execution order described above. Original comments identify “REFU memory curve,” “RPCO damping,” “TGMO toroidal field wrapping” and “Plot attractor trajectories.” They provide these names and immediate code roles, not a dated account of their invention.

This script contains no author/date/version statement or explanatory development note. The recovered catalog also records no declared source date or established version beyond its content hash. Filesystem timestamps were not used to infer which idea came first. No directly attributable record consulted here establishes why these constants were chosen or what motivated a preceding or subsequent version.

Accordingly, this walkthrough does not identify the earliest SRG, assign permanent experiencer/interpreter/builder roles, or turn the source names into claims about physical forces, learning or stored paths. It explains this one surviving implementation.

## The complete construction in one flow

**Import NumPy/pyplot → create three random positions and zero velocities → repeat 500 times: calculate the shared clock gain, update points 0 then 1 then 2 using current wrapped comparisons and carried/damped velocities, copy their resulting positions into the log → convert the log to an array → draw three complete lines → show one static figure.**

The review copies preserve original bytes; originals and existing Git state were checked before and after preparation, with only this new untracked task directory added. MANIFEST.json records identities, associations and package contents. No simulation, rebuild, prior proof extension, source repair, dependency change, commit, push or publication occurred.

**Missing evidence for discussion:** the original ordered position_log for the pictured run. No follow-on task or reproduction is underway.

