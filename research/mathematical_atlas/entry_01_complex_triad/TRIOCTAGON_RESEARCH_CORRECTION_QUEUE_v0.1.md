# TriOctagon research correction queue v0.1

Date: 2026-09-29. **Record only; nothing patched.** Frozen current baseline: `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`.

This queue distinguishes a demonstrated arithmetic/algebra error from a conflict among artifacts, an unjustified provenance claim, an interpretation, and a question requiring further evidence. Source identifiers, exact absolute paths and byte hashes are in [TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md>). A finding about an old document does not silently change current scientific definitions or parameters. All findings remain queued for a separately authorized review; none constitutes permission to modify the protected trees.

## Reciprocal asymmetry and theta-lock

### C01 — Scale invariance fails for the printed functional

**Classification: DEFINITE_MATH_ERROR.** S21 p. 6 Lemma 1; S11 lines 34–39 repeat the scale-invariant description.

For `θ(a,b)=abs(a/b−b/a)/sqrt(ab)` and `s>0`, direct substitution gives `θ(sa,sb)=θ(a,b)/s`. The printed proof correctly obtains the denominator `s sqrt(ab)` and then inserts an unjustified multiplicative s. The functional is homogeneous of degree −1, not zero. Symmetry under exchanging a and b remains true. Ratios of two such θ values can be invariant under a common scaling of all constants; that separate fact does not rescue the printed lemma.

### C02 — The φ,e value and claimed minimum ladder are incorrect

**Classification: DEFINITE_MATH_ERROR.** S21 pp. 3–4 and p. 6 Proposition 1.

Independent high-precision evaluation of the displayed definition gives the following order for the later stated set `{sqrt(3),φ,π,e}`:

| Pair | θ, rounded to 15 decimal places |
|---|---:|
| sqrt(3), φ | 0.081414604613593 |
| π, e | 0.099398803416665 |
| sqrt(3), e | 0.429623934379540 |
| φ, e | 0.517235406295468 |
| sqrt(3), π | 0.541210206288250 |
| φ, π | 0.632740741164980 |

Thus `θ(φ,e)≈0.244729` is incorrect for that formula. The three smallest pairs do not include φ,e: sqrt(3),e is smaller. The narrower inequality `θ(sqrt3,φ)<θ(π,e)<θ(φ,e)` is true, but does not imply that those are the three smallest. In the preliminary `{π,sqrt2,φ,e}` set, π,e already falsifies the claim that φ,e is the minimum.

### C03 — Constant-set and theta-lock semantics differ across sections/artifacts

**Classification: DOCUMENT_VERSION_CONFLICT.** S21 p. 3 starts with sqrt(2), while later sections use sqrt(3). S11 actually evaluates the formula for three selected pairs; it does not produce 0.244729 for φ,e.

The paper's chosen angular lock value and code's configured `theta_lock` must not be treated as a proven output of that formula. The code's normalized k triple is a separate construction using ratios. Preserve both definitions as encountered. Whether 0.244729 came from a different earlier formula, a fitted value or an arithmetic mistake beyond the printed calculation is unresolved; do not replace the live parameter with 0.517235.

### C04 — The Fibonacci/twelve-phase proof is invalid

**Classification: DEFINITE_MATH_ERROR.** S21 p. 7 Lemma 3 proof.

`φ=F_(n+1)/F_n` is not an exact finite-n identity. The printed `F_(n+1)^2−3F_n^2=(−1)^n` is false: at n=3 it gives `9−12=−3`, versus −1. The fixed number `sqrt(sqrt3*φ)` also cannot equal `1/12+O(φ^(−n))` as n grows. The resulting assertion that the fixed θ value tends to 1/12 does not follow. The numerical near-bound in the lemma happens to hold; its displayed proof does not.

### C05 — Correct closed form, inaccurate decimal expansion

**Classification: DEFINITE_MATH_ERROR.** S21 pp. 8–9.

