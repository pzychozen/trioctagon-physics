# BOUNDARY-12 — GPT mathematical and observation-prototype review

**Date:** 16 October 2026  
**Human research author / owner:** Hilmir Frímann Halldórsson  
**Submission:** `BOUNDARY12_GPT_REVIEW.zip`  
**Mathematical verdict:** **ACCEPTED_WITHIN_STATIC_TERMINATION_GRAPH_AND_CONVEX_ENVELOPE_SCOPE**  
**Required mathematical or report corrections:** None.  
**Prototype disposition:** Pure evaluator and embedded geometry pass the prescribed comparisons and expanded unit/scale checks. One lower-bound floating-point input issue, V01, is recorded for handling before application integration. Independent browser navigation was blocked before the page loaded.  
**Application / publication:** Neither a live application change nor a publication is authorized by this review.

## 1. The questions are answered

The submitted proofs establish two different natural clipping rules for the unchanged 21 supporting lines. On each of the 42 outward rays, Crossing A is the first meeting with another distinct original line strictly beyond the starting vertex. Crossing B is the last finite such meeting. This is a geometric incidence statement, not a time evolution, reflection law or assertion that a physical object stops there.

With positive panel width w, original edge s=(sqrt(2)-1)w and half-edge h=s/2, the exits are m +/- t u and R^2=w^2/3+t^2. Therefore:

- Whole sphere-to-sphere chord: C=2t.
- Added distance beyond each original endpoint: ell=t-h.
- At A: C=w and ell=(1-sqrt(2)/2)w, the existing chamfer cutback.
- At B: ell=w and C=(1+sqrt(2))w.

The common edge-tangent sphere makes these lengths equal across edges; no extra equality constraint or changed panel size is required. The three-term ratio 1+sqrt(2) is correctly attributed to the subsequent BOUNDARY-11 review and remains a relation of along-line distances, not of sphere radii or an infinite recurrence.

The first/last proof correctly excludes a line meeting its own opposite parametrization at t=0. Equal distances of every supporting line from the centre imply equal absolute along-line parameters at any distinct-line meeting. This makes reuse of the accepted complete common-parameter catalogue legitimate. The 42 labels participate at both A and B; there is no unaccounted ray-specific later intersection.

## 2. Independent geometric verification

The reviewer-written `verify_boundary12.py` reconstructs the 18 source vertices and 21 edges from Paper C's local octagon and three affine fold maps. It does not use the submitted new hull coordinates as the geometric premise. The reconstruction matches the unchanged accepted BOUNDARY-11 inventory and material indexing.

Exact arithmetic is in Q(sqrt(2),sqrt(3)). All zero and sign decisions for hull support are made on these exact algebraic values. The review independently enumerated all 816 vertex triples at each event, merging proportional plane equations and retaining precisely the supporting planes. It verified all maximal coplanar vertex sets, their outward orientations, side-squared and turn-dot sequences, actual edge incidences, closed vertex links, containment and D3h facet orbits.

| Event | Split graph V/E | Components | Cycle rank | Hull V/E/F | Maximal face types |
|---|---:|---:|---:|---:|---|
| Original | 18 / 21 | 1 | 4 | 18 / 27 / 11 | 3 regular octagons, 6 isosceles triangles, 2 nonregular hexagons |
| A | 36 / 63 | 1 | 28 | 18 / 48 / 32 | 30 isosceles triangles, 2 equilateral triangles |
| B | 54 / 105 | 1 | 52 | 18 / 36 / 20 | 6 isosceles triangles, 6 isosceles trapezoids, 6 rectangles, 2 equilateral triangles |

Across the three hulls there are 2,448 examined vertex triples and 63 maximal facets. The numbers of distinct noncollinear planes are 397, 488 and 397. Face orbit sizes are respectively (2,3,6), (2,6,6,6,12), and (2,3,3,6,6).

