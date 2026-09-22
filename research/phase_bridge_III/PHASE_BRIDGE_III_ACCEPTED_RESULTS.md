# Phase Bridge III — accepted results

Date: 2026-09-22. Baseline: `899d0fa900dc0d0ab8406e889908e47468d343db`.

This is the corrected research synthesis, read together with `PHASE_BRIDGE_III_CODEX_FINAL_REVIEW.md` and its execution record. It does not amend either preserved original report. “Accepted” means mathematical agreement under the explicit scopes below, including corrections independently required by their common equations. It does not mean every unqualified sentence in the two originals is retained.

The new focused verification passes **73/73 computed predicates**: 28 symbolic, 40 numerical, and 5 integrity checks. These are not counts of independent theorems. Analytic proofs, finite numerical evidence, and unresolved physical interpretation remain distinct. Earlier baseline identities are retained with their original hypotheses, without claiming this focused run retested all of them.

## 1. Coordinates, sign, and the continuous comparison field

**ACCEPTED_EXACT.** On each selected nonzero oriented coefficient plane,

\[
\Omega_i=q_i+ip_i=\sqrt{2I_i}e^{i\phi_i},\qquad
I_i=|\Omega_i|^2/2>0,\qquad
dq_i\wedge dp_i=dI_i\wedge d\phi_i.
\]

With \(\iota_X\sigma=dH\), \(\sigma=\sum_i dI_i\wedge d\phi_i\),
\(\dot I_i=\partial_{\phi_i}H\), \(\dot\phi_i=-\partial_{I_i}H\).
A prescribed local signed phase velocity \(\varpi_i(I_i)\) has radial Hamiltonian
\(-\sum_i\int^{I_i}\varpi_i(s)ds\). This term alone conserves the actions. A C1 multi-action rate law is locally realizable in this **fixed** form exactly when
\(\partial_{I_j}\varpi_i=\partial_{I_i}\varpi_j\); global realization additionally requires exactness. Positive action space supplies a simply connected domain for the usual closedness argument. No phase coordinate exists at zero amplitude.

**ACCEPTED_WITH_ASSUMPTION.** The specified Paper-A continuous parent, supplemented by a chosen local clock and continuous third-harmonic coefficient K, is

\[
\dot I_i=2\epsilon I_i(k_i-2I_i)-4gI_i+
2g\sum_{j\ne i}\sqrt{I_iI_j}\cos(\phi_j-\phi_i),
\]
\[
\dot\phi_i=g\sum_{j\ne i}\sqrt{I_j/I_i}\sin(\phi_j-\phi_i)
+K\sum_{j\ne i}\sin3(\phi_j-\phi_i)+\varpi_i.
\]

These are exact polar expressions for that **continuous** field on nonzero channels. They are not an implementation or a replacement of the frozen discrete map. The clocks, K, and physical units are supplied assumptions. A common phase-invariant clock disappears from a closed common-phase quotient; unequal local clocks can change relative phases, amplitude exchange, and the subsequent local rates. Geometry does not select harmonic 3 or a rate law.

## 2. H1: conditional embedding and integrability

**ACCEPTED_WITH_ASSUMPTION.** Consider the literal scalar field

\[
\dot\rho=\nu(1-\rho)S(\phi),\quad \dot\phi=v(\rho),\quad
S=\sin(E_0+A\sin\phi),\quad v=\omega+\kappa W(\rho).
\]

Where the C1 field is defined below rho=1, the real chart \(y=-\log(1-\rho)\) gives
\(\dot y=\nu S\), \(\dot\phi=v(1-e^{-y})\). Choosing \(I=I_*y\), \(I_*>0\), gives an exact canonical realization. Its unshifted positive-action encoding \(\Omega=\sqrt{2I}e^{i\phi}\) is restricted to `0<rho<1`; it neither identifies negative I with a squared complex amplitude nor extends invertibly to the boundary circles.

Define

\[
F'(\rho)=\frac{v(\rho)}{1-\rho},\quad U'(\phi)=S(\phi),\quad
Q=F(\rho)-\nu U(\phi),\quad m=\nu\int_0^{2\pi}S(\phi)d\phi.
\]

