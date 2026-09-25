# Two-seed transverse-axis falsification

**RESEARCH_TRANSVERSE_AXIS_FALSIFICATION_v0.1 — 25 September 2026**

Scientific lead: GPT. Author: Hilmir Frímann Halldórsson. Implementation, independent algebra and numerical verification: Codex. **Status: bounded research packet for GPT review; no new acceptance claimed.**

GPT's exact decomposition of the historical seed is verified. Its phase-rotated tangent perturbation already encodes the projective \((-1,-1,2)\) chirality axis. This identifies an initial-state explanation that the preceding Codex packet had not isolated; it does not make that historical seed near-synchronized or prove its complete nonlinear asymptotics.

Exactly **two new trajectories**, with **eight accepted recurrence updates each**, were run. Row zero plus eight updates gives **9 rows per seed, 18 rows total**. Their chirality axes remain **90 degrees apart at every row**. Seed A's maximum own-axis drift is \(1.1785113164\times10^{-8}\) radians; seed B's measured drift is zero. Both match the pre-run analysis. The minimum chirality norm is \(1.1351167546\times10^{-6}\).

These particular seeds have stronger symmetry protection than generic transverse perturbations. Their exact chirality axes remain orthogonal whenever nonzero; the experiment verifies that the accepted implementation respects that prediction over the authorized eight updates. Rapid collapse onto one universal axis is not observed and cannot be universal across these seeds. The result does not establish generic nonlinear behavior away from their invariant subspaces.

## 1. Authority, inputs and execution boundary

