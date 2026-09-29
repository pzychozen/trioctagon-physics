# TriOctagon mathematical atlas — Entry 04

**Face-state, transport, and chiral area geometry · Source packet v0.1 · 29 September 2026**

The accepted bridge is a real isometry between the canonical state Ω∈ℂ³ and three selected tangent-vector planes. Encoding and decoding are exact inverses on that six-real-dimensional state space. Matched transport keeps the two coordinates unchanged, and raw chirality is the cyclic triple of transported signed parallelogram areas. These statements define a representation of the existing state, with no added physical field, point-position law, seam interaction or recurrence.

Authority: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`, frozen baseline `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`. Atlas 01–03 remain closed. Their provenance investigations and correction queues are not reopened or applied.

Companions: [exact checks](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_04_EXACT_CHECKS.py) and [results JSON](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_04_EXACT_RESULTS.json). Both are external to the protected source trees. This packet distinguishes analytic arguments, independent symbolic predicates, and finite-precision/API evidence.

## Source map

| ID | Source and scope |
|---|---|
| B_CODE | [face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py): D/E/T implementation, frame metadata, signed-area wrappers, FaceState ownership. |
| READOUTS | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py): raw `z_chiral`. |
| B_PAPER | [Paper B v0.1.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md): accepted definitions, proofs and interpretation limits. Section/equation locators below refer to this version. |
| B_SYMBOLS | [symbols and theorem correspondence](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/PAPER_B_SYMBOLS_AND_THEOREMS_v0.1.1.md): statement-to-source support. |
| GEOMETRY | [geometry.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py): the accepted Atlas-03 carrier and orientation, used without redoing its topology/provenance investigation. |
| DYNAMICS | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py): existing F₃ and deterministic phase convention. |
| NUMERIC_POLICY | [_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py): finite-input and conservative arithmetic guards. |
| BOUNDED_WRAPPER | [operating_region.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/operating_region.py): the optional existing wrapper selected by `FaceState.step(profile=...)`. |
| FACE_TESTS | [test_face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_face_state.py): inspected existing coverage and witnesses; not counted as a newly executed suite. |
| READOUT_TESTS | [test_readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_readouts.py): inspected raw scale and precision cases. |
| OLD_MODEL | [old model_core.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/model_core.py:214): direct cyclic imaginary products. |
| PRODUCTION_MODEL | [copied production model_core.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/model_core.py:206): comparison of the same historical observable, read only. |
| OLD_3D | [old geometry_3d.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_3d.py): stored-triple and torus displays. |
| OLD_TETRA | [old dual_tetra_mapper.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/dual_tetra_mapper.py): reordered/rescaled trajectory display. |
| OLD_CURVES | [old analysis_tools.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_tools.py:119): separate diagnostic curves. |
| OLD_CORRIDOR | [old tangent_corridor_analysis.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/tangent_corridor_analysis.py:11): planar finite-difference trajectory tangent, distinct from Paper B frames. |

## 1. Exact face frames: inherited geometry and adopted coordinates

Fix the face order

```text
0 = A = P1
1 = B = P2
2 = C = P3
```

Atlas 03 provides the width-one panel maps

\[
X_A(u,z)=(-\tfrac14-\tfrac u2,\tfrac{\sqrt3}4-\tfrac{\sqrt3 u}2,z),\quad
X_B(u,z)=(u,0,z),\quad
X_C(u,z)=(\tfrac14-\tfrac u2,\tfrac{\sqrt3}4+\tfrac{\sqrt3 u}2,z).
\]

The local octagon is centred at `(u,z)=(0,0)`. Hence `cᵢ=Xᵢ(0,0)`. Its positive material order gives `nᵢ=∂uXᵢ×∂zXᵢ`; these derivatives are orthonormal, so that cross product is already a unit normal. With `e_z=(0,0,1)` and `tᵢ=e_z×nᵢ`, the exact data are:

| Face | Centre `cᵢ` | Outward normal `nᵢ` | Tangent `tᵢ` |
|---|---|---|---|
| A | `(-1/4, sqrt(3)/4, 0)` | `(-sqrt(3)/2, 1/2, 0)` | `(-1/2, -sqrt(3)/2, 0)` |
| B | `(0,0,0)` | `(0,-1,0)` | `(1,0,0)` |
| C | `(1/4, sqrt(3)/4, 0)` | `(sqrt(3)/2, 1/2, 0)` | `(-1/2, sqrt(3)/2, 0)` |

Each nᵢ is horizontal and unit. Therefore `‖e_z×nᵢ‖=1`; the cross product is perpendicular to both factors. This gives all requested orthogonality relations. The vector triple-product identity gives

\[
t_i\times e_z=n_i,\quad n_i\times t_i=e_z,\quad
n_i\times e_z=-t_i.
\]

Thus the matrix with columns `(tᵢ,e_z,nᵢ)` is orthogonal with determinant +1. The three normals obey `n_A+n_B+n_C=0` and pairwise dot product −1/2; they are not a Cartesian basis.

The centres, outward normals, common vertical and panel order are inherited carrier data. Once outward orientation and positive e_z are fixed, tᵢ follows. **Paper B adopts** the interpretation “real part along tᵢ, imaginary part along e_z” and the comparison of planes by matched coordinates. Neither adoption is forced by the material octagon or by topology. [B_PAPER §2, equations (1)–(5), and Adoptions 1–2; B_CODE lines 24–36]

## 2. Complex-to-tangent decoding

Let `Wᵢ=nᵢ⊥⊂ℝ³` be the vector plane associated with cᵢ. It is the space of free tangent vectors, not the bounded octagon or the affine set of its points. For `z=q+ip`, define

\[
D_i(z)=q t_i+p e_z.
\]

Introduce the 3×2 matrix `Bᵢ=[tᵢ e_z]`. Then `Dᵢ(q+ip)=Bᵢ(q,p)ᵀ` and `BᵢᵀBᵢ=I₂`. For real r,s,

\[
D_i(rz+sw)=rD_i(z)+sD_i(w),\qquad
\|D_i(z)\|^2=q^2+p^2=|z|^2,
\]

\[
D_i(q+ip)\cdot D_i(a+ib)=qa+pb
=\operatorname{Re}(\overline z\,w).
\]

The two columns of Bᵢ are independent and lie in Wᵢ, which is two-dimensional. Therefore the image is exactly Wᵢ. On the product space

\[
W_{\mathrm{tan}}=W_A\oplus W_B\oplus W_C,
\qquad D=D_A\oplus D_B\oplus D_C,
\]

the inner product is the sum of the three face inner products. D has real rank six, preserves this sum and is onto: it is a real isometry `ℂ³≅W_tan`. The nine ambient storage entries obey three normal constraints; there are six independent real coordinates.

D includes no `+cᵢ` term. Even when a diagram draws an arrow with tail at cᵢ, its mathematical value remains a vector. For example `D_B(10)=(10,0,0)` is valid, although an endpoint `c_B+D_B(10)` lies far outside the width-one panel. No clipping, physical units or particle position follow from D. [B_PAPER §3, equation (6), Proposition 1; B_CODE `decode_to_faces`]

## 3. Encoding, exact inverse domain and ambient projection

For v∈Wᵢ define

\[
E_i(v)=v\cdot t_i+i(v\cdot e_z).
\]

Orthonormality immediately gives `EᵢDᵢ(q+ip)=q+ip`. The same formula can be extended algebraically to every ambient v∈ℝ³, but then

\[
D_iE_i(v)=\Pi_i v,\qquad
\Pi_i=t_it_i^T+e_ze_z^T=I-n_in_i^T.
\]

Indeed decompose `v=(v·tᵢ)tᵢ+(v·e_z)e_z+(v·nᵢ)nᵢ`; E discards the last term. Thus `Πᵢ²=Πᵢ=Πᵢᵀ`, its image is Wᵢ and its kernel is `span{nᵢ}`. The product identities are `ED=I₆` and `DE=diag(Π_A,Π_B,Π_C)` on the ambient nine-real-dimensional arrays. DE is the identity only after restricting to W_tan.

A useful exact falsifier is `v=Dᵢ(z)+nᵢ`. It encodes to z, but decoding returns `Dᵢ(z)`, losing the nonzero normal. The current **production-facing API does not silently accept arbitrary ambient vectors**: `encode_from_faces()` validates tangency and rejects substantive normal components. Its small roundoff allowance is described in §9, separately from this exact projection theorem. [B_PAPER §3, equation (7); B_CODE `encode_from_faces`]

## 4. Complex structure and signed area convention

Define the ambient linear map `Jᵢv=nᵢ×v`. The frame identities imply

\[
J_it_i=e_z,\quad J_ie_z=-t_i,\quad
J_i(qt_i+pe_z)=-pt_i+qe_z=D_i(i(q+ip)).
\]

In the positive ordered tangent basis `(tᵢ,e_z)`,

\[
[J_i]=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J_i^2=-I\quad\text{on }W_i.
\]

Ambiently the sharper statement is `Jᵢ²=nᵢnᵢᵀ−I=−Πᵢ`; Jᵢ kills nᵢ. This prevents applying the tangent identity to normal-bearing vectors. On Wᵢ, Jᵢ is orthogonal and D/E become complex-linear for multiplication by i and the selected Jᵢ.

For `v=q tᵢ+p e_z`, `w=a tᵢ+b e_z`, define

\[
\omega_i(v,w)=n_i\cdot(v\times w)=qb-pa
=\operatorname{Im}((q-ip)(a+ib)).
\]

The sign is fixed by `ωᵢ(tᵢ,e_z)=+1`. It is the signed **parallelogram** area; a triangle would introduce a factor 1/2. Its coordinate matrix is

\[
[\omega_i]=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-[J_i],
\]

because `ωᵢ(v,w)=gᵢ(Jᵢv,w)` and `ωᵢ(v,Jᵢw)=gᵢ(v,w)`, with `gᵢ(v,w)=v·w`. The form is alternating, nondegenerate and constant, hence closed on this vector plane. These are the compatible plane structures of Paper B; they are not a claim of a smooth field or complex structure across the material shell's creases. [B_PAPER §3, equations (4), (6)–(8)]

## 5. Matched transport: destination first, source second

The accepted convention is

\[
T_{ij}=t_it_j^T+e_ze_z^T=B_iB_j^T,
\qquad\text{source }j\ \longrightarrow\ \text{destination }i.
\]

Applying it to source coordinates gives

\[
T_{ij}(qt_j+pe_z)=qt_i+pe_z,
\qquad T_{ij}D_j(z)=D_i(z).
\]

Thus the tangent restriction is a real and complex isometry, retaining the same q,p. Multiplying outer products or using `BⱼᵀBⱼ=I₂` gives the **ambient matrix identities**

\[
T_{ij}T_{jk}=B_i(B_j^TB_j)B_k^T=T_{ik},\qquad
T_{ii}=\Pi_i.
\]

Further,

\[
T_{ij}^T=T_{ji},\quad T_{ij}^TT_{ij}=\Pi_j,\quad
T_{ij}T_{ij}^T=\Pi_i,\quad J_iT_{ij}=T_{ij}J_j.
\]

Each Tᵢⱼ has rank two, kernel `span{nⱼ}` and image Wᵢ. Its singular values are `(1,1,0)`. The restriction `Wⱼ→Wᵢ` has inverse Tⱼᵢ, whereas the ambient 3×3 matrix is singular. In particular it is not a full rigid rotation: it kills a unit normal, while a rotation preserves that vector's length. [B_PAPER §4, equations (9)–(10), Proposition 2; B_CODE `transport`]

## 6. Relationship to the canonical C3 rotation

Let

\[
R=\begin{pmatrix}-1/2&-\sqrt3/2&0\\\sqrt3/2&-1/2&0\\0&0&1\end{pmatrix},
\quad o=(0,\sqrt3/6,0).
\]

The accepted spatial point rotation is `x↦o+R(x−o)` and sends `A→B→C→A`. For numerical indices 0,1,2 define `Rᵢⱼ=R^((i−j) mod 3)`. It carries all three source basis vectors to their destination counterparts, so

\[
R_{ij}=t_it_j^T+e_ze_z^T+n_in_j^T
=T_{ij}+n_in_j^T.
\]

Therefore

\[
T_{ij}=\Pi_iR_{ij}=R_{ij}\Pi_j,
\qquad T_{ij}v=R_{ij}v\quad(v\in W_j).
\]

The restriction to Wⱼ matters: on nⱼ the first map gives zero and the rigid rotation gives nᵢ.

For a drawing with a point `cⱼ+v`, the corresponding point transformation is

\[
o+R_{ij}(c_j+v-o)=c_i+R_{ij}v=c_i+T_{ij}v,
\quad v\in W_j.
\]

This affine statement is distinct from transporting the free vector. For example `c_B=0`, so `T_CB c_B=0`, while the correct rotated centre is `c_C=(1/4,√3/4,0)`. Using T on centres cannot implement point rotation. [B_PAPER §§2,4; GEOMETRY `rotate_c3`]

## 7. Closed transport cycle and zero-relative-phase convention

Transport around `A→B→C→A` acts, rightmost first, by

\[
T_{AC}T_{CB}T_{BA}=T_{AA}=\Pi_A.
\]

On W_A this is the identity. Each step preserves the ordered two-component column `(q,p)ᵀ`, so tangent-coordinate holonomy is trivial. It is not the ambient identity on arbitrary 3D inputs; a normal component is removed at the first step.

The identifier `c3_matched_zero_phase_v1` names this frame match: select the canonical C3-related frames and insert no relative complex phase between them. It does not identify a transport time, physical connection, arbitrary surface path rule or seam dynamics.

A passive basis change illustrates what “zero” refers to. If the basis on face i is rotated by θᵢ, the unchanged vector's complex coordinate becomes `zᵢ′=exp(−iθᵢ)zᵢ`. Holding the geometric transport fixed, its coordinate multiplier becomes `exp(i(θⱼ−θᵢ))`. Around the cycle those angle differences telescope to zero. Independently rotating the frames and then resetting every multiplier to one would change the chosen transport, not merely its written coordinates. This is a coordinate observation, not a physical gauge construction. [B_CODE `TRANSPORT_ID`; B_PAPER §4 and §7, equations (22)–(23)]

## 8. The existing recurrence in face coordinates

Let `F₃` be the already accepted Paper-A update. Its pre-synchronization value is

\[
\widetilde\Omega_i=\Omega_i+\varepsilon(k_i-|\Omega_i|^2)\Omega_i
+g\sum_{j\ne i}(\Omega_j-\Omega_i),
\]

with real ε,g,λ and real labelled kᵢ. Applying D and using norm preservation and `TᵢⱼDⱼ=Dᵢ` gives

\[
\widetilde v_i=v_i+\varepsilon(k_i-\|v_i\|^2)v_i
+g\sum_{j\ne i}(T_{ij}v_j-v_i).
\]

Every term lies in Wᵢ. Encoding this expression recovers the existing complex expression term for term, including its `L₃` coupling. No additional face coupling or force has been chosen.

For the inherited phase step set

\[
\phi_i=\operatorname{Arg}_0(E_i\widetilde v_i),\quad
\delta_i=\lambda\sum_{j\ne i}\sin(3(\phi_j-\phi_i)),\quad
v_i^+=\cos\delta_i\,\widetilde v_i+\sin\delta_i\,J_i\widetilde v_i.
\]

`Arg₀(z)` is the argument when z≠0 and exactly +0 for every exact complex zero, including signed IEEE zeros in the runtime implementation. All increments are evaluated simultaneously from the same pre-synchronization state. If λ=0, the current phase step is defined directly as the identity. If a pre-state component is zero, both the complex amplitude reconstruction and this vector rotation return zero.

Since `Dᵢ(iz)=JᵢDᵢ(z)`, the complete map is exactly

\[
F_{\mathrm{face}}=D F_3 E\quad\text{on }W_{\mathrm{tan}},
\qquad E F_{\mathrm{face}} D=F_3.
\]

This is **EXACT_COORDINATE_CONJUGACY**. Ω remains the canonical dynamical state. These equations create no new recurrence and derive no coefficient, harmonic, clock or physical law from the shell.

The domain restriction is essential: for ambient normal-bearing inputs, the algebraic extension would first discard normals; the runtime encoder normally rejects such data instead. The deterministic zero-phase convention is also essential. Conjugacy carries it unchanged, including its zero-stratum limitations; it does not regularize that convention. [B_PAPER §5, equations (11)–(14); DYNAMICS `arg0`, `phase_sync`, `step3`]

## 9. FaceState ownership and finite-precision boundaries

The implementation follows a single-state ownership model:

| Entry point | Stored/evaluated data | Consequence |
|---|---|---|
| `FaceState(omega)` | Validates and copies Ω into complex128, derives vectors with `_decode`, marks both arrays read-only | Display vectors are derived from canonical Ω. |
| `step(config)` | Calls `dynamics.step3(self.omega, config)` once; constructs a new view from its returned Ω | No encode/decode feedback cycle. |
| `step(config, profile=...)` | Calls the selected existing bounded wrapper once; that wrapper calls its imported `step3` once on a valid request | Same recurrence, with existing validation/failure policy. |
| `from_faces(vectors)` | Calls `encode_from_faces` once, then the normal constructor | Explicit rounded initialization, followed by canonical-state evolution. |
| `vectors` | Fresh real 3×3 display array, ordinarily non-writeable | Not an independent mutable state or recurrence input. |

“Read-only” disables ordinary array mutation; the code does not claim a security boundary against deliberate low-level manipulation. The constructor copies valid inputs, so caller-array edits do not alias the stored state. A decode failure after a successful recurrence can prevent creation of the new view; the previous view remains unchanged. Frame metadata belongs to the face view, not to an initialization receipt for another subsystem. [B_CODE `FaceState`, lines 158–211; B_PAPER Appendix A]

`EXACT_COORDINATE_CONJUGACY` must be separated from `FLOATING_IMPLEMENTATION_BITWISE_IDENTITY`. Runtime frames contain rounded binary64 values of radicals. On this recorded interpreter, a simple round trip is

```text
Ω = (1,0,0)
initial real part:       0x1.0000000000000p+0
E_float(D_float(Ω))[A]:   0x1.fffffffffffffp-1
```

The mathematical identity remains true; its separately evaluated floating conversions are not bitwise inverses. Repeating those conversions could change a trajectory. The executed ownership checks disable encoding during ordinary steps, instrument the selected recurrence call, and compare stored Ω bytes against direct recurrence output over four steps on each of the plain and bounded paths. These finite cases pass. Source inspection explains why the implementation retains Ω rather than feeding derived vectors back through E. This is not a claim that a separately computed face formula matches the complex recurrence bit for bit for all inputs/platforms.

The numerical boundary is specific:

- `encode_from_faces` requires a finite real `(3,3)` input; decode requires a finite numeric complex triple. Booleans and strings are rejected. Face indices must be non-Boolean integers 0–2.
- Tangency is checked using only participating horizontal normal coordinates. With `Kᵢ={k∈{x,y}: nᵢ,k≠0}` and `m=maxₖ∈Kᵢ |vₖ|`, zero m passes; otherwise the code tests `abs(fsum(nₖ vₖ/m)) ≤ 8ε_machine fsum(abs(nₖ vₖ/m))`. The tolerance is homogeneous, has no absolute floor, and gains no slack from a large z component. For face B the normal y-coordinate must be exactly zero.
- Normal residuals indistinguishable from frame roundoff within that test can be lost in E. Larger residuals are rejected. This finite test is not the exact theorem “v∈Wᵢ”.
- Checked nonzero products reject subnormal or overflowing intermediates and nonzero underflow to zero; checked outputs reject nonfinite and nonzero subnormal results. Exact zero is allowed. No small-state threshold normalizes or deliberately zeros the result.
- `math.fsum` is used for checked sums, but near cancellation a zero/small binary64 result is not an exact-zero proof. The guards are conservative domain checks, not a universal accuracy theorem.
- The optional bounded profile requires its explicit identifier, ε=1/20, g=1/5, kᵢ∈[0,8] and actual input moduli at most 3; it retains existing failure checks. Plain `step()` does not silently select that profile.

These boundaries were recorded and tested, not changed. [B_CODE `TANGENCY_RTOL`, `_decode`, `encode_from_faces`, `step`; NUMERIC_POLICY; BOUNDED_WRAPPER]

## 10. Signed transported areas and the full skew matrix

For channels i,j, transport the second vector to the first plane before taking the area:

\[
A_{ij}=n_i\cdot[v_i\times(T_{ij}v_j)].
\]

Write `Ωᵢ=qᵢ+ipᵢ`. The transported pair in Wᵢ is `(qᵢtᵢ+pᵢe_z, qⱼtᵢ+pⱼe_z)`. Cross-product bilinearity and `tᵢ×e_z=nᵢ` give

\[
v_i\times T_{ij}v_j=(q_ip_j-p_iq_j)n_i,
\]

\[
A_{ij}=q_ip_j-p_iq_j
=\operatorname{Im}(\overline{\Omega_i}\Omega_j).
\]

This derivation uses the actual tangent frames, not a call to `z_chiral`. It immediately yields `Aⱼᵢ=−Aᵢⱼ` and `Aᵢᵢ=0`.

Put `x=Re Ω`, `y=Im Ω`, regarded as vectors in the ordered **channel-coordinate space** ℝ³. Then

\[
A=xy^T-yx^T
=\begin{pmatrix}
0&A_{AB}&-A_{CA}\\
-A_{AB}&0&A_{BC}\\
A_{CA}&-A_{BC}&0
\end{pmatrix}.
\]

This is a real skew matrix. The following rank/invariant consequences are derived here from this formula, rather than attributed to a numerical rank test. Let `Z=x×y`, `c=‖Z‖²`. With `[Z]_×w=Z×w`, the sign is `A=−[Z]_×`, so

\[
A^2=ZZ^T-cI,\quad A^3=-cA,\quad AZ=0,
\quad c=\|x\|^2\|y\|^2-(x\cdot y)^2.
\]

If Z=0 then A=0 and its rank is zero. If Z≠0, A² restricts to `−cI` on Z⊥, so rank(A)=2, `ker A=span{Z}` and `im A=Z⊥=span{x,y}`. These are the only possible ranks. Other basic invariants are

\[
\operatorname{tr}A=\det A=0,\quad \|A\|_F^2=2c,\quad
\det(\mu I-A)=\mu(\mu^2+c).
\]

The eigenvalues are `0,±i‖Z‖`; the singular values are `‖Z‖,‖Z‖,0`. These algebraic invariants do not imply that the recurrence conserves them. [B_PAPER §6, equations (15)–(16), for the area identity; the rank and polynomial identities above are direct Atlas-04 consequences]

## 11. Raw chirality: channel slots, zero condition and scale

Expanding the cross product directly gives

\[
x\times y=
\begin{pmatrix}x_By_C-x_Cy_B\\x_Cy_A-x_Ay_C\\x_Ay_B-x_By_A\end{pmatrix}
=\begin{pmatrix}A_{BC}\\A_{CA}\\A_{AB}\end{pmatrix}.
\]

Thus `Z_A=A_BC`, `Z_B=A_CA`, `Z_C=A_AB`, in precisely that cyclic order. Each slot is the signed comparison of a pair of channel states. It is not the Cartesian component of one ambient arrow merely because there are three slots.

Algebraically,

\[
Z=0\ \Longleftrightarrow\ x,y\text{ are real-linearly dependent}
\ \Longleftrightarrow\ A=0.
\]

Equivalently, Ω can be written `Ω=c r` with c∈ℂ and r∈ℝ³, including the zero state. For nonzero components this permits phases differing by π as well as a common phase. It does not force equal amplitudes, a balanced state, vanishing Ω, or all face vectors to be collinear in ambient space. For example `(1,−2,3)` has zero chirality and unequal signed real channel coordinates.

For any complex scalar c,

\[
A(c\Omega)=|c|^2A(\Omega),\qquad Z(c\Omega)=|c|^2Z(\Omega).
\]

The observable retains raw quadratic scale. It is a state-vector parallelogram area, with squared state-amplitude units if units were later assigned; it is not the fixed area of a material octagon. No normalization, decay envelope, conservation law or monotonicity claim is inserted. READOUTS computes the three cyclic determinants; `area_triple()` delegates to that same readout bit for bit. `state_area(i,j)` selects its signed component, and evaluates the complete readout even for a diagonal request before returning zero. [B_PAPER §6; READOUTS; B_CODE `area_triple`, `state_area`]

## 12. Global complex phase and its limits

For `Ω′=exp(iα)Ω`, the real and imaginary channel vectors become

\[
x'=\cos\alpha\,x-\sin\alpha\,y,\qquad
y'=\sin\alpha\,x+\cos\alpha\,y.
\]

At each face,

\[
v_i'=\cos\alpha\,v_i+\sin\alpha\,J_i v_i.
\]

This is a positive tangent-plane rotation about the specified outward normal. Norms are preserved. Expanding either the two-by-two determinant or `overline(exp(iα)Ωᵢ)exp(iα)Ωⱼ` gives

\[
A'=A,\qquad Z'=Z.
\]

These polynomial identities hold for every state, including zero components. Complex conjugation instead sends `A→−A`, `Z→−Z`. A common complex phase is a coordinate action here; no physical temporal evolution follows from it.

The invariance of this **observable** must not be confused with global common-phase equivariance of F₃. For λ≠0, the fixed zero phase enters neighbours' increments. An exact counterexample uses ε=g=0, `Ω=(0,1,1)`, `α=λ=π/6`. Originally all assigned phases are zero and the update leaves Ω unchanged. After multiplying the state by `exp(iα)`, the nonzero components have phase α, the zero still has assigned phase 0, and each nonzero increment is `λ sin(−3α)=−λ`. Both nonzero outputs are therefore 1. But multiplying the original output by `exp(iα)` gives `(0,exp(iα),exp(iα))`, a different state. The exact squared per-component discrepancy is `2−√3`; the recorded floating maximum discrepancy is approximately `0.5176380902050414`.

On nonzero pre-synchronization components the common shift cancels from phase differences. At λ=0 the phase step is the identity, so that zero qualification disappears. The conjugacy in §8 remains valid in all these cases because it carries the same convention. [B_PAPER §§5,7,9]

## 13. Spatial symmetries and pure channel relabelling

Fix the permutation-matrix convention: if a symmetry sends source face i to destination `π(i)`, then `P_{π(i),i}=1`. Thus `(PΩ)_{π(i)}=Ωᵢ`.

For an accepted spatial shell symmetry with orthogonal linear part G, act on points by `x↦o+G(x−o)` and on face vectors by

\[
v'_{\pi(i)}=Gv_i,\qquad n_{\pi(i)}=Gn_i.
\]

Every D3h element preserves the vertical line, so `Ge_z=ηe_z`, `η=±1`. For δ=`det(G)`, the cross-product transformation formula gives

\[
Gt_i=G(e_z\times n_i)
=\delta(Ge_z\times Gn_i)
=\delta\eta\,t_{\pi(i)}.
\]

Consequently the encoded coordinates satisfy

\[
\Omega'_{\pi(i)}=
\begin{cases}
\eta\Omega_i,&\delta=+1,\\
-\eta\overline{\Omega_i},&\delta=-1.
\end{cases}
\]

This explicitly explains the conjugate-linear improper actions. It is not an assumption of physical time reversal.

Both signs square to one inside the transport outer products, so `G Tᵢⱼ Gᵀ=T_{π(i),π(j)}`. Substitute that identity into the transformed geometric area:

\[
A'_{\pi(i),\pi(j)}
=(Gn_i)\cdot[(Gv_i)\times(GT_{ij}v_j)]
=\det(G)A_{ij}.
\]

Thus, independently of the readout implementation,

\[
\boxed{A'=\det(G)PAP^T.}
\]

Converting a skew matrix to its cyclic channel triple adds the orientation sign of the channel permutation. Equivalently use `(Px)×(Py)=det(P)P(x×y)`. Therefore

\[
\boxed{Z'=\det(G)\det(P)PZ.}
\]

`det(G)` arises from reversing ambient orientation in a face-area calculation; `det(P)` arises from reordering the three channel axes. They describe different operations, even when both are negative.

Let

\[
P_c=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\qquad
S=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\]

| Spatial generator | G | Induced P | η | State action | Area action | Chirality action |
|---|---|---|---:|---|---|---|
| 120° rotation R | The matrix in §6 | P_c | +1 | `P_c Ω` | `P_c A P_cᵀ` | `P_c Z` |
| Vertical reflection V | `diag(−1,1,1)` | S, exchanging A/C | +1 | `−S conjugate(Ω)` | `−S A Sᵀ` | `S Z` |
| Horizontal reflection H | `diag(1,1,−1)` | I | −1 | `conjugate(Ω)` | `−A` | `−Z` |

The independent checker constructs all twelve accepted `G=R^r V^v H^h`, derives their face permutation from their action on the exact normals, and verifies frame, centre, transport, state, area and Z laws symbolically for arbitrary real qᵢ,pᵢ. It does not borrow the implementation's `area_triple` to establish these laws. Atlas 03's group classification is used, not reopened.

**Pure relabelling has a different law.** For any channel permutation Q with no active spatial transformation, `Ω′=QΩ` gives

\[
A'=QAQ^T,\qquad Z'=\det(Q)QZ.
\]

When displayed again in the fixed labelled frames, its vector action is `v′_{π(i)}=D_{π(i)}E_i(vᵢ)=T_{π(i),i}vᵢ`, without requiring a common spatial reflection G. In a wholly passive rename, the labels and their carriers are renamed together. Neither interpretation adds the ambient determinant. In particular a pure A/C swap sends Z to `−SZ`, while the active vertical reflection sends it to `+SZ`.

These are kinematic laws. Declaring a dynamical symmetry also requires the corresponding parameter assumptions: permutations are covariant when k is carried with the state; equal kᵢ is sufficient at fixed labels, while ε=0 makes k irrelevant. Phase/mirror actions retain the zero-stratum qualification from §12. No dynamical invariance is inferred from point-group membership alone. [B_PAPER §7, equations (17)–(23), and §9]

## 14. Cyclic witness: two different three-coordinate representations

Take the accepted state `Ω=(0,1,i)ᵀ`. Directly,

\[
x=(0,1,0)^T,\quad y=(0,0,1)^T,\quad Z=x\times y=(1,0,0)^T.
\]

The spatial C3 operation induces `Ω′=P_cΩ=(i,0,1)ᵀ`. Recomputing the channel determinants yields

\[
Z(\Omega')=P_cZ=(0,1,0)^T.
\]

If the same initial three numbers were instead Cartesian components of an ambient axial vector, this proper rotation would give

\[
RZ=(-\tfrac12,\tfrac{\sqrt3}{2},0)^T.
\]

These outputs differ, with squared distance `2−√3>0`. A slot containing “area of B/C” moves to a new channel-pair slot under permutation; an ambient x-directed arrow rotates through 120°. Equal storage dimension does not identify those two transformation rules.

This rejects the naive direct Cartesian interpretation. It does not rule out some separately defined channel-to-geometric observable map with its own covariance proof. No such extra map or physical axial-vector interpretation is introduced here. [B_PAPER §8, equation (24); FACE_TESTS cyclic witness]

## 15. Dictionary linking the closed entries

| Entry | Object already established | Role here |
|---|---|---|
| Atlas 01 | `Ω=x+iy∈ℂ³`, with raw channel chirality `x×y` | Supplies canonical state and observable; provenance investigation stays closed. |
| Atlas 03 | Fixed centres cᵢ, outward normals nᵢ, common e_z and tᵢ on three canonical faces | Supplies the geometric carrier; no mesh or geometry change occurs. |
| Atlas 04 | `Dᵢ(q+ip)=q tᵢ+p e_z`, `Eᵢ(v)=tᵢ·v+i e_z·v`, `Tᵢⱼ=BᵢBⱼᵀ` | Specifies the accepted state representation and comparison of its planes. |
| Atlas 04 | `Aᵢⱼ=Im(conj(Ωᵢ)Ωⱼ)`, `Z=(A_BC,A_CA,A_AB)` | Gives chirality its transported signed-area meaning and correct symmetry laws. |

The precise boundary going forward is

```text
PAPER_C_GEOMETRY != OMEGA_DYNAMICS
OMEGA_HAS_AN_ACCEPTED_TANGENT_VECTOR_REPRESENTATION
NO_ACCEPTED_PHYSICAL_POINT_POSITION_LAW_FROM_OMEGA
```

The representation is accepted mathematics. Interpreting those vectors as a physical field, choosing a physical length scale, or treating their endpoints as physical positions would require additional accepted input. A face centre may anchor a drawn vector without supplying that physical law. This entry sharpens the interface statement without editing the closed Atlas-03 packet. [B_PAPER §§1,3,11]

## 16. Bounded historical comparison

The question here is whether inspected older scalar/display code already supplies an equivalent **three-plane D/E/T dictionary**. The comparison does not reopen earlier provenance or correction work.

| Evidence | Finding | Classification |
|---|---|---|
| Current B_CODE and B_PAPER | Explicit outward frames, isometric D/E, matched rank-two T and the two-determinant symmetry law | EXACT_CURRENT_MATH |
| OLD_MODEL and PRODUCTION_MODEL | Both explicitly compute the cyclic triple `Im(conj(O₂)O₃), Im(conj(O₃)O₁), Im(conj(O₁)O₂)` | HISTORICAL_PRECURSOR |
| The old triple's algebraic relation to current Z | The displayed polynomial is exactly the current raw cross-product polynomial; this fact alone supplies neither the selected planes nor their transport | EXACT_CURRENT_MATH |
| OLD_3D `history_Zvec_to_xyz` and OLD_CURVES diagnostic plots | Stored three-component diagnostics are used directly as plotting coordinates, with separate Z_macro/Z_chiral/Z_total curve displays | HISTORICAL_PRECURSOR |
| OLD_3D torus map; OLD_TETRA trajectory | History-dependent display positions or reordered/rescaled coordinates, rather than three complex coordinates decoded into fixed tangent frames | STRUCTURAL_ANALOGY |
| OLD_CORRIDOR “tangent” analysis | Finite differences of a torus-display XY trajectory, normalized with an additive numerical floor, compared with XY-projected history jumps | STRUCTURAL_ANALOGY |
| The word “tangent” or a count of three in both lanes | Terminology/count overlap alone provides no mathematical equivalence | COINCIDENCE |
| Existence of an equivalent D/E/T dictionary somewhere else in uninspected historical material | Not established by this bounded search; no retrofitted bridge is supplied | OPEN |

In the inspected old model/display functions, the channel-area polynomial is present but the Paper-B tangent-frame dictionary is not. The old `Z_macro`/`Z_vec` blend is a separate construction; it does not change the current raw readout's definition or add an envelope to it. The old trajectory “tangent” is not tᵢ=e_z×nᵢ, and its finite-difference comparison is not Tᵢⱼ.

The bounded search covered relevant `.py`, `.md` and `.txt` files in `kernel_TO` and the copied production kernel for chirality/frame/transport/encoding terms, followed by direct inspection of the named implementations. This is evidence about those functions and search results, not proof that no equivalent idea ever existed in all notes, PDFs, branches or private recollections. Nothing in either historical tree was executed or modified for this comparison.

## 17. Independent exact checks and reproducibility

The checks script reconstructs the frames from the accepted affine panel maps. Before importing kernel code it verifies D/E, projectors, J and area-form signs, all nine transport matrices, all 27 composable index triples, matched C3 rotations, holonomy, symbolic pre-synchronization conjugacy, symbolic signed areas, skew-matrix invariants, global phase/scaling, all twelve spatial actions and all six pure channel permutations.

Negative cases cover normal-bearing inputs, rank-two transport, an out-of-polygon vector endpoint, dependent face normals, wrong transport of centres, the cyclic axial-vector mismatch, and a zero-stratum common-phase counterexample. API checks are then separately executed for numerical conversions, readout delegation, precise recurrence-call ownership, initialization and finite-input/precision guards.

**Executed result: 71/71 predicates PASS, 0 FAIL.**

| Group | Passed / total |
| --- | --- |
| API_FLOAT | 6 / 6 |
| API_FLOAT_FALSIFIER | 2 / 2 |
| API_OWNERSHIP | 5 / 5 |
| API_PRECISION | 5 / 5 |
| EXACT_ALGEBRA | 27 / 27 |
| EXACT_FALSIFIER | 7 / 7 |
| EXACT_SPATIAL_ACTION | 12 / 12 |
| SOURCE_INTEGRITY | 1 / 1 |
| TREE_INTEGRITY | 6 / 6 |

Recorded run: `2026-09-29T06:42:54.468030+00:00`. Python `3.11.15`, SymPy `1.14.0`, NumPy `2.4.4`; interpreter `C:\Users\Notandi\miniconda3\envs\torment\python.exe`.

A predicate can check an entire finite family; the count is not a count of independent theorems. Analytic image/rank/domain statements and representation meanings rest on the proofs above. The Python checker is supplemental evidence, not a substitute for those arguments. Existing tests and prior publication audit counts are not added to the executed total.

Run using the requested environment:

```powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_04_EXACT_CHECKS.py `
  --output C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_04_EXACT_RESULTS.json
```

