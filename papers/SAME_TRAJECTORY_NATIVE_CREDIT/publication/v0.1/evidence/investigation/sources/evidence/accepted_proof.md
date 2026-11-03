# Native reciprocal exchange — independent proof review

**Investigation:** NATIVE_RECIPROCAL_EXCHANGE_01  
**Date:** 3 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson / pzychozen  
**Candidate formulation and direction:** GPT  
**Independent challenge, proofs and preparation:** Codex  
**Disposition:** Local candidate investigation for GPT/author review. No adoption, implementation, manuscript, PDF, Git operation or publication.

## Verdict

**The specified candidate is mathematically coherent at the scope proved here.** Its exchange stage is a globally defined, unique nonlinear flow on the stated energy space, with continuous dependence, positive conserved total trial storage, and preservation of periodic H1 carrier regularity. No correction to the candidate's signs, factors of two, or equations T1–T7 is needed. The short-time claims have the stated asymptotic meaning; the coherent-domain and physical interpretations need the limitations below.

What this candidate supplies that the old model did not is **a changing native state with an exactly matched debit/credit for carrier work, together with a dynamic two-port receiving state whose storage change has an equal and opposite loading term in the carrier equation**. This is an actual feedback system, not a reservoir defined from a residual.

| Target | Verdict and proved scope |
|---|---|
| A: reciprocal mechanism and solutions | Pass for the proposed mathematical exchange system. The complete local and global balances hold; the coupled nonlinear problem is globally well posed in energy space. H1 preparation gives strong solutions and point-cut meaning. |
| B: actual activity and limits | Nonzero native supply and receiver gain occur for sufficiently short positive time from an empty carrier/receiver with a permitted coherent chiral core. Separately prepared negative-power data give genuine native credit. Receiver work can reverse. Neither argument proves a delayed return of a previously launched cohort on the same orbit. |
| C: native map and hybrid step | The exact native map is retained as the first substep. Exchange conserves the enlarged storage, but each full step changes it by the native intensity increment. At both couplings zero the sampled native state follows exactly F. Every finite ideal step exists; inherited coherent-domain invariance does not survive arbitrary coupled preparations. |

There are substantial limitations. Exchange preserves the complex bilinear invariant Z2, which bounds **net** extractable native storage and makes an aligned core with empty carrier/receiver dark. An explicit phase-boundary witness leaves the old coherent domain. A separate analytic preparation argument also refutes universal invariance of the sampled hybrid map over the allowed symbolic cadences. The receiver is a reversible store, not permanent disposal. Trial storage scales, continuous feedback, loading, cadence and any physical interpretation remain modeling choices. A physical central circulation, a six-opening allocation, and a 15–20% diversion have not been established.

The separate historical GPT analytical review and accompanying packet manifest were not available in the named local locations. The accepted proof and archive match their supplied byte identities; the complete defining publications and native definitions were available and reconciled. The current order and accepted published interpretation supply the point-versus-region qualification. No claim is made to have inspected the missing review. Detailed identities and proof dependencies are in SOURCE_IDENTITIES.json and CLAIM_SOURCE_LEDGER.md.

## S. Inherited definitions and new assumptions

### S1. Register

| Item | Status and role |
|---|---|
| Exact complex triad F, simultaneous prestage kicks, harmonic-three synchronization, Arg0 convention, fixed tuple, intensity identity | Inherited project definitions/results. Read as mathematical text; no project module imported. |
| Raw channel chirality Cch = Re(Omega) cross Im(Omega), selected host-pair normals, yaw registration and positive conversion gain | Inherited source-to-drive algebra. Raw C is distinct from its ambient axial attachment. |
| C1 circle, orientation, normalized disjoint tents, finite-width propagation, HC and collocated averages | Inherited conditional carrier. These were already adoptions, not consequences of F or geometric imagery. |
| HN = alphaN I/2, alphaN > 0 | GPT-proposed constitutive storage postulate. Positive, convenient and related to the native intensity account; not physical energy derived from the native potential V. |
| One receiver z in R2, HR = betaR times the squared norm of z divided by 2, betaR > 0 | GPT-proposed receiving state and storage, internal to the enlarged mathematical account. The two coordinates do not introduce two spatial holes. |
| Native feedback, receiver loading, dimensionless etaN and etaR | GPT-proposed equations, independently tested here. They are not native coefficients or diversion fractions. |
| Continuously updated chiral drive during exchange | New protocol. Replaces the old externally supplied sample/hold history during this stage. |
| F first, then exact exchange for symbolic h_ex > 0 | New split and cadence, not a differential equation equivalent to F or a recovered physical clock. |
| Powers, existence, activity, invariant and bounds established below | Codex deductions from these definitions. They are conditional mathematics, not observations or accepted-kernel additions. |

Power-preserving interconnection and matched power products are established methodology: see A. van der Schaft, *Port-Hamiltonian nonlinear systems*, [arXiv:2412.19673v1, sections 1.1–1.2](https://arxiv.org/html/2412.19673v1), especially equations (5)–(6) and the interconnection discussion. This is context only. It does not select this storage, chiral completion or receiver, establish a canonical Hamiltonian/Poisson structure, or prove this PDE's well-posedness. The balances and solution argument below are direct.

### S2. Exact candidate and orientation

Write x = (a,b) in R6, Omega = a + ib, I = |a|² + |b|² and Cch = a cross b. The symbol b here is the imaginary native vector; b_sigma denotes a carrier profile and d_pre denotes the native prestage increment.

Use u = (0,1,0), e_z = (0,0,1), and the inherited normals and registration

\[
n_\pm=(2u\pm\sqrt3e_z)/\sqrt7,\qquad
A_{\rm reg}=\lambda_g R_z(\delta_g),\qquad
K=\kappa_{\rm in}\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}A_{\rm reg},
\]
\[
f(x)=f_{\rm ch}(x)=K(a\times b),\qquad J(x)=D_xf(x).
\tag{S1}
\]

