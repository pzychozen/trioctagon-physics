# Three-Way map — Item 2C: why m=2?

The strongest reason for choosing m=2 is its **minimal combination of two quadratic critical mechanisms**. It is the first nontrivial even covering, its generic degree is four, and both its real covering fold and its inherited circle folds have local degree two. Higher even members retain the two restrictions but the real fold has local degree m. The Fibonacci connection is exact and useful, but does not select m=2: the power collapse holds for every m and the conjugate-reciprocal rule holds for every even m.

This is a symbolic and counting survey of m=1,...,12, supplemented by 180 constant substitutions at 120/200 decimal digits and twelve small restriction checks at 160 digits. No new dynamical atlas, model calls, or production work was performed. The existing Item 1–1G and Item 2B artifacts were preserved.

## Conventions and scope

Write **f_m** for the rational map and **b_k=Fib(k)** for Fibonacci numbers, so the two meanings of F_m never collide:

\[
f_m(z;A,B)=\frac{Az^{2m}+Bz^m+1}{z^{2m}+Bz^m+A},\qquad m\in\mathbb Z_{>0}.
\]

Unless stated otherwise, A,B are real and the map has full degree: A≠1 and B²≠(A+1)². The separated critical-point count additionally assumes B≠0. Statements about algebraic conjugation assume rational A,B, with the value and its conjugate finite and nonzero. Cancellations and poles are not norm-one identities. All generic results below are algebraic derivations; the checks verify their m=1,...,12 instances. The Lattès deduction additionally uses the explicitly cited standard criterion.

Locks mean preimages of the levels ±1, **not fixed points of iteration**. The original invariant curves are the real projective line and the unit circle. The original imaginary axis is generally not forward-invariant, even at m=2.

## 1. Fibonacci collapse, without choosing convenient exponents

Start with exactly

\[
\phi^k=b_k\phi+b_{k-1},\qquad b_0=0,\quad b_1=1.
\]

Substituting k=m and k=2m gives the requested general basis form:

\[
\boxed{f_m(\phi;A,B)=
\frac{(A b_{2m}+B b_m)\phi+A b_{2m-1}+B b_{m-1}+1}
{(b_{2m}+B b_m)\phi+b_{2m-1}+B b_{m-1}+A}.}
\]

Classification: **EXACT_FIBONACCI_REDUCTION**. For rational coefficients this lies in Q(√5), so its degree over Q is at most two for every m. The large exponents do not produce large algebraic degree.

For a parity form, define the Lucas integer L_m=b_{m-1}+b_{m+1}. With t=φ^m,

\[
\frac{f_m-1}{f_m+1}
=\frac{(A-1)(t-t^{-1})}{(A+1)(t+t^{-1})+2B}.
\]

This displayed quotient excludes f_m=-1, but the resulting rational expressions extend wherever their denominators are nonzero.

**Even m.** Here t+t⁻¹=L_m and t−t⁻¹=√5 b_m. Put H=(A+1)L_m+2B and K=(A−1)b_m. Then

\[
f_m(\phi)=\frac{H+\sqrt5K}{H-\sqrt5K},\qquad
(H^2-5K^2)(q^2+1)-2(H^2+5K^2)q=0,
\quad q=f_m(\phi).
\]

**Odd m.** Now t+t⁻¹=√5 b_m and t−t⁻¹=L_m. Put R=(A+1)b_m, S=2B and T=(A−1)L_m. Then

\[
f_m(\phi)=\frac{\sqrt5R+S+T}{\sqrt5R+S-T},\qquad
\operatorname{Norm}(f_m(\phi))=
\frac{(S+T)^2-5R^2}{(S-T)^2-5R^2}.
\]

All coefficients, including the less compact higher-exponent ones, are included rather than selected after looking at the outputs:

