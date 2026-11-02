# Minimum closed native information: independent proof review

**Task:** NATIVE_CLOSED_INFORMATION_01  
**Date:** 2 November 2026 (Atlantic/Reykjavik)  
**Disposition:** Candidate verified; minimum additional raw-entry count is **two** in the full dictionary and **three** in the real-only dictionary.  
**Prepared by:** Codex for GPT and Hilmir Frímann Halldórsson / pzychozen. This is a bounded mathematical review, not a runtime implementation or publication decision.

## 1. Verdict and the exact minimum statement

The three intensities together with the two signed areas \(A_{12},A_{13}\) determine the entire complex coherence throughout the specified coherent domain. The narrow ordinary phase interval makes each relative sine invertible and fixes the positive square-root branches. Reconstruction remains valid at alignment, zero areas, equal amplitudes, coincident phases, and the closed amplitude and phase boundaries.

This five-real-entry tuple has an autonomous update on its actual image of the domain. It retains every individual matched edge energy, the existing native potential, and the squared prestage increment in the accepted descent theorem. The fixed common-phase circle becomes one retained state, and the retained potential strictly decreases at every other retained state.

**Two additional dictionary entries are necessary and sufficient for this joint objective.** Every choice of zero or one additional entry fails to determine even the current potential on the stated domain. If only real coherences \(S_{ij}\) may be selected, every choice of two fails to determine the omitted edge energy and current potential, while all three suffice by inherited real-Gram closure. These lower bounds are static energy-retention obstructions; they are not assertions that the next retained values differ.

The minimum is taken only over subsets of

\[
\mathscr E=\{S_{12},S_{13},S_{23},A_{12},A_{13},A_{23}\},
\]

always retaining all three intensities. A complex pair entry costs two real entries. This is a statement on the entire domain, not on each special stratum separately, and not a minimum over arbitrary encodings or the coarsest possible energy quotient. The signed candidate retains more orientation information than the full real Gram even though it uses fewer raw pair entries. No classification of all mixed two-entry subsets is claimed.

For a subdictionary \(\mathscr A\), write \(m(\mathscr A)\) for the smallest cardinality of a subset whose retained tuple satisfies all three requirements on \(\mathcal D\): autonomous update on its actual image; retention of the potential and each edge energy; and retention of the squared prestage increment needed for the accepted inequality and equality case.

No correction to the candidate formulas was required.

## 2. Fixed setting and accepted dependencies

Throughout, use exactly

\[
\epsilon=\frac1{10},\qquad g=\frac1{60},\qquad
\lambda=\frac1{300},\qquad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),
\qquad L=\mathbf1\mathbf1^T-3I,
\tag{1}
\]

and put \(D_0=\pi/12\). The native domain is

\[
\mathcal D=\left\{\Omega\in\mathbb C^3:
\frac9{10}\le|\Omega_i|\le\frac{11}{10},\quad
\text{ordinary phase width}\le D_0\right\}.
\tag{2}
\]

An ordinary phase interval uses a full turn; phases differing by \(2\pi/3\) are not identified. Each state in (2) has consistent real phase lifts \(\theta_i\) whose maximum minus minimum is at most \(D_0\). Their common orientation is arbitrary.

The map and tested scalar are the unchanged native ones:

\[
v=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL\Omega,\qquad
\delta_i=\lambda\sum_{j\ne i}\sin3(\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i),
\qquad F_i(\Omega)=v_i e^{i\delta_i},
\tag{3}
\]
\[
\mathcal V(\Omega)=\epsilon\sum_i
\left(\frac{s_i^2}{4}-\frac{k_i s_i}{2}\right)
+\frac g2\sum_{i<j}|\Omega_i-\Omega_j|^2,
\qquad s_i=|\Omega_i|^2.
\tag{4}
\]

The following inputs are inherited, rather than re-proved or re-executed:

1. **Regular invariance:** \(F(\mathcal D)\subseteq\mathcal D\), and every prestage from \(\mathcal D\) satisfies
   \[
   \frac{88701}{100000}+\frac3{100}\cos D_0
   \le |v_i|\le\frac{107701}{100000},\qquad
   \frac9{10}<|v_i|<\frac{11}{10}.
   \tag{5}
   \]
   Positive input amplitudes alone would not establish this; these are the accepted prestage bounds from S2 below.
