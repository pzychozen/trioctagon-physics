# Same-trajectory native credit from an initially empty launch

**Investigation:** NATIVE_SAME_TRAJECTORY_RETURN_01  
**Date:** 3 November 2026, Atlantic/Reykjavik  
**Author and research direction:** Hilmir Frímann Halldórsson / pzychozen  
**Proposed certificate and subsequent review:** GPT  
**Independent analytical verification:** Codex  
**Status:** Local investigation for author/GPT review; no publication or model adoption.

## Disposition

**Established within the unchanged published exchange candidate.** For every fixed admissible geometry, finite-width profiles, registration, positive storage scales, native coupling and coherent launch specified below, the proposed finite receiver-coupling threshold is sufficient. Each finite coupling at or above it gives initial total native supply, initial receiver charging, and a later interval of strictly negative **total** native-to-carrier power on that same solution. No state is reset or separately prepared. The proposed constants and threshold require no correction.

This is a sufficient existence regime, not a statement about every positive receiver coupling. The later native gain recovers earlier supplied trial storage: the native store never exceeds its initial value. The certificate concerns fast, collocated exchange, not a completed spatial circuit or a substantial returned fraction. It makes no assertion about the exact receiver-power sign at the native-credit witness.

The defining baseline is research edition v0.1 at commit `273b1a6faaab19ea58748d00576439166eeef9ab`. Its seven defining files match the hashes in the new order. They are retained under [sources/](sources/), with full identities and immutable references in [SOURCE_IDENTITIES.json](SOURCE_IDENTITIES.json). This report adds the finite-coupling comparison proof; it does not amend that edition or retroactively change its stated open question.

## 1. Fixed problem, preparation and theorem

All vector spaces and inner products used below are real unless a complex native coordinate is explicitly written. Fix once and for all the published admissible periodic carrier geometry, its finite circumference $L_c$, speed $c>0$, and two contact positions $s_\pm=L_c/2\mp\eta_{\rm geom}$. Retain every published condition ensuring the normalized periodic tents below have disjoint supports. In particular $0<\epsilon_c<\eta_{\rm geom}$; no zero-width limit is taken.

Fix $\lambda_g,\kappa_{\rm in}>0$, a finite yaw $\delta_g$, positive storage scales $\alpha_N,\beta_R$, a fixed $\eta_N>0$, and one fixed $0<\phi<\pi/12$. The allowed default $\phi=\pi/24$ is a specialization; the proof keeps $\phi$ symbolic. None of these choices depends on the later choice of receiver coupling.

Use exactly the inherited registration and chiral drive:

\[
u=(0,1,0),\quad e_z=(0,0,1),\quad
n_\pm=\frac{2u\pm\sqrt3e_z}{\sqrt7},\quad
K=\kappa_{\rm in}
\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}\lambda_gR_z(\delta_g),
\qquad f(x)=K(a\times b),\quad J(x)=D_xf(x),\quad x=(a,b).
\tag{R1}
\]

There is no extra contact-tangent sign. Define

\[
b_\sigma(s)=\epsilon_c^{-1}
\left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
\quad \mathcal Bv=b_+v_++b_-v_-,\quad y=\mathcal B^*p,
\quad m=\frac2{3\epsilon_c},\quad d=\frac2{\epsilon_c^3}.
\tag{R2}
\]

For the finite positive constant $\kappa=\eta_R$, the equations under investigation are

\[
\begin{aligned}
\dot x&=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\\
p_t+c(r_c)_s&=\mathcal B\{\eta_Nf(x)-\kappa z\},\\
(r_c)_t+cp_s&=0,\\
\dot z&=\frac{\kappa}{\beta_R}y,\qquad y=\mathcal B^*p.
\end{aligned}
\tag{R3}
\]

All coefficients remain constant along a solution. In particular its propagation speed is always the original positive $c$. There are no native $F$-jumps, switching, damping, extra feedback terms or added states. The preparation is

