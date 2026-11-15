# Established results and their limits

GRAVITY_NATIVE_RECOVERY_01 · GPT · 22 October 2026

The native chain is already substantial: **potential → pre-state increment → matched face representation → background-dependent response → finite-sector spectral structure**. It supplies precise mathematical connections without treating the shell as a physical container. The complete map's energy control and the information needed to close a reduced description remain the useful next questions.

Equation IDs refer to [the equation map](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NATIVE_EQUATION_MAP.md). Proof and evidence locations are in [the source map](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_IMPLEMENTATION_SOURCE_MAP.md). “Established” below means a stated written proof or retained numerical result, not a new run in this recovery.

## Proof-level results

| Ownership | Established result | Essential restriction / implication |
|---|---|---|
| Papers B/C; GR0; SA0 | Panel metric I₂; D/E isometry on tangent fibres; \(T_{ij}T_{jk}=T_{ik}\); tangent holonomy identity (E02–E04). | Fixed geometry and flat matched connection. Ambient loop is a projector. No evolving curvature follows. |
| Papers D/E; GR0 | Correctly normalized quartic/graph potential has negative gradient b; exact intensity budget includes \(\|b\|^2\); transported graph quadratic equals complex graph quadratic (E05). | A variational increment and exact representation of graph energy. No full-map descent/conservation theorem. |
| GR0, extending prior Paper F triad result | Complete equal-background amplitude/phase Fourier multipliers, finite-N normal contraction and local attraction to the fixed circle (E07). | Strict inequalities, fixed finite N; common phase neutral. Marginal cases and nonlinear global behavior remain separate. |
| GR0 | Controlled fixed-mode diffusive scaling and quartic leading decrement when g+ℓ=0 (E07). | Linearization, fixed finitely many modes; no uniform nonlinear continuum limit. |
| GR1 | Unique local positive unequal branch; screened first response to coefficient heterogeneity (E08). | Continuation from a strictly stable equal point. No global branch theorem or mass-source identification. |
| GR1 | Pre-phase response P is self-adjoint under R²; conductances \(g r_ir_j\) for g>0 (E09). | Native phase-chart/state response geometry. For g<0 balance still holds but the Dirichlet form changes sign. |
| GR1 | Complete phase response is SP, generically not diagonally balanced (E10). | Triad cycle iff test uses positive off-diagonals near the stable equal point. General full-ring theorem has different hypotheses. |
| GR2 | Arbitrary SPD self-adjointness iff real semisimple spectrum; local positive triad has such a generally dense, nonunique metric despite failed diagonal balance. | Transverse quotient is not assumed to be the Euclidean sum-zero invariant plane. Full common-phase resonance can cause defects outside the stable neighborhood. |
| GR2 | For N≥9, three distinct repeated radii and \(g\ell[\ell(1+3g)-g]\ne0\) force non-real Bloch modes. | No SPD symmetrizer then exists. Complex stable modes are possible; they are not automatically physical waves. |
| CM0 | Complete D₃h degree≤2 ambient census; polar dimensions 2 linear/5 quadratic, axial 2/3; distinct chiral projections W and Γ. | Kinematic covariance, with coefficients carried under permutations. Symmetry does not select one physical position or motion law. |
| SA0 | D gives exact full face-state conjugacy; finite-carrier assignments have multiple independent choices; preparation reaches Ω before face decoding. | No spatial field extension, seam flux, rim state, deformation or boundary feedback is thereby defined. |
| SA0 | General fibre criterion for autonomous observation; full complex coherence and real Gram close on the regular pre-state domain (E11). | Intensity/chirality generally fail closure; zero convention blocks a global nonzero-λ quotient. |

### Exact exceptional six-ring result

GR2 proves more than a generic non-real-spectrum statement. For

\[
r=(1-\tau,1,1+\tau),\quad g=(1-\tau^2)/4,\quad
\ell=1,\quad\epsilon=1/20,\quad
k_i=r_i^2-\frac g\epsilon\frac{(\Delta_3r)_i}{r_i},
\]

the antiperiodic block is

\[
J(-1)=\frac{\tau^2}{4}
\begin{pmatrix}1\\-1\\1\end{pmatrix}
\begin{pmatrix}1+\tau&2&1-\tau\end{pmatrix}.
\]

For sufficiently small nonzero τ this is a native positive fixed background with a rank-one, square-zero block: Jordan sizes 2+1 at zero. Holding r,g,k,ε fixed and varying only the existing \(\ell=1+\delta\), its cubic discriminant is

\[
\mathfrak D_\pi=(27/2)\tau^{12}\delta^3+O(\delta^4).
\]

For fixed small nonzero τ, sufficiently small δ<0 gives a complex pair; δ>0 gives three distinct real roots; δ=0 is defective. Normal stability can persist through all three. Generic weak six-ring reality therefore cannot be promoted to a theorem covering exceptional baselines. Source: NRG spectral.tex, eq:fixture–eq:unfoldcoeff; GR2 §6.

