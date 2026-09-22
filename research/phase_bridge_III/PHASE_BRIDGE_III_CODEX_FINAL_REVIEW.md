# Phase Bridge III — Codex final independent review

Date: 2026-09-22. Frozen repository baseline: `899d0fa900dc0d0ab8406e889908e47468d343db`.

## 1. Decision and scope

**The core local-clock threshold survives. The corrected, conditional results can be frozen as research, with the accepted synthesis as the operative statement. No kernel change is warranted.** Claude's N2 needs a domain correction, N3 needs local/nondegeneracy qualifications, and the unrestricted cubic-CGLE equivalence must retain the condition `K=0`. The nonlinear destinations are reproducible finite-run observations; Hopf criticality remains unproved.

This review checks N1–N6, the eight corrections in Claude §23, and the narrow oscillator equivalence. It does not reopen the historical papers, rerun earlier scientific suites, search literature, or verify priority. Earlier Phase III results are carried forward only where needed for these checks; the final block does not mean every earlier proof was independently rerun here.

The original report and Claude's review remain separate, unchanged evidence. `PHASE_BRIDGE_III_ACCEPTED_RESULTS.md` contains the corrected synthesis. Corrections below are explicit restrictions or consequences of the equations both reports use, not silent changes to either report.

### Claim ledger

| Claim | Classification | Disposition |
|---|---|---|
| N1 characteristic equation and threshold formula | ACCEPTED_EXACT | Derived from the full field and checked symbolically. |
| N1 stable-to-unstable threshold for the physical-amplitude branch | ACCEPTED_WITH_ASSUMPTION | Requires the branch, regular rate law, nonzero coupling, and strict stability conditions below. |
| N1 formula as an unconditional criterion for existence of imaginary roots | REJECTED | An already unstable system can have imaginary roots; this is a stability threshold under stated hypotheses. |
| N2 exact return translation, and identity on its zero-drift domain | ACCEPTED_EXACT | A full turn inside the domain is essential. Use `nu*Shat=0`, including `nu=0`. |
| N2 every historical interior orbit closes at zero mean | REJECTED | A lower-boundary exit can occur before a turn finishes. |
| N2 positive mean forces every historical interior point toward rho=1 | REJECTED | The same early-exit obstruction applies. |
| N2 mean-drift classification for surviving, complete advancing trajectories | ACCEPTED_WITH_ASSUMPTION | Positive bounded clock on the closed strip gives the precise classification in §3. |
| N2 fate independent of warp for arbitrary historical initial conditions | REJECTED | Warp changes the first-turn survival condition. Independence holds in the restricted forward-invariant regime. |
| N3 multiplier identity | ACCEPTED_EXACT | `div(MX)=0` for sufficiently regular G. |
| N3 complete family and canonical embedding for arbitrary G | ACCEPTED_WITH_ASSUMPTION | Locally complete at regular points; an embedding needs nonvanishing G and global consistency if claimed globally. |
| N3 arbitrary I-star as a physical normalization or canonical gauge of a fixed form | REJECTED | It is a simultaneous scale freedom of the chosen form and Hamiltonian. |
| N4 invariant complex lines and balance | ACCEPTED_WITH_ASSUMPTION | Identical channel laws, corrected indexing, real coefficients, and the stated nonzero-domain model. |
| N5 tested destinations and finite absence of small saturation | NUMERICAL_OBSERVATION | Reproduced with explicit initial data and tighter tolerances. |
| N5 absence of every other attractor | REJECTED | The fixtures do not establish a global attractor theorem. |
| N5 subcritical Hopf classification | UNRESOLVED | Observations support that interpretation, but no first Lyapunov coefficient or branch continuation was computed. |
| N6 Jordan square-root sensitivity | ACCEPTED_EXACT | Exact monodromy and controlled floating perturbations. |
| N6 explanation of historical computations | UNRESOLVED | No such inference is made. |
| Affine local clocks give a cubic oscillator network when K=0 | ACCEPTED_EXACT | Direct substitution. |
| Full K-nonzero system is exactly the same cubic network | REJECTED | An additional third-harmonic phase term remains. |
| Novelty or priority of the construction | UNRESOLVED | No literature or priority audit was performed. |

## 2. N1 — general local-clock threshold

Use the specified comparison field on nonzero channels,

