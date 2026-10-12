# SRG Geometry: Local Response, Neighbor Exchange, and Compression

Hilmir Frímann Halldórsson · v0.1 · 12 October 2026

How does moving the same points change the next amplitudes? What happens when one selected neighbor replaces another, and when does compression preserve or erase the difference?

The paper begins with three points whose neighbors stay the same, then seven points with one isolated neighbor exchange. It gives complete proofs of the normalized geometry response, a sufficient selection margin, the exchange law and the compressor classification. A fixed rescaling makes all seven output amplitudes equal while leaving the complete particle state outside that equality.

- [Read the paper](SRG_GEOMETRY_v0.1.pdf).
- [Edit the self-contained LaTeX](manuscript/SRG_GEOMETRY_v0.1.tex).
- [Claim/source ledger](CLAIM_SOURCE_LEDGER.md).
- [Source versions, locators and access](SOURCE_INDEX.md).
- [Evidence roles and retained checks](EVIDENCE_SUMMARY.md).

## Reading guide

Sections 1–2 introduce the question and the three-point example. Sections 3–4 give the actual source order, smooth response and sufficient margins. Sections 5–6 develop the seven-point exchange and compression. Section 7 explains January's separate fixed-grid capture result. Section 8 states the limits; the appendices give the complete enhanced-addition coefficient and retained H bound.

These are incoming-configuration comparisons at one fixed pass, not trajectories. January's periodic field and Tower II's moving-particle state remain distinct. Equal compressed amplitudes do not imply full particle-state capture or later identical evolution.

## Status and evidence

The underlying OC03 and OC04 analyses are internally accepted within their declared one-pass exact-real scope. This new v0.1 manuscript and its exact proposed public file set are **for GPT manuscript-and-payload review**. No external peer review or physical validation is claimed.

The numerical illustrations are transcribed from saved evidence; neither accepted checker nor any historical program was rerun. This edition introduces no simulation, replacement operator or application integration. It is a separate local mathematical chapter and does not replace the reserved SRG-II mechanism paper.

For the historical context, see [SRG-I v0.1.1](https://github.com/pzychozen/trioctagon-physics/tree/3e5972be2f233b6c8ec3c2ebe0687ee1f8f2ff1f/SRG_REDISCOVERY/PAPERS/SRG_I_FOUNDATIONAL_RECONSTRUCTION/publication/v0.1.1) and [SRG Origins v0.1](https://github.com/pzychozen/trioctagon-physics/tree/3e5972be2f233b6c8ec3c2ebe0687ee1f8f2ff1f/SRG_REDISCOVERY/PAPERS/SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1). These are recorded checkpoint links, not fresh online verification.

## Editing and reuse

The TeX is a single editable file with coordinate tables, proofs and bibliography. It needs no local image files, historical source programs or bibliography database. Use an existing XeLaTeX-compatible tool such as Tectonic; a cached, untrusted local build was used for this review edition. Rebuilding can change PDF bytes or metadata.

Hilmir Frímann Halldórsson is the named human author. GPT supplied mathematical review and the work order; Codex assisted with the accepted analysis, manuscript assembly, source correspondence and artifact QA. These are assistance roles, not coauthorship or an institutional endorsement.

This edition grants no new blanket reuse licence. The repository's software licence does not automatically cover this scientific research. Referenced deposited originals retain their source-specific notices, including identified CC BY 4.0 notices; those notices are not transferred to this derived manuscript. The source index identifies the applicable boundaries.
