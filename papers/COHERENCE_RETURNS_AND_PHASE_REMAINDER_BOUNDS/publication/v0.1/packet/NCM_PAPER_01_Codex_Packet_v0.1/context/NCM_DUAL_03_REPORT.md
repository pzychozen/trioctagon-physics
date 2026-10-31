# NCM-DUAL-03 v0.1 — Native Three-Update Coherence Returns at Fixed Parameters

Completed bounded investigation, 31 October 2026. Author: Hilmir Frímann Halldórsson. GPT supplied the work order, proposed amplitude proof and fixed discovery design; Codex independently checked the sources/proofs, implemented and tested the research transcription, and executed the prescribed search. This package is research evidence, not a publication or an application change.

## Result

**No genuinely three-stage raw-coherence return was found or validated.** Of the 60 prescribed starts, 42 converged numerically to coherence-period-one states and 18 did not converge. The 42 nominal solutions form seven numerical groups under common-phase and cycle-start comparison. This finite search does not exclude period-three solutions in the remaining dispersed-phase domain.

There are nevertheless exact, useful exclusions at the fixed coefficients:

- The proposed amplitude lemma is correct: F(B3) lies strictly inside B_(3/2), and every finite unit-multiplier return starting in B3 has component moduli <=sqrt(1001/1000).
- A regular finite return in B3 that meets an ordinary phase sector of width <=pi/6 must be a fixed state. It cannot have coherence period three. This deduction does not require the published .9 lower amplitude bound.
- Any regular three-update return in B3 satisfies **|mu−1|<=161151/500000=0.322302**. Thus mu=+i and mu=−i are impossible for such a return. A minimal coherence period three cannot produce minimal full-state period twelve by an order-four remainder in this domain. This does not exclude every native twelve-cycle with other coherence periods.

The phase remainder was always an unknown. No coefficient, seed, phase objective, clock or motion law was adjusted to obtain these conclusions. The author's golden-ratio language remains illustrative, not a controller requirement.

## 1. Exact setup and source identity

The sole parameter tuple is

    epsilon=1/10, g=1/60, lambda=1/300,
    k=(999/1000,1,1001/1000).

The ideal map is

    V_i=z_i+epsilon z_i(k_i−|z_i|²)+g(z_j+z_k−2z_i),
    delta_i=lambda sum_(j!=i) sin[3(Arg0 V_j−Arg0 V_i)],
    F_i(z)=V_i exp(i delta_i).

All kicks use one prestage, Arg0(0)=0, and a zero output stays zero. The target is nonzero z in B3={max_i|z_i|<=3}, all nine three-block prestage components nonzero, F³(z)=mu z with |mu|=1, and distinct H0,H1,H2 for raw H(z)=zz†. No positive-scale quotient is taken. Fixed points and phase-drifting relative equilibria have coherence period one; a small residual alone proves neither an exact return nor its minimal period.

The exact coefficients and turning entrance (1+i,1+i,1−2i) are published in COHERENT:161–168. That source identifies the point as h=1/10, eta=1/1000 of the D1 family. DYNAMICS:57–104 fixes the actual recurrence/zero handling; OBSERVABLES:190–236 gives regular H closure and its zero-stratum limit. D1:118–156 supplies the amplitude potential and explicitly distinguishes the separate phase potential. Z:226–265 defines the existing cubic innovation and separate observer memory. Source IDs and selected ranges resolve in SOURCE_MANIFEST.json. No M3 coefficients or M3 radius theorem were used.

The five scientific source files match the accepted NCM-DUAL-02 manifest. The packet work order, prior report and prior manifest match the corresponding files already inspected byte-for-byte. The packet's proposed amplitude proof was reviewed, not treated as inherited authority. The prior GPT review was read as context; none of its old checkers or long certificates was replayed. Revision 7cc1fa03af589818bcdcfaaac51838cc36c84253 remains a reading locator, not a present-HEAD assertion.

