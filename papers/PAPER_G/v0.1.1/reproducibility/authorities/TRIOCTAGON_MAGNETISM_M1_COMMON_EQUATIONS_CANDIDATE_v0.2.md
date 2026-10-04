# M1 common equation candidate v0.2 — identical text for reciprocal acceptance

Date: 2026-10-01. Prepared by GPT from Codex's CE01–CE11 v0.1 and both supplied cross-reviews. The original Codex candidate is preserved unchanged inside its delivery ZIP.

Status: **PROPOSED_FOR_IDENTICAL_PEER_ACCEPTANCE. Neither reviewer has yet accepted this v0.2.**

Changes from Codex v0.1: CE05 gains an explicitly normalized, resonance-qualified triad zero-stratum characterization; CE10 makes the exact-lift/off-sector distinction explicit; CE11 clarifies that K4 may be nonzero both inside and outside A=0. Exact core, finite numerical observations, and optional new definitions remain separate. No kernel, paper, UI or repository changes are authorized.

This is one versioned candidate text, not a claim of consensus. The delivery manifest identifies its exact SHA-256. Peer acceptance must identify this version/hash and the accepted equation IDs. Any mathematical revision creates a new version rather than silently changing what was accepted. Physical magnetism and implementation are not admitted.

## CE01 — state, convention and carrier

Let Omega=x+iy, with real x,y. For a triad,

\[
S=xx^T+yy^T,\quad A=xy^T-yx^T,\quad C=x\times y=(A_{BC},A_{CA},A_{AB})^T,
\quad A=-[C]_\times,\quad\rho=\Omega\Omega^\dagger=S-iA.
\]

For nonzero Omega, rho has complex rank one. S has real rank at most two; A has rank zero or two. With I=tr S,

\[
SC=0,\quad |C|^2=e_2(S),\quad I^2=|\Omega\cdot\Omega|^2+4|C|^2,\quad |C|\le I/2.
\]

Equality in the bound means x perpendicular to y with equal norms (including the zero equality case). This bounds C by current intensity, not by a universal constant. A=0 iff x,y are real-linearly dependent, equivalently Omega=c r for c complex and r real.

Under Paper-B spatial G with face permutation Q,
\(A'=\det(G)QAQ^T\), \(C'=\det(G)\det(Q)QC\).
For pure channel relabelling, omit det(G). The three specified spatial generators act on C as P, -I, S_v, with P the A→B→C cyclic permutation and S_v swapping A,C.

These are kinematic covariance statements. Dynamical relabelling must carry k with the channel permutation; fixed unequal k does not retain full label-permutation symmetry. Common-phase dynamical covariance has the nonzero-pre-sync qualification below when lambda is nonzero. No action here is identified with physical time reversal.

## CE02 — the linear axial attachment and its limits

Let e=(1,1,1)^T, P_perp=I-ee^T/3 and use Paper-B **column** frames

\[
T=\begin{pmatrix}-1/2&1&-1/2\\-\sqrt3/2&0&\sqrt3/2\\0&0&0\end{pmatrix},\quad
N=\begin{pmatrix}-\sqrt3/2&0&\sqrt3/2\\1/2&-1&1/2\\0&0&0\end{pmatrix}.
\]

\[
W=TC,\quad\Gamma=e^TC,\quad s=Ae=e\times C,\quad Ns=\sqrt3 W,
\quad T^TT=\tfrac32P_\perp,\quad\ker T=\mathbb R e,
\quad C=\tfrac23T^TW+\tfrac\Gamma3e.
\]

W transforms as det(G)GW. The vector space of real-linear maps **of C** into ambient axial vectors for the stated D3h action is one-dimensional, spanned by T. NC fails axial V parity. Gamma has signs (+,-,+) under (C3,H,V), so Gamma e_z is polar-z-like, not axial-z. No assertion here excludes nonlinear functions of the full state. No units or spatial field interpolation are supplied.

## CE03 — graph decomposition, flatness and winding

