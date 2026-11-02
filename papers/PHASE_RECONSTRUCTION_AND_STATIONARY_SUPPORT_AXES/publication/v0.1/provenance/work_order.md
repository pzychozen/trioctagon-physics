# Codex work order — phase reconstruction and spatial correspondence paper

**Task:** NATIVE_PHASE_SPATIAL_PAPER_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson / pzychozen  
**Scientific direction and manuscript review:** GPT  
**Manuscript preparation and document verification:** Codex  
**Status:** Author requested the write-up; authorized manuscript preparation, returning for review

## 1. Assignment and stopping point

Prepare one complete mathematical companion paper combining the accepted results of **NATIVE_PHASE_RECONSTRUCTION_01** and **NATIVE_SPATIAL_CORRESPONDENCE_01**.

**Working title:**

> Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map

The central thread is:

> The existing closed retained dynamics determines a full native history once one initial common phase is supplied. The adopted decoder then gives its exact spatial action around the existing stationary reference axes, with a precise distinction between individual face rotations and a universal common rigid rotation.

Include the accepted overlap-angle correction as a principal result, rather than reducing the phase investigation to a reconstruction formula. Present the source-supported mathematical correspondence without choosing a material attachment or a new motion law.

The preceding investigations are scientifically accepted. This order records that acceptance and authorizes their manuscript preparation, including the specific editorial/table corrections below. Resolve ordinary exposition, notation, bibliography, compilation, and layout issues autonomously. No further preliminary approval or fresh-chat handoff is needed.

**Deliver a complete compiled, visually inspected review draft v0.1, its portable sources, and a compact source/evidence package. Then stop for GPT and author manuscript review.** This review concerns the assembled paper and its presentation. It does not automatically reopen accepted investigations. Publication, repository adoption, Git operations, push, release, and DOI deposit are outside this order.

## 2. Workspace, environment, and source access

Use Windows Command Prompt, the existing environment, and an available installed document toolchain:

~~~bat
call conda activate torment
~~~

Create the new external workspace:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_SPATIAL_PAPER_01
~~~

Use a dated suffix if occupied. Keep new source, evidence copies, build products, temporary files, and page renders inside it. Preserve all existing accepted notes, reviews, helpers, results, published editions, and repository files byte-for-byte. The corrections below apply to the new manuscript, not to those historical records.

The original checkout is `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`. It was deliberately preserved during earlier publication. Prefer the retained publication worktree for published inputs:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01\publication_worktree
~~~

The reading reference is commit `634ff13b666604d5caed11cc3731dcb5a863ff6c` in `pzychozen/trioctagon-physics`:

<https://github.com/pzychozen/trioctagon-physics/tree/634ff13b666604d5caed11cc3731dcb5a863ff6c>

This identifies sources, not a checkout instruction. Specific immutable files may be retrieved read-only if needed. Do not synchronize the original checkout or repeat previous publication audits. Use the existing cached document toolchain; no package installation or environment change is commissioned. Applicable local instructions may be read without changing them.

### Governing accepted inputs

| Input | Role |
| --- | --- |
| `research\NATIVE_PHASE_RECONSTRUCTION_01\NATIVE_PHASE_RECONSTRUCTION_01_PROOF_REVIEW.md` and its existing helper/results and source records | Full-state reconstruction, continuous canonical increment, accumulated phase, overlap correction and its analytic witness, representative dependence. |
| `research\NATIVE_SPATIAL_CORRESPONDENCE_01\NATIVE_SPATIAL_CORRESPONDENCE_01_PROOF_REVIEW.md`, `CLAIM_SOURCE_LEDGER.md`, existing helper/results and source records | Exact decoder/support dictionary, positioned axes, decoded evolution, universal proper-rotation classification, observer comparison. |
| `NATIVE_PHASE_RECONSTRUCTION_01_GPT_REVIEW.md` and `NATIVE_SPATIAL_CORRESPONDENCE_01_GPT_REVIEW.md`, if copied into the named workspaces or Downloads | Accepted dispositions and corrections. Their operative decisions and all required corrections are supplied in this order, so absence of a local review copy does not block preparation. |
| `papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/` | Published predecessor: exact retained coordinates, image, closed map, energy/descent retention. Cite it and state the necessary inherited hypotheses; do not reproduce its minimum-information or potential proofs. |
| NRG `manuscript/observables_closure.tex` and `manuscript/appendices.tex` | Adopted decoder, transport, face update, exact frame table, and interpretation limits. |
| `papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex`, or the accepted predecessor's primary-source snapshot | Inherited domain invariance, phase nesting, regularity, and limiting-phase bounds. |
| `docs/methods/Z_MOTION/v0.1/manuscript/NOTE.md`; read-only `kernel_physics/z_manifold.py` if needed | Staged/EMA definitions and the corrected distinction between updating memory and observing current memory. |
| Recorded local fixed-gap sources: `research\NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01\packet\REFERENCES\NCM_FIXED_GAP_01_REPORT.md` and `NCM_FIXED_GAP_01_GPT_REVIEW.md` | Exact origin/support conventions and accepted stationary-reference/attachment boundary. |

