# Native potential descent: independent proof review

**Task:** NATIVE_ENERGY_RESPONSE_01  
**Date:** 1 November 2026 (Atlantic/Reykjavik)  
**Disposition:** Both target implications verified under their stated hypotheses; the diagonal-balance comparison is verified.  
**Prepared by:** Codex for GPT and Hilmir Frímann Halldórsson / pzychozen. This is the bounded proof-review deliverable, not a manuscript or repository-adoption decision.

## 1. Verdict and exact scope

**Target A is true.** At each admitted strictly normally stable positive in-phase triad profile, the existing native potential strictly decreases under the complete ordered map in a sufficiently small regular neighborhood of its common-phase fixed circle, except on that circle. The proof identifies the potential's actual Hessian, proves strict contraction of that Hessian on the five-dimensional normal quotient, and controls the nonlinear remainder. It does not replace the potential with a fitted Lyapunov form. The neighborhood is an existence result; no numerical radius or extension to other branches or rings is claimed.

**Target B is true with the proposed constant.** For exactly the specified coefficients and the entire closed domain of amplitudes in \([9/10,11/10]\) and ordinary phase width at most \(\pi/12\),

\[
\boxed{\mathcal V(F\Omega)-\mathcal V(\Omega)
\le -\frac{16869}{20000}\|v(\Omega)-\Omega\|_2^2.}
\tag{B}
\]

Equality in the monotonicity statement \(\mathcal V(F\Omega)=\mathcal V(\Omega)\) occurs exactly on \(\{e^{i\theta}r_*\}\), where \(r_*\) is the accepted unique aligned profile in the stated amplitude cube. No root solve is needed. This is a finite-step theorem about the ideal mathematical map, not a floating-point certificate. The coefficient is a valid bound, not a claim of optimality.

**Failed positive diagonal balance can coexist with Target A.** On any admitted weak branch with nonzero leading cycle coefficient, all sufficiently small nonzero heterogeneities have failed diagonal balance and the local potential descent just proved. Arbitrary SPD self-adjointness is still available in this stable triad setting. No particular finite numerical heterogeneity is placed inside an unspecified asymptotic neighborhood.

No candidate formula needed a correction. The proof makes explicit the whole-segment disk bound, the quotient rather than an assumed invariant sum-zero plane, the factor \(1/2\) in second variation, and the stationary-state equality argument. These are proof obligations, not changes to the map, coefficients, potential, or domain.

## 2. Sources and dependency status

All repository sources below were read in place under `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`. They were not imported or executed. Source labels and line locators refer to those local files as read. The work order supplies accepted reading editions `82cab10cbe550f58c43163fb8b05fabdad1b05ae` for S2, `7cc1fa03af589818bcdcfaaac51838cc36c84253` for S3, and `6aa1daec7a25f51f482ff91743b9f9c3e33f476c` as the prior S4 reading context. These are inherited edition identifiers; no Git operation, checkout change, or fresh commit-byte authentication was performed.

