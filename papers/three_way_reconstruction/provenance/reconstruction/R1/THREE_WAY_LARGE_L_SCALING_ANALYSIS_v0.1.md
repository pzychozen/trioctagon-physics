# THREE-WAY LARGE-L SCALING ANALYSIS v0.1

Date: 5 October 2026. Initial-stage status: a work-order stop condition was triggered. **Authorized follow-ups: Section 12 proves the intermediate profile and matching; Section 13 identifies the exact involution behind \(s\mapsto2/s\); Section 14 gives the \(V_4\) quotient, zero/pole orbits, and inner/outer chart organization, distinguishing the global \(y\)-action from its lifts to \(x\).** Sections 1–11 retain the initial-stage findings and scope record.

**Initial-stage finding:** the proposed bulk, lock, outer, and inner profiles are correct, with the exclusions and normalizations below. An additional turning-point scale occurs at distance \(O(L^{-1/2})\) from each lock. Its limiting profile was initially left unresolved under the stop instruction and is now proved in Section 12 under the follow-up authorization. The report does not claim a complete uniform description of the entire graph.

All scripts, data, and figures are external to the repository. No kernel, UI, paper, or repository files were modified; no commits were made.

## 1. Exact family and scope

Only the real one-parameter family
\[
N_L(x)=Lx^4-Lx^2+1,\qquad D_L(x)=x^4-Lx^2+L,
\]
\[
\boxed{f_L(x)=N_L(x)/D_L(x),\qquad L>0}
\]
is studied. The finite-valued domain of \(f_L\) excludes \(D_L=0\). The literal reciprocal \(g_L=1/f_L\) requires both \(N_L\ne0\) and \(D_L\ne0\). When useful, \(D_L/N_L\) gives its natural rational extension across a pole of \(f_L\); that extension is explicitly distinguished below.

The exact algebra gives
\[
f_L(-x)=f_L(x),\qquad
N_L(1/x)=D_L(x)/x^4,\qquad
D_L(1/x)=N_L(x)/x^4.
\]
Consequently,
\[
\boxed{f_L(1/x)=g_L(x)}
\]
where the finite expressions are defined, and as an identity of rational functions.

Since
\[
N_L-D_L=(L-1)(x^4-1),\qquad D_L(\pm1)=1,
\]
the two real locks satisfy
\[
\boxed{f_L(\pm1)=g_L(\pm1)=1\quad\text{for every }L>0.}
\]
For \(L\ne1\), these are the only real solutions of \(f_L=1\). At \(L=1\), the real function is identically one. Other useful exact values are
\[
f_L(0)=L^{-1},\quad g_L(0)=L,\quad
\lim_{|x|\to\infty}f_L(x)=L,\quad
\lim_{|x|\to\infty}g_L(x)=L^{-1}.
\]

This is the diagonal slice \(A=B=L\) of the previously recovered **minus-sign** family. The historical \((9,9)\) example is simply \(L=9\), with no privileged mathematical status. Evenness, reciprocity, and the locks were established in the preceding reconstruction; they are re-derived here for self-containment. The later plus-sign formula is not substituted into this calculation. This work does not repeat the source audit or claim priority over the broader mathematical literature.

Repository reference: current trioctagon-physics checkout, HEAD **fe5758f21cc185665c13d8585674b362e36dad35**. The [run manifest](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/run_manifest.json) records the pre-existing dirty status and verifies that HEAD and status were unchanged by the computation. The supplied large-coefficient work order governs this report; earlier questions about rotations and mirrors are outside its scope.

## 2. Fixed-scale limit

Divide by \(L\):
\[
f_L(x)=\frac{x^4-x^2+L^{-1}}{L^{-1}x^4-x^2+1}.
\]
For fixed real \(x\ne\pm1\), the limiting denominator is nonzero, and
\[
\frac{x^2(x^2-1)}{1-x^2}=-x^2.
\]
The exact error identity is stronger:
\[
\boxed{f_L(x)+x^2=\frac{x^6+1}{x^4+L(1-x^2)}.}
\]
Thus the actual pointwise limit on the real line is
\[
F_\infty(x)=
\begin{cases}
-x^2,&x\ne-1,1,\\
1,&x=-1,1.
\end{cases}
\]
Each fixed \(x\) is eventually in the domain. A possible pole at an isolated finite value of \(L\) does not obstruct that limit.

For \(g_L\),
\[
\boxed{g_L(x)+x^{-2}=\frac{x^6+1}{x^2N_L(x)}}
\]
where defined. Therefore
\[
g_L(x)\longrightarrow -x^{-2}\quad(x\ne0,\pm1),\qquad
g_L(\pm1)=1,\qquad g_L(0)=L\longrightarrow+\infty.
\]
There is no finite real pointwise limit of \(g_L\) at zero.

**Locally uniform convergence, with a proof.** Let \(K\) be a compact subset of \(\mathbb R\setminus\{-1,1\}\). Set
\[
\delta=\min_K|1-x^2|>0,\quad
M_4=\max_K|x|^4,\quad Q=\max_K|x^6+1|.
\]
For \(L\delta>M_4\),
\[
\sup_K|f_L+x^2|\le\frac{Q}{L\delta-M_4}=O_K(L^{-1}).
\]
In particular, there are eventually no poles on \(K\).

For a compact \(K\subset\mathbb R\setminus\{0,-1,1\}\), also set
\[
m_2=\min_Kx^2>0,\qquad c=\min_K|x^2(x^2-1)|>0.
\]
For sufficiently large \(L\), both domains contain \(K\), and
\[
\sup_K|g_L+x^{-2}|\le\frac{Q}{m_2(Lc-1)}=O_K(L^{-1}).
\]
These are the uniform statements proved here; the numerical samples below are not substitutes for them.

**Why the locks survive.** At \(x=\pm1\), the leading numerator and denominator after division by \(L\) both vanish. Their \(L^{-1}\) terms are equal, so the ratio remains \(+1\). Cancelling the leading factors before setting \(x=\pm1\) loses this information. The two orders of limiting operations disagree:
\[
\lim_{L\to\infty}f_L(1)=1,\qquad
\lim_{x\to1,\ x\ne1}\left(\lim_{L\to\infty}f_L(x)\right)=-1.
\]
The statement at \(-1\) follows by evenness.

There is no uniform approximation by \(-x^2\) on a neighborhood containing a lock: the lock itself gives error two, and poles approach it. Even after assigning the correct exceptional point value in \(F_\infty\), the nearby poles prevent uniform convergence over a fixed neighborhood on the common finite domain.

Nor does the approximation hold uniformly over an unbounded real set extending to infinity: for each finite \(L\), \(f_L\) approaches \(L\), whereas \(-x^2\) is unbounded. The outer scaling below resolves this.

At the origin, **absolute** convergence of \(f_L\) to \(-x^2\) is locally uniform. The inner scaling is needed to resolve the leading size and moving zeros there, not to repair a failure of absolute convergence of \(f_L\) near zero. For \(g_L\), the origin is a genuine divergence region.

## 3. Exact poles and zeros

Put \(y=x^2\). The quadratic formula gives
\[
y_{p,\pm}=\frac{L\pm\sqrt{L^2-4L}}2,\qquad
y_{z,\pm}=\frac{1\pm\sqrt{1-4/L}}2.
\]

| Parameter | Real poles of \(f_L\) | Real zeros of \(f_L\) |
|---|---|---|
| \(0<L<4\) | None | None |
| \(L=4\) | \(\pm\sqrt2\), each of order two | \(\pm1/\sqrt2\), each of order two |
| \(L>4\) | Four simple poles | Four simple zeros |

For \(0<L<4\), both quadratics have negative discriminants and positive leading coefficients, so neither vanishes on the real line. At \(L=4\),
\[
D_4=(x^2-2)^2,\qquad N_4=(2x^2-1)^2.
\]
For \(L>4\), both roots of each quadratic are positive and distinct, producing the stated four real roots.

There is no hidden cancellation on the large-\(L\) branch. If \(L\ne1\) and numerator and denominator shared a root, subtraction would give \(x^4=1\). Substitution into \(D_L\) then gives either \(1\) or \(1+2L\), both nonzero for \(L>0\). Equivalently,
\[
\operatorname{Res}_x(N_L,D_L)=(L-1)^4(2L+1)^2.
\]
At \(L=1\), numerator and denominator coincide, and \(f_1=g_1=1\) on the entire real line. Their common polynomial \(x^4-x^2+1\) is strictly positive there. This known degeneration is separate from the \(L>4\) asymptotic branch.

