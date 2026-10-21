# CA03 — GPT scientific review

**Date:** 21 October 2026  
**Disposition:** **ACCEPTED_WITHIN_RETURNING_DRIVE_AND_LOCAL_SMALL_COUPLING_SCOPE**  
**Required scientific revisions:** None identified.  
**Historical reproduction:** Not established; the accepted printed-map completion and diagnostic protocols remain explicitly distinguished from an original Figure 4 replay.  
**Publication:** No staging, commit, push, release, external upload or manuscript revision is authorized by this review.

## 1. Scientific decision

CA03 answers the requested follow-up to CA02. In the finite comparison at coupling 1/32, the four inherited size/tilt distinctions remain nonzero through three returning pulses, but their angular separations decrease to approximately 63.2% of their checkpoint values. Under CONTINUE, the same distinctions remain unchanged within the available numerical resolution. The comparison measures differences between histories under the same schedule, rather than mistaking a shared phase displacement for loss of a distinction.

The submission also proves a new, separate small-coupling result: the full 800-update return map has local fixed-point branches continuing the two simple roots of its leading angular response. For sufficiently small positive coupling one branch is locally attracting and the other is a saddle. This is a theorem about the complete post-remap two-coordinate map, not an assumed scalar phase recurrence or a conclusion drawn from three pulses. It correctly leaves the validity threshold, the actual finite-coupling fixed points, and global basins unresolved.

Six one-time disturbances at the reference checkpoint give finite evidence that new size and tilt changes can acquire angular traces, while a direct phase disturbance contracts during one returning pulse. The analytic differential calculation agrees with these separately specified tests. The geometric reference remains passive.

No scientific correction is required for acceptance within these scopes. This is not a conclusion that all SRG-centre questions have been answered or that this historical formulation is preferable to every alternative.

## 2. Exact submission and review activity

Submitted archive: `CA03_GPT_REVIEW.zip`  
Bytes: **8,794,368**  
SHA-256: **`bc18315ce76f64ca8dae5b3fafa4bec77ce0e1eceb06a566a087c01fadb044e4`**

The archive contains **103 files: 102 manifested payloads plus MANIFEST.json**. Member uniqueness and path/symlink safety, CRC, manifest completeness, payload sizes, SHA-256 identities and extracted-copy equality passed. The separately supplied summary, analysis and work order agree byte-for-byte with their corresponding members.

All 16 selected CA02 member files agree with the earlier accepted CA02 archive. Its bundled complete ZIP agrees with the earlier attachment and the accepted hash. The two consumed CA01 source files—the analysis and actual geometric reference arrays—agree with the original accepted CA01 archive. Together with the accepted CA02 archive these account for the 19 consumed-original identity records. The supplied start packet is retained unchanged.

I read the work order, plan, mathematical analysis, pre-run analysis, evidence guide, source/claim map, verification, preservation and execution records, pure evaluator, numerical driver and relevant saved-analysis code. I visually inspected all three delivered figures. No submitted source module, runner, supervisor or plotting script was imported or launched.

Independent saved-evidence coverage:

| Item | Unique coverage |
|---|---:|
| Manifested payloads | 102 |
| Consumed-original identity records | 19 |
| Exact CA02 checkpoint state/lift pairs | 8 |
| Fresh-study branches represented in the saved submission | 22 |
| Saved CA03 successor transitions | 43,200 |
| Saved CA03 states, including branch initial states | 43,222 |
| Inherited CA01 isolated fixtures | 12 |
| Inherited CA02 saved predecessor rows | 24 |
| Saved-reference tangent steps | 800 |
| Passive geometric boundary observations | 64 |
| New trajectories / new rollout updates in this review | **0 / 0** |
| Native-kernel updates | **0** |

Every computed successor in this review was compared with a saved successor; it was never used as another evolving input. The tangent calculation propagates sensitivities along the already saved reference states, not a new state trajectory. Scalar forcing sums, exact rational root/sign tests and symbolic identities likewise do not advance a three-component state.

The review script completed once successfully. An earlier integrity-only attempt stopped before numerical verification because the reviewer initially compared a pre-run analysis hash with the final supplemented report. The check was corrected to use `evidence/PRE_RUN_ANALYSIS.md`, as documented by the submission. That snapshot matches its seal, and mathematical sections 1–7 match the final report; only the introduction and the subsequent evidence/scope sections differ. This was a reviewer path-assumption correction, not a submission defect. No input or scientific result was changed.

The completed script records 7,786 Boolean checks, including sizes, shapes, table cells, identity records and numerical consistency. That is **not a count of mathematical theorems**. The coverage above reports unique inspected records, not accumulated invocation counts.

