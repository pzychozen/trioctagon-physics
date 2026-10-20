# Z and the Central Twisted Hex Crystal — Geometric Relationship Investigation v0.1

19 October 2026 · Exploratory research for Hilmir and GPT

**Finding.** There is a meaningful threefold geometric compatibility, an exact historical gap-triangle shape relationship, and a shared shell axis available for a declared coordinate placement. There is no recovered equation attaching Z to the crystal. A stronger distinction follows algebraically: **under centre alignment, axis alignment and uniform scaling, macro-Z observation points cannot intersect any of the refined crystal’s six upper/lower triangular fans.** Their radial-to-height ratios are strictly smaller than the macro cone’s. This result concerns macro points, not the general blended vector or renderer-added connecting segments, and does not exclude other explicitly defined placements.

The authoritative checkout was `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`, HEAD `3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`. Source identifiers below link to exact files; following numbers identify line spans. **Recovered** denotes existing definitions/results; **Derived here** denotes algebra from those unchanged definitions; **Conditional** denotes a placement convention, not an adopted model. No crystal member or hand is selected.

## A. Recovered geometry

### The octagons and the central axis

Write

\[
s=\sqrt2-1,\quad d=1-\frac{\sqrt2}{2},\quad
r=\frac{\sqrt3}{6},\quad O=(0,r,0).
\]

The width-one local octagon has vertices
\[
(-\tfrac12,-\tfrac s2),(-\tfrac s2,-\tfrac12),
(\tfrac s2,-\tfrac12),(\tfrac12,-\tfrac s2),
(\tfrac12,\tfrac s2),(\tfrac s2,\tfrac12),
(-\tfrac s2,\tfrac12),(-\tfrac12,\tfrac s2).
\]
For local coordinates \((u,z)\), its three folded images are
\[
P_1=(-\tfrac14-\tfrac u2,\tfrac{\sqrt3}{4}-\tfrac{\sqrt3u}{2},z),\quad
P_2=(u,0,z),\quad
P_3=(\tfrac14-\tfrac u2,\tfrac{\sqrt3}{4}+\tfrac{\sqrt3u}{2},z).
\]
Their common threefold axis is **\(O+\mathbb R e_z\)**, not the global line \(x=y=0\). The welded shell has 18 vertices, 21 edges, three octagonal faces and two nine-edge boundary loops. It is an open annulus with point group \(D_{3h}\). For \(|z|\le s/2\), its section is the perimeter of a side-one equilateral triangle; the axis passes through the enclosed region, not through shell material. [G:16–49,153–183; PC:193–209,289–306,348]

### Historical construction and its exact idealization

The retained historical note describes extracting an octagonal gap triangle, translating its base to a helper-chord midpoint, reflecting it, then copying the pair through 120° rotations. The originating extraction is testimony retained in that note; `tri_oct.py` starts from the resulting numerical triangles. It rotates about the **global Y axis**, despite the earlier apex-pivot wording. [HN:27–61,66–83; HC:7–28]

The source prototypes are \((\pm a_h,\pm b_h,0)\) and apex \((0,\pm c_h,p_h)\), with matched height signs, where
\[
(a_h,b_h,c_h,p_h)=(0.27059805,0.38268343,0.92387953,0.46868957).
\]
An exact idealization is
\[
b_h=\sin(\pi/8),\quad c_h=\cos(\pi/8),\quad
a_h=b_h/\sqrt2,\quad p_h=\sqrt6\,b_h/2.
\]
Rotating these two prototypes generates all six primitive triangles and 18 vertices. Three diameters supply six base endpoints on each regular hexagonal ring. Upper/lower footprints are aligned; the twist is in the **connections**, not a rotation between those rings. The decimals and floating rotations must remain distinct from this radical idealization. [R:44–68; HC:13–58]

**Derived shape correspondence.** The ideal primitive has sides \((2b_h,2b_h,\sqrt2b_h)\). Dividing by the original octagon width \(2c_h\) gives \((s,s,d)\), exactly the accepted shell notch’s side lengths and tip angle \(\arccos(3/4)\). This establishes congruent triangle shape after normalization, not unchanged position or a registration of the complete crystal. The historical apex height/triangle-side ratio \((2+\sqrt2)/3\) differs from the host edge-centre target ratio 1, already excluding their centred one-scale fit. [HN:162–164; PC:243–269; R:112–121]

