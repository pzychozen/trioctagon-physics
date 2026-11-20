# Gravitational and magnetic work on an evolving triad

GM02 · 20 November 2026 · Local mathematical assessment for author and scientific review

## Result

The proposed feedback admits a unique branch in explicit nonzero load ranges and exactly conserves its declared energy. The magnetic test works: two initially dipole-silent triads acquire a nonzero interaction after one native step, and the feedback distinguishes end-to-end from side-by-side arrangements with gravity still active.

The conserved quantity is
\[
 {\cal E}=\eta U_{\rm pair}(q)+\sum_a\frac{S_a h_a^2}{2}.
 \tag{1}
\]
It excludes native \(V\), source self-energies and mechanical energy. Those terms are not automatically conserved by this rule. The storage energies are nonnegative, but \(S_a\) is a scale in joules, not a finite capacity.

Uniqueness is restricted to the stated box and the branch connected to zero load. The gravity benchmark has other real roots outside that box. This is a successful bounded mathematical construction, not global well-posedness over repeated updates or a physical realization of gravity and magnetism.

## 1. Inherited premises and new choices

The input is the reviewed GM01 correspondence, with Paper G and the NPC and spatial-work/transport sources pinned at
ca22652dc000ca2b16419c1af4167918eab1ae94. The supplied order reports GM01's mathematical acceptance. GM02's deductions below are new and are returned for review.

Use the unchanged native map
\[
\begin{split}
 v&=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL\Omega,\quad L=ee^T-3I_3,\\
 \delta_i&=\lambda\sum_{j\ne i}\sin3(\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i),\\
 F_i(\Omega)&=v_i e^{i\delta_i},\qquad e=(1,1,1)^T .
\end{split}\tag{2}
\]
All kicks use the same prestage and \(\operatorname{Arg}_0(0)=0\). In real coordinates \(q=(x,y)\), \(\Omega=x+iy\), the inherited observables are
\[
 I=\|q\|^2,\quad C=x\times y,\quad W=TC,\qquad
 T=\begin{pmatrix}
 -1/2&1&-1/2\\-\sqrt3/2&0&\sqrt3/2\\0&0&0
 \end{pmatrix}.
 \tag{3}
\]
The physical dictionary remains GM01's added premise:
\[
 m_a=m_{0a}+\alpha I_a,\qquad
 \boldsymbol\mu_a=\kappa R_aW_a,\quad
 m_{0a}\ge0,\ \alpha>0,\ R_a\in SO(3).
 \tag{4}
\]
For two bodies at fixed centers and poses, with \(r>0\), \(n=(X_1-X_2)/r\), and \(c_m=\mu_0/(4\pi)\), the single-counted pair interaction is
\[
 U=-\frac{G_Nm_1m_2}{r}
 +\frac{c_m}{r^3}\boldsymbol\mu_1^T(I_3-3nn^T)\boldsymbol\mu_2.
 \tag{5}
\]
Initial and final momenta are zero in the main problem. There is no spatial motion, radiative field or physical duration assigned to the step.

The new choices under assessment are one real \(h_a\) per body, its energy \(S_a h_a^2/2\) with \(S_a>0\), the neutral value \(h_a=1\), and feedback along the single frozen direction
\(d_a=F(q_a)-q_a\). Neither the dictionary nor the storage or feedback law is implied by the accepted native map.

## 2. Two independent tests of interaction work

Fix the NPC tuple
\[
 \epsilon=\frac1{10},\quad g=\frac1{60},\quad
 \lambda=\frac1{300},\quad
 k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right).
 \tag{6}
\]

### 2.1 Gravity with dipole-silent real states

For each body take \(\Omega=e\). The prestage is positive real, so all phase kicks vanish:
\[
 F(e)=\left(\frac{9999}{10000},1,\frac{10001}{10000}\right),\qquad
 \Delta I=\frac1{50\,000\,000}.
 \tag{7}
\]
Both initial and final moments are zero. For identical masses \(m>0\), let
\(b=\alpha/(50\,000\,000)>0\). The simultaneous unloaded work is
\[
 \Delta U_F=-\frac{G_N}{r}(2mb+b^2).
 \tag{8}
\]
Changing only \(r\) changes this work, although the native steps and every state-only internal-energy change are identical. This reproduces GM01 D5/O3.

### 2.2 Magnetic work from a silent Fourier entrance

