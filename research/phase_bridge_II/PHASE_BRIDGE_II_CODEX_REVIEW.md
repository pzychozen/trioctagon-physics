# Phase Bridge II — independent Codex verification

Date: 2026-09-21. Baseline: `562fbb5d82b1d05937fda4929eca615e6b8991a1`.

**PHASE_BRIDGE_II_CORE_RESULT = CONFIRMED_WITH_ASSUMPTION.** The oriented tangent-space metric and complex structure give the stated symplectic form exactly. The specified isotropic quadratic Hamiltonian then gives a rigorous phase flow, with the **negative** sign under the stated convention. This is conditional mathematical dynamics; it does not derive a physical observable, a frequency scale, or admission into `kernel_physics`.

The report is not confirmed without corrections. Its later positive-frequency sign conflicts with §3; its third-harmonic equilibrium description is incomplete; its identification of splay states with an entire transverse plane is false; its proposed scalar-amplitude loop chirality is identically zero; and its proof of algebraic independence is insufficient. The useful independence conclusion is nevertheless independently proved below, including actual algebraic independence of the four real polynomial outputs.

## Source and preservation

Claude's original was copied byte-for-byte to [PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md](PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md).

- Original: `C:/TORMENT/TRIOCTAGON_new/research/phase_bridge_II/PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md`.
- SHA-256: `e9bc4cf19d5292aa26e69095a75f9f7a64280b11292e8e33d2020a3f03e47b57`.
- Size: 35,427 bytes. References below use the copied original's section and line numbers.

The mathematical checks were written independently from the stated formulae. No Claude helper code was imported. Read-only calls to the current clean geometry/dynamics modules check coordinate-frame and one-step compatibility; no historical kernel was opened. No frozen manuscript, kernel file, first-bridge file, or original Claude report was modified. No physics was added to the kernel.

## Claim ledger

The six disposition labels below classify the claims **as written**, with the smallest required qualification or correction. A repaired proof in this review does not edit Claude's original. Repeated statements in §§13–15 and the original final block inherit the corresponding disposition.

