# GPT review — NATIVE_PROJECTION_CAPACITY_01

**Date:** 4 November 2026  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Disposition:** **Accepted. Established, with the proposed formulas and hypotheses unchanged.**  
**Corrections required:** None. No corrective Codex round is needed.

This review accepts the submitted bounded mathematical investigation. It covers the projection invariant, exact native debit identity, joint all-time ceiling, full-level feasibility and algebraic minimum, zero-ceiling/zero-drive equivalence, strict active coherent-launch witness and finite-time nonattainment example. It does not turn the algebraic minimum into a trajectory saturation theorem.

The submitted [proof](https://chatgpt.com/library?file_id=libfile_016f7967897c81918706d8d9f64a5e08&account_id=personal) and [review package](https://chatgpt.com/library?file_id=libfile_8e848df94e048191878d476a3e95fdd1&account_id=personal) remain unchanged. Their historical “GPT review pending” statements are resolved by this separate acceptance record.

## 1. Accepted result and its scope

Retain the published fixed real rank-two registration K, positive storage scales and couplings, finite carrier geometry and profiles, and the existing global solution class. Let e be either real unit vector spanning ker K. For the published yaw convention,

\[
e=(\cos\delta_g,-\sin\delta_g,0),\qquad
w=K^Ty,\qquad e\cdot w=0.
\]

Put \(I=|\Omega|^2\), \(h_e=|e\cdot\Omega|^2\). The new conserved quantity and exact account are

\[
\boxed{\mathcal J_K=I-2h_e,\qquad \dot{\mathcal J}_K=0,}
\]
\[
\boxed{H_N(0)-H_N(t)=\alpha_N[h_e(0)-h_e(t)].}
\]

Combining this invariant with the published \(Z_2=\Omega^T\Omega\), and writing \(Z_0=Z_2(\Omega_0)\), \(j_0=\mathcal J_K(\Omega_0)\), gives

\[
\boxed{
I(t)\ge\max(|Z_0|,j_0),\qquad
C_{\rm joint}
=\frac{\alpha_N}{2}[I_0-\max(|Z_0|,j_0)]
=\min\left\{C_Z,\alpha_N|e\cdot\Omega_0|^2\right\},
}
\]
\[
C_Z=\frac{\alpha_N}{2}(I_0-|Z_0|),\qquad
H_N(0)-H_N(t)\le C_{\rm joint}.
\]

For an initially empty carrier and receiver, the precise external-stock conclusion is

\[
\boxed{0\le H_C(t)+H_R(t)=H_N(0)-H_N(t)\le C_{\rm joint}
\quad(t\ge0).}
\]

For a preloaded external state, the same upper ceiling applies to signed net native debit, equivalently the increase in external stock over its initial value. It does not bound the entire pre-existing external stock. These distinctions are explicit in PC10–PC12.

The result applies at every fixed finite positive receiver coupling. AT01's large-coupling certificate is unnecessary for this structural theorem. All statements concern the unchanged exchange equations with fixed registration and coefficients.

## 2. Mathematical review findings

### 2.1 Registration, signs and inherited regularity

PC03 correctly expands the published matrix:

\[
K=\frac{G}{\sqrt7}
\begin{pmatrix}
2\sin\delta_g&2\cos\delta_g&\sqrt3\\
2\sin\delta_g&2\cos\delta_g&-\sqrt3
\end{pmatrix}.
\]

Its Gram determinant is \(48G^4/49>0\); the minus-yaw kernel convention is correct. No contact-tangent signs have been inserted into the raw registered drive.

The submitted right-handed-coordinate calculation correctly obtains

\[
\dot I=-4\mu\,w\cdot(a\times b),\qquad
\dot h_e=-2\mu\,w\cdot(a\times b),
\qquad \mu=\frac{\eta_N}{2\alpha_N}.
\]

Consequently the exact debit coefficient is \(\alpha_N\). The separate check \(\alpha_N\dot h_e=-P_{NC}\) agrees with the published signed power account. The scalar is indefinite and is not introduced as an additional positive physical store. These deductions use the exact [published native equation and balance](https://github.com/pzychozen/trioctagon-physics/blob/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/power.tex).

The regularity justification is sufficient. The [published global theorem](https://github.com/pzychozen/trioctagon-physics/blob/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/wellposed.tex) supplies C1 native coordinates and continuous L2 carrier coordinates. Bounded port averaging makes w continuous. The new proof differentiates only finite-dimensional native quantities; it does not differentiate an arbitrary L2 carrier preparation. No extra H1 hypothesis is required.

### 2.2 Joint floor and exact algebraic minimum

The combination with the [published Z2 invariant and ceiling](https://github.com/pzychozen/trioctagon-physics/blob/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/capacity.tex) is correct. Both terms in the minimum defining C_joint are nonnegative, including at native zero.

There is no missing absolute value on j in the stated floor. The proof establishes that every feasible invariant pair satisfies \(j\ge-|Z|\). Therefore \(\max(|Z|,|j|)=\max(|Z|,j)\) on all actual levels.

For \(\Omega=he+v_\perp\), the proof distinguishes the Hermitian norm from the complex bilinear square:

\[
Z=h^2+v_\perp^Tv_\perp,\qquad
j=\|v_\perp\|^2-|h|^2.
\]

The reverse triangle inequality and \(|v_\perp^Tv_\perp|\le\|v_\perp\|^2\) give \(|Z|\ge-j\), proving necessity of feasibility. The two explicit constructions in PC15–PC16 establish sufficiency and attain the lower bound. Hence

\[
\{\Omega\in\mathbb C^3:Z_2=Z,\ \mathcal J_K=j\}\ne\varnothing
\iff j\ge-|Z|,
\]
\[
\min_{\{Z_2=Z,\ \mathcal J_K=j\}}|\Omega|^2=\max(|Z|,j)
\quad\text{for feasible pairs}.
\]

The construction covers feasible negative j, both branch boundaries, Z=0, j=0 and native zero. Its phase selection divides by \(|Z|\) only in the expressly nonzero branch. No minimum is asserted on an empty constraint set. No compactness argument for an unbounded level set is presumed.

This is exact sharpness over the full common native invariant level in C3. The proof correctly avoids restricting the minimization to the coherent launch family or claiming that the coupled trajectory reaches an equality state.

### 2.3 Zero ceiling, zero drive and initial supply

PC18 proves

\[
C_{\rm joint}(\Omega_0)=0\iff f(x_0)=0
\]

in both directions. If the old ceiling vanishes, chirality vanishes; if the projection term vanishes, both real components lie in \(e^\perp\), and their cross product lies in ker K. Conversely, zero drive forces the cross product into the one-dimensional kernel. The proof correctly separates its zero and nonzero cases before using perpendicularity.

The real rank-two hypothesis is used essentially. Native zero is included without normalization or division by chirality.

With empty external preparation, zero drive gives a constant full solution, and uniqueness proves stationarity. Nonzero drive invokes the existing launch theorem:

\[
H_N(0)-H_N(t)
=\frac{\eta_N^2m}{2}|f_0|^2t^2+o(t^2)>0
\]

for all sufficiently small positive times. Thus positive joint capacity is accompanied by actual initial supply in this preparation class. The application is supported by [P1's general empty-launch proposition](https://github.com/pzychozen/trioctagon-physics/blob/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/manuscript/activity.tex). It does not establish saturation and does not make a nonzero preloaded dark core stationary.

### 2.4 Strict improvement for an active coherent launch

PC20–PC21 correctly evaluate the existing family \(\Omega_0=(1,e^{i\phi},1)\), \(0<\phi<\pi/12\). At fixed yaw \(\delta_g=\pi/4\),

\[
j_0=1+2\cos\phi,\qquad
|Z_0|=\sqrt{9-8\sin^2\phi},
\]
\[
j_0^2-|Z_0|^2=4\cos\phi(1-\cos\phi)>0.
\]

Both compared quantities are positive, so the squared comparison proves \(j_0>|Z_0|\). Therefore

\[
\boxed{0<C_{\rm joint}=\alpha_N(1-\cos\phi)<C_Z.}
\]

The same launch remains active:

\[
|f_0|^2=\frac{10G^2\sin^2\phi}{7}>0.
\]

This agrees with the exact [published coherent-launch drive](https://github.com/pzychozen/trioctagon-physics/blob/28e8a85c8fe1e6321328d4d7285b2560d1f98aa9/papers/SAME_TRAJECTORY_NATIVE_CREDIT/publication/v0.1/manuscript/problem.tex). The fixed positive gap \(C_Z-C_{\rm joint}\) excludes the old ceiling at every exchange time for this launch. The proof does not claim that every yaw improves the ceiling or that the new ceiling is dynamically attained.

### 2.5 Finite-time nonattainment is proved correctly

For real unit \(u\perp e\), the submitted example \(\Omega_0=u+ie\) has

\[
I_0=2,\qquad Z_0=j_0=0,\qquad f_0\ne0.
\]

Its common algebraic level includes native zero, the unique minimizer of intensity on that level. Nevertheless the nonzero native state cannot reach native zero at finite exchange time.

The full-state uniqueness argument retains the actual external coordinates at a hypothetical hitting time. The invariant native-zero subspace supplies an evolution through that same full state, and P1's forward/backward uniqueness forces its native coordinate to have been zero initially. It does not set the external state to zero.

The alternative argument is independently sufficient: along the actual solution, the continuous coefficient w(t) is fixed, and the native equation is a homogeneous linear ODE. A solution zero at any finite time is identically zero on the finite interval by uniqueness. Treating the actual coefficient in this way does not make it a free control.

The example is outside the restricted coherent launch family but within the general published preparation class. The proof makes no conclusion about infinite-time approach. Its finite-time conclusion and its stated limitation are both accepted.

## 3. Independent verification

The review combined source reading and written mathematical analysis with one replay of the submitted symbolic checker and an independent artifact audit. Three parallel analytical reviews covered the invariant/minimum, the launch/dynamical boundary, and the ledger/scope. All recommended acceptance unchanged. Their dispositions are recorded in INDEPENDENT_REVIEW_DISPOSITIONS.json.

| Review component | Result |
| --- | --- |
| Submitted archive SHA-256 | Matches the user-supplied digest and sidecar |
| Archive membership and manifest | 43 unique safe members; 42 hashed payloads; exhaustive manifest; all CRCs, sizes and hashes pass |
| Separate uploaded proof | Byte-identical to the archived proof |
| Issued packet continuity | All 23 issued members preserved exactly, including the three declared metadata relocations |
| Defining published sources | All seven retain their exact source identities |
| Prior accepted/context identities | All eight original registry entries agree; AT01 proof and ledger match its accepted ZIP |
| Protected-input evidence | All 37 baseline/final records reconcile and match retained reference bytes |
| Claim/source checks | PC01–PC22 covered; 33 recorded source-label references resolve; proof/ledger links resolve |
| Symbolic replay | 12 grouped checks executed, 12 passed, zero failed; every per-check record matches Codex's result |
| Scientific disposition | No correction to formulas, signs, factors, hypotheses, feasibility cases or interpretation |

The independent artifact audit contains 25 grouped integrity checks. These are separate from the 12 symbolic groups and do not increase the scientific check count.

The checker was inspected before execution and replayed unchanged using Python 3.12.14 and the already available reviewer SymPy 1.14.0. Codex's original execution used Python 3.11.15 and SymPy 1.14.0. No package was installed, no original evidence was modified, and no historical scientific suite was replayed. The equality of the per-check outputs excludes runtime/timestamp metadata from that comparison.

The symbolic groups support the algebraic identities and constructions. The written arguments establish the inequalities, both directions of feasibility, exact minimum, zero-drive equivalence and uniqueness-based nonattainment. Acceptance does not rest on the check count alone.

**Preservation boundary:** this review reconciles Codex's Windows baseline/final records and validates every recorded identity against retained exact input bytes. GPT did not access or audit the current live Windows filesystem.

Reviewed artifact identities:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Submitted review ZIP | 267075 | 11a55105e6803d595f93bd1211f9d5f6832a070b0af9b12bb257b5636234413e |
| Submitted proof | 20417 | b5b461e3127f762d5f48ebacc0d687d6c80d7fa31d9d1a767ea2d0ec32e6299c |
| Issued Codex packet | 219451 | 72733488122126b36b8c0b06b13179da02db84c809965f5d99c142a4da71ec0c |

## 4. Meaning, limits and research continuity

The new scalar can be read as the difference between the squared native amplitude perpendicular to the kernel direction and the squared amplitude along it. Its conservation gives a geometric restriction inside the existing registration. It adds a precise constraint to the published exchange account.

The accepted AT01 result remains unchanged. Its high receiver-share and recovery fractions concern the actual intermediate transferred stock. Its first-window transferred amount has a positive inverse-square leading scale and tends to zero as coupling increases. At the present fixed witness launch, C_joint is positive and independent of that coupling. The two results are therefore consistent and complementary.

The new ceiling is a necessary all-time bound on net extraction. Actual maximum extraction, dynamical attainment of the new ceiling, infinite-time behavior and useful finite transferred amounts beyond the accepted first-window regime remain open. Gross repeated positive work is not bounded by an upper limit on net storage debit.

The theorem assumes fixed exchange registration and coefficients. It does not supply an invariant across native F jumps or a lifetime hybrid capacity. The mathematical kernel axis has not been assigned to a physical support, opening, field axis or receiver location.

The central starting/meeting region, opposed cones, outward spreading and curved around–inward return, stationary supports and possible transfer elsewhere remain the intended programme. The carrier circle and intended tight toroid remain distinct, as do the original close enclosing sphere and the extended-line sphere. The tentative 15–20%, possibly more, remains the author's geometric intuition.

The agenda retains useful accessible capacity, native stepping/cadence, route correspondence, six-opening transport, linked gravity–magnetism, later outer geometry and justified SRG integration. No new geometric decision from the author was needed for this proof.

The accepted quantitative-transfer result and this accepted structural-capacity result now form a coherent basis for a follow-on manuscript. Preparing that manuscript before opening another capacity investigation is the recommended next editorial step. This review performs no manuscript, Git, publication or successor-investigation action.

**Final disposition:** NATIVE_PROJECTION_CAPACITY_01 is accepted unchanged. No unresolved review issue remains within its assigned mathematical scope.
