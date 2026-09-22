# Phase Bridge III: recursive time in action–angle coordinates

Date: 2026-09-21. Prepared by Codex from the supplied Phase Bridge III work order. This is a new derivation report, not a Claude-authored report or an independent verification of an existing Phase Bridge III report.

Frozen repository baseline: **899d0fa900dc0d0ab8406e889908e47468d343db**.

**Result.** The tangent-plane construction admits exact polar action–angle coordinates. A radial Hamiltonian can realize a specified state-dependent phase rate, but by itself conserves the actions and therefore does not close an action–phase feedback loop. Adding the Paper-A continuous parent supplies phase-dependent amplitude coupling. A local clock can then alter stability; an explicit conditional three-channel example and its exact instability threshold are derived below.

The supplied historical scalar system also admits an exact conditional embedding: $I=I_\ast[-\log(1-\rho)]$, with an arbitrary positive scale $I_\ast$, on $0<\rho<1$. This preserves its feedback rather than replacing it by a radial oscillator. It makes a serious limitation visible: every regular periodic orbit contained in this interior has two unit Floquet multipliers. The historical commutator formula, vanishing lemma, and proposed sufficient instability thresholds cannot be adopted as written.

The physical face observable, the identification of historical $\rho$, and the physical time scale remain **UNRESOLVED**. No claim of physical novelty, unique reconstruction, or kernel admission follows.

## 1. Scope, sources, and classifications

The primary references are the repository's frozen [Paper A](../../papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md), especially §§1 and 6.1; [Paper C](../../papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md), especially §§2–4, 7 and 9; [Bridge I](../top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md), §§2–7; its [unresolved interface assumptions](../top_to_recursive_bridge/UNRESOLVED_INTERFACE_ASSUMPTIONS.md); and the [Bridge II Codex review](../phase_bridge_II/PHASE_BRIDGE_II_CODEX_REVIEW.md), §§1–6. The [Claude original](../phase_bridge_II/PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md) is read together with that review, whose corrections control this report. [CURRENT_STATE.md](../../CURRENT_STATE.md) records the freeze.

The existing geometry and dynamics Python files were read as definitions; they were not imported or executed. The shell remains a local component. This report supplies no global host, boundary conditions, extra quantum states, or historical SRG architecture.

The following five local PDFs are the entire historical source set used here. Page numbers below are PDF page numbers; these agree with the printed page numbers in the cited passages. Dates are the dates printed in the documents, not inferred chronology.

| ID | Local file, under C:/TORMENT/TRIOCTAGON_new/pdfs_quantum/ | Printed title / date | Pages |
|---|---|---|---:|
| H1 | Continuous_time_2.pdf | Continuous-Time Recursive Temporality and Analytical Bounds for Structured Symmetry Breaking; January 22, 2026 | 19 |
| H2 | symmetry_normalization_geometric_origin.pdf | Symmetry, Normalization, and the Geometric Origin of the Constants $1/\sqrt2$ and $1/2$; January 2026 | 19 |
| H3 | quantum_postulates.pdf | Coherence-Selection Dynamics: A Structural Reformulation of Quantum Mechanics; January 16, 2026 | 23 |
| H4 | Modal Structure and Stability in an SRG-Inspired.pdf | Modal Structure and Stability in an SRG-Inspired Recursive System; January 16, 2026 | 9 |
| H5 | A_structural_reconstruction_of_quantum_mechanics-1.pdf | A Structural Reconstruction of Quantum Mechanics: From Symmetry, Normalization, and Coherence Dynamics; January 22, 2026 | 19 |

Statement classifications are **EXACT**, **STANDARD_KNOWN_MATHEMATICS**, **DERIVED_FROM_STATED_ASSUMPTION**, **HISTORICALLY_INTENDED**, **SUPPORTED_NOVEL_STRUCTURE**, **POSSIBLY_NOVEL**, **CANDIDATE_PHYSICAL_INTERPRETATION**, **UNRESOLVED**, and **CONTRADICTED**. “EXACT” describes the stated mathematics, not its physical realization or priority. No finding is promoted to SUPPORTED_NOVEL_STRUCTURE as a literature-priority conclusion.

## 2. What the historical objects actually mean

This table separates literal source definitions from proposed modern identifications. Match labels apply to the stated mapping, not to the validity of an entire paper.

| Historical object and source | Source definition / intended meaning | Candidate modern object and limitation | Match |
|---|---|---|---|
| H1, p.3 §2; p.6 §10 | A scalar state $\rho\in[0,1]$, with $\dot\rho=\nu(1-\rho)\sin(E_0+A\sin\phi)$. No face field, unit, or measurement operator is supplied. | An additional scalar, or a deliberately constructed function of a face action. Neither is selected physically. | POSSIBLE_MATCH |
| H1, pp.3–4 §§2–4 | $\dot\phi=\omega+\kappa W(\rho)$; $\kappa W'(\rho)\delta\rho$ changes the clock rate. | A state-dependent angular rate of a nonzero tangent-vector coefficient. | STRUCTURAL_MATCH |
| H1, p.3 §3 | Smooth bounded warp families, including $\tanh[\alpha(\rho-\rho_0)]/\tanh\alpha$. | An assumed constitutive frequency function; no geometric selection of its shape or steepness. | POSSIBLE_MATCH |
| H1's two equations under the chart proved in §8 below | $I=I_\ast[-\log(1-\rho)]$, $\Omega=\sqrt{2I}e^{i\phi}$, restricted to $0<\rho<1$. | Exactly the same scalar dynamics in one modern symplectic plane, conditional on this chosen encoding and scale. | EXACT_MATCH |
| H2, pp.2–6 §§1–2; pp.11–14 §§5–6 | Normalized coefficients, symmetric magnitudes, squared weights; wave intensity is assigned a squared-amplitude meaning. | $I_i/\sum_j I_j$ could be a normalized weight. Paper A does not normalize its state; a probabilistic or intensity interpretation is additional. | POSSIBLE_MATCH |
| H2, pp.16–17 §7 | A coherence functional $C$, gradient selection, and skew-gradient conservative transport. | Paper A's gradient parent and Bridge II's Hamiltonian geometry supply related mathematical structures, not the same specified functional. | STRUCTURAL_MATCH |
| H3, p.4 §§2.2–2.4 | General configurations $s$, or normalized $\psi$ in a quantum specialization; self-adjoint observables; $C=-E$ as a constraint score and a threshold $C\geq\theta$. | A Hermitian quadratic on the three complex coefficients could be defined. No supplied source identifies a particular face measurement or establishes its physical units. | POSSIBLE_MATCH |
| H3, p.9 §2.11.1 | $\rho$ is a positive trace-one **density operator**. | This operator is not H1's scalar clock state and not a face action. | NO_MATCH |
| H3, pp.16–17 §2.14 | A specified complex structure generates $e^{\alpha J}$; invariant $C$ gives an equivariant flow. | The oriented tangent-plane $J$ gives this same algebra, with a separately supplied invariant functional. | STRUCTURAL_MATCH |
| H3, pp.18–20 Lemmas 2.5, 2.7, 2.9 | Two parameters $t,\tau$, an assumed fixed ratio $r=d\tau/dt$, mixed gradient/skew-gradient flow, and scalar-Hessian rotation/envelope modes. | This preserves an intended two-flow interpretation; it is not automatically the state-dependent clock of H1. | ANALOGY_ONLY |
| H4, pp.2–5 §§1–2.2 | $X_t\in\mathbb R^N$, filtered memory $M_{t+1}=\rho M_t+(1-\rho)X_t$, and $2\times2$ modal blocks. Here $\rho$ is a fixed memory-retention parameter. | Genuine extra memory coordinates would enlarge the state. They cannot be silently identified with $I$, with H1's dynamic $\rho$, or with three selected tangent fibers. | NO_MATCH |
| H4, pp.3–5 | Complex modal eigenvalues supply oscillatory real planes; a near-identity limit supplies a continuous generator. | This can support phase planes after an operator and modes are specified; the shell does not supply that historical memory operator. | STRUCTURAL_MATCH |
| H5, pp.3–6 §§4–6 | Normalized Hilbert states, projector probabilities, and continuous **linear** norm-preserving evolution; §6.2 states a real-gradient convention. | A possible later measurement model. State-dependent nonlinear phase rates do not satisfy the linear-group premise automatically. | POSSIBLE_MATCH |
| H5, pp.17–19 §13 | Intrinsic phase transformations motivated by recursive time, skew generators, phase planes, and a universality premise. | Bridge I supplies the geometric complex structure and already distinguishes the strong universal-vector hypothesis from merely spanning by phase planes. | STRUCTURAL_MATCH |
| H5, p.19 closing paragraph | Historical toy models are said to exhibit phase locking and finite-time chirality selection. | This is a historical research claim, not a supplied observable definition, trajectory, or verification of the present model. | ANALOGY_ONLY |

**HISTORICALLY_INTENDED.** The source meanings include structural consistency, persistence/selection, conservative transport, filtered history, and state-dependent temporal phase. Those intentions remain in the record. They are different constructions; this report does not discard them or identify them by terminology alone.

