## Appendix A. Equation and source guide

The main text states assumptions next to their consequences. This guide gives the short route back to the accepted evidence. “Exact” describes a mathematical result under its stated definitions; it does not independently validate a physical identification. Code references identify equations and call order only: no source module was imported or executed for FB02.

| Equations | Subject and exact locator | Status and scope |
|---|---|---|
| G1, G2 | Equal-disk geometry and parent-area fraction. IVA §A1; BOUNDARY §§2–3. | Exact geometry; response observable is a choice. |
| G3 | Equilateral inradius ratio. ORIGINS1 §3.1. | Exact for the specified denominator. |
| G4, G5 | Golden split, trilogarithm and coth integrals. ORIGINS1 §4.4; classical references below. | Classical identities; not an SRG discovery or selector. |
| P1 | Area-to-amplitude preparation. BOUNDARY §2 A1–A4, §3 C1, §11; BCODE prepare_area_response. | Unique under the adopted assumptions; raw zero allowed. |
| F1, F2, F3, F4 | Four factors and weighted Fourier cycle. FIXED pp.4–6; IVA §A6; IVA_ACCEPT §3; TARGET §§2.1,8.2. | Exact for the declared tensor order and literal constants. |
| F5 | Helicity-sector intertwining and injection. TARGET §§2.2,8.2. | Exact reduced linear dynamics; normalized eigenbra required. |
| F6, F7 | Prepared raw initializer and cycle weights. BOUNDARY §4 C2–C4, §11; TARGET §8.4. | Exact composition of adopted preparation with fixed transfer. |
| J1 | Periodic-index spatial stencil. JTGMO lines4–46,62–76; IVA §A1. | Source equation; not the embedded-torus metric Laplacian. |
| J2 | January composite REFU step. JREFU lines109–138; APP lines234–238; ORIGINS1 §7.2. | Source order with stated app callbacks. |
| J3, J4 | Paper and signed compressors. JREFU lines37–69; APP lines54–57; ORIGINS1 §7.3. | Distinct historical maps and zero branches. |
| J5 | Prescribed H schedule. IVA §A5; SRGI §7.1. | Exogenous schedule; not state-driven memory. |
| N1, N2 | Modern two-stage deterministic recurrence. DYNAMICS lines57–104. | Declared raw map, including Arg₀ and λ=0 branches. |
| N3 | Tangent-face representation. PHASE1 §§3,6–7; KSM §10.3.3.2; FACE. | Inverse real isometries on the fixed vertical-face tangent spaces, with n_i·e_z=0. |
| N4 | Negative real-gradient increment. PHASE2_REVIEW §3 lines109–120; PHASE1 §7. | Exact increment identity; no unconditional discrete energy decay. |
| N5 | Explicit h-family and first-order approximation. PHASE2_REVIEW §3 lines109–151. | Conditional smooth-domain convergence as h tends to zero. |
| N6 | Action-angle sign and local-clock realization. PHASE3_ACCEPT §1 lines9–36; PHASE2_REVIEW §1. | Exact with the declared symplectic convention and chosen clock. |
| N7 | Cubic oscillator specialization. PHASE3_ACCEPT §7 lines207–218; PHASE3_REVIEW §9. | Exact continuous comparison only for K=0 and affine local clock. |
| S1, S2 | Finite spectrum and continuum inverse trace. RING §§2–3; ORIGINS1 §§5.1–5.2. | Exact spectrum and proven limit; all positive multiplicities, p>1/2. |
| S3, S4 | Free-ring Hamiltonians and energies. RING §§4.1–4.2. | Standard quantum interpretation adopts m, ℏ and energy scale. |
| S5 | Finite-band dynamical bound. RING §4.3 lines578–614. | Proven estimate under the adopted Schrödinger law. |
| S6, S7 | Inverse-cube trace and calibrated coupling. RING §5 lines616–683; ORIGINS1 §§5.2,6. | Exact calibrated equality; exponent and prefactor specified. |

Three important unnumbered results sit beside these equations: the same-step global complex-linear surjection obstruction is TARGET §§3.3,8.3; the orientation cycle is BOUNDARY §4 C4 and, separately, TARGET §8.4; the radius-three invariant polydisk and sharp uniform incident budget are BOUNDARY §§5,11. These are inherited proofs, not new FB02 computations.

