# Manuscript claim/source ledger and complete crosswalk

Status: AT01/PC01 and the submitted manuscript are internally accepted. The author approved this v0.1 publication edition; Codex verified the rebuilt release under the polish/publication order.

This record maps every one of the 29 AT and 22 PC accepted equation groups in both directions. Exact source identities are in SOURCE_IDENTITIES.json; literal original labels and complete reasoning remain in the unchanged accepted proofs/ledgers under evidence/input_packet/accepted/. Destinations below include printed manuscript numbers and PDF pages. Source-group comments in editable TeX are audit annotations, not rendered scientific prose.

## Forward coverage

| Accepted group | Content | Status/source locator | Manuscript destination |
| --- | --- | --- | --- |
| AT01 | Raw registration | P1 §1, eq:registration/eq:drive; P2 §2.1 | eq:registration (2.1, p. 2; manuscript/model.tex) |
| AT02 | Finite profiles and port identities | P1 §1/§3, eq:profilenorms | eq:ports (2.2, p. 2; manuscript/model.tex) |
| AT03 | Equations, launch and regularity | P1 Theorem 3.1; P2 §2.2–2.3 | eq:system (2.3, p. 3; manuscript/model.tex); eq:regularity (2.5, p. 3; manuscript/model.tex); eq:launch (2.7, p. 3; manuscript/model.tex) |
| AT04 | Stores and signed accounts | P1 §2, eq:balances/eq:integrated | eq:stores (2.4, p. 3; manuscript/model.tex); eq:emptystock (3.5, p. 4; manuscript/projection.tex) |
| AT05 | Launch drive and convex-ball bounds | P2 §2.3 (2.12)–(2.13), §4.2 (4.8) | eq:launch (2.7, p. 3; manuscript/model.tex); eq:drive0 (2.8, p. 3; manuscript/model.tex); eq:ball (5.5, p. 9; manuscript/proof.tex) |
| AT06 | Exact scaling | P2 §4.1 (4.1)–(4.2) | eq:scaling (5.1, p. 9; manuscript/proof.tex) |
| AT07 | Weighted norm and forced estimate | P2 §4.2 (4.4)–(4.7) | eq:operator (5.3, p. 9; manuscript/proof.tex); eq:forced (5.4, p. 9; manuscript/proof.tex) |
| AT08 | All-finite-time external/native drift | P2 §4.2–4.3 (4.9)–(4.11) | eq:drift (5.6, p. 9; manuscript/proof.tex); eq:constants (4.1, p. 7; manuscript/transfer.tex) |
| AT09 | Comparison-window constants | Accepted new deduction; complete argument restated | eq:constants (4.1, p. 7; manuscript/transfer.tex); tab:units (1, p. 14; manuscript/units.tex) |
| AT10 | Explicit comparison | P2 §5 (5.1)–(5.2) | eq:comparison (5.7, p. 10; manuscript/proof.tex) |
| AT11 | Strong difference and residual | P2 §5 (5.4), strong-difference construction | eq:error (5.8, p. 10; manuscript/proof.tex) |
| AT12 | Longer uniform error bound | Accepted new deduction; complete argument restated | eq:uniformerror (5.9, p. 10; manuscript/proof.tex) |
| AT13 | Landmarks, stock and maximum | Accepted new deduction; complete argument restated | eq:conversion (5.2, p. 9; manuscript/proof.tex); eq:landmarks (4.4, p. 7; manuscript/transfer.tex) |
| AT14 | Comparison norm | Accepted new deduction; complete argument restated | eq:comparisonnorm (5.10, p. 10; manuscript/proof.tex) |
| AT15 | Actual stock bounds | Accepted new deduction; complete argument restated | thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:stockbounds (4.5, p. 8; manuscript/transfer.tex) |
| AT16 | Separate carrier/receiver projections | Accepted new deduction; complete argument restated | thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:projectedbounds (4.6, p. 8; manuscript/transfer.tex) |
| AT17 | Positive-denominator definitions | Accepted new deduction; complete argument restated | thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:fractions (4.7, p. 8; manuscript/transfer.tex) |
| AT18 | Fractions and retention | Accepted new deduction; complete argument restated | thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:ratiobounds (4.8, p. 8; manuscript/transfer.tex) |
| AT19 | Absolute recovery | Accepted new deduction; complete argument restated | eq:recoverysubtraction (5.11, p. 11; manuscript/proof.tex); thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:recoveredamount (4.9, p. 8; manuscript/transfer.tex) |
| AT20 | Three-term product difference | Accepted new deduction; complete argument restated | eq:product (5.12, p. 11; manuscript/proof.tex) |
| AT21 | Receiver-product error and power conversion | Accepted new deduction; complete argument restated | eq:conversion (5.2, p. 9; manuscript/proof.tex); eq:receivererror (5.13, p. 11; manuscript/proof.tex) |
| AT22 | Unchanged native-credit threshold | P2 §3 (3.1)–(3.3) | eq:nativethreshold (4.2, p. 7; manuscript/transfer.tex); tab:units (1, p. 14; manuscript/units.tex) |
| AT23 | Joint sufficient threshold | Accepted new deduction; complete argument restated | eq:allocation (5.14, p. 11; manuscript/proof.tex); eq:cert (4.3, p. 7; manuscript/transfer.tex); tab:units (1, p. 14; manuscript/units.tex) |
| AT24 | Fractions, receiver/native signs and initial activity | New AT receiver/fraction deductions; native sign imported from P2 Theorem 3.1; initial activity P1 Proposition 4.1 | eq:initialdebit (3.16, p. 6; manuscript/projection.tex); eq:allocation (5.14, p. 11; manuscript/proof.tex); thm:transfer (4.1, p. 8; manuscript/transfer.tex); eq:ratiobounds (4.8, p. 8; manuscript/transfer.tex); eq:receiverwitnesses (4.10, p. 8; manuscript/transfer.tex); eq:nativewitness (4.11, p. 8; manuscript/transfer.tex) |
| AT25 | Later receiver-backflow interval | Accepted new deduction; complete argument restated | eq:backflowinterval (5.15, p. 11; manuscript/proof.tex); thm:transfer (4.1, p. 8; manuscript/transfer.tex) |
| AT26 | Original capacity normalization | P1 Theorem 5.1; AT normalization and stock bounds | eq:capacitynormalization (6.1, p. 12; manuscript/amount.tex); eq:oldinvariant (2.6, p. 3; manuscript/model.tex) |
| AT27 | Finite errors | Accepted new deduction; complete argument restated | eq:finiteamount (6.3, p. 12; manuscript/amount.tex); eq:finiteratios (6.4, p. 12; manuscript/amount.tex); tab:units (1, p. 14; manuscript/units.tex) |
| AT28 | Asymptotic scales | Accepted new deduction; complete argument restated | eq:asymptotics (6.5, p. 12; manuscript/amount.tex) |
| AT29 | Shrinking physical window | Accepted new deduction; complete argument restated | eq:traveltime (6.6, p. 13; manuscript/amount.tex) |
| PC01 | Exact core and C1 solution class | P1 Proposition 2.1 eq:core and Theorem 3.1 | eq:registration (2.1, p. 2; manuscript/model.tex); eq:regularity (2.5, p. 3; manuscript/model.tex); eq:core (3.7, p. 4; manuscript/projection.tex) |
| PC02 | General equations/stores/accounts | P1 §1–§2 | eq:system (2.3, p. 3; manuscript/model.tex); eq:stores (2.4, p. 3; manuscript/model.tex) |
| PC03 | Explicit fixed matrix and rank | P1 §1 registration; new PC verification | eq:kernel (3.1, p. 4; manuscript/projection.tex) |
| PC04 | Kernel direction | P1 registration; new PC deduction | eq:kernel (3.1, p. 4; manuscript/projection.tex) |
| PC05 | Indefinite scalar and sign independence | Accepted new deduction; complete argument restated | eq:projectiondef (3.2, p. 4; manuscript/projection.tex); tab:units (1, p. 14; manuscript/units.tex) |
| PC06 | Intensity derivative | Accepted new deduction; complete argument restated | eq:Idot (3.8, p. 4; manuscript/projection.tex) |
| PC07 | Projection derivative/invariance | Accepted new deduction; complete argument restated | thm:projection (3.1, p. 4; manuscript/projection.tex); eq:hdot (3.9, p. 4; manuscript/projection.tex) |
| PC08 | Exact debit identity | Accepted new deduction; complete argument restated | thm:projection (3.1, p. 4; manuscript/projection.tex); eq:debit (3.3, p. 4; manuscript/projection.tex); tab:units (1, p. 14; manuscript/units.tex) |
| PC09 | Inherited Z2 invariant | P1 Theorem 5.1 eq:Z2/eq:chiralityidentity/eq:floor | eq:oldinvariant (2.6, p. 3; manuscript/model.tex) |
| PC10 | Joint floor/ceiling | Accepted new deduction; complete argument restated | thm:projection (3.1, p. 4; manuscript/projection.tex); eq:joint (3.4, p. 4; manuscript/projection.tex) |
| PC11 | Empty external-stock bound | Accepted new deduction; complete argument restated | thm:projection (3.1, p. 4; manuscript/projection.tex); eq:emptystock (3.5, p. 4; manuscript/projection.tex) |
| PC12 | Preloaded signed account | Accepted new deduction; complete argument restated | thm:projection (3.1, p. 4; manuscript/projection.tex); eq:preloaded (3.6, p. 4; manuscript/projection.tex) |
| PC13 | Orthogonal decomposition | Accepted new deduction; complete argument restated | eq:decomposition (3.11, p. 5; manuscript/projection.tex) |
| PC14 | Feasibility necessity | Accepted new deduction; complete argument restated | prop:minimum (3.2, p. 5; manuscript/projection.tex); eq:feasibility (3.12, p. 5; manuscript/projection.tex) |
| PC15 | First equality branch | Accepted new deduction; complete argument restated | prop:minimum (3.2, p. 5; manuscript/projection.tex); eq:equalityone (3.13, p. 5; manuscript/projection.tex) |
| PC16 | Second equality branch | Accepted new deduction; complete argument restated | prop:minimum (3.2, p. 5; manuscript/projection.tex); eq:equalitytwo (3.14, p. 5; manuscript/projection.tex) |
| PC17 | Full-level minimum and boundary cases | Accepted new deduction; complete argument restated | prop:minimum (3.2, p. 5; manuscript/projection.tex); eq:minimum (3.10, p. 5; manuscript/projection.tex) |
| PC18 | Zero ceiling iff zero drive | Accepted new deduction; complete argument restated | prop:dark (3.3, p. 6; manuscript/projection.tex); eq:zeroceiling (3.15, p. 6; manuscript/projection.tex) |
| PC19 | Empty stationarity/initial supply | P1 Proposition 4.1 and §5 opening; applied within new PC result | prop:dark (3.3, p. 6; manuscript/projection.tex); eq:initialdebit (3.16, p. 6; manuscript/projection.tex) |
| PC20 | Coherent projection values | P2 §2.3, existing launch/drive; new PC projection evaluation | eq:launch (2.7, p. 3; manuscript/model.tex); eq:drive0 (2.8, p. 3; manuscript/model.tex); eq:launchprojection (3.17, p. 6; manuscript/projection.tex) |
| PC21 | Strict active yaw witness | Accepted new deduction; complete argument restated | eq:strictwitness (3.18, p. 6; manuscript/projection.tex) |
| PC22 | Finite-time nonattainment example | Accepted new deduction; complete argument restated | eq:nonattainment (3.19, p. 6; manuscript/projection.tex) |

