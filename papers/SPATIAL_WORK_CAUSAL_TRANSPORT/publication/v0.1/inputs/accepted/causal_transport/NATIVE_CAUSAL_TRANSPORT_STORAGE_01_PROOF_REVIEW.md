# Causal transport and storage candidate: independent proof review

**Task:** NATIVE_CAUSAL_TRANSPORT_STORAGE_01  
**Reviewer:** Codex  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Disposition:** T01-T07 of the analytical start are verified as stated at their submitted assumptions. No candidate equation, state metric or mathematical theorem needs replacement. One necessity-sounding sentence in the work order needs the clarification D01 below; the analytical start already states the correct sufficient condition.

The candidate supplies an explicit causal mathematical connection with nonnegative transport and receiving stocks, global forward mild evolution, exact augmented exchange conservation, and a nontrivial carrier-funded receiving and incoming-return example. C6 remains the exact direct observation component; it is not generally the whole loaded receiving drive. No physical curved route, aperture, material energy density, receiving location or calibrated clock follows from these results. This is an independent review returned for GPT/author assessment, not their acceptance of this new candidate or adoption of its physical interpretation.

## R0. Controlling definitions, evidence and scope

The equations being assessed are N1-N24 in the [supplied analytical start](inputs/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_GPT_ANALYTICAL_START.md). These are proposed equations. The supplied [claim ledger](inputs/CLAIM_LEDGER.json) identifies their seven claim groups. The completed W investigation, including its [proof](inputs/accepted/spatial_work/NATIVE_SPATIAL_WORK_REGISTRATION_01_PROOF_REVIEW.md), [GPT review](inputs/accepted/spatial_work/NATIVE_SPATIAL_WORK_REGISTRATION_01_GPT_REVIEW.md) and [acceptance record](inputs/accepted/spatial_work/GPT_ACCEPTANCE.json), is used as an accepted input. Its proofs, earlier investigations and the publication are not re-executed here.

| Source key | Retained local source | Role and exact locators |
| --- | --- | --- |
| NEW | [Analytical start](inputs/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_GPT_ANALYTICAL_START.md) | N1-N6 factorization; N7-N11 transport; N12-N15 coupled model/theorem; N16-N17 C6; N18 hybrid; N19-N24 latency/activity. |
| W | [Accepted proof](inputs/accepted/spatial_work/NATIVE_SPATIAL_WORK_REGISTRATION_01_PROOF_REVIEW.md) | R1 geometry/finite horizon; R2 causal L2 observation; R3 temporal adjoint; R5 signed conditional work. |
| CC-C | [Carrier](inputs/sources/CC/carrier.tex) | `eq:C1`, `eq:storage`, `eq:C6`; original free carrier, flux and retarded observation. |
| CC-G | [Geometry](inputs/sources/CC/geometry.tex) | `eq:vertices`, `eq:G`, `eq:circleconstants`, `eq:circle`; actual arcs and selected unit-tangent circle. |
| RX-C | [Candidate](inputs/sources/RX/candidate.tex) | `eq:drive`, `eq:tents`, `eq:ports`, `eq:storages`, `eq:system`; retained native/old-receiver equations and stores. |
| RX-P | [Power](inputs/sources/RX/power.tex) | `eq:jacobian`, `eq:localwork`, `eq:balances`; homogeneous native drive and original reciprocal cancellation. |
| RX-W | [Well-posedness](inputs/sources/RX/wellposed.tex) | `eq:profilenorms`, `eq:lipschitzbounds`, `eq:energynorm`; bounded ports, local polynomial structure and periodic unitary group. The original theorem is not treated as a theorem for the new model. |
| RX-H | [Hybrid](inputs/sources/RX/hybrid.tex) | `eq:tuple`, `eq:prestage`, `eq:nativemap`, `eq:hybrid`, `eq:hybridbalance`; original map and order. |
| RX-A | [Accounts](inputs/sources/RX/accounts.tex) | `eq:baselinewindow` and its preceding paragraph; post-jump endpoints and baseline count. |
| GEO | [Geometry/model boundary](inputs/context/GEOMETRY_MODEL_BOUNDARY.md) | Inherited endpoint delay versus physical curved path; product measure versus material density. |
| STATUS | [Current research list](inputs/context/TRIOCTAGON_RESEARCH_STATUS_2026-11-10.md), [paper plan](inputs/PAPER_PLAN.md) | Accepted W status, standing research qualifications and later manuscript boundary. |

`SOURCE_LOCATORS.json` gives current paths, exact source lines and hashes. `INPUT_IDENTITIES.json` records all 63 preserved packet members, all 62 manifest checks and all 46 registered source identities. It also binds the supplied W proof to its acceptance record and checks the supplied acceptance archive's checksum. These are input-identity checks, not a new audit of the older mathematical investigations. The original source checkpoints remain in `inputs/SOURCE_IDENTITIES.json`.

The preparation notes and the method reference are retained as context, not proof of this infinite-dimensional candidate. All claims below follow from the specified operators, characteristics and integral equations. Five new algebra groups E01-E05 corroborate limited symbolic issues only; no mesh simulation, parameter scan or pre-existing scientific suite is used as acceptance evidence.

### Fixed setting

Fix a common width, one admitted static geometry and one hand. Let S be the selected arclength circle of length L, and G the **disjoint labeled union** of the six actual two-segment arcs, with total arclength M. Both L and M are finite and positive. No closing chord, filled aperture or normal is added. Write \(\Lambda=S\times G\), \(d\mu=ds\,d\ell_X\), and use real spaces

\[
U=L^2(S;\mathbb R^2),\quad V=L^2(\Lambda;\mathbb R^2),\quad Y=L^2(G;\mathbb R^4).
\]

Accepted W supplies a continuous distance \(d_X(s)=|X-\gamma_w(s)|>\delta_w=297w/5000\), a finite upper distance bound, and a unit tangent \(\hat t(s)\). Thus
\(\theta_X(s)=d_X(s)/c_e\) has actual extrema
\(0<\theta_-\le\theta_X(s)\le\theta_+<\infty\).
Neither extremum needs numerical optimization. All geometric data are fixed in time; \(c_e,g_o>0\), \(a_o=g_o/(4\pi)\), \(\kappa\ge0\), and \(\beta_G>0\) are fixed finite parameters. The retained RX parameters, finite-width H1 tents and positive storage weights are unchanged.

