# NCM-Z-02 v0.1 — frozen versus scheduled retained-history Z

## Answer

The admitted window contains five retained native-triad states at actual indices 0–4, giving four consecutive spans. Frozen staged Z stays nearest **G+0 at all five endpoints**. Scheduled staged Z has **three resolved endpoint-label switches**. All three occur at the clock replacement in the required native → envelope → clock telescope. There are no primary nearest-label ties or precision disagreements. These are endpoint facts about a declared spatial readout, not continuous crossings or a material motion law.

## Admission before outcomes

The work order was read separately and checked against the ZIP copy. All 14 manifest-listed packet entries passed. The supplied NCM-Z-01 review archive has the prescribed SHA-256 and its 73 payload entries were checked without running its helpers. Its byte-bound definitions supplied the observation and geometry; the prior full study was not executed.

The read-only route began in the named Windows validation directory. Its fixture/export inventory and closeout identify only the old two-state record; the other export is an overwrite-protection sentinel. The first next evidence route, the central-geometry v0.3 source index, explicitly identifies its saved numerical audit archive. Its report describes a separate 120-decimal nominal calculation of the exact nominal starting state and four native images. NOMINAL_CROSSCHECK.json retains all six real state components at each of those indices.

The central manuscript/R6 rational comparison centers were rejected as substitutes. The selected data instead come from the independently retained nominal producer output. The archived verification.py, read as text, constructs the starting state from its radical/basis definition, fixes epsilon=.1, g=.2, lambda_phase=.17 and k=(2,3,4), iterates four times, and writes the five full states. Audit.py calls that function and serializes its returned object. The retained console log and report account for that earlier execution. No part of that producer was run or transcribed as an executable native evaluator in this task.

Source locators: [source/evidence index](sources/003_SOURCE_ACCESS.md), [prior audit report](sources/006_INDEPENDENT_NUMERICAL_AUDIT_REPORT.md), [producer text, lines 120–171](sources/arch_verification.py), [caller text, lines 551–552](sources/arch_audit.py), [prior execution account](sources/arch_ENVIRONMENT_AND_REPLAY.md), [prior console log](sources/arch_logs_audit-console.txt).

| Candidate | Bytes | Decision |
| --- | --- | --- |
| 1 | 10435 | EXCLUDED_TOO_SHORT: Two states at indices 0 and 1; no continuation in the inspected Windows record/fixture inventory |
| 2 | 55 | EXCLUDED_NOT_HISTORY: 55-byte overwrite-protection sentinel, not JSON or scientific samples |
| 3 | 8871 | ADMITTED_SELECTED: Five stored native triad states from the documented prior 120-digit nominal producer, at fixed parameters, with manifest-bound source and execution account |

Three distinct candidate artifacts totaling 19,361 bytes were inspected, below the 12-artifact, 32 MiB each, 128 MiB total limits. Known byte-identical old exports are one two-state observation, not independent histories. Interval result boxes were not converted to midpoints. The manifest route first yields this eligible nominal history; it was selected at rank 3 after the old-run continuation/initialization route did not supply a qualifying longer record. No equally ranked eligible competing history was admitted, so the tie-breakers did not select by outcomes. Later named route directories were filename-listed initially, but their state data were not read; the search stopped at admission. This is a bounded route result, not an assertion that no other history exists anywhere.

The historical nominal initial state was constructed for the earlier geometry investigation. It is not a random or representative draw. That inherited construction is disclosed; selection here used provenance and source-route order, not its new nearest-opening outcomes.

| Frozen item | Value |
| --- | --- |
| Selected member | NOMINAL_CROSSCHECK.json |
| Selected member size / SHA-256 | 8871 / a294a4b0bf181adaa2054aa52379c1832a7833e3faa7614d0785aecd709ea09c |
| Source archive SHA-256 | 959aff5caf6b617565e1b059035f5254046a39bdd93c875706008978a869e90b |
| Plan frozen UTC | 2026-11-01T02:31:20.882933+00:00 |
| ADMISSION_AND_PLAN.json SHA-256 | ceeafb7b333474d47b95005e2ee2f6c09e076c3425722d24b6c944c38b88bb23 |
| Included actual indices | 0, 1, 2, 3, 4; entire history; excluded suffix 0 |
| Native coefficient tokens | epsilon=.1; g=.2; lambda_phase=.17; k=(2,3,4) |
| Native-map calls / EMA updates | 0 / 0 |

