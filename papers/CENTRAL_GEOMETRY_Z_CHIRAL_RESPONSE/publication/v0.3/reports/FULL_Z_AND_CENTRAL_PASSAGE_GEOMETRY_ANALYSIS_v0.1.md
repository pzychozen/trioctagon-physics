# Full Z and the Central Passage — Constriction, Threefold Geometry and Finite-Region Contact v0.1

19 October 2026 · Written mathematical analysis for GPT and Hilmir’s review

**Answer to Hilmir’s picture.** There is a genuine geometric throat in the planar region inside the actual crystal band. It narrows and then widens between the two rings. The minimum is at the middle plane only at zero crystal parameter; otherwise it moves upward, reaching height \(3h/5\) at the endpoint member. The surrounding region between the band and shell does the opposite: it is widest at that level. Thus “inside the central passage” and “around the central passage” lead to different area trends.

The threefold arrangement also has a precise geometric basis. The upper openings **between** adjacent crystal fans have the same central azimuths as the shell’s three upper notch patches. Upper fan tips instead meet the centres of horizontal shell edges, between the notches. Lower tips move along their corresponding edges as the lower crystal footprint rotates relative to the fixed notches. These are available openings and geometric correspondences, not three separately bounded flow channels. Apart from lower tip-to-notch-vertex coincidences at the endpoint member, the finite fan triangles do not meet the finite notch patches.

Full Z changes the point-contact question substantially. For a frozen native state, its chiral term translates the macro curve without changing its angular tangent. That translation is derived from the same state as the macro amplitude. An exact example below, with unit comparison scale, unchanged observer defaults and a nonzero macro term, puts full Z strictly inside an actual fan triangle. It therefore removes the universal macro-only fan exclusion for full Z. It establishes mathematical contact, not a flow, natural alignment or state known to be reached by the recurrence.

The shape can support a conditional constricted-duct interpretation in the central slab. A Venturi/Bernoulli effect would additionally require an actual fluid domain, driving and boundary conditions, velocity, density and conserved flux. None is supplied by the existing Z definitions. The geometric throat and the full-Z contact result do not depend on assuming that physical interpretation.

## 1. Evidence, conventions and inherited results

