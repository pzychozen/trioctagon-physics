# CA04 — GPT scientific review

**Date:** 21 October 2026  
**Disposition:** **ACCEPTED_WITHIN_EXACT_REAL_FINITE_COUPLING_AND_FIVE_DYADIC_ENTRY_SCOPE**  
**Primary result:** `CERTIFIED_LOCAL_ATTRACTION_AT_1_OVER_32`  
**Required scientific corrections:** None identified.  
**Publication:** This review authorizes no staging, commit, push, release, external upload or changes to accepted research.

## 1. Scientific decision

CA04 closes the specific gap left by CA03. At exactly alpha = 1/32, the complete, exact-real, 800-update RETURN map has a unique fixed point in each of two specified nested intrinsic-coordinate rectangles. Both rectangles are strictly invariant and contracting in their respective weighted maximum norms. Consequently their common fixed point is locally attracting for the full two-coordinate block map, not merely for a leading-order scalar phase approximation.

All five specified saved Cartesian checkpoints, interpreted as exact dyadic new initial conditions at the same next forcing phase, have validated full-block images inside the larger rectangle. Under indefinite repetition of the declared RETURN schedule, these five new initial-value problems therefore converge to the same periodically driven response. Their angular distinctions tend to zero. This is asymptotic coalescence, not a proof of exact finite-time equality.

The result does not certify unknown exact versions of the earlier binary64 histories. It concerns the future from the specified stored numbers. It is not a global basin classification, an exact historical Figure 4 replay, a claim of a static state during a pulse, a minimal-period theorem, or a physical interpretation of the author's reference geometry.

## 2. Submission identity and review activity

Input: `CA04_GPT_REVIEW.zip`  
Bytes: **12,471,489**  
SHA-256: **`d641900612c131ade7f803010c44f58097cd7dbea25459c3c23b5a4f42424897`**

The archive contains **78 members: 77 manifested payloads and MANIFEST.json**. Member-name/path safety, uniqueness, non-symlink status, CRC, exact manifest coverage, sizes, hashes and extracted-byte equality passed. All 16 consumed-original identity records match accessible prior archives or the supplied start packet. The separately supplied summary and work order match their corresponding bundle members.

I read the work order, sealed plan, initial and final mathematical analysis, interval core, equivalent intrinsic map, automatic-differentiation implementation, separate hand differential, certificate construction and verification code, scalar-consequence calculation, execution ledger, preservation records and figure. I did not launch candidate search, construction, packaging or any historical runner.

### Fresh fixed-certificate replay

After inspecting the code, I ran the submitted standalone verifier once in a **separate copy**, preserving the submitted input directory. It completed successfully and reproduced the exact saved certificate quantities. This was real enclosure computation, not merely reading a PASS field:

| Fixed verification activity | Validated set steps |
|---|---:|
| Center residual, all 800 updates | 800 |
| Full X and B derivative/inclusion enclosures, automatic differentiation | 1,600 |
| Same two rectangles, separately hand-derived local Jacobian | 1,600 |
| Five specified Cartesian-entry problems, one complete block each | 4,000 |
| **Total newly performed certificate replay** | **8,000** |

The 3,200 derivative steps are included in, not additional to, those 8,000 state-set steps. The verifier also regenerated 800 forcing intervals. No candidate search, new parameter choice, prefix replay, exploratory point trajectory or native-kernel update was performed.

### Additional reviewer checks

A separately written reviewer checker independently verified the rational contraction inequalities, input identities, archive/source seals, root-localization inequalities, twelve saved transition relations and algebraic chart identities. It also constructed a **second rigorous enclosure of every forcing value** using independent 224-bit rational-endpoint arithmetic, degree-96 Taylor polynomials, reduction by 256 and eight doubling identities. Every one of those 800 enclosures lies inside the corresponding submitted 160-bit forcing enclosure. This is rigorous interval containment, not ordinary agreement between two floating precisions.

Independent scalar calculations also enclose the reported fixed-point phase and Cartesian coordinates within the supplied scalar-consequence intervals. The twelve independently grouped saved-successor calculations differ by at most **4.44e-16**, below the inherited consistency criterion. Those binary64 checks are consistency evidence only, not proof bounds.

The reviewer checker records 9,854 Boolean checks, including identity, interval, domain and table tests; this is **not a count of mathematical theorems**. One earlier integrity-only attempt stopped because its text-inclusion assertion expected the initial report's original title. Direct comparison showed an unchanged mathematical body, one renamed heading and a blank line. The reviewer corrected that assertion; no scalar forcing construction or state propagation had started in that failed attempt. No submission change was required.

Reviewer environment: Python 3.13.5, NumPy 2.3.5 and SymPy 1.14.0 on Linux. No dependency was installed. The author's Windows environment was not accessed.

## 3. Exact target and the mathematical role of the chart

The certified object retains the complete accepted recurrence:

