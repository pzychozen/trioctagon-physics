# NATIVE_CAPACITY_RECEIVING_RECOVERY_01 — independent proof

Research author: Hilmir Frímann Halldórsson (pzychozen). Proposal: GPT. Independent investigation: Codex. Date: 5 November 2026.

**Disposition: established unchanged, conditional only on the explicitly inherited candidate-model hypotheses below.** Every proposed PR01–PR23 obligation is covered. No correction to the proposed phase cutoff, coefficient regime, error constant, times or fractions is necessary. This is an investigation submitted for GPT's review, not an already accepted result or a manuscript.

## 1. Model, quantifiers and conclusion

Write \(\alpha=\alpha_N>0,\ \beta=\beta_R>0,\ \eta=\eta_N>0\), and \(\kappa=\eta_R>0\). These are merely abbreviations for the original coefficients. All coefficients are finite, constant in exchange time and selected before the phase. Keep the original registration gains, put \(G=\kappa_{\rm in}\lambda_g>0\), and fix yaw \(\delta_g=\pi/4\). The raw two-port order is \(+,-\). The unchanged equations are

\[
\begin{split}
 x&=(a,b),\quad \Omega=a+ib,\quad f(x)=K(a\times b),\quad J(x)=D_xf(x),\\
 K&=\frac{G}{\sqrt7}
 \begin{pmatrix}\sqrt2&\sqrt2&\sqrt3\\ \sqrt2&\sqrt2&-\sqrt3\end{pmatrix},\\
 \dot x&=-\frac{\eta}{2\alpha}J(x)^Ty,\qquad
 p_t+c(r_c)_s=\mathcal B(\eta f(x)-\kappa z),\\
 (r_c)_t+cp_s&=0,\qquad
 \dot z=\frac{\kappa}{\beta}y,\qquad y=\mathcal B^*p.
\end{split}\tag{RR01}
\]

The carrier is the admitted finite periodic circle of length \(L_c\), with \(c>0\). Contacts \(s_\pm=L_c/2\mp\eta_{\rm geom}\) have **whole-circle shortest separation** \(2\eta_{\rm geom}\); thus \(2\eta_{\rm geom}\le L_c/2\). Retain \(0<\epsilon_c<\eta_{\rm geom}\). The profiles and ports are

\[
\begin{split}
 b_\sigma(s)&=\epsilon_c^{-1}
 \left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
 \qquad \mathcal Bq=b_+q_++b_-q_-,\\
 \mathcal B^*p&=\left(\int b_+p\,ds,\int b_-p\,ds\right)^T,\qquad
 m=\frac{2}{3\epsilon_c},\quad d=\frac{2}{\epsilon_c^3},\\
 \mathcal B^*\mathcal B&=mI_2,\quad
 \|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\quad
 \|\partial_s\mathcal Bq\|_2=\sqrt d\,|q|.
\end{split}\tag{RR02}
\]

Integrals cover the entire circle. The separation condition ensures disjoint supports even across the periodic seam. Each continuous tent belongs to periodic \(H^1\), and its first weak derivative belongs to \(L^2\). Direct integration of its two affine halves gives RR02; disjointness removes derivative cross terms as well. No second weak derivative in \(L^2\) is presumed.

The original trial stores, rather than the auxiliary norm used later, define every conclusion:

\[
 H_N=\frac{\alpha}{2}(|a|^2+|b|^2),\quad
 H_C=\frac12(\|p\|_2^2+\|r_c\|_2^2),\quad
 H_R=\frac{\beta}{2}|z|^2,\quad E_{\rm out}=H_C+H_R.
\tag{RR03}
\]

In the published normalized native-amplitude convention, put \(R=\sqrt3\), \(k=\|K\|=G\sqrt{8/7}\), and choose the fixed coefficients to satisfy

\[
\begin{gathered}
 \nu^2=\frac{\eta^2mk^2R^2}{2\alpha},\qquad
 \sigma_{\rm ext}^2=\frac{c^2d}{m}+\frac{\kappa^2m}{\beta},\\
 \gamma=c\sqrt{d/m},\qquad
 \omega_R=\kappa\sqrt{m/\beta}=\frac{\nu}{3},
 \qquad 0<\frac{\gamma}{\nu}\le\frac1{100},\\
 0<\phi\le\frac1{100},\qquad
 \Omega_0=(1,e^{i\phi},1),\qquad p_0=r_{c,0}=z_0=0,\\
 C=C_{\rm joint}=\alpha(1-\cos\phi)>0,\qquad
 \omega_N=\sqrt{5/6}\,\nu,\quad
 \varpi=\sqrt{17/18}\,\nu,\quad
 t_A=\nu^{-1},\quad t_R=\pi/\varpi,\quad t_F=2\pi/\varpi .
\end{gathered}\tag{RR04}
\]

