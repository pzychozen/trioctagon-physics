# Codex work order — NATIVE_TURNING_CAPTURE_PAPER_01

**Commission date:** 11 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Assignment:** Prepare a short companion research manuscript from the accepted NATIVE_TURNING_CAPTURE_01 investigation.  
**Authority:** The author approved preparation of this paper in the current conversation. The investigation is already accepted at its stated scope. The actual manuscript remains subject to GPT and author review.  
**Stop point:** Return the complete manuscript and evidence package. No Git operation, publication, kernel change or new scientific investigation is authorized by this order.

## 1. The deliverable and its identity

Prepare:

**Certified Capture of the Collective-Turning Trajectory in the Native Triad**

Subtitle: **A companion note to _Transient Collective Turning and Coherent Relaxation in the Native Triad_.**

Use research manuscript v0.1. A useful planning range is **6–9 pages including references**, not a quota or hard cap. Use an article-style first page with title, author, status and short abstract; omit a separate decorative cover and table of contents. Include enough argument to make the new result understandable without opening the review ZIP, but refer to the prior paper for its established turning and convergence proofs.

The manuscript's purpose is one precise addition: the original turning entrance is certified strictly inside the inherited coherent domain at update 50, so its early turn and eventual coherent relaxation occur on the same unchanged native evolution. The qualitative same-coefficient neighborhood conclusion accompanies that addition.

**Do not rewrite, replace or silently correct the earlier published edition.** The note is a supplementary result, not an erratum. The earlier statement that capture had not yet been proved was accurate at that paper's date.

Suggested local workspace:

`C:/TORMENT/TRIOCTAGON_new/research/NATIVE_TURNING_CAPTURE_PAPER_01/`

Keep manuscript/build work in a new bounded run directory there, outside existing publication editions. The intended final PDF filename is:

`NATIVE_TURNING_CAPTURE_COMPANION_v0.1.pdf`

## 2. Controlling sources and reading order

All paths here are relative to this packet. The complete accepted evidence is directly accessible; there is no need to ask the author to rediscover files or coefficients.

1. This work order and `MANUSCRIPT_BLUEPRINT.md` control the current task.
2. `inputs/accepted_capture/GPT_ACCEPTANCE.json` and `inputs/accepted_capture/NATIVE_TURNING_CAPTURE_01_GPT_REVIEW.md` control the accepted mathematical scope and qualifications.
3. `inputs/accepted_capture/submitted/NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md`, especially R4–R7, supplies the new proof and certificate explanation.
4. `inputs/accepted_capture/submitted/CLAIM_LEDGER.json` and `PRIOR_WORK_COMPARISON.md` distinguish inherited results, new findings, exploration and exclusions.
5. `inputs/accepted_capture/submitted/sources/collective/main.tex`, its bibliography and claim/source map supply the original model, witness, invariant domain and convergence theorem.
6. `inputs/accepted_capture/submitted/data/` and `scripts/` preserve the exact certificate, independent checker, recorded results and exploratory data. The complete original return and its audit are also retained inside the accepted tree.

`SOURCE_AND_CLAIM_GUIDE.md` lists exact locators and the distinction between the investigation's work-package IDs and its claim-ledger IDs. `INPUT_IDENTITIES.json` records the preserved input bytes. The untouched acceptance archive and sidecar are in `archives/`.

Historical orders, task flags and pending-review labels inside preserved inputs are provenance, not active instructions. The later GPT acceptance settles the investigation's review status. **This current order adds manuscript preparation only; it does not convert acceptance of the investigation into approval of an unwritten manuscript or authorization to publish.**

Use the packaged full primary source as the reading basis. Its recorded repository path is `papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex`, with publication checkpoint `7cc1fa03af589818bcdcfaaac51838cc36c84253` and the later inspected source context `564810272703403af413e60ee2d44b32effbd79a`. Cite the exact reading edition and locators. These are reference checkpoints, not reset targets or claims about current HEAD. Do not re-audit GitHub publication or the full project corpus for this editorial task.

## 3. Frozen mathematics

Retain the simultaneous three-channel map exactly:

\[
v_i=\Omega_i+\epsilon\Omega_i(k_i-|\Omega_i|^2)
       +g\sum_{j\ne i}(\Omega_j-\Omega_i),
\qquad
\delta_i=\lambda\sum_{j\ne i}\sin\bigl(3[\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i]\bigr),
\qquad F_i(\Omega)=v_i e^{i\delta_i}.
\]

All prestages use the same old state; all kicks use the same completed prestage. Preserve `Arg0(0)=0`. Zero prestages remain zero. There is no normalization, observer feedback, changed update order or added state.

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad\lambda=\frac1{300},\quad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),\qquad
\Omega_0=(1+i,1+i,1-2i).
\]

