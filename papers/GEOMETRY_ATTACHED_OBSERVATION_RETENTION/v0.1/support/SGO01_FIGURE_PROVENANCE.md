# Accepted v02 figure provenance

Both distributed PNGs are unchanged copies of the accepted visualization revision. They are embedded without cropping, resampling or pixel changes in the manuscript; decoded embedded pixels were compared with the distributed originals. The original camera figure remains external provenance and is not distributed here.

| Figure | Dimensions | Bytes | SHA-256 |
|---|---|---:|---|
| [Geometry-only views](../figures/SGO01_GEOMETRY_ONLY_v02.png) | 2520 x 1404 | 193815 | `28106bf994a3353fac88ec6a300e65e60d6ef000538b06a19b9b0fdd9f43bdfe` |
| [Saved-output comparison](../figures/SGO01_FACE_READOUT_COMPARISON_v02.png) | 2520 x 2160 | 252515 | `f07584d79299752fa45416dc1cbb42d9239ec17d25b989685b8f0b3f8541b1d8` |

The rendering uses actual `geometry.folded_module()` vertices and face cycles at the SGO-01 source identity, with independent exact radical maps used for verification only. Three congruent regular octagons have 18 welded vertices, 21 edges and three shared seams. No fold angle, face size or assembly shape is changed.

The primary orthographic camera has elevation 28 degrees and azimuth -90 degrees; the reverse geometry-only view uses +90 degrees. A/C each retain about 0.441474 of face-on projected area and B about 0.882948. World limits are X [-0.85,0.85], Y [-0.4,1.2], Z [-0.6,0.6], with box aspect proportional to those extents. Transparent panels expose rear seams; their projection is not a physical change of area.

The comparison uses the two saved native outputs at a = 2 and b = sqrt(382/85), not the equal-scale controls or successive trajectory frames. Both full panels use identical cameras/scales and arrow gain 0.32. The B-detail crops are explicitly magnified, with common local u [-0.1,0.1], z [-0.055,0.055] limits, equal aspect and unchanged gain. Displayed endpoints are approximately +0.064000 and -0.066242 world-coordinate units. Arrows are free state vectors based at fixed centres, not displacements, deformation, forces, field lines or measured physical quantities. Tiny binary64 residues remain in the underlying saved vectors.

The project-internal review addendum visually accepted the geometry-only upload and checked the plotting source/data rule. Its supplied files lacked the comparison PNG, so it did not independently visually accept that image. Codex inspected both local originals; the owner's subsequent publication order explicitly authorized the corrected v02 figures. This records the actual review boundary without inventing another review or an external peer-review claim.

No figure was regenerated during publication preparation. Machine-bound plotting scripts and private render/preservation receipts are not distributed. See [MANIFEST.json](../MANIFEST.json) for final package identities.