The literal side faces are \((T_i,T_{i+1},B_{i+1})\), \((T_i,B_{i+1},B_{i+2})\); they differ from the comment’s intended quad split. Together with six diameter primitives and twelve nearest-apex caps, the historical object has \(V/E/F=18/60/30\), a branching boundary, nonmanifold vertices and crossings. The later audit reports twelve crossing face pairs, correcting the note’s six-only account. Its literal face complex has only \(C_1\) symmetry; the ideal vertex scaffold has \(D_{3h}\). It is not an embedded enclosing surface. [HC:60–89; R:70–110]

### The later proposed family

Use **\(\tau\)** for the crystal parameter called `t` in its sources, reserving \(t_c\) for clock time. Put
\[
a=d/2,\quad h=s/2,\quad H=1/2,\quad |\tau|\le h,
\quad J(x,y)=(-y,x),\quad A_\tau=I-(\tau/r)J.
\]
Let \(e_i=(\cos\theta_i,\sin\theta_i)\), \(\theta_i=-\pi/2+i\pi/3\), and \(n_k=e_{2k}\). All following coordinates are **relative to O**:
\[
T_i=(ae_i,h),\quad B_i=(aA_\tau e_i,-h),\qquad
U_k=(rn_k,H),\quad L_k=(rA_\tau n_k,-H).
\tag{1}
\]
Here \(i\bmod6\), \(k\bmod3\), in panel order \((P_2,P_3,P_1)\). This generates all 18 vertices exactly. The sources’ canonical coordinates are twice these centred physical coordinates, so canonical apex heights ±1 mean physical heights ±1/2. [F:34–43; SI:5–30; VC:44–79]

Upper tips are the highest-horizontal-edge centres. Lower tips remain on their corresponding finite lower edges, offset by \(-\tau Jn_k\), at distance \(|\tau|\) from their centres. Exactly,
\[
A_\tau=\sqrt{1+(\tau/r)^2}\,R_{-\delta},\qquad
\delta=\arctan(\tau/r),\qquad \alpha_{\rm crystal}=\cos\delta.
\]
Thus the lower ring and apex triangle expand and rotate together. The lower-edge-contact condition, ring placements and face connections are **previously proposed assumptions**. The host does not select \(\tau\); \(\alpha_{\rm crystal}\) is unrelated to the Z blend weight. [R:154–228; SI:32–50]

For PLUS, the band triangles are
\[
(T_i,T_{i+1},B_{i+2}),\qquad (T_i,B_{i+2},B_{i+1}).
\tag{2}
\]
Each upper fan consists of \((T_{2k-1},T_{2k},U_k)\) and \((T_{2k},T_{2k+1},U_k)\); the lower rule substitutes B and L. Consequently “three up/three down” means **six two-triangle fans**, not six individual faces. The diameter primitives are absent. The +1 band connections and +2 tessellation diagonals are distinct roles; their skew quads are not planar faces. MINUS reflects both geometry and connectivity; simply using the PLUS face list at negative parameter is a different family. [R:209–243; SI:21–30,68–99]

The proposed surface is an embedded open annulus, \(V/E/F=18/42/24\), with two six-edge boundaries. At nonzero magnitude each hand has point group \(C_3\), and the hands are not properly congruent. At zero the vertex set becomes achiral \(D_{3h}\), but each inherited surface remains chiral \(D_3\). The two surface limits differ, although their vertices coincide. Zero footprint twist therefore does not remove handed connectivity. [R:245–294; Z0:3–27,46–91]

### Sections and the distinction from shell measurements

For PLUS, let \(u=|\tau|\), \(0<\eta<1\), and section height \(z=h(1-2\eta)\). The actual band section alternates
\[
S_i=(1-\eta)ae_i+\eta aA_u e_{i+1},\qquad
D_i=(1-\eta)ae_i+\eta aA_u e_{i+2}.
\tag{3}
\]
The segments are \(S_iD_i,D_iS_{i+1}\). They form a simple star-shaped polygon with two six-point orbits and **\(C_6\) sectional symmetry**, generally twelve vertices. At \(u=0,\eta=1/2\), the two radii are \(\sqrt3a/2\) and \(a/2\). Interpolating corresponding indices instead gives \(I-\eta(\tau/r)J\), a different scaffold, not this surface. Above/below the band, sections lie in three separate fan sectors. None of these open surfaces defines a closed chamber or enclosed volume. [SI:52–119]

