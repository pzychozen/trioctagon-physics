# Paper C — Proof Audit v0.2.2

Companion to `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.2.2.md`. Keeps the three verification registers **cleanly separated** — the biggest quality problem in Draft 0 was collapsing them into one "check count." This v0.2.2 is the **F07 closeout** over v0.2.1: a single wording correction removes "outward-normal dot $=-\tfrac12$" from the list of *executed* regression checks (the suite contains no outward-normal predicate) and keeps that result classified as **analytic under Theorem 4**. v0.2.1 had already narrowed the suite's scope so that finite predicates no longer imply proofs of the closure family, the all-$z$ section/maximal band, the interior dihedral, the boundary sign separation, the chamfer-edge theorem, or the $D_{3h}$ upper bound — each owned by Register A. No source, kernel, or builder was imported or modified; the predicate logic and count are unchanged (still 51/51, 19/19). The v0.2 and v0.2.1 files are preserved.

The three registers are never merged:

```
REGISTER A — ANALYTIC PROOF                 (Theorems 1, 1b, 2-6 in the manuscript)
REGISTER B — EXECUTED SYMBOLIC/COMBINATORIAL REGRESSION  (paperC_geometry_audit_v0_2_1.py)
REGISTER C — PRESERVED HISTORICAL / EXPORT VALIDATION    (read-only width-1 package)
```

## Register A — analytic proofs (not finite tests)

| Result | Where | Status |
|---|---|---|
| $s=\sqrt2-1$; apothem $=\tfrac12$; circumradius radical chain | §2 | ANALYTIC |
| octagon area chain $4as=2(1+\sqrt2)s^2=8(\sqrt2-1)a^2=2(\sqrt2-1)w^2$ (F01) | §2/§Symbols | ANALYTIC |
| octagon regular (edges $s$, angles $135^\circ$), all panels | §2,§4 | ANALYTIC |
| general-$\beta$ maps, free edges, **closure domain $[0,\pi]\Rightarrow\beta=\tfrac\pi3$** and full family $2k\pi\pm\tfrac\pi3$ (F02) | §5 Thm 2 | ANALYTIC |
| hinge fixed for all $\beta$; isometry | §5 | ANALYTIC |
| $V=18,E=21,F=3,\chi=0$; two 9-edge rims | §5 Thm 1 | ANALYTIC |
| **manifold-with-boundary via vertex links; connected; orientable; $b=2$; $g=0$; annulus = sphere minus 2 discs** (F03) | §5 Thm 1b | ANALYTIC |
| section curve $\partial T$ vs enclosed filled $T$; triangle metrics (F04) | §6 Thm 3 | ANALYTIC |
| central-band height $s$; $45^\circ$ chamfer-edge inclination, vertical panel planes (F09) | §6 | ANALYTIC |
| interior dihedral $60^\circ$; outward-normal separation $120^\circ$ | §7 Thm 4 | ANALYTIC |
| exact notch vectors; tip $\arccos\tfrac34$; **derived base cosine $\tfrac{\sqrt2}{4}$**; projection equilateral; areas; plane $\arctan(2/\sqrt3)$ (F05) | §8 Thm 5 | ANALYTIC |
| rim/hexagon partition $A_{\mathrm{hex}}+3A_{\mathrm{notch,proj}}=\tfrac{\sqrt3}{4}$; virtual regions (F04/F11) | §8 | ANALYTIC |
| **$D_{3h}$ with matching upper bound** (crease segments; face preservation; finite-set covariance) (F06) | §9 Thm 6 | ANALYTIC |
| degree values ($41.4096^\circ$, $69.2952^\circ$, $49.1066^\circ$) | §8, App. A | NUMERICAL |

The general-angle closure **solution set** and the full-group $D_{3h}$ **upper bound** are analytic arguments; finite predicates support but do not replace them.

## Register B — executed regression (`paperC_geometry_audit_v0_2_1.py`)

Pure sympy; no source/kernel/builder import. Reconstructs the shell from the octagon and the **general-angle** fold transforms; welds by exact coincidence; then executes finite predicates. **51/51 executed regression predicates PASS**, spanning **all 19 numbered coverage groups**. Reported as an *execution count of finite symbolic/combinatorial predicates*, **not** independent theorems — these checks **supplement** the analytic proofs of Register A, they do not replace them.

Discipline enforced (F07): **no literal `True`; no expected-minus-itself predicate.** Nested-radical equalities use sympy's exact symbolic prover (`.equals`) as a fallback to `simplify`. The three v0.1 tautologies (`triangle_altitude` = expr−expr, `triangle_area` from expected base×height, `notch_other_angles` = literal `True`) are replaced by coordinate-derived computations; the ten weak v0.1 predicates are strengthened. In v0.2.1 two predicate names were narrowed so no name overstates its predicate (`closure_general_solution_family` → `closure_representative_angle_samples`; `full_width_band_height_s` → `width_formula_values_at_h_and_a`); the predicate logic is unchanged.

