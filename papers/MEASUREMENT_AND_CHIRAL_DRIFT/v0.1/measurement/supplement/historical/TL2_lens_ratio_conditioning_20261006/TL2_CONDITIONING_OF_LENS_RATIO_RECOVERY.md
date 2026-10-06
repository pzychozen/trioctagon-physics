# TL2 Conditioning of lens ratio recovery
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

Read-only mathematical research · 6 October 2026

**For fixed known nonzero extraction vector `v`, recovering `q=d/r` from the amplitude `t` is not singular near tangency. Its absolute derivative tends to zero, and the inverse is globally Lipschitz. Recovering the angle `θ` from the same amplitude has an unbounded derivative and optimal Hölder exponent `2/3`. Recovering the small gap `δ=2−q` is absolutely stable but can have large relative error under fixed absolute output error. Small extraction gain is a separate, potentially severe source of amplification.**

TL0 and TL1 remain closed. No initializer, radius channel, historical object, physical calibration or interpretation is added.

```text
TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED
TL2 = READ-ONLY CONDITIONING AND INFORMATION-INTERFACE RESULT
```

## 1. Definitions and the error model

The current definitions are [boundary_response.py](project-source/trioctagon-physics/kernel_physics/boundary_response.py:18), lines18–83, and [srg.py](project-source/trioctagon-physics/kernel_physics/srg.py:21), lines21–28,50–94,122–130,154–179. [TL1](project-source/research/TL1_lens_srg_identifiability_20261006/TL1_LENS_SRG_INITIALIZER_IDENTIFIABILITY.md) proves exact fibres and zero routes. The authoritative checkout remains `project-source/trioctagon-physics`, on `main` at **82cab10cbe550f58c43163fb8b05fabdad1b05ae**.

Throughout,

\[
q=d/r\in[0,2],\quad \theta=\arccos(q/2)\in[0,\pi/2],\quad
I(\theta)=\frac{2\theta-\sin2\theta}{\pi},\quad
t=\sqrt{I(\theta)}\in[0,1],\quad \Omega_0=tv.
\]

Write `V=||v||>0`. The incident vector, named branch, transfer count and hence the *known vector* `v` are fixed within each inverse problem. Dependence on their gain is analyzed separately in §7. Error in the supplied `v` itself is not part of the specified model.

Denote the inverses by `Θ(t)=θ`, `Q(t)=q`, and `Δ(t)=2−Q(t)`. Here `Δ(t)` denotes the gap, not a perturbation operator. The scalar condition numbers are

\[
C_x^{\rm abs}(t)=|x'(t)|,\qquad
\kappa_x(t)=\left|\frac{t}{x(t)}x'(t)\right|.
\tag{1}
\]

The latter refers to **relative error in the amplitude t**, and is defined when `t>0` and the recovered variable is nonzero. Endpoint limits do not define relative error at a zero value. The vector error is arbitrary deterministic complex error with `||e||≤η`; no distribution or stochastic-noise assumption is used.

## 2. Exact interior derivatives

**DERIVED IDENTITY.** Since `I′(θ)=4sin²θ/π` and `q′(θ)=−2sinθ`, for `0<θ<π/2`, equivalently `0<q<2` and `0<t<1`,

\[
\frac{dt}{d\theta}=\frac{2\sin^2\theta}{\pi t},\qquad
\boxed{\frac{dt}{dq}=-\frac{\sin\theta}{\pi t}
=-\frac{\sqrt{4-q^2}}{2\pi t}},
\tag{2}
\]

\[
\boxed{\frac{dq}{dt}=-\frac{\pi t}{\sin\theta}
=-\frac{2\pi t}{\sqrt{4-q^2}}},\qquad
\boxed{\frac{d\theta}{dt}=\frac{\pi t}{2\sin^2\theta}
=\frac{2\pi t}{4-q^2}},
\tag{3}
\]

\[
\frac{d\delta}{dt}=\frac{\pi t}{\sin\theta}=-\frac{dq}{dt}.
\tag{4}
\]

These follow directly by differentiation and the inverse-function rule on the interior. The factors that seem to be `0/0` at tangency must be resolved by limits, not evaluated by substituting endpoints into the interior formulas.

## 3. Tangency asymptotics and endpoint regularity

Let `δ=2−q→0+`. Define the exact constants