Three applicability qualifications matter for this bridge:

1. Equal coefficients plus normalization give equal squared weights. An exchange-invariant equation or a flat energy alone does not force every state to be exchange-invariant. Thus H2 does not derive a unique action or observable for the three faces.
2. Skewness conserves the generating functional, not every other quadratic. For $J(q,p)=(-p,q)$, $C=q$ gives $J\nabla C=(0,1)$, whose norm is not constant along a general trajectory. The phase-invariance premise stated later in H3 is needed for norm conservation. H3's earlier energy-sign arithmetic is not imported; Bridge II's convention and H5 §6.2's explicit real-gradient convention keep those choices distinct.
3. A jointly defined two-time solution $s_t=X(s),s_\tau=Y(s)$ requires $DX\,Y=DY\,X$ along it when mixed derivatives exist. The ray chain rule in H3 is conditional on such a solution. A mixed ODE $X+rY$ may be defined even when no compatible two-time surface exists. No two-time integrability is assumed here.

**UNRESOLVED.** None of these five sources derives a measurement map from an actual Paper-C face to its tangent vector. The exact conditional chart in §8 answers a mathematical realization question; it does not settle that physical interface.

## 3. Exact action–angle coordinates and the zero set

**EXACT.** Retain the frozen frame $v_i=q_i t_i+p_i e_z$, $J_i t_i=e_z$, $J_i e_z=-t_i$, and $\Omega_i=q_i+ip_i$. Write the symplectic form as $\sigma$ in this report to avoid confusing it with a frequency:

$$
\sigma=\sum_i dq_i\wedge dp_i,\qquad \iota_{X_H}\sigma=dH.
$$

On $\mathcal D=(\mathbb C\setminus\{0\})^3$, define

$$
I_i=\frac{q_i^2+p_i^2}{2}>0,\qquad
\phi_i\in\mathbb R/(2\pi\mathbb Z),\qquad
q_i=\sqrt{2I_i}\cos\phi_i,\quad p_i=\sqrt{2I_i}\sin\phi_i.
$$

For one channel, putting $r=\sqrt{2I}$,

$$
dq=\frac{\cos\phi}{r}\,dI-r\sin\phi\,d\phi,\qquad
dp=\frac{\sin\phi}{r}\,dI+r\cos\phi\,d\phi.
$$

Their wedge product is $(\cos^2\phi+\sin^2\phi)dI\wedge d\phi$. Therefore

$$
\boxed{\sigma=\sum_i dI_i\wedge d\phi_i.}
$$

Contraction, $\iota_X\sigma=\sum_i(\dot I_i\,d\phi_i-\dot\phi_i\,dI_i)$, gives

$$
\boxed{\dot I_i=\partial_{\phi_i}H,\qquad
\dot\phi_i=-\partial_{I_i}H.}
$$

In particular $H=\sum_i\nu_i I_i$ gives $\dot\phi_i=-\nu_i$, agreeing with $\dot\Omega_i=-i\nu_i\Omega_i$. We denote a **positive signed phase velocity** by $\varpi_i=\dot\phi_i$; thus the frequency symbol in $-i\nu_i\Omega_i$ satisfies $\nu_i=-\varpi_i$.

These are global coordinates with circle-valued angles, not a single global real-valued Arg. The one-form $d\phi=(q\,dp-p\,dq)/(q^2+p^2)$ is well defined on the punctured plane. The coordinates are exact polar area coordinates; calling $I$ an action does not imply it is conserved for an arbitrary $H$.

At $I_i=0$ the circle collapses to the origin and its phase is undefined. A stratum with $m$ zero complex coordinates has real codimension $2m$. The Cartesian form remains nonsingular; the polar chart does not. Coupling can carry a trajectory through a zero, so statements on $\mathcal D$ hold only up to such an exit unless an independent extension is supplied. A smooth radial frequency has a smooth Cartesian rotation field at zero; the phase-only neighbor term need not.

Paper A's $\operatorname{Arg}_0(0)=0$ makes its **discrete** map defined there; it does not repair this coordinate singularity or furnish a smooth continuous phase field. Its direct $\lambda=0$ branch and all frozen definitions remain unchanged.

## 4. Which Hamiltonians realize a recursive phase law?

### 4.1 Local action dependence

**DERIVED_FROM_STATED_ASSUMPTION.** Suppose a model explicitly chooses $\rho_i=r_i(I_i)$ and smooth functions $W_i$, with

$$
\varpi_i(I_i)=\omega_i^{(0)}+\kappa W_i(r_i(I_i)).
$$

The entire family of angle-independent Hamiltonians producing these rates on a connected action domain is

$$
\boxed{
H(I)=-\sum_i\left[\omega_i^{(0)}I_i+
\kappa\int^{I_i}W_i(r_i(s))\,ds\right]+C.}
$$

Differentiation proves both the sign and the rate. The work order's proposed minus sign is correct. Adding any $G(\phi)$ leaves the phase law unchanged but adds $\dot I_i=\partial_{\phi_i}G$. With no such term, $\dot I=0$: there is action-dependent frequency and shear between trajectories, but no return arrow from phase to action.

Neither positivity of $H$, the choice of $W$, nor a physical energy interpretation follows. A positive quadratic corresponds to negative signed phase velocity under the frozen convention.

### 4.2 Coupled actions and a shared rate

**EXACT.** For prescribed angle-independent $\varpi_i(I)$, a Hamiltonian exists locally exactly when

$$
\partial_{I_j}\varpi_i=\partial_{I_i}\varpi_j.
$$

Indeed the one-form $\alpha=\sum_i\varpi_i\,dI_i$ must be exact, with $H=-\int\alpha+G(\phi)$. On the positive action orthant closedness is also sufficient globally, since it is simply connected. On other domains exactness must be checked separately.

If every $\varpi_i=w(I)$, closedness says that all three partial derivatives of $w$ agree. Locally $w=f(N)$, $N=\sum I_i$; on the full positive orthant the connected constant-$N$ slices give the same global conclusion. The corresponding Hamiltonian is $-\int^N f(s)\,ds+G(\phi)$.

A scalar frequency shared by all channels is therefore not automatically Hamiltonian merely because its instantaneous matrix is scalar. For example $w=\sum I_i^2$ has unequal action derivatives away from the equal-action locus. Similarly, choosing local normalized weights $\rho_i=I_i/N$ and $W(\rho)=\rho$ gives cross derivatives $-I_i/N^2$ and $-I_j/N^2$, generally unequal. Smooth phase rotation, symplectic flow, and Hamiltonian flow are distinct requirements.

### 4.3 An independent $\rho$ variable

**EXACT, with typing qualification.** If $\rho$ is held as an external parameter and the specified $\varpi_i(\rho)$ have no $I$ dependence, the most general Hamiltonian producing the phase law in the $(I,\phi)$ variables is

$$
H(I,\phi;\rho)=-\sum_i I_i\varpi_i(\rho)+G(\phi,\rho).
$$

For the angle-independent ansatz $H(I,\rho)$, replace $G$ by $C(\rho)$. If $\rho$ is itself dynamical, this expression does not give its evolution: a symplectic extension, a Poisson structure, or an explicitly non-Hamiltonian auxiliary law must be supplied. A prescribed $\rho(t)$ gives a time-dependent Hamiltonian, not a closed autonomous reconstruction.

Nor may one differentiate at fixed $\rho$ and then substitute $\rho=r(I)$ without including the chain rule. The pullback Hamiltonian must satisfy the total action-derivative condition of §4.2. If $\rho$ depends also on phase, that condition is imposed at fixed phase and the induced action dynamics must be retained.

For a completely specified field $(\dot I,\dot\phi)=(F,\varpi)$, Hamiltonian realization in this fixed form requires the one-form

$$
\beta=\sum_i(F_i\,d\phi_i-\varpi_i\,dI_i)
$$

to be exact. Closedness includes symmetry of the action derivatives of $\varpi$, symmetry of the phase derivatives of $F$, and
$\partial_{I_j}F_i=-\partial_{\phi_i}\varpi_j$.
The Paper-A dissipative amplitude field does not generically meet these conditions.

### 4.4 What can coordinates remove?

**STANDARD_KNOWN_MATHEMATICS.** A single radial Hamiltonian with constant action is an integrable nonlinear oscillator. On an unwrapped angle patch a canonical transformation can locally flatten a nonzero frequency: take $J=f(I)$, $\psi=\phi/f'(I)$, so $dJ\wedge d\psi=dI\wedge d\phi$, and choose $f$ proportional to $H$.

This is not generally a global circle-coordinate change. A degree-one angle diffeomorphism with that constant-in-angle scaling requires $f'(I)=1$ (or $-1$ for the reversed circle orientation). More generally a time-preserving conjugacy must preserve orbit periods. A family with $T(I)=2\pi/|\varpi(I)|$ varying with action cannot become a common-frequency family by such a global conjugacy.

A time-dependent transformation using the integrable flow can remove that free flow, but changes the representation of couplings and measured phases. A state-dependent time rescaling $d\tau/dt=\varpi(I)/\varpi_\ast$, where positive, changes elapsed time and all the other rates. It is neither a common laboratory time coordinate for unequal channels nor a proof of observational equivalence.

