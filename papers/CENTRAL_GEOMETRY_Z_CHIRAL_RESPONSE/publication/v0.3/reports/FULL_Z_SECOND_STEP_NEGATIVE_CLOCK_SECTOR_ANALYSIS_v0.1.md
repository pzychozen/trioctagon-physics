# Full Z at the Second Scheduled Observation — The Same Certified Input Box in the First Negative Macro Sector v0.1

20 October 2026 · Written mathematical certificate for GPT and Hilmir’s review

**Answer.** For every input in R4’s unchanged closed twelve-coordinate box of radius \(10^{-8}\), the second scheduled full-Z observation has **negative height**, lies strictly in the central slab and host interior, and is **outside the actual filled band section**. Thus the first observation’s band-interior membership does not persist. Both complete native updates use the same configuration chosen by that input.

The uniform bounds proved below include

\[
\boxed{-0.1102<w_2<-0.1075,\qquad 0.155<R_2<0.160,}
\]
\[
\boxed{|w_2|<|w_1|<|w_0|,\qquad R_1<R_2<R_0.}
\]

Here \(R_n=\|(v_n)_{xy}\|_2\), and each comparison uses the same input’s own observations. The second point is closer to the throat plane than either preceding point, but farther from the axis than the first point. Its radial separation from the band boundary at its own height and azimuth is greater than \(0.0085\). There is a sign change between scheduled observations, \(w_1>0>w_2\); no intervening throat passage, surface contact or continuous trajectory follows.

The negative macro factor is only a starting identity. The full native continuation gives a positive third chiral component, which offsets part of the negative macro height. The resulting full height is nevertheless uniformly negative. Section 6 separates the coupled native changes, envelope change and clock change.

## 1. Quantifiers, exact input and source basis

Retain the exact constants and PLUS zero comparison of R4:

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,
\quad a=d/2,\quad h=s/2,\quad H=1/2,\quad O=(0,r,0).
\]

Coordinates \(v=X-O\) have fixed placement \(\mu=1,\psi=0\), and the throat plane is \(w=0\). The exact centre is

\[
P=\left(\frac{\sqrt3a}{6},-\frac a2-\frac r3,\frac{2h+H}{3}\right),
\quad A_*=0.4635,\quad c=\cos(0.732),
\]
\[
c_*=2[P-A_*c(1,0,1)]=(c_1,c_2,c_3),\quad
L_*=\|c_*\|,\quad t_*=\sqrt{c_1^2+c_2^2},
\]
\[
p_*=(-c_2,c_1,0)/t_*,\qquad q_*=(c_*/L_*)\times p_*,
\]
\[
X_*=\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\quad
Y_*=\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\qquad
\boxed{\Omega_*=X_*p_*+iY_*q_*.} \tag{1}
\]

These basis symbols are not clock variables. In particular, \(\|\Omega_*\|=3\), \(C(\Omega_*)=c_*\), and its initial observation is exactly P. This is the original state with its original basis, not a representative selected only by norm and chirality. [R4 (4); R3 (21)–(22)]

Put

\[
\mathcal P_*=(\epsilon_*,g_*,\lambda_*,k_{1,*},k_{2,*},k_{3,*})
=(1/10,1/5,17/100,2,3,4),\qquad \delta=10^{-8},
\]
\[
\mathcal U=\left\{(\Omega^{(0)}=x+iy,\mathcal P):
\max_j\max(|x_j-x_{*,j}|,|y_j-y_{*,j}|)\le\delta,
\quad \max_m|\mathcal P_m-\mathcal P_{*,m}|\le\delta\right\}. \tag{2}
\]

**All conclusions labelled uniform quantify over every point of this original closed box**, including its boundary, with all twelve real coordinates free to vary independently and simultaneously. For each input choose \(\mathcal P\) once and define precisely

\[
\Omega^{(1)}=F_{\mathcal P}(\Omega^{(0)}),\qquad
\boxed{\Omega^{(2)}=F_{\mathcal P}(F_{\mathcal P}(\Omega^{(0)})).} \tag{3}
\]

There is no second choice of parameters or new state perturbation. The first image is not reset into (2), renormalized or fitted to contact. Nearby initial inputs need not have norm three, orthogonal real and imaginary parts, or initial fan contact. The unequal-k reference is the inherited analytical configuration, not a physical default or a fixed-parameter threefold-symmetric configuration.

