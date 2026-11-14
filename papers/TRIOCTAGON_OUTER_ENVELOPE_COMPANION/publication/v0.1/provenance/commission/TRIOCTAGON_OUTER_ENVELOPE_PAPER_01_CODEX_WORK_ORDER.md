# TRIOCTAGON_OUTER_ENVELOPE_PAPER_01 — Codex manuscript work order

**Date:** 14 November 2026, Atlantic/Reykjavik.  
**Author:** Hilmir Frímann Halldórsson (pzychozen).  
**Scientific steering and internal acceptance:** GPT.  
**Assigned worker:** Codex — manuscript preparation and document verification.  
**Authorization:** the author's present instruction commissions this paper. Scientific acceptance of O01–O04 is complete at its stated scope. Manuscript review and any publication remain separate.

## 1. Deliverable and stop condition

Write a focused, self-contained companion manuscript:

**Noncollision Facet Transition and Exact Outer-Envelope Classification in the Folded Tri-Octagon**

Subtitle: **A companion to Spherical Edge Extensions of the Folded Tri-Octagon: Exact Incidence Events, Natural Terminations, and Convex Envelopes**.

Research manuscript v0.1. Target approximately **10–14 readable pages including references**, with a compact technical appendix for the plane representatives. This is a planning range, not a hard cap: preserve proof clarity and readable tables rather than squeeze typography. No decorative cover or long administrative introduction is required.

Final PDF name: `TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf`.

The contribution is the noncollision facet event and complete **closed A–B** face-lattice classification. Cite and reuse the original shell, source labels, coincidence theorem, symmetry and endpoint hulls as inherited. Do not rewrite the parent paper or commission another geometry investigation.

**Stop after delivering the actual manuscript, editable source and verified review package.** No commit, push, tag, release, DOI, branch/worktree creation, catalog insertion, repository adoption, application implementation or physical-boundary choice is authorized. Do not run any old or new scientific suite as part of authoring.

## 2. Controlling sources and historical status

Read the present order, then:

- `evidence/outer_envelope/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_REVIEW.md` and `GPT_ACCEPTANCE.json`;
- `evidence/outer_envelope/submitted/PROOF_REPORT.md`, `RESULT_SUMMARY.md`, `CLAIM_LEDGER.json` and `PRIOR_WORK_COMPARISON.md`;
- the present `MANUSCRIPT_BLUEPRINT.md`, `SOURCE_CLAIM_GUIDE.md` and `CLAIM_CROSSWALK_PLAN.json`;
- exact primary source texts and saved geometry/certificate records identified by the guide.

The accepted investigation and internal scientific review are dated **13 November 2026**. This manuscript commission is dated **14 November 2026**. Use the actual drafting/build dates; do not backdate an execution. Preserve the historical source statements, including pending-review fields in the original investigation and `manuscript_commissioned: false` in the earlier acceptance. This work order supersedes only the absence of a writing assignment. Record the change of stage in a separate current-status file.

Visible manuscript status:

> Accepted mathematical investigation; manuscript and author review pending. Project-internal research manuscript, not externally peer reviewed.

The author supplies authorship and geometric/research direction; GPT supplies scientific steering and internal review; Codex supplies investigation, verification and manuscript preparation. Separate mathematical acceptance, manuscript review, author approval and repository publication. Do not imply formal proof-assistant certification, external peer review, a journal acceptance or worldwide novelty.

## 3. Frozen object and exact result

Retain the source's actual folded geometry and label convention. For positive panel width w, let

\[
h=\frac{\sqrt2-1}{2}w,\qquad x=t/w,\qquad
A=\frac12,\quad B=\frac{1+\sqrt2}{2},\quad T=\frac{3(\sqrt2-1)}2.
\]

Here A and B denote the dimensionless endpoint parameters associated with Crossings A/B; T is the transition parameter, not time and not the historical scalar pi*e*phi. Define them before use. An explicit notation substitution `x_*` for T is allowed in the new manuscript, with a source-to-manuscript crosswalk; never rewrite historical files.

For each of the 21 original edge lines,

\[
m_e=(v_i+v_j)/2,\qquad u_e=(v_j-v_i)/(2h),\qquad
p_{e,\pm}(x)=m_e/w\pm x u_e,\qquad
H(x)=\operatorname{conv}\{p_{e,\pm}(x)\}.
\]

