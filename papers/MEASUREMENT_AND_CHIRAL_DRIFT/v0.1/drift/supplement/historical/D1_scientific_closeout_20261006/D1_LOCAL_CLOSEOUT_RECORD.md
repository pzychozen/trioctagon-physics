# D1 local scientific closeout record

6 October 2026 · External documentation only

**D1 is closed at PASS_WITH_QUALIFICATIONS.** The user authorized execution of the supplied `D1_SCIENTIFIC_CLOSEOUT.md`. That document is preserved byte-for-byte alongside this record. Its reviewer statements remain attributed to the supplied GPT review; this local closeout does not claim to have performed the reviewer's independent checks.

## Accepted mathematical result

On the fixed D0 chiral continuation,

\[
 \nu_+(h,\eta)=
 \frac{\sqrt3(33h^2-240h+688)}{3(1-3h)^3}\eta^3+O(\eta^5),
 \qquad \omega_+=h\nu_+.
\]

The coefficient of eta cubed is twice the normalized coefficient \(c_+(h)\), because the specified oriented Vandermonde equals two. At h zero it is \(688\sqrt3/3\), so the leading common-phase rate survives the mathematical generator limit. The analytic statement is local in eta, with D0's reference framework on \(0\le h\le1/4\).

The accepted finite-root coverage remains only the four specified h values and the reduced eta ladder recorded by D1. It is not extended by this closeout. The reference is a saddle; attraction of the continued states is not established.

In plain language, the complete state can advance by a common complex phase while its intensities, coherence matrix, and existing common-phase-invariant chirality readouts stay fixed. This does not declare common phase a physically unobservable gauge, and does not turn the advance into spatial core rotation or a calibrated physical frequency.

## Review consequences checked within closeout scope

The supplied generator edge identity has the correct sign: pairing opposite orientations gives

\[
 \nu\sum_i r_i^2=
 \frac1{30}\sum_{i<j}(r_i^2-r_j^2)
 \sin3(\theta_j-\theta_i).
\]

This explains how a weighted sum can remain after the unweighted kicks cancel. It is a necessary identity; the full D1 equations, rather than this identity alone, establish the branch and its nonzero rate. The finite-step sine identity remains distinct.

The review's conditional gradient obstruction is valid. If the generator were exactly \(X=-\operatorname{grad}_g V\), with positive-definite g and a differentiable common-phase-invariant V, a nonzero relative equilibrium would give both \(dV(X)=0\) and \(dV(X)=-g(\operatorname{grad}_gV,\operatorname{grad}_gV)<0\). This contradiction excludes that specific pure-gradient representation on a domain containing the nonzero-rate states. It does not classify every other dynamical representation or imply a physical current. No new model or further calculation was begun.

## Evidence received, retained, and not replayed

| Item | Local closeout disposition |
|---|---|
| Supplied review's primary D1 report identity | Matches the local report exactly: SHA-256 `7fa8bb8f61dab09c4f94f0a2227300f94bede4a7651241679e35375d0b8c0737`. |
| D0 evidence | Original report, script, and results retained; recorded **64/64** remains separate. No rerun. |
| D1 evidence | Original report, script, and results retained; recorded **133/133** remains separate. No rerun or expanded certificate audit. |
| Reviewer's independent symbolic substitution and midpoint comparisons | Reported by the supplied review. The four named companion files were not found in a bounded search of Downloads and external research; their execution was not reproduced here. This is not a claim about other locations or archives. |
| Original interval implementation | Available locally as part of D1, but not independently replayed in this closeout. The supplied review expressly limits its certificate assessment to inspection of the reported proof structure. That qualification is preserved. |
| This closeout's own work | Source-identity reconciliation, review of the two displayed algebraic arguments, documentation, and fresh preservation comparisons. No additional mathematical-check count is merged with prior counts. |

The supplied review's SHA-256 is `e62cdc5c72b0b3f9b1359e89c3104d80abec58de07ad168adf7a3140e022bef6`. The accompanying JSON receipt records its original Downloads path, the predecessor file hashes, the actual Git state, and before/after inventories.

## Preservation and stopping boundary

HEAD remains `82cab10cbe550f58c43163fb8b05fabdad1b05ae`, on main. The index was initially empty and remains unchanged. Pre-existing dirty and untracked work remains untouched. All **16,038 protected files** in the six inventoried roots are preserved, including D0, D1, existing temporary material, kernels, UI, papers, fixtures, and historical implementations.

Only this separate external closeout directory was written. It contains the verbatim supplied review, this local record, and `D1_CLOSEOUT_RECEIPT.json`. No predecessor artifact or repository metadata was edited, and no staging, commit, push, cleanup, or publication occurred.

**STOP at the D1 scientific checkpoint.** No D2, broader-ring search, parameter survey, physical reinterpretation, paper revision, or implementation is authorized or started by this closeout. The TL0–TL4 synthesis remains a separate outstanding write-up.