\[
\Omega_0=a_0+ib_0=(1,e^{i\phi},1),\qquad
p(0)=r_c(0)=z(0)=0.
\tag{R4}
\]

Let $G=\kappa_{\rm in}\lambda_g$, $R=|x_0|=\sqrt3$, $k=\|K\|=G\sqrt{8/7}$, and $f_0=f(x_0)$. Define the following constants, all independent of $\kappa$:

\[
\begin{gathered}
F_{\max}=\frac{kR^2}{2},\qquad
\omega=\sqrt{m/\beta_R},\qquad T=\frac{3\pi}{2\omega},
\qquad D=\frac m\omega|f_0|^2,\\
A=\frac{\eta_N^2k^2R^2mF_{\max}}{4\alpha_N},\qquad
C_1=\frac{3c\sqrt{md}\,|f_0|^2}{\omega^2},\qquad
C_2=mAT^3\left(F_{\max}+\frac{|f_0|}{3}\right),\\
\kappa_{\rm crit}=
\max\left\{1,\frac{4C_1}{D},\sqrt{\frac{4C_2}{D}}\right\}.
\end{gathered}
\tag{R5}
\]

**Theorem (finite-coupling same-trajectory credit).** Under the fixed assumptions above, $D>0$ and $\kappa_{\rm crit}$ is positive, finite and explicitly computable from those fixed parameters. For **each finite fixed** $\kappa\ge\kappa_{\rm crit}$, the unique global solution of (R3)–(R4) satisfies:

1. For some $\varepsilon_\kappa>0$, at every $0<t<\varepsilon_\kappa$ its total native power $P_{NC}(t)=\eta_Nf(x(t))^Ty(t)$ is positive, and its receiver storage $H_R(t)=\beta_R|z(t)|^2/2$ and receiver power $P_{CR}(t)=\kappa z(t)^Ty(t)$ are positive.
2. At the explicitly specified later time $t_*=T/\kappa$,

\[
P_{NC}(t_*)\le-\frac{\eta_N^2D}{2\kappa}<0.
\tag{R6}
\]

3. There is $0<\rho_\kappa<t_*/4$ such that on the whole closed interval $I_\kappa=[t_*-\rho_\kappa,t_*+\rho_\kappa]\subset(0,\infty)$,

\[
P_{NC}(t)\le-\frac{\eta_N^2D}{4\kappa},\qquad
H_N(t_*+\rho_\kappa)-H_N(t_*-\rho_\kappa)
\ge\frac{\eta_N^2D\rho_\kappa}{2\kappa}>0.
\tag{R7}
\]

The initial positive interval may be reduced so that it lies strictly before $I_\kappa$. It and the later negative interval belong to the very same empty-launch solution with the same constant coupling. No uniform initial interval or explicit lower bound for $\rho_\kappa$ is claimed.

For every future exchange time, irrespective of the later sign change,

\[
H_N(t)\le H_N(0),\qquad
\int_0^tP_{NC}(s)\,ds=H_C(t)+H_R(t)\ge0.
\tag{R8}
\]

Here $H_N=\alpha_N|x|^2/2$ and $H_C=\frac12\int(p^2+r_c^2)\,ds$. The theorem concerns these trial stores, not a calibrated physical energy or the distinct native quartic potential $V$.

## 2. Preparation, operator bounds and legitimate regularity

The source for (R1)–(R3) is [candidate.tex](sources/manuscript/candidate.tex), §1, equations (1.1)–(1.6). The signs and accounts are [power.tex](sources/manuscript/power.tex), §2, especially (2.1), (2.3), (2.5)–(2.6). Theorem 3.1 in [wellposed.tex](sources/manuscript/wellposed.tex) supplies global existence for every fixed finite choice of the parameters. Empty carrier preparation is periodic $H^1$, so the actual solution has

\[
(p,r_c)\in C(\mathbb R;H^1_{\rm per})^2\cap C^1(\mathbb R;L^2)^2,
\qquad x,z\in C^1(\mathbb R).
\tag{R9}
\]

