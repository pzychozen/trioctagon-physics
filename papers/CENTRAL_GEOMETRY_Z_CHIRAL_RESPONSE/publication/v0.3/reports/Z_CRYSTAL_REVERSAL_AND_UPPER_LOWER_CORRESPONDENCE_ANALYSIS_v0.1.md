# Z and the Central Crystal — Reversal and Upper/Lower Correspondence v0.1

20 October 2026 · Source-led written investigation for GPT and Hilmir

**Answer.** The geometry supports a precise part of Hilmir’s forward/reverse picture. Every existing edge can be traversed in either direction without changing the object’s hand. At the PLUS zero member, a particular rigid half-turn exchanges upper and lower fans and openings while preserving the actual triangle mesh and the fixed shell. It also maps a downward cross-ring edge to an upward traversal of another existing edge. A horizontal reflection alone instead exchanges the two distinct zero surfaces. At nonzero crystal parameter, unequal upper/lower sizes obstruct this same upper/lower symmetry.

Z supplies exact frozen macro upper/lower pairs six clock sectors apart. Full Z has additional, explicit chirality conditions for those pairs to agree with a reflection about the crystal’s centre. The mesh-preserving half-turn faces a separate obstruction from the unchanged lock angle. Conditional full-Z matches survive on odd clock sectors, but there is no general correspondence covering the whole curve or clock grid. Channel permutations do not transform the chiral triple like an ordinary Cartesian arrow.

No supplied definition evolves the crystal’s pose or shape. Continuous rigid axial motion would require releasing its current upper-tip registration. Registration is a placement equality, not an assumed fastening. The established symmetries and conditional observation identities therefore support geometric comparisons, not spontaneous reversal, retracing, a selected exit, or physical guidance of flow.

## 1. Authority, unchanged comparison and the meanings of reversal

The authoritative checkout read was
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at actual local HEAD
`3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`.
The relevant source definitions agree with the retained reports. No material definition discrepancy was found. The attachment supplies the investigation questions; the primary files and accepted geometry supply the definitions. Historical computational claims in references are inherited evidence, not computations performed here.

The principal object is the refined **PLUS zero face complex** already used in the four-update reports. It is not the historical intersecting construction, and its vertex scaffold is not a substitute for its faces. Both hands and their distinct zero surfaces remain in the comparison. The source family parameter is denoted by \(\tau\), never identified with time. [R0, geometry sections; RH §§4–5; SI; Z0]

Four different operations must remain separate:

* A rigid displacement changes the crystal’s pose relative to the fixed shell.
* Reversing an edge traversal changes the orientation of a parameterized path on the same object.
* An upper/lower exchange is a specified map of points and faces; whether it preserves the object must be proved.
* Hand reflection or shape-parameter variation changes which geometric object is being compared. Neither follows from reversing traversal.

The current geometry is immutable shell data and a separately documented crystal family. The native map has no geometry, pose or shape input; the observer reads the native state and an explicit clock. No inspected definition advances a crystal position, orientation or \(\tau\). This absence does not prevent the following structural analysis. [G: `FoldedModule`, `folded_module`; VC: `canonical_points`, `candidate_faces`; D: `_advance`, `step3`; Z: `observe_staged`; RUN: `_append`]

Use centred physical coordinates \(v=X-O=(x,y,w)\), with
\[
s=\sqrt2-1,\quad d=1-\frac{\sqrt2}{2},\quad
r=\frac{\sqrt3}{6},\quad a=\frac d2,\quad h=\frac s2,\quad
H_0=\frac12,\qquad O=(0,r,0).
\tag{1}
\]
Here \(H_0\) is the apex height called H in earlier reports; H below denotes a reflection. The retained plotting placement is exactly \(X=O+Z_{\rm total}\): unit scale, zero extra azimuth. No state, scale, angle or chiral offset is fitted.

The reference native configuration remains
\((\epsilon,g,\lambda,k)=(0.1,0.2,0.17,(2,3,4))\).
Where an input from the original twelve-coordinate \(10^{-8}\) box is discussed, its own chosen configuration stays fixed. A transformed state used in an identity is a mathematical comparison; it is not claimed to lie in that original box or to be a new actual observation.

## 2. Existing lines and their two traversal directions

### 2.1 Coordinates, connectivity and legitimate azimuth lifts

For PLUS at magnitude \(u=|\tau|\in[0,h]\), put
\[
e_i=(\cos\alpha_i,\sin\alpha_i),\quad
\alpha_i=-\pi/2+i\pi/3,\quad n_k=e_{2k},\quad J(x,y)=(-y,x),
\]
\[
A_u=I-(u/r)J
=\sigma_u R_{-\delta},\qquad
\sigma_u=\sqrt{1+(u/r)^2},\quad \delta=\arctan(u/r).
\]
Then
\[
T_i=(ae_i,h),\quad B_i=(aA_ue_i,-h),\quad
U_k=(rn_k,H_0),\quad L_k=(rA_un_k,-H_0).
\tag{2}
\]
Indices i and k are modulo six and three. The band triangles are
\[
F_i=[T_i,T_{i+1},B_{i+2}],\qquad
D_i=[T_i,B_{i+2},B_{i+1}].
\tag{3}
\]
The upper fan at k consists of
\([T_{2k-1},T_{2k},U_k]\) and \([T_{2k},T_{2k+1},U_k]\);
the lower fan substitutes B and L. MINUS is the reflection of **vertices and faces together** through \(x=0\). [VC:44–79; SI §§1, actual band sections]

