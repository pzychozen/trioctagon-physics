# Manuscript review: Same-Trajectory Native Credit

**Manuscript:** Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Reviewed edition:** Research manuscript v0.1, draft for manuscript review, 3 November 2026, 10 pages  
**Review:** GPT internal scientific, source, evidence and typeset-manuscript review, 3 November 2026

## 1. Disposition

**Scientific content accepted at the stated sufficient finite-coupling scope. One minor abstract clarification should be applied before publication.** No changed constant, missing proof step, unsupported extension of the theorem in its formal statement, or visual defect was found.

The manuscript successfully turns the accepted investigation into a readable companion paper. It states the unchanged problem, gives the complete new finite-error argument, and distinguishes local native recovery from cumulative gain, substantial recovered fraction and a completed spatial circuit. The inherited global-solution and initial-activity results are cited and restated at the regularity and hypothesis level needed by the new proof.

The one correction concerns the standalone abstract's phrase “a nonzero coherent launch.” A nonzero native state need not have nonzero chiral drive. The theorem and its declared preparation are already correct. The exact replacement and a minimal source patch accompany this review.

This disposition applies to the exact received PDF and source set identified below. It is an internal review, not external peer review, author approval of publication, physical validation, or a review of a future rebuilt PDF. After the specified correction, the remaining check is a focused comparison of the rebuilt artifact and refreshed records; the mathematics does not need to be reopened.

### Exact reviewed identities

| Item | Bytes | SHA-256 |
|---|---:|---|
| Submitted review ZIP | 2,900,379 | a78ad1027270be98e5bd4bcc36ff700fbf9522ff9f79264a49f11a3b6c65ef3b |
| Standalone and archived PDF | 109,858 | a75ca995bd56c3db940f3e83f2ff3352791f09ebcd01bee119e5b389833bc98e |
| Reviewed manuscript/main.tex | 4,167 | 7f0b466d96e2b429ab5b5dcd4df126ee014de4bd5a3ff2d00ec7c4615187d667 |

The submitted PDF and review archive are retained unchanged under inputs/ in this review package.

## 2. Required editorial clarification

**Issue MC-01 — Abstract, page 1; manuscript/main.tex.**

Replace the sentence:

> Fix the admissible geometry, positive storage scales and native coupling, and a nonzero coherent launch.

with:

> Fix the admissible geometry, positive storage scales and native coupling, and a launch from the specified coherent family with nonzero chiral drive.

This is the only requested manuscript wording change.

The reason is mathematical precision. For example, the aligned native state \(\Omega_0=(1,1,1)\) is nonzero but has \(b_0=0\), so \(a_0\times b_0=0\) and \(f(x_0)=0\). With the external states empty, the displayed equations admit the stationary preparation, so nonzero native amplitude alone does not imply initial supply or later credit. This is a direct reading of the manuscript's equations (2.2) and (2.6), not a new investigation. The formal theorem already selects \(\Omega_0=(1,e^{i\phi},1)\), \(0<\phi<\pi/12\), and equation (2.13) proves that its chiral drive is nonzero for every permitted fixed yaw. [M, §2.3, pp. 3–4; Theorem 3.1, p. 4]

The words “specified coherent family” keep the abstract tied to that preparation. The replacement does not extend the theorem to every coherent state with a nonzero drive.

The package contains corrections/main.tex, the complete original source with precisely this sentence replacement, and corrections/abstract_precision.patch. CORRECTION_IDENTITIES.json binds the original and corrected source bytes. The submitted edition has not been modified and no corrected PDF has yet been built in this review.

## 3. Scientific fidelity

### 3.1 The claim is preserved exactly

For fixed admissible geometry, finite distributed profiles, positive speed, registration, gains and storage scales, positive native coupling, and one phase in the declared launch family, the manuscript retains

\[
\kappa_{\mathrm{crit}}
=\max\left\{1,\frac{4C_1}{D},\sqrt{\frac{4C_2}{D}}\right\}.
\]

All constants are chosen before \(\kappa\), are finite, and \(D>0\). For each fixed finite \(\kappa\ge\kappa_{\mathrm{crit}}\), the same unique solution starting with empty carrier and receiver has initial positive total native power, positive receiver storage and positive receiver power, then satisfies

\[
t_*=\frac{3\pi}{2\omega\kappa},\qquad
P_{NC}(t_*)\le-\frac{\eta_N^2D}{2\kappa}<0.
\]

The continuity interval and integrated gain retain their exact factors:

\[
P_{NC}(t)\le-\frac{\eta_N^2D}{4\kappa}
\quad\text{on }[t_*-\rho_\kappa,t_*+\rho_\kappa],
\qquad 0<\rho_\kappa<t_*/4,
\]

\[
H_N(t_*+\rho_\kappa)-H_N(t_*-\rho_\kappa)
\ge\frac{\eta_N^2D\rho_\kappa}{2\kappa}>0.
\]

The theorem supplies an explicit sufficient regime and finite witness, together with an interval obtained by continuity. It does not assert a necessary or optimal threshold or a uniform quantitative lower bound for the interval width. “Total” refers to the complete signed sum over both native ports. [M, equations (2.8), (3.1)–(3.6), Theorem 3.1; P, R5–R7]

### 3.2 The vulnerable analytical steps remain valid

The review checked the complete new argument against the accepted report and analytical review, with particular attention to these points.

1. **Existence and regularity precede the estimate.** Section 2.2 cites the predecessor's global theorem and states \(C(H^1)\cap C^1(L^2)\) carrier regularity for the empty preparation. The subsequent energy calculation is applied to an existing strong solution. [M, (2.10); F, Theorem 3.1]

2. **The scaling is exact at each finite coupling.** The native derivative retains \(\eta_N^2/(2\alpha_N\kappa^2)\), while original-time native power is \((\eta_N^2/\kappa)f^T\widehat y\). The exact system still has the original positive propagation speed. [M, (4.1)–(4.3); P, R13–R14]

3. **Receiver loading remains in the energy-preserving linear part.** Periodic propagation cancellation and the matched receiver cancellation justify the weighted estimate. The regularized norm \(\sqrt{\|W\|^2+\varepsilon^2}\) correctly handles zero norm. [M, (4.4)–(4.7); P, R15–R17]

4. **The bounds are established for the actual solution first.** Conservation confines the native state to the radius-\(R\) ball, where the derivative and Lipschitz estimates hold. The external and drift estimates are obtained before introducing the comparison. Coherent-domain invariance is not assumed. [M, (4.8)–(4.11); P, R18–R20]

5. **The error's regularity is justified by subtraction.** Both exact and comparison curves already have the required carrier regularity. Their difference therefore supports the energy calculation before its residual is estimated. The propagation residual is negative in the second carrier component and uses only \(\mathcal B'\), an \(L^2\) first weak derivative. No second derivative of a tent or invalid regularity inference is used. [M, §5, (5.4)–(5.6); P, R23–R25]

6. **The complete power product is controlled.** The decomposition uses the actual output in \((f-f_0)^T\widehat y\), so no cross term is omitted. The absolute-sine integral is \(3/\omega\); the resulting error is \(C_1/\kappa+C_2/\kappa^2\); each term is allocated \(D/4\). [M, (5.5)–(5.9); P, R25–R27]

7. **The chronology concerns one solution.** Initial activity is invoked at each fixed finite coupling, and its positive interval is shortened to precede the later credit interval. The short-time expansions are not evaluated at \(T/\kappa\) and need not be uniform in \(\kappa\). Uniqueness links the two stages without a reset or prepared negative carrier state. [M, (5.10) and proof completion, pp. 7–8; P, R28]

The crosswalk is complete: all 30 accepted report entries R1–R30 and all 28 ledger entries STR01–STR28 are present. All 65 manuscript labels agree with the source declarations, label inventory and final auxiliary record. All 47 displayed equations and the theorem are covered. The manuscript's units table is consistent with the accepted certificate, including the distinction between drift constant \(A\), amplitude unit \(\mathrm A\), and registration matrix \(A_{\rm reg}\). [M, Appendix A; E, verification/LABEL_CROSSWALK.json]

### 3.3 The interpretation stays within the result

The paper preserves the essential distinctions.

- **Local recovery and cumulative accounting:** \(H_N(0)-H_N(t)=H_C(t)+H_R(t)\ge0\). A positive native increment during the return interval does not raise native storage above its initial stock. [M, (6.1)]

- **Native credit and receiver power:** The exact theorem establishes initial receiver charging and later total native credit. The negative receiver dot product at the comparison witness is explicitly identified as a comparison statement. The given threshold is not claimed to establish \(P_{CR}(t_*)<0\) on every exact solution it covers. [M, §6.1, (6.2)]

- **Absolute amount and returned fraction:** The external-stock estimate is \(O(\eta_N^2/\kappa^2)\) on fixed scaled windows. The witnessed power has the accepted leading term and remainder. These are not long-time decay statements; they do not determine a returned fraction without a numerator, denominator and interval. [M, §6.2, (6.3)–(6.4); P, R29]

