# First bridge: folded geometry to three complex state components

Date: 2026-09-21. Research result, not a change to either frozen paper or kernel.

## Scope and result

**EXACT.** The current geometry supplies a three-face permutation space, its balanced/transverse decomposition, and the unweighted adjacency operator used by Paper A:

\[
V=\mathbb R^{\{A,B,C\}}=\mathbb Ru\oplus u^\perp,
\qquad u=(1,1,1)^T/\sqrt3,
\qquad L_3=-3P_\perp.
\]

**EXACT.** The oriented transverse space is one real two-plane. Separately, the three face-center tangent planes form a real six-dimensional space with a geometric complex structure, once an ambient orientation and outward normals are chosen. Thus geometry provides a concrete *kinematic candidate* for \(\mathbb C^3\); it provides more than just a reason to use three labels.

**UNRESOLVED.** Neither frozen baseline identifies tangent vectors, perimeter waves, or oscillator quadratures with the dynamical state of Paper A. No field, observable, excitation mechanism, or continuous phase evolution on those geometric planes has been derived. Consequently the bridge to **three complex dynamical degrees of freedom** is conditional, not complete.

**DERIVED_FROM_STATED_ASSUMPTION.** A particularly direct circulating-wave proposal fails to provide the desired state: imposing single-valued scalar continuity along the welded seams on one first Fourier harmonic per octagon perimeter reduces six real coefficients to one. This is an obstruction to that specified proposal, not a no-go theorem for all fields on the shell.

The latest user instruction limits this work to the first bridge. The \(\mathbb C^3\otimes\mathbb C^2\) lift, recursion, chirality readouts, SRG, moving projectors, DMQPF, and field-theory extensions are deferred. No historical architecture is restored. No Paper D is drafted.

## Evidence and notation

The primary sources are [Paper C v0.3.1](C:/TORMENT/TRIOCTAGON_new/reconstruction/papers/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md), especially §§2–5 and 9, and [Paper A v0.5.1](C:/TORMENT/TRIOCTAGON_new/reconstruction/papers/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md), especially §§1 and 6. The implementation reference is `kernel_physics/geometry.py` and `kernel_physics/dynamics.py`. Authoritative source paths:

- Paper C: `C:/TORMENT/TRIOCTAGON_new/reconstruction/papers/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md`.
- Paper A: `C:/TORMENT/TRIOCTAGON_new/reconstruction/papers/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md`.
- Kernel: `C:/TORMENT/TRIOCTAGON_new/kernel_physics/`.
- Secondary S02: `C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOctagon_E8-SU3-Geometry.pdf`, PDF pp. 14–15 (§9), p. 20 (§12).
- Secondary S03: `C:/TORMENT/TRIOCTAGON_new/pdfs_quantum/A_structural_reconstruction_of_quantum_mechanics-1.pdf`, PDF pp. 17–19 (§13).

**HISTORICALLY_INTENDED.** S02 §9 proposes three phase-linked circulation modes and a phase-matching interface as a conceptual interpretation. Its §12 exhibits the same balanced vector and transverse basis used below. These motivate questions; they do not establish a field or boundary-value problem for the frozen Paper-C surface. Historical tetrahedral/host interpretations are not imported. S03 supplies a conditional phase-plane argument, examined only to determine its applicability here. No new literature was searched.

`source_manifest.json` records the exact source hashes. The two archives and other PDF extracts already inventoried before the scope correction remain as provenance; their operators are not used in this first-bridge derivation. No further archive investigation or historical code execution was performed after narrowing.

Throughout, \(C_3\) denotes the cyclic group and \(\mathbb C^3\) the complex vector space. “Mode” below means a representation or specified operator mode, not an automatically established physical vibration. Statement labels distinguish exact algebra, results conditional on stated assumptions, finite numerical checks, historical intent, candidate interpretations, unresolved interfaces, and contradicted implications.

## 1. Three face channels, derived without complex amplitudes

