# PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS

Independent mathematical-physics derivation. Phase Bridge II: from the oriented tangent geometry of the first bridge to a candidate genuine dynamical phase.

Author: Claude (independent derivation). Date: 2026-09-21.
Baseline: `trioctagon-physics` HEAD `562fbb5`. PAPER_A / PAPER_C frozen; `kernel_physics` clean; first bridge = COMPLETE (51/51).
Sources read (read-only, nothing modified): `research/top_to_recursive_bridge/{TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md, UNRESOLVED_INTERFACE_ASSUMPTIONS.md, bridge_symbolic_results.txt}`, `kernel_physics/{geometry.py, dynamics.py, covering.py}`, `papers/PAPER_A/PAPER_A_SYMBOLS_AND_THEOREMS_v0.3.md`, `papers/PAPER_C/…v0.3.1`, `CURRENT_STATE.md`.

**Governing discipline.** The geometry supplies the complex structure `J_i` exactly. Everything past that — a symplectic form, a Hamiltonian, a frequency, a continuous flow — is examined for whether it is *forced by geometry* or *added as an assumption*. The answer to the framing question is **not assumed to be yes**. Classifications used: `EXACT`, `STANDARD_KNOWN_MATHEMATICS`, `DERIVED_FROM_STATED_ASSUMPTION`, `CANDIDATE_PHYSICAL_INTERPRETATION`, `NUMERICAL_CHECK_SUGGESTED`, `UNRESOLVED`, `CONTRADICTED`.

**One-line answer.** The oriented tangent geometry supports a mathematically justified *kinematic* symplectic/Kähler structure `(g,J,ω)` **exactly**; a genuine dynamical phase `Ω̇ = -iνΩ` follows **only after adding a quadratic Hamiltonian and a frequency scale ν that the geometry does not supply**. The phase rotation is real and rigorous, but it is `DERIVED_FROM_STATED_ASSUMPTION`, not from the shell.

---

## 0. Fixed data recovered from source (used throughout)

Outward unit face normals (`geometry.py`, first bridge §3), all in the `z=0` plane:
```
n_A = (-√3/2,  1/2, 0),   n_B = (0, -1, 0),   n_C = (√3/2, 1/2, 0)     |n_i| = 1
```
Vertical axis `e_z=(0,0,1)`; oriented in-plane tangent `t_i = e_z × n_i = (-n_{i,y}, n_{i,x}, 0)`:
```
t_A = (-1/2, -√3/2, 0),   t_B = (1, 0, 0),   t_C = (-1/2, √3/2, 0)
```
Each face-center tangent plane `T_i = span(t_i, e_z)` is a **vertical** plane (Paper C: panel planes vertical), with oriented orthonormal frame `(t_i, e_z)`. Encoding `v_i = q_i t_i + p_i e_z`, `Ω_i = q_i + i p_i`. Complex structure `J_i v = n_i × v`.

Frozen Paper-A map (`dynamics.py`, exact): with `L_3 = [[-2,1,1],[1,-2,1],[1,1,-2]] = 11^T - 3I = -3P_⊥`, spectrum `{0,-3,-3}`,
```
Ω̃ = Ω + ε Ω⊙(k - |Ω|²) + g L_3 Ω          # pre-sync amplitude/coupling
φ_i ← φ_i + λ [ sin 3(φ_{i-1}-φ_i) + sin 3(φ_{i+1}-φ_i) ]   # harmonic-3 synchronizer
```
**There is no `iνΩ` term and no `dt` in the frozen map** (`dynamics.py` docstring: "no clock, dt, noise, normalization, geometry input"). This is the central fact against which §§3,7,9 are measured.

---

## 1. Review scope

Bounded to: the first bridge's tangent construction on the three face-center planes; a minimal Hamiltonian phase generator; the resulting free-phase symmetry; the relation to the frozen Paper-A amplitude map and harmonic-3 synchronizer; reflection/anti-symplectic structure; chiral transformation laws (`Z_chiral`, `J_eff`); and the `L_3` unitary centralizer as an SU(3)-carrier statement. No repository file was modified; nothing was executed; no `C³⊗C²` lift, recursion, DMQPF, SRG, or Standard-Model interpretation is attempted (all deferred by the order).

---

## 2. The symplectic / area form — `EXACT`

**Claim.** On each face plane the geometry already fixes a nondegenerate 2-form, the canonical oriented area form, with `ω_i(v,w) = g_i(J_i v, w)`.