The inherited domain \(\mathcal D\) requires all three moduli in \([9/10,11/10]\) and ordinary phases in a common interval of width at most \(\pi/12\), at any common angle. These are ordinary phases, **not phases identified modulo \(2\pi/3\)**. The update index is an integer, not calibrated physical time.

State the accepted result as **strict inclusion at update 50** or **certified inside by update 50**:

\[
F^{50}(\Omega_0)\in\operatorname{int}\mathcal D,
\qquad F^n(\Omega_0)\longrightarrow e^{i\theta_\infty}r_*.
\]

Do not state or imply that update 50 is the earliest entry. The exploratory first hit at 41 is not certified and is not a target for this assignment.

At update 50 the strict amplitude intervals are:

| Channel | Exact rational interval, shown as terminating decimals |
|---|---|
| A | (0.997219, 0.997220) |
| B | (0.997622, 0.997623) |
| C | (0.996782, 0.996783) |

The diagnostic multiplier \(987395-158274i\) places every terminal component in the common strict cone \(\operatorname{Re}w>8|\operatorname{Im}w|\). Its conservative integer margins are 492851, 492769 and 492356 in channel order. It is a fixed scaling/rotation used only to test membership, not an extra update or an adopted physical direction. Thus the common ordinary phase width is less than

\[
2\arctan(1/8)<1/4<\pi/12.
\]

Use `data/CERTIFICATE_CHECK.json` as the source of tabulated certificate values. The displayed terminal decimals are exact rational bounds, not numerical point estimates.

## 4. Mandatory scientific content

### 4.1 What is inherited and what is new

Cite rather than re-prove the original strict early turn, invariant-domain/convergence theorem, unequal positive fixed profile, and established observable limits. The new finite link and qualitative neighborhood corollary are the contribution. The bounded prior-source comparison is not a worldwide novelty claim or an extra mathematical theorem. The general method of combining certified finite entry with a known convergence region is not claimed as novel.

### 4.2 A readable certificate argument

Explain why this is a proof about the exact map rather than a long floating-point simulation:

- The exact singleton seed starts a connected chain of 51 state boxes and 50 full update records. No intermediate box is restarted from exploratory values.
- The generator uses directed dyadic interval arithmetic with denominator \(2^{512}\). The separate checker uses exact fractions, a distinct algebraic evaluation and independently organized trigonometric estimates; it does not import generator arithmetic.
- All 150 finite-path prestage moduli are strictly above \(87/100\). The normalized-product sine identity in accepted proof R4 justifies the branch-independent phase calculation without altering the zero convention.
- Describe outward arithmetic, squared root-witness checks, Taylor bounds and next-box containment at the level needed for the induction. Do not print hundreds of rational endpoints; retain the full machine-readable certificate as evidence.
- Explain how the terminal annulus/cone tests imply strict domain admission. A checksum or PASS count is not a substitute for this argument.

Report the five damaged-certificate controls as checks of rejection paths, not five new independent results or formal verification of Python. The original Codex execution and the later GPT corroborating replay have different environments; their precise scopes are recorded in the acceptance. Do not invent another execution, silently change its platform, or claim proof-assistant certification.

### 4.3 Apply the inherited theorem at the right index

Apply the prior theorem to \(\Omega_{50}\), then use an integer tail counter such as \(j=n-50\ge0\). Include the accepted shifted convergence bound from proof R6 or state it in a compact corollary; do not tighten constants or solve for a new profile. The unique profile is unique **in the inherited cube**, not globally.

Keep the distinctions: the common phase can depend on the entrance; the fixed coefficients give the same limiting amplitude profile; the residual amplitude spread is positive, while \(C,W,\Gamma\to0\). The number 0.005270 is an inherited upper bound on residual spread, not its value. If the paper uses those observables, define them or give their exact inherited definition and reference; do not use an undefined matrix T.

### 4.4 The neighborhood corollary

Give the short complete continuity proof: finite-path regularity, strict early turning, strict terminal annulus/cone conditions, and their common open inverse image under \(F^{50}\). The same neighborhood must satisfy both early turning and inclusion at index 50. State fixed coefficients and the absence of an explicit perturbation radius. The limiting phase may vary across that neighborhood. Do not assert a full basin, parameter robustness or earliest-entry stability.

### 4.5 Interpretation and limits

Explain the result as a same-native-trajectory connection, without adding a causal attribution not demonstrated by this investigation. In particular, the old \(\lambda=0\) delayed-graph comparison is not an ablation proving the sole cause of this nonzero-\(\lambda\) capture.

