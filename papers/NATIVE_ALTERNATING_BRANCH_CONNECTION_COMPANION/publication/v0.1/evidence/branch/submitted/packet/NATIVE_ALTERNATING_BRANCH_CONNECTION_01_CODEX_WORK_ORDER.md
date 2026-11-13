# Codex investigation order — Native alternating-branch connection

**Task:** NATIVE_ALTERNATING_BRANCH_CONNECTION_01  
**Date:** 11 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Scientific lead:** GPT; investigation and independent challenge: Codex  
**Authority:** The author requested the next bounded native-model investigation. This order commissions investigation and a review return, not a manuscript, software adoption or publication.

## 1. The one question

**Is the H-symmetric two-cycle certified by Paper G's repaired M3 result at mu=1/200 on the same nontrivial solution branch that emerges in M2's local supercritical period-doubling?**

Keep the native recurrence unchanged. Fix the existing M2/M3 host parameters and examine only their already identified phase-strength interval. A connected branch proof would relate the known local onset mechanism to the known finite-amplitude alternating regime. A rigorously established intervening obstruction, or a precise partial result, is also a valid scientific outcome.

This is NOT another proof that the M2 branch exists, another M3 entrance-capture calculation, or a sharper index/radius for the just-published turning-capture companion. Nor does it assume that all native examples settle: the latest companion and Paper G concern different coefficients and different regimes.

## 2. Mandatory prior-work gate — before new continuation calculations

Read `PRIOR_WORK_COMPARISON.md` and the packaged controlling text. Complete a bounded comparison against the existing Paper G supplement and relevant later local research. Search by statements as well as names: M2/M3 branch identity, mu=0.005 or 1/200, continuation from the flip, an explicit near-onset interval, and endpoint identification in U_plus.

The relevant starting sources are Paper G Sections 4–6 and its claim map; the final M2/M3 acceptance and correction records; NCM-DUAL-02's prior-results comparison; the later coherence-return work; and the current publication catalog. A short local persistence/symmetry result about M3 is NOT the missing continuation across the full interval. The collective paper's positive aligned-equilibrium continuation is also a different branch.

Record one of:

- **ALREADY_RESOLVED:** an existing result answers this exact question. Cite its theorem, hypotheses and proof/evidence and stop; no duplicate investigation or paper.
- **PARTLY_RESOLVED:** reuse every established subinterval/anchor and commission only the remaining connection within this order.
- **DISTINCT_GAP:** proceed with the bounded question below.
- **SOURCE_BLOCKED:** name the specific indispensable missing or inconsistent source and return the useful analysis already completed. Do not substitute a rounded parameter or ask the author to rediscover coefficients.

The present GPT comparison supports a distinct gap in the inspected sources; it is not an exhaustive search of every archive. Historical statements that no M4 was commissioned describe those earlier assignments. This order authorizes only this newly named, limited branch-connection task, without reopening the accepted M1–M3 premises.

## 3. Exact frozen family and source identities

Use the same simultaneous ordered recurrence throughout:

\[
v_i=\Omega_i+\epsilon\Omega_i(k_i-|\Omega_i|^2)
      +g\sum_{j\ne i}(\Omega_j-\Omega_i),\quad
\delta_i=\lambda\sum_{j\ne i}\sin(3[\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i]),
\quad F_\lambda(\Omega)_i=v_i e^{i\delta_i}.
\]

All prestages use the same old state; all phase kicks use the same complete prestage. Preserve Arg0(0)=0 and the implementation's separate lambda=0 convention. Do not normalize amplitudes, cycle coefficients, alter a phase rule, add a receiver or feed a passive observable back into the map.

Fix exactly

\[
\epsilon=1/20,\quad g=1/5,\quad
k=(1,1.2208964704604097,6.35310346037241).
\]

Those terminating decimals are exact rationals. The positive host u is the root identified by the accepted M2 host box, not its printed decimal center. Set

\[
M_u=I+\epsilon\operatorname{diag}(k-u^2)+gL,\quad L=\mathbf1\mathbf1^T-3I,
\quad B_0=V^TM_uV,
\quad \lambda_c=(1+1/m_1)/9,
\]

where V is the source's fixed orthonormal basis of u-perpendicular space and m1 is the larger eigenvalue of B0. The family is **lambda=lambda_c+mu, 0<mu<=1/200**, with exactly this same u, V and critical value. No decimal approximation to lambda_c is an exact replacement. Each member is a fixed-parameter autonomous map: parameter continuation is NOT an evolving trajectory with lambda changed at each native update.

