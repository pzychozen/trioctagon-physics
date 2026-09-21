# Paper C — Literature Context v0.2
### Standard machinery vs model-specific construction

Focused literature-context review of the frozen `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.2.2.md` (with `PAPER_C_PROOF_AUDIT_v0.2.2.md`, `PAPER_C_SYMBOLS_AND_IDENTITIES_v0.2.md`). **No manuscript was edited; no coordinate, equation, theorem, proof, or number was changed; the kernel was not touched.** Purpose: locate each mathematical ingredient of Paper C within established geometry/topology/group-theory literature and classify it conservatively.

**v0.2 update (citation-closeout companion to `DRAFT_v0.3.1`).** Three claim-scope distinctions sharpened, mathematics unchanged:
- **A1 — polyhedral *construction* vs PL *manifold-with-boundary*.** The word "polyhedral surface" is standard **terminology** for a finite union of planar polygons meeting along shared edges ([RS72], [Cox73]); this is background. That *this particular object* is a piecewise-linear **manifold** (surface) **with boundary** — that the local manifold hypotheses hold at every point — is **not** delivered by the terminology; it is **established here** for this object (§5, via the vertex links). The two are kept separate throughout.
- **A2 — vertex-link criterion is dimension-specific.** The general PL statement cited is: for a $2$-dimensional simplicial triangulation, each vertex link is a PL **circle** (interior vertex) or a PL **closed interval / arc** (boundary vertex) ([RS72, Exercise 2.21(1)]). The literature supplies the criterion; the actual links of *this* surface — every one an arc, so all $18$ vertices are boundary vertices — are computed here.
- **A3 — Cotton is cited for the point group only.** [Cotton90] (with [AH94]) supports the **Schoenflies point-group** material — $D_{3h}$, order $12$, $\cong D_3\times C_s$, classes and character table — and **not** the polyhedral interior-dihedral / outward-normal angle convention. That angle convention is cited to [Cox73, §10.7]. Cotton is no longer listed as a source for the outward-normal convention anywhere in this pass.

**Classification vocabulary (as instructed):** `STANDARD` · `STANDARD_SPECIALIZATION` · `MODEL_SPECIFIC_CONSTRUCTION` · `MODEL_SPECIFIC_DERIVATION` · `NO_CLOSE_PRECEDENT_LOCATED` · `NOVELTY_UNRESOLVED`. The word `NOVEL` is **never** used on the basis of a search finding nothing.

**Search scope (Sep 2026):** regular-polygon metric identities and normalization; hinged polygonal panels / rigid origami / folding algorithms; polyhedral and piecewise-Euclidean surfaces with boundary; Euler characteristic and classification of compact orientable surfaces with boundary; vertex links as PL manifold tests; dihedral-angle vs face-normal conventions; Euclidean point groups of polyhedral objects and $D_{3h}$ Schoenflies notation; exact/symbolic computational-geometry verification; and the exact three-octagon configuration. References by tag are in `PAPER_C_REFERENCE_LEDGER_v0.2.md`. This is a focused pass, not an exhaustive survey.

---

## 1. Headline finding

**Every general mathematical tool Paper C uses is standard textbook material.** Regular-polygon trigonometry, the Euler characteristic of a cell complex, the classification of compact surfaces with boundary via $\chi=2-2g-b$, vertex links as a manifold-with-boundary test, the dihedral/face-normal angle conventions, the Schoenflies point group $D_{3h}\cong D_3\times C_s$, and the exact-arithmetic verification paradigm are all established and citable.

**The model-specific content is the *instance*, not the machinery:** the **exact coordinate construction and complete geometric characterization of this particular three-octagon welded polyhedral surface** — its closed-form vertices, the general-$\beta$ closure and the $\tfrac{\pi}{3}$ solution, the $18$/$21$/$3$ counts, the specific angles ($60^\circ$ dihedral, $\arccos(3/4)$ notch), the rim/hexagon decomposition, and the theorem that its exact symmetry group is $D_{3h}$. For that specific object **no close precedent was located in the focused search** (`NO_CLOSE_PRECEDENT_LOCATED`, `NOVELTY_UNRESOLVED`); this is expected for a specific worked construction and is recorded, never asserted as novelty.

**Recommended positioning: CONSERVATIVE** (see `PAPER_C_POSITIONING_NOTE_v0.2.md`). Cite the standard frameworks as background; present the specific shell's exact construction and characterization as the model-specific contribution.