Use Q=(p,r_c) for the old carrier, x for the native state and z for the **old** two-coordinate receiver. The new receiver is \(\zeta\in Y\). The new spatial duplication J is different from the native derivative \(J_f\); C is different from the native raw chiral observable; \(\mathcal B\) denotes the old profile operator. Boundary signals a,b,c,d are not the real/imaginary native vectors. Write \(c_{\rm car}\) for the old carrier speed, and \(F_{\rm native}\) for the native map, reserving \(\mathcal F\) for the added carrier force.

## R1. T01: bounded spatial factorization and Gram operator

Define \(A_s(p,r_c)=(p,r_c\hat t(s))\). It is a four-by-two isometry because \(|\hat t|=1\). Direct integration gives

\[
(JQ)(s,X)=M^{-1/2}Q(s),\qquad
(J^*v)(s)=M^{-1/2}\int_Gv(s,X)d\ell_X,\quad J^*J=I_U. \tag{R1.1}
\]

Indeed \(\|JQ\|_V^2=M^{-1}\int_G\int_S|Q|^2=\|Q\|_U^2\). Pairing JQ with v and applying Fubini proves the displayed adjoint; hence \(\|J\|=\|J^*\|=1\).

For the proposed mixer,

\[
(Cv)(X)=a_o\sqrt M\int_S\frac{A_sv(s,X)}{d_X(s)}ds,\qquad
(C^*\zeta)(s,X)=\frac{a_o\sqrt M}{d_X(s)}A_s^*\zeta(X). \tag{R1.2}
\]

The first is well-defined a.e. X. Cauchy-Schwarz in s followed by integration in X gives
\(\|Cv\|_Y^2\le a_o^2ML\delta_w^{-2}\|v\|_V^2\).
This bound also justifies the pairing interchange that proves the adjoint formula. Thus \(\|C\|=\|C^*\|\le a_o\sqrt{LM}/\delta_w\), as an upper bound rather than an optimal-norm assertion.

For a complete history, time translation at fixed (s,X) gives \((D_\theta h)(s,X,t)=h(s,X,t-\theta_X(s))\). On whole-time L2 histories it preserves the norm, and on finite windows it has the corresponding restriction bound. Fubini proves representative independence; no single-time trace of an arbitrary L2 history is needed. Multiplying the two factors \(\sqrt M\) and \(1/\sqrt M\) in (R1.1)-(R1.2) cancels them exactly:

\[
(CD_\theta JQ)(X,t)=a_o\int_S\frac{A_sQ(s,t-\theta_X(s))}{d_X(s)}ds
=\mathcal K_GQ(X,t). \tag{R1.3}
\]

For example this identity holds in the accepted finite-window spaces when Q is supplied on \([-\theta_+,T]\), and pointwise records require the stronger history regularity already specified in W. Factorization alone constructs no energy store.

Write \(B(X)\) for the following four-by-four matrix, unrelated to \(\mathcal B\):

\[
(CC^*\zeta)(X)=B(X)\zeta(X),\quad
B(X)=a_o^2M\int_S\frac{\operatorname{diag}(1,\hat t(s)\hat t(s)^T)}{d_X(s)^2}ds. \tag{R1.4}
\]

For \(\zeta=(\zeta_{\rm sc},\zeta_v)\), its quadratic form is the integral of
\(a_o^2M d^{-2}(|\zeta_{\rm sc}|^2+|\hat t\cdot\zeta_v|^2)\), so it is nonnegative. It is a bounded measurable multiplication operator, with \(\|B(X)\|\le a_o^2ML/\delta_w^2\). Its scalar block satisfies

\[
0<\frac{a_o^2ML}{(c_e\theta_+)^2}\le m_0(X):=a_o^2M\int_Sd_X(s)^{-2}ds
\le\frac{a_o^2ML}{\delta_w^2}. \tag{R1.5}
\]

The vector block need not be invertible. If n is a unit normal to the selected carrier plane, then \(\hat t(s)\cdot n=0\) for all s, so \(\zeta(X)=(0,h(X)n)\) lies in \(\ker C^*\) for every \(h\in L^2(G)\). This will also give the D01 counterexample in R6.

No condition \(\|C\|\le1\) is used: the later cancellation pairs C with its adjoint in effort/flow work. It does not assert that C itself is a norm-preserving or contractive scattering map. E01 checks the tangent matrices, normalization, direct coefficient and explicit normal-vector kernel. T01 is verified as stated.

## R2. T02: variable-length transport, legitimate time traces and storage

Let \(\mathcal D=\{(s,X,\xi):0<\xi<\theta_X(s)\}\), and \(\mathcal W=L^2(\mathcal D;\mathbb R^2)\oplus L^2(\mathcal D;\mathbb R^2)\). The new equations are
\(\partial_tu_++\partial_\xi u_+=0\) and \(\partial_tu_--\partial_\xi u_-=0\).
Their inflows are \(a=u_+(0)\) and \(d=u_-(\theta)\); their outflows are \(c=u_+(\theta)\) and \(b=u_-(0)\). These four symbols have these specific orientations.

### R2.1 Characteristics and boundary representatives

For a fixed channel label \(\lambda=(s,X)\), set \(\ell=\theta_X(s)\). The forward solution is

\[
u_+(\lambda,\xi,t)=
\begin{cases}u_{+,0}(\lambda,\xi-t),&t<\xi,\\
a(\lambda,t-\xi),&t\ge\xi.
\end{cases} \tag{R2.1}
\]

For the backward solution either trace its characteristics directly or put \(\eta=\ell-\xi\). Reflection in each fixed fiber preserves Lebesgue measure, and the reflected profile obeys the forward equation with inflow d. It follows that