| m | b_m | b_(m-1) | b_(2m) | b_(2m-1) | L_m |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 1 | 1 |
| 2 | 1 | 1 | 3 | 2 | 3 |
| 3 | 2 | 1 | 8 | 5 | 4 |
| 4 | 3 | 2 | 21 | 13 | 7 |
| 5 | 5 | 3 | 55 | 34 | 11 |
| 6 | 8 | 5 | 144 | 89 | 18 |
| 7 | 13 | 8 | 377 | 233 | 29 |
| 8 | 21 | 13 | 987 | 610 | 47 |
| 9 | 34 | 21 | 2584 | 1597 | 76 |
| 10 | 55 | 34 | 6765 | 4181 | 123 |
| 11 | 89 | 55 | 17711 | 10946 | 199 |
| 12 | 144 | 89 | 46368 | 28657 | 322 |

At m=2, the four Fibonacci coefficients are 1,1,3,2. Thus H=3(A+1)+2B, K=A−1, recovering Item 2B's especially short formula. These are the first even-member coefficients, not a new recurrence or an identity that fails at higher m. For example f_2(φ;2,1/2)=(21+4√5)/19 and its polynomial is 19q²−42q+19. At m=4 the same mechanism gives (529+132√5)/439, also of norm one.

## 2. Exact conjugation rule and its exceptions

Since φ′=−1/φ and A,B are fixed by conjugation,

\[
\overline{f_m(\phi;A,B)}=f_m(-1/\phi;A,B)
=\begin{cases}
1/f_m(\phi;A,B),&m\text{ even},\\
1/f_m(\phi;A,-B),&m\text{ odd}.
\end{cases}
\]

The bar here denotes **the nontrivial automorphism of Q(√5)**, not ordinary complex conjugation of a real number.

For odd m, norm one is equivalent to g(t)=g(−t), where

\[
g(t)-g(-t)=
\frac{2B(1-A)t(t^2-1)}{(t^2+Bt+A)(t^2-Bt+A)}.
\]

Because t=φ^m>1, the exact answer on the stated domain is

\[
\boxed{\text{even }m:\ \text{always norm one};\qquad
\text{odd }m:\ \text{norm one iff }B=0\text{ or }A=1.}
\]

B=0 removes the sign-sensitive middle term and effectively uses z^(2m); A=1 gives the constant +1 map where defined. This includes the defined constant −1 case A=−1,B=0. The example A=2,B=1/2 has odd norms 41/45 at m=1, 155/171 at m=3, and 981/1025 at m=5, rather than one.

The underlying reason is a quadratic unit and its conjugate, not an unexplained preference for the golden ratio. An input α with quadratic conjugate ±α⁻¹ gives the corresponding rule; the minus sign creates the parity condition. Fibonacci numbers provide an exact computational basis for φ's particular quadratic field.

## 3. The common quadratic map and what composition does to iteration

Every member is exactly

\[
f_m=g\circ P_m,\qquad P_m(z)=z^m,\qquad
g(u)=\frac{Au^2+Bu+1}{u^2+Bu+A}.
\]

At the level of the formula, **all m-dependence is in the precomposition**. This does not make f_m dynamically conjugate to g. Under u=z^m the induced map is

\[
H_m(u)=[g(u)]^m,\qquad
P_m\circ f_m=H_m\circ P_m,\qquad
f_m\circ g=g\circ H_m.
\]

The exponent on g(u) is a pointwise power, not g iterated m times. Even the multiplier at the common fixed point 1 changes from λ for g to mλ for f_m. Its ±1 multiplier walls are λ=±1/m.

The quadratic g supplies two critical values and the reciprocal/reflection structure. The covering supplies ramification at 0,∞, m preimages of each inherited critical point, m repeated angular traversals, and a different return map H_m. The covering does not create m independent critical histories: all m roots over one critical point of g share their first image. Modulo reciprocity, there are at most two critical-orbit representatives for every full-degree m≥2, and only the inherited representative for m=1.

## 4. Cayley form, one-parameter g, and the limits of a quotient

Set