The shell’s three upper/lower **measurement triangles** are its chamfer notches, for example the upper seed at \(A=(0,\sqrt3/2,h)\) with edges \(d(-1/2,-\sqrt3/2,1)\), \(d(1/2,-\sqrt3/2,1)\). Their bases are measurement chords, not shell faces. Their three footprint axes have azimuths \(\pi/2+2k\pi/3\), displaced by 60° modulo 120° from the crystal’s upper-tip axes. Crystal fan triangles, historical translated primitives and these shell measurements are distinct objects. Registration of crystal tips to horizontal-edge centres does not identify entire fans with notch regions. [PC:241–285; GP:51–130; R:228,238–239]

## B. Recovered Z behaviour

### Native evolution, clock and observation

For \(\Omega\in\mathbb C^3\), the current native map first forms
\[
V=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL_3\Omega,
\qquad (L_3)_{ii}=-2,\quad (L_3)_{ij}=1\ (i\ne j),
\]
then preserves component magnitudes while updating phases by
\[
\varphi'_j=\varphi_j+\lambda_{\rm phase}
\sum_{k\ne j}\sin3(\varphi_k-\varphi_j).
\]
Here the phases are those of V; `arg0` assigns zero phase at exact zero. There is no clock, geometry input or dt in this map. Historical cores additionally permitted forcing and noise, separately from the retained unforced kernel. Three-channel permutation covariance is obtained by carrying k with the permutation; equal k is sufficient for fixed-parameter cyclic symmetry. A factor of three in phase synchronization does not alone establish a spatial rotation of the crystal. [D:1–4,12,27–44,57–104; E:78–110; A04:484]

The separate supplied clock has
\[
\theta=2\pi(q\bmod N)/N,\quad q'=(q+q_{\rm step})\bmod N,
\quad t_c'=t_c+dt.
\]
The angle is not the mean phase of Ω. The observer definitions are
\[
\kappa=\|\Omega\|,\quad \rho=\frac{\kappa}{1+\kappa},\quad
f=\lambda_{vp}\rho\cos3(\theta-\ell),
\]
\[
z_K=f e^{-\gamma t_c},\qquad
z_H=f+m,\quad m'=0.99m+0.01\frac{J_3}{1+|J_3|},
\quad J_3=\Im(\Omega_1\bar\Omega_2\Omega_3),
\]
\[
M=z(\cos\theta,\sin\theta,1),\quad
C=\Re\Omega\times\Im\Omega,\quad T=\alpha M+\beta C.
\tag{4}
\]
K is the staged scalar; H is the EMA scalar. Current observation advances neither Ω nor clock nor memory. EMA advancement is explicit. Historical defaults are \(N=12,q_{\rm step}=1,\lambda_{vp}=0.618,\ell=0.244,\gamma=0.577,\alpha=1,\beta=0.5\); they do not derive crystal dimensions. [Z:46–82,90–161,189–265; A06:47–69,445–497]

C carries relative phase: \(C_i=|\Omega_j||\Omega_k|\sin(\varphi_k-\varphi_j)\) in cyclic order. It is raw, quadratic, unchanged by common complex phase and reversed by conjugation. It has no imposed staged decay. \(J_3\) is a different, cubic observable, generally changed by cyclic relabelling or common phase. [C:7–17; E:247–277; A06:255–310]

There is already a precise geometric carrier for Ω: `face_state.py` decodes channel i as \(\Re\Omega_i(e_z\times n_i)+\Im\Omega_i e_z\) in its shell face tangent plane, using its own order A=P1, B=P2, C=P3 and three-dimensional face normals. C records three signed pairwise areas after the specified matched transport. These are channel slots, not automatically the Cartesian components of one ambient arrow. The crystal contacts share those shell panel labels, an exact incidence correspondence; no existing face-state operation places Z on the crystal. [FS:22–35,60–80,123–150; A04:353–380,409–508]

### Three upper and three lower extrema

