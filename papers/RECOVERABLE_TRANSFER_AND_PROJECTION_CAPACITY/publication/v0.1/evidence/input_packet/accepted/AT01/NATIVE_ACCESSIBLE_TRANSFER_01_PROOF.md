# NATIVE_ACCESSIBLE_TRANSFER_01 — finite-window transfer certificate

**Verdict: Established.**  
**Date:** 4 November 2026. **Research author:** Hilmir Frímann Halldórsson (pzychozen).  
**Disposition:** Independent Codex analytical investigation of GPT's proposal; submitted for GPT review. This is an investigation report, not a manuscript or publication.

Every proposed bound in work-order §§5.1–5.4 follows with the proposed constants and hypotheses unchanged. The new conclusions concern the actual finite-coupling solution: a positive transferred stock, its temporary concentration in the receiver, subsequent net recovery, and exact receiver charging and backflow. They do not follow merely from the comparison oscillator. The norm estimate, weighted projections, positive denominators and separate receiver-product estimate below supply the necessary transfers.

P1 denotes the published reciprocal-exchange edition at commit 273b1a6faaab19ea58748d00576439166eeef9ab. P2 denotes the published same-trajectory native-credit edition at commit 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9. The [claim/source ledger](NATIVE_ACCESSIBLE_TRANSFER_01_CLAIM_SOURCE_LEDGER.md) maps the labels AT01–AT29 below to exact source labels and identifies inherited versus new deductions. [SOURCE_IDENTITIES.json](SOURCE_IDENTITIES.json) records exact source bytes. The external [work order](NATIVE_ACCESSIBLE_TRANSFER_01_CODEX_WORK_ORDER.md) governs this task; its new formulas were proposals to verify, not accepted premises.

## 1. Fixed hypotheses, equations and inherited facts

Fix the published admissible carrier and registration before choosing the receiver coupling. Write x=(a,b) in real six-dimensional space and Ω=a+ib. In the original two-port order,

\[
\begin{gathered}
u=(0,1,0),\quad e_z=(0,0,1),\quad
n_\pm=(2u\pm\sqrt3e_z)/\sqrt7,\quad A_{\rm reg}=\lambda_gR_z(\delta_g),\\
K=\kappa_{\rm in}\begin{pmatrix}n_+^T\\ n_-^T\end{pmatrix}A_{\rm reg},
\qquad f(x)=K(a\times b),\qquad J(x)=D_xf(x),\qquad
G=\kappa_{\rm in}\lambda_g>0 .
\tag{AT01}
\end{gathered}
\]

Both gains are fixed positive numbers and the yaw is fixed. These are raw chiral projections, without inserting contact-tangent orientation signs. On the fixed circle of length L_c>0, fix c>0, contacts s_±=L_c/2∓η_geom whose shortest periodic distance is 2η_geom, and 0<ε_c<η_geom. The published normalized tents and their operators satisfy

\[
\begin{gathered}
b_\sigma(s)=\epsilon_c^{-1}
\left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
\quad \mathcal Bv=b_+v_++b_-v_-,
\quad \mathcal B^*p=(\int b_+p,\int b_-p)^T,\\
m=\frac2{3\epsilon_c},\quad d=\frac2{\epsilon_c^3},\quad
\mathcal B^*\mathcal B=mI_2,\quad
\|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\quad
\|\mathcal B'v\|_2=\sqrt d\,|v|.
\tag{AT02}
\end{gathered}
\]

The shortest-distance condition ensures disjoint support on the whole circle, including across its coordinate seam. Each tent is continuous and H¹; its first weak derivative is piecewise constant in L², without corner delta terms. No second derivative is needed.

Fix α_N, β_R, η_N>0 and one 0<φ<π/12. For each selected finite constant κ=η_R>0 the unchanged equations and preparation are

\[
\begin{aligned}
\dot x&=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,
&p_t+c(r_c)_s&=\mathcal B\{\eta_N f(x)-\kappa z\},\\
(r_c)_t+cp_s&=0,
&\dot z&=\frac{\kappa}{\beta_R}y,\qquad y=\mathcal B^*p,\\
\Omega_0&=(1,e^{i\phi},1),
&p(0)&=r_c(0)=z(0)=0 .
\end{aligned}\tag{AT03}
\]