\[
\dot\Omega_i=\epsilon\Omega_i(k-|\Omega_i|^2)+g(L_3\Omega)_i
 +i\Omega_i\left[K\sum_{j\ne i}\sin3(\phi_j-\phi_i)+\varpi(I_i)\right],
\qquad I_i=|\Omega_i|^2/2.
\]

This is not the frozen discrete Paper-A map. Parameters are real and identical across channels. Let `epsilon != 0`,
\(r^2=k-3g/\epsilon>0\), and let \(\varpi\) be at least C1 near \(I_*=r^2/2\).
The two splay orderings have phases \(\theta_j=\pm2\pi j/3\), with **j=0,1,2**.

Differentiate the full radial and angular field, then use \(x_i=\delta r_i/r\), \(y_i=\delta\phi_i\). The resulting real matrix is

\[
\begin{pmatrix}
-2\epsilon r^2 I-gL_3/2&-gS\\
cI+gS&(-g/2+3K)L_3
\end{pmatrix},\quad
S_{ij}=\sin(\theta_j-\theta_i),\quad c=r^2\varpi'(I_*).
\]

Here \(S^T=-S\), \(S\mathbf1=0\), \(S^2=-9P_\perp/4\). On the common-channel subspace the eigenvalues are \(-2\epsilon r^2,0\). On its transverse complement, \(L_3=-3I\) and the two eigenvalues of S are \(\pm3i/2\). Thus, with

\[
a=-2\epsilon r^2+3g/2,\quad d=3g/2-9K,\quad
\tau=a+d,\quad D=ad-9g^2/4,\quad b=3gc/2,
\]

the transverse quadratics are

\[
p_\pm(\lambda)=\lambda^2-\tau\lambda+D\pm ib,
\]

and the full real characteristic polynomial is

\[
\lambda(\lambda+2\epsilon r^2)
\left[(\lambda^2-\tau\lambda+D)^2+b^2\right].
\]

The verifier differentiates the full field independently and compares its characteristic polynomial to this expression. Reversing the ordering interchanges the two quadratics.

For \(p_+\), substituting \(\lambda=i\omega\) gives
\(\omega^2=D\), \(\tau\omega=b\). Therefore, for \(g\ne0\), \(\tau\ne0\), a nonzero-frequency crossing satisfies

\[
\boxed{c_*^2=\tau^2\left(\frac{4ad}{9g^2}-1\right)},\qquad
\omega_*=\frac{3gc_*}{2\tau},\quad |\omega_*|=\sqrt D.
\]

The other quadratic gives the conjugate frequency. The sign in the displayed signed frequency is tied to the chosen quadratic, not an independently selected handedness.

### Stability and degeneracies

For a **stable-to-unstable transverse threshold**, require \(\tau<0\), \(D>0\), \(g\ne0\). The transverse quartic has coefficients
\(1,-2\tau,\tau^2+2D,-2\tau D,D^2+b^2\).
Its second and third Hurwitz minors are

\[
-2\tau(\tau^2+D),\qquad 4\tau^2(\tau^2D-b^2).
\]

Consequently all transverse roots have negative real parts exactly when \(b^2<\tau^2D\). Equality is the oscillatory linear threshold; above it a conjugate pair has positive real part. For stability of the full common-phase quotient also require \(\epsilon r^2>0\). These conditions are not hypotheses for every possible algebraic imaginary root of an already unstable branch.

At the nondegenerate threshold the crossing is simple and

\[
\frac{d\,\Re\lambda}{d|c|}=\frac{3|g|\sqrt D}{\tau^2+4D}>0.
\]

This establishes a simple transverse oscillatory crossing. It does not compute the nonlinear Hopf criticality. Cases `g=0`, `tau=0`, `D=0`, `r=0`, and `epsilon=0` require separate treatment; the displayed threshold formula is not used there. In particular `g=0` leaves a triangular slope coupling and no such slope-induced threshold.

For \(\epsilon=g=K=1,k=6\), \(r^2=3\), \(a=-9/2\), \(d=-15/2\), \(\tau=-12\), \(D=63/2\). With \(\varpi=1+\alpha(I-3/2)\), \(c=3\alpha\), giving

\[
|\alpha_*|=4\sqrt{14}=14.9666295471,\qquad
|\omega_*|=3\sqrt{14}/2=5.61248608016.
\]

The derivative with respect to \(|\alpha|\) is \(\sqrt{14}/20\), approximately 0.187083.

