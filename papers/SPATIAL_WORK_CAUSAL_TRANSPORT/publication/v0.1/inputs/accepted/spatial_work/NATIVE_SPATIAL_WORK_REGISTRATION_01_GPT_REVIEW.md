# GPT review — spatial observation and work compatibility

**Task:** `NATIVE_SPATIAL_WORK_REGISTRATION_01`  
**Review date:** 10 November 2026, Atlantic/Reykjavik  
**Disposition:** **W01–W05 accepted as stated, within their specified assumptions. No mathematical correction is required.**

This record accepts the submitted Codex proof and its scoped conclusions. It does not select a physical spatial transport model, approve a manuscript or publish new work. Author adoption of a future model remains distinct from this mathematical review.

## 1. Reviewed material and conclusion

The controlling submission is `NATIVE_SPATIAL_WORK_REGISTRATION_01_REVIEW.zip`, SHA-256:

`990439720bc70edd124dca759571405dfb214d61bc485224dd05bc66c5ac0b2e`

Its standalone proof review has SHA-256:

`fc6a045b548925baca811b70f1cceba982b48456ab07d592ab4bf520c38cfe18`

The [submitted proof review](submitted/NATIVE_SPATIAL_WORK_REGISTRATION_01_PROOF_REVIEW.md) supplies the mathematical evidence, especially R1–R5. Its [corrections and limits](submitted/CORRECTIONS_AND_LIMITS.md) and [claim ledger](submitted/CLAIM_LEDGER.json) preserve the correct domain distinctions. All submitted members are preserved under `submitted/`, including `inputs/` with the primary equations and previously accepted foundations. The complete original review ZIP and supplied checksum are also included unchanged under `submitted_archive/`.

The study establishes a definite observation operator on the six actual G arcs, a uniform bound with a complete history domain, its exact finite-window adjoint and the conditional work residual. C6 remains a causal observation. The advanced dependence appears in direct use of its mathematical adjoint as feedback on sufficiently long observation windows. The integrated work account includes a signed prehistory term. These are precise compatibility results; they do not already supply a causal receiving mechanism at G. [Submitted proof R2–R5]

## 2. Evidence and input identity

GPT independently checked the current submission's archive and input chain:

| Item | Result |
| --- | --- |
| Uploaded ZIP versus supplied SHA-256 | Match. |
| ZIP members and CRC | 79 members; CRC check passed. |
| Review manifest | All 78 listed files matched byte counts and SHA-256. The manifest excludes itself, explaining the 79-member archive. |
| Standalone proof and result summary | Exact matches to their archive members. |
| Returned original GPT packet | Byte-for-byte match to the issued 249,613-byte packet, SHA-256 `e1e771dd72fb236824933968b6bce437c9e7641bcbb65438d4d2c6c6f8b35bff`. |
| Preserved packet members | All 52 matched the returned `inputs/` copies. |
| Original packet manifest | All 51 entries matched. |
| Preserved source identities | All 37 matched; available Git-blob identities also matched. |
| Claim/source locators | All 41 source-locator instances matched their file hashes and recorded line text. Proof-location hashes matched the reviewed proof. |
| Reported exact checks | Four groups, A01–A04, with consistent code, recorded outputs and successful Windows execution records. |

These checks concern the new review submission. The previously completed combined-paper publication was not re-audited.

GPT read the full proof, the relevant retained definitions, the qualifications and the exact-check code/logs. The submitted scripts were inspected, not re-executed or modified. Codex's Windows execution in `torment`, Python 3.11.15 and SymPy 1.14.0, is documented by its supplied environment and execution records. The four groups are Codex's executed corroboration, not an additional set of executions by GPT. The functional-analytic conclusions are supported by the written proofs, not by those four algebra groups alone. [Submitted proof R0, R6; embedded `logs/EXECUTION_RECORD.json`, `logs/EXACT_CHECKS.json`]

## 3. W01 — geometry, arclength and sufficient history horizon

**Accepted as stated.** R1 starts from the actual six two-segment G arcs and retains both wraparound segments. The proof uses centered three-dimensional coordinates, common width scaling, the entire static parameter interval and full reflection with labels preserved. It does not add chords or fill apertures. [Submitted proof R1.1–R1.3; retained CC geometry `eq:vertices`, `eq:G`]

The endpoint argument correctly obtains

\[
\|X-O\|\le wR_0,\qquad
R_0^2=\frac{13}{12}-\frac{\sqrt2}{2}.
\]

The decisive lower-tip identity is

