# D1 — Native chiral-branch phase drift
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

6 October 2026 · External read-only mathematical research

**D1 = PASS_WITH_QUALIFICATIONS.** The D0 positive-chirality branch has nonzero common complex-phase drift under weak three-distinct coefficients. Its cubic rate is exactly

\[
 \boxed{c_+(h)=\frac{\sqrt3(33h^2-240h+688)}{6(1-3h)^3}},\qquad
 \boxed{c_+(0)=\frac{344\sqrt3}{3}>0}.
\]

For the specified direction \(\kappa=(-1,0,1)\),

\[
 \nu_+(h,\eta)=2c_+(h)\eta^3+O(\eta^5),\qquad \omega_+=h\nu_+.
\]

Thus the leading rate survives the mathematical small-step limit. It is not solely a finite-step splitting effect. These are exact local analytic statements about the frozen native family. No model change, physical clock, spatial rotation law, or attracting rotating state is inferred.

The finite-root verification uses the four prescribed h values and, after a documented sufficient-bound failure at the fixed subdivision budget, a uniformly tenfold smaller eta ladder: \(\pm1/1000,\pm1/2000,\pm1/4000\). Every accepted point is connected to the D0 reference by validated parameter continuation or an exact symmetry image of that continuation. The original larger ladder is not claimed to have been validated.

## 1. Frozen problem, sources, and preservation

**SOURCE DEFINITION.** The authority is `project-source/trioctagon-physics`. Actual initial HEAD was the expected `82cab10cbe550f58c43163fb8b05fabdad1b05ae`, on `main`. The index had no staged changes. Existing dirty and untracked material was recorded before research and retained. D0's report, script, and results were read from `research/D0_chiral_reference_20261006/`; no predecessor writer was rerun into its original files.

The fixed mathematical problem is the native triad, indices 0,1,2 in positive cyclic order, with

\[
 \epsilon=h,\quad g=h/6,\quad\lambda=h/30,\quad\ell=h/10,
 \qquad k=(1,1,1)+\eta(-1,0,1).
\]

The reference is \(z^*_{+,j}=2^{-1/2}e^{2\pi ij/3}\), with its conjugate as the negative-chirality reference. The gauge is exactly D0's:

\[
 \gamma(z)=\Im\langle z^*,z\rangle/\|z^*\|^2=0,
 \qquad \Re\langle z^*,z\rangle>0.
\]

The channel-mean phase is not used. The unknowns retain all six real state coordinates and the rate nu; no unstable state directions are discarded.

Source locators:

| Source | Exact role |
|---|---|
| `trioctagon-physics/kernel_physics/dynamics.py`, lines 57–112 | Arg0 convention; simultaneous harmonic-three synchronization; amplitude/coupling stage followed by synchronization; complete triad update. |
| D0 report, §§5–8 and §11 | Exact drift identities, joint symmetry conventions, twisted reference, gauge, full bordered determinant, analytic h-zero extension, cubic selection. |
| `research/D0_chiral_reference_20261006/verify_d0.py` | Prior exact border/characteristic checks and source comparison, read rather than executed. |
| `research/D0_chiral_reference_20261006/D0_RESULTS.json` | D0 64/64 evidence, source identities, and preservation record, retained separately. |
| `kernel_physics/readouts.py`, as anchored in D0 | Existing raw chirality is common-phase invariant; no new observable is defined. |

All paths in this table are relative to `project-source/`. D1's initial source hashes are retained in `D1_RESULTS.json`. The native dynamics hash is `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4`; the D0 report hash is `a84ece868b9f68713f90792b7c3a092e4829fef0861e3e630a43bcc1962f4b60`.

A fresh preservation inventory covers **16,035 existing files** in the scientific checkout, historical `kernel_TO`, production `kernel_torment`, the separate sibling `kernel_physics`, external research predecessors, and reconstruction records. Only `.git` internals and this new D1 output directory are excluded from byte inventories. HEAD, branch, index fingerprint, dirty/untracked status, source hashes, and all six root inventories are separately rechecked. No protected repository, UI, paper, fixture, historical code, predecessor research, or temporary file is modified. There is no staging, commit, push, cleanup, publication, or new interpretation lane.

