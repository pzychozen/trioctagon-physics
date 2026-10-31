# NCM-DUAL-02 v0.1 — Existing-Equation Correspondence and Return Mechanisms

Independent bounded review, 31 October 2026. Author: Hilmir Frímann Halldórsson. The author supplied the motion intuition; GPT supplied the lead analysis; Codex performed the source review, deductions and verification here. This is a review package, not a manuscript or publication.

## Finding

The established mathematics supports **a distinction between a returning observable and a still-changing full state**. There is an exact native coherence-return theorem, an existing SRG reduction with a three-step channel return, and a precise obstruction between two proposed transports. These are substantive relationships and limitations, not a derivation of the cone choreography.

No inspected result supplies a native three-step coherence cycle with a quarter-phase remainder, or a state-to-cone map intertwining native updates with the prescribed legs. The apparent twelve-return therefore remains unestablished for native evolution. We stop motion integration here: no law, parameter fit, clock, normalization feedback, state variable, or pose schedule has been added.

The most useful additional deductions are:

1. A **single regular native coherence return** suffices to propagate its phase remainder indefinitely in exact mathematics; regularity of the repeated blocks follows from equivariance. Minimal coherence period and the order of that remainder determine full-state period.
2. A normalized-projector return is weaker: even its amplitude multiplier need not repeat. A two-update exact rational example demonstrates this.
3. The accepted M3 two-cycle cannot produce a three-stage or twelve-stage current-state readout under any fixed integer sampling stride. The obstruction follows from period divisibility, not from an unsuccessful simulation.
4. Fixed SRG has exact projective returns on helicity sectors despite having no nonzero raw periodic orbit. At steps three and twelve, projective return of the full six-state requires a single helicity eigensector.
5. The marked cone loop is parallel transport for its specified no-own-axis-spin path, whereas matched face transport is flat on its tangent planes. Fixed per-label changes of frame cannot equate their loop maps.

## Author correction and evidence status

The author's golden-ratio wording was illustrative and **is not a controller requirement**. This supersedes that interpretation in NCM-DUAL-01; the older record is unchanged. Historical constants remain literal at their own call sites. Nothing was fitted to the cone shape, return count, or a preferred number.

The work order is the authorized scope; the lead memo is proposed analysis, not authority. Its reported 19-check script was not among the supplied files and was not found by the bounded Downloads filename search. Its claimed run was not inherited as verification. This package has its own script, results and log.

Source identifiers below resolve to actual paths and SHA-256 records in `SOURCE_MANIFEST.json`. `source_reads.json` records selected ranges and searches. All source access was text/data only. No project modules, old checkers, or applications were executed. Accepted D1/M3 certificates are **inherited theorem statements**, not recertified results of this task. The supplied revision string is a locator, not a claim about the checkout's current revision.

## 1. Typed comparison: what returns, and what is lost?