The authoritative checkout read was `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`. Its actual local HEAD was `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R4; read-only tracked status was empty. R4 and R3 supplied the inherited certificate and exact continuation, followed by the relevant R2/R1 geometry sections and the five primary source files listed at the end. No material definition discrepancy affecting this calculation was found. Earlier reports and repository files were left unchanged.

All terminating decimals in equations and interval endpoints below are exact rationals. The new bounds are written algebraic enclosures of the ideal real/complex formulas. No scientific formulas were evaluated by a program, calculator, imported module or numerical test.

## 2. The complete twice-composed map and scheduled readout

### 2.1 Native dependency

For \(n=1,2\), define from the preceding state and the same \(\mathcal P\)

\[
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},\qquad
B_{n-1}=I+\epsilon\operatorname{diag}(k_j-|\Omega_j^{(n-1)}|^2)+gL_3,
\]
\[
V^{(n)}=B_{n-1}\Omega^{(n-1)},\qquad
\varphi_j^{(n)}=\operatorname{Arg}_0V_j^{(n)},
\]
\[
\delta_j^{(n)}=\lambda\sum_{m\ne j}\sin3(\varphi_m^{(n)}-\varphi_j^{(n)}),
\qquad
\Omega_j^{(n)}=|V_j^{(n)}|e^{i(\varphi_j^{(n)}+\delta_j^{(n)})}. \tag{4}
\]

Each stage’s three increments use that stage’s same pre-sync vector simultaneously. The source sets \(\operatorname{Arg}_0(0)=0\) and forces a zero component’s output to zero; it bypasses synchronization only at \(\lambda=0\). R4 excludes first-stage zeros on (2), and §4 below separately excludes second-stage zeros before normalization. Here \(\lambda\ge0.16999999>0\), so the full synchronizer remains enabled. There is no observer dt, geometry argument, forcing or normalization in this native map. [D: `arg0`, `phase_sync`, `_advance`, `step3`]

On the nonzero set put \(u_j^{(n)}=V_j^{(n)}/|V_j^{(n)}|\),
\(s_{jk}^{(n)}=\Im(\overline u_j^{(n)}u_k^{(n)})\), and \(T(s)=3s-4s^3\). Then exactly

\[
(\delta_1^{(n)},\delta_2^{(n)},\delta_3^{(n)})
=\lambda\big(T(s_{12}^{(n)})+T(s_{13}^{(n)}),
-T(s_{12}^{(n)})+T(s_{23}^{(n)}),
-T(s_{13}^{(n)})-T(s_{23}^{(n)})\big),
\]
\[
\Omega_j^{(n)}=V_j^{(n)}e^{i\delta_j^{(n)}}. \tag{5}
\]

Thus (1), (4), (5), applied only for n=1 and n=2, specify the exact nominal second state without any rounded midpoint substitution. The first application is exactly R3 (23)–(25). A star below always means this exact centre or its exact image.

The coupled second norm and chirality are

\[
\kappa_2=\|V^{(2)}\|_2,\qquad
C_{2,i}=\Im\!\left(\overline V_j^{(2)}V_k^{(2)}
e^{i(\delta_k^{(2)}-\delta_j^{(2)})}\right), \tag{6}
\]

with cyclic pairs \((j,k)=(2,3),(3,1),(1,2)\). In particular the norm is controlled before synchronization, while chirality is calculated after it. For \(D=V^{(2)}-\Omega^{(1)}\), the inherited exact identities also give

\[
\kappa_2^2-\kappa_1^2
=2\epsilon\sum_j |\Omega_j^{(1)}|^2(k_j-|\Omega_j^{(1)}|^2)
-2g\sum_{j<k}|\Omega_j^{(1)}-\Omega_k^{(1)}|^2+\|D\|^2,
\]
\[
C_2-C_1=(\operatorname{cof}B_1-I)C_1+(C_2-C_{V^{(2)}}),
\qquad C_{V^{(2)}}=\operatorname{cof}(B_1)C_1. \tag{7}
\]

B is an input-dependent real symmetric matrix, not the derivative of the nonlinear map. These identities retain the finite-step norm remainder and the relative-phase change in chirality. [R3 (4)–(8); RO: `z_chiral`]

### 2.2 Observer and the three scheduled observations

Retain \((\lambda_{vp},\gamma,\ell,\alpha,\beta)=(0.618,0.577,0.244,1,0.5)\), \(N=12\), \(q_{\rm step}=1\), \(dt=0.1\), recomputed initialization and no memory. The runner commits the native update, advances the independent clock and then observes. [Z; RUN; PRE]

Define

\[
K_n=0.618\frac{\kappa_n}{1+\kappa_n},\quad
E=e^{-0.0577},\quad A_n=K_nE^n,\quad s_\ell=\sin(0.732),
\]
\[
d_0=(1,0,1),\quad d_1=(\sqrt3/2,1/2,1),\quad
d_2=(1/2,\sqrt3/2,1).
\]

The schedule and clock factors follow directly:

| n | Native state | q | \(t_c\) | \(\theta\) | \(f_n=\cos3(\theta-0.244)\) |
|---|---|---|---|---|---|
| 0 | \(\Omega^{(0)}\) | 0 | 0 | 0 | \(c>0\) |
| 1 | \(\Omega^{(1)}\) | 1 | 0.1 | \(\pi/6\) | \(s_\ell>0\) |
| 2 | \(\Omega^{(2)}\) | 2 | 0.2 | \(\pi/3\) | \(-c<0\) |

Indeed the harmonic arguments are \(-0.732,\pi/2-0.732,\pi-0.732\). Consequently

\[
v_0=K_0c\,d_0+C_0/2,\qquad
v_1=K_1Es_\ell\,d_1+C_1/2,
\]
\[
\boxed{v_2=-K_2E^2c\,d_2+C_2/2,\qquad
w_2=-K_2E^2c+C_{2,3}/2.} \tag{8}
\]

Both terms in the last expression come from the same second state. The source clock angle alone is not the azimuth of their sum. Observer dt is not a native integration step. [R1 §6; R4 §2.1; Z: `clock_angle`, `staged_scalar`, `macro_vector`, `blend_vectors`, `observe_staged`]

## 3. New nominal second-step enclosure, derived from the exact first image

### 3.1 Polynomial stage

The following are inherited enclosures of the exact \(\Omega_*^{(1)}\), not coordinates selected within them. [R3 §7.3]

| j | \(\Re\Omega_{*,j}^{(1)}\) | \(\Im\Omega_{*,j}^{(1)}\) |
|---|---|---|
| 1 | \((0.3224,0.3230)\) | \((0.0947,0.0957)\) |
| 2 | \((-0.2594,-0.2587)\) | \((0.1111,0.1118)\) |
| 3 | \((-0.2451,-0.2444)\) | \((0.2062,0.2069)\) |

Magnitude preservation lets us use the tighter inherited intensity intervals from R4 §2.2:

\[
\begin{split}
0.1131079034&<|\Omega_{*,1}^{(1)}|^2<0.1132839593,\\
0.079437298&<|\Omega_{*,2}^{(1)}|^2<0.0796463434,\\
0.10253314&<|\Omega_{*,3}^{(1)}|^2<0.102587732.
\end{split} \tag{9}
\]

At the nominal configuration, B_1 has off-diagonal entries 0.2 and diagonal entries
\(0.8-0.1|\Omega_{*,1}^{(1)}|^2\),
\(0.9-0.1|\Omega_{*,2}^{(1)}|^2\),
\(1-0.1|\Omega_{*,3}^{(1)}|^2\). Thus they lie respectively in

\[
(0.78867,0.78870),\quad(0.89203,0.89206),\quad(0.98974,0.98975).
\]

Signed products in \(V_*^{(2)}=B_{1,*}\Omega_*^{(1)}\) give

| j | \(\Re V_{*,j}^{(2)}\) | \(\Im V_{*,j}^{(2)}\) | \(\lvert V_{*,j}^{(2)}\rvert\) |
|---|---|---|---|
| 1 | \((0.1533,0.1542)\) | \((0.1381,0.1393)\) | \((0.2063,0.2079)\) |
| 2 | \((-0.2160,-0.2150)\) | \((0.1592,0.1603)\) | \((0.2675,0.2690)\) |
| 3 | \((-0.2300,-0.2290)\) | \((0.2452,0.2463)\) | \((0.3355,0.3370)\) |

For example the real first component is bounded below by
\(0.78867(0.3224)-0.2(0.2594+0.2451)=0.1533666248\),
and above by
\(0.78870(0.3230)-0.2(0.2587+0.2444)=0.1541301\).
Its imaginary component is between 0.138147049 and 0.13921859 before widening to the table. The other rows use the same matrix products.

Squaring the coordinate endpoints gives the intervals

\[
\begin{array}{rcl}
|V_{*,1}^{(2)}|^2&\in&(0.04257250,0.04318213),\\
|V_{*,2}^{(2)}|^2&\in&(0.07156964,0.07235209),\\
|V_{*,3}^{(2)}|^2&\in&(0.11256404,0.11356369).
\end{array}
\]

Each lies strictly between the squares of the displayed positive magnitude bounds. Summing proves

\[
0.22670618<\kappa_{2,*}^2<0.22909791,
\qquad \boxed{0.4761<\kappa_{2,*}<0.4787.} \tag{10}
\]

The last root comparison uses \(0.4761^2=0.22667121\) and \(0.4787^2=0.22915369\). Nominal second pre-sync components are all nonzero before the following phase calculation.

### 3.2 Simultaneous phases and the actual second chirality

For this subsection abbreviate \(W=V_*^{(2)}\), \(r_j=|W_j|\),
\(p_{jk}=\Re(\overline W_jW_k)/(r_jr_k)\), and
\(s_{jk}=\Im(\overline W_jW_k)/(r_jr_k)\).
For pairs 12 and 13 the imaginary products are positive, so

\[
s_{jk}=\sqrt{1-p_{jk}^2},\qquad
T(s_{jk})=s_{jk}(4p_{jk}^2-1). \tag{11}
\]

This identity keeps useful correlation when the phase difference is close to a right angle. It avoids unnecessarily broad independent numerator/denominator bounds on s itself.

The product arithmetic needed for (11) and pair 23 is

| Pair | Product numerator used | Denominator \(r_jr_k\) | Result |
|---|---|---|---|
| 12 | \(\Re(\overline W_1W_2)\in(-0.01132168,-0.01062971)\) | \((0.05518525,0.0559251)\) | \(p_{12}\in(-0.206,-0.190)\) |
| 13 | \(\Re(\overline W_1W_3)\in(-0.00160388,-0.00079611)\) | \((0.06921365,0.0700623)\) | \(p_{13}\in(-0.024,-0.011)\) |
| 23 | \(\Im(\overline W_2W_3)\in(-0.0167440,-0.015849)\) | \((0.08974625,0.090653)\) | \(s_{23}\in(-0.187,-0.174)\) |

For example the lower real numerator in the first row is
\(-0.1542(0.2160)+0.1381(0.1592)=-0.01132168\).
Equation (11) gives \(0.9785<s_{12}<0.9819\). It follows that

\[
T(s_{12})\in(-0.841,-0.812),\qquad
T(s_{13})\in[-1,-0.9973],\qquad
T(s_{23})\in(-0.535,-0.500). \tag{12}
\]

For the first interval, the product in (11) is between
\(-0.9819(0.8556)=-0.84011364\) and
\(-0.9785(0.830256)=-0.812405496\).
For the second, \(s_{13}>0.9997\) and
\(1-4p_{13}^2>0.997696\), whose product exceeds 0.9973; the lower bound -1 is the exact sine bound. For the third, T is increasing on the stated s interval, and its endpoint values are -0.534843188 and -0.500927904.

Substituting the three intervals together into (5) with \(\lambda_*=0.17\) gives

\[
\delta_{*,1}^{(2)}\in(-0.3130,-0.3075),\quad
\delta_{*,2}^{(2)}\in(0.0470,0.0580),\quad
\delta_{*,3}^{(2)}\in(0.2545,0.2610). \tag{13}
\]

To bound the rotations, use parity, monotonicity on these intervals, and for \(0\le t\le0.313\) the alternating bounds

\[
t-t^3/6\le\sin t\le t-t^3/6+t^5/120,
\]
\[
1-t^2/2+t^4/24-t^6/720\le\cos t\le1-t^2/2+t^4/24. \tag{14}
\]

The omitted remainders have their alternating signs and are bounded by the first omitted terms. Rational endpoint substitution yields

| j | \(\cos\delta_{*,j}^{(2)}\) | \(\sin\delta_{*,j}^{(2)}\) |
|---|---|---|
| 1 | \((0.9514,0.9532)\) | \((-0.3080,-0.3026)\) |
| 2 | \((0.9983,0.9990)\) | \((0.0469,0.0580)\) |
| 3 | \((0.9661,0.9679)\) | \((0.2517,0.2581)\) |

Multiplying each W_j by its own rotation, all derived from the same W, gives

| j | \(\Re\Omega_{*,j}^{(2)}\) | \(\Im\Omega_{*,j}^{(2)}\) | \(C_{2,*,j}\) |
|---|---|---|---|
| 1 | \((0.1876,0.1899)\) | \((0.0838,0.0864)\) | \((0.0007,0.0036)\) |
| 2 | \((-0.2251,-0.2221)\) | \((0.1464,0.1501)\) | \((-0.0591,-0.0570)\) |
| 3 | \((-0.2862,-0.2829)\) | \((0.1775,0.1808)\) | \((0.0460,0.0480)\) |

The last column is the cross product of the first two columns, rather than a separately chosen offset. To expose the subtraction signs, its first component is bounded between

\[
-0.2251(0.1808)+0.2829(0.1464)=0.00071848
\]

and

\[
-0.2221(0.1775)+0.2862(0.1501)=0.00353587.
\]

The second is between -0.0590616 and -0.05700602, and the third between 0.04607662 and 0.04795263, before widening to the table. The full nonzero synchronization is therefore present in both the exact expression (6) and these enclosures.

### 3.3 Nominal second observation and its classification

Reuse the elementary bounds from R3 (28), whose square-root and alternating-series derivations remain valid:

\[
0.7438391<c<0.7438393,\quad 0.6683<s_\ell<0.6684,
\quad0.9439<E<0.9440,
\quad0.8660254<\sqrt3/2<0.86602545.
\]

In particular
\(0.89094721<E^2<0.891136\), so \(0.8909<E^2<0.8912\).
The exponential enclosure follows from the alternating degree-five/degree-four polynomials at 0.0577 with the first omitted term bounding the error; squaring preserves it because E is positive. No exponential evaluator is used.

Monotonicity of \(\kappa/(1+\kappa)\), (10), and positive products give

\[
0.1992<K_{2,*}<0.2001,\quad
0.1774<A_{2,*}<0.1784,\qquad
\boxed{0.1319<b_{2,*}:=A_{2,*}c<0.1328.} \tag{15}
\]

For example the K bounds follow by comparing 0.618 times the norm endpoints with 0.1992(1.4761) and 0.2001(1.4787). The intermediate A products exceed 0.17746728 and are below 0.17832912 before widening.

Substitution into (8) gives

\[
\boxed{
(v_{2,*})_x\in(-0.0661,-0.0641),\quad
(v_{2,*})_y\in(-0.1446,-0.1427),\quad
w_{2,*}\in(-0.1098,-0.1079).} \tag{16}
\]

Thus the positive nominal chiral height, between 0.023 and 0.024, is insufficient to offset the negative macro height. The horizontal bounds give
\(0.156<R_{2,*}<0.160\), by squaring. In particular
\(0.0641^2+0.1427^2=0.02447210>0.156^2\) and
\(0.0661^2+0.1446^2=0.02527837<0.160^2\).

With \(a<0.1465\), \(h>0.2071\), \(r>0.2886\), this already puts the exact centre’s second point strictly in the lower central slab and host interior, outside the band section with radial gap greater than 0.0095. The geometric justification of the containing radius a is given in §5. It compares at the actual point’s height and azimuth. The inherited first-point and initial bounds already prove the nominal own-observation orders stated at the beginning. The next section extends the result to the entire original box.

## 4. Uniform propagation of the unchanged original box

### 4.1 Second polynomial stage, including all parameter deviations

R4 (15), (19)–(20) supplies for every input in (2)

\[
\max_j|\Omega_j^{(1)}-\Omega_{*,j}^{(1)}|\le Q_1=0.00001639,
\qquad |\Omega_j^{(1)}|<0.34. \tag{17}
\]

Differences here use complex modulus. These are bounds on the first image of (2), not new radii for the original state. For estimation only, contain the actual correlated pair \((\Omega^{(1)},\mathcal P)\) in the product of this image enclosure and the original parameter box. Proving bounds on this larger containing set covers the actual composition with its identical parameters. It does not change that composition or introduce independently perturbed second-step inputs.

On this containing set let \(M=0.34\). We have
\(|\epsilon|<0.11\), \(|g|<0.21\), \(|\lambda|<0.18\), \(|k_j|<4.01\).
For \(|z|,|z_*|\le M\),

\[
\big||z|^2z-|z_*|^2z_*\big|\le3M^2|z-z_*|.
\]

Writing \(H_j(z,k)=z_j(k_j-|z_j|^2)\), the second-stage input bounds give

\[
|H_j-H_{*,j}|\le(4.01+3M^2)Q_1+M\delta
=4.3568Q_1+0.34\delta,
\]
\[
|H_{*,j}|\le0.34(4+0.34^2)=1.399304<1.4.
\]

The maximum absolute row sum of L_3 is 4, so its input-difference contribution is at most \(4Q_1\), and \(|(L_3\Omega_*^{(1)})_j|<1.36\). Splitting the exact difference as in R4 (13), including the products of all simultaneous deviations, gives

\[
\begin{split}
|V_j^{(2)}-V_{*,j}^{(2)}|
&\le Q_1+0.11(4.3568Q_1+0.34\delta)
+1.4\delta+0.21(4Q_1)+1.36\delta\\
&\le2.32Q_1+2.8\delta
=0.0000380528
<\boxed{D_2:=0.00004.}
\end{split} \tag{18}
\]

This is a finite-difference estimate throughout a containing set, not a centre Jacobian or first-order expansion.

The reverse triangle inequality and the newly derived nominal magnitudes now prove

\[
\boxed{
|V_1^{(2)}|>0.20626,\quad |V_2^{(2)}|>0.26746,\quad
|V_3^{(2)}|>0.33546,\qquad |V_j^{(2)}|<0.34.} \tag{19}
\]

In particular every second pre-sync magnitude exceeds 0.20. These are new second-stage nonzero bounds, proved before normalization; the first-stage lower bound has not been reused as though it applied automatically.

### 4.2 Complete second synchronization

With (19), normalized complex components satisfy

\[
|u_j^{(2)}-u_{*,j}^{(2)}|
\le\frac{2|V_j^{(2)}-V_{*,j}^{(2)}|}{|V_j^{(2)}|}
\le10D_2.
\]

The corresponding s differences are at most \(20D_2\). Since \(|T'(s)|\le9\) on [-1,1], the T differences are at most \(180D_2\). Both increments use their own same-stage vector simultaneously. Including the original lambda perturbation gives

\[
|\delta_j^{(2)}-\delta_{*,j}^{(2)}|
\le0.18(2\cdot180D_2)+2\delta
\le\boxed{G_2:=65D_2+2\delta=0.00260002.} \tag{20}
\]

There is no argument-branch ambiguity in (5). Using \(|e^{ia}-e^{ib}|\le|a-b|\) and \(|V_{*,j}^{(2)}|<0.34\),

\[
\begin{split}
|\Omega_j^{(2)}-\Omega_{*,j}^{(2)}|
&\le D_2+0.34G_2\\
&\le\boxed{Q_2:=24D_2+\delta=0.00096001.}
\end{split} \tag{21}
\]

This deliberately conservative post-phase error is larger than the pre-sync error. Neither the synchronizer nor variation of its nonzero coefficient has been omitted.

### 4.3 Same-state norm, chirality and observation errors

Synchronization preserves every component magnitude. Therefore

\[
|\kappa_2-\kappa_{2,*}|\le\sqrt3D_2<2D_2=0.00008,
\qquad \boxed{0.47602<\kappa_2<0.47878.} \tag{22}
\]

Both nominal and perturbed second component magnitudes remain below 0.34 by (19). For each cyclic pair the bilinear difference bound gives

\[
\|C_2-C_{2,*}\|_\infty\le0.68Q_2=0.0006528068. \tag{23}
\]

Together with the nominal table this yields the convenient uniform intervals

\[
\boxed{
C_{2,1}\in(0.00004,0.00426),\quad
C_{2,2}\in(-0.05976,-0.05634),\quad
C_{2,3}\in(0.04534,0.04866).} \tag{24}
\]

For nonnegative norms,

\[
\left|\frac{\kappa}{1+\kappa}-\frac{\kappa'}{1+\kappa'}\right|
=\frac{|\kappa-\kappa'|}{(1+\kappa)(1+\kappa')}\le|\kappa-\kappa'|.
\]

Every macro coordinate factor has absolute value at most one and the envelope is at most one. Consequently, at the fixed second clock,

\[
\begin{split}
\|v_2-v_{2,*}\|_\infty
&\le0.618(2D_2)+\tfrac12(0.68Q_2)\\
&=1.236D_2+0.34Q_2
=0.0003758434
<\boxed{E_2:=0.0004.}
\end{split} \tag{25}
\]

The triangle inequality is used only to bound errors; macro and chirality still originate from the same twice-updated state. Adding E_2 to the nominal interval endpoints in (16) gives, for every input of (2),

\[
\boxed{
(v_2)_x\in(-0.0665,-0.0637),\quad
(v_2)_y\in(-0.1450,-0.1423),\quad
w_2\in(-0.1102,-0.1075).} \tag{26}
\]

The nominal widths in §3 and the additional box-perturbation errors (18)–(25) are distinct parts of the proof. No shrinking, recentering or radius optimization has occurred.

## 5. Finite geometry and comparisons with the same input’s observations

### 5.1 Signed height, host and actual band section

The inherited radical bounds give

\[
0.1464<a<0.1465,\quad0.2071<h<0.2072,\quad0.2886<r<0.2887.
\]

Equation (26) proves uniformly

\[
-w_2>0.1075,\qquad h-|w_2|>0.2071-0.1102=0.0969. \tag{27}
\]

Thus every point is below the throat plane and strictly within the central slab. Its horizontal radius obeys

\[
R_2^2>0.0637^2+0.1423^2=0.02430698>0.155^2,
\]
\[
R_2^2<0.0665^2+0.1450^2=0.02544725<0.160^2. \tag{28}
\]

The host’s central filled section has unit outward panel normals \(n_k=e_{2k}\) and inequalities \(n_k\cdot v_{xy}<r\). Hence, for all three panels,

\[
\boxed{r-n_k\cdot(v_2)_{xy}\ge r-R_2>0.1286.} \tag{29}
\]

This is a positive host half-plane margin at the actual height, establishing the host part of “surrounding host space.” [R2 §2.2]

For the fixed PLUS zero face complex, let
\(e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3))\),
\(T_i=(ae_i,h)\), \(B_i=(ae_i,-h)\).
The actual band triangles remain
\([T_i,T_{i+1},B_{i+2}]\), \([T_i,B_{i+2},B_{i+1}]\).
At the input-dependent second height put \(\eta_2=(1-w_2/h)/2\). Its section has edges

\[
S_iD_i,\quad D_iS_{i+1},\qquad
S_i=(1-\eta_2)ae_i+\eta_2ae_{i+1},\quad
D_i=(1-\eta_2)ae_i+\eta_2ae_{i+2}. \tag{30}
\]

Each endpoint and every point on these finite segments is a convex combination of radius-a ring vertices; the norm triangle inequality therefore bounds its radius by a. R1 §2 establishes that this actual section is star-shaped about the contained axis. Its filled interior consequently also has radius at most a. This derives a containing disk from the actual face list; it does not replace the nonconvex section by that disk.

Because \(R_2>0\), the total point has a well-defined azimuth \(\varphi_2\). Applying the bound to the actual radial boundary at its own height and azimuth gives

\[
\boxed{R_2-R(w_2,\varphi_2)\ge R_2-a>0.155-0.1465=0.0085.} \tag{31}
\]

Thus every second point is strictly outside the filled band section, is not a band-surface contact, and by (29) belongs to the surrounding host space. The same bound gives a planar distance greater than 0.0085 to every point of the filled section at height w_2, by the reverse triangle inequality. Equation (31) is a radial and same-height planar clearance statement, not a claimed distance to the entire three-dimensional surface.

No near-upper-ring lower bound L(eta) is needed in this lower-slab proof. In particular no conclusion is drawn from a negative or loose L, and no pure height-reflection symmetry or switch to the MINUS mesh is assumed. The total horizontal coordinates in (26) are both negative; their direction has not been identified with the clock angle \(\pi/3\).

All finite upper/lower fans and shell-notch patches have \(h\le|w|\le H\). The strict height margin (27) excludes contact with each of those finite targets. It also excludes assigning this endpoint to one of their opening-height sectors. No further contact search or infinite-plane substitution is needed. [R2 §§1,3]

### 5.2 Own-observation axial and radial comparisons

The inherited R4 uniform first and initial bounds are

\[
0.16734<w_1<0.16788,\quad R_1<0.109,\quad (v_1)_x>0.10550,
\]
\[
w_0>0.3046,\qquad R_0>0.1693. \tag{32}
\]

These already include the original input’s perturbation. In particular the initial lower bounds are not comparisons with the fixed centroid P. Combining (26), (28), (32) gives

\[
\boxed{-0.06038<|w_2|-|w_1|<-0.05714,}
\]
\[
\boxed{|w_2|-|w_0|<-0.1944,}
\]
\[
\boxed{0.046<R_2-R_1<0.0545,\qquad R_2-R_0<-0.0093.} \tag{33}
\]

For example the upper axial difference uses 0.1102-0.16734, whereas the positive radial difference uses 0.155-0.109. The upper radial difference uses \(R_1\ge(v_1)_x>0.10550\). Because these inequalities hold for every input’s own quantities, no independence between observations or perturbations is assumed or needed.

The first scheduled point is inside the actual band section by R4 §5.4. The second is outside it by (31). The signed heights have opposite signs, but the absolute second height is smaller. These are statements about the three scheduled points only. The intermediate value theorem does not apply to this discrete sequence; no interpolating segment, additional clock observation, collision, throat-aperture crossing or selected exit channel is supplied.

## 6. Native-state, envelope and clock contributions

Keep the inherited attribution order, defining only accounting comparisons

\[
v_{2,N}=v(\Omega^{(2)},\pi/6,0.1),\quad
v_{2,E}=v(\Omega^{(2)},\pi/6,0.2),\quad
v_2=v(\Omega^{(2)},\pi/3,0.2).
\]

Using §2 notation gives the exact vector decomposition

\[
\begin{split}
v_{2,N}-v_1
&=\underbrace{Es_\ell(K_2-K_1)d_1}_{\Delta_{\rm norm}}
+\underbrace{(C_2-C_1)/2}_{\Delta_C},\\
v_{2,E}-v_{2,N}
&=\underbrace{K_2Es_\ell(E-1)d_1}_{\Delta_E},\\
v_2-v_{2,E}
&=\underbrace{-K_2E^2(c\,d_2+s_\ell d_1)}_{\Delta_\theta},\\
v_2-v_1&=\Delta_{\rm norm}+\Delta_C+\Delta_E+\Delta_\theta.
\end{split} \tag{34}
\]

The norm-amplitude difference is exactly

\[
K_2-K_1=0.618\frac{\kappa_2-\kappa_1}{(1+\kappa_2)(1+\kappa_1)}. \tag{35}
\]

Its sign is therefore the native norm-change sign. R4’s norm error and R3’s nominal norm interval give \(\kappa_1>0.54319844\), while (22) gives \(\kappa_2<0.47878\); the second native norm contraction is uniform. Equations (6), (7) determine the accompanying chirality change from the same state. The envelope acts only on the macro term. The final line in (34) changes both its harmonic sign and horizontal direction, with the second native state fixed. [R3 (11)–(15)]

The nominal bounds needed for height accounting are
\(K_{1,*}\in(0.2175,0.2177)\),
\(C_{1,*,3}\in(0.0603,0.0610)\) from R3, together with §3. Also

\[
0.63080837<Es_\ell<0.6309696.
\]

Signed products give the following outward enclosures. The uniform column covers every input in the original box.

| Contribution to height from observation 1 to 2 | Exact scalar | Nominal enclosure | Uniform enclosure |
|---|---|---|---|
| Native norm/amplitude | \(Es_\ell(K_2-K_1)\) | \((-0.01168,-0.01097)\) | \((-0.01172,-0.01093)\) |
| Native chirality | \((C_{2,3}-C_{1,3})/2\) | \((-0.00750,-0.00615)\) | \((-0.00784,-0.00581)\) |
| Complete native subtotal | Sum of the preceding two rows | \((-0.01918,-0.01712)\) | \((-0.01956,-0.01674)\) |
| Envelope | \(K_2Es_\ell(E-1)\) | \((-0.00709,-0.00703)\) | \((-0.007092,-0.007028)\) |
| Clock angle/harmonic | \(-K_2E^2(c+s_\ell)\) | \((-0.2520,-0.2505)\) | \((-0.2521,-0.2504)\) |

For reproducibility, \(|K_1-K_{1,*}|\le0.618(0.00000156)=0.00000096408\), and \(|K_2-K_{2,*}|<0.00004944\). Thus the error in the first row is less than 0.00004. The chiral-height error is at most

\[
\tfrac12(0.68Q_2+0.68Q_1)=0.000331976<0.00034.
\]

For the envelope row its error is less than
\(0.631(0.0561)(0.00005)<0.000002\).
For the clock row its error is less than
\(0.892(1.413)(0.00005)<0.000064\), covered by the displayed wider interval. These estimates propagate the same original perturbations; they do not perturb either clock.

All four contributions lower the height in this specified attribution order. The complete native comparison and the subsequent envelope comparison still have positive heights:

\[
0.14778<(v_{2,N})_z<0.15114,\qquad
0.140688<(v_{2,E})_z<0.144112. \tag{36}
\]

The clock comparison produces the sign reversal in this accounting order. This does not make the outcome a theorem about a negative macro factor alone: the actual second norm and positive second chiral height have been derived and bounded. In particular C has neither been frozen at C_1 nor assigned an independent fit. The total scheduled height displacement also follows directly from endpoint intervals:

\[
-0.27808<w_2-w_1<-0.27484. \tag{37}
\]

The two attribution points are not additional scheduled observations. Their full finite-region classification is unnecessary for the second-observation result, and no physical motion is attributed to the separate algebraic terms.

## 7. Compact certificate and stopping point

Every entry in this table is uniform on the original closed box (2), with one identical configuration used in both native updates.

| Property | Certified bound or margin | Basis |
|---|---|---|
| Original joint input | Six real state and six parameter deviations each at most \(10^{-8}\) | (1)–(3), inherited R4 box |
| First-image state error | \(Q_1=0.00001639\), each first-state component magnitude below 0.34 | R4; (17) |
| Second pre-sync error | Below \(D_2=0.00004\) per complex component | (18) |
| Second pre-sync nonzero margins | Magnitudes greater than 0.20626, 0.26746, 0.33546 respectively | (19) |
| Synchronization coefficient | \(0.16999999\le\lambda\le0.17000001\), retained on both steps | (2), (4) |
| Complete second-state error | At most \(Q_2=0.00096001\) per complex component | (20)–(21) |
| Second norm | \(0.47602<\kappa_2<0.47878\) | (22) |
| Second chirality | \((0.00004,0.00426)\times(-0.05976,-0.05634)\times(0.04534,0.04866)\) | (23)–(24) |
| Full second observation error | \(\lVert v_2-v_{2,*}\rVert_\infty\le0.0003758434<0.0004\) | (25) |
| Second coordinates | \((-0.0665,-0.0637)\times(-0.1450,-0.1423)\times(-0.1102,-0.1075)\) | (26) |
| Below throat | \(-w_2>0.1075\) | (27) |
| Strict central slab | \(h-\lvert w_2\rvert>0.0969\) | (27) |
| Horizontal radius | \(0.155<R_2<0.160\) | (28) |
| Host membership | Each panel margin \(r-n_k\cdot(v_2)_{xy}>0.1286\) | (29) |
| Band classification | Surrounding host space; radial and same-height planar section gap greater than 0.0085 | (30)–(31) |
| Finite fans/notches | No contact, by strict central-slab height exclusion | §5.1 |
| Distance to throat versus own first point | \(\lvert w_1\rvert-\lvert w_2\rvert>0.05714\) | (33) |
| Distance to throat versus own initial point | \(\lvert w_0\rvert-\lvert w_2\rvert>0.1944\) | (33) |
| Distance to axis versus own first point | \(R_2-R_1>0.046\) | (33) |
| Distance to axis versus own initial point | \(R_0-R_2>0.0093\) | (33) |
| Scheduled height sign change | \(w_1>0>w_2\), with no intermediate observation asserted | (26), (32) |

The unchanged box therefore admits a complete second-observation classification. The first point’s interior membership does not persist, despite the second point being closer to the throat plane. Radial inward movement from observation zero to one does not continue from one to two. These outcomes require no change of state selection, geometry, placement, clock or parameter radius.

This is a certificate for exactly two native updates from the original inputs. It establishes neither an invariant region, basin, attraction, long-time stability, historical-seed reachability, continuous passage nor physical flow. Geometry remains absent from the recurrence. It concerns ideal formulas, not binary64 execution, measurement tolerance or finite-precision safety.

The work consisted only of source/filesystem reads, written algebra and creation of this single report outside the repository. No scientific-code execution, calculator evaluation, simulation, sampled perturbation, test, implementation, viewer/application launch, repository change or publication work was performed. No third update, complete clock cycle, SRG, memory, fluid-model or fitting investigation is started. Work stops here for GPT and Hilmir’s review.

## Source locations

| Key | Exact source and consulted portions |
|---|---|
| R4 | [Completed local-robustness certificate][R4], §1 (1)–(4) exact original box and centre; §§2–4 first-image and observer errors; §§5–7 finite margins and scope |
| R3 | [Completed one-step report][R3], §§2–4 native schedule and coupled/attribution identities; §7 (21)–(31) exact first state and rational enclosures; §8 finite-region predicates |
| R2 | [Central-passage report][R2], §§1–3 actual triangles, zero throat, host nesting, finite fans and distinct notch patches |
| R1 | [Macro middle-band report][R1], §§1–3 actual PLUS face list, finite segments and star-shaped radial section; §6 clock sign pattern |
| D | [dynamics.py][D], `L3`; `DynamicsConfig`; `arg0`; `phase_sync`; `_advance`; `step3`, lines 12–104, read as text |
| RO | [readouts.py][RO], `z_chiral`, lines 7–17, raw same-state cross product |
| Z | [z_manifold.py][Z], `Clock`, `clock_angle`, `advance_clock`, lines 46–82; staged coefficients, norm, saturation, scalar and blend, 90–161; `_observe` and `observe_staged`, 189–199 |
| RUN | [_runner.py][RUN], `_step`, `_observe`, `_advance`, `_append`, and the initial sample in `run` |
| PRE | [_presets.py][PRE], `historical_observer`, lines 18–36, staged literals, clock, no memory and recomputed initialization |
| WO | [Second-observation work order][WO], original-box quantifier, fixed-configuration composition, finite-region questions, attribution convention and execution restrictions |

[R4]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_STEP_LOCAL_ROBUSTNESS_ANALYSIS_v0.1.md
[R3]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md
[R2]: C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md
[R1]: C:/Users/Notandi/.codex/reports/Z_MACRO_MIDDLE_BAND_INTERSECTION_ANALYSIS_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:27
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[RUN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py:83
[PRE]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_FULL_Z_SECOND_STEP_NEGATIVE_CLOCK_SECTOR_v0.1.md
