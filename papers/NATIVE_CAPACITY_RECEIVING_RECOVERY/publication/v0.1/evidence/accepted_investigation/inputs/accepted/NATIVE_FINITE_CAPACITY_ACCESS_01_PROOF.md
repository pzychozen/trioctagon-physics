# Native finite capacity access: independent proof assessment

**Task:** NATIVE_FINITE_CAPACITY_ACCESS_01  
**Date:** 4 November 2026  
**Research author and direction:** Hilmir Frímann Halldórsson (pzychozen)  
**Formulation:** GPT's proposed certificate  
**Independent investigation and proof:** Codex  
**Verdict:** **Established unchanged.** This new investigation result is submitted for GPT review; it is not a published paper or a claim of completed review.

## 1. Unchanged model and theorem

Use \(x=(a,b)\in\mathbb R^6\), \(\Omega=a+ib\), and the published raw two-port order \(+,-\). With positive finite registration gains, retain

\[
\begin{gathered}
e_y=(0,1,0),\quad e_z=(0,0,1),\quad
n_\pm=(2e_y\pm\sqrt3e_z)/\sqrt7,\quad
A_{\rm reg}=\lambda_gR_z(\delta_g),\\
K=\kappa_{\rm in}\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}A_{\rm reg},
\quad G=\kappa_{\rm in}\lambda_g>0,\quad
f(x)=K(a\times b),\quad J(x)=D_xf(x).
\end{gathered}\tag{FA01}
\]

These are P3 (2.1), originally P1 §1. Contact-tangent signs do not change the raw registration. Fix the published witness yaw \(\delta_g=\pi/4\).

The carrier is \(s\in\mathbb R/L_c\mathbb Z\), with finite positive \(L_c,c\), admitted contacts \(s_\pm=L_c/2\mp\eta_{\rm geom}\), shortest **periodic** distance \(2\eta_{\rm geom}\), and \(0<\epsilon_c<\eta_{\rm geom}\). For these positions the shortest-distance assertion includes \(2\eta_{\rm geom}\le L_c/2\); interval nonoverlap alone is not substituted. Define

\[
\begin{gathered}
b_\sigma(s)=\epsilon_c^{-1}
\left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
\quad \mathcal Bv=b_+v_++b_-v_-,\\
\mathcal B^*p=\begin{pmatrix}\int b_+p\,ds\\\int b_-p\,ds\end{pmatrix},
\quad m=\frac2{3\epsilon_c},\quad d=\frac2{\epsilon_c^3},\\
\mathcal B^*\mathcal B=mI_2,\quad
\|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\quad
\|\mathcal B'v\|_2=\sqrt d\,|v|.
\end{gathered}\tag{FA02}
\]

Integrals cover the whole circle. These inherited identities are P3 (2.2) and P1 eq:profilenorms. Whole-circle separation ensures disjoint supports including the coordinate seam. Each normalized tent is continuous and in \(H^1_{\rm per}\); its first weak derivative lies in \(L^2\) without corner delta terms. No second tent derivative is assumed.

For positive finite \(\alpha_N,\beta_R,\eta_N,\kappa=\eta_R\), retain the original, unscaled equations

\[
\begin{aligned}
\dot x&=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\\
p_t+c(r_c)_s&=\mathcal B\{\eta_Nf(x)-\kappa z\},\\
(r_c)_t+cp_s&=0,\qquad
\dot z=\frac{\kappa}{\beta_R}y,\qquad y=\mathcal B^*p .
\end{aligned}\tag{FA03}
\]

The trial stores and total signed powers are

\[
\begin{gathered}
H_N=\frac{\alpha_N}{2}|x|^2,\quad
H_C=\frac12(\|p\|_2^2+\|r_c\|_2^2),\quad
H_R=\frac{\beta_R}{2}|z|^2,\\
P_{NC}=\eta_Nf(x)^Ty,\quad P_{CR}=\kappa z^Ty,\quad
\dot H_N=-P_{NC},\quad
\dot H_C=P_{NC}-P_{CR},\quad
\dot H_R=P_{CR},\\
H_N+H_C+H_R=\text{constant}.
\end{gathered}\tag{FA04}
\]