## 2. Terminology verification

The manuscript's informal word **"shell"** has a precise standard replacement. The object is a finite union of planar polygons (the three octagons) meeting along shared edges — i.e. a **polyhedral surface** (equivalently a **piecewise-linear / piecewise-Euclidean surface**) **with boundary**. This terminology is standard in PL topology and discrete differential geometry ([RS72], [Cox73]); "polyhedral surface with boundary" is preferable to "shell" for a mathematical readership, with "shell" retained only as an informal descriptor. **A1 caution:** naming the object "polyhedral" is a terminology / background matter; it does **not** by itself establish that the object is a PL manifold with boundary. The manifold hypotheses are verified for this specific object in §5 (below). The remaining terms are standard and used correctly:

| Term | Standard? | Source | Note |
|---|---|---|---|
| annulus / cylinder | yes | [Massey91], [GX13] | genus-$0$ orientable surface with $2$ boundary circles |
| polygonal / polyhedral / piecewise-linear surface | yes | [RS72], [Cox73] | **preferred over "shell"** |
| crease / hinge / fold | yes | [DO07], [Tachi09] | rigid-origami / folding vocabulary |
| boundary component | yes | [Massey91], [Hatcher02] | the two rims |
| vertex link | yes | [RS72, Ex. 2.21(1)] | for a $2$-complex: PL circle (interior) or arc (boundary); here every link is an arc |
| dihedral angle | yes | [Cox73], [Cox69] | interior wedge |
| outward-normal angle | yes | [Cox73, §10.7] (convention) | supplement of the interior dihedral |
| point group $D_{3h}$ | yes | [Cotton90], [AH94], Schoenflies | order $12$; $\cong D_3\times C_s$ |

## 3. Component-by-component classification

| Paper C ingredient | Closest established concept | Best refs | Classification | What is model-specific |
|---|---|---|---|---|
| $s=\sqrt2-1$ under unit flat-to-flat normalization | regular-octagon edge/apothem/circumradius trigonometry | [Cox73], [Cox69] | **STANDARD** (identity); the normalization choice is a convention | choosing $w=1$; nothing new in the identity |
| three-octagon **hinged realization** | hinged polygonal panels; rigid-origami fold about crease lines | [DO07], [Tachi09] | **MODEL_SPECIFIC_CONSTRUCTION** (the assembly); hinged-fold context STANDARD | this particular reversed-orientation, three-panel assembly |
| general-$\beta$ closure $1-2\cos\beta=0$ | law of cosines / planar rotation about a hinge | [Cox69], [DO07] | **MODEL_SPECIFIC_DERIVATION**; method elementary/STANDARD | the closure equation *for this fold* and its $\beta=\tfrac{\pi}{3}$ root |
| $18$-vertex / $21$-edge / $3$-face welded complex | Euler characteristic of a CW/simplicial complex | [Hatcher02], [Massey91] | **MODEL_SPECIFIC_DERIVATION**; $\chi$ machinery STANDARD | the specific incidence counts of this weld |
| annulus classification ($g=0$, sphere minus $2$ discs) | classification of compact orientable surfaces with boundary, $\chi=2-2g-b$ | [Massey91], [GX13] | **STANDARD_SPECIALIZATION**; the shell's hypotheses are model-specific | verifying connected/compact/orientable/mfld-with-bdry/$b=2$ *for this surface* |
| manifold-with-boundary via **vertex links** | for a $2$-complex, each vertex link a PL circle (interior) or arc (boundary) | [RS72, Ex. 2.21(1)] | **STANDARD** (dimension-specific criterion); application model-specific | that every vertex link here is an arc, so all $18$ vertices are boundary vertices |
| equilateral central cross-section (side $1$) | planar section of a polyhedral surface | [Cox69] | **MODEL_SPECIFIC_DERIVATION** | the section geometry of this shell |
| $60^\circ$ interior dihedral / $120^\circ$ outward-normal separation | dihedral vs face-normal angle conventions (supplements) | [Cox73, §10.7] | **STANDARD** convention; values are **MODEL_SPECIFIC_DERIVATION** | the specific $60^\circ/120^\circ$ for this fold |
| $45^\circ$ **chamfer-edge** inclination | edge inclination vs plane inclination (a face-plane is vertical) | [Cox69] | **MODEL_SPECIFIC_DERIVATION**; trig STANDARD | the specific edge inclination |
| $3$D notch angle $\arccos(3/4)$ | angle between two space vectors (dot product) | [Cox69] | **MODEL_SPECIFIC_DERIVATION** | the notch geometry of this shell; `NO_CLOSE_PRECEDENT_LOCATED` |
| projected $60^\circ$ notch (vs spatial) | orthogonal projection of a space angle | [Cox69] | **MODEL_SPECIFIC_DERIVATION**; projection STANDARD | the spatial-vs-projected distinction here |
| rim **hexagon decomposition** / partition identity | polygon area by shoelace; region partition | [Cox69] | **MODEL_SPECIFIC_DERIVATION** | the specific hexagon+notch partition |
| **$D_{3h}$ full symmetry** of the shell | Schoenflies point group $D_{3h}\cong D_3\times C_s$ (order $12$) | [Cotton90], [AH94], [Bishop93] | group $D_{3h}$ **STANDARD**; that *this* shell has exactly $D_{3h}$ is **MODEL_SPECIFIC_DERIVATION** | the upper-bound proof and realization are Paper C's |
| exact-coordinate / symbolic **verification** | exact geometric computation; robust predicates; analysis vs implementation | [Yap97], [KMPSY08], [Shewchuk97] | **STANDARD** methodology | the specific predicate suite for this shell |