The centered physical vertices v_i have the source material indexing. Edges E01–E21 are the lexicographically ordered undirected endpoint pairs; plus goes from the lower to the higher V-index. Preserve all 42 labels even where endpoint positions coincide. `p` is dimensionless physical-frame position. `H` is the declared mathematical convex envelope, not the original open shell or a material wall.

State the inherited identities and premises needed here:

\[
|u_e|=1,\quad m_e\cdot u_e=0,\quad |m_e|^2=w^2/3,
\qquad |p_{e,\pm}(x)|^2=1/3+x^2.
\]

All 42 positions are distinct on `(A,B)`. At each endpoint 42 labels occupy 18 positions. The common-sphere exposed-point argument gives a hull vertex at each distinct position. The hull is full dimensional; summarize the seam-tetrahedron justification. Do not present these inherited facts as newly discovered.

The complete partition and accepted counts must appear, with **true polygon edges and maximal supporting facets**, not rendering triangles:

| Domain | V | E | F | Facet sizes |
|---|---:|---:|---:|---|
| A, inherited endpoint | 18 | 48 | 32 | 32 triangles |
| A < x < T | 42 | 96 | 56 | 36 triangles, 18 quadrilaterals, 2 hexagons |
| x = T | 42 | 84 | 44 | 24 triangles, 12 quadrilaterals, 8 hexagons |
| T < x < B | 42 | 90 | 50 | 24 triangles, 24 quadrilaterals, 2 hexagons |
| B, inherited endpoint | 18 | 36 | 20 | 8 triangles, 12 quadrilaterals |

The new statement is **exactly one interior change of the labelled maximal-face lattice**, at T, where all 42 exits stay distinct. Its exact expressions are

\[
t/h=3,\qquad 4T^2+12T-9=0,\qquad
R_*^2/w^2=\frac{85}{12}-\frac{9\sqrt2}{2}.
\]

The sphere radius and along-line distance are different quantities. Do not describe `56 -> 44 -> 50` as the endpoint facet counts. Both endpoints retain their inherited coincidence events.

## 4. Required proof exposition

The paper must explain the mathematical argument without making the reader execute the archive. PASS flags, hash totals, a plot, Euler's formula or three sample hulls are not a proof.

### 4.1 Contribution and inherited premises

Provide a short source/contribution table. O01 is accepted bounded documentary concordance, **not a new mathematical theorem or external novelty review**. O02 is the exact noncollision event; O03 the complete interval classification and endpoint attachment; O04 the local regrouping and scoped facet-size consequence. Preserve all four ledger records in the manuscript crosswalk.

Keep the accepted shell and midpoint/direction construction, finite D3h symmetry, line-coincidence catalogue, same-sphere exposed-point argument, original minimum ball, endpoint A/B hulls, and three-term silver-ratio relation on the inherited side. The source comparison is already complete; do not run another broad search to rediscover it.

### 4.2 Calculation chart and geometry identity

Explain the calculation-only change `(X,Y,Z)=(p_x,p_y/sqrt(3),p_z)`, which puts coefficients in `K=Q(sqrt(2))`. It preserves convexity, incidence, supporting halfspaces and polygon boundary order, but is **not a Euclidean isometry**. Physical squared norm is `X^2+3Y^2+Z^2` for dimensionless p. Use physical coordinates and equal spatial scales in illustrations. Never infer angles or lengths using the unweighted transformed norm.

State the exact serialization convention `[a,b] = a+b sqrt(2)` and ascending-power polynomial arrays where explaining the certificate. Empty arrays mean zero polynomials. Distinguish physical-plane coefficients in the candidate calculation from transformed-chart coefficients in the orbit appendix.

### 4.3 A concrete supporting-face transition

Give the accepted candidate plane in dimensionless physical coordinates, with `h1=(sqrt(2)-1)/2`:

\[
n(x)=\left(0,-1,\frac{\sqrt3}{2}(x-h_1)\right),\qquad
 d(x)=\frac{\sqrt6}{4}x^2+\frac{\sqrt6-\sqrt3}{4}x+\frac{\sqrt3}{24}+\frac{\sqrt6}{16}.
\]

