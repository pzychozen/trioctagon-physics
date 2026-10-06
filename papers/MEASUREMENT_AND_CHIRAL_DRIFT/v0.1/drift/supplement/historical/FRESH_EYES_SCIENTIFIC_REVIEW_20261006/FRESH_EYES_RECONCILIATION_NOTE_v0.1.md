# Reconciliation note to the fresh-eyes review v0.1

Claude · 6 October 2026 · read-only. **No new simulations were run, and nothing published was edited.** The kernel, NRG, Paper G and review v0.1 are unchanged, and the drift experiment has not been run.

This note keeps the accepted model-class diagnosis. It narrows or replaces the specific statements of review v0.1 listed in §5. Everything new below is a written derivation, labelled **DERIVED HERE** where it is not already established in the stack. Each must be checked symbolically at Gate D0 (§3.6) before it is relied on.

Companion files are unchanged and lie alongside this note in `research/FRESH_EYES_SCIENTIFIC_REVIEW_20261006/`:

| File | SHA-256 |
|---|---|
| `FRESH_EYES_SCIENTIFIC_REVIEW_v0.1.md` | `65dc00967ccdecc1c513bd8b3046568f475894ae0b960db314e1c0575c75b90d` |
| `fresh_eyes_checks.py` | `807e79cf4bda818835d19bc072b5802d23fff312dddc96c7df0ab26e7dca6d2d` |
| `fresh_eyes_checks_output.txt` | `92314cd236004d47cc3216aca509414cc05b062ed33605897f01fda7792eb31e` |

Notation: F_K is the native map with coefficient triple K = (K₀,K₁,K₂), so that k_j = K_{j mod 3} on N = 3q. ℓ = 3λ. Pre-sync values are Ω̃, and δ_i is the synchronizer increment computed from the pre-sync phases.

---

## 1. Restored qualifications

### 1a. Finite-step descent

The "gradient" language in review v0.1 refers to **increment identities**, not descent steps.

- The pre-sync increment equals −∇V in Euclidean coordinates (GR0 §4(d)). The synchronizer increment equals −∇_φU_λ in flat phase coordinates (GR0 §3.2).
- Neither stage decreases its function in general.
  - GR0's witness Ω=(2,2,2), ε=1, g=0, k=1 sends V from 6 to 168 and intensity from 12 to 48.
  - The pre-sync stage is a descent step only where the Hessian of V along the step stays below 2I. V is quartic, so this holds only locally.
  - For the synchronizer, the Hessian of U_λ = 3λ Σ_e cos(3Δ_e) L_e has norm at most 12λ, so **λ < 1/6** is a sufficient condition for descent on the nonzero domain. This is the same bound as GR0's sufficient phase domain. DERIVED HERE.
- No common U(1)-invariant Lyapunov function for the composite map is known.
- The no-drift argument for gradient systems used in v0.1 §9 applies **only to flows, or to maps with a strict U(1)-invariant descent function**. It is not available for the native map at finite step.

### 1b. Dissipation is local

- Near a strictly stable fixed point, all non-group multipliers lie inside the unit disk. There they are real at the equal background (GR0) and can be non-real on unequal backgrounds (GR2).
- Because |det DF| < 1 there, no smooth invariant volume, and hence no symplectic structure, exists in a neighbourhood of such a point.
- Nothing global follows: the native map can grow intensity (1a).

### 1c. Zero-stratum symmetry

| Symmetry | Domain where it holds (with `Arg₀(0)=0`) |
|---|---|
| Common phase U(1) | **Only where every pre-sync component is nonzero** (GR0 §5.1; Paper G §1.1). On the zero stratum the assigned phase 0 does not rotate, so neighbouring increments change. |
| Conjugation C | All of ℂᴺ (Paper G §1.1). |
| Dihedral site permutations, with coefficients carried along (§3.2) | All of ℂᴺ. |
| **Local Z₃ of the synchronizer**, Ω_j → e^{2πin_j/3}Ω_j | All of ℂᴺ. A zero site keeps phase 0, but every argument enters only through sin 3(·) and e^{i·}, and 3·(2π/3)n ∈ 2πℤ. DERIVED HERE; the numerical check in §D used nonzero states only. |
| Pre-sync stage under any U(1) rotation | All of ℂᴺ (polynomial). |

