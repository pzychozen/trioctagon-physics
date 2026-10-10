# SRG-I v0.1.1 claim/source ledger

All 26 claim IDs are preserved. Page/equation/TeX-line locators below refer to the revision. E01–E03 are the only scientific corrections. Other claims retain the frozen v0.1 analysis and GPT review scope; no broad re-audit is claimed.

## C01 — The glyph tuple is a state schema, without a defined algebra or updates for every entry.

- Manuscript: sec:state (2, PDF p.2, TeX line 155); eq:glyph (2.1, PDF p.2, TeX line 162)
- Evidence class: Recovered definition; unresolved typing
- Source: P03 p.2 §1.1 and p.18 symbol index
- Assumptions/limits: Do not identify the whole tuple with a real scalar. Glyph subscripts and ID label are disclosed notation.
- Status: Supported schema; closure unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C02 — P03 gives an explicit expression, an instantaneous consistency relation and a trail update; they are not interchangeable.

- Manuscript: eq:explicit (2.2, PDF p.3, TeX line 184); eq:consistent (2.3, PDF p.3, TeX line 189); eq:implicit-source (2.4, PDF p.3, TeX line 195)
- Evidence class: Recovered definitions; analytical counterexample
- Source: P03 p.2 §1.1; p.5 §2.2; p.7 §3.1
- Assumptions/limits: Empty echo sets distinguish the first two at nonzero current amplitude. No authorial correction selected.
- Status: Supported distinction
- Revision record: E02 consequential cross-reference: §3.3 now explicitly returns to eq:explicit, P03 p.2 §1.1; the three formulas themselves are unchanged.

## C03 — Literal substitution gives y=C_lambda(y+b).

- Manuscript: eq:temporal (3.1, PDF p.4, TeX line 298); eq:offset (3.2, PDF p.4, TeX line 309); eq:root (3.3, PDF p.4, TeX line 314)
- Evidence class: Deduction
- Source: P03 p.7 §3.1 and p.8 §3.3
- Assumptions/limits: Finite real scalar; current-pass feedback frozen; original temporal coefficient remains one.
- Status: Proved in §3.1
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C04 — The complete real root set is the union of the lower continuum when b=0 and the admissible upper singleton.

- Manuscript: eq:compressor (3.4, PDF p.5, TeX line 331); thm:branches (3.1, PDF p.5, TeX line 337); cor:positive (3.2, PDF p.5, TeX line 369)
- Evidence class: Deduction; full proof
- Source: P03 p.8 §3.4; manuscript Theorem 3.1 and Corollary 3.2
- Assumptions/limits: Every real lambda; upper branch includes equality. Nonnegative states require intersection with [0,infinity).
- Status: Proved, including boundaries
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C05 — The printed scalar relation is not a total single-valued successor map over all finite inputs.

- Manuscript: sec:implicit (3, PDF p.4, TeX line 290)
- Evidence class: Deduction; counterexamples
- Source: P03 pp.7–8; manuscript Example 3.3; P01 pp.22–24 Appendix C for pseudocode; P03 physical p.2 §1.1 for the distinct explicit expression eq:explicit.
- Assumptions/limits: Not a statement about every SRG implementation. Solver nonconvergence is not the no-root proof. No solver was recovered in the bounded source chain.
- Status: Proved for stated relation; solver absence bounded
- Revision record: E02 addressed: P03 and eq:explicit named explicitly after the P01 pseudocode citation. Replacement remains a separate decision.

## C06 — Partner cap, threshold scaling, positive-output log map and signed clamp have different branches, signs and zero values.

- Manuscript: sec:compression (4, PDF p.6, TeX line 450); eq:positive-branches (4.4, PDF p.7, TeX line 510); eq:signed-branches (4.5, PDF p.7, TeX line 527); app:branches (A, PDF p.17, TeX line 1314)
- Evidence class: Recovered maps; derived branch classification
- Source: P03 p.6 §2.5 and p.8 §3.4; P07 p.3 §2.1; Infinity lines49–53
- Assumptions/limits: Signs inside/outside exponential are literal. Alternate substitution is a comparison, not an adopted historical correction.
- Status: Proved in §4 and Appendix A
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C07 — Temporal second differences and the spatial graph operator act on different indices; the patch is a separate explicit position update.

