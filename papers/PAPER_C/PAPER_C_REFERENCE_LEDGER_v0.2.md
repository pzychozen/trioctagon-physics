# Paper C — Reference Ledger v0.2

Annotated bibliography for the literature-context pass on `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.2.2.md`; companion to the citation-closeout manuscript `DRAFT_v0.3.1`. Located by focused web search (Sep 2026). Every entry is **background / terminology**; none supports a model-specific theorem of Paper C. No manuscript was edited.

**v0.2 update (citation closeout).** Three claim-scope corrections and a metadata cleanup, mathematics unchanged:
- **RS72 vertex-link claim made dimension-specific.** The criterion cited is the $2$-dimensional case: for a $2$-complex, each vertex link is a PL circle (interior) or a PL arc/closed interval (boundary) — [RS72, Exercise 2.21(1)]. RS72 is no longer credited with a general all-dimension "sphere/ball" phrasing in Paper C's usage.
- **Cotton90 claim limited to the point group.** [Cotton90] supports the Schoenflies $D_{3h}$ material only. It is **no longer cited for the polyhedral interior-dihedral / outward-normal angle convention**; that convention is [Cox73, §10.7].
- **Bishop93 marked non-publication.** [Bishop93] is background/research context, **not** in the manuscript's publication citation set (13 tags) and not cited in `DRAFT_v0.3.1`.
- **Metadata placeholders resolved.** The "(verify at typesetting)" flags on Cox69, Tachi09, RS72, AH94, KMPSY08, DO07 are replaced with the checked records below. What genuinely remains a production step — the Tachi print-vs-online manifestation choice — is stated as such, not as an open metadata error.

For each source: **REFERENCE · WHAT IT ACTUALLY SUPPORTS · WHERE PAPER C COULD CITE IT · DIRECT/CONTEXT_ONLY · CLAIM LIMIT.**

---

## A. Regular-polygon metrics

**[Cox73]** H. S. M. Coxeter, *Regular Polytopes*, 3rd ed., Dover, 1973. ISBN 0-486-61480-8.
- **Supports:** regular-polygon and polytope metric relations (edge, apothem/inradius, circumradius, interior angle); "polyhedral" vocabulary; the interior-dihedral / outward-normal angle convention (§10.7).
- **Cite at:** §2 (octagon size measures $s=\sqrt2-1$, apothem $\tfrac12$, circumradius); §7 (dihedral/outward-normal convention, §10.7); terminology.
- **DIRECT** (for the standard identities and the angle convention).
- **Claim limit:** supports the *elementary identities, the angle convention, and terminology* only, not the specific normalization choice, the specific $60^\circ/120^\circ$ values, or any shell property.

**[Cox69]** H. S. M. Coxeter, *Introduction to Geometry*, 2nd ed., John Wiley & Sons, 1969. *(ISBN omitted: 0-471-50458-0 belongs to the later Wiley Classics Library paperback manifestation, not the original 1969 printing; not mixed in.)*
- **Supports:** planar/solid Euclidean geometry — polygon trigonometry, dihedral angles, projection, angle-between-vectors. The polyhedral interior-dihedral / outward-normal angle convention is [Cox73, §10.7] (see [Cox73]).
- **Cite at:** §2, §6–§8 (dihedral, section, notch, projection) as standard background.
- **CONTEXT_ONLY.**
- **Claim limit:** general methods; none of Paper C's specific values.

## B. Hinged panels / folding / rigid origami

**[DO07]** E. D. Demaine, J. O'Rourke, *Geometric Folding Algorithms: Linkages, Origami, Polyhedra*, Cambridge University Press, 2007. ISBN 978-0-521-85757-4. DOI 10.1017/CBO9780511735172. *(confirmed)*
- **Supports:** the mathematical setting of folding rigid polygonal panels about hinge/crease lines; "crease", "hinge", "fold" vocabulary; polyhedra folding.
- **Cite at:** §1, §3 (three-face hinged construction) as background for the folding setting.
- **CONTEXT_ONLY.**
- **Claim limit:** establishes the *field and vocabulary*, **not** this three-octagon assembly, its closure, or its kinematics. Do not cite as precedent for the shell.

