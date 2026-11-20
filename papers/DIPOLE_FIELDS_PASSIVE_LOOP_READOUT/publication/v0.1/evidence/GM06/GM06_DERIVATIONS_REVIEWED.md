# GM06 — Passive signed loop reception

20 November 2026 · Local assessment returned for review

**Verdict.** The proposed oriented contour readout distinguishes opposite steady source circulations at finite receiver radius, including a coaxial case whose vector observation vanishes at the contour center. It also distinguishes the reviewed GM05 native Fourier launch from its conjugate on a fully specified receiving copy, with a proved sufficient range \(R\ge100w\). It measures an area-averaged component of the curl of the adopted C6 vector observation. The inspected equations do not already install this contour sensor or use its scalar output in a second native triad's update.

The source remains GM05's externally worked candidate. This passive test neither identifies its internal donor nor adds receiver storage, a reciprocal force or a physical magnetic calibration.

## 1. Accepted inputs and the receiver already present

The [source map](SOURCE_MAP.md) lists exact primary labels and source lines; [SOURCE_VERIFICATION.json](SOURCE_VERIFICATION.json) records the 24 preserved primary files. The installed manual, question router, relevant claim atlas and physical correspondence register were consulted before deriving the new measurement. Their older status does not replace the newer GM04–GM05 evidence.

The [GM05 review](inputs/order/GM05_GPT_REVIEW.md) accepts the source result with a correction to common-offset examples. The [reviewed derivation](inputs/GM05_reviewed/GM05_DERIVATIONS_REVIEWED.md) is preserved beside the original so its relative links resolve. [GM05_REVIEW_DIFF.txt](GM05_REVIEW_DIFF.txt) confirms that only two paragraphs in section 4 changed. For \(j^-=\alpha DW^-+\beta_0e\), reversal yields \(j^+=-j^-+2\beta_0e\), with zero net carrier work; taking W to zero leaves \(3L\beta_0^2/2\); adding \(\beta e\) costs \(3L\beta_0\beta+3L\beta^2/2\). The six supplied exact controls pass. The original archive and its 93 manifested files are unchanged.

### 1.1 Complete geometric copies and point observations

PAIR geometry, equations **frames** and **placement**, places a full width-one shell point p as

\[
P_{mk}(p)=c_{mk}+s_mB_k(p-O),\quad
c_{mk}=O+R_m e_r(\phi_k)+h_m e_z,\quad
B_k=[e_r(\phi_k),e_z,-e_\phi(\phi_k)],\quad
\phi_k=\phi_0+2\pi k/12. \tag{1}
\]

These are proper orthonormal frames. The accepted H fixtures have \(R_m=3,\ s_m=1/4,\ h_m\in\{2a_c,a_c,0,-a_c,-2a_c\}\); the R fixtures have \(R_m\in\{2,3,4\},h_m=0,s_m=1/4\), all with \(\phi_0=\pi/2\). Here \(a_c=K_c/(1+\sqrt3/2)\) is the geometric contact height, not the carrier radius. There are 60 and 36 labeled sites, with the twelve H0/R2 sites duplicated: 84 distinct sites and frames, not a height-by-radius product.

The C6 equation in PAIR II exterior and INT carrier reads at the **body center** \(c_{mk}\):

\[
\begin{split}
U(X,t)&=\frac{g_o}{4\pi}\int\frac{p(s,t-d_X(s)/c_e)}{d_X(s)}\,ds,\\
V(X,t)&=\frac{g_o}{4\pi}\int
\frac{r_c(s,t-d_X(s)/c_e)\widehat t(s)}{d_X(s)}\,ds,\qquad
y_X=(U,B_X^TV),\quad d_X(s)=|X-\gamma(s)|.
\end{split}\tag{2}
\]

The full miniature is geometrically present, but its material extent is not sampled by that center-only rule. The same mathematical formula permits any separately specified off-wire X and known orthonormal frame. A continuous family of such evaluations is not automatically an installed continuous sensor.

