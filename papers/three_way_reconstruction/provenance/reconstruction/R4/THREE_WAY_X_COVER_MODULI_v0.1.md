# Three-Way: moduli of the full x-cover v0.1

Date: 2026-10-05  
Scope: bounded follow-up to the full two-parameter normal form; complex covers, real restrictions, and collision boundaries. External report only.

**Yes, with a precise qualification.** The generic Three-Way degree-eight cover has one complex modulus, \(\nu\). Adding its marked zero/pole fiber gives two independent complex moduli, \((\lambda,\nu)\). The resulting **coarse moduli space of this selected covering type is \(M_{0,5}\)**. The covering moduli problem itself retains covering data and automorphisms, so it is not literally the fine moduli problem of five labeled target points.

The distinction is essential: the same five points support other covering types. There is no missing continuous invariant within the Three-Way type, but that type must be specified.

## 1. The object and its generic domain

Start from the recovered minus-sign family
\[
F_{A,B}(y)=\frac{Ay^2-By+1}{y^2-By+A},\qquad y=x^2.
\]
Put
\[
c=A+1,\qquad \Delta=c^2-B^2,\qquad
\lambda=\frac{(A-1)^2}{\Delta},\qquad
\nu=\frac{c^2}{\Delta}.
\]
The preceding normal form gives
\[
u=a\frac{y-1}{y+1},\qquad
a=\frac{c+B}{d},\quad d^2=\Delta,
\qquad
\beta(u)=\frac{(u+u^{-1})^2}{4}.
\]
The square roots are coherent: \(a^2=(c+B)/(c-B)\). The full cover considered here is
\[
Q_{A,B}:\mathbb P^1_x\longrightarrow\mathbb P^1_\beta,
\]
\[
\boxed{
Q_{A,B}(x)=
\frac{\big[c(x^4+1)-2Bx^2\big]^2}
{\Delta(x^4-1)^2}.}
\tag{1}
\]
It has degree eight. The underlying tower is
\[
\mathbb P^1_x
\ \xrightarrow[\deg 2]{\,x^2\,}\
\mathbb P^1_y\simeq\mathbb P^1_u
\ \xrightarrow[\deg 4]{\,\beta\,}\
\mathbb P^1_\beta.
\]

The generic five-point domain is
\[
\Omega=
\{(\lambda,\nu):
\lambda,\nu\in\mathbb P^1\setminus\{0,1,\infty\},
\ \lambda\ne\nu\}.
\tag{2}
\]
In finite coefficient coordinates its inverse image is
\[
\mathcal P^\circ=
\{(A,B)\in\mathbb C^2:
A(A-1)(A+1)B\Delta(B^2-4A)\ne0\}.
\tag{3}
\]
Some excluded loci still give perfectly good degree-eight covers; they are excluded because the five labeled points cease to be distinct.

All equivalences below preserve the labels \(0,1,\infty,\nu\), and also \(\lambda\) when present. Source coordinates may change by Möbius transformations. Individual sheets or individual zeros are not labeled.

## 2. The unmarked cover is classified by nu

For \(c\ne0\), let
\[
t=\frac{B}{c}.
\]
Then
\[
\boxed{
Q_t(x)=\frac{(x^4-2tx^2+1)^2}
{(1-t^2)(x^4-1)^2},
\qquad
\nu=\frac1{1-t^2}.}
\tag{4}
\]
Thus the cover forgets \(A\) except through \(t\).

For generic \(\nu\), there are exactly two choices
\[
t=\pm\sqrt{1-\nu^{-1}}.
\]
They give isomorphic labeled covers because
\[
Q_{-t}(ix)=Q_t(x).
\tag{5}
\]
Conversely, an isomorphism preserving the branch labels preserves the value of \(\nu\). Hence
\[
\boxed{
\text{Generic Three-Way degree-eight covers over }\mathbb C
\text{ are classified by }\nu\in M_{0,4}.}
\tag{6}
\]
Here \(M_{0,4}\simeq\mathbb P^1\setminus\{0,1,\infty\}\), with the first three labels normalized.

