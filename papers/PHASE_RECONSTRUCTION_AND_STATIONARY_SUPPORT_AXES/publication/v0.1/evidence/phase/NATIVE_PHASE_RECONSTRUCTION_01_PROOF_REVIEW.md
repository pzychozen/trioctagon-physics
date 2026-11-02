# Native common-phase reconstruction: proof review

**Task:** NATIVE_PHASE_RECONSTRUCTION_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Author / review:** Hilmir Frímann Halldórsson; GPT scientific review  
**Execution and mathematical challenge:** Codex  
**Status:** Bounded analytical investigation complete; returned for GPT/author review. This is a local proof review, not a publication or implementation.

The accepted five-coordinate evolution determines the full native trajectory once the original state's initial common phase is supplied. The missing phase evolves by a unit-complex factor determined by the current retained coordinates. On this particular invariant domain, the channel-1 convention has a continuous real increment, an absolutely convergent accumulated increment, and the already-established limiting-phase estimate. Retained data alone leave the initial common phase undetermined.

**Target A — verified on the entire stated closed domain.** The proposed formula for the unit factor is correct, with the source's conjugation and index conventions. It includes both prestage and synchronization phase change. The reconstruction is a conjugate description of the existing map, valid for every mathematical iterate.

**Target B — verified, with the essential correction made explicit.** The adjacent-state overlap depends only on the retained data and stays in the open right half-plane. Its angle is generally different from the channel-1 increment. Their difference is the angle of the inner product of consecutive canonical representatives. This correction has a controlled principal branch here and must be included when accumulating the anchor phase. A change of representative transfers opposite endpoint factors between the two terms and leaves the overlap and reconstructed state unchanged.

No proposed multiplicative identity failed. The substantive cautions are branch justification, the distinction between two kinds of tail bounds, and retention of the representative correction. These are elementary consequences of accepted inputs; no external novelty is claimed.

## 1. Dependencies and source identity

The following table separates inherited results from the consequences established here. Source IDs resolve to actual absolute paths and SHA-256 values in Appendix A and in `SOURCE_IDENTITIES.json`. Section numbers and labels below refer to the source, except where explicitly designated as sections of this report.

| Status | Dependency or result | Precise location and use |
| --- | --- | --- |
| Accepted input | Ordered native map, zero convention, regular common-phase equivariance | P1, §2 `sec:setting`, `eq:pre`, `eq:full`; N, `thm:Hclosure`, `eq:Hpre`, `eq:Hpost`, and the zero-stratum discussion at `eq:zerocounter`. Equivariance is used only at regular prestages. |
| Accepted input | Fixed tuple; invariant closed domain; strictly positive prestages | P4, §4 `eq:parameters`, `eq:domain`, `eq:prebounds`; C, §6 `lem:phase`, `eq:phaselemma`, `eq:apos`, `eq:lower`, `eq:upper`. |
| Accepted input | Positive-root reconstruction, exact common-phase fibres, exact joint-span image, autonomous retained map | P2, §5 `thm:reconstruction`, `eq:roots`, `eq:radicands`, `eq:Hconvention`, `eq:representative`, `prop:image`, `eq:span`, `thm:autonomy`, `eq:Hpre`, `eq:Hpost`, `eq:reducedmap`, `eq:iterates`. No minimality theorem is re-proved. |
| Accepted input | Nested phase intervals, geometric width contraction, convergence and unique aligned profile; exclusion of nontrivial returns in this domain | C, §7 `thm:convergence`, `eq:nesting`, `eq:phasebound`, `eq:amplitudemap`, `eq:fixed`, and the paragraph following `eq:Cdecay`. |
| Accepted input | Retained potential, individual matched edge energies, finite descent and its equality states | P3, §6 `thm:retention`, `eq:matchededges`, `eq:traceidentity`, `cor:retaineddescent`, `eq:reducedequality`; P4, §4 `thm:finite`, `eq:finitedescent`, `eq:finiteequality`. |
| Immediate corollaries, verified here | Formula for the unit factor; one-step reconstruction; trace overlap; overlap factorization; representative-change identities | Report §§3.1, 4.1, 5.1, 6. Algebra and fibre/equivariance arguments from the preceding accepted inputs. The new generic symbolic helper independently checks the signs and factor order. |
| Deductions verified here | Canonical branches and right-half-plane bounds; all-step reconstruction; absolute-sum versus net-tail control; overlap correction and its accumulation | Report §§3.2–3.4, 4.2, 5.2–5.3, 6–7. Complete domain arguments are written below; no point tests replace them. |
| Separate accepted context | Conditional raw-coherence return; D1 drift under different state-domain hypotheses | R, §3 Theorem 1, §3.1 and §9; D, D1–D4, D45–D47. Used only for the comparisons in §9. |
| Motivation and scope, not reconstruction theorems | Earlier overlap proposal and interpretation checkpoints | Q, Question 3; H, §7 and standing-sequence passages; P5, §8; current order W, especially §§1, 6, 8. The current order governs this investigation. |

The published edition was available in the retained isolated publication worktree. Its PDF has the prescribed SHA-256, `0f710dbf732ce4ec227a98650f3a774f7ba6cdab0ca8120df9859ac326ddcc01`. Mathematics was read from the focused TeX sources; no new PDF inspection is claimed. Publication commit `634ff13b666604d5caed11cc3731dcb5a863ff6c` is a reading reference. No checkout HEAD was queried or changed. The supplied recovery proposal and its original research-workspace copy have identical hashes. Earlier proof helpers and certificates were not executed.