Thus non-removability under specified physical coordinates/time is meaningful, but it is not itself evidence of a new dynamical class. The historic feedback is tested more precisely in §§8–11.

## 5. Shared, local, and mixed clocks

Let $A_0(\Omega)$ denote the nonrecursive continuous field, including any phase synchronization under discussion, on its smooth nonzero domain.

**EXACT — shared term.** Suppose $A_0(e^{i\alpha}\Omega)=e^{i\alpha}A_0(\Omega)$ and

$$
\dot\Omega=A_0(\Omega)+i w(\rho_{\rm shared})\Omega.
$$

With the work order's convention $\Omega=e^{-i\Theta(t)}\Psi$, substitution gives

$$
\dot\Psi=A_0(\Psi)+i\,[w+\dot\Theta]\Psi.
$$

Choosing $\dot\Theta=-w$ along the trajectory removes the shared term. If $\rho_{\rm shared}$ is phase-invariant, or an auxiliary state with phase-equivariant dynamics, the reduced equations close without the common phase. Invariant observables then have exactly the same evolution at the same $t$. This is removal of a vertical common-phase drift, not rescaling of time.

Examples of invariant observables are $I_i$, $\overline\Omega_i\Omega_j$, relative phases, and $Z_{\rm chiral}$. A phase against a supplied external reference, $\Re\Omega_i$, the literal $J_{\rm eff}$, injection by a fixed complex drive, or feedback using absolute phase need not be invariant. Declaring one of them physically measured requires evidence; $J_{\rm eff}$'s algebraic non-invariance alone does not provide that evidence.

Even a phase-dependent shared vertical rate leaves an autonomous quotient field unchanged if it has no other influence on that quotient. However, auxiliary equations or readouts depending on absolute phase can prevent the **joint** quotient dynamics from closing. H1 explicitly has $f(\rho,\phi)$ depending on its absolute clock phase. Rotating this phase away reintroduces it in $f$; the shared-clock invisibility theorem does not apply to that historical scalar feedback system.

**EXACT — local terms.** For $\varpi_i=\omega_0+\kappa W(\rho_i)$,

$$
\frac{d}{dt}(\phi_i-\phi_j)\big|_{\rm clock}
=\kappa[W(\rho_i)-W(\rho_j)].
$$

Unequal $\rho$ gives unequal rates only if $W$ distinguishes the two values. Injectivity is sufficient; unequal states by themselves are not. If all $\rho_i$ are constants of motion, this is constant detuning on each invariant action level. If they evolve through phase-sensitive coupling, the return arrow closes and the effect is not reproduced by fixed detuning for a neighborhood of initial states.

Separate rotating frames move unequal rates into the coupling: the coefficient multiplying a transported $\Psi_j$ contains $e^{i(\Theta_i-\Theta_j)}$. The effect has been relocated, not removed from the coupled system.

**DERIVED_FROM_STATED_ASSUMPTION — mixed terms.** A model may set
$\varpi_i=w_{\rm common}(\rho_{\rm global})+w_{\rm local}(\rho_i)$.
Only the common part cancels in relative phases. H1 supplies one scalar clock; it does not select three local clocks, a shared three-channel clock, or this mixed extension. No option is preferred on provenance grounds here.

## 6. The exact Paper-A continuous parent in these coordinates

**EXACT.** Write $\delta_{ji}=\phi_j-\phi_i$, $r_i=\sqrt{2I_i}$, with real $\varepsilon,g,k_i$. Directly from
$\dot I_i=\Re(\overline\Omega_i\dot\Omega_i)$ and
$\dot\phi_i=\Im(\overline\Omega_i\dot\Omega_i)/(2I_i)$, the pre-sync parent yields

$$
F_i:=\dot I_i
=2\varepsilon I_i(k_i-2I_i)
-4gI_i+2g\sum_{j\ne i}\sqrt{I_iI_j}\cos\delta_{ji},
\tag{6.1}
$$

$$
\dot\phi_i\big|_{\rm presync}
=g\sum_{j\ne i}\sqrt{\frac{I_j}{I_i}}\sin\delta_{ji}.
\tag{6.2}
$$

The diagonal $-2\Omega_i$ contributes to amplitude only. The coefficients $2$ and $4$ in (6.1) follow from the action definition and are not freely adjustable.

**DERIVED_FROM_STATED_ASSUMPTION.** Adding the independently reviewed continuous third-harmonic term, and a chosen intrinsic rate, gives the comparison system

$$
\boxed{
\begin{aligned}
\dot I_i&=F_i(I,\phi),\\
\dot\phi_i&=
g\sum_{j\ne i}\sqrt{I_j/I_i}\sin\delta_{ji}
+K\sum_{j\ne i}\sin(3\delta_{ji})+\varpi_i.
\end{aligned}}
\tag{6.3}
$$

The four contributions are now explicit: local amplitude growth, first-harmonic amplitude/phase exchange through $L_3$, amplitude-preserving third-harmonic synchronization, and amplitude-preserving intrinsic rotation. Only the first two are the pre-sync parent; $K$ is a continuous comparison coefficient, and $\varpi$ is newly supplied. Equation (6.3) is not the frozen discrete map and not a new implementation.

At the differential level, for $j\ne i$,

$$
\partial_{\phi_j}F_i=-2g\sqrt{I_iI_j}\sin\delta_{ji},\qquad
\partial_{I_j}F_i=g\sqrt{I_i/I_j}\cos\delta_{ji}.
$$

The diagonal derivatives are

$$
\partial_{\phi_i}F_i=2g\sum_{j\ne i}\sqrt{I_iI_j}\sin\delta_{ji},\quad
\partial_{I_i}F_i=2\varepsilon(k_i-4I_i)-4g+
g\sum_{j\ne i}\sqrt{I_j/I_i}\cos\delta_{ji}.
$$

When $\varpi_i=\varpi_i(I_i)$, the phase-action block acquires
$\delta_{ij}\varpi_i'(I_i)$. Its coupling entries are
$g\sin\delta_{ji}/(2\sqrt{I_iI_j})$ off diagonal and
$-g\sum_{j\ne i}\sqrt{I_j/I_i}\sin\delta_{ji}/(2I_i)$ on the diagonal.
The phase-phase block has off-diagonal entries
$g\sqrt{I_j/I_i}\cos\delta_{ji}+3K\cos3\delta_{ji}$
and diagonal minus their row sum.

This proves the conditional loop
$I\longrightarrow\varpi(I)\longrightarrow\delta\longrightarrow F(I,\delta)\longrightarrow I$.
It can vanish at particular states or parameters; for example $g=0$ removes the return arrow in (6.3), and in-phase states have $\partial_\phi F=0$ at first order. Dependence of $\rho$ on other variables requires those derivatives and variables explicitly.

The total action obeys the useful consistency identity

$$
\frac{d}{dt}\sum_i I_i
=2\varepsilon\sum_i I_i(k_i-2I_i)
-g\sum_{i<j}|\Omega_i-\Omega_j|^2.
$$

Neither phase term contributes directly. There is no imposed normalization or conservation of total action.

## 7. Corrected third-harmonic classes and what recursion can change

### 7.1 The phase-only baseline

**EXACT, inherited with its hypotheses.** For identical constant intrinsic rates, no amplitude coupling, and $K\ne0$, let $\theta_i=3\phi_i$. After removing common drift the three phase-only classes and transverse eigenvalues are:

| Class in $\theta$ | Eigenvalues transverse to common phase | $K>0$ | Labelled relative branches in $\phi$ |
|---|---|---|---:|
| Synchronized $\theta$ | $-9K,-9K$ | attracting | 9 |
| Antipodal $2+1$ | $-3K,9K$ | saddle | 27 |
| Equilateral $\theta$-splay | $9K/2,9K/2$ | repelling | 18 |

For $K<0$ the first and third stability types exchange; the middle remains a saddle. Every class has a neutral common-phase direction. At $K=0$ the isolated relative-class classification is inapplicable. The familiar $\phi$ differences $0,\pm2\pi/3$ are among the **synchronized $\theta$** branches, not the equilateral $\theta$-splay class. The Jacobian is $3K\cos3\delta_{ji}$ off diagonal, with zero row sums.

A shared phase-invariant clock alone leaves these relative equations and their stability unchanged. With fixed local detunings, the common locked rate is $\overline\varpi=(\sum_i\varpi_i)/3$, and the locking equations become

$$
0=\varpi_i-\overline\varpi+K\sum_{j\ne i}\sin3\delta_{ji}.
$$

The old classes are exact solutions only when these equations still hold. Necessarily
$|\varpi_i-\overline\varpi|\le2|K|$, not a sufficient condition. For sufficiently small constant detuning, each nondegenerate quotient equilibrium continues by the implicit-function theorem; stability types persist until an eigenvalue reaches the imaginary axis. For variable actions the full block Jacobian, not the phase-only table, determines stability.

Geometry still does not select harmonic three.

### 7.2 A case in which local feedback does not destabilize synchrony

