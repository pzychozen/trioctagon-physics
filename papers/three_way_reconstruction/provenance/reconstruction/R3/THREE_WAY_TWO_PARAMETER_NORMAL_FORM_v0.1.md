# Three-Way: full two-parameter normal form v0.1

Date: 2026-10-05  
Scope: exact mathematics of the recovered minus-sign family; external report only.

## 1. Conclusion and necessary qualifications

**Yes, for the generic complex \(y\)-cover.** After a coherent choice of square roots, the two-parameter family

\[
F_{A,B}(y)=\frac{Ay^2-By+1}{y^2-By+A}
\]

has the exact normal form

\[
F_{A,B}=\frac{r+k}{r-k},\qquad
r=u+u^{-1},\qquad
\beta=\frac{r^2}{4},
\]

where \(\beta\) is the same fixed degree-four \(V_4\) Belyi quotient for every \(\Delta\ne0\). Its zero/pole fiber is marked at

\[
\boxed{\lambda(A,B)=\frac{(A-1)^2}{(A+1)^2-B^2}.}
\]

For \(\Delta\ne0\), \(A\ne1\), and with the three quotient branch values labeled, **equal \(\lambda\) is necessary and sufficient for equivalence up to a source Möbius transformation**. This remains true if the output coordinate \(F\), including its zero/pole labels, is preserved by the equivalence. The explicit isomorphism is given in Section 5.

Four qualifications are essential:

1. The square roots in the proposed formulas cannot be selected independently. An inconsistent choice replaces the desired function by its reciprocal.
2. At \(A=1\), the reduced function is constant. At \(\Delta=0\), the proposed \(T\) ceases to be a Möbius involution and the function drops degree. These are genuine exceptions.
3. A real plotting domain \(y=x^2\ge0\) remembers source-embedding information that \(\lambda\) forgets.
4. If the additional \(x\)-cover is retained, another invariant survives:
   \[
   \boxed{\nu(A,B)=\frac{(A+1)^2}{\Delta}.}
   \]
   The labeled complex cover tower, with the zero/pole marking, is classified by \((\lambda,\nu)\), under the precise equivalence specified in Section 8. Thus a one-modulus claim for the full \(x\)-construction would be false.

The previous nearest-neighbor identification extends algebraically to the reduced generic complex quotient. It supplies no new physical interpretation of \(F\), \(x\), or the additional cover.

## 2. Conventions, provenance, and square-root correction

The current authority is the user-supplied minus-sign family. This report does not substitute the plus-sign version or reopen physical interpretation. It extends the diagonal calculation in the [large-\(L\) analysis, Sections 13–14](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_large_L_scaling_v0.1/THREE_WAY_LARGE_L_SCALING_ANALYSIS_v0.1.md) and the [known-structure review](C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150/three_way_known_structure_review_v0.1/THREE_WAY_KNOWN_STRUCTURE_AND_PHYSICAL_ANALOGUE_REVIEW_v0.1.md).

Unless a real restriction is stated, parameters and source coordinates are complex. Rational functions are reduced and extended to \(\mathbb P^1\). A canceled point can remain a hole in a literal unreduced plotting formula; its rational extension is explicitly distinguished below.

Set

\[
c=A+1,\qquad p=c-B,\qquad q=c+B,\qquad
\Delta=pq=c^2-B^2.
\]

For \(\Delta\ne0\), choose either root \(d\) of \(d^2=\Delta\), and define

\[
\boxed{a=\frac qd=\frac d p,\qquad
u=a\frac{y-1}{y+1},\qquad
k=\frac{2(A-1)}d.}
\]

Then

\[
a^2=\frac{A+B+1}{A-B+1}.
\]

This is the proposed source scale, but with its sign tied to the choice of \(d\). Equivalently, choose a root \(a\) of \(q/p\), then set \(d=pa\).

Changing branches simultaneously gives
\[
(a,d,k,u,r)\mapsto(-a,-d,-k,-u,-r),
\]
which leaves \(F\) unchanged.

For example, at \((A,B)=(-2,0)\), independent positive square roots would give \(a=1,d=1,k=-6\). At \(y=0\), that proposed normal form gives \(-2\), while the actual function gives \(-1/2\). Taking \(d=1,a=-1,k=-6\), or \(a=1,d=-1,k=6\), restores the identity.

Consequently the candidate formulas are correct **with coherent square roots**, not as a universal prescription using independent principal roots.

## 3. Exact involutions, normal form, and quotient

Let
\[
N=Ay^2-By+1,\qquad D=y^2-By+A.
\]
The reversal identity gives
\[
F_{A,B}(1/y)=\frac1{F_{A,B}(y)}.
\]

