# Codex investigation order — NATIVE_TURNING_CAPTURE_01
## Same-trajectory connection from native collective turning to coherent relaxation

**Author/research direction:** Hilmir Frímann Halldórsson (pzychozen)  
**Scientific steering and subsequent review:** GPT  
**Investigator:** Codex  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Authorization:** The author asked GPT to choose the most efficient next native-model investigation and issue it as a Codex work order, after requiring a check against completed work. This order implements that request. It does not authorize publication or model changes.

## 1. The single question

At the fixed coefficients and entrance of the published collective-turning witness, determine whether the **same full native trajectory** reaches the existing invariant coherent domain in finite update count. A positive answer should connect the inherited early turning result to the inherited asymptotic relaxation theorem. Assess a small neighborhood of that entrance only after the single-seed question is settled.

This is not a new force, receiver, observation law, transport channel, imposed path or fitted model. Do not continue the W/T transport-extension programme under this name.

### Why this question, and exactly what is new

`papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex` proves a two-step turning example and, separately, convergence on an annulus-and-sector domain. Its abstract, `sec:overview`, and the discussion around `thm:convergence` explicitly do not connect that entrance to the domain. The October 29 and November 1 handoffs retain the same gap. Later completion lists retain turning and relaxation as separate results.

The intended new content is **finite entry of that particular original trajectory (and, if justified, nearby entrances), followed by reuse of the existing theorem**. No novelty is claimed for turning, the domain, phase contraction, the equilibrium profile, observable decay, the certificate method, or the elementary implication “finite entry plus forward invariance gives convergence.”

This initial source comparison is not an exhaustive novelty proof. Work package N01 is mandatory: search the relevant later sources for a result that already closes this exact gap.

## 2. Freeze the mathematical object

Use three channels and the original simultaneous ordered native map:

\[
v_i=\Omega_i+\epsilon\Omega_i(k_i-|\Omega_i|^2)
       +g\sum_{j\ne i}(\Omega_j-\Omega_i),
\]
\[
\delta_i=\lambda\sum_{j\ne i}\sin\!\left(3[\operatorname{Arg}_0 v_j-\operatorname{Arg}_0 v_i]\right),
\qquad F_i(\Omega)=v_i e^{i\delta_i},\qquad \operatorname{Arg}_0(0)=0.
\]

All prestages use the same old state, and all kicks use the same prestage. A zero prestage stays zero after multiplication. Preserve the implementation's separate lambda=0 bypass as a source convention, but **this case has nonzero lambda throughout**.

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad\lambda=\frac1{300},\quad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),\qquad
\Omega_*=(1+i,1+i,1-2i).
\]

The target is the **existing** domain

\[
\mathcal D=\{\Omega:9/10\le |\Omega_i|\le11/10\ \forall i,
\ \text{the three ordinary phases admit one common interval of width}\le\pi/12\}.
\]

The interval may have any common angle. It is an interval of ordinary phases modulo a common full turn, **not** a phase sector modulo 2pi/3. The entrance moduli are sqrt(2), sqrt(2), sqrt(5), so it starts outside this domain.

No coefficient continuation, normalization, timestep reinterpretation, split exchange, stochastic forcing, geometric feedback or state replacement is allowed. n counts native updates, not calibrated physical time. Exact rational input data control the proof; binary64 rounding defines only a numerical implementation/comparison.

## 3. N01 — prior-work gate (before new trajectories)

Complete `PRIOR_WORK_COMPARISON.md` against the actual accessible corpus. Start with the primary paper and claim/source map, then the closest later native works and their evidence. Consult the repository research/atlas indexes to find relevant omitted titles; do not rely only on paper names or a search engine's empty result.

For each potential overlap record: exact source, edition or hash/checkpoint, section/equation/theorem, parameter tuple, entrance/domain, conclusion, and why it does or does not answer this question. Look for equivalent results with renamed variables, same-trajectory basin entry, validated capture of this seed, or a stronger basin theorem covering it. Negative results and restrictions count as prior work.

Priority comparisons:

1. Collective turning and coherent relaxation: `eq:parameters`, `eq:entrance`, `eq:certturn`, `sec:domain`, `thm:convergence`, `eq:fullbound`, `sec:prior`.
2. Coherence Returns and Phase-Remainder Bounds: its return hypotheses, fixed-parameter searches and narrow-sector exclusions. A theorem about already-returning states is not automatically an entry theorem for this seed.
3. Native Potential and Closed Coherence: exact descent-domain and coordinate-closure hypotheses. A theorem requiring membership in D cannot silently supply entry into D.
4. Phase Reconstruction and Stationary Support Axes, and Natural Core Motion records: whether they actually generate and certify this finite connection rather than inherit its missing status.
5. Native Response Geometry (GR0–GR2/CM0/SA0), Paper G/M1–M3, and D0/D1: distinguish local branch stability, another seed's capture, another parameter regime and common-phase drift from the present claim.
6. Relevant later native evidence reached from those sources and the catalogue. The recent C/S/W/T papers are distinct conditional exchange/transport questions; do not treat their activity witnesses as native capture.