\[
a=\frac{2}{\sqrt{3\pi}},\qquad
B=a^{-2/3}=\left(\frac{3\pi}{4}\right)^{1/3},\qquad
A=a^{-4/3}=B^2=\left(\frac{3\pi}{4}\right)^{2/3}.
\]

**ASYMPTOTIC RESULT.** The angle, normalized area and gain satisfy

\[
\theta(\delta)=2\arcsin\frac{\sqrt\delta}{2}
=\sqrt\delta\left(1+\frac\delta{24}+\frac{3\delta^2}{640}+O(\delta^3)\right),
\tag{5}
\]

\[
I(\delta)=\frac{4}{3\pi}\delta^{3/2}
\left(1-\frac{3\delta}{40}-\frac{3\delta^2}{896}+O(\delta^3)\right),
\tag{6}
\]

\[
G(\delta)=a\delta^{3/4}\left(1-\frac{3\delta}{80}+O(\delta^2)\right).
\tag{7}
\]

**Derivation.** The half-angle identity gives (5). From TL1's ratio derivative, with `q=2−δ`,

\[
\frac{dI}{d\delta}=\frac{\sqrt{4\delta-\delta^2}}{\pi}
=\frac2\pi\delta^{1/2}\left(1-\frac\delta8-\frac{\delta^2}{128}+O(\delta^3)\right).
\]

Integrate from zero to obtain (6), then take the positive square root to obtain (7). These are convergent local analytic expansions in the relevant fractional-power coordinate; they are not fitted exponents.

To invert, let `y=(t/a)^(4/3)=At^(4/3)`. Equation (7) gives `y=δ−δ²/20+O(δ³)`, hence

\[
\boxed{\delta(t)=At^{4/3}+\frac{A^2}{20}t^{8/3}+O(t^4)},
\tag{8}
\]

\[
\boxed{\Theta(t)=Bt^{2/3}\left(1+\frac A{15}t^{4/3}+O(t^{8/3})\right)},
\qquad Q(t)=2-\delta(t).
\tag{9}
\]

The resulting derivative asymptotics are

\[
\frac{dt}{dq}\sim-\frac{3a}{4}\delta^{-1/4},\qquad
\frac{dq}{dt}\sim-\frac43At^{1/3}\longrightarrow0,\qquad
\frac{d\theta}{dt}\sim\frac23Bt^{-1/3}\longrightarrow+\infty.
\tag{10}
\]

**EXACT THEOREM, local regularity.** At `t=0`, `Θ` is continuous and locally Hölder `2/3`, but not Lipschitz or differentiable with a finite derivative. The exponent is optimal: `Θ(t)~Bt^(2/3)` rules out any larger Hölder exponent at zero. A local derivative bound `Θ′(t)≤Ct^(−1/3)`, integrated between two positive arguments and extended to zero, proves the two-point Hölder bound.

In contrast, `Q` and `Δ` extend with one-sided derivative zero and are `C¹` at zero. Their first derivatives are locally Hölder `1/3`; their second derivatives diverge in magnitude like `t^(−2/3)`. This follows from (8)–(9), or from analytic inversion in the variable `t^(2/3)`. A leading increment of order `t^(4/3)` is compatible with a differentiable inverse; it is not evidence of an unbounded first derivative.

The forward gain `t(q)` is locally Hölder `3/4` at `q=2` and has no finite endpoint derivative. The separate geometric chart `θ(q)` has exponent `1/2` there. Thus the forward singularity does not imply an inverse singularity for every recovered variable.

### Coincidence is a different endpoint

At `q=0`, `θ=π/2`, `t=1`, the interior derivatives have ordinary one-sided limits:

\[
\frac{dt}{dq}\to-\frac1\pi,\qquad
\frac{dq}{dt}\to-\pi,\qquad
\frac{d\theta}{dt}\to\frac\pi2,\qquad
\frac{d\delta}{dt}\to\pi.
\tag{11}
\]

More explicitly,

\[
I(q)=1-\frac{2q}{\pi}+O(q^3),\qquad
t(q)=1-\frac q\pi-\frac{q^2}{2\pi^2}+O(q^3),
\]

\[
Q(t)=\pi(1-t)-\frac\pi2(1-t)^2+O((1-t)^3).
\tag{12}
\]

The absolute inverse conditioning is finite at coincidence. Relative error in `q` is nevertheless singular there because the true ratio approaches zero.

