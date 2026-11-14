# Exact outer-envelope transitions between Crossings A and B

TRIOCTAGON_OUTER_ENVELOPE_01 · 13 November 2026 · Research author: Hilmir Frímann Halldórsson · New investigation and challenge: Codex · Returned for GPT/author review.

## 1. Object, inherited premises and scope

Let `w>0`, `h=(sqrt(2)-1)w/2`, and use the original centred frame. The 18 welded vertices and three material face cycles are Paper C v1.0.1 §4. Lexicographically ordered undirected endpoint pairs give E01–E21, with the positive direction going from the lower to the higher V-index. For every edge define

\[
m_e=(v_i+v_j)/2,\quad u_e=(v_j-v_i)/(2h),\quad
p_{e,\pm}(x)=m_e/w\pm x u_e,\quad x=t/w.
\]

The domain is exactly `[A,B]`, where `A=1/2` and `B=(1+sqrt(2))/2`. H(x) is the convex hull of unique positions of these 42 records; labels remain separate even at coincidence. The source facts are `|u_e|=1`, `m_e·u_e=0`, `|m_e|^2=w^2/3`, and hence `|p|^2=1/3+x^2`. The complete inherited coincidence theorem gives 42 distinct points throughout `(A,B)`, with 18 positions and 42 incidences at each endpoint. See S01 `def:exits`, `thm:events`, S07 §§1–3 and S16 review §2.

The same-radius exposed-point proof is inherited from S01 `prop:exposed` and S06 §4: for a point p, `p·q <= R^2`, with equality only at p. Every unique exit is therefore a hull vertex. This is not a new vertex mechanism. Three noncollinear seam positions at height `-x` and one at `+x` also make H(x) full dimensional for x>0. The checker verifies a corresponding nonzero tetrahedral determinant throughout each new domain.

The new definition extends the already declared convexification convention to the continuous A–B family. It does not adopt a material wall, dynamics, preferred radius, projection, or scale calibration. The source comparison and exact locators are in [PRIOR_WORK_COMPARISON.md](PRIOR_WORK_COMPARISON.md). Its `DISTINCT_GAP` disposition was recorded before the new scientific worker runs. No worldwide priority assertion is made.

## 2. Source concordance and calculation coordinates

All ten requested originals match their supplied Git blob identities. The 42 affine point functions were nominated from the authenticated inventory, while the decisive checker independently reconstructed the three fold maps, welded equal material vertices in panel order, deduplicated the face-cycle edges and recomputed every midpoint/direction. All 18 vertex coordinates, all three face cycles, all 21 endpoint pairs and both signs of every branch agree exactly with the original inventory. The source table and fold formulas also agree with the packet's transcription. The accepted sources remain unchanged.

For calculation only, use

\[
(X,Y,Z)=(p_x,p_y/\sqrt3,p_z).
\]

This invertible positive-determinant linear change places all coordinates in `K=Q(sqrt(2))`. It preserves convexity, coplanarity, support, incidences and cyclic polygon boundary order. Physical squared lengths use `X^2+3Y^2+Z^2`; the checker verifies this equals `1/3+x^2` for every affine branch. No metric conclusion is inferred from unweighted transformed coordinates. Physical coordinates and normals can be recovered by the inverse linear change.

Every saved field pair `[a,b]` means exactly `a+b*sqrt(2)`, with a and b rational strings. Polynomial arrays list coefficients in ascending powers of x. Empty arrays mean the zero polynomial. There are no floating values in decisive sign, root, endpoint or facet-identity tests.

## 3. Exact partition and complete face lists

Set `T=x*=3(sqrt(2)-1)/2`. The finite partition is

\[
\{A\},\quad (A,T),\quad\{T\},\quad(T,B),\quad\{B\}.
\]

The transition is the unique root of `4x^2+12x-9` in `(6213/10000,6214/10000)`. This polynomial is irreducible over Q because its discriminant 288 is not a rational square. The exact order `A<T<B` follows from the ordered-field test, or directly from `3sqrt(2)>4` and `sqrt(2)<2`. Its radius is

\[
R_*^2/w^2=1/3+T^2=85/12-9\sqrt2/2.
\]

The endpoints already have explicit exact expressions; A is rational and B satisfies `4x^2-4x-1=0`, with its positive root selected.

