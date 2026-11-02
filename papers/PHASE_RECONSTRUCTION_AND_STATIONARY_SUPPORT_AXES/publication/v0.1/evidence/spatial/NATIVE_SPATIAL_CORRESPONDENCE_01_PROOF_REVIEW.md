# Native phase and the existing spatial decoder

**Task:** NATIVE_SPATIAL_CORRESPONDENCE_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Author / scientific review:** Hilmir Frímann Halldórsson / GPT  
**Execution and mathematical challenge:** Codex  
**Status:** Complete bounded proof review; ready for GPT/author discussion.

The recovered common phase has an exact spatial meaning in the already-adopted decoder: it rotates each face arrow in its own fixed tangent plane. The positioned axis of that rotation is exactly the corresponding stationary support line, not merely a parallel line. The decoder's outward normal points opposite to the support direction, so the signed rotation angle changes sign when expressed using that support direction.

This action on three labelled arrows is generally not one proper rotation of their three free vectors in the ambient frame. For the precise universal question in the order, such a rotation exists **if and only if the common phase is a multiple of \(2\pi\)**. The result concerns every admitted state at fixed labels; it does not classify accidental registrations of particular triples or rule out other material motions.

**Target A: verified.** The existing lossless decoder composes with the accepted reconstruction, its evolution commutes with the lifted native map, and its axes coincide with the accepted positioned support lines. No frame correction or fitted alignment was required.

**Target B: verified.** The universal proper-rotation classification is proved below. The observation comparison shows exactly what the recovered phase adds: face vectors and the phase-sensitive cubic innovation, while staged Z still depends on retained coordinates and its external settings. An EMA history also needs its initial memory and update ordering.

All defining source checks needed for these statements were completed. The fixed-gap report copy matches the prescribed accepted raw-file hash. The current order records acceptance of the preceding phase investigation; no separate copied GPT phase review was needed. Identifying an arrow with a material feature remains an additional author-dependent step, not a consequence of the common axis.

## 1. Inputs, scope and notation

Source IDs used below resolve to exact paths, versions and SHA-256 values in `CLAIM_SOURCE_LEDGER.md`. The native map and domain, retained coordinates, phase reconstruction, and adopted decoder are accepted inputs. This note proves their spatial composition, the positioned-axis match and the quantified rotation result. It does not re-prove phase convergence, potential descent, equality classification, coordinate minimality or return exclusions. [W, PH, PS, PC, NO]

Fix

\[
\epsilon=\frac1{10},\qquad g=\frac1{60},\qquad
\lambda=\frac1{300},\qquad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),\qquad
L=\mathbf1\mathbf1^T-3I.
\]

For clarity, call the complex prestage \(\widetilde\Omega\), reserving \(v_i\) for the decoded real face vectors:

\[
\widetilde\Omega=M\Omega,\qquad
M=I+\epsilon\operatorname{diag}(k-|\Omega|^2)+gL,
\]
\[
\delta_i=\lambda\sum_{j\ne i}
\sin\bigl(3(\operatorname{Arg}_0\widetilde\Omega_j-
\operatorname{Arg}_0\widetilde\Omega_i)\bigr),\qquad
F_i(\Omega)=e^{i\delta_i}\widetilde\Omega_i.
\tag{1}
\]

All kicks use the same prestage. The native convention \(\operatorname{Arg}_0(0)=0\) and the lambda-zero bypass are unchanged. The accepted invariant domain \(\mathcal D\) has \(9/10\le|\Omega_i|\le11/10\), ordinary phase width at most \(D_0=\pi/12\), and arbitrary common angle. Ordinary phases are not reduced modulo \(2\pi/3\). Prestage nonvanishing and all-iterate regularity on this domain are inherited. [PS, PC, PH]

Write

\[
y=\mathcal R(\Omega)=(s_1,s_2,s_3,a_{12},a_{13}),\qquad
s_i=|\Omega_i|^2,\qquad a_{ij}=\operatorname{Im}(\overline\Omega_i\Omega_j),
\]
\[
b_2=+\sqrt{s_1s_2-a_{12}^2},\quad
b_3=+\sqrt{s_1s_3-a_{13}^2},\quad
z(y)=\left(\sqrt{s_1},\frac{b_2+ia_{12}}{\sqrt{s_1}},
\frac{b_3+ia_{13}}{\sqrt{s_1}}\right)^T.
\tag{2}
\]

