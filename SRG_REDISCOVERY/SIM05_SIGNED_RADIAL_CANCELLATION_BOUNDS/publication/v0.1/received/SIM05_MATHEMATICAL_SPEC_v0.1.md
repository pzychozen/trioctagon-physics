# SIM05 mathematical specification — signed radial intervals and collective cancellation

**14 October 2026 · New GPT proposal for Codex verification before numerical evaluation.**

This is a new bound construction, not an accepted SIM04 result and not a new motion law. The inherited authorities are SIM04's `MATHEMATICAL_RESULTS.md` and the subsequent `ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md`. The source operator, actual histories and their accepted records remain unchanged.

## 1. Question and information boundary

Can bounds that retain the **sign of each center's speed difference** through collective averaging remove a useful part of SIM04's norm-projection and center-cancellation overestimate?

The inputs are the already saved, outcome-free profiles

\[
p=\operatorname{sort}(|w_c|),\qquad q=\operatorname{sort}(|w_d|),\qquad
P_i=\|k(\min(p,q))\odot(p-q)\|_2.
\]

Use the existing stored `P_center`; do not rerun SIM04 to recreate it. Here c>d, and the center label i remains fixed. All signed differences are c minus d. Sorting acts within the three absolute components of a center, never across centers. It is a symmetry of this scalar readout, not arbitrary rotation invariance.

For the derivations define

\[
b(s)=1+\log(1+s),\quad d(s)=s/b(s),\quad F(p)=\|d(p)\|_2.
\]

The desired center difference is \(\delta_i=F(p)-F(q)\); the collective signed difference is \(\Delta u=\frac18\sum_i\delta_i\).

**Do not evaluate F(p), F(q), or componentwise d on actual saved records.** Do not use saved successors, losses, retention, post speeds or prior outcome differences to build a bound. The new calculations may use profiles, their squares/norms/maxima, the specified logarithmic derivative weights, and the analytic norm envelopes below. Exact d/F evaluation is permitted only on the fixed synthetic fixtures.

This prohibition prevents replacing the proposed bound by an exact re-evaluation of the answer. It is not a claim that the input lacks enough information to compute the answer exactly. These are conditional mathematical enclosures of a known readout on realized intermediates, not predictions from mean speed alone.

## 2. A monotone derivative in squared-component coordinates

SIM04 established

\[
k(s)=\frac{b(s)-s/(1+s)}{b(s)^2}>0,\qquad k'(s)<0,\quad k(0)=1.
\]

Define a new scalar function and derivative weight:

\[
\Phi(z)=\frac{z}{[1+\log(1+\sqrt z)]^2},\quad z\ge0,
\qquad \vartheta(s)=\frac{k(s)}{b(s)}
=\frac{b(s)-s/(1+s)}{b(s)^3}.
\]

For z>0, differentiating through s=sqrt(z) gives

\[
\Phi'(z)=\vartheta(\sqrt z).
\]

The right derivative at zero is one. Since

\[
\vartheta'(s)=\frac{k'(s)}{b(s)}-
\frac{k(s)}{(1+s)b(s)^2}<0,
\]

Phi is increasing and concave on [0,infinity), with Phi(0)=0. These are analytic statements. Finite derivative samples do not constitute their proofs.

## 3. Signed bounds for the squared-speed difference

For each paired profile component alpha, put

\[
x_\alpha=p_\alpha^2,\quad y_\alpha=q_\alpha^2,\quad
h_\alpha=x_\alpha-y_\alpha,\quad
z^-_\alpha=\min(x_\alpha,y_\alpha),\quad
z^+_\alpha=\max(x_\alpha,y_\alpha).
\]

Numerically use `(p-q)*(p+q)` for h to avoid subtracting nearby squares. Retain/check the direct subtraction as a local algebra residual if desired; it is not a new trajectory calculation.

There are exactly two fixed resolutions, **J=1 and J=4**. For J=4 use the five nodes

\[
z_{\alpha,r}=z^-_\alpha+(r/4)(z^+_\alpha-z^-_\alpha),\qquad r=0,1,2,3,4.
\]

Evaluate \(t_{\alpha,r}=\vartheta(\sqrt{z_{\alpha,r}})\). Reuse nodes 0 and 4 for J=1. Define