- **Invariant ceiling and attainable transfer:** The approximately 3.4074% maximum-span ceiling remains a net-extraction bound relative to initial core trial storage. It is not an achieved transfer, receiver share, diversion percentage or amount of repeated gross work. [M, §6.3, (6.5)–(6.6); P, R30]

- **Energetic return and spatial route:** \(t_* /(L_c/c)\to0\) as coupling increases with other parameters fixed. The collocated finite-profile certificate does not establish a completed circuit around the intended toroidal route. [M, §7, (7.1)]

These qualifications appear in the manuscript itself and are not confined to supporting documentation.

## 4. Independent PDF inspection

The reviewer rendered the received standalone PDF independently with Poppler at 130 dpi and visually inspected every page. The supplied Codex renders were not substituted for this review. The PDF identity was checked before rendering and agrees with the archived copy.

| Page | Material inspected | Finding |
|---|---|---|
| 1 | Title, subtitle, author accents, date/status, full abstract, contribution note | Readable and complete. MC-01 is a wording clarification; no layout defect. |
| 2 | Introduction, registration, two-port map, periodic tents and adjoint | Formulas, symbols, references and margins clear. Continuation to page 3 is coherent. |
| 3 | Profile norms, boxed system, stores, powers, balances, regularity and preparation | Signs and factors visible. Long storage line fits. Launch preparation is present below its heading. |
| 4 | Gram matrix, nonzero drive, constants, threshold and complete theorem | All constants and theorem inequalities readable. The witness, interval and gain are on the same page. |
| 5 | Scaling, weighted external norm, operator, cancellation and forced estimate | Factors, subscripts, integral limits and norm regularization clear. |
| 6 | Ball bounds, external bound, native drift, comparison and start of error regularity | Equations and proof organization readable. Continuation to page 7 retains the argument. |
| 7 | Error regularity, residual, finite error, complete power estimate and initial expansions | First derivative, negative sign, two error terms and coefficient denominators clear. |
| 8 | Chronology and proof completion; cumulative account, receiver qualification and scale | Proof end is clear. Returning-sign scope and fixed-window bounds readable. |
| 9 | Capacity ceiling, geometric meaning, continuation and contributions | Initial-stock denominator and geometry distinctions clear. Contribution paragraph continues normally. |
| 10 | Contributions completion, dimensional table and references | Table fits; all entries, bibliography text and author accents readable. Footer and references clear. |

No clipped text, overlapping equations, missing visible glyphs, unreadable table, broken page numbering or material typesetting defect was found. Minor normal paragraph continuations across pages do not impair the argument.

Independent structural inspection confirmed 10 A4 pages, 18 embedded fonts, 17 resolved bookmarks and 58 link annotations. Internal targets resolve and the three relative evidence targets exist in the complete edition. Those relative files accompany the edition; a detached PDF alone does not contain them. The baseline URL is pinned to the specified commit. This review did not make a new network request to that URL.

The independent render hashes and page notes are in INDEPENDENT_VISUAL_INSPECTION.json, and the structural record is INDEPENDENT_PDF_CHECKS.json.

## 5. Package, source and provenance review

The following were independently checked against actual supplied bytes.

| Check | Result |
|---|---|
| Finished ZIP checksum, member safety, uniqueness and CRC | Pass; 90 members |
| Outer manifest coverage, sizes and hashes | Pass; 89 payloads plus the self-excluded manifest |
| Candidate edition manifest | Pass; 56 payloads plus its self-excluded manifest |
| Standalone PDF versus archived PDF | Byte-identical |
| Ten TeX sources and build helper versus both build receipts | Match |
| PDF and source identities in crosswalk and visual records | Match |
| Accepted investigation evidence versus its original archive | All 26 members unchanged |
| Seven predecessor files versus previously verified published copies | All unchanged |
| Actual analytical review and issued manuscript order | Exact original bytes |
| Earlier replay summary and exact replay results | Exact original bytes |
| Received manuscript packet versus the packet issued for this task | Byte-identical |
| Final successful compiler and TeX logs | No warning diagnostics |
| Historical 78-file preservation record versus recorded baseline | Consistent within the supplied records |

The new ledger and source inventory correctly distinguish the seven published predecessor files at commit 273b1a6faaab19ea58748d00576439166eeef9ab from the later ORDER, CONTEXT, investigation, analytical review and manuscript-order inputs. The original historical ledger is preserved unchanged. The approved source-heading clarification is therefore implemented correctly. [E, CLAIM_SOURCE_LEDGER.md, SOURCE_IDENTITIES.json and PROVENANCE.md]