| ID | Original location and claim | Disposition | Independent finding / smallest correction |
|---|---|---|---|
| C01 | §0: normals, tangent frames, encoding, frozen update | CONFIRMED_EXACT | The coordinate derivatives give the reported frames. The frozen map has no independent frequency or time-step parameter. |
| C02 | §2: compatible triple, area form, flat Kähler space | CONFIRMED_EXACT | On the selected oriented vector planes, the form matrix is `-J`, while the complex-structure matrix is `J`. The constant form is closed and nondegenerate. |
| C03 | §3: isotropic H gives negative-sign phase rotation | CONFIRMED_WITH_ASSUMPTION | Exact given the added H, rates, and contraction convention; physical meaning remains unselected. |
| C04 | §3, line 82: `H ≥ 0` with preceding `ν_i ∈ R` | WORDING_CORRECTION | Nonnegativity requires `ν_i ≥ 0`; a positive definite per-face quadratic requires `ν_i > 0`. At zero rate the flow is trivial. |
| C05 | §§7,9,13.5/final block: `+iνΩ` identified with §3's generator | CONTRADICTED | For the same ν and conventions, use `-iνΩ` and `exp(-iνh)`. An explicit renaming of the signed frequency would also repair it. |
| C06 | §4: C3 requires equal face frequencies | CONFIRMED_WITH_ASSUMPTION | Necessary and sufficient for the specified **diagonal, uncoupled** quadratic/generator. It is not a constraint on every possible C3-invariant quadratic. |
| C07 | §4: equal rates retain proper spatial group; mirrors reverse flow | CONFIRMED_WITH_ASSUMPTION | Correct for the common-rate Hamiltonian. For unequal rates a mirror must also preserve H to reverse this same system. At ν=0 the flow is identity. Equal rates do not retain *only* C3. |
| C08 | §5: independent U(1) actions and three conserved charges | CONFIRMED_WITH_ASSUMPTION | Conserved actions are `Q_i=norm(v_i)^2/2`, independently on a dense open set. They are mathematical moment-map quantities, not established physical charges. |
| C09 | §5: free equal-rate U(3), temporal U(1), basis symmetry | CONFIRMED_WITH_ASSUMPTION | U(3) is the norm-preserving complex-linear symmetry group; equation covariance alone permits GL(3,C). Temporal U(1) is nontrivial only for nonzero ν. U(3) need not preserve selected face observables. |
| C10 | §§5,12: nonlinear subgroup “roughly U(1) ⋊ C3” | WORDING_CORRECTION | Specify coefficients, domain, and which fields are present. Common phase is central; equal k admits all S3 permutations. The zero-amplitude extension need not have full common U(1). |
| C11 | §§2,10: determinant-weighted anti-symplectic law | CONFIRMED_EXACT | Holds for all twelve induced tangent actions. |
| C12 | §10, line 219: all improper spatial symmetries are involutions | CONTRADICTED | All are anti-symplectic; **mirrors** are involutions. `C3 σ_h` is improper and has order six. |
| C13 | §6: standard oscillator/Kähler mechanics and no novelty claim | CONFIRMED_WITH_ASSUMPTION | The oscillator mechanics follows after the specified H is supplied. No geometric or physical inevitability is established. |
| C14 | §7: pre-sync is forward Euler of the negative gradient | CONFIRMED_EXACT | Algebraically `A_h=I+hA`, with the frozen step at h=1. This does not assert exact-flow equality or physical time calibration. |
| C15 | §7: Stuart–Landau / complex Ginzburg–Landau identification | CONFIRMED_WITH_ASSUMPTION | With the sign corrected, this is the isochronous Stuart–Landau algebraic form with real cubic/diffusive coefficients. A supercritical Hopf interpretation requires its usual nondegeneracy/sign assumptions, not merely the written polynomial. |
| C16 | §8: “Kuramoto–Sakaguchi” | WORDING_CORRECTION | Use **identical-frequency, zero-phase-lag, pure third-harmonic Kuramoto phase model on K3**. It is a zero-lag specialization of the more general phase-lag family. |
| C17 | §8.1: relative equilibria require each pairwise sine to vanish | CONTRADICTED | Sums can cancel. `(0,2π/9,4π/9)` is an explicit missing equilibrium. |
| C18 | §8.2: harmonic m gives m distinct locked families | CONTRADICTED | No such general count follows. The attractive third-harmonic synchronized class here has **nine labelled relative branches**, not three. |
| C19 | §8.3: in-phase and ±120° states stable for K>0 | CONFIRMED_WITH_ASSUMPTION | They are transversely attracting **modulo the common phase**, with exact transverse eigenvalues `-9K,-9K`; the full Jacobian also has zero. Other equilibria exist. No basin claim is verified. |
| C20 | §8.4, line 186: splay families and geometric transverse plane “coincide as sets” | CONTRADICTED | Splay states lie in two complex Fourier eigenlines inside the complex transverse space. They do not fill it and are C3 eigenstates, not fixed vectors. Use `u-perp` rather than the unrelated ring-sector symbol `V3-perp`. |
| C21 | §8.5: geometry does not force harmonic 3 | CONFIRMED_EXACT | Relabelling covariance holds for every integer harmonic. |
| C22 | §§8,9: synchronization is phase-coordinate Euler | CONFIRMED_EXACT | Its lifted Cartesian update is an exponential of the frozen phase increment, not Cartesian forward Euler of the phase field. |
| C23 | §9: legitimate first-order splitting | PROOF_INCOMPLETE | Repair requires an h-family, scaling of both substeps, and a smooth domain away from zero amplitudes. A complete conditional proof is given below. It approximates A+B, not A+B minus iνΩ. |
| C24 | §9, line 206: h=1 is necessarily large/far from exact flow; no simple autonomous realization | CONTRADICTED | The zero-field case is exact at h=1; small coefficients can give small errors. No blanket non-embeddability claim is proved. Replace by “generally not exact; h=1 has no automatic accuracy guarantee.” |
| C25 | §9: physical time is not supplied by the discrete step | CONFIRMED_WITH_ASSUMPTION | Dimensionless step indexing is valid. Physical time units/rates are extra inputs; a small-h family establishes numerical consistency, not a physical clock. |
| C26 | §11.1: Z common-phase, conjugation, permutation, mirror laws | CONFIRMED_EXACT | All laws hold as channel-space algebra. Physical parity/handedness interpretation remains additional. Z is not a readout implemented in the current clean physics kernel. |
| C27 | §11.2: J_eff has phase weight +1 | WORDING_CORRECTION | The **complex cubic** has weight +1. Its imaginary part mixes with the real part; J_eff alone is not a complex one-dimensional covariant. Non-invariance and conjugation oddness are correct. |
| C28 | §11.2: cyclic permutations mix cubic monomials | CONFIRMED_EXACT | The triple indexed by the conjugated channel permutes normally. The selected B component is not cyclic-invariant. |
| C29 | §11.2, line 249: closed-loop product provides a chiral plaquette scalar | CONTRADICTED | That product is `abs(Ω1 Ω2 Ω3)^2`, real nonnegative; its imaginary part is identically zero. It supplies no nontrivial chirality for these scalar amplitudes. |
| C30 | §11.2: cyclic bilinear sum equals sum of Z components | CONFIRMED_EXACT | Correct with the written cyclic order; it is not adopted as a new kernel readout. |
| C31 | §11.2, line 250: different degrees prove algebraic independence | PROOF_INCOMPLETE | Degrees alone do not prove it. A same-Z/different-J witness and a nonzero rank-four Jacobian minor independently establish the useful conclusion and the polynomial independence claim. |
| C32 | §12: both L3 centralizers and the line stabilizer | CONFIRMED_EXACT | Independent eigenspace/block proof below. U(1)×U(2) is also the joint centralizer with a scalar free generator; the free generator alone has U(3) centralizer within U(3). |
| C33 | §13.2: other radial Hamiltonians are possible | CONFIRMED_WITH_ASSUMPTION | A common radial function gives amplitude-dependent rotation and can respect C3. Neither the function nor frequency is geometrically selected. |
| C34 | §13 final paragraph, line 291: **any** positive quadratic gives uniform rotation in the fixed encoding | CONTRADICTED | Restrict to the specified **isotropic per-face** quadratics. A positive anisotropic quadratic need not rotate uniformly in the fixed `q+ip` coordinate. |
| C35 | §§13,15: physical observable, frequency scale, CP interpretation | UNRESOLVED | Not derived or admitted. “No field theory ... exists yet” can only mean none is provided by these sources; it is not an impossibility theorem. No CP/charge extension is examined here. |
| C36 | §13 final paragraph: “Everything weaker ... geometry-forced phase” | WORDING_CORRECTION | A geometry-forced dynamical phase would be a **stronger**, not weaker, assertion. |
| C37 | §§1,14/final block: no execution vs reported conversational scratch checks | UNRESOLVED | Neither execution history is inferred. This review records only the actual Codex execution described below. |