| Object | Carrier, evolution/index | Information and meaning of return | Source |
|---|---|---|---|
| Native state z=Omega | C^3, autonomous fixed-parameter F, integer update n | Retains amplitudes, relative phases and one common phase. Full return means equality of all three complex entries. No physical time calibration or cone pose is defined. | DYNAMICS:27–104; D1:D5–D7 |
| Coherence H=zz† | Rank-one positive Hermitian matrices (plus zero); induced update on the regular prestage domain | Keeps raw norm and relative complex shape; loses only common phase for nonzero z. Return need not be full-state return. | OBSERVABLES:185–236 |
| Normalized projector H/tr H | Rank-one projectors, z≠0 | Also loses positive scale. It does not generally carry a closed autonomous native evolution: the cubic stage depends on scale. | Coherence definitions; §3 below |
| Decoded face vectors D(z)_i=Re(z_i)t_i+Im(z_i)e_z | Direct sum of three fixed tangent planes W_i; D F D^{-1} is the induced full-state update | D is a real-linear bijection onto the tangent-vector triples, retaining common phase and raw scale. A common phase rotates components within each face plane; it is not automatically one ambient rigid body rotation. | FACE:66–112; OBSERVABLES closure theorem |
| Matched transport T_ij | W_j→W_i, label transport; no autonomous time update | Preserves the two coefficients in the matched bases. A closed label loop is identity on W_i. Ambient 3×3 extension has rank two. | FACE:123–133 |
| Fixed SRG U=B⊗A | C^2⊗C^3, integer transfer count n | Retains raw scale and helicity. Three transfers restore the channel factor up to D, leaving B^3. This n is not automatically native update count. | BRIDGE:F2–F7; SRG:57–94 |
| Staged Z | Readout of z plus observer clock (q,N,t) | Norm and Re(z)×Im(z) discard common phase. Harmonic, envelope and ambient direction use separately supplied clock data. Returning z alone need not return the full clocked observation. | Z:66–82,117–159,189–199 |
| EMA Z | Readout of z, clock and current scalar memory | Memory is separately advanced using Im(z0 conjugate(z1) z2), which can depend on common phase. It is an existing observer state, not a native cone frame. | Z:226–265 |
| Cone axes / labels / marked frames | Axes in RP^2; persistent oriented axes in S^2; full frames in SO(3) | Unmarked circular cones discard axial roll. Marks retain it only under the specified transport. Leg number advances a prescribed route; continuous progress is imposed kinematics. | DUAL_MATH:6–91; DUAL_RESULTS; DUAL_REPORT:152–174 |

Keep H (coherence), H_chart=diag(1,1,-1) (coordinate conversion), and the conjugation involution called H in Paper G distinct. Likewise J=iI below is unrelated to the EMA source's cubic scalar named J. Channel coordinates, spatial coordinates, complex phases and internal SU(2) phases are different carriers.

The observer preset N=12 supplies 30-degree observer increments. It is not evidence of twelve native updates, or 90-degree body rotations. In particular, staged Z at fixed clock is unchanged by z→e^{iχ}z. The EMA cubic instead transforms as Im(e^{iχ} z0 conjugate(z1) z2): it is 0 on (1,1,1) and 1 on (i,i,i). A blanket claim that every Z variant ignores common phase would be false. Neither variant defines the two cone frames.

## 2. Three-by-four comparison algebra and its limits

Let Pi(z0,z1,z2)=(z2,z0,z1), J=iI and Q=iPi. Then Pi^3=I, J^4=I and JPi=PiJ. Consequently

    Q^3=-iI, Q^6=-I, Q^9=iI, Q^12=I.

Q has minimal operator order twelve. Its eigenvalues are i, iω, iω², with ω=e^{2πi/3}; their orders are 4,12,12. Thus every nonzero vector on the equal-channel line has minimal Q-period four; every vector with a nonzero component in either other Pi eigenspace has minimal Q-period twelve. Zero has period one. No other nonzero full-state periods occur for this comparison.

On coherence, Q acts as H→Pi H Pi†, so periods divide three. For nonzero rank-one H, period one occurs exactly when z is a Pi eigenvector; otherwise it is three. Normalized projectors have the same classification here because Q is unitary. The exact example z=(1,2,3i) has full period twelve and coherence period three. These are Q-orbits, **not native trajectories**.

SRGI:742–770 already proves J's order-four identity and real, rather than complex-Hilbert, orthogonality. It explicitly separates the algebraic phase orbit from dynamics. Historical time shifts, mirrors and sector exchanges have other carriers and are not silently substituted for J.

### Native covariance is not execution of Q

Write L3=11^T−3I and

    V_k(z)=[I+epsilon diag(k−|z|²)+gL3]z,
    F_k(z)_i=V_i exp(i delta_i),
    delta_i=lambda sum_(j!=i) sin(3(Arg0 V_j−Arg0 V_i)).