The recorded run used `C:/Users/Notandi/miniconda3/envs/torment/python.exe` directly with bytecode disabled. To include the separately captured before/after inventory comparison, append this option to the command:

```powershell
--integrity-dir C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas04_20260929_pwk5juv2
```

Without that option the script still checks mathematics, API behaviour and consulted-source stability, but makes no full-tree inventory attestation. Re-running later inspects the then-present code, so the recorded baseline and hashes must still be checked. Retain the inventory directory to reproduce its optional comparison. The JSON contains the exact frames, D matrices, Π/J/T matrices, skew matrix, chirality expression, holonomy, all twelve symmetry actions, individual predicates, runtime ownership evidence and source hashes.

## 18. Integrity and closeout

All deliverables are under `C:/Users/Notandi/.codex/reports`, outside the protected trees. Fresh before/after file-content inventories were taken for the current repository, old kernel and entire production checkout; the copied production kernel is also reported as a nested scope.

Each inventory maps relative POSIX-form file paths to SHA-256 file-content hashes. The aggregate is SHA-256 of the sorted-key, compact JSON map. Ignored and untracked files are included; `.git` administrative contents are excluded. Timestamps, ACLs, empty directories and separate symlink metadata are not certified. Enumeration is sequential rather than an atomic filesystem snapshot; intervals and full snapshot hashes are recorded. Matching inventories demonstrate no net file-content/path change across the captured intervals.