## Reverse coverage

| Manuscript label | Printed number/page | Accepted basis | File |
| --- | --- | --- | --- |
| eq:ports | 2.2, p. 2 | AT02 | manuscript/model.tex |
| eq:registration | 2.1, p. 2 | AT01, PC01 | manuscript/model.tex |
| eq:drive0 | 2.8, p. 3 | AT05, PC20 | manuscript/model.tex |
| eq:launch | 2.7, p. 3 | AT03, AT05, PC20 | manuscript/model.tex |
| eq:oldinvariant | 2.6, p. 3 | PC09, AT26 | manuscript/model.tex |
| eq:regularity | 2.5, p. 3 | AT03, PC01 | manuscript/model.tex |
| eq:stores | 2.4, p. 3 | AT04, PC02 | manuscript/model.tex |
| eq:system | 2.3, p. 3 | AT03, PC02 | manuscript/model.tex |
| eq:Idot | 3.8, p. 4 | PC06 | manuscript/projection.tex |
| eq:core | 3.7, p. 4 | PC01 | manuscript/projection.tex |
| eq:debit | 3.3, p. 4 | PC08 | manuscript/projection.tex |
| eq:emptystock | 3.5, p. 4 | PC11, AT04 | manuscript/projection.tex |
| eq:hdot | 3.9, p. 4 | PC07 | manuscript/projection.tex |
| eq:joint | 3.4, p. 4 | PC10 | manuscript/projection.tex |
| eq:kernel | 3.1, p. 4 | PC03, PC04 | manuscript/projection.tex |
| eq:preloaded | 3.6, p. 4 | PC12 | manuscript/projection.tex |
| eq:projectiondef | 3.2, p. 4 | PC05 | manuscript/projection.tex |
| thm:projection | 3.1, p. 4 | PC07, PC08, PC10, PC11, PC12 | manuscript/projection.tex |
| eq:decomposition | 3.11, p. 5 | PC13 | manuscript/projection.tex |
| eq:equalityone | 3.13, p. 5 | PC15 | manuscript/projection.tex |
| eq:equalitytwo | 3.14, p. 5 | PC16 | manuscript/projection.tex |
| eq:feasibility | 3.12, p. 5 | PC14 | manuscript/projection.tex |
| eq:minimum | 3.10, p. 5 | PC17 | manuscript/projection.tex |
| prop:minimum | 3.2, p. 5 | PC14, PC15, PC16, PC17 | manuscript/projection.tex |
| eq:initialdebit | 3.16, p. 6 | PC19, AT24 | manuscript/projection.tex |
| eq:launchprojection | 3.17, p. 6 | PC20 | manuscript/projection.tex |
| eq:nonattainment | 3.19, p. 6 | PC22 | manuscript/projection.tex |
| eq:strictwitness | 3.18, p. 6 | PC21 | manuscript/projection.tex |
| eq:zeroceiling | 3.15, p. 6 | PC18 | manuscript/projection.tex |
| prop:dark | 3.3, p. 6 | PC18, PC19 | manuscript/projection.tex |
| eq:cert | 4.3, p. 7 | AT23 | manuscript/transfer.tex |
| eq:constants | 4.1, p. 7 | AT08, AT09 | manuscript/transfer.tex |
| eq:landmarks | 4.4, p. 7 | AT13 | manuscript/transfer.tex |
| eq:nativethreshold | 4.2, p. 7 | AT22 | manuscript/transfer.tex |
| eq:fractions | 4.7, p. 8 | AT17 | manuscript/transfer.tex |
| eq:nativewitness | 4.11, p. 8 | AT24 | manuscript/transfer.tex |
| eq:projectedbounds | 4.6, p. 8 | AT16 | manuscript/transfer.tex |
| eq:ratiobounds | 4.8, p. 8 | AT18, AT24 | manuscript/transfer.tex |
| eq:receiverwitnesses | 4.10, p. 8 | AT24 | manuscript/transfer.tex |
| eq:recoveredamount | 4.9, p. 8 | AT19 | manuscript/transfer.tex |
| eq:stockbounds | 4.5, p. 8 | AT15 | manuscript/transfer.tex |
| thm:transfer | 4.1, p. 8 | AT15, AT16, AT17, AT18, AT19, AT24, AT25 | manuscript/transfer.tex |
| eq:ball | 5.5, p. 9 | AT05 | manuscript/proof.tex |
| eq:conversion | 5.2, p. 9 | AT13, AT21 | manuscript/proof.tex |
| eq:drift | 5.6, p. 9 | AT08 | manuscript/proof.tex |
| eq:forced | 5.4, p. 9 | AT07 | manuscript/proof.tex |
| eq:operator | 5.3, p. 9 | AT07 | manuscript/proof.tex |
| eq:scaling | 5.1, p. 9 | AT06 | manuscript/proof.tex |
| eq:comparison | 5.7, p. 10 | AT10 | manuscript/proof.tex |
| eq:comparisonnorm | 5.10, p. 10 | AT14 | manuscript/proof.tex |
| eq:error | 5.8, p. 10 | AT11 | manuscript/proof.tex |
| eq:uniformerror | 5.9, p. 10 | AT12 | manuscript/proof.tex |
| eq:allocation | 5.14, p. 11 | AT23, AT24 | manuscript/proof.tex |
| eq:backflowinterval | 5.15, p. 11 | AT25 | manuscript/proof.tex |
| eq:product | 5.12, p. 11 | AT20 | manuscript/proof.tex |
| eq:receivererror | 5.13, p. 11 | AT21 | manuscript/proof.tex |
| eq:recoverysubtraction | 5.11, p. 11 | AT19 | manuscript/proof.tex |
| eq:asymptotics | 6.5, p. 12 | AT28 | manuscript/amount.tex |
| eq:capacitynormalization | 6.1, p. 12 | AT26 | manuscript/amount.tex |
| eq:finiteamount | 6.3, p. 12 | AT27 | manuscript/amount.tex |
| eq:finiteratios | 6.4, p. 12 | AT27 | manuscript/amount.tex |
| eq:synthesis | 6.2, p. 12 | SYN01 | manuscript/amount.tex |
| eq:traveltime | 6.6, p. 13 | AT29 | manuscript/amount.tex |
| tab:units | 1, p. 14 | AT09, AT22, AT23, AT27, PC05, PC08 | manuscript/units.tex |

