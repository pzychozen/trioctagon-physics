# Editorial source map and fidelity notes

**Task:** NATIVE_TRANSFER_CAPACITY_PAPER_01  
**Date:** 4 November 2026  
**Status:** Current manuscript guidance; accepted source evidence remains unchanged.

## 1. What the manuscript is presenting

P1 and P2 are the two published predecessor papers. AT01 and PC01 are completed and internally accepted analytical investigations now being presented in one new manuscript. Their original reports, ledgers, review archives and subsequent GPT acceptances are supplied separately.

The manuscript must distinguish:

| Quantity | Meaning | Relevant hypotheses |
| --- | --- | --- |
| E_out(t) | Actual external stock, equal to net native debit under empty preparation | Empty carrier and receiver |
| M_kappa | Actual maximum of that stock over the specified first window | Specified coherent launch; defined compact window |
| Receiver share | H_R(t_pi)/E_out(t_pi) | Positive intermediate total-stock denominator, proved by AT15–AT16 |
| Net recovery fraction | [H_N(t_2pi)−H_N(t_pi)]/E_out(t_pi) | Same positive intermediate total-stock denominator |
| Endpoint receiver retention | H_R(t_2pi)/H_R(t_pi) | Separately proved positive intermediate receiver stock |
| C_Z and C_joint | Necessary upper ceilings on signed net native debit | Fixed exchange model; arbitrary admitted preparations |
| A_kappa | M_kappa/C_inv, with C_inv=C_Z for the specified launch | Original AT normalization, unchanged |

The shared source model should allow arbitrary admitted preparations. The finite-window theorem adds the empty coherent launch and sufficient coupling threshold locally. “Projection capacity” means an upper bound on net native debit; it is not an assertion of an attained dynamical maximum.

## 2. E01 — repair printed P2 section locators in the new manuscript

During manuscript preparation, direct comparison with P2's published main.tex and verification/LABELS.json identified a minor citation issue in the accepted investigation ledgers:

- The AT01 source table lists P2's problem, theorem, energy, comparison, meaning and conclusion as §§1–6.
- The PC01 source table likewise lists P2.problem as §1.
- P2 has an Introduction as §1, so those printed section numbers are actually §§2–7.

The literal TeX labels, source files, mathematical equations and hypotheses are correct. This is an editorial source-locator correction, not a scientific correction to either accepted investigation.

**Disposition:** preserve both original ledgers and completed review records byte for byte. Use the verified locators below in the new manuscript, its bibliography and new claim/source crosswalk. Record E01 in the new provenance/fidelity record. No additional author approval is required for this routine citation repair.

| P2 source | Literal label | Published number | PDF page |
| --- | --- | --- | ---: |
| introduction.tex | sec:introduction | §1 | 2 |
| problem.tex | sec:problem | §2 | 2 |
| problem.tex | sec:ports | §2.1 | 2 |
| problem.tex | sec:equations | §2.2 | 3 |
| problem.tex | sec:launch | §2.3 | 3 |
| theorem.tex | sec:theorem | §3 | 4 |
| theorem.tex | thm:credit | Theorem 3.1 | 4 |
| energy.tex | sec:energy | §4 | 5 |
| comparison.tex | sec:comparison | §5 | 6 |
| meaning.tex | sec:meaning | §6 | 8 |
| conclusion.tex | sec:conclusion | §7 | 9 |
| units.tex | sec:units | Appendix A | 10 |

Source: exact published/P2/verification/LABELS.json, checked against the section ordering in published/P2/manuscript/main.tex. P2's immutable edition is at commit 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9.

P1's global solution is also numbered Theorem 3.1. Always identify the source paper when citing either that result or P2's Theorem 3.1 native-credit certificate.

## 3. Imported foundations versus arguments that belong in this paper

| Material | Treatment |
| --- | --- |
| P1 global evolution, balances, initial activity and Z2 invariant | Cite published theorem/proposition and restate the hypotheses/formulas used |
| P2 exact scaling, weighted norm estimate, ball/drift bounds and comparison | Cite and state the required definitions and estimates; a compact cancellation/regularized-norm reminder is sufficient |
| P2 native-credit witness and kappa_crit | Import explicitly, unchanged, with correct source theorem and launch hypotheses |
| Extension from the shorter witness horizon to S=2pi/omega | Give the AT proof with the 4/omega absolute sine integral |
| Stock bounds, positive denominators, receiver share, net recovery, endpoint retention and exact receiver-power signs | Give the complete accepted AT arguments |
| Projection invariant, exact debit, joint ceiling, feasibility/minimum, zero-drive equivalence and strict witness | Give the complete accepted PC arguments |
| Finite-time nonattainment example | Include its short uniqueness argument and its explicit infinite-time limitation |

Every AT01–AT29 and PC01–PC22 group must have a destination in the manuscript crosswalk. Duplicate shared definitions can map to one location. The record must distinguish inherited facts, accepted new deductions and manuscript-only notation or presentation choices.

## 4. One immediate synthesis is authorized

For the common coherent empty-launch setting,

\[
M_\kappa\le C_{\rm joint}\le C_Z=C_{\rm inv}.
\]

Give a one-line proof: the joint all-time bound holds at every time in the compact interval defining M_kappa; its minimum-of-ceilings formula makes it no larger than C_Z; the old coherent-launch value is C_inv.

Label this in the new ledger as **SYN01, immediate combination of AT13/AT26 and PC10–PC11**. This is a transparent application of the accepted results. It does not assert an achieved capacity or replace A_kappa's denominator.

No additional normalized capacity ratio, full yaw classification, small-phase ratio limit, optimized threshold or enlarged preparation class is requested. Earlier exploratory assessment formulas that were not part of the delivered accepted investigations are not manuscript premises.

## 5. Provenance and abstract lessons carried forward

P2's MC-01 replaced an ambiguous “nonzero coherent launch” description with the specified coherent family and nonzero chiral drive. Apply that lesson directly: the quantitative theorem's abstract description must independently retain the actual preparation and sufficient-regime qualifications.

The new structural theorem has a broader preparation and coupling scope. Its scope must remain separate in the abstract as well as in theorem statements.

Accepted mathematics, Codex's document fidelity/build checks, pending GPT review of the new final PDF and later publication are different statuses. Do not transfer the earlier paper's publication approval or final-PDF review to this new manuscript.

Preserved technical records can contain historical pending-review or open-question language. Their later acceptance/publication records resolve that history. The new prose should state the current result accurately while keeping every historical input unchanged.

If scientific check counts are useful, state 18 AT groups and 12 PC groups separately. Each was independently replayed. Neither reviewer repetition nor document inspection creates new scientific identities.
