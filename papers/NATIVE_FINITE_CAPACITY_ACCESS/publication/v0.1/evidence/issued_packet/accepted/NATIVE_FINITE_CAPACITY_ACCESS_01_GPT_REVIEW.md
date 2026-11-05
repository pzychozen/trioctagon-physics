# GPT review — Native finite capacity access

**Investigation:** NATIVE_FINITE_CAPACITY_ACCESS_01  
**Review date:** 4 November 2026, Atlantic/Reykjavik  
**Research author and direction:** Hilmir Frímann Halldórsson (pzychozen)  
**Proposal:** GPT  
**Independent investigation:** Codex  
**Current reviewer:** GPT, one project-internal analytical and evidence review

## Disposition

**Accepted — Established unchanged, within the commissioned scope.**

The submitted proof establishes the proposed finite-time quarter-capacity certificate. No correction to the model, hypotheses, rates, constant, time, or phase quantifiers is required. No corrective Codex round is needed.

This accepts the new investigation, not a new manuscript, publication, physical interpretation, kernel implementation, or successor assignment. Existing publications remain unchanged. The pi discussion remains brainstorming material and supplies no premise or change to this assessment.

## 1. Exact accepted result

Retain the published reciprocal chiral exchange equations, admitted finite periodic carrier and finite-width profiles, positive finite coefficients, fixed yaw delta_g = pi/4, and the coherent empty-launch family

\[
\Omega_0=(1,e^{i\phi},1),\qquad 0<\phi<\pi/12,
\qquad p(0)=r_c(0)=z(0)=0.
\]

In the published normalized amplitude convention, R = sqrt(3), k = G sqrt(8/7), m = 2/(3 epsilon_c), d = 2/epsilon_c^3, and

\[
C_{\rm joint}=\alpha_N(1-\cos\phi)>0.
\]

First fix all admitted finite positive coefficients satisfying

\[
\nu^2=\frac{\eta_N^2 m k^2 R^2}{2\alpha_N},\qquad
\sigma_{\rm ext}^2=\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R},
\qquad \sigma_{\rm ext}\le\frac{\nu}{2}.
\]

Then for every admitted phase, its unique unchanged empty-launch solution satisfies, at the same phase-independent time t_* = 1/nu,

\[
\boxed{E_{\rm out}(1/\nu)
=H_C(1/\nu)+H_R(1/\nu)
>\frac{1053}{4096}C_{\rm joint}
>\frac14C_{\rm joint}>0.}
\]

The previously established ceiling also gives E_out(t) <= C_joint. Thus the theorem supplies a strict lower bound greater than 25.708% of the joint ceiling at an explicit finite time, not merely an upper bound or infinitesimal launch statement. The decimal is explanatory; the proof uses exact inequalities.

The parameter set is nonempty without zero propagation or zero receiver coupling. With the other admitted finite positive parameters fixed, choosing one finite eta_N with

\[
\eta_N^2\ge\frac{8\alpha_N}{mk^2R^2}
\left(\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}\right)
\]

is exactly equivalent to the rate condition. It is selected before the phase family and is held constant along every trajectory. Equality in the rate condition is permitted.

**Submitted proof locators:** FA01–FA08 and FA25; supporting sources P1 manuscript/candidate.tex and manuscript/wellposed.tex, P3 manuscript/model.tex and manuscript/projection.tex.

## 2. Mathematical review

### 2.1 The inherited theorem is used at its actual scope

P1 Theorem 3.1 supplies global existence, uniqueness, conservation and H1 carrier regularity for this empty preparation. P2 Theorem 3.1 is the separate earlier native-credit theorem and is not substituted for existence or imported as a new return guarantee. The original carrier speed and both couplings remain positive and constant.

The whole-circle shortest-distance hypothesis is retained, including separation across the coordinate seam. The finite tents are H1 and only their first weak derivative enters. The initial native ball follows from conservation and nonnegative external stores, not from an assumed invariant coherent phase sector.

**Disposition:** FA02–FA05 and FA09 are faithful applications of the supplied sources.

### 2.2 Original weighted energy inequality

The operator in FA10 includes propagation and the full receiver interconnection. Periodic integration removes the derivative of the product of the two carrier coordinates. The receiver inner-product weight beta_R cancels its inverse in the state equation, so the two loading terms have exactly opposite signs and equal factors of kappa.

The inequality in FA11 is valid for the already known strong curve. Differentiating sqrt(||V||^2 + epsilon^2) first, integrating, and then taking epsilon down to zero avoids division by a zero norm. The proof does not infer existence or regularity merely from energy cancellation.