All parameters are fixed real numbers during a run. Since L3 commutes with Pi and |Qz|²=Pi|z|²,

    V_(Pi k)(Qz)=Q V_k(z).

If every V_i is nonzero, the common phase shift cancels from phase differences (including argument wraps inside the sine), so

    F_(Pi k)(Qz)=Q F_k(z).

Equal k gives symmetry of the same map. Unequal k gives parameter covariance, not generally fixed-map symmetry. There are exceptions, such as epsilon=0 when k drops out; equal k is sufficient, not an unconditional necessary condition. We never cycle k during evolution. With lambda=0 the amplitude identity is global in exact arithmetic.

The predeclared unequal-k probe gives an exact failure, beyond its numerical diagnostic. For b=(1+i,1−i,2+i) at the documented coefficients, the first component of QV_k(b) is (−17003+35006i)/30000, whereas the first component of V_k(Qb) is (−16997+34994i)/30000. The second squared modulus minus the first is −29/25000. Synchronization preserves each modulus, so F_k(Qb) and QF_k(b) cannot agree.

For k=(1,1,1), z=(1,1,1), every native increment vanishes for every real epsilon,g,lambda. Hence F(z)=z but Qz=iz. This exact fixed point refutes F=Q as an identity even in the equal-k symmetry class.

At zeros the native Arg0(0)=0 convention matters. At epsilon=g=0, lambda=1/10, let z=(1,−1,0) and z'=e^{iπ/6}z. The input H agrees. Output H_01 is −1 for z and −e^{−i/5} for z', so global coherence closure fails. For Qz=(0,i,−i),

    F(Qz)=(0,i exp(i/10),−i exp(−i/10)) != QF(z).

Thus the actual Q covariance also fails on this example. We neither repair nor smooth the zero convention. Since 0<1/5<2π and 0<1/10<2π these differences are exact, not conclusions from small numerical residuals.

The signed cone generators A,B_s,C do not commute: AB_s e_x=−e_y while B_s A e_x=−s e_z. Commuting phase/cycle generators cannot have these noncommuting factors as faithful images under the proposed factor identification. This does **not** exclude every nonlinear or restricted correspondence, or an abstract order-twelve cyclic representation. A product's order says nothing sufficient about its factors, continuous paths or amplitudes.

## 3. Native coherence return: theorem, proof and controls

On the regular domain V_i≠0, the inherited H update can be written without a phase choice. Put

    M(H)=I+epsilon diag(k−diag H)+gL3,
    Htilde=M(H) H M(H)^T,
    rho_i=sqrt(Htilde_ii),
    delta_i=lambda sum_(j!=i) Im[(Htilde_ji/(rho_j rho_i))^3],
    H^+=U_delta Htilde U_delta†,  U_delta=diag(exp(i delta_i)).

The cube is **inside** the imaginary-part operation. This is the source closure formula, obtained by expanding V_j conjugate(V_i). It is a genuine partial dynamic correspondence at the same update index. Its regular domain is not asserted globally forward invariant. The following return result closes that issue for a returning block itself.

**Regular coherence-return theorem.** Fix F. Let z≠0 and suppose its first p prestages have no zero components. If H(F^p z)=H(z), then there is a unique μ with |μ|=1 and F^p z=μz. Every subsequent block is regular and, for m≥0 and 0≤r<p,

    F^(mp+r)z=μ^m F^r z.

If p is the minimal coherence return and μ has exact order q, the full-state minimal period is pq. If μ is not a root of unity, there is no finite full-state return. One can extract μ directly as z†F^p z/(z†z), without fitting a phase rate.

**Proof.** Equality of the nonzero rank-one matrices gives the same one-dimensional range, so F^p z=az. Equality of their traces gives |a|=1. Common-phase multiplication preserves the prestage-zero pattern and, at regular prestages, commutes with F. Induction over the known p-block therefore proves F^r(μ^m z)=μ^m F^r(z), its regularity, and the displayed identity. No general invariant-domain assertion is needed. The resulting H sequence is p-periodic. If a full-state return occurred at N, write N=ap+r, 0≤r<p; then H(F^r z)=H(z), forcing r=0 by minimality. The remaining condition is μ^a=1. This gives pq, or no finite return. This proof is exact and is not replaced by a finite test.