## 2. Exact setting and notation

Fix throughout

\[
\epsilon=\frac1{10},\qquad g=\frac1{60},\qquad
\lambda=\frac1{300},\qquad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),
\qquad L=\mathbf1\mathbf1^T-3I.
\]

For \(s_i=|\Omega_i|^2\), the native update is

\[
M=I+\epsilon\operatorname{diag}(k-s)+gL,\qquad v=M\Omega,
\]
\[
\delta_i=\lambda\sum_{j\ne i}\sin\bigl(3(\operatorname{Arg}_0v_j-
\operatorname{Arg}_0v_i)\bigr),\qquad
F(\Omega)=U_\delta v,\qquad U_\delta=\operatorname{diag}(e^{i\delta_i}).
\tag{1}
\]

All kicks use the same prestage. The convention \(\operatorname{Arg}_0(0)=0\) and the native lambda-zero bypass remain unchanged. This task does not enter that zero stratum or change the fixed positive lambda.

Set \(D_0=\pi/12\). The full domain \(\mathcal D\) consists of states with \(9/10\le|\Omega_i|\le11/10\) whose ordinary phases admit one interval of width at most \(D_0\), with arbitrary common angle. Relative phases are not identified modulo \(2\pi/3\).

Use

\[
C_{ij}=\overline\Omega_i\Omega_j=S_{ij}+iA_{ij},\qquad
H=\Omega\Omega^\dagger=S_G-iA_G,\qquad
y=\mathcal R(\Omega)=(s_1,s_2,s_3,x,y_a),
\quad x=A_{12},\quad y_a=A_{13}.
\]

The exact image \(\mathcal Y=\mathcal R(\mathcal D)\) is given by

\[
\frac{81}{100}\le s_i\le\frac{121}{100},\qquad
a_1=0,\quad a_2=\arcsin\frac{x}{\sqrt{s_1s_2}},\quad
a_3=\arcsin\frac{y_a}{\sqrt{s_1s_3}},
\]
\[
m(y)=\min_i a_i,\qquad M_a(y)=\max_i a_i,\qquad
\Delta(y)=M_a(y)-m(y)\le D_0.
\tag{2}
\]

The arcsines are real principal arcsines, and the joint span is essential. Independent bounds on \(x\) and \(y_a\) would admit unintended phase widths. The symbol \(M_a\) denotes a scalar endpoint, distinct from the native matrix \(M\).

The accepted reconstruction is

\[
p=+\sqrt{s_1s_2-x^2},\qquad q=+\sqrt{s_1s_3-y_a^2},
\quad S_{23}=\frac{pq+xy_a}{s_1},\quad
A_{23}=\frac{py_a-xq}{s_1},
\]
\[
z(y)=\left(\sqrt{s_1},\frac{p+ix}{\sqrt{s_1}},
\frac{q+iy_a}{\sqrt{s_1}}\right)^T
=\bigl(\sqrt{s_i}e^{ia_i}\bigr)_{i=1}^3,
\qquad H(y)=z(y)z(y)^\dagger.
\tag{3}
\]

In particular, \(H_{12}=p-ix\) and \(H_{13}=q-iy_a\). The retained update \(G=F_{\mathcal R}\) is determined by

\[
\widetilde H=MHM^T,\qquad \rho_i=\sqrt{\widetilde H_{ii}},\qquad
\delta_i(y)=\lambda\sum_{j\ne i}\operatorname{Im}
\left[\left(\frac{\widetilde H_{ji}}{\rho_j\rho_i}\right)^3\right],
\]
\[
H^+=U_\delta\widetilde H U_\delta^\dagger,\qquad
Gy=(H^+_{11},H^+_{22},H^+_{33},-\operatorname{Im}H^+_{12},-\operatorname{Im}H^+_{13}).
\tag{4}
\]

The \(ji\) index and extraction minus signs are required. We use the accepted facts \(G\mathcal Y\subseteq\mathcal Y\), \(\mathcal R F=G\mathcal R\), exact common-phase fibres, and regular equivariance. At every admitted step,

\[
\rho_i\ge a_*:=\frac{88701}{100000}+\frac3{100}\cos D_0
>\frac9{10},\qquad
\rho_i\le\frac{107701}{100000}<\frac{11}{10}.
\tag{5}
\]

These are prestage bounds, not an inference from input nonvanishing alone. Consequently all formulas in (3)–(4) are continuous on the full closed image.

For iterates write \(y_n=G^ny_0\), \(\Delta_n=\Delta(y_n)\), and \(\Delta_{\rm init}=\Delta(y_0)\). This avoids confusing the initial width with its allowed maximum \(D_0\). The accepted phase results give consistent lifts with

\[
I_{n+1}\subseteq I_n,\qquad
\Delta_n\le c^n\Delta_{\rm init},\qquad
c=1-\frac{3\sqrt2}{200}\in(0,1),
\tag{6}
\]

and a unique limiting phase in their nested intersection. Accepted amplitude convergence gives \(\Omega_n\to e^{i\theta_\infty}r_*\). Those convergence theorems are inputs, not re-proved here.

## 3. Target A: the exact lift

### 3.1. The unit factor and the conjugate map

For \(z=z(y)\), \(z_1=\sqrt{s_1}>0\), so

