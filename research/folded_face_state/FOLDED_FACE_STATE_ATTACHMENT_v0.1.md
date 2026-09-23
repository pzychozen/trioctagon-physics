# Folded-face state and observable attachment — Claude review

Date: 2026-09-23
Derivation reviewer: **Claude**
Subsequent implementation owner: **Codex**

## Verdict

| Group | Verdict |
|---|---|
| **I** — existing encoding, explicit adoption | **ACCEPTED as an adoption. Every identity is exact; the adoption is a choice, not a theorem.** |
| **II** — transport and the same evolution | **ACCEPTED and STRENGTHENED, with two conventions the proposal does not flag.** |
| **III** — observables and geometric meaning | **ACCEPTED and IDENTIFIED. GPT's derivation is correct; the observable is the already-confirmed symplectic form.** |

Nothing in the proposal is refuted. The whole construction is **exactly conjugate** to the frozen map, so it adds a geometric dictionary and three new objects (`T_ij`, `F_face`, `A_ij`) and **no dynamical content whatsoever**. Two conventions are silently fixed by it, and five of the nine recorded interface questions remain open. This is not a derivation of Paper-A dynamics from the octagon shape, and the toy-model reconstruction is not complete.

---

## 0. Inputs — exact paths and hashes

Repository-relative, under `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`:

| Path | SHA-256 |
|---|---|
| `research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md` | `0fea9e9534de32c896fd8d5341a086d34ff92828cecd8c392ef978e6c967a974` |
| `research/top_to_recursive_bridge/UNRESOLVED_INTERFACE_ASSUMPTIONS.md` | `eead01206cf5d162acf36d1a273cf27a087f47395b914aaeb2f5ced67d8e84d1` |
| `research/phase_bridge_II/PHASE_BRIDGE_II_CODEX_REVIEW.md` | `fab671ec7321d3e2cfe8aca99e96bfeabe32873f0711ec91e87ea40494646380` |
| `kernel_physics/geometry.py` (read-only) | `18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf` |
| `kernel_physics/dynamics.py` (read-only) | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |

Under `C:\TORMENT\TRIOCTAGON_new`:

| Path | SHA-256 |
|---|---|
| `reconstruction/KERNEL_SOURCE_TO_MODEL.md` | `9ad910906a5f21adb00c6262f3f7f95e76c46d69b758abb4f2b47ee58912f69a` |
| `research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md` | `7d65c0c61560bc93149f307edd4a2f617e4e717cb9c11c356cf543b7444227ae` |

Duplicate copies of the first two exist at the project root outside the repository; both are byte-identical to the repository-relative versions, so no mixed-version reading occurred. Supporting computation: `CLAUDE_FOLDED_FACE_ATTACHMENT_CHECKS.py` with `CLAUDE_FOLDED_FACE_ATTACHMENT_RESULTS.json` and `..._STDOUT.txt`, in this directory. **29 exact checks, 29 pass, zero literal-`True` predicates. A pass count is not a proof count.** SymPy exact arithmetic throughout; NumPy only where a frozen floating map is being compared. Python 3.10.12, NumPy 2.2.6, SymPy 1.14.0. No suite was rerun; `kernel_physics.geometry` and `kernel_physics.dynamics` were imported read-only, and no historical kernel was opened.

---

## 1. Inherited exact results, and where they come from

Nothing below is new here. All of it is re-verified in the accompanying script rather than assumed.

| Inherited result | Source | Status | My check |
|---|---|---|---|
| `n_A=(-√3/2,1/2,0)`, `n_B=(0,-1,0)`, `n_C=(√3/2,1/2,0)` are the outward normals | first bridge §3 | EXACT | **G0.1** — equal to `folded_module().face_normal(0,1,2)` symbolically, confirming the `A=P1,B=P2,C=P3` order is the module's own |
| centres `c_A=(-1/4,√3/4,0)`, `c_B=(0,0,0)`, `c_C=(1/4,√3/4,0)` | first bridge §1 | EXACT | **G0.2** — equal to the actual face centroids |
| `t_i=e_z×n_i`; `(t_i,e_z)` an orthonormal oriented tangent frame | first bridge §3 | EXACT | **G0.4** — unit, `⊥n_i`, and `t_i×e_z=n_i` (right-handed) |
| `W_tan ≅ C³` isometrically, `Σ‖v_i‖²=Σ|Ω_i|²` | first bridge §3 | EXACT | **GI.1, GI.3** |
| `J_i v = n_i×v`, `J_i²=-1` on the tangent plane, `E(J v)=iE(v)` | first bridge §3 | EXACT | **GI.4** |
| `Γ_G J = det(G) J Γ_G`; mirrors act conjugate-linearly | first bridge §3 / PB-II §2 | CONFIRMED_EXACT | **G0.6** |
| horizontal mirror `Ω↦conj(Ω)`; vertical mirror `Ω↦-T conj(Ω)` | first bridge §3 / PB-II §2 | CONFIRMED_EXACT | **G0.6** |
| `ω(v,w)=q_v p_w − p_v q_w`, flat Kähler on each plane | PB-II §1 | CONFIRMED_EXACT | **GIII.2** |
| `Z` laws: common phase invariant, conjugation `Z↦-Z`, permutation `Z↦det(P)PZ`, vertical mirror `Z↦TZ` | PB-II §5 | CONFIRMED_EXACT | **GIII.5** |
| `L₃ = 𝟙𝟙ᵀ−3I = −3P_⊥` is the actual face-sharing Laplacian | first bridge §1 | EXACT | **GII.5** |
| C3 covariance needs equal `k`; `Arg₀(0)=0` breaks common-phase equivariance on the zero stratum for `λ≠0` | first bridge §7 | EXACT + NUMERICALLY_VERIFIED | **GII.10** — reproduced bit-for-bit |