| Source | Actual path and precise passage | Status and use here |
|---|---|---|
| Order | [NATIVE_ENERGY_RESPONSE_01_CODEX_WORK_ORDER.md](C:/Users/Notandi/Downloads/NATIVE_ENERGY_RESPONSE_01_CODEX_WORK_ORDER.md) | User-authorized bounded assignment. Its proposed deductions are reviewed, not assumed. |
| S1a | [GRAVITY_NEXT_INVESTIGATION.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NEXT_INVESTIGATION.md), Question 1 | Governing question and proposed Hessian/sign tests; not an accepted descent proof. |
| S1b | [GRAVITY_NATIVE_EQUATION_MAP.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NATIVE_EQUATION_MAP.md), E01, E05–E11 | Definition/notation inventory: map, potential, response, balance, and coherence conventions. |
| S1c | [GRAVITY_ESTABLISHED_RESULTS.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_ESTABLISHED_RESULTS.md), proof-level table; [GRAVITY_OPEN_QUESTIONS.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_OPEN_QUESTIONS.md), unresolved relationship 1 and domain traps | Historical 22 October scope and status, read in light of later accepted results. |
| S1d | [GRAVITY_IMPLEMENTATION_SOURCE_MAP.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_IMPLEMENTATION_SOURCE_MAP.md), K-DYN/K-DIAG, mathematical evidence ownership, discrepancy 1 | Source authority and normalization. Its previously recorded GR2 transcription correction is already incorporated in S2's `eq:K`; no old report is rewritten. |
| S2r | [response.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex), lines 20–39, 100–151, 158–198; `eq:potential`, `thm:branch`, `eq:fixed`, `eq:screen`, `eq:weighted`, `eq:SP`, `thm:cycle`, `eq:cycle`, `eq:K`, `eq:cycleweak` | Accepted map/potential, local positive branch and derivative, weighted response, and local diagonal-cycle criterion/factorization. |
| S2s | [spectral.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/spectral.tex), lines 1–77; `thm:spd`, `thm:triad`, `eq:triadD`, `eq:triadres` | Accepted symmetric triad reduction, quotient multipliers, and distinction between quotient semisimplicity and full-matrix resonance. |
| S2l | [THEOREM_LEDGER.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/provenance/THEOREM_LEDGER.md), L01, L04, L08, L10–L15, L17–L19 | Inherited result classification and qualifications; no listed scientific checker was rerun. |
| S3 | [main.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex), lines 161–164, 314–372, 414–448; `eq:parameters`, `lem:phase`, `eq:phaselemma`, `eq:apos`, `eq:lower`, `eq:upper`, `thm:convergence`, `eq:amplitudemap`, `eq:beta`, `eq:fixed` | Accepted prestage cone/radial bounds, phase pair-distance contraction, invariance, and existence/uniqueness of the aligned profile in \([0.9,1.1]^3\). These are the finite-domain inputs, not rerun certificates. |
| S4m | [drift/manuscript.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex), lines 116–156 and 646–668; D8–D11, D46–D47 | Accepted stage-specific gradient identities, segment descent principle, and conditional pure-gradient obstruction. |
| S4d | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py), `arg0`, `phase_sync`, `_advance`, `step3`, lines 57–104 | Text-only confirmation: zero convention, lambda-zero bypass, simultaneous phase kicks, and stage order. |
| S4v | [z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py), `_state_parameters`, lines 219–233; `potential`, lines 290–302 | Text-only confirmation: the three undirected edges occur once, onsite coefficients are \(1/4,-k_i/2\), and the graph coefficient is \(g/2\). |
| S5 | [accepted review main.tex](C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_COHERENCE_PAPER_01/manuscript/main.tex), Sections 5 and 5.1, Theorem 4, lines 131–170; [SECTOR_60_REVIEW.md](C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_COHERENCE_PAPER_01/proof_review/SECTOR_60_REVIEW.md), theorem and Sections 1–5 | Accepted overlap: 60-degree finite-return exclusion and aligned amplitude descent. Used to delimit novelty/scope, not as a prerequisite for A or B. |
| Handoff | [TRIOCTAGON_NATIVE_ENERGY_RESPONSE_HANDOFF_2026-11-01.zip](C:/Users/Notandi/Downloads/TRIOCTAGON_NATIVE_ENERGY_RESPONSE_HANDOFF_2026-11-01.zip), members `START_HERE.md` and `AUTHOR_CHECKPOINTS.md`; especially `START_HERE.md` Section 3.2 | Read directly from the archive. Records acceptance of S5 despite historical draft headers and fixes interpretive boundaries. Its initial pause was superseded by the present explicit work order; no successor task is commissioned. |

The deductions verified in this task are: identification of the potential Hessian in the local polar quotient; its exact complete-response decrement and nonlinear strict sign; the explicit full-complex finite-domain inequality (B) and equality classification; the comparison with the inherited cycle criterion; and the finite-step pair-coherence sign/normalization identity. None is inferred merely from eventual convergence or from a software check count.

## 3. Map, scalar, and regularity

Work exclusively with the triad and

\[
L=\mathbf1\mathbf1^T-3I=
\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
\]

The native map is

\[
v=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL\Omega,
\qquad b=v-\Omega,
\]
\[
\psi_i=\operatorname{Arg}_0(v_i),\qquad
\delta_i=\lambda\sum_{j\ne i}\sin3(\psi_j-\psi_i),\qquad
F_i(\Omega)=v_i e^{i\delta_i}.
\tag{1}
\]

The native convention \(\operatorname{Arg}_0(0)=0\) and the implemented \(\lambda=0\) bypass are retained. The scalar tested throughout is exactly

\[
\mathcal V(\Omega)=\epsilon\sum_{i=1}^3
\left(\frac{|\Omega_i|^4}{4}-\frac{k_i|\Omega_i|^2}{2}\right)
+\frac g2\sum_{i<j}|\Omega_i-\Omega_j|^2.
\tag{2}
\]

In nodewise real coordinates \(x_i\in\mathbb R^2\), differentiation gives

\[
\nabla_{x_i}\mathcal V=\epsilon(|x_i|^2-k_i)x_i
+g\sum_{j\ne i}(x_i-x_j),\qquad b=-\nabla_{\mathbb R^6}\mathcal V.
\tag{3}
\]

The norm in (B) is the usual real six-coordinate Euclidean norm, equivalently the complex three-coordinate norm. It measures the **prestage increment**, not \(F\Omega-\Omega\).

