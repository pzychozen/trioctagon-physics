# TRIOCTAGON — Magnetism M2 — Claude derivation v0.1: nonlinear onset of `W` at the first flip of the unequal-`k` in-phase host

**Date:** 1 October 2026. **Author:** Claude (independent derivation, before exchange with Codex). **Lead:** GPT. **Basis:** M1 accepted core CE01–CE11 at SHA-256 `a14e5a10…8ef6` (unchanged; nothing in M1 is reopened). **Scope:** mathematics only; current `kernel_physics` model (`64ddea15…d50b4`), read-only; no implementation, no new dynamics, no X01, no ring, no physical identification. `W` is the geometry-attached axial observable of CE02, not a field.

**Artifacts (standalone, mpmath only, no repository module):** `m2_flip.py` (SHA-256 `43004da1…4d80e`, 60-digit working precision, 16/16 checks) with `m2_flip_results.json` (`2fe2f350…98fd8`); `m2_entrance_compare.py` (`6eb51474…1f3733`) with results (`6acfb990…34d0156`). Python 3.11.15, mpmath 1.3.0.

**Evidence tags:** `[E]` exact (algebraic identity or interval-certified); `[N+]` numerical with two independent validations; `[N]` numerical observation only; `[G]` documented gap.

---

## 0. Result in one paragraph

Fix `ε = 1/20`, `g = 1/5`, `k = (1, 1.2208964704604097, 6.35310346037241)` (exact decimal rationals). The positive in-phase host `u` is certified (Krawczyk) `[E]`. On the open set where all pre-sync components are nonzero, the map is `U(1)`-equivariant (common phase) and `H`-equivariant (conjugation); a smooth gauge slice `Im(u·Ω) = 0` reduces it to a five-dimensional map `F̂` whose linearisation at the host is `blockdiag(J_R, B(λ))`, and for this all-positive host **`B(λ) = (1 − 9λ)·VᵀM(u)V` exactly** `[E]`. Hence the imaginary pair is real for all `λ`, the first crossing of `−1` is at

```
λ_c = (1 + 1/m₁)/9 = 0.367476394604213536549375991601945577651…,   m₁ = largest eigenvalue of VᵀM(u)V = 0.43340935089637667…,
```

it is **simple** (other multiplier `−m₂/m₁ = −0.768631673…`; real block `0.6809, 0.0886, 0.0726`), and **transversal** with `dμ_crit/dλ = −9m₁ = −3.90068415806739…` `[E]`. The centre-manifold (flip) normal-form coefficient, computed from the full two-substep map in the quotient with the slaved amplitude correction retained, is

```
c = ⟨p, C(q,q,q)⟩/6 + ⟨p, B(q, (I − A)⁻¹B(q,q))⟩/2 = 0.235387030441… − 0.148862180720… = +0.0865248497217875…   [N+]
```

so the flip is **supercritical**: for `μ = λ − λ_c > 0` a locally attracting period-two cycle exists with `a² = σμ/c + O(μ²)`, `σ = 9m₁`. Direct iteration confirms the law (ratio measured/predicted `0.99818` at `μ = 10⁻⁴`, deviation `≈ 18μ`). On the branch **`W` detects the critical mode at first order**: `W = a·W_q + O(a³)` with `W_q = T(u × η_c) = (3.173587, 1.947347, 0)`, `|W_q| = 3.723414`, azimuth `31.5337°`, so `|W| = 25.0001·√μ·(1 + O(μ))`; `Γ = a·(−0.043391) + O(a³)`. By `H`-equivariance the bifurcating cycle is `H`-symmetric, hence a **full period-two orbit of the complex state** (accumulated common phase exactly zero) with **`W₂ = −W₁`, `Γ₂ = −Γ₁` exactly** `[E given the cycle]`; it is not a relative orbit and `W` is alternating, not stationary. The entrance endpoints `√3f₁`, `√3f₂` at `μ = 0.005, 0.02` land, numerically, on exactly this cycle (phase-invariant distance `10⁻³⁹`) `[N]`; no basin theorem is claimed. **Remaining gap `[G]`:** `c` is a validated high-precision number, not an interval-certified sign; the connection to the remote `λ = 0.5` orbit is not established (its azimuth `31.65°` is merely close to `31.53°`).

