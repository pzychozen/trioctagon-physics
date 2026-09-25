# Transverse normal-form proof closeout

**RESEARCH_TRANSVERSE_NORMAL_FORM_CLOSEOUT_v0.1 — Codex, 25 September 2026**

Author: Hilmir Frímann Halldórsson. Scientific lead: GPT. New Codex derivations submitted for GPT review; this is not a new Claude review or joint acceptance.

The arbitrary-step coefficient system proves the four-rate law at the accepted parameters. Its exact sum is
\[
\boxed{\kappa_\infty=13375/1107936648
=0.000012071989877890563\ldots .}
\]
The missing minus sign in Claude §5 is a prose error in the displayed \(X_n\) solution. The independently derived increments and limiting expression agree with Claude's downstream formulas. Original evidence remains unchanged.

The full accepted amplitude-then-phase composition differs from the isolated phase-angle calculation. At the defaults,
\[
\psi_1=h^4\sin6\phi\left[-1/5760+(99/2500)\lambda+O(\lambda^2)\right]+O(h^6),
\]
\[
\boxed{\kappa_\infty(\lambda)=13375/1107936648
+(34494041501/849664304944)\lambda+O(\lambda^2).}
\]
These describe finite local coordinate displacements, not attraction to a universal channel axis. No model trajectory or model-evolution API was run.

## 1. Authority, evidence and scope