- alpha = 1/32, dt = 1/10 and forcing times f/10 for f = 0,...,799;
- the prescribed four-term decaying H within every block;
- the coordinate roll C(x,y,z) = (z,x,y);
- the cross-product increment, scalar clipping with epsilon = 1/100000, Euler step and active remap;
- continued state across blocks, with only the forcing index restarting.

The proof is about the exact-real recurrence. It is not a claim of bit-for-bit eventual periodicity of the primary floating evaluator. That evaluator remains byte-identical to the accepted CA03 source.

For the upper-torus chart,

\[
\chi(c,v)=\left((1+c/2)\frac{1-v^2}{1+v^2},
(1+c/2)\frac{2v}{1+v^2},\frac12\sqrt{1-c^2}\right),
\]

both c and v evolve. The radial/tangential decomposition in the submission is algebraically consistent with the Cartesian cross product. With the paper's intermediate a,b,d,h,L,w, the update

\[
c^+=d/L,\qquad v^+=(v+w)/(1-vw)
\]

is the same exact map on the verified chart. The positive-root and denominator hypotheses are checked throughout every interval tube. This is not a scalar replacement model or a reset to the old fixed circle.

The clipping simplification in the validated evaluator is legitimate because on K,

\[
\|q\|\le81/256<4/5-1/100000,
\qquad \rho-\|u-s\|\ge1199/2560>0.
\]

The supplied argument for |H| <= 9/2 is valid; it does not incorrectly sum the four separate amplitude maxima. The off-K input problems have their own first-step interval checks.

## 4. Arithmetic and derivative audit

The task-specific interval core represents endpoints as exact integers divided by 2^160. Inspection verifies outward rational conversion, signed arithmetic, zero-excluding reciprocal, squaring and integer-square-root bounds. The reviewer supplemented this written audit with 1,242 exact endpoint/extremum checks, including negative intervals and sub-grid inputs. Finite tests supplement rather than replace the general arithmetic argument.

The submitted degree-64 exp/sin/cos Taylor expansions operate on arguments reduced by 128. The exponential remainder bound 3/65! and sine/cosine bounds 1/65! are sufficient on the stated reduced domain. Seven doubling/squaring identities restore the original arguments with outward bounds. All 800 forcing values, including the late small values, remain present. The independent 224-bit forcing construction provides a separate check of those constants.

The automatic-differentiation rules implement the ordinary chain/product/quotient/square-root derivatives with intervals. Each step bounds the local Jacobian on the whole current state enclosure, and the signed matrix products enclose the composed derivative on the whole original rectangle. Absolute values are taken only after the full composition. This is not a sampled-center derivative.

The separate hand differential was also reviewed and replayed. It uses different algebraic groupings and produces slightly wider but still valid contraction bounds:

| Region | Main automatic-differentiation bound | Separate hand-differential bound |
|---|---:|---:|
| X | 0.850606416789... | 0.850607383690... |
| B | 0.924578804694... | 0.943681887849... |

Both routes prove strict contraction and inward inclusion. The advertised q_B < 0.925 comes from the exactly reproduced main certificate; it is not the wider hand-differential bound.

**Trust boundary:** the submitted verifier and both derivative routes share the reviewed integer interval core. The reviewer's forcing engine and rational inequality checks are separately implemented, but this remains a transparent computer-assisted proof relying on the reviewed code and Python integer semantics—not a proof-assistant formalization or wholly independent second end-to-end implementation.

## 5. Existence, uniqueness and attraction

The exact center is

\[
\widehat c=\frac{3296863744182679}{9007199254740992},\qquad
\widehat v=\frac{4382175857337591}{36028797018963968}.
\]

The primary radii are (10^-6, 10^-5); the larger radii are (10^-3, 10^-1). Both use the same center. Each full rectangle is covered in one interval traversal; no subdivision or unsampled gap is involved.

The verified quantities satisfy

\[
|T(\widehat x)-\widehat x|\le e,\qquad
|DT(x)|\le M\quad\text{for every }x\text{ in the rectangle},
\]
\[
e+Mr<r,\qquad q=\max_i (Mr)_i/r_i<1.
\]

Integrating DT along straight segments in the convex rectangle proves both inward inclusion and contraction in the corresponding weighted maximum norm. The closed rectangle is complete. The contraction argument therefore supplies a unique fixed point in that rectangle, invariance and convergence from every point in it. This concerns the actual RETURN map, not a preconditioned Newton iteration.

The margins remain strictly positive when recomputed as exact fractions. Their ordinary displays are approximately:

| Region | c inward margin | v inward margin |
|---|---:|---:|
| X | 9.99999999995635e-7 | 1.49393583195194e-6 |
| B | 9.99999999957557e-4 | 7.54211953063461e-3 |

X is contained in B, so their unique fixed points are the same. No global uniqueness follows.

Using the saved nonnegative M_X and residual e, the bound (I-M_X)^-1 e further encloses the root. The reviewer independently reproduced this exact rational implication and enclosed its phase within

\[
0.2420705842886754<\phi_*<0.2420705842886798.
\]