## 4. Relative condition numbers and a global absolute bound

**DERIVED IDENTITY.** Substituting (3)–(4) into (1), and using `πt²=2θ−sin2θ`, gives

\[
\boxed{\kappa_\theta=
\frac{2\theta-\sin2\theta}{2\theta\sin^2\theta}},\qquad
\boxed{\kappa_q=
\frac{2\theta-\sin2\theta}{2\sin\theta\cos\theta}
=\frac{2\theta}{\sin2\theta}-1},
\tag{13}
\]

\[
\boxed{\kappa_\delta=
\frac{2\theta-\sin2\theta}{2(1-\cos\theta)\sin\theta}}.
\tag{14}
\]

| Recovered variable | Relative conditioning as tangency is approached, `t→0+` | As coincidence is approached, `t→1−` |
|---|---|---|
| `θ` | `κ_θ→2/3` | `κ_θ→1` |
| `q` | `κ_q~(2/3)δ→0` | `κ_q~π/q→∞` |
| `δ=2−q` | `κ_δ→4/3` | `κ_δ→π/2` |

These finite tangency limits use *relative amplitude error*. They do not bound relative recovery error under an absolute error floor independent of `t`. At exactly zero angle/gap the corresponding relative error is undefined.

**EXACT THEOREM.** On the whole attainable amplitude interval,

\[
|Q(t_1)-Q(t_2)|\le\pi|t_1-t_2|,
\qquad |\Delta(t_1)-\Delta(t_2)|\le\pi|t_1-t_2|.
\tag{15}
\]

The constant `π` is sharp.

**Proof.** On the interior,

\[
\frac d{d\theta}\frac{I(\theta)}{\sin^2\theta}
=\frac{4(\sin\theta-\theta\cos\theta)}{\pi\sin^3\theta}\ge0.
\]

Indeed `sinθ−θcosθ` starts at zero and has derivative `θsinθ≥0`. The ratio tends to zero at `θ=0` and is one at `θ=π/2`. Therefore `t²=I≤sin²θ`, so `|Q′(t)|=πt/sinθ≤π`. Extend continuously at both endpoints and integrate. The limiting slope magnitude at `t=1` is `π`, proving sharpness. Since `Δ=2−Q`, the same bound holds for the gap. ∎

### An additive area error is a different inverse problem

If an independently perturbed scalar were `I=t²` with fixed additive error, then

\[
\delta(I)\sim AI^{2/3},\qquad
\theta(I)\sim BI^{1/3},\qquad
\left|\frac{dq}{dI}\right|=\frac{\pi}{2\sin\theta}\to\infty.
\tag{16}
\]

This would make even the ratio inverse non-Lipschitz at tangency. It is **not** the specified vector-amplitude error model. If area is computed from an amplitude estimate, its perturbation is `2t·error_t+error_t²`; one cannot replace that induced error by an unrelated fixed area-error budget and retain the same conditioning conclusion.

## 5. Arbitrary complex vector error

Let `w_hat=tv+e` with `||e||≤η`. Equip the complex vector space with the real inner product `Re(a†b)` when projecting onto the real amplitude line.

**EXACT THEOREM.** The unconstrained real least-squares estimate is

\[
\boxed{\widehat t=\frac{\operatorname{Re}(v^\dagger\widehat w)}{V^2}},\qquad
\boxed{|\widehat t-t|\le\frac{\|e\|}{V}\le E:=\frac\eta V.}
\tag{17}
\]

**Proof.** For real `s`,

\[
\|\widehat w-sv\|^2=\|\widehat w\|^2
-2s\operatorname{Re}(v^\dagger\widehat w)+s^2V^2.
\]

This strictly convex quadratic has its unique minimum at (17). Subtracting `t` gives `Re(v†e)/V²`; Cauchy–Schwarz proves the bound. It is sharp for the real parallel error `e=±ηv/V`. ∎

The distinction between complex orthogonality and real projection matters. Decompose

\[
e=(a_e+ib_e)v+e_H,\qquad a_e,b_e\in\mathbb R,\quad v^\dagger e_H=0.
\]

Then

\[
\widehat t-t=a_e,\qquad
\|e\|^2=(a_e^2+b_e^2)V^2+\|e_H\|^2.
\tag{18}
\]