| epsilon, g, K, k | alpha threshold | Critical frequency | Transverse test |
|---|---:|---:|---|
| 1, 1, 1, 6 | 14.9666295471 | 5.6124860802 | Negative at 0.99 threshold, zero within numerical error, positive at 1.01 threshold |
| 1, 0.8, 0.5, 5 | 8.0236490933 | 3.4292856399 | Same |
| 0.7, 1.3, 2, 9 | 18.3074646479 | 6.4761099435 | Same |
| 2, 0.5, 0.25, 4 | 23.8078683561 | 4.2204857540 | Same |

These confirm Claude §15 lines 799–816, with the threshold qualifications above. Equal constant detunings retain this exact branch but give `c=0`; they cannot reproduce this dependence on the local slope while preserving the branch and its on-orbit data.

## 3. N2 — return translation, survival, and the historical domain

For H1,

\[
\dot\rho=\nu(1-\rho)S(\phi),\qquad
\dot\phi=v(\rho)=\omega+\kappa W(\rho),\quad
S(\phi)=\sin(E_0+A\sin\phi),
\]

take a domain below rho=1 where the field is C1. Define \(F'=v/(1-\rho)\), \(U'=S\), \(Q=F-\nu U\). Direct differentiation gives \(\dot Q=0\). Where `v>0`, F is strictly increasing and

\[
F(\rho(\phi))=F(\rho_0)+\nu\int_{\phi_0}^{\phi}S(s)\,ds.
\tag{R}
\]

Let \(m=\nu\widehat S\), \(\widehat S=\int_0^{2\pi}S\). A completed turn gives \(F(\mathcal P\rho)=F(\rho)+m\). Thus the return map is the identity **where it exists** if `m=0`; it has no periodic points if `m!=0`. A regular periodic orbit in a strictly advancing flow must wind a positive integer number of turns, so the same obstruction excludes all such interior periodic orbits for nonzero m.

For the historical open strip `0<rho<1`, put `F(0)=0`. If v extends continuously and is strictly positive on `[0,1]`, then \(0<v_{min}\le v\le v_{max}\), and \(F(1^-)=+\infty\). Equation (R) gives the complete first-turn survival criterion:

\[
F(\rho_0)+\nu\int_{\phi_0}^{\phi}S(s)\,ds>0
\quad\text{throughout the turn}.
\tag{S}
\]

Under these assumptions:

* **m=0:** each orbit satisfying (S) returns and is a closed orbit. The full-turn subset is foliated by those orbits. Points failing (S) reach the lower boundary before closure; one cannot call the entire historical interior a closed-orbit foliation.
* **m>0:** no interior periodic orbit exists. A point that survives its first turn survives all subsequent turns: each partial-turn F value is increased by nm. Such trajectories tend to rho=1 as time tends to infinity. Other initial points can first reach or cross rho=0.
* **m<0:** every interior trajectory reaches rho=0 in finite time, possibly during its first turn. If the unmodified equations are extended past zero they can exit the strip; a clamp, reset, or reflecting rule would be a new model. No post-exit fate is asserted here.

The finite-time and upper-limit statements use the bounded, uniformly advancing clock. Positivity solely on a visited open range does not by itself ensure complete turns or a boundary orbit at rho=1. With `v(1)>0`, the upper boundary has period `2pi/v(1)` and transverse multiplier \(\exp[-m/v(1)]\). Positive m gives a linearly attracting boundary orbit, but does not make its basin equal to the entire historical interior.

### Explicit counterexamples to the unrestricted wording

Claude §9, lines 546–559, claims every zero-mean interior orbit is periodic and that the sign of m alone fixes every interior fate independently of warp. Both require the preceding restrictions.

1. Let `nu=1`, `E0=0`, `A=pi/2`, `v=1`, `rho0=0.01`, `phi0=pi`. The mean of S is exactly zero by half-turn antisymmetry. But \(\int_\pi^{2\pi}S=-2.36115996713\), whereas \(-\log(0.99)=0.01005033585\). In the extended rho<1 solution the endpoint rho is approximately -9.4972. The historical trajectory must cross zero before completing that half-turn. It closes only if one continues in an extended domain, which is a separate assumption.
2. Let `nu=1`, `E0=0.2`, `A=2`, `rho0=0.01`, `phi0=3pi/2`. Here \(\widehat S\approx0.27947753553>0\), but the integral over the first 0.1 radians is approximately -0.09745948604. With `v=1`, the logarithmic coordinate is already negative by that point, proving an early lower exit. With the **same forcing and initial state**, `v=1000` cannot exit: `|S|<=1` gives the lower first-turn bound \(-\log(0.99)-2\pi/1000>0\), and subsequent turns add positive drift. This solution tends to rho=1. Changing the warp can therefore change survival and fate in the unqualified historical-strip problem.