**ACCEPTED_EXACT.** Q is a first integral on the phase cover and \(H=-I_*Q\). Q and this H descend to single-valued functions on the phase cylinder when `m=0`; when `m!=0`, these particular primitives have nonzero monodromy. This is integrability of the specified two-dimensional field, not a prohibition on saddle exponents or on behavior in different discrete or augmented models.

### Integrating factors and scale

**ACCEPTED_EXACT.** For C1 G on the attained Q range,

\[
M=\frac{G(Q)}{1-\rho},\qquad\operatorname{div}(MX)=0,\qquad
\iota_X\left(Md\rho\wedge d\phi\right)=-G(Q)dQ.
\]

**ACCEPTED_WITH_ASSUMPTION.** This family is locally complete near a regular point: writing \(B=(1-\rho)M\) reduces the multiplier equation to \(XB=0\), so in a local regular flow box \(B=G(Q)\). An actual symplectic embedding requires G to be nowhere zero on the patch. Zero G satisfies the divergence identity but gives a degenerate form. Global completeness needs further level-set/domain hypotheses. For nonzero m, cylinder descent requires \(G(q-m)=G(q)\), and a Hamiltonian primitive need not descend even when the form does.

I-star scales the pair `(sigma,H)` together and leaves the scalar dynamics unchanged. It is not a transformation preserving a fixed sigma or a selected physical amplitude normalization. Geometry does not choose G or I-star.

### Return map and correct drift classification

**ACCEPTED_EXACT.** Where `v>0`, F is strictly increasing and, as long as the trajectory stays in the domain,

\[
F(\rho(\phi))=F(\rho_0)+\nu\int_{\phi_0}^{\phi}S(s)ds.
\]

Every completed turn translates F by m. The return map is the identity on its full-turn domain when `m=0`; nonzero m excludes interior periodic orbits in a strictly advancing flow.

**ACCEPTED_WITH_ASSUMPTION.** On the historical strip, suppose v is continuous and strictly positive on the closed interval `[0,1]`. Normalize `F(0)=0`; then `F(1-)=infinity`. First-turn survival in the open strip is exactly the condition

\[
F(\rho_0)+\nu\int_{\phi_0}^{\phi}S(s)ds>0
\quad\text{for the entire first turn}.
\]

* If `m=0`, surviving trajectories close, and the full-turn subset is foliated by closed orbits. Other initial points can encounter the lower boundary before returning.
* If `m>0`, surviving first-turn trajectories survive subsequent turns and tend to rho=1. Other initial points can exit first through rho=0.
* If `m<0`, trajectories reach the lower boundary in finite time. Continuation, clamping, or resetting there is not supplied by this interior analysis.

Thus the unrestricted historical-strip fate is not determined by mean sign alone: warp affects the survival criterion. If `nu*S>=0` everywhere and is not identically zero, the strip is forward invariant and every interior point tends to rho=1 under the stated clock bounds. This restricted conclusion is independent of warp shape; traversal rates and the boundary multiplier \(\exp[-m/v(1)]\) need not be. Identically zero forcing, including `nu=0`, instead gives constant-rho rotations. Merely positive v on a visited open range does not guarantee complete turns or `v(1)>0`.

## 3. Regular periodic orbits, commutators, and numerical shear

**ACCEPTED_EXACT.** Every nonstationary periodic orbit in a compact subset of the C1 domain rho<1 has two unit Floquet multipliers. Indeed
\(\operatorname{div}X=-\nu S=d\log(1-\rho)/dt\), so its full-period variational determinant is one, and the autonomous tangent solution supplies one unit multiplier. This includes an extension below zero only where W and the field have actually been defined there. It excludes equilibria and the rho=1 boundary. Unit multipliers allow Jordan shear and do not assert nonlinear stability.

The earlier commutator result is retained: for matrices
\(A_t=\left(\begin{smallmatrix}a_t&b_t\\c_t&0\end{smallmatrix}\right)\), pairwise commutation is equivalent to the triples `(a_t,b_t,c_t)` spanning dimension at most one. A triangular system is not automatically a commuting system. This is an algebraic statement about the specified matrices, not a general instability criterion.

**ACCEPTED_EXACT.** H1 with `S=0`, `v=1+rho`, `rho0=1/2` gives the exact monodromy

