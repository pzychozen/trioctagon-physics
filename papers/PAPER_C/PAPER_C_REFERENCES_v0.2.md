# Paper C — References v0.2

Formal bibliography for `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md`. Supersedes v0.1: the citation closeout removed **Bishop93** from the publication set (uncited), cleaned the Cox69 / Tachi09 / RS72 / AH94 / KMPSY08 metadata records, and replaced the blanket "all metadata verified" status with the honest checked-vs-production split. The **publication citation set is 13 tags**, matching the manuscript. **Every reference is background / terminology; none supports a model-specific theorem of Paper C.** The mathematics is unchanged.

Tags match the in-text citations of the v0.3.1 manuscript.

---

## Regular-polygon and Euclidean geometry

**[Cox73]** H. S. M. Coxeter. *Regular Polytopes.* 3rd ed., Dover, 1973. ISBN 0-486-61480-8. — Regular-polygon/polytope metric relations (edge, apothem, circumradius, interior angle); "polyhedral" terminology.

**[Cox69]** H. S. M. Coxeter. *Introduction to Geometry.* 2nd ed., John Wiley & Sons, 1969. — Euclidean plane/solid geometry: polygon trigonometry, dihedral angles, projection, angle between vectors. *(The ISBN 0-471-50458-0 belongs to the later Wiley Classics Library paperback manifestation, not the original 1969 printing; omitted here to avoid mixing manifestations.)*

## Hinged panels / folding / rigid origami

**[DO07]** E. D. Demaine, J. O'Rourke. *Geometric Folding Algorithms: Linkages, Origami, Polyhedra.* Cambridge University Press, 2007. ISBN 978-0-521-85757-4. DOI [10.1017/CBO9780511735172](https://doi.org/10.1017/CBO9780511735172). — The mathematical setting of folding rigid polygonal panels about hinge/crease lines.