The authoritative checkout is `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, on `main` at
`d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`,
tree `e9e7501fdb8c2942862943fc6cc529c12a5b4fa2`.

The user authorized the attached closeout work order. Existing reports are evidence, not independent authorization for their older scripts, trajectories or suggestions.

| Input | Use and disposition |
|---|---|
| `kernel_physics/dynamics.py`, `_advance`, `phase_sync`, `step3` | Authoritative map and operation order; read, never imported or called |
| `kernel_physics/readouts.py`, `z_chiral` | Source of \(C=\Re\Omega\times\Im\Omega\); no imposed decay envelope |
| `CLAUDE_GENERIC_TRANSVERSE_HARMONICS_REVIEW.md`, §§2–6,10 and Appendices C,D,F | Existing Claude results, sign typo, finite-range evidence and proposed all-step sum |
| `TRANSVERSE_AXIS_FALSIFICATION_REPORT.md`, §§2–4 | Historical-seed decomposition and two symmetry-protected seed classes; no replay |
| `CHIRAL_TRANSVERSE_REPORT.md`, §§2–3 | Existing Jacobian, phase-composition order and relative-synchronization qualifications |

The Claude review remains 61,509 bytes, SHA-256
`a7114abb47bf61829cc901876a04be88e3438bbe55d529d6118483b152de619d`.
The prior axis-falsification JSON remains 368,719 bytes, SHA-256
`455e25fae062ddf8bc9b2eeaec18e3ac53f0cad6846ca0274be504212f86aa03`.

The analysis concerns the exact real-arithmetic map with equal \(k=(1,1,1)\), near its synchronized fixed circle of unit radius. It is not an exact floating-point statement or a global theorem about the historical finite-amplitude seed. The phase chart is used only near nonzero, positive-real components and nonzero mean. No convention at zero is replaced.

Only three new files are created in the existing research directory: this report, `verify_transverse_normal_form.py`, and `TRANSVERSE_NORMAL_FORM_RESULTS.json`. The script reads source/evidence and emits verification JSON to stdout. New stdout is recorded separately from prior evidence.

## 2. Source map and signed convention

For \(e=(1,1,1)^T\), \(L_3=ee^T-3I\), the pre-sync source formula is
\[
F_j(\Omega)=\Omega_j+\epsilon\Omega_j(1-|\Omega_j|^2)
+g\left(\sum_l\Omega_l-3\Omega_j\right).
\]
Set \(a=1-3g,\ r=a-2\epsilon,\ m=1-2\epsilon=1-a+r\).
Sections 3–6 have phase strength zero.

Use the oriented orthonormal frame
\[
u=(1,-1,0)^T/\sqrt2,\quad v=(1,1,-2)^T/\sqrt6,\quad
u\times v=\widehat e=e/\sqrt3,
\]
\[
q=q(\phi)=u\cos\phi+v\sin\phi,\quad c_0=q(\phi+\pi/2),\quad
s_2=q(\pi/2-2\phi),\quad S=\sin3\phi.
\]
For \(\Omega_0=e+ihq\), \(h>0\) small, define
\[
\psi_n=\operatorname{atan2}(C_n\cdot(-q),C_n\cdot c_0).
\]
Positive means the \(u\)-to-\(v\) orientation. For each finite \(n\) and positive \(a\), use the branch tending to zero as \(h\to0^+\). At \(h=0\), chirality is zero and its angle is undefined; these expansions concern the limiting direction.

The product identities closing the calculation are
\[
q^{\circ2}=e/3+s_2/\sqrt6,\quad q^{\circ3}=q/2+Se/(3\sqrt6),\quad
q\circ s_2=q/\sqrt6+Se/3,
\]
\[
s_2^{\circ2}=e/3-s_2/\sqrt6+\sqrt{2/3}\,Sq,\qquad
q^{\circ5}=q/4+5Se/(18\sqrt6)+Ss_2/18,
\]
\[
s_2\cdot c_0=\cos3\phi,\qquad S\cos3\phi=\tfrac12\sin6\phi.
\]
The script verifies them as exact polynomials modulo \(\cos^2\phi+\sin^2\phi-1\).

## 3. Complete coefficient expansion and sign correction

Initially avoid phase gauge fixing, so common-mode terms are retained:
\[
\Re\Omega_n=e+h^2x_n+h^4u_n+O(h^6),\qquad
\Im\Omega_n=hy_n+h^3v_n+h^5w_n+O(h^7).
\]
These lower-case vectors are Taylor coefficients, not model states. With
\[
L_Iz=az+(1-a)e(e^Tz)/3,\qquad L_Rz=rz+(1-a)e(e^Tz)/3,
\]
the source cubic gives
\[
\begin{aligned}
y'&=L_Iy,\\
x'&=L_Rx-\epsilon y^{\circ2},\\
v'&=L_Iv-\epsilon(2x\circ y+y^{\circ3}),\\
u'&=L_Ru-\epsilon(3x^{\circ2}+2y\circ v+x\circ y^{\circ2}),\\
w'&=L_Iw-\epsilon(2x\circ v+2u\circ y+x^{\circ2}\circ y
+3y^{\circ2}\circ v).
\end{aligned} \tag{1}
\]
In particular the coefficient of \(x^{\circ2}\circ y\) is one. Common real and imaginary modes are included.

The products above prove by induction the closed ansatz
\[
\begin{aligned}
y&=Aq,&x&=Me+Xs_2,\\
v&=Bq+DSe,&u&=U_0e+U_ss_2+ESq,\\
w&=Pq+QSe+RSs_2 .
\end{aligned} \tag{2}
\]
Initially \(A_0=1\), all other amplitudes zero. The verifier checks the full ansatz, including the isotropic remainder of \(w\); no unlisted contribution is discarded.

The needed scalar recurrences are
\[
\begin{aligned}
A'&=aA,\\
M'&=mM-\epsilon A^2/3,\\
X'&=rX-\epsilon A^2/\sqrt6,\\
B'&=aB-\epsilon(2AM+2AX/\sqrt6+A^3/2),\\
D'&=D-\epsilon(2AX/3+A^3/(3\sqrt6)),\\
E'&=rE-\epsilon(\sqrt6X^2+2AD+A^2X/3),\\
R'&=aR-\epsilon(2XD+2AE/\sqrt6+AX^2/3+3A^2D/\sqrt6).
\end{aligned} \tag{3}
\]
The other real fourth-order pieces obey
\[
\begin{aligned}
U_0'&=mU_0-\epsilon(3M^2+X^2+2AB/3+A^2M/3+A^2X/(3\sqrt6)),\\
U_s'&=rU_s-\epsilon(6MX-3X^2/\sqrt6+2AB/\sqrt6+A^2M/\sqrt6+A^2X/6).
\end{aligned}
\]
The remaining \(P,Q\) are fixed by (1) and do not enter the angular projection.

Consequently
\[
A_n=a^n,\qquad
\boxed{X_n=-\frac{\epsilon}{\sqrt6}\frac{a^{2n}-r^n}{a^2-r}.} \tag{4}
\]
Here \(X_n\) is a coefficient of \(h^2\). Claude's notation includes that factor, so its corrected expression is
\[
X_n^{\rm Claude}=-\frac{\epsilon h^2}{\sqrt6}
\frac{a^{2n}-r^n}{a^2-r},\qquad X_1^{\rm Claude}=-\epsilon h^2/\sqrt6.
\]
For \(a^2=r\), the quotient has the continuous value \(nr^{n-1}\).

**Typo disposition.** Claude §5, line 94, prints the opposite sign while giving the correct first step. Appendix C, lines 489–529, expands the source polynomial directly and never uses that displayed solution. Appendix F sums coefficients from that expansion. Our independent \(\Delta_1,\Delta_2,\Delta_3\), arbitrary-step recurrence and limiting expression agree with the reported downstream formulas. No sign contamination is found in those adjudicated results. This is not a fresh replay or an audit of every older numerical output. The original report and its supplied evidence remain verbatim.

## 4. Arbitrary-step angular theorem and the four rates

The cross product expands as
\[
C=h\,e\times y+h^3(e\times v+x\times y)
+h^5(e\times w+x\times v+u\times y)+O(h^7).
\]
Its order-\(h^3\) projection on \(-q\) vanishes identically. At the next order,
\[
C\cdot(-q)=\frac{\sqrt3}{2}(R-XD)h^5\sin6\phi+O(h^7),\quad
C\cdot c_0=\sqrt3 A h+O(h^3).
\]
Thus for **every finite \(n\)**,
\[
\boxed{\psi_n=\kappa_nh^4\sin6\phi+O(h^6),\qquad
\kappa_n=\frac{R_n-X_nD_n}{2A_n}.} \tag{5}
\]
No other harmonic occurs at this order. This follows inductively from (1)–(3), rather than from a finite symbolic range. For now the remainder is at fixed \(n\).

Set \(F=E+AD,\ K=R-XD\). These are the combinations obtained when the common phase is removed at the relevant orders. Cancellation using \(a-r=2\epsilon\) gives
\[
F'=rF-\epsilon\left(\sqrt6X^2+\frac{1+2a}{3}A^2X+
\frac a{3\sqrt6}A^4\right), \tag{6}
\]
\[
\boxed{\Delta_{n+1}=-\frac{\epsilon F_n}{a\sqrt6}
+\frac{\epsilon(2r-1)X_n^2}{6a}
+\frac{\epsilon(r-2\epsilon)A_n^2X_n}{6a\sqrt6}
-\frac{\epsilon^2A_n^4}{36a},} \tag{7}
\]
where \(\Delta_{n+1}=\kappa_{n+1}-\kappa_n\). The common radius and isotropic cubic pieces cancel after being included.

For a closed solution put
\[
d=a^2-r,\quad t_n=(a^{2n}-r^n)/d,\quad
X_n=-\epsilon t_n/\sqrt6,\quad F_n=-\epsilon f_n/\sqrt6.
\]
The underlying equations extend continuously to \(\epsilon=0\), without dividing by it. Then
\[
t_{n+1}=rt_n+a^{2n},\quad t_0=f_0=0,
\]
\[
f_{n+1}=rf_n+\epsilon^2t_n^2
-\frac{\epsilon(1+2a)}3a^{2n}t_n+\frac a3a^{4n}, \tag{8}
\]
\[
\Delta_{n+1}=\frac{\epsilon^2}{36a}
[6f_n+\epsilon(2r-1)t_n^2-(r-2\epsilon)a^{2n}t_n-a^{4n}]. \tag{9}
\]
Let \(\rho_1=a^4,\rho_2=a^2r,\rho_3=r^2\), with
\[
b_1=\frac{\epsilon^2}{d^2}-\frac{\epsilon(1+2a)}{3d}+\frac a3,\quad
b_2=-\frac{2\epsilon^2}{d^2}+\frac{\epsilon(1+2a)}{3d},\quad
b_3=\frac{\epsilon^2}{d^2}.
\]
The forcing of (8) is exactly \(\sum_i b_i\rho_i^n\). Therefore
\[
\boxed{f_n=\sum_{i=1}^3b_i\frac{\rho_i^n-r^n}{\rho_i-r}.} \tag{10}
\]
Its initial value and recurrence are verified for arbitrary \(n\) by the geometric convolution identity. There is no fit.

Equations (9)–(10) place \(\Delta_{n+1}\) in the span of
\(a^{4n},(a^2r)^n,r^{2n},r^n\). All are nonzero at the accepted parameters, so shifting the index gives Claude's proposed four rates for \(\Delta_n\), including the required \(n\ge2\). It actually holds from \(n=1\) here.

**Domain:** the displayed distinct-rate form assumes \(a\ne0\), \(a^2\ne r\), and \(\rho_i\ne r\). The accepted \(a=2/5,r=3/10\) meets them. Rate collisions require polynomial-times-exponential limits, such as \(nr^{n-1}\); the coefficient recurrence still holds. No four-distinct-exponential claim is extended to those degeneracies.

As an independent check, not the proof, three coefficient substitutions reproduce Claude's exact \(\Delta_1,\Delta_2,\Delta_3\). At the defaults \(\kappa_1=-1/5760\), \(\kappa_2=-347/7200000\).

## 5. Exact infinite sum and its status

For \(0<a,r<1\), the coefficient sums converge. From \(n=0\), their values are
\[
T_2=\sum t_n^2=\frac{(1-a^4)^{-1}-2(1-a^2r)^{-1}+(1-r^2)^{-1}}{d^2},
\]
\[
T_A=\sum a^{2n}t_n=\frac{(1-a^4)^{-1}-(1-a^2r)^{-1}}d,\qquad
T_4=\sum a^{4n}=(1-a^4)^{-1}.
\]
Summing (8) gives
\[
\sum f_n=\frac{\epsilon^2T_2-\epsilon(1+2a)T_A/3+aT_4/3}{1-r}.
\]
Summation of (9) and exact reduction with \(\epsilon=(a-r)/2\) prove
\[
\boxed{\kappa_\infty(a,r)=
-\frac{(a-r)^2N(a,r)}
{288a(1+a)(1+a^2)(1-r)^2(1+r)(1-a^2r)},} \tag{11}
\]
\[
N=4a^3r^2+3a^3r-4a^3+a^2r^2-4a^2+4ar^2-a-2r^2-3r+2.
\]
The apparent \(d=0\) singularity cancels. Collision limits can be taken in this sum without asserting a distinct-rate representation there.

Independent rational substitution and reduction give
\[
\kappa_\infty(2/5,3/10)=13375/1107936648.
\]
Its positive sign is opposite the first-step coefficient in our signed convention.

The arbitrary-step coefficient law and infinite coefficient sum are now **proved from the source map**, no longer conditional on a finite-range fit. Identifying this sum with the \(h^4\) coefficient of an actual limiting direction additionally uses the local analytic theorem below. That conclusion applies at the accepted parameters and nearby parameters satisfying its hypotheses, not globally to all \(a,r\) or initial states.

## 6. Nonresonance and the local analytic normal form

Near the fixed circle use the real-analytic gauge
\[
\Omega\mapsto
\frac{\overline{\operatorname{mean}\Omega}}{|\operatorname{mean}\Omega|}\Omega.
\]
The mean becomes real positive. The quotient has five real coordinates: common radius \(\mu\), real transverse \(x\), imaginary transverse \(y\). Its derivative is diagonal with spectrum
\[
(m,r,r,a,a)=(9/10,3/10,3/10,2/5,2/5).
\]
The ungauged phase eigenvalue \(1\) is removed. A claim about an attracting fixed point in the ungauged six-dimensional map would not apply.

Every multiplier has \(v_5=-1\). For a degree-\(d\) monomial in all five eigenvalues,
\[
v_5(\nu_1^{\alpha_1}\cdots\nu_5^{\alpha_5})
=-\sum_i\alpha_i=-d.
\]
For \(d\ge2\) this differs from every target's valuation \(-1\). Repeated eigenvalues only combine exponents within their eigenspaces; they do not change total degree or valuation. This is an exact all-degree proof, replacing the finite exponent search.

The theorem used is attracting Poincaré linearization for a locally invertible holomorphic germ: in the Poincaré domain, formal linearizability implies holomorphic linearizability, and nonresonance supplies formal linearizability. See Marco Abate, [*Discrete holomorphic local dynamical systems*, Theorem 5.15, printed p.36 / PDF page 38](https://pagine.dm.unipi.it/abate/articoli/artric/files/DiscHolLocDynSys.pdf).

Here it is applied to the complexification of the **five real gauge coordinates**, not to a purported holomorphic map in the three original complex amplitudes. The quotient is locally real analytic; its derivative is invertible, diagonalizable, strictly contracting and nonresonant. Its complexification therefore has a convergent linearizing conjugacy. Uniqueness with identity linear part follows from the nonresonant homological equations. Conjugation symmetry then makes the conjugacy real on the real slice, giving the required real-analytic local change of coordinates.

The same uniqueness makes it equivariant under channel permutations and complex conjugation. In the linearizing imaginary transverse coordinates,
\[
\widetilde y_n=a^n\widetilde y_0
\]
exactly, so their projective angle is constant. The physical coordinates have a finite transient displacement.

Although the common radius contracts more slowly (\(m=.9\)) than \(a=.4\), the imaginary transverse part of the inverse conjugacy is odd under complex conjugation. Each nonlinear monomial in that part contains at least one imaginary transverse factor. After division by \(a^n\), every nonlinear term tends to zero since the other factors contract. For our seed \(\widetilde y_0=hq+O(h^3)\ne0\) for small positive \(h\). Thus the observed in-plane limiting direction is the direction of \(\widetilde y_0\). The real transverse component tends to zero, giving zero limiting elevation as well.

Analytic convergence on a smaller neighborhood justifies the Taylor limit in §5:
\[
\psi_\infty(h,\phi)=\kappa_\infty h^4\sin6\phi+O(h^6).
\]
The resulting angular map is near the identity, rather than collapsing onto finitely many axes. Chirality magnitude tends to zero; the theorem asserts its **limiting direction**, not a direction for the zero vector. This is a local exact-real result and does not guarantee late-time floating-point directional resolution.

## 7. Full accepted amplitude-then-phase contribution

The source applies `phase_sync` after the amplitude/coupling update. In the nonzero local chart it is
\[
z_j\mapsto z_j\exp(i\lambda H_j),\quad
H_j=\sum_{l\ne j}\sin(3(p_l-p_j)),\quad p_j=\arg z_j .
\]
The following formulas are exact in \(\epsilon,g\) and first order in \(\lambda\). The displayed tangent factor is exact in \(\lambda\) at linear order in the state.

For the general jets in (1),
\[
p=hp_1+h^3p_3+h^5p_5+O(h^7),\quad
p_1=y,\quad p_3=v-x\circ y-y^{\circ3}/3,
\]
\[
p_5=w-x\circ v+(x^{\circ2}-u)\circ y-y^{\circ2}\circ v
+x\circ y^{\circ3}+y^{\circ5}/5.
\]
Including the mixed cubic sine term,
\[
\begin{aligned}
H_1&=3L_3p_1,\\
(H_3)_j&=3(L_3p_3)_j-\tfrac92\sum_l(p_{1l}-p_{1j})^3,\\
(H_5)_j&=3(L_3p_5)_j-\tfrac{27}2\sum_l(p_{1l}-p_{1j})^2(p_{3l}-p_{3j})
+\tfrac{81}{40}\sum_l(p_{1l}-p_{1j})^5.
\end{aligned}
\]
Expansion of \(z\exp(i\lambda H)\) gives the coefficient-of-\(\lambda\) changes
\[
\begin{aligned}
\delta y&=H_1,&\delta x&=-y\circ H_1,\\
\delta v&=H_3+x\circ H_1,&\delta u&=-y\circ H_3-v\circ H_1,\\
\delta w&=H_5+x\circ H_3+u\circ H_1.
\end{aligned}
\]
Symbolic projection and cancellation yield
\[
\begin{aligned}
\delta A&=-9A,&\delta X&=9A^2/\sqrt6,\\
\delta D&=-3AX,&\delta E&=9AD,\\
\delta F&=-3A^2X,&
\delta K&=-9K-3XA^3/\sqrt6+47A^5/16.
\end{aligned} \tag{12}
\]
Dividing by the **changed** tangent amplitude gives
\[
\boxed{\delta\kappa_{\rm sync}
=-3XA^2/(2\sqrt6)+47A^4/32.} \tag{13}
\]
For the accepted composition the inputs in (12)–(13) are the outputs of the amplitude step.

### One complete step from the seed

The linear factors are \(m,r,r,b,b\), with
\[
b=a(1-9\lambda)=(1-3g)(1-9\lambda)
=1-3g-9\lambda+27g\lambda .
\]
The same tangent factor acts on both transverse directions.

Define signed elevation
\(\chi=\operatorname{atan2}(C\cdot\widehat e,\|C-(C\cdot\widehat e)\widehat e\|)\).
Then
\[
\boxed{\chi_1=h^2\cos3\phi
\left[\frac{\epsilon-9\lambda a^2}{3\sqrt2}+O(\lambda^2)\right]+O(h^4),} \tag{14}
\]
\[
\boxed{\psi_1=h^4\sin6\phi
\left[-\frac{\epsilon^2}{36a}
+\lambda\left(\frac{\epsilon a^2}4+\frac{47a^4}{32}\right)
+O(\lambda^2)\right]+O(h^6).} \tag{15}
\]
These are joint local expansions for small \(\lambda\), with \(b>0\) and the signed branch specified earlier. They do not assert a finite-\(\lambda\) prediction after discarding the remainder.

The same-order cross terms are retained. Explicitly, the coefficient of \(\lambda\) in (15) is
\[
\frac{\epsilon}{4}(1-6g+9g^2)
+\frac{47}{32}(1-12g+54g^2-108g^3+81g^4).
\]
It includes \(\epsilon\lambda,g\lambda\) and mixed higher polynomial factors. Apparent \(\epsilon^2\lambda\) normalization terms cancel against the composed numerator.

At \(\epsilon=1/20,a=2/5\),
\[
\kappa_{1,\rm full}=-1/5760+(99/2500)\lambda+O(\lambda^2).
\]
In (14) the effective numerator is \(1/20-(36/25)\lambda+O(\lambda^2)\).

**The \(243/160\) disposition.** The verifier independently reproduces Claude Appendix D's \(+(243/160)\lambda h^4\sin6\phi\) for the angle of an isolated phase vector initialized as \(p=hq\). That is valid for that chart and observable. Here the input is \(\Omega=e+ihq\), its post-amplitude phase differs from \(hq\), and the observable is the real/imaginary cross product. The composed coefficient is (15), so \(243/160\) does **not** survive unchanged. Even at \(\epsilon=g=0\), (15) gives \(47/32\). At the accepted positive parameters the first-order sync contribution is positive, but the total includes the negative amplitude term. No sign assertion is extended to unrestricted parameters or finite \(\lambda\).

### Exact first-order change of the limiting coefficient

The monomials needed in (7) satisfy a finite linear system. Set
\[
z=(A^4,A^2X,X^2,F)^T,\quad z_0=(1,0,0,0)^T.
\]
The amplitude step is \(z\mapsto T_0z\), with
\[
T_0=\begin{pmatrix}
a^4&0&0&0\\
-\epsilon a^2/\sqrt6&a^2r&0&0\\
\epsilon^2/6&-2r\epsilon/\sqrt6&r^2&0\\
-\epsilon a/(3\sqrt6)&-\epsilon(1+2a)/3&-\epsilon\sqrt6&r
\end{pmatrix},
\]
and angular increment \(\ell z\), where
\[
\ell=\left(-\frac{\epsilon^2}{36a},
\frac{\epsilon(r-2\epsilon)}{6a\sqrt6},
\frac{\epsilon(2r-1)}{6a},-\frac{\epsilon}{a\sqrt6}\right).
\]
The phase step has
\[
z\mapsto(I+\lambda P_s)z+O(\lambda^2),\quad
P_s=\begin{pmatrix}
-36&0&0&0\\9/\sqrt6&-18&0&0\\0&18/\sqrt6&0&0\\0&-3&0&0
\end{pmatrix},
\]
and angular increment \(\lambda\ell_s z+O(\lambda^2)\), with
\(\ell_s=(47/32,-3/(2\sqrt6),0,0)\).
The accepted order is therefore
\[
T_\lambda=(I+\lambda P_s)T_0+O(\lambda^2),\qquad
\ell_\lambda=\ell+\lambda\ell_sT_0+O(\lambda^2).
\]
This is a system for formal Taylor coefficients, not a surrogate model trajectory.

For \(R_0=(I-T_0)^{-1}\), geometric summation and differentiation give
\[
\boxed{\kappa_\infty(\lambda)=\ell R_0z_0+
\lambda(\ell_sT_0R_0+\ell R_0P_sT_0R_0)z_0+O(\lambda^2).} \tag{16}
\]
The spectral radius is below one at the defaults and nearby; the inverse and its parameter derivative are analytic. Equation (16) is an exact rational expression for the first-order coefficient with \(\epsilon=(a-r)/2\); its expanded rational expression is saved in the JSON.

Independent reduction yields
\[
\left.\frac{d\kappa_\infty}{d\lambda}\right|_0
=\frac{34494041501}{849664304944}
=0.04059725858822967322481654881405\ldots .
\]
This includes the changed tangent rate and feedback of the real coefficients at every subsequent formal step relevant to \(h^4\). It is not the sum of isolated one-step constants.

The analytic normal form persists for sufficiently small \(\lambda\). Choose a neighborhood with \(.3<b<.9\), retaining positive contracting multipliers bounded away from zero. High-degree products are uniformly smaller than every target. Only finitely many degrees can then resonate; their nonzero separations at \(\lambda=0\) persist in a smaller interval by continuity. Thus a common small interval is nonresonant. The analytic theorem and oddness argument in §6 apply there. The direction remains neutral in linearizing coordinates, with its finite displacement changed by (16). No claim is made at a tangent zero, a resonance, large phase strength or outside the local chart.

## 8. Scientific disposition

| Claim class | Disposition |
|---|---|
| Channel-space recurrence theorem | Equations (1)–(11) prove the arbitrary-step law and exact coefficient sum at the specified parameters |
| Local analytic normal form | Proved under the stated gauge, contraction and nonresonance hypotheses; not global selection or global convergence |
| D3/D6 symmetry | Channel permutations and conjugation constrain the harmonics; \(\sin6\phi\) does not mean six attracting physical directions |
| Protected axis types | Previously established pair-equality and conjugate-swap invariant subspaces remain intact; no trajectory replay |
| Paper-E external clock harmonic | Separate clock variable and construction; unchanged |
| Six candidate shell apertures | Separate geometry; unchanged |
| Physical gate hypothesis | Unproved; no coordinate dictionary or recurrence-to-aperture identification supplied |

The structures occupy **compatible/repeated D3-derived harmonic classes**. No identification of \(\phi\) with \(\theta-\ell\), common physical origin, or gate registration is asserted. No Z-lock tuning, shell change, RSB, portal mechanism or new dynamics is introduced.

Claude §10's conditional all-\(n\) statement is superseded only by this attributed proof. The old finite-range evidence is not relabelled. The zero-phase rational coefficient is proved; (16) is a controlled first-order-in-\(\lambda\) result. Higher orders in \(\lambda\) have not been computed.

## 9. Verification and preservation receipt

The existing interpreter was
`C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe`,
with `-B -X utf8`. No installation or new environment was needed. No applicable AGENTS.md or index lock was present at entry.

**49/49 symbolic identities passed** in the final verifier: source-cubic jets, full harmonic closure, common-mode cancellation, arbitrary-index convolution, three existing increments, independent sum, exact valuation inputs, composed phase projections, isolated \(243/160\) with its original scope, and the coefficient lift. The direct rational sum and matrix-resolvent expression agree symbolically.

Two verifier executions succeeded: the initial 42-identity version, then the final 49-identity version with strengthened checks. Both were symbolic-only. The JSON preserves both complete stdout/stderr records and script identities. No verification run failed. A report-write orchestration attempt had a JavaScript quoting error before any file write; it is separately recorded as a tooling event, not hidden or counted as a failed mathematical check. The number of identities is a computational count, not a count of independent theorems.

The JSON contains preflight identities, source excerpts, all check residuals, exact expressions, 80-digit evaluations, full raw execution output, and pre/post preservation reconciliation. It hashes the two companions but not itself; its external identity accompanies delivery.

All **70 protected raw-byte identities** match entry values. HEAD, tree, branch and index are unchanged; tracked and staged diffs remain empty. Existing status entries are unchanged outside the three new paths. Only those three files were added to the research directory. Previous reports, Claude's review, source, tests, paper evidence, receipts and unrelated work were preserved. The predecessor suite was not rerun because this task changes no implementation.

The final machine reconciliation is recorded in `TRANSVERSE_NORMAL_FORM_RESULTS.json`.

~~~text
ACCEPTED_BASELINE = d0aa8d1cb19421ff441eacda0f83ec89fc3160b3
ALL_N_COEFFICIENT_LAW = PROVED_FROM_COEFFICIENT_RECURRENCES
SIGN_TYPO = NEGATIVE_X_REQUIRED; ADJUDICATED_DOWNSTREAM_FORMULAS_AGREE
NONRESONANCE = ALL_DEGREES_BY_5_ADIC_VALUATION
KAPPA_INFINITY_AT_DEFAULTS = 13375/1107936648
PHASE_COMPOSITION = EXACT_EPSILON_G; FIRST_ORDER_LAMBDA
KAPPA_INFINITY_LAMBDA_DERIVATIVE = 34494041501/849664304944
SYMBOLIC_CHECKS = 49/49
PROTECTED_IDENTITIES = 70/70_UNCHANGED
NEW_MODEL_TRAJECTORIES = 0
MODEL_EVOLUTION_API_CALLS = 0
KERNEL_IMPORTS = 0
KERNEL_PAPER_GATE_LOCK_EDITS = NONE
STAGING_COMMIT_PUSH = NONE
DISPOSITION = STOP_FOR_GPT_REVIEW
~~~