Angles are in radians. The quantifiers are: for every admitted fixed geometry, scales and registration, and every fixed coefficient tuple satisfying RR04, the following holds for **every** phase in its declared interval, on that phase's single unique actual solution. Section 9 constructs such tuples without a limiting process. The times are phase independent for that tuple.

**Theorem.** On the actual positive-speed, positive-receiver-coupling solution of RR01,

\[
\begin{gathered}
 0<t_A<t_R<t_F,\qquad E_{\rm out}(t_A)>\frac{1053}{4096}C,\\
 H_R(t_R)>\frac C4,\qquad H_C(t_R)<\frac C{100},
 \qquad E_{\rm out}(t_F)<\frac C{100}.
\end{gathered}\tag{RR05}
\]

Writing \(E_A=E_{\rm out}(t_A), E_R=E_{\rm out}(t_R), E_F=E_{\rm out}(t_F)\), all denominators below are positive, and

\[
\begin{gathered}
 \frac{25}{26}<\frac{H_R(t_R)}{E_R}\le1,\qquad
 0\le\frac{H_R(t_F)}{H_R(t_R)}<\frac1{25},\\
 \frac{24}{25}<
 \mathcal R_A:=\frac{H_N(t_F)-H_N(t_A)}{E_A}\le1,\qquad
 \frac{24}{25}<
 \mathcal R_R:=\frac{H_N(t_F)-H_N(t_R)}{E_R}\le1,\\
 H_N(t_F)-H_N(t_R)>\frac6{25}C.
\end{gathered}\tag{RR06}
\]

These are stock and net-recovery accounts between specified times. They do not follow a tagged energy cohort or imply monotonic behavior.

## 2. Inherited existence, accounts and capacity

P1, Theorem 3.1 (label thm:global), supplies the unique global solution of the closed equations. Empty carrier preparation is in \(H^1_{\rm per}\), so
\((p,r_c)\in C(\mathbb R;H^1_{\rm per})^2\cap C^1(\mathbb R;L^2)^2\), with \(a,b,z\in C^1\). This inheritance precedes all estimates in this proof. Shifting \(a\) by a fixed vector preserves that regularity.

To check the native signs directly, set \(w=K^Ty,\ \mu=\eta/(2\alpha)\). Differentiating \(f\) gives \(J^Ty=(b\times w,w\times a)\), hence
\(\dot a=\mu w\times b,\ \dot b=-\mu w\times a\). The homogeneous quadratic identity \(J(x)x=2f(x)\), integration of the periodic carrier product derivative, and the receiver ODE give

\[
\begin{gathered}
 P_{NC}=\eta f(x)^Ty,\qquad P_{CR}=\kappa z^Ty,\\
 \dot H_N=-P_{NC},\qquad
 \dot H_C=P_{NC}-P_{CR},\qquad
 \dot H_R=P_{CR},\\
 H_N(t)+H_C(t)+H_R(t)=H_N(0),\qquad
 E_{\rm out}(t)=H_N(0)-H_N(t).
\end{gathered}\tag{RR07}
\]

All powers are continuous: finite coordinates and \(y=\mathcal B^*p\) are continuous. These are P1's original accounts, not a new balance law. Nonnegative stores also give \(|x(t)|\le R\).

P3, Theorem 3.1 (thm:projection), gives the joint invariant ceiling. For the present yaw and launch its strict-witness calculation gives

\[
\begin{gathered}
 f_{0,\pm}=\frac{G\sin\phi}{\sqrt7}(-\sqrt2\pm\sqrt3),\qquad
 |f_0|^2=\frac{10G^2\sin^2\phi}{7}>0,\\
 0\le E_{\rm out}(t)\le C=\alpha(1-\cos\phi)\quad(t\ge0).
\end{gathered}\tag{RR08}
\]

The phase lies inside \((0,\pi/12)\), as follows also from the elementary bound on \(\pi\) in section 7.1. The joint ceiling holds in the full native space; this proof never assumes the initially coherent family is invariant under evolution. P4's access theorem will be used only after its rate condition is checked in section 8.

## 3. Independent compatibility audit of the older sufficient certificates

Use the notation of P3's transfer section only in this paragraph:
\(\omega=\sqrt{m/\beta}, S=2\pi/\omega,\Lambda=\sqrt\beta\,|f_0|,\)
\(F_{\max}=kR^2/2,\ A=\nu^2F_{\max}/2,\)
\(B_2=\sqrt m\,AS^3/3\).
P1's cross-product bound \(|f(x)|\le k|x|^2/2\) gives \(F_{\max}\ge|f_0|>0\). For \(0<q\le1/5\), the \(B_2\) term of P3's sufficient threshold implies