Four persistent zero labels are E05+, E09+, E17+, E16-. For each of E21+ and E10-, the residual is

\[
n(x)\cdot p-d(x)=-\frac{\sqrt6}{4}(x-T)(x-B).
\]

Explain its negative sign on `(A,T)` and positive sign on `(T,B)`. This sign reversal does not by itself establish the full family; it motivates the exact local event and must be followed by complete support and global completeness.

At T show the full zero set in outward cyclic order:

`(E05+, E16-, E21+, E09+, E17+, E10-)`.

Use the complete residual table to establish that every other label is strictly inward, the normal is nonzero and the zero set is a maximal hexagon, not arbitrary coplanarity. Explain how inherited noncoincidence and the verified side tests prevent degeneracy. The actual group action yields six such hexagons; two other cap hexagons persist. **Do not call the six new hexagons regular.**

### 4.4 Parameter-uniform exact certification

For each face, define

\[
N=(b-a)\times(c-a),\quad D=N\cdot a,\quad r_l=N\cdot p_l-D.
\]

State the certificate requirements: nonzero N; exactly the declared zero set; strict inward sign for every other label; and strict cyclic side tests

\[
N\cdot((b-a)\times(c-a))>0
\]

for each consecutive edge `(a,b)` and every other face vertex c. Explain why these certify the genuine convex polygon boundary, not triangulation diagonals. Plane/residual degrees and side-test degrees should agree with the accepted report (at most two/three/four respectively). Treat persistent coplanarity as a zero polynomial, not an isolated event.

Explain exact signs over the ordered quadratic field. In the submitted method, endpoint factors are divided out before Sturm counting, and a midpoint sign together with absence of any interior root proves a strict chamber sign. Even-multiplicity interior roots must not be missed. Endpoint zeros are allowed for an open chamber; T and A/B are treated separately. No statement is inferred merely from floating nominations.

Include the independently organized reviewer verification as recorded evidence, not a new authoring computation: a separate algebraic-field backend with exact Bernstein-positivity certificates, without imports from the submitted arithmetic/geometry engine. Briefly explain the positivity principle on the open unit interval and that the saved checks needed no subdivision. Do not present this as formal verification or independence of all trusted assumptions. The original generator/checker share an engine; the reviewer replay of that engine and the separate reviewer implementation are distinct evidence layers.

### 4.5 Completeness and uniqueness of the interior transition

Supply a readable lemma/proof of the actual completeness argument:

1. Exact support, full zero sets and strict cycles make every listed polygon a true maximal facet of the full-dimensional hull.
2. Each certified side is a true ridge. The recorded incidences contain two distinct listed facets at each such ridge.
3. In a three-dimensional convex polytope a ridge has exactly two incident facets; explain using a small transverse convex-angle section.
4. Its facet adjacency graph is connected; explain using the source's boundary/sphere path argument.
5. A nonempty true-facet list closed under actual adjacency is therefore complete.

Apply the argument at every parameter in each certified chamber and at T. Constant zero-label sets and verified cyclic orders determine the entire labelled face lattice, not just its V/E/F counts. The differing lists at T and their constancy in both chambers establish the unique **interior combinatorial** transition. This does not prohibit an unrelated metric equality or a nonsupporting coplanarity inside a chamber.

Provide compact orbit representatives with exact planes, complete cyclic zero sets and orbit sizes (26 representatives across C1/T/C2) in a readable appendix or accompanying readable supplement clearly linked by the paper. Prefer an appendix if it fits without tiny text. All full facet records, residual polynomials and permutations must remain in the electronic evidence, even when abbreviated in print. Do not perform new all-triples or all-quadruples enumeration.

### 4.6 Local regrouping and endpoint limits

Explain the six copies of the local change:

**two triangles + one quadrilateral -> one maximal hexagon -> two quadrilaterals**.

Use the actual branch-label lists and side identities from the accepted transition record. Thirty-eight facets retain their **branch-label sets**; do not claim their coordinates or metric shape stay fixed. Twelve chamber edges disappear at T and six different edges appear after T. The event edge set is exactly the intersection of the two chamber edge sets. These are derived hull adjacencies, not edits to the original 21-line network.

