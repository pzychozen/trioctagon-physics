# Codex manuscript work order
## NATIVE_ALTERNATING_BRANCH_CONNECTION_PAPER_01

**Issued:** 12 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Scientific steering and manuscript review:** GPT  
**Recipient:** Codex  
**Authorization:** The author has approved preparation of the next manuscript work order. This commissions the focused Paper G companion described below. It does not authorize publication or another research investigation.

# 1. Assignment and stopping point

Prepare a complete, reader-facing mathematical companion paper, its editable LaTeX, and a self-contained review package from the accepted investigation **NATIVE_ALTERNATING_BRANCH_CONNECTION_01**.

**Working title:**

**Certified Connection from Local Period-Doubling to the Captured Alternating Cycle in the Native Triad**

**Subtitle:** A companion to *Geometry-Attached Axial Observables, Period-Doubling, and Certified Entrance Capture in the Tri-Octagon Map*.

**Edition:** Research manuscript v0.1. Aim for approximately **10–14 pages including references**, with a short technical appendix if genuinely necessary. This is a planning range, not a reason to remove proof steps or squeeze typography. A complete readable proof takes priority over a page target. No separate decorative cover is required.

**Requested final PDF name:** `NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION_v0.1.pdf`.

This is documentation of accepted mathematics, not a new search, stability project, model extension, rewrite of Paper G, or re-certification of M2/M3. Return the actual manuscript for GPT and author review. Stop after the verified review delivery. **No commit, push, branch/worktree creation, release, tag, DOI, repository adoption, or catalog edit is authorized.**

# 2. Current authority and historical wording

Read these in order:

1. `accepted/NATIVE_ALTERNATING_BRANCH_CONNECTION_01_GPT_REVIEW.md`, especially Sections 1–4 and 6.
2. `accepted/GPT_ACCEPTANCE.json`.
3. `accepted/submitted/PROOF_REPORT.md`.
4. `accepted/submitted/CLAIM_LEDGER.json` and `PRIOR_WORK_COMPARISON.md`.
5. `SOURCE_CLAIM_GUIDE.md` and `MANUSCRIPT_BLUEPRINT.md` in this commission.
6. The primary Paper G source and exact input records located by that guide.

The investigation was internally accepted on **11 November 2026**, without mathematical corrections. This commission is dated **12 November 2026**. Preserve those historical dates. Date the new manuscript and actual build records honestly at execution.

The acceptance archive says that a manuscript was not yet commissioned; the original Codex return says review was pending. Those are preserved historical descriptions. This work order supersedes only the absence of a manuscript commission. It does not rewrite historical evidence, grant manuscript acceptance in advance, or grant publication authority.

Use visible manuscript status such as:

> Accepted mathematical investigation; manuscript and author review pending. Project-internal research manuscript, not externally peer reviewed.

Credit the author by full name; describe GPT scientific steering/internal review and Codex investigation, implementation, and manuscript preparation accurately. Do not call AI review external peer review or proof-assistant verification.

# 3. Frozen object and the exact contribution

The family is the existing native triad of Paper G, with

\[
\epsilon=\frac1{20},\qquad g=\frac15,\qquad
k=(1,1.2208964704604097,6.35310346037241),\qquad
\lambda=\lambda_c+\mu.
\]

The terminating decimals are exact rationals. The host \(u\), fixed orthonormal slice basis \(V\), compression \(B_0=V^TM_uV\), its larger eigenvalue \(m_1\), critical sign/normalization, and \(\lambda_c=(1+1/m_1)/9\) are the accepted objects selected by the M2 source. Give their necessary defining equations. Never substitute a displayed rounded host, midpoint, or rounded critical value as an exact premise.

State the original simultaneous amplitude/graph prestage followed by simultaneous harmonic-three phase kicks, including `Arg0(0)=0`. Keep the separate implemented lambda-zero convention correctly scoped. There is no new amplitude normalization, sequential update, new state, receiver, applied force, feedback, or physical time. The positive gauge is a coordinate representation, not an extra native update.

**Main new conclusion:** a nontrivial H-exchanged branch, smooth for each positive parameter and continuous to the host at onset, connects the M2 germ to the exact repaired M3 cycle for every

\[
0<\mu\le\frac1{200}.
\]

It is a graph over this parameter interval, with uniqueness in the certified regions only. Zero is the regularized onset anchor, not a nontrivial period-two state. At each positive parameter the quotient and full-state orbit have primitive period two; the common-phase orbit family is retained. This describes separate autonomous maps at fixed parameters, **not one orbit driven by a parameter ramp**.

