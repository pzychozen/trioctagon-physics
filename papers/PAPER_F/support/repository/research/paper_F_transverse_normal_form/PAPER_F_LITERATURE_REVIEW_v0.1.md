# Paper F literature review v0.1

**Bounded positioning for Paper F v0.2, 25 September 2026.** This is not a comprehensive survey or a novelty determination. The supplied Claude suggestions were leads, not citation authority. Five sources were opened and checked.

For each cited source below:

```text
SOURCE_OPENED = YES
RELEVANT_STATEMENT_LOCATED = YES
BIBLIOGRAPHIC_DETAILS_CHECKED = YES
CLAIM_SUPPORTED = YES
```

“Bibliographic details checked” refers to the particular linked version and its visible metadata. Version uncertainties are stated rather than silently assigning printed-edition pagination.

| ID | Checked bibliographic identity and link | Relevant locator | Supported use and boundary |
|---|---|---|---|
| Ab | Marco Abate, *Discrete holomorphic local dynamical systems*. Author-hosted revised chapter; the author's publication list identifies the 2010 contribution to *Holomorphic dynamical systems*, Lecture Notes in Mathematics 1998, pp.1–55. [PDF](https://pagine.dm.unipi.it/abate/articoli/artric/files/DiscHolLocDynSys.pdf); [author's publication record](https://pagine.dm.unipi.it/abate/articoli/artric/artric.html). | Checked 58-page PDF: Definition 5.9 and Proposition 5.10, printed p.35/PDF page37; Theorem 5.15, printed p.36/PDF page38. | Fixed-parameter attracting Poincare-domain linearization and formal nonresonance. The parametric result is proved in Paper F Appendix D, not attributed to this statement. |
| St | Richard P. Stanley, *Invariants of finite groups and their applications to combinatorics*, Bulletin AMS (N.S.) 1(3), 475–511, May 1979. [Author-hosted article](https://math.mit.edu/~rstan/pubs/pubfiles/38.pdf). | §4; Theorem 4.1, printed p.486; Proposition 4.7, p.488; permutation-group example, p.489 (PDF pages12,14,15). | Reflection invariants and alternating-polynomial factorization. Paper F retains its direct degree proof on the full plane. No uninspected original Chevalley/Solomon article is cited. |
| Fi | Michael Field, *Dynamics and Symmetry*, undated online author manuscript, 423-page checked version. [PDF](https://chaosbook.org/library/FieldEquiv.pdf). | §1.2 example(6), printed p.3; Definition 2.10.1 and Proposition 2.10.4, printed pp.42–43, PDF pages52–53. | Dihedral order convention and preservation of subgroup fixed spaces by equivariant maps. These are the online manuscript's locators; the 2007 printed book's pagination is not substituted. |
| Ge | Erik Gengel, Erik Teichmann, Michael Rosenblum, Arkady Pikovsky, *High-Order Phase Reduction for Coupled Oscillators*, arXiv:2007.14077v1, 28 July 2020. [PDF](https://arxiv.org/pdf/2007.14077); [metadata](https://arxiv.org/abs/2007.14077). | §2.2, equation(3), printed/PDF p.4. | Cubic complex-amplitude context. The PDF title spells the first author “Gengel”; the arXiv metadata renders “Genge”. The manuscript follows the PDF. The Euler-step comparison is Paper F's algebraic observation, not recovered historical intent. |
| Sk | Per Sebastian Skardal, Edward Ott, Juan G. Restrepo, *Cluster synchrony in systems of coupled phase oscillators with higher-order coupling*, Physical Review E 84, 036208 (2011), published 16 September. [Author-institution article](https://www.colorado.edu/amath/sites/default/files/attached-files/physreve_84_036208.pdf). | §IV, equation(36), printed p.036208-7/PDF page7. | Pure integer-harmonic pairwise sine coupling, including harmonic three. Its continuous-time population results are not asserted for Paper F's three-channel composed discrete map. |

The Field and arXiv HTML fetches initially failed through some URLs; the linked Field mirror and arXiv PDF were subsequently opened successfully. Citation decisions use the successful full-text reads, not search snippets.

## Positioning decision

Finite-group invariant theory, equivariant fixed spaces and local analytic linearization are classical ingredients. The recurrence-specific content is the explicit coefficient realization for the adopted map. No claim that the harmonic law, isotropy mechanism or projective neutrality is new in kind is made.

The amplitude comparison and harmonic-coupling comparison explain mathematical neighborhoods in the literature. They do not recover the selection rationale for epsilon, g, the seed, or the decision to compose the two substeps. Paper A remains the source definition.

The fixed-parameter analytic theorem is external. Appendix D's bounded parameter argument is supplied explicitly: finite homological elimination followed by a uniform geometric convergence estimate. It is not represented as a theorem located in a suggested book.

```text
BOUNDED_LITERATURE_POSITIONING = COMPLETE
NOVELTY_OR_PRIORITY_CLAIM = NONE
HISTORICAL_SELECTION_RATIONALE_RECOVERED = NO
```