**[Tachi09]** T. Tachi. "Simulation of Rigid Origami." In R. J. Lang (ed.), *Origami 4: Fourth International Meeting of Origami Science, Mathematics, and Education*, A K Peters, 2009, pp. 175–187. ISBN 978-1-56881-408-3. — Rigid-panel folding about creases as a kinematic model. *(Print pages checked against the author's institutional bibliography; this is the print manifestation. A different DOI-linked online manifestation exists with different pagination and is deliberately not mixed in here; no DOI added in this citation.)*

## Surfaces with boundary / Euler characteristic / classification

**[Massey91]** W. S. Massey. *A Basic Course in Algebraic Topology.* Springer, Graduate Texts in Mathematics 127, 1991. ISBN 978-0-387-97430-9. — Classification of compact surfaces with and without boundary; Euler characteristic; $\chi=2-2g-b$ for connected orientable surfaces with $b$ boundary components.

**[GX13]** J. Gallier, D. Xu. *A Guide to the Classification Theorem for Compact Surfaces.* Springer, Geometry and Computing 9, 2013. ISBN 978-3-642-34363-6. DOI [10.1007/978-3-642-34364-3](https://doi.org/10.1007/978-3-642-34364-3). — Modern exposition of the classification of compact surfaces with boundary; genus/boundary bookkeeping.

**[Hatcher02]** A. Hatcher. *Algebraic Topology.* Cambridge University Press, 2002. ISBN 978-0-521-79540-1. — Euler characteristic of a CW/simplicial complex.

## Piecewise-linear topology / vertex links / polyhedral surfaces

**[RS72]** C. P. Rourke, B. J. Sanderson. *Introduction to Piecewise-Linear Topology.* Springer, Ergebnisse der Mathematik und ihrer Grenzgebiete 69, 1972; **1982 revised Study Edition printing** (ISBN 3-540-11102-6), DOI [10.1007/978-3-642-81735-9](https://doi.org/10.1007/978-3-642-81735-9) (attached to that edition). — PL manifolds; the vertex-link criterion for a 2-manifold with boundary (each vertex link a PL circle or closed interval, Exercise 2.21(1)); "polyhedral / piecewise-linear surface" terminology.

## Point groups / $D_{3h}$ / Schoenflies notation

**[Cotton90]** F. A. Cotton. *Chemical Applications of Group Theory.* 3rd ed., Wiley, 1990. ISBN 0-471-51094-7. — Schoenflies point-group / $D_{3h}$ material **only**: $D_{3h}$ (order 12; $C_3$, $3C_2'$, $\sigma_h$, $2S_3$, $3\sigma_v$); character tables. (Not a source for the polyhedral dihedral / outward-normal angle convention — that is [Cox73, §10.7].)

**[AH94]** S. L. Altmann, P. Herzig. *Point-Group Theory Tables.* Clarendon Press, Oxford, 1994. ISBN 0-19-855226-2. — Authoritative point-group tables, including $D_{3h}$ classes and $D_{3h}\cong D_3\times C_s$ (order 12).

## Exact / robust computational geometry

**[Yap97]** C. K. Yap. "Towards exact geometric computation." *Computational Geometry: Theory and Applications* **7**(1–2):3–23, 1997. DOI [10.1016/0925-7721(95)00040-2](https://doi.org/10.1016/0925-7721(95)00040-2). — The exact-geometric-computation (EGC) paradigm.

**[KMPSY08]** L. Kettner, K. Mehlhorn, S. Pion, S. Schirra, C. Yap. "Classroom examples of robustness problems in geometric computations." *Computational Geometry: Theory and Applications* **40**(1):61–78, 2008. DOI [10.1016/j.comgeo.2007.06.003](https://doi.org/10.1016/j.comgeo.2007.06.003). — Floating-point robustness failures; the value of exact predicates.

**[Shewchuk97]** J. R. Shewchuk. "Adaptive precision floating-point arithmetic and fast robust geometric predicates." *Discrete & Computational Geometry* **18**(3):305–363, 1997. DOI [10.1007/PL00009321](https://doi.org/10.1007/PL00009321). — Exact/robust geometric predicates.

---

## Verification note (Sep 2026)

| Tag | Status |
|---|---|
| Yap97 | confirmed — Comput. Geom. 7(1–2):3–23, 1997, DOI 10.1016/0925-7721(95)00040-2 (OpenAlex/ScienceDirect) |
| KMPSY08 | confirmed — Comput. Geom. 40(1):61–78, 2008, DOI 10.1016/j.comgeo.2007.06.003 (dblp/ScienceDirect) |
| Shewchuk97 | confirmed — Discrete Comput. Geom. 18(3):305–363, 1997, DOI 10.1007/PL00009321 (Springer/dblp) |
| DO07 | confirmed — Cambridge UP 2007, ISBN 978-0-521-85757-4, DOI 10.1017/CBO9780511735172 |
| RS72 | resolved — Springer Ergebnisse 69, 1972; 1982 revised Study Edition printing, ISBN 3-540-11102-6; DOI 10.1007/978-3-642-81735-9 attached to that edition |
| AH94 | confirmed — Clarendon Press/Oxford, 1994, ISBN 0-19-855226-2 |
| Cox69 | clarified — John Wiley & Sons, 2nd ed. 1969; ISBN omitted (belongs to the later Wiley Classics paperback manifestation) |
| Tachi09 | print manifestation completed — *Origami 4* (4OSME), A K Peters, 2009, pp. 175–187; print pages checked against the author's institutional bibliography; DOI-linked online manifestation (different pagination) deliberately not merged |
| Bishop93 | removed from this publication-bibliography file (uncited); retained as non-publication research context only in `PAPER_C_REFERENCE_LEDGER_v0.2.md` |

The final publisher/venue typesetting check — especially the choice of the Tachi print vs. online manifestation — remains a distinct production step. The **selected publication citation set** (13 tags, matching the manuscript) is internally consistent.

```
REFERENCE_METADATA_CHECKED = YES
PRODUCTION_METADATA_VERIFICATION_COMPLETE = NO
METADATA_RECORDS_REQUIRING_CLARIFICATION_OR_COMPLETION = 0
SELECTED_PUBLICATION_CITATION_SET_READY = YES
```