---

## 1. Model, parameters, host

Map `F_λ = S_λ ∘ 𝒜` on `ℂ³` (CE04–CE05): `𝒜(Ω)_i = Ω_i + εΩ_i(k_i − |Ω_i|²) + g(L₃Ω)_i`, `L₃ = eeᵀ − 3I`; `S_λ(Ω̃)_i = |Ω̃_i| e^{i(φ_i + λH_i)}`, `φ = Arg₀(Ω̃)`, `H_i = Σ_{j≠i} sin 3(φ_j − φ_i)`.

**Host `[E]`.** Newton at 60 digits from the brief's numbers gives `u = (1.554467816928818003448592547456798453948, 1.57342113186904311455547991587722827607, 2.085939972794636476507159514291052181445)`, residual `7·10⁻⁶²`. Krawczyk operator on the box `u ± 10⁻³⁰` (interval arithmetic at 60 digits, `Y = J(u)⁻¹`, `J = diag(ε(k_i − 3u_i²)) + gL₃`) maps the box strictly into itself with enclosure width `≈ 5·10⁻⁶⁰`: **there is exactly one solution of `εu∘(k − u²) + gL₃u = 0` in that box.** The all-positive sign pattern gives `K = 3L₃` in CE09.

---

## 2. Target 1 — removing the neutral phase direction

### 2.1 Symmetries used `[E]`

On `𝒟 = {Ω : 𝒜(Ω)_i ≠ 0 ∀i}` (open; contains a neighbourhood of `u`):
* **`U(1)`:** `F_λ(e^{iθ}Ω) = e^{iθ}F_λ(Ω)` — `𝒜` is real-linear in `Ω` and commutes with common phase; `S_λ` depends only on moduli and phase differences. Fails only through `Arg₀` at zero pre-sync components (CE05), which `𝒟` excludes.
* **`H`:** `F_λ(Ω̄) = conj F_λ(Ω)` — conjugation negates all phases, hence `H_i`, consistently. `u` is `H`-fixed.

### 2.2 Gauge slice and quotient map

Let `θ(Ψ) := arg(Σ_i u_iΨ_i)` (smooth where `u·Ψ ≠ 0`; `u` real). Define the **slice** `Σ = {Ω : Im(u·Ω) = 0, Re(u·Ω) > 0}` and coordinates `Ω = u + ξ + iη`, `ξ ∈ ℝ³`, `η ∈ u⊥`. With `V = [v₁ v₂]` an orthonormal basis of `u⊥` (`v₁ = (u₂, −u₁, 0)/‖·‖`, `v₂ = û × v₁`), `z = (ξ₁, ξ₂, ξ₃, η₁, η₂) ∈ ℝ⁵`, `η = Vz_{4:5}`. The quotient map is

```
F̂_λ(z) := coordinates of e^{−iθ(F_λ(Ω(z)))} F_λ(Ω(z))      (rotate the image back onto Σ).
```

**Domain:** `z` small enough that `Ω(z) ∈ 𝒟` and `u·F_λ(Ω(z)) ≠ 0` — a neighbourhood of `0` (at `u` both hold with margin). No global quotient through `Arg₀` zeros is claimed.

**Why observables are preserved `[E]`:** `|Ω_i|`, phase differences, `C = x × y`, `W = TC`, `Γ` are `U(1)`-invariant (`C(e^{iθ}Ω) = C(Ω)` since `(x,y) ↦` a rotation in each `(x_i, y_i)` plane leaves `x × y` invariant). Hence their values along `F̂`-orbits equal their values along `F`-orbits: `F̂ⁿ(z)` and `F_λⁿ(Ω(z))` differ by a common phase only. A `p`-cycle of `F̂` is a **relative** `p`-cycle of `F`; it is a genuine `p`-cycle iff the accumulated gauge angle `Θ_p = Σ θ(F(Ω_j))` vanishes mod `2π`.

