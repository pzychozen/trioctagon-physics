# NATIVE_PROJECTION_CAPACITY_01 — projection invariant and joint capacity ceiling

**Verdict: Established.**  
**Date:** 4 November 2026. **Research author:** Hilmir Frímann Halldórsson (pzychozen).  
**Status:** Completed bounded Codex investigation, submitted for GPT review.

The proposed projection invariant, exact debit account, joint floor, feasibility condition, algebraic minimum, zero-ceiling equivalence and active coherent-launch witness all hold with the proposed hypotheses and formulas unchanged. The structural statements require any fixed finite positive receiver coupling, with no large-coupling condition. The algebraic minimum is not a trajectory saturation theorem.

The [claim/source ledger](NATIVE_PROJECTION_CAPACITY_01_CLAIM_SOURCE_LEDGER.md) maps PC01–PC22 below to exact published source labels and separates inherited premises from the new deductions. [SOURCE_IDENTITIES.json](SOURCE_IDENTITIES.json) identifies the focused source bytes. P1 denotes *A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model*, v0.1, commit 273b1a6faaab19ea58748d00576439166eeef9ab. P2 denotes *Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate*, v0.1, commit 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9.

The author-approved [standalone work order](NATIVE_PROJECTION_CAPACITY_01_CODEX_WORK_ORDER.md) governs this investigation. Its formulas and the accompanying assessment were proposals requiring independent verification. The prior accessible-transfer investigation is accepted unchanged, as recorded in its preserved GPT review; that acceptance did not previously include the present projection-invariant lead.

## 1. Exact hypotheses and inherited solution class

Fix the published finite carrier geometry, normalized disjoint H¹ tents, periodic carrier length L_c>0 and positive speed c. The whole-circle shortest-separation condition and positive finite profile width remain as published. Let B map the two real port coordinates into the distributed profiles and let B* be its L² adjoint. In particular B*B=m Id₂ with m=2/(3ε_c)>0 and ‖B*‖=√m. No new spatial profile, point trace or registration is introduced.

Fix α_N, β_R, η_N>0, any finite constant κ=η_R>0, positive fixed registration gains and a fixed yaw δ_g. Write x=(a,b) in R⁶, Ω=a+ib, and retain the raw two-port order:

\[
\begin{gathered}
n_\pm=(2e_y\pm\sqrt3e_z)/\sqrt7,\qquad
K=\kappa_{\rm in}
\begin{pmatrix}n_+^T\\ n_-^T\end{pmatrix}\lambda_gR_z(\delta_g),
\qquad G=\kappa_{\rm in}\lambda_g>0,\\
f(x)=K(a\times b),\qquad J(x)=D_xf(x),\qquad
y=\mathcal B^*p,\quad w=K^Ty,\quad \mu=\eta_N/(2\alpha_N),\\
\dot a=\mu\,w\times b,\qquad
\dot b=-\mu\,w\times a,\qquad
\dot\Omega=-i\mu\,w\times\Omega .
\tag{PC01}
\end{gathered}
\]

The carrier and receiver equations and trial stores remain

\[
\begin{gathered}
p_t+c(r_c)_s=\mathcal B\{\eta_N f(x)-\kappa z\},\qquad
(r_c)_t+cp_s=0,\qquad
\dot z=(\kappa/\beta_R)y,\\
H_N=\alpha_N|\Omega|^2/2,\quad
H_C=(\|p\|_2^2+\|r_c\|_2^2)/2,\quad H_R=\beta_R|z|^2/2,\\
P_{NC}=\eta_N f(x)^Ty,\quad P_{CR}=\kappa z^Ty,\qquad
\dot H_N=-P_{NC},\quad
\dot H_C=P_{NC}-P_{CR},\quad
\dot H_R=P_{CR}.
\tag{PC02}
\end{gathered}
\]

All powers are full signed two-port sums. These are the published exchange equations, without native F jumps, coefficient switches or added feedback. H_N is a positive quadratic trial storage, distinct from the native quartic potential.

P1 Theorem 3.1 supplies a unique global mild solution in R⁶×L²_per²×R² for every admitted initial state, with C¹ native and receiver coordinates and continuous carrier coordinates in L². Because B* is bounded, y and w are continuous. Conservation and the positive storage weights bound the carrier L² norm and hence y throughout exchange. All differentiations below act on finite-dimensional C¹ native variables; no spatial derivative of an L² preparation is taken. The global integrated balances hold for this class. A new PDE theorem or H¹ preparation restriction is unnecessary for the invariant and floor.

Initial external states may be arbitrary in this class for the invariant, floor and signed-debit bound. We explicitly impose p₀=r_c,₀=z₀=0 only for the nonnegative external-stock and launch-activity conclusions.