For a stable and transparent root parametrization, define
\[
q=\sqrt{\frac{1+\sqrt{1-4/L}}2}\qquad(L\ge4).
\]
The positive roots can then be named
\[
\boxed{
z_i=\frac1{\sqrt L\,q},\quad z_n=q,\quad
p_n=\frac1q,\quad p_o=\sqrt L\,q.
}
\]
Subscripts denote inner, near-lock, and outer. For \(L>4\),
\[
0<z_i<z_n<1<p_n<p_o.
\]
The negative roots are their negatives. The exact pairings are
\[
p_nz_n=p_oz_i=1,\qquad
p_o=\sqrt L\,z_n,\qquad z_i=p_n/\sqrt L.
\]
The zeros of \(f_L\) are poles of \(g_L\); the poles of \(f_L\) are zeros of the rational extension \(D_L/N_L\). The literal composition \(1/f_L\) is not defined at a pole of \(f_L\).

**Asymptotic coefficients.** Write \(\varepsilon=L^{-1}\). Binomial expansion gives
\[
\sqrt{1-4\varepsilon}
=1-2\varepsilon-2\varepsilon^2-4\varepsilon^3-10\varepsilon^4+O(\varepsilon^5),
\]
hence
\[
q^2=1-\varepsilon-\varepsilon^2-2\varepsilon^3-5\varepsilon^4+O(\varepsilon^5).
\]
Taking the positive square root and its inverse yields
\[
\begin{aligned}
a(\varepsilon):=1/q
&=1+\tfrac12\varepsilon+\tfrac78\varepsilon^2+\tfrac{33}{16}\varepsilon^3
+\tfrac{715}{128}\varepsilon^4+O(\varepsilon^5),\\
b(\varepsilon):=q
&=1-\tfrac12\varepsilon-\tfrac58\varepsilon^2-\tfrac{21}{16}\varepsilon^3
-\tfrac{429}{128}\varepsilon^4+O(\varepsilon^5).
\end{aligned}
\]
These are analytic expansions near \(\varepsilon=0\), not fitted coefficients. They give all four root expansions:
\[
\boxed{p_n=a(1/L),\quad p_o=\sqrt L\,b(1/L),\quad
z_n=b(1/L),\quad z_i=L^{-1/2}a(1/L).}
\]
For example,
\[
p_o=\sqrt L-\frac1{2\sqrt L}-\frac5{8L^{3/2}}-\frac{21}{16L^{5/2}}+O(L^{-7/2}),
\]
\[
z_i=L^{-1/2}+\frac1{2L^{3/2}}+\frac7{8L^{5/2}}+\frac{33}{16L^{7/2}}+O(L^{-9/2}).
\]

As \(L\) increases above four, \(q\) increases to one. Thus \(z_n\) increases to one and \(p_n\) decreases to one. Also \(p_o\) increases without bound, and \(z_i=1/p_o\) decreases to zero. The real root-creation threshold is \(L=4\).

## 4. Boundary layer at \(\pm1\)

Use the proposed coordinate exactly:
\[
x^2=1+\frac{s}{L}.
\]
For real \(x\), its domain is \(s\ge-L\); every fixed bounded \(s\)-interval is admissible for sufficiently large \(L\). Substitution gives
\[
\boxed{
H_L(s):=f_L\!\left(\sqrt{1+s/L}\right)
=\frac{1+s+s^2/L}{1-s+2s/L+s^2/L^2}.
}
\]
Therefore
\[
\boxed{H_L(s)\longrightarrow H(s)=\frac{1+s}{1-s}\qquad(s\ne1).}
\]
On each bounded compact \(s\)-set excluding one, the denominator is eventually bounded away from zero and the coefficient errors are \(O(L^{-1})\). Subtracting the two quotients proves uniform \(O(L^{-1})\) convergence there.

The corresponding reciprocal profile is
\[
H_L(s)^{-1}\longrightarrow\frac{1-s}{1+s},
\]
uniformly on compact sets excluding \(s=-1\), if interpreted using the rational extension at a moving pole of \(H_L\). On the literal reciprocal domain the same estimate holds wherever defined.

The exact lock is \(s=0\), with value one. The positive near-lock zero and pole occur at
\[
\begin{aligned}
s_z&=L(z_n^2-1)
=-1-L^{-1}-2L^{-2}-5L^{-3}+O(L^{-4}),\\
s_p&=L(p_n^2-1)
=1+2L^{-1}+5L^{-2}+14L^{-3}+O(L^{-4}).
\end{aligned}
\]
Thus the limiting zero is \(s=-1\) and limiting pole \(s=1\). At the excluded coordinate \(s=1\), the exact value is
\[
H_L(1)=L,
\]
which confirms the need for the exclusion. The finite-\(L\) zero and pole are not exactly at their limiting coordinates.

For the direct coordinate \(x=1+u/L\),
\[
s=2u+u^2/L,\qquad
\boxed{f_L(1+u/L)\longrightarrow\frac{1+2u}{1-2u}\quad(u\ne\tfrac12).}
\]
The lock, zero, and pole approach \(u=0,-1/2,+1/2\). Around the negative lock:
\[
f_L(-1-u/L)=f_L(1+u/L),
\]
or, with an increasing coordinate,
\[
f_L(-1+u/L)\longrightarrow\frac{1-2u}{1+2u}\quad(u\ne-\tfrac12).
\]

Each root lies approximately \(1/(2L)\) from its lock, and the positive near-zero to near-pole gap is
\[
p_n-z_n=L^{-1}+\tfrac32L^{-2}+\tfrac{27}{8}L^{-3}+O(L^{-4}).
\]
This establishes the \(O(L^{-1})\) transition width. Its sharpening is also exact at the lock:
\[
f_L'(1)=4(L-1),\qquad f_L'(-1)=-4(L-1).
\]
The limiting layer tends to \(-1\) as \(|s|\to\infty\), matching the local value of the bulk profile as \(x\to\pm1\).

## 5. Outer \(x\sim\sqrt L\) scaling

Set \(x=\sqrt L\,\xi\). Direct substitution gives the correct normalization:
\[
\boxed{
O_L(\xi):=\frac{f_L(\sqrt L\,\xi)}L
=\frac{\xi^4-\xi^2/L+L^{-3}}{\xi^4-\xi^2+L^{-1}}.
}
\]
For fixed \(\xi\ne0,\pm1\),
\[
\boxed{O_L(\xi)\longrightarrow O(\xi)=\frac{\xi^2}{\xi^2-1}.}
\]
On compact sets excluding \(0,\pm1\), convergence is uniformly \(O(L^{-1})\), because the limiting denominator is separated from zero. In particular,
\[
f_L(\sqrt L\,\xi)=L\,\frac{\xi^2}{\xi^2-1}+O(1)
\]
there. The raw function is generally of order \(L\), not order one.

The positive outer pole in this coordinate is
\[
\xi_o=p_o/\sqrt L=q
=1-\frac1{2L}-\frac5{8L^2}-\frac{21}{16L^3}+O(L^{-4}).
\]
For \(L>4\), as \(\xi\) increases through this pole, \(f_L\) goes to \(-\infty\) from the left and \(+\infty\) from the right. Its numerator is positive at that pole and its denominator changes from negative to positive. Evenness determines the negative side.

The limiting singular coordinates must not be inserted into the finite limiting expression:
\[
O_L(\pm1)=L-1+L^{-2},\qquad
f_L(\pm\sqrt L)=L^2-L+L^{-1}.
\]
At \(\xi=0\), however, \(O_L(0)=L^{-2}\to0\), agreeing with the continuous extension \(O(0)=0\). This isolated agreement does **not** give uniform convergence around zero: the near-lock poles occur at \(\xi=\pm p_n/\sqrt L\) and approach zero.

The reciprocal normalization is also useful:
\[
\frac{L}{f_L(\sqrt L\,\xi)}
=\frac1{O_L(\xi)}
\longrightarrow\frac{\xi^2-1}{\xi^2}.
\]
This converges locally uniformly away from zero when evaluated as the rational extension \(L D_L/N_L\). It remains finite through the outer poles of \(f_L\), where that extension is zero. If used literally as \(L/f_L\), exclude those moving pole points from its finite-\(L\) domain.

For \(|\xi|\to\infty\), \(O(\xi)\to1\), matching the exact horizontal asymptote \(f_L\to L\).

## 6. Reciprocal inner scaling