**The crucial inherited label.** First bridge §3 already classified the tangent-vector observable as **CANDIDATE_INTERPRETATION**, with an explicit UNRESOLVED note: *"The shell does not supply the three vectors' values, a field from which to extract them, their units, or a law making tangent-vector rotation into dynamical phase."* `UNRESOLVED_INTERFACE_ASSUMPTIONS.md` then tabulates **nine** open interface questions. This review is about what GPT's adoption does and does not close among those nine.

---

## 2. What GPT proposes

One raw tangent vector `v_i` at each existing face centre — a finite-dimensional state observable, not a vertex displacement, physical field or seam-continuous perimeter wave.

```text
D(Ω)_i = Re(Ω_i) t_i + Im(Ω_i) e_z            encoding  C³ → W_tan
E(v)_i = t_i·v_i + i (e_z·v_i)                 decoding  W_tan → C³
T_ij   = t_i t_jᵀ + e_z e_zᵀ                   transport plane j → plane i
ṽ_i    = v_i + ε(k_i−‖v_i‖²)v_i + g Σ_{j≠i}(T_ij v_j − v_i)
F_face = D ∘ F_TO ∘ E
A_ij   = n_i · [ v_i × (T_ij v_j) ]
Z_chiral = (A_BC, A_CA, A_AB)
```

---

## 3. Group I — existing encoding, explicit adoption

### Verdict: **ACCEPTED as an adoption.**

### 3.1 Domains, inverse, norms

- **`E∘D = id` on all of `C³`** (GI.1), with no domain restriction, no normalization and no exceptional branch.
- **`D∘E = Π`, not the ambient identity** (GI.2). `Π_i = t_i t_iᵀ + e_z e_zᵀ` is an idempotent **rank-2** projector — for face A, `Π_A = [[1/4, √3/4, 0],[√3/4, 3/4, 0],[0,0,1]]` — which is the identity *on* the plane and annihilates `n_i`. So `D` and `E` are mutually inverse only between `C³` and `W_tan`. **Any normal component of a supplied `v` is silently discarded.** That must be an explicit rejection or a documented projection in code, not an accident.
- **Isometry including zero** (GI.3): `‖D(Ω)_i‖² = |Ω_i|²` exactly for each `i`; `D(0)=0`, `E(0)=0`.
- **Complex structure inherited** (GI.4): `E(J_i v) = i E(v)`, so multiplication by `i` is exactly a +90° turn about the outward normal.

### 3.2 What adopting this observable actually adds

The isomorphism was **already proved EXACT** in first bridge §3. Adoption therefore adds no mathematics to the encoding itself. Precisely, it adds:

1. **A declaration.** It converts §3's CANDIDATE_INTERPRETATION into a named observable, closing two of the nine open rows — *"What is measured on each face?"* (a raw tangent vector at the centre) and *"Where is its second real quadrature?"* (the `e_z` component) — and fixing the orientation half of a third.
2. **Two new objects that did not exist before:** the transport `T_ij` and the observable `A_ij`. These are genuine additions, reviewed in §§4–5.
3. **A dictionary** in which the shell's spatial symmetries become checkable channel operations.

It adds **nothing dynamical**. `F_face = D F_TO E` is conjugate to `F_TO` by an isometric isomorphism, so orbits, invariant sets, fixed points, bounds and every dynamical statement are in bijection with those of the frozen map. No new prediction, no new constraint, no new degree of freedom. **This is a relabelling with a geometric dictionary, not new physics** — which is exactly what makes it safe to adopt, and exactly why it must not be described as deriving anything.

### 3.3 Adoption costs and limits, stated

- **The shell does not distinguish `t_i` inside the face** (GI.5). A 45° rotation about `n_B` is a symmetry of a regular octagon yet moves `t_B`. Declaring *"`Re(Ω_i)` is the `t_i` component"* is extra data the geometry does not supply. First bridge §3 flagged precisely this as a hidden orientation/observable choice; adoption spends that choice rather than justifying it.
- **The precondition is that the faces are vertical** (G0.3). Every face normal is horizontal, so the single vertical `e_z` lies in all three tangent planes; that is what makes the second quadrature a *common* direction rather than three unrelated ones. I checked this at the canonical `β=π/3` weld and at `π/4`, `2π/5` and `π/2`: the normals are horizontal for **every** fold angle in this panel family, so the precondition is a property of the panel construction, not of the canonical weld alone. It is still a property of *this* geometry and should not be assumed for a different host.
- **Face centres only.** Three vectors at three points. PB-II §1 states it outright: *"this concerns selected tangent-vector spaces, not a smooth global tangent bundle through the creases of the polyhedral shell."* There is no field on the faces, no continuity across seams, and no perimeter wave. The perimeter route was separately examined in first bridge §4 and leaves **one** real coefficient, not three phase planes.
- **No length clipping, and the vectors can leave the face.** Face B is a regular octagon of circumradius `√(1−√2/2) = 0.541196100146197` about its centre. The admitted radius-three profile allows `|Ω_i| ≤ 3`, i.e. a state vector up to about **5.5×** the face's own circumradius. The picture is a vector *attached at* the centre, not *contained in* the face, and it must never be rescaled to fit.

---

## 4. Group II — transport and the same evolution

### Verdict: **ACCEPTED and STRENGTHENED.**

### 4.1 The stated properties hold, one of them more strongly than claimed