Contrast this with A/B, where labels coincide. Show the saved endpoint-limit table: C1 to A has 32 two-dimensional face images, 18 edge images and six point images; C2 to B has 20, 24 and six respectively. Every inherited endpoint facet is covered exactly once by a full-dimensional image with its exact vertex set. At T all chamber faces retain dimension two, with affected ones sharing a larger maximal supporting zero set. Counts alone must not stand in for the recorded label correspondence.

### 4.7 Scope consequence

The complete face-size list establishes **no ten-vertex maximal facet in the closed A–B convex-envelope family**. It does not exclude decagonal sections, projections, subsets, other enclosures or a separately adopted prism; symmetry alone was not the proof. Do not turn the result into a universal absence of golden-ratio relationships.

State that common positive scaling and reflection of the whole source construction transfer the result to the stated widths and hands, retaining labels and correctly transformed normals/cycles. Parameter variation is not time, shell breathing, a moving-support law, a force, an energy account or a native trajectory. T is not a fourth supporting-line coincidence or an extension of the finite silver-ratio sequence. Original-to-A and beyond-B remain outside this paper; do not silently open those investigations.

## 5. Presentation and figures

Use the preserved three-panel `local_facet_transition.svg` or PNG. Keep both original files byte-identical in the evidence. A vector-to-PDF conversion for embedding is allowed as a newly named documentary derivative, with source and output identities; it is not a new scientific calculation. Do not rerun the old figure script, import its mathematical modules or rerender geometry from scratch.

Caption the three panels accurately: `x=3/5`, `x=T`, `x=2/3`, with normalized physical coordinates and a common camera/scale. Define "before/after" as parameter order rather than elapsed time. Identify drawn diagonals as hull edges when present, not source-line rewiring. Check all branch labels at the final print size.

One additional purely documentary interval schematic is optional; if used it must be drawn from the already saved exact partition and counts, labeled schematic, without new hull computation. Do not invent new 3D views or use generative imagery for mathematical evidence. One good original figure and clear tables are enough.

Use legible body type and equations, sensible margins, repeated headers for any long appendix table, sufficient contrast and searchable text. No tiny all-fraction dump. Ensure long filenames and evidence links wrap without obscuring text. Do not append historical PDFs merely to inflate the page count.

## 6. What may run — and what may not

### Permitted documentary operations

- Raw-byte checksums, safe archive reads/extraction, source inventories, comparison of retained files and current copies.
- Reading saved JSON/Markdown/TeX, transcribing saved exact values and checking that the manuscript's tables and formulas match their source records.
- Document-only table generation or formatting, image-format conversion, bibliography/label/link checks, LaTeX build, font/text/page inspection and packaging.
- A narrowly needed read of an exact existing source for a bibliographic field; no broad external novelty search or new scientific premise. Use supplied metadata where sufficient.

### Not authorized

- Running/importing the original generator, scientific checker, rejection controls, geometry engine, source-collection scripts, reviewer exact/Bernstein scripts or historical suites.
- Any new hull nomination, parameter scan, root search, certificate regeneration, proof replay, native trajectory, refinement outside A–B, decagon/golden-ratio fitting or changing the accepted answer.
- Kernel, UI, TORMENT, production data, dependency or repository changes; no network-driven installs or environment upgrades.

Saved historical commands may be documented for readers to reproduce later in a fresh copy. They must be clearly distinguished from what the authoring run actually executes. New authoring helpers must not import scientific modules just to read stored data. A contradiction found during transcription is a scientific blocker to report, not permission to silently fix accepted claims or expand the assignment.

## 7. Windows workspace, preservation and statuses

Use Windows Command Prompt and the existing `torment` environment; record actual versions. Keep all work in a fresh external short workspace such as `C:\TORMENT\OE_PAPER_01\run_YYYYMMDD_01`. Keep the original Downloads, prior runs, accepted inputs and repository untouched. Avoid long nested Windows paths by choosing a short base, not by dropping provenance or editing global Git/OS settings.

The source checkpoint `46bf10808b8694476b61b359be305a66a46d4614` is a historical reading identifier, not an instruction to reset a checkout, a demand to update main, or a claim of present remote state. This packet already contains the needed source bytes. No Git operation is needed for normal manuscript preparation. If preservation evidence is collected from the existing checkout, it must be bounded, read-only and must leave its index, HEAD, branch, unrelated edits and files unchanged.