**Separate new attraction conclusion:** the actual two-step quotient derivative has the verified similarity-norm bound

\[
\|Q^{-1}D\widehat F_\mu^2 Q\|_\infty<0.9601,
\qquad \frac{4999}{1000000}\le\mu\le\frac1{200}.
\]

This gives local quotient attraction / attraction modulo common phase, not a new trapping neighborhood or uniform basin. M2's sufficiently-small-positive-parameter attraction has no explicit endpoint in this investigation. M3's endpoint trap and repaired entrance at update 301 are inherited. **Attraction throughout the full connection remains unresolved.** The failed sufficient broad bounds are not evidence of instability or a bifurcation.

The main contribution is branch identity and continuation between these particular known objects. Do not claim discovery of period doubling, validated continuation, the local branch, or the endpoint cycle anew. Distinguish it from the unrelated fixed-coefficient turning-to-alignment result and its update-50 certificate.

# 4. Required mathematical exposition

The manuscript must be readable without executing a ZIP. Include the central argument, not just a citation to acceptance or a list of PASS counts. Reuse Paper G's premises instead of re-proving its whole paper.

## 4.1 Inherited premises

State the exact host-selection problem, regular slice/gauge and H involution, and the accepted M2 local branch theorem with its corrected normalization. State the part of M3 needed for identification: the unique two-step fixed point in the exact `U_plus`, its H exchange, and the scope of the endpoint entrance theorem. Distinguish the actual trap from `Um`, which is only a historical outer image enclosure.

In a compact contribution table, separate I01/I02 (inherited), N01/N02 (new connection), N03 (application of inherited symmetry to the connected family), and N04 (new narrow stability strip). Retain all six ledger records in the manuscript claim crosswalk.

## 4.2 Removable formulation and actual onset

Explain

\[
t=\mu/\nu,\quad a=\sqrt t,\quad
\xi=tX,\quad \eta=a(e+t y e_\perp),\quad\nu>0,
\]

with \(e\) the exact unit critical vector, \(e_\perp=(-e_2,e_1)\), and \(e^T\eta=a\). The normalized unknown is \((X_A,X_B,X_C,y,\nu)\); do not confuse it with the five original quotient coordinates \((\xi,\eta)\). Retain the fixed-positive-mu coordinate determinant \(t^5/(2\nu)\) and its scope.

Define \(G(z,\mu)=\widehat F_\mu(z)-Hz\) and the normalized real/imaginary equations, including the powers \(t\) and \(a^3\). Show how the harmonic sine, entire C/S expressions and positive gauge make the apparent singularity removable. The original-state prestage, normalized phase identity and gauge formulas should appear in the body or a compact appendix with clear links to the proof.

Explain exact divided differences rather than calling them truncated jets. The cancellations at zero come from the exact host equation and critical compression, not tiny numerical residuals. State the 18-term C1/S1 value and derivative tail bounds, their sufficient \(|w|\le1\) condition, and the retained squared-kick bound below 0.0823. Avoid conflating the entire C function with the channel-area vector C; add a notation distinction without altering equations.

At onset give \(X_0=w_R/2\), \(\nu_0=c_{\rm nf}/\sigma>0\), and the noncritical equation for \(y_0\). Show the full limiting Jacobian's block structure, including lower-left coupling. Its nonsingularity, the refined root, local M2 uniqueness and the uniform first patch \([0,1/25600]\) identify the actual germ. Do not assume a hand-picked numerical offset lies in M2's unknown sufficiently-small interval.

## 4.3 Uniform validation and joins

State the uniform parameter-dependent contraction lemma actually used, including a fixed rational preconditioner, weighted norm, exact box radii, center defect and strict inclusion. Explain why \(\|I-A D_xR\|<1\) establishes the nonsingularity needed to infer root equivalence and smooth dependence. A floating inverse is only a source of candidate rational coefficients.

Give the exact interval partition

\[
I_i=[i/25600,(i+1)/25600],\qquad i=0,\ldots,127.
\]

Explain separately: parameter coverage; existence and uniqueness in each patch; positivity/regularity; and root identity at the 127 shared endpoints. Both roots lie in a common convex uniqueness region. Mere overlap of boxes does not prove identity. The connector does not need its own self-map because adjacent patches already establish existence. Explain outward outer-box evaluations and which boxes contain the roots.

Use the accepted bounds (patch norms below 0.614; join norms below 0.583) only as root-equation validation bounds. They are not native dynamical rates. Include a small certificate-summary table with the source keys and exact-versus-display status. Full endpoints stay in the supplement, not in a many-page printed dump.

## 4.4 Endpoint identity and full-state lift

