# Trioctagon Magnetism M3 — joint acceptance record v0.1

**Date:** 4 October 2026  
**Recorded by:** GPT, scientific lead  
**Disposition:** `M3_REPAIRED_ENTRANCE_CAPTURE_JOINTLY_ACCEPTED_WITH_STATED_DOMAIN`

## 1. Decision and source of agreement

The repaired, fixed-parameter entrance-capture theorem is jointly accepted.
Claude's v0.2 review accepts its corrected theorem in sections 3–4. Codex's
reconciliation addendum explicitly accepts that repaired statement, all six
required corrections, and the normalization and phase-parity clarifications.
This record reconciles those assents; it does not introduce a competing equation
set, claim a new proof, or require another round of approval of approvals.

The controlling statement is the Codex addendum's **Accepted statement**, copied
below without scientific alteration. Read it with Claude v0.2 sections 3–4 and
the exact endpoint receipts. The original M3 index-300 capture inference and the
identification of this attractor as the continued M2 branch are superseded, not
retrospectively certified. Original reports, scripts, and logs remain unchanged.

M1 and M2 retain their previously accepted scopes. No M1/M2 result is reopened.

## 2. Accepted fixed-parameter theorem

Fix the exact mathematical parameters

\[
\epsilon=1/20,\quad g=1/5,\quad
k=(1,1.2208964704604097,6.35310346037241),\quad
\lambda=\lambda_c+1/200,
\]

where the decimal entries of k are exact rationals and lambda_c is the exact
M2 critical value derived from its certified positive host. A displayed decimal
approximation to lambda_c is not substituted as a new exact parameter.

The Fourier normalization is

\[
f_1=(1,e^{-2\pi i/3},e^{-4\pi i/3})/\sqrt3,\qquad
\Omega_0=\sqrt3 f_1=(1,-1/2-i\sqrt3/2,-1/2+i\sqrt3/2),
\quad \|\Omega_0\|^2=3.
\]

Write s(z)=u+x+iVy for the M2 slice representative, Q for its common-phase
quotient, Fhat=Q composed with F composed with s, and
H(x,y)=(x,-y). For the exact box U_plus defined by the 80-digit replay's
rational endpoint receipts:

1. The validated trajectory from Omega_0 remains in the smooth nonzero domain
   through entry. Its quotient at index 301 is in the interior of U_plus.
2. Fhat squared maps U_plus strictly into itself and is contractive in the
   weighted maximum norm with certified public bound **q <= 0.9578 < 1**.
   It has a unique fixed point p in U_plus.
3. The additional existence certificate establishes Fhat(p)=H(p). The
   one-step image is disjoint from U_plus, so the orbit has period two rather
   than one.
4. If A=s(p) and B=F(A)=exp(i theta_p) conjugate(A), then F(B)=A. For some
   constant beta, with parity anchored at entry,

   \[
   \Omega_{301+2m}\longrightarrow e^{i\beta}A,\qquad
   \Omega_{302+2m}\longrightarrow e^{i\beta}B.
   \]

   Convergence is geometric per two steps. On this limiting orbit W and
   Gamma are nonzero and reverse sign each step.
5. The conjugate entrance sqrt(3) f2=conjugate(Omega_0) obeys the conjugate
   statement by exact equivariance. No separate trajectory propagation is
   needed to establish it.

**The continuation of this orbit from the M2 bifurcating branch is not
established.** No continuation proof from lambda_c to mu=0.005 was attempted.

### Interpretation of the statement

The index 301 is a certified entry index, not a claim that entry first occurs
there. The contraction bound applies to the two-step quotient map in the
specified weighted maximum norm, not to arbitrary states or a physical time
scale. Approximate printed box coordinates do not replace exact endpoints.

This closes the entrance-entry question for the two specified conjugate,
unit-component endpoints at this one parameter value. It is not a global basin
classification, an assertion about all entrance amplitudes, or a uniform
parameter-range theorem.

## 3. Corrections retained in the accepted record

- **Entry:** use `Fhat(X300) subset X301 subset interior(U_plus)`. Membership
  in an outer enclosure of `Fhat(U_plus)` alone never established capture.
- **Sets:** `E_minus` is an outer image enclosure, not the exact image and not
  an independently established trap. The alternative reflected-trap argument
  is auxiliary; direct index-301 entry is the primary accepted route.
- **Numerical premises:** use certified host/basis/lambda enclosures, exact
  rational endpoint comparisons, interval evaluation at the trap center, and
  the checked recentering points. Approximate centers, weights and
  preconditioners are allowed as explicitly chosen numbers, not exact roots.
- **Contraction and symmetry:** strict two-step self-inclusion plus the
  weighted bound proves the unique two-step fixed point in the trap. A
  separate Krawczyk existence check for `H composed with Fhat minus identity`,
  with preconditioner nonsingularity, proves its H-symmetry. Disjointness
  rules out period one.
- **Entrance normalization:** the main validated entrance has unit component
  moduli and squared norm 3. It is `sqrt(3) f1` with normalized `f1`, not
  `sqrt(3)` times the unnormalized triple. Codex further records that the old
  auxiliary `m3_symmetry_check.py` used squared norm 9; its 401-step log is
  withdrawn as entrance-specific evidence for this theorem. The main
  propagation was correctly normalized, and exact equivariance proves the
  conjugate-entrance conclusion without that auxiliary replay.
- **Phase:** convergence is to one constant common-phase rotation of a full
  two-cycle. The unadjusted accumulated gauge phase need not have a single
  limit across both parity subsequences.
