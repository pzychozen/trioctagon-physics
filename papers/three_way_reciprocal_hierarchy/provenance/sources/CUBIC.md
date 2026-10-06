# Cubic Three-Way elliptic correspondence v0.1

5 October 2026 · External mathematical research · No novelty or physics claim

## 1. Result and stopping point

The generic cubic correspondence is a standard elliptic **3-isogeny/Kummer construction**. Its order-three deck transformations are translations by a nonzero 3-torsion point. Its three transpositions are elliptic inversions followed by translations. The original degree-three rational map is recovered by quotienting this construction by inversion.

The proposed \(X_0(3)\) interpretation is correct **after forgetting the original reciprocal marking**. Retaining that marking selects a nonzero 2-torsion point as well, so the more finely marked object is parametrized by \(X_0(6)\). Explicit coordinates are

\[
\boxed{t=\frac{qr}{ps},\qquad
h=\frac{t(t-9)^2}{(t-1)^2},}
\tag{1}
\]

where \(t\) is a coordinate on \(X_0(6)\), \(h\) on \(X_0(3)\), and

\[
\boxed{j(E_3)=\frac{(h+27)(h+3)^3}{h},\qquad
j(E_3/C_3)=\frac{(h+27)(h+243)^3}{h^3}.}
\tag{2}
\]

These statements are established below by explicit models, group actions, an isogeny, and a converse moduli construction; resemblance to a known \(j\)-formula alone is not used as proof.

A second, separate stopping point occurs in the requested Tri-Octagon comparison. The **six documented candidate notch triangles**, with three upper/lower pairs, support an exact regular \(S_3\)-action and an equivariant identification with the six ordered pairs of distinct cubic sheets. This is an equivalence of finite group-action/incidence data. It supplies no identification of a geometric shell with an elliptic curve, a branched covering, or its four critical values. The explicit map and limitations are in §12.

Both requested stopping conditions have therefore been met. This report closes the algebraic/modular identification and that bounded comparison; it does not investigate other modular families, the earlier quadratic Edwards closure, or physical interpretations.

## 2. Domain, coefficients, and preserved exceptions

Starting from

\[
F_3(y)=\frac{Ay^3-By^2-Cy+1}{y^3-Cy^2-By+A},
\quad z=\frac{y-1}{y+1},\quad w=\frac{F_3-1}{F_3+1},
\]

put

\[
\begin{aligned}
p&=A+B-C-1,&q&=3(A-1)-B+C,\\
r&=3(A+1)+B+C,&s&=A+1-B-C.
\end{aligned}
\tag{3}
\]

Then \(r+s-p-q=8\), and

\[
w(z)=\frac{z(pz^2+q)}{rz^2+s}.
\tag{4}
\]

The degree-three condition is \(ps(ps-qr)\ne0\). The smooth genus-one regime studied here is

\[
\boxed{pqrs(ps-qr)(9ps-qr)\ne0.}
\tag{5}
\]

It has four simple critical points and four distinct critical values. In normalized coordinates this is \(t\notin\{0,1,9,\infty\}\).

The previously established exceptions remain:

- \(ps=0\) or \(ps=qr\): cancellation/lower degree; reduce the original rational function first.
- Exactly one of \(q,r\) zero, with degree three retained: ramification \((3,2,2)\), monodromy \(S_3\), genus-zero closure.
- \(q=r=0\): cyclic cubic, equivalently \(B=-3,C=-3A\), subject to the degree condition.
- \(qr=9ps\): cyclic cubic, equivalently \(3AC+B^2-3B-C^2=0\), subject to the degree condition.
- The last two cases have deck/monodromy \(C_3\) and smooth rational Galois closure after specialization.

All intrinsic classifications below are over \(\mathbb C\). An origin and certain displayed transformations require algebraic choices. Over a coefficient field or over \(\mathbb R\), twists and genus-one torsors require additional care; see §10.

## 3. Quartic, origin, and standard forms

### 3.1 Convenient invariants and normalization

Set

\[
U=ps,\quad V=qr,\quad
\alpha=-4p^2rs,\quad
\beta=V^2-6UV-3U^2,\quad
\gamma=-4pqs^2.
\tag{6}
\]

The correspondence curve is the smooth projective normalization of

\[
E:\eta^2=f(z)=\alpha z^4+\beta z^2+\gamma.
\tag{7}
\]

Choose \(\sigma^2=s/r\). The substitutions

\[
z=\sigma Z,\quad \eta=U\sigma Y,
\quad w=\frac{p}{r}\sigma W
\]

give

\[
W=\frac{Z(Z^2+t)}{Z^2+1},\qquad
E_t:\ Y^2=-4Z^4+(t^2-6t-3)Z^2-4t.
\tag{8}
\]

Thus two coordinate scales disappear and one parameter \(t\) remains when reciprocity is retained. The signs of square roots affect coordinate choices, not the complex coarse moduli point.

Choose a root \(a\) of \(f\) and the origin

\[
O=(a,0).
\tag{9}
\]

All four roots are simple on (5). This choice makes the involution \((z,\eta)\mapsto(z,-\eta)\) elliptic inversion. Choosing another such origin changes the origin by 2-torsion and yields an isomorphic marked group structure.

### 3.2 An explicit Weierstrass transformation

