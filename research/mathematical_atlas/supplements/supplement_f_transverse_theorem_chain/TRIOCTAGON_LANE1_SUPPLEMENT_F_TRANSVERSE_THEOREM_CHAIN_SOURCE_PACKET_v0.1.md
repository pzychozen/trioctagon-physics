# Tri-Octagon Mathematical Atlas — Lane-1 Closeout Supplement F

**Transverse group actions, jets, local spectrum, limiting coefficients and phase response.**

Date: 2026-09-29. Version v0.1. External source packet; not Atlas 10, a paper revision, or publication.

Scope: F02–F06 only. The authoritative repository is C:\TORMENT\TRIOCTAGON_new\trioctagon-physics at expected and observed HEAD 34c21830e7e7c4b5f4a5a940d084c37feaf1f82c. Supplement A and every prior source/Atlas/review remain read-only.

## 1. Frozen hypothesis ladder

This ladder was recorded from the accepted Paper-F ledger before the independent coefficient reconstruction.

| Item | Hypotheses | Permitted use |
|---|---|---|
| H0 | Omega in C³; real parameters; k=(1,1,1); e=(1,1,1), L3=eeᵀ−3I; amplitude/coupling update precedes simultaneous phase synchronization | Defines the map and its equal-channel symmetries |
| H1 | Local chart near e, all pre-sync entries and mean nonzero, common phase fixed by positive-real mean | Real-analytic quotient and local angle branches |
| H2 | Seed e+i h q(phi), h>0 sufficiently small; psi=atan2(C·(−q),C·q_perp) | Oriented seed-circle observable |
| H3 | lambda=0; polynomial finite-n jets allow unrestricted real parameters/r; a=1−3g≠0 for division defining kappa; a>0 for chosen oriented branch | Fixed-n local Taylor law only; no uniform-in-n remainder asserted |
| H4 | 0<r<a<1; r=a−2epsilon; m=1−a+r; spectrum (m,r,r,a,a) nonresonant | Analytic asymptotic bridge, not a restriction on polynomial finite jets |
| H5 | epsilon=1/20, g=1/5, a=2/5, r=3/10, m=9/10 | Historically selected specialization; motivation remains OPEN |
| H6 | Open real interval about lambda=0; b=a(1−9lambda); 0<r<b<1; 0<m<1; spectrum (m,r,r,b,b) nonresonant; common nonzero chart, uniformity on compact subintervals | Joint analytic limit argument; computed lambda expansion only through first order |

At H5, the accepted resonance-free component is
\[
J=(-7/2187,\;12579511/3600000000).
\]
The convenient symmetric sufficient choice is \(|\lambda|<7/2187\). No endpoint uniformity is claimed.

Dependency DAG (each arrow means proof dependence, not a runtime pipeline):

~~~mermaid
flowchart TD
 H0 --> G["F02: group, orbits, invariant fixed spaces"]
 H2 --> G
 H0 --> JET["F03: exact one-step and complete finite jets"]
 H2 --> JET
 H3 --> JET
 JET --> SUM["F04: formal infinite coefficient sum"]
 DECAY["|a|<1, |r|<1, a nonzero"] --> SUM
 H0 --> SPEC["F05: five-coordinate spectrum"]
 H1 --> SPEC
 H5 --> VAL["All-degree valuation nonresonance at H5"]
 SPEC --> LIN["External analytic linearization application"]
 H4 --> LIN
 VAL --> LIN
 LIN --> BRIDGE["F04: uniform h-disk, observed local limit"]
 H2 --> BRIDGE
 SUM --> BRIDGE
 JET --> PHASE["F06: full-composition first lambda derivative"]
 H1 --> PHASE
 H6 --> PARAM["Uniform parametric chart and interchange"]
 SPEC --> PARAM
 LIN --> PARAM
 PHASE --> RES["Differentiated coefficient resolvent"]
 SUM --> RES
 RES --> FINAL["F06: observed first-order limiting law"]
 PARAM --> FINAL
 BRIDGE --> FINAL
~~~

H5 is an example satisfying H4, not a hidden assumption in parameter-general algebra. The arrow from its valuation lemma to linearization supplies only that specialization; general H4 nonresonance is assumed separately. H6 extends the local bridge on compact parameter subintervals. State amplitudes contract even when a projective direction is constant.

Evidence labels used throughout: EXACT_SYMBOLIC, ANALYTIC_PROOF, EXTERNAL_THEOREM_APPLICATION, FINITE_ENUMERATION, HIGH_PRECISION_REFERENCE, BINARY64_RUNTIME_WITNESS, ORACLE_VERSUS_PAPER_ONLY, HISTORICAL_FIXTURE, NEGATIVE_FALSIFIER. Analytic arguments are not certified by a finite predicate count.

## 2. Controlling sources and runtime boundary

| ID | Exact current source | Use |
|---|---|---|
| PF | [Paper F publication v0.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md) | Accepted equations, Theorems 4–8, Appendices A/B/D |
| PL | [Theorem/provenance ledger v0.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_THEOREM_AND_PROVENANCE_LEDGER_v0.2.md) | Hypotheses and proof dependencies; its preparation-time candidate wording does not reverse publication acceptance |
| Census | [Source census](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_SOURCE_CENSUS.md) | Resolves CT/AX/CG/NF and their chronology |
| CT | [Chiral transverse report](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/CHIRAL_TRANSVERSE_REPORT.md) | §§2–3 intrinsic Jacobian/chirality; separate registration geometry is not imported into this proof |
| AX | [Axis falsification report](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION_REPORT.md) | Fixed-space formulas and historical 18-row diagnostic |
| CG | [Generic-transverse review](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/CLAUDE_GENERIC_TRANSVERSE_HARMONICS_REVIEW.md) | Earlier finite-range proposal and phase-only observable |
| NF | [Normal-form closeout](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_NORMAL_FORM_CLOSEOUT.md) | Accepted-chain predecessor: arbitrary-step algebra and full-composition coefficient |
| CR | [Adversarial review v0.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/reviews/CLAUDE_PAPER_F_ADVERSARIAL_REVIEW_v0.1.md) | Its v0.1 review and suggested strengthening, incorporated in v0.2; not a new review of this supplement |
| PF-check | [Preserved verifier](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py) | Inspected after new algebra existed; neither imported nor executed |
| PF-record | [Recorded validation](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_v0.2_VALIDATION.json) | Read only after independent results for comparison; its 131 predicates are not added to this task's count |
| K2C | [Analytic parity receipt](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.md) | Existing finite parity and explicit infinity exclusions |
| Oracle | [Paper F parity oracle](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/parity_oracles/paper_f_oracle.py) | Inspected after independent derivation; never imported by the new checker |
| Test | [P7/P8 test file](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_parity_p07_p08.py) | Only focused repository test executed, separately from new mathematics |

The completeness review, crosswalk and Supplement A are recorded as unchanged inputs in the result hashes. F02–F06 remain **RESEARCH_ONLY** theorem/proof families. The relevant current runtime bodies are [step3/L3](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py) and [z_chiral](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py). Inspection confirms amplitude/coupling first, simultaneous phase second, raw unnormalized chirality. No normal-form engine, coefficient-resolvent evolution, dynamics-controlling orbit classifier, six-axis selector or limiting-angle state is introduced.

Use the exact real-arithmetic recurrence
\[
\widetilde\Omega_j=\Omega_j+\epsilon\Omega_j(1-|\Omega_j|^2)
 +g\left(\sum_l\Omega_l-3\Omega_j\right),\qquad
\Omega_j^+=|\widetilde\Omega_j|
 e^{i[p_j+\lambda\sum_l\sin3(p_l-p_j)]}.
\]
Here \(p_j=\operatorname{Arg}_0\widetilde\Omega_j\); self-pair terms vanish. All phases in a step use the same pre-sync vector. On H1 a common analytic phase branch is available. At lambda=0 the phase stage is the identity. The mathematical calculations are not bitwise claims about binary64 arithmetic.

## 3. F02: basis, exact group action and orbits

**EXACT_SYMBOLIC / ANALYTIC_PROOF.** Put
\[
u=(1,-1,0)/\sqrt2,\quad v=(1,1,-2)/\sqrt6,\quad
\widehat e=e/\sqrt3,\quad E=[u\ v].
\]
Direct products give \(u\cdot u=v\cdot v=1\), \(u\cdot v=0\), \(e\cdot u=e\cdot v=0\). The cross product is
\((2,2,2)/\sqrt{12}=e/\sqrt3\), fixing positive orientation.
Define \(q=u\cos\phi+v\sin\phi\) and \(q_\perp=-u\sin\phi+v\cos\phi\).
Because \(e\times u=\sqrt3v\), \(e\times v=-\sqrt3u\),
\[
e\times q=\sqrt3q_\perp.
\]

