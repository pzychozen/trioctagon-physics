# GPT review of same-trajectory native return

**Investigation:** NATIVE_SAME_TRAJECTORY_RETURN_01  
**Review date:** 3 November 2026, Atlantic/Reykjavik  
**Author and research direction:** Hilmir Frímann Halldórsson / pzychozen  
**Analytical report:** Codex  
**Review:** GPT, project-internal mathematical and evidence review  
**Disposition:** **Accepted at the stated sufficient finite-coupling scope. The proposed constants and threshold are correct. No mathematical correction or additional scientific run is required to close this investigation.**

One minor provenance wording clarification is recorded in section 5. It does not affect the result or block acceptance. The supplied proof, ledger and package have been preserved unchanged.

## 1. The result now established

The unchanged reciprocal chiral exchange candidate has a declared family of initially empty launches that first supply native trial storage and later recover some of it on the same solution. This is a new dynamical result beyond the earlier prepared-credit proposition.

Fix the admissible periodic geometry, finite-width disjoint tent profiles, positive speed, fixed registration, positive storage scales, native coupling and one coherent preparation

\[
\Omega_0=(1,e^{i\phi},1),\qquad 0<\phi<\pi/12,
\qquad p(0)=r_c(0)=z(0)=0.
\]

Let the constants have exactly the definitions in the report's R5. They are independent of the receiver coupling \(\kappa=\eta_R\). For each fixed finite

\[
\kappa\ge\kappa_{\rm crit}
=\max\left\{1,\frac{4C_1}{D},\sqrt{\frac{4C_2}{D}}\right\},
\]

the same global exchange solution initially satisfies \(P_{NC}>0\), \(H_R>0\) and \(P_{CR}>0\) for sufficiently small positive time. At

\[
t_*=\frac{3\pi}{2\omega\kappa},
\]

it satisfies the strict total-power certificate

\[
\boxed{P_{NC}(t_*)\le-\frac{\eta_N^2D}{2\kappa}<0.}
\]

Continuity supplies a nonzero later interval with positive native-storage recovery. Specifically, the report correctly obtains some \(0<\rho_\kappa<t_*/4\) with

\[
P_{NC}(t)\le-\frac{\eta_N^2D}{4\kappa}
\quad\text{on }[t_*-\rho_\kappa,t_*+\rho_\kappa],
\]

\[
H_N(t_*+\rho_\kappa)-H_N(t_*-\rho_\kappa)
\ge\frac{\eta_N^2D\rho_\kappa}{2\kappa}>0.
\]

The witness time and power margin are explicit. The interval width exists by continuity; the report makes no claim of an explicit uniform lower bound for that width. Parameters remain constant, and no state is reset or separately prepared.

The original candidate remains a proposed extension alongside the native kernel. This acceptance establishes a mathematical behavior of that candidate, not physical energy calibration, external peer review, adoption into the native kernel, or a spatial circuit.

