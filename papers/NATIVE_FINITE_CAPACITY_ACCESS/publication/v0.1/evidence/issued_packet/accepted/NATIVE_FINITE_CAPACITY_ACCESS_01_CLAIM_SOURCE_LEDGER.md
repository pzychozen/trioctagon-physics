# Claim/source ledger: native finite capacity access

**Verdict: Established unchanged; submitted for GPT review.**

P1, P2 and P3 are accepted published foundations. The supplied source assessment is GPT's proposal, independently challenged in the accompanying proof. Its preparatory checks are not acceptance. New claims below belong to this bounded investigation; no accepted predecessor result is rewritten.

## Immutable source identities

- P1: 273b1a6faaab19ea58748d00576439166eeef9ab.
- P2: 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9.
- P3: 54c0f6c419fa681e2c1e74a5ad2bb46df787bb93; PDF 137,455 bytes, SHA-256 93de8c191549fd0ad70f4cf5df970abfbe0ae37d0f0a8b688cbb128577438f79.

Paths below are relative to inputs/published/P1/, P2/ or P3/. The supplied registry contains 62 selected exact source records; INPUT_VERIFICATION.json checks all of them. Fifty-nine reconcile to the supplied historical remote receipt and 58 to the self-excluded P3 publication manifest. This is not a new remote download or a claim that the complete published editions are included. Preserved nested descriptors retain original scopes.

## Inherited facts

| ID | Fact | Exact source locator | Current destination |
| --- | --- | --- | --- |
| I01 | Raw registration and drive | P3 §2.1, (2.1), p. 2; model.tex, eq:registration; originally P1 §1, candidate.tex, eq:registration and eq:drive | FA01 |
| I02 | Circle admissibility, finite tents and port identities | P3 §2.1, (2.2), pp. 2–3; model.tex, eq:ports; P1 §3, wellposed.tex, eq:profilenorms | FA02 |
| I03 | Original exchange equations | P3 §2.2, (2.3), p. 3; model.tex, eq:system; P1 §1, candidate.tex, eq:system | FA03 FA10 FA12 FA17 |
| I04 | Positive stores, conservation and signed accounts | P3 §2.2, (2.4), p. 3; model.tex, eq:stores | FA04 FA05 FA09 FA21 FA26 |
| I05 | Unique global solution and strong empty-launch regularity | P1 Theorem 3.1; wellposed.tex, thm:global, eq:strong; restated P3 §2.2, (2.5), p. 3, eq:regularity | FA09 FA11 FA17 |
| I06 | Coherent empty launch, R, k and drive | P3 §2.3, (2.7)–(2.8), p. 3; model.tex, eq:launch, eq:drive0; P2 §2.3 (2.12)–(2.13) | FA05 FA06 FA23 FA25 |
| I07 | General joint ceiling and empty external-stock bound | P3 Theorem 3.1, (3.3)–(3.6), p. 4; projection.tex, eq:debit, eq:joint, eq:emptystock, eq:preloaded | FA05 FA08 FA21 FA24 FA26 |
| I08 | Yaw pi/4 coherent witness, exact ceiling and drive magnitude | P3 §3.3, (3.18), p. 6; projection.tex, eq:strictwitness | FA05 FA23 FA24 FA26 |
| I09 | Weighted cancellation/forced estimate argument | P3 §5.1, (5.3)–(5.4), p. 9; proof.tex, eq:operator, eq:forced; also P2 §4.2 | FA10 FA11 |
| I10 | Native energy ball and Jacobian estimate | P3 §5.1, (5.5), p. 9; proof.tex, eq:ball and preceding conservation statement; P1 §3, eq:lipschitzbounds, eq:coercive | FA09 FA12 |
| I11 | Strong difference before first-weak-derivative residual | P3 §5.2, p. 10; proof.tex, paragraph preceding eq:error and following residual discussion | FA17 FA18 FA19 |
| I12 | Original accessibility definition and authorized synthesis | P3 §6.1, (6.1)–(6.2), p. 12; amount.tex, eq:capacitynormalization, eq:synthesis | Proof §8; symbol and denominator preserved |
| I13 | Large-coupling amount/fraction distinction | P3 §6.2, (6.3)–(6.5), p. 12; amount.tex, eq:finiteamount, eq:finiteratios, eq:asymptotics; receiving/recovery theorem in §4 | Proof §8; no old fraction imported |
| I14 | Dimensional conventions | P3 Appendix A, Table 1, p. 14; units.tex, tab:units; P1 §1, Table 2, candidate.tex, tab:units | FA06 FA21 FA25; proof §7 |
| I15 | Separate prior native-credit theorem | P2 §3, Theorem 3.1, theorem.tex, thm:credit; P3 (4.11), p. 8, and §5.5, p. 11 | Proof §§2,8; not a premise giving return in this new regime |

