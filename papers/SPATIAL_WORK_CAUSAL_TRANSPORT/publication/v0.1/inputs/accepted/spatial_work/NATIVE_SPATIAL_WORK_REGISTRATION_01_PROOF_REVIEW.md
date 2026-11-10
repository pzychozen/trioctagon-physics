# C6 spatial observation and work compatibility: independent proof review

**Task:** NATIVE_SPATIAL_WORK_REGISTRATION_01  
**Reviewer:** Codex  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Disposition:** W01-W05 verified as stated, at the submitted assumptions. No mathematical correction is required. This is the independent Codex review returned for GPT/author assessment, not an already-issued acceptance by them.

The inherited C6 formula defines a bounded causal observation of the complete carrier history on the six actual G arcs. Its finite-window Hilbert adjoint includes prehistory and, when the window exceeds the minimum delay, has an advanced forward-time part. With the original reciprocal exchange retained, formal loading by the negative adjoint leaves exactly the prehistory pairing in the integrated balance. These statements establish an observation/work compatibility assessment, not an additional physical receiving or transport mechanism.

## R0. Sources, notation and verification scope

All paths below are relative to this review's directory in the complete return ZIP. The original packet and its 52 members are preserved unchanged; the 51 manifest entries and all 37 source identities match. `INPUT_IDENTITIES.json` supplies SHA-256, sizes and Git-blob comparisons where the supplied registry contains them. `SOURCE_LOCATORS.json` resolves the labels/headings used here to actual retained file lines and hashes. The earlier source reading checkpoints are retained in `inputs/SOURCE_IDENTITIES.json`; they are not relabeled with the later publication commit. No fresh publication audit is part of this review.

| Key | Preserved source | Definition or accepted qualification used |
| --- | --- | --- |
| CC-G | [CC geometry](inputs/sources/CC/geometry.tex) | `eq:constants`, `eq:directions`, `eq:vertices`, `eq:G`, `eq:circleconstants`, `eq:circle`; actual arcs, reflection and selected circle. |
| CC-C | [CC carrier](inputs/sources/CC/carrier.tex) | `eq:C1`, `eq:storage`, `eq:C6` and exterior subsection; history observation and unloaded status. |
| PG | [PG geometry](inputs/sources/PG/geometry.tex) | `prop:balls`; source enclosing-ball constant, independently checked below against G vertices. |
| RX-C | [RX candidate](inputs/sources/RX/candidate.tex) | `eq:drive`, `eq:tents`, `eq:ports`, `eq:storages`, `eq:system`; fixed drive, ports, native/receiver equations and stores. |
| RX-P | [RX power](inputs/sources/RX/power.tex) | `eq:jacobian`, `eq:localwork`, `eq:balances`; source Euler identity and reciprocal cancellation. |
| RX-A | [RX accounts](inputs/sources/RX/accounts.tex) | `eq:baselinewindow`, `eq:windowbalances` and preceding endpoint convention. |
| RX-H | [RX hybrid](inputs/sources/RX/hybrid.tex) | `eq:tuple`, `eq:nativemap`, `eq:hybrid`, `eq:hybridbalance`; unchanged native map and F-first order. |
| SO | [Accepted six-opening proof](inputs/accepted/six_opening/NATIVE_SIX_OPENING_TRANSPORT_CORRESPONDENCE_01_PROOF_REVIEW.md), [acceptance](inputs/accepted/six_opening/GPT_ACCEPTANCE.json) | V17-V18 and S04: accepted common-width clearance, empty crossing preimages and unloaded C6. The separation proof is an input, not rerun here. |
| CR | [Accepted central-route review](inputs/accepted/central_route/NATIVE_CENTRAL_ROUTE_CORRESPONDENCE_01_GPT_REVIEW.md), [proof](inputs/accepted/central_route/NATIVE_CENTRAL_ROUTE_CORRESPONDENCE_01_PROOF_REVIEW.md) | Q01 in review section 5; C05's conditional common-phase information result. |
| CAD | [Accepted cadence limits](inputs/accepted/cadence/CORRECTIONS_AND_LIMITS.md), [status](inputs/accepted/cadence/CADENCE_STATUS.md) | Finite-step/cadence and capacity qualifications remain unchanged. |
| CTX | [Continuation](inputs/context/CONTINUATION_STATUS.md), [geometry intention](inputs/context/COLLABORATION_AND_GEOMETRY.md) | Static supports, central meeting region, outward/curved-return intention, possible elsewhere-transfer and local verification scope. |

