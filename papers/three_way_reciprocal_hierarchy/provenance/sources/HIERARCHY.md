# Three-Way reciprocal hierarchy, n = 2–4: first extension v0.1

5 October 2026. External mathematical research. No physics interpretation or novelty claim.

## 1. Main result, scope, and the early-stop condition

The proposed hierarchy exists, but reciprocal equivariance does **not** preserve the special quadratic deck symmetry. For the covers actually specified in this work order,

\[
F_n:\mathbb P^1_y\longrightarrow\mathbb P^1_v,
\qquad F_n=P_n/P_n^*,
\]

the generic answer is

\[
\boxed{\operatorname{Mon}(F_n)=S_n,\qquad
g(\widetilde F_n)=1+\frac{n!}{2}(n-3).}
\tag{1}
\]

Here \(\widetilde F_n\) is the connected Galois closure over the **unchanged target** \(v=F_n(y)\). Thus the generic genera for \(n=2,3,4\) are **0, 1, 13**, respectively. Section 9 proves (1), including the nonemptiness of the required generic locus within the coefficient-reversal family. This is a theorem, not an extrapolation from numerical examples.

There is an essential correction to the premise “\(n=2\longrightarrow g=1\).” The degree-two map \(F_2\) is already Galois and its source is a sphere, so its own Galois closure has genus zero. The previously reconstructed genus-one object was the closure of a different, larger cover: the degree-eight quotient tower that includes the quotient by target reciprocity and the squaring cover \(y=x^2\). These are different function-field extensions. This report does not change that earlier result or extend that larger tower to higher degree.

The requested stop conditions have been reached: the cubic loses the generic single-valued partner, has an elliptic Galois closure, and the quartic's generic closure already has genus 13. Accordingly, this report completes the cubic calculation and records only the direct quartic, general-degree, and squaring-cover consequences. It does **not** undertake an exhaustive quartic exceptional-locus census, a higher-degree moduli classification, or a new elliptic/modular reconstruction.

All statements below are over \(\mathbb C\), in characteristic zero, unless explicitly designated real. “Generic” means a nonempty Zariski-open subset of coefficient space. Coefficients are not assumed positive. Common factors must be canceled before interpreting a rational map; the original displayed fraction still has holes at such common zeros.

## 2. Established mathematical setting

This family belongs to the standard setting of rational maps commuting with a Möbius involution. Let

\[
\mathcal C(y)=\frac{y-1}{y+1},\qquad
z=\mathcal C(y),\qquad
H(z)=\mathcal C\circ F_n\circ\mathcal C^{-1}(z).
\]

Reciprocity becomes

\[
H(-z)=-H(z),\qquad H(z)=z\,\Psi(z^2)
\tag{2}
\]

for a rational function \(\Psi\). To prove the last assertion, \(H(z)/z\) is invariant under \(z\mapsto-z\), whose invariant field is \(\mathbb C(z^2)\). This normal form is also the order-two instance of Miasnikov–Stout–Williams, §2.1, Lemma 2, in the linked arXiv version. Their “automorphisms” are **commuting/conjugacy automorphisms**, not the deck transformations considered here. Their classification therefore must not be quoted as a classification of these covers' deck or monodromy groups. [Primary source](https://arxiv.org/pdf/1408.5655)

For this uncanceled coefficient chart, the generic forms are

\[
\begin{array}{ll}
n=2m+1:&H(z)=z\,U_m(z^2)/V_m(z^2),\\
n=2m:&H(z)=z\,U_{m-1}(z^2)/V_m(z^2).
\end{array}
\tag{3}
\]

The indicated leading and constant coefficients are generically nonzero. The odd-degree component fixes both \(0,\infty\); the even-degree component sends both to 0. After cancellation a different component or a lower degree can result.

Pakovich's treatment identifies the normalization of a rational function with its Galois closure and describes the genus-zero and genus-one cases using ramification/orbifold data; see §2 and Theorems 1.1–1.2. It supplies established context for the cubic result. It is not a complete coefficient-by-coefficient classification of the entire hierarchy in this work order. This bounded literature check establishes a standard mathematical species, not a claim of novelty or a completed prior-art audit. [Primary source](https://arxiv.org/pdf/1609.03482)

## 3. Exact identities for every n

Write \(P=P_n\), \(Q=P_n^*=y^nP(1/y)\), and let \(G=\gcd(P,Q)\) be monic. Set \(N=P/G\), \(D=Q/G\). The constant term of \(P\) is 1 and the leading coefficient of \(Q\) is 1, even if \(a_0=0\).

### 3.1 Reciprocity, degree, and divisors

Reversing twice gives \(Q^*=P\), so directly in the function field,

\[
F_n(1/y)=\frac{y^{-n}Q(y)}{y^{-n}P(y)}=\frac1{F_n(y)}.
\tag{4}
\]

This identity survives cancellation. Since \(Q\) has degree \(n\),

\[
\boxed{\deg F_n=n-\deg G}
\tag{5}
\]

for a nonconstant reduced map. There is no common root at 0 or infinity. Vanishing \(a_0\) alone does not lower the map degree.

In divisor notation, if \(R(y)=1/y\), then

\[
\operatorname{ord}_{R(p)}F_n=-\operatorname{ord}_pF_n.
\tag{6}
\]

