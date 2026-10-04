# Paper G claim-to-source and proof map

Paper G v0.1 - LOCAL REVIEW DRAFT - 4 October 2026. Section names and equation labels below refer to [the editable manuscript](source/paper_g.tex). The source manifests provide byte identities, not proof by hash. Exact-model results remain distinct from rounded runtime behavior.

## Controlling scientific records

| Authority | Exact controlling identity / local copy | Role |
|---|---|---|
| M1 accepted common core | SHA-256 `a14e5a108dc49c6f0c75950747567132993bd47b2d12ff7ee69d689a52768ef6`; [core](reproducibility/authorities/TRIOCTAGON_MAGNETISM_M1_COMMON_EQUATIONS_CANDIDATE_v0.2.md), [joint record](reproducibility/authorities/M1_JOINT_ACCEPTANCE_RECORD_v0.2.md) | CE01-CE09 and qualified CE11 are the paper's definitions/exact deductions. Candidate filename and old pending wording do not supersede final acceptance. CE10/S01 are separate ring scope; X01 is unadopted. |
| M2 joint acceptance | SHA-256 `17087119faf01256aea8c8673dacdfaf9c842eeaddedd2440ef958ad1c4537ce`; [record](reproducibility/authorities/M2_JOINT_ACCEPTANCE.md) | Controls local theorem, interval sign, odd remainder, corrected multiplier and scope. |
| M2 final corrections | [Claude correction](reproducibility/authorities/M2_CLAUDE_CORRECTIONS.md), [Codex assent](reproducibility/authorities/M2_CODEX_ASSENT.md) | Full nonlinear amplitude law, slaved coefficient convention, full-state reflected lift. Original report must be read with these corrections. |
| M2 exact certificate | SHA-256 `6fe4f3f314db1332712b31fed8f7a64cfcee892b9c07782018ea38d3749444a8`; [input](reproducibility/inputs/m2_accepted_certificate.json) | Integer endpoints over 2^240; fresh replay recomputes them rather than relying on the saved verdict. |
| Repaired M3 joint acceptance | SHA-256 `d2c2f6fd189befdbbe1d0c6c50d36c7946b4bbde6d789005f424e3df8e9e98ae`; [record](reproducibility/authorities/M3_JOINT_ACCEPTANCE.md) | Fixed-parameter entrance theorem, N=301, normalization and explicit non-continuation. |
| M3 corrected source | [Claude v0.2 review](reproducibility/authorities/M3_CLAUDE_REPAIRED_REVIEW.md), [Codex reconciliation](reproducibility/authorities/M3_CODEX_RECONCILIATION.md) | Actual final cross-review and repaired proof logic, including phase-parity summability. |
| M3 exact trap | [accepted support](reproducibility/inputs/m3_accepted_support.json), SHA-256 `10c4f505f11f1c85c87e3a91e76f61c36e2119a023b13d6dc26af77f9289ddb3` | `values.exact_receipts.Up` and `positive_weights` define the trap/norm exactly. `Um` is an outer image enclosure, not an equality. |

## Manuscript claims