\[
(MH)_{11}=(Mz)_1\overline z_1=\sqrt{s_1}(Mz)_1,
\qquad |F_1z|=|(Mz)_1|=\rho_1>0.
\]

It follows that the proposed expression is exactly

\[
\boxed{\kappa(y)=\frac{F_1(z(y))}{|F_1(z(y))|}
=e^{i\delta_1(y)}\frac{(M(y)H(y))_{11}}{\sqrt{s_1}\rho_1(y)}\in U(1).}
\tag{7}
\]

Both \(Fz(y)\) and \(z(Gy)\) lie in \(\mathcal D\) and have retained tuple \(Gy\). The accepted fibre theorem makes them common rotations of one another. Since \(z_1(Gy)=\rho_1>0\), comparison of their first components identifies that rotation as (7). Thus

\[
\boxed{F(z(y))=\kappa(y)z(Gy).}
\tag{8}
\]

The map \(\Phi:\mathcal Y\times U(1)\to\mathcal D\), \(\Phi(y,u)=u z(y)\), is a continuous bijection with the continuous inverse

\[
\Phi^{-1}(\Omega)=\left(\mathcal R(\Omega),\frac{\Omega_1}{|\Omega_1|}\right).
\]

There is no zero anchor in this domain. Equation (8) and regular equivariance prove

\[
F\circ\Phi=\Phi\circ T,\qquad T(y,u)=(Gy,u\kappa(y)).
\tag{9}
\]

This is conjugacy of self-maps; no invertibility of \(F\) or \(G\) is asserted or needed.

For an original initial state, the required data are

\[
u_0=\frac{\Omega_{1,0}}{|\Omega_{1,0}|},\qquad \Omega_0=u_0z(y_0).
\]

Inductively, if \(\Omega_n=u_nz(y_n)\), (8) gives
\(F\Omega_n=u_n\kappa(y_n)z(Gy_n)\). Therefore, for every integer \(n\ge0\),

\[
\boxed{y_{n+1}=Gy_n,\qquad u_{n+1}=u_n\kappa(y_n),\qquad
\Omega_n=u_nz(y_n),\qquad
u_n=u_0\prod_{j=0}^{n-1}\kappa(G^jy_0).}
\tag{10}
\]

The empty product is one. Forward invariance and (5) justify each successive step of this induction; it is not a claim based on finitely many computed states. Given only \(y_0\), all initial states and reconstructed trajectories are the family (10) indexed by \(u_0\in U(1)\). No phase-invariant input selects that initial factor.

### 3.2. Canonical real branch on the entire image

For canonical input \(z(y)\), its phase interval is \([m,M_a]\), with \(m\le0\le M_a\) and width \(\Delta=\Delta(y)\). By accepted positive prestage mixing, choose prestage phases \(\psi_i\in[m,M_a]\). By the accepted simultaneous phase lemma, the actual lifted output phases

\[
b_i=\psi_i+\delta_i
\]

also belong to \([m,M_a]\). Their width is at most \(c\Delta\). The harmonic-three sine does not change when an ordinary input lift changes by a multiple of \(2\pi\), so these are phases of the native output (1).

In particular, \(|b_1|\le\Delta\le D_0<\pi/2\), and

\[
\operatorname{Re}F_1(z(y))=\rho_1\cos b_1
\ge a_*\cos\Delta
\ge a_*\cos D_0>0.
\tag{11}
\]

Thus the principal argument in the open right half-plane supplies a single continuous function on all of \(\mathcal Y\):

\[
\boxed{\vartheta(y)=\operatorname{Arg}F_1(z(y))=b_1,
\qquad m(y)\le\vartheta(y)\le M_a(y),
\qquad |\vartheta(y)|\le\Delta(y).}
\tag{12}
\]

Also \(\kappa=e^{i\vartheta}\) and \(\operatorname{Re}\kappa\ge\cos D_0>0\). Continuity follows from continuous formulas (3)–(4), the positive denominators (5), and the explicit half-plane (11); nonvanishing alone would not justify a global argument branch.

The actual increment is \(\vartheta=\psi_1+\delta_1\), where \(\psi_1=\operatorname{Arg}(Mz)_1\) on this section. The interval argument proves this is an equality of real lifts here. Dropping \(\psi_1\) would generally discard part of the native phase change.

### 3.3. Real iteration and the two different tail bounds

Choose any real \(\theta_0\) with \(e^{i\theta_0}=u_0\) and set

\[
\theta_{n+1}=\theta_n+\vartheta(y_n),\qquad
\theta_N=\theta_0+\sum_{j=0}^{N-1}\vartheta(y_j).
\tag{13}
\]

These lifts have the claimed physical-state relation \(\Omega_n=e^{i\theta_n}z(y_n)\). To check consistency with the inherited ordinary phase intervals, the output phases relative to channel 1 are \(b_i-b_1\). They lie in \([-D_0,D_0]\), and principal arcsine in (2) recovers exactly those differences. Hence

\[
a_i(Gy)=b_i-b_1,\qquad
\theta_{i,n}=\theta_n+a_i(y_n)
\]

propagates the inherited consistent lift, with \(\theta_n=\theta_{1,n}\). There is no unresolved multiple of \(2\pi\) at a later step.

Equations (6) and (12) give the absolute-sum bound

\[
\boxed{\sum_{j=n}^{\infty}|\vartheta(y_j)|
\le\frac{\Delta_{\rm init}c^n}{1-c}.}
\tag{14}
\]

