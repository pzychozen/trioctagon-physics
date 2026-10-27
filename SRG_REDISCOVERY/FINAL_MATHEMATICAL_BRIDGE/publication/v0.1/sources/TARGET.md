# Bridge IV-B Target B — corrected proof reconstruction and GPT review

Date: 2026-09-22  
Author: GPT  
Status: **NEW GPT DERIVATION FROM RECOVERED SOURCES; AWAITING BOUNDED INDEPENDENT CODEX REVIEW**

This is not the missing Claude prose note. Claude's retrieval report says that note was never written. This document supplies a new, explicitly attributed mathematical write-up of the recovered Target B calculation, including corrections and two restricted arguments supplied here. It does not replace a historical source, change a kernel, or claim that the complete physical interface has been derived.

## 0. Sources, identity, and what was executed

The supplied three-entry manifest matches all three uploaded files:

| Source | SHA-256 |
|---|---|
| S1 — `b1_handoff.py`, 176 lines | `6ebd0b608b0fb1a3eeb8aaa5fb2cd993139cab56924cb6dff7185c530222dd8e` |
| S2 — `b1_handoff_stdout.txt` | `16995a8ff310c19319cfcbe7831cf7cecb61b2c2cd3fcbc41e14a91d1dd78234` |
| S3 — `RETRIEVAL_REPORT.md` | `6963889990f783d6551c3ac994e1a8d243ea8744a364df54ef24e05508055d61` |

The source-to-model reference is the supplied `KERNEL_SOURCE_TO_MODEL(2).md`, especially §§3.1–3.3, 9, and 10.3. Its equation (30) and earlier reviewed IV-A/R1 factorization are reused. The S1 operator construction is not a derivation of that historical factorization from its original four factors.

