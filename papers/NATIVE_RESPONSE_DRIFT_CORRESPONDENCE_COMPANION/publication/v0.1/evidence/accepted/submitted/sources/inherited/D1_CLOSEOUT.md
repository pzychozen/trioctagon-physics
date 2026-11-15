# D1 scientific closeout — native chiral phase drift

**Date:** 6 October 2026  
**Disposition:** PASS_WITH_QUALIFICATIONS for the mathematical result.  
**Scope:** Review and written explanation of the completed D0–D1 calculation. No D2, new model, kernel modification, paper revision, or publication is authorized by this note.

## 1. The question and its answer

D0 established a nonzero chiral reference state and a locally isolated continuation problem. D1 asked whether slightly unequal native coefficients make that branch advance by a common complex phase, and whether the resulting rate persists in the mathematical small-step limit.

**The answer is yes for the specified local branch.** D1 gives an explicit nonzero cubic coefficient, not a frequency fitted to a plotted trajectory. The analytic result and finite-root evidence are distinct parts of that answer.

The parameter family is

\[
(\epsilon,g,\lambda)=h(1,1/6,1/30),\qquad
k=(1-\eta,1,1+\eta),
\]

with reference

\[
z^*_{+,j}=2^{-1/2}e^{2\pi i j/3},\quad j=0,1,2.
\]

The phase-gauged unknown retains all six real state coordinates and the rate \(\nu\). For positive \(h\), the equations are

\[
F_h(z;k)=e^{ih\nu}z,\qquad \omega=h\nu.
\]

At \(h=0\), D0 defines their analytically desingularized generator equations, rather than substituting into an undefined numerical quotient. No physical clock was added.

**Source:** D1 §§1–2; D0 §§7–8.

## 2. The exact result

D1's normalization is

\[
\nu_+(h,\eta)=2c_+(h)\eta^3+O(\eta^5),
\qquad
c_+(h)=\frac{\sqrt3(33h^2-240h+688)}{6(1-3h)^3}.
\]

Equivalently,

\[
\boxed{\nu_+(h,\eta)=
\frac{\sqrt3(33h^2-240h+688)}{3(1-3h)^3}\eta^3+O(\eta^5).}
\]

The distinction between \(c_+\) and the displayed coefficient of \(\eta^3\) matters: the latter is **twice** \(c_+\) because the selected oriented Vandermonde equals two.

The coefficient is positive for \(0\le h\le1/4\). At the generator endpoint,

\[
c_+(0)=\frac{344\sqrt3}{3},\qquad
\nu_+(0,\eta)=\frac{688\sqrt3}{3}\eta^3+O(\eta^5).
\]

Thus the rate is not solely a finite-step splitting effect. At positive steps,

\[
\omega_+(h,\eta)=
\frac{688\sqrt3}{3}h\eta^3+1984\sqrt3\,h^2\eta^3
+O(h^3\eta^3+h\eta^5).
\]

The per-step angle tends to zero with \(h\), as it should for a finite limiting rate. The limiting statement concerns the derived generator family, not physical elapsed time.

The coefficient formulas are local analytic statements in \(\eta\). They do not assign the same behavior to every chiral state or every parameter tuple. The singular value \(h=1/3\) is outside the selected interval and cannot be approached using this result as though isolation remained unchanged.

**Source:** D1 §§3–4.

## 3. Why the leading term is cubic

D0 proves that the rate at a fixed chirality label is alternating under coefficient permutations, with the state, labels and gauge transformed consistently. On the fixed-mean coefficient plane it factors as

\[
\nu_m(h,x)=
(x_0-x_1)(x_1-x_2)(x_2-x_0)\,S_m(h,x),
\]

where the quotient is analytic and symmetric. The symmetric quotient has no linear term on that plane. This permits a cubic leading rate and excludes the quartic term. It does not by itself make the cubic coefficient nonzero.