## 1. Compatible form and Hamiltonian sign

**CONFIRMED_EXACT.** In each fixed frame `(t_i,e_z)` the metric is I2, and

```text
J = [[0,-1],[1,0]],       J(q,p)=(-p,q).
ω(v,w) = (Jv) dot w = q_v p_w - p_v q_w.
Matrix(ω) = J^T = -J = [[0,1],[-1,0]].
ω = dq ∧ dp;  ω(v,Jw)=g(v,w);  det Matrix(ω)=1.
```

The form is constant, hence closed on the vector plane. J is constant, orthogonal, and integrable there. Thus this is a flat Kähler vector space; the direct sum has real dimension six. This statement concerns selected tangent-vector spaces, not a smooth global tangent bundle through the creases of the polyhedral shell.

**CONFIRMED_WITH_ASSUMPTION.** Adopt the report's convention `i_X ω=dH` and its isotropic Hamiltonian `H=ν(q²+p²)/2`. Contraction gives

```text
i_X(dq ∧ dp) = qdot dp - pdot dq = νq dq + νp dp,
qdot=νp,  pdot=-νq,
vdot=-νJv,  Ωdot=-iνΩ,  Ω(t)=exp(-iνt) Ω(0).
```

For positive definite H, require ν>0; ν=0 gives no phase motion. The identity remains algebraically true for negative ν, with reversed direction and a negative quadratic. The positive sign in §§7 and 9 is incompatible with the same H and convention. The smallest repair is a minus sign wherever the same generator is invoked, including the phase model's natural frequency if identified with this ν. The phase model can alternatively use an independently named signed frequency `ω0=-ν`.