The five locator corrections requested by GPT are used here and in the main text: PHASE2_REVIEW §3; PHASE3_ACCEPT §1; PHASE3_ACCEPT §7 with PHASE3_REVIEW §9; BOUNDARY §4 C4 plus TARGET §8.4; and BOUNDARY §§5,11. FB01 has not been amended.

## Appendix B. Referenced sources and versions

Source IDs retain their FB01 meanings. Each linked ID opens the exact cited source: fifteen byte-identical files are linked at a fixed GitHub commit, and fourteen snapshots are included with this edition. SOURCE_LOCATORS.json records their titles, versions, original filenames, publication locations and SHA-256 identities. In the PDF, narrative IDs link to the entries below, whose source links open GitHub. Page references to historical PDFs are physical file pages; line references are to the frozen source text. Source snapshots retain historical local paths and instructions as evidence; use this publication source guide for current access.

**[IVA](sources/IVA.md)** — Bridge IV-A — independent adversarial review and fundamental-physics connection map. v0.1; 22 September 2026. Corrected review, scoped results.

**[IVA_ACCEPT](sources/IVA_ACCEPT.md)** — Bridge IV-A — corrected accepted-results digest. v0.2; 22 September 2026. Scoped accepted digest.

**[BOUNDARY](sources/BOUNDARY.md)** — Boundary-response toy closure: explicit proposal, proofs and implementation path. v0.1; 22 September 2026; §11 added 23 September. §11 adopts lens_area_norm_v1 and supersedes the initial pending header within scope.

**[TARGET](sources/TARGET.md)** — Bridge IV-B Target B — corrected proof reconstruction and GPT review. 22 September 2026. §8 contains the later independent acceptance; original pending header is historical.

**[ORIGINS1](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1.1/manuscript/SRG_ORIGINS_v0.1.1.md)** — SRG Origins — From Geometry to Recursive Operators. v0.1.1 publication edition; 21 October 2026. Author-approved edition; used without reopening its publication audit.

**[ORIGINS_STATUS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1.1/PUBLICATION_DISPOSITION.md)** — PUBLICATION_DISPOSITION.md for SRG Origins. v0.1.1. Later publication disposition governs edition status.

**[RING](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_QUANTUM_RING_SPECTRAL_CORRESPONDENCE/publication/v0.1/SRG_QUANTUM_RING_v0.1.tex)** — Symbolic Resonance Geometry and Quantum Ring Spectra: An Exact Discrete-to-Continuum Spectral Correspondence. v0.1; 13 October 2026. Accepted publication source; §4 is quantum theory and §5 is coupling.

**[RING_STATUS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_QUANTUM_RING_SPECTRAL_CORRESPONDENCE/publication/v0.1/PUBLICATION_DISPOSITION.md)** — PUBLICATION_DISPOSITION.md for the quantum-ring paper. v0.1. Publication disposition reused, not re-audited.

**[SRGI](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_I_FOUNDATIONAL_RECONSTRUCTION/publication/v0.1.1/manuscript/SRG_I_v0.1.1.tex)** — SRG-I: Foundational Reconstruction. v0.1.1; 10 October 2026. Completed accepted volume; inherited source distinctions.

**[LINEAGE](sources/LINEAGE.md)** — SRG mathematical and operator lineage. 11 October 2026. Completed documentary reconstruction.

**[PHASE1](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md)** — First bridge: folded geometry to three complex state components. 21 September 2026. Exact kinematics and conditional state interface.

**[PHASE2_REVIEW](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_II/PHASE_BRIDGE_II_CODEX_REVIEW.md)** — Phase Bridge II — independent Codex verification. 21 September 2026. Corrected sign and conditional first-order family.

**[PHASE3_ACCEPT](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_III/PHASE_BRIDGE_III_ACCEPTED_RESULTS.md)** — Phase Bridge III — accepted results. 22 September 2026. Operative corrected synthesis with stated assumptions.