The proposed second map is
\[
T(y)=\frac{cy-B}{By-c}.
\]
Its representing matrix satisfies
\[
\begin{pmatrix}c&-B\\B&-c\end{pmatrix}^{\!2}
=\Delta I.
\]
Thus, when \(\Delta\ne0\), \(T\) is a nonidentity Möbius involution. It commutes with \(R(y)=1/y\).

To obtain its conjugate without guessing, put \(w=(y-1)/(y+1)\). Direct substitution yields
\[
w(Ry)=-w(y),\qquad
w(Ty)=\frac{p}{q\,w(y)}.
\]
Since \(a^2=q/p\),
\[
\boxed{R:u\mapsto-u,\qquad T:u\mapsto u^{-1}.}
\]
These generate \(G=\{u,-u,u^{-1},-u^{-1}\}\cong V_4\).

Now
\[
N+D=c(y^2+1)-2By=:H(y),\qquad
N-D=(A-1)(y^2-1),
\]
and
\[
r=u+u^{-1}=\frac{2H(y)}{d(y^2-1)}.
\]
It follows exactly that
\[
\boxed{F_{A,B}(y)=\frac{r+k}{r-k}.}
\]
In particular, \(F(Ty)=F(y)\).

The quotient is
\[
\boxed{
\beta_{A,B}(y)=
\frac{[c(y^2+1)-2By]^2}{\Delta(y^2-1)^2}
=\frac{(u^2+1)^2}{4u^2}.
}
\]

No diagonal restriction remains. The rightmost function itself is parameter-independent.

| Branch value | Points in \(u\) | Stabilizer | Interpretation for nonconstant \(F\) |
|---|---|---|---|
| \(0\) | \(i,-i\) | \(RT\) | \(F=-1\). |
| \(1\) | \(1,-1\) | \(T\) | The critical pair of \(F\). |
| \(\infty\) | \(0,\infty\) | \(R\) | \(y=1,-1\), where \(F=1\). |

The derivative
\[
\beta'(u)=\frac{u^4-1}{2u^3}
\]
and the double poles at \(0,\infty\) show that each branch fiber has partition \((2,2)\). There is no other ramification. The map has degree four and generic fibers are precisely the four-point \(V_4\) orbits.

