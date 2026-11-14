# TRIOCTAGON_OUTER_ENVELOPE_01 — Codex investigation work order
## Exact outer-envelope transitions between Crossings A and B

**Date:** 13 November 2026.  
**Research author:** Hilmir Frímann Halldórsson (pzychozen).  
**Scientific lead:** GPT. **Investigation and independent challenge:** Codex.  
**Authorization:** The author explicitly approved the outer-geometry direction and a new investigation order. This order authorizes one bounded, static mathematical investigation and a review return. It does **not** authorize a manuscript, publication, application integration, kernel edit, or adoption of a new physical geometry.

## 1. The question and why it matters

> For the unchanged 21 supporting lines of the folded Tri-Octagon, what are the exact maximal faces of their convex outer envelope **throughout the interval between Crossing A and Crossing B**? Can the envelope change its face structure at a radius where no supporting-line exits coincide?

The completed BOUNDARY-11 result classifies coincidences of the spherical exits at every finite permitted radius. BOUNDARY-12 classifies the three special event hulls (Original, A, B). Neither statement, by itself, classifies the intervening maximal-face structures. The first task is to check whether any later source already does so.

A preliminary GPT calculation nominates a change at `t/h = 3`, strictly between A and B. A separate symbolic planning calculation finds a six-point supporting plane there. These are **leads for independent verification**, not an accepted complete classification or an instruction to reproduce a desired result.

The useful outcome is a proved explanation of how these existing larger envelopes fit together. An additional support-plane event is not a fourth line-incidence event. This distinction is the reason for the investigation, not a higher-resolution rendering exercise.

## 2. Prior-work gate — before new scientific calculations

Read `PRIOR_WORK_COMPARISON.md`, `SOURCE_GUIDE.md`, and the exact sources listed in `REQUIRED_SOURCES.json`. Check the relevant local successors and current geometry indexes, not just the titles of old papers. In particular compare:

- Paper C's original folded shell and its fixed indexing;
- BOUNDARY-10/11/12, their controlling reviews, and the spherical-edge synthesis;
- TSZ-01 / geometric-origins normalization findings where available;
- the later Spherical Edge Observer implementation, **read-only**, insofar as it may already contain a generic exact hull classification rather than a floating rendering;
- later source-linked outer-geometry reports identifiable from those indexes.

Write a short comparison with exact section/equation/claim locators. Distinguish the complete coincidence catalogue, the three event hulls, generic display meshes, and a parameter-uniform maximal-face theorem.

Use one of: `DISTINCT_GAP`, `PARTIALLY_ANSWERED`, `ALREADY_ANSWERED`, or `SOURCE_BLOCKED`.

If already answered at this scope, stop and return the existing answer with its controlling evidence. Do not relabel it as new, and do not automatically expand to another interval. If partially answered, reuse the answered part and investigate only the stated residual gap. A failed code-search query is not evidence of novelty. This is a bounded project-source comparison, not a worldwide priority claim.

The recently published turning-capture and M2–M3 connection are closed. Neither is a new task here. Full-range alternating-branch attraction remains open but out of scope.

## 3. Frozen object, conventions, and exact domain

Work in the original centred frame with positive panel width `w`. Preserve the inherited material vertices V0–V17, edge IDs E01–E21, face cycles, and both branch labels.

Let

\[
h=\frac{\sqrt2-1}{2}w,\qquad a_m=\frac w{\sqrt3},\qquad
\rho=w\sqrt{\frac{13}{12}-\frac{\sqrt2}{2}}.
\]

For each inherited edge with centred endpoints `v_i,v_j` in increasing V-index order,

\[
m_e=\frac{v_i+v_j}{2},\qquad
u_e=\frac{v_j-v_i}{2h},\qquad
q_e^\pm(t)=m_e\pm t u_e,\qquad R^2=a_m^2+t^2.
\]

Here `u_e` is the inherited unit direction. All lengths and labels come from the source geometry.

