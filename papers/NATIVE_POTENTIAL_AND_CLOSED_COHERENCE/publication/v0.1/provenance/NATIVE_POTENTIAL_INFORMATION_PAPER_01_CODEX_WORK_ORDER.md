# Codex work order — comma correction and manuscript preparation

**Task:** NATIVE_POTENTIAL_INFORMATION_PAPER_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Status:** Author authorized the correction and paper preparation  
**Research lead and manuscript reviewer:** GPT  
**Preparation and verification:** Codex  
**Author:** Hilmir Frímann Halldórsson / pzychozen

## 1. Assignment and stopping point

Make the single authorized comma correction in the accepted minimum-information proof note. Then prepare one complete, readable mathematical paper combining the accepted results of NATIVE_ENERGY_RESPONSE_01 and NATIVE_CLOSED_INFORMATION_01.

**Working title:**

> Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map

The paper's central thread is the behavior of the existing native potential under the complete ordered map, followed by an exact economical representation that preserves that potential, the individual edge energies, and the accepted descent quantity.

Return a compiled, visually inspected PDF and its complete source/evidence package for GPT and author manuscript review. **Stop there. No Git operations, repository adoption, commit, push, release, DOI deposit, or publication is authorized by this order.**

The two mathematical investigations are already accepted. This is manuscript preparation and one editorial correction, not another research round. Resolve ordinary wording, notation, citation, compilation, and layout issues autonomously within the accepted content. Do not ask the author to supervise routine preparation.

One manuscript review is required before publication because the assembled paper's statements, dependencies, presentation, and rendered pages have not yet been reviewed. The review is to assess the concrete manuscript, not automatically reopen the accepted investigations.

## 2. Environment and output location

Use the Windows source of truth and Command Prompt:

~~~bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
~~~

Use the installed document toolchain and the existing Python environment where useful for ordinary file/provenance work. Do not install packages or change the environment.

Read repository sources in place. Create all manuscript outputs in the fresh external directory

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PAPER_01
~~~

If that directory already contains work, use a new dated suffix and report its exact path. Keep build products, rendered inspection pages, and temporary manuscript files inside the new workspace.

The one existing-file edit permitted by this order is the comma deletion specified in Section 3. All other accepted research outputs, published editions, repository files, and runtime code remain inputs.

Read any applicable local workspace guidance. Normal LaTeX compilation, bibliography/reference passes, PDF rendering, and page inspection are authorized. These build operations must not import project runtime modules or invoke scientific helpers.

## 3. Exact correction and its receipt

Target the original local note:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_CLOSED_INFORMATION_01\
  NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md
~~~

In Section 5, equation (24), replace exactly

~~~tex
F_{\mathcal R}^{,n}
~~~

with

~~~tex
F_{\mathcal R}^{n}
~~~

This is a one-byte ASCII comma deletion. Preserve every other byte, including encoding and line endings.

Before editing, copy the original bytes into the new paper workspace's provenance/originals directory. Record the original SHA-256, make the exact replacement at its single occurrence, and verify that the corrected bytes equal that original with only the specified comma removed. Record the corrected SHA-256 and a minimal before/after excerpt in PREPARATION_REPORT.md.

The submitted copy accepted by GPT had SHA-256:

~~~text
d5fee37a95210dba6bfc0e62a378c5906f5d1a4373aa7e2e9b66a681800fb02a
~~~

Treat this as the submitted-copy identity, not an assumption about the current local file. Record any mismatch; never overwrite local changes with the uploaded copy. If the local note has unreviewed substantive changes, use the accepted copy for the manuscript and identify the discrepancy.

If the exact typo is already corrected, report that and make no replacement. If its location or multiplicity is ambiguous, leave that file untouched, report the exact issue, and complete the manuscript using the accepted corrected formula. Do not broaden the replacement.

Do not edit either prior GPT acceptance record or either symbolic helper/result file. The old accepted hash continues to identify the pre-correction copy; the corrected note receives its own identity. No scientific rerun is needed for this correction.

