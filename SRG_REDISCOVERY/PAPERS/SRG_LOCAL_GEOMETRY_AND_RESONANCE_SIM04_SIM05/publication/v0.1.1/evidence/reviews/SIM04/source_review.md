# SIM04 independent source and mathematics review

**Reviewer role:** independent source review for GPT synthesis.  
**Input:** `review_sim04/input`; unchanged `originals/srg_seed_explorer.py` and the four study documents.  
**Method:** source and document reading only. No original import, simulation, random draws or state propagation.

## Verdict

**Acceptable within the construction-and-historical-evidence scope. No scientific blocker found.** The full program was read, including observers and all experiment drivers. Its central recurrence is faithfully transcribed in E1–E8, and the report handles the distinction between the selected saved driver and other experiments correctly. Small source-line locator errors merit editorial correction before later publication; they do not affect equations or findings.

The data calculations are reviewed by a separate reviewer. This verdict does not independently certify the original March archive or Windows preservation claims, whose source files are outside this supplied package.

## Scientific findings and qualifications

- Adjacency and distances are built from incoming positions (source 91–98, 144–145). The local position stage is synchronous (100–109, 147–149), and resonance coupling uses incoming resonance plus retained incoming distances and adjacency (111–124, 151–152), despite executing after the position update. The documentation preserves these important distinctions.
- The scheduled H factor multiplies resonance (154–158). It is not a history-dependent signal. The global fusion target uses post-diffusion positions and post-H resonance (160–163), before the sine factor and signed RPCO (165–169).
- The source's velocity is a saved position difference (174–178), never read in the next movement update. Its `kinetic_energy` is mean squared displacement (631–632), with no physical time or mass calibration. The documentation is accurate.
- The resonance exchange is a directed row-normalized convex average at beta=.15. It does not generally preserve the arithmetic mean or total resonance. Narrowing of the saved distribution is a finite observation, not a universal variance theorem.
- Local weak disconnection does not disconnect the whole model: every point continues to enter the common fusion center. Directed strong components and weak isolated components must remain distinct. The final graph is correctly treated as a saved-state diagnostic, not evidence of an executed pass 21.
- Echo detection, seed rankings and geometric classifications are observers. `higher_polyhedra` is unconditional for more than seven selected points (257–265), and the top-quartile selection retains thirteen points here. None of those labels establishes a new force, stationary leader or polyhedral structure.
- Conditional resonance agreement can strongly support update attribution without recovering the stochastic position stream. The source-defined noise location is known; identifying its realized draws or exact original execution remains a separate evidentiary question. The package makes this qualification correctly.

## Three particularly useful deductions

### 1. The recorded resonance dynamics reduce to affine averaging

**DERIVED, conditional on the positive, unclipped recorded regime.** Let W_p be the incoming inverse-distance neighbor matrix, whose rows sum to one. Set P_p=.85 I+.15 W_p, a_p=m_p s_p, and epsilon=1e-9. Source 111–124, 154–169 gives, in real arithmetic,

`R_p = a_p P_p R_(p-1) + epsilon * 1`.

Floating-point evaluation of log/exp introduces the small arithmetic differences already measured in the package. The observed a_p values are positive; all inspected RPCO inputs are positive and unclipped.

Define A_0=1, b_0=0 and A_p=a_p A_(p-1), b_p=a_p b_(p-1)+epsilon. Then z_p=(R_p-b_p*1)/A_p satisfies z_p=P_p z_(p-1). Therefore each z value is a convex mixture of earlier z values: the normalized minimum cannot decrease, the normalized maximum cannot increase, and their range cannot expand. This is a structural explanation for smoothing that does not require an instantaneous connected graph.

This does **not** prove monotone raw variance, exact mean conservation, asymptotic consensus, or equivalence to a run with H removed. Geometry and fusion respond to resonance, so the common schedule can affect future neighbor matrices indirectly. A disconnected graph can average within its groups; earlier connections can already have shared values before disconnection.

The common positive multiplier and common epsilon offset preserve the ranking within a given update. Thus the immediate top-ID changes in the recorded regime occur at the local exchange stage; the clock/sine factors do not directly select a new highest point. This explains why a stable highest rank is compatible with continued motion and decreasing resonance spread.

### 2. Six is the smallest possible isolated group for this five-neighbor rule

**DERIVED plus the package's final membership observation.** In this saved record there are no coincident positions, the self-distance is uniquely zero, and each point chooses five distinct other points (91–98). Every weak component must therefore contain at least six points. If a weak component has exactly six members, each member must choose all five other members: it is a complete directed six-point graph.

Consequently, the observed six-member final component is a particularly clear minimal local neighborhood under k=5. Its size is constrained by the neighbor rule. It is not by itself evidence of a preferred hexagonal, octahedral or universal sixfold geometry. Its coordinate shape remains a separate geometric question.

### 3. The global fusion term almost preserves the arithmetic centroid

**DERIVED in the positive-resonance regime.** Let U_i be the post-H resonance, Y_i the post-local positions, delta=1e-8, and

`c = sum((U_i+delta)*Y_i) / sum(U_i+delta)`.

Source 161–163 applies `F_i=.03 U_i(c-Y_i)`. Writing Ybar for the arithmetic mean gives the exact real-arithmetic identity

`mean(F) = .03 * delta * (Ybar-c)`.

If the tiny center-weight offset were zero, the net arithmetic-centroid shift from this stage would be exactly zero. With the source offset, it is suppressed by 3e-10 times the separation of the two centers. This is not a new physical conservation law and does not hold in the same form for mixed-sign U because the center uses abs(U).

The identity helps distinguish contraction from whole-field translation. Individual groups can move toward the common center while the fusion stage produces almost no arithmetic-center drift. The local directed update and unsaved noise can still move the centroid. No counterfactual trajectory or numerical ablation is needed for this algebraic statement.

## Nonblocking editorial corrections to exact locators

The unchanged numbered source gives:

| In `CONSTRUCTION.md` | Correct exact source locator |
| --- | --- |
| Initialization of V cited as S:L67 | S:L66 |
| Initial history allocation cited as S:L68 | S:L67 |
| Initial pass_count cited as S:L69 | S:L68 |
| N initialization cited as S:L64 in the configuration row | S:L63 |
| Constructor's initial recording | Call at S:L81; record method at S:L83–89 |
| `lambda_vp` and `gamma_srg` cited as S:L74–75 | S:L73–74 |
| `echo_threshold` initialization cited as S:L80 | S:L79 |

`ORIGINAL_EVIDENCE.md` should cite S:L81–89, rather than S:L82–89, when including the constructor's initial recording call. Broad ranges elsewhere that contain the intended operation are adequate. These are navigation fixes, not mathematical corrections and do not justify rerunning numerical analysis.

## Recommended review disposition

Accept the scientific construction and its appropriately qualified interpretation, subject to the independent data/package checks. Preserve the original files. Record the locator corrections as minor editorial polish for a later corrected review edition or publication; do not silently alter the sealed input ZIP. The three deductions above can be discussed as source-derived observations now without opening another simulation assignment.
