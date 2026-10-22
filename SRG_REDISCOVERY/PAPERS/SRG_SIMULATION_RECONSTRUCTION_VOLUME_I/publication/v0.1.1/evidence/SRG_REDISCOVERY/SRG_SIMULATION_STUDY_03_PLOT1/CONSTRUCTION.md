# Complete construction of plot_1.py

The complete 167-line program was read, including its top-level file writes, animation, save and display paths. The unchanged copy is [originals/plot_1.py](originals/plot_1.py). All source line references in this document refer to that copy.

Original location: [plot_1.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_1/plot_1.py:1).

SHA-256: e13b92df8ac6df78cfee75b95dacea3b106e96bd5be9bf798cdcf39ccc5bc75c. There is no declared version, fixed seed or execution date in the source. Directory numbers do not establish development order.

## What the simulated world contains

Eight centers have three position coordinates, three velocity components and one persistent binary mode each. Positions occupy [0,10) in every coordinate, with periodic wrapping. No object represents the centroid: it is an arithmetic calculation over the centers. No physical box, wall, mass field or collision surface is implemented.

The four display offsets are (0.5,0.5,0.5), (-0.5,-0.5,0.5), (-0.5,0.5,-0.5), (0.5,-0.5,-0.5), joined into four faces (20–28). They form a fixed tetrahedron with edge length sqrt(2). Every tetrahedron keeps that orientation and size. Only its center translates. Vertex positions, face color and transparency do not enter the motion rule.

| State or quantity | Persistence and role | Source |
|---|---|---|
| positions, shape (8,3) | Carried coordinates, changed in place | 17, 125–126 |
| velocities, shape (8,3) | Carried velocity; receives drive, then damping | 18, 123–124 |
| rule_state, shape (8,) | Carried binary mode, initially all zero | 116–117, 152 |
| NumPy global RNG state | Initialization and gated mode draws consume it; no seed fixed | 17–18, 116 |
| prev_positions | Copy of incoming positions for this callback's diagnostic only | 107, 132 |
| H, GRF, centroid, diff, norm, force | Temporary calculations, not trajectory memories | 102–120 |
| energy, teleports | Recomputed diagnostics; neither feeds back into motion | 129–134 |
| CSV file | Persistent external history; the program never reads it back | 74–78, 143–147 |
| Eight collections | Persistent display objects; their geometry/colors are updated | 91–97, 137–141 |

The recurrence has 48 real-valued entries and eight binary modes, plus the external frame input and random stream. It has no stored learned route, energy reservoir, retained teleport flag, rotation state or running elapsed-time accumulator.

## Initialization and top-level side effects

1. Import NumPy, Matplotlib plotting/3D/animation, os, csv and time (1–7).
2. Set period 10, number of centers 8, frame count 200, DT=0.1 and VELOCITY_SCALE=0.2 (10–14).
3. Draw 24 position values using np.random.rand(8,3)*10. Draw 24 velocity values using (np.random.rand(8,3)-0.5)*0.2, giving components in [-0.1,0.1) (17–18). No seed is set.
4. Define geometry and helper functions (20–71).
5. Obtain a timestamp from time.strftime("%Y%m%d_%H%M%S"). Open tetrahedral_states_<timestamp>.csv in write mode and write its 11-column header (74–78). The path is relative to the process working directory. This happens before animation, even if later saving fails. The filename has no time-zone or unique-run identifier; the PLOT_1_ prefix on log A is not produced by this exact formatting statement.
6. Create a 10-by-8-inch 3D figure, axes 0–10, title "Tetrahedral Attractors with Energy and Teleport Tracking", and eight translucent Poly3DCollection objects with alpha=0.6 (81–97).
7. Define the mutating callback, then initialize all binary modes to zero (100–152).
8. Construct FuncAnimation with frames=200, interval=50 ms and blit=False (155). No separate init_func or repeat override is supplied.
9. Attempt to save tetrahedral_attractors_logic.mp4 with ffmpeg at 20 fps (158–162). Saving invokes callbacks; it is not merely exporting a precomputed trajectory.
10. Call plt.show() after either save success or failure (163–167). No numerical state is reset before display. Save exceptions are caught, but the earlier CSV setup lies outside this try block.

There is no main guard. Running or importing this module would initialize random state, write a CSV and start the animation/save machinery. This study did neither.

## One complete update, in actual execution order

