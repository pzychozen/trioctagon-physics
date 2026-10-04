# TRIOCTAGON — Magnetism M3 — Claude independent review v0.2

**Date:** 4 October 2026. **Reviewer:** Claude. **Object:** Codex `M3_CERTIFIED_ENTRANCE_CAPTURE` — package `TRIOCTAGON_MAGNETISM_M3_ENTRANCE_CAPTURE_CODEX_v0.1.zip` (SHA-256 `dc3a6137…ff79bf`) and report `TRIOCTAGON_MAGNETISM_M3_CODEX_DERIVATION_v0.1.md` (`a59c914c…cad26f`); all 17 internal `SHA256SUMS` entries verified. These bytes are identical to the package I reviewed on 2 October (`TRIOCTAGON_MAGNETISM_M3_CLAUDE_REVIEW_v0.1.md`). **This v0.2 supersedes v0.1**, which accepted a logical step that does not hold (§1). M1 and M2 are used only as accepted premises. Codex's package is unchanged.

**Final disposition: `M3_ACCEPTED_WITH_CORRECTIONS`** — with the domain stated in §4. As supplied, the package does not prove capture: its final inference from "`F³⁰⁰(Ω₀)` lies in the box `U₋`" to capture is unsupported, and its own enclosures cannot support it as stated. A one-step repair closes the gap with a wide margin, and every other claim survives once the point-valued premises are replaced by enclosures. One sub-claim is **not** proved: that the certified attracting orbit *is the continuation of the M2 bifurcating branch*.

**Artifacts** (standalone mpmath 1.3.0 / Python 3.11.15; no repository module; Codex files read only): `m3_claude_review_v0_2.py` (`f00b6bc6…5be27e`), 28/28 at interval precision 80 digits (results `a02b8a89…ccf4`, log `7c7ca8da…1b49`), with identical verdicts at 60 and 120 digits (`de5663b9…50c5`, `b212b3af…c43e`); `m3_nominal_crosscheck_v0_2.py` (`6c18f1a6…41ab`), an independent 130-digit nominal iteration with no shared code; and from v0.1, `m3_string_endpoint_attack.py`. Inputs: Codex `m3_validated_entry.json` (`c4e1e5fc…95361`) and the M2 certificate JSON (`6fe4f3f3…9444a8`) for the certified host and `λ_c`.

---

## 1. The decisive finding: entry into `U₋` is not capture

Codex's §"Validated finite entry" concludes from `qbox₃₀₀ ⊂ U₋` that the trajectory is captured, with `U₋ := F̂(c) + DF̂(U₊)(U₊ − c)`. But **`U₋` is an outer interval enclosure of `F̂(U₊)`, not the image**. A point of `U₋` need not be the image of any point of `U₊`, so `F̂²(U₊) ⊂ int U₊` says nothing about it. My v0.1 review made the same error: I wrote "`F̂(qbox₃₀₀) ⊂ F̂²(U₊) ⊂ U₊`", which does not follow. I withdraw that sentence.

The gap is not merely formal at the level of the computed boxes. The enclosure of `F̂(U₋-box)` is **not** inside `U₊`: in coordinate 4 its radius is `1.347·10⁻⁵`, while `U₊` has radius `1.098·10⁻⁵`. That is because `U₋` (radius `1.2465·10⁻⁵` there) is wider than `H(U₊)` (radius `1.0985·10⁻⁵`). So the inference cannot be rescued at box level with these enclosures.

**Repair (both pass):**
1. **Direct.** One more validated step: `qbox₃₀₁ = F̂(qbox₃₀₀) ⊂ int U₊`, offset at most `0.0146` of the `U₊` radii. So `F³⁰¹(Ω₀)` lies in the trap.
2. **Alternative.** `qbox₃₀₀ ⊂ int H(U₊)`. By exact `H`-equivariance (`F̂∘H = H∘F̂`, with `H` an isometry of the weighted norm), `H(U₊)` is a trap for `F̂²` with the same margins and the same contraction bound.