- **Oriented components and tangent norms are preserved** (GII.1): `E_i(T_ij v_j) = Ω_j` exactly, for all nine ordered pairs.
- **`T_ij T_jk = T_ik` is an identity of full 3×3 ambient matrices** (GII.2), verified on all 27 triples — because `t_j·t_j = 1` and `t_j·e_z = 0`. The work order asks only for it "on the stated spaces"; it is true without that restriction.
- **`T_ii` is the identity on the plane and the rank-2 tangent projector in the ambient space** (GII.3): `T_ii n_i = 0`, `T_ii ≠ I₃`, rank 2, idempotent. Stated correctly in the proposal.

### 4.2 Strengthening — `T_ij` is the C3 rotation, not an ad hoc frame match

**`T_ij` restricted to plane `j` coincides with the unique C3 rotation `R_ij` carrying face `j` to face `i`; as ambient matrices `T_ij = Π_i R_ij`** (GII.4, verified for all nine pairs both on-plane and ambient).

This upgrades the proposal in three ways: the transport is a genuine spatial symmetry of the existing shell rather than a coordinate convenience; the composition law `T_ij T_jk = T_ik` is simply the C3 group law; and `T_ii = Π_i` is the identity element, projected.

**It remains, emphatically, not a seam law.** `T_ij` is a rigid symmetry of the whole module, not parallel transport along the surface and not a welded continuity condition. The UNRESOLVED row *"How do seams couple fields?"* is untouched by it.

A provenance note that matters for anything placed **at** the centres: `geometry.rotate_c3` turns about the **centroid axis** `(0, √3/6, 0)`, not the origin (G0.5). Its *linear* part is the rotation about `e_z`, so tangent-frame statements are unaffected; but the face centres are permuted only by the centroid-axis map. Code that rotates attached vectors must use the linear part, and code that rotates their attachment points must use the full map.

### 4.3 The same evolution, exactly

**`E(ṽ)_i` equals the existing pre-sync update exactly** (GII.5), symbolically in `ε`, `g`, `k_i` and all six real coordinates:

```text
E(ṽ)_i = Ω_i + ε(k_i − |Ω_i|²)Ω_i + g (L₃ Ω)_i ,
Σ_{j≠i} (T_ij v_j − v_i) = (L₃ Ω)_i .
```

**The phase increment is a rotation about the outward normal** (GII.6): multiplying `Ω_i` by `e^{iδ_i}` is exactly the right-handed rotation of `v_i` by `δ_i` about `n_i`, modulus preserved. So the existing synchronizer acts on the shell as a per-face spin about that face's own normal, with no change to the recurrence.

**Zero stratum** (GII.7): at `v_i = 0` there is no direction to rotate. The current `Arg₀` assigns angle 0 to every exact complex zero, signed zeros included. The face picture must present that as a convention, not as a rotation.

`F_face = D F_TO E` is therefore well defined, satisfies `F_face ∘ Π = F_face`, and has image inside `W_tan`. **It is a transported toy law. It is not a derivation of Paper-A dynamics from a mechanical field or from the octagon shape.**

### 4.4 FINDING II-a — the transport convention silently fixes the reality of `L₃`

Any `Rot(n_i, θ_ij) ∘ T_ij` is an equally valid isometry from plane `j` to plane `i`. Under it (GII.8, exact):

```text
E_i(T′_ij v_j) = e^{i θ_ij} Ω_j ,
coupling  →  g Σ_{j≠i} ( e^{i θ_ij} Ω_j − v_i term ) ,
```

which is `L₃` **only** for `θ_ij ≡ 0`. So the realness of the existing coupling matrix is a *consequence of choosing the C3-matched, zero-relative-phase transport*, not an independent geometric fact. The proposal picks that transport without recording that it is a choice. **Smallest correction: name the convention and record it** (`TRANSPORT_ID`), exactly as the boundary packet names its response and gauge.

### 4.5 Passive frame change / spatial symmetry / dynamical symmetry

The three must not be conflated. Measured on the frozen map (GII.9, GII.10):

| Operation | Kind | Effect | Residual |
|---|---|---|---|
| choice of `t_i` inside the face | passive frame change | changes which real direction is `Re Ω_i` | not a symmetry of anything; pure convention |
| global `U(1)`, `Ω ↦ e^{iα}Ω` | dynamical symmetry | commutes with the full map | `2.6e-16` |
| per-face phases in `(2π/3)Z` | **synchronizer-only** | commutes with `phase_sync` (`4.3e-16`) and with `g=0` (`5.3e-16`) | **broken by the coupling: `0.2898`** |
| octagon's own 45° face rotation | spatial symmetry, **not** dynamical | `0.2705` | breaks the map |
| C3, equal `k` | spatial **and** dynamical | `0.0` | exact |
| C3, unequal `k`, fixed parameter labels | spatial only | `0.0893` | needs `k` permuted with the state |
| common phase on the zero stratum, `λ≠0` | fails | `0.09317017645041971` | reproduces the recorded first-bridge value bit-for-bit |

Two things are worth stating plainly. First, the harmonic-three synchronizer **does** have an independent per-face `Z₃` freedom — `3(φ_j + 2πm_j/3 − φ_i − 2πm_i/3)` differs from `3(φ_j−φ_i)` by a multiple of `2π` — and it is the *linear coupling* that destroys it, because `(L₃Ω)_i` mixes channels and needs one common phase. The transport convention of §4.4 is therefore precisely what removes the per-face freedom. Second, and directly per the work order: **arbitrary local phase changes do not leave the coordinate formula invariant.** Only the global phase does, and only off the zero stratum when `λ≠0`.

---

## 5. Group III — observables and geometric meaning

### Verdict: **ACCEPTED and IDENTIFIED.**