## 4. Governing sources and accepted status

### Newly accepted work to present

Use the complete notes and existing supporting files in these two external directories:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_ENERGY_RESPONSE_01\
  NATIVE_ENERGY_RESPONSE_01_PROOF_REVIEW.md
  exact_algebra.py
  exact_algebra_results.json

C:\TORMENT\TRIOCTAGON_new\research\NATIVE_CLOSED_INFORMATION_01\
  NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md
  exact_algebra.py
  exact_algebra_results.json
~~~

NATIVE_ENERGY_RESPONSE_01 is accepted for Target A, Target B, the diagonal-balance comparison, and the finite-step coherence identity. NATIVE_CLOSED_INFORMATION_01 is accepted for reconstruction, the exact retained domain, autonomous evolution, energy/descent retention, and both minimum-count statements. Its only recorded editorial issue is the comma above.

The accompanying acceptance records are:

- NATIVE_ENERGY_RESPONSE_01_GPT_REVIEW.md.
- NATIVE_CLOSED_INFORMATION_01_GPT_REVIEW.md.

Use supplied/downloaded copies if available; they may be in Downloads rather than the research folders. This order records their operative decisions, so the absence of a separately downloaded acceptance file is not a new scientific prerequisite. A bounded filename search of the named research folders and Downloads is sufficient; do not ask the author to rediscover archives.

### Inherited primary sources

| Source | Required role |
| --- | --- |
| papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex | Native map, potential normalization, admitted branch, amplitude/phase response definitions. |
| papers/NATIVE_RESPONSE_GEOMETRY/manuscript/spectral.tex | Positive-triad spectral facts and the diagonal-balance distinction used in the accepted local argument. |
| papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex | Adopted decoder and transport, fibre criterion, regular complex-coherence and real-Gram closure, native zero-stratum limitation. |
| papers/NATIVE_RESPONSE_GEOMETRY/provenance/THEOREM_LEDGER.md | Existing claim classifications and their limits, where needed. |
| papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex | Sections 6–7: invariant coherent domain, positive prestages, phase-stage lemma, unique aligned profile. Also use its established paper style and author attribution as a formatting reference. |

The NRG accepted reading edition is

~~~text
82cab10cbe550f58c43163fb8b05fabdad1b05ae
~~~

The coherent-relaxation accepted reading edition is

~~~text
7cc1fa03af589818bcdcfaaac51838cc36c84253
~~~

These identify reading editions, not a checkout instruction or a claim about current HEAD. Use precise theorem/equation labels and verified bibliographic metadata from the sources. Cite published works using their actual titles and known stable references. Do not invent a DOI, publication date, external review status, or public URL for an unpublished research note.

Only read runtime definitions as text if needed to resolve a specific notation or stage-order question. The accepted proof notes already identify those passages.

## 5. Mathematical content that must survive manuscript preparation

### A. Native map, potential, and notation

Define the complete ordered triad map and the existing potential explicitly. Preserve

\[
v=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL\Omega,
\qquad L=\mathbf1\mathbf1^T-3I,
\]

followed by the simultaneous native phase kicks and phase multiplication. Retain the native Arg0(0)=0 convention and the lambda-zero bypass.

Use the original edge-once normalization

\[
\mathcal V(\Omega)=
\epsilon\sum_i\left(\frac{|\Omega_i|^4}{4}
-\frac{k_i|\Omega_i|^2}{2}\right)
+\frac g2\sum_{i<j}|\Omega_i-\Omega_j|^2.
\]

Explain that the prestage increment is the negative real-coordinate gradient of this scalar. Descent of the complete synchronized map requires the accepted additional arguments.

Keep response matrices distinct from complex coherence. In particular, use visibly different notation for the response matrix and
\(\mathcal H=\Omega\Omega^\dagger\); distinguish the amplitude-response matrix from the signed pair areas \(A_{ij}\).