---

## 2. The twelve review items

| # | Item | Verdict | Basis |
|---|---|---|---|
| 1 | Full-state propagation, steps 0–20 | **valid** | Inspected: cubic step `Ω + εΩ(k−|Ω|²) + g(ΣΩ − 3Ω)`, `atan2` value with derivative `(x ẏ − y ẋ)/(x²+y²)`, simultaneous harmonic-3 sync, radius `√(pr²+pi²)` with derivative `ẋ/(2√v)`. Derivatives are evaluated over the whole current box, so `F(X) ⊂ F(c) + DF(X)(X−c)` is the valid componentwise mean-value form. Centre-in-box was not checked in the package; I assert it at all 300 steps. Pre-sync radius bound `≥ 0.04221212242796385935136…` (Codex's value reproduced; tightest at `n = 2`). Final width `3.8·10⁻²⁴`. |
| 2 | Smoothness / `Arg₀` / phase chart | **valid; justification sharpened** | `F` depends on phases only through 2π-periodic functions (`cos h`, `sin h`, `sin 3(φⱼ − φᵢ)`), so it is `C^∞` wherever every pre-sync radius is positive. `Arg₀` is never invoked (radii `≥ 0.0422`). Branch-cut exclusion, which I verified at every step, affects only tightness, not validity (v0.1 overstated it as a validity condition). The ratio-`atan` chart from index 21 onward needs **positive** pre-sync real parts, since `atan(y/x)` agrees with `atan2` only modulo π: certified `≥ 1.3096147241289281421`. |
| 3 | Full-state → quotient conversion | **valid** | At index 21, `u·Ω₂₁ ≈ −4.085 + 6.342i`: the real part is negative, so the gauge legitimately uses `atan2` (as Codex does), with `|u·Ω₂₁|² ≥ 56.9` and the box off the negative real axis. The result is the M2 slice `Im(u·Ω) = 0`, `Re > 0`. It is a direct interval evaluation and always encloses. |
| 4 | Host and basis enclosures | **valid but unproved in the package; repaired** | Codex's boxes are a 90-digit point root `± 10⁻²⁵`. Proof that they contain the exact objects: Codex's host is `4.9·10⁻⁶⁰` from the M2 certified centre, so its box contains the M2 Krawczyk box. The basis evaluated in interval arithmetic over that box lies inside Codex's `10⁻²⁵` basis boxes. The repaired run drops the inflation entirely: the host is the M2 **Krawczyk image** `K(X)` (width `3·10⁻⁶⁰`), which contains the unique root because `K(X) ⊂ int X`, and `v₁`, `v₂` are computed by interval arithmetic from it. |
| 5 | Centred interval-AD, steps 21–300 | **valid** | 279 steps (Codex's log label "280" counts evaluations). Each step uses the full box Jacobian, an in-box centre (asserted), and outward arithmetic. Lower bounds over the whole span: gauge denominator `u·Re F ≥ 7.7839261785287128809` (not recorded by Codex), radii `≥ 1.3132035799719558266`. Final width `4.6·10⁻⁵⁷` with the tight host (`2.8·10⁻²⁷` in v0.1, `1.46·10⁻²²` in Codex's run). |
| 6 | `F³⁰⁰(Ω₀) ∈ U₋` | **true but insufficient** | §1. |
| 7 | `U₋ = F(U₊)` | **misnamed** | `U₋` is an enclosure `⊇ F̂(U₊)`. Its radii `(3.4464, 3.5458, 4.1260, 1.2465, 9.6573)·10⁻⁵` reproduce Codex's. |
| 8 | `F̂²(U₊) ⊂ int U₊` | **holds after repair** | The package uses the nominal 90-digit `F̂²(z₊)` as the centre value, a point premise. With interval `F̂²(c)` the margins are `(2.4161·10⁻⁶, 2.4920·10⁻⁶, 2.8455·10⁻⁶, 4.6357·10⁻⁷, 6.7559·10⁻⁶)`, all positive. Chart bounds during the trap: pre-sync real part `≥ 1.5047`, gauge denominator `≥ 8.8698`, radii `≥ 1.5073367430120650397`. |
| 9 | Weighted bound `0.957798686507835 < 1` | **holds** | Row sums `Σⱼ sup|D(F̂²)ᵢⱼ| rⱼ / rᵢ = (0.93160, 0.93162, 0.93307, 0.95780, 0.93244)`, from the interval Jacobian `DF̂(U₋)·DF̂(U₊)` with exact endpoints. The float-derived weights `r` are only a chosen positive scaling; the inequality holds for any positive weights. |
| 10 | Is this a genuine Banach argument? | **yes, once stated and once entry is repaired** | `U₊` is a closed convex box. `F̂²` is `C¹` on it (chart bounds), maps it into itself, and satisfies `‖F̂²x − F̂²x′‖_r ≤ 0.9578‖x − x′‖_r` with `‖z‖_r = maxᵢ|zᵢ|/rᵢ`. Banach then gives a unique fixed point `p ∈ U₊`, attracting all of `U₊` with ratio `≤ 0.9578` per two steps. Codex never states the theorem. `U₊ ∩ U₋ = ∅` (coordinate 5: `+0.437` vs `−0.437`), so `p` is not a fixed point of `F̂`. |
| 11 | Lift to the full complex period-two orbit | **holds; symmetry now certified** | Codex asserts that the cycle is the `H`-symmetric one by appeal to symmetry only. Certified here: Krawczyk for `G = H∘F̂` on `U₊` gives `K(U₊) ⊂ int U₊` (image radii about one tenth of `U₊`'s; `|G(c) − c| ≤ 6.8·10⁻⁵⁹`). So there is `z* ∈ U₊` with `F̂(z*) = Hz*`, hence `F̂²(z*) = z*`, hence `z* = p`. Then `F(Ω_p) = e^{iϑ}Ω̄_p` and `F²(Ω_p) = Ω_p`: a full period-two orbit with `W`, `Γ` alternating in sign. **Accumulated phase:** `ϑ ∈ [0.058598, 0.059551]` on `U₊` and its negative on `H(U₊)`. `α_{n+2} − αₙ = g(zₙ)` with `g` smooth and `g(p) = 0`, and `zₙ → p` geometrically, so `αₙ` converges. The full state therefore converges to **one** fixed rotation of the period-two orbit, not merely "modulo phase". |
| 12 | Conjugate entrance `√3 f₂` | **rigorous, no second propagation** | Every pre-sync component is certified nonzero along the `f₁` trajectory, so exact conjugation equivariance gives `Fⁿ(√3f₂) = conj Fⁿ(√3f₁)` for `n ≤ 301`. With `q(conj Ω) = H q(Ω)` (valid because `u·Ψ` is never negative real), `q(F³⁰¹(√3f₂)) ∈ H(int U₊)`. The trajectory converges to `H(p) = F̂(p)`: the same orbit at the opposite phase. Codex's 401-step replay is supporting evidence only. |

### Point-valued premises (the attention item)

| Point value | Role in package | Status |
|---|---|---|
| Host `u` and basis `v₁`, `v₂` (90-digit) `± 10⁻²⁵` | enclosure premise | valid, now proved (item 4); replaced by `K(X)` |
| `λ_c` as two decimal strings | enclosure premise | The upper string is the M2 endpoint truncated `1.81·10⁻⁴⁶` *inward* (v0.1 misstated this as `10⁻⁴⁷`), so it was uncertified. Recomputing `λ_c` in interval arithmetic over `K(X)` gives `0.367476394604213536549375991601945577650996214699067058307151…161` (width `10⁻⁵⁹`), which **lies inside Codex's interval**: harmless, now proved. |
| `F̂²(z₊)` nominal | trap centre **value** | a real point premise; replaced by interval evaluation (item 8) |
| Re-centring midpoints parsed from `str()` | centres | centre-in-box never checked; repaired and asserted at all 300 steps |
| `_lo`/`_hi` via `str(x)` | every inclusion, margin and contraction decision | **not enclosing**: `mpi_to_str` rounds to nearest, and about 50 % of tested intervals parse inward. Repaired with the exact `_mpi_` endpoint tuples. My own v0.2 tooling hit the same trap: a 25-digit display collapsed endpoints of width `10⁻²⁷`, so the nominal cross-check compares exact rationals. |
| Cycle locator `z₊`, radii, Perron weights | box centre and shape, norm scaling | legitimate choices, not premises |
| `ε`, `g`, `k`, `μ` strings | parameters | checked: `iv.mpf(str(·))` encloses the exact rationals |

Independent cross-check, with no shared code: a 130-digit nominal iteration from `√3f₁` lands inside the exact-endpoint interval boxes at `N = 300` and `N = 301`.

---

## 3. What is proved

**Theorem (exact-decimal model `ε = 1/20`, `g = 1/5`, `k = (1, 1.2208964704604097, 6.35310346037241)`, `λ = λ_c + 1/200`, with `λ_c` the M2 critical value).** Let `Ω₀ = √3 f₁ = (1, e^{−2πi/3}, e^{−4πi/3})`.
* Every iterate up to index 301 has all pre-sync components nonzero.
* In the M2 gauge, `F³⁰¹(Ω₀)` lies in the box `U₊`.
* `F̂²` contracts `U₊` into itself, with ratio `≤ 0.9578` in the weighted max-norm.
* Its unique fixed point `p` satisfies `F̂(p) = H(p)`.

Consequently `Fⁿ(Ω₀)` converges geometrically to `e^{iα∞}`·(a genuine period-two orbit of the complex state), on which `W` and `Γ` reverse sign at every step. The same holds for `√3 f₂`, with the orbit entered at the opposite phase.

## 4. Domain and the remaining gap

* **Not proved: that this orbit is "the M2 branch".** M2 proves a supercritical branch only for *sufficiently small* `μ > 0`, with no explicit range. M3 certifies the unique `H`-symmetric attracting period-two orbit **in `U₊`** at `μ = 0.005`. That this is the continuation of the M2 branch from `λ_c` is numerically supported, by the M2 amplitude law and by the M2 runs in which the host seed and the entrance reached the same cycle at `μ = 0.005`, but it is not certified. Certifying it would take a continuation proof over `μ ∈ (0, 0.005]` with explicit M2 remainder bounds; not attempted here (no M4).
* Not claimed: other `Q`, other `μ`, any basin beyond these two trajectories, the `λ = 0.5` orbit, any binary64 statement, any physical interpretation.

**Required corrections to Codex's text:**
1. Replace "`F³⁰⁰(Ω₀) ∈ U₋` … proves capture" by the `N = 301` entry into `U₊` (or the `H(U₊)` route).
2. Rename `U₋` as an *enclosure* of `F̂(U₊)`.
3. State the Banach theorem.
4. Replace string endpoints, string `λ_c`, nominal `F̂²(c)` and unchecked centres with enclosures.
5. Certify the `H`-symmetry of the captured cycle.
6. Replace "the M2 period-two branch" by "the `H`-symmetric attracting period-two orbit certified in `U₊`", unless a continuation proof is supplied.

**Disposition: `M3_ACCEPTED_WITH_CORRECTIONS`.** If the lead requires the literal "M2 branch" identification, that sub-claim alone is `M3_REQUIRES_MORE_PROOF`. No implementation, repository change, M4, or physical-magnetism claim follows.
