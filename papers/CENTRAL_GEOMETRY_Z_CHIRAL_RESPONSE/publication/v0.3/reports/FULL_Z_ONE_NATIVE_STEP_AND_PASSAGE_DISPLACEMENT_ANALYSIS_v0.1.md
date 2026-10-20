# Full Z Through One Native Update — Coupled Changes and Passage-Relative Displacement v0.1

20 October 2026 · Source-led written algebra for GPT and Hilmir’s review

**Answer.** The native update changes the macro amplitude and chiral contribution together because both come from its updated complex state. The pre-synchronization stage changes the norm; the simultaneous phase synchronizer preserves that norm but can change both the size and direction of chirality. The observer then adds a separate envelope change and clock-angle change.

For the exact fan-contact state from the preceding report, paired with the configuration specified in this order, the norm falls from exactly 3 to between 0.5432 and 0.5437. With the clock held fixed, full Z leaves the original upper fan and lands in the surrounding host space outside the band interior. With the actual scheduled envelope and angle advance, the next observation instead lies strictly inside the band’s planar interior at its new height. Both endpoints are in the central slab, closer horizontally to the axis and axially to the zero-member throat plane. Neither is on the throat plane, a fan, or a finite shell-notch patch. These are exact endpoint conclusions established below by written rational bounds; they do not establish a motion through the intervening band, an opening, or a throat aperture.

The proposed extension of the **initial** contact is also correct: the upper fan triangle set is independent of crystal magnitude and invariant as a set under the hand reflection. The same initial point therefore contacts an upper fan for every member and either hand. This does not make the band sections or throat positions independent of the member. The principal endpoint classification here uses the required PLUS zero reference.

## 1. Evidence, authority and fixed comparison

