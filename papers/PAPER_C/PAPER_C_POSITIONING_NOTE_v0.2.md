# Paper C — Positioning Note v0.2

How to position the frozen `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.2.2.md` mathematics given the literature context. Companion to `PAPER_C_LITERATURE_CONTEXT_v0.2.md` and `PAPER_C_REFERENCE_LEDGER_v0.2.md`; the CONSERVATIVE positioning below is now realized in the referenced manuscript `DRAFT_v0.3.1`. No manuscript edit here. The mathematics is frozen.

**v0.2 update (citation-closeout companion).** Three claim-scope distinctions, carried consistently across manuscript / literature context / reference ledger / this note:
- **A1 — polyhedral *construction* is background; PL *manifold with boundary* is established here.** Calling the object a "polyhedral surface" (a finite union of planar polygons meeting along shared edges) is standard terminology ([RS72], [Cox73]). That *this* object is a PL **manifold** with boundary is **not** carried by the name — the local manifold hypotheses are verified in §5 (via the vertex links). Keep the two separate in every framing sentence.
- **A2 — the vertex-link criterion is dimension-specific.** Cite [RS72, Exercise 2.21(1)]: for a $2$-dimensional simplicial triangulation, each vertex link is a PL circle (interior) or arc (boundary). The literature supplies the criterion; the links of this surface (all arcs ⇒ all $18$ vertices on the boundary) are computed here.
- **A3 — the outward-normal / interior-dihedral angle convention is [Cox73, §10.7], not Cotton.** [Cotton90] (with [AH94]) is a **point-group** citation only ($D_{3h}$). Do not cite it for the polyhedral angle convention.

## The situation in one line

Every general tool (regular-polygon trigonometry, Euler characteristic, surface classification $\chi=2-2g-b$, vertex-link manifold test, dihedral/normal conventions, the point group $D_{3h}$, exact-arithmetic verification) is **standard**; the **exact coordinate construction and complete geometric characterization of this particular three-octagon welded polyhedral surface** is the model-specific contribution, for which **no close precedent was located**.

## Three positionings

### A. CONSERVATIVE — *recommended*
**Framing.** Treat all general machinery as established background, cited to [Cox73]/[Cox69] (polygon metrics), [Massey91]/[GX13] (surface classification), [RS72] (vertex links / polyhedral surface), [Cotton90]/[AH94] (the group $D_{3h}$), [DO07]/[Tachi09] (the hinged-folding setting), and [Yap97]/[KMPSY08]/[Shewchuk97] (exact-computation methodology). State plainly that $\chi=2-2g-b$, the classification theorem, and $D_{3h}$ are quoted, and that **Paper C supplies the hypotheses/coordinates/theorems for this specific shell**. **Contribution:** the exact closed-form construction (18 vertices; general-$\beta$ closure and $\beta=\tfrac{\pi}{3}$) and the complete characterization (topology + annulus, section, dihedral/normal, chamfer-edge, notch, rim/hexagon, and the theorem that the exact symmetry group is $D_{3h}$).
- **Pros.** Fully defensible; matches the evidence; matches the manuscript's own careful "no physical claim / normalization only" discipline; lowest referee risk.
- **Cons.** Modest-sounding, but accurate.
- **Best supported by the literature: YES.**

### B. MODERATE — *acceptable if framed carefully*
**Framing.** Foreground the **worked completeness** — a single specific polyhedral surface whose exact coordinates, topology, all characteristic angles, symmetry group (with a matching upper bound), and a genuine regression suite are all written down in closed form and independently verified. Present it as a clean, fully characterized exemplar rather than as new general theory.
- **Pros.** Honest; highlights that the end-to-end exact characterization in one object is not trivially off-the-shelf.
- **Cons.** Only acceptable if the paper **explicitly labels every general tool as background** and does not imply the machinery is new. Must retain the [Massey91]/[RS72]/[Cotton90] citations up front.
- **Best supported: PARTIALLY** — defensible only with the background clearly ceded.

### C. STRONG — *not recommended*
**Framing.** Claim a new theorem, mechanism, or object class.
- **Not supported.** Every mechanism has a standard home; the specific shell has no located precedent but absence is not novelty. `NOVELTY_CLAIM_JUSTIFIED = NO`. Do not adopt.

## Recommendation