Before combining sites, recover the ambient vector \(V(X_k)=B_kv_k\), where \(v_k\) is the measured vector part. A tangent component is \((B_k^Tt_k)\cdot v_k\). Summing local coordinate triples without these transformations combines different axes. U is a separate scalar observation and is unused by the contour.

PAIR I's **uniform** comparator instead reports \(B_k^TA_{\rm reg}C\), or analogous readout triples, independently of distance. Its reconstruction theorem concerns one common registered vector. It is not a reconstruction of a spatially varying C6 field from the same finite array.

### 1.2 WT samples arcs, and their actual endpoints matter

WT **actualG** specifies

\[
G_k^+=[U_k,T_{2k+1}]\cup[T_{2k+1},U_{k+1}],\quad
G_k^-=[L_k,B_{2k+1}]\cup[B_{2k+1},L_{k+1}],\quad k=0,1,2, \tag{3}
\]

with cyclic endpoints \(U_3=U_0,L_3=L_0\). In the centered width-one coordinates,
\(U_k=(r_ge_{2k},1/2)\), \(T_i=(a_ge_i,h_g)\),
\(L_k=(r_gA^\perp_{\tau_g}e_{2k},-1/2)\) and
\(B_i=(a_gA^\perp_{\tau_g}e_i,-h_g)\);
\(r_g=\sqrt3/6,\ a_g=(1-\sqrt2/2)/2,\ h_g=(\sqrt2-1)/2\),
\(e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3))\), and
\(A^\perp_{\tau_g}=I-(\tau_g/r_g)J_\perp\).
A common width w scales them; the hand reflection is applied to the complete construction.

The three upper arcs therefore concatenate into the closed polygonal walk
\(U_0,T_1,U_1,T_3,U_2,T_5,U_0\), and the lower arcs into
\(L_0,B_1,L_1,B_3,L_2,B_5,L_0\). This is an endpoint calculation, not an inference from the count six. Each has six edges; they are two separate closed paths. The upper vertices are not coplanar: the U vertices determine height \(1/2\), while each T vertex has height \(h_g\ne1/2\). Neither path is the circular disk sensor studied below.

WT uses the labeled arclength space \(Y=L^2(G;\mathbb R^4)\). Its observation \(\mathcal K_GQ\) is an ambient scalar-plus-vector field on these arcs. Its added receiving state \(\zeta\) satisfies

\[
\beta_G\dot\zeta=\sqrt2\,C_{\rm sp}c_{\rm in}
-C_{\rm sp}C_{\rm sp}^*\zeta,\qquad
(C_{\rm sp}v)(X)=a_o\sqrt M\int
\frac{(v_p,\widehat t\,v_r)(s,X)}{d_X(s)}\,ds. \tag{4}
\]

Here \(a_o=g_o/(4\pi)\), M is total arc length and \(c_{\rm in}\) is the arriving transport field, not a velocity. This map combines source labels at each X. It does not integrate the receiving vector along an oriented closed path. The loaded state \(\zeta\) is not generally equal to the instantaneous passive C6 output.

One could add a bounded functional \(\int_G t_G\cdot V\,d\ell\), with a consistently chosen edge traversal, to the continuous arc observation: its norm is at most \(\sqrt M\) on the vector L2 space. Endpoint values are irrelevant to that integral. But that functional is an additional readout. A flux interpretation would need a chosen spanning surface and clearance for that whole surface; the published individual convex-enclosure clearance does not automatically provide it. Nothing here silently fills the openings.

The retained WT/RX x is the original source state. The old receiver z has two coordinates without an assigned material location. Neither z nor \(\zeta\) is a second native complex triad. No inspected equation takes a contour output as an input to a second native F.

## 2. The proposed finite-area sensor

Take a receiving copy with a chosen allowed circle, and equip it with signed tangent measurements. No receiving carrier is activated. Let