| Scope | Before / after files | Before SHA-256 | After SHA-256 | Changed paths |
| --- | --- | --- | --- | --- |
| current | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | 0 |
| old | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | 0 |
| torment_kernel | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | 0 |
| torment_checkout | 173908 / 173908 | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | 0 |

Capture intervals (UTC):

| Scope | Before interval | After interval |
| --- | --- | --- |
| current | 2026-09-29T06:26:49.921726+00:00 to 2026-09-29T06:26:54.144904+00:00 | 2026-09-29T06:35:08.953054+00:00 to 2026-09-29T06:35:13.399108+00:00 |
| old | 2026-09-29T06:26:54.147446+00:00 to 2026-09-29T06:26:54.426916+00:00 | 2026-09-29T06:35:13.402486+00:00 to 2026-09-29T06:35:13.692560+00:00 |
| torment_kernel | 2026-09-29T06:26:54.429940+00:00 to 2026-09-29T06:26:54.457120+00:00 | 2026-09-29T06:35:13.700551+00:00 to 2026-09-29T06:35:13.725638+00:00 |
| torment_checkout | 2026-09-29T06:26:54.461121+00:00 to 2026-09-29T06:29:03.327350+00:00 | 2026-09-29T06:35:13.729446+00:00 to 2026-09-29T06:37:28.615978+00:00 |