### 5.1 GPT's derivation is correct

**`A_ij = n_i·[v_i × (T_ij v_j)] = q_i p_j − p_i q_j = Im(conj(Ω_i) Ω_j)`**, exactly, for all nine ordered pairs (GIII.1). The mechanism is that `v_i = q_i t_i + p_i e_z` and `T_ij v_j = q_j t_i + p_j e_z` lie in the same plane, so their cross product is `(q_i p_j − p_i q_j)(t_i × e_z) = (q_i p_j − p_i q_j) n_i`.

`A_ji = −A_ij` and `A_ii = 0` (GIII.3): a real antisymmetric 3×3 array with exactly three independent entries — which is *why* a triple suffices, rather than a coincidence.

**`Z_chiral = (A_BC, A_CA, A_AB)`** (GIII.4), equal symbolically to `Re Ω × Im Ω` and numerically to the value returned by the implemented `kernel_physics.readouts.z_chiral` (difference `0.0`). The four confirmed transformation laws reproduce exactly (GIII.5): common phase `5.6e-17`, conjugation `0.0`, cyclic permutation `0.0`, vertical mirror `0.0`.

### 5.2 Identification — `A_ij` is the confirmed symplectic form, transported

**`A_ij = ω_i(v_i, T_ij v_j)`** (GIII.2), where `ω(v,w) = q_v p_w − p_v q_w` is exactly the Kähler/symplectic form already **CONFIRMED_EXACT** in PB-II §1. So `A_ij` is the canonical area form of plane `i` evaluated on `v_i` and the transported `v_j` — not a new ad hoc bilinear. This also explains its symmetry behaviour for free: the anti-symplectic law `ω(Γv,Γw) = det(G) ω(v,w)` is what produces the `det(P)` in the permutation law and the sign flip under mirrors.

### 5.3 The four-way distinction

1. **Transported signed state-vector area** — what `A_ij` *is*. The signed area of the parallelogram spanned by `v_i` and `T_ij v_j` inside plane `i`, with sign from the outward `n_i`. Its units are the *square of the observable's* units, and it scales as `|c|²` under `Ω ↦ cΩ` (GIII.6).
2. **Physical surface area** — what it is *not*. `A_ij` contains no edge length, no octagon area `A_O` and no shell scale parameter `s` (GIII.6). The octagon's actual area never enters, and comparing `A_ij` with a surface area requires separately supplied units that do not exist yet.
3. **Channel-indexed triple** — what `Z_chiral` *is*. Three slots labelled by face.
4. **Ambient axial vector** — what `Z_chiral` is *not*. **Decisive witness (GIII.7):** under the *same* physical C3 rotation an ambient axial vector transforms by the rotation matrix about `e_z`, while `Z` transforms by the channel permutation — a rotation about `(1,1,1)/√3`. For `Z = (1,0,0)` these give `(-0.5, 0.866, 0)` and `(0,1,0)` respectively, separated by `0.518`. The three slots are face labels; that there are three of them, as there are three ambient axes, is a coincidence of dimension.

No electromagnetic spin, force, shell motion or feedback law is inferred, and none follows. PB-II §5's caution stands: *"Physical parity/handedness interpretation remains additional."* Its accompanying remark that `Z` is not implemented in the clean kernel is now out of date — `readouts.z_chiral` exists and this attachment is a *view* of it, not a second readout.

### 5.4 Decoding a prepared state, and successive steps

**No new preparation, normalization or phase generator is needed** (GIII.8). Taking the already-admitted pipeline — `theta_from_lens(1.0, 1.2)`, `ξ = (0.6+0.2j, −0.3+0.4j)`, `transfer_count=1`, `branch=negative_imag` — and decoding with `D` at each step, the `D`-then-`E` round trip returns the same state to `1.4e-17` over four downstream steps. The three face vectors carry lengths

```text
step 1: 0.15428736348119987   (all three equal)
step 2: 0.06924567619095894
step 3: 0.031143952760845563
step 4: 0.014013268345081733
```

equal across faces because a prepared SRG state is a single Fourier mode `a f_j`, whose three components share one modulus. Successive existing `step3` states are represented as those three vectors changing length and turning about their own normals. Nothing is added to the recurrence.

---

## 6. Minimum API requirements for later Codex implementation

Stated as requirements, not as an implementation.

**Constants to name and record.** `FRAME_ID = "face_center_tangent_ez_v1"` and `TRANSPORT_ID = "c3_matched_zero_phase_v1"`. Both belong in `handoff.metadata()` alongside the existing `response_id` and `gauge`, because §4.4 shows the transport is a choice that changes the law.

**Functions.**

| Requirement | Contract |
|---|---|
| `face_frames()` | immutable `(t_i, e_z, n_i, c_i)` for `i` in `A,B,C`, in the module's own `A=P1,B=P2,C=P3` order; arrays read-only, matching the treatment of `chi` and `omega` in the boundary packet |
| `decode_to_faces(omega)` | `D`; returns a fresh `(3,3)` real array; strict input validation in the style of `_response_numeric` |
| `encode_from_faces(v)` | `E`; **must explicitly reject or explicitly document** the discarded normal component (GI.2) rather than dropping it silently |
| `transport(i, j)` | `T_ij`, with `T_ij = Π_i R_ij` and `θ_ij = 0` recorded as the convention |
| `state_area(i, j, omega)` / `area_triple(omega)` | `A_ij` and `(A_BC, A_CA, A_AB)` |

**The single most important requirement: `F_face` must be a view, not a second law.** It must be computed as `D ∘ step3 ∘ E` using the existing `step3` exactly once per step, never reimplemented in face coordinates. Two copies of the same recurrence would drift. The same applies to `area_triple`: it must be a thin alias over the existing `z_chiral`, with a test asserting bitwise equality, not a parallel implementation.

