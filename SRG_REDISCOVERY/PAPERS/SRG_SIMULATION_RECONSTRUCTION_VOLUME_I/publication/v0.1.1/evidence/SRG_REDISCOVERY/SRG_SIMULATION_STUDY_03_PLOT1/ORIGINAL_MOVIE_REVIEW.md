# Original movie and attributable historical figures

The movie and two historical charts are preserved without alteration. All new stills, contact sheets and comparison images are labelled as inspections or drawings of already-recorded states. No animation callback or historical program was executed.

## Movie identity and inspection coverage

Original: OLD_MATERIAL/Simulations_Trash/Simulations_part_1/tetrahedral_attractors_logic.mp4 under SRG_REDISCOVERY. Copy: [originals/tetrahedral_attractors_logic.mp4](originals/tetrahedral_attractors_logic.mp4).

SHA-256: 0289d8e5a084e53f536183ad87d83b4a4c5ab972851bb61922a699406623203a.

The file is 176,442 bytes, H.264, 1000×800 pixels, 200 decoded frames at 20 fps, duration 10 seconds. Frame indices in this package are zero-based; f/20 is the encoded presentation time, with the last frame at 9.95 seconds. This is not the program's t=0.1*frame clock. No frame-to-callback identity is assumed merely from these counts.

Source association is strong: plot_1.py declares this exact movie name (158), 200 labels (12), 20 fps (161), the exact displayed title (86), eight translucent tetrahedra, axis range 0–10, and a viridis/Reds mode palette (137–141). The title is “Tetrahedral Attractors with Energy and Teleport Tracking.” A targeted search of recovered Python sources found the literal output name in plot_1.py. Filename alone is not the attribution argument.

All 200 frames decoded successfully. All are included as full-resolution PNGs in visuals/movie_frames, with hashes in [movie_inspection.json](analysis/movie_inspection.json). Ten captioned contact sheets cover every frame; [movie_overview.png](visuals/movie_overview.png) samples 16 frames.

Direct visual review covered the overview; consecutive sheets 0–19, 20–39, 80–99, 120–139 and 180–199; full-resolution frames 0,1,6,199; and the eight-frame original/recorded-state comparison panel. This is selective frame-by-frame review, not a claim that every decoded frame was manually inspected or that an uninterrupted playback was watched.

## What is visible

| Encoded frames / times | Direct observation | Interpretation and limit |
|---|---|---|
| 0→1 / 0.00→0.05 s | A shape near the lower right is absent there in the next frame, with a corresponding shape near the upper right; other shapes move little | A screen relocation consistent with periodic coordinate wrapping. The movie alone does not measure its native 3D increment |
| 0–19 / 0.00–0.95 s | Initially dispersed shapes move, while their ordinary palette phases cycle; a red/pink shape appears by frame6 | Source palette family encodes mode; phase encodes frame+body. Color change is not an object birth or instantaneous reversal |
| 20–39 / 1.00–1.95 s | The geometry changes more gradually; another shape adopts a red shade around frame34 | Consistent with another binary-mode transition under the candidate B correspondence; not a certified numeric movie join |
| 80–99 / 4.00–4.95 s | Movement is less visually pronounced than at the opening; red and ordinary colors continue cycling | Small visible movement does not establish exact rest |
| 120–139 / 6.00–6.95 s | The collection occupies a more compact projected region than at the opening, with multiple red shapes | A 2D projection does not prove 3D coincidence or a bound collective object |
| 180–199 / 9.00–9.95 s | Geometry changes little across adjacent views while colors keep changing; pale red faces can be very faint | Ongoing palette cycling can exaggerate visual activity or make a persistent object seem to disappear |

Examples at full resolution: [frame0](visuals/movie_frames/frame_000.png), [frame1](visuals/movie_frames/frame_001.png), [frame6](visuals/movie_frames/frame_006.png), [frame199](visuals/movie_frames/frame_199.png).

The camera is a fixed 3D projection. Transparency, overlap and face sorting can obscure objects. The program draws no trajectory trails, body-ID labels, energy graph, numerical energy overlay or teleport-event annotations on the movie. The title mentions tracking because diagnostics are computed/printed/logged elsewhere. Overlap of projected tetrahedra is not evidence of equal center coordinates; their decorative corners can extend outside the coordinate range without participating in motion or collision.

## Can the movie be joined to a CSV?

**Formal original-run provenance: UNLINKED.** There is no surviving export receipt tying a source hash, RNG state, CSV and MP4 together. However, a bounded content test gives strong positive evidence for **movie frame f ↔ B callback q=f+1**.