2. **Native descent and strictness:** S0 gives
   \[
   \mathcal V(F\Omega)-\mathcal V(\Omega)
   \le-\frac{16869}{20000}\|v-\Omega\|_2^2,
   \tag{6}
   \]
   with equality in monotonicity exactly on \(\{e^{i\theta}r_*\}\). Here \(r_*\) is the accepted unique aligned amplitude profile in \([9/10,11/10]^3\), supplied by S2. S0 also identifies \(v-\Omega=0\) with this circle within \(\mathcal D\).
3. **Closure and transport:** S1 supplies the regular complex-coherence and real-Gram closure theorems, the fibre criterion, and the adopted matched tangent transport/isometry.

### Source and dependency record

All paths below are actual local files read in place. The work order identifies accepted reading editions `82cab10cbe550f58c43163fb8b05fabdad1b05ae` for S1 and `7cc1fa03af589818bcdcfaaac51838cc36c84253` for S2. These are inherited edition references, not a claim about current checkout HEAD or a new byte-authentication audit. No Git operations were used.

| Source | Actual path and precise passage | Role |
|---|---|---|
| Work order | [NATIVE_CLOSED_INFORMATION_01_CODEX_WORK_ORDER.md](C:/Users/Notandi/Downloads/NATIVE_CLOSED_INFORMATION_01_CODEX_WORK_ORDER.md) | User-authorized scope; its candidate reconstruction and minimum are proof targets. |
| S0 | [NATIVE_ENERGY_RESPONSE_01_PROOF_REVIEW.md](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_ENERGY_RESPONSE_01/NATIVE_ENERGY_RESPONSE_01_PROOF_REVIEW.md), Section 5, equations (20)–(30); Section 7, equations (35)–(36) | Accepted on 1 November according to the present order. Finite-domain descent, equality, and pair-coherence signs. Its helper was not rerun and its proof was not reopened. |
| S1c | [observables_closure.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex), lines 78–102, `eq:decoder`, `eq:faceupdate`; lines 157–236, `thm:closure`, `eq:fibre`, `thm:Hclosure`, `eq:Hpre`, `eq:Hpost`, `thm:Sclosure`, `eq:zerocounter` | Accepted matched transport, fibre criterion, both regular closure results, matrix sign convention, and global zero-stratum limitation. |
| S1p | [response.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex), lines 29–39, `eq:potential` | Existing scalar and edge-once normalization. |
| S1l | [THEOREM_LEDGER.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/provenance/THEOREM_LEDGER.md), L34, L38, L40–L42 | Inherited theorem classifications and restrictions, including rank-deficient real-Gram factors and the need for persistent regularity. |
| S2 | [main.tex](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex), Section 6, lines 314–372, `lem:phase`, `eq:apos`, `eq:lower`, `eq:upper`; Section 7, lines 414–448, `thm:convergence`, `eq:amplitudemap`, `eq:beta`, `eq:fixed` | Accepted invariance, nonzero prestages, and unique aligned profile. No domain certificate or profile calculation was rerun. |
| S3q | [GRAVITY_NEXT_INVESTIGATION.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NEXT_INVESTIGATION.md), Question 2, lines 71–97 | Original minimum-information question. The present order fixes the dictionary, joint objective, and domain more narrowly. |
| S3e | [GRAVITY_NATIVE_EQUATION_MAP.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_NATIVE_EQUATION_MAP.md), E04–E05 and E11 | Matched edge quantities, scalar, \(S_G-iA_G\) convention, and the transposed coherence entry in the phase update. |
| S3m | [GRAVITY_IMPLEMENTATION_SOURCE_MAP.md](C:/TORMENT/TRIOCTAGON_new/research/GRAVITY_NATIVE_RECOVERY_01/GRAVITY_IMPLEMENTATION_SOURCE_MAP.md), K-DYN, K-FACE, K-DIAG, K-AX | Source/function ownership; quotient formulas are mathematical results, not an existing quotient runtime API. |
| S3d | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py), lines 57–104, `arg0`, `phase_sync`, `_advance`, `step3` | Text-only confirmation of zero convention, lambda-zero bypass, simultaneous kicks, and stage order. |
| S3v | [z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py), `potential`, lines 290–302 | Text-only confirmation of the potential normalization. |
| S3a | [axial_observables.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/axial_observables.py), `_sa`, lines 158–162 | Text-only confirmation of \(S_{ij}=q_iq_j+p_ip_j\) and \(A_{ij}=q_ip_j-p_iq_j\). |
| S3f | [face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py), `_decode`/`decode_to_faces`, lines 66–80; `transport`, lines 123–133; `state_area`, lines 141–154 | Text-only confirmation of the adopted decoder, source-to-destination transport, and area orientation. |

