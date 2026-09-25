# Paper F theorem and provenance ledger v0.2

**Successor scientific ledger, 25 September 2026.** The original v0.1 ledger remains unchanged.
All proposed manuscript claims are conditional mathematics of the specified map.
This ledger records Codex reconstruction for GPT/Hilmir review, not publication acceptance.

Source identifiers: **PA** = accepted Paper A §§1,6.1; **PB** = Paper B v0.1.2 §§5–8;
**CT** = `CHIRAL_TRANSVERSE_REPORT.md`; **AX** = `TRANSVERSE_AXIS_FALSIFICATION_REPORT.md`;
**CG** = existing Claude generic-transverse review; **NF** = `TRANSVERSE_NORMAL_FORM_CLOSEOUT.md`.
Exact paths and raw identities are in `PAPER_F_SOURCE_CENSUS.md`.
**CR** is the delivered `reviews/CLAUDE_PAPER_F_ADVERSARIAL_REVIEW_v0.1.md`, preserved byte-for-byte. Its acceptance applies to v0.1 within its reviewed scope, not a new review of v0.2.
**PF-check** is `paper_f_exact_checks_v0_2.py`; the original verifier is preserved. The successor imports neither the kernel nor any old verifier.

## Shared hypotheses and source separation

- **H0:** three complex channels, real parameters, equal amplitude coefficients k=(1,1,1), negative Laplacian L3=ee^T-3I. The phase update follows the amplitude/coupling update, simultaneously.
- **H1:** near e, all pre-sync entries and the channel mean are nonzero; common phase can be fixed by a real-positive mean.
- **H2:** seed e+i h q(phi), h>0 sufficiently small; signed angle atan2(C dot (-q), C dot q_perp).
- **H3:** zero phase strength; polynomial jet recurrences allow real parameters and unrestricted r. Defining kappa by division requires a=1-3g nonzero; the chosen oriented atan2 branch additionally requires a>0. Finite-n statements are local in h for each n.
- **H4:** 0<r<a<1, m=1-a+r, with r=a-2 epsilon; gauge spectrum (m,r,r,a,a) nonresonant. H4 is for analytic asymptotic conclusions, not an extra requirement on exact finite coefficient recurrences.
- **H5:** specified historically selected point epsilon=1/20, g=1/5, hence a=2/5, r=3/10, m=9/10. Selection rationale is OPEN; these are not general-theorem assumptions.
- **H6:** an open real interval J0 containing zero, with 0<r<b(lambda)<1, 0<m<1 and nonresonant spectrum (m,r,r,b,b). Uniformity and a common nonzero chart apply on compact subintervals. At H5, J=(-7/2187,12579511/3600000000); the explicit symmetric choice is |lambda|<7/2187. The expansion in lambda is about zero and controlled only to first order.

Parameter-general formulas come first. H5 only specializes them, proves a particular nonresonance instance and supplies quoted fractions. Historical seed calculations have their own explicit input.

The algebra uses the ideal real-arithmetic recurrence and exact rational interpretations of the specified decimals. Binary64 coefficients/rounding in saved experiments are a separate evidence class; the analytic and valuation theorems are not claims about a rounded bitwise map.

## F1 — Synchronized manifold and transverse space

**Statement/hypotheses:** Under H0, Omega=w e maps to [1+epsilon(1-|w|^2)]w e; the phase increment is zero whenever nonzero, and the stated zero convention preserves common zero. L3 e=0, L3 z=-3z on e-perp.
**Definitions:** e=(1,1,1)^T; e-perp is a real plane and its complexification as appropriate.
**Exact provenance:** PA §§1,6.1; accepted dynamics.py L3/_advance/phase_sync; CT §2.
**Proof:** direct substitution and multiplication, with local smoothness separated from zero-state invariance.
**Verification:** PF-check F1 identities; previous implementation tests are historical evidence, not fresh runs.
**Numerical evidence:** unnecessary for the theorem.
**Dependencies/known mathematics:** elementary permutation representation; “standard representation” means the complement to the trivial line in the permutation representation, defined here.
**Interpretation/exclusions:** intrinsic channel synchronization; not shell placement, clock synchronization or Paper A's larger-ring normal stability.
**Recommendation:** include as an elementary proposition, no novelty claim.
**Open issue:** no mathematical gap; physical motivation of the adopted law is outside the proof.

