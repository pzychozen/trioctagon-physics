# Actual motion and four kinds of grouping

**REPRODUCED seed-1618 setting · 120 stable IDs · boundaries 0–200**

The original construction draws six spatial populations, then repeatedly updates each point using its currently selected local neighbors. It does not move rigid six-part objects. The replay shows rapid early concentration into smaller groups, continuing small late motion, and transient links between two supplied populations. The [fixed-scale snapshots](figures/F01_world_snapshots.png), [geometry/movement figure](figures/F03_geometry_and_movement.png) and complete saved arrays support these statements.

All source locations below refer to the immutable [original program](handoff/originals/srg_condensate_breaking.py). All measurements here are analyses of REPRODUCED coordinates; they do not add geometry to the old aggregate evidence.

## What makes one point move

Lines 155–203 increment the integer pass and build one graph from incoming positions. Each point selects up to five nearest non-self neighbors within strict distance 6. A simultaneous local stage computes the unweighted mean of neighbor differences and adds `.05*lap + .15*tanh(lap)`. The amplitude exchange uses incoming distances and amplitudes, two weight-normalization stages, a squared-frequency-difference factor and each assigned frequency's sine. A common H multiplier follows. Ascending-ID fusion then moves each point toward a center of its selected neighbors, using their current coordinates and fixed post-H amplitudes. Compression follows; actual decaying Gaussian noise is added; completed displacement and observers are recorded.

There is no coordinate wrapping, boundary reflection, retained-velocity force or velocity damping here. V is the latest completed displacement, used by the GRF observer, not consumed by the next step. The source's stored `.08699` is unused. The initialized coordinate range is not a wall. H and the bound L are prescribed by integer time, not geometric objects or accumulated memories. See original lines 42–54, 61–103, 105–153 and 155–266.

At pass 1, mean lengths of the actual local, fusion and noise increments are .203511, .00562931 and .0168112 world units; mean net step is .209809. At pass 200 they are .00156648, .0000274445 and .00496697, with mean net step .00511879. The local movement dominates the initial recorded scale; the noise increment is the largest of these mean stage lengths at the endpoint. These are operand descriptions, not ablation results. Norms of stages do not add as scalar magnitudes to the net movement. [Stage data](analysis/stage_movement.csv).

## Group membership is not one quantity

| Structure | Definition | Observed result |
|---|---|---|
| Supplied populations P0–P5 | Fixed blocks `id//20`, original lines 677–699 | Six blocks of 20; used for analysis, never added as an interaction label |
| Assigned frequencies | Fixed original choice from four numerical values | Counts 29,36,28,27; each population happens to contain all four |
| Interaction graph | Directed row selections from incoming X, strict radius 6 and cap five | Always 600 selected edges here, no empty rows; weak components 5–14 and strong components 13–27 over the 200 incoming graphs |
| Spatial observer | Average-linkage clustering at cut distance 2 on completed X, original 216–223 | 49 groups at pass 1; ten at every pass 16–200; exact memberships also remain unchanged over those 185 observations |

Weak graph components ignore edge direction; strong components require mutual directed reachability through selections. We represent a partition by its member sets, canonically labeling each by its smallest point ID. Changing SciPy's arbitrary numeric cluster label cannot create a false membership-change result.

The graph at boundary b supplies pass b+1. The captured graphs cover b=0,…,199; observer memberships cover completed b=1,…,200. No extra graph at b=200 was computed and no pass 201 was executed. [Same-boundary comparisons](analysis/same_boundary_memberships.csv) use b=1,16,50,199, with graph from pass b+1 and observer from pass b. [Figure F02](figures/F02_group_memberships.png) compares b=16 and 199 directly. The separate [chronology table](analysis/graph_chronology.csv) explicitly labels incoming versus completed boundaries.

At incoming boundary 0 there are five weak components, because cross-population selections connect P1 and P4. At boundary 199 there are thirteen weak and fourteen strong components. The completed observer still reports ten spatial groups at boundary 200. Even after observer membership stabilizes, 35,682 directed-edge additions/removals are counted across all consecutive incoming graph comparisons over the run. This total counts changed binary entries across time, not unique pairs or independent events. The graph continues changing late: the graph supplying pass 200 differs from the previous incoming graph in 244 entries.

The ten stable observer groups split the supplied populations as follows:

| Supplied population | Stable IDs | Sizes of spatial-observer groups from pass 16 onward |
|---|---|---|
| P0 | 0–19 | 10 + 10 |
| P1 | 20–39 | 20 |
| P2 | 40–59 | 9 + 11 |
| P3 | 60–79 | 20 |
| P4 | 80–99 | 9 + 11 |
| P5 | 100–119 | 13 + 7 |

No late observer group mixes supplied populations in this replay. A population can contain several graph components or multiple compact pieces even where the thresholded observer calls it one group. A group count and a fixed member list do not establish exact point coincidence, rigid geometry, independence or convergence. Full member sets are in [selected partitions](analysis/SELECTED_PARTITIONS.json) and [supplemental readback](analysis/SUPPLEMENTAL_READBACK.json).

## A transient connection: IDs 34, 39 and 97

The only direct cross-population selections are:

| Row reading a neighbor | Executed passes retaining that selection | Number of visits |
|---|---|---:|
| 39 → 97 | 1–3 | 3 |
| 97 → 34 | 1–6 | 6 |
| 97 → 39 | 1–8 | 8 |