Only the **real parallel component** changes this estimator. Both the Hermitian-orthogonal component `e_H` and the quadrature component `ib_e v` contribute residual error but no scalar bias. This statement would not hold for estimating `t` merely as `||w_hat||/V` in arbitrary noisy data.

Clipping gives the constrained least-squares estimate `t_tilde=min(1,max(0,t_hat))`. Projection onto `[0,1]` cannot increase distance to the true `t∈[0,1]`, so `|t_tilde−t|≤E`. This is an analysis of an estimator, not a change to the initializer.

For completeness, the full error ball gives a sharp feasible interval. Set `r_perp=w_hat−t_hat v`. Real orthogonality yields

\[
\|\widehat w-sv\|^2=\|r_\perp\|^2+V^2(s-\widehat t)^2.
\]

If `||r_perp||≤η`, the feasible gains are

\[
\left[\widehat t-\frac{\sqrt{\eta^2-\|r_\perp\|^2}}V,
\widehat t+\frac{\sqrt{\eta^2-\|r_\perp\|^2}}V\right]\cap[0,1].
\tag{19}
\]

If the residual exceeds the budget, or the intersection is empty, the observation is incompatible with the stated error model. Applying decreasing `Q` to the interval's endpoints reverses their order and gives the exact feasible ratio interval. Orthogonal residual thus consumes error budget even though it does not shift `t_hat`.

## 6. What fixed absolute error does near tangency

Combining (15) and (17) gives a global bound for the clipped ratio estimate:

\[
\boxed{|Q(\widetilde t)-Q(t)|\le\min(2,\pi E)
=\min\left(2,\frac{\pi\eta}{V}\right).}
\tag{20}
\]

The same absolute bound holds for the gap. Interior local vector-to-variable absolute condition numbers are `|x′(t)|/V` for `x=θ,q,δ`; their sharpness follows from a real parallel error.

**ASYMPTOTIC RESULT, resolved regime.** When `E≪t≪1`, first-order worst-case errors have the forms

\[
|\mathrm{error}_q|=|\mathrm{error}_\delta|
\lesssim\frac43At^{1/3}E,
\qquad
|\mathrm{error}_\theta|\lesssim\frac23Bt^{-1/3}E.
\tag{21}
\]

The relative angle and gap errors are approximately bounded by `(2/3)E/t` and `(4/3)E/t`. The ratio's relative error is approximately `(2/3)δ E/t`. These are local asymptotic statements requiring error small compared with the true amplitude. They cannot be extrapolated to `t→0` at fixed positive `E`.

**EXACT THEOREM / ASYMPTOTIC RESULT, unresolved regime.** If `t≤E`, the permitted error `e=−tv` makes the observed amplitude zero. Thus tangency cannot be distinguished from that small positive gain under this absolute-error budget. At true tangency `t=0`, the clipped estimate ranges over `[0,min(E,1)]`; hence the exact worst-case errors are

\[
\max |\mathrm{error}_q|=\max |\mathrm{error}_\delta|=\Delta(\min(E,1)),
\quad
\max |\mathrm{error}_\theta|=\Theta(\min(E,1)).
\tag{22}
\]

For `E→0+`, these become

\[
\boxed{\max |\mathrm{error}_q|\sim AE^{4/3},\qquad
\max |\mathrm{error}_\theta|\sim BE^{2/3}.}
\tag{23}
\]

For a fixed nonzero error budget, taking the true lens ever closer to tangency does not make these uncertainty scales disappear. The absolute ratio error remains controlled, while relative accuracy of the *vanishing gap* is unavailable once its size is below that scale. At `δ=0` relative gap error is undefined, not infinite by definition.

**Error-model distinction.** If instead `||e||≤ε_rel||Ω₀||=ε_rel tV`, then `E/t≤ε_rel`, and (13)–(14) give the local relative conditioning. The extraction norm cancels from this relative-output-error model. Its finite tangency limits coexist with the absolute-error floor above; neither analysis assumes random noise.

## 7. Finite SRG count and near-orthogonal incidence

Let `a_inc=|χ†ξ|>0`. TL1's exact norm identity gives

\[
V=a_{\rm inc}h_n,\qquad
\boxed{E=\frac\eta{a_{\rm inc}h_n}}.
\tag{24}
\]

This is the sharp amplification of fixed absolute output error into amplitude error. The unit-modulus eigenvalue phase and unit Fourier vector do not alter the norm.