**Derivation.** In the oriented orthonormal frame `(t_i, e_z)`, compute `J_i` on the frame using `J_i v = n_i × v` and the triple product `n×(e_z×n) = e_z(n·n) - n(n·e_z) = e_z`:
```
J_i t_i = n_i × t_i = n_i × (e_z × n_i) = e_z
J_i e_z = n_i × e_z = -(e_z × n_i) = -t_i
```
So on `(q,p)` coordinates `v = q t_i + p e_z`, `J_i v = q e_z - p t_i = (-p, q)`; matrix `J_i = [[0,-1],[1,0]]`, and `E(J_i v) = -p + iq = i(q+ip) = iΩ_i` (**confirms the first bridge's `E∘J = i∘E`**). With `g_i = I₂` in this frame,
```
ω_i(v,w) = g_i(J_i v, w) = (J_i v)·w = (-p_v, q_v)·(q_w, p_w) = q_v p_w - p_v q_w = (dq ∧ dp)(v,w).
```

**Answers to the four required questions.**
1. **Nondegenerate?** Yes — `ω_i` in the frame is `[[0,1],[-1,0]]`, `det = 1 ≠ 0`. `EXACT`.
2. **Canonical oriented area form?** Yes — `ω_i(t_i, e_z) = g(J_i t_i, e_z) = g(e_z,e_z) = +1`, the signed area of the positively-oriented unit square `(t_i, e_z)`. `ω_i` *is* the Euclidean area 2-form of the oriented plane. `EXACT`.
3. **Transformation under symmetries.** For any induced tangent action `Γ_G` (an isometry, `g(Γ_G a, Γ_G b) = g(a,b)`) satisfying the first bridge's identity `Γ_G J = det(G) J Γ_G`,
   ```
   (Γ_G^* ω)(v,w) = ω(Γ_G v, Γ_G w) = g(J Γ_G v, Γ_G w)
                  = g(det(G) Γ_G J v, Γ_G w) = det(G) g(Γ_G J v, Γ_G w) = det(G) g(J v, w) = det(G) ω(v,w).
   ```
   So **`Γ_G^* ω = det(G) ω`**. `EXACT`.
4. **Mirrors symplectic or anti-symplectic?** Proper (`det = +1`): `Γ_G^* ω = +ω` → **symplectic**. Improper (`det = -1`): `Γ_G^* ω = -ω` → **anti-symplectic**. `EXACT`. (Sign convention note: the result is a *scaling by `det(G)`* and is therefore robust — choosing the opposite orientation for `ω` rescales both sides identically and does not change "proper = symplectic, improper = anti-symplectic".)

**Compatible triple.** `(g_i, J_i, ω_i)` satisfy `ω_i(v,w) = g_i(J_i v, w)`, `J_i^T = -J_i`, `J_i^2 = -I`, `g_i(J_i v, J_i w) = g_i(v,w)`. This is a **flat Kähler structure on each plane**, hence on `W_tan ≅ C³`. `STANDARD_KNOWN_MATHEMATICS`, with the *specific planes* fixed by the tri-octagon normals (`EXACT`).

---

## 3. Minimal Hamiltonian phase generator — geometry gives `ω`, dynamics needs an added `H` and `ν`

**Setup.** `H_i(v_i) = (ν_i/2)‖v_i‖² = (ν_i/2)(q_i² + p_i²)`, `ν_i ∈ ℝ`.

**Hamilton's equation from the symplectic convention.** Use the standard convention `ι_{X_H} ω_i = dH_i` with `ω_i = dq∧dp` (from §2). Writing `X_H = q̇ ∂_q + ṗ ∂_p`:
```
ι_{X_H}(dq∧dp) = q̇ dp - ṗ dq  ≟  dH_i = ν_i(q dq + p dp)
⇒  q̇ = ν_i p,   -ṗ = ν_i q   ⇒   (q̇, ṗ) = (ν_i p, -ν_i q).
```
In vector form `v̇_i = (ν_i p, -ν_i q) = -ν_i(-p, q) = **-ν_i J_i v_i**`. Hence the sign, **not chosen by preference**:
```
v̇_i = -ν_i J_i v_i      (standard convention ω = dq∧dp, ι_X ω = dH, H ≥ 0)
```
**Complex form.** `Ω̇_i = q̇ + iṗ = ν_i p - i ν_i q = -i ν_i (q + i p) = **-i ν_i Ω_i**`, and therefore
```
Ω_i(t) = e^{-i ν_i t} Ω_i(0).                                  (PROVED)
```

**Sign is convention-locked, not preference-locked.** The magnitude `ν_i` and the fact that the flow is a *rigid rotation of each plane* are convention-independent. The **handedness/sign** is fixed jointly by (a) the orientation of `ω_i` (equivalently the sign in `E∘J=i∘E`) and (b) the sign convention in Hamilton's equation `ι_Xω=±dH`. Flipping exactly one of these gives `v̇_i = +ν_i J_i v_i`, `Ω̇_i = +iν_i Ω_i`, `Ω_i(t)=e^{+iν_i t}Ω_i(0)`. The tri-octagon fixes the orientation of `ω` (via the ambient right-handed orientation and outward normals); the Hamilton-equation sign is a textbook choice. So the sign is determined **once both conventions are fixed**, and the geometry fixes only one of the two.

**Strict classification of the ingredients.**
| Object | Status |
|---|---|
| `J_i`, `ω_i` (the two-plane, its orientation, the area form) | **PURE GEOMETRY** — `EXACT` from `n_i` + ambient orientation |
| `H_i = (ν_i/2)‖v_i‖²` (that the generator is *this* quadratic) | **ADDED HAMILTONIAN ASSUMPTION** — simplest `C₃`-invariant choice, not forced |
| the frequency scale `ν_i` (its value, even its existence as a rate) | **ADDED** — geometry has no intrinsic time unit (see §13.7) |
| `v̇_i = -ν_i J_i v_i`, `Ω̇_i = -iν_iΩ_i`, `Ω_i(t)=e^{-iν_it}Ω_i(0)` | **DERIVED DYNAMICS** — exact consequence of geometry-`ω` + added `H` |

The geometry is **not** credited with determining `ν_i`. It determines only that *if* a positive quadratic Hamiltonian is imposed on the geometric `ω`, the motion is a uniform phase rotation of `Ω_i` at some rate that must be supplied externally.

---

## 4. Three-face symmetry constraints on `ν_A, ν_B, ν_C`

`W_tan = T_A ⊕ T_B ⊕ T_C`. The proper 120° rotation `C₃` maps frame `(t_A,e_z) → (t_B,e_z) → (t_C,e_z)` (cyclically) and acts on the complex coordinates by the cyclic permutation `R` (`EXACT`, first bridge §3). The total generator of the free flow is `diag(-iν_A, -iν_B, -iν_C)`.

- **Does exact face equivalence force a common `ν`?** If the Hamiltonian `H = Σ_i H_i` is required invariant under the spatial `C₃` (which the shell's own symmetry realizes), then because `C₃` permutes the three planes, invariance of `Σ (ν_i/2)‖v_i‖²` forces `ν_A = ν_B = ν_C ≡ ν`. `DERIVED_FROM_STATED_ASSUMPTION` (assumption = "the Hamiltonian respects the spatial symmetry"). Equivalently: `[R, diag(-iν_i)] = 0 ⇔ ν_A=ν_B=ν_C`.
- **What breaks if they differ?** The generator `diag(-iν_i)` no longer commutes with `R`; the `C₃` symmetry of the *dynamics* is broken (the three planes precess at different rates and the cyclic relabeling is no longer a symmetry). The static geometry is untouched — only the added dynamics breaks `C₃`.
- **Which choices retain only `C₃`?** Common `ν` (equal frequencies) retains the proper cyclic symmetry acting `ℂ`-linearly. Improper symmetries act **conjugate-linearly** (first bridge; §10 below), so even at equal `ν` a mirror does not commute with the flow in the naive `ℂ`-linear sense — it *reverses* it.
- **Which retain the full proper spatial symmetry?** Equal `ν` retains the whole **proper** point group `D₃ = {C₃, 3C₂'} ⊂ D_{3h}` acting `ℂ`-linearly (each proper element has `det=+1`, so `Γ_G J = +J Γ_G`, hence commutes with `diag(-iν)`); the improper coset (`σ_h, σ_v, S₃`) never commutes `ℂ`-linearly.

`FREQUENCY_DEGENERACY_REQUIRED_BY_C3 = YES` (given a symmetry-respecting Hamiltonian). Note the first bridge explicitly refused to assume full `D_{3h}` acts `ℂ`-linearly; this section respects that — only the proper subgroup does.

---

## 5. Symmetry group of the free equal-frequency dynamics — `EXACT`

For `Ω̇_i = -iνΩ_i` (all equal), the generator is the **scalar** `M = -iν·I₃`. Separate four distinct notions the order asks not to conflate:

| Structure | Group | Meaning |
|---|---|---|
| independent phase rotation of each plane | `U(1)³` | `Ω_i ↦ e^{iα_i}Ω_i`; conserves each `\|Ω_i\|²` separately — **three independently conserved `U(1)` charges** |
| common temporal evolution | diagonal `U(1)` | `Ω ↦ e^{-iνt}Ω`; this *is* the flow, a one-parameter subgroup of `U(1)³` |
| basis transformations (internal) | `U(3)` | any unitary of `C³` commutes with the scalar `M` and preserves `Σ\|Ω_i\|²` → full `U(3)` at equal `ν` |
| spatial `C₃` action | `ℤ₃ ⊂ U(3)` | the cyclic permutation `R`; a discrete geometric symmetry, distinct from internal phase |

**The requested distinction.** For the *free, uncoupled, equal-frequency* system the two readings **coincide**: because the three planes are dynamically uncoupled and each `‖v_i‖²` is separately conserved, the system genuinely has **three independently conserved `U(1)` charges** = `U(1)³`, i.e. it is "three oscillators each possessing its own phase plane" **and** "three independently conserved `U(1)` charges" at once. The internal symmetry *enlarges* to the full `U(3)` precisely because the frequencies are degenerate (a scalar generator commutes with everything unitary). This enlargement is fragile: it is broken down to the centralizer of whatever is added next —
- adding the geometric coupling `L_3` → reduces `U(3)` to `U(1)×U(2)` (§12);
- adding the entrywise cubic `εΩ_i(k_i-|Ω_i|²)` → reduces further to the entrywise-covariant subgroup (common phase `U(1)` ⋊ `C₃`, and `U(1)³` only when the phases are locked to per-plane rotations that the cubic tolerates — the cubic `Ω_i|Ω_i|²` is invariant under per-plane `U(1)`, so `U(1)³` survives the cubic but **not** `L_3`).

So the "larger group" (`U(3)`) is real but is an artifact of exact degeneracy and no coupling; the physically robust internal symmetry of the *coupled* nonlinear system is far smaller. `EXACT`.

---

## 6. Relation to standard Hamiltonian mechanics — `STANDARD_KNOWN_MATHEMATICS`

Everything in §§2–5 is textbook once `J_i` is in hand:
- **Harmonic-oscillator phase space.** `(q_i,p_i)` with `H_i=(ν_i/2)(q²+p²)` is the isotropic planar oscillator; its flow is uniform rotation — the classical fact that `q+ip` evolves as `e^{∓iνt}`.
- **Symplectic two-planes.** `(ℝ², dq∧dp)` is the model symplectic vector space; each face plane is a copy.
- **Compatible triple `(g,J,ω)`.** A Euclidean metric plus orthogonal complex structure plus `ω=g(J·,·)` is the definition of a (flat, finite-dimensional) **Kähler** vector space. `W_tan ≅ C³` with the standard Hermitian form is flat Kähler.
- **Hamiltonian rotations in `ℝ²`.** The generator of the flow is `-νJ`, the standard skew generator of `SO(2)`.

**What is particular to the Tri-Octagon vs. generic.** Only the *placement*: which three 2-planes inside `ℝ⁹` (and their orientations) are selected — these are fixed by the outward normals `n_A,n_B,n_C` and the ambient right-handed orientation. The oscillator *dynamics* is entirely generic. We claim **no novelty** in the mechanics; the geometry-specific content is the identification of the planes and their `C₃`/mirror transformation laws. `STANDARD_KNOWN_MATHEMATICS` (mechanics) + `EXACT` (the specific planes).

Desirable chain, honestly labelled:
```
Tri-Octagon orientation ⇒ J_i ⇒ ω_i                       [EXACT, geometry]
+ quadratic Hamiltonian H_i ⇒ Hamiltonian phase rotation   [DERIVED_FROM_STATED_ASSUMPTION]
```

---

## 7. Comparison to the Paper-A amplitude map — `Stuart–Landau` parentage of a term Paper A does **not** contain

Proposed continuous parent:
```
Ω̇_i = iν Ω_i + ε Ω_i(k_i - |Ω_i|²) + g (L_3 Ω)_i.
```
Group the per-node part: `iνΩ_i + εk_iΩ_i - ε|Ω_i|²Ω_i = (εk_i + iν)Ω_i - ε|Ω_i|²Ω_i`. This is **exactly the Stuart–Landau / Hopf normal-form oscillator** `ż = (a+iω)z - b|z|²z` with linear coefficient `a+iω = εk_i + iν` and nonlinear coefficient `b = ε`. The remaining `g L_3 Ω` is **linear diffusive (graph-Laplacian) coupling**. Therefore:

> The continuous parent is a network of three diffusively-coupled Stuart–Landau oscillators on the complete graph `K₃` — equivalently a discrete complex Ginzburg–Landau system. `STANDARD_KNOWN_MATHEMATICS` / `EXACT` (as an ODE identification).

**Crucial caveat (against over-claiming).** The frozen Paper-A map has **no `iνΩ` term** (`dynamics.py`; first bridge §7 proved the pre-sync increment is the *negative real gradient* of
`V = ε Σ_i(¼|Ω_i|⁴ − ½k_i|Ω_i|²) + (g/2)Σ_{i<j}|Ω_i−Ω_j|²`,
i.e. purely dissipative/gradient, with **no skew phase generator**). So the Stuart–Landau connection is **exact for the continuous parent but describes a system strictly larger than Paper A**: the parent = (Paper-A gradient field) + (the added skew `iνΩ` phase generator of §3). The phase generator is *precisely the piece Paper A lacks*.

**Discretization relationship (proved, not asserted).** Drop the added `iνΩ` term and consider `Ω̇ = ε Ω⊙(k−|Ω|²) + g L_3 Ω =: F_amp(Ω)`. **Explicit (forward) Euler with step `h`** gives `Ω_{n+1} = Ω_n + h F_amp(Ω_n)`; at `h = 1` this is **algebraically identical** to the frozen pre-sync map `Ω̃ = Ω + εΩ⊙(k−|Ω|²) + gL_3Ω`. Hence:

> The frozen pre-sync amplitude/coupling step **is explicit Euler at `dt = 1`** of the gradient vector field `F_amp` — `EXACT` as an algebraic identity, but a *first-order* (not exact-flow) discretization at a large step.

`STUART_LANDAU_CONNECTION = EXACT_FOR_CONTINUOUS_PARENT_ONLY`. `PAPER_A_CONTINUOUS_PARENT = EXISTS_BUT_ADDS_A_SKEW_TERM_ABSENT_FROM_PAPER_A`.

---

## 8. Higher-harmonic synchronization — `STANDARD_KNOWN_MATHEMATICS`, harmonic 3 **not** forced by geometry

Continuous phase system (from the synchronizer):
```
φ̇_i = ν + K Σ_{j∼i} sin 3(φ_j − φ_i).
```
This is the **Kuramoto–Sakaguchi model with third-harmonic coupling** on `K₃` (all-to-all for 3 nodes). Known-mathematics answers:

1. **Fixed phase-difference classes.** Relative-phase equilibria satisfy `sin 3(φ_j−φ_i) = 0 ⇒ 3Δφ ∈ πℤ ⇒ Δφ ∈ {0, ±π/3, ±2π/3, π} (mod 2π)`. The *phase-locked, `C₃`-compatible* families are `Δφ ∈ {0, ±2π/3}`.
2. **Why harmonic 3 admits `Δφ = 0, ±2π/3`.** For `Δφ = ±2π/3`, `sin 3(±2π/3) = sin(±2π) = 0`; for `Δφ=0`, `sin 0 = 0`. The multiplier `3` maps the three cube-roots-of-unity phase offsets to `0 (mod 2π)`, so the third harmonic has the in-phase state **and** the two 120° splay states as simultaneous equilibria (higher-harmonic multistability: harmonic `m` produces `m` distinct locked families).
3. **Stability by sign of `K`.** Linearizing on `K₃`, near `Δφ=0` `sin 3Δφ ≈ 3Δφ` (effective coupling `+3K`), and near `Δφ=±2π/3` `sin 3(2π/3+δ)=sin 3δ ≈ 3δ` (also slope `+3K`). For **`K>0`** both the in-phase and the 120° splay families are linearly stable (co-existing attractors); for **`K<0`** their stability inverts. Exact Jacobian eigenvalues and basin structure: `NUMERICAL_CHECK_SUGGESTED` (the frozen kernel's own atlas already records default `λ=0.001` regimes; a dedicated continuous-time `K₃` third-harmonic stability computation is the clean check).
4. **Relation to `C₃` geometry.** The equal-amplitude 120° state is exactly the `C₃`-symmetric configuration living in the **transverse (unbalanced) sector** `V₃^⊥` — the same transverse plane that carries the geometric complex structure (first bridge §7; Paper A "120° state lies in the transverse Fourier sector"). So harmonic 3's splay family and the geometric `C₃` two-plane coincide as *sets of states*, which is suggestive but is not a derivation of the coupling.
5. **Does geometry force harmonic 3?** **NO.** The first bridge proved (and I re-confirm) that `Σ_{j≠i} sin m(φ_j−φ_i)` is `S₃`-equivariant for **every** positive integer `m`; `C₃` selects none. Harmonic 3 is an **independent model assumption** in Paper A. `HARMONIC_3_FORCED_BY_GEOMETRY = NO` — preserved from the first bridge.

Continuous parent for the synchronizer as a discretization: `φ_i ← φ_i + λ Σ sin 3(φ_j−φ_i)` is **explicit Euler at `dt=1`** of `φ̇_i = λ Σ sin 3(φ_j−φ_i)` (the `K=λ`, `ν=0` case), consistent with §9.

---

## 9. Discrete vs continuous — first-order Lie–Trotter split at `dt=1`, **not** an exact flow

Write the full frozen step `F = S ∘ A` where
```
A(Ω) = Ω + ε Ω⊙(k−|Ω|²) + g L_3 Ω          # amplitude/coupling substep
S(Ω) : φ_i ↦ φ_i + λ Σ_{j∼i} sin 3(φ_j−φ_i)  # phase-sync substep (amplitude-preserving)
```
From §§7–8: `A` is **explicit Euler (`dt=1`)** of `X_A: Ω̇ = ε Ω⊙(k−|Ω|²)+gL_3Ω`, and `S` is **explicit Euler (`dt=1`)** of `X_S: φ̇_i = λ Σ sin 3(φ_j−φ_i)` (a phase-space vector field tangent to the tori `|Ω_i|=const`). Therefore:

> `F = S_{Δt} ∘ A_{Δt}` with `Δt = 1` has the form of a **Lie–Trotter operator split** of the continuous system `Ω̇ = X_A(Ω) + X_S(Ω)`. `DERIVED_FROM_STATED_ASSUMPTION`.

**Is it exact, first-order, or not a legitimate splitting?**
- It is a **legitimate first-order splitting** of `X_A + X_S`: Lie–Trotter `S_{Δt}∘A_{Δt}` reproduces the flow of `X_A+X_S` to `O(Δt²)` — but with two compounding first-order errors here, because *each* substep is itself only explicit Euler (`O(Δt²)` local error), not the exact sub-flow.
- It is **not exact.** At `Δt=1` (a large step) the map is far from the time-1 flow of `X_A+X_S`; neither substep is an exact flow, and the composition is not the exact flow of any simple autonomous field.
- The added `iνΩ` phase generator of §3 is a **third** field `X_ν: Ω̇=iνΩ` that appears in **neither** substep. A three-way split `S∘A∘Φ_ν` (with `Φ_ν = e^{iνΔt}`, the *exact* rotation) would be required to include it, and Paper A contains no such factor.

**Consequence for the physics kernel's time variable.** Because the step is Euler at `dt=1`, the discrete step-index is **not** a principled sampling of the continuous parent's time `t`; the continuum time acquires meaning only in a `dt→0` refinement that Paper A does not take. So, honestly: `DISCRETE_STEP_HAS_PRINCIPLED_CONTINUUM_TIME = NO (at dt=1)`; a principled time would require re-deriving Paper A as a small-step integrator, which is out of scope and not claimed.

---

## 10. Reflection, conjugation, anti-symplectic structure — `EXACT`

From §2(4): for improper `G` (`det G = -1`), `Γ_G^* ω = -ω`. Explicitly, using the first bridge's `Γ_G J = det(G) J Γ_G = -J Γ_G` and `Γ_G` orthogonal:
```
(Γ_G^* ω)(v,w) = g(J Γ_G v, Γ_G w) = -g(Γ_G J v, Γ_G w) = -g(Jv,w) = -ω(v,w).
```
So **improper spatial symmetries are anti-symplectic involutions** (`Γ_G^*ω = -ω`; and each listed mirror squares to the identity, hence *involution*). `EXACT`.

**Action on `Ω` and on phase evolution** (first bridge frames):
- Horizontal mirror `σ_h` (`z→-z`): `Ω ↦ conj(Ω)`. Under the flow `Ω(t)=e^{-iνt}Ω(0)`: `conj(e^{-iνt}Ω) = e^{+iνt}conj(Ω)` — the mirror **reverses the phase rotation** (sends frequency `-ν` to `+ν`). This is a **time-reversal-like** action on the phase.
- Vertical mirror `σ_v` (`x→-x`): `Ω ↦ -T conj(Ω)` (`T` swaps A↔C). Same conjugation of the temporal phase, composed with the transverse reflection `T`.

**Interpretation, deliberately un-named.** An anti-symplectic involution that conjugates `Ω` and reverses the oriented phase rotation is the mathematical precursor of a parity/conjugation operation. Using the required neutral vocabulary: this is an **orientation reversal / reflection / complex conjugation / anti-symplectic involution**. It is **not** yet a CP analogue — a genuine CP statement needs a charge and a combined transformation not derived here. `EXACT` (transformation law), `UNRESOLVED` (physical CP meaning). `REFLECTION_ANTI_SYMPLECTIC = YES`.

---

## 11. First look at chirality — transformation laws only

Let `Ω = a + i b`, `a = Re Ω`, `b = Im Ω ∈ ℝ³` (three real, three imaginary channel components).

### 11.1 `Z_chiral = a × b` (channel-space cross product; matches kernel `Re(Ω)×Im(Ω)`)

| Transformation | Law | Result |
|---|---|---|
| common phase `Ω ↦ e^{iα}Ω` | `a↦cosα·a−sinα·b`, `b↦sinα·a+cosα·b` | `a×b ↦ (cos²α+sin²α)(a×b) = **a×b**` — **INVARIANT** under common `U(1)` |
| conjugation `Ω ↦ conj(Ω)` | `a↦a`, `b↦−b` | `a×b ↦ −(a×b)` — **ODD** (parity-odd) |
| channel permutation `σ∈S₃` (orthogonal `P_σ`) | `a↦P_σ a`, `b↦P_σ b` | `(P_σ a)×(P_σ b)=det(P_σ)·P_σ(a×b)` — **pseudovector**: `+P_σ Z` for even `σ` (`C₃`), `−P_σ Z` for odd `σ` (transposition) |
| spatial reflection (via tangent rep) | `σ_h: Ω↦conj(Ω)` ⇒ `Z↦−Z`; `σ_v: Ω↦−Tconj(Ω)` ⇒ `a↦−Ta, b↦Tb` ⇒ `Z↦ (−Ta)×(Tb)= T(a×b)` | covariant with a mirror-dependent sign |

Derivations `EXACT`. Summary: `Z_chiral` is `U(1)`-**invariant**, conjugation-**odd**, an `S₃` **pseudovector**, and mirror-covariant — the expected signature of a handedness readout.

### 11.2 `J_eff = Im(Ω₁ conj(Ω₂) Ω₃)`

Net `U(1)` weight of `Ω₁ conj(Ω₂) Ω₃` is `(+1)+(−1)+(+1) = +1`. Consequences (all `EXACT`):
- **Common `U(1)`:** `Ω₁conj(Ω₂)Ω₃ ↦ e^{iα}·Ω₁conj(Ω₂)Ω₃`, so `J_eff ↦ Im(e^{iα}P) = |P|sin(argP+α)` — **NOT invariant; covariant with weight +1.** (This is a genuine finding: as literally written, `J_eff` is *not* a `U(1)`-invariant observable, unlike `Z_chiral`.)
- **Conjugation:** `P ↦ conj(Ω₁)Ω₂conj(Ω₃) = conj(P)`, so `J_eff = Im(P) ↦ −Im(P)` — **ODD**.
- **Cyclic permutation `1→2→3→1`:** `P ↦ Ω₂conj(Ω₃)Ω₁ = Ω₁Ω₂conj(Ω₃)`, a *different* monomial (the conjugated index moved), so `J_eff` is **not cyclic-invariant as written**; it transforms within a triple of related cubic monomials. A cyclic-*invariant* chiral scalar would instead be the closed-loop product `Im(Ω₁conj(Ω₂)·Ω₂conj(Ω₃)·Ω₃conj(Ω₁)) = |Ω₁||Ω₂||Ω₃|·… ` (the plaquette phase, `U(1)`-invariant), or the sum `Σ_i Im(conj(Ω_i)Ω_{i+1})` (bilinear, `= Σ` of `Z_chiral` components). **Not adopted or redefined** — flagged only to locate the invariant.
- **Algebraic independence from `Z_chiral`:** `J_eff` is **cubic** in `(a,b)` while `Z_chiral` is **bilinear**; they are algebraically independent (different degree; `J_eff` is not a polynomial in the components of `a×b`). `EXACT`.

`CHIRAL_TRANSFORMATION_LAWS = DERIVED` (with the flagged caveat that the literal `J_eff` is `U(1)`-covariant, not invariant). No Standard-Model meaning assigned — preparation for Phase Bridge III only.

---

## 12. SU(3) carrier structure — centralizer of `L_3`, `EXACT`

`C³` is the fundamental carrier of `U(3)` (hence `SU(3)`). The geometric coupling `L_3 = -3P_⊥ = -3I + 3uu^†`, `u=(1,1,1)^T/√3`, has spectral decomposition
```
L_3 u = 0        (eigenvalue 0, multiplicity 1, eigenspace ℂu — the balanced line)
L_3 |_{u^⊥} = -3 (eigenvalue -3, multiplicity 2, eigenspace u^⊥_ℂ ≅ ℂ² — the transverse plane).
```
**Centralizer (commutant) of `L_3`.** A unitary commutes with `L_3` iff it preserves each eigenspace:
```
Centralizer_{U(3)}(L_3) = U(1)_{ℂu} × U(2)_{u^⊥} ≅ U(1) × U(2).
Centralizer_{SU(3)}(L_3) = S(U(1) × U(2)) = { diag-block(e^{iθ}, V) : V∈U(2), e^{iθ}det V = 1 } ≅ U(2).
```
`EXACT`. **Fixing the balanced line `ℂu` leaves a full unitary action `U(2)` on the transverse `u^⊥_ℂ ≅ ℂ²`** — precisely the structure the order anticipated. So the geometric coupling singles out, inside the `SU(3)` that acts on the `C³` carrier, the subgroup
```
S(U(1) × U(2)) ≅ U(2)  ⊂  SU(3),
```
the natural stabilizer of a line in `C³`. This is the exact mathematical basis for a later `SU(3) → S(U(1)×U(2))` reduction question (structurally the same pattern as an electroweak-type `SU(3)→SU(2)×U(1)` embedding — **but no Standard-Model identification is made here**).

**Scope of the symmetry, honestly.** `U(1)×U(2)` is the centralizer of the **linear** coupling `L_3` and of the free equal-`ν` flow's scalar generator (which commutes with all of `U(3)`, so does not narrow it). The **nonlinear** entrywise term `εΩ_i(k_i-|Ω_i|²)` is *not* `U(2)`-covariant (it is only entrywise/diagonal + permutation covariant), so the *full nonlinear map's* exact internal symmetry is smaller than `U(1)×U(2)` — roughly `U(1)_{common} ⋊ C₃` with per-plane `U(1)³` surviving the cubic but broken by `L_3`. The clean, exact statement is: **`L_3`'s unitary centralizer is `U(1)×U(2)` (`SU(3)`: `S(U(1)×U(2))`)**; that is the SU(3)-carrier result, not a symmetry of the whole dynamics.

`L3_UNITARY_CENTRALIZER = U(1)×U(2)  [SU(3): S(U(1)×U(2)) ≅ U(2)]`. `SU3_CARRIER_STRUCTURE = EXACT`.

---

## 13. Falsification pass (strongest surviving statement, not the most ambitious)

1. **Are the tangent planes physical phase spaces or convenient coordinates?** The planes are **geometrically canonical** (fixed by `n_i` + ambient orientation), so *not arbitrary* coordinates — but they are **kinematic**. No field or observable has been shown to *take values* in them; the first bridge's `UNRESOLVED_INTERFACE_ASSUMPTIONS` still stands ("what real face observable carries the two quadratures?"). Verdict: symplectic structure `EXACT`; "physical phase space" = `CANDIDATE_PHYSICAL_INTERPRETATION` / `UNRESOLVED`.
2. **Is the quadratic Hamiltonian arbitrary?** Largely yes: `H_i=(ν_i/2)‖v‖²` is the simplest `C₃`-invariant, `SO(2)`-invariant choice, but any `f(‖v_i‖²)` is equally invariant and would give amplitude-dependent frequency. The *quadratic* choice is a **minimality assumption**, not forced. `DERIVED_FROM_STATED_ASSUMPTION`.
3. **Does any natural field theory produce the tangent vectors as observables?** Not derived. The first bridge's welded-scalar perimeter ansatz **collapsed to one real coefficient** (`CONTRADICTED` for that ansatz); no field theory yielding three tangent-vector observables exists yet. `UNRESOLVED`.
4. **Do mirrors really act anti-symplectically under the chosen convention?** Yes, and **robustly**: `Γ_G^*ω = det(G)ω` is a *scaling* by `det(G)`, independent of the orientation chosen for `ω` and of the Hamilton-equation sign. So "improper = anti-symplectic" survives any consistent convention change. `EXACT`, convention-robust.
5. **Does the continuous dynamics legitimately relate to Paper A?** Partially. The **gradient part** of Paper A is exactly explicit-Euler(`dt=1`) of `X_A`; the synchronizer is exactly explicit-Euler(`dt=1`) of `X_S`; together a first-order Lie–Trotter split. But the **phase generator `iνΩ` is absent from Paper A**, and `dt=1` is not the exact flow. So the relationship is a *first-order discretization of a strictly larger continuous system*. `DERIVED_FROM_STATED_ASSUMPTION`, not an equivalence.
6. **Is the Stuart–Landau connection exact or superficial?** **Exact as an ODE identification** of the continuous parent (Hopf normal form + diffusive coupling). **Superficial if asserted of the frozen map**, which lacks the skew term and is only first-order-consistent at `dt=1`. State the two separately.
7. **Does introducing `ν` add a physical scale absent from the geometry?** **Yes.** Paper C is a static Euclidean object; its only intrinsic scales are lengths (`s=√2−1`, apothem `1/2`, etc.). A frequency `ν` (dimension time⁻¹) has **no geometric origin** — it is a new dimensional input. `PHYSICAL_FREQUENCY_DERIVED_FROM_GEOMETRY = NO`.
8. **Would an alternative observable be equally natural?** Yes: the first bridge lists paired field/oscillator quadratures and the single transverse phase plane; the perimeter-circulation route (collapsed) was another. The tangent-vector encoding is the **most concrete** but **not unique or forced**. `UNRESOLVED`.

**Strongest surviving statement.** *The oriented tri-octagon geometry supplies, exactly and canonically, a per-face Euclidean two-plane with a compatible triple `(g,J,ω)` — a flat Kähler structure on `W_tan ≅ C³` — under which any imposed positive quadratic Hamiltonian generates a uniform phase rotation `Ω_i(t)=e^{-iν_i t}Ω_i(0)`, with proper spatial symmetries acting symplectically/`ℂ`-linearly and improper ones acting anti-symplectically/conjugate-linearly. The frequency `ν`, the choice of Hamiltonian, and the identification of any physical field on these planes are **not** supplied by the geometry.* Everything weaker than this (a genuine, geometry-forced dynamical phase) is **not** established.

---

## 14. Numerical checks suggested (not run here; no repo change)

- `NUMERICAL_CHECK_SUGGESTED`: exact Jacobian eigenvalues / basins of the continuous `K₃` third-harmonic Kuramoto `φ̇_i = ν + KΣ sin3(φ_j−φ_i)` at both signs of `K`, confirming co-stability of in-phase and 120° families (§8.3).
- `NUMERICAL_CHECK_SUGGESTED`: verify `A = I + F_amp` equals explicit Euler(`dt=1`) of `X_A` on random states to machine precision, and measure the `O(Δt²)` deviation of `F = S∘A` from the time-`Δt` flow of `X_A+X_S` as `Δt→0` (§9).
- `NUMERICAL_CHECK_SUGGESTED`: confirm `Z_chiral` `U(1)`-invariance and conjugation-oddness, and `J_eff` `U(1)`-covariance (weight +1) on random `Ω` (§11).
- `NUMERICAL_CHECK_SUGGESTED`: confirm `Centralizer_{U(3)}(L_3)=U(1)×U(2)` by random-unitary commutator tests on the eigenspaces of `L_3` (§12).

These are confirmations of analytic results, not substitutes for them.

---

## 15. Handoff note for Codex / Phase Bridge III

Ready to hand off: the compatible triple, the anti-symplectic mirror law, the `L_3` centralizer, and the chiral transformation laws are all `EXACT` and self-contained. **Blocking for a genuine physics kernel:** (i) a physical observable that takes values in the tangent planes (still `UNRESOLVED` from bridge I); (ii) an independently justified frequency scale `ν` (absent from geometry); (iii) a principled continuum-time interpretation of the `dt=1` step (absent). Phase Bridge III should target (i)–(iii) and the CP-analogue question (anti-symplectic involution + a charge), **not** assume the dynamical phase is already established.

---

```
ORIENTED_TANGENT_COMPLEX_STRUCTURE        = EXACT (J_i = n_i×·, J_i²=-I, orthogonal)
SYMPLECTIC_FORM                           = EXACT (ω_i = g(J_i·,·) = dq∧dp; nondegenerate; canonical oriented area form)
QUADRATIC_HAMILTONIAN_PHASE_FLOW          = DERIVED_FROM_STATED_ASSUMPTION (v̇=-νJv, Ω̇=-iνΩ, Ω(t)=e^{-iνt}Ω(0); sign convention-locked)
PHYSICAL_FREQUENCY_DERIVED_FROM_GEOMETRY  = NO (ν is an added time scale; geometry has no intrinsic frequency)
THREE_COMPLEX_DYNAMICAL_AMPLITUDES        = CONDITIONAL (exact kinematic C³; dynamical only after adding H and ν)
FREE_PHASE_DYNAMICS_SYMMETRY              = U(1)³ conserved charges, enlarging to U(3) at equal ν; diagonal U(1) = the flow; C₃ = discrete spatial ℤ₃
REFLECTION_ANTI_SYMPLECTIC                = YES (Γ_G^*ω = det(G)ω; improper mirrors anti-symplectic involutions; conjugate Ω, reverse phase)
PAPER_A_CONTINUOUS_PARENT                 = EXISTS but adds a skew iνΩ term ABSENT from Paper A (Paper A pre-sync = pure gradient)
STUART_LANDAU_CONNECTION                  = EXACT for the continuous parent (Hopf normal form + diffusive L_3 coupling); only first-order (Euler dt=1) for the frozen map
HIGHER_HARMONIC_KURAMOTO_CONNECTION       = EXACT (third-harmonic Kuramoto–Sakaguchi on K₃; splay families Δφ∈{0,±2π/3}; co-stable for K>0, invert for K<0 — NUMERICAL_CHECK_SUGGESTED)
HARMONIC_3_FORCED_BY_GEOMETRY             = NO (Σ sin m(φ_j-φ_i) is S₃-equivariant for every m; preserved from bridge I)
CHIRAL_TRANSFORMATION_LAWS                = DERIVED (Z_chiral: U(1)-invariant, conj-odd, S₃-pseudovector; J_eff: U(1)-COVARIANT weight+1 [NOT invariant], conj-odd, not cyclic-invariant as written, cubic ⇒ independent of Z_chiral)
L3_UNITARY_CENTRALIZER                    = U(1)×U(2)  [SU(3): S(U(1)×U(2)) ≅ U(2)]  — EXACT
SU3_CARRIER_STRUCTURE                     = EXACT (C³ = fundamental of U(3)/SU(3); L_3 selects the line-stabilizer U(1)×U(2); NO Standard-Model meaning assigned)
PHASE_BRIDGE_READY_FOR_CODEX              = PARTIAL (kinematic geometry EXACT; genuine dynamical phase requires an added observable, frequency, and continuum-time justification — all UNRESOLVED)

FROZEN_PAPERS_MODIFIED = NO
KERNEL_PHYSICS_MODIFIED = NO
REPOSITORY_MODIFIED = NO
NOTHING_EXECUTED = TRUE
```