These are P3 (2.3)–(2.4). \(H_N\) is the quadratic trial store, not the native quartic potential. All coefficients are constant along a trajectory; no native-map jump, reset or feedback change occurs.

For each phase in the stated open range, take the published coherent empty preparation:

\[
\begin{gathered}
\Omega_0=(1,e^{i\phi},1),\quad0<\phi<\pi/12,\quad
p(0)=r_c(0)=z(0)=0,\\
R=|x_0|=\sqrt3,\quad k=\|K\|=G\sqrt{8/7},\quad
f_{0,\pm}=\frac{G\sin\phi}{\sqrt7}(-\sqrt2\pm\sqrt3),\\
|f_0|^2=\frac{10G^2\sin^2\phi}{7}>0,\quad
C_{\rm joint}=\alpha_N(1-\cos\phi)>0,\\
E_{\rm out}(t)=H_C(t)+H_R(t)=H_N(0)-H_N(t),\quad
0\le E_{\rm out}(t)\le C_{\rm joint}\quad(t\ge0).
\end{gathered}\tag{FA05}
\]

The launch and drive are P3 (2.7)–(2.8); the yaw-specific ceiling is (3.18), within Theorem 3.1 and (3.5). Numerical amplitudes use the published normalized native convention. Section 7 restores units while retaining \(R^2\) in dimensional formulas. No invariance of the initial coherent sector is assumed.

**Theorem.** First fix admitted geometry and positive finite coefficients as above, at yaw \(\pi/4\). Define the positive estimate rates

\[
\nu^2=\frac{\eta_N^2mk^2R^2}{2\alpha_N},\qquad
\sigma_{\rm ext}^2=\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}.
\tag{FA06}
\]

Assume

\[
\sigma_{\rm ext}\le\frac\nu2,\qquad t_*=\frac1\nu.
\tag{FA07}
\]

Then, for **every** \(0<\phi<\pi/12\), the unique unchanged solution of (FA03) with (FA05) satisfies

\[
\boxed{E_{\rm out}(t_*)>
\frac{1053}{4096}C_{\rm joint}>
\frac14 C_{\rm joint}>0.}
\tag{FA08}
\]

The same coefficients and time \(t_*\) work throughout the phase range: \(R,k,m,d,\nu,\sigma_{\rm ext}\) are phase independent. Equality in the parameter condition is allowed. No zero speed/coupling, coefficient limit or switching is needed. The rate \(\nu\) is an analytical estimate scale, not a physical native frequency or \(F\) cadence. The conclusion concerns combined external stock at one time, relative to the joint ceiling.

## 2. Solution class and original forced estimate

P1 **Theorem 3.1** is the global exchange theorem; it is distinct from P2 **Theorem 3.1**, the later native-credit theorem. P1's theorem and P3 §2.2 give, for the empty \(H^1\) carrier preparation,

\[
\begin{gathered}
x,z\in C^1(\mathbb R),\quad
(p,r_c)\in C(\mathbb R;H^1_{\rm per})^2\cap C^1(\mathbb R;L^2)^2,\\
|x(t)|\le R,\quad \|J(x(t))\|\le kR,\quad
|y(t)|\le\sqrt m\,\|U(t)\|_{CR},\\
U=(p,r_c,z),\quad
\|U\|_{CR}^2=\|p\|_2^2+\|r_c\|_2^2+\beta_R|z|^2=2E_{\rm out}.
\end{gathered}\tag{FA09}
\]

Conservation and nonnegative external stores give the native ball. Also
\(J(x)h=K(h_a\times b+a\times h_b)\), and
\(|h_a||b|+|a||h_b|\le |x||h|\) gives \(\|J(x)\|\le k|x|\).
The port bound follows from (FA02) and the carrier projection of the weighted norm. These are unscaled uses of P3 (5.5). Existence and strong regularity precede, and are not inferred from, the following formal-looking cancellation.

On \(\mathcal H_{\rm ext}=L^2_{\rm per}\times L^2_{\rm per}\times\mathbb R^2\), use the weighted inner product corresponding to (FA09) and define