Use the source slice s(z)=u+xi+i V eta, z=(xi,eta) in R^3 x R^2, quotient Fhat_mu=Q composed with F_(lambda_c+mu) composed with s, and H(xi,eta)=(xi,-eta). The selected gauge requires u^T(u+xi)>0 and nonzero u^T F(s(z)); every native prestage involved must be nonzero.

The endpoint is the unique M3 two-step fixed point in the EXACT U_plus defined by `m3_accepted_support.json -> values.exact_receipts.Up`. Its positive weights are at `positive_weights`. Rounded center/radius displays do not define U_plus. `Um` is an outer image enclosure, not an exact image or another proved trapping set.

The two exact data files and final M2 authority records are to be read/copied from the existing Paper G supplement, using `SOURCE_GUIDE.md` and `REQUIRED_LOCAL_INPUTS.json`. They are deliberately not retyped from printed decimals. Their retrieval/identity check is part of this assignment, not author homework. The text sources bundled here are sufficient to specify the question, but are not a substitute for those endpoint data in a numerical proof.

## 4. Investigation sequence

### B01 — exact equation and branch discrimination

Form the symmetry equation

\[
G(z,\mu)=\widehat F_\mu(z)-H z=0.
\]

A nontrivial regular solution with eta not zero has a two-cycle in the quotient. Reuse and explicitly check the inherited equivariance argument for its full-state two-cycle; this algebra is not a newly discovered mechanism.

The host z=0 solves G=0 for EVERY mu. Solving G numerically can silently return that trivial branch. Use a declared nontriviality/phase-orientation condition, track the H-related pair, and never identify branches by a sign convention alone. Distinguish existence of a root, identity of its connected branch, its primitive period and its attraction.

`GPT_ANALYTICAL_GUIDE.md` supplies a proposed regularized near-onset formulation. It is a lead to check, not an accepted theorem or a prescribed numerical implementation. An equivalent rigorously justified formulation is allowed.

### B02 — anchor to the actual local M2 branch

M2's phrase “sufficiently small positive mu” does not certify ANY chosen numerical starting offset. In particular, starting at 10^-4 and observing the asymptotic amplitude law would leave an unproved gap to zero.

Obtain a genuine branch anchor by a removable-singularity/amplitude formulation at onset, explicit local remainder bounds and uniqueness, or another proof joining to the accepted local branch. Specify the exact root normalization and prove that the anchored nontrivial family has mu>0 and tends to the M2 host in the correct critical direction.

A rigorous near-onset interval must overlap the later finite continuation certificate. Do not treat O(mu^2), a fitted square-root law, or a small Newton residual as an explicit error bound. If the onset connection remains unresolved, keep that limitation even if the rest of the interval is successfully continued.

### B03 — bounded continuation along this family only

Use nominal root continuation to select centers, predictors, intervals and preconditioners if useful. Freeze its finite budget and record it. No broad parameter scan, other k/epsilon/g family, or long entrance-trajectory rerun is authorized.

Then seek validated connected continuation covering the intended interval without gaps. A suitable route is a finite collection of parameter intervals with uniform interval-Newton/Krawczyk or contraction bounds, together with analytic control of the near-onset segment. State and verify the actual theorem used.

For each patch, retain parameter bounds, state enclosure, regularity margins, residual/derivative enclosures and the existence/uniqueness decision. Approximate centers and nonsingular preconditioners are computational choices, not exact orbit points. Verify all required inverse/nonsingularity conditions.

**Two overlapping boxes do not alone prove that their roots coincide.** At every join, show that the relevant roots lie in a shared uniqueness region, or supply an equivalent rigorous identification. Exact parameter coverage and branch matching are separate checks.

Ordinary continuation in mu is preferred if it stays regular. If a fold requires an arclength/amplitude chart, it is permissible as a mathematical coordinate change, with verified chart transitions and the same physical model and bounded parameter corridor. Report if the result is a connected curve rather than a single-valued graph over mu. Failure of a solver, interval overestimation, or a gauge chart is not by itself a dynamical obstruction or proof of disconnection.

### B04 — identify the endpoint with repaired M3

At exact mu=1/200, prove that the continued nontrivial solution, or its H partner under an explicitly recorded parity choice, is inside U_plus and hence equals its inherited unique two-step fixed point. Alternatively give an equally strong common-uniqueness argument. Intersection of enclosing boxes, close coordinates, matching |W|, or similar plots is not endpoint identification.

Reuse the accepted M3 trapping and uniqueness theorem. Do not repeat the 301-update entrance propagation, the withdrawn differently normalized auxiliary run, or the old capture repair. Once the endpoint is identified, the old entrance theorem applies to that endpoint; this does not create entrance-capture theorems at other mu values.

### B05 — stability and meaning, separated from branch identity