\[
R_0^2-\|L_k\|^2=h_g^2-\tau_g^2\ge0
\]

at width one. Elbows have smaller norms, and convexity extends the bound along each segment. This is a ball-radius argument, including height, rather than a cylindrical-radius estimate. The bound is attained at lower tips when tau_g=h_g. [R1.2]

The exact total labeled length is

\[
M_w(\tau_g)=6w\left[
\sqrt{v_0^2+d_g^2}+\sqrt{D(\tau_g)^2v_0^2+d_g^2}
\right],\qquad v_0^2=r_g^2+a_g^2-a_gr_g.
\]

Only the horizontal part of the lower edge gains the factor D. The twelve edges and the maximum at tau_g=h_g are correctly counted. In contrast, the triangle-inequality ceiling

\[
d_X(s)\le w(K_c+R_\Gamma+R_0)
\]

is expressly a sufficient bound. Attainment of the ball bound does not imply simultaneous attainment of the carrier-to-G distance ceiling. The proposed history horizon therefore remains sufficient and unoptimized. [R1.2–R1.3]

A01/A02 corroborate exact identities and all directly assembled edges. Their role is accurately limited. The accepted separation theorem is reused as an input; the new review does not claim to have independently repeated S01–S05.

## 4. W02 — bounded causal observation and point-record regularity

**Accepted as stated.** With the declared space-time L2 spaces and complete history interval, the isometric tangent encoding and Cauchy–Schwarz in carrier arclength give

\[
\|\mathcal K_GQ\|_{\mathcal Y}
\le\frac{a_o\sqrt{LM_w}}{\delta_w}\|Q\|_{\mathcal H}.
\]

The crucial second step integrates in time and translates u=t-theta_X(s) for fixed s,X. That proves both the norm estimate and representative independence through Tonelli/Fubini. It avoids taking unjustified traces of an arbitrary L2 function on a single retarded sampling graph. No additional sqrt(2) or sqrt(T) is required. The bound is not asserted to equal the optimal norm. [Submitted proof R2.1]

Positive delay gives the correct observation-causality statement. Common scaling cancels out of the displayed operator constant for fixed gain while the necessary history horizon still scales with w/c_e. This does not calibrate a physical clock. [R2.1]

The continuous-record argument separately uses C(I;H1_per), whose continuous spatial representatives and time continuity provide joint continuity. The narrow-graph example has constant L2 history norm and a point reading growing as epsilon^(-1/2); it correctly proves that a fixed point reading is unbounded in that weaker norm. Both claims can hold together because they concern different topologies. [R2.2–R2.3]

## 5. W03 — the exact adjoint and its causal qualification

**Accepted as stated.** The proof keeps the entire history interval and extends the dual test by zero outside [0,T]. The adjoint samples

\[
\widetilde\lambda(X,u+\theta_X(s))
\]

and uses the scalar component together with the tangent projection of the ambient vector component. The time substitution has unit Jacobian; no spatial-delay derivative belongs in it. The proof justifies absolute integrability before interchanging the integrals and supplies an almost-everywhere adjoint on the declared Hilbert spaces. The framed-output qualification is correct. [Submitted proof R3.1]

The two window regimes are essential:

- For T<=theta_min, the forward-time restriction is zero almost everywhere; any equality at u=0 is a null endpoint. The adjoint's prehistory part may remain nonzero.
- For T>theta_min, the explicit load bump is supported wholly after a cutoff, while its adjoint differs from zero on a positive-measure set before that cutoff.

The submitted witness is stronger than an isolated point-value argument: it establishes noncausal operator dependence in the L2 setting itself. The epsilon bounds keep every chosen support strictly inside the required domains. [R3.2]

The conclusion concerns direct use of this adjoint as a forward feedback rule. It is not a proof that every causal spatial extension is impossible. Nor is integrated duality an instantaneous power identity. No correction is needed to the submitted scope.

## 6. W04 — the present-state/history distinction

**Accepted as stated.** The explicit smooth time bump is placed around a genuine delayed sample and compactly inside the allowed past interval. The zero history and the spatially constant bumped history share the same carrier state at t_0. Positivity of the scalar kernel gives distinct C6 outputs, and continuity extends the difference to an observation neighborhood. [Submitted proof R4]

The conclusion is exactly a failure of factorization through the present carrier value on the stated unrestricted analytic history class. The witness is not claimed to solve C1 or RX. It therefore proves no competing-history result for equal full RX states, no native-map invertibility theorem, and no universal conclusion for a specified generated launch/prehistory protocol. These restrictions remain explicit in the proof, ledger and limits.

