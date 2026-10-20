# Native Norm Growth and Chirality Change — Stage-by-Stage Explanation Through Update Four v0.1

20 October 2026 · Written mathematical analysis for GPT and Hilmir’s review

**Answer.** The two native norm increases have different finite-step balances. From state two to three, the onsite contribution is still smaller than the negative coupling contribution; the positive squared-increment remainder is essential to obtaining growth. From three to four, the coupling loss is substantially smaller, and the onsite contribution already exceeds it before that remainder is added. The unequal third channel supplies the largest positive onsite contribution in both transitions.

Chirality also has two different stage histories. From two to three, the polynomial stage reduces both the signed third component and the full chiral magnitude, and synchronization partially restores both. From three to four, both stages reduce those quantities; synchronization produces the larger reduction. At the last synchronization, all three ordinary pair-phase separations become smaller and remain near zero, with their component magnitude products held fixed. This alignment is proved for these inputs, not inferred from the name of the harmonic-three synchronizer.

These conclusions hold throughout the unchanged original closed twelve-coordinate box. Native norm growth therefore coexists with decreasing chiral magnitude and decreasing scale-independent chiral area. Direction needs separate qualifications: several directional changes are certified below, but the supplied bounds do not determine every ordering of the signed vertical projection fraction, particularly from state three to four. None of the native mechanisms accounts for the independent observer envelope or clock changes.

## 1. Fixed inputs, source authority and evidence boundary

