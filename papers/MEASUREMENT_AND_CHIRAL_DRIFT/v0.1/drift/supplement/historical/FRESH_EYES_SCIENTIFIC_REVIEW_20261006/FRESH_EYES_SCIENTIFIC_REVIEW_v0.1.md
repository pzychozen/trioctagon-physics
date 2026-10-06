# Fresh-eyes scientific review of the native research stack

Reviewer: Claude (independent, adversarial toward analogy) · 6 October 2026 · read-only

Scope read: GR0, GR1, GR2, CM0, SA0, TL0–TL4 (`research/`), the Native Response Geometry paper v0.1 (`trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY`, commit `82cab10`), Paper G and its M1–M3 authorities, and the kernel update `kernel_physics/dynamics.py`. Nothing in any repository or research folder was modified. The independent checks are in `fresh_eyes_checks.py`, with their output in `fresh_eyes_checks_output.txt`. They re-implement the update from its equations and import no project code.

Correspondence labels used throughout:

| Label | Meaning |
|---|---|
| **EXACT** | Identity-level: the native object *is* the known object under an explicit map, with no limit taken. |
| **LIMITING** | Holds only in a stated limit (long wave, small step). |
| **STRUCTURAL** | Same mathematical form, with no map that carries the physical meaning across. |
| **SPECULATIVE** | Plausible, but neither derived nor checked. |

---

## 0. Bottom line

The documents themselves are disciplined. GR0–GR2 and the NRG paper never claim gravity, and Paper G never claims Maxwell physics. The problem is the reverse: **the stack never says what model class the map belongs to.** That gap is what the QED and gravity priors have been filling.

Said plainly, the native map is:

> one explicit (forward-Euler) step of **relaxational, model-A dynamics for a soft-spin XY chain**, i.e. the real Ginzburg–Landau / Stuart–Landau lattice with all frequency and dispersion coefficients zero, **followed by** one explicit gradient step of an amplitude-blind **third-harmonic phase-locking energy**, on a ring with a period-3 on-site coefficient.

The complex numbers are notation for planar 2-vectors. Every coefficient is real, and the update never multiplies by *i*. The only exception is the phase rotation applied by the synchronizer.

Under that identification, there are three places where **the current interpretation is wrong**:

1. **The GR1 "background-dependent response geometry" (weights r², conductances g·rᵢrⱼ) is not emergent geometry.** It is the flat Euclidean state metric written in polar coordinates. Equivalently, it is the Doob (ground-state) transform of a discrete Schrödinger operator whose ground state is the background. GR0 §3.1 already said this about the polar chart, and GR1 §8 then called it "genuine geometry".
2. **The "magnetism" observable is vector spin chirality / U(1) bond current, a kinematic bilinear.** Its persistence and sign alternation in M2/M3 come from a period-doubling of the synchronizer step operated beyond its explicit stability limit, the same class of event as the SIMS g\*=2/3 edge. None of it is electromagnetic.
3. **The GR2 "spectral circulation" is real and survives the continuous-time limit, but it is *non-reciprocity*.** It is an imaginary (Hatano–Nelson-type) gauge flux created by combining an amplitude-weighted phase coupling (strength g) with an amplitude-blind one (strength ℓ=3λ). Nothing physical circulates.

QED/U(1) gauge theory is **not** a strong next comparison. The weak-gravity comparison failed every defining test and should be retired. The live comparators are dissipative oscillator lattices and generalized XY models, non-Hermitian/non-reciprocal linear response, and coupled-map/Floquet maps for the phenomena that only exist at finite step size.

---

## 1. What is unquestionably present (Q1)

All of the following are **EXACT**. Each is either already proved in the stack or re-verified here.

