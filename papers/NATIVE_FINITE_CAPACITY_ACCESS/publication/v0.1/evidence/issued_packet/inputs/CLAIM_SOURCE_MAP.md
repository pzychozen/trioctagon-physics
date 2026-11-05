# Claim/source map for the proposed investigation

**Status:** Preparatory map, 4 November 2026. Rows marked proposed require independent proof. Published numbering and page locators below refer to the accepted P3 v0.1 PDF at commit 54c0f6c419fa681e2c1e74a5ad2bb46df787bb93. Exact file identities are in SOURCE_IDENTITIES.json.

## Inherited foundations

| ID | Foundation | Exact source | Role |
|---|---|---|---|
| I01 | Registration \(f=K(a\times b)\), \(J=D_xf\) | P3 §2.1, (2.1), p. 2; manuscript/model.tex, eq:registration | Unchanged defining model |
| I02 | Circle, finite disjoint tents, \(m,d,\mathcal B,\mathcal B^*\) | P3 §2.1, (2.2), p. 2; model.tex, eq:ports | Norms, adjoint and first derivative |
| I03 | Original exchange equations | P3 §2.2, (2.3), p. 3; model.tex, eq:system | Native feedback and external dynamics |
| I04 | Trial storages and exact balance | P3 §2.2, (2.4), p. 3; model.tex, eq:stores | \(E_{\rm out}\) is exact net native debit under empty launch |
| I05 | Strong empty-launch solution class | P3 §2.2, (2.5), p. 3; model.tex, eq:regularity; inherited P1 Theorem 3.1, manuscript/wellposed.tex | Functional setting before residual estimates |
| I06 | Coherent empty-launch family and drive | P3 §2.3, (2.7)–(2.8), p. 3; model.tex, eq:launch and eq:drive0 | \(R,k,f_0\), phase range |
| I07 | Joint capacity and empty-launch ceiling | P3 Theorem 3.1, (3.3)–(3.6), p. 4; projection.tex, eq:debit and eq:emptystock | Structural upper bound, not an attainability theorem |
| I08 | Published yaw \(\pi/4\) witness and its stronger ceiling | P3 §3.3, (3.18), p. 6; projection.tex, eq:strictwitness | Exact \(C_{\rm joint}\) and \(|f_0|^2\) used here |
| I09 | Weighted skew cancellation and forced norm estimate | P3 §5.1, (5.3)–(5.4), p. 9; proof.tex, eq:forced | Reuse the argument; derive original-variable factors |
| I10 | Native ball and Jacobian bound | P3 §5.1, (5.5), p. 9; proof.tex, eq:ball | \(|x|\le R\), \(\|J\|\le kR\) |
| I11 | Difference regularity before first-derivative residual estimate | P3 §5.2, p. 10; proof.tex | No second tent derivative required |
| I12 | Published accessibility normalization and synthesis | P3 §6, (6.1)–(6.2), p. 12; amount.tex, eq:capacitynormalization and eq:synthesis | Preserve \(\mathcal A_\kappa=M_\kappa/C_{\rm inv}\) |
| I13 | Large-\(\kappa\) amount and ratio distinction | P3 §6, (6.3)–(6.5), p. 12; amount.tex, eq:asymptotics | Motivation for finite capacity access |
| I14 | Dimensional conventions | P3 Appendix A, p. 14; units.tex | Check \(\nu,\sigma_{\rm ext},t_*\) and \(R\)'s restored unit |
| I15 | Same-trajectory native credit | P2 Theorem 3.1, §3; manuscript/theorem.tex; P3 Introduction and references | Prior accepted behavior, not a return theorem for the new regime |

The published P3 crosswalk is included unchanged under published/P3/verification/CROSSWALK.json. P1's global Theorem 3.1 and P2's native-credit Theorem 3.1 are different statements. Preserve the corrected source offsets already recorded in P3.

## Proposed new steps

| ID | Proposed claim | Foundations and preparation locator | Verification needed |
|---|---|---|---|
| N01 | Original-variable forced estimate with complete receiver weighting | I02–I05, I09; SOURCE_ASSESSMENT (A1) | Cancellation, domain and zero-norm justification |
| N02 | Drive-dependent Volterra upper bounds | I03–I06, I10; (A4)–(A7) | Exact native derivative, coefficients, positive-kernel iteration and remainder |
| N03 | Reference-curve residual and norm | I02–I05, I11; (A8)–(A10) | Both residual terms, signs, weighted norm and strong regularity |
| N04 | Capacity-normalized finite-time lower bound | I04, I07–I08, N02–N03; (A11)–(A12) | Positive bracket before squaring |
| N05 | Quarter-capacity certificate with \(1053/4096\) margin | N04; (A13)–(A15) | Exact rational bounds and full phase-range quantifiers |
| N06 | Finite positive nonempty regime and dimensions | I06, I14; (A16) and §6 | Condition equivalence, finite selection, restored units |
| N07 | Scope of the new amount statement | I04, I07–I08, I12–I15; §7 | Joint-ceiling denominator, total external stock and no automatic old recovery fraction |

## Provenance boundary

P3 is the current accepted mathematical baseline. P1 and P2 remain the original publications of inherited foundations. The new route and rates in SOURCE_ASSESSMENT.md are GPT's proposed analysis for this mission; their presence in a hashed packet is not mathematical acceptance.

The selected published files were copied from the accepted P3 closeout payload and matched against its publication manifest and supplied remote-byte receipt. P1/P2 copies additionally retain their original immutable identities. The preparation performs no new remote audit and does not reattribute predecessor results to this investigation.
