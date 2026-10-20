# Full Z at Observations Three and Four — The Same Input Box Through the First Harmonic Return v0.1

20 October 2026 · Written mathematical certificate for GPT and Hilmir’s review

**Answer.** On every input of the original closed twelve-coordinate box of radius \(10^{-8}\), both new observations lie strictly **outside the actual filled band section and inside the host**, within the central slab. Observation three is below the throat plane; observation four is above it. **Band-interior membership does not return at observation four.** This conclusion includes the actual same-state chirality and does not follow from the positive fourth harmonic alone.

The new uniform coordinate enclosures are

\[
\boxed{v_3\in(0.0005,0.0014)\times(-0.1400,-0.1387)\times(-0.0939,-0.0926),}
\]
\[
\boxed{v_4\in(-0.0675,-0.0636)\times(0.1073,0.1111)\times(0.1333,0.1370).}
\]

From observation two to three, distances to the axis, throat plane and centre all decrease. From three to four, distance to the axis decreases again, but distances to the throat plane and centre increase. Both new points are closer to all three targets than their own initial point. Compared with observation one, observation four is farther from the axis but closer to the throat plane and centre. All comparisons below concern the same original input with its configuration fixed throughout four native updates.

The positive scalar harmonic at q=4 returns; neither the native state nor the full spatial observation is thereby returned. There is a scheduled height sign change between three and four, with no continuous crossing, contact or passage asserted.

## 1. Exact reference, quantifiers and sources

Retain the exact original centre from R5 (1), equivalently R4 (4), including its basis:

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,
\quad a=d/2,\quad h=s/2,\quad H=1/2,\quad O=(0,r,0),
\]
\[
P=(\sqrt3a/6,-a/2-r/3,(2h+H)/3),\quad A_*=0.4635,\quad c=\cos(0.732),
\]
\[
c_*=2[P-A_*c(1,0,1)]=(c_1,c_2,c_3),\quad
L_*=\|c_*\|,\quad t_*=\sqrt{c_1^2+c_2^2},
\]
\[
p_*=(-c_2,c_1,0)/t_*,\quad q_*=(c_*/L_*)\times p_*,
\]
\[
X_*=\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\quad
Y_*=\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\qquad
\Omega_*=X_*p_*+iY_*q_*.
\]

These basis symbols are not clock variables. Write

\[
\mathcal P_*=(\epsilon_*,g_*,\lambda_*,k_{1,*},k_{2,*},k_{3,*})
=(0.1,0.2,0.17,2,3,4),\qquad\delta=10^{-8},
\]
\[
\mathcal U=\left\{(x+iy,\mathcal P):
\max_j\max(|x_j-x_{*,j}|,|y_j-y_{*,j}|)\le\delta,
\quad\max_m|\mathcal P_m-\mathcal P_{*,m}|\le\delta\right\}. \tag{1}
\]

Every uniform assertion quantifies over **all twelve independently and simultaneously varying real coordinates of this original closed box**, including its boundary. For each input choose \(\mathcal P\) once and use

\[
\boxed{\Omega^{(n)}=F_{\mathcal P}^{\circ n}(\Omega^{(0)}),\qquad n=0,1,2,3,4.} \tag{2}
\]

There is no new perturbation, parameter selection, renormalization, contact fit or restart at a later image. Nearby inputs need not preserve the centre’s norm three, orthogonality or initial fan contact. The unequal-k reference does not supply fixed-parameter threefold dynamical symmetry.

The geometry is the PLUS zero face complex, u=0, with fixed placement \(\mu=1,\psi=0\), coordinates \(v=X-O\), and throat plane w=0. Its vertices and band faces remain

\[
e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3)),\quad
T_i=(ae_i,h),\quad B_i=(ae_i,-h),
\]
\[
[T_i,T_{i+1},B_{i+2}],\qquad[T_i,B_{i+2},B_{i+1}], \tag{3}
\]

with indices modulo six. The distinct MINUS zero mesh is not substituted. [R1 §§1–3; R2 §§1–3]