\[
\begin{gathered}
\mathscr LU=\left(-c(r_c)_s-\kappa\mathcal Bz,\,-cp_s,\,
\frac{\kappa}{\beta_R}\mathcal B^*p\right),\\
D(\mathscr L)=H^1_{\rm per}\times H^1_{\rm per}\times\mathbb R^2,\quad
\dot U=\mathscr LU+(\eta_N\mathcal Bf(x),0,0).
\end{gathered}\tag{FA10}
\]

For \(V=(q_c,h,v)\in D(\mathscr L)\), periodic integration and adjointness yield

\[
\begin{aligned}
\langle V,\mathscr LV\rangle_{CR}
&=-c\int[q_ch_s+h(q_c)_s]\,ds
-\kappa\langle q_c,\mathcal Bv\rangle_2
+\kappa v\cdot\mathcal B^*q_c=0,\\
\dot V=\mathscr LV+F
&\ \Longrightarrow\
\|V(t)\|_{CR}\le\|V(0)\|_{CR}+\int_0^t\|F(s)\|_{CR}\,ds .
\end{aligned}\tag{FA11}
\]

The carrier integrand is the weak derivative of the periodic product \(q_ch\), with zero integral. The receiver's inner-product weight \(\beta_R\) cancels the feedback denominator, leaving matching terms with \(\kappa\). Thus the original factors are derived explicitly, rather than copied from scaled-time P3 (5.4).

For a known strong curve \(V\in C([0,T];D(\mathscr L))\cap C^1([0,T];\mathcal H_{\rm ext})\) and continuous \(F\), regularize with \(\varepsilon>0\):
\[
\frac{d}{dt}\sqrt{\|V(t)\|_{CR}^2+\varepsilon^2}
=\frac{\langle V(t),F(t)\rangle_{CR}}
{\sqrt{\|V(t)\|_{CR}^2+\varepsilon^2}}\le\|F(t)\|_{CR}.
\]
Integration and \(\varepsilon\downarrow0\) prove (FA11), including at zeros. No differentiation of an unregularized norm at zero or division by zero is used. The actual and difference curves below have the required strong regularity.

## 3. Drive-dependent Volterra comparison

Set \(A_0=\eta_N\sqrt m\,|f_0|>0\), a forcing magnitude distinct from the published drift constant and accessibility statistic. The actual empty state and (FA11) give

\[
\begin{aligned}
\|U(t)\|_{CR}&\le\eta_N\sqrt m\int_0^t|f(x(s))|\,ds,\\
\dot f(x(t))&=J(x(t))\dot x(t)
=-\frac{\eta_N}{2\alpha_N}J(x(t))J(x(t))^Ty(t),\\
|f(t)-f_0|&\le
\frac{\eta_Nk^2R^2\sqrt m}{2\alpha_N}\int_0^t\|U(s)\|_{CR}\,ds.
\end{aligned}\tag{FA12}
\]

The chain rule holds since \(x\in C^1\) and \(f\) is quadratic. The sign and factor come from the actual feedback; the last line uses \(\|JJ^T\|\le k^2R^2\) and (FA09).

Define continuous nonnegative functions \(g=\|U\|_{CR}/A_0\) and \(h=|f-f_0|/|f_0|\). Then

\[
\begin{gathered}
g(t)\le t+\int_0^t h(s)\,ds,\qquad
h(t)\le\nu^2\int_0^t g(s)\,ds,\\
g(t)\le t+(\mathcal Vg)(t),\qquad
(\mathcal Vv)(t)=\nu^2\int_0^t(t-s)v(s)\,ds .
\end{gathered}\tag{FA13}
\]

The second coefficient is exactly
\(\eta_Nk^2R^2\sqrt m\,A_0/(2\alpha_N|f_0|)=\nu^2\), retaining both native-coupling factors. Interchanging the continuous nonnegative double integral proves the last line.

On a finite \([0,T]\), \(\mathcal V\) preserves order. Iterating \(g\le t+\mathcal Vg\) proves