Treating A_ij as an edge one-cochain on the channel triangle, define psi=Ae/3, (d psi)_ij=psi_j-psi_i, and ell_AB=ell_BC=ell_CA=1 with antisymmetric reversals. Then

\[
A=-d\psi+\tfrac\Gamma3\ell,
\qquad\Gamma=\Im\{\overline{(\Omega_B-\Omega_A)}(\Omega_C-\Omega_A)\}.
\]

This is not automatically a material seam cochain or a filled Paper-C cap. The shell is an open annulus. An explicitly added dual two-cell can carry the coboundary Gamma; its existence/interpretation must be declared.

Matched tangent maps satisfy
\(T_{ij}=t_it_j^T+e_ze_z^T\), \(T_{ij}T_{jk}=T_{ik}\), and \(T_{AC}T_{CB}T_{BA}=\Pi_A\): identity on the tangent plane.

For nonzero state phases z_i=Omega_i/|Omega_i|, vertex links v_ij=z_i conjugate(z_j), with source j→destination i, have unit cyclic product. Transported phase ratios q_ij=conjugate(z_i)u^0_ij z_j also have unit product for the flat matched connection. Their principal arguments can sum to 2pi times a nonzero integer; (1,zeta,zeta²) with zeta=exp(2pi i/3) gives +2pi in AB,BC,CA order. Branch cuts/zeros obstruct unconditional winding conservation. Passive frame changes require u'^0_ij=exp(i(theta_j-theta_i))u^0_ij. No cohomological prohibition of all curvature assignments is asserted.

## CE04 — exact pre-sync algebra

For M=3q channels let L be the negative cycle Laplacian, k repeat by residue class, D=diag(k-|Omega|²), and M_state=I+epsilon D+gL.

\[
\widetilde\Omega=M_{state}\Omega,\quad
\widetilde S=M_{state}SM_{state}^T,\quad
\widetilde A=M_{state}AM_{state}^T.
\]

For three channels, \(\widetilde C=\operatorname{cof}(M_{state})C\), including singular matrices. The cofactor matrix equals the adjugate here because M_state is symmetric; for a general matrix they are transposes.

\[
\widetilde A-A=\epsilon(DA+AD)+g(LA+AL)
+\epsilon^2DAD+\epsilon g(DAL+LAD)+g^2LAL.
\]

These are exact state-dependent identities, not linearity of the nonlinear update or a second engine.

## CE05 — exact synchronization and the no-seed domain

Use the existing convention phi_i=Arg0(tildeOmega_i), Arg0(0)=0,
\(\delta_i=\lambda\sum_{j\sim i}\sin3(\phi_j-\phi_i)\), and d_ij=delta_j-delta_i. Then

\[
A^+_{ij}=\widetilde A_{ij}\cos d_{ij}+\widetilde S_{ij}\sin d_{ij},\quad
S^+_{ij}=\widetilde S_{ij}\cos d_{ij}-\widetilde A_{ij}\sin d_{ij}.
\]

These formulas include zero entries when deltas follow Arg0. At lambda=0 the phase step is the identity. If A=0 and every pre-sync component is nonzero, all relative phases are 0 or pi and A+=0, including mixed signs. If lambda=0, A=0 is preserved even with zeros. All-zero Omega stays zero for all admitted parameters.

Universal invariance is false: Omega=exp(i pi/6)(1,-1,0), epsilon=g=0, lambda=pi/12 yields A+_AB=-1/2, C+=(0,0,-1/2), W+=(1/4,-sqrt(3)/4,0). At epsilon=1/20,g=1/5,k=e,lambda=1/1000 the same input gives A+_AB=-(4/25)sin(1/500). This is convention-sensitive boundary behavior, not a physical battery. No convention is changed.

### Complete triad zero-stratum area criterion (additional explicit scope)

