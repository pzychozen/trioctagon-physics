# CA02 — GPT scientific review

**Date:** 21 October 2026  
**Disposition:** **ACCEPTED_WITHIN_PRINTED_MAP_ENDPOINT_RETENTION_SCOPE**  
**Required scientific revisions:** None identified.  
**Historical reproduction:** Not established; the diagnostic inputs remain declared choices.  
**Publication:** This review authorizes no staging, commit, push, release or external publication.

## 1. Scientific decision

CA02 establishes the proposed endpoint-retention mechanism for CA01's accepted completion of Figure 4's printed recurrence. The drive can transfer differences in initial size or initial tilt into a difference in the final angular position, even though the remap alone erases those differences. The proof concerns the specified comparisons at sufficiently small nonzero coupling. The observations at coupling 1/32 are supporting finite numerical evidence, not interval-certified endpoint separations.

The strongest contribution is not just a changed first step. The analysis justifies the derivative of the limiting phase, computes distinct response coefficients, and thereby proves different limiting phases for the specified starts at sufficiently small nonzero coupling. The exact diagonal-ray erasure example and the rank-one endpoint map correctly limit the interpretation: retained dependence is not independent reconstruction of the full initial state.

No repair or additional simulation is required for acceptance within this scope.

## 2. Submission identity and independent review activity

Submitted archive: `CA02_GPT_REVIEW.zip`  
Bytes: **2,165,140**  
SHA-256: `b63d01492b96d7e125509f1d3fec7ca2eecdb43f5353fab3b3e18236aa7b34bc`

The archive contains **68 files: 67 manifested payloads and MANIFEST.json**. Archive-member safety, uniqueness, CRC, manifest completeness, sizes and SHA-256 identities passed. Both separately uploaded CA02 texts match the archive. The work order and the inherited CA01 scientific review match their separate attachments.

Nine included CA01 files are byte-identical to their members of the earlier accepted CA01 archive. That archive itself matches the accepted SHA-256. These nine files plus the accepted archive account for the ten consumed-original records. Supplied before/after preservation records, unchanged HEAD, identical status records and empty index records are consistent.

I read the mathematical analysis, plan, source/claim map, verification, execution records and relevant scripts. The submission's source scripts were inspected, not launched. Four function abstract syntax trees—H, P, step and the finiteness check—match their accepted CA01 definitions. Both explanatory figures were visually inspected, including their numerical qualifications and distinction between samples and motion.

Independent numerical verification used saved inputs only:

| Item | Unique coverage |
|---|---:|
| Manifested payloads | 67 |
| Consumed-original identity records | 10 |
| Preserved CA01 member files | 9 |
| Unchanged evaluator function ASTs | 4 |
| Inherited isolated fixtures | 12 |
| Inherited saved transitions | 200 |
| Saved CA02 transitions | 12,800 |
| Saved CA02 states, including initial states | 12,816 |
| New trajectories / new rollout updates | **0 / 0** |
| Native-kernel updates | **0** |

The reviewer checks evaluated each saved predecessor independently. No computed successor became another input. Bounded scalar calculations independently evaluated the response coefficients, their 39-term meridional corrections, the forcing sum and the tail formulas at 80-digit working precision. They were not additional three-component trajectories. Symbolic identities supplement the written proof review; they are not proof-assistant certification.

The review script completed once successfully. Its 1,227 Boolean checks include archive, identity, shape and record-consistency checks; this is **not a count of mathematical theorems**. Reviewer environment: Python 3.13.5, NumPy 2.3.5, SymPy 1.14.0 and mpmath 1.3.0, on Linux—not the author's Windows `torment` environment. No dependency was installed.

## 3. Endpoint definitions and zero-drive erasure

The endpoint is correctly indexed by the initial absolute clock. Inherited convergence gives a limiting point on the circle, while the new endpoint identity is

\[
E_{\alpha,k}(s)=E_{\alpha,k+1}(F_{\alpha,k}(s)).
\]

Restarting the endpoint calculation at clock zero after a step would generally describe a different forcing history. The report preserves this distinction and continues the angular lift consistently across the successor.

At zero drive, the remap preserves azimuth exactly and removes positive scale immediately. Its contracting meridional iteration then removes the initial inclination. Consequently

\[
E_0(x,y,z)=\left(\rho_*x/\rho,\rho_*y/\rho,z_*\right),
\qquad \rho=\sqrt{x^2+y^2}>0.
\]

The constant-endpoint sets are the stated azimuth half-planes. The phase gradient is nonzero and has the stated formula. The axis and origin are correctly excluded from these smooth angular charts. The fixed circle is a collection of possible endpoints, not a circulating orbit.

## 4. Why the drive can retain a difference that P alone erases

The component torque

\[
A(s)=s\times Cs=(y^2-xz,\ z^2-xy,\ x^2-yz)
\]

and the short-segment phase increment are correct. For displacement e, the real and imaginary parts of the horizontal complex product are

\[
\rho^2+xe_x+ye_y,\qquad xe_y-ye_x.
\]

