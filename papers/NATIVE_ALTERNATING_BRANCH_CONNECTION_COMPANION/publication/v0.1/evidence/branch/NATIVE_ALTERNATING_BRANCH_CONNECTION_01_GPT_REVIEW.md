# NATIVE_ALTERNATING_BRANCH_CONNECTION_01 — GPT scientific review and acceptance

**Date:** 11 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Investigation:** Codex  
**Disposition:** **ACCEPTED at the stated scope. No mathematical correction required.**  
**Status:** Project-internal scientific acceptance of this investigation. Not external peer review, proof-assistant certification, manuscript approval, or publication authorization.

## 1. Accepted result

For the exact existing Paper G parameter family

\[
\epsilon=\frac1{20},\qquad g=\frac15,\qquad
k=(1,1.2208964704604097,6.35310346037241),\qquad
\lambda=\lambda_c+\mu,
\]

where the terminating decimals are exact rationals and \(\lambda_c\) is defined by the accepted exact M2 host, the submitted result connects the nontrivial M2 alternating branch to the exact repaired M3 cycle for every

\[
\boxed{0<\mu\le 1/200.}
\]

The family is continuous to the host as \(\mu\downarrow0\), smooth at every positive parameter, and a graph over the stated parameter interval. Its selected representative lies in the certified regular chart. It is not a claim of uniqueness among every remote state-space solution. At each fixed positive parameter, the quotient and lifted full-state orbit have primitive period two. Varying the parameter to describe this family is not a time-dependent parameter schedule imposed on one trajectory.

The new stability statement is accepted separately and only on

\[
\boxed{4999/1000000\le\mu\le1/200,\qquad
\|Q^{-1}D\widehat F_\mu^2 Q\|_\infty<0.9601}
\]

at the certified cycle, in the verified similarity norm. This establishes local quotient attraction, or attraction modulo common phase in the full state. It is not a new trapping-domain or uniform-basin theorem. The inherited M2 sufficiently-small-positive-parameter attraction and inherited M3 endpoint trapping retain their own scopes. **Attraction across the full connected parameter interval remains unresolved by this investigation.**

## 2. Disposition of the claim ledger

| Record | Disposition | Scope retained |
|---|---|---|
| I01 | Inherited accepted premise | Exact positive M2 host, normalization, compression, critical data, corrected cubic coefficient and local branch theorem. No old host/jet theorem replay. |
| I02 | Inherited accepted premise | Repaired M3 endpoint uniqueness, H exchange and index-301 entrance theorem. No new entrance propagation. |
| N01 | Accepted | Removable normalized system, nonsingular limiting Jacobian, and connection of the actual M2 germ to the first uniform patch including zero. |
| N02 | Accepted | All 128 parameter patches, 127 common-uniqueness joins, and exact M3 endpoint identity. |
| N03 | Accepted as an application of inherited symmetry | Primitive period two for every positive parameter and sign reversal of the stated odd phase-invariant observables. No all-interval nonvanishing assertion for W or Gamma. |
| N04 | Accepted on the explicit narrow interval | Actual two-step derivative bound, independent of the root-solver contraction argument. Full-range attraction not claimed. |

No equation, certificate, accepted numerical bound, or scientific disposition needs replacement. The submitted broad-stability failures are correctly retained as inconclusive sufficient bounds, not as instability evidence.

## 3. Prior-work and premise boundary

The comparison in `submitted/PRIOR_WORK_COMPARISON.md` identifies the precise missing implication rather than restarting M2 or M3. I cross-checked the relevant retained sources: Paper G's local theorem and its explicit non-continuation boundary, final M2 acceptance and normalization corrections, the repaired M3 uniqueness statement, and the comparison's distinction from local M3 persistence and from the different turning-to-alignment family.

The accepted contribution is **the connection of these particular previously established objects**, not a new claim that period doubling, the M2 local branch, the M3 captured orbit, or validated continuation methods exist. The `DISTINCT_GAP` disposition remains a bounded project-corpus finding. It does not establish exhaustive coverage of every unindexed archive or worldwide priority.

The proof uses the exact root selected by M2. Neither a displayed decimal host nor a midpoint of its enclosure is substituted as the proof's exact host. All critical quantities use this same host and the same source basis and sign convention. The original host/cubic/entrance verifiers were read as references where needed but not executed during this review.

## 4. Mathematical review

### 4.1 The apparent onset singularity is genuinely removed

The change of coordinates is

\[
t=\mu/\nu,\qquad a=\sqrt t,\qquad
\xi=tX,\qquad \eta=a(e+t y e_\perp),\qquad\nu>0.
\]

Thus \(e^T\eta=a>0\) for positive \(\mu\). The normalized solver cannot silently use the persistent equilibrium \(\eta=0\) as its nontrivial branch. For fixed positive \(\mu\), the coordinate determinant in the oriented imaginary basis is \(t^5/(2\nu)>0\), as stated.

