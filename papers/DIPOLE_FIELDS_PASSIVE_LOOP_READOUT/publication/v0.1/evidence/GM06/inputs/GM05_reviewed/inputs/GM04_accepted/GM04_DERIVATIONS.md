# Native magnetic field transfer assessment

GM04 · 20 November 2026 · Local result returned for author and GPT review

The adopted C6 observation contains a precise magnetic-dipole **curl** when its circle is independently prepared with constant nonzero tangent-encoded circulation. Its published vector output is the quantity being differentiated, not that curl. The existing native-to-carrier and carrier-to-probe links do not turn this conditional pattern into a field determined by Paper G's moment candidate \(W\).

Two independent source obstructions establish the boundary. C1 and RX preserve the circle's mean \(r_c\), so an initially empty circle cannot acquire the circular-current moment even when the native update creates \(W\ne0\). Moreover, the actual two-port map \(KC\) loses a direction that \(TC\) retains. Geometry supplies the correct three normal directions, but the retained dynamics instantiates only one circle and does not assign its mean, or three means, from \(C\).

The exact receiver distinction is especially simple. On the loop axis, a steady constant preload gives \(U=0\) and \(V_{\rm ext}=0\), hence zero in every published observation frame. Its curl is nonzero. A receiver of the curl would distinguish that preload from an empty carrier; the existing center-sampled C6 receiver does not distinguish them on the axis. No equation in the inspected chain feeds this curl into a second native triad.

## 1. Premises and notation

The source files are copied unchanged from commit `ca22652dc000ca2b16419c1af4167918eab1ae94` and agree with the accepted atlas identities. [SOURCE_VERIFICATION.json](SOURCE_VERIFICATION.json) records original paths, Git blobs, hashes and copied filenames; [PRIMARY_LOCATORS.json](PRIMARY_LOCATORS.json) records exact label lines. The installed manual is a navigation authority that predates GM01–GM03. The underlying accepted investigations, rather than their manuscript's publication wording, supply the newer premises.

Paper G defines, in fixed channel labels,

\[
C=\Re\Omega\times\Im\Omega,\qquad W=TC,\qquad
T=\begin{pmatrix}-1/2&1&-1/2\\-\sqrt3/2&0&\sqrt3/2\\0&0&0\end{pmatrix},
\quad\ker T=\mathbb R(1,1,1)^T. \tag{1}
\]

Sources: [G](sources/G_paper_g.tex), `eq:SA`, `eq:T`, `eq:W`, `prop:attach`. \(C\) is a channel-space area vector; \(W\) is its specified ambient axial attachment. Neither is assigned SI units by that theorem.

Write the selected oriented circle in a right-handed orthonormal frame \((e_1,e_2,\nu)\):

\[
\gamma(\chi)=Y+\rho(\chi),\quad
\rho=a(\cos\chi\,e_1+\sin\chi\,e_2),\quad
\widehat t=-\sin\chi\,e_1+\cos\chi\,e_2,
\quad \nu=e_1\times e_2,\quad ds=a\,d\chi. \tag{2}
\]

Here \(a\) is the **circle radius**, \(Y\) its actual center, and \(r=|X-Y|\) an observation distance. In the published PLUS circle \(e_1=u=(0,1,0)\), \(e_2=e_z\), and \(\nu=e_x\). For common host width \(w\),

\[
Y=O+wK_cu,\quad a=wR_\Gamma,\quad
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\quad
R_\Gamma=\frac{\sqrt7}{2}\frac{K_c}{1+\sqrt3/2}. \tag{3}
\]

In particular, \(Y\ne O\). The source's contact-height symbol \(a_c=K_c/(1+\sqrt3/2)\) is different from this report's radius \(a\). Sources: [PAIR geometry](sources/PAIR_geometry.tex), `eq:axes`, `eq:circle`, `thm:circle`; [WT setting](sources/WT_02_setting.tex), `eq:circleconstants`, `eq:circle`.

C1 and C6 are already **adopted comparison equations**, not consequences of native \(F\):