Every surviving zero has a reciprocal pole of exactly the same order, including the pair \(0,\infty\). Common-root cancellation also occurs in reciprocal pairs, except at the fixed points \(\pm1\).

For \(a_0\ne0\), write \(P=a_0\prod_{i=1}^n(y-r_i)\). Then

\[
Q=a_0\prod_{i=1}^n(1-r_i y).
\]

Cancellation occurs exactly when some \(r_i r_j=1\), allowing \(i=j\), which gives \(r_i=\pm1\). Equivalently, \(\operatorname{Res}_y(P,Q)=0\). A useful root expression is

\[
\operatorname{Res}(P,Q)
=a_0^{2n}\prod_{i,j}(1-r_i r_j)
=(-1)^n a_0^{2n-2}P(1)P(-1)
\prod_{i<j}(1-r_i r_j)^2.
\tag{7}
\]

Use the polynomial resultant or the gcd when \(a_0=0\); (7)'s degree-\(n\) root parameterization then does not apply. Repeated zeros are detected by the polynomial discriminant when the degree is fixed. They give repeated reciprocal poles if uncanceled. Repeated zeros/poles need not lower monodromy: a double zero is an ordinary simple ramification point with critical value 0.

### 3.2 The ±1 fibers and parity

The exact reduced equations are

\[
F_n=1\iff N-D=0,\qquad
F_n=-1\iff N+D=0.
\tag{8}
\]

Read these as homogeneous fiber equations on \(\mathbb P^1\), including infinity where appropriate. At finite points, \(D\ne0\) is understood. Equivalently, divide \(P-Q\) and \(P+Q\) by \(G\) before finding their roots. Cross-multiplying the unreduced fraction without removing common factors can create false solutions.

Reversal makes \(P-Q\) anti-reciprocal and \(P+Q\) reciprocal. Consequently,

\[
\begin{array}{c|cc}
&P-Q&P+Q\\ \hline
n\text{ even}&(y-1)(y+1)\text{ divides}&\text{no forced linear factor}\\
n\text{ odd}&y-1\text{ divides}&y+1\text{ divides}.
\end{array}
\tag{9}
\]

Thus, provided there is no cancellation there,

\[
F_n(1)=1,\qquad F_n(-1)=(-1)^n.
\tag{10}
\]

The answer to “is \(y=1\) always a +1 lock?” is **yes for the defined, uncanceled fraction, but not unconditionally after continuation across a canceled point**. If \(P\) has a zero of order \(m\) at \(\epsilon=\pm1\), reversal has the same order and the reduced continuation is

\[
\boxed{F_n(\epsilon)=\epsilon^n(-1)^m.}
\tag{11}
\]

Indeed, near \(\epsilon\), \(1/y-\epsilon=-(y-\epsilon)+O((y-\epsilon)^2)\), and the extra factor \(y^n\) tends to \(\epsilon^n\). Odd-order cancellation flips the lock's sign; even-order cancellation preserves it. The original fraction is undefined there in either case. For example, \(F_2\) with \((A,B)=(2,3)\) reduces to \((2y-1)/(y-2)\) and continues to \(-1\) at \(y=1\).

Likewise \(F_n=1/F_n\) has exactly the reduced \(+1\) and \(-1\) fibers, since those are the two fixed values of target inversion. Neither a zero nor a pole satisfies it.

### 3.3 Values at 0 and infinity; constant exceptions

For \(a_0\ne0\),

\[
F_n(0)=1/a_0,\qquad F_n(\infty)=a_0.
\tag{12}
\]

If \(a_0=0\) and \(d_P=\deg P<n\), then 0 is a pole and infinity a zero, each of order \(n-d_P\). Neither is canceled.

The only constant maps are \(F_n\equiv1\) and \(F_n\equiv-1\). In the user's coefficient notation they occur precisely as follows:

- \(+1\): \(a_0=1\) and \(a_j=a_{n-j}\) for every interior index.
- \(-1\): \(a_0=-1\) and \(a_j=-a_{n-j}\) for every interior index. For even \(n\), the middle coefficient is then zero.

These follow from \(P=cP^*\) and reversal, which forces \(c^2=1\). Constant maps are excluded from statements about finite covers and monodromy.

### 3.4 Critical points

After cancellation, the critical divisor is the homogeneous Wronskian of \(N,D\). On the affine line it is computed by

\[
W_{\rm red}=N'D-ND',\qquad
P'Q-PQ'=G^2W_{\rm red}.
\tag{13}
\]

Homogenize to degree \(2\deg F_n-2\) to include critical points at infinity. A zero of multiplicity \(m\) in this divisor has local degree \(m+1\). Formula (13) includes ramified poles, whereas using only an ordinary derivative at finite-valued points can miss them.

The unreduced Wronskian satisfies

\[
W(1/y)=y^{2-2n}W(y).
\tag{14}
\]

Critical points and their values are therefore paired by \((c,F(c))\mapsto(1/c,1/F(c))\). For a nonconstant equivariant map, the local degree at a reciprocal fixed point is odd: in local coordinates the equivariance is an odd function. Thus \(\pm1\) cannot be *simple* critical points. They may become points of local degree 3 or higher on exceptional loci.

## 4. Complete cubic correspondence and cancellation

Let

\[
P=Ay^3-By^2-Cy+1,\qquad Q=y^3-Cy^2-By+A.
\]