On nonzero prestages the sine in (1) is the imaginary part of
\((v_j\overline v_i/(|v_j||v_i|))^3\). Thus the full map is smooth there and common-phase equivariant without relying on a principal-argument branch cut. The potential is common-phase invariant everywhere. All quotient/differentiation arguments below use regular states; no global equivariance assertion through zero prestages is made. Segment differentiation in Target B concerns only the polynomial potential and therefore needs no nonzero condition inside that segment.

## 4. Target A: strict local full-map descent

### A.1. Hypotheses and statement

Fix \(g>0\) and an admitted positive in-phase profile \(r\) on the existing branch continued from a strictly stable equal triad, satisfying

\[
\epsilon r_i(k_i-r_i^2)+g(Lr)_i=0.
\tag{4}
\]

Write

\[
R=\operatorname{diag}(r),\quad
H=I+\epsilon\operatorname{diag}(k-r^2)+gL,\quad Hr=r,
\]
\[
P_{\rm resp}=R^{-1}HR,\quad
A=H-2\epsilon R^2,\quad
J=(I+3\lambda L)P_{\rm resp}.
\tag{5}
\]

Assume the retained **strict** normal-stability conditions at the chosen profile: every eigenvalue \(\alpha_j\) of \(A\) obeys \(|\alpha_j|<1\), and the two quotient phase multipliers obey \(|\rho_\pm|<1\). These persist on a sufficiently small branch neighborhood by S2r; no unquantified continuation beyond that admitted neighborhood is assumed.

Then there is a regular open neighborhood \(U\) of
\(\mathcal C_r=\{e^{i\theta}r:\theta\in\mathbb R\}\) such that

\[
\mathcal V(F\Omega)<\mathcal V(\Omega)
\quad(\Omega\in U\setminus\mathcal C_r),
\qquad F\Omega=\Omega\quad(\Omega\in\mathcal C_r).
\tag{A}
\]

### A.2. Deriving the Hessian and its factor of one half

Use the local chart
\(\Omega=e^{i\theta}(r+a)\odot e^{i\phi}\), with \(a,\phi\) real and \(r_i+a_i>0\). Put \(q=r+a\). Direct substitution into (2) yields

\[
\mathcal V=
\epsilon\sum_i\left(\frac{q_i^4}{4}-\frac{k_iq_i^2}{2}\right)
+\frac g2\sum_{i<j}(q_i-q_j)^2
+g\sum_{i<j}q_iq_j[1-\cos(\phi_i-\phi_j)].
\tag{6}
\]

The first two terms have zero first derivative at \(q=r\) by (4). Their Hessian is

\[
B=\epsilon\operatorname{diag}(3r^2-k)-gL=I-A.
\tag{7}
\]

The last term of (6) starts with
\(\frac g2\sum_{i<j}r_ir_j(\phi_i-\phi_j)^2\).
An amplitude change in its coefficient contributes only degree at least three. Equivalently, every mixed second derivative contains a sine that vanishes at alignment. The onsite potential has no phase dependence. Hence there are no mixed amplitude/phase quadratic terms.

Let \(K\) have off-diagonal entries \(-gr_ir_j\) and diagonal entries
\(gr_i\sum_{j\ne i}r_j\). The fixed equation gives
\(\epsilon(k_i-r_i^2)=-g(Lr)_i/r_i\), and consequently

\[
K=R(I-H)R=R^2(I-P_{\rm resp}),\qquad K\mathbf1=0,
\]
\[
\phi^TK\phi=g\sum_{i<j}r_ir_j(\phi_i-\phi_j)^2.
\tag{8}
\]

Every edge is counted once. Since \(g>0\) and all radii are positive, the kernel is exactly \(\operatorname{span}\{\mathbf1\}\), and \(K\) is positive definite on the quotient. Thus, in any fixed local quotient section,

\[
\mathcal V(\Omega)-\mathcal V(r)
=\frac12 a^TBa+\frac12\phi^TK\phi
+O\!\left(\|(a,[\phi])\|^3\right).
\tag{9}
\]

The quadratic factor is \(1/2\) in both blocks. Because \(A\) is symmetric and \(|\alpha_j|<1\), the eigenvalues \(1-\alpha_j\) of \(B\) are positive. In particular, the fixed circle is a strict local minimum transversely for this very potential.

### A.3. Derivative and exact phase decrement on the quotient

Differentiating the cubic prestage at the real profile gives
\(\delta v=Aa+iHR\phi\). Thus its amplitude derivative is \(A\), and its phase derivative is \(R^{-1}HR=P_{\rm resp}\). Differentiating the simultaneous sine kicks at alignment gives \(3\lambda L\). Synchronization preserves amplitudes and follows the prestage, so the complete derivative is \(\operatorname{diag}(A,J)\), in the order (5). There is no linear amplitude/phase mixing.