For completeness, the exact identities
\[
Q-1=
\frac{[B(x^4+1)-2cx^2]^2}
{\Delta(x^4-1)^2},
\]
\[
Q-\nu=
\frac{4x^2(c-Bx^2)(cx^2-B)}
{\Delta(x^4-1)^2}
\tag{7}
\]
give the generic ramification partitions:

| Labeled target value | Ramification indices above it |
|---|---|
| \(0\) | \(2,2,2,2\) |
| \(1\) | \(2,2,2,2\) |
| \(\infty\) | \(2,2,2,2\) |
| \(\nu\) | \(2,2,1,1,1,1\) |

Above \(\nu\), the two ramification points are \(x=0,\infty\). Riemann–Hurwitz gives total ramification \(4+4+4+2=14=2\cdot8-2\), so this is the complete list.

The generic deck group is precisely
\[
\operatorname{Deck}(Q_t)=
\{x,-x,1/x,-1/x\}\simeq V_4.
\tag{8}
\]
To prove completeness, every deck transformation must preserve the distinguished ramified pair \(\{0,\infty\}\) over \(\nu\), so it is \(x\mapsto bx\) or \(b/x\). Preserving the four poles \(x^4=1\) forces \(b^4=1\). Equation (4), with \(t\ne0\), then forces \(b^2=1\).

## 3. Adding lambda: exactly M0,5 at the coarse level