**EXACT — face representation.** Label the actual panels \(A=P_1,B=P_2,C=P_3\). Their centers are

\[
c_A=(-1/4,\sqrt3/4,0),\quad c_B=(0,0,0),\quad
c_C=(1/4,\sqrt3/4,0).
\]

The Paper-C positive 120° rotation cycles \(A\to B\to C\to A\). On column coefficients attached to faces it acts by

\[
R=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]

The vertical mirror \(x\mapsto-x\) swaps A and C, with matrix \(T\); the horizontal mirror fixes each face label. Thus the real face permutation representation of \(D_{3h}\) factors through \(S_3\). It is not a faithful representation of the whole spatial group.

**EXACT — balanced line and transverse plane.** With the counting inner product, \(Rv=v\) requires all three entries equal. Positivity and unit norm select \(u=(1,1,1)^T/\sqrt3\). Orthogonality gives

\[
u^\perp=\{v:v_A+v_B+v_C=0\},\qquad
P_{\rm bal}=uu^T=\tfrac13(I+R+R^2),\quad P_\perp=I-P_{\rm bal}.
\]

Equal face-area weighting changes the inner product only by a common scalar. A useful orthonormal basis of the transverse plane is

\[
x=(1,-1,0)^T/\sqrt2,\qquad y=(1,1,-2)^T/\sqrt6.
\]

The real two-plane is irreducible under \(C_3\): a real invariant line would give a real eigenvalue of its 120° rotation, which has none. This proves the stated real \(\mathbf3=\mathbf1\oplus\mathbf2\) decomposition.

**EXACT — adjacency and the kernel.** Each face shares exactly one seam with each other face. Choosing one equal weight per adjacency gives

\[
L_3=R+R^2-2I=\mathbf1\mathbf1^T-3I=-3P_\perp.
\]

This equals the existing kernel's matrix. More generally, matrices commuting with the full face-permutation action have constant diagonal and constant off-diagonal entries, hence are \(aP_{\rm bal}+bP_\perp\). Requiring the balanced vector to be annihilated leaves a scalar multiple of \(P_\perp\).

**DERIVED_FROM_STATED_ASSUMPTION.** This identifies the *form* of a uniform, symmetry-preserving face coupling with zero row sums. It does not derive its physical use, magnitude, sign, time scale, or Paper A's coefficient \(g\). Unit seam weights are an operator convention, not a measured conductance.

**EXACT — what geometry alone encodes.** If a scalar-channel encoding of the fixed unlabelled shell is required to be equivariant under its stabilizer, its value must satisfy \(RE(\mathcal G)=E(\mathcal G)\); it lies on the balanced line. It cannot supply arbitrary channel excitations without additional data. This statement concerns scalar channels with the permutation action, not every possible vector-valued geometric construction.

## 2. What the cyclic representation does and does not make complex

**EXACT.** Write \(\omega=(-1+i\sqrt3)/2\). The orthonormal complex eigenvectors

\[
v_m=\frac1{\sqrt3}(1,\omega^{-m},\omega^{-2m})^T,
\qquad Rv_m=\omega^m v_m,\quad m=0,1,2
\]

diagonalize the cyclic permutation. For a *real* channel vector, the corresponding coefficients obey \(c_0\in\mathbb R\), \(c_2=\overline{c_1}\). They contain three real degrees of freedom, not three independent complex amplitudes.

**EXACT.** An oriented cyclic ordering selects

\[
J_\perp=\frac{R-R^2}{\sqrt3},\quad
J_\perp^T=-J_\perp,\quad
J_\perp^2=-P_\perp,\quad J_\perp u=0.
\]

It sends \(x\mapsto y\), \(y\mapsto-x\). On \(u^\perp\), it is a complex structure. Moreover

\[
e^{\theta J_\perp}=P_{\rm bal}+\cos\theta P_\perp+\sin\theta J_\perp,
\qquad e^{2\pi J_\perp/3}=R.
\]

