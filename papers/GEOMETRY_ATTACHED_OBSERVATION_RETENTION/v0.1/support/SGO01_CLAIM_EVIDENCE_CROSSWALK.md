# SGO-01 v0.1 claim-to-proof/evidence crosswalk

Companion to [Information Retention Across Geometry-Attached Observations in the Tri-Octagon Kernel](../publication/SGO01_GEOMETRY_ATTACHED_OBSERVATION_RETENTION_v0.1.pdf), by Hilmir Frímann Halldórsson. Author-authorized repository research publication, 7 October 2026. Review was project-internal, not external peer review.

Locations refer to the delivered manuscript's numbered sections, equations, tables and theorems. Counts are heterogeneous evidence records, not numbers of independent theorems.

| Claim | Classification | Proof/evidence location | Scope and qualification |
|---|---|---|---|
| Labelled face decoder retains all six real coordinates | Inherited from SA0/NRG | Section 2, equations (1)-(3); orthonormal-frame inverse argument | Fixed labels/frames and tangent domain; ambient DE is a projector; no hidden stored-state reconstruction |
| Transported signed areas agree with A; matched dots agree with S | Inherited area convention; SGO-01 explicit matched-dot specialization | Section 3, equations (4)-(7) | No factor 1/2; H = S - iA; untransported ambient dots differ; no new API/detector |
| Generic S fibre is common phase plus possible conjugation | **Inherited from NRG and applied here** | Section 4.1, equation (8); row-Gram isometry argument | Includes rank-deficient factors; static fibre result distinct from regular dynamical closure |
| H fixes a nonzero state modulo common phase; H/I fixes its complex line | Inherited rank-one coherence structure, applied | Section 4.1 | Normalization loses scale; no generic inverse of the update |
| W discards the component of C along (1,1,1); (W,Gamma) recovers C | Inherited from Paper G | Section 4.2, equations (9)-(10) | Rank-two attachment; C and W occupy different coordinate spaces; does not recover state |
| v = (1,-1+i,-i) has C = (1,1,1), W = 0, Gamma = 3 | SGO-01 exact static specialization | Section 4.2; Table 5 and equation (29) | Unevolved control; not a trajectory or physical field effect |
| Fixed one-update polynomial and real-phase mechanism | Inherited from published SPR-01 | Section 5, equations (11)-(14) | Positive ray, exact fixed coefficients, triad, one update; zero convention retained |
| Family face vectors, q, S/H and vanishing A/C/W/Gamma | SGO-01 exact specialization | Section 5, equations (15)-(16) | All a > 0; a zero axial display is not a zero-state certificate |
| Output intensity is globally injective on the positive family | New SGO-01 exact deduction | Theorem 1, equations (17)-(19) | Positive completed-square derivative and endpoint limits; not generic or finite-noise inversion |
| Raw and normalized-coherence inverses, including a = 5 | Inherited from SPR-01 | Section 6, equations (20)-(21), Table 2 | Chart exception handled separately; q/I, S/I, A/I undefined at zero; prior closure exclusions unchanged |
| Published pair has equal populations, unequal raw intensities and opposite signed coherence | Inherited collision with SGO-01 complete readout specialization | Section 7, equations (22)-(24), Table 3, Figure 2 | Actual unequal-scale outputs, distinct from equal-scale controls; signed difference survives S/I, not A |
| Complete snapshot is richer than H | New SGO-01 information qualification using existing fields | Section 8, equations (25)-(26), Table 4 | Qx/Qy/h are coordinate-reference dependent; residuals/metadata excluded; protected contract not edited |
| Complete ideal record is equivalent to (H,beta), beta = w^T w | New SGO-01 exact deduction | Theorem 2, equation (27) and proof | Fibres {w,-w} for nonzero beta, full phase circle for nonzero beta = 0, singleton at zero |
| Nine controls isolate scale, relative/global sign, conjugation, phase and projection losses | SGO-01 exact static deductions and retained numerical corroboration | Sections 8.2-8.3, Table 5, equations (28)-(29) | All nine are fixed unevolved inputs; no extra trajectories |
| Bounded native/FaceState/public agreement and fieldwise precision | Retained numerical corroboration | Section 9, equations (30)-(31), Table 6 | 205 inputs, 615 update-route evaluations, 9 static controls/18 observations; 204 predecessor overlaps; no claim outside fixtures |
| Saved-data independent audit agrees with original metrics | Project-internal independent numerical audit | Section 9.1 and reference [8] | 110-digit static/reference recomputation of saved records; no live kernel, observer, profiler or filesystem replay |
| RFO-02 negative result and entrance/direct-formula comparators remain | Inherited negative evidence and comparison boundary | Section 10; published SPR-01 Section 9 | No experimental retuning or reversal of the earlier classification result |
| Generic inversion, complete-record closure, physical readout and advantage | Open questions | Section 10 | Not established by exact family identifiability or finite software parity |

## Source and evidence access

The [NRG source](https://github.com/pzychozen/trioctagon-physics/blob/dd6c83cbf5bab228ea4fa4c2b90384d8b70f9772/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex), [Paper G source](https://github.com/pzychozen/trioctagon-physics/blob/dd6c83cbf5bab228ea4fa4c2b90384d8b70f9772/papers/PAPER_G/v0.1.1/source/paper_g.tex), [SPR-01 publication source](https://github.com/pzychozen/trioctagon-physics/blob/dd6c83cbf5bab228ea4fa4c2b90384d8b70f9772/papers/STRENGTH_PATTERN_IDENTIFIABILITY/v0.1/source/SPR01_STRENGTH_PATTERN_IDENTIFIABILITY_v0.1.tex) and [kernel definitions](https://github.com/pzychozen/trioctagon-physics/tree/dd6c83cbf5bab228ea4fa4c2b90384d8b70f9772/kernel_physics) are pinned to SGO-01's execution revision. Original SPR-01 native/public execution remains attributed to `6794a72e934a5383547c2507d8c4891346cddf7a`; this publication does not relabel it.

The accepted internal SGO-01 report, frozen protocol/results, raw CSV, verifier and private review files are not distributed in this lane. Their exact formulas and witnesses are presented in the manuscript; retained finite execution outcomes and audit scope are summarized honestly. The package does not assert that the undistributed operational prerequisites can be replayed from the public paper files alone. No new scientific execution occurred during publication preparation.

No literature-wide novelty, external peer review, calibrated noise robustness, physical validation or computational advantage is claimed. The AI-assistance and owner-responsibility disclosure is in the manuscript and [publication disposition](../PUBLICATION_DISPOSITION.md).