\[
 \kappa^2\ge\frac{2B_2}{q\Lambda}
 \quad\Longrightarrow\quad
 \left(\frac{\kappa\omega}{\nu}\right)^2
 \ge\frac{8\pi^3F_{\max}}{3q|f_0|}
 \ge\frac{8\pi^3}{3q}>\frac14.
\tag{RR09}
\]

The substitution uses \(\sqrt m/\sqrt\beta=\omega\); every divided quantity is positive. For example \(\pi>1,\ 1/q\ge5\) already makes the last bound exceed \(40/3\). In contrast P4 requires
\(\gamma^2+(\kappa\omega)^2\le\nu^2/4\), so \((\kappa\omega/\nu)^2\le1/4\). The sufficient certificate regimes therefore cannot overlap. This is not an impossibility theorem for the behaviors themselves. Neither P3's 80/81 fraction nor P2's returning-power witness is imported into the new regime.

## 4. Tangent geometry, exact remainder and forced norm estimate

Set \(v=(1,1,1)\), \(e=(1,-1,0)/\sqrt2\), \(u=a-v\), and let \([v]_\times q=v\times q\). Direct multiplication of the unchanged rank-two \(K\) gives

\[
\begin{gathered}
 D=K[v]_\times
 =\frac G{\sqrt7}
 \begin{pmatrix}
 \sqrt2-\sqrt3&-\sqrt2+\sqrt3&0\\
 \sqrt2+\sqrt3&-\sqrt2-\sqrt3&0
 \end{pmatrix}
 =\ell e^T,\\
 \ell=De=\frac G{\sqrt7}\binom{2-\sqrt6}{2+\sqrt6},
 \quad |\ell|^2=\frac{20G^2}{7},\quad Ke=0,\quad
 \omega_N^2=\frac{\eta^2m|\ell|^2}{2\alpha}=\frac56\nu^2 .
\end{gathered}\tag{RR10}
\]

Thus \(D\) is rank one; \(K\) stays rank two. This tangent factorization does not remove the exact nonlinear drive \(K(u\times b)\).

For \(Y=(u,b,p,r_c,z)\) define a Hilbert norm and its associated inner product by

\[
 \|Y\|_*^2=2\alpha(|u|^2+|b|^2)
             +\|p\|_2^2+\|r_c\|_2^2+\beta|z|^2.
\tag{RR11}
\]

This proof norm is not the native store, not the total physical/trial store, and not asserted to be conserved by the nonlinear dynamics. With domain consisting of \(H^1_{\rm per}\) carrier coordinates and unrestricted finite coordinates, define

\[
 \mathscr A_cY=
 \left(0,-\mu D^Ty,
 -c(r_c)_s+\eta\mathcal BDb-\kappa\mathcal Bz,
 -cp_s,\frac{\kappa}{\beta}y\right).
\tag{RR12}
\]

Since \(D^Ty=w\times v\), the tangent native contribution to the weighted inner product is \(-2\alpha\mu(Db)^Ty=-\eta(Db)^Ty\). The full cancellation is

\[
\begin{split}
 \langle Y,\mathscr A_cY\rangle_*
 &=-\eta(Db)^Ty+\eta y^TDb
 -c\int[p(r_c)_s+r_cp_s]\,ds
 -\kappa y^Tz+\kappa z^Ty=0 .
\end{split}\tag{RR13}
\]

The periodic \(H^1\) product rule makes the spatial integral zero. This verifies in particular the factor \(2\alpha\); using \(\alpha\) instead would leave an uncancelled tangent term.

For an already strong curve \(Z\) satisfying \(\dot Z=\mathscr A_cZ+F\), differentiate \((\|Z\|_*^2+\delta^2)^{1/2}\) for \(\delta>0\). RR13 and Cauchy–Schwarz bound its derivative above by \(\|F\|_*\). Integrating and letting \(\delta\downarrow0\) gives

\[
 \|Z(t)\|_*\le\|Z(0)\|_*+\int_0^t\|F(s)\|_*\,ds,\qquad t\ge0 .
\tag{RR14}
\]

This argument includes zero norm, requires no division by that norm, and does not infer existence from skew cancellation.

The exact native cross-product equations from section 2 and
\(f=Db+K(u\times b)\) give the exact decomposition