Consequently

\[
\theta_\infty=\theta_0+\sum_{j=0}^{\infty}\vartheta(y_j),\qquad
\Omega_n\longrightarrow e^{i\theta_\infty}r_*.
\tag{15}
\]

The sum in (15) recovers the same limiting lift as the inherited nested intervals: \(\theta_n\in I_n\), and the intersection of the intervals is their unique limiting phase. In particular that phase and \(\theta_n\) both lie in \(I_n\), giving

\[
\boxed{|\theta_\infty-\theta_n|\le\Delta_n
\le\Delta_{\rm init}c^n.}
\tag{16}
\]

This sharper bound is the inherited net remaining adjustment. It does **not** replace the factor \(1/(1-c)\) in the absolute-variation estimate (14). No optimal rate or global smooth asymptotic-phase theorem is claimed. Changing \(\theta_0\) by \(2\pi\ell\) changes every lift and its limit by the same amount and leaves every complex state unchanged.

### 3.4. Aligned input need not be a fixed state

When \(x=y_a=0\), (2) gives \(a_i=0\) and \(z(y)=r\), a positive real vector. The prestage is the accepted positive aligned amplitude update

\[
\mathcal A_i(r)=[1-2g+\epsilon(k_i-r_i^2)]r_i+g(r_j+r_k)>0.
\]

All kicks vanish. Thus \(\kappa=1\) and \(\vartheta=0\) throughout the aligned subset, even when \(\mathcal A(r)\ne r\). Its amplitudes relax under the inherited amplitude map. Only \(r=r_*\) is fixed; the accepted potential decreases strictly at every other aligned state. Zero phase increment is therefore not a criterion for a fixed full state or for zero potential decrease.

## 4. Target B: the adjacent-state overlap

### 4.1. Retained-data formula and common-phase invariance

Use \(\mathcal O\), not the old proposal's \(Z\), to distinguish this scalar from the placed-Z observer. Cyclicity of trace and \(H=\Omega\Omega^\dagger\) give

\[
\boxed{\mathcal O(\Omega)=\Omega^\dagger F(\Omega)
=\operatorname{tr}(U_\delta M H(y))
=\sum_i e^{i\delta_i(y)}(M(y)H(y))_{ii}.}
\tag{17}
\]

All quantities on the right are determined by \(y\) through (3)–(4), so write \(\mathcal O(y)\). Neither conjugating \(MH\) nor reversing the area sign is permitted. Equivariance also directly gives
\((u\Omega)^\dagger F(u\Omega)=\overline u u\,\Omega^\dagger F(\Omega)=\mathcal O(\Omega)\) for \(|u|=1\).

### 4.2. Half-plane, angle and accumulation

Take any admitted input and the inherited consistent phases of its one-step output. Both \(\theta_i\) and \(\theta_i^+\) lie in the same input interval of width \(\Delta\). Thus

\[
d_i=\theta_i^+-\theta_i\in[-\Delta,\Delta],\qquad
\mathcal O=\sum_i r_i\rho_i e^{id_i},\qquad r_i=|\Omega_i|.
\]

Positive weights, amplitude bounds and \(\Delta\le D_0\) give

\[
\boxed{\operatorname{Re}\mathcal O(y)
\ge\cos\Delta\sum_i r_i\rho_i
\ge\frac{243}{100}\cos\Delta
\ge\frac{243}{100}\cos D_0>0.}
\tag{18}
\]

The bound is deliberately nonoptimal. Moreover each summand lies in the closed sector \(|\arg w|\le\Delta<\pi/2\). This sector is convex: \(|\operatorname{Im}w|\le(\tan\Delta)\operatorname{Re}w\) is preserved under addition. Therefore

\[
\boxed{\alpha_{\rm ov}(y)=\operatorname{Arg}\mathcal O(y)
\text{ is continuous},\qquad |\alpha_{\rm ov}(y)|\le\Delta(y).}
\tag{19}
\]

This proof includes input intervals crossing a principal-argument cut; it uses consistent ordinary lifts, while the overlap itself is invariant under common rotation. Along any admitted mathematical iterate,

\[
\sum_{j=n}^{\infty}|\alpha_{\rm ov}(y_j)|
\le\frac{\Delta_{\rm init}c^n}{1-c}.
\tag{20}
\]

The accumulated overlap angles converge. They are not, by themselves, the anchor phase; no analogue of the sharper inherited net bound (16) is asserted for their uncorrected sum.

## 5. The correction between the two angles

### 5.1. Nonvanishing of the representative overlap

By (8),

\[
B_{\rm sec}(y):=z(y)^\dagger z(Gy),\qquad
\boxed{\mathcal O(y)=\kappa(y)B_{\rm sec}(y).}
\tag{21}
\]

For canonical phases \(a_i=a_i(y)\), \(a_i^+=a_i(Gy)\), both intervals contain zero. Hence
\(|a_i|\le\Delta\), \(|a_i^+|\le\Delta(Gy)\le c\Delta\le\Delta\), and

\[
B_{\rm sec}=\sum_i r_i\rho_i e^{i(a_i^+-a_i)},\qquad
|a_i^+-a_i|\le2\Delta\le\pi/6.
\]

The same sector argument yields

