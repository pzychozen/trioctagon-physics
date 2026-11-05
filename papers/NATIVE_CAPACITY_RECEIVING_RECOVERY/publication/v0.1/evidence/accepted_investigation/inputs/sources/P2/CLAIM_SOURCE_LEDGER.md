# Manuscript claim and source ledger

Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate

Research manuscript v0.1, draft for manuscript review. 3 November 2026. Final PDF: b1a3018a287cd1b0eda99ac82cd08102862672836afd66b51ca781d9dcb44e5e.

The seven published source IDs CANDIDATE through ACCEPTED_PROOF refer to unchanged complete files at edition commit 273b1a6faaab19ea58748d00576439166eeef9ab. ORDER and CONTEXT identify the later investigation inputs retained separately in SOURCE_IDENTITIES.json.

This is new editorial material. The original proof and ledger remain byte-for-byte unchanged. Their pending-review and missing-review statements describe their historical preparation. The current analytical review is available, was read in full, and accepts the finite-coupling result without a mathematical correction. GPT's internal manuscript review accepted the scientific content and found one minor abstract clarification. MC-01 has been applied in this closeout build. The revised PDF is returned for a focused final artifact check and author review before publication.

The provenance clarification narrows the old ledger heading to the seven published files. It changes no equation, theorem, source bytes or acceptance scope. ORDER and CONTEXT are later inputs; CURRENT_GPT_REVIEW and MANUSCRIPT_ORDER are separately identified in [SOURCE_IDENTITIES.json](SOURCE_IDENTITIES.json).

## Exact inherited sources

| ID | Retained complete file | Focused predecessor locator |
|---|---|---|
| CANDIDATE | [manuscript/candidate.tex](evidence/investigation/sources/manuscript/candidate.tex) | Section 1: registration, drive, tents, ports, stores, system, units. |
| POWER | [manuscript/power.tex](evidence/investigation/sources/manuscript/power.tex) | Section 2: Euler/Jacobian identity, native feedback, total powers and balances. |
| WELLPOSED | [manuscript/wellposed.tex](evidence/investigation/sources/manuscript/wellposed.tex) | Theorem 3.1 and proof: global/strong solutions, profile norms and Lipschitz bounds. |
| ACTIVITY | [manuscript/activity.tex](evidence/investigation/sources/manuscript/activity.tex) | Proposition 4.1: empty-launch expansions. Proposition 4.2 concerns different prepared data. |
| CAPACITY | [manuscript/capacity.tex](evidence/investigation/sources/manuscript/capacity.tex) | Theorem 5.1: invariant, floor and coherent-span net-extraction ceiling. |
| INTERPRETATION | [manuscript/interpretation.tex](evidence/investigation/sources/manuscript/interpretation.tex) | Section 8: collocation and geometric distinctions; historical open status. |
| ACCEPTED_PROOF | [evidence/accepted_proof.md](evidence/investigation/sources/evidence/accepted_proof.md) | S1-S4, A1-A16, B1-B4: finer predecessor proof locators; not the new R labels. |

## Accepted claims to printed manuscript

All STR labels below refer to the accepted investigation ledger. Claims classed as new in that historical ledger are the already accepted argument now typeset here. Mathematical premises, inequalities and regularity are justified by the written proof, not by symbolic PASS counts.