K is 2 by 3; J is 2 by 6. Both gains are positive and fixed; yaw is fixed and symbolic. K has rank two. In the inherited circle orientation the contact tangents are -n_plus and +n_minus; the source explicitly says these tangent signs do **not** insert extra signs into the readout-to-source law. Thus S1 preserves the plus/minus port ordering and source projections. The selected patches are N1+ and N1−, not all six central broken arcs.

For s modulo Lc, let 0 < epsilon_c < eta_geom and

\[
b_\sigma(s)=\epsilon_c^{-1}
\left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
\quad \mathcal Bv=b_+v_++b_-v_-,\quad
y=\mathcal B^*p=\binom{\int b_+p\,ds}{\int b_-p\,ds}.
\tag{S2}
\]

The shortest contact separation is 2 eta_geom, so the supports are disjoint. All spatial integrals below are over one whole circle unless a region is specified. Define

\[
H_N=\frac{\alpha_N}{2}|x|^2,\quad
H_C=\frac12\int(p^2+r_c^2)\,ds,\quad
H_R=\frac{\beta_R}{2}|z|^2,\quad H_{\rm tot}=H_N+H_C+H_R.
\tag{S3}
\]

For c, alphaN, betaR > 0 and etaN, etaR >= 0, the proposed exchange equations are retained exactly:

\[
\begin{aligned}
\dot x&=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\\
p_t+c(r_c)_s&=\mathcal B\{\eta_N f(x)-\eta_R z\},\\
(r_c)_t+cp_s&=0,\\
\dot z&=\frac{\eta_R}{\beta_R}y,\qquad y=\mathcal B^*p.
\end{aligned}
\tag{S4}
\]

Preparation (x0,p0,rc0,z0) is independently specified. The carrier is periodic. The receiver is inside the total account but has no selected material identity or spatial location. Its coupling uses the same distributed regions as native driving. This deliberate collocation is not transport to a separate aperture.

### S3. Dimensions

Let A denote the native amplitude unit, so [x] = A and [I] = A². This is a bookkeeping unit, not the registration matrix. The native implementation may use dimensionless amplitudes; setting A = 1 gives that convention. The inherited abstract carrier units are U, L, T.

| Quantity | Dimension |
|---|---|
| s, Lc, epsilon_c, eta_geom; c; t and h_ex | L; L/T; T |
| p, rc; b_sigma; y | U; L^(-1); U |
| Cch, f, z, J | A²; UL/T; UL/T; UL/(TA) |
| lambda_g, kappa_in, K | Q/A²; UL/(TQ); UL/(TA²), with inherited readout data unit Q |
| alphaN; betaR; etaN, etaR | U²L/A²; T²/L; dimensionless |
| HN, HC, HR; e; j and P_NC, P_CR | U²L; U²; U²L/T |
| Bv for a source-strength v; M_B = B*B | U/T; L^(-1) |

Consequently [J^T y/alphaN] = A/T, [y/betaR] = UL/T² = [zdot], and [B(etaN f − etaR z)] = U/T, matching both carrier time and propagation terms. The local identity has dimension U²/T; integration in s produces power U²L/T. Every Q below is U²L. No SI calibration, physical energy scale, or numerical gain/cadence is selected. The new alphaN and betaR supply mathematical commensurability; they do not derive it from V.

The native coefficients are given in the inherited normalized amplitude convention. If an amplitude unit A is restored purely for this dimensional check, [k_i] = A², [epsilon_native] = A^(-2), and native g and lambda are dimensionless, so d_pre has unit A. The fixed numerical tuple in C1 retains its original normalized meaning. Native step number has no time unit and is not divided by h_ex to create a differential equation.

## A. Reciprocal power and the closed solution problem

### A1. Jacobian, homogeneity and feedback signs

For [v]_cross h = v cross h, differentiation gives

\[
D C_{\rm ch}(a,b)[\delta a,\delta b]
=\delta a\times b+a\times\delta b,
\quad J=K\begin{bmatrix}-[b]_\times&[a]_\times\end{bmatrix},
\quad Jx=2f(x).
\tag{A1}
\]

Set w = K^T y and mu = etaN/(2 alphaN). Transposition yields

\[
J^Ty=\binom{b\times w}{w\times a},\qquad
\dot a=\mu w\times b,\quad \dot b=-\mu w\times a,
\quad \dot\Omega=-i\mu w\times\Omega.
\tag{A2}
\]

In particular x^T J^T y = 2 f^T y, not f^T y. This is precisely why the factor 1/2 in S4 is needed. All coefficients are polynomial in the finite-dimensional states and bounded linear in the carrier ports. There is no division by intensity, chirality, port output or state norm.

The completion is not uniquely forced by its power identity. Any additional sufficiently regular core term h(x,p,rc,z) satisfying x dot h = 0 would leave HNdot unchanged. Such a term could change the invariant or other dynamics. No such term is added, and no classification is claimed.

### A2. Local, global and integrated balances

Define signed powers

\[
P_{NC}=\eta_N f(x)^Ty,\qquad P_{CR}=\eta_R z^Ty.
\tag{A3}
\]

For strong solutions, A1 and S4 give HNdot = alphaN x dot xdot = −P_NC and HRdot = betaR z dot zdot = P_CR. With e = (p²+rc²)/2 and j = c p rc, the complete carrier equation gives

\[
\partial_t e+\partial_s j
=p\,\mathcal B(\eta_N f(x)-\eta_R z).
\tag{A4}
\]

The loading work must remain on the right side. Periodic integration cancels c integral(partial_s(p rc)) and adjointness gives