Use the dimensionless parameter

\[
x=t/w,\quad h_1=h/w=(\sqrt2-1)/2,
\qquad \boxed{\frac12\le x\le\frac{1+\sqrt2}{2}}.
\]

These are **exactly A through B**. The original sphere is a retained reference below this interval. It is not being replaced or re-optimized.

For every parameter in this interval define

\[
P(x)=\{m_e/w\pm x u_e:e=1,\ldots,21\},
\qquad H(x)=\operatorname{conv}P(x).
\]

`P(x)` denotes unique spatial positions; retain a separate 42-label incidence map. There are 42 distinct positions in the open interval and 18 at each endpoint by the inherited catalogue. The same-radius exposed-point argument makes these the hull vertices; cite/reuse it rather than announcing a new vertex mechanism.

**Explicit convention:** extending the already-used convexification convention from the three event sets to this interval is a mathematical observation definition. Once it is specified, `H(x)` has no added orientation or fitted scale. Convexification is not forced as a physical wall by the native kernel. Do not describe variation in `x` as a native trajectory, physical time, breathing motion, or a change in panel width.

The exact reconstruction recipe is in `EXACT_CASE.md`. Reconcile it with the inherited inventory before calculations; an inconsistency is a source issue to report, not permission to edit Paper C.

## 4. Inherited facts — consume, do not recommission

The source results include:

- The unique close minimum enclosing ball, the common edge-tangent sphere, and the complete finite line-incidence events.
- A: `x=1/2`, `R_A^2/w^2=7/12`, full chord `C=w`, event hull `(V,E,F)=(18,48,32)`.
- B: `x=(1+sqrt(2))/2`, `R_B^2/w^2=13/12+sqrt(2)/2`, per-end addition `ell=w`, event hull `(18,36,20)`.
- Original: `(18,27,11)`, useful reference only; no new Original-to-A task.
- Full finite exit-set symmetry `D3h`; no global tenfold symmetry at any finite radius in that family.
- The three event along-line distances follow the three-term silver-ratio relation with `sigma=1+sqrt(2)`. Sphere radii do not follow that geometric progression.
- The optional regular decagonal prism requires an independently selected axial orientation; its golden-ratio identity is already known.
- The previously tested `10`, `pi*e*phi`, and TSZ size comparisons have scoped outcomes and unresolved interpretive choices. No new numerical matching exercise is authorized.

Endpoint data are mandatory inputs. Authenticate/copy them, and compare the new interval representation with their exact faces at A and B. This compatibility check is not a replay of the historical 816-triple hull derivations or old line-pair catalogue.

## 5. Bounded investigation stages

### O01 — Prior-work and source concordance (documentary / inherited)

Complete the gate in Section 2. Freeze the exact input identities, indexing map, parameter interval, and definition of `H(x)`. Provide a minimal source-to-symbol crosswalk. Do not count this as a new theorem.

### O02 — Verify or reject the proposed noncollision face transition

Independently derive the candidate supporting-plane relation in `GPT_ANALYTICAL_START.md`. The nominated parameter is

\[
x_*=3h_1=\frac{3(\sqrt2-1)}2,\qquad
R_*^2/w^2=\frac{85}{12}-\frac{9\sqrt2}{2}.
\]

First show exactly that it is in `(A,B)` and is not one of the inherited coincidence parameters. Then check the supporting plane, its **complete** zero set, dimensionality, and the adjacent face changes. A six-point coplanarity alone is insufficient: the plane must support every point, and the polygon must be a genuine maximal facet.

Reject the candidate if it fails. If it holds, explain the geometric mechanism without describing it as a collision of points. Investigate its symmetry-related facets using the existing group action; do not assume a full orbit count from a picture.

### O03 — Certify the maximal-face structures throughout A–B

Give an exact finite partition into open parameter intervals and exceptional parameter values on which the labelled face lattice is constant. Do not assume the nominated transition is the only one. Equal `V/E/F` counts do not prove the same labelled incidence structure.