It conserves $H_N+H_C+H_R$, with $\dot H_N=-P_{NC}$ and $\dot H_R=P_{CR}$. No new existence result is inferred merely from a formal energy cancellation. This already proved regularity justifies the strong energy calculations used below, separately for every finite $\kappa$.

Independently, the row Gram matrix is

\[
KK^T=G^2\begin{pmatrix}1&1/7\\1/7&1\end{pmatrix},
\quad \operatorname{spec}(KK^T)=\{8G^2/7,6G^2/7\}.
\tag{R10}
\]

The yaw rotation cancels from this product. Thus the claimed $k$ is the Euclidean operator norm. The preparation gives $a_0=(1,\cos\phi,1)$, $b_0=(0,\sin\phi,0)$, $a_0\times b_0=(-\sin\phi,0,\sin\phi)$, and

\[
f_{0,\pm}=\frac{G\sin\phi}{\sqrt7}(-2\sin\delta_g\pm\sqrt3),
\quad |f_0|^2=\frac{G^2\sin^2\phi}{7}(6+8\sin^2\delta_g)>0.
\tag{R11}
\]

Its two entries differ by $2\sqrt3G\sin\phi/\sqrt7\ne0$; either individual entry may vanish, but the vector cannot. All native moduli are one and the ordinary phase span is $\phi$, satisfying the inherited coherent launch hypotheses. We assume no invariance of this particular family or coherent domain during evolution.

For a single tent, integrating its two affine halves yields mass one, squared $L^2$ norm $m$, and squared first weak derivative norm $d$. Its continuity makes the first weak derivative a piecewise constant $L^2$ function, with no delta distribution. Disjoint supports remove both types of cross term (endpoints are null sets). Consequently

\[
\mathcal B^*\mathcal B=mI_2,\qquad
\|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\qquad
\|\mathcal B'v\|_2=\sqrt d\,|v|.
\tag{R12}
\]

Differentiating $f$ and applying the cross-product and Cauchy–Schwarz inequalities gives

\[
|f(x)|\le k|a||b|\le\frac{k}{2}|x|^2,\qquad
|J(x)h|\le k\{|b||h_a|+|a||h_b|\}\le k|x||h|.
\tag{R13}
\]

For the empty launch, conservation and positivity of the external stores give $|x(t)|\le R$ at all times. On the convex Euclidean ball of radius $R$, (R13) and the line-segment integral of the derivative imply $|f(x)-f(\widetilde x)|\le kR|x-\widetilde x|$. This is a ball estimate; it uses no phase-domain preservation.

## 3. Exact scaling and the external-energy inequality

Set $\tau=\kappa t$, let $x_\kappa(\tau)=x(\tau/\kappa)$, and set

\[
(p,r_c,z)(\tau/\kappa)=\frac{\eta_N}{\kappa}
(\widehat p,\widehat r,\widehat z)(\tau),\qquad
\widehat y=\mathcal B^*\widehat p.
\tag{R14}
\]

Because $\kappa$ is dimensionless, $\tau$ retains time units. Direct chain rule, with the fixed linear operator $\mathcal B$, gives the **exact** finite-coupling system

\[
\begin{aligned}
(x_\kappa)_\tau&=-\frac{\eta_N^2}{2\alpha_N\kappa^2}J(x_\kappa)^T\widehat y,\\
\widehat p_\tau+\frac c\kappa\widehat r_s&=\mathcal B\{f(x_\kappa)-\widehat z\},\\
\widehat r_\tau+\frac c\kappa\widehat p_s&=0,\\
\widehat z_\tau&=\frac1{\beta_R}\widehat y.
\end{aligned}
\qquad
P_{NC}(\tau/\kappa)=\frac{\eta_N^2}{\kappa}f(x_\kappa(\tau))^T\widehat y(\tau).
\tag{R15}
\]

This is a change of variables, not a change of the physical-time speed or an infinite-coupling solution.

