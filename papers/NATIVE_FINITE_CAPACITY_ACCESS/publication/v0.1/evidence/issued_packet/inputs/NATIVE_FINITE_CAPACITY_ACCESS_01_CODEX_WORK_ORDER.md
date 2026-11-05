# Codex work order — NATIVE_FINITE_CAPACITY_ACCESS_01

## 1. Mission and reason

**Independently establish, correct or refute one explicit finite-time certificate that more than one quarter of the accepted joint capacity ceiling is held in the carrier and receiver combined.**

Use the existing reciprocal chiral exchange candidate, the published coherent empty-launch family, and the already published witness yaw \(\delta_g=\pi/4\). Retain finite positive propagation speed and receiver coupling.

The accepted transfer-and-capacity paper distinguishes a recoverable fraction of an actual transferred stock from the amount of that stock relative to a structural ceiling. Its large-receiver-coupling certificate gives strong receiving and recovery fractions while the intermediate stock decreases as \(\kappa^{-2}\). The present question is whether an explicit fixed finite regime certifies a positive fraction of the joint ceiling on an actual solution. Merely reproving a positive initial debit does not complete this mission.

The proposed constants and route below have received preparatory analytical checks. They remain **proposed**, pending your independent proof and subsequent review. Treat every new inequality as something to verify, not an accepted result to reproduce.

## 2. Baseline and authorization

The immediately preceding paper is published and closed:

**P3:** *Recoverable Transfer and Projection Capacity in the Reciprocal Chiral Exchange Candidate*, v0.1, 15 pages, commit **54c0f6c419fa681e2c1e74a5ad2bb46df787bb93**.

Its accepted PDF is 137,455 bytes with SHA-256:

    93de8c191549fd0ad70f4cf5df970abfbe0ae37d0f0a8b688cbb128577438f79

**P1:** *A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model*, v0.1, commit **273b1a6faaab19ea58748d00576439166eeef9ab**.  
**P2:** *Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate*, v0.1, commit **28e8a85c8fe1e6321328d4d7285b2560d1f98aa9**.

The author asks: “do we have a next mission that has a clear direction to start codex with?” This order supplies that next bounded investigation. Execute the mathematical assessment when the author hands you this packet. No additional scientific approval is needed to investigate the proposed statement. This order does not authorize publication or modification of accepted artifacts.

Work in:

    C:\TORMENT\TRIOCTAGON_new\research\NATIVE_FINITE_CAPACITY_ACCESS_01\

Read READ_ME_FOR_CODEX.md and verify the selected source hashes. Reuse the existing environment and exact local sources where they match. Keep investigation outputs separate. Do not change accepted mathematics, evidence, prior review packages, unrelated local work, repository state or the preserved context files.

## 3. Exact setup

Use P3's original, unscaled exchange equations:

\[
x=(a,b),\qquad \Omega=a+ib,\qquad f(x)=K(a\times b),\qquad J(x)=D_xf,
\]
\[
\dot x=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,
\]
\[
p_t+c(r_c)_s=\mathcal B(\eta_Nf(x)-\kappa z),\qquad
(r_c)_t+cp_s=0,
\]
\[
\dot z=\frac{\kappa}{\beta_R}y,\qquad y=\mathcal B^*p,\qquad \kappa=\eta_R>0.
\]

Retain the complete published registration of \(K\), positive finite geometry and storage parameters, and periodic finite tent profiles. In particular, the contacts' shortest periodic distance is \(2\eta_{\rm geom}\), and \(0<\epsilon_c<\eta_{\rm geom}\); preserve the full circle admissibility rather than only an interval nonoverlap condition. The inherited identities are

\[
\mathcal B^*\mathcal B=mI_2,\qquad
\|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\qquad
\|\mathcal B'v\|_2=\sqrt d\,|v|,
\]
\[
m=\frac{2}{3\epsilon_c},\qquad d=\frac{2}{\epsilon_c^3}.
\]

Fix

\[
\delta_g=\frac{\pi}{4},\qquad
\Omega_0=(1,e^{i\phi},1),\qquad 0<\phi<\frac{\pi}{12},\qquad
p_0=r_{c,0}=z_0=0.
\]

For this published normalized family,

\[
R=|x_0|=\sqrt3,\quad k=\|K\|=G\sqrt{8/7},\quad
G=\kappa_{\rm in}\lambda_g>0,
\]
\[
|f_0|^2=\frac{10G^2\sin^2\phi}{7},\qquad
C_{\rm joint}=\alpha_N(1-\cos\phi)>0.
\]

Use the actual external stock

