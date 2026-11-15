# Next theoretical gravity investigation

GRAVITY_NATIVE_RECOVERY_01 · GPT scientific recommendation · 22 October 2026

**Recommend starting with Question 1: does the existing transported energy control the complete unequal-background response?** It directly connects the native potential, matched transport, coefficient response and actual state update. The required equations and fixed branches already exist. The result could be a conditional descent theorem or an exact energy-growth obstruction; either would advance the mathematics without inventing a gravitational force or metric.

The present kernel already calculates Ω-trajectories, tangent representations, a quartic/graph potential, intensity and area-source budgets, and passive observations. The accepted research additionally derives background-dependent response weights, circulation, spectral alternatives and regular coherence closure. Their relation to an evolved physical geometry remains unestablished. The measurement framework is not being treated as a physical container.

Read with [equations E01–E15](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NATIVE_EQUATION_MAP.md), [source/function locators](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_IMPLEMENTATION_SOURCE_MAP.md), [established results](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_ESTABLISHED_RESULTS.md), and [open questions](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_OPEN_QUESTIONS.md).

## Ranking

The ranking weighs tractability and the amount of new mathematical understanding it can deliver. It is a recommendation, not a claim that any proposed theorem has been established.

| Rank | Question | Feasibility | Scientific significance |
|---|---|---|---|
| **1** | Does the native potential's transported phase energy decrease under the complete unequal-background update, and how does this differ from response reversibility? | **High.** Finite matrices, known positive branch and exact polynomial/Bloch formulas. Start with the triad; use six/twelve rings only as controlled contrasts. | **Highest immediate value.** Tests an actual energy–transport–response relationship; distinguishes physical-looking reweighting from a scalar already selected by the equations. |
| **2** | What is the smallest collection of existing intensities and pair coherences that closes and retains the native energy/transport accounting? | **High to medium.** SA0 supplies exact closure endpoints and fibre counterexamples. Degenerate strata are the main difficulty. | **High.** Identifies the information required for an autonomous geometric/energetic description and which apparently source-like aggregates lose essential data. |
| **3** | How can closed coherence evolution and native common-phase reconstruction jointly describe energy change and persistent trajectory drift? | **Medium.** Local regular reconstruction is accessible; complete domain and repeated-step statements need care. D1 gives an exact benchmark. | **High, with broader scope.** Connects actual trajectories to quotient geometry and energy, while respecting the accepted obstruction to one invariant-potential pure-gradient generator. |

## 1. Native energy versus full response — recommended first

**Precise question.** On the existing positive in-phase branch, is the native potential locally decreasing under the complete map, and which part of synchronization permits or prevents that? Can loss of diagonal balance coexist with contraction of this particular energy?

**Exact existing inputs:** E01 (ordered map), E03–E05 (isometry, transport energy and potential), E08 (positive fixed branch), E09 (A_r,P,Sφ,Jφ), E10 (cycle and Bloch decisions). Proof locations: GR0 §4(d–e); GR1 §§2–6; NRG eq:potential, eq:weighted, eq:SP; GR2 finite-sector formulas. Runtime definitions: dynamics.py, face_state.py and z_diagnostics.py. No new dynamics or metric is required.

Start with g>0 near a strictly stable equal triad, where r>0. Work modulo the common phase; do not assume the Euclidean sum-zero plane is Jφ-invariant. The first proof obligation is to identify the second variation of the **existing** potential in \(\Omega=r+a+iR\phi+\cdots\):

\[
B_a=Id-A_r,\qquad
K_\phi=R(Id-H_r)R=R^2(Id-P).
\]

The latter is the existing weighted Dirichlet form:

\[
\phi^TK_\phi\phi=g\sum_{\{i,j\}}r_ir_j(\phi_i-\phi_j)^2.
\]

These displayed combinations are algebraic targets obtained from E05/E09, not newly verified results of this recovery. Kφ has the common phase in its kernel; for g>0 it is positive on the quotient.

The decisive matrices to classify are

\[
\mathcal L_a=A_r^TB_aA_r-B_a,\qquad
\mathcal L_\phi=J_\phi^TK_\phi J_\phi-K_\phi.
\]

Their signs test one-step change of the potential's quadratic part. They are different tests from \(WJ_\phi=J_\phi^TW\). In particular, absence of an SPD symmetrizer does not itself rule out an energy contraction inequality.

A bounded analytic route:

1. Establish the Hessian identification and quotient domain with the correct factor of one half in the quadratic expansion.
2. Resolve the signs for the triad branch. Compare exact cycle-balanced and cycle-unbalanced cases; characterize degeneracies rather than fitting a new weight.
3. If needed, use the existing z=−1 and z=±i blocks to test whether the distinction survives in N=6 and N=12. Do not infer full-ring behavior solely from the repeated triad sector.
4. If the quadratic change is strictly negative on all normal directions, bound the nonlinear remainder locally. If not, give an exact perturbation direction showing the obstruction. Do not promote a semidefinite quadratic test to nonlinear descent.

The finite-step cross-check should separate the native pre-stage change from the synchronization change. Since synchronization preserves amplitudes, E05/E11 reduce the latter to pair coherences:

\[
\mathcal V(F\Omega)-\mathcal V(\widetilde\Omega)
=-g\sum_{\{i,j\}}\left[
\widetilde S_{ij}(\cos d_{ij}-1)-\widetilde A_{ij}\sin d_{ij}\right],
\quad d_{ij}=\delta_j-\delta_i.
\]