\[
M_0=\begin{pmatrix}1&0\\4\pi/3&1\end{pmatrix}.
\]

An error delta in the opposite off-diagonal entry changes its eigenvalues to
\(1\pm\sqrt{(4\pi/3)\delta}\). Controlled plus/minus float64-epsilon errors produce an approximately `3.05e-8` real or imaginary split while trace and determinant remain close to 2 and 1. This is sensitivity to matrix error, not proof that the eigensolver itself is wrong. Trace/determinant are useful diagnostics but do not certify exact multipliers. Combine analytic structure, entry/backward errors, invariant residuals, and numerical refinement. Nothing here explains any particular historical run.

## 4. Invariant lines, balance, and the general local-clock threshold

**ACCEPTED_WITH_ASSUMPTION.** For identical channel laws and equal real k, epsilon, g, K, the punctured complex lines

\[
\Omega_j=z,\qquad \Omega_j=z\zeta^{j-1},\qquad
\Omega_j=z\bar\zeta^{j-1},\quad j=1,2,3,\quad \zeta=e^{2\pi i/3},
\]

are invariant. They are two real dimensional. Their radial equations are
\(\dot r=r\epsilon(k-r^2)\) and \(\dot r=r[\epsilon(k-r^2)-3g]\), respectively; the common angular rate is \(\varpi(r^2/2)\). No origin extension of the full phase-dependent field is silently added.

**ACCEPTED_EXACT for the specified field.** With \(N=\sum I_i\),

\[
\dot N=2\epsilon\sum_i I_i(k-2I_i)
-g\sum_{i<j}|\Omega_i-\Omega_j|^2.
\]

At a common-phase relative equilibrium this equals zero. K and varpi are absent explicitly because their terms preserve amplitudes; they can still affect which state satisfies the balance. The equation is necessary, not sufficient, for a relative equilibrium.

**ACCEPTED_WITH_ASSUMPTION.** Let

\[
r^2=k-3g/\epsilon>0,\quad I_*=r^2/2,\quad
c=r^2\varpi'(I_*),\quad a=-2\epsilon r^2+3g/2,\quad d=3g/2-9K,
\]
\[
\tau=a+d,\qquad D=ad-9g^2/4.
\]

Assume a C1 common rate, `epsilon!=0`, `g!=0`, `tau<0`, `D>0`. The full characteristic polynomial at either splay ordering is exactly

\[
\lambda(\lambda+2\epsilon r^2)
\left[(\lambda^2-\tau\lambda+D)^2+9g^2c^2/4\right].
\]

The transverse stability threshold is

\[
\boxed{c_*^2=(a+d)^2\left(\frac{4ad}{9g^2}-1\right)}.
\]

Transverse roots are strictly stable below it, have a simple imaginary pair at it, and have an unstable pair above it. The critical frequency magnitude is \(\sqrt D\); in the quadratic with `+3igc/2`, its signed value is \(3gc/[2(a+d)]\). Full quotient stability also requires \(\epsilon r^2>0\). This is a stable-to-unstable threshold theorem, not an unconditional classification of every degenerate or already unstable case.

For `epsilon=g=K=1,k=6`, \(\varpi=1+\alpha(I-3/2)\),

\[
|\alpha_*|=4\sqrt{14},\qquad |\omega_*|=3\sqrt{14}/2,
\qquad \frac{d\Re\lambda}{d|\alpha|}=\frac{\sqrt{14}}{20}>0.
\]

Three further fixtures independently reproduce thresholds 8.0236490933, 18.3074646479, and 23.8078683561 for the parameter sets recorded in the review. The linear crossing theorem does not determine the nonlinear Hopf coefficient or criticality.

## 5. Nonlinear evidence and its limits

**NUMERICAL_OBSERVATION.** Six deterministic quotient fixtures were each integrated twice with refined tolerances. Three small perturbations of the splay branch at `alpha=threshold+0.05,+0.25,+1.0` departed and approached the in-phase branch. At `alpha=threshold-0.05`, the specified 0.01 perturbation returned to splay; the 0.2 perturbation reached in-phase. A small perturbation of in-phase returned there as well. The initial data are explicit in the verifier and JSON; these are independent fixtures, not an exact replay of unspecified Claude initial conditions.

