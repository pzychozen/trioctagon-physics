# NATIVE_SAME_TRAJECTORY_RETURN_01

## Codex investigation of later native credit from an initially empty launch

**Prepared:** 3 November 2026, Atlantic/Reykjavik.  
**Author and research direction:** Hilmir Frímann Halldórsson / pzychozen.  
**Formulation and subsequent review:** GPT.  
**Independent analytical investigation:** Codex.  
**Status:** One bounded investigation prepared under the author's request to continue from `START_HERE.md`. The reciprocal chiral exchange paper and its closeout are complete. The estimates below are a new proposed analytical certificate to verify; they are not a result already established by that publication or a completed Codex investigation.

### Task and intended outcome

Determine whether the published, unchanged exchange equations admit an initially empty carrier/receiver launch that first supplies native trial storage and later gives **strictly negative total native-to-carrier power on the same solution**. Investigate the one fast-receiver comparison developed below. Return a theorem with a finite admissible coupling threshold and strict power margin, or identify the precise defect or residual condition preventing that conclusion.

The useful claim is an existence result for a declared admissible family. It does not require a universal return classification, a complete cycle, maximum extraction, or a spatial circuit. Here “total” means the signed sum across both native ports.

The proposed mechanism is reversible exchange through the existing collocated receiver. It introduces no new state, feedback law, damping, load, spatial attachment, or switching protocol. Its parameter restrictions are analytical choices, not physical calibration.

## 1. Baseline and focused sources

The authoritative edition is **A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model**, v0.1, at commit:

`273b1a6faaab19ea58748d00576439166eeef9ab`