Consequently p=3 and μ=±i would indeed give a native twelve-update orbit. **Existence of such a native block has not been established.** No probe in this task searched for it.

### Normalized shape does not give this conclusion

For the normalized projector, equality implies only z'=aμz with a>0 and |μ|=1. Native F is not generally positively homogeneous, so one cannot infer F^(mp)z=(aμ)^m z from one such return.

An exact example uses k=(1,1,1), epsilon=1/10, g=1/60, lambda=1/300 and z=r(1,1,1), r>0 in the stated steps. Graph and phase increments vanish; r^+=f(r)=r[1+(1−r²)/10]. Starting at r0=1/2 gives

    r1=43/80,
    r2=2947693/5120000,
    (r1/r0)^2 r0=1849/3200 != r2.

The projector is identical at all three states, but raw H and the multiplier change. This also explains why a general autonomous projector update cannot be assumed merely from coherence closure.

More generally, failure of projector closure follows algebraically without another numerical case. With g=lambda=0 and equal k0, let a=1+epsilon k0≠0 and epsilon≠0. For nonzero components v_i,v_j with unequal squared moduli, the output ratio from tv is (v_i/v_j)[a−epsilon t²|v_i|²]/[a−epsilon t²|v_j|²]. It varies with positive t wherever its denominator is nonzero, although the input projector is independent of t. Thus an autonomous projector map cannot descend from F in this admissible parameter class.

### What the accepted native results actually provide

| Control | Precise inherited scope | Consequence here | What it does not supply |
|---|---|---|---|
| D1 relative equilibria | (epsilon,g,lambda)=h(1,1/6,1/30), k=(1−eta,1,1+eta), 0≤h≤1/4; local analytic branch near the nonzero twisted reference; regular domain. F_h(z)=exp(ih nu)z. nu_+=2c_+(h)eta³+O(eta⁵), c_+=sqrt(3)(33h²−240h+688)/(6(1−3h)³)>0. | For h>0 and sufficiently small nonzero eta there is genuine native common-phase drift with stationary H (p=1). The reference is a saddle. At h=0 F is identity; the extended generator rate is not an actual per-step advance. | No p=3 shape cycle, prescribed ±π/2 advance, attraction, or spatial rotation. No finite phase order is inferred from its expansion. |
| Accepted repaired M3 | epsilon=1/20, g=1/5, k=(1,1.2208964704604097,6.35310346037241); exact lambda=lambda_c+1/200. Entrance sqrt(3)f1 with squared norm 3; certified quotient capture by index 301. | Limiting cycle z_−=exp(i theta) conjugate(z_+), F(z_−)=z_+. Nonzero common-phase-invariant W,Gamma reverse sign, so minimal coherence period is 2. Full minimal period is also 2, μ=1 over the block. | Capture is convergence to a cycle, not a claim the entrance becomes exactly periodic at finite index. The separately proved local M2 branch is not silently identified with M3. No twelve-period phase remainder. |
| Coherent relaxation | epsilon=1/10, g=1/60, lambda=1/300, k=(.999,1,1.001); .9≤|z_i|≤1.1 with ordinary phases in one interval of width ≤π/12, up to common rotation. | Every state in this invariant domain converges to exp(i theta_infinity)r_*, the unique positive fixed profile in [.9,1.1]^3. A periodic orbit in this domain must be constant: a convergent periodic sequence is constant. | Not global convergence, not a statement about all parameters. The retained turning entrance lies outside this domain; no turn-to-capture theorem is inferred. |