\[
q(\theta)=X+b(\cos\theta\,e_1+\sin\theta\,e_2),\quad
t(\theta)=-\sin\theta\,e_1+\cos\theta\,e_2,\quad
u=e_1\times e_2,\quad A=\pi b^2. \tag{5}
\]

Here \(e_1,e_2\) are orthonormal, and increasing theta fixes the measured orientation. The disk \(D_b\) is a mathematical spanning disk, not a new material panel or aperture.

For V continuously differentiable on a neighborhood of the **whole disk**, Stokes' theorem gives

\[
\boxed{
S_b(X,u)=\frac1{\pi b}\int_0^{2\pi}V(q(\theta))\cdot t(\theta)\,d\theta
=\frac1{\pi b^2}\int_{D_b}H\cdot u\,dA,\qquad H=\nabla\times V.} \tag{6}
\]

It is a finite-area component measurement. It need not equal \(H(X)\cdot u\), and it is not by itself a full vector measurement. It has units V per length, the same as H in the inherited mathematical normalization.

On a steady plateau of finitely many constant source circles, V and H are smooth on any disk neighborhood separated from the source wires. A sufficient condition is
\(\delta_{\rm wire}=\min_{P\in D_b,i,s}|P-\gamma_i(s)|>0\).
All spatial derivatives can then be passed under the finite source integrals. Merely checking that the boundary does not touch a wire is insufficient; a wire may pierce the interior. General L2 C6 history statements do not by themselves give the differentiability required in (6). Our stationary comparisons do.

If \(f=H\cdot u\) is twice continuously differentiable and
\(M_2=\sup_{D_b}\|\nabla^2 f\|_{\rm op}\), Taylor's formula and the centered disk moments give

\[
\boxed{|S_b-H(X)\cdot u|\le\frac{b^2}{4}M_2.} \tag{7}
\]

Indeed the linear term averages to zero, the pointwise remainder is bounded by \(M_2|\xi|^2/2\), and the disk average of \(|\xi|^2\) is \(b^2/2\). This is an absolute error, not an assumed infinitesimal-sensor limit.

For source circles of equal radius a and signed means \(j_i\), write \(J_*=\sum_i|j_i|\). Two usable bounds are

\[
M_2\le\frac{12g_oaJ_*}{\delta_{\rm wire}^4},\qquad
|S_b-H(X)\cdot u|\le\frac{3g_oa b^2J_*}{\delta_{\rm wire}^4}. \tag{8}
\]

For the first, differentiate \(H=(g_o/4\pi)\sum j_i\oint d\gamma_i\times R/|R|^3\) twice. The directional second derivative of \(R/|R|^3\) has norm at most \(24|v|^2/|R|^4\); multiply by total weighted arclength \(2\pi aJ_*\). This also bounds the scalar Hessian operator norm through its quadratic form.

A stronger comparison is available if the receiver disk is separated by \(\delta_{\rm disk}>0\) from the **filled source disks**. GM04's source-disk representation and its Hessian derivative bound (10)–(12) yield

\[
M_2\le\frac{6g_oa^2J_*}{\delta_{\rm disk}^5},\qquad
\boxed{|S_b-H(X)\cdot u|
\le\frac{3g_oa^2b^2J_*}{2\delta_{\rm disk}^5}.} \tag{9}
\]

The source disks are also integration devices. Their stronger separation is used only for this bound, not asserted to be necessary for every contour.

### Finite sampling and the actual existing sites

At N equally spaced contour points with complete registered vector readings, the supported signed sum is

\[
S_{b,N}=\frac{2}{bN}\sum_{k=0}^{N-1}
t(\theta_k)\cdot B_kv_k,\qquad \theta_k=2\pi k/N. \tag{10}
\]

This would require installing those samples on the receiving circle. For \(F(\theta)=V(q(\theta))\cdot t(\theta)\in C^2\), the composite trapezoidal remainder gives

\[
|S_{b,N}-S_b|\le\frac{2\pi^2}{3bN^2}\sup|F''|,\quad
\sup|F''|\le b^2M_{2,V}+3bM_{1,V}+M_{0,V}. \tag{11}
\]