## 4. Answers to the work order's specific questions

**Regular-octagon metrics / normalization.** $s=\sqrt2-1$ for a unit flat-to-flat octagon, apothem $\tfrac12$, circumradius $\tfrac{s}{2}\sqrt{4+2\sqrt2}$, interior angle $135^\circ$ are elementary regular-polygon trigonometry ([Cox73], [Cox69]). `REGULAR_POLYGON_BACKGROUND_STANDARD = YES`. Do not present these as contributions.

**Hinged panels / folding.** Folding rigid polygonal panels about crease/hinge lines is the subject of geometric folding and rigid origami ([DO07], [Tachi09]). These support the *vocabulary and setting* of the construction (`CONTEXT_ONLY`), not the specific three-octagon assembly, which is model-specific.

**Surfaces with boundary / Euler characteristic.** The classification of compact surfaces with boundary and $\chi=2-2g-b$ for connected orientable surfaces with $b$ boundary components is standard ([Massey91], [GX13], [Hatcher02]). `SURFACE_CLASSIFICATION_BACKGROUND_STANDARD = YES`. The reference supplies the theorem; **Paper C supplies the hypotheses for this shell** ($g=0$, annulus).

**Vertex links as manifold test.** The PL criterion is dimension-specific: for a $2$-dimensional simplicial triangulation, each vertex link is a PL circle (interior vertex) or a PL closed interval / arc (boundary vertex) ([RS72, Exercise 2.21(1)]). The literature supplies the general criterion; the actual links here are each an arc, so all $18$ vertices are boundary vertices — that computation is done in the manuscript, not imported. `VERTEX_LINK_BACKGROUND_FOUND = YES`.

**Dihedral vs normal conventions.** Interior dihedral and outward-normal separation as supplements is a standard convention ([Cox73, §10.7]). `DIHEDRAL_CONVENTION_BACKGROUND_FOUND = YES`. This convention is a geometry citation, **not** a point-group citation — [Cotton90] is used only for the Schoenflies $D_{3h}$ material below, not for this angle convention. The manuscript's careful three-way distinction (fold magnitude vs dihedral vs normal) is good practice, not a new result.

**$D_{3h}$ group.** $D_{3h}$ in Schoenflies notation, order $12$, $\cong D_3\times C_s$, with a $C_3$ principal axis, three $\sigma_v$ planes, one $\sigma_h$ plane, $2S_3$, and three $C_2'$ axes, is standard point-group theory ([Cotton90], [AH94], [Bishop93]; Schoenflies notation). `D3H_GROUP_BACKGROUND_FOUND = YES`. **The literature supports the group *terminology*, not the theorem that this shell realizes $D_{3h}$** — that is proved in Paper C (lower bound + crease-segment upper bound).

**Computational verification.** Exact/symbolic arithmetic in computational geometry and the analysis-vs-implementation distinction are established ([Yap97], [KMPSY08], [Shewchuk97]). `COMPUTATIONAL_GEOMETRY_BACKGROUND_FOUND = YES`. These support the *methodology*; the specific 51-predicate suite is Paper C's.