Paths beginning `research\` above are relative to `C:\TORMENT\TRIOCTAGON_new`; repository paths are relative to the retained publication worktree. A bounded exact-filename lookup in those research directories and Downloads is sufficient if a review has moved. Use available accepted archive members as a fallback. Do not ask the author to reconstruct archives.

The accepted phase proof has SHA-256 `0ce3d59e249ee7794c3386047e2bf79f9d7a83b76ec563c8541de4b66c35f2c6`; the accepted spatial proof has SHA-256 `9b89dfdd94be93ea50bb0e4b9f8029383801a0bae6965e8c662eb4e4d07f2ddd`. These identify reviewed copies. Record discrepancies rather than overwriting changed local files. The spatial ledger already identifies its ten input files; reuse that focused provenance.

## 3. Manuscript structure and scientific content

Use a concise standalone exposition, with detailed algebra in appendices where helpful. There is no page quota. Supply complete arguments for the paper's central results and cite inherited theorems precisely.

### A. Setting and inherited reduced dynamics

Define the ordered native triad map explicitly, including the simultaneous prestage synchronization, native zero convention, and lambda-zero bypass. Keep

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad
\lambda=\frac1{300},\quad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right).
\]

The domain has component amplitudes in \([0.9,1.1]\), ordinary phase width at most \(\pi/12\), and arbitrary common phase. State the accepted regularity and forward invariance with citations.

Give the five retained coordinates \(y=(s_1,s_2,s_3,A_{12},A_{13})\), positive-root representative \(z(y)\), and exact joint-span image \(\mathcal Y\). Preserve boundaries, zero individual areas, coincident phases, and aligned inputs. Independent area bounds do not replace the image condition. Retain

\[
\overline\Omega_i\Omega_j=S_{ij}+iA_{ij},\qquad
H=\Omega\Omega^\dagger=S_G-iA_G.
\]

Explain which closure and fibre statements are inherited. Any reference to the earlier minimum count must retain its specified raw-entry dictionary; no new unrestricted minimality claim is intended.

### B. Exact phase reconstruction

Present the representative map, its inverse on the admitted domain, and the lifted update:

\[
\Psi(y,u)=uz(y),\qquad
\widehat F(y,u)=(Gy,u\kappa(y)),\qquad
F\Psi=\Psi\widehat F,
\]
\[
\kappa(y)=\frac{F_1(z(y))}{|F_1(z(y))|},\quad
u_0=\frac{\Omega_{1,0}}{|\Omega_{1,0}|},\quad
\Omega_n=u_0\left(\prod_{j=0}^{n-1}\kappa(G^jy_0)\right)z(G^ny_0).
\]

Retain the explicit retained-data expression for \(\kappa\), its nonzero denominator, and the homeomorphism/conjugacy statement. Conjugacy of self-maps does not require invertible dynamics. One initial common phase remains indispensable data.

Prove the canonical continuous argument using the accepted positive real-part bound, not nonvanishing alone. Distinguish the prestage phase change from the synchronization kick. Retain both accepted tail bounds, with \(c=1-3\sqrt2/200\):

\[
\sum_{j\ge n}|\vartheta(y_j)|\le
\frac{\Delta_{\rm init}c^n}{1-c},\qquad
|\theta_\infty-\theta_n|\le\Delta_{\rm init}c^n.
\]

These identify and control the already-established limiting phase. Keep absolute variation separate from net remaining adjustment. Explain the aligned case: zero angular increments can accompany amplitude relaxation.

### C. Overlap diagnostic and its correction

Retain the trace/conjugation order and factorization:

\[
\mathcal O(y)=\Omega^\dagger F(\Omega)
=\operatorname{tr}(U_\delta M H)
=\kappa(y)B_{\rm sec}(y),\quad
B_{\rm sec}(y)=z(y)^\dagger z(Gy),
\]
\[
\alpha_{\rm ov}=\vartheta+\gamma,\qquad
\gamma=\operatorname{Arg}B_{\rm sec}.
\]

Include the positive-real-part bounds and ordinary-argument justification. Accumulating overlap angles requires subtracting the representative correction. Keep the accepted analytic family \(z(t)=(1,e^{it},e^{it})\) and its derivative sign argument proving that this correction is not identically zero. This is an analytic witness in the same domain, not a sampled trajectory.

Give the accepted change-of-representative formulas and cancellation in the reconstructed state. Do not assert that the canonical correction is an endpoint difference, or that such a representation is impossible. Arbitrary continuous representative changes do not inherit the canonical absolute-variation estimates merely by continuity.

### D. Exact spatial action and stationary axes

Include one exact table of face centers \(c_i\), normals \(n_i\), tangents \(t_i\), support directions \(g_{i-1}\), and channel labels. Use the specified reference/PLUS support convention and common origin \(O=(0,\sqrt3/6,0)\).

Prove the accepted positioned-line and signed-angle identities:

\[
c_i-O=\frac{\sqrt3}{6}n_i,\quad n_i=-g_{i-1},\quad
c_i+\mathbb Rn_i=O+\mathbb Rg_{i-1},
\]
\[
D_i(e^{i\chi}\omega)=R_{n_i}(\chi)D_i(\omega)
=R_{g_{i-1}}(-\chi)D_i(\omega).
\]

Include the affine basepoint argument, so positioned-line equality is distinguished from a direction match. Explain the existing tangent-plane decoder, inverse, and ambient projector. Compose reconstruction with \(F_{\rm face}=DFE\), giving the commuting relation and exact face history.

Give prominence to the complete native-step expression:

\[
v_{i,n+1}=\sqrt{\frac{s_{i,n+1}}{s_{i,n}}}\,
R_{n_i}\!\left[\vartheta(y_n)+\eta_i(Gy_n)-\eta_i(y_n)\right]v_{i,n}.
\]

Separate pure common rephasing from the amplitude and relative-phase changes of an actual update. The algebraic decoder identity holds more broadly than the dynamic theorem; do not extend the latter across zero prestages or to other parameter histories.

### E. The universal proper-rotation theorem

State the quantifiers explicitly: for fixed \(\chi\), one \(Q_\chi\in SO(3)\), independent of \(\Omega\), must satisfy

\[
D_i(e^{i\chi}\Omega_i)=Q_\chi D_i(\Omega_i)
\quad\text{for every }\Omega\in\mathcal D\text{ and all fixed labels }i.
\]

Preserve the accepted classification \(\chi\equiv0\pmod{2\pi}\) and its short two-witness proof. Show admission of both witnesses, pairwise-Gram preservation, and the full-rank half-turn obstruction. Explain the planar special case to prevent an overstatement about every individual configuration.

This theorem compares free vectors in a fixed ambient frame. It neither classifies all individual registrations nor establishes a native period, a moving mesh, or a universal prohibition on material motion.

### F. Observations, consistency, and interpretation

Give a compact dependency table for face arrows, retained invariants, staged Z/placed points, EMA innovation, EMA memory updates, and observations from current memory. Use the corrected entries in §4 below.

Explain the all-iterate staged-history equality for equal retained starts and identical exogenous schedules. Preserve raw channel chirality \(C_{\rm ch}=(A_{23},-A_{13},A_{12})\); it is not the ambient axial projection. Do not claim closure on Z alone, infer unknown initial memory, or transfer this domain theorem to the different historical Z coefficients.

A short energy-consistency paragraph may cite the predecessor. Preserve its normalization and scope if quoting a bound; another descent or minimality proof is unnecessary.

Close with what the mathematics establishes and what would require a new declared correspondence. Mathematical arrows/endpoints, stationary reference lines, and material features remain distinct. No material attachment or continuous interpolating path is supplied. The author need not choose one to complete this paper.

## 4. Required editorial corrections and notation

Carry these into the new manuscript while preserving accepted source records:

1. Use **“full-state relation”** in place of the phase note's “physical-state relation.”
2. Describe the analytic witness as distinct from a **“numerical native-step evaluation”**; it does analytically differentiate the native map.
3. Where the section-changed overlap's unit factor is written explicitly, use \(B_{{\rm sec},h}/|B_{{\rm sec},h}|\).
4. Split the spatial note's combined **“EMA memory and resulting observation”** row. The accepted corrected dependencies are:

| Quantity | Inputs and phase dependence |
| --- | --- |
| EMA memory update | Uses \(J_n=\Im[u_nz_1(y_n)\overline{z_2(y_n)}z_3(y_n)]\), its normalization by \(1+|J_n|\), and current memory. Generating its history requires \(y_0,u_0\), initial memory, the existing update rule, and specified sampling/order; a supplied innovation sequence can replace native-history inputs. |
| EMA observation from current memory | Uses \(I(y_n)\), \(C_{\rm ch}(y_n)\), current memory, and the specified observer clock/configuration, plus placement data if a point is requested. At fixed retained data, memory, and observer settings, current phase supplies no extra value information. Phase can affect later observations through explicitly updated memory. Generating memory requires the additional inputs in the preceding row. |

The implementation names are `advance_ema` and `observe_ema`. Observation does not implicitly evaluate the cubic or update memory. These corrections need no scientific run.

Resolve notation once in a short table. Prefer \(\Psi\) for state reconstruction and \(\widehat F\) for the lifted update, avoiding the source notes' conflicting uses of \(\Phi\). Reserve \(\kappa\) for the unit phase multiplier; use \(N_\Omega\) for observer norm. Distinguish native phase from observer angle, \(A_{ij}\) from relative phases \(\eta_i\), raw chirality from coherence, complex prestage \(\widetilde\Omega\) from decoded vectors \(v_i\), and support axes from the graph matrix. Keep all source conventions traceable in the ledger.

## 5. Writing, figures, attribution, and references

Use the established project paper style, with readable theorem statements, connected proofs, an informative abstract, and a discussion grounded in the exact results. Explain the common-phase/relative-phase distinction in ordinary language before relying on compact notation. Avoid copying execution receipts into the scientific narrative.

An exact static diagram of the fixed axes and face frames is authorized if it improves understanding. A second panel may compare the already-proved symbolic phase witnesses. Generate any diagram directly from the accepted coordinates with ordinary plotting or vector tools. Label it as a static geometric/state comparison; declare any display scaling. No native trajectory, animation, invented material linkage, new shell construction, or observer advance is authorized for illustration. A useful figure is optional; no figure quota applies.

Use **Hilmir Frímann Halldórsson** as author, following the established attribution. A short acknowledgment may credit GPT for scientific direction and internal review and Codex for verification and preparation, accurately separating earlier scientific checks from this document build. Do not invent affiliation, contact information, ORCID, funding, DOI, external peer review, or publication status.

Mark the cover, PDF metadata, and README **Review draft v0.1 — awaiting GPT/author manuscript review**. State that the underlying results have project-internal acceptance. Cite the published predecessor and primary works by verified titles and stable references. Label unpublished proof notes as project research evidence. A new literature/novelty investigation is outside scope; make no unsupported priority claim.

## 6. Deliverables and proportionate document verification

Return a portable package with:

1. `NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf` — complete paper.
2. `manuscript/` — complete LaTeX source, bibliography, and any figure assets or document-only generation scripts, using relative paths.
3. `CLAIM_SOURCE_LEDGER.md` — manuscript theorem/equation labels mapped to the accepted reports and primary sources; distinguish inherited results from the accepted reconstruction and spatial deductions.
4. `evidence/phase/` and `evidence/spatial/` — byte-preserved copies of the accepted proof notes and existing helper/results, with available acceptance reviews. Preserve source identities; do not execute these helpers.
5. `provenance/` — the supplied order, compact snapshots of primary files actually relied upon, and a source manifest recording original paths/versions/hashes. Avoid deep redundant directory nesting and unrelated archives.
6. `PREPARATION_REPORT.md` — actual source access, editorial corrections incorporated, document commands/tool versions, build outcome, final PDF page count/hash, and inspection results.
7. `README.md` — paper status, contents, build instructions, and review endpoint.
8. `NATIVE_PHASE_SPATIAL_PAPER_01_REVIEW_PACKAGE.zip` — the portable review payload with a compact member/hash manifest; record the final archive checksum alongside it, outside the ZIP. Rendered inspection pages may remain in the workspace if documented.

Normal LaTeX and bibliography passes, text extraction, PDF rendering, and document/archive checks are authorized. Adapt existing document utilities in the new workspace if helpful. Keep the build independent of scientific execution.

Compile to resolve references and citations; check for missing glyphs, overflow, clipped equations/tables, and broken links. **Render and visually inspect every page of the final PDF**, including theorem blocks, figures, tables, references, and page breaks. Repair layout and inspect affected pages again; ensure the final inspected output is the delivered PDF. Record only inspection actually performed. Check package members and hashes once the final payload is assembled.

No project imports, native steps, trajectories, parameter scans, old scientific helper reruns, new numerical tests, package installation, or historical certificate/publication re-audits are needed. Document checks verify this manuscript, not new scientific claims.

If a substantive mathematical contradiction or missing assumption appears, identify its exact claim and source while completing unaffected preparation. Do not change the model or enlarge the theorem to resolve it. Routine notation, citation, and layout choices require no further author input.

## 7. Completion receipt and author checkpoint

Return the title, draft version, page count, PDF and review-package links, confirmation that the listed corrections were incorporated, a concise build/visual-inspection result, and any concrete unresolved issue.

The paper should let the author review the established phase-to-space correspondence before any named material feature is assigned to an arrow. Preserve the stationary support, close original sphere, tight-toroid distinction, and the alternatives of co-present arrangements versus rapid alternation. Standing research directions remain retained; this writing task does not activate them.

**Stop with the complete review draft. GPT reviews the assembled manuscript and discusses it with the author before a separate publication decision. No successor investigation or publication action follows automatically.**