These counterexamples use exactly the historical functional form of S. The scalar quadratures are recorded with numerical error estimates; the zero mean in example 1 follows analytically from antisymmetry.

There is a valid, useful warp-independent result: if `nu*S>=0` everywhere and is not identically zero, the strip is forward invariant, m is strictly positive, and every interior trajectory tends to rho=1 under the bounded advancing-clock assumptions. The zero forcing case is a family of constant-rho rotations. This includes the `nu=0` degeneracy omitted by a condition written only as `Shat=0`. No kappa-only instability threshold follows for this restricted regime.

## 4. N3 — integrating factors, embeddings, and scale

Let \(X=(\nu(1-\rho)S,v)\). On a C1 patch below rho=1, F and U have the derivatives above. For any C1 scalar G on the attained Q range,

\[
M=\frac{G(Q)}{1-\rho},\qquad \operatorname{div}(MX)=0.
\]

This identity is accepted exactly. To see local completeness, set \(B=(1-\rho)M\). The multiplier equation is exactly \(XB=0\). At a regular point \(X\ne0\), equivalently \(dQ\ne0\), a local flow box has Q as its transverse coordinate. Thus every C1 first integral B there is some G(Q). At equilibria, or across multiple connected components of a level set, a single global G is not automatically complete. One must specify a regular chart or connected-leaf/global descent hypotheses.

The two-form and Hamiltonian are

\[
\sigma_G=M\,d\rho\wedge d\phi,\qquad
\iota_X\sigma_G=-G(Q)\,dQ=dH_G,\qquad
H_G=-\int^QG(s)\,ds.
\]

**An actual symplectic chart requires G to be nowhere zero on that patch.** `G=0` satisfies the divergence identity but gives the zero form. A zero of G makes the form degenerate there. A nonzero negative G is admissible with reversed orientation; a positive-action physical convention may require a positive orientation. Locally, \(J(\rho,\phi)=\int^\rho M(s,\phi)ds\), \(\theta=\phi\), gives \(dJ\wedge d\theta=\sigma_G\). This is a local canonical realization, not a claim of global positive action.

On the phase cylinder, Q changes by -m on going around once. For `m!=0`, a multiplier of this form descends only if \(G(q-m)=G(q)\) on the relevant ranges. A primitive H_G need not descend. A continuous, nonvanishing, m-periodic G has fixed sign, so its integral over a period is nonzero; its local Hamiltonian has nonzero monodromy. For `m=0`, Q and H_G can be single valued, subject to the other global domain conditions. This separates a globally symplectic field from a globally Hamiltonian field.

For the logarithmic choice, \(y=-\log(1-\rho)\), \(I=I_*y\),

\[
\sigma=I_*\,dy\wedge d\phi,\qquad H=-I_*Q.
\]

Changing the positive constant I-star scales **both** sigma and H and leaves X unchanged. That is the precise dynamical scale freedom. It is not a canonical transformation preserving a fixed sigma, and the physical coefficient \(\Omega=\sqrt{2I}e^{i\phi}\) changes in magnitude. No physical normalization, energy unit, or time unit is selected. More general G similarly changes the form and Hamiltonian together; keeping the old form fixed instead generally changes the vector field.

The logarithmic real chart exists for rho<1 where W is defined. Its unshifted **positive-action complex encoding** requires `0<rho<1`; negative rho gives negative I. At rho=0 the boundary phase circle collapses in that encoding, and rho=1 lies at infinite I. Claude §7 lines 435–447 must not merge these distinct scopes.

Finally, integrability does not exclude a positive exponent at an interior saddle. Claude §8 lines 487–499 states a blanket no-positive-exponent conclusion, whereas its §9 correctly excludes equilibria from the unit-multiplier theorem. Only the regular periodic-orbit conclusion is admitted here. For example, the local equilibrium formula allows eigenvalues \(\pm\sqrt{\nu(1-\rho)S'v'}\); positive radicand is a saddle.