## F2 — Exact chirality decomposition

**Statement/hypotheses:** For real x=alpha e+xi, y=beta e+eta, with xi,eta in e-perp,
C=e cross (alpha eta-beta xi)+xi cross eta. The first term is transverse; the second parallel to e.
**Definitions:** raw, unnormalized C=x cross y in oriented channel coordinates.
**Exact provenance:** PB §6 and Proposition 5; CT §3.
**Proof:** bilinearity; e dot (e cross z)=0; two transverse vectors span e-perp or are dependent, so their cross product is normal (including zero). PF-check also checks components directly.
**Verification/numerics:** exact PF-check F2; no numerical premise.
**Dependencies/known theorem:** elementary cross-product identities; no new general theorem.
**Interpretation/exclusions:** after common-phase gauge, C=(1+mu)e cross y+x cross y. If y is nonzero, elevation ratio is at most ||x||/[sqrt(3)|1+mu|]. Relative synchronization with nonzero common amplitude forces plane approach. Absolute approach to zero does not.
**Recommendation:** include as a lemma and conditional corollary.
**Open issue:** no proof gap. Physical meaning is not established.

## F3 — Historical directional resolution

**Statement/hypotheses:** For the specified seed (1/5+3i/10,-2/5+i/10,1/10-i/5), its mean is (-1+2i)/30. The unit rotation (-1-2i)/sqrt(5) makes it sqrt(5)/30 and gives tangent chirality (7/300)(-1,-1,2), longitudinal chirality (7/75)e.
**Exact provenance:** original gate work order §6; GPT axis-falsification order §1; AX §2. Earliest located joint seed/parameter selection is recorded in the census, not asserted to be the historical origin.
**Proof/verification:** independent exact rational/radical calculation, PF-check F3.
**Numerical evidence:** previous historical trajectories motivate the question; they do not prove global convergence or exact late axis equality.
**Dependencies:** F2; no external theorem for the decomposition.
**Interpretation:** explanatory exact example. Relative synchronization makes the longitudinal/transverse ratio vanish; at the local linearized level their orders are r^n a^n versus a^n. The full argument uses the ratio bound, not a claimed exact finite-amplitude rate.
**Exclusions:** the historical seed has relative distance 2 sqrt(5) from its mean, so it is not itself a small perturbation. The theorem does not prove that seed reaches the unit synchronized circle, nor that its transient cannot rotate the tangent direction.
**Recommendation:** motivating case study, not a universal-direction theorem.
**Open:** HISTORICAL_SEED_PROVENANCE=OPEN; selection motivation cannot be supplied.

## F4 — Transverse circle and group action

**Statement/hypotheses:** Under H0–H2, u=(1,-1,0)/sqrt(2), v=(1,1,-2)/sqrt(6) are positively oriented with u cross v=e/sqrt(3). P=(C,A,B) acts by phi+2pi/3, T=(12) by pi-phi. Complex conjugation acts on the seed by phi+pi.
**Proof:** exact 2x2 matrices E^T P E and E^T T E; relations P^3=T^2=1, TPT=P^-1. Conjugation commutes and extends to a rotation of pi/3.
**Provenance:** PB Proposition 5 for the raw observable; AX basis; CG §§3–4; independent PF-check F4.
**Known mathematics:** standard S3 representation and dihedral presentation, explicitly demonstrated; no literature novelty inference.
**Numerics:** none required.
**Interpretation:** D_n means the planar dihedral group of order 2n: D3 has 6 elements, D6 has 12.
**Exclusions:** this is a channel seed-circle action, not an ambient shell symmetry identification.
**Recommendation:** include proof with matrices.
**Open issue:** none.

