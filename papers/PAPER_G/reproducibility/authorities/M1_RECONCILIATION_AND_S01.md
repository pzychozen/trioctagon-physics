# GPT M1 reconciliation note and sideband proof — v0.2

Date: 2026-10-01. Scope: review and standalone mathematics only. This note adds explicit corrections and a new exact derivation; it does not alter the supplied reports or imply bilateral acceptance.

## 1. Intake: the missing artifacts are now supplied

All 14 entries of the Claude original-export manifest, all four entries of the Claude cross-check manifest, and all 31 entries of the Codex delivery manifest match their supplied bytes. This is artifact integrity, not verification of their original creation histories or every scientific claim.

Claude's six named originals are in `CLAUDE_M1_SCRATCH_SCRIPTS_EXPORT.zip` under `m1_export/scripts/`. The README discloses the export workspace, original-script parameters, and dependencies. Its logs are explicitly export-time re-runs, not original stdout. The supplied `m1_verify.py` is the post-fix version; the preceding 41/42 version was not retained. The pseudoscalar snippet is explicitly a reconstruction. Preserve these distinctions in subsequent receipts.

Codex's `ORIGINAL_SCRIPTS_NOT_SUPPLIED` is an accurate statement about its earlier intake, not a current absence finding. Add a new receipt; do not rewrite the frozen old report. A file is supplied before it is inspected or replayed: report those as separate states.

I have not rerun all six original scripts or either reviewer's complete check suite. The 20 checks in `lead_checks/` are new GPT algebra/numerical checks, not those historical runs. They use Python 3.13.5 / NumPy 2.3.5 / SymPy 1.14.0 in this session, not the reviewers' original runtime. No repository module is imported.

## 2. Decision on the common mathematical core

Use Codex's CE01–CE11 structure as the base: it keeps exact algebra separate from finite-run results and labels the optional connection as an assumption. Both addenda support most of this core, but neither has accepted the supplied v0.2 text yet. It is a candidate, not consensus.

Retain:
- W=T C with its declared linear-class uniqueness and actual Paper-B covariance;
- exact S/A congruence and cofactor action, phase rotation, and state-dependent source decomposition;
- the qualified Gram closure, corrected zero-stratum behavior, and nonlinear covariants;
- exact entrance-to-W conversion with the nonzero multiplier hypothesis;
- local Jacobians and graph spectral identities with their actual domains.

Physical magnetism, physical current/helicity, automatic spatial flux, and dynamo interpretation remain unclaimed. H is already the geometric horizontal reflection in Paper B; physical time reversal is not an alternative reading to substitute into that established kinematic action.

## 3. Remaining corrections/qualifications to reconcile

### R9 — zero-stratum normalization and resonant zeros

Claude §3.1 writes tildeOmega=c u but drops |c|² in the area formula. Either choose |c|=1 and absorb all amplitude into u, or retain |c|². The candidate CE05 now makes this explicit. For example, tildeOmega=2 exp(i pi/6)(1,-1,0), lambda=pi/12 gives A+_AB=-2, not -1/2.

Claude's four predicates are necessary, not sufficient, for nonzero generation. Lambda=pi/2, alpha=pi/6 satisfies them but sin(2lambda sin3alpha)=sin pi=0. The complete iff criterion is the nonvanishing sine together with exactly one zero and opposite signs. This is a qualification of the generalization; the earlier Codex/GPT witnesses remain exact.

### R10 — exact entrance conversion versus finite persistence claims

For Omega=c f_j, j=1,2, Q=|c|²>0, b_i=1+epsilon(k_i-Q/3)-3g all nonzero, and epsilon nonzero:

C+=C0(b_B b_C,b_C b_A,b_A b_B), with C0=minus/plus sqrt(3)Q/6.

All harmonic-three torques vanish exactly at this first step, including sign flips. W+ is nonzero iff k is unequal. This is the agreed algebraic result, not just a sampled trend. With a zero b_i, use the actual Arg0 equation instead.

For the full decimal triple (1,1.2208964704604097,6.35310346037241), epsilon=.05,g=.2,Q=3,j=1, an exact rational interpretation of the printed decimals gives W+ approximately (-0.0412531228104126053,0.0825137050188467831,0). Codex's reported rounded computation agrees. The decimal vector is an approximation to the exact formula; do not label its truncated display exact.

Claude's original and cross scripts use the shorter literals (1,1.22089647,6.35310346). Codex uses the longer triple. This changes the first-step W by about (7.51e-12,1.04e-11,0). Their agreement at displayed precision is useful, but it is not identical parameter provenance. Retain both; use the longer declared triple for any new matched comparison, without modifying or retrospectively attributing it to the originals.

The sampled decay at lambda=.001/.1 and period-two observation at .5 do not prove 'persistent W requires lambda>lambda*' over all entrance amplitudes, branches, basins or parameter values. Lambda* is the local crossing of the specified in-phase fixed branch. Replace the universal necessity sentence in Claude §3.2 with its actual finite-run observation. The phase sign of an orbit and common-phase gauge also need to be stated.

### R11 — mixed-sign host, relative equilibrium and recurrence of observables

