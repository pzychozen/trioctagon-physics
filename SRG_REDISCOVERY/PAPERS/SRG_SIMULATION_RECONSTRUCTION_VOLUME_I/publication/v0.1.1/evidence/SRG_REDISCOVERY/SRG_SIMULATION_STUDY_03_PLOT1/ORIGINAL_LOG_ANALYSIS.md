# Original numerical evidence, in recorded order

These are observations of two preserved historical CSVs. No new trajectory was generated. The exact equations are transcribed in [CONSTRUCTION.md](CONSTRUCTION.md); the scripts substitute observed states into those equations without advancing calculated states.

## Provenance and schema

| Label | Original path under SRG_REDISCOVERY | SHA-256 |
|---|---|---|
| A | OLD_MATERIAL/Simulations_Trash/Simulations_part_1/PLOT_1_tetrahedral_states_20250712_015421.csv | 6e6fc49be7dbb5ecf77aa1fbeaf5106df12c04ef3c63c29ee84c693f2ed70e74 |
| B | OLD_MATERIAL/Simulations/CSV/tetrahedral_states_20250712_015647.csv | 051f8ad8be54794fcf54171a316d9931cc65b43349634799f446c53eb1b9afe8 |

Byte-identical copies are in [originals](originals). Log A also has identical-byte aliases in OLD_MATERIAL/Simulations/CSV and OLD_MATERIAL/Simulations_Trash/Simulations_part_3. These are one evidence stream with three preserved locations, not three independent runs.

The filenames suggest 2025-07-12 01:54:21 and 01:56:47. They do not establish a timezone, exact runtime, source version or development sequence. The PLOT_1_ prefix of A is not emitted by this source's filename expression. Attribution is supported by the matching schema, eight-body state, callback labels, binary modes, energy/GRF identities and sampled full update equations. Neither file supplies a seed, initial state before callback zero, random draws, dependency versions or export receipt. The movie-to-log provenance status is **UNLINKED**, with a strong tested candidate correspondence to B described separately.

The exact header is:

    Step,Tetrahedron,X,Y,Z,VX,VY,VZ,Energy,GRF,Rule_State

Coordinates, velocities and binary modes are post-update; Energy is the post-sweep global kinetic diagnostic, repeated eight times. GRF is from the incoming velocities. Step is a supplied animation label, not a unique update key. Tetrahedron is the zero-based body number. There is no saved teleport flag, detector distance, within-sweep state, wall-clock timestamp or H column.

Both files have finite numbers, complete eight-row blocks, body IDs in order 0–7, coordinates in [0,10), binary modes in {0,1}, and identical Step/Energy/GRF across each block. No partial or corrupt block was found.

## Preserve callback chronology

Let q be the zero-based block index in physical file order. It is an analysis locator, not an original column. Header is line 1; callback q occupies physical CSV lines 8q+2 through 8q+9. Body i is on line **8q+2+i**. All anchors below use this convention.

| Property | A | B |
|---|---:|---:|
| Original data rows | 8,736 | 3,520 |
| Complete callback blocks | 1,092 | 440 |
| Unique Step labels | 200 | 200 |
| Label-zero blocks | 12 | 6 |
| Repeated (Step,Tetrahedron) rows beyond first occurrence | 7,136 | 1,920 |
| Partial/corrupt blocks | 0 | 0 |

Exact ordered segments:

| Callback range q | Step labels | A | B |
|---|---|---|---|
| 0 | 0 | Present | Present |
| 1–200 | 0–199 | Present | Present |
| 201 | 0 | Present | Present |
| 202–401 | 0–199 | Present | Present |
| 402 | 0 | Present | Present |
| 403–602 | 0–199 | Present | Only q=403–439, labels 0–36 |
| 603 | 0 | Present | — |
| 604–803 | 0–199 | Present | — |
| 804 | 0 | Present | — |
| 805–1004 | 0–199 | Present | — |
| 1005 | 0 | Present | — |
| 1006–1091 | 0–85 | Present | — |

States continue across label resets. The full-record position and GRF checks include those boundaries; selected velocity-equation checks include the first 199→0 boundary and strong reset turns. There is no justification for merging label-zero states or connecting one unique point per Step. The callback pattern is consistent with animation initialization/save/display/repeat behavior, but the original GUI event trace is missing.