The exact simplification `θ(sqrt3,φ)=1/(3^(3/4)φ^(7/2))` is correct. It equals `0.081414604613592925…`, not the printed `0.081412…`. Its distance from `1/12` is `0.001918728719740408…`. The printed interval `(0.08141,0.08142)` and bound `<0.00193` survive. Do not discard a correct algebraic identity because its numerical presentation is wrong.

### C06 — Numerical proximity does not derive twelve-fold or third-harmonic dynamics

**Classification: PROVENANCE_OVERCLAIM.** S21 p. 7 corollary and pp. 8–9 emergence wording.

A value about 2.3% from 1/12 does not by itself select a unique discrete rotational system, and no rule in this argument produces `sin(3(φ_j−φ_k))`. The later acknowledgement of a near-miss also conflicts with the earlier limiting argument. A new geometric construction could be studied separately, but cannot be retroactively supplied as historical provenance.

## Bounded Infinity: parameters, figures and singularities

### C07 — The declared classical parameters conflict with the figures and executable preset

**Classification: DOCUMENT_VERSION_CONFLICT.** S22 pp. 7, 11–13; Figures 1–2. S23 lines 122–134; S24; S26.

The text/caption declares `(A,B,C)=(9,1,1)`. Rendered figure legends label the classical curve `(9,9)`. The `classic` preset returns `(9,9,1)`, while its command-line help says `(9,1)`. The asymptote CSV uses `x^4−9x²+9`, confirming B=9 for that artifact. A later key-pairs CSV explicitly uses `(9,1,1)` and zero residues. These are different parameter cases, not interchangeable records. Author review must determine the intended association for each figure/table; this queue does not choose a replacement version.

### C08 — The declared (9,1) and (π,e) cases do not have real denominator poles

**Classification: DEFINITE_MATH_ERROR.** S22 pp. 6 and 11–13, claims about denominator roots/resonance boundaries near ±1.

For `D(x)=x⁴−Bx²+A`, set `y=x²`. The discriminant is `B²−4A`: −35 for (9,1), and `e²−4π≈−5.1773145154` for (π,e). Both are negative, hence no real denominator zeros. With C=1 their corresponding numerators also have no real zeros. In contrast, B=9 gives the real poles listed in S24: approximately ±1.070466 and ±2.802517 for f, and ±0.356822 and ±0.934172 for 1/f. Claims about the first pair of declared parameters cannot be justified using the different plotted pair.

### C09 — Finite-grid arc lengths across poles do not establish bounded improper lengths

**Classification: DEFINITE_MATH_ERROR.** S22 §§4.4–4.6, pp. 12–13; S24–S25.

At a noncancelled simple pole a, `f(x)~c/(x−a)`, so `sqrt(1+f'(x)^2)~abs(c)/(x−a)^2`; the improper arc length diverges. A finite sampled integration value is not evidence that this integral is finite. For the plotted (9,9,1) case, the reciprocal has poles *inside* the nominal |x|<1 chamber. The CSV's very large finite values (about 116983 on each outer f1 segment and 75661 on the inner g1 segment) do not prove regularization or finite confinement.

### C10 — Arc-length narrative and supplied numerical ratios require reconciliation

**Classification: DOCUMENT_VERSION_CONFLICT.** S22 p. 12, S25–S26.

The statement that outside segments dominate for both f and its reciprocal conflicts with S25's g1 row: inside ≈75660.52 versus outside total ≈10.20. For f2, the reported outer/inner ratio is approximately 5.416 in S25 and 5.405 in S26. The prose's “closer to unity” is comparative wording, not evidence of a near-one value. Different grids/parameter versions must be identified before figures and tables can support one quantitative conclusion.

### C11 — Reflective membranes and compressed infinity are interpretations of these plots

**Classification: INTERPRETATION_ONLY.** S22 Figure 2 caption and §4.6.

Taking a reciprocal maps zeros and poles algebraically; it does not supply a dynamical reflection law, boundary condition, or proof that divergence re-enters a bounded chamber. Preserve this as historical interpretive vocabulary unless an explicit mathematical/dynamical construction is supplied. This is distinct from the definite root and integral errors above.

## D24 lattice and 0.3/0.6/0.9