The author's local checkout may be behind the latest publication. Historical reading pins are not reset instructions. Do not reopen publication verification. Read the available paper sources and dated dispositions; record what was inspected. Use the source guide and existing local research workspaces without asking the author to reconstruct old coefficients or find files.

**Gate outcomes:**
- `ALREADY_ESTABLISHED`: a valid existing theorem/certificate covers this exact case. Return its derivation/source match and stop; do not produce another “new” proof or substitute an unapproved problem.
- `DISTINCT_GAP`: the inspected relevant sources leave the connection unproved; state the bounded search coverage and proceed.
- `SOURCE_BLOCKED`: a necessary controlling source is unavailable or conflicts. Return the precise gap; do not infer novelty from missing access.

Do not turn this gate into a new corpus-wide archival/publication audit. It is a scientific overlap check for one question.

## 4. N02 — characterize the original trajectory, without fitting

After `DISTINCT_GAP`, independently implement or carefully reuse the unchanged native map in an isolated research directory. Check formula and update-order parity against the source. You may inspect/reuse numerical infrastructure, but do not rerun entire historical scientific suites or count old certificates as new tests.

A short floating/high-precision trajectory of **this one seed** may locate a candidate entry N. Label every such result exploratory. Default search budget: up to 512 updates; one justified extension to 4096 for the same trajectory is allowed if needed. These are administrative search limits, not physical constants or evidence of non-entry. Stop early after finding a useful strictly interior target.

Record full complex states or reproducible sufficient records, component amplitudes, minimum prestage moduli and ordinary phase-arc width. Record the method for branch-independent phase width; a principal-argument wrap must not manufacture loss or gain of coherence.

No broad parameter scan, random-start basin map, rerun of the old 60-start cycle search, or new search for a desired period is authorized. The aim is one transparent native orbit, not a favorable replacement example.

Earliest possible entry is not required. Prefer a comfortably interior N over an optimized boundary hit. Keep the inherited first two steps identifiable. A fresh evaluation of those steps needed for a connected enclosure is a dependency check, not rediscovery of turning.

## 5. N03 — prove or delimit finite entry

Seek a rigorous finite certificate for the exact mathematical map:

\[
F^N(\Omega_*)\in\mathcal D
\]

with explicit componentwise amplitude margins and a valid common ordinary phase interval. An analytical proof is welcome; otherwise use directed/outward-rounded interval or exact rational enclosure arithmetic, with proved elementary-function remainders. High decimal precision or agreement between two floating runs is **not** a rigorous enclosure.

The certificate must connect all steps to the original exact entrance. Do not restart from a rounded intermediate state without a validated inherited enclosure. Record N, all relevant nonzero-prestage lower bounds, endpoint bounds, arithmetic precision/rounding or rational denominator, and all truncation error rules. A finite single-seed interval certificate is enough for the primary question; no all-state basin claim is required.

A possible regular-chart strategy, to be checked independently, avoids angle branch decisions:

\[
\sin(3[\arg v_j-\arg v_i])=
\frac{\Im((v_j\overline v_i)^3)}{|v_j|^3|v_i|^3},\qquad v_i,v_j\ne0.
\]

Use the original Arg0 rule if a genuine zero occurs; never silently regularize it. An interval containing zero is an inconclusive enclosure, not proof of a zero orbit. Refine, use a sharper representation, or report the unresolved step.

For terminal phase membership, one sufficient approach is to select a fixed nonzero rational complex direction a+ib and put w_i=(a-ib)Omega_i. Certify Re(w_i)>0 and |Im(w_i)|<tan(pi/24) Re(w_i) for every i, with rigorous bounds on the tangent. This contains all ordinary phases in a sector of width <pi/12. It is a sufficient test, not an equivalent necessary test or a change to the state. Other correct certified phase-interval constructions are allowed.

Avoid interval blow-up by justified precision, subdivision or validated local-error bounds. Do not narrow an enclosure merely to agree with a floating trajectory. Record any computational limits honestly.

**Acceptable outcomes:** certified entry; certified obstruction/non-entry with a separate adequate mathematical argument; or an explicit unresolved finite assessment. Not entering by the numerical budget does not prove non-entry. A failed interval enclosure does not prove dynamical instability.

## 6. N04 — use the inherited theorem; test robustness narrowly

If entry is certified, invoke the original invariant-domain/convergence theorem at Omega_N. Do not re-prove it. State the resulting **same-trajectory** conclusion and its exact hypotheses:

\[
\Omega_n\to e^{i\theta_\infty}r_*\quad (n\to\infty),
\]

with the same unique positive unequal profile, positive residual amplitude spread, and C,W,Gamma tending to zero as in that theorem. Reindex its existing estimates from N rather than pretending the seed was in D at time zero. Do not turn its upper bound on residual spread into the actual limiting value. Parameter and update order must still match.

Then, only if the finite path is regular and the terminal inclusion is strict, assess a neighborhood of **initial conditions at the same coefficients**. Finite composition continuity plus the inherited strict early turning inequality can yield a qualitative open neighborhood whose trajectories both turn initially and enter D. Explain that argument and its domain. An explicit rational-radius ball/box and uniform finite-entry certificate are useful but optional; do not optimize its size or let this strengthening block completion of the exact-seed result.

A neighborhood proof needs the early turning sign and the terminal inclusion to hold for the same set of entrances. Existing strict turning plus justified continuity may suffice qualitatively; a concrete radius requires quantitative margins. Individual limiting common phases need not coincide across the neighborhood.

Conjugation and common rephasing may be used only with justified native symmetry on the complete relevant regular path. No claim across singular prestages follows automatically. Do not confuse convergence of the trajectory with a proof of finitely many remaining direction changes: shrinking increments can still change direction.

## 7. N05 — explain the native mechanism and report the boundary

Return a short explanation of what the result changes:

- What was already known (early turning and in-domain relaxation)?
- What new connection, if any, has actually been certified?
- Does the observed turning for this entrance lead into the known aligned regime, or does the bounded investigation leave a different outcome unresolved?
- What does this say about the native state and the existing attached observables, without identifying those observables as physical positions, gravity or magnetism?

Descriptive changes in phase width or amplitudes are permitted. Do not attribute causation to a term from one trace alone; use the already-established mean accounting/delayed-graph result at its own scope. The phase-off comparison is not this full-map orbit. Do not invent an external field or receiver to explain the trace.

One scientifically useful negative or restricted conclusion is preferable to silently replacing the question. A new paper is not commissioned automatically. Return the evidence first for GPT and author discussion.

## 8. Environment, preservation and execution

Use Windows Command Prompt and the existing `torment` environment (`conda activate torment`). Record the actual Python version, dependencies used, commands and exit codes. The previously recorded Python 3.11.15 is context, not a substitute for measuring this run.

Preferred external workspace:
`C:/TORMENT/TRIOCTAGON_new/research/NATIVE_TURNING_CAPTURE_01/`

Preserve existing contents; use a new run subfolder rather than overwriting an unrelated run. Keep all previous papers, evidence, kernel/application code, dependencies and user local changes untouched. No Git operations, branch changes, commit, push, release, publication, UI integration or full historical suite replay. No dependency installation or persistent environment reconfiguration is authorized. Use available tools or implement the needed bounded arithmetic locally; report any genuine limitation.

Read local instructions. Do not execute this packet's reference code merely because it is present; it is a source reference, and its ordinary floating arithmetic does not certify the exact trajectory. Any new checking code belongs in the new research workspace. Count analytical claims, numerical observations, exact identities and packaging checks separately.

## 9. Deliverables

Return one review ZIP plus external SHA-256 sidecar, with:

1. `NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md`: actual investigation, exact hypotheses, proofs/certificate interpretation and disposition of N01–N05. “Not applicable” is allowed after a valid stop.
2. `PRIOR_WORK_COMPARISON.md`: completed source-by-source overlap check, including inspected later sources and the gate outcome.
3. `RESULT_SUMMARY.md`: plain-language result and its significance, preferably under two pages.
4. `CLAIM_LEDGER.json`: each statement marked inherited, newly proved/certified, numerical only, unresolved, or excluded; exact source/proof locators.
5. `SOURCE_IDENTITIES.json`: only files actually used, their original paths/pins/hashes, and the local instruction scope. Preserve supplied source copies unchanged.
6. New scripts, small data/certificate files, an auditable independent certificate checker when computational proof is used, and actual execution logs. Distinguish generation from checking; copying the same arithmetic twice is not independence.
7. A self-excluding review manifest and a delivery audit reopening every archive member. These are packaging checks, not theorem counts.

The central question must be answerable from the report without running code. For a computational certificate, the written argument must explain why the checker’s finite inequalities imply exact entry and why the inherited theorem then applies.

## 10. Finish and stop

Complete the bounded scientific return. Do not start a wider basin study, a parameter phase diagram, another transport extension, a gravity paper or a publication task. No new author geometry choice is necessary for this state-space question. Ask the author only if a genuinely new geometric assumption would be needed; this order does not authorize making one.

**The result is not predetermined. This order is to investigate a documented gap, not to confirm a preferred answer.**
