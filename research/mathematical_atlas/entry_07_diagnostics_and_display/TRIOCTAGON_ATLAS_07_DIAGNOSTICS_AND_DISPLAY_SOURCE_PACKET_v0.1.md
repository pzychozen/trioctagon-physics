# Tri-Octagon mathematical atlas — Entry 07

## Diagnostics, finite-step accounting, and display maps

Version 0.1 · 29 September 2026 · External, read-only reconstruction; unpublished.

The diagnostics measure supplied state/readout data and report algebraic predictions, residuals, or display coordinates. They do not advance the canonical state. The finite-step intensity budget includes its full nonnegative remainder; a negative-gradient increment alone supplies no discrete descent theorem. The scalar displays retain different information from the total-vector display, and the history torus has a conditional inverse only under explicit hypotheses.

Authoritative repository: [trioctagon-physics](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics). Expected and inspected HEAD: **34c21830e7e7c4b5f4a5a940d084c37feaf1f82c**.

Atlas 01–05 remain closed and published; Atlas 06 remains closed, external, and unpublished. Their artifacts, Papers A–F, the old kernel and TORMENT are not modified. No historical or production module is executed. No paper revision, viewer launch, publication, commit or push is performed.

Companions: [checker](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_07_EXACT_CHECKS.py) and [results](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_07_EXACT_RESULTS.json).

Evidence labels used throughout:

- **SOURCE**: directly inspected accepted definition, implementation, or documented boundary.
- **DERIVATION**: algebra/proof supplied in this packet from those definitions.
- **WITNESS**: a bounded exact counterexample or numerical/API experiment, with its domain stated.
- **OPEN**: a documentary or runtime question not resolved by the evidence.

The results preserve a runtime caveat: focused pytest runs reported passing assertions and zero exit status, while stderr repeatedly reported Windows access violations. The mathematical/API check results and this unresolved runtime evidence are reported separately in §12.

## 1. Sources, public interface, and symbol dictionary

### 1.1 Source map

**SOURCE.** The checker records full file hashes and actual public signatures/record fields. The source IDs below are used as citations in this packet.

| ID | Exact source |
|---|---|
| DIAG | [z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py) |
| TEST | [test_z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_z_diagnostics.py) |
| E | [Paper E v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md) |
| Z | [z_manifold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py) |
| C | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py) |
| D | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py) |
| NUM | [_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py) |
| RUN | [_runner.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py) |
| RECORDS | [_records.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_records.py) |
| RUN_TEST | [test_runner_records.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_runner_records.py) |
| P9/P10 | [Paper-E parity tests](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_parity_p09_p10.py) |
| ORACLE | [independent Paper-E parity oracle](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/parity_oracles/paper_e_oracle.py) |
| ES | [Paper-E symbolic checker](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/check_symbolic.py), [retained symbolic receipt](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/symbolic_results.json), [edition checker](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/check_revision.py): supporting evidence, no broad historical workflow rerun |
| DP | [Paper D v0.1.1 §16.5](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md): potential normalization comparison only |
| A04 | [closed Atlas 04](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md): raw chirality and its established transport meaning |
| A06 | [closed external Atlas 06](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md): observer definitions, ownership, clock/memory separation and recording order |
| A01 | [closed Atlas 01 closeout](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_01_complex_triad/TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md): checked only for the bounded potential-normalization comparison; provenance investigations remain closed |

### 1.2 Public functions defined by the module

“Finite” in this table is the ideal input domain plus the implementation's stricter checked-intermediate domain described in §10. Integer clock fields exclude booleans. Historical names do not imply physical coordinates or energy.

| Function | Input / return | Definition and proof location |
|---|---|---|
| quadratic_form(vector) | Finite real (3,) vector → real scalar | $Q(v)=v_1^2+v_2^2-v_3^2$; §2, E (20) and DIAG's full generalization |
| readout_accounting(readout, *, alpha, beta) | ZReadout; checked real signed weights → ReadoutAccounting | Stored-value blend/norm/Q residuals; §2, E (18)–(20) |
| chiral_area_accounting(omega) | Finite complex (3,) state → ChiralAreaAccounting | Raw C, Gram determinant, bound/slack; §3, E (16)–(17) |
| historical_alignment(macro, chiral, total_vector) | Three checked real (3,) vectors → HistoricalAlignment | Thresholded normalized dots and resolution flags; §4, E (21),(23) |
| intensity_budget(omega, config) | Complex (3,) and DynamicsConfig with finite stored real values → IntensityBudget | Unforced pre-sync finite-step accounting; §5, E (33)–(36) |
| potential(omega, config) | Same state/config domain → real scalar | Six-real potential; §6, E (37)–(38) |
| direct_history_coordinates(history, key="Z_total") | Selected finite real (n,3) data; n may be zero → Coordinates | Copy selected stored vector columns; §7, E §11.1 |
| cylinder_point(kappa, q, z, *, N=12) | κ≥0, finite z, integer q,N>0 → read-only (3,) array | Scalar cylinder; §7, E (24), explicit current N |
| cylinder_history_coordinates(history, *, N=12) | Equal-length one-dimensional κ,z,integer phi_index arrays; empty allowed → Coordinates | Rowwise cylinder; §7 |
| history_torus_coordinates(history, *, R=2, r_max=1, N=12) | Same scalar history, nonempty, $R>r_{\max}>0$ → HistoryTorus | Whole-history normalization and torus map; §8, E (25),(27) |

The six returned record types are ReadoutAccounting, ChiralAreaAccounting, HistoricalAlignment, IntensityBudget, Coordinates, and HistoryTorus. All their fields are inventoried below. The module also imports helper objects; those imports are not additional diagnostic operations defined by it.

### 1.3 Disambiguating symbols

| Symbol | Meaning here | Distinct from |
|---|---|---|
| Ω=x+iy | Canonical complex state | Display coordinates or diagnostic prediction |
| z,M,C,T | Supplied observer scalar, macro, raw chirality and total | State intensity or physical energy |
| A,B,h | $x\cdot x,\ y\cdot y,\ x\cdot y$ in area accounting | Earlier matrices and Atlas-06 harmonic h |
| I | $\|\Omega\|^2=A+B$ | Identity matrix, denoted $\mathrm{Id}_3$ below |
| Q | Signed scalar form with $G=\operatorname{diag}(1,1,-1)$ | Earlier transverse projector or scaled covering isometry |
| D | Complex recurrence increment, identified with six real coordinates | Atlas-04 tangent decoder |
| $\widetilde\Omega$ | Pre-synchronization state Ω+D | E's pre-state symbol V |
| $\mathcal V$ | Real scalar potential | E's vector V, intensity I, z or Q(T) |
| P | Sum of pairwise squared state distances | Earlier covering pullback or Atlas-06 cubic product |
| h in $Du(T)[h]$ | A perturbation vector | Gram scalar h or observer harmonic |

## 2. Supplied readout norm and signed-Q accounting

### 2.1 Full expansions