For an A=0 input, the pre-sync image is still real up to common phase. Write it as
\(\widetilde\Omega=e^{i\alpha}r\), with \(r\in\mathbb R^3\); the common factor has **unit modulus**, and all amplitude scale is included in r. The all-zero image has A+=0. If all three pre-sync entries are nonzero, or at most one is nonzero, no area is generated. With exactly one zero entry i, let (i,j,k) be cyclic and let \(\sigma_j=\operatorname{sign}r_j\), \(\sigma_k=\operatorname{sign}r_k\). The only possibly nonzero cyclic area is

\[
 A^+_{jk}=r_jr_k\sin\!\left[\lambda(\sigma_j-\sigma_k)\sin(3\alpha)\right],
 \qquad C^+=A^+_{jk}e_i,\quad W^+=A^+_{jk}t_i.
\]

Here e_i is the channel-coordinate unit vector, not e=(1,1,1). This formula is unchanged by simultaneously replacing alpha by alpha+pi and r by -r.

For the sign choice r_j>0>r_k it becomes
\[
 A^+_{jk}=-|r_jr_k|\sin\!\left(2\lambda\sin3\alpha\right).
\]
With an arbitrary factorization \(\widetilde\Omega=c u\), u real and c nonzero, the right-hand side instead carries \(|c|^2\), with alpha=arg c and the signed real u entries. Do not silently omit that factor.

Thus nonzero generated area requires and, on this exactly-one-zero/opposite-sign stratum, is equivalent to \(\sin(2\lambda\sin3\alpha)\ne0\). Nonzero lambda and nonzero sin(3alpha) alone are not sufficient: lambda=pi/2, alpha=pi/6 gives a resonant zero. The witnesses already in CE05 have nonzero sine and remain valid.

At a nonzero-area-generating boundary point, nearby real-line pre-sync states with every component nonzero have A+=0; the synchronization map therefore has a discontinuity visible in this observable. This is not a smooth battery source. The criterion is for the triad; ring generalization must use its actual neighbor set. No assertion that the full map is continuous whenever A+ happens to vanish is made.

## CE06 — reduced-state closure

A and W alone do not determine their next values. For example (1,i,1) and (2,i/2,2) have the same A but at epsilon=.1,k=e,g=lambda=0 their next C are (-1,0,1) and (301/400)(-1,0,1).

For G_c=S+iA=conjugate(Omega)Omega^T, the pre-sync congruence uses intensities (G_c)_ii. If every pre-sync intensity is positive, define

\[
q_{ij}=\frac{\widetilde G_{c,ij}}{\sqrt{\widetilde G_{c,ii}\widetilde G_{c,jj}}},\quad
\delta_i=\lambda\sum_{j\sim i}\Im(q_{ij}^3),\quad
G^+_{c,ij}=\widetilde G_{c,ij}e^{i(\delta_j-\delta_i)}.
\]

This closes the rank-one Gram quotient on that one-step domain. Iteration requires remaining in it. Lambda=0 needs no nonzero restriction. Global Gram-only closure at nonzero lambda is false: (1,-1,0) and exp(i pi/6)(1,-1,0) have equal Gram matrices but the distinct next areas in CE05. No global common-phase-invariant reduction is inferred across Arg0 zeros.

## CE07 — anisotropy expansion with its remainder

For a triad write M_state=diag(d+a_i)+gL3, e·a=0, b=d-3g, C_perp=P_perp C. At fixed supplied state,

\[
\widetilde\Gamma=b^2\Gamma-b(a\cdot C_\perp)+O(|a|^2),
\]
\[
\widetilde C_\perp=bdC_\perp-dP_\perp(a\odot C)+g\Gamma a+O(|a|^2)
=bdC_\perp-dP_\perp(a\odot C_\perp)-\tfrac b3\Gamma a+O(|a|^2).
\]

The full parallel-to-transverse coefficient is -b/3, not +g alone. The omitted vector in the cofactor action is exactly diag(a_B a_C,a_C a_A,a_A a_B)C; project it for each displayed remainder. These scalars are internal multiplier anisotropy, not physical pressure.

## CE08 — exact endpoint conversion from the established entrance

Use the already documented endpoint Omega=c f_j, f_j(n)=exp(-2pi i j n/3)/sqrt(3). Put Q=|c|². Then

