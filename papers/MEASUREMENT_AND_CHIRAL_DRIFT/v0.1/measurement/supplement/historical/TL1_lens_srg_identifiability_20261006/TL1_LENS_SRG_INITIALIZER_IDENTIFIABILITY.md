# TL1 Lens to SRG initializer identifiability
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

Read-only mathematical research · 6 October 2026

**The adopted initializer retains exactly the lens shape ratio `d/r`, provided the fixed incident/extraction factor is nonzero. It loses the entire positive common scale. If the incident vector is orthogonal to the selected eigenbra, it loses even the shape ratio and returns zero for every admissible lens.**

For the exact mathematical map, every fibre is classified below. No historical top circle is selected, no physical meaning is assigned to the ratio, and no definition is changed.

```text
TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED
TL0 = CLOSED
TL1 = READ-ONLY INFORMATION-INTERFACE RESULT
```

## 1. Current definitions and fixed data

**SOURCE FACT / DEFINITION AND ADOPTION.** The authoritative checkout is [trioctagon-physics](project-source/trioctagon-physics), initially on `main` at **82cab10cbe550f58c43163fb8b05fabdad1b05ae**. Its existing dirty and untracked work was recorded and preserved.

The relevant definitions are [boundary_response.py](project-source/trioctagon-physics/kernel_physics/boundary_response.py:18), lines18–37 and55–103; [srg.py](project-source/trioctagon-physics/kernel_physics/srg.py:21), lines21–28,50–94,114–130 and154–179; and the numerical contracts in [_response_numeric.py](project-source/trioctagon-physics/kernel_physics/_response_numeric.py:52). The existing [Atlas 08](project-source/trioctagon-physics/research/mathematical_atlas/entry_08_boundary_srg_handoff/TRIOCTAGON_ATLAS_08_BOUNDARY_SRG_HANDOFF_SOURCE_PACKET_v0.1.md) already records the gain, derivative and transfer reduction. TL1 independently verifies those ingredients and assembles the complete lens-fibre classification. The predecessor is not revised or recertified.

Let

\[
\mathcal D=\{(r,d)\in\mathbb R^2:r>0,\ 0\le d\le2r\},\qquad
\theta=\arccos\frac{d}{2r},\qquad
I(\theta)=\frac{2\theta-\sin2\theta}{\pi},\qquad G=\sqrt I.
\]

Fix the known incident vector `ξ∈C²`, one of the named branches `negative_imag` or `positive_imag`, its normalized eigenvector/eigenbra `χ`, and a finite integer `n≥0`. The response is the explicitly adopted **lens_area_norm_v1**, without output normalization. Write

\[
n=3m+j,\quad j\in\{0,1,2\},\qquad
h_n=(r_s q_s^2c_s^2)^m(1,q_s,q_s^2c_s)_j,
\]

\[
q_s=e^{-.423},\quad r_s=e^{.577},\quad c_s=1-.618=.382,
\qquad
v=(\chi^\dagger\xi)b_\chi^n h_n f_j\in\mathbb C^3.
\]

The subscripted `r_s` is a fixed transfer coefficient, not the lens radius `r`. Each Fourier vector `f_j` has unit norm. All fixed data are absorbed into `v`, giving the exact map

\[
\boxed{H(r,d)=\Omega_0(r,d)=G\!\left(\arccos\frac{d}{2r}\right)v.}
\tag{1}
\]

Changing the incident vector, branch, count, or normalizing the output would be a different identifiability problem. None is varied to fit a lens here. The real-arithmetic statements below concern the defined mathematical formula; successful binary64 execution has a narrower domain.

## 2. Scale invariance and the surviving ratio

**EXACT THEOREM.** For every `(r,d)∈D` and every `α>0`,

\[
H(\alpha r,\alpha d)=H(r,d).
\tag{2}
\]

**Proof.** Positive common scaling preserves `r>0` and `0≤d≤2r`, and

\[
\frac{\alpha d}{2\alpha r}=\frac d{2r}.
\]

It therefore preserves `θ`, `I`, `G`, and (since the remaining factors are fixed) `Ω₀`. This includes both endpoints. ∎

Define `q=d/r∈[0,2]`, or equivalently `s=d/(2r)∈[0,1]`. The factorization is

\[
(r,d)\longmapsto q\longmapsto\theta=\arccos(q/2)
\longmapsto I(\theta)\longmapsto G(\theta)v.
\tag{3}
\]

Thus the only candidate geometric information is the **dimensionless separation-to-radius ratio**. Section 3 proves that no further shape information is lost when `v≠0`. When `v=0`, even this information is lost.

For reference, the same normalized area written directly in terms of the ratio is