The exact retained image \(\mathcal Y\) is the closed joint-span domain

\[
\frac{81}{100}\le s_i\le\frac{121}{100},\quad
\eta_1=0,\quad
\eta_2=\arcsin\frac{a_{12}}{\sqrt{s_1s_2}},\quad
\eta_3=\arcsin\frac{a_{13}}{\sqrt{s_1s_3}},
\]
\[
\max(0,\eta_2,\eta_3)-\min(0,\eta_2,\eta_3)\le D_0,
\tag{3}
\]

with real principal arcsines. Thus \(\eta_i(y)=\operatorname{Arg}z_i(y)\), with positive square-root branches in (2). Independent area bounds are not substituted for (3). Boundary amplitudes, coincident phases, equal amplitudes and zero individual areas are retained. [PC, `prop:image`, `eq:radicands`]

The accepted reconstruction gives

\[
F(z(y))=\kappa(y)z(Gy),\qquad
\kappa(y)=\frac{F_1(z(y))}{|F_1(z(y))|}=e^{i\vartheta(y)},
\]
\[
y_{n+1}=Gy_n,\qquad u_{n+1}=u_n\kappa(y_n),\qquad
\Omega_n=u_nz(y_n),\qquad
u_0=\frac{\Omega_{1,0}}{|\Omega_{1,0}|}.
\tag{4}
\]

Here \(\vartheta=\operatorname{Arg}F_1(z(y))\) is the accepted continuous canonical ordinary increment. It includes prestage and synchronization contributions. The adjacent-state overlap angle instead equals \(\vartheta+\operatorname{Arg}[z(y)^\dagger z(Gy)]\) on this domain, and is not substituted for \(\vartheta\). [PH §§3, 5]

## 2. Source frame and positioned axes — Target A1

### 2.1. Dictionary and orientation

Use the common right-handed ambient coordinates, \(e_z=(0,0,1)\), \(r=\sqrt3/6\), and \(O=(0,r,0)\). The NRG appendix provides the exact frame table. The implementation source corroborates `FACE_ORDER = ("A=P1", "B=P2", "C=P3")` and `FRAME_ID = "face_center_tangent_ez_v1"`; its Python indices are 0, 1, 2, respectively. [NA, FS]

| Native index / face / Python index | Center \(c_i\) | Outward normal \(n_i\) | Tangent \(t_i=e_z\times n_i\) | Support direction \(g_{i-1}\) |
| --- | --- | --- | --- | --- |
| 1 / A=P1 / 0 | \((-1/4,\sqrt3/4,0)\) | \((-\sqrt3/2,1/2,0)\) | \((-1/2,-\sqrt3/2,0)\) | \((\sqrt3/2,-1/2,0)\) |
| 2 / B=P2 / 1 | \((0,0,0)\) | \((0,-1,0)\) | \((1,0,0)\) | \((0,1,0)\) |
| 3 / C=P3 / 2 | \((1/4,\sqrt3/4,0)\) | \((\sqrt3/2,1/2,0)\) | \((-1/2,\sqrt3/2,0)\) | \((-\sqrt3/2,-1/2,0)\) |

The fixed-gap report uses centered coordinates \((X,Y,w)\) with \(e_w=e_z\), and explicitly identifies their origin as this same uncentered \(O\). Its planar operator \(J(X,Y)=(-Y,X)\) has the same positive orientation as \(e_z\times\). Its definitions

\[
e_j=\bigl(\cos(-\pi/2+j\pi/3),\sin(-\pi/2+j\pi/3),0\bigr),
\qquad g_k=e_{2k+1}
\]

give exactly the last column. Its centered support \(\mathbb Rg_k\) becomes

\[
L_k=O+\mathbb Rg_k
\tag{5}
\]

in the decoder frame. This match uses the defining reference/PLUS direction labels, with a translation of origin only; no reflection, fitting or channel permutation is performed. The report's other \(n_k=e_{2k}\) denotes hexagon directions, not these decoder normals. Here \(L_k\) always denotes a support line, not the report's separate lower fan-vertex label. [FG §1 and §3; FGR §§2–3]