So every statement about relative equilibria, drift or winding below assumes **all Ω_i ≠ 0 and all Ω̃_i ≠ 0**.

## 2. Gravity: what the analyzed operators actually establish

Five layers must be kept apart:

| Layer | What it is | Established |
|---|---|---|
| **Coordinate metric** | The flat Euclidean metric of ℂᴺ, ds² = Σ(dr_i² + r_i²dθ_i²). Its angular coefficients are the r_i². | GR1's weights R² are this chart factor. In Cartesian imaginary coordinates b = Rφ, the pre-sync block is H, with uniform conductance g (GR1 eq. 9; checks §A). Equivalently, it is the Doob transform by the ground state r (Hr = r). |
| **Response operators** | Jacobian blocks at the analyzed backgrounds: H − 2εR² (amplitude), P = R⁻¹HR (pre-sync phase), S (synchronizer), and the composite J = SP. | At the equal in-phase background the spectrum is real (GR0). On unequal three-periodic backgrounds, generically no positive diagonal symmetrizer exists (GR1), and non-real Bloch multipliers appear for N≥9 (GR2). The static response to κ is screened and amplitude-only at first order in η (GR1 eqs. 5–6). |
| **Symmetrizing inner products** | Any SPD G with GJ = JᵀG. | Exists only for a real semisimple spectrum, and is non-unique when it exists (GR2 §2). No privileged one is selected. |
| **Interaction graph** | The cycle C_N (the triad is K₃). It is a combinatorial graph, of dimension 1 as a graph. | It is not identified with any space (GR0 §3.1). |
| **Physical spacetime** | — | **Not identified by any checkpoint.** The fixed panel shell in ℝ³ is a separate, fixed embedded geometry (GR0). |

**Restricted statements that replace review v0.1 §3:**

1. **No common node-local metric.** The analyzed linear blocks are not self-adjoint in one common positive diagonal inner product. Even P (with R²) and S (with I) differ, and their composite generically admits no positive diagonal weight at all (GR1). This is a fact about these operators. It does not exclude non-diagonal or other constructions, or geometry extracted from other observables.
2. **Propagation, corrected.** At the equal background no linear mode oscillates (GR0 §6.1). On unequal backgrounds, damped modes with non-real multipliers **do** exist (GR2). What the analyzed operators lack is an *undamped* propagating branch: all multipliers lie inside the unit disk at the strictly stable backgrounds studied. Review v0.1's "nothing propagates" is withdrawn.
3. **Screening.** At first order in η on the analyzed in-phase branch, the static response is screened (H₀ = 2εkI − gΔ is positive definite) and confined to the amplitude block. Nothing is claimed about nonlinear or other backgrounds.
4. **Dimension, retracted as an exclusion.** The remarks "a 1D metric has no intrinsic curvature" and "the Einstein tensor vanishes in 1+1D" apply only *if* the interaction graph (or graph × iteration) were identified with physical space(time). No such identification exists, so these are conditional remarks, not exclusions. Emergent geometry from other carriers (state space, the shell, families of rings) is unaddressed. "Dimensionally impossible" is withdrawn.
5. **Revised verdict.** The analyzed operators supply no gravity analogue. The comparison is retired as a working hypothesis *for these operators*. That is not a theorem about the model.

## 3. Drift test: corrected design

### 3.1 Objects

A **relative equilibrium** is a state with F_K(Ω) = e^{iω}Ω, all Ω_i, Ω̃_i ≠ 0, and ω ∈ ℝ/2πℤ. It is defined modulo U(1); ω is U(1)-invariant.