The actual channel permutation \(P(A,B,C)=(C,A,B)\), and transposition \(T=(12)\), have matrices
\[
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\quad
T=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}.
\]
Taking \(E^TPE\) and \(E^TTE\) gives
\[
P_V=\begin{pmatrix}-1/2&-\sqrt3/2\\\sqrt3/2&-1/2\end{pmatrix},
\quad T_V=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
Matrix multiplication proves \(P_V^3=T_V^2=I\), \(T_VP_VT_V=P_V^{-1}\). The six matrices \(P_V^iT_V^j\), \(0\le i<3,0\le j<2\), are distinct. Thus the faithful action is \(S_3\simeq D_3\), with
\(P:\phi\mapsto\phi+2\pi/3\), \(T:\phi\mapsto\pi-\phi\).

Conjugation of \(e+ihq\) gives \(e+ih(-q)\), so on the seed circle it acts as \(J=-I\), \(\phi\mapsto\phi+\pi\). Real channel permutation matrices commute with it. \(JP_V^2\) is rotation by \(\pi/3\), and adjoining J gives twelve distinct matrices, the planar \(D_6\). Our convention is \(|D_n|=2n\). This channel seed-circle action is not the ambient Paper-C shell action, nor the deck action of Atlas 02; equal group names/orders do not identify the actions.

For roots \(\phi_k=k\pi/6\), the generators act as \(k\mapsto k+4\) and \(k\mapsto6-k\) modulo 12. Direct application gives:

| Action | Orbits | Stabilizer size |
|---|---|---|
| Oriented D3 | {0,2,4,6,8,10}; {1,5,9}; {3,7,11} | 1; 2; 2 |
| Oriented D6, adding k→k+6 | even k; odd k | 2; 2 |
| Projective D3, k modulo 6 | {0,2,4}; {1,3,5} | 2; 2 |

Orbit-stabilizer agrees with enumeration. For example \(u=q(0)\) has no nonidentity D3 stabilizer, so its orbit has six elements. \(v=q(\pi/2)\) is fixed by T, with stabilizer {I,T}; its D3 orbit has three elements. Its negative lies in the other odd orbit. Thus “two oriented D3 orbits” and “one six-element oriented v-type D3 orbit” are false. D6's size-six orbits are not regular: its group order is twelve.

## 4. F02: full-state isotropy and chirality

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** In the extended group u is fixed by JT and v by T. Solve these equations on the full complex state, not merely on the seed circle.

\(T\overline\Omega=\Omega\) means \(\Omega_1=\overline{\Omega_2}\) and \(\Omega_3=\overline{\Omega_3}\), giving
\[
\Omega=(x+iy,x-iy,z),\quad x,y,z\in\mathbb R.
\]
\(T\Omega=\Omega\) means the first two channels are equal, giving
\[
\Omega=(\alpha+i\beta,\alpha+i\beta,\gamma+i\delta),
\quad\alpha,\beta,\gamma,\delta\in\mathbb R.
\]
These fixed spaces have real dimensions three and four respectively. The scalar onsite function commutes with conjugation and channel permutations for real parameters and equal k. L3 does likewise. The simultaneous phase stage relabels all pair differences under permutations and changes signs of both phases and sine increments under conjugation. Integer harmonic phases respect \(2\pi\) branch changes; Arg0(0)=0 respects conjugation. Therefore the full recurrence preserves both fixed spaces. This does not assert attraction into them.

Crossing real and imaginary parts directly gives
\[
C_u=y(z,z,-2x),\qquad C_v=(\alpha\delta-\gamma\beta)(1,-1,0).
\]
\(C_u\) lies in the plane with first two coordinates equal, spanned by e and v. Its transverse part is
\[
(C_u)_\perp=\frac{y(z+2x)}3(1,1,-2),
\]
and its e-parallel part is \(2y(z-x)e/3\). Thus the transverse projective line is fixed while elevation can vary. Total \(C_u=0\) iff \(y=0\) or \(x=z=0\). Its transverse part can vanish when \(y(z+2x)=0\) even if its total vector is nonzero.

\(C_v\) lies on a fixed transverse line, and is zero exactly when \(\alpha\delta=\gamma\beta\). The two displayed chirality expressions have zero dot product for all permitted amplitudes. In particular, the u-type transverse line is perpendicular to the v-type line, and even u-type elevation preserves orthogonality to v-type. The entire u-type chirality is not asserted to lie on one fixed spatial line.

Directions/angles exist only for the respective nonzero vectors/projections. Outside the local oriented branch, signs can reverse. AX's eighteen saved rows are a **HISTORICAL_FIXTURE / BINARY64_RUNTIME_WITNESS**; they are not used to prove these exact fixed-space statements and are not replayed or reassessed here.

## 5. F03: exact one-step chirality and angle

**EXACT_SYMBOLIC.** Let \(a=1-3g\), \(S=\sin3\phi\), \(s_2=q(\pi/2-2\phi)\).
Expanding the explicit components gives
\[
q^{\circ2}=e/3+s_2/\sqrt6,\quad
q^{\circ3}=q/2+Se/(3\sqrt6),\quad
q\circ s_2=q/\sqrt6+Se/3.
\]
On the seed, \(1-|\Omega_j|^2=-h^2q_j^2\), L3e=0, and L3q=−3q. Therefore exactly at lambda=0,
\[
\Re\Omega_1=e-\epsilon h^2q^{\circ2},\quad
\Im\Omega_1=ahq-\epsilon h^3q^{\circ3}.
\]
Their cross product is
\[
C_1=ah(e\times q)-\epsilon h^3
 [e\times q^{\circ3}+a(q^{\circ2}\times q)]
 +\epsilon^2h^5(q^{\circ2}\times q^{\circ3}).
\]
This expansion, followed by scalar products against \(q_\perp,q,\widehat e\), independently yields:
\[
\begin{aligned}
A_C&=\sqrt3h\left[a-\epsilon h^2(2a+3)/6
                   +\epsilon^2h^4(5+\cos6\phi)/36\right],\\
B_C&=\sqrt3\epsilon^2h^5\sin6\phi/36,\\
D_C&=\sqrt6\epsilon h^3(2a-\epsilon h^2)\cos3\phi/12.
\end{aligned}
\]
The checker substitutes \(q=u c+v s\), expands the three cross-product projections and reduces their residuals by \(c^2+s^2-1\). Each residual is exactly zero, with symbolic a, epsilon and h. No saved PF-check result supplies this calculation.

For H3's a>0 branch, \(C\cdot q_\perp=\sqrt3ah+O(h^3)>0\), and
\[
\psi_1=\operatorname{atan2}(-B_C,A_C)
=-\frac{\epsilon^2}{36a}h^4\sin6\phi+O(h^6).
\]
The \(h^2\) denominator correction makes only an \(h^6\) angular correction; the cubic term in arctan begins still later. Only after this parameter formula, H5 gives
\(-\epsilon^2/(36a)=-(1/400)/(72/5)=-1/5760\).
The polynomial C1 identity is exact at finite h. The angle law is a local Taylor statement, not equality to a finite-amplitude angle.

## 6. F03: symmetry forces order and harmonics, not coefficients

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** Chirality is a channel pseudovector:
\(C(P\Omega)=\det(P)PC(\Omega)\), and \(C(\overline\Omega)=-C(\Omega)\).
In the moving basis \(q_\perp,q,\widehat e\), a 3-cycle gives \(2\pi/3\) periodicity. Conjugation preserves A_C and B_C, but reverses D_C. A transposition preserves A_C and reverses B_C,D_C. On the local angle branch these imply period \(\pi/3\) and reflection oddness for psi, hence only \(\sin(6j\phi)\); elevation permits \(\cos(3(2j+1)\phi)\).

The degree bound must precede unit-circle restriction. On the full plane V, write \(C(e+ihq)=\sum h^k c_k(q)\). Each coefficient is homogeneous of degree k because the seed enters through hq. Conjugation makes k odd. The scalar polynomial \(c_k(q)\cdot q\) is alternating and has even degree k+1.

Set
\[
I_3=\sum q_j^3,\qquad
\Delta=(q_1-q_2)(q_2-q_3)(q_3-q_1).
\]
On V, every alternating polynomial vanishes on the three distinct lines \(q_i=q_j\). Their relatively prime linear factors therefore divide it, so it is \(\Delta\) times a symmetric polynomial. The symmetric-polynomial algebra on \(q_1+q_2+q_3=0\) is generated by the quadratic and cubic elementary invariants. There is no nonzero symmetric linear polynomial there. Alternating even degree two is below degree three of Delta; at degree four the remaining symmetric degree-one factor is zero. At degree six the remaining symmetric cubic is proportional to \(I_3=3q_1q_2q_3\). Degree six is the first allowed alternating-even term.

Now restrict to unit norm and calculate components:
\[
I_3=\sin3\phi/\sqrt6,\qquad
\Delta=\cos3\phi/\sqrt2,\qquad
4\sqrt3 I_3\Delta=\sin6\phi.
\]
Thus B_C first permits \(h^5\sin6\phi\), and division by leading order-h chirality first permits \(h^4\sin6\phi\) in psi. The checker's exact homogeneous linear-constraint calculation gives dimensions 0,0,1 at degrees 2,4,6.

This is **SYMMETRY_FORCED_STRUCTURE**. The coefficient \(\sqrt3\epsilon^2/36\) is **RECURRENCE_SPECIFIC_COEFFICIENT**. Setting epsilon=0 leaves the symmetry intact and makes it vanish, explicitly falsifying coefficient determination from symmetry alone. This argument concerns a consequence of the adopted recurrence and does not reopen the historical reason for choosing harmonic three.

## 7. F03: complete vector jets and structural closure

**EXACT_SYMBOLIC / ANALYTIC_PROOF.** Work before fixing common phase, retaining all common modes:
\[
\Re\Omega_n=e+h^2x_n+h^4u_n+O(h^6),\quad
\Im\Omega_n=hy_n+h^3v_n+h^5w_n+O(h^7).
\]
Here lower-case x,u,y,v,w are coefficient vectors, not basis vectors or evolved truncated states. Let
\[
L_Iz=az+(1-a)e(e^Tz)/3,\quad
L_Rz=rz+(1-a)e(e^Tz)/3,\quad r=a-2\epsilon,\quad m=1-2\epsilon.
\]
Substitute the two series into \(\Omega+\epsilon\Omega(1-|\Omega|^2)+gL_3\Omega\) and collect powers. This derives the entire vector system:
\[
\begin{aligned}
y'&=L_Iy,\\
x'&=L_Rx-\epsilon y^{\circ2},\\
v'&=L_Iv-\epsilon(2x\circ y+y^{\circ3}),\\
u'&=L_Ru-\epsilon(3x^{\circ2}+2y\circ v+x\circ y^{\circ2}),\\
w'&=L_Iw-\epsilon(2x\circ v+2u\circ y+x^{\circ2}\circ y+3y^{\circ2}\circ v).
\end{aligned}
\]
In particular the coefficient on \(x^{\circ2}\circ y\) is one. Initial conditions are \(y_0=q\), with x0,u0,v0,w0 zero.

Every channel coefficient is a polynomial in its own initial q_j with symmetric coefficients in the triple. This holds initially; pointwise multiplication and summation over channels preserve it. On V the symmetric coefficients reduce to polynomials in \(\sum q_j^2\) and \(\sum q_j^3\). The three channel values have characteristic polynomial
\[
\prod_j(t-q_j)=t^3-\tfrac12t-\frac{S}{3\sqrt6}
\]
on the unit circle: the pair sum is −1/2 and the product is \(I_3/3=S/(3\sqrt6)\).
Thus t represents one channel q_j, not time. The exact algebra
\[
t^3=t/2+S/(3\sqrt6)
\]
reduces every channel polynomial to degree at most two in t. For \(b_0+b_1t+b_2t^2\), its channel trace is \(3b_0+b_2\).
With \(s_2=\sqrt6(t^2-1/3)\), the basis is e,q,s2. This is an algebraic identity, not a fit.

Homogeneity on the full plane fixes which S powers accompany that basis. Through degrees one to five: odd imaginary degree one permits q; degree two permits e,s2; degree three permits q,Se; degree four permits e,s2,Sq; degree five permits q,Se,Ss2. For example a coefficient \(S^2q\) has underlying degree seven and cannot appear in a degree-five jet. Powers of the quadratic invariant account for the lower-degree representatives after unit restriction.

Accordingly the closed ansatz, retaining every coefficient, is
\[
\begin{aligned}
y&=Aq,&x&=Me+Xs_2,&v&=Bq+DSe,\\
u&=U_0e+U_ss_2+ESq,&
w&=P_{\!j}q+Q_{\!j}Se+RSs_2.
\end{aligned}
\]
Here Pj,Qj are jet scalars, not the permutation P. A0=1 and every other scalar starts at zero. Useful further reductions are
\[
s_2^{\circ2}=e/3-s_2/\sqrt6+\sqrt{2/3}Sq,\qquad
q^{\circ5}=q/4+5Se/(18\sqrt6)+Ss_2/18.
\]

## 8. F03: all scalar recurrences, including Pj and Qj

**EXACT_SYMBOLIC.** Expanding §7's complete vector system and extracting the e,q,s2 coefficients gives the following full system. A prime denotes one coefficient update, with all right-hand quantities evaluated before it:
\[
\begin{aligned}
A'&=aA,\\
M'&=mM-\epsilon A^2/3,\\
X'&=rX-\epsilon A^2/\sqrt6,\\
B'&=aB-\epsilon(2AM+2AX/\sqrt6+A^3/2),\\
D'&=D-\epsilon(2AX/3+A^3/(3\sqrt6)),\\
U_0'&=mU_0-\epsilon(3M^2+X^2+2AB/3+A^2M/3+A^2X/(3\sqrt6)),\\
U_s'&=rU_s-\epsilon(6MX-3X^2/\sqrt6+2AB/\sqrt6+A^2M/\sqrt6+A^2X/6),\\
E'&=rE-\epsilon(\sqrt6X^2+2AD+A^2X/3),\\
P_{\!j}'&=aP_{\!j}-\epsilon\big[
 3A^2B/2+AM^2+2AMX/\sqrt6+2AU_0+2AU_s/\sqrt6
 +AX^2/6+2BM+2BX/\sqrt6\big],\\
Q_{\!j}'&=Q_{\!j}-\epsilon\big[
 A^2B/\sqrt6+A^2D+2AE/3+2AMX/3+2AU_s/3
 +AX^2/(3\sqrt6)+2BX/3+2DM\big],\\