The objects under review are the submitted analytical start's equations (1)-(19). Its `preparation/` notes are retained as preparation, not used as independent acceptance evidence. The proofs below derive the relevant results from the source definitions. Four new exact-algebra groups A01-A04 corroborate specific identities; they do not replace the functional-analytic or all-parameter arguments.

Write \(\tau_g\in[0,h_g]\) for a **static normalized geometry parameter**, \(w>0\) for the common host width, \(s\) for physical carrier arclength, and \(t,u\) for time. The carrier field \(r_c\) is neither a geometric radius nor a native component. \(R_0\) is a ball radius; cylindrical radius, when needed, means \(\rho_\perp(X)=\sqrt{(X_1-O_1)^2+(X_2-O_2)^2}\). The profile operator is \(\mathcal B\); the observation frame is \(E\); neither is the central lower vertex \(B_i\). The native discrete map is \(F_{\rm native}\), distinct from a hypothetical force pair \(\mathcal F=(F_p,F_r)\). Use \(\theta_X(s)\) for observation delay, not native common phase.

The geometry and delays are stationary throughout each assertion. The accepted SO input is

\[
d_X(s)=|X-\gamma_w(s)|>\delta_w:=\frac{297}{5000}w
\quad\text{on every actual G arc, all admitted }\tau_g\text{ and both hands}. \tag{R0.1}
\]

No filled aperture or physical flux measure is inferred. The observation measure is ordinary Euclidean arclength summed over the **disjoint labeled union** of the six broken arcs. Shared endpoints have zero arclength measure.

## R1. W01: actual arcs, ball bound, arclength and history horizon

### R1.1 Exact geometry and endpoints

At width one, measured relative to the common center O, set

\[
r_g=\frac{\sqrt3}{6},\quad d_g=1-\frac{\sqrt2}{2},\quad
a_g=\frac{d_g}{2},\quad h_g=\frac{\sqrt2-1}{2},\quad H_0=\frac12=h_g+d_g.
\]

Let \(e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3))\), with ring indices modulo six, and \(J(x,y)=(-y,x)\). Then

\[
A_\tau=I-(\tau_g/r_g)J,\quad
A_\tau^TA_\tau=(1+\tau_g^2/r_g^2)I=:D^2I,
\quad D^2\le D_*^2=10-6\sqrt2. \tag{R1.1}
\]

The source vertices are

\[
T_i=(a_ge_i,h_g),\ B_i=(a_gA_\tau e_i,-h_g),\quad
U_k=(r_ge_{2k},H_0),\ L_k=(r_gA_\tau e_{2k},-H_0).
\]

For k=0,1,2 the actual sets are

\[
G_k^+=[U_k,T_{2k+1}]\cup[T_{2k+1},U_{k+1}],\quad
G_k^-=[L_k,B_{2k+1}]\cup[B_{2k+1},L_{k+1}],\quad U_3=U_0,\ L_3=L_0. \tag{R1.2}
\]

These are joined segments, not directed flow paths. The last upper segment is \([T_5,U_0]\), and the last lower segment is \([B_5,L_0]\). In both, the adjacent horizontal directions have dot product \(1/2\), just as in the other ten segments. There is no added tip-to-tip chord. Multiply all centered coordinates by w and then translate by O. MINUS applies \(S=\operatorname{diag}(-1,1,1)\) to that entire centered construction with labels retained.

### R1.2 Enclosing ball and sufficient maximum delay

The exact identities

\[
r_g^2+h_g^2+H_0^2=\frac{13}{12}-\frac{\sqrt2}{2}=R_0^2,
\quad r_g^2-a_g^2=\frac{6\sqrt2-7}{24}>0 \tag{R1.3}
\]

follow by expansion. The last strict inequality is exact because both compared terms are positive and \((6\sqrt2)^2=72>49=7^2\). Also \(0<h_g<H_0\). For any lower tip,

\[
|L_k|^2=D^2r_g^2+H_0^2=r_g^2+\tau_g^2+H_0^2\le R_0^2,
\quad R_0^2-|L_k|^2=h_g^2-\tau_g^2. \tag{R1.4}
\]

This bound is attained at \(\tau_g=h_g\). A lower elbow is strictly smaller in norm than a lower tip because their squared-norm difference is
\(D^2(r_g^2-a_g^2)+(H_0^2-h_g^2)>0\).
The corresponding upper statement follows with D=1; upper tips have squared norm \(r_g^2+H_0^2\le R_0^2\). For a segment between endpoints P,Q in the ball,
\(|(1-v)P+vQ|\le(1-v)|P|+v|Q|\le R_0\), \(0\le v\le1\).
Thus every point of every actual arc lies in \(|X-O|\le wR_0\). This bounds the full three-dimensional norm, including height; it is not a cylindrical-radius calculation.