Two **branch labels** are used:

- the winding w(Ω) = (1/2π) Σ_j Arg(Ω_{j+1}Ω̄_j) ∈ ℤ, which is defined when no neighbour phase difference equals π;
- the oriented chirality Γ(Ω) = Σ_j Im(Ω̄_jΩ_{j+1}).

### 3.2 Joint transformations (DERIVED HERE)

For a site permutation σ, define (P_σx)_j = x_{σ⁻¹(j)}. The Laplacian and the synchronizer commute with dihedral permutations, and the on-site term carries its coefficient along. Hence

  **F_{P_σk}(P_σΩ) = P_σ F_k(Ω).**

Combined with F_k(CΩ) = C F_k(Ω), this moves the data (state, coefficient order, label, angle) together:

| Operation | State | Coefficient triple | w, Γ | ω |
|---|---|---|---|---|
| Common phase R_α (nonzero domain) | e^{iα}Ω | K | unchanged | **ω** |
| Conjugation C | Ω̄ | K | **−w, −Γ** | **−ω** |
| Reflection ρ: j ↦ −j | Ω_{−j} | (K₀,K₂,K₁) | **−w, −Γ** | **ω** |
| C∘ρ | Ω̄_{−j} | (K₀,K₂,K₁) | w, Γ | **−ω** |
| Translation τ: j ↦ j+1 | Ω_{j−1} | (K₂,K₀,K₁) | unchanged | **ω** |
| τ³ | Ω_{j−3} | K | unchanged | ω (a symmetry) |

The derivations are one line each. For example, F_{ρK}(P_ρΩ) = P_ρ(e^{iω}Ω) = e^{iω}P_ρΩ, and F_{ρK}(CP_ρΩ) = e^{−iω}CP_ρΩ. Reflection reverses the ring orientation, so it reverses w and Γ.

Consequences:

- **Pure reflection preserves ω.** It changes both the coefficient order and the label.
- **Conjugation reverses ω** at a fixed coefficient order.
- **At a fixed label, reversing the coefficient order reverses ω** (via C∘ρ).

Review v0.1's "ω odd under k-order reversal" is correct only in this last, fixed-label form.

### 3.3 Two equal coefficients: what is needed to infer zero drift

Suppose K₁ = K₂. (For K₀ = K₁ use j ↦ 1−j; for K₀ = K₂ use j ↦ 2−j.) Then ρ preserves K, so C∘ρ is a symmetry of F_K that maps (w, ω) to (w, −ω). This alone does **not** give ω = 0. Four extra hypotheses are needed:

- **Z1, isolation.** The relative equilibrium is locally unique modulo U(1) on its branch: the multiplier 1 is algebraically simple, carried by the common-phase direction alone.
- **Z2, invariance of the branch.** C∘ρ maps the branch to itself, for example because it is the unique continuation of a C∘ρ-invariant reference state. Z1 and Z2 together give C∘ρ(Ω) = e^{iβ}Ω, and hence e^{2iω} = 1, so **ω ∈ {0, π}**.
- **Z3, excluding π.** Rule out ω = π by continuity from a reference with ω = 0, or by a bound |ω| < π/2. This is not vacuous: §3.6 exhibits native ω = π relative equilibria.
- **Z4, nonzero domain** (§1c).

Without Z1–Z2, a symmetry-breaking bifurcation inside the K₁ = K₂ family can produce a pair of relative equilibria exchanged by C∘ρ, with ω = ±ω* ≠ 0. That is a drift pitchfork (Coullet–Goldstein–Gunaratne type). **Equal coefficients do not by themselves imply zero drift.**

### 3.4 Exact finite-step drift identity (DERIVED HERE)

On any relative equilibrium satisfying §3.1:

  **Σ_i r_i² sin(ω − δ_i) = 0,  i.e.  ω ≡ arg Σ_i r_i² e^{iδ_i}  (mod π).**