An ordered five-pointed sphere can be uniquely normalized so that its first three points are \(0,1,\infty\). Its other two coordinates are therefore exactly (2). This is the standard configuration-space description of \(M_{0,5}\); see [Mnev, notes, Eq. (210)](https://academicweb.nd.edu/~pmnev/f22/CFT_2022_notes.pdf).

For fixed \(\nu\), choosing a regular marked fiber is choosing
\[
\lambda\in\mathbb P^1\setminus\{0,1,\infty,\nu\}.
\]
Consequently the forgetful map for the selected Three-Way type is the usual map
\[
M_{0,5}\longrightarrow M_{0,4},
\qquad(\lambda,\nu)\longmapsto\nu.
\tag{9}
\]

The relation to the original zero/pole division is exact:
\[
\boxed{
Q=\lambda\left(\frac{F+1}{F-1}\right)^2.}
\tag{10}
\]
Thus \(Q^{-1}(\lambda)\) is the union of the zeros and poles of \(F(x^2)\). In the generic case it contains eight distinct points, four of each kind.

This division can be recovered from the selected tower and the labeled quotient: choose \(r=u+u^{-1}\) and \(k^2=4\lambda\), then
\[
F=\frac{r+k}{r-k}.
\]
The two choices of sign of \(k\) exchange \(F\) and \(1/F\); the source automorphism \(x\mapsto1/x\) realizes that exchange. They therefore give isomorphic objects even when the zero set and pole set are named separately, provided source reparametrization is allowed. No further coarse modulus is introduced.

The moduli problems nevertheless have different automorphisms:

| Object retained | Generic source automorphisms |
|---|---|
| \(Q\), with labeled branch values | \(V_4\) |
| \(Q\) plus the whole fiber at \(\lambda\) | \(V_4\) |
| The selected tower together with normalized \(F\), or its zero and pole sets separately | \(C_2=\{x,-x\}\) |
| Five labeled points on the target alone | Trivial |

Thus the selected Hurwitz moduli problem has coarse space \(M_{0,5}\), but its moduli stack is not \(M_{0,5}\): it remembers nontrivial stabilizers. Labeling individual sheets, individual zeros, or a chosen source coordinate would impose further data. No such labels are assumed here.

## 4. Why the covering type must still be specified

The degree-four quotient has deck transformations
\[
R:u\mapsto-u,\qquad
T:u\mapsto1/u,\qquad
RT:u\mapsto-1/u.
\]
Its fiber over a generic \(\nu\) is
\[
\{a,-a,a^{-1},-a^{-1}\}.
\]
There are six possible unordered pairs at which to branch a degree-two source cover. Under \(V_4\), these split into three pair types:

| Pair type | Representative branch pair |
|---|---|
| \(R\)-paired, the Three-Way type | \(\{a,-a\}\) |
| \(T\)-paired | \(\{a,a^{-1}\}\) |
| \(RT\)-paired | \(\{a,-a^{-1}\}\) |

Within each row, complementary pairs are equivalent under the quotient's deck group. Different rows are inequivalent when the target branch labels are fixed. Each construction gives a genus-zero degree-two source and the same generic degree-eight ramification partitions in Section 2.

These are inequivalent degree-eight covers, not merely different descriptions of the same tower. The Galois-closure calculation below shows that the Three-Way cover has a unique degree-four Galois intermediate cover. The same argument applies to the other two types after permuting the quotient branch labels. Any cover isomorphism must preserve that intermediate cover, so it cannot identify the three pair types while preserving the target labels.

This supplies an explicit reason that a five-point configuration, even together with the displayed ramification partitions, does not by itself select the Three-Way object among all Hurwitz covers. Selecting the \(R\)-paired type removes this ambiguity. We do not need a classification of every cover with those partitions.

## 5. The coefficient map has no extra algebraic constraint

Introduce
\[
h=\frac{A-1}{A+1},\qquad
t=\frac{B}{A+1}.
\]
Then
\[
\boxed{
\nu=\frac1{1-t^2},\qquad
\lambda=\frac{h^2}{1-t^2}.}
\tag{11}
\]
For any \((\lambda,\nu)\in\Omega\), choose
\[
h^2=\frac{\lambda}{\nu},\qquad
t^2=1-\frac1\nu.
\]
The inverse formulas are
\[
\boxed{
A=\frac{1+h}{1-h},\qquad
B=\frac{2t}{1-h}.}
\tag{12}
\]
On \(\Omega\), both square roots are nonzero, \(h\ne\pm1\), and \(t\ne\pm1\). Every sign choice therefore yields a finite coefficient pair in \(\mathcal P^\circ\).

There are exactly four coefficient pairs:
\[
(A,B),\quad (A,-B),\quad
(A^{-1},B/A),\quad(A^{-1},-B/A).
\tag{13}
\]
They are the independent sign changes of \(h,t\). Their complex source equivalences are realized by \(x\mapsto ix\) and \(x\mapsto1/x\), with compositions and parity.

In particular,
\[
\boxed{
\mathcal P^\circ/V_4\simeq\Omega\simeq M_{0,5}.}
\tag{14}
\]
The coefficient map is a four-sheeted finite étale cover of this open set. This \(V_4\) acts on coefficient presentations; it should be distinguished from the deck group of a single map.

An independent local check is
\[
\det\frac{\partial(\lambda,\nu)}{\partial(A,B)}
=\frac{8B(A+1)(A-1)}{\Delta^3},
\tag{15}
\]
which is nonzero on \(\mathcal P^\circ\).

Thus the image is **all** of the generic complex five-point configuration space, not a curve or a smaller algebraically constrained surface.

## 6. Monodromy and the Galois closure

This calculation determines the covering data used above. Write
\[
T(y)=\frac{y-t}{ty-1}
\]
and adjoin \(z\) satisfying \(z^2=T(x^2)\). The resulting curve is
\[
\boxed{
E_t:\quad t x^2z^2-x^2-z^2+t=0.}
\tag{16}
\]
For generic \(t\ne0,\pm1\), its smooth compactification has genus one. Indeed, its degree-two map to the \(x\)-sphere is branched at the four distinct points
\[
x=\pm\sqrt t,\qquad x=\pm1/\sqrt t.
\]

Over \(\mathbb C(y)\), the square classes of \(y\) and \((y-t)/(ty-1)\) are independent: their odd-order zeros and poles occur at disjoint pairs. Thus
\[
[\mathbb C(x,z):\mathbb C(y)]=4,\qquad
[\mathbb C(x,z):\mathbb C(\beta)]=16.
\]
All conjugates of \(x\) lie in this field:
\[
\pm x,\quad\pm1/x,\quad\pm z,\quad\pm1/z.
\]
It is therefore the Galois closure.

Define its automorphisms
\[
X(x,z)=(-x,z),\quad
Y(x,z)=(x,-z),\quad
S(x,z)=(z,x),\quad
C(x,z)=(1/x,1/z).
\]
Here \(SXS=Y\), while \(C\) is an independent central involution. Consequently
\[
\boxed{
G_{\rm mon}=\operatorname{Gal}(\mathbb C(x,z)/\mathbb C(\beta))
\simeq D_4\times C_2,\qquad |G_{\rm mon}|=16,}
\tag{17}
\]
where \(D_4\) denotes the dihedral group of order eight.

The degree-eight cover is the action on the eight cosets of \(H=\langle Y\rangle\). One compatible branch-cycle tuple, with loop order \(0,1,\nu,\infty\), is
\[
\begin{aligned}
\sigma_0&=(1\,4)(2\,3)(5\,8)(6\,7),\\
\sigma_1&=(1\,3)(2\,4)(5\,7)(6\,8),\\
\sigma_\nu&=(1\,7)(2\,8),\\
\sigma_\infty&=(1\,8)(2\,7)(3\,4)(5\,6).
\end{aligned}
\tag{18}
\]
With rightmost permutation acting first,
\[
\sigma_0\sigma_1\sigma_\nu\sigma_\infty=1.
\]
These permutations are respectively the coset actions of \(SC,S,X,XC\). They generate a transitive group of order sixteen and have precisely the required cycle types.

The normal closure of \(H\) in \(G_{\rm mon}\) is
\[
N=\langle X,Y\rangle,\qquad |N|=4.
\]
Every normal subgroup of order four containing \(H\) must equal \(N\). Hence the intermediate degree-four Galois cover is unique. This proves the intrinsic tower claim in Section 4.

The genus-one curve in (16) is an auxiliary Galois closure. The source of the original degree-eight map remains \(\mathbb P^1_x\).

## 7. Distinguished boundary loci and the dihedral specializations

Use the exact identities
\[
\lambda-1=\frac{B^2-4A}{\Delta},\qquad
\nu-1=\frac{B^2}{\Delta},\qquad
\nu-\lambda=\frac{4A}{\Delta}.
\tag{19}
\]
Away from intersections and indeterminate points, they give:

| Coefficient locus | Target collision | Effect |
|---|---|---|
| \(A=1\) | \(\lambda=0\) | \(F\equiv1\); \(Q\) remains degree eight if \(\nu\) is generic |
| \(B^2=4A\) | \(\lambda=1\) | Repeated zeros/poles of \(F\); \(Q\) remains degree eight |
| \(A=0\) | \(\lambda=\nu\) | The marked fiber meets the additional branch value |
| \(B=0\), \(A\ne-1\) | \(\nu=1\) | Degree-eight cover specializes to a \(D_4\)-Galois cover |
| \(A=-1\), \(B\ne0\) | \(\nu=0\) | Degree-eight cover specializes to a \(D_4\)-Galois cover |
| \(\Delta=0\), generically | \(\lambda,\nu\to\infty\) together | Triple target collision; fixed-coordinate \(F\) cancels to lower degree |

For \(B=0\), the specialized cover is
\[
Q_0(x)=\frac{(x^4+1)^2}{(x^4-1)^2}.
\tag{20}
\]
For \(A=-1,\ B\ne0\), it is
\[
Q_\infty(x)=-\frac{4x^4}{(x^4-1)^2}.
\tag{21}
\]
Both are invariant under \(x\mapsto ix\) and \(x\mapsto1/x\). These generate a group of order eight, equal to the degree, so both covers are Galois with deck group \(D_4\).

Their ramification differs by the labeled collision:

| Specialization | Above \(0\) | Above \(1\) | Above \(\infty\) |
|---|---|---|---|
| \(B=0,\ \nu=1\) | \(2^4\) | \(4^2\) | \(2^4\) |
| \(A=-1,\ \nu=0\) | \(4^2\) | \(2^4\) | \(2^4\) |

They satisfy \(Q_0=1-Q_\infty\); exchanging the labels \(0,1\) would identify them. With those labels fixed, they are distinct boundary specializations.

These are **boundary loci**, not generic interior points of \(M_{0,5}\) with an unexplained symmetry enhancement: two of the labeled branch values have collided. In the cover-only space \(M_{0,4}\), they are two of its three boundary points.

## 8. Stable target and admissible-cover interpretations

The standard compactification has the explicit model
\[
\overline M_{0,5}
\simeq
\operatorname{Bl}_{(0,0),(1,1),(\infty,\infty)}
(\mathbb P^1_\lambda\times\mathbb P^1_\nu).
\tag{22}
\]
Its ten boundary divisors are indexed by partitions of the five labels into a pair and a triple. In the displayed coordinates, seven come from
\[
\lambda=0,1,\infty;\qquad
\nu=0,1,\infty;\qquad
\lambda=\nu,
\]
and three are the exceptional divisors at the blown-up diagonal points. This model and its ten boundary curves are described explicitly by [Braungardt, “Covers of moduli surfaces,” §2](https://doi.org/10.1112/S0010437X03000642).

A collision is represented by a nodal target with an additional rational component carrying the colliding labels. It does not mean that the labels are simply deleted.

For the covering problem, the corresponding standard objects are admissible covers: nodes map to nodes, with equal ramification index on the two branches. Locally the map has the form \(\xi\mapsto\xi^e,\ \eta\mapsto\eta^e\) over a node. This preserves the covering degree through degeneration; see [Cavalieri–Markwig–Ranganathan, Definition 8 and §5.1](https://arxiv.org/pdf/1401.4626).

In this family, the monodromy around the new node is the product of the colliding branch cycles. The tuple (18) gives:

| Collision | Node cycle type |
|---|---|
| \(\nu\to0\) | \(4^2\) |
| \(\nu\to1\) | \(4^2\) |
| \(\nu\to\infty\) | \(2^4\) |

The marked regular value \(\lambda\) has identity monodromy. Its collisions change the decorated target but introduce no extra permutation factor.

The smooth rational maps (20)–(21) describe specializations after the colliding branch labels are merged. The admissible-cover limit with all labels retained has a bubbled target and additional source components. These are different, compatible descriptions.

**Cancellation requires special care.** At a generic point of \(\Delta=0\),
\[
\lambda,\nu\longrightarrow\infty,\qquad
\frac{\lambda}{\nu}=
\left(\frac{A-1}{A+1}\right)^2.
\tag{23}
\]
Thus the labels \(\infty,\lambda,\nu\) collide together. The limit lies on the exceptional boundary divisor over \((\infty,\infty)\), corresponding to the partition
\[
\{0,1\}\mid\{\infty,\lambda,\nu\}.
\]
The finite ratio in (23), generically different from \(0,1,\infty\), records the relative positions of the three labels on the new component. It is retained by the stable target.

At the same coefficient locus, canceling a common factor in the original \(F(y)\) produces a degree-one rational function. That lower-degree expression is not the degree-eight admissible-cover limit. The latter retains the missing covering degree on other components. Similarly, \(A=1\) destroys the nonconstant \(F\)-decoration but need not degenerate \(Q\) itself.

At intersections such as \((A,B)=(1,\pm2)\) or \((-1,0)\), the formulas for \(\lambda,\nu\) are indeterminate or have simultaneous degenerations. A coefficient point alone need not specify a unique limiting five-pointed object; the approach direction and, at further collisions, relative rates determine the stable limit.

One may make the coarse compactification statement precise: take the normalization of the closure of the selected Three-Way Hurwitz component in the admissible-cover compactification, without adding individual sheet labels. Its branch map on coarse spaces is finite and birational to \(\overline M_{0,5}\), hence is an isomorphism because the target is normal. Finiteness follows from properness of admissible covers and the finite choices of covers and gluings over a fixed stable marked target. This assertion concerns the selected normalized coarse component; it does not identify the covering stack, boundary automorphisms, or a fixed-coordinate rational formula with \(\overline M_{0,5}\).

## 9. Real coefficients and the actual x-plot

Complex classification does not settle real plotting equivalence. For real generic \(A,B\), the quantities \(h,t\) in (11) are real. Therefore
\[
t^2=1-\frac1\nu>0,\qquad h^2=\frac{\lambda}{\nu}>0.
\]
The real coefficient image is exactly the following part of \(\Omega(\mathbb R)\):
\[
\boxed{
(\nu>1,\ \lambda>0)
\quad\text{or}\quad
(\nu<0,\ \lambda<0),}
\tag{24}
\]
with the exclusions already in (2). Conversely, each such pair has the four real coefficient preimages (12).

In particular, real coefficients in this construction do not reach \(0<\nu<1\), or opposite signs of \(\lambda,\nu\).

Over a fixed attainable generic \((\lambda,\nu)\), there are two real isomorphism classes among these coefficient presentations, distinguished by the sign of
\[
t=\frac{B}{A+1}.
\]
Changing \(h\) to \(-h\) is realized by the real source map \(x\mapsto1/x\). Changing \(t\) to \(-t\) requires the complex map \(x\mapsto ix\); it has no real Möbius replacement. To see this, a real isomorphism must preserve the ramified pair \(\{0,\infty\}\) over \(\nu\) and the pole set \(x^4=1\). It must therefore be \(x\mapsto\pm x\) or \(\pm1/x\), all of which preserve \(t\).

Finally, the actual plotted construction specifies the coordinate \(x\), its real locus, and \(y=x^2\ge0\). These restrictions retain the positive \(y\)-half-line, locations of marked points, and the distinction between reparametrized graphs. The complex five-point configuration forgets that information. Even two coefficient presentations related by \(x\mapsto1/x\) need not be the same graph in a fixed coordinate.

No extra continuous complex modulus is hiding here: the generic coefficient reconstruction has only the four choices in (13). Real forms and a fixed plotting coordinate impose additional distinctions.

## 10. Verification, scope, and precise answer

The classification rests on the proofs above. Independent exact checks in this follow-up included:

- Seventeen symbolic identities: quotient reconstruction, coefficient inverse, coefficient equivalences, Jacobian, fiber factorizations, reciprocal coordinate symmetry, and Galois-closure identities.
- Exact factorization of the branch derivative and both dihedral specializations.
- Direct construction of the eight-coset permutation action: the tuple product is the identity, the generated group has order sixteen, the action is transitive and faithful, the deck-group order is four, and the three collision cycle types agree with Section 8.

All checks passed. No parameter scan or numerical approximation was required.

The new result relative to the [preceding normal-form report](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_two_parameter_normal_form_v0.1/THREE_WAY_TWO_PARAMETER_NORMAL_FORM_v0.1.md) is the precise moduli interpretation, the surjectivity and fourfold coefficient presentation, the distinction from other pair types, and the monodromy and stable-boundary description. The definitions of \(M_{0,n}\) and admissible covers are standard; the specialization to this family is derived here.

| Question | Exact answer |
|---|---|
| Does \(\nu\) classify the generic degree-eight cover? | Yes, within the selected Three-Way type, over \(\mathbb C\), with branch labels fixed. |
| Does adding \(\lambda\) complete the decorated classification? | Yes, under the stated equivalence and without individual sheet labels. |
| Is the decorated target a point of \(M_{0,5}\)? | Exactly, whenever all five labels are distinct. |
| Is the covering moduli problem literally \(M_{0,5}\)? | Its selected coarse space is; its stack retains covering automorphisms and its covering type must be specified. |
| Is there an extra algebraic relation between \(\lambda,\nu\)? | No. Every point of the generic \(M_{0,5}\) chart is attained. |
| Are \(B=0\) and \(A=-1\) distinguished? | Yes: they are the \(\nu=1\) and \(\nu=0\) collision boundaries with dihedral specializations. |
| Does this classify a real plotted graph? | Only after retaining the real form and coordinate/domain embedding. |

\[
\boxed{
\begin{gathered}
\text{The full generic Three-Way construction is a two-modulus}\\
\text{decorated branched cover of a fixed discrete Hurwitz type.}\\
\text{Its coarse complex moduli space is }M_{0,5},\\
\text{while its unmarked degree-eight cover has coarse moduli }M_{0,4}.
\end{gathered}}
\]

No repository files, previous reports, physical models, or commits were changed.