### B. Local theorem and diagonal-balance comparison

Present the accepted strict local descent theorem at an admitted positive in-phase branch, with \(g>0\), the specified continuation/stability hypotheses, and strict amplitude and quotient-phase multipliers inside the unit disk.

Include the actual potential Hessian, the full ordered derivative, the quotient-phase decrement, a legitimate complement to common phase, and the nonlinear remainder argument. A quadratic sign calculation alone is not the finished theorem.

Preserve the accepted distinctions:

- The local neighborhood is established by existence; no explicit radius or maximal basin is supplied.
- The common-phase direction is neutral, and the phase potential form is positive on the quotient while singular on the full phase space.
- A Euclidean sum-zero complement must not be assumed invariant without justification.
- Failed positive diagonal balance can coexist with local potential descent along the admitted sufficiently small weak branch when the stated leading coefficient is nonzero.
- An unspecified asymptotic interval does not certify a particular finite heterogeneity.
- Diagonal balance, general positive-definite symmetrization, stability, and potential descent remain distinct claims.

Use the accepted proof rather than introducing a new metric or stability criterion.

### C. Finite-domain descent and equality

Keep this theorem separate from the local theorem's hypotheses. Use exactly

\[
\epsilon=\frac1{10},\quad g=\frac1{60},\quad
\lambda=\frac1{300},\quad
k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right)
\]

on the entire closed domain

\[
\mathcal D=\left\{\Omega:
\frac9{10}\le|\Omega_i|\le\frac{11}{10},\
\text{ordinary phase width}\le\frac{\pi}{12}\right\}.
\]

State the inherited invariance and positive-prestage bounds with their source. Present the accepted proof of

\[
\mathcal V(F\Omega)-\mathcal V(\Omega)
\le-\frac{16869}{20000}\|v-\Omega\|_2^2.
\]

Retain the convex product-of-disks argument for the full prestage segment, the Hessian upper bound \(3131/10000\), and the accepted phase-stage nonincrease of each pair distance. Do not assume that an annulus is convex.

Equality in monotonicity is exactly the accepted fixed circle
\(\{e^{i\theta}r_*\}\), with \(r_*\) unique in the specified amplitude cube. The coefficient is a valid bound, without an optimality claim. It multiplies the squared prestage displacement; it is not a percentage decrease or a bound using the complete displacement \(F\Omega-\Omega\).

Do not turn this into a new classification of equality in every intermediate estimate.

Include the accepted finite-step pair-coherence identity as a short lemma or appendix. With \(d_{ij}=\delta_j-\delta_i\), preserve

\[
S_{ij}^+=\widetilde S_{ij}\cos d_{ij}
-\widetilde A_{ij}\sin d_{ij},
\]

and the corresponding edge-once formula for \(\mathcal V(F\Omega)-\mathcal V(v)\). Explain that this identity by itself supplies no global sign; the accepted local and sector arguments supply their respective conclusions.

### D. Closed coherence coordinates and energy retention

On that same \(\mathcal D\), present

\[
y=(s_1,s_2,s_3,A_{12},A_{13}),\qquad s_i=|\Omega_i|^2,
\]

with the accepted positive-root reconstruction, the remaining-pair formulas, and common-phase fibres. Cover closed boundaries, zero areas, coincident phases, equal amplitudes, and aligned/rank-one real-Gram states.

Give the exact image \(\mathcal Y=\mathcal R(\mathcal D)\), including the joint span condition on the two principal arcsines. Separate area bounds alone do not define this image.

Preserve

\[
C_{ij}=\overline{\Omega_i}\Omega_j=S_{ij}+iA_{ij},
\qquad \mathcal H=S_G-iA_G.
\]

The inherited coherence update uses the \(ji\) entry to reconstruct the native phase kick. Show the induced map, representative independence, semiconjugacy, and invariant image. Explain that the accepted domain supplies persistent nonzero prestages and hence repeated mathematical iteration.