Hence \(\mathbb C(u)^G=\mathbb C(\beta)\), and this is the same genus-zero Belyi map with passport \((2^2,2^2,2^2)\) identified in the preceding review. Standard covering terminology is as in [Sijsling–Voight, Introduction and Section 6](https://arxiv.org/pdf/1311.2529); the formulas here are proved directly.

## 4. Marked fiber and the parameter-plane stratification

For \(A\ne1\), zeros satisfy \(r=-k\), poles satisfy \(r=k\), and their union is
\[
\boxed{\beta=\lambda=\frac{k^2}{4}
=\frac{(A-1)^2}{\Delta}.}
\]

Two useful exact identities are
\[
\boxed{\beta-\lambda=\frac{4ND}{\Delta(y^2-1)^2}},
\qquad
\boxed{\lambda-1=\frac{B^2-4A}{\Delta}.}
\]

The first proves the marked-fiber statement including multiplicities. The second identifies the repeated-root boundary.

### 4.1 Complete degree-drop and cancellation loci

The resultant is
\[
\operatorname{Res}_y(N,D)=(A-1)^2\Delta.
\]

Equivalently, for \(A\ne1\), a common root must satisfy \(y^2=1\), and its denominator vanishes exactly when \(B=\pm(A+1)\). There is no further cancellation locus.

| Parameter locus | Reduced function and degree in \(y\) | Quotient status |
|---|---|---|
| \(A\ne1,\ \Delta\ne0\) | Degree 2. | Fixed \(V_4\) quotient; moving marked fiber. |
| \(A=1,\ B\ne\pm2\) | \(F\equiv1\), degree 0. | The displayed parameter-derived \(V_4\) action and \(\beta\) still exist; the constant function does not determine them. \(\lambda=0\). |
| \(B=A+1,\ A\ne\pm1\) | \((Ay-1)/(y-A)\), degree 1. | \(T\) collapses to the constant \(1\); no degree-four quotient arises from the proposed involutions. |
| \(B=-(A+1),\ A\ne\pm1\) | \((Ay+1)/(y+A)\), degree 1. | \(T\) collapses to the constant \(-1\). |
| \((A,B)=(1,\pm2)\) | \(F\equiv1\). | Both numerator and denominator of \(\lambda\) vanish; \(\lambda\) is indeterminate here. |
| \((A,B)=(-1,0)\) | \(F\equiv-1\). | The two \(\Delta=0\) lines meet; the displayed \(T\) is undefined. |

The cancellations on the two lines follow from
\[
\begin{aligned}
B=c:&\quad N=(y-1)(Ay-1),\quad D=(y-1)(y-A),\\
B=-c:&\quad N=(y+1)(Ay+1),\quad D=(y+1)(y+A).
\end{aligned}
\]

For \(B=c,\ A\ne\pm1\), the canceled point \(y=1\) has reduced value \(-1\), while \(y=-1\) retains value \(1\). For \(B=-c\), the corresponding statements exchange \(1\) and \(-1\). The generic value-one lock cannot be continued through its canceled point by substituting into the unreduced \(0/0\).

These are all constant cases as well: coefficient comparison in \(N=C D\) gives either \(A=1,C=1\), or \(A=-1,B=0,C=-1\).

### 4.2 Repeated zeros and poles

Let
\[
\chi=B^2-4A.
\]
Both quadratics have discriminant \(\chi\). On \(\Delta\ne0,\ A\ne1\),
\[
\chi=0\quad\Longleftrightarrow\quad\lambda=1.
\]

For \(B\ne0\), this locus has
\[
A=\frac{B^2}{4},\qquad
y_{\rm zero}=\frac2B,\qquad
y_{\rm pole}=\frac B2,
\]
each of multiplicity two. They remain distinct except at the excluded points \((1,\pm2)\).

At \((A,B)=(0,0)\), the same statement is projective:
\[
F(y)=y^{-2},
\]
with a double zero at infinity and a double pole at zero. The quotient remains valid and \(\lambda=1\).

Thus \(\lambda=1\) is a marked regular fiber meeting an existing branch value. The degree-four quotient itself does not degenerate.

### 4.3 The geometric level sets of \(\lambda\)

For a fixed finite \(\ell\),
\[
(A-1)^2=\ell[(A+1)^2-B^2]
\]
or
\[
\boxed{\ell B^2=(\ell-1)A^2+2(\ell+1)A+(\ell-1).}
\]

For \(\ell\ne0\), these are nonsingular projective conics: the determinant of the homogeneous quadratic-form matrix is \(-4\ell^2\). In the affine parameter plane, remove the indeterminate base points \((1,2)\), \((1,-2)\). The special fibers of this rational parameter map are:

- \(\ell=0\): the line \(A=1\), with multiplicity two in the level equation.
- \(\ell=1\): the parabola \(B^2=4A\).
- \(\ell=\infty\): the pair of lines \(B=\pm(A+1)\).

The two base points belong to the closures of every finite level conic. Therefore there is no unique limiting \(\lambda\) at either base point.

Approaching a generic \(\Delta=0\) point with \(A\ne1\) sends the marked value to infinity, but also makes the source normalization singular. This distinction explains why a fixed-\(y\) limit can be a degree-one map while a fixed-\(u\), \(k\to\infty\) limit is constant \(-1\). Those are different limiting coordinate choices.

### 4.4 Other distinguished loci

These do not change the generic \(y\)-quotient, but matter when its coordinate embedding or \(x\)-lift is retained:

| Locus, with \(\Delta\ne0\) | Exact event |
|---|---|
| \(A=0\) | A zero reaches \(y=\infty\), a pole reaches \(y=0\); the marked value equals the extra \(x\)-branch value, \(\lambda=\nu\). |
| \(B=0\) | \(T(y)=-y\); its fixed points are \(0,\infty\). The extra \(x\)-branch value becomes \(\nu=1\). |
| \(A=-1\) | \(T(y)=-1/y\); the \(F=-1\) points are \(0,\infty\). The extra \(x\)-branch value becomes \(\nu=0\). |

Section 8 derives the corresponding cover changes. Apart from the listed loci, there are no further finite-parameter degree drops, zero/pole collisions, or branch-value collisions for the specified maps. Conditional symmetry enhancements after forgetting branch labels are treated separately in Section 5.

## 5. Precise equivalence classes and information forgotten by \(\lambda\)

### 5.1 Labeled complex quotient: \(\lambda\) is complete

The object here is the \(y\)-sphere with its \(R,T\) action, quotient branch values labeled \(0,1,\infty\), and marked zero/pole fiber. Source coordinates may change by a Möbius transformation; the normalized target labels remain fixed.

Take two parameter pairs with \(\Delta,\Delta'\ne0\), \(A,A'\ne1\), and the same \(\lambda\). Choose coherent \(a,k\) and \(a',k'\). Since \(k'^2=k^2\), put
\[
\eta=\frac{k'}k\in\{1,-1\}.
\]
Define
\[
\boxed{
M(y)=
\frac{a'(y+1)+\eta a(y-1)}
{a'(y+1)-\eta a(y-1)}.
}
\]
Then \(u'(M(y))=\eta u(y)\), so
\[
\boxed{
\beta_{A',B'}(M(y))=\beta_{A,B}(y),\qquad
F_{A',B'}(M(y))=F_{A,B}(y).
}
\]
The same map conjugates the corresponding \(R\) and \(T\).

This proves sufficiency, even with the \(F\)-coordinate and its zero/pole labels preserved. Necessity follows because a Möbius map fixing the three labeled target branch values is the identity, so it must preserve the marked value.

For the usual regular marked-fiber description, also exclude \(\lambda=1\). The equivalence proof itself remains valid at \(\lambda=1\), with multiplicities retained.

For a regular marked fiber, the ordered target tuple \((\infty,0,1,\lambda)\) has cross-ratio \(\lambda\). Thus it is exactly a point of \(M_{0,4}\); the fixed three-branch cover contributes no further continuous modulus.

The nonconstant maps \(F\) also have critical values
\[
v_+=\frac{2+k}{2-k},\qquad v_-=\frac1{v_+}.
\]
Their unordered pair depends only on \(\lambda\), since
\[
v_++v_-=\frac{2(1+\lambda)}{1-\lambda}\qquad(\lambda\ne1).
\]
At \(\lambda=1\), the critical values are \(0,\infty\). This gives an independent check that the fixed-output degree-two covers have the same modulus.

### 5.2 What the sign and labels mean

\(\lambda\) does not reconstruct the sign of \(k\) in a fixed \(u,r\) chart. It also does not specify which of the two \(r\)-levels above \(\lambda\) is called zero or pole.

However, **that sign is not an extra intrinsic modulus under the stated equivalence**. The simultaneous change \(u\mapsto-u,\ k\mapsto-k\) preserves the function and carries zeros to zeros between the two normal forms. Within one fixed normal form, \(u\mapsto-u\) alone exchanges zeros and poles and sends \(F\) to \(1/F\).

Thus:

- A fixed source chart or an oriented choice of \(r\) needs signed \(k\).
- An abstract labeled cover up to source Möbius isomorphism needs only \(\lambda\).
- Ordering individual roots or selecting one sheet adds discrete marking data.
- Keeping \(y=0,\infty\), \(y\ge0\), or the actual \(x\)-cover adds source-embedding data.

### 5.3 Explicit recovery of the discarded coordinate parameter

The pair \((a,k)\), with \(a\ne0\), reconstructs the original finite coefficients:
\[
\boxed{
A=\frac{a+a^{-1}+k}{a+a^{-1}-k},\qquad
B=\frac{2(a-a^{-1})}{a+a^{-1}-k}.
}
\]
The denominator must be nonzero. The simultaneous replacement \((a,k)\mapsto(-a,-k)\) leaves \(A,B\) unchanged.

These equations exhibit the apparent two parameters as a signed marked-level coordinate \(k\) and a source-embedding coordinate \(a\). At fixed \(\lambda=k^2/4\), changing \(a\) changes the original coordinates without changing the labeled reduced quotient geometry.

### 5.4 If quotient branch labels are forgotten

Here the retained object is only the cover with one entire marked fiber: the \(F\)-coordinate and the zero/pole partition within that fiber are also forgotten. For this coarser object the classification is:
\[
\lambda\sim
1-\lambda\sim\frac1\lambda\sim\frac1{1-\lambda}
\sim\frac{\lambda}{\lambda-1}\sim\frac{\lambda-1}{\lambda}.
\]

This is not an assumed analogy with cross-ratios. The transformations
\[
u\mapsto iu,\qquad u\mapsto\frac{u+1}{u-1}
\]
induce respectively
\[
\beta\mapsto1-\beta,\qquad
\beta\mapsto\frac{\beta}{\beta-1},
\]
which generate all six permutations of the three branch labels.

For regular marked fibers, forgetting labels introduces enhanced automorphism loci at
\[
\lambda\in\{-1,\tfrac12,2\}
\quad\text{or}\quad
\lambda^2-\lambda+1=0.
\]
The stabilizer of the marked value in the six-element branch-permutation group has order two or three respectively, giving source-target automorphism groups of order eight or twelve instead of four when target branch permutations are allowed. The deck group over the fixed target coordinate remains \(V_4\). These are symmetries of the unlabeled decoration, not new ramification or cancellation loci. With the Three-Way branch roles labeled, they introduce no missing modulus.

## 6. Zeros, poles, locks, and stationary points

Away from cancellation, for \(A\ne0\),
\[
y_{z,\pm}=\frac{B\pm\sqrt{\chi}}{2A},\qquad
y_{p,\pm}=\frac{B\pm\sqrt{\chi}}2,\qquad
\chi=B^2-4A.
\]
The zero and pole sets are exchanged by \(y\mapsto1/y\).

For \(A=0,\ B\ne0\), the projective lists are
\[
\text{zeros: }\infty,\ 1/B;\qquad
\text{poles: }0,\ B.
\]
At \(A=B=0\), each corresponding origin/infinity root is double.

For \(\Delta\ne0,\ A\ne1\):

\[
F=1\iff y=\pm1,
\]
so the original real \(x=\pm1\) lock is exactly at value \(1\).

The value \(-1\) satisfies
\[
c(y^2+1)-2By=0.
\]
If \(c\ne0\), its two roots are
\[
y_{-,\pm}=\frac{B\pm\sqrt{-\Delta}}c.
\]
If \(c=0\), they are \(0,\infty\).

Finally,
\[
\boxed{
F'(y)=
-\frac{(A-1)[By^2-2cy+B]}{D(y)^2}.
}
\]
The projective critical pair is therefore
\[
By^2-2cy+B=0.
\]
For \(B\ne0\), it is \((c\pm\sqrt\Delta)/B\); for \(B=0\), it is \(0,\infty\). At \(\lambda=1\), the pair consists of the double zero and double pole, so “stationary graph point” must be replaced by local-degree-two critical point at the pole.

## 7. Real parameter plane versus real plotting geometry

Assume \(A,B\in\mathbb R\), \(\Delta\ne0\), \(A\ne1\), unless stated otherwise.

### 7.1 Two real forms of the fixed complex quotient

If \(\Delta>0\), the source scale \(a\) and \(k\) can both be chosen real. The real \(y\)-line maps to the real \(u\)-line, and
\[
\beta(\mathbb P^1(\mathbb R))=[1,\infty].
\]
Here the projective endpoint infinity is included. The \(T\)-fixed pair is real; the \(F=-1\) pair is nonreal.

If \(\Delta<0\), \(a\) and \(k\) are purely imaginary. Writing \(u=iv\) with real \(v\),
\[
r=i(v-v^{-1}),\qquad
\beta=-\frac{(v-v^{-1})^2}{4}\le0.
\]
Thus the real quotient image is the arc \((-\infty,0]\) together with its projective infinity. The \(T\)-fixed pair is nonreal; the \(F=-1\) pair is real.

These are different real structures on the same complex Belyi cover. For nonconstant real families, their distinction is already visible in the sign of \(\lambda\).

| Real parameter regime | Marked level | Zero/pole fiber on the real \(y\)-line |
|---|---|---|
| \(\Delta>0,\ 0<\lambda<1\) | Below the real quotient interval | Nonreal conjugate roots, since \(\chi<0\). |
| \(\Delta>0,\ \lambda=1\) | Meets the branch value \(1\) | Real double zero and double pole, projectively interpreted. |
| \(\Delta>0,\ \lambda>1\) | Regular point in the real quotient interval | Four distinct real \(y\)-points. |
| \(\Delta<0\) | Necessarily \(\lambda<0\) | Four distinct real \(y\)-points, since \(\chi=(A-1)^2-\Delta>0\). |

**In particular, \(\lambda<1\) is insufficient to infer nonreal zeros and poles.** Negative \(\lambda\) belongs to the other real form and gives real \(y\)-roots.

At \(A=1\), \(\lambda=0\) and \(F\equiv1\). If one retains the parameter-derived action despite the cancellation, its two real forms still depend on the sign of \(\Delta\); \(\lambda=0\) alone does not distinguish them.

For nonconstant real parameter pairs with equal \(\lambda\), the source isomorphism in Section 5 can be chosen real: \(a/a'\) is real, whether the two scales are both real or both imaginary. This equivalence need not preserve \(y\ge0\).

### 7.2 Which roots occur on real \(x\)?

Real \(x\) requires \(y\ge0\), a stricter condition than real \(y\).

| Coefficients, after excluding cancellation | Real-\(x\) zero/pole behavior |
|---|---|
| \(A>0,\ \chi<0\) | No real zeros or poles. |
| \(A>0,\ \chi>0,\ B>0\) | Two positive \(y\)-zeros and two positive \(y\)-poles: four simple real \(x\)-zeros and four simple real \(x\)-poles. |
| \(A>0,\ \chi>0,\ B<0\) | All these \(y\)-roots are negative: the \(x\)-roots are purely imaginary. |
| \(A>0,\ \chi=0,\ B>0\) | Two real \(x\)-zeros, each double, and two real \(x\)-poles, each double. |
| \(A>0,\ \chi=0,\ B<0\) | The double roots occur at purely imaginary \(x\). |
| \(A<0\) | Each \(y\)-quadratic has one positive and one negative root: two simple real \(x\)-zeros and two simple real \(x\)-poles, plus imaginary pairs. |
| \(A=0,\ B>0\) | Simple zeros at \(x=\pm1/\sqrt B\), simple poles at \(x=\pm\sqrt B\), a double pole at \(0\), and a double zero at infinity. |
| \(A=0,\ B<0\) | The finite nonzero roots are imaginary; the double pole at \(0\) and double zero at infinity remain. |
| \(A=B=0\) | \(f(x)=x^{-4}\): pole order four at \(0\), zero order four at infinity. |

For \(\Delta<0,\ c\ne0\), both \(F=-1\) points are positive precisely when \(B/c>0\), and negative when \(B/c<0\). At \(A=-1,\ B\ne0\), they are \(y=0,\infty\).

For \(\Delta>0,\ B\ne0\), both critical \(y\)-points are positive precisely when \(c/B>0\). When \(c/B<0\), the critical points exist on the real \(y\)-line but not at nonzero real \(x\). When \(\Delta<0\), there are no real critical \(y\)-points. The extra critical behavior at \(x=0,\infty\) from squaring is separate.

A direct illustration of the lost plotting data is
\[
F_{A,-B}(y)=F_{A,B}(-y).
\]
The two parameter pairs have the same \(\lambda\), but \(y\mapsto-y\) exchanges the positive and negative plotting halves. In \(x\), the corresponding complex coordinate change is \(x\mapsto ix\).

## 8. The additional \(x\)-cover and its missing invariant

The original construction has the tower
\[
\mathbb P^1_x\xrightarrow[\deg2]{y=x^2}
\mathbb P^1_y\xrightarrow[\deg4]{\beta_{A,B}}
\mathbb P^1_\beta.
\]

The first map branches at \(y=0,\infty\), which have \(u=-a,a\). Their common quotient image is
\[
\boxed{
\nu=\beta(0)=\beta(\infty)
=\frac{(A+1)^2}{\Delta}
=\frac{(a+a^{-1})^2}{4}.
}
\]
Moreover,
\[
\boxed{\nu-\lambda=\frac{4A}{\Delta},\qquad
\nu-1=\frac{B^2}{\Delta}.}
\]

For \(B\ne0,\ A\ne-1,\ \Delta\ne0\), the degree-eight composite has:

| Branch value | Ramification partition |
|---|---|
| \(0\) | \((2,2,2,2)\) |
| \(1\) | \((2,2,2,2)\) |
| \(\infty\) | \((2,2,2,2)\) |
| \(\nu\) | \((2,2,1,1,1,1)\) |

It is generically not Galois and not Belyi under Möbius coordinate changes. The mixed partition over \(\nu\) excludes a quotient by eight global deck transformations.

The proposed lift of \(T\) would require
\[
g(x)^2=\frac{cx^2-B}{Bx^2-c}.
\]
When \(Bc\ne0\), its zeros and poles are distinct and simple, so no rational square root exists.

There are exactly two nondegenerate exceptional lift loci:

- **\(B=0,\ A\ne-1\):** \(T(y)=-y\) lifts by \(x\mapsto ix\). Here \(\nu=1\), and the composite branch partitions over \(0,1,\infty\) are \((2^4),(4,4),(2^4)\).
- **\(A=-1,\ B\ne0\):** \(T(y)=-1/y\) lifts by \(x\mapsto i/x\). Here \(\nu=0\), and the partitions are \((4,4),(2^4),(2^4)\).

On both loci the degree-eight composite is a Galois Belyi cover with deck group the dihedral group of order eight. It is generated by the lifted transformations and parity; its quotient by \(x\mapsto-x\) recovers the \(y\)-level \(V_4\).

Off these loci, the full composite still has the different deck group
\[
H=\{x,-x,x^{-1},-x^{-1}\}\cong V_4.
\]
Writing \(v=x^2+x^{-2}\),
\[
\widehat\beta_{A,B}(x)=
\frac{[cv-2B]^2}{\Delta(v^2-4)}.
\]
A generic degree-eight fiber consists of two \(H\)-orbits. Its deck group has exactly order four: it contains \(H\), its order divides eight, and the mixed ramification excludes order eight.

### 8.1 Completeness of \((\lambda,\nu)\) for the labeled complex tower

Retain the tower, the branch labels \(0,1,\infty\), and the marked \(F\)-divisor. Require an isomorphism to commute with the degree-two covering maps, while allowing source Möbius coordinates on both spheres.

For \(\Delta\ne0,\ A\ne1\), equal \((\lambda,\nu)\) is necessary and sufficient.

Necessity follows because \(\lambda\) is the marked value and \(\nu\) is the image of the branching of the additional double cover.

For sufficiency, normalize both covers as before. Equal \(\nu\) implies
\[
a'\in\{a,-a,a^{-1},-a^{-1}\}.
\]
The appropriate map \(u\mapsto\eta u\) or \(u\mapsto\eta/u\), where \(\eta=k'/k\), preserves the required normal form and carries the unordered branch pair \(\{-a,a\}\) to \(\{-a',a'\}\). The resulting source map lifts to the double covers.

In coefficients, for \(A\ne0\), the complete finite orbit is
\[
\boxed{
(A,B),\quad(A,-B),\quad
(A^{-1},B/A),\quad(A^{-1},-B/A),
}
\]
with duplicates on special loci. The corresponding \(y\)-changes are \(y,-y,1/y,-1/y\); their complex \(x\)-lifts are among \(\pm x,\pm ix,\pm1/x,\pm i/x\). For \(A=0\), only the finite pairs \((0,\pm B)\) remain.

Indeed \(\nu/\lambda=((A+1)/(A-1))^2\) determines \(A\) up to inversion, and the remaining equation determines \(B\) up to the indicated signs.

This also proves that \(\lambda\) alone is insufficient for the full tower. For example,
\[
(A,B)=(9,9)
\quad\text{and}\quad
(A',B')=(2,\sqrt{557}/8)
\]
both have \(\lambda=64/19\), but have respectively
\[
\nu=100/19,\qquad \nu'=576/19.
\]
Their reduced marked \(y\)-quotients are isomorphic; their labeled \(x\)-cover towers are not.

For real \(x\)-cover isomorphisms commuting with the tower, \(y\mapsto-y\) and \(y\mapsto-1/y\) do not have real rational lifts. Generically only the coefficient identifications \((A,B)\) and \((A^{-1},B/A)\) survive over the real \(x\)-sphere. Special-locus duplicates are interpreted accordingly. Requiring preservation of the actual plotting coordinate is stricter still.

## 9. The four specified examples

Let \(\phi=(1+\sqrt5)/2\). All four examples have \(A>1\), \(c>0\), and \(\Delta>0\). Thus \(d=\sqrt\Delta>0\) and the positive source scale \(a=\sqrt{q/p}\) are coherent.

| Pair | \(\Delta\) | Source scale \(a\) | \(k\) | \(\lambda\) |
|---|---|---|---|---|
| \((9,9)\) | \(19\) | \(\sqrt{19}\) | \(16/\sqrt{19}\) | \(64/19\) |
| \((9,1)\) | \(99\) | \(\sqrt{11}/3\) | \(16/(3\sqrt{11})\) | \(64/99\) |
| \((\pi,e)\) | \((\pi+1)^2-e^2\) | \(\sqrt{(\pi+e+1)/(\pi-e+1)}\) | \(2(\pi-1)/\sqrt{(\pi+1)^2-e^2}\) | \((\pi-1)^2/[(\pi+1)^2-e^2]\) |
| \((\phi,1-\phi)\) | \(4\phi\) | \(\phi^{-1/2}\) | \(\phi^{-3/2}\) | \(1/(4\phi^3)=(\sqrt5-2)/4\) |

Numerical values:

| Pair | \(a\) | \(k\) | \(\lambda\) | \(\chi=B^2-4A\) |
|---|---:|---:|---:|---:|
| \((9,9)\) | 4.358898943541 | 3.670651741929 | 3.368421052632 | 45 |
| \((9,1)\) | 1.105541596785 | 1.608060504415 | 0.646464646465 | -35 |
| \((\pi,e)\) | 2.195372442666 | 1.370752047260 | 0.469740293767 | -5.177314515429 |
| \((\phi,1-\phi)\) | 0.786151377757 | 0.485868271757 | 0.059016994375 | -6.090169943749 |

**\((9,9)\).** Its marked value lies inside the real quotient range, \(\lambda>1\). Its two zeros and two poles in \(y\) are real and positive:
\[
y_z=\frac{3\pm\sqrt5}{6},\qquad
y_p=\frac{9\pm3\sqrt5}{2}.
\]
They yield four real \(x\)-zeros and four real \(x\)-poles. The marked fiber is regular; no roots are repeated.

**\((9,1)\).** Its marked value satisfies \(0<\lambda<1\), outside the real \(y\)-quotient range. Both zero and pole pairs in \(y\) are nonreal conjugate pairs; there are no real \(x\)-zeros or poles.

**\((\pi,e)\).** It occupies the same qualitative regime as \((9,1)\), though at a different marked value. The inequality \(e^2<4\pi\) proves \(\lambda<1\); this is not an inference from rounded numerical values.

**\((\phi,1-\phi)\).** Again \(0<\lambda<1\), so the zeros and poles are nonreal. Its negative \(B\) adds an embedding difference: \(a<1\), so the real plotting interval \(y\ge0\) maps to \(u\in[-a,a]\), which excludes \(u=\pm1\). Its real-\(y\) critical pair lies at negative \(y\); there are no nonzero real-\(x\) shoulders. For \(y\ge0\), the function increases from \(1/\phi\) to \(\phi\), crossing \(1\) at \(y=1\).

The other three examples have \(a>1\) and \(B>0\), so both critical points occur at positive \(y\). For all four examples, \(\Delta>0\) means the \(F=-1\) fiber is nonreal in \(y\), and hence absent from real \(x\).

Their extra \(x\)-branch values are, respectively,
\[
\nu=\frac{100}{19},\quad
\frac{100}{99},\quad
\frac{(\pi+1)^2}{(\pi+1)^2-e^2},\quad
1+\frac{\sqrt5-2}{4}.
\]

The differences are therefore explained by marked-fiber position and source embedding. No special physical role of the named numerical constants is inferred.

## 10. What extends from the nearest-neighbor identification

The already-fixed chain has the complexified relation
\[
\epsilon=u+u^{-1},\qquad
E=E_0-t\epsilon.
\]
Consequently every generic member of the present family gives exactly
\[
\boxed{\beta=\frac{\epsilon^2}{4},\qquad
\lambda=\frac{k^2}{4},\qquad
F=\frac{\epsilon+k}{\epsilon-k}.}
\]

This is the same algebraic spectral quotient, with a selected signed spectral level \(k\). It changes neither the Hamiltonian nor its dispersion; the standard chain relation is [Tong, Eq. 2.5](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate2.pdf).

The real-domain qualification now becomes more important:

- For real parameters with \(\Delta>0\), \(k\) is real. A marked level with \(0<\lambda<1\) lies inside the real Bloch band; \(\lambda=1\) is a band edge; \(\lambda>1\) lies outside the band. Original real \(y\) gives real \(u\), generally an evanescent spectral continuation rather than a propagating state.
- For real parameters with \(\Delta<0\), \(k\) is imaginary. The marked level is a complex spectral value, not a real-energy state. Original real \(y\) gives imaginary \(u\) and generally imaginary \(\epsilon\), rather than real-energy evanescent multipliers.
- Propagating real-energy states still require \(|u|=1\). The parameter-dependent plotting contour must not be identified with that circle.

The preceding physical-dictionary test found no independently prescribed observable equal to the nonconstant \(F\), and no independent physical role for the extra \(x\)-cover. Neither conclusion changes under this generalization. The identity above remains a reduced complex spectral-geometry identification.

## 11. Verification and final mathematical statement

The proofs in this report establish the classification. Independent checks comprised:

- **29 exact symbolic identities**, all passing: involutions and commutation, reciprocity and equal-value pairing, the coherent normal form, quotient identity, resultant, derivative, discriminants, cancellation formulas, embedding reconstruction, extra branch values, coefficient equivalences, and branch-permutation transformations.
- **48 fixed-case normal-form comparisons at 100 decimal digits**, using twelve parameter pairs and four complex source points each. The largest normalized discrepancy was \(2.701\times10^{-101}\).
- **80-digit evaluation** of the four historical examples, rounded only for the displayed table.

The fixed numerical cases included both signs of \(\Delta\), negative \(A\), \(A=0\), \(A=-1\), the constant stratum, and points close to cancellation. They are checks of the identities, not a numerical basis for the exceptional-locus classification.

The exact answer to the central question is:

\[
\boxed{
\begin{aligned}
\text{Labeled generic complex }y\text{-quotient:}&\quad \lambda\text{ is complete}.\\
\text{Original coordinate realization:}&\quad \lambda+\text{embedding data}.\\
\text{Labeled complex }x\text{-cover tower:}&\quad (\lambda,\nu)\text{ is complete}.\\
\text{Real }x\text{-plot:}&\quad \text{also retain the real domain and its embedding}.
\end{aligned}}
\]

This is a reduction of the generic two-parameter family, with explicitly identified exceptions. It is not a reduction of every degenerate map or every coordinate-dependent plot to one number.

No repository files, existing reports, Hamiltonians, kernels, UI code, or commits were changed.