## 2. Kernel direction and the new invariant

The published rotation convention is

\[
R_z(\delta)=
\begin{pmatrix}\cos\delta&-\sin\delta&0\\
\sin\delta&\cos\delta&0\\0&0&1\end{pmatrix},\qquad
K=\frac G{\sqrt7}
\begin{pmatrix}
2\sin\delta_g&2\cos\delta_g&\sqrt3\\
2\sin\delta_g&2\cos\delta_g&-\sqrt3
\end{pmatrix}.
\tag{PC03}
\]

Both row combinations are nonzero and independent: their sum points along (sinδ_g,cosδ_g,0), and their difference along e_z. Thus K is real of rank two. Equivalently det(KKᵀ)=48G⁴/49>0. The unit kernel vector is exactly

\[
e=R_z(-\delta_g)e_x=(\cos\delta_g,-\sin\delta_g,0),\qquad
Ke=0,\qquad \ker K=\mathbb R e,\qquad
e\cdot w=(Ke)^Ty=0 .
\tag{PC04}
\]

This uses the raw projection convention, without inserting contact-tangent signs. The result fixes a mathematical kernel direction; it does not identify a physical field axis, support or receiver location.

Define

\[
I=|\Omega|^2=|a|^2+|b|^2,\qquad
h_e=|e\cdot\Omega|^2=(e\cdot a)^2+(e\cdot b)^2,\qquad
\mathcal J_K=I-2h_e
=\Omega^\dagger(\mathrm{Id}-2ee^T)\Omega .
\tag{PC05}
\]

The real scalar J_K is not the Jacobian J(x); it may be negative. The direction e is not P1's carrier energy density, which used the same letter locally. Replacing e by −e leaves h_e and eeᵀ, hence J_K and every ceiling below, unchanged.

The scalar-triple-product signs from PC01 are

\[
\dot I
=2\mu\{a\cdot(w\times b)-b\cdot(w\times a)\}
=-4\mu\,w\cdot(a\times b).
\tag{PC06}
\]

For h_e, choose a right-handed real orthonormal basis whose third vector is e. Cross products retain their usual coordinate formula in such a basis. Write w=(w₁,w₂,0), a=(a₁,a₂,a₃), b=(b₁,b₂,b₃). Then

\[
\begin{aligned}
\dot h_e
&=2\mu\{a_3(w_1b_2-w_2b_1)-b_3(w_1a_2-w_2a_1)\}\\
&=-2\mu\{w_1(a_2b_3-a_3b_2)+w_2(a_3b_1-a_1b_3)\}\\
&=-2\mu\,w\cdot(a\times b),\qquad
\dot{\mathcal J}_K=\dot I-2\dot h_e=0 .
\end{aligned}\tag{PC07}
\]

This proof uses only the fixed rank-two kernel relation and the native equation. It is valid at native zero and at zero chirality, without division by either. The orthonormal basis is a proof device, not a change to the registered model.

Since I(t)=j₀+2h_e(t), where j₀=J_K(Ω₀), the exact debit identity is

\[
H_N(0)-H_N(t)=\alpha_N\{h_e(0)-h_e(t)\}.
\tag{PC08}
\]

Its derivative is also consistent with the existing power: α_N dot h_e=−η_N w·(a×b)=−P_NC. Thus PC08 expresses the same native debit through a fixed projection; it adds no storage and no new physical energy law.

## 3. Joint all-time floor and correct stock interpretation

Retain P1 Theorem 5.1:

\[
Z_2(\Omega)=\Omega^T\Omega
=|a|^2-|b|^2+2i\,a\cdot b,\qquad
Z_2(\Omega(t))=Z_0,\qquad
I^2-|Z_2|^2=4|a\times b|^2,\qquad I\ge|Z_2|.
\tag{PC09}
\]

The transpose here is complex bilinear, not conjugate transpose. From PC05 and PC07, I(t)=j₀+2h_e(t)≥j₀. Combining the two independent bounds gives, at every real exchange time,

\[
I(t)\ge\max\{|Z_0|,j_0\},\qquad
H_N(0)-H_N(t)\le
C_{\rm joint}:=\frac{\alpha_N}{2}\{I_0-\max(|Z_0|,j_0)\}
=\min\left\{C_Z,\alpha_Nh_e(0)\right\},
\quad
C_Z=\frac{\alpha_N}{2}(I_0-|Z_0|).
\tag{PC10}
\]

Both terms in the minimum are nonnegative: I₀≥|Z₀| and h_e(0)≥0. Hence C_joint≥0, including native zero. There is no division by initial intensity. This also proves that the joint bound never weakens the old one, although equality between the two ceilings can occur.