## 2. Exact equations used in both calculations

Write \(A=1/\sqrt2\), \(q_j=e^{2\pi ij/3}\), and use the invertible real local coordinates

\[
 z_j=Aq_jw_j,\qquad w_j=1+u_j+iv_j.
\]

Then gamma is \(\sum_jv_j/3\), and its positivity condition is \(\sum_j(1+u_j)/3>0\). Normalizing the state is only an analytic coordinate change; no runtime normalization is added.

The exact normalized prestage is \(p=w+ha\), where

\[
 a_i=w_i\left(k_i-\frac{|w_i|^2}{2}\right)
 +\frac16\left(\sum_{j\ne i}q_jq_i^{-1}w_j-2w_i\right).
\]

Define

\[
 C_i=\frac{p_i^3}{|p_i|^3},\qquad
 d_i=\frac1{30}\sum_{j\ne i}\Im(C_j\overline C_i).
\]

The reference factors disappear from the cube since \(q_i^3=1\). The actual native kick is \(\delta_i=hd_i\), evaluated at the **actual prestage** p. For positive h the original normalized complex residual is

\[
 \frac{p_i e^{ihd_i}-w_i e^{ih\nu}}h.
\]

This is exactly the requested complete system, with three complex rows and gamma. At h zero its analytic extension is \(a_i+iw_i(d_i-\nu)\), with p=w. It is D0's \(X_k(z)-i\nu z\), expressed in local coordinates.

For stable interval evaluation at small h, multiply each complex equation by \(e^{-ihd_i}\). This gives the equivalent seven-real-variable system

\[
 G_i=a_i+w_i E_h(d_i-\nu)=0,\qquad \gamma=0,
 \qquad E_h(t)=\frac{1-e^{-iht}}h,\quad E_0(t)=it.
\]

The row multiplication is invertible throughout the domain. It changes neither the roots nor the native order of operations, and avoids subtracting two nearly equal quantities followed by division by h. The symbolic calculation uses the original exponential residual; the interval proof uses this equivalent residual; independent numerical checks use the physical complex-state native formula.

## 3. Cubic coefficient from the full seven-variable jet

**DERIVED IDENTITY / EXACT THEOREM.** Use ordinary power-series coefficients, not derivatives without factorials:

\[
 u=\eta u_1+\eta^2u_2+\eta^3u_3+O(\eta^4),\quad
 v=\eta v_1+\eta^2v_2+\eta^3v_3+O(\eta^4),
\]
\[
 \nu=\eta\nu_1+\eta^2\nu_2+\eta^3\nu_3+O(\eta^4).
\]

At each order n, substituting all previously solved coefficients produces a forcing vector \(b_n\). The new coefficient vector \(U_n=(u_n,v_n,\nu_n)\) obeys

\[
 \mathcal B_hU_n=-b_n,
\]

where the entire D0 border is retained. In these normalized coordinates its phase column is \((0,0,0,-1,-1,-1)^T\), and its gauge row is \((0,0,0,1/3,1/3,1/3)\). Its determinant remains

\[
 \det\mathcal B_h=-\frac{(3h-1)^2}{1600}.
\]

Consequently the three order equations have unique exact solutions for \(0\le h\le1/4\), including the generator endpoint.

Here are the complete state corrections. Define \(d=3h-1\) and

\[
 P=108h^3+27h^2+828h-760,\quad
 Q=54h^3-270h^2-261h+592,
\]
\[
 U=972h^5+2025h^4+12744h^3+96570h^2+132h+64568,
\]
\[
 W=972h^5-8667h^4+112212h^3-521514h^2+98412h-206440.
\]

Then