**DERIVATION.** For arbitrary real three-vectors M,C and real signed α,β, set $\widehat T=\alpha M+\beta C$. Bilinearity and symmetry of the Euclidean product give

$$
\|\widehat T\|^2=\alpha^2\|M\|^2+\beta^2\|C\|^2+2\alpha\beta M\cdot C.
$$

Define $B_Q(u,v)=u^TGv=u_1v_1+u_2v_2-u_3v_3$, so $Q(v)=B_Q(v,v)$. The same expansion yields

$$
Q(\widehat T)=\alpha^2Q(M)+\beta^2Q(C)+2\alpha\beta B_Q(M,C).
$$

The term $\alpha^2Q(M)$ is required for general supplied vectors. If the macro-law hypothesis $M=z(\cos\theta,\sin\theta,1)$ has separately been established, then

$$
Q(M)=z^2(\cos^2\theta+\sin^2\theta-1)=0,
$$

and only then does E (20)'s shortened expression apply. For example M=(1,2,3), C=0, α=2 has Q(αM)=−16, not zero. Q can have either sign and can vanish on nonzero vectors. It is a diagnostic quadratic form; no spacetime metric is asserted. [DIAG: quadratic_form, readout_accounting; E §§9.1–9.2]

### 2.2 Every ReadoutAccounting field

Let $m^2=M\cdot M$, $c^2=C\cdot C$, $t^2=T\cdot T$. Here T is the **supplied** vector, not silently replaced by $\widehat T$.

| Fields | Exact intended contents |
|---|---|
| alpha, beta | Validated supplied α,β |
| variant, initialization | Markers copied from the readout |
| supplied_z | Validated stored scalar z |
| macro_norm_squared, chiral_norm_squared, total_norm_squared | $m^2,c^2,t^2$ |
| weighted_macro, weighted_chiral | $\alpha^2m^2,\ \beta^2c^2$ |
| cross_term | $2\alpha\beta M\cdot C$ |
| predicted_norm_squared | Sum of the preceding three weighted terms, $\|\widehat T\|^2$ ideally |
| norm_residual | $t^2-\mathrm{predicted\_norm\_squared}$ |
| blend_residual | Vector $T-\widehat T$ |
| q_macro, q_chiral, q_total | $Q(M),Q(C),Q(T)$ |
| q_weighted_macro, q_weighted_chiral | $\alpha^2Q(M),\ \beta^2Q(C)$ |
| q_cross_term | $2\alpha\beta B_Q(M,C)$ |
| q_prediction | Sum of all three weighted Q terms, including q_weighted_macro |
| q_residual | $Q(T)-\mathrm{q\_prediction}$ |
| macro_relation_residual | $\|M\|^2-2z^2$, using supplied_z |

**SOURCE.** The function validates and inspects stored values; it does not recompute Ω, a clock, M, C or T from an observer formula. Its blend_residual array is copied and made read-only. It leaves inconsistent supplied data intact. [DIAG; Z: ZReadout; A06 §§7–8]

**DERIVATION / WITNESS.** The residuals answer different consistency questions. blend_residual=0 is the exact vector blend condition for these supplied inputs. norm_residual=0 compares only squared lengths; q_residual=0 compares only the signed form. macro_relation_residual=0 checks one scalar consequence of the macro law.

Take z=1, M=(1,0,1), C=0, T=−M, α=1, β=0. The norm, Q and macro-relation residuals all vanish but blend_residual=(−2,0,−2). Scalar residuals therefore cannot certify the vector relation.

Even all the listed residuals can vanish without a valid macro law: take z=1, M=T=(1,0,−1), C=0, α=1, β=0. Q(M)=0 and $\|M\|^2=2z^2$, but $M_3=-1\ne z$. No θ satisfies the required macro law with that supplied z. Nor can these diagnostics alone identify a particular Ω, clock, observer call, or recorded history.

The ordinary inconsistent fixture z=1, M=(1,2,3), C=(0,1,0), T=(8,0,1), α=β=1 produces blend_residual=(7,−3,−2), norm_residual=46, q_residual=62, and macro_relation_residual=12. These are returned, not repaired.

### 2.3 Cancellation and norm bounds

**DERIVATION.** If β≠0, T=0 iff $C=-\alpha M/\beta$. If β=0, it means αM=0. If α=0, β≠0, it means C=0; if both weights vanish, every supplied pair cancels. When both weighted vectors are nonzero, cancellation requires equal lengths and opposite weighted directions.

Let $u=|\alpha|\|M\|$ and $v=|\beta|\|C\|$. For nonzero weighted vectors their cosine η lies in [−1,1], so

$$
\|\widehat T\|^2=u^2+v^2+2uv\eta,\qquad
(u-v)^2\leq\|\widehat T\|^2\leq(u+v)^2.
$$

Taking nonnegative square roots gives the reverse-triangle and triangle bounds

$$
\bigl||\alpha|\|M\|-|\beta|\|C\|\bigr|
\leq\|\widehat T\|\leq|\alpha|\|M\|+|\beta|\|C\|.
$$

Zero-vector cases follow directly. The sign of the unweighted cosine alone does not determine the sign of the cross term when αβ<0.

These are statements about supplied vector pairs; not every algebraically selected pair must be attainable from one common state or trajectory. A valid pointwise EMA example is Ω=(1,−i,−1), λ=0, current m=−1, q=0, α=1, β=−1: M=C=(−1,0,−1) and T=0. This uses an admitted supplied memory; it does not assert reachability from the historical zero-memory initializer in finitely many exact updates. [E (18)–(19), Proposition 8; DIAG; TEST]

## 3. Chiral Gram identity, slack and sharp bound

**SOURCE.** A04 establishes raw $C=x\times y$ and its channel-space interpretation. No transport derivation is reopened.

**DERIVATION.** Put $A=x\cdot x$, $B=y\cdot y$, $h=x\cdot y$, $I=A+B$. Expanding the three squared determinants gives

$$
\begin{aligned}
\|C\|^2
&=\sum_{i<j}(x_i y_j-x_j y_i)^2\\
&=\sum_{i,j}x_i^2y_j^2-\sum_{i,j}x_i y_i x_j y_j
=AB-h^2.
\end{aligned}
$$

Consequently

$$
\frac{I^2}{4}-\|C\|^2
=\frac{(A+B)^2}{4}-AB+h^2
=\frac{(A-B)^2}{4}+h^2\geq0.
$$

Since I and $\|C\|$ are nonnegative, $\|C\|\leq I/2$. Equality holds iff both squares on the right vanish: A=B and h=0. This includes Ω=0. At nonzero equality, x and y have equal nonzero lengths and are perpendicular. Conversely those conditions attain equality. The family x=(a,0,0), y=(0,a,0) gives $\|C\|=a^2=I/2$, so the constant 1/2 is sharp. [E (16)–(17), Theorem 7]

### ChiralAreaAccounting fields

