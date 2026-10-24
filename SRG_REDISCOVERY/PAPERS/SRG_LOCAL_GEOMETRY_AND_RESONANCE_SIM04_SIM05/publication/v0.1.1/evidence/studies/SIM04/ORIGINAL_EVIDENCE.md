# SIM04 — original evidence, chronology and observations

IN REVIEW, 23 October 2026. The source/run relation is **strongly ATTRIBUTED**, not a certified original execution identity. This file separates that provenance judgment from direct readings of the saved data.

## 1. Evidence identities and attribution

The exact archive was resolved through R0's `external_and_selected_sources.json` and `march_archive_verification.json`, not a filename search across the archive. It is:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\research_files\sources\Zenodo_research\19023429\simulations.zip`

SHA-256: `731b980fa2f09a8f433c4ff92bd0fcbb455e563790bdf85c556b111b36abd477`.

Each selected member agrees byte-for-byte with the archive, its existing extraction under `research_files/archive_members/Zenodo_research/19023429/simulations.zip/`, and R0's `selected_sources/MARCH_19023429/` copy. Those multiple copies are one source chain, not independent observations. Exact paths and sizes are in [SOURCE_PROVENANCE.json](SOURCE_PROVENANCE.json).

| Unchanged member | Bytes | SHA-256 |
| --- | ---: | --- |
| [srg_seed_explorer.py](originals/srg_seed_explorer.py) | 29,820 | `0c8ec661624bd100212b29d75dd184cacf2adbf5d173584e3817460d9fd6ea10` |
| [deep_trajectory.csv](originals/deep_trajectory.csv) | 150,582 | `7bcb5ceb18a65977c3c13b7c848962d897775a93aa0a2e3a6713c339ac3a4ee3` |
| [pass_metrics.csv](originals/pass_metrics.csv) | 4,196 | `f6d4484d654b4f88f1fa32024f6f88b3f7065ff67192d52d7124223f9e15d063` |
| [SRG_Deep_Analysis.md](originals/SRG_Deep_Analysis.md) | 10,705 | `8418cf8236a9139093c40575ab1c2a1a77a7120ee1d227cccf5ebf2c29beacd0` |

**ORIGINAL** means preserved historical bytes, including historical claims that may not be supported. The script and commentary date themselves March 14, 2026. ZIP timestamps are retained in [archive_members.json](analysis/archive_members.json); neither those timestamps nor later extraction times certify execution time, author identity or software version.

The source's deep driver specifies the same two filenames, schema, 50 IDs, initialization ranges, pass count and metric definitions. The co-packaged commentary §5 explicitly discusses this 50-glyph, seed-2038 trace and its top-ID changes. The stored metrics exactly match the corresponding states, V exactly matches successive positions, and the conditional resonance formula agrees throughout. Together these support **strong source/run attribution**. The CSV contains no source hash, invocation command, package versions or RNG checkpoint. No initialized random stream was regenerated. Exact source revision at original execution and the historical meaning of seed 2038 remain **MISSING/AMBIGUOUS**.

The driver's comment “Recreate the conditions from the original research” (source L604) is original prose. It does not establish that this March run recreates an earlier July run or any remembered event. This package adds no new **REPRODUCED** run.

## 2. Saved chronology and schemas

`deep_trajectory.csv` has columns `Pass,Glyph_ID,X,Y,Z,Resonance,VX,VY,VZ`. Its original row order is exactly 21 consecutive blocks: passes 0–20, each with IDs 0–49 in order. There are no missing keys, duplicates, nonfinite numeric values or inserted reordering. Pass 0 contains initialized positions/resonance and zero velocities, consistent with constructor recording at source L82–89. It must not be discarded as a spare frame.

For a specific saved row, the one-based CSV line, including the header, is **50 × Pass + Glyph_ID + 2**. Pass 0 is lines 2–51; pass 20 is lines 1002–1051. Glyph IDs are persistent array indices, not generated names or physical particle types.

`pass_metrics.csv` has 20 rows, labels 1–20, with twelve values per label: `R_mean,R_max,R_std,Rg,kinetic_energy,n_corridors,coherence,top_seed_id,top_seed_R,top_seed_x,top_seed_y,top_seed_z`. Pass p is CSV line p+1. Every value aligns to the same numbered post-update state. No aggregate pass 0 was originally exported; pass-0 diagnostics in our figures are new calculations on the saved initial block.