\[
\dot H_N=-P_{NC},\qquad
\dot H_C=P_{NC}-P_{CR},\qquad
\dot H_R=P_{CR},\qquad \dot H_{\rm tot}=0.
\tag{A5}
\]

For any finite exchange-only window [ta,tb], the corresponding identities are

\[
\begin{aligned}
H_N(t_b)-H_N(t_a)&=-\int_{t_a}^{t_b}P_{NC}\,dt,\\
H_C(t_b)-H_C(t_a)&=\int_{t_a}^{t_b}(P_{NC}-P_{CR})\,dt,\\
H_R(t_b)-H_R(t_a)&=\int_{t_a}^{t_b}P_{CR}\,dt.
\end{aligned}
\tag{A6}
\]

A3 below establishes these identities for the coupled mild solution as well, not just formally differentiable preparations. At H1 carrier regularity, A4 is distributional in space-time and point-cut fluxes have continuous spatial representatives. Arbitrary L2 preparation supports the global account and port averages, without an unrestricted point-cut assertion.

At the all-zero state the vector field vanishes. If x = 0, then f = J = 0; the native zero state stays zero even with a nonzero carrier/receiver. When p = rc = z = 0 but f(x) is nonzero, the carrier immediately begins to change. At z = 0 its instantaneous storage derivative is zero although zdot can be nonzero; quadratic storage can then grow. These cases use no singular normalization. A zero port average at one instant is not a claim that all later port averages vanish.

### A3. Global nonlinear well-posedness theorem

**Statement.** For each fixed allowed finite set of parameters and finite-width profiles, S4 defines a unique global mild solution in

\[
\mathcal H=\mathbb R^6\times L^2_{\rm per}(0,L_c)^2\times\mathbb R^2,
\qquad X\in C(\mathbb R;\mathcal H).
\tag{A7}
\]

The core and receiver are C1 in exchange time. The flow is locally Lipschitz in energy-space preparation on bounded sets over each finite time interval. It conserves Htot and satisfies A6. If the initial carrier belongs to H1_per squared, then

\[
(p,r_c)\in C(\mathbb R;H^1_{\rm per})^2
\cap C^1(\mathbb R;L^2)^2.
\tag{A8}
\]

Dependence also holds in this H1 preparation topology on finite intervals. The exchange-only statement is global in both signs of time; it is not an infinite-native-step boundedness result.

**Bounded ports and translation group.** Direct integration of a tent gives

\[
\int b_\sigma=1,\quad \|b_\sigma\|_2^2=m:=\frac2{3\epsilon_c},
\quad \|b_\sigma'\|_2^2=\frac2{\epsilon_c^3},\quad
M_B=\mathcal B^*\mathcal B=mI_2.
\tag{A9}
\]

Disjoint supports also apply to the weak derivatives up to null endpoints. Thus B and B* have L2 operator norm sqrt(m), and B maps R2 boundedly to H1 with squared operator norm m1 = m + 2/epsilon_c³ in the usual mathematical H1 norm. This auxiliary regularity norm is not a replacement storage. No bound is uniform as epsilon_c tends to zero; no point-interaction limit is taken.

Let v = (p,rc) and A_C v = (−c partial_s rc, −c partial_s p), with domain H1_per squared. In characteristic coordinates (p±rc)/sqrt(2), its group S(t) is periodic translation by ∓ct. It is strongly continuous and isometric in L2 and H1, with generator A_C. These properties follow from translation of trigonometric polynomials, density and the isometry bound, as in the complete C1 source. Define U(t) = diag(Id_R6,S(t),Id_R2) and use the norm

\[
\|X\|_E^2=\alpha_N|x|^2+\|v\|_2^2+\beta_R|z|^2=2H_{\rm tot}(X).
\tag{A10}
\]

This is equivalent to the product norm for fixed positive scales, and U(t) is an isometry. Write G(X) for the three nonlinear/bounded forcing components in S4: core feedback, (B(etaN f − etaR z),0), and receiver feedback. If k0 = ||K||, then

\[
|f(x)|\le(k_0/2)|x|^2,\qquad \|J(x)\|\le k_0|x|,
\qquad |y|\le\sqrt m\,\|p\|_2.
\tag{A11}
\]

The derivative bound follows by bounding |delta a cross b + a cross delta b| by |x| |delta x|. Products of these bounded linear and polynomial expressions show that G is bounded and Lipschitz on every bounded energy-space ball. This is the closed feedback nonlinearity, including its state-dependent drive.

**Local solution and dependence, without presuming energy conservation.** Solve the Duhamel equation

\[
X(t)=U(t)X_0+\int_0^t U(t-s)G(X(s))\,ds.
\tag{A12}
\]

On C([0,T];H), take a ball of radius r around U(t)X0 and choose a state ball containing it. If M and L bound G and its Lipschitz constant there, T M <= r and T L < 1 make the displayed map a self-map and contraction in the uniform norm. Completeness gives a unique fixed point; contraction iteration proves it, with no PDE simulation. The same construction uses U(t) for negative times. For two solutions staying in a common bounded ball,

\[
\|X(t)-\widetilde X(t)\|_E
\le\|X_0-\widetilde X_0\|_E
+L\int_0^t\|X(s)-\widetilde X(s)\|_E ds
\le e^{Lt}\|X_0-\widetilde X_0\|_E.
\tag{A13}
\]

The last inequality follows by iteration/integration of this scalar inequality. Local existence time can be chosen from a bound on ||X0||_E only. Uniqueness and finite-interval dependence follow by covering successive local intervals. These are explicit applications of the complete-space contraction principle and this scalar integral inequality; no additional PDE regularity theorem is assumed.

