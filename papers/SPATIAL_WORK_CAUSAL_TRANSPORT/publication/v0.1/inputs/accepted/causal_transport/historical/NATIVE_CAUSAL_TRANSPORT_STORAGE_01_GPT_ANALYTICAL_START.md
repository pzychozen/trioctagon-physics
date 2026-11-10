# A causal transport and storage candidate for the C6 observation

**Task:** `NATIVE_CAUSAL_TRANSPORT_STORAGE_01`  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Status:** Proposed mathematical extension and GPT analytical start. T01–T07 require independent Codex review. No new physical model, material receiver or curved route is adopted.

## 1. Purpose and the exact design decision

Accepted W01–W05 establish C6 as a causal history observation on the actual G arcs, identify the generally advanced finite-window adjoint, and give the signed prehistory residual for formal negative-adjoint forcing. They do not rule out a causal extension with its own state and work account. [W]

This study proposes one such extension. It adds two oppositely traveling signals, a positive transport stock, and a G-indexed receiving field with a quadratic stock. The retained native and old receiver equations remain unchanged; an explicitly specified additional force couples the original carrier to the new transport state. The new receiving field is not the old receiver z relocated to G.

The design uses **effort/flow boundary relations**, not the retarded operator's Hilbert adjoint as a time-feedback rule. The same-time spatial operator C is paired with C*, while the delay is realized by actual state evolution. No future load value is used. Wave-variable energy accounting for delayed interactions is established methodology; the reference [NS] provides that context, not a proof or selection of this Tri-Octagon candidate. All specific formulas and claims below are derived directly.

| Inherited input | Newly proposed in this candidate |
| --- | --- |
| RX native x, carrier Q=(p,r_c), old receiver z, profiles B/B*, parameters, trial stocks and native F jumps. | A continuum of delay states indexed by (s,X), with two propagation senses. |
| Static G arcs, common width, selected carrier, arclength tangent, distances and positive bounded C6 delays. | An isometric source duplication J and spatial mixing C with the stated mathematical product measure. |
| C6 gain g_o and observation speed parameter c_e. | Near-interface strength kappa>=0, new receiving weight beta_G>0, boundary relations, and receiving field zeta. |
| Accepted observation and work restrictions W01–W05. | The additional carrier force and positive transport/receiving stocks, to be tested under their own assumptions. |

The mathematical product measure and these added stocks are constitutive choices for this candidate. They are not physical energy densities inherited from C6. The internal coordinate below measures delay time; it is not an ambient spatial path. A separate physical correspondence would have to justify its attachment to the intended central/outward/return construction. [GEO]

## 2. Fixed setting and proposed claims

Fix one admitted static geometry, common width w>0 and hand. Let S=R/LZ be the selected carrier parameterized by physical arclength, and let G be the disjoint labeled union of all six actual broken arcs with ordinary arclength measure d ell. Put M=measure(G)>0. Preserve

\[
d_X(s)=|X-\gamma_w(s)|,\quad \theta_X(s)=d_X(s)/c_e,
\quad 0<\theta_-:=\min_{s,X}\theta_X(s)
\le\theta_X(s)\le\theta_+:=\max_{s,X}\theta_X(s)<\infty.
\tag{N1}
\]

Accepted W01 supplies a sufficient upper history horizon and W's accepted separation supplies a positive lower bound. The actual extrema in (N1) exist by compactness. They need not be optimized or explicitly evaluated for the proof. All parameters and geometry are constant during each assertion. [W R1–R3]

Use real Hilbert spaces

\[
U=L^2(S;\mathbb R^2),\quad V=L^2(S\times G;\mathbb R^2),\quad
Y=L^2(G;\mathbb R^4),\quad a_o=g_o/(4\pi),
\]

with unweighted mathematical arclength measures. Write A_s(p,r_c)=(p,r_c t_hat(s)); then A_s^*A_s=I_2. Ambient vector coordinates are fixed throughout. If an observation frame is later used, its orthogonal transformation and adjoint must both be carried through.

