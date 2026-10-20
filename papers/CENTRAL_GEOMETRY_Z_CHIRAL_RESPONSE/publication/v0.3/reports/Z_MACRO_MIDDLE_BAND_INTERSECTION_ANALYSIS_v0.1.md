# Macro-Z and the Crystal’s Middle Band — Exact Intersection Analysis v0.1

19 October 2026. Source reads and written algebra only.

**Result.** GPT’s proposed crossing argument is correct for the actual twelve-triangle band, with stronger quantifiers than “somewhere above and below.” Every fixed horizontal azimuth has exactly one upper and one lower cone contact. These contacts form two continuous closed curves, each assembled from twelve finite-face conic arcs. Existence follows from the continuous star-shaped sections; uniqueness needs the additional face-plane argument proved below.

The frozen signed macro curve visits those cone contacts only when its amplitude and angular alignment agree with them. For each height side there is an exact, implicitly defined onset amplitude: contact occurs at the onset and at every larger effective amplitude. The default twelve-sector clock has a different answer: on each side it can hit at only two specified effective amplitudes, possibly coincident. Consequently continuous contact can persist while every sampled point misses the band.

These are conditional comparisons under the declared placement, not a recovered attachment of Z to the crystal. The geometry, harmonic, lock and clock definitions are unchanged. The previous exclusion of all refined fan triangles still holds; this report concerns the middle band only.

| Object being compared with the band | Exact conclusion |
|---|---|
| Entire macro cone | One contact on every azimuth half-ray on each height side, for every allowed member and either hand |
| Frozen positive-amplitude macro curve | On side \(\sigma\), contact iff \(b\ge B_\sigma(u,\mathrm{hand},\ell+\psi)\), with \(a/2<B_\sigma<h\) |
| Full default twelve-sector frozen sample set | On side \(\sigma\), contact iff \(b\) belongs to the set of at most two amplitudes in (18) |

## 1. Source basis and fixed definitions

