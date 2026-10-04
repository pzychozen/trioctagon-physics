# M3 corrected certificate — Codex reconciliation addendum v0.1

Date: 4 October 2026. External mathematical review only.

**Disposition: `CODEX_M3_REPAIRED_CAPTURE_ACCEPTED_WITH_STATED_DOMAIN`.**

I accept the repaired fixed-parameter capture theorem below. I withdraw the
original v0.1 inference that membership at index 300 in an outer image box
established capture. My earlier certification statement was not justified by
that argument. This addendum supersedes that inference and the asserted M2
branch identification; all original files remain unchanged.

This is Codex's assent to Claude v0.2 sections 1–4 as clarified by the work
order. It is not a declaration of joint M3 acceptance; GPT retains that
reconciliation decision. M1 and M2 are accepted premises, not reopened here.

## Accepted statement

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

## Explicit verdicts on Claude's six required corrections

| Correction | Verdict | Reason |
|---|---|---|
| 1. Replace the index-300 capture inference by direct index-301 entry | ACCEPT | The repaired enclosure chain is Fhat(X300) subset X301 subset interior(U_plus). Exact endpoint comparisons pass. X300 subset interior(H(U_plus)) also passes as an alternative consistency check. |
| 2. Rename the outer image box | ACCEPT | Use E_minus, with Fhat(U_plus) subset E_minus. Neither equality nor surjectivity onto E_minus is established. The tested enclosure of Fhat(E_minus) fails inclusion in U_plus; this is not evidence that its exact image escapes. |
| 3. State the Banach theorem | ACCEPT | U_plus is closed, convex and complete in the weighted norm. Valid chart bounds give C1 regularity on a neighborhood of the relevant compact boxes. Strict self-inclusion and the interval derivative bound prove contraction; disjointness excludes period one. |
| 4. Replace point-valued proof premises | ACCEPT | Exact dyadic endpoints/Fractions decide containment and norm inequalities. Certified host, interval-derived basis and lambda_c, interval Fhat squared at the center, and checked centers replace the missing premises. Approximate centers, weights and preconditioners are legitimate fixed choices. |
| 5. Certify H-symmetry | ACCEPT | A strict Krawczyk inclusion for H composed with Fhat minus identity proves existence in U_plus. The additional inverse-defect bound verifies the preconditioner's nonsingularity. Banach uniqueness then identifies that solution with p. Symmetry alone would not suffice. |
| 6. Withdraw the M2-branch identification | ACCEPT | The theorem certifies the H-symmetric attracting period-two orbit in U_plus at the stated parameter. M2's sufficiently-small-mu theorem does not certify an interval reaching 0.005. |

**Theorem verdict: ACCEPT with the exact statement above.** Normalization,
phase-parity wording and interval-set notation clarify Claude's proposed
fixed-parameter theorem without changing its central repaired result. They
do not rescue the original proof as written. No remaining contradiction
requires another broad review round.

## Proof dependencies checked

The replay uses the same fixed host u throughout. Its accepted M2 Krawczyk
image encloses u and lies strictly inside the accepted host box. V(u),
V transpose M(u) V, its larger eigenvalue, and lambda_c are then enclosed
with interval arithmetic from that host. Widening dependencies during separate
evaluations is conservative: all evaluations include these same exact objects.
No nominal Newton root is used as a proof premise in the repaired propagation.

For every centered step, X is convex and contains the chosen center c, so
F(X) is contained in F(c)+DF(X)(X-c). The full trajectory uses 21 six-real
updates, followed by 279 quotient updates to X300 and one quotient update to
X301. **All 301 recenterings are checked**, including the last added step.

The following are decimal displays of checked enclosures, not decision
endpoints. Exact rational endpoints of U_plus, E_minus, H(U_plus), X300,
X301, the two-step image, Krawczyk image, center evaluation, host, basis,
lambda and weights are in `codex_m3_support_checks.json`.

| Certificate quantity | Observed display |
|---|---:|
| Full-state pre-sync radius minimum, updates 0–20 | 0.04221212242796385935136318 |
| Gauge conversion at index 21: lower bound for abs(u dot Omega21) squared | 56.9093923896302 |
| Quotient pre-sync real-part lower bound, indices 21–300 | 1.3096147241289281421 |
| Quotient gauge denominator lower bound | 7.7839261785287128809 |
| Quotient pre-sync radius lower bound | 1.3132035799719558266 |
| Maximum X300 coordinate width | 4.5654299e-57 |
| X301 maximum center offset / selected radius | 0.01458363717 |
| Maximum weighted two-step derivative row bound | 0.9577986865078347887356682 |
| Smallest strict two-step interior margin | 4.635684939e-7 |
| Trap pre-sync real-part lower bound | 1.5046726819698976568 |
| Trap gauge denominator lower bound | 8.8698230520473262805 |
| Trap pre-sync radius lower bound | 1.5073367430120650397 |
| Corrected separating gap, coordinate 5 | 0.8743092026060967745791934 |
| Weighted inverse-defect bound for Krawczyk preconditioner | 0.1101944217046150427755617 |