\[
J(q)=\frac{2\arccos(q/2)-q\sqrt{1-q^2/4}}{\pi},\qquad
J'(q)=-\frac{\sqrt{4-q^2}}{\pi}\quad(0<q<2).
\tag{4}
\]

This derivative is a **DERIVED IDENTITY**, not an assigned physical response law beyond the existing adoption.

## 3. Strict monotonicity and inversion

**EXACT THEOREM.** Both `I` and `G` are continuous strictly increasing bijections from `[0,π/2]` onto `[0,1]`.

**Proof.** Direct differentiation gives

\[
I'(\theta)=\frac{2-2\cos2\theta}{\pi}
=\frac{4\sin^2\theta}{\pi}.
\]

The derivative is positive for `0<θ≤π/2` and zero only at `θ=0`. To prove strict monotonicity on the *closed* interval, take `0≤a<b≤π/2`:

\[
I(b)-I(a)=\int_a^b\frac{4\sin^2 t}{\pi}\,dt>0.
\]

The integral is positive even when `a=0`, since its integrand is positive on a nonempty interior interval. Also `I(0)=0`, `I(π/2)=1`. Continuity and strict monotonicity give the claimed bijection. Taking the nonnegative square root preserves continuity, endpoints and strict order, proving the statement for `G`. ∎

**EXACT THEOREM.** For fixed known `v≠0`, an attainable output `w=Ω₀` uniquely recovers `G`, `I`, `θ` and `d/r`.

**Proof and inverse.** An attainable output has the form `w=t v` for a unique real `t∈[0,1]`. With the usual Hermitian inner product,

\[
t=\frac{v^\dagger w}{\|v\|^2}
=\frac{\|w\|}{\|v\|},\qquad
\|v\|=|\chi^\dagger\xi|h_n.
\]

The second equality is valid here because `t` is nonnegative; arbitrary complex collinearity would not suffice. Consequently

\[
\boxed{\theta=I^{-1}(t^2),\qquad \frac dr=2\cos(I^{-1}(t^2)).}
\tag{5}
\]

`I⁻¹` is the uniquely defined inverse of the strictly increasing real function. No elementary closed form or fitted inverse is required. ∎

The four requested recoverability statements are different:

| Quantity | From attainable `Ω₀` with fixed known `v≠0` |
|---|---|
| `θ` | **Yes**, uniquely, including both endpoints. |
| `d/r` | **Yes**, uniquely; a complete invariant of positive common scaling. |
| `d` | **Generally no.** If the recovered ratio is positive, every `d>0` occurs in the same fibre with `r=d/q`. At the coincident-circle endpoint `Ω₀=v`, one uniquely knows **d=0**. |
| `r` | **No, at every output**, including coincidence and tangency. Every positive radius is compatible with that output. |

When `v=0`, the output is always zero and none of these four quantities is identifiable from it. In particular zero output then does not identify tangency or coincidence.

## 4. Complete fibre classification

**EXACT THEOREM.** If `v≠0`, the attainable set is the closed real line segment

\[
H(\mathcal D)=\{tv:0\le t\le1\}\subset\mathbb C^3.
\tag{6}
\]

For any `w=tv` in this segment, put

\[
q_t=2\cos(I^{-1}(t^2)).
\]

Then the entire fibre is

\[
\boxed{H^{-1}(w)=\{(r,q_t r):r>0\}.}
\tag{7}
\]

Every `w` outside the segment has empty fibre. If `v=0`, the zero fibre is all of `D`, and every nonzero fibre is empty.

**Proof.** The gain ranges over exactly `[0,1]`, proving (6). For `v≠0`, equality `H(r,d)=tv` implies `G(θ)=t`, because at least one component of `v` is nonzero. Strict injectivity of `G` then forces exactly `d/r=q_t`. Conversely every pair `(r,q_t r)` lies in `D` and has that output. If `v=0`, (1) is the constant zero map. ∎

In particular, if `(r₀,d₀)` is any representative of a nonempty fibre with `v≠0`,

\[
H^{-1}(H(r_0,d_0))
=\{(\alpha r_0,\alpha d_0):\alpha>0\}.
\tag{8}
\]

Thus the proposed **positive scaling ray is exactly the whole ordinary fibre**, not merely a subset. No second shape ratio is hidden in that fibre. The excluded point `(0,0)` never belongs to it.

| Output, assuming `v≠0` | Lens shape | Exact fibre |
|---|---|---|
| `w=tv`, `0<t<1` | Proper overlap, `0<d<2r` | `{(r,q_t r):r>0}`, `0<q_t<2` |
| `w=v`, `t=1` | Coincident circles, `d=0`, `θ=π/2` | `{(r,0):r>0}` |
| `w=0`, `t=0` | External tangency, `d=2r`, `θ=0` | `{(r,2r):r>0}` |
| Outside the segment | Unattainable with these fixed inputs | Empty |