**CONTRADICTED.** “The three real channels therefore become \(\mathbb C^3\)” does not follow. The construction gives \(\mathbb R\oplus\mathbb C\) as real spaces after an orientation choice. No real 3-by-3 operator can satisfy \(J^2=-I_3\), since then \((\det J)^2=\det(-I_3)=-1\). The balanced line is explicitly unpaired.

**EXACT.** A reflection reverses this orientation: \(TJ_\perp T=-J_\perp\). Indeed the full face-permutation commutant contains no nonzero skew operator. The continuous group above is an algebraic extension on coefficients. Paper C's Euclidean symmetry group is finite, so every continuous one-parameter group of actual shell isometries is constant. A coefficient-space rotation must not be relabelled a continuous rigid rotation of the shell. The chosen extension also does not fix a physical rotation rate.

## 3. A positive geometric construction: three spatial tangent planes

**EXACT.** There is a different six-real-dimensional space already associated with the geometry:

\[
W_{\rm tan}=T_{c_A}P_A\oplus T_{c_B}P_B\oplus T_{c_C}P_C.
\]

These are tangent *vector spaces*, not the affine panel planes. The outward unit normals from the actual oriented coordinates are

\[
n_A=(-\sqrt3/2,1/2,0),\quad n_B=(0,-1,0),\quad
n_C=(\sqrt3/2,1/2,0).
\]

Given the ambient right-handed orientation, define \(J_i v=n_i\times v\). For tangent \(v\), the vector triple-product identity gives

\[
J_i^2v=n_i(n_i\cdot v)-v=-v,\qquad J_i^T=-J_i.
\]

Consequently \(J_{\rm tan}=J_A\oplus J_B\oplus J_C\) is an orthogonal complex structure on \(W_{\rm tan}\).

For the existing positive vertical axis, put \(e_z=(0,0,1)\) and \(t_i=e_z\times n_i\). Then \((t_i,e_z)\) is an orthonormal oriented tangent frame,

\[
v_i=q_i t_i+p_i e_z,
\qquad E_{\rm tan}(v)_i=q_i+i p_i,
\qquad E_{\rm tan}(J_{\rm tan}v)=iE_{\rm tan}(v).
\]

This is an explicit isometric identification \(W_{\rm tan}\cong\mathbb C^3\), with \(\sum_i\|v_i\|^2=\sum_i|\Omega_i|^2\). Complex structure is supplied by the oriented Euclidean planes, not by an appeal to quantum notation.

**EXACT — transformation qualification.** C3 takes each chosen tangent frame into the next, so it acts on these complex coefficients by the same cyclic permutation. Improper spatial symmetries reverse the complex structure. For the induced tangent action \(\Gamma_G\),

\[
\Gamma_GJ_{\rm tan}=\det(G)J_{\rm tan}\Gamma_G.
\]

In the stated frames, the horizontal mirror gives \(\Omega\mapsto\overline\Omega\), and the vertical mirror gives \(\Omega\mapsto-T\overline\Omega\). This is a real representation with complex-linear proper rotations and conjugate-linear improper symmetries, not the ordinary complex-linear face-permutation representation of all of \(D_{3h}\). In particular, demanding that this geometric horizontal mirror commute with a global complex structure is impossible: its real ±1 eigenspaces each have odd dimension three.

**CANDIDATE_INTERPRETATION.** One may propose one tangent-vector observable or polarization coefficient per face. Its length and tangent direction then become \(|\Omega_i|\) and \(\arg\Omega_i\). This is a concrete candidate for an encoding, not an established physical interpretation.

**UNRESOLVED.** The shell does not supply the three vectors' values, a field from which to extract them, their units, or a law making tangent-vector rotation into dynamical phase. Nor does it select these six coordinates over other vector observables. \(e^{\theta J_{\rm tan}}\) rotates tangent vectors; it does not rotate the full octagonal faces into themselves for every \(\theta\). These three selected fibers are not three proven global eigenmodes of a differential operator on the shell.