### Exact closure counterexamples

SA0 uses ε=1/20,g=1/5,k=(1,1,1). States (1,1,1) and (1,−1,1) share every initial intensity but give next intensities (1,1,1) and (9/25,1/25,9/25), independently of λ. Intensities alone therefore fail general closure. At g=0 there is the explicit exception \(s_i^+=s_i[1+\epsilon(k_i-s_i)]^2\).

At ε=g=0, λ=1/10, states \(z=(1,-1,0)\) and \(e^{i\pi/6}z\) have identical complex/real Grams. Their next complex (1,2) entries are −1 and \(-e^{-i/5}\); real entries are −1 and \(-\cos(1/5)\). This proves the zero-stratum obstruction. At λ=0 the Gram congruence updates are global.

Complete face state retains Ω and closes globally. Raw chirality C, W and Γ, including their joint chiral representation, generally discard information needed for their next values. These are failures of general closure, not exclusions of special invariant subsets.

## Numerical findings already retained

The source scripts/results contain **45 GR0 + 38 GR1 + 42 GR2 + 78 CM0 + 226 SA0 = 429 heterogeneous exact/source predicates**. They are not 429 theorems. The manuscript's **61 paper-local checks** are a separate count. No count below represents work newly executed here.

| Evidence | Fixture and retained measurement | What it supports |
|---|---|---|
| GR0 native finite differences | ε=1/20,g=1/5,λ=1/1000; C3 k=1, phase 0; C12 k=4, phase π/7. Best full-Jacobian errors \(1.338\times10^{-11}\), \(2.871\times10^{-11}\). | Implementation-to-derivative consistency at two witnesses. |
| GR0 independent 100-digit transcription | Difference steps \(10^{-10},10^{-20}\): errors \(5.0\times10^{-22},5.0\times10^{-42}\). | Transcription check, not high-precision execution of complex128 kernel. |
| GR1 branch | k=1, κ=(−1,0,1), same ε,g,λ; η=.01,.005,.0025. Fixed-equation residual ≤\(1.009\times10^{-99}\). | Local weak-branch calculation; first-order remainder scales as η². |
| GR1 cycle | \(\mathcal C/\eta^3\) approaches \(-6.95491311953\times10^{-8}\); at η=.01, \(\mathcal C\approx-6.95490385\times10^{-14}\). | Cubic obstruction agrees with exact factorization; no parameter survey. |
| GR2 Bloch roots | Same family; max imaginary part at z=i: \(4.21737\times10^{-13},5.27172\times10^{-14},6.58966\times10^{-15}\). | Cubic scaling, backed by exact non-real coefficient proof. |
| GR2 dense triad metric | η=.01: smallest G eigenvalue ≈.9988412910; balance residual ≈\(1.6073\times10^{-101}\), simultaneously nonzero diagonal-cycle obstruction. | Diagonal and arbitrary-SPD balance differ at the same fixture. |
| GR1/GR2 native phase differences | Errors ≲\(1.63\times10^{-14}\) on the checked N=3,6,12 cases. | Response formula check; does not resolve all the smaller imaginary eigenvalue parts. |
| CM0 | Twelve observable derivatives: maxima \(3.0680\times10^{-11}\) equal, \(1.12197\times10^{-11}\) weak unequal at step \(10^{-5}\). | Observable chain-rule response; no trajectory experiment. |
| SA0 | Ten quotient/zero-witness/FaceState/preparation comparisons; largest equality residual \(1.67250\times10^{-16}\). | Bounded numerical support for exact closure identities and pipeline typing. |

Full unrounded evidence: [retained_evidence.json](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/verification/retained_evidence.json). Human-readable method-separated tables: [NUMERICAL_EVIDENCE.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/verification/NUMERICAL_EVIDENCE.md).

## Later result that prevents an obsolete conclusion

The accepted DRIFT source proves the chiral relative equilibria in E15, including a nonzero cubic generator rate. This updates the earlier gravity inventory's trajectory context. It does not alter GR0–GR2's in-phase response theorems: it concerns a different background.

At a relative equilibrium the full state advances by common phase while coherence and the existing common-phase-invariant potential are unchanged. A single invariant-potential pure-gradient generator in a positive metric cannot describe that nonzero-rate orbit. The accepted argument is conditional and does not classify every variational or non-gradient description. The chiral reference is a saddle, so this is not evidence of an attracting spatial orbit.

The earlier blanket “nothing propagates” and dimensional gravity exclusions were explicitly narrowed/withdrawn in the [fresh-eyes reconciliation](C:/TORMENT/TRIOCTAGON_new/research/FRESH_EYES_SCIENTIFIC_REVIEW_20261006/FRESH_EYES_RECONCILIATION_NOTE_v0.1.md). They should not be inherited as no-go theorems. Equally, damped response modes and common-phase drift do not by themselves establish gravity.
