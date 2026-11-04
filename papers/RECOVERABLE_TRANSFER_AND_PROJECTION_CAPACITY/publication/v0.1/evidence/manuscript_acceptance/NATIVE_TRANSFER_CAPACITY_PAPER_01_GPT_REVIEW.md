# GPT manuscript review — NATIVE_TRANSFER_CAPACITY_PAPER_01

**Manuscript:** Recoverable Transfer and Projection Capacity in the Reciprocal Chiral Exchange Candidate  
**Edition reviewed:** research manuscript v0.1, 4 November 2026, 15 pages  
**Review date:** 4 November 2026  
**Disposition:** **Accepted for scientific manuscript content, source fidelity and final-artifact quality, unchanged.**  
**Required corrections:** none.  
**Release status:** GPT manuscript review is complete. Author approval and publication closeout remain separate subsequent steps.

This review concerns the exact supplied draft identified below. It does not alter the accepted investigations, the submitted PDF, its editable sources, or the historical evidence. One optional abstract wording refinement is recorded in §7; it is not a condition of acceptance.

## 1. Artifact identity and review basis

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Submitted manuscript review ZIP | 9,031,076 | a9d2e061a96bed75ad8462aeb9d0040d6169c673f9c21bae397557c09c80a4ba |
| Submitted 15-page PDF | 137,484 | 7ef5dfc699ff090be9768dd2e9ef2a0f07cb2fdc82206cc47c26ce07e9a44bf9 |
| Originally issued Codex manuscript packet | 5,438,284 | 1b84d029bcc00ba1a2ea1def397878acd3964f9f3cae64bdf9ea99dfb40fd9d3 |

The standalone PDF and the PDF in the submitted candidate edition are byte-identical. The review package retains the original submission and issued packet as separate evidence, together with the independent checks and fresh page renders.

The mathematical review compared the actual editable manuscript with both accepted proofs and ledgers, their GPT acceptance reports, the defining published P1/P2 sources, and the issued manuscript order. Separate review passes covered the general projection mathematics, the quantitative transfer argument, and the crosswalk/provenance. Root completed the final synthesis and personally inspected all 15 fresh PDF page renders. These are internal analytical and editorial reviews, not an assertion of external peer review.

The source hierarchy is preserved:

- **P1:** A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model, v0.1, immutable commit 273b1a6faaab19ea58748d00576439166eeef9ab.
- **P2:** Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate, v0.1, immutable commit 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9.
- **AT01:** the accepted NATIVE_ACCESSIBLE_TRANSFER_01 proof, claim/source ledger and review evidence.
- **PC01:** the accepted NATIVE_PROJECTION_CAPACITY_01 proof, claim/source ledger and review evidence.
- **Current manuscript:** a faithful combined presentation, with only the authorized immediate synthesis SYN01.

## 2. Structural result: accepted without a scope change

The manuscript places the projection result before imposing the quantitative launch restriction. Theorem 3.1 applies to arbitrary admitted preparations in the inherited global solution class and to every fixed finite positive receiver coupling. Its proof uses the continuously observed port output and the native coordinates' C1 regularity; it does not silently impose H1 preparation on the general structural result. See manuscript §§2.2 and 3.1, equations (2.5) and (3.7)–(3.9).

The registration expansion, kernel direction and rank certificate agree with PC01. The conserved scalar is correctly presented as generally indefinite:

\[
\mathcal J_K=I-2h_e,\qquad h_e=|e\cdot\Omega|^2.
\]

The exact signed debit retains the required factor:

\[
H_N(0)-H_N(t)=\alpha_N\bigl[h_e(0)-h_e(t)\bigr].
\]

Combining this with the published complex bilinear invariant gives the unchanged joint floor and ceiling:

\[
I(t)\ge\max\{|Z_0|,j_0\},\qquad
C_{\rm joint}
=\frac{\alpha_N}{2}\bigl[I_0-\max\{|Z_0|,j_0\}\bigr]
=\min\{C_Z,\alpha_Nh_e(0)\}.
\]

The paper distinguishes empty external preparation, where the debit equals the nonnegative external stock, from preloaded preparation, where the result bounds signed net debit rather than the whole existing external stock. This distinction is explicit in equations (3.5)–(3.6).

Proposition 3.2 correctly includes the feasible-domain condition \(j\ge-|Z|\). It makes no minimum assertion for an empty invariant level. Both equality-state constructions are retained, including negative feasible j, the branch boundaries, Z = 0 and native zero. The minimum is taken in the full native space; the manuscript does not restrict that algebraic optimization to the coherent family or claim that every minimizer lies on a coupled trajectory. See equations (3.10)–(3.14).