\[
 u_1=-\frac{3h+2}{d}(1,0,-1),\qquad
 v_1=\frac{\sqrt3(3h-10)}{3d}(1,-2,1),
\]
\[
 u_2=-\frac{P}{6d^3}(1,0,1)-\frac{Q}{3d^3}(0,1,0),\qquad
 v_2=-\frac{\sqrt3(3h-10)(45h-68)}{2d^3}(1,0,-1),
\]
\[
 u_3=-\frac{U}{6d^5}(1,0,-1),\qquad
 v_3=\frac{\sqrt3 W}{18d^5}(1,-2,1),
\]
\[
 \nu_1=\nu_2=0,\qquad
 \nu_3=-\frac{\sqrt3(33h^2-240h+688)}{3d^3}.
\]

The real and imaginary state components both change. Freezing amplitudes, or removing amplitude/phase mixing, would not produce this coefficient calculation.

### Exact substitution and normalization

**EXACT SYMBOLIC CHECK.** The verifier constructs the prestage polynomial, the normalized cubic unit factors using the binomial expansion of \((|p|^2)^{-3/2}\), the actual kicks, and both exponential factors, retaining all terms through degree three. After the solved state and rate coefficients are substituted back, every coefficient of all six real original residual rows and the gauge is exactly zero through that degree. All computations are exact expressions over the real h parameter and algebraic constants. No numerical fit is used to obtain nu-three.

D0's oriented Vandermonde is

\[
 V(\kappa)=(\kappa_0-\kappa_1)(\kappa_1-\kappa_2)(\kappa_2-\kappa_0)=2.
\]

Thus \(\nu_3=2c_+(h)\). Since \(\partial_\eta^3\nu(h,0)=6\nu_3\), the requested normalization is indeed

\[
 c_+(h)=\frac1{12}\partial_\eta^3\nu(h,0)=\frac{\nu_3}{2}.
\]

The analytic isolated branch exists by D0. Its alternating symmetry excludes a quartic rate term, upgrading the rate remainder to \(O(\eta^5)\), even though only state corrections through degree three are displayed. Along the chosen direction the rate is exactly odd in eta because reversing eta is the fixed-label conjugation/reflection comparison. The cubic state truncation's full residual is generally \(O(\eta^4)\), rather than identically zero at finite eta.

An independent substitution into the original transcendental physical-complex formula, at 110 decimal digits and eta values \(10^{-5},5\times10^{-6},2.5\times10^{-6}\), exhibits the expected factor-of-16 residual decrease on halving eta, both at h=0 and h=1/10. This is supporting **UNVALIDATED NUMERICAL EVIDENCE**, separate from the exact zero-coefficient substitution proof.

## 4. Proved small-step fate

The numerator obeys \(33h^2-240h+688\ge628>0\) for \(0\le h\le1/4\), and \(1-3h>0\). Hence \(c_+(h)>0\) on the entire D0 h interval. In particular,

\[
 c_+(0)=\frac{344\sqrt3}{3}
 \simeq198.6084926012312629911,
 \qquad c_+'(0)=992\sqrt3.
\]

The exact derivative is included for clarity; the generator coefficient is already nonzero, so no higher-order search is needed. Expanding in h gives

\[
 \nu_+(h,\eta)
 =\left(\frac{688\sqrt3}{3}+1984\sqrt3\,h+O(h^2)\right)\eta^3+O(\eta^5),
\]
\[
 \boxed{\omega_+(h,\eta)
 =\frac{688\sqrt3}{3}h\eta^3
 +1984\sqrt3\,h^2\eta^3
 +O(h^3\eta^3+h\eta^5).}
\]

The joint analytic neighborhood justifies these local expansions. At h=0, nu is obtained from the extended generator equations; omega/h and omega/h² are not evaluated by direct division. At positive h they are respectively nu and nu/h. The fact that the per-step angle tends to zero does not eliminate its limiting rate.

For the conjugate negative-chirality continuation \(\nu_-=-\nu_+\) at the same ordered coefficients. These conclusions hold locally on the specified isolated continuation; they do not assert a sign or stability classification for every state, every unequal coefficient triple, or every eta.

