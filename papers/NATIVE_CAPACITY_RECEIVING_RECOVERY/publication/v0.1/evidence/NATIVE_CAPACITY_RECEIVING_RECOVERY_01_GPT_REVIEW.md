# GPT review — Capacity-sized receiving and native recovery

**Investigation:** NATIVE_CAPACITY_RECEIVING_RECOVERY_01  
**Review date:** 5 November 2026, Atlantic/Reykjavik  
**Research author and geometric direction:** Hilmir Frímann Halldórsson (pzychozen)  
**Proposal and current review:** GPT  
**Independent investigation:** Codex  
**Review status:** project-internal mathematical and evidence review; not external peer review or machine-formal verification.

## Disposition

**Accepted — Established unchanged within the specified candidate-model regime.**

The returned proof establishes all commissioned receiving, remaining-stock and net-recovery conclusions with the proposed equations, hypotheses, phase cutoff, coefficient restrictions, evaluation times, error constant and fractions unchanged. No necessary mathematical, source or delivery correction was found. No corrective Codex investigation is required.

This acceptance applies to the investigation and its actual submitted proof/evidence. It is not acceptance of a new typeset manuscript, permission to publish, adoption in the native kernel, or a claim of calibrated physical transport. The prior P4 publication and XW-01 closeout remain closed.

## 1. Exact accepted statement

Use the inherited periodic carrier, whole-circle separation and finite-width H1 profiles; the unchanged raw two-port registration at yaw pi/4; original unscaled exchange equations; and positive finite coefficients fixed before the phase. Write alpha=alpha_N, beta=beta_R, eta=eta_N and kappa=eta_R.

In the published normalized amplitude convention,

\[
R=\sqrt3,\quad k=G\sqrt{8/7},\quad m=2/(3\epsilon_c),\quad d=2/\epsilon_c^3,
\]
\[
\nu^2=\frac{\eta^2 m k^2R^2}{2\alpha},\qquad
\gamma=c\sqrt{d/m},\qquad
\omega_R=\kappa\sqrt{m/\beta}=\nu/3,\qquad
0<\gamma/\nu\le1/100.
\]

For **every** phase \(0<\phi\le1/100\) radians, prepare the exact state

\[
\Omega_0=(1,e^{i\phi},1),\qquad p_0=r_{c,0}=z_0=0,
\qquad C=C_{\rm joint}=\alpha(1-\cos\phi)>0.
\]

Let

\[
\varpi=\sqrt{17/18}\,\nu,\qquad
0<t_A=1/\nu<t_R=\pi/\varpi<t_F=2\pi/\varpi.
\]

On that phase's **one unchanged actual solution**, with positive propagation and receiving throughout,

\[
E_A:=E_{\rm out}(t_A)>\frac{1053}{4096}C,
\]
\[
\boxed{H_R(t_R)>C/4,\qquad H_C(t_R)<C/100,\qquad
E_F:=E_{\rm out}(t_F)<C/100.}
\]

The first statement is inherited from P4 only after the same fixed tuple is shown to satisfy P4's condition. The three boxed statements are the new finite-error conclusions.

For \(E_R=E_{\rm out}(t_R)>0\), the accepted corollaries are

\[
\frac{25}{26}<\frac{H_R(t_R)}{E_R}\le1,\qquad
0\le\frac{H_R(t_F)}{H_R(t_R)}<\frac1{25},
\]
\[
\frac{24}{25}<\mathcal R_A:=\frac{H_N(t_F)-H_N(t_A)}{E_A}\le1,\qquad
\frac{24}{25}<\mathcal R_R:=\frac{H_N(t_F)-H_N(t_R)}{E_R}\le1,
\]
\[
H_N(t_F)-H_N(t_R)>\frac6{25}C.
\]

The written argument retains the sharper intermediate arithmetic
\(\mathcal R_A>25301/26325>24/25\). This is already in the submission, not a new strengthening commissioned by this review.

**Proof locators:** RR01–RR08, RR30–RR34. All coefficients and the three evaluation times are independent of phase at a fixed admissible tuple. Each phase defines a separately prepared trajectory; no parameter is changed along any trajectory.

## 2. Mathematical review

### 2.1 Inherited solution and accounts are used at their actual scope

P1 Theorem 3.1 supplies global existence, uniqueness and H1 carrier regularity for the empty preparation before any new estimate. The finite native shift preserves that regularity. The raw two-port native signs, factor one-half, matched receiver loading, and original quadratic stores agree with the supplied P1/P3/P4 sections.