**Disposition:** correct signs, weights and zero-norm treatment.

### 2.3 Drive-dependent Volterra bound

The actual finite-dimensional chain rule gives

\[
\dot f=-\frac{\eta_N}{2\alpha_N}JJ^Ty.
\]

The bound ||J|| <= kR is valid on the native ball. Combining the integral estimate for the external norm with the drive derivative yields the coefficient nu^2, including both factors of eta_N. The continuous nonnegative functions g,h satisfy the two stated integral inequalities, and their double integral gives the positive Volterra kernel nu^2(t-s).

For each finite interval the iteration remainder is bounded by M_T (nu T)^(2n)/(2n)!, and tends uniformly to zero. This justifies the sinh majorant without assuming differentiability of g at zero. Substitution into the h inequality gives the cosh drive bound. Applying the argument separately at each positive phase does not require a phase-uniform preliminary M_T; the resulting explicit formula is phase-uniform after normalization.

**Disposition:** FA12–FA15 are sound, including the convergence argument carried in prose rather than by the symbolic suite.

### 2.4 Reference residual and regularity

U_ref = (eta_N t B f_0, 0, 0) is a comparison curve, not a solution obtained by changing the actual coefficients. Since B f_0 is H1, the reference is strong. The actual-minus-reference difference is therefore strong before any residual estimate is invoked.

The residual contains both required terms:

\[
\left(0,-c\eta_Nt\mathcal B'f_0,
\frac{\kappa\eta_Nmt}{\beta_R}f_0\right).
\]

The second carrier component has a minus sign; the receiver component has a plus sign and is nonzero despite the reference receiver being zero. Their orthogonality in the weighted space gives the sum of squares defining sigma_ext, not an omitted receiver contribution or an arbitrary separate approximation. Only B' f_0 in L2 is used; the residual is not differentiated again to claim H1 regularity.

**Disposition:** FA16–FA19 retain all relevant errors and the original stock normalization.

### 2.5 Positive lower bound and strict rational margin

The reverse-triangle bracket is

\[
B(u,\rho)=2u-\sinh u-\frac{\rho u^2}{2},
\qquad u=\nu t,\quad \rho=\sigma_{\rm ext}/\nu.
\]

The proof explicitly requires B > 0 before squaring. At u = 1, rho <= 1/2 gives B >= 7/4 - sinh(1). The series-tail comparison proves strictly sinh(1) < 67/57 < 19/16, hence B > 9/16. The strictness of the tail is justified by the later factorial ratios being smaller than 1/20.

The independent capacity factor is exactly

\[
\frac{\alpha_N|f_0|^2}{k^2R^2C_{\rm joint}}
=\frac5{12}(1+\cos\phi)>\frac{13}{16}.
\]

The positive phase makes cancellation of 1 - cos(phi) legitimate. The exact square comparison for cos(pi/12) > 19/20 is valid. Multiplication produces 1053/4096 = 1/4 + 29/4096, with strictness preserved even when sigma_ext = nu/2.

**Disposition:** FA20–FA24 prove the stated strict constant. No floating-point test, unproved remainder, or squaring of a negative lower bound is hidden in this step.

### 2.6 Dimensions and quantifiers

Retaining the native amplitude dimension of R makes both squared rates have units T^-2; A_0 has units U L^(1/2)/T. The eta_N threshold is dimensionless. The fixed geometry, coefficients, and t_* are phase-independent in the declared normalized family.

No rate has been promoted to a native oscillation frequency, physical clock or F-step cadence. Finite positive nonemptiness is proved by an allowed coefficient selection, not by a zero-coupling or infinite-coupling limit.

**Disposition:** FA25 and the units table are consistent. No added hypothesis is needed.

## 3. Meaning and limits retained

The numerator is combined carrier-plus-receiver trial storage, and the denominator is the joint structural ceiling. This is not a quarter of all initial native storage. In this family,

\[
\frac{C_{\rm joint}}{H_N(0)}=\frac23(1-\cos\phi).
\]

The absolute stock can tend to zero as phi tends to the excluded zero-drive endpoint, even though the capacity-normalized guarantee is uniform. It is also not a saturation result, an identified maximizing time, monotone extraction, a receiver-only stock bound or a physical energy calibration.

The earlier 80/81 receiver-share and net-recovery guarantees retain their own hypotheses. This proof does not establish their overlap with the current finite-capacity-access regime and does not attach those fractions to this new amount. A later same-trajectory recovery result for this capacity-sized transfer would need its own argument.