| Accepted claim | Manuscript coverage | Foundation and scope |
|---|---|---|
| STR01: Raw chiral drive, fixed registration and original port ordering | Section 2.1 (p. 2; sec:ports); Eq. 2.1 (p. 2; eq:registration); Eq. 2.2 (p. 2; eq:drive) | CANDIDATE: eq:registration, eq:drive; ACCEPTED_PROOF: S1. |
| STR02: Normalized disjoint periodic tents; exact m, d and first-derivative norms | Eq. 2.3 (p. 2; eq:tents); Eq. 2.4 (p. 2; eq:ports); Eq. 2.5 (p. 3; eq:profilenorms) | CANDIDATE: eq:tents, eq:ports; WELLPOSED: eq:profilenorms; ACCEPTED_PROOF: A9. |
| STR03: Unchanged constant-coefficient exchange and empty preparation | Eq. 2.6 (p. 3; eq:system); Eq. 2.11 (p. 3; eq:preparation) | CANDIDATE: eq:system; ACTIVITY: Proposition 4.1; ORDER: sections 2-3. |
| STR04: Global uniqueness, conservation and strong regularity at each finite coupling | Eq. 2.9 (p. 3; eq:balances); Eq. 2.10 (p. 3; eq:regularity); Section 2.2 (p. 3; sec:equations) | WELLPOSED: Theorem 3.1, eq:strong; POWER: eq:balances. |
| STR05: Yaw-independent K norm from both Gram eigenvalues | Eq. 2.12 (p. 4; eq:gram) | CANDIDATE: eq:registration; accepted calculation R10. |
| STR06: R squared is 3; the launch drive is nonzero at every fixed yaw | Eq. 2.11 (p. 3; eq:preparation); Eq. 2.12 (p. 4; eq:gram); Eq. 2.13 (p. 4; eq:launchdrive) | ACTIVITY: Proposition 4.1, eq:nonzero; R11. |
| STR07: f and J bounds and convex-ball Lipschitz bound | Eq. 4.8 (p. 6; eq:ballbounds) | WELLPOSED: eq:lipschitzbounds; POWER: eq:jacobian. |
| STR08: Positive conserved total storage bounds the exact core by R | Section 4.2 (p. 5; sec:forced); Eq. 4.9 (p. 6; eq:externalbounds); Eq. 4.10 (p. 6; eq:coredrift) | POWER: eq:balances; WELLPOSED: conservation in Theorem 3.1. |
| STR09: Exact time/state scaling and original total-power factor | Eq. 4.1 (p. 5; eq:scaling); Eq. 4.2 (p. 5; eq:scaledsystem); Eq. 4.3 (p. 5; eq:powerconversion) | CANDIDATE: eq:system; chain rule, R14-R15. |
| STR10: Weighted energy cancellation and norm estimate, regularized at zero | Eq. 4.4 (p. 5; eq:externalnorm); Eq. 4.5 (p. 5; eq:operator); Eq. 4.6 (p. 5; eq:skew); Eq. 4.7 (p. 5; eq:forcedbound) | POWER: periodic integration and matched loading; WELLPOSED: eq:strong; R16-R18. |
| STR11: Exact external norm and port estimates before comparison | Eq. 4.9 (p. 6; eq:externalbounds) | R13, R16-R19 and empty preparation. |
| STR12: Core and drive drift with the accepted A and factor one-fourth | Eq. 3.2 (p. 4; eq:errorconstants); Eq. 4.10 (p. 6; eq:coredrift); Eq. 4.11 (p. 6; eq:drivedrift) | R5, R13-R20. |
| STR13: Explicit oscillator comparison and negative coefficient at T | Eq. 5.1 (p. 6; eq:comparison); Eq. 5.2 (p. 6; eq:comparisonoutput); Eq. 5.3 (p. 6; eq:comparisonmargin) | R21-R22; B*B=mI from WELLPOSED: eq:profilenorms. |
| STR14: Known strong difference, exact negative first-derivative residual | Section 5 (p. 6; sec:comparison); Eq. 5.4 (p. 7; eq:error) | WELLPOSED: eq:strong; R9, R21-R23; first weak derivative only. |
| STR15: Absolute sine integral and finite propagation/core error | Eq. 5.5 (p. 7; eq:errorintegral); Eq. 5.6 (p. 7; eq:finiteerror) | R18, R20, R23-R25. |
| STR16: Full two-port power error, using actual output in the first term | Eq. 5.7 (p. 7; eq:powerdecomposition); Eq. 5.8 (p. 7; eq:powererror) | R19-R27. |
| STR17: Sufficient finite threshold, D>0 and two D/4 error allocations | Eq. 3.3 (p. 4; eq:threshold); Eq. 3.4 (p. 4; eq:witness); Eq. 5.9 (p. 7; eq:allocation); Theorem 3.1 (p. 4; thm:credit) | R5-R6, R11, R27; other parameters fixed first. |
| STR18: Closed later interval and strictly positive integrated native gain | Eq. 3.5 (p. 4; eq:interval); Eq. 3.6 (p. 4; eq:gain); Section 5 (p. 6; sec:comparison) | R7; POWER: eq:integrated; continuity of total power. |
| STR19: Strict initial native supply and exact receiver charging | Eq. 5.10 (p. 7; eq:initialactivity) | ACTIVITY: Proposition 4.1, eq:initialreceiverpower; R28. |
| STR20: Initial and later intervals belong to one unchanged unique solution | Theorem 3.1 (p. 4; thm:credit); Section 5 (p. 6; sec:comparison) | WELLPOSED: Theorem 3.1; R6-R7 and R28; separate nonuniform small-time argument. |
| STR21: Cumulative total native debit remains nonnegative | Eq. 6.1 (p. 8; eq:cumulative); Section 6.1 (p. 8; sec:account) | POWER: eq:balances and eq:integrated; empty preparation. |
| STR22: Correct dimensions of drift constant, power coefficients and ratios | Appendix A (p. 10; sec:units) | CANDIDATE: tab:units; accepted proof section 6 units table. |
| STR23: External stock bound on fixed finite scaled windows | Eq. 6.3 (p. 8; eq:stockscale); Section 6.2 (p. 8; sec:scales) | R14-R15, R19 and R29. |
| STR24: Witness-power scaling and vanishing witness/circuit-time ratio | Eq. 6.4 (p. 8; eq:powerscale); Eq. 7.1 (p. 9; eq:traveltime); Section 6.2 (p. 8; sec:scales) | R6, R15, R27; proof section 6. All other parameters fixed. |
| STR25: Comparison backflow distinguished from unproved exact receiver sign at t* | Eq. 6.2 (p. 8; eq:comparisonbackflow); Section 6.1 (p. 8; sec:account) | R21-R22 and proof section 6; current review section 3. |
| STR26: Unchanged invariant and net-extraction ceiling with initial-core denominator | Eq. 6.5 (p. 8; eq:invariant); Eq. 6.6 (p. 9; eq:capacity); Section 6.3 (p. 8; sec:capacity) | CAPACITY: Theorem 5.1, eq:Z2, eq:floor, eq:netcapacity, eq:coherentcapacity. |
| STR27: Fast collocation and preserved geometric distinctions; bounded continuation | Section 7 (p. 9; sec:conclusion); Eq. 7.1 (p. 9; eq:traveltime) | INTERPRETATION: section 8; ORDER: section 6; current review sections 3 and 6; manuscript order section 5. |
| STR28: Accepted analytical record, 25 distinct replayed checks, pending final PDF review | Section 1 (p. 2; sec:introduction); Section 7 (p. 9; sec:conclusion) | SOURCE_IDENTITIES.json; EXACT_CERTIFICATE_RESULTS.json; current GPT review sections 1-5; reviewer replay summary; new PROVENANCE.md. |