The specified lower bound on horizontal distance makes the real part positive and keeps the increment on the intended local branch. Since P preserves the pre-remap azimuth, these increments account for the whole update's angular change.

The positive-scale identity correctly keeps the clipping factor's dependence on the squared initial scale. Scale independence of P alone therefore does not imply scale independence of P after the torque. This is a change of evolving state before remapping, not a passive observation effect.

For any fixed nonzero s=c(1,1,1), the first torque vanishes. Every positive rescaling has the same first remapped state at the same clock, and hence exactly the same subsequent future. This example proves exact erasure for a class of comparisons. It does not imply that subsequent torque vanishes. Conversely, a zero first *angular* increment is not a zero-torque or endpoint-erasure theorem; the zero-tilt diagnostic illustrates this distinction.

## 5. Limiting response: proof review

The response factor is

\[
W(s)=\frac{xA_y-yA_x}{\rho^2}
=\frac{xz(z+y)}{\rho^2}-y,
\]

and the derivative at zero coupling is

\[
D(s_0)=\left.\partial_\alpha\Phi_{\alpha,0}(s_0)\right|_0
=0.1\sum_{n=0}^{\infty}H(0.1n)W(P^n s_0).
\]

The absence of a separate first-order state-sensitivity contribution is justified: the angular increment is identically zero as a function of state at alpha=0, so its state derivative there is also zero. State sensitivity enters at higher order.

### Differentiating the limiting sum

The derivative/sum interchange is supported, not merely formal. On a compact admissible start neighborhood, sufficiently small coupling keeps the clip on its constant branch. After a finite entrance interval the torus dynamics has a uniformly contracting meridional coordinate, while azimuth is neutral up to summable drive-dependent terms. The phase-coupling derivatives carry a factor of H, and its exponential envelopes are summable.

The first-sensitivity recurrence therefore has bounded angular sensitivities and summably decaying meridional sensitivities. At the next derivative orders, nonlinear unforced terms involve products of the stable sensitivities; angular terms still carry the forcing factor. Induction through third order gives uniform convergence of the required derivative series. Finite entrance steps are smooth. This supports the local C3 claim and central-difference truncation order.

The supplementary argument for the selected coupling interval is also sound: uniform inactive clipping and off-axis bounds handle the finite initial steps, and uniformly small late forcing produces a common eventual contraction neighborhood. A finite third-derivative supremum exists there; the submission does not assign an unproved numerical value to it.

### Fixed-circle and size comparisons

On the fixed circle the response factor reduces to the stated nonconstant G(phi). The exact geometric-series expression for the forcing sum S is correct. The cardinal response values show that the drive is not merely a uniform angular rotation. A passive frame change must transform the coordinate operator as well as the vectors; rotating only an initial state is a different experiment.

For a positive ray through a fixed-circle point,

\[
D_{\rm ray}(\lambda,\phi)=D_{\mathcal C}(\phi)
+0.45(\lambda-1)G(\phi).
\]

The distinct coefficients at phi=0 prove distinct limiting phases for lambda=1/2, 1 and 3/2 at sufficiently small nonzero coupling. This conclusion concerns the infinite-time endpoint, not merely the initial displacement. It does not supply an explicit sufficient coupling threshold or certify the selected finite coupling by itself.

### Tilt comparisons

The two tilt starts keep norm and azimuth fixed, so the comparison does not confound tilt with initial size. The transient correction formula and its geometric remainder are correct. The strict bounds supplied for the two derivative differences are adequate:

- The zero-tilt difference has an upper bound below approximately -0.00664893 after its remaining correction is bounded.
- The pi/4-tilt difference has a lower bound above approximately +0.09680677.

These are bounds on response-coefficient differences, not on the finite-coupling endpoint differences. Their strict signs establish that the derivatives differ from the reference. Together with smoothness, they prove endpoint separation for sufficiently small nonzero coupling.

Independent scalar evaluation gives S approximately 65.8649686914812827 and the response coefficients:

| Start at azimuth zero | Derivative at zero coupling |
|---|---:|
| Half initial size | 1.164234730101693 |
| Reference | 1.205412588027442 |
| 1.5 times initial size | 1.246590445953192 |
| Zero tilt, reference norm | 1.145667134685628 |
| Pi/4 tilt, reference norm | 1.496345658915117 |

The analytic correction tail starting at index 40 is below approximately 1.63522e-19 in derivative units. This is distinct from rounding in either the submitted binary64 coefficient evaluation or the reviewer's higher-precision scalar evaluation.

## 6. What can and cannot be recovered

The endpoint depends on several initial coordinates, but it has only one angular coordinate. Near zero drive its nonzero gradient makes the endpoint map rank one, with two-dimensional local sets sharing an endpoint. This supports the report's limited use of retention: differences can affect an outcome without all initial coordinates becoming independently recoverable.