**H1 propagation and legitimate energy proof.** On any interval of the local energy-space solution, x,z are continuous, hence q(t) = etaN f(x(t)) − etaR z(t) is continuous. For H1 carrier preparation, its Duhamel formula therefore lies in C_t H1 and obeys

\[
\|v(t)\|_{H^1}\le\|v_0\|_{H^1}
+\sqrt{m_1}\int_0^{|t|}|q(\pm s)|\,ds.
\tag{A14}
\]

The translation generator maps H1 to L2; differentiating this formula in L2 proves A8 on the local interval. Consequently the strong energy calculation A4–A6 is justified there. In one spatial dimension the weak product rule and periodic traces justify cancellation of the spatial derivative.

For general L2 preparation, approximate only its carrier by periodic H1 functions converging in L2. Their energy norms are bounded, so the local existence interval above is common. A13 gives convergence in C_t H. In A6, the stocks converge by continuity of squared norms; f(x), z and B*p converge uniformly on that interval, so the finite-time work integrals converge too. Thus A6 and conservation pass to the mild solution. Repeating on local intervals proves the same claim throughout its existence interval. In fact the work integrands are continuous here, so the integrated global identities have continuous time derivatives. We need not infer this from pointwise carrier time differentiation.

**Global continuation.** If E0 = Htot(X0), conservation gives

\[
|x(t)|\le\sqrt{2E_0/\alpha_N},\quad
\|v(t)\|_2\le\sqrt{2E_0},\quad
|z(t)|\le\sqrt{2E_0/\beta_R}.
\tag{A15}
\]

The local contraction time therefore has a uniform positive lower bound along the solution. Repeated restarts rule out any finite forward or backward maximal endpoint. This proves global energy-space existence, not merely a formal conservation assertion. It also gives finite-interval uniform constants in A13 for bounded initial data.

For H1 preparation, the separate forcing bound

\[
|q(t)|\le \eta_N k_0 E_0/\alpha_N
+\eta_R\sqrt{2E_0/\beta_R}=:Q_0
\tag{A16}
\]

and A14 give ||v(t)||_H1 <= ||v0||_H1 + |t| sqrt(m1) Q0. This is the required H1 estimate; an L2 energy bound alone would not suffice. For two preparations, the H1 Duhamel difference is bounded by their initial H1 difference plus sqrt(m1) times the integral of |q − q_tilde|. Local Lipschitzness of f and A13 control the latter, proving H1 continuous dependence. No H2 smoothness at tent corners, delta source or arbitrary L2 point trace is asserted.

## B. Actual exchange, reversibility and usable storage

### B1. Supply and receiver gain from empty preparation

Let etaN, etaR > 0, p0 = rc0 = z0 = 0 and f0 = f(x0) != 0. Such a core exists inside the old coherent domain for every fixed yaw and positive inherited gains. Take

\[
\Omega_0=(1,e^{i\phi},1),\quad 0<\phi<\pi/12.
\]

Then a0 = (1,cos(phi),1), b0 = (0,sin(phi),0), Cch = (−sin(phi),0,sin(phi)), and

\[
f_{0,\pm}=\frac{\kappa_{\rm in}\lambda_g\sin\phi}{\sqrt7}
\{-2\sin\delta_g\pm\sqrt3\}.
\tag{B1}
\]

Their difference is 2 sqrt(3) kappa_in lambda_g sin(phi)/sqrt(7), which is nonzero. The moduli are one and the ordinary phase width is phi, so this is genuinely inside the inherited domain, without selecting a yaw or fitting a gain.

The empty carrier is H1, and A8 gives p'(0) = etaN B f0, rc'(0) = 0 in L2. Therefore, as t decreases to zero through positive values,

\[
p(t)=\eta_Nt\mathcal Bf_0+o(t)\quad\hbox{in }L^2,
\qquad r_c(t)=o(t),\qquad
y(t)=\eta_NtM_Bf_0+o(t).
\tag{B2}
\]

x'(0) = 0 and A2 with the last estimate imply x(t) − x0 = O(t²), hence f(x(t)) = f0 + O(t²). Inserting B2 into A6 and integrating gives

\[
H_N(t)-H_N(0)
=-\frac{\eta_N^2t^2}{2}f_0^TM_Bf_0+o(t^2),
\tag{B3}
\]
\[
z(t)=\frac{\eta_N\eta_Rt^2}{2\beta_R}M_Bf_0+o(t^2),\qquad
H_R(t)=\frac{\eta_N^2\eta_R^2t^4}{8\beta_R}\|M_Bf_0\|^2+o(t^4).
\tag{B4}
\]

Also HC(t) = etaN² t² f0^T M_B f0/2 + o(t²), directly from B2 and A9. The positive definiteness of M_B makes the B3 debit and B4 gain strict for sufficiently small positive t. P_NC has a positive leading term of order t; P_CR has positive leading term etaN² etaR² t³ ||M_B f0||²/(2 betaR). Thus storage changes dynamically, with receiver loading already present in the exact solution.

These expansions need only the proved regularity, first derivatives in L2 and integrals of continuous port outputs. They do not assume smooth tent second derivatives. Both couplings occupy the same finite support regions: the t² receiver state is **not** an arrival-time calculation for a spatially separate aperture or evidence of a full circuit. These are exact asymptotic proofs, not numerically evolved trajectories.

### B2. Prepared native credit and reversible receiving

For the same x0 with nonzero f0, take an allowed H1 preparation

\[
p_0=\pm T_*\mathcal Bf_0,\quad r_{c,0}=0,\quad z_0=0,
\qquad [T_*]=T,\quad T_*>0.
\tag{B5}
\]

Then y0 = ±T_* M_B f0 and

\[
P_{NC}(0)=\pm\eta_NT_*f_0^TM_Bf_0.
\tag{B6}
\]