\[
p_t+c(r_c)_s=g_c,\qquad (r_c)_t+cp_s=0,\qquad s\in\mathbb R/L\mathbb Z,\quad L=2\pi a, \tag{4}
\]
\[
\begin{split}
U(X,t)&=a_o\int\frac{p(s,t-d_X(s)/c_e)}{d_X(s)}\,ds,\\
V_{\rm ext}(X,t)&=a_o\int\frac{r_c(s,t-d_X(s)/c_e)\widehat t(s)}{d_X(s)}\,ds,\\
Y_X&=(U,B^TV_{\rm ext}),\qquad
a_o=\frac{g_o}{4\pi},\quad d_X(s)=|X-\gamma(s)|.
\end{split}\tag{5}
\]

Here \(g_o,c,c_e>0\), \(B\) is a known orthonormal frame, and \(X\notin\Gamma\). C6 specifies the tangent encoding, \(1/d\) kernel and straight delay. These are material assumptions of the comparison. Its \(r_c\widehat t\) is not the scalar energy flux \(cpr_c\) and is not an assigned material electric current. Sources: [INT carrier](sources/INT_carrier.tex), `eq:C1`, `eq:C6`; [PAIR II exterior](sources/PAIRII_exterior.tex), `eq:C6`, `thm:history`.

## 2. Exact finite-radius field of a constant preload

Take \(g_c=0,p=0,r_c=j_0\ne0\), with the same constant history throughout every required delay window. This is an exact time-independent C1 solution. The resulting mathematical quantities are

\[
V(X)=a_oj_0\oint_\Gamma\frac{d\gamma}{|X-\gamma|},\qquad
H(X)=\nabla_X\times V(X)
=a_oj_0\oint_\Gamma
\frac{d\gamma\times(X-\gamma)}{|X-\gamma|^3}. \tag{6}
\]

For any compact set disjoint from the circle the kernel and all needed derivatives are uniformly bounded. Differentiation under this finite integral is legitimate. The sign follows from

\[
\nabla_X(d^{-1})\times d\gamma
=-\frac{X-\gamma}{d^3}\times d\gamma
=\frac{d\gamma\times(X-\gamma)}{d^3}.
\]

At \(X=Y+z\nu\), \(d=\sqrt{a^2+z^2}\) is constant, and the integral of \(d\gamma\) is zero. On the other hand,

\[
d\gamma\times(z\nu-\rho)
=a^2\nu\,d\chi+az(\cos\chi\,e_1+\sin\chi\,e_2)\,d\chi.
\]

The second term integrates to zero. Therefore, for **every real \(z\)**,

\[
\boxed{V(Y+z\nu)=0,\qquad
H(Y+z\nu)=\frac{g_oj_0a^2}{2(a^2+z^2)^{3/2}}\nu.} \tag{7}
\]

This includes \(z=0\), which is off the wire. It is even in \(z\), changes sign with \(j_0\), and agrees with increasing-\(\chi\) orientation. Differentiating the zero vector **after** restricting to the axis would incorrectly discard the transverse derivatives. Equation (6) differentiates first.

For this preload the carrier storage is \(Lj_0^2/2\), while its signed energy flux \(cpr_c\) is zero. The nonzero tangent-encoded circulation is thus not a demonstrated circulating energy throughput or material current.

## 3. The full angular law and a uniform remainder

Put \(X=Y+rn\), \(n\in S^2\), and

\[
m_\Gamma=\frac{j_0}{2}\oint\rho\times d\rho
=j_0\pi a^2\nu. \tag{8}
\]

Expanding the vector kernel gives the first nonzero vector observation

\[
V(Y+rn)=\frac{g_o}{4\pi r^2}(m_\Gamma\times n)
+O(g_o|j_0|a^4/r^4). \tag{9}
\]

Indeed the constant term integrates to zero, and
\(\oint(n\cdot\rho)d\rho=\pi a^2\nu\times n\).
The quadratic Taylor term vanishes by the half-turn \(\rho\mapsto-\rho,d\rho\mapsto-d\rho\). The remainder is uniform in direction on \(r\ge2a\). A separate differentiated estimate below, rather than an unjustified derivative of a big-O symbol, establishes the curl error.

Let \(D_a\) be the filled disk in the circle plane, used **only as an integration device**. Stokes' theorem componentwise gives, for \(r>a\),

\[
\Phi(R)=\int_{D_a}\frac{dA_\rho}{|R-\rho|},\quad
V=a_oj_0\nabla_R\Phi\times\nu,\quad
H=a_oj_0\int_{D_a}\operatorname{Hess}_R(|R-\rho|^{-1})\nu\,dA_\rho. \tag{10}
\]