Retain every individual matched edge energy, the same potential, and

\[
\widehat{\mathcal B}(y)
=\operatorname{tr}(N\mathcal H N^T)
=\operatorname{tr}(NS_GN^T)
=\|v-\Omega\|_2^2,\qquad N=M-I.
\]

Transfer the accepted inequality and the monotonicity-equality tuple

\[
y_*=(r_{*,1}^2,r_{*,2}^2,r_{*,3}^2,0,0).
\]

Distinguish this algebraic representative from recovery of the original common phase or its accumulated native advance.

### E. Attained minimum counts

State the optimization class explicitly: all three intensities are always retained, and additional entries are selected from

\[
\{S_{12},S_{13},S_{23},A_{12},A_{13},A_{23}\}.
\]

The objective jointly requires autonomous evolution and retention of the potential, all individual edge energies, and the prestage-increment norm throughout \(\mathcal D\). A complex entry counts as two real entries.

Include the accepted static within-domain witnesses excluding zero or one entry, and the shared-anchor witness excluding every two-real-entry selection. Keep the original labelled unequal \(k\) fixed. The lower bounds are failures of current energy retention; they do not establish dynamic nonclosure of every rejected tuple.

State both attained minima:

- Two additional entries in the full dictionary, attained by \(A_{12},A_{13}\).
- Three additional entries in the real-only dictionary, attained by the full real Gram.

Explain why signed areas can use fewer raw entries while retaining orientation that the real Gram discards. This is a restricted entry-count theorem, not a minimum over arbitrary encodings or the coarsest sufficient energy quotient. No classification of all mixed two-entry subsets is needed.

## 6. Paper organization and exposition

Use a single scientific narrative rather than joining two execution reports. A suitable organization is:

1. Question, motivation, and precise contributions relative to the existing papers.
2. Native map, potential, notation, and a compact table of the distinct theorem settings.
3. Local potential descent and the diagonal-balance comparison.
4. Explicit finite-domain descent and equality.
5. Closed coherence coordinates, their exact domain, and autonomous evolution.
6. Energy retention and transfer of descent.
7. Minimum raw-entry counts and real-only comparison.
8. Interpretation, limits, and relation to the standing programme.
9. Concise appendices where algebra or source/provenance detail would interrupt the argument.

The central new proofs must be readable in the paper itself. Cite inherited theorems with enough hypotheses for readers to assess their use. Clearly distinguish new accepted deductions from already published closure, invariance, convergence/profile, and response results.

Include a compact comparison table for the retained representations. Figures are optional: use only an exact explanatory schematic if it adds information. New simulation plots, fitted diagrams, or numerical state histories are unnecessary.

Use plain explanations before long derivations. Explain what the signed areas retain, why real cosines leave an ambiguity, and what an autonomous retained description means. Avoid padding to a page target and keep process logs out of the main mathematical narrative.

Use the author's established name and the project's actual attribution conventions. Label the document **review draft v0.1**. State that the underlying results have project-internal mathematical acceptance and that this assembled manuscript is awaiting GPT/author review. Do not copy publication-approved wording from an earlier paper's cover. No external peer review is claimed.

## 7. Scope and author checkpoints

The task authorizes manuscript writing, the exact comma deletion, ordinary algebraic/notation reconciliation, citations, file copying and provenance, document compilation, and visual inspection.

It does not authorize native-step evaluations, new trajectories, profile/root solves, parameter searches, old scientific helper reruns, observer advances, larger-ring investigations, or a new common-phase reconstruction task. No new physical identification, geometry, control law, or model component is part of this paper.

Preserve the distinctions among the mathematical potential, intensities, matched transported squared differences, physical energy, and pose/flux interpretations. The 15-degree coherent domain is not the separate 60-degree finite-return sector or a spatial cone angle.