Equivalently, for `v≠0` the quotient of the admissible lens-pair domain by positive common scaling is represented without further identification by `q∈[0,2]`. This is an information statement about (1), not an adopted geometric host.

## 5. All exact zero-output routes

First verify the fixed transfer factors rather than assuming they are nonzero.

**DERIVED IDENTITY / EXACT THEOREM.** In the current definitions the helicity matrix is

\[
B_s=\operatorname{diag}(e^{-i\alpha_B},e^{i\alpha_B})
\begin{pmatrix}\cos\beta&-i\sin\beta\\-i\sin\beta&\cos\beta\end{pmatrix},
\quad \alpha_B=2\pi(.244),\quad\beta=\pi(.244).
\]

Both factors are unitary with determinant one, so `B_s` is unitary with determinant one. Its trace is `2τ`, where `τ=cosα_B cosβ`; hence its two eigenvalues are

\[
b_\pm=\tau\pm i\sqrt{1-\tau^2},\qquad |b_\pm|=1.
\tag{9}
\]

Because `0<β<π/2`, `|τ|≤cosβ<1`. The two named eigenvalues are distinct and nonzero. Therefore `b_χⁿ≠0` for either branch and every finite `n≥0`; in particular `b_χ⁰=1`.

The transfer gains satisfy

\[
q_s>0,\qquad r_s>0,\qquad c_s=\frac{191}{500}>0,
\]

\[
D_s=r_s q_s^2c_s^2=e^{-269/1000}\left(\frac{191}{500}\right)^2>0,
\qquad h_n=D_s^m(1,q_s,q_s^2c_s)_j>0.
\tag{10}
\]

This covers all three residues of `n` modulo 3; `h₀=1`. Each `f_j` has three entries of magnitude `1/√3`, so it is never the zero vector. There is **no branch-specific or finite-count-specific zero factor**. Although `D_s<1` and `h_n→0` as the count tends to infinity, an infinite-count limit is not an admitted finite count and does not create another exact zero route.

Combining these facts with strict monotonicity yields the complete criterion

\[
\boxed{\Omega_0(r,d)=0\quad\Longleftrightarrow\quad
d=2r\ \text{or}\ \chi^\dagger\xi=0.}
\tag{11}
\]

The routes can overlap. `ξ=0` is included in the second route but is not its only case. For normalized `χ=(a,b)^T`,

\[
\xi_\perp=\begin{pmatrix}-\overline b\\\overline a\end{pmatrix},\qquad
\chi^\dagger\xi_\perp=-\overline a\,\overline b+\overline b\,\overline a=0,
\qquad\|\xi_\perp\|=1.
\tag{12}
\]

All incident vectors with zero extraction form exactly the one-complex-dimensional subspace `kerχ†=C ξ_perp`. Thus a **nonzero incident vector can erase every lens ratio** for the chosen branch. The other normalized eigenmode of `B_s` is also orthogonal to `χ`, because `B_s` is normal and its eigenvalues are distinct. No special choice of transfer count restores that discarded component in the named extraction.

This proves the classification for the fixed adopted parameters. It does not vary `.618` or any other SRG constant to create extra exceptional models.

## 6. Information loss and the top-layer boundary

**EXACT THEOREM.** With `χ†ξ≠0`, two admissible lens pairs give the same canonical initial state **if and only if** they have the same shape ratio:

\[
H(r_1,d_1)=H(r_2,d_2)
\quad\Longleftrightarrow\quad
\frac{d_1}{r_1}=\frac{d_2}{r_2}
\quad\Longleftrightarrow\quad
(r_2,d_2)=\alpha(r_1,d_1)\text{ for some }\alpha>0.
\tag{13}
\]

The last implication uses `α=r₂/r₁`, which is positive. In particular **same shape ratio plus arbitrary positive common scale gives exactly the same canonical initial state**. No function of that state alone can distinguish these radii: it receives an identical input for every point on the ray. With orthogonal incident data, the lost information is larger: all of `D` collapses to one output.

The native response receipt stores `θ`, incident data, branch and transfer count, but not an absolute input radius or separation (`srg.HandoffResult`, lines134–151). This is consistent with the result; it is not an extra scale channel. Source metadata recorded elsewhere would be additional information, outside recovery from `Ω₀` alone.