For the single selected carrier define

\[
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\quad
a_c=\frac{K_c}{1+\sqrt3/2},\quad R_\Gamma=\frac{\sqrt7}{2}a_c,\quad L=2\pi wR_\Gamma,
\]
\[
\gamma_w(s)=O+wK_c u+wR_\Gamma(\cos\chi\,u+\sin\chi\,e_z),
\quad \chi=s/(wR_\Gamma),\quad u=(0,1,0).
\]

Differentiation gives \(\hat t=-\sin\chi\,u+\cos\chi\,e_z\), of unit norm. Thus s really is arclength. The carrier satisfies \(|\gamma_w-O|\le w(K_c+R_\Gamma)\), so the triangle inequality gives

\[
d_X(s)\le D_w:=w(K_c+R_\Gamma+R_0),\qquad
T_{\rm hist}:=D_w/c_e. \tag{R1.5}
\]

Consequently every input time required for observations on \([0,T]\) lies in \([-T_{\rm hist},T]\). The endpoint equality in (R1.4) does **not** assert that all inequalities used for (R1.5) can be equalities simultaneously. The history horizon is sufficient, not optimized.

### R1.3 Total labeled length, common scale and reflection

For adjacent directions \(e_i\cdot e_{i+1}=1/2\), the horizontal squared edge length is

\[
v_0^2=r_g^2+a_g^2-a_gr_g
=(r_g-a_g/2)^2+3a_g^2/4>0. \tag{R1.6}
\]

An upper segment has squared length \(v_0^2+d_g^2\). Applying \(A_\tau\) to the horizontal difference gives squared length \(D^2v_0^2+d_g^2\) for a lower segment: the vertical difference remains \(d_g\). There are six upper and six lower segments, including both wraparound segments. Their lengths add, since within each broken arc the two noncollinear segments share only their elbow. Hence

\[
M_w(\tau_g)=6w\left[\sqrt{v_0^2+d_g^2}+\sqrt{D^2v_0^2+d_g^2}\right]
\le M_{w,*}:=6w\left[\sqrt{v_0^2+d_g^2}+\sqrt{D_*^2v_0^2+d_g^2}\right]. \tag{R1.7}
\]

The right lower-edge length is increasing in \(\tau_g^2\), since \(v_0^2>0\). Thus the maximum occurs at \(h_g\); at zero the result is twelve identical segment lengths. Scaling the entire lower three-dimensional edge by D would be wrong: it would also change \(d_g^2\).

Because \(S^TS=I\), full reflection preserves every distance, segment length and unit tangent norm, and preserves the delay/length bounds with the same labels. Width scaling is common to the carrier, central geometry and arclength; an independently moved or scaled carrier is outside this assertion. A01 checks the radical/margin identities and A02 explicitly checks all twelve symbolic edge lengths, their reflected lengths and the tangent. W01 is verified as stated.

## R2. W02: bounded history operator, causality and point records

Fix one static configuration, \(g_o,c_e>0\), and \(0<T<\infty\). Put \(a_o=g_o/(4\pi)\), \(I=[-T_{\rm hist},T]\), \(\theta_X(s)=d_X(s)/c_e\), and

\[
\mathcal H=L^2((\mathbb R/L\mathbb Z)\times I;\mathbb R^2),\quad
\mathcal Y=\bigoplus_{k,\sigma}L^2(G_{k,w}^{\sigma}\times[0,T];\mathbb R^4).
\]

Use the measures ds du and dℓ dt. In ambient coordinates let \(A_s(p,r_c)=(p,r_c\hat t(s))\). Then \(A_s^TA_s=I_2\), since \(|\hat t|=1\), and C6 is

\[
(\mathcal K_G Q)(X,t)=a_o\int_0^L\frac{A_sQ(s,t-\theta_X(s))}{d_X(s)}\,ds. \tag{R2.1}
\]

### R2.1 Space-time estimate and representative independence

Initially take smooth Q. Vector Cauchy-Schwarz, the isometry of \(A_s\) and (R0.1) give

\[
|\mathcal K_G Q(X,t)|^2\le\frac{a_o^2L}{\delta_w^2}
\int_0^L|Q(s,t-\theta_X(s))|^2ds. \tag{R2.2}
\]

For fixed s and X, set \(u=t-\theta_X(s)\). Its derivative with respect to t is one; its integration interval \([-\theta_X(s),T-\theta_X(s)]\) lies in I. Tonelli therefore yields