\[
\boxed{\operatorname{Re}B_{\rm sec}\ge\frac{243}{100}\cos(2\Delta)
\ge\frac{243\sqrt3}{200}>0,\qquad
\gamma(y):=\operatorname{Arg}B_{\rm sec}(y),\quad |\gamma(y)|\le2\Delta(y).}
\tag{22}
\]

Thus \(\gamma\) is a continuous principal argument on the entire image. From (21), the two angles initially agree modulo \(2\pi\):
\(\alpha_{\rm ov}\equiv\vartheta+\gamma\). But
\(|\vartheta+\gamma|\le3\Delta\le\pi/4<\pi\), so their chosen real values satisfy exactly

\[
\boxed{\alpha_{\rm ov}(y)=\vartheta(y)+\gamma(y).}
\tag{23}
\]

This resolves the possible wrap; a bare argument-of-a-product rule would not suffice globally.

### 5.2. Accumulation requires the correction at each step

The correct reconstruction from overlap angles is

\[
\boxed{\theta_N-\theta_0
=\sum_{j=0}^{N-1}\alpha_{\rm ov}(y_j)
-\sum_{j=0}^{N-1}\gamma(y_j).}
\tag{24}
\]

Both series converge absolutely, since (22) gives

\[
\sum_{j=n}^{\infty}|\gamma(y_j)|
\le\frac{2\Delta_{\rm init}c^n}{1-c}.
\tag{25}
\]

Their difference has the stronger net-tail bound (16) because it is exactly the canonical reconstruction. The correction in (24) has not been shown to be an endpoint-only difference, and no such telescoping assumption is used. Endpoint terms arising from a *change of section* below are a different statement. On the aligned subset, \(B_{\rm sec}=\sum_i r_i\mathcal A_i(r)>0\), so all three angles \(\gamma,\alpha_{\rm ov},\vartheta\) vanish even during amplitude relaxation.

### 5.3. Analytic check that the correction is not identically zero

A short local calculation at the original fixed coefficients establishes that the two angles can differ inside \(\mathcal D\). It is an analytic family, not a generated trajectory, parameter sweep, or native-step computation.

Take the canonical input \(z(t)=(1,e^{it},e^{it})\), \(|t|\le D_0\). Its intensities are constant, so its prestage matrix is constant. At \(t=0\), put

\[
w_i=1+\epsilon(k_i-1),\qquad
w=\left(\frac{9999}{10000},1,\frac{10001}{10000}\right),\qquad \sum_i w_i=3.
\]

The prestage phase derivatives at zero are

\[
\tau_1=\frac{2g}{w_1},\qquad
\tau_2=1-\frac{g}{w_2},\qquad
\tau_3=1-\frac{g}{w_3}.
\]

Indeed, differentiating the prestage gives imaginary derivatives \(i(2g,w_2-g,w_3-g)\) at the positive real vector \(w\). Let \(d=1-9\lambda>0\), \(T=\sum_i\tau_i\). Differentiating the simultaneous sine kicks at aligned prestage phases gives output phase derivatives

\[
\sigma_i=d\tau_i+3\lambda T.
\]

Output modulus derivatives vanish at zero. Removing the output channel-1 phase therefore gives canonical-output derivatives \(i w_i(\sigma_i-\sigma_1)\). The input conjugate derivatives are \((0,-i,-i)\). Consequently

\[
B_{\rm sec}(0)=3,\qquad
\operatorname{Im} B_{\rm sec}'(0)
=\sum_i w_i\sigma_i-3\sigma_1-(w_2+w_3).
\]

Since \(\sum_i w_i\tau_i=w_2+w_3\), this reduces to