| Claim | Proposed result |
| --- | --- |
| T01 | Bounded spatial duplication/mixing, exact C6 factorization and explicit C C*. |
| T02 | Causal transport characteristics, admissible time traces and an exact nonnegative transport-storage balance. |
| T03 | Closed RX/transport/receiving candidate with exact exchange-only total conservation. |
| T04 | Unique global forward mild solution in the full energy space, with boundary signals locally L2 in time. |
| T05 | Exact C6 direct component, with return and startup terms retained under the correct history conditions. |
| T06 | Original native hybrid increment and finite-step existence; exact decoupling at kappa=0. |
| T07 | Positive receiving delay and delayed return for empty new states, plus strict receiving and incoming-return witnesses from declared carrier preload. |

No claim is made here about a completed curved physical circuit, irreversible disposal, a capacity-sized amount, native recovery through the new connection, all-six simultaneous receiving, or a calibrated clock.

## 3. T01 — spatial factorization without a contraction assumption

Define

\[
(JQ)(s,X)=\frac{Q(s)}{\sqrt M},\qquad
(J^*v)(s)=\frac1{\sqrt M}\int_G v(s,X)d\ell_X,
\tag{N2}
\]

and

\[
(Cv)(X)=a_o\sqrt M\int_S\frac{A_s v(s,X)}{d_X(s)}ds,
\qquad
(C^*\zeta)(s,X)=\frac{a_o\sqrt M}{d_X(s)}A_s^*\zeta(X).
\tag{N3}
\]

Then J*J=I_U, ||J||=1, and

\[
\|C\|\le a_o\sqrt{LM}/\delta_w,
\qquad \delta_w=297w/5000.
\tag{N4}
\]

**Proof.** Integrating |Q|^2/M over G proves the isometry. Fubini proves both displayed adjoints. Cauchy–Schwarz in s, |A_s v|=|v| and d>=delta_w give (N4). These operators are static; C* is not the temporal adjoint of the delayed observation.

For a complete history define (D_theta h)(s,X,t)=h(s,X,t-theta_X(s)). The original ambient C6 map has the exact factorization

\[
\mathcal K_GQ=C D_\theta JQ.
\tag{N5}
\]

No state or energy conclusion follows from this factorization alone. It is an identity of the existing observation formula.

The spatial Gram operator is pointwise in X:

\[
(CC^*\zeta)(X)=a_o^2M\int_S\frac1{d_X(s)^2}
\begin{pmatrix}1&0\\0&\hat t(s)\hat t(s)^T\end{pmatrix}ds\,\zeta(X).
\tag{N6}
\]

It is bounded and nonnegative. Its scalar block is

\[
m_0(X)=a_o^2M\int_S d_X(s)^{-2}ds>0.
\]

The vector block can have a kernel: for the planar selected carrier, the direction perpendicular to its plane is not generated by the tangent encoding. No positive-definiteness or inverse of CC* is assumed. The proposed energy proof works for every bounded C; it imposes no requirement ||C||<=1. This is because C/C* are used in power-conjugate effort/flow relations, not asserted to be a unit-power scattering transfer.

## 4. T02 — explicit delay state and its exact work

For each pair (s,X) introduce an internal coordinate 0<xi<theta_X(s), and two real two-component states u_+,u_-. Let

\[
\mathcal D=\{(s,X,\xi):s\in S,X\in G,0<\xi<\theta_X(s)\},
\quad \mathcal W=L^2(\mathcal D;\mathbb R^2)\oplus L^2(\mathcal D;\mathbb R^2).
\]

The proposed equations are

\[
\partial_tu_++\partial_\xi u_+=0,\qquad
\partial_tu_--\partial_\xi u_-=0.
\tag{N7}
\]

Define the near and far boundary signals, interpreted as locally L2 time traces,

\[
a=u_+(0),\quad b=u_-(0),\qquad
c=u_+(\theta),\quad d=u_-(\theta).
\]

Here a travels from the carrier side toward the new receiving side, and d travels in the reverse sense. These are directions in the abstract channel, not upper/lower G flow signs or an ambient toroidal route.

The symbols a,b,c,d in this candidate denote boundary signals only. They are not the real/imaginary native vectors used in some RX source formulas. The retained carrier speed is written c_car below to distinguish it from the far signal c; its value is unchanged.