Here \(\Delta_R\Phi=0\), since \(R=rn\) is outside the disk. This use of a disk neither fills a physical opening nor changes the carrier. The Hessian at its center is

\[
\operatorname{Hess}(|R|^{-1})=\frac{3nn^T-I_3}{r^3}. \tag{11}
\]

The linear Taylor term in \(\rho\) integrates to zero. The following bound controls the second-order remainder of that Hessian:

\[
\|D_w^2\operatorname{Hess}(|x|^{-1})\|_{\rm op}
\le \frac{24|w|^2}{|x|^5},\qquad x\ne0. \tag{12}
\]

For completeness, rotate \(x/|x|\) to \(e_3\) and a unit \(w\) into the \(e_1,e_3\) plane, with \(w=(\sqrt{1-q},0,\sqrt q)\) up to a sign and \(0\le q\le1\). The matrix multiplied by \(|x|^5\) has an independent eigenvalue \(3-15q\in[-12,3]\) and the block

\[
M(q)=\begin{pmatrix}9-21q&-24\sqrt{q(1-q)}\\-24\sqrt{q(1-q)}&36q-12\end{pmatrix}. \tag{13}
\]

The diagonal entries of \(24I-M\) are \(15+21q,36(1-q)\ge0\), and its determinant is \(180(1-q)(3+q)\ge0\). The diagonal entries of \(24I+M\) are \(33-21q\ge12,12+36q\ge12\), and its determinant is \(396+180q(2-q)\ge396\). Both are positive semidefinite, proving (12). Changing the sign of the off-diagonal entry does not change the conclusion.

Since \(|R-t\rho|\ge r-a\) for \(0\le t\le1\), Taylor's integral remainder and \(\int_{D_a}|\rho|^2dA=\pi a^4/2\) yield

\[
\boxed{H(Y+rn)=\frac{g_o}{4\pi r^3}
\{3n(n\cdot m_\Gamma)-m_\Gamma\}+\mathcal R(R),}\tag{14}
\]
\[
\boxed{\|\mathcal R(R)\|\le
\frac{3g_o|j_0|a^4}{2(r-a)^5}\quad(r>a),\qquad
\|\mathcal R(R)\|\le\frac{48g_o|j_0|a^4}{r^5}\quad(r\ge2a).} \tag{15}
\]

The bound is conservative; it is not a relative-error assertion of smallness at \(r=2a\). It proves an \(O(r^{-5})\) error uniformly over **all** directions, with a nonzero dipole leading coefficient for every direction when \(j_0\ne0\). No \(r^{-4}\) curl term survives the centered disk symmetry.

The angular factor for \(m_\Gamma=m\nu\) is:

| Direction | Leading \(H\), divided by \(g_om/(4\pi r^3)\) |
|---|---|
| \(n=\pm\nu\) | \(2\nu\) |
| \(n\perp\nu\) | \(-\nu\) |
| \(n=(e_1+\nu)/\sqrt2\) | \(3e_1/2+\nu/2\) |
| General \(n\) | \(3n(n\cdot\nu)-\nu\) |

Reversing \(j_0\) reverses the exact field and all leading components. At fixed direction, \(H(Y+2rn)=H(Y+rn)/8+O(g_o|j_0|a^4/r^5)\), and the norm ratio tends to \(1/8\). This is asymptotic, not an exact finite-radius ratio. The exact axial magnitude ratio is \([(a^2+r^2)/(a^2+4r^2)]^{3/2}\).