The manuscript also counts the historical algebraic verification correctly: **25 distinct exact-algebra checks, independently replayed**. The manuscript preparation and this manuscript review did not perform a new scientific replay. Archive, document and source assertions are not additional scientific identities.

### Limits of this verification

The received artifacts were directly read, hashed, structurally inspected and rendered. The Windows compilation is supported by its supplied logs and matching source/helper/PDF receipts; it was not independently rerun here. The historical 78-file Windows preservation report was checked for internal consistency, while the retained files were independently compared with their accepted originals. This review does not claim live access to or a repository-wide audit of the author's Windows machine.

The supplied successful build records the correction of an earlier cached-font compilation failure. That failed attempt does not affect the final PDF's clean build record or inspected pages.

No submitted scientific evidence or manuscript was altered during review. The separate corrected main.tex is a proposed editorial replacement, clearly distinguished from the reviewed source.

## 6. Research direction carried forward

The paper retains the collaborative geometric direction: a central starting/meeting region, opposed cones, outward spreading and curvature around an intended tight toroidal arrangement, inward return and possible transfer elsewhere. Stationary supports remain stationary. The carrier circle, intended toroid, close original sphere and extended-line sphere remain distinct; finite host-notch N regions remain distinct from the six central broken G boundaries. Excluding exact O does not exclude every finite central region. The author's tentative 15–20%, possibly more, remains geometric motivation rather than a fitted target or a deduction from the extraction ceiling. [M, §7, p. 9]

The next scientific stage remains **accessible transfer and receiver behavior**, followed by native stepping/cadence, intended route correspondence and six-opening transport. Gravity–magnetism remains linked across the programme, with outer Tri-Octagon geometry and further justified SRG integration later. New geometry should continue to be developed collaboratively where a genuine directional choice is needed. The accepted agenda is not replaced by the fast collocated comparison. [M, §7; O, research-continuation requirements]

The immediate step is the single editorial correction and final document closeout. Publication follows manuscript and author approval; the next investigation follows publication. This review does not start a new scientific work order.

## 7. Completion path

Use the accompanying NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_EDITORIAL_CLOSEOUT_ORDER.md.

Its scope is deliberately small: apply MC-01 using the supplied corrected source or exact patch, rebuild the document, inspect the resulting PDF, refresh its source/label/visual/package identities, and return the revised package for a focused final artifact check. Preserve the accepted proof and all historical evidence.

No additional theorem, trajectory computation, coupling regime or scientific replay is required for this correction. All scientific findings in this review remain accepted unless some later edit changes the mathematics.

## 8. Source key and review records

**M — Reviewed manuscript.** [Exact submitted PDF](inputs/SAME_TRAJECTORY_NATIVE_CREDIT_v0.1.pdf), identified in §1. Its ten TeX sources are inside the exact submitted package.

**E — Submitted complete edition.** [Exact original review package](inputs/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_REVIEW_PACKAGE.zip). Edition prefix: candidate_edition/papers/SAME_TRAJECTORY_NATIVE_CREDIT/publication/v0.1/.

**P — Accepted proof.** E/evidence/investigation/NATIVE_SAME_TRAJECTORY_RETURN_01_PROOF.md, SHA-256 841b5e3a35d0f32cf083388eb1c4a07a60ac8075bc7f622ada76fe1f7591d39b.

**A — Prior GPT analytical acceptance.** E/evidence/current_gpt_review.md, SHA-256 220669c0d6a503f7cdebfda6385df7ee26bdd3404cd251f0a1d010212c0e1709. This is the earlier analytical review, distinct from the present manuscript review.

**O — Issued manuscript order.** E/evidence/manuscript_order.md, SHA-256 a6e92229a4f4e2a14406d6852be9777ed0e784be9a47f1a7013d7137235dbc3e.

**F — Published mathematical foundation.** A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model: Well-posedness, matched storage, and extraction limits, v0.1, commit 273b1a6faaab19ea58748d00576439166eeef9ab. The seven complete defining files are retained in E/evidence/investigation/sources/ and were byte-compared with the previously verified copies.

**Independent records:** INDEPENDENT_PACKAGE_CHECKS.json; INDEPENDENT_PDF_CHECKS.json; INDEPENDENT_VISUAL_INSPECTION.json; CORRECTION_IDENTITIES.json; REVIEW_EXECUTION.md; the read-only review scripts and independent renders. The reviewer ZIP manifest and adjacent checksum bind this review package.