**INFORMATION-INTERFACE RESULT.** A proposed top layer whose absolute radius can vary independently would **not be identifiable through this initializer alone**. Its differently scaled admissible lens representatives are indistinguishable at this interface. This result neither selects a historical top circle nor proves that a future geometric or physical model cannot possess a radius, an external calibration or a different information channel. It only states what the present adopted map preserves and forgets. No extra variable, coupling or calibration is introduced to repair the loss.

**PHYSICAL INTERPRETATION:** none established. **STRUCTURAL ANALOGY:** none needed for the proof. **OPEN QUESTION:** any independent attachment or physical role of these lens parameters remains outside TL1.

## 7. Bounded verification and preservation

**NUMERICAL EVIDENCE.** [verify_tl1.py](project-source/research/TL1_lens_srg_identifiability_20261006/verify_tl1.py) uses a single representative fixed choice: `ξ=(1+2i,−1+i)`, branch `negative_imag`, transfer count `n=5`. The universal statements above are analytic and cover both named branches and every finite admitted count; the finite checks do not supply that quantification.

The bounded checks are:

- Four native scale-related pairs `(1,.75)`, `(8,6)`, `(.125,.09375)` and `(17,12.75)`: identical binary64 output in these exactly represented ratio fixtures.
- Three further common scales `1/10`, `√2`, `1000`, evaluated independently at 100-digit precision.
- Interior ratios `1/4`, `3/4`, `3/2`: bracket inversion of `I` recovers each ratio; the largest recorded absolute recovery error is approximately **1.43×10⁻¹⁰¹**. Native outputs differ from the independently evaluated formula by at most **1.75×10⁻¹⁷** in componentwise absolute error on these fixtures.
- Coincidence `(1,0)` and `(7,0)`: gain one and identical output. Tangency `(1,2)` and `(7,14)`: zero output.
- A zero incident vector and the admitted nonzero orthogonal incident construction (12): zero extraction. The symbolic cancellation proves exact orthogonality; the numerical result only checks the selected implementation fixture.

**Verification result: 24/24 PASS** — 7 symbolic identity checks, 8 bounded numerical check groups and 9 preservation checks. Full inputs, residuals, source hashes and counts are in [TL1_RESULTS.json](project-source/research/TL1_lens_srg_identifiability_20261006/TL1_RESULTS.json). No earlier checkpoint or paper test counts were rerun or combined.

**Exact mathematics versus finite precision.** Scale invariance for every positive real `α` is not a promise of bitwise invariance under every machine multiplication. Floating scaling, division and `acos` can round, merge inputs, or leave the accepted numeric domain. Guarded nonzero underflow/subnormal intermediates raise precision errors, and a finite transfer gain may become unevaluable despite being mathematically positive. Conversely compensated complex dot products can round to zero through cancellation; a computed zero alone is not an exact certificate for (11). These are already documented numerical limitations. The theorem concerns exact fibres; it does not claim an injective finite-precision inverse for all inputs.

**SOURCE FACT / preservation PASS.** HEAD remains **82cab10cbe550f58c43163fb8b05fabdad1b05ae**. Git status and index fingerprints are unchanged. Complete path/content fingerprints agree for the authoritative repository, `kernel_TO`, `kernel_torment`, the separate sibling `kernel_physics`, and the pre-existing external `research` and `reconstruction` trees. These six inventories cover **16,015 predecessor/source files**; only the new TL1 output directory is excluded. TL0 and the parked research/papers remain untouched. No kernel, UI, paper, fixture, predecessor artifact, commit or remote state was modified.

## 8. Final answers

1. **What survives?** With nonzero fixed extraction, exactly `d/r`, equivalently `θ`, normalized lens area `I`, or gain `G`. With zero extraction, no lens information survives.
2. **What is lost?** Positive common scale, hence every absolute radius. Absolute separation is also lost except that coincidence identifies the special value `d=0`.
3. **Exact fibres?** With nonzero extraction: one positive scaling ray for every attainable output, including the coincidence and tangency rays; empty fibres off the segment. With zero extraction: the whole admissible domain over zero and empty fibres elsewhere.
4. **What produces zero?** Exactly tangency `d=2r` or `χ†ξ=0`, including nonzero orthogonal incidents. No finite transfer count or named eigenvalue contributes an additional exact zero.
5. **Can absolute radius be recovered?** No, for any output from this interface alone.
6. **What follows for a future top layer?** Any independent absolute-radius distinction is invisible to the present initializer. This is an information-interface limitation, not a physical no-go theorem or a top-circle adoption.
7. **ONE justified next derivation:** determine the conditioning of the recovered shape ratio under small output error, with fixed nonzero incident/extraction data, especially near tangency. This would distinguish exact injectivity from practical numerical recoverability without adding scale, changing the initializer or choosing a top layer. That follow-up is not begun here.

**STOP: TL1 complete. `TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED`.**
