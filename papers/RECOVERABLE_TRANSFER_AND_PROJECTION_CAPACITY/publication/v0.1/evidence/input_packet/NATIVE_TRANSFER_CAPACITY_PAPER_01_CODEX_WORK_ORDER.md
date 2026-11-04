# NATIVE_TRANSFER_CAPACITY_PAPER_01 — Codex manuscript order

**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Date:** 4 November 2026  
**Status:** Author-approved manuscript preparation  
**Working title:** **Recoverable Transfer and Projection Capacity in the Reciprocal Chiral Exchange Candidate**

## 1. Execute the approved manuscript direction

Prepare one complete mathematical research manuscript combining the two accepted investigations:

- **NATIVE_ACCESSIBLE_TRANSFER_01 (AT01):** actual finite-coupling transfer, temporary receiver concentration, net native recovery, exact receiver charging/backflow, and explicit small-stock scaling.
- **NATIVE_PROJECTION_CAPACITY_01 (PC01):** the projection invariant, exact native debit identity, sharper all-time capacity ceiling, sharp algebraic minimum, zero-drive equivalence, active strict-improvement witness and finite-time nonattainment example.

Both investigations are **Established with formulas and hypotheses unchanged**, with completed GPT analytical reviews. The author approved writing their combined paper before opening another investigation. Proceed through writing, typesetting, document build, fidelity review and every-page visual inspection without another confirmation. Return the finished manuscript package for GPT/author manuscript review.

The paper's central point is the relationship between **how much of a transferred stock returns** and **how much storage the fixed exchange geometry permits to leave the core**. These are different quantities with different denominators and theorem hypotheses.

This is manuscript production from accepted mathematics. Preserve the complete substantive arguments and improve their presentation. No new scientific investigation, parameter scan, trajectory, optimization or mathematical generalization is requested.

## 2. Inputs, authority and workspace

Start with this order, EDITORIAL_SOURCE_MAP.md and context/RESEARCH_CONTINUITY.md. SOURCE_IDENTITIES.json identifies the exact supplied inputs.

| Input | Role |
| --- | --- |
| published/P1/ | Published reciprocal-exchange edition at commit 273b1a6faaab19ea58748d00576439166eeef9ab: equations, global solutions, balances, initial activity, Z2 and old ceiling |
| published/P2/ | Published same-trajectory native-credit edition at commit 28e8a85c8fe1e6321328d4d7285b2560d1f98aa9: scaled estimates, comparison and sufficient native-credit theorem |
| accepted/AT01/ | Accepted proof, ledger, original review ZIP/checksum, completed GPT review and its replay/evidence package |
| accepted/PC01/ | Accepted proof, ledger, original review ZIP/checksum, completed GPT review and its replay/evidence package |
| context/ | Preserved collaboration/geometry and agenda, plus current manuscript continuity |
| authorization/USER_AUTHORIZATION.json | Current approval of this manuscript direction |

The published dependencies are selected exact source/build/reference files, not a reconstruction of either entire publication archive. Their preserved historical prose and manifest scopes must not be rewritten. Nested archives are supporting evidence; do not recursively rerun their workflows.

Use a fresh research workspace:

    C:\TORMENT\TRIOCTAGON_new\research\NATIVE_TRANSFER_CAPACITY_PAPER_01\

If that path already contains work, preserve it and use a new run subdirectory. Prepare an isolated candidate payload at:

    candidate_edition\papers\RECOVERABLE_TRANSFER_AND_PROJECTION_CAPACITY\publication\v0.1\

The candidate PDF is:

    RECOVERABLE_TRANSFER_AND_PROJECTION_CAPACITY_v0.1.pdf

This is a proposed later publication layout. The current task does not write to the real repository. Keep compiler intermediates and page renders outside the candidate edition.

Use the packet first. Routine recovery from the named existing research directories and supplied Downloads belongs with Codex; do not ask the author to remember coefficients or find evidence already provided.

## 3. Manuscript architecture

State both results and their relationship early. Use a shared **general** model section, then retain separate theorem hypotheses. A suitable order is:

| Part | Content | Accepted coverage |
| --- | --- | --- |
| Introduction | What the published same-trajectory result left open; quantitative recovery and a geometric extraction restriction as the present contributions | AT disposition; PC disposition; both GPT reviews |
| Fixed candidate and inherited foundations | Raw registration, finite profiles, full equations, stores, signed powers and global regularity; separately identify the special launch family | AT01–AT05; PC01–PC02, PC09; P1/P2 |
| Projection capacity | General projection theorem, full-level algebraic minimum, zero-drive equivalence, active coherent witness and finite-time distinction | PC03–PC22 |
| Quantitative transfer theorem | Exact constants, preparation, time landmarks, finite stock bounds, fractions, receiver signs and inherited native-credit witness | AT09, AT13–AT25 |
| Finite-error proof | Exact scaling; inherited bounds; longer-horizon estimate; weighted projections; complete receiver-product estimate | AT06–AT12, AT14–AT25 |
| Amount and interpretation | Explicit finite errors before asymptotics; original accessibility normalization; compatibility with the joint ceiling; scope and brief geometric continuation | AT26–AT29; PC limits |
| Appendix and references | Units or supporting algebra where helpful; exact source locators and reproducibility pointers | Both proofs and ledgers |

Section grouping may be improved without altering scope. A general projection theorem, a separate algebraic-minimum proposition and a quantitative transfer theorem make the logical dependencies clear. Put complete proofs of the new results in the paper. Cite and restate the needed published foundations; reproducing P1's entire well-posedness proof is unnecessary.

Let completeness and readability determine page count. There is no page quota. Detailed hashes, scripts, audit records and the full provenance crosswalk belong in supporting material.

## 4. Shared model and separation of hypotheses

Retain \(x=(a,b)\), \(\Omega=a+ib\), \(f(x)=K(a\times b)\), \(J=D_xf\), the published normals, gains and fixed yaw. Keep the raw two-port order and registration signs. Display the unchanged coupled equations:

\[
\dot x=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\qquad
p_t+c(r_c)_s=\mathcal B\{\eta_N f(x)-\kappa z\},\qquad
(r_c)_t+cp_s=0,\qquad
\dot z=\frac{\kappa}{\beta_R}y,\quad y=\mathcal B^*p .
\]

Retain \(\alpha_N,\beta_R,\eta_N>0\), finite constant \(\kappa=\eta_R>0\), positive fixed registration gains and the resulting fixed real rank-two K. All carrier parameters and profile widths remain finite and admissible.

Define the positive quadratic trial stores, total signed two-port powers and balances. Retain the distinction between \(H_N\) and the native quartic potential. Describe the finite periodic carrier, positive speed, normalized H1 tents and whole-circle shortest-separation condition needed for disjoint support.

Use P1's global solution theorem. For the projection theorem, arbitrary admitted L2 carrier preparations suffice: the native coordinates are C1 and the bounded port output is continuous. For the quantitative theorem, the empty carrier is H1, giving the inherited strong regularity.

**Do not impose empty coherent preparation or the large-coupling certificate on the general model or projection theorem.** Conversely, do not extend the accepted quantitative theorem to arbitrary nonzero-drive native states.

For quantitative transfer retain precisely

\[
\Omega_0=(1,e^{i\phi},1),\quad 0<\phi<\pi/12,\qquad
p(0)=r_c(0)=z(0)=0,
\]
\[
f_{0,\pm}=\frac{G\sin\phi}{\sqrt7}(-2\sin\delta_g\pm\sqrt3),\qquad
|f_0|^2=\frac{G^2\sin^2\phi}{7}(6+8\sin^2\delta_g)>0 .
\]

Fix geometry, profiles, speed, registration, positive scales, native coupling and one admitted phase before choosing receiver coupling. Each trajectory has one finite constant κ; asymptotics compare such solutions with all other parameters fixed. No coherent-sector invariance, native F jump or coefficient switching is assumed.

The abstract must state the specified coherent family with nonzero chiral drive for the quantitative result. The prior MC-01 clarification ruled out replacing that hypothesis by the ambiguous phrase “a nonzero coherent launch.”

## 5. Projection theorem and its complete consequences

Preserve PC03–PC22, including:

\[
e=R_z(-\delta_g)e_x,\quad Ke=0,\quad w=K^Ty\perp e,\quad
h_e=|e\cdot\Omega|^2,\quad
\mathcal J_K=I-2h_e,\quad I=|\Omega|^2,
\]
\[
\dot I=-4\mu w\cdot(a\times b),\quad
\dot h_e=-2\mu w\cdot(a\times b),\quad
\dot{\mathcal J}_K=0,\qquad \mu=\frac{\eta_N}{2\alpha_N},
\]
\[
H_N(0)-H_N(t)=\alpha_N[h_e(0)-h_e(t)].
\]

The scalar is indefinite and distinct from J(x); changing the sign of e changes none of the quantities. It is not an added physical store.

With \(Z_0=Z_2(\Omega_0)\), \(j_0=\mathcal J_K(\Omega_0)\), retain

\[
I(t)\ge\max(|Z_0|,j_0),\quad
C_{\rm joint}=\frac{\alpha_N}{2}[I_0-\max(|Z_0|,j_0)]
=\min\{C_Z,\alpha_Nh_e(0)\},\quad
C_Z=\frac{\alpha_N}{2}(I_0-|Z_0|).
\]

For empty external preparation, \(0\le H_C+H_R=H_N(0)-H_N(t)\le C_{\rm joint}\). For preloaded preparation, the bound concerns signed native debit, equal to external stock **minus its initial value**.

Prove the full-space feasibility/minimum statement:

\[
\{Z_2=Z,\mathcal J_K=j\}\ne\varnothing\iff j\ge-|Z|,\qquad
\min_{\{Z_2=Z,\mathcal J_K=j\}}|\Omega|^2=\max(|Z|,j)
\quad(j\ge-|Z|).
\]

For infeasible pairs the constraint set is empty and no minimum is asserted. Include both accepted equality constructions and their full range of validity, negative j, branch boundaries, Z=0 and native zero. Distinguish \(v^Tv\) from \(v^\dagger v\). The phase choice must explicitly handle Z=0 without division or arg(0). This is a minimum over the full native level set in C3.

Retain \(C_{\rm joint}=0\iff f(x_0)=0\), the empty-launch stationarity/initial-supply consequences, and the preloaded-state qualification. At the single fixed witness yaw π/4, show

\[
0<C_{\rm joint}=\alpha_N(1-\cos\phi)<C_Z,\qquad
j_0^2-|Z_0|^2=4\cos\phi(1-\cos\phi)>0,\qquad
|f_0|^2=\frac{10G^2\sin^2\phi}{7}>0.
\]

Keep the accepted example \(\Omega_0=u+ie\), with real unit \(u\perp e\): a nonzero active state with Z=j=0 whose algebraic minimum is native zero. Include the finite-time nonattainment proof using uniqueness through the actual full state, or the equivalent homogeneous native ODE with the actual continuous coefficient w(t). Leave infinite-time approach unresolved.

Neither the equality constructions nor the strict witness establishes dynamical attainment of C_joint. The example is outside the special coherent family and must be identified accordingly.

## 6. Quantitative transfer: constants, denominators and proof

### 6.1 Preserve the entire finite certificate

Keep all definitions from AT05, AT08–AT09 and AT22–AT23:

\[
\begin{gathered}
R=\sqrt3,\quad k=G\sqrt{8/7},\quad
m=\frac2{3\epsilon_c},\quad d=\frac2{\epsilon_c^3},\quad
F_{\max}=\frac{kR^2}{2},\quad
A=\frac{\eta_N^2k^2R^2mF_{\max}}{4\alpha_N},\\
\omega=\sqrt{m/\beta_R},\quad S=\frac{2\pi}{\omega},\quad
T=\frac{3\pi}{2\omega},\quad
\Lambda=\sqrt{\beta_R}|f_0|,\quad
D=\frac m\omega|f_0|^2=\omega\Lambda^2,\\
B_1=\frac{4c\sqrt d\,|f_0|}{\omega^2},\quad
B_2=\frac{\sqrt m\,AS^3}{3},\quad
\varepsilon_\kappa=\frac{B_1}{\kappa}+\frac{B_2}{\kappa^2},\\
C_1=\frac{3c\sqrt{md}\,|f_0|^2}{\omega^2},\quad
C_2=mAT^3(F_{\max}+|f_0|/3),\\
\kappa_{\rm crit}=\max\{1,4C_1/D,\sqrt{4C_2/D}\},\\
\kappa_{\rm cert}(q)=\max\left\{\kappa_{\rm crit},1,
\frac{2B_1}{q\Lambda},\sqrt{\frac{2B_2}{q\Lambda}}\right\},
\qquad 0<q\le1/5 .
\end{gathered}
\]