**[PHASE3_REVIEW](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_III/PHASE_BRIDGE_III_CODEX_FINAL_REVIEW.md)** — Phase Bridge III — Codex final independent review. 22 September 2026. Independent review; §9 scopes the oscillator equivalence.

**[KSM](sources/KSM.md)** — KERNEL_SOURCE_TO_MODEL.md. FB01 frozen snapshot. Admitted model/state correspondence at §10.3.3.2.

**[FIXED](sources/FIXED.pdf)** — Recursive SRG Evolution: A Qutrit–Qubit Operator, Dual-Core Geometry, and Computational Interpretation. 24 November 2025; file U_REFU.pdf. Historical fixed-matrix source, interpreted through corrected Bridge IV-A/IV-B.

**[P01](sources/P01.pdf)** — Symbolic Recursion and SRG Fusion: Emergent Lattice Fields from Glyph Memory Dynamics. 15 July 2025. Historical lock equation and Appendix A design rationale.

**[P06](sources/P06.pdf)** — Recursive Dark Energy and Vacuum Feedback: A Vesica-Phase Cosmological Framework. 13 July 2025. Historical equation; glossary identification conflicts with its solved γ*.

**[VPQW](sources/VPQW.pdf)** — Vesica Piscis Quantum Wavefunction (VPQW): A Novel Geometric Approach to Quantum Systems. printed cover: 28 February 2025. Historical conventions; circumference/radius discrepancy retained.

**[VESICA](sources/VESICA.pdf)** — The Vesica Delay Method: A Geometric-Perceptual Bridge to Coherence. 2025. Historical chosen radius and half-angle example.

**[APP](sources/APP.py)** — app.py. January archive 18285147; FB01 snapshot. Historical defaults, callbacks and time convention.

**[JREFU](sources/JREFU.py)** — refu.py. January archive 18285147; FB01 snapshot. Historical composition and compressor definitions.

**[JTGMO](sources/JTGMO.py)** — tgmo.py. January archive 18285147; FB01 snapshot. Historical periodic-index stencil.

**[INFINITY](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_LOCAL_GEOMETRY_AND_RESONANCE_SIM04_SIM05/publication/v0.1.1/evidence/originals/SIM05/srg_infinity.py)** — srg_infinity.py. March archive 19023429; FB01 snapshot. Historical assigned coupling call sites.

**[BCODE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/boundary_response.py)** — kernel_physics/boundary_response.py. FB01 snapshot. Adopted preparation implementation, read only.

**[SRGCODE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/srg.py)** — kernel_physics/srg.py. FB01 snapshot. Frozen decimals, branch/gauge and fixed transfer implementation.

**[DYNAMICS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/dynamics.py)** — kernel_physics/dynamics.py. FB01 snapshot. Unchanged modern raw recurrence, read only.

**[REGION](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/operating_region.py)** — kernel_physics/operating_region.py. FB01 snapshot. Opt-in radius-three domain and incident budget, read only.

**[FACE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/face_state.py)** — kernel_physics/face_state.py. FB01 snapshot. Optional state representation, read only.

**[GPT_REVIEW](provenance/reviews/FB01_GPT_SCIENTIFIC_REVIEW.md)** — FB01_GPT_SCIENTIFIC_REVIEW.md, 27 October 2026, supplied by the operator in the FB02 order packet. Decision: FB01 accepted within its source-and-equation scope. The cited review is preserved unchanged in this edition. Its historical instructions are task guidance only as adopted by the operator, not new mathematical evidence. Subsequent final manuscript acceptance and publication authorization are recorded in PUBLICATION_DISPOSITION.md.

**Classical references already in the accepted source chain.** NIST, [DLMF §25.12, Polylogarithms](https://dlmf.nist.gov/25.12). Lubomir Markov, [Hjortnaes Integrals Involving the Di- and Trilogarithms](https://www.diogenes.bg/ijam/contents/2024-37-3/2/2.pdf), International Journal of Applied Mathematics 37(3), 305–310 (2024), DOI 10.12732/ijam.v37i3.2, especially p.308, Eqs.(8),(11). These are the classical references carried by ORIGINS1 §4.4 and §11 and checked in the supplied GPT review; FB02 makes no new literature or priority claim.