| Domain ID | Domain | V/E/F | Maximal polygon sizes | D3h orbit sizes |
|---|---|---|---|---|
| A | inherited singleton | 18/48/32 | 32 triangles | 6,12,6,6,2 |
| C1 | A < x < T | 42/96/56 | 36 triangles, 18 quadrilaterals, 2 hexagons | 2,6,12,6,12,6,3,3,6 |
| T | x=T | 42/84/44 | 24 triangles, 12 quadrilaterals, 8 hexagons | 2,6,12,6,6,3,3,6 |
| C2 | T < x < B | 42/90/50 | 24 triangles, 24 quadrilaterals, 2 hexagons | 2,6,12,6,6,3,6,3,6 |
| B | inherited singleton | 18/36/20 | 8 triangles, 12 quadrilaterals | 6,6,3,3,2 |

The ordering of an orbit list is bookkeeping, not a matching of orbit identities across domains. [FACE_REPRESENTATIVES.md](data/FACE_REPRESENTATIVES.md) supplies all 26 new-domain orbit representatives, their explicit exact plane families, complete zero sets in cyclic order and orbit sizes. The 12 symmetry actions are computed by coefficient equality, not inferred from a picture: in calculation coordinates the 120-degree rotation is `(X,Y,Z) -> (-(X+3Y)/2,(X-Y)/2,Z)`, with reflections of X and Z. Their permutations of all 42 labels appear in the certificate. Applying them to the representatives recovers all 56, 44 and 50 faces respectively.

The full labelled records are in [exact_certificate.json](data/exact_certificate.json), including every face's defining triple and all 42 residual polynomials. [FACE_INCIDENCE_RECORDS.json](data/FACE_INCIDENCE_RECORDS.json) additionally supplies every actual polygon side, edge-to-facet incidence, vertex-to-facet incidence, vertex link, dual adjacency and limit map. Face IDs are local to a domain. Counts alone are not used as an identity test.

## 4. The proposed supporting plane and its complete zero set

Write `h1=(sqrt(2)-1)/2`. Direct substitution of the independently reconstructed branches into the proposed physical-coordinate plane gives

\[
n(x)=\left(0,-1,\frac{\sqrt3}{2}(x-h_1)\right),
\]
\[
d(x)=\frac{\sqrt6}{4}x^2+
\frac{\sqrt6-\sqrt3}{4}x+\frac{\sqrt3}{24}+\frac{\sqrt6}{16}.
\]

The residual is identically zero for E05+, E09+, E17+ and E16-. For each of E21+ and E10- it is exactly

\[
n(x)\cdot p-d(x)=-\frac{\sqrt6}{4}(x-T)(x-B).
\]

This is strictly negative on `(A,T)` and strictly positive on `(T,B)`. The first plane supports a four-vertex facet in C1 and fails to support the whole set in C2. This is an exact sign change, not a fitted numerical root.

At T, `n_*=(0,-1,sqrt(3)h1)` and `d_*=-13sqrt(3)/12+sqrt(6)`. All 42 residuals are nonpositive. Exactly these six are zero, in one outward cyclic order:

\[
(\mathrm{E05+},\mathrm{E16-},\mathrm{E21+},
  \mathrm{E09+},\mathrm{E17+},\mathrm{E10-}).
\]

[CANDIDATE_RESIDUAL_TABLE.md](data/CANDIDATE_RESIDUAL_TABLE.md) lists the complete 42-label calculation in 13 exact value classes after division by positive sqrt(3). Every nonzero row is strictly negative, including the small expression `(7-5sqrt(2))/2`, whose sign follows from `49<50`. Thus no unlisted point lies on or beyond the plane.

The normal is nonzero. The six points are distinct by the inherited noncoincidence theorem, and a straight line intersects the common sphere in at most two points, so they span a plane. The supporting zero set is therefore a genuine maximal two-dimensional face. Cyclic side tests certify the displayed hexagon rather than an arbitrary six-point coplanarity. Its exact group orbit contains six distinct facets, T/F02, F07, F17, F20, F24 and F30. Two additional hexagonal facets are the persistent upper/lower caps. No regular-hexagon assertion is required or made.

T lies strictly between the only coincidence endpoints in this domain and differs from the original event `h1<A`. It is consequently a supporting-face event with 42 distinct exits, not a fourth supporting-line incidence event.

## 5. Parameter-uniform support, order and maximality

For a proposed ordered face with first three points a,b,c, compute

\[
N=(b-a)\times(c-a),\qquad D=N\cdot a,\qquad r_l=N\cdot p_l-D.
\]

The affine coordinates make each N component degree at most two and each point residual degree at most three over K. In an open chamber, a saved face passes only if its residual is identically zero for precisely the declared labels, and strictly negative throughout the chamber for every other label. The checker recomputes these polynomials from the fold-defined coordinates and compares the actual coefficients with the saved ones before deciding signs. At T it instead substitutes the exact algebraic parameter and computes constant residuals. It explicitly rejects a missing zero label or any mixed support sign.