## F5 — Exact one-step harmonic selection

**Statement:** Under H0,H2,H3, C1=A_C q_perp+B_C q+D_C ehat, with
A_C=sqrt(3)h[a-epsilon h^2(2a+3)/6+epsilon^2 h^4(5+cos6phi)/36],
B_C=sqrt(3)epsilon^2 h^5 sin6phi/36,
D_C=sqrt(6)epsilon h^3(2a-epsilon h^2)cos3phi/12.
Hence psi1= -epsilon^2 h^4 sin6phi/(36a)+O(h^6).
**Provenance:** CG §2, AX exact source expansion; reconstructed in PF-check F5.
**Proof:** one substitution into the cubic, component-product identities and cross product.
**Symmetry versus coefficients:** permutation/conjugation parity forces sin(6j phi) in the in-plane angle and cos(3(2j+1)phi) in signed elevation. Polynomial degree excludes an in-plane term below h^4 and permits only sin6phi there. The displayed numerical coefficients require this recurrence, not symmetry alone.
**Verification:** PF-check exact projections and harmonic generator laws.

**Cleaner invariant explanation:** each h^k chirality coefficient is a homogeneous degree-k polynomial on the full plane V. Establish the degree bound before imposing unit norm. On the unit circle, I3=sum(q_j^3)=sin(3phi)/sqrt(6) and Delta=(q1-q2)(q2-q3)(q3-q1)=cos(3phi)/sqrt(2), so sin(6phi)=4sqrt(3) I3 Delta. Alternation forces divisibility by Delta; even parity and the absence of a symmetric linear polynomial on V exclude degrees two and four. Degree six is the first permitted alternating-even term. The proof remains direct; Stanley §4 supplies verified literature context.
**Numerics:** earlier Claude runs are attributed finite evidence only, unnecessary for the proof.
**Dependencies/known mathematics:** F4 plus polynomial degree/equivariance; external invariant-theory citation is optional positioning, not a missing proof.
**Exclusions:** allowed harmonics can have zero coefficients at special parameters. No physical source or attractor inference.
**Recommendation:** include exact proposition; label SYMMETRY_FORCED separately from RECURRENCE_SPECIFIC_COEFFICIENT.
**Open:** none.

## F6 — Isotropy classes; correction to the order's candidate wording

**Correct statement:** Twelve oriented roots phi=k pi/6 have THREE D3 orbits: k even (six), {1,5,9}, {3,7,11} (three each). Under D6 there are two orbits, even/odd k. After antipodal identification, D3 has two projective orbits of three axes each.
**Counterexample to supplied wording:** T fixes v, so its D3 orbit has size 6/2=3; -v is in the other three-element oriented orbit. It cannot be one six-element v-type D3 orbit.
**Stabilizers:** u is fixed by conjugation composed with T, while v is fixed by T. Their full-state fixed subspaces are (x+i y,x-i y,z) with x,y,z real, and (a+i b,a+i b,c+i d).
**Proof:** exact group enumeration and fixed-space algebra. Chirality is y(z,z,-2x) in the first and (ad-cb)(1,-1,0) in the second.
**Provenance:** CG §4 and AX §4 supplied the correct two structural types but insufficient oriented-orbit wording. PF-check F6 establishes the correction.
**Review correction:** CR §3.6 retracts Claude's own earlier phrase “regular D6 orbits.” The size-six orbits have order-two stabilizers in the order-twelve group. This is distinct from the corrected D3 orbit count. No original review text was changed.
**Dependencies:** F2,F4; standard orbit-stabilizer counting, also enumerated directly.
**Numerics:** none needed.
**Interpretation/exclusions:** zero projective in-plane drift for u-type with possible elevation; v-type chirality lies on a fixed transverse line. Oriented signs may reverse outside the chosen small local regime. A zero transverse projection has no in-plane angle even if total chirality is nonzero; total zero also has no direction. These are invariant isotropy subspaces, not attractors.
**Recommendation:** include corrected theorem and explicit orbit table.
**Open:** no unresolved mathematical issue; the incorrect two-D3-oriented-orbit claim is rejected, not published.