## 5. N4 — invariant lines and action balance

With identical real epsilon, g, K, equal real k, and the same sufficiently regular local rate function, the following complex lines are invariant wherever the specified field is defined:

\[
\Omega_j=z,\qquad \Omega_j=z\zeta^{j-1},\qquad
\Omega_j=z\bar\zeta^{j-1},\quad j=1,2,3,\quad \zeta=e^{2\pi i/3}.
\]

Each is two real dimensional. Claude's expression with `Omega_1` and exponent j requires the index correction j-1, or a switch to j=0,1,2 and a common coefficient z. The third-harmonic sums vanish on all three lines. L3 acts by 0 on the first, and -3 on the other two, so the reduced equations are

\[
\dot z=\epsilon z(k-|z|^2)+i\varpi(|z|^2/2)z,
\]
\[
\dot z=[\epsilon(k-|z|^2)-3g]z+i\varpi(|z|^2/2)z
\quad\text{on either splay line}.
\]

These statements concern the punctured lines unless an origin extension is explicitly supplied. The continuous comparison field contains phases; no global zero-component regularization is silently inherited from the discrete map.

Put \(N=\sum I_i\). For **every** nonzero-domain state of this field, not only relative equilibria,

\[
\dot N=2\epsilon\sum_i I_i(k-2I_i)
-g\sum_{i<j}|\Omega_i-\Omega_j|^2.
\]

The phase terms are purely imaginary multiples of their own channels and make no direct contribution. The real symmetric Laplacian gives the displayed negative pairwise sum. At a common-phase relative equilibrium \(\Omega(t)=e^{i\omega_*t}z\), N is constant and the requested balance follows. It is necessary, not sufficient, for a relative equilibrium. K and varpi do not appear **explicitly**; they can still influence which actions and phase differences realize a relative equilibrium. The formula also presumes no omitted forcing, noise, or additional amplitude law.

## 6. N5 — independent nonlinear observations

The verifier integrates the five real quotient coordinates
`(log I1, log I2, log I3, delta21, delta31)` using the specified field with `epsilon=g=K=1`, `k=6`, and \(\varpi=1+\alpha(I-3/2)\). Log actions keep the numerical coordinates positive. Three deterministic Cartesian derivative comparisons check the implemented quotient equations independently. No random perturbations or broad scans are used.

The splay base is
\(y_s=(\log1.5,\log1.5,\log1.5,2\pi/3,4\pi/3)\).
Use the fixed direction \(d=(0.4,-0.3,-0.1,0.7,-0.5)\). A perturbation called 0.01 or 0.2 means exactly `y_s + scale*d` in these coordinates, not an unspecified Cartesian norm. Claude did not supply enough initial-condition detail for a bit-for-bit replay; these are independent reproduction fixtures.

| Fixture | Initial condition | Observed destination |
|---|---|---|
| alpha=threshold+0.05 | y_s+0.01d | In-phase, actions 3, relative phases zero |
| alpha=threshold+0.25 | Same | In-phase |
| alpha=threshold+1.0 | Same | In-phase |
| alpha=threshold-0.05 | y_s+0.01d | Original splay branch |
| alpha=threshold-0.05 | y_s+0.2d | In-phase |
| alpha=threshold-0.05 | Perturbed in-phase base+0.01d | In-phase |

Each fixture uses DOP853 twice: `(rtol,atol,max_step)=(2e-12,2e-14,0.1)` and `(5e-14,5e-16,0.05)`. Maximum time is 2400. Arrival means the maximum absolute action deviation and relative-unit-phasor deviation from a branch falls below `1e-8`. A further five time units check persistence near that branch. The results record full initial data, actual termination times, tolerances, finite tail errors, and sampled action minima. Both integrations are also compared at 10,001 common times using action and relative-phasor differences, with required maximum discrepancy below `1e-3`. The actual largest discrepancy is `4.78172624e-6`; all six destination comparisons agree. At the tighter settings the three above-threshold arrival times are approximately 250.476375, 68.621607, and 22.228154. The below-threshold small perturbation arrives near 1329.957, with a five-unit tail error about `1.33e-8`; its tiny-error first-crossing time is sensitive to the oscillatory envelope even when the trajectories agree.

No small saturated modulation is observed before these trajectories settle at the in-phase branch. This is a statement about these fixtures, integration times, and precision. It excludes neither other basins nor periodic or chaotic attractors elsewhere. A spectrum changing with alpha proves a local linear change, not a global restriction to two possible attractors.