\[
E_{\rm out}(t)=H_C(t)+H_R(t)=H_N(0)-H_N(t),
\]

and the original weighted norm

\[
U=(p,r_c,z),\qquad
\|U\|_{CR}^2=\|p\|_2^2+\|r_c\|_2^2+\beta_R|z|^2=2E_{\rm out}.
\]

All coefficients are finite and constant along a trajectory. There are no native-map jumps, switched couplings, changed contacts or modified feedback laws in this mission.

## 4. Proposed theorem to assess

Define the positive estimate rates

\[
\boxed{\nu^2=\frac{\eta_N^2mk^2R^2}{2\alpha_N}},
\qquad
\boxed{\sigma_{\rm ext}^2=\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}}.
\]

The symbol \(\sigma_{\rm ext}\) avoids collision with the published port index. The rate \(\nu\) is an analytical estimate scale; do not identify it with a physical native frequency or native \(F\) cadence.

Assume

\[
\boxed{\sigma_{\rm ext}\le\frac{\nu}{2}}.
\]

At the explicit time

\[
\boxed{t_*=\frac1\nu},
\]

the proposed certificate is

\[
\boxed{E_{\rm out}(t_*)>
\frac{1053}{4096}C_{\rm joint}>
\frac14 C_{\rm joint}>0.}
\]

The simple quarter fraction is the substantive target; \(1053/4096\) is the proposed exact proof margin. It is not a fitted physical fraction.

**Quantifiers:** first fix the admissible geometry and all positive finite coefficients satisfying the displayed condition. Then, for every \(0<\phi<\pi/12\), consider that phase's unique coherent empty-launch solution. The same coefficients and \(t_*\) work throughout the phase range, since \(R,\nu,\sigma_{\rm ext}\) are phase independent in this family. This is a family of fixed-parameter trajectories, not a time-dependent selection of parameters or phase.

Prove the regime is nonempty with all parameters finite and positive. A proposed sufficient selection, with all other allowed parameters fixed, is

\[
\eta_N^2\ge
\frac{8\alpha_N}{mk^2R^2}
\left(\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}\right).
\]

Show that this is exactly the intended condition. Retain \(R^2\) in dimensional formulas, even though its normalized numerical value is \(3\).

## 5. Required analytical route and proof obligations

SOURCE_ASSESSMENT.md gives the proposed derivation in detail. Independently check its signs, weights, factors, hypotheses and regularity.

1. **Inherited framework.** Cite the exact model, finite-profile identities, strong empty-launch solution class, storage balance, \(|x(t)|\le R\), \(\|J(x)\|\le kR\), and yaw-specific \(C_{\rm joint}\). P1 Theorem 3.1 is the global solution theorem; P2 Theorem 3.1 is the same-trajectory native-credit theorem. Keep those locators distinct.

2. **Original weighted external estimate.** Derive the unscaled operator
   \[
   \mathscr LU=(-c(r_c)_s-\kappa\mathcal Bz,\,-cp_s,\,
   \kappa\mathcal B^*p/\beta_R)
   \]
   and its skew cancellation in the stated weighted norm. Use the inherited forced-energy argument, deriving the original factors explicitly rather than copying scaled-time factors from P3.

3. **Drive-dependent Volterra comparison.** Differentiate the finite-dimensional drive along the actual native equation:
   \[
   \dot f=-\frac{\eta_N}{2\alpha_N}JJ^Ty.
   \]
   Establish
   \[
   \|U(t)\|_{CR}\le
   \frac{\eta_N\sqrt m|f_0|}{\nu}\sinh(\nu t),
   \qquad
   |f(t)-f_0|\le|f_0|[\cosh(\nu t)-1].
   \]
   Prove the positive-kernel Volterra comparison and the vanishing iteration remainder on finite intervals. Do not assume differentiability of a norm at zero.