**DERIVED_FROM_STATED_ASSUMPTION.** Let $k_i=k>0$, $\varepsilon>0$, and use the same smooth $\varpi(I)$ in all channels of (6.3). At the in-phase orbit $I_i=k/2$, the linearization has action block
$-2\varepsilon k\,\mathbf1+gL_3$, zero phase-to-action block, and phase block $(g+3K)L_3$. The frequency slope enters only the lower-left block.

Hence its eigenvalues are

$$
-2\varepsilon k,\quad -2\varepsilon k-3g\ \text{(twice)},\quad
0,\quad -3g-9K\ \text{(twice)}.
$$

For positive $g,K$ the orbit remains locally attracting modulo common phase for every finite slope $\varpi'(k/2)$. The slope may create transient shear, but cannot change these eigenvalues. This directly falsifies a universal claim that steep local recursive frequency necessarily destroys synchrony.

### 7.3 A case in which the local frequency slope changes stability

**DERIVED_FROM_STATED_ASSUMPTION — an analytic conditional example, not an executed experiment.** Consider equal $k$, $\varepsilon>0$, and

$$
\Omega_i=r\,e^{i(\varpi_\ast t+\theta_i)},\quad
\theta=(0,2\pi/3,4\pi/3),\quad
r^2=k-3g/\varepsilon>0,\quad
\varpi(I_\ast^{\rm orb})=\varpi_\ast,\quad I_\ast^{\rm orb}=r^2/2.
$$

This is an exact relative equilibrium of (6.3). The conjugate phase ordering gives another. Let $x_i=\delta r_i/r$, $y_i=\delta\phi_i$, and define the real skew matrix
$S_{ij}=\sin(\theta_j-\theta_i)$, including its zero diagonal.
It annihilates the balanced vector and has eigenvalues $\pm3i/2$ on its complex transverse modes; $S^2=-(9/4)P_\perp$.

Direct differentiation gives

$$
\frac{d}{dt}\binom{x}{y}=
\begin{pmatrix}
-2\varepsilon r^2\mathbf1-\frac g2L_3&-gS\\
c\mathbf1+gS&(-g/2+3K)L_3
\end{pmatrix}\binom{x}{y},\qquad c=r^2\varpi'(r^2/2).
\tag{7.1}
$$

For either transverse eigenvalue $s=\pm3i/2$, put
$a=-2\varepsilon r^2+3g/2$, $d=3g/2-9K$.
The characteristic equation is

$$
(\lambda-a)(\lambda-d)-9g^2/4+gc\,s=0.
\tag{7.2}
$$

As a fully specified algebraic witness choose
$\varepsilon=g=K=1$, $k=6$, $r^2=3$, and
$\varpi(I)=1+\alpha(I-3/2)$.
Then the balanced eigenvalues are $-6,0$, and the four transverse eigenvalues solve the conjugate pair of equations

$$
\lambda^2+12\lambda+\frac{63}{2}\ \pm\frac{9i}{2}\alpha=0.
$$

Equivalently they are $-6\pm\sqrt{(9/2)(1\pm i\alpha)}$. A square root has positive real part exceeding six exactly when
$\sqrt{1+\alpha^2}>15$. Thus

$$
|\alpha|<4\sqrt{14}:\ \text{strict transverse linear stability},\qquad
|\alpha|>4\sqrt{14}:\ \text{linear instability}.
$$

At equality a conjugate pair is purely imaginary, with frequency $3\sqrt{14}/2$; nonlinear stability is unresolved there. If $\varpi_\ast=1$, the laboratory orbit has period $2\pi$, so its variational multipliers are $e^{2\pi\lambda}$. The rotating-frame transformation is periodic and preserves these multipliers.

Every value of $\alpha$ in this comparison has the same actions, geometry, and intrinsic rate **on the orbit**. Only the off-orbit frequency slope changes. A fixed-detuning replacement matching the orbit therefore misses the stability change. Both chiral orderings have the same spectrum. The example proves neither a preferred chirality nor hysteresis, new attractors, or a nondegenerate Hopf bifurcation. Those require further specified-model analysis.

This affine-rate example is also an explicitly recognizable nonisochronous cubic-oscillator term plus the retained third-harmonic interaction. Its exact calculation is evidence of a conditional feedback effect, not evidence of an unprecedented mechanism.

## 8. Reconstructing H1 without inventing its state variable

### 8.1 Literal equations and domain

**HISTORICALLY_INTENDED.** H1, pp.3 and 6, specifies

$$
\dot\rho=\nu(1-\rho)S(\phi),\qquad
\dot\phi=v(\rho):=\omega+\kappa W(\rho),\qquad
S(\phi)=\sin(E_0+A\sin\phi).
\tag{8.1}
$$

Here H1's $\nu$ is its amplitude-evolution coefficient, not automatically Bridge II's Hamiltonian frequency. Its $\rho$ is a scalar, not a density operator, action, radius, memory coefficient, or a previously derived physical field.

**EXACT — a domain qualification.** The upper boundary $\rho=1$ is invariant, but the lower boundary $\rho=0$ has velocity $\nu S(\phi)$. If that quantity is negative for an allowed phase, the asserted interval $[0,1]$ is not forward invariant. A sufficient inward-pointing condition is $\nu S(\phi)\ge0$ at every phase. No clipping, reflection, or corrected state law is silently introduced. Subsequent interior statements hold while the trajectory stays in the stated domain.

### 8.2 An exact conditional canonical realization

**EXACT — mathematical coordinate construction.** On $\rho<1$, set

$$
y=-\log(1-\rho),\qquad
\dot y=\nu S(\phi),\qquad
\dot\phi=v(1-e^{-y}).
\tag{8.2}
$$

This follows from $\dot y=\dot\rho/(1-\rho)$. The transformed field has zero divergence in $(y,\phi)$, and preserves

$$
dy\wedge d\phi=\frac{d\rho\wedge d\phi}{1-\rho}.
$$

For any chosen $I_\ast>0$, take

$$
I=I_\ast y,\qquad
\rho=1-e^{-I/I_\ast},\qquad
\Omega=\sqrt{2I}\,e^{i\phi},\qquad 0<\rho<1.
\tag{8.3}
$$

Then $I>0$ and the standard tangent-plane form is exactly
$dI\wedge d\phi=I_\ast d\rho\wedge d\phi/(1-\rho)$.
Writing $U'(\phi)=S(\phi)$, the Hamiltonian

$$
\boxed{
H_{\rm hist}(I,\phi)
=-\int^{I}v(1-e^{-s/I_\ast})\,ds+\nu I_\ast U(\phi)}
\tag{8.4}
$$

gives
$\dot I=\nu I_\ast S(\phi)$ and
$\dot\phi=v(1-e^{-I/I_\ast})$.
Substitution into $\dot\rho=e^{-I/I_\ast}\dot I/I_\ast$ proves exact recovery of (8.1).

This is a rigorous example of how the historical feedback can live in a modern symplectic plane. Its Hamiltonian has a phase-dependent term, which preserves the return arrow absent from the purely radial construction in §4. It is not an identification guessed from quantum amplitudes.

The limitations are essential:

- The positive scale $I_\ast$, and the assignment of this scalar system to a physical face, remain choices. Geometry does not select them. The invariant area factor motivates this chart but does not uniquely select a physical symplectic measure or exclude other integrating factors.
- Since $\phi$ is real in H1, (8.4) is defined on its unwrapped phase cover. It descends to a single-valued Hamiltonian on the modern phase cylinder exactly when
  $\nu\int_0^{2\pi}S(\phi)\,d\phi=0$.
  Otherwise the vector field still descends and is symplectic there, but its Hamiltonian is only local/multivalued. The one-form $\iota_X\sigma$ has nonzero integral around the phase circle.
- The inverse map is an exact cylinder-to-punctured-plane identification for $0<\rho<1$. At $\rho=0$, the historical boundary circle would collapse to $I=0$; it is not an invertible extension. At $\rho=1$, $I$ diverges. The phase-dependent Hamiltonian is not thereby a smooth Cartesian Hamiltonian at $\Omega=0$.
- The historical field is not the Paper-A amplitude parent: its action law is $\nu I_\ast S(\phi)$, not (6.1). Assigning three copies would specify three extra modeled channel laws, not derive the frozen law.

**CANDIDATE_PHYSICAL_INTERPRETATION / UNRESOLVED.** Equation (8.3) is an exact mathematical encoding if it is chosen. It does not show that the physical observable is logarithmic saturation, that $\rho$ measures energy, or that the tangent-vector norm has the historical interpretation. Its physical match remains open.

For comparison, a proposed identification $\rho=r(I)$ must satisfy the pushforward identity
$r'(I)\dot I=f(r(I),\phi)$.
The isolated Paper-A amplitude parent has an angle-independent $\dot I$, while H1 generally has angle-dependent $f$. No nonconstant radial identification makes those isolated equations identical for all phases. More generally, a phase-invariant action observable pushed forward by the common-phase-equivariant Paper-A parent cannot acquire H1's absolute-phase dependence without an additional reference or a redefinition of that phase as a relative phase.