**Primary new sources:** [Codex proof, R1–R30](https://chatgpt.com/library?file_id=libfile_1b4edae6f044819181811cfca5656515&account_id=personal); [claim/source ledger, STR01–STR28](https://chatgpt.com/library?file_id=libfile_6d6da89fcb2c81918968a2f53929dcab&account_id=personal).

## 2. Mathematical review

### 2.1 The source equations and preparation are retained

R1–R4 agree with the fixed edition at commit `273b1a6faaab19ea58748d00576439166eeef9ab`: raw chiral drive, two-port ordering, normalization, reciprocal coefficient one-half, negative receiver loading, periodic carrier and empty preparation. No contact-tangent sign is inserted into the drive.

The registration calculation is correct:

\[
KK^T=G^2\begin{pmatrix}1&1/7\\1/7&1\end{pmatrix},
\quad k=\|K\|=G\sqrt{8/7},
\quad G=\kappa_{\rm in}\lambda_g.
\]

For the declared coherent preparation, \(R=|x_0|=\sqrt3\) and

\[
|f_0|^2=\frac{G^2\sin^2\phi}{7}(6+8\sin^2\delta_g)>0.
\]

This proves \(D>0\) for every fixed yaw under the stated positive-gain assumptions. The proof needs at least one nonzero port, not both separately. It does not assume that the coherent launch family remains invariant.

The two disjoint tents give

\[
m=\frac2{3\epsilon_c},\qquad d=\frac2{\epsilon_c^3},\qquad
\mathcal B^*\mathcal B=mI_2,\qquad
\|\mathcal B'v\|_2=\sqrt d\,|v|.
\]

The bounds \(|f(x)|\le k|x|^2/2\) and \(\|J(x)\|\le k|x|\) are valid. Conservation with empty external stores keeps \(|x|\le R\), so the needed Lipschitz bound is on a convex Euclidean ball. Old coherent-domain preservation is not used.

**Locators:** report R1–R4, R10–R13; ledger STR01–STR08; published `candidate.tex`, `power.tex`, `wellposed.tex`, `activity.tex`.

### 2.2 The comparison is attached to an actual finite-coupling solution

The scaling

\[
\tau=\kappa t,\qquad
(p,r_c,z)=\frac{\eta_N}{\kappa}
(\widehat p,\widehat r,\widehat z)
\]

is exact. It gives core drift proportional to \(\kappa^{-2}\), propagation proportional to \(\kappa^{-1}\) on the scaled time, and

\[
P_{NC}(\tau/\kappa)
=\frac{\eta_N^2}{\kappa}f(x_\kappa(\tau))^T\widehat y(\tau).
\]

The actual original-time propagation speed stays fixed and positive. A finite \(\kappa\) is selected once before launch.

The explicit comparison is correctly solved from zero external data. With \(\omega^2=m/\beta_R\), it has

\[
\widehat p^{(0)}=\mathcal Bf_0\frac{\sin(\omega\tau)}{\omega},
\qquad \widehat r^{(0)}=0,
\qquad \widehat z^{(0)}=f_0(1-\cos(\omega\tau)).
\]

At \(T=3\pi/(2\omega)\), its total coefficient equals \(-D=-m|f_0|^2/\omega\). The proof subsequently bounds the actual finite solution's difference from this comparison. It does not treat the comparison as the desired trajectory.

**Locators:** report R14–R15, R21–R22; ledger STR09 and STR13.

### 2.3 The energy-space regularity argument is sufficient

This is the most consequential rigor check in the proof. The published global theorem supplies the actual carrier's

\[
C_\tau H^1_s\cap C^1_\tau L^2_s
\]

regularity for each fixed finite coupling. The explicit comparison is also a strong curve. Their difference therefore has the regularity needed for the energy calculation before any estimate from its residual is invoked.

In the external norm

\[
\|(q,h,v)\|_{CR}^2=\|q\|_2^2+\|h\|_2^2+\beta_R|v|^2,
\]

periodic integration by parts cancels propagation, while adjointness cancels the receiver loading and receiver-state work. R17 is correct. The regularization by \(\sqrt{\|W\|_{CR}^2+\varepsilon^2}\) then proves R18 without division by a vanishing norm.

The residual contains only the first weak spatial derivative \(\mathcal B'f_0\in L^2\). It need not be \(H^1\). That is sufficient because the strong regularity of the difference is already known by subtraction. No second tent derivative, unproved operator-norm limit, or circular inference of regularity is used.

**Locators:** report R9, R16–R18, R23–R25; ledger STR04, STR10 and STR14–STR15.

### 2.4 Both error constants are correct

With \(F_{\max}=kR^2/2\), the exact finite-solution estimates are

\[
\|V_\kappa(\tau)\|_{CR}\le\sqrt mF_{\max}\tau,
\qquad |\widehat y(\tau)|\le mF_{\max}\tau,
\]

\[
|f(x_\kappa(\tau))-f_0|\le\frac{A\tau^2}{\kappa^2},
\qquad A=\frac{\eta_N^2k^2R^2mF_{\max}}{4\alpha_N}.
\]

The factor one-fourth includes both the feedback factor one-half and integration of the linear time bound. The negative propagation residual in the second carrier component is

\[
-\frac c\kappa\mathcal B'f_0
\frac{\sin(\omega\tau)}{\omega}.
\]

The absolute sine integral through \(T\) is \(3/\omega\), yielding

\[
\|V_\kappa(T)-V_0(T)\|_{CR}
\le\frac{3c\sqrt d\,|f_0|}{\kappa\omega^2}
+\frac{\sqrt mAT^3}{3\kappa^2}.
\]

R26 correctly decomposes the power error using the actual output \(\widehat y\) in its first term. There is no missing product error. The complete two-port bound is

\[
|Q_\kappa+D|\le\frac{C_1}{\kappa}+\frac{C_2}{\kappa^2},
\]

\[
C_1=\frac{3c\sqrt{md}|f_0|^2}{\omega^2},\qquad
C_2=mAT^3\left(F_{\max}+\frac{|f_0|}{3}\right).
\]

The proposed threshold allocates at most \(D/4\) to each error and therefore leaves the required \(-D/2\) margin. The units also check: \(A\) has drive divided by time squared, \(D,C_1,C_2\) have power units, and both threshold ratios are dimensionless.

**Locators:** report R5, R19–R20, R23–R27 and section 6 unit table; ledger STR11–STR17 and STR22.

### 2.5 The earlier and later intervals belong to the same solution

The threshold estimate proves the negative witness for each finite fixed coupling. The published launch proposition is applied separately to that same solution and coupling. Its small-time remainder need not be uniform in \(\kappa\), and the proof never evaluates that nonuniform expansion at \(T/\kappa\).

The initial positive interval can be shortened to lie before \(t_*/4\). Continuity permits a closed later interval within \((3t_*/4,5t_*/4)\) retaining half the witness margin. The integrated gain coefficient in R7 is correct. Global uniqueness identifies these as stages of one trajectory.

This proves the assigned endpoint without prepared negative carrier data or a time-reversal argument.

**Locators:** report R6–R7, R28 and section 5; ledger STR17–STR20.

## 3. Meaning and limits of the accepted theorem

The positive result is that the candidate's reciprocal interface actually develops total native credit after an initially empty launch. The previous paper's separately prepared credit state is no longer the only established route to a returning sign.

The following qualifications are substantive and correctly retained:

| Question | Accepted conclusion |
| --- | --- |
| Is the result about both native ports together? | Yes. The certificate bounds the full signed dot product. |
| Is the receiver active? | Yes. Initial exact receiver storage and receiver power are strictly positive for sufficiently small positive time. |
| Does every positive receiver coupling give return? | Not established. The threshold is sufficient, finite and conservative; no optimality or necessity is claimed. |
| Does native storage exceed its initial stock? | No. Empty external preparation and conservation give \(H_N(t)\le H_N(0)\) and cumulative debit \(H_C+H_R\ge0\). |
| Is exact receiver power negative at the native-credit witness? | Not established by this threshold. Negative comparison receiver power is distinguished from a finite-solution theorem about \(P_{CR}(t_*)\). |
| Is the amount or fraction recovered quantified substantially? | A positive interval gain is proved, with continuity determining its width. No substantial return fraction or capacity attainment is established. |
| Is a spatial circuit completed? | Not established. The witness is fast collocated exchange and can occur arbitrarily early relative to \(L_c/c\). |

R29 gives an external-storage upper bound of order \(\eta_N^2/\kappa^2\) on fixed scaled windows, while the witnessed native power is

\[
-\eta_N^2D/\kappa+O(\eta_N^2/\kappa^2)
\]

with the other parameters fixed. These statements are correctly scoped to the scaled windows. They are not large-time decay claims. A small absolute transferred amount does not by itself determine what fraction of that amount is returned; a fraction requires a specified numerator, denominator and time window.

The conserved \(Z_2\) and initial coherent-span ceiling remain compatible with the new recovery interval. The approximately 3.4074% figure bounds net extraction relative to initial core trial storage at the stated maximum phase span. It is not an achieved fraction, gross-work bound, receiver share or the author's tentative diversion share.

The central starting/meeting region, opposed cones, intended outward–around–inward toroidal route and stationary supports remain the geometric direction. The carrier circle, tight toroid, close sphere, extended-line sphere, finite host-notch \(N\) regions and central broken \(G\) boundaries retain their distinct meanings. Exact-point \(O\) exclusion is not expanded into exclusion of every finite central region.

## 4. Independent evidence and package checks

### 4.1 Received archive and source bindings

The supplied archive is **86,820 bytes**, SHA-256:

`c832f8f5a49ba88f77260aa7aaf02331af9a1da68c574eedfc68cad7eb1c67d3`

Independent checks confirm:

- **26 archive members:** 25 hashed payloads and the self-excluded member manifest.
- Exact member coverage, unique safe paths, CRC reading, every payload size and every payload SHA-256.
- Exact agreement of the standalone proof and ledger with their archived copies.
- Exact agreement of the retained work order with the one issued in this conversation, and of the retained standalone context with the recovered handoff's `START_HERE.md`.
- All **seven defining publication files** match their source record, the preserved handoff edition, and the previously directly retrieved commit-pinned bytes and Git blob identities.
- The preservation record's nine entries are internally consistent with the received retained files.
- The Codex review record binds the actual final proof, ledger, source record and symbolic result bytes.
- The report has R1–R30 once each, and the ledger has STR01–STR28 once each.

The live Windows before/after preservation is Codex's recorded execution. This review does not claim access to that machine or a new repository-wide audit. Fresh remote retrieval was unnecessary because exact source bytes and commit identities were already independently recovered in this conversation. The separately external `PACKAGE_VERIFICATION.json` was not attached; direct received-archive verification supplies the review's integrity evidence.

Details are in `INDEPENDENT_PACKAGE_CHECKS.json` and its reviewer script.

### 4.2 Independent exact-algebra replay

After inspecting the complete symbolic helper, I copied it unchanged into a separate reviewer directory and executed it. **All 25 exact checks pass.** Their identifiers, descriptions, residuals, unit exponents and helper identity match the submitted result.

Helper SHA-256:

`7b4ca738f237ad2151876020646258d65c71b8eb241edc30e65da7a0326c748a`

Codex's recorded environment was Windows Python 3.11.15 / SymPy 1.14.0. This independent replay used reviewer Python 3.12.14 / SymPy 1.14.0. The initial reviewer interpreter lacked SymPy and failed before running any check. SymPy 1.14.0 and mpmath 1.3.0 were then installed only into an isolated scratch dependency directory; the submitted helper and results were not modified.

This is a replay of the same 25 checks, not 25 additional distinct identities. Symbolic checks support exact algebra and coefficient collection. They do not replace the analytical arguments for regularity, norm inequalities, admissibility, continuity or the theorem.

`SYMBOLIC_REPLAY_REVIEW.json` records the comparison. The unchanged helper, actual replay result and stdout are retained in `reviewer_replay/`. No trajectory, carrier simulation, native update, source redesign, Git operation or publication was performed during this review.

## 5. One nonblocking provenance wording clarification

The ledger's opening says that all source IDs in its table refer to files at the publication commit. Its table also includes **ORDER** and **CONTEXT**, which are subsequent investigation inputs. Their actual roles and identities are correctly documented elsewhere.

A precise replacement for that introductory sentence is:

> The seven published source IDs CANDIDATE through ACCEPTED_PROOF refer to unchanged complete files at edition commit `273b1a6faaab19ea58748d00576439166eeef9ab`. ORDER and CONTEXT identify the later investigation inputs retained separately in SOURCE_IDENTITIES.json.

This clarification does not change a source byte, equation, proof dependency or theorem. It can be incorporated in a later editorial version without reopening the mathematical investigation. The supplied ledger remains unchanged in the reviewed package.

Codex also correctly disclosed that the full earlier handoff and separate publication review were unavailable in its focused local search. The defining seven source files and exact new order were present and matched. The missing contextual review therefore creates no mathematical dependency gap.

## 6. Research disposition and continuation

**Priority 1 is complete at its declared sufficient-regime scope:** later total native credit is established on the same initially empty exchange solution. The broader classification of return for arbitrary prescribed couplings remains open, as expected.

The next agenda direction remains **accessible transfer and receiver behavior**. This theorem makes it useful to distinguish the amount initially supplied, the amount recovered over a declared interval, current receiver retention, carrier storage and repeated gross exchange. The exact later receiver-power sign is also a separate quantity to establish where useful. Those questions precede native stepping and cadence, then spatial route and six-opening correspondence.

Gravity–magnetism remains linked across the programme; outer Tri-Octagon geometry and further justified SRG integration remain standing later directions. The completed earlier publications remain foundations. No new work order or publication action is part of this review.

The author need not reconstruct coefficients or supply a new geometric assumption for this acceptance. GPT and Codex can continue from the equations and retained source evidence. Author intuition should be requested when a concrete spatial ambiguity, new geometric assumption or direction-changing interpretation is reached.

**Final disposition: the theorem and its unchanged constants are accepted internally. The assigned mathematical investigation is closed; the single ledger wording clarification is nonblocking.**