### C12 — Printed weighting formula does not produce its listed sequence

**Classification: DEFINITE_MATH_ERROR.** S27 Appendix C p. 24.

For `R(r)=η+(1−η)min(3,r)/3`, taking η=0.1 gives R(0..3) = `{0.1,0.4,0.7,1}`. It increases to saturation, whereas the text lists `{1,0.9,0.6,0.3}`. Even reversing its order gives `{1,0.7,0.4,0.1}`, not the printed sequence. No replacement formula is inferred.

### C13 — Arms, window counts and figure description disagree with the set definitions

**Classification: DEFINITE_MATH_ERROR.** S27 pp. 24–25, Figure 6.

With k running over all integers, each `A_j={ϑ0+(π/12)(k+8j) mod 2π}` is the same entire 24-node circle; the displayed sets do not partition it into three distinct arms. The defined union `W(r)` has counts `{3,9,15,21,24}` for r=0..4, obtained by enumerating `(s+8j) mod 24`. It does not have `{1,3,6,9,…}`. In particular, r=1 selects nine points, not the caption's three. The author may have intended other domains or a different counting convention, but those are not what is printed.

### C14 — The printed sequences are not derived by the displayed lattice argument

**Classification: PROVENANCE_OVERCLAIM.** S27 p. 25 interpretation.

The text claims the 1/3/6 and 1/.9/.6/.3 patterns follow directly from geometry, while the preceding formulas do not yield them and the weighting already introduces a saturation assumption. The 15° lattice and 120° separations are documented structural motifs. Neither the erroneous sequences nor that lattice establish the later H3 phase law.

## First harmonic, harmonic three and claimed derivation

### C15 — Three-phase averaging is not a third harmonic

**Classification: PROVENANCE_OVERCLAIM.** S16 p. 17 and p. 63 versus S14 pp. 2–3 and S08.

The water equation `(κ_Tri/3)Σ sin(θ_j−θ_k)` has harmonic one. Its 3 counts/normalizes three phases. The later `Σ sin(3(φ_j−φ_k))` multiplies a phase difference inside the sine. No source proving the exact replacement/design transition was recovered. Any historical account presenting the former equation as already deriving the latter needs correction. The water equation itself is not a mathematical error merely for using harmonic one.

### C16 — Two timing/normalization conventions remain unresolved

**Classification: NEEDS_REVIEW.** S16 p. 17 versus Appendix E pp. 73–74 and S17–S19; S14 eqs. (8),(13) versus S10/S01.

The water paper displays κ_Tri/3, while its appendix/companion code uses κ times the sine sum. A redefined κ could reconcile them, but an explicit identification was not established. Separately, the v3.9 printed update adds a difference evaluated at t to a phase at t+1; old/current kernel code extracts phases from the post-amplitude, pre-sync state. This may be schematic notation, or a different update order. Do not silently equate the versions. These ambiguities do not change the verified fact that the target harmonic is three.

### C17 — The historical pair-potential gradient misses a factor of three

**Classification: DEFINITE_MATH_ERROR.** S14 p. 5 eqs. (11)–(12).

For the printed `V=−λ/2 Σ_(k≠j) cos(3(φ_j−φ_k))`, direct differentiation gives `−∂V/∂φ_k=3λΣ_(j≠k)sin(3(φ_j−φ_k))`. Equation (12) omits the leading 3. The ordered sum and its 1/2 cancel double-counting; they do not cancel the chain-rule factor. No rescaling of λ is silently imposed, and the current implemented coefficient is not changed.

### C18 — A local phase-identification assumption is presented as geometric necessity

**Classification: PROVENANCE_OVERCLAIM.** S14 §11 p. 5; compare S05 §8.5, S06 C21, S07 and S04 line 51.

The historical section claims a unique derivation and no additional assumptions. It assumes `φ_k ~ φ_k+2π/3` independently for each oscillator and then selects a lowest Fourier mode. Three channels, their permutations, and common phase symmetry do not force that local identification: pair laws `sin(m d)` satisfy those symmetries for every integer m. Even an imposed 2π/3 pair periodicity allows all multiples of three. The full graph-coupled Ω map also does not generally have independent local Z3 rephasing symmetry. The paper documents a design argument, not a completed derivation from the earlier geometry. The exact historical selection remains OPEN.