## 5. Validated continuation and finite-root isolation

### 5.1 What is certified

**VALIDATED NUMERICAL RESULT.** All calculations use precisely

\[
 h\in\{0,1/10,1/100,1/1000\}.
\]

The diagnostic Newton solves use 110 decimal digits. The subsequent proof uses outward-rounded interval arithmetic at 100 decimal digits. Root approximation and root certification are separate operations.

The original eta ladder was provisional. A fixed budget of 64 parameter subintervals per positive path was imposed before accepting the continuation. At h=1/10 the first original-ladder interval \([0,(1/100)/64]\) failed the sufficient contraction test: its computed q bound exceeded 4.077. This is a failure of that enclosure, not evidence of nonexistence or a bifurcation. The entire nested ladder was reduced by ten, as authorized:

\[
 \boxed{\eta\in\{\pm1/1000,\ \pm1/2000,\ \pm1/4000\}.}
\]

No hatted coefficient, mean k, perturbation direction, gauge, or branch label was retuned. The certified positive parameter path is \([0,1/1000]\), divided into 64 equal subintervals at each h. Negative paths are obtained by the exact fixed-label symmetry and their finite roots are independently approximated and isolated.

### 5.2 Contraction certificate and connection proof

For one parameter interval E, choose an approximate midpoint root \(x_c\in\mathbb R^7\), a fixed finite-decimal approximate inverse C, and an infinity-norm ball \(X=x_c+[-r,r]^7\). Interval automatic differentiation encloses the **full** state/rate derivative of G on \(X\times E\). Form rigorous bounds

\[
 Y\ge\sup_{\eta\in E}\|CG(x_c,\eta)\|_\infty,\qquad
 q\ge\sup_{x\in X,\eta\in E}\|I-CG_x(x,\eta)\|_\infty.
\]

Every accepted box satisfies \(q<1\) and \(Y+qr<r\). Therefore the map \(x\mapsto x-CG(x,\eta)\) contracts X into its interior for every parameter in E. Banach's theorem gives a unique root in X for each eta. The same inequality shows the full border is nonsingular; specifically \(\|G_x^{-1}\|_\infty\le\|C\|_\infty/(1-q)\). C need not be an exact inverse: \(\|I-CG_x\|<1\) itself implies its nonsingularity along with that of the square Jacobian.

Every shared parameter endpoint has an additional radius-\(10^{-60}\) fixed-parameter root box. That tight box is explicitly proved to lie inside both adjacent parameter boxes. Their unique roots consequently agree. The first box contains the known exact reference at eta zero. These finite overlap certificates establish connection to D0, rather than merely displaying a series of nearby low-residual roots. There are **256 parameter boxes and 260 endpoint boxes** over the four h values; the prescribed positive eta values occur among those endpoints.

The remaining negative-eta roots are linked by C composed with \(j\mapsto2-j\), which negates eta on this direction and preserves the chirality label. Their fixed-parameter boxes are additionally checked against uniqueness boxes containing the transformed positive endpoint. Conjugation transports the entire proof to the negative-chirality branch by a signed coordinate isometry.

The interval elementary functions enclose the actual equations. In particular the removable quotient \(E_h(t)\) is evaluated with its entire series through degree 24 and the explicit remainder bound

\[
 \left|E_h(t)-\sum_{n=1}^{24}\frac{-(-i)^nh^{n-1}t^n}{n!}\right|
 \le \frac{|h|^{24}|t|^{25}e^{|ht|}}{25!}.
\]

Its real and imaginary derivatives are evaluated directly as \(\sin(ht)\) and \(\cos(ht)\). At h=0 the exact expression is it. Positive lower bounds on input and prestage moduli justify every square root and phase-unit expression. Recorded endpoint bounds are rounded outward, not treated as exact midpoints.

### 5.3 Bounds along the connected paths