Below threshold the two attracting quotient equilibria also have analytic local support: the splay spectrum is strictly stable under §2, and the in-phase quotient eigenvalues are `-12` three times and `-15` twice, independent of finite alpha. Thus both local basins exist in the smooth nonzero domain. The numerical small/large perturbations demonstrate particular basin destinations, not the full basin boundary.

The escape just above threshold, finite absence of small saturation, and coexistence below are evidence consistent with subcriticality. They do not establish a nonzero first Lyapunov coefficient, the direction/stability of a periodic branch, or an absence of a nearby global basin mechanism. Those nonlinear classification questions remain unresolved.

```ini
LINEAR_THRESHOLD = THEOREM_UNDER_STATED_ASSUMPTIONS
NONLINEAR_DESTINATION = NUMERICAL_OBSERVATION
SUBCRITICALITY_EVIDENCE = SUPPORTED
SUBCRITICALITY_PROVED = NO
```

## 7. N6 — exact Jordan witness and numerical interpretation

Take H1 with `S=0`, `v(rho)=1+rho`, and `rho0=1/2`. The exact nonstationary circle has period \(T=4\pi/3\). In `(delta rho, delta phi)` its variational equation is \(\delta\dot\rho=0\), \(\delta\dot\phi=\delta\rho\), hence

\[
M_0=\begin{pmatrix}1&0\\s&1\end{pmatrix},\quad s=4\pi/3,
\qquad (M_0-I)^2=0,\quad M_0\ne I.
\]

It has exactly two unit multipliers and linear-in-n shear in \(M_0^n\). Perturb the opposite off-diagonal entry by delta:

\[
M_\delta=\begin{pmatrix}1&\delta\\s&1\end{pmatrix},\qquad
\lambda_\pm=1\pm\sqrt{s\delta},\quad
\operatorname{tr}M_\delta=2,\quad\det M_\delta=1-s\delta.
\]

With delta equal to plus or minus float64 machine epsilon, the actual eigensolver returns a real or imaginary split of approximately `3.04975125e-8`, while trace is 2 and determinant differs from 1 by approximately `9e-16`. This is a **controlled perturbation witness**. The eigensolver correctly computes the eigenvalues of the perturbed matrix; the problem is sensitivity of inferring the exact monodromy from finite-accuracy entries. Exact triangular input need not show any split.

Trace and determinant are useful stable aggregate diagnostics here, but close agreement does **not** certify exact unit multipliers or stability. The same witness has near-exact trace/determinant and a real eigenvalue greater than one for positive delta. Use the analytic periodic-orbit constraint, matrix-entry/backward-error control, trace/determinant and discriminant residuals, step/tolerance or precision refinement, and where appropriate a structure-preserving variational representation. Schur computation improves numerical robustness but cannot eliminate an intrinsically ill-conditioned spectrum. If monodromy error is eta, the scale is generally square-root eta near a Jordan block; eta can exceed machine epsilon because of integration error.

This verifies a plausible numerical failure mode only. No claim about the cause of historical runs is admitted. Claude §9 lines 568–577 needs this distinction, especially its description of trace/determinant as a sufficient “test”.

## 8. Eight corrections in Claude §23

| No. | Decision | Exact correction accepted here |
|---|---|---|
| 1 | MODIFY | Widen the regular periodic-orbit theorem to compact orbits in rho<1 **where the field is defined and C1**. The original §8.3 proof already uses this scope; its boxed/headline restriction is narrower. Do not widen the unshifted positive-action complex encoding beyond 0<rho<1. |
| 2 | MODIFY | Insert the survival-qualified return/drift classification in §3 above. The unrestricted historical-interior foliation and warp-independent fate assertions are false. Include nu=0. |
| 3 | MODIFY | Insert the exact multiplier family, local regular-point completeness, nonzero-G requirement, and global cylinder conditions. “Every G gives a canonical embedding” is false for zero/vanishing G. |
| 4 | ACCEPT | State C1 regularity and that closedness is relative to the frozen sigma. Global sufficiency additionally uses an appropriate simply connected action domain or direct exactness. |
| 5 | ACCEPT | Restate \(J_{\rm eff}=\Im(\Omega_1\overline{\Omega_2}\Omega_3)\). The clock contribution is \((\varpi_1-\varpi_2+\varpi_3)\Re(\Omega_1\overline{\Omega_2}\Omega_3)\). |
| 6 | ACCEPT | Require a continuous extension of the common local rate to I=0 for the stated one-channel-limit proof. Identical, strictly monotone rates are sufficient for that symmetry theorem; no stronger necessity claim is accepted. |
| 7 | MODIFY | Add the N1 theorem with its hypotheses and N5 as finite observations. Retain unresolved criticality and do not replace “linear instability” with a global no-new-attractor theorem. |
| 8 | ACCEPT | The field \(J\nabla C=(0,1)\) has constant norm. It is the state norm along its trajectories that need not be conserved. This corrects the original §2 line 58. |