The zero-capacity/zero-raw-drive equivalence is complete in both directions. Empty-launch stationarity is properly separated from a nonzero dark core driven by a preloaded carrier. The active coherent witness at yaw \(\pi/4\) preserves the strict positive gap below the old ceiling and the nonzero drive. It is an exclusion of the old ceiling, not a proof that the new ceiling is reached.

The finite-time nonattainment example retains the actual external state at a hypothetical native-zero hitting time. Its forward/backward uniqueness argument is sound and does not assume those external coordinates vanish. It makes no claim excluding infinite-time approach. See manuscript §§3.3–3.4.

**Disposition:** all 22 PC groups are faithfully presented; no required mathematical correction.

## 3. Quantitative transfer: accepted with constants and hypotheses unchanged

The quantitative result uses exactly the specified coherent family

\[
\Omega_0=(1,e^{i\phi},1),\qquad 0<\phi<\pi/12,
\]

with nonzero raw drive and initially empty carrier and receiver. Geometry, profiles, scales, speed, registration, native coupling and phase are fixed before choosing the finite constant \(\kappa\). Different values of \(\kappa\) compare different constant-parameter solutions. This qualification appears before the quantitative theorem and is preserved in the abstract.

The constants A, \(\omega,S,T,\Lambda,D,B_1,B_2,C_1,C_2\), the inherited native threshold, and the sufficient quantitative threshold all match the accepted proof. The two error allocations remain separate:

\[
\kappa_{\rm cert}(q)=
\max\left\{\kappa_{\rm crit},1,
\frac{2B_1}{q\Lambda},
\sqrt{\frac{2B_2}{q\Lambda}}\right\},
\qquad 0<q\le\frac15.
\]

The proof retains the exact finite-coupling scaling, the weighted carrier/receiver norm and the native drift coefficient. It establishes strong regularity of the exact-minus-comparison curve before estimating the residual. Only the first weak derivative of the tent profiles is used. The extension to the full comparison window is justified through the actual error equation and the absolute sine integral \(4/\omega\); it is not an unsupported extension of P2's shorter-horizon conclusion. See manuscript §5.1–§5.2.

Both required positive denominators are proved before normalization: the intermediate total external stock and the intermediate receiver stock. Separate weighted projections give the carrier-small/receiver-large estimates at \(t_\pi\), whereas the endpoint estimate uses the zero of the whole comparison external state. The maximum \(M_\kappa\) is correctly defined on the compact window; its time is not identified with a comparison landmark.

Receiver share and native recovery retain the intermediate total external stock as denominator. Receiver retention uses the intermediate receiver stock. The \(80/81\) recovery and share bounds, the \(1/81\) retention bound, and the absolute recovery inequality are all preserved. No monotonic native recovery over the whole interval is assumed. See Theorem 4.1 and §5.3.

The receiver-power proof retains both linear error terms and their product. Its conversion factor is \(\eta_N^2/\kappa\), distinct from the storage conversion. The native-credit witness is imported separately from P2 Theorem 3.1 with exactly the applicable hypotheses and constants. Initial activity is invoked for each fixed finite coupling, without substituting a coupling-dependent time into a nonuniform short-time expansion.

Continuity supplies a later closed backflow interval with the accepted sign margin. The proof allows further shortening for simultaneous native credit and does not claim an explicit uniform lower bound on the interval width. Every event belongs to the same unchanged solution. See §5.4–§5.5.

**Disposition:** all 29 AT groups are faithfully presented; no required mathematical correction.

## 4. Combination, asymptotics and interpretation

The sole added synthesis is equation (6.2):

\[
M_\kappa\le C_{\rm joint}\le C_Z=C_{\rm inv},
\]

with the last equality confined to the specified coherent launch. Its proof directly applies the joint all-time bound on the window defining \(M_\kappa\). The original accessibility normalization \(M_\kappa/C_{\rm inv}\) remains unchanged; no new ratio using \(C_{\rm joint}\) is introduced.

Explicit finite estimates precede the asymptotic statements. They support a positive inverse-square leading term for the maximum transferred stock, an \(O(\kappa^{-4})\) upper bound for endpoint stock, and \(O(\kappa^{-2})\) errors in the recovery/receiver fractions. All other parameters remain fixed. The manuscript explicitly excludes a monotonicity conclusion at every finite coupling and uniformity as the launch phase approaches zero.

The paper also explains why the \(80/81\) fraction cannot be multiplied by a structural ceiling to infer an established recovered amount. High recovery of the actual transferred stock and a small absolute transferred stock are compatible. Neither an optimized extraction amount nor an exact nonlinear period follows. See manuscript §6.