For etaN > 0, plus gives native debit; minus gives native credit and exactly opposite carrier work at that instant. Continuity makes each strict sign persist over a sufficiently short interval. This proves possible **energetic return through the interface**, for explicitly prepared initial carrier data.

For receiver reversal, any chosen y0 is realized by p0 = B M_B^(-1) y0 in H1. Choose nonzero y0 and z0 with z0 dot y0 < 0. With etaR > 0, HRdot(0) < 0 and the corresponding carrier loading contributes positive work. The opposite dot-product sign charges the receiver. z has its stated source-strength units; no numerical amplitude is selected. These preparations are compatible with all state equations.

The flow also has an exact mathematical reversing involution R(x,p,rc,z) = (x,−p,rc,z): substituting shows G_full(RX) = −R G_full(X) on strong states, and uniqueness extends the reversal relation to mild solutions. This is a mathematical symmetry, not a physical parity assignment. In particular the receiving law supplies neither damping nor one-way disposal.

None of B5–B6 proves that an empty-carrier launch later returns on its own trajectory, identifies a tagged energy cohort, or realizes the intended central geometric route. A complete delayed-return orbit, eventual transfer classification and attainability of the capacity bound below are not proved or required here.

### B3. Dark states, invariant and net capacity

**Dark preparation.** If f(x0) = 0 and p0 = rc0 = z0 = 0, the constant state is a solution of S4 and is unique. In particular an aligned common-phase core Omega0 = e^(i theta) q with q real has Cch = 0 and does not launch from empty preparation. A projection-dark core with Cch in ker(K) has the same empty-preparation conclusion. Noise, a background source and a different readout are not added. A zero drive at one instant with a preloaded carrier is different: J^T y may then change the core even if f is zero.

**Invariant.** A2 gives

\[
\frac d{dt}(|a|^2-|b|^2)=0,\qquad
\frac d{dt}(a\cdot b)=0.
\tag{B7}
\]

Indeed a dot (w cross b) = −w dot (a cross b), while b dot (w cross a) = w dot (a cross b); these cancel in the difference of squared norms. The two terms in the derivative of a dot b each contain a vector dotted with its own cross product and vanish. Thus

\[
Z_2(\Omega)=\sum_i\Omega_i^2
=|a|^2-|b|^2+2i\,a\cdot b
\tag{B8}
\]

is constant during exchange, regardless of receiver state or carrier regularity in A7. This conclusion follows from the actual core equation, not from naming a general framework. No Poisson/Casimir classification is asserted.

The triangle inequality gives |Z2| <= I. Equivalently,

\[
I^2-|Z_2|^2=4\{|a|^2|b|^2-(a\cdot b)^2\}
=4|a\times b|^2\ge0.
\tag{B9}
\]

Consequently, throughout an exchange-only interval beginning at zero,

\[
H_N(t)\ge\frac{\alpha_N}{2}|Z_2(\Omega_0)|,
\quad
H_N(0)-H_N(t)\le\frac{\alpha_N}{2}\{I_0-|Z_2(\Omega_0)|\}.
\tag{B10}
\]

The left difference is signed: native storage may instead increase. The upper bound concerns **net** extraction, integral(P_NC), not the positive work counted repeatedly while energy is returned and supplied again. It is not an attainability theorem; the fixed projection and other dynamical restrictions may reduce what is reachable.

For nonzero amplitudes with phases in an ordinary interval [theta_min,theta_max] of width Delta0 <= pi/12, rotate Z2 by exp(−i(theta_min+theta_max)). Each doubled phase lies within Delta0 of that new axis. Thus

\[
\Re\{e^{-i(\theta_{\min}+\theta_{\max})}Z_2\}
=\sum_i s_i\cos(2\theta_i-\theta_{\min}-\theta_{\max})
\ge I_0\cos\Delta_0,
\tag{B11}
\]

and |Z2| >= I0 cos(Delta0). No persistence of that phase interval is needed, because Z2 itself is invariant. For I0 > 0,

\[
\frac{H_N(0)-H_N(t)}{H_N(0)}
\le1-\cos\Delta_0
\le1-\frac{\sqrt6+\sqrt2}{4}.
\tag{B12}
\]

This exact fraction uses **initial core trial storage** as denominator. It is not the author's diversion fraction or a bound on gross carrier work. At I0 = 0 this normalized expression is undefined; the unnormalized result and invariant native zero state remain valid. At Delta0 = 0, |Z2| = I0, so net core extraction cannot be positive. Empty carrier/receiver plus total conservation then forces complete inactivity, consistently with the dark-state argument. For B1, |Z2| = sqrt(9 − 8 sin²(phi)) < 3, so its strictly positive short-time extraction does not contradict the bound.

Native F jumps can change Z2 and reset this exchange-only capacity. There is no whole-hybrid Z2 conservation law or lifetime capacity claim here.

### B4. Common phase and information use

Under Omega -> exp(i theta) Omega, the real coordinate pair transforms orthogonally as a_theta = cos(theta)a − sin(theta)b and b_theta = sin(theta)a + cos(theta)b. Their cross product is unchanged. Hence f is invariant and J(Q_theta x) = J(x) Q_theta^T. At the same p,rc,z, the native vector field transforms by Q_theta, while the carrier and receiver right sides are unchanged. This proves exchange-flow equivariance by uniqueness. Z2 changes by exp(2i theta), with its modulus and capacity unchanged.

The candidate therefore uses only the common-phase-invariant chiral drive. It need not use every coordinate recovered by the phase reconstruction paper and supplies no common-phase-sensitive outlet selector. Raw channel C, its separate ambient attachment, decoded based face vectors and a spatial transport law remain different objects.

## C. Exact native substep and hybrid consequences