\[
\theta^-_{\alpha,1}=t_{\alpha,4},\quad
\theta^+_{\alpha,1}=t_{\alpha,0},
\]
\[
\theta^-_{\alpha,4}=\tfrac14\sum_{r=1}^4t_{\alpha,r},\quad
\theta^+_{\alpha,4}=\tfrac14\sum_{r=0}^3t_{\alpha,r}.
\]

These are lower and upper Darboux averages of a decreasing derivative. Therefore, including the zero-length interval,

\[
\Phi(x_\alpha)-\Phi(y_\alpha)
\in[\min(h_\alpha\theta^-_{\alpha,J},h_\alpha\theta^+_{\alpha,J}),
       \max(h_\alpha\theta^-_{\alpha,J},h_\alpha\theta^+_{\alpha,J})].
\]

**Sum the signed component intervals**, not their absolute values. Call the sums \([N^-_J,N^+_J]\). They enclose

\[
F(p)^2-F(q)^2=\sum_\alpha[\Phi(x_\alpha)-\Phi(y_\alpha)].
\]

The J=4 interval is contained in the J=1 interval in exact arithmetic, by refinement of the same monotone partition. These four subintervals are auxiliary mathematical intervals, not time steps or additional simulated states. No adaptive subdivisions, quadrature search or extra resolution is authorized.

## 4. Denominator bounds without computing the damped endpoint norms

For a nonnegative three-component profile p, let m=||p|| and M=max(p). Define

\[
L(p)=\frac{m}{b(M)},\qquad U(p)=\frac{m}{b(m/\sqrt3)}.
\]

Both are zero for p=0. They satisfy

\[
L(p)\le F(p)\le U(p).
\]

**Lower bound:** b(p_alpha)<=b(M), so sum p_alpha^2/b(p_alpha)^2 >= m^2/b(M)^2.

**Upper bound:** concavity of Phi gives

\[
F(p)^2=\sum_{\alpha=1}^3\Phi(p_\alpha^2)
\le3\Phi(m^2/3)=\frac{m^2}{b(m/\sqrt3)^2}.
\]

These closed-form envelopes are allowed computations even when a special profile makes one of them exact. Do not tighten them by summing the three exact damped-component squares on source records.

Except when p=q=0, \(D^-=L(p)+L(q)>0\) and \(D^+=U(p)+U(q)\). Rationalization gives

\[
\delta_i=\frac{F(p)^2-F(q)^2}{F(p)+F(q)}.
\]

An interval for delta_i is the minimum/maximum of the four quotients

\[
N^-_J/D^-,\quad N^-_J/D^+,\quad N^+_J/D^-,\quad N^+_J/D^+.
\]

Intersect it with the independently valid norm-difference interval

\[
[L(p)-U(q),\ U(p)-L(q)].
\]

Denote the result \(I^{raw}_{i,J}\). If p=q=0, define it directly as [0,0]. If p=q componentwise, the signed numerator is zero and the interval must be [0,0], regardless of different signs/permutations in the original vectors.

Finally intersect with SIM04's existing center bound:

\[
I_{i,J}=I^{raw}_{i,J}\cap[-P_i,P_i]=[\ell_{i,J},r_{i,J}].
\]

This is a mathematically justified intersection of independently valid enclosures, not clipping a measured failure. Keep the raw interval, every intersection endpoint and the identity of active endpoints. No particular ordering of the raw radial estimate and P is assumed. All exact-real intervals are nonempty because they contain the same delta_i.

J=4 remains contained in J=1 after the fixed intersections. Finite-precision handling of nearly empty intervals is prescribed in the work order; never conceal a substantive empty intersection.

## 5. Average first, then take an absolute value

Set

\[
\mu_{i,J}=(\ell_{i,J}+r_{i,J})/2,\qquad
\epsilon_{i,J}=(r_{i,J}-\ell_{i,J})/2.
\]

The collective signed interval is

\[
\Delta u\in[\bar\ell_J,\bar r_J]
=[\bar\mu_J-\bar\epsilon_J,\bar\mu_J+\bar\epsilon_J].
\]

Define the fixed upper families

\[
B^{signed}_J=\max(|\bar\ell_J|,|\bar r_J|)
=|\bar\mu_J|+\bar\epsilon_J,
\]
\[
B^{unsigned}_J=\frac18\sum_i\max(|\ell_{i,J}|,|r_{i,J}|)
=\overline{|\mu_J|}+\bar\epsilon_J.
\]