| Stage | Operation | Lines |
|---|---|---|
| Shared inputs | t = frame*DT; compute GRF from all incoming velocities; evaluate H(t) | 102–104 |
| Diagnostic snapshot | Copy all incoming positions | 107 |
| For body i=0,...,7 | Recompute centroid from current stored positions | 109–110 |
| Direction | centroid − position[i]; wrap each displacement into [-5,5); compute Euclidean norm plus 0.01 | 111–113 |
| Mode gate | If GRF>0.5, draw one np.random.rand(); if it is <0.01, replace b_i by 1−b_i | 116–117 |
| Signed interaction | Multiply normalized displacement by H and by −1 if the new mode is 1, otherwise +1 | 120 |
| Velocity | Add DT*force*GRF to old velocity; apply RPCO componentwise | 123–124 |
| Position | Add DT*new velocity; wrap into [0,10) | 125–126 |
| After all bodies | Compute whole-system energy, run teleport diagnostic, optionally print events | 129–134 |
| Rendering | Translate each tetrahedron; set palette phase by (i+frame)%8/8 and palette family by its current mode | 137–141 |
| Recording | Open CSV in append mode; write eight rows in body order, all after the full sweep | 144–147 |

Earlier bodies' new positions affect later bodies' centroids during the same callback. GRF and H are shared constants for that callback. The code does not update GRF again after individual velocities change. The mode draw occurs after direction calculation and before the drive. Python's short-circuit condition means there is **no random draw** when GRF<=0.5.

## Exact mathematical transcription

Let q denote the ordered callback index used in this analysis, f_q the supplied frame label, and incoming state x_i,v_i,b_i. The program does not store q. Define componentwise operations

\[
W(z)=z\bmod10,\qquad D(z)=((z+5)\bmod10)-5,
\quad R(u)_a=\frac{u_a}{1+\log(1+|u_a|)}.
\]

\[
t_q=0.1f_q,\quad
H(t)=2e^{-0.5t}\cos t+e^{-0.3t}\sin t+1.5e^{-0.7t}+e^{-0.4t},
\quad g_q=\frac{1}{1+\frac18\sum_j\|v_j\|_2}.
\]

For i in order 0 through 7,

\[
c_{q,i}=\frac18\left(\sum_{j<i}x_j^++\sum_{j\ge i}x_j\right),
\qquad d_{q,i}=D(c_{q,i}-x_i),\qquad r_{q,i}=\|d_{q,i}\|_2.
\]

If g_q>0.5, the code draws U_{q,i} with np.random.rand(). Let F_{q,i}=1 when that draw is <0.01, otherwise 0. If the gate is closed, set F_{q,i}=0 without a draw. Then

\[
b_i^+=b_i\mathbin{\mathrm{XOR}}F_{q,i},\quad
a_{q,i}=0.1g_qH(t_q)(1-2b_i^+)\frac{d_{q,i}}{r_{q,i}+0.01},
\]
\[
u_{q,i}=v_i+a_{q,i},\qquad v_i^+=R(u_{q,i}),\qquad
x_i^+=W(x_i+0.1v_i^+).
\]

a is the velocity contribution, not an additional implemented variable or proposed mechanism. The sign belongs to the **post-gate mode** stored in the current CSV block. H is multiplied exactly once.

The centroid includes body i and averages wrapped Cartesian coordinates. Wrapping the displacement afterward does not make this an intrinsic periodic mean. The response magnitude before DT and GRF is |H|r/(r+0.01); it is a regularized direction response, not an inverse-square law.

## Exact diagnostics and record meanings

The function compute_energy ignores its positions argument:

\[
K_q=\frac12\sum_{i=0}^{7}\|v_i^+\|_2^2+0.
\]

The zero is the literal potential_energy placeholder (57–61). There is no implemented position potential, mass parameter, conservation test or energy feedback. K is a whole-system, post-sweep quantity, repeated in every row. Summing Energy across the eight rows multiplies the same diagnostic by eight.

The source's diagnostic distance is

\[
T_{q,i}=\|W(x_i^+-x_i)\|_2.
\]

It prints a tuple when T>1 (64–71, 132–134). This is **not** D, not a minimal periodic distance, and not the native increment norm. wrap_position's docstring mentions teleport detection, but the function itself merely takes a modulo. The detector has no effect on the recurrence and its flags/distances are not exported to the CSV.

Each row is

    Step, Tetrahedron, X, Y, Z, VX, VY, VZ, Energy, GRF, Rule_State

Step is f_q. Coordinates, velocities and Rule_State are post-update. Energy is post-sweep K_q. GRF is from the incoming velocities before the sweep. All eight rows share the same Step, Energy and GRF. Tetrahedron is zero-based 0–7.

The palette family indicates mode: viridis for 0, Reds for 1. Within either family, the phase advances with (i+frame)%8. It does not indicate velocity direction, physical temperature or per-body energy. No numeric energy or teleport annotation is drawn on the movie itself.
