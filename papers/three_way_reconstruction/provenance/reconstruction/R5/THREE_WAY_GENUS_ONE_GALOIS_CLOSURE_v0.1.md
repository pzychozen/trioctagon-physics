# Three-Way: genus-one Galois closure v0.1

Date: 2026-10-05  
Mode: exact mathematics and literature identification. External report only.

**The closure is a standard Edwards elliptic curve.** The proposed Legendre parameter and both proposed \(j\)-formulas are correct. More precisely, \(\nu\) is a coordinate on the modular curve \(X_0(4)\), retaining a cyclic subgroup of order four in addition to the elliptic isomorphism class. The marking \(\lambda\) lifts to a degree-sixteen divisor, generically one orbit of the Galois group. It is not an additional elliptic modulus of the closure.

The family is thereby identified with an already classified elliptic family. This report completes the requested identifications and stops there.

## 1. Scope, assumptions, and an elliptic origin

Consider the smooth compactification of
\[
E_t:\quad t x^2z^2-x^2-z^2+t=0,
\qquad t=\frac{B}{A+1},
\qquad t\notin\{0,1,-1,\infty\}.
\tag{1}
\]
Unless stated otherwise, isomorphisms are over \(\mathbb C\). The original coefficient invariant and the cover are
\[
\nu=\frac1{1-t^2},\qquad
\lambda=\frac{(A-1)^2}{(A+1)^2-B^2},
\]
\[
\beta=Q_t(x)=
\frac{(x^4-2tx^2+1)^2}{(1-t^2)(x^4-1)^2}.
\tag{2}
\]
The extension \(\mathbb C(E_t)/\mathbb C(\beta)\) has degree sixteen; the original \(\mathbb C(x)/\mathbb C(\beta)\) has degree eight.

Choose \(a^2=t\). A convenient elliptic origin is
\[
O=(0,a).
\tag{3}
\]
This choice makes the symmetry calculations particularly simple. It is a choice of origin on an existing genus-one curve, not another modulus. There is also a parameter-independent section \((1,i)\), satisfying (1) identically; thus the family has a point over \(\mathbb C(t)\) even without adjoining \(\sqrt t\). Our chosen origin (3) is convenient over each complex fiber.

The compactification relevant to (1) lies in \(\mathbb P^1_x\times\mathbb P^1_z\). A singular plane-quartic presentation should not be confused with this smooth genus-one model at generic \(t\).

## 2. Explicit standard forms

### Edwards and Montgomery forms

