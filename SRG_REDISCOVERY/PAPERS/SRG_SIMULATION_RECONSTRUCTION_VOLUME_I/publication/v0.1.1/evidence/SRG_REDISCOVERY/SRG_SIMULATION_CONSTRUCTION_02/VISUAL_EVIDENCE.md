# Visual evidence and its limits

The original movie was found through the existing R0 source index, then decoded and inspected in this checkpoint. No new simulation generated any of the evidence below.

## Attribution

| Evidence | Finding |
|---|---|
| Historical file | OLD_MATERIAL/Simulations_Trash/Simulations_part_1/tetrahedral_attractors_animation.mp4 |
| Preservation identity | 1,002,986 bytes; SHA-256 4f90ce9fc384b134b68b5a64424ef3e05d364153d4e70efdd1596c0b8c937dd3 |
| Exact filename link | 3Dtriangles.py:110 declares this name; it was the only matching literal found in Python sources under OLD_MATERIAL |
| Title and scene | The movie displays "Tetrahedral Attractors in Toroidal Space", matching source line 59, with eight tetrahedral glyphs and axes labeled X, Y, Z over 0–10 |
| Frame and encoding link | 2,000 frames decoded; 60 fps; 1000-by-800 pixels; H.264; duration 33.333333 s. Frame count and fps match source 10, 107, 113; dimensions are consistent with its 10-by-8-inch figure |
| Directory difference | The source is in Simulations_part_2, the movie in Simulations_part_1. Source 110–113 writes to a relative working-directory path; directory difference alone does not contradict the association |
| What remains missing | Original random state, numerical positions/velocities, callback history, exact generating source snapshot and historical library/backend versions |

This is a **strongly source-associated historical movie**, not a certified byte-for-byte reconstruction of its generating run.

The similarly named tetrahedral_attractors_logic.mp4 belongs to a different declared output: plot_1.py:158, with a different title at 86, 200 frame labels at 12, and 20 fps at 161. It was used only to disambiguate filenames; its movie was not imported into this package.

The previous R0 index had only hashed the selected movie, without inspecting frames. See [source_manifest.json](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/R0_SOURCE_RECOVERY/source_manifest.json:947). Its selected source entry begins at 1003. The source and movie hashes still agree with those records.

No numerical trajectory record was certified for this specific source/run. The already recovered log linkages in [SRG_R0_REPORT.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/R0_SOURCE_RECOVERY/SRG_R0_REPORT.md:320) associate the two older fixed-step tetrahedral state logs with plot_1.py; the curvature log uses a different, incompletely recovered update. Those records are not substituted for missing 3Dtriangles.py data. The local attractors.png is the previously studied three-attractor figure. The neighboring REFU/RPCO/TGMO text files are helper-function samples, not a trajectory record for this movie.

## What was inspected

All 2,000 movie frames were decoded to check readability and count. Visual inspection covered the following selected frames and sheets, not uninterrupted real-time playback of the whole movie:

| New inspection artifact | Movie frame indices, zero based | Purpose |
|---|---|---|
| evidence/movie_overview.png | 0, 10, 30, 60, 120, 240, 400, 600, 900, 1200, 1600, 1999 | Full-duration overview |
| evidence/first_eight_frames.png | 0–7, every frame | Separate changes in color from changes in position |
| evidence/early_same_color_phase.png | 0–120, every eighth frame | Hold the source palette phase constant while comparing early geometry |
| evidence/early_relocation_window.png | 8–16, every frame | Inspect the relocation noticed between overview samples 8 and 16 |
| evidence/frames/*.png | Full-resolution versions of all selected frames | Allow inspection without contact-sheet reduction |

Every sheet was visually inspected. Frames 0, 30, 60, 1999, 13 and 14 were additionally opened at full resolution. Frame/time labels were added only to the new sheets. The unaltered MP4 and extracted full-resolution frames contain no added annotations.

The inspection scripts save their selected indices, decoder timestamps and PNG hashes under inspection/. Seconds in these records are **movie playback time**, not the model's H argument. The FFmpeg metadata report ends with "At least one output file must be specified" because it was invoked solely to report input metadata; decoding was performed successfully with OpenCV.

## Observations, interpretation and limits

| Direct observation from inspected images | Source-supported interpretation | What this does not establish |
|---|---|---|
| Frames 0–7 change colors while glyph locations also move slightly | The per-frame palette rule is independent of position dynamics (102) | A color seen in two consecutive frames does not identify the same center |
| In the same-phase samples, the glyph at lower right in frame 8 is at the left in frame 16 | The detailed window locates a large screen relocation at 13→14, consistent with coordinate wrapping (95–96) | Exact crossing axis, velocity or native travel distance; a new teleport mechanism |
| Several glyph silhouettes move closer in the projected view over early-to-late samples; there is visible overlap near the lower central group | Shared centroid response couples the centers; projected arrangements genuinely change | A measured decrease in every 3D pair distance, physical collisions, fusion or identical paths |
| An upper glyph and a right-side glyph remain visibly separated in the final image | The inspected movie does not end in one completely coincident displayed cluster | An asymptotic non-convergence theorem or a precise final 3D separation |
| The arrangements at 600, 1200 and 1600 are much more similar than the early arrangements; these three labels also have the same palette phase | Visible motion is much slower late in the movie; decaying drive and retained damped velocity are consistent mechanisms | Exact stationarity, a measured speed curve, or a proof of equilibrium |
| The sampled frames do not establish a particular leader, route-following pair or coordinated reversal | No such outcome was imposed or searched for | Absence of every possible collective event between uninspected frames |

The relocation is a specific observed event. Its wrap explanation is an inference from the source and the rendered evidence. The exact three-dimensional state history was not recovered from pixels. Apart from this event, the sampling does not certify a complete catalogue of rapid transitions or individual direction reversals.

## Rendering effects to keep separate

The source plots a fixed 3D view of translucent polygons (54–71, 99–102). Projection can superimpose objects that are separated in depth, and overlapping transparency or depth sorting can change their apparent appearance. Some tetrahedra look like flat triangles from this viewpoint; their source geometry still has four faces.

Vertices are translated but not individually wrapped. A center close to a boundary can have corners extending beyond the nominal coordinate cube. A center wrap relocates the entire displayed shape. Axis framing or overlap can obscure part of a shape; no particular missing face is claimed here as a verified clipping defect.

There are no trajectory lines or accumulated trails in this program. Consequently, the long connected-line artifact possible in simulation 1's static trajectory plot is not present in this rendering. Color changes, projection overlap and coordinate jumps remain important.

For convenient review, open [the original movie copy](evidence/tetrahedral_attractors_animation.mp4), [the overview](evidence/movie_overview.png), and [the consecutive relocation window](evidence/early_relocation_window.png). Their provenance and transformations are included in MANIFEST.json.
