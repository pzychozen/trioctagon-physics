# SIM04: the six-point group's scale and relative shape

Hilmir, the six points do more than become a smaller copy of their earlier arrangement. Their relative separations change as well. They remain spread in three dimensions, with a more uneven directional spread near the end. That is a measurable shape change without needing to name a solid.

**NEW ANALYSIS / VISUALIZATION OF SIM04 HISTORICAL DATA.** No SIM04 simulation was run. The unchanged [deep trajectory](originals/SIM04/deep_trajectory.csv) supplies positions and amplitudes. The accepted [GPT review](context/SIM04_GPT_REVIEW/SIM04_GPT_SCIENTIFIC_REVIEW.md) supplies the selection and prior component finding. Its retained directed-neighbor table independently confirms all30 internal selections and no cross-boundary selections at every pass5–20. The new coordinate-based component calculation agrees. The accepted package is untouched.

## Defined finite question and methods

The fixed IDs are **10,15,27,30,33,47**, over exactly16 saved states, passes5–20. Their weak component is also the complete directed six-node graph in these records: each point chooses the other five. Graph connectivity says nothing by itself about polyhedral coordinates.

For each state use the unweighted arithmetic centroid, Y_i=X_i−mean(X), `C=(1/6)ΣY_iY_iᵀ`, Rg=sqrt(trace C), and diameter=max pair distance. Eigenvalues are ordered descending. A negative eigenvalue within `1e−12*max(1,trace C)` is treated as floating roundoff and clamped to zero; a more negative value fails the check. Fractions are λ/trace, with zero fractions by convention only when trace≤1e−24. No recorded state approaches that zero-trace branch; all raw minimum eigenvalues are positive.

All15 pairs retain their original IDs and are divided by the same state's Rg. No nearest-pair or ranked-pair substitution is used. The [16-row geometry table](analysis/SIM04_six_geometry.csv) and [240 pair measurements](analysis/SIM04_six_normalized_pairs.csv) are complete.

| Quantity | Pass5 | Pass20 |
|---|---:|---:|
| Diameter | 2.170026613 | .073785244 |
| Rg | 1.036195894 | .035947985 |
| λ1 | .490870627 | .000691851255 |
| λ2 | .297262535 | .000357704136 |
| λ3 | .285568769 | .000242702209 |
| Fractions λ1,λ2,λ3 | .457176,.276858,.265967 | .535382,.276806,.187813 |

**OBSERVED IN HISTORICAL DATA / DERIVED:** diameter becomes about29.4 times smaller. It is not strictly decreasing: pass18=.104807911, pass19=.107004762, a rebound of .002196850, followed by .073785244 at pass20. Rg continues decreasing over this interval.

The minimum covariance fraction ranges from .0731862 to .272665 over the16 states. At pass19 it is .0731862, then returns to .187813 at pass20. Thus the group has positive spread in all three directions, while its relative directional distribution varies. No categorical “planar/nonplanar” cutoff is introduced. The largest endpoint change in normalized pair distance is IDs27–33: 1.227644 Rg units at pass5 versus1.983691 at pass20, a change of .756047. Uniform shrinking and any rigid rotation would preserve these normalized distances, so scale change alone cannot explain the saved sequence.

![Whole-field context](figures/F06_SIM04_context.png)

**Historical whole-field context:** saved passes0,5,10,20 use common equal scales. The fixed six are highlighted; before pass5 they are a selected set within the larger connected graph. Small points overlap at the final whole-field viewing scale; they have not been collapsed into one numerical point.

![Relative shape and scale](figures/F07_SIM04_scale_and_shape.png)

**Six-point detail:** passes5,10,20 are centered and divided by their own Rg; equal axes and fixed world-coordinate orientation are retained. No rigid alignment is performed, so apparent orientation changes in these panels include rotation as well as deformation. The covariance fractions and identity-preserving normalized distances supply rotation-invariant shape information. No edges, filled hulls or inferred faces are drawn. Had all graph links been displayed,15 undirected links would stand for30 directed selections, not physical faces.

This addendum completes the geometry question for the selected historical window. It adds no infinite-time conclusion, physical body identification or new path-inheritance claim. The similarly indexed six points in Infinity are replay evidence from a changed recurrence and random schedule, not a controlled causal comparison.
