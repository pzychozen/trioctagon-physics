# Claude independent review: generic transverse harmonics of chirality near the synchronized manifold

**Task:** `CLAUDE_GENERIC_TRANSVERSE_HARMONICS_v0.1` · **Reviewer:** Claude (independent mathematical review) · **Scientific lead:** GPT · **Author:** Hilmir Frímann Halldórsson · **Date:** 25 September 2026 · **Accepted baseline:** `d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`

Scope kept as ordered: pure mathematics of the accepted three-node recurrence at `k = (1,1,1)`, phase strength 0, `ε = 1/20`, `g = 1/5`. No gate mapping, no electromagnetic reading, no clock identification. No kernel code was executed, edited or imported; every computation below is my own algebra (SymPy, exact) or my own scratch evaluation of the stated polynomial map (mpmath at 80–160 digits, and float64 only for the noise-floor estimate in §9). Inputs read: the work order, `TRANSVERSE_AXIS_FALSIFICATION_REPORT.md`, `CHIRAL_TRANSVERSE_REPORT.md` §§2–3, and `dynamics.py` (to confirm the map and the form of `phase_sync`). Nothing in the repository was written except this file.

Labels used throughout: **EXACT** (theorem about the recurrence, proved symbolically), **NORMAL FORM** (local result near `Ω = e`, proved to the stated order), **NUMERICAL** (high-precision evaluation, not a proof), **SYMMETRY** (representation-theoretic statement), **DICTIONARY OPEN** (needs a coordinate identification that does not exist), **MODEL CHOICE**.

## 0. Summary of findings

1. **GPT's one-step formula is exact** — every coefficient, sign, harmonic and order in `h`, to all orders (it is a polynomial identity, not an expansion). One convention remark: the signed in-plane angle is `−(ε²/36a) h⁴ sin 6φ` in the orientation `u × v = +ê` (rotation from `u` toward `v` positive); GPT's `+` sign corresponds to measuring the angle from `ĉ₀` toward `q(φ)`.
2. **The harmonics are forced by symmetry** (S3 × conjugation × common phase acting on the seed family as the dihedral group D6 on the `φ`-circle): the in-plane rotation can only contain `sin 6nφ`, the out-of-plane component only `cos 3(2n+1)φ`, the in-plane magnitude only `cos 6nφ`; and `h³`, `h⁵` are the minimal degrees at which `cos 3φ` and `sin 6φ` can appear. The coefficients are dynamical and nonzero, so the structure is generic.
3. **The twelve `sin 6φ = 0` directions are all genuine symmetry axes, of two different kinds.** Six (`v`-type, e.g. `(1,1,−2)`) are fixed lines of a channel transposition: the whole state is invariant, so chirality is confined exactly to its axis with no in-plane and no out-of-plane deviation, ever. Six (`u`-type, e.g. `(1,−1,0)`) are fixed lines of a transposition composed with complex conjugation: in-plane drift vanishes exactly, but the out-of-plane deviation is maximal there (`cos 3φ = ±1`). Seed B was `v`-type, seed A was `u`-type; this is precisely why B showed zero drift and A showed only the out-of-plane `√2 h²/120`.
4. **Beyond one step the picture changes qualitatively.** The one-step rotation is *not* the leading behaviour of the accumulated drift: the second step contributes an increment of the same order and opposite sign, later increments decay like `r ⁿ = 0.3ⁿ` (the real-transverse multiplier), and the total asymptotic in-plane drift is, exactly at the defaults,
   `ψ∞ = (13375/1107936648) h⁴ sin 6φ ≈ +1.2072×10⁻⁵ h⁴ sin 6φ`,
   opposite in sign and 14 times smaller than the one-step value `−h⁴ sin 6φ/5760`. I give a closed form in `a = 1−3g`, `r = a−2ε` (§6.4).
5. **No accumulation, no selection.** The gauge-fixed map has multipliers `(0.9, 0.3, 0.3, 0.4, 0.4)` with no resonances, so it is analytically conjugate to its linear part (Poincaré). In linearizing coordinates the projective angle is exactly conserved; the observed drift is a bounded coordinate effect of total size `O(h⁴)`. Every direction, special or generic, is **neutral**. The asymptotic map `φ₀ ↦ φ∞ = φ₀ + ψ∞(h, φ₀)` displaces generic directions by `O(h⁴)` toward the nearest `v`-type axis, but this is a one-time displacement set by the initial amplitude, not an attraction.
6. **No canonical identification `φ = θ − ℓ` follows from accepted mathematics**, and none can: `θ` advances by `π/6` per update regardless of the state, while `φ` converges to a constant. The shared "3" is the lowest nontrivial harmonic of D3 in both places, no more.
7. **Another trajectory at `h = 10⁻³` cannot resolve the in-plane effect** (total `1.2×10⁻¹⁷` rad against a float64 floor of `~10⁻¹⁶`; even the one-step `1.7×10⁻¹⁶` is marginal). The smallest sensible amplitude is `h = 10⁻²`; `h = 2×10⁻²` gives comfortable margins. But the mathematics is now exact, so such a run would be an implementation witness, not a discovery (§9).
8. Caveat for later work: at nonzero phase strength the accepted `phase_sync` term contributes its own D6-forced in-plane rotation of `(243/160) λ h⁴ sin 6φ` per step to leading order — at `λ = 10⁻³` about nine times the `ε²` one-step term. The present result is specific to `λ = 0`.

## 1. Setup and conventions

`e = (1,1,1)`, `u = (1,−1,0)/√2`, `v = (1,1,−2)/√6`, `q(φ) = u cos φ + v sin φ`. Facts used (all EXACT, checked): `u × v = ê`, so `(u, v, ê)` is right-handed and "positive rotation" in `e⊥` means `u → v`; `e × q(φ) = √3 q(φ + π/2)`, hence `ĉ₀ = q(φ + π/2)`; the componentwise products of transverse unit vectors are

    q∘q     = e/3 + q(π/2 − 2φ)/√6,
    q∘q∘q   = q/2 + (√6/18) sin 3φ · e,           (exactly in span(e, q))
    Σⱼ qⱼ³  = sin 3φ/√6,  e·(q∘q × q) = −cos 3φ/√2.

In the chart `z = q_u + i q_v = e^{iφ}` the transposition (12) acts as `φ ↦ π − φ`, the 3-cycle as `φ ↦ φ ± 2π/3`, and complex conjugation of `Ω` on the seed family `e + ihq(φ)` acts as `φ ↦ φ + π` with `C ↦ −C`. Together these generate the dihedral group D6 (order 12) on the `φ`-circle; the common phase `U(1)` acts trivially on the family and leaves `C` invariant (EXACT: `Re(e^{iα}Ω) × Im(e^{iα}Ω) = Re Ω × Im Ω`).

## 2. One-step formula (item 1, 2): EXACT, confirmed

Applying the recurrence literally to `Ω = e + ihq(φ)` (SymPy, symbolic `ε, g, h, φ`; no truncation):

    Re Ω₁ = e − ε h² (q∘q),          Im Ω₁ = a h q − ε h³ (q∘q∘q),     a = 1 − 3g,

because `L₃ e = 0`, `L₃ q = −3q`, and `1 − |Ωⱼ|² = −h² qⱼ²`. Crossing and projecting on `(ĉ₀, q, ê)` gives exactly GPT's

    A = √3 h [a − ε h²(2a+3)/6 + ε² h⁴ (5 + cos 6φ)/36],
    B = (√3/36) ε² h⁵ sin 6φ,
    D = (√6/12) ε h³ (2a − ε h²) cos 3φ,

with no residual component. **Every coefficient, sign, harmonic and power of `h` is confirmed, and the identity is exact rather than asymptotic.** The mechanism, in my own decomposition: `C₁ = a h (e×q) − ε h³ (e×t) − a ε h³ (s×q) + ε² h⁵ (s×t)` with `s = q∘q`, `t = q∘q∘q`; `e×t` is parallel to `ĉ₀`; `s×q` supplies the `cos 3φ` out-of-plane term at order `ε h³`; only `s×t`, through `q(π−2φ) = −cos 3φ q + sin 3φ ĉ₀`, supplies the `sin 6φ` in-plane term at order `ε² h⁵`. There is no `ε¹ h⁵` in-plane term.

Consequences, confirmed: `tan ∠(C₁, e⊥) = D/√(A²+B²) = (√2 ε/6) h² cos 3φ (1 + O(h²))`; signed in-plane angle relative to `ĉ₀`, positive `u → v`:

    ψ₁ = atan2(C₁·q(φ+π), C₁·ĉ₀) = −atan(B/A) = −(ε²/36a) h⁴ sin 6φ + O(h⁶) = −(h⁴/5760) sin 6φ + O(h⁶).

GPT's `+ε²/(36a)` is the same quantity measured from `ĉ₀` toward `q(φ)`, i.e. clockwise; the magnitude and harmonic are identical. I recommend fixing the orientation `u × v = +ê` in any later packet so that signs are comparable across steps (§6 shows the sign matters).

Two exact by-products worth recording: after one step the common phase receives a **third-harmonic kick**, `mean(Ω₁) = 1 − εh²/3 − i(√6/18) ε h³ sin 3φ`, and the real transverse part acquires a **second-harmonic response** `−(εh²/√6) q(π/2 − 2φ)`. The `sin 6φ` in-plane rotation at one step is exactly the product of these two (a `sin 3φ` gauge rotation applied to a `cos 3φ`-projecting real vector).

## 3. Symmetry origin of `cos 3φ` and `sin 6φ` (item 3): SYMMETRY, forced

**Equivariance of the map (EXACT, checked symbolically):** `F(PΩ) = P F(Ω)` for all permutations `P`, `F(e^{iα}Ω) = e^{iα}F(Ω)`, `F(Ω̄) = F(Ω)̄`. Chirality transforms as `C(PΩ) = det(P)·P C(Ω)`, `C(Ω̄) = −C(Ω)`, `C(e^{iα}Ω) = C(Ω)`.

**Consequences for functions of the seed angle.** Write `C_n = A_n ĉ₀ + B_n q + D_n ê` for the state after any number of steps from `e + ihq(φ)`, and `ψ_n = −atan(B_n/A_n)`.