The angular tensor and inverse-cube term agree with the magnetic-dipole comparison in [Tong, *Electromagnetism*, §3.3, equations \(3.19\)–\(3.24\)](https://www.damtp.cam.ac.uk/user/tong/em/em2.pdf). The identification of \(H\) as a measured magnetic field and of \(g_o\) with an SI prefactor are additional calibration choices. In inherited units \([V]=\mathrm U,[H]=\mathrm U/\mathrm L,[m_\Gamma]=\mathrm U\mathrm L^2\).

GM02 equations (13)–(14) instead obtain **exact** external dipole interactions for disjoint smooth radial magnetization profiles. A line circle is not such a profile. Its finite-radius correction in (7) and (15) cannot be discarded by invoking GM02's radial averaging theorem.

## 4. What the native drive can put into the circle

### 4.1 An invariant and an independent preload

Define the mean circulation and its associated circular-current moment by

\[
\mathcal I_c(t)=\int_0^Lr_c(s,t)\,ds,\qquad
m_c(t)=\frac12\int_0^L(\gamma-Y)\times(r_c\widehat t)\,ds.
\]

The circle identity \(\rho\times\widehat t=a\nu\) proves, without assuming spatial uniformity,

\[
\boxed{m_c(t)=\frac a2\nu\,\mathcal I_c(t).} \tag{16}
\]

For C1, and for RX `eq:system`,

\[
\frac{d\mathcal I_c}{dt}=-c\int_0^Lp_s\,ds=0. \tag{17}
\]

This holds for the stated periodic \(H^1\) solutions. For \(L^2\) mild solutions it follows by testing against the constant function, or by integrating the translation formula: the forcing enters the two characteristics equally and cancels in their difference. The mean is a bounded linear functional on \(L^2(S_L)\), so the result extends by continuity. Native forcing, the old receiver term and the nonlinear reciprocal feedback change the \(p\) equation but not this mean identity.

In the native-first RX hybrid, the jump changes only \(x=(\Re\Omega,\Im\Omega)\); \(p,r_c,z\) are unchanged. Thus (17) also survives every jump. An initially empty carrier has \(\mathcal I_c=m_c=0\) forever under this hybrid. This does **not** assert that its whole carrier state, exterior output or transported energy stays zero.

There is a stronger freedom. If \((x,p,r_c,z)\) is an RX solution, then \((x,p,r_c+j_0,z)\) is another with the same native history and old receiver history. Only the constant mean and associated carrier storage change. The spatial derivative of the offset is zero, and all native/old receiver feedback uses \(p\). The same statement holds across native jumps. With the offset also in the required C6 prehistory, the two exterior observations differ exactly by (6). Consequently even a complete \(W(t)\) history does not select this loop moment from the retained equations and unspecified carrier preparation.

### 4.2 The exact Fourier witness

At the inherited NPC/RX tuple
\(\epsilon=1/10,g=1/60,\lambda=1/300,k=(999/1000,1,1001/1000)\), take

\[
\Omega=(1,\omega,\omega^2),\quad\omega=e^{-2\pi i/3}.
\]

All prestage factors are positive, the Fourier phases remain fixed, and the three-harmonic phase kicks are exactly zero. Direct computation gives

\[
F_i(\Omega)=\frac{(9499,9500,9501)_i}{10000}\Omega_i,
\quad W=0,\quad
W^+=\left(\frac{\sqrt3}{200000000},\frac{57}{400000},0\right)\ne0. \tag{18}
\]

This is GM02 (9)–(10), independently reproduced here. The native jump changes \(C,W,I\), not the carrier. Subsequent RX exchange can redistribute carrier modes and change the native state, but preserves (16)–(17). Empty versus constant-preloaded circles therefore retain different moments at the same native preparation. Also, \(W=0\) initially does not imply \(f=0\): the Fourier entrance has \(C=-(\sqrt3/2)(1,1,1)^T\), generally visible to \(K\) even though it is in \(\ker T\).

### 4.3 Zero mean does not mean zero exterior signal

For a fixed instantaneous profile define
\(J_0=\int r_c(s)\widehat t(s)\,ds\). The simultaneous spatial kernel has leading term

\[
V(Y+rn)=\frac{g_o}{4\pi r}J_0+O(r^{-2}),\qquad
\nabla\times V(Y+rn)=\frac{g_o}{4\pi r^2}(J_0\times n)+O(r^{-3}). \tag{19}
\]

This is a frozen-profile spatial calculation, not an approximation that silently removes the delays from arbitrary evolving C6 data. For example \(r_c=A\cos\chi\) has zero mean but \(J_0=A\pi a e_2\ne0\). Even \(J_0=0\) alone does not turn an arbitrary nonuniform profile into a divergence-free steady line current: symmetric first-moment contributions may remain. For source-off **stationary** C1, (4) requires both \(p_s=0\) and \((r_c)_s=0\), so the constant case above has the needed special structure.

An exact time-dependent C1 example makes the observation distinction without freezing a nonstationary solution:

\[
r_c=A\cos\chi\cos(ct/a),\quad p=A\sin\chi\sin(ct/a). \tag{20}
\]

It has zero mean for all time. On the axis all delays equal \(d/c_e\), so its **actual retarded C6** record is

\[
U=0,\qquad V(Y+z\nu,t)=\frac{g_oAa}{4\sqrt{a^2+z^2}}
\cos\left[\frac ca\left(t-\frac{\sqrt{a^2+z^2}}{c_e}\right)\right]e_2. \tag{21}
\]

This can be nonzero despite \(m_c=0\). It is a prepared free wave with a supplied history, not an empty launch or a generated static magnetic dipole.

### 4.4 The actual source interface loses part of \(W\)

RX uses

\[
f=KC,\qquad K=\kappa_{\rm in}\lambda_g
\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}R_z(\delta_g),\qquad
n_\pm=\frac{2e_y\pm\sqrt3e_z}{\sqrt7}. \tag{22}
\]