Set \(d=1-9\lambda\). Since \(L=\mathbf1\mathbf1^T-3I\),

\[
J=dP_{\rm resp}+3\lambda\mathbf1(\mathbf1^TP_{\rm resp}).
\tag{10}
\]

Weighted balance of the prestage gives
\(P_{\rm resp}^TR^2=R^2P_{\rm resp}\). Therefore

\[
P_{\rm resp}^TK
=R^2P_{\rm resp}(I-P_{\rm resp})
=KP_{\rm resp}.
\tag{11}
\]

Because \(K\mathbf1=0\), all terms containing the second summand of (10) disappear from its quadratic form:

\[
J^TKJ=d^2P_{\rm resp}^TKP_{\rm resp}.
\tag{12}
\]

These are identities on the full three-coordinate space. Their strict signs belong to the quotient \(\mathbb R^3/\operatorname{span}\{\mathbf1\}\). In particular, no invariance of the Euclidean sum-zero plane under \(J\) is used.

For completeness, the inherited symmetric reduction follows directly from (4): with \(\sigma=\sum_i r_i\),

\[
M_3=\sigma R^{-1}-\mathbf1\mathbf1^T,\qquad H=I-gM_3.
\tag{13}
\]

Weighted Cauchy–Schwarz gives
\(z^TM_3z=\sigma\sum_i z_i^2/r_i-(\sum_i z_i)^2\ge0\), with equality exactly when \(z\) is proportional to \(r\). Let its two positive eigenvalues be \(\mu_\pm\), with Euclidean-orthonormal eigenvectors \(w_\pm\perp r\). Define

\[
v_\pm=R^{-1}w_\pm,\quad p_\pm=1-g\mu_\pm,
\quad \rho_\pm=dp_\pm.
\tag{14}
\]

Then \(P_{\rm resp}v_\pm=p_\pm v_\pm\), and (10) makes \([v_\pm]\) quotient eigenvectors of \(J\) with eigenvalues \(\rho_\pm\). Their potential pairing is

\[
v_\beta^TKv_\alpha
=g\,w_\beta^TM_3w_\alpha
=g\mu_\alpha\delta_{\alpha\beta}.
\tag{15}
\]

For \([\phi]=c_+[v_+]+c_-[v_-]\), (12)–(15) prove exactly

\[
\boxed{\phi^T(J^TKJ-K)\phi
=g\sum_{\alpha\in\{+,-\}}
\mu_\alpha(\rho_\alpha^2-1)c_\alpha^2.}
\tag{16}
\]

The expression is strictly negative for every nonzero quotient class under \(|\rho_\pm|<1\). Repeated \(\mu\)'s at equal radii cause no difficulty: choose any orthonormal basis of their eigenspace. The case \(d=0\) also obeys the displayed identities.

### A.4. Amplitude decrement and nonlinear completion

Choose a Euclidean-orthonormal eigenbasis of the symmetric \(A\), and write the amplitude coefficients as \(z_j\). Since \(B=I-A\),

\[
a^T(A^TBA-B)a
=\sum_{j=1}^3(1-\alpha_j)(\alpha_j^2-1)z_j^2.
\tag{17}
\]

Each coefficient is strictly negative for \(|\alpha_j|<1\). This sign uses the specific relation \(B=I-A\), rather than a general assertion that spectral stability contracts any prescribed energy.

Here is a regular quotient chart that also handles the remainder. Let
\(E=\operatorname{span}\{v_+,v_-\}\), which is complementary to \(\mathbf1\) because \(\mathbf1^TR^2v_\pm=r^Tw_\pm=0\). Use the representative \(\phi=c_+v_++c_-v_-\in E\). After applying the full map, remove its local common phase to return to this same section. This does not assume \(E\) is \(J\)-invariant: its possible common-phase output is precisely what the quotient removes.

In coordinates \(u=(z_1,z_2,z_3,c_+,c_-)\), the induced smooth quotient map satisfies

\[
f(u)=Tu+O(\|u\|^2),\qquad
T=\operatorname{diag}(\alpha_1,\alpha_2,\alpha_3,\rho_+,\rho_-).
\]

At \(u=0\), the input, prestage, and output components all have moduli \(r_i>0\). Shrinking the chart preserves nonzero components and smoothness of the map and the output section. The potential expansion (9), composed with this actual nonlinear map, consequently gives