The checker separately proves `N·N>0` throughout the domain. For each consecutive side `(a,b)` of a proposed cycle, every other face point c must satisfy

\[
N\cdot((b-a)\times(c-a))>0.
\]

These degree-at-most-four polynomial inequalities certify the true convex polygon boundary and its outward orientation uniformly. They exclude an internal triangulation diagonal being reported as a polygon side. The strict tests also exclude collinear triples on the displayed face. No floating atan2 order is accepted without these checks. Persistent coplanar families are represented by zero polynomials, not a spurious collection of isolated roots.

### Exact sign and root basis

For `q=a+b sqrt(2)`, the sign is immediate if one term is zero or both terms have the same sign. With opposite signs, compare the rational numbers `a^2` and `2b^2`, adjusting for the sign of a. Irrationality of sqrt(2) excludes equality for nonzero rational a,b. This is exact integer/rational arithmetic and handles cancellation without a tolerance.

For a nonzero polynomial f and a chamber `(l,u)`, remove all factors `x-l` and `x-u` by exact division. This removes only boundary roots, which are allowed. Construct the Sturm sequence of the remaining polynomial by differentiation and negative Euclidean remainders over K. Multiplying a remainder by a positive field element only controls coefficient growth. At each endpoint, ignore zero sequence entries and count sign variations. Because the reduced first polynomial is nonzero at both endpoints, their difference is exactly the number of distinct real roots in the open interval. The algorithm also detects even-multiplicity roots; a dedicated rejection control tests that case.

Every nonzero support/order/normal polynomial has zero roots in its claimed chamber and the required sign at its exact field midpoint. Continuity therefore proves that sign everywhere in the chamber. No interval claim is inferred from the three floating nominations. These computations use exact ordered-field Sturm decisions rather than inexact interval arithmetic; no outward floating enclosure is needed.

The decisive run checked 6,300 point residual signs and 972 polygon-side signs over the three new domains, with 254 distinct monic sign forms after domain-aware deduplication. Those are implementation counts, not independent theorem counts. All saved residual polynomials and the checking algorithm are included; success flags are not mathematical premises.

## 6. Completeness: why no omitted face or transition remains

Fix any parameter in one of the certified open chambers or at T. Every retained polygon has a nonzero supporting plane, its entire zero set, and at least three noncollinear points. It is therefore an actual maximal facet of H(x). Every certified polygon side is an edge of that facet, hence a true ridge of the three-dimensional convex polytope H(x). The side-incidence calculation places exactly two distinct retained facets on every such ridge.

A ridge of a three-dimensional convex polytope has exactly two incident facets: a sufficiently small transverse planar section at an interior ridge point is a convex angle, with precisely its two boundary sides. Hence the retained list contains **both** neighbors across every ridge of every retained facet. It is closed under actual facet adjacency.

The facet adjacency graph of a full-dimensional convex polytope is connected. One direct argument radially projects its boundary from an interior point to a sphere. Join two facet-interior points by a path avoiding the finite projected vertices and crossing the finite edge arcs transversely. The successive facets form an adjacency path. Consequently a nonempty subset of facets closed under adjacency must contain all facets.

Applying this argument to the checked list proves completeness at **every** parameter in each domain. Connected listed facet graphs, connected cyclic vertex links and Euler's relation are additional consistency checks; they are not substituted for the support/ridge-closure argument. The proof does not assume all other quadruple coplanarities are absent. Coplanarities on nonsupporting planes or strictly within H(x) cannot add a facet to an already complete boundary list.

All complete zero sets and directed polygon cycles stay fixed within each chamber, so all edges and higher face incidences do too. There is no omitted labelled face-lattice change inside either chamber. The explicit lists differ at T, establishing it as the only interior combinatorial transition. A special metric equality inside a chamber, such as regularity of an already known latitude polygon, would not contradict this statement about the face lattice.

## 7. What changes at T and at A/B

For the representative T/F30 above, the actual neighboring faces are:

| C1: before T | T | C2: after T |
|---|---|---|
| Quadrilateral `(E05+,E16-,E09+,E17+)` | Hexagon `(E05+,E16-,E21+,E09+,E17+,E10-)` | Quadrilateral `(E05+,E16-,E21+,E10-)` |
| Triangle `(E05+,E17+,E10-)` | same maximal hexagon | Quadrilateral `(E09+,E17+,E10-,E21+)` |
| Triangle `(E09+,E16-,E21+)` | same maximal hexagon | |