## F7 — Two-seed diagnostic/falsification

**Inputs:** e+i(1/1000)u and e+i(1/1000)v; H5 and lambda=0; eight recorded updates each.
**Provenance:** AX §§3–7, immutable CSV/JSON and original scripts; all identities pinned in census.
**Proof:** the two complete invariant-subspace chirality formulas in F6 are orthogonal whenever defined.
**Verification:** PF-check F7 reads all 18 rows, checks index sequence/validity and recomputes raw cross products from saved states. It performs no new update.
**Numerical status:** preserved binary64 observations: A drift at most 1.1785113164e-8 rad, B drift zero, measured mutual axes 90 degrees at each row; min norm approximately 1.1351167546e-6.
**Dependencies:** F6; no external theorem.
**Interpretation/exclusions:** falsifies unrestricted rapid universal-axis collapse for these nonvanishing seeds; the exact symmetry result is stronger than the eight-row diagnostic. The chosen pair does not characterize generic dynamics.
**Recommendation:** short diagnostic example or appendix, not the primary theorem.
**Open:** no missing output. The historical rationale for parameter selection remains separate.

## F8 — Arbitrary-step coefficient theorem

**Statement/hypotheses:** H0,H2,H3, with a>0; for every finite n, psi_n=kappa_n h^4 sin6phi+O(h^6), with fixed-n remainder. Full real h^2,h^4 and imaginary h,h^3,h^5 coefficients include common modes.
**Provenance:** NF §§3–4 corrected CG's finite-range proposal. PF-check derives the needed scalar recurrences independently in the universal three-root algebra t^3=t/2+sin3phi/(3sqrt(6)).
**Proof:** induction in the complete jet system; F=E+A D, K=R-X D give kappa=K/(2A). For t_n=(a^(2n)-r^n)/(a^2-r), f_n has three-rate forcing filtered by r. Thus Delta_(n+1) spans a^(4n),(a^2 r)^n,r^(2n),r^n. Finite geometric sums yield kappa_n.
**Structural closure:** channelwise polynomial jets have symmetric coefficients. On V these reduce using the degree-two and degree-three symmetric invariants; on the unit circle the cubic root relation reduces to the finite span e,q,s2. Homogeneity before restriction and equivariance fix the allowed powers of S through degree five.
**Verification:** PF-check F8 derives the coefficient lift, arbitrary-index t/convolution identities and forcing decomposition without trajectory fitting.
**Numerics:** neither previous nine symbolic steps nor later high-precision trajectories are used as proof.
**Dependencies/known theorem:** F4,F5, elementary formal Taylor algebra and geometric sums.
**Exclusions:** at a!=0 all rate-collision singularities in the distinct-rate representation are removable by the polynomial jet recurrences followed by division by 2a^n. kappa_n itself is not claimed polynomial at a=0. A finite-n expansion alone is not uniform in n.
**Recommendation:** principal theorem, parameter-dependent.
**Open:** none after exact reconstruction; domain conditions must remain in manuscript.

## F9 — Infinite coefficient sum

**Statement/hypotheses:** The formal coefficient series converges absolutely for |a|<1, |r|<1, a!=0, including negative parameters. The rational expression is unchanged from equation (11) of NF / equation (40) of Paper F. Rate-collision singularities are removable. At H5 it reduces exactly to 13375/1107936648.
**Proof:** sum t_n^2, a^(2n)t_n, a^(4n), and the filtered f_n; independent coefficient-lift resolvent gives the same rational function.
**Verification:** PF-check F9 derives both sums independently of saved stdout; exact numerator/denominator and decimal are saved.
**Provenance:** CG Appendix F proposed the conditional expression; NF proved the all-n law; this packet reconstructs it.
**Dependencies:** F8. Identifying it with the observed limiting-angle coefficient additionally requires F10–F12, not just a convergent formal series.
**Numerics:** 80-digit evaluation is an illustration of an exact rational, not precision of a historical experiment.
**Interpretation:** positive limiting coefficient at H5, opposite the first-step sign in the fixed convention.
**Exclusions:** no global basin claim; historical motivation for H5 is OPEN.
**Recommendation:** theorem for the sum and explicitly qualified local asymptotic corollary.
**Open:** no derivation gap.