\[
u_-(\lambda,\xi,t)=
\begin{cases}u_{-,0}(\lambda,\xi+t),&t<\ell-\xi,\\
d(\lambda,t-\ell+\xi),&t\ge\ell-\xi.
\end{cases} \tag{R2.2}
\]

Consequently, as time traces,

\[
c(\lambda,t)=\mathbf1_{0\le t<\ell}u_{+,0}(\lambda,\ell-t)+\mathbf1_{t\ge\ell}a(\lambda,t-\ell),
\]
\[
b(\lambda,t)=\mathbf1_{0\le t<\ell}u_{-,0}(\lambda,t)+\mathbf1_{t\ge\ell}d(\lambda,t-\ell). \tag{R2.3}
\]

Equalities at seams are immaterial in the L2 time-space interpretation. For any H>0, substitution \(\xi=\ell-t\) and Fubini give

\[
\int_0^H\|c(t)\|_V^2dt\le\|u_{+,0}\|_{L^2(\mathcal D)}^2+
\int_0^H\|a(t)\|_V^2dt,\quad
\int_0^H\|b(t)\|_V^2dt\le\|u_{-,0}\|_{L^2(\mathcal D)}^2+
\int_0^H\|d(t)\|_V^2dt. \tag{R2.4}
\]

There is no extra factor two: for each channel the startup and delayed pieces occupy disjoint time intervals. The substitution \(\xi=t\) proves the backward startup estimate. The delayed terms use a time translation of unit Jacobian. Applied to differences of representatives that vanish in L2, these estimates prove independence a.e. in (s,X,t). They provide legitimate locally L2 time traces for arbitrary finite-energy profiles, not a claim that such a profile has a value at a boundary at a prescribed instant.

### R2.2 Strong continuity of the evolving energy state

Extend a forward initial profile by zero from \(0<\xi<\ell\) to the whole real ξ-line. On a finite time horizon also extend its inflow by zero from nonnegative times to the whole time line. Formula (R2.1) is the restriction to \(\mathcal D\) of the sum of the translated initial extension \(v_0(\xi-t)\) and the reflected translated inflow extension \(h(t-\xi)\); their supports do not overlap except at a null seam. Translation is strongly continuous on \(L^2(\Lambda\times\mathbb R)\), first for smooth finite sums and then by density and its isometry bound. Restriction has norm at most one. This proves continuity in \(L^2(\mathcal D)\), including t=0. For u-minus, the fixed fiber reflection is an isometry, so the same proof applies. Thus \((u_+,u_-)\in C([0,H];\mathcal W)\) even without corner compatibility.

### R2.3 Integrated power without spatial Sobolev traces

For a single forward channel with initial profile v0 and inflow h, direct substitution in (R2.1) gives

\[
\int_0^\ell|v(\xi,t)|^2d\xi
=\int_0^{(\ell-t)_+}|v_0(\eta)|^2d\eta
+\int_{(t-\ell)_+}^{t}|h(r)|^2dr. \tag{R2.5}
\]

Subtract the initial norm. The loss of initial profile equals the time integral of the startup outflow, and the part of h that has already exited equals the integral of its delayed outflow. Hence
\(\|v(t)\|^2-\|v_0\|^2=\int_0^t(|h|^2-|o|^2)dr\), where o is its outflow. All terms are integrable by (R2.4), so integrate over labels and apply the same identity to the reversed fibers. With

\[
E_{\rm tr}=\tfrac12(\|u_+\|_{L^2(\mathcal D)}^2+\|u_-\|_{L^2(\mathcal D)}^2)\ge0,
\quad P_N=\tfrac12(\|a\|_V^2-\|b\|_V^2),\quad
P_G=\tfrac12(\|c\|_V^2-\|d\|_V^2),
\]

one obtains, for every T in the constructed interval,

\[
E_{\rm tr}(T)-E_{\rm tr}(0)=\int_0^T(P_N-P_G)dt. \tag{R2.6}
\]

The energy is absolutely continuous, with the derivative identity a.e. The state continuity above removes any ambiguity about its endpoint values. This proof uses arbitrary L2 profiles and inflows directly. It requires neither integration by parts at unsupported boundary traces nor a derivative of θ. The variable delay enters as a static fiber length; ξ is mathematical travel time, not an embedded physical arclength or a G-surface flow. E03 independently checks both orientations and both startup regimes using exact polynomial profiles with incompatible corners and symbolic positive delay. T02 is verified as stated.

## R3. T03: the closed candidate and its augmented work identity

### R3.1 Retained subsystem and the proposed boundary laws

Write \(x=(a_N,b_N)\), \(f(x)=K(a_N\times b_N)\), \(J_f=D_xf\), \(q=\eta_Nf-\eta_Rz\), \(y=\mathcal B^*p\). The retained equations are

\[
\dot x=-\frac{\eta_N}{2\alpha_N}J_f^Ty,\qquad
\dot z=\frac{\eta_R}{\beta_R}y,
\quad A_c(p,r_c)=(-c_{\rm car}(r_c)_s,-c_{\rm car}p_s).
\]

The derivative identity \(J_fx=2f\) follows by differentiating the degree-two cross product in the direction x; the source one-half therefore gives \(\dot H_N=-\eta_N f\cdot y\), while \(\dot H_R=\eta_Rz\cdot y\). The old carrier source supplies the opposite sum by \(\langle p,\mathcal Bq\rangle=\langle\mathcal B^*p,q\rangle\).

The proposed near effort and flow are \(e_N=(a+b)/\sqrt2=\kappa JQ\), \(f_N=(a-b)/\sqrt2\). Solving for a and setting \(\mathcal F=-\kappa J^*f_N\) gives

\[
a=\sqrt2\kappa JQ-b,\qquad
\mathcal F=-\kappa^2Q+\sqrt2\kappa J^*b,\qquad
\dot Q=A_cQ+(\mathcal Bq,0)+\mathcal F. \tag{R3.1}
\]

At the far end, \(e_G=(c+d)/\sqrt2=C^*\zeta\), \(f_G=(c-d)/\sqrt2\), and \(\beta_G\dot\zeta=Cf_G\) similarly imply