The bounded adjoint makes the port output continuous. Periodic H1 products justify integration by parts. The tents are differentiated once only; no corner delta term or second L2 derivative is assumed. The whole-circle separation, including the periodic seam, is explicitly retained.

Conservation gives E_out=H_N(0)-H_N(t) and nonnegative external stock. P3 supplies the same C_joint at yaw pi/4 in the declared phase family. P4 is not confused with P1 despite their matching theorem numbers.

**Finding:** RR01–RR08 use the accepted sources consistently and add no hidden preparation or invariant-phase-domain assumption.

### 2.2 The old sufficient certificate regimes really are incompatible

P3's B2 threshold, with A=nu^2 Fmax/2, implies

\[
(\kappa\sqrt{m/\beta}/\nu)^2
\ge\frac{8\pi^3F_{\max}}{3q|f_0|}
\ge\frac{8\pi^3}{3q}>1/4
\qquad(0<q\le1/5).
\]

Every divided quantity is positive; Fmax >= |f0| follows from the inherited drive bound. P4's condition instead requires this same squared rate to be at most 1/4. The conclusion is disjointness of the **sufficient certificate regimes**, not impossibility of simultaneous access, receiving or recovery behaviors. The proof correctly supplies a new route rather than importing P3's 80/81 or P2's returning-power guarantee.

**Finding:** RR09 is correct at its explicitly limited scope.

### 2.3 Tangent geometry and the exact nonlinear remainder are correct

For v=(1,1,1) and e=(1,-1,0)/sqrt(2), direct evaluation gives
D=K[v]_cross=ell e^T, |ell|^2=20G^2/7 and omega_N^2=(5/6)nu^2. This is a rank-one **tangent** drive; the original K remains rank two.

With u=a-v, the decomposition retains all of

\[
\mathscr N(Y)=\left(\mu w\times b,-\mu w\times u,
\eta\mathcal B K(u\times b),0,0\right).
\]

The proof norm weights the native deviations by **2 alpha**, not alpha. Its tangent native work is -eta(Db)^T y, exactly cancelling the carrier term. Receiver loading cancels with its beta-weighted state term, while periodic propagation contributes zero. This norm is explicitly not the original native store or a conserved nonlinear energy.

The nonlinear estimate is sound: orthogonal native/external blocks give
\(\|\mathscr N(Y)\|_*^2\le L^2(X_N^2V_{\rm ext}^2+X_N^4/4)\),
which is bounded by \(L^2\|Y\|_*^4\). The submitted proof establishes the stated L without changing its value.

**Finding:** RR10–RR16 retain the complete system, correct signs and weights. The zero-norm regularization is valid for already strong curves; no existence claim is inferred from cancellation alone.

### 2.4 Exact initial data and scalar majorant are legitimate

The initial real deviation is (0,cos(phi)-1,0), not zero. The imaginary component is (0,sin(phi),0), not its first-order approximation. Their auxiliary norm squared is exactly 4C.

The proof constructs a positive differentiable scalar Q from the actual continuous norm, obtains Q'<=L Q^2, and integrates (1/Q)' >= -L. It inverts only a positive lower bound. The independent parameter calculation establishes theta=2L sqrt(C)t_F<1/25 before the majorant is used up to t_F. Thus there is no circular bootstrap or unjustified differentiation of a norm at zero.

**Finding:** RR17–RR18 and RR23–RR24 are sufficient, including the cutoff endpoints.

### 2.5 The reference includes moving native and receiver coordinates

The explicit reference preserves the full static real deviation and inactive imaginary part, and its active coordinate starts at the correct negative value X0=-sqrt(alpha)sin(phi). All three coupled oscillator equations and all initial data hold. Its carrier embedding has the correct normalization through B*B=mI.

At t_R the reference carrier vanishes; at t_F the entire reference external state vanishes. Its receiver amplitude at t_R is exactly
\((2\sqrt{30}/17)\cos(\phi/2)\sqrt{2C}\).
These are reference-only facts until the finite error is controlled. The proof makes no actual-period, exact-state-return or first-return assertion.

**Finding:** RR19–RR22 correctly retain native response rather than freezing the core.

### 2.6 The finite-error estimate handles propagation and nonlinearity

The actual and reference curves are strong before subtraction, so the difference is strong before its L2 residual is estimated. Both linear operators include the same native/carrier/receiver interaction. Their only propagation difference on the reference is -c partial_s p^(0) in the second carrier coordinate. There is no missing receiver residual and no operator-norm limit of an unbounded generator.