Define the binary-quartic combinations

\[
I=\beta^2+12\alpha\gamma,
\qquad J=72\alpha\beta\gamma-2\beta^3.
\]

The exact birational transformation is

\[
X=\frac{f'(a)}{4(z-a)}+\frac{f''(a)}{24},\qquad
Y_W=-\frac{f'(a)\eta}{8(z-a)^2}.
\tag{10}
\]

It gives

\[
\boxed{Y_W^2=X^3-\frac I{48}X-\frac J{1728}.}
\tag{11}
\]

The inverse is

\[
z=a+\frac{f'(a)}{4(X-f''(a)/24)},\qquad
\eta=-\frac{8Y_W(z-a)^2}{f'(a)}.
\]

These are birational maps of the smooth projective curves; the apparent exceptional denominators are handled by extension to their projective points. The point (9) maps to the Weierstrass point at infinity. Substitution using \(f(a)=0\) proves (11), and the accompanying script checks the identity symbolically.

The coefficients of (11) lie in the coefficient field even if \(a\) does not. In that field, (11) is the Jacobian model; the displayed isomorphism from the original genus-one curve uses the chosen origin over an extension. No rational section of the original quartic over an arbitrary coefficient field is being assumed.

### 3.3 Exact elliptic invariants

For the displayed model (11), with the usual convention \(\Delta=(c_4^3-c_6^2)/1728\),

\[
\begin{aligned}
c_4&=I=\beta^2+12\alpha\gamma,\\
c_6&=J/2=\beta(36\alpha\gamma-\beta^2),\\
\Delta_E&=\frac{\alpha\gamma(\beta^2-4\alpha\gamma)^2}{16}\\
&=\boxed{p^3qrs^3(ps-qr)^6(9ps-qr)^2},\\
j(E)&=\frac{16(\beta^2+12\alpha\gamma)^3}
{\alpha\gamma(\beta^2-4\alpha\gamma)^2}.
\end{aligned}
\tag{12}
\]

The polynomial discriminant of \(f\) is \(256\Delta_E\). The model-dependent \(c_4,c_6,\Delta_E\) scale with a change of invariant differential; \(j\) does not.

In \(U,V\), a useful fully factored formula is

\[
\boxed{j(E)=
\frac{(V+3U)^3(V^3-15UV^2+75U^2V+3U^3)^3}
{U^3V(U-V)^6(9U-V)^2}.}
\tag{13}
\]

In the normalized family let \(M=t^2-6t-3\). Then

\[
\begin{aligned}
c_4(t)&=M^2+192t=(t+3)(t^3-15t^2+75t+3),\\
c_6(t)&=M(576t-M^2),\\
\Delta(t)&=t(t-1)^6(t-9)^2,\\
j(t)&=\frac{(t+3)^3(t^3-15t^2+75t+3)^3}
{t(t-1)^6(t-9)^2}.
\end{aligned}
\tag{14}
\]

For the original coefficients no large expanded polynomial is necessary:

\[
\begin{aligned}
U&=(A-C)^2-(B-1)^2,\\
V&=(3A+C)^2-(B+3)^2,\\
H_3&=A^2+AC-B-1,\\
K_3&=3AC+B^2-3B-C^2.
\end{aligned}
\tag{15}
\]

Here \(V-U=8H_3\), \(V-9U=8K_3\), and \(V+3U=4(3A^2-B^2+C^2-3)\). Substitute these expressions in (13); equivalently,

\[
\boxed{h=\frac{V K_3^2}{U H_3^2},\qquad
j(E)=\frac{(h+27)(h+3)^3}{h},\qquad
\Delta_E=2^{24}U^3V H_3^6K_3^2.}
\tag{16}
\]

The bare complex elliptic isomorphism class has **one modulus**, namely \(j\). The parameter \(t\) is not a one-to-one coordinate on bare elliptic isomorphism classes: its map to the \(j\)-line has degree twelve.

### 3.4 Legendre, Montgomery, and Edwards forms

For a direct Legendre form, write the four roots of \(f\) as \(a,-a,b,-b\), keeping (9) as origin. Put

\[
c=\frac{b-a}{b+a},\quad m=c^2,\quad
X_L=c\frac{z+a}{z-a},\quad
Y_L=\kappa\frac{\eta}{(z-a)^2},\quad
\kappa^2=-\frac{4a^2c^2}{\alpha(a+b)^2}.
\tag{17}
\]

Then \(Y_L^2=X_L(X_L-1)(X_L-m)\). The inverse is \(z=a(X_L+c)/(X_L-c)\), followed by the inverse scaling of \(\eta\). Changing the ordering of the roots gives the usual six cross-ratio values. This is an algebraic transformation after choosing the displayed roots, not generally a rational Legendre parameter over \(\mathbb C(A,B,C)\).

There is also a natural marked 2-torsion point, proved in §5. In (11) it is \(Q=(-\beta/6,0)\). With \(X_2=X+\beta/6\),

\[
Y_W^2=X_2^3-\frac\beta2X_2^2+
\frac{\beta^2-4\alpha\gamma}{16}X_2.
\tag{18}
\]

Choose \(d^2=(\beta^2-4\alpha\gamma)/16\), set \(X_2=d u\), \(Y_W=d^{3/2}v\), and \(A_M=-\beta/(2d)\). This gives the Montgomery form

\[
v^2=u^3+A_Mu^2+u.
\]

The exact substitutions \(x_E=u/v\), \(y_E=(u-1)/(u+1)\) then give

\[
(A_M+2)x_E^2+y_E^2=1+(A_M-2)x_E^2y_E^2.
\tag{19}
\]

The inverse is \(u=(1+y_E)/(1-y_E)\), \(v=(1+y_E)/[(1-y_E)x_E]\). These standard forms are useful consequences of the selected 2-torsion and explicit algebraic choices. They do not identify this curve with the earlier quadratic tower's Edwards curve. [Standard Montgomery conventions](https://www.hyperelliptic.org/EFD/g1p/auto-montgom.html)

## 4. Ordered sheet pairs and the exact S₃ action

To avoid confusing Cayley coordinates with the original \(y\), write the three roots of a fiber of (4) as \((z,v,u)\). The fiber polynomial is

\[
pT^3-wrT^2+qT-ws=0.
\]

Once the first two roots are specified, the third is

\[
u=\frac rp w-z-v.
\tag{20}
\]

The correspondence equation is

\[
p(rz^2+s)v^2+(ps-qr)zv+s(pz^2+q)=0,
\]

and the relation to the quartic is

\[
\eta=2p(rz^2+s)v+(ps-qr)z.
\tag{21}
\]

Thus, over a regular target value, a point of \(E\) is an **ordered pair of distinct source points in the same cubic fiber**, equivalently a full ordering of its three roots. There are \(3\cdot2=6\) such points. The compactified normalization also contains the limiting points where two roots coincide; one must not remove those points when studying ramification.

Define

\[
\tau:(z,v,u)\mapsto(v,u,z),\qquad
\iota:(z,v,u)\mapsto(z,u,v).
\tag{22}
\]

These give rational automorphisms of the function field, hence automorphisms of the smooth projective curve. They preserve \(w\), satisfy

\[
\tau^3=\iota^2=1,\qquad \iota\tau\iota=\tau^{-1},
\tag{23}
\]

and generate the six-element Galois group. In quartic coordinates, \(\iota(z,\eta)=(z,-\eta)\); the action of \(\tau\) is explicit by (20)–(22): first recover \(v\) from (21), then set the new first coordinate to \(v\) and the new ordinate to \(2p(rv^2+s)u+(ps-qr)v\).

### Why the 3-cycles really are translations

Inertia in this Galois cover has order two. Consequently an order-three element fixes no point of \(E\). This also follows from (22): a fixed ordering would require a triple root, absent on (5).

Every automorphism of a complex elliptic curve has the form \(T_R\circ a\), where \(a\) fixes the origin. If \(a\ne1\), then \(1-a\) is a nonzero isogeny and is surjective, so \(T_R\circ a\) has a fixed point. Therefore a fixed-point-free finite automorphism is a translation. It follows that

\[
\tau=T_P,\qquad 3P=O,\quad P\ne O.
\tag{24}
\]

Since \(\iota\) fixes the origin (9), it is \([-1]\). The six automorphisms are therefore exactly

\[
\boxed{1,T_P,T_{-P},[-1],T_P[-1],T_{-P}[-1].}
\tag{25}
\]

The last three are the transpositions. Their fixed points satisfy \(2R=kP\), for \(k=0,1,-1\), respectively; each has four fixed points. They are not all origin-fixing automorphisms. This proof uses the actual action and its lack of fixed points, rather than the abstract group name alone.

### An explicit 3-torsion point

In the Weierstrass model (11), a generator is

\[
\boxed{P=\left(\frac{(V+3U)^2}{12},
-\frac{U(V-U)^2}{2}\right).}
\tag{26}
\]

The sign fixes the orientation of the cycle in (22); replacing it by its opposite chooses the other generator. In the normalized family,

\[
P_t=\left(\frac{(t+3)^2}{12},-\frac{(t-1)^2}{2}\right).
\]

Substitution proves that it lies on (11), and the tangent doubling formula gives \(2P=-P\). Its ordinate is nonzero on (5), so it is nontrivial of exact order three.

For an explicit link to the original incidence action, in (8) choose a critical point \(b\), so

\[
t=\frac{b^2(b^2+3)}{b^2-1},\qquad a=\frac{2b}{b^2-1}.
\]

The fiber has roots \((a,b,b)\), so \(O\) is represented by \((a,b)\) and \(\tau(O)\) by \((b,b)\). Formula (21) at the latter is \(Y=b(2b^2+3-t)\). Applying (10) yields exactly (26)'s normalized coordinates. Thus the torsion point in the Weierstrass model has been identified with the actual cyclic deck action.

## 5. Reciprocity supplies an additional 2-torsion marking

Original reciprocity becomes \(z\mapsto-z\), \(w\mapsto-w\). Its simultaneous lift to the ordered incidence curve is

\[
\rho:(z,v,u)\mapsto(-z,-v,-u),
\qquad \rho(z,\eta)=(-z,-\eta).
\tag{27}
\]

It commutes with all root permutations, has order two, and is fixed-point-free: above \(z=0\) it swaps the two nonzero ordinates; at infinity it swaps the two points distinguished by \(\eta/z^2=\pm\sqrt\alpha\). Hence

\[
\boxed{\rho=T_Q,\qquad Q\in E[2]\setminus\{O\}.}
\tag{28}
\]

For the chosen origin, \(Q=(-a,0)\) in quartic coordinates and

\[
Q=(-\beta/6,0)
\]

in (11). The other lift covering the same source involution is \(\rho\iota=(-z,\eta)=T_Q[-1]\); it has fixed points. The simultaneous lift (27) is the one commuting with the entire \(S_3\)-action. This characterizes the extra marking without arbitrarily selecting a different 2-torsion point.

The translations \(\langle P,Q\rangle\) form a cyclic subgroup of order six. The transformations generated by them and inversion form \(S_3\times C_2\), of order twelve. Only the \(S_3\) subgroup fixes \(w\); \(\rho\) sends \(w\) to \(-w\). The original reciprocal involution remains an equivariance, not a deck transformation of the cubic map to its fixed target.

## 6. Quotient tower and explicit 3-isogeny

Let \(H=\langle\iota\rangle\). Its invariant field is \(\mathbb C(z)\), so

\[
E/H\simeq\mathbb P^1_z\simeq\mathbb P^1_y.
\]

The degree-six quotient by \(S_3\) is the \(w\)-sphere, and the intermediate degree-three map is exactly (4). The three conjugate transposition subgroups fix, respectively, the first, second, or third root coordinate. Choosing one gives one of the three conjugate cubic subfields. At a generic target point, the three sheets can be described by the cosets of one such subgroup; the six points above them are full root orderings.

Now take the normal subgroup \(\langle\tau\rangle=C_3\). It acts freely, so its quotient \(E'=E/C_3\) has genus one by Riemann–Hurwitz. With \(O'=\phi(O)\), the quotient map is a degree-three isogeny with kernel \(\{O,P,-P\}\).

An explicit model and map are obtained from the cubic discriminant. Put

\[
\begin{aligned}
\mathcal B(w)&=-4r^3s w^4+(V^2+18UV-27U^2)w^2-4pq^3,\\
J_z&=prz^4+(3ps-qr)z^2+qs.
\end{aligned}
\]

Then

\[
\boxed{E':\chi^2=\mathcal B(w),\qquad
\phi(z,\eta)=\left(
\frac{z(pz^2+q)}{rz^2+s},
\frac{J_z\eta}{(rz^2+s)^2}\right).}
\tag{29}
\]

The identity \(\chi^2=\mathcal B(w(z))\) is checked directly. Its field-theoretic meaning is especially simple:

\[
\chi=p^2(z-v)(z-u)(v-u).
\tag{30}
\]

This Vandermonde expression is invariant under 3-cycles and changes sign under transpositions. Thus \(\mathbb C(w,\chi)\) is exactly the fixed field of \(C_3\), of degree two over \(\mathbb C(w)\), rather than a separately guessed elliptic model. The formula extends to the smooth projective curves, sends the selected origins to each other, and is therefore the asserted isogeny.

The full diagram is

\[
\begin{array}{ccc}
E&\xrightarrow{\quad\phi\ (3)\quad}&E'=E/C_3\\
\downarrow 2&&\downarrow 2\\
\mathbb P^1_z&\xrightarrow{\quad w(z)\ (3)\quad}&\mathbb P^1_w.
\end{array}
\tag{31}
\]

Both vertical arrows are Kummer quotients by inversion with the chosen origins. In particular

\[
E/S_3=(E/C_3)/\{\pm1\}\simeq\mathbb P^1.
\]

This exact diagram explains the original cubic while keeping its sphere source distinct from its elliptic Galois closure.

## 7. Four branch values and the other Legendre parameter

Because the involution of \(E'\) is \((w,\chi)\mapsto(w,-\chi)=[-1]\), its four fixed points are precisely \(E'[2]\). Their images on the \(w\)-sphere are the four zeros of the homogeneous quartic \(\mathcal B\). These are exactly the cubic's four simple critical values. They are not, in general, the four branch points of the different degree-two map \(E\to\mathbb P^1_z\).

Write these target values as \(c,-c,d,-d\). After choosing an ordering, their cross-ratio can be taken as

\[
\boxed{m'=\left(\frac{d-c}{d+c}\right)^2.}
\tag{32}
\]

The same transformation as (17), with \(z,\eta,a,b\) replaced by \(w,\chi,c,d\), puts \(E'\) into Legendre form with parameter \(m'\). Thus it is the **3-isogenous quotient** whose Legendre parameter is furnished by the original four critical values.

In normalized coordinates, let \(L=t^2+18t-27\). The quotient quartic is

\[
\chi^2=-4w^4+Lw^2-4t^3.
\]

Up to root ordering and the six standard cross-ratio transforms,

\[
m'=\frac{L+8t^{3/2}}{L-8t^{3/2}},\qquad
m=\frac{M+8\sqrt t}{M-8\sqrt t}
\tag{33}
\]

for \(E'\) and \(E\), respectively. The signs of square roots account for permitted reorderings. These expressions are not asserted to be single-valued rational functions of \(t\). In both cases the invariant is

\[
j=256\frac{(1-m+m^2)^3}{m^2(1-m)^2}.
\]

The unordered four-point branch configuration determines \(j(E')\). It does not generically determine which cyclic 3-isogeny produced the cubic: that is additional finite covering data. Likewise a labeling of the four points is additional level-two data and is not silently built into \(h\).

## 8. Precise modular interpretation and its proof

### 8.1 The X₀(3) statement

Forgetting reciprocity leaves the datum \((E,\langle P\rangle)\), with the direction of the isogeny retained. A generic elliptic curve has four cyclic order-three subgroups, the four lines in \(E[3]\simeq\mathbb F_3^2\). Consequently the forgetful map \(X_0(3)\to X(1)\) has degree four.

Conversely, any complex elliptic curve with a cyclic order-three subgroup gives (31): quotient by that subgroup, then descend the isogeny through inversion. Its degree-three rational map has a genus-one \(S_3\) Galois closure. Choosing another transposition subgroup merely changes the intermediate source by an isomorphism. Thus this is the intrinsic moduli datum of the generic cubic cover under independent source and target Möbius transformations.

The quartic invariants of (29) give, directly,

\[
j(E')=\frac{(t+3)^3(t^3+225t^2-405t+243)^3}
{t^3(t-1)^2(t-9)^6}.
\tag{34}
\]

Substitution of (1) into (2) reproduces (14) and (34) exactly. The rational functions \(j_E(h),j_{E'}(h)\) generically determine \(h\): the symbolic gcd, in a second variable \(k\), of the two cleared equations \(j_E(k)=j_E(h)\), \(j_{E'}(k)=j_{E'}(h)\), is \(k-h\). This rules out an unnoticed generic identification of the oriented isogeny pair. The next subsection establishes that forgetting the extra 2-torsion has degree three, equal to the degree of \(t\mapsto h\). Hence \(h\) generates the function field of the selected \(X_0(3)\) moduli problem: it is a Hauptmodul.

These are the standard level-three modular formulas. Elkies gives the \((h+27)(h+243)^3/h^3\) convention and the duality \(h\mapsto729/h\); our source curve uses the dual orientation. This agreement is a literature identification, in addition to the independent construction above. [Elkies, §4, equation (80)](https://people.math.harvard.edu/~elkies/modular.pdf)

### 8.2 Why the reciprocal object is X₀(6)

Retaining (27) retains \(Q\ne O\) in \(E[2]\), so the datum is

\[
(E,\langle P\rangle,Q)\quad\Longleftrightarrow\quad
(E,\langle P,Q\rangle),\qquad |\langle P,Q\rangle|=6.
\tag{35}
\]

This equivalence is exact: a cyclic group of order six has unique subgroups of orders two and three. Over a generic elliptic curve there are three choices for \(Q\); hence forgetting it has degree three.

For a converse, start with (35). Translation by \(Q\) commutes with both inversion and the order-three translations, so it descends to involutions on both spheres in (31). On the source Kummer sphere its two fixed points come from \(2R=Q\). The 3-isogeny is an isomorphism on 4-torsion, so it maps these two fixed points bijectively to the two fixed points of the target involution. Choose them as 0 and infinity on each sphere, with matching images. The descended cubic is then odd and has the form (4). This reconstructs the reciprocal marking from (35).

Independent coordinate scalings \(z\mapsto az\), \(w\mapsto bw\) reduce (4) to (8). The remaining simultaneous exchange of the two matched fixed points on both spheres also leaves \(qr/(ps)\) unchanged. Thus \(t\) is generically complete for this reciprocal marked object. The converse construction proves that its coarse parameter curve is \(X_0(6)\), not just a curve with a similar \(j\)-function.

Accordingly,

\[
\boxed{X_0(6)_t\xrightarrow{3}X_0(3)_h\xrightarrow{4}\mathbb P^1_j.}
\tag{36}
\]

These are coarse moduli statements. Individual root labels, fixed coordinate scales, differential normalizations, and field-of-definition descent are separate markings or arithmetic data. The two generator signs \(P,-P\) are exchanged by inversion; for orders three and six this does not add a generic coarse-moduli sheet. Rigid labeling of group elements can still retain an orientation. The explicit rational torsion point (26) in our Jacobian model is compatible with this statement; it does not turn the intrinsic subgroup into a universally chosen labeled sheet.

### 8.3 Cusps and enhanced automorphisms

In the \(h\)-coordinate, the cusps are \(0\) and infinity. The source \(j\)-function has pole orders 1 and 3 there. Its distinguished finite fibers are

\[
\begin{aligned}
j=0 &: h=-27\ \text{(simple)},\quad h=-3\ \text{(triple)},\\
j-1728&=\frac{(h^2+18h-27)^2}{h}.
\end{aligned}
\tag{37}
\]

Thus the two points over 1728 are \(h=-9\pm6\sqrt3\), each with ramification two. The modular orbifold \(X_0(3)\) has one enhanced order-three elliptic point, at \(h=-27\), and no order-two elliptic point. At \(h=-3\), the bare elliptic curve also has \(j=0\), but its extra automorphisms do not preserve the selected cyclic subgroup; that point is instead triply ramified in the forgetful map.

The four \(t\)-cusps are \(0,1,9,\infty\), with source \(j\)-pole orders \(1,6,2,3\). Moreover

\[
\frac{dh}{dt}=\frac{(t-9)(t+3)^2}{(t-1)^3},\qquad
h+27=\frac{(t+3)^3}{(t-1)^2}.
\tag{38}
\]

Choosing nonzero 2-torsion removes the order-three stabilizer: the enhanced point lifts with ramification three at \(t=-3\). There is no elliptic stabilizer beyond the generic central \(\pm1\) on the level-six coarse problem. These enhanced automorphism points are smooth fibers, not the singular cubic-cover specializations in §9.

## 9. Degenerations and the two kinds of genus-zero specialization

### 9.1 Discriminant and modular boundary

Equations (12) and (14) factor the complete elliptic discriminant. The following table refers to the normalized one-parameter Jacobian model; its orders are read after the usual change of scale at infinity.

| t | h | Order of the elliptic discriminant | Meaning in coefficient space |
|---|---|---:|---|
| 0 | 0 | 1 | \(q=0\) or \(r=0\); their intersection requires separate analysis |
| 9 | 0 | 2 | \(qr=9ps\), cyclic degree-three locus |
| 1 | infinity | 6 | \(ps=qr\), cancellation |
| infinity | infinity | 3 | \(p=0\) or \(s=0\), cancellation in the original degree-three chart |

The suitably scaled \(c_4\) is nonzero at each of these four cusps. Thus the minimal Weierstrass fibers are nodal/multiplicative, not cuspidal. Resolving a minimal Weierstrass total space may introduce the familiar polygonal components; a contracted Weierstrass cubic and an uncontracted correspondence model need not display the same components. Higher-order or intersecting coefficient paths can change multiplicities. The direct correspondence fibers below give the relevant distinction without treating cancellation as a smooth elliptic cover.

### 9.2 The cyclic surface qr = 9ps

On this locus, with degree three retained,

\[
\eta^2=-\frac{4p^2s}{r}(rz^2-3s)^2.
\tag{39}
\]

Over \(\mathbb C\) it is the union of two rational components, meeting at \(z=\pm\sqrt{3s/r}\). Both intersections are ordinary nodes. These components are the graphs of the two nonidentity cyclic deck transformations; the residual correspondence has split.

The target discriminant simultaneously becomes

\[
\mathcal B(w)=-4r^3s\left(w^2-\frac{27p^2s}{r^3}\right)^2.
\tag{40}
\]

The four simple branch values coalesce in pairs to two values. The specialized cubic is smooth as a rational map and has two totally ramified fibers, hence cyclic monodromy \(C_3\). Its connected Galois closure is a sphere. It is **not** the singular or reducible genus-one fiber (39). Formation of the generic connected closure and specialization do not commute in that naive sense.

This locus maps to \(t=9\), hence the \(h=0\) cusp. It must not be interpreted as a smooth special elliptic curve with extra automorphisms.

### 9.3 The cyclic line q = r = 0

Here \(w=(p/s)z^3\) and the homogeneous quartic is

\[
\eta^2=-3p^2s^2 Z^2T^2.
\tag{41}
\]

It is again two rational components with two ordinary intersections, now above \(z=0,\infty\). The two components describe the two cyclic partners of \(z\). The target branch quartic has double zeros at \(w=0,\infty\).

This coefficient locus has \(t\to0\), but it is the **intersection** of the divisors \(q=0\) and \(r=0\). Along a path where both vanish simply, \(t\) vanishes to order two and \(\Delta_E\) has order two, rather than the transverse order one of a single divisor. The coordinate normalization (8) also becomes singular because it divides by \(r\). This explains why the original correspondence fiber is reducible although the normalized generic \(t=0\) model has an irreducible node. Modular boundary data alone forget this embedding-path distinction.

### 9.4 Exactly one of q, r vanishes

For \(q=0,r\ne0\),

\[
\eta^2=-p^2s z^2(4rz^2+3s).
\tag{42}
\]

This is irreducible and nodal at \(z=0\); its normalization has genus zero. The two target branch values approaching \(w=0\) coalesce into a triple-ramification value of the cubic, while the other two remain simple. For \(r=0,q\ne0\), the analogous node and collision occur at infinity:

\[
\eta^2=-ps^2(3pz^2+4q),
\]

read as a homogeneous quartic with a double factor at infinity. Both specializations keep \(S_3\) monodromy and give ramification \((3,2,2)\). Their connected normalizations are still degree-six Galois covers, now from a sphere. They are boundaries of the same elliptic family with monodromy retained, unlike the split cyclic boundaries. Their Riemann–Hurwitz value is \(6[-2+2/3+1/2+1/2]=-2\).

## 10. What survives from the three coefficients

The generic counts are precise:

| Data retained | Intrinsic parameter | Further information forgotten |
|---|---|---|
| Bare complex elliptic curve | \(j(E)\), one modulus | Four possible cyclic 3-subgroups and three possible nonzero 2-torsion points |
| Elliptic curve plus the cyclic 3-subgroup; equivalently the generic cubic up to independent source/target Möbius maps | \(h\in X_0(3)\), one modulus | The selected reciprocal 2-torsion; three generic possibilities |
| Same object with the original reciprocal equivariance | \(t\in X_0(6)\), one modulus | Original coordinate embedding and scales |
| Four unordered critical values up to target Möbius transformation | \(j(E')\), one modulus | Which of the four generic dual 3-isogeny choices supplied the cubic |
| Original \((A,B,C)\) expression | Three complex parameters | Nothing quotiented: two generic continuous parameters are embedding data |

The generic fibers of \((A,B,C)\mapsto t\) are two-dimensional. Surjectivity onto the generic \(t\)-line is explicit: one section is

\[
\boxed{A=\frac{t+3}{1-t},\quad B=1,\quad C=\frac{t-5}{1-t}.}
\tag{43}
\]

It has \(p=r=s=8/(1-t)\) and \(q=8t/(1-t)\). Under arbitrary source and target Möbius equivalence, \(h\), rather than \(t\), is the invariant. Under equivalence preserving the selected reciprocal involutions, \(t\) is the invariant. Reversing the isogeny replaces \(h\) by \(729/h\); that reverses an oriented datum and is not silently identified here.

Over \(\mathbb R\) there is more information. The normalization scale \(\sqrt{s/r}\) can be imaginary; the orders and real/complex placement of roots and branch values matter. Most importantly, the genus-one incidence curve need not have a real point. For example, at \(t=2\),

\[
Y^2=-4Z^4-11Z^2-8
\]

has no real affine points and no real points at infinity. The section (43) realizes it at real coefficients \((A,B,C)=(-5,1,3)\). Its Jacobian has a real Weierstrass origin, but the original real genus-one curve does not. The complex origin choice in §3 therefore must not be advertised as a real birational identification in all regimes.

Even when a real origin exists, twists and real embeddings are not fixed by complex \(j\). Retaining \(y=x^2\ge0\) restricts the original real source still further; a general Möbius equivalence does not preserve that domain. No number of physical degrees of freedom is assigned to these coefficients.

## 11. Short comparison with the quadratic construction

For a separable degree-two rational map, the one other sheet is automatically a rational Möbius deck partner. Adjoining reciprocal equivariance yields the familiar quadratic \(V_4\) action, and further quotients/lifts can produce the previously studied elliptic closure.

For the generic cubic, the two other sheets cannot be chosen rationally over the original source. Their ordered incidence relation itself normalizes to genus one, and its six root orderings form the \(S_3\) closure. The 3-torsion translation subgroup is a consequence of this cubic closure, not a continuation of the quadratic deck involution.

No identification or isogeny with the earlier quadratic-tower Edwards curve has been tested or inferred. Writing both kinds of elliptic curve in a standard Edwards form is not such an identification.

## 12. Tri-Octagon comparison gate: an exact finite incidence match

This subsection was undertaken only after the elliptic structure above was derived. It uses the already documented mathematical patches, not a presumed physical interpretation of “gaps.”

The existing [six-patch report, §2–§3.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md) defines three upper candidate notch triangles and their three lower mirrors. It explicitly distinguishes these measurement triangles from boundary components: the underlying shell has two connected rims. Its source formula, using a different symbol \(\ell\) for the triangle parameter to avoid the modular \(t\), is

\[
\mathcal P_j^\epsilon:
X=O+r(\ell)u_j+\omega v_j+\epsilon h(\ell)e_z,
\quad 0\le\ell\le1,\quad |\omega|\le d\ell/2,
\tag{44}
\]

where \(j\in\mathbb Z/3\), \(\epsilon=\pm1\),

\[
u_j=R_z(2\pi j/3)(0,1,0),\quad
v_j=R_z(2\pi j/3)(-1,0,0),
\]

\(O=(0,\sqrt3/6,0)\), \(d=1-\sqrt2/2\), \(r(\ell)=1/\sqrt3-\sqrt3d\ell/2\), and \(h(\ell)=(\sqrt2-1)/2+d\ell>0\).

On centered spatial coordinates define

\[
R=R_z(2\pi/3),\qquad S=\operatorname{diag}(-1,1,-1).
\tag{45}
\]

The second is a half-turn about the horizontal \(u_0\)-axis through \(O\), combining the documented vertical and horizontal reflections. These are actual rigid maps, not permutations invented solely from the count six. They satisfy

\[
R^3=S^2=1,\quad SRS=R^{-1},
\]

and act on the whole finite triangles by

\[
R:\mathcal P_j^\epsilon\mapsto\mathcal P_{j+1}^\epsilon,
\qquad
S:\mathcal P_j^\epsilon\mapsto\mathcal P_{-j}^{-\epsilon}.
\tag{46}
\]

For the second identity, \(Su_j=u_{-j}\), \(Sv_j=-v_{-j}\), and \(Se_z=-e_z\); it preserves the triangle inequalities by \(\omega\mapsto-\omega\). A nonidentity rotation fixes no label, and each involution swaps upper and lower. Thus the group acts freely and transitively on the six triangles: this is a regular \(S_3\)-set.

There is an explicit incidence-preserving bijection to the six ordered pairs of distinct elements of \(\mathbb Z/3\):

\[
\boxed{\Phi:\mathcal P_j^\epsilon\longmapsto(j,j+\epsilon).}
\tag{47}
\]

Here \(+1,-1\) are read modulo three. Under \(R\), both entries increase by one; under \(S\), both are negated. Hence (47) intertwines the actual geometric generators with the natural \(S_3\) permutation action on three symbols. Forgetting the second entry corresponds to forgetting upper/lower and retaining the vertical pair \(j\). Each such pair has an order-two stabilizer, and the three stabilizers are precisely the three transposition subgroups.

This matches the finite monodromy/incidence system of a regular cubic fiber: three sheet labels, six ordered sheet pairs, and the projection from an ordered pair to its first sheet. Technically, label permutation is the left regular monodromy action on root orderings; the deck transformations (22) permute positions and provide the commuting right regular action. These two standard actions must not be confused. The displayed identification concerns the former together with its three-point quotient.

**Classification: exact finite group-action/incidence equivalence, with chosen initial labels and orientation.** It is stronger than an equality of counts. It is not a canonical assignment of a particular patch to a particular analytic sheet: relabeling changes the chosen bijection. No map varying over the \(w\)-sphere, four branch values, elliptic modulus, ramification, complex structure, metric identification, or physical attachment is supplied by the shell data. The existence of this finite \(S_3\)-set is not unique to Tri-Octagon; many configurations share it.

The source also distinguishes its upper/lower swap from its cyclic rotation: these alone commute and generate \(C_3\times C_2\). The noncommuting involution required for \(S_3\) is specifically the half-turn \(S\), which reverses the pair index as well as swapping heights. Omitting that step would give the wrong group.

This exact finite match triggers the user's comparison stop condition. No broader shell/elliptic identification is attempted.

## 13. Verification, sources, and integrity

`verify_cubic_elliptic.py` ran successfully with SymPy 1.14.0 and mpmath 1.3.0. Its **73 exact checks** cover the birational identities, quartic/elliptic discriminants, 3-torsion and doubling, root-incidence actions, explicit 3-isogeny, \(j\)-formulas, generic recovery of \(h\) from the oriented \(j\)-pair, degeneration factors, Riemann–Hurwitz arithmetic, and the exact finite-patch action and incidence bijection.

Three fixed complex points at \(t=17\) were also evaluated at 100 decimal digits. Maximum absolute residuals were approximately \(2.52\times10^{-95}\) for the Weierstrass transformation and \(4.09\times10^{-96}\) for the isogeny. These are supporting numerical checks, not proofs of algebraic equivalence. The topological and moduli arguments are given in prose above, not claimed to be machine-formalized.

The explicit modular formulas were checked against Elkies' primary exposition, §4, equation (80), with the source/quotient orientation recorded. Montgomery conventions were checked against the Explicit-Formulas Database. Neither source is being used to claim priority for this reconstruction, and no broad novelty search was performed. The Tri-Octagon comparison reads the existing mathematical report without importing or running kernel code.

All new files are external, in `C:/TORMENT/TRIOCTAGON_new/research/three_way_cubic_elliptic_20261005`. `verification_results.json` contains the symbolic and numerical records. `integrity_baseline.json` and `integrity_result.json` record preserved repository HEAD/status and **1,279 protected file identities**, including all tracked repository files and the completed reconstruction, kernel, and UI files present in the specified protected directories. Source identities are recorded in `source_manifest.json`; final deliverable hashes are in `artifact_manifest.json`.

No completed paper, repository file, kernel, UI, or historical report was modified. No commit, publication, or physical implementation was performed.

## 14. Final dictionary

| Object | Exact meaning |
|---|---|
| **3 sheets** | Three source points in a regular fiber of the original degree-three rational map; equivalently the three cosets for a transposition subgroup. |
| **\(S_3\)** | The Galois group of the closure, acting by permutations of three roots; geometrically \(\langle T_P,[-1]\rangle\). |
| **6-element Galois fiber** | Six ordered pairs of distinct roots, equivalently six complete root orderings. Deck and monodromy supply commuting regular actions. |
| **\(C_3\) subgroup** | The free translations \(\{1,T_P,T_{-P}\}\); its quotient is the natural degree-three isogeny \(E\to E'\). |
| **\(C_2\) subgroups** | The three subgroups generated by \([-1],T_P[-1],T_{-P}[-1]\); their sphere quotients give conjugate degree-three intermediate covers. |
| **\(E_3\)** | The smooth complex genus-one normalization of the residual equal-value correspondence, made elliptic by choosing an origin; over smaller fields it may first be a torsor. |
| **4 branch values** | Images of \(E'[2]\) under the quotient \(E'\to\mathbb P^1_w\); their ordered cross-ratio is a Legendre parameter of the 3-isogenous quotient. |
| **Cyclic loci** | Specializations where the residual correspondence splits and the smooth cubic becomes a cyclic rational cover; singular elliptic-boundary fibers are distinct from its specialized connected closure. |
| **Original reciprocal involution** | An equivariance \(z\mapsto-z,w\mapsto-w\); its simultaneous lift is translation by the distinguished nonzero \(Q\in E[2]\). |
| **\(h\)** | Hauptmodul for \((E,\langle P\rangle)\in X_0(3)\), after forgetting the reciprocal 2-torsion marking. |
| **\(t\)** | Hauptmodul for \((E,\langle P\rangle,Q)\in X_0(6)\); two continuous original coefficient parameters remain coordinate-embedding data. |
| **Tri-Octagon 3/6 match** | An explicitly verified equivalence of the six candidate-patch \(S_3\)-set and its three-pair quotient with the finite cubic sheet-incidence system; no elliptic or branched-cover identification follows. |
