# Exact scalar branches and conditional completion theorem

This appendix supplements the main report's exact P03 threshold theorem. Every substitution below is an **analytical comparison of source operators**, not a historical repair or an executed dynamical model. All statements concern finite real scalar values unless stated otherwise.

## 1 Partner-dependent compression

P03 p.6 §2.5 gives \(C(x)=\min(x,\phi^{-1}R_{\rm partner})\). Hold the partner's current value fixed and denote its cap by \(a\). Substitution into the implicit structure gives
\[
 y=\min(y+b,a).
\]
Since \(y\leq a\), either \(y<a\), forcing \(b=0\), or \(y=a\), requiring \(b\geq0\). Thus
\[
 \mathcal S_{\min}(b)=
 \begin{cases}
 \varnothing,&b<0,\\
 (-\infty,a],&b=0,\\
 \{a\},&b>0.
 \end{cases}
\]
For nonnegative amplitudes intersect with \([0,\infty)\). In particular, a negative cap admits no nonnegative solution. If the partner is instead an unknown next-state value, this is a coupled system and the fixed-cap classification no longer settles it. The source does not select the partner or timing.

## 2 All branches for the positive-output logarithmic operator

P07 p.3 defines \(C_+(x)=\exp(\operatorname{clip}(\operatorname{sign}(x)\log(|x|+\epsilon),-L,L))\).
Assume \(L>0,\epsilon>0\); put \(a=e^{-L},A=e^L,x=y+b\). Every solution of \(y=C_+(y+b)\) is positive and must occur in the following table. Test the stated inequalities for every candidate; take the union and remove duplicates at clamp boundaries.

| Input branch | Candidate or family | Necessary and sufficient branch tests |
|---|---|---|
| \(x=0\) | \(y=1,b=-1\) | Exactly this equality |
| \(x>0\), lower plateau | \(y=a\) | \(x=a+b>0,\ x+\epsilon\leq a\) |
| \(x>0\), unclipped | Every eligible y, only if \(b=-\epsilon\) | \(x=y-\epsilon>0,\ a\leq y\leq A\) |
| \(x>0\), upper plateau | \(y=A\) | \(x=A+b>0,\ x+\epsilon\geq A\) |
| \(x<0\), lower plateau | \(y=a\) | \(x=a+b<0,\ (\epsilon-x)^{-1}\leq a\) |
| \(x<0\), unclipped | \(y_\pm=(\epsilon-b\pm\sqrt{(b-\epsilon)^2-4})/2\) | Discriminant nonnegative, \(y_\pm>0,\ x=y_\pm+b<0,\ a\leq y_\pm\leq A\) |
| \(x<0\), upper plateau | \(y=A\) | \(x=A+b<0,\ (\epsilon-x)^{-1}\geq A\) |

**Proof.** For positive x the operator is \(\operatorname{clip}(x+\epsilon,a,A)\); separate its plateaus and linear interior. Interior equality requires \(y=y+b+\epsilon\), i.e. \(b=-\epsilon\). For negative x it is \(\operatorname{clip}(1/(\epsilon-x),a,A)\). The interior equation
\[
 y=\frac1{\epsilon-y-b}
 \quad\Longleftrightarrow\quad y^2+(b-\epsilon)y+1=0
\]
gives the quadratic candidates, with the input/sign/plateau tests preventing extraneous roots. Zero input is defined separately. These cases exhaust the domain.

At \(L=10,\epsilon=10^{-6},b=-3\), both roots are positive, unclipped and have negative input: approximately \(0.381966\) and \(2.618035\). Both solve the substituted relation. Thus this historical alternate compressor does not generally restore uniqueness. At \(b=-\epsilon\), the positive-input interior gives a continuum of roots. These facts are source-operator comparisons; P03 does not direct the reader to substitute P07's operator.

If \(L=0\), the whole operator is the constant 1 and the relation has the single solution \(y=1\), independently of b. This degenerate case is outside the displayed table's assumption.

## 3 Later signed operator

For \(C_s(x)=\operatorname{sign}(x)\operatorname{clip}(|x|+\epsilon,a,A)\), with \(C_s(0)=0\), all scalar candidates for \(y=C_s(y+b)\) can likewise be specified exhaustively:

* Zero: \(y=0\) is allowed exactly when \(b=0\).
* For each sign \(s\in\{-1,+1\}\), the lower plateau candidate \(y=sa\) is allowed when \(s(y+b)>0\) and \(|y+b|+\epsilon\leq a\).
* For each sign s, the upper plateau candidate \(y=sA\) is allowed when \(s(y+b)>0\) and \(|y+b|+\epsilon\geq A\).
* On the interior of sign s, the equality is \(y=y+b+s\epsilon\). It therefore requires \(b=-s\epsilon\), \(sy>0\), \(s(y+b)>0\), and \(a\leq |y|\leq A\). All y satisfying those conditions are roots.

These conditions include boundary overlap deliberately. For the actual later defaults \(a>\epsilon>0\), b=0 has precisely the three roots \(0,\pm A\): the interior requires nonzero b; lower plateaus fail because \(a+\epsilon>a\); the upper plateaus succeed. Oddness and sign preservation are not sufficient for unique implicit solvability.

## 4 Changing the temporal coefficient

**New proposal family, not the historical equation.** Insert coefficient a before the centered temporal second difference. For known current x, previous z and feedback F, the equation becomes
\[
 y=C_\lambda(a y+d),\qquad d=(1-2a)x+az+F.
\]
With P03's \(q=\phi^{-1}\), the complete branch conditions are:

* If \(a\ne1\), the lower candidate is \(y=d/(1-a)\), valid exactly when \(a y+d<\lambda\), equivalently \(y<\lambda\).
* If \(a=1\), the lower branch exists exactly for d=0 and then contains all \(y<\lambda\).
* If \(a\ne1/q\), the upper candidate is \(y=qd/(1-qa)\), valid exactly when \(a y+d=d/(1-qa)\geq\lambda\).
* If \(a=1/q\), the upper branch exists exactly for d=0 and then contains all \(y\geq q\lambda\).

The union of admissible branches is the whole solution set. This follows by solving \(y=ay+d\) and \(y=q(ay+d)\) on their respective domains, retaining singular denominators as separate cases.

Adding a coefficient alone does not guarantee uniqueness. For \(a=1/2,\lambda=1,d=0.4\), the lower candidate is 0.8 and the upper candidate is approximately 0.3578, whose input is below 1 and therefore invalid. For \(d=0.6\), the lower candidate is 1.2 and invalid; the upper input is approximately 0.8683 and also invalid: **there is still no root**. The jump in C remains consequential even when \(|a|<1\).

## 5 A sufficient condition for a new well-defined implicit model

Let E be a Banach space and \(\widetilde C:E\to E\) be globally Lipschitz with constant K. For fixed d, define \(T(y)=\widetilde C(a y+d)\). If \(\rho=|a|K<1\), then
\[
 \|T(y)-T(z)\|\leq\rho\|y-z\|.
\]
Starting from any \(y_0\), successive differences satisfy
\(\|y_{m+1}-y_m\|\leq\rho^m\|y_1-y_0\|\). The geometric-series bound makes the sequence Cauchy; completeness gives a limit \(y_*\), and continuity gives \(T(y_*)=y_*\). For two roots,
\(\|y_*-z_*\|\leq\rho\|y_*-z_*\|\), hence they coincide.

The same proof works on a closed invariant subset of E. Without invariance, a local Lipschitz inequality alone does not establish existence in the intended domain. This is a sufficient theorem for a **newly specified** model, not a property of P03's discontinuous threshold operator. No fixed-point iteration was executed here.

## 6 Mathematical reversal versus an inverse calculation

For an autonomous bijective discrete map F, an involution T is a reversor if \(TFT=F^{-1}\). For a nonautonomous source map \(F_n\), time reversal must also specify the reversal of the clock and forcing schedule. An invertible phase shift, an odd compressor, a reciprocal graph, a geometric mirror, or a sector-exchange matrix does not independently establish that identity.

The original implicit relation is not a total single-valued F. Threshold compression is noninjective. The later finite complex map is invertible when its compression strength is below one, but its inverse reverses the factor order and inverts amplification/damping. The later stochastic R/D model also requires specifying what happens to noise realizations. These distinctions explain why no common physical time-reversal law can be recovered merely from the recurring word “mirror.”