There are no native F jumps, resets or parameter switches. Varying κ compares different constant-parameter solutions. Membership of the initial coherent family or phase sector is not assumed to persist.

P1 Theorem 3.1 supplies a unique global solution; the empty carrier is H¹, so (p,r_c) belong to C(R;H¹_per)²∩C¹(R;L²)² and x,z are C¹. Thus all accounts used here are accounts of an existing strong solution. The inherited stores and full signed two-port powers are

\[
\begin{gathered}
H_N=\alpha_N|x|^2/2,\quad H_C=(\|p\|_2^2+\|r_c\|_2^2)/2,\quad
H_R=\beta_R|z|^2/2,\\
P_{NC}=\eta_N f(x)^Ty,\quad P_{CR}=\kappa z^Ty,\quad
\dot H_N=-P_{NC},\quad \dot H_C=P_{NC}-P_{CR},\quad \dot H_R=P_{CR},\\
E_{\rm out}(t):=H_C(t)+H_R(t)=H_N(0)-H_N(t)\ge0 .
\tag{AT04}
\end{gathered}
\]

H_N is the candidate's positive quadratic trial storage, distinct from the native quartic potential. Initial empty external stores and conservation give |x(t)|≤R=√3. The exact published launch drive and bounds are

\[
\begin{gathered}
k=\|K\|=G\sqrt{8/7},\quad F_{\max}=kR^2/2,\\
f_{0,\pm}=\frac{G\sin\phi}{\sqrt7}(-2\sin\delta_g\pm\sqrt3),\qquad
|f_0|^2=\frac{G^2\sin^2\phi}{7}(6+8\sin^2\delta_g)>0,\\
|f(x)|\le F_{\max},\quad \|J(x)\|\le kR,\quad
|f(x)-f(\widetilde x)|\le kR|x-\widetilde x|
\quad (|x|,|\widetilde x|\le R).
\tag{AT05}
\end{gathered}
\]

The ball is convex, so the last estimate follows from integrating J along its line segment, independently of phase-sector invariance. The drive vector is nonzero for every fixed yaw; a single component may vanish.

## 2. Exact scaling and extension of the error estimate

Use the finite change of variables

\[
\begin{gathered}
\tau=\kappa t,\quad x_\kappa(\tau)=x(\tau/\kappa),\quad
(p,r_c,z)(\tau/\kappa)=\frac{\eta_N}{\kappa}
(\widehat p,\widehat r,\widehat z)(\tau)=\frac{\eta_N}{\kappa}V_\kappa(\tau),
\quad\widehat y=\mathcal B^*\widehat p,\\
(x_\kappa)'=-\frac{\eta_N^2}{2\alpha_N\kappa^2}J(x_\kappa)^T\widehat y,\quad
\widehat p_\tau+(c/\kappa)\widehat r_s=\mathcal B(f(x_\kappa)-\widehat z),\\
\widehat r_\tau+(c/\kappa)\widehat p_s=0,\quad
\widehat z_\tau=\widehat y/\beta_R .
\tag{AT06}
\end{gathered}
\]

The original positive speed remains c. Because κ is dimensionless, τ has time units. For W=(q_c,h,v) define

\[
\begin{gathered}
\|W\|_{CR}^2=\|q_c\|_2^2+\|h\|_2^2+\beta_R|v|^2,\\
\mathcal L_\kappa W=
(-(c/\kappa)h_s-\mathcal Bv,\;-(c/\kappa)(q_c)_s,\;\beta_R^{-1}\mathcal B^*q_c),
\quad D(\mathcal L_\kappa)=H^1_{\rm per}{}^2\times\mathbb R^2,\\
\langle W,\mathcal L_\kappa W\rangle_{CR}
=-\frac c\kappa\int(q_ch_s+h(q_c)_s)
-\langle q_c,\mathcal Bv\rangle+v^T\mathcal B^*q_c=0,\\
W_\tau=\mathcal L_\kappa W+g
\quad\Longrightarrow\quad
\|W(\tau)\|_{CR}\le\|W(0)\|_{CR}+\int_0^\tau\|g(s)\|_{CR}\,ds .
\tag{AT07}
\end{gathered}
\]