\[
w=\frac{z-1}{z+1},\quad P=A+1+B,\quad Q=A+1-B,\quad
\lambda=\frac{2(A-1)}P,\quad n=\frac P Q.
\]

On the regular chart,

\[
\widetilde g(w)=\frac{\lambda n w}{w^2+n},\qquad
C_m(w)=\frac{(1+w)^m-(1-w)^m}{(1+w)^m+(1-w)^m},\qquad
\boxed{R_m(w)=\frac{\lambda n C_m(w)}{C_m(w)^2+n}.}
\]

The complex scaling w=√n v conjugates g to v↦λv/(1+v²) for every m, because g itself is unchanged. For the full map, the normalized covering is C_m(√n v)/√n. This equals v when m=1 but depends on n when m≥2. Thus eliminating n from g does not eliminate its position relative to the covering.

C_m has degree m. At m=2 only, it is the quadratic block 2w/(1+w²), so the full map is a composition of two quadratic blocks. For even m=2k, C_m=C_k∘C_2; this factors through squaring but leaves a degree-k block beyond it when k>1.

Writing C_m=p_m/d_m with the odd/even binomial polynomials gives

\[
R_m=\frac{\lambda n p_m d_m}{p_m^2+n d_m^2},\qquad
p'_m d_m-p_m d'_m=m(1-w^2)^{m-1}.
\]

R_m is odd for **all m**. Write it as w h_m(q), q=w². The equation for nonzero fixed pairs, h_m(q)=1, has generic degree m. The inherited-critical equation n d_m²−p_m²=0 also has degree m in q. These two equations are quadratic specifically at m=2; they are linear at m=1 and degree ≥3 afterward. In the original variable u=z^m the inherited-critical equation remains quadratic for every m.

These are reductions of equations and compositional blocks. The actual quotient dynamics is q↦q h_m(q)², still of degree 2m. Likewise, for even m the invariance R_m(1/w)=R_m(w) lets one express the output as a degree-m function of W=w+1/w, but the dynamical quotient sends W to R_m+1/R_m and has degree 2m. A branched quotient can change an apparent fold order; it is not a smooth coordinate conjugacy that removes dynamical complexity.

## 5. Critical points and multiplicities

In the original coordinate,

\[
f'_m(z)=\frac{m(A-1)z^{m-1}[Bz^{2m}+2(A+1)z^m+B]}
{(z^{2m}+Bz^m+A)^2}.
\]

For full degree and B≠0:

* Inherited points: z^m=u_±, where Bu²+2(A+1)u+B=0 and u_+u_−=1. There are 2m distinct points of local degree two, hence multiplicity one each.
* Covering points: 0 and ∞, each of local degree m and critical multiplicity m−1. They are not critical at m=1.
* Total multiplicity: 2m+2(m−1)=4m−2=2deg(f_m)−2.

At m=2 these are six distinct simple critical points. At m=3 there are eight distinct points but total multiplicity ten. More generally, m>1 gives 2m+2 distinct generic points; only m=2 makes all of them simple. It is the first member with both sources of criticality present.

Special cases must be counted after cancellation. For B=0 and A≠±1, f_m=M_A(z^(2m)), so 0 and ∞ each have multiplicity 2m−1. On B=±(A+1), away from constant intersections, the degree drops to m and only covering ramification remains, with multiplicity m−1 at each endpoint. A=1 is constant +1; A=−1,B=0 is constant −1. A=0 is not by itself a degree drop: critical points at poles must be counted in spherical local coordinates.

When PQ<0 the inherited points lie on the unit circle. When PQ>0 their images are real, even when their m-th roots lie on several non-real rays. Thus critical histories are on the real line or circle after at most one step for every m, not just m=2.

## 6. Invariant restrictions, Wick twins, and actual unimodality

Real coefficients preserve the real projective line. Combining them with f_m(1/z)=1/f_m(z) preserves the unit circle for every m. In Cayley coordinates these become the real and imaginary axes; hence

