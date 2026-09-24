# MK-K1 reference scaffold v0.1: implementation and verification

Date: 24 September 2026. Implementer/checker: Codex. GPT implementation review
is **pending**; Claude implementation review was **not performed**. This is the
new Paper-D convergence packet, distinct from the original Paper-A/C task called
K1. Paper D's accepted mathematics is the specification; these new code bytes
are submitted for implementation review, not represented as already accepted.

## Location, authority and preflight

~~~text
AUTHORITATIVE CHECKOUT: C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
SOURCE EDIT TARGET:    C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\kernel_physics
BORROWED INTERPRETER:  C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe
BASE HEAD: c60e4cfa9b3e5247f522a6036657c4d6fac75da1
BRANCH: main
~~~

Git top-level and HEAD matched the order. The local `origin/main` ref matched
HEAD; this is explicitly a local tracking observation, not a fresh remote check.
No fetch, pull, reset, switch, stash or Git mutation was performed. The index and
tracked worktree were initially clean. All four proposed new paths were absent.
The initial complete status and index are retained in the JSON companion.

Four predecessor test files were already untracked: `test_boundary_pipeline.py`,
`test_boundary_response.py`, `test_operating_region.py`, and `test_srg.py`. Their
hashes match the preceding Paper-E publication preflight, so they are identified
pre-existing work, not a concurrent source discrepancy. They were included in
local discovery and preserved. An initial conservative empty-scope-status guard
was resolved by that identity comparison before source edits; nothing was stashed,
copied, deleted or overwritten to force a clean scope.

The controlling specification is
`papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md`, §§4–14, including
equations (2a), (16a) and (16b). Its HEAD blob and actual file blob both match
`84823582c45232fb27a472ba45be33dad38b1228`. The preserved root draft did not govern
the implementation. Supporting reads were the revision README, the coordinate
transcription and the accepted scaffold script/results. Neither paper helper nor
its `runtime.py` was imported or executed. Existing geometry, tests, README,
face-state conventions and directly referenced historical receipts were read.
No paper rebuild, evidence regeneration or historical-corpus search occurred.

Before testing, the actual executable and imports were printed and asserted.
Python **3.12.14**, NumPy **2.3.5**, SymPy **1.14.0** were used without installation
or upgrade. `kernel_physics`, `geometry` and `dynamics` resolved under the source
edit target. Final verification additionally checks `reference_scaffold` there.
The sibling source directory was not synchronized, edited or imported.

## Exact change set and API

Created only:

- `kernel_physics/reference_scaffold.py`
- `kernel_physics/tests/test_reference_scaffold.py`
- `kernel_physics/K1_REFERENCE_SCAFFOLD_VALIDATION.md`
- `kernel_physics/K1_REFERENCE_SCAFFOLD_VALIDATION.json`

Modified only `kernel_physics/README.md`: authoritative-location block, opt-in API
and conventions, measured test provenance, and links to these records.
No `__init__.py` export, registry, default switch, dependency change, replacement
mesh, evolution state or face-state attachment was added.

The new runtime module imports only `dataclasses`, `fractions` and SymPy. Frozen
dataclasses and nested immutable tuples hold the exact geometry. `ConvexHull`
prescribes a closed filled set of supplied generators; it is not a Boolean hull
engine or a material declaration. `HalfPlane` and `HalfPlaneIntersection` expose
the closed inequalities, with no tolerance. `Octagon` distinguishes its ordered
vertices, eight-segment closed outline and filled hull.

`ReferenceScaffold(s,g_gap)` uses positive gap coordinates. `from_radius(s,p)`
requires the equivalent positive directed coefficient, and `regular(s)` selects
equal side classes. The object exposes ordered endpoints/edges, metrics, support
triangle/cells/half-planes, complete planar frames and the separate vertical
reference figures. It never supplies a replacement `FoldedModule`.

`paper_c_member(s)`, `paper_c_rigid_map(point,s)`,
`translate_paper_c_to_regular(s)` and `shrink_paper_c_at_fixed_centres(s)` have named
starting conditions. The shrink function always constructs the Paper-C-family
starting member, rather than accepting an arbitrary placement and silently
applying its special factor.