NCM-Z-01 instead used epsilon=.05, g=.2, phase_strength=.001, k=(1,1,1), and a different starting state. Consequently this is a new retained example, not a same-lineage extension or same-configuration replication.

Original values are in [the immutable selected copy](inputs/SELECTED_HISTORY.json) and [the original-token ledger](ORIGINAL_TOKEN_LEDGER.json). The record has no internal Core content seal; its member size and SHA-256, plus the selected producer/caller/report/log members, match the historical OUTPUT_HASH_MANIFEST.json. The old regression parent also matches its prescribed bytes and inert deterministic digest. Integrity and a source account do not authenticate a producer or newly certify ideal native evolution. The nominal record explicitly labels itself NUMERICAL_CORROBORATION_ONLY. Its enclosure-agreement flags are inherited, not freshly proved here.

## Definitions, fixed geometry and numerical meaning

Native Omega is the saved complex triad. It is not altered, rephased, normalized, interpolated or stepped. The state-to-observation chain uses


\[
\kappa=\|\Omega\|,\quad C=\Re\Omega\times\Im\Omega,\quad
K=\lambda_{\rm vp}\frac{\kappa}{1+\kappa},\quad
E(t)=e^{-\gamma t},\quad
H_\theta=\cos(3(\theta-\ell))(\cos\theta,\sin\theta,1),
\]
\[
M=KEH_\theta,\quad Z=\alpha M+\beta C,\quad
X=O+\mu R_\psi Z.
\]

The unchanged observer preset is N=12, q0=0, q_step=1, time0=0, dt=0.1, lambda_vp=0.618, gamma=0.577, lock_angle=0.244 radians, alpha=1, beta=0.5, mu=1, psi=0. These observer coefficients differ in role from the native tuple. The literal 0.618 retains binary64 source semantics; no exact inverse golden ratio or controller was substituted.

For actual saved index n, q=(q0+n*q_step) mod N, theta=2*pi*q/N and t=time0+n*dt. Frozen F_n uses the first included index n*=0, hence theta*=t*=0. Scheduled S_n uses each actual n. Integer q is computed before angle evaluation. No sample ordinal substitutes for n; late and sparse schedules are tested separately. F_n and S_n are simultaneous readout alternatives of the same state, not successive native positions. The native recurrence has no feedback from these observations.

Geometry is fixed PLUS tau=0, width one, centered at O=(0,sqrt(3)/6,0). With r=sqrt(3)/6, d=1−sqrt(2)/2, a=d/2, h=(sqrt(2)−1)/2 and e_i=(cos(−pi/2+i*pi/3),sin(−pi/2+i*pi/3)), the upper broken arc is
G+k = U_k—T_(2k+1)—U_(k+1), where U_k=(r e_(2k),1/2), T_i=(a e_i,h). Lower arcs replace positive heights with their negatives at tau=0. All six compete. No filled aperture interior, aperture normal or flux is invented. No tau/branch/pose sensitivity scan was performed.

The separate finite host notch is
N_(k,sigma)(lambda,zeta)=(2r−sqrt(3)d*lambda/2)g_k+zeta*Jg_k+sigma(h+d*lambda)e_z,
0≤lambda≤1, abs(zeta)≤d*lambda/2, g_k=e_(2k+1). Its carrier plane alone is insufficient: both plane and finite barycentric domain are tested. The passive original enclosing sphere has radius sqrt(13/12−sqrt(2)/2)≈0.6133730937584284.