Set \(x=\xi/\sqrt L\). Inversion sends this point to \(\sqrt L/\xi\), which is an outer point. Hence, for \(\xi\ne0\) and on the common domain,
\[
\boxed{
I_L(\xi):=L f_L(\xi/\sqrt L)=\frac1{O_L(1/\xi)}.
}
\]
Substituting, or using this exact identity, gives
\[
\boxed{
I_L(\xi)=\frac{1-\xi^2+\xi^4/L}{1-\xi^2/L+\xi^4/L^3}
\longrightarrow I(\xi)=1-\xi^2.
}
\]
The denominator tends uniformly to one on every bounded \(\xi\)-set. Thus convergence is locally uniform with error \(O(L^{-1})\) on the entire real \(\xi\)-line, including zero and \(\pm1\). The rational expression also explains its continuous evaluation at \(\xi=0\), where \(I_L(0)=1\).

For the reciprocal function,
\[
\boxed{
\frac{g_L(\xi/\sqrt L)}L
=\frac1{I_L(\xi)}
=O_L(1/\xi)
\longrightarrow\frac1{1-\xi^2}.
}
\]
This last convergence is locally uniform with error \(O(L^{-1})\) on compact sets excluding \(\xi=\pm1\). It holds at zero by direct evaluation, \(g_L(0)/L=1\); the intermediate expression \(O_L(1/\xi)\) itself is not defined there as a finite-coordinate substitution.

The positive inner zero of \(f_L\), equivalently the inner pole of \(g_L\), is at
\[
\xi_i=\sqrt L\,z_i=p_n
=1+\frac1{2L}+\frac7{8L^2}+\frac{33}{16L^3}+O(L^{-4}).
\]
As \(\xi\) increases through \(\xi_i\), \(g_L\) goes to \(+\infty\) from the left and \(-\infty\) from the right. At the limiting coordinate \(\xi=1\), finite-\(L\) expressions are
\[
I_L(1)=\frac{L^{-1}}{1-L^{-1}+L^{-3}},\qquad
\frac{g_L(1/\sqrt L)}L=L-1+L^{-2}.
\]
Thus \(I_L\to0\) there, while its reciprocal diverges. This is the inner counterpart of the outer singular behavior.

## 7. Matched multiscale picture

The leading profiles already established are:

| Region | Coordinate | Quantity with finite limiting profile | Limit | Exclusions for local uniform convergence |
|---|---|---|---|---|
| Fixed scale | \(x\) fixed | \(f_L(x)\) | \(-x^2\) | \(x=\pm1\) |
| Fixed reciprocal scale | \(x\) fixed | \(g_L(x)\) | \(-1/x^2\) | \(x=0,\pm1\) |
| Positive lock | \(s=L(x^2-1)\) | \(f_L(x)\) | \((1+s)/(1-s)\) | \(s=1\) |
| Outer | \(\xi=x/\sqrt L\) | \(f_L(x)/L\) | \(\xi^2/(\xi^2-1)\) | \(\xi=0,\pm1\) |
| Inner | \(\xi=x\sqrt L\) | \(L f_L(x)\) | \(1-\xi^2\) | None on bounded sets |
| Inner reciprocal | \(\xi=x\sqrt L\) | \(g_L(x)/L\) | \(1/(1-\xi^2)\) | \(\xi=\pm1\) |

Here “exclusions” concern fixed compact sets in the indicated coordinate; exceptional pointwise values and rational-extension conventions were specified above.

The leading expressions agree in the following overlap regions. These statements follow either by substituting the overlap assumptions in the exact quotients, or directly from the fixed-error identity.

- If \(L^{-1/2}\ll |x|\ll1\), the inner coordinate satisfies \(|\xi|\gg1\), and \(f_L\sim-\xi^2/L=-x^2\).
- If \(1\ll|x|\ll\sqrt L\), the outer coordinate satisfies \(|\xi|\ll1\), and \(f_L\sim-L\xi^2=-x^2\).
- If \(L^{-1}\ll|x^2-1|\ll1\), then \(|s|\gg1\), the lock profile tends to \(-1\), and the bulk profile also tends to \(-1\).

The locks and reciprocal pairings stay fixed as algebraic relations. Their adjacent zero and pole move toward them from opposite sides, while the slope at each lock grows linearly with \(L\). Outer poles escape to infinity; their reciprocal zeros approach the origin. This is a precise real-graph description, without adding a three-dimensional or physical interpretation.

**Stop-condition finding: an additional distance scale near the locks.** Differentiation, verified symbolically, gives
\[
f_L'(x)=
\frac{2x(L-1)\left[2(L+1)x^2-L(x^4+1)\right]}{D_L(x)^2}.
\]
For \(L>4\), its two positive nonzero stationary points are finite and occur at
\[
\boxed{
c_\pm=\sqrt{1+L^{-1}\pm\sqrt{2L^{-1}+L^{-2}}}
=1\pm\frac1{\sqrt{2L}}+O(L^{-1}).
}
\]
There are corresponding negative points by evenness. Thus stationary features approach each lock at distance \(O(L^{-1/2})\), which is larger than the \(O(L^{-1})\) zero-lock-pole transition width. This is a distance from \(x=\pm1\), distinct from the already requested \(x=O(L^{-1/2})\) region near the origin.

This exact evidence satisfies the instruction to stop if another asymptotic scale appears. No rescaled turning-point profile, refined stationary values, derivative matching, or further regime search is developed here. The requested four primary regions are valid, but describing the **entire** geometry requires resolving this additional scale and specifying the desired error criterion. There is no claim here that the displayed profiles form an exhaustive uniform composite approximation.

## 8. Numerical verification

The external [verification and plotting script](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/verify_and_plot.py) uses SymPy for exact algebra and mpmath for numerical evaluation. It does not import or run production kernels. Software versions were Python 3.11.15, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.4.4, and Matplotlib 3.11.2.

Twenty named symbolic checks passed: the divided family, both fixed-error identities, parity and inversion, the lock and its slope, the exact layer substitutions, inner/outer reciprocity, the exceptional scaled values, the \(L=1\) degeneration, derivative and resultant, both cubic root series, and both quadratic root formulas. The exact stationary-point equation was also checked as stop-condition evidence.

Numerical calculations were independently repeated at **120 and 200 decimal digits**, for
\[
L=10,\ 10^2,\ 10^3,\ 10^4,\ 10^6,\ 10^{12}.
\]
The final value tests cancellation at particularly thin layers and the fourth-order root remainders; it is not an additional parameter regime.

The checks evaluate numerator/denominator residuals at the exact roots, reciprocal root products, inversion products, direct substitutions versus exact scaled formulas, and convergence toward each limiting profile.

| Numerical identity check | Largest residual |
|---|---:|
| Normalized identity/root residual, 120 digits | \(2.996\times10^{-109}\) |
| Normalized identity/root residual, 200 digits | \(4.343\times10^{-189}\) |
| Normalized change from 120 to 200 digits | \(5.506\times10^{-121}\) |

Polynomial residuals are divided by the sum of the absolute magnitudes of their terms. Direct-versus-scaled values use \(|a-b|/\max(1,|a|)\); reciprocal products use \(|ab-1|\). The precision comparison uses \(|a_{120}-a_{200}|/\max(1,|a_{200}|)\). The largest roundoff residual occurs at the largest \(L\), where directly forming and subtracting near-lock quantities loses digits. Both precision runs remain far more accurate than the asymptotic errors being measured.

The following are **maximum absolute errors over explicitly listed finite sample sets**, not supremum norms over intervals.

| \(L\) | Fixed \(f\) and \(g\) error* | Lock \(H_L-H\) | Outer \(O_L-O\) | Inner \(I_L-I\) | Inner \(g/L\) error |
|---:|---:|---:|---:|---:|---:|
| \(10\) | \(4.643\) | \(10.35\) | \(5.019\times10^{-1}\) | \(7.273\times10^{-1}\) | \(8.802\times10^{-1}\) |
| \(10^2\) | \(2.289\times10^{-1}\) | \(3.696\times10^{-1}\) | \(4.883\times10^{-2}\) | \(4.172\times10^{-2}\) | \(5.163\times10^{-2}\) |
| \(10^3\) | \(2.178\times10^{-2}\) | \(3.473\times10^{-2}\) | \(4.933\times10^{-3}\) | \(4.016\times10^{-3}\) | \(4.960\times10^{-3}\) |
| \(10^4\) | \(2.168\times10^{-3}\) | \(3.452\times10^{-3}\) | \(4.938\times10^{-4}\) | \(4.002\times10^{-4}\) | \(4.940\times10^{-4}\) |
| \(10^6\) | \(2.167\times10^{-5}\) | \(3.450\times10^{-5}\) | \(4.938\times10^{-6}\) | \(4.000\times10^{-6}\) | \(4.938\times10^{-6}\) |
| \(10^{12}\) | \(2.167\times10^{-11}\) | \(3.450\times10^{-11}\) | \(4.938\times10^{-12}\) | \(4.000\times10^{-12}\) | \(4.938\times10^{-12}\) |

