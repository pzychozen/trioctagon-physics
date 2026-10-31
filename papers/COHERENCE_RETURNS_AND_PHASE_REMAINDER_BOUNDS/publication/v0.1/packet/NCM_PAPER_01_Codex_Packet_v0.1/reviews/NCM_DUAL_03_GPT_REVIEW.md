# NCM-DUAL-03 — GPT mathematical and evidence review

**31 October 2026.** Internal review of the supplied bounded investigation, not publication approval, external peer review, or a new native-motion experiment.

## Disposition

**Accept NCM-DUAL-03 as a completed bounded investigation.** I found no blocking mathematical error in the amplitude, reported 30-degree phase-sector, or phase-remainder exclusion arguments. The numerical search was appropriately reported as inconclusive for genuine coherence-period-three orbits, not as a global nonexistence proof.

The specific connection `minimal raw-coherence period 3 + quarter-phase remainder = full-state period 12` is excluded **at the stated fixed coefficients, for regular returning blocks starting in B3**. This is an analytic exclusion, independent of whether the 60-start search found a candidate. It is not an exclusion of all native twelve-cycles, all parameter sets, all initial amplitudes, other sampling relations, or the author's broader spatial hypothesis.

Keep the author correction controlling: golden-ratio language in the cone explanation was illustrative and is not a controller requirement. No parameter, observer clock, sampling stride, pose law, or transport rule has been changed to recover a desired count.

## 1. Material reviewed and integrity

Received archive: `NCM_DUAL_03_v0.1_REVIEW.zip`.

- Size: **1,375,003 bytes**.
- SHA-256: `e93d1c2af0993f88dc2d7596381b8b599d76211ac17da3425891b91e9299748a`.
- **111/111 manifest-listed members** match their recorded byte lengths and SHA-256 hashes; the manifest itself is the 112th archive entry.
- The separate report attachment is byte-identical to `phase_b/REPORT.md`.
- All five frozen-plan/code hashes match.
- The ten embedded work-order-packet members match the original uploaded packet, whose complete archive identity also matches the intake record.
- All eight original-input before/after preservation records are internally consistent. **The live Windows originals were not inspected here.**
- The original extracted review input was rehashed after the review: **111/111 unchanged**.

The root Stage A files are preserved preliminary evidence. The final controlling report and outcome records are under `phase_b/`. The documented missing-packet status was resolved before the discovery freeze. It is not an outstanding blocker.

## 2. Fixed mathematical problem

The sole parameter tuple is

\[
\epsilon=1/10,\qquad g=1/60,\qquad \lambda=1/300,\qquad
k=(999/1000,1,1001/1000).
\]

The target is a nonzero state with

\[
F^3(z)=\mu z,\qquad |\mu|=1,
\]

and three distinct raw coherences \(H_n=z_nz_n^\dagger\). All nine prestage components in the block must be nonzero. Here

\[
B_3=\{z\in\mathbb C^3:\max_i|z_i|\le3\}
\]

is an amplitude domain in state space, **not the spatial enclosing sphere**. Common complex phase is not automatically a physical rotation angle.

## 3. Review of the submitted analytical proofs

### 3.1 Amplitude absorption and returning-block bound

Set \(K=1001/1000\) and \(A=32003/30000\). On \(B_3\), the self-coefficient in the prestage is at least \(4997/30000>0\). It is therefore legitimate to use

\[
|F_i(z)|=|V_i(z)|\le Ar_i-r_i^3/10+1/10.
\]

The maximum of \(Ar-r^3/10\) on \([0,3]\) occurs at \(\sqrt{10A/3}\), with squared maximum \(40A^3/27<49/25\). Consequently \(F(B_3)\subset\operatorname{int}B_{3/2}\).

For \(R\le3/2\), the cubic envelope is increasing on \([0,R]\), giving

\[
\max_i|F_i(z)|\le T(R):=R[1+(K-R^2)/10].
\]

The balls \(B_{3/2}\) and \(B_{\sqrt K}\) are invariant. Any finite unit-multiplier return from \(B_3\) lies entirely in \(B_{3/2}\). If \(R\) is its largest component modulus and \(R>\sqrt K\), a component attaining that maximum as an output would obey \(R\le T(R)<R\), a contradiction. Hence

\[
\max_{n,i}|z_{n,i}|\le\sqrt K\approx1.000499875062461.
\]