### 4.1 Exact level equations, resultant, and zeros

\[
\begin{aligned}
P-Q&=(y-1)\big[(A-1)(y^2+y+1)+(C-B)y\big],\\
P+Q&=(y+1)\big[(A+1)(y^2-y+1)-(B+C)y\big].
\end{aligned}
\tag{15}
\]

Define

\[
H_3=A^2+AC-B-1.
\]

Then

\[
\boxed{\operatorname{Res}(P,Q)
=(A-B-C+1)(A+B-C-1)H_3^2.}
\tag{16}
\]

The first two factors are the common-root conditions at \(+1,-1\). The squared factor is the reciprocal-pair cancellation condition, including its collisions with the fixed points.

The remaining lock-fiber solutions in (15) can also be written as reciprocal pairs:

\[
\begin{array}{ll}
F_3=1:&y=1\ \text{or}\ y^2-\tau_+y+1=0,
\quad\tau_+=(B-C)/(A-1)-1,\\
F_3=-1:&y=-1\ \text{or}\ y^2-\tau_-y+1=0,
\quad\tau_-=1+(B+C)/(A+1).
\end{array}
\]

For real coefficients and finite \(\tau\), \(|\tau|>2\) gives two real reciprocal points, \(|\tau|<2\) gives a nonreal conjugate pair on the unit circle, and \(\tau=\pm2\) gives a repeated fixed point. When the divided coefficient vanishes, use (15) projectively: on the degree-three locus, \(A=1\) has \(+1\) fiber \(\{0,1,\infty\}\), and \(A=-1\) has \(-1\) fiber \(\{0,-1,\infty\}\). Common-root loci must still be reduced first.

The zeros are the roots of \(P\), and poles their reciprocals, after the gcd is removed. For \(A\ne0\), the zero discriminant is

\[
\operatorname{Disc}(P)
=B^2C^2+4AC^3+4B^3+18ABC-27A^2.
\tag{17}
\]

For real coefficients it is positive for three distinct real zeros, negative for one real zero and a nonreal conjugate pair, and zero for repeated zeros. Apply this to the uncanceled cubic; after cancellation use the reduced polynomial. The reversed cubic has the same discriminant.

### 4.2 Exact equal-value factorization

Put

\[
\alpha=B-AC,\quad b=C-AB,\quad h=A^2-1.
\]

Then

\[
\boxed{F_3(u)-F_3(y)=\frac{(u-y)\mathcal Q_y(u)}{Q(u)Q(y)},}
\tag{18}
\]

where

\[
\begin{aligned}
\mathcal Q_y(u)={}&(\alpha y^2+by+h)u^2\\
&+\big[by^2+(h+B^2-C^2)y+b\big]u\\
&+hy^2+by+\alpha.
\end{aligned}
\tag{19}
\]

This is the requested residual quadratic correspondence. Its two roots are the two other sheets in a generic fiber. Coefficient vanishings at an individual \(y\) are interpreted projectively, not as a global splitting.

For an uncanceled map, a rational single-valued solution \(u=M(y)\ne y\) would satisfy \(F_3\circ M=F_3\). Degrees multiply, so \(\deg M=1\). It would therefore be a Möbius deck transformation. The order of the deck group divides 3; any nonidentity element makes the cover cyclic Galois of degree three. Consequently there is **no generic rational partner**, and the residual quadratic is generically irreducible over \(\mathbb C(y)\).

### 4.3 Coordinates exposing all cubic exceptional loci

Use \(z=(y-1)/(y+1)\) and \(w=(F_3-1)/(F_3+1)\). Define

\[
\begin{aligned}
p&=A+B-C-1,&q&=3(A-1)-B+C,\\
r&=3(A+1)+B+C,&s&=A+1-B-C.
\end{aligned}
\]

Then exactly

\[
\boxed{w=\frac{z(pz^2+q)}{rz^2+s}.}
\tag{20}
\]

Here \(r+s-p-q=8\), fixing the otherwise irrelevant common scale. Also

\[
ps-qr=-8H_3.
\tag{21}
\]

The condition for degree three is precisely

\[
\boxed{ps(ps-qr)\ne0.}
\tag{22}
\]

For completeness, the lower-degree strata are determined without a parameter scan:

- Constants: \(A=1,B=C\) gives \(+1\); \(A=-1,C=-B\) gives \(-1\).
- Degree two: exactly one of \(p,s\) vanishes and \(ps-qr\ne0\).
- Every other nonconstant point on (16)'s zero locus has degree one.

To check this last classification, use the homogeneous pair \(pZ^3+qZV^2\), \(rZ^2V+sV^3\). A zero of \(s\) introduces the common factor at \(z=0\), a zero of \(p\) the common factor at infinity, and \(ps=qr\) the quadratic common factor when both are nonzero. Their intersections give either a quadratic common divisor or proportional forms. This also handles repeated cancellation at a fixed point. Lower-degree covers are classified by their reduced degree: a nonconstant quadratic has deck/monodromy \(C_2\) and genus-zero closure; a Möbius map has trivial monodromy.

In the coordinates (20), after removing \(v-z\), the equal-value correspondence is particularly small:

\[
\mathcal K_z(v)
=p(rz^2+s)v^2+(ps-qr)zv+s(pz^2+q)=0.
\tag{23}
\]