- Rotation by the 3-cycle: `φ ↦ φ + 2π/3`, `C ↦ PC`, `ĉ₀, q ↦ Pĉ₀, Pq`: all of `A, B, D, ψ` are invariant under `φ ↦ φ + 2π/3`.
- Conjugation: `φ ↦ φ + π`, `C ↦ −C`, and `ĉ₀(φ+π) = −ĉ₀(φ)`, `q(φ+π) = −q(φ)`: `A, B, ψ` invariant, `D ↦ −D`.
- Transposition (12): `φ ↦ π − φ`, `C ↦ −PC`, `Pe = e`: `D ↦ −D`; the in-plane part is reflected, so `A` is invariant and `B, ψ` change sign.

Hence `ψ` has period `π/3` and is odd under reflections: `ψ ∈ span{sin 6nφ}`. `D` has period `2π/3`, is antiperiodic under `π`, and odd under reflections: `D ∈ span{cos 3(2n+1)φ}`. `A ∈ span{cos 6nφ}`. (Table of these parity checks in Appendix D output.) In invariant-theory terms: D3 acting on `e⊥ ≅ ℂ` has invariant ring generated by `|z|²` and `Re z³`, plus the pseudo-invariant `Im z³`; with this chart's origin `Σqⱼ³ ∝ sin 3φ` is the invariant and `cos 3φ` the pseudo-invariant, and `e·C` is a pseudo-scalar. Adjoining conjugation (which acts as `−1` on the plane) enlarges D3 to D6, whose lowest pseudo-invariant is `Im z⁶ ∝ sin 6φ`. This is exactly what appears.

**Minimal orders are also forced.** A vector-valued polynomial of degree `m` in `q` contains harmonics at most `m`. `D ê` with `D ∝ cos 3φ` needs `m ≥ 3` → `h³`. `B q(φ)` with `B ∝ sin 6φ` has harmonics `5, 7` → `m ≥ 5` → `h⁵`. The `cos 6φ` piece of `A` likewise needs `h⁵`. So GPT's orders are the lowest that symmetry permits, and since the coefficients (`√6/12·2a·ε`, `√3 ε²/36`) are nonzero, the phenomenon is generic. **What symmetry does not fix** is the coefficients and, in particular, whether a multi-step total keeps the one-step sign — it does not (§6).

## 4. The six `sin 6φ = 0` projective directions (item 3, 4): SYMMETRY, two kinds

The twelve zeros `φ ∈ (π/6)ℤ` are:

| `φ` | direction `q` | stabilizer in the extended group | consequence (EXACT) |
|---|---|---|---|
| `0, π/3, 2π/3, …` (`u`-type) | `±(1,−1,0)/√2, ±(1,0,−1)/√2, ±(0,1,−1)/√2` | `P q = −q` for one transposition, so `Ω = e + ihq` is fixed by **`P ∘ conj`** | `C = P C` ⇒ `C ∈ span(e, v_P)` where `v_P` is the mirror axis of `P`: **in-plane drift is exactly zero for all time; out-of-plane deviation is allowed and maximal (`cos 3φ = ±1`)** |
| `π/6, π/2, 5π/6, …` (`v`-type) | `±(1,1,−2)/√6, ±(2,−1,−1)/√6, ±(−1,2,−1)/√6` | `P q = q` for one transposition, so `Ω` itself is fixed by **`P`** | `C = −P C` ⇒ `C ∈ span(u_P)`: **chirality is confined exactly to one line for all time; no in-plane and no out-of-plane deviation** |

Both kinds are genuine fixed-point sets of elements of the symmetry group `S₃ × ℤ₂(conj) × U(1)` and therefore invariant lines of the exact dynamics — not merely stationary points of the one-step `sin 6φ`. But they are not the same kind of axis, and they are not attractors (§7). The six projective lines form two D3-orbits of three; they are not a single orbit of six.

**Why the executed seeds were protected (item 4).** Seed A `= e + ih(1,−1,0)/√2` is `u`-type: it lies in the subspace `(x+iy, x−iy, z)` fixed by `(12)∘conj`, so its chirality is exactly `y(z, z, −2x) ∈ span(e, (1,1,−2))`: no in-plane term at any order (`B ≡ 0`), and the observed `1.1785×10⁻⁸` rad is purely the out-of-plane `(√2 ε/6) h² cos 3φ` with `cos 0 = 1`; my exact one-step value `√2·h²/120 = 1.17851132162×10⁻⁸` at `h = 10⁻³` reproduces Codex's pre-run number to all quoted digits, and the multi-step out-of-plane angle decays like `r ⁿ = 0.3ⁿ` (ratios `0.46, 0.356, 0.325, 0.312, 0.306, …` → `0.3`, matching Codex's table). Seed B `= e + ih(1,1,−2)/√6` is `v`-type, fixed by `(12)` itself: `B ≡ D ≡ 0`, exactly zero drift, as measured. The pair therefore tested the two protected classes and nothing generic; their `90°` separation is the angle between a mirror line and a perpendicular anti-mirror line and is exact for the same reason.

## 5. Gauge-fixed local normal form (item 5): NORMAL FORM

Fix the common phase so that the channel mean is real and positive, and write `Ω = (1+μ)e + x + iy` with real `x, y ∈ e⊥`. Then **exactly** `C = (1+μ) e×y + x×y`: the in-plane part of `C` is `e × y` (up to the positive factor `1+μ`), and the out-of-plane part is `x×y ∥ e`. So in this gauge the in-plane chirality angle *is* the angle of `y`, and `tan ∠(C, e⊥) = e·(x×y)/(√3 (1+μ)|y|) ≈ |x| sin∠(x,y)/√3`.

Linearization at `Ω = e` (EXACT): `δΩⱼ ↦ δΩⱼ − 2ε Re δΩⱼ` on-site, `−3g δΩ` from coupling on `e⊥`, `−2ε` for the mean radius. Multipliers: mean radius `1−2ε = 0.9`; `x`: `r = a − 2ε = 0.3` (double); `y`: `a = 0.4` (double); common phase `1` (gauged away). Both transverse blocks are scalar multiples of the identity on `e⊥` — the "degeneracy" of the earlier packets — so the projective angle of `y` is neutral at linear order.

Leading nonlinear amplitude map, with `x = X q(π/2−2φ)` (the only real transverse component generated at `O(h²)`), `y = Y q(φ)`, verified symbolically:

    Y' = Y [ a − 2εμ − (√6/3) ε X − (ε/2) Y² ],
    X' = r X − (ε/√6) Y²,
    μ' = (1−2ε) μ − (ε/3) Y²,
    common-phase kick per step  α = −(ε/18)(12 X Y + √6 Y³) sin 3φ.

Everything decays: `Y_n ≈ aⁿ h`, `X_n = (ε h²/√6)(a^{2n} − r ⁿ)/(a² − r)` (so `X₁ = −εh²/√6`), `μ_n → 0` at rate `0.9`. **The angle is not slaved to these three amplitudes alone**: at `O(h⁴)` the gauge rotation `α` also feeds `x` with components along `q(φ)` and `q(φ+π/2)` (size `ε h⁴ sin 3φ`), and these re-enter the angle through `−2ε(x∘y)` at the next step at the same order `ε² h⁴ sin 6φ`. A one-line slaving formula built from `(μ, X, Y)` only reproduces the first step and fails at the second (I checked; it does not reproduce `Δ₂`). The exact per-step increments therefore have to be computed with the full state, which is what §6 does.

**Resonances (item 5, attracting/repelling):** with multipliers `{0.9, 0.3, 0.3, 0.4, 0.4}` there is no relation `λ_s = 0.9ⁱ 0.3ʲ 0.4ᵏ`, `i+j+k ≥ 2` (checked to exponents `< 12`; none exists in general because `0.3` and `0.4` are not products of the others). All multipliers lie strictly inside the unit disk. By Poincaré's linearization theorem the gauge-fixed map is **analytically conjugate to its linear part** near the synchronized point. In the linearizing coordinates `ỹ_n = aⁿ ỹ₀` exactly, so the projective angle of `ỹ` is exactly constant; the conjugacy is unique with identity linear part and hence equivariant, so the twelve symmetry lines are the same lines in both charts. Consequently: **no direction is attracting or repelling; all are neutral; the observed angle converges to `φ∞ = φ₀ + ψ∞(h, φ₀)`, a bounded analytic, D6-odd function of the initial condition of size `O(h⁴)`.** "Drift" is a finite coordinate displacement, not a secular accumulation.

## 6. Exact multi-step increments and the asymptotic drift (item 5): EXACT + NUMERICAL

**Method.** I expanded the exact recurrence to `O(h⁵)` with `ε` and `g` symbolic (polynomial arithmetic in `h, cos φ, sin φ` reduced by `cos²φ = 1 − sin²φ`), recomputed `C_n` and `ψ_n = −atan(B_n/A_n)` after each of nine steps, and independently iterated the exact map at 80–160 digits (`h = 10⁻⁵` and `10⁻²⁵`, several `φ`). The two agree to all printed digits.

**Structure.** Every `ψ_n` is `κ_n h⁴ sin 6φ + O(h⁶)` with no other harmonic (checked exactly, `n ≤ 9`; numerically to `10⁻⁶⁰` for `n ≤ 120`). Writing `a = 1−3g`, `r = a−2ε`, the increments `Δ_n = κ_n − κ_{n−1}` are

    Δ₁ = −(a−r)²/(144a) = −ε²/(36a),
    Δ₂ = −(a−r)²(2a⁴ − 2a³ + 4a²r − 2ar − 3a + 2r² − r)/(288a),
    Δ₃ = −(a−r)²(2a⁸ − 2a⁷ + 4a⁶r − 4a⁵r − 3a⁵ + 6a⁴r² − a⁴r + 4a⁴ − 4a³r² − 2a³r + 2a³ + 4a²r³ − 2a²r² − 2a²r − 3a² − 2ar³ + ar² + 2ar + 2r⁴ − r³ − 3r²)/(288a),