Let \(\omega=e^{-2\pi i/3}\) and prepare both bodies at
\(\Omega=(1,\omega,\omega^2)\), with the same fixed pose, chosen as \(R=I_3\). This is the unnormalized Fourier vector. It is in the full native state space, outside NPC's near-aligned phase sector.

Because \(L\Omega=-3\Omega\) and all initial moduli equal one,
\[
 F_i(\Omega)=a_i\Omega_i,\qquad
 (a_1,a_2,a_3)=\frac1{10000}(9499,9500,9501).
 \tag{9}
\]
The positive factors leave the phases unchanged. All differences have triple-angle sine zero, so (9) is the complete update, not just its prestage.

Direct application of (3) gives
\[
 W=0,\qquad
 w:=W^+=\left(\frac{\sqrt3}{200000000},
              \frac{57}{400000},0\right),\qquad
 |w|^2=\frac{812250003}{40000000000000000}>0.
 \tag{10}
\]
Choose the center line parallel to \(w\) in one arrangement and along \(e_z\) in the other. The distance, states, poses and native steps remain the same. Both initial magnetic energies are zero; the final magnetic energies are
\[
 U_{\parallel}^{m,+}=-\frac{2c_m\kappa^2|w|^2}{r^3},\qquad
 U_{\perp}^{m,+}=+\frac{c_m\kappa^2|w|^2}{r^3}.
 \tag{11}
\]
Therefore
\[
 \Delta U_{F,\perp}-\Delta U_{F,\parallel}
 =\frac{3c_m\kappa^2|w|^2}{r^3}>0
 \quad(\kappa\ne0).
 \tag{12}
\]
Gravity, each body's self-energy, and any joint energy depending only on the two internal states cancel in this comparison. Thus even a joint state-only correction cannot balance both arrangements. No attribution of all the work to only one body's update has been made.

Both negative controls pass. Setting \(\kappa=0\) removes (12). Setting all \(k_i=1\) makes the common multiplier \(19/20\), leaves the state proportional to the Fourier entrance, and gives \(W^+=0\). Equal coefficients remove the angular difference, not the nonzero gravitational work of that preparation.

### 2.3 Exact extension to disjoint smooth radial sources

Let \(\chi_a\) be smooth, radial, normalized, supported in a ball of radius \(\ell_a\), with mass density \(m_a\chi_a\) and magnetization \(\boldsymbol\mu_a\chi_a\). Suppose
\(r>\ell_1+\ell_2\).

For any harmonic function \(f\) on the containing ball,
\[
 \int\chi_a(u)f(X_a+u)\,d^3u=f(X_a).
 \tag{13}
\]
Indeed, each spherical average is the center value by the mean-value property, and integrating it with the radial weight gives that value times \(\int\chi_a=1\).

Apply (13) successively in each variable to
\(K(r)=1/|r|\). Disjointness supplies a neighborhood free of its singularity throughout both averages. The double average is exactly \(1/r\), giving the point-mass cross energy in (5).

Each component of \(\nabla\nabla K\) is also harmonic off the origin. The same two averages give the exterior magnetic cross energy
\[
 -c_m\,\boldsymbol\mu_1^T(\nabla\nabla K)(r)\boldsymbol\mu_2
 =\frac{c_m}{r^3}\boldsymbol\mu_1^T(I_3-3nn^T)\boldsymbol\mu_2 .
 \tag{14}
\]
Differentiation commutes with these compact integrals because the separation is strictly positive. Thus (8) and (12), and the pair interaction used below, are **exact for these disjoint finite radial profiles**, not merely leading far-field terms. This argument does not cover overlapping supports, nonradial profiles or self-interactions.

## 3. Exact work for a simultaneous step

Define the fields of the other body at the fixed center:
\[
 \Phi_{-1}=-G_Nm_2/r,\qquad
 B_{-1}=\frac{c_m}{r^3}(3nn^T-I_3)\boldsymbol\mu_2,
 \tag{15}
\]
with the analogous expressions for body 2. For the disjoint radial profiles these also equal the relevant profile-averaged external fields.

