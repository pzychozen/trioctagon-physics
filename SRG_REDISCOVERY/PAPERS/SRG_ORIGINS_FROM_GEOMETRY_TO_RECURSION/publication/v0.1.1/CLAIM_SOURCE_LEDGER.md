# Claim-to-source ledger — SRG Origins v0.1

11 October 2026. Each row identifies one substantive claim and its strongest source or proof. H = historical definition/claim; D = mathematical deduction; A = later analytical choice; U = unresolved. “H” certifies recovery, not truth of an empirical assertion. Titles, public access routes and source hashes are resolved in [SOURCE_INDEX.md](SOURCE_INDEX.md). Code lines count from one, including any BOM. Report locators refer to the technical sections of [SRG Origins](manuscript/SRG_ORIGINS_v0.1.md). The original 61 claims are retained, with the accepted source-and-notation addendum and the explicit presentation additions below.

| ID | Claim | Classification / provenance of choice | Precise source or proof | Report locator / disposition |
|---|---|---|---|---|
| L01 | Equal-circle intersections lie on the midpoint line | D from declared equal circles; H analogy | Rainman p.3; subtract the two circle equations | §3.1, Eq.(3); proved |
| L02 | 45°/135° projection product is 1/2 | D; chosen angles, not a lock selector | Elementary sine/cosine values | Eq.(2); proved |
| L03 | Equilateral inradius/side squared is 1/12 | D; classical geometry reused by October | Received Geometry–Zeta note §§1–2; area proof here | Eq.(4); original-circle radius distinguished from circumradius |
| L04 | Canonical vesica does not itself derive a golden ratio | U selection gap | Eq.(3) fixes midpoint and height; pentagon adds different assumptions | §3.2 |
| L05 | Pentagon diagonal/side is φ | D | Cyclic-quadrilateral relation d²=s²+sd | §3.2; positive root |
| L06 | Fibonacci ratios tend to φ | D; specific recursive rule | Closed-form solution and decaying second root | Eq.(5); proved |
| L07 | Compound-growth limit is e | D | Logarithm integral bounds | §3.3; proved |
| L08 | Three integrations yield Li₃ and then ζ(3) | D; three is an observable choice | Rainman p.23; DLMF 25.12; positive-series proof | Eqs.(6)–(7) |
| L09 | Rainman scaled endpoint gives Li₃(a), not invariant ζ(3) | D correcting H | Rainman p.24; explicit pullback including numerator a | Eq.(8); counterexample a=1/2 |
| L10 | Rainman takes γ* as input | H | Rainman pp.18,20,24 | §4.3; not independent selection |
| L11 | Printed translated-line image has wrong sign | D correcting H | Rainman p.21 displayed T and displayed image | §4.3; forward substitution proves distinction |
| L12 | Claimed intersection chain lacks a dimension/map proof | U | Rainman pp.20–24, compare curve intersections with X³ integral | §4.3; not completed here |
| L13 | Non-singularity alone does not prove ambient spanning | D | Rainman p.18 Lemmas 12.2–12.3; vector (1,0) counterexample | §4.3 |
| L14 | Golden trilogarithm identity is exact | D; classical identity, October reuse | DLMF 25.12 identities; derivative and limit proof | Eqs.(9)–(10) |
| L15 | Golden finite-interval integrals give ζ(3)/10 and π²/20 | D; classical, not project discovery | Markov 2024 pp.305–308 Eqs.(2),(3),(8),(11); expansion proof | Eq.(11) |
| L16 | Golden-series evaluation has a geometric tail bound | D | Positive remainder of Li₃ at φ⁻² | §4.4 after Eq.(12) |
| L17 | Cycle Fourier eigenvalues are 4N² sin²(πk/N) | D from A scale | Received Geometry–Zeta note §3; Fourier substitution | Eq.(13) |
| L18 | Fixed circumference and zero-mode removal are new diagnostics | A introduced in 9 October note | Received note §§1,3,5,6 | §§5.1–5.3 |
| L19 | Exact finite inverse trace is (1−N⁻²)/12 | D | Finite sine product and cot derivative | Eqs.(14)–(15); exact matrix corroboration |
| L20 | Full-spectrum inverse-power limit is 2ζ(2p)/(2π)^(2p) | D; p>1/2 | Dominating bound λ≥16k² and paired modes | Eq.(16); general proof |
| L21 | Restricted repeated-triad inverse trace tends to zero after N² scaling | D | Only modes 0,N/3,2N/3 survive | §5.2; distinct from full spectrum |
| L22 | Prefactor 4π²/(eφ) imports historical target | A, explicitly chosen in October | Received Geometry–Zeta note §5 | Eq.(17); not native selection |
| L23 | Sampled-minus-bulk finite part tends to −1/12 | D with A observable/subtraction | Finite sine sum, cot Taylor series; received note §6 | Eqs.(18)–(20); sign proof |
| L24 | Half-integer modes change cutoff constant to +1/24 | D | Derivative of 1/(2 sinh(t/2)) | Eq.(21) discussion; boundary/mode choice matters |
| L25 | July lock was printed, not inferred by October analysis | H | P06 p.4 Eq.(2); P01 p.3 Eq.(1) | Eq.(1), §6.1 |
| L26 | P06 identifies γ as Euler–Mascheroni, inconsistent with lock | H plus D contradiction | P06 p.6 glossary; substitute into Eq.(1) | §6.1; retained source conflict |
| L27 | P01 says empirical/calibrated and not first-principles derived | H claim | P01 pp.3–4 §§2.2–2.3 | §6.1; no raw estimator implied |
| L28 | P19 GammaEstimate lacks an implemented specification in bounded sources | H placeholder / U implementation | P19 p.13 Algorithm 1; bounded search receipt | §6.2 |
| L29 | P19 γ=0.10 table is labelled an example | H | P19 p.12 “Run Stamp (example)” | §6.2; not measurement receipt |
| L30 | March JSON gamma is formula-assigned | H code/data | srg_resonance_lock_analysis.py lines 42,453–466; resonance_lock_results.json | §6.3; six nonfinite lock times |
| L31 | March CSV gamma column is a prediction | H code/data; D audit | Tower II lines 289–318; master_equation_verification.csv | §6.3; 90 rows,45 predictions,45 blanks |
| L32 | Literal informal phrase has no match in bounded supplied text | U naming | Accepted private bounded-search receipt: 278 supplied files; personal paths not republished | §6.4; not universal negative |
| L33 | Scalar equation equal to one is a distinct approximate multiplier condition | H plus D qualification | srg_resonance_lock_analysis.py lines 293–327 | §6.4; ε and linearization assumptions exposed |
| L34 | DieGlocke ratio is algebraically different from July lock | H plus D | DieGlocke_Sim_Core.py lines 6–14 | §6.4; product versus quotient |
| L35 | Provided DieGlocke Run does not use that ratio for feedback | H static data flow | DieGlocke_Run.py lines 11–16,37–46 | §6.4; fresh field product by t |
| L36 | P13 has a distinct named master operator | H / U typing | P13 p.5; accepted SRG-I §6.4, physical pp.12–13 | §6.4; not identified with scalar lock |
| L37 | June golden-tanh map is bounded and contractive on real scalars | H plus D | P08 p.1 §2.1; derivative ≤φ/√3<1 | §7.1 |
| L38 | Surviving TGMO is a minor-circle sampler | H plus D geometric reading | early/TGMO.py lines 5–14; P05 p.1 | §7.1 |
| L39 | Surviving REFU file is H(t), not a complete next-state update | H | early/REFU.py lines 5–13; P05 p.1 | §7.1 |
| L40 | Surviving RPCO file is a damped angular field | H | early/RPCO.py lines 5–13; P05 p.1 | §7.1 |
| L41 | Constant radius and spatial radius give different Laplacians | H alternatives plus D | P11 pp.1–2; Δr=1/r for r>0 in 2D | §7.1; no source repair |
| L42 | P03 temporal rule reduces to an implicit relation | H plus D; scalar/frozen feedback assumption explicit | P03 pp.7–8; accepted SRG-I §3.2, Theorem 3.1, physical pp.4–6 | Eq.(22); full branch proof |
| L43 | July patch uses a position graph, not the temporal trail equation | H | P05 p.2; early/recursive_field_evolve.py | §7.1; no solver equivalence |
| L44 | January TGMO is a unit-step periodic difference with anisotropic coefficients | H | JANUARY p.2; tgmo.py lines 4–46,86–99 | Eq.(23) |
| L45 | That stencil is not automatically the embedded torus metric Laplacian | D | SRG-I §5.3, physical p.9, Eq.(5.7); January tgmo.py lines 62–76; induced metric/divergence proof with January angle names | §7.2 |
| L46 | January nonlinear/spatial terms use same input; H precedes RPCO | H | JANUARY p.3; refu.py lines 109–138; app.py lines 234–246 | Eq.(24) |
| L47 | January H is prescribed and sampled normalization is source-specific | H | refu.py lines 8–31 and run_refu; accepted OC01 normalization discussion | §7.2 |
| L48 | RPCO paper and signed branch laws differ at negative inputs and zero | H plus D | JANUARY p.3; refu.py lines 37–69 | Eq.(25) |
| L49 | Paper reciprocal pairing and signed oddness are exact, not time reversal | D | Symmetric logarithmic clamp algebra | §7.3 |
| L50 | P07 sign-retention prose and P18 reciprocal prose contradict their equations | D checking H | P07 p.3; P18 p.4 Eq.(2) | §§7.1,7.3 |
| L51 | OC01 zero regularity, zero-gain, sample-count and custom-H corrections remain | Accepted D reused | Internal Operator Composition 01 report, hash in SOURCE_INDEX.md, RPCO and source-caveat sections; received OC02 review | §7.3 |
| L52 | 3×3 example follows the same-input composition | D; chosen example values | Algebra from Eqs.(23)–(25) | Eq.(26); scalar corroboration, no field call |
| L53 | March source explicitly acknowledges particle adaptation | H | Seed Explorer line 29 and lines 53–57 | §8.1 |
| L54 | Seed Explorer's gamma is unused; first H time is one | H static source | Seed Explorer lines 74,139–169; full-file gamma search | §8.1 |
| L55 | Infinity uses assigned gamma in unequal R/D coupling | H | Infinity lines 91,114–137,176–195 | Eq.(27); not exchange symmetry |
| L56 | Golden Tower assigns bands and mixes amplitudes | H | Golden Tower lines 72–94,122–179 | §8.1 |
| L57 | Tower II adds nonlinear mixing before H and preclip fusion | H recovered stages | Tower II lines 135–213; accepted R0 report | Eq.(28) applies only after both row guards pass; skipped rows retain incoming R at that stage. H/fusion/RPCO/noise follow; no zeta in update |
| L58 | Frequency master equation shifts odd-zeta index by one | H plus D | P18 p.5 Eq.(6), p.7 Eqs.(10),(12) | Eq.(29),m=n+1 |
| L59 | Frequency formula has a pole/domain restriction | D; source skips low arguments | Eq.(29); Tower II lines 293–298 | §8.3; positive-series domain explicit |
| L60 | OC01–02 fixed-state results are later deductions with limited scope | Accepted D reused | Internal Operator Composition 01 report, hash in SOURCE_INDEX.md and internal Operator Composition 02 report | §7.4; no transfer to particles |
| L61 | No independent native selector or gamma measurement recovered | U bounded conclusion | Accepted private provenance and named-reference search receipts; rows L25–L35 | §6.4; bounded absence, not a universal negative |