- Manuscript: sec:geometry (5, PDF p.8, TeX line 596); eq:patch-a (5.1, PDF p.8, TeX line 613); eq:patch-b (5.2, PDF p.8, TeX line 614); eq:patch-c (5.3, PDF p.8, TeX line 617)
- Evidence class: Recovered definitions; deduction
- Source: P03 p.8 §3.3; P05 pp.1–2 §§2–3; Position lines31–40,45–78
- Assumptions/limits: X,Y,Z are N-by-3 row arrays; P is N-by-N and acts from the left. Coordinate scaling acts as Z times a 3-by-3 diagonal from the right. Fixed initial graph, empty-row identity, clock coefficient, noise and stage order remain unchanged. Mean conservation still needs column balance.
- Status: E03 addressed: row-array typing and right coordinate action clarified; no source or model change.
- Revision record: Operative Position source lines45–48,65–78 checked as text, not executed.

## C08 — The embedded ring-torus metric gives a first-derivative term absent from a flat-product operator.

- Manuscript: sec:torus (5.3, PDF p.9, TeX line 683); eq:torus-lb (5.7, PDF p.9, TeX line 703)
- Evidence class: New conditional geometric comparison
- Source: P07 p.4 §2.2 and P08 p.2 §2.3 provide comparison targets; §5.3 derives the new operator
- Assumptions/limits: R>r>0, induced metric and smooth scalar field declared. Flat metric remains a distinct legitimate choice.
- Status: Proved diagnostic; not adopted
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C09 — Phi_D=i Phi_Q gives an order-four quarter-turn and real quadrature, not Hermitian orthogonality or independent complex sectors.

- Manuscript: eq:phase-pair (6.1, PDF p.10, TeX line 736); eq:quarter-cycle (6.3, PDF p.10, TeX line 764)
- Evidence class: Recovered definition; deduction
- Source: P09 p.2 §2.3; P10 p.2 §2.3
- Assumptions/limits: Inner product linear in its second argument; nonzero vector for nonorthogonality. Four algebraic images are not four observed passes.
- Status: Proved in Proposition 6.1
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C10 — Time shift, spatial reflection and dynamical reversal are distinct operations.

- Manuscript: sec:shift-reversal (6.2, PDF p.10, TeX line 789); eq:shift-reversal (6.4, PDF p.10, TeX line 797); eq:reflection (6.5, PDF p.11, TeX line 816); eq:reversor (6.6, PDF p.11, TeX line 829)
- Evidence class: Recovered shift; standard definitions; deduction
- Source: P06 p.3 Eq.(1), p.8 equation-index entry(1); P14 p.10 §4.2
- Assumptions/limits: Two-sided signal domain for shift reversal; monochromatic nonzero frequency for quadrature; autonomous bijection for TFT=F^-1.
- Status: Supported identities; complete historical reversor unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C11 — The later R/D block has conditional exchange/quarter-turn commutation; the full update does not acquire these symmetries from one substage.

- Manuscript: sec:rd (6.3, PDF p.11, TeX line 838); eq:rd-block (6.7, PDF p.11, TeX line 857); eq:rd-parameters (6.8, PDF p.11, TeX line 863); prop:rd (6.2, PDF p.11, TeX line 871)
- Evidence class: Static code transcription; deduction
- Source: Infinity lines70–91,114–135,162–202
- Assumptions/limits: Fixed geometry for amplitude block; empty-row mask retained; spatial covariance transforms noise too.
- Status: Proved conditional identities; no trajectories executed
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C12 — The later driven memory ODE has a unique absolutely continuous convolution solution for specified input.

- Manuscript: eq:memory-ode (7.5, PDF p.14, TeX line 1048); eq:memory-solution (7.6, PDF p.14, TeX line 1057)
- Evidence class: Recovered equation and solution; proof
- Source: P14 p.5 Eq.(10), p.17 Eq.(25)
- Assumptions/limits: Locally integrable I(t), finite fixed coefficients and H(0); does not solve coupled PDE.
- Status: Proved in §7.3
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C13 — An onto pullback preserves the sup norm; the printed differentiable unit-normal map has a Jacobian eigenvalue one and no Euclidean fixed point.