All graph vertices, exact segment intervals, lengths, source edge/ray labels, adjacency, degrees and connected components were checked. The cumulative graph populations are 108 vertex records and 189 segment records. The proof formulas V_k=18(k+1), E_k=21(2k+1), and cycle rank=4+24k apply to k=0,1,2 only in this finite classification. They are not an unbounded sequence of further events.

Each hull's exposed vertex set is exactly the corresponding 18 outer sphere points. Consequently the accepted upper bound on point-set symmetry also bounds the hull's symmetry. The graph has that hull and is D3h invariant, giving the same complete spatial symmetry. No additional global tenfold symmetry follows from a face or vertex count.

## 3. The framework and enclosing surface must stay separate

The submitted graph-to-hull classification passes exact active-plane checks over whole segments, not just samples:

| Event | Graph edges on hull edges | Graph edges within a single face | Open graph segments strictly inside hull | Boundary / interior graph vertices |
|---|---:|---:|---:|---:|
| Original | 21 | 0 | 0 | 18 / 0 |
| A | 0 | 0 | 63 | 18 / 18 |
| B | 0 | 0 | 105 | 18 / 36 |

At A and B every open segment is interior, even though some endpoints touch the hull. Thus extending the lines constructs a connected interior framework; it does not itself trace or fill the hull's outer faces. The convex hull is a separately declared, parameter-free enclosure once the point set and convexification convention are chosen.

The original convex hull adds six boundary edges and eight faces beyond the existing three-panel shell. None of these new filled faces is retrospectively part of Paper C.

The hulls are nested by segment containment, but they are not similar copies: their edge and face counts differ. Increasing only observer radius is therefore genuinely different from uniformly scaling the whole construction. This is a useful result for observation software, not an equivalence of physical dynamics.

## 4. Scaling and scalar-source review

Uniform geometric scaling preserves the exact incidences, angles, labels and ratios. Areas and volumes of similar copies scale with the corresponding second and third powers. Choosing display unit w, s, C or ell is not changing R/w. The ell unit is undefined when ell=0. Neither a display-unit conversion nor a geometric similarity demonstrates covariance of a nonlinear memory or physics kernel.

The seven fixed presets and all 294 branch-coordinate records were independently recomputed at 85 decimal digits. The largest discrepancy with the stored numerical coordinates is approximately 8.803e-16 in width units. The event presets reproduce exact event identities; assigned R/w=1, t/w=1, R/w=10 and R/w=pi*e*phi remain distinct assigned comparisons.

The supplied numbered source excerpts and three source-page images were read. They support the report's distinction between gamma_* defined by zeta(3)/(pi*e*phi), historical run-dependent or unspecified estimators, Euler–Mascheroni gamma, and the static frequency family. The ordinary zeta-series domain stated in the report follows from its exponent being greater than one.

The golden-interval expansion and supplied polylogarithm substitutions correctly leave the coefficient 1/10. The independent scalar quadrature gave a residual about -1.01e-87 against zeta(3)/10 at 85-digit working precision. That is numerical corroboration of the written algebra, not formal interval certification or an independent geometric derivation. The identity and attribution are inherited from the provided source account; this review performed no external literature search.

All four prescribed ratio values, signed discrepancies and conditional length/area/volume conversions agree. No ratio matches T/10 in the tested comparisons. This is a result about those specified candidates, not a proof excluding every possible correspondence.

The remembered near-10 aggregate remains unresolved. I checked the submitted bounded-search account, not a new exhaustive search of all historical research. There is no need to manufacture an aggregate to complete the geometric study.

## 5. Viewer verification and V01

The actual HTML's embedded JSON equals the checked inventories, and its pure evaluator agrees with the standalone evaluator after CRLF/LF normalization. The accepted Plotly library matches the original BOUNDARY-11 archive byte-for-byte.

A reviewer-written Node test exercised the actual pure evaluator in an isolated context. It passed 434 checks, including 81 valid combinations of seven presets, three positive widths and four display units (excluding the three singular original/extension-unit combinations); six near-event inputs; thirteen invalid requests; exact C/w=1, ell/w=0 and ell/w=1 entries; and both submitted browser-created export payloads. The largest normalized-coordinate discrepancy was 1.776e-15. Physical/display-coordinate residuals depend on the selected scale/unit and are recorded separately.