\[
\begin{gathered}
g(t)\le\sum_{j=0}^{n-1}\frac{\nu^{2j}t^{2j+1}}{(2j+1)!}
+(\mathcal V^ng)(t),\\
0\le(\mathcal V^ng)(t)
\le M_T\frac{\nu^{2n}t^{2n}}{(2n)!}
\le M_T\frac{\nu^{2n}T^{2n}}{(2n)!}\longrightarrow0,\quad
M_T=\sup_{0\le s\le T}g(s)<\infty .
\end{gathered}\tag{FA14}
\]

The identity
\(\int_0^t(t-s)s^\ell ds=t^{\ell+2}/[(\ell+1)(\ell+2)]\)
proves the summands and remainder bound by induction, beginning with \(\mathcal V^0t=t\) and \(\mathcal V^0 1=1\). Continuity gives finite \(M_T\). Successive factorial bounds have ratio
\((\nu T)^2/[(2n+2)(2n+1)]\to0\), so the remainder vanishes uniformly on the finite interval. No differential inequality for the norm \(g\) is assumed. The series sums to \(\sinh(\nu t)/\nu\).

Substitute this into the bound for \(h\) to obtain, at every finite \(t\ge0\),

\[
\boxed{\|U(t)\|_{CR}\le\frac{A_0}{\nu}\sinh(\nu t),\qquad
|f(t)-f_0|\le |f_0|[\cosh(\nu t)-1].}
\tag{FA15}
\]

Both estimates retain the actual launch-drive factor, essential to normalizing by a capacity that becomes small near the excluded zero-drive phase.
The iteration is applied separately to each admitted phase and requires no phase-uniform bound on \(M_T\). Its resulting explicit estimate has the same formula for every phase.

## 4. Reference curve, full residual and finite error

Use a comparison curve, not a replacement dynamical system:

\[
U_{\rm ref}(t)=(\eta_Nt\mathcal Bf_0,0,0),\qquad
\|U_{\rm ref}(t)\|_{CR}=A_0t,\qquad W=U-U_{\rm ref}.
\tag{FA16}
\]

Since \(\mathcal Bf_0\in H^1_{\rm per}\), the reference is \(C^1\) with values in \(D(\mathscr L)\). The actual state already has (FA09). Consequently \(W\) is strong **before** its residual is estimated: its carrier is \(C_tH^1_{\rm per}\cap C_t^1L^2\) and its receiver is \(C^1\). This preserves the regularity order used in P3 §5.2, p. 10.

Substitute \(U=W+U_{\rm ref}\) into (FA10) and subtract \(\dot U_{\rm ref}\):

\[
\begin{aligned}
\dot W&=\mathscr LW+(\eta_N\mathcal B(f-f_0),0,0)+F_{\rm ref}(t),
\qquad W(0)=0,\\
F_{\rm ref}(t)&=\mathscr LU_{\rm ref}(t)
=\left(0,-c\eta_Nt\mathcal B'f_0,
\frac{\kappa\eta_Nmt}{\beta_R}f_0\right).
\end{aligned}\tag{FA17}
\]

The first coordinate of \(\mathscr LU_{\rm ref}\) vanishes because its \(r_c,z\) are zero. The negative second coordinate is \(-c\partial_sp_{\rm ref}\); the positive receiver coordinate is \(\kappa\mathcal B^*p_{\rm ref}/\beta_R\), using the exact Gram identity \(mI_2\). The latter is nonzero even though the reference receiver is zero. Neither actual \(c\) nor actual \(\kappa\) has been set to zero.

The two residual coordinates are orthogonal in the weighted space:

\[
\begin{aligned}
\|F_{\rm ref}(t)\|_{CR}^2
&=\eta_N^2|f_0|^2t^2
\left(c^2d+\frac{\kappa^2m^2}{\beta_R}\right)
=A_0^2\sigma_{\rm ext}^2t^2,\\
\|F_{\rm ref}(t)\|_{CR}&=A_0\sigma_{\rm ext}t\quad(t\ge0).
\end{aligned}\tag{FA18}
\]