| # | Structure | Where |
|---|---|---|
| 1 | Pre-sync stage = Ω − ∇V. V = εΣ(sᵢ²/4 − kᵢsᵢ/2) + (g/2)Σ\|Ωᵢ−Ωⱼ\|² is a lattice Ginzburg–Landau (φ⁴ soft-spin) energy: ferromagnetic exchange for g>0, antiferromagnetic for g<0. | GR0 §4(d) |
| 2 | Sync stage = one gradient step of U_λ = −(λ/3)Σ cos 3(θⱼ−θᵢ) in **flat angle** coordinates. | GR0 §3.2 |
| 3 | The full map is a Lie–Trotter composition of the two gradient steps. Each is self-adjoint in its own metric: Euclidean for stage 1, flat-phase for stage 2. Their composite is self-adjoint in neither. | GR1 §3 |
| 4 | Symmetry: global U(1) (= SO(2) of planar spins), complex conjugation Z₂, translation by 3, and D₃ₕ on the triad geometry. **No local U(1).** The on-site term has local U(1). The synchronizer has a **local Z₃** symmetry (θⱼ→θⱼ+2πnⱼ/3; verified). The graph coupling g breaks both down to global. | checks §D |
| 5 | Strictly dissipative near its attractors: real multipliers inside the unit disk, plus one neutral Goldstone direction. No symplectic or Hamiltonian structure, and a non-conserved intensity budget. | GR0 §§3–5 |
| 6 | A gapped amplitude mode (multiplier 1−2εk) and a diffusive Goldstone (phase) mode. | GR0 §5.3 |
| 7 | Exact finite Fourier/Bloch reducibility on N=3q rings. | GR0, GR2 §5 |
| 8 | Non-self-adjoint composite phase response on unequal backgrounds: Kolmogorov cycle obstruction, non-real Bloch modes for N≥9, and an exceptional point on the six-ring. | GR1, GR2 |
| 9 | Flip bifurcations at explicit-step stability edges. | SIMS, Paper G M2 |
| 10 | Chirality/current bilinears Aᵢⱼ = Im(Ω̄ᵢΩⱼ), and the U(3) moment map ΩΩ† = S − iA. | Paper G §2 |
| 11 | Fixed flat geometry: Euclidean panels, and matched transport with identity holonomy. | GR0 §4 |

## 2. Closest legitimate comparators (Q2)

| Native object | Known object | Status |
|---|---|---|
| Pre-sync update | Explicit-Euler step of time-dependent GL / model-A dynamics (Hohenberg–Halperin). Equivalently a Stuart–Landau lattice with zero frequencies and dispersion (the "real GL" corner of the CGLE family; Aranson–Kramer). | **EXACT** |
| Whole recurrence | A complex **coupled map lattice** (Kaneko): local cubic map plus diffusive coupling on a ring, in discrete time. | **EXACT** (model class) |
| Bond energy −g rᵢrⱼ cos θᵢⱼ − (λ/3) cos 3θᵢⱼ | **Generalized XY model** with q=3 harmonic (Lee–Grinstein; Korshunov; Poderoso–Arenzon–Levin 2011), with soft amplitudes. | **EXACT** for the energy functions. **STRUCTURAL** for the dynamics, which is *not* the gradient of their sum (item 3 above). |
| GR0 multipliers, stability domains | Von Neumann amplification factors of explicit Euler; the domains are CFL-type step limits. | **EXACT** |
| GR0 long-wave phase symbol | Heat (diffusion) equation. | **LIMITING** |
| GR1 weights r², conductances g rᵢrⱼ | (a) The flat C^N metric in polar coordinates, bᵢ = rᵢφᵢ. (b) The Doob / ground-state transform of H = I + g(Δ − diag(Δr/r)), for which H r = r: the stationary measure is r² ("ψ₀²"). (c) Physically, the superfluid / Josephson phase stiffness g rᵢrⱼ and the phase capacity rᵢ². | **EXACT** (checks §A) |
| GR1 eq. (5), screened Poisson | GL healing-length equation. The screening mass 2εk is the amplitude-mode gap, and ξ² = g/(2εk). | **EXACT** (form) |
| GR1 cycle obstruction, GR2 Γ | Kolmogorov criterion. A non-reciprocal hopping matrix with **net imaginary flux**: Hatano–Nelson class, where positive diagonal similarities are the "imaginary gauge transformations" and cycle products are their Wilson loops. | **EXACT** as linear algebra (checks §§B, C, F) |
| GR2 six-ring nilpotent fixture | Exceptional point (EP2), with a real → defective → complex unfolding. | **EXACT**, but it sits at ℓ=1 (map-only, §7) |
| GR2 eq. (15): transverse mode colliding defectively with the Goldstone multiplier | A **Goldstone-mode exceptional point**. This is the mechanism of non-reciprocal phase transitions (Fruchart–Hanai–Littlewood–Vitelli 2021) and of parity-breaking drift bifurcations (Coullet–Goldstein–Gunaratne 1989). | **STRUCTURAL**, unexplored |
| Paper G C = x×y, Γ = eᵀC | (a) Vector spin chirality sⱼ×sₖ of planar spins. Γ is the triangle chirality of frustrated XY magnets, and the Fourier entrances f₁, f₂ are its two chiral 120° states. (b) U(1) Noether bond current of the GL energy. (c) The spin (antisymmetric) part of a 3D coherency matrix, or angular momentum of the 3D isotropic oscillator (Jordan–Schwinger): I² = \|Ω·Ω\|² + 4\|C\|², and f₁·f₁ = 0 is a circular (C-point) state. | **EXACT** (checks §D) |
| SA0 Gram closure | Descent of an equivariant map to the orbit space C³/U(1) (or /O(2)); the Gram entries are the generating invariants. | **EXACT** (standard invariant theory) |
| CM0 counts | Equivariant polynomial (Molien-type) counting under D₃ₕ. | **EXACT** (standard) |
| TL1/TL2 lens gain G = √I, with I = (2θ − sin 2θ)/π | I(θ) is **exactly the diffraction-limited incoherent MTF of a circular pupil** at normalized frequency d/2r (the autocorrelation of a disk). TL2's Hölder exponents are the MTF's (1−ν)^{3/2} cutoff behaviour. | **EXACT** |