Sources: D1:40–114; M3:193–197,285–315,372–391; COHERENT:160–164,316 onward,414–448. Long certificates were not rerun.

**Additional period-divisibility obstruction.** If z lies on an exact native r-cycle and R is any single-valued current-state map, then R(F^{n+r}z)=R(F^n z). Every minimal periodic readout period divides r. Sampling F^m for any fixed positive integer m yields a state period r/gcd(r,m), so the readout period divides that number. Thus no such map of the M3 limiting two-cycle can produce the three distinct cone stations, or the twelve distinct marked stages, at any fixed integer stride. This does not constrain transient readings, nonperiodic native trajectories, or observers carrying additional memory/clock state. An H-only map is constant on a D1 relative equilibrium, even though the full z changes phase.

### Can existing phase represent opposite rolls?

A single common phase is not inherently too small to represent the **correlated** three-leg roll pair. At fixed reference axes one may choose the representation

    rho(exp(iχ))=(R_X(χ), R_Y(−χ)).

At χ=π/2 this has the two residual rolls of the independent s=−1 loop. More explicitly, on a local chart z_j≠0 the function z_j/|z_j| transforms by the common phase and can feed this representation. This demonstrates mathematical capacity, not an inherited correspondence: axes, phase origin, chart/gauge, and the assignment of the two rolls have been chosen. It supplies neither the intervening station axes nor a native p=3 return. It cannot encode two freely independent SO(3) frames. For μ=−i the inverse roll pair results unless the convention is reversed.

After an identical **full** native-state return, any single-valued current-state map must also return. A diagnostic transported along history may retain a turn, but it is a different mathematical object. Existing observer memory must be included explicitly if used; it cannot silently supply cone-marker memory or a missing leg stage.

## 4. Fixed SRG: real reduction, raw contraction and projective exceptions

Use the accepted Fourier basis f_j=Z^j f0 and frozen values

    q=exp(−.423), r=exp(.577), c=.382,
    alpha=61π/125, beta=61π/250,
    A=RZC, B=exp(−i alpha sigma_z) exp(−i beta sigma_x), U=B⊗A.

Direct multiplication gives Af0=qf1, Af1=qcf2, Af2=rcf0. Since these vectors form a basis,

    A^3=D I3, D=r q² c²=exp(−269/1000)(191/500)^2,
    U^3=D(B^3⊗I3), U^12=D^4(B^12⊗I3).

This is exact for all input states, without normalization. The channel factor returns projectively after three transfers. It need not have minimal projective period three: A eigenvectors already have period one.

### Exact short nonresonance and contraction proofs

The eigenvalues of B are exp(±i vartheta), with cos(vartheta)=t=cos(alpha)cos(beta). Since alpha=π/2−3π/250 and 0<beta<π/2,

    0<t<sin(3π/250),
    0<delta=asin(t)<3π/250,
    vartheta=π/2−delta.

B^12 therefore has eigenvalues exp(±12i delta). They are distinct because 0<12delta<36π/250<π. It is not any scalar matrix. B^3 has eigenvalues exp(±3i vartheta); these also are distinct and differ from the exact quarter-phase pair. For example its eigenvalue ratio is −exp(−6i delta), not 1, using 0<6delta<18π/250<π. No rounded angle supplies an equality.

Also 0<D<1. Unitarity gives ||U^{3m}psi||=D^m||psi||. A nonzero raw p-periodic state would also satisfy U^{3p}psi=psi, contradicting its norm. This excludes **all nonzero raw finite-period orbits of this fixed U**, without an irrationality claim about vartheta and without a trajectory experiment.

| Fixed-constant diagnostic | Display (not an interval certificate) |
|---|---:|
| vartheta | 88.4443098768953 degrees |
| 3 vartheta | 265.332929630686 degrees |
| 12 delta | 18.6682814772564 degrees |
| D | 0.111506840437208 |
| D^4 | 0.000154598772296353 |