On the external energy space $\mathcal E=L^2_{\rm per}\times L^2_{\rm per}\times\mathbb R^2$, use

\[
\|W\|_{CR}^2=\|q\|_2^2+\|h\|_2^2+\beta_R|v|^2,
\qquad W=(q,h,v),
\]
\[
\mathcal L_\kappa W=
\left(-\frac c\kappa h_s-\mathcal Bv,
      -\frac c\kappa q_s,\frac1{\beta_R}\mathcal B^*q\right),
\quad D(\mathcal L_\kappa)=H^1_{\rm per}{}^2\times\mathbb R^2.
\tag{R16}
\]

For $W$ in that domain, periodic integration by parts and adjointness give

\[
\langle W,\mathcal L_\kappa W\rangle_{CR}
=-\frac c\kappa\int(qh_s+hq_s)\,ds
-\langle q,\mathcal Bv\rangle+v^T\mathcal B^*q=0.
\tag{R17}
\]

Thus a strong solution of $W_\tau=\mathcal L_\kappa W+g$ satisfies

\[
\|W(\tau)\|_{CR}\le\|W(0)\|_{CR}
+\int_0^\tau\|g(s)\|_{CR}\,ds\quad(\tau\ge0).
\tag{R18}
\]

For rigor at zeros of the norm, differentiate $\sqrt{\|W\|_{CR}^2+\varepsilon^2}$. By (R17) its derivative is at most $\|g\|_{CR}$; integrate and let $\varepsilon\downarrow0$. The homogeneous equation therefore preserves this weighted norm. No division by a vanishing norm is used. We apply (R18) only to the known strong solution and its difference from an explicitly strong comparison. A group representation or operator-norm limit of unbounded generators is unnecessary.

Take $V_\kappa=(\widehat p,\widehat r,\widehat z)$. It starts at zero and has forcing $g=(\mathcal Bf(x_\kappa),0,0)$. Since $|x_\kappa|\le R$, (R12)–(R13) and (R18) yield, for every finite $\tau\ge0$,

\[
\|V_\kappa(\tau)\|_{CR}\le\sqrt mF_{\max}\tau,
\qquad |\widehat y(\tau)|\le\sqrt m\|\widehat p(\tau)\|_2
\le mF_{\max}\tau.
\tag{R19}
\]

The constants are independent of $\kappa$. Keeping the receiver in the energy-conserving linear block is essential here; bounding its loading separately would lose this estimate.

Integrating the first equation in (R15), then using the ball Lipschitz bound, gives

\[
|x_\kappa(\tau)-x_0|
\le\frac{\eta_N^2 kR mF_{\max}}{4\alpha_N\kappa^2}\tau^2,
\qquad
|f(x_\kappa(\tau))-f_0|\le\frac{A\tau^2}{\kappa^2}.
\tag{R20}
\]

The factor (1/4) includes the feedback factor (1/2) and the integral of $s$. No comparison convergence has been assumed to obtain either (R19) or (R20).

## 4. Explicit comparison and its finite error

Only in the comparison problem, freeze the core and remove scaled propagation. With the same zero external preparation its exact solution is

\[
x^{(0)}=x_0,\qquad
\widehat p^{(0)}(\tau)=\frac{\sin(\omega\tau)}{\omega}\mathcal Bf_0,
\quad \widehat r^{(0)}=0,\quad
\widehat z^{(0)}(\tau)=f_0\{1-\cos(\omega\tau)\},
\]
\[
\widehat y^{(0)}(\tau)=\frac m\omega f_0\sin(\omega\tau).
\tag{R21}
\]

Indeed $\widehat p^{(0)}_\tau=\mathcal B(f_0-\widehat z^{(0)})$ and $\widehat z^{(0)}_\tau=\mathcal B^*\widehat p^{(0)}/\beta_R$, because $\omega^2=m/\beta_R$. These fields start at zero and the carrier is $C^1_\tau H^1_s$. At $T=3\pi/(2\omega)$,