\[
\mathcal V(F\Omega)-\mathcal V(\Omega)
=-\frac12\left[
\sum_j(1-\alpha_j)(1-\alpha_j^2)z_j^2
+g\sum_{\alpha\in\{+,-\}}\mu_\alpha(1-\rho_\alpha^2)c_\alpha^2
\right]+O(\|u\|^3).
\tag{18}
\]

All five bracket coefficients are positive. Let \(m\) be their minimum. On a sufficiently small chart there is a finite \(C\ge0\) bounding the absolute remainder by \(C\|u\|^3\). Shrink the chart until \(C\|u\|\le m/4\). Then

\[
\mathcal V(F\Omega)-\mathcal V(\Omega)
\le-\frac m4\|u\|^2<0\quad\text{for }u\ne0.
\tag{19}
\]

The coordinate norm controls the Taylor remainder; the quantity being decreased remains exactly (2). Since both regular-map equivariance and potential invariance are exact under common rotation, rotating this neighborhood supplies the same conclusion around the entire fixed circle. A sufficiently small rotation-saturated neighborhood is regular and open. Its only equality states have \(u=0\), hence lie on \(\mathcal C_r\). This proves (A).

Unit-modulus normal multipliers and other cases with only a semidefinite quadratic decrement are outside the statement. Nothing in this argument upgrades such a sign to nonlinear strict descent.

## 5. Target B: explicit finite-domain inequality

### B.1. Exact parameters and whole-segment domain

Fix, independently of Target A's local branch hypotheses,

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad
\lambda=\frac1{300},\quad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),
\]
\[
\mathcal D=\left\{\Omega:\frac9{10}\le|\Omega_i|\le\frac{11}{10},
\ \text{ordinary phase width}\le\frac\pi{12}\right\}.
\tag{20}
\]

Ordinary phases are lifted in a single full-turn phase convention; there is no identification modulo \(2\pi/3\). The common orientation of the containing interval is arbitrary.

S3, `eq:apos`–`eq:upper`, supplies positive prestage mixing, preservation of the input cone, and

\[
\frac{88701}{100000}+\frac3{100}\cos\frac\pi{12}
\le |v_i|\le\frac{107701}{100000},
\qquad \frac9{10}<|v_i|<\frac{11}{10}.
\tag{21}
\]

These are inherited exact-expression bounds, not new evaluations of states or reruns of their certificates. In particular the prestage is regular and has phase width at most \(\pi/12\).

Both endpoints \(\Omega\) and \(v\) lie in the product of closed disks
\(\mathcal P=\{x\in\mathbb C^3:|x_i|\le11/10\}\). This set is convex. Explicitly,

\[
|\Omega_i+t b_i|=|(1-t)\Omega_i+t v_i|
\le(1-t)|\Omega_i|+t|v_i|\le11/10
\quad(0\le t\le1).
\tag{22}
\]

Thus the entire straight segment is in \(\mathcal P\). No convexity of the annulus or of \(\mathcal D\) is claimed or required.

### B.2. Curvature and prestage descent

Differentiating (3), the onsite Hessian block is exactly

\[
\epsilon\big[(|x_i|^2-k_i)I_2+2x_ix_i^T\big],
\tag{23}
\]

and the graph Hessian is \(-gL\otimes I_2\) in nodewise real-coordinate order. For any \(y_i\in\mathbb R^2\), Cauchy–Schwarz and \(\epsilon>0\) imply

\[
y_i^T\nabla^2\mathcal V_{\mathrm{onsite},i}y_i
\le\epsilon(3|x_i|^2-k_i)\|y_i\|^2
\le\epsilon\left(3(11/10)^2-999/1000\right)\|y_i\|^2.
\]

The largest eigenvalue of \(-gL\) is \(3g\). Adding these form bounds proves, everywhere on \(\mathcal P\),

\[
\nabla^2\mathcal V\preceq M I_6,\qquad
M=\frac1{10}\left(3\frac{121}{100}-\frac{999}{1000}\right)
+\frac3{60}=\frac{3131}{10000}.
\tag{24}
\]

Only this upper bound is needed. A positive lower Hessian bound is neither asserted nor used on the disks.

Taylor's integral formula along (22), with (3), gives

\[
\begin{aligned}
\mathcal V(v)-\mathcal V(\Omega)
&=\nabla\mathcal V(\Omega)^Tb
+\int_0^1(1-t)b^T\nabla^2\mathcal V(\Omega+tb)b\,dt\\
&\le-\|b\|^2+\frac M2\|b\|^2
=-\frac{16869}{20000}\|b\|^2.
\end{aligned}
\tag{25}
\]

The constant follows exactly from
\(1-\tfrac12(3131/10000)=16869/20000>0\).

### B.3. Synchronization and the native first-harmonic term