### C1. Retained F and full finite-step square

For the fixed tuple

\[
\epsilon=1/10,\quad g=1/60,\quad\lambda=1/300,\quad
k=(999/1000,1,1001/1000),\quad L_N=\mathbf1\mathbf1^T-3I,
\tag{C1}
\]

the unchanged ideal native map is

\[
s_i=|\Omega_i|^2,\quad
d_{{\rm pre},i}=\epsilon(k_i-s_i)\Omega_i
+g\sum_{j\ne i}(\Omega_j-\Omega_i),\quad
\widetilde\Omega=\Omega+d_{\rm pre},
\tag{C2}
\]
\[
\delta_i=\lambda\sum_{j\ne i}\sin\{3[\operatorname{Arg}_0\widetilde\Omega_j
-\operatorname{Arg}_0\widetilde\Omega_i]\},\quad
F_i(\Omega)=e^{i\delta_i}\widetilde\Omega_i,\quad \operatorname{Arg}_0(0)=0.
\tag{C3}
\]

All prestage kicks use the same original state; all synchronizer increments use the same prestage. Exact zero components remain zero after synchronization. The source bypasses phase extraction when lambda = 0, although the candidate's fixed lambda is nonzero. No normalization, continuous gradient replacement or coefficient change is made.

Synchronization preserves each prestage modulus, so direct expansion gives, with each undirected edge once,

\[
I(F\Omega)-I(\Omega)
=2\epsilon\sum_i s_i(k_i-s_i)
-2g\sum_{i<j}|\Omega_i-\Omega_j|^2+\|d_{\rm pre}\|^2.
\tag{C4}
\]

The factor two in the graph term comes from the two endpoints of an edge. If h_i = (k_i − s_i) Omega_i, then the entire square is

\[
\|d_{\rm pre}\|^2=\epsilon^2\|h\|^2
+2\epsilon g\Re(h^\dagger L_N\Omega)
+g^2\|L_N\Omega\|^2,\qquad
\|L_N\Omega\|^2=3\sum_{i<j}|\Omega_i-\Omega_j|^2.
\tag{C5}
\]

Neither the mixed term nor the complete intensity increment has a predetermined sign. C4 holds also on zero-prestage strata. This is the inherited exact identity, independently reconciled algebraically here; d_pre is not the full displacement F(Omega) − Omega.

### C2. Ordered composition and storage increment

Let Phi_h be the exact global exchange flow just proved. For any new symbolic cadence h_ex > 0, define

\[
X_{n+1}=\Phi_{h_{\rm ex}}(F_R(x_n),p_n,r_{c,n},z_n).
\tag{C6}
\]

The state is sampled before its next native jump: first apply F, then propagate and exchange for h_ex. No numerical integrator is defined. Since the exchange conserves Htot and the jump changes only x,

\[
H_{\rm tot}(X_{n+1})-H_{\rm tot}(X_n)
=\frac{\alpha_N}{2}[I(F\Omega_n)-I(\Omega_n)].
\tag{C7}
\]

This is a **native baseline storage increment**. It is neither carrier work nor receiver work, and it is not assigned to an external physical source by renaming it. Over finitely many full steps the total change is the sum of these baseline increments. No compensating reservoir is introduced.

The accepted quartic V has d_pre = −grad_R6 V and a descent theorem for F on its stated coherent domain and tuple. This does not say that HN descends. An exact algebraic example is Omega = (1,1,1), for which synchronization is inactive and

\[
F\Omega=(9999/10000,1,10001/10000),\qquad
I(F\Omega)-3=1/50000000>0.
\tag{C8}
\]

Both the state and its prestage are aligned and in the accepted domain. Thus native trial storage can increase while the separate accepted V theorem applies. The real Z2 also increases in this example. This is a single rational formula evaluation, not a trajectory experiment. V decrease supplies no identified recipient, and S4 has not been asserted to decrease V. The full hybrid is not automatically a closed energy-conserving physical system.

### C3. Limiting cases, timing and finite-index existence

| Limit or comparison | Exact consequence |
|---|---|
| etaN = etaR = 0 | x is constant during every exchange interval; the sampled core is exactly F^n of its preparation. The carrier follows source-off C1 for elapsed exchange time n h_ex; the receiver is constant. |
| etaR = 0 | z is constant and exerts no load. Native/carrier exchange can remain active when etaN > 0. |
| etaN = 0 | x is constant during exchange but still undergoes F at native jumps. Carrier/receiver coupling can remain active. A prepared receiver can load or supply the carrier. |
| Clamp x to an external history, suppress its feedback, etaR = 0 | The carrier is exogenous C1 with drive etaN f(x_history(t)). With etaN = 1 it is exactly the inherited chiral drive amplitude; a specified hold recovers that comparison protocol. A retained drive with its debit omitted needs an external work account. |

At nonzero native coupling, S4 recomputes f from the evolving x, using the current carrier response in return. This is not the old sample/hold model under another name. h_ex is a new cadence, separate from static geometric tau, native step number, observer clock and Lc/c. Without external forcing, the internal source/loading B(etaN f − etaR z) may still be nonzero. Consequently the old source-off carrier period Lc/c is not automatically a period of the coupled flow. If the complete internal forcing is zero throughout an interval, the source-off carrier theorem applies to that interval on its own hypotheses.

For every finite ideal state, C2 is finite and C3 defines a finite next state by the exact zero convention. A3 then defines the next whole exchange interval. Induction therefore proves existence of every finite hybrid step for H or H1 preparations, even after leaving the coherent domain. It proves no uniform bound as n tends to infinity.