Restricted to initial states already on the fixed circle, sufficiently small drive yields a strictly increasing lifted circle map. That is a separate, one-dimensional invertibility statement. Neither the degree-one result inherited from CA01 nor the finite diagnostic table establishes monotonicity at every coupling, global injectivity on the three-dimensional start domain, a storage capacity, or a physical memory device.

## 7. Numerical evidence and error accounting

All 16 cases match the authorized matrix, with 800 saved updates each and no additional fresh probes recorded. All saved clocks are t_n=0.1n. The original clipping formula remains present and every saved clipping factor is one, as predicted by the predeclared bounds. The evaluator source retains the accepted function bodies.

Independently calculated successor values, using explicit torque components and the closed-form remap, agree with the saved successors to at most **4.44e-16**. The largest independently calculated scaled Euler residual is **4.50e-16**; the largest scaled perpendicularity residual is **2.19e-17**. The torus residual is at most **1.67e-16**. The lifted phase agrees with the saved state's azimuth modulo 2pi to **1.14e-14**. All are below the stated 1e-12 consistency criteria.

The minimum saved horizontal-segment lower bound is approximately **0.58942684**, and the maximum raw torque is approximately **0.48074318**. Both support the intended off-axis, unclipped regime. The saved endpoint and comparison tables match independently recomputed arithmetic.

At alpha=1/32, the phase estimates at update 800 are:

| Start | Phase estimate, radians |
|---|---:|
| Reference | 0.034913238851 |
| Half initial size | 0.033801059304 |
| 1.5 times initial size | 0.036032627511 |
| Zero tilt, same norm | 0.033301883984 |
| Pi/4 tilt, same norm | 0.042901847724 |

The remaining exact-trajectory angular tail expression evaluates to approximately **2.13895878976e-11 radians** per trajectory. This is not an accumulated floating-point-error enclosure. Small one-step residuals and high-precision scalar calculations do not supply the missing global enclosure. The submission explicitly makes this distinction, and no interval-certified separation at alpha=1/32 is claimed.

The two central-difference comparisons agree with the derived coefficients and the expected second-order truncation behavior. Their observed error-reduction ratios are approximately **3.99891** and **4.05929**. These are consistency observations, not proofs of smoothness or required success criteria. The Richardson estimate remains an estimate.

## 8. Geometry, preservation and limits

The optional geometric overlay was omitted because the native-coordinate comparisons already answer the question. No circle or crystal was fitted to the data, and no force or boundary was added from the analytical reference framework. The endpoint circle and transfer mechanism arise from the accepted recurrence, not from a new physical geometry.

The two supplied figures are legible and properly label the finite endpoint estimates, first-order predictions, connecting sample segments and exact-tail-versus-floating-error distinction. Neither figure presents the endpoint family as an orbit.

The consumed-source snapshots match the earlier upload and the before/after records. All extracted submission payloads remained unchanged during this review. I did **not** inspect the author's Windows filesystem or Git remote directly. Therefore preservation and no-publication statements are supported by the supplied records, not independently witnessed remote or local Git actions. Historical producer gaps remain unchanged; this result applies to the accepted printed-map completion, not every historical SRG program.

## 9. Closeout

**CA02 is scientifically accepted within printed-map endpoint-retention scope. No required revision or additional numerical run is identified.**

The plain-language conclusion is:

> Remapping can erase a starting difference in size or tilt while leaving its earlier effect on the final angle. The system retains an outcome-dependent trace, not an independently readable copy of the entire initial state.

CA01 established what the recurrence approaches. CA02 establishes a mechanism by which the initial state influences the selected endpoint. Neither result establishes a physical substance, calibrated memory capacity, ongoing circular motion, or a completed SRG-to-Z correspondence.

This acceptance is not publication authorization.

## Review files and reproducibility

`CA02_INDEPENDENT_RESULTS.json` records the checks and scalar evaluations. `review_ca02.py` performs only saved-record, identity, symbolic and scalar-formula checks. It does not import the submitted evaluator or launch any submitted script.

Example Windows CMD invocation, with paths replaced by actual extracted locations:

```bat
call conda activate torment
python -B review_ca02.py --input-dir "C:\path\to\extracted_CA02" --archive "C:\path\to\CA02_GPT_REVIEW.zip" --ca01-archive "C:\path\to\CA01_GPT_REVIEW.zip" --output-dir "C:\path\to\new_reviewer_output"
```

`--attachments-dir` is optional and compares separately supplied text attachments when present. Do not run `supervise.py`, `run_diagnostics.py` or CA01's original runner as part of reviewing this submission.

**Principal sources:** `CA02_ENDPOINT_RETENTION_ANALYSIS.md` §§1–7; `CA02_PLAN.md`; `READ_ME_FIRST.md`; `RUN_RESULTS.json`; `ENDPOINT_RESULTS.json`; `VERIFICATION.md/json`; CSV tables; `raw/*.npz`; `evidence/PRESERVATION.json`; `evidence/MODEL_EXTRACTION.json`; and the unchanged CA01 references. The proof assessment above is the reviewer's analysis of those supplied definitions and arguments, without external-source substitution.