The prestage hypotheses of S3's `lem:phase` are all satisfied: by (21), every prestage modulus is positive; its ordinary phase width \(D_v\) is at most \(\pi/12<\pi/6\); and \(0\le\lambda=1/300\le1/9\). With consistent input/output lifts, that lemma yields

\[
|\psi_i^+-\psi_j^+|
\le(1-9\lambda\cos3D_v)|\psi_i-\psi_j|,
\quad 0\le1-9\lambda\cos3D_v
\le1-\frac{3\sqrt2}{200}<1.
\tag{26}
\]

Writing \(s_i=|v_i|\), each squared pair distance is

\[
|s_ie^{i\psi_i}-s_je^{i\psi_j}|^2
=(s_i-s_j)^2+2s_is_j[1-\cos(\psi_i-\psi_j)].
\tag{27}
\]

The synchronizer preserves the \(s_i\), and \(1-\cos t\) is increasing for \(0\le t\le\pi/12\). Thus every squared pair distance in (27) is nonincreasing. Every onsite term of (2) is unchanged, and its graph coefficient is positive. Therefore

\[
\mathcal V(F\Omega)\le\mathcal V(v).
\tag{28}
\]

This is a conclusion about the first-harmonic graph term in the native potential, obtained from pair-angle contraction. It does not appeal to descent of the separate harmonic-three phase potential. Equations (25) and (28) prove (B) for every point of \(\mathcal D\), including its boundaries. S3 also gives \(F(\mathcal D)\subset\mathcal D\), although the proof of the one-step inequality already follows from the stated prestage and phase bounds.

### B.4. Equality in monotonicity

If \(\mathcal V(F\Omega)=\mathcal V(\Omega)\), (B) forces \(b=0\). Write \(\Omega_i=r_i e^{i\theta_i}\) using a containing interval of width at most \(\pi/12\), with \(r_i\ge9/10\). Choose a channel \(m\) with minimal phase. The imaginary part of \(e^{-i\theta_m}b_m=0\) is

\[
0=g\sum_{j\ne m}r_j\sin(\theta_j-\theta_m).
\tag{29}
\]

Every summand is nonnegative, and any phase strictly above the minimum makes its summand strictly positive because its difference is in \((0,\pi/12]\). Since \(g>0\) and \(r_j>0\), (29) forces all three phases to agree. Thus \(b=0\) implies \(\Omega=e^{i\theta}r\), where \(r\in[9/10,11/10]^3\) satisfies (4).

S3's `thm:convergence` and its amplitude contraction proof, specifically `eq:amplitudemap`, `eq:beta`, and `eq:fixed`, give exactly one such profile \(r_*\) in this cube. Conversely, \(e^{i\theta}r_*\) has prestage equal to itself and zero phase kicks, so it is fixed and the potential is unchanged. Consequently

\[
\mathcal V(F\Omega)=\mathcal V(\Omega)
\ \Longleftrightarrow\ b=0
\ \Longleftrightarrow\ \Omega\in\{e^{i\theta}r_*\}
\quad(\Omega\in\mathcal D).
\tag{30}
\]

These are precisely the fixed states of the full map within \(\mathcal D\); a fixed state must satisfy equality and hence (30). The classification did not assume convergence implies monotonicity and did not calculate \(r_*\).

## 6. Diagonal balance versus descent

Use S2r's notation \(\ell=3\lambda\), \(d=1-3\ell\). To avoid collision with the amplitude perturbation \(a\), keep the radii named \(r_1,r_2,r_3\). Set
\(\sigma_1=r_1+r_2+r_3\),
\(\sigma_2=r_1r_2+r_1r_3+r_2r_3\), and \(\sigma_3=r_1r_2r_3\). The accepted factorization, also checked symbolically here, is

\[
\mathcal C_{\rm cyc}=J_{12}J_{23}J_{31}-J_{21}J_{32}J_{13}
=\frac{g\ell d(r_1-r_2)(r_1-r_3)(r_2-r_3)}{\sigma_3^2}\,\mathcal K,
\tag{31}
\]
\[
\mathcal K=g^2\ell\sigma_1^3+
[g^2(1-2\ell)-g\ell]\sigma_1\sigma_2+
(3g\ell-g+\ell)\sigma_3.
\tag{32}
\]

The scalar \(\mathcal K\) in (32) is distinct from the phase Hessian \(K\). Near a strictly stable equal triad, all off-diagonals of \(J\) are positive: at equality they equal
\(q_0=g+\ell-3g\ell\), and the transverse multiplier \(1-3q_0\in(-1,1)\) implies \(0<q_0<2/3\). Positivity persists nearby. In this neighborhood, the inherited diagonal criterion states