## 4. Can perimeter circulation supply the missing planes?

**DERIVED_FROM_STATED_ASSUMPTION — independent loops.** Give each octagon perimeter its own real scalar field, arclength \(\ell=8(\sqrt2-1)\), periodic arclength translation, and the one-dimensional operator \(-\partial_\xi^2\). Its first nonconstant eigenspace is

\[
f_i(\xi)=a_i\cos(2\pi\xi/\ell)+b_i\sin(2\pi\xi/\ell).
\]

The coefficients form a real two-plane with a rotation action under arclength translation. Three *independent* such loops give \(\mathbb R^6\cong\mathbb C^3\). This construction states the field, operator, and harmonic truncation explicitly. None is already specified in Paper C. Translation of a field on an intrinsic perimeter circle is not a continuous Euclidean symmetry of the polygon.

**DERIVED_FROM_STATED_ASSUMPTION — welded scalar continuity.** Now require those scalar fields to be single-valued on shared seam edges. Set \(\xi=0\) at the midpoint of each panel's local right vertical edge, with positive traversal upward there. The midpoint of its opposite edge lies at \(\ell/2\), where traversal is downward. On a seam at height \(z\), put \(\alpha=2\pi/\ell\). Then

\[
f_i^{R}(z)=a_i\cos(\alpha z)+b_i\sin(\alpha z),\qquad
f_i^{L}(z)=-a_i\cos(\alpha z)+b_i\sin(\alpha z).
\]

The actual maps satisfy \(P_i(1/2,z)=P_{i+1}(-1/2,z)\), cyclically. Equality of the right and next left traces throughout the nonzero-length seam interval therefore implies

\[
a_i=-a_{i+1},\qquad b_i=b_{i+1}.
\]

The odd three-cycle forces \(a_A=a_B=a_C=0\), while all \(b_i\) equal one real number. The six-coefficient constraint matrix has rank five. Its one-dimensional nullspace is not preserved by the independent phase-plane complex structure. Reversing the perimeter orientation or changing the arclength origin merely changes the coefficient basis, not this dimension.

For any common fixed harmonic \(n\ge1\), the constraints become

\[
a_i=(-1)^n a_{i+1},\qquad b_i=(-1)^{n+1}b_{i+1}.
\]

Exactly one family survives: uniform b for odd n, uniform a for even n. Thus this entire single-common-harmonic scalar ansatz has one real surviving coefficient. The script computes n=1 and n=2; the general conclusion is the parity argument above, not an executed infinite test.

**EXACT — topology cross-check.** For the existing cellular shell, the oriented boundary matrices have \(\operatorname{rank}\partial_1=17\), \(\operatorname{rank}\partial_2=3\), and \(\partial_1\partial_2=0\). Its edge graph has cycle-space dimension \(21-17=4\), whereas the filled-face shell has \(\dim H_1=21-17-3=1\). The three panel perimeters are boundaries of the actual faces, not three independent noncontractible circulation classes of the surface.

**UNRESOLVED.** Neither calculation excludes three dynamical modes of a suitable field. Face-resolved fields, vector fields, discontinuous traces with an interface law, multiple harmonics, or different operators can change the answer. None is selected here. Continuity in the probe is a stated local scalar-field assumption; it is not an assignment of physical conditions at the two open rims or a global host model.

## 5. Exactly what the phase-plane theorem can contribute

**DERIVED_FROM_STATED_ASSUMPTION.** In using S03 §13, take the transformations explicitly to be a continuous group of real-linear orthogonal maps on a finite-dimensional inner-product space. Its generator K is skew. On every nontrivial invariant real two-plane,

\[
K=\nu\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad K^2=-\nu^2I,
\]

after choosing the plane orientation. A nonzero K on one plane proves only a local complex structure.