Its discriminant in \(v\) is

\[
\mathcal D(z)=-4p^2rsz^4+
(q^2r^2-6pqrs-3p^2s^2)z^2-4pqs^2.
\tag{24}
\]

On (22), this quadratic splits over \(\mathbb C(z)\) **if and only if**

\[
\boxed{q=r=0\quad\text{or}\quad qr=9ps.}
\tag{25}
\]

These conditions are proved by the ramification classification below, and directly verified by (24). On \(qr=9ps\),

\[
\mathcal D(z)=-\frac{4p^2s}{r}(rz^2-3s)^2.
\tag{26}
\]

On \(q=r=0\), \(\mathcal D=-3p^2s^2z^2\). If just one of \(q,r\) vanishes, (24) is not a rational square; a genus-zero correspondence on such a locus does **not** imply a single-valued partner over the original \(z\)-line.

In the original coefficients the two cyclic loci are

\[
\boxed{B=-3,\quad C=-3A}
\qquad\text{or}\qquad
\boxed{3AC+B^2-3B-C^2=0,}
\tag{27}
\]

always restricted by (22). They are disjoint in that degree-three domain. This is a complete cyclic/deck/splitting criterion over \(\mathbb C\), not merely a list of examples.

## 5. Cubic critical points, branch values, monodromy, and closure

### 5.1 Critical points and values in explicit equations

Let \(c=3(A^2-1)+B^2-C^2\). The original-coordinate Wronskian is

\[
W_3(y)=\alpha(y^4+1)+2b(y^3+y)+cy^2.
\tag{28}
\]

For \(y\ne0,\infty\), put \(\tau=y+1/y\). The critical-point equation reduces to

\[
\alpha\tau^2+2b\tau+(c-2\alpha)=0,
\qquad y^2-\tau y+1=0.
\tag{29}
\]

Projective homogenization of (28) handles \(\alpha=0\) and infinity. In the coordinates (20), the same critical divisor is

\[
J(z)=prz^4+(3ps-qr)z^2+qs,
\tag{30}
\]

homogenized as a binary quartic. Thus critical points are obtained by a quadratic equation for \(z^2\), with critical values found by (20). Alternatively the critical values in the \(w\)-target are the zeros of the binary quartic

\[
\boxed{\mathcal B(w)=
-4r^3s w^4+(q^2r^2+18pqrs-27p^2s^2)w^2-4pq^3.}
\tag{31}
\]

This is \(\operatorname{Disc}_z(pz^3-wrz^2+qz-ws)\). Homogenize to degree four to retain a branch at \(w=\infty\). The original target values are \((1+w)/(1-w)\). Equivalently, compute the discriminant of \((A-v)y^3+(-B+vC)y^2+(-C+vB)y+1-vA\) in \(y\).

### 5.2 Exhaustive ramification classification in degree three

On (22), the discriminant of (30) is

\[
16pqrs(ps-qr)^2(9ps-qr)^2.
\tag{32}
\]

Together with the projective interpretation, this yields the complete table:

| Coefficient condition, always with (22) | Ramification indices over distinct branch values | Monodromy | Deck group | Closure degree | Closure genus |
|---|---|---|---|---:|---:|
| \(qr\ne0\), \(qr\ne9ps\) | \(2,2,2,2\) | \(S_3\) | trivial | 6 | 1 |
| Exactly one of \(q,r\) is zero | \(3,2,2\) | \(S_3\) | trivial | 6 | 0 |
| \(q=r=0\) | \(3,3\) | \(C_3\) | \(C_3\) | 3 | 0 |
| \(qr=9ps\) | \(3,3\) | \(C_3\) | \(C_3\) | 3 | 0 |

Proof of completeness: a degree-three map has total ramification 4 and local degree at most 3. The only possible multiplicity partitions of the critical divisor are four simple points, one double plus two simple points, or two double points. Distinct critical points cannot have the same image: two simple ramification points in one fiber would already use degree 4, and a triple point uses the entire degree-three fiber. Hence no further critical-value collision stratum has been omitted. Equation (30) realizes the three possibilities exactly as shown.

For the first two rows, the connected cover has transitive monodromy in \(S_3\) and includes a transposition, so the group is \(S_3\). In the last two rows the branch cycles are 3-cycles, so it is \(C_3\) and the degree-three cover is Galois. A nontrivial deck transformation could only occur in these last rows, proving (25)'s converse.

The genera follow from Galois Riemann–Hurwitz. For the first row,

\[
2g-2=6[-2+4(1-1/2)]=0.
\]

For the second row it is \(6[-2+2/3+1/2+1/2]=-2\); for the cyclic rows it is \(3[-2+2(2/3)]=-2\).

### 5.3 An explicit generic genus-one Galois closure

Adjoin a root \(v\) of (23) to \(\mathbb C(z)\). The third root of the fiber cubic is then rational in \(z,v\), by its elementary symmetric functions. Thus this degree-two extension of \(\mathbb C(z)\) is the full splitting field over \(\mathbb C(w)\). A model is

\[
\boxed{E_3:\eta^2=\mathcal D(z),}
\tag{33}
\]

with \(\mathcal D\) from (24), using the smooth projective normalization. Its quartic discriminant is