**Must not.** No clipping or rescaling of vector lengths to fit inside an octagon (§3.3). No interpolation, field or seam-continuity construction. No second recurrence, no new default, no normalization. `F_face` stays an opt-in view of an already admitted law.

**Tests that would earn admission.** `E∘D = id`; `D∘E = Π` with `Π n_i = 0`; the isometry including zero; `T_ij T_jk = T_ik` on all 27 triples; `T_ij = Π_i R_ij`; `E(ṽ) = ` existing pre-sync; `D(e^{iδ}Ω) = Rot(n_i,δ) D(Ω)`; `area_triple == z_chiral` bitwise; the four transformation laws; and negative tests for the unequal-`k` and zero-stratum qualifications so they cannot be quietly promoted later.

---

## 7. Remaining physical interpretations — the nine recorded rows, scored

| Interface question (from `UNRESOLVED_INTERFACE_ASSUMPTIONS.md`) | Status after this adoption |
|---|---|
| What is measured on each face? | **Answered by declaration.** A raw tangent vector at the face centre. Declared, not derived. |
| Where is its second real quadrature? | **Answered.** The `e_z` component, available because all three faces are vertical (G0.3). |
| Why is the tangent-plane candidate physically relevant? | **OPEN.** No field, no units, no extraction map is supplied. |
| What generates phase? | **OPEN.** The rotation about `n_i` is the *representation* of Paper A's existing synchronizer, not a generator derived from geometry. |
| What fixes the sign and scale of phase? | **Half answered.** Sign and orientation are fixed (right-handed, outward `n_i`, `t_i = e_z×n_i`). Scale, period and time unit remain **OPEN**. |
| How do seams couple fields? | **OPEN.** `T_ij` is a rigid C3 symmetry, not a seam or trace law (§4.2). |
| Which three modes are retained? | **OPEN.** Three faces are assumed to give three channels; no operator or justified finite-dimensional restriction is supplied. |
| Which symmetry action should the state obey? | **Answered.** The tangent-vector action: C3 cyclic, mirrors conjugate-linear, with the equal-`k` qualification (§4.5). |
| What relates this state to the frozen nonlinear rule? | **Answered as a conjugation, not a derivation.** `F_face = D F_TO E`. The amplitude nonlinearity and harmonic three remain Paper-A choices; first bridge §7 already showed C3 does not select `m=3`. |

**Three of nine answered, one half, five open.** That is real progress on a real interface and it is not a complete physical attachment. Nothing here supplies a host, a rim condition, a field, units, a time scale, or a reason the three faces are the relevant modes.

---

## 8. Corrections to record

Two predicates in my own first run failed. Both were defects in my test construction, diagnosed to root cause rather than loosened:

- **G0.5** — I compared `geometry.rotate_c3` against a rotation about the origin's `z`-axis. `rotate_c3` turns about the **centroid axis** `(0, √3/6, 0)`. All six frame-cycling conditions were already true; only the point comparison was wrong. Re-verified on differences of points (the linear part) and separately on the face centres. The observation is worth keeping — see §4.2.
- **GII.9** — I claimed per-face phases in `(2π/3)Z` commute with the frozen map. They do not: they commute with the *synchronizer* and with the `g=0` map, and the coupling `g L₃` breaks them (`0.2898`). The corrected statement is sharper and is now §4.5.

Neither failure was in GPT's proposal.

---

## 9. Boundaries

No kernel file, shared source-to-model record, recovery record, GPT candidate or Codex record was modified. `geometry.py` and `dynamics.py` were imported read-only; no historical `kernel_TO`, `quantum_kernel` or production TORMENT module was opened; no suite was rerun; no parameter sweep, dataset, UI, new folder, corpus sweep, E8 work, alternative host geometry, global field/PDE construction, commit or push occurred. Three files were written, all in this existing directory.

**Exit.** An explicit mathematical state/observable attachment on the existing folded faces, reviewed: exact, conjugate to the frozen law, strengthened in its transport, identified in its observable, and honest about the five interface questions it leaves open. Codex owns canonical incorporation. The toy-model reconstruction is **not** declared complete.

## 10. Codex reconciliation, implementation and validation — 2026-09-23

**Disposition: ADOPTED_AND_IMPLEMENTED_AS_AN_OPT_IN_GEOMETRIC_VIEW.** This attributed addition executes the user's folded-face work order. Claude's original §§0–9 remain intact as a 25,347-byte prefix, SHA-256 `79ba39c9cac05dcb7d3091a09dd1bb17ead7302258ecd286684f56228ced4618`. The boundary/SRG packet remains closed; its 75-test implementation and all predecessor code/tests were not reopened or changed.

### 10.1 Evidence identity and review scope

Before edits, **all seven hashes in §0 matched** the actual local files. Codex read the specific first-bridge derivation §§1,3,7 and unresolved-interface note, plus the corrected Phase-II review §§1,2,5. These are the existing repository copies, not a new source search or restart of those bridge suites. Their actual identities, protected dependencies and original note identity are saved in [CODEX_FOLDED_FACE_BASELINE.json](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_BASELINE.json).

Claude's supplied supporting files remain unchanged:

| File in research/GPT_proof | SHA-256 |
|---|---|
| CLAUDE_FOLDED_FACE_ATTACHMENT_CHECKS.py | `25410a1da609aa0e964b979322617d9f1427e9c5b655fd2feb791b3764f6cc4f` |
| CLAUDE_FOLDED_FACE_ATTACHMENT_RESULTS.json | `1ca8622b8bb351a68e26305b967bfea73b9fb5485b6f218a14aabf8551778356` |
| CLAUDE_FOLDED_FACE_ATTACHMENT_STDOUT.txt | `4b3d4d40953db259822dbdae4d998a253ce14af149870ce7d595b183fb0faa53` |

