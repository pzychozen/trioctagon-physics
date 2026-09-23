# Paper E reference and provenance ledger

Access and local inspection date: 23 September 2026. Author: Hilmir Frímann Halldórsson. Source tracing and this ledger: Codex. The preceding reconstruction is accepted input by the Paper E work order. Paper E scientific review remains PENDING_GPT.

## Primary local evidence

**[R]** `C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/HISTORICAL_Z_MANIFOLD_AND_SIX_GAP_RECONSTRUCTION_v0.1.md`. Copy: `evidence/accepted_reconstruction/HISTORICAL_Z_RECONSTRUCTION_v0.1.md`. Sections 1-9 provide the source definitions, harmonic/cone/ordering derivation, display alternatives, metric distinctions, bounded parameter study, preserved-run recovery and open registration. Section 10 records the unresolved precise author question. The manuscript uses those results and their scope; it does not label them a new independent review.

Original verification package: `C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/historical_z_manifold_v0.1/`. Its verification script, results and preservation receipt are included unchanged. The original `verification_execution.txt` is preserved at that path and explicitly identified as earlier Codex re-execution stdout, not an original captured-run artifact. Its 63 checks and 23 fixed configurations are not rerun for Paper E. The six earlier figures were visually inspected in reconstruction and their hashes are recorded in `evidence/source_provenance.json`; Paper E redraws the same evidence with the requested expanded mathematical figures.

| Prior figure evidence | Paper E continuation |
|---|---|
| Harmonic and macro extrema | Figures 2-4; separate analytic height, cone and planar decomposition |
| Direct components | Figure 5; same baseline, common raw scale |
| Display comparison | Figure 7; all four explicit maps |
| Spike mechanisms | Figure 8; recovered phase-off event, component definitions retained |
| Parameter / variant comparison | Section 16 reuses results; Figure 10 isolates staged vs EMA |
| Preserved-run reproduction | Figure 9; exact array comparisons, explicit failure indices |

**[K]** Source root: `C:/TORMENT/TRIOCTAGON_new/kernel_TO/`. Included originals are under `evidence/source_snapshots/staged/`. `source_provenance.json` stores each original path, copy path and SHA-256 identity. No formula was repaired. Function names are durable anchors; the following line numbers refer to these included bytes.

| Source and anchor | Paper E claims |
|---|---|
| `model_core.py`: `_unit` 21; parameters 35; state 73 | thresholds, defaults and initial zero Z |
| `model_core.py`: `phase_lock_step` 133; `advance_phi` 164; `update_z` 169 | recurrence, clock and exact staged Z hierarchy |
| `model_core.py`: `step` 246; `run` 268 | update dependency and pre-step recording |
| `phase_triad_sync.py`: `apply_phase_triad_sync` 5 | simultaneous magnitude-preserving phase formula; zero-strength bypass |
| `constants_selector.py`: `default_k_triplet` | effective soft/scaled triplets, distinct caller settings |
| `geometry_3d.py`: cylinder 4, torus 25, direct extraction 60 | Section 11 maps; hardcoded twelve-sector conversion |
| `geometry_embeddings.py`: config 6, cylinder 12, torus 19 | alternate configurable sector count |
| `definitions.py`: J 22/30; direction 117; full metric 263; entropy 340 | cubic scalar, full/angle/entropy distinction and thresholds |
| `z_spike_diagnostic.py`: run 29; picker 72; writer 94; CLI 245 | saved settings, global picker input, endpoint alignment, clipped windows and plotting limits |
| `toy_3d_triocta.py`: wrapper 80; run 138; channel map 283; scaling 649; selector 685; callbacks 826/848 | display maps, independent percentile scaling, measurement noise, full overlay vs channel trail |
| `analysis_tools.py`: direct plot 93 | direct stored-vector plotting; other scalar display helpers |
| `diagnostics.py`: `run_once` 38 | seed-zero small unnormalized initializer and separate 200-row wrapper |
| `chirality_lab.py`: fits 187; finite differences 288; branch fits 515; plot 868 | exploratory J fits, time-based curvature/torsion distinct from full v |

Other included helpers satisfy imports of the isolated replay harness. A filename or unused imported projection does not authorize an additional interpretation in this paper. Only the core, constants and definitions bodies are exercised by the replay; GUI, scans and downstream experimental models are not launched.

**[H]** `C:/TORMENT/TRIOCTAGON_new/reconstruction/recursive_state_archaeology/codex_verification_I/source_snapshots/model_core.py`. Included at `evidence/source_snapshots/committed_ema/model_core.py`; `update_z`, line 169, uses the cubic observable and memory. H is not substituted for K. Its preserved provenance class does not identify the original saved-run commit.

**[B]** Hilmir Frímann Halldórsson, *Triadic Chirality and Orientation Geometry*, publication revision v0.1.2, 23 September 2026. Exact package: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/publication/v0.1.2/`. Sections 6-7, especially Theorem 4 and Proposition 5, identify the ordered channel triple as transported signed areas and distinguish channel transformations from ambient transformations. Paper E carries only that accepted scope, not a new geometry adoption.

Approved B PDF SHA-256: `5555eb4f07b0974addced80339bf0f87bb7a5ab87d268926f321a3c586da35ad`.

**[D]** Hilmir Frímann Halldórsson, *Tri-Octagon Reference-Scaffold Geometry: Exact Construction of an Alternating Hexagonal Core*, v0.1.1, 23 September 2026. Exact package: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/`. Sections 5-7 and 15-20: author-clarified reference scaffold, positive-length aligned construction, support geometry, fixed-centre transformation and bounded model/Z source trace. This is a source for the clarified scaffold, not for an unknown six-gap registration.

Approved D PDF SHA-256: `7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf`.

## External primary mathematical sources

**[Erb]** Wolfgang Erb. *Rhodonea curves as sampling trajectories for spectral interpolation on the unit disk*. arXiv:1812.00437v1, submitted 2 December 2018. https://arxiv.org/abs/1812.00437 and https://arxiv.org/pdf/1812.00437 . Inspected the paper, specifically PDF p. 10, Example 3(iv): odd-frequency polar rose has that many petals, while even frequency doubles the count. Used only to verify “three-petal rhodonea/rose” terminology. No interpolation theorem is imported, no long quotation is used, and no novelty is claimed.

**[VA]** Harvey Mudd College Mathematics. *Elementary Vector Analysis*, institutional Calculus Online Tutorials, undated. https://math.hmc.edu/calculus/hmc-mathematics-calculus-online-tutorials/multivariable-calculus/elementary-vector-analysis/ . Inspected the cross-product section, specifically Lagrange's identity and the parallelogram-area interpretation. The manuscript supplies its own coordinate expansion and equality proof; unrelated tutorial examples are not relied upon.

**[SG]** Daniel A. Spielman. *Spectral Graph Theory, Lecture 2: The Laplacian*, Yale University, 4 September 2009. https://www.cs.yale.edu/homes/spielman/561/2009/lect02-09.pdf . Inspected p. 2, equation (2.2): positive-Laplacian quadratic form as the weighted sum of pair differences. Used for the standard sign convention; equation (34) is independently expanded for the exact source matrix.

No broad corpus search was performed. No external source closed the six-gap interface. The new algebraic refinements and counterexamples are Codex mathematical exposition for Paper E, not recovered historical claims or newly accepted GPT/Claude results.