The exact frames come from NA's defining table. FS was read, never imported: it constructs a folded mesh at module import. Its code corroborates the frame/decoder route and labels, but this task does not claim to have independently executed that construction or certified floating-point decoding.

### 2.2. Positioned-line proof

Direct subtraction of the common origin gives

\[
c_1-O=(-1/4,\sqrt3/12,0),\quad
c_2-O=(0,-\sqrt3/6,0),\quad
c_3-O=(1/4,\sqrt3/12,0).
\]

Multiplying each listed normal by \(r\) gives the same vectors, and comparison with the support column gives

\[
\boxed{n_i=-g_{i-1},\qquad c_i-O=r n_i.}
\tag{6}
\]

Consequently, with no unverified offset,

\[
\boxed{\ell_i:=c_i+\mathbb R n_i
=O+(r+\mathbb R)n_i
=O+\mathbb Rg_{i-1}=L_{i-1}.}
\tag{7}
\]

The lines therefore coincide as positioned, unoriented sets. This is stronger than equality of directions. They remain three different stationary lines through \(O\); the result does not collapse them into one common axis.

Let \(R_n(\chi)\) be the right-hand proper rotation with Rodrigues convention

\[
R_n(\chi)=\cos\chi\,I+\sin\chi\,[n]_\times
+(1-\cos\chi)nn^T,\qquad [n]_\times v=n\times v.
\]

Since \(n_i=-g_{i-1}\),

\[
\boxed{R_{n_i}(\chi)=R_{g_{i-1}}(-\chi).}
\tag{8}
\]

The affine rotations about the two descriptions of the axis also agree. Indeed \(R_{n_i}(\chi)(c_i-O)=c_i-O\), so for any ambient point \(X\),

\[
c_i+R_{n_i}(\chi)(X-c_i)
=O+R_{g_{i-1}}(-\chi)(X-O).
\tag{9}
\]

This verifies the origin and the sign together. The fixed-gap support is a stationary reference/attachment locus under its accepted conditional interpretation; equality (7) does not turn it into a recovered material rod or supply an attachment. [FG §3; FGR §§1–3, 6]

## 3. Decoder phase action and native evolution — Target A2

### 3.1. Losslessness and the signed rotation

Let \(W_i=n_i^\perp\). The adopted decoder and encoder are

\[
D_i(q+ip)=q t_i+p e_z,\qquad
E_i(v)=t_i\cdot v+i e_z\cdot v.
\tag{10}
\]

From the table, \(n_i\) is unit and horizontal, \(t_i=e_z\times n_i\), and

\[
t_i\cdot e_z=0,\quad \|t_i\|=1,\quad
n_i\times t_i=e_z,\quad n_i\times e_z=-t_i.
\tag{11}
\]

Thus \((t_i,e_z,n_i)\) is a right-handed orthonormal basis. Equations (10) give \(E_iD_i=I\), \(\|D_i\omega\|=|\omega|\), and
\(D_iE_i v=(I-n_in_i^T)v\) for ambient vectors. In particular \(D_iE_i=I\) on \(W_i\); it is a projector on arbitrary ambient data. This is the existing lossless tangent-state decoder, not an inverse from unrestricted nine-dimensional arrays. [NO `eq:decoder`; FS `decode_to_faces`, `encode_from_faces`]

For \(\omega=q+ip\), multiplication by \(e^{i\chi}\) gives real and imaginary parts \(q\cos\chi-p\sin\chi\) and \(q\sin\chi+p\cos\chi\). Applying (10) and (11),

\[
\begin{aligned}
D_i(e^{i\chi}\omega)
&=(q\cos\chi-p\sin\chi)t_i
+(q\sin\chi+p\cos\chi)e_z\\
&=\cos\chi\,D_i\omega+\sin\chi\,n_i\times D_i\omega\\
&=R_{n_i}(\chi)D_i\omega.
\end{aligned}
\tag{12}
\]

The last equality uses tangency, which eliminates the normal term in Rodrigues' formula. This is an exact algebraic identity for every complex \(\omega\) and real \(\chi\), including \(\omega=0\). That broader decoder identity does not extend (4), native equivariance across zero prestages, or the domain theorem to other coefficients or historical Z states.