For any bilinear pairing, the finite product rule is
\[
 x^+y^+-xy=\bar x\,\Delta y+\bar y\,\Delta x,\qquad
 \bar x=(x+x^+)/2 .
 \tag{16}
\]
Apply it to both terms of (5), using the symmetry of the dipole tensor:
\[
 \boxed{\quad
 \Delta U=\sum_{a=1}^2
 \left(\bar\Phi_{-a}\Delta m_a-
       \bar B_{-a}\cdot\Delta\boldsymbol\mu_a\right).
 \quad}\tag{17}
\]
There is no extra factor \(1/2\) outside this sum. Each bar already divides the simultaneous cross increment between the two bodies.

For the silent-to-magnetic test, \(\bar B_{-a}=B_{-a}^+/2\). The two terms in (17) together give the full final magnetic interaction. Evaluating only the initial fields incorrectly charges zero magnetic work.

At fixed nonzero canonical momentum, a separate kinetic term contributes exactly
\[
 \Delta K_a=
 \frac{|P_a|^2}{2m_a^+}-\frac{|P_a|^2}{2m_a}
 =-\frac{|P_a|^2\Delta m_a}{2m_am_a^+},
 \quad m_a,m_a^+>0.
 \tag{18}
\]
This is not the formula for fixed velocity.

## 4. Feedback and exact conservation

With the native directions evaluated once, define
\[
\begin{split}
 s_a&=(h_a+h_a^+)/2,\qquad D_s=(s_a d_a)_a,\\
 q_a^+&=q_a+s_a d_a,\\
 L_a(s)&=\int_0^1\nabla_{q_a}U(q+\theta D_s)\cdot d_a\,d\theta,\\
 h_a^+&=h_a-\eta L_a(s)/S_a .
\end{split}\tag{19}
\]
The integral is along a straight state-space segment; it is not a native microtrajectory. There is no reevaluation of \(F\) inside this integral.