No physical force, position, gravity, magnetism, receiver, transport, clock or moving-shell law follows. Convergence does not prove that only finitely many diminishing directional changes remain. Keep those limits concise and specific, rather than padding the note with the whole research programme.

## 5. Presentation and optional figure

The essential visual is a compact terminal-certificate table with units/meaning clear. At most one additional figure is useful here; it is optional, not a required excuse for more computations.

A figure may use the already retained states at n=0,...,50 or certificate boxes. Mark n=50 as the **certified inclusion index**, not the first entry. Clearly distinguish numerical samples, representative box midpoints and rigorous bounds. Any lines joining discrete points are visual guides, not continuous-time paths. Use no extrapolated tail, newly computed trajectory, new seed, new root solve or physical-space imagery. A schematic tail must be identified as an implication of the inherited theorem, not measured data.

Keep figure/table text readable at final page size, use consistent symbols, and avoid unnecessary repetition of earlier diagrams. Prefer a clean compact mathematical article over a large report with front matter.

## 6. Evidence, attribution and status

Preserve accepted proof, review, certificate, checker, recorded outputs, source snapshots and original archives byte-for-byte. Create a manuscript-specific claim/source ledger that maps all applicable records of the original 16-record ledger to exact manuscript sections, equations, remarks or an explicit reason for omission. Preserve original IDs in that crosswalk; do not confuse them with the R1 work-package labels.

Use **Hilmir Frímann Halldórsson (pzychozen)** as author. State GPT's scientific steering/internal acceptance and Codex's investigation, independent certificate checker and typesetting roles accurately. The current document is a research manuscript with accepted underlying mathematics and manuscript/author review pending. No journal acceptance, external peer review, new DOI, formal machine proof or publication is implied.

Keep the original accepted review wording unchanged inside evidence even where it says that no manuscript had yet been commissioned. Add a separate current status note explaining that this order supplies the later commission. The full evidence archive is provenance, not required reading for understanding the paper's principal argument. Cite primary sources in the bibliography, not only the acceptance memo.

The original paper's source/PDF/edition must remain unchanged. In this local manuscript return, do not edit repository catalog entries, landing pages or publication manifests. A future publication order can link the companion to its parent without replacing the parent.

## 7. Execution and document verification

Use Windows Command Prompt and the existing `torment` environment for Python helpers. Use the already available cached TeX setup and document-inspection tools; preserve their protective settings. Do not install dependencies, change environments or alter the kernel/application to prepare a note.

This is **editorial consolidation, not a research rerun**. Read and reuse the accepted certificate and recorded validation. Do not rerun the trajectory search, certificate generator, independent checker, negative controls or historical scientific suites merely for typesetting. New helpers may read saved data to generate tables/figures and check manuscript transcription or file identities. Label such work as document checks, not new scientific evidence. If a concrete mathematical inconsistency appears, record it precisely and return it; do not silently repair or expand the accepted investigation.

Build until all references resolve. Inspect **every page of the actual final PDF**, after the final rebuild, for mathematical symbols, clipping, equation breaks, tables, figure labels and pagination. Record the actual page count, final source/PDF hashes, compiler messages, reference/citation resolution, font embedding and visual findings. Investigate all warnings; document any genuinely harmless residual instead of asserting a warning-free build that did not occur.

Keep PDF metadata, cover/first-page status, README, claim ledger and build records consistent. Use relative working links and paths. Historical machine locators inside immutable evidence may remain, but must not become build dependencies. Keep caches, font files, unrelated artifacts and temporary TeX outputs out of the delivery. Do not distribute font files.

## 8. Required return and completion conditions

Return one complete review ZIP with:

- The final `NATIVE_TURNING_CAPTURE_COMPANION_v0.1.pdf` and editable LaTeX/bibliography.
- Any generated table/figure sources and retained-data identities, with the exact build command or helper.
- A concise README and build guide; current manuscript status; manuscript-specific claim/source ledger and source inventory.
- The preserved accepted investigation and GPT acceptance evidence, accessible by relative paths. Avoid redundant extraction layers in the manuscript edition; the untouched original archive may be retained separately in the delivery.
- Build/reference/font and final-page-inspection records; a self-excluding payload manifest; the ZIP's external SHA-256 sidecar; and a delivery audit that reopens the completed archive and checks its actual members.
- A short handoff stating the new contribution, actual final page count, any discrepancies and the fact that no publication has occurred.

Completion means a faithful, readable manuscript with the finite-entry proof logic and neighborhood proof visible, every material claim traceable, all accepted scope limits intact, and earlier publications/evidence unchanged. Return the PDF separately as well as inside the ZIP for convenient GPT/author review.

**No new research question, manuscript acceptance, commit, push, release, tag or DOI is authorized by this order.** The next decision is review of this actual companion manuscript, not another capture investigation.