R'&=aR-\epsilon(2XD+2AE/\sqrt6+AX^2/3+3A^2D/\sqrt6).
\end{aligned}
\]
Initial data: A=1 and M=X=B=D=U0=Us=E=Pj=Qj=R=0.
These formulas include all real coefficients through h4 and all imaginary coefficients through h5. D and Qj are imaginary common modes with linear multiplier one in this ungauged calculation; they must not be discarded merely because the later quotient removes common phase.

The checker independently expands real and imaginary cubic polynomials before invoking the root relation, verifies each of the five vector identities, and extracts all eleven scalars. In particular Pj and Qj are newly printed explicitly here rather than set to zero or hidden behind their absence from the final angular formula.

## 9. F03: arbitrary fixed-n angular coefficient

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** The complete cross product expands as
\[
C=h\,e\times y+h^3(e\times v+x\times y)
 +h^5(e\times w+x\times v+u\times y)+O(h^7).
\]
Projecting onto −q gives zero at order h3, and
\[
C\cdot(-q)=\frac{\sqrt3}{2}(R-XD)h^5\sin6\phi+O(h^7),
\quad C\cdot q_\perp=\sqrt3Ah+O(h^3).
\]
Define the source variables
\[
F=E+AD,\qquad K=R-XD,\qquad \kappa=K/(2A).
\]
F and K are coefficient combinations, not state variables. This establishes, for every **fixed finite n**, with a>0,
\[
\psi_n=\kappa_n h^4\sin6\phi+O(h^6),\qquad A_n=a^n.
\]
The neighborhood and Taylor remainder here may depend on n. The underlying coefficient recurrence permits all real a,r; dividing by \(2a^n\) requires a≠0, and the chosen atan2 branch additionally requires a>0.

Substitute §8 into F′=E′+A′D′ and K′=R′−X′D′. Using a−r=2epsilon cancels common-phase pieces only after they have been included:
\[
F'=rF-\epsilon\left(\sqrt6X^2+\frac{1+2a}{3}A^2X+
\frac{a}{3\sqrt6}A^4\right),
\]
\[
\Delta_{n+1}:=\kappa_{n+1}-\kappa_n
=-\frac{\epsilon F_n}{a\sqrt6}
 +\frac{\epsilon(2r-1)X_n^2}{6a}
 +\frac{\epsilon(r-2\epsilon)A_n^2X_n}{6a\sqrt6}
 -\frac{\epsilon^2A_n^4}{36a}.
\]
M,B,D,U0,Us,Pj,Qj cancel from this final increment; that cancellation does not justify omitting them from the full jet construction.

Let \(t_0=f_0=0\), and define polynomial recurrences
\[
t_{n+1}=rt_n+a^{2n},\qquad
f_{n+1}=rf_n+\epsilon^2t_n^2-\epsilon(1+2a)a^{2n}t_n/3+a^{4n+1}/3.
\]
Then \(X_n=-\epsilon t_n/\sqrt6\), \(F_n=-\epsilon f_n/\sqrt6\), as follows by induction from their updates and initial data. At epsilon=0 these identities still hold; no division by epsilon is needed to define f. The increment is
\[
\Delta_{n+1}=\frac{\epsilon^2}{36a}
 [6f_n+\epsilon(2r-1)t_n^2-(r-2\epsilon)a^{2n}t_n-a^{4n}].
\]
Unrolling t gives the polynomial convolution
\[
t_n=\sum_{j=0}^{n-1}r^{n-1-j}a^{2j}
=\frac{a^{2n}-r^n}{a^2-r}\quad(a^2\ne r).
\]
The sign is fixed by \(X_1=-\epsilon/\sqrt6\). This independently reproduces the accepted correction to CG's printed sign without editing CG.