| Fields | Exact intended contents |
|---|---|
| chiral | Raw C, delegated once to C.z_chiral |
| A, B, h | $x\cdot x,\ y\cdot y,\ x\cdot y$ |
| intensity | I=A+B |
| chiral_norm, chiral_norm_squared | $\|C\|,\ \|C\|^2$ |
| gram_product, h_squared | AB, h² |
| gram_rhs | AB−h² |
| gram_residual | $\|C\|^2-(AB-h^2)$ |
| amplitude_bound | I/2, a bound on the norm of C, not on each original amplitude |
| slack_sum_of_squares | $(A-B)^2/4+h^2$ |
| observed_slack | $(I/2)^2-\|C\|^2$ |
| slack_residual | observed_slack−slack_sum_of_squares |

Under Ω→rΩ for real r, I and C scale by r²; their squared/slack expressions scale by r⁴. The bound is sharp **at a given state intensity**. It is not uniform over unbounded Ω, since the equality family grows without bound. A bound relating simultaneous state quantities does not make either one conserved by a recurrence.

**WITNESS / LIMIT.** Nearly parallel finite input can produce a nonzero signed floating gram_residual. The implementation neither clamps it nor replaces Gram subtraction with a presumed nonnegative answer. A rounded residual of zero is not an exact equality certificate. [DIAG: chiral_area_accounting; TEST; P10]

## 4. Alignment, resolution and direction conditioning

**SOURCE.** For each supplied real vector v, historical_alignment uses a stable checked norm and

$$
u_{\rm hist}(v)=
\begin{cases}
0,&\|v\|<10^{-12},\\
v/\|v\|,&\|v\|\geq10^{-12}.
\end{cases}
$$

The strict lower branch is preserved: **exactly 10⁻¹² uses the normalized branch**. Nonfinite or invalid inputs are rejected; this is not a sanitizer.

| HistoricalAlignment field | Meaning |
|---|---|
| d_TM | $u_{\rm hist}(T)\cdot u_{\rm hist}(M)$ |
| d_CM | $u_{\rm hist}(C)\cdot u_{\rm hist}(M)$ |
| d_TC | $u_{\rm hist}(T)\cdot u_{\rm hist}(C)$ |
| macro_resolved, chiral_resolved, total_resolved | Respective norm≥10⁻¹² tests |
| TM_resolved, CM_resolved, TC_resolved | Logical AND of the corresponding two individual flags |
| threshold | The literal 1e−12 |

**DERIVATION.** If both vectors are resolved, their normalized dot is the cosine of the ordinary Euclidean angle. Cauchy–Schwarz bounds it in [−1,1] in exact arithmetic; equality ±1 means parallel/opposite directions. If either is unresolved, the stored dot is zero by convention.

**WITNESS.** M=(10⁻¹³,0,0), T=C=(1,0,0) are parallel, but d_TM=d_CM=0 and both pair flags are false. M=(0,1,0), T=C=(1,0,0) also gives d_TM=0, this time with resolved flags and actual orthogonality. The flag is necessary to distinguish them. No numerical cosine clipping is applied. [E §10, (23); DIAG; TEST]

**DERIVATION.** For mathematical normalization $u(T)=T/\|T\|$ at T≠0, a perturbation h satisfies

$$
D\|T\|[h]=u\cdot h,\qquad
Du(T)[h]=\frac{h-u(u\cdot h)}{\|T\|}
=\frac{(\mathrm{Id}_3-uu^T)h}{\|T\|}.
$$

The numerator projects onto the plane perpendicular to T. The derivative's Euclidean operator norm is $1/\|T\|$, attained by a perpendicular perturbation. Near cancellation, a small change in T can therefore cause a large change in direction. For $T_\pm=\pm\eta e_2$, their displacement is 2η→0 while their unit-vector separation stays two.

This derivative concerns ordinary normalization away from zero, not a differentiability claim for the thresholded piecewise algorithm across its boundary. It explains direction conditioning, not physical speed. Alignment cosines, or differences between them, are not energy fractions; the signed cross term in §2 is the applicable norm accounting. [E (21),(23)]

## 5. Exact finite-step intensity accounting

### 5.1 Identity and hypotheses

**SOURCE.** The accepted unforced triad recurrence uses real ε,g,k_i and the negative graph Laplacian

$$
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
$$

Set $s_i=|\Omega_i|^2$, $I=\sum_i s_i$,

$$
D_i=\epsilon(k_i-s_i)\Omega_i+g(L_3\Omega)_i,\qquad
\widetilde\Omega=\Omega+D,\qquad
P=\sum_{i<j}|\Omega_i-\Omega_j|^2.
$$

There is no forcing/noise term or extra dt here. phase_strength belongs to the existing separate phase operation. DIAG validates the stored DynamicsConfig values, including phase_strength, although this budget does not apply that operation.

**DERIVATION.** With Hermitian product $\langle u,v\rangle=\sum_i\bar u_i v_i$, expand each pair distance. Each $|\Omega_i|^2$ occurs twice and off-diagonal terms occur in conjugate pairs:

$$
\langle\Omega,L_3\Omega\rangle
=-2\sum_i|\Omega_i|^2+\sum_{i\ne j}\bar\Omega_i\Omega_j=-P.
$$

This is real and nonpositive. Expanding the finite increment exactly, without dropping a quadratic term, gives

$$
\begin{aligned}
\|\widetilde\Omega\|^2-I
&=2\Re\langle\Omega,D\rangle+\|D\|^2\\
&=2\epsilon\sum_i(k_i s_i-s_i^2)-2gP+\|D\|^2.
\end{aligned}
$$

Writing $a_i=(k_i-s_i)\Omega_i$, the remainder itself expands as

$$
\|D\|^2=
\epsilon^2\sum_i s_i(k_i-s_i)^2
+g^2\|L_3\Omega\|^2
+2\epsilon g\Re\sum_i(k_i-s_i)\bar\Omega_i(L_3\Omega)_i.
$$

The cross term may have either sign; the complete squared norm is nonnegative. For g≥0 the coupling contribution −2gP is nonpositive, whereas g<0 reverses its sign when P>0. For ε≥0 each onsite summand has the sign of k_i−s_i when s_i>0; the sum may have either sign. Negative ε reverses these signs. None of these first-order sign observations controls the full finite update without its remainder. [E (33)–(36), Theorem 11]

### 5.2 Every IntensityBudget field

| Field | Exact intended contents |
|---|---|
| component_intensities | $(s_1,s_2,s_3)$ |
| intensity_before | I |
| increment | D from its defining onsite and imported-L3 terms |
| diagnostic_pre_sync_prediction | $\widetilde\Omega=\Omega+D$, a diagnostic complex array |
| intensity_pre_sync | $\|\widetilde\Omega\|^2$ computed inside the diagnostic |
| pair_distance_sum | P |
| onsite | $2\epsilon\sum_i(k_i s_i-s_i^2)$ |
| coupling | −2gP |
| remainder | $\|D\|^2$ |
| predicted_delta | onsite+coupling+remainder |
| observed_delta | intensity_pre_sync−intensity_before |
| residual | observed_delta−predicted_delta |