**Adopt A (CONSERVATIVE).** Optionally borrow B's one-sentence framing of the *worked completeness* ("a specific polyhedral surface fully characterized in closed form — coordinates, topology, angles, and exact symmetry group — with an independent regression suite") **only** after the background is ceded with citations. The frozen mathematics needs no change; a referenced version adds (i) a short "Relation to established results" paragraph with the citations above, (ii) the terminology upgrade below, and (iii) the honest "no close precedent located" sentence. No claim of priority; a literature-context pass is not a novelty determination.

## Terminology recommendation (requested)

**Prefer "polyhedral surface (with boundary)" over "shell."** The polygonal construction is polyhedral [RS72, Cox73]; §5 establishes that this particular object is a piecewise-linear surface with boundary. Recommended usage: introduce it once as "a polyhedral surface with boundary (informally, an open lateral shell)," then use "polyhedral surface" as the primary term and keep "shell" only as an informal descriptor. This is a wording upgrade for a mathematical readership and changes no geometry.

## Concrete additions for a referenced version (no math change)

1. §1 or a new "Relation to established results": one paragraph placing the octagon metrics ([Cox73]), the hinged-folding setting ([DO07], [Tachi09]), $\chi=2-2g-b$ and surface classification ([Massey91], [GX13]), the vertex-link manifold criterion ([RS72]), the dihedral/normal conventions ([Cox73, §10.7]), and $D_{3h}\cong D_3\times C_s$ ([Cotton90], [AH94]). Naming the object "polyhedral" is background; the PL-manifold-with-boundary property is established in §5.
2. §5: cite [Massey91]/[GX13] for the classification theorem and [RS72, Exercise 2.21(1)] for the dimension-specific vertex-link criterion (PL circle or arc for a $2$-complex) — with the explicit note that *Paper C supplies the hypotheses for this surface* (every link an arc ⇒ all $18$ vertices on the boundary).
3. §9: cite [Cotton90]/[AH94] for the group $D_{3h}$ — with the explicit note that *the theorem that this shell realizes $D_{3h}$ is proved here* (lower bound + crease-segment upper bound), not quoted.
4. §10 / proof audit: cite [Yap97]/[KMPSY08]/[Shewchuk97] for the exact-computation methodology and the analysis-vs-implementation distinction.
5. Terminology: adopt "polyhedral surface with boundary" per above.
6. One honest sentence (§6.5-style, or Limitations): "No close precedent for this specific three-octagon polyhedral surface was located in a focused literature search; its novelty is unresolved and not claimed."
7. Bibliography from `PAPER_C_REFERENCE_LEDGER_v0.2.md` (13-tag publication set; Bishop93 is non-publication background and uncited). The metadata records are checked; a final publisher-of-record spot-check (notably the Tachi09 print-vs-online manifestation) remains a production step.

These additions are background/terminology only and change no coordinate, theorem, or number.

## What NOT to do

- Do not cite folding/origami works as precedent for *this* shell's existence, closure, or symmetry.
- Do not cite the classification theorem or $D_{3h}$ group tables as *proving* the shell's annulus type or symmetry — Paper C proves those.
- Do not promote standard background (polygon metrics, $\chi=2-2g-b$, dihedral conventions, $D_{3h}$ theory) as contributions.
- Do not treat "polyhedral surface" (terminology) as establishing the PL-manifold-with-boundary property — that is proved in §5.
- Do not cite [Cotton90] for the outward-normal / interior-dihedral angle convention — that is [Cox73, §10.7]; Cotton is a point-group citation only.
- Do not write "novel" — write "no close precedent was located in the focused search."

```
RECOMMENDED_POSITIONING = CONSERVATIVE
POSITIONING_REALIZED_IN = DRAFT_v0.3.1
TERMINOLOGY_UPGRADE = polyhedral surface with boundary (over "shell")
A1_POLYHEDRAL_VS_MANIFOLD_SCOPE = RESOLVED
A2_VERTEX_LINK_DIMENSION_SPECIFIC = RESOLVED
A3_ANGLE_CONVENTION_COX73_NOT_COTTON = RESOLVED
NOVELTY_CLAIM_JUSTIFIED = NO
NOVELTY_STATUS = UNRESOLVED
MATHEMATICS_CHANGED = NO
MANUSCRIPT_CHANGED = NO
READY_FOR_REFERENCED_MANUSCRIPT = YES
```