The user reports that the canonical Windows location is now `C:\TORMENT\TRIOCTAGON_new\reconstruction\bridge_IV_B\`. S3's original export-location wording predates the reported move. No Windows filesystem or Git state was inspected by GPT; no commit claim is inferred from a local-save report. There is no reason to move the files again or delete the empty predecessor directory for this task.

After reading S1, GPT re-executed it unchanged in a separate process, with bytecode writing disabled. It printed 18 passes: **17 computational conditions and one literal-True documentary assertion**. This reproduces the conditions, not all the theorem claims embedded in their messages. All original uploaded files remain byte-identical.

GPT separately constructed exact symbolic Fourier/projector identities and narrowly chosen numerical diagnostics without importing either kernel or S1's implementation helpers. The supporting verifier records 14 checks: five symbolic, seven numerical/predicate-audit checks, and two execution/integrity checks. Those counts are not numbers of independent theorems. Runtime: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0.

Supporting artifacts, separate from the originals:

- `verify_target_b_review.py`
- `execution/target_b_review_results.json`
- `execution/gpt_original_b1_reexecution_stdout.txt`

The original script and supplied stdout are evidence of their respective executions. A new run is not a reconstruction of the old session's exact execution history.

## 1. Model placement and hypotheses

This packet concerns the **fixed six-state SRG** and its potential connection to the deterministic Paper-A three-channel map. It does not substitute the January field REFU, dynamic REFU memory, RSB tensor, portal prototype, or TORMENT memory subsystem for that operator.

Use the code's helicity-major tensor order

\[
\mathcal H=\mathbb C^2\otimes\mathbb C^3.
\]

Writing the source factors in the opposite tensor order requires the corresponding tensor-swap change of coordinates; it is not permission to swap matrix multiplication order.

Let

\[
\omega=-\frac12+i\frac{\sqrt3}{2},\quad
f_0=\frac{(1,1,1)^T}{\sqrt3},\quad
f_1=\frac{(1,\bar\omega,\omega)^T}{\sqrt3},\quad
f_2=\bar f_1,
\qquad p=f_0f_0^\dagger.
\]

These conventions agree with S1:16–38. Let

\[
q=e^{-\eta},\quad r=e^{\gamma},\quad c=1-\lambda_c,
\]
\[
R=qI+(r-q)p,\qquad C=cI+(1-c)p,\qquad
\mathsf Z=\operatorname{diag}(1,\bar\omega,\omega),\qquad A=R\mathsf ZC,
\]
\[
B=e^{-i\alpha\sigma_z}e^{-i\beta\sigma_x},\qquad U=B\otimes A.
\]

The printed parameters are

\[
\lambda_c=.618,\quad\gamma=.577,\quad\eta=.423,\quad
\alpha=2\pi(.244),\quad\beta=\pi(.244).
\]

Analytic statements interpret those decimal literals as the stated real parameters, not as names for nearby irrational constants. Their floating-point realizations are treated separately in the checks. Thus at this source point

\[
c=191/500>0,\qquad q,r>0.
\]

Statements about a complete three-mode cycle require nonzero cycle weights, in particular \(c\ne0\). At \(c=0\), annihilation interrupts it. The simple non-equality with a function of \(L_3\) below only needs \(q>0\).

For the downstream comparison use exactly S1:94–102: no forcing, noise, subsequent normalization, physical-time rescaling, or added clock. With real finite \(\varepsilon,g,\lambda_p,k_j\),

\[
F_{\rm TO}(v)=S_{\lambda_p}\!\left(v+\varepsilon v\odot(k-|v|^2)+gL_3v\right),
\qquad L_3=\mathbf1\mathbf1^T-3I=-3(I-p).
\]

\(S_{\lambda_p}\) is the written simultaneous harmonic-three phase update, preserving every component modulus, with the stated exact-zero convention. \(\lambda_p\) is the downstream synchronization coefficient, not the SRG compression parameter \(\lambda_c\).

## 2. Claim group I — weighted cycle and exact helicity reduction

### 2.1 The weighted mode cycle

The Fourier vectors are orthonormal and

\[
L_3f_0=0,\quad L_3f_1=-3f_1,\quad L_3f_2=-3f_2.
\]

Moreover \(\mathsf Z f_j=f_{j+1\pmod3}\). The compression C acts as 1 on \(f_0\) and c on its complement; R acts as r on \(f_0\) and q on its complement. Applying them in their actual order gives

\[
\boxed{Af_0=qf_1,\qquad Af_1=qcf_2,\qquad Af_2=rcf_0.}\tag{G1}
\]

For \(F=[f_0\ f_1\ f_2]\),

\[
F^\dagger AF=
\begin{pmatrix}0&0&rc\\q&0&0\\0&qc&0\end{pmatrix},
\qquad A^3=DI,\qquad D=rq^2c^2=\det A.
\]

This is the exact algebra behind B1.2/B1.3, already present in the prior reviewed fixed-SRG structure. It is not a new connection to spatial octagonal vertices.

### 2.2 Exact projection to a helicity eigenmode

For a normalized eigenvector \(\chi\) of the unitary B, write

\[
B\chi=\lambda_\chi\chi,\quad |\lambda_\chi|=1,\quad
\Phi_\chi=\langle\chi|\otimes I_3.
\]

Unitarity gives \(\langle\chi|B=\lambda_\chi\langle\chi|\). Therefore

\[
\boxed{\Phi_\chi U=(\lambda_\chi A)\Phi_\chi.}\tag{G2}
\]

The right inverse \(T_\chi v=\chi\otimes v\) satisfies \(\Phi_\chi T_\chi=I\). Hence \(\Phi_\chi\) is surjective.

For this chosen projection, if any map G satisfies \(\Phi_\chi U=G\Phi_\chi\) on all of \(\mathcal H\), evaluate at \(T_\chi v\) to obtain \(G(v)=\lambda_\chi Av\) for every v. That is the correct rigidity claim.

Within the ansatz \(\Phi=\langle\chi|\otimes I\) and target \(\lambda A\), necessity follows from

\[
(\langle\chi|B-\lambda\langle\chi|)\otimes A=0.
\]

Since A is nonzero, the row factor must vanish. Random samples are not needed to prove necessity. At the printed B there are two eigenmodes; for a degenerate B the statement should be about its eigenspaces, not universally about exactly two possible projections.

**Scope correction to B1.6/B1.9.** A different surjection need not induce the identical matrix \(\lambda_\chi A\) in these coordinates. For example, an invertible change T gives \(\widetilde\Phi=T\Phi_\chi\) and induced map \(T(\lambda_\chi A)T^{-1}\). Thus cycling versus fixing these particular named Fourier lines is not, on its own, a proof against all surjective linear maps. The all-surjective result at the supplied source point needs the independent argument in §3.3.

## 3. Claim group II — comparison with Paper-A dynamics

### 3.1 What the symmetric-k test actually establishes

Assume \(k=(k_0,k_0,k_0)\), as the artifact does. For \(v=a f_j\), every component has squared modulus \(|a|^2/3\). Let \(\ell_0=0\) and \(\ell_1=\ell_2=-3\). The pre-sync update is

\[
V=d_j(a)\,a f_j,\qquad
 d_j(a)=1+\varepsilon(k_0-|a|^2/3)+g\ell_j.
\]

When nonzero, its phase differences are still multiples of \(2\pi/3\); a negative real d adds only a common phase of \(\pi\). All harmonic-three sine increments vanish. At d=0 all components are zero. Thus

\[
\boxed{F_{\rm TO}(a f_j)=d_j(a)\,a f_j.}\tag{G3}
\]

This proves **invariance of three complex lines**. Where output is nonzero it also proves fixed projective classes. It does not prove constant amplitude, a stationary U(1)-relative equilibrium at every amplitude, transverse stability, attraction, or completeness of the set of relative equilibria.

For a U(1)-relative equilibrium at a particular nonzero amplitude one additionally needs \(|d_j(a)|=1\). For real d this is d=1 or d=−1. B1.7's actual fixture has multipliers 1.108, .748, .748, so it does not satisfy that extra condition. Its direction test succeeds while its amplitude changes.

The equal-k hypothesis is also required by the invariant-mode interpretation in **B1.11**, not only B1.7 and B1.9. The source-to-model default is the unequal scaled triplet. A state on one of these lines remains a legitimate downstream input at unequal k, but the invariant-line conclusion does not transfer. The independent default-fixture check gives an off-line norm of about .123653 for each normalized mode after one step; this is a counterexample, not a scan.

### 3.2 The direct chosen-projection mismatch is exact

Any spectral function h of \(L_3\) preserves \(\mathbb C f_0\), whereas \(\lambda_\chi Af_0=\lambda_\chi qf_1\ne0\). Therefore

\[
\lambda_\chi A\ne h(L_3).
\]

In particular it is not \(I+gL_3\). This establishes B1.8 in its precise same-coordinate/map class with finite real SRG exponents. \(I+gL_3\) is the downstream linear subcase with both the cubic and phase correction removed; it should not be called the universal linearization of the full map.

### 3.3 A correct global no-go at the supplied fixed-SRG parameter point

**New GPT argument, replacing B1.9's insufficient inference.** For the supplied fixed U and the deterministic F above, there is no fixed complex-linear **surjection** \(\Phi:\mathcal H\to\mathbb C^3\) satisfying

\[
\Phi U=F_{\rm TO}\Phi
\]

on the entire vector space, for any of the real finite downstream parameters covered here.

**Case A: \(\varepsilon\ne0\).** Surjectivity gives a complex-linear right inverse T. The asserted equality would imply \(F_{\rm TO}=\Phi U T\), so F would be complex-linear.

Set \(M=I+\varepsilon\operatorname{diag}k+gL_3\) and \(N(v)=v\odot|v|^2\). Since phase synchronization preserves norm, for positive real t and v nonzero,

\[
\|F_{\rm TO}(tv)\|=\|tMv-\varepsilon t^3N(v)\|,
\quad
\lim_{t\to\infty}\frac{\|F_{\rm TO}(tv)\|}{t^3}
=|\varepsilon|\,\|N(v)\|>0.
\]

A linear map scales only as t. This is a contradiction, with no equal-k assumption and no restriction to one test amplitude.

**Case B: \(\varepsilon=0\).** For every g and \(\lambda_p\), the downstream map fixes the nonzero state \(f_0\): the Laplacian term is zero and all phases are equal.

At the supplied SRG point,

\[
D=e^{-269/1000}(191/500)^2\in(0,1),
\quad U^{3n}=D^n(B^{3n}\otimes I).
\]

Because B is unitary, \(U^{3n}\psi\to0\) for every \(\psi\). Choose \(\psi\) with \(\Phi\psi=f_0\). Iterating the alleged intertwining identity yields

\[
f_0=F_{\rm TO}^{3n}(f_0)=\Phi U^{3n}\psi\longrightarrow0,
\]

again a contradiction.

The zero map is not excluded by the words “no linear map” without qualification; surjectivity is essential to the theorem just stated. This theorem concerns fixed global linear surjections and raw, same-step evolution. It says nothing against nonlinear readouts, restricted state families, normalized dynamics, a selected switch-time initialization, or different time-sampling conventions. It is not a physical impossibility theorem and does not identify other historical SRG variants with this U.

**Separate correction to B1.10.** A nonzero phase coefficient alone does not always make the *composition* nonlinear. If \(\varepsilon=0\) and \(g=1/3\), then \(I+gL_3=p\). Its output has identical components, so synchronization acts trivially and \(F_{\rm TO}=p\) for every \(\lambda_p\). The preceding Case B, not a blanket phase-nonlinearity assertion, covers this case for the supplied U.

### 3.4 One restricted approximation question can also be answered now

S3 correctly reports that the original controlled-approximation branch was never worked. The following is **a new GPT bound**, not a recovered old result and not a full approximation classification.

Keep the chosen \(\Phi_\chi\), fixed SRG parameters, raw same-step comparison, and symmetric k. At the unit input \(f_0\), orthogonality gives

\[
\left\|(\lambda_\chi A)f_0-F_{\rm TO}(f_0)\right\|^2
=q^2+\left|1+\varepsilon(k_0-1/3)\right|^2
\ge q^2.
\]

The lower bound is q≈.655079 at the supplied source point. As the downstream cubic coefficient tends to zero with the other objects fixed, the mismatch tends to \(\sqrt{1+q^2}\), approximately 1.195461, not zero. Thus this particular comparison cannot have a vanishing \(O(\varepsilon^p)\), p>0, error bound on a state set containing that unit mode. This is not a statement about changing \(\Phi\), changing SRG parameters, sampled/normalized models, nonlinear maps, or domains shrinking to zero amplitude.

## 4. Claim group III — an explicit initialization map and its channel geometry

### 4.1 What an initial-state handoff can mean here

The recovered projection gives the following mathematically specified state-preparation family:

\[
H_{\chi,n}(\Psi_0)=\Phi_\chi U^n\Psi_0
=(\lambda_\chi A)^n\Phi_\chi\Psi_0,
\qquad n\in\mathbb N_0.
\]

One may use this output as the initial condition for the separately defined downstream map. That does not require downstream evolution to equal the reduced SRG evolution. At the supplied invertible A, every such fixed-n map is surjective; it does not by itself select a preferred downstream initial state.

For a prepared source state \(\Psi_0=\chi\otimes a f_0\),

\[
A^{3m}f_0=D^m f_0,\quad
A^{3m+1}f_0=D^m qf_1,\quad
A^{3m+2}f_0=D^m q^2cf_2.
\]

Thus it cycles those three channel patterns, with explicit amplitude factors and the scalar helicity eigenphase \(\lambda_\chi^n\). This is the restricted positive content of B1.11. It is not “precisely all Paper-A relative equilibria,” and generic superpositions are not forced onto this three-mode set.

The formal initialization is valid as a vector-space construction even at unequal downstream k. Its interpretation as preparing **invariant** downstream modes requires the equal-k hypotheses in §3.1. No source here fixes the choice of \(\chi\), transfer step n, source preparation, physical normalization, or coupling to an actual face/field. Therefore the construction is not the entire DMQPF/Vesica-to-shell physical interface.

### 4.2 B1.13 is contradicted by the same source operator

Define the source's channel readout

\[
Z_{\rm chiral}(v)=\operatorname{Re}v\times\operatorname{Im}v.
\]

This is the channel readout `Z_chiral`, not the diagonal phase operator \(\mathsf Z\). Direct substitution with the declared channel order gives

\[
Z_{\rm chiral}(f_0)=0,\qquad
Z_{\rm chiral}(f_1)=-\tfrac12f_0,\qquad
Z_{\rm chiral}(f_2)=+\tfrac12f_0.
\]

Since \(Af_0=qf_1\),

\[
\boxed{Z_{\rm chiral}(Af_0)=-\tfrac12q^2f_0\ne0
\quad\text{although}\quad Z_{\rm chiral}(f_0)=0.}\tag{G4}
\]

Therefore the statement that A cannot produce a nonzero handed channel pattern is false for the very A in the script. Complex linearity does not imply preservation of this quadratic readout or preservation of real vectors. For this operator, standard conjugation K also satisfies \(KAf_0=qf_2\ne qf_1=AKf_0\).

After independently normalizing each nonzero pure-mode output, the chiral sequence is

\[
0\ \longrightarrow\ -f_0/2\ \longrightarrow\ +f_0/2\ \longrightarrow\ 0.
\]

Without normalization the same signs carry the squared amplitude factors above. The sense of cycling is already encoded by the prescribed \(\mathsf Z\); replacing it with its conjugate reverses the first splay direction. This is not a demonstration of spontaneous physical chirality, stable sign selection, physical angular momentum, or an E6/E8 action. It is an exact statement about the existing channel-space observable and operator.

The projection makes `Z_chiral` well-defined on its output. That is not an independently specified conservation law on the original six-state space. One can define a pulled-back observable \(Z_{\rm chiral}\circ\Phi_\chi\), but it is not thereby unchanged by U.

## 5. Disposition of the recovered predicate messages

| Identifier | Disposition |
|---|---|
| B1.1 | Retain the exact Fourier/Laplacian identities. |
| B1.2–B1.3 | Retain the weighted-cycle and cubic identities; distinguish the nondegenerate cycle from c=0 annihilation. |
| B1.4–B1.5 | Retain the eigenmode projection and necessity within its written ansatz; use the algebraic proof, not random sampling as necessity. |
| B1.6 | Rigidity is for the selected projection. Arbitrary coordinate changes induce conjugate target maps, not necessarily the identical matrix. |
| B1.7 | Three invariant complex lines under equal k, not arbitrary-amplitude U(1)-relative equilibria or a stability/completeness theorem. |
| B1.8 | Direct non-equality with spectral functions of L3 in the chosen coordinates is valid; qualify “linearization” and the parameter domain. |
| B1.9 | Its general-surjection inference is insufficient. Its modulus-only condition cannot distinguish the Fourier modes and even passes with A replaced by identity. §3.3 supplies a separate proof at the actual SRG point. |
| B1.10 | Nonzero cubic coefficient supplies the scaling obstruction. Nonzero phase coefficient alone has exceptions. The source-point contraction argument covers the remaining case here. |
| B1.11 | Retain the pure-mode orbit and explicit initialization family. Apply equal-k to any invariant-downstream-mode assertion; do not claim a completed physical boundary interface or all relative equilibria. |
| B1.12, six conditions | Preserve the concrete conditions. An invertible nonunitary 3×3 matrix does not establish SU(3) dynamical symmetry. The written C3 relation is phase-weighted covariance, not commutation. Determinant magnitude alone is not a proof that every vector contracts. B's unitary/helicity and the phase-shift identities have their stated algebraic meanings. |
| B1.13 | Documentary condition is literally True and the no-generated-chirality sentence is contradicted by (G4). Replace that conclusion in the accepted account, not in the preserved original script. |

For the specific source A, singular values are the absolute cycle weights q, qc, rc; all are below one at the printed point. That stronger source-point contraction can be checked directly, but it is not what a determinant-only predicate proves. No SU(3) physical interpretation follows from calling the target vector space a carrier.

## 6. What this changes in the scientific record

1. The missing prose note was not recovered; Claude reports it was never written. The script is the historical computational artifact now in hand. Further searches for that prose note are not the next task.
2. The exact helicity-sector reduction to \(\lambda_\chi A\) is supported by an explicit proof. It is a real evolution-preserving reduction, with the target correctly named.
3. The target is not the global Paper-A dynamics under the fixed global linear-surjection comparison. This does not prevent the former from supplying an initial state for the latter.
4. The familiar invariant-line interpretation needs equal k. The original default unequal k remains unchanged.
5. A limited initial-state construction and an exact channel-chirality cycle are retained. The claim that A is incapable of producing channel chirality is not retained.
6. The broad controlled-approximation problem was not solved in the original work. §3.4 now resolves one explicitly fixed-projection small-cubic route, not all such questions.

The actual upstream preparation and physical face/field attachment are still separate interface questions. No conclusion here resets the mapped RSB, portal, memory variants, folded shell, or Papers A/C.

## 7. Bounded Codex handoff — same Target B, not a new campaign

Save this GPT-authored note and its supporting artifacts under the existing `reconstruction\bridge_IV_B\` location, preserving author and original-source distinctions. Review the three claim groups in §§2–4 against S1 and the already accepted fixed-SRG definitions. Independently verify the short algebraic arguments and targeted counterexamples; a repeat of S1's 18 passes is not a substitute.

Add an attributed Codex review disposition to this same proof note, and update the existing `KERNEL_SOURCE_TO_MODEL.md` and recovery record with the precise outcomes and source paths. Record source corrections separately from GPT's new global-surjection proof and limited approximation bound. Do not claim prior Claude authorship or joint acceptance of unreviewed additions.

No new corpus search, E8 work, Target A/C work, model redesign, kernel edit, further folder reorganization, archive, broad simulation, commit or push. No deletion task is needed for the empty old directory. Describe local saves as saves; if earlier Git commits are asserted, identify the actual repository and SHA through a bounded read-only check rather than inferring them from prose. Do not create a commit to make an earlier claim true.

Exit: one reviewed Target-B proof note and the two existing record updates. A restricted initialization result is a legitimate outcome; it must not be inflated into complete evolution equality or a physical host construction.


## 8. Independent Codex review disposition — 2026-09-22

Reviewer: **Codex**. Status: **ACCEPTED WITH THE EXPLICIT SCOPE BELOW; BOUNDED TARGET-B REVIEW COMPLETE**. This section supersedes the opening awaiting-review status. The preceding GPT-authored note remains an unchanged 21,586-byte prefix, SHA-256 `bbe9b8b3361144297406acbbe41c12825f5065f34ca76ecea8df54d9b58bf498`. The derivations in §§3.3–3.4 and the presentation/counterexample remain attributed to GPT; this is Codex's independent assessment, not a recovered Claude proof note or a claim of broader joint acceptance.

### 8.1 Scope, local paths and independent method

All three S1–S3 entries match the [supplied manifest](C:/TORMENT/TRIOCTAGON_new/reconstruction/bridge_IV_B/SHA256SUMS.txt). Codex inspected the actual [S1 script](C:/TORMENT/TRIOCTAGON_new/reconstruction/bridge_IV_B/b1_handoff.py), [supplied stdout](C:/TORMENT/TRIOCTAGON_new/reconstruction/bridge_IV_B/b1_handoff_stdout.txt) and [retrieval report](C:/TORMENT/TRIOCTAGON_new/reconstruction/bridge_IV_B/RETRIEVAL_REPORT.md). Operator order, tensor order and parameters agree with equation (30) of the existing [source-to-model record](C:/TORMENT/TRIOCTAGON_new/reconstruction/KERNEL_SOURCE_TO_MODEL.md) and §3 of the already accepted [IV-A digest](C:/TORMENT/TRIOCTAGON_new/reconstruction/continuity_closeout_20260922/BRIDGE_IV_A_ACCEPTED_RESULTS_v0.2.md). The modern deterministic dynamics module was read as source to compare its update and exact-zero convention; it was not imported or executed. This review reuses the accepted factorization and does not rerun IV-A.

This proof note and its three GPT supporting files are actually saved together in **research/GPT_proof**. The local links are [GPT verifier](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/verify_target_b_review.py), [GPT results](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/target_b_review_results.json), and [GPT unchanged-original re-execution stdout](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/gpt_original_b1_reexecution_stdout.txt). The earlier `execution/` relative paths and §7 relocation instruction are superseded for this local handoff by these actual paths and the user's instruction that no further moves are needed. The original S1–S3 package remains at **reconstruction/bridge_IV_B**. No file or folder was moved and no empty directory was removed.

Codex inspected S1 and the GPT verifier before running a separate [independent verifier](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/codex_target_b_review_20260922/verify_target_b_codex.py). Its exact checks use rational coefficient arithmetic in \(\mathbb Q(\omega)\), with \(\omega^2+\omega+1=0\), and polynomial coefficients in q,r,c. Using the unnormalized Fourier columns \(G=\sqrt3F\), \(G^\dagger G=3I\), avoids approximating \(\sqrt3\) in the algebraic identities. NumPy is used only for the separately labelled numerical witnesses. The [Codex results](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/codex_target_b_review_20260922/codex_target_b_results.json) and [Codex stdout](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/codex_target_b_review_20260922/codex_target_b_stdout.txt) are new, separately attributed outputs. Runtime: Python3.12.14, NumPy2.3.5; bytecode writing disabled.

**19/19 supporting checks pass:** ten exact algebra/inequality checks, eight numerical or predicate-audit checks, and one manifest/documentary audit. This is not a count of theorems. The proof review below is necessary for statements quantified over all states and parameters. Neither the GPT verifier nor S1 was rerun by Codex; their supplied output is attributed execution evidence. S3 §8 explicitly identifies its stdout as an unchanged-script re-execution, not the first session's captured stdout. That supplied text equals GPT's separate re-execution text. The original count is **17 computational conditions plus one literal-True documentary assertion**, with B1.13 at source line167. It does not prove the false chirality sentence.

### 8.2 Claim group I — accepted exact helicity-sector reduction

**Accepted:** the weighted cycle (G1), \(A^3=rq^2c^2I\), the corresponding determinant, and the exact projection (G2), with the stated nondegeneracy qualifications. The independent verifier checks the coefficients of \(F^\dagger AF\) and \(A^3\) symbolically, rather than evaluating only the printed parameter point. At c=0 it separately confirms the nonzero square-zero map and consequent interrupted cycle.

For clarity about the eigenvalue in the bra identity, normality of the unitary B gives \(B^\dagger\chi=\bar\lambda_\chi\chi\), hence \(\chi^\dagger B=\lambda_\chi\chi^\dagger\). Thus both
\[
\Phi_\chi U=(\lambda_\chi A)\Phi_\chi,\qquad
UT_\chi=T_\chi(\lambda_\chi A),\qquad
\Phi_\chi T_\chi=I
\]
hold, where \(T_\chi v=\chi\otimes v\). This is a genuine invariant helicity-sector reduction. For the chosen surjection the target is unique, even if an arbitrary target G was initially allowed: composition with \(T_\chi\) forces \(G=\lambda_\chi A\). The necessity claim is confined to the tensor-product row ansatz; a nonzero A makes its row-factor argument valid. The two printed eigenmodes mean two eigenlines, with the usual arbitrary eigenvector phase, not exactly two normalized vectors.

**Accepted source correction:** a different surjection can induce a conjugate matrix in different target coordinates. S1's named-line cycling argument alone does not establish a theorem about every linear surjection. The same-coordinate non-equality \(\lambda_\chi A\ne h(L_3)\) is nevertheless exact because \(h(L_3)\) preserves \(\mathbb C f_0\) and \(Af_0=qf_1\ne0\). This is a mathematical distinction between targets, not a reason to deny the reduction.

### 8.3 Claim group II — accepted GPT proofs with the stated map class

**Invariant lines and source-message corrections accepted.** Under equal k, (G3) follows from equal component intensities and the vanishing harmonic-three phase increments. A negative real multiplier supplies a common phase reversal; zero output has no projective class. A U(1)-relative equilibrium at a nonzero amplitude additionally requires \(|d_j(a)|=1\). The printed fixture instead gives multipliers 1.108, .748, .748. Codex independently reproduces these and separately checks the negative-multiplier and exact-zero branches.

The supplied unequal-default-k fixture yields off-line norm **0.12365280750667096** for each normalized Fourier mode after one step, confirming that the default fixture does not inherit those invariant lines. The equal-k hypothesis is the sufficient symmetry hypothesis used for the nonzero-cubic comparison; it must not become an unconditional necessity statement when \(\varepsilon=0\), since k then drops out. This qualification changes neither the printed counterexample nor the proofs.

**GPT §3.3 global-surjection theorem accepted.** Its proof repairs the missing quantifier in B1.9:

- If \(\varepsilon\ne0\), a global complex-linear surjection has a linear right inverse T, so intertwining would make \(F_{\rm TO}=\Phi UT\) linear on all \(\mathbb C^3\). Phase synchronization preserves norm even at zero components. For any nonzero v, the cubic term gives \(\|F_{\rm TO}(tv)\|/t^3\to|\varepsilon|\|v\odot|v|^2\|>0\), contradicting linear growth. No equal-k assumption enters this case.
- If \(\varepsilon=0\), \(f_0\) is fixed for every g and phase coefficient. At the supplied SRG point, \(0<D=e^{-269/1000}(191/500)^2<1\) and \(U^{3n}=D^n(B^{3n}\otimes I)\). A preimage of \(f_0\) under a surjective \(\Phi\) would therefore project both to the fixed \(f_0\) and to a sequence tending to zero. That contradiction also covers \(\varepsilon=0,g=1/3\), where the full downstream map is exactly p despite a nonzero phase coefficient.

These arguments concern the exact mathematical formulas on their whole vector spaces, with fixed finite real parameters, raw same-step comparison and a fixed complex-linear surjection. They do not assert bitwise equality or behavior beyond a numerical implementation's representable range. They do not exclude state preparation, maps on restricted domains, nonlinear projections, normalization, or different time sampling. The zero map is outside the asserted surjective class. Neither the original invariant-line comparison nor a bare nonzero phase coefficient suffices for this global result.

**GPT §3.4 restricted approximation bound accepted.** For the chosen helicity projection, fixed SRG parameters and symmetric k, the orthogonal components at unit \(f_0\) give
\[
\|(\lambda_\chi A)f_0-F_{\rm TO}(f_0)\|^2
=q^2+|1+\varepsilon(k_0-1/3)|^2.
\]
Its q lower bound rules out a vanishing \(O(\varepsilon^p)\), \(p>0\), error on a domain containing that state while the other stipulated objects stay fixed. Codex obtains q=0.6550786331118063, the printed-\(\varepsilon=.3,k_0=1\) mismatch 1.3671605668536644, and the \(\varepsilon=0\) mismatch 1.1954614237020085, each agreeing with the formula within \(2.23\times10^{-16}\). This resolves only that approximation route. It is a new GPT bound, not a result recovered from the missing historical note.

### 8.4 Claim group III — accepted preparation family and opposite channel orientations

**Accepted positive handoff:** for fixed normalized helicity eigenvector \(\chi\) and transfer step \(n\ge0\),
\[
H_{\chi,n}=\Phi_\chi U^n=(\lambda_\chi A)^n\Phi_\chi.
\]
At the supplied invertible A it is surjective. An explicit right inverse, making that statement concrete, is
\[
J_{\chi,n}(v)=\chi\otimes(\lambda_\chi A)^{-n}v,\qquad
H_{\chi,n}J_{\chi,n}=I.
\]
This is an immediate consequence of GPT's formulas, made explicit here by Codex. It shows that a desired downstream vector can be prepared once \(\chi,n\) and the source state are chosen; it does not select those choices. The independent n=2 numerical witness has maximum right-inverse error \(1.23\times10^{-15}\).

For source preparation \(\chi\otimes a f_0\), set
\[
b_{3m}=D^m,\quad b_{3m+1}=D^m q,\quad b_{3m+2}=D^m q^2c.
\]
The reduced output is \(a\lambda_\chi^n b_n f_{n\bmod3}\). Since
\[
Z_{\rm chiral}(zv)=|z|^2Z_{\rm chiral}(v),
\]
its unnormalized readout is exactly
\[
|a|^2|b_n|^2
\begin{cases}
0,&n\equiv0\pmod3,\\
-f_0/2,&n\equiv1\pmod3,\\
+f_0/2,&n\equiv2\pmod3.
\end{cases}
\]
For a nonzero prepared state, normalizing each output removes the positive amplitude factor and gives the claimed \(0\to-f_0/2\to+f_0/2\to0\) cycle. The exact rational-field check verifies the signs in the declared channel order. In particular, \(Z_{\rm chiral}(Af_0)=-q^2f_0/2\ne0\), refuting S1 B1.13's no-generated-channel-chirality statement. Standard complex conjugation also fails to commute with this A on \(f_0\). Merely defining a pulled-back observable does not make it conserved.

This is a concrete cycle through opposite orientations of the **channel readout**. The phase direction is imposed by \(\mathsf Z\); it is not spontaneous physical chirality, a stable sign selection, a spatial shell construction or a physical angular-momentum identification. Z_chiral has no imposed decay envelope; need not decay in general. On this particular prepared raw SRG orbit its nonzero values do decay through the displayed \(D^{2m}\) factor. A trajectory-specific decay result does not restore the earlier blanket decay claim.

### 8.5 Corrections, provenance and bounded exit

The dispositions in §5 are accepted with the qualifications above. In particular, B1.12's phase-weighted covariance, selected-channel transition and ordinary matrix properties are retained without promoting them to SU(3) dynamical symmetry or a physical helicity identification. Independent singular values are approximately (0.6802229476370523, 0.6550786331118061, 0.2502400378487101); their being below one confirms contraction at this source point. A determinant-only predicate would not prove that all vectors contract.

The historical computational claims, GPT's new proofs and counterexample, and Codex's independent disposition remain distinct. S3 reports that the old prose note was never written; Codex accepts that as the supplied retrieval provenance, not as the outcome of a new search. The missing prose was not recovered by this task. No inference about Targets A/C or the previously bounded E8 question is made.

Bounded read-only Git checks find that **research/GPT_proof** and **reconstruction/bridge_IV_B** are not within Git repositories. These artifacts are local exports/saves; no repository/commit receipt is supplied for them. Modern repository HEAD remains `a0875c493b23b7d1aaa718ea2b40aa17af9adcd2` and historical repository HEAD remains `6310de7ba1ef4f41ed6e7cd683cf9186585cdd11`, with their existing status entries unchanged. No commit was created to support earlier wording.

The [preservation receipt](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/codex_target_b_review_20260922/preservation_results.json) confirms all **167 watched files** retain their SHA-256, byte sizes and exact UTC modification-time ticks, including the 70 tracked modern-repository files, original Target-B artifacts, GPT supporting scripts/results/stdout, and the previous Claude-review verification packet. This note gains only this attributed appendix; the source-to-model record is updated and the existing recovery record receives an append. No folder move, cleanup, source search, E8 investigation, Target A/C work, kernel execution/change, broad simulation, publication task, commit or push occurred.

**Bounded exit achieved:** an exact helicity-sector reduction, explicit surjective state-preparation family and channel-orientation cycle are accepted. GPT's global-surjection obstruction and restricted approximation bound explain why these results do not reproduce Paper-A evolution under the stated comparison. Upstream physical preparation and actual face/field attachment remain separate missing interfaces; no complete physical host or broader joint acceptance is claimed.