**DERIVED IDENTITY / ASYMPTOTIC RESULT.** Put `p₀=1`, `p₁=q_s`, `p₂=q_s²c_s`. With the unchanged source constants,

\[
D_s=e^{-.269}(.382)^2=0.11150684043720778166\ldots,
\quad \rho=D_s^{1/3}=0.48131992098096438032\ldots.
\]

For every finite `n=3m+j`,

\[
\boxed{h_n=p_j\rho^{-j}\rho^n>0},\qquad
h_{n+3}=D_s h_n,\qquad
\frac1{h_n}=\frac{\rho^j}{p_j}\rho^{-n}.
\tag{25}
\]

The prefactor depends only on `n mod 3` and stays bounded above and below by positive constants. Therefore the asymptotic decay is exponential, `h_n=Θ(ρ^n)`, with rate

\[
-\log\rho=0.73122311358370791319\ldots.
\]

Each **three** added transfers amplifies the same absolute error by exactly `D_s⁻¹≈8.9680596821`. The exponential per-count rate is `ρ⁻¹≈2.0776202198`; this is not the exact ratio for every individual step because of the three residue prefactors.

| Transfer count `n` | `h_n` | Multiplier `1/h_n` in the absolute-error bound |
|---|---:|---:|
| 0 | 1 | 1 |
| 3 | 0.111506840437 | 8.96805968207 |
| 12 | 0.000154598772296 | 6468.35667028 |
| 30 | 2.97176936859×10⁻¹⁰ | 3.36499867913×10⁹ |

These are four evaluations of an exact formula, not a sweep or a calibrated detectability claim. No universal “practical cutoff count” exists without an error budget and a recovery-accuracy requirement. The native floating evaluator can reject sufficiently small intermediate gains, although they remain positive mathematically. No such arithmetic failure is a new exact zero route.

**EXACT THEOREM, near-orthogonal incident limit.** For fixed finite count, `a_inc→0+` gives `V→0+` and absolute amplification `1/V→∞`. Nevertheless every positive `a_inc` retains TL1's exact shape injectivity. To realize this limit at fixed incident norm, take an orthonormal pair `(χ,ψ)` and

\[
\xi_\varepsilon=\varepsilon\chi+\sqrt{1-\varepsilon^2}\,\psi,
\qquad0<\varepsilon\le1.
\]

Then `||ξ_ε||=1`, `|χ†ξ_ε|=ε`, and `V=εh_n`. Since `0≤t≤1`, all outputs satisfy `||Ω₀||≤εh_n`; the entire attainable segment shrinks uniformly to zero. At **ε=0 exactly**, TL1's whole lens domain collapses to zero and ratio identifiability fails. Poor conditioning at positive overlap and exact non-identifiability at zero are different statements.

A deterministic distinguishability criterion makes the finite-error issue precise. Two candidate gains have output distance `V|t₁−t₂|`. Their radius-`η` error balls intersect iff

\[
V|t_1-t_2|\le2\eta.
\tag{26}
\]

In particular, if `V≤2η`, the single observation `w_hat=v/2` is consistent with **every** gain in `[0,1]` under the error bound. This is ambiguity of a noisy observation; the exact map at positive `V` remains injective in shape. Decreasing `η` can improve it, whereas no precision improvement repairs the exact zero-overlap collapse.

## 8. Absolute radius remains non-identifiable

**INFORMATION-INTERFACE RESULT.** For all `α>0`,

\[
q(\alpha r,\alpha d)=q(r,d),\qquad
\Omega_0(\alpha r,\alpha d)=\Omega_0(r,d).
\tag{27}
\]

The first equality is cancellation of `α`; the second follows because all other factors are fixed. Thus different radii on the same positive scaling ray give exactly identical noiseless data. Even an exact, infinitely precise recovery of `q` leaves `r` arbitrary and `d=qr`. At coincidence it identifies `d=0`, but still no radius. An estimator of radius from `Ω₀` alone would have to assign different values to the same input, which is impossible.

This is non-identifiability, not a bad condition number to be fixed by a numerical method. Improving shape conditioning cannot restore an absent scale channel. It is not a physical no-go theorem.

## 9. Bounded checks and preservation