For frozen nonzero positive amplitude \(A=\lambda_{vp}\rho e^{-\gamma t_c}\), the pure harmonic has extrema at \(\theta=\ell+k\pi/3\). With \(\xi_j=\ell+2j\pi/3\), their macro images are
\[
U_j^Z=A(\cos\xi_j,\sin\xi_j,1),\qquad
L_j^Z=A(\cos\xi_j,\sin\xi_j,-1).
\]
They form three vertical pairs, visited
\[
U_0^Z,L_2^Z,U_1^Z,L_0^Z,U_2^Z,L_1^Z.
\]
Negative scalar radius adds π to horizontal azimuth. Thus six scalar extrema give **three projected directions**, not six evenly spaced physical rays. The planar image is a three-petal rose; the macro satisfies
\[
M_x^2+M_y^2=M_z^2,\qquad \|M\|^2=2z^2.
\tag{5}
\]
These are existing Paper E results. The cone identity survives evolving amplitudes and either scalar law. The frozen pairing need not: an EMA offset has opposite-sign extrema only when \(|m|<|\lambda_{vp}\rho|\), and generally removes vertical pairing. [E:112–245,708–712]

At N=12 the frozen normalized samples are \((c,s_\ell,-c,-s_\ell)\) repeated three times, with \(c=\cos3\ell,s_\ell=\sin3\ell\). At the default lock the signs are ++−− and no continuous extremum is hit. Evolving Ω, time and memory further prevent a frozen angular symmetry from being a temporal periodicity. [E:135–150,194,243–245; A06:99–138]

### What the retained motion displays change

The retained historical runner records before each update, then changes Ω, clock, time and readouts in that order. Its constructor stores zero Z even for nonzero Ω; the initial origin is therefore not evidence of emergence from a spatial centre. [K:71–97,245–329]

| Display | Coordinates or operation | What moves |
|---|---|---|
| Direct Z | Stored T, M or C columns | The selected readout; straight connecting segments are renderer additions |
| Scalar cylinder | \((\kappa\cos\theta,\kappa\sin\theta,z)\) | Norm, supplied clock angle and scalar height |
| History torus | \(((R+r_t\cos\chi)\cos\theta,(R+r_t\cos\chi)\sin\theta,r_t\sin\chi)\), \(r_t=r_{\max}\rho\), \(\chi=\pi z/(2H_z)\), \(H_z=\max_{\mathcal H}\lvert z\rvert+10^{-9}\) | A history-normalized display, which can reposition old points when the history changes |
| Three channel curves | Fixed major azimuths \(2\pi(j-1)/3\), j=1,2,3; local tube angle \(\arg\Omega_j\), radius \(0.6[1+0.4\log(1+\lvert\Omega_j\rvert)]\) | Channel phases/magnitudes; these curves do not use Z or the clock |

[GD:4–76; TV:283–325; ZD:305–413; E:378–452]

The viewer additionally rescales each selected Z history by \(0.85r_{\rm frame}/D_{99}\), its own 99th-percentile norm denominator. Selecting macro versus chiral recomputes that scale. The trail callback moves the three channel endpoints through retained data; it does not shorten the full Z overlay. This separates state-derived motion, clock progression and display effects without replacing the author’s description of simulated energy movement with a flux law. [TV:649–703,826–846; E:454–469]

Two retained 2000-row Z-total CSVs are identified in [DATA1] and [DATA2], with \(g=0.664\) and \(0.667\). Their columns are `i,t,Zx,Zy,Zz,v_rec,J_eff`. Paper E records compatible phase-off replays and a nonfinite critical Z tail beginning at row 1279; those are earlier results, not new runs here. Exact original runtime/commit attribution remains unresolved. Original source locations and preservation provenance are retained in [PROV:5–19,41–44,95–121].

## C. Mathematical relationships

### Axis alignment is possible but does not define contact

**Conditional representation.** A placement
\[
\Phi(v)=O+\mu R_z(\psi)v,\qquad\mu>0,
\tag{6}
\]
aligns the observer origin and third axis with the crystal. It represents any finite Z vector or trajectory consistently in that frame, but its scale, azimuth and attachment meaning are additional choices. The frozen macro obeys \(M(\theta+2\pi/3)=R_{2\pi/3}M(\theta)\), so (6) intertwines its threefold rotation with the crystal’s. No consulted definition fixes \(\mu,\psi\), a crystal parameter, or a face assignment. [G:166–171; E:223–245,718–728]