Current HEAD remains `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`; production HEAD remains `a06edcc5c9df5d3b56405085d9f2942b768dc203`. Before/after tracked Git status is clean, checked with optional locks disabled. That status command does not classify untracked files; the content inventories cover them. No Git mutation command was issued.

Consulted-source fingerprint register:

| ID | SHA-256 |
| --- | --- |
| B_CODE | `be9d1e25a6f368e644ecfa9b1af70ba9382599e8b4d43d529d1783004d86ded7` |
| READOUTS | `3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9` |
| B_PAPER | `fb4575120470e8d7143ebc1f475ee4635caf9f39f21f88308960308fb259e150` |
| B_SYMBOLS | `1987aa42883097ded5f9c498b78cb7b467812ea238bf7bb522078f2e9e19ea66` |
| GEOMETRY | `18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf` |
| DYNAMICS | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |
| NUMERIC_POLICY | `cc33f797e76f7dbeff6fbd58ab52003fde2acbadf35ae299d827b4b55ba29655` |
| BOUNDED_WRAPPER | `4428dc5d1b9a8328da818550c51e1aef489d42ddd8338c19c3185fed9300f160` |
| FACE_TESTS | `0625221cf107f2c4ac778e17c9ff3262af64978089bb2ad571ee32bf07740bcb` |
| READOUT_TESTS | `df8683819e6733ddf6b47d52cbc42b332a72e7af8ec9148195e3e935201763e0` |
| OLD_MODEL | `ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6` |
| OLD_3D | `b6803b3a02f5240a5cb00a3dbc9cf403c2e762de713146aa3848996738772400` |
| OLD_TETRA | `14845223bbfa0c0f17df2781ee4a0ebba9befeee5f374bb01a4647242dbedf9f` |
| OLD_CURVES | `3be6de46c7060b6e797bc6801de002c5b59374957a3ef1a9fd37d51b11b20106` |
| OLD_CORRIDOR | `8596940375d1f299a6e8fef40b49e9a603405298867594f276e95fdcd464c81b` |
| PRODUCTION_MODEL | `c9fcc15940749b27fbe9a8afea6aad46fed6e56b469b30ad976a7ba225ac66ab` |

Checks-script SHA-256: `08b172d07568c742aa5c3f179b4a07ffea243174a0318c5d2c256b0c65713e91`.

Results-JSON SHA-256: `5ae102aaf2093c3a149191b591b6b5bb9e5dbe1e905a7a4c11b54eccb7fa6a89`. The packet omits a self-hash to avoid a circular dependency. Full inventory paths, hashes and Git observations appear in the JSON.

```text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
PAPER_C_GEOMETRY != OMEGA_DYNAMICS
OMEGA_HAS_AN_ACCEPTED_TANGENT_VECTOR_REPRESENTATION
NO_ACCEPTED_PHYSICAL_POINT_POSITION_LAW_FROM_OMEGA
```

The change flags refer to the captured content/path comparison and source checks; commit/push counts refer to this work order. No source modification, new recurrence, source-document correction, physical interpretation or repository placement was performed. Stop after this external source-packet closeout.