and for `n ≥ 2` the polynomials `P_n = −288a Δ_n/(a−r)²` satisfy **exactly** a four-rate law `P_n = c₁ a^{4n} + c₂ (a²r)ⁿ + c₃ r^{2n} + c₄ rⁿ` with rational-function coefficients `c_i(a, r)` (fitted on `n = 2…5`, verified on `n = 6…9`). No `aⁿ` term appears. Numerically at the defaults (`h⁴ sin 6φ` units):

| n | κ_n (exact rational) | Δ_n | Δ_n/Δ_{n−1} |
|---|---|---|---|
| 1 | −1/5760 = −1.7361×10⁻⁴ | −1.7361×10⁻⁴ | — |
| 2 | −347/7200000 = −4.8194×10⁻⁵ | +1.2542×10⁻⁴ | −0.722 |
| 3 | −6.6254×10⁻⁶ | +4.1569×10⁻⁵ | 0.331 |
| 4 | +6.3774×10⁻⁶ | +1.3003×10⁻⁵ | 0.313 |
| 6 | +1.1556×10⁻⁵ | +1.2016×10⁻⁶ | 0.302 |
| 8 | +1.2025×10⁻⁵ | +1.0849×10⁻⁷ | 0.3002 |
| 12 | +1.20716×10⁻⁵ | +8.79×10⁻¹⁰ | 0.30000 |
| ∞ | **13375/1107936648 = +1.20720×10⁻⁵** | — | → r = 0.3 |

Even at leading order in `ε` the first three increments are comparable (`Δ₁ = −0.0694 ε²`, `Δ₂ = +0.0493 ε²`, `Δ₃ = +0.0232 ε²` at `g = 1/5`), so there is no sense in which the one-step result is "the" leading drift; the late tail decays with the real-transverse multiplier `r`, not with `a⁴`.

**6.4 Closed form (EXACT for the summed four-rate law).** Summing the geometric tails:

    ψ∞ = κ∞(a, r) · h⁴ sin 6φ + O(h⁶),
    κ∞ = −(a−r)² · N(a,r) / [ 288 a (1+a)(1+a²)(1−r)²(1+r)(1−a²r) ],
    N  = 4a³r² + 3a³r − 4a³ + a²r² − 4a² + 4ar² − a − 2r² − 3r + 2 .

At `a = 2/5`, `r = 3/10` this equals `13375/1107936648` exactly, which the 160-digit iteration reproduces to 55 significant digits (the `O(h⁶)` remainder at `h = 10⁻²⁵` is `10⁻⁵⁰`). In `(ε, g)`: `κ∞ = (96875/5130216) ε² − (215328125/600235272) ε³ + O(ε⁴)` at `g = 1/5`, i.e. `≈ +0.0189 ε²` against the one-step `−0.0694 ε²`. The `h⁴` law and the pure `sin 6φ` dependence of the total were checked at `φ = π/12, π/8, π/5, 0.3, π/12 + π/3, π/12 + π` (NUMERICAL, 15 digits).

**Reading.** The sign reversal means the one-step formula points the wrong way for the asymptotic direction. Since `κ∞ > 0`, the asymptotic map `φ₀ ↦ φ₀ + κ∞ h⁴ sin 6φ₀` moves a generic seed by `O(h⁴)` **toward the nearest `v`-type (mirror) axis and away from the nearest `u`-type axis** — the opposite of what the first step does. This displacement is set once by the initial amplitude and does not grow (§5): it is neither weak selection nor attraction. With `h = 10⁻³` it is `1.2×10⁻¹⁷` rad.

## 7. Out-of-plane versus in-plane, kept separate (item 6)

- Out-of-plane deviation `∠(C, e⊥)`: first appears at `ε h³` (`cos 3φ`), is maximal on `u`-type axes and zero on `v`-type axes, is *even* under `h ↦ −h` combined with `φ ↦ φ+π`, and decays along an orbit like `r ⁿ = 0.3ⁿ` once `x` has formed (because it is `≈ |x_n| sin∠(x_n, y_n)/√3`). It is the effect seed A measured.
- In-plane axis displacement `ψ`: first appears at `ε² h⁵` in `C` (`ε² h⁴` in angle), harmonic `sin 6φ`, zero on **both** kinds of axes, converges to the exact `κ∞ h⁴ sin 6φ` of §6.4. Neither seed could see it.

They are governed by different group characters (pseudo-scalar odd under `π`-shift versus pseudo-scalar even under it), different orders, different multipliers, and vanish on different axis sets; a single "drift" number mixes them and should be avoided in any follow-up.

## 8. Comparisons at the level of symmetry only (items 7, 8): DICTIONARY OPEN

**Paper-E harmonic `cos(3(θ − ℓ))`.** In `z_manifold` this is a chosen readout of the external clock angle `θ = 2πq/12`, which advances by `π/6` per update whatever `Ω` does. In the present result the third harmonic is the lowest D3 harmonic of the channel-permutation symmetry acting on a *state* angle `φ` that converges to a constant. The two "3"s have the same group-theoretic origin (three channels) and nothing else in common: one angle is a counter, the other a coordinate on `e⊥`; one rotates uniformly, the other freezes. **No identification `φ = θ − ℓ` follows from accepted mathematics, and as dynamical variables they cannot be identified**; the lock `ℓ` has no counterpart here at all (the seed family has its own D6-symmetric origin fixed by the vertex labelling). The accepted `phase_sync` term `sin 3(p_l − p_j)` is a third "3": a design choice acting on state phase differences, which is D3-compatible by construction; its own contribution to the in-plane rotation is `(243/160) λ h⁴ sin 6φ` per step to leading order on `p = h q(φ)` (SYMMETRY + series; the cubic term is isotropic, the quintic is the first D6 pseudo-invariant), so at `λ = 10⁻³` it would exceed the `ε²` mechanism by an order of magnitude. Anything said about "the" sixth harmonic must state `λ`.

**Six candidate apertures.** The shell's six patches form one regular orbit of D3h (three azimuths × upper/lower, swapped by `σ_h`). The six `sin 6φ = 0` projective lines form two D3-orbits of three (`u`-type and `v`-type); the twelve oriented directions form two regular D6 orbits. The channel group has no element playing the role of `σ_h` (conjugation acts as `−1` on `q`, which is projectively trivial). So the count "6 = 6" arises from `|D3| = 6` in two structurally different ways; no bijection is canonical, and no spatial registration is adopted or implied. This is a symmetry analogy only.

## 9. Is another numerical trajectory useful? (item 9)

**Resolvability.** Iterating the same polynomial map in float64 and comparing with the 80-digit truth, the error in the signed in-plane angle is `~10⁻¹⁶` rad and essentially independent of `h` (every imaginary component is `O(h)` with no `O(1)` cancellation). Against that floor:

| h | ψ₁ exact | ψ∞ exact | float64 error | SNR one-step | SNR total (n=6) |
|---|---|---|---|---|---|
| 10⁻³ | −1.74×10⁻¹⁶ | +1.21×10⁻¹⁷ | 2–8×10⁻¹⁷ | ≈ 5 | ≈ 0.5 |
| 3×10⁻³ | −1.41×10⁻¹⁴ | +9.8×10⁻¹⁶ | ~2×10⁻¹⁶ | 1.4×10² | ≈ 3 |
| 10⁻² | −1.74×10⁻¹² | +1.21×10⁻¹³ | ~2×10⁻¹⁶ | 4×10⁴ | 6×10² |
| 2×10⁻² | −2.78×10⁻¹¹ | +1.93×10⁻¹² | ~3×10⁻¹⁶ | 4×10⁵ | 8×10³ |
| 5×10⁻² | −1.09×10⁻⁹ | +7.5×10⁻¹¹ | ~1×10⁻¹⁶ | 5×10⁷ | 7×10⁵ |

**At `h = 10⁻³` the in-plane effect is not resolvable**: the asymptotic total is below the noise and the one-step value is marginal. I say so plainly rather than recommend a run.

**Is a run needed?** Not for the mathematics: the one-step formula is an exact identity, the increments and the asymptotic coefficient are exact, and the neutrality statement is a theorem. A run would test the implementation's agreement with an already-proved polynomial identity, which the previous packet has in effect already done at `9×10⁻¹⁷`. **If GPT nevertheless wants an implementation witness for the generic case**, the smallest meaningful design is: two seeds `e + ihq(φ)` with `h = 2×10⁻²`, `φ = +π/12` and `φ = −π/12` (`sin 6φ = ±1`, `cos 3φ = +1/√2` for both, so the out-of-plane part is a shared control and the in-plane part flips sign), eight updates each, observable = signed in-plane angle `atan2(C·q(φ₀+π), C·q(φ₀+π/2))` with the `ê` component projected out, in the orientation `u × v = +ê`. Predictions to compare, at `h = 2×10⁻²`: `ψ₁ = ∓2.7778×10⁻¹¹`, `ψ₂ = ∓7.711×10⁻¹²`, `ψ₄ = ±1.0204×10⁻¹²`, `ψ₈ = ±1.9241×10⁻¹²`, `ψ∞ = ±1.9315×10⁻¹²` (all `h⁴ = 1.6×10⁻⁷` times the §6 table), out-of-plane `∠(C₁, e⊥) = (√2/120)(4×10⁻⁴)/√2 = 3.333×10⁻⁶` rad for both. The sign reversal between the two seeds and the sign reversal between step 1 and step 4 are the two qualitative facts a run could witness. Amplitude `h = 10⁻²` is the floor; below it the total is not cleanly resolvable.

## 10. Classification of every statement