The difference isolates the loss from taking absolute values before averaging **for the same interval information**:

\[
B^{unsigned}_J-B^{signed}_J
=\overline{|\mu_J|}-|\bar\mu_J|\ge0.
\]

This does not claim the interval midpoints equal the true center differences. The residual average radius remains in the bound and measures enclosure uncertainty.

There is also a lower bound on the collective absolute difference:

\[
A_J=\begin{cases}
0,&\bar\ell_J\le0\le\bar r_J,\\
\min(|\bar\ell_J|,|\bar r_J|),&\text{otherwise}.
\end{cases}
\]

Thus

\[
A_J\le |\Delta u|\le B^{signed}_J\le B^{unsigned}_J\le P,
\]

where P=mean(P_i). Refinement yields \(A_4\ge A_1\), \(B^{signed}_4\le B^{signed}_1\), and \(B^{unsigned}_4\le B^{unsigned}_1\). No strict improvement is promised.

Retain raw pre-P collective intervals as diagnostics. The five primary upper-bound families are **P_PROFILE** (inherited), **RADIAL_1_UNSIGNED**, **RADIAL_1_SIGNED**, **RADIAL_4_UNSIGNED**, **RADIAL_4_SIGNED**. Retain both signed-family lower bounds. Do not add outcome-selected families.

## 6. Two-sided population variance and honest sufficient conditions

For m complete cycle values,

\[
\operatorname{Var}(u)=\frac1{m^2}\sum_{c>d}(u_c-u_d)^2.
\]

Therefore

\[
W^-_J=\frac1{m^2}\sum_{c>d}A_{cd,J}^2
\le\operatorname{Var}(u^+)\le
W^+_J=\frac1{m^2}\sum_{c>d}(B^{signed}_{cd,J})^2.
\]

All-five uses ten unordered pairs and denominator 25; new-four reuses six pairs and denominator 16. The intervals for different pairs need not be independent or jointly attainable at all endpoints for these inequalities to be valid. Do not claim the summed bounds are sharp extrema over compatible cycle values.

For a reference variance V_ref:

- W^+_J < V_ref suffices for decrease.
- W^-_J > V_ref suffices for increase.
- Otherwise this sufficient test decides neither.

Use the specified numerical margin classification, not a demand for any number of successes. Evaluate **incoming** and **pre-damping** references separately after sealing all analytic bounds. Actual changes, evaluated later from saved speeds, remain a distinct column. An increasing phase is as legitimate as a decreasing phase.

For a declared speed tolerance epsilon>=0, B_signed<=epsilon suffices for the pair difference<=epsilon; W_plus<=epsilon^2 suffices for population SD<=epsilon. No epsilon is fitted to the outcomes in this task.

## 7. What the new slack comparison means

After outcomes are joined, let S=abs(mean true center differences). The effective J=4 upper bound satisfies

\[
P-S=(P-B^{unsigned}_4)+(B^{unsigned}_4-B^{signed}_4)+(B^{signed}_4-S).
\]

The three nonnegative exact-real gaps respectively measure improvement from the center enclosures, the additional benefit of preserving midpoint signs through averaging, and remaining upper-bound slack. They are not causal shares of the dynamics. Keep all signed numerical residuals, including roundoff, and compare against the separately reduced accepted collective difference.

Compare J=1 and J=4 to expose how much uncertainty comes from the fixed derivative intervals. Compare raw versus P-intersected intervals to disclose how much of the guarantee is inherited from P. Report unresolved center signs and collective signs; do not infer a sign from an interval straddling zero.

## 8. Limits and required proof review

Codex must independently verify each derivation before the selected-data pass. The finite float64 evaluation is not outward-rounded interval certification. The analytic enclosures are real-valued statements; observed margins are checked at fixed tolerances.

No theorem here requires complete-update contraction, eventual recurrence or convergence. The input profiles already condition on realized sequential forcing and retained state. A narrower bound means a better scalar comparison, not altered damping or motion, a causal intervention, generalization to unseen states, or a memory-performance claim. The four-subinterval rule is fixed before the data evaluation. If it remains too loose, report that limitation rather than increasing resolution until a certificate appears.
