# GPT numerical-audit closure — Central Geometry, Z Readouts, and Chiral Response v0.2

20 October 2026 · Review of the delivered standalone numerical audit · No manuscript or repository edits

## Verdict

**ACCEPTED WITHIN SCOPED IDEAL REAL/COMPLEX MATHEMATICS. The required numerical-verification obligations in the authorized audit work order are closed. No new scientific correction is required by this review.**

E01–E06 remain closed. This receipt accepts the numerical evidence supporting the corrected local manuscript v0.2. It does not approve the author-attributed paragraph, authorize publication, or claim verification of production floating-point execution.

This disposition is based on inspection of the supplied implementation and its proof structure, a successful unmodified portable replay, and exact comparison of the regenerated evidence. It is not an independent human assessment, a third independently written scientific evaluator, or formal proof-assistant verification.

## 1. Delivered identities and preservation

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Numerical-audit review ZIP | 419520 | `959aff5caf6b617565e1b059035f5254046a39bdd93c875706008978a869e90b` |
| Numerical-audit report | 26922 | `877b97fcb51a1b3abf9dc4d6cdb8168ef7a6c153eecba10d5b240aa676765d60` |
| Accepted manuscript v0.2 review ZIP | 595068 | `37674d5df58596749855fc8d4c33c77e262e7b926ce2e7528c4dcec1b3b2a38c` |
| Accepted v0.2 TeX | 86681 | `02610193c2aebdf8b97b424f1837696dff79feb1f3079e038a0385dc4863640b` |
| Accepted v0.2 PDF | 364084 | `f0b323bae4f552ee385e6a32f812c1842d88dc26423d129bcff2e74b7b332288` |
| Accepted v0.2 disposition | 4940 | `ea7b5297d0fbf52a842d55ca1155776f083dc129a24273222e3742fb07931a9d` |

The delivered audit archive has 44 members: 43 manifest-listed payloads plus the hash manifest. Every listed payload's byte count and SHA-256 match; there are no unexpected members. The separately uploaded report is identical to its bundled copy.

All 27 copied inputs match the audit input manifest. The six copied manuscript-review documents match the accepted v0.2 ZIP, and all ten retained R0–R9 reports match the earlier uploaded originals. All 37 scientific source identity records agree with the accepted manuscript manifest. The latter is a comparison of recorded identities, not a new fetch of all 37 Windows originals.

The delivered extraction was preserved. Replay occurred in a separate copy. Its four checker files and copied inputs remain byte-identical to delivery. No manuscript, prior report, accepted publication or project code was edited or executed.

## 2. Review performed

Inspected `rigorous.py`, `audit.py`, `supplement.py` and `verification.py`, with emphasis on the following load-bearing points:

- Closed rational intervals on the `10^-60` grid use outward integer floor/ceiling for conversion, multiplication and division. Square roots use integer square-root inequalities. Denominators containing zero and ambiguous phase rectangles are rejected.
- Machin's identity, arctangent reductions, trigonometric range reductions/extrema, and exponential Taylor sums retain explicit remainder allowances. The interval calculations do not use the nominal mpmath values as premises.
- The exact original initial-state formulas are evaluated before adding the twelve-coordinate input box. Rounded comparison vectors remain proof-enclosure centres, not replacement initial or evolving states.
- The full polynomial map and simultaneous phase synchronization agree with the supplied source definitions. Nonzero domains are established before divisions and phase-sensitivity estimates. Native evolution does not receive an observer time step or a geometric feedback term.
- Both the direct interval composition and the inherited comparison-residual/sensitivity induction are evaluated. Repeated coefficient intervals conservatively enclose the correlated fixed-configuration composition; the mathematical input problem is not changed to independently selected later coefficients.
- The two phase-domain proofs cover all 64 closed rational cells in each phase rectangle, retaining the full amplitude and coefficient intervals in every cell. This is set-valued interval coverage, not a grid of point samples.
- Finite-region conclusions use the relevant actual-section bounds, including the first-interior lower bound and the fourth-observation finite-edge wedge/support checks.
- Interval overlap with zero is treated as an arithmetic consistency check, not proof of equality. Supporting algebraic identities are handled separately by exact reductions and the stated mathematical arguments.

The four-update horizon, original box radius, unequal reference coefficients, fixed geometry, placement and observer schedule remain unchanged. No fifth update or new research result was added.

## 3. Unmodified replay

Executed `python -B audit.py` in an isolated copy using the existing Linux Python 3.13.5 environment, with SymPy 1.14.0 and mpmath 1.3.0. No packages were installed. Bytecode writes were disabled and temporary/cache paths were confined to the replay workspace.