Definitions are from [observer.py](accepted_sources/observer.py), lines 184–204, 262–276 and 305–369; [central.tex](accepted_sources/central.tex), lines 181–224 and 331–373; [host.tex](accepted_sources/host.tex), lines 235–242 and 283–285. Complete source identities are in SOURCE_MANIFEST.json. Accepted snapshots are used, not an assumed current Git HEAD. No current-source repair or source substitution was made.

Primary computation explicitly converts the retained decimal strings to binary64 for the detached application-style overlay, retaining the original strings and conversion hex tokens. The historical producer used 120 decimal working digits but stored up to 100 significant digits; “120 digits” is not a claim of 120 retained digits. Independent 80-decimal calculations parse the original strings directly, lift the binary64 observer coefficient constants exactly, and use high-precision pi/radicals and independently written segment/patch formulas. These checks assess readout/classification stability without reconstructing any native state.

The historical record's saved Z used its own ideal-decimal formula. Its values are compared separately within 2e-13*max(1,magnitudes), not relabeled as bit-identical application readouts. High-precision state/output values are not certified state intervals. Geometry/tie tolerance is 1e-12 width units. All 18 primary/intermediate evaluations received high-precision comparison, covering the required switch endpoints, S/F disagreements, borderline tests and first/middle/last samples. No scheduled envelope underflow or nonfinite output occurred.

Largest binary64-versus-80-decimal discrepancy across computed state/readout coordinates and arc distances: **1.1102230246251565e-16**. Largest telescope residual component: **5.5511151231257827e-17**. No precision comparison changed a nearest-label decision. The 4e-12 robustness allowance is heuristic screening, not a proven error enclosure.

## Complete endpoint results

All measurements below use host width units and centered coordinates; world X adds O. All ten primary points are inside the original sphere. “Inside the sphere” does not assert membership in a material core.

| Point | X−O | radius | height | azimuth ° | elevation ° | nearest arc | distance | runner-up margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F0 | (0.042275495, -0.169448350, 0.304737854) | 0.351233712 | 0.304737854 | -75.991317209 | 60.183386316 | G+0 | 0.040278337 | 0.076377921 |
| S0 | (0.042275495, -0.169448350, 0.304737854) | 0.351233712 | 0.304737854 | -75.991317209 | 60.183386316 | G+0 | 0.040278337 | 0.076377921 |
| F1 | (0.148736653, -0.044969182, 0.192160843) | 0.247124683 | 0.192160843 | -16.822217138 | 51.040135192 | G+0 | 0.036974322 | 0.190068418 |
| S1 | (0.105768147, 0.023667565, 0.167583498) | 0.199577763 | 0.167583498 | 12.613198604 | 57.107423355 | G+0 | 0.105220814 | 0.056893427 |
| F2 | (0.149612692, -0.029004970, 0.172039452) | 0.229832154 | 0.172039452 | -10.971660081 | 48.464401179 | G+0 | 0.060604027 | 0.161423748 |
| S2 | (-0.065101227, -0.143623201, -0.108849333) | 0.191608901 | -0.108849333 | -114.383737769 | -34.616500540 | G-2 | 0.135722802 | 0.089378212 |
| F3 | (0.151094214, -0.025835667, 0.170454698) | 0.229241679 | 0.170454698 | -9.703190677 | 48.035471100 | G+0 | 0.064292802 | 0.156593182 |
| S3 | (0.000912176, -0.139329469, -0.093221142) | 0.167641625 | -0.093221142 | -89.624895764 | -33.784718349 | G-0 | 0.182193240 | 0.001265553 |
| F4 | (0.165895777, -0.004682977, 0.169250786) | 0.237042544 | 0.169250786 | -1.616940407 | 45.562137207 | G+0 | 0.084583106 | 0.128576263 |
| S4 | (-0.065513936, 0.109209874, 0.135109276) | 0.185670108 | 0.135109276 | 120.959131870 | 46.692634698 | G+1 | 0.104222316 | 0.099250624 |

All six finite-arc distances, not azimuth sectors:

| Point | G+0 | G+1 | G+2 | G-0 | G-1 | G-2 |
| --- | --- | --- | --- | --- | --- | --- |
| F0 | 0.040278337 | 0.316875788 | 0.116656258 | 0.527629662 | 0.602960839 | 0.547576177 |
| S0 | 0.040278337 | 0.316875788 | 0.116656258 | 0.527629662 | 0.602960839 | 0.547576177 |
| F1 | 0.036974322 | 0.227042740 | 0.270026486 | 0.400865297 | 0.467094458 | 0.485950587 |
| S1 | 0.105220814 | 0.162114241 | 0.255049393 | 0.387587538 | 0.408233267 | 0.451531736 |
| F2 | 0.060604027 | 0.222027775 | 0.279343626 | 0.382395526 | 0.443755654 | 0.471302180 |
| S2 | 0.376325202 | 0.433828227 | 0.329536673 | 0.225101013 | 0.313102524 | 0.135722802 |
| F3 | 0.064292802 | 0.220885984 | 0.281867625 | 0.381296711 | 0.441659727 | 0.471209267 |
| S3 | 0.332297005 | 0.414566835 | 0.332992570 | 0.182193240 | 0.307634097 | 0.183458794 |
| F4 | 0.084583106 | 0.213159369 | 0.301596847 | 0.384537650 | 0.438185553 | 0.481694008 |
| S4 | 0.274700460 | 0.104222316 | 0.203472939 | 0.432883970 | 0.350414726 | 0.392623131 |

A unique numerical winner requires its lead over the second-best arc to exceed 1e-12, with agreement of the independent high-precision winner set. Otherwise the result is a set/unresolved decision, never a label-order tie break. No primary tie occurred. Segment ties at a shared elbow are retained separately and do not create two different nearest arcs.

| Point | nearest segment(s), zero-based | distinct nearest spatial points | nearest point(s) |
| --- | --- | --- | --- |
| F0 | 0 | 1 | (0.075467884, -0.160470889, 0.325714387) |
| S0 | 0 | 1 | (0.075467884, -0.160470889, 0.325714387) |
| F1 | 1 | 1 | (0.130537848, -0.066667938, 0.215932001) |
| S1 | 1 | 1 | (0.132565852, -0.063085884, 0.220754373) |
| F2 | 1 | 1 | (0.128617181, -0.070060403, 0.211364865) |
| S2 | 0,1 | 1 | (-0.126826484, -0.073223305, -0.207106781); (-0.126826484, -0.073223305, -0.207106781) |
| F3 | 1 | 1 | (0.128955939, -0.069462057, 0.212170394) |
| S3 | 0,1 | 1 | (0.126826484, -0.073223305, -0.207106781); (0.126826484, -0.073223305, -0.207106781) |
| F4 | 1 | 1 | (0.133999919, -0.060552897, 0.224164428) |
| S4 | 0,1 | 1 | (0.000000000, 0.146446609, 0.207106781); (0.000000000, 0.146446609, 0.207106781) |

Primary point-on-central-boundary flags: none. Primary finite-notch point memberships: none. Primary outward-ray finite-notch hits: [('F1', 'N+0')]. Full plane residuals, finite-domain coordinates, carrier-ray parameters, hit reasons and every one of the 60 primary point/patch comparisons are retained in GAP_COMPARISON.json. A ray is a geometric direction test, not an observed path.

| Point / patch | ray parameter t | centered ray-hit point | finite lambda | finite zeta | point itself a patch member |
| --- | --- | --- | --- | --- | --- |
| F1 / N+0 | 2.381759636 | (0.354254956, -0.107105783, 0.457680939) | 0.855513688 | 0.084371149 | False |

This single forward-ray hit does not establish emission. The finite notch triangle is a separate measurement region, not a filled central opening or material cap. A ray hit and a closest-central-boundary label answer different geometric questions.

## Every stored interval and same-index comparison