For initial profiles u_{+,0},u_{-,0}, characteristics give, almost everywhere,

\[
u_+(s,X,\xi,t)=
\begin{cases}u_{+,0}(s,X,\xi-t),&t<\xi,\\a(s,X,t-\xi),&t\ge\xi,\end{cases}
\]
\[
u_-(s,X,\xi,t)=
\begin{cases}u_{-,0}(s,X,\xi+t),&t<\theta_X(s)-\xi,\\
d(s,X,t-\theta_X(s)+\xi),&t\ge\theta_X(s)-\xi.
\end{cases}
\tag{N8}
\]

In particular,

\[
c=\mathbf1_{t<\theta}u_{+,0}(s,X,\theta-t)+\mathbf1_{t\ge\theta}a(s,X,t-\theta),
\]
\[
b=\mathbf1_{t<\theta}u_{-,0}(s,X,t)+\mathbf1_{t\ge\theta}d(s,X,t-\theta).
\tag{N9}
\]

These formulas use only initial profiles and earlier boundary values. A single arbitrary L2 profile need not have a pointwise boundary value, but integration over time in (N9), followed by the substitution xi=t or xi=theta-t, gives an L2 time trace bounded by the profile norm. The delayed boundary terms similarly have L2 time bounds by translation. Thus representative independence and the trace interpretation are justified; a fixed-time Sobolev trace is not being assumed.

The new nonnegative transport stock is

\[
E_{\rm tr}(t)=\frac12\int_{S\times G}\int_0^{\theta_X(s)}
(|u_+|^2+|u_-|^2)d\xi\,ds\,d\ell_X.
\tag{N10}
\]

Define

\[
P_N=\frac12(\|a\|_V^2-\|b\|_V^2),\qquad
P_G=\frac12(\|c\|_V^2-\|d\|_V^2).
\]

For finite-energy initial profiles and locally L2 incoming boundaries, direct substitution into (N8) and Fubini give

\[
E_{\rm tr}(T)-E_{\rm tr}(0)=\int_0^T(P_N-P_G)dt.
\tag{N11}
\]

For smooth states this is integration by parts in xi. For arbitrary L2 states the characteristic formula gives the same integrated identity and a continuous energy-space evolution. The time coordinate has unit propagation speed by definition; no physical speed in an ambient path has thereby been chosen.

## 5. T03 — the proposed closed interconnection

Retain the RX equations for x and z, source q and old stocks:

\[
q=\eta_N f(x)-\eta_Rz,\quad y=\mathcal B^*p,\quad
\dot x=-\frac{\eta_N}{2\alpha_N}J_f(x)^Ty,\quad
\dot z=\frac{\eta_R}{\beta_R}y,
\]
\[
H_{\rm RX}=\frac{\alpha_N}2|x|^2+\frac12\|Q\|_U^2+\frac{\beta_R}2|z|^2.
\]

Write the original free carrier generator as A_c(p,r_c)=(-c_car(r_c)_s,-c_car p_s), with the retained c_car>0. Its periodic translation group is unitary. Choose new constants kappa>=0 and beta_G>0, and a new field zeta in Y. The candidate equations are

\[
\boxed{
\begin{aligned}
\dot Q&=A_cQ+(\mathcal Bq,0)+\mathcal F,\\
\mathcal F&=-\kappa^2J^*JQ+\sqrt2\kappa J^*b
=-\kappa^2Q+\sqrt2\kappa J^*b,\\
a&=\sqrt2\kappa JQ-b,\\
d&=\sqrt2C^*\zeta-c,\\
\beta_G\dot\zeta&=\sqrt2Cc-CC^*\zeta.
\end{aligned}}
\tag{N12}
\]

Together with (N7) and the unchanged x,z equations, these specify the entire exchange-stage candidate. All incoming signals b,c are supplied causally by (N9).

The near effort and flow are e_N=(a+b)/sqrt(2)=kappa JQ and f_N=(a-b)/sqrt(2). Thus F=-kappa J*f_N. At the far boundary e_G=(c+d)/sqrt(2)=C*zeta and f_G=(c-d)/sqrt(2), so beta_G zeta_dot=C f_G. The identity <e,f>=(||incoming||^2-||outgoing||^2)/2 fixes the power signs at each end.