**[Tachi09]** T. Tachi, "Simulation of Rigid Origami," in R. J. Lang (ed.), *Origami 4: Fourth Int. Meeting of Origami Science, Math., and Education (4OSME)*, A K Peters, 2009, pp. 175–187. ISBN 978-1-56881-408-3. *(Print manifestation; pages checked against the author's institutional bibliography. A DOI-linked online manifestation with different pagination exists and is deliberately not merged; the print-vs-online choice is a production step, not an open error. No DOI added here.)*
- **Supports:** rigid-panel folding about creases as a kinematic model.
- **Cite at:** §3 as background that folding rigid panels about hinges is an established construction genre.
- **CONTEXT_ONLY.**
- **Claim limit:** genre/vocabulary only; no claim about this shell. (Paper C makes no physical/kinematic folding-motion claim.)

## C. Surfaces with boundary / Euler characteristic / classification

**[Massey91]** W. S. Massey, *A Basic Course in Algebraic Topology*, Springer GTM 127, 1991. ISBN 978-0-387-97430-9.
- **Supports:** classification of compact surfaces (with and without boundary); Euler characteristic; $\chi=2-2g-b$ for connected orientable surfaces with $b$ boundary components; annulus/cylinder as genus-$0$, $b=2$.
- **Cite at:** §5 Theorem 1b (annulus classification), the $\chi=2-2g-b$ step.
- **DIRECT** (for the general theorem).
- **Claim limit:** supplies the classification theorem; **Paper C supplies the hypotheses** (connected, compact, orientable, manifold-with-boundary, $b=2$) for this shell.

**[GX13]** J. Gallier, D. Xu, *A Guide to the Classification Theorem for Compact Surfaces*, Springer, Geometry and Computing vol. 9, 2013. ISBN 978-3-642-34363-6. DOI 10.1007/978-3-642-34364-3.
- **Supports:** a modern exposition of the classification of compact surfaces **with boundary**, Euler characteristic and the normal-form/genus–boundary bookkeeping.
- **Cite at:** §5 Theorem 1b, as an accessible companion reference to [Massey91].
- **DIRECT** (general theorem).
- **Claim limit:** same as [Massey91] — theorem only, not the shell's hypotheses.

**[Hatcher02]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. ISBN 978-0-521-79540-1.
- **Supports:** Euler characteristic of a CW/simplicial complex; surfaces.
- **Cite at:** §5 (the $\chi=V-E+F$ computation) as standard background.
- **CONTEXT_ONLY.**
- **Claim limit:** general definition; the $18/21/3$ counts are Paper C's.

## D. Piecewise-linear topology / vertex links / polyhedral surfaces

**[RS72]** C. P. Rourke, B. J. Sanderson, *Introduction to Piecewise-Linear Topology*, Springer, Ergebnisse der Mathematik und ihrer Grenzgebiete 69, 1972; **1982 revised Study Edition printing**, ISBN 3-540-11102-6, DOI 10.1007/978-3-642-81735-9 (attached to that edition).
- **Supports:** PL manifolds; the **link of a vertex** and, **for a $2$-dimensional simplicial triangulation**, the criterion that each vertex link is a PL **circle** (interior vertex) or a PL **closed interval / arc** (boundary vertex) — [Exercise 2.21(1)]; here every link is an arc; "polyhedral / piecewise-linear surface" terminology.
- **Cite at:** §5 Theorem 1b (vertex-link manifold-with-boundary argument); terminology ("polyhedral surface").
- **DIRECT** (for the dimension-specific criterion and terminology).
- **Claim limit:** supplies the general PL criterion (in the $2$-dimensional form used) and the "polyhedral surface" terminology **only**; naming the object "polyhedral" is background, and RS72 does **not** by itself establish that this object is a PL manifold with boundary — the verification that every vertex link of *this* surface is an arc, so that all $18$ vertices are boundary vertices, is Paper C's (§5).

## E. Point groups / $D_{3h}$ / Schoenflies notation

**[Cotton90]** F. A. Cotton, *Chemical Applications of Group Theory*, 3rd ed., Wiley, 1990. ISBN 0-471-51094-7.
- **Supports:** Schoenflies point groups; $D_{3h}$ as order-$12$ with a $C_3$ principal axis, $3C_2'$, $\sigma_h$, $2S_3$, $3\sigma_v$; character table. **Point-group material only.**
- **Cite at:** §9 (the $D_{3h}$ *terminology* and element inventory).
- **DIRECT** (for the group definition/terminology).
- **Claim limit:** defines the group; **does not** establish that this shell has $D_{3h}$ (Paper C's Theorem 6 proves that), and is **not** a source for the polyhedral interior-dihedral / outward-normal angle convention — that is [Cox73, §10.7]. Cotton is not cited anywhere for the angle convention.

**[AH94]** S. L. Altmann, P. Herzig, *Point-Group Theory Tables*, Clarendon Press, Oxford, 1994. ISBN 0-19-855226-2. *(confirmed)*
- **Supports:** authoritative point-group tables, including $D_{3h}$ elements, classes, and the decomposition $D_{3h}\cong D_3\times C_s$ (order $12$).
- **Cite at:** §9 for the isomorphism $D_{3h}\cong D_3\times C_s$ and element classes.
- **DIRECT** (group tables).
- **Claim limit:** tables/terminology only.

**[Bishop93]** D. M. Bishop, *Group Theory and Chemistry*, Dover, 1993. ISBN 0-486-67355-3. **— NON-PUBLICATION background / research context; NOT in the manuscript's publication citation set (13 tags) and NOT cited in `DRAFT_v0.3.1`.**
- **Supports:** clean textbook treatment of Schoenflies point groups and $D_{nh}$ structure.
- **Cite at:** not cited in the manuscript; listed here as an alternative background source only.
- **CONTEXT_ONLY** (research context, uncited).
- **Claim limit:** background only; carries no manuscript citation.

*(Schoenflies notation itself is standard and attributable to A. Schoenflies; the group facts are covered by [Cotton90]/[AH94]/[Bishop93]. The International Tables for Crystallography, Vol. A, is an additional authoritative source if a crystallographic citation is preferred — verify at typesetting.)*

## F. Exact / symbolic computational-geometry verification

**[Yap97]** C. K. Yap, "Towards exact geometric computation," *Computational Geometry: Theory and Applications* **7**(1–2):3–23, 1997. DOI 10.1016/0925-7721(95)00040-2. *(confirmed)*
- **Supports:** the exact-geometric-computation (EGC) paradigm — exact arithmetic to guarantee correct geometric predicates.
- **Cite at:** §10 / proof audit (the exact symbolic verification approach; analysis vs implementation).
- **DIRECT** (for the methodology).
- **Claim limit:** methodology only; the specific predicate suite is Paper C's.

**[KMPSY08]** L. Kettner, K. Mehlhorn, S. Pion, S. Schirra, C. Yap, "Classroom examples of robustness problems in geometric computations," *Computational Geometry: Theory and Applications* **40**(1):61–78, 2008. DOI 10.1016/j.comgeo.2007.06.003. *(confirmed)*
- **Supports:** why exact/symbolic checks matter (floating-point robustness failures); the value of exact predicates.
- **Cite at:** §10 / proof audit (justifying exact over floating-point where the manuscript notes tolerances).
- **CONTEXT_ONLY.**
- **Claim limit:** motivates methodology; no geometric claim about the shell.

**[Shewchuk97]** J. R. Shewchuk, "Adaptive precision floating-point arithmetic and fast robust geometric predicates," *Discrete & Computational Geometry* **18**(3):305–363, 1997. DOI 10.1007/PL00009321. *(confirmed)*
- **Supports:** exact/robust geometric predicates.
- **Cite at:** §10 / proof audit as a companion methodology reference.
- **CONTEXT_ONLY.**
- **Claim limit:** methodology only.

---

## Note on completeness

This is a *focused* pass across the families named in the work order, not an exhaustive survey. No priority or novelty determination is made from absence. The exact configuration search (three hinged regular octagons folded into a triangular-prism lateral polyhedral surface) returned only ordinary octagonal prisms ($D_{8h}$, a different object) and augmented prisms; **no close precedent was located**.

Metadata status: the entries formerly flagged "(verify at typesetting)" have been checked (DOIs, ISBNs, edition/printing, page range) and the records above reflect those checks — `REFERENCE_METADATA_CHECKED = YES`. The remaining production step is not an open metadata error but a manifestation choice: the Tachi09 print vs. DOI-linked online version (different pagination). `METADATA_RECORDS_REQUIRING_CLARIFICATION_OR_COMPLETION = 0`; a final publisher-of-record spot-check before typesetting is still appropriate (`PRODUCTION_METADATA_VERIFICATION_COMPLETE = NO`).