- Manuscript: eq:normal-map (7.9, PDF p.14, TeX line 1121)
- Evidence class: Deduction; obstruction
- Source: P14 p.16 Eqs.(17)–(18), pp.17–18 §§E.3–E.4
- Assumptions/limits: Positive compression length; differentiable unit normal; onto domain for equality. No claim about a redesigned vector field or quotient map.
- Status: Proved; broader attractor claim unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C14 — The finite-core comparison requires consistent basis order and per-corridor factors; raw norm loss, normalization, conjugacy and generator signs are distinct.

- Manuscript: sec:later (8, PDF p.15, TeX line 1156); app:finite (B, PDF p.20, TeX line 1486)
- Evidence class: Recovered factors; conditional deductions; source conflicts
- Source: P15 pp.3–8 §§2–4; p.24 Appendix C; p.31 E.5; p.34 H.6; pp.44–45 M; p.49 O
- Assumptions/limits: A tensor B factorization follows stated per-corridor action. Literal Appendix C flip conflicts with its printed ordering. Prior corrected QSM/Bridge conventions are not re-audited or replaced.
- Status: Proved under stated conventions; source conflicts retained
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C15 — Solving the lock identity gives gamma≈0.0869947475; it is not an independent estimator or Euler–Mascheroni.

- Manuscript: eq:constant-lock (C.1, PDF p.22, TeX line 1672); app:sources (C, PDF p.21, TeX line 1630)
- Evidence class: Recovered identity; deduction; unresolved estimator
- Source: P01 p.3 Eq.(1); P06 p.4 Eq.(2), p.6 symbols; P19 pp.8–9 and p.13 Algorithm1
- Assumptions/limits: Constants and units require role-specific dictionaries. P19 GammaEstimate is unspecified.
- Status: Algebra supported; empirical provenance unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C16 — A selected explicit law, new contraction model or separate curvature observer would be completion choices.

- Manuscript: sec:conclusion (9, PDF p.16, TeX line 1217); eq:new-contraction (9.1, PDF p.17, TeX line 1281); app:coefficient (A.4, PDF p.19, TeX line 1427); app:new-model (A.5, PDF p.19, TeX line 1460)
- Evidence class: New-model comparison; unresolved historical choice
- Source: FOUNDATIONS-01 §9 and branch appendix §5; manuscript §9 and A.4–A.5
- Assumptions/limits: Complete invariant domain, Lipschitz constant and |chi|K<1 for sufficient theorem. No choice made or iteration executed.
- Status: Clearly separated from recovered intent
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C17 — Reciprocal echo membership and fusion predicates do not define a periodic orbit or merged state.

- Manuscript: sec:feedback-domain (2.3, PDF p.3, TeX line 232); eq:corridor (2.6, PDF p.4, TeX line 253); eq:fusion-predicate (2.7, PDF p.4, TeX line 259)
- Evidence class: Recovered definitions; deduction; missing rules
- Source: P03 p.3 §1.2, p.7 §3.2, p.10 §§4.1–4.3, p.12 §5.2
- Assumptions/limits: Distance symmetry, antisymmetric phase and reciprocal echo membership give a_ji=a_ij. Exact coefficient symmetry is (H_i-H_j)a_ij=0: equal memories are necessary only on nonzero-weight edges. A zero edge imposes no equality. No compensating loss term is printed.
- Status: E01 addressed: exact zero-weight qualification; following nonconservation example retained.
- Revision record: Localized qualification of previously accepted prose; earlier report preserved unchanged.

## C18 — The July REFU function is a clock schedule that decays and changes sign arbitrarily late on a continuous time domain.

- Manuscript: eq:H (7.1, PDF p.13, TeX line 981); eq:H-bound (7.2, PDF p.13, TeX line 994); eq:H-sign (7.3, PDF p.13, TeX line 1001)
- Evidence class: Recovered expression; analytical proof
- Source: P07 p.6 §3.1; REFU lines5–13; Infinity lines176–182
- Assumptions/limits: t>=0; sign sequence t=3pi/2+2pi n. This is not a claim about every discrete sampling or accepted trajectory.
- Status: Proved; normalization/insertion domain unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C19 — Stored trails, weighted embeddings and the echo observer are history/readout structures, without guaranteed lossless memory.