The nonlinear majorant integrates to y0 theta/(1-theta). The propagation term integrates over the full reference period to 4 gamma |X0| omega_N/varpi^2. The integrands are nonnegative, so the resulting endpoint estimate bounds every earlier time. Dividing by the positive sqrt(2C) gives the full uniform inequality.

All strict rational comparisons are correct, including the integral certificate for pi<22/7, pi>8/3, nu t_F<20/3, theta<1/25, and

\[
\sup_{0\le t\le t_F}\frac{\|Y-Y^{(0)}\|_*}{\sqrt{2C}}
<\frac5{84}+\frac1{25}=\frac{209}{2100}<\frac1{10}.
\]

Strictness survives phi=1/100 and gamma/nu=1/100. The positive-phase endpoint excludes C=0 before normalized divisions. The elementary pi inequalities are local arithmetic tools, not an invocation of the separate pi brainstorming topic.

**Finding:** RR23–RR28 are valid finite-parameter estimates; none is merely an asymptotic assertion about a comparison system.

### 2.7 Stock projections and denominators are correct

The carrier, beta-weighted receiver and joint external projections are contractive for the auxiliary norm, and on those projections the norm is exactly twice the respective original trial stock when squared. There is no rescaling of the conclusions' physical bookkeeping.

The reference receiver amplitude exceeds (3/5)sqrt(2C). Subtracting the error leaves a positive actual amplitude above (1/2)sqrt(2C) **before squaring**. The reference zero carrier and zero final external state then give the strict C/100 bounds with the original factor one-half.

The new fixed coefficients satisfy sigma_ext^2/nu^2 <= 1/10000+1/9 < 1/4, so P4's access statement applies on the very same global solution. C, H_R(t_R), E_R and E_A are all proved positive before ratios are formed. Conservation gives the net recovery identities and the upper bounds of one. Every receiver-share, receiver-retention, external-stock and capacity denominator remains distinct.

The integrated accounts and power continuity imply existence of separate nonempty sign intervals within the relevant windows. They do not establish coincident native/receiver sign intervals, endpoint signs, a first return or a monotone window. The submission states this correctly.

**Finding:** RR29–RR33 complete the requested actual-solution conclusions.

### 2.8 Nonempty finite regime and units

Choosing one finite nu_target >=100c sqrt(d/m), then
eta=nu_target sqrt(2alpha)/(kR sqrt(m)) and
kappa=(nu_target/3)sqrt(beta/m), produces the exact declared relations before any phase is selected. Actual c and kappa remain strictly positive. This is an equality-constrained sufficient family, not a robustness neighborhood or classification of all P4 tuples.

Restoring amplitude A_* retains R=sqrt(3)A_*, the amplitude of v in D, and A_*/R in theta. Both chosen couplings are dimensionless, the comparison rates have inverse-time units, and the auxiliary norm has the square-root units of the original stores. No physical calibration or native F-step clock follows.

**Finding:** RR34–RR36 and the units table are consistent. No hypothesis or coefficient needs correction.

## 3. Meaning and remaining limits

The accepted advance is one same-trajectory sequence: a certified capacity-sized external stock, a later capacity-sized **receiver** stock, and subsequent quantified **net native recovery**. It closes the precise receiving/recovery question commissioned for the declared subfamily.

This is not a quarter of the whole native store. The exact ratio remains
C/H_N(0)=(2/3)(1-cos(phi)), and the absolute stocks can tend to zero as phase approaches zero even though their capacity-normalized guarantees are uniform. The present small phase range is material, not an incidental restriction.

The result does not establish ceiling saturation, large absolute/whole-native transfer, all admissible couplings/phases, irreversible retention, tagged-cohort transport, sustained monotonicity, exact nonlinear recurrence, an assigned material receiver, physical calibration or the intended spatial circuit. No part of P3's 80/81 fraction is silently transferred into this regime.

The central starting/meeting region, opposed cones, outward spreading, curved around-and-inward return, stationary supports and possible transfer elsewhere remain the programme's geometric direction. Carrier circle, intended tight toroid, close original sphere, extended-line sphere, host-notch N regions and central broken G boundaries retain their distinctions.

## 4. Independent evidence verification

The accompanying independently written `independent_review_verify.py` checks actual bytes, not just submitted PASS flags. Its results are in `verification/REVIEW_VERIFICATION.json`.