For a vector based at fixed \(c_i\), its mathematical endpoint \(X_i=c_i+D_i\omega\) becomes

\[
X_i'=c_i+R_{n_i}(\chi)(X_i-c_i)
=O+R_{g_{i-1}}(-\chi)(X_i-O).
\tag{13}
\]

It rotates about exactly the stationary line (7), with \(c_i\) fixed. It lies in the unbounded affine tangent plane; it need not lie inside the finite octagonal face. The endpoint is not thereby a particle position, and (13) attaches no material feature to the line. [NO `sec:attachment`]

### 3.2. Commutation with the existing face update

Write \(D=(D_i)_i\), \(E=(E_i)_i\). The existing matched transport is

\[
T_{ij}=t_it_j^T+e_ze_z^T:W_j\to W_i,
\qquad T_{ij}D_j\omega=D_i\omega.
\]

It is an isometry between the two tangent planes and rank two on ambient vectors; it is not one ambient proper rotation of arbitrary vectors. It retains the source convention `c3_matched_zero_phase_v1`. The accepted face evolution is

\[
\widetilde v_i=v_i+\epsilon(k_i-\|v_i\|^2)v_i
+g\sum_{j\ne i}(T_{ij}v_j-v_i),
\]
\[
v_i^+=\cos\delta_i\,\widetilde v_i
+\sin\delta_i\,n_i\times\widetilde v_i,
\qquad F_{\rm face}=DFE
\tag{14}
\]

on \(\bigoplus_iW_i\), with the same encoded prestage kicks as (1). Encoding the first line gives the original native prestage; (12) gives the second line. No independent vector recurrence or moving carrier is introduced. [NO `eq:faceupdate`; FS `transport`]

Use the current order's notation

\[
\mathscr D(y,u)=D(u z(y)),\qquad
\Phi(y,u)=(Gy,u\kappa(y)).
\]

Here \(\Phi\) denotes the lifted **update**. For \(y\in\mathcal Y\), \(|u|=1\), \(ED=I\) and the accepted regular reconstruction give

\[
\begin{aligned}
F_{\rm face}(\mathscr D(y,u))
&=DFE(D(u z(y)))\\
&=DF(u z(y))\\
&=D(u\kappa(y)z(Gy))\\
&=\mathscr D(\Phi(y,u)).
\end{aligned}
\]

Therefore

\[
\boxed{F_{\rm face}\circ\mathscr D=\mathscr D\circ\Phi.}
\tag{15}
\]

Losslessness is preserved: encoding \(\mathscr D(y,u)\) recovers \(u z(y)\), whose retained tuple and first-component unit factor recover \(y,u\). On this image, (15) describes exactly the same admitted native evolution in face coordinates.

Composing the accepted all-step formula with \(D_i\) gives, for every integer \(n\ge0\),

\[
\boxed{v_{i,n}=D_i\!\left[
u_0\left(\prod_{j=0}^{n-1}\kappa(G^jy_0)\right)
z_i(G^ny_0)\right].}
\tag{16}
\]

The empty product is one. All-iterate validity is inherited from the invariant domain and (4); no trajectory has been computed. Given \(y_0\) alone, different \(u_0\) give the family of face histories, just as they give the family of native histories.

### 3.3. Pure rephasing, the full update and representative choice

Pure common rephasing holds \(y\) fixed and changes \(u\) to \(e^{i\chi}u\). Equation (12) rotates each arrow about its own axis without changing its length. In a native step, \(y\) also changes. Choose the accepted real lift \(u_n=e^{i\theta_n}\), with \(\theta_{n+1}-\theta_n=\vartheta(y_n)\). Then

\[
\theta_{i,n}=\theta_n+\eta_i(y_n)
\]

is the accepted consistent ordinary phase of channel \(i\). Subtracting consecutive values gives the exact real equality

\[
\boxed{\theta_{i,n+1}-\theta_{i,n}
=\vartheta(y_n)+\eta_i(Gy_n)-\eta_i(y_n).}
\tag{17}
\]

It is not merely a congruence modulo \(2\pi\): the branch and ordinary-lift compatibility are the accepted PH §3.3 result. This subtraction makes no new branch or convergence claim.

In particular,

