# GPT manuscript and proposed-payload review
## Finite-Time Access to Native Projection Capacity in the Reciprocal Chiral Exchange Candidate, v0.1

**Review date:** 4 November 2026, Atlantic/Reykjavik  
**Research author and direction:** Hilmir Frímann Halldórsson (pzychozen)  
**Reviewer:** GPT, project-internal manuscript and evidence review

## Disposition

**The 11-page manuscript and its exact PDF are accepted unchanged.** The scientific presentation, hypotheses, rates, strict constant, quantifier order, complete argument, units, interpretation and geometric outlook faithfully preserve the accepted investigation. All eleven freshly rendered pages have been visually inspected; no required PDF, LaTeX or layout correction was found.

**The proposed publication metadata needs one small correction, XW-01:** repair character encoding in the generated `verification/CROSSWALK.json`. The exact reviewed replacement and diff are supplied. This changes no mathematics, PDF, TeX source, destination locator or preserved original evidence. No PDF rebuild or scientific replay is required. Correct the active metadata and refresh its hash-dependent records before publication.

**The reported input-archive exception is reconciled at source level.** An independently available original packet matches the stated checksum, and all 74 original members match the returned copies exactly. A different received ZIP is not retroactively declared to have matched that checksum. The separate reconciliation receipt preserves this distinction.

**Stage B remains locked pending explicit author publication GO.** This review accepts the actual manuscript and the stated metadata repair; it neither performs Git operations nor treats Codex's checks as publication permission. The correction can be closed within an explicitly authorized Stage B order without another manuscript round.

## 1. Artifact identities

| Object | Bytes | SHA-256 |
|---|---:|---|
| Submitted Stage A review ZIP | 3560096 | `53fee5678e508d8ff07e36e48109b423dace9a1a08350338e45969476d3717d3` |
| Accepted manuscript PDF | 110500 | `e337a9b59488b7f1dc4ac1371150e7b5d69d168d7b230dcd665ccb61bade1318` |
| Submitted candidate manifest | 20056 | `c8832b6fcc811ffff8276da0a4d57b58e9ad4d0f4650186c5b6522339e087aea` |
| Submitted prospective allowlist | 29788 | `5f483ad685c2cbd5b2e3e3ed5e148cbedfde57ec7eb3fc07ca4bfeb1f505b338` |
| Submitted generated crosswalk | 41800 | `bb281be227450cc753de9ffe3bfb2963395b8aee0ab108caa2a3c939c5595dc6` |
| Reviewed XW-01 replacement crosswalk | 41639 | `b7e22b38e18e4911cbcda19c38e758af82617c108020d2829487e9a6574d1b8c` |

The accepted PDF is at `candidate_edition/papers/NATIVE_FINITE_CAPACITY_ACCESS/publication/v0.1/NATIVE_FINITE_CAPACITY_ACCESS_v0.1.pdf` in the unchanged submission. The manifest and allowlist above describe the submitted Stage A candidate, not a future corrected/publication tree. Their active successors must be recomputed after XW-01 and publication-wrapper additions.

## 2. Scientific fidelity

The manuscript was read in full, alongside the accepted proof FA01–FA26, scientific review, issued manuscript order, selected predecessor sources and manuscript claim/source ledger. This is review of the typeset presentation, not a new scientific investigation.

### Setup and theorem — Sections 2–3, pages 2–4

The raw two-port order, fixed registration at yaw pi/4, positive finite gains, periodic circle, whole-circle shortest separation and finite H1 tent profiles are preserved. The original unscaled equations have the correct factors and receiver loading sign. Quadratic native trial storage remains distinct from the native quartic potential.

The launch is exactly Omega_0 = (1, exp(i phi), 1), with 0 < phi < pi/12 and empty carrier/receiver. The drive vector is nonzero and the joint ceiling is alpha_N(1 - cos(phi)). The paper does not assume the launch family or its phase sector remains invariant.

Theorem 3.1 and equation (3.3), page 4, retain

    nu^2 = eta_N^2 m k^2 R^2 / (2 alpha_N)
    sigma_ext^2 = c^2 d / m + kappa^2 m / beta_R
    sigma_ext <= nu/2,    t_* = 1/nu
    H_C(t_*) + H_R(t_*) > (1053/4096) C_joint > C_joint/4 > 0.