## F10 — Five-real-coordinate local spectrum

**Coordinates:** gauge Omega=(1+mu)e+x_u u+x_v v+i(y_u u+y_v v); mean positive real.
**Statement:** on-site derivative at e is (delta real,delta imag) -> ((1-2epsilon)delta real,delta imag). Coupling gives m=1-2epsilon and r=1-2epsilon-3g twice, a=1-3g twice. Full phase composition changes a to a(1-9lambda).
**Provenance:** accepted runtime; CT §2, CG §5, NF §6. PF-check differentiates the cubic before specializing.
**Proof:** Jacobian with explicit chart embedding/extraction; common imaginary mean is removed.
**Verification/numerics:** exact PF-check F10; no numerical Jacobian needed.
**Dependencies/known mathematics:** real derivative; inverse function theorem after nonzero multipliers.
**Interpretation/exclusions:** derivative is real-linear in the original complex amplitudes. No holomorphic claim in C^3; no ungauged five-versus-six-dimensional confusion.
**Recommendation:** include calculation, then H5 multiset (9/10,3/10,3/10,2/5,2/5).
**Open:** H5 selection rationale, not spectrum derivation.

## F11 — Nonresonance and external theorem

**Statement:** At H5 every eigenvalue has v5=-1. Any monomial of total degree d has v5=-d. Equality to a target would require d=1, excluding all nonlinear resonances.
**Hypotheses/exceptions:** nonnegative integer exponents, repetitions included individually; zero exponents contribute zero. The phase eigenvalue 1 is not in the five-coordinate quotient. All multipliers are nonzero.
**Provenance:** NF §6; new exact valuation checks and written all-degree proof.
**External theorem:** Abate, Proposition 5.10 (formal nonresonant linearization), Theorem 5.15 (attracting Poincare-domain analytic linearization), checked in the author's PDF, printed pp.35–36.
**Application:** complexify five real analytic gauge coordinates; verify invertible, diagonalizable derivative, attraction and nonresonance. The symmetry group acts linearly on these coordinates, so conjugation by a symmetry produces another tangent-to-identity conjugacy. Uniqueness forces equivariance and preservation of the real slice. The common-phase multiplier one has been removed.
**Verification:** PF-check F11 checks exact valuations; the arbitrary-degree inference is a proof, not a finite search.
**Numerics:** none needed.
**Interpretation/exclusions:** the valuation proof is specific to H5. Parameter-general statements assume nonresonance or establish it separately. External analytic-linearization theory is established mathematics, not a claimed new theorem.
**Recommendation:** separate model-specific arithmetic lemma, external theorem and checked application.
**Open:** no missing external-theorem hypothesis for the stated local case.

## F12 — Local dynamical interpretation

**Statement/hypotheses:** H1,H2,H4 (or H5 satisfying H4). For sufficiently small h>0 in the specified seed family, C_n!=0 at every update and C_n/||C_n|| converges to a unit vector in V. The imaginary transverse direction is projectively constant in linearizing coordinates; the observed channel direction tends to a nearby initial-data-dependent limit. Chirality magnitude tends to zero.
**Proof:** uniqueness makes the conjugacy conjugation-equivariant, so its imaginary part is odd in the imaginary transverse variables. Each nonlinear inverse-chart term contains one such factor and at least one further contracting factor; divide by a^n and use uniform analyticity. C elevation then vanishes by F2. On the seed circle the limiting angular map is a near-identity diffeomorphism for small h.
**Provenance:** NF §6; CR §3.4 confirms the delicate coefficient bridge. The successor explicitly uses a fixed complex h-disk, Weierstrass convergence and the Cauchy coefficient formula. Uniform parity estimates establish nonzero chirality at every update.
**Verification/numerics:** exact hypotheses F10,F11; this analytic inference is not certified by a finite test count.
**Known theorem:** F11 application.
**Interpretation:** “neutral” describes projective direction in linearizing coordinates; all state eigenvalues still contract. A universal local six-axis selector is excluded for this near-synchronized seed family.
**Exclusions:** not neutrality of state amplitudes, not global dynamics, and no direction assigned to C=0. Do not claim all finite-amplitude angles are fixed or that no other attractor exists elsewhere.
**Recommendation:** qualified local corollary.
**Open:** no gap under stated hypotheses.