Each quantitative solution uses a finite \(\kappa\ge\kappa_{\rm cert}(q)\). The constants are finite, independent of κ and dimensionally commensurate. Retain \(a_\kappa=\eta_N^2/(2\kappa^2)\) and the AT27 auxiliary sum \(L=B_1+B_2\); a notation-only alias such as \(L_{\rm err}\) is permitted if recorded explicitly.

Keep the four distinct landmarks:

\[
t_{\rm q}=\frac{\pi}{2\omega\kappa},\quad
t_\pi=\frac{\pi}{\omega\kappa},\quad
t_{\rm b}=\frac{3\pi}{2\omega\kappa},\quad
t_{2\pi}=\frac{2\pi}{\omega\kappa}=\frac S\kappa .
\]

Define \(E_{\rm out}=H_C+H_R=H_N(0)-H_N\) and \(M_\kappa=\max_{0\le t\le t_{2\pi}}E_{\rm out}(t)\). Do not identify tπ as the actual maximizing time.

Retain the positive intermediate total-stock and receiver lower bounds, the separate carrier bound and endpoint external-stock bound in AT15–AT16. Positivity of both denominators must precede these definitions:

\[
\mathcal S_\kappa=\frac{H_R(t_\pi)}{E_{\rm out}(t_\pi)},\qquad
\mathcal R_\kappa=\frac{H_N(t_{2\pi})-H_N(t_\pi)}{E_{\rm out}(t_\pi)}.
\]

Retain the separately normalized receiver retention \(H_R(t_{2\pi})/H_R(t_\pi)\), the error ratio \(r_\kappa=[\varepsilon_\kappa/(2\Lambda-\varepsilon_\kappa)]^2\), and the accepted absolute recovery lower bound

\[
H_N(t_{2\pi})-H_N(t_\pi)
\ge\frac{2\eta_N^2}{\kappa^2}\Lambda(\Lambda-\varepsilon_\kappa)>0.
\]

The certificate implies

\[
\mathcal S_\kappa,\mathcal R_\kappa
\ge1-\left(\frac q{2-q}\right)^2\ge\frac{80}{81},\qquad
\frac{H_R(t_{2\pi})}{H_R(t_\pi)}
\le\left(\frac q{2-q}\right)^2\le\frac1{81},
\]
\[
P_{CR}(t_{\rm q})\ge\frac{\eta_N^2D}{2\kappa}>0,\qquad
P_{CR}(t_{\rm b})\le-\frac{\eta_N^2D}{2\kappa}<0,\qquad
P_{NC}(t_{\rm b})\le-\frac{\eta_N^2D}{2\kappa}<0.
\]

Explicitly attribute the last native-power inequality to P2's unchanged theorem, with the κcrit hypothesis. The receiver signs are new AT01 conclusions. Include initial activity and the continuous later receiver-backflow interval from AT25; its width has no asserted explicit or uniform positive lower bound. Net recovery does not assert monotonic native recovery throughout the whole interval.

### 6.2 Proof details that must survive condensation

The manuscript must justify the actual finite-coupling conclusion, with these connected steps:

1. Exact finite scaling \(\tau=\kappa t\) and \((p,r_c,z)=(\eta_N/\kappa)V_\kappa\), including the scaled equations. The original system retains c>0.
2. Weighted external norm \(\|V\|_{CR}^2=\|\widehat p\|_2^2+\|\widehat r\|_2^2+\beta_R|\widehat z|^2\), propagation/receiver cancellations and the forced norm inequality. Retain the regularized-norm justification at zero.
3. Conservation/convex-ball estimates and native/drive drift with the accepted factor one-fourth.
4. The explicit sine/cosine comparison, clearly identified as frozen-core and omitted-scaled-propagation comparison.
5. Strong regularity of the difference from the already known exact and comparison solutions, before estimating the L2 residual.
6. Exact negative second-coordinate propagation residual, using only the first weak profile derivative. No second tent derivative or operator-norm limit is introduced.
7. The extended horizon \(0\le\tau\le S\) and absolute sine integral \(4/\omega\), giving the new uniform error \(\sup\|V_\kappa-V_0\|_{CR}\le\varepsilon_\kappa\). This extension must be proved, not obtained by changing the horizon in P2's witness theorem.
8. Separate weighted carrier and receiver projections at π/ω, and the whole comparison-state zero at S. These give the actual positive denominators and stock bounds.
9. The receiver-product error with both linear terms and their cross term, and the correct power factor \(\eta_N^2/\kappa\). Stock scaling has a different factor.
10. Both allocations in κcert, the \(2q+q^2\le11/25<1/2\) margin, the native theorem import, and continuity/uniqueness placing all events on one unchanged solution.

### 6.3 Finite errors and large-coupling interpretation

Retain the explicit AT27 finite errors before stating the AT28 asymptotics:

\[
M_\kappa=\frac{2\eta_N^2\beta_R|f_0|^2}{\kappa^2}+O(\kappa^{-3}),
\qquad E_{\rm out}(t_{2\pi})=O(\kappa^{-4}),
\]
\[
1-\mathcal S_\kappa,\ 1-\mathcal R_\kappa=O(\kappa^{-2}),
\qquad \mathcal A_\kappa\to0.
\]

Here preserve the original definition

\[
\mathcal A_\kappa=M_\kappa/C_{\rm inv},\qquad
C_{\rm inv}=\frac{\alpha_N}{2}(3-\sqrt{9-8\sin^2\phi}).
\]

C_inv equals C_Z for this launch. **Do not silently replace this denominator by C_joint.** The two accepted results can be read together as \(M_\kappa\le C_{\rm joint}\le C_Z=C_{\rm inv}\), by applying the all-time bound on the defined compact window. No new normalized capacity statistic is needed.

The 80/81 recovery guarantee concerns actual intermediate transferred stock, not initial native storage or either structural ceiling. In particular, multiplying 80/81 by C_joint does not give an established recovered amount. Pair high recovery fractions with the small absolute amount and shrinking physical window \(t_{2\pi}/(L_c/c)\to0\). Keep every other parameter fixed in the asymptotic statements; no uniform claim as φ→0 or monotonicity of actual quantities as κ varies is accepted.

## 7. Editorial fidelity, citations and provenance

Prepare a manuscript claim/source ledger and **complete AT01–AT29 / PC01–PC22 crosswalk**. Map all 51 accepted equation groups to the corresponding manuscript statement, proof or inherited citation; grouping shared premises is allowed. Give reverse coverage for every substantive new equation/theorem. Record notation-only aliases.

Apply **E01 in EDITORIAL_SOURCE_MAP.md** in the new manuscript: resolve P2's printed section numbers against the supplied published label record. The original ledgers' P2 section summaries are offset by one. Literal labels, equations, hypotheses and accepted scientific results are unchanged. Preserve the original ledgers exactly; this routine citation repair requires no additional approval.

Keep P1/P2 published sources, accepted AT01/PC01 technical evidence, GPT internal reviews, governing orders and author context in distinct provenance categories. Do not attribute later evidence to a predecessor commit or invent a DOI/published-paper status for either new investigation.

Historical “review pending,” “return remains open” or draft wording in preserved sources remains historical. The new manuscript states that the underlying mathematics is accepted, Codex prepared and checked this manuscript, and review of its final PDF by GPT/the author is pending. Do not claim approval of an unseen PDF. Hilmir retains research authorship; preserve GPT's formulation/internal-review role and Codex's independent investigation/manuscript role.

If evidence counts are mentioned, report **18 AT groups and 12 PC groups separately**, each independently replayed. Replays and document checks do not create additional mathematical identities. Written proofs and cited foundations carry the scientific claims.

Use immutable published references and correct theorem/equation locators. Scientific prose should not contain local Windows paths, ChatGPT download links, hash inventories or workflow logs. Supporting technical records can be cited as such. No new literature survey or broad priority claim is needed.