### 2.3 Linearisation `[E]`

`u` is `H`-fixed, so `DF_λ(u)` commutes with `(ξ, η) ↦ (ξ, −η)` and is block-diagonal: `J_R` on `ξ` (CE09: `M(u) − 2ε diag(u_i²)`, `λ`-independent) and `J_I(λ) = D_u(I + 3λL₃)D_u⁻¹M(u)` on `η`. `J_I u = u` (neutral phase). In the splitting `ℝ³ = ℝu ⊕ u⊥`, `J_I = [[1, cᵀ],[0, B]]`, so the gauge removes exactly the unit multiplier and `DF̂(0) = blockdiag(J_R, B)`, `B = VᵀJ_IV`. Verified: finite-difference `DF̂(0)` equals this to `2·10⁻³¹`.

**Exact reduction.** `D_uL₃D_u⁻¹ = u(1/u)ᵀ − 3I`, and `Vᵀu = 0`, so

```
B(λ) = Vᵀ[(1 − 9λ)I + 3λ u(1/u)ᵀ] M(u) V = (1 − 9λ) VᵀM(u)V .
```

`VᵀM(u)V` is symmetric with eigenvalues `m₁ = 0.4334093508963766711598144 > m₂ = 0.333132154536164575374778` (so `p = q` for the reduced block). Consequences: the reduced imaginary multipliers `(1 − 9λ)m₁`, `(1 − 9λ)m₂` are **real for all `λ`**, both decrease linearly through `0` at `λ = 1/9`, and the first to reach `−1` is `m₁`'s at `λ_c = (1 + 1/m₁)/9`. Interval check (certified host box, 60 digits): `det(B(λ) + I)` changes sign on `[λ_c − 10⁻²⁵, λ_c + 10⁻²⁵]`. The real block never crosses (`λ`-independent, moduli `< 0.681`). **Equal-`k` contrast:** there `VᵀMV = (1 − 3g)I₂`, `m₁ = m₂`, giving CE09's double crossing at `7/18`; here `m₁ ≠ m₂` because `k` is unequal, and the crossing is simple with gap `|−1| − |−m₂/m₁| = 0.2314`.

**Eigenvectors and conventions.** Right eigenvector `q` (in `V`-coordinates, `‖q‖ = 1`): `q = (−0.0234992933106126, 0.9997238534785)`; left eigenvector `p = q` (symmetry), normalised `⟨p, q⟩ = 1`. In `ℝ³`: `η_c = Vq = (0.465351693591539, 0.504461868549057, −0.727300504916283)`, `η_c ⊥ u`, `‖η_c‖ = 1`. Embedded in `ℝ⁵`: `q₅ = (0,0,0,q)`, `p₅ = (0,0,0,p)`.

**Transversality `[E]`:** `μ_crit(λ) = (1 − 9λ)m₁`, so `dμ_crit/dλ = −9m₁ = −3.90068415806739004…` (direct numerical `⟨p, B′q⟩` agrees to all printed digits). Define `σ := 9m₁ > 0`, so `μ_crit = −(1 + σμ)` with `μ = λ − λ_c`.

---

## 3. Target 2 — leading nonlinear return law

### 3.1 Normal-form conventions

Write `F̂_λ(z) = Az + ½B(z,z) + ⅙C(z,z,z) + O(‖z‖⁴)` at `λ_c`, with `B`, `C` the symmetric multilinear forms (second and third Fréchet derivatives). Since `A` has the simple eigenvalue `−1` and no eigenvalue `1` in the quotient (`spec A = {0.0726, 0.0886, 0.6809, −0.7686, −1}`), the centre manifold is one-dimensional and tangent to `q₅`; the restricted map in the coordinate `a` (so that `z = a q₅ + ½a²w + O(a³)`) is

```
a ↦ −a + c a³ + O(a⁴),        c = ⟨p, C(q,q,q)⟩/6 + ⟨p, B(q, (I − A)⁻¹B(q,q))⟩/2        (Kuznetsov, flip of maps)
```