## F13 — Correct composition and observable distinction

**Statement:** the accepted operation order is amplitude/coupling, then simultaneous phase synchronization. Isolated phase angle p=hq gives 243/160, not the full raw-chirality coefficient for Omega=e+i hq.
**Proof:** expand p=arg(R+iI) and z exp(i lambda H), including changed amplitude-coordinate real parts and the changed tangent denominator.
**Provenance:** accepted `_advance` and `phase_sync`; PA §6.1; PB §5; CG Appendix D versus NF §7.
**Verification:** PF-check reproduces the isolated phase coefficient with its proper scope and independently derives the full coefficient transformations.
**Dependencies:** F8,F10; elementary Taylor algebra.
**Numerics:** none needed.
**Interpretation/exclusions:** same harmonic does not mean same observable or coefficient. No new synchronization law is introduced.
**Recommendation:** explain before nonzero-lambda theorem.
**Open:** none.

## F14 — First-order nonzero-lambda theorem

**Statement/hypotheses:** H0,H1,H2,H6. For one step, angle coefficient is
-epsilon^2/(36a)+lambda[epsilon a^2/4+47a^4/32]+O(lambda^2).
At H5 it is -1/5760+(99/2500)lambda+O(lambda^2).
The limiting coefficient at H5 is 13375/1107936648+(34494041501/849664304944)lambda+O(lambda^2).
**Proof:** derive the four-monomial lift z=(A^4,A^2X,X^2,F); T_lambda=(I+lambda P_s)T_0+O(lambda^2), ell_lambda=ell+lambda ell_s T_0+O(lambda^2). Sum with (I-T_0)^-1 and differentiate.
**Provenance:** NF §7 first derived this full-composition result; new universal-component reconstruction verifies it independently.
**Verification:** PF-check F14; both exact fractions and full parameter expressions saved.
**Dependencies/known theorem:** F8,F10–F12; equation (55) is a coefficient-resolvent derivative. Theorem 8 now has explicit hypotheses. The actual nonlinear parameter dependence is proved separately in Appendix D by uniform homological bounds, finite elimination and a convergent geometric iteration. It is not inferred from a truncated matrix's spectral radius.
**Limits:** finite-n coefficient extraction first establishes the formal system. A common local analytic chart and uniform contraction/denominator bounds justify n->infinity and Taylor-coefficient/first-lambda-derivative interchange there. No literal angle at h=0, no arbitrary-amplitude interchange and no unqualified large-lambda extrapolation.
**Interpretation:** NONZERO_LAMBDA=CONTROLLED_TO_FIRST_ORDER; projective neutrality persists only in the stated local seed regime on compact parameter subintervals below the resonance boundary. At epsilon=g=0, the 47/32 comparison is only a one-step identity.
**Recommendation:** separate extension theorem, with parameter-general matrix formula and H5 specialization.
**Open:** higher lambda orders uncomputed; historical parameter rationale OPEN.

## Constants and conventions register