The gains are positive and fixed. In channel coordinates let

\[
v=R_z(-\delta_g)e_x=(\cos\delta_g,-\sin\delta_g,0)^T.
\]

Then

\[
Kv=0,\quad
Tv=\left(-\tfrac12\cos\delta_g-\sin\delta_g,
-\tfrac{\sqrt3}{2}\cos\delta_g,0\right),\quad
|Tv|^2=1+\tfrac12\sin2\delta_g\ge\tfrac12. \tag{23}
\]

Choose real channel vectors \(x=e_3,y=v\times e_3\), and states \(\Omega_\pm=x\pm iy\). Both have intensity 2, with \(C_\pm=\pm v\), \(f_\pm^{\rm state}=0\), and opposite nonzero \(W=\pm Tv\). The superscript here distinguishes the two **states** from the upper/lower port subscripts.

Thus \(W\) is not a function of these two port values: such a function would have to assign opposite answers to the same input. With native state clamped, equal complete port histories and equal carrier/prehistory give equal downstream observations. In the exchange-only RX or WT model these two states and an entirely empty carrier/receiver/transport preparation remain stationary: all drives and responses are zero, so uniqueness gives the zero external solution despite nonzero opposite \(W\). Ordinary later native jumps can change the drives. No equality of later histories is inferred from an instantaneous equality.

## 5. The loaded WT mean and its receiving subspace

WT is an added storage-bearing extension on \(\Lambda=S_L\times G\), with \(G\) the six specified labeled broken arcs and measure \(ds\,d\ell_X\). Its propagation coordinate \(0<\xi<\theta_X(s)=d_X(s)/c_e\) is time/age. It is neither an ambient field PDE nor a coupling to a second autonomous triad. The receiving state is \(\zeta\in L^2(G;\mathbb R^4)\); the old \(z\in\mathbb R^2\) still has no assigned material position.

Let \(M=\int_Gd\ell_X\), and write \(b_r\) for the second component of WT's near incoming wave \(b=u_-(0)\). The complete `eq:closedmodel`, including its feedback, gives

\[
(r_c)_t=-cp_s-\kappa^2r_c+
\frac{\sqrt2\kappa}{\sqrt M}\int_G b_r(s,X,t)\,d\ell_X,
\]
\[
\boxed{\dot{\mathcal I}_c=-\kappa^2\mathcal I_c+
\frac{\sqrt2\kappa}{\sqrt M}\int_{S_L\times G}b_r(s,X,t)\,ds\,d\ell_X.} \tag{24}
\]

The integrated version is valid for finite-energy mild solutions, by the bounded mean functional and locally \(L^2\) incoming traces. At \(\kappa=0\) it reduces to (17). At \(\kappa>0\) it is **not** a conservation law. For example admissible nonzero initial backward profiles with constant second component \(b_0\) give \(b_r=b_0\) for \(0<t<\theta_-\). From mean zero their initial mean derivative is \(\sqrt2\kappa L\sqrt M b_0\ne0\). This example uses an independent finite-energy preload; it does not misdescribe an empty startup.

For the fully empty startup \(Q_0=z_0=u_{+,0}=u_{-,0}=\zeta_0=0\), with a native state allowed to drive the \(p\) ports, the WT characteristic formulas instead imply:

1. \(b=0\) before \(\theta_-\), because the backward initial profile is zero.
2. \(c=0\) and \(\zeta=0\) before \(\theta_-\). Hence the far inflow \(d=\sqrt2C^*\zeta-c\) is also zero then.
3. Consequently \(b=0\) before **\(2\theta_-\)**, and (24) keeps the initially zero mean zero throughout that interval, including any native jumps, which leave Q unchanged.