Define the new receiving stock H_G=beta_G||zeta||_Y^2/2 and H_total=H_RX+E_tr+H_G. Then

\[
\dot H_{\rm RX}=\langle Q,\mathcal F\rangle_U=-P_N,
\qquad \dot H_G=\langle C^*\zeta,\sqrt2c-C^*\zeta\rangle_V=P_G.
\tag{N13}
\]

Indeed, expanding ||sqrt(2)kappa JQ-b||^2 gives the first identity. Expanding ||sqrt(2)C*zeta-c||^2 gives the second. The original native and z powers cancel inside H_RX exactly as in accepted RX/W05. Combining (N11) and (N13) proves

\[
\boxed{H_{\rm total}(T)=H_{\rm total}(0)}
\tag{N14}
\]

on exchange-only intervals at the regularity proved in T04. The apparent damping terms in (N12) transfer energy to traveling states; no unrecorded dissipative sink is introduced.

H_G is not generally monotone. For empty lines and a preparation zeta_0 with C*zeta_0 nonzero, c=0 initially and H_G'(0+)=-||C*zeta_0||^2<0. The new store can return work into the backward signal. No irreversible-disposal claim is made.

### Abstract units and new normalization

This is a normalized mathematical interconnection. Its coefficients carry the units needed to compare the trial stocks; no SI calibration is asserted. One consistent bookkeeping assignment takes [Q]=U, [s]=[ell]=L, [xi]=T and [g_o]=G_o. Then [kappa]=T^(-1/2), [a,b,c,d]=U/(L T)^(1/2), [zeta]=U/(G_o T^(1/2)) and [beta_G]=G_o^2 T. Equations (N10) and H_G both have units U^2 L, matching H_RX, and F has units U/T. A numerical value for kappa or beta_G is not selected. These choices, including the new receiving metric, are proposed constitutive bookkeeping rather than inherited physical data.

## 6. T04 — global forward energy-space well-posedness

**Proposed theorem.** For fixed setting (N1), retained RX parameters, kappa>=0 and beta_G>0, every initial state

\[
(x_0,Q_0,z_0,u_{+,0},u_{-,0},\zeta_0)
\in\mathbb R^6\times U\times\mathbb R^2\times\mathcal W\times Y
\]

has a unique global forward mild solution. Its state is continuous in this product energy space, x,z are C1, zeta is locally absolutely continuous, a,b,c,d are locally L2 in time, and (N14) holds. No global H1 regularity of the line profiles or pointwise-in-time boundary trace is claimed.

**Proof by steps.** Choose h with 0<h<=theta_-. On the first interval, (N9) determines b,c from the initial profiles alone. On any subsequent interval [nh,(n+1)h], every delayed boundary argument t-theta is <=nh (up to null endpoints). Thus b,c are known from the already constructed solution and any remaining initial-profile part. Time translation/Fubini give b,c in L2 of the current interval with values in V.

With b known, the x,Q,z subsystem is RX plus bounded linear damping -kappa^2Q and known additive L2 forcing sqrt(2)kappa J*b. The original polynomial nonlinearity is locally Lipschitz on R6 x U x R2 because the retained profile averages are bounded. The unitary carrier group and a local integral-equation argument therefore yield a unique local mild solution for this L1-in-time forcing on the finite interval. The new zeta equation is a bounded linear ODE on Y with L2 input Cc, so it also has a unique absolutely continuous solution.

To justify energy without assuming carrier differentiability, use the interaction variable v(t)=exp(-t A_c)Q(t). Its Duhamel formula is absolutely continuous on every interval where the solution exists. Differentiating its squared norm gives the carrier work identity almost everywhere; the native/z coordinates satisfy their ordinary chain rules. Hence

\[
H_{\rm RX}(t)-H_{\rm RX}(nh)
=\frac12\int_{nh}^t(\|b\|_V^2-\|a\|_V^2)du
\le\frac12\int_{nh}^t\|b\|_V^2du.
\tag{N15}
\]