Despite the field name observed_delta, its value comes from the **diagnostic's own pre-sync prediction**, not a supplied or independently fetched canonical next state. It checks the diagnostic algebra. The function does not call step3 or phase_sync and cannot replace the authorized recurrence output.

### 5.3 Required exact overshoot

**WITNESS.** For Ω=(2,2,2), ε=1, k=(1,1,1), g=0 and phase_strength=0:

$$
s_i=4,\quad D_i=2(1-4)=-6,\quad
\widetilde\Omega=(-4,-4,-4).
$$

| Quantity | Exact value |
|---|---:|
| I before / after | 12 / 48 |
| P | 0 |
| onsite | $2\cdot3(4-16)=-72$ |
| coupling | 0 |
| remainder | $3\cdot36=108$ |
| predicted_delta = observed_delta | 36 |
| residual | 0 |

Thus a negative onsite contribution can coexist with growth of total intensity. This witness uses exactly the requested g=0; it does not need rounding error or an observer.

A second exact qualification is pure coupling on Ω=(1,−1,0), ε=0: the pre-state is $(1-3g)\Omega$ and $\Delta I=6g(3g-2)$. Positive g>2/3 increases intensity, despite the first-order graph term being negative.

### 5.4 What phase synchronization preserves

**DERIVATION / SOURCE.** The accepted synchronizer changes each nonzero pre-state component to $|\widetilde\Omega_i|e^{i(\phi_i+\delta_i)}$ with real δ_i. Its modulus is unchanged. Zero remains zero under the accepted zero-amplitude convention. Therefore all current-step s_i and their sum are preserved ideally, so the finite intensity identity also holds after that phase operation. Binary64 reconstruction has rounding effects.

Relative phases affect pairwise interference in the graph term of later updates. Preserving component magnitudes in this phase operation does not imply equal magnitudes after the next coupled update. The checker verifies this with two phase-off/on continuations of the same bounded mixed input. No recurrence symmetry or harmonic provenance is inferred. [D; E §17.2; A06]

## 6. Potential, gradient identity and normalization comparison

**SOURCE.** The implemented potential is

$$
\mathcal V(\Omega)=
\epsilon\sum_i\left(\frac{s_i^2}{4}-\frac{k_i s_i}{2}\right)
+\frac g2P.
$$

**DERIVATION.** Use six real coordinates $(x_1,x_2,x_3,y_1,y_2,y_3)$. Since $\partial s_i/\partial x_i=2x_i$,

$$
\frac{\partial\mathcal V}{\partial x_i}
=\epsilon(s_i-k_i)x_i+g\sum_{j\ne i}(x_i-x_j)
=\epsilon(s_i-k_i)x_i-g(L_3x)_i.
$$

The identical y derivative replaces x by y. Negating the six derivatives gives the real/imaginary components of D exactly:

$$
D=-\nabla_{\mathbb R^6}\mathcal V.
$$

This specifies the gradient convention; it is not an ambiguous complex derivative. [DIAG: potential; E (37), Proposition 12]

**WITNESS.** At the §5 overshoot parameters,

$$
\mathcal V(2,2,2)=3(4-2)=6,\qquad
\mathcal V(-4,-4,-4)=3(64-8)=168.
$$

So the exact negative-gradient **increment** does not guarantee descent under the unit-size discrete update. Replacing it with a continuous gradient flow would change the model. Historical dt supplies no missing gradient-step multiplier.

The phase operation preserves all s_i, hence the onsite part of $\mathcal V$. It may change P and therefore the graph term. If g=0, the phase operation preserves this potential; for general g there is no universal sign conclusion.

**New exact WITNESS.** Consider unit-amplitude pre-state phases $(0,\pi/6,0)$ and the adopted synchronizer with strength π/6. The increments give new phases $(\pi/6,-\pi/6,\pi/6)$. Before and after, every s_i=1. Yet P changes from $4-2\sqrt3$ to 2, so the phase stage alone changes the graph potential by

$$
\Delta\mathcal V=g(\sqrt3-1)>0\quad(g>0).
$$

This is a bounded counterexample to a universal descent assertion for the phase stage, not a change to the recurrence or its provenance.

**DERIVATION — additive constant.** Completing the square gives

$$
\mathcal V_{\rm square}
=\frac\epsilon4\sum_i(s_i-k_i)^2+\frac g2P
=\mathcal V+\frac\epsilon4\sum_i k_i^2.
$$

Thus, if comparing these two normalizations, the exact parameter-only constant is $\epsilon\sum_i k_i^2/4$; for common k it is $3\epsilon k^2/4$. Their gradients and finite differences at fixed parameters agree. At ε=1,k_i=1, the square-normalized overshoot values would be 27/4 and 675/4, still differing by 162.

**SOURCE / OPEN boundary.** Actual Paper D (35) and Paper E (37) both use the expanded normalization implemented by DIAG. The available preserved Atlas 01–06 packets were searched for a differing completed-square formula; no such displayed earlier Atlas formula was located. The identity above is therefore a derived normalization comparison, not an invented attribution to an earlier document. If another earlier formula was intended, that documentary identification remains OPEN. No preserved document is revised.

I, $\mathcal V$, z, Q(T), and $\|T\|^2$ are distinct functions on distinct supplied inputs. The potential identity alone identifies none of them as physical energy. [DP §16.5; E §18; A01, A06]

## 7. Direct and scalar-cylinder displays

### 7.1 Direct coordinates

**SOURCE.** direct_history_coordinates selects a stored (n,3) real array. The default key is Z_total. It falls back to Z_vec **only when Z_total is absent**. If an explicitly requested key is absent, KeyError is raised; no other fallback is used. If Z_total is present but malformed or nonfinite, validation fails rather than substituting Z_vec.

The result Coordinates contains x, y and z, each a fresh detached read-only copy of a selected column. The function does not scale, normalize, rotate, select a face, or register a scaffold. A properly shaped empty array (0,3) is accepted; a bare empty list is one-dimensional and is rejected.

The map is lossless for the selected vector values: stacking the three returned columns recovers them. It does not retain the source key, times, Ω, clock, configuration, decomposition, or provenance. It cannot invert the observer just because it faithfully copies T. [DIAG; E §11.1]

### 7.2 Cylinder and custom sectors

**SOURCE / DERIVATION.** For κ≥0, θ=$2\pi(q\bmod N)/N$ and real z,

$$
F(\kappa,\theta,z)=(\kappa\cos\theta,\kappa\sin\theta,z).
$$

The current point helper and history helper both honor their explicit N parameter, default 12. The history helper requires equally sized one-dimensional kappa, z and phi_index arrays; q entries must be integers. It validates N even for an empty history. Zero/negative sector values are handled by modular integer reduction; negative κ is invalid.

Given exact XYZ:

- $\kappa=\sqrt{X^2+Y^2}$ and z=Z are always retained.
- If κ>0, θ=atan2(Y,X) is recoverable modulo 2π; known N identifies the admitted sector residue, not raw q or turn count.
- If κ=0, X=Y=0 for every θ: angle disappears, but **z is still retained**.

This is a radial-coordinate display of scalar data. Varying κ makes it a family of coaxial cylinders, not a fixed-radius surface. It does not recover complex channel phases, C, or T.

**SOURCE comparison only.** Paper E v0.1.1 §11.1 and its edition check establish that the two preserved historical cylinder helpers hardcoded twelve sectors; an alternate historical torus helper used its configured sector count. Current DIAG helpers use custom N explicitly. No historical helper is imported or executed here. Historical channel-torus curves and viewer percentile scaling are not features of this module. [DIAG; E (24), §11.1; ES edition checker]

## 8. Whole-history torus, bounds and conditional inverse

### 8.1 Map and geometric range

**SOURCE.** For a finite nonempty scalar history, define

$$
z_{\max}=\max_j|z_j|,\qquad H_z=z_{\max}+\delta,\quad\delta=10^{-9},
$$

$$
r=r_{\max}\frac{\kappa}{1+\kappa},\qquad
\chi=\frac{\pi z}{2H_z},\qquad
G_{\mathcal H}=
((R+r\cos\chi)\cos\theta,\ (R+r\cos\chi)\sin\theta,\ r\sin\chi).
$$

The accepted display domain is $R>r_{\max}>0$, finite κ≥0 and finite scalar histories. Empty histories are invalid. Defaults are R=2, r_max=1,N=12; custom N uses the same clock rule as the cylinder.

**DERIVATION.** In exact arithmetic,

$$
0\leq r<r_{\max},\qquad
r_{\max}-r=\frac{r_{\max}}{1+\kappa}>0,
$$

$$
|\chi|\leq\frac{\pi z_{\max}}{2(z_{\max}+\delta)}
<\frac\pi2.
$$

The last strict gap is $\pi\delta/[2(z_{\max}+\delta)]>0$. The positive regularizer prevents division by zero even when all z_j=0, in which case χ=0 for every row. It also keeps the exact extrema inside the admitted angular branch. It does not sanitize nonfinite histories or supply a physical length/time scale.

Let $s=\sqrt{X^2+Y^2}$, u=s−R and Z be the plotted vertical coordinate. Because cosχ>0,

$$
s=R+r\cos\chi>0,\quad
u=r\cos\chi\geq0,\quad
u^2+Z^2=r^2<r_{\max}^2.
$$

For κ>0, u>0; for κ=0, u=Z=0. In a meridional plane this lies in the open outer half-disc of radius r_max, together with its centre on the major ring. Rotating that section describes an outer portion of a solid toroidal tube, not a single fixed-minor-radius torus surface. A fixed history further restricts $|\chi|$ to its bound above; integer N restricts θ to its sector grid, and a finite supplied history yields only its finite set of samples. No claim of filling the continuous region is made.

### 8.2 Every HistoryTorus field

| Field | Meaning |
|---|---|
| x, y, z | Detached read-only plotted XYZ columns; this returned z is $r\sin\chi$, **not the input scalar z** |
| r | Detached read-only minor-radius array |
| chi | Detached read-only normalized minor-angle array |
| z_max | Supplied-history maximum absolute scalar height |
| H_z | Actual evaluated normalization z_max+1e−9, including its rounding |
| regularizer | Literal 1e−9 |
| R, r_max, N | Validated display parameters |
| normalization | Literal entire_supplied_history |

Coordinates and HistoryTorus are frozen records with copied arrays, not objects attached to the material shell. The normal function paths validate inputs; manual record constructors do not certify mathematical consistency. [DIAG; E (25)]

### 8.3 Conditional inverse of XYZ

**DERIVATION.** Assume known $R>r_{\max}>0$, known fixed H_z>0, finite κ>0, a point generated by this exact map, and the admitted branch $|\chi|<\pi/2$. Then:

$$
\begin{aligned}
s&=\sqrt{X^2+Y^2},&u&=s-R,&r&=\sqrt{u^2+Z^2},\\
\theta&=\operatorname{atan2}(Y,X)\pmod{2\pi},&
\chi&=\operatorname{atan2}(Z,u),\\
\kappa&=\frac{r}{r_{\max}-r},&
z&=\frac{2H_z\chi}{\pi}.
\end{aligned}
$$

The positive major radius determines θ. Since $(u,Z)=r(\cos\chi,\sin\chi)$, r>0 and u>0 recover χ on its specified branch. Strict r<r_max makes the κ inverse finite; known H_z restores scalar height. Known N identifies a sector residue if the point is known to arise on that grid, not a raw integer lift.

This does not invert Ω or T. If H_z is unknown, the same point generally fixes only the ratio z/H_z. Knowing the correct global H_z is therefore part of the inverse data, not something a single XYZ point establishes.

**WITNESS / precision qualification.** The runtime inverse is not implemented. The external checker applies the analytic inverse only as a bounded verification on admitted fixtures. A successful forward float evaluation does not guarantee its strict hypotheses: r may round to r_max, H_z to z_max, and χ to ±π/2. Moreover with κ=10⁻²⁰,q=0,z=0,R=2,r_max=1, the returned r is positive, but R+r rounds to R and XYZ becomes (2,0,0). Even a positive radius can disappear from rounded coordinates. Inversion is also ill-conditioned near saturation:

$$
\frac{d\kappa}{dr}=\frac{r_{\max}}{(r_{\max}-r)^2}.
$$

Small r brings cancellation in s−R and sensitivity of the minor angle. No numerical inverse or “improved” policy is introduced. [E (27), Proposition 9; DIAG]

### 8.4 κ=0: distinguish XYZ from the full returned record

At κ=0, r=0 and

$$
G_{\mathcal H}(0,\theta,z)=(R\cos\theta,R\sin\theta,0).
$$

Because R>0, **θ remains visible modulo 2π**. Scalar z disappears from XYZ, regardless of H_z; the plotted vertical coordinate is zero. κ=0 is detectable ideally as the centre of the meridional section.

The full HistoryTorus record contains extra metadata: χ and H_z are returned even at r=0. Given those exact fields one can recover input scalar z from $2H_z\chi/\pi$, including at κ=0. This is not an inverse of XYZ alone. Conversely the cylinder at κ=0 retains z while losing θ. Neither map recovers all complex channel information.

### 8.5 History dependence

**DERIVATION / WITNESS.** Appending a row with larger |z| increases H_z, reducing the absolute minor angle of an earlier unchanged nonzero scalar. Its plotted coordinates therefore change even though its earlier κ,q,z are unchanged.

For the earlier row κ=1,q=1,z=0.2,N=12,R=2,r_max=1:

| Supplied history | H_z | Earlier plotted XYZ (binary64 witness) |
|---|---:|---|
| That row alone | 0.200000001 | (1.732050811, 1.000000002, 0.5) |
| Append κ=1,q=2,z=2 | 2.000000001 | (2.159732405, 1.246922085, 0.078217232) |