## 8. Interpretation and geometric continuity

The abstract and conclusion must convey both theorem ranges and the amount/fraction distinction. The general invariant has no large-coupling threshold; the quantitative theorem supplies an explicit sufficient regime for the declared initially empty coherent family.

Retain the accepted limits once in a focused discussion: actual C_joint attainment remains open; sharpness is algebraic; finite-time nonattainment says nothing about infinite-time approach; no exact nonlinear period, exact peak time, monotonic recovery over the whole window, permanent retention, disposal or full-time optimized extraction has been proved. H_N never exceeds its initial stock under empty preparation. Net capacity is distinct from gross repeated positive work.

Do not add a full yaw classification, a small-phase ceiling ratio, a new threshold, a new normalized capacity ratio or a quantitative theorem for arbitrary launches during manuscript writing. If a tempting additional deduction appears, park it in a brief note without expanding this task.

Carry the author's central meeting region, opposed cones, outward spreading and curved around–inward return, stationary supports and possible transfer elsewhere in one concise motivation/continuation paragraph. Preserve the distinctions between carrier circle and intended tight toroid, close original sphere and extended-line sphere, and host-notch N regions and central broken G boundaries. Do not identify e with a physical support, opening, field axis or receiving location. The tentative 15–20%, possibly more, remains geometric intuition.

The later agenda remains useful accessible capacity, native stepping/cadence, intended route correspondence, six-opening transport, linked gravity–magnetism, outer geometry and justified SRG integration. No new geometric choice is needed to write the accepted mathematics.

## 9. Build, verification and deliverables

Use the existing Windows document workflow and supplied prior build examples in a fresh research copy. Record actual interpreter/compiler/font/tool versions. Keep TeX restricted/untrusted, build intermediates external, and use the existing cached resources. Installation, scientific imports and historical suite replay are outside this order.

Complete:

1. **Manuscript fidelity:** all quantifiers, constants, powers, denominators, signs, regularity, equality cases, units and attribution; the complete bidirectional claim crosswalk.
2. **Document build:** readable equations/tables, resolved references, complete bibliography, no missing glyphs or clipped content, and a portable document-only build recipe/helper. Any substantive build warning must be resolved or explained.
3. **Every-page inspection:** render and inspect every page of the final PDF at readable resolution. Bind the record to that exact PDF and source hashes. After a final rebuild, check every resulting page; earlier renders do not verify the changed artifact.
4. **Document structure:** title/author/date/status, fonts, bookmarks/links where used, page count, labels and evidence references. Preserve the accents in the author's name.
5. **Focused preservation and package integrity:** check the supplied input identities actually used, safe unique archive membership, exhaustive self-excluded manifest, CRCs, sizes and hashes. Do not audit unrelated research or expand nested historical archives merely to increase counts.

A figure is optional. If an exact comparison plot is useful, label it throughout as the comparison, with a reproducible document-only plotting source. It must not appear to be an actual finite-coupling trajectory or a spatial toroidal route. No new simulation is needed.

Return:

- The standalone PDF, byte-identical to its packaged copy, with editable LaTeX and bibliography.
- README.md, BUILD.md/build helper, PROVENANCE.md, source identities and the complete manuscript claim/source ledger/crosswalk.
- Both unchanged accepted proofs, ledgers, GPT acceptance records and essential accepted evidence with original archive identities.
- Fidelity, build, document, every-page visual-inspection and focused preservation records tied to the final artifact.
- **NATIVE_TRANSFER_CAPACITY_PAPER_01_REVIEW_PACKAGE.zip** and adjacent SHA-256 checksum. Keep intermediate build products outside the candidate edition; delivery support may include final page renders for review.

Lead the completion response with the title, actual page count and **ready for manuscript review** status, then link the PDF, complete package and checksum. Identify any concrete unresolved issue.

Finish the reviewable manuscript package and stop. This order includes no Git operation, publication, announcement or successor investigation. Routine editorial decisions and E01 are authorized; raise only a genuine mathematical/source conflict, a necessary new assumption or a concrete unresolved build problem after completing unaffected work.