\[
\|\mathcal K_G Q\|_{\mathcal Y}^2
\le\frac{a_o^2L}{\delta_w^2}\int_{\mathcal G_w}\int_0^L
\int_{-\theta_X(s)}^{T-\theta_X(s)}|Q(s,u)|^2du\,ds\,d\ell_X
\le\frac{a_o^2LM_w}{\delta_w^2}\|Q\|_{\mathcal H}^2. \tag{R2.3}
\]

In particular the triple pullback integral is finite for any measurable L2 representative. Applying the same estimate to a difference that vanishes a.e. in \((s,u)\) makes that triple integral zero. Fubini then makes the s integral independent of representatives for a.e. \((X,t)\). This is the requisite representative argument; a single curve through a null set would not suffice. Smooth periodic functions restricted to I are dense in \(\mathcal H\), so the smooth formula has a unique bounded extension, agreeing with this a.e. integral. The asserted constant is exactly the stated **upper bound**

\[
\|\mathcal K_G\|\le a_o\sqrt{LM_w}/\delta_w\le a_o\sqrt{LM_{w,*}}/\delta_w. \tag{R2.4}
\]

It is not claimed to equal the optimal operator norm. No extra factor \(\sqrt2\) arises from the two input components because \(A_s\) is an isometry. No \(\sqrt T\) arises: the time integral is already part of the input norm.

Only earlier input times occur, with delay at least \(\delta_w/c_e>0\). Thus histories equal a.e. through a cutoff time give equal outputs a.e. through that cutoff (within the declared domains). This is observation causality, not a feedback law. Writing \(L=wL_1\), \(M_{w,*}=wM_{1,*}\), \(\delta_w=w\delta_1\) shows the uniform bound equals \(a_o\sqrt{L_1M_{1,*}}/\delta_1\), independent of w at fixed gain. The sufficient history length still scales as \(w/c_e\). These are norms on the corresponding physical measure spaces, not a clock or speed calibration.

### R2.2 Continuous records under the stronger hypothesis

The one-dimensional periodic embedding \(H^1\hookrightarrow C^0\) is continuous for fixed L. If \(Q\in C(I;H^1_{\rm per})\), then time continuity in H1 implies uniform-in-s continuity in time, and each spatial representative is continuous. The triangle inequality between \(Q(s,u)\), \(Q(s,u_0)\), and \(Q(s_0,u_0)\) proves joint continuity. On the compact carrier/history domain that representative is bounded and uniformly continuous. Positive clearance and continuity of \(d_X(s),\hat t(s)\) now give continuity of (R2.1) on every labeled arc times \([0,T]\), by uniform continuity or dominated convergence. The statement remains true at elbows and endpoints with the arc topology. All negative-time values needed by (R2.1) must be supplied; prescribing Q(0) alone supplies none of that prehistory.

### R2.3 A point evaluation is unbounded in the history L2 norm

Fix \(X_0\) on an actual arc and \(0<t_0<T\). The periodic function
\(u_0(s)=t_0-\theta_{X_0}(s)\) is smooth because the distance is strictly positive. It lies strictly inside I: its lower endpoint margin is at least \(t_0>0\), and its upper endpoint margin is at least \(T-t_0+\theta_{\min}>0\). Choose nonzero smooth periodic \(v\ge0\), and \(\psi\in C_c^\infty((-1,1))\) with \(\psi(0)>0\). For sufficiently small ε set

\[
Q_\epsilon(s,u)=\left(\epsilon^{-1/2}v(s)\psi((u-u_0(s))/\epsilon),0\right).
\]

For every s the whole bump lies inside I. Substitution in the u integral gives exactly
\(\|Q_\epsilon\|_{\mathcal H}^2=\|v\|_2^2\|\psi\|_2^2\), independent of ε. But

\[
U_\epsilon(X_0,t_0)=a_o\epsilon^{-1/2}\psi(0)
\int_0^L\frac{v(s)}{d_{X_0}(s)}ds\longrightarrow+\infty. \tag{R2.5}
\]

The integral is strictly positive. Each input is smooth, so this is already a counterexample on the dense smooth class to any bounded point-evaluation functional in the \(\mathcal H\) norm. It does not refute the continuous-record theorem, which assumes a stronger topology. W02 is verified as stated; no single-time trace estimate is substituted for (R2.3).

## R3. W03: finite-window adjoint and its advanced part

Let \(\lambda=(\lambda_0,\lambda_v)\in\mathcal Y\), with \(\lambda_v\in\mathbb R^3\), and extend it by zero outside \([0,T]\), writing \(\widetilde\lambda\). The proposed adjoint is