\[
C(c f_0)=0,\quad C(c f_1)=-\tfrac{\sqrt3}{6}Qe,\quad
C(c f_2)=+\tfrac{\sqrt3}{6}Qe,
\quad W=0\text{ for all three}.
\]

For j=1 or 2 let C0 be the signed scalar above, and set b_i=1+epsilon(k_i-Q/3)-3g. Since e^T f_j=0,

\[
\widetilde\Omega_i=b_i\Omega_i,\quad
\widetilde C=C_0(b_Bb_C,b_Cb_A,b_Ab_B)^T.
\]

When every b_i is nonzero, all pre-sync phase differences remain multiples of pi/3, including sign flips, so every harmonic-three torque is zero and C+=tildeC. For c nonzero and epsilon nonzero in this domain, W+ is nonzero **iff k is not uniform**: equal pair products for nonzero b_i force all b_i equal. With zero b_i use CE05 directly; do not extrapolate this proof through missing phases.

For f0 the pre-sync state remains a common complex scalar times real entries; CE05 applies. This converts hidden area for f1/f2, not zero total area. It does not reopen or physically calibrate the entrance.

## CE09 — local real-host Jacobian, not a global generation theorem

Let u be a real fixed point, all u_i nonzero, M_state(u)u=u. Put K_ij=3 sign(u_i u_j) for i≠j, K_ii=-sum_{j≠i}K_ij. The real and imaginary blocks are

\[
J_R=M_{state}(u)-2\epsilon\operatorname{diag}(u_i^2),\quad
J_I=\operatorname{diag}(u)(I+\lambda K)\operatorname{diag}(u)^{-1}M_{state}(u).
\]

For k=k0 e, k0>0, u=sqrt(k0)e, the six multipliers are

\[
1-2\epsilon k_0,\quad 1-3g-2\epsilon k_0\ (\times2),\quad
1,\quad (1-3g)(1-9\lambda)\ (\times2).
\]

The unit multiplier is common phase. Strict modulus <1 of the other five gives local linear stability transverse to the fixed circle. In the regime 0<g<1/3 with initially stable radial blocks, the imaginary transverse block crosses -1 at lambda*=(2-3g)/(9(1-3g)); g=1/5 gives 7/18. This is an eigenvalue crossing, not proof of a stable nonlinear period-two branch, its basin, or connection to a remote orbit. It does not create a perturbation from an exactly invariant zero-area trajectory.

## CE10 — ring Fourier and restricted plane-wave conclusions

Use Omega_n=M^(-1/2)sum_m z_m exp(i kappa_m n), kappa_m=2pi m/M, with modulo-M sums. Then

\[
\widetilde z_m=[1-4g\sin^2(\pi m/M)]z_m
+\frac\epsilon{\sqrt M}\sum_p\widehat k_{m-p}z_p
-\frac\epsilon M\sum_{p-q+r=m}z_p\overline z_q z_r.
\]

If b_n=exp(i delta_n), \(z_m^+=M^{-1/2}\sum_p\widehat b_{m-p}\widetilde z_p\). For a_n=Im(conjugate(Omega_n)Omega_(n+1)),

\[
\widehat a_\ell=\frac1{2i\sqrt M}\sum_p\overline z_p z_{p+\ell}(e^{i\kappa_{p+\ell}}-e^{-i\kappa_p}),\quad
\Gamma_M=\sum_m|z_m|^2\sin\kappa_m,
\]
\[
\Gamma_M^+-\Gamma_M=\sum_m\sin\kappa_m[2\Re(\overline z_m\Delta z_m)+|\Delta z_m|^2].
\]

Graph diffusion is diagonal; unequal periodic k can linearly mix modes, and onsite/phase nonlinearities can mix modes. The raw residue lift P intertwines the nonlinear triad/ring maps; the isometric Q generally does not. The exact M=12 lift stays in {0,4,8}. An exactly lifted initial state cannot spontaneously leave that invariant sector, even if off-sector linear perturbations would grow. Any later robustness experiment must separately declare an off-sector perturbation or different input; it must not attribute numerical leakage to a new exact source. The equal-k, carrier-m=1 plane wave discussed separately is not the residue-three entrance lift, and its stability conclusion cannot be transferred without a new analysis. A graph spectrum requires no asserted physical spatial calibration; it does not establish a turbulent or inverse magnetic cascade.