- **Branch identity:** no certified continuation from the M2 local
  bifurcating branch to `mu=0.005` is asserted. That stronger identification
  is not required for this fixed-parameter theorem.

## 4. Evidence and execution attribution

| Evidence | Status |
|---|---|
| Claude v0.2 repaired certificate and theorem | `M3_ACCEPTED_WITH_CORRECTIONS` |
| Codex reconciliation of that repaired theorem | `CODEX_M3_REPAIRED_CAPTURE_ACCEPTED_WITH_STATED_DOMAIN` |
| Claude interval script replayed by Codex | 28/28 supplied verdicts at 80 interval digits |
| Codex supplementary predicates | 23/23; reuse Claude's interval engine, not a separately implemented propagation |
| Separately formulated nominal calculation replayed by Codex | 2/2 membership predicates; numerical consistency, not interval proof |
| GPT preceding repair review | Reviewed and replayed Claude's repaired code in the preceding turn; not newly executed by this record |
| GPT current closeout | Delivery hashes/manifests, matching report bytes, and exact Fraction comparisons of selected supplied endpoint decisions |

The three check counts are not added into a total of independent proofs.
The supplied 60/80/120-digit records are robustness evidence. Codex reports only
an 80-digit replay in this reconciliation; this closeout repeats none of those
propagation or nominal calculations.

The current GPT endpoint audit separately confirms strict direct entry,
self-inclusion, the Krawczyk-box inclusion, positive weights, disjointness, and
that all supplied weighted row bounds lie below the exact rational
`4789/5000 = 0.9578`. It checks recorded enclosure decisions, not their full
construction. Its receipt explicitly documents that the stored reflected box
is very slightly outward-rounded; the step-300 enclosure is also strictly
inside the exact reflection of the stored trap endpoints. This introduces no
new hypothesis or correction to the direct-entry theorem.

## 5. Frozen review identities

| Artifact | SHA-256 |
|---|---|
| Codex complete reconciliation package | `0a9ad7c4660a93f1a8611673a0cc2dfe7991679c0e684b8e7604a51849301b58` |
| Codex reconciliation addendum | `67d2f1b5a28b0900ca94fc5fa4cd7f72f3aaeed88b12658f5a6808cc91363a73` |
| Claude v0.2 review within the package | `2c600f8ad84e3325f9671479a5e4a9b68734b26a2f63685e3cd9f45f6c6572b0` |
| Claude v0.2 checks ZIP within the package | `9dabd9c87b4934fe1349db006934d2aa864b3f9a075b8557cb438e88f3f592b6` |
| Repaired interval script | `f00b6bc62a47d6aac88d32215a9361d2be77dc67903db5945a8c0740245be27e` |
| Codex support-result JSON containing exact endpoint receipts | `10c4f505f11f1c85c87e3a91e76f61c36e2119a023b13d6dc26af77f9289ddb3` |
| Accepted M2 interval input JSON present in this package | `6fe4f3f314db1332712b31fed8f7a64cfcee892b9c07782018ea38d3749444a8` |

The exact definition of `U_plus` is
`codex_m3_support_checks.json -> values -> exact_receipts -> Up`, with norm
weights in `positive_weights`. This file is inside the preserved reconciliation
ZIP. Other exact receipts include `q301`, `Zw`, `Kr`, `lambda_c`, and
`lambda_parameter`. Historical `Um` in JSON denotes the outer enclosure
`E_minus` in the accepted prose; it is not equality with the exact image.

The M2 joint-record hash reported and verified by Codex is
`17087119faf01256aea8c8673dacdfaf9c842eeaddedd2440ef958ad1c4537ce`.
That record is an inherited accepted premise. Its file bytes are not included
in this delivery and were not newly hashed in this GPT closeout. The M2
certificate input JSON used by the repaired calculations is included and was
verified here.

The scientific source baseline is `64ddea159e0e69888926aa21fa281e42f5dd50b4`
as recorded by both reviewers. This is not a new observation of remote or
Windows HEAD. Repository and original-file preservation claims remain
attributed to Codex's closeout receipts; no repository was accessed in this
GPT closeout.

## 6. Limits and implementation decision

**Not established by M3:** continuation from the M2 branch; a connection to the
`lambda=0.5` orbit; other entrance amplitudes or general perturbation basins;
a range of phase strengths; ring dynamics; physical magnetic fields, units,
Maxwell laws or a dynamo; guaranteed binary64 runtime behavior.

**Mathematical acceptance is not implementation or publication authorization.**
No kernel, scientific application, UI, paper, TORMENT, Historical kernel,
database, service, or repository file is changed or authorized by this record.
X01 remains unadopted. No M4 or continuation investigation is opened.

M3 review is complete for the repaired fixed-parameter theorem. Retain the
source ZIP intact alongside this record; do not regenerate original evidence
or overwrite earlier reports to make the historical chain appear error-free.

## 7. Contents and reproducibility of this closeout

The compact closeout packet contains this record, the original Codex ZIP
unchanged (which already contains Claude's review and check bundle), a GPT
integrity/endpoint receipt, and its standard-library verification script.
It does not duplicate earlier M1/M2 archive trees or add a new scientific engine.

To repeat only the closeout verification from the extracted packet root:

```text
python verification/verify_m3_delivery.py evidence/TRIOCTAGON_MAGNETISM_M3_CODEX_RECONCILIATION_v0.1.zip
```

This command verifies hashes and supplied rational-endpoint comparisons. It
does not rerun the interval or nominal trajectory, or access any repository.
The optional second argument is the separately supplied Codex addendum when
verifying that copy against the ZIP. See the preserved source package for the
original mathematical replay commands and their environment requirements.
