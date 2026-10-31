# GPT review — NCM-DUAL-02 v0.1

**Date:** 31 October 2026  
**Task:** Independent review of the supplied existing-equation investigation, not publication or implementation approval.

## Disposition

**Accepted as a completed bounded mathematical investigation. No blocking error found in the principal proofs or their stated scopes.** The package establishes useful return criteria and obstructions inside the existing mathematics. It does not establish a native three-update coherence cycle with quarter-phase remainder, a native twelve-update orbit, or a native-to-cone evolution correspondence. Keep motion integration and publication parked. No additional author geometry specification is required for the next equation-level question.

The author's correction is controlling: the golden-ratio wording illustrated the picture; it is not a new controller requirement. The existing constants were neither changed nor fitted.

The positive question is meaningful to the established model: which information returns, and which does not? The stronger proposed cone choreography remains a hypothesis, not a result of the unchanged native recurrence.

## Material reviewed

The attached `REPORT(20261031-135730).md` and `NCM_DUAL_02_v0.1_REVIEW.zip`, including the report, claims table, predeclared cases, verifier, results, before/after source records, command/log files, closeout, and member manifest. The prior uploaded NCM-DUAL-01 archive was used only to obtain its byte-identical `results.json` for the verifier's retained-product comparison. Its checker was not rerun.

The original NCM-DUAL-02 lead packet was inspected to resolve the report's intake limitation. The long accepted D1/M3/coherent certificates were not independently replayed. Their theorem statements remain inherited rather than newly certified by this review.

## 1. Package and replay checks

- All **16/16 manifest-listed members** match their lengths and SHA-256 hashes. The archive has those 16 members plus `MEMBER_MANIFEST.json`, with no extra members.
- The separately attached report is byte-identical to the report in the archive.
- The predeclared case-plan digest agrees with `results.json`.
- The 18 source before/after records are internally consistent with their before manifest and all record unchanged bytes. The live Windows originals were not independently accessible or inspected here. This is not a whole-checkout preservation audit.
- The uploaded archive's computed SHA-256 is `b9e2207759f73f2890574d59aefb39931d425664046c8cd06b17a72aaefa8224`. This is a computed content identifier, not producer authentication or a comparison with the external Windows archive receipt, which was not included.
- **46/46 verifier checks passed** in a separate replay directory.
- All mathematical results, exact expressions, numeric diagnostic strings, native-case values, check names, outcomes and totals match the submitted `results.json` exactly as parsed values. The five differing fields are timestamp, interpreter path, platform, Python version, and NumPy version.

### Replay environment and adaptation

Replay: Linux, Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.3.5. This is not a Windows recertification. The original report lists Windows/Python 3.11.15 and NumPy 2.4.4.

`verify.py` was unchanged. In the **replay copy only**, the `DUAL_RESULTS.path` entry in `SOURCE_MANIFEST.before.json` was redirected to the prior result extracted from the uploaded NCM-DUAL-01 archive. That prior result is 80,255 bytes, SHA-256 `c0ecfe0fed7f6be7893933a536684ed3bbb91239b96d8304ee64fd6efd3afd26`, exactly matching the declared input. This path adjustment does not claim access to the Windows originals or reproduce their preservation checks.

Command used:

```text
python -X utf8 -I -B /mnt/data/ncm_dual02_gpt_review/replay/verify.py
```

The replay repeated only this task's eight predeclared cases/nine native-formula updates, plus its symbolic and SRG diagnostic work. There was no native-orbit search, old scientific checker execution, project import, application change, Git operation, installation, or physical calibration.

### Lead-checker intake clarification

The original uploaded lead packet contains `lead_checks/check_leads.py` and `lead_checks/lead_check_results.json`. Codex's report correctly records that those were not among the two files it received locally or found in its bounded search. Therefore its statement is a **local intake limitation**, not evidence that the checker was absent from the original ZIP. Its independent 46 checks appropriately did not rely on the unavailable earlier run. This requires no scientific repair or repeat of the completed investigation.

## 2. Proof review

### Regular-block coherence return