\[
\exists\, W>0\text{ diagonal with }WJ=J^TW
\quad\Longleftrightarrow\quad\mathcal C_{\rm cyc}=0.
\tag{33}
\]

Necessity follows by multiplying the three pair-balance identities. For sufficiency, the positive diagonal entries
\((J_{21}J_{31},J_{12}J_{31},J_{13}J_{21})\)
balance edges 12 and 13 identically, while the edge-23 residual is the cycle difference. Thus a nonzero factor product in (31) rules out positive diagonal balance while Target A still proves descent wherever its strict stability hypotheses hold.

For an exact asymptotic comparison, take the inherited weak branch
\(k_i=k+\eta\kappa_i\), \(k>0\), \(\sum_i\kappa_i=0\). S2r gives

\[
r_i=\sqrt{k}+\eta\frac{\epsilon\sqrt{k}}{2\epsilon k+3g}\kappa_i+O(\eta^2).
\]

Substitution in (31), using
\(\mathcal K|_{r_i=\sqrt{k}}=k^{3/2}K_0\), yields

\[
\mathcal C_{\rm cyc}=C_3\eta^3+O(\eta^4),\quad
C_3=g\ell dK_0\left(\frac{\epsilon}{2\epsilon k+3g}\right)^3
\prod_{i<j}(\kappa_i-\kappa_j),
\]
\[
K_0=g(9g-1)+\ell(1-3g)^2.
\tag{34}
\]

If \(C_3\ne0\), there is \(\eta_0>0\) such that for every \(0<|\eta|<\eta_0\), the branch remains positive and strictly normally stable, its off-diagonals remain positive, and \(\mathcal C_{\rm cyc}\ne0\). For example, the remainder can be bounded by \(|C_3||\eta|^3/2\) after shrinking the interval; continuity supplies the other conditions. Therefore failed diagonal balance and local descent coexist throughout this punctured branch interval. The statement is conditional on the exact nonzero coefficient, not on a newly tuned fixture. No claim is made that any specified numerical \(\eta\) lies in it. If \(C_3=0\), leading-order information alone does not settle balance; (31) remains the exact local test.

The four properties must remain distinct:

| Property | Meaning and conclusion in the admitted stable triad setting |
|---|---|
| Positive diagonal balance | \(WJ=J^TW\) for a positive diagonal \(W\). It fails precisely when (31) is nonzero in the local positive-off-diagonal region. |
| Arbitrary SPD self-adjointness | \(GJ=J^TG\) for some SPD \(G\), possibly dense. S2s gives equivalence to a real semisimple full spectrum. The quotient eigenvalues are real semisimple and strictly inside the unit circle, separated from the common eigenvalue 1, so the full stable triad is diagonalizable over \(\mathbb R\) and admits such a \(G\). |
| Strict normal spectral stability | \(|\alpha_j|<1\), \(|\rho_\pm|<1\), with the common phase neutral. For an arbitrary matrix and a prescribed energy this alone would not establish energy contraction. |
| Contraction in the existing potential Hessian | Equations (16)–(18) establish it for \(B\) and \(K\), and (19) establishes nonlinear descent. These forms were derived from (2), not selected from the family of SPD symmetrizers. |

In fact (10)–(11) also give \(J^TK=KJ=dKP_{\rm resp}\). This is self-adjointness in the **positive quotient form** \(K\), which is singular on the full phase space. It is entirely compatible with failed positive diagonal balance and must not be described as a full-space SPD metric by itself. Full-space SPD existence follows from the separate real-semisimplicity argument above, not from overlooking the common-phase kernel.

## 7. Finite-step coherence sign and normalization check

Use exactly
\(S_{ij}=\Re(\overline{\Omega_i}\Omega_j)\),
\(A_{ij}=\Im(\overline{\Omega_i}\Omega_j)\), and
\(d_{ij}=\delta_j-\delta_i\). With tildes denoting prestage quantities,

\[
\overline{F_i}F_j
=\overline v_i v_j e^{i(\delta_j-\delta_i)}
=(\widetilde S_{ij}+i\widetilde A_{ij})
(\cos d_{ij}+i\sin d_{ij}).
\]

Taking real parts proves

\[
S_{ij}^+=\widetilde S_{ij}\cos d_{ij}
-\widetilde A_{ij}\sin d_{ij}.
\tag{35}
\]

Since intensities are preserved during synchronization and
\(|z_i-z_j|^2=|z_i|^2+|z_j|^2-2S_{ij}\), the graph coefficient \(g/2\) contributes \(-g\) times the coherence change. Thus

\[
\boxed{\mathcal V(F\Omega)-\mathcal V(v)
=-g\sum_{i<j}\left[
\widetilde S_{ij}(\cos d_{ij}-1)
-\widetilde A_{ij}\sin d_{ij}\right].}
\tag{36}
\]