The coefficient follows by dividing the ordinary integral error
\((2\pi)(2\pi/N)^2\sup|F''|/12\) by \(\pi b\).
For a steady line kernel on a contour of clearance delta,

\[
\sup|F''|\le\frac{g_oaJ_*}{2}
\left(\frac{2b^2}{\delta^3}+\frac{3b}{\delta^2}+\frac1\delta\right). \tag{12}
\]

These use \(\|\nabla d^{-1}\|\le\delta^{-2}\),
\(\|\nabla^2d^{-1}\|_{\rm op}\le2\delta^{-3}\), and total weighted source arclength. Exact contour integration requires a continuous signed record, a justified quadrature limit, or a model-based reconstruction with its own error control. A finite sum is not an exact line integral for arbitrary smooth fields; unsampled contributions can change the integral.

The existing twelve module centers on an outer ring do support a different signed sum. Their tangent is \(e_\phi\), while \(B_ke_3=-e_\phi\), so

\[
S_{{\rm outer},12}=-\frac1{6R_m}\sum_{k=0}^{11}(v_k)_3. \tag{13}
\]

It approximates the vector-observation circulation around that **outer placement circle**, with (11) for \(b=R_m,N=12\) under a smooth continuous extension. It does not measure a local circle on one receiving body, and defining this aggregate is itself new processing. The repeated H0/R2 sites are not extra independent samples. Some outer-ring disks, in particular the height-zero disks containing the central source, are pierced by source wires; their boundary clearance does not justify disk Stokes or a center-H interpretation. The circular sensors below have independently verified whole-disk clearance.

## 3. Coaxial test at finite radius

Fix an oriented source circle about Y,
\(\gamma(\phi)=Y+a(\cos\phi\,e_1+\sin\phi\,e_2)\), with
\(\nu=e_1\times e_2\). Positive source mean j means tangent encoding in increasing phi. The receiver center is \(X=Y+z\nu\), \(z\ne0\); its contour uses the same basis and increasing theta, so \(u=\nu\).

For the steady source \(p=0,r=j\), the C6 vector at X is exactly zero because its distance to every source point is \(\sqrt{a^2+z^2}\) and \(\oint d\gamma=0\). The scalar U is zero too. Nevertheless GM04 gives

\[
H(X)\cdot\nu=\frac{g_oj a^2}{2(a^2+z^2)^{3/2}}. \tag{14}
\]

The exact double line integral in (6) contains
\(d\gamma\cdot dq=ab\cos(\phi-\theta)\,d\phi\,d\theta\). Rotational invariance removes the theta integral and gives

\[
\boxed{
S_b(Y+z\nu,\nu)=\frac{g_oj a}{2\pi b}
\int_0^{2\pi}
\frac{\cos\phi\,d\phi}{\sqrt{a^2+b^2+z^2-2ab\cos\phi}}.} \tag{15}
\]

Put \(C=a^2+b^2+z^2,\ q=2ab\). Since \(C-q=(a-b)^2+z^2>0\), pair positive and negative cosines:

\[
I=\int_{-\pi/2}^{\pi/2}\cos\phi
\left[(C-q\cos\phi)^{-1/2}
-(C+q\cos\phi)^{-1/2}\right]d\phi>0. \tag{16}
\]

Every interior integrand is strictly positive. This proves the sign for all \(a,b>0,z\ne0\), with no large-distance or point-sensor approximation. Integrating the derivative of \(t^{-1/2}\) over the paired interval gives the explicit bounds, for \(j>0\),

\[
\frac{g_oj a^2}{2[z^2+(a+b)^2]^{3/2}}
\le S_b\le
\frac{g_oj a^2}{2[z^2+(a-b)^2]^{3/2}}. \tag{17}
\]

The equalities are conservative bounds, not claims of attainment at finite positive radii. Empty j gives zero; replacing j by -j reverses S exactly; reversing the receiver traversal with the source fixed reverses S exactly. Reversing both restores S. Reparametrizing the source while also reversing its signed r is only a coordinate change and leaves its tangent-encoded vector unchanged.