**CONTRADICTED.** “Any positive quadratic” is too broad. For `H=(q²+2p²)/2`, the Hamiltonian velocity is `(2p,-q)`; no one constant ν makes this equal `-νJ(q,p)` for every q,p. Isotropy in the *fixed metric/encoding*, not positivity alone, is essential. For a radial H=f(q²+p²), the rate is `2 f'(q²+p²)`; that is an additional Hamiltonian choice.

## 2. Frequency degeneracy, equation symmetry, and mirrors

**CONFIRMED_WITH_ASSUMPTION.** For `Dν=diag(νA,νB,νC)`, the cyclic face action obeys `[R,Dν]=0` exactly when all three diagonal entries agree. This proves the report's degeneracy condition for the uncoupled diagonal ansatz. A general C3-invariant Hermitian quadratic need not have one rate: `Pb+2Pperp` commutes with R but has mode eigenvalues 1,2,2. The uncoupled isotropic-per-face premise must remain visible.

For arbitrary diagonal rates, the free equations conserve `Q_i=abs(Ω_i)^2/2` and admit independent phase changes. The Q_i generate the negative-oriented phase rotations with `i_X ω=dH`; the positive-oriented action uses generators `-Q_i`. Their differentials are independent where all three components are nonzero. These are classical mathematical actions/moment maps, without an identified physical charge.

For a common nonzero rate, the equation generator is a complex scalar. Every complex-linear invertible map commutes with it, but imposing the Euclidean norm restricts that group to U(3). Common temporal evolution is a diagonal U(1) subgroup. At ν=0 it is the trivial flow; if one ignores the specified complex structure, the zero equation even admits all real orthogonal transformations.

**UNRESOLVED.** Internal equation symmetry does not select physical observables. A unitary mixing two channels preserves total norm while changing both labelled face actions. Keeping every Q_i as an individually fixed observable restricts to diagonal phases; preserving their set permits permutations as well. There is no proof that a general U(3) basis mixing is a physical symmetry of the underlying shell/observables.

**CONFIRMED_EXACT.** Let Γ be an induced tangent isometry of a spatial symmetry G. Since `ΓJ=det(G) JΓ` and Γ is orthogonal,

```text
ω(Γv,Γw) = g(JΓv,Γw) = det(G) g(ΓJv,Γw)
          = det(G) ω(v,w).
```

This proves the pullback law for all group elements, independently of the Hamiltonian. Horizontal and vertical mirrors are anti-symplectic involutions, acting as `Ω -> conjugate(Ω)` and `Ω -> -T conjugate(Ω)`, where T swaps A,C. An anti-symplectic G reverses the same Hamiltonian flow when H is G-invariant; the common-rate H has this property. For unequal rates the horizontal mirror still preserves H, while the vertical one requires νA=νC. An improper element need not square to identity: `R Γ_h` has order six.

**WORDING_CORRECTION.** A nonzero L3 coupling narrows the unitary symmetry to its centralizer. The entrywise cubic by itself permits independent phases and, at equal k, all S3 permutations. On the nonsingular domain the combined fields admit common U(1) and permutations preserving k; these factors commute. The frozen Arg0 extension at zeros does not have unrestricted common-U(1) equivariance when synchronization is nonzero. Therefore no universal full-map group “U(1) ⋊ C3” follows from the report. Parameter degeneracies and removed terms can enlarge the group further.

## 3. Euler parent and a rigorous splitting statement

**CONFIRMED_EXACT.** Denote the complex pre-sync vector field by A and its real potential by V:

```text
A_i(z) = ε z_i(k_i-abs(z_i)^2) + g (L3 z)_i.
V = ε sum_i [abs(z_i)^4/4 - k_i abs(z_i)^2/2]
    + (g/2) sum_{i<j} abs(z_i-z_j)^2.
A = -gradient_R6 V.
```

Direct differentiation gives the stated field. Forward Euler is `A_h(z)=z+hA(z)`; h=1 equals the frozen pre-sync rule. This is an algebraic embedding into a family of numerical methods, without inserting a new clock into the kernel. A gradient flow decreases V continuously, but the finite Euler update has no unconditional energy-decrease or accuracy guarantee.

**CONFIRMED_WITH_ASSUMPTION — corrected splitting theorem.** Work on `D=(C without 0)^3`. Fix real ε,g,λ,k and define

```text
f_i(z) = sum_{j != i} sin[3(arg z_j - arg z_i)],
B_i(z) = i λ z_i f_i(z),
S_h(z)_i = z_i exp[i h λ f_i(z)],
F_h = S_h composed with A_h.
```

The angle-dependent functions are smooth on D despite the lack of a globally single-valued arg: their sines can be expressed through the normalized nonzero complex components. Take a compact trajectory neighborhood separated from every zero coordinate. For sufficiently small h, the fields and derivatives are bounded there and A_h stays inside D. Taylor expansion gives

```text
S_h(z) = z + h B(z) + h² C(z) + O(h³),
C_i(z) = -(λ²/2) z_i f_i(z)^2,
F_h(z) = z + h[A(z)+B(z)] + h²[DB(z) A(z)+C(z)] + O(h³).
```

The exact local flow of `zdot=A(z)+B(z)` has expansion

```text
Φ_h(z) = z + h(A+B) + (h²/2) D(A+B)(A+B) + O(h³).
```

Consequently the local defect is O(h²). Bounded derivatives give a one-step Lipschitz factor `1+O(h)`; the usual finite-time error recurrence then gives global O(h) error while exact and numerical trajectories stay in the chosen regular neighborhood. This is a **first-order splitting with approximate Euler-type substeps**, not a composition of exact Lie–Trotter subflows. The S substep is Euler in phase coordinates and preserves radii exactly; it is not Cartesian Euler `z+hB(z)`.

The corresponding call to the existing kernel uses `eps=hε`, `g=hg`, `phase_strength=hλ`, with k unchanged. No fixed h=1 map alone establishes a convergence order: the order statement is about this explicit h→0 family. It does not establish that h=1 is large, small, or physically calibrated. At the zero stratum, the Arg0 extension is generally discontinuous and the smooth proof does not apply; when λ=0 the phase field vanishes and ordinary gradient Euler has no such phase singularity.

**CONTRADICTED for the enlarged target.** This family is not first-order consistent with `zdot=A+B-iνz` at fixed nonzero ν: its first-order increment lacks `-iνz`. Including that target requires an explicitly added phase step `exp(-iνh)` or an explicitly stated rotating-frame formulation. On D, common-phase equivariance means `z=exp(-iνt)w` converts `wdot=A(w)+B(w)` into the enlarged equation. Neither interpretation is silently imposed on the frozen kernel.

**CONFIRMED_WITH_ASSUMPTION.** With the corrected sign, the amplitude-plus-free-phase ODE has the algebraic isochronous Stuart–Landau form `zdot=(εk-iν)z-ε abs(z)^2 z`, plus real graph coupling. Calling it a generic Hopf bifurcation requires, for example, a nonzero frequency and an appropriate varying growth rate/cubic sign. This mathematical identification is not a physical derivation of the oscillator or time scale.

## 4. Third-harmonic locking and analytic stability

Use the **identical-frequency, zero-phase-lag, pure third-harmonic Kuramoto model**

```text
φdot_i = ω0 + K sum_{j != i} sin[3(φ_j-φ_i)].
```

If its natural frequency comes from the Hamiltonian above, `ω0=-ν`. An independent phase model can use any separately named ω0. Remove the common drift to study relative equilibria.

**CONFIRMED_EXACT.** For the coupling field the Jacobian is