## 10. F03/F04: forcing rates, finite formula and collisions

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** Put \(d_0=a^2-r\) (not a dimension). When \(d_0\ne0\), expanding t² and \(a^{2n}t\) gives forcing rates
\(\rho_1=a^4,\rho_2=a^2r,\rho_3=r^2\), with coefficients
\[
b_1=\epsilon^2/d_0^2-\epsilon(1+2a)/(3d_0)+a/3,\quad
b_2=-2\epsilon^2/d_0^2+\epsilon(1+2a)/(3d_0),\quad
b_3=\epsilon^2/d_0^2.
\]
Hence
\[
f_n=\sum_{i=1}^3b_i\frac{\rho_i^n-r^n}{\rho_i-r}.
\]
This follows for arbitrary n from the convolution identity
\[
C_n(p,q)=\sum_{j=0}^{n-1}q^{n-1-j}p^j,\quad
C_{n+1}=qC_n+p^n,\quad C_0=0,
\]
and \(C_n=(p^n-q^n)/(p-q)\) when p≠q. It is not a fit to a finite sequence. Substitution into §9 proves that \(\Delta_{n+1}\) is a linear combination of
\[
a^{4n},\quad(a^2r)^n,\quad r^{2n},\quad r^n.
\]
An index shift preserves these rate families only when division by their rates is allowed; the displayed n+1 indexing also accommodates zero rates through the recurrences.

Define \(H_n(z)=\sum_{j=0}^{n-1}z^j\), so \(H_n(1)=n\). Summing increments from n=0 yields
\[
\begin{aligned}
T_{2,n}&=[H_n(a^4)-2H_n(a^2r)+H_n(r^2)]/d_0^2,\\
T_{A,n}&=[H_n(a^4)-H_n(a^2r)]/d_0,\\
F_n^\Sigma&=\sum_i b_i[H_n(\rho_i)-H_n(r)]/(\rho_i-r),\\
\kappa_n&=\frac{\epsilon^2}{36a}
[6F_n^\Sigma+\epsilon(2r-1)T_{2,n}
 -(r-2\epsilon)T_{A,n}-H_n(a^4)].
\end{aligned}
\]

Every distinct-rate denominator is now visible: \(d_0=a^2-r\), the three \(\rho_i-r\), and, if rational rather than polynomial H is used, \(1-a^4\), \(1-a^2r\), \(1-r^2\), \(1-r\). Expanding \(\rho_i-r\) gives \(a^4-r\), \(r(a^2-1)\), \(r(r-1)\). The angular construction additionally divides by a (or by \(2a^n\)).

At p=q the polynomial convolution gives
\[
C_n(q,q)=nq^{n-1}\quad(n\ge1),\qquad C_0=0.
\]
At q=0 this is interpreted as the polynomial convolution: C1=1, Cn=0 for n>1, not an ambiguous zero-power convention. Thus \(t_n=nr^{n-1}\) when a²=r; each coincident \(\rho_i=r\) uses the same divided-difference limit. Hn(1)=n removes the H denominators. Simultaneous collisions use the polynomial convolution expressions before taking limits, or their repeated derivatives. They remain regular because the complete jets are polynomial recurrences at every fixed n.

For a≠0, division by \(2a^n\) preserves this removable-collision property for kappa_n. It does not make kappa_n polynomial at a=0:
\(\kappa_1=-(a-r)^2/(144a)\) already has a possible pole. The checker verifies the general divided-difference limit and exact finite recurrences at representative simultaneous collisions, labelled **FINITE_ENUMERATION**, separately from this proof.

## 11. F04: exact formal infinite coefficient, before any observed-limit claim

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** Assume only \(|a|<1,|r|<1,a\ne0\).
Let \(\rho=\max(|a|^2,|r|)<1\). The polynomial convolution bound gives
\(|t_n|\le n\rho^{n-1}\). Its quadratic forcing and the filter r show that f_n is bounded by a polynomial in n times a decaying geometric sequence (choose any larger rate below 1 if necessary). All increment terms are absolutely summable, including collisions and negative a or r.

Write
\[
T_4=(1-a^4)^{-1},\quad
T_2=\frac{T_4-2(1-a^2r)^{-1}+(1-r^2)^{-1}}{(a^2-r)^2},
\quad
T_A=\frac{T_4-(1-a^2r)^{-1}}{a^2-r}.
\]
These are respectively \(\sum a^{4n},\sum t_n^2,\sum a^{2n}t_n\), with collision values interpreted as above. Summing the f recurrence gives
\[
\sum_{n\ge0}f_n=
\frac{\epsilon^2T_2-\epsilon(1+2a)T_A/3+aT_4/3}{1-r}.
\]
Insert this into §9's summed increments and only then use \(\epsilon=(a-r)/2\). Exact rational cancellation gives
\[
\boxed{\kappa_\infty(a,r)=
-\frac{(a-r)^2N(a,r)}
{288a(1+a)(1+a^2)(1-r)^2(1+r)(1-a^2r)}},
\]
\[
N=4a^3r^2+3a^3r-4a^3+a^2r^2-4a^2+4ar^2-a-2r^2-3r+2.
\]
None of the remaining denominator factors vanishes in the stated domain. The cancelled rate-collision poles are removable. The checker computes this independently both from the scalar sums and from the coefficient matrix resolvent derived in §17; the two rational functions coincide.

Now specialize H5. The exact polynomial N is \(-428/3125\), and \((a-r)^2=1/100\). Thus the unsimplified substitution is
\[
\frac{(1/100)(428/3125)}
{288(2/5)(7/5)(29/25)(7/10)^2(13/10)(119/125)}
=\boxed{\frac{13375}{1107936648}}.
\]
This fraction is obtained by exact rational arithmetic, not decimal fitting or a saved expected-output lookup. Also \(\kappa_1=-1/5760\) and \(\kappa_2=-347/7200000\); the first and limiting signs differ.

**This is so far a formal coefficient sum.** Fixed-n Taylor expansions alone do not allow interchanging n→infinity with h→0 or coefficient extraction. Even the existence of pointwise real limits is insufficient. A concrete falsifier is
\[
f_n(h)=\frac{nh^6}{1+nh^2}.
\]
Every fixed n has zero h4 coefficient and \(f_n=O(h^6)\), but for each fixed real nonzero h the limit is h4. The complex poles \(\pm i/\sqrt n\) prevent a fixed analytic disk. The required additional bridge is supplied in §§12–15, not by the formal sum.

## 12. F05: five-real-coordinate gauge and spectrum

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** For nonzero mean \(w=\operatorname{mean}\Omega\), choose
\[
\Gamma(\Omega)=\overline w\,\Omega/|w|.
\]
Near e the positive square-root branch of |w| makes this real analytic. Its mean is positive real. Thus
\[
\Omega=(1+\mu)e+x_u u+x_v v+i(y_u u+y_v v),\quad1+\mu>0.
\]
There are five real coordinates: one common real radius and two components each of real and imaginary transverse parts. The common imaginary mean/common phase is removed. This gauge is an analytic coordinate construction, not a runtime normalization step.

At scalar value 1,
\[
D[\Omega+\epsilon\Omega(1-|\Omega|^2)](\delta\Omega)
=\delta\Omega-2\epsilon\Re(\delta\Omega).
\]
Indeed the modulus-squared derivative is \(2\Re\delta\Omega\). Adding L3 gives common real multiplier \(m=1-2\epsilon\), real transverse multiplier \(r=1-2\epsilon-3g\), and imaginary transverse multiplier \(a=1-3g\). Therefore
\[
D\mathcal F_0(0)=\operatorname{diag}(m,r,r,a,a).
\]
The ungauged imaginary common direction has multiplier one. Including it in this attracting quotient would be a dimension and hypothesis error.

Linearize the simultaneous phase stage around synchrony:
\[
p_j^+=p_j+3\lambda\sum_l(p_l-p_j)+O(\|p\|^3),
\quad p_\perp^+=(1-9\lambda)p_\perp.
\]
Sine contributes a factor 3 and L3's transverse eigenvalue contributes −3. Composing after amplitude/coupling gives
\[
D\mathcal F_\lambda(0)=\operatorname{diag}(m,r,r,b,b),
\qquad b=a(1-9\lambda).
\]
This retains the mixed \(27g\lambda\) term. The checker uses an explicit six-real-coordinate derivative, a 6×5 gauge embedding and a 5×6 extraction to derive this matrix.

At H5 the lambda=0 spectrum is \((9/10,3/10,3/10,2/5,2/5)\). The original map on C³ is not holomorphic: at scalar 1, the real increment is multiplied by \(1-2\epsilon\), while the imaginary increment is multiplied by 1. Except in a degenerate parameter case these fail complex linearity. Complexification below applies to the five real analytic coordinates, not to the original complex amplitudes.

## 13. F05: all-degree nonresonance and external theorem application

**ANALYTIC_PROOF.** At H5 every one of the five nonzero multipliers has 5-adic valuation −1. A monomial \(\prod_j\lambda_j^{\alpha_j}\), with nonnegative integer exponents and total degree d, has valuation −d. Equality to any target multiplier of valuation −1 forces d=1. Thus no nonlinear resonance exists in any degree. Repetitions in the spectrum merely aggregate exponents; zero exponents contribute zero. No finite-degree search is used as the proof.