*The fixed-\(f\) and fixed-\(g\) maxima happen to coincide on these inversion-paired samples. They are separately computed.

Sample sets, rebuilt from exact rationals at each precision:

- Fixed \(x\): \(0,1/2,2/3,3/4,4/3,3/2,2\); omit zero for \(g_L\).
- Lock \(s\): \(-3,-2,-1,0,1/2,3/2,2,3\).
- Outer \(\xi\): \(1/2,3/4,5/4,3/2,2\).
- Inner \(\xi\): \(0,1/4,1/2,3/4,1,5/4,3/2,2\); omit one for the reciprocal limit.

The large \(L=10\) lock error is expected: a sample is still relatively close to its displaced finite-\(L\) pole. The theorem is asymptotic and does not assert a small error for that parameter. For large \(L\), these sample errors decrease at the proved \(O(L^{-1})\) rate.

For roots, let \(a_3,b_3\) be the cubic truncations in Section 3. The two normalized errors test **all four roots**, because
\[
p_n=\sqrt L\,z_i=a(1/L),\qquad p_o/\sqrt L=z_n=b(1/L).
\]

| \(L\) | \(|a-a_3|\) | \(|b-b_3|\) | \(L^4(a-a_3)\) | \(L^4(b-b_3)\) |
|---:|---:|---:|---:|---:|
| \(10\) | \(7.979\times10^{-4}\) | \(4.724\times10^{-4}\) | \(7.97906\) | \(-4.72355\) |
| \(10^2\) | \(5.755\times10^{-8}\) | \(3.449\times10^{-8}\) | \(5.75521\) | \(-3.44949\) |
| \(10^3\) | \(5.602\times10^{-12}\) | \(3.361\times10^{-12}\) | \(5.60239\) | \(-3.36109\) |
| \(10^4\) | \(5.588\times10^{-16}\) | \(3.353\times10^{-16}\) | \(5.58758\) | \(-3.35251\) |
| \(10^6\) | \(5.586\times10^{-24}\) | \(3.352\times10^{-24}\) | \(5.58595\) | \(-3.35157\) |
| \(10^{12}\) | \(5.586\times10^{-48}\) | \(3.352\times10^{-48}\) | \(5.58594\) | \(-3.35156\) |
| Proved limit | — | — | \(715/128=5.5859375\) | \(-429/128=-3.3515625\) |

Machine-readable results include exact-root decimal values, both precision runs, all residuals, and the stop finding: [JSON](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/numerical_results.json) and [CSV](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/numerical_results.csv).

To reproduce with the already available local environment, run the script from this external output directory:

    & 'C:/TORMENT/app-g-dev/env/Scripts/python.exe' -B './verify_and_plot.py'

A different Python environment can run the same script with the four listed libraries installed. The repository path used for its read-only status check is explicitly declared near the top. Rerunning writes only the sibling data and figure outputs.

## 9. Figures

All five plots use fixed, controlled axes. Colored solid curves are evaluations of the exact finite-\(L\) formulas at \(L=10,10^2,10^3,10^4,10^6\). Dashed dark curves are limiting profiles or leading root scales. Figure E additionally uses colored dotted curves for truncated asymptotic expansions. Other plots contain no truncated expansion curves. “Exact finite-\(L\)” means the exact formula evaluated numerically, not symbolic drawing.

Curve values were evaluated with 120-digit arithmetic before conversion to plotting coordinates. Pole neighborhoods are split or masked so no line bridges an asymptote. The central plot adds samples resolving the shrinking lock region. Clipping hides off-scale values; it does not bound the mathematical graph. All PNGs were visually inspected; SVG copies provide scalable versions.

**A — Fixed central window.** Axes \(x\in[-2,2]\), ordinate \([-6,4]\). Filled points show the exact \(+1\) locks. Open points at ordinate \(-1\) mark the values excluded from the ordinary bulk parabola. The visible sharpening is resolved separately in B.

![A: Fixed central window](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/A_fixed_central_window.png)

[SVG A](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/A_fixed_central_window.svg)

**B — Lock boundary layer.** Axes \(s\in[-4,4]\), ordinate \([-8,8]\). The finite curves approach \((1+s)/(1-s)\); their zero and pole approach \(-1\) and \(+1\). The negative lock gives the same graph under the even coordinate convention.

![B: Lock boundary layer](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/B_lock_boundary_layer.png)

[SVG B](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/B_lock_boundary_layer.svg)

**C — Outer scale.** Axes \(\xi\in[0.4,2]\), ordinate \([-6,6]\), plotting \(f_L/L\). This window isolates the positive outer pole. Evenness gives the negative counterpart. Zero is intentionally outside the window because the near-lock poles collapse toward zero in this coordinate.

![C: Outer scale](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/C_outer_scale.png)

[SVG C](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/C_outer_scale.svg)

**D — Reciprocal inner scale.** Axes \(\xi\in[-2,2]\). Left ordinate \([-4,2]\) shows \(L f_L\to1-\xi^2\). Right ordinate \([-6,6]\) shows \(g_L/L\to1/(1-\xi^2)\). The colored \(L\) legend applies to both panels.

![D: Reciprocal inner scale](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/D_reciprocal_inner_scale.png)

[SVG D](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/D_reciprocal_inner_scale.svg)

**E — Pole/zero migration.** Positive root locations are shown for \(4\le L\le10^6\); negative roots follow by parity. The left panel has logarithmic parameter and root axes. The right panel plots \(L(p_n-1)\) and \(L(1-z_n)\), which approach \(1/2\), with cubic root expansions overlaid.

![E: Pole and zero migration](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/E_pole_zero_migration.png)

[SVG E](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/figures/E_pole_zero_migration.svg)

## 10. What is proven / numerical / unresolved

**Proven by exact algebra and elementary asymptotic estimates:** the piecewise pointwise limit; local uniformity and explicit fixed-scale bounds; the complete real zero/pole classification for \(L>0\); the cancellation exception at \(L=1\); root expansions and reciprocal pairings; the lock width and limiting rational profile; the outer and inner normalizations and their limits; the stated leading overlap matches; and the exact evidence for the additional turning-point distance scale.

**Numerical evidence:** the 120/200-digit residuals, sample convergence rates, root remainder checks, and finite-\(L\) plotted curves. These support the proofs and help detect implementation mistakes. A finite plot or sample set cannot prove uniform convergence or exhaust all scales.

**Geometric interpretation justified here:** a real graph with fixed locks, sharpening nearby transitions, receding outer poles, inward-moving reciprocal zeros, and distinct coordinate-dependent limiting profiles. The statement that \(f_L\) “approaches a parabola” is accurate only with the fixed-scale exclusions and convergence meaning given in Section 2.

**Already known versus established in this bounded analysis:** the minus-sign family, historical \(L=9\) specialization, evenness, inversion, and exact locks are inherited facts rechecked here. This report supplies explicit large-\(L\) normalizations, root coefficients, convergence qualifications, leading matches, numerical replication, and the stop-condition finding. No fresh literature/prior-art audit was performed, so these are contributions of this calculation, not claims of mathematical novelty or publication priority.

**Unresolved under the stop instruction:** the turning-point layer near \(\pm1\), its vertical normalization, matching at the level of slopes/curvature, and whether further refinement is needed for a stated global error norm. A single Euclidean uniform approximation on intervals containing genuine poles cannot be the target without specifying excluded neighborhoods or another comparison framework. No off-diagonal \(A/B\), negative-\(L\), iteration dynamics, rotation, topology, or physical analysis was undertaken.

The [run manifest](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/run_manifest.json) records source-work-order and script hashes, figure hashes, and unchanged repository status. The [delivery manifest](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/delivery_manifest.json) records hashes of the complete external bundle.

## 11. Suggested next mathematical question

For the same \(A=B=L>0\) family, resolve only the newly detected region
\[
x=\pm1+O(L^{-1/2}).
\]
What vertical rescaling around the local bulk value produces a nontrivial profile there, and how does it recover the exact stationary points while matching both the bulk and the thinner \(O(L^{-1})\) lock layer?

That is the next bounded mathematical question. It is recorded for Hilmir/GPT and is **not executed** in this work order.

## 12. Authorized follow-up: the \(O(L^{-1/2})\) profile and its matching