For each chamber and exceptional value return:

- exact parameter endpoints, with minimal polynomial / isolating interval if required;
- each maximal supporting-plane family or a complete set of symmetry representatives;
- the full zero-set vertex labels, cyclic face order, true edges and vertex/facet incidences;
- `V/E/F`, face-size histogram, and orbit data sufficient to interpret the changes;
- exact parameter-uniform residual signs for every point against every retained plane;
- an explicit completeness argument that excludes omitted facets or transitions.

Collinear triples, identically coplanar families, source-label coincidences, and genuine combinatorial transitions must be handled separately. Merge coplanar triangle fans into their actual maximal polygon faces. A coplanarity root that occurs strictly inside the hull is not automatically a boundary transition.

Suggested exact approach: in the fixed algebraic field `Q(sqrt(2),sqrt(3))`, point coordinates are affine in `x`; orientation determinants for four points have degree at most three. Use these expressions with exact sign/root decisions, symmetry reduction, and explicit handling of identities. Alternatively provide a smaller complete halfspace/face certificate and a proof that it exhausts the convex hull for every parameter in each interval. A list of plausible supporting faces and Euler's formula alone is not a completeness proof.

Floating hull calculations may nominate candidate faces only. No numerical tolerance may supply a final coplanarity, face identity, transition endpoint, or interval-coverage decision. Use the exact endpoint data at A and B as inherited compatibility targets.

### O04 — Interpret what the complete result forces, and what it does not

Describe how the new chambers connect to the inherited A and B hulls, including vertices merging at A/B versus any noncollision facet regrouping in between. Use the existing support-line network separately from the envelope. Do not introduce new graph edges simply because a hull edge is drawn.

As a direct readout of the **certified complete face list**, state whether any maximal facet in this interval has ten vertices. If one does, assess its regularity from exact side/angle data. If none does, limit the conclusion to facets of this declared A–B hull family. This does not exclude arbitrarily chosen planar sections, selected subsets, projections, external enclosures, or another unadopted construction. The previously proved global `D3h` symmetry is not by itself a proof that a ten-sided facet is impossible.

Keep the golden ratio `phi=(1+sqrt(5))/2`, silver ratio `sigma=1+sqrt(2)`, original close sphere, A/B spheres, and proposed decagonal prism distinct. Report exact formulas actually produced by the geometry. Do not search for arbitrary ratios close to phi, fit `pi*e*phi`, or claim that a field of coordinate coefficients excludes every possible metric golden-ratio relation.

The interpretation should answer: **which new features are forced once the inherited exit family and convex-hull convention are fixed?** Any further geometric/physical adoption remains a separate author decision.

## 6. Proof and checker standard

Written arguments, not manifest counts or nominal plots, establish the conclusions. Supply a read-only checker of the new certificate that reconstructs the frozen family and validates its exact decisions. Independently organize the decisive containment, sign, maximality, coverage, and endpoint checks rather than trusting saved success flags.

Shared libraries or a shared algebra engine are allowed but must be disclosed. Do not call two wrappers around the same arithmetic engine two independent implementations. Keep exact arithmetic separate from decimal display output. At least three meaningful rejection controls should cover a false transition parameter/sign, an omitted facet or incomplete zero set, and a broken label/endpoint mapping. Add a coverage-gap control if the representation supports it.

Exact identities can be proved symbolically; interval checks require outward enclosures and a documented trusted basis. Hashes authenticate bytes, not theorems. Do not claim proof-assistant verification unless one is actually performed; it is not required.

No old scientific suite needs to be rerun. Reading a retained source and comparing a new endpoint representation against saved exact input are permitted and should be described accurately.

## 7. Execution limits and preservation