The maximum discrepancy between the two integrations at 10,001 common sample times was approximately `4.782e-6` in action or relative phasor. Both tolerances agreed on all destinations. The small below-threshold perturbation approaches an oscillatory error envelope, making a tiny-error arrival time sensitive even when the trajectories agree. Arrival time is therefore recorded, not used as a proxy for trajectory agreement.

No small saturated modulation was observed in these runs. Both local basins below threshold also follow from the strictly stable quotient linearizations of the splay and in-phase branches. The observed basin destinations and finite non-observation of saturation are not a global attractor classification.

**UNRESOLVED.** The observations support subcriticality but do not prove it. No first Lyapunov coefficient, continuation of a small periodic branch, or basin-scaling theorem was computed. No assertion that the model has no other attractor is accepted.

## 6. Chirality and unitary symmetry retained with scope

**ACCEPTED_WITH_ASSUMPTION.** The direct clock contribution to
\(Z_i=\Im(\overline\Omega_j\Omega_k)\), with cyclic indices, is

\[
\dot Z_i|_{clock}=2\sqrt{I_jI_k}\cos(\phi_k-\phi_j)
(\varpi_k-\varpi_j).
\]

Unequal local rates can generate Z from an aligned state with unequal amplitudes. This is not proof of spontaneous handedness from a symmetric state or of a physical chiral observable. For
\(J_{eff}=\Im(\Omega_1\overline\Omega_2\Omega_3)\),

\[
\dot J_{eff}|_{clock}=(\varpi_1-\varpi_2+\varpi_3)
\Re(\Omega_1\overline\Omega_2\Omega_3).
\]

The fixed-frequency joint centralizers of L3 and a real diagonal frequency matrix retain the earlier multiplicity classification:

| Frequency multiplicity | Unitary joint centralizer | Special-unitary restriction |
|---|---|---|
| All equal | U(1) x U(2) | S(U(1) x U(2)) |
| Exactly two equal | U(1) x U(1) | U(1) |
| All distinct | Scalar U(1) | Z3 |

These are coefficient-space symmetries of fixed operators, not physical gauge identifications.

For identical strictly monotone local rates extending continuously to I=0, the pure local-clock field has unitary symmetry `U(1)^3 semidirect S3`. Intersecting with the L3 symmetry leaves common phase times permutation; its special-unitary part is the 18-element set \(\{\zeta^m(\det P)P\}\). The continuity assumption justifies the one-channel-limit argument. These are sufficient hypotheses for the retained theorem, not a claim that nonmonotonicity automatically produces extra global unitaries. Equal instantaneous frequencies at one state do not restore a global nonlinear U(2) symmetry.

## 7. Oscillator equivalence and physical boundary

**ACCEPTED_EXACT.** With `K=0` and affine \(\varpi(I)=\omega_0+\alpha I\), the field is exactly

\[
\dot\Omega_i=(\epsilon k+i\omega_0)\Omega_i
-(\epsilon-i\alpha/2)|\Omega_i|^2\Omega_i+g(L_3\Omega)_i,
\]

the cubic coupled nonisochronous oscillator / discrete complex Ginzburg–Landau form. For nonzero K it has an **additional third-harmonic phase-coupling term**. Its vanishing on special invariant lines does not remove its effect on transverse stability. No exact pure-cubic equivalence is asserted for the full K-nonzero model.

**UNRESOLVED.** A physical face measurement, physical frequency/time scale, and any extra independently evolving recursive state remain unspecified. No novelty or priority claim is established. The algebraic equivalence does not decide the status of the historical recursive programme, stored memory, SRG, discrete recursion, or future extensions. No physical law has been admitted into kernel_physics.

## 8. Preservation and freeze meaning

Both source reports retain their recorded SHA-256 hashes; all 63 baseline-tracked files are unchanged. The new files consist only of the copied review, this synthesis, the final Codex review, the focused verifier, and its two result files. The original Phase III report is retained unchanged alongside them. No commit, push, archive-metadata update, or kernel implementation was performed in this verification task.

The corrected statements are ready to freeze as conditional mathematical research. This includes explicit unresolved nonlinear and physical questions; it does not authorize implementation.

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