**EXTERNAL_THEOREM_APPLICATION.** The checked literature source is [Marco Abate, Discrete holomorphic local dynamical systems](https://pagine.dm.unipi.it/abate/articoli/artric/files/DiscHolLocDynSys.pdf), Proposition 5.10 and Theorem 5.15, printed pp.35–36 (zero-based PDF pages 36–37). The first supplies formal linearization for the locally invertible nonresonant hyperbolic germ; the second promotes formal to analytic linearization in the attracting Poincare domain. These statements were reopened and checked for this supplement. The preserved [literature record](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_LITERATURE_REVIEW_v0.1.md) records the version. The parameter-uniform result is proved separately in §19, not attributed to Abate.

The model-specific application has these checks. Under H1 the quotient is a real-analytic germ at its synchronized fixed point. Complexify its five real coordinates. Under H4 its diagonal derivative is invertible, with \(0<m=1-a+r<1\) and \(0<r<a<1\); all eigenvalues attract and the assumed nonlinear nonresonance holds. H5 satisfies this by the valuation proof. The external theorem gives a local analytic linearizing chart H tangent to identity.

At each degree the homological denominators are \(\lambda^\alpha-\lambda_j\). Nonresonance makes them nonzero, so the tangent-to-identity formal conjugacy is unique. On gauge coordinates permutations act linearly on both transverse pairs, and channel conjugation acts by \((\mu,x,y)\mapsto(\mu,x,-y)\). These commute with the map and derivative; conjugating H by such a symmetry produces another tangent-to-identity conjugacy, which uniqueness equates with H. Similarly complex conjugating the complexified real coordinates gives another such conjugacy, so H preserves the real slice. Restricting back gives the required real-analytic, equivariant chart.

This separates the computed spectrum/arithmetic, the established external theorem, and its verified application. No general linearization theorem is claimed as new Tri-Octagon mathematics.

## 14. F04: local orbit, nonzero chirality and limiting direction

**ANALYTIC_PROOF under H1,H2,H4.** Let H be §13's linearizing chart and G=H inverse. Choose a smaller complex ball in H coordinates whose image under G lies within the common nonzero-mean/nonzero-pre-sync chart. The diagonal contraction maps this ball into itself. Compactness of the real seed circle permits one sufficiently small h bound for every phi. Consequently every gauge-fixed iterate remains in the chart.

In linearizing coordinates Z=(Mu,X,Y),
\[
Z_n=(m^n Mu_0,r^n X_0,a^nY_0).
\]
Conjugation-equivariance makes G's imaginary transverse component odd in Y. Its linear term is Y; each nonlinear term contains at least one Y factor and at least one further contracting factor. Because the initial seed has only imaginary transverse displacement, parity and tangency to identity give
\[
Mu_0=O(h^2),\quad X_0=O(h^2),\quad Y_0=hq+O(h^3).
\]
Terms containing only imaginary factors have at least three Y factors; terms linear in Y but nonlinear overall contain Mu or X. Dividing the imaginary component by a^n therefore gives
\[
a^{-n}y_n=hq+O(h^3)\quad\text{uniformly in }n,\phi,
\qquad a^{-n}y_n\longrightarrow Y_0.
\]
Uniformity follows by domination of the convergent inverse-chart power series on a smaller ball: after the one a^n factor is removed, every nonlinear monomial has only bounded contracting factors, with a factor of order h² in addition to its order-h imaginary factor. Their tails are uniformly summable.

For small real h>0 choose the bound so \(\|a^{-n}y_n-hq\|\le h/2\) for every n,phi. Then y_n never vanishes. In the positive-mean gauge, raw chirality is exactly
\[
C_n=(1+\mu_n)e\times y_n+x_n\times y_n.
\]
The two terms are orthogonal: the first lies in V and the second along e. The positive common factor makes \(C_{\perp,n}\ne0\), hence \(C_n\ne0\), at every update.

The real transverse inverse-chart component is even in Y. Permutation equivariance excludes a pure function of Mu with values in V, since V has no nonzero permutation-fixed vector. Every term therefore contains X or at least two Y factors. This gives
\[
x_n=O(r^n+a^{2n}),\qquad
\frac{\|C_{\parallel,n}\|}{\|C_{\perp,n}\|}
\le\frac{\|x_n\|}{\sqrt3|1+\mu_n|}
=O(r^n+a^{2n}).
\]
Also \(\mu_n\to0\), and
\[
\frac{C_n}{\|C_n\|}
\longrightarrow\frac{e\times Y_0}{\|e\times Y_0\|}\in V,\qquad
\|C_n\|\to0.
\]
Thus a normalized direction converges while chirality magnitude vanishes. No direction is assigned to the zero vector.

The direction of \(a^nY_0\) in linearizing coordinates is constant projectively. Its observed counterpart tends to a nearby direction depending on the initial seed. “Neutral” here describes only projective direction; all five state multipliers contract.

## 15. F04: fixed complex h-disk and coefficient-to-limit interchange

**ANALYTIC_PROOF.** The preceding real estimate is strengthened on a fixed complex disk. Complexify the real gauge coordinates, not the original amplitudes. The seed is the holomorphic curve \((0,0,hq(\phi))\) with complex h. Because phi lies on a compact real circle and H,G are holomorphic on common smaller balls, choose \(h_\ast>0\) so the closed disk \(|h|\le h_\ast\) for every phi stays in those domains for all diagonal iterates. No numerical radius is asserted; this is a uniform existence radius from the local analytic bounds.

Oddness removes the apparent factor h in \(a^{-n}y_n\). The inverse-chart monomial estimates used in §14 hold uniformly for complex h in this disk, and after division by a^n they converge uniformly to Y0. The real and common coordinates converge uniformly to zero. Define holomorphic normalized angular components by bilinear continuation:
\[
N_n(h,\phi)=\frac{C_n\cdot(-q)}{a^nh},\qquad
D_n(h,\phi)=\frac{C_n\cdot q_\perp}{a^nh}.
\]
Their h=0 singularities are removable. Uniformly in n and phi,
\(D_n=\sqrt3+O(h^2)\). Shrinking the disk ensures, for example,
\(|D_n-\sqrt3|<\sqrt3/2\) and \(|N_n/D_n|<1/2\).
The arctan power series then provides a common holomorphic branch
\(\psi_n=\arctan(N_n/D_n)\) agreeing with the real atan2 branch at positive h.

These angle functions converge uniformly on that complex disk and in phi. Weierstrass convergence supplies a holomorphic limit; Cauchy's formula on any smaller circle \(|h|=\rho<h_\ast\),
\[
[h^4]\psi_n=\frac{1}{2\pi i}\int_{|h|=\rho}\frac{\psi_n(h)}{h^5}\,dh,
\]
permits the n-limit through the integral. Thus the formal coefficient sum in §11 is now the coefficient of the observed local limiting angle. Conjugation parity gives even powers of h, and the lower coefficients vanish by §6; uniform bounds on a larger disk give a uniform \(O(h^6)\) remainder on a smaller one. Consequently
\[
\boxed{\psi_\infty(h,\phi)
=\kappa_\infty(a,r)h^4\sin6\phi+O(h^6)}
\]
uniformly in phi under H1,H2,H4. At H5 insert \(13375/1107936648\).

The same compact analytic control allows differentiation with respect to phi. The limiting seed-circle angle map has derivative
\(1+6\kappa_\infty h^4\cos6\phi+O(h^6)>0\) for sufficiently small h. It is a near-identity circle diffeomorphism, excluding collapse of this local circle onto six discrete axes. This is not a global basin, a universal finite-amplitude selector, or a classification of attractors elsewhere. A truncated coefficient matrix's spectral radius and eight finite runtime steps cannot replace this argument.

## 16. F06: phase expansion after amplitude and denominator differentiation

**EXACT_SYMBOLIC.** For an already amplitude-updated jet, write R=1+h²x+h4u and I=hy+h³v+h5w. Expanding \(p=\arctan(I/R)\) gives
\[
\begin{aligned}
p_1&=y,\\
p_3&=v-xy-y^{\circ3}/3,\\
p_5&=w-xv+(x^{\circ2}-u)y-y^{\circ2}v+xy^{\circ3}+y^{\circ5}/5.
\end{aligned}
\]
Products are componentwise. This follows by \(R^{-1}=1-h^2x+h^4(x^2-u)+\cdots\) and arctan z=z−z³/3+z5/5+… .
Let \(H_j=\sum_l\sin3(p_l-p_j)=hH_1+h^3H_3+h^5H_5+\cdots\). Taylor expansion yields
\[
\begin{aligned}
H_1&=3L_3p_1,\\
(H_3)_j&=3(L_3p_3)_j-\tfrac92\sum_l(p_{1l}-p_{1j})^3,\\
(H_5)_j&=3(L_3p_5)_j-\tfrac{27}2\sum_l(p_{1l}-p_{1j})^2(p_{3l}-p_{3j})
 +\tfrac{81}{40}\sum_l(p_{1l}-p_{1j})^5.
\end{aligned}
\]
The coefficients are the sine-series coefficients, including the mixed cubic factor.

At first order in lambda, \(z e^{i\lambda H}=z+i\lambda Hz+O(\lambda^2)\), so
\[
\delta y=H_1,\quad\delta x=-yH_1,\quad
\delta v=H_3+xH_1,\quad
\delta u=-yH_3-vH_1,\quad
\delta w=H_5+xH_3+uH_1.
\]
The independent checker uses two formal channel roots for j and l, reduces them by the same cubic relation, and takes the channel trace to evaluate these difference sums. Extracting the scalar changes gives
\[
\delta A=-9A,\quad\delta X=9A^2/\sqrt6,\quad
\delta D=-3AX,\quad\delta E=9AD,
\]
\[
\delta F=-3A^2X,\qquad
\delta K=-9K-3XA^3/\sqrt6+47A^5/16.
\]
These include the changed real quadratic coordinate X and tangent factor A.
Since \(\kappa=K/(2A)\), differentiating the denominator is essential:
\[
\delta\kappa=\frac{\delta K}{2A}-\frac{K\,\delta A}{2A^2}
=-\frac{3XA^2}{2\sqrt6}+\frac{47A^4}{32}.
\]
The −9K terms cancel; omitting the denominator term would leave a false contribution.

For one full step from the seed, the phase input has A=a and \(X=-\epsilon/\sqrt6\). Therefore
\[
\operatorname{coefficient}_1(\lambda)=
-\frac{\epsilon^2}{36a}
+\lambda\left(\frac{\epsilon a^2}{4}+\frac{47a^4}{32}\right)+O(\lambda^2).
\]
At H5,
\[
\frac{\epsilon a^2}{4}=\frac1{500}=\frac5{2500},\qquad
\frac{47a^4}{32}=\frac{94}{2500},
\]
so the coefficient is \(-1/5760+(99/2500)\lambda+O(\lambda^2)\).
Multiplying by \(h^4\sin6\phi\) and adding the local \(O(h^6)\) remainder gives the signed-angle law.

The isolated phase-vector calculation starts instead with p=hq and measures the phase-vector angle, not raw chirality of the post-amplitude complex state. Its fifth difference-power has Ss2 coefficient 3/2. Projection onto q_perp contributes half a sin6phi, so its coefficient is
\((81/40)(3/2)(1/2)=243/160\).
It is correct for that different input/observable and is a **NEGATIVE_FALSIFIER** for substitution into the full-composition law. Even at epsilon=g=0 the full one-step chirality coefficient is 47/32, not 243/160; that parameter case is not an attracting limit regime.

## 17. F06: four-monomial lift and differentiated resolvent

**EXACT_SYMBOLIC / ANALYTIC_PROOF for convergent coefficient sums.** Define
\[
z=(A^4,A^2X,X^2,F)^T,\quad z_0=(1,0,0,0)^T.
\]
These are formal coefficient monomials. A,X,F were defined in §§7–9; letters are not interpreted from their names.

Expand A′=aA, \(X'=rX-\epsilon A^2/\sqrt6\), and F′ from §9. Row by row:
A′4 yields a4A4; A′²X′ yields \(a^2rA^2X-\epsilon a^2A^4/\sqrt6\);
X′² yields \(r^2X^2-2r\epsilon A^2X/\sqrt6+\epsilon^2A^4/6\);
F′ supplies the last row. Thus
\[
T_0=\begin{pmatrix}
a^4&0&0&0\\
-\epsilon a^2/\sqrt6&a^2r&0&0\\
\epsilon^2/6&-2r\epsilon/\sqrt6&r^2&0\\
-\epsilon a/(3\sqrt6)&-\epsilon(1+2a)/3&-\epsilon\sqrt6&r
\end{pmatrix},
\]
\[
\ell=\left(-\frac{\epsilon^2}{36a},
\frac{\epsilon(r-2\epsilon)}{6a\sqrt6},
\frac{\epsilon(2r-1)}{6a},-\frac{\epsilon}{a\sqrt6}\right).
\]
The amplitude step advances z by T0z and adds ell z to kappa.

Now differentiate the four monomials using §16:
\[
\delta A^4=-36A^4,\quad
\delta(A^2X)=9A^4/\sqrt6-18A^2X,\quad
\delta X^2=18A^2X/\sqrt6,\quad
\delta F=-3A^2X.
\]
These give
\[
P_s=\begin{pmatrix}-36&0&0&0\\9/\sqrt6&-18&0&0\\0&18/\sqrt6&0&0\\0&-3&0&0\end{pmatrix},
\qquad
\ell_s=(47/32,-3/(2\sqrt6),0,0).
\]
The phase correction acts on post-amplitude coefficients, so its order is
\[
T_\lambda=(I+\lambda P_s)T_0+O(\lambda^2),\qquad
\ell_\lambda=\ell+\lambda\ell_sT_0+O(\lambda^2).
\]
The checker extracts every row coefficient from the derived scalar expressions rather than loading these matrices from a saved oracle.

At \(|a|<1,|r|<1,a\ne0\), T0 has diagonal eigenvalues \(a^4,a^2r,r^2,r\), all strictly inside the unit disk. Thus \(R_0=(I-T_0)^{-1}\) exists and \(\sum T_0^n=R_0\). Jordan/collision polynomial factors still decay. The differentiated series, with one insertion of PsT0 in each product, is absolutely summable by a geometric bound with at most an extra factor n.

Differentiate \((I-T_\lambda)R_\lambda=I\) at zero:
\[
-P_sT_0R_0+(I-T_0)R'_0=0,\quad
R'_0=R_0P_sT_0R_0.
\]
Then
\[
\boxed{\kappa_\infty(\lambda)=\ell R_0z_0+
\lambda(\ell_sT_0R_0+\ell R_0P_sT_0R_0)z_0+O(\lambda^2)}.
\]
This is first a coefficient-resolvent calculation; the nonlinear parameter-uniform bridge is §19.

With epsilon=(a−r)/2 the displayed matrices give a parameter-dependent rational formula before any specialization. The independent script uses exact lower-triangular elimination and also matches the scalar sum of §11. Exact H5 evaluation gives
\[
\boxed{\kappa_\infty(\lambda)=
\frac{13375}{1107936648}
+\frac{34494041501}{849664304944}\lambda+O(\lambda^2)}.
\]
The expanded parameter rational expression for the derivative is retained in the JSON; the compact matrix formula above defines the same exact expression more readably. These fractions are **EXACT_SYMBOLIC** derivations, and their later comparison with the paper is **ORACLE_VERSUS_PAPER_ONLY**. Neither is a long-runtime binary64 certification.

## 18. F05/F06: exact all-degree resonance interval and historical lambda

**ANALYTIC_PROOF / EXACT_SYMBOLIC.** At H5 set m=9/10, r=3/10, a=2/5 and \(b=a(1-9\lambda)\). Aggregate repeated eigenvalue exponents: every resonance has form
\[
t=m^i r^j b^k,\quad t\in\{m,r,b\},\quad i,j,k\ge0,\quad i+j+k\ge2.
\]
This aggregation covers all five-coordinate multiindices.
Let \(L=m^9=387420489/10^9\), \(U=r/m^3=100/243\). For \(L<b<U\), exact inequalities are
\[
0<r<L<b<U<m<1,\quad U^2<r,\quad r/m^2<L,\quad U<m^8.
\]
They exhaust the infinite problem as follows:

1. If j≥1, the nonlinear product is strictly below r, hence below all three targets.
2. If j=0, target m is impossible: a b factor makes the product smaller than m, and a pure nonlinear power of m is smaller than m.
3. For target b, any b factor gives equality only at excluded degree one. Without b the condition is \(b=m^i\), i≥2. The adjacent powers \(m^9=L\) and \(m^8>U\) exclude every interior equality.
4. For target r, k≥2 gives product below r by U²<r. For k=0, \(m^i=r\) is excluded by 5-adic valuation for i≥2 and direct inequality for i=0,1. For k=1 the remaining family is \(b=r/m^i\), i≥1. It increases with i; its adjacent values \(r/m^2<L\) and \(r/m^3=U\) exclude all interior equalities.

Both boundary resonances actually occur. Solving b=a(1−9lambda) gives
\[
\lambda_-=(1-U/a)/9=-7/2187,\quad r=m^3b \ \text{(degree 4)},
\]
\[
\lambda_+=(1-L/a)/9=12579511/3600000000,\quad b=m^9 \ \text{(degree 9)}.
\]
Since b decreases strictly with lambda, these are the nearest negative and positive real resonances. J is the open resonance-free component containing zero. The symmetric sufficient interval \(|\lambda|<7/2187\) is chosen within it; its radius follows from the negative boundary, not from defining “symmetric sufficient” to mean maximal. These are nonresonance boundaries, not proved dynamical bifurcations or proofs of failure of linearization at the endpoints.

For the recorded lambda=1/1000, \(b=991/2500\), inside J. Independently,
\(v_5(m)=v_5(r)=-1\), \(v_5(b)=-4\).
A target m or r would require i+j+4k=1, impossible at nonlinear degree. A target b requires i+j+4k=4; aside from excluded k=1,i=j=0, only k=0,i+j=4 remains. Multiplying these five candidates by 10⁴ gives
\(81,243,729,2187,6561\), whereas \(10^4b=3964\). None matches. This valuation reduction proves all-degree nonresonance; enumeration of the five exhaustive residual cases is not a degree-capped search.

Why this historical lambda, epsilon, g or seed was selected remains OPEN. No new trajectory at lambda=1/1000 was run.

## 19. F06: uniform analytic chart and parameter interchange

**ANALYTIC_PROOF under H6.** Fix a compact real subinterval K strictly inside the nonresonant interval, containing zero for a Taylor statement about zero. The complexified five-coordinate map is jointly holomorphic in z and lambda near K: local square roots and phase logarithms have common branches near the synchronized nonzero state. Write
\[
F_\lambda(z)=\Lambda_\lambda z+O(\|z\|^2),\qquad
\Lambda_\lambda=\operatorname{diag}(m,r,r,b,b).
\]
After shrinking a complex neighborhood of K, bound all eigenvalue moduli between eta>0 and rho<1. Choose rho<q<1 and an integer N with \(q^{N+1}<\eta\). A degree-d≥N+1 homological denominator obeys
\[
|\lambda^\alpha-\lambda_j|\ge\eta-\rho^d
\ge\eta-q^{N+1}>0.
\]
Here subscripted lambdas denote multipliers, not the phase parameter.
For degrees 2 through N there are finitely many denominators. Nonresonance on compact K gives a positive minimum; continuity preserves a lower bound on a smaller complex parameter neighborhood. Repeated multipliers are included, not excluded from this argument.

Solve homological equations only through degree N. Their coefficients are holomorphic in the parameter and uniformly bounded. The resulting tangent-to-identity polynomial change \(P_\lambda\) has a common local inverse after shrinking the ball. The transformed map has
\[
G_\lambda=P_\lambda F_\lambda P_\lambda^{-1}
=\Lambda_\lambda z+R_\lambda(z),\quad
\|R_\lambda(z)\|\le M_\ast\|z\|^{N+1}.
\]
Choose a common ball where \(\|G_\lambda(z)\|\le q\|z\|\).
Define \(H_{\lambda,n}=\Lambda_\lambda^{-n}G_\lambda^n\). The telescoping difference is bounded by
\[
\|H_{\lambda,n+1}-H_{\lambda,n}\|
\le\frac{M_\ast}{\eta}
\left(\frac{q^{N+1}}{\eta}\right)^n\|z\|^{N+1}.
\]
This is a uniformly convergent geometric majorant in z and complex lambda. Its limit is jointly holomorphic, tangent to identity, and satisfies \(H_\lambda G_\lambda=\Lambda_\lambda H_\lambda\). A common inverse follows from the inverse function theorem after another uniform shrink. Thus \(H_\lambda P_\lambda\) is the required jointly analytic chart, without invoking an unspecified parametric version of the external theorem.

At H5, every compact K⊂J permits eta=1/4, q=19/20 and N=27 after complex-neighborhood shrinking: the real eigenvalues lie between 3/10 and 9/10, and \(4(19/20)^{28}<1\). These are proof bounds, not changed model parameters.

Uniqueness again enforces real-slice and symmetry preservation. In the imaginary inverse-chart component every nonlinear term contains a Y factor; after dividing iterates by \(b(\lambda)^n\), all remaining nonlinear factors contract uniformly. On the seed family, parity removes h as well. The argument in §§14–15 now uses the common complex h-disk and a common smaller complex parameter neighborhood, with angular denominator bounded away from zero after division by \(b(\lambda)^nh\).

Uniform holomorphic convergence allows Weierstrass and Cauchy integrals first in h and then in lambda. For example the coefficient derivative is represented by the double integral of \(\psi_n(h,\lambda)/(h^5\lambda^2)\) on smaller contours around zero. Uniform convergence permits the n-limit through both integrals. This justifies interchanging local iteration limit, h4 extraction and first lambda derivative. It is not inferred from the spectral radius of T0.

Consequently the actual local observed law is
\[
\psi_\infty(h,\phi;\lambda)=h^4\sin6\phi
[\kappa_\infty(0)+\lambda\kappa_\infty'(0)+O(\lambda^2)]+O(h^6),
\]
with locally uniform remainders in phi and on the specified compact subintervals, with the coefficients of §§11,17. No uniformity is asserted up to resonance endpoints, and no second or higher lambda coefficient has been computed. The limiting circle map remains a local diffeomorphism; state amplitudes contract and no global axis-attraction statement follows.

## 20. Evidence separation and K2C comparison

| Evidence class | Conclusion or role | Boundary |
|---|---|---|
| EXACT_SYMBOLIC | Basis/actions, one-step projections, complete jets, phase variations, scalar sums, resolvent fractions, endpoint equalities | Exact algebra of the ideal recurrence; not a floating-point trajectory |
| ANALYTIC_PROOF | All-n jet induction, collision removability, absolute summability, valuation and interval nonresonance, local direction and interchanges | Written proofs with their hypotheses; not certified by finite predicate totals |
| EXTERNAL_THEOREM_APPLICATION | Nonresonant attracting analytic linearization, applied in five complexified real coordinates | Established theorem, not a new model theorem or holomorphy of the original C³ map |
| FINITE_ENUMERATION | Twelve-root orbit enumeration, selected collision regressions, eight exact coefficient iterations | Finite corroboration; the all-degree/all-n proofs are separate |
| HIGH_PRECISION_REFERENCE | K2C's 80/100-digit finite full-map and finite-h derivative references; earlier attributed CR calculations | Current focused tests reproduce only K2C's bounded cases, not CR's longer calculations |
| BINARY64_RUNTIME_WITNESS | Current focused P7/P8 runtime comparisons and finite differences | Bounds concern finite state/C/angle outputs and one-step sensitivity |
| ORACLE_VERSUS_PAPER_ONLY | Post-derivation comparison of the two limiting rational constants with recorded Paper F results | No runtime infinity certification |
| HISTORICAL_FIXTURE | AX's 18 saved rows from two seeds | Retained context, not reread as new trajectories or reopened as F07 |
| NEGATIVE_FALSIFIER | Wrong orbit counts, incorrect observable substitution, invalid limit inferences | Each wrong claim is rejected with an explicit counterexample or missing-hypothesis argument |

K2C P7 distinguishes exact projections and finite-n coefficients from finite full-map high-precision values. Its two amplitudes .02/.01, two orientations ±pi/12 and eight updates have explicit O(h6) remainders; a truncated jet is not the finite-amplitude map. Sign claims are made only when the stated binary64 angle bound resolves them. The infinite coefficient comparison is explicitly ORACLE_VERSUS_PAPER_ONLY.

K2C P8 differentiates the full post-amplitude complex state, then C and atan2. Its finite-h target differs from the leading \((99/2500)h^4\sin6\phi\). Centered differences use separately declared truncation and roundoff allowances. The wrong \(243/160\) law is tested against its distinct observable/input and rejected as a full-map substitute. The limiting derivative remains ORACLE_VERSUS_PAPER_ONLY.

The new checker never imports paper_f_oracle.py or the preserved PF verifier. Its own exact mathematics is completed before opening PF-record for two numeric-rational comparisons. The separately authorized focused test naturally uses its existing oracle; that execution is labelled parity evidence and is not the derivation engine.

The focused run used conda torment and only kernel_physics/tests/test_parity_p07_p08.py. Result: **8 passed**, exit 0, stderr empty; no broad suite and no historical integrated runner executed. Therefore this run is **PASS**. The pre-existing Atlas 07/08 Windows access-violation stderr caveat remains **UNRESOLVED_NOT_INVESTIGATED**; this clean run does not clear it.

## 21. Required falsifiers A–L

| Wrong claim | Explicit falsification or scope failure | Evidence |
|---|---|---|
| A. There are only two oriented D3 root orbits | Generator action gives sizes 6,3,3 (§3) | FINITE_ENUMERATION plus orbit-stabilizer proof |
| B. The oriented v-type D3 orbit has size six | T fixes v, stabilizer order 2, orbit size 6/2=3 | EXACT_SYMBOLIC / ANALYTIC_PROOF |
| C. Symmetry fixes the numerical B_C coefficient | Same symmetric recurrence family at epsilon=0 has zero coefficient; at epsilon≠0 its epsilon² factor is nonzero | NEGATIVE_FALSIFIER |
| D. Fixed-n Taylor remainder is automatically uniform in n | \(nh^6/(1+nh^2)\) has a growing fixed-n h6 coefficient and no common complex disk | NEGATIVE_FALSIFIER |
| E. A convergent coefficient series alone proves the observed angular limit | The same family has h4 coefficient zero at every n but real pointwise limit h4; formal coefficient convergence does not commute with the limit | NEGATIVE_FALSIFIER |
| F. Common phase multiplier 1 belongs to the attracting five-dimensional quotient | It is the sixth ungauged direction and gives resonances \(\lambda_j=\lambda_j1^k\); §12 removes it | EXACT_SYMBOLIC / ANALYTIC_PROOF |
| G. The original C³ recurrence is holomorphic | D at scalar 1 scales real and imaginary increments differently when epsilon≠0 | NEGATIVE_FALSIFIER |
| H. 243/160 is the full-composition one-step coefficient | Exact phase-only and raw-chirality derivations give different coefficients; H5 gives 99/2500 | EXACT_SYMBOLIC / NEGATIVE_FALSIFIER |
| I. Eight runtime steps prove kappa infinity | The exact eighth coefficient differs from the exact infinite sum (difference stored); finite values also cannot establish the analytic interchange | NEGATIVE_FALSIFIER |
| J. Degree-capped search proves all-degree nonresonance | Spectrum (1/2,1/8192) has no nonlinear resonance through degree 12 but has \(1/8192=(1/2)^{13}\) | EXACT_SYMBOLIC finite example plus all-degree reasoning |
| K. Higher lambda orders are established | Adding arbitrary c lambda² changes second order while preserving the verified value and first derivative; no second coefficient was derived | Logical NEGATIVE_FALSIFIER, not an assertion that the true second coefficient is arbitrary |
| L. Local projective direction convergence proves global axis attraction | The local limiting circle map is a diffeomorphism, and the two exact nonzero isotropy chirality types remain orthogonal; no global basin hypothesis exists | ANALYTIC_PROOF / NEGATIVE_FALSIFIER |

The all-degree nonresonance proofs, external-theorem application, common analytic chart, coefficient/limit interchange and parameter-uniform interchange are closed by §§13–19's written arguments. Predicates check algebraic ingredients and counterexamples; their count is not a count or certificate of these analytic theorems.

## 22. Claim-to-owner closure

| Owner | Prior omission | Exact section/proof/check evidence | Status |
|---|---|---|---|
| F02 | Seed D3/D6 actions; oriented/projective classes; stabilizers; invariant full-state subspaces | §§3–4; exact P/T matrices and relations; conjugation extension; orbit-stabilizer proof and enumeration; solved fixed-space equations, full-map equivariance and chirality formulas. Checks F02_GROUP_ACTION / F02_ISOTROPY | FULL |
| F03 | One-step projections; harmonic selection and degree exclusion; complete finite jets; arbitrary finite-n laws; remainder qualifications | §§5–10; direct cross product, alternating-polynomial proof, full vector and all eleven scalar recurrences, convolution induction, finite H formula. Checks F03_ONE_STEP / F03_HARMONIC_SELECTION / F03_FINITE_JETS / F03_RATE_COLLISIONS. Fixed-n qualification remains explicit | FULL |
| F04 | Parameter rational sum and H5 fraction; collision limits; formal versus observed limit; analytic bridge | §§10–11 scalar summation and removability; §§14–15 invariant local chart, nonzero C, fixed complex h-disk and Cauchy extraction. Checks F04_INFINITE_SUM plus bridge counterexample/ingredients; actual bridge is the written proof | FULL |
| F05 | Five-coordinate gauge; spectrum; common-phase removal; nonresonance; scoped normal form | §§12–13 real Jacobian, explicit quotient, all-degree valuation proof, checked external theorem and equivariant real-slice application; §18 all-degree interval proof. Checks F05_GAUGE_SPECTRUM / F05_NONRESONANCE / F05_LINEARIZATION_HYPOTHESES | FULL |
| F06 | Full composition; angle denominator; 99/2500 versus 243/160; differentiated resolvent and exact limiting derivative; parameter-uniform interchange | §§16–19 phase expansion and coefficient extraction, matrix rows derived from monomials, inverse differentiation, rational evaluation, all-degree resonance bounds, finite elimination and uniform majorant with double Cauchy extraction. Checks F06_ONE_STEP_LAMBDA / F06_RESOLVENT_DERIVATIVE / F06_RESONANCE_INTERVAL / F06_UNIFORM_ANALYTICITY | FULL |

These are new supplement coverage determinations only. A07–A09, F07 and all other ledger rows are not reassessed. The overall 75-row completeness decision is not rerun. Earlier review/crosswalk/Atlas/Supplement A records remain immutable.

## 23. Reproducible checker and external-safe packaging

Deliverables:

- [Source packet](C:/Users/Notandi/.codex/reports/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_SOURCE_PACKET_v0.1.md)
- [Independent checker](C:/Users/Notandi/.codex/reports/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_CHECKS.py)
- [Results](C:/Users/Notandi/.codex/reports/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_RESULTS.json)

Example rerun with new, unused external destinations:

~~~powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_CHECKS.py --repo C:\TORMENT\TRIOCTAGON_new\trioctagon-physics --output C:\Users\Notandi\.codex\reports\supplement_f_new_run.json --scratch C:\Users\Notandi\AppData\Local\Temp\supplement_f_new_run
~~~

The checker requires bytecode writing disabled, requires output and scratch, rejects protected-tree destinations and existing outputs, and redirects temporary/cache locations externally. No destination depends on its own script location. Its read-only relocated copy runs with output and scratch elsewhere; original/relocated hashes and unchanged relocation-directory inventory are checked.

Separate --test-receipt, --packaging-receipt and --integrity-receipt inputs supply the full task closeout. Without them a mathematics-only run reports pending closeout receipts. New integrity generation also takes --fingerprint-before, --external-before and --git-before, and fingerprints after the mathematical work. Receipt and after-manifest outputs use exclusive creation and must be external. All receipt contents and hashes are embedded in the result.

The packet carries the analytic arguments; the JSON explicitly records that analytic proofs are not certified by predicate count. The final exact check total is determined by emitted records, not a preselected target. The preserved PF verifier's 131 predicates remain prior evidence and are never merged into that total.

Task scratch and raw receipts:
C:\Users\Notandi\AppData\Local\Temp\trioctagon_supplement_f_20260929_4e729c.

## 24. Integrity and final execution record

Full before/after inventories include regular-file relative paths and SHA256 content, excluding only .git internal paths. Git HEAD and tracked status are independently captured using optional locks disabled. Current repository coverage includes Papers A–F and the published prior Atlas. The production kernel is fingerprinted separately and also lies within the fingerprinted full production checkout.

External inventories cover all 27 prior Atlas artifacts, the four-file completeness-review set and all three Supplement-A files. The copied fingerprint helper is only standard-library receipt infrastructure; no Supplement-A mathematical code is used as the Supplement-F derivation engine. Supplement A itself is unchanged.

Final execution completed in conda environment torment, Python 3.11.15, SymPy 1.14.0.

**CHECK_COUNT = 89; all passed.** This comprises 82 independent records, three subsequent source-parity records, the expected-HEAD record and three receipt records. The packaging receipt contains 9 successful contract/relocation checks, which are not added again to CHECK_COUNT. Written analytic proofs remain separate.

**FOCUSED_TEST_STATUS = PASS:** P7/P8, 8 passed, exit code 0, empty stderr. Those eight tests are reported separately from the independent checker count.

**RUNTIME_CAVEAT_STATUS = UNRESOLVED_NOT_INVESTIGATED:** the earlier Atlas 07/08 Windows stderr caveat remains open. This clean focused run does not clear it.

| Fingerprinted tree | Regular files before/after | Matching SHA256 |
|---|---:|---|
| current | 7803 / 7803 | eb913f8b685be59b18ed9cbf1656b06e3d7dcb617b6579e3ec60fc27753dc1df |
| old | 401 / 401 | cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd |
| torment_kernel | 64 / 64 | 8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41 |
| torment_checkout | 173908 / 173908 | 3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4 |

| External protected set | Files | Matching SHA256 of path/content map |
|---|---:|---|
| prior_atlas | 27 | 5e235603155426511b451301a5beb2747b8aa521a7a477573d7e7744d77cd760 |
| completeness_review | 4 | 1085f63e5e6114e6fd907eb8207e5d65551a82ef022fc0b9c049f3529b538951 |
| supplement_a | 3 | b033ccbb7442fd32fe8c57066c7d66a93a8c554d795448a2cdd824906443948a |

All regular-file path/content maps match, with no added, removed or modified files. Git HEAD and tracked status also match their before records. The JSON embeds separate test, packaging and integrity receipts, their hashes, source hashes and the locations and hashes of both full manifests.

~~~text
F02 = FULL
F03 = FULL
F04 = FULL
F05 = FULL
F06 = FULL
INTEGRITY = PASS
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
PAPERS_A_F_CHANGED = NO
PRIOR_ATLAS_CHANGED = NO
COMPLETENESS_REVIEW_CHANGED = NO
SUPPLEMENT_A_CHANGED = NO
COMMITS = 0
PUSHES = 0
PUBLICATION = NO
~~~

Task stopped after this F02–F06 report. No other ledger row or overall completeness decision was reassessed.