The authoritative checkout is
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`,
on `main` at
`d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`,
tree `e9e7501fdb8c2942862943fc6cc529c12a5b4fa2`.

The existing interpreter,
`C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe`,
was invoked through Windows CMD with `-B -X utf8`. No dependency installation or new environment was used. No applicable AGENTS.md was found in the relevant ancestor, research or source directories. No index lock was present.

The new script imports the authoritative `kernel_physics/dynamics.py` and `kernel_physics/readouts.py`, with exact import-path assertions. It does not import geometry, observers, clock, lock, EMA, previous research runners, UI or historical restoration machinery. Previous packet receipts were read for provenance and preservation, without using gate geometry in this investigation.

The only evolution configuration was
\[
\epsilon=0.05,\quad g=0.2,\quad k=(1,1,1),\quad
\lambda_{\rm phase}=0.
\]
No forcing term was introduced. The accepted `step3` is unchanged. Its internal synchronizer takes the existing zero-strength early return; no phase extraction or synchronization reconstruction is performed in that branch.

The derivation and allowances were saved **before** the first update. A persistent run guard was saved before evolution and prevents any replay, including replay after a partial failure. Every accepted step's input/output state hashes and full output state were recorded. Runtime profiling counted exactly **16 `step3`**, **16 `_advance`** and **16 `phase_sync`** entries. The latter two are nested calls inside those same 16 updates, not additional trajectories.

All subsequent analysis and tests used the saved rows or symbolic algebra. The independent source-residual check evaluates the polynomial at each recorded input without feeding any result forward and without calling an evolution API. No historical trajectory was rerun.

## 2. GPT's exact historical-seed finding, independently verified

**Attribution:** this decomposition was supplied in GPT's present work order. The calculations below independently verify it. It is distinct from Codex's preceding local-degeneracy and plane-tendency conclusions.

For
\[
\Omega_0=(1/5+3i/10,\ -2/5+i/10,\ 1/10-i/5)^T,\qquad e=(1,1,1)^T,
\]
direct summation gives
\[
w=\frac{-1+2i}{30},\qquad |w|=\frac{\sqrt5}{30}.
\]
The exact common phase rotation making the mean positive real is
\[
Q=\frac{\bar w}{|w|}=\frac{-1-2i}{\sqrt5}.
\]
Writing \(Q\Omega_0=|w|e+\tilde\xi+i\tilde\eta\), exact rational/radical arithmetic gives
\[
\tilde\xi=\sqrt5(7/150,\ 13/150,\ -2/15)^T,
\qquad
\tilde\eta=\frac{7\sqrt5}{50}(-1,1,0)^T.
\]
Both vectors have sum zero. A common complex phase preserves the real/imaginary cross product, so
\[
\begin{aligned}
C
&=|w|e\times\tilde\eta+\tilde\xi\times\tilde\eta\\
&=\underbrace{\frac7{300}(-1,-1,2)^T}_{\text{first-order transverse term}}
+\underbrace{\frac7{75}(1,1,1)^T}_{\text{quadratic e-parallel term}}\\
&=(7/100,\ 7/100,\ 7/50)^T.
\end{aligned}
\]

“First-order” and “quadratic” classify terms in the relative-synchronization expansion with fixed mean; they do not assert dominance in this historical initial state. In fact,
\[
\frac{\sqrt{\|\tilde\xi\|^2+\|\tilde\eta\|^2}}{\sqrt3|w|}
=2\sqrt5\approx4.4721.
\]
The historical seed is not a small perturbation of its mean. Nonetheless its tangent part points **exactly** along \((-1,1,0)\), whose cross product with e is the historically observed comparison axis \((-1,-1,2)\). No universal nonlinear selector is needed merely to explain why that axis is already available in the seed.

This sharpens the earlier interpretation without rewriting its evidence: the seed's **phase-rotated tangent part**, rather than its unrotated imaginary component, supplies the exact axis. The previously measured small late offset and any finite-amplitude changes during the original nonlinear transient are not erased by this decomposition.

## 3. Prediction derived before evolution

The authorized states are
\[
\Omega_A(0)=e+ihv_A,\qquad \Omega_B(0)=e+ihv_B,\qquad h=10^{-3},
\]
\[
v_A=(1,-1,0)^T/\sqrt2,\qquad
v_B=(1,1,-2)^T/\sqrt6.
\]
They are normalized, orthogonal, and transverse to e. Their initial means equal 1.

At \(w=1\), the phase-like transverse factor is exactly
\[
A_t=1+\epsilon(k-|w|^2)-3g=\frac25.
\]
Thus the first-order predictions are
\[
\eta_n=(2/5)^n\eta_0+O(h^3),\qquad
\|C_n\|=\sqrt3\,h(2/5)^n+O(h^3)
\]
for each fixed bounded n as \(h\to0\). These are expansions, not exact finite-amplitude equalities. The componentwise real map respects complex conjugation, giving the indicated odd/even small-h structure.

On \(e^\perp\),
\[
e\times(e\times v)=-3v,\qquad \|e\times v\|=\sqrt3\|v\|.
\]
Hence \(v\mapsto e\times v\) is a scaled 90-degree rotation of that plane. The initial **oriented** unit chirality vectors are
\[
\widehat C_A(0)=(1,1,-2)^T/\sqrt6,\qquad
\widehat C_B(0)=(-1,1,0)^T/\sqrt2.
\]
Their projective axes are orthogonal. The sign choice does not change a projective axis.

### Exact one-step finite-amplitude correction

For any real transverse v and initial state \(e+ihv\), let \(v^{\circ j}\) denote componentwise powers, \(a=2/5\), and \(\epsilon=1/20\). One symbolic application of the source formula gives
\[
x_1=e-\epsilon h^2v^{\circ2},\qquad
y_1=ahv-\epsilon h^3v^{\circ3},
\]
so exactly
\[
C_1=ah\,e\times v
-\epsilon h^3\big[e\times v^{\circ3}
                  +a(v^{\circ2}\times v)\big]
+\epsilon^2h^5(v^{\circ2}\times v^{\circ3}).
\]
For a nonzero leading chirality this gives an \(O(h^2)\) normalized/projective correction unless its directional coefficient cancels.

For seed A, write
\[
Y=h(2/5-h^2/40)/\sqrt2.
\]
Then
\[
C_A(1)=Y(1,1,-2+h^2/20)^T.
\]
Its exact acute angle from its initial axis is
\[
\theta_A(1)=
\arctan\frac{\sqrt2\,h^2}{20(6-h^2/10)}
=\frac{\sqrt2}{120}h^2+O(h^4).
\]
At the authorized h this is
\[
1.1785113216194345\ldots\times10^{-8}\ {\rm rad}.
\]
This correction was derived before running, not fitted to the output.

For seed B, the first two complex components remain equal. Its C direction therefore remains exactly parallel to \((-1,1,0)\) while C is nonzero. All directional orders cancel for that invariant subspace, even though its magnitude has finite-amplitude corrections.

## 4. Exact symmetry makes this pair especially informative—and limited

With real symmetric coefficients and phase strength zero, the accepted polynomial map commutes with channel permutations and complex conjugation.

Seed A lies in
\[
\Omega_A=(x+iy,\ x-iy,\ z),\qquad x,y,z\in\mathbb R.
\]
This form is preserved, because it is fixed by channel swap 1↔2 followed by conjugation. Its chirality is
\[
C_A=y(z,z,-2x).
\]
Seed B lies in
\[
\Omega_B=(a+ib,\ a+ib,\ c+id),\qquad a,b,c,d\in\mathbb R,
\]
and equality of the first two channels is preserved. Its chirality is
\[
C_B=(ad-cb,\ cb-ad,\ 0).
\]
Consequently
\[
\boxed{C_A\cdot C_B=0}
\]
exactly, independently of their finite amplitudes, whenever the two states remain in these invariant subspaces. If both C vectors are nonzero, their projective angle is exactly \(\pi/2\).

Thus the eight-step experiment is not an unconstrained test of a generic pair of perturbations. It is a clean counterexample to an unrestricted rapid-universal-axis claim, backed by a source symmetry theorem, and an implementation check of that theorem. It cannot rule out additional behavior on generic initial conditions outside these subspaces or on other parameters/time ranges.

The optional permutation cross-check needs no third trajectory. For a permutation matrix P,
\[
F(P\Omega)=PF(\Omega),\qquad C(P\Omega)=\det(P)\,PC(\Omega).
\]
Chirality is an axial vector under an odd permutation. A common channel permutation preserves the mutual orthogonality and gives permuted projective axes. Only this algebraic covariance was checked; no permuted seed was run.

## 5. Pre-run finite-amplitude and arithmetic allowances

The ideal real-arithmetic bounds below were saved before the experiment. They are intentionally conservative and are not adjusted to the observed drift.

### Positive norm bounds through eight updates

Let \(h=10^{-3}\), \(x_{\min}=1-3h^2\), and write each component's real/imaginary parts as x,y. For rows 0–8 a containing box is
\[
x_{\min}\le x_j\le1,\qquad |y_j|\le2h.
\]
The real update is increasing in each real component in this box. At the lower corner,
\(1-x_{\min}^2-4h^2=2h^2-9h^4>0\); at the upper real corner the amplitude correction is nonpositive. For the imaginary update write
\[
f_j=0.4+0.05(1-x_j^2-y_j^2),\qquad
f_{\min}=0.4-0.2h^2,\quad f_{\max}=0.4+0.3h^2.
\]
The corresponding linear mixing of the current imaginary components has nonnegative entries and row sums at most \(f_{\max}+0.6=1+0.3h^2\). The initial maximum imaginary component times this factor to the eighth power is below \(0.000816499<2h\). This closes the finite-horizon box argument.

For A, \(y_{n+1}=f_1y_n\) and
\(\|C_A\|\ge\sqrt6\,x_{\min}|y|\), giving
\[
\|C_A(n)\|\ge\sqrt3\,h\,x_{\min}f_{\min}^8
>1.1351088714\times10^{-6}\qquad(0\le n\le8).
\]
For B, the two distinct channel values evolve through a real 2×2 mixing matrix with determinant
\[
(f_1+2g)(f_3+g)-2g^2=f_1f_3+gf_1+2gf_3
\ge f_{\min}^2+0.6f_{\min}.
\]
The real/imaginary area, hence C, is multiplied by that positive determinant. Therefore
\[
\|C_B(n)\|\ge\sqrt3\,h(f_{\min}^2+0.6f_{\min})^8
>1.1351104606\times10^{-6}.
\]
These lower bounds show that the exact chosen chirality vectors cannot vanish in the authorized window.

For A a tighter box is \(1-h^2\le x,z\le1\), with
\(|y_n|\le(h/\sqrt2)0.401^n\).
Writing \(d_n=z_n-x_n\), the exact recurrence gives
\[
d_{n+1}=
[0.45-0.05(z_n^2+z_nx_n+x_n^2)]d_n+0.05x_ny_n^2.
\]
The bracket is nonnegative and below .301. Since \(d_0=0\),
\[
0\le d_n\le .025h^2
\sum_{j=0}^{n-1}.301^{n-1-j}.401^{2j}\le .025h^2.
\]
The final inequality follows from \(.301+.401^2<1\), by comparison with its binomial expansion. The transverse projection of \(C_A\) stays on its initial axis, and
\[
\tan\theta_A(n)=\frac{\sqrt2\,d_n}{z_n+2x_n}.
\]
Thus a pre-run bound for all eight updates is
\[
\theta_A(n)\le
\frac{\sqrt2\,h^2}{120(1-h^2)}
=1.1785124805\ldots\times10^{-8}\ {\rm rad}.
\]
Seed B's exact directional drift and the mutual deviation from \(\pi/2\) are zero by symmetry.

### Arithmetic allowance and observed precision

For a deliberately conservative engineering allowance, the packet uses binary64 \(u=2^{-53}\), initial component error at most \(2uh\), local absolute component error budget \(128u\), and six-real-component infinity-norm Lipschitz factor 1.01 on a slightly expanded version of the above box. The derivative row sums there are below 1.01. This gives
\[
E_{\rm state}\le 2uh(1.01)^8+128u\sum_{j=0}^7(1.01)^j
=1.1774670103\ldots\times10^{-13}.
\]
A componentwise cross-product budget is
\[
E_{\rm component}\le2[(1+2h)E_{\rm state}+E_{\rm state}^2]
+32u(1+E_{\rm state})(2h+E_{\rm state}),
\]
and \(E_C\le\sqrt3 E_{\rm component}\).
Using twice \(E_C\) divided by the smaller ideal norm lower bound gives a per-axis allowance
\(7.2013289214\times10^{-7}\) rad, and mutual allowance
\(1.4402657843\times10^{-6}\) rad.

The local \(128u\) budget assumes ordinary finite normal binary64 evaluation of the short NumPy expression, including magnitude evaluation and coefficient rounding. It is a conservative engineering budget, **not an interval-certified proof of a NumPy/libm implementation**. It is much looser than the measured drift, and overwhelmingly smaller than a 90-degree axis separation. No observed value was used to fit these allowances.

The saved-input 80-digit polynomial residuals use the exact dyadic values of the stored binary64 inputs and coefficients. Their maximum complex-component discrepancy is \(8.9837080672\times10^{-17}\), below the chosen local budget. This is independent residual evaluation, not an independently integrated trajectory.

For interpreting each stored C direction, the CSV/JSON also give the local cross-product roundoff proxy
\[
32u\,\operatorname{hypot}(
 |x_2y_3|+|x_3y_2|,\,
 |x_3y_1|+|x_1y_3|,\,
 |x_1y_2|+|x_2y_1|).
\]
A direction is marked numerically usable when its norm is positive and more than 1000 times this proxy. All 18 pass by margins above \(2.5\times10^{14}\). This diagnostic excludes accumulated state uncertainty; it is not a physical criterion.

The old \(10^{-12}\) threshold plays **no role** in validity or classification. The files only report the ratio to that number as a familiar scale reference. The actual minimum C norm exceeds it by about 1.135 million.

## 6. Actual bounded results

| Row | A C norm | B C norm | A own-axis drift rad | B own-axis drift rad | Mutual angle deg | A plane residual |
|---|---|---|---|---|---|---|
| 0 | 0.00173205080757 | 0.00173205080757 | 0 | 0 | 90 | 0 |
| 1 | 0.000692820268179 | 0.000692820268179 | 1.1785113164e-08 | 0 | 90 | 1.17851132071e-08 |
| 2 | 0.000277128105955 | 0.000277128105955 | 5.4211518935e-09 | 0 | 90 | 5.42115186835e-09 |
| 3 | 0.000110851242949 | 0.000110851242949 | 1.92804443759e-09 | 0 | 90 | 1.92804442797e-09 |
| 4 | 4.43404974338e-05 | 4.43404974338e-05 | 6.26685133589e-10 | 0 | 90 | 6.26685136287e-10 |
| 5 | 1.77361990662e-05 | 1.77361990662e-05 | 1.95728981946e-10 | 0 | 90 | 1.95729033892e-10 |
| 6 | 7.09447965968e-06 | 7.09447965968e-06 | 5.99545038965e-11 | 0 | 90 | 5.99544681752e-11 |
| 7 | 2.83779187579e-06 | 2.83779187579e-06 | 1.81839734736e-11 | 0 | 90 | 1.81840158756e-11 |
| 8 | 1.1351167546e-06 | 1.1351167546e-06 | 5.4868451061e-12 | 0 | 90 | 5.48680347406e-12 |

Angles in the table are radians except the mutual angle column. The full complex Omega, mean, relative synchronization distance, raw and unit C, signed plane residual, plane angle, own/other initial-axis angles, mutual angle and numerical diagnostics are retained for every row in both CSV and JSON.

The minimum norms, both at row 8, are:

- A: \(1.1351167545977547\times10^{-6}\).
- B: \(1.1351167545977540\times10^{-6}\).

The row-8 norm divided by the linear prediction \(\sqrt3h(0.4)^8\) is 0.9999999448069271 for A and 0.9999999448069266 for B. This small finite-amplitude difference from unity is consistent with the expansion; it is not evidence for a universal direction selector.

Seed A reaches its maximum own-axis drift at row 1:
\[
1.1785113163961323\times10^{-8}\ {\rm rad},
\]
versus the exact pre-run one-step value
\(1.1785113216194345\ldots\times10^{-8}\) rad. Its plane angle agrees at the expected floating precision. Seed B's own-axis drift and plane residual are stored zero throughout.

Both source symmetry residuals are stored zero at every row. The computed mutual projective angle is the same binary64 value \(\pi/2=1.5707963267948966\) throughout. Stored zeros alone are not general exact-zero proofs; here the separate symbolic symmetry argument supplies the exact ideal-real result.

**Falsification disposition:** the simple local interpretation survives this bounded test. Rapid universal-axis collapse is challenged by two distinct, nonvanishing, orthogonal chirality axes throughout the authorized window. The chosen seeds' exact invariant subspaces make this an especially controlled counterexample, not statistical evidence about generic initial states. No nonlinear-selection investigation or additional run is initiated.

## 7. Verification and preservation receipt

**20/20 new tests passed**, with discovered, executed and successful IDs identical. The full IDs, raw test output and final code/test hashes are in `TRANSVERSE_AXIS_FALSIFICATION_RESULTS.json`. Tests performed no model updates. They verify:

- the exact historical decomposition, source symmetries and one-step expansion;
- the two-seed/16-update trace and saved state hash chains;
- the pre-run prediction timestamp and exact authorized configuration;
- all 18 rows, initial axes, finite-amplitude predictions and prior allowances;
- source-polynomial residuals, raw chirality, masks and CSV values;
- permutation covariance without another trajectory;
- a single accepted-update call site and no unrelated imports.

All **64 protected identities** remain unchanged. The inventory extends the preceding 59 protected files with all five chiral-transverse outputs. It preserves the accepted source, previous research and reviews, paper evidence, local-only predecessor test files and continuity/provenance inputs. Original files were neither rewritten nor cleaned up.

HEAD, tree, branch and index remain at entry; tracked and staged diffs remain empty. All existing status entries are unchanged outside the five new research paths. No full predecessor suite, additional trajectory, parameter sweep or cleanup operation was run.

Only these five new persistent files were created in the existing research directory:

- `transverse_axis_falsification.py`
- `test_transverse_axis_falsification.py`
- `TRANSVERSE_AXIS_FALSIFICATION.csv`
- `TRANSVERSE_AXIS_FALSIFICATION_REPORT.md`
- `TRANSVERSE_AXIS_FALSIFICATION_RESULTS.json`

The JSON includes the full two trajectories, exact derivation, pre-run allowances, commands and outputs, per-update trace, source/path hashes, test evidence and pre/post preservation comparison. It hashes the four companions but not itself. Its external byte count and SHA-256 are supplied with delivery.

```
ACCEPTED_BASELINE = d0aa8d1cb19421ff441eacda0f83ec89fc3160b3
HISTORICAL_SEED_DECOMPOSITION = VERIFIED_EXACTLY_WITH_GPT_ATTRIBUTION
NEW_MODEL_TRAJECTORIES = 2
RECURRENCE_UPDATES_PER_TRAJECTORY = 8
TOTAL_ACCEPTED_STEP3_CALLS = 16
ROWS_PER_TRAJECTORY = 9
TOTAL_ROWS = 18
ADDITIONAL_MODEL_RUNS_IN_TESTS = 0
KERNEL_MODIFIED = NO
GATE_GEOMETRY_OR_Z_FEATURES_INVOLVED = NO
STAGE_COMMIT_PUSH = NO
DISPOSITION = STOP_FOR_GPT_REVIEW
```
