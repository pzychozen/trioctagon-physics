# Comparison with simulation 1

This comparison was made after reading all of 3Dtriangles.py and inspecting its associated movie. It compares the two original programs. Neither was executed here, and the seed-specific findings of the prior replay are not used to claim behavior of the eight-center program.

Included sources: [simulation 1, recursive_attractor.py](source/recursive_attractor.py), 74 lines; [simulation 2, 3Dtriangles.py](source/3Dtriangles.py), 119 lines. Source 1's original location is [here](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_2/recursive_attractor.py:1). Line references in the table are S1 / S2.

| Mechanism | Simulation 1 | Simulation 2 | Status and implication |
|---|---|---|---|
| State dimension | 3 centers in 2D; 6 position and 6 velocity entries (7, 10–11) | 8 centers in 3D; 24 position and 24 velocity entries (9, 15–16) | Changed size and dimension |
| Initialization | Positions random in [-1,1); velocities zero (10–11) | Positions random in [0,10); velocities random in [-0.1,0.1) (15–16) | Random starting velocity introduced; neither source fixes a seed |
| H | Prescribed damped oscillatory function (17–27) | Same expression and constants (33–42) | Preserved exactly; no trajectory-memory input in either |
| Update clock | One explicit loop: 500 labels, t=step*0.05 (38–40) | Animation labels: 2000, t=frame*0.1 (76,107) | Changed scheduler and nominal window; callback repeats/initializations can mutate state |
| Step multiplier | 0.05 in both velocity and position advance (6,54,56) | 0.1 in both (11,91,95) | Changed; not a harmless change of plotting speed |
| Interactions | Sum of regularized directions to the other two centers (45–51) | Regularized direction toward arithmetic centroid of all eight, including self (85–88) | Pairwise sum removed; centroid mechanism introduced |
| Distance regularizer | 0.001 (51) | 0.01 (88) | Changed short-distance response |
| Shared speed factor | Absent | GRF from mean incoming speed (48–51,79,91) | New global state-dependent modulation |
| In-place order | 0,1,2; earlier positions already updated when later force is calculated (43–57) | 0,...,7; centroid recomputed from mixed positions inside loop (83–96) | Sequential dependency preserved |
| Velocity retention | Add drive to old velocity, damp, move (54–56) | Same order (91–96) | Preserved, with different drive |
| RPCO | u/(1+log(1+abs(u))), componentwise (30–31) | Identical (44–46) | Preserved exactly |
| Periodic coordinates | Period 2; same wrapper for position and pair displacement, range [-1,1) (34–35,50,56) | Period 10; position range [0,10), displacement range [-5,5) (29–31,87,96) | Wrapping preserved in kind, changed in scale and centroid use |
| Numerical history | Stores all 500 post-sweep positions (14,57–62); not the initial state | No trajectory array or state-file writer | Explicit trajectory history removed |
| Rendering | Three static 2D connected trajectories, with legend (65–74) | Eight translated tetrahedra in animated 3D view; colors change every frame (54–71,99–107) | Polyhedral geometry and time-dependent coloring introduced |
| Recording/display | plt.show(); no built-in file save (74) | Attempts MP4 save, then show on success or failure (110–119) | Video export introduced; saving itself invokes updates |

The changed interaction is mathematically substantial. In S1, each neighbor contributes a separately wrapped and separately normalized vector:

\[
F_i^{(1)}=\sum_{j\ne i}\frac{D_2(x_j-x_i)}{\|D_2(x_j-x_i)\|+0.001},
\quad D_2(z)=((z+1)\bmod2)-1.
\]

In S2, positions are first averaged and only the resulting centroid displacement is wrapped and normalized:

\[
F_i^{(2)}=H(t)\frac{D_{10}(c_i-x_i)}{\|D_{10}(c_i-x_i)\|+0.01},
\quad D_{10}(z)=((z+5)\bmod10)-5.
\]

Both use the mixed state produced by their own sequential loops. In S1, H multiplies the summed force in the velocity update; in S2 it is already included in F above. Averaging before wrapping and normalizing is not algebraically equivalent to summing wrapped, normalized neighbor vectors. S2 is therefore not simply S1 drawn in three dimensions.

Implementation differences establish different rules, initial-state families and recording behavior. They do not establish that S2 has stronger attraction, more collective motion, faster convergence, greater stability or new path inheritance. The period, step size, number of centers, initialization, force construction and response factor all change together, and no controlled behavioral comparison was run.

What the recovered evidence does add is a time-ordered movie associated with S2, including a visible early relocation and much slower late screen change. Its lack of numeric state records limits what can be measured from it. The review checkpoint ends with these construction and evidence distinctions.