The whole receiving disk has wire clearance
\(\sqrt{z^2+(a-b)_+^2}>0\); its distance from the filled source disk is at least \(|z|\). Thus (9) yields the finite-radius error

\[
|S_b-H(X)\cdot\nu|
\le\frac{3g_o|j|a^2b^2}{2|z|^5}. \tag{18}
\]

### Actual receiver radius and the meaning of “center”

Use the established circle \(\Gamma_0\) on a width-w copy, with

\[
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\quad
a=b=wR_\Gamma,\quad
R_\Gamma=\frac{\sqrt7K_c}{2(1+\sqrt3/2)}
=0.5364520971832998\ldots. \tag{19}
\]

The source has \(Y=O+wK_ce_y\), \(\nu=e_x\). Translate an unrotated receiving copy by \(ze_x\). Its local circle is coaxial and has center \(X=Y+ze_x\), while its **body center** is \(O_R=O+ze_x\). This is an explicitly imposed rigid test placement preserving the established copy geometry, not one of the published H/R fixture sites.

The zero-center diagnostic refers to **X, the circle center**. C6 is mathematically defined there, but a new center evaluation at X must not be conflated with the original module-center reading at \(O_R=X-wK_ce_y\). That latter reading is generally nonzero. In fact it is off the source axis. Thus the result does not claim that a geometrically coaxial copy's existing body-center sensor is necessarily silent.

The finite benchmark \(z=4w\) separates the complete copies and their circles: each full shell and its three circles lies within a radius \(w(K_c+R_\Gamma)<2w\) ball about its body center, so the two such balls are disjoint. The all-\(z\ne0\) integral theorem is broader than this collision-free full-body benchmark.

For \(w=g_o=j=1\), actual-kernel quadrature gives:

| Axial separation z | Finite contour S | Center \(H\cdot\nu\) | Bound (18) |
|---:|---:|---:|---:|
| 2 | 0.0148118125093 | 0.0162062684439 | 0.00388208527065 |
| 4 | 0.00213341379003 | 0.00218896603617 | 0.000121315164708 |
| 8 | 0.000277297390899 | 0.000279151038132 | 0.00000379109889712 |

The same finite-radius contour is checked by the single angular integral, the double line integral and a disk integral of the curl. These numbers corroborate (15)–(18); the strict-sign proof is (16), not the quadrature.

## 4. Reviewed native launch on all three displaced source circles

Use centered coordinates relative to O, the same width w, and the published ordered normals:

\[
u_k=R_z(2\pi k/3)e_y,\quad
Y_k=O+wK_cu_k,\quad
\nu_k=u_k\times e_z,\quad
T=[\nu_2\ \nu_0\ \nu_1].
\]

The reviewed minimum-source launch has means in order A/circle 2, B/circle 0, C/circle 1:

\[
j=\frac{\alpha\sqrt3}{600000000}(-28501,2,28499)^T,\qquad
Tj=\alpha W_0,\quad
W_0=\left(\frac{\sqrt3}{200000000},\frac{57}{400000},0\right)^T. \tag{20}
\]

This comes from the exact Fourier entrance at the accepted native tuple, followed by the new GM05 source impulse. Its conjugate reverses j. The means are held at their source-off steady endpoints, with p zero, as in reviewed GM05. Their energy cost remains
\(270750001L\alpha^2/40000000000000000\), with the donor still unidentified. Holding these endpoints is a comparison protocol, not active continued RX exchange.

### 4.1 A specified receiving copy

Choose the same-width receiving copy with the already defined orientation

\[
Q=B(\pi/2)=[e_y,e_z,e_x],\qquad
O_R=O+(R-wK_c)e_z,\qquad R>0. \tag{21}
\]

Place every width-one shell point p at \(O_R+wQ(p-O)\). Its local circle 0 then has