**D1 supplies that missing coefficient.** Along \(x=\eta(-1,0,1)\), the oriented product is \(2\eta^3\), and the additional fixed-label symmetry makes the rate odd in \(\eta\).

Conjugation reverses the rate and chirality together. Pure site reflection carries the coefficients, changes the chirality label and preserves the rate. Conjugation combined with reflection reverses the rate at fixed label. The validated two-equal-coefficient control has exactly zero rate because local uniqueness and this symmetry apply; a tiny computed residual is not interpreted as drift.

**Source:** D0 §8; D1 §§3,7.

## 4. What drives the common phase

The following is an algebraic rearrangement of D1's generator identity, not a new dynamical assumption. Write a generator relative equilibrium as \(z_i=r_i e^{i\theta_i}\). Pairing the real onsite/coupling contribution with \(z\) gives a real number. Therefore

\[
\nu\sum_i r_i^2=
\frac1{30}\sum_i r_i^2\sum_{j\ne i}
\sin3(\theta_j-\theta_i).
\]

Pairing opposite orientations of each edge rewrites this as

\[
\nu\sum_i r_i^2=
\frac1{30}\sum_{i<j}(r_i^2-r_j^2)
\sin3(\theta_j-\theta_i).
\]

The unweighted sum of pairwise phase kicks cancels, but the amplitude-weighted sum need not. On the continued branch, both amplitudes and phase differences adjust. D1 solves those adjustments together and finds the nonzero net rate; the identity alone would not prove the existence of that branch or its drift.

For the native finite-step map the necessary consistency identity is instead

\[
\sum_i |z_i|^2\sin(h\nu-\delta_i)=0,
\]

with \(\delta_i\) evaluated at the actual prestage. The generator identity must not replace this finite-step condition.

**Source:** D1 §§2–3,7.

## 5. Why the result is more than a linear-response analogy

GR1–GR2 established non-reversible response and sector-dependent spectra on specified backgrounds. D1 now establishes actual **relative equilibria**: the full state advances on a common-phase group orbit rather than remaining fixed.

**Reviewer-derived consequence, distinct from the report's explicit theorem list:** the generator cannot, on a domain containing these nonzero-rate states, simply be negative gradient motion of a single common-phase-invariant potential in a positive-definite metric.

Indeed, suppose \(X=-\operatorname{grad}_g V\), with \(g\) positive definite and \(V(e^{i\alpha}z)=V(z)\). At a relative equilibrium \(X=i\nu z\),

\[
dV(X)=\nu\,dV(iz)=0,
\]

whereas gradient motion requires

\[
dV(X)=-g(\operatorname{grad}_gV,\operatorname{grad}_gV).
\]

Thus \(X=0\), inconsistent with \(z\ne0\) and \(\nu\ne0\). This rules out that specified gradient description. It does not classify every possible non-gradient, driven, Hamiltonian, or effective description, and does not identify a physical current.

## 6. What an invariant observer sees

At a relative equilibrium,

\[
z^+=e^{i\omega}z
\quad\Longrightarrow\quad
z^+(z^+)^\dagger=zz^\dagger.
\]

Every component intensity and every already defined common-phase-invariant chirality readout is therefore unchanged. The full state moves; its coherence quotient is stationary.

This is an exact state-versus-readout distinction. It does not say that every possible observable is insensitive to the phase, nor that common phase has been declared an unobservable physical gauge. It also does not establish hidden spatial dimensions or a bulk/brane interpretation.

The reference is a saddle. D1 has not certified attraction of the continued relative equilibria and did not integrate trajectories. Common complex-phase drift is not automatically rigid spatial rotation of the Tri-Octagon, the measurement cylinder, or a physical core.

**Source:** D1 §§7,9.

## 7. Analytic proof and finite-root certification have different domains

The analytic coefficient calculation is exact in the parameter \(h\), with D0's local branch framework applying on \(0\le h\le1/4\).

D1 reports finite-root validation at only

\[
h\in\{0,1/10,1/100,1/1000\},\qquad
\eta\in\{\pm1/1000,\pm1/2000,\pm1/4000\}.
\]

