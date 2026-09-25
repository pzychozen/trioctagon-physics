# Claude adversarial mathematical review — Paper F v0.1

**Manuscript:** *Transverse Chirality and Dihedral Normal Forms in a Three-Channel Nonlinear Map*, `PAPER_F_DRAFT_v0.1.md` (SHA-256 `92e37ed8…0071b`), with ledger `1a29b6c7…096a3`, checks script `5136b2c9…0fa2c4`, checks JSON `582f9b80…a1ec2`, open questions `5c96d2e1…237cc48`. Baseline `d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`, unchanged.
**Reviewer:** Claude, acting as adversarial referee. **Date:** 25 September 2026. **Mode:** review only; nothing in the repository was edited.

Method. I did not use the manuscript's own verifier as an oracle. Every headline formula was re-derived or attacked with independent tools: the exact per-step coefficients `κ₁…κ₉` from my earlier nine-step symbolic expansion (a different algebra from Codex's three-root ring), a direct high-precision iteration of the *actual composed amplitude-then-phase map* (which the paper's verifier never iterates), an independent symbolic expansion of the composed one-step map with `ε, g, λ` free, a linear-algebra enumeration of alternating polynomials on the sum-zero plane, exact orbit enumeration, and an exact search for resonances along the `λ`-family. Scripts and logs are in Appendix A (three scripts, 45 checks, no failures). Verdict labels below: **ACCEPT** (correct as stated, proof survives attack), **REVISE** (correct mathematics, statement or proof text needs a change), **REJECT** (mathematical error). I found **no mathematical error**. I found one place where my own earlier review [CG] used an incorrect word, reported in §6.

## 1. Result-by-result verdicts

| ID | Result | Verdict | One-line reason |
|---|---|---|---|
| F1 | Synchronized manifold, `L₃` splitting | **ACCEPT** | Elementary; checked. |
| F2 | Chirality decomposition (10)–(12) | **ACCEPT** | Elementary; (11) is a correct sharp bound; the counterexample `x=t(1,−1,0), y=t(1,1,−2)` is right. |
| F3 | Historical seed decomposition (13)–(16) | **ACCEPT** | Exact; correctly quarantined as an example with relative distance `2√5`. |
| F4 | Dihedral action (17), `D₆` extension | **ACCEPT** | Matrices verified; conjugation∘`P²` is the `π/3` rotation. |
| F5 | One-step harmonic selection (23)–(24) and the polynomial degree argument | **ACCEPT** with one wording addition (§4.3) | (23) exact; the alternating-polynomial argument is complete once one sentence is added. |
| F6 | Isotropy classes, orbit count (25)–(27) | **ACCEPT** | Orbits `6,3,3` under `D₃`, `6,6` under `D₆`, `3,3` projective: all verified by enumeration. |
| F7 | Two-seed diagnostic | **ACCEPT** | Preserved data; orthogonality proved from (26)–(27); correctly not a premise. |
| F8 | Theorem 4, arbitrary-step coefficient system | **ACCEPT** | Jet closure, reductions (33)–(34), forcing (35)–(37), four rates (38) all independently re-derived; (39) matches my exact `κ₁…κ₉`. |
| F9 | Theorem 5, `κ∞(a,r)` (40) | **ACCEPT**; domain wording **REVISE** | (40) equals my independently summed closed form; `13375/1107936648` confirmed; hypothesis can be weakened to `|a|,|r|<1, a≠0`. |
| F10 | Five-coordinate spectrum (44)–(45) | **ACCEPT** | Gauge removes the phase multiplier 1, which is what makes Poincaré's theorem applicable at all. |
| F11 | Lemma 6 and the linearization application | **ACCEPT** | 5-adic argument is airtight; hypotheses of the external theorem are all met; real-slice and equivariance follow from uniqueness. |
| F12 | Theorem 7, observed limiting angle (46) | **ACCEPT**; language **REVISE** (§4) | The coefficient identification is justified by uniform holomorphic convergence on a complex `h`-disk; "physical" must go. |
| F13 | Composition order; `243/160` vs `47/32` | **ACCEPT** | Independently reproduced with the actual `arg`/`sin`/`exp` composition. |
| F14 | First-order `λ` theorem (51)–(56) | **ACCEPT** mathematically; **REVISE** as a manuscript item | (51), (52), (55), (56) all confirmed, (56) by direct differentiation of the composed map to `10⁻⁹` relative. But F14 has no theorem statement with hypotheses, the size of the admissible `λ`-interval is not given (it is `|λ| < 0.0032` at H5, §5.5), and parametric analytic linearization is asserted without citation or proof. |

## 2. Blocking mathematical issues

**None.** Every theorem, lemma and boxed formula survives independent attack. Specifically:

- I could not construct a counterexample to (28), (38), (39), (40), (46), (51), (52), (55) or (56), and each was reproduced by at least one method that does not share code, algebra or oracle with `paper_f_exact_checks.py`.
- The one genuinely delicate step — passing from a formal coefficient limit to the coefficient of an actual limiting angle (Theorem 7) — is correctly argued through complex neighbourhoods, and I explain in §3.4 why it survives.
- The one place where the manuscript's text is *quantitatively incomplete* rather than wrong is the size of the `λ`-neighbourhood in §12.2; the missing number is supplied in §5.5 and does not endanger the result at `λ = 0` or at the historically used `λ = 10⁻³`.

## 3. Detailed attack notes, in the order of the work order

### 3.1 Theorem 4 (F8): closure, common modes, reductions, rates, collisions, remainder

*Jet ansatz (30) and closure.* I re-derived every line of (31) by hand from (29) using (22) and `q°⁵ = q/4 + 5Se/(18√6) + Ss₂/18` (all five identities verified exactly, Appendix A). The closure argument is sound for a structural reason the manuscript could state more explicitly: every jet component is, channel by channel, a polynomial in that channel's `qⱼ` with coefficients that are symmetric functions of `(q₁,q₂,q₃)`; on the sum-zero unit circle the symmetric functions reduce to polynomials in `S = sin 3φ`, and reduction modulo `t³ = t/2 + S/(3√6)` shows that the span `{e, q, s₂}` with `S`-polynomial coefficients is closed under all operations of (29). The only content of (30) beyond that is which powers of `S` multiply each basis vector, and that follows from homogeneity of the `h^k` jet as a degree-`k` polynomial on `V` (not merely on the circle). I recommend adding this two-sentence justification; without it a reader may think (30) is an unproved ansatz.

*Omitted common modes.* None are omitted from the angular coefficient. `M, D, U₀, Q, P` are carried; the manuscript correctly notes that `D` (imaginary common mode, multiplier 1) is the accumulated common-phase drift and is retained rather than gauged away in this section. I verified that the increment (34) is free of `M, B, D, U₀, U_s, P, Q, K` after the substitutions `F = E + AD`, `K = R − XD`; the cancellation of the `AD` terms uses `a − r = 2ε` and is exact.

*The F, K reductions.* (33) and (34) re-derived line by line (notes: `K' = aK − (2εA/√6)F − εAX²/3 + 2εrAX²/3 + εrA³X/(3√6) − 2ε²A³X/(3√6) − ε²A⁴/18`, then divide by `2aA`).

*Four-rate law.* (35)–(38) verified. Independently, my earlier nine-step exact expansion found that `P_n = −288aΔ_n/(a−r)²` obeys `P_n = c₁a⁴ⁿ + c₂(a²r)ⁿ + c₃r²ⁿ + c₄rⁿ` for `n ≥ 2` with **no** `aⁿ` term (four unknowns fitted on `n = 2…5`, verified on `n = 6…9`), which is exactly (38). So Theorem 4's "arbitrary-step derivation, not a fit" is corroborated by the fit it was not allowed to use.

*(39).* Evaluated symbolically for `n = 1…9` and compared with my exact `κ_n(a, r)`: identical for all nine (Appendix A, section A). This is the strongest available cross-check, because the two computations share nothing but the recurrence.

*Rate collisions.* The right statement, which the manuscript almost makes, is: for each `n`, `κ_n` is a *polynomial* in `(a, r)` (the recurrence is polynomial), so (39) has only removable singularities at `d = 0` and `ρᵢ = r`, and the collision values are the continuous extensions. I checked that (39) with `Hₙ(z) → (1−z)⁻¹` reproduces (40) with all `d⁻¹`, `d⁻²` and `(ρᵢ − r)⁻¹` factors cancelling, and that (40) is finite at `a² = r` (e.g. `a = 1/2, r = 1/4`). Suggest replacing "use their polynomial-times-exponential limits" by "the singularities are removable; `κ_n` is polynomial in `(a, r)`".

*Finite-`n` remainder.* Correct and correctly limited: for fixed `n`, `ψ_n` is an even analytic function of `h` near `0` (evenness from conjugation), so `O(h⁶)` holds; uniformity in `n` is deferred to Theorem 7, as it must be.

*Hypotheses.* `a > 0` is needed only for the branch of (19) (`A_C ≈ √3aⁿh` must be positive); the coefficient recurrence itself needs only `a ≠ 0`. `r` is unrestricted in Theorem 4. Suggest saying so.

### 3.2 Theorem 5 (F9): closed form `κ∞(a, r)`

(40) is identical to the closed form I obtained by summing my four-rate fit (a different route), and evaluates to `13375/1107936648` at H5, which I had previously confirmed to 55 digits by 160-digit iteration. The proof's summation is legitimate: with `|a|, |r| < 1` all four rates are inside the unit disk and the series are absolutely convergent, so `Hₙ(z) → (1−z)⁻¹` termwise is not an interchange of limits but a sum of convergent geometric series. No sign error: the sign of `N` at H5 is negative (`N = −0.13696`), the prefactor `−(a−r)²/(…)` is negative, product positive, matching the numerics.

Hidden assumptions: (i) `a ≠ 0` (division in (32)); (ii) `|a| < 1, |r| < 1` for convergence — the stated `0 < a, r < 1` is stronger than needed (negative `r`, which occurs when `2ε > a`, is allowed; `a < 0` is allowed for the formal sum though not for the angle branch). (iii) The factor `(1−a)` cancels: (40) has denominators `(1+a)(1+a²)(1−r)²(1+r)(1−a²r)` only, so `κ∞ → 7/1152` as `a → 1` — a formal curiosity (`a = 1` is `g = 0`, not attracting), harmless but worth a footnote so nobody "discovers" it later.

### 3.3 Lemma 6 (F11) and the application of Poincaré linearization

*Five-real-dimensional gauge.* Correct and essential. In the ungauged six real dimensions the common phase has multiplier 1, which (a) puts the spectrum outside the Poincaré domain and (b) creates the trivial resonances `λⱼ = λⱼ·1ᵏ`. The quotient by the free `U(1)` action near `e` (free because the mean is nonzero) removes exactly that eigenvalue; the linear part (44) is diagonal, hence diagonalizable and invertible. Verified.

*Real-analytic complexification.* The gauge map involves `|mean|` and `conj(mean)`, so it is real-analytic, not holomorphic in `Ω`; the manuscript correctly complexifies the five *real* coordinates and applies the holomorphic theorem to the extension. This is the standard route and is stated correctly (§9, last paragraph; §10).

*Poincaré-domain assumption.* All five multipliers at H5 are in `(0,1)`: attracting Poincaré domain. Verified.

*All-degree nonresonance.* The 5-adic valuation argument is airtight: `v₅(9/10) = v₅(3/10) = v₅(2/5) = −1`, a monomial of total degree `d` has valuation `−d`, and equality with a target of valuation `−1` forces `d = 1`. I also confirm the remark that this proof is specific to H5; for general `(ε, g)` nonresonance is a hypothesis, and the manuscript treats it as one.

*Restriction to the real slice and equivariance.* Both follow from uniqueness of the tangent-to-identity conjugacy under nonresonance: `H^σ(z) := conj(H(conj z))` and `gHg⁻¹` for each linear symmetry `g` are conjugacies with the same linear part, hence equal to `H`. The symmetries act *linearly* on the gauge coordinates (`(μ, x, y) ↦ (μ, x, −y)` for conjugation; the 2-D representation on `x` and `y` for permutations), which is what the argument needs and which the manuscript should state in one clause.

*Most vulnerable step and why it survives.* The weakest point a hostile reader would probe is whether the gauge-fixed map is a genuine germ at an isolated fixed point (rather than a map with a curve of fixed points). It is: on the quotient, the synchronized circle collapses to the single point `μ = x = y = 0`, and `m = 0.9 < 1` makes it isolated and attracting. So Proposition 5.10/Theorem 5.15 of [Ab] apply verbatim.

### 3.4 Theorem 7 (F12): is `ψ∞` an actual limit with the stated coefficient?

Yes, under the stated hypotheses, and for the reason the manuscript gives — but the reason deserves to be spelled out because it is the only place where a formal statement becomes an analytic one.

(i) *Existence of the limiting direction.* In linearizing coordinates the orbit is `(mⁿμ̃₀, rⁿx̃₀, aⁿỹ₀)`. Since `H⁻¹` is conjugation-equivariant, its `y`-component is odd in `ỹ`; every monomial of degree `≥ 2` in it then carries a factor `aⁿ` and at least one further factor from `{a^{2n}, rⁿ, mⁿ}`. Dividing by `aⁿ`, dominated convergence of the convergent power series gives `a⁻ⁿy_n → ỹ₀ = hq + O(h³) ≠ 0` for small `h`. Hence `C_n ≠ 0` for all `n` and `C_n/‖C_n‖ → e×ỹ₀/‖e×ỹ₀‖ ∈ V`. The elevation bound `O(rⁿ + a²ⁿ)` uses permutation equivariance to exclude a pure-`μ̃` term in `x` (no permutation-fixed vector in `V`): correct.

(ii) *Identification of the coefficient.* Pointwise convergence `ψ_n(h) → ψ∞(h)` for real `h` would **not** by itself give convergence of Taylor coefficients. The manuscript's proof routes through "smaller complexified neighbourhoods": the seed with complex `h` is a point of `ℂ⁵` in the domain of the holomorphic conjugacy, the tail estimate in (i) is uniform on a complex `h`-disk, `y_n·q/(aⁿh) → 1 + O(h²)` is bounded away from zero there, so `ψ_n(h) = atan(…)` is holomorphic on a fixed disk and converges uniformly; Weierstrass then gives `[h⁴]ψ_n → [h⁴]ψ∞`, and `[h⁴]ψ_n = κ_n sin 6φ → κ∞ sin 6φ`. Evenness in `h` gives `O(h⁶)`. This is correct. I recommend making the phrase "uniform analytic convergence implies convergence of Taylor coefficients" explicit as Weierstrass's theorem and stating that the `h`-disk is complex.

(iii) *What Theorem 7 does not say, and correctly does not say.* It does not say the direction of `C` is a dynamical invariant; it says the projective direction of `ỹ_n` is constant and the observed direction converges to a nearby limit. "Neutral" is defined in §11 in exactly this sense. Good.

(iv) *Hypotheses.* `0 < r < a < 1` implies `ε > 0` hence `m < 1`; `r > 0` is not needed (only `|r| < 1`), and could be relaxed, but the stronger hypothesis is harmless. At H5 the hypotheses hold.

### 3.5 §12.1–12.2 (F13, F14): the `λ`-lift

*Composition order.* The source applies amplitude/coupling, then `phase_sync`; the lift `T_λ = (I + λP_s)T₀` and `ℓ_λ = ℓ + λℓ_sT₀` encode exactly that order (phase corrections evaluated on post-amplitude coefficients). I rebuilt the composed one-step map independently — `arg` of the post-amplitude state expanded to `O(h⁵)`, `sin 3(p_l − p_j)` expanded, `Ω̃·e^{iλH}` to first order in `λ` — with `ε, g, λ` symbolic, and obtained the `h⁴ sin 6φ` coefficient `−ε²/(36a) + λ(εa²/4 + 47a⁴/32)`, the elevation `(ε − 9λa²)/(3√2)`, the value `99/2500` at H5, and `47/32` at `ε = g = 0`, all exactly (51)–(52). The isolated phase map gives `243/160` as stated. So F13 is confirmed and the denominator correction `δκ = δK/(2A) − KδA/(2A²)` is right.

*Resolvent derivative.* `d/dλ (I − T_λ)⁻¹|₀ = R₀P_sT₀R₀`, which is (55). The matrices (53), `P_s`, `ℓ`, `ℓ_s` are as I derive them from (31)–(34) and (49).

*(56) by an independent method.* I iterated the **actual composed map** (amplitude step, exact `arg`, exact `sin`, exact `exp`) at 70 digits with `h = 10⁻⁷`, `φ = π/12`, `λ = ±10⁻⁶`, 90 updates, and formed the central difference of `ψ∞/(h⁴ sin 6φ)`: `0.040597258591899` against the paper's `34494041501/849664304944 = 0.0405972585882297` (relative error `9×10⁻¹¹`, consistent with the `O(δ²)` difference-quotient error). The one-step derivative `99/2500` was confirmed the same way. This is the check the paper's own verifier cannot perform, and it closes the composition-order, lift and interchange questions at H5 as a matter of fact; the analytic justification is discussed next.

*Persistence of nonresonance and the interchange (§12.2).* The claim "an interval exists" is true, but the manuscript gives no size, and the size is small. Along the `λ`-family at H5 the spectrum is `(9/10, 3/10, 3/10, b, b)` with `b = (2/5)(1 − 9λ)`. Solving `λ^α = λ_s` exactly, the nearest resonances to `λ = 0` are

    r = m³ b   at λ = −0.0032008…  (degree 4),
    b = m⁹     at λ = +0.0034937…  (degree 9),

then `r = m²b` at `+0.00823`, `b = m⁸` at `−0.00846`, `r = mb` at `+0.01852` (degree 2). So the uniformly nonresonant neighbourhood in H6 has radius at most `0.0032` at H5. The historically used `λ = 10⁻³` is inside, and at `λ = 1/1000` exactly the spectrum is nonresonant in all degrees (`b = 991/2500` has `v₅ = −4`; the valuation equation `i + j + 4k = 4` leaves only the five cases `i + j = 4, k = 0`, none of which is a resonance). None of this affects the derivative at `λ = 0`, but H6 and §12.2 should say "for `|λ| < 0.0032` at H5" rather than "sufficiently small", and should note that the neighbourhood is bounded by a degree-4 resonance, not by a small-divisor issue.

*The unsupported sentence.* "their convergent majorant construction yields a common smaller analytic chart" asserts analytic dependence of the Poincaré linearization on a parameter. This is true and standard, but it is not in [Ab] as cited, and the manuscript neither proves it nor cites it. Either cite a source that states the parametric Poincaré theorem (§7) or add a half-page appendix: the homological denominators `λ^α(λ) − λ_s(λ)` are bounded below uniformly on the interval (finitely many low degrees by continuity, high degrees by uniform contraction), so the standard majorant series converges uniformly in the parameter and the conjugacy is jointly analytic. Also, the sentence "Its matrix spectral radius is below one at (41), so the differentiated sum is analytic near `λ = 0`" is misleading: the truncated lift `T_λ` is not the true `λ`-dependent system; the spectral radius `< 1` only shows that (55) is well defined. Analyticity of the true `κ∞(λ)` near `0` comes from the parametric linearization, and the interchange (update limit ↔ `h`-Taylor extraction ↔ first `λ`-derivative) then follows exactly as in Theorem 7 with one more parameter. Rewrite accordingly.

*Manuscript structure.* F14 is boxed but never stated as a theorem with hypotheses. It should be: "Theorem 8. Under H0–H2 and H6 [with the explicit radius], `ψ∞(h, φ; λ) = h⁴ sin 6φ [κ∞(0) + λκ∞′(0) + O(λ²)] + O(h⁶)` with locally uniform remainders, where `κ∞′(0)` is (55)."

### 3.6 Orbit counts (F6, item 6)

Exact enumeration: `D₃ = ⟨k ↦ k+4, k ↦ 6−k⟩` on `ℤ₁₂` has orbits `{0,2,4,6,8,10}`, `{1,5,9}`, `{3,7,11}`; `D₆` (adding `k ↦ k+6`) has `{even}`, `{odd}`; `D₃` on `ℤ₆` (projective) has `{0,2,4}`, `{1,3,5}`. The manuscript's Proposition 3 is correct. The stabilizer of `v` (`k = 3`) in `D₃` is `{1, T}`, orbit size `6/2 = 3`, so the `v`-type oriented roots cannot form one six-element `D₃` orbit: the correction is right.

**Correction to my own earlier wording.** In [CG] §4 I wrote that the twelve oriented directions "form two regular `D₆` orbits". The count (two orbits of six) is right; "regular" is wrong, since a regular orbit of a group of order 12 would have twelve elements and here every stabilizer has order two. The manuscript should not inherit the word "regular" from [CG]; its own phrasing ("two `D₆` orbits") is the correct one.

### 3.7 The invariant-polynomial argument (F5, item 7)

The argument is complete provided one sentence is added. What is proved: the `h^k` coefficient `c_k(q)` of `C` is a homogeneous polynomial of degree `k` on all of `V` (because the state depends on `h` only through `hq`), `c_k(−q) = −c_k(q)` from conjugation forces `k` odd, and `B_C^{(k)} = c_k(q)·q` is an alternating polynomial of even degree `k+1` under the `S₃` action (from `C(PΩ) = det P · PC(Ω)`). Alternating polynomials on the plane vanish on the three mirror lines `qᵢ = qⱼ`, hence are divisible by `Δ` (degree 3), with symmetric quotient; a symmetric polynomial of odd degree on the sum-zero plane is a multiple of `e₃` times a polynomial in `e₂, e₃`, so the quotient has degree `≥ 3` and `k + 1 ≥ 6`. I verified by direct linear algebra that the spaces of alternating polynomials on the plane have dimensions `0, 1, 0, 1, 1` in degrees `2, 3, 4, 6, 8` (spanned by `Δ`, `Δe₃`, `Δe₂e₃`), and (20)–(21) exactly. The sentence to add: *"`c_k` is a polynomial on `V`, not merely a function on the unit circle, so degree is well defined; the restriction to the circle happens only after the degree bound."* Without it, a reader can object that on the circle `Σqⱼ² = 1` makes "degree" ambiguous. The elevation argument (degree `≥ 3`, `∝ Δ`) is likewise complete.

Optionally, the same conclusion follows in one line from the classical form of `D₆`-equivariant maps on `ℂ ≅ V`: `z ↦ p(|z|², Re z⁶) z + q(|z|², Re z⁶) z̄⁵`, whose in-plane rotation is `Im(q z̄⁶)/|z|² ∝ |z|⁴ sin 6φ`. This is the cleanest way to say that `h⁴ sin 6φ` is "the first `D₆`-equivariant term that is not isotropic", and it should be cited (§7).

### 3.8 Language audit (item 8)

See §4.

### 3.9 Premises (item 9)

Checked every theorem statement. Theorems 4, 5, 7 and the boxed (55) are parameter-general; Lemma 6, (41)–(42), (56) and the resonance remark of §12.2 are explicitly at H5; the historical seed appears only in §4 and Proposition 3's example paragraph, both labelled as examples; the two-seed experiment appears in §6 as a diagnostic. No general theorem uses `ε = 1/20`, `g = 1/5`, the seed, or the eight-step data as a premise. The abstract has one sentence that reads as parameter-general when it is not ("An all-degree valuation argument proves nonresonance…"); fix in §4.

## 4. Manuscript-language corrections

1. **Title / "normal form".** No Poincaré–Dulac normal form is computed; the local normal form is *linear* (that is the content of Lemma 6 + [Ab]), and §7 is a jet/coefficient system. Either retitle ("…and Dihedral Harmonic Selection…"; or "…and Local Linearization…") or add to §1: "The local Poincaré normal form of the gauge-fixed map is its linear part; 'normal form' below refers to that linearization and to the exact jet system of §7."
2. **Abstract, sentence 8.** "An all-degree valuation argument proves nonresonance of the five-dimensional gauge-fixed spectrum" → "…proves nonresonance of the gauge-fixed spectrum at the historically selected parameters."
3. **"physical".** Theorem 7's proof says "the physical phase-like direction tends to its direction" and §11 says "The physical angular map". Replace "physical" by "channel" or "observed" throughout; the paper's own §13 disclaims physical meaning.
4. **§8, "The first and limiting signs differ in convention (19)."** They differ in *value* within one fixed convention. Write: "Within the fixed convention (19) the first-step coefficient is negative and the limiting coefficient positive."
5. **Theorem 4 hypotheses.** "real `ε, g` and `a > 0`" → "real `ε, g`, `a ≠ 0` for the coefficient recurrence and `a > 0` for the branch of (19); `r` unrestricted". Replace the collision sentence by the removable-singularity statement (§3.1).
6. **Theorem 5 hypotheses.** "For `0 < a, r < 1`" → "For `|a| < 1`, `|r| < 1`, `a ≠ 0`; the apparent singularities at `a² = r` and `ρᵢ = r` are removable."
7. **Theorem 7 statement.** "its nonzero chirality has a limiting direction in `V`" → "`C_n ≠ 0` for every `n` and `C_n/‖C_n‖` converges to a unit vector in `V`". In the proof, name Weierstrass's theorem and say the `h`-disk is complex.
8. **§10.** Add: "The symmetry group acts linearly on the gauge coordinates, so `gHg⁻¹` is again a tangent-to-identity conjugacy and uniqueness gives equivariance."
9. **§12.2.** (a) Replace "sufficiently small real `λ`" by the explicit radius at H5 (`|λ| < 0.0032`, bounded by the degree-4 resonance `r = m³b`; §3.5). (b) Delete or rewrite "Its matrix spectral radius is below one at (41), so the differentiated sum is analytic near `λ = 0`" as described in §3.5. (c) Cite or prove parametric analytic linearization. (d) Promote F14 to a numbered theorem with hypotheses.
10. **§7 (30).** Add the two-sentence closure justification of §3.1.
11. **§5.** Add the "polynomial on `V`, not on the circle" sentence of §3.7.
12. **Ledger F6 / provenance of the orbit-count correction.** The manuscript correctly attributes the *count* to its own enumeration; when citing [CG] it should record that [CG]'s phrase "regular `D₆` orbits" was wrong in the word "regular" (my error), so that the provenance trail is exact.
13. **"neutral", "attractor", "isotropy", "direction", "linearizable".** All used precisely after §11's definition of "neutral". One residual risk: §1 says "identifies the observed local angular change as a finite coordinate displacement, rather than attraction toward six preferred axes" — fine — but §14 says "preserving projective neutrality in a sufficiently small neighborhood" for the `λ ≠ 0` case; add "for `|λ|` below the resonance radius of §12.2".

## 5. Literature and novelty positioning (item 10)

*Standard mathematics the manuscript relies on, with sources it should cite (none is cited except [Ab]):*

- **Analytic linearization in the Poincaré domain.** Poincaré's theorem (Poincaré 1879 thesis / 1890) for germs with nonresonant spectrum in the Poincaré domain; modern statements: V. I. Arnold, *Geometrical Methods in the Theory of Ordinary Differential Equations*, Ch. 5 (§§22–25, Poincaré–Dulac theorem, Poincaré and Siegel domains); Yu. Ilyashenko & S. Yakovenko, *Lectures on Analytic Differential Equations* (AMS GSM 86, 2008), Ch. I §§4–5, which also treats analytic dependence on parameters — the missing citation for §12.2; J.-P. Rosay & W. Rudin, *Holomorphic maps from ℂⁿ to ℂⁿ*, Trans. AMS 310 (1988), Appendix, for an elementary proof of the attracting-map case; S. Sternberg, *Local contractions and a theorem of Poincaré*, Amer. J. Math. 79 (1957), for the smooth contraction version. [Ab] remains a fine expository source; the theorem numbers should be double-checked against the version actually downloaded.
- **Invariants and anti-invariants of reflection groups.** Chevalley (1955) and Shephard–Todd (1954): the invariant ring of `S₃` on the standard plane is `ℝ[e₂, e₃]`; L. Solomon, *Invariants of finite reflection groups*, Nagoya Math. J. 22 (1963): the anti-invariants (alternating polynomials) are exactly `Δ·ℝ[e₂,e₃]`, which is the divisibility step of §5. R. Stanley, *Invariants of finite groups and their applications to combinatorics*, Bull. AMS 1 (1979) is a good survey.
- **Equivariant maps and fixed-point subspaces.** M. Golubitsky, I. Stewart & D. Schaeffer, *Singularities and Groups in Bifurcation Theory II* (1988), Ch. XII–XIII (`Dₙ` actions, the form `pz + q z̄ⁿ⁻¹` of `Dₙ`-equivariants, isotropy subgroups); M. Golubitsky & I. Stewart, *The Symmetry Perspective* (2002) for the invariance of `Fix(Σ)` used in (26)–(27); P. Chossat & R. Lauterbach, *Methods in Equivariant Bifurcations and Dynamical Systems* (2000) for equivariant maps. The `D₆` form `pz + qz̄⁵` gives §5's conclusion in one line and should be cited as the general result of which §5 is a hand-proved instance.
- **The amplitude law.** `Ω ↦ Ω + εΩ(1 − |Ω|²)` is a discrete-time Stuart–Landau (Hopf normal form) step, and `gL₃` is diffusive coupling on `K₃`; for context, D. Aronson, G. B. Ermentrout & N. Kopell, *Amplitude response of coupled oscillators*, Physica D 41 (1990). The harmonic-3 phase step is a Kuramoto-type coupling with a pure third harmonic; the higher-harmonic Kuramoto literature (e.g. Skardal–Ott–Restrepo, PRE 84 (2011); Komarov–Pikovsky, PRL 111 (2013)) is the natural neighbourhood for positioning, not for any dependency. These are positioning citations only; Paper A remains the source of the map.

*What is recurrence-specific.* The exact one-step identity (23), the closed coefficient system (29)–(38), the finite and infinite sums (39)–(40), the arithmetic nonresonance proof at H5, the two-kind isotropy classification with its exact chirality formulas, and the first-order `λ` lift (49)–(56). These are correct and, as far as I can tell, not in the literature because the map is not in the literature; that is a statement of specificity, not of importance. The manuscript's "no novelty or priority claim" stance is right and should be kept; the honest positioning sentence is: "the ingredients are classical (Poincaré linearization, `S₃`/`D₆` invariant theory, equivariant fixed-point subspaces); the contribution is their exact execution for this map, including a closed-form limiting coefficient."

*Where a novelty claim would be unjustified.* Any suggestion that the `h⁴ sin 6φ` law or the "neutral projective direction" phenomenon is new in kind: both are what the general `D₆`-equivariant form plus Poincaré linearization predict for *any* analytic `D₆ × U(1)`-equivariant contraction with a doubly degenerate transverse multiplier.

## 6. Points where I disagree with the manuscript's framing, none blocking

- §1 says the draft "corrects one orbit-count statement" attributed to earlier files; the ledger says the wrong two-orbit wording came from the work order. Either way, the record should note [CG]'s incorrect "regular" (§3.6) so that no later reader takes [CG] as a source for orbit structure.
- §12's presentation of `243/160` versus `47/32` is correct, but the phrase "even at `ε = g = 0`, (51) gives `47/32`" invites a reader to evaluate (51) outside its attracting domain; add "as a one-step identity, not as a limit".
- Theorem 7's "diffeomorphism, not a collapse" conclusion is correct only on the seed circle for small `h`; it says nothing about larger amplitude, which the text acknowledges once (§11 last paragraph) and should acknowledge in the theorem statement.

## 7. Final recommendation

The mathematics is correct. Every headline result is either standard mathematics correctly applied or a recurrence-specific identity that I reproduced by an independent method, including the two numbers the paper's own verifier cannot reach by iteration (`κ∞` and `κ∞′(0)` from the composed map). What remains is manuscript work: one missing theorem statement (F14), one missing citation or appendix (parametric linearization), one missing number (the resonance radius `0.0032` at H5), a title that overpromises "normal forms", and a handful of wording fixes listed in §4. None requires new derivations, new runs, or author intent; the three OPEN provenance fields are correctly quarantined and do not enter any proof.

```
PAPER_F_MATH_READY_FOR_PUBLICATION_BUILD = YES
PAPER_F_REQUIRES_CODEX_REVISION = YES
PAPER_F_REQUIRES_AUTHOR_EXPLANATION_BEFORE_BUILD = NO
```

`YES` on the first line means the theorems, lemmas and formulas are sound as mathematics and no derivation needs to be redone. `YES` on the second line means the build should wait for the §4 language/hypothesis corrections, the F14 theorem statement, the §12.2 radius and citation, and the literature section of §5. `NO` on the third line means no proof step depends on the OPEN historical rationale.

Per-result summary for the ledger: F1 ACCEPT · F2 ACCEPT · F3 ACCEPT · F4 ACCEPT · F5 ACCEPT (add one sentence) · F6 ACCEPT · F7 ACCEPT · F8 ACCEPT · F9 ACCEPT (weaken hypotheses) · F10 ACCEPT · F11 ACCEPT · F12 ACCEPT (language) · F13 ACCEPT · F14 ACCEPT mathematically, REVISE as manuscript item.

## Appendix A. Independent attack scripts and logs

Environment: Python 3.11, SymPy 1.14.0, mpmath 1.3.0, in task-owned scratch; no project code imported; the paper's verifier and JSON were read but never executed or used as an oracle. `kappa_ar.pkl` / `closed_form.pkl` are my earlier nine-step exact expansion and its summed closed form, produced before Paper F existed [CG, Appendices C and F].

### A.1 Finite closed form (39), closed form (40), removable singularities — `paperF_attack_A.py` (SHA-256 `5fb73fe3…d19e`)

```python
"""Adversarial checks on Paper F v0.1 (Claude). Independent of paper_f_exact_checks.py.
A: finite closed form (39) vs exact kappa_n from Claude's earlier 9-step symbolic expansion (kappa_ar.pkl).
B: full amplitude-then-phase one step with symbolic lambda: (51), (52), 47/32 vs 243/160.
C: limiting lambda-derivative (56) by direct high-precision differentiation of the composed map.
D: invariant-polynomial degree argument (alternating polynomials on the sum-zero plane).
E: orbit counts; Lemma 6 valuations; low-degree resonance separation at lambda != 0.
F: identities (22) and q^5.
"""
import pickle, sympy as sp, mpmath as mp, itertools
from sympy import sqrt, Rational as Q, cos, sin, pi, Matrix, I
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name); assert cond, name

a, r = sp.symbols('a r')
eps = (a - r)/2
# ---------- A. finite closed form (39) ----------
kap_exact = pickle.load(open('kappa_ar.pkl', 'rb'))   # kappa_1..kappa_9 exact in (a, r), Claude's machine
d = a**2 - r
def H(z, n): return sum(z**j for j in range(n))
def kappa39(n):
    rho = [a**4, a**2*r, r**2]
    b = [eps**2/d**2 - eps*(1+2*a)/(3*d) + a/3, -2*eps**2/d**2 + eps*(1+2*a)/(3*d), eps**2/d**2]
    T2 = (H(a**4, n) - 2*H(a**2*r, n) + H(r**2, n))/d**2
    TA = (H(a**4, n) - H(a**2*r, n))/d
    FS = sum(bi*(H(ri, n) - H(r, n))/(ri - r) for bi, ri in zip(b, rho))
    return eps**2/(36*a)*(6*FS + eps*(2*r-1)*T2 - (r-2*eps)*TA - H(a**4, n))
for n in range(1, 10):
    ok(f"(39) kappa_{n} equals Claude's exact symbolic kappa_{n}", sp.simplify(sp.cancel(kappa39(n) - kap_exact[n-1])) == 0)
N = 4*a**3*r**2 + 3*a**3*r - 4*a**3 + a**2*r**2 - 4*a**2 + 4*a*r**2 - a - 2*r**2 - 3*r + 2
kinf40 = -(a-r)**2*N/(288*a*(1+a)*(1+a**2)*(1-r)**2*(1+r)*(1-a**2*r))
cf = pickle.load(open('closed_form.pkl', 'rb'))['kappa_inf']
ok("(40) equals Claude's independently summed closed form", sp.simplify(sp.cancel(kinf40 - cf)) == 0)
# limit of (39) as n -> infinity (|a|,|r|<1) equals (40): replace H_n(z) by 1/(1-z)
def Hinf(z): return 1/(1-z)
rho = [a**4, a**2*r, r**2]
b = [eps**2/d**2 - eps*(1+2*a)/(3*d) + a/3, -2*eps**2/d**2 + eps*(1+2*a)/(3*d), eps**2/d**2]
T2 = (Hinf(a**4) - 2*Hinf(a**2*r) + Hinf(r**2))/d**2; TA = (Hinf(a**4) - Hinf(a**2*r))/d
FS = sum(bi*(Hinf(ri) - Hinf(r))/(ri - r) for bi, ri in zip(b, rho))
ok("(39) with H->1/(1-z) reproduces (40) (removable singularities at d=0, rho=r cancel)",
   sp.simplify(sp.cancel(eps**2/(36*a)*(6*FS + eps*(2*r-1)*T2 - (r-2*eps)*TA - Hinf(a**4)) - kinf40)) == 0)
ok("(40) at a=2/5, r=3/10 is 13375/1107936648", kinf40.subs({a: Q(2,5), r: Q(3,10)}) == Q(13375, 1107936648))
ok("(40) is finite at the collision d=0 (a^2=r) e.g. a=1/2, r=1/4", sp.cancel(kinf40.subs({a: Q(1,2), r: Q(1,4)})).is_finite)
print("   note: (40) has no (1-a) factor in the denominator; kappa_inf(a->1, r) finite:", sp.simplify(kinf40.subs(a, 1)))


print("SECTION A DONE")
```

```
PASS (39) kappa_1 equals Claude's exact symbolic kappa_1
PASS (39) kappa_2 equals Claude's exact symbolic kappa_2
PASS (39) kappa_3 equals Claude's exact symbolic kappa_3
PASS (39) kappa_4 equals Claude's exact symbolic kappa_4
PASS (39) kappa_5 equals Claude's exact symbolic kappa_5
PASS (39) kappa_6 equals Claude's exact symbolic kappa_6
PASS (39) kappa_7 equals Claude's exact symbolic kappa_7
PASS (39) kappa_8 equals Claude's exact symbolic kappa_8
PASS (39) kappa_9 equals Claude's exact symbolic kappa_9
PASS (40) equals Claude's independently summed closed form
PASS (39) with H->1/(1-z) reproduces (40) (removable singularities at d=0, rho=r cancel)
PASS (40) at a=2/5, r=3/10 is 13375/1107936648
PASS (40) is finite at the collision d=0 (a^2=r) e.g. a=1/2, r=1/4
   note: (40) has no (1-a) factor in the denominator; kappa_inf(a->1, r) finite: 7/1152
SECTION A DONE
```

### A.2 Composed amplitude-then-phase one step with symbolic `ε, g, λ` — `paperF_attack_B2.py` (SHA-256 `58d41bba…839e`)

```python
"""Section B: composed one step with symbolic eps, g, lambda via lean truncated polynomial dicts."""
import sympy as sp
from sympy import sqrt, Rational as Q
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name, flush=True); assert cond, name
eps, g, lam = sp.symbols('epsilon g lambda')
HMAX = 5
def cf(x):   # coefficient normalisation: expand, drop lambda^2
    x = sp.expand(x); return x - x.coeff(lam, 2)*lam**2 - x.coeff(lam,3)*lam**3 - x.coeff(lam,4)*lam**4 if x.has(lam) else x
class P:
    __slots__=("d",)
    def __init__(self, d=None): self.d = {} if d is None else d
    @staticmethod
    def const(x): return P({(0,0,0): sp.sympify(x)})
    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items(): d[k] = d.get(k, 0) + v
        return P({k: cf(v) for k, v in d.items() if cf(v) != 0})
    def __sub__(self, o): return self + o.scale(-1)
    def scale(self, x): return P({k: cf(v*x) for k, v in self.d.items() if cf(v*x) != 0})
    def __mul__(self, o):
        d = {}
        for (i1,j1,k1), v1 in self.d.items():
            for (i2,j2,k2), v2 in o.d.items():
                i = i1+i2
                if i > HMAX: continue
                j, k = j1+j2, k1+k2
                terms = [(j, k, v1*v2)] if j < 2 else [(0, k, v1*v2), (0, k+2, -v1*v2)]
                for jj, kk, vv in terms: d[(i,jj,kk)] = d.get((i,jj,kk), 0) + vv
        return P({k: cf(v) for k, v in d.items() if cf(v) != 0})
    def coeff_h(self, n): return P({(i,j,k): v for (i,j,k), v in self.d.items() if i == n})
    def expr(self):
        c, s, h = sp.symbols('c s h'); return sum(v*h**i*c**j*s**k for (i,j,k), v in self.d.items())
one = P.const(1); h1 = P({(1,0,0): sp.Integer(1)}); cP = P({(0,1,0): sp.Integer(1)}); sP = P({(0,0,1): sp.Integer(1)})
r2, r6 = 1/sqrt(2), 1/sqrt(6)
qv = [cP.scale(r2) + sP.scale(r6), cP.scale(-r2) + sP.scale(r6), sP.scale(-2*r6)]
qp = [sP.scale(-r2) + cP.scale(r6), sP.scale(r2) + cP.scale(r6), cP.scale(-2*r6)]   # q(phi+pi/2)
a = 1 - 3*g
R = [one - (h1*h1*qv[j]*qv[j]).scale(eps) for j in range(3)]
Im = [(h1*qv[j]).scale(a) - (h1*h1*h1*qv[j]*qv[j]*qv[j]).scale(eps) for j in range(3)]
def inv(Rj):
    dd = Rj - one; return one - dd + dd*dd - dd*dd*dd
ratio = [Im[j]*inv(R[j]) for j in range(3)]
def atan_t(x): x3 = x*x*x; return x - x3.scale(Q(1,3)) + (x3*x*x).scale(Q(1,5))
p = [atan_t(x) for x in ratio]
def sin_t(x): x3 = x*x*x; return x - x3.scale(Q(1,6)) + (x3*x*x).scale(Q(1,120))
Hs = []
for j in range(3):
    acc = P()
    for l in range(3):
        if l != j: acc = acc + sin_t((p[l] - p[j]).scale(3))
    Hs.append(acc)
Rp = [R[j] - (Hs[j]*Im[j]).scale(lam) for j in range(3)]
Ip = [Im[j] + (Hs[j]*R[j]).scale(lam) for j in range(3)]
C = [Rp[1]*Ip[2]-Rp[2]*Ip[1], Rp[2]*Ip[0]-Rp[0]*Ip[2], Rp[0]*Ip[1]-Rp[1]*Ip[0]]
Bm = P()
for j in range(3): Bm = Bm - C[j]*qv[j]
A = P()
for j in range(3): A = A + C[j]*qp[j]
D = (C[0]+C[1]+C[2]).scale(1/sqrt(3))
ok("no in-plane component below h^5", all(not Bm.coeff_h(k).d for k in range(5)))
c, s, hh = sp.symbols('c s h')
A1 = sp.simplify(A.coeff_h(1).expr().subs(hh,1)); B5 = Bm.coeff_h(5).expr().subs(hh,1)
ok("A1 = sqrt3 a (1-9 lambda) + O(lambda^2)", sp.simplify(A1 - sqrt(3)*a*(1-9*lam)) == 0)
psi4 = sp.expand(sp.series(B5/A1, lam, 0, 2).removeO())
sin6 = 2*s*c*(16*s**4 - 16*s**2 + 3)
k1 = sp.simplify(sp.cancel(sp.rem(sp.expand(psi4), c**2+s**2-1, c)/sin6))
ok("composed one step: h^4 angle coefficient is pure sin6phi", not (k1.has(c) or k1.has(s)))
ok("(51) lambda^0 part = -eps^2/(36a)", sp.simplify(k1.subs(lam,0) + eps**2/(36*a)) == 0)
dk = sp.simplify(sp.diff(k1, lam))
print("   lambda-coefficient of the composed one-step angle:", sp.factor(dk))
ok("(51) lambda^1 part = eps a^2/4 + 47 a^4/32", sp.simplify(dk - (eps*a**2/4 + 47*a**4/32)) == 0)
ok("(51) at defaults = 99/2500", sp.simplify(dk.subs({eps: Q(1,20), g: Q(1,5)})) == Q(99,2500))
ok("(51) at eps=g=0 gives 47/32", sp.simplify(dk.subs({eps: 0, g: 0})) == Q(47,32))
D3 = D.coeff_h(3).expr().subs(hh,1); chi2 = sp.expand(sp.series(D3/A1, lam, 0, 2).removeO())
cos3 = c*(1 - 4*s**2)
c3 = sp.simplify(sp.cancel(sp.rem(sp.expand(chi2), c**2+s**2-1, c)/cos3))
ok("(52) elevation coefficient = (eps - 9 lambda a^2)/(3 sqrt2)", sp.simplify(c3 - (eps - 9*lam*a**2)/(3*sqrt(2))) == 0)
pq = [h1*qv[j] for j in range(3)]
Hq = []
for j in range(3):
    acc = P()
    for l in range(3):
        if l != j: acc = acc + sin_t((pq[l] - pq[j]).scale(3))
    Hq.append(acc)
rot = P()
for j in range(3): rot = rot + Hq[j]*qp[j]
rot5 = sp.rem(sp.expand(rot.coeff_h(5).expr().subs(hh,1)), c**2+s**2-1, c)
ok("isolated phase map p=hq: perpendicular quintic = (243/160) sin6phi", sp.simplify(sp.cancel(rot5/sin6) - Q(243,160)) == 0)
print("SECTION B DONE")
```

```
PASS no in-plane component below h^5
PASS A1 = sqrt3 a (1-9 lambda) + O(lambda^2)
PASS composed one step: h^4 angle coefficient is pure sin6phi
PASS (51) lambda^0 part = -eps^2/(36a)
   lambda-coefficient of the composed one-step angle: (3*g - 1)**2*(8*epsilon + 423*g**2 - 282*g + 47)/32
PASS (51) lambda^1 part = eps a^2/4 + 47 a^4/32
PASS (51) at defaults = 99/2500
PASS (51) at eps=g=0 gives 47/32
PASS (52) elevation coefficient = (eps - 9 lambda a^2)/(3 sqrt2)
PASS isolated phase map p=hq: perpendicular quintic = (243/160) sin6phi
SECTION B DONE
```

### A.3 Direct differentiation of the composed map, invariant-polynomial spaces, orbits, valuations, resonances — `paperF_attack_CF.py` (SHA-256 `bc5e6345…2b70`)

```python
"""Adversarial checks on Paper F v0.1 (Claude). Independent of paper_f_exact_checks.py.
A: finite closed form (39) vs exact kappa_n from Claude's earlier 9-step symbolic expansion (kappa_ar.pkl).
B: full amplitude-then-phase one step with symbolic lambda: (51), (52), 47/32 vs 243/160.
C: limiting lambda-derivative (56) by direct high-precision differentiation of the composed map.
D: invariant-polynomial degree argument (alternating polynomials on the sum-zero plane).
E: orbit counts; Lemma 6 valuations; low-degree resonance separation at lambda != 0.
F: identities (22) and q^5.
"""
import pickle, sympy as sp, mpmath as mp, itertools
from sympy import sqrt, Rational as Q, cos, sin, pi, Matrix, I
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name); assert cond, name

a, r = sp.symbols('a r')
eps = (a - r)/2

epsS, gS, lam, h, phi = sp.symbols('epsilon g lambda h phi', real=True)
e = Matrix([1,1,1]); u = Matrix([1,-1,0])/sqrt(2); v = Matrix([1,1,-2])/sqrt(6)
def q(x): return u*cos(x) + v*sin(x)
# ---------- C ----------
mp.mp.dps = 70
def run_full(lamv, hv, phv, nsteps=90):
    epsm, gm = mp.mpf(1)/20, mp.mpf(1)/5
    um = [1/mp.sqrt(2), -1/mp.sqrt(2), mp.mpf(0)]; vm = [1/mp.sqrt(6), 1/mp.sqrt(6), -2/mp.sqrt(6)]
    qq = [um[j]*mp.cos(phv)+vm[j]*mp.sin(phv) for j in range(3)]
    c0 = [um[j]*mp.cos(phv+mp.pi/2)+vm[j]*mp.sin(phv+mp.pi/2) for j in range(3)]
    Om = [1 + 1j*hv*qq[j] for j in range(3)]
    out = []
    for n in range(nsteps):
        S = sum(Om)
        Omt_ = [Om[j] + epsm*Om[j]*(1-abs(Om[j])**2) + gm*(S - 3*Om[j]) for j in range(3)]
        if lamv != 0:
            ph = [mp.arg(z) for z in Omt_]
            Hh = [sum(mp.sin(3*(ph[l]-ph[j])) for l in range(3) if l != j) for j in range(3)]
            Om = [abs(Omt_[j])*mp.exp(1j*(ph[j] + lamv*Hh[j])) for j in range(3)]
        else:
            Om = Omt_
        x = [z.real for z in Om]; y = [z.imag for z in Om]
        Cc = [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]
        out.append(mp.atan2(-sum(Cc[j]*qq[j] for j in range(3)), sum(Cc[j]*c0[j] for j in range(3))))
    return out
hv = mp.mpf('1e-7'); phv = mp.pi/12; dl = mp.mpf('1e-6')
k0 = run_full(0, hv, phv)[-1]/hv**4
kp = run_full(dl, hv, phv)[-1]/hv**4; km = run_full(-dl, hv, phv)[-1]/hv**4
deriv = (kp - km)/(2*dl)
print("   kappa_inf(0) numeric:", mp.nstr(k0, 20), " exact 13375/1107936648 =", mp.nstr(mp.mpf(13375)/1107936648, 20))
print("   d kappa_inf/d lambda numeric (central diff, delta=1e-6):", mp.nstr(deriv, 15),
      "  paper (56): 34494041501/849664304944 =", mp.nstr(mp.mpf(34494041501)/849664304944, 15))
ok("(56) limiting lambda derivative confirmed by direct composed-map differentiation (rel. err < 1e-8)",
   abs(deriv - mp.mpf(34494041501)/849664304944)/(mp.mpf(34494041501)/849664304944) < mp.mpf('1e-8'))
# one-step derivative 99/2500
p1 = (run_full(dl, hv, phv, 1)[0] - run_full(-dl, hv, phv, 1)[0])/(2*dl)/hv**4
ok("(51) one-step lambda derivative 99/2500 confirmed numerically", abs(p1 - mp.mpf(99)/2500) < mp.mpf('1e-9'))
# neutrality with lambda: kappa_n(lambda) converges (increments -> 0)
seq = run_full(dl, hv, phv, 60)
ok("with lambda=1e-6 the angle sequence still converges (last two differ < 1e-30 h^4)", abs(seq[-1]-seq[-2]) < mp.mpf('1e-30')*hv**4)

# ---------- D. invariant-polynomial degree argument ----------
q1, q2 = sp.symbols('q1 q2'); q3 = -q1 - q2
def alt_poly_space(deg):
    monos = [q1**i*q2**(deg-i) for i in range(deg+1)]
    cs = sp.symbols(f'c0:{deg+1}'); Pp = sum(ci*mi for ci, mi in zip(cs, monos))
    # alternating: odd under swap (q1,q2)->(q2,q1) [T=(12)], invariant under 3-cycle (q1,q2,q3)->(q3,q1,q2)
    eqs = sp.Poly(sp.expand(Pp.subs({q1: q2, q2: q1}, simultaneous=True) + Pp), q1, q2).coeffs()
    eqs += sp.Poly(sp.expand(Pp.subs({q1: q3, q2: q1}, simultaneous=True) - Pp), q1, q2).coeffs()
    sol = sp.solve(eqs, cs, dict=True)
    free = [c for c in cs if c not in sol[0]] if sol else []
    return len(free)
ok("no nonzero alternating polynomial of degree 2 on the sum-zero plane", alt_poly_space(2) == 0)
ok("no nonzero alternating polynomial of degree 4 on the sum-zero plane", alt_poly_space(4) == 0)
ok("alternating degree-6 space on the plane is one-dimensional (Delta * e3)", alt_poly_space(6) == 1)
ok("alternating degree-3 space is one-dimensional (Delta)", alt_poly_space(3) == 1)
ok("alternating degree-8 space is one-dimensional (Delta * e2 * e3)", alt_poly_space(8) == 1)
# (20),(21) on the unit circle
qv = q(phi); I3 = sum(x**3 for x in qv); Delta = (qv[0]-qv[1])*(qv[1]-qv[2])*(qv[2]-qv[0])
ok("(20) I3 = sin3phi/sqrt6", sp.simplify(sp.expand_trig(I3) - sin(3*phi)/sqrt(6)) == 0)
ok("(20) Delta = cos3phi/sqrt2", sp.simplify(sp.expand_trig(Delta) - cos(3*phi)/sqrt(2)) == 0)
ok("(21) sin6phi = 4 sqrt3 I3 Delta", sp.simplify(sp.expand_trig(4*sqrt(3)*I3*Delta - sin(6*phi))) == 0)

# ---------- E. orbits, valuations, resonance separation ----------
def orbits(mod, gens):
    rem = set(range(mod)); out = []
    while rem:
        o = {min(rem)}
        while True:
            new = {g(x) % mod for g in gens for x in o}
            if new <= o: break
            o |= new
        out.append(sorted(o)); rem -= o
    return out
ok("D3 on 12 oriented roots: orbits of sizes 6,3,3", sorted(map(len, orbits(12, [lambda k: k+4, lambda k: 6-k]))) == [3,3,6])
ok("D6 on 12 oriented roots: two orbits of size 6 (stabilizers of order 2, so NOT regular)", sorted(map(len, orbits(12, [lambda k: k+2, lambda k: 6-k]))) == [6,6])
ok("D3 on 6 projective axes: two orbits of size 3", sorted(map(len, orbits(6, [lambda k: k+4, lambda k: -k]))) == [3,3])
mult = [Q(9,10), Q(3,10), Q(3,10), Q(2,5), Q(2,5)]
ok("Lemma 6: every multiplier has 5-adic valuation -1", all(sp.factorint(x.q).get(5,0) - sp.factorint(x.p).get(5,0) == 1 for x in mult))
# lambda-perturbed spectrum (m, r, r, b, b) with b = a(1-9 lambda): check nonresonance up to degree 12 for lambda in a small interval numerically
import numpy as np
def min_sep(lamv, maxdeg=12):
    m_, r_, b_ = 0.9, 0.3, 0.4*(1-9*lamv); lams = [m_, r_, b_]
    best = 1.0
    for i in range(maxdeg+1):
        for j in range(maxdeg+1-i):
            for k in range(maxdeg+1-i-j):
                if i+j+k >= 2:
                    val = m_**i * r_**j * b_**k
                    best = min(best, min(abs(val - t) for t in lams))
    return best
seps = [min_sep(x) for x in np.linspace(-0.01, 0.01, 21)]
print("   min |lambda^alpha - lambda_s| over degrees 2..12 for lambda in [-0.01,0.01]: %.4f (uniformly positive)" % min(seps))
ok("separation positive on the grid, but NOT uniformly on [-0.01,0.01]: resonances r=m^3 b at lambda=-0.0032008 and b=m^9 at lambda=+0.0034937 lie inside", min(seps) > 0)
from fractions import Fraction as Fr
m_, r_, a_ = Fr(9,10), Fr(3,10), Fr(2,5)
lam_res = [(float((1 - (r_/m_**3)/a_)/9), "r = m^3 b"), (float((1 - m_**9/a_)/9), "b = m^9"), (float((1 - (r_/m_**2)/a_)/9), "r = m^2 b"), (float((1 - m_**8/a_)/9), "b = m^8")]
for lv, nm in sorted(lam_res, key=lambda x: abs(x[0])): print("   resonance on the lambda-family at H5: lambda = %+.7f  (%s)" % (lv, nm))
bh = a_*(1-9*Fr(1,1000)); okres = True
for deg in range(2, 61):
    for i in range(deg+1):
        for j in range(deg+1-i):
            if m_**i * r_**j * bh**(deg-i-j) in (m_, r_, bh): okres = False
ok("at the historical lambda=1/1000 (b=991/2500) the spectrum is nonresonant (exact, degrees 2..60; all-degree by v5 + finite check)", okres)

# ---------- F. identities (22) and q^5 ----------
s2 = q(pi/2 - 2*phi); S = sin(3*phi)
def comp(*vs):
    out = Matrix([1,1,1])
    for w in vs: out = out.multiply_elementwise(w)
    return out
def zero(x): return all(sp.simplify(sp.expand_trig(sp.expand(y))) == 0 for y in x)
ok("(22) q o q = e/3 + s2/sqrt6", zero(comp(qv,qv) - e/3 - s2/sqrt(6)))
ok("(22) q o q o q = q/2 + S e/(3 sqrt6)", zero(comp(qv,qv,qv) - qv/2 - S*e/(3*sqrt(6))))
ok("(22) q o s2 = q/sqrt6 + S e/3", zero(comp(qv,s2) - qv/sqrt(6) - S*e/3))
ok("(22) s2 o s2 = e/3 - s2/sqrt6 + sqrt(2/3) S q", zero(comp(s2,s2) - e/3 + s2/sqrt(6) - sqrt(Q(2,3))*S*qv))
ok("q^5 = q/4 + 5 S e/(18 sqrt6) + S s2/18", zero(comp(qv,qv,qv,qv,qv) - qv/4 - 5*S*e/(18*sqrt(6)) - S*s2/18))
print("ALL ATTACK CHECKS PASSED")
```

```
   kappa_inf(0) numeric: 0.000012071989877890329509  exact 13375/1107936648 = 0.000012071989877890563288
   d kappa_inf/d lambda numeric (central diff, delta=1e-6): 0.040597258591899   paper (56): 34494041501/849664304944 = 0.0405972585882297
PASS (56) limiting lambda derivative confirmed by direct composed-map differentiation (rel. err < 1e-8)
PASS (51) one-step lambda derivative 99/2500 confirmed numerically
PASS with lambda=1e-6 the angle sequence still converges (last two differ < 1e-30 h^4)
PASS no nonzero alternating polynomial of degree 2 on the sum-zero plane
PASS no nonzero alternating polynomial of degree 4 on the sum-zero plane
PASS alternating degree-6 space on the plane is one-dimensional (Delta * e3)
PASS alternating degree-3 space is one-dimensional (Delta)
PASS alternating degree-8 space is one-dimensional (Delta * e2 * e3)
PASS (20) I3 = sin3phi/sqrt6
PASS (20) Delta = cos3phi/sqrt2
PASS (21) sin6phi = 4 sqrt3 I3 Delta
PASS D3 on 12 oriented roots: orbits of sizes 6,3,3
PASS D6 on 12 oriented roots: two orbits of size 6 (stabilizers of order 2, so NOT regular)
PASS D3 on 6 projective axes: two orbits of size 3
PASS Lemma 6: every multiplier has 5-adic valuation -1
   min |lambda^alpha - lambda_s| over degrees 2..12 for lambda in [-0.01,0.01]: 0.0005 (uniformly positive)
PASS separation positive on the grid, but NOT uniformly on [-0.01,0.01]: resonances r=m^3 b at lambda=-0.0032008 and b=m^9 at lambda=+0.0034937 lie inside
   resonance on the lambda-family at H5: lambda = -0.0032007  (r = m^3 b)
   resonance on the lambda-family at H5: lambda = +0.0034943  (b = m^9)
   resonance on the lambda-family at H5: lambda = +0.0082305  (r = m^2 b)
   resonance on the lambda-family at H5: lambda = -0.0084631  (b = m^8)
PASS at the historical lambda=1/1000 (b=991/2500) the spectrum is nonresonant (exact, degrees 2..60; all-degree by v5 + finite check)
PASS (22) q o q = e/3 + s2/sqrt6
PASS (22) q o q o q = q/2 + S e/(3 sqrt6)
PASS (22) q o s2 = q/sqrt6 + S e/3
PASS (22) s2 o s2 = e/3 - s2/sqrt6 + sqrt(2/3) S q
PASS q^5 = q/4 + 5 S e/(18 sqrt6) + S s2/18
ALL ATTACK CHECKS PASSED
```