The first plotted vertical value rounds to 0.5; ideal χ remains strictly below π/2. This batch dependence prevents interpreting the map as a causal state evolution. Appending rows that do not increase the maximum leaves its normalization unchanged. [E §11.2; DIAG; TEST]

## 9. Information-loss comparison

**Exact WITNESS.** At matching staged clock/configuration,

$$
\Omega_a=(1,1,1),\qquad \Omega_b=(1,i,1)
$$

both have κ=√3, so they share ρ, scalar z and M. Direct cross products give

$$
C_a=0,\quad C_b=(-1,0,1),\qquad
T_b-T_a=\beta(-1,0,1).
$$

For β≠0 their totals differ. Their cylinder inputs are identical; their torus points are identical when the normalization is shared (including the matched one-row histories). Even an exact torus scalar inverse cannot recover the missing C and hence cannot generally reconstruct T.

| Map/input | Retained by coordinate output | Lost or not supplied | Inverse hypotheses | Dependence on other rows |
|---|---|---|---|---|
| Direct: selected stored vector | All three selected vector values | Ω, decomposition, clock, metadata | Stack the copied columns; this recovers only that vector | None in this adapter |
| Macro: z,θ | z from M₃; θ modulo 2π if z≠0 after dividing horizontal coordinates by z | Angle at z=0; raw C and most Ω information | Macro-law hypothesis; z≠0 for angle | None at fixed observer inputs; EMA z may depend on supplied memory |
| Cylinder: κ,θ,z | κ,z; θ when κ>0 | Angle at κ=0; complex phases, C,T | κ>0 for angle; known N for sector residue | None |
| Torus XYZ: κ,θ,z plus normalization | Conditional κ,θ,z; θ persists at κ=0 | Scalar z at κ=0; normalization if omitted; complex channels, C,T | Known R,r_max,H_z; finite κ>0; admitted branch; ideal strict radius | Entire supplied scalar history through H_z |
| Full HistoryTorus record | XYZ plus r,χ,H_z and display parameters | Raw q lift, t, Ω,C,T; numerical rounding losses remain | Metadata can restore z even at κ=0; κ inverse still needs r<r_max | Entire supplied history |

The macro cone, scalar cylinder, history torus, direct channel-coordinate plot and Paper-C material shell are distinct mathematical objects. Equal-looking points or axis labels do not identify them.

**SOURCE comparison only.** E (26) discusses three historical channel-torus curves driven by individual channel magnitudes/phases and fixed channel azimuths, rather than the present clock/scalar map. E (29) describes a viewer's history-dependent 99th-percentile overlay scaling. Neither algorithm is implemented by DIAG's direct/cylinder/torus adapters. No viewer, historical source module, or percentile workflow is executed or restored. [E §§11–12; A04; A06]

## 10. Passivity, precision and ownership boundaries

### 10.1 Calls as well as imports

**SOURCE.** DIAG imports DynamicsConfig and L3 but never calls a recurrence. Its dependency paths are validators and checked products/sums; raw C.z_chiral; pure Z.blend_vectors; and Clock/clock_angle for display angles. None advances Ω, clock, or EMA memory.

**WITNESS.** The checker patches step3, step_ring, _advance, phase_sync, advance_clock and advance_ema to raise if called, then successfully exercises all ten public diagnostic/display functions. It separately inspects call names and performs a fresh-process import check excluding historical/production and shell/face/scaffold modules. Importing dynamics for constants/types is not evidence of state advancement.

Ordinary inputs are copied/validated; successful and failed calls preserve input state/history/readout bytes in the checked cases. Arrays returned in accounting, budgets, coordinates, torus metadata and cylinder points are detached and read-only. Frozen records reject ordinary field assignment. These protections are not a security boundary against deliberately changing NumPy flags or bypassing frozen attributes.

**SOURCE / WITNESS.** Several record constructors merely freeze array fields. They are not general validators or proof certificates when manually called: for example Coordinates can be directly constructed with mismatched column lengths or nonnumeric entries. Normal function paths validate their domains before returning them. Likewise A06's manually supplied ZReadout can be mathematically inconsistent; accounting reports rather than repairs it.

### 10.2 Numerical domain

| Issue | Recorded consequence |
|---|---|
| Polynomial degree | I,Q(real vector) are quadratic in their direct inputs; C is quadratic in Ω; C²/Gram and potential have quartic terms in Ω; D has cubic terms and its squared remainder can have degree six. Their representable domains differ. |
| Stable norms versus squares | Alignment's hypot can resolve large vectors whose squared norm would overflow elsewhere. Successful observation or alignment is not a guarantee of successful quartic accounting. |
| Checked intermediates | Nonfinite or nonzero-subnormal products/results and specified nonzero values lost to zero raise ResponsePrecisionError. Products are checked before cancellation. Zero coefficients do not universally skip validation or calculation of the other terms. |
| Compensated sums | math.fsum improves summation of already-rounded terms; it is not exact real arithmetic and cannot restore multiplication errors. Zero residual is not a certificate; signed residuals are not clamped. |
| Threshold | Norm<1e−12 is unresolved; equality resolves. Numerical cosine scores are not clipped or universally certified to lie in [−1,1]. |
| Saturation and regularizer | r can round to r_max; H_z can round to z_max. The returned actual values make this visible. Strict inverse hypotheses are not ensured by successful forward evaluation. |
| Small minor radius | Adding a tiny nonzero r to R can erase its radial contribution in XYZ; the separate r metadata may retain it. |
| History dynamic range | Dividing a tiny z by a very large H_z can underflow and fail, even though each input was finite. |
| Stored config | Diagnostics validate the actual stored floats. DynamicsConfig may already have coerced a raw construction input; diagnostics do not reconstruct that prior input type. Invalid mutated stored values are rejected. |
| Manual records | Frozen storage does not enforce formula identities or all domain relations; use the validated function path to obtain a normal diagnostic result. |

**WITNESSES.** quadratic_form rejects direct magnitudes 10²⁰⁰ and 10⁻²⁰⁰ through overflow/underflow. The potential fails at state scale 10¹⁰⁰; area accounting can fail through quartic underflow at scale 10⁻¹⁰⁰. A staged readout for Ω=(10¹⁰⁰,i10¹⁰⁰,0) can be finite while its readout accounting fails when squaring the large chiral contribution. These are domain distinctions, not edits or proposed repairs.

External high-precision comparisons use exact binary inputs and independently calculated expressions, with stated fixture-specific scale-based allowances. They are not universal numerical error theorems. [NUM; DIAG; TEST; ORACLE]

## 11. Current runner: which diagnostics, which sampled state

**SOURCE.** RUN exposes exactly these diagnostic selections:

| Selection | Evaluated from |
|---|---|
| chiral_area_accounting | Each sampled Ω |
| intensity_budget | Each sampled Ω and the native recurrence parameters |
| potential | Each sampled Ω and the native recurrence parameters |
| readout_accounting | Each selected observer's readout at that sample, with that observer's α,β |
| historical_alignment | Each selected observer's M,C,T at that sample |

The last two require selected observers. Raw z_chiral is a separate readout selection. Standalone quadratic_form and direct/cylinder/torus display helpers are not runner-owned diagnostic selections. Version 1 rejects ring observations/readouts/diagnostics; this audit concerns the triad.

RUN samples the initial state, including its requested observer initialization convention. On each update it computes the new canonical Ω, advances each observer's clock and EMA memory as applicable, obtains its readout, then computes requested diagnostics for that sample. With updates=n it records n+1 samples, as established in A06.

An intensity budget stored at index n predicts forward from **Ω_n**. It is not automatically the residual of the transition Ω_(n−1)→Ω_n. The runner test compares it with a direct budget of each stored state.

**WITNESS.** Enabling the five diagnostics and a staged observer preserves the encoded Ω sample sequence bit-for-bit against the bare run in the bounded check. Instrumentation records diagnostics at the initial sample and after the newly advanced state.

**Failure boundary.** A requested diagnostic may raise during initial sampling or a later _sample call. The exception propagates, the requested run returns no completed RunRecord, and ordinary caller inputs remain unchanged. A canonical recurrence update may already have been computed locally before a later-sample diagnostic fails; passivity does not mean the failed request returns that partial work. At zero updates, a tiny finite Ω can be recorded without diagnostics while requested intensity_budget fails its numerical domain.

The existing record loader does not recompute or repair diagnostic numbers on load. Stored results remain reported data rather than a new state authority. [RUN; RECORDS; RUN_TEST]

## 12. Claim-to-proof/check map and reproducibility

### 12.1 Coverage and bounded results

| Claim family | Proof / source | Independent checks and current tests |
|---|---|---|
| Full norm/Q expansions; residual limitations | §2; E (18)–(20); DIAG | full_euclidean_blend, full_signed_Q_blend_including_QM; four manually supplied exact records; TEST/P10 |
| Cancellation and triangle bounds | §2.3; E Proposition 8 | Two symbolic bound slack identities; valid pointwise EMA cancellation |
| Gram/slack/sharp equality/raw scale | §3; E (16)–(17) | Polynomial identities, zero/nonzero equality family, every Gram field on a dyadic state |
| Resolution and directional sensitivity | §4; E (21),(23) | Symbolic normalization Jacobian; below/equal/above threshold and tiny-parallel witnesses |
| Finite-step budget and exact remainder | §5; E (33)–(36) | Hermitian graph identity, full budget/remainder expansion, all budget fields on signed dyadic inputs |
| Overshoot and gradient limitation | §§5–6; E (37)–(38) | g=0 exact witness; six gradient components; pure-coupling and phase-stage counterexamples |
| Potential normalization constant | §6 | Completed-square algebra; actual DP/E normalization inspection; no unsupported earlier-document attribution |
| Direct and cylinder semantics | §7 | Key/fallback/malformed/empty/copy cases; custom N and κ=0 |
| Torus bounds, inverse and history dependence | §8; E (25),(27) | Strict gaps; meridional identity; high-precision forward fixtures; conditional inverse; metadata and endpoint rounding |
| Information loss | §9; E (28) | Equal κ,z,M but different C,T; matched scalar displays; κ=0 distinctions |
| Passivity and failure propagation | §§10–11; DIAG/RUN | Patched forbidden calls, byte preservation, import/call inspection, record failure witnesses, focused runner tests |
| Protected-source preservation | §13 | Full before/after inventories, Git identity/status, Papers A–F subset and prior external artifact hashes |

The checker derives symbolic expectations before calling current implementations. It does not execute historical or production modules or use implementation outputs to define its symbolic identities.

All **160** final predicates passed, including the optional integrity comparison:

| Group | Passed |
|---|---:|
| EXACT_ALGEBRA | 25 |
| EXACT_BOUNDS | 10 |
| EXACT_FALSIFIER | 9 |
| API/PRECISION | 46 |
| DISPLAY/INFORMATION_LOSS | 39 |
| OWNERSHIP | 18 |
| INTEGRITY | 13 |

These are grouped predicates, some covering vectors or record fields. They are not a fabricated count of individually independent theorems. The JSON preserves each predicate and its evidence.

### 12.2 Focused repository tests and runtime caveat

Actual selection:

- All 36 tests in test_z_diagnostics.py.
- All five P10Tests methods in test_parity_p09_p10.py.
- P9Tests.test_constructor_zero_and_bitwise_passivity.
- Seven RunnerRecordTests methods: test_zero_updates_has_one_row_and_no_advancement; test_exact_schedule_new_omega_then_clock_then_ema_then_observe; test_observer_and_diagnostic_selection_cannot_change_trajectory; test_intensity_budget_is_from_each_stored_state; test_abort_on_numeric_failure_preserves_inputs; test_bad_requests_are_rejected_before_execution; test_diagnostic_numbers_are_not_recomputed_or_repaired_on_load.

Each of the two identical focused selections reported **49 passed tests and 13 passed subtests**, exit code zero. No collected test was deselected within those explicit selections; other P9/runner methods and unrelated suites were not requested. There was no archive verifier, old integrated kernel run, paper rebuild, or broad historical workflow.

**OPEN — runtime anomaly.** Both focused receipts also contain “Windows fatal exception: access violation” on stderr. An isolated run of TEST's test_runtime_import_and_call_boundary reported **one passed test**, exit zero, and reproduced the stderr messages while waiting on its import-check subprocess. Some traces also referenced SymPy. This localizes one reproducible setting but does not establish the root cause or assign it to the mathematical kernel. The isolated test is a repeat of an already counted test, not an extra new passing test.

All receipts are retained in the results, including stderr. Overall status is **PASS_WITH_RUNTIME_CAVEAT** rather than an unqualified clean-runtime certification. This scientific reconstruction neither suppresses the messages nor changes scientific source, dependencies, or numeric policy to obtain a cleaner result. The isolated test used pytest's visible-output option; its exact command is retained.

### 12.3 Checker interface and Windows CMD commands

**SOURCE / WITNESS.** The new checker requires --output and --scratch. Both are validated as outside all protected trees. It rejects an existing output before running its audit and opens a new result with exclusive-create mode. Its source location does not determine output location; --repo is explicit or discovered from source ancestors. The final run was executed from a byte-identical copy in a separate external directory with the checker file's read-only attribute set, while writing the explicitly selected external results path. This verifies source/output location separation without placing a file in the protected repository. The same interface permits later read-only repository execution.

Optional --integrity-dir and --test-receipt supply external evidence; neither is conflated with the scientific checks. Without inventories the result explicitly records INTEGRITY as NOT_REQUESTED. The companion result for this execution includes them. Interface guards verified missing-output rejection, protected-output rejection, and existing-result preservation.