\[
v_{i,n}=\sqrt{s_{i,n}}
\bigl(\cos\theta_{i,n}\,t_i+\sin\theta_{i,n}\,e_z\bigr),
\qquad \|v_{i,n}\|=\sqrt{s_{i,n}}.
\tag{18}
\]

The actual angular change includes the change in relative phase \(\eta_i\), and the arrow length can change as well. Equivalently, since \(s_{i,n}>0\),

\[
v_{i,n+1}
=\sqrt{\frac{s_{i,n+1}}{s_{i,n}}}\,
R_{n_i}\!\left(\vartheta(y_n)+\eta_i(Gy_n)-\eta_i(y_n)\right)v_{i,n}.
\tag{19}
\]

This identity states the decoded step; it does not prescribe a continuous interpolating motion. On aligned inputs, \(\eta_i=0\) and the accepted canonical increment is zero, yet the aligned amplitudes can still relax before the fixed profile is reached. Their arrows retain direction while lengths change. A full native update is therefore not a pure common rotation. [PH §3.4]

For any specified alternate representative \(z_h(y)=h(y)z(y)\), \(|h|=1\), the accepted transformation is

\[
u_h=u/h(y),\qquad
\kappa_h(y)=\frac{h(y)}{h(Gy)}\kappa(y).
\]

Consequently

\[
\boxed{D_i(u_h z_{h,i}(y))=D_i(u z_i(y)).}
\tag{20}
\]

The change of representative alters the bookkeeping factors together and leaves every decoded vector and its endpoint unchanged. It is different from actually rephasing \(\Omega\). The canonical increment itself is not representative-independent; no new classification of representative choices is needed. [PH §6]

Equations (15)–(20) retain the closed boundaries and zero-area cases of \(\mathcal Y\). The roots and anchor are nonsingular there by the accepted positive-amplitude and positive-radicand bounds. The decoder uses no inverse area or phase difference. No zero-stratum extension of the native theorem is made.

## 4. The universal proper-rotation question — Target B1

For a fixed \(\chi\), consider precisely

\[
\exists Q_\chi\in SO(3)\quad
\forall\Omega\in\mathcal D\quad\forall i\in\{1,2,3\}:
\quad D_i(e^{i\chi}\Omega_i)=Q_\chi D_i(\Omega_i),
\tag{21}
\]

where \(Q_\chi\) is independent of \(\Omega\). The vectors are free vectors in the same fixed ambient frame. Centers, labels and mesh are not moved or permuted.

**Proposition.** Statement (21) holds if and only if \(\chi\equiv0\pmod{2\pi}\).

**Proof.** The first symbolic witness is \(\Omega=(1,1,1)\). Its component moduli are one and phase width zero, so it belongs to \(\mathcal D\). The original vectors are \(t_i\), and their rephased values are

\[
w_i=\cos\chi\,t_i+\sin\chi\,e_z.
\]

For \(i\ne j\), the frame table gives \(t_i\cdot t_j=-1/2\). An orthogonal \(Q_\chi\) must preserve these pairwise inner products, but

\[
w_i\cdot w_j=-\frac12\cos^2\chi+\sin^2\chi
=-\frac12+\frac32\sin^2\chi.
\tag{22}
\]

Thus \(\sin\chi=0\), leaving only \(0\) and \(\pi\) modulo \(2\pi\).

For the remaining half-turn, use \(\Omega=e^{i\pi/4}(1,1,1)\). Its moduli are again one and its phase width is zero. The common angle \(\pi/4\) is allowed: \(D_0\) limits the width, not the absolute orientation. Its three decoded columns form

\[
V=\left[\frac{t_1+e_z}{\sqrt2}\quad
\frac{t_2+e_z}{\sqrt2}\quad
\frac{t_3+e_z}{\sqrt2}\right]
=\frac1{\sqrt2}
\begin{pmatrix}
-1/2&1&-1/2\\
-\sqrt3/2&0&\sqrt3/2\\
1&1&1
\end{pmatrix},
\]
\[
\det V=\frac{3\sqrt6}{8}>0.
\tag{23}
\]

At \(\chi=\pi\), complex multiplication negates all three columns, so a proposed rotation would satisfy \(Q_\pi V=-V\). Since \(V\) is invertible, \(Q_\pi=-I\), whose determinant is \(-1\), contradicting \(Q_\pi\in SO(3)\). Equivalently, \(\det(-V)=-\det V\) reverses the oriented volume, which a proper rotation preserves.