The weights are the positive dyadics selected by the supplied 80-digit run,
displayed approximately as
(3.5322590088879646e-5, 3.6441896819931174e-5, 4.2514894042419980e-5,
1.0984693497410257e-5, 1e-4). The exact definition of the box and weights is
the rational receipt, not rounded digits in this addendum.

In the trap, let J1 enclose DFhat(U_plus) and J2 enclose DFhat(E_minus).
J2 J1 encloses the two-step derivative. The maximum of the exact weighted
row bounds is strictly below the rational 0.9578. The interval center value
Fhat(Fhat(c)) and this matrix produce strict self-inclusion. A scalar equality
between a rounded point evaluation and the exact center value is unnecessary.

For R(z)=H Fhat(z)-z, the chosen approximate inverse Y is enclosed as a fixed
matrix. The interval bound on I-Y DR over U_plus has weighted norm below 1,
which ensures Y is nonsingular. The strict Krawczyk inclusion therefore
certifies a zero z* of R in U_plus. H-equivariance makes z* a fixed point of
Fhat squared, and uniqueness in U_plus gives z*=p. This is an existence
argument, not reliance on the tiny nominal cycle residual.

## Full-state phase and observable qualifications

Common-phase covariance and conjugation equivariance imply
F(s(p))=exp(i theta_p) conjugate(s(p)) and F squared(s(p))=s(p).
The nonzero pre-sync and gauge bounds justify the local smooth formulas;
the chosen ratio-atan branch has positive denominators. The full phase map
itself is smooth away from zero because its final expressions are periodic
in the arguments. Principal-argument cut avoidance is also checked along
the initial interval boxes.

Let alpha_n be the accumulated phase removed to obtain the slice, and let
theta(z) be the one-step gauge increment. Then
alpha_(n+2)-alpha_n=theta(z_n)+theta(Fhat(z_n)). This smooth function vanishes
at p and at H(p). Geometric quotient convergence makes these increments
summable separately on the two parity subsequences. Consequently
alpha_(301+2m) tends to beta and alpha_(302+2m) tends to beta+theta_p, modulo
2 pi. It does **not** follow that the entire raw alpha_n sequence has a
single limit. Factoring the intrinsic theta_p into B gives the single
constant rotation of the full two-cycle stated above. There is no physical
time-reversal interpretation.

W and Gamma are invariant under common-phase rotation and odd under
conjugation. The supplementary interval ranges over U_plus exclude zero:
W_x is approximately [1.33420545,1.33511621], W_y approximately
[0.81817883,0.81892114], W_z=0, and Gamma approximately
[-0.01779195,-0.01645262]. These displayed intervals are explanatory;
the exact receipts and sign predicates supply the nonzero conclusions.

One further historical reporting correction is necessary. The original
**main** nominal and validated-entry scripts used the correct unit-component
entrance. But `m3_symmetry_check.py` defined f1 as the unnormalized triple
and then multiplied it by sqrt(3), giving norm squared 9. Its old 401-step
record is therefore not entrance-specific evidence for this theorem. I
withdraw that attribution, preserve the script and log unchanged, and use
the exact conjugation argument above. This affects ancillary evidence, not
the repaired theorem or its correctly normalized propagation; no different
entrance was rerun here.

## Bounded replay and independent assessment

I inspected the complete repaired code before running it, including the
cubic amplitude map, simultaneous harmonic-three update, AD rules,
mean-value enclosures, quotient chart, two-step derivative composition and
Krawczyk operator. The source implements the accepted map. In particular,
arg derivatives use (x dy-y dx)/(x squared+y squared), and the quotient
ratio-atan formulas assert the required positive denominators.

The execution evidence is attributed as follows:

- **Claude's unchanged interval script, replayed by Codex at 80 interval
  digits / 90 point digits:** 28/28 check verdicts. All values and exact
  X300/X301 rational endpoint strings match the supplied 80-digit record.
  These are 28 verdicts, including documentary consistency checks, not
  28 independent mathematical proofs.
- **New Codex support predicates over that replay:** 23/23. These audit exact
  entry, self-inclusion, the outward public contraction bound, preconditioner
  nonsingularity, Krawczyk inclusion, chart and slice positivity, corrected
  disjointness, observable signs, and an inward-rounded string-endpoint
  witness. They reuse Claude's interval engine; they are not an independently
  implemented trajectory certificate. Mathematical assent also rests on
  the source and theorem reasoning given above.