Here \(\theta_->0\) is WT's minimum over its actual compact circle-and-arc domain, not an arbitrary exterior probe delay. Equal-time endpoints are interpreted almost everywhere in its energy-space formulation.

After startup, the exact incoming term is

\[
b_r(s,X,t)=\mathbf1_{t\ge\theta_X(s)}
\left[\frac{\sqrt2a_o\sqrt M}{d_X(s)}
\widehat t(s)\cdot\zeta_v(X,t-\theta_X(s))
-c_r(s,X,t-\theta_X(s))\right]. \tag{25}
\]

Return of the generated vector sector and its receiver load can therefore enter the mean balance. This is not a direct native source term, nor a theorem that every empty launch develops a nonzero mean. Delayed, spatially weighted returns cannot in general be replaced by the simultaneous mean of \(r_c\). Independent nonempty backward profiles add their own startup source; nonzero \(\zeta_0\) can produce return after a one-way delay. Equation (24), with these actual histories, is the determination supplied by WT. There is no algebraic closure \(\mathcal I_c=\text{constant}\times W\) and no immediate generation of (8) from (18).

WT's receiver reads the same tangent vector sector, not its spatial curl. Its spatial map has

\[
(Cv)(X)=a_o\sqrt M\int\frac{(v_p,\widehat t\,v_r)(s,X)}{d_X(s)}\,ds,
\qquad(C^*\zeta)_r=\frac{a_o\sqrt M}{d_X(s)}\widehat t\cdot\zeta_v(X). \tag{26}
\]

Since \(\widehat t\cdot\nu=0\), all vector outputs of C lie in the carrier plane, and \((0,h(X)\nu)\in\ker C^*\). The evolution \(\beta_G\dot\zeta=\sqrt2Cc-CC^*\zeta\) preserves the normal component of \(\zeta_v\); if it starts zero, it remains zero. This is an exact subspace obstruction, not merely a rank count. The candidate axial \(H\) in (7) points precisely in that rejected direction. This compares vector components: the C6 axis test does not assert that its observation point lies on G. WT does have a genuine delayed, loaded receiving law on its own six arcs; it does not thereby read H at an arbitrary second triad or establish magnetic force.

Sources: [WT transport](sources/WT_05_transport.tex), `eq:J`, `eq:Cspatial`, `eq:Gram`, `eq:transportPDE`, `eq:bstartup`, `eq:closedmodel`; [WT preparation](sources/WT_07_preparation.tex), `eq:loadedC6`, `eq:historycompatibility`, native-jump paragraph. The same-time spatial \(C^*\) here is not the noncausal finite-window temporal adjoint in WT `eq:temporaladjoint`.

## 6. Geometric match and the missing three-circle source law

The published PLUS axes are \(u_j=R_z(2\pi j/3)e_y\), and (2) gives \(\nu_j=u_j\times e_z\). Therefore

\[
\nu_0=(1,0,0),\quad\nu_1=(-1/2,\sqrt3/2,0),\quad
\nu_2=(-1/2,-\sqrt3/2,0),\qquad
\boxed{[\nu_2\ \nu_0\ \nu_1]=T.} \tag{27}
\]

The label order is \(A\leftrightarrow2,B\leftrightarrow0,C\leftrightarrow1\). Circle normals are not the contact normals \(n_j^\pm\), and the contact tangent signs \(-n_j^+,+n_j^-\) do not modify the source projection (22).

For the source's full MINUS reflection \(S=\operatorname{diag}(-1,1,1)\) with labels and parameter direction retained,

\[
\gamma'_j=S\gamma_j,\quad \widehat t'_j=S\widehat t_j,\quad
\nu'_j=\det(S)S\nu_j=-S\nu_j. \tag{28}
\]

Thus the reflected ordered normal matrix is \(-ST\), not \(ST\). If the mirrored construction is expressed back in Paper G's fixed symmetry labels, the vertical mirror swaps A and C: \(TQ_{AC}=-ST\). This agrees with Paper G's `eq:Ccov` and axial law. Transforming the geometry with retained labels and actively relabeling a state in the original geometry are two descriptions; applying both changes twice would be an error. For the separate horizontal mirror \(H_s=\operatorname{diag}(1,1,-1)\), transported normals are \(-H_s\nu_j=-\nu_j\). An arclength-coordinate reversal is different again: reversing both \(r_c\) and \(\widehat t\) leaves the physical tangent-encoded vector unchanged.

