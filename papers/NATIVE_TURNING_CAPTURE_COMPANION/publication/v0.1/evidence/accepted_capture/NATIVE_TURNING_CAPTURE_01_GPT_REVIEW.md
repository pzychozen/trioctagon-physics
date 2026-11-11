# NATIVE_TURNING_CAPTURE_01 — GPT scientific review and acceptance

**Date:** 10 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Investigation:** Codex  
**Disposition:** **ACCEPTED at the stated scope. No mathematical correction required.**  
**Status:** Project-internal scientific acceptance of the investigation, not external peer review, formal proof-assistant verification, manuscript approval or publication.

## 1. Accepted conclusion

For the original native map, the unchanged exact coefficients

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad\lambda=\frac1{300},\qquad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),
\]

and the original entrance

\[
\Omega_0=(1+i,1+i,1-2i),
\]

the connected exact certificate proves

\[
F^{50}(\Omega_0)\in\operatorname{int}\mathcal D,
\]

where the **inherited** coherent domain has component moduli in [0.9,1.1] and ordinary phases contained in a single interval of width at most pi/12. Therefore the already published coherent-relaxation theorem applies from update 50 onward:

\[
F^n(\Omega_0)\longrightarrow e^{i\theta_\infty}r_*.
\]

The same trajectory has the previously established strict positive early collective turn. The limiting amplitude profile is the inherited positive, pairwise unequal profile unique in [0.9,1.1]^3, not a new equilibrium construction. Its common phase depends on the initial condition.

At the same fixed coefficients, some open neighborhood of the original entrance also has strict positive early turning and membership in the coherent domain at update 50, hence the inherited convergence. No explicit neighborhood radius is accepted or claimed.

**Use “certified inside by update 50” or “strict inclusion at update 50.”** This is not a certified first-entry index. The numerical suggestion of entry at update 41 remains exploratory. The submission already states this distinction; no correction is required.

## 2. What is new, and the prior-work boundary

The new content is the finite original-seed connection and its qualitative initial-condition corollary. Early turning, domain invariance, coherent convergence, the fixed amplitude profile, and the method of combining finite entry with an invariant convergence theorem are inherited.

I reviewed the submitted bounded prior-work comparison and cross-checked the controlling original theorem and relevant exclusions in the retained sources. In particular:

- `sources/collective/main.tex`, the abstract and `sec:overview`, explicitly leave capture of the turning entrance unproved; `sec:domain` and `thm:convergence` assume admission to the coherent domain.
- `sources/returns/main.tex`, the coherent-relaxation and M3 comparisons, distinguishes finite-return restrictions from forward capture. Its M3 example has different coefficients, entrance, target and limiting two-cycle.
- `sources/NCM/NCM_DUAL_02_REPORT.md`, the prior-results table, retains the same missing turn-to-capture connection.
- The native-potential domain theorem assumes the coherent domain; local response, reconstruction and passive-observation results do not supply this entrance certificate.
- The reciprocal and causal-transport candidates evolve extended systems; their activity results are not native-only capture results.

The submitted `PRIOR_WORK_COMPARISON.md` covers the wider targeted catalog, atlas and local native successors. Its **DISTINCT_GAP** finding is accepted as a bounded project-source comparison, not as an exhaustive search of every unindexed archive or a worldwide priority claim. Its administrative classification must not be counted as a new mathematical theorem.

## 3. Certificate mathematics

### 3.1 Frozen map and connected finite chain

The proof and verifier retain the simultaneous native prestage, then simultaneous harmonic-three synchronization. There is no sequential phase update, amplitude normalization, replacement seed, parameter fitting, observer feedback or added state.

The certificate starts with exact singleton boxes for the original six real coordinates. Its 51 state boxes and 50 step records form one connected enclosure chain. The checker recomputes each prestage from the preceding supplied state box and each next state from the checked prestage and phase rotation. It does not restart from exploratory floating values.

The computed enclosure tests prove inclusion of the exact trajectory by induction. Padding in the generator only widens boxes; acceptance rests on the independently evaluated containment tests, not on the padding rule or high precision alone.

### 3.2 Regularity and phase calculation

For nonzero prestages the identity

\[
\sin\bigl(3(\arg v_j-\arg v_i)\bigr)
=\frac{\operatorname{Im}((v_j\overline{v_i})^3)}{|v_j|^3|v_i|^3}
\]

agrees with the native phase rule independently of argument branch cuts. The checker verifies every positive square-root witness by exact squared inequalities. All 150 prestage moduli are strictly above 87/100. Thus no zero-prestage convention is bypassed on the certified finite path.

The generator uses directed dyadic interval arithmetic at denominator 2^512. The submitted independent checker uses exact fractions, combined prestage coefficients, the expanded imaginary-cube expression, and midpoint trigonometric estimates rather than importing the generator's arithmetic.

### 3.3 Trigonometric errors

I checked the Taylor orders and remainder bounds. The sine polynomial ends at degree 47 and also equals the degree-48 Taylor polynomial because that coefficient vanishes. The cosine polynomial ends at degree 48 and also equals the degree-49 Taylor polynomial. On |delta| < 1/100 the stated remainders `(1/100)^49/49!` and `(1/100)^50/50!` are valid.

The checker's midpoint-radius extension uses |sin'| <= 1 and |cos'| = |sin| <= |x|, bounding the latter throughout each argument interval. These estimates justify its exact rational sine and cosine enclosures. All supplied boxes contain the independently calculated bounds.

### 3.4 Terminal admission

Exact rational squaring certifies the strict amplitude intervals