| Actual interval | span | Frozen labels | Scheduled labels | category |
| --- | --- | --- | --- | --- |
| 0→1 | 1 | G+0 → G+0 | G+0 → G+0 | neither |
| 1→2 | 1 | G+0 → G+0 | G+0 → G-2 | scheduled_only |
| 2→3 | 1 | G+0 → G+0 | G-2 → G-0 | scheduled_only |
| 3→4 | 1 | G+0 → G+0 | G-0 → G+1 | scheduled_only |

Totals: frozen-only 0; scheduled-only 3; both same ordered labels 0; both different labels 0; neither 1; unresolved/tied 0. Same-index S/F disagreements occur at 2, 3 and 4. No unresolved transition was silently counted as “neither.” The complete ledger also records changes in per-arc segment ties.

| Interval | Convention | center-radius change | nearest-boundary distance change |
| --- | --- | --- | --- |
| 0→1 | frozen | -0.104109029 | -0.003304016 |
| 0→1 | scheduled | -0.151655949 | 0.064942477 |
| 1→2 | frozen | -0.017292529 | 0.023629706 |
| 1→2 | scheduled | -0.007968863 | 0.030501987 |
| 2→3 | frozen | -0.000590475 | 0.003688775 |
| 2→3 | scheduled | -0.023967276 | 0.046470439 |
| 3→4 | frozen | 0.007800865 | 0.020290304 |
| 3→4 | scheduled | 0.018028483 | -0.077970925 |

Distances to both the old and new winners for every scheduled switch:

| Interval | Boundary | distance before | distance after | change |
| --- | --- | --- | --- | --- |
| 1→2 | G+0 | 0.105220814 | 0.376325202 | 0.271104388 |
| 1→2 | G-2 | 0.451531736 | 0.135722802 | -0.315808934 |
| 2→3 | G-0 | 0.225101013 | 0.182193240 | -0.042907773 |
| 2→3 | G-2 | 0.135722802 | 0.183458794 | 0.047735992 |
| 3→4 | G+1 | 0.414566835 | 0.104222316 | -0.310344519 |
| 3→4 | G-0 | 0.182193240 | 0.432883970 | 0.250690730 |

For example, F1→F2 moves inward (radius 0.247125→0.229832) while moving farther from G+0 (distance 0.036974→0.060604). The scheduled S2→S3 switch is separated by only 0.001265553 width units at S3, still far above the tie tolerance. Neither a switch nor a small gap lead means attraction, activation, aperture crossing or energy flow.

## Displacements and chord turns

Delta F and Delta S connect adjacent stored indices algebraically; no continuous path is supplied. For successive non-negligible displacement vectors u,v, the unsigned chord angle is atan2(norm(u cross v),u·v). A zero or norm≤1e-12 displacement has an undefined angle; actual nonzero components are retained, not zeroed. Spans remain visible. These are not calibrated speeds, accelerations or continuous curvature.

| Interval | Delta F | norm | Delta S | norm |
| --- | --- | --- | --- | --- |
| 0→1 | (0.106461158, 0.124479167, -0.112577011) | 0.198752672 | (0.063492653, 0.193115915, -0.137154356) | 0.245227223 |
| 1→2 | (0.000876039, 0.015964212, -0.020121391) | 0.025700075 | (-0.170869374, -0.167290766, -0.276432831) | 0.365510128 |
| 2→3 | (0.001481522, 0.003169303, -0.001584754) | 0.003840682 | (0.066013403, 0.004293732, 0.015628191) | 0.067973861 |
| 3→4 | (0.014801563, 0.021152690, -0.001203912) | 0.025845154 | (-0.066426112, 0.248539343, 0.228330418) | 0.343975309 |

| Middle actual index | incoming/outgoing spans | Frozen chord angle ° | Scheduled chord angle ° |
| --- | --- | --- | --- |
| 1 | 1/1 | 31.704824126 | 93.352411440 |
| 2 | 1/1 | 31.919418190 | 131.055760071 |
| 3 | 1/1 | 23.722089304 | 89.386044451 |


## Ordered attribution and the two freezes

For adjacent saved endpoints i,j, set K_i=K(kappa_i), E_i=E(t_i), H_i=H(theta_i). Here placement is the identity scale/rotation:

\[
D_{\rm nat}=\alpha E_i(K_j-K_i)H_i+\beta(C_j-C_i),\quad
D_{\rm env}=\alpha K_j(E_j-E_i)H_i,\quad
D_{\rm clock}=\alpha K_j E_j(H_j-H_i).
\]

Insert X(Omega_j,theta_i,t_i), then X(Omega_j,theta_i,t_j). Subtracting these four evaluations telescopes exactly to S_j−S_i over the reals. The implementation computes total−[native+(envelope+clock)] and retains its finite-arithmetic residual. The norm/chiral split is inside the native term; chirality is not a separate fourth contribution.

The interval-native term uses the **previous scheduled setting**, while Delta F uses the **global first-sample setting**:

\[
\Delta F=\alpha E_\star(K_j-K_i)H_\star+\beta(C_j-C_i).
\]

They coincide in the first interval here; generally they differ afterward. Neither is an order-independent physical force. Norms are not additive contribution percentages.

| Interval | Native | Envelope | Clock | local native − Delta F |
| --- | --- | --- | --- | --- |
| 0→1 | (0.106461158, 0.124479167, -0.112577011) | (-0.009074477, -0.000000000, -0.009074477) | (-0.033894028, 0.068636747, -0.015502867) | (0.000000000, -0.000000000, -0.000000000) |
| 1→2 | (0.004410080, 0.010319028, -0.018099972) | (-0.006117158, -0.003531743, -0.007063485) | (-0.169162297, -0.174078051, -0.251269374) | (0.003534042, -0.005645184, 0.002021419) |
| 2→3 | (-0.000893421, 0.001901515, -0.004691655) | (0.003751259, 0.006497372, 0.007502518) | (0.063155565, -0.004105155, 0.012817328) | (-0.002374943, -0.001267788, -0.003106901) |
| 3→4 | (-0.000670044, 0.009460669, -0.028367541) | (0.000000000, 0.007018783, 0.007018783) | (-0.065756068, 0.232059891, 0.249679176) | (-0.015471608, -0.011692021, -0.027163629) |

The full four-point sequence for every interval, including actual settings and world coordinates, is stored through ATTRIBUTION.json evaluation IDs into GAP_COMPARISON.json. Its nearest labels are:

| Interval | initial scheduled | native replacement | envelope replacement | final scheduled |
| --- | --- | --- | --- | --- |
| 0→1 | G+0 | G+0 | G+0 | G+0 |
| 1→2 | G+0 | G+0 | G+0 | G-2 |
| 2→3 | G-2 | G-2 | G-2 | G-0 |
| 3→4 | G-0 | G-0 | G-0 | G+1 |

Thus the three scheduled switches arise at the clock replacement in this declared order. The envelope alone does not change a nearest label in any of these intervals, although it changes the observation. These replacements are counterfactual evaluations of stored states, not extra native stages, event times or traced paths.

## Independently verified margin bound

Let G_a be any nonempty fixed boundary set and d_a(x)=inf_{p in G_a} norm(x−p). The triangle inequality gives d_a(y)≤d_a(x)+norm(y−x): take the infimum over p. Interchanging x,y yields abs(d_a(y)−d_a(x))≤norm(y−x). The finite segment unions here are nonempty compact sets, so their minima also exist.

If a is uniquely nearest at x and m=min_{b≠a}(d_b(x)−d_a(x)), then for every b≠a:

d_b(y)−d_a(y) ≥ d_b(x)−norm(y−x)−[d_a(x)+norm(y−x)] ≥ m−2 norm(y−x).

Consequently m>2 norm(y−x) implies a remains uniquely nearest. Applying x=F_n,y=S_n establishes the brief's exact sufficient condition. The failure of that condition proves nothing about label change. As a check, singleton sets at 0 and 10 on one axis give: x=1,y=1.1 satisfies the bound and retains the winner; x=1,y=9 fails and switches; x=1,y=−9 fails but retains the winner.