```text
D_ij = 3K cos[3(φ_j-φ_i)]                       (i != j),
D_ii = -3K sum_{j != i} cos[3(φ_j-φ_i)].
```

It is symmetric and has zero row sums. At every branch `φ_i=Φ+2πk_i/3`, it equals `3K L3`, with spectrum `0,-9K,-9K`. The zero is the common-phase direction. Thus for K>0 these circles are locally asymptotically attracting in relative phase; for K<0 they repel transversely; for K=0 there is no restoring dynamics. In the laboratory frame with nonzero ω0, the circles are periodic phase-locked motions rather than isolated fixed points.

There are nine labelled relative branches after setting k_A=0 and allowing k_B,k_C in {0,1,2}. They comprise one in-phase branch, two ±120° cyclic splay branches, and six two-cluster branches. The special ±120° states are not the whole attractive family.

**CONTRADICTED — pairwise-zero condition as necessity.** Put `θ_i=3φ_i`. The coupling sum can vanish by cancellation; `φ=(0,2π/9,4π/9)` is a direct witness. For completeness, all relative equilibria for K≠0 can be classified without a numerical scan. The sum of phase velocities from coupling is zero, so a common relative-locking frequency must have zero coupling contribution. Write `r exp(iψ)=sum_j exp(iθ_j)`. Then each condition is `r sin(ψ-θ_i)=0`.

- For r≠0, every θ_i is ψ or ψ+π. This gives synchronized θ or an antipodal 2+1 split.
- For r=0, three unit phasors sum to zero, hence form an equilateral triple: θ-splay.

Their spectra are obtained by substituting their cosines into D:

| Type in θ=3φ | Transverse eigenvalues | K>0 | K<0 |
|---|---|---|---|
| Synchronized | `-9K, -9K` | Attracting modulo common phase | Repelling modulo common phase |
| Antipodal 2+1 | `-3K, 9K` | Saddle | Saddle |
| Equilateral splay | `9K/2, 9K/2` | Repelling modulo common phase | Attracting modulo common phase |

This gives 9, 27, and 18 labelled relative branches respectively when lifted to φ, or 54 circles in total; at K=0 this discrete classification is replaced by the whole relative phase torus. These counts concern identical frequencies and three labelled all-to-all nodes only. No basin sizes or global attraction claims are made.

For the phase-only **discrete** h-step, the synchronized transverse multipliers are `1-9hK`. For h>0, strict linear transverse attraction requires `0<hK<2/9`; equality has unit spectral radius and is inconclusive at this linear level. These are not stability results for the full amplitude/synchronization kernel.

**CONTRADICTED — splay versus transverse space.** Equal-amplitude ±120° vectors lie in the two nontrivial complex C3 eigenlines, inside the complex dimension-two space orthogonal to u. They do not fill it: `(1,i,-1-i)` has sum zero but unequal amplitudes. They also are not fixed vectors of R, only eigenvectors up to phase. A real geometric transverse plane, its complexification, and a complex Fourier eigenline must be distinguished.

**CONFIRMED_EXACT.** For any positive integer m, replacing 3 by m in the pairwise sine sum preserves permutation covariance, by relabelling the summation index. No C3 argument here selects harmonic three.

## 5. Chiral transformation laws and non-determination

Let `Ω=a+ib`, with a,b real channel vectors, `Z=a cross b`, and `M=Ω_A conjugate(Ω_B) Ω_C`. Write `M=X+iJ`, so `J=J_eff`.

**CONFIRMED_EXACT**, with the real-versus-complex distinction indicated:

| Operation | Z transformation | J_eff transformation |
|---|---|---|
| Common phase `Ω -> exp(iα)Ω` | Z unchanged | `J -> cos(α)J + sin(α)X` |
| Conjugation | `Z -> -Z` | `J -> -J` |
| Channel permutation P | `Z -> det(P) P Z` | Permutes the triple of imaginary cubic monomials indexed by their conjugated channel; the B component is not generally fixed |
| Horizontal spatial mirror | `Z -> -Z` | `J -> -J` |
| Vertical spatial mirror `Ω -> -T conjugate(Ω)` | `Z -> T Z` | `J -> J` because T fixes the conjugated B index |