This bounds all x,Q,z norms on the interval before any putative finite blowup. The known b forcing has finite integral, so local solutions extend to the end of the step. The zeta solution remains finite as a bounded-generator ODE. Equations (N12) give outgoing a,d in L2, allowing the next step. The characteristic transport solution (N8) is continuous in W and satisfies (N11). Induction constructs every finite interval.

Combining the established component identities yields (N14), which gives a global energy bound on x,Q,z,zeta and the transport state. Uniqueness follows stepwise from the local subsystem uniqueness and the fixed characteristic data. Standard integral estimates on each finite set of steps also give continuous dependence on the initial energy-space state, with constants depending on the bounded energy set, fixed parameters and observation horizon. No uniform estimate as theta_- tends to zero or over unbounded parameter sets is asserted.

The argument proves the claimed energy-space theorem directly; it does not invoke the original RX theorem as if it already covered this added feedback. Compatibility of line profiles with boundary values is unnecessary for a mild solution. A later strong-solution theorem would require its own preparation compatibility and regularity analysis.

## 7. T05 — what remains exactly C6 under loading

There are two different history statements.

### 7.1 Arbitrary initial line profiles

For histories known only for t>=0 define the zero-extended delay D_theta^+ by

\[
(D_\theta^+h)(s,X,t)=\mathbf1_{t\ge\theta_X(s)}h(s,X,t-\theta_X(s)),
\]

and define c_init(s,X,t)=1_{0<=t<theta_X(s)}u_{+,0}(s,X,theta_X(s)-t). Then (N9) and (N12) give exactly

\[
c=\sqrt2\kappa D_\theta^+JQ-D_\theta^+b+c_{\rm init},
\]
\[
\boxed{\beta_G\dot\zeta
=2\kappa\mathcal K_{G,0}Q-\sqrt2 C D_\theta^+b
\,+\sqrt2C c_{\rm init}-CC^*\zeta,\qquad
\mathcal K_{G,0}=CD_\theta^+J.}
\tag{N16}
\]

K_{G,0} is C6 evaluated with the specified zero extension for this algebraic decomposition. Defining that decomposition does not assert that an arbitrary physical past was zero. The initial forward profile contributes the separate startup term. Independent initial profiles do not automatically determine or coincide with a complete past RX trajectory.

### 7.2 Compatible complete boundary histories

If initial forward profiles are compatible with a complete launched history, u_{+,0}(s,X,xi)=a(s,X,-xi), and the relation a+b=sqrt(2)kappa JQ also holds on the needed negative times, then c=D_theta a and

\[
\boxed{\beta_G\dot\zeta
=2\kappa\mathcal K_GQ-\sqrt2 C D_\theta b-CC^*\zeta.}
\tag{N17}
\]

The compatibility hypothesis must be stated; it is not inferred from a supplied Q history alone. After t>=theta_+, (N16) also has no startup term and all displayed delayed arguments are nonnegative.

Thus C6 is retained exactly as an observation of the actual Q history and as the direct component in the receiving equation. Under loading, the total received drive additionally contains a delayed return contribution, and possibly startup data. It is not generally equal to C6 alone. All of these terms are causal; none is K_G*, the finite-window adjoint proved in W03.

E_tr(0) is a nonnegative preparation of the new state. It is not identified with W's signed bilinear W_pre, and no cancellation of that term is achieved by relabeling it a stock. This candidate earns its work account from the local evolution and boundary identities.

## 8. T06 — native updates and the decoupled limit

At each native jump apply exactly F_native to x and leave Q,z,u_+,u_-,zeta unchanged. Retain the existing F-first/exchange-second order and symbolic positive dwell. Since the new exchange is global, every finite native/exchange iterate is well defined for finite initial energy. For post-jump endpoints on [t_a,t_b] count t_a<t_j<=t_b; then

\[
\boxed{H_{\rm total}(t_b)-H_{\rm total}(t_a)
=\sum_{t_a<t_j\le t_b}\frac{\alpha_N}{2}
\big[I(F_{\rm native}\Omega(t_j^-))-I(\Omega(t_j^-))\big]=B_N.}
\tag{N18}
\]