The packet arrived after the independent Stage A analysis. The original interim Stage A snapshot is preserved unchanged; this report supersedes its missing-input status. The final plan was frozen at **2026-10-31 15:00:20 UTC**, before the first discovery evaluation. There was no intervening search and no change to the frozen solver after results were seen.

## 2. Analytical results before discovery

### Amplitude lemma: independently confirmed

Write V_i=[a_i−r_i²/10]z_i+g(z_j+z_k), with r_i=|z_i| and

    31997/30000 <= a_i=1+epsilon k_i−2g <= 32003/30000.

On B3, every self coefficient is >=4997/30000>0. This positivity justifies

    |F_i|=|V_i| <= (32003/30000)r_i−r_i³/10+1/10.

Put A=32003/30000. The cubic h(r)=Ar−r³/10 has its maximum on [0,3] at sqrt(10A/3), and max(h)²=40A³/27<49/25. Hence every output modulus is <7/5+1/10=3/2. The brief uses the slightly looser coefficient 27/25; its squared margin 49/25−5832/3125=293/3125 is also correct. Its minimum derivative fraction 11747/30000 on [0,3/2] is correct.

For R<=3/2, h is increasing on [0,R], giving

    max |F_i(z)| <= T(R)=R[1+(K−R²)/10], K=1001/1000.

B_(3/2) and B_(sqrt K) are invariant. If F^p(z)=mu z, |mu|=1, starting in B3, the block lies below radius 3/2, including its initial state because the last state has the same moduli. Let R be the maximum component modulus over the finite block. The outputs have the same modulus collection as the inputs. If R>sqrt K, an output attaining R would satisfy R<=T(R)<R, a contradiction. Therefore the whole block is in B_(sqrt K). This finite-block argument needs neither future-domain regularity nor a specified phase.

It gives no positive lower amplitude bound, no common phase sector and no existence or global cycle exclusion. Outside B3 is unclassified.

### Further sector exclusion

Consider a regular finite return in B3 that has one stage with ordinary phases in a closed interval of width D<=pi/6. Regular return makes every component at every stage nonzero. The amplitude bound gives each self coefficient >=29/30−1/5000>0. Thus every prestage is a strictly positive combination of all three input rays.

If D>0, this combination lies strictly between the extreme rays because the sector width is less than pi. The prestage phase width is strictly smaller than D. The published simultaneous phase lemma applies to that now strictly sub-pi/6 width at lambda=1/300, preserves its interval and cannot increase its width. Subsequent intervals remain nested. The unique short containing-arc width is invariant under common phase, so it cannot strictly decrease and return to its original value. Therefore all phases must agree.

In the aligned case the common phase remains exactly fixed, kicks vanish, and the positive amplitude vector follows the existing gradient step r^+=r−grad W(r), where

    W=epsilon sum_i(r_i^4/4−k_i r_i²/2)
      +(g/2)sum_(i<j)(r_i−r_j)².

On the convex cube [0,sqrt K]^3, the Hessian upper bound is

    L=epsilon(3K−k_min)+3g=313/1250<2.

The entire amplitude step segment lies in this cube, so Taylor's integral estimate gives W(r^+)<=W(r)−(1−L/2)||grad W(r)||². A finite return forces every increment to vanish. It is a fixed state with mu=1. This establishes the sector exclusion without assuming a common Lyapunov function for general amplitude-plus-synchronization evolution.

Separately, the inherited coherent annulus .9<=|z_i|<=1.1 with ordinary phase width <=pi/12 converges to a fixed state. A periodic H sequence in that invariant domain must be constant. Neither result is extended to arbitrary dispersed phases.

### Necessary phase-remainder bound

On B_(sqrt K), V=(I+D_z)z with the Hermitian matrix D_z=epsilon diag(k−|z|²)+gL3. Its spectrum is in [−251/5000,1001/10000]. Consequently

    ||V−z||_2 <= (1001/10000)||z||_2,
    ||V||_2 <= (11001/10000)||z||_2.