For empty external preparation, conservation gives the requested all-future-time bound

\[
0\le H_C(t)+H_R(t)=H_N(0)-H_N(t)\le C_{\rm joint}
\qquad(t\ge0).
\tag{PC11}
\]

For arbitrary preloaded external states the exact relation instead is

\[
H_N(0)-H_N(t)
=[H_C(t)+H_R(t)]-[H_C(0)+H_R(0)]\le C_{\rm joint}.
\tag{PC12}
\]

The signed native debit can be negative. The joint ceiling bounds the increase over pre-existing external stock, not that entire stock. In particular, zero joint ceiling does not imply that a preloaded solution is stationary.

## 4. Feasibility and sharp algebraic minimum

Fix any complex Z and real j. The minimization in this section ranges over the full native space C³, with e fixed. It does not impose the coherent launch family, carrier constraints or trajectory reachability.

Write Ω=h e+v_perp with h=eᵀΩ in C and eᵀv_perp=0. Real orthogonal projection gives

\[
Z_2=h^2+v_\perp^Tv_\perp,\qquad
\mathcal J_K=\|v_\perp\|^2-|h|^2,\qquad
I=|h|^2+\|v_\perp\|^2 .
\tag{PC13}
\]

Here ‖v_perp‖²=v_perp†v_perp≥0, whereas v_perpᵀv_perp is complex and can vanish for nonzero v_perp. In an orthonormal real basis of e-perp, the triangle inequality gives |v_perpᵀv_perp|≤‖v_perp‖². If Z₂=Z and J_K=j, the reverse triangle inequality yields

\[
|Z|=|h^2+v_\perp^Tv_\perp|
\ge |h|^2-|v_\perp^Tv_\perp|
\ge |h|^2-\|v_\perp\|^2=-j.
\tag{PC14}
\]

Therefore j≥−|Z| is necessary, even when the rightmost quantity is negative. Every feasible state also obeys I≥|Z| and I≥j by PC09 and PC13.

To prove sufficiency and attainment of that lower bound, put ρ=|Z|. Select real orthonormal vectors u,v spanning e-perp. If ρ>0, choose a unit complex number γ with γ²ρ=Z; such a square root of Z/ρ exists. If ρ=0, set γ=1. Multiplication by γ preserves I and J_K and multiplies Z₂ by γ².

For −ρ≤j≤ρ, set

\[
\Omega_*=\gamma\left[
\sqrt{\frac{\rho+j}{2}}\,u+
\sqrt{\frac{\rho-j}{2}}\,e\right].
\quad
I_*=\rho,\quad Z_2(\Omega_*)=\gamma^2\rho=Z,\quad
\mathcal J_K(\Omega_*)=
\frac{\rho+j}{2}-\frac{\rho-j}{2}=j .
\tag{PC15}
\]

Both square roots are real and nonnegative on this interval. Real orthogonality eliminates cross terms. This attains I*=max(ρ,j)=ρ, including all feasible negative j.

For j≥ρ, use

\[
\Omega_*=\gamma\left[
\sqrt{\frac{j+\rho}{2}}\,u+
i\sqrt{\frac{j-\rho}{2}}\,v\right].
\quad
I_*=j,\quad
Z_2(\Omega_*)=\gamma^2\left[\frac{j+\rho}{2}-\frac{j-\rho}{2}\right]=Z,\quad
\mathcal J_K(\Omega_*)=j .
\tag{PC16}
\]

The factor i contributes a minus sign in the bilinear square but a plus sign in the Hermitian norm. There is no e component, so J_K=I. This attains the other branch of the lower bound. The result is consequently

\[
\{\Omega:Z_2(\Omega)=Z,\ \mathcal J_K(\Omega)=j\}\ne\varnothing
\ \Longleftrightarrow\ j\ge-|Z|,\qquad
\min_{\substack{Z_2(\Omega)=Z\\\mathcal J_K(\Omega)=j}}|\Omega|^2
=\max(|Z|,j)
\quad(j\ge-|Z|).
\tag{PC17}
\]

For j<−|Z| the constraint set is empty, so no minimum is asserted. Explicit construction, not compactness of an unbounded level set, proves attainment in every feasible case.

All boundary cases are covered without division by ρ:

| Case | Equality state and conclusion |
| --- | --- |
| ρ>0, j=−ρ | γ√ρ e; I*=ρ and J_K=−ρ |
| ρ>0, −ρ<j<0 | PC15; negative J_K is permitted |
| ρ>0, j=ρ | Both constructions give γ√ρ u |
| Z=0, j<0 | Infeasible by PC14 |
| Z=0, j=0 | Minimum zero, attained only by the native zero vector |
| Z=0, j>0 | √(j/2)(u+i v); Z₂=0 and I*=J_K=j |
| Native zero | Z₂=J_K=I=h_e=C_joint=0; all preceding formulas are defined |

The Z=j=0 level contains nonzero states as well; only its minimizing state must be zero. A construction at the minimum does not certify that any given coupled trajectory can reach it. The dynamical distinction is demonstrated in §7.

## 5. Zero joint ceiling is exactly zero drive

For any native initial state with the fixed real rank-two K,

\[
C_{\rm joint}(\Omega_0)=0
\quad\Longleftrightarrow\quad f(x_0)=0 .
\tag{PC18}
\]

Here is a proof in both directions. Since PC10 is the minimum of two nonnegative terms, C_joint=0 implies C_Z=0 or h_e=0.

If C_Z=0, then I=|Z₂|, and PC09 gives a×b=0; hence f=0. If h_e=0, the real quantities e·a and e·b both vanish. Both vectors lie in e-perp, so their cross product is parallel to e, possibly zero. K annihilates that direction and f=0.

Conversely, f=0 implies a×b∈ker K=R e. If a×b=0, PC09 and the nonnegativity of I and |Z₂| give I=|Z₂| and C_Z=0. If a×b=λe with λ≠0, its perpendicularity to both a and b gives e·a=e·b=0. Thus h_e=0. Either case makes C_joint=0. Native zero belongs to the first case; no division by intensity or chirality was made. The division by λ is used only in the explicitly nonzero branch.

For empty carrier and receiver, f(x₀)=0 makes the constant full state a solution. P1 uniqueness makes it the actual solution. For f(x₀)≠0 and the fixed positive couplings, P1 Proposition 4.1 gives initial positive supply; in particular,

\[
H_N(0)-H_N(t)
=\frac{\eta_N^2m}{2}|f(x_0)|^2t^2+o(t^2)>0
\quad\text{for all sufficiently small }t>0 .
\tag{PC19}
\]

Thus a positive joint ceiling is consistent with and, for empty preparation, accompanied by actual initial supply. It does not imply saturation. For a nonzero zero-drive core with a preloaded carrier, J(x)ᵀy can be nonzero; stationarity is not a consequence of f(x)=0 at one instant. Native zero is special because both f(0) and J(0) vanish for every allowed external state.

## 6. A strict improvement for an admitted active coherent launch

Use exactly Ω₀=(1,exp(iφ),1), 0<φ<π/12, with empty external preparation. The state has ordinary phase span φ and unit native amplitudes, as in P1/P2. Direct evaluation with the verified kernel direction gives

\[
\begin{gathered}
I_0=3,\qquad Z_0=2+e^{2i\phi},\qquad
|Z_0|=\sqrt{9-8\sin^2\phi},\\
e\cdot\Omega_0=\cos\delta_g-\sin\delta_g\,e^{i\phi},\qquad
h_e(0)=1-\sin(2\delta_g)\cos\phi,\qquad
j_0=1+2\sin(2\delta_g)\cos\phi .
\tag{PC20}
\end{gathered}
\]

Select the single fixed admissible yaw δ_g=π/4 before the trajectory. Put C=cosφ, so 0<C<1. Then j₀=1+2C>0 and |Z₀|>0, and

\[
\begin{gathered}
j_0^2-|Z_0|^2=4C(1-C)>0,\qquad j_0>|Z_0|,\\
0<C_{\rm joint}=\alpha_N(1-\cos\phi)
<C_Z=\frac{\alpha_N}{2}\left(3-\sqrt{9-8\sin^2\phi}\right),\\
C_Z-C_{\rm joint}
=\frac{\alpha_N}{2}(j_0-|Z_0|)>0,\qquad
|f_0|^2=\frac{10G^2\sin^2\phi}{7}>0 .
\tag{PC21}
\end{gathered}
\]

The comparison of squares implies the strict comparison itself because both sides are positive. Also φ>0 ensures 1−cosφ>0. The drive formula follows by evaluating P2's exact registered launch drive at sin²δ_g=1/2; no altered drive or port sign is used.

For this active launch, PC11 and PC21 prove that the old ceiling C_Z cannot be reached at any exchange time: the fixed positive gap C_Z−C_joint separates it from every possible net debit. This is a strict improvement for one admitted non-dark launch, not a claim that all yaws improve the ceiling or that C_joint is attained. The yaw is an analytical witness, not a switched parameter, optimization or preferred physical orientation.