## 3. Reassessing the weak / low-energy gravity comparison (Q3)

**What matched, and how well**

- *A background-dependent inner product.* **EXACT**, but it is the polar chart of a flat metric (§2), so it is not emergent.
- *A Poisson-type static response.* **STRUCTURAL**. It is screened (Yukawa), with range equal to the GL coherence length. Newtonian gravity is defined by being *unscreened*.
- *Diffusive long-wave behaviour.* **LIMITING**. This is the heat equation, not a wave equation.
- *Flat matched transport.* Consistent with **zero** field.

**What did not match: the defining tests**

1. **Universality / equivalence principle.** Gravity's core property is that all perturbations see one metric. Here three different metrics appear:
   - amplitude perturbations obey H − 2εR² (self-adjoint in the Euclidean metric);
   - pre-sync phase perturbations obey R⁻¹HR (self-adjoint in R²);
   - the synchronizer is self-adjoint in the flat metric I.
2. **Propagation.** The dynamics is dissipative and first-order. At the homogeneous background the spectrum is real, so there are no light cones and no waves (GR0 §6.1). Analogue gravity (Barceló–Liberati–Visser) gets an acoustic metric only from *conservative* condensate phase dynamics. That needs imaginary GL coefficients, and the native model has none.
3. **Dimension.** The ring is one-dimensional. A 1D Riemannian metric has no intrinsic curvature: any weighting is a reparametrization, and only spectral data survive (a discrete inhomogeneous string). In 1+1 dimensions the Einstein tensor vanishes identically. Weak-field GR on the native ring is therefore *dimensionally impossible*, not merely unproven.
4. **Sourcing.** To first order, a static inhomogeneity κ sources only the **gapped** amplitude mode (GR1 eq. 5–6). The massless (phase) channel is not sourced by a static scalar. So the long-range channel is exactly the one that does not respond to "mass".

**What was overlooked**

The four points above, plus the fact that the established literature for "geometry from response", analogue gravity, explains precisely why this model cannot qualify: it is dissipative.

**Verdict:** retire the gravity comparison. The GR checkpoint names are historical labels only.

## 4. QED / U(1) gauge theory (Q4)

**Present:** global U(1); a Noether bond current Im(Ω̄ᵢΩⱼ); ring winding numbers; conjugation Z₂.

**Absent:**

- local U(1) invariance;
- link or gauge variables;
- a field strength (the only connection-like object, matched transport, has identity holonomy, i.e. it describes zero field);
- a Gauss law or minimal coupling;
- current conservation (the dynamics is dissipative and the intensity budget has sources);
- any Schrödinger/Dirac-type *i* in the evolution;
- a photon-like mode.

The state is complex only in notation: the map is an O(2)-vector map with real coefficients.

The **only native local redundancy is Z₃**, on the synchronizer stage, and g breaks it. If a gauge-type comparison is wanted at all, the honest candidate is a discrete Z₃ (p-atic-type) structure, and even that is only **STRUCTURAL**.

**Verdict:** QED is superficially attractive because the state is complex. It is not a strong next comparison. It would become live only if a dynamical link variable existed, which would be a model extension.

## 5. Does the magnetism work strengthen an EM/QED comparison? (Q5)

**No.**

- **M1** is rigorous, but it is kinematics plus representation theory. C is the chirality / current / spin bilinear that every complex 3-vector has. W = TC is its unique D₃ₕ-equivariant linear attachment to the panels (Paper G Prop. 1). There are no curl/div field equations, no sources, and no magnetization. Time reversal is undefined natively, and the two natural readings disagree about whether C is even or odd under it:
  - XY reading, where Ω → −Ω plays time reversal: C is T-even.
  - Polarization reading, where conjugation plays time reversal: C is T-odd.