\[
d=\sqrt2C^*\zeta-c,\qquad
\beta_G\dot\zeta=\sqrt2Cc-CC^*\zeta. \tag{R3.2}
\]

All four laws agree exactly with N12; no boundary law or preparation has been substituted. Inflows b,c in these equations are the causal outflows of the two channels in (R2.3).

### R3.2 Component powers and total conservation

The real Hilbert identity
\(\langle(v+w)/\sqrt2,(v-w)/\sqrt2\rangle=(\|v\|^2-\|w\|^2)/2\)
holds without a contraction hypothesis. Thus

\[
\langle Q,\mathcal F\rangle_U
=-\langle e_N,f_N\rangle_V=-P_N,
\quad\frac{d}{dt}\frac{\beta_G}{2}\|\zeta\|_Y^2
=\langle C^*\zeta,f_G\rangle_V=P_G. \tag{R3.3}
\]

Equivalently the near power is \(-\kappa^2\|Q\|^2+\sqrt2\kappa\langle JQ,b\rangle\), and the receiving power is \(\sqrt2\langle C^*\zeta,c\rangle-\|C^*\zeta\|^2\). Expanding the two outgoing-wave norms gives these exact expressions. The native, carrier and old z powers cancel internally except for the added force, so

\[
H_{\rm RX}=\frac{\alpha_N}{2}|x|^2+\frac12\|Q\|_U^2+\frac{\beta_R}{2}|z|^2,
\quad H_G=\frac{\beta_G}{2}\|\zeta\|_Y^2,\quad
\boxed{H_{\rm total}=H_{\rm RX}+E_{\rm tr}+H_G\ \text{is constant during exchange}.} \tag{R3.4}
\]

At this stage (R3.3) is algebra with legitimate integrated meaning whenever the component solutions have the regularity proved in R4. R4 establishes those identities before using their sum, avoiding a circular existence argument. E02 checks the complete near/far cancellation and original-port cancellation for arbitrary efforts, not for a chosen small gain.