For correction 4, the rate-form condition is \(\partial_{I_j}\varpi_i=\partial_{I_i}\varpi_j\) at fixed \(\sigma=\sum dI_i\wedge d\phi_i\). It is a local criterion; a different symplectic form is a different problem. For correction 6, the proof establishes a sufficient theorem. Claude §18's claim that any nonmonotone rate admits extra global unitaries does not follow merely from two equal rate values; global equivariance is a functional identity over all states. That stronger aside is not admitted.

## 9. Narrow oscillator equivalence and novelty scope

For `K=0` and \(\varpi(I)=\omega_0+\alpha I\), substitution gives exactly

\[
\dot\Omega_i=(\epsilon k+i\omega_0)\Omega_i
 -(\epsilon-i\alpha/2)|\Omega_i|^2\Omega_i+g(L_3\Omega)_i.
\]

This is the algebraic form of a discrete cubic complex Ginzburg–Landau / coupled nonisochronous Stuart–Landau network with real diffusive coupling. An affine shift such as \(1+\alpha(I-3/2)\) just changes omega0. The isolated-channel specialization is `g=K=0`.

For `K!=0`, one must add
\(iK\Omega_i\sum_{j\ne i}\sin3(\phi_j-\phi_i)\).
It is generally nonzero and is not the same cubic polynomial network. For example, phases `(0,pi/6,0)` with unit radii give an extra `iK` in channel 1. It vanishes on the invariant lines but its transverse derivative does not; indeed K occurs in d and in the threshold. Claude §19's table at line 980 correctly restricts `K=0`; its §20 line 1019 omits that essential condition. The synthesis retains the table's narrower statement.

The coupled spectral witness obstructs replacement by a constant-detuning model that preserves the specified orbit and spectrum. It does not establish non-removability by every possible coordinate change into every other model, nor a new mathematical class. Isolated phase flattening has its own regularity and global-circle restrictions. No conclusion is drawn about the full historical recursive programme, SRG, discrete recursion, additional stored state, or future models. “Novelty only in geometric realization” is not established by this algebra; priority and novelty remain unresolved.

## 10. Execution provenance and preservation

The accompanying verifier finishes with **73/73 computed predicates passing, zero failures**: 28 symbolic, 40 numerical, and 5 integrity checks. These are not 73 independent theorems. Narrative proofs, scope restrictions, and physical non-identifications remain separate from finite regression support. The final `results.txt` and `results.json` are the execution record, including software versions, initial conditions, script hash, tolerances, output classifications, and per-check booleans.

Execution used Python 3.11.15 in the existing `torment` environment, NumPy 2.4.4, SciPy 1.17.1, and SymPy 1.14.0. The command is:

```text
python -B research/phase_bridge_III/verify_phase_bridge_III.py
```

Only these new focused verification calculations were run. Claude's claimed 188 checks, random searches, and historical numerical accounts are source claims, not imported execution evidence. No helper from Claude, original kernel, or earlier verifier is imported.

Development executions are disclosed: the first run produced 68/70, exposing a SymPy characteristic-polynomial generator-symbol mismatch and an ill-conditioned arrival-time comparison. The symbol was explicitly substituted, and trajectory agreement at common times replaced the arrival-time test. Three Cartesian derivative checks were added. The next run produced 72/73: the closest-above-threshold transient differed by about 0.0108 between the initial solver settings despite matching destinations. Solver tolerances and maximum step were tightened for all fixtures without changing the 0.001 trajectory-agreement criterion, equations, initial states, or outcome labels. The accompanying final record contains the refined run.