**Deductions established here:** the five-entry reconstruction and exact image characterization; its common-phase fibres and induced invariant update; exact retention and transfer of (6); the within-domain zero/one-entry lower bound; and the real-only two-entry obstruction and attained three-entry minimum. The old general intensity nonclosure witness is not used as a witness on (2).

## 3. Reconstruction throughout the closed domain

Retain

\[
y=\mathcal R(\Omega)=(s_1,s_2,s_3,x,y_a),\qquad
x=A_{12},\quad y_a=A_{13},
\tag{7}
\]

and define the pair convention

\[
C_{ij}=\overline{\Omega_i}\Omega_j=S_{ij}+iA_{ij}.
\tag{8}
\]

Channel 1 is a fixed algebraic anchor. Nothing about this choice asserts a physical attachment or permutation symmetry of the unequal-coefficient dynamics.

Let \(r_i=|\Omega_i|\). On (2), \(|\theta_j-\theta_i|\le D_0<\pi/2\), so

\[
S_{ij}=r_ir_j\cos(\theta_j-\theta_i)>0,
\qquad A_{ij}=r_ir_j\sin(\theta_j-\theta_i).
\]

Consequently, writing \(p=S_{12}\) and \(q=S_{13}\), the unique allowed roots are

\[
\boxed{p=+\sqrt{s_1s_2-x^2},\qquad
q=+\sqrt{s_1s_3-y_a^2}.}
\tag{9}
\]

Their radicands obey the uniform strict lower bounds

\[
s_1s_2-x^2\ge\left(\frac{81}{100}\right)^2\cos^2D_0>0,
\qquad
s_1s_3-y_a^2\ge\left(\frac{81}{100}\right)^2\cos^2D_0>0.
\tag{10}
\]

The relation between the remaining pair and the anchor pairs is

\[
\overline{C_{12}}C_{13}
=(\Omega_1\overline{\Omega_2})(\overline{\Omega_1}\Omega_3)
=s_1\overline{\Omega_2}\Omega_3=s_1C_{23}.
\]

Expanding \((p-ix)(q+iy_a)\) therefore gives exactly

\[
\boxed{S_{23}=\frac{pq+xy_a}{s_1},\qquad
A_{23}=\frac{py_a-xq}{s_1}.}
\tag{11}
\]

The only denominator in (11) is \(s_1\ge81/100\). These formulas do not divide by an area or by a phase difference.

### Matrix convention and fibres

The accepted matrix convention differs from (8):

\[
\mathcal H=\Omega\Omega^\dagger=S_G-iA_G,
\qquad \mathcal H_{ij}=\overline{C_{ij}},
\qquad A_{ij}=-\Im\mathcal H_{ij}.
\tag{12}
\]

Thus the reconstruction is

\[
\boxed{
\mathcal H(y)=
\begin{pmatrix}
s_1&p-ix&q-iy_a\\
p+ix&s_2&S_{23}-iA_{23}\\
q+iy_a&S_{23}+iA_{23}&s_3
\end{pmatrix}.}
\tag{13}
\]

A convenient representative, used only to prove this algebra, is

\[
z(y)=\left(\sqrt{s_1},\frac{p+ix}{\sqrt{s_1}},
\frac{q+iy_a}{\sqrt{s_1}}\right)^T.
\tag{14}
\]

Its squared moduli are \(s_1,s_2,s_3\), and (9)–(11) show
\(z(y)z(y)^\dagger=\mathcal H(y)\). Thus the reconstructed matrix is Hermitian positive semidefinite of rank exactly one on the retained image. For any original state,
\(z(\mathcal R(\Omega))=e^{-i\theta_1}\Omega\).