Explain why the refined endpoint belongs to the last patch's branch. Its entire reconstructed interval lies strictly inside the exact accepted `values.exact_receipts.Up`; an intersection, midpoint or small residual would not suffice. The accepted positive parity already lies in that box. Invoke the inherited uniqueness theorem to identify M3, without rerunning its 301-update capture.

Use \(G=0\), H equivariance and nonzero \(\eta\) to establish primitive quotient period two. State the inherited full-state calculation \(F(A)=e^{i\theta}\overline A\Rightarrow F^2(A)=A\) on the certified regular domain, with the common-phase and conjugation assumptions explicit. Sign reversal of C, W and Gamma is an inherited oddness consequence; it does not assert their nonvanishing at every intermediate parameter. No entrance theorem at other mu follows from the connection.

## 4.5 Stability is a separate theorem

Define the two-step quotient derivative and retain

\[
P=D\widehat F(Hz)D\widehat F(z)=(H D\widehat F(z))^2.
\]

Explain the rational basis Q, approximate inverse R_Q and exact inverse-defect inequality before the norm bound. State how the narrow-strip root box is identified with the continued branch. Give the exact strip endpoints and strict bound; label the longer decimal as approximate if used.

Do not treat contraction of the root-solving map as contraction of the native map. Keep the neutral common-phase direction out of the quotient contraction. Do not interpolate stable samples, claim an unproved basin, or silently join the M2 local-attraction interval to the endpoint strip. Put the unresolved full-range conclusion in the abstract, stability section and conclusion.

# 5. Presentation and evidence standards

Use the accompanying blueprint as a writing plan, not a requirement to force awkward section lengths. A theorem for the connection, an inherited-symmetry corollary and a separate narrow-stability proposition/theorem are sufficient; administrative checks are not theorems.

At most one or two technical figures are needed; none is mandatory if the tables explain the argument better. Any figure must be generated from retained data or be explicitly schematic. A parameter-interval/proof-dependency diagram must distinguish full connection coverage from narrow explicit stability coverage. An inset or a marked broken scale is necessary if otherwise the 10^-6-wide strip is invisible. Never invent a numerical size for M2's qualitative near-onset attraction neighborhood. A curve through saved approximate branch centers is illustration, not an orbit or a proof of unsampled values. No new solves or dynamics to improve a picture.

Use neutral, clear language. Say native-state/quotient branch, not physical branch. Keep mathematical parameters separate from calibrated physical units. Introduce symbols once, with a concise crosswalk where source notation collides (critical m1 versus mean m, regularized t versus update index, entire C/S functions versus channel area).

State that Paper G's earlier non-continuation limitation was accurate for its own edition and is now supplemented, not corrected. **Leave Paper G v0.1.1, its metadata, sources, proofs and all other published editions unchanged.** The new note has its own edition and status.

Cite the original Paper G title and edition, the accepted investigation, and the GPT acceptance record at their actual scope. Source record dates are historical. Repository checkpoint `035a32099605bac84bc739a94d001ab96c7c5f55` is a retained reading locator, not an instruction to reset the checkout or a claim about current HEAD. Reuse already documented bibliographic metadata; do not add outside mathematical premises or a literature-survey task.

Disclose the trusted computational basis accurately: generator and checker share the new interval/AD engine; exact Fraction comparisons are separately organized. The prior Linux GPT replay is corroboration, not a second independent interval engine or Windows execution. Five direct-form numerical spot checks were diagnostics, not interval proofs. Four rejection controls and 31 algebra/source checks are verification counts, not new theorem counts. The current manuscript task adds no scientific replay.

# 6. Allowed and excluded work

**Allowed now:** reading supplied source/evidence; drafting and editing new LaTeX; a documentary source/claim crosswalk; copying evidence without alteration; reading saved JSON to make tables; deterministic exact-rational transcription/rounding checks; generating clearly sourced presentation graphics; PDF compilation; checking references/fonts/links; rendering and visually inspecting final pages; checksums/manifests and packaging.

**Not commissioned:** new trajectories, roots, continuation, onset jets, certificate generation or replay, rejection-control reruns, broader stability bounds, searches for other branches, numerical basin studies, re-audits of earlier publications, kernel/API/UI changes, new physical interpretation, dependency installation, or repository mutations. Do not run a historical helper merely because it is retained in an archive. Do not import a mathematical script with execution side effects to make a document table; read its saved data with a new documentary helper instead.

If drafting reveals an actual contradiction, missing mathematical premise or source ambiguity, record the precise location and return the strongest accurate draft with that blocker. Do not silently change the accepted equations, manufacture missing proof, or expand the assignment to resolve full-range stability. Ordinary editorial choices need no repeated approval.