For (4)–(5), \(U(q)\) is a polynomial of total degree at most four. At fixed \(q,d\), \(L(s)\) is polynomial of degree at most three. The integral is therefore exactly computable. It uses the same fundamental-theorem mechanism as average-vector-field/discrete-gradient energy methods; no general numerical-method novelty is claimed. See [Celledoni et al., Theorem 1 and its discussion](https://arxiv.org/pdf/1202.4555). The present frozen native direction and storage coupling require their own proof, given here.

The chain rule yields
\[
 \Delta U=\int_0^1\frac{d}{d\theta}U(q+\theta D_s)\,d\theta
         =\sum_a s_aL_a(s).
 \tag{20}
\]
For each store,
\[
 \Delta(S_a h_a^2/2)
 =S_a s_a(h_a^+-h_a)=-\eta s_aL_a(s).
 \tag{21}
\]
Equations (20)–(21) prove conservation of (1) at **every solution** of the step equations.

For computation, write their residual as
\[
 {\cal R}_a(s)=s_a-h_a+\frac{\eta L_a(s)}{2S_a}.
 \tag{22}
\]
Even away from a root, the exact energy defect for \(q^+=q+D_s\), \(h^+=2s-h\) is
\[
 {\cal E}^+-{\cal E}=2\sum_a S_as_a{\cal R}_a(s).
 \tag{23}
\]
Thus finite numerical residuals are not described as exact conservation. The theorem is exact; the reported root brackets separately control numerical evaluation.

At \(\eta=0\), \(h^+=h\) and \(s=h\). Neutral initialization \(h=1\) therefore recovers the original discrete \(F\) at every subsequent zero-load step. Without neutral initialization the zero-load map is \(q^+=q+h\,d\), not generally \(F\).

If \(d_a=0\), then \(L_a=0\), \(h_a^+=h_a\), and \(q_a^+=q_a\), regardless of the other body. This rule cannot initiate motion from a native fixed state. For example, with equal \(k_i=1\), \(q=e\) is a fixed state while the gravitational mass gradient is nonzero. Feedback acts only along the chosen native update direction.

## 5. Existence and uniqueness on a stated region

### 5.1 General local statement

For any fixed preparation, positive \(S_a\) and separated fixed geometry, (22) is smooth in \((s,\eta)\), and
\[
 {\cal R}(h,0)=0,\qquad D_s{\cal R}(h,0)=I .
 \tag{24}
\]
The implicit-function theorem gives a locally unique branch through \(s=h\). This argument treats \(d=F(q)-q\) as fixed data, so it needs no derivative of \(F\) at the preparation. Smooth dependence on varying \(q\) would require the native regularity qualifications.

A quantitative criterion uses the map
\({\cal T}_a(s)=h_a-\eta L_a(s)/(2S_a)\) on a closed box of radius \(\delta\) around \(h\). If
\[
 \frac{|\eta|\sup|L_a|}{2S_a}\le\delta,\qquad
 \max_a\frac{|\eta|}{2S_a}
       \sum_b\sup|\partial_{s_b}L_a|<1,
 \tag{25}
\]
then the map sends the box into itself and is a contraction there. Banach's theorem gives existence, uniqueness in the box, and convergence of fixed-point iteration initialized there. This is stronger than testing a numerical root alone.

### 5.2 Gravity certificate

Take identical real preparations from (7), identical \(m_0\), stores \(S>0\), and \(h_1=h_2=1\). Along each frozen direction,
\[
 m(t)=M+b t^2,\quad
 M=m_0+3\alpha,\quad b=\alpha/50000000,\quad W(t)=0.
 \tag{26}
\]
Writing \(A=G_N/r\), direct integration gives
\[
 L_1=-A b s_1(M+b s_2^2/2),\qquad
 L_2=-A b s_2(M+b s_1^2/2).
 \tag{27}
\]
Set
\[
 \gamma=\frac{\eta G_N bM}{2Sr},\qquad
 \zeta=\frac{b}{2M}\le\frac1{300000000}.
 \tag{28}
\]
On \({\cal B}=[1/2,3/2]^2\), the map is
\[
 {\cal T}_1=1+\gamma s_1(1+\zeta s_2^2),\qquad
 {\cal T}_2=1+\gamma s_2(1+\zeta s_1^2).
 \tag{29}
\]
For \(0\le\gamma\le1/10\),
\[
 \|{\cal T}-1\|_\infty
 \le \frac3{20}\left(1+\frac94\zeta\right)<\frac12,\qquad
 \|D{\cal T}\|_\infty
 \le\frac1{10}\left(1+\frac{27}{4}\zeta\right)<1.
 \tag{30}
\]
This proves the requested nonzero load range, equivalently
\[
 0\le\eta\le\frac{Sr}{5G_NbM}.
 \tag{31}
\]
Uniqueness and exchange symmetry imply \(s_1=s_2=s\). For positive load, (29) implies \(s>1\). Its derivative along the branch is
\[
 \frac{ds}{d\gamma}
 =\frac{s(1+\zeta s^2)}{1-\gamma(1+3\zeta s^2)}>0
 \tag{32}
\]
by (30). Thus smaller separation gives a larger advance, when both distances lie in the certified range with the same \(\eta,S,M,b\).

The resulting real amplitudes are
\((1-s/10000,1,1+s/10000)\). Throughout the box they lie in \([0.9,1.1]\) with zero phase width. This specific output remains in NPC's finite domain. NPC's descent/convergence theorem for repeated **unmodified** native steps does not thereby become a theorem for repeated loaded steps.

### 5.3 Magnetic certificate with gravity retained

Put \(a=1/10000\), \(t=1/20\). The Fourier preparation has the exact path quantities
\[
\begin{split}
 I(z)&=3(1-tz)^2+2a^2z^2,\\
 W(z)&=\left(\frac{\sqrt3}{2}a^2z^2,\
              \frac32 az(1-tz),0\right).
\end{split}\tag{33}
\]
The direction of \(W(z)\) changes slightly with \(z\); the end-to-end center line remains fixed at \(n=w/|w|\), defined by the unloaded endpoint. No adjustment of geometry to the loaded answer is made.

Let \(A=G_N/r\), \(D=c_m\kappa^2/r^3\), and \(Q=I_3-3nn^T\), with either center line. The path polynomial is
\[
 P(z_1,z_2)=-A\,m(z_1)m(z_2)
             +D\,W(z_1)^TQW(z_2).
 \tag{34}
\]
Its two \(L_a\) are the integrals of \(\partial_{z_a}P(\theta s_1,\theta s_2)\).

On \(0\le z\le3/2\), elementary component bounds give
\[
\begin{gathered}
 m(z)\le M=m_0+3\alpha,\quad
 |m'(z)|\le3\alpha/10,\quad |m''(z)|<\alpha/50,\\
 |W(z)|<1/4000,\quad |W'(z)|<1/6000,\quad
 |W''(z)|<1/60000,\quad \|Q\|_2=2.
\end{gathered}\tag{35}
\]
For example use \(\sqrt3<2\) and the sum of component magnitudes. These bounds apply on every integration segment in the box.

Consequently, for both arrangements,
\[
\begin{split}
 |L_a|&\le C_0=\frac3{10}A\alpha M+\frac{D}{12000000},\\
 \sum_b|\partial_{s_b}L_a|&\le \frac12 C_H,\\
 C_H&=A\left(\frac{\alpha M}{50}+\frac{9\alpha^2}{100}\right)
       +\frac{23D}{360000000}.
\end{split}\tag{36}
\]
The factor \(1/2\) comes from \(\int_0^1\theta\,d\theta\) when differentiating \(L_a\). Thus one explicit sufficient range is
\[
 0\le\eta\le
 \min\left\{\frac{S}{2C_0},\frac{S}{C_H}\right\}.
 \tag{37}
\]
Terms with zero denominator can be omitted; if both couplings vanish the step is explicit.

A convenient concrete certificate takes the permitted benchmark \(m_0=0\). In native numerical amplitude units define
\[
 a_{\rm load}=\frac{\eta G_N\alpha^2}{Sr},\qquad
 b_{\rm load}=\frac{\eta c_m\kappa^2}{Sr^3}.
 \tag{38}
\]
For the nonzero rectangle
\[
 0\le a_{\rm load}\le\frac14,\qquad
 0\le b_{\rm load}\le10^6,
 \tag{39}
\]
the full two-variable maps satisfy
\[
 \|{\cal T}-1\|_\infty\le\frac{37}{240}<\frac12,\qquad
 \|D{\cal T}\|_\infty\le\frac{73}{2880}<1 .
 \tag{40}
\]
Both have exactly one solution in \({\cal B}\), with
\(s_a\in[203/240,277/240]\) and
\(h_a^+\in[83/120,157/120]\). This is a dimensionless mathematical load range, not a measured estimate of \(G_N,\alpha,\kappa,S\).

Along the whole box, the three complex factors are
\(1-(t+a)z,\ 1-tz,\ 1-(t-a)z\), all positive and at least \(0.92485\). The interpolation contains no zero channel and retains the original Fourier phases. It remains outside NPC's near-aligned sector, despite its moduli lying in the amplitude annulus. No NPC phase-sector theorem is invoked for this test.

### 5.4 Symmetry and response sign

For identical bodies with equal \(S\), exchange symmetry maps any solution in the box to another. Uniqueness therefore forces equal \(s\). Set
\(u(s)=U(q+s d,q+s d)\). Then
\[
 L_1(s,s)=L_2(s,s)=\frac{u(s)-u(0)}{2s}\quad(s>0),
\]
and the scalar residual is
\[
 f(s)=s-1+\frac{\eta[u(s)-u(0)]}{4Ss}.
 \tag{41}
\]
Differentiating at \(\eta=0,s=1\) gives the proposed expansion
\[
 \boxed{\ s=1-\frac{\eta\,\Delta U_F}{4S}+O(\eta^2).\ }\tag{42}
\]
The remainder statement is local at a fixed preparation and geometry.

The sign comparison is stronger than this first-order expansion. The contraction bound makes each \(f\) strictly increasing on \([1/2,3/2]\). Hence throughout its certified range,
\[
 s>1\ \Longleftrightarrow\ \Delta U_F<0,\qquad
 s<1\ \Longleftrightarrow\ \Delta U_F>0,
 \tag{43}
\]
for \(\eta>0\); equality holds when the unloaded work is zero.

For the magnetic test,
\[
 u_\perp(s)-u_\parallel(s)
 =3D\,\frac{[w\cdot W(s)]^2}{|w|^2}>0
 \quad(1/2\le s\le3/2,\ D>0).
 \tag{44}
\]
Both components of \(W(s)\) have the signs of \(w\) there. Initial magnetic energies are zero, so (41) and strict monotonicity imply
\[
 \boxed{\ s_\parallel>s_\perp\ }\tag{45}
\]
over the entire common certified load range with \(\eta>0,\kappa\ne0\). Gravity remains active in both equations.

The Fourier state's intensity decreases in its unloaded step. Thus its gravitational work is positive:
\[
 \Delta U_F^g=\frac{G_N}{r}(M^2-m(1)^2)>0.
 \tag{46}
\]
The transverse arrangement always has \(\Delta U_F>0\) and \(s_\perp<1\). The parallel arrangement has \(s_\parallel>1\) exactly when
\(2D|w|^2>\Delta U_F^g\); otherwise it can also slow down, while still advancing farther than the transverse case. Magnetic attraction alone must not be used to guess the total work sign.

### 5.5 Uniqueness is not global

For the gravity example, the equal-body residual is
\[
 f_g(s)=s-1-\gamma s(1+\zeta s^2).
 \tag{47}
\]
For \(0<\gamma\le1/10\), \(\zeta>0\), it is negative at zero and positive at two, tends to negative infinity as \(s\to+\infty\), and to positive infinity as \(s\to-\infty\). There are therefore three distinct real roots: one negative, one in \((0,2)\), and another beyond two. All satisfy the formal energy identity; only one lies in the certified box and tends to the neutral unloaded solution.

Selecting that bounded branch is essential to the proposed update. No global uniqueness, large-load existence, repeated-step invariant region or asymptotic stability is claimed.

## 6. Certified examples

The following roots are enclosed by exact rational bisection brackets of width \(2^{-100}\), after the full-map contraction certificates above. Printed values are rounded. The energy theorem holds at the exact root; midpoint residuals are recorded separately in CHECK_RESULTS.json.

| Case | Specified load | \(s\) | \(h^+=2s-1\) | Total store change divided by \(S\) |
|---|---|---:|---:|---:|
| Real preparation, distance \(r\) | \(m_0=0,\ \gamma=1/10\) | 1.111111111619 | 1.222222223238 | +0.493827162978 |
| Same real preparation, distance \(2r\) | Same parameters, \(\gamma=1/20\) | 1.052631579152 | 1.105263158304 | +0.221606649104 |
| Fourier preparation, parallel | \(m_0=0,\ \eta=1,\ a_{\rm load}=1/100,\ b_{\rm load}=10^6\) | 1.006036216843 | 1.012072433686 | +0.024290611028 |
| Same Fourier preparation, transverse | Same parameters and distance | 0.990788805176 | 0.981577610351 | −0.036505394857 |

Each pair interaction change \(\Delta(\eta U)/S\) is the negative of the final column. For the magnetic example the *unloaded* pair work divided by \(S\) is
\(-0.023918063733000004\) parallel and
\(+0.037000686491999996\) transverse. Loaded and unloaded work are different quantities.

The midpoint energy defects have magnitude below \(2\times10^{-30}S\). This is a numerical certificate for these examples, not an experimentally meaningful precision.

## 7. What the benchmark includes and omits

### 7.1 Source self-energies

Only the cross interaction (5) is retained in (1). Keeping the profiles fixed does **not** make their self-energies constant when \(m,\boldsymbol\mu\) change.

For a smooth radial normalized \(\chi_a\), define
\[
 J_a=\iint\frac{\chi_a(x)\chi_a(y)}{|x-y|}\,d^3x\,d^3y,\qquad
 K_a=\int\chi_a(x)^2\,d^3x .
 \tag{48}
\]
Both are finite. In GM01's effective fixed-source variational account, the self terms are
\[
 U^{g}_{a,\rm self}=-\frac{G_NJ_a}{2}m_a^2,\qquad
 U^{m}_{a,\rm self}=-\frac{\mu_0K_a}{3}|\boldsymbol\mu_a|^2 .
 \tag{49}
\]
For the second formula use
\(\widehat B=\mu_0P_T\widehat M\), \(M=\boldsymbol\mu\chi\), radiality of \(|\widehat\chi|^2\), the angular average \(P_T=(2/3)I_3\), and Parseval. Thus
\(\int M\cdot B=(2\mu_0/3)|\boldsymbol\mu|^2\int\chi^2\), and the effective potential is minus half this quantity. The positive magnetic field energy alone has the opposite sign. These effective source-coupling terms are not a derived total microscopic matter energy.

Their exact changes are
\[
 \Delta U^g_{\rm self}=-G_NJ_a\,\bar m_a\,\Delta m_a,\qquad
 \Delta U^m_{\rm self}=-\frac{2\mu_0K_a}{3}
       \bar{\boldsymbol\mu}_a\cdot\Delta\boldsymbol\mu_a.
 \tag{50}
\]
They cancel between the two unloaded arrangements in the angular test, but generally do not vanish in either individual update. If retained in a conserved energy, they need their own segment work terms. Adding them to the same scaled \(U\) keeps the algebraic proof but changes the implicit map and requires new quantitative bounds.

### 7.2 Native potential and kinetic energy

The accepted native \(V\) is not included in (1). Assigning it an energy scale \(E_0\) and adding \(E_0V\) to the claimed total leaves a defect \(E_0\Delta V\) under the unchanged benchmark. Already at zero load and the real preparation (7),
\[
 V(F e)-V(e)=-\frac{3499999999}{200000000000000000}<0
 \tag{51}
\]
per body, while the benchmark stores do not change. Thus the augmented claim would fail even before interaction is turned on.

In general a retained extra state energy \(E_{\rm extra}(q)\) needs
\[
 L_{{\rm extra},a}=\int_0^1
 \nabla_{q_a}E_{\rm extra}(q+\theta D_s)\cdot d_a\,d\theta .
 \tag{52}
\]
Replacing the storage debit by
\(-[\eta L_a+L_{{\rm extra},a}]/S_a\) restores that extended algebraic account, but changes the feedback rule. If \(E_{\rm extra}\) is unscaled native \(V\), neutral zero-load recovery at every step is no longer automatic. Retaining original \(F\) at zero load while accounting for its dissipation would require a different, explicitly specified channel such as a store that does not feed back into \(s\). No such additional model is adopted here.

Nonzero fixed canonical momentum similarly requires (18), or its segment-gradient version with a positive mass bound. Zero momenta make this term identically zero in all main certificates.

### 7.3 Relation to the accepted transport work

The earlier spatial-work/causal-transport extension declares traveling states, a receiving metric, port laws and storage, proves well-posed forward evolution, and then proves its total work cancellation. Its zero-coupling and physical-route qualifications remain intact.

GM02 shares the requirement to prove both solvability and conservation, but its new \(h_a\) is not identified with an existing receiver, traveling field, source stock or material reservoir. The inspected sources do not supply that identification. Its implicit step is an instantaneous static endpoint model. In particular, algebraic conservation does not furnish electromagnetic retardation, radiation, spacetime dynamics or mechanical motion.

The first physical correspondence assumption is already (4): what measured mass and magnetic moment correspond to the native observables and how \(\alpha,\kappa\) are calibrated. Within GM02 specifically, the first new physical assumption is that a measurable storage degree of freedom with scale \(S_a\) can regulate advance along \(F(q_a)-q_a\) according to (19). The work order authorizes testing that proposal; its physical carrier and a clock remain unspecified.

## 8. Verification and handoff

[CHECK_RESULTS.json](CHECK_RESULTS.json) records 47 exact algebra, inequality and root-certificate groups from [checks.py](checks.py). The written harmonic-averaging, existence and conservation arguments above are necessary; the count is not a count of physical experiments or independent theorems.

The calculations ran in Windows Command Prompt after conda activation of torment. No historical scientific suite, production application or accepted native kernel was modified or rerun. [INPUT_VERIFICATION.json](INPUT_VERIFICATION.json) records the unchanged 29-entry GM01 manifest, its original review archive, and six directly accessible pinned source files. The supplied work order is preserved byte-for-byte under inputs.

[CLAIM_LEDGER.json](CLAIM_LEDGER.json) distinguishes inherited premises, new deductions, the benchmark's modeling choices and unresolved physical correspondence. [REVIEW_RECEIPT.json](REVIEW_RECEIPT.json) records preservation, local navigation and package verification.

| Source | Exact premise |
|---|---|
| [Paper G](sources/papers/PAPER_G/v0.1.1/source/paper_g.tex) | eq:amp, eq:phase, eq:T, eq:W, eq:hidden: native update, axial attachment and Fourier normalization. |
| [NPC setting](sources/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex) | eq:pre, eq:full, eq:potential: unchanged recurrence and native \(V\). |
| [NPC finite domain](sources/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/finite.tex) | eq:parameters, eq:domain, thm:finite: parameter tuple, near-aligned domain and descent scope. |
| [Declared transport](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/05_transport.tex) | eq:closedmodel, eq:augmentedstocks, eq:componentpowers: added state, storage and work pairing. |
| [Transport evolution](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/06_evolution.tex) | thm:global, eq:conservation: existence before conservation. |
| [Transport interpretation](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/09_discussion.tex) | Physical route, clock and storage interpretations remain separate from the proved channel model. |

The GM02 assessment completes the requested bounded check. Publication, physical adoption and extension to moving bodies or repeated-step dynamics are separate work.