4. **Linear-in-time comparison curve.** Use
   \[
   U_{\rm ref}(t)=(\eta_Nt\mathcal Bf_0,0,0).
   \]
   Derive the exact difference equation. Its residual must include both the negative second-carrier term \(-c\eta_Nt\mathcal B'f_0\) and the positive receiver term \(\kappa\eta_Nmtf_0/\beta_R\). The weighted norm of these orthogonal components is \(\eta_N\sqrt m|f_0|\sigma_{\rm ext}t\).

5. **Finite lower bound.** Establish
   \[
   \|U-U_{\rm ref}\|_{CR}\le
   \eta_N\sqrt m|f_0|
   \left[\frac{\sinh(\nu t)}{\nu}-t+\frac{\sigma_{\rm ext}t^2}{2}\right].
   \]
   Justify strong regularity before applying the forced estimate to the difference. Only the first weak tent derivative should be needed. Establish positivity before squaring the reverse-triangle lower bound.

6. **Capacity fraction and exact constants.** Verify the factor
   \[
   \frac{\alpha_N|f_0|^2}{k^2R^2C_{\rm joint}}
   =\frac5{12}(1+\cos\phi)>\frac{13}{16}.
   \]
   Supply exact elementary bounds for \(\cos(\pi/12)>19/20\) and \(\sinh1<19/16\), and derive \(1053/4096>1/4\). Decimal approximations alone do not certify the margin.

7. **Meaning, units and regime.** Check both rates have units of inverse time using the published dimensional conventions, show finite positive nonemptiness, and state precisely what stock and denominator the bound concerns.

These steps are one investigation: a finite-time norm comparison and its quarter-capacity corollary. A shorter rigorous route to the same statement is welcome; document any departure from the proposed proof.

## 6. Interpretation and bounded scope

The target is a fraction of the **joint structural ceiling**, not a fraction of the whole initial native stock. In this family,

\[
\frac{C_{\rm joint}}{H_N(0)}=\frac23(1-\cos\phi).
\]

The fractional statement can be uniform in \(\phi\) while its absolute amount tends to zero as \(\phi\downarrow0\). The theorem would give actual external stock at one time; it would not identify the time of maximum storage or prove ceiling saturation.

Keep P3's published \(\mathcal A_\kappa=M_\kappa/C_{\rm inv}\) unchanged. State this investigation's direct inequality for \(E_{\rm out}/C_{\rm joint}\), rather than reusing that symbol with a new denominator or time.

No receiver-share or later-return claim is part of the target. In particular, do not attach the prior \(80/81\) receiving/recovery fractions to this amount without a separate proof that their parameter conditions overlap on the same solution. That overlap is outside this order.

The intended outward, spreading, around-and-inward geometric route remains the research motivation. This estimate does not register the carrier circle as that spatial circuit. Native \(F\) cadence, six openings, linked gravity–magnetism and later outer geometry remain in the agenda, in their agreed sequence. The author's tentative diversion fraction remains geometric intuition, not a chosen coefficient.

A parameter optimization, numerical trajectory survey, receiver-only theorem, new launch family, physical calibration, new paper or successor investigation is unnecessary here. Stop when the one theorem has a rigorous disposition.

## 7. Evidence and focused verification

The written argument must carry the functional-analytic and comparison claims. Use a small reproducible exact-algebra script for the genuinely useful arithmetic, signs, weights and normalization checks. Do not inflate the check count with duplicate identities or replay the previous 18/12 checks.

Useful checks include the weighted receiver cancellation, both residual coordinates and their norm, the factor in \(\nu^2\), the capacity normalization, the rational cosine and hyperbolic-sine certificates, the final positive margin, and equivalence of the finite parameter condition. A symbolic check does not replace the regularity argument or the Volterra proof.

Record selected-input hashes before and after the investigation and report exactly which scope was protected. Do not imply that unrelated worktree bytes were independently checked unless they were actually inventoried. No Git command is needed for this task.

## 8. Deliverables and verdict

Return a review package containing:

- NATIVE_FINITE_CAPACITY_ACCESS_01_PROOF.md — a self-contained theorem, proof, units, parameter regime and interpretation.
- NATIVE_FINITE_CAPACITY_ACCESS_01_CLAIM_SOURCE_LEDGER.md — inherited facts, new lemmas and final claim, with exact source locators.
- A focused exact-algebra verification script and its machine-readable results, if used.
- INPUT_PRESERVATION.json — stated input scope and before/after hashes.
- COMPLETION_REPORT.md — verdict, exact final hypotheses/constants, any deviation, checks performed and unresolved issue, if any.
- A self-excluded manifest, the complete review ZIP, and its SHA-256 checksum; verify membership, CRC, sizes and hashes.

Use one honest verdict:

- **Established unchanged:** every stated hypothesis and constant survives.
- **Established with documented correction:** list each necessary change and its reason; distinguish the original proposition from the corrected theorem. Do not silently weaken the quarter-capacity objective.
- **Not established / refuted:** provide the concrete gap, obstruction or counterexample and identify which supporting steps remain valid.

If the route fails, pursue only a tightly related correction within the unchanged model and launch. A new physical/geometric choice or materially different question should be reported for GPT/author review, not silently adopted.

Return the completed package for GPT review. Do not commit, push, publish, alter the accepted editions, begin a manuscript, or start a successor investigation.