These are internal eigenphases and raw amplitude factors. They are not measured 3-D cone angles. The displayed numbers agree at 80 and 100 digits; the preceding elementary inequalities, not decimal agreement, prove the exclusions.

**State-specific refinement.** Write psi=chi_+⊗v_+ + chi_-⊗v_- in the two orthonormal B eigensectors. At either m=3 or m=12, U^m multiplies these summands by D^{m/3} exp(±im vartheta). Their distinctness proves that U^m psi is proportional to psi exactly when only one v-sector is nonzero. Thus every nonzero single-helicity state has a projective return at three and twelve, despite amplitude decay; a mixed-helicity state does not at those steps. Some single-sector states return projectively in one step when v is an A eigenvector. We do not classify every possible longer projective resonance.

### Existing intertwining and the separate initializer

For a normalized B eigenvector chi with eigenvalue b_chi, let Phi_chi=chi†⊗I and T_chi(v)=chi⊗v. Normality supplies the eigenbra identity, giving

    Phi_chi U=(b_chi A)Phi_chi,
    U T_chi=T_chi(b_chi A), Phi_chi T_chi=I.

This is category A: an actual same-step dynamic correspondence between fixed linear state spaces. No cone map is involved. The accepted preparation/extraction route gives

    Omega_initial=sqrt(I_aperture)(chi†xi) b_chi^n b_n f_(n mod 3),
    b_(3m)=D^m, b_(3m+1)=D^m q, b_(3m+2)=D^m q²c.

The full Phi_chi is onto C^3. The admitted lens-prepared family is much smaller: at a fixed n it occupies one Fourier line (possibly zero), and over all n it stays within three lines. Aperture information resides in raw magnitude; normalizing discards it. The native handoff uses the extracted value as an initializer, not as an equivalence of future evolution. Equal-k native Fourier-line invariance does not automatically survive unequal k.

The inherited TARGET:182–224 obstruction is valid and worth preserving: there is no fixed global complex-linear **surjection** Phi from the frozen U to native F with Phi U=F Phi on all raw states, for the real finite parameters considered. If epsilon≠0, a linear right inverse would make F linear, while norm preservation by synchronization leaves cubic growth ||F(tv)||/t³→|epsilon| ||v⊙|v|²||>0. If epsilon=0, native F fixes nonzero f0, whereas U^{3n} decays to zero; a preimage of f0 gives a contradiction. This proof does not assume equal k and covers the special linear projection case g=1/3 as well. Its scope does not exclude nonlinear/restricted maps, a preparation handoff, normalized dynamics or a different sampling convention. No such alternative is installed here.

## 5. Cone transport versus matched face transport

The retained chart is left-handed: x right, y up, z far. Convert using H_chart=diag(1,1,−1). At a quarter turn, the actual chart matrices are

    A = [ 0  1  0 ]   B_s = [ 1  0  0 ]   C = [ 0  0  1 ]
        [-1  0  0 ]         [ 0  0 −s ]       [ 0  1  0 ]
        [ 0  0  1 ]         [ 0  s  0 ]       [-1  0  0 ].

Green follows A,B_s,C; orange follows B_s,C,A. Direct products are

    G3=C B_s A = [−s  0  0 ]   O3=A C B_s = [ 0  0 −s ]
                [ 0  0 −s ]                [ 0 −s  0 ]
                [ 0 −1  0 ]                [−1  0  0 ].

Both initial labelled axes acquire −s after three legs. The inherited repeating extension therefore gives:

| First return in legs | Independent s=+1 | Independent s=−1 | Rigid s=+1 | Rigid s=−1 |
|---|---:|---:|---:|---:|
| Uncolored axis set / colored opposed-pair axes | 3 | 3 | 3 | 3 |
| Persistent labelled axes | 6 | 3 | 6 | 3 |
| Full marked frames | 6 | 12 | 6 | 3 |