### 8.3 Exact first integral, return map, and Floquet obstruction

**EXACT.** On an interval with $\rho<1$, define

$$
F(\rho)=\int^\rho\frac{v(s)}{1-s}\,ds,\qquad U'(\phi)=S(\phi).
$$

Along (8.1),

$$
\frac{d}{dt}\,[F(\rho)-\nu U(\phi)]
=\frac{v(\rho)}{1-\rho}\nu(1-\rho)S(\phi)
-\nu S(\phi)v(\rho)=0.
\tag{8.5}
$$

When $v>0$ and a trajectory completes a full phase turn within the interval, its exact Poincaré map $\mathcal P$ obeys

$$
F(\mathcal P(\rho_0))=F(\rho_0)+\nu\int_0^{2\pi}S(\phi)\,d\phi.
\tag{8.6}
$$

Here $F'>0$. If the integral vanishes, the return map is the identity wherever the full turn exists. If the integral is nonzero, there is no interior fixed point of that return map. In H1's notation its Fourier expansion gives
$\langle S\rangle=\sin E_0\,J_0(A)$; the return-map conclusion needs only the integral, not the Bessel representation.

A stronger local Floquet statement does not require $v>0$. Let an actual **regular periodic orbit** stay in a compact subset of $\rho<1$, with the state and phase modulo $2\pi$ returning after $T$. The transformed field (8.2) has divergence zero, so its variational determinant is one. Because the orbit is a nonstationary solution of an autonomous system, its velocity is a nonzero periodic variational solution; one multiplier is one. The other is therefore one as well. The coordinate derivative is periodic and bounded with bounded inverse on that orbit, so the same multipliers hold in $(\rho,\phi)$.

Equivalently, directly in the original variables,

$$
\operatorname{div}X=-\nu S(\phi)
=\frac{d}{dt}\log(1-\rho),
$$

whose integral over any such periodic orbit is zero.

$$
\boxed{\mu_1=\mu_2=1\quad\text{on every regular interior periodic orbit of (8.1).}}
\tag{8.7}
$$

A nontrivial Jordan block can still produce linear shear, and finite-time amplification can occur. Equation (8.7) does not claim nonlinear Lyapunov stability of every orbit. It does rule out a positive Floquet exponent of those periodic orbits. Regular compact bands of rotating periodic orbits similarly permit bounded or shear-like variational growth rather than a positive asymptotic exponent; singular limits and equilibria require separate treatment.

The boundary $\rho=1$ is not covered by the logarithmic chart. If $v(1)\ne0$, it is a periodic boundary orbit with period $T=2\pi/|v(1)|$. Its multipliers are

$$
1,\qquad \exp[-\nu T\langle S\rangle].
$$

That exponent is determined by the signed mean, not by a claim that a nonzero commutator creates instability. At equilibria with $v(\rho_\ast)=0$ and $S(\phi_\ast)=0$, the interior Jacobian has eigenvalues
$\pm\sqrt{\kappa\nu(1-\rho_\ast)W'(\rho_\ast)S'(\phi_\ast)}$.
A positive product gives a saddle. This is a different mechanism and lies outside a strictly advancing rapid-clock regime.

**CONTRADICTED / UNRESOLVED.** H1's universal reading of a recursive Floquet instability in the exact regular interior periodic system conflicts with (8.7). Its finite-time numerical amplification claims are not disproved by this statement, and were not rerun. Clipping, a different discrete model, additional variables, a boundary limit, or a frozen-coefficient proxy would require separate specifications; none is inferred to explain the historical results.

## 9. The recursive variational loop and repaired commutator theorem

### 9.1 Full variational equations

**EXACT.** For the general historical form
$\dot\rho=f(\rho,\phi)$, $\dot\phi=\omega+\kappa W(\rho)$,

$$
\frac{d}{dt}\binom{\delta\rho}{\delta\phi}
=\mathcal J(t)\binom{\delta\rho}{\delta\phi},\qquad
\mathcal J(t)=\begin{pmatrix}a(t)&b(t)\\c(t)&0\end{pmatrix},
$$

where $a=f_\rho$, $b=f_\phi$, $c=\kappa W'(\rho(t))$.
For H1, $a=-\nu S$, $b=\nu(1-\rho)S'$, and
$S'=A\cos\phi\cos(E_0+A\sin\phi)$. The feedback arrows are
$\delta\rho\xrightarrow{c}\delta\phi\xrightarrow{b}\delta\rho$.
They identify dependencies, not the sign or magnitude of asymptotic growth.

On intervals where $c\ne0$, eliminating $\delta\rho$ yields the **exact** equation