P1 Theorem 3.1 is global existence/regularity. P2 Theorem 3.1 is later native credit. The current proof uses the former; it does not import the latter's conclusion into a different regime. P3's corrected printed P2 section offsets remain in force.

## New steps and their independent proof

| ID | Claim | Dependencies | Proof destination | Exact checks | Analytical obligation/disposition |
| --- | --- | --- | --- | --- | --- |
| N01 | Original-variable forced estimate with receiver weight | I02–I05, I09 | FA10 FA11 | EC01 | Skew cancellation by periodic Sobolev integration; regularized norm and limit at zeros. Proposed A1 independently proved, original c/kappa factors retained. |
| N02 | Drive-dependent Volterra bounds | I03–I06, I10; N01 | FA06 FA12 FA13 FA14 FA15 | EC02 EC04 | Actual chain rule, two native-coupling factors, positive-kernel iteration and factorial remainder on every finite interval. Proposed A4–A7 independently proved. |
| N03 | Reference residual, its norm and finite error | I02–I05, I11; N01–N02 | FA16 FA17 FA18 FA19 | EC03 EC04 | Strong regularity established first; negative second-carrier and positive receiver residual both retained. Proposed A8–A10 independently proved. |
| N04 | Capacity-normalized finite-time lower bound | I04, I07–I08; N02–N03 | FA20 FA21 | EC05 | Reverse triangle, positive-bracket prerequisite and original storage factor 1/2. Proposed A11–A12 independently proved. |
| N05 | Strict quarter-capacity certificate | N04; I06, I08 | FA07 FA08 FA22 FA23 FA24 | EC06 EC07 | Exact cosine/sinh rational bounds; bracket >9/16, prefactor >13/16; strict 1053/4096 and excess 29/4096. Proposed A13–A15 independently proved. |
| N06 | Finite positive nonempty regime and dimensions | I06, I14; N02–N03 | FA06 FA07 FA25 | EC08 | Equivalent eta_N condition, finite positive selection before phase, and both rates T^-1 with R retained. Proposed A16 and units independently proved. |
| N07 | Meaning and scope of the new amount | I04, I07–I08, I12–I15; N05–N06 | FA26; proof §8 | EC05 | Combined stock/joint ceiling; fixed phase-independent parameters/time, vanishing absolute stock near phase zero, no receiver share or later-return import. |

## Reverse coverage of displayed groups