Even the six extrema cannot be identified with the crystal’s tips by (6). Their transverse-radius/half-height ratio is 1; the upper crystal ratio is \(r/H=1/\sqrt3\). At nonzero \(\tau\), unequal upper/lower radii and relative rotation are additional obstructions. At zero, the two six-point skeletons share triangular-prism combinatorics, but not similarity class. This is a metric distinction, not a rejection of their threefold relationship. [E:170–188; MF:12–27,47–48; derived comparison]

### A stronger obstruction for all six crystal fans

**Derived here from (1) and (5).** Write \(R_\perp=\|(X-O)_{xy}\|\) and here let \(z=(X-O)_z\). At the upper ring and tip vertices,
\[
\frac{R_\perp}{|z|}=\frac a h=\frac1{\sqrt2}<1,
\qquad \frac rH=\frac1{\sqrt3}<1.
\]
For all permitted \(|\tau|\le s/2\), the lower vertices obey
\[
\left(\frac{R_\perp}{|z|}\right)^2_{\rm ring}
=\tfrac12(1+12\tau^2)\le 5-3\sqrt2<1,
\]
\[
\left(\frac{R_\perp}{|z|}\right)^2_{\rm tip}
=\tfrac13+4\tau^2\le\tfrac13+s^2<1.
\]
Every fan triangle has vertices in the same height half-space. For a convex combination with weights \(w_i\),
\[
R_\perp\le\sum_i w_iR_{\perp,i}
<\sum_i w_i|z_i|=|z|.
\]
Hence **every point of all twelve fan triangles has \(R_\perp<|z|\)**, for both hands, including zero. All macro points under (6) instead have \(R_\perp=|z|\). They cannot meet a fan, even away from extrema, for either scalar law. [VC:44–79; MF:63–77; Z:145–150]

This excludes only the specified macro points and continuous macro image. Straight segments inserted by a renderer need not lie on the cone and are not covered. It does not exclude band intersections, anisotropic placement, a different origin/axis, or T, whose chiral contribution generally takes it off the cone. Nor does it apply to the shell’s separate notch measurements; the prior finite-patch analysis concerns those other triangles. [E:217–221,329–337; GP:51–90,151–203]

### What threefold and handed compatibility actually establish

With Ω, time, parameters and current memory held fixed, C does not rotate when the clock angle shifts. Thus
\[
T(\theta+2\pi/3)-R_{2\pi/3}T(\theta)
=\beta(I-R_{2\pi/3})C.
\]
For nonzero β this vanishes precisely when C lies on the third **plotting** axis. Threefold macro covariance therefore does not automatically extend to the total. Channel cycling gives \(C\mapsto P_cC\), not the ambient matrix \(R_{2\pi/3}C\). Atlas 04 explicitly distinguishes these representations. [A06:499–524; A04:486–508; displayed difference derived here]