This section answers the subsequent explicit request to resolve the intermediate scale. The stop statements in Sections 1–11 record the boundary of the initial work order; the present request authorizes this additional profile and its matching only.

**The proposed limit is correct for every fixed real \(s\ne0\), with convergence locally uniform away from zero.** Put
\[
h=L^{-1/2},\qquad \delta=x^2-1,\qquad s=\delta/h,\qquad t=L\delta=s/h.
\]
Here \(s\) is the new intermediate coordinate; \(t\) denotes the thinner lock coordinate previously called \(s\) in Section 4. Both real branches \(x=\pm\sqrt{1+hs}\) have the same values by evenness.

### Exact substitution and proof of the profile

Since
\[
N_L+D_L=(L+1)\delta^2+2\delta+2,\qquad
D_L=-L\delta+(1+\delta)^2,
\]
the exact rescaled function is
\[
\boxed{
P_h(s):=\frac{f_L(\pm\sqrt{1+hs})+1}{h}
=\frac{s^2+2+2hs+h^2s^2}{-s+h(1+hs)^2}.
}
\]
For fixed \(s\ne0\), its denominator tends to \(-s\), proving
\[
\boxed{
\sqrt L\,[f_L(x)+1]\longrightarrow W(s):=-s-\frac2s,
\qquad x^2=1+\frac{s}{\sqrt L}.
}
\]
For each such fixed \(s\), the real coordinate is admissible and the quotient is defined for all sufficiently large \(L\).

For precision about the mode of convergence, let \(K\subset\mathbb R\setminus\{0\}\) be compact, with \(m=\min_K|s|>0\) and \(M=\max_K|s|\). For sufficiently small \(h>0\),
\[
h(1+hM)^2\le m/2,\qquad
|-s+h(1+hs)^2|\ge m/2\quad(s\in K).
\]
The exact difference is
\[
P_h(s)-W(s)=
\frac{h\left[(3s^2+2)+h(3s^3+4s)+h^2(s^4+2s^2)\right]}
{s[-s+h(1+hs)^2]}.
\]
Its numerator is uniformly \(O_K(h)\), and the absolute value of its denominator is at least \(m^2/2\). Thus
\[
\sup_{s\in K}|P_h(s)-W(s)|=O_K(h)=O_K(L^{-1/2}).
\]
Indeed, expansion of the same exact quotient gives
\[
P_h(s)=W(s)-h\left(3+\frac2{s^2}\right)+O_K(h^2).
\]
The quotient is smooth jointly in \(h,s\) on a neighborhood of each such compact set, with its denominator separated from zero. Its derivatives therefore also converge locally uniformly: \(P_h\to W\) in \(C^k_{\mathrm{loc}}(\mathbb R\setminus\{0\})\) for every fixed nonnegative integer \(k\).

Zero must be excluded. At \(s=0\), \(x=\pm1\) and
\[
P_h(0)=2/h=2\sqrt L,
\]
because the exact lock value remains \(+1\). Furthermore, the near-lock pole occurs at \(s=h+O(h^3)\) and collapses toward zero in this coordinate. No uniform finite-valued intermediate approximation through \(s=0\) is asserted.

### A quantitative estimate that justifies both overlap limits

Matching requires allowing the scaled coordinate to vary with \(L\). Fixed-\(s\) convergence alone is insufficient. The following exact identity provides the required control:
\[
\boxed{
f_L(x)+1=
-\frac{\displaystyle \delta+\frac2{L\delta}+\frac{\delta+2}{L}}
{\displaystyle 1-\frac{(1+\delta)^2}{L\delta}}
\qquad(\delta\ne0).
}
\]
Define
\[
A=\delta+\frac2{L\delta},\qquad
b=\frac{\delta+2}{L},\qquad
q=\frac{(1+\delta)^2}{L\delta}.
\]
For real \(\delta\ne0\), the two terms in \(A\) have the same sign, so
\[
|A|=|\delta|+\frac2{L|\delta|}\ge|\delta|.
\]
If \(0<|\delta|\le1/2\) and \(L|\delta|\ge5\), then
\[
|q|\le\frac9{4L|\delta|}<\frac12,\qquad
|b/A|\le\frac5{2L|\delta|}.
\]
Consequently the function is defined there and
\[
\left|\frac{f_L+1}{-A}-1\right|
=\left|\frac{b/A+q}{1-q}\right|
\le\frac{10}{L|\delta|}.
\]
This proves the uniform relative estimate
\[
\boxed{
f_L(x)+1=
-\left(\delta+\frac2{L\delta}\right)
\left[1+O\!\left(\frac1{L|\delta|}\right)\right]
}
\]
throughout the overlap region
\[
L^{-1}\ll|\delta|\ll1.
\]
The \(O\)-constant can be chosen independently of \(\delta,L\) under the displayed bounds. This is a statement about arbitrary real sequences in the region, including either sign of \(\delta\), not just about successive formal limits.

In intermediate coordinates, the same estimate reads
\[
f_L+1=hW(s)\left[1+O\!\left(\frac h{|s|}\right)\right],
\qquad h\ll|s|\ll h^{-1}.
\]
The balance of the two nonzero terms occurs at \(|\delta|\) of order \(L^{-1/2}\).

### Matching to the ordinary bulk

The bulk-side overlap is
\[
L^{-1/2}\ll|\delta|\ll1,
\qquad\text{equivalently}\qquad
1\ll|s|\ll\sqrt L.
\]
Here \(2/(L\delta)=o(\delta)\). The quantitative estimate gives
\[
\frac{f_L+1}{-\delta}
=\left(1+\frac2{L\delta^2}\right)
\left[1+O\!\left(\frac1{L|\delta|}\right)\right]
\longrightarrow1.
\]
Thus
\[
\boxed{f_L(x)=-x^2+o(|x^2-1|)}
\]
along every sequence in that overlap. This proves matching even after the common constant \(-1\) has been removed. At the level of the profile,
\[
W(s)\sim-s\quad(|s|\to\infty),\qquad
hW(s)\sim-hs=-\delta.
\]

The first bulk correction also agrees. From the exact error identity,
\[
f_L+x^2
=-\frac{(1+\delta)^3+1}{L\delta}
\left[1-\frac{(1+\delta)^2}{L\delta}\right]^{-1}
=-\frac2{L\delta}
\left[1+O\!\left(|\delta|+\frac1{L|\delta|}\right)\right].
\]
Hence the profile's second term, \(-2h/s=-2/(L\delta)\), is precisely the singular leading bulk correction near either lock.

### Matching to the thinner \(O(L^{-1})\) lock layer

The thinner layer has coordinate \(t=L\delta\) and limiting profile
\[
H(t)=\frac{1+t}{1-t},\qquad H(t)+1=\frac2{1-t}.
\]
The common overlap is
\[
L^{-1}\ll|\delta|\ll L^{-1/2},
\]
or equivalently
\[
1\ll|t|\ll\sqrt L,\qquad L^{-1/2}\ll|s|\ll1.
\]
Now \(\delta=o(2/(L\delta))\), and the quantitative estimate gives
\[
f_L+1\sim-\frac2{L\delta}=-\frac2t.
\]
Meanwhile \(H(t)+1\sim-2/t\) as \(|t|\to\infty\). Therefore
\[
\boxed{
\frac{f_L(x)+1}{H(t)+1}\longrightarrow1,
\qquad f_L(x)-H(t)=o(|t|^{-1}).
}
\]
This compares the nonconstant part of each profile, so the matching is stronger than the observation that both approach \(-1\).

There is an exact check and a sharper estimate. Substituting \(\delta=t/L\) gives
\[
\frac{f_L(x)+1}{H(t)+1}
=
\frac{1-t}{1-t+2t/L+t^2/L^2}
\left[1+\frac{t^2+2t}{2L}+\frac{t^2}{2L^2}\right].
\]
For \(1\ll|t|\ll\sqrt L\), this equals
\[
1+O(t^2/L).
\]
Indeed, \(|1-t|\) is comparable to \(|t|\), the relative correction in the first factor is \(O(L^{-1}+|t|L^{-2})\), and the second factor differs from one by \(O(t^2/L)\). Thus the relative matching error tends to zero for every sequence in the stated overlap.

At the profile level, \(W(s)\sim-2/s\) as \(s\to0\); because \(t=s/h\),
\[
hW(s)\sim-\frac{2h}{s}=-\frac2t.
\]
The restrictions \(h\ll|s|\ll1\) are essential. Taking \(s\) all the way to zero at fixed \(L\) enters the thinner layer and ultimately the exact \(+1\) lock.

### Consistency with the turning points