This proof does not assume regularity or a phase target. It supplies no positive lower bound and no global orbit-existence result. Both the report's upper-envelope derivative \(11753/30000\) and the earlier brief's conservative minimum individual derivative \(11747/30000\) are consistent; they refer to different coefficient bounds.

### 3.2 Reported 30-degree sector exclusion

Regularity of a returning block implies that the state components at every stage are nonzero, including the initial state, because its last output is \(\mu z\). The amplitude bound gives positive self-coefficients, at least \(14497/15000\), with positive off-diagonal coupling. If the phases lie in a positive-width sector narrower than a half-plane, every prestage ray lies strictly inside that sector.

The phase stage preserves the prestage sector on the report's stated width domain. Therefore a positive shortest containing-arc width strictly decreases and cannot return under a common phase rotation. All phases must instead agree.

On the aligned set the synchronization kicks vanish and the common phase stays fixed. The remaining amplitude dynamics are the specified gradient step on a convex invariant cube. The Hessian upper bound is \(L=313/1250<2\), so the descent coefficient is

\[
1-L/2=2187/2500>0.
\]

A finite return must therefore be a fixed state. The argument does not assert descent of this potential for general dispersed-phase states. The original 30-degree exclusion is valid. Section 5 gives an additional reviewer strengthening, with its own elementary proof.

### 3.3 Phase-remainder exclusion

On \(B_{\sqrt K}\), the Hermitian prestage perturbation has spectrum in

\[
[-251/5000,\;1001/10000].
\]

The synchronization kicks obey \(|\delta_i|\le1/150\). Therefore

\[
\|Fz-z\|_2\le c\|z\|_2,\qquad
c=\frac{1001}{10000}+\frac{11001}{10000}\frac1{150}
=\frac{53717}{500000}.
\]

At the cyclic starting stage of maximal Euclidean norm in a regular three-return, the multiplier remains the same by regular equivariance. Telescoping yields

\[
|\mu-1|\le3c=\frac{161151}{500000}=0.322302.
\]

In particular \(|\pm i-1|=\sqrt2\) exceeds the bound, so a quarter-phase remainder is impossible. The exact principal-angle bound is

\[
|\operatorname{Arg}\mu|\le2\arcsin\left(\frac{161151}{1000000}\right),
\]

whose rounded display is **18.5474213628073 degrees**. The displayed decimal is not a separate interval certificate; the exact formula and rational inequalities carry the proof. This is a necessary bound on a common-phase remainder, not a measured spin rate or a spatial cone angle.

## 4. Numerical and execution review

The 60 starts are initial guesses for a Newton-type return-equation solver, **not 60 forward-time trajectory experiments**. Root-finder convergence to a relative equilibrium supplies no attraction claim for that state.

The retained records support:

- 42 numerically lower-coherence-period-one results, grouped into seven numerical common-phase/cycle-start groups;
- 17 line-search failures and one iteration-ceiling failure;
- zero genuine numerical coherence-period-three candidates and zero existence-certificate attempts;
- 8,211 discovery map evaluations reconstructed from the retained accounting;
- 151 independent regression/test attempts in the submitted work, including one intentional singular-prestage refusal.

The fixed gauge chart, bounded backtracking, finite starting set and local Newton method can miss solutions. Near-zero absolute residuals were not falsely accepted: the explicit S01 case fails its relative residual criterion. The seven numerical groups are not newly certified branches, nor silently identified with inherited D1 solutions.

### Replay performed here

Only copied input files were executed, in an isolated sandbox replay directory.

1. The unchanged `test_stage_a.py` replay passed **25/25** checks, with 25 map attempts, 24 completed and one intentional singular refusal.
2. The unchanged `phase_b/analyze.py` replay passed **68/68** audit checks and reevaluated all 42 nominal converged blocks with the direct Arg0 formula: **126 map evaluations**, no solver runs.
3. All five replayed result documents are exactly equal as parsed JSON to the submitted documents, including the numerical strings. Byte differences are text serialization/newline differences, not mathematical-output differences.
4. The new reviewer algebra script passed **27/27** rational/symbolic checks with **zero native-map evaluations**. The general proof in Section 5 is an argument, not a theorem inferred from that finite count.

No discovery search was rerun; no new seeds, parameter variations, longer trajectories, interval certificates, observer-clock updates, or EMA-memory updates were performed. The submitted 87 pre-search checks were inspected as records, not claimed as a newly executed suite here.