For the common phase, the real vectors transform as `a'=cosα a-sinα b`, `b'=sinα a+cosα b`, giving Z unchanged. Orthogonal cross-product covariance gives the permutation law. The spatial-mirror laws follow by composition. The **complex** M transforms as `exp(iα)M`; its imaginary component alone is not a weight-one complex scalar. Cyclic invariance fails, for example, at `(1,i,1)`, where J=-1, while the active cyclic permutation `(1,1,i)` gives J=+1.

**CONTRADICTED.** The proposed product in §11.2 simplifies to

```text
(Ω1 conjugate(Ω2))(Ω2 conjugate(Ω3))(Ω3 conjugate(Ω1))
    = abs(Ω1)^2 abs(Ω2)^2 abs(Ω3)^2.
```

Its imaginary part vanishes identically, including at zeros; where nonzero its phase is zero. Independent edge variables could define a different loop observable, but none are introduced here. The separately proposed bilinear cyclic sum does equal the sum of Z's three components.

**CONFIRMED_EXACT — Z does not determine J.** Take

```text
Ω=(1,i,1),       iΩ=(i,-1,i).
Z(Ω)=Z(iΩ)=(-1,0,1),
J_eff(Ω)=-1,     J_eff(iΩ)=0.
```

Every amplitude in this witness is nonzero. Therefore no single-valued function of Z, polynomial or otherwise, determines J on the full state space. More generally a common-phase orbit fixes Z while rotating the complex cubic.

**PROOF_INCOMPLETE in the original; independently repaired.** Different degrees do not prove algebraic independence: x² and x⁴ have different degrees and satisfy a polynomial relation. A correct proof here uses the real polynomial map `(a,b) -> (Zx,Zy,Zz,J)`. At `a=(1,2,1)`, `b=(1,1,-1)`, the Jacobian minor in columns `(a0,a1,a2,b0)` has determinant **12**. Hence the map has rank four at that point and its image contains an open subset of R4. Any polynomial relation among the four outputs would vanish on that open subset and thus be the zero polynomial. The four real polynomial functions are indeed algebraically independent. This proves the claim independently rather than accepting the degree argument. It gives no physical interpretation to either readout.

## 6. Independent centralizer proof

**CONFIRMED_EXACT.** The orthonormal basis `U=[u,x,y]` gives `U* L3 U=diag(0,-3,-3)`. If a complex-linear T commutes with L3, then for every eigenvector v of eigenvalue λ,

```text
L3(Tv)=T(L3v)=λTv.
```

Thus T preserves the balanced complex line and transverse complex two-plane. Conversely every block operator preserving these spaces commutes with their scalar eigenvalues. The unrestricted complex commutant is therefore exactly `M1(C) direct-sum M2(C)` in this basis.

Requiring T unitary gives blocks `a in U(1)` and `V in U(2)` independently:

```text
Centralizer_U(3)(L3) = U [ U(1) × U(2) ] U*.
Centralizer_SU(3)(L3) = U [ S(U(1) × U(2)) ] U*,
S(U(1) × U(2)) = {diag(a,V): a det(V)=1}.
```

The conventional notation suppresses the change of basis U. The SU subgroup is isomorphic to U(2) by `V -> diag(det(V)^(-1),V)`. Fixing the **line** permits its phase to compensate det(V); fixing the unit vector u itself would instead leave SU(2) inside SU(3). These are exact centralizer statements, not a proof of a symmetry of the nonlinear update, a physical gauge group, or a Standard-Model identification.

## 7. Execution provenance and verification scope

**UNRESOLVED — Claude execution provenance.** The source's §1 (line 38) and final `NOTHING_EXECUTED = TRUE` (line 332) assert no execution. §14 labels numerical checks as suggestions. The user reports a conversational mention of scratch numerical checks, but no scratch transcript, command, input, or output was supplied with this work order. This review neither infers that those runs happened nor that they did not. The original assertion is preserved unchanged as source evidence, not adopted as a Codex-verified fact.