### C19 — Amplitude preservation is narrower than preservation of full dynamics/readouts

**Classification: NEEDS_REVIEW.** S14 pp. 1–3, S15 lines 666–709, S32 p. 1.

The phase substep preserves each input amplitude exactly in ideal arithmetic. It changes Ω phases, so later graph/amplitude steps and phase-dependent chirality/readouts can change. Wording that all stability thresholds, cadence or underlying chirality/Z dynamics remain unchanged requires its actual parameter ranges, experiments and meaning of “unchanged.” Keeping an observable's definition unchanged is different from preserving its numerical values. Do not promote finite-run observations to a universal invariance theorem.

### C20 — Experiment-harness output alone is not evidence of the real kernel

**Classification: NEEDS_REVIEW.** S09 lines 401–415 and its ModelAdapter interface.

The supplied example main explicitly uses fake random dynamics for smoke testing; it does not apply the real kernel synchronizer. Its coherence formula is relevant documentary evidence. S14 p. 18 itself identifies this as an early exploratory harness and names the separate unified runner as its results entry point. The recovered runner S44 steps the model and calls triad_coherence. Scientific conclusions about a particular λ-driven run still require that run's configuration and provenance. This finding does not assert that the paper's runs used the dummy adapter.

## Current interpretive guardrails discovered during the closeout

### C21 — Uncorrected Bridge II phase-equilibrium claims must not be carried forward

**Classification: DEFINITE_MATH_ERROR.** S05 §8, already identified in S06 C17/C18/C20 and treated in S07 §7.

Equilibrium does not require every pairwise sine to vanish: `(φ1,φ2,φ3)=(0,2π/9,4π/9)` makes the sums cancel. Nor does harmonic m generally imply exactly m labelled locked families. For the attractive H3 phase-only model, the synchronized transformed-phase family has nine labelled relative lifts modulo common phase. Splay eigenlines do not fill the entire complex transverse plane. Record these as existing review corrections; do not revive the draft wording or identify those nine lifts with the older nine semantic labels without an explicit map.

### C22 — Local/discrete results and continuous phase analogies have different scopes

**Classification: INTERPRETATION_ONLY.** S01, S04 and S06 C14/C19/C22–C25.

The frozen implementation composes a finite amplitude/graph step with a simultaneous phase-coordinate update. Continuous negative-gradient or phase-flow interpretations are useful conditional mathematical parents, not equality to an exact time flow or a physical clock. Common/transverse splitting is exact for L3; full nonlinear stability and Paper F's local conclusions retain their stated coefficient, amplitude and nonzero-chart hypotheses. No new scientific error is asserted merely because one uses those analogies with their hypotheses intact.

### C23 — The earlier triangular potential supplies context, not the missing variable map

**Classification: INTERPRETATION_ONLY.** S20 p. 7 compared with S14 §11.

The November 2025 one-variable triple-well potential explicitly supplies the “threefold orientation” idea before v3.9. This upgrades that motif from recollection to documentary context. It does not establish that each complex component's phase is the same orientation variable, nor derive the later pairwise interaction or coherence average. Keep the documented motif and missing causal edge separate.

## Verification and disposition

Calculations used the `torment` Python interpreter for independent arithmetic and read-only inspection. Reciprocal values were evaluated with high-precision Decimal arithmetic, D24 counts with explicit integer residues, and pole/gradient conclusions by direct algebra. Source code was not imported or executed. PDF extraction and rendering used the available document runtime; decisive figure/equation pages were visually inspected. No model simulations or repository tests were run because this work was an evidence audit, not recertification of the kernel.

All 23 items are **recorded, not applied**. Exact artifact hashes and links are in the provenance ledger; complete before/after tree fingerprints and zero-commit/zero-push attestation are in [TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md>). Historical correction needs do not authorize repair of the protected current implementation or production system.