\[
(\mathcal K_G^*\lambda)(s,u)=a_o\sum_{k,\sigma}\int_{G_{k,w}^\sigma}
\frac{\big(\widetilde\lambda_0(X,u+\theta_X(s)),\,
\hat t(s)\cdot\widetilde\lambda_v(X,u+\theta_X(s))\big)}{d_X(s)}d\ell_X,
\quad u\in I. \tag{R3.1}
\]

### R3.1 Derivation and a.e. validity

Insert (R2.1) into \(\langle\lambda,\mathcal K_GQ\rangle_{\mathcal Y}\). The absolute triple integral is bounded by
\((a_o/\delta_w)\sqrt{L}\|\lambda\|_{\mathcal Y}\sqrt{M_w}\|Q\|_{\mathcal H}\): apply Cauchy-Schwarz in \((X,t,s)\) and the same translation estimate as in R2. Thus Fubini is justified for L2 inputs as well as smooth ones. At fixed s,X, translate t to \(u=t-\theta_X(s)\). Transposition gives
\(A_s^T(\lambda_0,\lambda_v)=(\lambda_0,\hat t\cdot\lambda_v)\).
The translated time indicator is precisely \(0\le u+\theta_X(s)\le T\); zero extension in (R3.1) keeps it, and the sufficient history horizon permits the u integral over all I. Therefore

\[
\langle\lambda,\mathcal K_GQ\rangle_{\mathcal Y}
=\langle Q,\mathcal K_G^*\lambda\rangle_{\mathcal H}. \tag{R3.2}
\]

No spatial variable is changed in the time substitution. In particular neither \(\partial_s\theta\), an arclength derivative, nor an additional Jacobian occurs. Direct Cauchy-Schwarz in X gives
\(|\mathcal K_G^*\lambda(s,u)|^2\le a_o^2M_w\delta_w^{-2}\int_{\mathcal G_w}|\widetilde\lambda(X,u+\theta_X(s))|^2d\ell_X\).
Integrating u,s proves the same bound (R2.4) and representative independence for (R3.1). Duality gives the usual exact equality of operator norms \(\|\mathcal K_G^*\|=\|\mathcal K_G\|\); it does not say the upper bound is attained.

For a fixed known orthonormal output frame E, the output is \((U,E^TV)\). The second adjoint component is then \(\hat t\cdot(E\widetilde\lambda_v)\). Leaving E out while using framed test coordinates would be wrong. The present proof consistently uses ambient coordinates, and \(\mathcal B\) never enters this frame transformation.

### R3.2 Support, the short window and a concrete causality witness

Compactness of the circle and finite arcs gives actual extrema \(0<\theta_{\min}\le\theta_X(s)\le\theta_{\max}\le T_{\rm hist}\). In fact \(\theta_{\min}>\delta_w/c_e\) follows from compactness and the strict accepted bound. The adjoint can be supported only in
\([-\theta_{\max},T-\theta_{\min}]\subset I\).
Its negative-time part is essential to (R3.2).

If \(T\le\theta_{\min}\), then for u>0, \(u+\theta_X(s)>T\), so the forward-time restriction vanishes. At equality a possible u=0 endpoint has zero time measure. Thus it is zero a.e. on \([0,T]\). The full adjoint can still be nonzero: choose a positive scalar test around an interior observation time and an arc patch; its translated support lies at negative u in I. This is compatible with a nonzero observation generated entirely by prehistory.

For \(T>\theta_{\min}\), choose a circle point \(s_*\) and an interior point \(X_*\) of some actual segment with \(\theta_*:=\theta_{X_*}(s_*)<T\). Such interior points exist even if a minimizer lies at an elbow or tip: the strict inequality persists in nearby segment interiors. Choose \(0<u_*<T-\theta_*\), and then

\[
0<\epsilon<\min\{u_*/4,\theta_*/8,(T-u_*-\theta_*)/4\}.
\]

Shrink circle/arc neighborhoods so that \(|\theta_X(s)-\theta_*|<\epsilon\). Choose a nonnegative scalar spatial bump on this arc patch, positive on a smaller patch of positive arclength. Choose a time bump positive whenever \(|t-(u_*+\theta_*)|<2\epsilon\), supported where that absolute difference is less than \(3\epsilon\). Its whole support lies in \((u_*,T)\). Let their product be \(\lambda_0\) and set \(\lambda_v=0\).

This test and the zero test agree through time \(u_*\). For s in the smaller circle neighborhood and \(u\in(u_*-\epsilon,u_*)\), the shifted time lies in the positive time bump. Since \(a_o/d_X(s)>0\), the scalar adjoint is strictly positive there. The discrepancy is on a set of positive ds du measure **before** the cutoff, not merely at one representative-dependent point. Hence the nontrivial forward-time restriction is noncausal as an operator from the test history to carrier forcing. Multiplication by minus one does not remove this dependence.