This result is compatible with accepted AT01. Its sufficiently large finite κ solutions are a subset of the present any-finite-positive-κ scope. For this fixed yaw and phase, C_joint is positive and independent of κ, while AT01's first-window maximum transferred stock tends to zero with a positive inverse-square leading scale. That small transfer can respect the stronger ceiling and still have AT01's high receiver-share and net-recovery fractions, whose denominators remain the actual intermediate stock. No κcert condition enters the invariant or the all-time ceiling.

## 7. Checked boundary between algebraic sharpness and dynamics

Take a real unit vector u perpendicular to e, and let Ω₀=u+i e. This example lies outside the restricted coherent launch family. It is an admitted native state for P1's global theorem and may, in particular, be paired with empty external preparation. Direct calculation gives

\[
I_0=2,\qquad Z_0=1-1+2i\,u\cdot e=0,\qquad
h_e(0)=1,\qquad j_0=0,\qquad
a_0\times b_0=u\times e\ne0,\qquad f(x_0)\ne0 .
\tag{PC22}
\]

Indeed u×e is a unit vector perpendicular to e. Since ker K=R e, K cannot annihilate this vector. The common native invariant level Z=j=0 contains Ω*=0, and PC17 gives its algebraic minimum I*=0. Here C_joint=C_Z=α_N.

Nevertheless a nonzero native state cannot reach native zero at a finite exchange time. Suppose Ω(t*)=0 at finite t*. At that time retain the actual carrier and receiver coordinates, which need not vanish. The invariant native-zero subspace admits an evolution with native coordinate identically zero: f(0)=J(0)=0, while the remaining carrier/receiver subsystem continues to evolve. The global forward/backward solution theorem and uniqueness through this same full state identify the original solution with that native-zero solution in both time directions. This would force Ω(0)=0, a contradiction.

Equivalently, along the original solution w(t) is continuous, and the native equation is a homogeneous linear ODE in Ω with that fixed continuous time-dependent coefficient. The zero solution and any solution that is zero at t* agree by finite-time uniqueness in both directions. This argument does not assume that the external subsystem is zero and does not merely appeal to equality of invariant values.

Thus the algebraic minimum is unattainable at any finite time from this particular nonzero native preparation, although it belongs to the common invariant level. No conclusion about infinite-time approach follows. The example is not a counterexample to any accepted coherent-launch theorem.

## 8. Units, scope and scientific disposition

With P1's native amplitude unit A, the quantities I, h_e, J_K, Z₂ and |Z₂| all have dimension A²; e and the reflection matrix are dimensionless. Since α_N has dimension U²L/A², both terms of C_joint and both sides of PC08 have storage dimension U²L. The kernel direction and indefinite invariant introduce no new physical unit or constitutive storage. The bookkeeping units are not a physical calibration.

The structural theorem holds for the unchanged fixed real rank-two candidate, arbitrary admitted native and external preparations for signed debit, and every exchange time. Empty external preparation is required for PC11 and the launch conclusions. No native stepping, new port or receiving law, control/orbit classification, trajectory computation, parameter scan, full yaw classification, coupling optimization or infinite-time saturation theorem is supplied.

The invariant-level lemma is sharp in the full native space under exactly two constraints; it makes no claim that these exhaust all dynamical restrictions. The nonzero example in §7 shows why that distinction matters. The new result provides a stronger necessary capacity limit, while useful accessible amounts and actual saturation remain open.

The author's central starting/meeting region, opposed cones, outward spreading and around–inward return, stationary supports and possible transfer elsewhere remain the intended programme. The carrier circle, intended tight toroid, close original sphere and extended-line sphere remain distinct. No physical support, opening, field axis or receiver location is identified with e. The tentative 15–20%, possibly more, remains geometric intuition, not a fitted target.

Later directions remain useful accessible capacity beyond necessary ceilings, native stepping/cadence, intended route correspondence, six-opening transport, linked gravity–magnetism, outer geometry and justified SRG integration. No successor investigation was performed.

**Correction audit:** no proposed sign, factor, constant, feasibility condition, construction or hypothesis required correction. In particular, negative j and native zero are included; the preloaded-state account remains signed; no large-coupling restriction was added.

**Evidence and review:** the standalone symbolic checker verifies selected derivative identities, constructions and witness coefficients. The written arguments above establish feasibility in both directions, the minimum, the zero-drive equivalence and the dynamical boundary. Check counts and execution details are recorded separately and do not include historical suites or document checks. Hilmir supplies authorship and direction; GPT supplied the bounded proposal; Codex derived and checked this result. The accepted AT01 artifacts remain unchanged. GPT review of this new investigation is pending; no external peer review or physical validation is claimed.