The derived [A callback table](analysis/A_callbacks.csv) and [B callback table](analysis/B_callbacks.csv) retain q, CSV line anchors, Step, H argument/value, energy, GRF, speed and event counts. They supplement rather than replace the unchanged CSVs. [A chronology](visuals/A_chronology.png) and [B chronology](visuals/B_chronology.png) use callback order on their horizontal axes.

## Checks and scope of agreement

The primary checker reads every row, checks schema/block invariants, computes energy for every block, and checks position and incoming-speed GRF relations for every consecutive block. There are 8,728 checkable body transitions in A and 3,512 in B. Callback zero has no recorded predecessor, so its incoming-state recurrence and first random decisions cannot be verified.

For velocity equations, the declared sample is the union of callbacks 1–5, the final five callbacks, the maximum native-increment callback, the strongest consecutive-velocity turn, the closest-pair callback, the first label discontinuity, first decreasing-label reset, first switch and first seam. Duplicate selections are retained only once in this *check list*, never removed from data. This gives 16 sampled transitions in A and 15 in B. The exact lists and residuals are in [A equation checks](analysis/A_equation_residuals.csv) and [B equation checks](analysis/B_equation_residuals.csv).

At each selected body update, the centroid uses the observed current block's prefix of already-updated bodies and the preceding block's suffix. The checker never feeds its calculated velocity or position to another body or callback. It uses the observed post-gate binary mode; it does not reconstruct the lost random draw.

An independent stdlib csv/math implementation rechecks the original R0 samples:

- A: q=1,2,3,4,5,1087,1088,1089,1090,1091.
- B: q=1,2,3,4,5,435,436,437,438,439.

It also independently checks energy, position and GRF across the full logs. All declared checks pass absolute tolerance 1e-12. Across the two methods, maximum reported position-equation residual is 1.78e-15, sampled velocity residual 3.61e-16, energy/GRF identity residual 2.23e-16, and sampled drive/damping energy balance residual 6.67e-16. These are floating-point residuals, not a claim that the full unknown historical execution was reproduced bit for bit. The force recurrence was sampled; the position/GRF/energy relations were checked throughout.

## Movement and apparent jumps

Native increment means 0.1 times the recorded outgoing velocity. Stored-coordinate jump means the Euclidean norm of the difference between successive wrapped positions. They are different measurements.

| Measurement | A | B |
|---|---:|---:|
| Largest checked native increment | 0.061531942 | 0.060380826 |
| Its anchor | q205, body2, Step3, line1644 | q205, body5, Step3, line1647 |
| Largest stored-coordinate jump | 9.997419049 | 9.993505332 |
| Its anchor | q1038, body4, Step32, line8310 | q430, body5, Step27, line3447 |
| Native increment at that stored jump | 0.012148730 | 0.015841001 |
| Body transitions crossing a coordinate seam | 22 | 7 |
| Coordinate seam crossings | 22 | 7 |
| Recomputed source-detector flags | 8,151 | 3,129 |
| Flags without a coordinate crossing | 8,130 | 3,122 |
| Crossings missed by the detector | 1 | 0 |

Thus no checked native increment reaches even 0.062 in either file. Large plotted relocations are not large native displacements in these records. This bound covers recorded transitions, not arbitrary runs or an unknown pre-log state.

The source detector takes the *unsigned* modulo of a difference, so a small negative component becomes nearly 10. Its flags in this report are **recomputed would-flag results**: no original console transcript or logged event flag survives. The full event tables preserve coordinates, velocities, diagnostic distances and row anchors: [A wraps](analysis/A_wrap_events.json), [B wraps](analysis/B_wrap_events.json). The [A movement figure](visuals/A_movement.png) and [B movement figure](visuals/B_movement.png) compare these measurements.

Specific observations:

- A q1, body0, line10: native length 0.052418691, no seam, detector distance 9.975329933.
- B q2, body2, Step1, line20: Z goes from 0.004472603 to 9.965972877 with native length 0.054654713. Stored jump is 9.961575809. This is the earliest B seam.
- A q265, body3, Step63, line2125: Z goes from 0.001799251 to 9.998477914 with native length 0.005387221. This is the earliest A seam.
- B body7 crosses X at q409/414/418, lines3281/3321/3353, while mode stays 1 over q400–420. Native lengths are 0.055897106, 0.044266228 and 0.037032498. VX changes sign between crossings. [The focused window](visuals/B_body7_seam_window.png) shows genuine reversals and coordinate jumps separately. The next mode change is q431, outside this window.

## Switching, turns and carried motion

All callbacks have GRF>0.5, so the source gate is eligible throughout. Between recorded blocks, A has 79 mode toggles and B 33. Counts by body 0–7 are A=[11,8,8,14,16,11,2,9] and B=[1,5,2,5,10,4,4,2]. Both first recorded blocks have all modes zero. No toggle contradicts gate eligibility, but the missing uniform draws cannot be checked.

No observed toggle immediately produces an obtuse angle between the previous and outgoing velocity vectors. Across *all* transitions there are 17 such obtuse turns in A and 6 in B. This does not mean switches cannot cause later turns. B's first switch, body5 at q7, slows its inward velocity; by q9 its velocity component along the instantaneous centroid direction is negative. A body4 behaves similarly over q12–14. Exact records and derived directional components are in [episode_records.json](analysis/episode_records.json); the interpretation and table are in [TIME_SWITCH_AND_MOVEMENT.md](TIME_SWITCH_AND_MOVEMENT.md).

The strongest consecutive-vector reversal in A is body4 at q1005, Step0, line8046: cosine −0.977692 and speed 0.014863845→0.337050458. In B it is body5 at q402, Step0, line3223: cosine −0.973052 and speed 0.018644692→0.340312292. Both retain mode1. They coincide with frame-time resets, not mode toggles. This distinguishes response-sign changes, velocity direction changes and clock-driven bursts.

## Energy and shared response

| Quantity | A | B |
|---|---:|---:|
| First / last recorded K | 0.438453299 / 0.053459522 | 0.463349826 / 0.034047257 |
| Minimum K | 0.000700823 at q602 | 0.000721126 at q198 |
| Maximum K | 1.344062276 at q4 | 1.248928427 at q406 |
| Minimum / maximum incoming GRF | 0.633308909 / 0.987992109 | 0.641949259 / 0.987362064 |

At q200→201 the label changes 199→0. A energy rises 0.000922772→0.479749699 and B 0.000721817→0.473368802. The source changes H from about 0.002614 to 4.5 while retaining state. This is an externally reset drive clock combined with carried velocity and damping. It is not evidence that a conserved energy is spontaneously produced. The source has no position-dependent energy term.

## Pair relationships and limits

All 28 body pairs were checked at each stored block using minimal periodic separation D(x_j−x_i). Closest recorded pairs:

| Log | Anchor | Bodies | Distance | Velocity cosine | Relative speed |
|---|---|---|---:|---:|---:|
| A | q602, Step199, lines4820/4825 | 2,7 | 0.111912869 | 0.959590042 | 0.006143850 |
| B | q118, Step117, lines947/950 | 1,4 | 0.813987821 | −0.568814101 | 0.052972935 |

A contains a near pair with similarly directed, slow velocities at this recorded instant. B's closest pair is not aligned at its closest instant. Those observations do not establish persistent pair binding, shared historical routes or asymptotic convergence.

The checker also reports a declared descriptive screen: separation <0.1, velocity cosine >0.9, and both speeds >1e-6 at consecutive stored callbacks. No pair meets even its distance threshold. This arbitrary narrow screen is not a physical threshold and is not a rejection of approximate collective following. No delayed route-following criterion or recollection was tested. Per-pair minima are retained in analysis/A_pair_minima.json and analysis/B_pair_minima.json.

## What remains unresolved

The original initial states/RNG streams, exact source snapshots used for export, historical dependency/backend versions, and GUI causes of repeated callbacks are missing. Exact movie/run linkage is unproven. Sampled recurrence agreement is strong attribution evidence, not a complete velocity audit of every callback. Finite records do not establish long-time stability, a probability law for switching, a conserved energy, or a physical gravitational interpretation. These boundaries remain explicit for scientific review.