The following commands use Windows CMD syntax. Choose a **new** output filename on each run; the delivered result is not a default overwrite target.

~~~bat
conda activate torment
set PYTHONDONTWRITEBYTECODE=1
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
set "ATLAS07_SCRATCH=%TEMP%\trioctagon_atlas07_recheck"
set "MPLCONFIGDIR=%ATLAS07_SCRATCH%\mpl"
set "XDG_CACHE_HOME=%ATLAS07_SCRATCH%\cache"
python -B -X utf8 "C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_07_EXACT_CHECKS.py" ^
  --repo "C:\TORMENT\TRIOCTAGON_new\trioctagon-physics" ^
  --scratch "%ATLAS07_SCRATCH%" ^
  --output "%ATLAS07_SCRATCH%\new_results_01.json"
~~~

The scientific run above does not invent fresh integrity evidence. To include this execution's preserved evidence, additionally pass --integrity-dir with the external evidence directory in the results JSON and --test-receipt with its focused receipt. Reusing old inventories is documentary replay, not a new filesystem capture.

The exact pytest command and all node selections are stored in each test receipt. A minimal focused diagnostic rerun is:

~~~bat
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
python -B -X utf8 -m pytest -q -p no:cacheprovider ^
  --basetemp "%ATLAS07_SCRATCH%\pytest_new_run" ^
  kernel_physics/tests/test_z_diagnostics.py ^
  kernel_physics/tests/test_parity_p09_p10.py::P10Tests
~~~

The recorded full selection additionally includes the one P9 and seven runner nodes listed above. Scratch/temp/cache paths for this execution were external and bytecode writing disabled.

**A06 packaging constraint, not scientific failure.** Atlas-06's checker remains unchanged. It binds results to its own directory and requires external execution there. That is a later packaging constraint if it is ever moved into protected source. Atlas 07's output interface avoids that coupling; no retrofit to Atlas 06 is performed.

## 13. Integrity, scope limits and next-entry boundary

All deliverables are outside the protected trees. The established fingerprint method includes every regular file, including ignored/untracked content, except paths with a .git component. It hashes file bytes with SHA-256, then hashes the sorted-key compact JSON map from relative POSIX paths to file hashes. Before/after comparisons use the full maps, not just Git tracked status.

These are sequential path/content inventories, not atomic snapshots. They do not certify timestamps, ACLs, empty directories, separate symlink metadata, or .git administrative bytes. Git HEAD and tracked status are captured separately. Existing untracked content is preserved; empty tracked status does not imply an empty untracked inventory.

| Protected scope | Before = after files | Identical before/after tree SHA-256 |
|---|---:|---|
| Current repository | 7,803 | eb913f8b685be59b18ed9cbf1656b06e3d7dcb617b6579e3ec60fc27753dc1df |
| Old kernel_TO | 401 | cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd |
| Production kernel subset | 64 | 8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41 |
| Whole production torment_fabric checkout | 173,908 | 3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4 |

The production subset is also contained in the whole-checkout inventory. Papers A–F are checked explicitly as a subset of the current-repository file map. Prior external Atlas-01–06 artifacts are hash-checked separately. The final JSON records scan intervals, before/after hashes and differences, evidence-file hashes and Git identities.

The next entry is not selected or started by this packet. Remaining current-kernel interfaces can be assigned by a subsequent work order; global Atlas synthesis and companion papers A_1, B_1, etc. remain deferred. Physical interpretations, inverse recovery of unrecorded Ω from a scalar display, old viewers, and unresolved harmonic provenance are not silently promoted into new authority.

### Source fingerprints

These hashes bind the inspected source packet and the checker receipt; no paper is rebuilt.

| Source ID | SHA-256 |
|---|---|
| DIAG | db6c5d87fcecd492ac76fbc3cbcd6b71520d2ab4c9bbe4b1686c138aa0549d09 |
| TEST | b5b4ae0eb43b1c4c0e1b2f919328540f5a74e7930c713766062bb9441935ee3e |
| E | a79bc29d991c3af8bba546f0bc5e1ff7a6bbe5501d8adf2ef6d19c66b362978d |
| Z | 97ebdbb37103e736d2ae86c272541c458a5b585e1889e6d14ff056b316494f4f |
| C | 3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9 |
| D | ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4 |
| NUM | cc33f797e76f7dbeff6fbd58ab52003fde2acbadf35ae299d827b4b55ba29655 |
| RUN | 3a9f3ce718b1600f445bf963b968b9dbb3c41b03e6f2acf15239e2ae1512bcf6 |
| RECORDS | aa82d39cfc92a9d8f58ffd87342186ddf67134c4590f41e475327f0396bb5785 |
| RUN_TEST | 2b95ca7f03b0942739e3f511b729f9e730c0a8a22c65809f7ddb9508f64b3e0e |
| P9_P10 | 081dfa0c3a69b69a170bcc6b2a3dcf61728c8d3b7155d2dd6942b1751eb7b648 |
| ORACLE | 6b70279fa402c2ddb49aa0de89f68def34abdd3d5b47886897f700b39d4aa2f0 |
| SYMBOLIC | 674e4cb7cad70825ca01a0a7bb390876f41996cd148849fa51e663b784ff87df |
| SYMBOLIC_RECEIPT | 265e250d69fd6e17176d9eeaf2b43a03e72f72fcbe28fdf3c1e8f7a24d3ff0d2 |
| E_REVISION | ca704891214c87bce57bb27516dc8e9e04eed1ae47f7cd9255650e72f8e5876a |
| D_POTENTIAL | 7bc87de09400ba1a37d5dc9ab7be38c9a978be31bb35ece56102d29ee2e5d25b |
| A04 | f9138ae3e0f0369b8adde82ef35314c6024437bbdd2dab45dd5e9cbe1dd82e8d |
| A01 | c4604b5311893850bdd2392c068e6e366085ce2c7be7a04537d18d6eea007c95 |
| A06 external packet | 2aca9d099ca21005f87980108a55eb09b2f7a32e26898a3065ed3abd5bf2a5bf |
| New Atlas-07 checker | 2752624a079d0934dc848825ff6f428351e7e45db38a5acbf2ef9b7dd27c8089 |

### Final integrity receipt

All four before/after file inventories match with no added, removed or content-changed paths.
Papers A–F: 5001 files unchanged. Prior external Atlas-01–06 artifacts: 16 files unchanged.
Current and production Git HEAD/tracked status are unchanged. Current HEAD remains 34c21830e7e7c4b5f4a5a940d084c37feaf1f82c.
The complete external inventories and test/interface receipts are retained under [the evidence directory](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas07_20260929_917a4721ac).
Commits, pushes and publication are recorded actions of this execution, not deductions from file hashes.

~~~text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
PAPERS_A_F_CHANGED = NO
COMMITS = 0
PUSHES = 0
ATLAS_07_PUBLISHED = NO
~~~

The Windows stderr anomaly remains OPEN as described in §12. It does not alter the measured file-integrity result. No source or environment repair was attempted.