I checked the cubic prestage expansion, the normalized harmonic-three sine, and the positive-gauge formulas against the original ordered map. The entire functions \(C(w)=\cos\sqrt w\) and \(S(w)=\sin\sqrt w/\sqrt w\) are evaluated using their power-series definitions, so the removable formula does not require a numerical square root of a possibly negative auxiliary argument or division by the zero amplitude.

The divided-difference operations retain exact identities of the form \(f(t)=f_0+t f_1(t)\); their second entries are not discarded Taylor remainders. The constant identities \(\widetilde o(0)=u\) and \(V^T\widetilde j(0)=-e\) follow from the exact inherited host and compression. Dropping those constants in the residual is therefore justified by exact identities, not a rounded near-zero value.

The 18-term C1/S1 bounds were checked with their derivative tails. The first omitted terms have denominators \(38!\) and \(39!\), respectively. On \(|w|\le1\), the stated value bounds \(2/38!,2/39!\) and derivative bounds \(36/38!,36/39!\) are valid geometric-tail bounds. The automatic derivative adds the derivative tail multiplied by the derivative of its argument. The recorded squared-kick bound is strictly below 0.0823, within this sufficient domain. This is not the unrelated short-kick hypothesis used by the turning-capture certificate.

### 4.2 The first patch is anchored to the actual M2 branch

At zero, the real equation gives \(X_0=w_R/2\). The imaginary critical projection gives \(\nu_0=c_{\rm nf}/\sigma>0\), and the noncritical projection determines \(y_0\). The full limiting Jacobian retains its lower-left coupling; its block-triangular structure, invertibility of \(J_R-I\), and independent lower-right columns \(\gamma e_\perp,-\sigma e\) establish nonsingularity.

The accepted source enclosures for \(w_R/2\) and \(c_{\rm nf}/\sigma\) are consistent with the refined onset root enclosures. The written asymptotic and local-uniqueness argument identifies this normalized germ with M2's H-exchanged branch, including its parity. The first certified interval is exactly \([0,1/25600]\), so no unsupported choice of a merely 'small enough' numerical starting parameter is needed.

### 4.3 Patch contraction and joining prove a connected graph

For each parameter interval the proof uses a fixed rational preconditioner and the map \(T_\mu(x)=x-A R(x,\mu)\). The center-defect estimate preconditions the parameter derivative before integrating over the parameter offset, which is legitimate because A is fixed. Strict inclusion and the weighted derivative norm below one prove existence and uniqueness in the stated box.

The bound on \(I-A D_xR\) also proves that both A and the square state Jacobian are nonsingular. This is the needed justification for root equivalence and local smooth dependence; A is not assumed to be an exact inverse because it was generated numerically.

All parameter intervals equal \([i/25600,(i+1)/25600]\), with \(i=0,\ldots,127\). At each shared endpoint the connector is a **convex uniqueness region containing both adjacent evaluated boxes**. A derivative contraction bound on that region forces the two already-established endpoint roots to coincide. Mere box intersection would not be enough; the submitted certificate does not make that mistake. The connector need not have a separate self-map property, because existence has already been supplied by the adjacent patches.

Independent exact comparisons of the stored bounds give maximum patch and join norms below 0.614 and 0.583. The region bounds keep the slice projection, prestage real parts and moduli, gauge denominator and nu strictly positive. Root-solver contraction is not a dynamical attraction estimate.

### 4.4 The endpoint is the original M3 orbit

The endpoint refinement is inside the last patch's uniqueness region and hence selects that same continued root. Its reconstructed **entire interval enclosure** lies strictly inside the original exact `values.exact_receipts.Up`. The smallest coordinate margin is greater than 0.00001098. The accepted positive parity already selects this box; no undocumented parity swap is used.

The root equation and H equivariance imply that this point is a two-step fixed point. Inherited M3 uniqueness in Up therefore identifies it with the accepted M3 point. This is an exact set-containment and uniqueness argument, not agreement of a plot, a rounded center, or a residual. The historical outer image enclosure `Um` does not enter the identification.

For positive mu, nonzero eta excludes period one in the quotient. If \(A=s(z)\) and \(F(A)=e^{i\theta}\overline A\), regular common-phase and conjugation equivariance give \(F^2(A)=A\). Thus the full-state primitive period is also two. This reuses the existing lift argument at newly connected branch points.

### 4.5 The stability claim is appropriately narrower

The actual quotient derivative is computed by differentiating the original cubic prestage, phase rule and gauge, not the divided root equation. At a symmetric root,

\[
D\widehat F(Hz)D\widehat F(z)=(H D\widehat F(z))^2.
\]

The numerical basis only selects fixed rational matrices Q and R_Q. The exact inverse-defect inequality \(\|I-R_QQ\|_\infty<1\) verifies nonsingularity and justifies division by \(1-\|I-R_QQ\|_\infty\). The strip's root enclosure is identified with the already continued branch through parent-patch uniqueness. The final derivative bound is approximately 0.9600371642733128, with the stored rational quantity controlling the strict 0.9601 comparison.