\[
256p^3qrs^3(ps-qr)^6(9ps-qr)^2.
\tag{34}
\]

On the first row of the table it has four distinct roots and hence genus one. The degree-six map to \(w\) is the Galois closure, with \(S_3\) acting by permutations of the three roots of the fiber cubic. Equivalently, (23) is a curve of bidegree \((2,2)\) whose generic normalization is (33). On cyclic loci the correspondence splits; it should not be described as a connected elliptic closure there.

This elliptic curve has arisen from the cubic's multivalued equal-value correspondence. It is not an identification with the previous quadratic quotient tower's Edwards curve. No such comparison is attempted here.

### 5.4 Rational transformations on the two cyclic loci

Let \(\omega^3=1\), \(\omega\ne1\).

If \(q=r=0\), then \(w=(p/s)z^3\). The deck transformations are \(z\mapsto\omega z,\omega^2z\). In the original coordinate these are

\[
y\longmapsto\frac{1+\omega^j(y-1)/(y+1)}{1-\omega^j(y-1)/(y+1)},\quad j=1,2.
\]

If \(qr=9ps\), choose \(a^2=3s/r\), put \(\kappa=3pa/r\), and set \(h(z)=(z-a)/(z+a)\). Direct substitution gives

\[
\frac{w-\kappa}{w+\kappa}=h(z)^3.
\tag{35}
\]

The two deck transformations are \(h^{-1}(\omega^j h(z))\). Constants and square roots are taken over \(\mathbb C\); these formulas are not a blanket claim of real Möbius partners for real coefficients.

The involution \(R\) is \(z\mapsto-z\), and sends \(w\mapsto-w\); it is not a deck transformation of a nonconstant \(F_3\). Adjoining it to the cyclic deck group gives:

- \(C_6\) on \(q=r=0\), because it commutes with \(z\mapsto\omega z\).
- A dihedral group of order six on \(qr=9ps\), because \(h(-z)=1/h(z)\) and conjugation inverts the order-three generator.

These are groups of source transformations preserving or inverting the target value, not groups entirely fixing the target. A \(V_4\) deck group is impossible for a degree-three cover because its order would not divide 3. Generically even this extended group is just \(\{1,R\}\).

## 6. The bounded quartic calculation

Let \(P=Ay^4-By^3-Cy^2-Dy+1\), \(Q=y^4-Dy^3-Cy^2-By+A\). Exactly,

\[
\begin{aligned}
P-Q&=(y^2-1)\big[(A-1)(y^2+1)+(D-B)y\big],\\
P+Q&=(A+1)(y^4+1)-(B+D)(y^3+y)-2Cy^2.
\end{aligned}
\tag{36}
\]

The \(+1\) locks at both \(\pm1\) are an even-degree effect. They do not force an equal-value involution on the whole source.

Put

\[
H_4=A^3+A^2C-A^2+ABD-2AC-AD^2-A-B^2+BD+C+1.
\]

Then

\[
\boxed{\operatorname{Res}(P,Q)
=(A-B-C-D+1)(A+B-C+D+1)H_4^2.}
\tag{37}
\]

As before, the linear factors are fixed-point cancellations and the squared factor records reciprocal-pair cancellation. Intersections are resolved by the gcd, not by counting resultant-factor multiplicities as canceled degrees.

Define

\[
\begin{aligned}
\alpha_4&=B-AD,&b_4&=2C(1-A),\\
c_4&=-3AB+BC-CD+3D,&d_4&=4A^2+2B^2-2D^2-4.
\end{aligned}
\]

The critical polynomial is

\[
W_4=\alpha_4(y^6+1)+b_4(y^5+y)+c_4(y^4+y^2)+d_4y^3.
\tag{38}
\]

Its reciprocal reduction is the cubic

\[
\alpha_4\tau^3+b_4\tau^2+(c_4-3\alpha_4)\tau+d_4-2b_4=0,
\qquad \tau=y+1/y.
\tag{39}
\]

Each solution gives two critical points through \(y^2-\tau y+1=0\), subject to multiplicities and the projective treatment of 0 and infinity. The critical values are \(F_4(c_i)\), or equivalently the roots of the binary sextic \(\operatorname{Disc}_y(P-vQ)\). The generic situation has six simple critical points and six distinct branch values, paired reciprocally.

For an exact compact form of the remaining equal-value cubic, write \(P(y)=\sum_{i=0}^4c_i y^i\), where \((c_0,c_1,c_2,c_3,c_4)=(1,-D,-C,-B,A)\). Then

\[
\frac{P(u)Q(y)-P(y)Q(u)}{u-y}
=\sum_{0\le j<i\le4}(c_ic_{4-j}-c_jc_{4-i})(uy)^j
\sum_{k=0}^{i-j-1}u^{i-j-1-k}y^k.
\tag{40}
\]

The verification script checks this polynomial identity directly. This cubic is generically irreducible over \(\mathbb C(y)\): in \(S_4\), the stabilizer of one sheet is \(S_3\), which acts transitively on the other three. There is no generic rational partner or nontrivial Möbius deck transformation. The connected Galois closure has degree 24, and

\[
2g-2=24[-2+6(1-1/2)]=24,\qquad\boxed{g=13.}
\tag{41}
\]

Several genuine exceptional loci demonstrate why an exhaustive census would be a separate task:

- Cancellation: (37), followed by reduction.
- Constant \(+1\): \(A=1,B=D\), with \(C\) arbitrary.
- Constant \(-1\): \(A=-1,D=-B,C=0\).
- \(B=D=0\), where degree four is retained: \(F_4(y)=F_{2;A,C}(y^2)\). This has the deck involution \(y\mapsto-y\) and is decomposable. Its monodromy is imprimitive, rather than generic \(S_4\).
- \(B=C=D=0\), \(A^2\ne1\): \(F_4=(Ay^4+1)/(y^4+A)\) is a cyclic Galois degree-four cover, with deck group \(C_4\).
- \(A=-1,B=D=0,C\ne0\): the degree-four map has the four deck transformations \(y,-y,i/y,-i/y\), so it is a \(V_4\) Galois cover.

The last two have genus-zero closures. These are proved examples, not a claim that all quartic exceptional covers lie on the displayed loci. A critical-divisor discriminant detects nonsimple ramification, and the discriminant of the branch-value polynomial detects collisions of distinct critical values. Unlike degree three, two simple ramification points **can** share a degree-four fiber, with partition \((2,2)\). Thus the cubic's very short exceptional classification does not extend verbatim.

## 7. Direct comparison with n = 2

This table concerns \(F_n:\mathbb P^1_y\to\mathbb P^1_v\) itself, not a quotient of its target or the extra \(x\)-cover.

| Property | n = 2 | n = 3 | n = 4 |
|---|---|---|---|
| Generic degree | 2 | 3 | 4 |
| Reciprocal equivariance | \(F(1/y)=1/F(y)\) | same | same |
| Other equal-value sheets | One Möbius partner | Two roots of an irreducible quadratic correspondence | Three roots of an irreducible cubic correspondence |
| Generic deck group | \(C_2\) | trivial | trivial |
| Generic monodromy | \(S_2=C_2\) | \(S_3\) | \(S_4\) |
| Degree of Galois closure | 2 | 6 | 24 |
| Genus of Galois closure | 0 | 1 | 13 |
| Forced uncanceled +1 locks | \(y=\pm1\) | \(y=1\) | \(y=\pm1\) |
| Value at uncanceled \(y=-1\) | +1 | −1 | +1 |
| Simple generic branch values | 2 | 4 | 6 |
| Special coefficient loci | Cancellation \((A-1)^2[(A+1)^2-B^2]=0\); zero/pole repetition \(B^2=4A\) | (16), (25), and \(q=0\) or \(r=0\) as classified above | (37), decomposable and Galois examples above; further strata not classified |

For \(n=2\), the single other sheet must be rational: any separable quadratic extension is Galois. Its nontrivial deck map is

\[
T(y)=\frac{(A+1)y-B}{By-(A+1)}
\]

on the degree-two locus. The reciprocal involution \(R\) normalizes this unique nonidentity deck transformation and hence commutes with it. Together they give \(V_4\), with \(T\) fixing \(F\) and \(R,RT\) inverting \(F\). The full \(V_4\) is the deck group of the further invariant quotient, **not** of \(F_2\) itself.

For \(n\ge3\), more than one other sheet remains. Generic monodromy permutes those other sheets transitively, preventing a rational choice of one. This is the mathematical reason degree two is exceptional. Even parity by itself does not restore the quadratic mechanism.

## 8. Exact witnesses and numerical verification

The symbolic script `verify_hierarchy.py` supplies **51 exact algebraic checks** and **4 numerical residual checks**. There is no coefficient scan. Two fixed witnesses certify that the desired low-degree open loci are nonempty:

For \((A,B,C)=(2,3,5)\),

\[
W_3=-7y^4-2y^3-7y^2-2y-7,
\quad\operatorname{Disc}(W_3)=17000000\ne0,
\]

and

\[
\operatorname{Disc}_y(P-vQ)
=5(353v^4-1222v^3+1763v^2-1222v+353),
\]

whose discriminant is \(1228250000000000\ne0\). The numerator/denominator resultant is also nonzero. This is an exact witness of four simple critical points with distinct values, hence \(S_3\) and genus one.

For \((A,B,C,D)=(2,3,5,7)\),

\[
W_4=-11y^6-10y^5-17y^4-68y^3-17y^2-10y-11,
\]

with discriminant \(376072090731675648\ne0\). The branch polynomial is

\[
-96(7151v^6-35048v^5+78095v^4-100468v^3
+78095v^2-35048v+7151),
\]

and its discriminant is the nonzero integer

\[
3646562824941264253142253156816617538226238952132575232.
\]

This is an exact witness of six distinct simple branch values, hence \(S_4\) and genus 13. Exact nonvanishing, rather than a floating-point root plot, is what proves these examples lie in the stated open loci.

Numerical evaluation used mpmath at 100 digits and SymPy `nroots` at 85 digits. These are numerical approximations, not certified interval enclosures. The observed checks were:

| Witness | Maximum \(|F(1/y)F(y)-1|\) over three fixed complex probes | Maximum normalized critical-polynomial residual | Minimum computed branch-value separation |
|---|---:|---:|---:|
| Cubic | \(2.94\times10^{-101}\) | \(6.02\times10^{-86}\) | 0.0801558… |
| Quartic | \(1.84\times10^{-101}\) | \(5.48\times10^{-86}\) | 0.250616… |