\[
Q_0(T):=f_0^T\widehat y^{(0)}(T)=-\frac m\omega|f_0|^2=-D<0.
\tag{R22}
\]

Let $E_\kappa=V_\kappa-V_0$, where $V_0=(\widehat p^{(0)},0,\widehat z^{(0)})$. Direct subtraction, keeping the **finite** operator $\mathcal L_\kappa$ on the error, gives

\[
(E_\kappa)_\tau=\mathcal L_\kappa E_\kappa
+(\mathcal B(f(x_\kappa)-f_0),0,0)
+\left(0,-\frac c\kappa\mathcal B'f_0
                    \frac{\sin(\omega\tau)}{\omega},0\right),
\qquad E_\kappa(0)=0.
\tag{R23}
\]

In particular the last sign is negative: it is the second component of $(\mathcal L_\kappa-\mathcal L_0)V_0$. The first component of this operator difference is zero because $\widehat r^{(0)}=0$. The residual differentiates only $\widehat p^{(0)}$ once in space. By (R12) it belongs to $L^2$; no second derivative, Fourier truncation, delta source, uniform $H^1$ limit or operator-norm convergence is involved.

The error is a legitimate strong energy-space curve: it is the difference of the known $C_\tau H^1_s\cap C^1_\tau L^2_s$ exact carrier and the explicit comparison. We need not infer its regularity from the residual, whose spatial derivative is not assumed to be $L^2$. Applying (R18), the triangle inequality, (R12) and (R20) yields, on $0\le\tau\le T$,

\[
\|E_\kappa(\tau)\|_{CR}
\le\frac{c\sqrt d\,|f_0|}{\kappa\omega}
       \int_0^\tau|\sin(\omega s)|\,ds
+\frac{\sqrt m A\tau^3}{3\kappa^2}.
\tag{R24}
\]

The absolute sine integral is $2/\omega+1/\omega=3/\omega$ at $T$, with the split at $\pi/\omega$. Therefore

\[
\boxed{\|E_\kappa(T)\|_{CR}
\le\frac{3c\sqrt d\,|f_0|}{\kappa\omega^2}
+\frac{\sqrt m AT^3}{3\kappa^2}.}
\tag{R25}
\]

This estimate controls propagation and core drift simultaneously along the exact solution. The comparison alone would not establish finite-coupling return.

## 5. Total-power margin and completion of the theorem

Put $Q_\kappa=f(x_\kappa(T))^T\widehat y(T)$. The exact two-port decomposition is

\[
Q_\kappa-Q_0(T)
=(f(x_\kappa(T))-f_0)^T\widehat y(T)
+f_0^T(\widehat y(T)-\widehat y^{(0)}(T)).
\tag{R26}
\]

The first term uses the exact finite-solution port bound, not the comparison port. Boundedness of $\mathcal B^*$, (R19), (R20) and (R25) give

\[
\begin{aligned}
|Q_\kappa+D|
&\le\frac{AT^2}{\kappa^2}\,mF_{\max}T
+|f_0|\sqrt m\left(
\frac{3c\sqrt d\,|f_0|}{\kappa\omega^2}
+\frac{\sqrt m AT^3}{3\kappa^2}\right)\\
&=\frac{C_1}{\kappa}+\frac{C_2}{\kappa^2}.
\end{aligned}
\tag{R27}
\]

All constants in (R5) are finite and strictly positive under the fixed hypotheses; in particular (R11) proves $D>0$. If $\kappa\ge\kappa_{\rm crit}$, then $C_1/\kappa\le D/4$ and $C_2/\kappa^2\le D/4$. Thus $Q_\kappa\le-D/2$, and the exact power scaling (R15) proves (R6). This is the signed dot product across both native ports, not a negative component offset by a larger positive component.