This proves the stated local attraction on the explicit strip. It does not prove that all 128 broad parameter intervals are attracting. Their failed sufficient bounds do not prove a loss of stability. The neutral full-state common-phase direction is not falsely counted as contracting.

## 5. Actual reviewer executions and integrity checks

The scripts were inspected before execution. All original submission bytes were preserved. Reviewer computations were performed in a separate extraction.

| Check | Outcome |
|---|---|
| Incoming archive, checksum sidecar, CRC and safe unique names | PASS; 149 members |
| Self-excluding manifest | PASS; 148 file entries |
| External archive audit and standalone proof/summary identity | PASS; 149 audited members and both standalone documents |
| Source inventory | PASS; 34 entries |
| Original packet and its extracted contents | PASS; 23 members, unchanged |
| Packet source registry / additionally copied source records | PASS; 13 / 8 entries, including supplied Git blob identities |
| Complete submitted certificate checker replay | PASS; 128 patches, 127 joins, onset and endpoint refinements, stability records |
| Four submitted rejection controls | All rejected with their recorded reasons |
| Submitted algebra/source check replay | PASS; 31 checks |
| Stable scientific result fields versus submitted Windows outputs | All matched; execution times and timestamps excluded |
| Independent reviewer exact comparisons of reported margins | PASS |
| Independent direct-form numerical spot checks | PASS; five residual/Jacobian samples, explicitly non-proof diagnostics |
| Submitted bytes after all reviewer work | Unchanged |

**Execution environment:** reviewer Linux Python 3.13.5; Codex's recorded run is Windows Python 3.11.15 in `torment`. Only the conda-name guard in a replay copy of `scripts/common.py` was replaced by an explicit reviewer-Linux guard. Assertion optimization remained disabled. The adaptation diff and environment record are included. No mathematical checking function, interval precision, assertion, or certificate was changed. This is not a Windows rerun.

The generator and the submitted checker share their new interval/AD engine, as disclosed by Codex. The reviewer replay is another execution of that checker, **not** another independent interval implementation. The independently written direct-form spot check uses high-precision original complex phases and gauge formulas at five positive parameter samples, and checks values plus state/parameter derivatives. It uses a host midpoint only for this numerical diagnostic, not as an exact proof premise. These samples do not substitute for the interval proof or certify unsampled parameters.

No native trajectory, new root/continuation solve, old scientific suite, historical host/jet/capture verifier, remote publication audit or Git operation was executed for this review. Saved preservation logs are not relabeled as a fresh audit of the author's Windows checkout.

## 6. Limits and next disposition

The full branch connection is complete at this scope. The incomplete full-range stability assessment does not invalidate it and is not a mathematical blocker to documenting it.

Retain the following exclusions: no global state-space uniqueness or basin theorem; no entrance theorem away from the inherited M3 endpoint; no identification with the separate lambda=0.5 orbit; no claim that W or Gamma is nonzero at every intermediate parameter; no parameter ramp within an orbit; no physical magnetic-field, gravity, material-motion or clock correspondence; and no proof-assistant or external peer-review status.

For a reader-facing manuscript, describe the chart as the original-state/quotient chart, rather than letting shorthand such as 'physical branch' imply physical calibration. This is a presentation precaution, not a correction to the accepted equations or theorem.

**Recommendation:** document the completed M2-to-M3 connection as a focused companion to Paper G, explicitly separating the proved existence/identity interval from the narrower new attraction interval. Do not automatically expand this assignment to complete full-range stability before writing. A new manuscript, stability investigation, or publication requires its own instruction. The original Paper G edition and accepted M2/M3 evidence should remain unchanged.

## 7. Controlling submitted identities

- Review ZIP SHA-256: `a8394bea8d2a39a5124e1308e2bcc654a5401996f19a062f765548982abb0149`.
- Proof report SHA-256: `d4ac533f40ef51e1d45f606fd812244511fefaf3be0a5cf7725a3e6a97ca3744`.
- Connection certificate SHA-256: `3a3c61f2ad4905ef9c0f5eba5d1b91afb0ba6288b2bdc92ab4e240c07d7d1011`.
- Submitted checker SHA-256: `09131b16bd3655765ac208effe5de7d5e9abe09446d584b0c8ebb342f9f58405`.
- Submitted arithmetic engine SHA-256: `00df30f4d953c1cd57319a791ee68605430706cfb7a935f2df58c09963c0e1ac`.
- Submitted analytic model SHA-256: `97562d66b60d99af703f0df4e8970ee23d2bbfcb7b661c57e0454cbf77222f92`.

The complete original review archive and standalone returns are under `received/`; its extracted contents are under `submitted/`. Reviewer scripts, actual outputs and exact identity checks are under `reviewer/`. Historical documents retain their historical wording; this new acceptance does not edit them.