Carry the complete acceptance extraction and intact archive into the review delivery. `PRESERVED_INPUTS.json` must map incoming relative paths to delivered relative paths with raw-byte hashes. Preserve CRLF and LF exactly in inherited files. In particular hash **raw bytes**, not decoded text after line-ending normalization. New document files may have a consistent line-ending policy, explicitly recorded.

Do not rewrite historical dispositions. Add new `CURRENT_STATUS.json` and a short `HANDOFF.md` explaining: accepted mathematics; author-commissioned manuscript; actual manuscript and author review pending; no publication. Date and identify the actual final PDF.

## 8. Claim crosswalk, build and page inspection

Create `MANUSCRIPT_CLAIM_LEDGER.json` mapping every O01–O04 record to actual final manuscript section/equation/theorem/table/figure labels and PDF pages, plus exact proof/evidence paths. Map inherited premises separately so they are not counted as newly proved. The supplied crosswalk plan is a drafting aid, not a completed crosswalk or predetermined final numbering.

Transcription checks must cover the five-row V/E/F table and facet histograms; exact partition/T identities; representative label sets; plane/residual formulas; six/38/12/6 transition counts; endpoint image counts; all printed orbit sizes/coefficients; and the appropriately separated historical verification counts. The supplied certificate/record is the source; formatting helpers do not recertify the theorem.

Build the final manuscript from the actual delivered editable sources in external staging using an existing compatible compiler/cache. Record command, environment, exit status, source raw hashes and PDF hash. Resolve every reference/citation. Check PDF page count, selectable text, embedded fonts, metadata, no missing glyphs, no clipped equations, no unintended blank pages, and any overflow/compiler warnings. Inspect every final page as a rendered image, including references and appendix; record page-specific observations tied to the exact final PDF SHA-256. Any source change after that requires rebuild and renewed final-PDF inspection.

Do not distribute font binaries, compiler caches, executables, virtual environments, transient TeX outputs or unrelated private files. Embedded PDF fonts are appropriate. Preserve inspection images and actual command logs in the review package. The build guide must not promise byte-identical PDFs across different platforms/compiler/font versions.

## 9. Required review return

Return one review ZIP with a clear root and at least:

- `TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf`, editable LaTeX (`main.tex`, bibliography, tables, figure embedding assets) and document-only build/verification helpers;
- `README.md`, `BUILD.md`, `CURRENT_STATUS.json`, `HANDOFF.md`, `MANUSCRIPT_CLAIM_LEDGER.json`, `PRESERVED_INPUTS.json` and a source/evidence access guide;
- unchanged `evidence/outer_envelope/`, intact acceptance ZIP and original sidecar under `archives/`, and the new commission documents retained separately;
- final build/document/font/reference/transcription records, execution logs, every final page render and the bound all-page visual inspection record;
- a raw-byte self-excluding payload manifest covering every other ZIP member.

Recommended delivery filename: `TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip`. Alongside it return its `.sha256` file and `FINAL_ARCHIVE_AUDIT.json`. The external audit must reopen every member and check safe unique/case-unique paths, byte counts, hashes and CRC; cross-compare all preserved inputs; and confirm that standalone, archived, built and inspected PDFs are the same bytes. Keep external audit/checksum outside the ZIP to avoid circular hashes. Record member counts from the actual final package, not an estimated target.

The final message should give the page count, delivery paths, concise document-check status, exact remaining review stage, and any real blocker. State that no scientific rerun, repository change or publication occurred. Do not write a publication receipt for this manuscript return.

## 10. Acceptance criteria and escalation

A successful delivery faithfully explains the unique noncollision transition, whole closed-interval classification, true-side/ridge completeness argument, endpoint correspondences and limited no-ten-vertex-facet consequence. All four accepted claims and inherited premises are traceable; preserved records remain unchanged; the final PDF is readable and fully checked.

No new geometry decision is needed to write this note. If an actual contradiction, missing authoritative byte, unbuildable mandatory asset or materially different interpretation blocks the work, return the concrete discrepancy and bounded completed work. Do not ask the author to recover equations already in the packet, and do not fill gaps with an assumed physical meaning.

**Writing and review delivery only. Once that return is complete, stop.**