**CONTRADICTED — a hypothesis shortcut relevant to this bridge.** “Invariant phase planes span the space” is not equivalent to “every nonzero vector belongs to a nontrivial invariant phase plane.” Although S03 Axiom 13.3 uses both formulations, the stronger one is needed for a common scalar normalization of its generator. The explicit example

\[
K=\operatorname{diag}(J_2,2J_2),\qquad J_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

is skew and generates normalized periodic rotations. Its two coordinate planes span \(\mathbb R^4\), but \(K^2=\operatorname{diag}(-I_2,-4I_2)\). No one scalar rescaling of the phase parameter makes its square \(-I_4\). The vector \(e_1+e_3\) has a four-dimensional Krylov span under K, so lies in no invariant two-plane. This is a targeted applicability check, not a new review of the secondary paper's other claims.

**DERIVED_FROM_STATED_ASSUMPTION — sufficient version with a complete proof.** Suppose instead every nonzero vector lies in a nontrivial K-invariant real two-plane. Then K has no kernel and for every nonzero v, \(K^2v=-\nu_v^2v\). Thus every vector is an eigenvector of the linear operator \(K^2\). Applying it to independent v,w and v+w forces their eigenvalues to be equal. Hence \(K^2=-\nu^2I\), \(\nu>0\), and

\[
J=K/\nu,\qquad J^T=-J,\qquad J^2=-I.
\]

This J is fixed by the specified generator and its time orientation; an inner product alone does not select it. A Hermitian inner product, linear in its first argument, is \(h(v,w)=\langle v,w\rangle-i\langle Jv,w\rangle\). This shows precisely what a real-to-complex construction establishes mathematically, without deriving quantum observables or probabilities.

**EXACT.** A weaker useful construction exists for any invertible skew K: \(J=K(-K^2)^{-1/2}\). It normalizes distinct frequency blocks separately. It requires a supplied invertible generator and does not turn every orbit of the original K into a single-frequency circle. Compositionality of already supplied generators does not create missing local quadratures.

**UNRESOLVED — application to the shell.** The scalar three-channel space fails the universality hypothesis because of its balanced line. The tangent construction has a full kinematic J, but the required interpretation as an intrinsic reversible phase transformation has not been derived. Independent loop coefficients have phase planes before welding; the specified continuous scalar subspace after welding does not. The cited theorem therefore does not fill the missing dynamical premise.

## 6. The smallest explicit conditional interface

**DERIVED_FROM_STATED_ASSUMPTION.** If a model supplies two independent real quadratures per face, \(q,p\in V\), with compatible units and a chosen common phase rotation,

\[
W=V\oplus V,\qquad J(q,p)=(-p,q),\qquad E(q,p)=q+ip,
\]

then \(J^2=-I\), \(EJ=iE\), and the rotations preserve \(\|q\|^2+\|p\|^2\). This rigorously yields \(\Omega\in\mathbb C^3\). It adds a quadrature per *real* channel, not the later \(\mathbb C^3\otimes\mathbb C^2\) doubling, which has twelve real dimensions.

One possible observable prescription, if two real scalar fields f,h are supplied, uses the orthonormal L2 face-indicator functions \(e_i=1_{P_i}/\sqrt{A_O}\):

\[
q_i=\langle e_i,f\rangle,\quad p_i=\langle e_i,h\rangle,\quad
\Omega_i=q_i+ip_i.
\]

The seams have surface measure zero, so this is an L2 coefficient map. Discontinuous face indicators are not thereby eigenfunctions, or even admissible H1 functions, of a welded-surface PDE. If instead the pair is displacement and velocity, a frequency/scale is needed to combine units: for \(\dot q=v,\ \dot v=-\nu^2q\), \(q+iv/\nu\) evolves as \(e^{-i\nu t}\). The oscillator equation and \(\nu\) are additional data.

**CANDIDATE_INTERPRETATION.** The most concrete positive candidate found here is the tangent-vector encoding of §3 because its two-plane geometry and complex structure are explicit. The simplest abstract alternative is paired field/oscillator quadratures. They are alternatives requiring different observables and symmetry actions; neither is adopted into the kernel.

## 7. Compatibility with the existing Paper-A map

**EXACT — coupling.** The coupling-only step acts by

\[
I+gL_3=P_{\rm bal}+(1-3g)P_\perp.
\]

It leaves the balanced component unchanged and multiplies both real and imaginary transverse components by the same real scalar. In particular all complex pairwise differences are multiplied by \(1-3g\). It is not a skew circulation generator. For real g, strict transverse norm contraction of this isolated linear step occurs exactly for \(0<g<2/3\); this is not a stability statement about the full nonlinear map. Individual polar phase differences and amplitude differences are nonlinear functions of the summed balanced/transverse components and are not independently multiplied by that scalar.

**EXACT — increment type.** In real coordinates \(\Omega_i=q_i+ip_i\), the pre-sync increment is the negative real gradient of

\[
V=\varepsilon\sum_i\left(\tfrac14|\Omega_i|^4-\tfrac12k_i|\Omega_i|^2\right)
 +\tfrac g2\sum_{i<j}|\Omega_i-\Omega_j|^2.
\]

This characterizes the increment; it does not assert monotonic decrease of V under the finite discrete step or of a physically identified energy. The synchronizer's phase increment is likewise \(\lambda\nabla_\phi W\), with

\[
W=\tfrac13\sum_{i<j}\cos 3(\phi_j-\phi_i).
\]

These formulae do not supply a nonzero constant skew phase generator. Nonlinear maps can have nontrivial temporal behavior without being an intrinsic reversible phase group.

**EXACT — harmonic three is not forced by face permutation.** A term \(\sum_{j\ne i}\sin(m(\phi_j-\phi_i))\) is equivariant under permuting the three labels for every positive integer m. C3 symmetry alone does not select m=3. Paper A already chooses that harmonic. Its term vanishes for in-phase states and for relative phases differing by multiples of \(2\pi/3\); the equal-amplitude 120° state lies in the transverse Fourier sector, not the balanced sector.

Changing to the R eigenbasis rewrites the nonlinear synchronizer but does not diagonalize it into independent character updates. For example the entrywise cubic amplitude operation N already fails to commute with the Fourier basis change F: \(N(Fe_0)=Fe_0/3\), whereas \(FN(e_0)=Fe_0\). Spectral decomposition of the linear coupling is not a derivation of the nonlinear phase rule.

**EXACT — parameter and zero conventions matter.** The whole map is C3-equivariant at fixed parameters when all \(k_i\) equal; otherwise parameter labels must be permuted with the state for that covariance. Its complex state need not be normalized. With nonzero pre-sync components it has common-phase equivariance. The specified \(\operatorname{Arg}_0(0)=0\) convention generally prevents this equivariance on the zero stratum for nonzero synchronization strength. The direct \(\lambda=0\) identity branch remains unchanged. A complex state space does not itself require every update to be a reversible phase symmetry.

**NUMERICALLY_VERIFIED.** Fixed-state checks against the current kernel confirm these scoped statements. For \(X=(0,1,e^{0.2i})\), \(\lambda=0.1\), and global phase shift 0.4, the maximum synchronizer equivariance discrepancy is 0.09317017645041971. A separate fixed unequal-k example gives a C3 discrepancy 0.05794410895157131. These are counterexamples to overly broad symmetry claims, not changes or defects relative to the frozen definition. All other tested identities use exact symbolic algebra or explicitly delimited floating-point comparisons.

## 8. Verification, preservation, and the stopping point

**NUMERICALLY_VERIFIED.** `verify_bridge_identities.py` completed with **51/51 predicates passing**: 40 symbolic/combinatorial predicates, 9 fixed numerical predicates (including 2 expected counterexamples), and 2 source-hash predicates. This is a new first-bridge execution count, unrelated to Paper C's earlier 51-predicate geometry audit. No historical geometry audit, existing 41-test suite, stability atlas, trajectory scan, or archive code was rerun.

Predicate coverage: 02–14 face channels/projectors/adjacency; 15–21 cyclic phase-plane limits; 22–27 tangent planes and mirror action; 28–34 circulation topology and welded harmonic constraints; 35–39 phase hypotheses and conditional complexification; 40–50 current-map compatibility; 01 and 51 preservation. The determinant obstruction, full strong-hypothesis argument, all-n seam result, and absence of continuous geometric isometries have analytic proofs above. Finite predicates support those arguments rather than replacing them.

Reproduce from PowerShell with the existing environment:

```powershell
& 'C:\Users\Notandi\miniconda3\envs\torment\python.exe' -I -S -B -X utf8 'C:\TORMENT\TRIOCTAGON_new\research\top_to_recursive_bridge\verify_bridge_identities.py'
```

Runtime: Python 3.11.15, SymPy 1.14.0, NumPy 2.4.4. Results are `bridge_symbolic_results.txt` and `.json` alongside the script. Bytecode writing is disabled. Ten previously recorded manuscript/kernel files matched their initial SHA-256 hashes before and after verification; the test script imports only the clean physics geometry/dynamics modules. The existing 41-test baseline is preserved, not newly claimed as executed.

**UNRESOLVED.** The smallest remaining scientific question is now precise: **what real face observable carries the two quadratures, and what independently justified local evolution or transformation rotates them?** In a tangent-vector proposal, an independent adversarial derivation should test the observable's meaning, the conjugate-linear mirror action, and whether any interface conditions constrain the six coefficients. In a circulating scalar proposal it must first address the explicit seam obstruction. This is the input needed before choosing a physical encoding or changing `kernel_physics`.

```ini
SCOPE = FIRST_GEOMETRY_TO_STATE_BRIDGE_ONLY
GEOMETRY_TO_REAL_THREE_CHANNELS = EXACT
C3_BALANCED_DECOMPOSITION = EXACT
L3_PROJECTOR_IDENTITY = EXACT
C3_PHASE_REPRESENTATION = ONE_TRANSVERSE_REAL_PHASE_PLANE
THREE_ORIENTED_TANGENT_PLANES = EXACT
TANGENT_SPACE_COMPLEX_STRUCTURE = EXACT_GIVEN_ORIENTATION
GEOMETRY_TO_C3 = CONDITIONAL_KINEMATIC_CONSTRUCTION
THREE_COMPLEX_DYNAMICAL_AMPLITUDES_DERIVED = NO
INDEPENDENT_SCALAR_PERIMETER_FIRST_HARMONICS_SURVIVE_WELDING = NO
CONSERVATIVE_PHASE_GENERATOR = NOT_DERIVED_AS_DYNAMICS
C3_TO_C3xC2_LIFT = DEFERRED
CHIRAL_EXTERIOR_GEOMETRY = DEFERRED
TOP_TO_RECURSION_HANDOFF_OBJECT = DEFERRED
DMQPF_ROLE = DEFERRED
MOVING_PROJECTOR_ALREADY_PRESENT = NOT_ASSESSED
MINIMAL_RECURSIVE_EXTENSION = DEFERRED
BRIDGE_READY_FOR_PHYSICS_KERNEL = PARTIAL
PHYSICAL_ENCODING_READY_FOR_IMPLEMENTATION = NO
VERIFICATION_PREDICATES_PASSED = 51
VERIFICATION_PREDICATES_FAILED = 0
FROZEN_PAPERS_MODIFIED = NO
KERNEL_PHYSICS_MODIFIED = NO
KERNEL_TO_TOUCHED = NO
KERNEL_NEW_TOUCHED = NO
PRODUCTION_TORMENT_TOUCHED = NO
```