## R1-R30 equation crosswalk

The R numbers belong to the accepted same-trajectory report. They do not renumber the predecessor or the manuscript. The machine-readable crosswalk also includes final source hashes and every label: [LABEL_CROSSWALK.json](verification/LABEL_CROSSWALK.json).

| Accepted report | Claim | Printed manuscript |
|---|---|---|
| R1 | Registration and chiral drive | Eq. 2.1 (p. 2; eq:registration); Eq. 2.2 (p. 2; eq:drive) |
| R2 | Finite disjoint tents and ports | Eq. 2.3 (p. 2; eq:tents); Eq. 2.4 (p. 2; eq:ports) |
| R3 | Unchanged exchange system | Eq. 2.6 (p. 3; eq:system); Eq. 2.7 (p. 3; eq:storages); Eq. 2.8 (p. 3; eq:powers); Eq. 2.9 (p. 3; eq:balances) |
| R4 | Empty coherent launch | Eq. 2.11 (p. 3; eq:preparation) |
| R5 | All constants and sufficient threshold | Eq. 2.5 (p. 3; eq:profilenorms); Eq. 2.12 (p. 4; eq:gram); Eq. 3.1 (p. 4; eq:constants); Eq. 3.2 (p. 4; eq:errorconstants); Eq. 3.3 (p. 4; eq:threshold); Appendix A (p. 10; sec:units) |
| R6 | Explicit later native-power witness | Theorem 3.1 (p. 4; thm:credit); Eq. 3.4 (p. 4; eq:witness); Eq. 5.9 (p. 7; eq:allocation) |
| R7 | Closed credit interval and integrated gain | Eq. 3.5 (p. 4; eq:interval); Eq. 3.6 (p. 4; eq:gain) |
| R8 | Empty-launch cumulative debit | Eq. 6.1 (p. 8; eq:cumulative) |
| R9 | Inherited global solution and strong regularity | Eq. 2.10 (p. 3; eq:regularity); Section 2.2 (p. 3; sec:equations) |
| R10 | Exact row Gram matrix and operator norm | Eq. 2.12 (p. 4; eq:gram) |
| R11 | Nonzero drive for every fixed yaw | Eq. 2.13 (p. 4; eq:launchdrive) |
| R12 | Norms and first weak derivative of tents | Eq. 2.5 (p. 3; eq:profilenorms) |
| R13 | Ball bounds and convex-ball Lipschitz estimate | Eq. 4.8 (p. 6; eq:ballbounds) |
| R14 | Exact finite-coupling scaling | Eq. 4.1 (p. 5; eq:scaling) |
| R15 | Scaled system and original-power conversion | Eq. 4.2 (p. 5; eq:scaledsystem); Eq. 4.3 (p. 5; eq:powerconversion) |
| R16 | Weighted external space and finite operator | Eq. 4.4 (p. 5; eq:externalnorm); Eq. 4.5 (p. 5; eq:operator) |
| R17 | Propagation and receiver cancellation | Eq. 4.6 (p. 5; eq:skew) |
| R18 | Forced external norm inequality | Eq. 4.7 (p. 5; eq:forcedbound) |
| R19 | Exact external norm and port bounds | Eq. 4.9 (p. 6; eq:externalbounds); Section 4.2 (p. 5; sec:forced) |
| R20 | Core and drive drift, factor one-fourth | Eq. 4.10 (p. 6; eq:coredrift); Eq. 4.11 (p. 6; eq:drivedrift) |
| R21 | Explicit empty-start active-receiver comparison | Eq. 5.1 (p. 6; eq:comparison); Eq. 5.2 (p. 6; eq:comparisonoutput); Eq. 6.2 (p. 8; eq:comparisonbackflow) |
| R22 | Strict negative comparison coefficient | Eq. 5.3 (p. 6; eq:comparisonmargin) |
| R23 | Exact error equation and derivative regularity | Eq. 5.4 (p. 7; eq:error); Section 5 (p. 6; sec:comparison) |
| R24 | Integrated error bound | Eq. 5.5 (p. 7; eq:errorintegral) |
| R25 | Finite error at the witness | Eq. 5.6 (p. 7; eq:finiteerror) |
| R26 | Complete total-power product decomposition | Eq. 5.7 (p. 7; eq:powerdecomposition) |
| R27 | Finite power error | Eq. 5.8 (p. 7; eq:powererror) |
| R28 | Inherited initial activity and same-solution chronology | Eq. 5.10 (p. 7; eq:initialactivity); Section 5 (p. 6; sec:comparison) |
| R29 | Storage on fixed scaled windows | Eq. 6.3 (p. 8; eq:stockscale) |
| R30 | Invariant and initial-core extraction ceiling | Eq. 6.5 (p. 8; eq:invariant); Eq. 6.6 (p. 9; eq:capacity) |

No scientific replay or new trajectory calculation was performed for this manuscript. The supporting history is 25 distinct exact-algebra checks, independently replayed, not 50 distinct checks.

## MC-01 editorial closeout

The author explicitly approved GPT’s manuscript review and the exact MC-01 correction. Only the supplied abstract sentence in main.tex changed. The other nine TeX files, build helper and protected scientific evidence remain byte-identical. All 65 labels, printed numbers and page locators are unchanged in the fresh build; the accepted R1-R30/STR01-STR28 mappings above remain intact. The current source inventory separately identifies the manuscript review and closeout order. The earlier analytical review has not been overwritten.