The actual local revision inspected in the authoritative checkout,
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, is
`3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R6. The six requested primary files were read as text. Their relevant definitions agree with the inherited reports; no material definition discrepancy was found.

The work order supplies the requested scope and deliverable. The mathematical definitions below are checked against the primary source, while the previously established enclosure certificates are explicitly inherited evidence. This report does not claim independent regeneration of all earlier decimal residuals.

Retain R6 §1’s exact centre, including its original basis:

\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,\quad
a=d/2,\quad h=s/2,\quad H=1/2,
\]
\[
P=(\sqrt3a/6,-a/2-r/3,(2h+H)/3),\quad A_*=0.4635,
\quad c_*=2[P-A_*\cos(0.732)(1,0,1)],
\]
\[
L_*=\|c_*\|,\quad t_*=\sqrt{c_1^2+c_2^2},\quad
p_*=(-c_2,c_1,0)/t_*,\quad q_*=(c_*/L_*)\times p_*,
\]
\[
X_*=\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\qquad
Y_*=\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\qquad
\Omega_*=X_*p_*+iY_*q_*.
\tag{1}
\]

The basis symbols are not observer-clock variables. Set

\[
\mathcal P_*=(\epsilon_*,g_*,\lambda_*,k_{1,*},k_{2,*},k_{3,*})
=(0.1,0.2,0.17,2,3,4),\qquad \delta=10^{-8},
\]
\[
\mathcal U=\left\{(x+iy,\mathcal P):
\max_j\max(|x_j-x_{*,j}|,|y_j-y_{*,j}|)\le\delta,\quad
\max_m|\mathcal P_m-\mathcal P_{*,m}|\le\delta\right\}.
\tag{2}
\]

Every conclusion labelled uniform applies to **all twelve independently and simultaneously varying real coordinates**, including the boundary. For each input, its configuration is chosen once:

\[
\Omega^{(n)}=F_{\mathcal P}^{\circ n}(\Omega^{(0)}),\qquad 0\le n\le4.
\tag{3}
\]

There is no restart, later independent perturbation, new representative state, normalization or contact fit. Nearby inputs need not preserve norm three, real/imaginary orthogonality or initial fan contact. Unequal reference coefficients \(k=(2,3,4)\) are neither physical defaults nor a fixed-parameter threefold-symmetric configuration.

The PLUS zero geometry, \(O=(0,r,0)\), unit placement scale, zero placement rotation and throat plane \(w=0\) remain fixed. So do the staged observer coefficients \((0.618,0.577,0.244,1,0.5)\), \(N=12\), clock step one, \(dt=0.1\), recomputed initialization and absence of memory. The geometry does not enter the native recurrence. [R6 §§1–2; R4 §§1–2; R3 §7; R2 §5]

All terminating decimals below are exact rationals. The analysis concerns the ideal real/complex formulas. Only source/reference/filesystem reading, written algebra and creation of this report were used; no scientific-code or calculator execution was used.

## 2. Complete native map and retained enclosure data

For a transition \(n\to n+1\), write

\[
I_{n,j}=|\Omega_j^{(n)}|^2,\quad
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix},
\quad
B_n=\mathrm{Id}+\epsilon\operatorname{diag}(k_j-I_{n,j})+gL_3,
\]
\[
V^{(n+1)}=B_n\Omega^{(n)},\quad
\varphi_j=\operatorname{Arg}_0 V_j^{(n+1)},\quad
\Delta_j=\lambda\sum_{m\ne j}\sin3(\varphi_m-\varphi_j),
\]
\[
\Omega_j^{(n+1)}=V_j^{(n+1)}e^{i\Delta_j},\quad
\kappa_n=\|\Omega^{(n)}\|,\quad
C_n=\Re\Omega^{(n)}\times\Im\Omega^{(n)}.
\tag{4}
\]

All increments use the same pre-sync vector simultaneously. The source assigns phase zero to an exact zero component and forces its output to zero. Here the inherited stage domains below exclude such zeros, and \(0.16999999\le\lambda\le0.17000001\). \(B_n\) is the real input-dependent multiplier, not the nonlinear map’s Jacobian. [D: `arg0`, `phase_sync`, `_advance`, `step3`; RO: `z_chiral`]

### 2.1 Comparison vectors are enclosure centres

The following rational vectors and radii are inherited from R6 §§3.1–3.4. A pair denotes real and imaginary coordinates. None of these comparison vectors is substituted into the actual composition (3).

| State | Comparison component 1 | Component 2 | Component 3 |
|---|---|---|---|
| \(\widehat z_1\) | (0.322706,0.095167) | (-0.259081,0.111445) | (-0.244759,0.206520) |
| \(\widehat z_2\) | (0.188739,0.085078) | (-0.223602,0.148232) | (-0.284600,0.179065) |
| \(\widehat z_3\) | (0.072196,0.121963) | (-0.237006,0.161219) | (-0.305291,0.199972) |
| \(\widehat z_4\) | (-0.102612,0.144250) | (-0.223813,0.244521) | (-0.284466,0.308622) |

Use the maximum complex-component modulus for enclosure errors. Nominal enclosure width and original-input propagation error remain distinct:

| n | Exact nominal image’s radius about \(\widehat z_n\) | Perturbed image’s distance from exact nominal image \(Q_n\) | Sum \(t_n\) |
|---|---:|---:|---:|
| 1 | 0.000060 | 0.0000011 | 0.0000611 |
| 2 | 0.000220 | 0.0000033 | 0.0002233 |
| 3 | 0.001050 | 0.0000151 | 0.0010651 |
| 4 | 0.003900 | 0.0000557 | 0.0039557 |

The polynomial comparison vectors needed here are

| Stage | \(\widehat W_{n,1}\) | \(\widehat W_{n,2}\) | \(\widehat W_{n,3}\) |
|---|---|---|---|
| 2 | (0.153744,0.138649) | (-0.215523,0.159751) | (-0.229524,0.245724) |
| 3 | (0.048542,0.133157) | (-0.218805,0.185171) | (-0.288355,0.223702) |
| 4 | (-0.050848,0.169564) | (-0.257977,0.208159) | (-0.334187,0.253945) |

R6 certifies a complex-component error below 0.000003 between each \(\widehat W_n\) and the exact polynomial value at \(\widehat z_{n-1}\). Its whole-domain polynomial Lipschitz factor is 1.41 on these later stages, with parameter contribution below \(4\delta\). Thus the uniform pre-sync distances from \(\widehat W_2,\widehat W_3,\widehat W_4\) are below

\[
1.41t_{n-1}+4\delta+0.000003
=0.000089191,\quad0.000317893,\quad0.001504831,
\tag{5}
\]

respectively. We use the outward radii \(0.00009,0.00032,0.00151\).

**Arithmetic clarification to R6 §3.4 only:** its last displayed domain-coverage expression equals
\[
1.41(0.001050+0.0000151)+0.00000004+0.000003
=0.001504831<0.00151,
\]
rather than the printed 0.001504871. The domain and all conclusions using the larger radius are unchanged. R6 itself is preserved.

For the nominal pre-sync images alone the corresponding stage-three and stage-four radii are 0.0003132 and 0.0014835; the original-input pre-sync errors are separately bounded in R6 by 0.0000047 and 0.0000214. Equation (5) uses the unrounded joint bound.

### 2.2 Nonzero domains before phase division

R6 §3.3 covers the entire needed pre-sync domains and segments:

| Stage | Component 1 magnitude | Component 2 magnitude | Component 3 magnitude |
|---|---|---|---|
| 1 | (0.28,0.34) | (0.28,0.34) | (0.28,0.34) |
| 2 | (0.206,0.209) | (0.267,0.270) | (0.334,0.338) |
| 3 | (0.140,0.144) | (0.284,0.289) | (0.362,0.369) |
| 4 | (0.174,0.181) | (0.328,0.335) | (0.415,0.424) |

Synchronization preserves these component magnitudes. These are stage-specific bounds, not a reused first-stage lower bound. They justify all normalized components, phase derivatives and positive denominators used below.

Containing balls and interval products are conservative supersets of the correlated images of (2). They do not introduce new choices of parameters at later stages. [R6 §§3.3–3.4; R5 §§2–4; R4 §§3–4]

## 3. Exact norm budgets: contraction and the two kinds of growth

Define
\[
\mathcal H_n=\Omega^{(n)}\odot(k-I_n),\qquad
\mathcal L_n=L_3\Omega^{(n)},\qquad
D_n^{\rm step}=\epsilon\mathcal H_n+g\mathcal L_n.
\]

The expansion of \(\|\Omega^{(n)}+D_n^{\rm step}\|^2\), together with
\[
\Re\langle\Omega,L_3\Omega\rangle
=-\sum_{j<k}|\Omega_j-\Omega_k|^2,
\]
gives exactly
\[
\boxed{\kappa_{n+1}^2-\kappa_n^2
=\mathcal O_n+\mathcal G_n+\mathcal R_n,}
\tag{6}
\]
\[
\mathcal O_n=2\epsilon\sum_j I_{n,j}(k_j-I_{n,j}),\quad
\mathcal G_n=-2gJ_n,\quad
J_n=\sum_{j<k}|\Omega_j^{(n)}-\Omega_k^{(n)}|^2,\quad
\mathcal R_n=\|D_n^{\rm step}\|^2.
\]

The subsequent synchronization makes exactly zero direct change to this norm. This is the existing `intensity_budget` identity, read as a definition, not executed. [ZD: `intensity_budget`; R3 (4)–(5)]

### 3.1 Uniform budget table

Every interval in this subsection applies throughout (2).

| Transition | Onsite \(\mathcal O_n\) | Coupling \(\mathcal G_n\) | Finite-step remainder \(\mathcal R_n\) | Exact total change in \(\kappa^2\) |
|---|---|---|---|---|
| 1 → 2 | (0.16900,0.16924) | (-0.27310,-0.27283) | (0.03635,0.03653) | **(-0.06775,-0.06706)** |
| 2 → 3 | (0.14654,0.14711) | (-0.16500,-0.16426) | (0.02510,0.02562) | **(0.00664,0.00847)** |
| 3 → 4 | (0.15774,0.16009) | (-0.10210,-0.09942) | (0.02250,0.02509) | **(0.07814,0.08576)** |

The controlling linear subtotals are
\[
\mathcal O_1+\mathcal G_1\in(-0.10410,-0.10359),\quad
\mathcal O_2+\mathcal G_2\in(-0.01846,-0.01715),\quad
\mathcal O_3+\mathcal G_3\in(0.05564,0.06067).
\tag{7}
\]

At 1 → 2 the remainder is too small to offset the negative subtotal. At 2 → 3 it is essential: \(0.02510>0.01846\), while the linear subtotal alone is strictly negative. At 3 → 4 the linear subtotal is already positive, and the remainder adds further growth. Replacing (6) by a continuous-time linearized budget would give the wrong growth sign at 2 → 3.

The change from the contraction budget to the first growth budget is chiefly the reduced coupling loss:
\[
\mathcal G_2-\mathcal G_1\in(0.10783,0.10884),
\]
while the onsite total falls by between 0.02189 and 0.02270 and the remainder falls by between 0.01073 and 0.01143. Between the two growth budgets,
\[
\mathcal G_3-\mathcal G_2\in(0.06216,0.06558),\qquad
\mathcal O_3-\mathcal O_2\in(0.01063,0.01355).
\tag{8}
\]
The remainder decreases; its possible change lies in \((-0.00312,-0.00001)\). Thus the larger fourth-update gain is primarily accounted for by a smaller negative coupling term, with a smaller positive increase of the onsite term.

For the norm itself,
\[
\kappa_{n+1}-\kappa_n
=\frac{\mathcal O_n+\mathcal G_n+\mathcal R_n}
{\kappa_{n+1}+\kappa_n}.
\tag{9}
\]
The denominator is positive by §2.2. Hence the squared-norm signs just proved are also norm-change signs; no division by a potentially zero or signed quantity is used.

### 3.2 Channel and pair contributions

Retaining each unequal \(k_j\), the onsite channel terms \(2\epsilon I_{n,j}(k_j-I_{n,j})\) obey:

| n | Channel 1 | Channel 2 | Channel 3 |
|---|---|---|---|
| 1 | (0.04269,0.04274) | (0.04642,0.04650) | (0.07989,0.08000) |
| 2 | (0.01673,0.01683) | (0.04206,0.04224) | (0.08775,0.08804) |
| 3 | (0.00782,0.00809) | (0.04756,0.04834) | (0.10236,0.10366) |

At every row, channel three exceeds channel two, which exceeds channel one, with separated bounds. From incoming state two to three, the first onsite contribution falls, while the second and third rise; the third supplies the largest positive change. These are channel-resolved effects, not a replacement of the unequal \(k_j\) by a symmetric coefficient.

The corresponding pair squared differences are:

| n | Pair 12 | Pair 13 | Pair 23 |
|---|---|---|---|
| 1 | (0.33859,0.33889) | (0.33427,0.33457) | (0.00922,0.00927) |
| 2 | (0.17363,0.17440) | (0.23245,0.23332) | (0.00460,0.00474) |
| 3 | (0.09581,0.09849) | (0.14693,0.15024) | (0.00582,0.00651) |

Pairs 12 and 13 supply almost all of the coupling loss. Their order is 12 > 13 > 23 at state one and 13 > 12 > 23 at states two and three. Both large pair differences decrease between states two and three, whereas the small pair-23 difference increases. Thus the falling coupling loss is not a claim that every pair difference decreases.

### 3.3 Written checks and error allowances for the new budgets

The comparison intensities, obtained by squaring the rational coordinates in §2.1, are:

| n | \(\widehat I_1\) | \(\widehat I_2\) | \(\widehat I_3\) |
|---|---:|---:|---:|
| 1 | 0.113195920325 | 0.079542952586 | 0.102557478481 |
| 2 | 0.042860676205 | 0.071970580228 | 0.113061434225 |
| 3 | 0.020087235785 | 0.082163409997 | 0.133191395465 |

For a component upper bound \(M_j\) from §2.2,
\[
|I_{n,j}-\widehat I_{n,j}|\le2M_jt_n.
\tag{10}
\]
The onsite function is increasing in I on these domains, since \(k_j-2I>0\). Its intensity derivative is bounded by \(2\epsilon k_j\). Adding the direct epsilon and \(k_j\) variations, together below \(2\cdot10^{-8}\) per channel, gives safe channel-error allowances:

| n | Channel 1 error | Channel 2 error | Channel 3 error |
|---|---:|---:|---:|
| 1 | 0.000017 | 0.000026 | 0.000034 |
| 2 | 0.000038 | 0.000073 | 0.000122 |
| 3 | 0.000123 | 0.000370 | 0.000630 |

For example, the nominal-coefficient comparison onsite terms at n=2 lie in
\((0.01677,0.01679)\), \((0.04214,0.04216)\), \((0.08788,0.08791)\).
These are rational comparison evaluations, not exact nominal-state values. Applying the displayed errors gives the uniform table.

For a comparison pair difference \(\widehat a=\widehat z_j-\widehat z_k\),
\[
\left||\Omega_j-\Omega_k|^2-|\widehat a|^2\right|
\le4|\widehat a|t_n+4t_n^2.
\tag{11}
\]
The exact comparison pair sums are
\[
\widehat J_1=0.682401478796,\quad
\widehat J_2=0.411568322980,\quad
\widehat J_3=0.251893385824.
\]
Upper bounds on the three comparison pair lengths are respectively
\((0.583,0.579,0.097)\), \((0.418,0.483,0.069)\),
and \((0.312,0.386,0.079)\). Equation (11), then multiplication by the positive \(2g\), proves the pair and coupling tables, including the variation of g.

For the remainder compare \(D_n^{\rm step}\) with
\(\widehat D_n=\widehat W_{n+1}-\widehat z_n\). The actual polynomial-stage Lipschitz estimate and its retained rational residual give
\[
\max_j|D_{n,j}^{\rm step}-\widehat D_{n,j}|
<b_n:=2.41t_n+4\delta+0.000003.
\]
\[
(b_1,b_2,b_3)=(0.000150291,0.000541193,0.002569931).
\tag{12}
\]
Exact comparison squared norms are
\[
\|\widehat D_1\|^2=0.036438669609,\quad
\|\widehat D_2\|^2=0.025360851774,\quad
\|\widehat D_3\|^2=0.023796891123.
\]
Their sums of component moduli are below 0.284, 0.232 and 0.246. Therefore
\[
\left|\mathcal R_n-\|\widehat D_n\|^2\right|
\le2b_n\sum_j|\widehat D_{n,j}|+3b_n^2
<0.000086,\ 0.000252,\ 0.001285
\tag{13}
\]
respectively. These inequalities give the remainder intervals in §3.1. In particular the small positive margin at 2 → 3 includes both inherited nominal enclosure width and all original parameter/state perturbations.

### 3.4 The mixed term is negative, not an omitted positive remainder

Exactly,
\[
\mathcal R_n=A_n^{\rm rem}+M_n^{\rm rem}+B_n^{\rm rem},
\]
\[
A_n^{\rm rem}=\epsilon^2\|\mathcal H_n\|^2,\quad
M_n^{\rm rem}=2\epsilon g\Re\langle\mathcal H_n,\mathcal L_n\rangle,\quad
B_n^{\rm rem}=g^2\|\mathcal L_n\|^2.
\tag{14}
\]
Here \(\|\mathcal L_n\|^2=3J_n\), since \(L_3^2=-3L_3\).
Also \(\|\mathcal H_n\|^2=\sum_j I_{n,j}(k_j-I_{n,j})^2\).
The function \(I(k-I)^2\) is increasing on these intensity domains because
\((k-I)(k-3I)>0\). Substitution of (10), with the original parameter intervals, gives:

| n | \(A_n^{\rm rem}\) | \(B_n^{\rm rem}\) | \(M_n^{\rm rem}\) |
|---|---|---|---|
| 1 | (0.0263,0.0265) | (0.08184,0.08194) | (-0.07209,-0.07161) |
| 2 | (0.0247,0.0251) | (0.04928,0.04950) | (-0.04950,-0.04836) |
| 3 | (0.0273,0.0281) | (0.02982,0.03064) | (-0.03624,-0.03203) |

The mixed-term intervals follow from the exact identity
\(M_n^{\rm rem}=\mathcal R_n-A_n^{\rm rem}-B_n^{\rm rem}\)
using independently justified bounds on all three quantities. For example,
\[
M_2^{\rm rem}<0.02562-0.0247-0.04928=-0.04836<0.
\]
Its sign has not been inferred from \(\mathcal R_n\ge0\). The onsite and coupling increments oppose one another in this real-inner-product sense; their negative mixed contribution belongs to their joint finite increment, not exclusively to either mechanism.

Synchronization has zero direct norm contribution at its own stage, but it supplies the phase configuration used in the next pair-distance and increment budget. This report does not isolate that future influence through a disabled-synchronization trajectory. Nor is this intensity accounting identified with physical energy conservation.

## 4. Chirality transported by the polynomial stage and changed by synchronization

Writing \(\Omega=x+iy\), expansion of the alternating two-by-two minors proves
\[
C_{V,n+1}=(B_nx)\times(B_ny)=\operatorname{cof}(B_n)C_n,
\tag{15}
\]
\[
C_{n+1}-C_n
=\underbrace{(\operatorname{cof}(B_n)-\mathrm{Id})C_n}_{\Delta C_{\rm pre}}
+\underbrace{C_{n+1}-C_{V,n+1}}_{\Delta C_{\rm sync}}.
\tag{16}
\]
No inverse is used, so (15) also holds for singular B. The cyclic source order is
\((j,k)=(2,3),(3,1),(1,2)\), giving components 1, 2, 3 respectively. [RO: `z_chiral`; R3 (6)–(8)]

For the same pre-sync vector set
\[
Q_{jk}=\overline V_jV_k=P_{jk}+iA_{jk},\qquad
d_{jk}=\Delta_k-\Delta_j.
\]
Multiplying \(Q_{jk}\) by \(e^{id_{jk}}\) and taking its imaginary part verifies the proposed rearrangement:
\[
\boxed{C_{n+1,i}=A_{jk}\cos d_{jk}+P_{jk}\sin d_{jk},}
\]
\[
\boxed{\Delta C_{{\rm sync},i}
=A_{jk}(\cos d_{jk}-1)+P_{jk}\sin d_{jk}.}
\tag{17}
\]
It is branch independent and uses the actual simultaneous increments. It introduces no new map or independent phase controls.

### 4.1 Incoming, pre-sync and post-sync components

The rational cross products needed in addition to R6’s post-sync comparison products are:
\[
C(\widehat z_2)
=(0.002147535070,-0.058009747835,0.047000770404),
\]
\[
C(\widehat W_3)
=(0.004447867595,-0.049255429219,0.038123988067),
\]
\[
C(\widehat W_4)
=(0.004052062468,-0.043753489108,0.033159143196).
\tag{18}
\]

For each cyclic component,
\[
|C_i(z)-C_i(\widehat z)|
\le |z_j-\widehat z_j||z_k|
+|\widehat z_j||z_k-\widehat z_k|.
\tag{19}
\]
The three error coefficients \(M_j+M_k\) are
\((0.608,0.547,0.479)\) at state two,
\((0.658,0.513,0.433)\) at stage three, and
\((0.759,0.605,0.516)\) at stage four.
Use \(t_2,t_3,t_4\) for synchronized states, and the smaller raw radii 0.00032 and 0.00151 for the intervening pre-sync vectors.

This proves the following **uniform** component table:

| Actual object | Component 1 | Component 2 | Signed component 3 |
|---|---|---|---|
| \(C_2\) | (0.00201,0.00229) | (-0.05814,-0.05788) | (0.04689,0.04712) |
| \(C_{V,3}\) | (0.00423,0.00466) | (-0.04942,-0.04909) | (0.03798,0.03827) |
| \(C_3\) | (0.00112,0.00253) | (-0.05222,-0.05112) | (0.04008,0.04101) |
| \(C_{V,4}\) | (0.00290,0.00520) | (-0.04467,-0.04283) | (0.03237,0.03394) |
| \(C_4\) | (0.00024,0.00080) | (-0.01177,-0.00697) | (0.00515,0.00924) |

The last first-component interval uses the additional relative-phase proof in §5.3. Equation (19) alone gives the valid but sign-unresolved interval \((-0.00252,0.00349)\). Thus the positive sign in this report is a new proved tightening, not an assertion that R6’s wider interval already established it.

For clarity, the corresponding **nominal-only third-component** enclosures, obtained using the nominal radii rather than \(t_n\), are:

| Exact nominal object | Third-component enclosure |
|---|---|
| \(C_{2,*}\) | (0.04689,0.04711) |
| \(C_{V,3,*}\) | (0.03798,0.03826) |
| \(C_{3,*}\) | (0.04009,0.04100) |
| \(C_{V,4,*}\) | (0.03239,0.03393) |
| \(C_{4,*}\) | (0.00518,0.00921) |

These nominal enclosures are not point estimates; (18) describes comparison vectors, not exact nominal states.

### 4.2 Signed third-component budgets

Subtracting the incoming and pre-sync bounds, then using (17) as tightened in §5.2, gives:

| Transition | \((\Delta C_{\rm pre})_3\) | \((\Delta C_{\rm sync})_3\) | Complete third-component change |
|---|---|---|---|
| 2 → 3 | (-0.00914,-0.00862) | (0.00218,0.00268) | (-0.00696,-0.00594) |
| 3 → 4 | (-0.00864,-0.00614) | (-0.02800,-0.02400) | (-0.03586,-0.03084) |

For the first transition the stages **oppose**: the pre-sync loss exceeds the positive synchronization recovery, since \(0.00862>0.00268\).
For the second they **reinforce**, and the synchronization loss is larger, since \(0.02400>0.00864\).

The first complete-change interval is the sum of its two stage intervals. The second uses \(C_4-C_3\) directly, cancelling the shared \(C_{V,4}\); adding separately widened stage intervals would be unnecessarily loose. No interval-dependency cancellation is assumed where it has not been justified.

## 5. Phase products and what the synchronizer actually does

### 5.1 Uniform products and relative increments

The real comparison products in cyclic order are
\[
(P_{23},P_{31},P_{12})(\widehat W_3)
=(0.104516638817,0.015790158804,0.014035582537),
\]
\[
(P_{23},P_{31},P_{12})(\widehat W_4)
=(0.139073496954,0.060052670556,0.048437887172).
\tag{20}
\]
The complex-product bound underlying (19) controls real as well as imaginary parts.

For the increments, R6 §3.2 gives intervals at the exact polynomial images of the comparison inputs. Phase variation from those images is bounded componentwise by raw error divided by the magnitude lower bound. At stage three use
\[
(e_1,e_2,e_3)=(0.002286,0.001127,0.000884),
\]
and at stage four use
\[
(e_1,e_2,e_3)=(0.00868,0.00461,0.00364).
\]
The bounds are valid along the nonzero segments of §2.2. Since sine is 1-Lipschitz,
\[
|\Delta_j-\widehat\Delta_j|
\le3(0.17000001)(2e_j+e_k+e_l)+2\delta.
\tag{21}
\]
Here \(\widehat\Delta\) refers to the exact polynomial comparison image, not independently rounded phases of \(\widehat W\). The raw radii used above also cover the distance to that exact image.

Equations (19)–(21) yield:

| Stage | Cyclic pair | \(P_{jk}\) | \(A_{jk}\) | \(d_{jk}\) |
|---|---|---|---|---|
| 3 | 23 | (0.10430,0.10473) | (0.00423,0.00466) | (-0.031,-0.019) |
| 3 | 31 | (0.01562,0.01596) | (-0.04942,-0.04909) | (-0.272,-0.258) |
| 3 | 12 | (0.01389,0.01418) | (0.03798,0.03827) | (0.283,0.297) |
| 4 | 23 | (0.13792,0.14023) | (0.00290,0.00520) | (-0.048,-0.003) |
| 4 | 31 | (0.05913,0.06097) | (-0.04467,-0.04283) | (0.479,0.528) |
| 4 | 12 | (0.04765,0.04922) | (0.03237,0.03394) | (-0.503,-0.452) |

The last pair-23 increment interval is deliberately coarse; its correlation with the incoming phase difference is retained in §5.3 when a sharper conclusion is needed.

### 5.2 Pair 12 explains the opposite third-component effects

At stage three, \(d_{12}\in(0.283,0.297)\). Alternating sine/cosine bounds give
\[
\sin d_{12}\in(0.279,0.293),\qquad
\cos d_{12}-1\in(-0.044,-0.039).
\]
Consequently
\[
A_{12}(\cos d_{12}-1)\in(-0.00169,-0.00148),\qquad
P_{12}\sin d_{12}\in(0.00387,0.00416).
\tag{22}
\]
The positive term dominates the negative one. Their sum lies in
\((0.00218,0.00268)\), proving the synchronization recovery used in §4.2.

The ordinary pre-sync separation \(u=\varphi_2-\varphi_1\) lies in
\((1.214,1.223)\), and after synchronization in \((1.497,1.520)\), strictly below \(\pi/2\).
Thus pair 12 moves toward a right angle, increasing its sine.
At fixed product \(r_1r_2\), where
\[
0.03976<r_1r_2<0.041616,
\]
that is an increase of the third chiral component. It is not ordinary alignment toward zero.

For the same stage, \(v=\varphi_3-\varphi_2\in(0.0404,0.0447)\).
Adding \(d_{23}\) puts its post-sync separation in \((0.0094,0.0257)\), closer to zero. The 13 separation instead moves from \((1.2544,1.2677)\) to \((1.5124,1.5397)\), again toward \(\pi/2\). These inequalities explain the reduced first component and more negative second component in the table without assuming a uniform effect across pairs.

At stage four,
\[
\sin d_{12}\in(-0.483,-0.436),\qquad
\cos d_{12}-1\in(-0.124,-0.100).
\]
Both terms in (17) are now negative:
\[
A_{12}(\cos d_{12}-1)\in(-0.00421,-0.00323),\qquad
P_{12}\sin d_{12}\in(-0.02378,-0.02077).
\tag{23}
\]
Their sum lies in \((-0.02800,-0.02400)\). In particular the large negative term comes from the positive real pair product multiplied by a negative relative-phase sine. Neither changing component amplitudes during synchronization nor an observer decay factor is involved.

The trigonometric bounds in (22)–(23) follow, for example, from the alternating polynomials through sine degree 7 and cosine degree 8 on \(|d|\le0.503\), with the first omitted term controlling the error. The wider rational endpoints shown leave strict margins.

### 5.3 Last-stage ordinary alignment, with pair correlation retained

The R6 arctangent quotient intervals and the phase errors in (21) give the **actual** pre-sync phase domain
\[
u=\varphi_2-\varphi_1\in(0.587,0.614),\qquad
v=\varphi_3-\varphi_2\in(0.020,0.038).
\tag{24}
\]
All phases here are taken in the already certified quadrants; the resulting relative-phase identities are independent of adding whole turns.

The simultaneous increment formulas imply exactly
\[
u'=u+\lambda[-2\sin3u+\sin3v-\sin3(u+v)],
\]
\[
v'=v+\lambda[\sin3u-\sin3(u+v)-2\sin3v]
=b(u,v,\lambda)v,
\]
\[
b=1-\frac{2\lambda\sin(3v/2)}v
\left[\cos(3u+3v/2)+2\cos(3v/2)\right].
\tag{25}
\]
There is no independent choice of \(d_{23}\) in this expression.

On (24),
\[
-0.323<\cos(3u+3v/2)<-0.218,\quad
\cos(3v/2)>0.9983755,
\]
\[
1.49918775<\frac{\sin(3v/2)}v<1.5.
\]
Together with the original lambda interval these imply
\[
\boxed{0.091<b<0.147,\qquad 0.00182<v'<0.005586.}
\tag{26}
\]
These cosine bounds can be checked by reducing their arguments about \(\pi/2\) and using the alternating sine bounds; all remaining arguments have magnitude below 0.33.

For a tighter bound on \(u'\), R6’s comparison phase intervals give
\(\widehat u\in(0.6004,0.6007)\) and
\(\widehat d_{12}\in(-0.47774,-0.47750)\), hence
\(\widehat u'\in(0.12266,0.12320)\).
Actual deviations of u and v from the exact comparison phases are below 0.0133 and 0.0083. On the whole rectangle (24),
\[
|\partial_u u'|<1.466,\qquad
|\partial_v u'|<0.702,\qquad
|\partial_\lambda u'|\le4.
\]
For instance these follow from
\(\cos3u\in(-0.268,-0.189)\) and
\(\cos3(u+v)\in(-0.376,-0.247)\).
Integration along segments gives
\[
|u'-\widehat u'|
<1.466(0.0133)+0.702(0.0083)+4\delta
<0.025325,
\]
so
\[
\boxed{0.097<u'<0.149.}
\tag{27}
\]

Equations (24), (26), (27) prove that each of the positive separations
\(u,v,u+v\) strictly decreases and remains below \(\pi/2\). The closest multiple of pi is zero before and after. Thus the last synchronizer brings every pair closer to ordinary zero-phase alignment, without a crossing of zero. It does not align them toward pi on this box.

Every product \(r_jr_k\) is unchanged by this stage. Since sine is strictly increasing on these positive intervals, all three absolute chiral components decrease during this synchronization. In particular
\[
C_{4,1}=r_2r_3\sin v',\qquad
0.328(0.415)<r_2r_3<0.335(0.424).
\]
With (26), this proves \(0.00024<C_{4,1}<0.00080\), the sharpening used above.

This is a result about this stage’s actual phases. The third-update increase of chiral magnitude in §6, as well as the earlier increase in R3, rules out a universal “synchronization suppresses chirality” interpretation.

## 6. Signed component, magnitude, direction and state scale

### 6.1 Actual magnitude changes

Squaring the component bounds in §4.1 and comparing with rational squares gives:

| Actual object | Signed component 3 | Full magnitude \(\|C\|\) | Signed fraction \(C_3/\|C\|\) | Passive ratio \(2\|C\|/\kappa^2\) |
|---|---|---|---|---|
| \(\Omega^{(2)}\) | (0.04689,0.04712) | (0.0745,0.0749) | (0.627,0.632) | (0.652,0.659) |
| \(V^{(3)}\) | (0.03798,0.03827) | (0.0622,0.0627) | (0.607,0.614) | (0.527,0.534) |
| \(\Omega^{(3)}\) | (0.04008,0.04101) | (0.0649,0.0665) | (0.608,0.626) | (0.550,0.567) |
| \(V^{(4)}\) | (0.03237,0.03394) | (0.0537,0.0564) | (0.584,0.621) | (0.335,0.359) |
| \(\Omega^{(4)}\) | (0.00515,0.00924) | (0.0086,0.0150) | (0.592,0.620) | (0.053,0.096) |

All five chiral vectors are proved nonzero before taking their fractions. The fourth-state fraction uses the correlated phase refinement in §6.2; the other fractions follow directly from the component rectangles.

As one check on the square comparisons,
\[
0.0055528066<\|C_2\|^2<0.0056057981,
\]
which lies between \(0.0745^2\) and \(0.0749^2\).
For the fourth state, its positive first-component refinement gives
\[
\|C_4\|^2
<0.00080^2+0.01177^2+0.00924^2
=0.0002245505<0.0150^2.
\]

The **actual sequential magnitude differences**, rather than norms of vector increments, obey:

| Transition | Pre-sync magnitude change | Sync magnitude change | Complete magnitude change |
|---|---|---|---|
| 2 → 3 | (-0.0127,-0.0118) | (0.0022,0.0043) | (-0.0100,-0.0080) |
| 3 → 4 | (-0.0128,-0.0085) | (-0.0478,-0.0387) | (-0.0579,-0.0499) |

For example \(0.0649>0.0627\) proves a synchronization increase at stage three, while \(0.0150<0.0537\) proves the large decrease at stage four. The magnitude conclusions are independent checks, not deductions solely from the third component. They also satisfy the exact telescoping identity
\[
\|C_{n+1}\|^2-\|C_n\|^2
=(\|C_{V,n+1}\|^2-\|C_n\|^2)
+(\|C_{n+1}\|^2-\|C_{V,n+1}\|^2).
\tag{28}
\]

### 6.2 What is established about direction

For positive \(C_3\),
\[
\frac{C_3}{\|C\|}
=\left[1+\left(\frac{C_1}{C_3}\right)^2+
\left(\frac{C_2}{C_3}\right)^2\right]^{-1/2}.
\tag{29}
\]
Using this dependence, rather than treating numerator and norm as independent, proves the first four fraction intervals in the table. For example the upper third-state fraction is below 0.626 because
\[
0.04101^2
<0.626^2(0.04101^2+0.05112^2+0.00112^2).
\]
The second-state fraction is above 0.627 by the analogous lower-bound comparison. Thus the complete 2 → 3 transition has both magnitude loss and a strictly smaller vertical projection fraction. The polynomial stage alone also decreases that fraction, from above 0.627 to below 0.614.

For the last fraction, the squares of the rational \(\widehat W_4\) components are
\[
0.031337469200,\quad0.109882301810,\quad0.176169013994.
\]
Positive-root comparisons followed by the 0.00151 radius give
\[
r_1\in(0.17551,0.17854),\quad
r_2\in(0.32997,0.33300),\quad
r_3\in(0.41821,0.42124).
\]
In particular \(r_3/r_2\in(1.255,1.277)\). Using (26)–(27),
\[
-\frac{C_{4,2}}{C_{4,3}}
=\frac{r_3}{r_2}\frac{\sin(u'+v')}{\sin u'}
\in(1.270,1.351),\qquad
0<\frac{C_{4,1}}{C_{4,3}}<0.139.
\tag{30}
\]
For the first quotient use
\(\sin(u'+v')/\sin u'=\cos v'+\cot u'\sin v'\);
its lower bound exceeds 1.012 and its upper bound is below
\(1+0.005586/0.097<1.058\).
For the second use \(r_3/r_1<2.401\) and
\(\sin u'>0.9962u'\).
Equation (29) then gives \(0.592<C_{4,3}/\|C_4\|<0.620\).
For example
\(0.592^2(1+1.351^2+0.139^2)<1\) and
\(0.620^2(1+1.270^2)>1\).
This also proves a smaller fourth-state vertical fraction than at state two.

Directional changes can be shown without asserting an ordering of the vertical fraction. The positive ratios \(C_1/C_3\) obey
\[
\begin{array}{c|cccc}
\text{object}&C_2&C_{V,3}&C_3&C_{V,4}\\ \hline
C_1/C_3&(0.042,0.049)&(0.110,0.123)&(0.027,0.064)&(0.085,0.161).
\end{array}
\tag{31}
\]
The separated adjacent intervals show that neither of those polynomial stages, nor the third synchronization, acts as a scalar rescaling of its incoming chiral vector.

For the fourth synchronization, (25) retains the needed correlation:
\[
\frac{(C_{4,1}/C_{4,3})}{(C_{V,4,1}/C_{V,4,3})}
=\frac{\sin v'}{\sin v}\frac{\sin u}{\sin u'}
<
\frac{0.147}{0.99975}
\frac{0.614}{0.9962(0.097)}
<0.935<1.
\tag{32}
\]
Here \(\sin v>0.99975v\) on (24). Thus this synchronization also changes direction, in addition to decreasing magnitude.

**Unresolved by these bounds:** the sign of the vertical-fraction change during the third synchronization, during either stage of 3 → 4, and over the complete 3 → 4 transition. Their fraction intervals overlap. The supplied bounds also do not certify the net directional change over 3 → 4 merely from the two individually proved stage-direction changes; those changes could partly undo one another. No mixed behavior or constancy is inferred from overlapping bounds. No full spatial rotation law or rotation angle has been established.

The strong fourth-update loss is nevertheless a proved loss of full magnitude, not merely a loss of vertical projection. Conversely, the complete 2 → 3 third-component decrease has both a magnitude decrease and a certified decrease in vertical fraction. The identity
\(C_3=\|C\|(C_3/\|C\|)\) keeps those two statements distinct.

### 6.3 State scale and the Gram check

Introduce only as a passive analysis ratio
\[
\eta_C=\frac{2\|C\|}{\kappa^2},\qquad 0\le\eta_C\le1.
\tag{33}
\]
The sharp bound follows from the existing Gram identity; this symbol is not a new API, state normalization, evolution variable or physical efficiency.

For the table in §6.1, suitable squared-norm bounds are
\[
\kappa_2^2\in(0.22752,0.22827),\quad
\kappa_3^2\in(0.23492,0.23596),\quad
\kappa_4^2\in(0.31454,0.32023).
\tag{34}
\]
The first uses the comparison intensity sum and (10). The other two use R6’s exact comparison squared norms
0.235442230508 and 0.317388785004, with raw errors bounded by
\(2(0.144+0.289+0.369)(0.00032)\) and
\(2(0.181+0.335+0.424)(0.00151)\).
Pre-sync and post-sync traces at the same stage are identical.

The eta intervals prove a decrease at each polynomial stage, a recovery during the third synchronization and a decrease during the fourth synchronization. Across the complete transitions,
\[
\eta_C(\Omega^{(3)})<0.567<0.652<\eta_C(\Omega^{(2)}),
\]
\[
\eta_C(\Omega^{(4)})<0.096<0.550<\eta_C(\Omega^{(3)}).
\]
Thus the declining raw chiral area is accompanied by a declining area relative to squared state norm. It cannot be explained by uniform amplitude shrinkage: native norm actually increases, and a uniform nonzero complex scaling would leave eta unchanged.

For
\[
\Gamma(\Omega)=
\begin{pmatrix}\|x\|^2&x\cdot y\\x\cdot y&\|y\|^2\end{pmatrix},
\qquad
\operatorname{tr}\Gamma=\kappa^2,\quad
\det\Gamma=\|C\|^2,
\tag{35}
\]
the determinant enclosures are:

| Object | \(\det\Gamma\) |
|---|---|
| \(\Omega^{(2)}\) | (0.00555025,0.00561001) |
| \(V^{(3)}\) | (0.00386884,0.00393129) |
| \(\Omega^{(3)}\) | (0.00421201,0.00442225) |
| \(V^{(4)}\) | (0.00288369,0.00318096) |
| \(\Omega^{(4)}\) | (0.00007396,0.00022500) |

The trace grows at both polynomial updates and is unchanged by synchronization. The determinant falls at both polynomial stages, rises during the third synchronization, and falls sharply during the fourth. Its net changes from state two to three and three to four are both negative. These invariant statements give a precise account of increasing norm with diminishing real/imaginary area.

The individual real norm, imaginary norm and their dot product depend on common phase. Their trace and determinant do not; neither does C. No particular common-phase decomposition is promoted to an invariant mechanism. Norm and chirality still do not determine the next state. [ZD: `chiral_area_accounting`; R3 §§3.2–3.4; R2 §5.1]

## 7. Return to the existing full-Z attribution

Keep the existing observation law:
\[
K_n=0.618\frac{\kappa_n}{1+\kappa_n},\quad E=e^{-0.0577},\quad
f_n=\cos(n\pi/2-0.732),\quad
d_n=(\cos(n\pi/6),\sin(n\pi/6),1),
\]
\[
v_n=K_nE^nf_nd_n+\frac12C_n.
\tag{36}
\]
The runner commits the native state, advances the independent observer, then observes. The attribution retains R6’s order: native update at the old clock, envelope change, clock change. [Z: `staged_scalar`, `macro_vector`, `observe_staged`; RUN: `_step`, `_advance`, `_append`; PRE: `historical_observer`]

The refined native height identity is exactly
\[
\Delta w_{\rm native}
=E^nf_n(K_{n+1}-K_n)
+\frac12(\Delta C_{\rm pre})_3
+\frac12(\Delta C_{\rm sync})_3,
\]
\[
K_{n+1}-K_n
=0.618\frac{\kappa_{n+1}-\kappa_n}
{(1+\kappa_{n+1})(1+\kappa_n)}.
\tag{37}
\]
Both native norms grow. At the old clocks \(f_2=-\cos(0.732)<0\) and
\(f_3=-\sin(0.732)<0\), so the positive K increments make **negative** height contributions.

The uniform attribution is:

| Height contribution | 2 → 3 | 3 → 4 | Evidence |
|---|---|---|---|
| Native norm/amplitude at old clock | (-0.00201,-0.00098) | (-0.01234,-0.01104) | Inherited R6 §7 |
| Polynomial chiral stage, half third component | (-0.00457,-0.00431) | (-0.00432,-0.00307) | §4.2 |
| Synchronization chiral stage, half third component | (0.00109,0.00134) | (-0.01400,-0.01200) | §§4.2,5.2 |
| Complete native subtotal | **(-0.00549,-0.00395)** | **(-0.03027,-0.02646)** | (37), with shared pre-sync term cancelled |
| Envelope | (0.00747,0.00754) | (0.00697,0.00707) | Inherited R6 §7 |
| Clock | (0.01277,0.01287) | (0.2485,0.2509) | Inherited R6 §7 |

At 3 → 4 the tighter native subtotal uses
\((C_{4,3}-C_{3,3})/2\in(-0.01793,-0.01542)\), rather than adding the two separately widened chiral-stage intervals. This is exact cancellation of the intermediate \(C_{V,4,3}\). Both new native subtotal intervals are contained in R6’s previously certified intervals.

Writing \(c=\cos(0.732)\) and \(s_\ell=\sin(0.732)\), the inherited envelope contributions are \(K_3E^2c(1-E)\) and \(K_4E^3s_\ell(1-E)\). The clock-height contributions are \(K_3E^3(c-s_\ell)\) and \(K_4E^4(c+s_\ell)\). Their positive signs belong to the observer changes, not to native synchronization. In the stipulated accounting order, the fourth native update and envelope update still leave a negative height; the clock change produces the positive fourth scheduled height. [R6 §7]

The existing geometric classifications remain context: observations two, three and four are outside the filled band section and inside the host, with third height negative and fourth height positive. Those finite-region results are inherited, not re-proved here. The fourth harmonic’s positive return does not restore band-interior membership. [R5 §5; R6 §§4–7]

## 8. Scope and stopping point

This report explains the existing two principal transitions with exact finite-map identities and rational bounds on the original box. The 1 → 2 transition was used only for the compact norm-contraction comparison. Nominal enclosure uncertainty and original-input propagation error are kept separate, and the unresolved projection comparisons are explicitly identified.

The conclusions do not imply geometry feedback, physical deflection, continuous passage, a selected outlet, pressure, velocity, attraction or long-time behavior. No fluid, SRG or memory model was introduced. No source, repository, geometry, observer, configuration, application or prior-report changes were made; no tests, simulations, scientific-code execution, renderings or publication operations were performed.

The analysis stops at the existing fourth update. The report is returned for GPT and Hilmir’s review, without starting a further investigation.

## Source locations

| Key | Source and substantive portions |
|---|---|
| R6 | [Third/fourth-observation certificate][R6], §§1–4 exact inputs, comparison vectors, residual certificates, whole-domain bounds and norm/chirality; §7 attribution |
| R5 | [Second-observation certificate][R5], §§1–4 exact second state and inherited bounds; §6 attribution |
| R4 | [Local-robustness certificate][R4], §§1–4 original box, complete first update and first-image propagation |
| R3 | [One-native-step report][R3], §§2–4 schedule, exact intensity budget, cofactor and phase identities; §7 exact starting state |
| R2 | [Central-passage report][R2], §5 same-state constraint, Gram identity and declared plotting comparison |
| D | [dynamics.py][D], `L3`, `DynamicsConfig`, `arg0`, `phase_sync`, `_advance`, `step3` |
| RO | [readouts.py][RO], `z_chiral`, source cyclic component order |
| ZD | [z_diagnostics.py][ZD], `intensity_budget`, `chiral_area_accounting`, read as definitions only |
| Z | [z_manifold.py][Z], `Clock`, `clock_angle`, `advance_clock`, norm/saturation, staged scalar, macro vector, blend, `observe_staged` |
| RUN | [_runner.py][RUN], `_step`, `_observe`, `_advance`, `_append`, initial observation in `run` |
| PRE | [_presets.py][PRE], `historical_observer`, fixed staged coefficients and independent clock |
| WO | [Current work order][WO], mechanism questions, unchanged-input quantifiers and four-update stopping boundary |

[R6]: C:/Users/Notandi/.codex/reports/FULL_Z_THIRD_FOURTH_OBSERVATIONS_ANALYSIS_v0.1.md
[R5]: C:/Users/Notandi/.codex/reports/FULL_Z_SECOND_STEP_NEGATIVE_CLOCK_SECTOR_ANALYSIS_v0.1.md
[R4]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_STEP_LOCAL_ROBUSTNESS_ANALYSIS_v0.1.md
[R3]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md
[R2]: C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py
[ZD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py
[RUN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py
[PRE]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_NATIVE_NORM_AND_CHIRALITY_MECHANISM_v0.1.md