Inputs are Python integers/Fractions or exact SymPy real finite expressions.
Booleans, strings, complex/nonfinite lengths and every retained `Float` atom are
rejected. There is no floating geometry layer or rationalization. Positive
symbolic `s,g_gap` are supported; independent positive `s,p` do not by themselves
prove a positive connector and are rejected if that inequality is undecidable.
Zero/negative lengths and the collapsed connector boundary are excluded.
`is_regular` returns `True`, `False` or `None`; the exact residual is retained.
Point membership also preserves an undecidable result. Finite real local
coordinate arguments describe affine maps; finite faces use their stated local
filled-octagon domain, not every point in the supporting plane.

## Equation-to-implementation-to-test ledger

Test names below are methods in `ReferenceScaffoldTests`; the common `test_`
prefix is omitted. The JSON records their complete discovered IDs and stdout.

| Printed authority | Implementation | Exact checks | Hypotheses |
|---|---|---|---|
| (1), (2), (2a) | `Octagon`, `ConvexHull` | `octagon_metrics_edges_and_filled_outline_distinction` | exact real `s>0`; filled set distinct from outline |
| (3)–(5), (11) | `RADIAL`, `TANGENT`, `A`, `B`, `vertices` | `radial_and_tangent_frames`, `printed_equation_11_oracle` | prescribed alignment/index order; independent printed six-vertex oracle |
| (6)–(10) | `selected_edges`, `connectors`, `side_lengths`, `from_radius` | `directed_edges_connectors_and_closure`, `positive_lengths_turns_and_interior_angles`, `radius_parameterization_is_exact` | positive directed connector, not an absolute distance alone |
| (12)–(14) | `circumradius_squared`, `area`, `q_H`, regularity | `circumcircle_shoelace_and_dissection_area`, `regular_member_metrics_and_unknown_equality` | generic positive `s,g_gap`; regular specialization explicitly selected |
| (15)–(16) | support triangle and corner hulls | `support_triangle_and_equilateral_corner_cells`, `global_convex_support_nonoverlap_certificate` | `W=s+2*g_gap>2*g_gap`; closed convex construction |
| (16a–b) | six half-planes, `filled_hexagon` | `every_vertex_all_halfplanes_and_exact_active_edges`, `connector_retention_apex_and_outer_leg_exclusion` | every vertex/all six inequalities; exact active edges; boundary retention |
| §10 | ordered E/G roles and complete-frame centres | `c3_covariance_and_reflection`, `regular_d6_role_d3_and_traversal_c3`, `exact_nonregular_witnesses` | class preservation differs from fixed labels and traversal |
| (17)–(18) | planar centres/maps/full frames | `complete_planar_frames_and_inward_outline_reversal` | one published completion; no uniqueness or deployment claim |
| (19) | vertical maps/full frames/top edges | `vertical_family_full_domain_and_top_height` | centre radius `p`, top `a`; not planar radius `L` |
| (20)–(22) | `paper_c_member`, rigid map | `paper_c_rigid_formula_and_finite_vertex_edge_sets` | general local-coordinate identity at width one plus exact finite vertex/edge sets |
| (23)–(24) | named translation/shrink | `translation_and_shrink_have_distinct_consequences`, `global_similarity_preserves_gap_ratio` | special Paper-C start, fixed vertical centres for shrink |
| (25)–(27) | width-one specialization | `width_one_fixed_centre_shrink` | six sides exactly `1/3`, altered top/width, fixed support side |
| (28)–(29) | proof/test only; no distance engine | `plane_intersection_distance_decomposition_and_attaining_pair` | `p=(a+delta)/sqrt(3)`, `delta>=0`, filled faces |
| API contract | validators and immutable values | `exact_input_types_and_rejected_domains`, `membership_unknown_and_coordinate_index_validation`, `immutable_representations_and_input_preservation` | explicit symbolic uncertainty; exact inputs only |
| Integration boundary | isolated opt-in module | `runtime_import_boundary_and_no_hidden_model_import`, `existing_geometry_and_dynamics_remain_deterministic` | no new model imports/state; unchanged geometry/recurrence |

## Geometric reasoning and proof scope