Where the proof or inexpensive additional bounds support it, assess transverse attraction using the actual two-step quotient derivative

\[
P_\mu=D\widehat F_\mu(H z(\mu))D\widehat F_\mu(z(\mu)).
\]

A contraction used to validate roots is an auxiliary solver; it does NOT establish dynamical contraction of P_mu. The full complex map retains a neutral common-phase direction, so attraction is modulo common phase.

Label the stability conclusion independently: proved throughout; proved on specified subintervals; a certified loss; or unresolved/not assessed. A connected branch may lose stability, and a loss of stability alone need not end the branch or its two-step phase cancellation. Do not demand a uniform contraction constant strictly below one as mu tends to zero; the critical limit has multiplier one for the second iterate.

The existing C, W and Gamma may be evaluated to explain the resulting branch. Their oddness gives sign reversal on a proved H-exchanged cycle. Nonzero magnitude at both endpoints does not prove nonvanishing throughout; any all-interval nonvanishing claim needs its own bound. Additional amplitude laws, optimized thresholds, global basins and physical-field interpretations are outside the requested outcome.

## 5. What constitutes an adequate result

The preferred result is a proved connection from the M2 onset to the M3 endpoint, with the exact range, regularity and stability scope stated. Do not preselect PASS.

If a full connection is not established, return the strongest bounded result and its exact remaining gap: for example an anchored local segment, an endpoint-connected interval with an unresolved interval to onset, a certified fold, a certified stability change, or a regularity/uniqueness condition that remains undecided. “No connection” requires a proof, not continuation failure. A partial branch segment must not be advertised as the completed M2-to-M3 result.

Separate inherited claims, newly proved deductions, computational certificates, nominal numerical evidence and interpretation. A compact proof with a small number of substantive conclusions is preferable to splitting routine bookkeeping into purported theorems.

## 6. Verification and reproducibility

Write new work in a fresh directory under
`C:\TORMENT\TRIOCTAGON_new\research\NATIVE_ALTERNATING_BRANCH_CONNECTION_01\`.
Keep the checkout, received packet and inherited evidence read-only. Work in Windows Command Prompt with `conda activate torment`; record the ACTUAL Python, dependencies and command lines. Use existing dependencies; no installation or global environment changes. Do not use Python -O for assertion-based checkers.

Mathematical parameter strings, host/basis/critical-value definitions and the exact M3 trap must remain connected in the whole certificate. Inherited intervals may be reused as accepted inputs; authenticate them and state their role. Recompute only a narrowly necessary host or derivative enclosure if the new proof needs tighter bounds, identifying this as supporting work rather than a new host theorem. Do not replay the whole Paper G supplement or historical scientific suites by default.

The short-kick bound |delta|<1/100 in the turning-capture certificate belongs to a DIFFERENT parameter family. Do not reuse that bound, its convergence constants, or its 50-step checker without proving new applicability. Derive trig bounds for the actual intervals here. No floating finite-difference derivative is a certified enclosure.

Provide a checkable certificate and checker for new interval claims. Prefer an independently organized arithmetic/containment check of decisive new inequalities. Disclose any shared interval engine, differentiation code or copied helper; a replay of shared code is corroboration, not a new independent implementation. Written regularization and patch-joining arguments remain necessary even when every numerical check passes.

Include a few relevant rejection controls, such as a false coverage interval, a broken join, a substituted host solution or an invalid endpoint inclusion. They test the checker, not scientific novelty. Preserve unsuccessful attempts and bound their interpretation; do not silently refresh expected values to obtain agreement.

## 7. Return deliverables and stopping rule

Return one review ZIP with a SHA-256 sidecar, standalone result summary and proof report. Include:

- completed prior-work comparison and scope decision;
- exact case and input/source identities, including the two endpoint-data files copied unchanged;
- written derivation, branch-anchor and joining arguments, endpoint identification and separate stability disposition;
- nominal planning data clearly labeled, new certificate/checker and actual execution logs;
- claim-to-source/proof ledger with assumptions, accepted/inherited/new status and remaining limits;
- a compact self-excluding file manifest and final archive integrity check.

Keep the readable result summary short: what connects, what does not yet connect, what was actually checked and what that tells us about native dynamics. Do not write a manuscript, add diagrams solely for decoration, launch successor tasks, or perform repository writes. No commit, push, release, tag, kernel/UI/API change or physical-model adoption is authorized. Read-only source/provenance queries are allowed; no checkout reset or mutation is needed.

Return to GPT and the author for review. **No author geometry decision is required within this fixed mathematical question.** If answering a different physical question would require a new coupling or geometric attachment, leave it outside this task rather than choosing it silently.
