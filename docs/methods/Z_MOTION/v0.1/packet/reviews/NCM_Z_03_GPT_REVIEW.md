# NCM-Z-03 v0.1 — GPT scientific and package review

**Review date:** 1 November 2026  
**Disposition:** ACCEPTED within the bounded source-accounting scope. No blocking mathematical, data, or presentation correction found. This is not publication approval or a physical-motion identification.

## 1. What was reviewed

The submitted archive is `NCM_Z_03_v0.1_REVIEW.zip`, 4,771,959 bytes, SHA-256 `5d739cf1a06bcb8825af6738ae7b6d4733fc3a72ebb8031b62d61f5d8679efd0`.

The report, work order, mathematical brief, plan, calculation source, independent copy-only checker, source snapshots, numerical ledgers, primary-evaluation log, precision policy, preservation records, and three original figure sheets were reviewed. The five saved states and four adjacent spans remain the sole primary example. Its native coefficients are epsilon=1/10, g=1/5, phase strength=17/100, k=(2,3,4), distinct from the coherence-return paper's parameters and the first two-state Z example.

The global observer freeze is theta*=time*=0, alpha=1, beta=1/2, placement scale=1 and rotation=0. Observer literals retain their binary64 values; they were not replaced by mathematical constants. Here r=X−O denotes centered placed position, not native amplitude or physical particle position.

## 2. Main scientific assessment

The numerical account resolves the question asked: which existing native intensity and chirality terms account for the four frozen readout displacements? Its answer uses the admitted data without altering the underlying recurrence or inventing geometric motion.

The most useful distinction is that native intensity, a coordinate of the frozen readout, and distance from the placement center are different quantities. They can change in different directions. In particular, the saved 2→3 span increases native intensity while decreasing placed radius; 3→4 increases radius while decreasing height.

All four spans are included. There is no selected successful suffix, additional state, inferred continuous trajectory, or post-index-4 reconstruction. The retained figures use different panel scales with explicit labels and do not claim physical units or calibrated time.

## 3. Mathematical identities checked

### 3.1 Finite intensity accounting

For u=epsilon D Omega and v=g L Omega, the prestage is Omega+u+v, with both contributions evaluated at the same before-state. Expanding its squared norm gives

    Delta I_model = 2 epsilon sum_i(k_i s_i − s_i²)
                    − 2g sum_(i<j)|Omega_i−Omega_j|²
                    + ||u+v||².

The identity

    ||u+v||² = ||u||² + 2 Re(u†v) + ||v||²

expands the third parent term; those children must not be added again to the parent sum. The square is a genuine finite-step term, not numerical error. Phase multiplication preserves each prestage modulus, so its ideal intensity contribution is zero. That does not mean phase synchronization leaves the spatial readout unchanged.

The source API's reconstructed-prestage comparison is not confused with the independently supplied after-state: the report explicitly retains R_I=Delta I_saved−Delta I_model.

### 3.2 Chirality accounting

With S=xx^T+yy^T, A=xy^T−yx^T, and C=(A_23,A_31,A_12), the sign convention is consistent: Omega Omega†=S−iA and conjugate pair products have S+iA. The matrix expansion for M=Id+epsilon D+gL gives all five first, squared, and mixed amplitude terms.

The cofactor identity (Mx)×(My)=cof(M)(x×y) is polynomial and remains valid when M is singular. No inverse is needed. The pair rotation has the correct sign:

    A^+_ij = Atilde_ij cos(delta_j−delta_i)
             + Stilde_ij sin(delta_j−delta_i).

The two phase contributions are therefore Atilde(cos d−1) and Stilde sin d, entrywise. The code preserves the source Arg0 convention and the lambda=0 bypass. These seven contributions are an exact algebraic decomposition, not seven independent forces or intervention experiments. The phase terms depend on the already mixed prestage.

### 3.3 Carrying the budgets into frozen Z

At this freeze,

    r = K(kappa) H + C/2,
    K(kappa) = lambda_vp kappa/(1+kappa),
    H = cos(3 lock) (1,0,1).

For endpoint norms a,b with a+b>0,

    K(b)−K(a) = q (b²−a²),
    q = lambda_vp/[(a+b)(1+a)(1+b)].

This is an exact finite divided difference, not a first-order derivative. Multiplying the parent intensity terms by qH and the area terms by 1/2 produces the source-resolved displacement ledger. Model-to-data and readout arithmetic residuals are retained separately. Both-zero endpoint norms leave q undefined and Delta K=0; the report does not create a default value.