# 7. Workspace and input preservation

Use Windows Command Prompt and the existing `torment` environment for Python work:

```bat
conda activate torment
```

Read applicable local instructions. Use a fresh external research workspace, preferably a short path such as `C:\TORMENT\TRIOCTAGON_new\research\NATIVE_AB_PAPER_01\run_<actual-date>_01`, recording the actual location. Do not overwrite previous investigation runs or modify the scientific checkout. Use existing TeX tools and caches; no package installation or persistent environment change. Existing parent-paper styling may be consulted locally as a read-only reference.

The packet supplies both the frozen acceptance ZIP under `archives/` and its complete unchanged extraction under `accepted/`. The original Codex return, exact M2/M3 inputs, source manuscripts, checker/engine code, failed trials, recorded checks and reviewer evidence are included. No separate acceptance message or archive is needed from the author.

Verify the incoming packet manifest and acceptance/archive identities without executing scientific checkers. `tools/verify_packet.py` is an optional standard-library integrity-only helper. Preserve all 177 extracted acceptance members and the frozen acceptance ZIP/sidecar. Use a separate current manuscript-status record rather than editing old statuses.

For delivery, a short layout such as `evidence/branch/` for the acceptance extraction and `archives/` for the unchanged ZIP is suitable. Bind any path relocation with a manifest; unchanged bytes matter. Long copied machine-local paths in old records are provenance, not prerequisites for reading the new note. Avoid proliferating extra copies beyond the frozen archive and one accessible evidence tree.

# 8. Required delivery

Return one review ZIP and external SHA-256, plus a standalone PDF and a concise handoff. The ZIP must contain:

- Full manuscript PDF, editable LaTeX and bibliography, all actual figure/table sources and data, and build instructions/helper.
- `MANUSCRIPT_CLAIM_LEDGER.json` or equivalent mapping all I01/I02/N01–N04, assumptions, displayed bounds, theorem statements and qualifications to actual final manuscript labels/pages and accepted source sections/JSON fields. Record real locators after the final build, not planned labels.
- A readable scope/status summary identifying accepted mathematics, pending manuscript/author review, unresolved full-range attraction, and no publication.
- Full unchanged accepted investigation/review evidence, original archive and sidecar, plus preserved commission materials and a source/input inventory.
- Actual build, reference, font, transcription, preservation and final-page visual-inspection records; execution environment and commands; actual output identities.
- A self-excluding payload manifest and member-by-member final archive verification. Keep the final archive audit and external checksum outside the archive where needed to avoid circular hashes.

The external final audit must bind the exact standalone PDF to the archived and inspected PDF. Return the source package as well as the PDF; do not return only a summary or a rendered document.

# 9. Document acceptance checklist

1. Read the finished prose against the accepted proof and review, with special attention to onset, common uniqueness joins, whole-enclosure endpoint containment and stability scope.
2. Check fixed exact coefficients, host dependence, critical definition, branch parity, signs, normalization, tail bounds and strict versus non-strict interval endpoints. Every displayed decimal is either an exact rational bound or clearly approximate.
3. Check that existing mathematical results and methods are distinguished from the new connection, and no historical pending status is mistaken for a new task.
4. Compile until all equation references, theorem labels, citations, tables and internal links resolve. Record warnings honestly and repair layout warnings that affect the final document.
5. Confirm text is selectable, all fonts are embedded, mathematical glyphs render correctly, and metadata identifies the actual author, title, edition and pending manuscript status. Do not distribute font binaries or caches.
6. Render **every page of the final PDF** and inspect each page for clipping, overflowing formulas, misplaced indices, illegible tables, missing symbols, collisions, broken glyphs, blank pages and misleading plot labels. Any subsequent PDF change requires renewed inspection of the changed final artifact.
7. Verify all preserved input bytes and source links. Ensure new documentary helpers did not execute a solver, interval replay, original capture, or broad stability calculation.
8. Verify archive CRC, safe unique paths, member-by-member bytes, manifest coverage, external checksum and standalone-PDF identity. Packaging counts are not scientific counts.

**Completion message:** give the actual page count, exact file locations and the bounded statement that manuscript review remains pending. Report any unresolved blocker rather than inventing a passed check. No publication claim is appropriate.

# 10. Stop boundary

This assignment ends at the manuscript review return. The accepted M2-to-M3 investigation is complete. Full-range attraction stays an explicit open question, not a prerequisite for this note or an automatic follow-on assignment. GPT/author review and any later publication require the next disposition.