Finally, if \(\chi\equiv0\pmod{2\pi}\), every complex component is unchanged and \(Q_\chi=I\) satisfies (21) for all states. This proves necessity and sufficiency. \(\square\)

These are symbolic state witnesses, not native-step experiments; no coefficients were changed. The second witness is essential to this proof because the first triple is planar and cannot detect proper orientation. For that particular planar first triple at \(\chi=\pi\), the proper rotation \(R_{e_z}(\pi)\) does send all \(t_i\) to \(-t_i\). This simple special case illustrates why failure of (21) does not exclude a proper registration for every particular triple. No classification of such special registrations is undertaken.

The individual rotations in (12) are proper rotations about their respective axes. Their failure to be the same universal ambient rotation does not conflict with any single-axis identity. Nor does either result select a rigid-body pose or establish what motion a material object can perform. The conditional support stabilizers in FG §3 answer a different question about an attached common rigid transformation; they are not substituted for the quantified free-vector test (21).

## 5. What the reconstructed phase adds to existing observations — Target B2

The raw channel quantities used by the historical staged Z are

\[
I(y)=s_1+s_2+s_3,\qquad
a_{23}(y)=\frac{b_2a_{13}-a_{12}b_3}{s_1},\qquad
C(y)=(a_{23},-a_{13},a_{12}).
\tag{24}
\]

For \(\Omega=q+ip\), the source convention gives \(C=q\times p\). This is the raw channel chirality, not the distinct ambient axial observable \(W=T_fC\), where \(T_f\) has the tangent columns. Equation (24) is a composition of accepted pair reconstruction with the existing readout. [PC `eq:thirdpair`; NO `eq:chiral`; Z §3, C09]

To avoid confusing the methods note's norm symbol with the reconstruction multiplier \(\kappa\), denote the norm here by \(N_\Omega=\sqrt I\). With the source's specified external observer settings, staged Z has the form

\[
K(N_\Omega)=\lambda_{\rm vp}\frac{N_\Omega}{1+N_\Omega},\quad
E_{\rm obs}(t)=e^{-\gamma t},\quad
H_{\theta_{\rm obs}}=
\cos[3(\theta_{\rm obs}-\ell)]
(\cos\theta_{\rm obs},\sin\theta_{\rm obs},1),
\]
\[
Z=\alpha K E_{\rm obs}H_{\theta_{\rm obs}}+\beta C,
\qquad X=O+\mu R_\psi Z.
\tag{25}
\]

All settings in (25) are observer/placement inputs, not replacement native coefficients. No schedule or preset is newly selected. [Z §3, C07–C10]

| Existing quantity | Native data required at a sample | Additional data for a history | What recovered common phase adds |
| --- | --- | --- | --- |
| Three decoded face arrows | \(y_n,u_n\), with fixed adopted frames | \(y_0,u_0\); accepted native update | Supplies the missing phase-dependent directions and their exact history (16). |
| Intensity \(I\) and raw chirality \(C\) | \(y_n\) through (24) | \(y_0\) and the closed map \(G\) | Nothing to their values; they are common-phase invariant. |
| Staged \(Z\) | \(y_n\) and specified observer settings | The same \(y_0\) plus the supplied exogenous observer schedule | No additional value information once those inputs are fixed. |
| Placed point \(X\), and its deterministic measurements against fixed geometry | Staged data and the prescribed placement | The observer/placement schedule and fixed measurement definitions | No additional value information; changing \(y\) can still change the point. |
| Cubic EMA innovation \(J\) | \(y_n,u_n\) | Reconstructed full-state history | Determines the phase-sensitive innovation. |
| EMA memory and resulting observation | Innovation plus current memory | Initial memory, specified filter settings and observation/update ordering | Does not infer unknown past memory or choose the ordering. |