Set
\[
U=\frac{x}{a},\qquad V=\frac{z}{a},\qquad d=t^2.
\]
Then (1) becomes exactly
\[
\boxed{U^2+V^2=1+dU^2V^2,\qquad d\ne0,1.}
\tag{4}
\]
This is an untwisted Edwards equation, with origin \((0,1)\). The original equation \(x^2+z^2=a^2(1+x^2z^2)\) is also the original Edwards normal form with parameter \(a\); the literature identification is exact, not an analogy. See the [Edwards paper and publication details collected by Bernstein–Lange](https://www.hyperelliptic.org/tanja/newelliptic/newelliptic.html) and the [Explicit-Formulas Database](https://www.hyperelliptic.org/EFD/g1p/auto-twisted.html).

Define
\[
M=\frac{1+V}{1-V},\qquad N=\frac{M}{U}.
\]
Direct substitution gives
\[
\gamma N^2=M^3+\alpha M^2+M,
\qquad
\alpha=\frac{2(1+t^2)}{1-t^2}=4\nu-2,\qquad
\gamma=\frac4{1-t^2}=4\nu.
\tag{5}
\]
The inverse on a dense open set is
\[
U=M/N,\qquad V=(M-1)/(M+1).
\]
The origin extends to the point at infinity. These rational maps extend to isomorphisms of the smooth compact curves.

Over \(\mathbb C\), choose \(\sqrt\gamma\) and put \(W=\sqrt\gamma N\). A particularly simple Weierstrass form is
\[
\boxed{W^2=M^3+(4\nu-2)M^2+M.}
\tag{6}
\]
The square-root choices matter for models over smaller fields and possible twists; they do not change the complex isomorphism class.

For a short Weierstrass equation, put \(M=\xi-\alpha/3\). Then
\[
W^2=\xi^3+p\xi+q,
\]
\[
p=-\frac{16\nu^2-16\nu+1}{3},\qquad
q=\frac{2(2\nu-1)(32\nu^2-32\nu-1)}{27}.
\tag{7}
\]
Its discriminant is
\[
\Delta_{\rm W}=-16(4p^3+27q^2)=256\nu(\nu-1).
\tag{8}
\]
Here \(\Delta_{\rm W}\) is the discriminant of this affine Weierstrass model, distinct from the original \((A+1)^2-B^2\). Behavior at \(\nu=\infty\) requires a model in a coordinate near infinity.

The Edwards–Montgomery relationship and its invariants are standard; see [Morain, “Edwards curves and CM curves,” §§2.4–2.5](https://cacr.uwaterloo.ca/techreports/2009/cacr2009-17.pdf). Equations (4)–(8) were independently checked here.

### Jacobi quartic and the candidate Legendre parameter

Set
\[
w=(tx^2-1)z.
\]
Then
\[
w^2=(tx^2-1)(x^2-t)
=tx^4-(t^2+1)x^2+t.
\tag{9}
\]
After \(v=w/a\), this is a Jacobi quartic:
\[
v^2=x^4-\left(t+t^{-1}\right)x^2+1.
\tag{10}
\]
The inverse is \(z=w/(tx^2-1)\), away from its exceptional coordinate points. Equation (10) has the standard Jacobi-quartic parameter \(-\tfrac12(t+t^{-1})\); compare the [Explicit-Formulas Database's Jacobi model](https://www.hyperelliptic.org/EFD/g1p/auto-jquartic.html).

For a fully explicit Legendre transformation, set
\[
q_0=\frac{1-t}{1+t},\qquad
\ell=q_0\frac{x-a}{x+a},\qquad
\kappa=\frac{2ia(t-1)}{(t+1)^2},\qquad
\eta=\kappa\frac{w}{(x+a)^2}.
\]
Then
\[
\boxed{\eta^2=\ell(\ell-1)(\ell-m),\qquad
m=q_0^2=\left(\frac{t-1}{t+1}\right)^2.}
\tag{11}
\]
Indeed, the four branch points transform as
\[
a\mapsto0,\qquad -a\mapsto\infty,\qquad
-a^{-1}\mapsto1,\qquad a^{-1}\mapsto m,
\]
and
\[
\ell(\ell-1)(\ell-m)
=-\frac{4t(t-1)^2}{(t+1)^4}\,
\frac{w^2}{(x+a)^4}.
\]
The inverse starts with \(x=a(q_0+\ell)/(q_0-\ell)\), then recovers \(w,z\).

Thus the proposed \(m\) is valid exactly. Reordering the branch points gives the usual six Legendre parameters
\[
m,\quad1-m,\quad1/m,\quad1/(1-m),\quad
m/(m-1),\quad(m-1)/m.
\]
The displayed Legendre map sends \((-a,0)\), rather than (3), to its point at infinity. This is a change of elliptic origin; it leaves \(j\) unchanged. The Montgomery map above preserves the chosen origin.

## 3. The invariant j and the precise meaning of nu

For (6),
\[
c_4=16(\alpha^2-3),\qquad
\Delta_{\rm W}=16(\alpha^2-4).
\]
Hence
\[
j=\frac{c_4^3}{\Delta_{\rm W}}
=256\frac{(\alpha^2-3)^3}{\alpha^2-4}.
\]
Substituting either \(t\) or \(\nu\) proves
\[
\boxed{j(t)=16\,\frac{(t^4+14t^2+1)^3}
{t^2(t^2-1)^4},}
\tag{12}
\]
\[
\boxed{j(\nu)=16\,\frac{(16\nu^2-16\nu+1)^3}
{\nu(\nu-1)}.}
\tag{13}
\]
An independent computation from (11),
\[
j=256\frac{(1-m+m^2)^3}{m^2(1-m)^2},
\]
gives exactly (12). Both candidates are therefore verified by two standard models.

### Modular interpretation

In the Edwards group law, \(P=(a,0)\) has order four:
\[
2P=(0,-a),\qquad4P=O.
\]
In (6), it becomes
\[
P=(1,\sqrt{\alpha+2}),\qquad2P=(0,0).
\]
The modulus \(\nu=(\alpha+2)/4\) classifies the pair
\[
\boxed{(E_t,\langle P\rangle),}
\tag{14}
\]
where the subgroup is cyclic of order four.

Here is a direct completeness proof. Given any complex elliptic curve with a cyclic subgroup \(\langle P\rangle\) of order four, put its nonzero double \(2P\) at \((0,0)\) in an equation
\[
Y^2=X(X^2+bX+c).
\]
The duplication formula implies \(X(P)^2=c\). Scaling \(X\) by \(X(P)\) normalizes the equation to (6), with \(X(P)=1\). A subgroup-preserving isomorphism fixes the origin, \((0,0)\), and the \(X\)-coordinate \(1\) of the two generators. It therefore preserves \(\alpha\). Conversely \(\alpha\) determines this pair.

This is precisely the noncuspidal moduli problem for \(X_0(4)\); see [Sutherland, Lecture 19, §19.3](https://math.mit.edu/classes/18.786/2024/LectureNotes19.pdf). Thus
\[
Y_0(4)\simeq\mathbb P^1_\nu\setminus\{0,1,\infty\},
\]
with \(\nu\) a rational coordinate, or Hauptmodul, on its compactification \(X_0(4)\). This conclusion also agrees with the Edwards/Kubert modular parameterizations in Morain, §2.5.

Forgetting the subgroup gives the degree-six map (13) to the \(j\)-line. A generic elliptic curve has twelve points of exact order four, hence six cyclic order-four subgroups. Its generic origin-preserving automorphisms are only \(\pm1\), so these give six distinct moduli points over the same \(j\).

Therefore:

- \(j\) is complete for the bare complex genus-one isomorphism class.
- \(\nu\) determines that class and retains the cyclic order-four structure; it is more information than \(j\).
- Generically six distinct \(\nu\)'s give isomorphic bare curves.
- \(t\) additionally distinguishes the two coefficient-coordinate presentations with the same \(\nu\).

For example, \(j(1-\nu)=j(\nu)\), corresponding to \(t\mapsto1/t\). This identity alone does not exhaust the sixfold equivalence. None of these assertions identifies real forms, rational twists, or fixed plotting coordinates.

## 4. All three boundary values

The branch points of the \(x\)-projection are
\[
\pm\sqrt t,\qquad\pm1/\sqrt t.
\]
The compact biquadratic equation provides exact limiting fibers:

| Boundary | Branch-point collision on the \(x\)-sphere | Limiting biquadratic curve |
|---|---|---|
| \(\nu=1,\ t=0\) | \(\pm\sqrt t\to0\), \(\pm1/\sqrt t\to\infty\) | \(x^2+z^2=0\): two rational \((1,1)\) components |
| \(\nu=0,\ t=\infty\) | \(\pm\sqrt t\to\infty\), \(\pm1/\sqrt t\to0\) | \(x^2z^2+1=0\): two rational \((1,1)\) components |
| \(\nu=\infty,\ t=1\) | Two pairs collide at \(x=1,-1\) | \((x^2-1)(z^2-1)=0\): four rational components |
| \(\nu=\infty,\ t=-1\) | Two pairs collide at \(x=i,-i\) | \((x^2+1)(z^2+1)=0\): four rational components |

At \(t=\infty\), the equation has first been divided by \(t\). All statements about components include their projective closures.

At \(t=0\), the two components meet transversely at \((0,0)\) and \((\infty,\infty)\). At \(t=\infty\), they meet at \((0,\infty)\) and \((\infty,0)\). At \(t=\pm1\), the two vertical and two horizontal components meet in a cycle of four ordinary nodes. The nearby total family is smooth at these nodes, as differentiation with respect to \(t\), or \(1/t\), verifies.

Thus the displayed semistable model over the \(t\)-line has polygon fibers of types \(I_2,I_2,I_4,I_4\), respectively. These fibers are reducible nodal curves, not smooth tori and not cuspidal curves. With one elliptic origin retained, their stabilized genus-one curves are nodal rational curves.

The \(j\)-poles are
\[
j(\nu)\sim-\frac{16}{\nu}\quad(\nu\to0),\qquad
j(\nu)\sim\frac{16}{\nu-1}\quad(\nu\to1),\qquad
j(\nu)\sim65536\nu^4\quad(\nu\to\infty).
\tag{15}
\]
These give cusp widths \(1,1,4\) for \(X_0(4)\). The map from \(t\) is ramified at \(t=0,\infty\), explaining the order-two poles there. One should not infer a particular global Weierstrass fiber model merely from a \(j\)-pole: twists and base changes can change that model. The component statements above concern the explicit biquadratic family.

The connection to the preceding cover analysis is exact:

- \(B=0\) gives \(\nu=1\), and the smooth specialized sphere map is
  \[
  Q_0(x)=\frac{(x^4+1)^2}{(x^4-1)^2}.
  \]
- \(A=-1,\ B\ne0\) gives \(\nu=0\), and the specialized sphere map is
  \[
  Q_\infty(x)=-\frac{4x^4}{(x^4-1)^2}.
  \]
  Both are degree-eight Galois maps with dihedral deck group of order eight.
- \((A+1)^2-B^2=0\) gives \(t=\pm1,\ \nu=\infty\), the cancellation/branch-collision boundary. Generically \(\lambda\) also tends to infinity, with the relative ratio retained on the stable marked target.

The specialized dihedral map has a rational Galois closure of degree eight. It is not the same object as the degeneration of the generic degree-sixteen genus-one Galois cover. Keeping the branch labels distinct requires the admissible-cover limit, with additional target and source components. Cancellation in a fixed rational formula does not retain all of that limiting data.

## 5. Enhanced automorphisms and CM

For a complex elliptic curve with an origin,
\[
\operatorname{Aut}(E,O)\simeq
\begin{cases}
C_2,&j\ne0,1728,\\
C_4,&j=1728,\\
C_6,&j=0.
\end{cases}
\tag{16}
\]
This follows directly from the short Weierstrass equation: an automorphism fixing infinity has the form \((\xi,W)\mapsto(u^2\xi,u^3W)\), requiring \(u^4p=p\) and \(u^6q=q\). Without a chosen origin, translations must also be included.

The exact loci are:

| Locus | \(t\) | \(\nu\) |
|---|---|---|
| \(j=0\) | \(t^2=-7\pm4\sqrt3\), equivalently \(t=\pm i(2\pm\sqrt3)\) | \((2\pm\sqrt3)/4\) |
| \(j=1728\) | \(t=\pm i\), or \(t^2-6t+1=0\), or \(t^2+6t+1=0\) | \(1/2,\ (4+3\sqrt2)/8,\ (4-3\sqrt2)/8\) |

The proof of the second row is the factorization
\[
j(t)-1728=
\frac{16(t^2+1)^2(t^2-6t+1)^2(t^2+6t+1)^2}
{t^2(t^2-1)^4},
\]
or equivalently
\[
j(\nu)-1728=
\frac{16(2\nu-1)^2(32\nu^2-32\nu-1)^2}
{\nu(\nu-1)}.
\tag{17}
\]
Writing \(c=A+1\), the coefficient conditions, away from the excluded singular loci, are
\[
j=0:\quad B^4+14B^2c^2+c^4=0,
\]
\[
j=1728:\quad
(B^2+c^2)(B^2-6Bc+c^2)(B^2+6Bc+c^2)=0.
\tag{18}
\]
For real \(t\), the \(j=0\) locus is absent; the real \(j=1728\) points are the four values \(\pm(3\pm2\sqrt2)\).

Both enhanced loci are smooth CM points: their endomorphism rings are \(\mathbb Z[i]\) and \(\mathbb Z[\exp(2\pi i/3)]\), respectively. Most other CM elliptic curves still have only the two origin-preserving automorphisms. CM means that the endomorphism ring is larger than \(\mathbb Z\); it is not synonymous with an enhanced finite automorphism group.

None of these smooth CM points is a boundary degeneration. The group of the labeled degree-sixteen cover remains \(D_4\times C_2\) at these smooth parameters. Extra automorphisms of the bare elliptic curve do not thereby become deck transformations of \(\beta\). In particular they do not preserve the marked cyclic subgroup of order four: an additional CM unit acting as \(\pm1\) on its generator would force an endomorphism of norm \(1,2,\) or \(3\) to kill a point of order four, which is impossible.

The previously found dihedral specializations are instead at \(\nu=0,1\), where the genus-one closure degenerates.

## 6. The group action is translation and inversion

Use the origin \(O=(0,a)\), and retain the previous generators
\[
\mathsf X(x,z)=(-x,z),\quad
\mathsf Y(x,z)=(x,-z),\quad
\mathsf S(x,z)=(z,x),\quad
\mathsf C(x,z)=(1/x,1/z).
\]
The Edwards addition formula in (4) gives
\[
\mathsf X=[-1],\qquad
\tau_P(x,z)=(z,-x)=\mathsf Y\mathsf S(x,z),
\]
\[
\tau_{2P}(x,z)=(-x,-z)=\mathsf X\mathsf Y(x,z).
\tag{19}
\]
Thus the order-four element is explicitly translation by the point \(P=(a,0)\), not an inference from an abstract group name. The addition and negation formulas used here are recorded in the [Explicit-Formulas Database](https://www.hyperelliptic.org/EFD/g1p/auto-twisted.html).

The involution \(\mathsf C\) has no fixed point on a smooth fiber: a fixed point would require \(x,z\in\{1,-1\}\), which forces \(t=1\). It is therefore translation by a nonzero two-torsion point \(Q\). To justify this standard criterion, an involution of a complex elliptic curve has linear part \(1\) or \(-1\). Any map \(R\mapsto-R+T\) has a fixed point because multiplication by two is surjective. A fixed-point-free involution must consequently be a translation of order two.

Explicitly \(Q=\mathsf C(O)=(\infty,a^{-1})\). Moreover \(\mathsf C\ne\tau_{2P}\), so \(Q\ne2P\). We obtain
\[
H_{\rm tr}=\langle\tau_P,\tau_Q\rangle\simeq C_4\times C_2,
\]
\[
\boxed{G_{\rm mon}=H_{\rm tr}\rtimes\langle[-1]\rangle
\simeq D_4\times C_2.}
\tag{20}
\]
Inversion negates \(P\) and fixes \(Q\). The other generators have the exact descriptions
\[
\mathsf Y=\tau_{2P}[-1],\qquad
\mathsf S=\tau_P[-1],\qquad
\mathsf C=\tau_Q.
\]

### The two V4 actions and the sphere quotients

The full elliptic two-torsion is
\[
E_t[2]=\{O,2P,Q,2P+Q\},
\]
whose translations are \(\langle\mathsf X\mathsf Y,\mathsf C\rangle\simeq V_4\).

In the original biquadratic coordinates these points are \((0,a),(0,-a),(\infty,a^{-1}),(\infty,-a^{-1})\). The four ramification points of the \(x\)-projection form the coset \(P+E_t[2]\): \((a,0),(-a,0),(a^{-1},\infty),(-a^{-1},\infty)\). This recovers the four stated branch coordinates directly from the group law.

The original \(x\)-sphere is
\[
\mathbb P^1_x=E_t/\langle\mathsf Y\rangle.
\tag{21}
\]
Here \(\mathsf Y:R\mapsto-R+2P\) is inversion with origin shifted to \(P\). Thus (21) is a Kummer quotient, a sphere obtained by identifying a point with its negative relative to that origin. The translations by \(E_t[2]\) commute with this involution and descend faithfully to the previously found
\[
x\mapsto x,\ -x,\ 1/x,\ -1/x.
\]
So this \(V_4\) is naturally the action of elliptic two-torsion on a Kummer sphere.

The intermediate \(y\)-sphere is
\[
\mathbb P^1_y=E_t/\langle\mathsf X,\mathsf Y\rangle.
\]
Put \(E'=E_t/\langle2P\rangle\). Then the \(y\)-sphere is the Kummer quotient of \(E'\). Since
\[
H_{\rm tr}/\langle2P\rangle=E'[2],
\]
the \(V_4\) deck group of the degree-four \(y\)-quotient is naturally the two-torsion action on this two-isogenous elliptic curve. The two occurrences of \(V_4\) are related, but they are not literally the same subgroup acting on the same sphere.

### Why nu is a Legendre parameter on a different elliptic curve

The translation quotient \(\bar E=E_t/H_{\rm tr}\) is also isomorphic to \(E'\), because
\[
H_{\rm tr}=[2]^{-1}(\langle2P\rangle).
\]
The degree-eight isogeny \(E_t\to\bar E\) can therefore be realized as multiplication by two followed by the two-isogeny to \(E'\). The final map
\[
\bar E\longrightarrow\mathbb P^1_\beta
\]
has degree two and is branched exactly over \(0,1,\infty,\nu\).

This also follows explicitly from (6). Quotienting by \((0,0)=2P\) gives
\[
E':\quad W'^2=M'\big(M'-(\alpha+2)\big)\big(M'-(\alpha-2)\big),
\tag{22}
\]
via
\[
M'=M+\alpha+M^{-1},\qquad
W'=W(1-M^{-2}).
\]
The two nonzero roots are \(4\nu\) and \(4(\nu-1)\), so an affine change of coordinate gives a Legendre model with parameter \(\nu\). In particular,
\[
j(E')=256\frac{(1-\nu+\nu^2)^3}{\nu^2(1-\nu)^2}.
\tag{23}
\]
Thus \(\nu\) is generally **not** a Legendre parameter for \(E_t\) itself. It is one for the natural two-isogenous quotient. Equations (13) and (23) describe different, isogenous elliptic curves.

## 7. The exact elliptic meaning of lambda

Let \(\pi:E_t\to\mathbb P^1_\beta\) be the degree-sixteen Galois map. For a generic marking
\[
\lambda\notin\{0,1,\infty,\nu\},
\]
its pullback is
\[
\boxed{D_\lambda=\pi^*[\lambda].}
\tag{24}
\]
This is a reduced effective divisor of degree sixteen and a single free \(G_{\rm mon}\)-orbit.

Equivalently, on \(\bar E=E_t/H_{\rm tr}\), it is an unordered pair
\[
\{q,-q\}
\]
over \(\beta=\lambda\), using the origin induced by \(O\). Choosing one lift \(R\in E_t\), the divisor consists of
\[
(R+H_{\rm tr})\ \cup\ (-R+H_{\rm tr}).
\tag{25}
\]
Neither \(R\) nor \(q\) is individually selected. Generically this is not a torsion marking.

The fiber divisor class is fixed:
\[
D_\lambda\sim D_\infty.
\]
Indeed, their difference is the principal divisor of \(\beta-\lambda\). The information in \(\lambda\) is the particular effective divisor/orbit in this family, not a varying degree-sixteen class in \(\operatorname{Pic}^{16}(E_t)\).

Under the original \(F\)-decoration, four zeros and four poles lie on the \(x\)-sphere. Each lifts to two points on \(E_t\), so \(D_\lambda\) splits into eight zero points and eight pole points, with that labeling inherited from \(F\).

This gives an exact elliptic interpretation of the two-modulus object: a curve with its order-four/cover structure, plus a point on its specified quotient sphere, or equivalently the divisor (24). It is not just an arbitrary elliptic curve with one arbitrarily marked point. The previous \(M_{0,5}\) description remains the coarse space of the selected labeled cover; it should not be replaced by bare \(M_{1,2}\).

## 8. The four historical coefficient pairs

Let \(\phi=(1+\sqrt5)/2\), and let \(J(t)\) denote (12).

| \((A,B)\) | Exact \(t\) | Exact \(\nu\) | Chosen Legendre \(m\) | Exact \(j\) |
|---|---|---|---|---|
| \((9,9)\) | \(9/10\) | \(100/19\) | \(1/361\) | \(8780093172522724/263900025\) |
| \((9,1)\) | \(1/10\) | \(100/99\) | \(81/121\) | \(5927735656804/2401490025\) |
| \((\pi,e)\) | \(e/(\pi+1)\) | \((\pi+1)^2/[(\pi+1)^2-e^2]\) | \((\pi+1-e)^2/(\pi+1+e)^2\) | \(J(e/(\pi+1))\) |
| \((\phi,1-\phi)\) | \(2-\sqrt5\) | \((2+\sqrt5)/4\) | \((3+\sqrt5)/2=\phi^2\) | \(2048\) |

Computed at 100 decimal digits, with rounded values shown:

| Pair | \(t\) | \(\nu\) | \(m\) | \(j\) |
|---|---:|---:|---:|---:|
| \((9,9)\) | 0.9 | 5.26315789473684211 | 0.00277008310249307479 | 33270528.0059095258 |
| \((9,1)\) | 0.1 | 1.01010101010101010 | 0.669421487603305785 | 2468.35739274161674 |
| \((\pi,e)\) | 0.656337321369094558 | 1.75678591761901002 | 0.0430494062828726886 | 132958.437104208270 |
| \((\phi,1-\phi)\) | -0.236067977499789696 | 1.05901699437494742 | 2.61803398874989485 | 2048 |

All four are smooth and none has \(j=0\) or \(1728\). For \((\pi,e)\), the rigorous elementary bounds \(0.65<e/(\pi+1)<0.66\), compared with the exact exceptional \(t\)-values in Section 5, suffice to exclude both enhanced loci and all boundaries.

**CM conclusions require exact arithmetic:**

- For \((9,9)\) and \((9,1)\), the displayed \(j\)'s are rational nonintegers. Every CM \(j\)-invariant is an algebraic integer, so both curves are provably non-CM.
- For \((\phi,1-\phi)\), \(m^2-3m+1=0\), hence \((m-1)^2=m\), and the Legendre formula gives \(j=2048\) exactly. This is an algebraic special value, but not an enhanced-automorphism value and not a CM value: \(2048\) is absent from the complete list of thirteen rational CM \(j\)-invariants.
- For \((\pi,e)\), CM status is **not established** here. Transcendental inputs do not imply a transcendental output. CM would imply algebraic \(j\), hence algebraic \(\nu\) by (13), and therefore algebraic \(e/(\pi+1)\). No proof of that algebraicity or its negation follows from the given construction. Numerical proximity cannot settle the question.

The integrality theorem and the complete rational CM list are stated in [Daniels–Lozano-Robledo, Theorem 2.1 and the introduction](https://alozano.clas.uconn.edu/wp-content/uploads/sites/490/2014/01/Daniels_and_Lozano-Robledo_2.pdf). No significance is assigned merely to the use of \(\pi,e,\phi\).

## 9. Verification, literature identification, and stopping point

The named species is completely identified:

- Equation (1) is the original Edwards normal form.
- Equation (4) is an untwisted Edwards model with parameter \(d=t^2\).
- Equation (10) is a Jacobi quartic.
- Equation (11) is an explicit Legendre model.
- Equations (5)–(7) give Montgomery and Weierstrass models.
- The \(\nu\)-line is the standard \(X_0(4)\) modular parameter line for the closure with its selected cyclic order-four subgroup.

These are different presentations of known elliptic geometry. The contribution of this analysis is their exact identification within the Three-Way tower, including the distinct two-isogenous quotient and the lifted marking \(\lambda\).

Independent verification comprised **42 exact symbolic checks**, all passing. They cover the birational transformations and inverses, the three invariant formulas, exceptional-locus factorizations, discriminant, two-isogeny, boundary factorizations, generator symmetries, and exact historical values.

For the four historical examples, the three expressions \(j(t)\), \(j(\nu)\), and \(j(m)\) were also compared at 100 decimal digits. The largest relative discrepancy was \(1.423\times10^{-100}\). These computations verify identities; the CM conclusions use exact arguments and the cited classification.

Reproducible supplementary files:

- [Verification script](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_genus_one_galois_closure_v0.1/verify_genus_one.py)
- [Exact-check results and high-precision values](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_genus_one_galois_closure_v0.1/verification_results.json)

The unresolved CM status of the \((\pi,e)\) example is explicitly separated from the completed geometric classification. No wider CM search, new model, or parameter scan is needed for the requested classification.

## 10. Final geometric dictionary

The smooth complex closure is topologically a torus. The original source is a sphere. This associated torus establishes no physical spacetime, brane, universe, or surface-of-revolution identification.

No repository files, prior reports, kernels, UI files, or commits were changed.

| Quantity | Geometric meaning |
|---|---|
| \(t\) | Edwards/biquadratic coordinate parameter; \(d=t^2\); it retains a sign lost by \(\nu\). |
| \(\nu\) | Modulus of the labeled degree-eight cover; a Hauptmodul on \(X_0(4)\) for \((E_t,\langle P\rangle)\); also a Legendre parameter for the natural two-isogenous quotient. |
| \(j\) | Complete isomorphism invariant of the bare complex genus-one curve; it forgets the order-four/cover marking. |
| \(\lambda\) | Marked quotient value; its lift is a degree-sixteen effective divisor and a generic \(G_{\rm mon}\)-orbit, or an unordered pair on the translation quotient. |
| \(D_4\times C_2\) | The degree-sixteen Galois group, concretely \((C_4\times C_2)\rtimes\{\pm1\}\) acting by translations and inversion. |
| Original \(x\)-sphere | The genus-zero quotient \(E_t/\langle\mathsf Y\rangle\), carrying the original degree-eight map and additional real plotting restrictions. |
| Genus-one Galois closure | The associated smooth Edwards elliptic curve \(E_t\); mathematically distinct from the original source and from any proposed physical or revolved surface. |