Review environment: Linux, Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0. This is not a second Windows certification.

## 5. Additional reviewer deduction: the sector exclusion extends to 60 degrees

**Status: new written GPT deduction during this review, separate from Codex's submitted report. It should receive independent verification before manuscript inclusion.**

### Proposition

At the same fixed parameter tuple, any nonzero regular finite unit-multiplier return starting in \(B_3\) that has one stage whose ordinary phases fit in a closed arc of width at most \(\pi/3\) is a fixed state with \(\mu=1\).

### Proof

The reviewed amplitude bound places the entire returning block in \(B_{\sqrt K}\). Every component is nonzero and every prestage is a strictly positive combination of all three state rays. Choose phase lifts in a shortest containing interval of width \(D\le\pi/3\). If \(D>0\), the prestage phases have lifts \(\phi_i\) strictly inside that interval; their containing width is therefore strictly smaller than \(D\).

For their simultaneous synchronization step, put

\[
a_{ij}=\begin{cases}
\lambda\,\dfrac{\sin(3(\phi_j-\phi_i))}{\phi_j-\phi_i},&\phi_j\ne\phi_i,\\
3\lambda,&\phi_j=\phi_i.
\end{cases}
\]

On \(|\phi_j-\phi_i|\le\pi/3\), the sine has the sign of the difference, and \(|\sin(3d)|\le3|d|\). Thus

\[
0\le a_{ij}\le3\lambda=\frac1{100},\qquad
1-\sum_{j\ne i}a_{ij}\ge1-6\lambda=\frac{49}{50}>0.
\]

The actual phase update can consequently be written exactly as a convex combination:

\[
\phi_i^+=\left(1-\sum_{j\ne i}a_{ij}\right)\phi_i
+\sum_{j\ne i}a_{ij}\phi_j.
\]

Every output phase stays inside the prestage interval. Taking arguments modulo \(2\pi\) does not alter the sine kicks; these lifts describe the same complex outputs. Hence a positive containing width strictly shrinks in the amplitude/coupling stage and cannot increase in the phase stage. This property persists within the nested interval.

Multiplication of the entire state by a common phase preserves its shortest containing-arc width. A finite unit-multiplier return is therefore incompatible with \(D>0\). For \(D=0\), all phases agree. The aligned amplitude-potential descent argument of Section 3.2 then makes every increment zero, proving a fixed state and \(\mu=1\). QED.

### Scope

This extends the report's sufficient ordinary-phase-sector condition from 30 degrees to 60 degrees. It is **not** a global exclusion: the complementary dispersed-phase domain remains unresolved. It is also not the 60-degree spatial cone-pair midpoint result; the two angles live in different spaces. No new phase or geometric convention is introduced.

## 6. Interpretation and stopping boundary

The conditional return theorem from NCM-DUAL-02 remains correct. NCM-DUAL-03 now excludes its desired quarter-phase specialization for regular three-returns in the specified amplitude domain at the fixed published coefficients.

This closes that specific proposed bridge more decisively than a failed search could. Do not change coefficients, clocks, normalization or sampling merely to recover twelve, and do not relabel a one-stage relative equilibrium as three distinct configurations.

The original cone choreography remains a valid prescribed kinematic construction, not an established native trajectory. Native cone motion, spatial energy flow and physical angular speed remain unestablished. The author's broader hypothesis is not rejected by a scoped exclusion, but it has not acquired affirmative support from this native-period investigation.

For a possible mathematical note, the amplitude, phase-sector and phase-remainder results are the substantive outcomes. They merit proof-focused independent review and novelty/placement assessment. A native-cone-motion paper is not warranted. No new work order, manuscript, repository edit, commit or publication is initiated by this review.

## Evidence files

- `PACKAGE_AUDIT.json`: archive/member, attachment, freeze and packet comparisons.
- `REPLAY_COMPARISON.json`: exact parsed-result comparisons.
- `stage_a_replay.log`: replayed 25-check output.
- `retained_analysis_replay.log`: retained-result regression/audit output.
- `review_exact_checks.py`, `REVIEW_EXACT_CHECKS.json`: independent coefficient checks and rounded display values.

The evidence ZIP includes the replayed mathematical scripts/results needed to identify what was run, but omits the 60 attempt records already present in the unchanged original package. This avoids presenting copied discovery records as a new experiment.