The geometry describes three possible circles with centers \(Y_j=O+wK_cu_j\). PAIR II, INT, RX and WT explicitly retain **one** dynamical circle, \(\Gamma_0\). Neither the three geometric options, six normal readings, nor the exterior module count instantiate three independent carrier states or source equations.

As the requested diagnostic, suppose three equal-radius loops were separately instantiated with constant weights \(j=(j_A,j_B,j_C)^T\) in order \(2,0,1\). Their leading total moment would be

\[
m_{\rm tot}=\pi a^2Tj,\qquad
m_{\rm tot}=\pi a^2\lambda TC
\iff j-\lambda C\in\ker T=\mathbb R(1,1,1)^T. \tag{29}
\]

Here \(\lambda\) includes the new units and registration, not a native phase-kick parameter. No inspected evolution supplies (29). One selected circle has only the fixed direction \(\nu_0\), which also cannot span general planar \(W\).

Even under the hypothetical relation, the finite-distance field is the sum of three loop integrals with **distinct** centers. A common-center far-field approximation requires distance large compared with their radii and offsets from the chosen common reference. Translation can produce terms beyond the aggregate dipole term. The freedom \(j\mapsto j+\beta(1,1,1)\) leaves (29) unchanged but need not leave the exact spatial field unchanged: near each disjoint loop its nonzero local line contribution cannot be canceled by smooth fields from the other loops. Matching a leading moment does not determine all finite-distance data.

## 7. What a second triad can actually read

The inherited complete module placements are

\[
X_{mk}=O+\rho_m e_r(\phi_k)+h_m e_z,\quad
B_k=[e_r(\phi_k),e_z,-e_\phi(\phi_k)],\quad
\phi_k=\pi/2+k\pi/6. \tag{30}
\]

They place full geometric copies; C6 samples their centers. Its law also permits any specified off-circle point and orthonormal frame. The axis diagnostic is allowed by that general domain even though it need not be one of the retained H/R fixture sites. Neither the arbitrary second body's native state nor its susceptibility appears in C6.

For the constant preload the signed response at a specified point and complete frame is **determined**:

\[
Y_{X,B}=\left(0,\ a_oj_0B^T\oint\frac{d\gamma}{|X-\gamma|}\right),\qquad
Y_{Y+rn,B}=\left(0,\frac{g_o}{4\pi r^2}B^T(m_\Gamma\times n)+O(r^{-4})\right). \tag{31}
\]

A complete known B is invertible: it retains the vector V. A single calibrated axis \(\ell\) retains only \(\ell\cdot V\); it distinguishes two states exactly when this projection differs. Scalar-only U distinguishes none of these constant \(p=0\) preloads. On the loop axis even the complete record is zero for every \(j_0\). Off-axis, appropriately oriented signed components can distinguish reversal; squared norms alone lose that sign. Observation of this **vector-potential-shaped** record is a valid existing comparison result, not a readout of H or an update of a receiving native state.

A stronger informational map is already defined in PAIR I: its uniform comparator is \(y_k^C=B_k^TA_{\rm reg}C\). With complete frame and invertible registration it reconstructs C and hence \(TC\), including the null direction of K. But distances and scales do not enter that rule. It simply reports registered native data at every frame, with no \(1/r^3\) field law, propagation or feedback. It cannot be substituted for the missing spatial source-to-probe mechanism. Sources: [PAIR observation](sources/PAIR_observation.tex), `eq:uniform`, `thm:reconstruct`, explicit distance-independence paragraph.

GM01's proposed magnetization dictionary plus its imposed magnetostatic field law does supply a separate field. GM02 (15) supplies the field of the other radial body and uses it in the proposed energy feedback. Those are already-declared extensions, not a derivation of this carrier law from native F. Their success is compatible with the source and receiver obstructions above.

### Time-dependent differentiation and startup

For a smooth supplied C6 history, differentiating its retarded vector observation gives

\[
\nabla_X\times V(X,t)=a_o\int\left[
\frac{r_c(s,t-d/c_e)}{d^3}
+\frac{\partial_t r_c(s,t-d/c_e)}{c_ed^2}\right]
\widehat t(s)\times(X-\gamma(s))\,ds. \tag{32}
\]

