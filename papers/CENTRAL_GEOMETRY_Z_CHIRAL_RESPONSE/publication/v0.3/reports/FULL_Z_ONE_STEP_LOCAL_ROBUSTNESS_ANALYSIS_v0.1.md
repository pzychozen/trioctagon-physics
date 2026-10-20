# Full Z After One Native Update — Explicit Local Robustness of the Passage-Relative Result v0.1

20 October 2026 · Written mathematical certificate for GPT and Hilmir’s review

**Answer.** Yes. GPT’s continuity deduction is correct locally around the specified input, provided the pre-synchronization components are kept away from zero. An explicit joint box allowing independent changes of up to **\(10^{-8}\) in each of the six real state coordinates and each of the six native configuration coordinates** preserves the result for every input in the box, including its boundary. The complete native update, including variation of the nonzero phase-synchronization coefficient, is retained.

Throughout this box, the native-only attribution endpoint is in the surrounding host space, strictly outside the filled band section. The scheduled endpoint is strictly inside the actual band section at its own perturbed height. Both remain above and closer to the fixed throat plane than their **own** initial observation. The stronger orders

\[
\boxed{0<w_1<w_N<h<w_0,\qquad R_1<R_N<R_0}
\]

also hold uniformly. Explicit section-clearance guarantees are \(m_N=0.0019\) outside and \(m_1=0.005\) inside. Exact initial fan contact is not imposed: the neighbourhood has nonempty interior in all twelve real input coordinates. This is a conservative one-step input certificate, not a stability or flow theorem.

## 1. Precise statement, reference and source basis

Let \(\Omega_*=x_*+iy_*\) be exactly the state in R3 (21)–(22), with its original basis choice, and let

\[
\mathcal P_*=(\epsilon_*,g_*,\lambda_*,k_{1,*},k_{2,*},k_{3,*})
=(1/10,1/5,17/100,2,3,4).
\]

Choose the positive rational radii

\[
\boxed{\delta_\Omega=\delta_{\mathcal P}=\frac1{100000000}=10^{-8}.} \tag{1}
\]

The certified closed product box is

\[
\mathcal U=\left\{(\Omega=x+iy,\mathcal P):
\max_j\max(|x_j-x_{*,j}|,|y_j-y_{*,j}|)\le\delta_\Omega,
\quad \max_{m=1,\ldots,6}|\mathcal P_m-\mathcal P_{*,m}|\le\delta_{\mathcal P}
\right\}. \tag{2}
\]

These are absolute coordinate bounds. They are not a bound on each complex component’s modulus, a relative-error convention, or physical tolerances. All twelve coordinates may vary independently and simultaneously. The interior obtained by replacing both inequalities with strict inequalities is a nonempty open subset of \(\mathbb R^{12}\).

For **every** input in (2), take one complete update with that input’s fixed configuration,

\[
\Omega^+=F_{\mathcal P}(\Omega),\qquad
v_0=v(\Omega,0,0),\quad v_N=v(\Omega^+,0,0),\quad
v_1=v(\Omega^+,\pi/6,0.1), \tag{3}
\]

and put \(R_j=\|(v_j)_{xy}\|_2\), \(w_j=(v_j)_z\). Sections 3–6 prove the stated conclusions and the positive margins in the certificate table. Only \(v_0,v_1\) are scheduled observations; \(v_N\) remains the native-only attribution endpoint.

The fixed geometry is the **PLUS zero face complex**, \(u=0\), with

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,
\quad a=d/2,\quad h=s/2,\quad H=1/2,\quad O=(0,r,0).
\]

The placement is fixed at \(\mu=1,\psi=0\), and coordinates v are relative to O. The throat plane is \(w_*=0\). The MINUS zero mesh is distinct and is outside this certificate. The band triangles remain
\([T_i,T_{i+1},B_{i+2}]\) and \([T_i,B_{i+2},B_{i+1}]\), where at zero
\(T_i=(ae_i,h)\), \(B_i=(ae_i,-h)\), and
\(e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3))\).
This is the inherited geometry, with no replacement surface or new attachment law. [R1 §§1–2; R2 §§1–2]

For an unambiguous exact specification of the box centre, retain