The earlier common-phase information result remains a separate accepted statement with its own target-rule and trajectory qualifications. W04 neither replaces nor strengthens it.

## 7. W05 — exact added work and the signed prehistory term

**Accepted as stated.** The source factor one-half in native feedback, the Euler identity J_f x=2f and the original B/B* pairing produce exactly the retained native and old-receiver powers. For conditional added carrier forcing, periodic integration leaves

\[
\dot H_{\rm base}=P_{\rm add},\qquad
P_{\rm add}=\int(pF_p+r_cF_r)\,ds.
\]

Both added-force contributions have the stated signs. The proof assumes sufficient solution regularity and integrable added work; it does not assert existence or regularity for an unspecified force law. [Submitted proof R5.1; retained RX candidate/power]

Native jumps retain the original map and F-first order. Post-jump endpoints count exactly 0<t_j<=T, so

\[
\Delta H_{\rm base}-B_N=\int_0^T P_{\rm add}(t)\,dt.
\]

The jump at zero is already in the initial value; one at T is counted. The baseline increment is not port work. [R5.2; retained RX accounts `eq:baselinewindow`]

Splitting the full adjoint pairing into negative and forward times gives

\[
W^{\rm test}=W_{\rm pre}+J_{\rm fwd}.
\]

Under the conditional formal force -K_G*lambda on forward times, the forward work is -J_fwd. Consequently

\[
\boxed{\Delta H_{\rm base}+W^{\rm test}-B_N=W_{\rm pre}.}
\]

The coefficient of the prehistory term is positive; the pairing itself is signed. Zero prehistory is sufficient, not necessary, for its vanishing. For short windows the forward force is zero, while W_test=W_pre can remain nonzero. All of these distinctions are retained. [R5.3]

The simple-delay examples are correct: direct integration of (t+1)^2 gives 7/3, 26/3 and 21 on the three stated windows, with the T=3 forward contribution 37/3 and prehistory contribution 26/3. Negating the test reverses the latter sign. The nonzero-history cancellation example is also exact. A03/A04 corroborate these algebraic details without masquerading as geometry-dependent operator proofs or RX trajectories. [R5.1, R5.3; embedded exact-check code/log]

Finally, the possible transit-store relation is a necessary balance for a later declared model. A residual alone establishes neither positivity, causality, a physical location nor an energy interpretation. The existing H_R is already part of H_base and is not counted twice. [R5.4]

## 8. Acceptance boundaries and current status

No requested replacement equation, bound, proof, source definition or interpretation is outstanding. `CORRECTIONS_AND_LIMITS.md` supplies important qualifications, not corrections to a false submitted claim. All five ledger items may be carried forward as accepted at their stated assumptions.

The previous C01–C05/Q01, S01–S05 and scoped cadence/receiving results remain accepted foundations. The present acceptance does not alter their preparation or domain limits. In particular, failed enclosing containment is not universal absence of delay; carrier/G separation does not assign zero to undefined aperture flux; and a mathematical G test measure does not become physical aperture area.

The completed contribution is **C6 spatial observation and work compatibility**. A causal receiving mechanism at G and the intended outward–around–inward route remain unconstructed by this study. No physical speed, six-way allocation, material receiver, connecting curve or aperture surface has been selected. There is no author geometry decision needed to close W01–W05.

## 9. Recommended next research target

The useful next move is constructive: **formulate and test one explicitly labeled causal extension with a declared transport/history state and nonnegative intermediate storage**, then determine whether it can retain the existing C6 forward observation and what additional port relations or gain conditions it needs. This is a recommendation for a new model assessment, not a result of W01–W05 and not an adoption of such an extension.

A realization of observation memory alone would not establish energetic passivity. A candidate must make the work at its boundaries and its stored quantity explicit, preserve or explicitly account for the existing RX subsystem, and demonstrate the claimed balance along its actual dynamics. The present results are requirements and diagnostics for that test; they do not uniquely choose the candidate.

The mathematical feasibility assessment can begin before choosing new G geometry. Its physical attachment must remain visible as a proposed choice: the author intends a central meeting region, opposed directions, outward spreading, curved return and possible transfer elsewhere with stationary supports. Once concrete alternatives would change that intended construction, show their consequences and ask one focused geometric question. Do not ask the author to recover old equations or parameters.

This review commissions no new manuscript, repository change or publication. The broader gravity–magnetism, outer-geometry and SRG directions retain their previously stated place and qualifications; no new strict ordering among them is imposed.
