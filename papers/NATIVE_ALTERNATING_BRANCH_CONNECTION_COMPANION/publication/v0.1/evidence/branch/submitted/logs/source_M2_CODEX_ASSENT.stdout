# Trioctagon Magnetism M2 — Codex review and acceptance addendum v0.1

Date: 2 October 2026

Status: **CODEX_ACCEPTED_WITH_STATED_SCOPE; M2_JOINT_ACCEPTANCE_RECORD_PENDING**

I reviewed the M2 brief, the accepted M1 record, GPT’s independent M2 review and sign certificate, Claude’s actual certificate attack/correction addendum, the supplied scripts/results, and the new bounded checks. I accept the proposed local nonlinear-persistence result and the sign certificate within the exact scope below. This addendum does not itself create a joint acceptance record.

The accepted M1 reference is `TRIOCTAGON_MAGNETISM_M1_COMMON_EQUATIONS_CANDIDATE_v0.2.md`, SHA-256 `a14e5a108dc49c6f0c75950747567132993bd47b2d12ff7ee69d689a52768ef6`. M1 remains closed and unchanged.

## Reviewed evidence

The exact supplied GPT review artifacts are:

- `GPT_M2_REVIEW_AND_SIGN_CERTIFICATE_v0.1.md`: `f0522d1c8bdac39c067b50b5b9990519ff9935f7f31fb58c6d9ab6283eeb58b8`
- `new_checks/gpt_m2_analytic_interval_review.py`: `6d71fd50ed243a4f3f99403a5ba20cbf129f5c1f92cf30ab13f1cec1b0d84d02`
- its supplied result JSON: `6fe4f3f314db1332712b31fed8f7a64cfcee892b9c07782018ea38d3749444a8`
- `new_checks/gpt_m2_cross_checks.py`: `08efe68f97e88ef04a24325a9b9e63c2b0710a9c7cfc9e8c3213295086bd0a1b`
- its supplied result JSON: `283ea7c082326788cdcfce8e5019e8f90343b0a78c3d7c0e7bc1ce96a3f78bb7`

Claude’s reviewed correction addendum is `TRIOCTAGON_MAGNETISM_M2_CLAUDE_REVIEW_ADDENDUM_v0.1.md`, SHA-256 `86408b49d33b1307ff3bfb297ebd75a8a4a043435e1a364c68ec5d87e0ddbe00`. Its supplied attack-check archive is `CLAUDE_M2_REVIEW_CHECKS.zip`, SHA-256 `5a6379acc99707be27d6ed0b289db3f6cb37bad76d7a94e7378e25a513cfcb36`. The original Claude script and result hashes remain `43004da1dc7c1eac27912e3a8688a312a24da7ac0d84ddb12444263c6b44d80e` and `2fe2f35006f79ee6a3c97ee6e8063c5d47c6a3c0125fd72abafcbe5790d98fd8`.

The GPT and original-Claude hashes were checked against their supplied manifests; the Claude response hashes were checked against the supplied response files and archive. Original Claude files were not edited or replayed as evidence for this review.

## Mathematical verdict

I accept the interval certificate

`0.0865248497217 < c < 0.0865248497219`

for the exact decimal-rational parameter model

`epsilon=1/20`, `g=1/5`, `k=(1, 1.2208964704604097, 6.35310346037241)`.

The certificate’s enclosure chain is adequate: exact rational conversion, outward-rounded dyadic interval operations, Krawczyk inclusion for the positive host, recomputed interval basis/eigenvector data over the host box, interval inverse for the slaved real block, and interval evaluation of the third-order jet. Claude’s 7/7 adversarial checks specifically confirmed the cubic amplitude expansion, interval reciprocal/square-root/power behavior, Jet algebra, normal-form projection convention, and the enclosed crossing. GPT’s supplied cross-checks pass 21/21.

My independent direct-map calculation, written separately and not importing either review script or the repository, gives:

```text
m1       = 0.43340935089637667115981438670293127293968082167…
m2       = 0.33313215453616457537477802867833809950125889590…
lambda_c = 0.36747639460421353654937599160194557765099621470…
sigma    = 3.90068415806739004043832948032638145645712739504…
direct c = 0.08652484972178753847335349360894814355568800721…
```

This independent value agrees with the interval certificate and with the supplied direct/slaved split. It also gives `W_q=(3.17358673166478867…, 1.94734707082316243…, 0)` and `|W_q|=3.72341420710110443…`, so W detects the critical mode at first order.

The quotient compression is exact on the stated local positive chart:

`B(lambda)=(1-9 lambda) V^T M(u) V`.

The unequal-k host therefore has a simple transversal `-1` crossing at `lambda_c`; the other quotient imaginary multiplier is `-m2/m1`, while the real block is strictly inside the unit disk in the certified host box.

## Corrections adopted

The amplitude substep is nonlinear. Its common-phase covariance follows from `A(Omega)=M(|Omega|^2)Omega`, where the real state-dependent matrix depends only on intensities. It is not real-linear in Omega.

In the H-odd center coordinate, the local scalar law is odd:

`a_next=-(1+sigma*mu)a+c a^3+O(a^5+|mu|a^3+mu^2|a|)`.

For `c>0`, the local branch is on `mu>0` and

`a^2=sigma*mu/c+O(mu^2)`.

The multiplier of the second iterate **at the emerging cycle** is

`1-4 sigma mu+O(mu^2)`.

The different `1+2 sigma mu+O(mu^2)` expression belongs to the second iterate at the still-existing fixed point, not to the new cycle. The direct numerical witnesses approach the factor four.

The H-reflected quotient cycle lifts to a full complex period-two orbit: the two common-phase increments cancel. Common-phase rotations form a neutral family, so attraction is orbital/modulo common phase. W and Gamma reverse sign at the two points and have zero two-step mean. This is alternating mathematical persistence of the geometry-attached observable, not a stationary electromagnetic field.

## Limits retained

The result is local. It supplies no certified neighborhood radius or explicit interval of admissible positive `mu`; those remain ordinary local bifurcation-theorem existence statements after the nondegenerate hypotheses are certified. It supplies no entrance-basin theorem. The accepted `sqrt(3) f_1` and conjugate `sqrt(3) f_2` endpoint trajectories are parameterized numerical illustrations only. It does not connect the local branch to the remote `lambda=0.5` orbit, establish a global persistence threshold, or cover other amplitudes, branches, initial conditions, the equal-k double crossing, the ring, X01, or physical magnetism.

No new dynamics, normalization, forcing, state, feedback, ring extension, implementation, repository test, paper, UI, production TORMENT, Historical TORMENT, database, service or model system was changed. The current physics repository remained at HEAD `64ddea159e0e69888926aa21fa281e42f5dd50b4`; its tracked worktree was clean and `kernel_physics/dynamics.py` retained SHA-256 `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4`.

The independent Codex check source is `codex_m2_independent_checks.py` (SHA-256 `5ff5471c56ba573fa1b3145381dd1253c5f8dbdce094afeeaef5c8457d4478ba`) with its result JSON alongside it. It passed seven bounded checks: host residual, simple spectral gap, crossing sign, normalized/transverse critical direction, independent positive cubic coefficient, and nonzero W projection. The supplied GPT analytic script and cross-check script were also rerun externally; the cross-check summary was 21/21. These runs used conda environment `torment`, Python 3.11.15, mpmath 1.3.0 on Windows; they are independent mathematical checks, not byte-for-byte claims about Claude’s original runtime.

**Codex disposition:** no specific objection. The M2 local flip result and the positive sign certificate are accepted with the stated domains and evidence strength. A lead-authored M2 joint acceptance record may now reconcile this assent with Claude’s certificate acceptance; no implementation follows.
