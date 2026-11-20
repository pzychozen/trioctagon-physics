# Identifying the proposed store through spatial response and switch-off

GM03 · 20 November 2026 · Mathematical assessment for author and scientific review

## Result and scope

GM01–GM02 imply an exact, parameter-free matched-control prediction:
\[
 \boxed{\ q_{2,\mathrm{exposed}}-F(q_1)
 =2(s_{\rm on}-1)\,[F(q_1)-q_1].\ }\tag{1}
\]
Each exposed body is compared with a fresh neutral copy at **its own reached state** \(q_1\), after the interaction parameter has been set to zero without changing that state or its store. The next native direction is provably nonzero for both magnetic examples, so the prediction is observable in the mathematical state variables.

A failure of (1), after independently establishing the switch, preparation and state registration, would reject this feedback rule even if the mass and magnetic-moment dictionary remained valid. A transverse component of displacement relative to the native update direction would reject its scalar-response form even more directly.

The neutral-angle and neutral-distance predictions also check. They constrain the source interaction but do not uniquely identify the store. Ideal state and geometry observations can identify two coupling-to-storage ratios, not all dimensional source and storage scales. No independent physical measurements are supplied or claimed.

## 1. Premises and notation

The native map \(F\), coefficient tuple, Fourier preparation, mass/moment dictionary, pair potential and storage rule are those of the reviewed GM01–GM02 packages. Keep two identical bodies, \(m_0=0\), common fixed pose \(R=I_3\), positive equal \(S\), and initial \(h=1\). In numerical native amplitude units,
\[
 m=\alpha I,\qquad \boldsymbol\mu=\kappa W,\qquad
 U=-\frac{G_Nm_1m_2}{r}
 +\frac{c_m}{r^3}\boldsymbol\mu_1^T(I_3-3nn^T)\boldsymbol\mu_2,
 \quad c_m=\frac{\mu_0}{4\pi}.
 \tag{2}
\]
Here \(n\) is the unit center-line direction. The added energy and response rule are
\[
\begin{split}
 {\cal E}&=\eta U+\sum_a S h_a^2/2,\\
 d_a&=F(q_a)-q_a,\qquad q_a^+=q_a+s_a d_a,\\
 s_a&=(h_a+h_a^+)/2,\qquad
 h_a^+=h_a-\eta L_a(s)/S,\\
 L_a(s)&=\int_0^1\nabla_{q_a}U(q+\tau D_s)\cdot d_a\,d\tau.
\end{split}\tag{3}
\]
The integral parameter \(\tau\) is not physical time. The native direction is evaluated once at the beginning of the step.

For the preparation \(\Omega_0=(1,\omega,\omega^2)\), \(\omega=e^{-2\pi i/3}\), put \(a=1/10000\), \(t=1/20\). Along the first step's straight segment,
\[
 \Omega(s)=\operatorname{diag}(1-(t+a)s,\ 1-ts,\ 1-(t-a)s)\Omega_0,
\]
\[
 I(s)=3(1-ts)^2+2a^2s^2,\qquad
 W(s)=\left(\frac{\sqrt3}{2}a^2s^2,\frac32as(1-ts),0\right).
 \tag{4}
\]
These are GM02's exact expressions. The initial moment is zero; \(w=W(1)\ne0\) is the unloaded final moment before multiplication by \(\kappa\).

## 2. Neutral spatial response

### 2.1 Every center-line direction is covered

For every unit \(n\), \(Q(n)=I_3-3nn^T\) has eigenvalue \(-2\) along \(n\) and \(+1\) on its orthogonal plane. Hence \(\|Q(n)\|_2=2\). GM02's bounds use only this norm, not the two specially chosen directions.

Consequently its full two-body contraction certificate applies to all \(n\) whenever
\[
 0\le a_{\rm load}=\frac{\eta G_N\alpha^2}{Sr}\le\frac14,\qquad
 0\le b_{\rm load}=\frac{\eta c_m\kappa^2}{Sr^3}\le10^6.
 \tag{5}
\]
The unique solution in \([1/2,3/2]^2\) has equal \(s_a=s\), lies in
\([203/240,277/240]\), and is the branch connected to neutral zero load.

