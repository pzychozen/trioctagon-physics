# Paper A — Proof Audit v0.3
Companion to `PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.3.md` (freeze candidate). Carries the v0.2 audit (analytic proof vs finite regression) unchanged in substance; the v0.3 spot-check corrections are wording/scope (F01, F09, F11, F14) and the publication-script root (F15) — no audit result changed. **Distinguishes ANALYTIC PROOF from NUMERICAL/FINITE CORROBORATION.** The finite scripts are regression evidence; they do not "prove" the general theorems.

**v0.3 note (F15).** The publication reduction script `paperA_reduction_check.py` now derives the project root via `Path(__file__).resolve().parents[2]` (with an optional `--root`/`PAPER_A_ROOT` override) and reports kernel_TO `.pyc` files **created** by the run via a before/after inventory, rather than assuming a container path or counting existing files. The pure-math audit script `paperA_proof_audit_v0_2.py` imports nothing and is unchanged (20/20).

## A. Provenance of the proofs (analytic, not enumerative)

| Result | Proof status | Where |
|---|---|---|
| $\Delta_M P=P\Delta_d\iff d\mid M$ | **ANALYTIC PROOF** (incidence/boundary-row) | manuscript §3(i); referee P01/P02 |
| Invariance classification: $V_d=\operatorname{im}P$ invariant $\iff d\mid M$ or $(3,2)$ (range $1\le d\le M$) | **ANALYTIC PROOF** (boundary-row cases) | §3(ii); referee P02 |
| $Q^\ast\Delta_M Q=\Delta_d$, $P^\ast\Delta_M P=q\Delta_d$ | **ANALYTIC PROOF** | §3(iii) |
| Fourier $V_3=\{e_0,e_4,e_8\}$, spectra | **ANALYTIC PROOF** | §5; referee P04 |
| $C_{12}\to C_3$ covering, deck $\mathbb Z_4$, quotient | **ANALYTIC PROOF** | §4; referee P03 |
| $F_M(P\Omega)=P F_3(\Omega)$ for every $3\mid M$ | **ANALYTIC PROOF** (modular identity 6.2) | §6.2; referee P05 |
| Real decomposition $U_0\oplus U_2\oplus U_{13}$ | **ANALYTIC PROOF** (equivariance + projectors) | §7.1; referee P06 |
| Feedback Corollary 3 (sufficient) | **ANALYTIC PROOF** | §10 |
| Representative $\rho_\perp$, $g_\ast$, perturbation rates | **NUMERICAL** (independently reproduced) | §7–§8; referee reproduction |

## B. Regression audit (`paperA_proof_audit_v0_2.py`) — 20/20 PASS

Pure math, no implementation import. **Corroborates** the analytic proofs above; does not replace them.

| Block | Statement | Result |
|---|---|---|
| A | intertwining exact for all $d\mid M\le90$ (425 pairs) | max err 0.0 — PASS |
| B | intertwining fails for every non-divisor $2\le d<M\le60$ | PASS |
| C | **invariance via $(I-PP^{+})\Delta_M P=0$** matches "$d\mid M$ or $(3,2)$", $1\le d\le M\le40$ | 0 mismatches — PASS |
| C | $(3,2)$: $\operatorname{im}P$ invariant but intertwining fails | PASS |
| C | $(5,3)$: $P^{+}P=I$ yet $\operatorname{im}P$ NOT invariant — **old audit test was invalid** | PASS |
| C | $d>M$: $\operatorname{im}P=\mathbb C^M$ | PASS |
| D | $Q^\ast Q=I_3$; $Q^\ast\Delta_{12}Q=L_3$; $P^\ast\Delta_{12}P=4L_3$; $\|P\Omega\|=2\|\Omega\|$ | PASS ×4 |
| E | $V_3=\{e_0,e_4,e_8\}$, spec $\{0,-3,-3\}$; deck-fixed $\{0,4,8\}$; **complement $\{-2\pm\sqrt3(\times2),-1(\times2),-2(\times2),-4\}$** | PASS ×3 |
| F | real projectors $E_0,E_2,E_{13}$: ranks $6,6,12$; orthogonal, sum $=I$; $\operatorname{range}E_0$ = realification of $V_3$ | PASS ×3 |
| G | $C_3\not\subset C_{12}$ (0 triangles); deck $\{0,3,6,9\}$ | PASS ×2 |
| H | modular identity (6.2) for all $n$, $M\in\{3,\dots,63\}$ | PASS |
| I | $z^+=z(1-\varepsilon|z|^2)$: unit multiplier, algebraic decay $|z_N|=7.070\times10^{-3}$ vs $(2\varepsilon N)^{-1/2}=7.071\times10^{-3}$ (NOT exponential) | PASS |