Regular dependence is a separate issue. Where all encountered prestages have nonzero components, F is smooth: the sine of three phase differences can be written in terms of normalized nonzero complex components, so a branch cut in an individual argument is not itself an obstruction. For a finite number of such jumps, a positive lower bound on those component moduli holds in a sufficiently small preparation neighborhood; composition with A13 gives local continuous/Lipschitz dependence. On zero-prestage strata the convention defines the map but gives no general smoothness or continuity guarantee for neighbors whose synchronization uses that phase. The smooth exchange flow does not remove this native qualification. No global quotient/convergence theorem is transferred to the hybrid system.

### C4. The coherent domain is not universally preserved

Let D be the inherited domain 9/10 <= |Omega_i| <= 11/10 with ordinary phase width <= pi/12. For etaN > 0, take

\[
\Omega_0=(1,e^{i\phi},1),\quad \phi=\pi/12,\quad
w_0=K^Ty_0=-W e_z,\qquad W>0.
\tag{C9}
\]

This feedback direction is accessible for every fixed yaw, since with gamma = kappa_in lambda_g,

\[
y_0=\frac{\sqrt7W}{2\sqrt3\gamma}(-1,1),\qquad
p_0=\mathcal B M_B^{-1}y_0,\quad r_{c,0}=z_0=0
\tag{C10}
\]

realizes it with an H1 carrier. From A2,

\[
\dot\theta_1(0)=-\mu W\cos\phi,\qquad
\dot\theta_2(0)=+\mu W\cos\phi,\qquad
\dot\theta_3(0)=0.
\tag{C11}
\]

For small positive time theta1 becomes the minimum and theta2 remains the maximum. Hence the right derivative of ordinary phase width is 2 mu W cos(phi) > 0. The moduli start strictly between the radial bounds, so the initial exit is through the phase boundary. This explicitly refutes invariance of D under N4 for arbitrary allowed carrier preparations. Nothing is clamped or normalized.

Failure of a substep's invariance alone would not logically prove failure of every sampled composition. The following additional analytical construction establishes that N5 has **no universal D-invariance over its allowed preparations and cadences** either. Start a hybrid step at Omega = (1,1,1), so the native jump gives q = (q1,q2,q3) from C8. Choose an H1 profile p_bar with K^T B*p_bar = −W e_z, and set the initial carrier to R p_bar, rc = z = 0, for a dimensionless R > 0. Introduce fast time tau = R t and keep all model constants fixed.

On each fixed bounded tau interval, energy bounds give bounded ||p_R/R||_2, while the core equation and Gronwall give |x_R(tau/R)| <= |q| exp(C tau) uniformly in R; integrating the receiver equation gives |z_R(tau/R)| <= C tau. Duhamel and strong continuity of translations give, uniformly there,

\[
p_R(\tau/R)/R\longrightarrow p_{\rm bar},\qquad
K^Ty_R(\tau/R)/R\longrightarrow-W e_z.
\tag{C12}
\]

Indeed the initial free term divided by R is S(tau/R)(p_bar,0) -> (p_bar,0). The forcing term divided by R is bounded by a constant times 1/R² on such intervals, using the preceding x,z bounds. Finite-dimensional integral equations and a Lipschitz/Gronwall estimate then give uniform convergence of the core to the exact constant-feedback limit

\[
\frac{d\Omega}{d\tau}=i\mu W e_z\times\Omega,\quad
\Omega_1=q_1\cosh(\mu W\tau)-i q_2\sinh(\mu W\tau),
\]
\[
\Omega_2=q_2\cosh(\mu W\tau)+i q_1\sinh(\mu W\tau),\qquad
\Omega_3=q_3.
\tag{C13}
\]

Choose the symbolic finite tau_star with tanh(mu W tau_star) = 1/4. The limiting phase width is

\[
\arctan\frac{q_2}{4q_1}+\arctan\frac{q_1}{4q_2}>\pi/12.
\tag{C14}
\]

For example q2/q1 and q1/q2 are both greater than 9/10, so the left side exceeds 2 arctan(9/40), which exceeds pi/12: tan(pi/24) = sin(pi/12)/(1+cos(pi/12)) < (1/3)/(3/2) = 2/9 < 9/40. These are exact inequalities, not sampled trajectories. Uniform convergence and nonzero limiting components preserve the strict excess for sufficiently large finite R. Choose h_ex = tau_star/R for that preparation. The sampled N5 output is then outside D. This existential cadence/preparation witness does not say every prescribed cadence or empty-carrier launch exits.

The older F-only invariance, V-descent and coherent-coordinate results therefore remain valid on their original scope, but cannot be promoted to general N4/N5 theorems. At etaN = 0, native sampling still follows F and retains its old domain property; this special decoupling does not contradict the counterexamples.

## D. What the receiver work counts

### D1. Per-port positive and negative transfers

On a common declared finite interval define

\[
P_{N,\sigma}=\eta_N f_\sigma(x)y_\sigma,\qquad
P_{R,\sigma}=\eta_R z_\sigma y_\sigma,
\tag{D1}
\]
\[
\begin{aligned}
Q_{N\to C}&=\int\sum_\sigma[P_{N,\sigma}]_+dt,&
Q_{C\to N}&=\int\sum_\sigma[-P_{N,\sigma}]_+dt,\\
Q_{C\to R}&=\int\sum_\sigma[P_{R,\sigma}]_+dt,&
Q_{R\to C}&=\int\sum_\sigma[-P_{R,\sigma}]_+dt.
\end{aligned}
\tag{D2}
\]

Positive/negative parts are taken **per port before summation**. If two simultaneous port powers are A and −A with A > 0, this convention counts A in each direction; taking a positive part after summing would count zero. These are matched interface work amounts, not geometric section fluxes, distinct energy cohorts or per-pass toroidal throughput. They are finite because the ports and powers are continuous on finite exchange intervals; finite hybrid windows have finitely many such intervals.