With rigorously proven distance error e_d and displacement-norm error e_b, m_hat−2e_d−2(b_hat+e_b)>0 would certify the same conclusion. Here 1e-12 tolerances are not proven enclosures. The frozen plan's screening condition is m_hat−2b_hat−4e-12>0, with independent high-precision checks; it is reported only as a numerical sufficient-margin diagnostic.

| Index | frozen lead m | observer separation b | m−2b | adjusted slack | numerical diagnostic | actual labels agree |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.076377921 | 0.000000000 | 0.076377921 | 0.076377921 | sufficient | True |
| 1 | 0.190068418 | 0.084624709 | 0.020818999 | 0.020818999 | sufficient | True |
| 2 | 0.161423748 | 0.371669093 | -0.581914439 | -0.581914439 | inconclusive | False |
| 3 | 0.156593182 | 0.323975981 | -0.491358780 | -0.491358780 | inconclusive | False |
| 4 | 0.128576263 | 0.260168560 | -0.391760857 | -0.391760857 | inconclusive | False |

The bound succeeds at indices 0 and 1. It fails at 2–4, where direct distance comparisons happen to show disagreements. That coincidence does not turn failure of the bound into a predictor. This elementary distance-to-set argument is an interpretation aid, not a new observation or motion law.

## Figures and QA

![Top comparison](figures/01_top.png)

![Opposite side comparisons](figures/02_opposite_sides.png)

![All-six distances and radius/height](figures/03_index_diagnostics.png)

There are three sheets, all with original width-one geometry and the close sphere. Both conventions use the same spatial limits; all five markers are plotted without connectors or thinning. Both camera directions and all upper/lower near/far arcs are retained. Some frozen markers overlap in projection; this is real proximity, not omitted data. The full numerical ledger disambiguates them. Index-chart lines only guide the eye between stored rows. PNGs were inspected as files, not through the Windows application. A visual-only label/title adjustment changed no calculations.

The standalone script passed **246 assertions**. All 18 evaluations were checked at 80 decimals, including every switch endpoint, same-index disagreement and the first/middle/last states. The regression fixture, synthetic geometric cases and common-phase display-copy tests are excluded from primary history counts. A separate portable copy passed the same 246 checks and reproduced all five numerical JSON ledgers byte-for-byte on this host. Cross-platform last-place differences are possible; changed classifications must be reviewed, not waived. Ten monitored original sources/inputs remained unchanged; this is a bounded preservation check, not a whole-checkout audit.


## Reproduce the detached analysis

From Command Prompt, using the existing environment, after extracting the review package:

~~~bat
call conda activate torment
python -X utf8 -I -B C:\TORMENT\TRIOCTAGON_new\research\NATURAL_CORE_MOTION_Z_RETAINED_HISTORY_01\analyze.py --portable
python -X utf8 -I -B C:\TORMENT\TRIOCTAGON_new\research\NATURAL_CORE_MOTION_Z_RETAINED_HISTORY_01\make_figures.py
~~~

Substitute the extraction path if moved. Portable mode checks packaged source/input bytes; it does not assert preservation of inaccessible original Windows paths. It regenerates derived files, so verify the delivered manifest before rerunning. Existing Python/math libraries are required; this task performs no installation. Never run the archived producer scripts as part of this detached review.

## Limits and closeout

The result is “no frozen nearest-label switch in this five-state window, three scheduled switches.” It is not a proof of absent native motion, global nonexistence of frozen switches, long-time behavior, a period or upper-side preference. The selected input has its own constructed nominal initialization and different native coefficients from NCM-Z-01. Its saved numerical producer lineage is admitted at the stated evidence level, not upgraded to authentication or replay certification.

No missing-data result was necessary because a qualifying pre-existing history was found. No longer record, second history, alternative window, phase sweep, extra anchor, geometry scan, fitted rotation, native evaluator, EMA trace, application/kernel edit, Git operation or publication followed. No material core trajectory, aperture passage, emitted energy or new mechanism is established. The work stops with this review package.