The two cross-ring edge families are \(T_iB_{i+1}\), the actual cross-struts, and \(T_iB_{i+2}\), the chosen triangulation diagonals. The latter are existing mesh edges, not separately declared material struts. There are no \(T_iB_i\) struts in this mesh.

For m=1 or 2 parameterize one of these existing segments by
\[
\Gamma_{i,m}(\eta)=
\big((1-\eta)ae_i+\eta aA_ue_{i+m},\ h(1-2\eta)\big),
\qquad 0\le\eta\le1.
\tag{4}
\]
This parameter labels a segment, not elapsed time. Its endpoint azimuth difference is
\[
\Delta\phi_m=m\pi/3-\delta.
\]
Since \(u/r\le\sqrt3s<\sqrt3\), \(0\le\delta<\pi/3\); consequently
\[
0<\Delta\phi_1<\pi,\qquad 0<\Delta\phi_2<\pi.
\]
Both endpoint radii are positive. Their positive convex combinations lie in a sector narrower than pi, so the horizontal projection never meets the axis. A continuous azimuth lift is therefore legitimate on the whole segment. Writing its horizontal part as p gives
\[
\frac{d\phi}{d\eta}
=\frac{\det(p,p')}{|p|^2}
=\frac{a^2\sigma_u\sin(m\pi/3-\delta)}{|p|^2}>0,
\qquad \frac{dw}{d\eta}=-2h<0.
\tag{5}
\]
The PLUS downward traversal has positive azimuth progression. At zero, its total azimuth advances are exactly \(\pi/3\) and \(2\pi/3\), respectively.

Traversing the **same** segment backward changes both derivative signs and both signed endpoint differences. It leaves the segment, its connectivity, and its geometric hand unchanged. In particular the sign of \(d\phi/dw\) is unchanged by reversing the parameter. Reflecting to MINUS instead reverses the azimuth progression at the same downward orientation. That is a different operation.

### 2.2 Open fan boundary arcs

Set \(g_k=e_{2k+1}=R_{\pi/3}n_k\). The upper open-boundary arc between adjacent tips is
\[
\mathcal B_k^+:\quad U_k\longrightarrow T_{2k+1}
\longrightarrow U_{k+1}.
\tag{6}
\]
Each straight part has a positive continuous azimuth advance of \(\pi/3\), justified by the same nonzero-sector argument. The axial changes are, in order, \(-d,+d\), since \(H_0-h=d\). Thus the arc advances azimuthally while descending and then ascending; it is not a monotonically downward channel.

The corresponding lower arc is
\[
\mathcal B_k^-:\quad L_k\longrightarrow B_{2k+1}
\longrightarrow L_{k+1}.
\tag{7}
\]
Its horizontal projection is \(A_u\) applied to that of (6), which preserves orientation and adds the common offset \(-\delta\). Its two azimuth advances remain \(+\pi/3,+\pi/3\), but its axial changes are \(+d,-d\). Reverse either arc and the ordered axial changes and azimuth orientation reverse. In MINUS the reflected arcs have the opposite azimuth orientation, with the same height sequence.

The middle fan edge \(U_kT_{2k}\), and its lower counterpart, has constant azimuth and joins the two triangles of one fan. It is not an open boundary edge. Ring edges are shared between the band and fans. The open boundaries are the twelve outer edges of (6)–(7), arranged as two six-edge loops. Cross-struts, diagonals, internal fan edges and open boundary edges therefore have different incidence roles. None is automatically a groove, guide or fluid streamline. [RH §5; R2 §3.2]

## 3. Exact upper/lower actions on faces, openings and the host

### 3.1 The zero mesh: face correspondence, not only matching vertices

Consider
\[
H=\operatorname{diag}(1,1,-1),\quad
S=\operatorname{diag}(-1,1,1),\quad
Q=SH=\operatorname{diag}(-1,1,-1),\quad
R=R_z(2\pi/3).
\tag{8}
\]
All act about O. H and S are improper reflections; Q is a proper half-turn about the centred y-axis.

At zero, H swaps \(T_i\leftrightarrow B_i\) and
\(U_k\leftrightarrow L_k\). S sends \(i\mapsto-i,\ k\mapsto-k\).
In the common zero vertex labels define the MINUS band faces by
\[
\bar F_j=[T_j,T_{j-1},B_{j-2}],\qquad
\bar D_j=[T_j,B_{j-2},B_{j-1}].
\]
Ignoring vertex ordering within an unoriented triangle, direct substitution gives
\[
SF_i=\bar F_{-i},\quad SD_i=\bar D_{-i},\qquad
HF_i=\bar D_{i+2},\quad HD_i=\bar F_{i+2},
\]
\[
\boxed{QF_i=D_{-i-2},\qquad QD_i=F_{-i-2}.}
\tag{9}
\]
H maps upper fans to lower fans with the same k in the opposite hand. S maps upper fans to upper fans at \(-k\), exchanging their two triangle sides and the hand. Q maps an upper fan to a lower fan at \(-k\) **in the same hand**, again exchanging its two sides. R sends \(i\mapsto i+2,\ k\mapsto k+1\) and preserves all faces.

Thus H and S exchange the zero hands; Q and R preserve each zero mesh. This is the source’s chiral \(D_3\) face symmetry, distinct from the achiral \(D_{3h}\) vertex scaffold. The distinction is material: Z0 §3 supplies a point strictly inside a PLUS band triangle lying in no MINUS triangle. Equal vertex sets and equal section areas cannot replace (9).

A direct forward/reverse correspondence now follows from (4):
\[
\boxed{Q\Gamma_{i,m}(\eta)
=\Gamma_{-i-m,m}(1-\eta)\quad(u=0,\ m=1,2).}
\tag{10}
\]
The half-turn maps a downward edge traversal to an upward traversal of another edge of the same family. It does not turn the original object into its mirror, and does not say that anything actually travels along either edge.

For boundary arcs, H maps \(\mathcal B_k^+\) to \(\mathcal B_k^-\) in the opposite hand. Q maps it to the **reverse traversal** of \(\mathcal B_{-k-1}^-\) in the same zero mesh. These statements include the intermediate odd ring vertex, not just the tips.

### 3.2 Finite shell notches and the open spaces between fans

The host is preserved by H, S, Q and R as a full octagonal face complex: H reverses each panel’s height, S fixes panel P2 and swaps P1/P3, and R cycles them. This follows from `panel_point` and the symmetric local octagon, and is established in Paper C §9. [G:16–49,166–183; PC §9]

For precision, write \(j_k=Jg_k\). The six finite notch measurement triangles are
\[
\mathcal N_k^\sigma=
\left\{
\left(2r-\frac{\sqrt3d}{2}\lambda_N\right)g_k
\zeta_Nj_k+\sigma(h+d\lambda_N)e_z:
0\le\lambda_N\le1,\quad
|\zeta_N|\le\frac{d\lambda_N}{2}
\right\},\quad \sigma=\pm1.
\tag{11}
\]
The parameters here describe a finite triangle, not time or native phase. Its plane is
\[
g_k\cdot v_{xy}+\sigma\frac{\sqrt3}{2}w
=2r+\frac{\sqrt3}{2}h.
\tag{12}
\]
Its legs are shell boundary edges; its base is a measurement chord. It is not a crystal fan or an added shell face. [PC §8; R2 (7)–(8)]

Because \(Sg_k=g_{-k-1}\) and \(Sj_k=-j_{-k-1}\), the exact finite-set correspondences are
\[
H\mathcal N_k^+=\mathcal N_k^-,
\quad S\mathcal N_k^\sigma=\mathcal N_{-k-1}^\sigma,
\quad Q\mathcal N_k^+=\mathcal N_{-k-1}^-,
\quad R\mathcal N_k^\sigma=\mathcal N_{k+1}^\sigma.
\tag{13}
\]
Both the plane and the bounded inequalities are preserved; \(\lambda_N\) stays fixed and S/Q reverse \(\zeta_N\).

At zero the fan-boundary openings have the same k mappings. Their angular midlines are \(g_k\), whereas fan tips point along \(n_k\), a \(60^\circ\) offset modulo \(120^\circ\). The actual opening at a height between ring and tips is the space between bordering fan pieces, not a triangle added across them. An isometry preserving the full mesh and host, such as Q at zero, maps these complementary spaces as well as their boundary edges.

Consequently Q preserves the zero band’s interior and surrounding region as separate sets while exchanging their positive and negative height sections. It preserves the zero throat plane and its finite aperture. H gives the corresponding statement between the two zero hands. This uses the actual star-shaped sections and their bounded interiors from R2 §2, not only their areas.

### 3.3 Nonzero members: the obstruction and the surviving mirror relation

For \(u>0\), the lower ring radius is \(a\sigma_u>a\), and the lower tip radius is \(r\sigma_u>r\), with relative angular offset \(-\delta\) in PLUS. H or Q would put these enlarged footprints at the upper levels. Every member of the retained family instead has upper radii exactly a and r. Therefore neither H nor Q maps this member to itself **or to another member of the retained registered family**, in either hand. A rotation cannot repair a radius mismatch; a rescaling or deformation would change the specified geometry and registration.

The fan-to-fan relation at nonzero u is the affine map
\[
(p,w)\longmapsto(A_up,-w)
\tag{14}
\]
from the upper fan system to the lower fan system of that member. It includes dilation and rotation, is not a rigid symmetry, and is not asserted to preserve the entire mesh. It does not preserve the host notch patches: the shell’s \(g_k\) axes stay fixed while lower opening axes rotate to \(R_{-\delta}g_k\).

S still maps PLUS at u exactly to its prescribed MINUS mirror. In common signed labels this is \(\tau\mapsto-\tau,\ i\mapsto-i\), together with the reflected face list. It preserves upper/lower designation and maps corresponding fans, openings and host patches. R remains a same-hand symmetry at every u.

The nonzero throat has \(w_*>0\) in both hands, as R2 (4) shows. Hand reflection does not move it below the middle plane. This is another obstruction to interpreting a hand switch as upper/lower reversal.

Passing through zero by changing \(\tau\) does not remove these distinctions. The signed vertex positions are continuous, but the prescribed mirrored face family has different PLUS and MINUS zero limits. Holding one face list fixed gives a different local continuation. Reversing travel on a fixed edge changes neither list. [SI §§1–2; Z0 §§1,3–4]

### 3.4 Literal axial motion and registration

Suppose an axial rigid rotation and translation sends the registered upper-tip set to the same fixed upper-edge centres:
\[
\{(rR_\chi n_k,H_0+c):k=0,1,2\}
=\{(rn_k,H_0):k=0,1,2\}.
\]
Then
\[
c=0,\qquad \chi\in(2\pi/3)\mathbb Z.
\tag{15}
\]
A continuous path in this discrete set is constant. If each physical tip must retain its own labelled centre, only \(\chi\in2\pi\mathbb Z\) remains. Allowing a general translation does not help: equality of the tip-set centroids forces that translation to vanish.

The Q endpoint at zero exchanges which tips are upper and lower. It is not a continuous rotation preserving the original upper-tip equalities along the way. A path between symmetry-related endpoint poses would have to release those equalities; its intermediate clearance and mechanical feasibility have not been established. Registration is not a weld, so this is not a claim that physical movement is impossible. It identifies the extra assumption required to discuss it.

Varying the existing family parameter can keep the upper tips fixed while changing lower geometry, but that is a shape deformation, not a rigid axial motion or an existing evolution law.

## 4. Frozen Z curves, clock relabelling and traversal reversal

Write, with the unchanged coefficients,
\[
A=A(\Omega,t_c)=0.618\frac{\|\Omega\|}{1+\|\Omega\|}
e^{-0.577t_c},\quad \ell=0.244,\quad
f(\theta)=\cos3(\theta-\ell),\quad
d(\theta)=(\cos\theta,\sin\theta,1),
\]
\[
M(\Omega,\theta,t_c)=Af(\theta)d(\theta),\quad
C(\Omega)=\Re\Omega\times\Im\Omega,\qquad
v=\alpha M+\beta C,\quad \alpha=1,\quad\beta=\frac12.
\tag{16}
\]
The geometry uses these existing component slots as plotting coordinates under the declared placement. It does not identify the channel-area triple with an ambient vector representation under every shell symmetry. All identities below are exact mathematical formulas; no floating implementation is being evaluated. At finite \(t_c\), \(A=0\) exactly when \(\Omega=0\), when C and v are also zero. [Z:103–161,189–199; RO:7–17]

### 4.1 Traversal reversal is always available as a parameter operation

At fixed \(\Omega,t_c\), the parameterization
\[
s\longmapsto v(\theta_0-s)
\]
traverses the same frozen angular curve in reverse. Its tangent is
\(-\partial_\theta v\) at the corresponding point. The curve’s position set and frozen chiral offset are unchanged. This statement does not require a spatial symmetry, a negative scalar height or conjugating the state. It supplies no orientation for an evolving crystal.

There is also a distinct reflection identity. Let \(V_\ell\) be the vertical-plane reflection whose horizontal action sends angle \(\theta\) to \(2\ell-\theta\). Then
\[
M(2\ell-\theta)=V_\ell M(\theta),\qquad
M(2\ell+\pi-\theta)=HV_\ell M(\theta).
\tag{17}
\]
Both follow from the evenness of cosine and \(f(\theta+\pi)=-f(\theta)\). Their rotated copies have reflection axes \(\ell+m\pi/3\).

These are **not** the crystal/host reflection planes at the retained placement. The host planes have horizontal axes \(\pi/2+m\pi/3\), modulo pi. Coincidence would require
\[
\ell=\pi/6\pmod{\pi/3},
\tag{18}
\]
which the unchanged \(\ell=0.244\) does not satisfy. Likewise (17) would require the clock relabelling
\(\widehat q=12\ell/\pi-q\), or that value plus six, with an optional integer multiple of four for the rotated copies. Since \(0<12\ell/\pi<1\), this is not an integer-sector permutation. No lock or placement is changed to cure this mismatch.

### 4.2 Upper/lower and threefold identities that do respect the grid

For the frozen macro curve, for every state and finite time,
\[
\boxed{M(\theta+\pi)=HM(\theta),\qquad
M(\theta+2\pi/3)=RM(\theta).}
\tag{19}
\]
The first identity uses both the negative scalar and the opposite horizontal direction; it is not \(M\mapsto-M\).
On the actual \(N=12\) grid these are precisely
\(\widehat q=q+6\) and \(\widehat q=q+4\), modulo twelve.

For the same frozen state, full Z satisfies
\[
v(\theta+\pi)-Hv(\theta)=\beta(C-HC)
=(0,0,2\beta C_3),
\tag{20}
\]
\[
v(\theta+2\pi/3)-Rv(\theta)=\beta(C-RC).
\tag{21}
\]
Thus original-centre upper/lower pairing holds exactly when \(C_3=0\);
the rotation identity holds exactly when \(C_1=C_2=0\).
Without these conditions the frozen curve has the corresponding symmetries about its translated centre/axis, as R2 (27) established. Those translated operations do not automatically preserve the fixed crystal.

These are equal-time, equal-state observations. An actual observation six scheduled updates later has a different native state and envelope time. Even artificially holding the state fixed while advancing time by \(6dt\) would produce the additional macro difference
\[
\alpha\big(e^{-6\gamma dt}-1\big)HM(\Omega,q,t_c),
\]
besides (20). This is an explanatory comparison, not a newly executed schedule.

### 4.3 The actual S and Q: exact lock mismatches

Put \(c_\ell=\cos3\ell>0\). Direct trigonometry gives
\[
\boxed{M(\pi-\theta)-SM(\theta)
=-2A c_\ell\cos3\theta\,d(\pi-\theta),}
\tag{22}
\]
\[
\boxed{M(-\theta)-QM(\theta)
=2A c_\ell\cos3\theta\,d(-\theta).}
\tag{23}
\]
For example \(f(-\theta)+f(\theta)=2c_\ell\cos3\theta\). The Q relation needs a scalar sign reversal, rather than the even reflection of (17).

The angle maps in (22)–(23) are the admissible sector permutations
\[
\widehat q=6-q,\qquad \widehat q=-q.
\tag{24}
\]
For nonzero states at the unchanged lock, their macro mismatch vanishes exactly when \(\cos3\theta=0\): on the grid, exactly the **odd sectors**. It does not vanish over the whole curve or grid. The other mesh-preserving zero half-turns \(R^jQ\) have relabelling \(4j-q\); their macro mismatch is R\({}^j\) applied to (23), with the same obstruction.

The permutations in (24) reverse the clock order: \(r(q+1)=r(q)-1\), not \(r(q)+1\). They are frozen observation comparisons, not symmetries of the unchanged step-one clock evolution. Conversely the offsets \(q+6,q+4\) commute with a step-one clock advance, but still do not identify two times of the original evolving state.

## 5. Native actions, same-state chirality and forward-map covariance

Let \(\mathcal K\Omega=\overline\Omega\), let P swap channels A and C
(\(P(C_1,C_2,C_3)=(C_3,C_2,C_1)\)), and let
\[
P_c(C_1,C_2,C_3)=(C_3,C_1,C_2).
\]
The face-state order is \(A=P1,B=P2,C=P3\), not the crystal index order \((P2,P3,P1)\). With that retained convention, the actual shell actions encoded by `face_state` are
\[
T_H=\mathcal K,\qquad T_S=-P\mathcal K,\qquad
T_Q=-P,\qquad T_R=P_c.
\tag{25}
\]
This follows directly from the decoder
\(\Re\Omega_i(e_z\times n_i)+\Im\Omega_i e_z\):
H preserves its horizontal tangent and reverses its vertical direction;
S exchanges A/C and reverses their horizontal tangents;
Q reverses both tangent coordinates while exchanging A/C.
Atlas 04 §13 gives the general derivation.

All actions in (25) preserve the norm, so their macro amplitude is recomputed from the transformed state and equals A at the same time. The polynomial cross-product identities, valid also at zero components, are
\[
C(\mathcal K\Omega)=-C,\quad C(P\Omega)=-PC,\quad
C(-P\mathcal K\Omega)=PC,\quad C(-P\Omega)=-PC,\quad
C(P_c\Omega)=P_cC.
\tag{26}
\]
In particular the chiral laws for the physical shell actions are **not**
\(HC,SC,QC,RC\) in general. The slots encode transported pair areas, not an automatically covariant ambient arrow. A new channel-to-space dictionary could change that question, but none is introduced. [FS:22–35,60–80,123–150; A04 §§13–14; R2 §8.2]

For the real-parameter polynomial stage \(\mathcal G_{\mathcal P}\),
\[
\mathcal G_{\mathcal P}(\overline\Omega)
=\overline{\mathcal G_{\mathcal P}(\Omega)}.
\]
For synchronization, conjugation reverses nonzero phases modulo \(2\pi\) and reverses every sine increment. `Arg_0(0)=0` is itself conjugation compatible, and zero outputs remain zero. Hence
\[
\boxed{\mathcal F_{\mathcal P}\mathcal K
=\mathcal K\mathcal F_{\mathcal P}}
\tag{27}
\]
at the **same configuration**, including zero components, for the exact source formula. In the nonzero phase charts of the phase-regions report, conjugation also sends \((u,v,\zeta)\) to \((-u,-v,-\zeta)\) with the coupled lift identifications. Their update formulas are odd under this joint change. This is native phase covariance, not a spatial or temporal velocity.

Any three-channel permutation \(\Pi\) is covariant with the complete triad map when k is carried with it:
\[
\mathcal F_{\epsilon,g,\lambda,\Pi k}(\Pi\Omega)
=\Pi\mathcal F_{\epsilon,g,\lambda,k}(\Omega).
\tag{28}
\]
The two neighbours are the other two channels, and their simultaneous sine sum is permutation covariant even at zeros. At the **same** k the polynomial mismatch is exactly
\[
\mathcal G_k(\Pi\Omega)-\Pi\mathcal G_k(\Omega)
=\epsilon(\Pi\Omega)\odot(k-\Pi k).
\tag{29}
\]
Thus \(\Pi k=k\), or the exceptional \(\epsilon=0\), suffices for fixed-configuration covariance. No such permutation symmetry is supplied by the worked unequal tuple: \(Pk=(4,3,2)\) and \(P_ck=(4,2,3)\). Its small original parameter box also keeps the k entries distinct. Equation (29) does not rule out accidental identities on particular states, but it rules out treating permutation covariance as a general fixed-configuration symmetry here.

The minus sign in \(T_S,T_Q\) is an additional common phase of pi. The common-phase covariance of synchronization requires all pre-sync components to be nonzero, or the bypass \(\lambda=0\). At a zero component its assigned phase does not shift with the others, so that covariance cannot be used generally across zero strata. The existing certified third/fourth pre-sync images are nonzero; their bounds are retained, not regenerated. Equation (26) itself needs no such qualification. [D:57–104; R3 §3.3; RP §§2–3]

Finally, (27) is **commutation with forward evolution**. Since \(\mathcal K^2=I\), it gives \(\mathcal K\mathcal F\mathcal K=\mathcal F\), not an inverse-map identity. A time-reversal claim would require a separate identity such as \(\mathcal T\mathcal F\mathcal T^{-1}=\mathcal F^{-1}\) on a specified domain. None has been established. Negating the observer clock step would likewise not invert the native update or undo its envelope schedule.

## 6. Full-Z correspondence tests and their exact limits

For any norm-preserving native action considered here, define
\[
\mathcal E_{G,T}(\Omega,\theta,t_c)
=v(T\Omega,\widehat\theta,t_c)-Gv(\Omega,\theta,t_c).
\]
The same-state amplitude and chirality laws give the exact decomposition
\[
\boxed{\mathcal E_{G,T}
=\alpha\,[M(\Omega,\widehat\theta,t_c)-GM(\Omega,\theta,t_c)]
+\beta\,[C(T\Omega)-GC(\Omega)].}
\tag{30}
\]
Consequently the displayed residual being zero is necessary and sufficient for the proposed full-vector correspondence. No amplitude and offset are varied independently.

### 6.1 H: an exact conditional bridge, generally between hands

For the actual shell state action \(T_H=\mathcal K\), with
\(\widehat\theta=\theta+\pi\) or \(\widehat q=q+6\),
\[
\boxed{\mathcal E_{H,\mathcal K}
=-\beta(C+HC)=(-2\beta C_1,-2\beta C_2,0).}
\tag{31}
\]
Hence
\[
v(\overline\Omega,q+6,t_c)=Hv(\Omega,q,t_c)
\quad\Longleftrightarrow\quad C_1=C_2=0.
\tag{32}
\]
This is an entire-curve and entire-grid observation identity for any supplied state satisfying that condition. It uses conjugation, which commutes with the native map at the same configuration. At the zero crystal it exchanges PLUS and MINUS and upper/lower target sets. It is not a same-hand zero-mesh symmetry.

There is also the unchanged-state identity (20), valid iff \(C_3=0\). That one is a frozen observation pairing, not the face-state action induced by H. Both conditions are stated separately to avoid substituting the most favourable action silently. Neither condition has been proved invariant under the native recurrence, so neither supplies a whole evolving paired trajectory automatically.

### 6.2 Q: the same-hand zero-mesh exchange

First use its actual shell action \(T_Q=-P\) and \(\widehat q=-q\). Equations (23), (26) and (30) give
\[
\boxed{\mathcal E_{Q,-P}
=2\alpha A c_\ell\cos3\theta\,d(-\theta)
+\beta(C_1-C_3,-2C_2,C_3-C_1).}
\tag{33}
\]
On the odd sectors the macro term vanishes; the full correspondence then holds exactly when
\[
C_1=C_3,\qquad C_2=0.
\tag{34}
\]
For completeness, (33) resolves the even sectors too. With \(\Omega\ne0\), summing its x and w components forces
\(\cos\theta=-1\), hence \(q=6\), because \(\cos3\theta=\pm1\) on even sectors. At that sector the remaining conditions are
\[
C_2=0,\qquad C_1-C_3=-2\alpha A c_\ell/\beta.
\tag{35}
\]
All other even sectors, including \(q=0\), are excluded for nonzero states, regardless of the chosen C. Thus no nonzero state makes (33) vanish on the entire grid. This bridge also has the parameter-permutation and common-phase qualifications in §5.

A useful second test uses **native conjugation alone**, explicitly not the shell-induced action of Q. It needs neither a channel permutation nor a parameter change:
\[
\boxed{\mathcal E_{Q,\mathcal K}
=2\alpha A c_\ell\cos3\theta\,d(-\theta)
-(0,2\beta C_2,0).}
\tag{36}
\]
The w component first forces \(\cos3\theta=0\) for a nonzero state. Therefore, at the retained defaults,
\[
\boxed{
v(\overline\Omega,-q,t_c)=Qv(\Omega,q,t_c)
\quad\Longleftrightarrow\quad
q\ \hbox{odd and}\ C_2=0,\qquad \Omega\ne0.}
\tag{37}
\]
The corresponding continuous-angle condition is
\(\theta=\pi/6+j\pi/3,\ C_2=0\).
This is a genuine conditional match between the same-hand zero geometry, a grid relabelling and an existing native transformation at the same fixed configuration. It is not a universal bridge, not an identification of the two native actions in (25), and not a fit of a new state.

Using the identity state action instead gives the same odd-sector macro match with chiral condition \(C_1=C_3=0\). These alternatives show exactly which component restrictions matter. They do not assert that an arbitrary supplied state satisfies any of them.

### 6.3 S and R: mirror and rotational comparisons

For S with its actual shell action \(-P\mathcal K\), the full residual is
\[
\boxed{\mathcal E_{S,-P\mathcal K}
=-2\alpha A c_\ell\cos3\theta\,d(\pi-\theta)
+\beta(C_1+C_3,0,C_1-C_3).}
\tag{38}
\]
It vanishes on odd sectors exactly when \(C_1=C_3=0\).
For nonzero states on even sectors its y component requires
\(\sin\theta=0\). At \(q=0\) the exact conditions are
\(C_1=0,\ C_3=-2\alpha A c_\ell/\beta\);
at \(q=6\) they are
\(C_3=0,\ C_1=-2\alpha A c_\ell/\beta\).
No other even sector qualifies. The same lock obstruction prevents an entire-grid S correspondence. Geometrically S relates hands without exchanging heights.

For R with its shell action \(P_c\), \(\widehat q=q+4\) gives
\[
\boxed{\mathcal E_{R,P_c}=\beta(P_cC-RC).}
\tag{39}
\]
For this one generator the precise vanishing condition is
\[
C=t\,(-(2+\sqrt3),1,1),\qquad t\in\mathbb R.
\tag{40}
\]
Indeed the third equation is \(C_2=C_3\); the first gives
\(C_1=-(2+\sqrt3)C_2\), which also satisfies the second.
If both the one-third and two-thirds rotation identities are required from the same original state, the second additionally requires
\(C=t'(1,-(2+\sqrt3),1)\); their intersection is \(C=0\).
Thus a single accidental vector match must not be promoted to general representation covariance. Fixed-configuration native cyclic symmetry remains obstructed by unequal k.

At \(\Omega=0\), all residuals vanish trivially. That observation point is the centre, not a contact with a fan or a finite notch. These exceptional zero equalities do not support passage guidance.

### 6.4 The already supplied contact state is not silently replaced

The original exact state in R2 §7 has norm three and
\[
C_*=2\left[
P_*-0.4635\cos(0.732)(1,0,1)
\right],\qquad
P_*=\left(\frac{\sqrt3a}{6},-\frac a2-\frac r3,
\frac{2h+H_0}{3}\right).
\tag{41}
\]
It contacts \([T_0,T_1,U_0]\) at \(q=0,t_c=0\) with barycentric weights \(1/3\). No new representative is selected here.

Its second chiral component is exactly
\[
C_{*,2}=-a-\frac{2r}{3}<0.
\tag{42}
\]
Therefore the conjugation-based H correspondence (32), and both Q conditions (34), (37), fail for this state. Independently, its q=0 is excluded by (33) for every nonzero state.

The unchanged-state H condition also fails: \(\cos(0.732)>1-0.732^2/2>0.73\), so \(0.4635\cos(0.732)>0.338\), whereas
\((2h+H_0)/3<0.31\). Thus \(C_{*,3}<0\).
These are written rational bounds, not evaluated trajectories. They show why the previously constructed upper-fan contact does not automatically furnish a matched lower contact under these operations.

No claim is made here that a subsequent member of the original certified box meets a special equality in §§6.1–6.3. Their exact necessary-and-sufficient conditions are available for supplied states; the retained four-observation classifications are unchanged, and no fifth update is taken.

## 7. Compact correspondence table and finite-contact implications

| Operation | Geometry preserved or exchanged | Existing Z counterpart | Exact limit |
|---|---|---|---|
| Reverse traversal of an existing edge | Same edge and hand; signed axial and azimuth progression reverse | Reverse a frozen angular parameterization | Neither operation moves the crystal or inverts native evolution |
| H | Host preserved; upper/lower exchanged; PLUS zero goes to MINUS zero | \(q\mapsto q+6\); \(T_H=\mathcal K\) | Full match iff \(C_1=C_2=0\); with unchanged state instead, iff \(C_3=0\); no registered nonzero-family exchange |
| S | Host preserved; hands exchanged; upper/lower designation retained | \(q\mapsto6-q\); \(T_S=-P\mathcal K\) | Residual (38); odd-sector match iff \(C_1=C_3=0\); lock, parameter and zero-stratum qualifications |
| Q=SH | Host and each zero mesh preserved; upper/lower fans, openings and notches exchanged | \(q\mapsto-q\); \(T_Q=-P\) | Residual (33); odd-sector match iff \(C_1=C_3,\ C_2=0\); unequal k prevents general fixed-configuration covariance |
| Q with conjugation as a separate comparison | Same geometric half-turn; this is not its encoded shell action | \(T=\mathcal K,\ q\mapsto-q\) | Nonzero-state full match exactly at odd q with \(C_2=0\); native commutation holds, clock-order commutation does not |
| R | Host and either hand preserved at every member | \(q\mapsto q+4,\ T_R=P_c\) | Residual (39); no general channel/Cartesian covariance or fixed-unequal-k symmetry |
| Lock-aligned \(V_\ell,HV_\ell\) | Macro-curve reflection/half-turn axes, generally not host axes | Continuous identities (17) | Noninteger grid relabelling and wrong geometric axes at the retained lock; full Z adds \(\beta[C(T\Omega)-GC]\) |
| Change \(\tau\) or switch hand | Deformation or reflected object, not reverse traversal | No supplied time or coupling law | Distinct zero face limits; no fitted observer counterpart |

When an exact full-vector identity holds and G maps an actual target to another, finite contact transfers by ordinary set membership:
\[
v\in F\quad\Longleftrightarrow\quad Gv\in GF.
\tag{43}
\]
For triangle contact this preserves all barycentric weights, including boundary cases. For (11) it preserves the plane equation and finite inequalities as shown in (13). At the PLUS zero member, a valid Q correspondence therefore carries an upper-fan contact to the specified lower fan in the same hand, or an upper-notch contact to its lower notch. H carries the analogous mesh statement between hands. These are **conditional implications**, not existence proofs for contact under the special chiral restrictions.

The openings between fans also map as complementary regions under the applicable full geometric isometry. Matching their angular midlines alone is weaker: it tests neither height, supporting plane nor finite extent. In the inherited geometry the zero-member fans are disjoint from all finite same-side notch patches; at nonzero members the previously established endpoint lower-tip/notch-vertex coincidences do not identify whole fans with notches. [R2 §§3.1–3.3]

A nonzero residual in (30) means that particular observation is not the proposed geometric image. It does not prove that the observation misses every other fan or notch; that is a separate finite-region test. Likewise an exact mapped contact does not select an exit, describe a path through an opening, or prove motion along an edge. No connecting drawing segment or unsampled angle is promoted to a physical path.

## 8. Results ready for paper consideration and remaining connections

The following results are ready to enter the proposed paper as mathematical statements, with the qualifications above: the signed progression of the two actual cross-ring edge families and fan boundary arcs; the face-level zero-mesh H/S/Q correspondences; the exact finite-notch mappings; the nonzero-radius obstruction; the registration obstruction to continuous axial rigid motion; the frozen macro and grid identities; and the full-Z mismatch formulas and conditional correspondences. They can be presented without a positive physical reversal result.

The strongest positive same-object geometric statement is (10) together with the Q mapping of upper/lower finite regions. The strongest fixed-configuration native result used here is conjugation commutation (27). Their partial observation bridge is (37), with an odd-sector and chiral-component restriction. Those three statements must not be merged into a universal reversal law.

The unresolved connections are whether any intended physical process moves or deforms the crystal, how its registration would be released, how actual matter or energy would interact with its edges and neighbouring spaces, and whether a specified evolving state satisfies a conditional contact correspondence at relevant observations. The current definitions do not answer those questions. No force, fluid, feedback, motion, inverse-map or channel-to-space law has been added.

The phase-region gain/loss results remain native synchronization statements. Their mean phases are not the observer angle, and their chiral-area changes are not a change of crystal hand or a spatial reversal. The existing four-update findings remain intact. [RP §§2–3,7–8]

Only source/reference reads, written algebra and this new report were used. The repository and earlier reports were preserved. No scientific-code or calculator execution, additional native update, simulation, test, rendering, viewer launch, implementation, paper drafting or publication operation was performed. SRG and memory remain outside scope. Work stops here for GPT and Hilmir’s review.

## Source locations

References identify the definitions and inherited evidence actually used. New face substitutions, edge derivatives and Z residuals are derived explicitly in this report.

| Key | Exact source location and use |
|---|---|
| G | [geometry.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py:16), constants and `panel_point`; 136–183, `folded_module`, `central_section`, `rotate_c3`, `reflect_vertical`, `reflect_horizontal` |
| FS | [face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py:22), frame/channel order; 60–80 decoder; 123–150 transport and cyclic areas |
| D | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:12), `L3`; 27–44 real fixed configuration; 57–104 `arg0`, `phase_sync`, `_advance`, `step3` |
| RO | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7), `z_chiral`, raw cyclic cross product |
| Z | [z_manifold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:47), clock; 91–161 staged coefficients, norm, scalar, macro and blend; 189–199 pure same-state observation |
| RUN | [_runner.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py:47), `_advance`; 83–96 `_append`, native update followed by clock/observer advancement and observation |
| PRE | [_presets.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18), `historical_observer`, unchanged staged literals and schedule |
| RH | [Crystal host registration report](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/CRYSTAL_HOST_REGISTRATION_REPORT.md:123), §§3–5 host targets, lower offsets, candidate faces, handedness and clearance |
| VC | [verify_host_registration.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/verify_host_registration.py:44), `canonical_points`, `candidate_faces`; read as text only |
| SI | [Signed family identities](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/SIGNED_FAMILY_IDENTITIES.md:8), signed labels/reflected connectivity; §§2–4 footprint map and actual section identities |
| Z0 | [Zero-state analysis](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/ZERO_STATE_ANALYSIS.md:8), full mesh versus vertex symmetry; 46–103 distinct zero surfaces and continuity qualifications |
| FA | [Twisted hex family analysis](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/TWISTED_HEX_FAMILY_ANALYSIS.md:29), parameter domain and candidate status; zero limits and geometric-only scope |
| PC | [Paper C v1.0.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md:241), §8 finite notch geometry and non-cap distinction; §9 exact host face symmetries |
| A04 | [Face-state/chirality source packet](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md:383), §§12–14 common-phase qualifications, induced shell actions and channel/Cartesian distinction |
| R0 | [Initial Z/crystal investigation](C:/Users/Notandi/.codex/reports/Z_AND_CENTRAL_TWISTED_HEX_CRYSTAL_GEOMETRIC_RELATIONSHIP_INVESTIGATION_v0.1.md), A–C: historical versus refined geometry, source/display distinction, placement, handedness and macro fan exclusion |
| R2 | [Central-passage report](C:/Users/Notandi/.codex/reports/FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md), §§1–3 coordinates, throat, openings and finite notches; §5 same-state full Z; §7 exact contact state; §8 transformed-curve and channel distinctions |
| R3 | [One-native-step report](C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md), §§2–5 schedule, complete native map, zero qualifications, attribution and finite-target tests |
| RP | [Synchronizer phase-regions report](C:/Users/Notandi/.codex/reports/SYNCHRONIZER_PHASE_REGIONS_AND_CHIRALITY_RESPONSE_ANALYSIS_v0.1.md), §§2–3 phase lifts and weighted chirality; §§7–8 existing stages and limits on spatial interpretation |
| WO | [Current work order](C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_Z_CRYSTAL_REVERSAL_CORRESPONDENCE_v0.1.md), exploratory hypothesis, questions A–C, report destination and execution boundary |