Reviewer environment: Python 3.13.5, NumPy 2.3.5, SymPy 1.14.0 and mpmath 1.3.0 on Linux. It is not the author's Windows `torment` environment. No dependencies were installed. Symbolic checks support the written proof review; this is not proof-assistant certification.

## 3. Checkpoints, clocks and source semantics

The primary evaluator is byte-identical to accepted CA02 `model.py`. The cross-product convention, forcing function, scalar clipping including epsilon, Euler increment and trigonometric remap order are retained. The independent reviewer instead used explicit torque components and the off-axis closed form of the remap as a cross-check on saved inputs; this did not replace the primary calculation.

All eight unperturbed starting states and their lifted phases match CA02 `states[800]` and `phase_lift[800]` byte-for-byte. Both arms start from the same complete checkpoint, not a rounded endpoint or a point fitted back onto the limiting circle. The six disturbed inputs match their declared one-time constructions.

For every saved update the schedule is exactly:

- CONTINUE: absolute update `n = 800 + j`, forcing index `f = 800 + j`.
- RETURN: the same absolute count, forcing index `f = j mod 800`.
- Disturbances: only the first RETURN block, `j = 0,...,799`.

All `t = 0.1*f`, block indices, state/predecessor/successor linkages and initial lift values pass. State is carried through RETURN boundaries; only the forcing clock resets. No inherited prefix was replayed in the submitted execution records. The reported numerical launch and source hashes are consistent with the 22 saved branches and 43,200 updates. As always, a supplied execution record is not direct observation of the author's machine.

The prescribed inactive-clipping argument is sound. The bound `|H(t)| <= 4.5` uses `|sin t| <= t` and a decreasing envelope for the first two terms; it is not an incorrect sum of four amplitude maxima. Including the enlarged SIZE+ start still leaves a wide margin below `0.8 - 1e-5`. Clipping remains in the evaluator and every saved factor is one. The minimum independently computed horizontal-segment lower bound is approximately **1.16426885021**, and maximum raw torque is approximately **0.211708407752**. No near-axis or clipping-switch ambiguity affects these diagnostics.

## 4. Mathematical review: the returned block really can select phase

### 4.1 Finite response

Write the full block in torus coordinates as `T_alpha = (M_alpha, A_alpha)`. At zero coupling it is `(g^800(theta), phi)`. On the unforced fixed circle, each state stays fixed, and the horizontal angular increment is identically zero as a state function at alpha=0. Therefore the first alpha derivative of the composed angular change is the sum of the direct per-step derivatives; a separate first-order state-sensitivity contribution does not appear there.

This gives

\[
A_\alpha(\theta_*,\phi)=\phi+\alpha K_{800}G(\phi)+O(\alpha^2),
\]

with the submitted `G` and finite forcing sum. Smoothness on a compact neighborhood of the circle and uniformly inactive clipping justify the finite-composition Taylor expansion and its phase derivative. No infinite-time derivative interchange is smuggled into this finite-block argument.

An independent 90-digit scalar evaluation of both the 800-term sum and its finite geometric expression gives

\[
K_{800}=6.58649686916412787317049621696\ldots.
\]

The expressions agree at the specified working precision. Positivity is also established by the report's written bound, rather than depending on that decimal evaluation. The first-order phase gain can be less or greater than one according to the starting phase. The actual block retains a meridional coordinate; no result licenses replacing its full action by this leading scalar expression at finite coupling.

### 4.2 Exactly two simple leading zeros

The half-angle substitution `v = tan(phi/2)` gives the submitted quartic, with the sign checked independently by symbolic rational simplification:

\[
p(v)=b v^4+2(r+z_*)v^3+2(r-z_*)v-b.
\]

There is one positive root and one negative root by the sign argument, and neither the omitted phase pi nor a quadrant boundary is an additional zero. The geometric sign equation locates these roots in quadrants I and III. The simplified derivative at a root,

\[
G'(\phi)=z_*\cos^2\phi-r/\cos\phi,
\]

is negative in quadrant I and positive in quadrant III, so both are simple.

I independently checked both supplied rational root brackets with exact interval arithmetic using fresh 60-decimal-grid square-root enclosures. Opposite polynomial signs and strict root-slope signs pass. The displayed leading phases, approximately **0.245117619178** and **3.252359982752 radians**, agree with the independently evaluated bracket midpoints. These are leading roots as coupling tends to zero, not certified finite-coupling fixed-point locations at 1/32.

### 4.3 Full-block fixed points, not a fitted invariant circle

The meridional derivative at zero coupling is

\[
\mu=(\sqrt3-2)^{800}>0.
\]

It is about `2.76669938348e-458`: very small but not mathematically zero. Since `mu - 1` is nonzero, the implicit function theorem solves the meridional fixed-point equation for `theta = h(alpha, phi)`. This is a fixed-point equation, not an assertion that this graph is invariant under all nearby block motion.