The authoritative checkout read was `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at actual local HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R5. The relevant definitions in the five requested primary source files agree with the retained report definitions. No material discrepancy was found. Existing reports and repository files, including untracked material, were preserved.

R1–R5 retain the numbering specified in the work order. This report tightens certain **proof enclosures**, not inputs or previous conclusions. Terminating decimals denote exact rationals. All bounds concern ideal real/complex formulas and were derived by written algebra; no scientific formula was evaluated by a program or calculator.

## 2. Complete continuation and the first harmonic return

Let G denote the polynomial pre-sync map. For each n=1,2,3,4,

\[
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},\qquad
V^{(n)}=G_{\mathcal P}(\Omega^{(n-1)})
=\Omega^{(n-1)}+\epsilon\Omega^{(n-1)}\odot(k-|\Omega^{(n-1)}|^2)+gL_3\Omega^{(n-1)}.
\]

All three synchronization increments use this same stage’s V simultaneously:

\[
\varphi_j=\operatorname{Arg}_0V_j,\quad
\Delta_j=\lambda\sum_{m\ne j}\sin3(\varphi_m-\varphi_j),\quad
\Omega_j^{(n)}=|V_j|e^{i(\varphi_j+\Delta_j)}. \tag{4}
\]

The source assigns zero phase to an exact zero and forces its output to zero. The coefficient remains \(0.16999999\le\lambda\le0.17000001\), so synchronization is retained. Section 3 proves nonzero magnitudes at each required stage before division. On those domains, with \(u_j=V_j/|V_j|\), \(s_{jm}=\Im(\bar u_j u_m)\),

\[
\Delta_j=\lambda\sum_{m\ne j}(3s_{jm}-4s_{jm}^3),\qquad
\Omega_j^{(n)}=V_je^{i\Delta_j}. \tag{5}
\]

Equations (2), (4), (5) continue R5’s exact second state, not a rounded state from its interval table. Norm and chirality remain coupled through this full state:

\[
\kappa_n=\|V^{(n)}\|_2=\|\Omega^{(n)}\|_2,\qquad
C_{n,i}=\Im(\overline V_j^{(n)}V_k^{(n)}e^{i(\Delta_k-\Delta_j)}), \tag{6}
\]

for cyclic pairs (j,k). In particular synchronization preserves the norm but generally changes chirality. No frozen chiral offset or reduced norm/chirality recurrence is substituted. [D: `arg0`, `phase_sync`, `_advance`, `step3`; RO: `z_chiral`; R3 §3]

Keep the staged coefficients \((0.618,0.577,0.244,1,0.5)\), N=12, clock step one, dt=0.1, recomputed initialization and no memory. The runner commits a native update, advances its independent observer, then observes. Set

\[
K_n=0.618\frac{\kappa_n}{1+\kappa_n},\quad E=e^{-0.0577},\quad
s_\ell=\sin(0.732),\quad d_n=(\cos(n\pi/6),\sin(n\pi/6),1).
\]

| n | q | \(t_c\) | Angle | \(f_n\) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | c |
| 1 | 1 | 0.1 | \(\pi/6\) | \(s_\ell\) |
| 2 | 2 | 0.2 | \(\pi/3\) | -c |
| 3 | 3 | 0.3 | \(\pi/2\) | \(-s_\ell\) |
| 4 | 4 | 0.4 | \(2\pi/3\) | c |

These follow from \(f_n=\cos(n\pi/2-0.732)\). Thus exactly

\[
\boxed{v_3=-K_3E^3s_\ell(0,1,1)+C_3/2,\qquad
v_4=K_4E^4c(-1/2,\sqrt3/2,1)+C_4/2.} \tag{7}
\]

At n=4 only the scalar harmonic equals its initial factor. The direction d_4, envelope E^4, native amplitude K_4 and chirality C_4 have all changed. Rotating v_0 does not produce v_4. Observer dt is not a native integration step; no twelfth sector or periodic orbit is investigated. [Z; RUN; PRE; R1 §6]

## 3. Tighter written enclosures without changing the input

### 3.1 Rational comparison vectors and initial inclusion

R5’s second-image error 0.00096001 is valid but deliberately coarse. Repeated global cubic bounds would amplify proof slack unnecessarily. Instead, this report uses finite-domain derivative bounds and rational comparison vectors with explicit residuals. The comparison vectors below are **centres of containing balls only**. They are neither substituted native states nor fitted inputs. Their residuals and the original-state inclusion are carried at every step.

Use the maximum of the three complex component moduli as the state norm for these bounds, denoted \(\|\cdot\|_{\infty,\mathbb C}\). In each table entry a pair denotes (real part, imaginary part).

| n | \(\widehat z_{n,1}\) | \(\widehat z_{n,2}\) | \(\widehat z_{n,3}\) |
|---|---|---|---|
| 0 | (1.461707, -0.0233543) | (-2.609395, -0.0130824) | (0, 0.2318499) |
| 1 | (0.322706, 0.095167) | (-0.259081, 0.111445) | (-0.244759, 0.206520) |
| 2 | (0.188739, 0.085078) | (-0.223602, 0.148232) | (-0.284600, 0.179065) |
| 3 | (0.072196, 0.121963) | (-0.237006, 0.161219) | (-0.305291, 0.199972) |
| 4 | (-0.102612, 0.144250) | (-0.223813, 0.244521) | (-0.284466, 0.308622) |

The exact input inclusion can be sharpened using R3’s existing intervals for c_1,c_2,c_3 and its cancellation-free formula (22). Squaring positive endpoints and substituting in the radicals gives

\[
0.6934413<t_*<0.6934422,\quad
2.9909076<X_*<2.9909079,\quad
4.313131<X_*/t_*<4.313139.
\]

For example, at the rational comparison values -0.6049880 and -0.3388967, the sum of squares is 0.48086145341489. R3’s c intervals change this by less than 0.000000431; both t endpoints bound the resulting positive root. The X bounds follow from the same positive-root comparison in its defining formula. The resulting exact-state coordinate enclosures are

| Coordinate | Refined nominal enclosure |
|---|---|
| \(x_{*,1}\) | (1.461705, 1.461710) |
| \(x_{*,2}\) | (-2.609399, -2.609390) |
| \(x_{*,3}\) | Exactly 0 |
| \(y_{*,1}\) | (-0.0233545, -0.0233541) |
| \(y_{*,2}\) | (-0.0130826, -0.0130822) |
| \(y_{*,3}\) | (0.2318496, 0.2318503) |

Consequently

\[
\|\Omega_*-\widehat z_0\|_{\infty,\mathbb C}<0.000006. \tag{8}
\]

This sharpens nominal enclosure widths only; the original input-box radius is still exactly \(10^{-8}\).

### 3.2 Written residual certificates at the comparison vectors

At \(\mathcal P_*\), the pre-sync matrix has off-diagonals 0.2 and diagonal entries \(0.8-0.1|z_1|^2,0.9-0.1|z_2|^2,1-0.1|z_3|^2\). All entries of \(G_{\mathcal P_*}(\widehat z_{n-1})\) are therefore rational numbers. The following table gives rational comparison values \(\widehat W_n\); every real and imaginary coordinate of the exact pre-sync value differs from its listed value by less than 0.000002. The complex-component difference is consequently below 0.000003.

| n | \(\widehat W_{n,1}\) | \(\widehat W_{n,2}\) | \(\widehat W_{n,3}\) |
|---|---|---|---|
| 1 | (0.3351004, 0.0300612) | (-0.2793475, 0.0388329) | (-0.2295376, 0.2233163) |
| 2 | (0.153744, 0.138649) | (-0.215523, 0.159751) | (-0.229524, 0.245724) |
| 3 | (0.048542, 0.133157) | (-0.218805, 0.185171) | (-0.288355, 0.223702) |
| 4 | (-0.050848, 0.169564) | (-0.257977, 0.208159) | (-0.334187, 0.253945) |

For example, the squared component magnitudes of \(\widehat z_2\) are exactly

\[
0.042860676205,\quad0.071970580228,\quad0.113061434225.
\]

These give the third-stage diagonal entries
0.7957139323795, 0.8928029419772, 0.9886938565775. Their signed products with the comparison coordinates give the n=3 row above. The n=4 diagonal entries obtained from \(\widehat z_3\) are 0.7979912764215, 0.8917836590003, 0.9866808604535. This makes the polynomial part of the residual calculation directly reproducible with rational arithmetic.

For a compact check of the simultaneous phase part, use the following positive rational quotient intervals. They are bounds on quotients of the **exact polynomial values at the comparison vectors**, not divisions of independently rounded entries in the preceding table. Put \(\alpha_j=\arctan t_j\).

| n | \(t_1\) | \(t_2\) | \(t_3\) | Exact phase forms |
|---|---|---|---|---|
| 1 | (0.089706, 0.089711) | (0.139012, 0.139016) | (0.013736, 0.013741) | \((\alpha_1,\pi-\alpha_2,3\pi/4+\alpha_3)\) |
| 2 | (0.051620, 0.051628) | (0.148613, 0.148624) | (0.034083, 0.034092) | \((\pi/4-\alpha_1,3\pi/4+\alpha_2,3\pi/4-\alpha_3)\) |
| 3 | (0.36453, 0.36457) | (0.08325, 0.08327) | (0.12625, 0.12628) | \((\pi/2-\alpha_1,3\pi/4+\alpha_2,3\pi/4+\alpha_3)\) |
| 4 | (0.29986, 0.29989) | (0.10686, 0.10689) | (0.13642, 0.13646) | \((\pi/2+\alpha_1,3\pi/4+\alpha_2,3\pi/4+\alpha_3)\) |

The quotient definitions follow from these quadrants. At n=3, for example,
\(t_1=\Re W_1/\Im W_1\),
\(t_2=(-\Re W_2-\Im W_2)/(-\Re W_2+\Im W_2)\), and similarly for t_3. The n=2 first quotient is \((\Re W_1-\Im W_1)/(\Re W_1+\Im W_1)\); its third quotient is \((\Im W_3+\Re W_3)/(\Im W_3-\Re W_3)\). All denominators are positive. Cross multiplication of rational endpoints proves the displayed intervals.

For \(0\le t\le0.365\), the alternating arctangent series through degree 13 has error at most \(t^{15}/15<2\cdot10^{-8}\), with the first omitted sign. Reduce the triple phase differences using their exact multiples of \(\pi/4\); their remaining arguments have magnitude below 1.5. Alternating sine/cosine polynomials through degrees 13/12 then have errors below \(4\cdot10^{-9}\). Values at multiples of \(\pi/4\) use the inherited rational bounds on \(\sqrt2\). Finally use the same alternating bounds for the increments, whose magnitudes are below 0.34. These steps require no numerical inverse-trigonometric evaluator.

They give the following outward phase-increment intervals at the comparison inputs, and then the stated complex residual bounds after multiplying W_j by its own rotation:

| n | \(\Delta_1\) | \(\Delta_2\) | \(\Delta_3\) | \(\|F_{\mathcal P_*}(\widehat z_{n-1})-\widehat z_n\|_{\infty,\mathbb C}<\rho_n\) |
|---|---|---|---|---|
| 1 | (0.19729, 0.19733) | (-0.26812, -0.26808) | (0.07077, 0.07082) | 0.00002 |
| 2 | (-0.31035, -0.31030) | (0.05243, 0.05248) | (0.25784, 0.25791) | 0.00004 |
| 3 | (-0.18495, -0.18485) | (0.10496, 0.10504) | (0.07987, 0.07995) | 0.00005 |
| 4 | (0.32690, 0.32703) | (-0.15071, -0.15060) | (-0.17636, -0.17625) | 0.00005 |

For clarity, these residuals certify the rational comparison vectors’ accuracy as enclosures; they are not a claim that those vectors solve the recurrence exactly. The actual state is always the exact composition (2).

### 3.3 Whole-domain bounds for the polynomial and phase stages

The sharper finite-difference estimates use derivatives bounded on entire containing domains, followed by integration along segments. They do not use a centre Jacobian as a substitute for a box proof.

For the polynomial stage’s own-component real two-by-two derivative, put
\(b_j=1-2g+\epsilon(k_j-|z_j|^2)\). Its radial and tangential eigenvalues are

\[
1-2g+\epsilon(k_j-3|z_j|^2),\qquad b_j.
\]

Each off-component block is g times the identity. In the first-stage input domain around \(\widehat z_0\), including (8) and the original perturbations, the own-block norms are below 1.15 and the off-block sum below 0.401. Hence a safe polynomial Lipschitz factor is 1.6. At all subsequent input domains below, component magnitudes are below 0.45; the own-block norm is below 1.000001 and the off-block sum below 0.400001. Thus the later factor is 1.41. These inequalities use the actual parameter box near (0.1,0.2,0.17,2,3,4), not broad arbitrary coefficients.

For the synchronizer write \(a_{jm}=\cos3(\varphi_m-\varphi_j)\). Its j-th derivative row, in the maximum-complex-component norm, is bounded by

\[
\boxed{\mathcal L_j\le
\max\left\{1,\left|1-3\lambda\sum_{m\ne j}a_{jm}\right|\right\}
+3|\lambda|\sum_{m\ne j}\frac{|V_j|}{|V_m|}|a_{jm}|.} \tag{9}
\]

To derive (9), resolve an input variation into radial and tangential parts. Its own radial coefficient is one, its own tangential coefficient is \(1-3\lambda\sum a_{jm}\), and each other tangential variation has coefficient \(3\lambda|V_j|a_{jm}/|V_m|\). This also explains why globally bounding the triple-angle cubic derivative separately is much looser here. Variation of lambda has output norm at most \(2|V_j||d\lambda|\).

The following domains contain the needed pre-sync segments, including both nominal-enclosure and original-input errors. Every listed magnitude bound is fresh for its stage. In particular neither third nor fourth components are assumed to remain below 0.34.

| Stage | Magnitude intervals for components 1,2,3 | \(a_{12}\) | \(a_{13}\) | \(a_{23}\) | Safe synchronizer factor |
|---|---|---|---|---|---|
| 1 | All in (0.28,0.34) | [-1,1] | [-1,1] | [-1,1] | 4 |
| 2 | (0.206,0.209), (0.267,0.270), (0.334,0.338) | (0.45,0.65) | (-0.10,0.10) | (0.80,0.90) | 2 |
| 3 | (0.140,0.144), (0.284,0.289), (0.362,0.369) | (-0.91,-0.82) | (-0.85,-0.73) | (0.97,1] | 3.2 |
| 4 | (0.174,0.181), (0.328,0.335), (0.415,0.424) | (-0.29,-0.16) | (-0.39,-0.23) | (0.98,1] | 2.6 |

Here is a check of domain coverage and the derivative factors. Relative to \(\widehat W_2,\widehat W_3,\widehat W_4\), pre-sync complex-component deviations are respectively below 0.00009, 0.00032, 0.00151, as the induction below shows. Squaring the comparison coordinates and using these radii proves the magnitude intervals, hence excludes zero before phase normalization. Along each such ball the phase deviation from its comparison direction is at most the ball radius divided by its magnitude lower bound. Triple pair differences therefore vary by at most 0.0027, 0.0138, 0.0521 respectively. The comparison phases in §3.2 give the cosine intervals in the table. For pair 23 near zero angle, bounding the angle itself before taking cosine gives the sharper positive lower bounds 0.97 and 0.98.

Substitution in (9), using \(|\lambda|<0.18\), bounds the largest rows at stages two, three and four by less than 1.86, 2.92 and 2.22 respectively. For example the stage-three third row is at most

\[
1+0.54\left(\frac{0.369}{0.140}0.85+\frac{0.369}{0.284}\right)<2.92.
\]

Its own-block maximum is one because \(a_{13}+a_{23}>0\). The stage-three first row instead retains its own factor greater than one. At stage one the general bound \(1+12(0.18)(0.34)/0.28<4\) suffices. Integration over the contained segments gives the displayed finite-difference constants; no continuity through a possible pre-sync zero is assumed.

### 3.4 Nominal enclosure induction and propagation of the original box

Let \(\varepsilon_n^{\rm enc}\) bound \(\|\Omega_*^{(n)}-\widehat z_n\|_{\infty,\mathbb C}\), and let Q_n bound the difference between the actual perturbed and exact nominal n-th states. They measure different uncertainties.

The residuals in §3.2 and the domain constants give the following nominal induction:

| n | Nominal enclosure radius \(\varepsilon_n^{\rm enc}\) | Sufficient strict bound before rounding |
|---|---|---|
| 0 | 0.000006 | (8) |
| 1 | 0.000060 | \(4(1.6)(0.000006)+0.00002=0.0000584\) |
| 2 | 0.000220 | \(2(1.41)(0.000060)+0.00004=0.0002092\) |
| 3 | 0.001050 | \(3.2(1.41)(0.000220)+0.00005=0.00104264\) |
| 4 | 0.003900 | \(2.6(1.41)(0.001050)+0.00005=0.0038993\) |

Now retain the independent original parameter deviations in (1). In the first polynomial stage, state changes contribute at most \(1.6\sqrt2\delta<2.4\delta\). On its containing domain,
\(|z_j(k_j-|z_j|^2)|<10\), \(|(L_3z)_j|<11\), and \(|\epsilon z_j|<0.27\). Parameter changes therefore contribute less than \(21.27\delta\), including products through the domain bounds. A safe first pre-sync error is \(D_1=0.00000025\). The synchronizer then gives \(Q_1\le4D_1+\delta<0.0000011\).

For each later polynomial stage the same parameter contribution is below \(4\delta\): on \(|z_j|<0.45\), the three derivative bounds are 1.9, 1.8 and 0.046. Thus

\[
D_n\le1.41Q_{n-1}+4\delta,\qquad
Q_n\le L_nD_n+2M_n\delta, \tag{10}
\]

where L_n is the synchronizer factor and M_n its current component upper bound. Using the unchanged parameter box at each stage bounds the actual fixed-parameter composition conservatively; it does not choose new parameters at that stage.

| n | Pre-sync perturbation bound D_n | Complete-state perturbation bound Q_n |
|---|---|---|
| 1 | 0.00000025 | 0.0000011 |
| 2 | 0.0000016 | 0.0000033 |
| 3 | 0.0000047 | 0.0000151 |
| 4 | 0.0000214 | 0.0000557 |

For example, the third raw bound before rounding is \(1.41(0.0000033)+4\cdot10^{-8}=0.000004693\); its post-phase bound is below \(3.2(0.0000047)+0.74\cdot10^{-8}<0.0000151\). The fourth raw bound is 0.000021331, and its post-phase bound is below \(2.6(0.0000214)+0.85\cdot10^{-8}<0.0000557\).

The promised domain coverage follows at the same induction steps. Including the 0.000003 pre-comparison rounding allowance, the later raw distances from \(\widehat W_n\) are bounded by

\[
1.41(\varepsilon_{n-1}^{\rm enc}+Q_{n-1})+4\delta+0.000003.
\]

For n=2,3,4 these are respectively 0.000089191, 0.000317893, 0.001504871, below the radii used in §3.3. The first raw ball follows from (8), the first polynomial factor and the first comparison row; it lies strictly within the stated nonzero range. At each stage the previous enclosure proves the next raw domain before the synchronizer bound is applied. There is no circular assertion of later nonzero components.

This proves the tighter Q values on the **whole original box**, not on sampled corners or newly recentered inputs. R4/R5’s broader bounds remain valid; no earlier report needs correction or alteration.

## 4. Nominal and uniform readout enclosures

### 4.1 Norm and chirality from the complete new states

Squaring the rational pre-comparison vectors gives

\[
\|\widehat W_3\|_2^2=0.235442230508,\qquad
\|\widehat W_4\|_2^2=0.317388785004.
\]

Hence their norms lie respectively in (0.4852,0.4853) and (0.5633,0.5634). For nominal norm error, use the polynomial-stage bounds rather than the larger post-phase enclosure radii. The nominal raw component errors are below 0.0003132 and 0.0014835, so their norm errors are below twice those values. It follows that

\[
\kappa_{3,*}\in(0.4845,0.4860),\quad K_{3,*}\in(0.2016,0.2022),
\]
\[
\kappa_{4,*}\in(0.5603,0.5664),\quad K_{4,*}\in(0.2219,0.2235). \tag{11}
\]

These are enclosures of exact nominal images, not the norm of a substituted comparison state. Positive-denominator cross multiplication proves the K bounds.

For chirality, the exact rational cross products of the post-sync comparison vectors are

\[
C(\widehat z_3)=(0.001824145897,-0.051671384745,0.040545329702),
\]
\[
C(\widehat z_4)=(0.000484295100,-0.009365899836,0.007194236398).
\]

For any cyclic pair j,k, the bilinear product difference is bounded by

\[
|C_i(z)-C_i(z')|\le |z_j-z'_j||z_k|+|z'_j||z_k-z'_k|. \tag{12}
\]

Use the component upper bounds from §3.3 for both comparison and true states, together with \(\varepsilon_n^{\rm enc}\). At n=3, the three error coefficients are 0.658, 0.513 and 0.433; at n=4 they are 0.759, 0.605 and 0.516. This yields

| Quantity | Nominal enclosure |
|---|---|
| \(C_{3,*}\) | \((0.0011,0.0026)\times(-0.0523,-0.0511)\times(0.0400,0.0411)\) |
| \(C_{4,*}\) | \((-0.0025,0.0035)\times(-0.0118,-0.0070)\times(0.0051,0.0093)\) |

The component-one sign at n=4 is not resolved by this enclosure and is not needed. The third components used in the total heights are positive in both cases. All three components were derived from the synchronized native states.

For the additional effect of the original input perturbation,

\[
|\kappa_n-\kappa_{n,*}|<2D_n,
\]

so the uniform norm intervals are (0.48449,0.48601) and (0.56025,0.56645). For later attribution it suffices to retain

\[
K_2\in(0.19919,0.20011),\quad K_3\in(0.20159,0.20221),\quad
K_4\in(0.22187,0.22353),
\]
\[
C_{2,3}\in(0.04599,0.04801),\quad C_{3,3}\in(0.03999,0.04111),\quad
C_{4,3}\in(0.00507,0.00933). \tag{13}
\]

The n=2 bounds combine R5’s nominal bounds with this report’s tighter Q_2. The later ones combine (11)–(12) with D_n,Q_n. Both new native norms increase: the lower third norm exceeds R5’s uniform upper second norm 0.47878, and the lower fourth norm exceeds the upper third norm. Continuing the earlier native norm contraction would therefore be incorrect.

### 4.2 Staged observation coordinates

Reuse R3/R5’s elementary rational bounds

\[
0.7438391<c<0.7438393,\quad0.6683<s_\ell<0.6684,\quad
0.9439<E<0.9440,\quad0.8660254<\sqrt3/2<0.86602545.
\]

Positive multiplication gives \(0.8409<E^3<0.8413\) and \(0.7937<E^4<0.7942\). These follow from the previously certified exponential interval, whose alternating polynomial remainder was stated in R3 §7.3; no new exponential evaluation is needed. With (11),

\[
0.1132<b_{3,*}:=K_{3,*}E^3s_\ell<0.1138,
\qquad0.1309<b_{4,*}:=K_{4,*}E^4c<0.1322.
\]

The positive products before widening include
\(K_{3,*}E^3\in(0.16952544,0.17011086)\) and
\(K_{4,*}E^4\in(0.17612203,0.1775037)\).
Substituting the nominal chirality intervals in (7) gives

| n | Nominal x | Nominal y | Nominal w |
|---|---|---|---|
| 3 | (0.00055,0.00130) | (-0.13995,-0.13875) | (-0.09380,-0.09265) |
| 4 | (-0.06735,-0.06370) | (0.1074,0.1110) | (0.13345,0.13685) |

For the original-box observation error, saturation is Lipschitz with constant one, the macro factors have absolute value at most one, and chirality satisfies (12). Therefore

\[
\|v_n-v_{n,*}\|_\infty\le1.236D_n+M_nQ_n.
\]

With M_3=0.37 and M_4=0.425 this gives, respectively,

\[
\boxed{\|v_3-v_{3,*}\|_\infty<0.000012,\qquad
\|v_4-v_{4,*}\|_\infty<0.000051.} \tag{14}
\]

The unrounded upper bounds are 0.0000113962 and 0.0000501229. Adding these errors to the nominal coordinate bounds and widening outward yields

\[
\boxed{v_3\in(0.0005,0.0014)\times(-0.1400,-0.1387)\times(-0.0939,-0.0926),}
\]
\[
\boxed{v_4\in(-0.0675,-0.0636)\times(0.1073,0.1111)\times(0.1333,0.1370).} \tag{15}
\]

Nominal enclosure width, propagated original-input error and the geometric margins below are explicitly separate quantities. Macro and chirality errors are added conservatively, without treating their native-state dependency as an independent choice.

## 5. Actual finite sections and host classifications

The inherited radical bounds give \(0.1464<a<0.1465\), \(0.2071<h<0.2072\), \(0.2886<r<0.2887\). From (15),

\[
-w_3>0.0926,\quad h-|w_3|>0.1132,\qquad
w_4>0.1333,\quad h-|w_4|>0.0701. \tag{16}
\]

Both observations are strictly in the central slab. Squaring horizontal coordinate bounds gives

\[
\boxed{0.1387<R_3<0.1401,\qquad0.1247<R_4<0.1301.} \tag{17}
\]

For example \(R_4^2>0.0636^2+0.1073^2=0.01555825>0.1247^2\), and \(R_4^2<0.0675^2+0.1111^2=0.01689946<0.1301^2\). The host section is the actual central equilateral triangle with unit normals \(n_k=e_{2k}\). Therefore every host inequality has margin

\[
r-n_k\cdot(v_3)_{xy}>0.1485,\qquad
r-n_k\cdot(v_4)_{xy}>0.1585. \tag{18}
\]

### 5.1 Observation three: a sharper containing disk from the actual segments

At its own height let \(\eta_3=(1-w_3/h)/2\). Equation (15) implies
\(0.723<\eta_3<0.727\). For the actual section vertices of (3),

\[
S_i=(1-\eta)ae_i+\eta ae_{i+1},\qquad
D_i=(1-\eta)ae_i+\eta ae_{i+2},
\]
\[
|S_i|^2=a^2(1-\eta+\eta^2),\qquad
|D_i|^2=a^2(1-3\eta+3\eta^2)\le |S_i|^2. \tag{19}
\]

Every point on S_iD_i or D_iS_{i+1} has norm at most the larger endpoint norm. The inherited star-shaped filled section is therefore also contained in that disk. Since \(1-\eta+\eta^2\) increases for \(\eta>1/2\),

\[
R(w_3,\varphi)\le a\sqrt{1-\eta_3+\eta_3^2}
<0.1465(0.896)=0.131264<0.1313.
\]

Here \(1-0.727+0.727^2=0.801529<0.896^2\). Applying this bound at the total observation’s own azimuth,

\[
\boxed{R_3-R(w_3,\varphi_3)>0.1387-0.1313=0.0074.} \tag{20}
\]

Thus observation three is outside the actual filled band section, in surrounding host space by (18). The same positive bound is a same-height planar separation from the filled section by the reverse triangle inequality. The disk is a consequence of the finite segments, not a replacement for them. No height-reflection symmetry has been used.

### 5.2 Observation four: identify its finite radial edge

Although \(R_4<a\), this alone cannot establish interior membership. Set \(k_0=\sqrt3/2\) and \(\eta_4=(1-w_4/h)/2\). Equation (15) gives
\(0.169<\eta_4<0.179\). The section endpoints of the actual triangle \([T_3,T_4,B_5]\) are

\[
D_3=a(-k_0\eta_4,1-3\eta_4/2),\qquad
S_4=a(-k_0,1/2-\eta_4).
\]

Writing p=(v_4)_{xy}, the two oriented wedge conditions are strictly positive:

\[
\frac{\det(D_3,p)}a
=(1-3\eta_4/2)|p_x|-k_0\eta_4p_y
>0.7315(0.0636)-0.8661(0.179)(0.1111)>0.029,
\]
\[
\frac{\det(p,S_4)}a
=k_0p_y-|p_x|(1/2-\eta_4)
>0.8660(0.1073)-0.0675(0.331)>0.0705. \tag{21}
\]

R1’s strict star-shaped ordering of the actual edges now identifies D_3S_4 as the radial boundary edge on this ray. This is a finite-segment check, not an intersection-of-all-half-planes assumption about a nonconvex polygon.

Its unit horizontal normal is \(n=(-1/2,k_0)\), and the segment’s line has

\[
n\cdot x=a k_0(1-\eta_4).
\]

The point’s normal projection and the line value obey

\[
n\cdot p>0.0636/2+0.8660(0.1073)=0.1247218,
\]
\[
a k_0(1-\eta_4)<0.1465(0.8661)(0.831)<0.1055.
\]

Consequently the line residual is greater than 0.0192. The ray meets the finite segment by (21), and its positive normal-direction cosine is at most one. Hence

\[
\boxed{R_4-R(w_4,\varphi_4)>0.0192.} \tag{22}
\]

This is a radial clearance and a supporting-line normal gap. It is not asserted to be the minimum planar distance to every other section edge, or a distance to the full three-dimensional surface. It proves strict exterior membership at the actual height and total-vector azimuth. Together with (18), observation four is in surrounding host space. The first observation’s band-interior membership therefore does not return.

Both new points have \(|w|<h\); all finite upper/lower fans and shell-notch patches occupy \(h\le|w|\le H\). They are excluded by the positive height margins in (16). There is no new fan or notch contact, and neither new point is a band-boundary contact. [R2 §§1–3]

## 6. Three distances and own-observation comparisons

Distinguish

\[
R_n=\|(v_n)_{xy}\|,\qquad A_n^{\rm plane}=|w_n|,\qquad
D_n=\|v_n\|=\sqrt{R_n^2+w_n^2}.
\]

Here D_n denotes distance to O; the pre-sync error bounds in §3 used the same letter with a different stated role and are not used in this section. None of these distances is distance to the boundary of the throat aperture.

First, GPT’s deduction from inherited bounds is correct. R5 (26),(28) gives

\[
D_2^2<0.02544725+0.1102^2=0.03759129<0.195^2.
\]

R4’s first-point x and height lower bounds give, even without its positive y contribution,

\[
D_1^2>0.10550^2+0.16734^2=0.0391329256>0.197^2.
\]

Thus \(D_2<0.195<0.197<D_1\), despite \(R_2>R_1\). This is a derived consequence, not an additional premise.

For the new observations, (15)–(17) imply

\[
\boxed{0.1667<D_3<0.1687,\qquad0.1825<D_4<0.1890.} \tag{23}
\]

For example the lower third squared bound is
\(0.1387^2+0.0926^2=0.02781245>0.1667^2\), and its upper bound is
\(0.1401^2+0.0939^2=0.02844522<0.1687^2\).
The fourth squared bounds are
\(0.1247^2+0.1333^2=0.03331898>0.1825^2\) and
\(0.1301^2+0.1370^2=0.03569501<0.1890^2\).

The compact table collects uniform bounds for each input’s actual observations. Rows zero through two retain the earlier classifications; their distance-to-centre bounds are elementary consequences of their inherited coordinate bounds.

| n and status | Signed height w | Axis distance R | Throat-plane distance | Centre distance D | Finite-region statement |
|---|---|---|---|---|---|
| 0, inherited input | (0.3046,0.3049) | (0.1693,0.1760) | (0.3046,0.3049) | (0.3484,0.3530) | Above band slab; exact centre initially on the upper fan; nearby inputs need not retain contact |
| 1, inherited R4 | (0.16734,0.16788) | (0.10550,0.1090) | (0.16734,0.16788) | (0.1970,0.2010) | Inside actual band section and host |
| 2, inherited R5 | (-0.1102,-0.1075) | (0.1550,0.1600) | (0.1075,0.1102) | (0.1886,0.1950) | Outside band section, inside host |
| 3, new | (-0.0939,-0.0926) | (0.1387,0.1401) | (0.0926,0.0939) | (0.1667,0.1687) | Outside band section, inside host |
| 4, new | (0.1333,0.1370) | (0.1247,0.1301) | (0.1333,0.1370) | (0.1825,0.1890) | Outside band section, inside host |

For the initial row, R4’s \(\|v_0-P\|_\infty<10^{-7}\) and P’s coordinates give \(|(v_0)_x|<0.0424\), \(|(v_0)_y|<0.1696\), hence \(R_0<0.176\). The lower squared centre distance exceeds \(0.1693^2+0.3046^2=0.12144365>0.3484^2\); the upper distance is below 0.353. The second-point lower distance uses \(0.155^2+0.1075^2=0.03558125>0.1886^2\). These comparisons do not assume initial contact for perturbed inputs.

All requested comparisons now have strict uniform signs and positive margins:

| Same-input comparison | Axis distance | Throat-plane distance | Centre distance |
|---|---|---|---|
| 3 versus preceding 2 | \(R_2-R_3>0.0149\) | \(A_2^{\rm plane}-A_3^{\rm plane}>0.0136\) | \(D_2-D_3>0.0199\) |
| 3 versus initial 0 | \(R_0-R_3>0.0292\) | \(A_0^{\rm plane}-A_3^{\rm plane}>0.2107\) | \(D_0-D_3>0.1797\) |
| 4 versus preceding 3 | \(R_3-R_4>0.0086\) | \(A_4^{\rm plane}-A_3^{\rm plane}>0.0394\) | \(D_4-D_3>0.0138\) |
| 4 versus initial 0 | \(R_0-R_4>0.0392\) | \(A_0^{\rm plane}-A_4^{\rm plane}>0.1676\) | \(D_0-D_4>0.1594\) |
| 4 versus first 1 | \(R_4-R_1>0.0157\) | \(A_1^{\rm plane}-A_4^{\rm plane}>0.03034\) | \(D_1-D_4>0.0080\) |

Uniform interval separation proves these inequalities for each input’s own sequence; no independent reselection of an earlier observation is involved. The point can approach the axis while moving farther from both the throat plane and O. Neither the scalar harmonic nor radial distance alone describes all these comparisons.

## 7. Native, envelope and clock contributions

For each transition n=2 to 3 and n=3 to 4, retain the same attribution order: first update the native state at the old observer clock, then change envelope time, then change clock angle. Direct subtraction gives

\[
\Delta_{\rm norm}=E^nf_n(K_{n+1}-K_n)d_n,\qquad
\Delta_C=(C_{n+1}-C_n)/2,
\]
\[
\Delta_E=K_{n+1}E^n(E-1)f_nd_n,
\]
\[
\Delta_\theta=K_{n+1}E^{n+1}(f_{n+1}d_{n+1}-f_nd_n),
\]
\[
\boxed{v_{n+1}-v_n=\Delta_{\rm norm}+\Delta_C+\Delta_E+\Delta_\theta,}
\qquad
K_{n+1}-K_n=0.618\frac{\kappa_{n+1}-\kappa_n}{(1+\kappa_{n+1})(1+\kappa_n)}. \tag{24}
\]

Both native norms increase here. Because each old macro sector is negative, the native amplitude increase lowers the height. Both chiral-height contributions also decrease. Conversely, envelope decay of that negative macro term **raises** the height. The clock contribution raises it in both transitions. These signs are derived from the actual intervals, not copied from the first-to-second transition.

### 7.1 Observation two to three

| Height contribution | Exact scalar | Nominal enclosure | Uniform enclosure on original box |
|---|---|---|---|
| Native norm/amplitude | \(-E^2c(K_3-K_2)\) | (-0.00199,-0.00099) | (-0.00201,-0.00098) |
| Native chirality | \((C_{3,3}-C_{2,3})/2\) | (-0.00400,-0.00245) | (-0.00401,-0.00244) |
| Complete native subtotal | Sum of preceding two rows | (-0.00599,-0.00344) | (-0.00602,-0.00342) |
| Envelope | \(K_3E^2c(1-E)\) | (0.00748,0.00753) | (0.00747,0.00754) |
| Clock | \(K_3E^3(c-s_\ell)\) | (0.01278,0.01286) | (0.01277,0.01287) |

### 7.2 Observation three to four

| Height contribution | Exact scalar | Nominal enclosure | Uniform enclosure on original box |
|---|---|---|---|
| Native norm/amplitude | \(-E^3s_\ell(K_4-K_3)\) | (-0.01232,-0.01106) | (-0.01234,-0.01104) |
| Native chirality | \((C_{4,3}-C_{3,3})/2\) | (-0.01800,-0.01535) | (-0.01802,-0.01533) |
| Complete native subtotal | Sum of preceding two rows | (-0.03032,-0.02641) | (-0.03036,-0.02637) |
| Envelope | \(K_4E^3s_\ell(1-E)\) | (0.00698,0.00706) | (0.00697,0.00707) |
| Clock | \(K_4E^4(c+s_\ell)\) | (0.2486,0.2508) | (0.2485,0.2509) |

For reproducibility, useful positive factors are

\[
E^2c\in(0.6626,0.6630),\quad E^3s_\ell\in(0.5619,0.5624),\quad
1-E\in(0.0560,0.0561),
\]
\[
c-s_\ell\in(0.0754391,0.0755393),\quad
c+s_\ell\in(1.4121391,1.4122393).
\]

Together with (11), (13), the nominal chiral intervals and R5’s nominal \(K_{2,*}\in(0.1992,0.2001)\), \(C_{2,*,3}\in(0.0460,0.0480)\), these prove both tables by signed interval multiplication. For example the first envelope’s nominal lower product is \(0.2016(0.6626)(0.056)=0.00748048896\); its uniform widening covers the original norm perturbation. The negative-sector sign has not been lost in this multiplication.

The attribution comparisons are not additional observations. Their height bounds do identify the stage responsible for the three-to-four sign change in this specified accounting order. At the old third clock, after the fourth native update, the height is between -0.12426 and -0.11897. After changing only the envelope it is still negative, with upper bound -0.11190. The clock change then gives the positive fourth height in (15). For two-to-three, both corresponding attribution heights and the final third height remain negative; the native subtotal lowers the height and the two observer contributions raise it.

This assigns algebraic contributions, not physical velocities or trajectories. The same-state chirality was retained throughout, and changing the accounting order would redistribute the intermediate terms without changing the scheduled endpoints.

## 8. Scope and stopping point

The original full box has a common strict classification at both new observations. No unresolved band-membership predicate or smaller-box fallback is needed. The necessary tightening was of nominal enclosure widths and whole-domain sensitivity bounds; it did not change the original exact centre, original box, configuration persistence, geometry, placement, clock or earlier reports.

Across observations one through four, the band-section membership is inside, outside, outside, outside. The positive harmonic at observation four does not restore interior membership. The sign change from negative third height to positive fourth height is a statement about discrete scheduled endpoints, not an intermediate-value argument or a continuous re-entry, collision, throat traversal or selected opening.

The result is a finite four-update certificate, not an invariant region, basin, attraction, stability or periodicity theorem, physical flow, historical-seed reachability claim or binary64 certificate. No fluid, pressure, velocity, force, SRG or memory model has been introduced.

Only source/reference/filesystem reads, written algebra and creation of this single report were used. No scientific-code or calculator evaluation, project import, simulation, sampling, test, implementation, rendering, viewer/application launch, repository edit or publication operation was performed. The work stops at observation four for GPT and Hilmir’s review; no fifth update or follow-on investigation is started.

## Source locations

| Key | Exact source and substantive portions |
|---|---|
| R5 | [Second-observation certificate][R5], §1 original input; §§2–4 exact second state, nominal bounds and prior perturbation certificate; §§5–7 finite-region and own-observation results |
| R4 | [Local-robustness certificate][R4], §§1–4 original closed box and first-image definitions; §5 first-point and initial bounds, actual interior margin; §7 scope |
| R3 | [One-native-step report][R3], §§2–4 map, coupled identities and attribution; §7 (21)–(31) exact state, cancellation-free coordinates, elementary rational bounds; §8 actual finite geometry |
| R2 | [Central-passage report][R2], §§1–3 fixed PLUS geometry, zero throat, host nesting, fans and finite notch domains |
| R1 | [Macro middle-band report][R1], §§1–3 actual faces, ordered star-shaped sections and finite-face planes; §6 clock factors |
| D | [dynamics.py][D], `L3`, `DynamicsConfig`, `arg0`, `phase_sync`, `_advance`, `step3`, read as text |
| RO | [readouts.py][RO], `z_chiral`, raw cross product from the native state |
| Z | [z_manifold.py][Z], `Clock`, `clock_angle`, `advance_clock`; staged configuration, norm/saturation, scalar, macro vector, blend and `observe_staged` |
| RUN | [_runner.py][RUN], `_step`, `_observe`, `_advance`, `_append`, initial sample in `run` |
| PRE | [_presets.py][PRE], `historical_observer`, staged literals, independent clock, recomputed initialization and no staged memory |
| WO | [Current work order][WO], four-total-update boundary, unchanged-box quantifier, proof tightening, finite-region/distance/attribution requirements and execution restrictions |

[R5]: C:/Users/Notandi/.codex/reports/FULL_Z_SECOND_STEP_NEGATIVE_CLOCK_SECTOR_ANALYSIS_v0.1.md
[R4]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_STEP_LOCAL_ROBUSTNESS_ANALYSIS_v0.1.md
[R3]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md
[R2]: C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md
[R1]: C:/Users/Notandi/.codex/reports/Z_MACRO_MIDDLE_BAND_INTERSECTION_ANALYSIS_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:27
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[RUN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py:83
[PRE]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_FULL_Z_THIRD_FOURTH_OBSERVATIONS_v0.1.md