**NUMERICAL EVIDENCE.** [verify_tl2.py](project-source/research/TL2_lens_ratio_conditioning_20261006/verify_tl2.py) uses symbolic differentiation/series and 100-digit deterministic arithmetic. The numerical set is limited to three tangency gaps (`10⁻⁴,10⁻⁸,10⁻¹²`), two tangency error levels (`10⁻³,10⁻⁶`), one complex-vector error fixture plus its sharp parallel-error check, four transfer counts as tabulated, and three positive overlap magnitudes (`1,10⁻³,10⁻⁶`). The fixture vector has the native scalar-times-Fourier form; no physical units or noise law are assigned to these numbers.

**29/29 checks pass:** 12 symbolic/asymptotic/invariance checks, 8 bounded numerical groups and 9 preservation checks. The script verifies coefficients and condition-number limits, the real least-squares decomposition and sharp interval, and the stated finite-count scaling. The written arguments establish the universal statements; passing fixtures do not replace them. Full residuals, fixture values and source identities are in [TL2_RESULTS.json](project-source/research/TL2_lens_ratio_conditioning_20261006/TL2_RESULTS.json).

Exact conditioning must also be distinguished from numerical evaluation of the formulas. Direct subtraction in `2−q` or `2θ−sin2θ`, rounding of lens ratios, and cancellation in an eigenbra overlap can affect floating evaluation. The existing initializer's small-angle branch and precision guards remain unchanged. This report analyzes a bounded additive error on the final output; it does not certify every machine operation, uncertain parameter, or arbitrary input magnitude.

**Preservation PASS.** HEAD, working-tree status and index entries match the starting snapshot. Path/content hashes agree for all **16,018** files in the six protected inventories: authoritative repository, historical `kernel_TO`, `kernel_torment`, separate sibling `kernel_physics`, and pre-existing external `research` and `reconstruction`. The new TL2 directory alone is excluded. TL0, TL1, all parked lanes, existing papers, UI and pre-existing dirty/untracked work are unchanged. Only the external report, verification script and results file were written. No staging, commit, push, implementation or predecessor test rerun occurred.

## 10. Final answers and stop

1. **Is ratio recovery ill-conditioned near tangency?** Not with respect to absolute amplitude error at fixed nonzero `v`: `dq/dt→0`, and the inverse is globally `π`-Lipschitz. Its relative condition number also tends to zero under relative amplitude error. A tiny extraction norm and fixed absolute output error are separate limitations.
2. **Which variables are singular or Hölder?** `θ(t)` is optimally Hölder `2/3` and has unbounded derivative at tangency. `q(t)` and `δ(t)` are `C¹` with zero endpoint slope and Hölder-`1/3` first derivatives. The forward `t(q)` is Hölder `3/4`. An additive-area-error model instead gives inverse exponents `2/3` for the gap and `1/3` for the angle. At coincidence all absolute inverse slopes are finite, but relative `q` recovery is singular because `q=0`.
3. **What does fixed absolute output error do?** It yields amplitude uncertainty `E=η/V`. Near unresolved tangency, absolute ratio/gap uncertainty is of order `E^(4/3)` and angle uncertainty of order `E^(2/3)`; the small gap need not be relatively resolved. The vanishing local ratio derivative cannot be used outside the regime `E≪t`.
4. **How strongly does transfer count matter?** Absolute-error amplification grows exponentially, with an exact factor about `8.96806` per three transfers and bounded residue-dependent prefactors. Every finite gain remains nonzero in exact arithmetic.
5. **How does near-orthogonal incidence matter?** It multiplies absolute-error amplification by `1/|χ†ξ|`. Positive overlap retains exact injectivity; zero overlap destroys it for the whole domain. A purely relative-output-error model behaves differently because the gain cancels.
6. **What remains fundamentally unrecoverable?** Absolute common lens scale, including the radius, at every nonzero extraction as well as at zero. At zero overlap all lens information is unrecoverable through this map.
7. **ONE next top-layer calculation, if any?** No unconditional top-layer calculation is selected by these results. The next justified *conditional* calculation is a factorization test for an independently supplied top-layer observable or attachment: determine whether it is constant on TL1's scaling fibres and therefore can be recovered through the existing ratio channel. No such object is supplied or chosen here, so that calculation is not begun.

**OPEN QUESTION:** the historical top-circle identity and any independent geometric attachment remain unresolved. **STOP after TL2.**