| Channel | Lower bound | Upper bound |
|---|---:|---:|
| A | 0.997219 | 0.997220 |
| B | 0.997622 | 0.997623 |
| C | 0.996782 | 0.996783 |

The common diagnostic multiplier `987395 - 158274 i` places every terminal component in the same strict cone `Re(w) > 8 |Im(w)|`. The checker confirms positive cone margins with conservative integer lower bounds 492851, 492769 and 492356 respectively. This rotation is a diagnostic only; it is never applied as an extra dynamical update.

Consequently all ordinary phases fit inside an interval of width less than

\[
2\arctan(1/8)<1/4<\pi/12.
\]

The amplitude and cone tests establish strict inclusion in the original domain. They do not identify phases modulo 2pi/3.

## 4. Convergence and robustness

The inherited estimates are correctly reindexed with the integer tail counter `t = n - 50`, not treated as physical time. With

\[
c=1-\frac{3\sqrt2}{200},\qquad\beta=\frac{8571}{10000},
\]

the stated explicit bound is

\[
\|\Omega_{50+t}-e^{i\theta_\infty}r_*\|_\infty
\le \frac15\beta^t+
\frac{107701}{12800000}\frac{c^{2t}-\beta^t}{c^2-\beta}
+\frac{11}{40}c^t.
\]

I checked the coefficients against `eq:forcing`, `eq:radialbound`, `eq:fullbound` and `eq:beta` in the inherited source. Here `c^2 > beta`; the bound tends to zero. The inherited positive residual amplitude spread and decay of C, W and Gamma follow. The number 0.005270 remains an upper bound, not the limiting spread.

The neighborhood argument is valid: nonzero prestages on a finite orbit give smooth local representations of every relevant update; the early turning functional is continuous and strictly positive; and the terminal annulus/cone inequalities define an open set. Intersecting these conditions with the inverse image under F^50 yields an open set containing the exact entrance. The limiting common phase may vary within it. This establishes qualitative robustness at the fixed coefficients, not a numerical tolerance or a full basin classification.

## 5. Actual reviewer checks and their scope

The submitted code was read before execution. I reproduced its certificate validation and five damaged-certificate controls in the reviewer runtime, preserving all submitted files.

| Item | Reviewer outcome |
|---|---|
| Incoming archive checksum, CRC, safe unique names and extracted bytes | PASS, 112 members |
| Self-excluding review manifest | PASS, 111 entries |
| External final-delivery audit against actual member bytes | PASS, 112 entries |
| Retained source identities, including computed Git blob IDs where supplied | PASS, 59 entries |
| Claim ledger source/proof locators and hashes | PASS, 39 locators across 16 ledger records |
| Original commissioned packet and its extracted input members | Unchanged; 12 members |
| Exact certificate replay | PASS, 50 links and 150 positive prestages |
| Stable checker result values compared with Windows return | All match |
| Five submitted damaged-certificate controls | All rejected with the same recorded reasons |
| Exact rational constants in the shifted convergence bound | PASS |
| Submitted evidence after replay | Unchanged |

**Environment disclosure:** Codex's recorded scientific run used Windows Python 3.11.15 in `torment`. The reviewer replay used Linux Python 3.13.5. In memory only, the checker’s single conda-name guard was replaced by a check that Python assertion optimization is disabled. All mathematical functions and assertions are unchanged; its main-program output writer was not executed. The original checker bytes remain intact. This is a corroborating replay of the submitted independent checker, not a third independently implemented checker or a Windows rerun. The adapter, exact one-line adaptation, actual environment and results are retained under `reviewer/`.

The current certificate checker was replayed; the generator, exploratory trajectory and historical scientific suites were not rerun. No remote publication audit or Git operation was performed. Packaging records are integrity checks, not scientific theorem counts. Ordinary Python execution and review are not formal proof-assistant certification.

## 6. Limits retained and closeout

No change is required to the map, certificate, checker arithmetic, finite-entry proof, convergence application or qualitative neighborhood argument.

This result does not establish earliest entry, an explicit initial-condition radius, global attraction, a new parameter regime, uniqueness of the amplitude profile outside the inherited cube, or finitely many remaining diminishing direction changes. The graph-off comparison in the old paper is not an ablation proving a sole cause of this full-map capture. No physical gravity, magnetism, force, motion, clock, receiver or spatial transport correspondence is inferred.

**Research disposition:** this exact finite-entry gap is closed and should not be recommissioned. The old turning and convergence theorems remain inherited rather than relabeled as new. For documentation, a short companion note or clearly scoped addendum to the collective-turning paper would fit the result better than another broad model-extension paper; any earlier published edition should remain unchanged. That is a recommendation, not a new manuscript commission or publication authorization.

## 7. Controlling submitted identities

- Review ZIP: `c9fd8d7bb366dd882a9f7457e943345f06fba7b0e335a161aa7e66435af1ca6e`.
- Codex proof: `7f57b3e87272a6be822ed8e1f211e62de56d6556224a136193347b1108da8f72`.
- Certificate: `1244cafe2e8aa6b646aa25b4784102f4ce085c90464e5087b3cf01bde43782a1`.
- Submitted independent checker: `f7b01f38bd897399812c1adb748dd88de6d90a08da7d77136267350d49c6b32e`.
- Primary inherited source: `40b6ca84ca136453b045386e2dead012fc8fcd7984b845d159ae6d6c8a6c2292`; Git blob `de060bd217261af9bc87a52f0a79fe6fa4f6495d`.

All paths in this review refer to the acceptance package. Original Codex evidence is under `submitted/`, and original incoming archives and standalone returns are under `received/`. No historical document is silently edited by this acceptance.