This program uses a plain Python loop, not a drawing callback. Unlike the Volume I third program, these files contain no repeated pass labels. The `Pass` integers support an ordered 20-update window, not a clock in seconds. The CSV has no wall-clock timestamps or between-pass samples.

| Quantity | Initial pass 0, newly summarized | Original metric at pass 1 | Original metric at pass 20 |
| --- | ---: | ---: | ---: |
| Radius of gyration | 5.386371733 | 5.217452026 | 4.186458315 |
| Mean absolute resonance | 0.047764939 | 0.049214453 | 0.050282090 |
| Maximum absolute resonance | 0.099707052 | 0.093168045 | 0.060837880 |
| Resonance population std | 0.028332747 | 0.024172739 | 0.007223414 |
| Source coherence | 0.406829744 | 0.508828545 | 0.856342244 |
| Mean squared displacement | 0 by initialization | 0.065856610 | 0.004374372 |
| Reported echo pairs | 0 | 0 | 96 |

**OBSERVED:** spread decreases at every stored transition, while resonance narrows without becoming uniform. The maximum resonance decreases even as coherence rises. The mean changes and there is no recorded exact scalar conservation. These are statements about this window, not an asymptotic theorem.

## 3. Identifiable movement episodes

**A. Ranking changes, then remains stable while the point keeps moving.** Glyph 3 has the highest |R| at passes 0–2; glyph 40 at passes 3–5; glyph 38 at passes 6–20. For example, pass 3 / glyph 40 is trajectory line 192 and metric line 4. Pass 6 / glyph 38 is trajectory line 340; pass 20 / glyph 38 is line 1040. The latter moves from (−2.558493, 3.825752, −1.214059) to (−1.799225, 3.733941, −1.836565): endpoint displacement 0.986118749, sum of its saved step lengths 1.031366622. It remains highest for **15 saved passes**, inclusive of 6 and 20. The source does not promote it to a leader or attractor object.

**B. The first echo observation is another pair.** At pass 6, glyphs 5 and 43 are 0.324779240 apart and have echo score 0.830711274. At pass 7 they are 0.230854325 apart, their resonance difference is 0.004150495 and the score is 0.869788748, exceeding .85. These are the first pair reported by the observer. Trajectory anchors are lines 307/345 at pass 6 and 357/395 at pass 7; metric line 8 records one corridor. [first_corridor_history.csv](analysis/first_corridor_history.csv) shows the entire pair chronology. The threshold crossing does not turn a new force on. No exponential growth law is fitted to the later corridor count.

**C. The final top three are close, but no new entity exists.** Final IDs 38, 23, 8 are at trajectory lines 1040, 1025 and 1010. Their three-dimensional distances are 0.056274321 (38/23), 0.033963906 (38/8) and 0.067736245 (23/8). This supports the March commentary's finite observation of a close top-three group, with 0.07 as a rounded upper bound. It does not establish exact coincidence, a special three-point mechanism, a bound object or equilibrium. The complete 50-point field still has maximum pair distance 8.397737161. The last pair distances also fluctuate; a late increase is visible in Figure F03.

**D. The local graph becomes less connected while the global statistics smooth.** These are **new OBSERVED diagnostics derived from historical positions**, not original saved columns. Rebuild the directed five-neighbor graph exactly as the source does. Ignoring direction, it has one connected component at passes 0–4, two at passes 5–19 and three at pass 20. Directed strongly connected component counts rise from one to seven. The last weak groups contain 21, 23 and 6 points; exact membership is in [graph_components.json](analysis/graph_components.json). The six-point group is IDs 10,15,27,30,33,47.

At pass 20 there are 11 newly selected directed edges out of 250 relative to pass 19, the largest turnover in this short record. Glyph 6, for example, changes neighbors from {4,12,35,40,42} to {4,35,40,41,42}; its recorded coordinates move from (2.845846,−0.897225,1.771734) to (2.825469,−0.999973,1.794428). Source distances at each endpoint, not an imposed grouping rule, determine that change. The graph formed on saved pass 19 supplies the 19→20 update; the graph formed on saved pass 20 is a diagnostic here, because no pass-21 state survives. The global fusion term still spans all points, so this local disconnection does not make the full dynamics independent between groups.