This is a proposed identity to explicitly derive from the existing pair rotation before relying on it. Its sign, not its existence as an algebraic expansion, is the scientific issue.

**Reviewable endpoint:** a finite-domain theorem or exact counterexample connecting the native potential Hessian, transported graph energy and full response; explicit separation from diagonal balance. Stop before physical interpretation, simulation, parameter sweep or implementation.

## 2. Minimal closed energy-bearing coherence

**Precise question.** For the native triad, which subset of existing pair coherences, together with \(s_1,s_2,s_3\), determines the next retained observables on an explicitly specified regular domain? Does the same subset retain the potential and transported edge energies?

**Exact existing inputs:** E01, E04–E05 and E11; SA0 §8 fibre criterion and exact witnesses; NRG eq:fibre, eq:Hpre/Hpost and eq:zerocounter. K-DIAG supplies \(\mathcal V\); K-AX supplies S_G,A_G and pair-rotation accounting.

The accepted bracket is already known: intensities are insufficient, full real Gram is sufficient on the regular domain. For each proposed retained subset \(\mathcal A\), the required statement is

\[
\mathcal A(\Omega)=\mathcal A(\Omega')
\ \Longrightarrow\
\mathcal A(F\Omega)=\mathcal A(F\Omega').
\]

Use

\[
|\Omega_i-\Omega_j|^2=s_i+s_j-2S_{G,ij}
\]

to test exact retention of each transported edge energy and their sum in \(\mathcal V\). Distinguish retaining energy at one instant from closing its evolution.

**Bounded route:** restrict initially to the triad, fixed native parameters and nonzero pre-components. Enumerate subsets of existing pair entries, using the rank-one Hermitian or rank≤2 real-Gram identities. For each omitted entry, prove reconstruction with its domain or construct a same-retained-data/different-next-data witness. Explicitly separate a generic chart result from a statement valid across rank/zero degeneracies. A global result for nonzero λ must confront SA0's existing zero-stratum counterexample.

Signed area cannot be silently recovered from an unoriented real Gram: conjugation changes A_G. Keep the optional target “retain signed area and drift” separate from “retain potential and edge energies.”

**Reviewable endpoint:** a minimality theorem with domain and reconstruction formulas, or a finite table of exact insufficiency witnesses. This answers SA0's still-open next calculation; it does not select a mass density, stress field or spatial position.

## 3. Coherence, energy and phase reconstruction of trajectories

**Precise question.** Which part of the full native trajectory can be reconstructed from the closed coherence path, and what phase information is discarded when it is reduced further to real Gram? Can energy change of the shape and persistent common-phase advance be accounted for separately using the existing state inner product?

**Exact existing inputs:** E01 (F), E03 (native real/complex Euclidean pairing), E05 (common-phase-invariant potential), E11 (coherence quotient), E14 (trajectory), E15 (accepted relative equilibria and weighted phase identities). Proof locations: SA0 §8; DRIFT D39–D47 and D1 closeout §§4–6.

A local diagnostic to investigate, derived from the existing pairing rather than a new metric, is

\[
Z(\Omega)=\sum_i\bar\Omega_iF_i(\Omega),\qquad
\alpha(\Omega)=\arg Z(\Omega),\qquad
F_{\rm aligned}(\Omega)=e^{-i\alpha(\Omega)}F(\Omega),
\]

where Z≠0 and a continuous phase branch has been specified. This does not replace the native update; it separates an observation of phase from an aligned representation of the same next state.

First establish its exact dependence on full coherence using the existing M and δ:

\[
Z=\sum_i e^{i\delta_i}(M\mathcal H)_{ii}.
\]

Then address what is mathematically nontrivial: the domain of a repeated-step reconstruction, phase accumulation along closed quotient paths, the orientation ambiguity after retaining only real Gram, and whether an energy inequality for the quotient survives alongside nonzero accumulated phase. Separate section/phase conventions from quantities invariant under their change.

Use the accepted D1 branch as a required consistency check, not a new discovery target. At a relative equilibrium this diagnostic must return \(h\nu\) modulo \(2\pi\), while coherence and \(\mathcal V\) are stationary. In the generator limit the known balance is

\[
\nu I=\frac1{30}\sum_{i<j}(r_i^2-r_j^2)\sin3(\theta_j-\theta_i).
\]

It must not be substituted for the finite-step sine identity. D1's nonzero rate already rules out one invariant-potential pure-gradient generator; a proposed decomposition must accommodate it.

**Reviewable endpoint:** exact local reconstruction and a precise description of its failure/ambiguity domains, with energy and phase roles kept distinct. Any claim of geometric phase must specify the quotient and convention; it is not the fixed shell connection's holonomy, spatial rotation or a gravitational trajectory.

## Decision for GPT and Hilmir

Choose **Question 1** first. It tests the most direct missing relationship with a scalar and transport law already selected by the native equations. Question 2 is the cleanest subsequent reduction problem. Question 3 is the broader trajectory investigation once the energy and information requirements are clear.

This recovery adds no Newtonian premise, Einstein equation, new metric, simulated trajectory or production change. All proposed calculations above remain unperformed. The five review documents are the only authored deliverables; accepted sources are preserved.