The script hash agrees with the supplied results. The script was inspected as source evidence and was **not rerun**: its `--output` path would be opened for overwrite, and no original output was needed for this new implementation run. Its 29/29 reported checks include exact symbolic, floating and mixed comparisons. For example GII.7 is a floating API check, GII.9–10 are floating comparisons, GIII.4 combines symbolic and numerical checks, and GIII.5/7/8 contain floating evidence. Therefore the original blanket “29 exact checks” wording is not adopted as a description of every runtime predicate; the count is not a proof count. Codex's new tests/results below are separately attributed, not described as a new Claude execution or as Claude acceptance of the final code.

### 10.2 Reconciled disposition of the three groups

**I — encoding: accepted as a declared finite-dimensional geometric view, with the domain and orientation qualifications.** Write `D(Omega)_i=q_i t_i+p_i ez` and `E(v)_i=t_i dot v_i+i ez dot v_i`. Since `(t_i,ez)` is orthonormal, E D=I on C³, while D E=Pi on the ambient nine-real-dimensional space. Pi is the tangent projector, not ambient identity; D and E are inverse between C³ and W_tan. The implementation rejects substantive normal input rather than silently exposing an ambient projection. Exact isometry does not make floating encode/decode bitwise invertible.

GPT's orientation qualification is retained: a 45-degree symmetry of one isolated regular octagon is **not a symmetry of the full welded shell**. Given positive ez and the outward n_i, t_i=ez cross n_i is fixed; there is no residual arbitrary in-face t_i after those choices. Adoption is the decision to use these tangent vectors as the state view. No physical observable, field, units or phase generator is thereby recovered. The implementation is scoped to the current canonical geometry; it does not require a new family of folds or a general-host claim.

**II — transport/evolution: accepted, with rank, axis, convention and canonical-state qualifications.** T_ij=t_i t_j^T+ez ez^T preserves the two tangent components. Using t_j dot t_j=1, ez dot ez=1 and their orthogonality gives T_ij T_jk=T_ik as a **full ambient matrix identity**, all 27 triples, not merely a tangent restriction. However T_ij has rank two, kills the source normal, and is **not a full ambient rigid rotation**. T_ij=Pi_i R_ij, and only its restriction to the source tangent plane equals the matched C3 rotation's linear part. Points at the face centres use the affine centroid-axis rotation through `(0,sqrt(3)/6,0)`; free vectors use its linear part. Neither is a seam-continuity or surface parallel-transport law.

`TRANSPORT_ID=c3_matched_zero_phase_v1` records the fixed zero-relative-phase convention; adjustable transport phases are absent. The geometric pre-sync expression encodes to the existing complex pre-sync law, and phase multiplication becomes an outward-normal tangent-vector rotation. Thus **F_face=D F_TO E is exact coordinate conjugacy on W_tan**, not a new evolution. In code, `FaceState` instead stores the original Omega and steps it directly with the selected existing recurrence once, then decodes the returned state. There are **no repeated automatic E(D(Omega)) round trips** and no separately evolving face state. An explicitly supplied face array may initialize Omega once through rounded E.

The unequal-k and zero-stratum qualifications survive unchanged. At fixed parameter labels C3 covariance requires equal k; otherwise k must be permuted with the state. The inherited common-phase equivariance requires nonzero pre-sync components when phase_strength is nonzero; Arg0(0)=0 assigns a convention to a vector with no direction. At zero phase strength the direct branch remains valid including zeros. No symmetry claim upgrades a finite floating residual to an exact arithmetic proof.

**III — signed-area observables: accepted as the existing transported symplectic form, with separate spatial and channel signs.** The independent exact geometric expression reduces to

```text
A_ij = n_i dot [v_i cross (T_ij v_j)] = q_i p_j - p_i q_j
     = omega_i(v_i, T_ij v_j),
Z = (A_BC,A_CA,A_AB) = Re(Omega) cross Im(Omega).
```

This is the Phase-II confirmed area form, with antisymmetry and zero diagonal. Production code delegates to the existing readout and selects signed components; geometric cross products are only verification. For a spatial shell symmetry G with induced face permutation P, transport covariance and the anti-symplectic parity give `A'=det(G) P A P^T`. Taking the channel-indexed dual gives **`Z'=det(G)det(P) P Z`**. The det(G) comes from spatial orientation, while det(P) comes from permuting the three channel slots; one does not cause the other. A pure channel permutation instead gives `Z'=det(P)PZ`. Horizontal mirror gives -Z; vertical mirror with the A/C swap gives PZ. Z is not an ambient axial vector, and A is a signed state-vector area, not physical surface area.

**Correction to the displayed fixture in §5.4.** The actual `groupIII` script selects **k=(1,1,1), phase_strength=.001**, not the documented unequal-k triple. Its four printed rows are sampled **before** each update at downstream indices **0,1,2,3**, including the initialized state; they are not the four post-step states 1–4. Equal prepared Fourier magnitudes alone do not ensure equal later magnitudes. This particular equal-k evolution preserves the Fourier line to rounding; unequal-k evolution generally leaves it. Both configurations are recorded independently below.

**Metadata correction to §6.** The work order places frame/transport metadata in the face view or combined run record. It does **not** belong in `HandoffResult.metadata()`, which remains initialization-only and unchanged. The source selection, downstream profile/configuration and counters stay explicit and separate.