*Proof.* The sum Σ_i Ω̄_iΩ̃_i is real for every Ω. Its terms are |Ω_i|²[1 + ε(k_i − |Ω_i|²)] plus g⟨Ω, ΔΩ⟩, and Δ is real symmetric. So Σ_i r_i r̃_i sin(θ̃_i − θ_i) = 0. On a relative equilibrium, r̃_i = r_i (the synchronizer preserves moduli) and θ̃_i − θ_i = ω − δ_i. ∎

Corollaries:

- (i) If λ = 0, then ω ∈ {0, π}.
- (ii) Σ_i δ_i = 0 exactly, because the edge terms cancel in antisymmetric pairs. So at small δ, ω = Σ_i (r_i² − r̄²)δ_i / Σ_i r_i² + O(δ³). Drift requires the synchronizer torques to correlate with the amplitude inhomogeneity.
- (iii) This replaces review v0.1's heuristic formula, and **every computed drift must satisfy it to working precision.** This is a built-in consistency check.

### 3.5 Per-step angle versus limiting rate

Use the small-step family (ε, g, λ) = h(ε̂, ĝ, λ̂).

- ω(h) is the **per-step angle**. ω(h) → 0 trivially as h → 0, because F → identity.
- The flow-level quantity is the **rate** Ω̂ = lim ω(h)/h. By §3.4 it equals −Σ r_i² ∂_{θ_i}Û / Σ r_i², evaluated at the generator's relative equilibrium, provided the generator branch exists and is nondegenerate.

Report ω(h), ω(h)/h and ω(h)/h² over at least three values of h. The classification is:

| Behaviour | Classification |
|---|---|
| Ω̂ ≠ 0 | **Flow-level drift** |
| Ω̂ = 0 but ω(h)/h² → const ≠ 0 | **Splitting-level drift** |
| Drift only at O(1) step size | **Map-only drift** |

A nonzero ω(h) at a single h classifies nothing.

### 3.6 Reference branch: existence before parameter choice (Gate D0, DERIVED HERE)

**Equal-coefficient twisted family.** On N = 3q with all k_j = k̄, take Ω_j = A e^{iφj}, with φ = 2πm/N and h_m = 2 − 2cos φ. Then ΔΩ = −h_mΩ, and every synchronizer increment cancels: sin(3φ) + sin(−3φ) = 0. So

- F(Ω) = cΩ with c = 1 + ε(k̄ − A²) − g h_m.
- **The ω = 0 fixed branch** (c = 1) exists **iff A_m² = k̄ − g h_m/ε > 0**, with ε ≠ 0. It has w = m (for |φ| < π) and Γ = N A_m² sin φ ≠ 0 whenever φ ∉ {0, π}. It is C∘ρ-invariant (Z2 holds at η = 0).
- c = −1 gives native relative equilibria with **ω = π**, where A² = k̄ − (g h_m − 2)/ε. These are why Z3 is needed.
- In the small-step family, A_m² = k̄ − ĝh_m/ε̂ does not depend on h.

**Paper G's parameters fail existence on the triad.** For m = ±1, h = 3 and 3g/ε = 12, while k̄ ≈ 2.858. So those parameters must not be reused for this test.

**Nondegeneracy (Z1 at η = 0).** Write the perturbation as e^{iφj}(A + a_j + ib_j), and use the Fourier mode e^{iθj} with θ = 2πp/N and u = 1 − cos θ. The linearization block is

  M(θ) = diag(1, σ_θ) · [[D_a, −iX], [iX, D_b]],

with

- D_a = 1 − 2εA² − 2g cos φ · u
- D_b = 1 − 2g cos φ · u
- X = 2g sin φ sin θ
- σ_θ = 1 − 2ℓ cos(3φ) · u