[check_visual_correspondence.py](inspection/check_visual_correspondence.py) draws source-defined tetrahedra from saved CSV positions and modes, using the source frame label, fixed figure size, default view, fixed palette and current Matplotlib. It performs no dynamics, interpolation, fitted camera search, random draw or parameter sweep.

The first comparison uses every recorded label-zero state: 12 in A and 6 in B. This is a finite attribution check across existing records, not a new simulation or seed search. The script then checks the fixed movie frames 0,1,6,34,82,120,184,199 against B q=f+1. These represent the opening seam, selected palette transitions and later geometry.

A simple colored-pixel mask is max(R,G,B)−min(R,G,B)>15. The checker reports mask intersection-over-union (IoU) and mean absolute RGB error over the union. These are descriptive similarity measures, not statistical likelihoods:

| Check | Mask IoU | Mean absolute RGB error, 0–255 scale |
|---|---:|---:|
| Movie0 vs Bq1 | 0.890282 | 5.516925 |
| Movie0 vs Bq0 | 0.859051 | 13.001680 |
| Movie0 vs other B label-zero states | About 0.10–0.12 | About 101–105 |
| Movie0 vs A label-zero states | About 0.002–0.048 | About 91–106 |
| Eight selected frames vs Bq=f+1 | 0.856495–0.890282 | 5.516925–7.086700 |

The [comparison panel](visuals/movie_recorded_state_comparison.png) was visually reviewed. Shape positions and palette transitions closely agree at all eight samples. Compression, transparency, very pale Reds colors and historical rendering-version differences affect pixel scores. The exact metrics and selection are retained in [visual_correspondence.json](analysis/visual_correspondence.json).

Under this candidate correspondence, frame0→1 matches Bq1→2, the small native Z movement across the seam for body2. Frame6 matches Bq7, the first recorded mode flip of body5. These are corroborating correspondences, stated conditionally. They do not prove all 200 frames have been matched, recover the unknown initial state, or certify a unique historical export.

## Historical center-7 charts

Two nearby PNGs were directly inspected and copied:

| Historical file in OLD_MATERIAL/Simulations_Trash/Simulations_part_1 | Bytes | SHA-256 |
|---|---:|---|
| Tetrahedron_7_position_trace_with_teleport_events.png | 117,437 | bf6dfb6ec1da4a9ceb56c9107b654671492576945a1b62426625b18ec99fe798 |
| Tetrahedron_7_GRF_over_time.png | 120,207 | 8f3c93d74ec1c03f97d70320b5c760953dca805b3bd3f1e967d54d6789a5b137 |

Copies: [position chart](originals/Tetrahedron_7_position_trace_with_teleport_events.png), [GRF/energy chart](originals/Tetrahedron_7_GRF_over_time.png).

These are **ORIGINAL artifacts, ATTRIBUTED to postprocessing of B**. Their geometry/energy pattern and markers at 409,414,418 strongly match B. They are not direct output statements in plot_1.py: no PNG-saving code exists there, and their generating chart script has not been recovered.

The position traces occupy Step labels 0–199 and show multiple passes folded onto the same range. Connecting successive physical records while using Step as X also draws long connectors from label199 back to label0. Yet the red event markers are at 409,414,418, which match B's body7 seam *callback indices*. They sit far beyond the trace's 0–199 range.

[B_historical_axis_diagnostic.png](visuals/B_historical_axis_diagnostic.png) is a new, explicitly derived demonstration using B's recorded values and those two different axes. Its trace shapes and marker layout visually corroborate the explanation. It does not claim pixel-perfect recovery of the missing plotting script. The old GRF/energy chart similarly superposes repeated labels; its Energy is the source's global K repeated on body7's rows, not body7's own kinetic energy.

The original red markers also differ radically from the source detector's thousands of would-flag results. They align with actual body7 coordinate crossings, suggesting postprocessing with a different event selection. Without the chart generator, their threshold/algorithm cannot be certified. The source detector must not be credited with correctly identifying just these events.

## Excluded neighboring material

Two further nearby PNGs were inspected for attribution and excluded from this package's behavioral evidence:

- GRF_CRE_DRE_evo_around_teleportation.png (SHA c52beabb35d7c4eb660c771e119fc82a59ee71db9dcce87be3107d64727fde02): contains CRE/DRE quantities not defined by this program; their derivation is unrecovered.
- ec4c0969-3a1b-4df5-b96f-6aad098f1efb.png (SHA 4b84089260cd078d3d94f5233f0fdb1935db80d6ca28b8194b579140bdc9f327): displays “Isolated Harmonic Tunnel” / “Resonance Echo” content absent from this program.

Both remain untouched in their original part_1 directory. The separately indexed tetrahedral_states_curvature_20250712_062601.csv belongs to a different, incompletely recovered rule and was not used. No missing historical trajectories, notes or frames were invented.