Every kick has magnitude <=2lambda=1/150. Using |exp(ix)−1|<=|x| yields

    ||Fz−z||_2 <= c||z||_2, c=53717/500000.

For a regular three-return, choose the cyclic starting stage with greatest Euclidean norm among its three states. Regular equivariance gives the same mu at every cyclic start. Summing three increments then gives

    |mu−1| <= 3c=161151/500000.

Equivalently Re(mu)>=1−(3c)²/2 and |Arg(mu)|<=2 asin(161151/1000000). This is a necessary region, not an imposed phase or a certificate of an actual mu. Since |(+/-i)−1|=sqrt(2), quarter-phase remainders are excluded. Other exact roots of unity may lie in this arc; finite decimals are not rationalized into an order, nor used to claim irrationality.

These arguments do not exclude the entire remaining state domain. In particular, very small components remain possible. The regular evaluator's derivatives become problematic near zero prestages; a small epsilon alone is not a uniform quotient contraction theorem. Thus the prescribed bounded discovery was warranted.

## 3. Frozen numerical experiment

[PLAN.md](PLAN.md), [resolved_plan.json](resolved_plan.json) and [PLAN_FREEZE.json](PLAN_FREEZE.json) bind the experiment. All 54 prescribed polar states and six Cartesian/conjugate diagnostics were used, in order. Exact rational/pi formulas remain alongside their 80-digit representations. Exact squared moduli choose the largest-component pivot, with lowest-index ties, avoiding floating tie choices.

The eight real unknowns are the six components of z and a,b for mu=a+ib. The residual contains all six equations F³(z)−mu z, a²+b²−1, and Im(z_pivot)=0. The pivot remains positive and fixed throughout a solve. Initial common rephasing is a gauge choice; no modulus is set to one, no intermediate state is rephased, and no state is normalized. Initial mu is the unit phase of z†F³z. No initial correlation was zero, so the neutral fallback was never needed.

The smooth evaluator uses Im of the cubed normalized prestage product, with no denominator repair. An independently written direct evaluator uses the original Arg0 form. The Jacobian is real, analytically differentiated through the three updates and independently tested against real finite differences. No holomorphic differentiation is used.

Each solve uses 80-digit Newton/LU and the frozen eight-row residual scaling. Backtracking tries 1,1/2,...,2^-20 with Armijo factor 10^-4. Trials outside B3 or with a nonpositive fixed gauge pivot are rejected before evaluation. Every rejection reason is retained. There is no hidden restart, alternative seed, changed coefficient or continuation.

Acceptance screening requires absolute return error <=1e-45, relative return error <=1e-40, and circle/gauge errors <=1e-45. Near-zero norm, amplitude-bound violation and small prestage/pivot conditions are screened separately. Lower-period classification requires all pairwise relative H separations and one-step phase-proportionality residual <1e-25. Genuine candidates require all three pair separations >1e-12. These are numerical criteria, not exact-period or existence proofs.

## 4. Actual outcomes, failures and validation disposition

| Outcome | Count | Interpretation |
|---|---:|---|
| Numerical lower coherence period one | 42 starts | Seven numerical groups, including fixed-like states and phase-drifting relative-equilibrium-like states; no interval existence/uniqueness claim. |
| Line search failed | 17 starts | No accepted decreasing trial among the frozen choices. This does not exclude a root locally or globally. |
| Iteration ceiling reached | 1 start, S01 | Approached a very small state without satisfying the relative return criterion. |
| Genuine numerical coherence-period-three candidates | 0 | No candidate triggered local existence validation. |
| Exact singular initial block / budget exhausted | 0 / 0 | All prescribed starts were attempted within the ceiling. |
| Certificate attempts / validated period-three cycles | 0 / 0 | No 120-digit candidate reevaluation, interval boxes or precision escalation was warranted. |

All attempt identities, states, prestages, kicks, raw H matrices, mu values, residuals and rejection histories are retained in `attempts/S01.json` through `attempts/S60.json`. [ATTEMPTS.md](ATTEMPTS.md) gives a compact complete ledger. [analysis_results.json](analysis_results.json) and [candidates.json](candidates.json) preserve the failures rather than discarding them.