\[
X=O_R+wK_cQe_y=O+Re_z,\quad
q(\theta)=X+b(\cos\theta\,e_z+\sin\theta\,e_x),\quad
b=a=wR_\Gamma,\quad u=e_y. \tag{22}
\]

Q is a published proper frame, but the translation is an explicitly imposed axial test placement; it is not a published ring fixture, whose ring radius is positive. No new shell shape or loop radius is chosen. The circle is made into a sensor only by adding the tangent sampling and aggregation of section 2. Its geometric center X again differs from the native body center \(O_R\).

At \(R\ge100w\), the full receiving copy and its circles are well separated from the source copy and its circles by their enclosing balls. In particular the receiver disk and every filled source disk have the conservative positive clearance

\[
\delta_D\ge R-wK_c-a-b>0. \tag{23}
\]

We keep all three source centers. They are never merged into a coincident loop or silently replaced by point dipoles in the exact integral.

### 4.2 Explicit error bound and a nonzero distance range

Let \(\ell_0=wK_c\), \(J_*=\sum|j_i|\), and define the leading common-origin curl

\[
H_{\rm lead}(O+Rn)=\frac{g_o}{4\pi R^3}
\{3n(n\cdot m)-m\},\qquad m=\pi a^2\alpha W_0.
\]

At \(n=e_z\), its measured y-component is

\[
h_{\rm lead}=-\frac{g_oa^2\alpha W_{0y}}{4R^3}. \tag{24}
\]

For \(R>\ell_0+a+b\), the difference of the finite-area measurement from this signed leading value satisfies

\[
\boxed{
|S_b-h_{\rm lead}|\le g_oJ_*
\left[
\frac{6a^2\ell_0}{(R-\ell_0)^4}
+\frac{3a^4}{2(R-\ell_0-a)^5}
+\frac{3a^2b^2}{2(R-\ell_0-a-b)^5}
\right]=:\mathcal E(R).} \tag{25}
\]

Here the first term is a center-translation error, the second the accepted single-loop finite-radius error, and the third the receiver-disk averaging error (9).

For completeness, the common-origin translation uses
\(G(x)=\operatorname{Hess}|x|^{-1}=|x|^{-3}(3nn^T-I)\). Direct differentiation gives

\[
D_vG(x)=|x|^{-4}
\left[-15(n\cdot v)nn^T+3(n\cdot v)I
+3(nv^T+vn^T)\right],
\quad \|D_vG(x)\|_{\rm op}\le24|v|/|x|^4. \tag{26}
\]

The line segment from \(X-O\) to \(X-Y_i\) stays outside radius \(R-\ell_0\). Multiply its derivative estimate by \(g_o|j_i|a^2/4\) and sum to obtain the first term of (25). GM04's (15), at distances at least \(R-\ell_0\), gives the second. The source-disk/receiver-disk separation (23) gives the third. The derivative estimate holds throughout the receiver disk. Equation (25) bounds the error of its area-averaged reading relative to the central leading component.

For \(\alpha\ne0\),

\[
\frac{J_*}{|\alpha|W_{0y}}
=\frac{57002\sqrt3}{85500}<\frac65,\quad
0<K_c<1,\quad \frac12<R_\Gamma<1. \tag{27}
\]

Put \(q=w/R\le1/100\). Dividing (25) by \(|h_{\rm lead}|\) and using (27) gives the rational upper bound

\[
\frac{\mathcal E(R)}{|h_{\rm lead}|}
<
\frac{144q}{5(1-q)^4}
+\frac{36q^2}{5}\left[(1-2q)^{-5}+(1-3q)^{-5}\right].
\tag{28}
\]

Each summand increases on \(0\le q\le1/100\). At the upper endpoint the right side is exactly

\[
\frac{7804605427237675733225000}
{25890315358991719010197977}
=0.301448835945798\ldots<\frac13. \tag{29}
\]

Thus **for every \(R\ge100w\)**, with the actual fixed receiver radius \(b=wR_\Gamma\),

