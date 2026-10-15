# Additional reviewer theorem — the profile bound weakly dominates the signed-component bound

**14 October 2026 · New GPT reviewer deduction, separate from Codex's submitted SIM04 findings**

This note proves a further relationship between two **already specified and evaluated** SIM04 families. It introduces no new bound family, data selection, damping operator, trajectory or numerical experiment. The submitted report correctly records the observed strict ordering and deliberately does not claim a universal ordering. That report remains accepted unchanged.

## Statement

For SIM04's exact definitions of `K_COMPONENT` and `P_PROFILE`,

\[
P_i\le K_i\quad\text{for each labeled center},\qquad
P\le K,
\]

for every pair of finite real pre-damping vectors. Consequently

\[
\boxed{\mathrm{BEST\_PRE}=\min(K,P)=P}
\]

in real arithmetic, not only on the recorded population. The inequality is weak: equal vectors and other special pairs give equality. SIM04's strict pair-level inequality in all 2,000 comparisons remains an empirical statement.

The result uses the specified positive, nonincreasing slope function

\[
k(s)=\frac{1+\log(1+s)-s/(1+s)}{[1+\log(1+s)]^2},\qquad s\ge0,
\]

with \(k(0)=1\). Its monotonicity is proved in the submitted `MATHEMATICAL_RESULTS.md`, §2. No assertion is made for an arbitrary replacement weight or damping rule.

## 1. Weighted matching cost on nonnegative components

Define

\[
C(a,b)=k(\min(a,b))^2(a-b)^2,\qquad a,b\ge0.
\]

For \(a<b\), direct differentiation gives

\[
\frac{\partial^2 C}{\partial a\,\partial b}
=4k(a)k'(a)(b-a)-2k(a)^2<0.
\]

For \(b<a\), the symmetric formula uses \(b\). The mixed derivative extends continuously across \(a=b\) with value \(-2k(a)^2\). Thus the mixed derivative is nonpositive throughout the nonnegative quadrant, with the usual one-sided interpretation on its boundary.

For \(a_1\le a_2\), \(b_1\le b_2\), integrating over the rectangle yields

\[
\begin{aligned}
&C(a_1,b_1)+C(a_2,b_2)-C(a_1,b_2)-C(a_2,b_1)\\
&\qquad=\int_{a_1}^{a_2}\int_{b_1}^{b_2}
\frac{\partial^2 C}{\partial a\,\partial b}(a,b)\,db\,da\le0.
\end{aligned}
\]

Therefore uncrossing an inverted match never increases the total cost. Repeatedly uncrossing gives sorted matching as a minimizer:

\[
\sum_{\alpha=1}^{3} C(p(x)_\alpha,p(y)_\alpha)
\le \sum_{\alpha=1}^{3}C(|x_\alpha|,|y_\alpha|),
\]

where \(p(x)=\operatorname{sort}(|x|)\) in ascending component order. The left side is exactly \(P_i^2\), including the prescribed derivative weights, not merely the unweighted profile distance.

## 2. Passing from signed intervals to absolute magnitudes

Let \(\kappa_\alpha\) be the specified maximum derivative on the signed interval between \(x_\alpha\) and \(y_\alpha\).

When the two components have the same sign, or either is zero,

\[
C(|x_\alpha|,|y_\alpha|)
=\kappa_\alpha^2(x_\alpha-y_\alpha)^2.
\]

When their signs are strictly opposite, the signed interval contains zero and \(\kappa_\alpha=1\). Since \(0<k\le1\),

\[
\begin{aligned}
C(|x_\alpha|,|y_\alpha|)
&\le (|x_\alpha|-|y_\alpha|)^2\\
&\le (|x_\alpha|+|y_\alpha|)^2\\
&=(x_\alpha-y_\alpha)^2
=\kappa_\alpha^2(x_\alpha-y_\alpha)^2.
\end{aligned}
\]

Summing and applying the weighted sorted-matching inequality proves

\[
P_i^2\le \sum_\alpha C(|x_\alpha|,|y_\alpha|)
\le \sum_\alpha\kappa_\alpha^2(x_\alpha-y_\alpha)^2=K_i^2.
\]

Both quantities are nonnegative. Taking square roots and averaging over the same eight labeled centers establishes \(P\le K\).

## 3. Consequences and limits

This strengthens the existing hierarchy to

\[
S\le P\le K\le Q\le T\le\Gamma\le\Omega.
\]

The finding explains why taking the minimum of K and P cannot improve on P under these definitions. There is no need to seek a different recorded state to decide which family wins: weak dominance is structural. The amount of numerical improvement and observed strictness still depend on the vectors.

The theorem does **not** establish that P is close to the target, remove norm-projection or signed-center-cancellation slack, certify phasewise nonincrease, or prove contraction of the complete dynamics. The reported zero sufficient-condition certificates are unchanged. Sorting is a symmetry reduction of a scalar damping readout, not a transformation of the evolving state, arbitrary rotation, or relabeling of centers.

The review's one numerical pass already produced all component bounds. A comparison of those existing reviewer arrays is consistent with the centerwise theorem at the fixed float64 tolerance; its largest signed P-minus-K excess is approximately \(1.39\times10^{-17}\). This is a roundoff-scale check, not the proof and not an extra data pass. Pair-level P remains strictly below K throughout the submitted population.

## Source and attribution

Definitions and inherited monotonicity: SIM04 `MATHEMATICAL_RESULTS.md`, §§2–4, and `SIM04_REPORT.md`, “Checked mathematics.” The weighted matching argument and resulting universal weak ordering are new to this reviewer note. They were not part of Codex's reported pre-evaluation theorem claims. No accepted source, numerical table or report has been revised.