Repository: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics` (read-only).  
New workspace: `C:\TORMENT\TRIOCTAGON_new\research\TRIOCTAGON_OUTER_ENVELOPE_01\run_<actual-date>_<unique-id>\`.

Use Windows Command Prompt and the existing `torment` environment. Record actual Python and library versions. Do not install/update packages, change persistent settings, or import/run the native physics kernel, production TORMENT, UI, or historical simulations. Use existing exact arithmetic facilities or isolated local code. Do not require SciPy just to reproduce the optional GPT pilot.

The reading checkpoint is `46bf10808b8694476b61b359be305a66a46d4614`, not a checkout/reset target or a claim about future HEAD. Read-only Git commands for source retrieval/identity are allowed. No fetch, checkout, reset, clean, branch creation, worktree addition, stage, commit, push, tag, CI dispatch, or repository write is authorized. Prefer existing local source bytes; if necessary, retrieve a **listed pinned** source by an authorized read, into external scratch only. Do not silently normalize CRLF/LF to make a hash match; preserve working-file and Git-blob identities separately. `tools/collect_sources.py` is an optional standard-library read-only helper.

Keep all original inputs unchanged. Copy only relevant sources into the result. Do not duplicate giant historical closeout trees or bundle font files, compiler caches, credentials, private unrelated files, or whole repository status dumps.

Bound the numerical nomination phase to 64 parameter samples in the stated interval, with at most 32 additional bisection evaluations for candidate brackets. These are planning limits, not proof of completeness. Symbolic root isolation must cover the claimed intervals regardless of how few samples were used. Start from the supplied candidate to avoid a blind sweep. Exact finite enumerations are allowed; freeze the method and resource bound before execution. Use bounded worker runs (for example at most 15 minutes and 2 GiB per worker), preserving failures rather than escalating indefinitely. These are process ceilings, not predicted runtimes.

Do not let a difficult full classification turn into a claim of nonexistence. If a bounded run proves only a local transition or one subinterval, return the exact partial domain and the remaining proof obligation. If additional mathematical effort is needed within the same scope, explain it without silently opening another research programme.

## 8. Author-decision boundary

No new geometric choice is required for this assessment: the source shell and supporting lines are fixed, and convexification is explicitly an observation convention. Ordinary derivation and verification can proceed independently.

Stop before choosing a material wall, moving-support law, physically preferred observer radius, new projection/section plane, decagonal orientation, new recursion, scale calibration, or altered shell. Show the concrete alternatives if such a choice becomes essential. Recovering existing files, coefficients and definitions is Codex/GPT's responsibility, not the author's homework.

## 9. Return package

Return:

1. `RESULT_SUMMARY.md`: plain-language result and exact domain; distinguish inherited, new proved, proposed and unresolved content.
2. `PROOF_REPORT.md`: derivation, chamber classification, maximality/completeness arguments, endpoint compatibility, interpretation limits.
3. `PRIOR_WORK_COMPARISON.md` and `CLAIM_LEDGER.json`: exact locators and dispositions; do not count O01 as a discovery.
4. `data/`: exact certificate, transition definitions, face/incidence records, endpoint mapping, and separately labelled exploratory records.
5. `scripts/`: new checker and any generation helpers, with execution/negative-control evidence and actual dependency versions.
6. `sources/` and identity manifest: the necessary unchanged originals, clearly distinguished from GPT transcriptions/pilot material.
7. A safe, self-excluding payload manifest, review ZIP, external SHA-256 sidecar, and final member-by-member archive audit.

An explanatory computed figure is optional, not a substitute for proof. Label any triangulation, viewpoint, scale normalization and envelope convention. No polished paper or application viewer is commissioned.

Review ZIP name: `TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip`.

## 10. Stop condition

Return for GPT/author review when this bounded A–B assessment is complete, already answered, source-blocked, or precisely partial. Do not extend to Original–A, beyond B, all radii, full-range dynamical stability, AI memory, SRG, or a new paper automatically.

**Core instruction:** determine what the existing geometric family actually requires; do not make it acquire the hoped-for decagon or a target constant by adding a choice.
