# CT: intrinsic excerpt (verbatim sections 2-3)

Codex, 25 September 2026. Full mixed-scope source remains preserved in its original location.
Source lines 51-173; original SHA-256 67d8eb7c44afe3c6e02eff8ef3f5de3630faf13cca9a3e98fee634c51e89834a. New heading is packaging metadata; the text below is unchanged.

## 2. Exact synchronized manifold and transverse Jacobian

**SOURCE FORMULA, followed by DERIVATION.** For equal real k, the pre-sync map is
\[
F_j(\Omega)=\Omega_j+\epsilon\Omega_j(k-|\Omega_j|^2)+g(L_3\Omega)_j,
\qquad L_3=ee^T-3I,\quad e=(1,1,1)^T.
\]
Immediately,
\[
L_3e=0,\qquad L_3v=-3v\quad(e^Tv=0).
\]
These identities are exact over both real and complex channel vectors.

For \(\Omega=we\),
\[
F(we)=swe,\qquad s=1+\epsilon(k-|w|^2)\in\mathbb R.
\]
Thus the synchronized manifold is invariant. The full phase step preserves it for any fixed real phase strength: all nonzero equal components have equal phase and every phase-difference sine vanishes. A negative s adds one common phase \(\pi\), not a channel difference. If \(sw=0\), the source's zero-phase convention returns the common zero state. This invariance does not require a local phase derivative at zero.

Equal k is a hypothesis. For unequal k, a nonzero common state generally develops unequal components through \(\epsilon w k_j\); trivial exceptions such as zero state or zero epsilon are not a general invariant-manifold claim.

For a complex transverse perturbation \(\delta\), \(e^T\delta=0\), differentiation of \(\Omega_j|\Omega_j|^2\) gives
\[
D(\Omega|\Omega|^2)_w[\delta]=2|w|^2\delta+w^2\bar\delta.
\]
At phase strength zero,
\[
\boxed{\delta'=
 [1+\epsilon(k-2|w|^2)-3g]\delta-\epsilon w^2\bar\delta.}
\]
This is an instantaneous **real-linear** derivative, not a complex-linear map and not a global stability theorem. Both conjugate terms remain transverse.

Writing \(w=a+ib\), the same channel-independent real block on \((\xi,\eta)\) is
\[
B=
\begin{pmatrix}
1+\epsilon(k-3a^2-b^2)-3g & -2\epsilon ab\\
-2\epsilon ab & 1+\epsilon(k-a^2-3b^2)-3g
\end{pmatrix}.
\]
It acts identically on both independent channel directions of \(e^\perp\).
For \(w=re^{i\phi}\ne0\), write \(\delta=e^{i\phi}(u+iv)\). Then
\[
u'=[1+\epsilon(k-3r^2)-3g]u,\qquad
v'=[1+\epsilon(k-r^2)-3g]v.
\]
The radial and phase-like sectors can contract at different rates, but **each sector remains twofold degenerate in channel space**. A component mixture can change the observed C direction without selecting a universal channel axis.

### Phase synchronization to first order

Use a local phase chart around a synchronized **nonzero pre-sync output** \(W=sw\). For phase differences \(p_j\), the source map reads
\[
p'_j=p_j+\lambda\sum_{l\ne j}\sin(3(p_l-p_j))
      =p_j+3\lambda(L_3p)_j+O(\|p\|^3).
\]
Hence
\[
p'_\perp=(1-9\lambda)p_\perp
\]
to first order. The amplitude perturbation is unchanged by this phase-only step. Composing with the pre-sync derivative,
\[
u_{\rm full}'=A_ru,\qquad
v_{\rm full}'=(1-9\lambda)A_tv,
\]
where \(A_r=1+\epsilon(k-3r^2)-3g\) and
\(A_t=1+\epsilon(k-r^2)-3g\).
This factor is exact at first order in the perturbation for fixed lambda; it is not a claim that finite phase differences are linear. The same twofold degeneracy survives. If \(W=0\), this phase-chart derivative is unavailable; source invariance of the zero state does not fix that problem.