The consulted checkout is `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, unchanged from [R0] and [R1]. The read-only tracked-status inspection reported no tracked changes. Existing untracked material was preserved; no full-tree audit was performed. Source code was read as text. No scientific code, symbolic script, simulation, test, new render, viewer, implementation or publication operation was used.

The geometry and observer equations below are inherited definitions. The area formula, finite notch/fan separation, attainable-state construction and full-Z contact example are new written derivations. The placement is a declared comparison. The fluid discussion in §4 explicitly introduces hypothetical physical assumptions. No substantive contradiction with R0/R1 was found. In particular, an open band’s ability to bound a duct segment does not contradict the earlier statement that the full surface has no closed, capped chamber.

Retain physical width-one coordinates

\[
s=\sqrt2-1,\quad d=1-\frac{\sqrt2}{2},\quad r=\frac{\sqrt3}{6},
\quad a=\frac d2,\quad h=\frac s2,\quad H=\frac12,\quad O=(0,r,0).
\]

Useful identities are \(h=\sqrt2a\) and \(H-h=d\). Coordinates \(v=(v_x,v_y,w)=X-O\) are relative to the existing centre. Let

\[
u=|\tau|\in[0,h],\qquad \xi=u/r,\qquad
\mathsf A_u=I-\xi J,\qquad J(p_x,p_y)=(-p_y,p_x).
\]

For PLUS, put \(e_i=(\cos\alpha_i,\sin\alpha_i)\), \(\alpha_i=-\pi/2+i\pi/3\), and \(n_k=e_{2k}\). The actual vertices are

\[
T_i=(ae_i,h),\quad B_i=(a\mathsf A_u e_i,-h),\quad
U_k=(rn_k,H),\quad L_k=(r\mathsf A_u n_k,-H). \tag{1}
\]

The band triangles are \([T_i,T_{i+1},B_{i+2}]\) and \([T_i,B_{i+2},B_{i+1}]\), indices modulo six. Each upper fan contains \([T_{2k-1},T_{2k},U_k]\) and \([T_{2k},T_{2k+1},U_k]\); lower fans substitute \(B,L\). There are twelve band triangles and twelve fan triangles. [VC:44–79; CJ:218–231]

MINUS reflects the **entire face complex** by \(S(v_x,v_y,w)=(-v_x,v_y,w)\). It is not obtained by negative \(\tau\) with unchanged PLUS connectivity. The two zero face complexes remain distinct, although their vertex sets coincide. The original candidate JSON excluded zero; the later signed-family and zero analyses supply the zero limits used here. These rules remain the existing research candidate, not a host-selected member or a kernel adoption. [SI:5–45; FA:29–43,86–93; Z0:46–103]

R1 already establishes continuous, star-shaped band sections, one macro-cone contact on every azimuth half-ray on each height side, a finite-triangle membership criterion and the frozen pure-macro threshold/sampling results. Those results are inherited without rerunning or re-proving their classification.

## 2. The actual area throat and the surrounding region

### 2.1 Area of the polygonal band section

At \(w=h(1-2\eta)\), \(0\le\eta\le1\), the actual section alternates

\[
S_i=(1-\eta)ae_i+\eta a\mathsf A_u e_{i+1},\qquad
D_i=(1-\eta)ae_i+\eta a\mathsf A_u e_{i+2},
\]

with edges \(S_iD_i\) and \(D_iS_{i+1}\). This is the source’s twelve-edge star-shaped section, not corresponding-index interpolation. If \(b_r=a\sqrt{1+\xi^2}\) and \(\delta=\arctan\xi\), its consecutive determinants are

\[
\det(S_i,D_i)=\frac{\sqrt3}{2}(\eta b_r)^2+
\eta(1-\eta)ab_r\sin\delta,
\]
\[
\det(D_i,S_{i+1})=\frac{\sqrt3}{2}((1-\eta)a)^2+
\eta(1-\eta)ab_r\sin\delta. \tag{2}
\]

They are positive for interior sections, including \(\xi=0\). At the endpoints alternate edges collapse to the corresponding hexagon. Thus the shoelace area is the ordinary enclosed planar area. No material cap is added. [SI:68–119; R1 §2]

Since \(b_r\sin\delta=a\xi\), summing the six identical determinant pairs gives

\[
\boxed{\mathcal A_{\rm band}(\eta)
=\mathcal A_0\left[(1-\eta)^2+(1+\xi^2)\eta^2
+\frac{4\xi}{\sqrt3}\eta(1-\eta)\right],
\qquad \mathcal A_0=\frac{3\sqrt3}{2}a^2.} \tag{3}
\]

Define

\[
p=1-\frac{2\xi}{\sqrt3},\qquad
D=2+\xi^2-\frac{4\xi}{\sqrt3}=2p+\xi^2.
\]

On the allowed interval \(0\le\xi\le\sqrt3s\), \(p\ge1-2s=s^2>0\) and
\(D=(\xi-2/\sqrt3)^2+2/3>0\). Equation (3) becomes

\[
\mathcal A_{\rm band}=\mathcal A_0(1-2p\eta+D\eta^2)
=\mathcal A_{\min}+\mathcal A_0D(\eta-\eta_*)^2,
\]
\[
\boxed{\eta_*=\frac pD,\qquad
w_*=h\frac{\xi^2}{D},\qquad
\mathcal A_{\min}=\mathcal A_0\left(1-\frac{p^2}{D}\right).} \tag{4}
\]

The derivative is \(2\mathcal A_0(D\eta-p)\), and the second derivative is \(2\mathcal A_0D>0\). Since \(0<p<D\), there is exactly one stationary point in the open slab, a strict minimum. Traversing from the upper ring toward the lower ring, the inside area decreases until \(\eta_*\) and increases afterwards. It does not generally attain its minimum at \(w=0\).

The endpoints and positivity are explicit:

\[
\mathcal A_{\rm band}(0)=\mathcal A_0,\qquad
\mathcal A_{\rm band}(1)=\mathcal A_0(1+\xi^2),\qquad
\mathcal A_{\rm band}(\eta)\ge\mathcal A_0/2>0. \tag{5}
\]

The last inequality follows directly from (3), whose extra \(\xi\)-dependent terms are nonnegative and whose first two zero-parameter terms sum to at least \(1/2\). Equality holds only at \(\xi=0,\eta=1/2\).

For completeness,
\(d\eta_*/d\xi=-2\xi(1-\xi/\sqrt3)/D^2<0\) for \(\xi>0\). Thus the throat moves upward continuously. The minimum area itself increases strictly with \(\xi\): the partial derivative of the bracket in (3), evaluated at its interior minimizer, is
\(2\xi\eta_*^2+(4/\sqrt3)\eta_*(1-\eta_*)>0\).

| Member magnitude | Throat position | Minimum inside area |
|---|---|---|
| \(u=0\) | \(\eta_*=1/2,\ w_*=0\) | \(\mathcal A_0/2\) |
| \(0<u<h\) | \(1/5<\eta_*<1/2,\ 0<w_*<3h/5\) | Formula (4), strictly between its endpoint values |
| \(u=h\) | \(\eta_*=1/5,\ w_*=3h/5\) | \(\mathcal A_0(1-s^2/5)\) |

At the last endpoint \(p=s^2\), \(D=5s^2\), which gives the displayed exact values. Neither endpoint is degenerate. Reflection to MINUS reverses oriented shoelace signs if vertex order is retained, but preserves unsigned area and height. Consequently (3)–(5) hold for both hands; the throat does **not** move below the middle plane merely by changing hand. Equal zero-section areas do not identify the two zero surfaces.

### 2.2 Nesting inside the host and the complementary area

Throughout \(|w|\le h\), the shell section is the perimeter of an equilateral triangle of side one. Its filled planar interior has inradius \(r\) and area \(\sqrt3/4\). [G:153–163; PC:193–209]

Every band-section vertex is a convex combination of ring vertices. Hence its horizontal norm is at most \(a\sqrt{1+\xi^2}\), as is every point of a section edge. Moreover,

\[
\frac{a^2(1+\xi^2)}{h^2}\le5-3\sqrt2<1,
\qquad h<r.
\]

The whole section and its star-shaped filled interior therefore lie strictly inside the host’s incircle, hence strictly inside its triangular region. This establishes the nesting needed for subtraction, rather than assuming it from a drawing. It is consistent with the source’s all-vertex inward-halfspace proof. [RH:284–292]

The area between the band and shell in the central slab is exactly

\[
\boxed{\mathcal A_{\rm between}(w)
=\frac{\sqrt3}{4}-\mathcal A_{\rm band}(\eta),
\qquad \eta=\frac{1-w/h}{2}.} \tag{6}
\]

It is positive and has a unique **maximum**, not a throat, at \(w_*\). From the upper ring downward it first widens and then narrows. Its minimum over the closed slab occurs at the lower ring for \(u>0\); at zero the two end areas tie. Thus an area-speed analogy applied to this surrounding space would predict the opposite central trend from one applied to the inside region.

At each central height, the inside is one star-shaped disk-like region. The surrounding region is one connected annular region between nested boundaries; the geometry has not divided it into three channels. The guaranteed cylinder \(R_\perp<a/2\) is a constant-area protected subset of the inside, with section area \(\pi a^2/4\). It is neither a wall nor a replacement for (3) or (6). Historical scalar-cylinder and torus displays supply no additional physical boundary. [R0:229–233; ZD:331–413]

The actual band can geometrically provide lateral boundaries for an open-ended duct segment; end caps are not necessary for that statement. Interpreting those boundaries as impermeable material is an additional assumption. Above and below the rings, the section becomes three separated fan pieces. No closed duct section or partition into three outlets is continued through those pieces by inventing connecting walls.

## 3. Threefold incidence, finite notches and openings

### 3.1 The exact targets occupy different angular positions

Write \(m_k=Jn_k\). A shell panel has plane \(n_k\cdot v_{xy}=r\). Its upper and lower horizontal edges have endpoints
\((rn_k\pm h m_k,\ \pm H)\). The upper crystal tip is exactly their upper centre \(U_k\); the lower tip is

\[
L_k=(rn_k-u m_k,-H),
\]

which stays on the finite lower edge, at displacement \(u\) from its centre. It reaches one endpoint only at \(u=h\). [RH:132–148,172–203]

Define the three notch directions by

\[
g_k=R_{\pi/3}n_k=n_k+n_{k+1},\qquad j_k=Jg_k,
\]

with \(k\) modulo three. These are unit vectors. Their unordered azimuth set is \(\{\pi/2,7\pi/6,11\pi/6\}\), as in R0, displaced by \(60^\circ\) modulo \(120^\circ\) from the upper tip axes. Each notch is between two neighbouring panel-normal/tip directions.

The six actual finite measurement patches, relative to \(O\), are

\[
\mathcal N_k^\sigma:quad
v=\left(2r-\frac{\sqrt3d}{2}\lambda\right)g_k+zeta j_k
+\sigma(h+d\lambda)e_z,
\qquad 0\le\lambda\le1,\quad |\zeta|\le\frac{d\lambda}{2}. \tag{7}
\]

Here \(\sigma=+1\) denotes upper and \(-1\) lower. These are triangles with sides \(s,s,d\), spatial area \(\sqrt7s^2/8\), and the source plane

\[
g_k\cdot v_{xy}+\sigma\frac{\sqrt3}{2}w=K,
\qquad K=2r+\frac{\sqrt3}{2}h
=\frac{\sqrt3}{12}+\frac{\sqrt6}{4}. \tag{8}
\]

The unit normal with outward radial component is \((2g_k,\sigma\sqrt3)/\sqrt7\). The two chamfer legs are actual shell boundary edges; the base is a measurement chord. These finite patches are not added shell faces, crystal fans or material caps. [PC:241–283; GP:51–130, geometry only]

### 3.2 What aligns with a notch is an opening between fans

The upper crystal boundary is a six-edge loop alternating \(U_k\) and odd ring vertices. Between tips \(U_k,U_{k+1}\), the boundary arc is

\[
U_k\;--\;T_{2k+1}\;--\;U_{k+1},\qquad
T_{2k+1,xy}=a g_k.
\]

At height \(w=h+d\lambda\), \(0<\lambda<1\), the two bordering fan-edge endpoints have horizontal coordinates

\[
\left[(1-\lambda)a+\frac{\lambda r}{2}\right]g_k
\ \pm\ \frac{\lambda\sqrt3r}{2}j_k. \tag{9}
\]

They are symmetric about the same direction \(g_k\) as notch (7). Between them is an open angular sector; the displayed segment between them is not an existing face or wall. Equation (9) identifies the threefold relation without turning a tip into a notch centre. The upper fans flank these openings, while their own middle directions are \(n_k\).

The lower boundary has the same construction after applying \(\mathsf A_u\) horizontally and reversing height. Since

\[
\mathsf A_u=\sqrt{1+\xi^2}\,R_{-\delta},\qquad\delta=\arctan\xi,
\]

its opening axes are \(R_{-\delta}g_k\) and its tip axes are \(R_{-\delta}n_k\), whereas the shell notch axes remain \(g_k\). The lower relation is parameter dependent, not an exact fixed-axis copy of the upper alignment. The other hand reverses this angular shift. At zero the upper/lower footprint alignments agree, without erasing the band’s two distinct handed face complexes.

Plane normals give another useful distinction. For an upper fan’s two triangles, put

\[
p_{k,\pm}=\frac{\sqrt3}{2}n_k\pm\frac12m_k,
\qquad \gamma_f=\frac{\sqrt3(r-a)}{2d}>0.
\]

Their planes are

\[
p_{k,\pm}\cdot v_{xy}-\gamma_f w
=\frac{\sqrt3a}{2}-\gamma_f h. \tag{10}
\]

The horizontal normal azimuths are \(n_k\)'s angle plus or minus \(30^\circ\), not the notch axes at plus or minus \(60^\circ\). Their radial-outward normals have a negative vertical component. For the lower triangles the corresponding normal is \((\mathsf A_u^{-T}p_{k,\pm},+\gamma_f)\). These are surface orientations, not selected directions of motion; reversing a normal does not supply a different flow law.

### 3.3 Finite fans do not extend into finite notch interiors

This can be decided exactly, not just by comparing axes. For an upper notch plane, a ring vertex has plane value at most \(a+\sqrt3h/2<K\). An upper tip has value at most \(r/2+\sqrt3H/2<K\), because \(g_j\cdot n_k\) is either \(1/2\) or \(-1\). Convexity then places every upper fan strictly on the inner side of every upper notch plane. Thus none intersects a finite upper notch patch.

For a lower notch plane, ring vertices likewise satisfy strict inequality, using \(a\sqrt{1+\xi^2}<2r\). At lower tips,

\[
g_j\cdot(rn_k-u m_k)\le\frac r2+\frac{\sqrt3u}{2}.
\]

Subtracting their maximum plane value from \(K\) gives

\[
K-\left(\frac r2+\frac{\sqrt3u}{2}+\frac{\sqrt3H}{2}\right)
=\frac{\sqrt3}{2}(h-u)\ge0. \tag{11}
\]

For \(u<h\), all lower fans therefore miss all lower notch patches. At \(u=h\), each \(L_k=rn_k-hm_k\) is exactly the corresponding horizontal-edge endpoint and a base vertex of notch \(\mathcal N_{k-1}^-\). Only that tip reaches the plane; the other vertices of its fan triangles are strictly inside. Accordingly the sole fan/notch intersections at that member are these three lower vertex contacts, not finite overlaps or connections through aperture interiors. Reflection gives the other hand’s mirrored endpoint incidences. The disjoint height slabs and strict ring inequalities also exclude opposite-height or band/notch contacts.

The geometry therefore supports threefold open sectors adjacent to threefold shell notches, most directly in the upper footprint and the zero lower footprint. It also points elsewhere: tips terminate on panel edges, fan normals have different directions, and the lower structure rotates. No three enclosed channels, streamline, collision rule, mirror rule or equal division of flux is selected. The macro-only point-contact obstruction says nothing by itself about whether an assumed material wall could guide a fluid.

## 4. The limited Venturi/Bernoulli comparison

Suppose an additional fluid model chose one of the nested regions, supplied a drive, treated its lateral boundaries as impermeable, and imposed steady flow without lateral mass exchange or accumulation. For constant fluid density \(\varrho_f\), the sectional mean normal speed \(\bar U\) satisfies

\[
\dot m=\int_{\mathcal A}\varrho_f\,\mathbf U\cdot\hat n\,dA
=\varrho_f\bar U\mathcal A,
\qquad Q=\bar U\mathcal A.
\]

The constant-flux conclusion requires those domain and boundary assumptions; it does not follow from the polygon’s area alone. Fluid density \(\varrho_f\) is unrelated to the observer saturation \(\rho\). [NASA Glenn, *Mass Flow Rate*](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/mass-flow-rate/)

For steady, incompressible, inviscid flow with no added heat or mechanical work and negligible potential-height changes, the displayed Bernoulli relation is

\[
p+\tfrac12\varrho_f U^2=\text{constant along a streamline}.
\]

Here \(U\) is local streamline speed, not automatically \(\bar U\). Replacing it by \(Q/\mathcal A\) needs an appropriate quasi-one-dimensional approximation to the velocity distribution. Viscous losses, separation or significant potential changes require further treatment; no physical gravity term is imported into the kernel. [NASA Glenn, *Bernoulli’s Equation*](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/bernoullis-equation/)

Under that additional approximation, the **inside** throat would support increased mean speed and a corresponding pressure decrease along an applicable streamline. The surrounding region’s central area maximum would give the opposite mean-speed trend at the same conserved flux. Neither a pressure drop nor a flux value is determined here. NASA’s Venturi discussion explicitly rejects inventing an absent opposing boundary to infer a velocity field from a shape; the separated fan sectors likewise cannot be treated as a closed nozzle by adding invisible walls. [NASA Glenn, *Venturi Theory*](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/venturi-theory/)

| Ingredient | What the consulted model supplies |
|---|---|
| Geometry | Exact shell, candidate band/fans, finite notch measurements and the derived areas |
| Fluid domain and walls | No selection of inside versus surrounding fluid; no material or impermeability law |
| Velocity and pressure | No fluid velocity field or pressure variable |
| Conserved fluid flux and driving | No specified mass/volume flux, inlet, outlet or driving boundary condition |
| Z interpretation | A state/clock-dependent readout and declared plotting comparison; no calibrated fluid variable |

A norm, phase change, clock step or plotting derivative is not thereby fluid speed or pressure. Threefold geometry alone also does not impose symmetric boundary data or equal flux through three sectors.

## 5. Full Z from one native state

### 5.1 The dependency and sharp constraint

Freeze one finite native state \(\Omega=x+iy\in\mathbb C^3\) and clock time \(t_c\). The primary source definitions are

\[
\kappa=\|\Omega\|,\quad \rho=\frac{\kappa}{1+\kappa},\quad
A_\Omega=0.618\,\rho e^{-0.577t_c},\quad C_\Omega=x\times y,
\]
\[
Z_{\rm total}(\theta)=A_\Omega\cos3(\theta-\ell)
(\cos\theta,\sin\theta,1)+\frac12 C_\Omega,
\qquad\ell=0.244. \tag{12}
\]

These are the unchanged defaults \(\alpha=1,\beta=0.5\), not replacements by nearby geometric constants. Current observation computes the macro and chiral terms from the same supplied state and advances neither state nor clock. [Z:90–161,189–199; RO:7–17]

The existing Gram identity and its slack are

\[
\|C_\Omega\|^2=\|x\|^2\|y\|^2-(x\cdot y)^2,
\]
\[
\frac{\kappa^4}{4}-\|C_\Omega\|^2
=\frac{(\|x\|^2-\|y\|^2)^2}{4}+(x\cdot y)^2\ge0. \tag{13}
\]

Thus \(\|C_\Omega\|\le\kappa^2/2\). Equality holds exactly when \(\|x\|=\|y\|\) and \(x\cdot y=0\), including the zero state. Chirality is zero exactly when \(x,y\) are linearly dependent; for nonzero states this permits a common complex phase times a real vector, including relative signs, not merely strictly real or balanced states. [E:247–299; ZD:166–182; A04:353–380]

For a **given state**, C is fixed. Across all mathematically admissible states with a fixed norm \(\kappa\), the bound is also attainable in every direction and at every magnitude below it. Here is the construction, needed rather than assumed for the example below. For a prescribed vector \(c\ne0\) with \(L=\|c\|\le\kappa^2/2\), choose a unit \(p\perp c\), set \(q=\hat c\times p\), and put

\[
X=\sqrt{\frac{\kappa^2+\sqrt{\kappa^4-4L^2}}2},\quad
Y=\sqrt{\frac{\kappa^2-\sqrt{\kappa^4-4L^2}}2},\quad
\Omega=Xp+iYq. \tag{14}
\]

Then \(p,q\) are orthonormal, \(p\times q=\hat c\), \(X^2+Y^2=\kappa^2\), and \(XY=L\). Thus its actual norm is \(\kappa\) and its actual cross product is \(c\). For \(c=0\), choose \(y=0,\|x\|=\kappa\). This proves state admissibility in the observer’s mathematical input domain, not reachability from an initial condition under the recurrence.

Under a real nonnegative scaling \(\Omega\mapsto q_s\Omega\),

\[
A(q_s)=0.618\frac{q_s\kappa}{1+q_s\kappa}e^{-0.577t_c},
\qquad C(q_s)=q_s^2 C_\Omega. \tag{15}
\]

For a general complex scale, use its modulus in these expressions; common phase leaves C invariant. Macro amplitude saturates with state norm, while nonzero chirality grows quadratically. Varying amplitude while holding an arbitrary C fixed is therefore not the same operation as scaling a native state.

### 5.2 Translation and the declared comparison

Keep only

\[
\Phi(Z)=O+\mu R_z(\psi)Z,\qquad\mu>0,
\]
\[
\Delta_C=\mu\beta R_z(\psi)C_\Omega,\quad
b_\Omega=\mu\alpha A_\Omega,\quad
v(\theta)=\Delta_C+b_\Omega f(\theta)d_\psi(\theta),
\]
\[
f(\theta)=\cos3(\theta-\ell),\qquad
d_\psi(\theta)=(\cos(\theta+\psi),\sin(\theta+\psi),1). \tag{16}
\]

For this frozen state C is a constant translation of its macro curve. It does not reshape that curve or change its angular tangent:

\[
\frac{dv}{d\theta}=b_\Omega\left[-3\sin3(\theta-\ell)d_\psi(\theta)
+f(\theta)(-\sin(\theta+\psi),\cos(\theta+\psi),0)\right]. \tag{17}
\]

The offset is already part of Z, not an extra adjustable translation in \(\Phi\), a force or a dynamical deflection. The same-state constraint implies
\(\|\Delta_C\|\le\mu|\beta|\kappa^2/2\); both \(b_\Omega\) and \(\Delta_C\) are recomputed together under (15).

The three entries of C originate as a channel-area triple. The existing face-state decoder puts \(x_i(e_z\times n_i)+y_i e_z\) in shell face i’s tangent plane, in its stated A=P1, B=P2, C=P3 order. It does not identify the three area slots with one ambient Cartesian arrow. Equation (16) retains the already declared plotting-coordinate comparison without adding a conversion matrix or claiming a recovered spatial attachment. [FS:22–35,60–80,123–150; A04:353–380,486–508]

## 6. Exact contact with band, fans and finite notch patches

### 6.1 One criterion, with each finite target retained

For any ordered target triangle \(F=[p_0,p_1,p_2]\), all relative to O, choose

\[
U=p_1-p_0,\quad V=p_2-p_0,\quad n_F=U\times V,\quad c_F=n_F\cdot p_0.
\]

The exact plane equation for full Z is

\[
\boxed{b_\Omega f(\theta)
\bigl[n_{F,x}\cos(\theta+\psi)+n_{F,y}\sin(\theta+\psi)+n_{F,w}\bigr]
=c_F-n_F\cdot\Delta_C.} \tag{18}
\]

It is necessary but not sufficient alone. With \(Y_F=v(\theta)-p_0\) and
\(G=(U\cdot U)(V\cdot V)-(U\cdot V)^2>0\), also require

\[
\lambda_1=\frac{(Y_F\cdot U)(V\cdot V)-(Y_F\cdot V)(U\cdot V)}G\ge0,
\]
\[
\lambda_2=\frac{(Y_F\cdot V)(U\cdot U)-(Y_F\cdot U)(U\cdot V)}G\ge0,
\qquad \lambda_0=1-\lambda_1-\lambda_2\ge0. \tag{19}
\]

Equations (18)–(19) are necessary and sufficient. They are R1’s finite-triangle criterion with the actual state-derived offset inserted, not a test against an infinite supporting plane.

Apply them separately to:

- **Band:** the twelve triangles in (1), with the band connectivity stated in §1. R1’s explicit plane table can equivalently be used.
- **Fans:** the twelve fan triangles in §1, or their planes (10) and their lower transformed versions, always retaining their own barycentric inequalities.
- **Shell notches:** the six triangles (7), using (8). An equivalent particularly simple finite-domain test is
  \(\lambda_N=(\sigma w-h)/d\in[0,1]\), \(g_k\cdot v_{xy}+\sigma\sqrt3w/2=K\), and \(|j_k\cdot v_{xy}|\le d\lambda_N/2\).

Both hands use their actual reflected vertices and faces; the shell patch set is the corresponding reflection-invariant set. No target is substituted for another.

### 6.2 Zero factors, coplanarity and duplicate contacts

Let \(k_F(\theta)=n_{F,h}\cdot(\cos(\theta+\psi),\sin(\theta+\psi))+n_{F,w}\) and \(d_F=c_F-n_F\cdot\Delta_C\). The undivided equation \(b_\Omega f k_F=d_F\) retains every case:

1. If \(b_\Omega>0\) and \(d_F\ne0\), neither \(f\) nor \(k_F\) can vanish. A formal solution \(b_\Omega=d_F/(f k_F)\) must be positive and must still be the amplitude of the supplied state.
2. If \(b_\Omega>0\) and \(d_F=0\), the correct condition is \(f=0\) **or** \(k_F=0\). When \(f=0\), the point is \(\Delta_C\); it is a contact only if (19) holds there. When \(k_F=0\), the line \(\Delta_C+t d_\psi(\theta)\) lies in the plane, but only the actual point at \(t=b_\Omega f(\theta)\), checked by (19), is an observation. Unlike the original-centre macro case, this coplanar-generator case cannot be discarded.
3. Under the retained staged defaults, \(b_\Omega=0\) means \(\Omega=0\), hence \(C=0\) and \(v=0\). That point belongs to none of these finite targets. In a generalized zero-macro input with a nonzero supplied offset, membership would instead be the ordinary point test at that offset.

All the specified triangles are nondegenerate, including the endpoint crystal members; their nonzero ring edge and different-height tip/third vertex ensure positive G, and the notch area is explicitly positive. A zero barycentric coordinate denotes an edge, two denote a vertex. Count a geometric point once even if two fan triangles, neighbouring band triangles or several target labels contain it; retain the incident labels separately. Repeated observation angles at that same point are separate observation events, not additional spatial intersections.

Tangencies are included by (18)–(19); on a face interior a repeated angular root also satisfies \(f'k_F+fk'_F=0\). There is no need to assume every contact crosses a face. With \(b_\Omega>0\), the plane equation is a nonconstant trigonometric polynomial: horizontal normal components give nonzero second/fourth harmonics, and a purely vertical normal gives a third harmonic. Thus the whole nonconstant frozen curve cannot lie in a face plane, although particular generators can.

### 6.3 A sufficient obstruction when the offset is small

R0’s original theorem remains true: macro points miss every fan because all fan points satisfy \(R_\perp<|w|\). A quantitative version bounds when the translated curve still misses them. Put

\[
g_u=\min\left\{h-a\sqrt{1+\xi^2},\ H-r\sqrt{1+\xi^2}\right\}>0. \tag{20}
\]

These are the smaller lower-vertex radial-to-height gaps; the corresponding upper gaps are no smaller. For every convex combination within a fan, all vertex heights have the same sign, so the triangle inequality gives \(|w|-R_\perp\ge g_u\).

For any macro-cone point \(m\), however,

\[
|(m+\Delta_C)_w|-\|(m+\Delta_C)_{xy}\|
\le |\Delta_{C,w}|+\|\Delta_{C,xy}\|.
\]

Consequently

\[
|\Delta_{C,w}|+\|\Delta_{C,xy}\|<g_u
\quad\Longrightarrow\quad\text{no full-Z fan contact at any angle}. \tag{21}
\]

An entirely same-state sufficient condition is
\(\mu|\beta|\kappa^2/\sqrt2<g_u\), since the left side of (21) is at most \(\sqrt2\|\Delta_C\|\). These are sufficient exclusions, not sharp contact thresholds. At C=0 they recover the fan exclusion for every macro amplitude, without any small-amplitude restriction.

## 7. A fully specified same-state interior fan contact

This is an existence witness, not a preferred crystal or a natural alignment. Declare the PLUS zero face-complex limit, \(\mu=1\), \(\psi=0\), \(t_c=0\), and the unchanged defaults. Use the actual upper fan triangle

\[
F=[T_0,T_1,U_0],\qquad
P=\frac{T_0+T_1+U_0}{3}
=\left(\frac{\sqrt3a}{6},\ -\frac a2-\frac r3,\ \frac{2h+H}{3}\right). \tag{22}
\]

Its three barycentric weights are \(1/3\), so P is strictly in the finite triangle’s interior. We will specify one native state of norm exactly three, not independently assign a macro amplitude and an arbitrary chirality.

Set

\[
\kappa_*=3,\qquad A_*=0.618\frac34=0.4635,\qquad c_\ell=\cos(3\ell)=\cos(0.732)>0,
\]
\[
c_*=2\left[P-A_*c_\ell(1,0,1)\right],\qquad L_* =\|c_*\|. \tag{23}
\]

This candidate cross product is nonzero: its second component is \(-a-2r/3<0\). It is attainable at the prescribed norm. Indeed \(\|P\|<1/\sqrt3<1\), because P is an interior convex combination of vertices whose largest norm is the upper-tip norm \(\sqrt{r^2+H^2}=1/\sqrt3\). Also \(\sqrt2 A_*c_\ell<1\). Hence

\[
0<L_*\le2\bigl(\|P\|+\sqrt2 A_*c_\ell\bigr)<4<\frac92=\frac{\kappa_*^2}{2}.
\]

To remove any remaining arbitrary basis choice, write \(c_*=(c_1,c_2,c_3)\) and define

\[
p_* =\frac{(-c_2,c_1,0)}{\sqrt{c_1^2+c_2^2}},\qquad
q_* =\frac{c_*}{L_*}\times p_*,
\]
\[
X_* =\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\qquad
Y_* =\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\qquad
\boxed{\Omega_*=X_*p_*+iY_*q_*.} \tag{24}
\]

Every quantity in this state is specified by the exact constants above. Denominators are nonzero and radicands are positive. By the construction (14), its actual norm is three and its actual cross product is \(c_*\). Therefore the amplitude computed from this same state at \(t_c=0\) is exactly \(A_*\).

At the existing clock sector \(q=0\), \(\theta=0\), the macro term is nonzero and

\[
Z_{\rm total}(0)
=A_*c_\ell(1,0,1)+\frac12c_*=P. \tag{25}
\]

With the declared unit placement this is exactly finite-fan contact. The macro term by itself still lies on the original cone and misses every fan. No observer coefficient, lock, geometric dimension or new scale was fitted. The state was deliberately constructed within the common-state constraint to establish existence; neither spontaneous alignment nor recurrence reachability is claimed. The statement is exact observer mathematics, not a floating-point contact certification.

At harmonic-zero angles \(\theta=\ell+\pi/6+j\pi/3\), any frozen state instead gives the single spatial point \(v=\Delta_C\). If that point lies in a target, all six such angles repeat its contact. That is a separate possible mechanism, governed by (19); it does not supply six spatial routes. The witness (25) does not use it. For a nonzero staged amplitude, the angular derivative at those zeros can be nonzero even though their positions coincide, which also does not establish physical flow.

## 8. Symmetry, samples and supplied evolving observations

### 8.1 What survives the translation

Let \(Q(v)=v_x^2+v_y^2-w^2\), let \(R=R_z(2\pi/3)\), and let \(H_z=\operatorname{diag}(1,1,-1)\). For a frozen nonzero state,

\[
Q(v-\Delta_C)=0,\qquad
Q(v)=Q(\Delta_C)+2b_\Omega f(\theta)
\left[\Delta_{C,xy}\cdot e_{\theta+\psi}-\Delta_{C,w}\right]. \tag{26}
\]

The original-centre cone condition is generally lost. For a whole nonconstant frozen curve it survives only when \(\Delta_C=0\), as the distinct second/fourth and third harmonics in (26) force each offset component to vanish. Individual points may still satisfy it accidentally.

The exact surviving geometric symmetries are

\[
v(\theta+2\pi/3)=\Delta_C+R[v(\theta)-\Delta_C],
\quad
v(\theta+\pi)=\Delta_C+H_z[v(\theta)-\Delta_C]. \tag{27}
\]

Thus the full frozen curve still has threefold symmetry about its **translated** axis, and vertical pairs about the plane \(w=\Delta_{C,w}\). Covariance about the crystal’s original axis requires \(\Delta_{C,xy}=0\); pairing across the original middle plane requires \(\Delta_{C,w}=0\). A translated pair can be entirely above or entirely below that middle plane. Contact sets with the fixed crystal need not retain the curve’s translated symmetries.

R1’s pure-macro threshold intervals and its two-amplitude sampling formula therefore do not automatically survive. More strongly, consider native scalings \(q_s\Omega_*\) of the witness. Its macro norm stays bounded by \(\sqrt2\,0.618\) at the fixed time and unit scale, while its nonzero chiral offset grows as \(q_s^2c_*/2\). For sufficiently large \(q_s\), the entire curve leaves every bounded target region. It has a fan hit at \(q_s=1\) and none for all sufficiently large scales. A “larger native state always preserves contact” interval theorem is false for full Z.

At C=0, the translated cone reduces to the original one and all R1 pure-macro results recover with effective amplitude \(b_\Omega=\mu\alpha A_\Omega\), positive under the retained defaults. At \(\Omega=0\), the actual staged formula gives \(A=C=Z_{\rm total}=0\); this agrees with zero output for that state but must not be confused with historical constructor-zero storage, which can store zero readouts even for nonzero supplied states. [Z:268–297]

### 8.2 Ambient reflection is not a channel permutation

Reflecting the plotted curve and crystal together by S is a legitimate geometric comparison. It sends the offset to \(S\Delta_C\), exchanges the two crystal hands and reflects the finite notch set. It does not specify a native state transformation that makes the plotted offset obey that Cartesian law.

The native source laws are different: conjugation keeps \(\kappa,A\) fixed and sends \(C\mapsto-C\); a channel permutation P sends \(C\mapsto\det(P)PC\). In the actual face-state action of a shell symmetry G, the channel-area triple obeys \(C'=(\det G)(\det P)PC\). Specifically, the vertical shell reflection induces \(\Omega'=-P_{AC}\overline\Omega\) and \(C'=P_{AC}C\), an A/C slot exchange, not the Cartesian matrix \(S=\operatorname{diag}(-1,1,1)\) applied to the plotted triple. Cyclic channel permutation likewise differs from ambient rotation of one arrow. [A04:409–508]

Consequently no native chirality sign or channel relabelling is silently identified with the crystal hand, and no dynamical symmetry is inferred merely from the geometric group. The comparison map is unchanged.

### 8.3 The actual clock and generic pointwise rule

For the complete \(N=12\), step-one orbit, \(\theta_q=\pi q/6\). Keep the existing lock and define \(c_\ell=\cos(3\ell)\), \(s_\ell=\sin(3\ell)\). The harmonic factors remain

\[
(f_q)_{q=0}^{11}=(c_\ell,s_\ell,-c_\ell,-s_\ell,
c_\ell,s_\ell,-c_\ell,-s_\ell,c_\ell,s_\ell,-c_\ell,-s_\ell),
\]
\[
v_q=\Delta_C+b_\Omega f_q
(\cos(\pi q/6+\psi),\sin(\pi q/6+\psi),1). \tag{28}
\]

Substitute these actual points into (18)–(19), separately for each target. In particular their height signs are determined by \(\Delta_{C,w}+b_\Omega f_q\), not by the macro sign alone, and their total horizontal azimuths are not the macro azimuths after adding a transverse offset. The twelve sample positions need not repeat in contact-equivalent groups about the crystal. The original two-amplitude rule cannot be reused. The worked state supplies an exact hit at sector zero; it does not assert cyclic copies of that hit.

For other steps, use only residues \((q_0+nq_{\rm step})\bmod N\), whose orbit length is \(N/\gcd(N,|q_{\rm step}|)\), with \(\gcd(N,0)=N\). A finite observation list uses only its actual residues. Continuous frozen contacts at unsampled angles can be missed. [Z:46–82; A06:47–69,99–138]

For already supplied evolving data \((\Omega_j,t_{c,j},\theta_j)\), compute \(C_j=\Re\Omega_j\times\Im\Omega_j\) and the staged \(z_j=0.618\rho_j e^{-0.577t_{c,j}}\cos3(\theta_j-\ell)\) from that same state. The entire generic rule is the finite point test on

\[
v_j=\mu R_z(\psi)\left[\alpha z_j(\cos\theta_j,\sin\theta_j,1)+\beta C_j\right]. \tag{29}
\]

For supplied current-memory EMA data, replace only the scalar by
\(z_j=0.618\rho_j\cos3(\theta_j-\ell)+m_j\). There is no staged exponential in that variant and no implicit memory update in this point test. An EMA offset in z multiplies the angle-dependent macro direction; it is distinct from the constant frozen chiral translation. No memory evolution or trajectory replay is performed. [Z:202–265; A06:381–389]

Equation (17) is an angular derivative of a frozen comparison curve, not a velocity field or proof of deflection. Connecting discrete samples creates drawing segments, not intermediate observations, streamlines or measured flux. None of these results is a finding about a retained Z-total CSV or a native flow through the shell.

## 9. What is established and what remains conditional

The actual inside section has a positive, exactly located throat throughout the allowed family. The nested surrounding space has a central bulge instead. Three upper openings align angularly with the three finite shell notches, while tips, fan normals and lower footprint displacement prevent identifying all these objects as one set of channels. The finite-region distinctions include the endpoint lower vertex contacts in (11).

Full Z admits finite-fan contact from a single mathematically admissible native state, including a nonzero-macro default-clock witness, and has the exact finite-domain criterion (18)–(19) for all three target classes. Small offsets retain a proved fan exclusion. The frozen chiral term translates a curve; it does not itself supply steering dynamics, fluid variables or a new attachment law. The macro-only no-fan theorem remains intact in its original scope.

No global contact bifurcation diagram is needed for these conclusions. For a particular supplied state and comparison, its remaining contact angles are precisely the roots and finite-domain inequalities already given. Recurrence reachability of the constructed witness and a physical passage/flow interpretation remain unestablished; neither was assumed or investigated beyond this order. No follow-on task is issued. Work stops with this report for GPT and Hilmir’s review.

## Source locations

Line references are to the consulted local files. Historical verification and status language in them is not new computational evidence or an instruction to reopen completed work.

| Key | Relevant source locations |
|---|---|
| R0 | [Z and central crystal report][R0], definitions (1)–(6); sections and shell notches 83–95; components/channel distinction 99–139; fan exclusion 189–210; clearance 229–233 |
| R1 | [Macro middle-band report][R1], §§2–4 continuous sections, finite-face criterion and macro thresholds; §§5–7 worked reference, sampling and scope |
| G | [geometry.py][G], 16–49 host constants/maps; 153–183 central section, centre-axis rotation and reflections |
| PC | [Paper C v1.0.1][PC], 193–209 central section; 241–283 notch vertices, planes, finite regions and non-cap distinction |
| RH | [Crystal host registration report][RH], 123–203 edge centres and lower-edge offsets; 209–243 ring/fan rules; 245–294 embedding, boundaries and inward halfspaces |
| VC | [verify_host_registration.py][VC], 44–79 vertex definitions and actual face lists, read as text only |
| CJ | [Candidate JSON][CJ], 18–25 original domain; 218–231 declared ring/face rules |
| HG | [Host geometry JSON][HG], 15–29 centre, axis and dimensions |
| SI | [Signed family identities][SI], 5–45 definitions/reflection/footprint map; 68–119 actual section vertices and determinant identities |
| FA | [Family analysis][FA], 29–43 candidate status and signed domain; 86–93 zero limits |
| Z0 | [Zero-state analysis][Z0], 18–27 surface versus vertex symmetry; 46–103 distinct zero limits and connectivity |
| GP | [Retained six-patch report][GP], **geometry only**, 51–130 finite notch coordinates, normals and inequalities |
| Z | [z_manifold.py][Z], 46–82 clock; 90–161 scalar/macro/blend; 189–199 same-state observation; 202–265 EMA; 268–297 constructor-zero record |
| RO | [readouts.py][RO], 7–17 raw cross product |
| ZD | [z_diagnostics.py][ZD], 166–182 Gram/bound accounting; 331–413 cylinder/torus display maps |
| FS | [face_state.py][FS], 22–35 frames/channel order; 60–80 decoder; 123–150 transport/area definitions |
| E | [Paper E v0.1.1][E], 52–76 definitions; 112–245 harmonic/cone/sampling; 247–323 chirality, sharp bound and common-state qualification |
| A04 | [Atlas 04 source packet][A04], 353–380 area slots/zero cases; 409–508 native versus ambient symmetry laws |
| A06 | [Atlas 06 source packet][A06], 47–69 clock reachability; 99–138 sampling; 381–389 frozen EMA distinction |

The three NASA Glenn reference pages linked in §4 were read for the bounded external comparison on 19 October 2026. No broad fluids review was undertaken.

[R0]: C:/Users/Notandi/.codex/reports/Z_AND_CENTRAL_TWISTED_HEX_CRYSTAL_GEOMETRIC_RELATIONSHIP_INVESTIGATION_v0.1.md:5
[R1]: C:/Users/Notandi/.codex/reports/Z_MACRO_MIDDLE_BAND_INTERSECTION_ANALYSIS_v0.1.md:5
[G]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py:153
[PC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md:241
[RH]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/CRYSTAL_HOST_REGISTRATION_REPORT.md:123
[VC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/verify_host_registration.py:44
[CJ]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/CANONICAL_CRYSTAL_CANDIDATE.json:218
[HG]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/HOST_GEOMETRY.json:15
[SI]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/SIGNED_FAMILY_IDENTITIES.md:68
[FA]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/TWISTED_HEX_FAMILY_ANALYSIS.md:29
[Z0]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/ZERO_STATE_ANALYSIS.md:46
[GP]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md:51
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:90
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[ZD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py:166
[FS]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py:22
[E]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md:279
[A04]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md:353
[A06]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_06_z_observer/TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md:47