The transverse identities hold:

    Q Delta r = Q Delta C/2,
    Delta r_y = Delta C_y/2,
    Delta(r_x−r_z) = Delta(C_x−C_z)/2,

where Q projects perpendicular to H. Centered y is essential: absolute X_y includes O_y. The wording correction in the plan is appropriate and does not change any displacement.

### 3.4 Radial accounting

The fine radial ledger uses

    Delta ||r||² = (r_after+r_before) dot Delta r.

It is a linear allocation of the squared-radius difference across the existing displacement terms, not a classification of each term as an intrinsically inward/outward mechanism.

The separate coarse identity is

    ||r||² = K²||H||² + ||C||²/4 + K H dot C.

Its three endpoint differences describe macro magnitude, chiral magnitude, and the mixed term. The last term changes with both size and relative alignment; the figure's “cross alignment” label must not be read as an angle-only measurement.

The fine source split and coarse endpoint split answer different questions and must not be combined. Contribution norms do not form additive causal percentages. The ordinary-radius ledger follows by dividing by the sum of endpoint radii when it is nonzero.

## 4. What the four spans establish

| Span | Native intensity change | Frozen radius change | Interpretation within this example |
|---|---:|---:|---|
| 0→1 | −8.704703224 | −0.1041090293 | Strong initial decrease; the finite square is essential and the spatial terms partly cancel. |
| 1→2 | −0.0674033688 | −0.0172925288 | Smaller inputs and significant coordinate cancellation, especially in x. |
| 2→3 | +0.00754917595 | −0.000590475242 | Explicit numerical witness that intensity growth need not produce outward placed motion. |
| 3→4 | +0.08194667837 | +0.00780086538 | Macro growth exceeds the two opposing coarse radial terms, while height still falls. |

### First span

From I_0 approximately 9, onsite −5.203523014 and graph −10.25785089 alone would give a negative endpoint intensity. The positive finite square +6.756670678 restores the actual balance, leaving I_1 approximately 0.2952967756. Dropping the square is not an admissible exact description of this step.

### Middle balance

At 2→3, dropping the square would even reverse the predicted sign of the intensity change. In the full spatial balance the positive macro-size term +0.0009815887265 is exceeded by chiral-size −0.0003154152833 and cross-term −0.0009372451754.

The sum of absolute source-resolved radial contributions is approximately 223.885 times the magnitude of their net. This ratio depends on the specified decomposition. It is a cancellation diagnostic, not a percentage, condition certificate, number of independent effects, or evidence of equilibrium. The sign remains well separated from the numerical screening threshold.

### Final outward step

The coarse squared-radius balance is

    +0.009772971461 − 0.001044366176 − 0.005091184838
    = +0.003637420448.

The actual displacement is approximately

    (+0.0148015633, +0.02115268993, −0.00120391213).

Thus “outward” does not mean “upward.” The phase symmetric-pair contribution gives approximately +0.0144813 to the centered y change while contributing approximately −0.00478717 to the fine squared-radius sum. Its sign in one coordinate does not define its role in all directions.

### Additional explanatory inference from the retained values

The report already records I_1,I_2,I_3<0.3, whereas min k_i=2. Consequently each before-state component intensity after the first span lies below its own k_i. Its onsite intensity contribution 2 epsilon s_i(k_i−s_i) is then positive (nonnegative at a zero component). This explains why the aggregate onsite term promotes intensity growth in the last three spans. Meanwhile g>0 makes the first graph term nonpositive. This inference is from the displayed fixed coefficients, saved endpoint intensities and existing formula; it is not a new simulation or long-term conclusion.

## 5. Consistency is not full-state certification

The saved after-values agree numerically with the intensity and chirality budgets under the specified screen. These quantities, and frozen staged Z, discard common phase. Rephasing a saved after-state would leave those checks unchanged. Budget closure therefore does not independently establish every complex component of F(Omega_before)=Omega_after, nor reconstruct a hidden phase trajectory. The prior source admission and numerical status remain exactly as recorded.

The largest retained 120-digit saved-after residual is on the order of 1.27e−100, consistent with evaluating a history saved to about 100 significant digits. Neither that residual nor 80/120 agreement is an interval proof of exact evolution. It would be incorrect to call the result a new 120-digit native trajectory certificate.

The algebra establishes a sound observational explanation for these four spans. It does not establish gravity, energy emission, material motion, aperture passage, relaxation to an equilibrium, a periodic orbit, or the author's fixed-support/dual-arrangement interpretation. None of those ideas is rejected by this accounting either.