More explicitly, if \(\sigma_n\) collects the specified external staged and placement data, (24)–(25) define \(Z_n=\mathcal Z(y_n;\sigma_n)\) and \(X_n=\mathcal X(y_n;\sigma_n)\). Equal \(y_0\) gives equal \(G^ny_0\); equal external schedules therefore give equal staged and placed histories on the admitted domain, even for different initial common phases and different face-vector histories. This uses accepted closure and the source's common-phase invariance. It is not a proof of an autonomous recurrence on Z alone. Frozen settings remove observer changes, not dependence on \(I(y)\) and \(C(y)\); those changes can move the point, while some particular changes can also cancel. [PC `thm:autonomy`; Z §§3, 8 C22]

For the separate EMA construction, put \(P(y)=z_1(y)\overline{z_2(y)}z_3(y)\). Unit modulus of \(u\) gives

\[
\Omega_1\overline\Omega_2\Omega_3
=uP(y),\qquad J=\operatorname{Im}[uP(y)].
\tag{26}
\]

Thus the reconstruction supplies its cubic innovation. The source normalizes \(J\) by \(1+|J|\) and uses stored memory with literal innovation weight 0.01. An EMA history additionally needs its initial memory and the prescribed placement of observations relative to updates; current native data cannot infer an unspecified past memory. No EMA has been advanced here. [Z §8 C24]

Native phase \(\theta_n\), observer angle \(\theta_{\rm obs}\), observer time \(t\), native update index \(n\), and the static geometry parameter \(\tau\) remain distinct. The historical Z01 coefficients \((\epsilon,g,\lambda)=(.05,.2,.001)\), \(k=(1,1,1)\), and Z02/Z03 coefficients \((1/10,1/5,17/100)\), \(k=(2,3,4)\), differ from this task's tuple. Their histories were neither replayed nor brought under the current domain theorem. [Z §2]

## 6. Verification, interpretation boundary and stopping point

The new standalone `exact_algebra.py` checked the transcribed support directions; normal/origin correspondence; right-handed tangent frames and projector; complex-phase rotation sign; affine axis/sign equality; the first witness's Gram identity; the second witness's nonzero signed determinant; and the raw chirality orientation. All eight identity groups passed in the existing `torment` environment, using Python 3.11.15 and SymPy 1.14.0. These are static symbolic checks, not native updates, geometry construction or observer advancement. The written proof supplies the universal quantifier, witness admissibility and all-step composition. Actual commands, results, identities and source checks are in `PREPARATION_REPORT.md` and the helper's JSON output.

**What is established.** Pure native common rephasing acts on each existing decoded face vector by its own normal-axis rotation. Those positioned normal axes equal the accepted corresponding stationary support lines, with the signed convention in (8)–(9). The accepted reconstructed state produces the exact face history and satisfies the commuting relation (15). The universal common proper rotation of all three labelled free vectors exists exactly for \(\chi\equiv0\pmod{2\pi}\). The source paths and required fixed-gap report identity were verified; no unresolved defining-source mismatch was found.

**What would be additional.** Identifying a named material feature with one of these based arrows or endpoints, prescribing registration to a stationary line, or extending the vector correspondence to a body-pose law would add information not present in the decoder. No moving support, hinge, filled central aperture, flow, force, emission, physical-energy assignment or material attachment has been introduced. The central broken opening arcs and filled host-notch measurement patches remain different objects. Their coincidence with neither an arrow nor an attachment is assumed.

**Next decision.** No further author input is needed to review or accept the mathematics in this note. If a subsequent discussion seeks a material identification, the focused question is: **Which named material feature, if any, is to be identified with the decoded face-A arrow based at \(c_1\)?** The proved relation already fixes that arrow's phase-action axis as stationary \(L_0\), with angle \(-\chi\) about \(g_0\); it does not choose the feature. This is an interpretation boundary for GPT/author discussion, not a request to reopen the support's stationarity or supply a complete motion story.

The close original enclosing sphere and separately discussed tight toroid remain distinct, as do two co-present arrangements and rapid alternation. No choice is made among them. Natural core motion and gravity–magnetism remain linked directions; outer structure and justified SRG integration remain available later; TORMENT remains separate and protected; Three-Way remains parked. Completed Z work, SRG reconstruction, fixed-gap geometry and return exclusions remain closed within their accepted scopes. [W §6; FG/FGR interpretation boundaries]

**Endpoint:** the bounded work is complete and ready for GPT/author review. No successor investigation, body-pose interpretation, paper, application change, repository edit, Git operation, push or publication was started.