The ledger does not claim the original authors derived the modern proofs in this report. Nor does reuse of an accepted report imply execution of its checks or review of all its ancillary files.


## Presentation and addendum claims

| ID | Claim | Classification | Source and exact disposition |
|---|---|---|---|
| O01 | P01 explains the roles of the constants and reports gamma about .087 | H interpretation, not a first-principles proof | P01 Appendix A, physical pp.19–20; paper §6.1a and walkthrough page 3; source excerpt visually checked |
| O02 | Three SRG-I references are corrected | Editorial source correction A01 | Scalar theorem §3.2/pp.4–6; torus §5.3/p.9/Eq.(5.7); complex typing §6.4/pp.12–13 |
| O03 | January embedding uses theta major, phi minor | H convention plus D metric | tgmo.py lines 62–76; paper §7.2. Both consistent relabellings give the same geometry; neither equals the constant stencil |
| O04 | Tower II has two resonance-stage skip guards | H scope correction A03 | srg_golden_tower_II.py lines 151–163: no selected neighbours or raw weight sum <1e-10; §8.3 |
| O05 | Six-site eigenvalue list and all three displayed values | D illustration of A diagnostic | Substitute N=6 into Eqs.(13),(18),(19): 36,108,144,108,36; inverse sum 35/432; inverse 3/2 sum 0.011619908238239586…; remainder −0.083716607756… |
| O06 | Zero corners distinguish two compressor modes | D from H, illustrative chosen parameters | Eqs.(23)–(26); walkthrough p.4, no source-step execution |
| O07 | H is clock-prescribed, not a state accumulator | H data-flow reading | January refu.py lines 8–31,109–138; §7.2. A separate state-based memory claim requires its own definition |
| O08 | No blanket reuse licence or institutional endorsement is created | Publication disposition | PUBLICATION_DISPOSITION.md; assistance statement in paper §10 |

The exact accepted-report-to-reading-edition and accepted-ledger-to-public-ledger diffs are retained in the private final review package. They show the citation/convention/guard corrections, Appendix A explanation, reader navigation and private-path removal. They do not alter any frozen historical source or earlier result.