| Quantity | Classification and exact origin | Restriction |
|---|---|---|
| e=(1,1,1), k=(1,1,1) | DEFINED common channel direction; selected equal-unit coefficient case | No claim about unequal k |
| L3 diagonal -2, off-diagonal +1 | DEFINED accepted negative graph Laplacian; equals ee^T-3I | Three channels |
| sqrt(2), sqrt(6), sqrt(3) | DERIVED lengths of (1,-1,0), (1,1,-2), e; orientation fixes signs | Euclidean channel metric |
| phi, h, psi | DEFINED seed angle, perturbation amplitude, oriented readout angle | h>0 and local nonzero branch |
| epsilon=.05, g=.2, exact seed | HISTORICALLY_SELECTED; MOTIVATION_UNKNOWN; three provenance fields OPEN | Never silently generalize |
| h=.001 and eight updates | DEFINED bounds of the recorded two-seed experiment | Numerical example only |
| a,r,m | DERIVED 1-3g, a-2epsilon, 1-2epsilon from Jacobian | Gauge and local chart |
| 9/10,3/10,2/5 | DERIVED at the historically selected point | Parameter-specific spectrum |
| -1/5760 | DERIVED -epsilon^2/(36a) at that point | One-step zero-phase angle |
| 99/2500 | DERIVED epsilon a^2/4+47a^4/32 there | First lambda derivative |
| 13375/1107936648 | DERIVED infinite coefficient sum | F8,F9; observed limit additionally F12 |
| 34494041501/849664304944 | DERIVED differentiated coefficient resolvent | First lambda derivative only |
| a^4,a^2r,r^2,r | DERIVED quadratic monomials in t_n and r-filtering | Collision limits treated separately |
| 243/160 versus 47/32 | DERIVED distinct phase-angle and chirality-coordinate coefficients | Observable/input chart must be named |
| harmonic 3 in synchronization | DEFINED by accepted source; original design motivation not reconstructed | Not a shell-derived necessity |
| theta_lock=.244 | Separate historical observer literal; provenance OPEN | NO Paper F proof dependence |

All derived headline constants have explicit reproducible algebra. This does not close the original rationale for selected inputs. `UNEXPLAINED_HEADLINE_CONSTANTS=0` counts missing **algebraic derivations**, while `HISTORICAL_INPUT_PROVENANCE_OPEN=3` is separately reported.

## Revision-specific proof and evidence register

- **R1 / exact resonance boundary:** all aggregate exponent cases m^i r^j b^k reduce, on m^9<b<r/m^3, to b=m^i or b=r/m^i. Adjacent-power inequalities exclude every interior resonance. Endpoint equations are r=m^3 b (degree four) and b=m^9 (degree nine); their exact lambda values are -7/2187 and 12579511/3600000000. Source: CR proposal; independent Codex proof in v0.2 §12.2 and exact checks.
- **R2 / historical lambda:** lambda=1/1000 gives b=991/2500. The 5-adic proof reduces the only nonlinear target-b possibility to five degree-four monomials, all unequal. This is an all-degree proof; the degree-12 enumeration in the JSON is separately labelled finite corroboration.
- **R3 / joint analyticity:** Appendix D proves uniform denominator bounds. Remove degrees 2 through N, then sum H_n=Lambda^(-n) G^n with geometric bound (q^(N+1)/eta)^n. At H5, eta=1/4, q=19/20 and N=27 suffice. These are proof constants, not model parameter changes.
- **R4 / literature:** Abate, Stanley, Field, Gengel et al. and Skardal–Ott–Restrepo were opened and their relevant statements and version-specific locators checked. `PAPER_F_LITERATURE_REVIEW_v0.1.md` records scope and bibliographic qualifications.
- **Evidence separation:** executable exact identities; finite enumeration; analytic proof; checked external theorem; and Claude-reported high-precision numerical cross-checks remain distinct. The latter were not rerun.
- **Checks:** 131/131 predicates in the successor verifier, including the unchanged 103 predecessor predicates and 28 additions. Predicates are not a count of theorems.

## Ledger disposition

The mathematical chain and bounded literature positioning are complete for the v0.2 candidate. Historical rationale remains OPEN. The four historical motivation questions do not block the conditional mathematics or a later authorized publication build. No formula or parameter is inferred from the lock value, geometry, a handoff claim or a fit. PUBLICATION_BUILD_READY=YES is Codex's revision disposition, not a new Claude review or GitHub publication authorization. No PDF build or publication action has occurred.