For s=−1, conversion gives G3=R_X(+π/2) and O3=R_Y(−π/2). The four three-leg blocks explain 0,3,6,9,12 in the independent marked extension. For s=+1 the three-leg products have order two. In the rigid comparator, the three-leg computational transport is diag(−s,−s,1); it has no marked residual for s=−1. Both branches and both interpolation choices remain distinct. The author did not prescribe the repeating continuation or diagnostic marks.

At equal intermediate progress theta on each independent leg, g·o=−sin(theta)cos(theta). At theta=π/4 the directed angle is 120 degrees and the smaller **unoriented axis** angle is 60 degrees. Unequal progress generally changes this; native equations supply no equal-progress rule. The rigid comparator keeps axes perpendicular and follows a different 120-degree shortest rotation per leg.

### Why the independent cone loop is parallel transport

In computational coordinates, the angular-velocity axes per unit theta are k_A=−e_Z, k_B=−s e_X, k_C=−e_Y. On each actual independent path, direct differentiation verifies u'=k×u and k·u=0 for its cone axis u. For an attached tangent marker v⊥u, the same rigid transport gives v'=k×v. Since |u|=1, k=u×u', and

    v'=(u×u')×v=−u(u'·v).

The derivative is purely normal to the sphere of unit directions. Its tangential component vanishes: this is exactly Levi-Civita parallel transport along the specified great-circle leg. The equality holds piecewise through the three-leg loop, and the matrix products compute its holonomy. It requires no extrapolation from the enclosing reference sphere and no force law. The sphere here is the mathematical sphere of directions; the close enclosing sphere in the sketch remains a passive reference.

The rigid comparator is different: its first computational axis is (−s,s,−1)/sqrt(3), which has nonzero projection on both e_X and e_Y. It includes own-axis spin and is not this no-own-spin transport. Its return counts must not be substituted for the independent construction.

### Matched face transport and the scoped obstruction

Let E_i=[t_i,e_z] with E_i^T E_i=I2, so T_ij=E_i E_j^T. Then

    T_ij T_jk=E_i(E_j^T E_j)E_k^T=T_ik.

A closed loop is E_i E_i^T, the ambient tangent projector, whose restriction to W_i is the identity. It is **not** the ambient I3; rank-two T_ij are not full SO(3) rotations. The verification uses an equivalent planar matched basis, while the proof works for every such orthonormal face basis, including the inherited geometry.

If each label has a fixed invertible frame identification S_i, transformed transports S_i T_ij S_j^{-1} have closed-loop map S_i I S_i^{-1}=I on the tangent space. They cannot produce the nonidentity transverse quarter-turn of the s=−1 independent cone loop. This is category E for **single-valued, fixed per-label identifications of these connections**. It says nothing universal about state-dependent maps or other transports. The missing native evolution relation cannot be supplied by relabeling frames alone.

## 6. Independent disposition of GPT's lead

| Lead | Review outcome |
|---|---|
| Pi/J/Q and native covariance | Confirmed with proper regularity. Added complete nonzero state-period classification, epsilon=0 qualification, and an explicit Q-specific zero-stratum failure. |
| Conditional native coherence return | Confirmed. Strengthened: one regular returning block propagates regularity, rather than requiring a separate future-domain assumption for that block. This is not a proof of existence. |
| Normalized shape distinction | Confirmed and sharpened with exact nonlinear amplitude counterexample. No repeated scale multiplier or closed projector dynamics may be presumed. |
| D1/M3/coherent controls | Confirmed within their different parameter/domain hypotheses. Added the M3 current-state period-divisibility obstruction; inherited certificates were not replayed. |
| Hidden phase versus two frames | No inherited dictionary found. A conditional opposite-weight U(1) representation shows why a blanket dimensional impossibility claim would overreach. Intervening leg stages still lack a native derivation. |
| Fixed SRG short bound and decay | Confirmed analytically. Added exact three-/twelve-step projective eigensector classification; retained the genuine extraction/injection and inherited global-linear-surjection obstruction. |
| Transport mismatch | Confirmed only in the stated fixed-frame class. Derived the actual no-own-spin parallel-transport connection from the signed paths; did not infer it from the image of a sphere. |

The memo's main mathematical reasoning survives independent review. Its central bridge remains conditional; matching counts does not supply the absent intertwining. The observer clarification and normalized-shape refinement prevent broader claims than the sources permit.

## 7. Verification and limitations

`verify.py` passed **46 checks, zero failed, zero execution errors**. These are check groups, not 46 new theorems. Exact SymPy work checks comparison spectra/powers, amplitude covariance, cone products against retained JSON, the actual angular-velocity identities, matched transport, SRG cycle and tensor reduction. Native transcription uses **eight predeclared cases, nine updates total, maximum two per case** at 80 decimal digits. `CASES.md` was written before evaluation and its hash is recorded in `results.json`.

N2/N3 covariance residual was 0 at the working precision; N2 H-closure discrepancy was about 4.22e−81. N4's unchanged-unequal-k mismatch was about 4.47213e−4. These are diagnostics; the general covariance identity and zero-stratum failures have separate exact proofs above. Exact rational N8 values validate the nonlinear amplitude distinction. All original inputs, prestages, kicks, outputs and exact zeros are retained. No clipping or altered zero handling was used.

Environment: Windows AMD64, `C:\Users\Notandi\miniconda3\envs\torment\python.exe`, Python 3.11.15, SymPy 1.14.0, mpmath 1.3.0 (NumPy 2.4.4 installed but not needed by this verifier). Execution used Command Prompt, `call conda activate torment`, and `python -X utf8 -I -B`. Native diagnostics were run once; a separate 80/100-digit SRG display comparison is not an interval certificate. Analytical theorems require mathematical review, not only passing software checks.

No accepted long-run certificate or earlier QA suite was rerun. No new figure was needed: the exact products answer the question more directly than another animation. No global absence of native twelve-cycles, no novelty claim, no spatial spin/energy assignment, and no physical motion law is established. Before/after hashing covers only the 18 listed inspected inputs, not the whole checkout or machine. Final preservation and archive results are in `CLOSEOUT.txt` and the archive receipt.

## 8. Simple explanation and paper readiness

Your observation points to a real mathematical question: **can something look returned while some information has not returned?** The native equations can do that. A common complex phase can change while the relative pattern and size stay the same; D1 is an existing example. In the cone drawing, an added stripe can turn while an unmarked cone looks unchanged. These are comparable distinctions, but they are not yet the same mechanism.

Three has three separate origins here: a prescribed cone route, a channel permutation, and the fixed SRG channel transfer. Four can come from multiplying by i, or from repeating a particular marked-cone quarter-roll. Their product does not prove the native model performs either operation. The useful result is the exact test: find a real native coherence return, compute its leftover phase, and only then determine a full return count. None was tuned or manufactured in this investigation.

**Readiness decision:** there is substantive established-model mathematics for a focused scientific review, but this is **not ready for a paper claiming native cone motion or a native twelve-period spin**. A standalone manuscript is not recommended yet: much of the positive content is inherited, and the new return and obstruction statements are elementary, useful corollaries whose novelty has not been assessed. They are suitable candidate lemmas or an appendix in a future source-grounded account.

The reviewable candidate claims are the regular-block return theorem (including the projector limitation), the M3 period-divisibility consequence, and the precise transport/SRG exclusions. Remaining evidence for a stronger motion claim would be an actual unchanged-native branch or orbit satisfying the return hypotheses, plus a justified single-valued state/observable-to-pose map and an explicit evolution identity such as R(F^m z)=K(R(z)) on a stated domain. Any leg-stage information must come from that established state, not an appended schedule. Those are missing mathematical relations, not a request for the author to invent a new law. Motion integration is parked at this boundary; nothing is published.