## 6. Verification actually performed by GPT

### Integrity and provenance

- The submitted archive matches the external receipt's byte count and SHA-256.
- All 83 manifest-listed payload files match sizes and hashes; the 84th archive member is the manifest. Names are unique and safe, the exact member set matches, and the CRC check passed.
- The separately attached report and plain-language summary match the archive byte-for-byte. The radial figure also matches. The uploaded intensity and transverse image previews have different bytes and smaller dimensions; review used the verified archived originals.
- The included Z-02 archive matches the earlier uploaded archive. The selected five-state file matches its original member exactly, including the stated SHA-256.
- The plan/frozen calculation-source hashes match. The primary log has exactly the declared eight evaluations: four saved pairs at each of two precisions.
- All twelve before/after original-file records are internally consistent, and the five delivered scientific source snapshots match their declared hashes. The live Windows originals were not inspected from this environment.

### Portable replay

The delivered copy-only checker was run unchanged in a new external sandbox directory with byte-identical ledgers and input. All 80 checks passed. Its complete parsed JSON result matched the submitted portable verification result exactly, including numerical strings.

This replay recalculated endpoint observables and checked retained ledger sums. It evaluated no native prestage, phase kick, complete update, additional observer schedule, or EMA memory. It is not a second Windows certification.

### Independent reviewer checks

A separate reviewer script passed 41 grouped checks: nine generic symbolic identities; 24 per-interval finite-gain, source-to-observation, radial, transverse, and cancellation checks; five qualitative sign predicates; and three source/preservation/check-log consistency predicates. The 1,851 submitted scalar-screen records were checked for internal arithmetic and pass-status consistency, not reproduced by rerunning their producer.

The primary `analyze.py` guard was respected: it was read, not imported or reexecuted. No new primary budget evaluations were performed. No historical checker/producer was run. The review added zero native states, zero successors, zero EMA updates, zero Git operations, zero model/application modifications and zero publications.

### Environment and figures

The replay used Linux, Python 3.13.5, mpmath 1.3.0 and SymPy 1.14.0. All three original archived PNG sheets were inspected directly. Parent/child hierarchy, sign labels, independent scales and units are visible; no material visual correction is required. The initially attempted all-attachment byte-equality check stopped on resampled PNG previews; archive-original comparisons resolved that intake assumption without altering scientific inputs.

## 7. Recommendation

Close the NCM-Z-03 source-accounting task at its agreed boundary. No repair work order is required.

Z-01, Z-02 and Z-03 now form a completed explanatory chain: existing state dependence, observer-versus-native comparison, and source-term accounting of the remaining displacement. A source-grounded synthesis of this chain is the proportionate next documentary step. It should reuse the existing proofs and retained evidence, separate inherited identities from new applications, and assess whether it belongs in an explanatory appendix/application guide or a focused methods note. It is not automatically a new standalone physical-research paper.

Do not extend this history or search for preferred motion merely to keep the sequence of tasks going. Any new scientific experiment needs a concrete unanswered question beyond the four transitions already accounted for. The author's wider geometry remains open, without asking for further intuition merely to complete this analysis.

## Source locations in the submitted archive

- `REPORT.md`, sections “Inherited native identities,” “Derived finite readout and radial bookkeeping,” the four span analyses, and “Verification, uncertainty and stopping boundary.”
- `START_HERE.md`, `NUMERIC_POLICY.json`, `PLAN.json`, `PLAN_FREEZE_RECEIPT.json`.
- `sources/kernel_physics/axial_observables.py`, `z_diagnostics.py`, `dynamics.py`, `readouts.py`; `sources/papers/PAPER_G/v0.1.1/source/paper_g.tex`.
- `STATE_SNAPSHOTS.json`, `NATIVE_INTENSITY_BUDGET.json`, `NATIVE_CHIRAL_BUDGET.json`, `FROZEN_Z_SOURCE_BUDGET.json`, `RADIAL_TRANSVERSE_ACCOUNTING.json`, `PASSIVE_PRESTAGES.json`.
- `CHECKS.json`, `PRIMARY_EVALUATIONS.jsonl`, `COUNTS.json`, `PORTABLE_VERIFICATION.json`, preservation and manifest files.

The accompanying GPT evidence ZIP contains the review scripts, hashes, copy-only replay results and independent-check results, not a rerun of the primary science.