$$
\delta\ddot\phi-\left(a+\frac{\dot c}{c}\right)\delta\dot\phi
-bc\,\delta\phi=0,\qquad
\frac{\dot c}{c}=\frac{W''(\rho)}{W'(\rho)}\dot\rho.
\tag{9.1}
$$

For H1 this is

$$
\delta\ddot\phi+
\left[\nu S-\frac{W''}{W'}\dot\rho\right]\delta\dot\phi
-\kappa\nu(1-\rho)W'S'\delta\phi=0.
$$

The $W''\dot\rho/W'$ contribution may be neglected only with a quantitative bound and away from zeros of $W'$. A sharp warp can make this contribution important. H1 p.7 explicitly neglects it in an approximation; it is not absent from the exact variational system.

### 9.2 The actual commutator

**EXACT.** Use the convention $[\mathcal J_1,\mathcal J_2]=\mathcal J_1\mathcal J_2-\mathcal J_2\mathcal J_1$. Direct matrix multiplication gives

$$
\boxed{
[\mathcal J_1,\mathcal J_2]=
\begin{pmatrix}
b_1c_2-b_2c_1&a_1b_2-a_2b_1\\
c_1a_2-c_2a_1&c_1b_2-c_2b_1
\end{pmatrix}.}
\tag{9.2}
$$

For constant $c$,

$$
\begin{pmatrix}
c(b_1-b_2)&a_1b_2-a_2b_1\\
c(a_2-a_1)&c(b_2-b_1)
\end{pmatrix}.
\tag{9.3}
$$

H1 p.17 Eq.(76), repeated on p.19, omits both diagonal entries and gives the opposite signs for both off-diagonal entries under its printed commutator convention. Changing the commutator order reverses **all** entries; it cannot account for missing diagonals. The work order correctly warns about nonvanishing off-diagonal terms, but the full repair requires (9.2).

**EXACT — necessary and sufficient commuting-family criterion.** All matrices in a family of the displayed form commute pairwise if and only if the vectors
$(a(t),b(t),c(t))$ span a space of dimension at most one.
Proof: the three independent entries in (9.2) are precisely, up to signs, all $2\times2$ minors of two such three-vectors. Their vanishing is equivalent to pairwise linear dependence. If one vector is nonzero, every vector is its scalar multiple.

Consequences:

- If $c\ne0$ is fixed, pairwise commutation is equivalent to **both $a$ and $b$ being constant**.
- If $c=0$, it is equivalent to $a_1b_2=a_2b_1$ for every pair of times. Where $a\ne0$, this means a constant ratio $b/a$, with the zero cases handled by the rank statement.
- If $b=0$ and $c\ne0$ is fixed, $a$ must be constant. If $b=c=0$, arbitrary $a(t)$ commutes.
- With variable $c(t)$, a sufficient and necessary representation is $\mathcal J(t)=h(t)\mathcal J_0$, apart from the identically zero case which is included trivially.

Two explicit counterexamples to the old lemma are

$$
\left[\begin{pmatrix}1&0\\0&0\end{pmatrix},
\begin{pmatrix}0&1\\0&0\end{pmatrix}\right]
=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0
$$

with $c=0$, and

$$
\left[\begin{pmatrix}1&0\\1&0\end{pmatrix},
\begin{pmatrix}0&0\\1&0\end{pmatrix}\right]
=\begin{pmatrix}0&0\\-1&0\end{pmatrix}\ne0
$$

with $b=0,c=1$.

### 9.3 What survives of the triangular argument

**EXACT.** With $c=0$, define $A(t)=\int_0^t a(s)\,ds$. The fundamental matrix is

$$
\Phi(t)=
\begin{pmatrix}
e^{A(t)}&e^{A(t)}\int_0^t e^{-A(s)}b(s)\,ds\\
0&1
\end{pmatrix}.
$$

With $b=0$, it is

$$
\Phi(t)=
\begin{pmatrix}
e^{A(t)}&0\\
\int_0^t c(s)e^{A(s)}\,ds&1
\end{pmatrix}.
$$

For periodic coefficients both have multipliers $e^{A(T)}$ and $1$. Off-diagonal time ordering can change shear and transient gain, but not these multipliers. If $A(T)<0$, one direction decays and one is neutral; the full system is not strictly contracting. If $A(T)>0$, ordinary diagonal growth already causes instability.

The correct replacement for H1's lemma is therefore two separate statements: the rank criterion characterizes commutation; triangularity fixes the Floquet spectrum without requiring commutation. In H1 itself, $S'\equiv0$ makes $a=-\nu S$ constant, which is a stronger special situation than arbitrary $b=0$. That special case does not rescue the general lemma.

## 10. Time ordering, Magnus terms, and what instability would require

**STANDARD_KNOWN_MATHEMATICS.** The variational propagator satisfies

$$
\Phi(T)=\mathcal T\exp\!\int_0^T\mathcal J(t)\,dt,\qquad
\mathcal M_1=\int_0^T\mathcal J(t)\,dt,\qquad
\mathcal M_2=\frac12\int_0^Tdt_1\int_0^{t_1}dt_2
[\mathcal J(t_1),\mathcal J(t_2)].
$$

Here $\mathcal M$ denotes the Magnus logarithm, avoiding collision with the state $\Omega$. A sufficient convergence condition in finite dimension is $\int_0^T\|\mathcal J(t)\|_2dt<\pi$. A finite truncation outside an established error regime is not an exact stability theorem. This is the standard framework, including the convergence qualification, in [Blanes, Casas, Oteo and Ros, §§2.2, 2.7, 3.2](https://arxiv.org/html/0810.5488).

**EXACT.** Noncommutation can give nonzero higher terms. For example
$\mathcal J(t)=\mathcal J_0+t\mathcal J_1$ gives
$\mathcal M_2=-T^3[\mathcal J_0,\mathcal J_1]/12$.
Using the first counterexample of §9.2 gives a nonzero second term despite $c=0$. Noncommuting pairs can also integrate to a zero second term; no biconditional between one nonzero commutator and growth follows.

**EXACT — ordinary parametric-instability witness.** To isolate what time ordering can do, consider two constant segments

$$
B_1=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
B_2=\begin{pmatrix}0&4\\-1&0\end{pmatrix},
$$

lasting $T_1=\pi/2$ and $T_2=\pi/4$, repeated periodically. Since $B_j^2=-b_j\mathbf1$,

$$
e^{T_1B_1}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
e^{T_2B_2}=\begin{pmatrix}0&2\\-1/2&0\end{pmatrix},\quad
M=e^{T_2B_2}e^{T_1B_1}=\operatorname{diag}(-2,-1/2).
$$

Each constant segment has purely imaginary eigenvalues, whereas the periodic system has growth rate $\log2/(T_1+T_2)>0$. Its averaged generator also has purely imaginary eigenvalues. This is an exact time-ordering effect. It is an externally specified piecewise periodic linear system, **not** a derived trajectory Jacobian of H1 or the Tri-Octagon model. It demonstrates possibility, not provenance or novelty.

Conversely, a constant Jacobian can be unstable without time ordering: for the smooth local system

$$
\dot\rho=-a(\rho-\rho_\ast)+b\sin\phi,\qquad
\dot\phi=\kappa\tanh(\rho-\rho_\ast),\quad a,b,\kappa>0,
$$

the equilibrium $(\rho_\ast,0)$ has eigenvalues
$(-a\pm\sqrt{a^2+4b\kappa})/2$.
There is a positive exponent, although the Jacobian on that orbit is constant. This is a simple conditional feedback instability of an otherwise contracting scalar state law. It is not H1, not chaos, and not a proof that every recursive clock destabilizes a contracting system. Taking $b=0$ instead removes that instability for every $\kappa$.

### 10.1 Why H1's published threshold does not follow

**CONTRADICTED as a proved sufficient criterion; historical numerical claim UNRESOLVED.**

1. H1's Eqs.(18), (32) compare absolute/RMS magnitudes with an unspecified approximate inequality. Magnitudes do not control the required signed correlations or a monodromy eigenvalue. These are heuristic scales, not proved sufficient bounds.
2. Along an actual trajectory, $c=\kappa W'(\rho(t))$ varies, and the Jacobian is periodic only if the relevant state trajectory actually is periodic. Freezing $\rho$ and replacing $\phi(t)$ by $\omega t$ produces a different periodic proxy.
3. The approximation requires a bound on the accumulated error, including $\kappa W/\omega$, slow state change, and the dropped $W''$ term. A proposed threshold with $\kappa$ proportional to $\omega$ does not by itself keep those errors small.
4. The printed second-order commutator is incorrect. Its proposed effective matrix also drops the mean lower-left term already present in Eq.(75). The resulting Eq.(80) is not a valid second-order sufficient instability theorem.
5. The exact interior-periodic obstruction (8.7) must be satisfied by any approximation claimed to describe (8.1). A proxy with an unstable multiplier can fail this constraint and cannot establish an instability of that exact orbit.

No continuous-time numerical threshold is claimed verified here. H1 §6's account of simulations remains a literal source claim; its data, parameters, boundary handling, and computations have not been recovered or inferred.

### 10.2 Coordinate invariants versus representation-dependent terms

**EXACT.** Under a time-dependent change of variational coordinates $\eta=P(t)\xi$, the generator becomes
$\widetilde{\mathcal J}=\dot P P^{-1}+P\mathcal J P^{-1}$.
Individual commutators and Magnus terms therefore depend on the representation. If $P(T)=P(0)$, monodromies are similar and Floquet multipliers agree. Bounded coordinate derivatives and inverse derivatives preserve asymptotic Lyapunov exponents. An unbounded transformation, a singular limit such as $\rho\to1$, or a change of time requires separate accounting.

Any fundamental-matrix transformation can formally trivialize a linear equation. That observation neither removes measured amplification nor establishes novelty. A meaningful comparison fixes the state observables and time, or tracks their transformations explicitly. Pure diagonal phase generators commute at different times even when their entries vary; new noncommutation concerns the **full variational generator**, including derivatives of those entries and amplitude coupling.

## 11. Chirality: generation, bias, and spontaneous selection

**EXACT.** For cyclic $(i,j,k)$,

$$
Z_i=\Im(\overline\Omega_j\Omega_k)
=2\sqrt{I_jI_k}\sin(\phi_k-\phi_j).
$$

Differentiating on the nonzero domain gives

$$
\dot Z_i=
\left(\frac{\dot I_j}{2I_j}+\frac{\dot I_k}{2I_k}\right)Z_i
+2\sqrt{I_jI_k}\cos(\phi_k-\phi_j)(\dot\phi_k-\dot\phi_j).
\tag{11.1}
$$

The direct recursive contribution is consequently

$$
\dot Z_i\big|_{\rm clock}
=2\sqrt{I_jI_k}\cos(\phi_k-\phi_j)(\varpi_k-\varpi_j).
$$

A shared clock has exactly zero direct contribution. Under §5's equivariance conditions it also has no indirect effect on the invariant trajectory. Absolute-phase-dependent auxiliary feedback invalidates that stronger conclusion.

Local clocks can generate nonzero $Z$ from $Z=0$. For the explicit conditional choice $\Omega=(1,2,3)$ real and $\varpi_i=\alpha I_i$, the actions are $(1/2,2,9/2)$, and the initial direct derivative is

$$
\dot Z\big|_{\rm clock}=\alpha(15,-12,3).
$$

This is phase shearing of unequal initial actions. It is not spontaneous selection from a fully symmetric initial condition. With identical channel laws and exactly equal amplitudes and phases, permutation invariance and uniqueness preserve that symmetric state and give $Z=0$.

**EXACT — the relevant symmetry must be specified.** For an even-in-phase state variable such as $I$, fixed nonzero local rates are not conjugation-equivariant: conjugating $i\varpi(I)\Omega$ changes its sign. A Hamiltonian radial clock is instead reversible under conjugation when considered alone. Adding gradient damping does not preserve that time-reversal symmetry. A selected temporal orientation or rate law must not be mislabeled spontaneous breaking of a symmetry it already violates.

With identical channel parameters, ordinary channel permutations still preserve (6.3). The scalar $u\cdot Z$ changes sign under an odd channel permutation; hence paired chiral solutions can still be related by an actual permutation symmetry. Existence of two attracting branches, their basins, and a selection process must be shown for a particular model. Section 7.3 proves equal spectra for its two phase orderings, not preferential selection of either one. No CP or particle interpretation is assigned.

The cubic diagnostic $M=\Omega_1\overline\Omega_2\Omega_3$ obeys
$\dot M|_{\rm clock}=i(\varpi_1-\varpi_2+\varpi_3)M$.
Thus $\dot J_{\rm eff}|_{\rm clock}=(\varpi_1-\varpi_2+\varpi_3)\Re M$.
A shared rate changes this diagnostic while leaving $Z$ fixed, consistently with Bridge II. It is not used as feedback or as an established physical observable.

## 12. Unitary carrier symmetry: frozen operators versus nonlinear laws

### 12.1 The joint centralizer at a fixed frequency matrix

**EXACT.** The centralizer of $L_3$ itself never changes:

$$
C_{U(3)}(L_3)=U(1)\times U(2),\qquad
C_{SU(3)}(L_3)=S(U(1)\times U(2)),
$$

with blocks on $\mathbb Cu\oplus u^\perp_{\mathbb C}$. A new frequency operator changes a **joint** centralizer, not this theorem.

For a fixed real diagonal $D=\operatorname{diag}(\nu_1,\nu_2,\nu_3)$, consider the linear generator $gL_3-iD$ with $g\ne0$. A unitary commuting with that generator also commutes with its adjoint, hence with its Hermitian and anti-Hermitian parts separately. Its centralizer is exactly
$C_{U(3)}(L_3)\cap C_{U(3)}(D)$.

| Fixed $D$ | Joint centralizer in $U(3)$ | Joint centralizer in $SU(3)$ |
|---|---|---|
| All three rates equal | $U(1)\times U(2)$ | $S(U(1)\times U(2))$ |
| Exactly two rates equal | $U(1)\times U(1)$, represented as $\operatorname{diag}(a,a,b)$ in the basis described below | $a^2b=1$, isomorphic to $U(1)$ |
| All rates distinct | Scalar $U(1)$ | The scalar cube roots of unity, $\mathbb Z_3$ |

Proof for the distinct case: commuting with $D$ makes the unitary diagonal in the face basis. Commuting with $uu^\ast$ forces its three diagonal phases to coincide. If $\nu_1=\nu_2\ne\nu_3$, put $e_+=(e_1+e_2)/\sqrt2$, $e_-=(e_1-e_2)/\sqrt2$. The condition $Uu=au$ forces the same phase $a$ on $e_+$ and $e_3$, leaving a free phase $b$ on $e_-$. These prove the table. If $g=0$, the coupling restriction is absent and the answer is instead the usual frequency-eigenspace block centralizer of $D$.

### 12.2 A state-dependent frequency is not a fixed matrix

**EXACT.** For $N(\Omega)=-iD(\Omega)\Omega$, a fixed unitary is an equation symmetry precisely when

$$
D(U\Omega)\,U\Omega=U D(\Omega)\Omega\quad\text{for every state in the domain}.
\tag{12.1}
$$

Pointwise commutation with $D(\Omega)$ alone neither expresses this condition nor accounts for its derivatives in the variational equation.

For a shared rate $D(\Omega)=\nu(\rho_{\rm global}(\Omega))\mathbf1$, (12.1) reduces to invariance of the composite scalar function $\nu\circ\rho_{\rm global}$. Taking $\rho_{\rm global}$ to depend only on total action guarantees all of $U(3)$ for the clock term and leaves the $L_3$ centralizer intact. A shared scalar depending on a labelled face action, or on $\sum I_i^2$, need not have that invariance. “Shared” is not sufficient by itself.

**DERIVED_FROM_STATED_ASSUMPTION — exact local-law result.** For the same smooth strictly monotone function $\nu(I_i)$ in each channel, the pure local-clock field has precisely the monomial unitary symmetries
$U(1)^3\rtimes S_3$.
To see the absence of other unitaries, test (12.1) on a one-channel state $z e_j$. Each nonzero component $U_{ij}$ must obey
$\nu(|U_{ij}|^2|z|^2/2)=\nu(|z|^2/2)$.
Strict monotonicity forces $|U_{ij}|=1$; column normalization then permits only one nonzero entry. Conversely independent phases and permutations plainly preserve the local law. The argument can use limits from the nonzero domain if necessary.

Intersecting these symmetries with the $L_3$ centralizer gives

$$
\{e^{i\alpha}P:P\in S_3\}=U(1)\times S_3.
$$

In $SU(3)$ impose $e^{3i\alpha}\det P=1$. Its continuous component is trivial; the group has 18 elements and can be written
$\{\zeta^m(\det P)P:m=0,1,2,\ P\in S_3\}$, $\zeta^3=1$.
Nonmonotone, constant, or differently labelled rate laws require their own symmetry check; (12.1) is the general answer, not a universal assertion of this smaller group.

Equal local rates at a particular equal-action state do not restore a global $U(2)$ equation symmetry. Conversely, unequal instantaneous rates in an identical local law do not destroy permutation **equivariance**, since permuting the state also permutes those rates. This distinguishes the fixed-operator table from the nonlinear equation.

The entrywise cubic amplitude field already reduces continuous mixing symmetry, and fixed unequal $k_i$ reduce permutations. At identical parameters the common phase and permitted channel permutations remain symmetries of (6.3) on its smooth domain. These are statements about complex coefficient equations, not automatically physical transformations of the face observables. The anti-symplectic geometric mirror action is a different, conjugate-linear representation. No Standard Model interpretation is made.

## 13. Comparison with established dynamical models

These comparisons concern the derived equations, not a presumed explanation of every historical mechanism. The limited external reading checked standard tools and model definitions; it was not a novelty or priority search.

| Comparison baseline | Classification | Exact scope / distinguishing premise |
|---|---|---|
| Action–angle mechanics | EXACT_EQUIVALENCE | The coordinate identity and Hamilton equations of §§3–4 are canonical polar mechanics with the explicitly frozen sign. This does not identify a physical action. |
| Hamiltonian state-dependent frequency | SPECIAL_CASE_OF | Angle-independent $H(I)$ gives integrable amplitude-dependent rotation. The closedness criterion restricts which multi-channel rates are Hamiltonian. |
| A one-degree-of-freedom separable Hamiltonian | EXACT_EQUIVALENCE | H1 on the unwrapped interior has the explicit Hamiltonian (8.4). On the phase cylinder it is globally Hamiltonian only under the zero-period-integral condition. The exact equivalence retains the feedback and its observable time dependence. |
| Isochronous Stuart–Landau oscillator | EXACT_EQUIVALENCE | With $g=K=0$, constant $\varpi$, and supplied coefficients, $\dot z=(\varepsilon k+i\varpi)z-\varepsilon|z|^2z$ has exactly this algebraic form. The supercritical limit-cycle interpretation requires the appropriate positive growth/saturation and nonzero frequency. |
| Nonisochronous Stuart–Landau oscillator | EXACT_EQUIVALENCE | For $g=K=0$ and $\varpi(I)=\omega_0+\alpha I$, $\dot z=(\varepsilon k+i\omega_0)z-(\varepsilon-i\alpha/2)|z|^2z$. Arbitrary $W(r(I))$ need not be cubic. |
| General amplitude-dependent nonlinear oscillators | SPECIAL_CASE_OF | Radial growth plus a smooth radial phase rate is this known class. A field-derived choice of the rate could still be a new model-specific result. |
| Phase–amplitude reduction | SHARES_STRUCTURE_WITH | The exact polar equations retain all six real coordinates. A phase-only reduction additionally needs, for example, a stable limit cycle, controlled perturbations, and appropriate asymptotic phase coordinates. |
| Synchronization theory | SPECIAL_CASE_OF / EXTENSION_OF | The isolated constant-rate third-harmonic phase subsystem is exactly the reviewed Kuramoto-type model. Evolving actions/auxiliary state extend that particular phase-only model. |
| Complex Ginzburg–Landau networks | SPECIAL_CASE_OF | With $K=0$, affine local frequency and real $g$, the equations are a cubic complex-oscillator network with graph diffusion. This is a graph version, not the continuum PDE. A general warp and the separate normalized harmonic-3 term go beyond that cubic form. |
| Floquet theory | EXACT_EQUIVALENCE | For an actual periodic variational system, the monodromy determines linear exponential growth. Periodicity of a frozen proxy is insufficient to identify an exact nonlinear-orbit multiplier. |
| Parametric instability | SHARES_STRUCTURE_WITH | Periodic feedback coefficients can in principle produce it. Section 10 gives a separate exact example; H1's regular interior periodic orbits instead obey (8.7). |
| H3's fixed-ratio dual-time mixed flow | DISTINCT unless an extra equivalence is proved | A common coherence functional and fixed gradient/skew-gradient ratio are not derived for (6.3). A state-dependent angular speed is not automatically that same two-time construction. |
| H4's filtered-history recursion | DISTINCT | $M_t$ is an independent stored state. Equations on $I,\phi$ alone do not reproduce that memory without an explicit reconstruction. |

For context, [Nakao, phase-reduction review, §§2–4 and Appendix B](https://arxiv.org/html/1704.03293), distinguishes polar angle from asymptotic phase and develops the Stuart–Landau example and weak-coupling reduction. [Aranson and Kramer, §I.A](https://arxiv.org/html/cond-mat/0106115), supplies the standard cubic complex Ginzburg–Landau equation as a comparison. The equivalences in the table are established by the substitutions displayed here, not by the citations or by matching terminology.

An important falsification test is particularly explicit. For an isolated oscillator

$$
\dot r=r(a-br^2),\qquad \dot\phi=\omega-cr^2,\qquad b\ne0,\ r>0,
$$

the angle

$$
\vartheta=\phi-\frac cb\log r
$$

satisfies $\dot\vartheta=\omega-ca/b$. Its radial dependence can be removed from the isolated angle equation. This is even a canonical phase shift with $I$ unchanged on the punctured plane, since $\vartheta-\phi$ depends only on $I$.

It does not contradict §4.4: here $I$ evolves, whereas the radial Hamiltonian there conserves it. With coupling, substituting $\phi_i=\vartheta_i+(c/b)\log r_i$ changes phase differences inside all coupling terms. The radial information survives in the interaction and in measured Cartesian quadratures. More generally, for $\dot I=F(I)$, $\dot\phi=\varpi(I)$, a shift $\vartheta=\phi+h(I)$ gives constant rate $\varpi_\ast$ wherever
$h'=(\varpi_\ast-\varpi)/F$ is well defined and extends regularly across any zero of $F$. Thus “state-dependent angular speed” alone does not establish irreducible recursive novelty.

The novelty categories requested in the work order can now be separated:

| Category | Finding |
|---|---|
| KNOWN TOOL | Symplectic coordinates, variational equations, implicit-function continuation, Magnus expansions, Floquet multipliers, and centralizer algebra. |
| KNOWN DYNAMICAL CLASS | Integrable radial oscillators; the conditional separable Hamiltonian realization of H1; cubic nonisochronous oscillators for affine local rate; feedback systems with additional state when explicitly supplied. |
| NEW COMBINATION | Relative to the frozen repository, (6.3) combines its existing parent with a chosen local clock. This is a research proposal, not a worldwide novelty determination. |
| POSSIBLY NOVEL MECHANISM | A justified, measurable face-state-dependent temporal feedback with effects not accounted for by an equivalent established model. The physical premise and such an exclusion are presently unresolved. |
| NOVEL RESULT IF PROVED | A specific independently checked theorem or discriminating observable prediction for a fully specified model, followed by an adequate literature comparison. The exact conditional results here are candidates for review, not priority claims. |

No universal impossibility of new recursive physics is asserted. No established mathematical structure is counted as a novelty merely because it has a new name.

## 14. Falsification ledger and the smallest surviving bridge

| Attempt to falsify | Result and scope | Classification |
|---|---|---|
| Remove a shared recursive clock completely | Succeeds on a closed common-phase quotient under §5's premises; invariant observables then cannot distinguish it. Fails as a conclusion about absolute-phase forcing such as H1's $f(\rho,\phi)$. | EXACT |
| Reduce every local clock to a constant detuning | Succeeds on fixed-action uncoupled levels. Fails for the neighborhood of the specified orbit in §7.3: its rate on the orbit is unchanged but its transverse stability depends on the frequency slope. | DERIVED_FROM_STATED_ASSUMPTION |
| Remove isolated amplitude-dependent frequency by a phase coordinate | Succeeds for the nonisochronous oscillator transformation in §13; does not remove the induced changes to couplings or physical phase readouts. | EXACT |
| Argue that the word “recursive” creates an extra degree of freedom | Fails. If $\rho=r(I)$, the model still has six real state coordinates. An independent $\rho$ or filtered memory is extra state and must be specified separately. | CONTRADICTED |
| Show that the feedback loop always destabilizes | Fails: the in-phase branch in §7.2 stays linearly stable under its stated positive-parameter assumptions; a phase-independent $f$ also removes the return arrow. | CONTRADICTED |
| Show that a nonzero commutator proves instability | Fails: triangular counterexamples and the exact H1 interior periodic result separate time ordering, shear, and exponential growth. | CONTRADICTED |
| Show that time-ordering effects vanish under any legitimate coordinate change | Fails for invariant Floquet multipliers under periodic invertible transformations. Individual Magnus terms can vanish or change representation. | EXACT |
| Recover the missing physical $\rho$ observable from the five sources | No face-specific observable, units, or extraction law is found. The logarithmic action chart is an exact conditional mathematical encoding, not that physical derivation. | UNRESOLVED |
| Derive a unique warp function from geometry | No derivation supplied. $W,\kappa$, scales, and possibly the state coordinate remain choices. The physical meaning of large $W'$ depends on the coordinate/units chosen for $\rho$. | UNRESOLVED |
| Separate genuine warp effects from a change of the scalar coordinate | For $\widetilde\rho=h(\rho)$, the same model has $\widetilde f=h'f$ and $\widetilde W=W\circ h^{-1}$. Comparing slopes without transforming the rest is not invariant. | EXACT |
| Explain all proposed behavior with a simpler known system | Several cases have exact known-form equivalences. H1 has an unexpectedly restrictive canonical realization. No theorem identifies every possible state-dependent network extension with one simpler system. | UNRESOLVED in general |
| Produce hysteresis, new attracting classes, or selected chirality from unspecified recursion | Not determined by the data. A linear threshold is not a nonlinear bifurcation or selection theorem. | UNRESOLVED |
| Obtain a distinguishable prediction | The conditional local-slope threshold in §7.3 differs from a constant-detuning replacement. It is a dimensionless model prediction, with no measured face observable or calibrated time yet. | DERIVED_FROM_STATED_ASSUMPTION |

**EXACT mathematical content available for the next review:** the action–angle sign; the Hamiltonian integrability conditions; the conditional logarithmic realization and Floquet obstruction for the literal historical scalar law; the full commutator classification; the Paper-A polar parent; the conditional local-clock stability calculation; the chirality derivative; and the distinction between pointwise centralizers and nonlinear equivariance.

**UNRESOLVED physical content:** what the face vector measures, why a particular $\rho$ and warp are selected, whether the historical phase is absolute or relative to a supplied reference, the frequency/time units, and which observables make a proposed effect testable.

These are independent questions. The exact constructions neither restore the historical SRG architecture nor admit a new mechanism into the physics kernel.

## 15. Verification scope, provenance, and stop boundary

All mathematical checks in this report are analytic derivations, explicit substitutions, or finite matrix calculations written out above. **No implementation, symbolic verification script, numerical integration, parameter scan, scientific regression, or archive verification suite was run.** There is no new executed predicate count and no claim of independent Phase Bridge III verification.

Actual tool work consisted of read-only repository/source inspection, PDF text extraction, PDF page rendering for source-equation inspection, a limited check of three standard external comparison references, writing this report, and byte-hash preservation checks. Temporary source extracts and renders are outside the repository. The repository receives only this new report; its frozen metadata, checksum lists, scientific sources, reports, papers, and kernel are unchanged. No commit or push is made as part of this derivation.

The preservation check matched all **63 pre-existing tracked repository files** and all **five historical PDFs** to their before-work SHA-256 values. The report's local links and math-delimiter/text structure were checked separately; these are document checks, not scientific verification predicates.

The source hashes identify the exact five historical PDFs:

| Source | SHA-256 |
|---|---|
| H1 | bae8bb70a06447469001759536fbc9afb442959a68191cbd846fcd29c289d32b |
| H2 | 47d7eb3ab44b5bf8481ace4c70c66251233503801b62860b536ad8f9a8944ee8 |
| H3 | 4977b3c5b04647851982a62a2d43f7632110ceddff37da930d0f4935df552fc0 |
| H4 | 6a3345d251878d1abdbb97e5ea5fb6de2e952b489ab449a5bca03b1d2d794461 |
| H5 | 7243a26b408cce75806aef9b43ab047f1d7cf8309449b9d1f75d5376e45e9c66 |

The status below is a report handoff, not a kernel-admission verdict. “PARTIAL” retains the unresolved physical interpretation and the need for an independent check of these new proofs. It does not erase the exact conditional constructions or treat historical mechanisms as disposable.

~~~ini
ACTION_ANGLE_FORM = EXACT_D_I_WEDGE_D_PHI
RECURSIVE_PHASE_HAMILTONIAN = DERIVED_FROM_STATED_ASSUMPTION_WITH_INTEGRABILITY_CONDITIONS
SHARED_CLOCK_REMOVABLE = EXACT_ON_EQUIVARIANT_PHASE_INVARIANT_QUOTIENT
LOCAL_CLOCK_RELATIVE_PHASE_EFFECT = EXACT_CONDITIONAL_RATE_DIFFERENCE
PAPER_A_ACTION_ANGLE_PARENT = EXACT_ON_NONZERO_DOMAIN
STATE_PHASE_FEEDBACK_LOOP = DERIVED_FROM_STATED_ASSUMPTION
HISTORICAL_RHO_MODERN_MATCH = UNRESOLVED_PHYSICALLY_EXACT_CONDITIONAL_LOGARITHMIC_CHART
RECURSIVE_VARIATIONAL_LOOP = EXACT
COMMUTATOR_LEMMA_REPAIRED = EXACT_NECESSARY_AND_SUFFICIENT_RANK_CRITERION
NONTRIVIAL_MAGNUS_STRUCTURE = EXACT_POSSIBILITY_NOT_SPECIFIC_TO_RECURSION
FLOQUET_RECURSIVE_INSTABILITY = CONTRADICTED_FOR_REGULAR_H1_INTERIOR_PERIODIC_ORBITS_CONDITIONAL_IN_EXTENSIONS
RECURSIVE_TIME_REDUCES_TO_KNOWN_MODEL = EXACT_IN_SPECIFIED_SUBCASES_UNRESOLVED_IN_GENERAL
SUPPORTED_NOVEL_MECHANISM = UNRESOLVED
RECURSIVE_TIME_CHIRALITY_EFFECT = EXACT_LOCAL_RATE_EFFECT_SELECTION_UNRESOLVED
SU3_SYMMETRY_EFFECT = EXACT_FIXED_OPERATOR_CLASSIFICATION_CONDITIONAL_NONLINEAR_SYMMETRY
PHASE_BRIDGE_III_READY_FOR_CODEX = PARTIAL
~~~