### 10.3 Final API and numerical contract

Only one production module and one focused test file are added under the authoritative checkout `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`:

| API in kernel_physics/face_state.py | Contract |
|---|---|
| FRAME_ID / TRANSPORT_ID / FACE_ORDER | `face_center_tangent_ez_v1` / `c3_matched_zero_phase_v1` / `(A=P1,B=P2,C=P3)`, indices 0,1,2 |
| `face_frames()` / `FaceFrames` | Frozen record with fresh read-only tangents, ez, outward normals and centres derived from existing exact `folded_module()`; geometry.py SHA-256 recorded. No second shell generator. |
| `decode_to_faces(omega)` | Strict finite complex triple to fresh real (3,3) vectors; raw magnitude retained, exact zeros remain zero, no polygon-boundary rescaling. |
| `encode_from_faces(v)` | Strict finite real (3,3), rejects complex values, strings, booleans, wrong shapes and substantive normals; returns fresh complex128 Omega. |
| `transport(i,j)` | Fresh read-only rank-two matrix, source j to destination i; integer 0–2 only, booleans excluded; no adjustable phase. |
| `area_triple(omega)` | Thin direct call to existing `readouts.z_chiral`, bitwise identical on the same input. |
| `state_area(i,j,omega)` | Corresponding signed readout component, antisymmetric, zero diagonal. Evaluates the complete readout even for diagonal requests, retaining its input/precision failures. |
| `FaceState(omega)` | Validated private copy of raw canonical Omega plus derived read-only vectors. Signed zeros in stored Omega are retained; decoded zero vectors are canonical zeros. |
| `FaceState.from_faces(v)` | Explicit one-time rounded E conversion; does not create a second trajectory. |
| `view.step(config, profile=None)` | One existing plain `dynamics.step3` if profile is None. If supplied, forwards to existing `step_bounded_triad` with its validation and exactly one step3 call. Then decodes; never re-encodes existing derived vectors. |
| `view.metadata()` | Frame/transport IDs, explicit face order, canonical-state convention, geometry source hash/width/fold/centroid and tangency tolerance. No SRG metadata change. |

For tangency the precise test is

```text
|sum(n_k v_k)| <= (8 * machine_epsilon) * sum(|n_k v_k|), k=x,y,
8 * machine_epsilon = 1.7763568394002505e-15.
```

It is evaluated after homogeneous scaling by the maximum magnitude of coordinates with nonzero normal coefficients. There is **no absolute floor**, no unit-scale floor, and no tolerance slack from a large vertical component. Pure normal vectors are rejected however small, including a 1e-250 normal component on face B alongside an enormous tangent z. Only normal residuals within the stated frame-roundoff allowance can be discarded; this is a numerical uncertainty allowance, not a claim to distinguish information below rounding resolution. It does not classify small states as zero.

The adapter reuses the current private checked scalar products/sums. Nonzero subnormal or overflowing checked intermediates/results raise `ResponsePrecisionError`. Exact zero succeeds; 1e-250-scaled finite tangent states survive with no absolute-tolerance shortcut. The conversion, readout and bounded-step numerical domains remain distinct. A 1e-320 decode fixture explicitly fails; a 1e-170-scaled area readout fails; a successfully decoded 1e-250-scaled state fails on its next bounded square operation. A post-step decode can fail conservatively after the recurrence evaluates, without modifying the previous immutable view. No precision policy of a protected module is changed and no universal machine-safety assertion is made.

### 10.4 Equation-to-code and focused-test correspondence

All named tests below are in the single new `test_face_state.py` (names shown without `test_`):

| Equation/requirement | Production operation | Verification |
|---|---|---|
| Existing exact centres/normals/order, t_i=ez cross n_i | frame construction / face_frames | `exact_source_frames_centres_and_geometry_identity`; immutable/fresh-frame test |
| E D=I, tangent isometry, ambient D E=Pi | decode/encode | `exact_inverse_isometry_and_ambient_projector`; scaled roundtrip/norm and normal-rejection tests |
| All nine T_ij; all 27 ambient compositions; T_ij=Pi_i R_ij | transport | `all_exact_transport_and_ambient_composition_identities`; separate floating-matrix test |
| Centroid-axis points versus free vectors | frame centres / transport | `point_rotation_uses_centroid_axis_and_vectors_use_linear_part`; isolated-octagon non-global-symmetry test |
| Existing geometric pre-sync dictionary and outward-normal phase rotation | existing recurrence only | `exact_presync_and_outward_normal_phase_dictionary` (symbolic verification, no second production formula) |
| Signed transported area and readout correspondence | state_area / area_triple | exact and floating independent cross-product test; bitwise delegation test |
| Spatial parity versus permutation parity | same encoding/readout | `spatial_and_channel_permutation_signs_are_separate`: all 12 D3h actions and six pure channel permutations, separately delimited floating checks |
| Equal/unequal-k and zero-stratum qualifications | FaceState.step -> existing law | covariance test, zero-stratum counterexample, combined README fixtures |
| Canonical Omega / exactly one update / selected profile | FaceState.step | six-step trajectories through each stepping route, counted calls, encode patched to reject any hidden round trip; explicit initialization/profile-error tests |
| Zero/signed-zero/tiny/invalid/precision cases | strict conversions and delegated readout | strict-input, scaled tiny, normal rejection, immutability and explicit-failure tests |

### 10.5 Actual final execution and two complete small pipelines

The pinned interpreter was `C:/TORMENT/TRIOCTAGON_new/kernel_physics/.venv/Scripts/python.exe`; Python **3.12.14**, NumPy **2.3.5**, SymPy **1.14.0**, mpmath **1.3.0**. All imported package files resolve to the authoritative checkout, not the sibling package holding the environment. No install/upgrade; all executions used `-B`.