This establishes exactly the proposed qualification. It is not a prohibition on all causal systems with extra propagating state, memory, storage or different ports. Time-integrated Hilbert duality is not same-time physical power matching. W03 is verified as stated.

## R4. W04: an explicit present-state/history witness and its scope

Fix an interior arc point \(X_0\), \(0<t_0<T\), and a circle point \(s_0\). Set \(u_*=t_0-\theta_{X_0}(s_0)\). By (R1.5) and positive delay,
\(-T_{\rm hist}<u_*<t_0\). Choose
\(0<\epsilon<\tfrac12\min\{u_*+T_{\rm hist},t_0-u_*\}\) and the smooth nonnegative bump

\[
\phi(u)=\begin{cases}
\exp\!\left[-1/(1-((u-u_*)/\epsilon)^2)\right],&|u-u_*|<\epsilon,\\
0,&|u-u_*|\ge\epsilon.
\end{cases}
\]

Its support is compactly contained in \((-T_{\rm hist},t_0)\), and \(\phi(u_*)>0\). Define \(Q_0(s,u)=0\) and \(Q_1(s,u)=(\phi(u),0)\). They are smooth, periodic in s, and have identical complete carrier states at \(t_0\), namely zero. Delay continuity makes \(\phi(t_0-\theta_{X_0}(s))>0\) on a circle neighborhood of \(s_0\). Therefore

\[
U_1(X_0,t_0)=a_o\int_0^L\frac{\phi(t_0-\theta_{X_0}(s))}{d_{X_0}(s)}ds>0,
\qquad U_0(X_0,t_0)=0. \tag{R4.1}
\]

R2.2 gives a difference on an observation neighborhood, also of positive arclength-time measure after shrinking inside the segment/window. Both histories lie in the stated analytic domain. Nothing here requires or asserts that they solve C1 or RX. Consequently the counterexample refutes factorization of this unrestricted history observation through the single present carrier value; it does not establish two generated RX solutions with the same state, nonreconstruction from full \((x,p,r_c,z)\), native-map noninvertibility, or an obstruction under a prescribed empty-launch and prehistory protocol. Those are different domains/questions.

The accepted common-phase information result is also separate: it concerns an outlet rule that really distinguishes common-phase-related native states while exchange outputs agree. It is neither needed nor strengthened by (R4.1). W04 is verified as stated.

## R5. W05: conditional added work, native jumps and prehistory residual

### R5.1 Native cancellation and the local added-force identity

Retain exactly the source equations and storages. With constant source matrix K, \(x=(a,b)\), \(f(x)=K(a\times b)\), \(J_f=D_xf\), and \(y=\mathcal B^*p\), write

\[
q=\eta_Nf-\eta_Rz,\quad
\dot x=-\frac{\eta_N}{2\alpha_N}J_f^Ty,\quad
\dot z=\frac{\eta_R}{\beta_R}y,
\]
\[
H_N=\alpha_N|x|^2/2,\quad H_C=\tfrac12\int_0^L(p^2+r_c^2)ds,
\quad H_R=\beta_R|z|^2/2,\quad H_{\rm base}=H_N+H_C+H_R.
\]

Here \(\alpha_N,\beta_R>0\), \(\eta_N,\eta_R\ge0\), and the finite tent profiles and \(\mathcal B,\mathcal B^*\) are the unchanged RX ones. The old z receiver has no specified G placement.

Differentiating the cross product gives
\(D(a\times b)[a,b]=a\times b+a\times b\), hence \(J_fx=2f\). It follows directly that

\[
\dot H_N=-\eta_N f\cdot y,\qquad \dot H_R=\eta_Rz\cdot y. \tag{R5.1}
\]

The one-half in native feedback is necessary for this cancellation; omitting it would double the native debit. For a **conditional** added forcing \(\mathcal F=(F_p,F_r)\), set

\[
p_t+c(r_c)_s=\mathcal Bq+F_p,\qquad (r_c)_t+cp_s=F_r. \tag{R5.2}
\]

Assume a solution with sufficient regularity, for example \(Q\in C_tH^1_{\rm per}\cap C_t^1L^2\) on each exchange interval, with the corresponding native/receiver equations and integrable added work. Multiplication by p and \(r_c\), followed by addition, gives

\[
\partial_t\frac{p^2+r_c^2}{2}+\partial_s(cpr_c)
=p\mathcal Bq+pF_p+r_cF_r. \tag{R5.3}
\]