The geometric programme is carried forward accurately: the central meeting region, opposed cones, outward spread and curved around–inward return, stationary supports and possible transfer elsewhere. The carrier circle, intended tight toroid, close original sphere, extended-line sphere, host-notch N regions and central broken G boundaries remain distinguished. No physical axis, support, opening or receiving site is assigned to the algebraic kernel direction.

The tentative 15–20%, possibly more, remains geometric intuition. It is not a fitted parameter or a consequence of the proved recovery fraction. The subsequent agenda retains useful accessible amount, native cadence, route correspondence and six-opening transport, together with the linked gravity–magnetism, outer-geometry and SRG programme. See manuscript §7 and the unchanged continuity records.

## 5. Sources, crosswalk and integrity

The complete forward crosswalk covers all 51 accepted groups: 29 AT and 22 PC. The 64 reverse substantive labels are accounted for by those groups and the authorized SYN01 combination. Label numbers and pages agree with the actual editable TeX and final compiler auxiliary record.

E01 is applied to the new citations. P2's general model is correctly located in §2, its native-credit theorem in §3, its scaled estimates in §4 and its comparison proof in §5. The manuscript distinguishes P2 Theorem 3.1 from P1's separately cited global-solution Theorem 3.1. Historical proof ledgers remain unchanged.

The independent byte audit checks the submitted outer archive, candidate manifest, originally issued packet and source identities. It confirms the 133-member submission with 132 manifest payloads, the 89-member candidate edition with 88 manifest payloads, and exact preservation of all 60 issued packet members. The 52 protected source-identity records and the accepted proof/review archives are retained intact.

The supplied 63-entry protected-input baseline and final preservation records are reconciled. This is a check of supplied records and the copies available in this review; it is not a fresh audit of the user's Windows filesystem. Final build/source/PDF bindings and the subsequent document, fidelity and visual records refer to the reviewed artifacts.

The historical 18 AT and 12 PC algebra groups remain separate accepted evidence. No new scientific replay, trajectory computation or scientific result is claimed for this manuscript review.

## 6. Final PDF and visual review

Root rendered the submitted PDF afresh with Poppler at 125 dpi and opened every page individually. All 15 pages passed visual review: mathematical symbols, inequality signs, subscripts, equation numbers, page breaks, text margins, the units table and bibliography are legible. No required layout correction was found.

The independent document check confirms:

- 15 A4 pages, with the expected title, author, edition and draft-review metadata;
- 18 embedded fonts;
- 68 internal links whose destinations resolve;
- two external links pointing to the supplied immutable P1/P2 editions;
- no unresolved-reference markers in the extracted text;
- consistent running headers on the body pages;
- no compiler warnings, errors, undefined references or overfull/underfull box diagnostics in the supplied final build log.

The internal references, source locators and visible page numbers were cross-checked with the manuscript. External URL targets were compared with the supplied immutable source identities; this review did not repeat a remote repository publication audit.

The supplied final build receipt binds all ten TeX source files, the build helper and the PDF. Root did not independently compile the manuscript. The artifact check instead combines the bound submitted build record, source review, independent PDF examination and fresh visual rendering.

A page-specific inspection record, render hashes, fresh page images, extracted text and the reproducible read-only document audit are included with this report.

## 7. Editorial disposition and next step

**No required correction is raised.** The paper is accepted unchanged for the scope reviewed here.

One nonblocking precision suggestion concerns the abstract phrase “endpoint stock is of fourth inverse order.” Equations (6.3) and (6.5) state an upper bound \(O(\kappa^{-4})\), without asserting a positive fourth-order leading coefficient. The abstract can therefore be read consistently with the proof. At routine release cleanup, “endpoint stock is bounded by a fourth inverse power” would make the upper-bound meaning immediately explicit. This is optional wording polish, not a mathematical defect or a condition of acceptance.

The draft's “review pending” wording and metadata truthfully record its submission state. This report separately records completion of GPT review against the exact draft hashes. After author approval, the publication closeout can update the release status and verify the resulting artifact before publication.

No submitted input was edited. No Git operation, publication action or successor investigation was performed.

## Evidence supplied with this review

- Original submitted manuscript ZIP and its checksum.
- Original standalone PDF and supplied package-verification receipt.
- Original issued Codex manuscript packet and checksum.
- Independent byte/manifest/crosswalk verification script and result.
- Independent PDF/document verification script and result.
- Root's 15-page visual inspection record, fresh renders and text extraction.
- A self-excluded payload manifest for this GPT review package.

The machine-readable results give exact checked paths and hashes. They complement the written mathematical review; hash agreement and document checks are not substitutes for the proofs.