\[
 \dot Y=\mathscr A_cY+\mathscr N(Y),\qquad
 \mathscr N(Y)=
 \left(\mu w\times b,-\mu w\times u,
       \eta\mathcal BK(u\times b),0,0\right).
\tag{RR15}
\]

There is no discarded term in RR15. To bound it, set
\(X_N=\sqrt{2\alpha}\sqrt{|u|^2+|b|^2}\),
\(V_{\rm ext}^2=\|p\|_2^2+\|r_c\|_2^2+\beta|z|^2\), and
\(L=\eta k\sqrt m/(2\alpha)\).
Then \(|w|\le k\sqrt m\,V_{\rm ext}\). The weighted native remainder is at most \(LX_NV_{\rm ext}\); its external remainder is at most
\(\eta k\sqrt m\,|u||b|\le (L/2)X_N^2\).
These are orthogonal blocks of RR11, so

\[
\begin{split}
 \|\mathscr N(Y)\|_*^2
 &\le L^2\left(X_N^2V_{\rm ext}^2+\frac14X_N^4\right)
 \le L^2(X_N^2+V_{\rm ext}^2)^2,\\
 \|\mathscr N(Y)\|_*&\le L\|Y\|_*^2.
\end{split}\tag{RR16}
\]

The second squared inequality has the nonnegative gap
\(3X_N^4/4+X_N^2V_{\rm ext}^2+V_{\rm ext}^4\).
Thus the proposed deliberately conservative quadratic bound holds globally.

## 5. Exact initial data and a legitimate scalar majorant

No first-order phase approximation is made:

\[
 u_0=(0,\cos\phi-1,0),\quad b_0=(0,\sin\phi,0),\quad
 \|Y(0)\|_*^2
 =2\alpha[(\cos\phi-1)^2+\sin^2\phi]=4C .
\tag{RR17}
\]