Full critical points, values, exact discriminants, and tool versions are in `verification_results.json`. Numerical agreement supports the identities; the proofs of monodromy and genus use exact ramification and group arguments.

## 9. General theorem: generic symmetric monodromy and its genus

**Theorem.** For every \(n\ge2\), a nonempty Zariski-open subset of this coefficient-reversal family has degree \(n\), \(2n-2\) simple critical points, distinct critical values, monodromy \(S_n\), and closure genus (1). For \(n\ge3\) its deck group is trivial, and the residual equal-value correspondence is irreducible of degree \(n-1\) over \(\mathbb C(y)\).

**Proof of existence, not a numerical extrapolation.** Work in the odd-function coordinate (2). Start with \(H_1(z)=z\) for the odd-degree induction, and \(H_2(z)=z/(z^2+1)\) for the even-degree induction. The second has two simple critical points \(\pm1\) with distinct values \(\pm1/2\); both 0 and infinity are unramified. The first has no critical points, and both are likewise unramified.

Suppose \(H_d\) has degree \(d\), simple critical points with distinct values, is unramified at 0 and infinity, and has the appropriate asymptotic behavior \(cz\) for odd degree or \(c/z\) for even degree. Choose a finite \(b\ne0\) so that \(\pm b\) are regular, noncritical points and \(H_d(b)\) is finite, nonzero, and different from every existing critical value and its negative. Only finitely many points are forbidden. For small nonzero \(\varepsilon\), set

\[
H_{d+2}(z)=H_d(z)+\varepsilon\frac{z}{z^2-b^2}.
\tag{42}
\]