The crystal’s signed footprint determinant is \(\det(rn_k,rn_k-\tau Jn_k)=-r\tau\). Conjugation instead sends \(C\mapsto-C\), while a shell spatial reflection follows the established two-sign law \(C'=(\det G)(\det P)PC\). For example, the vertical mirror used to exchange crystal hands sends the shell area triple to the A/C-swapped triple; it is not simply conjugation or universal negation. [MF:29–45; A04:409–482]

No equation relates \(\tau\) to Ω, C or \(J_3\). Either crystal hand can be paired with a real state having C=0, or with conjugate states of opposite C, without changing a definition. At zero the surface remains chiral while its footprint determinant vanishes. Consequently a footprint sign, surface handedness, channel-area orientation and clock direction cannot be identified by one sign rule. The continuous frozen macro image itself has reflection symmetries; its traversal direction comes from the chosen clock progression. [Z0:18–27; E:227–243; Z:46–82]

### The centre has distinct geometry

**Derived here:** the refined surface has a uniform positive axial clearance. In either hand every band triangle’s horizontal vertex directions fit in an angular wedge of width at most \(2\pi/3\), and all vertex radii are at least a. Projection on that wedge’s bisector is therefore at least \(a\cos(\pi/3)=a/2\), including every convex combination. Fan triangles fit in narrower 60° wedges and satisfy the same bound. Thus
\[
R_\perp\ge a/2=d/4
\]
on the entire refined surface. At zero a central-band diagonal midpoint attains the bound. The open cylinder \(R_\perp<d/4\) is free of that surface; it is geometric clearance, not an enclosed vessel or proposed transport channel. The historical diameter primitives, by contrast, pass through their ring centres, so this global clearance cannot be transferred to the historical object. [SI:68–119; VC:44–79; HC:13–28]

Under (6), macro Z reaches the spatial centre only when z=0; its nonzero points cannot lie elsewhere on the axis. The frozen continuous pure harmonic has six origin passages, but the default twelve-sector samples miss those zeros. A total-vector zero can instead result from cancellation \(\alpha M=-\beta C\), with nonzero state. These are different meanings of “centre,” distinct again from constructor-zero storage. [E:135–150,196–219,303–345; K:71–97]

## D. Interesting findings

- **The threefold/sixfold distinction is exact:** the complete refined crystal is threefold while its band sections are sixfold; Z’s six scalar extrema project to three directions. These counts describe different mathematical objects.
- **The historical gap origin survives as a shape identity:** its normalized primitive triangle is congruent to a shell notch, although the later family replaces those primitive faces and changes the full registration.
- **Centre alignment is weaker than regional contact:** it provides a compatible frame, but the cone inequality proves that uniformly placed macro points miss all six refined fans.
- **Handedness persists without footprint twist:** the zero-parameter crystal surface remains chiral, independently of whether the channel chirality vanishes.

## E. Next bounded question

**For each existing crystal member and both hands, which centre-preserving, axis-preserving placements with separate positive transverse and axial scales and an azimuth rotation place the six frozen pure-macro extrema inside the six finite fan regions, with one consistent cyclic correspondence?** This is an exact finite-triangle membership problem. It would determine whether anisotropic calibration suffices, and how much freedom remains, without selecting a preferred parameter, changing the crystal or adding dynamics. It has not been undertaken here.

## Source locations and inspection record

Line spans refer to the files in the inspected checkout. The linked starting lines and named sections/functions locate substantive claims.

| ID | Exact source and locations |
|---|---|
| G | [kernel_physics/geometry.py][G], 16–49,153–183: octagon, fold maps, section and symmetry generators |
| PC | [Paper C publication v1.0.1][PC], §§6–9, lines 193–306; conclusion 348 |
| HC | [source_evidence/tri_oct.py][HC], 7–89: literal historical construction; 98–140: views and render layers |
| HN | [Historical reconstruction note][HN], 27–112,144–164: attributed construction history, idealization and original intersection account |
| R | [CRYSTAL_HOST_REGISTRATION_REPORT.md][R], 44–121: historical corrections; 123–294: exact host, candidate and proof |
| VC | [verify_host_registration.py][VC], 11–18,44–79: coordinate and face definitions, read as text only |
| F | [TWISTED_HEX_FAMILY_ANALYSIS.md][F], 13–57,86–115: status, units and family distinctions |
| SI | [SIGNED_FAMILY_IDENTITIES.md][SI], 5–119: signed vertices, reflection and actual sections |
| Z0 | [ZERO_STATE_ANALYSIS.md][Z0], 3–91: zero vertex/surface symmetry and distinct limits |
| MF | [METRIC_FUNCTIONS.md][MF], 10–80: contact skeleton, determinant and vertex radii |
| CA | [CRYSTAL_SELECTION_ATLAS.md][CA], 3–49; [viewer source][CV], 102–126: parameter, hand and projection controls |
| GP | [Six-patch report][GP], **geometry only**, 51–130 and comparison 151–203: shell measurement triangles, not crystal fans |
| D | [kernel_physics/dynamics.py][D], 12,57–104: native map and zero convention |
| C | [kernel_physics/readouts.py][C], 7–17: raw channel area |
| Z | [kernel_physics/z_manifold.py][Z], 46–82,90–161,189–297: clock, scalar variants, vectors and constructor-zero record |
| ZD | [kernel_physics/z_diagnostics.py][ZD], 111–181,305–413: passive accounting and display adapters |
| FS | [kernel_physics/face_state.py][FS], 22–35,60–80,123–150: existing face carrier and transported areas |
| E | [Paper E v0.1.1][E], §§3–12,15,19–20: equations, frozen geometry, displays, retained trajectories and open spatial attachment |
| A06 | [Mathematical Atlas Entry 06][A06], §§1–7,9,15–18: current observer and qualified transformation laws |
| A04 | [Mathematical Atlas Entry 04][A04], §§11–14: existing channel/ambient distinction and spatial reflection laws |
| K | [Retained staged model_core.py][K], 71–97,133–230,245–329: historical state, update and recording |
| H | [Retained EMA model_core.py][H], 169–223: separate historical scalar |
| GD | [Retained geometry_3d.py][GD], 4–76: cylinder, history torus, direct vector |
| TV | [Retained toy_3d_triocta.py][TV], 283–325,649–703,826–846: channel torus, scale, selection, endpoint callback |
| AT | [Retained analysis_tools.py][AT], 93–117: direct Z trajectory plot |
| PROV | [source_provenance.json][PROV], 5–19,41–44,95–121: original source and dataset locations |
| DATA1 | [Subcritical CSV][DATA1], header and initial rows; [saved summary][DS1], 1–17 |
| DATA2 | [Critical CSV][DATA2], header and initial rows; [saved summary][DS2], 1–17; E:535–569 for earlier reproduction and failure boundary |

Existing figures visually inspected: [historical versus proposed crystal][FIG1], [full host embedding][FIG2], [both hands at the illustrative s/4 member][FIG3], [macro cone][FIG4] and [four distinct Z displays][FIG5]. The atlas documentation and viewer source were read; the viewer was not launched. Its parameter slider changes geometry, not time. The s/4 figure is an existing illustration, not a selection.

Execution stayed within the order: filesystem/source reads, existing-image inspection and written algebra; one report saved outside the repository. No Python, project imports, tests, simulations, numerical experiments, application or UI execution, publication work, commits or pushes. No original files were altered by this investigation, and no SRG research was used to infer a Z/crystal relationship. Tracked Git status was empty at inspection; pre-existing untracked material was present and left in place. No full-tree byte-inventory claim is made. The exploratory values 0.002, 0.0002 and 0.0001 were not adopted.

[G]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py:16
[PC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md:193
[HC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/source_evidence/tri_oct.py:7
[HN]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/source_evidence/twisted_hex_crystal_research_note.md:27
[R]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/CRYSTAL_HOST_REGISTRATION_REPORT.md:44
[VC]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/verify_host_registration.py:44
[F]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/TWISTED_HEX_FAMILY_ANALYSIS.md:13
[SI]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/SIGNED_FAMILY_IDENTITIES.md:5
[Z0]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/ZERO_STATE_ANALYSIS.md:3
[MF]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/family_analysis/METRIC_FUNCTIONS.md:10
[CA]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/visual_selection/CRYSTAL_SELECTION_ATLAS.md:3
[CV]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/visual_selection/crystal_selection_viewer.html:102
[GP]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md:51
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:57
[C]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7
[Z]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46
[ZD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py:305
[FS]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py:60
[E]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md:52
[A06]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_06_z_observer/TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md:47
[A04]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md:353
[K]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/staged/model_core.py:71
[H]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/committed_ema/model_core.py:169
[GD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/staged/geometry_3d.py:4
[TV]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/staged/toy_3d_triocta.py:283
[AT]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/staged/analysis_tools.py:93
[PROV]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_provenance.json:5
[DATA1]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/preserved_runs/v3.7_p869bf44ed4_s2158500047_Z_total_series.csv:1
[DS1]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/preserved_runs/v3.7_p869bf44ed4_s2158500047_Z_total_summary.txt:1
[DATA2]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/preserved_runs/v3.7_p37abc4f4f9_s2158500047_Z_total_series.csv:1
[DS2]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/preserved_runs/v3.7_p37abc4f4f9_s2158500047_Z_total_summary.txt:1
[FIG1]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/02_historical_vs_canonical.png
[FIG2]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/06_full_host_embedding.png
[FIG3]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/twisted_hex_crystal_registration_v0.1/visual_selection/handedness_s_over_4.png
[FIG4]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/figures/03_macro_cone.png
[FIG5]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/figures/07_four_displays.png