Codex §8's exact equal-unit mixed-sign existence calculation and its relative-equilibrium observation have not yet received Claude's reciprocal response. Compare against the newly supplied originals, including precise seeds and growth-fit windows.

A stationary C/W does not prove a fixed complex Omega. Likewise six alternating Gamma_M samples do not prove the ring state is period two. Record separately the full-state two-step residual, a common-phase-minimized residual, and recurrence of the chosen observable. Do not elevate a finite plot or rounded cycle to an exact orbit theorem.

### R12 — exact lifts, sidebands and the proposed ring follow-up

An exact repeated-triad entrance remains on its residue-three sector by the raw lift theorem F_12(Pz)=P F_3(z). Off-sector instability does not produce an off-sector perturbation from zero. A small perturbation, non-lifted input or noise changes the experiment and must be named.

Claude's off-line instability uses equal k=1,g=.1 and carrier mode 1. The proposed entrance investigation uses a generally unequal period-three k and lifted modes {0,4,8}, usually g=.2. These are different backgrounds. The instability of one is not evidence of the instability of the other.

For a general ring, W=T C is not yet a canonical three-component ambient readout: T belongs to the triad's geometry. Use the accepted edge-area cochain for ring claims unless a block/aggregate attachment is explicitly defined and reviewed. No new attachment is adopted here.

### R13 — function-class language

K4 can be nonzero on A=0, but is not confined to that sector. Example Omega=(1,2,3i) has K4=6 and C=(6,-3,0). Retain Codex's narrower wording. The Gram bound is relative to current intensity; use Atlas 09's scoped bounded region without saying it is the only possible boundedness theorem.

The external plasma sign remains UNRESOLVED_EXTERNAL_CONVENTION and is not load-bearing. Do not spend another general literature round on it to close this core.

## 4. S01 — an exact sideband result for Claude's particular plane wave

This is a new GPT derivation strengthening the numerical observation in Claude §3.5, offered separately for both reviewers to check. It does not prove the reported nonlinear ring end state or its basin.

Use a ring of N=12, equal k0=1, epsilon=1/20, g=1/10, carrier q=pi/6 and

\[
 r_*^2=2\sqrt3-3>0,\qquad \Omega_n^*=r_*e^{iqn}.
\]

The two harmonic-three neighbor torques cancel. Furthermore cos(3q)=cos(pi/2)=0, so the first derivative of the phase torque is zero. At this nonzero host the synchronizer derivative is the identity for every finite lambda. This explains, rather than assumes, the reported lambda-independence of the linear instability.

Write a perturbation as deltaOmega_n=e^{iqn}eta_n. Using the plane-wave equilibrium equation, the derivative of the pre-sync map is

\[
 \eta_n^+=(1-2g\cos q-a)\eta_n
 +g(e^{iq}\eta_{n+1}+e^{-iq}\eta_{n-1})-a\overline\eta_n,
 \qquad a=\epsilon r_*^2.
\]

For Fourier sideband ell, the pair (eta_ell,conjugate(eta_-ell)) has block

\[
 B_\ell=\begin{pmatrix}
 1-2g\cos q-a+2g\cos(q+\ell)&-a\\
 -a&1-2g\cos q-a+2g\cos(q-\ell)
 \end{pmatrix}.
\]

Therefore

\[
 \mu_\pm(\ell)=1-a-2g\cos q(1-\cos\ell)
 \pm\sqrt{a^2+(2g\sin q\sin\ell)^2}.
\]

For ell=pi/6, this gives

\[
 \boxed{\mu_+=\frac{13-2\sqrt3}{10}
              +\frac{\sqrt{22-12\sqrt3}}{20}
        =1.008712209379843415\ldots>1.}
\]

Indeed a=(2sqrt(3)-3)/20>0 and mu+=1-2a+sqrt(a²+1/400). The inequality mu+>1 is equivalent to 1>3(2sqrt(3)-3)², or sqrt(3)>31/18, which follows by squaring positive terms: 3>961/324. Thus this sideband instability is exact within the declared mathematical model, not merely a finite-difference eigenvalue. The paired physical Fourier modes are 1-1=0 and 1+1=2. The conjugate sideband block supplies the real degeneracy; the full real Jacobian has the reported double growing multiplier.

The standalone check additionally compares the analytic 24x24 real Jacobian to centered finite differences at lambda=0 and .3, with maximum observed differences about 5.84e-11 and 1.09e-10 respectively. These are numerical checks of the algebra, not its proof and not a replay of Claude's script.

Interpretation: this equilibrium attracts radially on its invariant plane-wave line but is unstable to particular perturbations away from that line. Both statements can hold simultaneously. This result applies to this specific equal-k carrier, not the unequal-k entrance lift and not a physical plasma instability.

## 5. Proposed disposition

Accept or object to CE01–CE11 of candidate v0.2 independently. X01 remains an optional, unadopted definition. S01 may be accepted separately after checking the derivation; its status must not be confused with the original finite numerical report.

Keep numerical thresholds/orbits in the separate numerical register. No persistence phase diagram or global attractor theorem is claimed. No implementation, UI changes, paper edits/publication, TORMENT work, broad new scan or new connection is authorized.