For hybrid windows in this section, use post-jump endpoint values when an endpoint is a jump instant, and count jumps with ta < t_j <= tb. The pre-jump samples in equation C6 can instead be handled with their corresponding left limits and the matching included jumps. Let B_N be the sum of alphaN [I(F Omega_minus) − I(Omega_minus)]/2 over the included native jumps. The exact accounts are

\[
\begin{aligned}
\Delta H_N&=B_N-Q_{N\to C}+Q_{C\to N},\\
\Delta H_C&=Q_{N\to C}-Q_{C\to N}-Q_{C\to R}+Q_{R\to C},\\
\Delta H_R&=Q_{C\to R}-Q_{R\to C},\\
\Delta H_{\rm tot}&=B_N.
\end{aligned}
\tag{D3}
\]

For an exchange-only window B_N = 0. Native jumps leave the carrier and receiver continuous and produce no impulsive port work in this model; their storage increment must be booked separately. Equation D3 answers what the receiver actually measures: signed retained trial storage equals signed matched work.

### D2. Ratios and actual restrictions

Both Delta HR/Q_NtoC and Q_CtoR/Q_NtoC require Q_NtoC > 0. In B1 this denominator is positive for sufficiently small positive time; dark or fully decoupled preparations can give zero, making the ratios undefined. The first is a signed receiver-storage-change ratio and the second a gross receiving-work ratio. Neither automatically measures efficiency or permanently diverted energy.

From D3,

\[
\Delta H_R=Q_{N\to C}-Q_{C\to N}-\Delta H_C.
\tag{D4}
\]

For an exchange-only experiment with **both carrier and receiver initially empty**, this yields

\[
0\le\Delta H_R=H_R(t)\le Q_{N\to C},
\tag{D5}
\]

because HC(t) and Q_CtoN are nonnegative. Thus the retained ratio is in [0,1] under precisely these restrictions and a positive denominator. If additionally Q_RtoC = 0, the same bound applies to the gross receiver ratio. Without that no-backflow condition, gross receiving can count repeated exchange; D5 is not a bound on Q_CtoR.

There is a limited further point that should not be obscured: D4 still holds across native jumps, because they change neither HC nor HR. Therefore the initially-empty retained-ratio bound also survives a finite hybrid window with the same start condition and the same complete per-port counting. Baseline native increments nevertheless invalidate interpreting its denominator as depletion of the *initial native stock*, or applying B10/B12 unchanged across those jumps. They do not by themselves violate D5.

For arbitrary preparation there is no universal [0,1] bound. HC may release an initial stock, allowing positive Delta HR to exceed Q_NtoC; a prepared receiver may release stock, making Delta HR negative. These are dynamically admissible possibilities, not just formal ledger options. Choose f0 != 0, y0 = T_star M_B f0 with T_star > 0, and z0 = A f0 for dimensionless A > 0. Then Q_NtoC has positive instantaneous rate etaN T_star f0^T M_B f0, whereas the receiver rate is etaR A T_star f0^T M_B f0. For etaN,etaR > 0, any symbolic A > etaN/etaR makes the small-window retained and gross ratios tend to etaR A/etaN > 1. Taking A < 0 gives a negative retained ratio. All preparations have finite trial storage and are allowed by A3. No trajectory or parameter scan is used.

Initial receiver/carrier stock, return work, repeated transfers and native baseline increments must therefore accompany any interpretation. Permanent siphoning would require a separately justified irreversible mechanism, further state or loading law; none is added. C6 remains an unloaded observation, not this receiver, and its squared records are not substituted for HR or a work integral.

## E. Geometry, evidence limits and review boundary

The candidate now has an analytical receiving location in the storage account and a specified loading location on C1's two finite profiles. It does not assign the receiver a physical location, material body, surface aperture or a path to the six central openings. In particular:

- The selected host-notch measurement triangles N1+ and N1− differ from all six two-segment broken arcs Gk+ and Gk−. Two port coordinates do not define six outlet allocations or filled holes.
- The original close enclosing sphere is a geometric reference, not a wall; it differs from the extended-line sphere, intended tight toroid and opposed cones.
- The support lines remain stationary. Native common phase, static shape tau, iteration index, observer clock and exchange time retain distinct meanings. Decoded vector lengths are not travel distances.
- The known offset circle misses exact O. That fact does not exclude every finite central starting/meeting region. No receiving/control region or registration to the intended central route is selected. A one-dimensional circle neither specifies nor rules out a surrounding three-dimensional field.
- No central closing chord, new material attachment, toroidal field law, six-port coupling, electromagnetic law or gravity–magnetism correspondence is deduced from the storage equations.

The proposed mathematical balances do not validate the author's physical picture or numerical diversion intuition. They make the reciprocal candidate testable at its own stated mathematical scope. The retained capacity is a serious constraint on what this particular chiral completion can supply from a coherent empty-carrier preparation; its denominator must not be confused with a receiving-work share.

The standalone exact-algebra helper checks the finite algebra behind the Jacobian, signs, invariant, phase covariance, tent norms, short-time coefficients, native finite square and domain witnesses. Its results are evidence separate from the written proofs. It does not establish functional analysis, asymptotic remainders or physical claims by computation. No numerical native trajectory, PDE simulation, parameter fitting, scan, geometry constructor, old helper, project import, installation or Git command was run for this investigation.

**Review disposition:** A and B pass at the proved exchange-stage scope; C passes as an exact finite-step extension with an exposed native baseline increment and a refuted universal coherent-domain claim. No algebraic defect requires replacing the specified candidate. Decisions about accepting its trial storage, improving usable capacity, choosing a central-route registration, or adding irreversible receiving remain for GPT/author review. The report stops here; it does not adopt the candidate or commission a successor.