Only \(\mathcal B'f_0\in L^2\) is needed. This residual need not belong to \(H^1\); no strong regularity is inferred from it, and it is not differentiated spatially again. No second tent derivative or operator-norm limit of an unbounded propagation operator is used.

Apply (FA11) to the already strong \(W\), take the triangle inequality for its forcing terms, and use (FA15), (FA18):

\[
\begin{aligned}
\|U(t)-U_{\rm ref}(t)\|_{CR}
&\le\eta_N\sqrt m\int_0^t|f(s)-f_0|\,ds
+A_0\sigma_{\rm ext}\int_0^ts\,ds\\
&\le
\boxed{A_0\left[
\frac{\sinh(\nu t)}{\nu}-t+\frac{\sigma_{\rm ext}t^2}{2}
\right]} .
\end{aligned}\tag{FA19}
\]

This is a finite-time error estimate for the actual solution, valid before imposing (FA07). Both native drift and the complete external residual are included.

## 5. Positive lower bound and exact rational margin

Let \(u=\nu t\), \(\rho=\sigma_{\rm ext}/\nu\). Reverse triangle gives

\[
\|U(t)\|_{CR}\ge\frac{A_0}{\nu}B(u,\rho),\qquad
B(u,\rho)=2u-\sinh u-\frac{\rho u^2}{2}.
\tag{FA20}
\]

This remains true when its right side is negative, but squaring such a negative lower bound would be invalid. **Only for \(B(u,\rho)>0\)** can we conclude

\[
\frac{E_{\rm out}(t)}{C_{\rm joint}}\ge
\frac{\alpha_N|f_0|^2}{k^2R^2C_{\rm joint}}B(u,\rho)^2,
\qquad
\frac{A_0^2}{2\nu^2}=\frac{\alpha_N|f_0|^2}{k^2R^2}.
\tag{FA21}
\]

Capacity is positive by (FA05). The factor \(1/2\) comes from the original stock, \(\|U\|_{CR}^2/2\); no scaled-time stock factor has entered.

At \(u=1\), (FA07) gives \(B(1,\rho)\ge7/4-\sinh1\). To prove a positive bound exactly, write \(a_j=1/(2j+1)!\). For \(j\ge1\),
\[
\frac{a_{j+1}}{a_j}=\frac1{(2j+2)(2j+3)}\le\frac1{20},
\]
with equality at \(j=1\) and strictly smaller subsequent ratios. The positive tail starting at \(a_1=1/6\) is therefore strictly below its geometric majorant:

\[
\sinh1<1+\frac{1/6}{1-1/20}=\frac{67}{57}<\frac{19}{16},
\qquad
\frac{19}{16}-\frac{67}{57}=\frac{11}{912}>0.
\tag{FA22}
\]

Consequently
\(B(1,\rho)\ge7/4-\sinh1>7/4-19/16=9/16>0\).
This licenses (FA21), including at equality in the parameter condition.

Using (FA05), the phase-dependent factor and exact cosine comparison are

\[
\begin{aligned}
\frac{\alpha_N|f_0|^2}{k^2R^2C_{\rm joint}}
&=\frac5{12}\frac{\sin^2\phi}{1-\cos\phi}
=\frac5{12}(1+\cos\phi)>\frac{13}{16},\\
3-\left(\frac{161}{100}\right)^2
&=\frac{4079}{10000}>0,\qquad
\cos^2(\pi/12)=\frac{2+\sqrt3}{4}>
\frac{2+161/100}{4}=\left(\frac{19}{20}\right)^2 .
\end{aligned}\tag{FA23}
\]

Positive square roots give \(\cos(\pi/12)>19/20\). Since cosine is strictly decreasing on \([0,\pi/12]\), every admitted phase has \(\cos\phi>19/20\); and \((5/12)(1+19/20)=13/16\). Cancellation of \(1-\cos\phi\) is legitimate because \(\phi>0\).

Combining these strictly positive bounds proves

\[
\frac{E_{\rm out}(1/\nu)}{C_{\rm joint}}>
\frac{13}{16}\left(\frac9{16}\right)^2
=\frac{1053}{4096}
=\frac14+\frac{29}{4096}>\frac14 .
\tag{FA24}
\]

Multiplication by \(C_{\rm joint}>0\) proves (FA08). The entire certificate is finite and exact; no decimal approximation, asymptotic remainder or computed trajectory is needed.

## 6. A nonempty finite positive regime

Both rates are positive, so squaring the condition is an equivalence. Substitution of (FA06) and multiplication by the positive factor \(8\alpha_N/(mk^2R^2)\) give exactly

\[
\sigma_{\rm ext}\le\frac\nu2
\quad\Longleftrightarrow\quad
\eta_N^2\ge
\frac{8\alpha_N}{mk^2R^2}
\left(\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}\right).
\tag{FA25}
\]