The following are deliberately weakened outward decimal summaries of the full interval receipts:

| h | Maximum q below | Minimum input modulus squared above | Minimum prestage modulus squared above | Maximum border inverse norm below |
|---:|---:|---:|---:|---:|
| 0 | 0.196109 | 0.497619 | 0.497619 | 72.417 |
| 1/10 | 0.523617 | 0.495978 | 0.495886 | 189.991 |
| 1/100 | 0.212847 | 0.497508 | 0.497501 | 76.597 |
| 1/1000 | 0.197700 | 0.497608 | 0.497608 | 72.811 |

The inverse norms refer to the equivalent full seven-equation system in normalized local coordinates. They are not silently substituted for condition numbers in an unrelated coordinate convention. At a root, converting to the original physical-complex residual and state coordinates gives a conservative factor-two bound for the corresponding original bordered inverse in the real infinity norm.

Gauge positivity is certified throughout. The maximum local phase deviation is below 0.016566 radians, much less than pi/6. Hence every neighbor phase difference stays away from pi, the winding remains +1 on the positive branch, and each positively oriented chirality summand remains positive. Conjugation gives winding -1 and negative chirality. This is a domain certificate, not a plot-based label.

## 6. Finite rates and controlled comparison with the cubic coefficient

The table lists midpoint digits for eta positive on the positive-chirality branch. Every rate has a certified coordinate error at most \(10^{-60}\) in nu. Both signs of eta and both chirality labels are provided in the results file, giving **48 accepted chiral-root records**, derived from 24 independently isolated positive-chirality points and their exact conjugates.

| h | eta | nu, approximately | nu / (2 eta³), approximately |
|---:|---:|---:|---:|
| 0 | 0.001 | 3.96847183606590e-7 | 198.42359180329 |
| 0 | 0.0005 | 4.96412883151119e-8 | 198.56515326045 |
| 0 | 0.00025 | 6.20618242410550e-9 | 198.59783757138 |
| 0.1 | 0.001 | 1.12177163091642e-6 | 560.88581545821 |
| 0.1 | 0.0005 | 1.39907430589031e-7 | 559.62972235613 |
| 0.1 | 0.00025 | 1.74764433349168e-8 | 559.24618671734 |
| 0.01 | 0.001 | 4.33329030539714e-7 | 216.66451526986 |
| 0.01 | 0.0005 | 5.42025801905918e-8 | 216.81032076237 |
| 0.01 | 0.00025 | 6.77634944420660e-9 | 216.84318221461 |
| 0.001 | 0.001 | 4.00302531755321e-7 | 200.15126587766 |
| 0.001 | 0.0005 | 5.00733550033525e-8 | 200.29342001341 |
| 0.001 | 0.00025 | 6.26019299725693e-9 | 200.32617591222 |

The exact coefficient values at these four h values are approximately 198.60849260123, 559.11239698359, 216.85381829653, and 200.33684804178, respectively. Finite eta ratios need not equal those coefficients; treating them as the coefficients would produce noticeable errors, particularly at h=1/10.

The ratio's certified root-error contribution is bounded by

\[
 \frac{10^{-60}}{2|\eta|^3}\le3.2\times10^{-50}
\]

on the accepted ladder. The finite-eta correction is much larger than this numerical uncertainty. Exact analyticity plus the computed cubic coefficient and the symmetry-excluded fourth-order rate term proves

\[
 \frac{\nu_+(h,\eta)}{2\eta^3}-c_+(h)=O(\eta^2).
\]

For each accepted point the results file encloses the scaled remainder

\[
 R(h,\eta)=\frac{\nu_+(h,\eta)/(2\eta^3)-c_+(h)}{\eta^2}
\]

using the certified rate interval and an interval evaluation of the exact c. Across the twelve positive points its magnitude is below \(2.141\times10^6\). For h=0, its values at the three decreasing eta values are approximately -184900.798, -173357.363, and -170480.478; for h=1/10 they are approximately 1773418.475, 2069301.490, and 2140635.740. These are finite-point remainder bounds. They are not a claimed uniform explicit remainder constant over all intervening eta. The order statement rests on the analytic proof, and the coefficient was derived before examining these ratios.