\[
\boxed{|S_b-h_{\rm lead}|<|h_{\rm lead}|/3.} \tag{30}
\]

For positive alpha the launch is strictly negative in this orientation and its conjugate strictly positive. The exact finite-radius integral is linear in all source means, so the conjugate response is exactly the negative, not merely opposite at leading order. Negative alpha reverses these signs; alpha zero is the inactive exception. This is a sufficient conservative range, not the earliest possible detection distance or a statement about noise sensitivity.

At \(g_o=\alpha=w=1\), computations from the actual three source loops give:

| R | Finite contour | Leading component | Bound \(\mathcal E(R)\) |
|---:|---:|---:|---:|
| 100 | \(-1.0251976124210\times10^{-11}\) | \(-1.0252192872890\times10^{-11}\) | \(2.2207690784546\times10^{-12}\) |
| 200 | \(-1.2815173359258\times10^{-12}\) | \(-1.2815241091113\times10^{-12}\) | \(1.3656205101897\times10^{-13}\) |

The run records source/receiver angular resolutions 64, 128 and 256 and an independent disk integration of H. In this native-launch placement the center V is generally **not zero**; the zero-center phenomenon belongs to the separate coaxial single-source test.

### 4.3 A certified finite-sample alternative at the benchmark

For \(R=100w\), N=1024 added equally spaced samples on the receiving circle suffice to determine the same sign, provided each signed vector sample is exact. Apply (11)–(12) using \(\delta>97w\), \(a=b>w/2\), \(a=b<w\), (27), and \(\pi^2<10\). Then

\[
\frac{|S_{b,1024}-S_b|}{|h_{\rm lead}|}
<
\frac{64000000}{1024^2}
\left(\frac2{97^3}+\frac3{97^2}+\frac1{97}\right)<\frac23. \tag{31}
\]

Since the continuous response has magnitude greater than \(2|h_{\rm lead}|/3\), this proves the discrete sum has the same sign. The sharper evaluated bound using the exact radii is \(5.34545831761952\times10^{-12}\) at unit scales; the sampled value is \(-1.02519761242099\times10^{-11}\). Equation (31), rather than floating-point evaluation of that sharper bound, certifies the sign margin.

These are additional contour samples, not the existing 84 center probes. The N=1024 bound is only asserted here at \(R=100w\); fixed N need not retain this conservative relative guarantee at arbitrarily large distance. Measurement error would require a further budget: if each tangent component error is at most epsilon, (10) adds at most \(2\epsilon/b\) to the uncertainty. No experimental resolution is assumed.

## 5. Which component is identified?

The exact observable is the single scalar disk average in (6). The centered approximation and its error are explicitly (7)–(9). In the specified native test it is a signed y-component average, with the controlled leading value (24). That already answers the passive sign question.

Three allowed normals in one copy remain coplanar under any rigid placement. Even if three center components of H could be measured at the **same** point, their matrix has rank two:

\[
\sum_{i=0}^2\nu_i\nu_i^T=\frac32(I-e_ze_z^T). \tag{32}
\]

In the body-local frame they determine the horizontal projection. In ambient coordinates a copy rotated by \(Q\) has the corresponding projector \(Q(I-e_ze_z^T)Q^T\). In local coordinates the inverse is \(H_\perp=(2/3)\sum_i\nu_i(\nu_i\cdot H)\), not the third component. The physical circles also have distinct centers \(O_R+wK_cQ u_i\); their finite-area averages are not components of one common pointwise vector in the first place. Moving them to a common point or assuming a uniform field would need an additional experiment or approximation with its own gradient and area error. We make no full-vector reconstruction claim.

The same distinction applies to the two closed WT polygonal paths. Closure supplies a possible integration domain, not an equation installing a curl-sensitive sensor, a common-plane normal or a native response.

## 6. Delay history and source-off plateaus

The source is zero before a prescribed GM05 impulse at \(t_0\), and is then held at the constant profiles used here. The new impulse supplies that discontinuity; it is not a free C1 solution across the jump.

