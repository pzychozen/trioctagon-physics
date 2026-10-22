# Time and movement

Primary source: [3Dtriangles.py](source/3Dtriangles.py), especially 33–51 and 74–119. The exact recurrence is in [CONSTRUCTION_WALKTHROUGH.md](CONSTRUCTION_WALKTHROUGH.md).

## Four distinct notions of time

| Quantity | What the source actually does | Consequence |
|---|---|---|
| Update size DT | Fixed 0.1 in velocity and position changes (11, 91, 95) | It does not adapt to rendering speed or wall-clock time |
| H argument | t = frame * 0.1 (76, 82) | Time comes from the supplied label, not from counted state changes |
| GUI timer | interval=50 ms (107) | Nominally 20 frame events per second; actual runtime can differ |
| Saved video | fps=60 (113) | Movie time advances by 1/60 second per encoded frame |

If labels 0,...,1999 are each processed exactly once, H is evaluated at 0,...,199.9, while 2,000 update multipliers amount to 200 model-time units. This is a conditional accounting, not a recovered callback history. On that single-pass interpretation, one movie second corresponds to six model-time units. The GUI timer would nominally give two model-time units per wall-clock second. No physical calibration is specified.

The inspected movie really contains 2,000 decoded frames at 60 fps: duration 33.333333 seconds, last frame timestamp 33.316667 seconds. Its frame count does not certify that only 2,000 state-changing callbacks occurred.

## Callback time can restart while numerical state continues

The program passes a mutating update function without a separate initialization function (107). For a concrete implementation check, the locally installed Matplotlib 3.10.9 source was read, without constructing an animation:

| Library operation | Relevant installed animation.py lines | Effect with this source |
|---|---|---|
| Integer frame argument | 1704–1706 | Generates range(frames), starting at zero |
| FuncAnimation initialization draw | 1761–1782 | With no init_func, invokes the draw callback on the first frame |
| Blitting setup / interactive start | 1235–1245; 916–933 | Can perform initialization draws |
| Save | 1120–1138 | Initializes, then calls the draw/update path for each saved frame |
| Repeated interactive playback | 1442–1452; 1454–1469 | repeat defaults to True; restarts the frame sequence and initializes again |

The excerpts, their source path and library hash are saved in inspection/matplotlib_callback_excerpts.txt and inspection/environment.json. These establish present-library behavior and a real source-level ambiguity. The historical library version, backend and exact GUI event sequence were not recovered; no exact number of historical initialization callbacks is asserted.

Each extra call to update changes velocities and positions and applies damping again. Calling frame 0 twice applies H(0)=4.5 twice to successively changed states. A display restart can therefore renew the prescribed drive without renewing the random initialization. Saving followed by showing does not reset the arrays. Initialization draws are not harmless pictures of an unchanged state in this construction.

Library caching of frame labels is not a numeric trajectory record. The source provides no callback-count log from which to reconstruct total elapsed update time.

## Which calculations use time and which use state?

| Operation | Explicit inputs actually read | Type of dependence |
|---|---|---|
| H | frame * DT | Prescribed time schedule only |
| GRF | Incoming global velocity norms | Current state only; positions and t arguments unused |
| Centroid | Mixed old/new position array inside the sequential loop | Current state and update order |
| Direction and distance | Wrapped centroid-minus-center displacement | Current state and coordinate representation |
| RPCO | The velocity after adding this update's drive | Current candidate velocity; no elapsed-time argument |
| Position advance / wrapping | Old position, new velocity, fixed DT | Current state |
| Color | Object index and frame label | Display schedule only |

Positions and velocities depend indirectly on earlier calls, so state-only operations still carry consequences of the past. They do not access a saved route or an elapsed-time memory.

## H, response strength and damping

H starts at 4.5. It is not always positive: at t=3*pi/2 its cosine term is zero and

\[
H(3\pi/2)=-e^{-0.45\pi}+1.5e^{-1.05\pi}+e^{-0.6\pi}
\approx-0.03600350414.
\]

This is a scalar evaluation of the unchanged formula, not a simulated transition. Negative values reverse the centroid-directed contribution; they do not necessarily reverse the current velocity. The actual frame clock samples t on multiples of 0.1 during an ordinary pass, so this illustrative time is not claimed as an actual frame label.

For nonnegative t,

\[
|H(t)|\le2e^{-0.5t}+e^{-0.3t}+1.5e^{-0.7t}+e^{-0.4t}\to0.
\]

The envelope decays as the frame time increases, but H oscillates and its magnitude need not decrease at every frame. Resetting the frame labels also resets this schedule.

GRF lies in (0,1] for finite velocities. Increasing mean incoming speed lowers the next common drive factor; decreasing it raises that factor. GRF is computed once, so velocity changes during a sweep affect the next callback's GRF, not later objects' GRF within the same sweep. It is neither a measured retention history nor an explicit positional-stability test, despite its name and comment.

RPCO preserves each candidate velocity component's sign and reduces its magnitude unless it is zero. Its reduction becomes relatively weaker near zero. It does not force an exact stop when H is small or zero, and it need not reduce speed compared with the velocity before the new drive was added. Because components are damped by different factors, the operation can change a vector's direction as well as its magnitude.

Direction changes can arise from a changed centroid, a displacement-wrap branch change, a sign change in H, and unequal component damping. Carried velocity can delay a reversal relative to a changed drive. These are permitted mechanisms, not claims that every one is visible in this movie.

## Wrapping changes both the picture and the interaction calculation

Before wrapping, the center moves by delta x_i = 0.1 v_i^+. Its stored coordinate difference instead satisfies

\[
x_i^+-x_i=0.1v_i^+-10k_i,\qquad k_i\in\mathbb Z^3.
\]

A displayed jump can therefore be large even when the unwrapped increment is small. The video does not interpolate a periodic seam crossing, and the tetrahedron's vertex offsets are not independently wrapped or split (95–101).

There is a separate issue in the force itself: the program averages the stored wrapped coordinates, then wraps the displacement to that arithmetic average. It does not compute a circular or intrinsic periodic mean. A single center crossing the positive boundary in one coordinate contributes a -10/8 = -1.25 shift to that coordinate of the arithmetic centroid, in addition to its ordinary movement contribution. Later centers in the sweep see that changed centroid. The operation is exactly what the historical source does; no replacement mean was introduced.

Thus a boundary crossing can cause a coordinate jump in the display and a change in the interaction target. It would be incomplete to dismiss every consequence as a plotting artifact. The displacement operation also selects [-5,5), so the half-period branch is a possible discontinuity in its chosen direction.

The movie's relocation at frames 13–14 is consistent with wrapping. Exact native displacement, crossing axis and subsequent velocity response cannot be certified without the associated numerical states. Slow late screen changes likewise do not prove an equilibrium, a complete stop, or convergence to one common position.