The central meeting region, opposed cones, outward spreading, curved around-and-inward return, stationary supports and possible transfer elsewhere remain the geometric motivation. Carrier circle/tight toroid, close/extended-line spheres and host-notch N/central G boundaries remain distinct. No new route or six-opening registration is inferred from this norm estimate.

The continuing agenda remains useful accessible amount and attainability, followed by native F/exchange cadence, intended-route correspondence and six-opening transport, with linked gravity–magnetism and later outer geometry and justified SRG integration. Three-Way remains parked. No successor investigation is commissioned by this review.

**Submitted proof locators:** FA26 and Section 8.

## 4. Independent evidence checks

The accompanying REVIEW_VERIFICATION.json and review_verify.py record the checks performed in this review.

| Check | Observed result |
| --- | --- |
| Submitted ZIP | 639,560 bytes; supplied SHA-256 matches; 91 safe unique members; CRC verification passes |
| Top-level manifest | All 90 payloads match their recorded sizes and SHA-256; exact exhaustive membership and self-exclusion |
| Carried input manifest | 74 members, with all 73 non-self payloads matching their manifest |
| Standalone proof and completion report | Byte-identical to their archived copies |
| Issued work order | Independently retrieved Library version 1 matches the returned copy exactly |
| Selected-source registry | All 62 entries match actual supplied bytes |
| Independent prior-byte comparison | 59 entries byte-identical to the previously uploaded publication closeout payload |
| Historical remote record and publication manifest | 59 and 58 corresponding source entries reconcile, respectively; the manifest self-exclusion explains the difference |
| Separate publication records | Supplied receipt and remote-comparison record match their separate earlier uploads |
| Focused preservation | All 77 before/after records agree with the baseline; 74 delivered input members match actual bytes; the separate issued order also matches |
| Claim crosswalk | All 15 inherited groups, 7 new steps and 26 displayed groups accounted for; proof/ledger bindings correct |
| Printed source locators | All 15 recorded P3 label/page pairs match the supplied label record |
| Algebra replay | All eight check groups pass; each result payload matches Codex's original result |
| Post-review preservation | Extracted submission still byte-identical to the received archive |

The fresh algebra execution used an isolated exact copy of the inspected exact_checks.py, Python 3.13.5 and SymPy 1.14.0. Codex's run used Python 3.11.15 and SymPy 1.14.0. Scientific check payloads match; timestamps, interpreter paths and other execution metadata appropriately differ. This is a replay of the same eight groups, not eight additional independent scientific results.

The symbolic script checks finite algebra and rational inequalities. The written review separately assessed regularity, the positive-kernel comparison, the vanishing remainder, quantifiers and interpretation. Hash matching is preservation evidence, not a proof of mathematics.

### Verification limits

This review did not inspect the live Windows filesystem. Its 77 preservation checks reconcile recorded before/after identities. Of those, 74 refer to actual input members present here and one to the separately retrieved original work order. The original issued ZIP and its checksum were not separately available; their two preservation records are internally consistent but were not compared to independent original archive bytes. The complete carried input manifest and all delivered member bytes were checked.

Of the 62 registry records, 59 compare to independently retained prior publication payloads and two more to separate earlier uploads. The carried subsequent GPT closeout-review file is hash-verified inside the packet, but no independent copy was fetched in this review. No source claim relies on treating that file as new mathematical evidence.

No fresh remote retrieval, Git operation, PDF render/build, numerical trajectory, parameter scan, package installation, historical AT/PC suite, or successor investigation was performed. Source review used the supplied editable mathematical text. No external peer review or machine-formal proof is claimed.

## 5. Accepted identities and closure

**Submitted proof:** NATIVE_FINITE_CAPACITY_ACCESS_01_PROOF.md  
Bytes: 22,634  
SHA-256: `05d962af8be00377212c96c63a2ae498e57b4912192dfad87e705b4aadd56cb7`

**Submitted review ZIP:** NATIVE_FINITE_CAPACITY_ACCESS_01_REVIEW_PACKAGE.zip  
Bytes: 639,560  
SHA-256: `e554415e2dd874d956924737fdcb95422583bf281a18554d94e3f72873abe905`

**Exact-algebra script SHA-256:** `b0d32159028013a99cc9a152f4bc56be7c5041225dad2ac51c2898fe679dcfe1`

**Issued work-order SHA-256:** `cff35558c510a368c41258d77d1b451539730636aed8cae8598be4bc44798b36`

**Final verdict: accepted unchanged.** This completes project-internal GPT review of the commissioned finite-capacity-access theorem. There is no blocking mathematical, source or package discrepancy and no required corrective round. The established advance is explicit finite-time access to more than one quarter of the joint ceiling on actual fixed-parameter empty-launch solutions.