The profile has
\[
W'(s)=-1+\frac2{s^2},
\]
so its stationary points are \(s=\pm\sqrt2\). The exact derivative of the intermediate profile is
\[
P_h'(s)=\frac{(1-h^2)(2+2hs-s^2)}{[-s+h(1+hs)^2]^2}.
\]
For sufficiently large \(L\), its stationary points therefore satisfy
\[
s^2-2hs-2=0,\qquad s=h\pm\sqrt{2+h^2},
\]
which converge to those two values. This recovers the previously detected distance from the positive lock,
\[
x-1=\pm\frac1{\sqrt{2L}}+O(L^{-1}).
\]
The negative lock follows by evenness. This provides an independent geometric consistency check of the intermediate profile; it does not invoke iteration dynamics or additional parameter families.

### Symbolic and high-precision verification

The external [follow-up verification script](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/verify_shoulder_profile.py) checks nine exact symbolic identities: the rescaled quotient, its error and first correction, the limit, the overlap identity, the bulk error, the lock matching ratio, and the stationary equations. It repeats numerical checks at 120 and 200 decimal digits for \(L=10,10^2,10^3,10^4,10^6,10^{12}\).

For the profile, sample coordinates are
\[
s=\pm\tfrac12,\ \pm1,\ \pm\sqrt2,\ \pm2.
\]
The maximum absolute sample errors \(\max|P_h-W|\) are:

| \(L\) | Maximum sample error | \(\sqrt L\) times that error |
|---:|---:|---:|
| \(10\) | \(2.96551\times10^1\) | \(93.7776\) |
| \(10^2\) | \(1.53592\) | \(15.3592\) |
| \(10^3\) | \(3.82376\times10^{-1}\) | \(12.0918\) |
| \(10^4\) | \(1.13240\times10^{-1}\) | \(11.3240\) |
| \(10^6\) | \(1.10316\times10^{-2}\) | \(11.0316\) |
| \(10^{12}\) | \(1.10000315\times10^{-5}\) | \(11.0000315\) |

The scaled error approaches 11 because the largest first-correction magnitude on this set is \(3+2/(1/2)^2=11\). The poor \(L=10\) approximation reflects a sample's proximity to the displaced pole; it does not contradict an asymptotic theorem.

Both sides of each overlap were tested with
\[
\delta=\pm L^{-1/4}\quad\text{(bulk)},\qquad
\delta=\pm L^{-3/4}\quad\text{(thin layer)}.
\]
At \(L=10^{12}\), the bulk ratios \((f_L+1)/(-\delta)\) are approximately \(1.0000020030\) and \(1.0000019970\). The thin-layer ratios \((f_L+1)/(H(t)+1)\) are approximately \(1.0000005010\) and \(1.0000004990\). All approach one as proved.

The maximum normalized exact-identity residual was \(1.156\times10^{-109}\) at 120 digits and \(5.526\times10^{-190}\) at 200 digits. The maximum normalized change between precision runs was \(2.481\times10^{-110}\). Direct evaluation loses digits through cancellation in \(f_L+1\); the scaled exact expression avoids that loss. Full values and normalization details are in the [results JSON](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/shoulder_verification_results.json) and the script.

These numerical results support the symbolic proof. The locally uniform limit and both moving-coordinate matching statements follow from the exact estimates above. Repository HEAD and status remained unchanged.

## 13. Bounded follow-up: origin of the involution \(s\mapsto2/s\)

**Conclusion.** This is not the coordinate image of the original \(x\mapsto1/x\) reciprocity. Matching reveals it as an exchange of the two leading contributions. More strongly, it is the large-\(L\) limit of a distinct, exact, value-preserving involution already present in the finite-\(L\) rational function when written in \(y=x^2\). Thus the simple formula \(2/s\) is a limiting symmetry, but its existence is not created solely by taking the limit.

Throughout, \(h=L^{-1/2}\), \(y=x^2=1+hs\), and
\[
P_h(s)=\frac{f_L(x)+1}{h}
=\frac{s^2+2+2hs+h^2s^2}{-s+h(1+hs)^2}.
\]
Finite expressions below are understood where their denominators are nonzero. For compact \(s\)-sets separated from zero, all needed real coordinates and denominators are valid for sufficiently large \(L\).

### Original reciprocity induces a different involution

Under \(x\mapsto1/x\), \(y\mapsto1/y\). The exact induced intermediate coordinate is
\[
s'=\frac{(1+hs)^{-1}-1}{h}
=\boxed{R_h(s)=-\frac{s}{1+hs}}.
\]
It is an involution, \(R_h(R_h(s))=s\), and
\[
R_h(s)\longrightarrow-s
\]
locally uniformly for fixed bounded \(s\). In particular, it does not tend to \(2/s\).

The output also transforms. Since \(f_L=-1+hP_h\),
\[
\boxed{
P_h(R_h(s))
=\frac{P_h(s)}{-1+hP_h(s)}.
}
\]
Taking the limit at fixed \(s\ne0\) gives
\[
W(-s)=-W(s).
\]
Thus original reciprocity explains the oddness of the limiting profile, exchanging the two sides of a lock and reciprocating the original ordinate. It does not explain the equal-value identity \(W(2/s)=W(s)\) by coordinate transformation alone.

### The exact finite-\(L\) value-preserving involution

Write
\[
F_L(y)=\frac{Ly^2-Ly+1}{y^2-Ly+L}
=\frac{N(y)}{D(y)}.
\]
Direct factorization yields
\[
\boxed{
N(u)D(y)-N(y)D(u)
=(L-1)(u-y)\left[(L+1)(u+y)-L(uy+1)\right].
}
\]
For \(L\ne1\), the equal-value equation \(F_L(u)=F_L(y)\) therefore has the original point \(u=y\) and a second point
\[
\boxed{
u=T_L(y):=\frac{(L+1)y-L}{Ly-(L+1)}.
}
\]
Algebra verifies
\[
T_L(T_L(y))=y,\qquad F_L(T_L(y))=F_L(y).
\]
For example, a matrix representing this fractional-linear map is
\[
M=\begin{pmatrix}L+1&-L\\L&-(L+1)\end{pmatrix},
\qquad M^2=(2L+1)I.
\]
For \(L>0\), this proves it is a nondegenerate involution as a rational transformation. At \(L=1\), the function is constant, so the “second equal-value point” interpretation is not unique; the large-\(L\) regime has no such exception.

Transforming \(T_L\) to the intermediate coordinate gives
\[
\boxed{
J_h(s):=\frac{T_L(1+hs)-1}{h}
=\frac{hs+2}{s-h}.
}
\]
Consequently,
\[
\boxed{J_h(J_h(s))=s,\qquad P_h(J_h(s))=P_h(s).}
\]
For fixed \(s\ne0\),
\[
J_h(s)=\frac2s+h\left(1+\frac2{s^2}\right)+O(h^2)
\longrightarrow\frac2s,
\]
locally uniformly away from zero. Passing to the limit in the exact value-preserving identity, using the local uniform convergence of \(P_h\), proves
\[
\boxed{W(2/s)=W(s).}
\]

This is an exact rational involution in \(y\), not generally a globally real rational transformation in \(x\). A local lift near either lock is
\[
x'=\pm\sqrt{T_L(x^2)},
\]
choosing the same sign branch when desired. For fixed nonzero \(s\) and sufficiently large \(L\), both \(x^2\) and \(T_L(x^2)\) are positive and close to one, so these real local lifts exist. No global symmetry of the entire real \(x\)-domain is asserted.

The uncorrected map \(s\mapsto2/s\) does not preserve the finite-\(L\) profile in general:
\[
P_h(2/s)-P_h(s)
=h\left(\frac2{s^2}-\frac{s^2}{2}\right)+O(h^2).
\]
Its exact finite-\(L\) counterpart is \(J_h\).

### Why asymptotic matching reveals the same involution

The matched leading expression is
\[
f_L+1\sim-\left(\delta+\frac2{L\delta}\right),
\qquad \delta=x^2-1.
\]
Exchanging its two contributions,
\[
\delta\mapsto\frac2{L\delta},
\]
preserves their sum exactly. Because \(\delta=hs\), this becomes \(s\mapsto2/s\).

This explanation is consistent with, and is a limiting form of, the exact finite algebra. Indeed,
\[
\boxed{
\delta'=T_L(1+\delta)-1
=\frac{\delta+2}{L\delta-1}
=\frac2{L\delta}\,
\frac{1+\delta/2}{1-1/(L\delta)}.
}
\]
Throughout \(L^{-1}\ll|\delta|\ll1\),
\[
\delta'=\frac2{L\delta}
\left[1+O\!\left(|\delta|+\frac1{L|\delta|}\right)\right].
\]
Thus the exact map reduces to the exchange of the two matched contributions. In particular, it interchanges the bulk-side overlap
\[
L^{-1/2}\ll|\delta|\ll1
\]
and the thinner-layer-side overlap
\[
L^{-1}\ll|\delta|\ll L^{-1/2},
\]
asymptotically, preserving the sign of \(\delta\) in those regions.

