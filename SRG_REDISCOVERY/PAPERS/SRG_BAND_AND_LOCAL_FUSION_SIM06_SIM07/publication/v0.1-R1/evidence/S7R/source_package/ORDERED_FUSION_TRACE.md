# What the ordered fusion actually read

**REPRODUCED · actual operands from the one seed-1618 capture · no reordered control**

The capture records every one of the 24,000 ascending-ID row visits. It establishes a nonzero realized contribution from earlier writes in the selected examples. It does not establish the trajectory difference caused by reversing or simultaneous-vectorizing the loop; no such alternative was evaluated.

## Exact source sequence and records

Original [srg_condensate_breaking.py](handoff/originals/srg_condensate_breaking.py), lines 160 and 178–196:

- Incoming adjacency N_i is chosen once from boundary p−1. It remains frozen throughout the pass.
- The simultaneous local-position stage has already produced Y. The synchronous amplitude exchange and H multiplication have already produced Q. Q is unchanged during fusion.
- For i=0,…,119, the original `np.where(adj[i]>0)` returns selected neighbor IDs in ascending order. An empty row skips its center and write; none is empty in this capture.
- The local center uses actual current `self.positions[nbrs]`, with weights `abs(Q[nbrs])+1e−8`. There is no inverse-distance factor in this center. Direct self is excluded by the graph.
- The original statement writes `positions[i] += .03*Q[i]*(local_center−positions[i])` before visiting the next i. A later row can read that just-written coordinate.
- Compression occurs only after every fusion row; using final compressed R as the fusion weight would change the operation.

The capture's `fusion_reads`, `fusion_weights`, `fusion_center`, `fusion_before`, `fusion_after` and Q are actual copied operands/results. `np.average` is called once with its original input and returns its original result. The [full instrumentation diff](methods/CAPTURE_HOOKS.diff) adds observational hooks only; [recorder.py](methods/recorder.py) supplies the copy-only observer. [Verification](analysis/FIDELITY_VERIFICATION.json) confirms for every selected j that its read is exactly the saved fusion-after coordinate when j<i, or Y_j when j>i. No aliasing into a live array is retained.

## A descriptive identity, not a second evolution

For the recorded row i, let w_j=|Q_j|+10⁻⁸, a_j=w_j/sum(w), and Z_read,j be the actual coordinate passed to the center calculation. The contribution of already-realized writes relative to recorded post-local Y is

`d_i = sum_(j in N_i) a_j * (Z_read,j − Y_j)`.

In exact arithmetic the recorded center is `sum_j a_j*Y_j + d_i`. This decomposes the one actual center. It does not update any alternate state or use the decomposition term as a counterfactual successor. Floating arithmetic can leave a small residual because the original weighted-average evaluation and this reporting decomposition do not arrange products/reductions identically. [All-row accounting](analysis/ordered_read_accounting.csv) reports residuals separately.

The selected passes are 1, 16 and 200: initial movement, the first ten-group observation and the final authorized pass. Within each fixed pass, the representative row maximizes `||d_i||` among that pass's recorded rows. This is selection from existing records, not a seed/parameter search or an attempt to elicit a predetermined behavior. The sampled path windows are boundaries 0–6, 11–21 and 195–200. [Figure F04](figures/F04_actual_ordered_reads.png) shows these paths and the signed per-neighbor contributions; differing close-view scales and fixed translations are disclosed.

| Pass | Target row | Selected neighbors | Earlier-written selected IDs | ||d_i|| [world units] | Largest absolute accounting residual |
|---:|---:|---|---|---:|---:|
| 1 | 112 | 100,102,103,107,109 | all five | .00826298157 | 2.66454e−15 |
| 16 | 6 | 2,5,11,16,18 | 2,5 | .00104550551 | 1.77636e−15 |
| 200 | 8 | 0,1,3,7,19 | 0,1,3,7 | .0000213994194 | 8.88178e−16 |

All exact vectors, Q values, normalized weights, raw weight operands and before/after target coordinates are in [ORDERED_EPISODES.json](analysis/ORDERED_EPISODES.json). Binary authoritative files are [pass 1](runs/B_CAPTURE/stages/pass_001.npz), [pass 16](runs/B_CAPTURE/stages/pass_016.npz), and [pass 200](runs/B_CAPTURE/stages/pass_200.npz).

## Pass 16, row 6: earlier writes and untouched later rows together

This row makes the mixed-age read easy to inspect. The target's post-local position is approximately `(10.2474442766, −.007902847779, −1.2237732789)` and Q_6=.145515333383. It selects IDs 2,5,11,16,18. Rows 2 and 5 have already been written in the fusion loop; rows 11,16,18 have not.

| Selected ID | Normalized weight a_j | ||actual read − Y_j|| | Weighted contribution (x,y,z) |
|---:|---:|---:|---|
| 2 | .2408018130 | .00196331337 | (−.0000184399205, .000139327244, −.000451396512) |
| 5 | .2448881163 | .00235633574 | (.0000822453404, .000169235183, −.000545498603) |
| 11 | .1692338522 | 0 | (0,0,0) |
| 16 | .1773596550 | 0 | (0,0,0) |
| 18 | .1677165636 | 0 | (0,0,0) |

For ID 5, Y was `(10.1642402234, −.009263063370, −1.0188735915)`. Row 6 actually reads `(10.1645760721, −.008571991931, −1.0211011336)`. Its read has therefore changed by approximately `(.000335848639, .000691071439, −.002227542157)`. That is the earlier row's actual fusion displacement, not an inferred direction from a plot.

The total realized contribution is approximately `(.000063805420, .000308562427, −.000996895115)`. The actual center is `(10.2112525079, .123574916694, −1.4044326301)`. The actual target write is `(−.000157993719, .000573960922, −.000788661172)`, leaving row 6 at `(10.2472862828, −.007328886857, −1.2245619401)`. These values are pre-noise and pre-completed-boundary. The subsequent pass noise is separately retained, not confused with the fusion write.

The identity's residual has maximum absolute component 1.77636e−15. A nonzero `d_i` is evidence that earlier writes entered this actual center. It is not the final position difference between this implementation and a hypothetical simultaneous one.

## Early and late examples

At pass 1, row 112's five selected IDs are all earlier. ID 100 supplies the largest individual increment in that row: its actual read differs from Y_100 by about .0201320 in norm, with normalized weight .337438. The combined center contribution is approximately `(−.00783296461, −.00260857949, −.000341822868)`.

At pass 200, row 8 reads four earlier writes and one untouched later neighbor, ID 19. The earlier increments are much smaller but do not vanish: the combined contribution is approximately `(−1.05948e−6, 1.99493e−5, −7.67060e−6)`, norm 2.13994e−5. ID 19 contributes exactly zero to this decomposition because its fusion write has not happened yet. The target row's actual fusion displacement has components about `(1.39295e−5, 6.09501e−6, 3.22838e−5)`.

All 200 passes use original ascending IDs, original incoming selections and uncompressed Q. The evidence supports the ordered-read mechanism at actual recorded values and its diminishing scale in these examples. It does not quantify order sensitivity as a property of a modified model, prove convergence or imply physical causality.