The corresponding Cartesian location is approximately (1.148520440083195, 0.283583940922842, 0.465302429551067), with rigorous component enclosures supplied in the certificate. The earlier leading phase near 0.245117619178 was only a solver seed. No parameter-continuation connection to that branch is certified here.

The q values are conservative distance-contraction bounds in two different weighted norms. They are not eigenvalues, observed angular-retention percentages or fractions of stored information. A tiny derivative component does not establish an exact zero or finite-time loss of invertibility.

## 6. Entry of the five stored initial conditions

I independently verified all five NPZ member identities, row-byte hashes, float-hex values, exact dyadic component fractions and inherited phase-lift records. The certificate uses the actual three Cartesian components as new exact initial values. It does not fit them to the torus or old circle.

For each input the first f=0 step is validated in Cartesian coordinates, including clipping and nonsingularity; the actual remap produces the intrinsic state. The remaining updates run at f=1,...,799. Thus the result is at a common next block boundary, not an incorrectly reset phase after the first step.

All five complete-block interval images lie inside B:

| Saved start | Validated entry blocks | Display of final v |
|---|---:|---:|
| A0p_RETURN | 1 | 0.065973712572206 |
| Bhalf_RETURN | 1 | 0.065671414263580 |
| Bthreehalf_RETURN | 1 | 0.066277935162302 |
| Czero_RETURN | 1 | 0.065535723538212 |
| Cquarter_RETURN | 1 | 0.068144045826960 |

These are displays of certified intervals, not exact scalar endpoints. Each v interval is narrower than 2e-45. Every interval's inclusion was reproduced in the fresh verifier and independently checked against B's exact rational boundaries.

Invariance and contraction now apply indefinitely. At block boundaries all five states converge to the same fixed point. At each corresponding within-block phase, finite-prefix continuity transfers that convergence to the same periodically driven history. No continuous-time interpolation or minimal-period statement is needed.

The proof treats the saved values as exact new initial data. It does not enclose accumulated error of the preceding 3,200 binary64 updates, reconstruct historical producer inputs, or prove entry for the other cardinal controls. Those limitations do not undermine the five explicitly stated new initial-value problems.

## 7. Preservation and presentation

The 16 consumed-original records agree with before/after hashes and accessible prior archives. HEAD, staged diff and tracked diff snapshots agree. All 21,134 reported status lines outside CA04 match after exclusion of this new workspace. Existing Git warnings about overlong untracked paths are explicitly preserved; these status records do not establish a complete inventory of those trees.

I did not inspect the author's Windows filesystem or the Git remote. Preservation and no-publication claims are supported by the supplied evidence, not independently witnessed Git operations. All submitted payload bytes remained unchanged during this review; verifier outputs were written only into a separate extracted copy.

The figure is legible and correctly distinguishes the large certified region, small primary rectangle, five entry enclosures and illustrative markers. Its vertical axis is a scaled c-coordinate difference; the rectangle is a coordinate domain, not a material enclosure. The standalone uploaded PNG is a different-resolution rendering from the ZIP's PNG, not a byte-identical attachment; both present the same scientific layout.

## 8. Closeout and scope

**CA04 is accepted. The finite-coupling local-attraction gap is closed, and all five specified exact stored starts have certified entry. No scientific repair or additional exploratory run is required for this acceptance.**

The coherent result across this research sequence is protocol-dependent retention. A fading drive can leave distinct angular endpoints. Returning drive can progressively reduce those distinctions; at the tested setting, CA04 now establishes asymptotic convergence for the five declared futures rather than extrapolating a finite trend.

Still unclassified: global attraction, other finite-coupling roots and basins, connection to the small-coupling branch, minimal period, ambient-neighborhood certification, finite-time injectivity and recovered historical producer inputs. No heat, magnetism, light, physical storage or predictive SRG-to-Z identification follows. The reference geometry remains passive.

Acceptance is not publication authorization and does not certify every question in the SRG-centre program.

## 9. Review artifacts

The accompanying review package contains:

- this scientific review;
- `review_ca04.py` and `CA04_INDEPENDENT_RESULTS.json`;
- independent 224-bit forcing enclosures;
- fresh fixed-replay verification, ledger and launch/stdout records;
- activity and supplementary scalar-bound records;
- reproduction instructions and a review-package manifest.

The checker imports only the inspected interval primitive module from the submission, not its state runner. It performs scalar, symbolic, identity and saved-input checks. The separately replayed submitted verifier performs the declared 8,000 validated set steps. Do not confuse those activities or relaunch the candidate solver to review this result.

**Principal submission sources:** `CA04_FINITE_COUPLING_ANALYSIS.md`; sealed plan/initial analysis; `CERTIFICATE.json`; `CERTIFICATE_SCALAR_CONSEQUENCES.json`; interval/map/derivative/verifier modules; forcing and center-residual records; exact input index; execution and preservation records; supplied explanatory figure. Proof assessments above are the reviewer's reasoning and explicit checks of those definitions, not substitution of external sources.