For constant k0 on a plane-wave line, with epsilon>0,

\[
r^+=|1+\epsilon(k_0-r^2)-4g\sin^2(\kappa/2)|r,
\quad r_*^2=k_0-(4g/\epsilon)\sin^2(\kappa/2)>0.
\]

Small nonzero r grows if 1+epsilon k0-4g sin²(kappa/2)>1. The positive-multiplier equilibrium is locally radially stable when 0<epsilon r*²<1; no off-line stability follows. The phase torque cancels on this line. No universal saturation follows: at epsilon=1/20,k=e a real balanced amplitude 10 maps to -39.5, and |a|²>41 yields continuing growth on that invariant real line. Retain only the actual Atlas-09 restricted bounded region.

The exact intensity budget, with dOmega=tildeOmega-Omega, is

\[
I^+-I=2\epsilon\sum_i(k_i|\Omega_i|^2-|\Omega_i|^4)
-2g\sum_{\text{cycle edges}}|\Omega_i-\Omega_j|^2+\|d\Omega\|^2.
\]

## CE11 — nonlinear covariants and Paper-F transfer

Let p=(S_AA,S_BB,S_CC), r=(S_BC,S_CA,S_AB). The quartic real-state polynomial K4=e·(p×r) is common-phase invariant and has (C3,H,V) signs (+,+,-); K4 e_z is an axial-z covariant. It is not linear in C, is conjugation-even and is not a proposed physical field. K4=12 at Omega=(1,2,3). This shows that K4 can be nonzero even when A=0, not that it is supported only on A=0: at Omega=(1,2,3i), K4=6 and C=(6,-3,0). H remains Paper B's geometric horizontal reflection; identifying complex conjugation with physical time reversal would be an additional, unadopted interpretation.

Hp=e·(p×C) and Hr=e·(r×C) are common-phase-invariant quartic pseudoscalars with signs (+,-,-). Their pairs (-8,8) and (52,6) at the specified GPT example states are not proportional. No unique quartic pseudoscalar or exhaustive invariant catalogue is claimed.

For Paper-F's oriented basis u=(1,-1,0)/sqrt(2), v=(1,1,-2)/sqrt(6), q(phi)=u cos phi+v sin phi, and its seed Omega=e+i h q(phi), h>0,

\[
C=e\times hq(\phi),\quad W=\frac{3h}{\sqrt2}(\cos(\phi-\pi/3),\sin(\phi-\pi/3),0).
\]

T is an orientation-preserving similarity on C_perp, so the accepted small-seed angular displacement transfers with this constant offset, retaining Paper-F's parameter, remainder and nonzero-direction hypotheses. It is not sustained circulation or a six-axis attractor. The correct general component expression is e×y=(y_C-y_B,y_A-y_C,y_B-y_A).

## Optional construction X01 — not adopted into the current connection

One may stipulate u^eta_ij=u^0_ij exp(i eta A_ij), with real eta of inverse-area units. Then u^eta_ji=conjugate(u^eta_ij), passive link covariance follows from invariant transported A, and the cyclic product is exp(i eta Gamma). This is a **NEW_ASSUMPTION_REQUIRED** composite readout rule, not the existing matched connection, not a unique extension, not an independent dynamical field and not an implementation recommendation. No peer acceptance of X01 as a model addition is presumed.

## Explicit exclusions

No magnetic field units, spatial Maxwell law, density/pressure/charge/current identification, physical helicity, smooth battery, universal attractor, or dynamo is established. Numerical thresholds/orbits are recorded separately with parameters and finite-run limits. The plasma sign convention remains external and unresolved. Acceptance of these mathematical statements authorizes no implementation.