\[
P=\left(\frac{\sqrt3a}{6},-\frac a2-\frac r3,\frac{2h+H}{3}\right),
\quad A_*=0.4635,\quad c_\ell=\cos(0.732),
\]
\[
c_*=2[P-A_*c_\ell(1,0,1)]=(c_1,c_2,c_3),\quad L_*=\|c_*\|,
\quad t_*=\sqrt{c_1^2+c_2^2},
\]
\[
p_*=(-c_2,c_1,0)/t_*,\quad q_*=(c_*/L_*)\times p_*,
\]
\[
X_*=\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\quad
Y_*=\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\qquad
\boxed{\Omega_*=X_*p_*+iY_*q_*.} \tag{4}
\]

The basis symbols \(t_*,p_*,q_*\) are not clock variables. R3 establishes \(\|\Omega_*\|=3\) and \(v_{0,*}=P\). Nearby states in (2) are arbitrary raw complex states; (4) is used only to specify the centre. They are not reconstructed from new contact data, and need not retain norm three, orthogonal real/imaginary parts, or initial contact. [R2 §7; R3 §7.1]

The authoritative checkout consulted was `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at actual local HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R3. Read-only tracked status was empty. Reports were read in the requested order R3, R2, R1, followed by the relevant primary definitions. No material source discrepancy or correction to the reused inequalities was found. Prior reports and repository files were left unchanged. Terminating decimals below denote exact rational numbers; the certificate concerns the ideal real/complex formulas, not floating-point execution.

## 2. Fixed observation law and nominal margins

### 2.1 Definitions and schedule

The source native map is

\[
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},\qquad
V=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL_3\Omega,
\]
\[
\varphi_j=\operatorname{Arg}_0V_j,\quad
\delta_j=\lambda\sum_{m\ne j}\sin3(\varphi_m-\varphi_j),\qquad
\Omega_j^+=|V_j|e^{i(\varphi_j+\delta_j)}. \tag{5}
\]

All increments use the same pre-sync V, simultaneously. The source assigns phase zero to exact zero components and forces their output to zero; at \(\lambda=0\) it bypasses phase extraction. Section 3 proves that no pre-sync component in this box is zero and that \(\lambda>0\), before using division by a magnitude. There is no dt or geometry argument in (5), and B from R3 is not a Jacobian of this nonlinear map. [D: `arg0`, `phase_sync`, `_advance`, `step3`]

Keep the staged coefficients exactly
\((\lambda_{vp},\gamma,\ell,\alpha,\beta)=(0.618,0.577,0.244,1,0.5)\). For every input,

\[
v(\Omega,\theta,t_c)
=0.618\frac{\|\Omega\|_2}{1+\|\Omega\|_2}e^{-0.577t_c}
\cos3(\theta-0.244)(\cos\theta,\sin\theta,1)
+\frac12 C(\Omega),
\]
\[
C(\Omega)=\Re\Omega\times\Im\Omega,
\qquad C_i(\Omega)=\Im(\overline\Omega_j\Omega_k)
\quad\text{for cyclic }(j,k). \tag{6}
\]

The initial observation is recomputed at \(q=0,t_c=0\), with \(N=12,q_{\rm step}=1,dt=0.1\). The current runner commits the native update, advances the independent observer clock, and then recomputes the next observation. Its angle rule is \(\theta=2\pi(q\bmod N)/N\); here the next values are \(q=1,t_c=0.1,\theta=\pi/6\). The staged observer has no memory. Neither the historical constructor-zero record nor a historical display’s recording order is substituted. These coefficients and clock values do not vary in (2). [Z: `clock_angle`, `advance_clock`, `observe_staged`; RUN: `_step`, `_advance`, `_append`; PRE: `historical_observer`]

### 2.2 Inherited enclosures used, with the needed arithmetic checked

Use a star for the exact centre and its one-step outputs, not for interval midpoints. The needed R3 §7.3 enclosures are

| Quantity | Exact nominal enclosure |
|---|---|
| \(\lvert V_{*,1}\rvert\) | \((0.3363,0.3366)\) |
| \(\lvert V_{*,2}\rvert\) | \((0.2818,0.2823)\) |
| \(\lvert V_{*,3}\rvert\) | \((0.3202,0.3204)\) |
| \((v_{N,*})_x,(v_{N,*})_y,w_{N,*}\) | \((0.14848,0.14899),\ (-0.04515,-0.04480),\ (0.19193,0.19244)\) |
| \((v_{1,*})_x,(v_{1,*})_y,w_{1,*}\) | \((0.10551,0.10602),\ (0.02345,0.023885),\ (0.16735,0.16787)\) |

For the magnitude bounds, squaring and adding R3’s real/imaginary W intervals gives respectively

\[
\begin{split}
0.1131079034&<|V_{*,1}|^2<0.1132839593,\\
0.079437298&<|V_{*,2}|^2<0.0796463434,\\
0.10253314&<|V_{*,3}|^2<0.102587732.
\end{split}
\]

These sit strictly between the squares of the tabulated positive magnitude endpoints. In particular, the common bounds needed below are

\[
0.2818<|V_{*,j}|<0.34\qquad(j=1,2,3). \tag{7}
\]

The nominal observation table is also consistent with the actual same-state blend in R3 (26). Its bounds
\(b\in(0.16178,0.16194)\), \(b_1\in(0.13720,0.13737)\), and

\[
C_*^+\in(-0.0266,-0.0259)\times(-0.0903,-0.0896)\times(0.0603,0.0610)
\]

give \(v_{N,*}=(b,0,b)+C_*^+/2\) and
\(v_{1,*}=(\sqrt3b_1/2,b_1/2,b_1)+C_*^+/2\). For example,
\(0.16178-0.0266/2=0.14848\) and
\(0.16194+0.0610/2=0.19244\). Using
\(0.8660254<\sqrt3/2<0.86602545\) gives the scheduled x enclosure; the other coordinates require only addition. No tighter nominal one-step calculation is needed.

The coarse fixed-geometry inequalities

\[
0.1464<a<0.1465,\quad 0.2071<h<0.2072,\quad
0.2886<r<0.2887,\quad \sqrt3/2>0.8660 \tag{8}
\]

follow by squaring rational bounds on \(\sqrt2,\sqrt3\), as in R3. They also give directly

\[
-0.1695<P_y<-0.1694,\qquad 0.3047<P_w<0.3048. \tag{9}
\]

For instance \(a/2+r/3>0.0732+0.0962=0.1694\), and
\((2h+H)/3>0.9142/3>0.3047\). These initial bounds will be perturbed too. None of the widths in the nominal table is treated as a new perturbation radius.

## 3. Uniform control of the complete native update

### 3.1 Pre-sync polynomial differences with all parameter changes present

For the derivation temporarily let \(\delta_\Omega\le1/4\) and \(\delta_{\mathcal P}\le1/100\), conditions satisfied by (1). Define

\[
e=2\delta_\Omega,\qquad
\boxed{D_V=26\delta_\Omega+52\delta_{\mathcal P}.} \tag{10}
\]

Every complex component difference is at most
\(\sqrt2\delta_\Omega\le e\). Since \(\|\Omega_*\|_2=3\), each centre component has modulus at most 3, while every perturbed component has modulus at most \(3+e<4\). Throughout this containing box,

\[
|\epsilon|\le1/5,\quad |g|\le3/10,\quad
|\lambda|\le1/5,\quad |k_j|\le5.
\]

For complex z,z_* of modulus at most 4,

\[
\big||z|^2z-|z_*|^2z_*\big|
\le\left(|z|^2+(|z|+|z_*|)|z_*|\right)|z-z_*|
\le48|z-z_*|. \tag{11}
\]

Let \(H_j(\Omega,k)=\Omega_j(k_j-|\Omega_j|^2)\), where H_j here is the onsite expression, unrelated to the fixed tip height H. Splitting the linear k product and the cubic term gives

\[
|H_j-H_{*,j}|\le5e+3\delta_{\mathcal P}+48e
=53e+3\delta_{\mathcal P},\qquad
|H_{*,j}|\le3(4+9)=39. \tag{12}
\]

The maximum absolute row sum of L_3 is 4. Therefore
\(|(L_3(\Omega-\Omega_*))_j|\le4e\) and
\(|(L_3\Omega_*)_j|\le12\). The exact difference

\[
V-V_*=(\Omega-\Omega_*)+\epsilon(H-H_*)
+(\epsilon-\epsilon_*)H_*
+gL_3(\Omega-\Omega_*)+(g-g_*)L_3\Omega_*
\]

then yields

\[
\begin{split}
|V_j-V_{*,j}|
&\le e+\tfrac15(53e+3\delta_{\mathcal P})
+39\delta_{\mathcal P}+\tfrac3{10}(4e)+12\delta_{\mathcal P}\\
&=12.8e+51.6\delta_{\mathcal P}
\le D_V.
\end{split} \tag{13}
\]

This includes simultaneous changes in every state component, epsilon, g and every k_j; products of perturbations are covered by the uniform coefficient bounds. It is an exact finite-difference bound over the whole box, not a centre Jacobian or a first-order truncation.

At the selected radii,

\[
\boxed{D_V=0.00000078<0.001.} \tag{14}
\]

The reverse triangle inequality applied to the nominal magnitudes proves, **before any normalization**,

\[
\begin{split}
|V_1|&>0.33629922,\\
|V_2|&>0.28179922,\\
|V_3|&>0.32019922.
\end{split}
\qquad
\boxed{0.28<|V_j|<0.34\quad\text{on all of }\mathcal U.} \tag{15}
\]

For the upper bound, the largest nominal upper bound is 0.3366, and
\(0.3366+D_V=0.33660078<0.34\). Also

\[
0.16999999\le\lambda\le0.17000001,
\]

so phase synchronization remains enabled. All inputs and formula values are finite, all normalizing magnitudes in the next step are positive, and the ideal complete native map is well defined throughout the closed box.

### 3.2 Branch-independent synchronization bound

For the now-proved nonzero components set

\[
u_j=V_j/|V_j|,\quad u_{*,j}=V_{*,j}/|V_{*,j}|,
\quad s_{jk}=\Im(\overline u_j u_k),\quad T(s)=3s-4s^3.
\]

Then exactly

\[
\sin3(\varphi_k-\varphi_j)=T(s_{jk}),\qquad
\delta_j=\lambda\sum_{m\ne j}T(s_{jm}),\qquad
\Omega_j^+=V_je^{i\delta_j}. \tag{16}
\]

The u_j here are normalized complex components, not the fixed crystal magnitude u=0. To bound their change, add and subtract \(V_{*,j}/|V_j|\):

\[
|u_j-u_{*,j}|\le\frac{2|V_j-V_{*,j}|}{|V_j|}
\le8D_V, \tag{17}
\]

where the convenient weaker lower bound \(|V_j|>1/4\) follows from (15). Products of unit complex numbers give

\[
|s_{jk}-s_{*,jk}|\le16D_V.
\]

Both s values and their intervening real interval lie in [-1,1]. On that entire interval,
\(|T'(s)|=|3-12s^2|\le9\), so

\[
|T(s_{jk})-T(s_{*,jk})|\le144D_V.
\]

Since \(|T(s_{*,jk})|\le1\), variation of lambda as well as V is included by

\[
|\delta_j-\delta_{*,j}|
\le\tfrac15(2\cdot144D_V)+2\delta_{\mathcal P}
\le\boxed{G_\delta:=58D_V+2\delta_{\mathcal P}}. \tag{18}
\]

There is no sequential substitution of changed phases. Finally
\(|e^{ia}-e^{ib}|\le|a-b|\) and \(|V_{*,j}|<0.34\) imply

\[
\begin{split}
|\Omega_j^+-\Omega_{*,j}^+|
&\le |V_j-V_{*,j}|+|V_{*,j}|\,|e^{i\delta_j}-e^{i\delta_{*,j}}|\\
&\le D_V+0.34G_\delta
\le\boxed{Q:=21D_V+\delta_{\mathcal P}}.
\end{split} \tag{19}
\]

For (1),

\[
G_\delta=0.00004526,\qquad Q=0.00001639. \tag{20}
\]

These bounds include the complete nonlinear pre-sync step and all three simultaneous phase changes.

### 3.3 What this verifies about continuity

At the centre, (7) already puts V away from zero. The polynomial pre-sync map is jointly continuous in state and parameters. On the nonzero set, (16) is a smooth expression in the real/imaginary parts and lambda; a principal-argument branch cut cannot create a discontinuity in this expression. The observer’s norm, saturation and cross product are continuous as well. R1’s section boundary is continuous within the slab, and the nominal geometric and own-initial comparison inequalities are strict. Thus the qualitative existence of a local joint neighbourhood follows.

This confirms GPT’s deduction **locally**, without extending it through pre-sync zeros. The source’s Arg_0 convention at such zeros can affect other components’ phase increments; global continuity or common-phase symmetry there is not being assumed. Equations (13)–(20) are the quantitative replacement for an unspecified “sufficiently small” neighbourhood. They prove that this particular closed box excludes those zeros. Initial fan contact is an equality and need not persist under continuity; none of the required conclusions depends on preserving it.

## 4. Propagate to the initial and both updated full-Z observations

Use \(\|\cdot\|_\infty\) for the largest absolute coordinate of a real plotted vector. For complex state vectors, the explicit component estimates below refer to complex modulus, while \(\|\cdot\|_2\) is the usual Euclidean norm of all six real components.

For nonnegative norms,

\[
\left|\frac{\kappa}{1+\kappa}-\frac{\kappa'}{1+\kappa'}\right|
=\frac{|\kappa-\kappa'|}{(1+\kappa)(1+\kappa')}
\le|\kappa-\kappa'|. \tag{21}
\]

At either fixed observation clock used here, the envelope is at most one, and every coordinate of
\(\cos3(\theta-\ell)(\cos\theta,\sin\theta,1)\) has absolute value at most one. The macro coordinate error is consequently at most 0.618 times the state-norm error.

For the chiral term, the exact bilinear product identity gives, for any two states z,z' and a cyclic pair (j,k),

\[
|C_i(z)-C_i(z')|
\le |z_j-z'_j|\,|z_k|+|z'_j|\,|z_k-z'_k|. \tag{22}
\]

This controls the full chirality of the actual state, including its synchronization change; it does not introduce an independent offset choice.

### Initial observation

The norm inequality gives
\(|\|\Omega\|_2-3|\le\sqrt6\delta_\Omega<3\delta_\Omega\).
Using the component bounds 4 and 3 from §3.1 in (22), the initial chiral-coordinate change is at most \(7e=14\delta_\Omega\). Therefore

\[
\boxed{\|v_0-P\|_\infty
\le0.618(3\delta_\Omega)+\tfrac12(14\delta_\Omega)
\le E_0:=9\delta_\Omega.} \tag{23}
\]

For (1), \(E_0=0.00000009<10^{-7}\). Parameters do not affect the initial observation, but arbitrary raw state changes do. This bound is what permits comparison with each input’s own v_0.

### Updated observations

Synchronization preserves component magnitudes, so its next norm is exactly \(\kappa^+=\|V\|_2\). Hence the sharper norm error comes directly from (13), rather than the larger post-phase error Q:

\[
|\kappa^+-\kappa_*^+|\le\|V-V_*\|_2\le\sqrt3D_V<2D_V. \tag{24}
\]

Both the centre and perturbed post-sync component magnitudes are below 0.34 by (7), (15) and magnitude preservation. Equations (19), (22) thus give

\[
\|C(\Omega^+)-C(\Omega_*^+)\|_\infty\le0.68Q.
\]

The endpoint error bound, valid for both fixed clocks, is

\[
\boxed{
\|v_N-v_{N,*}\|_\infty\le E_N,\qquad
\|v_1-v_{1,*}\|_\infty\le E_1,
\quad E_N=E_1:=\frac{309}{250}D_V+\frac{17}{50}Q.
} \tag{25}
\]

The first term is the common-state macro error \(0.618(2D_V)\), and the second is half its chiral error. At (1), written rational substitution gives

\[
E_N=E_1=1.236(0.00000078)+0.34(0.00001639)
=0.00000653668<\boxed{10^{-5}}. \tag{26}
\]

All estimates are uniform over the simultaneous joint box. Triangle inequalities allow the macro and chiral errors to be added conservatively, but both originate from the same input and complete next state. No cancellation, parameter correlation, fixed initial norm, or frozen chirality was assumed.

## 5. Uniform endpoint intervals and finite geometric margins

### 5.1 New intervals after adding perturbation error

Expand the nominal table in §2.2 by \(10^{-5}\) per coordinate, using (26). For every input in the closed box,

| Endpoint | x | y | w |
|---|---|---|---|
| \(v_N\) | \((0.14847,0.14900)\) | \((-0.04516,-0.04479)\) | \((0.19192,0.19245)\) |
| \(v_1\) | \((0.10550,0.10603)\) | \((0.02344,0.023895)\) | \((0.16734,0.16788)\) |

These are perturbed endpoint intervals, not revised nominal intervals. Combining (9) and (23) also gives

\[
(v_0)_y<-0.1694+10^{-7}<-0.1693,
\qquad w_0>0.3047-10^{-7}>0.3046.
\]

In particular

\[
\boxed{R_0>0.1693,\qquad w_0>0.3046.} \tag{27}
\]

The initial x component is not needed for this lower bound on its radius; its variation is still covered by the full vector estimate (23).

### 5.2 Central slab and host interior

The intervals and (8) prove

\[
0<w_1<w_N<h<w_0,
\]
\[
w_1>0.16734,\quad w_N-w_1>0.02404,\quad
h-w_N>0.01465,\quad w_0-h>0.0974. \tag{28}
\]

The scheduled point also has \(h-w_1>0.03922\). Thus both endpoints are strictly in the central slab before any band-interior predicate is applied.

For horizontal radii, simple upper rectangles suffice:

\[
R_N^2<0.1490^2+0.0452^2=0.02424404<0.156^2,
\]
\[
R_1^2<0.1061^2+0.0239^2=0.01182842<0.109^2. \tag{29}
\]

The fixed host section has unit panel normals n_k and interior inequalities \(n_k\cdot v_{xy}<r\). Since \(r>0.2886\), (29) gives

\[
r-n_k\cdot(v_N)_{xy}\ge r-R_N>0.1326,
\qquad
r-n_k\cdot(v_1)_{xy}>0.1796 \tag{30}
\]

for all three panels. Both are strictly inside the host’s triangular planar interior at their respective heights. [R2 §2.2]

### 5.3 Native-only endpoint: exterior of the filled band section

Every actual PLUS zero band-section boundary point has radius at most a: it lies on a triangle segment whose horizontal coordinates are convex combinations of radius-a ring vertices. The inherited star-shaped filled section also lies within that radius. Thus, uniformly,

\[
R_N-a\ge(v_N)_x-a>0.14847-0.1465=0.00197.
\]

Consequently a convenient positive separation guarantee is

\[
\boxed{m_N=0.0019=\frac{19}{10000},\qquad
(v_N)_x>a+m_N.} \tag{31}
\]

Together with (30), this places v_N in the surrounding host space, strictly outside the filled band section. It is not on the band surface. The planar distance to every point of that filled section, at the same height, is greater than 0.00197 by the reverse triangle inequality. [R3 §8.2; new perturbation margin]

### 5.4 Scheduled endpoint: inside the actual section at its perturbed height

At this input’s height w_1 put

\[
\eta_1=(1-w_1/h)/2.
\]

The actual zero-member section has edges between
\(S_i=(1-\eta)ae_i+\eta ae_{i+1}\) and
\(D_i=(1-\eta)ae_i+\eta ae_{i+2}\), and between D_i and S_{i+1}. It is star-shaped about the contained axis. The bound inherited from R3 (34) is

\[
R(w,\varphi)\ge L(\eta):=
\min\{a\sqrt3(1-\eta)/2,\ a(1-3\eta/2)\} \tag{32}
\]

where both terms are positive. It follows from the actual triangles: on a top-two-vertex triangle, projection on its unit horizontal plane normal equals \(a\sqrt3(1-\eta)/2\); on a bottom-two-vertex triangle, projection on e_i is at least \(a(1-3\eta/2)\). Thus (32) bounds every boundary segment, including the nonconvex section’s inward vertices. A disk bound is being deduced from these triangles, not used as a replacement geometry. [R1 §2; R3 §8.2]

Use the **perturbed** interval \(w_1>0.16734>0.1673\), together with \(h<0.2072\). Since \(0.2072(0.806)=0.1670032<0.1673\),

\[
0<\eta_1<0.097.
\]

Equation (8) therefore gives both positive lower bounds

\[
a\sqrt3(1-\eta_1)/2
>0.1464(0.8660)(0.903)=0.1144845072,
\]
\[
a(1-3\eta_1/2)>0.1464(0.8545)=0.1250988.
\]

In particular, **for all input-dependent heights and azimuths in this box**,

\[
L(\eta_1)>0.1144,\qquad R_1<0.109,
\qquad L(\eta_1)-R_1>0.0054. \tag{33}
\]

A convenient positive clearance certificate is

\[
\boxed{m_1=0.005=\frac1{200},\qquad
\sup_{\mathcal U}R_1+m_1\le0.114<0.1144\le\inf_{\mathcal U}L(\eta_1).} \tag{34}
\]

The axis-containing star-shaped section and (32) now put v_1 strictly in its filled interior. Every boundary point at that same height is at planar distance greater than 0.0054 from v_1, again by the reverse triangle inequality. This is a section-clearance statement; no distance to the full three-dimensional surface or to the throat boundary is inferred. The boundary estimate was made at varying w_1, not at the nominal height.

### 5.5 Approach relative to each input’s own initial observation

Because \(w_*=0\) and all relevant heights are positive, the ordinary axial distances equal their heights. From (27) and the endpoint intervals,

\[
\boxed{w_0-w_N>0.11215,\qquad w_0-w_1>0.13672.} \tag{35}
\]

Both approach statements therefore compare the perturbed endpoint with the **same input’s perturbed v_0**, not with the fixed centroid P. If expressed in squared distances,

\[
w_0^2-w_N^2>0.11215(0.3046+0.19192)
=0.055684718>0.0556,
\]
\[
w_0^2-w_1^2>0.13672(0.3046+0.16734)
=0.0645236368>0.0645. \tag{36}
\]

Neither endpoint reaches the throat plane: their uniform positive height margins are already in (28) and the endpoint table. A smaller axial distance is not passage through the finite throat aperture or an estimate of distance to its boundary.

The radial order is equally uniform. Using the perturbed initial lower bound (27), the native x lower bound, and (29),

\[
\boxed{R_0-R_N>0.1693-0.156=0.0133,\qquad
R_N-R_1>0.14847-0.109=0.03947.} \tag{37}
\]

Thus the optional stronger radial ordering holds as well. No observation is inserted between these endpoints, and v_N is not an additional time sample.

## 6. Compact certificate table

Every bound in this table holds for **every** point of the closed twelve-coordinate box (2). The listed decimal margins are exact rational numbers.

| Property | Governing inequality | Uniform bound or positive margin | Derivation |
|---|---|---|---|
| Joint input neighbourhood | Six state-coordinate and six parameter-coordinate deviations | Each at most \(10^{-8}\); nonempty twelve-dimensional interior | (1)–(2) |
| Pre-sync perturbation | \(\max_j\lvert V_j-V_{*,j}\rvert\le D_V\) | \(D_V=0.00000078\) | (10)–(14) |
| Nonzero pre-sync components | \(\min_j\lvert V_j\rvert\) | Greater than 0.28179922; use lower bound 0.28 | (15) |
| Synchronization retained | \(\lambda\) | At least 0.16999999, strictly positive | §3.1 |
| Complete next-state perturbation | \(\max_j\lvert\Omega_j^+-\Omega_{*,j}^+\rvert\le Q\) | \(Q=0.00001639\) | (16)–(20) |
| Initial full-Z perturbation | \(\lVert v_0-P\rVert_\infty\le E_0\) | \(E_0=9\cdot10^{-8}<10^{-7}\) | (23) |
| Both updated full-Z perturbations | \(\lVert v_N-v_{N,*}\rVert_\infty,\lVert v_1-v_{1,*}\rVert_\infty\) | At most 0.00000653668, hence below \(10^{-5}\) | (24)–(26) |
| Above throat | \(w_N,w_1>0\) | \(w_N>0.19192\), \(w_1>0.16734\) | §5.1 |
| Central slab | \(h-\lvert w_N\rvert,h-\lvert w_1\rvert\) | Greater than 0.01465 and 0.03922 | (28) |
| Initial above upper ring | \(w_0-h\) | Greater than 0.0974 | (27)–(28) |
| Updated height order | \(w_N-w_1\) | Greater than 0.02404 | (28) |
| Host membership | \(r-n_k\cdot(v_j)_{xy}>0\), every panel k | Greater than 0.1326 for N; 0.1796 for 1 | (29)–(30) |
| Native exterior section separation | \(R_N-a\) | Greater than 0.00197; choose \(m_N=0.0019\) | (31) |
| Scheduled varying section | \(0<\eta_1<0.097\), \(R_1<L(\eta_1)\) | \(R_1<0.109\), \(L>0.1144\); gap greater than 0.0054; choose \(m_1=0.005\) | (32)–(34) |
| Axial approach to own initial point | \(w_0-w_N,w_0-w_1\) | Greater than 0.11215 and 0.13672 | (35) |
| Squared axial approach | \(w_0^2-w_N^2,w_0^2-w_1^2\) | Greater than 0.0556 and 0.0645 | (36) |
| Radial approach to own initial point | \(R_0-R_N\) | Greater than 0.0133 | (37) |
| Updated radial order | \(R_N-R_1\) | Greater than 0.03947 | (37) |
| Off fans and finite notch patches | Both endpoints have \(\lvert w\rvert<h\) | Strict height exclusion from all their finite domains | §5.2; R2 §3 |

The box radius is deliberately small and was not optimized. The proof uses uniform inequalities over the box, not sampled corners, one-coordinate perturbations, or an empirical parameter sweep. The nominal enclosure widths and the newly propagated input errors have been kept separate throughout.

## 7. Interpretation and stopping point

This certificate supplies the quantitative content missing from a qualitative continuity argument. It preserves the full native state dependency, nonzero simultaneous synchronization, the staged envelope, and the fixed next clock angle. Exact initial fan contact has played no role in defining the neighbourhood or proving the new inequalities. At the centre the original contact is lost as R3 established; for nearby inputs that did not initially contact a fan, the correct statement is simply that both resulting endpoints are off all fans and finite notch patches.

The result is a neighbourhood of inputs whose **single-step observations** have fixed geometric classifications. It is not a basin of attraction, invariant region, theorem of temporal stability, observed traversal, probability statement or claim of historical-seed reachability. Geometry remains absent from the native evolution law. Neither an intermediate crossing nor physical flow follows from the endpoint inequalities. No member/hand extension, memory evolution, SRG, fluid model, fitting, implementation or publication work is included.

All work for this order consisted of source/filesystem reads, written algebra and creation of this one new report outside the checkout. No scientific formulas were evaluated by a program; no scientific code, tests, simulations, modules, symbolic scripts or applications were run. Earlier reports and repository files remain unchanged. The ideal-formula certificate does not certify binary64 execution, measurement tolerance or finite-precision safety. Work stops here for GPT and Hilmir’s review; no follow-on task is issued.

## Source locations

| Key | Exact source and consulted portions |
|---|---|
| R3 | [Completed one-step report][R3], §§2–4 map, zero conventions and observer; §7 (21)–(31) exact centre and nominal rational enclosures; §8.2 actual section bound (34) and endpoint margins; §§8.4–9 fixed-reference scope |
| R2 | [Central-passage report][R2], §§1–2 actual geometry, nested regions and throat; §3 fan/notch height domains; §5 same-state readout; §7 exact contact construction |
| R1 | [Macro middle-band report][R1], §§1–2 actual PLUS zero face list, section vertices, star-shaped radial boundary and face-plane table |
| D | [dynamics.py][D], `L3` line 12; `DynamicsConfig` 27–44; `arg0` 57–63; `phase_sync` 66–84; `_advance` and `step3` 87–104 |
| RO | [readouts.py][RO], `z_chiral`, lines 7–17, unnormalized cyclic cross product |
| Z | [z_manifold.py][Z], `Clock`, `clock_angle`, `advance_clock` 46–82; staged coefficients, norm/saturation, scalar and blend 90–161; `_observe` and `observe_staged` 189–199 |
| RUN | [_runner.py][RUN], `_step` 13–18; `_observe` 38–44; `_advance` 47–52; `_append` 83–96; initial sample in `run` |
| PRE | [_presets.py][PRE], `historical_observer` 18–36, literal staged coefficients, clock values, no staged memory and recomputed initialization |
| WO | [Current local-robustness work order][WO], prescribed joint quantifiers, fixed reference, required conclusions and execution limits |

[R3]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md
[R2]: C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md
[R1]: C:/Users/Notandi/.codex/reports/Z_MACRO_MIDDLE_BAND_INTERSECTION_ANALYSIS_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:27
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[RUN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py:83
[PRE]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_FULL_Z_ONE_STEP_LOCAL_ROBUSTNESS_v0.1.md