**Directed chain.** Subtracting A from B gives `s*t_i`. Subtracting successive
endpoint pairs gives `g_gap*R60*t_i`. Since both coefficients are positive, the
successive exterior turns are positive 60 degrees; their dot products are
`s*g_gap/2`, determinants `sqrt(3)*s*g_gap/2`, and interior cosines `-1/2`.
The chain closes by its indexed endpoints. Those local identities alone do not
prove global convexity.

**Global support construction.** Intersecting the three selected-edge half-planes
gives an equilateral triangle of side `W=s+2*g_gap`. Each corner cut has three
equal sides `g_gap`. Its corner barycentric coordinate is at least
`1-g_gap/W>1/2`; two such cells cannot overlap because barycentric coordinates
sum to one. Each original support side retains a positive length `W-2*g_gap=s`.
Thus the six closed half-planes leave a convex polygon with precisely the six
specified positive edges. The tests verify every endpoint against every plane,
the two active constraints per vertex, and strict slack for the other four.
Linearity retains the full connector between its endpoints. At a removed apex,
connector slack is `-sqrt(3)*g_gap/2`; it is half that value at each outer-leg
midpoint. The same affine interpolation excludes every non-endpoint portion of
the outer leg. Removing ordinary open cell interiors would retain these points
and is explicitly not the API definition.

**Metrics and marking.** Endpoint orthogonality gives `R_H^2=p^2+s^2/4`.
Independent shoelace evaluation and subtraction of three equilateral corner
areas both give `sqrt(3)*(s^2+4*s*g_gap+g_gap^2)/4`. Equal sides are necessary for
regularity and, together with the already proved convex/equiangular structure,
sufficient. Hence regularity is exactly `g_gap=s`. The generic positive symbols
leave that equality undecidable, which the API reports. The regular polygon
admits the twelve D6 actions; six preserve E/G classes and only three also
preserve traversal. The test separately checks fixed edge labels. Rotating by
60 degrees exchanges E and G and fails to preserve the three complete-frame
centres, so it is not a symmetry of that arrangement.

**Completion and finite Paper-C comparison.** The planar map is an isometry
centred at `(p+a)*u_i`. Its local CCW edge indices 4-to-5 run B-to-A, whereas the
selected direction is A-to-B. The vertical map has centre `p*u_i` and top height
`a`. At `p0=a/sqrt(3)`, the 30-degree rotation and translated origin send frames
0,1,2 to P3,P1,P2. At width one, the tests compare affine formulas for arbitrary
real local coordinates, all eight finite-face vertices and all eight edges
against the current `geometry.py`, including its actual welded face cycles.
The Paper-D local vertex cycle equals `PaperC[3:]+PaperC[:3]`, a cyclic shift
without reversal. Equal finite convex-hull generators under the same affine
map establish finite-face parity; supporting-plane agreement alone is not used.
The six top measurement points retain gap ratio `1/sqrt(2)` and are distinct
from the actual nine-edge nonplanar rim.

**Tuning and separation.** Fixed-size translation changes p by
`(2-sqrt(2))*s/(2*sqrt(3))`, preserving size/top. Fixed-vertical-centre shrink solves
`sqrt(3)*p0-lambda*s/2=lambda*s` and yields `(1+sqrt(2))/3`; both local horizontal
and vertical coordinates scale. At original width one, the resulting six sides
are exactly `1/3`, `W=1`, width `(1+sqrt(2))/3`, top `(1+sqrt(2))/6`, and area
`sqrt(3)/6`. Holding planar centres fixed instead would give midpoint radius
`L-lambda*a`, so that operation is not silently identified with fixed p. A global
similarity scales s, p and the gap together and leaves their ratio invariant.

For finite-face separation, write `p=(a+delta)/sqrt(3)` with `delta>=0` and local
coordinates `xi=a-X`, `eta=-a+Y`, where `X,Y>=0` on the filled octagons. Direct
expansion for each adjacent pair gives
`delta^2+delta*(X+Y)+(X-Y)^2+X*Y+(z-z')^2`. Every excess term is nonnegative.
The points `(a,0)` and `(-a,0)` are side midpoints in the respective local hulls
and attain the bound. At delta zero, the entire common side interval is a seam;
at positive delta the finite faces are disjoint. The translated and shrunk
specializations have the printed positive separation. No assertion of this
minimum is made for `p<a/sqrt(3)`.