At this regularity the local statement is distributional: H1 spatial products and the L2 temporal derivative justify the product rules in L1. Periodic integration removes the flux derivative. Adjointness of the original ports, \(\int p\mathcal Bq\,ds=y\cdot q\), gives

\[
\dot H_C=\eta_N f\cdot y-\eta_Rz\cdot y+P_{\rm add},\quad
P_{\rm add}(t)=\int_0^L(pF_p+r_cF_r)ds,
\quad\boxed{\dot H_{\rm base}=P_{\rm add}.} \tag{R5.4}
\]

Both added terms have a plus sign. A03 checks the generic polynomial Euler identity and algebraic cancellation, including both local force terms. This does not prove existence, uniqueness or the stated regularity for an unspecified force law.

### R5.2 Finite hybrid windows

Retain the original native tuple \(\epsilon=1/10\), \(g=1/60\), \(\lambda=1/300\), \(k=(999/1000,1,1001/1000)\), the original zero convention, and F-first/exchange-second stage order. For a finite number of native jumps and no new impulses, carrier and z do not jump. Only native storage changes by

\[
\Delta_jH_N=\frac{\alpha_N}{2}
\left[I(F_{\rm native}\Omega(t_j^-))-I(\Omega(t_j^-))\right].
\]

Use post-jump values at endpoints and define \(\Delta H=H(T^+)-H(0^+)\) if an endpoint is a jump, otherwise its ordinary value. Integrating (R5.4) over the exchange subintervals and telescoping adds exactly the jumps \(0<t_j\le T\):

\[
B_N=\sum_{0<t_j\le T}\Delta_jH_N,\qquad
\boxed{\Delta H_{\rm base}-B_N=\int_0^T P_{\rm add}(t)dt.} \tag{R5.5}
\]

A jump at zero is already reflected in the initial post-jump value and is excluded; a jump at T is included. This is the RX endpoint convention, not a changed sampled-state convention. \(B_N=0\) on an exchange-only window. The native increment is not additional port work or a hidden reservoir. The new conditional forcing calculation leaves the inherited map and finite-step qualifications untouched.

### R5.3 Exact residual for formal negative-adjoint loading

For complete \(Q\in\mathcal H\) and \(\lambda\in\mathcal Y\), define

\[
W^{\rm test}=\langle\lambda,\mathcal K_GQ\rangle_{\mathcal Y},\quad
W_{\rm pre}=\int_{-T_{\rm hist}}^0\int_0^L
Q(s,u)\cdot(\mathcal K_G^*\lambda)(s,u)\,ds\,du.
\]

Both pairings are finite by R2-R3 and Cauchy-Schwarz. Splitting the exact geometry-dependent duality (R3.2) at u=0 gives

\[
W^{\rm test}=W_{\rm pre}+J_{\rm fwd},\qquad
J_{\rm fwd}=\int_0^T\int_0^LQ(s,u)\cdot(\mathcal K_G^*\lambda)(s,u)ds\,du. \tag{R5.6}
\]

Now suppose a solution satisfying R5.1-R5.2 also has the **formal** forcing \(\mathcal F=-\mathcal K_G^*\lambda\) restricted to \([0,T]\). Then \(\int P_{\rm add}=-J_{\rm fwd}\). Substitute into (R5.5) and use (R5.6):

\[
\boxed{\Delta H_{\rm base}+W^{\rm test}-B_N=W_{\rm pre}.} \tag{R5.7}
\]

The prehistory term has a **positive coefficient** on the right. The pairing itself is signed; no nonnegativity theorem is implied. Dropping prehistory generally breaks this identity. Zero Q on negative times is sufficient for its vanishing, not necessary: the adjoint may have disjoint support, or the pairing may vanish by orthogonality or cancellation. The condition for this integrated cancellation is exactly \(W_{\rm pre}=0\).

For \(T\le\theta_{\min}\), R3 gives \(\mathcal F=0\) a.e. forward in time, so \(\Delta H_{\rm base}=B_N\), while (R5.6) says \(W^{\rm test}=W_{\rm pre}\). The latter may be nonzero. Thus the short-window regime is consistent and cannot be discarded as a boundary detail. If in addition prehistory is zero, the observed output is zero a.e. on that short window as well.

An exact simple-delay example independently corroborates signs and window endpoints. For this example alone take \((Kq)(t)=q(t-2)\), \(q(u)=u+3\), and \(\lambda(t)=t+1\) on \([0,T]\), zero elsewhere. Direct polynomial integration gives:

| T | \(W^{\rm test}\) | \(W_{\rm pre}\) | \(J_{\rm fwd}\) | \(\Delta H_{\rm base}-B_N=-J_{\rm fwd}\) |
| --- | --- | --- | --- | --- |
| 1 | 7/3 | 7/3 | 0 | 0 |
| 2 | 26/3 | 26/3 | 0 | 0 |
| 3 | 21 | 26/3 | 37/3 | -37/3 |