Periodic integration eliminates the first term, and adjointness cancels the receiver terms. For a strong curve, differentiate √(‖W‖²_CR+δ²), with δ>0, to obtain a derivative at most ‖g‖_CR. Integrate and let δ decrease to zero. This proves the estimate even where W vanishes, without dividing by its norm. We apply it only to the known strong solution and its explicit strong comparison difference.

P2's all-finite-τ estimates can also be read directly from AT05–AT07. Apply AT07 to Vκ with g=(Bf(xκ),0,0), then integrate the native equation and apply the convex-ball Lipschitz bound. For every finite τ≥0,

\[
\begin{gathered}
\|V_\kappa(\tau)\|_{CR}\le\sqrt m F_{\max}\tau,\qquad
|\widehat y(\tau)|\le mF_{\max}\tau,\\
|x_\kappa(\tau)-x_0|
\le\frac{\eta_N^2kRmF_{\max}}{4\alpha_N\kappa^2}\tau^2,\qquad
|f(x_\kappa(\tau))-f_0|\le\frac{A\tau^2}{\kappa^2},\quad
A=\frac{\eta_N^2k^2R^2mF_{\max}}{4\alpha_N}.
\tag{AT08}
\end{gathered}
\]

The factor 1/4 is the product of the native feedback factor 1/2 and the integral of s. The bounds require neither a small-time expansion nor a restriction to P2's witness horizon.

Set the fixed, κ-independent constants

\[
\begin{gathered}
\omega=\sqrt{m/\beta_R},\quad S=2\pi/\omega,\quad
\Lambda=\sqrt{\beta_R}|f_0|>0,\quad D=(m/\omega)|f_0|^2=\omega\Lambda^2>0,\\
B_1=\frac{4c\sqrt d\,|f_0|}{\omega^2},\quad
B_2=\frac{\sqrt m\,AS^3}{3},\quad
\varepsilon_\kappa=\frac{B_1}{\kappa}+\frac{B_2}{\kappa^2}.
\tag{AT09}
\end{gathered}
\]

The published frozen-core, omitted-scaled-propagation comparison is

\[
\widehat p^{(0)}=\frac{\sin(\omega\tau)}{\omega}\mathcal Bf_0,\quad
\widehat r^{(0)}=0,\quad
\widehat z^{(0)}=f_0(1-\cos(\omega\tau)),\quad
\widehat y^{(0)}=\frac m\omega f_0\sin(\omega\tau).
\tag{AT10}
\]

It solves its comparison equations because ω²=m/β_R. It does not replace the actual positive-speed system. The comparison carrier is C¹ in τ with values in H¹. The scaled exact solution retains the strong regularity stated after AT03. Their difference Eκ=Vκ−V0 therefore already has carrier regularity CτH¹_s∩C¹_τL²_s and a C¹ receiver coordinate. Subtracting the equations gives