\[
\operatorname{Im} B_{\rm sec}'(0)
=-9\lambda(w_2+w_3)-3d\tau_1,
\qquad
\boxed{\gamma'(0)=-3\lambda(w_2+w_3)-d\tau_1<0.}
\tag{26}
\]

The already-established right-half-plane branch makes this differentiation legitimate. Hence \(\gamma(t)\ne0\) for every sufficiently small positive \(t\), and (23) gives \(\alpha_{\rm ov}\ne\vartheta\) there. This is a sign witness, not a classification of their agreement set or a new continuation problem.

## 6. Change of representative

An explicit alternative is the positive channel-2 anchor

\[
h_2(y)=e^{-ia_2(y)},\qquad z_{h_2}(y)=e^{-ia_2(y)}z(y).
\tag{27}
\]

It is a continuous, globally specified section on \(\mathcal Y\), with second component \(\sqrt{s_2}\). It does not assume that the unequal channels are interchangeable physically.

More generally, for a specified \(h:\mathcal Y\to U(1)\), put \(z_h=h z\). Equivariance and (8) give

\[
F(z_h(y))=h(y)\kappa(y)z(Gy)
=\frac{h(y)}{h(Gy)}\kappa(y)z_h(Gy).
\]

Thus the section-relative factor, and the corresponding representative overlap, obey

\[
\boxed{\kappa_h(y)=\frac{h(y)}{h(Gy)}\kappa(y),\qquad
B_{{\rm sec},h}(y)=\overline{h(y)}h(Gy)B_{\rm sec}(y).}
\tag{28}
\]

The multiplier \(\kappa_h\) is the scalar relating \(Fz_h(y)\) to \(z_h(Gy)\); the channel-1 positive-output normalization (7) is specific to the canonical section. The two factors in (28) cancel, proving \(\mathcal O=\kappa_h B_{{\rm sec},h}\). Both remain nonzero, but an arbitrary new section need not keep either factor in the canonical half-plane.

Write \(h_j=h(y_j)\). Finite products cancel internally to give, for every \(N\),

\[
\prod_{j=0}^{N-1}\kappa_h(y_j)
=\frac{h_0}{h_N}\prod_{j=0}^{N-1}\kappa(y_j),\qquad
\prod_{j=0}^{N-1}B_{{\rm sec},h}(y_j)
=\frac{h_N}{h_0}\prod_{j=0}^{N-1}B_{\rm sec}(y_j).
\tag{29}
\]

This follows by cancellation of consecutive factors (or induction), not from a three-step test alone. Setting \(u_{h,0}=u_0/h_0\) gives

\[
u_{h,N}=u_N/h_N,\qquad u_{h,N}z_h(y_N)=u_Nz(y_N)=\Omega_N.
\tag{30}
\]

For a **specified real lift** \(h(y)=e^{i\chi(y)}\), define real increment lifts

\[
\vartheta_h^{\rm lift}(y)=\vartheta(y)+\chi(y)-\chi(Gy),\qquad
\gamma_h^{\rm lift}(y)=\gamma(y)-\chi(y)+\chi(Gy).
\tag{31}
\]

They exponentiate to the respective unit factors and sum exactly to \(\alpha_{\rm ov}\). Without a branch bound their principal arguments are only congruent to (31) modulo \(2\pi\). Their finite real sums satisfy

\[
\sum_{j=0}^{N-1}\vartheta_h^{\rm lift}(y_j)
=\sum_{j=0}^{N-1}\vartheta(y_j)+\chi(y_0)-\chi(y_N),
\]
\[
\sum_{j=0}^{N-1}\gamma_h^{\rm lift}(y_j)
=\sum_{j=0}^{N-1}\gamma(y_j)-\chi(y_0)+\chi(y_N),
\qquad \theta_{h,n}=\theta_n-\chi(y_n).
\tag{32}
\]

No unspecified global argument of an arbitrary unit-complex function has been invoked. Formulas (28)–(30) hold at the unit-complex level even without such a real lift. Continuity is an extra condition on \(h\) when discussing continuity of the changed section.

For the explicit section (27), \(\chi_2=-a_2\) is a justified global real lift, and

\[
\vartheta_2=\vartheta+a_2(Gy)-a_2(y)
=b_2-a_2(y).
\tag{33}
\]

This is the actual ordinary increment of channel 2. Both phases on the right lie in the same input interval, so \(|\vartheta_2|\le\Delta\), with no wrap. That additional bound is proved for this explicit anchor; it is not a bound for arbitrary \(h\).

In general, the canonical bounds (12), (14), (22), and (25) stay attached to their original section unless a separate proof applies. Even if \(h\) is continuous and \(y_n\to y_*\), convergence of \(h(y_n)\) alone does not control its total variation. An eventual local real lift near the limiting unit value is possible, but summability of its successive absolute changes does not follow just from continuity. Equations (31)–(32) provide the correct endpoint changes when the chosen real lift is available; they do not identify the original \(\gamma\) as an endpoint-only function or establish geometric holonomy.

## 7. Closed boundaries and degeneracies

Every assertion above applies to the full closed \(\mathcal Y\), without excluding equal amplitudes, coincident phases or individual zero areas. The accepted radicand bound is

\[
s_1s_2-x^2,\ s_1s_3-y_a^2
\ge\left(\frac{81}{100}\right)^2\cos^2D_0>0.
\]

Together with \(s_1\ge81/100\) and (5), this keeps all denominators positive at amplitude endpoints and at the width boundary \(\Delta=D_0\). No area, phase difference or amplitude difference is a denominator. The principal arcsines remain strictly inside their own singular endpoints because their arguments have modulus at most \(\sin D_0<1\).

If \(x=0\), then \(a_2=0\); if \(y_a=0\), then \(a_3=0\). Either may vanish independently. If \(A_{23}=0\), the narrow-sector difference \(a_3-a_2\) is zero. These are regular coincident-phase configurations. Equal amplitudes change none of the fibre, branch or positivity arguments. When both retained areas vanish, all phases align and §§3.4 and 5.2 apply. Complex coherence remains rank one everywhere; a drop to rank one of the *real* Gram in this sector identifies the aligned case and creates no new singularity.

Zero input components and zero prestages lie outside the accepted domain. This report avoids them by the inherited domain theorem and does not extend equivariance across the native zero convention.

## 8. Energy consistency

The inherited scalar and each matched edge energy are

\[
\mathcal V(\Omega)=\epsilon\sum_i
\left(\frac{|\Omega_i|^4}{4}-\frac{k_i|\Omega_i|^2}{2}\right)
+\frac g2\sum_{i<j}|\Omega_i-\Omega_j|^2,
\qquad E_{ij}(y)=s_i+s_j-2S_{ij}(y).
\]

Under \(\Omega=u z(y)\), \(|u|=1\), intensities and every distance are unchanged:
\(|u z_i-u z_j|^2=|z_i-z_j|^2\). By P3 `eq:matchededges`, these are also the individual accepted transported tangent-edge energies. Therefore \(\mathcal V(u z)=\widehat{\mathcal V}(y)\) and each \(E_{ij}\) is independent of \(u\), in either section. This does not reconstruct the phase-sensitive decoded face vectors from \(y\) alone.

Likewise \(M(u z)=M(z)\) as a matrix-valued function of intensities, and

\[
v(u z)-u z=u(Mz-z),\qquad
\|v(u z)-u z\|_2^2=\|Mz-z\|_2^2
=\widehat{\mathcal B}(y),
\]
\[
\widehat{\mathcal B}(y)=\operatorname{tr}((M-I)H(M-I)^T).
\]

Thus the accepted inequality transfers unchanged to the lifted description:

\[
\boxed{\mathcal V(F\Omega)-\mathcal V(\Omega)
\le-\frac{16869}{20000}\|v-\Omega\|_2^2,
\qquad
\widehat{\mathcal V}(Gy)-\widehat{\mathcal V}(y)
\le-\frac{16869}{20000}\widehat{\mathcal B}(y).}
\tag{34}
\]

Equality in **monotonicity**, \(\mathcal V(F\Omega)=\mathcal V(\Omega)\), holds exactly at the fixed circle \(\{u r_*:|u|=1\}\), equivalently \(y=y_*=(r_{*,1}^2,r_{*,2}^2,r_{*,3}^2,0,0)\). The inherited \(\widehat{\mathcal B}=0\) classification is the same. No claim about equality in every intermediate quantitative bound is substituted for that statement. The coefficient multiplies the squared prestage increment, not the full-step distance or a percentage of potential. No potential theorem or normalization is changed or re-proved.

## 9. Interpretation and consistency with other accepted results

The canonical increment is an anchor-dependent coordinate of the native update. The overlap angle is a common-phase-invariant adjacent-state diagnostic. A phase-sensitive readout can be evaluated from the reconstructed full state once its definition and the initial phase are supplied. None of these facts identifies common complex phase with a spatial pose, angular velocity, physical time or energy flux. The original \(u_0\) is state data; changing the mathematical representative changes bookkeeping, as (30) demonstrates.

**Conditional returns.** R §3 Theorem 1 says that for a nonzero state with a regular \(p\)-block, raw coherence return \(H(F^p\Omega)=H(\Omega)\) is equivalent to \(F^p\Omega=\mu\Omega\), with unique \(|\mu|=1\); the repeated blocks then satisfy \(F^{mp+r}\Omega=\mu^m F^r\Omega\). Its raw-coherence and regularity qualifications are retained; normalized projectors do not supply the same statement. Formally, a return \(G^p y=y\) in the present coordinates would have \(\mu=\prod_{j=0}^{p-1}\kappa(G^jy)\) by (10). But C §7 already excludes nonconstant periodic and nontrivial common-phase relative-periodic orbits entirely in \(\mathcal D\). Here only the fixed circle remains, with \(\mu=1\). No closed quotient orbit or holonomy was sought, and no return classification was re-proved.

**Separate D1 drift.** D, D1–D4, concerns a local twisted relative-equilibrium branch near components \(2^{-1/2}e^{2\pi i j/3}\), for \((\epsilon,g,\lambda)=h(1,1/6,1/30)\), \(k=(1-\eta,1,1+\eta)\), \(0\le h\le1/4\), with its stated local continuation hypotheses. It establishes a nonzero cubic-in-heterogeneity rate on that branch, which has a saddle reference. Its states lie outside the present narrow coherent domain; attraction is not inferred. For its finite-map equation \(F_h z=e^{ih\nu}z\), direct substitution gives \(z^\dagger F_hz=e^{ih\nu}\|z\|^2\), so its overlap angle is \(h\nu\) modulo \(2\pi\), while raw coherence and the phase-invariant potential remain stationary. This does not transport the present half-plane bounds to D1. At \(h=0\), the map is identity and the analytically extended generator rate is not a nonzero per-update advance. D45–D47 retain their conditional generator-level obstruction to a specified single invariant-potential pure-gradient representation; that argument is not substituted for a finite-map identity here. These facts coexist with finite-domain descent (34) because their hypotheses differ.

The supporting 180-degree line remains stationary. The close original sphere, tight toroid, and two-arrangement versus fast-alternation alternatives remain distinct; this investigation chooses none of them. The standing sequence remains phase reconstruction, then justified spatial/fixed-support correspondence; gravity–magnetism remains linked; outer geometry and legitimate SRG integration remain later; TORMENT/embodiment remains parallel; Three-Way remains parked. These are retained author checkpoints, not consequences proved by the phase formulas.

## 10. Execution, verification and stopping status

All new artifacts are confined to the fresh workspace `C:/TORMENT/TRIOCTAGON_new/research/NATIVE_PHASE_RECONSTRUCTION_01`. Source files were read only. Command Prompt with `call conda activate torment` was used for Python. Focused source reading and filesystem inspection also used PowerShell. No dependencies were installed.

The small, isolated `exact_algebra.py` was executed once with:

```bat
call conda activate torment && python -I -B C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_RECONSTRUCTION_01\exact_algebra.py
```

Actual environment: `C:\Users\Notandi\miniconda3\envs\torment\python.exe`, Python **3.11.15**, SymPy **1.14.0**. Its result file records the interpreter, versions, script hash, exact residuals and scope. The result is **PASS** for these generic symbolic identities:

1. \(H=S_G-iA_G\), checking the area/conjugation orientation.
2. \((MH)_{11}=z_1(Mz)_1\) for a positive real first component.
3. \(z^\dagger U M z=\operatorname{tr}(UMH)\).
4. \(\operatorname{tr}(UMH)=\sum_i u_i(MH)_{ii}\) for diagonal \(U\).
5. \(z^\dagger(\kappa z^+)=\kappa(z^\dagger z^+)\).
6. Cancellation of opposite section factors in the overlap.
7. Endpoint orientation for three formal factors of the section-changed increment.
8. Cancellation of initial and terminal section factors in the reconstructed full state.

The helper uses generic matrices, vectors and formal scalar factors; it implements no native update and contains no fixed native parameters. A three-factor symbolic cancellation supports, but does not replace, the arbitrary-length cancellation proof in §6. Branch bounds, continuity, continuous-domain validity, iteration and convergence are justified by the written arguments and accepted inputs. The local analytic differentiation in §5.3 was derived on paper, not by running a native-step evaluator.

`record_sources.py` performs focused file hashing and copies the two supplied task inputs into `inputs/`. `SOURCE_IDENTITIES.json` records the actual source identities. `package_review.py` inserts those identities into this report, checks that the focused source files and the checked helper still match their recorded hashes, and creates a convenience ZIP with a CRC read check. These are file/document checks, not further scientific computations or a publication audit. No Git command, repository import, old scientific helper, programmatic native-step evaluation, numerical trajectory, profile/root solve, cycle search, parameter sweep, observer/EMA advance, or historical certificate execution was performed. No application, model, accepted source, paper or repository file was changed.

**Unresolved mathematical issue within the commissioned targets:** none identified in this review. The results remain restricted to the exact tuple, image and inherited hypotheses stated above. No external literature search or novelty assessment was performed. GPT and the author retain scientific acceptance and interpretation review.

**Stopping status:** Both bounded targets are complete and the new evidence is returned for discussion. No successor investigation, geometric interpretation, paper, implementation, Git operation or publication has been started.

## Appendix A. Actual source paths and hashes

The identities below record only the focused files used in this review. Hashing a source records its identity; it does not claim re-verification of every result in that source. P0 was hashed for edition identification. Q and Q-download are byte-identical copies, not independent evidence. The compact review ZIP includes the supplied task inputs and new deliverables; the other accepted sources remain at the recorded local paths.

**W** — [C:/Users/Notandi/Downloads/NATIVE_PHASE_RECONSTRUCTION_01_CODEX_WORK_ORDER.md](<C:/Users/Notandi/Downloads/NATIVE_PHASE_RECONSTRUCTION_01_CODEX_WORK_ORDER.md>)  
SHA-256: `f82a3bd742c8ff0e48ebf39cca8fe8823879583f3d597409ef515b14b68514c0`

**P0** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf>)  
SHA-256: `0f710dbf732ce4ec227a98650f3a774f7ba6cdab0ca8120df9859ac326ddcc01`