**F13 resolved:** the v0.1 "$(3,2)$ PASS" was a literal `True`, and the unused expression $\Delta_M P\,P^{+}P=\Delta_M P$ follows from $P^{+}P=I$ for any full-column-rank $P$ and does **not** test invariance (it would "pass" for the non-invariant $(5,3)$ image). v0.2 uses the correct test $(I-PP^{+})\Delta_M P=0$ and classifies the full range.

## C. Reduction cross-check (`paperA_reduction_check.py`, read-only) and referee reproduction

- Local read-only import (`sys.dont_write_bytecode=True`; 0 `.pyc` written): one-step and free-trajectory max **per-component (infinity-norm)** discrepancies (not Euclidean).
- **Referee independent reproduction** (fourth-order FD Jacobian; direct cyclic matrices; source loaded only after re-derivation):

| test | max per-component error |
|---|---|
| one-step $F_{12}(P\Omega)$ vs lifted reference, 50 runs | $5.53\times10^{-15}$ |
| free 600-step, defaults, 5 seeds | $2.13\times10^{-15}$ |
| free 600-step, $(0.2,0.5)$, 5 seeds | $3.82\times10^{-15}$ |
| one-step generalization $M=3,\dots,63$ | $2.61\times10^{-16}$ |
| free 600-step, **all** random params (caveat) | $4.94$ per-component; $11.09$ Euclidean |

**Long-trajectory caveat (retained):** exact one-step algebra does **not** guarantee indefinite machine-close trajectories in unrestricted regimes; sensitive parameters amplify implementation-order differences (worst $g\approx0.0076,\lambda\approx0.637$).

## D. Numerical values verified by the referee (cited, not regenerated)

- Default block moduli: tangential $U_0$ $(0.07264,0.08864,0.33013,0.42951,0.68095,1)$; $U_2$ $(0.11947,0.17736,0.47305,0.48865,0.73101,0.85127)$; largest $U_{13}$ $0.94892$.
- Representative $\rho_\perp$ (seeds 0,19,407): $0.9489192132$; $0.9912953186$/per-step $0.9956381464$; $1.1342206175$; $2.4167066891$; $1.0942264506$; $1.0000000000$.
- Euclidean op-norm of the $g{=}0.2,\lambda{=}0.5$ normal monodromy: $1.0326263720>1$ (transient growth despite $\rho_\perp<1$).
- $g_\ast=0.4220744431784353$ (fixed radii $(1.62613,1.63733,1.93169)$, residual $2.3\times10^{-16}$; eigenvalue slope $\approx-3.97$; character-2 block). Not promoting $\lambda\approx0.42844590$ at $g=0.2$ (branch longitudinally unstable there).
- **Corrected perturbation table (F07):** $(0.2,0.001)$ $-0.05243161232$/$-0.05243161307$; $(0.2,0.5)$ $-0.004371394220$/$-0.004371394222$; $(0.1,0.3)$ $+0.06297286724$/$+0.06297286730$; $(0,0.4)$ $+0.11030071763$/$+0.11030071784$; $(0.3,0.5)$ $+0.09004767578$/$+0.09004767572$; $(0,0)$ $\approx0$. Largest fit error $1.64\times10^{-8}$; period-8 amplitude-$10^{-5}$ run has no admissible fit (reported honestly).
- Atlas: coarse 190 = 96/40/1/53; all 379 = 150/132/1/96 (unresolved counts explicit). Sampled region, not area.

## E. Claim-discipline audit (unchanged boundaries)

No physics/spacetime/particle/measured-phenomenon claim; no historical-design claim (ring is a 2026 construction); no TORMENT/systems claim (§9 shared algebra only); exact reduction generalizes to all $3\mid M$ while the stability atlas is $M=12$-specific; $V_3$ attraction stated local/regional with counterexamples and the linear/nonlinear distinction; feedback stated as sufficient, not iff.

## F. Verdict

```
ANALYSIS_VS_REGRESSION_SEPARATED = YES
GENERAL_CONVERSE_ANALYTICALLY_PROVED = YES
INVARIANCE_TEST_CORRECTED (I-PP+)DP=0 = YES
THEOREM_STATEMENTS_AUDITED = YES
PROOFS_AUDITED = YES
NUMERICAL_VALUES_AUDITED = YES   (20/20 regression PASS; referee values cited)
CODE_REFERENCES_AUDITED = YES
```
