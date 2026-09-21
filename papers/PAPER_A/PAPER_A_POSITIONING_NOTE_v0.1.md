# Paper A — Positioning Note v0.1
How to position `PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.3.md` given the literature context. Companion to `PAPER_A_LITERATURE_CONTEXT_v0.1.md`. No manuscript edit here — this is advice for a future referenced v0.4.

## The situation in one line
The machinery (cycle-Laplacian pull-back, quotient/covering, synchrony subspace, Fourier/deck spectrum, fibration semiconjugacy, IRR/deck transverse block-diagonalization, master-stability Floquet analysis) is **standard**; the **specific map and its deck-resolved transverse-stability atlas** are the model-specific contribution, for which no close precedent was located.

## Three positionings

### A. CONSERVATIVE — *recommended*
**Framing.** Treat graph-covering / equitable-partition / synchrony-subspace reduction entirely as **established background**, cited to [GR01], [SGP03], [DL15], [Pecora14]/[Sorrentino16]. State plainly that Theorem 1 is the equitable-partition quotient-matrix identity specialized to cycles, that $V_3$ is a synchrony subspace, that Proposition 2 is an instance of the fibration ⇒ conjugacy principle, and that the transverse block-diagonalization is the abelian case of the IRR cluster-stability method. **Contribution:** the specific nonlinear model (complex Mexican-hat + cycle-Laplacian + harmonic-3 phase sync) and its **explicit, deck-resolved transverse-stability atlas** (regimes, $g_\ast$, Floquet values, direct-perturbation confirmation), together with the all-$3\mid M$ worked reduction and the RSB shared-sector observation.
- **Pros.** Fully defensible; matches the evidence; the paper's own "elementary and self-contained" wording for §§3–5 already points here; lowest referee risk.
- **Cons.** Modest-sounding, but accurate.
- **Best supported by the literature: YES.**

### B. MODERATE — *acceptable if framed carefully*
**Framing.** Foreground the **explicit all-$3q$ nonlinear realization and its deck-resolved stability atlas** as a concrete, fully worked **extension/application** of established synchrony theory to a specific complex coupled-map ring — i.e. "here is a clean, exactly-reducible nonlinear model in which the synchrony subspace, its symmetry-adapted transverse blocks, and its Floquet stability boundaries can all be written down explicitly and verified numerically."
- **Pros.** Still honest; highlights that the worked completeness (exact reduction + explicit atlas + perturbation confirmation in one model) is not trivially available off the shelf.
- **Cons.** Only acceptable if the paper **explicitly labels the reduction machinery as background** and does not imply the reduction *mechanism* is new. Must retain [DL15]/[SGP03]/[Pecora14] citations up front.
- **Best supported: PARTIALLY** — defensible only with the background clearly ceded.

### C. STRONG — *not recommended*
**Framing.** Claim a genuinely new theorem or mechanism.
- **Not supported.** Every mechanism located a standard home. `NOVELTY_CLAIM_JUSTIFIED = NO`. Do not adopt.

## Recommendation
**Adopt A (CONSERVATIVE).** Optionally borrow B's one-sentence framing of the *worked completeness* ("an exactly reducible model in which sector, symmetry-adapted transverse blocks, and Floquet boundaries are all explicit") **only** after the background is ceded with citations. The frozen mathematics needs no change; a v0.4 adds (i) a short "Relation to prior work" paragraph with the [GR01]/[SGP03]/[DL15]/[Pecora14]/[Sorrentino16] citations and the §2 terminology crosswalk, (ii) [HMM93] for the harmonic-3 coupling, and (iii) [PC98]/[ABS96] for the transverse-stability method. No claim of priority; a literature-context pass is not a novelty determination.

## Concrete additions for a referenced v0.4 (no math change)
1. §1 or a new "Relation to prior work": one paragraph placing Theorem 1 (equitable-partition quotient / covering pullback [GR01]), $V_3$ (synchrony subspace / balanced coloring [SGP03], [GS06]), Proposition 2 (fibration ⇒ conjugacy [DL15]; discrete-time [Field04]), §7 (IRR/master-stability transverse blocks [PC98], [Pecora14], [Sorrentino16]).
2. §4: one line stating covering ≡ surjective fibration ≡ balanced-coloring quotient ≡ equitable-partition quotient for regular cycle covers (crosswalk), citing [GFBC24].
3. §6.1: one line noting $\sin 3(\phi_i-\phi_j)$ is standard higher-harmonic phase coupling that supports three-cluster states [HMM93].
4. §7.5: keep "transverse $-1$ eigenvalue crossing"; optionally note it is a transverse period-doubling-type instability (not a blowout, which needs a chaotic base [OS94]).
5. Bibliography from `PAPER_A_REFERENCE_LEDGER_v0.1.md`, verifying page ranges flagged "(verify at typesetting)".

These are additive, background-only, and change no theorem, number, or claim.