If two states of \(\mathcal D\) have the same retained tuple, (14) gives the same representative, so they differ by one common phase. Conversely, a common phase leaves every retained entry unchanged and preserves \(\mathcal D\). Therefore the fibres are **exactly the common-phase orbits in \(\mathcal D\)**. Formula (14) neither determines the original common phase nor reconstructs its accumulated native advance; that later question is not addressed here.

### Boundary and degenerate cases

The closed amplitude boundaries and phase-width boundary preserve (10) and the positive denominator, so no additional chart exclusion is needed. Equal amplitudes introduce no singularity. Coincident phases merely set the corresponding area to zero.

In particular, \(x=0\) forces \(\theta_2=\theta_1\) within this phase sector, and \(y_a=0\) forces \(\theta_3=\theta_1\). Either can vanish while the other is nonzero. If both vanish, all phases align, \(p=\sqrt{s_1s_2}\), \(q=\sqrt{s_1s_3}\), \(S_{23}=\sqrt{s_2s_3}\), and \(A_{23}=0\).

The real Gram \(S_G\) has rank one precisely when its nonzero planar row vectors are collinear. On this narrow ordinary sector they must then point along the same ray, so this is exactly the aligned case just covered. The complex coherence itself is rank one everywhere, including nonaligned states. Rank-one real-Gram states therefore cause no loss of validity, and no generic nonzero-area assumption has been made.

## 4. Exact retained domain

First define the domain intrinsically by

\[
\mathcal Y=\mathcal R(\mathcal D).
\tag{15}
\]

A complete readout-only characterization is the following. The coordinates are real, with

\[
\frac{81}{100}\le s_i\le\frac{121}{100},\qquad
|x|\le\sqrt{s_1s_2},\qquad |y_a|\le\sqrt{s_1s_3},
\tag{16}
\]

and the principal real arcsines

\[
\alpha_2=\arcsin\frac{x}{\sqrt{s_1s_2}},\qquad
\alpha_3=\arcsin\frac{y_a}{\sqrt{s_1s_3}}
\tag{17}
\]

satisfy

\[
\boxed{\max(0,\alpha_2,\alpha_3)
-\min(0,\alpha_2,\alpha_3)\le D_0.}
\tag{18}
\]

The explicit area bounds in (16) simply ensure that the arcsines are real; (18) implies the stronger bounds \(|x|\le\sqrt{s_1s_2}\sin D_0\) and \(|y_a|\le\sqrt{s_1s_3}\sin D_0\).

**Necessity.** For \(\Omega\in\mathcal D\), subtract \(\theta_1\) from the consistent lifts. Both relative phases lie in \([-D_0,D_0]\), where principal arcsine inverts sine. Thus \(\alpha_2=\theta_2-\theta_1\) and \(\alpha_3=\theta_3-\theta_1\), and their span together with zero is the same as the original phase span. Equations (16)–(18) follow.

**Sufficiency.** Given (16)–(18), take

\[
z=(\sqrt{s_1},\sqrt{s_2}e^{i\alpha_2},\sqrt{s_3}e^{i\alpha_3}).
\]

It belongs to \(\mathcal D\) by the amplitude bounds and (18), and its retained areas are exactly \(x,y_a\). Its positive cosines make it the representative (14). Hence the tuple belongs to \(\mathcal Y\), proving equality with (15). This also proves that (13) is a valid rank-one coherence for every tuple in the characterized domain, not merely for tuples assumed to have come from a state.

Separate area bounds alone are insufficient. For example, normalized areas \(\sin D_0\) and \(-\sin D_0\) separately meet the natural anchor bounds, but their recovered phases \(D_0,-D_0\) span \(2D_0\) and fail (18). The joint span condition prevents this unintended domain enlargement.

## 5. Autonomous update and all mathematical iterates

For \(y\in\mathcal Y\), reconstruct (13) and define

\[
M(y)=I+\epsilon\operatorname{diag}(k-s)+gL,
\qquad \widetilde{\mathcal H}=M\mathcal H M^T,
\qquad \rho_i=\sqrt{\widetilde{\mathcal H}_{ii}}.
\tag{19}
\]