The consulted checkout is `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, the revision recorded by [R0]. The read-only tracked-status inspection reported no tracked changes. Existing untracked material was left alone; no full-tree audit was undertaken. Code was read as text, not imported or executed.

There is one relevant scope difference between records: the candidate JSON’s original parameter domain is \(0<\tau\le h\), whereas the subsequent family analysis explicitly includes the two zero limits and the signed reflection convention. Zero below means those existing face-complex limits, not a replacement common mesh. The candidate’s ring and face rules remain declared research assumptions, not host-forced or kernel-adopted geometry. [CJ:18–21,218–231; FA:29–43,86–93; Z0:77–103]

Use the inherited physical width-one coordinates

\[
s=\sqrt2-1,\quad d=1-\frac{\sqrt2}{2},\quad r=\frac{\sqrt3}{6},
\quad a=\frac d2,\quad h=\frac s2,\quad O=(0,r,0),
\qquad h=\sqrt2\,a.
\]

Write \(v=X-O=(x,y,w)\), \(u=|\tau|\in[0,h]\), and \(\xi=u/r\). Thus

\[
0\le\xi\le\sqrt3(\sqrt2-1),\qquad
\xi^2\le9-6\sqrt2<1.
\]

For PLUS, with indices modulo six, set

\[
\alpha_i=-\frac\pi2+\frac{i\pi}3,\qquad
e_i=(\cos\alpha_i,\sin\alpha_i),\qquad
\mathsf A_u=I-\xi J,\quad J(x,y)=(-y,x),
\]
\[
T_i=(ae_i,h),\qquad B_i=(a\mathsf A_u e_i,-h),
\qquad
F_i^T=[T_i,T_{i+1},B_{i+2}],\quad
F_i^B=[T_i,B_{i+2},B_{i+1}]. \tag{1}
\]

These are exactly the twelve band triangles from `canonical_points` and `candidate_faces`; the superscripts distinguish the top-two-vertex and bottom-two-vertex triangles, not cap fans. MINUS is the image of this entire face complex under \(S(x,y,w)=(-x,y,w)\). In common signed vertex labels its face list is correspondingly permuted. Substituting negative \(\tau\) into (1) while retaining PLUS connectivity is not that reflection. Both zero face complexes remain distinct. [VC:44–79; SI:5–30,68–99; Z0:46–63]

The only placement used is

\[
\Phi(M)=O+\mu R_z(\psi)M,\qquad \mu>0.
\]

Freeze the staged amplitude at a supplied state and clock time \(t_c\):

\[
A=\lambda_{vp}\rho e^{-\gamma t_c}>0,\qquad b=\mu A,
\]
\[
v_b(\theta)=b\cos3(\theta-\ell)
\bigl(\cos(\theta+\psi),\sin(\theta+\psi),1\bigr). \tag{2}
\]

The effective amplitude \(b\) includes the comparison scale \(\mu\); it is not a new native parameter. The source defaults remain \(\lambda_{vp}=0.618\), \(\gamma=0.577\), \(\ell=0.244\), \(N=12\), and clock step one. No state, time, member, hand or physical calibration is selected by the results. [Z:46–82,90–150; E:52–76,112–150]

## 2. Verifying GPT’s crossing argument

### The radial section is well defined and continuous

At height \(w=h(1-2\eta)\), \(0\le\eta\le1\), the actual section has vertices

\[
S_i(\eta)=(1-\eta)ae_i+\eta a\mathsf A_u e_{i+1},\qquad
D_i(\eta)=(1-\eta)ae_i+\eta a\mathsf A_u e_{i+2}, \tag{3}
\]

with segments \(S_iD_i\) and \(D_iS_{i+1}\). These are intersections with the triangles in (1), not corresponding-index interpolation. Put \(\beta=a\sqrt{1+\xi^2}\) and \(\delta=\arctan\xi\). The source identities give

\[
\det(S_i,D_i)=\frac{\sqrt3}{2}(\eta\beta)^2+
\eta(1-\eta)a\beta\sin\delta>0,
\]
\[
\det(D_i,S_{i+1})=\frac{\sqrt3}{2}((1-\eta)a)^2+
\eta(1-\eta)a\beta\sin\delta>0 \qquad(0<\eta<1). \tag{4}
\]

The two successive angular increments are each in \((0,\pi)\). Their sum is congruent to \(\pi/3\), since \(S_{i+1}=R_{\pi/3}S_i\), and is less than \(2\pi\); it is therefore exactly \(\pi/3\). Each segment crosses each intermediate azimuth once, so the polygon winds once and is strictly star-shaped about the axis. At \(\eta=0,1\), alternate segments collapse and the remaining segments give the ordinary upper or lower hexagon. Those endpoint sections also have a unique radial boundary point. [SI:68–119]

Define \(R(w,\varphi)>0\) by that point:

\[
(R(w,\varphi)\cos\varphi,R(w,\varphi)\sin\varphi,w)\in\mathcal B.
\]

This function is continuous, including at triangle transitions and ring levels. To see this without assuming a smooth surface, take any convergent sequence of heights and azimuths. Its section points lie in the compact finite union of triangles. Any subsequential limit lies on the limiting section and ray; its radius stays positive by the inherited clearance \(R\ge a/2\). Uniqueness of the limiting radial section point forces all such limits to agree. This also handles the merging section vertices at either endpoint. [R0:229–233]

At the middle plane,

\[
R(0,\varphi)\ge a/2>0.
\]

At the rings, every point is a convex combination of vertices of the respective regular hexagon, hence

\[
R(h,\varphi)\le a<h,
\qquad
R(-h,\varphi)\le a\sqrt{1+\xi^2}<h, \tag{5}
\]

where the last squared ratio is at most \(5-3\sqrt2<1\).

For **every** \(\varphi\) and each \(\sigma\in\{+1,-1\}\), the continuous function \(R(\sigma t,\varphi)-t\) is positive at \(t=0\) and negative at \(t=h\). It has a zero in \((0,h)\). Thus GPT’s proposed argument proves contact on every half-ray \(t(\cos\varphi,\sin\varphi,\sigma)\), not merely an unspecified contact on each side. It does not, by itself, prove uniqueness.

### The actual face planes additionally prove uniqueness

Here is the needed extra calculation. Let \(k_0=\sqrt3/2\). For each face write its plane as
\(n_{F,h}\cdot(x,y)+n_{F,w}w=c_F\), using the following unnormalized normals:

| Face | \(n_{F,h}\) | \(n_{F,w}\) | \(c_F\) |
|---|---|---|---|
| \(F_i^T\) | \(R_{\alpha_i}(\sqrt3/2,1/2)\) | \(a(\xi-k_0)/(2h)\) | \(a(k_0+\xi)/2\) |
| \(F_i^B\) | \(R_{\alpha_i}(\xi,1)\) | \(a[k_0(1+\xi^2)-\xi]/(2h)\) | \(a[k_0(1+\xi^2)+\xi]/2\) |

In the local frame of \(T_i\), the first horizontal normal takes the values \(ak_0,ak_0,a\xi\) at \(T_i,T_{i+1},B_{i+2}\). The second takes \(a\xi,ak_0(1+\xi^2),ak_0(1+\xi^2)\) at \(T_i,B_{i+2},B_{i+1}\). Equating the top and bottom plane values gives the table directly. In particular, **every \(c_F>0\)**, including at zero.

On an interior-height section of either triangle, the horizontal-normal value is strictly positive: it interpolates between the displayed endpoint values, at least one of which is positive on each end-to-end pair. Consequently, wherever a fixed-azimuth radial section lies in that face,

\[
d_F(\varphi):=n_{F,h}\cdot(\cos\varphi,\sin\varphi)>0,
\quad
\frac{R(\sigma t,\varphi)}{t}
=\frac{c_F}{d_F(\varphi)t}-\frac{\sigma n_{F,w}}{d_F(\varphi)}. \tag{6}
\]

Its derivative with respect to \(t\) is \(-c_F/[d_F(\varphi)t^2]<0\). The radial section is piecewise affine in height with finitely many face pieces; at their boundaries it is continuous. Thus \(R(\sigma t,\varphi)/t\) is strictly decreasing throughout \(0<t<h\). Its crossing of one is unique.

Denote that positive height/radius by \(T_\sigma(\varphi;u,\mathrm{hand})\), suppressing the last two arguments below. Uniqueness and compactness, or the same subsequence argument used above, show that \(T_\sigma\) is continuous in \(\varphi\), and continuous in \(u\) within each hand’s closed interval. Therefore

\[
\mathcal B\cap\{x^2+y^2=w^2\}
=\bigcup_{\sigma=\pm1}
\left\{T_\sigma(\varphi)(\cos\varphi,\sin\varphi,\sigma):
\varphi\in\mathbb R/(2\pi\mathbb Z)\right\}. \tag{7}
\]

These are two disjoint simple closed curves. The band has \(C_6\) symmetry, so \(T_\sigma(\varphi+\pi/3)=T_\sigma(\varphi)\). This statement does not assign \(C_6\) symmetry to the complete crystal with its fans.

All arguments include \(u=h\) because (5) remains strict, and include each distinct \(u=0\) face limit. Applying \(S\) proves the same conclusions for MINUS.

## 3. Exact finite-face pieces and their shared edges

For a face from the table, define

\[
D_{F,\sigma}(\varphi)=n_{F,h}\cdot(\cos\varphi,\sin\varphi)+\sigma n_{F,w}.
\]

Its cone piece is exactly the following set, with the inequalities retained:

\[
t=\frac{c_F}{D_{F,\sigma}(\varphi)},\qquad
D_{F,\sigma}(\varphi)>0,\quad 0<t<h,
\quad v=t(\cos\varphi,\sin\varphi,\sigma)\in F. \tag{8}
\]

For explicit finite-triangle membership, take ordered vertices \(p_0,p_1,p_2\), put \(U=p_1-p_0\), \(V=p_2-p_0\), \(Y=v-p_0\), and

\[
G=(U\cdot U)(V\cdot V)-(U\cdot V)^2>0,
\]
\[
\lambda_1=\frac{(Y\cdot U)(V\cdot V)-(Y\cdot V)(U\cdot V)}G,
\quad
\lambda_2=\frac{(Y\cdot V)(U\cdot U)-(Y\cdot U)(U\cdot V)}G,
\quad \lambda_0=1-\lambda_1-\lambda_2. \tag{9}
\]

Together with the face-plane equality, membership is equivalent to \(\lambda_0,\lambda_1,\lambda_2\ge0\). Nondegeneracy follows also from the nonzero horizontal ring edge and the third vertex at the opposite height. Equations (8)–(9), for the twelve faces and both signs, are a reusable exact description with no infinite-plane substitutions.

The gluing points have a particularly simple algebraic specification. Every cross-ring edge is

\[
E_i^{(m)}(\eta)=\bigl(a[(1-\eta)e_i+\eta\mathsf A_u e_{i+m}],
h(1-2\eta)\bigr),\qquad m=1,2.
\]

Here \(m=1\) gives the six cross-struts and \(m=2\) the six declared tessellation diagonals. On this edge,

\[
\frac{x^2+y^2-w^2}{a^2}
=-1+K_m\eta-(K_m-\xi^2)\eta^2,
\quad K_1=7+\sqrt3\xi,\quad K_2=5+\sqrt3\xi. \tag{10}
\]

This quadratic is negative at \(0,1\) and positive at \(1/2\). It has exactly two simple roots

\[
\eta_{m,\pm}=\frac{K_m\pm\sqrt{K_m^2-4(K_m-\xi^2)}}{2(K_m-\xi^2)},
\qquad 0<\eta_{m,-}<\frac12<\eta_{m,+}<1. \tag{11}
\]

The smaller root gives the upper contact and the larger gives the lower contact. The diagonal joins \(F_i^T\) to \(F_i^B\); the cross-strut joins \(F_i^B\) to \(F_{i-1}^T\). Each shared-edge point is one geometric contact represented by two faces.

Each face has two cross-ring edges and one ring edge. Hence each height side has twelve distinct edge contacts, joining twelve face arcs in a closed loop; each face contributes one arc per side. One can also see the single-arc assertion from (7): that simple loop crosses a given triangle’s boundary at exactly its two simple cross-edge roots. It cannot have an extra component wholly inside that triangle. Ring edges and vertices have no cone contacts by (5).

There are no hidden ray or tangency exceptions for this family:

- If \(D_{F,\sigma}=0\), the ray is parallel to the face plane and has no intersection, since \(c_F>0\). No cone generator is contained in a face plane.
- In a face interior, cone and plane meet transversely. The cone normal is proportional to \((x,y,-w)\), whose dot product with \(v\) is zero on the cone; it cannot be parallel to \(n_F\), for which \(n_F\cdot v=c_F>0\).
- Equation (11) excludes tangencies to cross-ring edges and multiple roots there. At a mesh seam the two conic pieces can have different tangents, but there is no vertex contact or additional intersection to count.

This excludes cone–face tangency, not tangency of the more constrained harmonic curve to a face. That latter event is relevant at amplitude onset below.

## 4. Imposing the signed frozen macro law

Substitution of (2) into a face plane gives precisely

\[
b\cos3(\theta-\ell)
\left[n_{F,x}\cos(\theta+\psi)+n_{F,y}\sin(\theta+\psi)+n_{F,w}\right]=c_F. \tag{12}
\]

For a supplied \(b>0\), this equality **and** the three inequalities (9), evaluated at (2), are necessary and sufficient for contact with that face. Taking the union over faces gives contact with the band; shared-edge duplicates are removed geometrically. This verifies and supplements the work order’s proposed equation.

If either multiplicative factor on the left other than \(b\) vanishes, there is no solution because \(c_F>0\). Division to solve for \(b\) is legitimate only when their product is positive. In particular the bracket alone need not be positive: for a negative scalar it is negative at a valid contact. No coplanar case or origin contact is lost by these rules. When \(A=0\), (2) is the origin relative to \(O\), which is outside the band.

### The independent continuous angular alignment

Set

\[
\chi=\ell+\psi,\qquad H_\chi(\varphi)=\cos3(\varphi-\chi).
\]

For the upper half of (2), the physical azimuth is \(\varphi=\theta+\psi\). For the lower half it is \(\varphi=\theta+\psi+\pi\). In the latter case the harmonic is \(-H_\chi(\varphi)\). Thus, on **either** side, the geometric frozen curve has the form

\[
v=bH_\chi(\varphi)(\cos\varphi,\sin\varphi,\sigma),
\qquad H_\chi(\varphi)>0. \tag{13}
\]

The necessary-and-sufficient radial contact condition is consequently

\[
H_\chi(\varphi)>0,\qquad bH_\chi(\varphi)=T_\sigma(\varphi). \tag{14}
\]

The sign restriction is essential; replacing the signed scalar by an absolute value at the parameter azimuth would put lower points on the wrong rays. Upper and lower curve points are vertically paired, but the two band contact heights \(T_+\) and \(T_-\) need not agree at their common azimuth.

Writing \(\alpha=\theta-\ell\) in (2) shows that the continuous geometric image depends on \(\ell,\psi\) only through \(\chi\). Keeping \(\chi\) fixed while changing their split only changes the angular starting label. It is therefore inappropriate to fit them as independent continuous-image orientations. This reparameterization need not preserve a fixed clock grid.

### Exact onset and proof of the entire allowed amplitude interval

Let \(I_\chi=(\chi-\pi/6,\chi+\pi/6)\); the other two positive-harmonic intervals are its translates by \(2\pi/3\). Define

\[
B_\sigma(u,\mathrm{hand},\chi)
=\min_{\varphi\in I_\chi}
\frac{T_\sigma(\varphi;u,\mathrm{hand})}{\cos3(\varphi-\chi)}. \tag{15}
\]

This is a well-defined attained minimum, despite the open interval. Its objective is continuous, positive, and tends to infinity at both interval ends, since the numerator stays bounded away from zero. The band’s \(C_6\) symmetry makes the same minimum apply on all three intervals.

The image of this continuous objective is exactly \([B_\sigma,\infty)\): it attains its minimum, and moving from a minimizer toward either endpoint supplies every larger value by the intermediate value theorem. Therefore

\[
\boxed{\text{contact on side }\sigma\iff b\ge B_\sigma.}
\quad
\begin{cases}
\text{at least one side: } b\ge\min(B_+,B_-),\\
\text{both sides: } b\ge\max(B_+,B_-).
\end{cases} \tag{16}
\]

No disconnected allowed-amplitude intervals are being assumed away. Equality is actual finite-band contact. At equality there is at least one contact per positive-harmonic interval; strictly above onset there are at least two per interval, one on each side of a minimizer. Thus there are at least three, respectively six, distinct geometric contacts on that height side. Further contacts or repeated scalar roots can occur; these lower counts are not a global root classification.

The inherited clearance gives an immediate exclusion for \(b<a/2\). In fact equality is excluded too: for \(u>0\), the angular wedge used for each band triangle’s clearance is strictly narrower than \(120^\circ\); at \(u=0\), equality \(R=a/2\) requires the equal-weight midpoint of \(T_iB_{i+2}\), at \(w=0\). None is on the cone. Compactness then gives

\[
\frac a2<\min_\varphi T_\sigma(\varphi)
\le B_\sigma(\chi)
\le T_\sigma(\chi)<h. \tag{17}
\]

Hence \(b\le a/2=d/4\) is a rigorous uniform no-contact range, not the sharp phase-dependent onset. Conversely **every \(b\ge h\) guarantees contact on both sides**, for every alignment, member and hand. Each fixed comparison actually has a smaller exact threshold given by (15). Increasing amplitude does not lose continuous contact: the contact angles can move toward harmonic zeros, even when the curve’s maxima lie beyond the band.

For an entirely finite-face version of (15), replace \(T_\sigma\) by \(c_F/D_{F,\sigma}\) from (8), retaining its barycentric admissibility. Minimize \(c_F/[H_\chi D_{F,\sigma}]\) over the admissible arcs with \(H_\chi>0\). At a smooth interior minimizer,

\[
H'_\chi D_{F,\sigma}+H_\chi D'_{F,\sigma}=0,
\quad H'_\chi=-3\sin3(\varphi-\chi),\quad
D'_{F,\sigma}=-n_{F,x}\sin\varphi+n_{F,y}\cos\varphi.
\]

This is tangency of the frozen curve to that face. A first contact can instead occur at a shared-edge corner, where one-sided conditions apply. Above onset there can also be other tangencies at stationary values. Equations (8)–(9), (12), and (15) include all of them without assuming transversality or differentiability across seams. On each face the contact equation is a nonconstant trigonometric polynomial with a nonzero fourth-harmonic contribution, so it cannot hold on an interval: contacts at fixed positive amplitude are finite, not whole coincident curve arcs.

For the native frozen amplitude, (16) means \(A\ge B_\sigma/\mu\). It does not guarantee that any particular supplied state, time and scale attain that value. If negative \(A\) is admitted, explicitly replace \(A\) by \(|A|\) and \(\ell\) by \(\ell+\pi/3\), since that shift negates the third harmonic. The same criteria then apply to the resulting curve and sample signs; no such change is made to the primary positive-amplitude defaults here.

### Cyclic symmetry, hand reflection and traversal

The frozen curve has \(C_3\) symmetry. Its contact set inherits that symmetry because the band has \(C_6\). Rotating \(\chi\) by \(\pi/3\) rotates the contact set by \(\pi/3\), preserving the band, so each threshold is \(\pi/3\)-periodic in \(\chi\). This relates contact sets by a spatial rotation; it does not identify differently located points.

The source reflection gives

\[
T_\sigma^{\mathrm{MINUS}}(\varphi;u)
=T_\sigma^{\mathrm{PLUS}}(\pi-\varphi;u),
\quad
B_\sigma^{\mathrm{MINUS}}(u,\chi)
=B_\sigma^{\mathrm{PLUS}}(u,\pi-\chi).
\]

The reflected frozen image has alignment \(\pi-\chi\); in the relative parameter \(\alpha=\theta-\ell\), the corresponding map is \(\alpha\mapsto-\alpha\). It reverses traversal order. Away from the origin the original parameter is recovered as \(\theta=\varphi-\psi\) above and \(\theta=\varphi-\psi-\pi\) below, modulo \(2\pi\). Those formulas distinguish a geometric contact set from its visiting order. They do not assert that reflection preserves the default sampled sequence. [E:223–245]

## 5. Exact worked reference at zero, with the actual face list

This is a conditional coordinate reference, not a preferred member or hand. Use the PLUS zero limit of (1) and, for this example only, the declared comparison rotation \(\psi=0\). Retain the default \(\ell=0.244\). Put

\[
k=\frac{a\sqrt3}{4h}=\frac{\sqrt6}{8},\qquad
c_0=\frac{a\sqrt3}{4},\qquad
t_0=\frac{c_0}{1-k}=\frac{h\sqrt6}{8-\sqrt6},\qquad
\eta_0=\frac{1-t_0/h}{2}.
\]

Since \(1/4<k<1/2\), one has \(0<\eta_0<1/3\). The actual face
\(F_1^T=[T_1,T_2,B_3]\) has plane \(x-kw=c_0\). The cone point \(P_+=(t_0,0,t_0)\) lies strictly inside it, with positive barycentric weights

\[
\left(\frac{1+\eta_0}{2},\frac{1-3\eta_0}{2},\eta_0\right).
\]

The actual face \(F_0^B=[T_0,B_2,B_1]\) has plane \(x+kw=c_0\). The cone point \(P_-=(t_0,0,-t_0)\) lies strictly inside it, with weights

\[
\left(\eta_0,\frac{1+\eta_0}{2},\frac{1-3\eta_0}{2}\right).
\]

For example, the upper weights give horizontal coordinate
\(x=(\sqrt3a/2)(1-\eta_0)=t_0\), \(y=0\), and height \(h(1-2\eta_0)=t_0\); the lower calculation is the reflected-height counterpart in its stated face. This establishes finite-triangle membership, not just plane equality.

Write \(C=\cos(3\ell)\) and \(S_\ell=\sin(3\ell)\), both positive at the unchanged default. The actual frozen curve visits \(P_+\) at \(\theta=0\) and \(P_-\) at \(\theta=\pi\) exactly when

\[
b=\frac{t_0}{C},\qquad\text{equivalently }\mu A=\frac{t_0}{\cos(3\ell)}.
\]

These are clock sectors 0 and 6; their \(C_3\) copies supply sectors 4,8 above and 2,10 below. The lower scalar is negative, but its physical horizontal azimuth is zero, not \(\pi\). This is an amplitude condition, not a claim that a supplied state satisfies it.

It is also demonstrably later than continuous onset. Near physical azimuth zero, both relevant contact-height functions equal \(c_0/(\cos\varphi-k)\), so their derivative at zero vanishes. For \(\chi=\ell\), the derivative of the objective in (15) at zero is \(-3t_0S_\ell/C^2<0\). Thus each continuous threshold is strictly less than this sampled-hit amplitude.

The same zero reference makes shared-edge contact explicit: on every actual diagonal \(T_iB_{i+2}\), (10) becomes \(-1+5\eta-5\eta^2=0\). Its roots are \((1\mp1/\sqrt5)/2\), giving heights \(\pm h/\sqrt5\). Each such point belongs to the two incident faces and is counted once. Its frozen-curve amplitude still must satisfy (14); cone membership alone does not supply that amplitude. The MINUS reference is obtained by reflecting all these triangles and points, retaining its distinct zero face complex.

## 6. What the existing clock samples

For a fixed clock with step \(d_q\), use only its reachable residues

\[
\mathcal Q=\{(q_0+nd_q)\bmod N:0\le n<N/\gcd(N,|d_q|)\},
\qquad \gcd(N,0)=N,
\]

and \(\theta_q=2\pi q/N\). A shorter supplied observation list uses its actual subset. For the frozen positive-amplitude law let \(h_q=\cos3(\theta_q-\ell)\). A sector with \(h_q=0\) is the origin and cannot hit. For every other sector define

\[
\sigma_q=\operatorname{sign}h_q,\qquad
\varphi_q=\theta_q+\psi+\pi\,\mathbf1_{h_q<0}\pmod{2\pi}.
\]

Its exact sampled-hit condition is

\[
b=\frac{T_{\sigma_q}(\varphi_q)}{|h_q|},
\]

equivalently (12) and (9) at that sector. Thus a finite clock orbit supplies a finite set of amplitudes for each side, not the continuous interval (16). A continuous intersection at a different angle is missed. Even when the whole grid is reachable, no observation is implied at angles between its sectors. [Z:46–82; AZ:47–69]

For \(N=12\), step one, the unchanged default lock gives

\[
(h_q)_{q=0}^{11}=(C,S_\ell,-C,-S_\ell,C,S_\ell,-C,-S_\ell,C,S_\ell,-C,-S_\ell),
\]

where \(C=\cos(0.732)>0\) and \(S_\ell=\sin(0.732)>0\). Each side samples the same two physical-azimuth classes, \(\psi\) and \(\psi+\pi/6\), each repeated under \(120^\circ\) rotations. Consequently the complete exact amplitude sets are

\[
\boxed{\mathcal S_\sigma(u,\mathrm{hand},\psi)=
\left\{\frac{T_\sigma(\psi)}{C},
\frac{T_\sigma(\psi+\pi/6)}{S_\ell}\right\}.} \tag{18}
\]

Contact on side \(\sigma\) occurs iff \(b\in\mathcal S_\sigma\); both sides are sampled iff \(b\in\mathcal S_+\cap\mathcal S_-\). The two values on a side may coincide, and the upper/lower sets need not intersect. Every member of \(\mathcal S_\sigma\) is at least \(B_\sigma\), since it is a continuous contact too. One matching value supplies its three cyclic copies; coincident values supply both classes.

This also sharply distinguishes large-amplitude behavior. Every \(b\ge h\) gives continuous contact on both sides, whereas

\[
b>\frac{h}{\min(C,S_\ell)}
\]

puts every default sampled point outside the band’s height range, so none can hit. No lock or coefficient has been retuned to arrange (18).

For the continuous image, only \(\chi=\ell+\psi\) matters. For a fixed sampled clock, the relative grid offsets \(\theta_q-\ell\) matter as well: a reparameterization is allowed only if it maps the reachable sector set onto itself. For instance, the continuous reflection correspondence \(\theta\mapsto2\ell-\theta\), with the appropriately reflected placement, preserves the full \(N\)-grid only if \(2\ell\) is a grid increment modulo \(2\pi\). The default \(\ell=0.244\), \(N=12\), does not meet that condition. Clock traversal follows its supplied step, not a sorting of spatial contact points.

A rendered segment joining samples is not an intermediate macro observation. Its possible triangle intersections are unrelated to (18); it need not even lie on the macro cone. No tolerance, interpolated motion or renderer chord is used as exact-contact evidence. [E:196–245]

## 7. Scope of the result and remaining conditional data

The cone identity and finite-face point criterion apply to **any supplied finite macro scalar**, because the source map is always \(M=z(\cos\theta,\sin\theta,1)\). For supplied evolving values \(z_j,\theta_j\), the complete pointwise rule is: if \(z_j=0\), there is no contact; otherwise set

\[
\sigma_j=\operatorname{sign}z_j,\quad
\varphi_j=\theta_j+\psi+\pi\mathbf1_{z_j<0},\quad
t_j=\mu|z_j|.
\]

Then contact is equivalent to \(t_j=T_{\sigma_j}(\varphi_j)\), or to the finite-face plane and barycentric conditions. For supplied evolving positive staged amplitudes, substitute \(z_j=A_j\cos3(\theta_j-\ell)\) point by point. The frozen interval theorem does not turn such a sequence into a continuous crossing trajectory.

The phase reduction, vertical pairing, threshold interval and default two-value amplitude sets as written depend on the frozen pure third harmonic. They are not conclusions about an EMA trajectory, a retained Z-total CSV, the chiral term or the blended vector. The universal cone statement can apply to a supplied EMA macro point, but its scalar law does not justify substituting the frozen harmonic thresholds. [Z:145–161,202–265; E:154–168]

The previous no-fan result is preserved: under this same centre/axis alignment, azimuth rotation and uniform positive scale, every macro point has horizontal radius \(|w|\), while every point of the twelve refined fan triangles has radius strictly less than \(|w|\). Thus none of these band contacts is a fan contact. They also establish nothing about the shell’s separate notch measurement regions. Anisotropic fan fitting remains deferred. [R0:189–210,229–246]

There is no unresolved existence or amplitude-interval case within the stated member domain and the two prescribed hands. General phase-dependent onset values remain specified by the exact admissible extremum (15), rather than an unnecessary classification of all its stationary roots. An actual observational hit remains conditional on the supplied member, hand, placement and scalar values; none has been inferred from visual resemblance or from a run.

The evidence for the new claims is the algebra above. Only source/filesystem reads and this report write were performed for this order. No scientific code, simulation, test, numerical experiment, new render, application launch, implementation, publication action or repository mutation was performed. Work stops with this report.

## Source locations

All line numbers refer to the consulted local files. Existing computational statements in those files are provenance, not new certification for this report.

| Key | Exact source portions used |
|---|---|
| R0 | [Completed Z/crystal report][R0], definitions (1)–(6), actual sections at 83–93, no-fan proof 189–210, clearance 229–233, scope 241–246 |
| VC | [verify_host_registration.py][VC], `canonical_points` 44–66 and `candidate_faces` 68–79, read as text |
| CJ | [CANONICAL_CRYSTAL_CANDIDATE.json][CJ], origin/scale/domain 6–25, ring/face rules 218–231 |
| HG | [HOST_GEOMETRY.json][HG], centre, axis and host constants 15–29 |
| SI | [SIGNED_FAMILY_IDENTITIES.md][SI], definitions/reflection 5–45; actual section vertices, endpoints and determinant proof 68–119 |
| Z0 | [ZERO_STATE_ANALYSIS.md][Z0], inherited zero connectivity 3–6; distinct limits 46–63; fixed-list versus prescribed mirrored extension 77–103 |
| FA | [TWISTED_HEX_FAMILY_ANALYSIS.md][FA], candidate status and physical parameter domain 29–43; actual section distinction 53–57; zero limits 86–93 |
| G | [geometry.py][G], width/edge/centre 16–26; host-axis rotation and reflections 166–183 |
| Z | [z_manifold.py][Z], clock 46–82; defaults and staged scalar 90–142; macro/blend 145–161; pure observation 197–199; EMA distinction 202–265 |
| E | [Paper E v0.1.1][E], definitions 52–76; frozen harmonic and samples 112–150; cone/sign 154–195; projection, drawing and transformations 196–245 |
| AZ | [Atlas entry 06 source packet][AZ], clock and reachable sectors 47–69; harmonic/sampling scope 99–138 |

[R0]: C:/Users/Notandi/.codex/reports/Z_AND_CENTRAL_TWISTED_HEX_CRYSTAL_GEOMETRIC_RELATIONSHIP_INVESTIGATION_v0.1.md:5
[VC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/verify_host_registration.py:44
[CJ]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/CANONICAL_CRYSTAL_CANDIDATE.json:218
[HG]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/HOST_GEOMETRY.json:15
[SI]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/SIGNED_FAMILY_IDENTITIES.md:68
[Z0]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/ZERO_STATE_ANALYSIS.md:46
[FA]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/TWISTED_HEX_FAMILY_ANALYSIS.md:29
[G]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py:16
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[E]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md:112
[AZ]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_06_z_observer/TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md:47