- New focused tests: **20/20 passed**, 0 failures/errors, **1.080 s**, [focused log](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_FOCUSED_01.txt).
- Complete modern suite, **once after the focused pass**: **95/95 passed**, 0 failures/errors, **3.897 s**, [final log](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_TESTS_FINAL.txt). Count is 75 protected predecessor methods + 20 new face-view methods, not a proof count or a target of 75.
- [Separate Codex validation script](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_VALIDATE.py), [results](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_RESULTS.json) and [captured stdout](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_STDOUT.txt) execute the final README code verbatim and preserve both complete run records, all five state snapshots per fixture, frame data, source hashes, precision failures and runtime identities. This receipt does not rerun the suite or an old bridge script.

Full-suite command, from the authoritative checkout:

```bat
"C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe" -B -m unittest discover -s kernel_physics/tests -v
```

Both fixtures retain radius=1, separation=1.2, theta=0.9272952180016123, xi=(0.6+0.2i,-0.3+0.4i), response `lens_area_norm_v1`, negative-imaginary branch, spectral-projector positive-pivot gauge, helicity-major tensor order, source parameters (.423,.577,.618,.244) and **one SRG initialization application**. Each uses eps=.05, g=.2, phase_strength=.001, profile `triad_eps005_g02_k0to8_radius3_v1` and **four downstream Paper-A steps**. Face metadata belongs to the combined record. There is no noise, forcing, clipping, normalization or RNG.

| k fixture | Face lengths at initialization | Face lengths after 4 downstream steps |
|---|---|---|
| (1,1.2208964704604097,6.35310346037241) | approximately (.15428736348119987,.15428736348119987,.15428736348119987) | (.025016243526232367,.025428337440200618,.07488215680898741) |
| (1,1,1) | same initialized Fourier state | (.006305833164827623,.006305833164827608,.0063058331648275885) |

For **both** trajectories the stored Omega and area readout are **bitwise equal** to the same existing bounded wrapper and `z_chiral` on identical raw inputs at every recorded step. Rounded E(D(Omega)) has maximum absolute discrepancy **1.3877787807814457e-17** in these fixtures; that conversion is checked but never fed back into the trajectory. The 1e-250 scaled conversion fixture has maximum discrepancy **5.551115123125783e-17 after division by its scale**, with every face still nonzero. These are finite numerical observations, distinguished from the exact identities proved/tested symbolically. The README count-only prose was updated after the suite, then its final code was executed for the receipt; no tested Python code changed afterward.

### 10.6 Identities, preservation and remaining interpretation limits

| Final added/edited modern path | SHA-256 |
|---|---|
| kernel_physics/face_state.py | `be9d1e25a6f368e644ecfa9b1af70ba9382599e8b4d43d529d1783004d86ded7` |
| kernel_physics/tests/test_face_state.py | `0625221cf107f2c4ac778e17c9ff3262af64978089bb2ad571ee32bf07740bcb` |
| kernel_physics/README.md | `5ec00f5fc36cdc1ef1fae03ca870ee0d5dd8fb033af57e3159cb0c830dc5201e` |

Unchanged current dependencies retain their actual identities, including geometry `18398bd15b12c2dc1711c3ea2769f50215f2bcad5335ced9ee23e4e6baf1ddbf`, dynamics `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4`, SRG `90a563d8ef0a18ef769c76d4884e94badbaa38771d4dd192610a4cc74d709d34`, operating profile `4428dc5d1b9a8328da818550c51e1aef489d42ddd8338c19c3185fed9300f160`, and readouts `3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9`. The receipt includes every imported dependency, covering, numeric support and boundary source too.

[Final preservation receipt](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_FOLDED_FACE_PRESERVATION.json) records actual before/after identities for the **four authorized existing-file edits** (README, this append, source-to-model update, recovery append), the **two new package files**, and the seven new bounded evidence files. It separately checks **239 protected paths** by SHA-256, size and modification time; the note's original 25,347-byte prefix and recovery's original 48,414-byte prefix remain intact. The bounded inventory is not a whole-disk claim. All predecessor implementations/tests, supplied Claude evidence, old reports/results and historical kernels are preserved.

Modern HEAD stays `a0875c493b23b7d1aaa718ea2b40aa17af9adcd2`; historical HEAD stays `6310de7ba1ef4f41ed6e7cd683cf9186585cdd11`. Modern status has the existing tracked README edit, the ten predecessor untracked module/test files, the **two new face adapter/test files**, and pre-existing corpus/research entries. Exact statuses are saved in the preservation receipt. There is no staging, commit or push, and no local save is called a Git commit. No historical kernel or production TORMENT execution, folder moves/cleanup, old suite restart, physical-source search, E8 work, new geometry, datasets or UI occurred.

**Exit:** the named finite-dimensional adapter is working and tested, with canonical-state preservation and no second law. The view answers interface questions by declared mathematical choices. Reading §7 row by row, rows 1,2,8,9 have such declared answers; row 5 has a fixed orientation but unresolved physical scale, and four further rows remain physically open. Thus five rows retain unresolved physical content; the original “three of nine” scoring is not a validation count. Physical relevance/units/extraction, a phase generator and time scale, seam conditions and justified mode selection are still absent. There is no field interpolation, surface-area identification, ambient axial-vector interpretation or mesh deformation. **The broader reconstruction remains unfinished.** Z_chiral has no imposed decay envelope; need not decay. The existing Target-B acceptance and distinction between the SRG cycle and Paper-A evolution remain intact.