**P1** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex>)  
SHA-256: `f0b3113ce197085b6175e7a8b738d37c9f6f8785f67b0376341353757940edfe`

**P2** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/coordinates.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/coordinates.tex>)  
SHA-256: `f244a48b9203c5a4d703097635d6b745ed7b0f2e072602e86bce0f13784e0137`

**P3** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/retention.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/retention.tex>)  
SHA-256: `49f56d2a404e35c96186f1d53468f3541d04ba565a8c284f14997744e49a2060`

**P4** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/finite.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/finite.tex>)  
SHA-256: `c07bb1df62d1782d9a3dc0c05b7a027e8d9e71e4da5c840ef1239bcb1e615c8b`

**P5** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/discussion.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/discussion.tex>)  
SHA-256: `4c57c971af213524b21dc13660c0019949acdb4b411ec42c64498f1104b84024`

**C** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/provenance/primary_sources/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/provenance/primary_sources/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex>)  
SHA-256: `40b6ca84ca136453b045386e2dead012fc8fcd7984b845d159ae6d6c8a6c2292`

**N** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/provenance/primary_sources/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/provenance/primary_sources/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex>)  
SHA-256: `fd3316c3845657e00cf3e0d103b9b13b605436a35b458c34f61dcceb41ef4aa4`