Substituting it into the angular fixed-point equation, dividing by alpha through a smooth extension, and using the two simple zeros yields actual local branches of fixed points of the complete two-coordinate block map. The zero-coupling angular component has no theta dependence, so eliminating theta does not change its first-order angular coefficient.

The two simple-eigenvalue expansions are correct:

\[
\lambda_{\rm mer}=\mu+O(\alpha),\qquad
\lambda_{\rm ang}=1+\alpha K_{800}G'(\phi_{\rm root})+O(\alpha^2).
\]

Thus sufficiently small positive coupling gives a local attracting branch in quadrant I and a saddle branch in quadrant III; sufficiently small negative coupling reverses those angular roles. Meridional stability persists. The argument does not supply an explicit alpha threshold, a global basin classification, or certification at 1/32.

A fixed point of the block map means that the state repeats at corresponding boundaries under the repeated forcing schedule. Motion during a pulse can be nonconstant. With the clock included, this is a periodically driven history, not necessarily a static resting point or a persistent trajectory on the old fixed circle. The report correctly makes no minimal-period claim.

### 4.4 Retention and coalescence are protocol-dependent

Finite contraction does not establish exact erasure. Conversely, finite survival does not establish permanent protection. Under indefinite repetition, nearby starts in the attracting neighborhood supplied by the small-coupling theorem approach the same block state asymptotically. The finite experiment does not establish that all eight histories at 1/32 satisfy those hypotheses.

The fading-drive endpoint theorem cannot be applied to indefinite restarting because the driving sequence is no longer absolutely summable over all blocks. The local block theorem supplies a different valid argument in its own domain. These two conclusions are compatible, not competing descriptions of the same protocol.

## 5. Independent finite-result verification

The four RETURN comparisons reproduce the submitted table:

| Earlier difference | Checkpoint separation, radians | After three RETURN blocks, radians | Retained magnitude |
|---|---:|---:|---:|
| Half initial size | -0.001112179547 | -0.000702991202 | 0.632084274 |
| 1.5 times initial size | +0.001119388660 | +0.000707461627 | 0.632007141 |
| Earlier zero tilt | -0.001611354867 | -0.001018539820 | 0.632101495 |
| Earlier pi/4 tilt | +0.007988608873 | +0.005046949205 | 0.631768220 |

These are approximately 36.8% reductions in **angular separation**. They are not percentages of recoverable information or a universal retention constant. The reductions after one and two pulses also agree with the supplied ranges, about 85.9% and 73.7% remaining. None of these four differences reverses sign; small within-pulse increases mean the contraction is a net block result, not a monotone decrease at every update.

For CONTINUE, the largest change of the four phase differences is approximately `6.68e-15` radians. The correct reading is no resolved change at this numerical precision, not an exact equality theorem. The orientation controls turn by different amounts under RETURN; the effect is not a common rotation concealing unchanged separations.

The six later-disturbance outcomes agree with the reported results: approximately ±0.1914 microradians from the fractional size disturbances, approximately ±1.076 microradians from tilt disturbances, and approximately ±85.922 microradians remaining from the ±100-microradian phase disturbances. These are different input directions, in different parameter units, at one disturbance size and one reference checkpoint. They do not constitute a general noise study or a physical robustness ranking.

## 6. Differential calculation and numerical accuracy

The stated torque Jacobian and remap derivatives are correct. I checked the saved tangent recurrence through an independently constructed trigonometric Jacobian, and also propagated the tangent columns along the same 800 saved reference steps. No fresh perturbed state input or state trajectory was generated.

The resulting one-block phase derivatives are approximately:

| Perturbation parameter | Independent derivative |
|---|---:|
| Fractional size | 0.001914096242234714 |
| Tilt angle | 0.01075615522221948 |
| Phase angle | 0.8592175718680587 |

These agree with the saved differential calculation and the central differences from the six authorized branches, within their stated finite-order/roundoff qualifications. The maximum discrepancy between the independent cumulative tangent and stored tangent is approximately `1.03e-14`, below the `1e-12` consistency criterion. This agreement is not a numerical certificate for all higher derivatives or a global accumulated-error bound.

Independent saved-successor checks have maximum discrepancy **4.44e-16**. The scaled Euler identity, perpendicularity and torus residual maxima are approximately **4.64e-16**, **2.58e-17** and **1.67e-16**, respectively. The maximum lifted-phase versus azimuth discrepancy is approximately **1.40e-14** radians. Small differences from Codex's residual maxima are expected from independent arithmetic grouping and environment; all are well within the declared criteria.

