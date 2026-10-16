# BOUNDARY-11 — GPT mathematical and deliverable review

**Date:** 16 October 2026  
**Human research author and owner:** Hilmir Frímann Halldórsson  
**Submission:** `BOUNDARY11_REVIEW_PACKAGE.zip`  
**Verdict:** **ACCEPTED_WITHIN_SPHERICAL_EDGE_EXTENSION_SCOPE**  
**Required mathematical or report corrections:** None.  
**Viewer disposition:** Embedded geometry/data verified; submitted interactive QA inspected. Independent browser navigation was blocked before loading the page, so no independent browser-control acceptance is claimed.  
**Publication/integration:** Not authorized by this review. No next experiment is started.

## 1. Basis and execution

This review reads the complete five-page report and its editable source, the exact geometry inventory, angular catalogue, pairwise coincidence evidence, polygon results, original analytical scripts as text, visualization source, and submitted QA. The mathematical basis is the unchanged Paper C construction, not a regular octagon substituted for the folded shell.

A read-only GitHub connector request retrieved Paper C v1.0.1, lines 46–155, at the already-known checkpoint `e1f5115402a05965834493c1254b03118a531c92`. Its local vertices, panel maps, welded numbering and face cycles agree with the submitted construction. This is a pinned source read, not a current-main or publication check. The two available original BOUNDARY-10 attachments also match the supplied input ledger byte-for-byte. Only a range of Paper C was fetched; its complete-file SHA-256 has not been independently rechecked here.

I independently rendered all five submitted PDF pages with Poppler at 125 dpi and inspected each page individually. Equations, tables, all three figure plates and explanatory captions are readable; no required clipping, overlap or broken-glyph correction was found. No PDF was rebuilt and no supplied figure was regenerated.

The reviewer-written `verify_boundary11.py` uses exact arithmetic in Q(sqrt(2),sqrt(3)). It reconstructs vertices from the accepted local panel maps rather than trusting the submitted coordinate table. It executed once and passed. The count of 2,056 internal assertions is an accounting detail, not a count of independent discoveries or experiments.

Review coverage:

| Population | Independently checked |
|---|---:|
| Welded vertices | 18 |
| Unique original edges | 21 |
| Labelled line/sphere branches | 42 |
| Branch-pair equations | 861 |
| Supporting-line pairs | 210 |
| Exact angular-pair coefficient records | 861 |
| Distinct symbolic angular functions | 60 |
| Supplied numerical display radii | 6 |
| Supplied display points across those radii | 252 |

No submitted Python scientific checker was run or imported. The review did execute its own exact/static geometry checks, plus the small pure JavaScript coordinate evaluator in a sandboxed Node context. It performed no dynamical evolution, random sampling, physics-kernel operation, SRG execution, source change or Git write.

## 2. Geometry and full coincidence classification — PASS

The 21 source edges separate into three seam edges, six horizontal edges and twelve chamfers. For every edge, with centered midpoint m, half-edge vector D, unit direction u, and h=(sqrt(2)-1)w/2, the exact checks give

- ||D||²=h²;
- m·D=0;
- ||m||²=w²/3.

Therefore every complete supporting line is tangent at its midpoint to the same sphere of radius a=w/sqrt(3), and its intersections with a concentric sphere of radius R are

\[
q_e^\pm(R)=m_e\pm t u_e,\qquad t=\sqrt{R^2-w^2/3}.
\]

The report correctly calls this an **edge-tangent** sphere, not a face-tangent insphere. It intersects panel interiors; the three panels themselves are not a closed solid.

All 861 branch-pair equations were independently solved using an exact scalar projection followed by a zero-residual check. This also checked the supplied negative and inadmissible solutions, not just the three desired roots. Only tau=t/h in {1,1+sqrt(2),3+2sqrt(2)} is admissible for tau>=1.

The independent supporting-line calculation gives 90 intersecting pairs, 108 skew pairs and 12 distinct parallel pairs. Its admissible radii coincide exactly with the branch calculation. These finite algebraic classifications corroborate the report's exhaustive written proof: same-panel support lines meet at the three possible octagonal secant distances, and cross-panel meetings must occur on a shared seam line.

| Event | t/w | R²/w² | R/w | Unique sphere points |
|---|---|---|---:|---:|
| Original vertices | (sqrt(2)-1)/2 | 13/12-sqrt(2)/2 | 0.6133730937584284 | 18 |
| Crossing A | 1/2 | 7/12 | 0.7637626158259734 | 18 |
| Crossing B | (1+sqrt(2))/2 | 13/12+sqrt(2)/2 | 1.338073284435453 | 18 |

Every event has twelve double points and six triple points. Thus there remain 42 labelled incidences, not 18 edges or a deletion of labels. At every other allowed finite R there are 42 distinct positions. These are parameter-dependent intersections of fixed straight lines, **not temporal collisions**.

The sphere-point sets at these radii are not interchangeable simply because they have the same cardinality. The report preserves their separate coordinates, multiplicities and symmetry orbits.

## 3. Angular, symmetry and section results — PASS

All 861 coefficient triples in the angular inventory agree exactly. The 60 classes are functions of tau; they are not a universal count of distinct evaluated angles at every radius.

The three D3h generators preserve the complete symbolic branch family. The generic second moment is exactly