This is odd. It introduces simple poles at \(\pm b\) and has degree \(d+2\), with no cancellation for sufficiently small nonzero \(\varepsilon\). Existing simple critical points persist with distinct values. Near \(b\), put \(a=H_d'(b)\ne0\). The two new critical points and values have expansions

\[
\begin{aligned}
z&=b\pm\sqrt{\varepsilon/(2a)}+O(\varepsilon),\\
H_{d+2}(z)&=H_d(b)\pm\sqrt{2\varepsilon a}+O(\varepsilon).
\end{aligned}
\tag{43}
\]

The other two occur near \(-b\), with opposite values by oddness. They are simple, mutually distinct, and separated from the old values for sufficiently small nonzero \(\varepsilon\). No new critical point occurs at 0 or infinity: their nonzero local linear coefficients persist. There are now \((2d-2)+4=2(d+2)-2\) simple critical points, so Riemann–Hurwitz leaves no missing ramification. This proves existence in every degree.

To place these witnesses in the user's exact coefficient chart, conjugate back with \(\mathcal C\). The choices can ensure a nonzero numerator constant term; a generic nonzero scaling of \(H\) avoids any remaining normalization obstruction and does not affect simplicity or separation of branch values. The resulting coprime forms satisfy \(Q=P^*\): reciprocity first gives proportional reversed forms, and their common nonzero value at \(y=1\) fixes the reversal sign to +1. Normalize the numerator constant to 1. The parity in (3) ensures the required degree and fixed-point values. Thus the witnesses lie in the stated family.

The failure of coprimeness, simple ramification, or distinct critical values is an algebraic condition, expressed by resultants/discriminants of homogeneous forms. Existence therefore gives a nonempty Zariski-open subset of the irreducible coefficient space.

**Proof of monodromy.** Each simple branch value has one ramification point of index two, so each local monodromy is a transposition. The monodromy is transitive because the source cover is connected. A transitive group generated by transpositions is \(S_n\): make a graph whose edges are the transpositions; transitivity makes it connected, and the edge transpositions of a connected graph generate the full symmetric group.

**Proof of deck and partner assertions.** Deck permutations commute with monodromy on a generic fiber. The centralizer of the natural \(S_n\)-action is trivial for \(n\ge3\). The stabilizer of one sheet is \(S_{n-1}\), transitive on the other \(n-1\) sheets, so the residual correspondence is irreducible. As in the cubic argument, any rational partner would have degree one and would be a deck transformation.

**Proof of genus.** In the Galois closure the group has order \(n!\), there are \(2n-2\) branch values, and all inertia groups have order two. Therefore

\[
2g-2=n!\left[-2+(2n-2)\left(1-\frac12\right)\right]=n!(n-3),
\]

which is (1). This completes the theorem. It concerns generic coefficients, not every point of the reciprocal family. No conjecture is required for these generic conclusions.

## 10. Returning to y = x²

Write \(f_n(x)=F_n(x^2)\). A reduced degree-\(d\) nonconstant \(F_n\) gives a degree-\(2d\) map in \(x\). It satisfies

\[
f_n(-x)=f_n(x),\qquad f_n(1/x)=1/f_n(x).
\tag{44}
\]

The first is a deck symmetry; the second is reciprocal equivariance. Squaring is branched at \(x=0,\infty\). At any point, local degrees multiply:

\[
e_{f_n}(x)=e_{x^2}(x)\,e_{F_n}(x^2).
\tag{45}
\]

On the generic open subset where \(F_n\) is unramified at \(y=0,\infty\), their images \(1/A,A\) are distinct regular values of \(F_n\), and all its critical points are finite and nonzero:

- Each of the \(2n-2\) old branch values has two ramified preimages in the \(x\)-source, both of index two. Its partition is \((2,2,1^{2n-4})\).
- There are exactly two additional branch values, \(1/A,A\), each with partition \((2,1^{2n-2})\), from \(x=0,\infty\), respectively.
- Total ramification is \(2(2n-2)+2=4n-2=2(2n)-2\), as required for a sphere source.

| Lift | Degree | Old branch values | Additional generic branch values | Total branch values | Total ramification |
|---|---:|---:|---:|---:|---:|
| \(F_3(x^2)\) | 6 | 4, partition \((2,2,1,1)\) | 2, partition \((2,1,1,1,1)\) | 6 | 10 |
| \(F_4(x^2)\) | 8 | 6, partition \((2,2,1,1,1,1)\) | 2, partition \((2,1,1,1,1,1,1)\) | 8 | 14 |

If \(A^2=1\), if an endpoint image is already a branch value, or if \(F_n\) is ramified at an endpoint, these generic counts need adjustment. Equation (45) remains exact and gives the adjustment. For \(A=0\), use the endpoint orders from §3.3. The genus formula (1) must **not** be reused for these composite maps: they have shared critical values and an imprimitive degree-\(2n\) covering structure. Their Galois closures are outside this report's stopping point.

For real coefficients and real \(x\), retain the restriction \(y=x^2\ge0\). A positive real zero/pole of the reduced \(F_n\) gives two real points \(\pm\sqrt y\); a negative real one gives imaginary points, and a nonreal one gives nonreal square roots. Reciprocal pairing preserves positivity and negativity. At nonzero \(x\), criticality is exactly \(F_n'(x^2)=0\), by \(f_n'=2xF_n'(x^2)\); \(x=0\) has the special local behavior in (45).

Equations (29) and (39) provide a useful real critical-point test: a real \(\tau>2\) gives two positive reciprocal \(y\)-critical points and hence four real \(x\)-critical points; \(\tau<-2\) gives negative \(y\)-points and no real \(x\); \(-2<\tau<2\) gives nonreal unit-circle \(y\)-points. The endpoints \(\tau=\pm2\) require the multiplicity analysis at reciprocal fixed points.

The visible \(x=\pm1\) points both come from \(y=1\), so generically they have value +1 for **every** \(n\). The odd/even distinction at \(y=-1\) concerns \(x=\pm i\), outside the real plot. Cancellation can flip the continued value at \(x=\pm1\) by (11). Equal complex-cover type does not identify the restricted real plotting domains or remove their holes.

## 11. What survives, what changes, and the bounded next question

Reciprocity, reciprocal zero/pole divisors, endpoint pairing, critical-point pairing, and parity-controlled locks survive throughout the hierarchy. For real coefficients, the unit circle also maps to itself: away from holes, \(\overline{F(y)}=F(\bar y)=F(1/y)=1/F(y)\) when \(|y|=1\), so \(|F(y)|=1\). The coefficient reversal can be expressed exactly as oddness in a Cayley coordinate; this is established rational-map mathematics.

The generic second Möbius symmetry does not survive. Degree two has one other sheet, hence an automatic deck involution. Degree three has an irreducible two-valued correspondence whose normalization is generically elliptic. Degree four has three other sheets and generic closure genus 13. These generic monodromy/genus conclusions are the same as for any simply branched rational map of the respective degree; the reciprocity constraint still allows that generic ramification. Cyclic and other finite deck groups occur on special coefficient loci rather than governing the generic family.

The central distinction for any next work order is therefore the choice of cover:

1. The specified \(F_n\) over its original target, classified generically here.
2. The direct squared-source lift \(F_n(x^2)\), whose extra branch data are recorded here.
3. A further quotient by target reciprocity, analogous to the earlier Belyi tower, which is a different extension and has not been introduced into this report.

The natural bounded follow-up, if requested, is the cubic correspondence (33): its intrinsic elliptic geometry and how its marked reciprocal involution acts. The quartic exceptional census and the closures of the lifted/target-quotiented maps remain separate questions. No physics interpretation follows from this report.

## 12. Files, reproducibility, and integrity

This report and all new evidence are outside the `trioctagon-physics` repository, in `C:/TORMENT/TRIOCTAGON_new/research/three_way_reciprocal_hierarchy_20261005`.

- `verify_hierarchy.py`: the exact identities, exact low-degree witnesses, numerical checks, and read-only repository integrity checks.
- `verification_results.json`: 51 exact checks, 4 numerical checks, explicit critical points/values, and versions.
- `integrity_baseline.json` and `integrity_result.json`: hashes of all 284 files present in the protected reconstruction-paper, kernel, and scientific-UI directories; repository HEAD and status.
- `source_checks.txt`: bounded primary-source verification and scope of the literature comparison.
- `artifact_manifest.json`: checksums of the external deliverables, excluding itself.

Reproduce with Python 3.11.15, SymPy 1.14.0, and mpmath 1.3.0:

```powershell
& 'C:\TORMENT\app-g-dev\env\Scripts\python.exe' '.\verify_hierarchy.py'
```

The algebraic identities have been checked symbolically. The topological/group-theoretic arguments and the all-degree existence proof are written out in the report; they are not claimed to be machine-formalized. No parameter scan, physical-model search, paper edit, kernel/UI edit, commit, or publication was performed.