In each row the residual is exactly (R5.7). Negating the T=3 load gives \(W_{\rm pre}=-26/3\), illustrating its signed nature. Alternatively \(q(u)=u+1\) with unit load on \([0,3]\) gives nonzero prehistory but \(\int_{-2}^0(u+1)du=0\). A04 executes these exact calculations. They are elementary operator/accounting examples, not actual RX trajectories or a replacement for the geometry-dependent proof (R5.6).

### R5.4 What the account requires, and what it leaves open

The arclength pairing has no automatically supplied physical work units or constitutive meaning for λ. Even if such a meaning is proposed later and \(W_{\rm pre}=0\), R5.7 is integrated duality; it does not turn the advanced operator into causal instantaneous loading. A general L2 adjoint force also need not have the stronger regularity assumed in R5.1. The existence of a sufficiently regular solution with this formal force remains a condition, not a conclusion.

If a later extension declares receiving power \(P_G\) into an additional store, excludes other external powers and intermediate storage, its closed exchange balance requires \(P_{\rm add}=-P_G\). If it explicitly adds a transit store \(E_{\rm tr}\), the necessary balance is

\[
\dot E_{\rm tr}=-P_{\rm add}-P_G. \tag{R5.8}
\]

The old receiver H_R is already included in \(H_{\rm base}\) and is not silently counted again. A residual integral alone proves neither nonnegative \(E_{\rm tr}\), causal dynamics, admissible physical units nor spatial location. Any later dissipation or external power needs its own declared term. W05 is verified as stated, conditional on its regularity and unchanged native/receiver hypotheses.

## R6. Dispositions, retained limits and reproducible evidence

| Claim | Codex disposition | Independent proof | Executed corroboration |
| --- | --- | --- | --- |
| W01 | verified-as-stated | R1.1-R1.3 | A01 exact radical/margin algebra; A02 all twelve symbolic edges and full reflection. |
| W02 | verified-as-stated | R2.1-R2.3 | Written Fubini/density, continuity and narrow-graph argument; no numerical surrogate. |
| W03 | verified-as-stated | R3.1-R3.2 | Written adjoint derivation and positive-measure future-test witness. A04 checks simple-delay window arithmetic only. |
| W04 | verified-as-stated | R4 | Explicit analytic smooth bump, not an evolved solution. |
| W05 | verified-as-stated | R5.1-R5.4 | A03 generic Euler/energy algebra; A04 exact residual examples. |

No source equation, proposed bound or mathematical conclusion needs replacement. The following qualifications are part of these dispositions, not new modeling assumptions: the norm estimate is space-time L2, point records require stronger regularity, the forward adjoint is zero for short windows and generally advanced for longer ones, the W04 witnesses are arbitrary histories, and the prehistory term in R5.7 is signed despite its plus sign.

Accepted C01-C05/Q01 and S01-S05 remain foundations. In particular Q01 permits a positive cut delay inside an inner source-free gap as well as for enclosing cuts; failed containment is not universal absence of delay. The carrier's separation from G does not assign a zero value to an undefined physical aperture flux. Common-phase information limits are conditional on a phase-sensitive target rule, and autonomous-F reconstruction is not automatically coupled/hybrid reconstruction. Accepted native cadence and receiving/capacity results retain their own finite-step, preparation and domain restrictions. Historical missing-feedback language in older C1 passages is superseded by the actual RX reciprocal equations used here.

The actual environment measured for this review was Python 3.11.15 at `C:\Users\Notandi\miniconda3\envs\torment\python.exe`, with existing SymPy 1.14.0. No environment modification was needed. The reproducible entry command is `run_python.cmd checks\run_checks.py`, executed in Command Prompt with conda torment activated. `logs/EXECUTION_RECORD.json` records subprocess commands, actual timestamps and exit statuses; both validation and the four-group algebra script exited 0. `logs/EXACT_CHECKS.json` records symbolic outputs and scope. Supplied preparation checks and prior scientific suites were not counted as new tests.

The remaining spatial-model question is concrete: **what additional spatially registered state and causal loading law connect the carrier to the intended central/return/elsewhere interaction, with a justified work and storage account?** C6 does not select that state, route, material receiver, aperture, speed or physical clock. Local reversible exchange and the larger intended outward-around-inward route remain compatible. This review resolves all five bounded checks without a new geometry choice; it returns local evidence for GPT/author review and performs no manuscript, kernel, commit or publication work.