| Manuscript location / label | Claim and evidence class | Source and verification dependency | Boundary retained |
|---|---|---|---|
| Section 1, `eq:amp`-`eq:full` | Adopted mathematical map | Current Paper A publication section 6.1; M1 CE04-05; current `dynamics.py` inspected read-only | Amplitude before simultaneous phase, real parameters, Arg0(0)=0; no physics or defaults inferred. |
| Section 2, `eq:SA`, `eq:gram` | Exact Gram/area identities | Paper B transported signed area theorem; M1 CE01; elementary cross-product algebra shown | Pair order and both Gram sign conventions stated; W=0 is weaker than area=0. |
| Proposition 1, `eq:T`-`eq:Ccov` | Exact attachment, rank, reconstruction, real-linear uniqueness | Paper B v0.1.2 actual frames; M1 CE02. Generator and commutant proof supplied | Uniqueness only among real-linear maps of C; unequal fixed k not S3-symmetric. |
| Section 2 nonlinear qualification | Exact K4 example and scope | M1 CE11 | Does not assert an exhaustive invariant classification, field, or physical time reversal. |
| Section 3.1, `eq:cof`-`eq:rotateS` | Exact finite-step identities | M1 CE04-05; algebraic expansion and pair-product proof | State-dependent cubic map; cofactor includes singular M; epsilon^2, epsilon*g and g^2 retained. |
| Proposition 2, `eq:hidden`-`eq:entrance` | Exact Fourier entrance conversion | M1 CE08; Atlas 08 endpoint context | c, epsilon and every b_i nonzero; expose existing area; no entrance preparation rederivation. |
| Section 3.3, `eq:zeroexception` | Conditional zero-area preservation and explicit exception/resonance | M1 CE05; exact accepted witnesses | No universal invariant zero-area cone or global phase/Gram closure. Unit phase factor and real r normalization. |
| Section 3.3 same-A witness | Exact failure of A-only closure | M1 CE06, factors 1 and 301/400 | No A-only state evolution/cache. |
| Section 4.1, host | Computer-assisted unique positive host | M2 integer Krawczyk certificate, recomputed by `gpt_m2_analytic_interval_review.py` | Approximate host coordinates are not proof premises. |
| Section 4.2, `eq:compression`, `eq:critical` | Exact quotient compression with interval spectral hypotheses | M2 derivation section 2, final joint record; certificate `critical_data` and Sylvester minors | Simple unequal-k crossing; no transfer of equal-k double crossing theorem. |
| Section 4.3, `eq:cnf`, `eq:cinterval` | Analytic coefficient convention plus outward sign certificate | M2 analytic degree-three jets, direct/slaved terms; final Claude correction sections 1-2 | c in (0.0865248497217,0.0865248497219); finite differences only historical consistency. |
| Theorem 3, `eq:normal`-`eq:Wscale` | Exact local consequence of certified hypotheses | Corrected M2; standard flip/center-manifold statements; proof gives factor four and reflected lift | Unknown sufficiently-small-mu range; orbital attraction; parameter-specific approximate prefactor. |
| Theorem 4 and `eq:entry` | Computer-assisted fixed-parameter capture | Repaired M3: 21 full updates, quotient through 300, extra validated step to301; direct enclosure | N301 sufficient, not first; norm squared3; exact lambda_c+1/200. |
| `eq:contraction` | Interval derivative plus Banach | Repaired M3 J2*J1, interval Fhat^2(center), positive chart bounds, exact Fraction decisions | q<=4789/5000 per TWO steps; complete convex box; no outer-image surjectivity assumption. |
| `eq:kraw` | Separate interval existence for H-symmetry | Repaired M3 Krawczyk image; support inverse-defect norm and Banach uniqueness | A small residual or H-equivariance alone would not establish symmetry of captured point. |
| Section 5.4, `eq:fulllimit` | Exact full-state conclusion and geometric phase summability | Reconciled M3 parity argument; smooth gauge bounds and q^m tail sum in text | One limiting rotation of full two-cycle; two raw gauge-phase limits. |
| Section 5.4 W/Gamma signs | Computer-assisted nonzero limits | Recomputed interval evaluation on Up and exact sign predicates | Finite coarse displays are outward statements; no physical field claim. |
| Conjugate entrance | Exact equivariance consequence | M1 conjugation; final repaired M3 assent | No norm-nine auxiliary log reused as entrance evidence. |
| Section 6 | Scope of persistence | Final M2/M3 records; M1 CE10/CE11 | M2-to-M3 continuation unproved, not prerequisite; no lambda=.5 link, global basin, binary64 theorem, M4 or X01. |

## Figures and data

All figures are generated by [make_figures.py](source/make_figures.py). The included [figure record](reproducibility/results/figure_record.json) identifies script, data and asset hashes. [Nominal CSV](reproducibility/results/nominal_trajectory.csv) is newly generated, not relabelled historical output.