\[
T_m(\xi)=-iR_m(i\xi),\qquad
D_m(\xi)=-iC_m(i\xi)=\tan(m\arctan\xi),\qquad
T_m=\frac{\lambda n D_m}{n-D_m^2}.
\]

This Wick relation holds for every m. It is a complex-coordinate relation between two restrictions, not a real conjugacy between their interval dynamics, and it has no physical implication.

In the original coordinate, f_m(iz) behaves differently: m≡0 mod 4 leaves the map unchanged; m≡2 mod 4 changes B to −B; odd m does not generically remain in the same real-parameter family. For even m, the original imaginary axis maps **into the real axis**. Calling that imaginary axis invariant would be incorrect.

**Real restriction.** Take n<−1 and λ>0. For even m, C_m increases from 0 to 1 on [0,1], then decreases to 0 on [1,∞]. The outer function λn v/(v²+n) is increasing and pole-free on [0,1]. Therefore R_m is a bounded unimodal self-map of the positive half-line, with one maximum at w=1, independent of λ and n. Locally,

\[
C_m(1+h)=1+(-1)^{m+1}2^{1-m}h^m+O(h^{m+1}),
\]

\[
R_m(1+h)=\frac{\lambda n}{1+n}
 +\frac{\lambda n(n-1)}{(n+1)^2}(-1)^{m+1}2^{1-m}h^m+O(h^{m+1}).
\]

Thus its fold is quadratic at m=2, quartic at m=4, and so on. This order survives any smooth coordinate change with nonzero derivative. It is also preserved by the sign quotient w→w² near w=1. A further branched identification w↔1/w at the critical point is a different operation.

For odd m, C_m is monotone on the positive half-line, passing through 1 with a stationary point of odd local degree when m>1. It then reaches √(-n), producing a pole in R_m. There is no one-turning-point real interval self-map from this mechanism. At m=1 the covering is unramified and the real restriction has no critical point in the folded regime. These statements do not exclude other interval return maps on special parameter sets that were not surveyed.

**Circle restriction.** For n=−s²<0 and λ>0,

\[
T_m=\frac{\lambda s^2D_m}{s^2+D_m^2}.
\]

On the first lobe 0≤θ≤π/m, equivalently 0≤ξ≤a_m=tan(π/(2m)), there is exactly one quadratic maximum:

\[
\xi_c=\tan\!\left(\frac{\arctan s}{m}\right),\qquad
T_m(\xi_c)=\frac{\lambda s}{2}.
\]

For m=1 take a_1=∞. The lobe is a forward-invariant interval precisely when λs/2≤a_m. Each inherited circle fold is quadratic for every m; there are 2m on the full circle. The fold locations depend on n but not λ. In fact all critical locations are λ-independent at fixed n because R_m is linear in λ.

This establishes unimodal **geometry under the given conditions**, not a cascade for every member. For example, m=1's normalized circle map has attracting nonzero fixed points for every λ>1 and does not acquire a finite positive-λ flip from that branch. Existing m=2 cascades cannot simply be assigned to all higher m.

The direct checks used only n=−12/5 and λ=1/(10m): all twelve circle folds had negative second derivative, correct critical value and interval containment; the measured real local order agreed with m; each odd member had the predicted positive-half-line pole. No orbit scan was needed.

## 7. All twelve members at a glance

In every row: input reciprocity, unit-circle invariance, real/circle invariant restrictions, Cayley oddness, Wick relation, the quadratic g block, and fixed/2-cycle sign reversal survive. Every row also has a conditional one-critical-point circle lobe as described above. Both lock equations survive; their generic number of distinct preimages is 2m for each sign.

“Even” means original f_m(−z)=f_m(z); odd rows instead change B's sign. “Cover” records two critical points times their multiplicity, not the number of extra distinct points. “Fixed q” is the degree of the fixed-pair equation, not the degree of the dynamical quotient. Lattès conclusions refer to real coefficients and the qualifications in §10.