The authoritative checkout consulted was `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at actual local HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R2. Read-only tracked-status inspection was empty. Existing untracked material was preserved. The completed reports were consulted in the requested order, R2, R1, R0; primary source files were read as text. No scientific code, symbolic script, recurrence, test, simulation, application, new rendering, repository change or publication operation was performed. The sole new artifact is this report outside the checkout.

The work order supplies the scope and the deliberate pairing of existing inputs. The native and observer source files supply their definitions. R2 supplies the exact contact state and inherited geometry; the new dependency identities, one-step expressions and endpoint inequalities below are written derivations. Decimal coefficients in those formulas are treated as their exact terminating-decimal values. The rational enclosures are mathematical bounds, not measured output or certification of binary64 execution.

Retain

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,
\quad a=d/2,\quad h=s/2,\quad H=1/2,\quad O=(0,r,0).
\]

Thus \(h=\sqrt2a\), \(H-h=d\). The comparison is always

\[
\Phi(Z)=O+\mu R_z(\psi)Z,\qquad \mu>0,
\]

with the same \(\mu,\psi\) before and after. Write \(v=\Phi(Z)-O\) and \(w=v_z\). Crystal magnitude \(u=|\tau|\) and hand are fixed during the update. MINUS reflects the entire face complex; the distinct zero band meshes are not identified. No additional channel-to-ambient map is introduced. The component order of the channel-area triple remains the source order; its use as plotting coordinates is the declared comparison, not a recovered physical attachment. [R2 §§1–3,8; R1 §§1–3]

There is a scheduling distinction to retain, rather than silently reconcile: R0’s description of recording before an update concerns the historical display runner. The current `_runner.py` explicitly records an initial sample, then records each newly updated state after advancing its observers. This report uses that current schedule and its recomputed initialization. No relevant change to the native or observer formulas was found. [RUN; PRE]

## 2. The source schedule and actual two-stage native map

Let the supplied fixed native configuration be

\[
\mathcal P=(\epsilon,g,\lambda_{\rm phase},k_1,k_2,k_3).
\]

`DynamicsConfig` supplies no default physical tuple. In `step3`, `_advance` first forms

\[
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},
\qquad
V=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL_3\Omega. \tag{1}
\]

`phase_sync` then uses **all phases of this same V**:

\[
\varphi_j=\operatorname{Arg}_0V_j,\qquad
\delta_j=\lambda_{\rm phase}\sum_{m\ne j}\sin3(\varphi_m-\varphi_j),
\qquad
\Omega_j^+=|V_j|e^{i(\varphi_j+\delta_j)}. \tag{2}
\]

It does not substitute an already updated phase into another component’s increment. Antisymmetry gives \(\sum_j\delta_j=0\); this is not a common rotation of all components. Exact zeros have \(\operatorname{Arg}_0(0)=0\), and their output is explicitly zero. At \(\lambda_{\rm phase}=0\), the implementation returns V directly without extracting and reconstructing phases. No observer dt, forcing, noise, normalization, geometry or extra state appears in this native map. [D: `DynamicsConfig`, `arg0`, `phase_sync`, `_advance`, `step3`]

For each requested native update, the current runner performs:

1. `_step`: commit \(\Omega^+\) and increase the native update index.
2. `_advance`: advance each supplied observer’s clock; where memory exists, explicitly update it using the **new** native state.
3. `_observe`: recompute the readout with that new state and advanced observer; `_sample` records it.

The initial sample precedes these steps. The retained staged preset specifies recomputation, not historical constructor-zero storage. The relevant clock rules are

\[
\theta=\frac{2\pi(q\bmod N)}N,\qquad
q^+=(q+q_{\rm step})\bmod N,\qquad t_c^+=t_c+dt. \tag{3}
\]

The worked preset has \(N=12,q=0,q_{\rm step}=1,t_c=0,dt=0.1\). Its next clock is exactly \(q^+=1,t_c^+=0.1,\theta^+=\pi/6\). The modulo rule remains necessary at wrapping sectors. Observer dt is not a native integration step or a physical velocity calibration. [RUN: `_step`, `_advance`, `_append`, `run`; PRE: `historical_observer`; Z: `clock_angle`, `advance_clock`]

The EMA boundary is precisely the optional memory update in `_advance`, calling `advance_ema(new_state, current_memory)` before observation. An EMA decomposition would have to account for that explicit memory change and its different scalar law. No EMA evolution or SRG investigation is undertaken here.

## 3. Coupled norm and chirality identities

### 3.1 Pre-synchronization norm and intensity budget

Write \(\Omega=x+iy\), \(I_j=x_j^2+y_j^2\), \(\kappa=\|\Omega\|\), and \(C=x\times y\). Define the real symmetric, input-state-dependent matrix

\[
B=I+\epsilon\operatorname{diag}(k_j-I_j)+gL_3.
\]

Then \(V=Bx+iBy\). Synchronization preserves every component magnitude, so the proposed identity is confirmed:

\[
\boxed{(\kappa^+)^2=\|Bx\|^2+\|By\|^2.} \tag{4}
\]

Set \(D=V-\Omega\). Expanding \(\|\Omega+D\|^2\), and using
\(\Re(\overline\Omega\cdot L_3\Omega)=-\sum_{j<k}|\Omega_j-\Omega_k|^2\), gives

\[
\boxed{(\kappa^+)^2-\kappa^2
=2\epsilon\sum_j I_j(k_j-I_j)
-2g\sum_{j<k}|\Omega_j-\Omega_k|^2+\|D\|^2.} \tag{5}
\]

This is the existing intensity-budget identity, now applied to the complete update because the subsequent synchronizer leaves intensity unchanged. When \(\kappa^++\kappa>0\), the norm difference itself is the right side of (5) divided by \(\kappa^++\kappa\); when that denominator is zero, both norms and their difference are zero. The nonnegative finite-step remainder cannot generally be dropped. Even for positive g, no universal sign of the total change follows. No energy, potential or conservation interpretation is added. [ZD: `intensity_budget`]

### 3.2 Cofactor transport and the synchronizer’s separate contribution

Define the cofactor matrix by

\[
(\operatorname{cof}B)_{ij}=(-1)^{i+j}\det B_{\widehat i,\widehat j}.
\]

For invertible B this is \(\det(B)B^{-T}\); its transpose is the adjugate. Expansion of the cross product by its alternating minors gives the polynomial identity

\[
\boxed{C_V=(Bx)\times(By)=\operatorname{cof}(B)C.} \tag{6}
\]

For example, each coefficient of \(x_p y_q-x_q y_p\) on the left is the corresponding signed two-by-two minor of B. Thus (6) holds also when B is singular; it does not depend on taking an inverse or on treating B as a Jacobian. B is simply held at its value for this input state.

Put \(r_j=|V_j|\). For cyclic pairs \((j,k)=(2,3),(3,1),(1,2)\), respectively,

\[
C_{V,i}=r_jr_k\sin(\varphi_k-\varphi_j),
\qquad
\boxed{C_i^+=r_jr_k\sin(\varphi_k-\varphi_j+\delta_k-\delta_j).} \tag{7}
\]

The full change therefore separates exactly as

\[
C^+-C=(\operatorname{cof}B-I)C+(C^+-C_V), \tag{8}
\]
\[
(C^+-C_V)_i=r_jr_k\left[
\sin(\varphi_k-\varphi_j+\delta_k-\delta_j)
-\sin(\varphi_k-\varphi_j)\right].
\]

The pre-sync stage can change norm and chirality. Synchronization cannot change the norm, but its different relative phase increments can change chirality’s magnitude and direction. Neither stage is generally a scalar rescaling of C or a rigid rotation of its plotted arrow. The worked example below actually has an increase of chiral magnitude during synchronization, following a much larger pre-sync decrease.

For any resulting state \(\Omega^+=x^++iy^+\),

\[
\left(\frac{(\kappa^+)^2}{2}\right)^2-\|C^+\|^2
=\frac{(\|x^+\|^2-\|y^+\|^2)^2}{4}+(x^+\cdot y^+)^2\ge0.
\]

Consequently the sharp same-state bound remains

\[
\boxed{\|C^+\|\le(\kappa^+)^2/2.} \tag{9}
\]

Equality is attained when the real and imaginary parts are orthogonal and have equal norm. [RO: `z_chiral`; ZD: `chiral_area_accounting`]

### 3.3 Zeros and the common-phase qualification

The zero input remains zero. A nonzero input can also have V=0; then \(\kappa^+=C^+=0\). Singular B is already covered by (4)–(6). Rank at most one forces \(\operatorname{cof}B=0\) and hence \(C_V=0\); rank two need not. A zero V component remains zero under synchronization, and the components of (7) containing its magnitude vanish. Nevertheless its assigned phase zero still enters the increments of the other components.

Pre-synchronization is covariant under a common complex phase, since B depends on intensities. Synchronization is likewise covariant when **all V components are nonzero**, and the bypass at \(\lambda_{\rm phase}=0\) preserves covariance even at zeros. General covariance across pre-sync zero components is false. The readout identity \(C(e^{i\chi}\Omega)=C(\Omega)\) remains true for each state; it does not repair a noncovariant native map.

There is also no unconditional invariance of \(C=0\). A concise written counterexample uses \(\epsilon=g=0\), \(\lambda_{\rm phase}=\pi/12\), any k, and

\[
\Omega=V=e^{i\pi/6}(1,-1,0).
\]

Initially C=0. The zero convention yields \((\delta_1,\delta_2,\delta_3)=(-\lambda_{\rm phase},\lambda_{\rm phase},0)\), so

\[
\Omega^+=e^{i\pi/6}(e^{-i\lambda_{\rm phase}},-e^{i\lambda_{\rm phase}},0),
\qquad C^+=(0,0,-\sin(2\lambda_{\rm phase}))=(0,0,-1/2).
\]

By contrast, the common-phase-related input \((1,-1,0)\) has all phase increments zero and retains C=0. This proves both failures without execution. If C=0 and all three V components are nonzero, (6) gives \(C_V=0\), their phases differ only by zero or pi, and every sine in (2) vanishes: C=0 is then preserved. If at most one V component is nonzero, chirality is necessarily zero afterwards as well. The mixed-sign, zero-component case above is the obstruction to a universal claim. [D: `arg0`, `phase_sync`; TD: documented phase-covariance qualifications]

### 3.4 Norm and chirality alone do not determine their next values

Use the very same fixed configuration later required for the principal example,
\(\mathcal P_{\rm check}=(0.1,0.2,0.17,(2,3,4))\). The two inputs
\((1,0,0)\) and \((0,1,0)\) both have \((\kappa,C)=(1,0)\). Their pre-sync outputs are respectively

\[
(0.7,0.2,0.2),\qquad (0.2,0.8,0.2).
\]

All components are positive real, so synchronization changes neither. Their next squared norms are \(57/100\) and \(72/100\), respectively. Thus even with the configuration fixed, \((\kappa,C)\) does not close the next-step dependency. The native state must be retained. This counterexample is a sufficiency check, not a replacement for the principal contact state or a proposed reduced evolution law.

## 4. Native, envelope and clock-angle displacement

With the staged defaults unchanged, write

\[
A(\Omega,t_c)=0.618\frac{\kappa}{1+\kappa}e^{-0.577t_c},
\quad f(\theta)=\cos3(\theta-0.244),
\quad d(\theta)=(\cos\theta,\sin\theta,1),
\]
\[
v(\Omega,\theta,t_c)=\mu R_z(\psi)
\left[\alpha A(\Omega,t_c)f(\theta)d(\theta)+\beta C(\Omega)\right],
\quad \alpha=1,\quad\beta=1/2. \tag{10}
\]

Subtracting two fractions confirms the proposed amplitude identity:

\[
\boxed{A(\Omega^+,t_c)-A(\Omega,t_c)
=0.618e^{-0.577t_c}
\frac{\kappa^+-\kappa}{(1+\kappa^+)(1+\kappa)}.} \tag{11}
\]

Its denominators are positive, including at zero norm. At fixed time the amplitude change has exactly the norm change’s sign. There is no independent choice of the new amplitude or chiral offset. [Z: `state_norm`, `saturated_norm`, `staged_scalar`, `macro_vector`, `blend_vectors`, `observe_staged`]

Define the attribution endpoints

\[
v_0=v(\Omega,\theta,t_c),\quad v_N=v(\Omega^+,\theta,t_c),
\quad v_E=v(\Omega^+,\theta,t_c+dt),
\quad v_1=v(\Omega^+,\theta^+,t_c+dt).
\]

Put \(A_+=A(\Omega^+,t_c)\), \(A_0=A(\Omega,t_c)\), and \(E=e^{-0.577dt}\). Then

\[
v_N-v_0=
\underbrace{\mu\alpha R_z(\psi)(A_+-A_0)f(\theta)d(\theta)}_{\Delta_{\rm norm}}
+\underbrace{\mu\beta R_z(\psi)(C^+-C)}_{\Delta_C}, \tag{12}
\]
\[
v_E-v_N=\underbrace{\mu\alpha R_z(\psi)A_+(E-1)f(\theta)d(\theta)}_{\Delta_E}, \tag{13}
\]
\[
v_1-v_E=\underbrace{\mu\alpha R_z(\psi)A_+E
\left[f(\theta^+)d(\theta^+)-f(\theta)d(\theta)\right]}_{\Delta_\theta}. \tag{14}
\]

Thus

\[
\boxed{v_1-v_0=\Delta_{\rm norm}+\Delta_C+\Delta_E+\Delta_\theta.} \tag{15}
\]

If useful, the bracket in (14) is itself
\([f(\theta^+)-f(\theta)]d(\theta)+f(\theta^+)[d(\theta^+)-d(\theta)]\), separating harmonic and directional changes in a stated order. The exponential acts only on the macro term. It is not an imposed decay of C. The points \(v_N,v_E\) are attribution conventions, not additional observations emitted by the runner. Reordering these intermediate changes reallocates contributions but leaves the total difference unchanged.

## 5. Reusable finite-geometry conditions

For two relative endpoints v and v', compare

\[
\Delta R_\perp^2=(v_x'^2+v_y'^2)-(v_x^2+v_y^2),
\qquad
\Delta D_*^2=(w'-w_*)^2-(w-w_*)^2. \tag{16}
\]

These test horizontal approach to the axis and axial approach to the **fixed** throat plane, respectively. They do not test distance to the throat boundary or entry through its finite aperture. In the inherited notation \(\xi=u/r\),

\[
w_*=h\frac{\xi^2}{2+\xi^2-4\xi/\sqrt3}.
\]

For \(|w|\le h\), R1 supplies the actual continuous radial boundary \(R(w,\varphi)\) of the star-shaped band section. At nonzero horizontal radius, compare \(R_\perp\) with that value at the endpoint’s **total-vector** azimuth: less means band interior, equality band surface, greater means outside the band interior. Calling the latter surrounding host space additionally requires host membership, which in this slab is
\(n_k\cdot v_{xy}<r\) for all three panel normals. The sufficient condition \(R_\perp<r\) is convenient here. On the axis, the section’s positive clearance places the point inside without inventing an azimuth. Outside the slab this band-interior predicate is not applied. At \(w=w_*\) the same finite section condition is still required. [R1 §2; R2 §2]

For a nondegenerate finite triangle \(F=[p_0,p_1,p_2]\), use both its plane residual \(r_F(v)=n_F\cdot v-c_F\) and its finite domain. Explicitly put \(U=p_1-p_0\), \(W=p_2-p_0\), \(Y=v-p_0\), and

\[
G=(U\cdot U)(W\cdot W)-(U\cdot W)^2>0,
\]
\[
b_1=\frac{(Y\cdot U)(W\cdot W)-(Y\cdot W)(U\cdot W)}G,
\quad
b_2=\frac{(Y\cdot W)(U\cdot U)-(Y\cdot U)(U\cdot W)}G,
\quad b_0=1-b_1-b_2. \tag{17}
\]

Contact is equivalent to \(r_F(v)=0\) and all \(b_i\ge0\). With a fixed normal, \(|r_F|/\|n_F\|\) is distance to the supporting plane, not automatically to the finite triangle. An actual triangle-distance comparison would require minimizing
\(\|v-(p_0+b_1U+b_2W)\|^2\) over \(b_1,b_2\ge0,b_1+b_2\le1\), including its edges and vertices. No unperformed finite-distance minimization is used below. [R1 §3; R2 §6]

The actual upper opening directions are

\[
g_0=(\sqrt3/2,-1/2),\quad g_1=(0,1),\quad
g_2=(-\sqrt3/2,-1/2).
\]

For PLUS, lower opening directions are \(R_{-\arctan(u/r)}g_k\); MINUS uses the reflected whole geometry. They are opening axes, not channel labels or fan-tip directions. The finite upper openings are the sectors between the boundary arcs \(U_k--T_{2k+1}--U_{k+1}\) above h. Their flanking endpoints at \(w=h+d\lambda\) are

\[
\left[(1-\lambda)a+\lambda r/2\right]g_k
\ \pm\ \lambda\sqrt3r\,Jg_k/2,\qquad 0<\lambda<1.
\]

There is no material patch joining those endpoints. A directional projection \(g_k\cdot v_{xy}\), or its change, is only a projection.

The separate shell-notch patch \(\mathcal N_k^\sigma\), \(\sigma=\pm1\), requires all of

\[
\lambda_N=(\sigma w-h)/d\in[0,1],\qquad
g_k\cdot v_{xy}+\sigma\sqrt3w/2=K,
\qquad |Jg_k\cdot v_{xy}|\le d\lambda_N/2,
\]
\[
K=2r+\sqrt3h/2. \tag{18}
\]

These conditions keep finite notch measurements distinct from the crystal fans and their intervening openings. [R2 §3]

Even endpoints on opposite sides of a supporting plane would not supply an intermediate observation, a collision, or passage through its finite triangle. No straight interpolation is inserted. Geometry is absent from (1)–(3) and (10): changing u or hand while holding the state, configuration and placement fixed changes the comparison targets, not the computed endpoints. No attraction, flux, steering or physical velocity is inferred from (15).

## 6. Short written check against the documented source fixture

The source test `DynamicsTests.test_one_step_against_hand_calculated_pre_sync_state` supplies

\[
\Omega_{\rm check}=(1,2i,-1+i),\qquad
\mathcal P_{\rm check}=(0.1,0.2,0.17,(2,3,4)).
\]

Here \(x=(1,0,-1)\), \(y=(0,2,1)\), \(I=(1,4,2)\), and

\[
B=\begin{pmatrix}7/10&1/5&1/5\\1/5&1/2&1/5\\1/5&1/5&4/5\end{pmatrix},
\qquad
V=(1/2+3i/5,\ 6i/5,\ -3/5+6i/5),
\]
\[
\kappa^2=7,\qquad (\kappa^+)^2=77/20,\qquad
C=(2,-1,2),\qquad C_V=(18/25,-24/25,3/5). \tag{19}
\]

The cofactor matrix is

\[
\operatorname{cof}B=
\begin{pmatrix}9/25&-3/25&-3/50\\-3/25&13/25&-1/10\\-3/50&-1/10&31/100\end{pmatrix},
\]

whose product with C gives the displayed \(C_V\). Also \(D=(-1/2+3i/5,-4i/5,2/5+i/5)\), \(\|D\|^2=29/20\), \(\sum I_j(k_j-I_j)=1\), and the pair-distance sum is 12. Equation (5) gives
\(1/5-24/5+29/20=-63/20=77/20-7\), as required.

The nonzero synchronizer is retained explicitly. For \(\tau_{jk}=\sin3(\varphi_k-\varphi_j)\), elementary triple-angle identities give

\[
\tau_{12}=\frac{415}{61\sqrt{61}},\qquad
\tau_{13}=-\frac{1744}{305\sqrt{305}},\qquad
\tau_{23}=\frac{11}{5\sqrt5}.
\]

Thus

\[
(\delta_1,\delta_2,\delta_3)
=\frac{17}{100}(\tau_{12}+\tau_{13},-\tau_{12}+\tau_{23},-\tau_{13}-\tau_{23}),
\quad \Omega_j^+=V_j e^{i\delta_j}. \tag{20}
\]

In particular \(\tau_{12}>4/5\), \(\tau_{13}>-2/5\), so \(\delta_1>0\); synchronization has not been turned off. Inserting these increments and the fixture’s phases \(\operatorname{atan2}(6,5),\pi/2,\operatorname{atan2}(2,-1)\) into (7) gives its exact post-sync C. Norm (19) is unchanged by this stage. These are written identities agreeing with the documented expected expression, not an appeal to its rounded assertion or an executed test. The fixture is neither a physical default nor a retained trajectory. Its unequal k does not confer fixed-parameter cyclic dynamical symmetry. [TD: lines 13–23]

## 7. Continue exactly R2’s contact state

### 7.1 Unchanged state, configuration and reference geometry

Use the prescribed PLUS zero reference, \(\mu=1,\psi=0,q=0,t_c=0\), and

\[
F=[T_0,T_1,U_0],\qquad
P=\left(\frac{\sqrt3a}{6},-\frac a2-\frac r3,\frac{2h+H}{3}\right).
\]

R2’s exact state is retained in full, including its basis choice:

\[
A_*=0.4635,\quad c=\cos(0.732),\quad
c_*=2[P-A_*c(1,0,1)]=(c_1,c_2,c_3),\quad L=\|c_*\|,
\]
\[
t=\sqrt{c_1^2+c_2^2},\quad p=(-c_2,c_1,0)/t,\quad q=(c_*/L)\times p,
\]
\[
X=\sqrt{\frac{9+\sqrt{81-4L^2}}2},\qquad
Y=\sqrt{\frac{9-\sqrt{81-4L^2}}2},\qquad
\Omega_*=Xp+iYq. \tag{21}
\]

The scalar t in this paragraph is only a basis denominator, not clock time or crystal magnitude. To make the calculation transparent, \(XY=L\) gives the equivalent **same state**

\[
x=\left(-\frac{Xc_2}{t},\frac{Xc_1}{t},0\right),\qquad
y=\left(-\frac{c_3c_1}{Xt},-\frac{c_3c_2}{Xt},\frac tX\right). \tag{22}
\]

No representative with merely the same norm and C has been substituted. This state has \(\kappa_*=3\), \(C_*=c_*\), and \(v_0=A_*c(1,0,1)+c_*/2=P\), with fan barycentric weights \((1/3,1/3,1/3)\). [R2 (22)–(25)]

As explicitly directed, pair this existing state with \(\mathcal P_{\rm check}\) and the staged schedule of §2. This combination is a declared mathematical probe; it is not attributed to an earlier run or selected after inspecting the outcome.

### 7.2 Closed one-step expressions

With \(I_j=x_j^2+y_j^2\) from (22), put

\[
B_*=
\begin{pmatrix}
0.8-0.1I_1&0.2&0.2\\
0.2&0.9-0.1I_2&0.2\\
0.2&0.2&1-0.1I_3
\end{pmatrix},
\qquad W=V_*=B_*x+iB_*y. \tag{23}
\]

In particular its real components are
\(((0.8-0.1I_1)x_1+0.2x_2,\ 0.2x_1+(0.9-0.1I_2)x_2,\ 0.2(x_1+x_2))\),
and its imaginary components are \(B_*y\). These are closed expressions in the fixed radicals and \(\cos(0.732)\) in (21).

All W components are nonzero, as certified below. Define

\[
r_j=|W_j|,\quad s_{jk}=\frac{\Im(\overline W_jW_k)}{r_jr_k},\quad
\tau_{jk}=3s_{jk}-4s_{jk}^3\quad(j<k),
\]
\[
(\delta_1,\delta_2,\delta_3)
=0.17(\tau_{12}+\tau_{13},-\tau_{12}+\tau_{23},-\tau_{13}-\tau_{23}). \tag{24}
\]

The triple-angle identity makes this exactly (2), without needing approximate arguments. The required complete next state and readouts are

\[
\boxed{\Omega_{*,j}^+=W_j(\cos\delta_j+i\sin\delta_j),\qquad
\kappa_*^+=\sqrt{\sum_j|W_j|^2},}
\]
\[
\boxed{C_{*,i}^+=\Im\!\left(\overline W_jW_k e^{i(\delta_k-\delta_j)}\right)}
\quad\text{for cyclic }(j,k). \tag{25}
\]

Together (21)–(25) explicitly specify the next state and all three chiral components from the original state, with no free fit or suppressed phase stage.

Set

\[
A_+=0.618\frac{\kappa_*^+}{1+\kappa_*^+},\qquad
b=A_+c,\quad E=e^{-0.0577},\quad s_\ell=\sin(0.732),\quad b_1=A_+Es_\ell.
\]

Since \(f(0)=c\) and \(f(\pi/6)=s_\ell\), the requested endpoints are exactly

\[
\boxed{v_N=(b,0,b)+C_*^+/2,\qquad
v_E=(bE,0,bE)+C_*^+/2,}
\]
\[
\boxed{v_1=(\sqrt3b_1/2,b_1/2,b_1)+C_*^+/2.} \tag{26}
\]

The separate contributions are

\[
\Delta_{\rm norm}=(b-A_*c)(1,0,1),\qquad
\Delta_C=(C_*^+-c_*)/2,
\]
\[
\Delta_E=b(E-1)(1,0,1),\qquad
\Delta_\theta=(\sqrt3b_1/2-bE,\ b_1/2,\ b_1-bE). \tag{27}
\]

### 7.3 Hand-derived rational certificate

Every interval in this subsection is open and has rational, terminating-decimal endpoints. They are deliberately wider than needed. The following elementary enclosures start the derivation:

\[
1.4142135<\sqrt2<1.4142136,\qquad
1.7320508<\sqrt3<1.7320509,
\]
\[
0.7438391<c<0.7438393,\quad
0.6683<s_\ell<0.6684,\quad 0.9439<E<0.9440. \tag{28}
\]

The root bounds follow by squaring the rational endpoints. For c, the alternating cosine polynomials through degree ten and degree eight at the exact rational argument 183/250 bound it below and above; rational substitution places both between the stated endpoints. Sine’s degree-seven and degree-nine alternating bounds give the displayed s_ell interval. The alternating exponential polynomials through degree five and degree four at 577/10000 bound E below and above. Thus (28) does not rely on a numerical trigonometric evaluator.

Substitution in (21), positive-root comparison by squaring, and the cancellation-free formula (22) give

| Quantity | Rational enclosure |
|---|---|
| \(c_1\) | \((-0.6049883,-0.6049877)\) |
| \(c_2\) | \((-0.3388968,-0.3388966)\) |
| \(c_3\) | \((-0.0800636,-0.0800629)\) |
| \(t\) | \((0.69344,0.69345)\) |
| \(X\) | \((2.99090,2.99092)\) |
| \(x_1,x_2,x_3\) | \((1.4616,1.4618),\ (-2.6095,-2.6093),\ 0\) |
| \(y_1,y_2,y_3\) | \((-0.02336,-0.02334),\ (-0.01309,-0.01307),\ (0.23184,0.23186)\) |

Using the signs in these intervals in the explicit real matrix (23) yields

| Component j | \(\Re W_j\) | \(\Im W_j\) |
|---|---|---|
| 1 | \((0.33497,0.33523)\) | \((0.03005,0.03008)\) |
| 2 | \((-0.27953,-0.27916)\) | \((0.03882,0.03885)\) |
| 3 | \((-0.22958,-0.22950)\) | \((0.22330,0.22334)\) |

For a representative intermediate arithmetic check, these input intervals give
\(2.1368193156<I_1<2.1374049296\), hence
\(0.58625950704<(B_*)_{11}<0.58631806844\). Multiplying by the positive x_1 interval and adding \(0.2x_2\) encloses \(\Re W_1\) between 0.33497 and 0.33523 as shown. All the other entries follow from the same signed sums and products in (23).

Squaring the W bounds gives

\[
0.3363<r_1<0.3366,\quad 0.2818<r_2<0.2823,\quad
0.3202<r_3<0.3204,
\]
\[
0.295078<(\kappa_*^+)^2<0.295519,
\qquad 0.5432<\kappa_*^+<0.5437. \tag{29}
\]

The phase calculation can be checked entirely with products, quotients and the cubic in (24):

| Pair jk | \(s_{jk}\) | \(\tau_{jk}\) |
|---|---|---|
| 12 | \((0.2251,0.2262)\) | \((0.629,0.633)\) |
| 13 | \((0.7575,0.7595)\) | \((0.526,0.534)\) |
| 23 | \((-0.5932,-0.5905)\) | \((-0.948,-0.944)\) |

For example,
\(0.0213922934<\Im(\overline W_1W_2)<0.0214319479\) and
\(0.09476934<r_1r_2<0.09502218\), giving the first s interval. The cubic \(3s-4s^3\) is increasing on that interval and decreasing on each of the other two, so its endpoint values give the stated tau enclosures. The other imaginary products are bounded by
\(0.081695276<\Im(\overline W_1W_3)<0.0817760346\) and
\(-0.0535210402<\Im(\overline W_2W_3)<-0.053417245\).

Consequently

\[
\delta_1\in(0.1963,0.1984),\quad
\delta_2\in(-0.2688,-0.2674),\quad
\delta_3\in(0.0697,0.0718). \tag{30}
\]

On these short intervals, the alternating sine bounds through degrees three/five and cosine bounds through degrees six/four, together with monotonicity and parity, give

| j | \(\cos\delta_j\) | \(\sin\delta_j\) |
|---|---|---|
| 1 | \((0.9803,0.9808)\) | \((0.1950,0.1972)\) |
| 2 | \((0.9640,0.9645)\) | \((-0.2657,-0.2642)\) |
| 3 | \((0.9974,0.9976)\) | \((0.0696,0.0718)\) |

Multiplying \(W_j\) by these rotations, and then taking the actual cross product, gives

| j | \(x_j^+\) | \(y_j^+\) | \(C_{*,j}^+\) |
|---|---|---|---|
| 1 | \((0.3224,0.3230)\) | \((0.0947,0.0957)\) | \((-0.0266,-0.0259)\) |
| 2 | \((-0.2594,-0.2587)\) | \((0.1111,0.1118)\) | \((-0.0903,-0.0896)\) |
| 3 | \((-0.2451,-0.2444)\) | \((0.2062,0.2069)\) | \((0.0603,0.0610)\) |

For example the lower bound on C_1^+ follows from
\(-0.2594(0.2069)+0.2444(0.1111)=-0.02651702>-0.0266\); the upper bound follows from
\(-0.2587(0.2062)+0.2451(0.1118)=-0.02594176<-0.0259\).
The other two components use exactly the other cyclic products in (7).

The same intervals prove \(L>0.69\), \(\|C_V\|<0.101\), and
\(0.111<\|C_*^+\|<0.113\). Thus chirality decreases greatly in the pre-sync stage and increases in magnitude during synchronization; its third component changes from negative initially to positive afterwards. It has not undergone a common positive rescaling. The final bound (9) is consistent with these values.

Finally, monotonicity of \(\kappa/(1+\kappa)\), followed by positive products with (28), gives

\[
0.2175<A_+<0.2177,\qquad
0.16178<b<0.16194,\qquad
0.13720<b_1<0.13737. \tag{31}
\]

Equations (26) consequently give the decisive endpoint enclosures

| Endpoint | x | y | w |
|---|---|---|---|
| Native-only \(v_N\) | \((0.14848,0.14899)\) | \((-0.04515,-0.04480)\) | \((0.19193,0.19244)\) |
| Scheduled \(v_1\) | \((0.10551,0.10602)\) | \((0.02345,0.023885)\) | \((0.16735,0.16787)\) |

The separated changes in (27), also as rational bounds, make their different roles visible:

| Contribution | x | y | w |
|---|---|---|---|
| Norm/amplitude | \((-0.1830,-0.1828)\) | 0 | same as x |
| Chirality | \((0.2891,0.2896)\) | \((0.1242,0.1247)\) | \((0.0701,0.0706)\) |
| Envelope | \((-0.00909,-0.00905)\) | 0 | same as x |
| Harmonic/angle | \((-0.0341,-0.0337)\) | \((0.06860,0.068685)\) | \((-0.01568,-0.01533)\) |

In particular, native amplitude contraction alone would give the wrong full displacement. The simultaneous change in the same state’s chirality contributes positively to all three plotted coordinates here.

## 8. What these endpoints do relative to the passage

### 8.1 The original finite fan contact is lost

For the specified F, the R2 plane normal and constant simplify to

\[
n_F=(1/2,-\sqrt3/2,-\gamma_f),\quad
\gamma_f=\frac{2+\sqrt2-\sqrt3}{4},\quad
c_F=\frac{\sqrt3-\sqrt2}{8}. \tag{32}
\]

Initially \(r_F(P)=0\), with all three barycentric weights equal to 1/3. The bounds above, using
\(0.4205<\gamma_f<0.4206\) and \(0.0397<c_F<0.0398\), give

\[
-0.0078<r_F(v_N)<-0.0067,\qquad
-0.0785<r_F(v_1)<-0.0772. \tag{33}
\]

Both endpoints depart to the negative side of this fixed oriented plane. The scheduled endpoint is farther from the supporting plane than the native-only endpoint. There is an independent finite-domain obstruction: every point of F has \(h\le w\le H\), while both new heights are strictly below h. In a putative barycentric representation on F, the tip weight would be \((w-h)/d<0\). Thus neither endpoint contacts the actual finite triangle, irrespective of any infinite-plane interpretation.

Both endpoints have positive distance from the original contacted triangle: for every p in F, \(\|v-p\|\ge h-w>0\). This only establishes departure from the initial zero distance. No ordering of the two new **finite-triangle** distances is claimed from (33), and no omitted edge/vertex minimization is implied. The height obstruction also excludes all upper and lower fan triangles at these endpoints.

### 8.2 Central slab, host, band interior and throat

The endpoint bounds give \(0<w_1<w_N<h\). Both have horizontal radius less than r, so both are strictly inside the host’s central triangular region. They lie in the band’s height slab, where a section-interior predicate is applicable.

At u=0 every band-section boundary point is a convex combination of radius-a ring vertices, so \(R(w,\varphi)\le a\). For the native-only point,

\[
R_{\perp,N}\ge (v_N)_x>0.14848>a.
\]

Hence \(v_N\) is strictly in the surrounding host space, outside the filled band section. It is not a band-surface contact.

For the scheduled endpoint, a stronger local lower bound on the **actual** section is useful. At \(u=0\), put \(\eta=(1-w/h)/2\). On a top-two-vertex band triangle, its unit horizontal plane normal has projection
\(a\sqrt3(1-\eta)/2\) on every point of that section segment. On a bottom-two-vertex triangle \([T_i,B_{i+2},B_{i+1}]\), projection on \(e_i\) is at least \(a(1-3\eta/2)\). Whenever these quantities are positive, every boundary point therefore satisfies

\[
R(w,\varphi)\ge
\min\{a\sqrt3(1-\eta)/2,\ a(1-3\eta/2)\}. \tag{34}
\]

This uses the actual triangles and their fixed height weights, not a corresponding-index interpolated scaffold. For \(v_1\), (28) and its height bound give \(0<\eta_1<0.097\). Since \(a>0.1464\) and \(\sqrt3/2>0.8660\), both lower bounds in (34) exceed 0.1144. But

\[
R_{\perp,1}^2<0.1061^2+0.0239^2=0.01182842<0.109^2.
\]

Thus \(R_{\perp,1}<0.109<0.1144<R(w_1,\varphi_1)\): the actual next observation is **strictly inside** the filled band section at its new height. It is not on the band surface. The attribution endpoints v_N and v_1 belong to different regions; that fact supplies no observation on the separating surface.

The radial comparison itself is strict:

\[
R_{\perp,1}^2<0.01182842
<0.14848^2<R_{\perp,N}^2
<0.1490^2+0.0452^2=0.02424404
<0.04^2+0.169^2<R_{\perp,0}^2. \tag{35}
\]

For the principal zero member \(w_*=0\), and

\[
0<w_1<w_N<P_w=(2h+H)/3,
\qquad (w_1-w_*)^2<(w_N-w_*)^2<(P_w-w_*)^2. \tag{36}
\]

Both are closer to the throat plane and neither reaches it. The scheduled endpoint is inside the passage’s section at **w_1**, not in the throat aperture at w=0. R2’s distinction remains: the band interior has an area minimum at the throat, whereas the surrounding space has an area maximum there. No area-speed or pressure claim follows from either endpoint classification.

### 8.3 Opening-direction projections and finite notch exclusion

The three upper directions, and the lower directions at this zero reference, give:

| Endpoint | \(g_0\cdot v_{xy}\) | \(g_1\cdot v_{xy}\) | \(g_2\cdot v_{xy}\) |
|---|---|---|---|
| P, exactly | \(a/2+r/6\) | \(-a/2-r/3\) | \(r/6\) |
| \(v_N\), rational enclosure | \((0.1509,0.1517)\) | \((-0.04515,-0.04480)\) | \((-0.1067,-0.1059)\) |
| \(v_1\), rational enclosure | \((0.0794,0.0802)\) | \((0.02345,0.023885)\) | \((-0.1039,-0.1030)\) |

The initial first projection is between 0.1213 and 0.1214. It increases under the native-only comparison, but the combined scheduled value is below its initial value. The g_1 projection increases and changes sign in the scheduled comparison; the g_2 projection decreases from its positive initial value to negative. Thus even these three simple directional measures do not describe a common motion toward all openings.

These are projections of the full endpoint, not its macro angle or a channel permutation. Both new endpoints have \(|w|<h\), outside the upper/lower finite fan-opening height ranges and outside every finite notch patch’s domain in (18). They therefore do not provide an endpoint in one of those openings or a notch contact. Initial P is itself in a fan interior, not an opening. No walls close the intervening fan sectors into ducts, and no route between P and the next point is specified.

### 8.4 Verify the initial-contact strengthening, with its proper limits

For every allowed u, the upper vertices \(T_i=(ae_i,h)\) and \(U_k=(rn_k,H)\) are unchanged. The upper triangles remain
\([T_{2k-1},T_{2k},U_k]\) and \([T_{2k},T_{2k+1},U_k]\). Under the hand reflection \(S(x,y,w)=(-x,y,w)\),

\[
Se_i=e_{-i},\qquad ST_i=T_{-i},\qquad SU_k=U_{-k}.
\]

This permutes the six upper triangles, exchanging the two sides of the corresponding fans. In particular S sends \([T_0,T_1,U_0]\) to \([T_0,T_5,U_0]\), and sends that partner back to the same geometric F. The upper fan triangle set is invariant. Therefore the unchanged point P, and hence the unchanged initial full-Z observation, belongs to a fan for every member and either hand. This confirms GPT’s proposed strengthening as an equality of geometric target sets; it requires no transformation or refitting of the native state.

The endpoints (26) likewise do not change when only the comparison member or hand is changed. Their height-based fan and notch exclusions persist. The throat height depends on u and is preserved by the hand reflection; the band radial function and lower opening directions follow the member and hand rules in R1/R2. The zero-reference band conclusions in §8.2 have not been assumed to cover that family. The two zero band face complexes remain distinct. No family sweep or new state selection is undertaken.

## 9. Scope and stopping point

The confirmed cofactor and amplitude identities give exact coupled dependencies; the explicit synchronizer term supplies the part that a norm-only or pre-sync-only account would miss. The exact continued witness loses its original fan contact. The native-only attribution endpoint is in the surrounding space, while the scheduled next observation is inside the band interior and still above the throat. The rational certificate resolves these signs without scientific execution or a fitted replacement state.

A deliberately supplied one-step input does not establish reachability from a historical seed, persistent contact, recurrence, attraction or physical passage. The observational displacement is not a velocity or flux. The preceding report’s conditional fluid comparison is sufficient background and has not been extended. SRG, memory investigations, anisotropic fitting and publication work remain deferred. Work stops with this report for GPT and Hilmir’s review; no follow-on order is issued.

## Source locations

Named functions and sections identify the consulted portions; test assertions and prior computational claims are documentary source material, not execution evidence for this report.

| Key | Exact file and relevant portions |
|---|---|
| R2 | [Full Z and central-passage report][R2], §§1–3 geometry/throat/openings; §§5–6 same-state and finite-target conditions; §7 equations (22)–(25), exact contact state; §8 scope and symmetries |
| R1 | [Macro middle-band report][R1], §§1–3 actual face list, star-shaped sections, face-plane table and barycentric criterion; §5 PLUS zero reference |
| R0 | [Original Z/crystal report][R0], recovered native/observer definitions, historical runner distinction, declared placement and channel/ambient distinction |
| D | [dynamics.py][D], `L3` line 12; `DynamicsConfig` 27–44; `arg0` 57–63; `phase_sync` 66–84; `_advance` 87–96; `step3` 99–104 |
| RO | [readouts.py][RO], `z_chiral`, lines 7–17 |
| Z | [z_manifold.py][Z], `Clock`, `clock_angle`, `advance_clock` 46–82; `StagedConfig` through `blend_vectors` 90–161; `_observe`/`observe_staged` 189–199; `advance_ema` 240–250; constructor-zero distinction 268–297 |
| RUN | [_runner.py][RUN], `_step` 13–18; `_observe` 38–44; `_advance` 47–52; `_append` 83–96; `run` initial sample 147–153 |
| PRE | [_presets.py][PRE], `historical_observer`, lines 18–36, staged literals, independent clock and recomputed initialization |
| ZD | [z_diagnostics.py][ZD], `chiral_area_accounting` 166–182; `intensity_budget` 256–288 |
| TD | [test_dynamics.py][TD], `DynamicsTests.test_one_step_against_hand_calculated_pre_sync_state` 13–23; simultaneous update, zero convention and qualified phase-covariance examples; read only |
| WO | [Current work order][WO], scope, supplied reference configuration and required exact continuation of R2’s state |

[R2]: C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md
[R1]: C:/Users/Notandi/.codex/reports/Z_MACRO_MIDDLE_BAND_INTERSECTION_ANALYSIS_v0.1.md
[R0]: C:/Users/Notandi/.codex/reports/Z_AND_CENTRAL_TWISTED_HEX_CRYSTAL_GEOMETRIC_RELATIONSHIP_INVESTIGATION_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:27
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[RUN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py:83
[PRE]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18
[ZD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py:256
[TD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_dynamics.py:13
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_FULL_Z_ONE_NATIVE_STEP_v0.1.md