The tail convention is correctly clock-qualified. After the last finite RETURN pulse, a hypothetical future without further resets has the exact-trajectory tail bound `B_800`, approximately `2.13895878976e-11` radians per state. CONTINUE's final uninterrupted tail is `B_3200`, approximately `1.15050858390e-42` radians. Earlier RETURN boundaries may use `B_800` only for the counterfactual that no further reset occurs, not to bound the next actual pulse. Two-state tails add.

Neither bound includes inherited checkpoint error, disturbance-construction error or accumulated floating-point error. In particular the latter tail does not give 42-digit accuracy to a binary64 state. The observed finite-coupling separations remain numerical evidence, not certified exact intervals. That limitation is correctly present in the submission and does not invalidate the separate small-coupling proof.

## 7. Passive geometry and figure review

The native meridional/phase coordinates help distinguish a strongly contracting direction from angular differences. The actual crystal reference supplies positional context but no additional invariant or predictive SRG-to-Z correspondence has been established.

All 64 indexed observations were reconstructed from the saved boundary states. The rigid rotation transforms the data, actual reference arrays, circle and measuring axes together. Native coordinates are recovered to about `2.22e-16`; all-pair Euclidean distances remain equal to about `8.88e-16` in the reviewer's broader all-64-pairs comparison. Original face and open-boundary arrays are retained. No observer result feeds back into the recurrence. Equal vertex-distance readouts for the two hands do not distinguish their different face surfaces.

All three figures are legible and retain their needed qualifications. Figure 1 distinguishes RETURN from CONTINUE and net separation from whole-pattern movement. Figure 2 labels leading-order curves and their noncertification at the tested coupling. Figure 3 keeps the size, tilt and phase parameter units distinct, shows different vertical scales, and identifies its three sample stages rather than implying a continuous orbit. No rendering repair is required.

No physical ball, confining torus, pressure mechanism, magnetic field or thermodynamic identification follows from this comparison. The reference framework remains the author's analytical instrument, not an asserted material container.

## 8. Preservation, limits and closeout

All 19 consumed-original identities are consistent with their retained copies and, where supplied, the earlier accepted archives. Before/after status bytes agree, the index records are empty, and recorded HEAD and branch agree. The pre-run source seals, numerical-launch script hashes and all 22 recorded raw-branch hashes check out. All extracted input bytes remained unchanged during this review.

I did not access the author's Windows filesystem or the Git remote. These are checks of supplied evidence, not direct independent observation of every local file or publication action. No original-source search was repeated, and no broader historical model was silently substituted.

**CA03 is scientifically accepted within the stated finite-protocol and local small-coupling scopes. There are no required scientific revisions.** Its main lesson is that a later input can register new differences while reducing earlier ones. Repeated activity is not automatically a mechanism for preserving every past distinction.

The specific unresolved bridge is between the local theorem for sufficiently small coupling and indefinite behavior at the diagnostic value 1/32. The current finite run does not resolve that bridge, nor does it require changing the accepted equations. A future investigation should be separately specified. No continuation, new run or publication is authorized by this acceptance.

## 9. Review artifacts and reproduction

- `CA03_INDEPENDENT_RESULTS.json`: unique saved-record coverage, residuals, rational/sign checks, scalar values and comparison results.
- `CA03_REVIEW_ACTIVITY.json`: separate-attachment checks, hash checks, figure inspection and the reviewer-checker attempt history.
- `review_ca03.py`: standalone saved-record checker; it imports no submitted scientific scripts and starts no trajectory.

Example Windows CMD invocation, replacing path placeholders with actual extracted locations:

```bat
call conda activate torment
python -B review_ca03.py --input-dir "C:\path\to\extracted_CA03" --archive "C:\path\to\CA03_GPT_REVIEW.zip" --ca02-archive "C:\path\to\CA02_GPT_REVIEW.zip" --ca01-archive "C:\path\to\CA01_GPT_REVIEW.zip" --packet "C:\path\to\SRG_CA03_CODEX_START_PACKET.zip" --output-dir "C:\path\to\new_review_outputs"
```

The three prior-archive/packet arguments are optional extra identity comparisons; the CA03 input and archive are required. Keep output outside the submission directory. Review the supplied evidence without running `run_stage.py`, `supervise.py` or the original historical programs.

**Principal sources:** `CA03_RETURNING_DRIVE_ANALYSIS.md` §§1–9; `CA03_PLAN.md`; `READ_ME_FIRST.md`; `EVIDENCE_GUIDE.md`; `SOURCE_AND_CLAIM_MAP.md`; `model.py`; `run_stage.py`; `SCALAR_ANALYSIS.json`; the CSV/JSON comparisons, `raw/*.npz`, `TANGENT.npz`, `OBSERVER.npz`; consumed-source and execution records; unchanged CA01/CA02 inputs and their accepted reviews. Proof assessments above are independent reasoning about those supplied definitions, not substitution of outside sources.