**R** — [C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/manuscript/main.tex](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/manuscript/main.tex>)  
SHA-256: `5d0f384b3774dac3d3fc24c8f5262533f26d48f16f07ba270f4693ea2091d604`

**D** — [C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex>)  
SHA-256: `19b5cf6566035655792dccb658fe55370b5a4814daf48ce1e30b85c1c7dece92`

**Q** — [C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NEXT_INVESTIGATION.md](<C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NEXT_INVESTIGATION.md>)  
SHA-256: `b163db7e6004ae37a80e7da91389a25558089ca402697a80ad1c6eb40a8678ac`

**Q-download** — [C:/Users/Notandi/Downloads/GRAVITY_NEXT_INVESTIGATION.md](<C:/Users/Notandi/Downloads/GRAVITY_NEXT_INVESTIGATION.md>)  
SHA-256: `b163db7e6004ae37a80e7da91389a25558089ca402697a80ad1c6eb40a8678ac`

**H** — [C:/Users/Notandi/Downloads/TRIOCTAGON_FRESH_CHAT_HANDOFF_NATIVE_ENERGY_RESPONSE_2026-11-01.md](<C:/Users/Notandi/Downloads/TRIOCTAGON_FRESH_CHAT_HANDOFF_NATIVE_ENERGY_RESPONSE_2026-11-01.md>)  
SHA-256: `2a8848f92438a3d83e8191520b5fe27eb64145a1176489447c10f8177ff6be1b`
