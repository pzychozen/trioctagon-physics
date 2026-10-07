# Version-specific recursive lineage

This is explanatory provenance for the measurement v0.1.1 candidate. It records a bounded reading of named primary passages and source routines. No old physical claim, numerical spectrum, simulation outcome, attractor claim or convergence claim is adopted. Historical scripts are source evidence and were not executed.

The raw source hashes, exact selected PDF pages, project-relative locators and excerpt hashes are in [lineage_sources.json](../../../provenance/lineage_sources.json).

## Sources and distinct mathematical meanings

| ID | Primary source / locator inside this folder | Definition inspected |
|---|---|---|
| S1 | RPCO.py.txt, original RPCO.py, lines 5–13 | Static angular sinusoid times radial Gaussian. No state-to-next-state call occurs in the function. The plot title calls it Recursive Phase Collapse Operator. |
| S2 | TGMO.py.txt, original TGMO.py, lines 6–16 | Parametric fixed-azimuth toroidal-coordinate curve, not an iterative state map. Plot title: Toroidal Geometry Memory Orbit. |
| S3 | REFU.py.txt, original REFU.py, lines 5–12 | Prescribed damped cosine/sine/exponential function H(t). It does not update an independent stored memory state. |
| S4 | recursive_field_evolve.py.txt, evolve_field | Position-array update with fixed initial adjacency, neighbor differences, tanh feedback, mean-position bias and random perturbation. Not a six-state matrix. No script was run. |
| J1 | J1_primary_excerpts.txt, PDF pp. 1–3 | July 15 glyph narrative: Symbolic Resonance Geometry, identifiers, positions, scalar resonance and recursive passes. |
| J2 | J2_primary_excerpts.txt, pp. 1–3, 5–6 | July 15 expansion explicitly cites an earlier account named SRG_recursion.pdf. The identity of that filename with J1 is not proved here; no composition chronology follows from common archive membership. |
| J3 | J3_primary_excerpts.txt, pp. 1–3, 5 | July 14 glyph tuple including H(t), echo set and resonance. Its prescribed memory envelope is not the later fixed U_REFU matrix. |
| P21 | P21_primary_excerpts.txt, pp. 4–5, 16–18 | November 24 field/descriptor/memory model. RPCO normal compression, TGMO tangential modulation, REFU diffusion/drift plus memory. Eq. (11), p. 5, and eq. (28), p. 18, give the three-stage composition on (u,H,C). Missing functions and integration choices prevent reading this as one recovered executable algorithm. |
| P23 | P23_primary_excerpts.txt, pp. 2–6, 30 | November 24 six complex amplitudes. Introduction expands SRG as Structured Recursive Geometry. Defining update is U_REFU U_TGMO U_flip U_RPCO, with the separate flip essential. Core projector has rank two; fixed U_REFU has no auxiliary memory variable. |
| N-srg.py | ../native/kernel_physics/srg.py, fixed_november_srg and handoff_area_response | Same fixed transfer constants and B tensor (R Z C); then chosen eigenbra extraction and adopted lens-area gain initialize a triad. |
| N-dynamics.py | ../native/kernel_physics/dynamics.py, _advance, phase_sync, step3 | Later native nonlinear amplitude/coupling update followed by simultaneous phase synchronization, with no six-state SRG call or auxiliary H(t). |

All copies in this folder are unchanged raw script bytes with a .txt extension, or explicitly headed verbatim page-text extracts produced with pypdf. PDF extraction can lose visual typography; original PDF identities and page locators are retained. The raw PDFs are not redistributed here. The relevant displayed source formulas were also checked against their original page renders.

## Arrow classification

| ID | Arrow | Classification | Evidence and limit |
|---|---|---|---|
| A1 | Earlier glyph-SRG account to J2 expansion | DOCUMENTED LINEAGE | J2 p. 1 explicitly identifies prior work; not an exact update equivalence, and not a proved identification of SRG_recursion.pdf with J1. |
| A2 | Early named illustration scripts to later field/matrix roles | STRUCTURAL REINTERPRETATION | Reused names and motifs, with different state types and maps. A direct chronological code genealogy is NOT RECOVERED. |
| A3 | P21 field-memory description to P23 fixed six-state description | STRUCTURAL REINTERPRETATION | The comparison is between mathematical roles. An exact dimensional reduction and order of composition of the two same-date documents are NOT RECOVERED. |
| A4 | P23 defining four-factor product to native fixed U | EXACT DESCENDANT | In helicity-major ordering, factors are I2 tensor R, D tensor Z, X tensor I3, I2 tensor C. Their ordered product equals (D X) tensor (R Z C). The fixed constants agree. This is not a validation of P23's other claims. |
| A5 | Historical six-state evolution proposal to lens initialization role | STRUCTURAL REINTERPRETATION | Current source adopts a preparation/interface role; it does not derive the lens response or subsequent recurrence from historical physics. |
| A6 | Native handoff output to canonical initial triad | EXACT DESCENDANT | Explicit existing eigenbra projection and fixed-cycle formula in handoff_area_response; manuscript M22–M23 unchanged. |
| A7 | Repeated SRG powers to later nonlinear Tri-Octagon recurrence | NOT RECOVERED | Different state dimensions and formulas; no conjugacy/equality/reduction in the inspected sources. This is a bounded provenance statement, not a universal impossibility theorem. |

EXACT DESCENDANT means formula/interface inheritance is explicitly verified. DOCUMENTED LINEAGE means the source states the connection. STRUCTURAL REINTERPRETATION means reused roles with changed objects, without asserting a derived reduction. NOT RECOVERED is limited to this source set.

## Fixed-product check

The exact algebra uses the standard Kronecker multiplication identity in the original factor order. It never interchanges R with Z, nor the helicity phase with the flip. All 36 matrix differences vanish symbolically for independent symbolic scalar entries in the stated factors. A single fixed-parameter assembly from P23's definitions matches native U to maximum absolute entry residual 3.3422138886441676e-16 (tolerance 2e-15). This is a bounded transcription check, not a new dynamics result, parameter sweep or physical calibration.

The three-factor composition belongs specifically to P21. P23 has four factors; its fixed REFU is a matrix, whereas P21's REFU uses a separately evolving scalar H(t), and S3 prescribes H(t) directly. No timeless equality SRG = REFU composed with TGMO composed with RPCO is asserted.

## Interpretation boundary

The useful explanatory thread is compression/phase/feedback vocabulary becoming a specified finite-dimensional transfer and then being used as a controlled initializer. The rigorous inherited link is the defining fixed-operator factorization. A physical memory mechanism, spatial trajectory, spin, material shell, field law or reduction to the later nonlinear recurrence does not follow from that lineage.