- Manuscript: eq:embedding (7.4, PDF p.13, TeX line 1022)
- Evidence class: Recovered observer; counterexample
- Source: P01 pp.5–7 §§3.2–3.5, pp.23–24 Appendix C; Echo lines10–43
- Assumptions/limits: Nonzero denominator; nonnegative weights for convexity. S_j and E are disclosed shorthand.
- Status: Supported; lossless inference rejected
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C20 — The scalar tanh module is a global contraction with unique fixed point zero; the drift map contracts only under a fixed-reference coefficient condition.

- Manuscript: eq:golden-tanh (7.7, PDF p.14, TeX line 1077)
- Evidence class: Recovered formulas; standard deduction
- Source: P08 p.1 §2.1; P03 p.13 §5.4
- Assumptions/limits: Real scalar tanh; for drift fixed reference and 0<alpha<2. Does not prove full-stack stability.
- Status: Proved conditional statements
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C21 — The literal Revolution series needs beta_n/alpha_n→−1/Omega_X, and that necessary condition is insufficient.

- Manuscript: eq:revolution (7.8, PDF p.14, TeX line 1103)
- Evidence class: Recovered expression; term-test counterexample
- Source: P13 pp.4,6
- Assumptions/limits: Fixed finite nonzero Omega_X and nonzero alpha_n. Replacing it by Omega_n adds a definition.
- Status: Proved; intended self-modification unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C22 — The curvature expression has a vector curl-curl reading under Euclidean hypotheses, while complex floor and competing phase laws remain undefined.

- Manuscript: sec:tensor (6.4, PDF p.12, TeX line 930); eq:curvature-tensor (6.9, PDF p.12, TeX line 935); eq:phase-feedback (6.10, PDF p.12, TeX line 958)
- Evidence class: Recovered expressions; identity; typing conflict
- Source: P13 pp.3,5,8–9
- Assumptions/limits: Smooth 3D vector field for identity; constant spatial phase for simple covariance; no canonical complex floor. Epsilon_theta is a disclosed renaming.
- Status: Identity supported; carrier and schedule choice unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C23 — The absolute-value identity has sixfold magnitude period; reflection of a regular tetrahedron need not create a Star-of-David projection.

- Manuscript: eq:sixfold (8.1, PDF p.15, TeX line 1164); sec:later (8, PDF p.15, TeX line 1156)
- Evidence class: Recovered identity; geometric counterexample
- Source: P14 pp.10–11 §§4.2–4.4
- Assumptions/limits: cos(delta)!=0 for nonzero pattern; specified regular tetrahedron and z=0 reflection. No universal impossibility asserted.
- Status: Proved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C24 — Three spin-half tensor factors have dimension eight and no total-weight-zero state; a six-dimensional direct sum differs.

- Manuscript: app:finite (B, PDF p.20, TeX line 1486)
- Evidence class: Elementary deduction; source inconsistency
- Source: P15 p.49 Appendix O
- Assumptions/limits: Three spin-half factors specifically, not all possible representations.
- Status: Proved; historical identification unsupported
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C25 — Horizon, single-mode threshold integral and entropy balance do not define a time-reversal dynamics.

- Manuscript: eq:horizon (C.2, PDF p.22, TeX line 1700); eq:threshold-integral (C.3, PDF p.22, TeX line 1716); eq:entropy (C.4, PDF p.23, TeX line 1723)
- Evidence class: Recovered expressions; elementary deductions
- Source: P06 p.4 Eqs.(3),(5); p.5 Eq.(7); p.6 symbols
- Assumptions/limits: Fixed radius; no temporal cosine inserted; no sum over modes inserted; total entropy conservation needs epsilon_f=0.
- Status: Identities retained; physical interpretation unresolved
- Revision record: Retained principal claim and v0.1 review scope; locators refreshed for v0.1.1.

## C26 — Twenty prior arithmetic certificates are reused as evidence, not rerun or substituted for proofs.

- Manuscript: app:evidence (D, PDF p.23, TeX line 1732)
- Evidence class: Prior finite algebraic evidence; provenance
- Source: FOUNDATIONS-01 ALGEBRA_CERTIFICATES.json A01–A20
- Assumptions/limits: Finite examples only; no new field update, model import, simulation or earlier suite replay.
- Status: Receipt copied unchanged; general claims rest on proofs
- Revision record: Twenty prior certificates retained byte-for-byte; no base, FOUNDATIONS, R0–R3 or reviewer check suite rerun. GPT reviewed v0.1; v0.1.1 awaits closure review.