Write \(y_0=2\sqrt C>0\). The actual global strong solution, RR14 and RR16 imply
\(\|Y(t)\|_*\le y_0+L\int_0^t\|Y(s)\|_*^2ds=:Q(t)\).
Here \(Q\) is positive and continuously differentiable on every finite time interval, \(Q(0)=y_0\), and \(Q'\le LQ^2\). Hence
\((1/Q)'=-Q'/Q^2\ge-L\), so \(1/Q(t)\ge1/y_0-Lt\). Only where the right side is positive may we invert it, obtaining

\[
 \|Y(t)\|_*\le Q(t)\le\frac{y_0}{1-Ly_0t}
 \quad\hbox{for }0\le t<(Ly_0)^{-1}.
\tag{RR18}
\]

This establishes the positive-denominator comparison without assuming a bootstrap bound or constructing the solution from this estimate. Section 7.1 proves \(Ly_0t_F<1/25\) directly from the fixed parameters before using RR18 up to \(t_F\).

## 6. Complete moving-native reference

Define \(Y^{(0)}\) by the linear equation \(\dot Y^{(0)}=\mathscr A_0Y^{(0)}\), with the exact same initial deviation RR17. Only this reference removes propagation and the quadratic remainder. The actual \(c,\kappa\) stay positive and unchanged.

Let \(n=\ell/|\ell|\) and \(h_0=e^Tb_0=-\sin\phi/\sqrt2\). The inactive part is
\(b_\perp=b_0-h_0e=(\sin\phi/2,\sin\phi/2,0)\), with \(Db_\perp=0\). Embed the reference as

\[
\begin{gathered}
 u^{(0)}(t)=u_0,\qquad
 b^{(0)}(t)=b_\perp+e\,X(t)/\sqrt{2\alpha},\\
 p^{(0)}(t)=\mathcal Bn\,P(t)/\sqrt m,\qquad
 r_c^{(0)}(t)=0,\qquad z^{(0)}(t)=nZ(t)/\sqrt\beta .
\end{gathered}\tag{RR19}
\]

Both static components are retained, including the component of \(u_0\) parallel to \(e\). Since \(D^Tn=|\ell|e\) and \(y^{(0)}=\sqrt m\,nP\), substitution of every block into \(\mathscr A_0\) gives

\[
 \dot X=-\omega_NP,\qquad
 \dot P=\omega_NX-\omega_RZ,\qquad
 \dot Z=\omega_RP,\qquad
 X_0=-\sqrt\alpha\sin\phi<0,\quad P_0=Z_0=0 .
\tag{RR20}
\]

The sign of \(X_0\) is negative, since \(0<\phi<\pi/2\). Solving this three-coordinate system gives

\[
\begin{split}
 X(t)&=X_0\frac{\omega_R^2+\omega_N^2\cos(\varpi t)}{\varpi^2},\\
 P(t)&=X_0\frac{\omega_N}{\varpi}\sin(\varpi t),\\
 Z(t)&=X_0\frac{\omega_N\omega_R}{\varpi^2}
                   [1-\cos(\varpi t)] .
\end{split}\tag{RR21}
\]

Differentiation verifies all three equations and all initial data; \(X^2+P^2+Z^2=X_0^2\). In particular,

\[
\begin{gathered}
 (p^{(0)},r_c^{(0)})(t_R)=0,\qquad
 (p^{(0)},r_c^{(0)},z^{(0)})(t_F)=0,\\
 \frac{X_0^2}{2}=C\cos^2(\phi/2),\qquad
 \frac{|Z(t_R)|}{\sqrt{2C}}
 =\frac{2\sqrt{30}}{17}\cos(\phi/2).
\end{gathered}\tag{RR22}
\]

The positive cosine permits \(|X_0|/\sqrt{2C}=\cos(\phi/2)\le1\). The reference is an explicitly strong curve: its carrier is a fixed \(H^1\) profile times a smooth scalar. No actual solution is restarted at either landmark, and \(t_F\) is not claimed to be an exact nonlinear period.

## 7. Finite error over the complete interval

### 7.1 Positive denominator and elementary strict constants

For completeness the elementary constants used here have exact certificates. Polynomial division gives

\[
\begin{gathered}
 \frac{22}{7}-\pi
 =\int_0^1\frac{s^4(1-s)^4}{1+s^2}\,ds>0,\\
 \frac1{1+s^2}-(1-s^2)=\frac{s^4}{1+s^2}>0\quad(0<s<1),
 \qquad \pi>8/3.
\end{gathered}\tag{RR23}
\]

For the first identity the quotient is \(s^6-4s^5+5s^4-4s^2+4\), whose integral is \(22/7\), and the remainder is \(-4\). Integrating \(4/(1+s^2)\) gives \(\pi\). Strict positivity on the open interval proves both inequalities. Thus \(1/100<\pi/12\) and \(\pi>1\).

Put \(T=t_F\) and \(\theta=Ly_0T=2L\sqrt C\,T\). Since \(1-\cos\phi=2\sin^2(\phi/2)\le\phi^2/2\),

\[
\begin{split}
 \nu T&=2\pi\sqrt{18/17}<20/3,\qquad 1/\sqrt3<3/5,\\
 \theta&=\frac{\sqrt2}{R}\sqrt{1-\cos\phi}\,\nu T
 \le\frac{\phi}{\sqrt3}\nu T<4\phi\le\frac1{25}.
\end{split}\tag{RR24}
\]

The first strict time bound follows by \(\pi<22/7\) and squaring positive quantities:
\((20/3)^2-(44/7)^2(18/17)=19568/7497>0\).
Similarly \((3/5)^2-1/3=2/75>0\). The elementary inequality \(|\sin q|\le|q|\) follows, for example, by integrating \(\cos q\). Thus \(1-Ly_0t\ge1-\theta>24/25\) for all \(0\le t\le T\), justifying RR18 on the entire required interval.

Also \(\varpi/\nu=\sqrt{17/18}<1<\pi\), so \(t_A<t_R\), and \(t_F=2t_R>t_R>0\).

### 7.2 Strong difference before residual estimation

The actual curve is strong by P1 and the shifted coordinates. The reference is strong by RR19–RR21. Therefore their difference \(E=Y-Y^{(0)}\) belongs to \(C_t\) of the stated \(H^1\) carrier domain and is \(C^1_t\) in the Hilbert norm **before** any error estimate. Subtracting their equations yields the exact identity in that Hilbert space:

\[
 \dot E=\mathscr A_cE+\mathscr N(Y)
          +(0,0,0,-c\partial_sp^{(0)},0),\qquad E(0)=0.
\tag{RR25}
\]

Indeed \((\mathscr A_c-\mathscr A_0)Y^{(0)}\) has zero first carrier residual because \(r_c^{(0)}=0\), and second carrier residual \(-c\partial_sp^{(0)}\). Native and receiver couplings are present in both operators. No receiver residual is omitted, and only the first weak derivative of a tent is used. In particular an unbounded-operator norm limit is neither used nor asserted.

Apply RR14 to RR25. RR16–RR18 and RR24 give

\[
\begin{split}
 \int_0^T\|\mathscr N(Y(t))\|_*\,dt
 &\le\int_0^T\frac{Ly_0^2}{(1-Ly_0t)^2}\,dt
 =\frac{y_0\theta}{1-\theta},\\
 \int_0^T c\|\partial_sp^{(0)}(t)\|_2\,dt
 &=\int_0^T\gamma|P(t)|\,dt
 =\frac{4\gamma|X_0|\omega_N}{\varpi^2}
 \le\sqrt{2C}\frac{4\gamma\omega_N}{\varpi^2}.
\end{split}\tag{RR26}
\]

Here \(\|\partial_s\mathcal Bn\|_2=\sqrt d\), and
\(\int_0^{2\pi}|\sin q|\,dq=4\) by splitting into its two signed half-periods. These are integrals of nonnegative quantities; the full-\(T\) bound also bounds their integrals to every earlier time. Dividing by the positive \(\sqrt{2C}\) yields the uniform finite-error estimate

\[
 \sup_{0\le t\le T}\frac{\|E(t)\|_*}{\sqrt{2C}}
 \le\frac{\sqrt2\,\theta}{1-\theta}
                  +\frac{4\gamma\omega_N}{\varpi^2}.
\tag{RR27}
\]

### 7.3 Exact margins, including the endpoints of the parameter range

The positive propagation coefficient satisfies
\[
 \frac{4\gamma\omega_N}{\varpi^2}
 =\frac{72}{17}\sqrt{5/6}\frac{\gamma}{\nu}
 <4\frac{\gamma}{\nu}\le\frac1{25},
\]
because \(16-(72/17)^2(5/6)=304/289>0\).
Also \(\sqrt2<10/7\), since \((10/7)^2-2=2/49>0\).
Using the strict \(\theta<1/25\) and the increasing function \(\theta/(1-\theta)\) on \([0,1)\), RR27 gives

\[
 \sup_{0\le t\le t_F}\frac{\|E(t)\|_*}{\sqrt{2C}}
 <\frac{10}{7}\frac1{24}+\frac1{25}
 =\frac5{84}+\frac1{25}
 =\frac{209}{2100}<\frac1{10},
 \qquad \frac1{10}-\frac{209}{2100}=\frac1{2100}>0.
\tag{RR28}
\]

All strict inequalities survive \(\phi=1/100\) and \(\gamma/\nu=1/100\). No coefficient depends on \(\phi\); the bound is uniform over the declared phase interval at one fixed coefficient choice. The excluded case \(\phi=0\) would have \(C=0\), so none of the normalized divisions is made there.

## 8. Transfer to the actual stocks and all denominators

The weighted receiver norm of the reference at \(t_R\) is \(\sqrt\beta|z^{(0)}(t_R)|=|Z(t_R)|\). Its strict lower bound follows from

\[
\begin{gathered}
 \frac{2\sqrt{30}}{17}>\frac58,\qquad
 \frac{120}{289}-\frac{25}{64}=\frac{455}{18496}>0,\\
 \cos(\phi/2)\ge1-\frac{\phi^2}{8}
 \ge\frac{79999}{80000}>\frac{24}{25},\qquad
 \frac{79999}{80000}-\frac{24}{25}=\frac{3199}{80000}>0,\\
 \frac{\sqrt\beta|z^{(0)}(t_R)|}{\sqrt{2C}}>\frac35 .
\end{gathered}\tag{RR29}
\]

The carrier projection, the weighted receiver projection, and their joint external projection are contractive for RR11. Reverse triangle at \(t_R\), with RR28, therefore gives
\(\sqrt\beta|z(t_R)|>(3/5-1/10)\sqrt{2C}=(1/2)\sqrt{2C}>0\).
The lower bound is positive **before** it is squared. The reference carrier is zero at \(t_R\) and its entire external state is zero at \(t_F\). Accordingly

\[
\begin{gathered}
 H_R(t_R)=\tfrac12(\sqrt\beta|z(t_R)|)^2>C/4,\\
 H_C(t_R)=\tfrac12\|(p,r_c)(t_R)\|_2^2<C/100,\qquad
 E_F=\tfrac12\|(p,r_c,z)(t_F)\|_{CR}^2<C/100 .
\end{gathered}\tag{RR30}
\]

This converts auxiliary error into the original stores with their original factors \(1/2\).

For exactly these fixed actual coefficients,

\[
 \frac{\sigma_{\rm ext}^2}{\nu^2}
 =\left(\frac{\gamma}{\nu}\right)^2+\frac19
 \le\frac1{10000}+\frac19<\frac14,\qquad
 \frac14-\left(\frac1{10000}+\frac19\right)=\frac{12491}{90000}>0.
\tag{RR31}
\]

All other hypotheses of P4, Theorem 3.1 (thm:access), have already been checked: fixed yaw, profiles and finite positive coefficients; normalized coherent empty launch; \(\phi\in(0,\pi/12)\). Applying its original certificate gives \(E_A>1053C/4096\) on this same actual solution at \(t_A=1/\nu\).

Thus \(C>0,\ H_R(t_R)>C/4>0,\ E_R\ge H_R(t_R)>C/4>0,\) and \(E_A>1053C/4096>0\). These establish every normalization denominator. With \(H_C(t_R)\ge0\), \(H_R(t_F)\le E_F\), and RR30,

\[
 \frac{H_C(t_R)}{H_R(t_R)}<\frac1{25},\qquad
 \frac{H_R(t_R)}{E_R}
 =\frac1{1+H_C(t_R)/H_R(t_R)}>\frac{25}{26},\qquad
 0\le\frac{H_R(t_F)}{H_R(t_R)}<\frac1{25}.
\tag{RR32}
\]

The first receiving-share ratio is at most one. Conservation RR07 now gives

\[
\begin{split}
 \mathcal R_A&=1-\frac{E_F}{E_A}>
 1-\frac{4096}{105300}
 =\frac{25301}{26325}>\frac{24}{25},
 \qquad \frac{25301}{26325}-\frac{24}{25}=\frac{29}{26325}>0,\\
 \mathcal R_R&=1-\frac{E_F}{E_R}>1-\frac1{25}=\frac{24}{25},\\
 H_N(t_F)-H_N(t_R)&=E_R-E_F>
 \left(\frac14-\frac1{100}\right)C=\frac6{25}C .
\end{split}\tag{RR33}
\]

Both recovery fractions are at most one because \(E_F\ge0\) and their denominators are positive. This proves RR05–RR06 in full.

For interpretation only, RR07 also gives positive integrated receiver supply on \((0,t_R)\), negative integrated receiver supply on \((t_R,t_F)\), and negative integrated native supply on \((t_R,t_F)\). For example \(H_R(t_F)<H_R(t_R)\) follows from RR30, and \(H_N(t_F)>H_N(t_R)\) from RR33. Continuity of each power then guarantees a nonempty open interval of the corresponding strict sign within the relevant window. The receiver and native intervals are not asserted to coincide. No exact-time power sign, first return, maximum-stock time or monotonic window follows from these integrated statements.

## 9. Nonempty finite parameter family

Fix any admitted finite geometry and finite positive \(c,\alpha,\beta,G\). Then \(k,m,d,R\) are finite and positive. Choose any finite
\(\nu_{\rm target}\ge100c\sqrt{d/m}>0\), and set once, before choosing a phase,

\[
 \eta=\frac{\nu_{\rm target}\sqrt{2\alpha}}{kR\sqrt m}>0,
 \qquad
 \kappa=\frac{\nu_{\rm target}}3\sqrt{\frac{\beta}{m}}>0 .
\tag{RR34}
\]

Substitution gives \(\nu=\nu_{\rm target}\), \(\omega_R=\nu/3\), and \(0<\gamma/\nu\le1/100\). Both couplings are finite and constant on every trajectory in the declared family. This is a sufficient subfamily, without a zero-speed actual system, infinite-coupling limit, altered feedback, reset, profile change or parameter scan.

## 10. Dimensions and restoration of native amplitude

Use the source's abstract carrier units \(\mathrm U,\mathrm L,\mathrm T\) and bookkeeping native amplitude unit \(\mathrm A\). The normalized numeric launch above uses a unit amplitude \(A_*\) whose numeric value is one; restoring it means

\[
\begin{gathered}
 v=A_*(1,1,1),\quad \Omega_0=A_*(1,e^{i\phi},1),\quad R=\sqrt3\,A_*,\\
 D=K[v]_\times,\quad |\ell|^2=\frac{20G^2A_*^2}{7},\quad
 C=\alpha A_*^2(1-\cos\phi),\quad
 X_0=-\sqrt\alpha\,A_*\sin\phi,\quad y_0=2\sqrt C.
\end{gathered}\tag{RR35}
\]

The directions \(e,n\) remain dimensionless. All initial deviations acquire the same factor \(A_*\). The definitions retain \(R^2\) in \(\nu^2\) and the amplitude of \(v\) in \(D\), so \(\omega_N^2/\nu^2=5/6\) remains dimensionless and unchanged.

| Quantity | Dimension |
|---|---|
| \(a,b,u,v,R,A_*\) | \(\mathrm A\) |
| \(K,k,G\) | \(\mathrm U\mathrm L/(\mathrm T\mathrm A^2)\) |
| \(D,\ell,J\) | \(\mathrm U\mathrm L/(\mathrm T\mathrm A)\) |
| \(p,r_c,y\) | \(\mathrm U\) |
| \(f,z\) | \(\mathrm U\mathrm L/\mathrm T\) |
| \(\alpha;\ \beta;\ \eta,\kappa\) | \(\mathrm U^2\mathrm L/\mathrm A^2;\ \mathrm T^2/\mathrm L;\ 1\) |
| \(m;\ d;\ c\) | \(\mathrm L^{-1};\ \mathrm L^{-3};\ \mathrm L/\mathrm T\) |
| \(\|Y\|_*,X,P,Z,\sqrt C\) | \(\mathrm U\sqrt{\mathrm L}\) |
| \(L\), the nonlinear-bound coefficient | \((\mathrm U\sqrt{\mathrm L}\,\mathrm T)^{-1}\) |
| \(\gamma,\nu,\omega_N,\omega_R,\varpi\) | \(\mathrm T^{-1}\) |
| \(\theta\) and all stock fractions | \(1\) |

Here \(L\), the named nonlinear coefficient, is distinct from the unit \(\mathrm L\) and circle length \(L_c\). In dimensional form the identity used in RR24 is

\[
 \theta=\frac{\sqrt2\,A_*}{R}\sqrt{1-\cos\phi}\,\nu T
 \le\frac{\phi}{\sqrt3}\nu T<\frac1{25}.
\tag{RR36}
\]

The factor \(A_*/R=1/\sqrt3\) must not be suppressed in a dimensional identity. Both expressions in RR34 are dimensionless couplings. Restoring amplitude changes none of the normalized fractions or error bounds. Commensurable trial stores are not an SI calibration, an exchange cadence or a physical clock.

## 11. Exact scope and remaining research limitations

No mathematical gap remains in the bounded proposed certificate under its stated hypotheses. It establishes a substantial fraction of the joint capacity in the receiver and later net native recovery on the same fixed-parameter trajectory that P4 certifies at \(t_A\). It does not classify all P4 tuples or show that P3's sufficient regime overlaps it. The auxiliary norm and oscillator are analytical devices.

The capacity fraction of the original native store is
\(C/H_N(0)=\frac23(1-\cos\phi)\to0\) as \(\phi\downarrow0\).
By RR08, actual external stocks and the positive net recovered amounts in RR33 are at most \(C\). They therefore tend to zero in absolute trial-storage units despite uniform fractional guarantees. This result proves neither ceiling saturation nor a large fraction of the whole initial native stock.

The receiver remains the published collocated conservative receiver, without an irreversible load or assigned material location. The reference landmarks are not asserted to be exact maxima, first return times or a nonlinear period. There is no tagged-cohort transport, exact nonlinear trajectory reconstruction or guaranteed sustained monotone receiving/recovery interval.

The central starting/meeting region, opposed cones, outward spreading, curved around-and-inward return, stationary supports and possible transfer elsewhere remain research intentions rather than conclusions of this energy account. The adopted carrier circle, intended tight toroid, close original sphere and extended-line sphere remain distinct, as do host-notch N regions and central broken G boundaries. The tentative 15–20% intuition is not a coefficient, denominator or target here.

After review, the remaining receiving/recovery questions must be assessed before any advance to native F/exchange cadence, central-route correspondence or six-opening transport. Gravity–magnetism remains linked; outer geometry, separate golden-ratio relationships and justified SRG integration remain later directions. Three-Way stays parked. Pi and Hoki-poki brainstorming are neither premises nor extra missions; RR23 is only an elementary numerical inequality.

## 12. Evidence and source status

P1–P4 are the exact supplied published mathematical sources, with immutable identities and labels enumerated in the accompanying claim/source ledger and SOURCE_IDENTITIES.json. P4 and its XW-01 closeout remain accepted and unchanged. The proposal in the incoming assessment has been challenged as new content, not used as an established premise.

The independently written exact_checks.py was executed using Command Prompt, conda environment torment, isolated Python with bytecode writing disabled. Its 14 groups passed; EXACT_ALGEBRA_RESULTS.json records the finite algebra/arithmetic, and EXACT_CHECK_EXECUTION.json records the actual environment and identities. Regularity, periodic Sobolev integration, norm regularization at zero, the scalar reciprocal comparison, quantified phase uniformity and positive-denominator reasoning are the written arguments above, not claims that symbolic checks prove a PDE theorem.

The supplied preparatory scientific script and historical scientific suites were not executed. Source verification used supplied records and separately retained prior closeout bytes; there was no fresh remote retrieval and no Git operation. The final preservation and package records specify the audited input scope. No manuscript, publication or successor investigation was produced.