**What the suite actually executes** (faithful scope), group by group: (1) apothem support-distance + circumradius chain; (2) shoelace area + identity chain + bad-formula refutation; (3) symbolic free-edge gap and $y,z$ agreement, exact restricted solve on $[0,\pi]$, and finite checks at **two closing-angle representatives and one non-closing angle** (not a derivation of the infinite family); (4) hinge fixed for all $\beta$ + isometry; (5) connectivity; (6) interval vertex links + edge incidence; (7) coherent orientation via each directed edge once + each seam traversed oppositely; (8) Euler characteristic, two degree-two boundary components, and genus arithmetic $g=0$ — **used alongside** the analytic surface proof, not a stand-alone classification; (9) projected endpoint comparisons for $P_1,P_2$, centroid exclusion, and **width-formula values at $z=h$ and $z=a$** (not a quantified all-height/maximal-band proof); (10) triangle altitude by point-to-line distance; (11) triangle area by shoelace; (12) inradius + circumradius from coordinates; (13) co-directional-strip $120^\circ$ rotation; (14) notch tip + **derived base cosine $\tfrac{\sqrt2}{4}$**; (15) three projected notch sides $=d$; (16) notch-plane inclination + areas; (17) hexagon sides/angle-cosines/area/partition; (18) $C_3^3=\mathrm{id}$ pointwise + $C_3\ne\mathrm{id}$; (19) generator face/edge permutation + reflection squares + $D_3$ conjugation + $\sigma_h$ commutation. Plus the regression against the authoritative welded coordinate table.

**Explicit scope split (do not conflate):**

```
ANALYTIC RESULT (owned by §§5-9, not by finite tests):
  full closure solution family        (Theorem 2)
  full central-band section theorem / maximal full-width band   (§6)
  outward-normal separation = 120 (dot = -1/2) and interior-dihedral relation
                                       (Theorem 4 / §7; NO regression predicate exists for it)
  boundary sign separation (two rims separated by z=0)  (§5)
  chamfer-edge inclination theorem     (§6; NO regression predicate exists for it)
  full D3h upper bound                 (§9)

REGRESSION SUPPORT (the finite predicates actually executed):
  the 51 predicates listed above, e.g. degree-two boundary components (not a z-sign test),
  representative closing-angle samples, and width values at h and a.
```

The v0.1 "46/46 independent checks" claim is **withdrawn**: the referee inventory found $33$ genuine, $3$ tautological, $10$ weak predicates and $19$ untested coverage groups. A script printing PASS records is not evidence that every theorem has an independent check.

## Register C — preserved historical / export validation (read-only)

The width-1 package records **26 construction entries and 46 export-validation predicates** (72 records). Inspected, not assumed, and **not** characterized as 72 independent confirmations (F08):

- **Construction: 24 conditional predicates + 2 informational PASS records.** The two informational records print a value without a comparison — the dihedral-cosine record and the closure-gap-expression record — each tested by a neighbouring record. Most predicates are exact; outward-winding and half-space containment use floating-point sign/tolerance ($10^{-12}$).
- **Export: 46 predicates, reading OBJ/CSV/JSON without importing the builder** — a useful implementation separation, but overlapping in purpose. They combine direct numerical geometry checks (counts, angles, areas, planarity, seams, boundary), exact scaling/serialization consistency against the archived $s=1$ export, metadata/status validation (one predicate merely asserts the 26 builder statuses are PASS; the stage-table predicate checks only row count; render predicates check file existence), and archive-hash preservation. Numerical tolerance $10^{-13}$.

These records support the geometry and preserve provenance; they are **not** 72 mathematically independent geometric theorems. The historical files are unchanged.

## Claim-discipline audit (unchanged, correct)

No physical, quantum, particle, propulsion, spacetime, or memory-system/TORMENT claim; no historical-design claim. Width $1$ is a nonphysical normalization. The shell is **not** a torus (it has boundary; it is an annulus, a sphere minus two discs), and **not** labelled $D_{24}/\mathbb Z_{24}$ (group $D_{3h}$); older concentric constructions are separated, not adopted (§10). Panels are zero-thickness; no collision-free physical folding; no enclosed volume. The v0.1 "torus with two open discs removed" parenthetical (a genuine topology misstatement despite the intended "not a torus" conclusion) is corrected in v0.2 (F03).

## Verdict

```
VERIFICATION_REGISTERS_SEPARATED = YES  (analytic proof / executed regression / preserved historical)
ANALYTIC_PROOFS = Theorems 1,1b,2-6
EXECUTED_REGRESSION = 51/51 PASS, 19/19 coverage groups, no literal-True, no expected-minus-itself
REGRESSION_CLAIM_EXCEEDS_EXECUTION = NO
ANALYTIC_AND_REGRESSION_SCOPE_SEPARATED = YES
OUTWARD_NORMAL_RESULT_CLASSIFICATION = ANALYTIC_ONLY (Theorem 4; no regression predicate)
ANALYTIC-OWNED (not finite-proved) = closure family, all-z section / maximal band,
                outward-normal separation / interior dihedral, boundary sign separation,
                chamfer-edge, D3h upper bound
PRESERVED_PACKAGE = 24 conditional + 2 informational construction records + 46 overlapping export predicates
INDEPENDENT_AUDIT_COUNT_HONEST = YES
OLD_72_RECORD_PACKAGE_CHARACTERIZED_HONESTLY = YES
GENERAL_CLOSURE_DOMAIN_EXPLICIT = YES
MANIFOLD_WITH_BOUNDARY_PROVED = YES
ANNULUS_CLASSIFICATION_PROVED = YES
SECTION_CURVE_REGION_DISTINGUISHED = YES
NOTCH_VECTOR_CORRECTED = YES
D3H_UPPER_BOUND_PROVED = YES
MATCHES_AUTHORITATIVE_SPEC_TABLE = YES
COORDINATES_CHANGED = NO
CORE_GEOMETRY_CHANGED = NO
SOURCE_MODIFIED = NO
KERNEL_MODIFIED = NO
READY_FOR_FINAL_CODEX_GEOMETRY_SPOTCHECK = YES
```