Only native storage changes at each jump; (N14) applies between jumps. This does not supply an infinite-step bound, coherent-domain invariance, old exchange-only capacity conservation across jumps, or later recovery after F updates. Those questions retain their existing status. [RX hybrid/accounts; CAD]

At kappa=0, F=0 and a=-b. The original RX subsystem is exactly decoupled from the new subsystem even for prepared transport/receiving states, since its added force vanishes. The new subsystem can still exchange its own prepared energy. If its states start empty, they remain empty. This is a parameter limit of the proposed extension, not a change to the original RX parameters.

For kappa>0 the additional carrier force changes the coupled trajectories. Keeping the native and old z equations in the same form does not automatically transfer their previously proved receiving, credit, capacity or convergence theorems to this extension, even during exchange-only evolution. Reuse of any such theorem requires checking its actual hypotheses and invariants.

## 9. T07 — latency and an actual receiving witness

### 9.1 Empty new states impose genuine delay

Take u_{+,0}=u_{-,0}=0 and zeta_0=0, while allowing a finite RX preparation. For 0<=t<theta_-, c=0 from characteristics. The receiving ODE and zero initial zeta give zeta=0 and d=0 there. Hence

\[
H_G(t)=0\quad(0\le t\le\theta_-),\qquad
b(t)=0\ \text{a.e. for }0\le t<2\theta_-.
\tag{N19}
\]

The second statement follows because every backward arrival uses d(t-theta), and that argument is <theta_- until time 2theta_-. It concerns the incoming return contribution sqrt(2)kappa J*b. The direct launching term -kappa^2Q starts immediately and is not delayed. No exact nonzero first-arrival assertion for arbitrary preparations is made.

### 9.2 A strict positive example from declared carrier stock

Fix kappa>0 and prepare

\[
x_0=0,\quad z_0=0,\quad Q_0(s)=(P,0),\quad P>0,
\quad u_{+,0}=u_{-,0}=0,\quad\zeta_0=0.
\tag{N20}
\]

This is a carrier-preload example. It is not native supply from an empty carrier, capacity-sized receiving or native recovery. The original receiver z remains active according to its unchanged law.

Before 2theta_-, b=0. The carrier equation is original RX with bounded damping -kappa^2Q. Its H1 preparation and retained H1 tent forcing give Q continuous in H1 on this initial interval. One-dimensional embedding therefore supplies epsilon with

\[
0<\epsilon<\theta_-,\qquad p(s,u)>P/2
\quad\text{for all }s\text{ and }0\le u\le\epsilon.
\tag{N21}
\]

This temporary carrier regularity does not assert globally H1-compatible line data. Empty lines with a nonzero launch boundary have a corner mismatch; the full system is the mild-energy solution supplied by T04.

For theta_-<t<theta_-+epsilon<2theta_-, all arrived forward samples have ages 0<=t-theta_X(s)<epsilon. The scalar part of the receiving equation is

\[
\beta_G\partial_t\zeta_{\rm sc}(X,t)+m_0(X)\zeta_{\rm sc}(X,t)
=2\kappa a_o\int_{\theta_X(s)\le t}
\frac{p(s,t-\theta_X(s))}{d_X(s)}ds\ge0.
\tag{N22}
\]

For each t>theta_-, strict sublevels of the continuous delay have positive product measure near a minimizing pair, including nearby segment interiors if the minimum is at a tip or elbow. Taking an intermediate time between theta_- and t gives a positive forcing set of X values over a nonzero time interval. The scalar integrating-factor formula, with m_0(X)>0 and zero initial receiving field, implies

\[
\boxed{H_G(t)>0\qquad\text{for }\theta_-<t<\theta_-+\epsilon.}
\tag{N23}
\]

This proves nontrivial receiving somewhere in the G-indexed field after the positive delay; it does not establish equal receiving at all six labels or a physical G aperture flux. Conservation also gives 0<=H_G(t)<=H_total(0), without an optimized fraction or transfer time. The new stock's increase is balanced by the other modeled stocks, rather than inferred from the observation magnitude.

### 9.3 A nonzero incoming return for the same preparation