This is 17 selection visits across three unique directed pairs, all between P1 and P4. No direct cross-population edge appears in incoming graphs supplying passes 9–200. Finite horizon alone did not make all supplied populations disconnected at initialization; the source comment “Each cluster only sees itself” at line 693 does not hold for these early actual selections.

Point 97 starts at approximately (−5.97170, −.946781, 5.79831). Its z coordinate first decreases, then increases while x continues toward the P4 grouping: at boundary 8 it is (−4.15099, −1.16281, 5.13300), at 16 it is (−1.78667, −1.36076, 6.13502), and at 200 it is (.394820, −1.52310, 6.37897). Its total sampled path length is **8.11917**, the largest among the 120 stable IDs; it ends in observer group with minimum ID 83, entirely from P4. This is a turn in recorded motion, not a coordinate wrap or point-identity exchange.

Selection can cease before a pair leaves radius 6 because the nearest-five cap also applies. The captured distances/adjacency expose that distinction. [Figure F06](figures/F06_transient_cross_population_contact.png) shows the x–z projection and exact selected-edge intervals; y is omitted explicitly. [Cross-selection data](analysis/CROSS_POPULATION_SELECTIONS.json), [distance history](analysis/cross_population_distance_history.csv) and [complete selected tracks](analysis/cross_population_tracks.csv) retain the actual values. Losing an edge is not a measured causal experiment: no trajectory with that edge removed or retained was run.

For fixed selections, finite-horizon fusion has no global/band-center bridge across disconnected weak components. Common time schedules and use of one RNG stream are not an extra geometry-dependent center. This source property does not imply permanent dynamic independence of populations or establish what would happen beyond the observed horizon.

## Geometry and persistent late movement

For any specified fixed membership G, new geometric measurements use its vector arithmetic center c and

`Rg = sqrt(mean_i ||X_i−c||²)`, `diameter = max_(i,j) ||X_i−X_j||`.

No alignment, fitted shape or inferred surface is used. Full-field Rg changes from **8.31680** at initialization to **8.07151** at pass 200; diameter changes from **22.39876** to **19.02194**. The whole-field arithmetic center moves **.223801** from its initial position. These whole-field numbers remain large because the supplied populations remain separated.

| Population | Initial Rg | Final Rg | Final diameter | Center displacement from initialization |
|---|---:|---:|---:|---:|
| P0 | 2.50832 | 1.55558 | 3.13435 | .613349 |
| P1 | 2.45767 | 1.00993 | 2.11683 | .269736 |
| P2 | 2.13184 | 1.24062 | 2.51307 | .211871 |
| P3 | 2.33977 | .0669491 | .166309 | .305873 |
| P4 | 2.87175 | 1.35205 | 2.73501 | .898055 |
| P5 | 2.93003 | 1.80620 | 3.80287 | .444551 |

The original printed `spread=np.std(pos_k)` pools all coordinate entries around one scalar mean. It is preserved verbatim in stdout and the analysis table; it is not any Rg above. For example P3's endpoint original spread is 3.23881 while its proper centered Rg is .0669491. The former includes the population's location relative to coordinate components. [Population geometry](analysis/population_geometry.csv) provides both explicitly.

All 120 points have nonzero recorded displacement at pass 200. The mean step there is .00511879 and maximum .0110598; the mean over passes 151–200 is .00604926. Mean cumulative path is **3.48176**, with range **1.86716–8.11917**. Small late changes may be invisible on fixed world-scale snapshots. Overlapping plotted markers do not mean merged identities; connecting sampled points with lines does not imply a continuous-time law between updates. [Selected stable-ID paths](analysis/selected_point_tracks.csv), [whole geometry](analysis/geometry.csv), and [fixed endpoint-group geometry traced backward](analysis/endpoint_group_geometry.csv) distinguish these quantities. The latter uses endpoint member lists at earlier times as a diagnostic; it does not claim those were already observer groups then.

## Amplitudes and the moving compression bound

All saved signed R values are positive, ranging .00291918–.293883 across boundaries 0–200; all captured B and Q are also positive. Thus positive inward fusion coefficients describe this particular replay. There were no empty rows and no failed second normalization guards. The per-frequency sine, local exchange, H multiplier, and compression stages are retained separately in the records. At pass 1 the H factor is 1.0299332763; at pass 16 it is .9999852242; at pass 200 the floating factor is exactly 1.0. The recorded H itself is then small and nonzero. A programmed decay is not an autonomous memory process.

None of the 24,000 pre-compression inputs activates a lower or upper log clip; none is zero or raised from a nonzero input to the lower floor. The smallest log-space margin to either bound is about **3.03207**. The original signed `exp(clip(log(abs(Q)+1e−9),−L,L))` still runs. Inactivity of the clipping thresholds does not remove the epsilon or floating exp/log evaluation, and it does not justify retroactive conclusions about other drivers or an unrun breathing-off control.

At the endpoint signed amplitudes span about .07769615–.20064584. Mean amplitudes grouped by fixed frequency remain different, with recorded local exchange and label-specific modulation in [amplitude stage data](analysis/amplitude_by_frequency.csv). Assigned labels are not discovered frequency bands or proof of emergent golden spacing. [Figure F05](figures/F05_metrics_and_amplitudes.png) relates the original aggregate readouts to the frozen comparison without promoting their names into physical claims.

The endpoint driver prints all 15 pairs of population centers as `SEPARATE`, meaning only that their distances exceed 3 (actual range 10.1837–17.1597). Its diversity threshold `> .01 means independently evolving` is source wording, not a proved independence test. No energy, ground-state functional, physical force law, infinite-time condensate or convergence theorem is supplied or established by this replay.