Codex's delivered run used Windows Python 3.11.15 with the same SymPy and mpmath versions. The portable replay exited **0** with `PASS_WITHIN_SCOPED_IDEAL_MATHEMATICS`.

| Numerical proof block | Scalar bound records | Replay disposition |
|---|---:|---|
| A_START — exact witness and initial inclusion | 26 | PASS |
| A_CHAIN — residuals, domains, sensitivities and recurrences | 301 | PASS |
| B_OBSERVATIONS — readouts, finite geometry and distances | 150 | PASS |
| C_MECHANISM — norm, chirality, existing direction bounds and attribution | 208 | PASS |
| D_THEOREMS — complete closed phase/amplitude domains | 34 | PASS |
| D_APPLICATION — actual-image inclusion and polynomial supply | 49 | PASS |
| **Total** | **768** | **All pass** |

The 58 arithmetic self-checks and eight exact supporting-identity checks also pass. These are separate counts; the 768 records are not 768 independent theorems.

## 4. Exact evidence comparison

All 768 scalar records agree exactly with the delivered results, including their rational interval endpoints, stated bounds, margins, source hashes, dependencies and statuses. There are 731 `VERIFIED_RIGOROUS` and 37 `VERIFIED_EXACT` scalar records, with no failed, unresolved or source-blocked numerical item.

A separate review helper reparsed every obtained bound and claimed bound as Python `Fraction` values. It checked strict/non-strict containment and recomputed each recorded minimum endpoint margin. All 768 pass this additional record-level consistency check. This checks the saved certificates; it is not a substitute for the interval-code review or a fresh derivation of each scientific claim.

The original input-box specification, whole-box observations, direct nominal/box/raw-stage enclosure file, arithmetic self-checks, exact-identity checks, coverage rows and 120-digit nominal corroboration also match the delivered evidence exactly as structured data.

The only top-level result differences are environment metadata, original-path availability before/after replay, and the corresponding source-preservation status. All 27 copied inputs were available and matched. Original Windows paths were unavailable on this host, so the replay correctly reports `VERIFIED_EXACT_COPIES_ORIGINAL_PRESERVATION_UNAVAILABLE`. Its console's `original input identities before/after: False` denotes that availability limitation, not a hash mismatch or a failed numerical test. The live Windows repository and its preservation status were not independently re-inspected here.

## 5. What the audit now supports

The four scheduled observations retain the certified **inside, outside, outside, outside** band sequence, with all four inside the host and central slab. The first native-only attribution endpoint remains outside. The stated signed heights, distances, norm budgets, chiral-magnitude changes, existing directional inequalities and observer attribution are supported by the replayed whole-box bounds.

For the full closed phase/amplitude products, the outward display hulls for the squared-chiral response are:

- Third domain: `[0.00038225851403, 0.00045739302538]`, strictly above the claimed `0.00034` gain.
- Fourth domain: `[-0.00324272106279, -0.00258815011647]`, strictly below the claimed `-0.00248` response.

The separate inclusion of the actual third/fourth pre-sync images is checked as well. The abstract phase-domain theorems do not depend on every point of those larger products being reachable.

The coverage table accounts for all 37 accepted manuscript claim IDs: 14 quantitative rows are checked within scope, six are checked only as supporting definitions/identities, and 17 are outside this numerical audit. No claim is made that all 37 full statements were newly proved by execution.

## 6. Remaining boundaries and next editorial step

The previously unresolved projection/direction comparisons remain unresolved for the manuscript; this audit was not permission to promote additional conclusions from tighter enclosures. The result does not certify production binary64 execution, long-time dynamics, an invariant region, physical flow, crystal movement or a physical geometry-to-dynamics coupling.

Confidence remains conditional on the inspectable interval implementation, Python's integer/Fraction arithmetic, the analytic identities/remainder bounds, and correct source transcription. Successful replay and code review do not constitute formal verification.

The original manuscripts remain accurate historical records of what was verified when they were written. The appropriate next document-only step is to prepare a separately versioned final-review copy that cites this audit and updates its previously pending numerical-verification status. Preserve v0.2, the research reports and the complete delivered audit unchanged. There is no new scientific correction or further trajectory investigation required by this review.

Hilmir's author-wording approval and a publication decision remain separate. This receipt does not grant either, does not issue a repository-write order, and does not launch the next task.

## Review evidence

The companion GPT replay-evidence ZIP contains the regenerated result files, console log and exit code, exact-comparison receipt, artifact/hash checks, comparison helper and unmodified checker copies. The original audit bundle supplies the hash-bound input texts and portable replay instructions. The evidence package documents this completed replay; it does not replace Codex's preserved delivery.