Shrink epsilon so that also |Q(s,u)|<=2P for 0<=u<=epsilon. On theta_-<=v<=theta_-+epsilon, the explicit early-arrival formula gives

\[
\|Cc(v)\|_{L^\infty_X}\le\frac{2\sqrt2\kappa a_oPL}{\delta_w},
\qquad
\|\zeta(v)\|_{L^\infty_X}
\le\frac{4\kappa a_oPL}{\beta_G\delta_w}(v-\theta_-).
\]

The second estimate uses the pointwise nonnegative matrix in (N6), whose exponential is a contraction. Thus the far effort contribution sqrt(2)C*zeta is uniformly small just after first arrival. Choose additionally

\[
\epsilon<\frac{\beta_G\delta_w^2}{16a_o^2ML}.
\]

For 2theta_-<t<2theta_-+epsilon and each channel with theta_X(s)<t/2, the direct scalar arrival at time t-theta_X(s) is at least kappa P/sqrt(2M), while the far effort term is less than half that value. Characteristics therefore give

\[
b_p(s,X,t)=d_p(s,X,t-\theta_X(s))
<-\frac{\kappa P}{2\sqrt{2M}}<0.
\tag{N24}
\]

The delay sublevel set has positive product measure, so ||b(t)||_V>0 for almost every t in that interval (and for the explicit characteristic representative at every such t). This supplies a nontrivial delayed incoming wave for the same preparation. It does not assert that its projection J*b cannot cancel, that the net carrier work becomes positive, or that native credit/recovery has occurred. Those are distinct accounts. The statement concerns the proposed delay-bank return, not a demonstrated physical toroidal path.

## 10. Geometric meaning, review boundary and proposed paper plan

The construction supplies an abstract causal connection and positive state storage if T01–T07 survive review. Its delay labels use the inherited endpoint distance d/c_e. They do not trace the intended outward–around–inward spatial curve. A physical rectifiable route of length ell_route joining the same endpoints has ell_route>=d; at constant speed c_e a genuine detour would take ell_route/c_e rather than d/c_e. A new route or speed relation would therefore be an additional correspondence, not a consequence of the delay-bank proof. [GEO]

G remains six actual broken arcs. No aperture closures, normals, thickness, selected rim points or physical receiver positions have been supplied. The field zeta is a newly proposed mathematical receiving state indexed by G, and the line bundle can have multiple (s,X) labels that would require an account of overlap if physically embedded. The old z, carrier, central toroid and close/outer spheres remain distinct.

Codex should independently establish, correct or reject all seven claims. Particular attention is needed for the infinite-dimensional trace and method-of-steps proof, initial-profile terms, the difference between direct C6 and loaded drive, the mild receiving witness, and the limitation to finite native-step existence. Internal GPT checks are preparation, not independent acceptance.

The current editorial decision is to combine accepted W01–W05 with the reviewed findings of this candidate in the next paper. A failed or restricted candidate must be reported honestly; the paper plan does not predetermine a positive result. Manuscript drafting follows independent candidate review. Publication remains a later step.

### References and retained sources

- **W:** `accepted/spatial_work/` — accepted W01–W05 proof, GPT review and acceptance record; complete acceptance archive also supplied.
- **RX:** `sources/RX/candidate.tex`, `power.tex`, `wellposed.tex`, `hybrid.tex`, `accounts.tex` — exact original subsystem, trial stocks, source regularity and jump conventions.
- **CC:** `sources/CC/carrier.tex`, `geometry.tex` — inherited C6 and static carrier/G definitions.
- **CAD:** retained cadence records under `accepted/cadence/`.
- **GEO:** `context/GEOMETRY_MODEL_BOUNDARY.md` and preserved author geometry.
- **NS:** G. Niemeyer and J.-J. E. Slotine, *Stable adaptive teleoperation*, IEEE Journal of Oceanic Engineering 16(1), 152–162 (1991), DOI [10.1109/48.64895](https://doi.org/10.1109/48.64895), [publisher record](https://ieeexplore.ieee.org/document/64895/). Cited for established wave-variable/passivity methodology only. Its publisher abstract was consulted; it is not used as a black-box theorem for (N12), and no claim of novelty is made for the general delay-line energy method.