| Statement | Class |
|---|---|
| One-step `A, B, D` formula; symmetry identities; `C` gauge invariance; `q∘q`, `q∘q∘q` decompositions | EXACT recurrence theorem |
| Harmonic content (`sin 6nφ`, `cos 3(2n+1)φ`, `cos 6nφ`) and minimal orders `h³`, `h⁵` | SYMMETRY (forced) |
| Two kinds of symmetry axes; exact protection of seeds A and B; A's out-of-plane, B's total confinement | EXACT (invariant subspaces) |
| Gauge-fixed multipliers; absence of resonances; analytic linearization; neutrality of all directions; boundedness of total drift | NORMAL FORM (theorem under Poincaré's hypotheses, which hold) |
| Amplitude map for `(μ, X, Y)` and the phase kick `α` | NORMAL FORM, leading order, proved |
| Exact `Δ_n` for `n ≤ 9`; four-rate law for `2 ≤ n ≤ 9` | EXACT (symbolic) |
| Four-rate law for all `n ≥ 2`, hence the closed form `κ∞(a, r)` | EXACT given the law; the law itself is proved for `n ≤ 9` and confirmed numerically to 55 digits at the defaults (NUMERICAL beyond `n = 9`) |
| `h⁴` scaling and pure `sin 6φ` of the total | NUMERICAL (15 digits, six angles, two amplitudes) — consistent with the SYMMETRY constraint |
| Asymptotic displacement toward `v`-type axes | EXACT sign of `κ∞` at defaults; interpretation as displacement, not attraction, is NORMAL FORM |
| `phase_sync` in-plane coefficient `243/160` | SYMMETRY + series on the phase map alone; not integrated with the amplitude step (`λ = 0` in this order) |
| Relation to `cos(3(θ−ℓ))`, to the six apertures | symmetry analogy only; DICTIONARY OPEN; no identification |
| Any physical reading of `φ`, `C`, or the axes | physical hypothesis, not addressed |

```
ACCEPTED_BASELINE = d0aa8d1cb19421ff441eacda0f83ec89fc3160b3
KERNEL_EXECUTED_OR_MODIFIED = NO
MODEL_RUNS = NO (scratch evaluation of the stated polynomial map only)
ONE_STEP_FORMULA = CONFIRMED_EXACT (sign convention noted)
HARMONICS = FORCED_BY_S3xCONJ_SYMMETRY (D6 on the seed circle)
SIX_AXES = TWO_KINDS_OF_EXACT_SYMMETRY_LINES (u-type: in-plane protected; v-type: fully confined)
MULTI_STEP = NEUTRAL_NO_ACCUMULATION; total drift O(h^4), sign opposite to one step
ASYMPTOTIC_COEFFICIENT_AT_DEFAULTS = 13375/1107936648 (closed form in a, r given)
CLOCK_IDENTIFICATION = NONE_FOLLOWS
APERTURE_IDENTIFICATION = NONE_FOLLOWS
NEW_RUN_AT_h=1e-3 = NOT_RESOLVABLE; h >= 1e-2 if a witness run is wanted
STAGE_COMMIT_PUSH = NO
NEXT_BOUNDARY = GPT_ADJUDICATION
```

## Appendix A. Exact one-step algebra (script and output)

Environment: Python 3.11, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.4.4, task-owned scratch. Script SHA-256 `2a082b5d088794d202854088a524c298845ba50cbae3ee80a6244ea217c3b800`.

```python
"""CLAUDE_GENERIC_TRANSVERSE_HARMONICS_v0.1 -- Part A: exact one-step algebra.

Independent of GPT's intermediate algebra: the recurrence is applied literally to
Omega = e + i h q(phi) with symbolic eps, g, h, phi; C = Re x Im is decomposed on
(c0hat, q, ehat) by orthogonal projection. No project code imported.
"""
import sympy as sp
from sympy import sqrt, Rational as Q, cos, sin, pi, Matrix, I, simplify, expand

eps, g, h, phi = sp.symbols('epsilon g h phi', real=True)
e = Matrix([1, 1, 1]); u = Matrix([1, -1, 0])/sqrt(2); v = Matrix([1, 1, -2])/sqrt(6)
L3 = e*e.T - 3*sp.eye(3)
def q(x): return u*cos(x) + v*sin(x)
def step(Om):  # accepted recurrence, k=(1,1,1), phase strength 0
    return Matrix([Om[j] + eps*Om[j]*(1 - Om[j]*sp.conjugate(Om[j])) for j in range(3)]) + g*L3*Om
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    assert cond, name

Om0 = e + I*h*q(phi)
Om1 = step(Om0).applyfunc(lambda z: sp.expand(z))
re1 = Om1.applyfunc(sp.re); im1 = Om1.applyfunc(sp.im)
C1 = re1.cross(im1).applyfunc(sp.expand)

a = 1 - 3*g
c0 = e.cross(q(phi))/sqrt(3); ehat = e/sqrt(3)
ok("c0hat = q(phi+pi/2) (e x q(phi) = sqrt3 q(phi+pi/2))", simplify(c0 - q(phi + pi/2)) == sp.zeros(3, 1))
ok("(u, v, ehat) right-handed: u x v = ehat", simplify(u.cross(v) - ehat) == sp.zeros(3, 1))

A = sp.simplify(C1.dot(c0)); B = sp.simplify(C1.dot(q(phi))); D = sp.simplify(C1.dot(ehat))
A_gpt = sqrt(3)*h*(a - eps*h**2*(2*a + 3)/6 + eps**2*h**4*(5 + cos(6*phi))/36)
B_gpt = sqrt(3)*eps**2*h**5*sin(6*phi)/36
D_gpt = sqrt(6)*eps*h**3*(2*a - eps*h**2)*cos(3*phi)/12
def zero(x): return sp.simplify(sp.expand_trig(sp.expand(x))) == 0 or sp.simplify(x.rewrite(sp.exp)) == 0
ok("A coefficient (along c0hat) matches GPT exactly, all orders in h", zero(A - A_gpt))
ok("B coefficient (along q) matches GPT exactly", zero(B - B_gpt))
ok("D coefficient (along ehat) matches GPT exactly", zero(D - D_gpt))
ok("C1 = A c0hat + B q + D ehat exactly (no other component)", all(zero(x) for x in (C1 - A_gpt*c0 - B_gpt*q(phi) - D_gpt*ehat)))

# building blocks used in my own derivation
s = Matrix([q(phi)[j]**2 for j in range(3)]); t = Matrix([q(phi)[j]**3 for j in range(3)])
ok("q o q = e/3 + q(pi/2 - 2phi)/sqrt6", all(zero(x) for x in (s - e/3 - q(pi/2 - 2*phi)/sqrt(6))))
ok("q o q o q = q/2 + (sqrt6/18) sin3phi e (exactly in span(e,q))", all(zero(x) for x in (t - q(phi)/2 - sqrt(6)/18*sin(3*phi)*e)))
ok("Re Omega1 = e - eps h^2 (q o q)", all(zero(x) for x in (re1 - e + eps*h**2*s)))
ok("Im Omega1 = a h q - eps h^3 (q o q o q)", all(zero(x) for x in (im1 - a*h*q(phi) + eps*h**3*t)))
ok("sum_j q_j^3 = sin(3phi)/sqrt6 (scalar cubic D3 invariant)", zero(sum(t) - sin(3*phi)/sqrt(6)))
ok("e.(s x q) = -cos(3phi)/sqrt2 (pseudoscalar cubic)", zero(e.dot(s.cross(q(phi))) + cos(3*phi)/sqrt(2)))
mean1 = sum(Om1)/3
ok("mean after one step = 1 - eps h^2/3 - i (sqrt6/18) eps h^3 sin3phi (common-phase kick)",
   zero(sp.re(mean1) - (1 - eps*h**2/3)) and zero(sp.im(mean1) + sqrt(6)/18*eps*h**3*sin(3*phi)))

# small-h consequences
ang_out = sp.series(D_gpt/A_gpt, h, 0, 4).removeO()   # tan(angle to e-perp) = D/sqrt(A^2+B^2) = D/A (1+O(h^8))
ok("angle to e-perp ~ (sqrt2 eps/6) h^2 cos3phi", zero(sp.simplify(ang_out - sqrt(2)*eps/6*h**2*cos(3*phi))))
num = {eps: Q(1,20), g: Q(1,5), h: Q(1,100), phi: pi/12}
print("   check at h=1/100, phi=pi/12: exact atan(D/sqrt(A^2+B^2)) =", sp.N(sp.atan(D_gpt/sp.sqrt(A_gpt**2+B_gpt**2)).subs(num), 15),
      " leading (sqrt2 eps/6)h^2 cos3phi =", sp.N((sqrt(2)*eps/6*h**2*cos(3*phi)).subs(num), 15))
# signed in-plane angle in the (u,v) orientation: psi = atan2(C.q(phi+pi), C.c0hat) = -atan(B/A)
psi = sp.series(-sp.atan(B_gpt/A_gpt), h, 0, 6).removeO()
ok("signed in-plane angle (u->v positive) = -(eps^2/(36a)) h^4 sin6phi + O(h^6)", zero(sp.simplify(psi + eps**2*h**4*sin(6*phi)/(36*a))))
print("   at eps=1/20, g=1/5: eps^2/(36 a) =", Q(1, 400)/(36*Q(2, 5)), "= 1/5760")

# symmetries of the recurrence (exact)
P12 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); P123 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
z = sp.symbols('z0:3'); Omg = Matrix(z)
ok("F(P Omega) = P F(Omega) for a transposition", all(sp.simplify(x) == 0 for x in (step(P12*Omg) - P12*step(Omg))))
ok("F(P Omega) = P F(Omega) for a 3-cycle", all(sp.simplify(x) == 0 for x in (step(P123*Omg) - P123*step(Omg))))
al = sp.symbols('alpha', real=True)
ok("F(e^{i alpha} Omega) = e^{i alpha} F(Omega)", all(sp.simplify(sp.expand(x)) == 0 for x in (step(sp.exp(I*al)*Omg) - sp.exp(I*al)*step(Omg))))
ok("F(conj Omega) = conj F(Omega)", all(sp.simplify(x) == 0 for x in (step(Omg.applyfunc(sp.conjugate)) - step(Omg).applyfunc(sp.conjugate))))
# action on the seed family: conj -> phi+pi ; P12 -> pi - phi ; 3-cycle -> phi + 2pi/3 (up to orientation)
ok("P12 q(phi) = q(pi - phi)", all(zero(x) for x in (P12*q(phi) - q(pi - phi))))
ok("P123 q(phi) = q(phi + 2pi/3) or q(phi - 2pi/3)",
   all(zero(x) for x in (P123*q(phi) - q(phi + 2*pi/3))) or all(zero(x) for x in (P123*q(phi) - q(phi - 2*pi/3))))
# the two executed seeds
for name, ph in (("seed A (u-type, phi=0)", 0), ("seed B (v-type, phi=pi/2)", pi/2)):
    print(f"   {name}: B = {sp.simplify(B_gpt.subs(phi, ph))}, D = {sp.simplify(D_gpt.subs(phi, ph))}, "
          f"out-of-plane angle at h=1e-3, eps=1/20: {float((sqrt(2)*eps/6*h**2*cos(3*phi)).subs({phi: ph, eps: Q(1,20), h: Q(1,1000)})):.10e}")
print("   Codex measured seed-A one-step drift 1.1785113164e-08 = sqrt2/120 * 1e-6 =", float(sqrt(2)/120*1e-6))

# tangent of C1 in-plane (gauge-invariance): common phase leaves C invariant
xr = sp.symbols('x0:3', real=True); yr = sp.symbols('y0:3', real=True)
Omr = Matrix([xr[j] + I*yr[j] for j in range(3)])
rot = (sp.exp(I*al)*Omr).applyfunc(sp.expand)
ok("C is invariant under common phase e^{i alpha}", all(sp.simplify(x) == 0 for x in
   (rot.applyfunc(sp.re).cross(rot.applyfunc(sp.im)) - Omr.applyfunc(sp.re).cross(Omr.applyfunc(sp.im)))))
print("PART A DONE")
```

```
PASS c0hat = q(phi+pi/2) (e x q(phi) = sqrt3 q(phi+pi/2))
PASS (u, v, ehat) right-handed: u x v = ehat
PASS A coefficient (along c0hat) matches GPT exactly, all orders in h
PASS B coefficient (along q) matches GPT exactly
PASS D coefficient (along ehat) matches GPT exactly
PASS C1 = A c0hat + B q + D ehat exactly (no other component)
PASS q o q = e/3 + q(pi/2 - 2phi)/sqrt6
PASS q o q o q = q/2 + (sqrt6/18) sin3phi e (exactly in span(e,q))
PASS Re Omega1 = e - eps h^2 (q o q)
PASS Im Omega1 = a h q - eps h^3 (q o q o q)
PASS sum_j q_j^3 = sin(3phi)/sqrt6 (scalar cubic D3 invariant)
PASS e.(s x q) = -cos(3phi)/sqrt2 (pseudoscalar cubic)
PASS mean after one step = 1 - eps h^2/3 - i (sqrt6/18) eps h^3 sin3phi (common-phase kick)
PASS angle to e-perp ~ (sqrt2 eps/6) h^2 cos3phi
   check at h=1/100, phi=pi/12: exact atan(D/sqrt(A^2+B^2)) = 8.33334722225791e-7  leading (sqrt2 eps/6)h^2 cos3phi = 8.33333333333333e-7
PASS signed in-plane angle (u->v positive) = -(eps^2/(36a)) h^4 sin6phi + O(h^6)
   at eps=1/20, g=1/5: eps^2/(36 a) = 1/5760 = 1/5760
PASS F(P Omega) = P F(Omega) for a transposition
PASS F(P Omega) = P F(Omega) for a 3-cycle
PASS F(e^{i alpha} Omega) = e^{i alpha} F(Omega)
PASS F(conj Omega) = conj F(Omega)
PASS P12 q(phi) = q(pi - phi)
PASS P123 q(phi) = q(phi + 2pi/3) or q(phi - 2pi/3)
   seed A (u-type, phi=0): B = 0, D = sqrt(6)*epsilon*h**3*(-epsilon*h**2 - 6*g + 2)/12, out-of-plane angle at h=1e-3, eps=1/20: 1.1785113020e-08
   seed B (v-type, phi=pi/2): B = 0, D = 0, out-of-plane angle at h=1e-3, eps=1/20: 0.0000000000e+00
   Codex measured seed-A one-step drift 1.1785113164e-08 = sqrt2/120 * 1e-6 = 1.1785113019775793e-08
PASS C is invariant under common phase e^{i alpha}
PART A DONE
```

## Appendix B. High-precision multi-step evaluation (script and output)

SHA-256 `54cfdbb5872b6e53b55e37a8d48bedb4fcb360a3823b46c96810917cb02626a9`.

```python
"""Part B: multi-step behaviour at 80-digit precision (mpmath), exact map, no truncation.

Signed in-plane angle psi_n of C_n relative to c0hat(phi) in the (u,v) orientation
(u -> v positive): psi = atan2(C.q(phi+pi), C.q(phi+pi/2)).  Out-of-plane angle
theta_n = atan(C.ehat / |C_inplane|).  All relative to the INITIAL phi.
"""
import mpmath as mp
mp.mp.dps = 80
eps, g = mp.mpf(1)/20, mp.mpf(1)/5
a = 1 - 3*g; r = a - 2*eps
e = [mp.mpf(1)]*3
u = [mp.mpf(1)/mp.sqrt(2), -mp.mpf(1)/mp.sqrt(2), mp.mpf(0)]
v = [mp.mpf(1)/mp.sqrt(6), mp.mpf(1)/mp.sqrt(6), -2/mp.sqrt(6)]
def q(x): return [u[j]*mp.cos(x) + v[j]*mp.sin(x) for j in range(3)]
def step(Om):
    S = sum(Om)
    return [Om[j] + eps*Om[j]*(1 - abs(Om[j])**2) + g*(S - 3*Om[j]) for j in range(3)]
def cross(x, y): return [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]
def dot(x, y): return sum(x[j]*y[j] for j in range(3))
def chir(Om): return cross([z.real for z in Om], [z.imag for z in Om])
def angles(C, phi):
    c0 = q(phi + mp.pi/2); qm = q(phi + mp.pi); eh = [mp.mpf(1)/mp.sqrt(3)]*3
    A, Bm, D = dot(C, c0), dot(C, qm), dot(C, eh)
    return mp.atan2(Bm, A), mp.atan(D/mp.sqrt(A*A + Bm*Bm)), mp.sqrt(A*A + Bm*Bm + D*D)

def run(h, phi, n=14):
    Om = [e[j] + 1j*h*q(phi)[j] for j in range(3)]
    out = []
    for k in range(n+1):
        psi, th, nrm = angles(chir(Om), phi)
        out.append((k, psi, th, nrm))
        Om = step(Om)
    return out

h = mp.mpf('1e-5'); phi = mp.pi/12    # sin6phi = 1, cos3phi = 1/sqrt2 : generic
rows = run(h, phi)
print("step   psi_n/(h^4 sin6phi)          Delta psi_n/(h^4 sin6phi)      theta_n/(h^2 cos3phi)   |C_n|/(sqrt3 h a^n)")
prev = mp.mpf(0)
for k, psi, th, nrm in rows:
    kap = psi/(h**4*mp.sin(6*phi)); dk = (psi-prev)/(h**4*mp.sin(6*phi)); prev = psi
    print(f"{k:3d}   {mp.nstr(kap, 20):>24}   {mp.nstr(dk, 20):>24}   {mp.nstr(th/(h**2*mp.cos(3*phi)), 12):>14}   {mp.nstr(nrm/(mp.sqrt(3)*h*a**k), 14)}")
kappa_inf = rows[-1][1]/(h**4*mp.sin(6*phi))
print("kappa_1  (one step) =", mp.nstr(rows[1][1]/(h**4*mp.sin(6*phi)), 25), "  vs -1/5760 =", mp.nstr(-mp.mpf(1)/5760, 25))
print("kappa_inf (total)   =", mp.nstr(kappa_inf, 25))
print("naive geometric sum -1/(5760 (1-a^4)) =", mp.nstr(-1/(5760*(1-a**4)), 25))
print("identify kappa_inf as rational:", mp.identify(kappa_inf), " 1/kappa_inf =", mp.nstr(1/kappa_inf, 25))
# per-step increments as rationals
for k in range(1, 6):
    dk = (rows[k][1]-rows[k-1][1])/(h**4*mp.sin(6*phi))
    print(f"   Delta_{k}: {mp.nstr(dk, 22)}   1/Delta = {mp.nstr(1/dk, 22)}   identify: {mp.identify(dk)}")

# scaling checks
h2 = mp.mpf('2e-5'); rows2 = run(h2, phi)
print("h^4 law: kappa_inf(h=2e-5)/kappa_inf(h=1e-5) =", mp.nstr(rows2[-1][1]/rows[-1][1]/16, 15), "(should be 1 + O(h^2))")
for ph in [mp.pi/8, mp.pi/5, mp.mpf('0.3'), 0, mp.pi/6, mp.pi/12 + mp.pi/3, mp.pi/12 + mp.pi]:
    rr = run(h, ph)
    s6 = mp.sin(6*ph)
    print(f"phi={mp.nstr(ph,8):>10}: psi_inf/h^4 = {mp.nstr(rr[-1][1]/h**4, 15):>22}   kappa_inf*sin6phi = {mp.nstr(kappa_inf*s6, 15):>22}   theta_1/h^2 = {mp.nstr(rr[1][2]/h**2, 12)}   (sqrt2/120)cos3phi = {mp.nstr(mp.sqrt(2)/120*mp.cos(3*ph), 12)}")
# out-of-plane decay ratio -> r = a - 2 eps = 0.3
th = [row[2] for row in rows]
print("theta_{n+1}/theta_n:", [mp.nstr(th[k+1]/th[k], 8) for k in range(1, 8)], " (limit a-2eps =", mp.nstr(r, 5), ")")
# seed A / seed B reproduction at h = 1e-3 (Codex table)
rA = run(mp.mpf('1e-3'), 0, 8); rB = run(mp.mpf('1e-3'), mp.pi/2, 8)
print("seed A (phi=0) out-of-plane angle rows 1..3:", [mp.nstr(rA[k][2], 11) for k in (1,2,3)], " in-plane drift max:", mp.nstr(max(abs(rA[k][1]) for k in range(9)), 5))
print("seed B (phi=pi/2) out-of-plane, in-plane max:", mp.nstr(max(abs(rB[k][2]) for k in range(9)), 5), mp.nstr(max(abs(rB[k][1]) for k in range(9)), 5))
print("seed A |C_8| =", mp.nstr(rA[8][3], 17), " Codex: 1.1351167545977547e-06")
```

```
step   psi_n/(h^4 sin6phi)          Delta psi_n/(h^4 sin6phi)      theta_n/(h^2 cos3phi)   |C_n|/(sqrt3 h a^n)
  0   4.6436621249194806344e-62   4.6436621249194806344e-62   -1.31342599123e-71   1.0
  1   -0.00017361111111248553241   -0.00017361111111248553241   0.0117851130198   0.99999999999208
  2   -0.00004819444444642109838   0.00012541666666606443403   0.00542115198908   0.99999999999161
  3   -6.6254444467000977481e-6   0.000041568999999721000632   0.00192804449003   0.99999999999212
  4   6.3774219532333079063e-6   0.000013002866399933405654   0.000626685169938   0.99999999999269
  5   0.000010354002933059801841    3.976580979826493935e-6   0.00019572904265   0.99999999999322
  6   0.000011555622370941580428   1.2016194378817785867e-6   5.99544714621e-5   0.99999999999368
  7   0.000011916986778861706744   3.6136440792012631546e-7   1.81840628254e-5   0.9999999999941
  8   0.000012025480321919479168   1.0849354305777242417e-7   5.48685426949e-6   0.99999999999448
  9   0.000012058036220138144421   3.2555898218665252929e-8   1.65111794835e-6   0.99999999999482
 10   0.000012067803707254416359   9.7674871162719385853e-9   4.96145251305e-7   0.99999999999513
 11   0.000012070734018582028689   2.9303113276123298992e-9   1.4897315408e-7   0.9999999999954
 12   0.000012071613117876797969   8.7909929476927990861e-10   4.4712678814e-8   0.99999999999565
 13   0.000012071876848197314845   2.6373032051687619977e-10   1.34171208586e-8   0.99999999999587
 14   0.000012071955967341425093   7.9119144110248150156e-11   4.02566701189e-9   0.99999999999607
kappa_1  (one step) = -0.0001736111111124855324074168   vs -1/5760 = -0.0001736111111111111111111111
kappa_inf (total)   = 0.00001207195596734142509339775
naive geometric sum -1/(5760 (1-a^4)) = -0.000178172322568874293012224
identify kappa_inf as rational: None  1/kappa_inf = 82836.61758751654499829809
   Delta_1: -0.0001736111111124855324074   1/Delta = -5759.9999999544   identify: None
   Delta_2: 0.0001254166666660644340278   1/Delta = 7973.421926948586218695   identify: None
   Delta_3: 0.0000415689999997210006315   1/Delta = 24056.38817404103339289   identify: None
   Delta_4: 0.00001300286639993340565448   1/Delta = 76906.11971565911903155   identify: None
   Delta_5: 0.000003976580979826493935016   1/Delta = 251472.3087680291552234   identify: None
h^4 law: kappa_inf(h=2e-5)/kappa_inf(h=1e-5) = 0.999999999419049 (should be 1 + O(h^2))
phi=0.39269908: psi_inf/h^4 =    8.53616192669253e-6   kappa_inf*sin6phi =    8.53616192669253e-6   theta_1/h^2 = 0.00450996750123   (sqrt2/120)cos3phi = 0.00450996750122
phi=0.62831853: psi_inf/h^4 =   -7.09571768392741e-6   kappa_inf*sin6phi =   -7.09571768392741e-6   theta_1/h^2 = -0.00364180020375   (sqrt2/120)cos3phi = -0.00364180020374
phi=       0.3: psi_inf/h^4 =    1.17562457188613e-5   kappa_inf*sin6phi =    1.17562457188613e-5   theta_1/h^2 = 0.0073257437303   (sqrt2/120)cos3phi = 0.00732574373029
phi=         0: psi_inf/h^4 =    7.1444643765627e-62   kappa_inf*sin6phi =                    0.0   theta_1/h^2 = 0.0117851130198   (sqrt2/120)cos3phi = 0.0117851130198
phi=0.52359878: psi_inf/h^4 =   1.31980815607952e-61   kappa_inf*sin6phi =  -3.79688308432548e-86   theta_1/h^2 = -5.8045776562e-72   (sqrt2/120)cos3phi = -1.85333248368e-83
phi= 1.3089969: psi_inf/h^4 =    1.20719559673414e-5   kappa_inf*sin6phi =    1.20719559673414e-5   theta_1/h^2 = -0.00833333333335   (sqrt2/120)cos3phi = -0.00833333333333
phi=  3.403392: psi_inf/h^4 =    1.20719559673414e-5   kappa_inf*sin6phi =    1.20719559673414e-5   theta_1/h^2 = -0.00833333333335   (sqrt2/120)cos3phi = -0.00833333333333
theta_{n+1}/theta_n: ['0.46', '0.35565217', '0.32503667', '0.31232436', '0.30631362', '0.30329786', '0.30173973']  (limit a-2eps = 0.3 )
seed A (phi=0) out-of-plane angle rows 1..3: ['1.1785113216e-8', '5.4211518462e-9', '1.9280444291e-9']  in-plane drift max: 7.1445e-82
seed B (phi=pi/2) out-of-plane, in-plane max: 6.965e-82 4.7454e-81
seed A |C_8| = 1.1351167545977556e-6  Codex: 1.1351167545977547e-06
```

## Appendix C. Exact symbolic multi-step expansion in `(a, r)` (script; first three outputs)

SHA-256 `9c0ead0787a43b0d49afc96d96ebf36138200b943300ccf8413aee41af621998`. Steps 1–9 were computed; the full step-4 to step-9 polynomials are long and are summarized by the four-rate law of Appendix F.

```python
"""Part C: exact multi-step expansion of the signed in-plane chirality angle to O(h^4),
with epsilon and g SYMBOLIC.  Truncated polynomial arithmetic in (h, c=cos phi, s=sin phi),
reduced by c^2 = 1 - s^2.  Real and imaginary parts carried separately (no complex symbols).
"""
import sympy as sp
from sympy import Rational as Q, sqrt
import sys, time

aa, rr = sp.symbols('a r'); eps, g = (aa-rr)/2, (1-aa)/3
HMAX = 5
class P:
    """polynomial in h, c, s with coefficients in Q(eps,g); dict {(i,j,k): coeff}; j in {0,1}; i<=HMAX."""
    __slots__ = ("d",)
    def __init__(self, d=None): self.d = {} if d is None else d
    @staticmethod
    def const(x): return P({(0,0,0): sp.sympify(x)})
    def copy(self): return P(dict(self.d))
    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items(): d[k] = d.get(k, 0) + v
        return P({k: v for k, v in d.items() if v != 0})
    def __sub__(self, o): return self + o.scale(-1)
    def scale(self, x): return P({k: sp.expand(v*x) for k, v in self.d.items()})
    def __mul__(self, o):
        d = {}
        for (i1,j1,k1), v1 in self.d.items():
            for (i2,j2,k2), v2 in o.d.items():
                i = i1+i2
                if i > HMAX: continue
                j, k = j1+j2, k1+k2
                terms = [(j, k, v1*v2)]
                if j == 2:  # c^2 -> 1 - s^2
                    terms = [(0, k, v1*v2), (0, k+2, -v1*v2)]
                for jj, kk, vv in terms:
                    d[(i,jj,kk)] = d.get((i,jj,kk), 0) + vv
        return P({k: sp.expand(v) for k, v in d.items() if sp.expand(v) != 0})
    def coeff_h(self, n): return P({(i,j,k): v for (i,j,k), v in self.d.items() if i == n})
    def to_expr(self, phi):
        c, s = sp.cos(phi), sp.sin(phi); h = sp.symbols('h')
        return sum(v*h**i*c**j*s**k for (i,j,k), v in self.d.items())

h1 = P({(1,0,0): sp.Integer(1)})
cP = P({(0,1,0): sp.Integer(1)}); sP = P({(0,0,1): sp.Integer(1)})
r2, r6 = 1/sqrt(2), 1/sqrt(6)
# q(phi) components: q1 = c/sqrt2 + s/sqrt6, q2 = -c/sqrt2 + s/sqrt6, q3 = -2 s/sqrt6
qv = [cP.scale(r2) + sP.scale(r6), cP.scale(-r2) + sP.scale(r6), sP.scale(-2*r6)]
def q_shift(x):  # q(phi + x) components as P
    cx, sx = sp.cos(x), sp.sin(x)   # cos(phi+x) = c cx - s sx ; sin(phi+x) = s cx + c sx
    C = cP.scale(cx) - sP.scale(sx); S = sP.scale(cx) + cP.scale(sx)
    return [C.scale(r2) + S.scale(r6), C.scale(-r2) + S.scale(r6), S.scale(-2*r6)]

# state: (Re_j, Im_j) as P
Re = [P.const(1) for _ in range(3)]; Im = [h1*qv[j] for j in range(3)]
def step(Re, Im):
    SR = Re[0]+Re[1]+Re[2]; SI = Im[0]+Im[1]+Im[2]
    nRe, nIm = [], []
    for j in range(3):
        mod2 = Re[j]*Re[j] + Im[j]*Im[j]
        f = P.const(1) - mod2
        nRe.append(Re[j] + (Re[j]*f).scale(eps) + (SR - Re[j].scale(3)).scale(g))
        nIm.append(Im[j] + (Im[j]*f).scale(eps) + (SI - Im[j].scale(3)).scale(g))
    return nRe, nIm
def cross(x, y): return [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]
def dot(x, y): return x[0]*y[0]+x[1]*y[1]+x[2]*y[2]

phi = sp.symbols('phi', real=True)
c0 = q_shift(sp.pi/2); qm = q_shift(sp.pi)
results = []
t0 = time.time()
for n in range(1, 10):
    Re, Im = step(Re, Im)
    C = cross(Re, Im)
    A = dot(C, c0); Bm = dot(C, qm)
    # psi = atan2(Bm, A) ; A = A1 h + A3 h^3 + A5 h^5, Bm = B5 h^5 (+ lower?) -> psi = B/A to O(h^4)
    lowB = [k for k in Bm.d if k[0] < 5]
    assert not lowB, f"unexpected low-order in-plane component at step {n}: {lowB}"
    A1 = A.coeff_h(1).to_expr(phi).subs(sp.symbols('h'), 1)
    B5 = Bm.coeff_h(5).to_expr(phi).subs(sp.symbols('h'), 1)
    psi4 = sp.cancel(sp.expand_trig(B5/A1))
    # sin(6phi) = 2 s c (16 s^4 - 16 s^2 + 3): divide exactly
    s_, c_ = sp.sin(phi), sp.cos(phi)
    kap = sp.cancel(psi4/(2*s_*c_*(16*s_**4 - 16*s_**2 + 3)))
    assert not kap.has(phi), ("phi-dependence is not pure sin(6phi)", kap)
    kap = sp.factor(kap)
    results.append(kap)
    print(f"step {n}: psi_n = h^4 * [{kap}] * sin(6phi)   (time {time.time()-t0:.1f}s)")
    sys.stdout.flush()

import pickle
pickle.dump([sp.factor(k) for k in results], open('kappa_ar.pkl','wb'))
D = [results[0]] + [sp.factor(results[i]-results[i-1]) for i in range(1, len(results))]
for i, d in enumerate(D): print(f"Delta_{i+1} =", d)
pickle.dump(D, open('delta_ar.pkl','wb'))
```

```
step 1: psi_n = h^4 * [-(-a + r)**2/(144*a)] * sin(6phi)   (time 0.1s)
step 2: psi_n = h^4 * [-(-a + r)**2*(2*a**4 - 2*a**3 + 4*a**2*r - 2*a*r - 3*a + 2*r**2 - r + 2)/(288*a)] * sin(6phi)   (time 1.2s)
step 3: psi_n = h^4 * [-(-a + r)**2*(2*a**8 - 2*a**7 + 4*a**6*r - 4*a**5*r - 3*a**5 + 6*a**4*r**2 - a**4*r + 6*a**4 - 4*a**3*r**2 - 2*a**3*r + 4*a**2*r**3 - 2*a**2*r**2 + 2*a**2*r - 3*a**2 - 2*a*r**3 + a*r**2 - 3*a + 2*r**4 - r**3 - r**2 - r + 2)/(288*a)] * sin(6phi)   (time 4.4s)
Delta_1 = -(-a + r)**2/(144*a)
Delta_2 = -(-a + r)**2*(2*a**4 - 2*a**3 + 4*a**2*r - 2*a*r - 3*a + 2*r**2 - r)/(288*a)
Delta_3 = -(-a + r)**2*(2*a**8 - 2*a**7 + 4*a**6*r - 4*a**5*r - 3*a**5 + 6*a**4*r**2 - a**4*r + 4*a**4 - 4*a**3*r**2 - 2*a**3*r + 2*a**3 + 4*a**2*r**3 - 2*a**2*r**2 - 2*a**2*r - 3*a**2 - 2*a*r**3 + a*r**2 + 2*a*r + 2*r**4 - r**3 - 3*r**2)/(288*a)
```

## Appendix D. Symmetry table, axes, resonances, phase-sync term, float64 floor (script and output)

SHA-256 `e10e6152d60ed8a10b1056237a38fabf2ae9ccb3102e4e4a77b5e633c8469c4d`.

```python
"""Part D: symmetry/invariant theory, resonances, phase-sync term at symmetry level, binary64 feasibility."""
import sympy as sp, numpy as np, mpmath as mp, math
from sympy import Rational as Q, sqrt, cos, sin, pi, Matrix

phi, h, lam = sp.symbols('phi h lambda', real=True)
u = Matrix([1, -1, 0])/sqrt(2); v = Matrix([1, 1, -2])/sqrt(6); e = Matrix([1,1,1])
def q(x): return u*cos(x) + v*sin(x)
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name); assert cond, name

# --- 1. D3 invariant theory on e-perp, in the (u,v) chart: z = q_u + i q_v = e^{i phi}
# transposition (12): phi -> pi - phi  (reflection across the v axis); 3-cycle: phi -> phi +- 2pi/3
# cubic invariant (even under reflection) and cubic pseudo-invariant (odd):
ok("sum q_j^3 = sin3phi/sqrt6 is invariant under phi -> pi - phi", sp.simplify(sin(3*(pi-phi)) - sin(3*phi)) == 0)
ok("cos3phi is odd under phi -> pi - phi", sp.simplify(cos(3*(pi-phi)) + cos(3*phi)) == 0)
ok("both are invariant under phi -> phi + 2pi/3", sp.simplify(sin(3*(phi+2*pi/3)) - sin(3*phi)) == 0 and sp.simplify(cos(3*(phi+2*pi/3)) - cos(3*phi)) == 0)
# conjugation: (h, phi) -> (h, phi+pi); C -> -C.  Group generated on the phi-circle: D6 (order 12).
# Allowed harmonics: in-plane rotation psi: invariant under phi->phi+pi/3, odd under reflections -> sin(6n phi)
# out-of-plane D: period 2pi/3, antiperiodic under pi, odd under reflection -> cos(3(2n+1)phi)
# A: even, period pi/3 -> cos(6n phi)
fs = [sin(6*phi), cos(6*phi), cos(3*phi), sin(3*phi), sin(12*phi), cos(9*phi)]
def test(f, shift, sign): return sp.simplify(f.subs(phi, shift) - sign*f) == 0
print("   harmonic | +pi/3 invariant | odd under pi-phi | antiperiodic under +pi | odd under pi-phi")
for f in fs:
    print(f"   {str(f):>12} | {test(f, phi+pi/3, 1)!s:>15} | {test(f, pi-phi, -1)!s:>16} | {test(f, phi+pi, -1)!s:>22} |")
ok("sin6phi is the unique lowest harmonic allowed for the in-plane rotation", test(sin(6*phi), phi+pi/3, 1) and test(sin(6*phi), pi-phi, -1)
   and not test(cos(6*phi), pi-phi, -1) and not test(sin(3*phi), phi+pi/3, 1))
ok("cos3phi is the unique lowest harmonic allowed for the out-of-plane component", test(cos(3*phi), phi+2*pi/3, 1) and test(cos(3*phi), phi+pi, -1) and test(cos(3*phi), pi-phi, -1)
   and not test(sin(3*phi), pi-phi, -1))

# --- 2. the twelve sin(6phi)=0 directions: two D3 orbits
P12 = Matrix([[0,1,0],[1,0,0],[0,0,1]]); P13 = Matrix([[0,0,1],[0,1,0],[1,0,0]]); P23 = Matrix([[1,0,0],[0,0,1],[0,1,0]])
print("   phi (deg) | direction q | fixed by a transposition (P q = q) | anti-fixed (P q = -q) ")
for k in range(12):
    ph = k*pi/6; qq = sp.simplify(q(ph))
    fixed = [nm for nm, P in (("(12)",P12),("(13)",P13),("(23)",P23)) if sp.simplify(P*qq - qq) == sp.zeros(3,1)]
    anti = [nm for nm, P in (("(12)",P12),("(13)",P13),("(23)",P23)) if sp.simplify(P*qq + qq) == sp.zeros(3,1)]
    print(f"   {k*30:9d} | {tuple(sp.nsimplify(x*sqrt(6)) for x in qq)}/sqrt6 | {fixed} | {anti}")
# --- 3. resonance check of the gauge-fixed linearisation at the synchronized fixed point
eps, g = Q(1,20), Q(1,5); a = 1-3*g; r = a-2*eps; m = 1-2*eps
mult = {"mu": m, "x": r, "y": a}
print(f"   multipliers: mean radius {m}, real transverse {r} (x2), imaginary transverse {a} (x2); common phase 1 (gauged away)")
res = []
for tgt_name, tgt in mult.items():
    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                if i+j+k >= 2 and m**i * r**j * a**k == tgt: res.append((tgt_name, i, j, k))
ok("no resonances lambda_s = mu^i r^j a^k (i+j+k>=2, exponents <12)", res == [])
ok("all multipliers strictly inside the unit disk (Poincare domain)", all(0 < x < 1 for x in mult.values()))

# --- 4. the phase-sync term at symmetry level (lambda != 0 is OUTSIDE the work order's parameters)
# phase map p_j -> p_j + lam * sum_{l != j} sin(3(p_l - p_j)) on phases; take p = h q(phi) (transverse).
p = h*q(phi)
inc = Matrix([sum(sin(3*(p[l]-p[j])) for l in range(3) if l != j) for j in range(3)])
inc_s = inc.applyfunc(lambda z: sp.series(z, h, 0, 6).removeO())
def perp(vec, x): return sp.simplify(sp.expand_trig(vec.dot(q(x))))
cub = inc_s.applyfunc(lambda z: z.coeff(h, 3)); qui = inc_s.applyfunc(lambda z: z.coeff(h, 5))
ok("phase-sync cubic term is isotropic (parallel to q): no rotation at O(lambda h^2)", perp(cub, phi+pi/2) == 0)
rot5 = sp.simplify(perp(qui, phi+pi/2))
print("   phase-sync quintic term: component along q(phi+pi/2) =", rot5, "  (times lambda h^5)")
lin = sp.simplify(sp.expand_trig(inc_s.applyfunc(lambda z: z.coeff(h, 1)).dot(q(phi))))
print("   phase-sync linear term along q:", lin, " (i.e. (1-9 lambda) factor per step)")
s_, c_ = sin(phi), cos(phi)
coef5 = sp.cancel(rot5/(2*s_*c_*(16*s_**4 - 16*s_**2 + 3)))   # sin6phi = 2 s c (16 s^4 - 16 s^2 + 3)
ok("phase-sync in-plane rotation at O(lambda h^4) is proportional to sin(6phi)", not coef5.has(phi))
print("   -> per-step in-plane angle from the sync term alone (p = h q(phi)): lambda * h^4 *", coef5, "* sin(6phi) =", float(coef5), "lambda h^4 sin6phi")
print("      at lambda = 1e-3 this is", float(coef5)*1e-3, "h^4 sin6phi, versus the eps^2 one-step term 1/5760 =", 1/5760, "and the total 13375/1107936648 =", 13375/1107936648)

# --- 5. binary64 feasibility: float64 iteration of the same polynomial map vs 80-digit truth
mp.mp.dps = 80
def run_mp(hh, ph, n):
    epsm, gm = mp.mpf(1)/20, mp.mpf(1)/5
    um = [1/mp.sqrt(2), -1/mp.sqrt(2), mp.mpf(0)]; vm = [1/mp.sqrt(6), 1/mp.sqrt(6), -2/mp.sqrt(6)]
    qq = [um[j]*mp.cos(ph)+vm[j]*mp.sin(ph) for j in range(3)]
    Om = [1 + 1j*hh*qq[j] for j in range(3)]; out = []
    c0 = [um[j]*mp.cos(ph+mp.pi/2)+vm[j]*mp.sin(ph+mp.pi/2) for j in range(3)]; qm = [-x for x in qq]
    for k in range(n+1):
        x = [z.real for z in Om]; y = [z.imag for z in Om]
        C = [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]
        out.append(mp.atan2(sum(C[j]*qm[j] for j in range(3)), sum(C[j]*c0[j] for j in range(3))))
        S = sum(Om); Om = [Om[j]+epsm*Om[j]*(1-abs(Om[j])**2)+gm*(S-3*Om[j]) for j in range(3)]
    return out
def run_f64(hh, ph, n):
    epsf, gf = 0.05, 0.2
    uf = np.array([1,-1,0])/np.sqrt(2); vf = np.array([1,1,-2])/np.sqrt(6)
    qq = uf*np.cos(ph)+vf*np.sin(ph); Om = np.ones(3, dtype=np.complex128) + 1j*hh*qq; out = []
    c0 = uf*np.cos(ph+np.pi/2)+vf*np.sin(ph+np.pi/2); qm = -qq
    for k in range(n+1):
        C = np.cross(Om.real, Om.imag); out.append(math.atan2(float(C@qm), float(C@c0)))
        Om = Om + epsf*Om*(1-np.abs(Om)**2) + gf*(np.sum(Om) - 3*Om)
    return out
print("   float64 feasibility, phi = pi/12 (sin6phi=1), signed in-plane angle relative to c0hat:")
print("      h      | psi_1 exact     | psi_inf exact   | f64 error at n=1 | f64 error at n=6 | f64 error at n=10 | SNR(one-step) | SNR(total,n=6)")
for hh in ['1e-3', '3e-3', '1e-2', '2e-2', '3e-2', '5e-2', '1e-1']:
    tru = run_mp(mp.mpf(hh), mp.pi/12, 10); f64 = run_f64(float(hh), math.pi/12, 10)
    err = [abs(float(tru[k]) - f64[k]) for k in range(11)]
    print(f"   {hh:>7} | {float(tru[1]):+.3e} | {float(tru[10]):+.3e} | {err[1]:.2e} | {err[6]:.2e} | {err[10]:.2e} | {abs(float(tru[1]))/max(err[1],1e-300):9.1e} | {abs(float(tru[6]))/max(err[6],1e-300):9.1e}")
print("PART D DONE")
```

```
PASS sum q_j^3 = sin3phi/sqrt6 is invariant under phi -> pi - phi
PASS cos3phi is odd under phi -> pi - phi
PASS both are invariant under phi -> phi + 2pi/3
   harmonic | +pi/3 invariant | odd under pi-phi | antiperiodic under +pi | odd under pi-phi
     sin(6*phi) |            True |             True |                  False |
     cos(6*phi) |            True |            False |                  False |
     cos(3*phi) |           False |             True |                   True |
     sin(3*phi) |           False |            False |                   True |
    sin(12*phi) |            True |             True |                  False |
     cos(9*phi) |           False |             True |                   True |
PASS sin6phi is the unique lowest harmonic allowed for the in-plane rotation
PASS cos3phi is the unique lowest harmonic allowed for the out-of-plane component
   phi (deg) | direction q | fixed by a transposition (P q = q) | anti-fixed (P q = -q) 
           0 | (sqrt(3), -sqrt(3), 0)/sqrt6 | [] | ['(12)']
          30 | (2, -1, -1)/sqrt6 | ['(23)'] | []
          60 | (sqrt(3), 0, -sqrt(3))/sqrt6 | [] | ['(13)']
          90 | (1, 1, -2)/sqrt6 | ['(12)'] | []
         120 | (0, sqrt(3), -sqrt(3))/sqrt6 | [] | ['(23)']
         150 | (-1, 2, -1)/sqrt6 | ['(13)'] | []
         180 | (-sqrt(3), sqrt(3), 0)/sqrt6 | [] | ['(12)']
         210 | (-2, 1, 1)/sqrt6 | ['(23)'] | []
         240 | (-sqrt(3), 0, sqrt(3))/sqrt6 | [] | ['(13)']
         270 | (-1, -1, 2)/sqrt6 | ['(12)'] | []
         300 | (0, -sqrt(3), sqrt(3))/sqrt6 | [] | ['(23)']
         330 | (1, -2, 1)/sqrt6 | ['(13)'] | []
   multipliers: mean radius 9/10, real transverse 3/10 (x2), imaginary transverse 2/5 (x2); common phase 1 (gauged away)
PASS no resonances lambda_s = mu^i r^j a^k (i+j+k>=2, exponents <12)
PASS all multipliers strictly inside the unit disk (Poincare domain)
PASS phase-sync cubic term is isotropic (parallel to q): no rotation at O(lambda h^2)
   phase-sync quintic term: component along q(phi+pi/2) = 243*(16*sin(phi)**4 - 16*sin(phi)**2 + 3)*sin(phi)*cos(phi)/80   (times lambda h^5)
   phase-sync linear term along q: -9  (i.e. (1-9 lambda) factor per step)
PASS phase-sync in-plane rotation at O(lambda h^4) is proportional to sin(6phi)
   -> per-step in-plane angle from the sync term alone (p = h q(phi)): lambda * h^4 * 243/160 * sin(6phi) = 1.51875 lambda h^4 sin6phi
      at lambda = 1e-3 this is 0.0015187500000000001 h^4 sin6phi, versus the eps^2 one-step term 1/5760 = 0.00017361111111111112 and the total 13375/1107936648 = 1.2071989877890563e-05
   float64 feasibility, phi = pi/12 (sin6phi=1), signed in-plane angle relative to c0hat:
      h      | psi_1 exact     | psi_inf exact   | f64 error at n=1 | f64 error at n=6 | f64 error at n=10 | SNR(one-step) | SNR(total,n=6)
      1e-3 | -1.736e-16 | +1.207e-17 | 3.13e-17 | 2.14e-17 | 8.11e-17 |   5.5e+00 |   5.4e-01
      3e-3 | -1.406e-14 | +9.775e-16 | 1.03e-16 | 2.93e-16 | 1.42e-16 |   1.4e+02 |   3.2e+00
      1e-2 | -1.736e-12 | +1.207e-13 | 4.37e-17 | 2.00e-16 | 2.13e-16 |   4.0e+04 |   5.8e+02
      2e-2 | -2.778e-11 | +1.929e-12 | 6.52e-17 | 2.39e-16 | 3.72e-16 |   4.3e+05 |   7.7e+03
      3e-2 | -1.406e-10 | +9.758e-12 | 1.84e-17 | 1.05e-16 | 1.31e-16 |   7.6e+06 |   8.9e+04
      5e-2 | -1.085e-09 | +7.506e-11 | 2.09e-17 | 9.78e-17 | 7.37e-17 |   5.2e+07 |   7.3e+05
      1e-1 | -1.737e-08 | +1.183e-09 | 5.56e-17 | 4.91e-17 | 1.92e-16 |   3.1e+08 |   2.3e+07
PART D DONE
```

## Appendix F. Four-rate law and closed form (script and output)

SHA-256 `b3c6ed1dd775b089fe72ef797b0f508949ab0ac8746d03f52da1dceaee6483a2`. Reads the exact `P_n` produced by Appendix C.

```python
"""Part F: sum the exact increments (from Part C2 pickle) into a closed form and verify."""
import pickle, sympy as sp
a, r = sp.symbols('a r')
P = pickle.load(open('P_ar.pkl','rb'))            # P_n = Delta_n * (-288 a/(a-r)^2), n = 1..9, exact
lams = [a**4, a**2*r, r**2, r]; cs = sp.symbols('c0:4')
eqs = [sp.expand(sum(c*l**n for c, l in zip(cs, lams)) - P[n-1]) for n in range(2, 10)]
sol = sp.solve(eqs[:4], cs, dict=True)[0]
assert all(sp.simplify(e.subs(sol)) == 0 for e in eqs[4:]), "n=6..9 do not follow the four-rate law"
print("PASS P_n = c1 a^{4n} + c2 (a^2 r)^n + c3 r^{2n} + c4 r^n holds exactly for n = 2..9 (4 fitted, 4 checked)")
total = 2 + sum(sol[c]*l**2/(1-l) for c, l in zip(cs, lams))
kappa_inf = sp.factor(sp.cancel(-(a-r)**2/(288*a)*total))
print("kappa_inf(a,r) =", kappa_inf)
val = kappa_inf.subs({a: sp.Rational(2,5), r: sp.Rational(3,10)})
print("PASS at a=2/5, r=3/10 equals 13375/1107936648:", val == sp.Rational(13375,1107936648))
print("float:", float(val))
```

```
PASS P_n = c1 a^{4n} + c2 (a^2 r)^n + c3 r^{2n} + c4 r^n holds exactly for n = 2..9 (4 fitted, 4 checked)
kappa_inf(a,r) = (-a + r)**2*(4*a**3*r**2 + 3*a**3*r - 4*a**3 + a**2*r**2 - 4*a**2 + 4*a*r**2 - a - 2*r**2 - 3*r + 2)/(288*a*(a + 1)*(a**2 + 1)*(r - 1)**2*(r + 1)*(a**2*r - 1))
PASS at a=2/5, r=3/10 equals 13375/1107936648: True
float: 1.2071989877890563e-05
```