The report's main theorem is sound under its stated hypotheses. For nonzero z, equality of the unnormalized rank-one matrices H(F^p z)=H(z) implies F^p z=mu z with a unique unit-modulus mu. The trace equality is essential: it retains raw norm, unlike a normalized projector.

Regularity for the first p prestages makes common-phase equivariance available on that block. Multiplying a block's initial state by mu changes no prestage-zero pattern, and the same block repeats up to that phase. Hence all following blocks are regular and

`F^(mp+r) z = mu^m F^r z`, for m>=0 and 0<=r<p.

If p is the minimal coherence period, every full-state period is a multiple of p. Full-state minimal period is p times the exact finite order of mu, or there is no finite full-state period if mu is not a root of unity. This is a conditional theorem, not existence of any particular p or mu. Numerical closeness to i cannot establish exact order four.

### Normalized-projector limitation

The exact uniform-line example is correct. With the stated coefficients and r0=1/2, r1=43/80 and r2=2947693/5120000, while the repeated-first-multiplier prediction is 1849/3200. The normalized projector is unchanged, but the raw amplitude multiplier is not. The additional unequal-component scaling argument correctly refutes general autonomous normalized-projector closure in its stated parameter class.

### Native controls and readout periods

The inherited controls address different regimes and must not be combined into one orbit. D1 gives stationary coherence and nonzero native phase advance on its stated local branch; M3 gives an exact limiting two-cycle, with full-state period two; the coherent invariant domain converges to fixed states. The report correctly distinguishes convergence to a limiting cycle from becoming exactly periodic after a finite number of steps.

The period-divisibility result for single-valued current-state readouts is correct. It prevents deriving three distinct stations or twelve marked stages from M3's exact limiting two-cycle at a fixed integer sampling stride. It does not prohibit those patterns in every other native regime, nor apply unchanged to an observer with additional clock or memory state.

### Q=iPi

The operator powers and state-period classifications are correct. In particular, an operator of order twelve need not give a twelve-period orbit for every state: the equal-channel line has period four under Q. Some other Pi eigenvectors have full Q-period twelve while their coherence is stationary. Thus an operator count alone identifies neither a three-stage relative pattern nor the native update.

The native covariance proof correctly keeps parameter permutation distinct from fixed-parameter symmetry, and its zero-prestage exceptions matter. The consensus fixed-point counterexample refutes the global identity F=Q; it does not rule out every restricted orbit relation involving Q.

### Fixed SRG

The exact identities A^3=D I and U^3=D(B^3 tensor I) are correctly inherited and checked. With the frozen constants, 0<D<1 excludes every nonzero raw periodic orbit of U, without needing an irrationality proof. The strict bound on the internal eigenphase excludes scalar B^3 and B^12. At those two step counts, the projective-return eigensector classification is sound. Projective return is not raw-state return, and the transfer index is not native update time.

The existing helicity extraction/injection is a genuine same-step intertwining. The obstruction to a fixed global complex-linear surjection from raw SRG to the nonlinear native map is correctly scoped; it is not a universal statement about nonlinear or restricted maps.

### Cone transport and matched face transport