## Authorized synthesis and editorial choices

SYN01 is equation (6.2): M_kappa <= C_joint <= C_Z = C_inv, obtained by applying PC10–PC11 on the compact window of AT13 and using AT26. Its one-line proof is in §6.1. No new normalized capacity statistic or attained maximum is introduced.

E01 is applied: P2's Introduction is §1; its problem, theorem, energy, comparison, meaning and conclusion are §§2–7, respectively. Its native-credit result is Theorem 3.1; its units are Appendix A. The supplied P2 LABELS.json and main.tex verify these locators. P1's global evolution is separately identified as P1 Theorem 3.1. Original accepted ledgers and review receipts remain byte-identical.

Notation-only aliases: L_err denotes the accepted L=B1+B2; e_y denotes the registration vector originally called u, while u,v remain the real perpendicular vectors in the algebraic constructions. No coefficient or hypothesis changes.

Shared general model in §2 retains arbitrary admitted preparations. Projection Theorem 3.1 uses that general class at all finite positive couplings. Transfer Theorem 4.1 adds exactly the declared empty coherent family and sufficient threshold. The abstract states this separation and the nonzero chiral-drive hypothesis.

Introductory and concluding claims summarize these mapped results. General solution/initial activity/Z2 foundations are inherited from P1; P2's native-credit witness is explicitly imported. The new accepted AT/PC arguments are printed in full. Table 1 uses P1 §1 and P2 Appendix A bookkeeping with AT/PC derived quantities.

Unresolved interpretations: actual joint-ceiling attainment, infinite-time approach, arbitrary-launch quantitative recovery, full yaw classification, optimization, native stepping and physical route/receiver correspondence remain outside the paper. No additional deduction was pursued.

Evidence: 18 AT grouped algebra checks and 12 PC groups were independently replayed in the accepted reviews. This manuscript task ran no scientific checks or historical suites. Document and integrity checks do not add mathematical identities. Authorship, GPT formulation/internal review and Codex investigation/manuscript roles are retained; GPT accepted the submitted draft; Codex checks this rebuilt publication PDF under the author's approval. No claim is made that GPT inspected the new PDF.