For any fixed admitted geometry and fixed finite positive \(c,\kappa,\alpha_N,\beta_R,G\), the right side is positive and finite. Choose \(\eta_N\) as its positive square root, or any larger finite number, **once before choosing the phase**, and keep it constant. This constructs a nonempty regime with genuinely positive propagation and receiver coupling, including the allowed equality case. No new physical/geometric choice, feedback modification or coefficient limit is required.

Since \(R^2=3\) numerically in this family, and \(k,m,d\) depend only on fixed registration/profiles, neither condition (FA25) nor \(t_*=1/\nu\) depends on \(\phi\). The theorem compares separately prepared trajectories with the same fixed coefficients. It does not select coefficients along one trajectory, and it asserts no threshold optimization.

## 7. Units

P1 §1, Table 2, and P3 Appendix A, Table 1 (p. 14), use carrier amplitude \(\mathrm U\), length \(\mathrm L\), exchange time \(\mathrm T\) and native amplitude \(\mathrm A_{\rm amp}\). Normalized numerical identities in (FA05) use one native amplitude unit; restoring it attaches the corresponding powers to those launch identities. In particular \(R\) has an amplitude dimension although its normalized numerical value is \(\sqrt3\).

| Quantity | Dimension |
| --- | --- |
| \(x,R\) | \(\mathrm A_{\rm amp}\) |
| \(k,K\) | \(\mathrm U\mathrm L/(\mathrm T\mathrm A_{\rm amp}^2)\) |
| \(J\) | \(\mathrm U\mathrm L/(\mathrm T\mathrm A_{\rm amp})\) |
| \(p,r_c,y\) | \(\mathrm U\) |
| \(f,z\) | \(\mathrm U\mathrm L/\mathrm T\) |
| \(\alpha_N\) | \(\mathrm U^2\mathrm L/\mathrm A_{\rm amp}^2\) |
| \(\beta_R\) | \(\mathrm T^2/\mathrm L\) |
| \(\eta_N,\kappa\) | \(1\) |
| \(m,d,c\) | \(\mathrm L^{-1},\mathrm L^{-3},\mathrm L/\mathrm T\) |
| \(\|U\|_{CR}\), \(A_0\) | \(\mathrm U\mathrm L^{1/2}\), \(\mathrm U\mathrm L^{1/2}/\mathrm T\) |
| \(\nu,\sigma_{\rm ext}\), \(t_*\) | \(\mathrm T^{-1},\mathrm T^{-1}\), \(\mathrm T\) |
| \(E_{\rm out},C_{\rm joint}\) | \(\mathrm U^2\mathrm L\) |

Explicitly, \([mk^2R^2/\alpha_N]=\mathrm T^{-2}\),
\([c^2d/m]=\mathrm T^{-2}\) and
\([\kappa^2m/\beta_R]=\mathrm T^{-2}\).
Thus both squared rates have inverse-time-squared units, (FA20)'s bracket is dimensionless, and (FA25)'s right side is dimensionless like \(\eta_N^2\). Keeping \(R^2\) is essential to these cancellations.

These are commensurability checks, not physical calibration. Neither rate identifies native frequency, \(F\)-step cadence or completed carrier circulation.

## 8. Interpretation and limits

The theorem certifies actual combined external stock at one time, exceeding a quarter of the **joint ceiling**, not of the whole initial native stock. In the normalized family,

\[
\frac{C_{\rm joint}}{H_N(0)}
=\frac{\alpha_N(1-\cos\phi)}{3\alpha_N/2}
=\frac23(1-\cos\phi).
\tag{FA26}
\]