The function $P_{NC}$ is continuous: $x$ is continuous, $f$ is polynomial, $p$ is continuous in $L^2$, and $\mathcal B^*$ is bounded. Its strict margin at $t_*$ therefore permits $0<\rho_\kappa<t_*/4$ such that the half-margin in (R7) holds throughout the closed interval. Integrating the inherited identity $\dot H_N=-P_{NC}$ proves the stated positive increment. The witness time and power margin are explicit; the interval width is supplied by continuity, with no asserted uniform modulus.

Proposition 4.1 in [activity.tex](sources/manuscript/activity.tex) applies for **each fixed finite** positive $\kappa$, since the preparation is empty and $f_0\ne0$. More explicitly its expansions give

\[
\begin{aligned}
P_{NC}(t)&=\eta_N^2m|f_0|^2t+o(t)>0,\\
H_R(t)&=\frac{\eta_N^2\kappa^2m^2|f_0|^2}{8\beta_R}t^4+o(t^4)>0,\\
P_{CR}(t)&=\frac{\eta_N^2\kappa^2m^2|f_0|^2}{2\beta_R}t^3+o(t^3)>0
\end{aligned}
\tag{R28}
\]

for all sufficiently small positive time. Reduce this positive interval to lie in $(0,t_*/4)$. It is then strictly earlier than $I_\kappa$. These remainders need not be uniform as $\kappa\to\infty$, and no such uniformity was used. Unique global evolution ensures that the initial and later observations are on one trajectory. Prepared-credit data and the reversing involution play no role in this inference.

Finally, the initially empty stores and conservation give

\[
H_N(0)-H_N(t)=H_C(t)+H_R(t)
=\int_0^tP_{NC}(s)\,ds\ge0,
\]

which is (R8) and completes the theorem. A later negative interval reduces this cumulative debit without reversing its nonnegative all-time sign.

## 6. Units, quantitative meaning and limits

The inherited units in candidate Table 2 use native amplitude $\mathrm A$, carrier $\mathrm U$, length $\mathrm L$, and time $\mathrm T$. The letter $A$ in (R5) is a drift constant, distinct from the amplitude unit. Relevant dimensions are:

| Quantity | Dimension |
|---|---|
| $R;k;F_{\max},f_0$ | $\mathrm A;\ \mathrm U\mathrm L/(\mathrm T\mathrm A^2);\ \mathrm U\mathrm L/\mathrm T$ |
| $m;d;c$ | $\mathrm L^{-1};\ \mathrm L^{-3};\ \mathrm L/\mathrm T$ |
| $\alpha_N;\beta_R;\omega$ | $\mathrm U^2\mathrm L/\mathrm A^2;\ \mathrm T^2/\mathrm L;\ \mathrm T^{-1}$ |
| $\tau,T,t_*;\kappa,\eta_N$ | $\mathrm T;\ 1$ |
| $A$ | $\mathrm U\mathrm L/\mathrm T^3$ |
| $\|V\|_{CR}$ | $\mathrm U\mathrm L^{1/2}$ |
| $D,C_1,C_2,Q_\kappa,P_{NC}$ | $\mathrm U^2\mathrm L/\mathrm T$ |
| $C_1/D,C_2/D,\kappa_{\rm crit}$ | $1$ |

For example $\sqrt m A T^3$ and $c\sqrt d|f_0|/\omega^2$ both have external-norm units. The comparison is dimensionally consistent. No physical scale, coupling calibration or diversion target is thereby selected. The $1$ in the threshold is dimensionless and harmless; the threshold is conservative, not claimed optimal or necessary.

At the comparison witness $\widehat z^{(0)}(T)=f_0$ and $\widehat y^{(0)}(T)=-(m/\omega)f_0$. Their dot product is negative, illustrating receiver backflow in the comparison. The theorem proves exact total **native** credit and actual initial receiver activity. It does not additionally assert $P_{CR}(t_*)<0$ for every coupling satisfying this particular threshold; that would require its own finite bound.

For any fixed finite scaled window $0\le\tau\le S$, (R14) and (R19) imply