\[
\operatorname{diag}(12t^2+4w^2,\ 12t^2+4w^2,\ 18t^2+6w^2).
\]

At each exceptional radius, the unique-point second moment instead has vertical-minus-horizontal difference 3w²/2. Together with the three-point seam level, this establishes the report's upper bound on possible symmetries, not merely the presence of some D3h operations. The exact finite group remains D3h throughout R>=rho. The event orbit sizes are (6,12), (6,6,6), and (6,12).

The explicit seam/horizontal/chamfer family formulas agree coefficient-by-coefficient with all 42 original branches. The two stated latitude-hexagon events yield regular hexagons of chord side and circumradius w/3. The three stated regular panel-16-gon events follow from exact angle interleaving.

At the three coincidence radii, each original panel contributes eight points on its own sphere-section circle. Checking their endpoints along the **original support lines** gives cyclic steps 1, 2 and 3, respectively: a convex octagon, two squares, and the octagram {8/3}. These are section/endpoint-connectivity descriptions, not newly added shell faces. Interior crossings of drawn chords must not be confused with the sphere intersections being counted.

The normalized limiting directions have exactly 20 members, with two poles and three six-point rings at latitude 0 and +/-45 degrees. Their second moment is diag(6,6,8) and their symmetry is D6h. This is an infinite-radius directional limit, not a fourth finite event. Neither a 20-point count nor the section polygons establishes global tenfold symmetry.

The radial-projection comparison is correctly kept separate: scaling the original 18 vertices preserves their angular pattern, whereas extending an edge's supporting line follows a different construction for R>rho.

## 4. Additional reviewer observation: an exact octagonal ratio

This is an algebraic consequence of the accepted event table, stated explicitly here as a **subsequent reviewer observation**, not an additional experiment or a claim made in Codex's submission.

Writing the three exceptional midpoint-to-sphere distances as t0,t1,t2,

\[
\frac{t_1}{t_0}=\frac{t_2}{t_1}=1+\sqrt2,
\qquad
\frac{(t_0,t_1,t_2)}{h}=\bigl(1,1+\sqrt2,(1+\sqrt2)^2\bigr).
\]

Thus their displacement parameters form a three-term geometric progression using the reciprocal of the original normalized octagon edge length. Equivalently, t0*t2=t1²=w²/4.

This ratio is **not** the ratio of the enclosing radii, since R²=a²+t². It does not establish an infinite hierarchy, a recurrence law or dynamics; indeed the exhaustive result proves there are no further finite coincidence radii for this fixed 21-line family. It does not introduce pi*e*phi or select a physical boundary.

## 5. Figures, viewer and implementation limits

The six supplied numerical display cases reproduce the independently derived coordinates exactly in this reviewer environment; the maximum spherical norm residual is 2.220446049250313e-16 w. This is finite implementation evidence, separate from the exact proof.

The viewer includes the complete geometry inventory. Its pure coordinate evaluator matches `viewer_math.js` after only CRLF/LF normalization, and the embedded inventory matches the independently checked JSON. The evaluator was checked at all six supplied radii, including all three events, and against a custom R/w=10; counts and coordinates pass. Invalid R/w=0.5 and infinite radius are rejected. These checks do not certify arbitrary floating-point magnitudes or all browser/hardware combinations.

The HTML, mesh construction, control handlers and export construction were inspected as text. Codex's browser QA and its oblique screenshot were inspected; they are consistent with the report and static figure plates.

An independent Chromium file-navigation attempt was blocked by the environment before any page code loaded (`ERR_BLOCKED_BY_ADMINISTRATOR`). No alternate-navigation or policy-bypass attempt was made. Therefore this review does **not** claim to have independently exercised live browser controls, WebGL rendering or the export button. That limitation does not undermine the mathematical results. The supplied evidence already discloses Codex's different loopback browser test.

The initial pure-JS comparison stopped before numerical evaluation because it compared LF text against the HTML's CRLF representation. Normalizing line endings in reviewer memory resolved it; no submitted file changed. The subsequent pure-math pass succeeded. These are reviewer execution incidents, not source failures.

## 6. Archive, source preservation and final disposition

The supplied ZIP is 6,395,505 bytes, SHA-256:

`4bd26f23df8399abae332106a7c3f57d4698f4cc8a899114e732b5d7f88be431`

Its 45 members comprise 44 manifested payloads plus the manifest. Coverage, safe paths, exact and casefold name uniqueness, no-symlink checks, CRC, sizes and all payload SHA-256 values pass.

Report PDF: 960,736 bytes, SHA-256 `f6e638b11171066f938628d15090bc59ef5f83e3f57fd9c29fab3b2fa88a3da1`.

Standalone viewer: 4,806,355 bytes, SHA-256 `1021739222e88b56f41e7047c80127ba1868a897726d4c30c9125f8c6359b932`.

The supplied before/after source records agree. The actual two BOUNDARY-10 attachments match them. This review has no access to the author's Windows filesystem and makes no fresh repository-state or publication claim. The extracted submission and original uploaded archive were left unchanged.

**Final:** Accept this as a completed isolated geometric investigation. No report, proof, coordinate or figure revision is required. The result warrants discussion of the three exact incidence configurations and their section structure; it does not authorize adding a physical boundary, changing the model or beginning another task. Preserve this reviewer note alongside, not inside or over, the original report.