S01 illustrates why relative screening matters: its final state norm was about 4.7027e-25 and absolute return error about 8.3061e-26, but relative return error was about 0.1766. It was not accepted as a return. It remains classified as solver failure at the iteration cap, rather than silently relabeled an exact zero root. S37 stopped with a small prestage modulus about 7.77e-6 and relative return error about 0.00251; it is not a candidate either. There were no numerically converged ambiguous-separation or near-singular candidates under the declared screening rules.

The 42 converged results group as follows. Grouping allows only a unit common phase and cyclic starting state, not channel permutation or conjugation. Every original conjugate start remains in the ledger.

| Group | Representative | Starts grouped | Fitted three-step phase, radians | Numerical character |
|---|---|---:|---:|---|
| G01 | S02 | 11 | about 2.10e-53 | Aligned, fixed-like |
| G02 | S04 | 10 | +3.3653148927493e-7 | Twisted, relative-equilibrium-like |
| G03 | S10 | 6 | −3.3653148927493e-7 | Conjugate twisted group, kept distinct |
| G04 | S13 | 7 | 0 at working precision | Mixed-sign, fixed-like |
| G05 | S16 | 6 | 0 at working precision | Mixed-sign, fixed-like |
| G06 | S19 | 1 | −6.9937464264523e-5 | Relative-equilibrium-like; minimum prestage modulus about 0.000928 |
| G07 | S52 | 1 | 0 at working precision | Mixed-sign, fixed-like |

These names describe numerical outputs, not newly certified branches or an identification with a specific inherited D1 solution. Their coherence is already stationary after one step within numerical tolerance. A three-step fitted multiplier on them does not make them three-stage solutions. No exact order of their phase remainder or full-state finite period is inferred.

All 42 nominal converged blocks were independently reevaluated with the direct Arg0 formula at 80 digits. The largest discrepancy between stored smooth-formula states and those direct states was about 6.69e-81; every regression passed. This confirms the transcription on the reported blocks, not an exact root. The prescribed 120-digit reevaluation was reserved for genuine period-three candidates; none existed, so no certificate checker was invoked or counted as passing. No certificate failed or was hidden: the prerequisite candidate was absent.

The search used 733 iteration passes, 691 Newton directions and 674 accepted steps. Trial outcomes were 449 outside-B3 rejections, 273 nonpositive-pivot rejections and 1,270 insufficient-decrease rejections. A fixed gauge without chart restarts and a local Newton method can miss roots; these limitations are part of the result.

## 5. Existing readouts and scientific interpretation

For the existing cubic K=z0 conjugate(z1) z2 and j=Im K,

    K(mu z)=mu² conjugate(mu) K(z)=mu K(z),  |mu|=1.

For an exact relative block this would imply j(F^(3m)z)=Im(mu^m K(z)). H ignores the same common phase. [READOUTS.md](READOUTS.md) reports j at the four actual evaluated stages of all seven numerical groups, alongside their H-separation measures; full H matrices are retained in JSON. Those are the real evaluated transitions, not values fabricated from a phase formula. No additional twelve-update trace, observer clock or EMA memory was advanced.

Some nominal lower-period states therefore show precisely the previously understood possibility: a nearly unchanged relative pattern with a changing common phase. They do not show the author's three distinct configurations. At the same frozen observer clock/configuration, staged Z discards that common phase; j can respond to it. No autonomous closure of (H,j), energy flux, spatial rotation or cone-pose map follows.

## 6. Verification, budgets and preservation