The fraction is uniform over the admitted phase range at the same coefficients and time. The absolute stock nevertheless tends to zero as \(\phi\downarrow0\), since the inherited upper bound gives
\(0\le E_{\rm out}(t_*)\le\alpha_N(1-\cos\phi)\to0\).
The zero-drive endpoint is excluded; its zero capacity is never used as a denominator.

No receiver share, later recovery of this amount, monotonic extraction, time of maximum stock or ceiling saturation is established. The inherited empty-launch account also keeps \(H_N(t)\le H_N(0)\). P3's \(\mathcal A_\kappa=M_\kappa/C_{\rm inv}\) retains its original denominator and compact window. This investigation states the direct inequality for \(E_{\rm out}(1/\nu)/C_{\rm joint}\) without reassigning that symbol.

P3's \(80/81\) receiving/recovery guarantees and P2's native-credit witness retain their own sufficient hypotheses. Their overlap with (FA25) on the same solution has not been proved here; those guarantees are not attached to the new amount. That question is outside this order.

The author's central meeting region, opposed cones, outward spreading and curved around–inward return remain the motivation. Stationary supports and possible transfer elsewhere are retained. Carrier circle versus tight toroid, close original sphere versus extended-line sphere, and host-notch \(N\) regions versus central broken \(G\) boundaries remain distinct. This norm comparison assigns no spatial route, opening, physical receiving location or diversion coefficient. The tentative 15–20%, possibly more, remains geometric intuition.

The agenda continues toward useful accessible amount and attainability, then native \(F\)/exchange cadence, intended-route correspondence and six-opening transport, with linked gravity–magnetism and later outer geometry and justified SRG integration. Three-Way remains parked. This task ends at the one theorem and its review package.

## 9. Evidence and disposition

The written proof carries the strong-regularity, zero-norm, positive-kernel, vanishing-remainder and strict-inequality arguments. The independently written **exact_checks.py** checks **eight** focused exact-algebra groups using installed SymPy 1.14.0 under conda torment Python 3.11.15. These cover the weighting, native derivative/rate coefficient, both residuals and weighted norm, comparison integration, capacity normalization, rational certificates, positive final margin, and finite-regime/units equivalence. Software does not replace the functional-analytic proof.

No supplied readiness script, previous 18 AT/12 PC suite, numerical trajectory or parameter scan was run. No installation, accepted-source edit, Git operation, new manuscript or publication occurred. Preservation records protect only their explicitly inventoried input scope; they claim neither an unrelated-worktree audit nor fresh remote retrieval.

**Established unchanged:** all proposed hypotheses, rates, phase quantifiers, time \(1/\nu\) and the strict \(1053/4096\) constant stand. There is no necessary mathematical correction or added assumption. GPT review of this new result and package remains pending.

## Primary sources

- **P1:** Hilmir Frímann Halldórsson, *A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model*, v0.1, [immutable edition](https://github.com/pzychozen/trioctagon-physics/tree/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1). Selected exact sources: inputs/published/P1/, especially manuscript/candidate.tex and manuscript/wellposed.tex.
- **P2:** Hilmir Frímann Halldórsson, *Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate*, v0.1, [immutable edition](https://github.com/pzychozen/trioctagon-physics/tree/28e8a85c8fe1e6321328d4d7285b2560d1f98aa9/papers/SAME_TRAJECTORY_NATIVE_CREDIT/publication/v0.1). Its Theorem 3.1 supplies prior behavior, not a return conclusion in this regime. Selected sources: inputs/published/P2/.
- **P3:** Hilmir Frímann Halldórsson, *Recoverable Transfer and Projection Capacity in the Reciprocal Chiral Exchange Candidate*, v0.1, [immutable edition](https://github.com/pzychozen/trioctagon-physics/tree/54c0f6c419fa681e2c1e74a5ad2bb46df787bb93/papers/RECOVERABLE_TRANSFER_AND_PROJECTION_CAPACITY/publication/v0.1). Current accepted baseline; selected exact sources: inputs/published/P3/.

The supplied inputs/SOURCE_ASSESSMENT.md (A1)–(A16) is GPT's **proposed** route, independently assessed above. Its preparatory checks and hashes were not treated as acceptance or proof. The accompanying claim/source ledger separates all inherited facts and new steps with exact locators.