[Immutable publication directory](https://github.com/pzychozen/trioctagon-physics/tree/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1)

All paths in the following table are relative to `papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/` at that commit.

| Source | What to use |
| --- | --- |
| `manuscript/candidate.tex`, §1, especially (1.2)–(1.6) | Fixed registration, raw chiral drive, exact normalized finite tents, trial storages, full exchange equations and units. |
| `manuscript/power.tex`, §2 | Jacobian bounds and homogeneous completion; signs of both total powers; complete local and integrated accounts. |
| `manuscript/wellposed.tex`, Theorem 3.1 | Global exchange solution, strong regularity for empty preparation, translation framework, bounded ports, first weak derivative norms, polynomial estimates. |
| `manuscript/activity.tex`, Proposition 4.1 | Admissible coherent launch and strict initial native supply and receiver charging. Proposition 4.2 records the distinct prepared-credit result. |
| `manuscript/capacity.tex`, §5 | Invariant, dark preparations, extraction ceiling and its actual denominator. |
| `manuscript/interpretation.tex`, §8 | Collocation, central-region qualification, stationary supports, distinct carrier circle and intended toroidal route, distinct N and G objects. |
| `evidence/accepted_proof.md` | Retained defining proof, particularly S1–S4, A1–A16 and B1–B4; use for finer source locators if needed. |

The recovered `TRIOCTAGON_SAME_TRAJECTORY_RETURN_HANDOFF_2026-11-03.zip` contains the full edition, `NEXT_INVESTIGATION.md`, `CANDIDATE_AND_RESULTS.md`, `COLLABORATION_AND_GEOMETRY.md`, `RESEARCH_AGENDA.md`, `SOURCE_MAP.md` and the exact accepted analytical review. This order implements that brief. It does not reopen the completed publication.

GPT's assessment read the six manuscript sections above and the relevant handoff and accepted-review content. The seven retrieved defining files, including the accepted proof, match the handoff edition and the immutable Git blob identities. This is the source basis for this new question, not a repeat of the publication closeout.

### Working locations

- Original repository: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`.
- Retained publication worktree: `C:\TORMENT\TRIOCTAGON_new\research\NATIVE_RECIPROCAL_EXCHANGE_PAPER_PUBLISH_01\publication_worktree`.
- Prior accepted investigation: `C:\TORMENT\TRIOCTAGON_new\research\NATIVE_RECIPROCAL_EXCHANGE_01`.
- Fresh output directory: `C:\TORMENT\TRIOCTAGON_new\research\NATIVE_SAME_TRAJECTORY_RETURN_01`.
- Existing operator environment: Windows Command Prompt, `call conda activate torment`, Python 3.11.15.

Use existing local source copies first. Recover any needed defining text from the immutable edition or the supplied handoff. Routine source recovery and algebra belong with GPT/Codex; do not ask the author to recall coefficients or find previously supplied files. If the proposed output directory already contains work, preserve it and use a separate run subdirectory.

## 2. Exact mathematical starting point

Write

\[
x=(a,b)\in\mathbb R^6,\qquad \Omega=a+ib,\qquad
f(x)=K(a\times b),\qquad J(x)=D_xf(x).
\]

The fixed source registration is

\[
u=(0,1,0),\quad e_z=(0,0,1),\quad
n_\pm=\frac{2u\pm\sqrt3e_z}{\sqrt7},\quad
A_{\rm reg}=\lambda_gR_z(\delta_g),
\]

\[
K=\kappa_{\rm in}
\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}A_{\rm reg},
\qquad \lambda_g,\kappa_{\rm in}>0.
\]

Keep the yaw and inherited gains fixed. Contact-tangent orientation signs do not change this source projection.

On the published periodic carrier of length \(L_c\), retain its fixed speed \(c>0\), contact positions \(s_\pm=L_c/2\mp\eta_{\rm geom}\), and normalized disjoint tents

\[
b_\sigma(s)=\epsilon_c^{-1}
\left(1-\frac{|\operatorname{wrap}_{L_c}(s-s_\sigma)|}{\epsilon_c}\right)_+,
\qquad 0<\epsilon_c<\eta_{\rm geom}.
\]

All underlying admissibility conditions of the published circle and disjoint profiles remain in force. Define

\[
\mathcal Bv=b_+v_++b_-v_-,\qquad y=\mathcal B^*p,
\qquad m=\frac{2}{3\epsilon_c},\quad d=\frac{2}{\epsilon_c^3}.
\]

The source supplies

\[
\mathcal B^*\mathcal B=mI_2,\quad
\|\mathcal B\|=\|\mathcal B^*\|=\sqrt m,\quad
\|\mathcal B'v\|_2=\sqrt d\,|v|.
\]

Here \(\mathcal B'v\) is the first weak spatial derivative of \(\mathcal Bv\). The tents are periodic \(H^1\); no second spatial derivative in \(L^2\) is assumed.

The unchanged exchange equations are

\[
\boxed{\begin{aligned}
\dot x&=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\\
p_t+c(r_c)_s&=\mathcal B\{\eta_Nf(x)-\eta_Rz\},\\
(r_c)_t+cp_s&=0,\\
\dot z&=\frac{\eta_R}{\beta_R}y,\qquad y=\mathcal B^*p.
\end{aligned}}
\]

The fixed storage scales satisfy \(\alpha_N,\beta_R>0\). The couplings \(\eta_N,\eta_R\) are dimensionless. Use both strictly positive for this investigation. All parameters are chosen once before launch and remain constant along each solution.

The trial storages and total powers are

\[
H_N=\frac{\alpha_N}{2}|x|^2,\qquad
H_C=\frac12\int(p^2+r_c^2)\,ds,\qquad
H_R=\frac{\beta_R}{2}|z|^2,
\]

\[
P_{NC}=\eta_Nf(x)^Ty,
\qquad P_{CR}=\eta_Rz^Ty,
\]

\[
\dot H_N=-P_{NC},\quad
\dot H_C=P_{NC}-P_{CR},\quad
\dot H_R=P_{CR},\quad
H_N+H_C+H_R=\text{constant}.
\]

The native quartic potential \(V\) is distinct from \(H_N\). This investigation uses exchange time and omits native \(F\)-jumps, as the approved diagnostic scope requires.

## 3. Smallest claim and declared preparation

Use

\[
\Omega_0=(1,e^{i\phi},1),\qquad
0<\phi<\pi/12,\qquad p(0)=r_c(0)=z(0)=0.
\]

Fix one such \(\phi\); \(\phi=\pi/24\) is a concrete default. It is equally useful to retain a fixed symbolic \(\phi\) throughout the proof. No invariance of this launch family during evolution is assumed.

The published drive is

\[
f_{0,\pm}=\frac{\kappa_{\rm in}\lambda_g\sin\phi}{\sqrt7}
(-2\sin\delta_g\pm\sqrt3).
\]

Thus \(f_0\ne0\) for every fixed yaw and positive inherited gains. Useful algebraic simplifications to check independently are, with \(G=\kappa_{\rm in}\lambda_g\),

\[
|x_0|=\sqrt3,\qquad
\|K\|=G\sqrt{8/7},\qquad
|f_0|^2=\frac{G^2\sin^2\phi}{7}(6+8\sin^2\delta_g)>0.
\]

### The theorem to establish or correct

Fix the admissible published geometry, finite profiles, positive storage scales, registration, one preparation above and a fixed \(\eta_N>0\). Prove that there is a finite computable threshold \(\kappa_{\rm crit}>0\) such that, for each **fixed** \(\eta_R=\kappa\ge\kappa_{\rm crit}\), its initially empty exchange solution has

\[
P_{NC}(t)>0\quad\text{for sufficiently small }t>0,
\]

and

\[
P_{NC}(t_*(\kappa))<0
\quad\text{at an explicitly specified later time}.
\]

Continuity must then give a nonzero later interval of native credit and a positive native-storage increment over that interval. Initial supply and receiver charging can invoke Proposition 4.1 after checking its hypotheses.

This quantifier order is essential: fix the other admissible parameters and preparation, derive a threshold depending on them, choose a finite receiver coupling, and follow that one solution. It is not a claim that any prescribed receiver coupling already satisfies the condition.

For this empty launch, conservation also gives the exact all-time restrictions

\[
H_N(t)\le H_N(0),\qquad
\int_0^tP_{NC}(s)\,ds=H_C(t)+H_R(t)\ge0.
\]

A later negative-power interval therefore means recovery of earlier supplied trial storage. It does not mean cumulative gain above the initial stock.

## 4. Proposed analytical route

Independently derive and challenge each step. The formulas in this section are a proposed certificate, not an instruction to confirm a preferred answer. A corrected finite bound within this same comparison is a successful outcome.

### 4.1 Exact rescaling

Set

\[
\kappa=\eta_R>0,\qquad \tau=\kappa t,\qquad
(p,r_c,z)=\frac{\eta_N}{\kappa}
(\widehat p,\widehat r,\widehat z).
\]

In this section, \(x(\tau)\) denotes the original native state evaluated at \(t=\tau/\kappa\). The exact equations in scaled time are

\[
\begin{aligned}
x_\tau&=-\frac{\eta_N^2}{2\alpha_N\kappa^2}
J(x)^T\widehat y,\\
\widehat p_\tau+\frac c\kappa\widehat r_s
&=\mathcal B\{f(x)-\widehat z\},\\
\widehat r_\tau+\frac c\kappa\widehat p_s&=0,\\
\widehat z_\tau&=\frac1{\beta_R}\widehat y,
\qquad \widehat y=\mathcal B^*\widehat p.
\end{aligned}
\]

The original total power is

\[
P_{NC}(t)=\frac{\eta_N^2}{\kappa}
f(x(\kappa t))^T\widehat y(\kappa t),
\]

where the core on the right is expressed in scaled time. The scaling is exact for every finite positive \(\kappa\). The carrier speed in the original equations remains the fixed positive \(c\).

### 4.2 Explicit comparison and negative margin

Introduce

\[
\omega=\sqrt{m/\beta_R},\qquad
T=\frac{3\pi}{2\omega}.
\]

With core drift and scaled propagation set to zero only in the comparison problem, its zero-external-state solution is

\[
x^{(0)}(\tau)=x_0,
\quad \widehat p^{(0)}(\tau)
=\frac{\sin(\omega\tau)}{\omega}\mathcal Bf_0,
\quad \widehat r^{(0)}(\tau)=0,
\]

\[
\widehat z^{(0)}(\tau)=f_0\{1-\cos(\omega\tau)\},\qquad
\widehat y^{(0)}(\tau)=\frac m\omega f_0\sin(\omega\tau).
\]

Its total-power coefficient satisfies

\[
Q_0(\tau)=f_0^T\widehat y^{(0)}(\tau)
=\frac m\omega|f_0|^2\sin(\omega\tau),
\]

\[
Q_0(T)=-D,\qquad D:=\frac m\omega|f_0|^2>0.
\]

This comparison is a proof device. The actual solution must retain propagation and core drift. Freezing the core or taking \(\kappa=\infty\) without the following finite error control would not establish the target.

### 4.3 Uniform bounds for the exact finite-coupling solution

Use

\[
V_\kappa=(\widehat p,\widehat r,\widehat z),\qquad
\|V\|_{CR}^2=\|\widehat p\|_2^2+\|\widehat r\|_2^2
+\beta_R|\widehat z|^2.
\]

The linear carrier/receiver part preserves this norm. Establish the resulting forced energy inequality directly, or from a properly justified group representation. Empty preparation is \(H^1\), so the source's strong regularity suffices; a mild formulation is also acceptable if all steps are justified.

Let

\[
R=|x_0|,\qquad k=\|K\|,\qquad
F_{\max}=\frac{kR^2}{2}.
\]

Original total conservation and nonnegative external stores imply \(|x(\tau)|\le R\). The published bounds imply

\[
|f(x)|\le F_{\max},\qquad \|J(x)\|\le kR.
\]

The intended estimates, uniformly for finite \(\kappa>0\) on \(0\le\tau\le T\), are

\[
\|V_\kappa(\tau)\|_{CR}\le\sqrt m F_{\max}\tau,
\qquad |\widehat y(\tau)|\le mF_{\max}\tau,
\]

\[
|x(\tau)-x_0|
\le\frac{\eta_N^2 kR mF_{\max}}{4\alpha_N\kappa^2}\tau^2,
\]

\[
|f(x(\tau))-f_0|\le\frac{A\tau^2}{\kappa^2},
\qquad
A:=\frac{\eta_N^2 k^2R^2mF_{\max}}{4\alpha_N}.
\]

The last estimate uses the Lipschitz bound for \(f\) on the Euclidean ball of radius \(R\), not preservation of an old coherent phase domain.

### 4.4 Control propagation with first weak derivatives

Let \(V_0\) denote the explicit comparison above. In the equation for \(V_\kappa-V_0\), the two forcing errors are

\[
(\mathcal B(f(x)-f_0),0,0)
\]

and

\[
\left(0,-\frac c\kappa\mathcal B'f_0
\frac{\sin(\omega\tau)}{\omega},0\right).
\]

The second expression is in the external energy space because the tents are \(H^1\). Check its sign and the exact comparison equation before estimating its norm. No second derivative of a tent, Fourier truncation, or operator-norm convergence of the whole unbounded generator is needed.

The proposed estimate is

\[
\|V_\kappa(\tau)-V_0(\tau)\|_{CR}
\le
\frac{c\sqrt d\,|f_0|}{\kappa\omega}
\int_0^\tau|\sin(\omega s)|\,ds
+\frac{\sqrt m A\tau^3}{3\kappa^2}.
\]

At \(T=3\pi/(2\omega)\), the sine integral is \(3/\omega\), giving

\[
\boxed{
\|V_\kappa(T)-V_0(T)\|_{CR}
\le\frac{3c\sqrt d\,|f_0|}{\kappa\omega^2}
+\frac{\sqrt m AT^3}{3\kappa^2}.
}
\]

### 4.5 A finite threshold that preserves total negative power

Set

\[
Q_\kappa=f(x(T))^T\widehat y(T).
\]

Use the exact decomposition

\[
Q_\kappa-Q_0(T)
=(f(x(T))-f_0)^T\widehat y(T)
+f_0^T\{\widehat y(T)-\widehat y^{(0)}(T)\}.
\]

The proposed bound is

\[
\boxed{
Q_\kappa\le-D+\frac{C_1}{\kappa}+\frac{C_2}{\kappa^2},
}
\]

where

\[
C_1=\frac{3c\sqrt{md}\,|f_0|^2}{\omega^2},
\qquad
C_2=mAT^3\left(F_{\max}+\frac{|f_0|}{3}\right).
\]

All these constants are finite, independent of \(\kappa\), and \(D>0\). Check units as well as algebra. Since \(\kappa\) is dimensionless, \(C_1/D\) and \(C_2/D\) must be dimensionless.

A conservative proposed threshold is

\[
\boxed{
\kappa_{\rm crit}=
\max\left\{1,\frac{4C_1}{D},\sqrt{\frac{4C_2}{D}}\right\}.
}
\]

For \(\kappa\ge\kappa_{\rm crit}\), the claimed consequence is

\[
Q_\kappa\le-\frac D2,
\qquad
t_*:=\frac T\kappa>0,
\]

\[
\boxed{
P_{NC}(t_*)\le-\frac{\eta_N^2D}{2\kappa}<0.
}
\]

Justify continuity of the total power from the established solution regularity. Choose a sufficiently small neighborhood of \(t_*\), lying strictly after zero, on which the power is negative. If using the displayed margin, continuity permits a neighborhood with \(P_{NC}\le-\eta_N^2D/(4\kappa)\). Integrating \(\dot H_N=-P_{NC}\) gives the required positive gain over a later interval on this same solution.

The initial positive-power interval is already supplied by Proposition 4.1 for every fixed finite positive \(\kappa\). Its small-time remainder need not be uniform as \(\kappa\to\infty\); do not assume such uniformity.

## 5. Codex proof and evidence endpoints

Complete these three linked steps as one investigation:

1. **Confirm the exact problem and comparison.** Bind the equations to the immutable source; verify the nonzero coherent preparation, exact scaling, comparison solution and total negative margin. Retain the full two-port sum and active receiver.
2. **Prove or correct the finite-coupling certificate.** Justify the forced external energy estimate, core-drift bound, first-derivative propagation residual and resulting strict finite threshold. Independently recalculate constants. A larger sound threshold is preferable to an unjustified sharp one.
3. **State the theorem and its meaning.** Show initial supply, later total credit and receiver activity on the same unchanged trajectory. Record the sufficient regime and the actual interpretation. If a proof step fails, identify the exact failed implication and the strongest supported conditional result; a failure of this route is not a universal no-return theorem.

This is a proof-first assignment. Numerical trajectories and parameter sweeps are unnecessary. Exact symbolic checks may support the rescaling, comparison solution, norm constants and threshold algebra; list what each check verifies, and keep it distinct from the analytical PDE argument. Do not count prior historical checks as newly executed checks.

Work in the separate research directory. Reading existing sources and writing the new investigation artifacts are in scope. Existing publications, source/model implementations and kernel behavior remain the baseline. This assignment includes no Git operations, hybrid rollout, model redesign or publication work.

Stop when the theorem with a finite certificate, or a precise scoped obstruction/conditional result, is reviewable. Do not start a second parameter regime or a broader return classification to strengthen an already sufficient result.

### Requested return package

Provide:

- `NATIVE_SAME_TRAJECTORY_RETURN_01_PROOF.md`: one theorem or scoped disposition, full assumptions and quantifiers, the derivation, corrected constants if needed, and clear physical/geometric scope.
- `NATIVE_SAME_TRAJECTORY_RETURN_01_CLAIM_SOURCE_LEDGER.md`: distinguish inherited equations/results from new exact identities, proved estimates and conditional statements.
- A concise source identity and execution record. Preserve the hashes of the defining files actually used; record any optional helper and its exact purpose. A focused provenance record suffices; this is not a new repository-wide audit.
- One review ZIP containing the report, ledger, this order and any supporting records/helpers actually used, with a member manifest and archive SHA-256. Do not duplicate unrelated historical collections.

The return message should lead with **established**, **conditional**, or **not established within this route**, then give the exact finite-parameter conclusion and its most important limitation. GPT will review it before any subsequent research phase or publication proposal.

## 6. Interpretation to preserve

### What a successful theorem adds

The published work already supplies matched debit/credit equations, global exchange evolution, strict launch activity and prepared credit. The new result would show that an initially empty launch **actually reaches later total native credit without resetting or preparing a second state**. It would close the smallest approved dynamical gap.

The receiver is dynamically active: for the nonzero drive and positive couplings, the published launch result gives \(H_R(t)>0\) for sufficiently small positive time. A positive coupling with an identically inactive receiver would not be an adequate substitute.

### What mechanism this particular certificate studies

At the comparison witness,

\[
\widehat z^{(0)}(T)=f_0,\qquad
\widehat y^{(0)}(T)=-\frac m\omega f_0.
\]

Thus receiver backflow is the comparison mechanism for returning native storage. The finite theorem's required conclusion is total native credit; any additional assertion about the exact receiver power at that same instant must have its own justified bound.

The witness time is \(O(\kappa^{-1})\). The external storage on this time window is \(O(\eta_N^2\kappa^{-2})\), following from the displayed scaled norm bound. The negative power is of order \(\eta_N^2/\kappa\) in this comparison regime. Strict existence can therefore coexist with a small transferred amount. Neither a substantial returned fraction nor maximum accessible capacity is established by this construction.

Because the two couplings share the same finite profile regions, increasing \(\kappa\) makes this witness arbitrarily early compared with the fixed circle-travel time \(L_c/c\). An energetic return here is not evidence that a wave has completed an outward–around–inward spatial journey.

### Capacity and geometry

Carry forward the conserved \(Z_2=\sum_i\Omega_i^2\) and the coherent-span ceiling on **net extraction relative to initial core trial storage**. The approximately 3.4074% bound for initial span at most \(\pi/12\) is not an attained fraction, a gross-throughput bound, a receiver share or the author's tentative diversion share. A later gain in \(H_N\) is compatible with that invariant.

The author's intended picture remains a central starting/meeting region, opposed upward/downward cones, outward spreading and curvature around an intended tight toroidal arrangement, inward return, and possible transfer elsewhere. The rough 15–20%, possibly more, is intuition rather than a measured or fitted target. Stationary support lines remain stationary.

The adopted one-dimensional circle, intended tight toroid, close original enclosing sphere and extended-line sphere remain distinct. The selected finite host-notch regions \(N\) differ from the six central broken boundaries \(G_k^\pm\). No new receiving location, central chord, six-port map or physical energy unit is selected by this investigation. The circle's exclusion of exact \(O\) is not an exclusion of every finite central starting/meeting region.

## 7. Research agenda and collaboration

The approved order remains:

| Priority | Direction | Meaning of the next step |
| --- | --- | --- |
| Completed | Reciprocal chiral exchange paper and closeout | Preserved mathematical baseline at its accepted scope. |
| 1, this investigation | Same-trajectory native credit | One admissible empty launch with later total negative native power, or a precise scoped obstruction/condition. |
| 2 | Accessible transfer and receiver behavior | Determine reachable storage, charging/backflow, transient retention and parameter dependence. The invariant ceiling alone does not establish attainability. |
| 3 | Candidate under native stepping | Study \(F\)-jumps and exchange cadence after exchange-only behavior is understood; track the exact native baseline increment and domain. This is the hybrid part of accessible-transfer work. |
| 4 | Natural core motion and intended route | Connect state exchange to the central meeting region, opposed cones, outward–around–inward route, spatial receiving locations and stationary supports. |
| 5 | Six-opening transport correspondence | Assess how the three upper and three lower central broken boundaries enter a justified route or transfer description. |
| Linked across these | Gravity–magnetism correspondence | Continue toward justified source, force, units, response and motion relations; naming a trial storage does not settle these. |
| Later standing direction | Outer Tri-Octagon geometry | Decagonal boundary, separate golden-ratio relationships, larger shells and the close original enclosing sphere. |
| Later standing direction | Further justified SRG integration | Reuse the seven completed reconstructions, Volumes I–III and Final Mathematical Bridge without reopening their completed work. |

Explicit exchange improvements and an irreversible receiving model remain possible later proposals when evidence makes them useful. Preserve this first candidate as a comparison. TORMENT, intelligence/memory, epistemic dynamics and game/embodiment remain parallel interests; Three-Way remains parked.

GPT leads formulation and review; Codex independently challenges the bounded mathematics. The author welcomes clearly labelled interpretations and improvements. Routine analytical choices, source recovery and exact algebra can proceed autonomously. Ask for geometric intuition only when genuinely different spatial interpretations remain, a new geometric assumption is required, or a proposed connection changes the intended direction. Present the concrete relation and choice first.

**No author-side geometric decision is required to assess the proposed certificate.** The meaningful later discussion will be what this verified mode of exchange tells us about the desired route and which spatial relationship to investigate next.

## 8. Source identities for the defining analytical inputs

These SHA-256 values identify the exact publication files used for GPT's source assessment. They are included to make this one assignment independently reproducible.

| File relative to the edition | SHA-256 |
| --- | --- |
| `manuscript/candidate.tex` | `babb811ccf53415dc77c19c3f00c7a281924713728d6816f9478f2522e2c43e5` |
| `manuscript/power.tex` | `2d302fb32d0a5e825ae4929e7cc1e7aceb4772937cc5457bed951e717a2cfc89` |
| `manuscript/wellposed.tex` | `0cb9c047931c4b2c8484012ade0799417bee4168e5d6fc8de3a1b9e951636895` |
| `manuscript/activity.tex` | `da5a775458e50475d37a280770302fe46742efa88f4a0c8db8dacf97adcc5054` |
| `manuscript/capacity.tex` | `b5a67749c6b1f4a313ef34e7e82d6a7b28e0fd770c43dded6692655d9f0749be` |
| `manuscript/interpretation.tex` | `c55dd6c7179483d8720f13d72ccc363802a39cdbe6d0258043854c69c7af939c` |
| `evidence/accepted_proof.md` | `ea3e40a0bd3de11308771a9cd83600912b449534808a1d540bb489b45d7edb86` |

The full handoff's `SOURCE_MAP.md` supplies prior publication identities and the Windows source route. This order supplies the new scoped question and proposed proof; the published paper supplies the baseline equations and accepted earlier results.