Let \(u(s)=U(\Omega(s),\Omega(s))\). The equal-body residual is
\[
 f(s)=s-1+\frac{\eta[u(s)-u(0)]}{4Ss}.
 \tag{6}
\]
The contraction bound gives \(f'(s)\ge1-73/2880>0\) throughout the box. At \(s=1\),
\(f(1)=\eta\Delta U_F/(4S)\). Thus, for positive load on this branch,
\[
 s=1\iff\Delta U_F=0,\quad
 s>1\iff\Delta U_F<0,\quad
 s<1\iff\Delta U_F>0.
 \tag{7}
\]
This proof evaluates the angular criterion only at the unloaded endpoint \(s=1\). It does not assume that \(W(s)\) remains parallel to \(w\).

### 2.2 The neutral locus and its endpoints

Write \(M=m(q_0)\), \(m_F=m(Fq_0)\), and define
\[
 A_g=G_N(M^2-m_F^2)>0,\qquad
 B_m=c_m\kappa^2|w|^2>0 .
 \tag{8}
\]
For the acute angle \(\theta\in[0,\pi/2]\) between \(n\) and \(w\),
\[
 \Delta U_F(r,\theta)=\frac{A_g}{r}
 +\frac{B_m}{r^3}(1-3\cos^2\theta).
 \tag{9}
\]
Therefore the positive-load neutral locus is
\[
 3\cos^2\theta_*(r)-1=\frac{A_g}{B_m}r^2,\qquad
 r_*=\sqrt{\frac{2B_m}{A_g}}.
 \tag{10}
\]

| Separation, within the certified domain | Consequence |
|---|---|
| \(0<r<r_*\) | One interior acute neutral angle. Smaller angles advance farther than \(F\); larger angles advance less. |
| \(r=r_*\) | Only the end-to-end direction is neutral; every nonzero acute angle slows the advance. |
| \(r>r_*\) | Every direction slows the advance. |

As \(r\downarrow0\), the formula approaches \(\arccos(1/\sqrt3)\), but neither overlapping bodies nor uncertified small separations are included by taking that formal limit.

The zero in (9) comes from the GM01 source interaction. The equivalence between zero work and \(s=1\), and the signs in (7), use GM02's specific response rule. Many other response models could share a zero-work locus. A neutral angle alone does not identify \(h\), its energy, or its persistence.

For non-neutral magnitudes, specifying \(\theta\) alone is generally insufficient: \(W(s)\) turns slightly, so the full direction \(n\), including its azimuth relative to that turn, matters. The sign and neutral locus above depend only on \(\theta\) because they use \(w=W(1)\). One definite angular scan is
\(n=\cos\theta\,w/|w|+\sin\theta\,e_z\).

### 2.3 Benchmark and held-out distance

At \(r_0\), GM02 has \(a_{\rm load}=1/100\), \(b_{\rm load}=10^6\), and \(\eta=1\). The exact endpoint values are
\[
 I_F=\frac{135375001}{50000000},\qquad
 |w|^2=\frac{812250003}{40000000000000000},\qquad
 \xi:=\frac{A_gr_0^2}{B_m}
 =\frac{4173609104249999}{5076562518750000}.
 \tag{11}
\]
Thus
\[
 \cos^2\theta_*(r_0)=
 \frac{9250171622999999}{15229687556250000},
\]
\[
 \theta_*(r_0)\approx38.79941498146755^\circ,\qquad
 \frac{r_*}{r_0}
 =\sqrt{\frac{10153125037500000}{4173609104249999}}
 \approx1.559710449481958.
 \tag{12}
\]
The rational and radical formulas define the exact quantities; the decimals are approximations.

Keep \(\eta,G_N,c_m,\alpha,\kappa,S\) fixed while changing distance. For \(r=\rho r_0\),
\[
 a_{\rm load}(\rho)=\frac{1}{100\rho},\qquad
 b_{\rm load}(\rho)=\frac{10^6}{\rho^3}.
 \tag{13}
\]
At \(\rho\ge1\) these remain in (5). If \(r_0>\ell_1+\ell_2\), all these comparisons retain disjoint supports, so GM02's exact radial-source cross-energy result continues to apply.

At the held-out distance \(2r_0\), with no refit:

| Fixed center-line direction | Predicted \(s\) |
|---|---:|
| Parallel to \(w\) | 0.999181277166928332 |
| Along \(e_z\), perpendicular to the body plane | 0.997279741050153918 |

Each value has a rational root enclosure of width \(2^{-100}\). Both are below one, consistent with \(2r_0>r_*\). These are predictions of the mathematical candidate, not measured outcomes.

## 3. One loaded step followed by switch-off

### 3.1 Matched copies reveal the proposed store

Starting from \(h_0=1\), a loaded step gives
\[
 h_1=2s_{\rm on}-1,\qquad
 q_1=q_0+s_{\rm on}[F(q_0)-q_0].
 \tag{14}
\]
Now set \(\eta=0\), holding \(q_1,h_1\) fixed across the intervention. Equation (3) gives
\[
 h_2=h_1,\qquad
 q_{2,\rm exposed}-q_1=h_1d_1,\qquad d_1=F(q_1)-q_1.
 \tag{15}
\]
A fresh copy at the same \(q_1\), pose, geometry and zero load, initialized with \(h=1\), has \(q_{2,\rm control}=F(q_1)\). Subtracting proves (1) and
\[
 s_{\rm next,off}-1=2(s_{\rm on}-1).
 \tag{16}
\]
It is the departure of the *multiplier* from one that doubles. The native directions at \(q_0\) and \(q_1\) differ, so absolute state displacement does not generally double.

The two arrangements reach different \(q_1\). Each exposed body must be compared with its own matched control, not with the other arrangement's reached state.

### 3.2 The next direction is nonzero

This can be proved on the whole inherited box \(1/2\le s\le3/2\), without numerically resolving the next phase kicks.

Let \(b_i=|\Omega_i(s)|\). Equation (4) gives \(9/10<b_i<1\) and
\[
 \sum_i\Omega_i(s)=as(\omega^2-1),\qquad
 \left|\sum_i\Omega_i(s)\right|=\sqrt3\,as<3a.
 \tag{17}
\]
At this state, the next native prestage can be written
\[
 v_i=\rho_i\Omega_i+g\sum_j\Omega_j,\qquad
 \rho_i=\frac{19}{20}+\frac1{10}(k_i-b_i^2).
 \tag{18}
\]
Since \(k_i\in[0.999,1.001]\),
\[
 \frac{9499}{10000}\le\rho_i\le\frac{9691}{10000},\qquad
 g\left|\sum_j\Omega_j\right|<\frac1{200000}.
 \tag{19}
\]
Triangle inequalities imply
\[
 |v_i|>\frac{170981}{200000}>0,\qquad
 b_i-|v_i|>\frac{5561}{200000}>0.
 \tag{20}
\]
The phase stage preserves each prestage modulus, even though its kicks need not vanish at this second step. Therefore every output modulus is strictly smaller than its input modulus, proving \(d_1\ne0\). In particular,
\[
 \|d_1\|_2>\sqrt3\,\frac{5561}{200000}.
 \tag{21}
\]
Both reported preparations, and the neutral-angle reached state, lie in this box.

### 3.3 Predictions and controls

The original GM02 rational brackets imply:

| Previous arrangement at \(r_0\) | Loaded \(s_{\rm on}\) | Exposed next multiplier at zero load | Own matched neutral control |
|---|---:|---:|---:|
| Parallel | 1.006036216843173 | 1.012072433686345 | 1 |
| Transverse | 0.990788805175576 | 0.981577610351153 | 1 |
| Exact neutral angle | 1 exactly | 1 exactly | 1 |

The neutral-angle control still has a nonzero next native direction by (20), but no exposure-induced store difference. For a native fixed-state control \(F(q)=q\), all multipliers yield zero displacement. Such a control cannot identify \(h\), even if its value or stored energy differs.

At every later ideal step with \(\eta=0\), \(h\) remains constant. The multiplier therefore persists while the triad evolves by \(q^+=q+h[F(q)-q]\). The resulting displacement, readout change or detectability need not stay constant; it can vanish if the native direction vanishes. No repeated-step boundedness or convergence theorem is added.

The matched-copy conclusion uses the product-state preparation allowed by GM02: \(q\) and \(h\) are independently specifiable, so a fresh neutral \(h=1\) copy at arbitrary finite \(q_1\) is mathematically admissible. A physical preparation apparatus capable of that reset has not been identified.

Instantaneous prescribed source fields depend on the current triads, poses and geometry, not on \(h\). The matched copies therefore have the same current \(q_1\) and prescribed fields. Any single-valued function of those inputs assigns them the same value; it cannot distinguish the two next advances. This establishes missing state information in that reduced description of GM02, not a failure of the unmodified native closure theorem.

## 4. Switching has an external work account

The step conservation theorem assumes fixed \(\eta\) and geometry. During the stated switch, \(q,h\) are held fixed, so the external work on the modeled energy is
\[
 W_{\rm switch}=(\eta_{\rm after}-\eta_{\rm before})U(q_1).
 \tag{22}
\]
For switch-off from \(\eta=1\), it is \(-U(q_1)\), not zero. In the benchmark, using \(S\) as energy unit, it is approximately \(+0.114290611028S\) for the parallel trial and \(+0.053494605143S\) for the transverse trial. These terms are separate from the loaded-step exchange and the subsequent zero-load evolution.

If an external controller instead changes geometry while freezing the states and stores, with \(\eta\) fixed, its work is
\[
 W_{\rm geom}=\eta\,[U(q_1;r_f,n_f)-U(q_1;r_i,n_i)] .
 \tag{23}
\]
For fixed poses this is explicitly
\[
\begin{split}
 W_{\rm geom}/\eta={}&-G_Nm_1m_2(1/r_f-1/r_i)\\
 &+c_m\left[
 \frac{\boldsymbol\mu_1^TQ(n_f)\boldsymbol\mu_2}{r_f^3}
 -\frac{\boldsymbol\mu_1^TQ(n_i)\boldsymbol\mu_2}{r_i^3}\right].
\end{split}\tag{24}
\]
Changing poses also changes the moments in these endpoint energies and requires the corresponding rotational work. With both geometry and \(\eta\) controlled and \(q,h\) fixed, the total is
\(\eta_f U_f-\eta_iU_i\); its differential is \(U\,d\eta+\eta\,d_{\rm geom}U\).

Moving to a finite “neutral” geometry is not switching the interaction off. Equation (10) cancels a particular unloaded work increment for the original preparation; it does not set the interaction or its derivatives to zero for later states. Taking separation to infinity makes \(U\to0\) in this static model and costs \(-\eta U_i\), but no finite-time physical separation protocol is supplied. If the state changes during the intervention, (22)–(24) alone are insufficient.

An independently verified physical operation corresponding to the mathematical switch is therefore part of the proposed experiment, not something established by these equations.

## 5. Reconstructing advance and identifying parameters

### 5.1 Required state observations

For \(d=F(q)-q\ne0\), a registered state pair gives
\[
 s_{\rm obs}=\frac{(q^+-q)\cdot d}{d\cdot d},\qquad
 r_\perp=q^+-q-s_{\rm obs}d .
 \tag{25}
\]
The candidate requires \(r_\perp=0\). A nonzero residual beyond independently characterized measurement and native-map error cannot be repaired by fitting \(S,\eta\) or \(h\).

The measurement must recover the six real coordinates \((\Re\Omega_i,\Im\Omega_i)\), with channel labels, the coefficient tuple, handedness and amplitude normalization fixed. Both snapshots must use a common phase registration. One *shared* common-phase rotation of the pair preserves (25) on the regular native domain; independently rephasing successive snapshots generally does not. Update order and sample index must also be known. A native update count is not yet a calibrated physical time.

The accepted face decoder supplies a mathematical route: if all three labeled vectors are known in their fixed planes,
\[
 v_i=x_i t_i+y_i e_z,\qquad
 \Omega_i=t_i\cdot v_i+i\,e_z\cdot v_i.
 \tag{26}
\]
It is lossless on those tangent planes. The source does not identify an instrument that measures the required vectors as physical features.

Intensity, \(C,W,\Gamma\), or staged Z alone do not supply this full registered state. The accepted five-coordinate reconstruction additionally needs common-phase data and its stated near-aligned native domain and history. The Fourier benchmark is outside that domain, and its loaded evolution is not the unchanged native history. That theorem cannot be used here to infer unmeasured phase. A computational full-state record can implement (25), but testing the same implementation that generated it is not an independent physical observation.

When \(d\) is small, projection is ill-conditioned: with known \(d\), an additive displacement error \(\varepsilon\) can produce \(|\delta s|\le\|\varepsilon\|/\|d\|\). At \(d=0\), \(s\) is unidentifiable by displacement. The positive bound (21) removes that particular degeneracy for the first switch-off test.

### 5.2 Independent work and the store scale

For a symmetric step from neutral storage, the two store changes sum to \(4Ss(s-1)\). Hence non-neutral trials require
\[
 \boxed{\ \frac{S}{\eta}
 =-\frac{\Delta U_{\rm loaded}}{4s(s-1)}>0.\ }\tag{27}
\]
The same value must hold across trials with the same store scale and load parameter. Here \(\Delta U_{\rm loaded}\) is the change of the **unscaled** \(U\) evaluated at the actual loaded endpoints, not the unloaded \(\Delta U_F\). If the independently measured work is instead \(W_{\rm int}=\eta\Delta U_{\rm loaded}\), the corresponding formula directly returns \(S\).

At \(s=1\), both numerator and denominator vanish. Such a trial provides no scale estimate. Near one, independent errors are amplified; for \(R=S/\eta\),
\[
 \frac{\delta R}{R}\approx
 \frac{\delta(\Delta U)}{\Delta U}
 -\frac{2s-1}{s(s-1)}\,\delta s .
 \tag{28}
\]
The formula is also singular at \(s=0\), which is outside the branch used here.

Pair work inferred solely by inserting fitted \(\alpha,\kappa\) and observed states into (2) is useful for an internal consistency check. It cannot independently validate the energy account. Such validation requires a calibrated measurement of the relevant interaction work, separated from switching, self-energy and other native or apparatus contributions. No such measurement is in the reviewed record.

### 5.3 What ideal state and geometry data identify

Define the known geometric/state functions
\[
 J_g=-I_1I_2/r,\qquad
 J_m=W_1^TQ(n)W_2/r^3 .
 \tag{29}
\]
For known positive \(\eta\), the measured symmetric endpoints imply
\[
 \frac{G_N\alpha^2}{S}\Delta J_g+
 \frac{c_m\kappa^2}{S}\Delta J_m
 =-\frac{4s(s-1)}{\eta}.
 \tag{30}
\]
Two or more trials identify the two ratios when this two-column design has rank two. The parallel and transverse benchmark trials satisfy that condition: the gravitational work coefficients are positive, while the magnetic coefficients have opposite signs. An exact interval determinant check using the original root brackets confirms nonzero rank.

In units based on \(r_0\), a fit to these model-generated trials recovers
\(a_{\rm load}=0.01\) and \(b_{\rm load}=10^6\) within their propagated root uncertainty. This demonstrates identifiability, not empirical support. The held-out predictions in §2.3 use these same scales.

With independently measured physical distances, the ratios in (30) have dimensions of length and length cubed, respectively, in the fixed native amplitude convention. If distances are only known up to scale, additional length-scale ambiguity remains. If \(\eta\) is not calibrated, only its products with the two ratios are identified at that load.

The transformation
\[
 \alpha\mapsto c\alpha,\quad
 \kappa\mapsto c\kappa,\quad
 S\mapsto c^2S,\qquad c>0,
 \tag{31}
\]
leaves all such state-response data unchanged. Identical-body interaction trials also cannot determine the sign of \(\kappa\). Independent mass, magnetic-field/moment, or work/energy calibration is needed to separate these scales.

The neutral locus determines \(A_g/B_m\), hence a ratio of source strengths once the native preparation is known; \(S\) cancels. An unloaded probe at \(d\ne0\), on the other hand, measures the dimensionless \(h\) directly through its advance. Energy assigned to that value still requires \(S\). The switch-off doubling test provides a held-out prediction without fitting either scale.

## 6. Earlier observables and stores

The accepted router and claim atlas lead to PHASE/NRG for state reconstruction and to RX/WT for added storage. Their actual equations give the following comparison. No generic “memory” label is treated as a carrier identification.

| Existing object | Defined state, initialization and energy | Relevant behavior and missing identification |
|---|---|---|
| Face-state decoder | Three labeled tangent-plane vectors; inverse (26). | Supplies full state mathematically, not an extra store or physical measurement apparatus. |
| PHASE retained state and common phase | Retained tuple plus initial common phase; theorem on its specified native domain. | Reconstructs the admitted native history. Does not reconstruct GM03's Fourier/loaded history from reduced readings. |
| Z/EMA observation memory | Initial memory plus sampled innovation and fixed update weight \(0.01\); observation and memory update are distinct operations. No assigned physical energy. | Can record history as an observer state. It neither multiplies the native update by that memory nor freezes its update automatically when GM02's \(\eta\) is zero. A coupling and energy dictionary would be new. |
| RX receiver \(z\) and carrier \((p,r_c)\) | Independently prepared receiver/carrier; \(H_R=\beta_R|z|^2/2\), \(H_C=\frac12\int(p^2+r_c^2)\). Units are abstract \(\mathrm U^2\mathrm L\), not an established joule calibration. | Native exchange is \(\dot x=-\eta_NJ_f(x)^Ty/(2\alpha_N)\), followed through an \(F\)-then-exchange cadence. At \(\eta_N=0\), each sampled native jump is \(F\), regardless of receiver history. It does not supply the persistent multiplier (16). |
| WT traveling fields and receiving field \(\zeta\) | Independent energy-space profiles and receiving state; \(E_{\rm tr}\) and \(H_G=\beta_G\|\zeta\|^2/2\). | Added feedback is \(-\kappa_T^2Q+\sqrt2\kappa_TJ^*b\). Setting \(\kappa_T=0\) removes this added channel, but old RX couplings may remain. This is not automatically GM03's full switch-off. No map to \(h\), \(S\), or the exact scalar gain is defined. |

Here \(\kappa_T\) denotes the transport paper's coupling, to distinguish it from the magnetic-moment coefficient \(\kappa\). Likewise the RX coefficients and exchange cadence are not GM03's \(\eta,S,h\).

These sources provide possible classes of additional state, not a demonstrated implementation of the controls. A carrier identification would have to specify a map from a measured carrier state to \(h\), convert its energy to \(Sh^2/2\), realize neutral preparation at the reached \(q_1\), implement the loaded debit, preserve \(h\) during verified switch-off, and produce the measured advance along \(F(q)-q\). Existing equations supply no such complete identification.

This conclusion does not exclude a later correspondence using these states. It identifies the additional laws and measurements it would require.

## 7. Decisive tests and delivery

The strongest store-specific rejection test is a matched-copy trial with a clearly non-neutral loaded step and \(d_1\ne0\). If a verified switch leaves \(q_1,h_1\) unchanged but the exposed next multiplier differs from \(2s_{\rm on}-1\), the proposed rule fails. In particular, ordinary advance \(1\) after a non-neutral exposure would contradict its persistent store prediction. Adjusting \(S,\alpha,\kappa\) cannot repair the parameter-free relation once \(s_{\rm on}\) is measured.

A nonzero perpendicular residual in (25) rejects the response-direction ansatz without needing an energy measurement. Inconsistent positive scale estimates from independent work in (27) reject the declared store account. A neutral angle by itself does neither.

All these statements are conditional on the stated measurement, registration and intervention controls. No independently measured quantity currently supports the physical realization. [CHECK_RESULTS.json](CHECK_RESULTS.json) contains 39 reproducible exact identity, inequality, interval and numerical-corroboration groups; none is a physical experiment. The prior four root brackets were checked directly, and the new held-out roots have rational brackets of width \(2^{-100}\).

[CLAIM_LEDGER.json](CLAIM_LEDGER.json) separates inherited premises, exact consequences, conditional physical predictions and missing evidence. [INPUT_VERIFICATION.json](INPUT_VERIFICATION.json) records unchanged GM01/GM02 packages and twelve primary sources. [REVIEW_RECEIPT.json](REVIEW_RECEIPT.json) records final preservation and document checks. The one-page explanation is supplied separately in editable text and PDF.

### Primary source locators

- [GM02 derivations](inputs/GM02_DERIVATIONS.md), equations (5), (19)–(25), (33)–(46), and its certified examples.
- [Paper G](sources/papers/PAPER_G/v0.1.1/source/paper_g.tex), eq:T, eq:W, eq:hidden.
- [Native setting](sources/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex), eq:pre and eq:full.
- [Lossless decoder](sources/papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/manuscript/spatial.tex), eq:decoder; [reconstruction](sources/papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/manuscript/reconstruction.tex), thm:reconstruction.
- [Observation and EMA dependencies](sources/papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/manuscript/observations.tex), eq:rawobservations, eq:staged, eq:innovation and the dependency table.
- [RX stores and exchange](sources/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/candidate.tex), eq:storages and eq:system; [zero-coupling hybrid](sources/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/hybrid.tex), prop:hybrid.
- [WT retained RX account](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/02_setting.tex), eq:RX and eq:RXstocks; [new transport/storage law](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/05_transport.tex), eq:closedmodel and eq:augmentedstocks; [physical interpretation](sources/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/09_discussion.tex).