**E. A large turn can be a small movement.** Glyph 47's last two stored displacement vectors turn by 155.34°, with norms only 0.01919 and 0.03343. A large angle is not a large jump or new transition mechanism. The source's local term, fusion term and unsaved noise jointly determine the next movement; no separate cause is identified from the angle alone. [episodes.json](analysis/episodes.json) retains this ranked diagnostic and its small-motion context. No wrapping exists to reinterpret it as a coordinate seam event.

## 4. Visual evidence and its limits

The exact March archive contains 38 members, with no PNG/JPEG/SVG/GIF/MP4/PDF member. Its recovered extraction has the same relevant files, and the complete selected source contains no plotting, rendering or animation calls. R0's coverage lists images and movies for other older programs but supplies no certified visual join to this deep trace. This bounded study therefore found **no attributable original figure or movie for this run**. It did not restart a wider archive inventory or infer linkage from a similar filename.

The following are **new visualizations of historical data**, produced by [plot_historical_records.py](plot_historical_records.py). PNG and editable SVG are included. Lines join recorded samples; they do not reconstruct unobserved between-pass paths. Positions are unwrapped raw coordinates. Projection overlap is not three-dimensional coincidence. No coordinate normalization is applied to disguise contraction.

![Positions on fixed scales](figures/F02_position_views.png)

**F02.** The same 50 points at passes 0, 10, 20 in XY and XZ projections, with fixed coordinate and resonance-color scales. Gray lines connect saved states only. Local concentration occurs in several spatial regions, while some paths overlap in projection.

![Rank and pair episodes](figures/F03_identifiable_episodes.png)

**F03.** A: resonance histories of IDs that become top-ranked. B: distances between the final top-three IDs, logarithmic distance axis. C: first observed echo pair, IDs 5/43, crossing the fixed .85 threshold. D: all-pair corridor counts. Neither rank nor corridor count changes the update.

![Source terms and graph observations](figures/F04_terms_and_neighbors.png)

**F04.** A: deterministic local/fusion terms and unexplained position residual at each independently supplied recorded input, plotted as RMS vector norms. These are not an additive decomposition of RMS norms: vector terms can oppose each other. B: prescribed memory/sine factors relative to one. C: directed edge turnover between saved-state graphs. D: graph component counts; the global fusion coupling remains. [F01](figures/F01_recorded_overview.png) supplies the four global traces shown in START_HERE. Full captions and inputs are in [FIGURE_REGISTER.json](FIGURE_REGISTER.json).

## 5. Historical interpretation versus supported evidence

| March commentary claim | Assessment in this selected program/record |
| --- | --- |
| Negative resonance is inverted into positive values | Contradicted by the implemented signed RPCO; negative inputs retain sign. No alternate “paper” mode is executed here. |
| `lambda_vp` may affect geometric/Z modulation | This stored parameter is unused in this source. Changing it does not change these equations. The active .001 sine multiplies resonance, not Z coordinates. |
| Echo corridors drive convergence | Corridors are an observer; the update never reads their count or list. Local neighbor exchange and global fusion are the causal expressions present. |
| `higher_polyhedra` establishes lattice formation | For this 13-point active subset the label is unconditional, including pass 0. No polyhedral fit is performed. |
| Glyph 38 “holds its position” / has “locked” | Stable highest rank, continued motion: 0.986 endpoint displacement after pass 6. No locking test appears in this driver. |
| Final seed triad lies within .07 | Supported as a finite distance observation for IDs 38,23,8, not as fusion into one object or an exact stationary state. |
| Universal attraction / all seeds always merge | Not established by this window or its source comments. Local graph splitting and remaining spread caution against reading a single-object endpoint into the data; they do not prove universal nonmerger either. |
| Equilibrium / exponential corridor phase | Twenty transitions do not establish an equilibrium or growth law. Schedules, noise and changed neighborhoods remain present. |

These corrections preserve the historical text unchanged. They assess only claims directly relevant to this selected source and saved run. The tower, zeta, dark-field, fixed-grid and proposed master-equation work is not reopened.