- **Claude's separately implemented 130-digit nominal formulation, replayed
  by Codex:** both X300 and X301 membership checks pass. This is numerical
  consistency evidence only, not an interval proof.
- **Supplied 60/80/120-digit records:** the script hash and all verdicts
  agree. Only 80 digits was replayed here; endpoint bytes across different
  precisions are not required to agree.

The original disjointness Boolean was valid; its displayed gap expression
used min where max was needed to choose the separating orientation. The new
diagnostic is max over i of max(lower(E_i)-upper(U_i),
lower(U_i)-upper(E_i)). It gives the positive coordinate-5 gap above. Original
source labels remain verbatim in the replay, including a label writing
`Fhat(qbox_300) = qbox_301`; the actual calculation and this addendum mean
**inclusion**. No label is used as a mathematical premise.

Commands were run in Command Prompt with conda `torment`:

```bat
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
python -I -B -X utf8 verify_intake.py
python -I -B -X utf8 codex_m3_support_checks.py > codex_m3_support_checks.log 2>&1
cd replay
python -I -B -X utf8 m3_nominal_crosscheck_v0_2.py m3_claude_review_v0_2_results.json > nominal_replay.log 2>&1
```

The support wrapper uses `runpy` to execute an unchanged COPY of
`m3_claude_review_v0_2.py` with arguments
`INPUT_gpt_m2_analytic_interval_review.json INPUT_codex_m3_validated_entry.json 80`.
Its stdout is in `replay/interval_replay.log`. All outputs land in this new
directory. Runtime: Windows, Python 3.11.15, mpmath 1.3.0. Output-file hashes
can differ from the supplied Linux records through version metadata and
newline serialization; comparisons above concern parsed values and exact
rational endpoint strings.

## Identities and preservation

All 11 outer-packet manifest entries, all 14 Claude archive manifest entries,
and all 17 original Codex archive entries verified. The supplied original
Codex input is byte-identical to the original archive's validated-entry JSON.
The M2 input is byte-identical to
`M2_GPT_REVIEW/new_checks/gpt_m2_analytic_interval_review.json` in the earlier
M2 GPT review ZIP. Its accepted record hash was verified without reopening
M2 scientific conclusions.

| Input / script | SHA-256 |
|---|---|
| Correction packet | `78594b315c3301c3d8daa0470c660bc912ce34c31e365c108717c8d54ef2c524` |
| Original Codex M3 ZIP | `dc3a6137db4c6bd6bd013ca3612379e3be8e7dad03b1e2de3e938ce6deff79bf` |
| Original Codex M3 report | `a59c914c307e2660f154472a8ae6eabaed8316df737cbcb06cb11a69e8cad26f` |
| Claude v0.2 report | `2c600f8ad84e3325f9671479a5e4a9b68734b26a2f63685e3cd9f45f6c6572b0` |
| Claude v0.2 archive | `9dabd9c87b4934fe1349db006934d2aa864b3f9a075b8557cb438e88f3f592b6` |
| Replayed Claude interval script | `f00b6bc62a47d6aac88d32215a9361d2be77dc67903db5945a8c0740245be27e` |
| Replayed Claude nominal script | `6c18f1a6b1aab549e053439e54cbdacd8cd7722d07b891ca5b99d3f417d641ab` |
| New Codex supporting script | `c79215a8b26e3399c322f78f9b862e11a379222ca79509ecc21cd2aea1853161` |
| Original Codex input JSON | `c4e1e5fc191e4aafddac8d1155bac0f3e3ffec08d02323d0a0f5e5c9b9c95361` |
| Accepted M2 input JSON | `6fe4f3f314db1332712b31fed8f7a64cfcee892b9c07782018ea38d3749444a8` |
| M2 joint acceptance record | `17087119faf01256aea8c8673dacdfaf9c842eeaddedd2440ef958ad1c4537ce` |

The intake snapshot and final preservation receipt compare all 62 captured
input/original files byte-for-byte. Historical Codex files, supplied reviews
and authority copies are unchanged. The repository remains at
`64ddea159e0e69888926aa21fa281e42f5dd50b4`, with no staged or unstaged tracked
diff and the same pre-existing untracked list. No repository or production
files were written.

The report's own hash, supporting output hashes and all delivered-file hashes
are recorded in `SHA256SUMS.txt`; `closeout_receipt.json` records preservation
and parsed-result comparisons. The ZIP's hash is supplied with delivery.

The sole retained branch-identity qualification is exact: **M2-branch
continuation is not established.** No kernel integration, publication, X01,
new dynamics, other parameter study, ring work, TORMENT work or M4 was done.