The matrix \(M\) is real, and for any representative \(\Omega\) of \(y\),
\(M\Omega=v(\Omega)\). Consequently
\(\widetilde{\mathcal H}=vv^\dagger\) and \(\rho_i=|v_i|\). Since a representative lies in \(\mathcal D\), the inherited bounds (5) prove \(\rho_i>0\) for every \(y\in\mathcal Y\).

Use exactly the accepted coherence update:

\[
\delta_i=\lambda\sum_{j\ne i}\Im\left[
\left(\frac{\widetilde{\mathcal H}_{ji}}{\rho_j\rho_i}\right)^3\right],
\qquad U_\delta=\operatorname{diag}(e^{i\delta_i}),
\qquad \mathcal H^+=U_\delta\widetilde{\mathcal H}U_\delta^\dagger.
\tag{20}
\]

The **\(ji\) entry** is essential:

\[
\frac{\widetilde{\mathcal H}_{ji}}{\rho_j\rho_i}
=\frac{v_j\overline v_i}{|v_j||v_i|}
=e^{i(\psi_j-\psi_i)}.
\]

Its cubed imaginary part is \(\sin3(\psi_j-\psi_i)\), with the same sign as (3). Substituting \(C_{ij}\) for \(\mathcal H_{ij}\), or using the untransposed entry in this formula, would reverse that sign. No such substitution is made.

Extract

\[
\boxed{F_{\mathcal R}(y)=
(\mathcal H^+_{11},\mathcal H^+_{22},\mathcal H^+_{33},
-\Im\mathcal H^+_{12},-\Im\mathcal H^+_{13}).}
\tag{21}
\]

The diagonal entries are real positive intensities. The regular coherence-closure theorem gives

\[
\mathcal R(F\Omega)=F_{\mathcal R}(\mathcal R(\Omega))
\qquad(\Omega\in\mathcal D).
\tag{22}
\]

Equivalently, the fibre criterion applies because equal retained tuples are common-phase orbits, and the native map is common-phase equivariant on this nonzero-prestage domain. This supplies an independent well-definedness explanation: the output is independent of the representative.

For each \(y\in\mathcal Y\), choose \(\Omega\in\mathcal D\) with \(\mathcal R(\Omega)=y\). Inherited invariance yields \(F\Omega\in\mathcal D\), and (22) then gives

\[
F_{\mathcal R}(\mathcal Y)\subseteq\mathcal Y.
\tag{23}
\]

Induction justifies every subsequent mathematical iterate:

\[
F_{\mathcal R}^{n}(\mathcal R(\Omega))
=\mathcal R(F^n\Omega),\qquad n\ge0,
\tag{24}
\]

with nonzero prestages at each step by (5). No trajectories were run to establish (24).

The native \(\operatorname{Arg}_0(0)=0\) convention is retained. It is not encountered here because of the accepted bounds, not because it has been repaired. The implementation's \(\lambda=0\) bypass remains part of the native definition; the fixed tuple (1) uses nonzero \(\lambda\). The coherence formula reduces to the identity phase stage when \(\lambda=0\), but no alternative parameter task or global zero-stratum extension is undertaken. S1c's `eq:zerocounter` remains a limitation on unrestricted quotient claims.

## 6. Edge energies, potential, increment norm, and descent

### Individual matched edge energies

For each unordered pair reconstruct

\[
\boxed{E_{ij}(y)=s_i+s_j-2S_{ij}(y)
=|\Omega_i-\Omega_j|^2.}
\tag{25}
\]

Let \(D_i\) be the accepted real-linear isometry into the labelled tangent plane and \(T_{ij}\) the accepted transport from channel \(j\)'s plane to channel \(i\)'s plane. The matched-frame identity is \(T_{ij}D_j=D_i\). Therefore

\[
D_i\Omega_i-T_{ij}D_j\Omega_j=D_i(\Omega_i-\Omega_j),
\qquad
E_{ij}(y)=\|D_i\Omega_i-T_{ij}D_j\Omega_j\|^2.
\tag{26}
\]

Thus all three individual transported squared differences are retained. The absolute common-phase-dependent face vectors themselves are not reconstructed, and no physical flux is inferred.

### The same native scalar

Define, with each edge counted once,

\[
\boxed{\widehat{\mathcal V}(y)=
\epsilon\sum_i\left(\frac{s_i^2}{4}-\frac{k_i s_i}{2}\right)
+\frac g2\sum_{i<j}E_{ij}(y).}
\tag{27}
\]