| Group | Status | Basis | Scope |
| --- | --- | --- | --- |
| FA01 | Inherited model | I01 | Complete raw registration; yaw fixed to the accepted witness, not a new registration. |
| FA02 | Inherited profile identities | I02 | Full periodic-distance admissibility and first weak derivative. |
| FA03 | Inherited equations | I03 | Original variables; no scaled-time factors. |
| FA04 | Inherited accounts | I04 | Quadratic trial stores and total signed powers. |
| FA05 | Inherited launch and yaw specialization | I04 I06 I07 I08 | Positive drive/capacity for the admitted phase, empty-launch stock identity. |
| FA06 | New proposed rates, established | N02 N06 | Exact nu and sigma_ext definitions. |
| FA07 | New sufficient regime/time, established | N05 N06 | Condition permits equality; time independent of phase. |
| FA08 | New main theorem, established | N05 | Strict 1053/4096 joint-capacity access. |
| FA09 | Inherited regularity/bounds and norm convention | I02 I04 I05 I10 | Legitimate strong solution before estimating it. |
| FA10 | Original external operator, newly assembled | I03 N01 | Receiver coupling remains inside the skew part. |
| FA11 | Forced estimate in original variables | N01 | Zero-norm regularization in adjacent proof. |
| FA12 | Actual drive derivative and integral inequalities | N02 | Jacobian acts along the full actual native curve. |
| FA13 | New drive-dependent Volterra inequality | N02 | Nonnegative continuous g,h; exact rate coefficient. |
| FA14 | New comparison iteration and vanishing remainder | N02 | Written finite-interval functional proof, not a software assertion. |
| FA15 | New hyperbolic norm/drive bounds | N02 | Drive magnitude retained, all finite nonnegative times. |
| FA16 | New comparison curve | N03 | Reference only, not altered coefficients or an exact trajectory. |
| FA17 | New full difference equation/residual | N03 | Both signs and receiver weight verified. |
| FA18 | New weighted residual norm | N03 | Orthogonal carrier/receiver components. |
| FA19 | New finite error estimate | N03 | First derivative only; strong difference known beforehand. |
| FA20 | New reverse-triangle bound | N04 | No squaring if bracket is negative. |
| FA21 | New normalized bound after positivity | N04 | Original stock conversion and positive denominator. |
| FA22 | Exact elementary sinh certificate | N05 | Strict geometric-tail comparison. |
| FA23 | Exact capacity factor and cosine certificate | I06 I08 N05 | Division valid only for admitted positive phase. |
| FA24 | New final strict margin | N05 | 1053/4096 = 1/4 + 29/4096. |
| FA25 | New equivalent finite selection | N06 | Positive multiplier; same coefficients for all phases. |
| FA26 | Scope accounting from inherited stores | I04 I08 N07 | Ceiling fraction of initial native storage; not quarter-total extraction. |

The unnumbered regularized-norm derivative belongs to N01/FA11; the monomial identity and factorial-ratio argument belong to N02/FA14; the sinh-series ratio belongs to N05/FA22. The dimensions table and explicit unit cancellations belong to I14/N06. The theorem's quantifier order is stated before FA06 and proved in §6. Thus unnumbered substantive supporting arguments are also accounted for.

## Check scope and notation

Eight exact-algebra groups EC01–EC08 are executed once by the independently written exact_checks.py, using installed SymPy 1.14.0 in conda torment. These are useful arithmetic/algebra checks for this proof, not eight new scientific identities or a replay of the prior 18 AT/12 PC groups. The supplied readiness_checks.py remains untouched and was not executed. The written argument carries regularity, periodic integration, positive-kernel order, convergence of the iteration remainder and strictness.

A0 is a forcing magnitude, not P3's drift constant A or accessibility statistic. The scalar functions g,h, the Volterra operator V, reference-error W and dimensionless bracket B(u,rho) are local proof notation. sigma_ext avoids the port index; nu is an estimate rate, not native F cadence. P3's A_kappa=M_kappa/C_inv is unchanged.

There is no correction to the supplied proposition. Explicating the shortest-circle-distance consequence, norm regularization, iteration remainder and restored amplitude units makes existing hypotheses and proof obligations explicit; it adds no assumption. The sufficient condition and strict constant remain exactly as proposed.

No receiver-only fraction, later-return guarantee, maximum time, ceiling saturation, full parameter overlap, physical calibration, spatial route or successor investigation is established by this package. The carried geometric agenda remains intact.