At φ = 0 this reproduces GR0's μ_a and μ_φ. The background acts on perturbations like a Peierls phase e^{±iφ}. Reference nondegeneracy requires:

- εA² ≠ 0 (the θ = 0 amplitude multiplier differs from 1);
- for every p = 1, …, N−1: (D_a − 1)(σ_θ D_b − 1) − σ_θ X² ≠ 0.

Stability is not required. Under these conditions the implicit-function theorem continues the relative equilibrium (unknowns Ω on a slice, plus ω) analytically to K = k̄ + ηκ, with ω(0) = 0.

**Leading order is forced by symmetry.** Along the continued branch, ω is an analytic function of x = ηκ on the zero-sum plane.

- Translation by one site maps the reference to itself up to phase, so ω is C₃-invariant (§3.2).
- C∘ρ makes ω odd under the reflections.

Hence ω is divisible by V(x) = (x₀−x₁)(x₁−x₂)(x₂−x₀):

  **ω = c_m η³ (κ₀−κ₁)(κ₁−κ₂)(κ₂−κ₀) + O(η⁵).**

Inside this neighbourhood, Z1–Z4 hold automatically, and ω vanishes when two κ coincide. Whether c_m ≠ 0 is exactly the open question.

The drift is cubic in η, the same order as GR2's Γ. The experiment therefore needs GR2-grade precision (100-digit or interval arithmetic), not binary64. That the drift must be cubic is a design requirement, not a result.

### 3.7 Branch-restricted conclusions

These replace review v0.1's outcome list. Each finding is tied to the branch label w, the coefficient triple K, the step-size parameters, and the resolved order in η and h.

| Finding | Licensed conclusion |
|---|---|
| ω = 0 (or c_m = 0) | The **examined branch** does not drift, at the examined parameters, to the resolved order. This says **nothing** about variational structure: GR1/GR2 already show that the linear response at flow level is non-reversible. It says nothing about other branches or parameters either. |
| c_m ≠ 0, with Ω̂ ≠ 0 | The examined branch is a flow-level rotating relative equilibrium: a native nonlinear consequence of non-reciprocity. |
| Drift only at splitting or map level | Classify as in §3.5. |

Every drift number must also satisfy the §3.4 identity and transform as in §3.2. Concretely, conjugate entrances must give −ω, and C∘ρ-related coefficient orders must give −ω.

## 4. Unchanged

The following stand as written in v0.1:

- the model-class identification;
- the polar-chart and Doob reading of R²;
- the chirality / bond-current / U(3) identities;
- the E = (ℓ−g) + 3gℓ decomposition and the fixture checks;
- the QED assessment, with "global U(1)" read as in §1c;
- the map-only status of M2/M3, the six-ring exceptional point and the SIMS edge. On that last point the precise wording is: in any small-step family all multipliers are 1 + O(h), so a −1 crossing is unreachable.

## 5. Statements of review v0.1 superseded here

| v0.1 location | Replaced by |
|---|---|
| §1 item 4, "global U(1)" | §1c (nonzero pre-sync domain only) |
| §1 item 5, §2 "gradient step" | §1a–1b (increment identities; local dissipation; descent conditions) |
| §3 entire verdict, "nothing propagates", "dimensionally impossible" | §2 |
| §5 "an equilibrium of a flow cannot period-double" | §4 (1 + O(h) multipliers) |
| §9 symmetry predictions | §3.2–3.3 |
| §9 heuristic ω formula | §3.4 |
| §9 outcomes | §3.7 |
| §9 parameter choice | §3.6 (existence and nondegeneracy first) |
| §7 "vanish identically if amplitude-weighted" | Verified only at the tested fixtures. In general it requires the weighted synchronizer to be positive definite. |

**No further step is started.** The next gate, D0, is the symbolic check of §§1a, 1c, 3.2, 3.4 and 3.6, together with a reference-parameter selection satisfying §3.6. The drift experiment comes after that.