| Resource/check category | Actual work | Authorized limit or meaning |
|---|---:|---|
| Primary starts | 60 | 60 |
| Iteration passes per start | maximum 80 | 80 |
| Discovery F evaluations | 8,211 completed/attempted | 120,000 aggregate |
| Independent formula/testing F attempts | 151 | 384; includes 25 Stage A attempts and 126 direct regression calls |
| Intentional exact-zero test refusal | 1 | Included in 151 attempted calls; 150 completed |
| Total F attempts across this investigation | 8,362 | 8,361 completed and one intentional test refusal |
| Validation candidates / boxes / 120- or 160-digit candidate runs | 0 / 0 / 0 | No genuine candidate triggered them |
| Optional further native trace calls | 0 | 96 |
| Stage A evaluator/math checks | 25 passed | Zero failures/errors |
| Packet/plan/seed/classifier checks | 87 passed | Includes seed and hash checks; not 87 theorems |
| Post-run regression/accounting checks | 68 passed | Includes per-start accounting; not an orbit certificate |

The discovery count can be independently reconstructed: 60 initial three-step blocks, 733 Jacobian/residual three-step blocks and 1,944 evaluated line-search blocks give 3(60+733+1944)=8,211. Analytic directional derivatives do not call F behind the counter. Out-of-domain/pivot rejections made no F calls. All frozen plan/code hashes remain unchanged. No retry or post-result plan amendment occurred.

Environment: Windows AMD64; Command Prompt; existing `torment`; Python 3.11.15 at `C:\Users\Notandi\miniconda3\envs\torment\python.exe`; SymPy 1.14.0 and mpmath 1.3.0. NumPy 2.4.4 was installed but not required by the new computation. Commands used `python -X utf8 -I -B`. Exact rational definitions specify the ideal target; high-precision evaluations remain rounded numerical diagnostics, not interval enclosures or a binary64 parameter experiment.

SOURCE_MANIFEST.json records bounded original-input and packet before/after identities, and CLOSEOUT.txt records final preservation. This is not a whole-checkout audit. All authored files are under the fresh external research root. No Git, kernel/application/lock/prior-paper edits, package installation, UI control, old certificate replay, added clock or publication occurred. The Stage A archive and prior studies are preserved.

## 7. Required scientific summary and readiness

| Required question | Answer |
|---|---|
| What was analytically excluded? | Amplitudes above sqrt(1.001) in any finite return from B3; nonstationary regular coherence returns meeting a <=pi/6 ordinary phase sector; +/-i remainders of regular three-returns throughout B3. All hypotheses are stated above. |
| What was searched? | The exact prescribed 60 starts at the one fixed rational coefficient tuple, using the frozen 80-digit eight-equation solver. |
| Which states returned? | 42 nominal lower-period results, 18 numerical failures, zero genuine period-three candidates, zero validated period-three cycles. No exact-zero or singular candidate is claimed. |
| What is known about phase/full period? | A rigorous necessary arc for any qualifying three-return; numerical multipliers for lower-period outcomes; no exact phase order or actual period-three full-state period established. |
| What do existing diagnostics distinguish? | H discards common phase; K transforms by mu and j can detect it; frozen staged Z ignores it. Actual lower-period readout records are retained, with no fabricated continuation. |
| What is missing for cone motion? | Existence/validation of a genuinely three-stage native return remains unresolved in the complementary domain, and a separate state-to-pose/evolution correspondence would still be needed. Neither follows from a count. |

**Plain-language result:** the unchanged equations repeatedly led this search to states whose relative pattern already returns after one update. Some of those states still change common complex phase. The search did not establish a sequence of three different relative patterns. More strongly, the proven bounds say that any such three-update return within B3 could not leave the quarter-phase remainder needed for the proposed three-times-four count. That is a specific mathematical limit, not a rejection of every kind of motion or of the author's broader idea.

**Paper readiness:** the fixed-parameter amplitude, sector and phase-remainder exclusions are substantive bounded results worth independent mathematical review, potentially as a focused proposition or appendix. This package is not ready for a paper claiming a native three-stage orbit, twelve-update cone motion or physical energy transport. Novelty and proof presentation still need scientific review; the finite search is evidence of its own outcomes, not a nonexistence theorem. No larger search, changed parameter point, manuscript or automatic successor task is started. This work stops with the complete bounded review package.