| m | Degree | Inherited points | Cover multiplicities | Total critical multiplicity | Fixed q | Even? | Real fold order | Phi norm one? | Lattes? |
|---:|---:|---:|---|---:|---:|:---:|---:|---|---|
| 1 | 2 | 2 | none | 2 | 1 | no | - | exceptions only | excluded (real) |
| 2 | 4 | 4 | 2 x 1 | 6 | 2 | yes | 2 | yes | known examples |
| 3 | 6 | 6 | 2 x 2 | 10 | 3 | no | - | exceptions only | excluded (real) |
| 4 | 8 | 8 | 2 x 3 | 14 | 4 | yes | 4 | yes | excluded (real) |
| 5 | 10 | 10 | 2 x 4 | 18 | 5 | no | - | exceptions only | excluded (real) |
| 6 | 12 | 12 | 2 x 5 | 22 | 6 | yes | 6 | yes | excluded (real) |
| 7 | 14 | 14 | 2 x 6 | 26 | 7 | no | - | exceptions only | excluded (real) |
| 8 | 16 | 16 | 2 x 7 | 30 | 8 | yes | 8 | yes | excluded (real) |
| 9 | 18 | 18 | 2 x 8 | 34 | 9 | no | - | exceptions only | excluded (real) |
| 10 | 20 | 20 | 2 x 9 | 38 | 10 | yes | 10 | yes | excluded (real) |
| 11 | 22 | 22 | 2 x 10 | 42 | 11 | no | - | exceptions only | excluded (real) |
| 12 | 24 | 24 | 2 x 11 | 46 | 12 | yes | 12 | yes | excluded (real) |

The optional JSON gives an explicit per-m field for every requested classification, including circle counts, original quarter-turn behavior, critical polynomials, restrictions and degeneracies. The generic degree of the inherited-critical equation in q is also the “Fixed q” column; the full Cayley and dynamical quotient degrees are the “Degree” column.

## 8. High-priority candidate reasons A–G

| Candidate | Verdict | What changes away from m=2 |
|---|---|---|
| A. Lowest nontrivial even member | **Yes, exactly m=2.** | m=1 has no covering critical points; higher even members are no longer minimal. |
| B. Quartic rational degree | **Unique to m=2 generically.** | Full degree is 2m. Special cancellation loci have different counts. |
| C. Composition with squaring and degree-two g | **Unique as a 2×2 decomposition.** | Every m has g∘z^m; every even m factors through squaring but has an additional higher-degree block. |
| D. One-parameter quadratic normal form for g | **Not unique.** | The same g is used for every m. Its conjugacy does not remove n from the full covering composition. |
| E. Six critical points / degree-four budget | **Unique generic all-simple budget.** | m>2 has endpoint multiplicity m−1 and total budget 4m−2. |
| F. Two invariant one-dimensional restrictions | **Not unique.** | They exist for all m. Two nontrivial sources of criticality first coexist at m=2. |
| G. Quadratic critical folds after reduction | **Partly unique, coordinate must be stated.** | Circle folds and the u=z^m critical equation are quadratic for all m. The real fold is order m; the fixed-q and inherited-critical-q equations have degree m. The simultaneous quadratic real/circle fold mechanism singles out m=2. |

## 9. Roots of unity and sign reversal

\[
f_m-1=\frac{(A-1)(z^{2m}-1)}{z^{2m}+Bz^m+A},\qquad
f_m+1=\frac{(A+1)z^{2m}+2Bz^m+A+1}{z^{2m}+Bz^m+A}.
\]

Away from degeneracy the +1 lock set is exp(πik/m), k=0,...,2m−1, split into the two m-element sets z^m=1 and z^m=−1. All map to 1; only 1 is itself a generic fixed point. The real locks are always ±1. The imaginary-axis locks ±i occur iff m is even. Therefore **m=2 is the smallest member whose +1 locks include all four quadrantal points**; every even member includes them plus additional roots when m>2.

This is a coordinate-geometric specialness. It does not establish an invariant original imaginary axis. Indeed all these +1 locks lie on the original invariant circle; after Cayley transformation they all lie on its imaginary-axis image.