These are source-level proof arguments and exact algebra checks. The three fixed
nonregular witnesses `(2,1)`, `(2/3,5/4)` and `(sqrt(2),1)` are additional exact
examples, not a scan or a replacement for the generic proof. No K1 geometric
comparison uses floating arithmetic or a tolerance. One regression test calls
the unchanged NumPy recurrence before/after using the new API and compares
output bytes and untouched input bytes; that is deterministic regression
evidence, not a general numerical proof of the geometry. Existing numerical
tests retain their source-defined tolerances, including the original covering/
dynamics `rtol=atol=2e-14` and the face-view qualifications in the README.

## Test execution and coverage qualification

All test processes were launched through Windows CMD with the documented
interpreter and `-B`. An inline standard-library unittest harness captured the
same discovery/runner as the following reproducible commands, storing output
directly in the one JSON record rather than extra log files:

~~~bat
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe -B -m unittest discover -s kernel_physics/tests -v
C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe -B -m unittest kernel_physics.tests.test_reference_scaffold -v
~~~

Baseline: **95/95 passed**, zero failures/errors/skips, before implementation.
The 41-test original receipt is covering 10 + dynamics 15 + geometry 16.
`CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md` lines 170–180 records 75 tests:
those 41 plus boundary response 8, SRG 9, readouts 4, operating region 9 and
pipeline 4. `FOLDED_FACE_STATE_ATTACHMENT_v0.1.md` lines 367–368 records the
subsequent 20 face tests, giving 95. Actual current discovery agrees with that
local history. The four untracked predecessor files hold 30 of the 95 tests;
the base commit tracks 65. No tests were reconstructed or moved to manufacture
a count, and this packet does not repair that publication coverage gap.

First new focused run: **25/27 passed**. Two new assertions tested syntactic
equality of differently factored exact expressions or queried positivity before
simplification. They were corrected to exact coordinate-difference identities
and exact simplification. No geometry formula, accepted definition, old test,
source or tolerance changed. Fixed-label and attaining-pair checks were also
made explicit. The original failure output is retained in the JSON.

The first complete post-edit run passed all 27 scaffold tests but failed two
existing README tests: they require exactly one `~~~python` pipeline block, while
the newly added scaffold example initially introduced a second. Only the new
example was changed to a standard backtick Python fence. The original executable
pipeline block and both predecessor tests remain unchanged. This documentation
integration correction changes no mathematical or model behavior; its failed
run is retained separately from the final result.

Final discovery and execution: **122/122 passed: 95 preserved baseline + 27 new
K1**, zero failures/errors/skips, **49.826 seconds**. Baseline duration was
**4.358 seconds**. The final run, timings, complete IDs, results and reverified import locations are
recorded in the JSON. Counts refer to unittest methods, not theorems or subcases.
The published paper suites, historical runs and GPT/Claude checker outputs were
not rerun or added to this count.

## Preservation and limitations

The bounded pre-edit inventory contains **34 identities**: existing package
files, the five consulted Paper-D inputs and two directly cited prior reports.
The README is the sole authorized change among those identities; all other
**33** remain byte-identical. The JSON lists individual before/after hashes,
new implementation/test hashes, and exact Git status reconciliation. This is
a bounded preservation check, not a whole-filesystem integrity claim. Old test
receipts/manifests and the consulted paper/evidence bytes remain unchanged.

Fresh whitespace checks apply to all five new/changed text paths without staging;
no previous publication exception is inherited. The final JSON records actual
results. Validation-record self-hashes are not recursively embedded; Markdown,
implementation, tests and README identities are recorded in the JSON after
finalization.

No mathematical/source discrepancy or alteration of protected behavior is needed
for this packet. The documented coverage limitation is the four pre-existing
untracked test files. Implementation review remains open. The exact API rejects
unproved input-domain membership instead of attempting an unrestricted symbolic
decision procedure; it supplies neither an arbitrary-p separation engine nor
collision-free motion. Closed reference cells are not a physical field domain.
Paper C remains the existing welded geometry and face-state carrier. Papers D/E
are not declared fully implemented. No Z/clock, six-gap registration, new dynamics,
K2/K3, physical calibration, QCD/E6/E8, UI or further research was started.