The admitted geometry and finite coefficients are fixed before the phase. The same coefficients and time work for every phase in the declared open interval. Equality in the sufficient rate condition is allowed. There is no reset, coefficient switch, native jump or assertion of a necessary/optimal condition.

### Strong solution and weighted estimate — Section 4.1, pages 4–5

P1 Theorem 3.1 is correctly distinguished from P2's native-credit theorem and P3's projection theorem. The known solution has strong carrier regularity before the energy estimate. Periodic Sobolev product integration and the receiver's beta_R weight give the exact cancellation. The regularized norm calculation (4.5) justifies (4.4) at zero without division by a vanishing norm.

### Evolving-drive comparison — Section 4.2, pages 5–6

Equation (4.6) retains the actual derivative `dot f = -eta_N JJ^T y/(2 alpha_N)` and the original coupling factors. The nonnegative Volterra-kernel argument explicitly iterates its inequality and controls the remainder by `M_T (nu T)^(2n)/(2n)!`. Its vanishing on a fixed finite interval is justified in prose. No differential inequality for a nondifferentiable norm is assumed.

The bounds preserve the factor |f_0|. That is crucial when normalizing by a capacity that tends to zero near the excluded phase endpoint. The phase-wise preliminary remainder bound is not misrepresented as an assumed phase-uniform bound.

### Reference residual and finite error — Section 4.3, page 6

The reference curve is a proof device, not an altered actual system. The difference is strong before the residual is estimated. Equation (4.12) includes both the negative propagation term in the second carrier coordinate and the positive receiver component, even though the reference receiver coordinate itself is zero. Their weighted orthogonality gives exactly sigma_ext. Only the first weak profile derivative is used. Equation (4.14) includes both the external residual and changing native drive.

### Strict margin and nonempty regime — Sections 4.4–5, pages 6–7

The reverse-triangle bound is squared only after proving its bracket positive. The exact inequalities `sinh(1) < 67/57 < 19/16` and `cos(pi/12) > 19/20` retain their strictness arguments. The normalized factor is `(5/12)(1 + cos(phi)) > 13/16`; cancellation of `1 - cos(phi)` occurs only at positive phi. Equation (4.22) gives `1053/4096 = 1/4 + 29/4096` with no numerical approximation carrying the proof.

Section 5 keeps the exact equivalent finite eta_N condition, including equality. It establishes a nonempty positive finite regime without setting propagation or receiving to zero. Neither estimate rate is identified as a physical oscillation frequency or native-map cadence.

### Interpretation, units and contribution — Sections 6–7 and Appendix A, pages 8–10

The numerator is carrier-plus-receiver storage at one specified time; the denominator is joint capacity, not the complete initial native stock. Equation (6.1) and the small-phase upper bound correctly preserve the possibility of vanishing absolute stock.

The earlier 80/81 receiving/recovery theorem is not attached to this amount without a same-parameter argument. Receiver-only allocation, subsequent recovery of this amount, monotonic extraction, maximum time, saturation and spatial circuit completion remain unproved here. P3's original accessibility statistic retains its own denominator and window.

The dimensional table and equation (A.1) retain the amplitude dimension of R and both inverse-time rates. The central meeting region, opposed cones, spreading and curved return, stationary supports, N/G distinctions and distinct sphere/toroid/circle constructions remain motivation rather than inferred physical results. The established research sequence is preserved; the pi brainstorming supplied no premise.

The bibliography and historical attribution distinguish original evidence, investigation acceptance and new-manuscript acceptance. Eight algebra groups and their earlier replay are not counted as sixteen distinct results. This manuscript review did not rerun that suite.

## 3. Independent PDF inspection

The supplied PDF was freshly rendered locally at 125 dpi and all 11 page images were individually opened and examined, including the title-page equations, theorem, proof continuations, exact rational bounds, units table and bibliography. No clipped content, missing glyph, material overlap or unreadable formula/table was found. These independently generated images are also byte-identical to Codex's supplied page images.

Structural checks confirm 11 pages, 19 valid bookmarks, 17 embedded font resources, 66 internal link annotations and three external foundation-edition links. All 48 labels agree between TeX definitions, the final auxiliary record and the label JSON; all 44 reference occurrences resolve. Five bibliography keys are defined and resolved. The targeted final log screen found no warning, overfull/underfull, missing-character or undefined-reference/citation diagnostic.