- **M2/M3** persistence is map-only. At the M2 flip λ_c = 0.3675, so the synchronizer **alone** multiplies the triad transverse phase mode by 1 − 9λ_c = **−2.307**: it overshoots, since |·| > 1 already for λ > 2/9. The pre-sync damping m₁ = 0.433 brings the product back to exactly −1. W then alternates sign every step. The small-step flow has no counterpart: an equilibrium of a flow cannot period-double. This is the same class of event as SIMS (g\* = 2/3 ⇔ 1−3g = −1).

**Where the M-series does point:**

- frustrated XY chirality (with conjugation as the Z₂ chirality);
- circulating supercurrents in ring condensates / Josephson arrays;
- 3D polarization spin.

**Conditional:** *if* the iteration index is declared to be a physical drive period, then the period-2 chirality alternation is a subharmonic response of a kicked dissipative system, comparable to classical discrete time crystals (Yao–Nayak–Balents–Zaletel 2020). That is an owner decision, not a result.

## 6. Where the finite-ring, phase, circulation, chirality, response and orientation results point (Q6)

Ranked by fit:

1. **Dissipative oscillator lattices / TDGL / generalized XY (q=3).** The model's home. **EXACT** at the level of definitions.
2. **Non-reciprocal (non-Hermitian) response.** Hatano–Nelson flux, exceptional points, non-reversible consensus/Markov operators, non-reciprocal phase transitions. **EXACT** for the GR1/GR2 algebra. The *dynamical* consequence is open (§9).
3. **Coupled-map lattices / Floquet maps.** For everything that requires an O(1) step: M2/M3, the six-ring EP, the λ=1/9 rank-one case, SIMS.
4. **Frustrated XY chirality and U(3) polarization kinematics.** For M1.
5. **Equivariant bifurcation theory.** For CM0/SA0/D₃ₕ; the paper already cites Golubitsky–Stewart–Schaeffer.
6. **Fourier optics.** For the TL lens gain.

Not supported: QED; weak gravity; conservative nonlinear waves or solitons (real GL has neither dispersion nor a Hamiltonian).

## 7. Step-size dissection, performed as a check in this review

Substitute (ε, g, λ) = h·(ε̂, ĝ, λ̂) and let h → 0. The question is which results belong to the underlying flow and which exist only for the finite-step map.

| Result | Small-step fate | Evidence |
|---|---|---|
| GR0 spectrum and stability domains | Spectrum → diffusion (flow). Stability domains are CFL limits (map). | GR0 formulas |
| GR1 triad cycle obstruction | **Flow-level.** Leading coefficient g ℓ (g − ℓ)·[(c/a + a/b + b/c) − (a/c + b/a + c/b)]. | native 𝒞/h³ → −5.170e-3 vs generator −5.192e-3 (checks §C) |
| GR2 Γ, E = ℓ(1+3g) − g | E = **(ℓ − g)** + **3gℓ**: a flow-level mismatch term plus a splitting term. The complex Bloch *rates* converge to the generator's complex rates. They vanish at ℓ̂ = ĝ (generator), and vanish **identically** if the synchronizer were amplitude-weighted (diagnostic counterfactual only, not a proposal). | checks §§B, F (h = 1e-1…1e-4) |
| Generator on N=12 | Net imaginary flux log(Π_fwd/Π_bwd) = −0.0091 ≠ 0: Hatano–Nelson type. | checks §F |
| Six-ring nilpotent (ℓ=1); λ=1/9 rank-one | **Map-only** (O(1) parameters). | GR2 §6 |
| M2 flip (λ_c = 0.367); M3 capture | **Map-only.** | Paper G |
| SIMS g\* = 2/3 | **Map-only.** | prior falsifier |
| M1 identities | Independent of the time interpretation. | Paper G §2–3 |

So the flow-level content of the whole stack is **non-reciprocal phase diffusion on a chiral period-3 soft-spin XY ring.** Whether the map-only content is physics (Floquet) or a discretization effect depends on whether the iteration index is physical time. The model cannot decide that; it is the owner's call.

## 8. What deserves synthesis before further research (Q7)

**Scientifically strongest: GR1 + GR2, the non-reciprocity block.** It is exact, it survives the continuous-time limit, and it maps onto an active research area. It is already inside NRG v0.1, so the right move is a **v0.2 positioning revision, not new research**:

- (a) name the model class (TDGL / Stuart–Landau / CML; generalized XY q=3);
- (b) replace the "response geometry" language with the polar-chart / Doob explanation;
- (c) add the decomposition E = (ℓ − g) + 3gℓ and its reading as amplitude-weighted vs amplitude-blind coupling;
- (d) add the missing literature context: non-Hermitian / non-reciprocal physics (Hatano–Nelson; Fruchart et al.), GL/CGLE, and coupled map lattices. The current six references are all pure mathematics.

**Technically strongest: Paper G's computer-assisted theorems.** They are rigorous, but their content is map-specific. Any future synthesis should call W "vector chirality", not magnetism.

## 9. The one discriminating calculation (Q8)

QED and gravity are already eliminated on structural grounds (§§3–4), so a calculation spent on them would be wasted. The live fork is:

> **effectively variational (equilibrium generalized XY)** vs **non-reciprocal / active**.

The canonical discriminator between those is the **drift test**.

**Calculation.** On the triad, and on N=9, take three distinct kᵢ in the small-step regime (λ far below 2/9). Find the native *relative equilibria* F(Ω) = e^{iω}Ω on the chirality-carrying branches: the Fourier-entrance / winding families and their conjugates. Then determine whether ω ≠ 0, and compute its leading coefficient. Saddles count; stability is not required.

**Why it is decisive.** A U(1)-invariant gradient system can have **no** relative equilibrium with ω ≠ 0, stable or not. Non-reciprocal systems generically do (You–Baskaran–Marchetti 2020; Fruchart et al. 2021).

At flow level, weight each phase velocity by rᵢ² and sum. The pre-sync contribution cancels by U(1) invariance, leaving

**ω = −Σ rᵢ² ∂_{θᵢ}U / Σ rᵢ²**  (**SPECULATIVE** heuristic; derived here, not verified)

So ω is nonzero exactly when the synchronizer torques correlate with the amplitude inhomogeneity. It vanishes identically for an amplitude-weighted synchronizer.

**Predicted symmetry structure, which doubles as a kill test.** ω should be:

- odd under conjugation (f₁ ↔ f₂);
- odd under k-order reversal (k₁,k₂,k₃) → (k₁,k₃,k₂);
- exactly zero when two kᵢ are equal (reflection symmetry restored).

**Outcomes:**

- **ω ≡ 0 at flow level.** "Circulation" is a linear-response feature only. The right comparator is equilibrium generalized-XY physics, and chirality is static order.
- **ω ≠ 0 at flow level, with the predicted symmetries.** The model is a non-reciprocal (active) chiral ratchet. This would be the first native result in which "circulation" means motion, and in which M1's bond currents are real steady currents. Next comparators: non-reciprocal phase transitions and active chiral matter.
- **ω ≠ 0 only at O(1) step sizes.** A CML/Floquet effect.

Neither outcome revives QED or gravity.

**Hygiene:** solve the relative-equilibrium equations directly, with ω as an unknown, plus a phase gauge. Do not infer ω from long runs. Use several values of h and run the symmetry tests. This uses only the native map; nothing is added to the model.

---

## Sources

- Hatano & Nelson, *Localization transitions in non-Hermitian quantum mechanics* (1996): https://arxiv.org/abs/cond-mat/9603165
- Fruchart, Hanai, Littlewood & Vitelli, *Non-reciprocal phase transitions*, Nature (2021): https://research-portal.st-andrews.ac.uk/en/publications/non-reciprocal-phase-transitions/
- You, Baskaran & Marchetti, *Nonreciprocity as a generic route to traveling states*, PNAS (2020): https://arxiv.org/abs/2005.07684
- Coullet, Goldstein & Gunaratne, *Parity-breaking transitions of modulated patterns* (1989): https://dx.doi.org/10.1103/PhysRevLett.63.1954
- Poderoso, Arenzon & Levin, *New ordered phases in a class of generalized XY models* (2011): https://ar5iv.labs.arxiv.org/html/1008.0868
- Jordan–Schwinger map, the 3D oscillator, and polarization parameters: https://arxiv.org/pdf/0801.4744
- Yao, Nayak, Balents & Zaletel, *Classical discrete time crystals*: https://arxiv.org/pdf/1801.02628

Standard results cited from general knowledge, not re-fetched: Hohenberg–Halperin (1977); Aranson–Kramer (2002); Kaneko's coupled map lattices (1984); Barceló–Liberati–Visser, *Analogue gravity* (2005); the circular-pupil MTF.