For the −1 locks, y=z^m solves (A+1)y²+2By+A+1=0, so y values and their lifted root sets are reciprocal. For real coefficients and nondegenerate roots, |B|<|A+1| puts both y roots on the unit circle; otherwise y is real and its m-th roots occupy rays. At A=−1,B≠0 the −1 preimages are 0 and ∞, each with multiplicity m; the generic 2m-distinct-root count must not be used there.

The parameter inversion (A,B)→(1/A,B/A), or λ→−λ at fixed n, gives f_- = I∘f_+ with I(z)=1/z. Because I commutes with every f_m, f_- composed with itself equals f_+ composed with itself for every m. A non-self-reciprocal fixed pair becomes a reciprocal two-cycle with squared multiplier and conversely. This exact relation is generic to the entire ladder, not a squaring-only dynamical accident. It is also distinct from changing B's sign under an odd input sign change.

## 10. Cheap Lattès test: a further genuine m=2 distinction

The standard facts used here are that a Lattès map has three or four postcritical points, with possible ramification signatures (2,2,2,2), (3,3,3), (2,4,4), (2,3,6). With four postcritical points, all critical points must be simple and none postcritical; that condition is also sufficient. [Milnor, *On Lattès Maps*, Corollaries 4.5 and 4.8](https://www.math.stonybrook.edu/preprints/ims04-01.pdf).

**Our application to the inherited Item 1B points.** At A=−1,B=±2, the inherited critical equation is z^(2m)=−1 and its critical values are ±i. For m>1 the covering points 0,∞ also contribute the value −1, followed by 1.

* m=2: 0,∞→−1→1 and inherited critical points→±i→1. The postcritical set is exactly {−1,1,i,−i}, with six simple critical points outside it: the two known Lattès maps are recovered.
* Odd m: ±i are themselves inherited critical points and map into {±i}. There is a periodic critical orbit, so these examples are not Lattès.
* Even m>2: the same four postcritical locations survive, but 0 and ∞ have local degree m>2. They fail the four-point criterion. Finite postcriticality alone was not used to label them Lattès.

**A counting obstruction, rather than a search, for the other real members.** For full degree and B≠0, g has two distinct critical values γ and γ⁻¹. Neither is ±1, and neither equals g(0)=1/A or g(∞)=A: a degree-two fiber cannot contain both a regular endpoint and a critical preimage. Algebraically g(u)−A=(1−A)(Bu+A+1)/(u²+Bu+A), and the candidate common root in the critical equation would force PQ=0.

If A≠−1, these give four distinct critical values of f_m. If A=−1, there are three such values, but the additional image −1→1 makes at least four postcritical points. Consequently any Lattès member with m≥3 would need exactly four postcritical points while having local degree m at 0,∞: impossible. This obstruction is independent of the size of m and covers all full-degree B≠0 members with m≥3.

For real B=0, and for the real degree-drop Möbius-after-power loci, the unit disk and exterior are preserved or exchanged. Their even iterates form normal families there, so the Julia set is not the entire sphere. These cases do not supply missing Lattès examples.

For m=1, the real λ normal form also excludes Lattès: |λ|<1 gives an attracting zero; λ>1 gives fixed points with multiplier (2−λ)/λ of modulus <1; λ<−1 gives an attracting two-cycle with multiplier ((λ+2)/λ)²; λ=±1 gives parabolic behavior. Constant or Möbius degeneracies are excluded by definition.

Thus **m=2 is the only ladder member admitting Lattès maps with real A,B**. This does not claim that A=−1,B=±2 exhaust all Lattès parameter values at m=2. The cheap computation verifies the portraits and critical polynomials; the exclusion uses the preceding mathematical argument, not a numerical search. Complex coefficient families are outside the final real-parameter uniqueness statement.

## 11. An inherited m=2 phenomenon that is not unique: fivefold contact

The Item 1C fivefold fixed point also generalizes. Since

\[
C_m(w)=mw-\frac{m(m^2-1)}3w^3
 +\frac{m(m^2-1)(2m^2-3)}{15}w^5+O(w^7),
\]

every m≥2 has a fifth-order parabolic contact at

\[
\lambda=1/m,\quad n=-\frac{3m^2}{m^2-1},\quad
A=\frac{(2m+1)(m+1)}{(m-1)(2m-1)},\quad B=\frac{2(2m+1)}{m-1}.
\]

There,

\[
R_m(w)=w-\frac{(m^2-1)(4m^2-1)}{45}w^5+O(w^7).
\]

The m=2 values are (A,B)=(5,10) and the coefficient is −1, exactly as in Item 1C. The script checks exact divisibility of the original fixed polynomial by (z−1)^5, but not (z−1)^6, for m=2,...,12. What is special at m=2 is that this collision uses **all five** fixed points; higher members retain 2m−4 other fixed points counted with multiplicity. Fifth-order contact alone is therefore not a reason to privilege m=2.

## 12. Geometric constants: the same controls at every exponent

The controls are (A,B)=(2,1/2), (3,2), and (1/2,3). All five inputs φ,√2,√3,π,e are evaluated for every m=1,...,12: 180 substitutions, independently recomputed at 120 and 200 digits. The JSON retains the high-precision values, exact algebraic expressions and field norms; no PSLQ or fitted decimal identities were used.

Classifications are explicit: φ outputs are **EXACT_FIBONACCI_REDUCTION**; square-root outputs are **ALGEBRAIC_REDUCTION**; all inversion checks are **GENERIC_RECIPROCAL_STRUCTURE**; no extra π/e-specific equality is asserted (**NO_SPECIAL_RELATION**).

For c=√k with rational k, even m makes c^m rational and hence the entire output rational. For odd m it remains in Q(√k), possibly reducing further at special coefficients. On these controls φ has degree two for all twelve m, while √2 and √3 have degree one for even m and degree two for odd m. Thus φ is not uniquely effective at reducing algebraic degree. The following compact table uses the same first control (2,1/2) throughout; all three are in JSON:

| m | phi | sqrt2 | sqrt3 | pi | e |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.298142397 | 1.21244472379 | 1.34094635845 | 1.6599211274 | 1.59443049761 |
| 2 | 1.57601431105 | 1.42857142857 | 1.64 | 1.92395527947 | 1.88896615207 |
| 3 | 1.7680190814 | 1.61327045983 | 1.82283490381 | 1.98109788203 | 1.96860731358 |
| 4 | 1.87735984745 | 1.75 | 1.91428571429 | 1.994579802 | 1.98993472172 |
| 5 | 1.93453895861 | 1.84174107938 | 1.95730033596 | 1.99833683627 | 1.996506912 |
| 6 | 1.96404429582 | 1.9 | 1.97783747482 | 1.99947694662 | 1.99874376366 |
| 7 | 1.97961966942 | 1.93618564799 | 1.98807498989 | 1.99983415178 | 1.99954177412 |
| 8 | 1.9881346076 | 1.95864661654 | 1.99341258424 | 1.99994727426 | 1.9998319593 |
| 9 | 1.99295178194 | 1.97275207506 | 1.99629726603 | 1.9999832235 | 1.99993825322 |
| 10 | 1.99575419162 | 1.98176583493 | 1.99789598209 | 1.99999466055 | 1.99997729437 |
| 11 | 1.99741836552 | 1.98763529963 | 1.99879654464 | 1.99999830047 | 1.99999164838 |
| 12 | 1.99842073812 | 1.99152542373 | 1.99930896048 | 1.99999945903 | 1.99999692779 |

The drift toward 2 in this particular table is generic saturation toward A, not a constant identity. For every c>1,

\[
f_m(c)-A=\frac{(1-A)(Bc^m+A+1)}{c^{2m}+Bc^m+A}\longrightarrow0.
\]

No decimal proximity in this table is promoted to a relation. The Fibonacci identities describe powers in a quadratic field. They imply no physical quantum, quasicrystalline, or other physical interpretation.

## Reproduction and remaining scope

Run from the playground:

```powershell
& 'C:\Users\Notandi\miniconda3\envs\torment\python.exe' -B .\three_way_item2c_checks.py
```

The checks verify the composition, derivative, degree-drop, parity, lock, Cayley and Wick identities; Fibonacci reductions; critical and fixed-pair polynomial degrees; old exceptional portraits; generalized fivefold contacts; all constant evaluations; and the small restriction diagnostics. The script writes only `three_way_item2c_classification.json`. The report is a mathematical derivation accompanied by checks, not a claim that finite computational tests prove statements for arbitrary m by themselves. Source hashes and library versions are retained.

The main open dynamical question is what the higher even real maps do with an order-m fold, and how that behavior compares with the quadratic circle restriction at the same parameters. No cascade, universality class, or exhaustive m=2 exceptional-parameter classification was inferred here. A useful bounded follow-up is m=4: verify the quartic real fold versus quadratic circle fold, then test one controlled bifurcation slice, alongside a review of the Lattès counting obstruction.

## Required summary

```text
GENERAL_Fm_COMPOSITION = f_m = g o (z -> z^m), with the same quadratic g for all m
M_DEPENDENCE_ONLY_FROM_POWER_COVERING = YES algebraically; NOT unchanged g dynamics, since the quotient is [g(u)]^m

PHI_GENERAL_FORMULA = [(A b_2m+B b_m)phi+A b_(2m-1)+B b_(m-1)+1] / [(b_2m+B b_m)phi+b_(2m-1)+B b_(m-1)+A]
PHI_EVEN_M_NORM_ONE = YES for rational A,B on the defined nonzero domain
PHI_ODD_M_RULE = conjugate = 1/f_m(phi;A,-B); norm one iff B=0 or A=1
FIBONACCI_STRUCTURE_EXACT = YES, every positive integer m; checked through 12

M2_UNIQUE_PROPERTIES = Generic quartic degree; 2x2 composition; six simple critical points; quadratic real covering fold; degree-two fixed/inherited-critical equations in q; only real-parameter ladder member admitting Lattes maps
M2_NONUNIQUE_PROPERTIES = Reciprocity, invariant real/circle curves, Wick twins, quadratic g normal form, circle folds, even-m phi norm one, sign-reversal relation, fivefold parabolic contact
M2_FIRST_NONTRIVIAL_EVEN_MEMBER = YES; also first with both critical sources
M2_ROOT_OF_UNITY_SPECIALNESS = First complete quadrantal +1 set; every even m contains it

CRITICAL_POINT_STRUCTURE_BY_M = 2m inherited simple points plus 0,infinity of multiplicity m-1 each; generic total 4m-2
WICK_TWIN_STRUCTURE_BY_M = R_m and -i R_m(i xi) for all m; original quarter-turn depends on m mod 4
LOWEST_M_WITH_REAL_AND_IMAGINARY_LOCKS = 2; original imaginary axis is not itself invariant

MOST_CONVINCING_REASON_M2_IS_SPECIAL = Minimal simultaneous quadratic real/circle critical mechanisms; higher even real folds have order m
MOST_CONVINCING_REASON_M2_IS_NOT_SPECIAL = The same g, reciprocity, two invariant restrictions and Fibonacci field reduction persist throughout the ladder
FIBONACCI_CONNECTION_SIGNIFICANCE = Exact quadratic-field arithmetic and parity; no unique selection of m=2 and no physics inference
MOST_IMPORTANT_OPEN_POINT = Higher-even real flat-critical dynamics versus the quadratic circle restriction; no atlas or universality claim
CLAUDE_FOLLOWUP_TARGET = Review the Lattes exclusion and quotient distinctions; use m=4 as a controlled quartic-real/quadratic-circle comparison
```