\[
(E_\kappa)_\tau=\mathcal L_\kappa E_\kappa
+(\mathcal B(f(x_\kappa)-f_0),0,0)
+\left(0,-\frac c{\kappa\omega}\mathcal B'f_0\sin(\omega\tau),0\right),
\qquad E_\kappa(0)=0 .
\tag{AT11}
\]

The residual is negative in the second carrier coordinate. Its first coordinate is zero because the comparison's second carrier coordinate is zero. The residual uses only B'f0 in L². It need not be H¹; the strong regularity of Eκ was obtained by subtraction before using the residual estimate. No second tent derivative, discretization or operator-norm limit of an unbounded generator is asserted.

Apply AT07 to AT11 and use AT08. For 0≤τ≤S,

\[
\begin{aligned}
\|E_\kappa(\tau)\|_{CR}
&\le\frac{c\sqrt d\,|f_0|}{\kappa\omega}
\int_0^\tau|\sin(\omega s)|\,ds
+\frac{\sqrt m\,A}{\kappa^2}\int_0^\tau s^2\,ds\\
&\le\frac{4c\sqrt d\,|f_0|}{\kappa\omega^2}
+\frac{\sqrt m\,AS^3}{3\kappa^2}
=\varepsilon_\kappa,\qquad
\sup_{0\le\tau\le S}\|E_\kappa(\tau)\|_{CR}\le\varepsilon_\kappa .
\end{aligned}\tag{AT12}
\]

The absolute sine integral equals 2/ω on each half of [0,2π/ω], hence 4/ω altogether. Both integrals on the first line are nondecreasing in τ. The global strong solution and all-finite-τ drift estimate justify the longer horizon; this is a fresh estimate on [0,S], not a substitution into a theorem proved only on [0,T].

## 3. Actual stock, receiver projections and normalized recovery

Introduce the positive scale aκ=η_N²/(2κ²), and the ordered physical landmarks

\[
t_{\rm q}=\frac{\pi}{2\omega\kappa}
<t_\pi=\frac{\pi}{\omega\kappa}
<t_{\rm b}=\frac{3\pi}{2\omega\kappa}
<t_{2\pi}=\frac{2\pi}{\omega\kappa}=\frac S\kappa,
\qquad
E_{\rm out}(\tau/\kappa)=a_\kappa\|V_\kappa(\tau)\|_{CR}^2 .
\tag{AT13}
\]

All times are strictly positive. Continuity of the stores on [0,t2π] ensures that Mκ=max Eout over this compact interval exists. No maximizing time is identified.

By B*B=mI and m/ω²=β_R,

\[
\|V_0(\tau)\|_{CR}^2
=\beta_R|f_0|^2\{\sin^2(\omega\tau)+(1-\cos(\omega\tau))^2\}
=4\Lambda^2\sin^2(\omega\tau/2).
\tag{AT14}
\]

Thus ‖V0‖_CR≤2Λ throughout the window, with V0(π/ω)=(0,0,2f0) of norm 2Λ and V0(S)=0. Triangle and reverse triangle inequalities give, when εκ<2Λ,

\[
0<a_\kappa(2\Lambda-\varepsilon_\kappa)^2
\le E_{\rm out}(t_\pi)\le M_\kappa
\le a_\kappa(2\Lambda+\varepsilon_\kappa)^2,\qquad
E_{\rm out}(t_{2\pi})\le a_\kappa\varepsilon_\kappa^2 .
\tag{AT15}
\]

For the intermediate-time projections, let Π_C take the two carrier coordinates and Π_R take the receiver coordinate. Their norms are respectively the ordinary carrier L² pair norm and √β_R times the receiver Euclidean norm; each projection is contractive relative to ‖·‖_CR. At π/ω, Π_CV0=0 and ‖Π_RV0‖=2Λ. Consequently,

\[
H_C(t_\pi)\le a_\kappa\varepsilon_\kappa^2,\qquad
H_R(t_\pi)\ge a_\kappa(2\Lambda-\varepsilon_\kappa)^2>0
\quad(\varepsilon_\kappa<2\Lambda).
\tag{AT16}
\]

The small carrier bound uses a carrier zero at π/ω. The endpoint bound uses the whole-state zero at S. Receiver positivity follows directly from its weighted projection, not from total-stock positivity alone.

Now both requested denominators are known positive. Define

\[
\mathcal S_\kappa=\frac{H_R(t_\pi)}{E_{\rm out}(t_\pi)},\quad
\mathcal R_\kappa=\frac{H_N(t_{2\pi})-H_N(t_\pi)}{E_{\rm out}(t_\pi)}
=1-\frac{E_{\rm out}(t_{2\pi})}{E_{\rm out}(t_\pi)},\quad
r_\kappa=\left(\frac{\varepsilon_\kappa}{2\Lambda-\varepsilon_\kappa}\right)^2.
\tag{AT17}
\]

The second equality is conservation AT04, not a monotonicity assumption. Since 1−Sκ=HC(tπ)/Eout(tπ), division of AT15–AT16 gives

\[
1-r_\kappa\le\mathcal S_\kappa\le1,\qquad
1-r_\kappa\le\mathcal R_\kappa\le1,\qquad
0\le\frac{H_R(t_{2\pi})}{H_R(t_\pi)}\le r_\kappa .
\tag{AT18}
\]

These inequalities hold for εκ<2Λ; the common lower bound is strictly positive for εκ<Λ. For the receiver-retention inequality use HR(t2π)≤Eout(t2π) and the independent positive receiver lower bound AT16. Further,

\[
\begin{aligned}
H_N(t_{2\pi})-H_N(t_\pi)
&=E_{\rm out}(t_\pi)-E_{\rm out}(t_{2\pi})\\
&\ge a_\kappa\{(2\Lambda-\varepsilon_\kappa)^2-\varepsilon_\kappa^2\}
=\frac{2\eta_N^2}{\kappa^2}\Lambda(\Lambda-\varepsilon_\kappa)>0
\quad(\varepsilon_\kappa<\Lambda).
\end{aligned}\tag{AT19}
\]

The increment is at most Eout(tπ)≤Mκ. These are net recovery and remaining receiver storage between specified times. They neither follow a tagged energy cohort nor use gross cumulative positive work as the denominator. Native storage need not increase monotonically throughout [tπ,t2π].

## 4. Separate finite receiver-power estimate and joint threshold

At τq=π/(2ω) and τb=3π/(2ω), the comparison receiver is f0 and its output is respectively +(m/ω)f0 and −(m/ω)f0. Write δz=ẑ−ẑ0 and δy=ŷ−ŷ0. The error bound gives |δz|≤εκ/√β_R and |δy|≤√m εκ. At either landmark the full product decomposition is

\[
\widehat z^T\widehat y-(\widehat z^{(0)})^T\widehat y^{(0)}
=(\widehat z^{(0)})^T\delta y
+\delta z^T\widehat y^{(0)}+\delta z^T\delta y .
\tag{AT20}
\]

The three absolute bounds are √m|f0|εκ, (m/(ω√β_R))|f0|εκ=√m|f0|εκ, and √(m/β_R)εκ²=ωεκ². Therefore, with Q_R=ẑᵀŷ,

\[
\begin{gathered}
|Q_R(\tau_{\rm b})+D|\le\omega(2\Lambda\varepsilon_\kappa+\varepsilon_\kappa^2),\qquad
|Q_R(\tau_{\rm q})-D|\le\omega(2\Lambda\varepsilon_\kappa+\varepsilon_\kappa^2),\\
P_{CR}(\tau/\kappa)=\frac{\eta_N^2}{\kappa}Q_R(\tau).
\tag{AT21}
\end{gathered}
\]

The power conversion has one factor κ from its definition and two factors η_N/κ from z and y. Both vector errors and their product are retained. P2's native-credit result alone does not prove these receiver signs.

For completeness, retain P2's unchanged sufficient native-credit constants

\[
T=\frac{3\pi}{2\omega},\quad
C_1=\frac{3c\sqrt{md}\,|f_0|^2}{\omega^2},\quad
C_2=mAT^3(F_{\max}+|f_0|/3),\quad
\kappa_{\rm crit}=\max\{1,4C_1/D,\sqrt{4C_2/D}\}.
\tag{AT22}
\]

Fix an analytical tolerance 0<q≤1/5 and choose any finite

\[
\kappa\ge\kappa_{\rm cert}(q)
:=\max\left\{\kappa_{\rm crit},1,\frac{2B_1}{q\Lambda},
\sqrt{\frac{2B_2}{q\Lambda}}\right\}.
\tag{AT23}
\]

All constants are finite and independent of κ; Λ and D are strictly positive. The two new threshold terms imply B1/κ≤qΛ/2 and B2/κ²≤qΛ/2 separately. Thus εκ≤qΛ<Λ. Since r↦r/(2−r) is increasing on [0,1), and 2q+q²≤11/25<1/2, AT18 and AT21 imply

\[
\begin{gathered}
\mathcal S_\kappa,\mathcal R_\kappa
\ge1-\left(\frac q{2-q}\right)^2\ge\frac{80}{81}>0,\qquad
\frac{H_R(t_{2\pi})}{H_R(t_\pi)}
\le\left(\frac q{2-q}\right)^2\le\frac1{81},\\
P_{CR}(t_{\rm q})\ge\frac{\eta_N^2D}{2\kappa}>0,\qquad
P_{CR}(t_{\rm b})\le-\frac{\eta_N^2D}{2\kappa}<0,\qquad
P_{NC}(t_{\rm b})\le-\frac{\eta_N^2D}{2\kappa}<0 .
\tag{AT24}
\end{gathered}
\]

For the receiver signs, the sharper factor 1−(2q+q²) is at least 14/25 and hence at least 1/2. The last native inequality is imported directly from P2's theorem using κ≥κcrit and T/κ=tb; no new proof of that accepted theorem is being claimed. The fractions 80/81 and 1/81 illustrate q=1/5 and are analytic guarantees in this sufficient regime, not fitted percentages or physical diversion coefficients.

For each of these same finite constant-κ solutions, P1 Proposition 4.1 gives PNC(t)>0, HR(t)>0 and PCR(t)>0 for all sufficiently small positive t, since η_N,κ>0 and f0≠0. Its interval may be shortened into (0,tq/2). This fixed-κ fact is used only for initial activity; the witness at tq comes from AT21–AT24, without substituting a κ-dependent time into nonuniform short-time expansions.

The actual receiver power is continuous because z is continuous and y=B*p is continuous by boundedness of B* on L². The new strict margin at tb therefore supplies a radius ρκ>0 which can be chosen less than π/(4ωκ), with

\[
P_{CR}(t)\le-\frac{\eta_N^2D}{4\kappa}
\quad\hbox{for }t\in[t_{\rm b}-\rho_\kappa,t_{\rm b}+\rho_\kappa]
\subset(t_\pi,t_{2\pi}).
\tag{AT25}
\]

If a common interval of native credit and receiver backflow is wanted, continuity of PNC and its AT24 margin allow this radius to be further shortened so both powers satisfy the same negative margin. In particular, integrating HR'=PCR shows a strict receiver-storage decrease on that interval. Its width is supplied by continuity, without a claimed uniform or explicit positive lower bound. Global uniqueness places the initial supply, exact charging witness, intermediate stock, late backflow and endpoint recovery on one unchanged solution.

## 5. Invariant ceiling, explicit finite errors and limits

P1 Theorem 5.1 preserves Z2=ΣΩ_i² and gives HN(t)≥α_N|Z2(Ω0)|/2. Here Z2(Ω0)=2+exp(2iφ) and |Z2|²=9−8sin²φ. Since 0<φ<π/12, 0<|Z2|<3, and the fixed ceiling is strictly positive:

\[
\begin{gathered}
C_{\rm inv}=\frac{\alpha_N}{2}(3-\sqrt{9-8\sin^2\phi})>0,\quad
0\le E_{\rm out}(t)\le C_{\rm inv}\quad(t\ge0),\\
\mathcal A_\kappa:=\frac{M_\kappa}{C_{\rm inv}},\qquad
\frac{a_\kappa(2\Lambda-\varepsilon_\kappa)^2}{C_{\rm inv}}
\le\mathcal A_\kappa
\le\min\left\{1,\frac{a_\kappa(2\Lambda+\varepsilon_\kappa)^2}{C_{\rm inv}}\right\}
\quad(\varepsilon_\kappa<2\Lambda).
\tag{AT26}
\end{gathered}
\]

This denominator is a published upper ceiling, not an established attainable maximum. Its positive value is held fixed in the limits below. There is no assertion uniform as φ decreases to zero.

Finite error bounds precede all asymptotic conclusions. Under AT23, put L=B1+B2, so εκ≤L/κ for κ≥1. The sandwich AT15, including its lower bound at tπ without identifying a maximizer, yields

\[
\begin{gathered}
\left|M_\kappa-\frac{2\eta_N^2\Lambda^2}{\kappa^2}\right|
\le\frac{\eta_N^2}{2\kappa^2}(4\Lambda\varepsilon_\kappa+\varepsilon_\kappa^2)
\le\frac{2\eta_N^2\Lambda L}{\kappa^3}
+\frac{\eta_N^2L^2}{2\kappa^4},\\
0\le E_{\rm out}(t_{2\pi})\le\frac{\eta_N^2L^2}{2\kappa^4},\\
0\le1-\mathcal S_\kappa,\ 1-\mathcal R_\kappa,\
\frac{H_R(t_{2\pi})}{H_R(t_\pi)}
\le\frac{L^2}{(2-q)^2\Lambda^2\kappa^2},\\
0<\mathcal A_\kappa\le
\min\left\{1,\frac{\eta_N^2(2+q)^2\Lambda^2}{2C_{\rm inv}\kappa^2}\right\}.
\tag{AT27}
\end{gathered}
\]

The third line uses 2Λ−εκ≥(2−q)Λ>0. All constants on the right are fixed. Therefore, as finite constant-coupling solutions are compared with κ tending to infinity,

\[
\begin{gathered}
M_\kappa=\frac{2\eta_N^2\beta_R|f_0|^2}{\kappa^2}+O(\kappa^{-3}),\qquad
E_{\rm out}(t_{2\pi})=O(\kappa^{-4}),\\
\mathcal S_\kappa,\mathcal R_\kappa\longrightarrow1,\qquad
1-\mathcal S_\kappa,\ 1-\mathcal R_\kappa=O(\kappa^{-2}),\qquad
\mathcal A_\kappa\longrightarrow0,\\
2\eta_N^2\beta_R|f_0|^2
=\frac{2\eta_N^2\beta_RG^2\sin^2\phi}{7}(6+8\sin^2\delta_g).
\tag{AT28}
\end{gathered}
\]

The leading stock coefficient is quadratic in the fixed native coupling and drive magnitude and linear in the receiver storage scale, with inverse-square receiver-coupling dependence. These statements keep all other parameters fixed; they are not a joint scaling or an optimization theorem. AT19 and AT24 show that a large fraction of the intermediate stock returns, while AT26–AT28 show that this window accesses a vanishing fraction of the invariant ceiling.

## 6. Dimensions, interpretation and review status

Retain P2's abstract units U,L,T and native amplitude unit A_amp. The drift constant A is distinct from A_amp and A_reg. The essential new dimensions are:

| Quantity | Dimension |
| --- | --- |
| m; d; c; ω; S | L⁻¹; L⁻³; L/T; T⁻¹; T |
| f0; A; β_R | UL/T; UL/T³; T²/L |
| Λ, B1, B2, εκ, external norm | UL^(1/2) |
| D, PCR, PNC | U²L/T |
| Mκ, Eout, Cinv, native recovery | U²L |
| q, κ, κcert, Sκ, Rκ, Aκ, retention ratio | 1 |

In particular B1/Λ and B2/Λ are dimensionless, and all threshold terms are commensurate. This is mathematical unit bookkeeping, not physical calibration.

The entire physical window shrinks relative to the fixed carrier circuit time:

\[
\frac{t_{2\pi}}{L_c/c}=\frac{cS}{\kappa L_c}\longrightarrow0 .
\tag{AT29}
\]

Both interactions occupy the same finite profiles. The result describes fast collocated reversible exchange. It establishes neither an exact nonlinear period nor a whole carrier circuit, long-time relaxation, permanent retention, disposal, arbitrary-coupling behavior or full-time capacity attainability. The point tπ is a prescribed comparison landmark, not a proved exact maximum. HN never exceeds its initial value by AT04, even during native credit. The separate projection-invariant lead in the assessment is preserved for subsequent capacity work and is neither proved nor used here.

The author's central starting/meeting region, opposed cones, outward spreading and curved around–inward return, stationary supports and possible transfer elsewhere remain the intended geometric programme. The one-dimensional carrier circle, intended tight toroid, close original enclosing sphere and extended-line sphere remain distinct. No six-opening assignment or new receiving location/law is introduced. The tentative 15–20%, possibly more, is intuition, not the denominator or a calibration target of this certificate.

The subsequent agenda remains accessible capacity beyond this window/regime, native stepping/cadence, intended route correspondence, six-opening transport, linked gravity–magnetism, later outer geometry and justified SRG integration. No successor investigation was performed.

**Correction audit:** no proposed constant, hypothesis, sign, normalization or bound required a correction. The proof explicitly supplies the horizon-extension argument, both weighted projections, positive denominators, all three receiver-product errors and the finite joint threshold. The standalone exact-algebra checker supports identified algebraic steps and allocations; it does not certify infinite-dimensional regularity, energy inequalities or continuity. Its actual execution count and scope are recorded separately. Existing published proofs are inherited, not counted as newly executed checks.

**Review status:** Established within the stated mathematical scope by this investigation; GPT's focused review of the new proof and package remains pending. This is not external peer review or physical validation.