I did not recompile the manuscript. The compiler execution and environment remain Codex's recorded run; I independently checked the build receipt's ten TeX hashes, helper hash and PDF hash against actual bytes. No standalone fonts are included in this review package.

## 4. Independent artifact and preservation checks

| Check | Result |
|---|---|
| Submitted review ZIP | 148 safe unique members; CRC passes; all 147 manifest-covered payload hashes and sizes match |
| Active candidate edition | 103 files including the self-excluded manifest; all 102 covered payloads match |
| Exact original issued packet | 74 members; all 73 manifest-covered payloads verified; outer checksum matches its sidecar |
| Original versus returned issued members | All 74 original files match; only extra is the identical external sidecar |
| Convenience and delivered-source registries | 67 and 75 records respectively match actual bytes |
| Accepted proof/review/archive anchors | Match separately mounted earlier attachments exactly |
| Nested scientific-review archive | 14 members / 13 payloads verified |
| Nested original investigation archive | 91 members / 90 payloads verified; equals the separate original upload |
| New crosswalk coverage | I01–I15, N01–N07 and FA01–FA26 all covered; 107 destination locators and 10 analytical-obligation groups verified |
| Crosswalk text fidelity | XW-01: 30 copied string fields in 22 generated rows have encoding damage; reviewed replacement restores exact accepted text |
| Input-preservation records | All 78 before/after entries match their baseline; 77 actual delivered/independent files additionally checked |
| Prospective publication tree | Exactly 104 new candidate/landing-page paths plus one root README modification; 105 prospective paths total |
| Root README proposal | Append-only; diff reproduced; historical base matches the separately supplied P3 publication closeout |
| Locked publication gate | PDF, candidate manifest, allowlist and patch identities all agree |
| Post-review source preservation | Every extracted submission member remains byte-identical to the received ZIP |

The 78 preservation entries are a scoped recorded Windows audit, not this review's inspection of the live Windows filesystem. The one raw file not independently available is Codex's different received outer packet. The independently held original is not substituted for that different container in the preservation count.

The overlapping crosswalk sets are coverage groups, not 48 independent mathematical discoveries. Hash and manifest checks establish identity/preservation, not mathematical truth.

## 5. XW-01: required metadata-only repair

Only the newly generated `verification/CROSSWALK.json` shows the identified encoding problem among active candidate TeX, Markdown, JSON and Python text outside historical evidence. Its copied original strings show `Â§` for `§` and `â€“` for `–`. All affected records match a single UTF-8-as-Windows-1252 misdecoding of the correct preserved source text. The PDF, manuscript, readable ledger, original accepted crosswalk, claim IDs and numerical locators are unaffected.

The supplied `correction/CROSSWALK.json` restores the 30 affected fields directly from the preserved original. It preserves all 48 row IDs, all 107 destination locators, every other JSON field and CRLF line endings. `XW01_VERIFICATION.json` records the exact changes. `XW01.patch` shows the diff. This replacement is accepted as the documentary repair; it is not a scientific correction.

Apply it only to a fresh working/publication copy. Preserve the submitted review package and original evidence. Refresh all active manifests/allowlists/gate records whose hashes cover the changed generated file. Do not rebuild the PDF, rewrite prior records or rerun science. If regenerating the crosswalk, explicitly decode its source JSON as UTF-8.

## 6. Source archive and publication boundary

`SOURCE_ARCHIVE_RECONCILIATION.md` records the original packet's matching hash and exact 74-member comparison. The original archive is included in this reviewer package. This resolves scientific-source ambiguity without claiming that the different received wrapper ever matched its sidecar, or identifying how it was repackaged.

No fresh GitHub fetch, live-branch/collision check, staging, commit, push, release or successor investigation was performed here. The prospective README baseline is historical, not a claim about current remote main. Stage B must perform the live checks already required by the issued order after author GO.

The accepted PDF and TeX need not be rebuilt to remove preparation-time review-pending wording. The existing order permits a dated publication disposition to explain later acceptance while preserving exact accepted bytes. Current publication wrappers should also explain the historical archive exception and this subsequent reconciliation. Final wrappers and the XW-01 correction will change some metadata hashes; freeze and verify the actual final allowlist rather than assuming 105 is the eventual committed-file count.

**Final disposition:** manuscript/PDF accepted unchanged; one fully specified generated-metadata correction before publication; scientific-source ambiguity resolved. No further manuscript review round is needed for the supplied exact replacement. Explicit author publication GO remains outstanding.