with `w = (I − A)⁻¹B(q,q)` the **slaved amplitude correction**. Including the parameter: `a ↦ −(1 + σμ)a + c a³ + O(a⁴, μa², μ²a)`; the second iterate is `a ↦ (1 + 2σμ)a − 2c a³ + …`, so a period-two cycle exists for `σμ/c > 0` with `a² = σμ/c + O(μ²)`, and it is locally stable iff `c > 0` (supercritical; coexists with the unstable fixed point for `μ > 0`).

### 3.2 Computation (full two-substep map, quotient coordinates)

Multilinear forms by central differences of `F̂` at 60 digits with `F̂(0) = 0`: `B(v,w) = [F̂(h(v+w)) + F̂(−h(v+w)) − F̂(h(v−w)) − F̂(−h(v−w))]/(4h²)`, `C(v,v,v) = [F̂(2hv) − 2F̂(hv) + 2F̂(−hv) − F̂(−2hv)]/(2h³)`, at `h = 10⁻¹⁰` and `10⁻¹²` (truncation `O(h²)`, roundoff `≲ 10⁻⁶⁰/h³`): the two step sizes agree to `2·10⁻²¹`.

```
B(q,q) = (−0.146803468889, −0.171397133268, −0.316290944864, 0, 0)        (ξ-block only: H-even, as symmetry requires)
w = (I − A)⁻¹B(q,q) = (−0.59487114104, −0.623294604481, −0.761784218696, 0, 0)
⟨p, C(q,q,q)⟩/6 = +0.235387030441397
⟨p, B(q,w)⟩/2   = −0.148862180719609
c = 0.086524849721787538473
```

The slaved term is not small (it removes 63 % of the cubic term); the phase-only Jacobian would give the wrong magnitude.

**Local theorem (stated with its evidence).** *Let `ε, g, k` be as above and `u` the certified host. Then `F_λ` restricted to the slice has, at `λ_c = (1 + 1/m₁)/9`, a simple multiplier `−1` crossing transversally with `σ = 9m₁ > 0` `[E]`. If `c > 0` (established numerically as `0.0865248497…` with error far below `10⁻¹²` `[N+]`), then for all sufficiently small `μ > 0` there is a unique period-two cycle of `F̂_{λ_c+μ}` near `0`, `z_± = ±a q₅ + ½a²w + O(a³)`, `a = √(σμ/c)(1 + O(μ))`, locally asymptotically stable in the quotient, and no cycle for `μ < 0`.*

### 3.3 Validation by direct iteration `[N+]`

Seed `u + 10⁻⁶ i η_c`, iterate `F_{λ_c+μ}` (40 digits), measure `a` as `⟨p, Vᵀ Im Ω̂⟩` on the converged cycle:

| `μ` | steps | `a` measured | `√(σμ/c)` | ratio | `|W|` measured | `|W_q|√(σμ/c)` | `F²(Ω) = Ω` residual |
|---|---|---|---|---|---|---|---|
| `10⁻⁴` | 600000 | 0.0670206 | 0.0671429 | 0.99818 | 0.249333 | 0.250001 | `1.6·10⁻⁴²` |
| `4·10⁻⁴` | 150000 | 0.133317 | 0.134286 | 0.99279 | 0.494719 | 0.500002 | `0` |
| `1.6·10⁻³` | 37500 | 0.261116 | 0.268572 | 0.97224 | 0.959437 | 1.000003 | `0` |
| `6.4·10⁻³` | 20000 | 0.484871 | 0.537143 | 0.90269 | 1.718319 | 2.000006 | `0` |

`1 − ratio ≈ 18μ`: the deviation is linear in `μ`, as the `O(μ²)` term of `a²` requires; the sign and magnitude of `c` are thereby confirmed independently of the centre-manifold formula. Below threshold (`μ = −10⁻³`) the seed decays to `|C| < 10⁻³⁹`: no cycle on the `μ < 0` side, consistent with supercriticality.

---

## 4. Target 3 — `W`, `Γ` and the actual complex state

### 4.1 Observable on the critical direction `[E]`

With `Ω = u + ξ + iη`, `C = (u + ξ) × η`. On the branch `ξ = O(a²)` and `η = aη_c + O(a³)`, so `C = a (u × η_c) + O(a³)`:

```
C_q = u × η_c = (−2.19662716001146, 2.10126092719872, 0.0519755510793086)
W_q = T C_q   = (3.17358673166479, 1.94734707082316, 0),   |W_q| = 3.7234142071011,   azimuth 31.53372757°
Γ_q = e·C_q   = −0.0433906817334317
```

`W` detects the critical mode at **first order** (`T(u × η_c) ≠ 0`; it would vanish only if `u × η_c ∥ e`). Leading laws on the branch: `W = ±a W_q + O(a³)`, `Γ = ±aΓ_q + O(a³)`, hence

```
|W| = |W_q| √(σ/c) · √μ · (1 + O(μ)) = 25.0001 √μ (1 + O(μ)),      |Γ|/|W| → |Γ_q|/|W_q| = 0.01165 .
```

(`25.0001` is the computed constant `3.7234142·6.714286…`; no exactness is claimed.) `W` is horizontal (`z`-component `0`) by CE02; `Γ` is the small polar companion.

### 4.2 Reversal, drift, period `[E given the cycle; checked numerically]`

`F̂` is `H`-equivariant and `q₅` is `H`-odd, so `H` maps the unique local cycle to itself and must swap its two points: `z₋ = Hz₊` (`ξ` equal, `η` opposite). In the full state, if `Ω₁ = e^{iα}Ω̂₁`, then `Ω₂ = F(Ω₁) = e^{i(2α + θ₁)} conj(Ω₁)` with `θ₁ = θ(F(Ω̂₁))`, and the gauge angle at the second step is `θ₂ = θ(F(conj Ω̂₁)) = −θ₁`. Therefore:

* **accumulated common phase over the cycle `Θ₂ = θ₁ + θ₂ = 0`**: the bifurcating cycle is a **full period-two orbit of the complex state**, not merely a relative one (checked: `‖F²(Ω) − Ω‖ ≤ 1.6·10⁻⁴²`; `H`-symmetry residual `‖F(Ω) − e^{iχ}conj Ω‖ ≤ 7·10⁻⁴¹`);
* the per-step common phase alternates `±θ₁` (`θ₁ = 0.0086958` at `μ = 10⁻⁴`, growing `∝ √μ`);
* **`W₂ = −W₁` and `Γ₂ = −Γ₁` exactly** (`C` is `U(1)`-invariant and `H`-odd; checked `‖W₁ + W₂‖ ≤ 6·10⁻⁴¹`): `W` **alternates in sign** with the two-cycle mean zero — not stationary, not drifting.

**What local stability guarantees.** In the quotient the cycle is attracting (centre-direction multiplier of `F̂²` is `1 − 2σμ + O(μ²)`; the other four are products of the stable multipliers). In the full state this means: any trajectory that enters the neighbourhood converges to **some common-phase rotation** of the cycle (the phase offset is a neutral constant of the limit, fixed by the initial data), and its `W`, `Γ`, moduli and phase differences converge to those of the cycle. It guarantees nothing about trajectories outside the neighbourhood and nothing about the remote `λ = 0.5` orbit.

---

## 5. Target 4 — entrance relevance without a basin claim

The accepted endpoints are `Ω₀ = √3 f₁` and `√3 f₂ = conj(√3 f₁)` (`Q = 3`, common phase `0` declared). CE08 gives their exact first step (`W⁺ = (−0.0412531, 0.0825137, 0)`, `Γ⁺ = −0.611341` for `f₁`; signs reversed for `f₂`). The local theorem then says: **if** the subsequent trajectory enters the neighbourhood of §3 at a `λ = λ_c + μ`, `μ > 0` small, it converges (modulo common phase) to the period-two orbit with `|W| ≈ 25.0√μ`, alternating sign, `Γ ≈ ∓0.0434a`. **Entry into that neighbourhood is not proved**; the endpoint is far from the host (phase differences `±120°`, gauged distance `O(1)`).

Numerical illustration `[N]` (30 000 steps, 30 digits; `μ` explicit, no perturbation added; conjugate endpoint run separately):