| Check | Result |
|---|---|
| Submitted review ZIP | 290,510 bytes; sidecar matches; 95 safe unique members; CRC passes |
| Review manifest | All 94 payload sizes/hashes match, with exhaustive membership and exact self-exclusion |
| Original issued packet | 219,620 bytes; own checksum matches; 77 members / 76 manifest-covered payloads verified |
| Issued inputs in submission | All 77 original members byte-identical; no added or missing input member |
| Standalone proof, ledger and completion report | Exactly match their archived versions |
| Separate issued order and assessment | Exactly match their original packet and returned copies |
| Selected source registry | All 64 records match supplied bytes |
| Independent source comparison | 61 match the separately mounted prior publication closeout; the other three match separately mounted review/receipt/remote-record attachments |
| Historical source-account reconciliation | 61 retained remote-record entries and 60 publication-manifest entries agree; the manifest self-exclusion explains the difference |
| Prior closeout used as reference | Matching sidecar; 330 members / 329 manifest payloads and CRC independently checked, read-only |
| Input preservation | All 82 before/after records match their baseline and actual supplied/reference bytes: 77 input members plus five separately mounted original files |
| Crosswalk | PR01–PR23, RR01–RR36, 11 inherited groups, all 41 source labels and 25 available printed label records checked |
| Analytical obligations | All 14 written obligation entries accounted for; analytical validity assessed in section 2 above, not inferred from counts |
| Exact replay | All 14 returned algebra groups pass; every group result equals Codex's result |
| Post-review preservation | Every extracted submission byte still equals the received archive |

The new source comparison also independently resolves the three entries for which Codex lacked a separate prior-archive comparison: the previous GPT closeout review, publication receipt and remote-byte JSON all match their separately mounted attachments. These remain provenance records, not new mathematical premises.

### Execution and verification limits

The exact script was inspected, copied unchanged to a separate replay directory, and executed with Python 3.13.5 / SymPy 1.14.0, isolated mode and bytecode disabled. Codex used Python 3.11.15 / SymPy 1.14.0. The fourteen result groups match exactly; timestamps and environment metadata appropriately differ. This is another execution of the **same fourteen groups**, not fourteen additional independent discoveries.

The written review separately checks existence/regularity inheritance, periodic Sobolev integration, zero-norm regularization, nonlinear scalar comparison, strict bounds, quantifiers and interpretation. Symbolic identities do not formally prove those analytical arguments. Hash matching supports identity and preservation, not mathematical truth.

This review did not inspect the live Windows filesystem or perform fresh GitHub retrieval, Git operations, PDF rendering/building, historical-suite execution, parameter scans or numerical trajectories. The Windows before/after records are independently reconciled against the delivered/reference bytes; no machine-wide audit is claimed. No supplied preparation or packaging workflow was executed.

## 5. Accepted identities

| Object | Bytes | SHA-256 |
|---|---:|---|
| Submitted proof | 27611 | `561fff728cc4e887ead8b7fc377a78bfbc91cde873ad7c1ac4e6631828797774` |
| Submitted ledger | 15493 | `1fdd5eceb714bcebd1e74bb2b78f291c1188660f2fd420b6a37090d0926fd00e` |
| Submitted review ZIP | 290510 | `d34f1975a3d4dc76638566414836d28da5b19915dba15e724db5e7d2e47614fe` |
| Exact-check script | 13565 | `54dad3bb9421aa608ce4f78cc57c04f42710d21c7637b722e085eb0ffe93500f` |
| Issued work-order packet | 219620 | `474270eb78f06e2c4f9bc988add58078f4de8063de836970fba1acd035f81dd3` |

## 6. Closure and recommendation

**The bounded investigation is accepted unchanged and closed. No corrective round is necessary.**

Recommendation: capture this result in a focused companion paper before opening another scientific investigation. The same-parameter receiving/recovery gap is now answered in an explicit nonempty subfamily; the remaining universality, optimization, saturation and physical/spatial questions are distinct. They need not be treated as defects in this completed certificate.

After manuscript/publication closeout, the agreed next scientific assessment can turn to native F stepping and exchange cadence, explicitly tracking the native baseline increment. Intended-route and six-opening correspondence follow, with gravity–magnetism linked and outer geometry / justified SRG integration standing later. This paragraph is a recommendation and continuity statement, not a new Codex work order or publication authorization. Three-Way stays parked. No new geometric choice was needed for this review.