The original report SHA-256 is
`d19178a45b44f422a0f9f5c38494c79778914be846f3e2eddb118e29baa68f95`.
Claude's external review and the byte-identical repository copy have SHA-256
`bd051995d03cec556ac291575249164755c23351ef1102a3af34a3cb373c8a5c`.
All 63 baseline-tracked files retain their pre-task byte hashes. The ordered tracked-path/hash aggregate is
`9ce79620e720e538e0295374ca1a504fecc5c6e0c9957cb0418a842ca6bacb80`.
No frozen source, CURRENT_STATE, archive manifest, or checksum file was edited. No kernel implementation, commit, or push is part of this task.

## 11. Final disposition

`READY_TO_FREEZE_PHASE_III=YES` means freeze the corrected accepted research statements and their limitations, with these two original reports preserved as history. It does not admit a physical rate law, select a face observable, resolve nonlinear criticality, or authorize modifying kernel_physics. Existing action–angle, polar-parent, commutator, and symmetry statements below retain their stated earlier hypotheses; this focused task is not a fresh audit of every earlier theorem.

```ini
PHASE_III_CORE_MATHEMATICS = ACCEPTED_WITH_ASSUMPTION
ACTION_ANGLE = ACCEPTED_EXACT_ON_NONZERO_PLANES
PAPER_A_POLAR_PARENT = ACCEPTED_EXACT_FOR_CONTINUOUS_PARENT_ON_NONZERO_DOMAIN
H1_CANONICAL_EMBEDDING = ACCEPTED_WITH_ASSUMPTION
H1_INTEGRABILITY = ACCEPTED_EXACT_WITH_LOCAL_AND_GLOBAL_SCOPE_DISTINGUISHED
H1_TRICHOTOMY = ACCEPTED_WITH_ASSUMPTION_SURVIVAL_AND_DOMAIN_QUALIFIED
COMMUTATOR_RANK_THEOREM = ACCEPTED_EXACT_CARRIED_FORWARD
GENERAL_LOCAL_CLOCK_THRESHOLD = ACCEPTED_EXACT_UNDER_STATED_BRANCH_AND_STABILITY_HYPOTHESES
120_DEGREE_THRESHOLD = ABS_ALPHA_EQUALS_4_SQRT_14
INVARIANT_MANIFOLDS = ACCEPTED_WITH_ASSUMPTION_AND_CORRECTED_INDEXING
ACTION_TRANSFER_BALANCE = ACCEPTED_EXACT_FOR_SPECIFIED_REAL_COEFFICIENT_FIELD
NONLINEAR_POST_THRESHOLD_DESTINATION = NUMERICAL_OBSERVATION_IN_PHASE_IN_TESTED_FIXTURES
SUBCRITICALITY = UNRESOLVED_NUMERICAL_EVIDENCE_SUPPORTS_SUBCRITICALITY
DEFECTIVE_MONODROMY_CAUTION = ACCEPTED_EXACT_CONTROLLED_FAILURE_MODE_ONLY

LOCAL_CLOCK_CHIRALITY = ACCEPTED_WITH_ASSUMPTION_FOR_DIRECT_CLOCK_CONTRIBUTION
SPONTANEOUS_CHIRALITY = UNRESOLVED_NOT_ESTABLISHED
FIXED_FREQUENCY_SU3_STRUCTURE = ACCEPTED_EXACT_CARRIED_FORWARD_WITH_MULTIPLICITY_CASES
LOCAL_CLOCK_SYMMETRY = ACCEPTED_WITH_ASSUMPTION_CONTINUOUS_COMMON_STRICTLY_MONOTONE_RATE

KNOWN_OSCILLATOR_EQUIVALENCE = ACCEPTED_EXACT_FOR_AFFINE_CLOCK_AND_K_ZERO_ONLY
NOVELTY_SCOPE = UNRESOLVED_NO_PRIORITY_CLAIM

PHYSICAL_FACE_OBSERVABLE = UNRESOLVED
PHYSICAL_TIME_SCALE = UNRESOLVED
EXTRA_RECURSIVE_STATE = UNRESOLVED_NOT_SPECIFIED_OR_ADDED
PHYSICAL_INTERPRETATION_READY = NO

READY_TO_FREEZE_PHASE_III = YES
READY_TO_MODIFY_KERNEL_PHYSICS = NO

KERNEL_PHYSICS_MODIFIED = NO
FROZEN_SOURCES_MODIFIED = NO
```