### V01 — custom-radius lower-bound roundoff

An additional reviewer probe, outside the exact-preset cases, used:

```javascript
boundary12Geometry(data, {
  mode: 'R', value: data.geometry.rho, w: 1, unit: 'width'
})
```

It returns `ell_over_w = -2.220446049250313e-16`, with no exact-event tag. The custom radius passes the viewer's lower-bound comparison, but floating-point conversion to t followed by t-h gives a tiny negative extension. The mathematical domain requires ell>=0.

This is **not an error in any exact geometry, reported event length, graph, hull or source constant**, and the explicit Original preset is correct. It is a nonblocking issue for acceptance of this isolated research and a concrete numeric-input requirement **before live app integration**. It must not be concealed as a physical negative extension or "fixed" by promoting nearby numeric radii into exact incidence events. A later scoped implementation should define the lower-bound representation/validation policy, preserve the raw request and exact-event distinction, and test the boundary plus its adjacent floating-point inputs. No patch was applied in this review.

### Browser limitation

One independent Chromium navigation to a loopback-only preview was rejected with `ERR_BLOCKED_BY_ADMINISTRATOR` before page code loaded. No alternate route, policy bypass or retry was attempted. The preview server was shut down. Therefore this review does not independently certify live controls, WebGL, camera gestures or browser downloads. The four supplied screenshots and Codex browser-QA records were inspected; they are consistent with the checked data and static figures. The two supplied browser exports agree with the independently exercised pure exporter.

`APP_OBSERVER_DESIGN.md` is an appropriate observation-only design proposal. It remains a proposal, not a completed audit of live application integration.

## 6. Integrity, execution, and limits

Submission ZIP: **5,531,404 bytes**, SHA-256:

`02cadf8601628bc9243f0bd89706e12b4f8c901a7374ab2666a3b2595404983e`

All **117 members** (116 manifested payloads plus `REVIEW_MANIFEST.json`) pass exact hash/size, coverage, CRC, safe-path, unique/case-unique name and no-symlink checks. The separately supplied report is identical to its archived copy.

All 14 original handoff members agree with the actual previously supplied handoff ZIP. The six selected BOUNDARY-11 files match the actual original submission archive; the complete subsequent review ZIP matches the actual prior reviewer package. All 81 supplied Windows source-preservation records agree internally. This does not claim direct access to the author's Windows filesystem or independent enumeration of all 81 live files.

The exact/static reviewer script executed once successfully (2,120 checks, approximately 4.65 seconds). The independent pure-JavaScript test executed once successfully. These check counts describe implementation accounting, not numbers of separate mathematical discoveries. The only blocked stage was the disclosed browser navigation.

No supplied analytical/checker script, historical simulation, kernel, RNG, state reconstruction, PDF build, old suite or Git operation was run. No report, source, figure, viewer or accepted data was modified. Two static figure plates, four submitted viewer screenshots and three supplied source-page images were inspected; there is no new report PDF in this submission, so no report-page-render claim is made.

## 7. Disposition and recommendation

Accept the BOUNDARY-12 mathematical report and exact new inventories. Preserve the original submission and this separate review; V01 stays in the observation-integration issue list.

The BOUNDARY-10/11/12 sequence now supports a detailed mathematical account and a useful observation-only application feature. Recommended next preparation is a unified account of the edge-tangent sphere, finite incidence events, natural clipping lengths, connected frameworks, and their separately defined convex envelopes. A later scoped app task should first inspect the actual integration boundary, handle V01, and prove observation leaves kernel state, random state and time unchanged.

Do not add a force, material wall, reflection rule, recursive stopping law, new physical scale or automatic mapping to 10 or pi*e*phi. None is needed to preserve or display the accepted geometric results. No additional unbounded geometric search is required before documentation and an observation-integration decision.