**The exact three-octagon shell.** Searches around "three hinged regular octagons," "octagon triangular-prism shell," "folded octagonal panels," etc. returned only ordinary **octagonal prisms** (eight rectangles capped by two octagons; symmetry $D_{8h}$ — a different object) and augmented prisms. **No close precedent was located in the focused search** for this specific three-octagon welded polyhedral surface. `CLOSE_PRECEDENT_FOR_EXACT_THREE_OCTAGON_SHELL_FOUND = NO`; `NOVELTY_UNRESOLVED`.

## 5. What is genuinely model-specific (the contribution surface)

1. **The exact coordinate construction** of this specific three-octagon welded polyhedral surface (closed-form $18$ vertices; general-$\beta$ fold maps; the closure equation and $\beta=\tfrac{\pi}{3}$ solution). `MODEL_SPECIFIC_CONSTRUCTION`.
2. **The complete geometric characterization**: topology ($18/21/3$, $\chi=0$, annulus with the hypotheses verified), the equilateral unit central section, the $60^\circ/120^\circ$ dihedral/normal values, the $45^\circ$ chamfer-edge inclination, the spatial notch $\arccos(3/4)$ vs projected $60^\circ$, the rim/hexagon partition, and the theorem that its exact symmetry group is $D_{3h}$. `MODEL_SPECIFIC_DERIVATION`.
3. **No near-identical object located.** `NO_CLOSE_PRECEDENT_LOCATED`, `NOVELTY_UNRESOLVED`.

None of these justifies a novelty claim; they are what a specific exact-construction paper naturally contributes.

## 6. Tempting but inappropriate attributions (to avoid)

- Do **not** cite [DO07]/[Tachi09] as establishing *this* shell or its closure/kinematics; they establish the folding/hinge *setting* only (`CONTEXT_ONLY`).
- Do **not** cite [Massey91]/[GX13] as proving the shell is an annulus; they prove the *classification theorem*. Paper C supplies the hypotheses.
- Do **not** cite [Cotton90]/[AH94] as proving the shell has $D_{3h}$; they define the *group*. Paper C proves the shell realizes it. Do **not** cite [Cotton90] for the polyhedral outward-normal / interior-dihedral angle convention — that is [Cox73, §10.7]; Cotton is a point-group citation only.
- Do **not** treat "polyhedral surface" (terminology, [RS72]/[Cox73]) as establishing that this object is a PL manifold with boundary — the local manifold hypotheses are established here in §5, not by the name.
- Do **not** promote $s=\sqrt2-1$, $\chi=2-2g-b$, dihedral conventions, or $D_{3h}$ group theory as contributions — they are standard background.
- Do **not** write "novel" from the absence of a precedent; write "no close precedent was located in the focused search."

## 7. Verdict

```
PAPER_C_LITERATURE_CONTEXT = COMPLETE   (focused pass; not an exhaustive survey)

REGULAR_POLYGON_BACKGROUND_STANDARD = YES
SURFACE_CLASSIFICATION_BACKGROUND_STANDARD = YES
VERTEX_LINK_BACKGROUND_FOUND = YES
DIHEDRAL_CONVENTION_BACKGROUND_FOUND = YES
D3H_GROUP_BACKGROUND_FOUND = YES
COMPUTATIONAL_GEOMETRY_BACKGROUND_FOUND = YES

CLOSE_PRECEDENT_FOR_EXACT_THREE_OCTAGON_SHELL_FOUND = NO
MODEL_SPECIFIC_CONSTRUCTION_IDENTIFIED = YES

NOVELTY_CLAIM_JUSTIFIED = NO
NOVELTY_STATUS = UNRESOLVED

MATHEMATICS_CHANGED = NO
MANUSCRIPT_CHANGED = NO
KERNEL_TOUCHED = NO

RECOMMENDED_POSITIONING = CONSERVATIVE
READY_FOR_REFERENCED_MANUSCRIPT = YES
```

The machinery is standard; the instance — the exact construction and complete characterization of this three-octagon polyhedral surface — is model-specific with no close precedent located. A referenced manuscript can proceed by citing the standard frameworks as background and framing the contribution conservatively (see `PAPER_C_POSITIONING_NOTE_v0.2.md`).