Sufficient hypotheses are a fixed off-circle spatial neighborhood with positive clearance and time-\(C^1\) histories whose values and time derivatives have an integrable dominating bound in s over the needed delay windows. Smooth periodic histories on a compact window suffice. The published \(L^2\) history theorem alone does not supply this pointwise derivative. Jumps can instead require distributional terms; a step-switched constant circulation is not a free C1 solution.

If a generated history is identically zero before a specified start, C6 changes cannot be observed before the minimum straight delay for that probe. This is an adopted mathematical causal delay, with independent \(c_e\), rather than a recovered native physical clock or electromagnetic propagation law. The steady preload used for (6) has no first arrival. No dynamic magnetic transmission or second-triad backreaction claim is made from the static calculation.

## 8. Smallest missing choices and the completed scope

| Link | Supplied by | Result or missing choice |
|---|---|---|
| \(\Omega\mapsto C\mapsto W\) | Native definitions and Paper G attachment | Exact; (18) shows native generation of nonzero W. |
| \(C\mapsto KC\) | Adopted registration and two ports | Exact but not sufficient to recover W; (23). |
| Native forcing to mean circular moment | C1/RX | Mean invariant; empty carrier cannot gain (16). |
| Loaded change in that mean | Added WT transport | Only damping and actual incoming vector waves in (24); startup and preparation matter. |
| Constant loop preload to V | Adopted C6 | Exact integral, signed frame response (31), zero on the axis. |
| V to dipole-pattern H | Spatial differentiation | Exact curl (6), angular law and bound (14)–(15); not the published receiver output. |
| Geometric normals to T | Existing three-circle geometry | Exact ordered identity (27); no independently sourced three-circle dynamics. |
| H to a second triad's response | No such equation in this chain | Need a specified derivative-sensitive observable and, for state response, an actual input law. |

To distinguish the alternatives at the **source**, one must add a rule for the otherwise free carrier mean and ensure the source retains the part of C needed for W. Appending one calibrated scalar \(v^TC\) to K's two independent components would remove the demonstrated input ambiguity; changing the two-component source to one with kernel \(\ker T\) is another possibility. Neither by itself generates circulation. A mean-source or jump rule must then explicitly change \(\int r_cds\); for a proposed uniform weight \(j(t)\), an added right-hand side \(S_r\) in the second C1 equation would have to satisfy \(\int S_rds=L\dot j\), and an assigned jump would need \(\Delta\int r_cds=L\Delta j\). Three loops would additionally need their independent state laws, registration and a relation such as (29), including any common-weight freedom relevant to finite-distance fields.

At the **probe**, a declared measurement of \(\nabla\times V\), or a calibrated local spatial stencil implementing it under sufficient regularity, would distinguish the two axis preparations. A single center value of V cannot. Feeding that measurement into a second triad then requires its own coupling, units, preparation, and—if motion or force is claimed—motion and energy laws. These are identified choices, not adopted modifications or unperformed parts of this bounded check.

The static field-pattern question is complete conditionally: a **preloaded tangent-encoded constant loop**, rather than an automatically generated native W, produces the dipole curl. Existing probes read V or its projections; WT adds a specified tangent-sector receiver on G, but neither reads the missing curl nor implements a second native magnetic response. The precise source and readout gaps have been established. A paper, publication, broader field model and author-level coupling selection remain subsequent decisions.

## 9. Verification and review materials

[checks.py](checks.py) contains independent exact symbolic identities and numerical quadrature diagnostics, run in Windows Command Prompt after `conda activate torment`. [CHECK_RESULTS.json](CHECK_RESULTS.json) distinguishes their types and stores the vector samples. The written Stokes, differentiated-kernel, periodic-mean, mild-solution and input-kernel arguments above establish the continuum conclusions; a numerical sample or check count does not replace those proofs.

[SOURCE_TO_PROBE_MAP.md](SOURCE_TO_PROBE_MAP.md) gives the equation-level route. [CLAIM_LEDGER.json](CLAIM_LEDGER.json) separates inherited definitions, deductions and hypothetical additional choices. Original GM01–GM03 manifests and the accepted reference were checked without replaying their scientific suites. No accepted files, native implementation, production TORMENT, earlier paper, Git commit or remote branch is changed by GM04. This local package is returned for review.