This verifies both the area sign and the edge normalization. The algebraic identity alone has no general sign. Target B's sign comes from the phase-sector lemma and (27), while Target A's sign comes from its complete local response and nonlinear remainder. No retained Z budgets or new states were evaluated.

## 8. Relation to inherited results and limits

S5 already proves aligned amplitude descent on its returning-block cube \([0,\sqrt{1001/1000}]^3\), using the upper Hessian constant \(313/1250\) and decrement coefficient \(2187/2500\). Together with positive mixing and sector arguments, it excludes nonfixed regular finite unit-multiplier returns meeting a closed 60-degree ordinary phase sector under its stated hypotheses. That result is inherited, not rediscovered here.

Target B instead proves a quantitative one-step inequality for all complex states in the separate domain (20), without a finite-return assumption. Its radius bound is \(11/10\), its phase width is 15 degrees, and its coefficient is \(16869/20000\). The S3 convergence theorem supplies domain/profile facts but was not used to infer monotonicity. Target A is a local theorem at the admitted normally stable branch profiles and does not identify its unspecified neighborhood with (20).

Neither result claims global descent for arbitrary complex states, larger rings, other branches, or unit-modulus normal spectra. Neither replaces the full displacement by the prestage increment without stating it. The D1 conditional obstruction in S4m concerns a single common-phase-invariant potential generating a continuous pure-gradient field on a domain containing nonzero-rate relative equilibria. A scoped discrete-map descent inequality near the present in-phase branch or on (20) neither asserts that representation nor contradicts the obstruction.

The scalar remains a native mathematical potential. No physical energy, gravitational law, pose correspondence, rotating support, or added geometry is inferred. The stationary-support and other standing interpretive distinctions in the handoff remain untouched. This task ends with the proof review.

## 9. Exact-algebra support and execution record

The isolated helper [exact_algebra.py](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/exact_algebra.py) was run once successfully in the existing `torment` environment. It uses SymPy and the standard library only, with no repository imports. Its output [exact_algebra_results.json](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/exact_algebra_results.json) records **PASS** and the actual interpreter/library versions: Python 3.11.15, SymPy 1.14.0, interpreter `C:/Users/Notandi/miniconda3/envs/torment/python.exe`.

The helper differentiates the polar potential to check the two Hessian blocks and vanishing mixed block; checks the fixed-profile reduction, common-phase kernel, weighted Dirichlet form, response order, self-adjointness and quadratic contraction identities; checks the cycle factorization and its equal-radius coefficient; differentiates the Cartesian onsite potential; verifies the two rational finite-domain constants; and checks the complex pair-rotation sign. All variables in response identities are symbolic. The helper does not solve for profiles, evaluate the native map at states, sample a domain, certify floating-point arithmetic, or establish the nonlinear remainder argument. The written proofs above supply those analytic conclusions; the number of algebra checks is not a theorem count.

Execution was limited to bounded file/path searches, text reading (including two handoff members directly from the ZIP), creating this previously absent external output directory, writing the review/helper, executing the isolated exact helper, and inspecting the delivered files. PowerShell was used for file inspection and directory creation. Python work used Command Prompt with `call conda activate torment`:

```bat
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
call conda activate torment
python -I -B C:\TORMENT\TRIOCTAGON_new\research\NATIVE_ENERGY_RESPONSE_01\exact_algebra.py
```

One earlier inline `python -c` environment probe failed at command-line quote parsing with a `SyntaxError`; no helper or native code ran in that probe. Using the script-file invocation above resolved it. The helper opens its result file in exclusive-create mode to preserve existing results; any later intentional rerun should use a fresh output directory. No package installation was needed or performed.

No Git commands, repository writes, application launches, kernel/UI edits, observer advances, old scientific checker/solver/certificate reruns, root solves, trajectories, parameter sweeps, or numerical native-map evaluations were performed. Existing research outputs were preserved. The fresh requested directory was available, so no dated suffix was required.

All outputs are in `C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01`:

| Output | Purpose |
|---|---|
| [NATIVE_ENERGY_RESPONSE_01_PROOF_REVIEW.md](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/NATIVE_ENERGY_RESPONSE_01_PROOF_REVIEW.md) | This self-contained proof, source/dependency record, scope, equality cases, and execution record. |
| [exact_algebra.py](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/exact_algebra.py) | Small isolated symbolic verification helper. |
| [exact_algebra_results.json](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/exact_algebra_results.json) | Exact-check results and environment metadata. |

The bounded assignment is complete. GPT/author review of these findings is the next decision point; no successor investigation, paper, integration, commit, or publication was initiated.