For every record, `D1_RESULTS.json` supplies h, eta, ordered k, branch label, all three complex state components, rate and angle, omega/h and omega/h² when h>0, gauge and full residuals, input/prestage moduli, winding/chirality, the root enclosure, inverse bounds, and continuation provenance. At h=0 the divided-angle fields are null; nu belongs to the extended generator equations.

## 7. Built-in identities and joint symmetries

### Generator identity, including its sign

**DERIVED IDENTITY.** The generator's amplitude/coupling contribution has real total pairing with z, because its onsite coefficients are real and the Laplacian is real symmetric. Therefore

\[
 \Im(z^\dagger X_k(z))
 =\frac1{30}\sum_i|z_i|^2\sum_{j\sim i}\sin3(\arg z_j-\arg z_i).
\]

At \(X_k(z)=i\nu z\), the left side equals \(\nu\sum_i|z_i|^2\). This proves the requested **positive** sign and the coefficient \(\widehat\lambda=1/30\). At positive h, D0's exact native identity is

\[
 \sum_i|z_i|^2\sin(h\nu-\delta_i)=0,
\]

with kicks recomputed at the actual prestage. Neither identity replaces the full relative-equilibrium equations.

All fixed-root interval boxes enclose zero in each full equation, gamma, and the appropriate identity. A conservative common bound on the original real residual components over those boxes is \(2.84\times10^{-60}\); the identity bound is below \(2.16\times10^{-60}\). At the certified exact root the full residual is exactly zero; the intervals describe uncertainty in its represented coordinates.

Independent 110-digit midpoint diagnostics give maximum identity residual below \(2.32\times10^{-108}\). These tiny numbers are diagnostics, not the reason roots are certified.

### Symmetry checks and the control

The exact transformation rules remain those of D0:

- Conjugation changes chirality and negates nu and omega at the same ordered k.
- Cyclic relabeling carries k and preserves the rates and chirality label.
- Pure reflection carries k, changes chirality, and preserves the rates.
- Conjugation composed with reflection carries k at fixed chirality and negates the rates.
- For this chosen direction, C composed with \(j\mapsto2-j\) also implements eta to minus eta within the positive-chirality branch.

In local coordinates these are permutations and sign changes, with the reference-specific gauge restored consistently. They transport interval root balls and nonsingularity certificates. Independent transformed physical-complex residuals are below \(3.69\times10^{-105}\). No original-review “pure reflection must negate drift” rule is reintroduced.

One prescribed two-equal-coefficient control uses h=1/10, eta=1/100000, and the direction \((1,1,-2)\). A single parameter box validates its connection to the same chiral reference, with q below 0.372566, and a radius-\(10^{-60}\) endpoint box isolates the root. C composed with the reflection swapping the two equal coefficients fixes the local branch and negates nu. Local uniqueness along the connected near-zero branch therefore proves **nu=0 exactly**. The numerical rate, about \(-1.17\times10^{-116}\), is rounding residue, not evidence of a tiny nonzero drift. This is one control, not a parameter survey.

### What changes and what does not

**EXACT THEOREM.** For a relative equilibrium, \(z^+=e^{i\omega}z\) leaves

\[
 z^+(z^+)^\dagger=zz^\dagger
\]

and every component intensity unchanged. Every already defined common-phase-invariant chirality readout is unchanged as well. At the generator relative equilibrium, the derivative of this coherence matrix is zero. The independent diagnostics check these consequences; their largest coherence residual is below \(4.92\times10^{-106}\). The native complex128 implementation gives full-update relative-equilibrium residuals below \(3.15\times10^{-16}\), consistent with its rounding precision and distinct from the interval proof of the ideal mathematical equations.