Equations (4) and (25) give exactly
\(\widehat{\mathcal V}(\mathcal R(\Omega))=\mathcal V(\Omega)\).
There is no new potential or change of normalization.

### Squared prestage increment

Set \(N(y)=M(y)-I\). Then \(v-\Omega=N\Omega\), so

\[
\boxed{\widehat{\mathcal B}(y)=
\operatorname{tr}(N\mathcal H N^T)
=\operatorname{tr}(N S_G N^T)
=\|N\Omega\|_2^2=\|v-\Omega\|_2^2.}
\tag{28}
\]

Indeed, since \(N\) is real,
\(N\mathcal H N^T=(N\Omega)(N\Omega)^\dagger\), a positive semidefinite Hermitian matrix. Its trace is real and nonnegative and equals the squared complex Euclidean norm. Also \(A_G^T=-A_G\), so
\((NA_GN^T)^T=-NA_GN^T\). Every diagonal entry of this real skew matrix is zero; thus its trace, and the imaginary contribution in (12), vanish. This proves the middle equality in (28) without any assumption of alignment. The symmetry of \(N\) for the present map is not needed for this trace argument; realness is enough.

### Direct transfer of the accepted theorem

For any \(y\in\mathcal Y\), choose a representative \(\Omega\in\mathcal D\). Combining (22), (27), (28), and the accepted inequality (6) gives

\[
\boxed{\widehat{\mathcal V}(F_{\mathcal R}y)-\widehat{\mathcal V}(y)
\le-\frac{16869}{20000}\widehat{\mathcal B}(y).}
\tag{29}
\]

This is retention and transfer of S0, not a new proof of native descent. The right-hand side still uses the prestage increment, not the complete displacement \(F\Omega-\Omega\).

Define

\[
y_*=(r_{*,1}^2,r_{*,2}^2,r_{*,3}^2,0,0)\in\mathcal Y.
\tag{30}
\]

The entire accepted common-phase fixed circle has retained tuple \(y_*\). Conversely, a tuple equal to (30) reconstructs the aligned coherence \(r_*r_*^T\), so its fibre is exactly that circle. Applying S0's equality classification to any representative proves

\[
\boxed{\widehat{\mathcal V}(F_{\mathcal R}y)=\widehat{\mathcal V}(y)
\quad\Longleftrightarrow\quad y=y_*.}
\tag{31}
\]

The state \(y_*\) is fixed under (21), and there is no other fixed retained state: any fixed retained state would have equality in (31). Likewise (28) and S0 imply \(\widehat{\mathcal B}(y)=0\) exactly at \(y_*\). These are statements using the already accepted profile, not a profile solve. Equality in the quantitative inequality (29) is not separately classified.

## 7. Minimum additional count in the full dictionary

The candidate (7) gives an upper bound of two additional real pair scalars. To exclude zero or one, it suffices to exhibit equal retained data but different current energy. No conclusion about dynamic nonclosure is needed for this lower bound.

Suppose a single retained entry concerns the pair \(\{i,j\}\), and let \(\ell\) be the remaining channel. Fix arbitrary amplitudes \(r_1,r_2,r_3\in[9/10,11/10]\). Keep the original labelled unequal \(k_i\) and every coefficient in (1) fixed. Consider the static family

\[
\Omega_i(t)=r_i,\qquad\Omega_j(t)=r_j,\qquad
\Omega_\ell(t)=r_\ell e^{it},\qquad 0\le t\le D_0.
\tag{32}
\]

Every member belongs to \(\mathcal D\). All three intensities are constant, as are both possible entry types for the retained pair:

\[
S_{ij}(t)=r_ir_j,\qquad A_{ij}(t)=0.
\tag{33}
\]

This covers any of the six singleton choices. The two edges involving \(\ell\) have

\[
E_{i\ell}(t)=(r_i-r_\ell)^2+2r_ir_\ell(1-\cos t),
\quad
E_{j\ell}(t)=(r_j-r_\ell)^2+2r_jr_\ell(1-\cos t).
\tag{34}
\]

The onsite potential is constant throughout the family, since its intensities and coefficients are constant. The \(ij\) edge is also constant. Hence, for every \(0<t\le D_0\),