No staging, commit, push, branch creation, cleanup, dependency/environment change
or PDF/publication operation is authorized or performed here.

~~~text
TASK = MK-K1_REFERENCE_SCAFFOLD
SOURCE_CHECKOUT_VERIFIED = PASS; expected base commit, main
IMPORTED_PACKAGE_PATH_VERIFIED = PASS; authoritative checkout, before and after
PAPER_D_REVISION = v0.1.1; controlling Git blob verified
REFERENCE_SCAFFOLD_IMPLEMENTATION = COMPLETE_WITHIN_K1_SCOPE
EXACT_GEOMETRY_CHECKS = PASS; generic positive symbolic inputs and fixed exact witnesses
PAPER_C_RIGID_COMPARISON = PASS; affine formulas, finite vertices and edge sets
FIXED_CENTRE_SHRINK = PASS; width-one result has six sides exactly 1/3
CURRENT_BASELINE_TEST_COUNT = 95; all pass
FINAL_TEST_COUNT = 122; all pass
BASELINE_COVERAGE_QUALIFICATION = 30 baseline tests in four preserved untracked files; 65 tracked
PROTECTED_FILES_PRESERVED = 33 of 33 protected identities; one authorized README edit
PAPER_A_DYNAMICS_CHANGED = NO
PAPER_C_WELDED_GEOMETRY_CHANGED = NO
Z_OR_CLOCK_IMPLEMENTATION_ADDED = NO
SIX_GAP_REGISTRATION_ADDED = NO
K2_OR_K3_STARTED = NO
COMMIT_OR_PUSH_PERFORMED = NO
GPT_IMPLEMENTATION_REVIEW = PENDING
CLAUDE_IMPLEMENTATION_REVIEW = NOT_PERFORMED
~~~

## R1 — symbolic-domain preservation correction, 24 September 2026

Task: `MK-K1-R1_SYMBOLIC_DOMAIN_PRESERVATION_v0.1`. Authority: the user's execution
of the supplied K1-R1 work order. The entire preceding K1 report is preserved as
the submitted-candidate history. Its 122-test result did not cover the defect
below and is not a certificate of domain preservation. GPT has not accepted the
implementation; GPT review of the corrected bytes remains pending. No Claude
implementation review was performed.

### Reviewed candidate and observed failure

All four reviewed LF-byte identities matched exactly before source edits:

| Submitted artifact | SHA-256 |
|---|---|
| `reference_scaffold.py` | `042724d37db2343edf4f741f8a42b53a4781c9fc27baa29cc2582062d3c3dcf7` |
| `tests/test_reference_scaffold.py` | `9e185c92ae23a13d70ac823424e14422da7c2443f1d5f1349eb833cdada971d5` |
| Original Markdown report | `405c703aaa08d5553a4e2a9583cb90ff2613facc5d48d87c51d31b2af61c51f3` |
| Submitted README | `58c29ac72f0a2d55a96495344d4cf0ed56cafa67174928f2b91682d40db39d43` |

The local full JSON companion was read and hashed separately; GPT had not
received it, so no reviewed JSON identity is asserted. Its original top-level
keys/values and all earlier failure/pass outputs remain unchanged. New R1
evidence is under `R1`. In particular, the original `artifact_sha256` map and
`final_runs` describe the submitted K1 stage, not current R1 bytes. Current
identities and runs are explicitly labeled within `R1`.

The checkout remains on `main` at
`c60e4cfa9b3e5247f522a6036657c4d6fac75da1`, with the existing K1 changes and four
untracked predecessor test files preserved. The equal `origin/main` value is a
local tracking observation only; no fetch or other Git mutation occurred.
The documented Windows CMD interpreter again reported Python 3.12.14, NumPy
2.3.5 and SymPy 1.14.0. Package/geometry/dynamics/scaffold import paths were
asserted under the authoritative checkout before executing the witness.

For positive x, the admitted `s=1/(1+sqrt(x))` is provably positive, finite and
real. Running GPT's witness against the unmodified submitted source produced:

~~~text
symbolic vertex:
(sqrt(3)*sqrt(x)/(2*x - 2) - sqrt(3)/(2*x - 2),
 -sqrt(x)/(2*x - 2) + 1/(2*x - 2))