**CONFIRMED_EXACT — what Codex actually ran.** The new [verification script](verify_phase_bridge_II.py) executes **53 predicates**: 45 symbolic/combinatorial, 4 numerical (including one expected counterexample), and 4 integrity predicates. All passed. Predicate counts include grouped subcases and are not counts of independent theorems. The four numerical predicates cover:

1. One fixed nonzero three-state fixture at h=`0.01,0.005,0.0025,0.00125`, comparing the h-scaled existing kernel to an independently formed composition.
2. Comparison to the second-order Taylor expansion of the exact A+B flow, with local-error ratios approximately `4.00538,4.00268,4.00134` and convergence to the analytically derived h² defect coefficient.
3. A fixed pre-sync forward-Euler identity.
4. The known zero-stratum common-phase counterexample, discrepancy about `0.09317017645`.

No reference ODE trajectory was integrated. No random states, basin scan, stability atlas, historical code, old 41-test suite, or old first-bridge audit was run. The comparison errors are floating-point diagnostics; the local/global order argument, full equilibrium classification, and Lie-group centralizer proof are analytic arguments above. A source edit making the numerical predicate explicitly retain the formula-error value and a new anisotropic-quadratic predicate were followed by a final rerun of this new script only. The final results files record that complete execution, not an invented account of Claude's earlier work.

Runtime: Python 3.11.15, SymPy 1.14.0, NumPy 2.4.4 in the existing conda `torment` environment. Reproduction command from this repository:

```powershell
& 'C:/Users/Notandi/miniconda3/envs/torment/python.exe' -I -S -B -X utf8 research/phase_bridge_II/verify_phase_bridge_II.py
```

The script writes only its two result files in this new directory. It checks all 58 pre-existing tracked files against the named baseline and preserves their bytes and modification times. It separately verifies Claude's copied/original report hash and preservation of the original modification time. The source-copy hash appears in the JSON result. No pre-existing manifest or checksum file is changed; these new research files are not silently added to the frozen archive's checksum list.

## 8. Admission boundary

**CONFIRMED_WITH_ASSUMPTION.** The surviving result is a coherent conditional Hamiltonian model on the selected kinematic tangent planes, together with exact algebraic observables and centralizers. It is suitable as a mathematical input to the next carefully scoped investigation **after using the corrected statements in this review**.

**UNRESOLVED.** A physical face observable, physical phase generator/frequency scale, and interface to the fixed nonlinear kernel remain unselected. The original report needs the enumerated corrections before being treated as an accepted source without this review. Readiness is therefore **PARTIAL**. No next bridge, charge/CP construction, host geometry, or physics implementation has been undertaken.

```ini
PHASE_BRIDGE_II_CORE_RESULT = CONFIRMED_WITH_ASSUMPTION
SYMPLECTIC_STRUCTURE = CONFIRMED_EXACT
HAMILTONIAN_PHASE_FLOW = CONFIRMED_WITH_ASSUMPTION_NEGATIVE_SIGN
ANTI_SYMPLECTIC_MIRRORS = CONFIRMED_EXACT
EULER_PARENT = CONFIRMED_EXACT_FOR_PRESYNC_GRADIENT
SPLITTING_CLAIM = CONFIRMED_WITH_ASSUMPTION_SMALL_H_ON_NONZERO_DOMAIN_FOR_A_PLUS_B
THIRD_HARMONIC_STABILITY = CONFIRMED_EXACT_MODULO_COMMON_PHASE_WITH_CORRECTED_CLASSIFICATION
Z_CHIRAL_TRANSFORMS = CONFIRMED_EXACT
J_EFF_TRANSFORMS = CONFIRMED_EXACT_WITH_REAL_COMPONENT_MIXING
J_EFF_DETERMINED_BY_Z_CHIRAL = NO
L3_U3_CENTRALIZER = U(1) x U(2)
L3_SU3_CENTRALIZER = S(U(1) x U(2))
READY_FOR_NEXT_PHYSICS_BRIDGE = PARTIAL
KERNEL_PHYSICS_MODIFIED = NO
```