\[
\boxed{\mathcal V(\Omega(t))-\mathcal V(\Omega(0))
=g r_\ell(r_i+r_j)(1-\cos t)>0.}
\tag{35}
\]

Thus one extra entry cannot determine the required individual edge energies or even the total native potential. With no extra entry, the same states still have identical retained intensities and different energy. Relabelling \(i,j,\ell\) only chooses which static family to display; the labelled dynamics and \(k\) are never permuted or assumed symmetric.

Equations (32)–(35) exclude every smaller subset for the joint objective, and (7) attains it. Therefore

\[
\boxed{m(\mathscr E)=2.}
\tag{36}
\]

This lower bound deliberately uses a stratum with one aligned pair. A representation required to work throughout \(\mathcal D\) must work there too. It is not a generic-chart count or a claim that each stratum needs two entries separately.

## 8. Real-coherence-only comparison

Now restrict the dictionary to
\(\mathscr E_{\rm real}=\{S_{12},S_{13},S_{23}\}\), with the same energy-retaining autonomous objective. It is not required to reconstruct signed complex coherence.

### All three suffice

The three intensities plus these three entries determine the full real Gram
\(S_G\). Let its actual domain be
\(\mathcal Z=\{S_G(\Omega):\Omega\in\mathcal D\}\).
The inherited `thm:Sclosure` gives a well-defined update on regular Gram fibres, including rank-deficient factors. Equal real Grams identify states related by a common phase and/or conjugation; both transformations preserve (2), and the native map has the required equivariances on the regular domain. By (5) and invariance, the induced real-Gram update maps \(\mathcal Z\) into itself and all subsequent iterates remain regular.

Every \(E_{ij}\) is immediately known from (25), the potential follows from (27), and the prestage norm follows from \(\operatorname{tr}(N S_G N^T)\). Thus (29) and its monotonicity equality classification transfer to this representation too. The fixed circle maps to the single real Gram \(r_*r_*^T\). Losing signed orientation is no obstacle for this energy objective.

### No two suffice throughout the domain

Any two distinct edges of a triad share one channel. Denote it by \(h\), with the other channels \(j,\ell\). Fix amplitudes \(r_i\in[9/10,11/10]\) and choose

\[
u>0,\quad v>0,\quad u+v\le D_0.
\]

Keep all coefficients (1) fixed, and form two static states

\[
\Omega_h^\pm=r_h,\qquad
\Omega_j^\pm=r_j e^{iu},\qquad
\Omega_\ell^\pm=r_\ell e^{\pm iv}.
\tag{37}
\]

The plus state's width is \(\max(u,v)\), and the minus state's width is \(u+v\); both are admitted, including the allowed boundary. Intensities and the two retained real entries agree:

\[
S_{hj}^+=S_{hj}^-=r_hr_j\cos u,\qquad
S_{h\ell}^+=S_{h\ell}^-=r_hr_\ell\cos v.
\]

The omitted entry differs because

\[
S_{j\ell}^+=r_jr_\ell\cos(u-v),\qquad
S_{j\ell}^-=r_jr_\ell\cos(u+v),
\]
\[
S_{j\ell}^+-S_{j\ell}^-=2r_jr_\ell\sin u\sin v>0.
\tag{38}
\]

Consequently

\[
E_{j\ell}^- - E_{j\ell}^+=4r_jr_\ell\sin u\sin v>0,
\quad
\boxed{\mathcal V(\Omega^-)-\mathcal V(\Omega^+)
=2g r_jr_\ell\sin u\sin v>0.}
\tag{39}
\]

The other two edge energies and all onsite terms agree. For example, \(u=v=\pi/24\) is an exact permitted member of this analytic family; no numerical state or map evaluation is required.

The labelled assignments covering all two-real-entry subsets are:

| Retained real entries | Shared anchor \(h\) | Other labels \((j,\ell)\) in (37) | Omitted entry |
|---|---|---|---|
| \(S_{12},S_{13}\) | 1 | \((2,3)\) | \(S_{23}\) |
| \(S_{12},S_{23}\) | 2 | \((1,3)\) | \(S_{13}\) |
| \(S_{13},S_{23}\) | 3 | \((1,2)\) | \(S_{12}\) |