The C1 interior diagonals `(E05+,E17+)` and `(E09+,E16-)` cease to be hull edges at T. The new C2 diagonal is `(E10-,E21+)`. The 12 verified group actions give six local changes of this form. There are 38 common unchanged maximal facets. The event edge set is exactly the intersection of the two chamber edge sets: 12 edges are lost and six different edges gained. [TRANSITION_READOUT.json](data/TRANSITION_READOUT.json) lists every affected face and edge.

![Computed local facet change](figures/local_facet_transition.png)

The illustration uses actual 3D patches at x=3/5, T and 2/3, physical coordinates normalized by w, and one common camera/scale. Filled polygons are maximal envelope facets. Rendering is only an illustration; label and sign decisions come from the exact certificate.

At A and B, in contrast, 42 labels merge into 18 positions. The checker evaluates each affine branch exactly and matches its coordinate and group membership against S02 and the accepted S03/S04 endpoint vertices. It then compares every saved facet cycle, complete supporting zero set and true edge with the new endpoint representation. This is a correspondence check against inherited exact faces, not a repeat of the old all-triple enumeration.

The limiting chamber polygons account for the endpoints explicitly:

| Limit | Two-dimensional face images | Edge images | Point images |
|---|---:|---:|---:|
| C1 -> A | 32 | 18 | 6 |
| C2 -> B | 20 | 24 | 6 |

The full-dimensional images cover each inherited endpoint facet exactly once; the remaining faces collapse as labels merge. All 56 C1 faces and 50 C2 faces retain dimension two at T, where some share a larger maximal supporting zero set instead. `limits` in the incidence records supplies the individual image vertices and containing endpoint/transition facets. Thus both chamber attachments are fully specified, not guessed from matching V/E/F counts.

## 8. Interpretation and exclusions

The complete closed-interval list contains only triangles, quadrilaterals and hexagons, so it has no ten-vertex maximal facet. This is narrower than excluding selected planar sections, projections, arbitrary subsets, independent enclosing objects or a differently adopted family. Global D3h symmetry alone would not establish this facet-size conclusion.

Once the inherited affine exits and convex-hull convention are fixed, the two chambers, exact noncollision transition, six local regroupings and all listed incidences follow without fitting a scale or selecting an orientation. They do not select a physical observer radius, material wall, moving-support law or native dynamics. Hull edges are derived enclosure adjacencies; drawing them does not change the original 21-line network.

The silver ratio `sigma=1+sqrt(2)` belongs to the inherited three-term along-line relation `h, sigma*h, sigma^2*h`. The new value `3h` is a supporting-face parameter, not another line meeting or an infinite recurrence. Sphere radii retain the additive `w^2/3` term. The golden ratio `phi=(1+sqrt(5))/2`, original close sphere and optional decagonal prism retain their separate definitions. No arbitrary ratio search, pi*e*phi fit, physical unit calibration, or claim about every possible metric golden-ratio relation is made.

Positive common scaling preserves all inequalities and incidences after dividing by w. A common orthogonal reflection of the whole source construction maps the hull, labels and supporting faces to the other hand. This transfers the result without changing material indexing or adopting a different construction.

## 9. Verification, controls and status

The generation program used the authenticated midpoint/direction inventory; the checker rebuilt from folds and recomputed the decisive containment, zero-set, cycle, coverage, endpoint and symmetry decisions. They share the disclosed exact rational/quadratic field and polynomial engine. This is separate checking organization, not two independent arithmetic implementations. SymPy parses exact source expressions and formats readouts; SciPy supplies only three floating nominations; neither floating tolerances nor saved nominal outputs decide a theorem.

Six coherent damaged certificates are rejected: wrong transition, inward support sign, omitted facet, incomplete zero set, swapped endpoint label and interval coverage gap. An additional even-multiplicity interior-root control is rejected, while a polynomial with roots only at chamber endpoints passes its strict interior sign test. Mutations are in-memory copies; originals and the final certificate are unchanged. See [NEGATIVE_CONTROL_RESULTS.json](data/NEGATIVE_CONTROL_RESULTS.json).

All new scientific workers used the requested Windows Command Prompt/torment environment, a 900-second wall ceiling and a 2 GiB Windows process-memory ceiling. Actual versions, bounded-worker receipts, output and reproducibility guidance are retained. No old scientific suite, historical simulation, production kernel or UI was imported or run. The repository was read-only, with before/after preservation checks reported separately from mathematical evidence.

The A–B assessment is complete and returned for GPT/author review. The proof is a mathematical argument supported by an exact finite certificate, not proof-assistant verification. Earlier papers, their accepted results and historical statuses are unchanged. No publication or sequel is performed.
