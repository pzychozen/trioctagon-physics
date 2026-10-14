# Early SRG Recursive Motion: Source Reconstruction, Stateful Feedback, and Finite Replays

**SIM01 · Research edition v0.1 · Prepared 14 October 2026 · Awaiting publication approval**

How do the surviving early SRG programs turn stored state into motion? This edition preserves the completed [SIM01 research note](SIM01_REPORT.md), its recorded evidence and the subsequent [GPT scientific review](review/SIM01_GPT_SCIENTIFIC_REVIEW.md). The study follows three historical programs closely enough to distinguish their evolving state from what an animation or displacement detector displays.

The programs share retained velocities, componentwise logarithmic damping and periodic coordinate wrapping. Their mechanisms develop in three steps:

- **A** moves three centers in two dimensions. Each center responds to wrapped pairwise differences, using the positions already changed by earlier centers in the same update.
- **B** moves eight centers in three dimensions. It repeatedly calculates the arithmetic centroid of stored wrapped coordinates and uses a common gain calculated from incoming mean speed. The tetrahedra are display shapes attached to the centers.
- **C** carries the same kinds of position and velocity state plus a binary force-sign choice for each center. Actual random draws can toggle these choices when the incoming-speed gate permits them.

C therefore has a concrete feedback loop: stored positions and velocities determine the centroid and common gain; eligible draws update retained signs; the resulting forces, damping and wrapping produce the next state. The common gain is frozen for that complete update. Centers move sequentially, and their random draws follow source index order. The prescribed H(t) curve supplies clock-dependent forcing; it is distinct from carried memory. The edition preserves the arithmetic centroid, damping and original ordering.

The finite records show substantial slowing while separated centers continue moving. C produced **14 bit changes in 1,600 actual draws**; its eligibility gate stayed open throughout this run. Its explicit feedback and traceable saved state motivated selection of **C as the base for this surviving motion family**, with A and B retained as references.

![Recorded C trajectories in wrapped and passively unwrapped coordinates](plots/C_trajectories.png)

The two panels show the same recorded motion. The unwrapped view accumulates minimal-image displacements; it adds no evolving state. The note also contains [speed and separation histories](plots/motion_metrics.png) and [forcing, gain and bit histories](plots/forcing_and_feedback.png).

The evidence has distinct origins:

| Stage | Recorded work |
|---|---|
| Codex study | 12 preflight full-system calls; 2,700 fresh updates: A 500, B 2,000, C 200; 1,530 passive historical-transition checks |
| GPT review | 2,700 passive checks of saved fresh transitions plus 1,530 historical checks; zero additional rollout updates |
| This preparation | File-integrity and publication-readiness checks; no scientific checker or simulation rerun |

GPT additionally compared B's existing 200-update prefix with C's existing 200 updates. Their first difference follows C's first sign switches. This reviewer finding is [preserved with its provenance](review/INDEPENDENT_REVIEW_RESULTS.json); it was passive analysis, not a newly executed controlled experiment.

A source observer computes $J=\|(p^+-p)\bmod10\|$. A displacement of (-0.001,0,0) consequently reads as length 9.999, although its minimal-image length is 0.001. It flags **1,509 body-events** in C and **8,151 / 3,129** in the two historical records; none exceeds threshold 1 under the minimal-image measurement. Coordinate-wrap crossings are a separate count. Both readouts are retained without changing the trajectories.

Actual update count, supplied frame argument and movie playback are three different clocks. Historical frame labels reset while state continues evolving, resetting H's argument too. A proposed comparison of schedules has not been run.

These are finite source-consistent observations, not an asymptotic-attractor theorem or an experimentally calibrated physical model. C is not the recovered June topology producer.

Read the [accepted note](SIM01_REPORT.md), then the [review](review/SIM01_GPT_SCIENTIFIC_REVIEW.md). The [access and evidence map](ACCESS_AND_EVIDENCE_MAP.md) explains source paths, records and checker requirements; the [disposition](PUBLICATION_DISPOSITION.md) records authorship, acceptance, rights and pending approval.