These are separately labelled static states at the original fixed \(k\), not applications of a permutation symmetry of the dynamics. Counts zero and one are already excluded by Section 7. Therefore

\[
\boxed{m(\mathscr E_{\rm real})=3.}
\tag{40}
\]

### Comparison for the stated joint objective

| Additional raw entries, beyond all intensities | Autonomous representation established here or inherited? | Energy retention | Disposition |
|---|---|---|---|
| None | Not needed for exclusion | Fails: (32)–(35) give the same intensities with different current potential | Insufficient |
| Any single entry from \(\mathscr E\) | Not tested or claimed to fail dynamically | Fails by the same family with its retained pair fixed | Insufficient |
| \(A_{12},A_{13}\) | Yes, (19)–(24), with common-phase fibres | All three edge energies, potential, prestage norm, and descent retained | Attains full-dictionary minimum 2 |
| Any two real coherences | Not tested or claimed to fail dynamically | Fails: omitted edge energy and potential differ in (37)–(39) | Insufficient |
| All three real coherences | Yes, inherited real-Gram closure with persistent regularity | All required energy quantities and descent retained | Attains real-only minimum 3 |

Two anchor cosines leave an ambiguity in the sides of the anchor on which the other two phases lie; (37) changes that relative placement and hence the missing cosine. The signed sines remove this ambiguity on the narrow sector. This explains the raw-entry comparison without claiming that signed orientation is needed by the energy itself or that the candidate is the coarsest sufficient quotient.

## 9. Proportional verification, execution, and outputs

The written reconstruction, fibre, invariant-domain, and analytic witness arguments establish the continuous-domain statements. The optional isolated helper [exact_algebra.py](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01/exact_algebra.py) independently checks the pair-product signs, the Hermitian matrix reconstruction, \(\mathcal H=S_G-iA_G\), the real-matrix trace/norm identity, the transposed-entry phase sign, and the static potential-difference identities used for both lower bounds. It contains no native-step implementation and no repository imports. In particular it does not evaluate (19)–(21), solve a profile, or generate a trajectory.

The helper completed successfully using Command Prompt and the existing `torment` environment. [exact_algebra_results.json](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01/exact_algebra_results.json) records **PASS**, the exact checks and their purposes, and the actual environment: Python 3.11.15, SymPy 1.14.0, interpreter `C:/Users/Notandi/miniconda3/envs/torment/python.exe`. No packages were installed. Its generic symbolic matrix identities do not certify runtime floating-point arithmetic, and its check count is not a theorem count.

The successful invocation was:

```bat
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
call conda activate torment
python -I -B C:\TORMENT\TRIOCTAGON_new\research\NATIVE_CLOSED_INFORMATION_01\exact_algebra.py
```

The helper opens its result file in exclusive-create mode; a later intentional rerun should use a fresh output directory. No prior helper, including the accepted energy-response helper, was rerun.

Execution comprised bounded source reading and text/path searches, creating the previously absent external directory, authoring this note and the isolated helper, running that helper once, and checking the delivered files. Command Prompt was used for inspection, setup, and the Python invocation; file editing tools wrote only the fresh research outputs. Some initial text-search patterns required correction for Command Prompt quoting; these were read-only searches, not scientific executions. No applicable `AGENTS.md` was found in the bounded workspace guidance search.

No numerical native-step calls, trajectories, state-budget replays, profile solves, parameter searches, larger-ring investigations, observer/EMA advances, application launches, Git commands, repository edits, integration, or publication were performed. Existing research files were preserved. No dated suffix was needed.

All outputs are in `C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01`:

| Output | Purpose |
|---|---|
| [NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01/NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md) | This proof/review, exact scope, accepted dependencies, minimality witnesses, and execution record. |
| [exact_algebra.py](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01/exact_algebra.py) | Isolated symbolic checks of the load-bearing algebra and static witness differences. |
| [exact_algebra_results.json](C:/TORMENT/TRIOCTAGON_new/research/NATIVE_CLOSED_INFORMATION_01/exact_algebra_results.json) | PASS results, purposes, limitations, and environment metadata. |

The task ends here for GPT/author review. No common-phase-history reconstruction, new physical interpretation, successor investigation, implementation, paper, or publication has been initiated. The channel anchor remains bookkeeping, and the stationary-support and other standing scope distinctions are unchanged.