Thus the nonzero rate concerns motion around a common-phase group orbit in state space. It is not automatically an observable current, spatial core rotation, scaffold motion, or a physical time frequency. The reference is a saddle. D1 has not proved that the continued relative equilibria attract trajectories, and no trajectories were integrated.

## 8. Evidence, reproduction, and limits

The output set is exactly:

1. `D1_NATIVE_CHIRAL_PHASE_DRIFT.md` — this report.
2. `verify_d1.py` — exact jets, independent numerical formulas, interval automatic derivatives and contraction certificates, symmetry tests, and preservation checks.
3. `D1_RESULTS.json` — expressions, all accepted roots, parameter/endpoint certificates, remainder intervals, source hashes, and integrity receipts.

The reproducible PowerShell command, using the already installed environment, is:

```powershell
& 'python' -X utf8 -B `
  'project-source\research\D1_chiral_drift_20261006\verify_d1.py' `
  --jets --validate --checks --enclose --preserve
```

It writes only this lane's results file, retaining its initial baseline. It imports the native pure dynamics module with bytecode disabled for the bounded complex128 comparison; it does not run predecessor scripts or simulation drivers. The external environment uses SymPy for exact algebra and mpmath for the independent high-precision and interval arithmetic. No dependencies were installed.

Evidence classifications remain separate:

| Class | Result |
|---|---|
| **DERIVED IDENTITY / EXACT THEOREM** | Full native residual equivalence; explicit cubic coefficient; nonzero generator coefficient; analytic orders in eta and h; drift identity signs; symmetry implications; coherence invariance. |
| **EXACT SYMBOLIC CHECK** | Border determinant; order-by-order state/rate solve; substitution in every original residual through degree three; coefficient normalization and derivative. |
| **VALIDATED NUMERICAL RESULT** | Connected parameter sections; endpoint overlaps; isolated roots with nonzero rate intervals; regularity, gauge and winding bounds; one stationary control; interval residual and identity enclosures. |
| **UNVALIDATED NUMERICAL EVIDENCE** | Newton midpoint residuals, direct Taylor-substitution scaling, transformed-state comparisons, native complex128 checks. These support but do not certify the roots. |
| **OPEN QUESTION / OUTSIDE D1** | Behavior outside the validated/local branch; finite-amplitude global classification; attraction of continued states; physical meaning or calibration of common phase. |

The final D1 result is **133/133 named checks passing**, recorded by class in the results file. This is separate from D0's retained 64/64 and all earlier checkpoint counts. A count is not a count of independent theorems: the written arguments and interval inequalities state what is proved.

The preservation pass confirms the original 16,035 file identities, original dirty/untracked status, HEAD, branch, index fingerprint, and source/predecessor hashes. Existing temporary files remain included and untouched. The results file records the final report and script hashes. No repository changes or publication actions were made.

## 9. Answer and stop

**Yes.** On D0's specified isolated chiral branch, weak unequal coefficients produce a nonzero common complex-phase rate. Analytically its leading form is

\[
 \nu_+(h,\eta)=
 \frac{\sqrt3(33h^2-240h+688)}{3(1-3h)^3}\eta^3+O(\eta^5),
 \qquad \omega_+=h\nu_+.
\]

At h zero the leading rate is \((688\sqrt3/3)\eta^3\), so it survives the mathematical generator limit. Exact symbolic substitution proves the coefficient; validated continuation certifies nonzero finite rates on the smaller accepted ladder; high-precision and native-precision comparisons are supporting evidence. The larger original eta ladder remains uncertified in this bounded run.

In plain language, the unequal native coefficients can make this chiral state advance by a common complex phase even while its intensities, coherence matrix and existing phase-invariant chirality stay fixed. That is the mathematical link D1 establishes. It supplies no new physical motion observable or clock.

**STOP after D1.** Returned for scientific review and written closeout. No D2, paper revision, publication, gravity/QED/dark-matter interpretation, or other research lane was started. The TL0–TL4 synthesis remains a separate outstanding write-up.