The channel anchor is bookkeeping. The supporting 180-degree line remains stationary. Existing native, decoded-face, and observer evolution retain their established meanings; an unproved physical correspondence does not erase them.

If preparation reveals a substantive contradiction or a missing hypothesis that changes an accepted claim, identify the exact source passages and finish unaffected preparation. Report the affected passage as unresolved; do not silently repair the model, enlarge the domain, or launch another investigation. Ordinary exposition or transcription defects should be fixed within this order.

The current authorization covers this paper. The standing common-phase, spatial/Z/fixed-support, outer-geometry, and legitimate SRG directions remain later discussion items. Gravity–magnetism coupling remains linked; the TORMENT/intelligence/memory/games/embodiment programme remains parallel. Three-Way stays parked.

## 8. Deliverables and proportionate verification

Return one complete review package containing:

| Deliverable | Required content |
| --- | --- |
| manuscript/main.tex and required source assets | Complete editable LaTeX, bibliography or equivalent references, and any actually used figures/tables. Build independently from the new workspace; no imports of scientific runtime code. |
| NATIVE_POTENTIAL_AND_COHERENCE_v0.1_REVIEW.pdf | The compiled review draft corresponding exactly to the final source. |
| CLAIM_SOURCE_LEDGER.md | Main theorem/proposition claims mapped to manuscript labels, accepted proof-note sections/equations, and inherited primary-source labels. Distinguish inherited inputs from accepted new deductions. One ledger is enough. |
| PREPARATION_REPORT.md | Exact correction receipt; source provenance; final build command and tool versions; PDF page count; reference/layout checks; remaining issues, if any; exact output paths and PDF/source-file hashes. Report the archive hash separately as described below. |
| evidence/ and provenance/ | Namespaced copies of the two accepted proof notes and their existing helpers/results, plus the untouched before-copy and corrected-note identity for the comma edit. Include supplied GPT reviews when available. |
| README.md | Short scope/status explanation and exact build instructions. Explain that scientific evidence helpers are archival and are not part of the document build. |
| NATIVE_POTENTIAL_INFORMATION_PAPER_01_REVIEW_PACKAGE.zip | The portable final source, PDF, ledger, preparation report, and the small supporting evidence set. |

Keep the two helpers and result files in distinct task subdirectories so identically named files cannot overwrite one another. Copy them without execution. Portable references should point to the packaged copies or verified published sources, not depend on Windows-only links in the paper.

For the archive hash, compute it after packaging and report it in the final return or a small adjacent checksum file; do not make the archive contain a report that claims its own final hash. Temporary rendered page images need not be included in the review archive.

Compile with the installed toolchain until citations and cross-references resolve. Inspect every PDF page for clipped equations, table overflow, broken glyphs, misleading line breaks, blank pages, running-header collisions, and legibility. Repair ordinary layout defects and rebuild as needed. Inspect the affected pages after the final repair and perform a complete final page pass.

Compare the final theorem statements and central formulas with the accepted notes. Check the domain/parameter table, local-versus-finite hypotheses, matrix sign conventions, coefficient \(16869/20000\), prestage norm, equality wording, and restricted minimality class. Verify the single-edit byte relationship for the correction. These targeted checks and document-build checks are sufficient; no new scientific test suite or rerun is requested.

If a required installed rendering/build tool is unavailable, report the exact limitation and deliver the completed source and available build result. Do not claim PDF visual verification that was not performed, and do not install a replacement environment without authorization.

## 9. Final return

Report:

1. Whether the comma was corrected or had already been corrected, with its receipt location.
2. The exact paper title, review-draft version, PDF page count, and output directory.
3. Links/paths to the PDF, source archive, claim/source ledger, and preparation report.
4. Whether all manuscript checks passed and any precise remaining issue.
5. Confirmation that the task ended at manuscript preparation and did not perform scientific reruns or Git/publication actions.

**Return the review package to GPT and the author. Do not push directly. Publication will be a separate concrete decision after the finished manuscript has been reviewed.**