| PDF figure | Source | Evidence class |
|---|---|---|
| Figure 1, `01_geometry_observable` | Paper B v0.1.2 exact centers/normals/tangents, M1 T and decomposition; correctly normalized nominal state at n=1 | Exact coordinate definitions rendered numerically; no spatial field interpolation. |
| Figure 2, `03_local_onset` | Unchanged `m2_nominal_onset.json -> values.amplitude_law_table`, rows 0.0001,0.0004,0.0016 | Original finite numerical observations, not rerun; leading asymptotic line, no certified parameter-range shading/continuation. |
| Figure 3, `04_capture` | Short nominal quotient replay; exact accepted trap/weights, q301, Zw and weighted row bounds | Nominal approach plus rounded display of interval certificate; five-coordinate inequalities supply proof. |
| Figure 4, `02_signed_trajectory` | 321-step 130-digit replay of accepted nominal formulation at exact-model parameter interpreted at high precision; q300/q301 checked against exact receipts | Numerical illustration only; signed even/odd series, late Gamma scale explicitly enlarged. |

## Corrections that must not regress

| Superseded wording/evidence | Controlling correction in this paper |
|---|---|
| Amplitude map is real-linear | M is real but depends on intensities; map is cubic. |
| Universal preservation of zero area / global Gram closure | Nonzero pre-sync condition or lambda=0; actual Arg0 zero exception and resonance retained. |
| M2 c sign is numerical only | Final analytic outward certificate supplies sign. |
| Emerging cycle two-step multiplier 1-2 sigma mu | 1-4 sigma mu + O(mu^2); host second iterate is different. |
| N300 lies in outer image, therefore captured | Direct Fhat(X300) subset X301 subset int Up at301. |
| U_minus equals actual image | E_minus is an outer enclosure; old `Um` JSON key retained verbatim. |
| Symmetry alone proves H-reflected captured cycle | Separate Krawczyk existence plus unique Fhat^2 fixed point. |
| Raw gauge phase has one limit | Parity limits beta and beta+theta_p; one rotation after factoring the cycle phase. |
| Original auxiliary 401-step symmetry run proves correct entrance | Withdrawn attribution (norm squared9); use squared-norm-three short replay and exact conjugation theorem. |
| M3 cycle is proved continued from local M2 branch | Unproved; no continuation attempted or required. |

## Primary literature check

Checked on 4 October 2026, confined to standard methods:

- Kuznetsov, *Elements of Applied Bifurcation Theory*, second edition: [actual text](https://wwwf.imperial.ac.uk/~dturaev/kuznetsov.pdf), printed pp.121-123, Theorems4.3-4.4; sections5.1-5.2 and5.4.2 for center manifolds/projection. The author's [chapter errata](https://webspace.science.uu.nl/~kouzn101/BOOK_ERR2.pdf) was also retrieved; the stated nondegeneracy and transversality conditions are retained. The paper derives its odd special-case coefficient convention explicitly.
- Contraction statement checked directly in the same author's Theorem1.3, printed p.17: self-map of a complete metric space with Lipschitz constant strictly below1. Banach1922 is the historical citation; the original bibliographic entry was checked at the university [publication catalogue](https://kielich.amu.edu.pl/Stefan_Banach/e-publications.html). The 1922 PDF/DOI retrieval failed, so this package does not claim a fresh reading of that original proof. The complete hypothesis and convergence estimate used are supplied in Paper G.
- Rump and Graillat: [author-hosted paper](https://www.tuhh.de/ti3/paper/rump/RuGr09.pdf), Theorem2.1, on strict interval inclusion for simple roots of a C1 system. [University publication record](https://tore.tuhh.de/entities/publication/8cb5b317-0f4b-4259-8396-b1f34cd0e3a8) verifies Numerical Algorithms54(3),359-377(2010). Its multiple-root results are not imported.

These are references to actual theorem statements, not an external novelty review or external peer review. No full external PDF is redistributed.