The coefficient two is fixed by the local algebra:
\[
N_L+D_L=(L+1)\delta^2+2\delta+2.
\]
The constant term is \(N_L(\pm1)+D_L(\pm1)=2\). Balancing that term with \(L\delta^2\), then dividing by the leading denominator \(-L\delta\), produces the two matched contributions and their coefficient.

### Self-dual points and the shoulders

The limiting involution fixes exactly
\[
s=\frac2s\quad\Longleftrightarrow\quad s=\pm\sqrt2.
\]
Differentiating \(W(2/s)=W(s)\) at a fixed point gives
\[
W'(s)\left(-\frac2{s^2}\right)=W'(s).
\]
There \(-2/s^2=-1\), so \(W'(s)=0\). Conversely,
\[
W'(s)=-1+\frac2{s^2}
\]
has no other zeros. Hence the self-dual points are precisely the limiting stationary points.

The finite-\(L\) correspondence is exact too:
\[
J_h(s)=s
\quad\Longleftrightarrow\quad
s^2-2hs-2=0
\quad\Longleftrightarrow\quad
s=h\pm\sqrt{2+h^2}.
\]
These are exactly the stationary points of \(P_h\), because
\[
P_h'(s)=\frac{(1-h^2)(2+2hs-s^2)}{[-s+h(1+hs)^2]^2}.
\]
For \(L>4\), both points are regular, lie in the real chart, and correspond to the nonzero stationary points near each lock. They approach \(\pm\sqrt2\). This ties the shoulders to exact equal-value branch pairing, not merely to a suggestive limiting diagram.

A direct geometric description is available. A level \(W(s)=w\) obeys
\[
s^2+ws+2=0.
\]
The two roots, when distinct and real, have product two and are interchanged by \(s\mapsto2/s\). They coalesce at
\[
w=\pm2\sqrt2,\qquad s=\mp\sqrt2.
\]
On \(s>0\), \(W\) has a maximum \(-2\sqrt2\) at \(s=\sqrt2\); on \(s<0\), it has a minimum \(2\sqrt2\) at \(s=-\sqrt2\). The paired sides of each shoulder are the two points at the same ordinate, one closer to the thin-layer end and the other closer to the bulk end. At the shoulder they coincide, and the two matched contributions are equal. This is a geometric interpretation of a turning point of a real graph.

### Classification and bounded verification

| Operation | Exact intermediate-coordinate map | Limiting action | Effect on ordinate |
|---|---|---|---|
| Original inversion \(x\mapsto1/x\) | \(R_h(s)=-s/(1+hs)\) | \(s\mapsto-s\) | \(f\mapsto1/f\); \(W\mapsto-W\) |
| Equal-value pairing in \(y=x^2\) | \(J_h(s)=(hs+2)/(s-h)\) | \(s\mapsto2/s\) | \(P_h\) unchanged; \(W\) unchanged |

These are distinct involutions. They commute where their compositions are defined, but neither is the same transformation as the other.

Accordingly, the symmetry is **revealed by asymptotic matching and inherited from a separate exact equal-value involution of the finite-\(L\) family**. It is not inherited from \(x\mapsto1/x\) alone, and it is not an involution that exists only after the large-\(L\) limit.

The [bounded verification script](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/verify_intermediate_involutions.py) passes 23 exact symbolic checks, plus explicit checks of the finite fixed points and the involution derivative there. Results and unchanged repository status are recorded in [the verification JSON](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/intermediate_involution_results.json). No parameter scans, additional limiting regimes, repository changes, or physical interpretations were introduced.

## 14. The exact \(V_4\) action, its quotient, and the large-\(L\) charts

**Answer.** Yes: on the rational \(y=x^2\) sphere, the action has a complete orbit description and a degree-four quotient onto another sphere, with three branch values. It organizes zeros, poles, locks, and shoulders exactly. The inner and outer charts descend to matching expressions in the same quotient. On the original \(x\)-sphere, however, the \(y\)-action does not lift to a global rational group action; its pullback is a degree-eight branched cover. These two statements must be distinguished.

We retain real \(L>0\); the rational maps are considered on the complex projective line to include every finite point and infinity. This adds no complex parameter family. The original function is constant at \(L=1\); statements using it as a nonconstant quotient coordinate exclude that value.

### Exact normal form and quotient

Let
\[
a=\sqrt{2L+1},\qquad k=\frac{2(L-1)}{a},\qquad
u=a\,\frac{y-1}{y+1}.
\]
This is a global Möbius coordinate on the \(y\)-sphere, with inverse
\[
y=\frac{a+u}{a-u}.
\]
The two involutions from Section 13 become
\[
R:y\mapsto1/y\quad\Longleftrightarrow\quad u\mapsto-u,
\]
\[
T:y\mapsto\frac{(L+1)y-L}{Ly-(L+1)}
\quad\Longleftrightarrow\quad u\mapsto1/u.
\]
Their product is \(u\mapsto-1/u\). Thus the exact group is
\[
G=\{u,-u,1/u,-1/u\}\cong V_4.
\]
The parameter dependence has disappeared from the group action itself.

Set
\[
r=u+\frac1u,\qquad
\boxed{\mathcal Q_L(y)=r^2=\left(u+\frac1u\right)^2.}
\]
In the original coordinate,
\[
\boxed{
\mathcal Q_L(y)=
\frac{4\left[(L+1)(y^2+1)-2Ly\right]^2}
{(2L+1)(y^2-1)^2}.
}
\]
A generic fiber consists exactly of one group orbit:
\[
\{u,-u,1/u,-1/u\}.
\]
To prove completeness, \(\mathcal Q=q\) is equivalent to
\[
u^4+(2-q)u^2+1=0.
\]
If \(u\) is one root, the four listed orbit points give all roots, counting multiplicity. The rational map has degree four and identifies precisely the orbits. Therefore its target is the quotient sphere.

The function itself has the normal form
\[
\boxed{F_L(y)=\frac{r+k}{r-k}.}
\]
The quotient tower, with degrees, is consequently
\[
\mathbb P^1_y
\xrightarrow[\deg 1]{u}
\mathbb P^1_u
\xrightarrow[\deg 2]{r=u+u^{-1}}
\mathbb P^1_r
\xrightarrow[\deg 2]{q=r^2}
\mathbb P^1_q.
\]
For \(L\ne1\), \(F_L\) is a Möbius coordinate on the intermediate \(r\)-sphere. The first degree-two step identifies \(T\)-pairs with equal \(F_L\); the second identifies the reciprocal values \(F_L\) and \(1/F_L\).

Equivalently,
\[
\mathcal Q_L
=k^2\left(\frac{F_L+1}{F_L-1}\right)^2,\qquad
F_L+\frac1{F_L}=2\,\frac{\mathcal Q_L+k^2}{\mathcal Q_L-k^2}.
\]
Thus \(F_L+1/F_L\) is another coordinate on the same quotient when \(L\ne1\), related to \(\mathcal Q_L\) by a Möbius transformation.

### Exceptional orbits and branch geometry

There are exactly three exceptional orbits:

| Points in \(u\) | Stabilizing involution | Quotient value | Meaning in the original function |
|---|---|---:|---|
| \(0,\infty\) | \(u\mapsto-u\) | \(\infty\) | \(y=1,-1\), where \(F_L=1\) |
| \(1,-1\) | \(u\mapsto1/u\) | \(4\) | The fixed pair of \(T\); regular shoulders for \(L>4\) |
| \(i,-i\) | \(u\mapsto-1/u\) | \(0\) | \(F_L=-1\), for \(L\ne1\) |

Each orbit has two points, each with ramification index two. Every other orbit has four points and is unramified. This follows directly from
\[
\frac{d}{du}\left(u+\frac1u\right)^2
=\frac{2(u^2-1)(u^2+1)}{u^3},
\]
together with the double poles at \(u=0,\infty\). The quotient is a sphere with three order-two branch values, often recorded as signature \((2,2,2)\). Its coarse underlying surface is a sphere.

The quotient of the real projective \(y\)-line is the interval \(q\in[4,\infty]\): real \(u\) gives \((u+1/u)^2\ge4\), with the endpoint at infinity included. The third branch orbit \(u=\pm i\) is nonreal.

The physical plotting domain \(y=x^2\ge0\) is only part of the real projective line and is not globally invariant under \(T\). Therefore the interval description is for the full real projective action, not a claim that every positive-\(y\) point has four positive-\(y\) orbit partners.

### Zeros and poles form a quotient fiber

For \(L\ne1\),
\[
F_L=0\iff r=-k,\qquad F_L=\infty\iff r=k.
\]
Both lie above the same quotient value
\[
\boxed{q_{\mathrm{zp}}=k^2=\frac{4(L-1)^2}{2L+1}.}
\]
Generically, the two \(y\)-zeros and the two \(y\)-poles form a single four-point orbit. The operation \(T\) swaps the zeros with each other and swaps the poles with each other; \(R\) exchanges reciprocal zero-pole pairs.

For \(L>4\), using the positive \(x\)-root names of Section 3, this orbit is
\[
\{z_i^2,z_n^2,p_o^2,p_n^2\}.
\]
At \(L=4\),
\[
q_{\mathrm{zp}}=4,
\]
so the orbit meets the stationary branch fiber and reduces to the two points \(y=1/2,2\). These are precisely the double zero and double pole.

Indeed,
\[
k^2-4=\frac{4L(L-4)}{2L+1}.
\]
For \(0<L<4\), \(L\ne1\), the zero-pole level lies below the real quotient range and the roots are nonreal. At \(L=1\), numerator and denominator cancel and \(F_L\equiv1\); zeros and poles are absent after reduction. The \(V_4\) action and its canonical quotient still exist, but the constant function no longer encodes that quotient.

### What happens on the full \(x\)-sphere

The original map factors as
\[
f_L:\quad x\longmapsto y=x^2\longmapsto F_L(y).
\]
For \(L\ne1\), its degree is four. The full orbit-invariant function
\[
\boxed{\widehat{\mathcal Q}_L(x)=\mathcal Q_L(x^2)}
\]
has degree eight, with a generic fiber obtained by taking both square roots of each of the four \(y\)-orbit points.

The \(T\)-action cannot be lifted to a globally rational map of \(x\), because that would require a rational square root of
\[
T_L(x^2)=\frac{(L+1)x^2-L}{Lx^2-(L+1)}.
\]
For \(L>0\), this function has distinct simple zeros and poles. A square of a rational function has only even zero and pole orders. Thus the proposed rational lift is impossible. Local square-root lifts remain valid away from their branch obstructions.

There is a different global \(V_4\) on the \(x\)-sphere:
\[
H=\{x,-x,1/x,-1/x\}.
\]
Its quotient coordinate is
\[
v=x^2+x^{-2}.
\]
Our degree-eight function factors through that degree-four quotient as
\[
\widehat{\mathcal Q}_L(x)
=\frac{4[(L+1)v-2L]^2}{(2L+1)(v^2-4)},
\]
a further degree-two map in \(v\). A generic eight-point fiber therefore contains two \(H\)-orbits. In particular, for \(L>4\), the zero-pole set splits into
\[
\{\pm z_i,\pm p_o\},\qquad
\{\pm z_n,\pm p_n\}
\]
under this globally defined \(x\)-action. Their \(y\)-images are joined by \(T\).

The pullback also has one additional branch value:
\[
\boxed{
c_L=\mathcal Q_L(0)=\mathcal Q_L(\infty)
=\frac{4(L+1)^2}{2L+1}>4.
}
\]
The associated \(y\)-orbit is
\[
\left\{0,\infty,\frac{L}{L+1},\frac{L+1}{L}\right\}.
\]
It is unramified under \(\mathcal Q_L\). The map \(x\mapsto x^2\), however, ramifies at \(0,\infty\), producing the following degree-eight fibers:

| Branch value of \(\widehat{\mathcal Q}_L\) | Ramification indices over that value |
|---|---|
| \(0\) | \(2,2,2,2\) |
| \(4\) | \(2,2,2,2\) |
| \(\infty\) | \(2,2,2,2\) |
| \(c_L\) | \(2,2,1,1,1,1\) |

There are no other branch values: composition can ramify only above ramification points of its two factors. The mixed indices over \(c_L\) also show that the degree-eight map is not a quotient by a globally acting group of eight automorphisms; stabilizers have equal orders throughout a single group orbit.

### The large-\(L\) charts in the same quotient

In the intermediate chart,
\[
u=\frac{\sqrt{2L+1}\,hs}{2+hs}\longrightarrow\frac{s}{\sqrt2}.
\]
Therefore
\[
\boxed{
\mathcal Q_L\longrightarrow
\left(\frac{s}{\sqrt2}+\frac{\sqrt2}{s}\right)^2
=\frac{W(s)^2}{2}.
}
\]
The limiting orbit is \(\{s,-s,2/s,-2/s\}\). The two shoulders \(s=\pm\sqrt2\) meet the single quotient branch value \(q=4\). This gives a global algebraic explanation for the intermediate profile's symmetry.

The other previously established charts also have simple quotient limits:

| Chart | Coordinate held fixed | Quotient normalization and limit |
|---|---|---|
| Ordinary bulk | \(y=x^2\ne\pm1\) | \(\mathcal Q_L/(2L)\to[(y-1)/(y+1)]^2\) |
| Thin lock layer | \(\tau=L(y-1)\ne0\) | \(\mathcal Q_L/(2L)\to1/\tau^2\) |
| Intermediate layer | \(s=\sqrt L(y-1)\ne0\) | \(\mathcal Q_L\to W(s)^2/2\) |
| Inner chart | \(\zeta=Ly=(x\sqrt L)^2\) | \(\mathcal Q_L-k^2\to8(1-\zeta)\) |
| Outer chart | \(\eta=y/L=(x/\sqrt L)^2\ne0\) | \(\mathcal Q_L-k^2\to8(1-1/\eta)\) |

These statements follow by substituting into the exact rational expression. Each is locally uniform on compact coordinate sets avoiding the displayed exclusions; the inner statement has no exclusion on bounded sets. Here the quotient extends smoothly through zeros and poles of \(F_L\), so \(\zeta=1\) and \(\eta=1\) need not be excluded from the last two limits.

A useful exact formula proving the centered limits is
\[
\boxed{
\mathcal Q_L-k^2
=\frac{16N_L(y)D_L(y)}{(2L+1)(y^2-1)^2},
}
\]
where \(N_L(y)=Ly^2-Ly+1\) and \(D_L(y)=y^2-Ly+L\). For \(y=\zeta/L\), the numerator's leading behavior is \(16L(1-\zeta)\) and the denominator's is \(2L\). For \(y=L\eta\), their leading ratio is \(8(\eta-1)/\eta\). The factored form also keeps the values at numerator and denominator roots regular.

Original inversion sends the inner chart exactly to the outer chart with
\[
\eta=\frac1\zeta.
\]
Under that substitution, their two centered quotient limits agree:
\[
8(1-1/\eta)=8(1-\zeta).
\]
Their zero and pole limits are the common centered level zero.

The other generator exchanges ordinary bulk and thin-lock descriptions:
\[
L[T_L(y)-1]\longrightarrow\frac{y+1}{y-1}.
\]
Substituting this value of \(\tau\) into the thin-lock quotient limit reproduces the bulk quotient limit.

There is a limitation to the leading chart atlas. The exact images of an entire inner or outer chart under \(T\) satisfy
\[
\tau_{\rm inner}
=-\frac{L+\zeta}{L+1-\zeta}\longrightarrow-1,
\]
\[
\tau_{\rm outer}
=\frac{L\eta+1}{L\eta-1-L^{-1}}\longrightarrow1.
\]
Thus \(T\) sends them into neighborhoods of the thin layer's zero and pole that collapse to single points in its leading coordinate. The exact quotient retains the orbit information, and its centered inner/outer limit remains nontrivial. A uniformly resolved atlas including these images would require finer local charts; those are not developed here. The global algebraic quotient is complete without claiming that the existing leading asymptotic charts resolve every orbit uniformly.

### Verification and scope

The [quotient verification script](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/verify_V4_quotient.py) passes 28 exact checks of the normal form, group invariants, branch data, root threshold, and requested chart limits. It also checks the polynomial evidence excluding a rational lift of \(T\) to \(x\). Results and unchanged repository status are recorded in [the quotient verification JSON](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/V4_quotient_results.json).

The quotient and all orbit statements above are algebraic proofs. No parameter scans, new physical interpretation, or repository modifications were made. The additional finer-chart requirement is recorded as a limitation, not pursued as a new asymptotic investigation.