\[
H_C(\tau/\kappa)+H_R(\tau/\kappa)
=\frac{\eta_N^2}{2\kappa^2}\|V_\kappa(\tau)\|_{CR}^2
\le\frac{\eta_N^2mF_{\max}^2S^2}{2\kappa^2}.
\tag{R29}
\]

In particular $S=T$ covers launch through the witness, and $S=5T/4$ covers the credit interval chosen above. The external storage on these windows is $O(\eta_N^2/\kappa^2)$. Equation (R27) also gives $P_{NC}(t_*)=-\eta_N^2D/\kappa+O(\eta_N^2/\kappa^2)$ when all other parameters are fixed. Strict existence is compatible with small transfer; no substantial return fraction, maximal extraction or accessible-capacity result is implied.

The witness obeys $t_*/(L_c/c)=cT/(\kappa L_c)\to0$. Thus sufficiently large finite couplings make it arbitrarily early compared with the fixed circle-travel time. Both interactions use the same finite profile regions. This is not an outward–around–inward route certificate, a first circuit time, or identification of a tagged cohort.

The inherited exchange invariant remains $Z_2=\sum_i\Omega_i^2$. Combining (R8) with the invariant bound in [capacity.tex](sources/manuscript/capacity.tex), Theorem 5.1, gives

\[
0\le\frac{H_N(0)-H_N(t)}{H_N(0)}
\le\frac{I_0-|Z_2(\Omega_0)|}{I_0}
\le1-\cos\phi
<1-\cos(\pi/12)\simeq0.0340741737109317.
\tag{R30}
\]

This is net extraction relative to initial core trial storage. It is compatible with a later local gain and remains valid without coherent-domain invariance. The approximately 3.4074% ceiling is neither attained here nor a gross-work bound, receiver fraction or the author's tentative diversion share.

The distinctions in [interpretation.tex](sources/manuscript/interpretation.tex), §8, remain in force: the one-dimensional circle, intended tight toroid and opposed cones, close original enclosing sphere, and extended-line sphere are different objects. The selected host-notch pair $N_1^\pm$ differs from the six central broken boundaries $G_k^\pm$. Supports stay stationary. Exclusion of the exact point $O$ does not exclude every finite central starting/meeting region. No new receiver location, chord, six-opening map, field, gravity–magnetism relation or physical energy unit has been assigned. The author's outward–around–inward picture and rough 15–20%, possibly more, remain motivating intuition, not a fitted value or a conclusion of this certificate.

## 7. Evidence and endpoint

The proposed certificate was challenged by checking registration, nonzero preparation, exact scaling, the weighted skew cancellation, strong regularity of the error, the residual sign and derivative order, both error terms, dimensions, quantifier order and the distinction between local credit and cumulative gain. The resulting analytical proof establishes the proposed sufficient finite threshold without changing the model or constants.

The new [exact helper](exact_certificate_checks.py) and [results](EXACT_CERTIFICATE_RESULTS.json) record 25 finite-expression checks (SymPy 1.14.0 in torment Python 3.11.15). They support algebra, integrals, coefficient collection and dimensional exponents. They do **not** prove PDE regularity, integration-by-parts hypotheses, norm inequalities, continuity, source admissibility or the theorem. Those are justified above using the seven identified sources and the written energy argument. Historical 28-check evidence was not rerun or added to the new count.

The standalone [START_HERE context](START_HERE_CONTEXT.md) reports a later review of the previous PDF. Its named full handoff ZIP and separate review files were not found in the focused Downloads search, and their contents were not inspected here. That availability point does not remove a defining source: all seven hash-pinned files required for this investigation were available and matched. The new [order](SUPPLIED_WORK_ORDER.md) supplies the proposed route; it is not treated as proof that the new theorem was already established. Current GPT review of this investigation is pending.

The endpoint is this reviewable theorem and package. No numerical trajectory, parameter sweep, native $F$-jump, model import, geometry construction, observer update, Git operation or publication was performed. Accessible transfer, exact later receiver behavior, hybrid stepping, intended spatial route and broader return classification remain separate subsequent investigations.