| `μ` | endpoint | `|W|` at steps 1 / 100 / 30000 | `Γ` final | two-step residual | distance to the host-seed cycle (phase-invariant) |
|---|---|---|---|---|---|
| 0.005 | `√3f₁` | 0.0923 / 1.5808 / 1.5656767 | +0.01712 | `6·10⁻³¹` | `9.8·10⁻⁴⁰` |
| 0.005 | `√3f₂` | same | −0.01712 | same | (mirror) |
| 0.02 | `√3f₁` | 0.0923 / 2.3725 / 2.3725062 | +0.02212 | `0` | `5.9·10⁻⁴⁰` |
| 0.05 | `√3f₁` | 0.0923 / 2.5220 / 2.5220429 | +0.01781 | `0` | not compared |

At `μ = 0.005` and `0.02` the entrance trajectories reach **the same period-two orbit as the host seed** (phase-invariant distance `≈ 10⁻³⁹`); at these `μ` the cycle is already outside the asymptotic regime (`a = 0.437` vs the leading law `0.475`), so the agreement is with the actual cycle, not with the leading law. The conjugate endpoint gives the mirror orbit (`Γ` sign reversed, same `|W|`). This is evidence for these three parameter values and this amplitude `Q = 3` only; it establishes no basin, no threshold over `Q` or branches, and no independence from initial amplitude. The `λ = 0.5` orbit (`|W| = 1.908`, azimuth `31.65°`) lies at `μ = 0.1325`; `|W|` is not monotone in `μ` between (`2.52` at `μ = 0.05`), and no continuation from the local branch to it has been performed.

---

## 6. Claims with evidence strength, and the documented gap

| # | Statement | Tag |
|---|---|---|
| 1 | Host `u` unique in `u ± 10⁻³⁰` (Krawczyk, exact decimal `k`) | `[E]` |
| 2 | `U(1)`/`H` equivariance on `𝒟`; gauge slice; `DF̂(0) = blockdiag(J_R, B)`; observables preserved | `[E]` |
| 3 | `B(λ) = (1 − 9λ)VᵀM(u)V`; multipliers real; `λ_c = (1 + 1/m₁)/9`; simple; `σ = 9m₁`; real block stable | `[E]` |
| 4 | `c = 0.0865248497218 > 0`, supercritical flip, `a² = σμ/c + O(μ²)` | `[N+]` (formula + amplitude law) |
| 5 | `W = aW_q + O(a³)`, `|W_q| = 3.7234`, azimuth `31.534°`, `|W| ≈ 25.0√μ`; `Γ_q = −0.04339` | `[E]` given 4 |
| 6 | Cycle is `H`-symmetric ⇒ full period two, `W₂ = −W₁`, `Γ₂ = −Γ₁`, alternating `±θ₁` common phase | `[E]` given 4 |
| 7 | Entrance endpoints at `μ ∈ {0.005, 0.02}` land on the same cycle | `[N]` |
| 8 | Relation to the `λ = 0.5` orbit | not established |
| G1 | Rigorous sign certificate for `c` (interval evaluation of the third derivatives of the two-substep map) | `[G]` |
| G2 | Entry of entrance trajectories into the local neighbourhood | `[G]` |

**Suggested attacks for Codex:** (a) re-derive `B(λ) = (1 − 9λ)VᵀMV` and `λ_c = (1 + 1/m₁)/9` independently (it is elementary; if wrong, everything in §2 is wrong); (b) recompute `c` by a different route (symbolic third derivatives, or a second-iterate Taylor expansion) and check the split `0.235387 / −0.148862`; (c) check that `B(q,q)` has no `η`-component and that `(I − A)⁻¹` is applied in the quotient, not in `ℝ⁶`; (d) test the `H`-symmetry argument for the cycle (uniqueness of the local cycle is what forces `z₋ = Hz₊`); (e) attempt an interval certificate for `c` to close G1; (f) try to break claim 7 with a different `Q` or a perturbed endpoint.

No implementation, X01 adoption, ring extension or physical identification follows from this result.