The larger proposed eta ladder failed a sufficient contraction-bound test at the fixed subdivision budget. Reducing the entire ladder, without changing the hatted coefficients or switching branches, respects the work order. That failure was not evidence that the larger branch did not exist.

The report describes 256 parameter boxes and 260 endpoint boxes, with contraction inequalities, endpoint-overlap inclusions and connection to the exact D0 reference. Negative eta and conjugate branches use the stated exact symmetries, with additional fixed-root checks. These are stronger claims than small Newton residuals alone; they are the report's validated-numerical evidence.

The finite-point normalized rate differs noticeably from the cubic coefficient. D1 correctly distinguishes the analytic \(O(\eta^2)\) normalized-rate remainder from finite-point remainder enclosures. It does not claim an explicit uniform numerical remainder bound over every intervening eta.

**Source:** D1 §§5–6.

## 8. Independent GPT review performed in this session

The attached D1 report was available. Its original `verify_d1.py` and `D1_RESULTS.json` were not supplied in this conversation. Consequently this review does **not** claim to replay the original 133-check suite or audit its interval implementation and certificates.

Two independent bounded checks were performed from the report's equations:

### Exact symbolic substitution

A new checker represents series through degree three in eta with exact coefficients in \(\mathbb Q(\sqrt3)(h)\), keeping real and imaginary parts separate. It implements the original amplitude/coupling stage and the original synchronizer at its actual prestage, then substitutes the report's complete state and rate jets.

All six real native residual rows and the gauge vanish through degree three as rational identities in h. The reported rate normalization, generator coefficient and first h derivative agree. This is an independent verification of the displayed jet, **not** an independent derivation of the jet coefficients from scratch. With D0's isolated analytic branch, this substitution provides substantive corroboration of the coefficient.

File: `check_d1_exact_jet.py`; results: `exact_jet_check.json`.

### Independent midpoint reproduction

At 110 decimal digits, a separate direct implementation of the original physical-complex equations and their h-zero generator was used to solve the twelve positive-eta table fixtures. The reported jet initialized the solves. Every reported rounded rate agrees; the largest full-equation residual was below \(3.38\times10^{-105}\).

These are **unvalidated numerical comparisons**. They are not interval proofs, independent continuation certificates or a replacement for Codex's original certificate artifacts.

File: `check_d1_midpoints.py`; results: `midpoint_check.json`.

These reviewer checks are kept separate from D1's 133 checks, D0's 64 checks and every earlier checkpoint count.

## 9. Disposition and next boundary

**The analytic core of D1 passes this review.** The source report's `PASS_WITH_QUALIFICATIONS` is appropriate: nonzero local common-phase drift and its surviving generator coefficient are established, while stability, physical meaning, broader parameter coverage and publication remain separate questions.

The report's interval proof structure is coherent on inspection; full implementation-level validation of those certificates requires the original verifier and results. No claim that the complete certificate package was independently replayed is made here.

This written closeout explains the completed result. It does not create a new paper or authorize changes to NRG, Paper G, the kernel or the UI. The outstanding TL0–TL4 synthesis remains a separate unfinished write-up. There is no automatic D2, broader-ring search, physical reinterpretation or social-media publication.

## Source identity and reproduction

Primary uploaded report: `D1_NATIVE_CHIRAL_PHASE_DRIFT.md`  
SHA-256: `7fa8bb8f61dab09c4f94f0a2227300f94bede4a7651241679e35375d0b8c0737`

The companion D0 report and D1 work order were read for scope. The authoritative Windows checkout and original protected-file inventories were not accessed or reverified in this review.

Reviewer tools: Python, SymPy 1.14.0, mpmath 1.3.0. The two review commands, usable from this supplement directory in an environment containing those packages, are:

```text
python -B check_d1_exact_jet.py
python -B check_d1_midpoints.py
```

They write only their own review JSON files. They do not import or alter the native kernel or original D0/D1 artifacts.
