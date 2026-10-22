# Construction walkthrough

Source identity: OLD_MATERIAL/Simulations_Trash/Simulations_part_2/3Dtriangles.py, 119 lines, 3,970 bytes. SHA-256: 4c53678eefd803e93a910b74e7a8096bfd5095e0d09d09c9df0e7cf514b312f1. The entire program, including recording and display, was read. All line numbers below refer to the unchanged [included source](source/3Dtriangles.py).

Original: [3Dtriangles.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_2/3Dtriangles.py:1).

## What exists

There are eight indexed centers, each with three position coordinates and three velocity components. The stored coordinates occupy [0,10) in each direction, with periodic wrapping. This is a coordinate construction, not a physical wall or containing material. There is no ninth central object: the centroid is recalculated from the eight centers.

Each center gets the same four fixed vertex offsets:

    (0.5,0.5,0.5), (-0.5,-0.5,0.5),
    (-0.5,0.5,-0.5), (0.5,-0.5,-0.5).

Four triangular faces join these offsets (lines 18–26). Adding the center position translates the tetrahedron. There is no rotation, deformation, collision detection, surface interaction, or separate vertex motion. The source comment says "normalized"; the actual vertex distance from the center is sqrt(3)/2 and edge length sqrt(2). These dimensions affect the picture, not the force.

## Initialization and parameters

| Item | Exact implementation | Source lines |
|---|---|---|
| Number and dimension | 8 centers; positions and velocities each have shape (8,3) | 9, 15–16 |
| Period | TORUS_SIZE = 10.0 in each coordinate | 8, 29–31 |
| Frame sequence | STEP_COUNT = 2000 | 10, 107 |
| Update multiplier | DT = 0.1, used in both velocity and position updates | 11, 91, 95 |
| Initial position | np.random.rand(8,3) * 10; coordinates in [0,10) | 15 |
| Initial velocity | (np.random.rand(8,3) - 0.5) * 0.2; components in [-0.1,0.1) | 12, 16 |
| Randomness | No seed specified; 24 position and 24 velocity draws; no random draws in update | 15–16, 74–104 |
| Direction regularizer | norm(diff) + 0.01 | 88 |
| H parameters | 2, 0.5, 1, 0.3, 1.5, 0.7, 1, 0.4, as expanded below | 33–42 |
| Damping | Componentwise RPCO | 44–46, 92 |
| Shared response factor | GRF = 1/(1 + mean speed), computed once per callback | 48–51, 79 |
| Display | 10-by-8-inch figure; axes 0 to 10; alpha 0.6; viridis palette | 54–71 |
| Playback / encoding | GUI interval 50 ms; MP4 save at 60 fps | 107, 113 |

The source does not assign physical units to these quantities.

## One complete callback, in execution order

1. Receive frame; assign t = frame * 0.1 (74–76).
2. Read all current velocity norms. Compute one common GRF value (79, using 48–51). Its arguments positions and t are unused: the function reads the global velocities array.
3. Compute H(t) once (82).
4. For i = 0,1,...,7, recompute the arithmetic centroid of the currently stored positions (83–85). Earlier centers have already moved in this callback; later centers have not.
5. Subtract center i from that centroid, then wrap each displacement coordinate into [-5,5) (86–87).
6. Divide the displacement by its Euclidean norm plus 0.01, and multiply by H(t) (88). This gives the variable named force.
7. Add 0.1 * force * GRF to velocity i, then apply RPCO component by component (91–92). Velocity is carried, not replaced by the force.
8. Add 0.1 * the newly damped velocity to position i, then wrap position into [0,10) (95–96). Immediately continue to the next center.
9. After all eight updates, translate each tetrahedron's faces to its new center and change its face color (99–102). Return the eight collection objects to the animation machinery (104).

The renderer sees the result of a complete eight-center sweep. It does not show the eight intermediate substeps separately.

## Exact mathematical transcription

This notation describes the existing code; it introduces no replacement equations. Let q count actual callback invocations for explanation only. The program itself does not store q. Let f_q be the frame label delivered on callback q, and x_i, v_i its incoming state.

\[
W(z)=z\bmod 10,\qquad D(z)=((z+5)\bmod10)-5,
\quad R(u)_a=\frac{u_a}{1+\log(1+|u_a|)}.
\]

\[
H(t)=2e^{-0.5t}\cos t+e^{-0.3t}\sin t+
1.5e^{-0.7t}+e^{-0.4t},\qquad
g_q=\frac{1}{1+\frac18\sum_{j=0}^{7}\|v_j\|_2}.
\]

For i in the actual order 0 through 7:

\[
c_i=\frac18\left(\sum_{j<i}x_j^++\sum_{j\ge i}x_j\right),
\qquad d_i=D(c_i-x_i),
\]
\[
F_i=H(0.1f_q)\frac{d_i}{\|d_i\|_2+0.01},
\qquad v_i^+=R(v_i+0.1g_qF_i),
\qquad x_i^+=W(x_i+0.1v_i^+).
\]

W and D operate componentwise. The centroid includes center i itself. H appears once in the velocity drive, already inside F_i; the comment at line 90 must not be read as a second multiplication by H.

The force magnitude is |H| r/(r+0.01), where r is the wrapped displacement norm. It approaches |H| at large r and vanishes at r=0. This is a regularized direction response, not an inverse-square law. A zero instantaneous force does not erase a carried velocity.

## Retained state, recording and display

The recurrent numerical state is the two (8,3) arrays. GRF, H, centroid and force are temporary values. There is no stored route, past-position array, learned path, per-object rule state, measured energy, or accumulated elapsed-time variable. The name "memory curve" identifies H in a comment; H never reads a trajectory.

The eight Poly3DCollection objects retain display geometry. Their color is viridis(((i + frame) % 8)/8), so it advances every frame and repeats after eight labels. Colors do not affect movement.

At top level, FuncAnimation is created with update, frames=2000, interval=50 and blit=True (107). No init_func or repeat override is supplied. The code immediately attempts to save tetrahedral_attractors_animation.mp4 with the ffmpeg writer at 60 fps (110–114). The path is relative to the process's working directory, which need not be the source directory. os.makedirs creates that output directory if necessary (112).

If saving raises an exception, the error is printed and plt.show() is called (115–117). After successful saving, plt.show() is also called (118–119). Neither branch resets positions or velocities. Saving invokes the update to make frames; it is not simply exporting a precomputed state log. There is no numeric trajectory export or built-in trail recording.

The script has no main guard. Importing or running it would initialize random state, create an animation and attempt a movie save. Neither was done in this checkpoint.