The new H_G counts ζ, not old z; the old H_R is already in H_RX. The apparently dissipative terms in (R3.1)-(R3.2) have explicit traveling-wave counterparts in (R2.6). They are not an undeclared sink. H_G need not be monotone: with empty lines and \(C^*\zeta_0\ne0\), c vanishes on the first short interval and \(H_G'(0+)=-\|C^*\zeta_0\|^2<0\). The lost receiving stock enters the reverse-traveling state.

### R3.3 Consistent abstract units

Let [Q]=U, [s]=[ℓ]=L, [ξ]=T and [g_o]=G_o. Then [JQ]=U L^(-1/2). The assignments below make each equation and stock commensurate:

| Quantity | Proposed abstract dimension |
| --- | --- |
| κ | T^(-1/2) |
| a,b,c,d and u-plus/u-minus | U L^(-1/2) T^(-1/2) |
| ζ | U G_o^(-1) T^(-1/2) |
| β_G | G_o^2 T |
| Cc and CC*ζ | U G_o T^(-1/2) |
| added force | U/T |
| E_tr and H_G | U^2 L |

For example C multiplies the pointwise wave units by \(a_o\sqrt M\int ds/d\), whose dimension is \(G_o L^{1/2}\); C* multiplies ζ units by \(G_o L^{-1/2}\). The transport integral multiplies the wave square by \(d\xi\,ds\,d\ell\), with dimension \(TL^2\). These yield the displayed stock dimension matching H_RX. Old \(\beta_R\), whose RX dimension is \(T^2/L\), has a different role and is not identified with \(\beta_G\). E04 checks the exponent balances, including the witness time bound used in R7. No SI energy, speed or receiver calibration is selected. T03 is verified as stated.

## R4. T04: global forward mild well-posedness in the product energy space

We prove the new theorem directly for every initial state in
\(\mathbb R^6\times U\times\mathbb R^2\times\mathcal W\times Y\).
Here a mild solution means the carrier/native/old-receiver Duhamel equation, the Hilbert-space receiving ODE, and the transport characteristic formulas (R2.1)-(R2.2), with boundary laws holding in locally L2 time spaces. The norm whose square is twice (R3.4) is equivalent to the ordinary product norm at fixed positive weights. The argument uses no initial Sobolev boundary trace or corner compatibility.

### R4.1 Causal construction on time slabs

Choose \(0<h\le\theta_-\). On \([0,h]\), b,c are given by initial profiles in (R2.3) except at irrelevant endpoints. On \([nh,(n+1)h]\), whenever \(t\ge\theta_X(s)\), the delayed argument obeys \(t-\theta_X(s)\le nh\). Therefore b,c on that slab are known from the initial profiles or from previously constructed a,d. Formula (R2.4), also applied to time subintervals, gives \(b,c\in L^2([nh,(n+1)h];V)\). No current outgoing value is needed to determine current incoming data on a set of positive measure; equality at a slab endpoint changes no L2 class.

### R4.2 Local forced RX solution and separate receiving ODE

On a slab let r=nh and let b,c be this known data. The free carrier group \(S_c(t)\) is unitary on U: in \((p\pm r_c)/\sqrt2\) coordinates it is periodic translation by opposite speeds. It is strongly continuous by the isometry bound and density of trigonometric polynomials. Put \(\mathscr S(t)=\operatorname{diag}(I,S_c(t),I)\) on the RX product space.

The retained inequalities \(|f(x)|\le\|K\||x|^2/2\), \(\|J_f(x)\|\le\|K\||x|\), and \(|\mathcal B^*p|\le\|\mathcal B\|\|p\|\) show that the RX vector field plus \(-\kappa^2Q\) is bounded and locally Lipschitz on each bounded product ball. Denote it by \(N_\kappa\). The integral equation is

\[
X(t)=\mathscr S(t-r)X(r)+\int_r^t\mathscr S(t-v)
\{N_\kappa(X(v))+(0,\sqrt2\kappa J^*b(v),0)\}\,dv,\quad X=(x,Q,z). \tag{R4.1}
\]

The forcing is L2 and thus L1 on each finite slab. On a sufficiently short subinterval its L1 norm is small. The usual contraction on a closed ball in \(C([r,r+\varepsilon];\mathbb R^6\times U\times\mathbb R^2)\) follows by choosing \(\varepsilon\) small enough for the bounded vector-field term to remain in the ball and its Lipschitz constant times \(\varepsilon\) to be less than one. This proves local existence and uniqueness before any conservation claim.

Independently, \(-CC^*/\beta_G\) is a bounded nonpositive self-adjoint generator on Y, so its exponential is a contraction. The formula

\[
\zeta(t)=e^{-(t-r)CC^*/\beta_G}\zeta(r)
+\frac{\sqrt2}{\beta_G}\int_r^t e^{-(t-v)CC^*/\beta_G}Cc(v)\,dv \tag{R4.2}
\]

gives the unique receiving solution for the known c. It is continuous and locally absolutely continuous (indeed H1 in time on finite slabs) because the input is L2 and the generator is bounded. It stays finite on the whole slab without invoking total conservation.

### R4.3 Legitimate work for the mild carrier and noncircular continuation

For a local solution of (R4.1), set \(v(t)=S_c(-(t-r))Q(t)\). Duhamel's formula makes v absolutely continuous in U, with derivative
\(S_c(-(t-r))[(\mathcal Bq(t),0)-\kappa^2Q(t)+\sqrt2\kappa J^*b(t)]\) a.e. The Hilbert-space chain rule and unitarity therefore give the carrier norm derivative by pairing Q with that bracket. No derivative \(A_cQ\) is required for L2 data. The native and old-receiver coordinates have continuous right-hand sides, because x,Q,z are continuous and the ports are bounded; hence x,z are C1 and their ordinary chain rules apply. Original RX cancellation plus (R3.3) now yields, on every local subinterval of the slab,

\[
H_{\rm RX}(t)-H_{\rm RX}(r)
=\frac12\int_r^t(\|b(v)\|_V^2-\|a(v)\|_V^2)dv
\le\frac12\int_r^t\|b(v)\|_V^2dv. \tag{R4.3}
\]

The right side is known and finite. Since H_RX controls every component of X, the solution cannot become unbounded before the slab endpoint. More explicitly, on this bounded ball \(N_\kappa(X)\) is bounded and the added forcing is L1. Thus the full interaction variable \(\mathscr S(-(t-r))X(t)\) has an integrable derivative and a limit at a putative finite maximal endpoint. Strong continuity of the group gives a limit of X itself. Restarting the local integral construction from that limit contradicts maximality. This extends X through the entire slab using (R4.3), **without** first assuming total conservation or extra carrier H1 regularity.

Now \(a=\sqrt2\kappa JQ-b\) and \(d=\sqrt2C^*\zeta-c\) are L2 on the slab. R2 constructs the transport state from these inflows and proves its continuity and energy identity. The receiving chain rule applied to (R4.2) gives the second identity in (R3.3) a.e. Summing the already-established component identities proves (R3.4) for all slab times. The next slab has the required known incoming traces, so induction gives every finite forward interval.

The conserved energy controls \(|x|,\|Q\|,|z|,\|(u_+,u_-)\|\) and \(\|\zeta\|\) uniformly in exchange time for this fixed preparation; their squared weights are exactly those in (R3.4). This is a state-energy bound, not a pointwise boundary-trace bound. Adjacent slab solutions join continuously. The x,z right-hand sides also join continuously, giving C1 regularity throughout exchange time. ζ is locally absolutely continuous across the finite number of joins on each finite horizon, while a,b,c,d remain only locally L2 in time in general.

### R4.4 Uniqueness and finite-horizon dependence

Uniqueness follows by induction: identical initial data give identical first incoming traces, unique solutions of (R4.1)-(R4.2), and hence identical outgoing histories and transport states; the same statement then applies to every next slab.

For dependence, take two initial states in a common bounded energy ball and fix H<infinity. Their conserved energies keep both solutions in a common bounded state ball, giving a finite Lipschitz constant for \(N_\kappa\). On one slab, Duhamel and the unitary bound give
\(\|\Delta X\|_{C}\le K_h(\|\Delta X(r)\|+\sqrt h\|\Delta b\|_{L^2})\).
Formula (R4.2) gives
\(\|\Delta\zeta\|_C\le\|\Delta\zeta(r)\|+\sqrt{2h}\|C\|\|\Delta c\|_{L^2}/\beta_G\).
The boundary laws then bound outgoing differences by these suprema and the incoming L2 differences. From (R2.4), incoming differences are bounded by the initial-profile differences plus previously constructed outgoing-history differences. Finally, the characteristic energy identity for differences gives

\[
\sup_{t\le H}\|\Delta(u_+,u_-)(t)\|_{\mathcal W}^2
\le\|\Delta(u_{+,0},u_{-,0})\|_{\mathcal W}^2
+\int_0^H(\|\Delta a\|_V^2+\|\Delta d\|_V^2)dt. \tag{R4.4}
\]

There are finitely many slabs for fixed H and positive \(\theta_-\). Induction therefore gives a finite constant depending on the initial energy bound, fixed parameters and H, controlling the product-state C norm and boundary L2 norms by the initial product-energy difference. In particular the required continuous dependence holds (locally Lipschitz on these bounded sets). No uniform assertion is made as \(\theta_-\downarrow0\), as parameters become unbounded, or across native singular prestages. This is a forward mild theorem, not a backward-flow or global H1 theorem. T04 is verified as stated.

## R5. T05: exact C6 direct term with explicit return and startup data

For nonnegative-time boundary histories define
\((D_\theta^+h)(s,X,t)=\mathbf1_{t\ge\theta_X(s)}h(s,X,t-\theta_X(s))\).
Let
\(c_{\rm init}(s,X,t)=\mathbf1_{0\le t<\theta_X(s)}u_{+,0}(s,X,\theta_X(s)-t)\).
This is an L2 time signal by R2. Substituting the actual near boundary law into the exact forward characteristic gives

\[
c=\sqrt2\kappa D_\theta^+JQ-D_\theta^+b+c_{\rm init}.
\]

Apply C and use the far ODE, obtaining an identity in locally L2 time with values in Y:

\[
\boxed{\beta_G\dot\zeta
=2\kappa\mathcal K_{G,0}Q-\sqrt2CD_\theta^+b
+\sqrt2C c_{\rm init}-CC^*\zeta,\quad
\mathcal K_{G,0}=CD_\theta^+J.} \tag{R5.1}
\]

The startup term has a **plus** sign. The two factors \(\sqrt2\) give the coefficient 2κ on the direct C6 term. Here \(\mathcal K_{G,0}\) evaluates C6 on a specified zero extension of Q for the purpose of this decomposition. It does not claim that an arbitrary initial transport profile arose from zero past forcing, or from any past RX trajectory. The missing past carried by independent forward profiles is precisely why the startup term is present.

For the separate complete-history statement, suppose the necessary negative-time histories are supplied, the near law \(a+b=\sqrt2\kappa JQ\) holds there as well as forward in time, and
\(u_{+,0}(s,X,\xi)=a(s,X,-\xi)\) a.e. on \(\mathcal D\).
For t<θ the startup expression is then \(a(s,X,t-\theta_X(s))\); for t≥θ it is the same expression from the boundary. Thus c=Dθa and

\[
\boxed{\beta_G\dot\zeta
=2\kappa\mathcal K_GQ-\sqrt2CD_\theta b-CC^*\zeta.} \tag{R5.2}
\]

Suitable L2 histories on the required finite interval make these pairings well-defined. Compatibility of Q alone is insufficient: the negative-time near relation and initial forward profile also involve b and a. Conversely, arbitrary initial profiles allowed by R4 need not admit a past generated by the full model. No backward-existence theorem is used. For t≥θ-plus the startup contribution in (R5.1) vanishes a.e., and every delayed argument displayed there is nonnegative, so the corresponding form no longer needs negative-time data.

Both formulas are causal. C* in the far law is a same-time spatial adjoint, whereas the accepted W adjoint \(\mathcal K_G^*\) is an adjoint over a temporal observation window and generally samples future test values. The latter is not the force here. C6 is retained as an exact direct component of the actual Q history; ζ and its entire loaded drive are not generally equal to bare C6. The backward contribution and, for arbitrary preparation, the initial forward profile remain explicit. Nonnegative \(E_{\rm tr}(0)\) is a quadratic preparation of the new states, not W's signed bilinear prehistory pairing renamed as a positive stock. T05 is verified as stated.

## R6. T06: native hybrid, true decoupling and clarification D01

### R6.1 Original native map and finite-window balance

Retain precisely the source tuple

\[
\epsilon=1/10,\quad g=1/60,\quad \lambda_N=1/300,\quad
k=(999/1000,1,1001/1000).
\]

For \(\Omega\in\mathbb C^3\), form the simultaneous prestage
\(\widetilde\Omega_i=\Omega_i+\epsilon(k_i-|\Omega_i|^2)\Omega_i+g\sum_{j\ne i}(\Omega_j-\Omega_i)\).
Then set
\(\delta_i=\lambda_N\sum_{j\ne i}\sin(3[\operatorname{Arg}_0\widetilde\Omega_j-\operatorname{Arg}_0\widetilde\Omega_i])\),
\(F_{{\rm native},i}=e^{i\delta_i}\widetilde\Omega_i\), with \(\operatorname{Arg}_0(0)=0\). Every kick uses the prescribed shared old/prestage state. Exact zero prestage components remain zero. This is the old map, not a continuous gradient or a changed synchronization law.

At each jump apply it only to x, leaving Q,z,u-plus,u-minus,ζ unchanged. The storage change is therefore exactly
\(\alpha_N[I(F_{\rm native}\Omega^-)-I(\Omega^-)]/2\).
Exchange afterwards obeys (R3.4). For post-jump endpoints, telescoping over finitely many jumps gives

\[
\boxed{H_{\rm total}(t_b)-H_{\rm total}(t_a)
=\sum_{t_a<t_j\le t_b}\frac{\alpha_N}{2}
\{I(F_{\rm native}\Omega(t_j^-))-I(\Omega(t_j^-))\}=B_N.} \tag{R6.1}
\]

A jump at the left endpoint is already included in its post-jump value and is excluded from the sum; one at the right endpoint is included. No new state impulse or port impulse is inserted. F-first and then an exchange stage of the fixed positive symbolic dwell is the retained order.

For a finite native state the prestage polynomial is finite, the stipulated phase convention is defined and the rotation has modulus one. Thus every native image is finite even at a zero prestage. R4 then supplies the next whole exchange interval with finite energy. Induction proves every finite hybrid iterate. It supplies no uniform infinite-step bound and no continuity through singular native prestages. The native baseline term is not automatically external physical energy or a compensating reservoir.

### R6.2 Exact zero coupling and the wording issue

At κ=0, \(\mathcal F=0\) for every b, and the entire old x,Q,z subsystem is exactly RX, even when the added states are prepared nonzero. The isolated added subsystem has a=-b and continues to satisfy its transport/far equations. At the near interface \(P_N=0\), so its own \(E_{\rm tr}+H_G\) is conserved. It may evolve from its prepared stock. If all its initial states are zero, uniqueness makes them remain zero. This is exactly the conditional statement in analytical-start section 8.

**D01: work-order clarification, not a changed candidate.** The T06 instruction says, “Zero new activity also requires empty new states.” If read as a necessary condition for inactivity, this is false. The correct statement is: **κ=0 alone does not guarantee that the added subsystem is inactive; empty added states are sufficient for inactivity, but not necessary.**

A concrete counterexample uses the very vector kernel retained in T01. Take κ=0, u-plus,0=u-minus,0=0, and \(\zeta_0(X)=(0,h(X)n)\ne0\) with n perpendicular to the carrier plane and nonzero \(h\in L^2(G)\). Then \(C^*\zeta_0=0\), \(CC^*\zeta_0=0\). The solution has a=b=c=d=0, both waves zero, and \(\zeta(t)=\zeta_0\). Its receiving stock is positive and constant, while all added interface work and time evolution vanish. The old RX solution can be arbitrary and decoupled. E01 corroborates the pointwise kernel. This refutes necessity without modifying any boundary law or preparation allowed by the candidate.

The mathematical T06 claim in the analytical start and input claim ledger is already correct; the clarification applies only to the work-order phrasing. Its disposition is therefore **verified-as-stated**, with D01 separately recorded as a documentary/interpretive correction. For κ>0, the added force changes Q and therefore the coupled trajectory. Unchanged algebraic forms of the native and old-z equations do not transfer old capacity, credit, convergence or receiving theorems without checking their hypotheses and invariants afresh.

## R7. T07: latency, strict receiving and delayed incoming return

### R7.1 Empty new states and the exact latency statements

Assume \(u_{+,0}=u_{-,0}=0\) and \(\zeta_0=0\), with arbitrary finite RX preparation. For \(0\le t<\theta_-\), (R2.3) gives c=0 a.e. and (R4.2) gives ζ=0. Hence d=0 there. For t<2θ-minus, b is either its zero initial-profile part or d evaluated at \(t-\theta_X(s)<\theta_-\), which is zero. Thus

\[
H_G(t)=0\quad(0\le t\le\theta_-),\qquad
b(t)=0\text{ a.e. on }[0,2\theta_-). \tag{R7.1}
\]

The inclusion of the receiving endpoint follows from ζ's continuity; no boundary value at the exact onset is asserted. The incoming force \(\sqrt2\kappa J^*b\) is delayed in this sense. The other added term \(-\kappa^2Q\) acts immediately to launch the forward waves. The account does not claim that every preparation produces a nonzero wave exactly at either delay threshold.

### R7.2 Temporary carrier regularity for the stated preload

Now take κ>0 and the exact preparation
\(x_0=0,z_0=0,Q_0(s)=(P,0)\), P>0, with all added states empty. Since f(0)=0 and \(J_f(0)=0\), uniqueness keeps x=0; no native funding or native credit occurs in this witness. Old z continues to obey its retained equation; it is not clamped to zero.

Before 2θ-minus the carrier has no incoming b. The remaining force is \(-\kappa^2Q\), and \(\mathcal Bq(t)\) is continuous into H1 because the finite tents are H1 and q is continuous. The carrier formula
\(Q(t)=e^{-\kappa^2t}S_c(t)Q_0+\int_0^t e^{-\kappa^2(t-v)}S_c(t-v)(\mathcal Bq(v),0)dv\)
therefore belongs to \(C_tH^1_{\rm per}\) on every closed subinterval before 2θ-minus. The periodic one-dimensional embedding into C0 proves that some ε>0 can be chosen with

\[
0<\varepsilon<\theta_-,\quad
p(s,u)>P/2,\quad |Q(s,u)|\le2P
\quad(s\in S,\ 0\le u\le\varepsilon). \tag{R7.2}
\]

This uses continuity at the constant initial state, not an H1 consequence of the energy bound. The line profiles need not satisfy a corner compatibility condition: zero initial forward profile and a nonzero launch at time zero are allowed by R4. No later global carrier/line H1 conclusion is inferred.

### R7.3 Scalar receiving is strictly positive on a nonempty interval

On \(\theta_-<t<\theta_-+\varepsilon<2\theta_-\), each arrived sample uses \(0\le t-\theta_X(s)<\varepsilon\). The near input at that sampled time has b=0, so \(c=\sqrt2\kappa\mathbf1_{t\ge\theta}JQ(t-\theta)\). The block diagonal Gram formula decouples the scalar receiving equation from its vector block:

\[
\beta_G\partial_t\zeta_{\rm sc}(X,t)+m_0(X)\zeta_{\rm sc}(X,t)
=2\kappa a_o\int_{\theta_X(s)\le t}\frac{p(s,t-\theta_X(s))}{d_X(s)}ds\ge0. \tag{R7.3}
\]

Its scalar integrating-factor formula, starting from zero, proves nonnegativity on this early interval. For strict positivity at an arbitrary fixed \(t\in(\theta_-,\theta_-+\varepsilon)\), choose \(\theta_-<r<t\). A minimizing pair for θ exists. Continuity provides a relative product neighborhood with \(\theta<r\); if its G point is a tip or elbow, move into an adjacent segment interior while keeping the strict inequality. Shrink to a circle interval I and an interior G interval J of positive arclength with \(\sup_{I\times J}\theta<r\). Thus for every \(X\in J\) and \(v\in[r,t]\), the contribution of I to the right side of (R7.3) is at least \(\kappa a_o P|I|/(c_e\theta_+)\). Its scalar solution satisfies

\[
\zeta_{\rm sc}(X,t)\ge
\frac{\kappa a_oP|I|}{\beta_Gc_e\theta_+}
\int_r^t e^{-m_0(X)(t-v)/\beta_G}dv>0\quad\text{for a.e. }X\in J. \tag{R7.4}
\]

These intervals exist for every t strictly above the minimum, without differentiating the delay or assuming an interior minimizer. Positive arclength of J gives

\[
\boxed{H_G(t)>0\quad\text{for every }\theta_-<t<\theta_-+\varepsilon.} \tag{R7.5}
\]

The mild receiving state is continuous in Y, so this all-times stock statement is meaningful despite only a.e. boundary traces. Conservation gives \(0\le H_G(t)\le H_{\rm total}(0)=LP^2/2\). This is receiving funded by declared carrier preload. It proves neither a capacity fraction nor native empty-launch receiving/recovery, and does not assert equal or simultaneous receiving at all six G labels.

### R7.4 Uniform estimate and a strictly nonzero incoming-return trace

The early expression for c and (R7.2), together with \(|A_sQ|=|Q|\), imply

\[
\|Cc(v)\|_{L^\infty(G)}\le\frac{2\sqrt2\kappa a_oPL}{\delta_w}
\quad(\theta_-\le v\le\theta_-+\varepsilon). \tag{R7.6}
\]

The pointwise Gram matrix B(X) is nonnegative, so its finite-dimensional exponential is a Euclidean contraction for positive times. With zero initial ζ and no receiving input before θ-minus, the pointwise form of (R4.2) gives the useful representative and bound

\[
\|\zeta(v)\|_{L^\infty(G)}
\le\frac{4\kappa a_oPL}{\beta_G\delta_w}(v-\theta_-). \tag{R7.7}
\]

This stronger bound is particular to the bounded early forcing of this witness, not an L-infinity theorem for arbitrary energy preparations. Shrink ε, preserving (R7.2), to satisfy

\[
\varepsilon<\frac{\beta_G\delta_w^2}{16a_o^2ML}. \tag{R7.8}
\]

For \(2\theta_-<t<2\theta_-+\varepsilon\) and a channel with \(\theta=\theta_X(s)<t/2\), put v=t-θ and u=t-2θ. Then
\(\theta_-<v<\theta_-+\varepsilon\) and \(0<u<\varepsilon\).
The scalar forward arrival at v is
\(c_p(s,X,v)=\sqrt2\kappa p(s,u)/\sqrt M>\kappa P/\sqrt{2M}\).
Meanwhile (R7.7) and the scalar component of C* give

\[
|\sqrt2(C^*\zeta(v))_p(s,X)|
\le\frac{4\sqrt2\kappa a_o^2P\sqrt M L}{\beta_G\delta_w^2}\varepsilon
<\frac{\kappa P}{2\sqrt{2M}}. \tag{R7.9}
\]

Consequently the backward characteristic and far boundary law give

\[
\boxed{b_p(s,X,t)=d_p(s,X,t-\theta)
<-\frac{\kappa P}{2\sqrt{2M}}<0
\quad\text{on }\{\theta_X(s)<t/2\}.} \tag{R7.10}
\]

The constant 16 in (R7.8) is exact: at equality its effort bound is half the direct lower bound. E05 checks this ratio symbolically. The same relative-neighborhood argument used in R7.3 makes the sublevel set in (R7.10) have positive product measure whenever t>2θ-minus, including endpoint/elbow minima. Therefore \(\|b(t)\|_V>0\) for a.e. t in the stated interval. For the characteristic representative defined by the bounded early Q and pointwise receiving formula, the sublevel inequality can be taken at every such t; the energy-space conclusion does not rely on that representative at a single onset time.

Nonzero b is not the assertion \(J^*b\ne0\), positive net carrier work, native credit or recovery. Spatial averaging/projection and the simultaneous launching term remain in the force. No ambient return path has been constructed. T07 is verified as stated for the declared preload and sufficiently small interval.

## R8. Dispositions, evidence and remaining physical correspondence

| Claim | Independent disposition | Proof | Executed corroboration |
| --- | --- | --- | --- |
| T01 | verified-as-stated | R1 | E01 normalization, tangent/Gram blocks and kernel. |
| T02 | verified-as-stated | R2 | E03 both characteristic orientations and startup energy algebra. |
| T03 | verified-as-stated | R3, justified for mild solutions in R4 | E02 port signs/cancellation; E04 unit exponents. |
| T04 | verified-as-stated | R4 | Written Hilbert-space proof; no finite-dimensional test is substituted. |
| T05 | verified-as-stated | R5 | E01 direct coefficient; written characteristic substitution supplies startup/history claims. |
| T06 | verified-as-stated | R6 | E01 corroborates D01's nullspace witness; D01 corrects only the work-order necessity wording. |
| T07 | verified-as-stated | R7 | E05 exact return constant; positivity, regularity and measure arguments are written proofs. |

No submitted candidate equation or analytic theorem is changed. D01 distinguishes sufficiency from necessity in the work order's inactivity wording; its counterexample is within the candidate, not an alternative model. The complete mathematical contribution is a forward causal extension with nonnegative declared state stocks and matched work, a qualified exact C6 direct component, and a carrier-preload receiving/return witness. The original W finite-window adjoint and signed prehistory result remain true for their different operator and domain.

All hypotheses that do work in the proof remain visible: one fixed positive-width static geometry; finite positive upper/lower delay bounds; finite bounded spatial maps and retained finite-width profiles; κ≥0 and β_G>0; finite-energy preparation; and, only for the activity witness, the stated constant positive carrier preload, zero native/old-receiver preparation and empty new states. Reflection and common scaling are already in the accepted geometry; no new all-parameter uniform regularity or zero-delay theorem is asserted. Ball radius, cylindrical radius, old carrier arclength and the channel's time coordinate are distinct. Q01, phase-information, cadence, singular-prestage, capacity and receiving/recovery qualifications remain at their accepted scopes.

The proof uses straight endpoint distance only as inherited delay data. A physical rectifiable path joining those endpoints has length at least their Euclidean distance; a nontrivial detour at the same constant speed would change the delay. Hence these abstract channels do not by themselves trace the intended central/outward/curved-return circuit. Their product measure can contain multiplicity in (s,X), and any physical embedding must justify overlap, material density, interface location, dual units and the relation of route length to travel time. G remains a collection of actual broken arcs, not a newly filled aperture; old z, new ζ, the carrier, tight toroid, close ball and outer arrangements remain distinct. Local exchange and a larger return/elsewhere circuit remain compatible aims.

The measured execution environment was Command Prompt with conda `torment`, Python 3.11.15 and existing SymPy 1.14.0. `run_python.cmd checks\run_checks.py` executed the new input validator and five new exact-algebra groups, both subprocesses exiting 0. `logs/EXECUTION_RECORD.json` retains actual commands, timestamps, outputs and statuses; `logs/EXACT_CHECKS.json` limits their corroborating scope. No dependency was installed. `CLAIM_LEDGER.json` maps every claim to this proof and current source locators. The complete review is returned for GPT/author assessment. Manuscript drafting, physical attachment decisions and publication remain later work; this task changes no native kernel or repository publication.