For the receiving contour C, define

\[
\tau_{\max}^{C}=\max_{P\in C,i,s}|P-\gamma_i(s)|/c_e,\quad
\tau_{\min}^{C}=\min_{P\in C,i,s}|P-\gamma_i(s)|/c_e. \tag{33}
\]

The contour is still silent for \(t<t_0+\tau_{\min}^C\). Its whole static record is attained after \(t>t_0+\tau_{\max}^C\), provided the sources have remained constant. Intermediate readings must use the actual retarded histories. For the disk Stokes comparison and spatial derivatives, the relevant latest delay is
\(\tau_{\max}^D=\max_{P\in D_b,i,s}|P-\gamma_i(s)|/c_e\).
For this filled circular disk and the adopted straight delays, \(\tau_{\max}^D=\tau_{\max}^C\) for every source arrangement. For each fixed source point the distance to it is convex on the disk. Every interior point is a convex combination of two rim points, so its distance is at most the larger distance at those endpoints. Maximizing also over the source points proves the equality. The disk minimum can occur in the interior. The strict post-maximum inequality gives a neighborhood where the retarded arguments all lie on the smooth plateau.

In the coaxial test the largest delay for the contour and disk is
\(\sqrt{z^2+(a+b)^2}/c_e\).
The contour's minimum is \(\sqrt{z^2+(a-b)^2}/c_e\); the disk's minimum is \(\sqrt{z^2+(a-b)_+^2}/c_e\).
For the native placement, sufficient disk-wide bounds are

\[
\frac{R-\ell_0-a-b}{c_e}\le\tau_{\min}^D
\le\tau_{\max}^D\le\frac{R+\ell_0+a+b}{c_e}. \tag{34}
\]

At \(R=100w,b=a\), the right side is \(101.82961419736\,w/c_e\), and the clearance bound is \(98.17038580264\,w\). A center-only delay window does not suffice for a contour or disk measurement. If the source changes again, all sampled delayed times must still lie in the stated plateau. These are the adopted C6 straight delays with its independent speed; no electromagnetic propagation speed or native physical clock is derived.

## 7. Scope of the result and verification

| Object | Existing or added | What it reads or does |
|---|---|---|
| C6 module-center probe | Existing adopted comparison | U and signed local components of V at one body center; no loading |
| Finite H/R array | Existing specified sites | Distinct center records; the aggregate (13) would be new processing |
| WT arc observation and receiving stock | Existing extension | Continuous arc records and a loaded tangent-sector state; no oriented contour aggregate or second native triad |
| Circle sensor (6) | Proposed passive readout | Signed finite-area component of curl V, with finite-radius and delay qualifications |
| Native receiving response | Not supplied | Would need a defined native input law; a reciprocal work law is a separate choice |

[checks.py](checks.py) runs in Command Prompt through [run_python.cmd](run_python.cmd), which activates conda torment. [CHECK_RESULTS.json](CHECK_RESULTS.json) records 59 passing checks: 28 exact algebra checks, 28 quadrature checks, one floating bound evaluation, one grouped run of the six supplied GM05 review controls and one grouped byte check of 24 primary sources. All three development runs succeeded; later runs added the body-center distinction and certified finite-sampling control. No old scientific suite or production module was run.

The proofs of strict finite-radius sign, Taylor and quadrature errors, delay clearance and the all-\(R\ge100w\) range are written above. Sampled quadrature does not substitute for them. [CLAIM_LEDGER.json](CLAIM_LEDGER.json) separates inherited premises, the candidate sensor, deductions and unprovided couplings. [REVIEW_RECEIPT.json](REVIEW_RECEIPT.json) records preservation and packaging checks.

The bounded question is complete conditionally: the extended passive sensor can distinguish opposite source circulations, including the reviewed native launch. Its successful scalar reading is not yet a physical magnetic response of an autonomous second triad. The active receiver and its energy exchange remain separate choices; the GM05 donor question remains independent. No paper, publication, commit, push or production change is included.