At the synchronized fixed circle \(|w|=1\) for the recorded k/epsilon/g, the transverse factors are 0.3 radially and 0.4 (lambda=0) or 0.3964 (lambda=.001) in the phase-like sector. The longitudinal radial factor is 0.9 and the common-phase factor is 1. These are local factors at that circle. They neither prove that the recorded initial condition reaches it nor establish global convergence. The initial relative synchronization distance is about 4.47, well outside a small-transverse-perturbation interpretation.

## 3. Chirality: structural plane tendency, no forced axis

**EXACT DERIVATION.** Define the channel means \(a,b\), so
\[
x=\Re\Omega=ae+\xi,\qquad y=\Im\Omega=be+\eta,\qquad
e^T\xi=e^T\eta=0.
\]
Then
\[
\boxed{C=x\times y=e\times(a\eta-b\xi)+\xi\times\eta.}
\]
The first term is transverse and first order in the perturbation. The second is second order and parallel to e. Therefore
\[
e\cdot C=e\cdot(\xi\times\eta),
\]
which is generally nonzero; the sum-zero statement is not an exact invariant for arbitrary finite perturbations.

A stronger bound avoids assuming a nonvanishing generic first-order coefficient. Multiplication of all channels by \(e^{-i\arg w}\), \(w=a+ib\ne0\), preserves C. In that phase frame let the transverse real and imaginary components be \(\tilde\xi,\tilde\eta\). Exactly,
\[
C=|w|e\times\tilde\eta+\tilde\xi\times\tilde\eta.
\]
The terms are orthogonal, and
\[
\|C_\perp\|=\sqrt3|w|\,\|\tilde\eta\|,\qquad
\|C_\parallel\|\le\|\tilde\xi\|\,\|\tilde\eta\|.
\]
If C is nonzero, then \(\tilde\eta\ne0\), so
\[
\boxed{\tan\angle(C,e^\perp)
 \le \frac{\|\tilde\xi\|}{\sqrt3|w|}
 \le \frac{\|\delta\|}{\sqrt3|w|}.}
\]
Consequently **relative** synchronization \(\|\delta\|/|w|\to0\), with C nonzero where a direction is discussed, forces the projective direction toward \(e^\perp\). This is algebraic geometry of the readout, applicable independently of a convergence theorem for this recurrence.

Absolute approach to synchronized zero is insufficient. For example,
\[
x=t(1,-1,0),\quad y=t(1,1,-2),\quad C=2t^2e.
\]
The state tends to zero as \(t\to0\), while C points along e. This is a small algebraic counterexample, not a new model trajectory.

### Why the special direction is not forced

For any real desired \(d\in e^\perp\), take a near-unit synchronized state with
\(\eta=-e\times d/3\) and \(\xi=0\). Its first-order chirality is \(e\times\eta=d\). Every transverse direction is therefore available; the channel-independent Jacobian does not privilege one.

There are also exact invariant channel-equality subspaces. If \(\Omega_1=\Omega_2\), the symmetric pre-sync and phase-sync formulas preserve that equality. Whenever C is nonzero there, \(C\parallel(1,-1,0)\). The near-synchronized fixture
\[
\Omega=e+i t(1,1,-2),\qquad C=(-3t,3t,0)
\]
lies in that subspace. It excludes a universal \((-1,-1,2)\)-axis claim unless additional restrictions remove this family.

The nonlinear componentwise cubic has permutation symmetry, not arbitrary continuous rotation symmetry in the transverse plane. Thus linear degeneracy does **not** prove that all finite-amplitude nonlinear biases vanish. This packet establishes no weak nonlinear selection theorem. The observed near-special axis should be described as specific to these initial data and their transient, not necessarily equal to the literal initial imaginary perturbation and not an asymptotic axis proved from two runs.