On the specified independent legs, k dot u=0 and u'=k cross u. The transported tangent marker satisfies v'=-u(u' dot v), so its tangential derivative vanishes on the sphere of unit directions. The report therefore identifies the connection from the actual paths, not merely from a picture of a surrounding sphere.

Matched face transport has identity loop action on each tangent plane. Its ambient 3x3 extension is a rank-two projector, not I3. Conjugation by fixed per-label frame identifications cannot turn an identity loop into the nontrivial transverse quarter-turn of the specified cone loop. The report does not overextend this obstruction to all state-dependent correspondences.

The sphere of directions in this argument is not a demonstrated physical field on the close enclosing sphere.

## 3. Reviewer consequence: an existing diagnostic can see a conditional phase remainder

This is an additional deduction from the report's return theorem and its existing EMA innovation formula, **not a demonstrated orbit or a new motion law**.

Use zero-based channel labels. Write

`K(z) = z0 conjugate(z1) z2`, and `j(z)=Im K(z)`.

The scalar j is the cubic quantity already used by the EMA observer. For any unit common phase mu,

`K(mu z) = mu K(z)`.

Suppose the report's hypotheses hold with minimal coherence period p=3 and mu=i. Let K(z)=a+ib. At successive returning coherence blocks, exact substitution gives:

| Native index | Native state | Existing scalar j |
|---|---|---|
| 0 | z | b |
| 3 | i z | a |
| 6 | -z | -b |
| 9 | -i z | -a |
| 12 | z | b |

For mu=-i, the scalar sequence is b,-a,-b,a,b instead.

In a regular returning block, z itself has no zero components: the final regular prestage produces nonzero components in F^p z=mu z. Hence K(z) is nonzero. Its four-block real sequence is nonconstant and has minimal sequence period four. For example, the sum over four entries of the squared difference between entries two blocks apart is `8(a^2+b^2)>0`; the corresponding one-block sum is `4(a^2+b^2)>0`.

Because H has minimal period three, the **joint sequence** (H(z_n),j(z_n)) would have minimal sequence period twelve in this conditional situation. This concerns the period of the entire sequence, not the first accidental equality of two individual readout values. The joint readout is not asserted to be an autonomous closed state description.

By contrast, staged Z with the same frozen clock/configuration factors through norm and channel area, hence through H. It would repeat with the coherence blocks and cannot distinguish this common-phase remainder at those block returns.

This distinction is useful: the established mathematics already contains both phase-insensitive and phase-sensitive quantities. It still does not provide the cone-pose map or prove the hypothesized native block. The full EMA memory trajectory and clocked Z need not repeat immediately with j; no periodic EMA-state initialization, steady state, or clock alignment is inferred. EMA is not being proposed as a controller for the cones.

Nine additional symbolic checks of these transformation/sequence identities passed. They used SymPy only and performed zero native updates. These checks and their proof remain separate from Codex's 46-check report.

## 4. Scientific direction and stop conditions

The completed task proves **how** a native return would lift, and rules out several proposed shortcuts. It intentionally did not search for the relevant native return. Absence of an exhibited p=3 block is not a theorem that none exists anywhere.

The next defensible equation-level question is an existence/classification problem at a previously established, fixed native parameter set:

`F^3(z) = mu z`, with `|mu|=1`, regular prestages, raw coherence retained, and lower coherence periods explicitly excluded.

The phase mu must be determined by the unchanged equations, not fixed to +/-i to manufacture twelve. A non-quarter phase, a fixed relative shape, failure to find a root, or a proved obstruction in a stated domain must all remain possible outcomes. A finite unsuccessful search does not prove absence. Any numerical discovery would require separate mathematical validation before an exact return claim. No new clock, leg counter, feedback, normalization, or parameter fitting is permitted by this recommendation.

Even an actual relative-periodic orbit would be only one part of the desired bridge: a justified current-state/observable-to-pose relation and its evolution identity would still need to be established. Matching twelve alone does not identify the cone choreography. Do not use a chart or marker chosen specifically to reproduce the animation as proof that the original model already performs it.

No successor executable work order is issued by this review. This note identifies the focused next question for discussion without reopening completed certificates or asking the author to invent a law.

## 5. Paper readiness

Agree with the report: not ready for a manuscript claiming native cone motion, a native twelve-update spin, energy transport, or physical duality. The positive return theorem and several obstructions are useful source-grounded lemmas; novelty is not established by this review. They can support a future account if a substantive model-specific correspondence or classification is obtained.

Do not discard the author's intuition, and do not treat the numerical pattern as confirmation of the missing dynamics. Preserve the kinematic result, the established-state result, and the unproved bridge as three distinct records.

## Evidence files

The accompanying review ZIP contains this note, package/provenance audits, exact replay comparison, replay log/results, the reviewer-only phase-visibility checker, and its nine-check results/log. Received inputs were kept unchanged. All reviewer work was written in the conversation sandbox, not the user's checkout.