construct then substitute: (nan, nan)
substitute then construct: (sqrt(3)/4, -1/4)
own-vertex membership: ValueError coordinate must be provably real and finite
~~~

The JSON retains the actual captured witness output and exact source identity.
The denominator `x-1` was introduced by symbolic rationalization; it was not a
geometric degeneration or an excluded input. Simplifying a difference to zero
before substituting x=1 would hide this loss of pointwise domain.

### Narrow correction and pipeline audit

The only runtime change is the new module's `_point` policy:

~~~python
sp.expand(sp.radsimp(sp.simplify(v), symbolic=False))
~~~

An explanatory comment documents why symbolic denominators must not be
rationalized. Numerical radical denominators remain processed exactly. The
official [SymPy 1.14.0 radsimp documentation](https://docs.sympy.org/latest/modules/simplify/simplify.html#sympy.simplify.radsimp.radsimp)
warns of substitution-induced NaN under symbolic rationalization and specifies
this option. The online page identifies itself as 1.14.0; the separate versioned
URL was inaccessible during this check. The page's stated behavior supports the
policy choice, not a proof of arbitrary expression-domain preservation.

The remaining coordinate pipeline was inspected: input validation, ordinary
`simplify`, final `expand`, hull input normalization, support-plane construction
and the point-producing callers. Validators, positivity rules and uncertain
membership/regularity semantics were not changed. The same `_point` serves A/B,
support vertices, planar/vertical centres and point maps, and the Paper-C rigid
map; the higher-level frames/cells consume those outputs. `_r60` uses it only
on exact fixed normals. The correction is not copied into protected `geometry.py`
or the original test oracle/normalizer. No equation, placement, frame order,
role convention, shrink factor or accepted geometric claim changed.

Immediately after correction the primary witness gave finite exact
`(sqrt(3)/4,-1/4)` by both construction orders, and the generated symbolic first
vertex passed its own filled-hexagon membership check. No limit, tolerance,
floating evaluation, excluded x=1, NaN replacement or parameter-name special
case was introduced.

### R1 regression coverage and attribution

Twelve targeted methods are appended as `SymbolicDomainRegressionTests` in the
same test file. The original 27 methods and their substantive assertions remain
unchanged. The new helper first substitutes into each returned coordinate,
checks finite/real/exact output, and only then compares with a rebuilt exact
point. It does not use the original test file's `point()` normalizer. Primary
hexagon checks also compare with direct constants and the preserved independent
equation-(11) oracle, so expected values do not pass through the unsafe policy.

| New test suffix (`test_` omitted) | Domain evidence |
|---|---|
| `regular_composite_length_substitution_first` | GPT's positive composite side, x=1, direct first vertex and all six oracle coordinates |
| `nonregular_composite_side_substitution_first` | composite side with fixed gap=1 |
| `nonregular_composite_gap_substitution_first` | fixed side=1 with composite gap |
| `generated_symbolic_vertices_self_membership` | all six symbolic vertices in each of those three members |
| `complete_planar_frames_composite_length` | all complete planar hulls, centres and local filled octagon |
| `vertical_local_coordinate_substitution_first` | finite symbolic local coordinates in each indexed vertical map |
| `planar_local_coordinate_substitution_first` | finite symbolic local coordinates in each indexed planar map |
| `rigid_map_local_coordinate_substitution_first` | finite symbolic ambient coordinates, with independent exact constants |
| `support_vertices_corner_cells_and_boundaries` | support hull, corners, E/G edges, outline and all half-plane coefficients |
| `vertical_reference_frames_centres_and_top_edges` | complete finite vertical hulls, centres and selected top edges |
| `named_paper_c_constructions_composite_length` | original family, fixed-size translation, fixed-centre shrink and rigid comparison map |
| `second_exact_witness_no_parameter_special_case` | positive rho with side `1/(2+sqrt(rho))`, specializing at rho=4 |

This is a bounded substitution regression set, not a parameter sweep or a
universal certificate for arbitrary SymPy expressions. The existing invalid-input,
unknown-membership, exact geometry, symmetry, finite Paper-C and shrink tests
are retained. Genuinely undecidable relations still remain undecidable; this
known finite witness is not relabeled as such.

GPT's reported Linux grouped run of all 27 original tests and eight experimental
witness outcomes remain GPT-attributed review evidence as described in the
work order. They are not counted as new Codex Windows runs. The supporting
conversation JSON was not imported as code or added as a new repository path.
The full local suite and new focused results are separately captured under `R1`.

### R1 execution results and preservation

Both runs used the documented existing interpreter with `-B`, through Windows
CMD, from the authoritative checkout. Their equivalent standalone commands are:

~~~bat
C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe -B -m unittest kernel_physics.tests.test_reference_scaffold.SymbolicDomainRegressionTests -v
C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe -B -m unittest discover -s kernel_physics/tests -v
~~~

The inline standard-library unittest harnesses preserve discovered IDs, raw
captured output and actual timings directly in the full JSON companion. Their
source is retained there, with the Windows command-envelope qualification.

| R1 run | Actual result | Time |
|---|---|---|
| Targeted substitution regressions | 12/12 passed, no failures/errors/skips | 56.311 s |
| Complete currently present local suite | 134/134 passed, no failures/errors/skips | 117.748 s |

The final count is measured: 95 predecessor + 27 original K1 + 12 R1 methods.
The original local-only qualification remains: four pre-existing untracked
predecessor files contain 30 baseline tests; 65 baseline methods are tracked at
the base commit. No predecessor test was copied, weakened, removed or staged.
The full run reverified the exact authoritative module import paths and source
identity. All R1 geometry comparisons are exact; no floating tolerance is used.
Existing numerical regression tolerances are unchanged.

The runtime patch is verified as exactly the `_point` keyword change plus its
comment by reconstructing and hashing the original source text. All original K1
class methods, setup/assertion helpers and the test-file prefix preceding the new
class retain their prior hashes. The accepted geometric tests/oracle remain
substantively and textually unchanged.

All 33 bounded protected identities retain their before hashes. The original
Markdown bytes remain an exact prefix. Removing only the new `R1` key and
serializing the prior JSON with its original formatting reproduces the complete
pre-R1 JSON SHA-256: earlier fields, original failures, results and hashes have
not been silently rewritten. The original raw JSON identity is recorded under
`R1.preflight`, not represented as a GPT-reviewed artifact.

Current R1 hashes for source, tests, README and this appended Markdown are under
`R1.current_artifact_sha256`; the JSON excludes its own self-hash. The original
top-level hash map remains the submitted K1 identity. The only changed paths
are the same five K1 paths. Git index, HEAD, branch, local tracking ref and status
outside those paths remain unchanged. Fresh strict whitespace checks pass on all
five paths without staging, configuration changes or a publication exception.

The remaining limit is explicit: these witnesses and the full regression suite
support this correction; they are not a universal theorem about every possible
SymPy expression or simplification. No symbolic input class is newly excluded,
finite-input validation is not weakened, and genuinely unknown membership stays
unknown. GPT implementation review remains pending. No K2/K3, geometry adoption
beyond K1, Z/clock, six-gap registration, historical-code repair or new research
was performed.

~~~text
TASK = MK-K1-R1_SYMBOLIC_DOMAIN_PRESERVATION
PREPATCH_WITNESS = REPRODUCED_NAN_AND_OWN_VERTEX_REJECTION
CORRECTION_POLICY = expand(radsimp(simplify(v), symbolic=False)) in new _point only
VALID_SUBSTITUTION_REGRESSIONS = 12/12 PASS
GENERATED_GEOMETRY_SELF_MEMBERSHIP = PASS; all six vertices in three witness members
ORIGINAL_K1_TESTS_RETAINED = 27/27; original method bodies unchanged
FULL_LOCAL_SUITE = 134/134 PASS; zero failures/errors/skips
TRACKED_VS_LOCAL_TEST_QUALIFICATION = RETAINED; 30 predecessor tests local-only, 65 tracked
PROTECTED_FILES_PRESERVED = 33/33 bounded identities; prior report/JSON history preserved
K2_K3_STARTED = NO
STAGING_COMMIT_PUSH = NO
GPT_IMPLEMENTATION_REVIEW = PENDING
CLAUDE_IMPLEMENTATION_REVIEW = NOT_PERFORMED
~~~
