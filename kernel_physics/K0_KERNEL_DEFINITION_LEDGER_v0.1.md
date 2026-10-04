# K0 kernel definition ledger v0.1

Date: 2026-09-26. Authority snapshot:
`2b70485c1fd0044baf90e0df361182165c1b9315`.
Companion: [public contract freeze](K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md).
Status: FROZEN for the scope and explicit open dispositions below. This is an
ownership ledger, not a second mathematical implementation or new theorem set.

## Reading and counting rules

Each ID denotes one definition/operation family; all symbols listed in that row
share its **one** engineering classification. Counts are row/definition-family
counts, not counts of functions, equations, tests or theorems. IDs are stable
within ledger 0.1 and may never be rebound to a different definition. Splitting
a family in a later ledger requires new IDs and an explicit crosswalk.

`CORE` means required accepted mathematics/essential software support; it does
not mean geometry runs inside dynamics. `OPTIONAL` means explicitly selected
accepted facility, not automatically part of the initial facade. `RESEARCH_ONLY`
can contain accepted theorems used as parity oracles. `HISTORICAL` names literals
and conventions; their existence is not a law. `OPEN` records unresolved
support/provenance, never supplies a guessed equation.

Exposure: **yes** = supported directly or in the named record; **explicit
optional** = only on request (the companion fixes the actual K1 subset);
**no** = no supported v1 runtime export. Ownership: **immutable** definition/
configuration, **evolving** canonical dynamics snapshot, **observer** clock/
memory/configuration, **derived** read-only result. Immutable configurations
inside observer families are distinguished in their descriptions. `NONE` in
the ambiguity column means no unresolved semantic/authority issue for the
specified definition, not a universal claim of numerical exactness.

All module paths below are exact repository-relative paths. Test aliases in
the evidence column expand to the exact paths in the next table; source IDs
expand to the edition and locator in the source registry. No local-only file is
represented as a tracked fresh-clone dependency. Hazards H01–H18 and open items
O01–O03 refer to the companion's registers. Software-only rows name planned
modules as **not implemented**, rather than inventing a current runtime owner.

The frozen row census is **CORE 24; OPTIONAL 27; RESEARCH_ONLY 13;
HISTORICAL 8; OPEN 3; total 75**. Historical definition IDs use L01–L06
to distinguish them from the companion's H01–H18 hazard IDs.

## Source and evidence registry

| ID | Controlling source / edition / interpretation |
|---|---|
| PA | `papers/PAPER_A/publication/paper_A_publication.md`, publication v1.0; mathematical source `papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md`; §§1–3,6 own the accepted map/covering |
| PB | `papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md`; §§2–9 and Appendix A; physical limits §11 |
| PC | `papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md`; preserved science v0.3.1, §§2–7,9, Appendix B; no new mathematics in publication scope/citation revision |
| PD | `papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md`, equations (1)–(29); accepted closed-halfplane formulation |
| PE | `papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md`; equations (1)–(40), with historical-source and zero-convention qualifications |
| PF | `papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md`; accepted v0.2 science, theorem 8 and Appendix D; no runtime evolution subsystem |
| PF-L | `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_THEOREM_AND_PROVENANCE_LEDGER_v0.2.md`; F1–F14, hypotheses H0–H6, constants register. Its preparation-time candidate wording is retained evidence. |
| PF-V | `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py` and `PAPER_F_v0.2_VALIDATION.json` in the same directory; published verifier/support, 131 recorded predicates, not rerun |
| K1R | `kernel_physics/K1_REFERENCE_SCAFFOLD_VALIDATION.md` and `.json`; Paper D correspondence and R1 symbolic-denominator fix |
| K2R | `kernel_physics/K2_HISTORICAL_Z_VALIDATION.md` and `.json`; Paper E observer correspondence and preserved source hashes |
| K3R | `kernel_physics/K3_MATHEMATICAL_DIAGNOSTICS_VALIDATION.md` and `.json`; passive accounting/display correspondence |
| CLOSE | `kernel_physics/K1_K2_K3_PARITY_CLOSEOUT.md`, accepted checkpoint `d2b1cbeca807ae33117f02f697e5eff0b4b1ca96`; dated pending language in receipts is superseded within scope |
| BASE | `kernel_physics/baseline_manifest.json`, `VALIDATION.md`, `validation.json`, `test_run.txt`; original 41-test evidence, not current-suite execution |
| BR | Local predecessor `C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md`; user-adopted lens-area toy option and conditional SRG/profile evidence; not included in repository |
| FACE | `research/folded_face_state/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md`; accepted technical representation evidence, supplemented by PB |
| GOLD | Local-only `research/GATE_TORUS_INVESTIGATION_v0.1/TRAJECTORIES.csv`, `REPORT.md` §4, `RESULTS.json`, `investigate.py`; saved 388 rows, not authoritative spatial registration |
| AX | Tracked `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION.csv`, matching `_REPORT.md` and `_RESULTS.json`; saved 18 rows |
| K0 | User's 2026-09-26 K0 work order and the companion engineering contract; new software contracts, no new science |

| Test alias | Exact existing repository-relative path | Static methods / status |
|---|---|---|
| TD | `kernel_physics/tests/test_dynamics.py` | 15 tracked |
| TCov | `kernel_physics/tests/test_covering.py` | 10 tracked |
| TR | `kernel_physics/tests/test_readouts.py` | 4 tracked |
| TF | `kernel_physics/tests/test_face_state.py` | 20 tracked |
| TG | `kernel_physics/tests/test_geometry.py` | 16 tracked |
| TS | `kernel_physics/tests/test_reference_scaffold.py` | 39 tracked |
| TZ | `kernel_physics/tests/test_z_manifold.py` | 37 tracked |
| TDiag | `kernel_physics/tests/test_z_diagnostics.py` | 36 tracked |
| TBR | `kernel_physics/tests/test_boundary_response.py` | 8 local-only |
| TSRG | `kernel_physics/tests/test_srg.py` | 9 local-only |
| TOP | `kernel_physics/tests/test_operating_region.py` | 9 local-only |
| TPIPE | `kernel_physics/tests/test_boundary_pipeline.py` | 4 local-only |

Static method definitions counted in K0: 177 tracked, 30 local-only, 207 total.
No tests executed. CLOSE owns the earlier 177/177 and 207/207 execution claims.
The four local-only hashes and the GOLD/AX hashes are pinned in the companion.

## Paper A and essential numerical support

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol (current source lines) | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 parameter tuple | A / CORE | Real eps,g,lambda and three real amplitude coefficients k; phase_strength=lambda | `kernel_physics/dynamics.py`: `DynamicsConfig` (28–44) | immutable | yes via Parameters | TD `test_input_state_and_config_remain_unchanged`, `test_invalid_shapes_and_parameters_rejected` | P1,P12 | PA §6.1; BASE | H08,H10,H16; k is not a wavenumber | NONE |
| A02 negative triangle Laplacian | A / CORE | Diagonal -2, off-diagonal 1; L3=ee^T-3I | `kernel_physics/dynamics.py`: `L3` (12) | immutable | yes through dynamics; no writable constant export | TD `test_l3_spectrum`; TCov `test_twelve_three_restriction_is_the_printed_l3` | P1,P2,P4 | PA §§1,5 | Negative-sign convention | NONE |
| A03 zero-phase convention | A / CORE | Arg0(z)=arg(z) for nonzero z; exact complex zero has +0 phase, including signed IEEE zeros | `kernel_physics/dynamics.py`: `arg0` (57–63) | derived | yes through step | TD `test_arg0_overrides_all_signed_complex_zeros` | P1,P3,P4 | PA §6.1; PE v0.1.1 source distinction | H09 | NONE |
| A04 simultaneous phase synchronization | A / CORE | Magnitude retained; phase plus lambda times both cyclic-neighbor sin(3 phase difference) terms, all from same pre-sync state; lambda=0 direct copy | `kernel_physics/dynamics.py`: `phase_sync` (66–84) | derived | yes through step | TD simultaneous-sync, amplitude-preservation, lambda-zero and zero-stratum tests | P1,P3,P4 | PA §6.1 | H09; no sequential in-place phase update | NONE |
| A05 nonlinear triad recurrence | A / CORE | V=Omega+eps*Omega*(k-abs(Omega)^2)+g*L3@Omega; F3=S(V) | `kernel_physics/dynamics.py`: `step3`, private `_advance` (87–104) | evolving (returns new array) | yes via step | TD hand pre-sync oracle; TF canonical-trajectory delegation test | P1–P8,P12 | PA §6.1; PB §5 | H03,H04,H08; no dt/no normalization | NONE |
| A06 nonlinear ring recurrence | A / CORE | Same onsite law on cycle M=3q, residue-repeated k, periodic two-neighbor coupling; unrestricted ring inputs | `kernel_physics/dynamics.py`: `step_ring`, `_advance` (87–112) | evolving (returns new array) | yes via explicit ring topology | TCov nonlinear lifts and off-sector periodic-wrap test | P1,P4,P12 | PA §6.2 | H17; no enforced projection to lifted subspace | NONE |
| A07 cycle Laplacian | A / CORE | Delta f(n)=f(n+1)+f(n-1)-2f(n), retaining repeated incidences at sizes 1 and 2 | `kernel_physics/covering.py`: `cycle_laplacian` (20–28) | immutable | no direct v1 export | TCov degenerate-cycle and divisor tests | P4 | PA §§2–3 | Positive integer sizes; not a simple-graph replacement at size 2 | NONE |
| A08 residue pullback | A / CORE | P[n,n mod d]=1 for all positive M,d | `kernel_physics/covering.py`: `pullback_matrix` (31–37) | immutable | no direct v1 export | TCov residue/d>M/nondivisor tests | P4 | PA §§2–3 | Intertwining iff divisor; V invariance has exceptional (3,2), not a new intertwining case | NONE |
| A09 isometric pullback | A / CORE | Q=P/sqrt(M/d), only for d dividing M; Q*Q=I and Q*Delta_M Q=Delta_d | `kernel_physics/covering.py`: `isometric_pullback` (40–47) | immutable | no direct v1 export | TCov Q-isometry/compression | P4 | PA §3 | H17; Q cannot replace P in cubic lift identity | NONE |
| N01 numeric adapter contract | Software / CORE | Strict finite scalar/vector validation; checked real/complex products, fsum totals, bra contractions; conservative subnormal/overflow failures | `kernel_physics/_response_numeric.py`: `ResponsePrecisionError`, `real_scalar`, `complex_vector`, `checked_real`, `product`, `total`, `complex_product`, `scale_complex`, `bra_dot`, `checked_array` | derived | yes exception; helpers private | TR precision tests; TZ PrecisionTests; TDiag ContractTests; local TBR/TSRG | P9,P10,P12 | Current shared implementation; K2R/K3R | H08; module docstring's old opt-in wording does not exclude readouts' actual dependency | NONE |

## Paper B: raw readout and the optional representation

The raw area identity is CORE. The optional frame construction is accepted,
but is not required to run Paper A, compute chirality, or produce a Run Record.
No FaceState operation supplies a physical shell-point dictionary.

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| B01 raw channel chirality | B,E / CORE | C=Re(Omega) cross Im(Omega), cyclic order (BC,CA,AB); no normalization/envelope | `kernel_physics/readouts.py`: `z_chiral` (7–17) | derived | yes | TR hand cross product/raw scaling; TF area-delegation test; TZ exact cross-product order | P3,P5–P10 | PB §6; PE (13),(14) | H08,H14; channel pseudovector, not ambient axial field | NONE |
| B02 oriented tangent frames | B,C / OPTIONAL | Tangent t_i=e_z cross n_i, centres from accepted shell; A=P1,B=P2,C=P3 | `kernel_physics/face_state.py`: `FaceFrames`, `face_frames`, `FRAME_ID`, `TRANSPORT_ID`, `FACE_ORDER`, private exact frame tuples (22–63) | immutable / derived frame result | no initial facade export | TF exact-source-frames and read-only-frame tests | P11,P12 | PB §§2–3; FACE | H01,H06,H14; current module imports optional profile chain | NONE |
| B03 decoding and encoding | B / OPTIONAL | D_i(q+ip)=q*t_i+p*e_z; E_i(v)=v dot t_i+i*v dot e_z on tangent plane; DE ambient projector | `kernel_physics/face_state.py`: `decode_to_faces`, `encode_from_faces` (73–112) | derived | no initial facade export | TF inverse-isometry/projector, normal-rejection, tiny-value tests | P3,P11,P12 | PB §3 adoption and Proposition 1 | H06,H08; exact-domain theorem versus rounded conversion | NONE |
| B04 matched transport | B / OPTIONAL | T_ij=t_i t_j^T+e_z e_z^T; source j to destination i; zero relative phase | `kernel_physics/face_state.py`: `transport` (123–133) | derived | no initial facade export | TF exact transport/composition, point-versus-vector rotation | P3,P11 | PB §4 | H01,H14; rank-two ambient operator, not a rigid point rotation | NONE |
| B05 signed-area accessor | B / CORE | A_ij=Im(conj(Omega_i)*Omega_j); antisymmetric, zero diagonal; area_triple delegates to B01 | `kernel_physics/face_state.py`: `area_triple`, `state_area` (136–154); sole calculation B01 | derived | yes raw triple through z_chiral; pair accessor not exported | TF signed-area independent geometric comparison and bitwise delegation | P3,P9,P11 | PB §6 theorem 4 | H14; even diagonal request evaluates full underlying readout and can fail | NONE |
| B06 canonical face-state value | B / OPTIONAL | Stores raw Omega, derives vectors once; from_faces initializes via E; step advances stored Omega exactly once then decodes | `kernel_physics/face_state.py`: `FaceState`, `from_faces`, `step`, `metadata` (157–207) | evolving canonical snapshot / derived view | no initial facade export | TF canonical trajectory, explicit initialization/profile errors | P1,P12 | PB §5 and Appendix A; FACE | H06,H11; optional profile=None vs explicit PROFILE_ID, no auto re-encoding | NONE |

## Paper C: exact geometry, uncoupled from dynamics

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 canonical folded module | C / CORE | Width-one exact weld of three regular octagonal panels at beta=pi/3; 18 vertices, 21 edges, 3 oriented faces | `kernel_physics/geometry.py`: `folded_module`, `FoldedModule` (57–150) | immutable | yes via get_geometry(C01) | TG printed 18 vertices/face cycles/edges | P11,P12 | PC §§2–4; BASE | H01,H18; coordinate geometry only | NONE |
| C02 fixed dimensions and material octagon | C / CORE | w=1, s=sqrt(2)-1, beta=pi/3, half=1/2; eight ordered (u,z) vertices; centroid=(0,sqrt(3)/6,0) | `kernel_physics/geometry.py`: `WIDTH`, `EDGE_LENGTH`, `FOLD_ANGLE`, `HALF`, `LOCAL_OCTAGON`, `CENTROID` (16–26) | immutable | yes in C Geometry Record | TG width/local-octagon tests | P11 | PC §§2–4 | Geometric width convention, not historical dynamics default | NONE |
| C03 general-angle panel maps | C / CORE | Three affine panel maps of PC theorem 2, from reversed stacked start; real beta; canonical weld at pi/3 | `kernel_physics/geometry.py`: `panel_point` (35–50) | derived | no arbitrary-beta facade export; used by C01 | TG symbolic closure and fixed-hinge tests | P11 | PC theorem 2 | H01; intermediate configurations not certified nonintersecting | NONE |
| C04 topology/incidence | C / CORE | Sorted undirected edges; count-two seams/count-one boundaries; degree-two boundary loops; V-E+F=0 | `kernel_physics/geometry.py`: `FoldedModule.edges`, `seam_edges`, `boundary_edges`, `boundary_loops`, `euler_characteristic` (64–111) | derived | yes in C Geometry Record | TG edge/seam/Euler/boundary/opposite-incidence tests | P11,P12 | PC §§4–6 | Loops begin at lowest vertex, lower neighbor first; no duplicated closing vertex | NONE |
| C05 normals and dihedral | C / CORE | Unit normal from oriented face coordinates; normal separation 2pi/3, interior wedge pi/3 | `kernel_physics/geometry.py`: `face_normal`, `normal_separation`, `interior_dihedral` (113–133) | derived | yes normals in record; angles in provenance | TG normals and 60/120 tests | P11 | PC §7 | H01; do not confuse normals with fold labels | NONE |
| C06 central section | C / CORE | At real abs(height)<=s/2, three unit segments forming equilateral section curve | `kernel_physics/geometry.py`: `central_section` (153–163) | derived | yes explicitly requested section heights | TG central-section/domain tests | P11,P12 | PC central-section definition | H18; no cap/fill; height default internal only | NONE |
| C07 D3h generators | C / CORE | C3 rotation around centroid vertical axis; x=0 and z=0 mirrors; 12 accepted actions | `kernel_physics/geometry.py`: `rotate_c3`, `reflect_vertical`, `reflect_horizontal` (166–183) | immutable transform / derived point | yes symmetry metadata/permutations | TG generator edge/whole-face preservation and 12-action relations | P11 | PC §9 | H14; point transforms include axis offset | NONE |

## Paper D: explicit exact reference scaffold

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| D01 octagon and exact hull | D / OPTIONAL | Positive s; a=(1+sqrt(2))*s/2,w=2a,R_oct=s/(2sin(pi/8)),b=s/2; ordered octagon outline and closed hull | `kernel_physics/reference_scaffold.py`: `Octagon`, `ConvexHull` (73–88,131–168) | immutable | explicit optional via D03 record | TS octagon metrics/outline/filled distinction | P11,P12 | PD (1)–(3); K1R | H05,H18; not welded material | NONE |
| D02 closed halfplane regions | D / OPTIONAL | normal dot x<=offset; slack; intersection including boundary; contains=True/False/None | `kernel_physics/reference_scaffold.py`: `HalfPlane`, `HalfPlaneIntersection` (91–128) | immutable / derived predicate | explicit optional via D03 record | TS all-halfplanes/active-edge and connector/apex tests | P11,P12 | PD (16a); K1R | H05,H18; not triangle minus ordinary open interiors | NONE |
| D03 aligned reference family | D / OPTIONAL | s>0,g_gap>0; p=(s+2g_gap)/(2sqrt(3)), L=p+a; A_i=p*u_i-s*t_i/2, B_i=p*u_i+s*t_i/2 | `kernel_physics/reference_scaffold.py`: `ReferenceScaffold`, `from_radius`, p/L/A/B/vertices/selected_edges/connectors/outline/side_lengths/edge_roles (171–243) | immutable | explicit optional via get_geometry(D03) | TS printed eq11, directed edges, radius parameterization | P11,P12 | PD §§4–8; K1R/CLOSE | H01,H05; from_radius needs p>s/(2sqrt(3)), not p>0 | NONE |
| D04 metrics and regular member | D / OPTIONAL | R^2=(s^2+s*g_gap+g_gap^2)/3; area=sqrt(3)*(s^2+4s*g_gap+g_gap^2)/4; regular iff g_gap=s | `kernel_physics/reference_scaffold.py`: `regular`, `circumradius_squared`, `area`, `q_H`, `regularity_residual`, `is_regular` (194–196,245–265) | derived | explicit optional in D03 record | TS circumcircle/area/regularity, D6-role-D3/traversal-C3 tests | P11 | PD §§7–9 | Regular polygon D6 does not preserve E/G roles under every action; unknown equality None | NONE |
| D05 support triangle and cells | D / OPTIONAL | Three support and three connector closed halfplanes; support hull and corner hulls; W=s+2g_gap | `kernel_physics/reference_scaffold.py`: `support_halfplanes`, `connector_halfplanes`, `filled_hexagon`, `support_vertices`, `support_triangle`, `W`, `corner_cells` (267–296) | derived | explicit optional in D03 record | TS support/cell/dissection/nonoverlap tests | P11 | PD §§8–10, (16a); K1R | H18; keep closed connector boundaries | NONE |
| D06 complete reference frames | D / OPTIONAL | Radial/tangent frames; planar_point=(L+x)u+y*t; vertical_point=(p*u+xi*t,z); full octagon domains | `kernel_physics/reference_scaffold.py`: `RADIAL`, `TANGENT`, planar_centres/point/frames, vertical_centres/point/frames, top_selected_edges (19–20,298–336) | immutable frames / derived geometry | explicit optional in D03 record | TS complete planar/vertical frames and top-height tests | P11 | PD (17),(19); K1R | H01; selected edge A->B reverses local outline indices 4->5 | NONE |
| D07 Paper-C comparison placement | D / OPTIONAL | p0=a/sqrt(3); rigid map Rz(pi/6)x+(0,a/sqrt(3),0); only width one equals geometry.py | `kernel_physics/reference_scaffold.py`: `paper_c_member`, `paper_c_rigid_map` (339–352) | derived | explicit optional construction/comparison metadata | TS finite vertex/edge rigid comparison | P11 | PD comparison construction; K1R | Frame order 0,1,2 -> P3,P1,P2, not P1,P2,P3 | NONE |
| D08 translation and fixed-centre shrink | D / OPTIONAL | Translate individual centres to p*=sqrt(3)s/2 OR shrink C-member local xi,z by (1+sqrt(2))/3 at fixed vertical centres | `kernel_physics/reference_scaffold.py`: `translate_paper_c_to_regular`, `shrink_paper_c_at_fixed_centres`, `PAPER_C_SHRINK_FACTOR` (21,355–372) | derived | explicit optional separate constructions | TS translation/shrink distinction, width-one shrink and symbolic R1 regressions | P11 | PD §§13–14; K1R | Not common rigid translation; shrink changes top height/planar centres, not generic p rule | NONE |

## Paper E: observer states, results, and passive diagnostics

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| E01 explicit clock | E / OPTIONAL | theta=2pi*(q mod N)/N; advancement q'=(q+q_step) mod N,t'=t+dt | `kernel_physics/z_manifold.py`: `Clock`, `clock_angle`, `advance_clock` (46–82) | observer; q/t evolve, N/q_step config immutable | explicit optional | TZ ClockTests | P5,P9,P12 | PE (1),§3.3; K2R | H03,H04,H16; supplied q retained until advance; dt lost-to-rounding raises | NONE |
| E02 norm and staged scalar | E / OPTIONAL | kappa=norm(Omega),rho=kappa/(1+kappa); z=lambda_vp*rho*exp(-gamma*t)*cos(3(theta-theta_lock)) | `kernel_physics/z_manifold.py`: `StagedConfig`, `state_norm`, `saturated_norm`, `staged_scalar`, private `_harmonic` (90–142) | immutable observer config / derived scalar | explicit optional | TZ scalar/high-precision/signed-config/frozen-harmonic tests | P5,P9 | PE (1),(2),(5)–(7); K2R | H08,H16; floating rho may round to 1; frozen harmonic is not trajectory extrema | NONE |
| E03 macro, blend and result | E / OPTIONAL | M=z(cos(theta),sin(theta),1); T=alpha*M+beta*C; readout stores decomposition | `kernel_physics/z_manifold.py`: `macro_vector`, `blend_vectors`, `ZReadout`, `observe_staged`, `observe_ema` (145–199,262–265) | derived observer result | explicit optional | TZ exact macro cone/norm, cancellation, alias, pure observation tests | P5,P9,P12 | PE (2),(8),(18); K2R | H03,H12,H14; C still evaluated when beta=0 | NONE |
| E04 committed EMA state and update | E / OPTIONAL | J=Im(O1*conj(O2)*O3),j=J/(1+abs(J)); m'=(1-.01)m+.01*j using newly committed Omega; EMA z=harmonic+m | `kernel_physics/z_manifold.py`: `EMAConfig`, `EMAState`, `cubic_j`, `normalized_cubic`, `advance_ema`, `ema_scalar` (202–259) | observer; config immutable,m evolving | explicit optional | TZ cubic hand values, exact one/two updates, pure observation, unrolling and endpoint tests | P5,P9,P12 | PE (15),(39),(40); K2R | H03; no gamma; fixed historical .01 expression order; cubic is not C or U(1)-invariant | NONE |
| E05 constructor-zero record | E / HISTORICAL | Validated initial Omega/config/clock with m=0 and all stored Z fields zero; no formula evaluation | `kernel_physics/z_manifold.py`: `ConstructorZeroRecord`, `historical_constructor_zero` (268–297) | observer initialization / derived historical record | explicit optional initial mode | TZ InitializationTests | P5,P9,P12 | PE §3.3; K2R | H12; differs from recomputed row zero | NONE |
| E06 norm and Q accounting | E / OPTIONAL | Q(v)=v1^2+v2^2-v3^2; full alpha^2/beta^2/cross expansions for norm^2 and Q; retain Q(M) | `kernel_physics/z_diagnostics.py`: `quadratic_form`, `ReadoutAccounting`, `readout_accounting` (75–141) | derived passive diagnostic | explicit optional | TDiag exact generic blend, noncone/signed-weight/inconsistent-record tests | P9,P10 | PE (18),(20); K3R | H15; no repair of supplied readout; cone only for defined M | NONE |
| E07 Gram/slack accounting | E / OPTIONAL | A=x dot x,B=y dot y,h=x dot y,I=A+B; norm(C)^2=AB-h^2; I^2/4-norm(C)^2=(A-B)^2/4+h^2 | `kernel_physics/z_diagnostics.py`: `ChiralAreaAccounting`, `chiral_area_accounting` (144–182), delegates C to B01 | derived passive diagnostic | explicit optional | TDiag Gram/slack exact identities, delegation and no-clamp tests | P10 | PE (16),(17); K3R | H08,H15; rounded zero not equality proof | NONE |
| E08 historical alignment result | E / HISTORICAL | u(v)=0 below norm 1e-12, unit v otherwise; TM/CM/TC dot values plus resolution flags | `kernel_physics/z_diagnostics.py`: `HistoricalAlignment`, `historical_alignment` (185–216) | derived passive diagnostic | explicit optional by historical name | TDiag threshold/equality/resolution and stable-large tests | P10,P12 | PE (23); K3R | H15,H16; unresolved zero is not orthogonality, no clipping | NONE |
| E09 finite-step intensity budget | E / OPTIONAL | D=eps*(k-s)*Omega+gL3Omega; delta I=2eps sum(k_i*s_i-s_i^2)-2gP+norm(D)^2 | `kernel_physics/z_diagnostics.py`: `IntensityBudget`, `intensity_budget` (236–287); imported L3 | derived passive diagnostic | explicit optional | TDiag exact finite budget, mixed signed high-precision, actual-step and nonmutation tests | P10,P12 | PE (33)–(36); K3R | H15; diagnostic_pre_sync_prediction is not a next-state authority | NONE |
| E10 real potential | E / OPTIONAL | V=eps sum(s_i^2/4-k_i*s_i/2)+(g/2)sum_{i<j}abs(Oi-Oj)^2; negative six-real-coordinate gradient is D | `kernel_physics/z_diagnostics.py`: `potential` (290–302) | derived passive diagnostic | explicit optional | TDiag six-real-gradient, exact/runtime overshoot tests | P10 | PE (37),(38); K3R | H15; discrete map need not decrease V | NONE |
| E11 direct and cylinder displays | E / OPTIONAL | Direct stored vector columns; cylinder=(kappa*cos(theta),kappa*sin(theta),z) | `kernel_physics/z_diagnostics.py`: `Coordinates`, `direct_history_coordinates`, `cylinder_point`, `cylinder_history_coordinates` (305–365) | derived display result | explicit optional outside Runner/GeometryRecord | TDiag direct fallback, empty history, custom N/zero-height tests | P10,P12 | PE (24); K3R | H13,H14,H16; different information from M/C/T, no shell attachment | NONE |
| E12 entire-history torus display | E / OPTIONAL | PE (25); H_z=max(abs(z_history))+1e-9, saturated minor radius and history-normalized angle | `kernel_physics/z_diagnostics.py`: `HistoryTorus`, `history_torus_coordinates` (368–413) | derived batch display result | explicit optional outside Runner/GeometryRecord | TDiag torus oracle, appended-history, saturation, inverse-domain and information-loss tests | P10,P12 | PE (25)–(28); K3R | H07; domain R>r_max>0; no runtime inverse | NONE |
| E13 observer-only analytic results | E / RESEARCH_ONLY | Frozen harmonic critical angles/signs, macro cone and pairing, pointwise symmetry, conditional torus inverse/information loss and EMA bounded-memory proofs | PE manuscript §§4–11,19; runtime witnesses E01–E12, **no separate theorem engine** | derived proof/oracle | no theorem subsystem | TZ symbolic groups; TDiag ExactTests/DisplayTests; PE `check_symbolic.py` evidence | P9,P10 | PE; K2R/K3R | Frozen hypotheses must not become evolving-state claims | NONE |
| E14 historical analysis consumers | E / RESEARCH_ONLY | Viewer percentile scaling, spike statistic/threshold analysis, preserved-run parameter comparisons, conditional forcing discussion | PE manuscript §§12–16,§17.2; `papers/PAPER_E/evidence/source_snapshots/staged/diagnostics.py`, `geometry_3d.py`; no supported current kernel owner | derived research analysis | no | PE preserved runs/symbolic evidence; no v1 runtime test claimed | P10 (exclusion),P12 | PE (29)–(32) and limits | No diagnostic threshold, forcing or viewer scaling feeds Omega | NONE |

## Paper F: accepted parity oracles, never a dynamics subsystem

All rows below classify theorem/proof objects as RESEARCH_ONLY. The runtime
targets are references to the existing owners, not ownership transferred to
research. Exact ideal-arithmetic results and binary64 traces remain distinct.

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol or proof owner | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| F01 synchronization and chirality decomposition | F / RESEARCH_ONLY | e=(1,1,1); synchronized scalar restriction; C=e cross(alpha*eta-beta*xi)+xi cross eta | PF-L F1–F3 / PF manuscript; targets `kernel_physics/dynamics.py:step3,L3` and `kernel_physics/readouts.py:z_chiral` | derived oracle | no | PF-V F1–F3; AX historical decomposition | P2,P6,P7 | PF H0–H3 | Historical seed is not a small perturbation of its mean | NONE |
| F02 transverse basis/group/isotropy | F / RESEARCH_ONLY | u=(1,-1,0)/sqrt(2),v=(1,1,-2)/sqrt(6),u cross v=e/sqrt(3); S3 plus conjugation D6 seed action, qualified orbit classes | PF-L F4–F6 / PF manuscript; target existing step3/z_chiral | immutable oracle basis / derived identities | no | PF-V F4–F6; AX | P3,P6,P7 | PF; PB channel transformation laws | D3 has three oriented root orbits, D6 two; projective count differs; not shell D3h | NONE |
| F03 exact one-step harmonics and finite jets | F / RESEARCH_ONLY | PF-L F5,F7,F8 exact projections and all-n coefficient recurrences at lambda=0; angle leading h^4*sin(6phi) | PF manuscript / PF-V; target `kernel_physics/dynamics.py:step3` then `readouts.py:z_chiral` | derived oracle | no | PF-V F5,F7,F8 exact expressions | P1,P7 | PF H0–H3 | Nonzero a needed for coefficient division; a>0 for stated angle branch; finite n not uniform infinity | NONE |
| F04 limiting coefficient and local interpretation | F / RESEARCH_ONLY | Rational coefficient sum; at eps=1/20,g=1/5 gives 13375/1107936648; observed local limit additionally requires analytic hypotheses | PF manuscript / PF-L F9–F12 / PF-V | derived oracle | no | PF-V F9–F12 and published proof, no finite test substitutes | P7 | PF H1,H2,H4–H5 | No universal six-axis selector; chirality direction undefined at zero; local not global basin | NONE |
| F05 local spectrum/normal form | F / RESEARCH_ONLY | Five-real-coordinate quotient spectrum (m,r,r,a,a), m=1-2eps,r=1-2eps-3g,a=1-3g; phase changes a to a*(1-9lambda) | PF manuscript / PF-L F10–F12 / PF-V; no current runtime normal-form owner | derived proof | no | PF-V exact spectrum, valuation checks; analytic proof and Appendix D | P7,P8,P12 exclusion | PF H4–H6 | Gauge removes common phase; not holomorphic C3 dynamics; no new evolution layer | NONE |
| F06 full-composition lambda derivative | F / RESEARCH_ONLY | One-step coefficient -eps^2/(36a)+lambda*(eps*a^2/4+47a^4/32)+O(lambda^2); historical derivatives 99/2500 and 34494041501/849664304944 | PF theorem 8/Appendix D; PF-L F13–F14; target step3 composition | derived oracle | no | PF-V F13–F14 exact differentiated coefficient system | P8 | PF H0–H2,H6 | Isolated-phase 243/160 is different input/observable; first order only, nonzero local chart | NONE |
| F07 saved trajectory witnesses | F/software / RESEARCH_ONLY | GOLD: 2 runs*97 rows*2 observers=388; AX:2 seeds*9 rows=18 | GOLD and AX CSV/report owners; runtime targets A05/B01/E01–E04 | immutable evidence / derived samples | no runtime imports | Hashes/row counts in companion; PF-V reads AX without evolving model | P5,P6 | Saved predecessor experiments; PF support | Exclude registration/display fields from core parity; golden publication O03 | NONE for bytes/meaning; O03 for availability |

## Explicit optional candidates and historical values

| ID / name | Paper / class | Mathematical definition or exact reference | Authoritative module : symbol | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| X01 lens area-norm response | Adopted option / OPTIONAL | theta=acos(d/(2r)); I=(2theta-sin(2theta))/pi; gain=sqrt(I); preparation gain*(xi tensor f0), helicity-major | `kernel_physics/boundary_response.py`: `RESPONSE_ID`, `theta_from_lens`, `lens_area_fraction`, `lens_area_gain`, `prepare_area_response` | derived initialization | no pending O01 | TBR 8 and TPIPE 4 local-only; BR high-precision/direct references | P12 plus candidate support tests if A | BR; package README; not A–F physical law | Domain theta in [0,pi/2]; area and gain have different numeric ranges; no normalized xi | NONE mathematics; O01 support |
| X02 fixed November operators | Historical adopted option / OPTIONAL | Fourier columns f0,f1,f2; R,Z,C,A=RZC,B, U=B tensor A with fixed historical literals | `kernel_physics/srg.py`: `SRGOperators`, `fourier_basis`, `fixed_november_srg` | immutable definition / fresh array result | no pending O01 | TSRG operator/weighted-cycle tests; BR conditional reduction | P12 plus candidate tests if A | BR/current fixed implementation | H02,H11,H16; f1 uses conjugate root ordering | NONE mathematics; O01 support |
| X03 mode gauge/extraction | Adopted option / OPTIONAL | Named positive-pivot spectral-projector gauge; generic bra projection versus named B eigenmode extraction | `kernel_physics/srg.py`: `GAUGE_ID`, `HelicityMode`, `helicity_mode`, `project_bra`, `extract_helicity` | derived | no pending O01 | TSRG gauge, full-space intertwining and cancellation tests | P12 plus candidate tests if A | BR H1 conditional extraction | No eigensolver-order convention or overlap threshold; generic bra has no H1 promise | NONE mathematics; O01 support |
| X04 SRG initialization handoff | Adopted option / OPTIONAL | gain*(chi-dagger xi)*eigenvalue^n*cycle_gain(n)*f_(n mod 3); n counts transfer only | `kernel_physics/srg.py`: `HandoffResult`, `metadata`, `handoff_area_response`, private `_cycle_gain` | derived initial Omega / immutable receipt | no pending O01 | TSRG direct U^n fixture and TPIPE integration | P12 plus candidate tests if A | BR C3/current implementation | H02; no downstream recurrence or geometry coordinates | NONE mathematics; O01 support |
| X05 radius-three profile | Adopted option / OPTIONAL | eps=1/20,g=1/5,k_i in [0,8], actual max abs(Oi)<=3; uniform incident norm<=3sqrt(3) is sufficient, not necessary | `kernel_physics/operating_region.py`: `PROFILE_ID`, `UNIFORM_INCIDENT_BUDGET`, `bounded_config`, `validate_bounded_triad`, `validate_uniform_incident_budget`, `initialize_bounded_area`, `step_bounded_triad` | immutable profile / derived validation / returns new state | no pending O01 | TOP 9 and TPIPE 4 local-only; TF profile callers | P12 plus candidate tests if A | BR; uses existing DynamicsConfig/step3 | H08,H16; no clipping; exact bound not all-input machine safety; no radius-ten extension | NONE mathematics; O01 support |
| L01 experiment recurrence literals | A/F evidence / HISTORICAL | eps=.05,g=.2,k=(1,1,1),lambda=0 and .001 in named saved experiments | GOLD report §4; AX report; PF-L H5; **no general default owner in dynamics.py** | immutable preset evidence | yes explicit values/provenance, no default Parameters | GOLD/AX/PF-V | P5–P8,P12 | GOLD,AX,PF | Rationale O02; hypotheses recorded, not universal parameters | NONE values; O02 rationale |
| L02 historical seed | F/evidence / HISTORICAL | (.2+.3i,-.4+.1i,.1-.2i); exact rational reading for PF algebra vs binary literals for replay | GOLD report §4; PF-L F3; **no current kernel seed function**; planned `_presets.py:historical_seed` | immutable preset | yes by `gate_torus_seed_v1` only | GOLD; PF-V F3 | P5,P6,P12 | GOLD/PF; earliest located provenance not origin claim | H16; no random substitute or normalization | NONE values; O02 rationale |
| L03 staged/EMA coefficient literals | E / HISTORICAL | lambda_vp=.618,gamma=.577,theta_lock=.244,alpha=1,beta=.5; no gamma for EMA | `kernel_physics/z_manifold.py`: `StagedConfig`, `EMAConfig`; underlying current defaults | immutable preset | explicit optional named observer preset or explicit constructor | TZ literal-default tests; K2R source hashes | P5,P9,P12 | PE recovered staged/committed sources | H16; .618 is literal, not golden-ratio replacement; lock rationale O02 | NONE values; O02 lock rationale |
| L04 clock/run and memory literals | E / HISTORICAL | q=0,N=12,t=0,q_step=1,m=0,dt=.1; EMA tau=.01, retention evaluated as 1-tau | `kernel_physics/z_manifold.py`: `Clock`, `EMAState`, `advance_ema`; dt in PE/GOLD runner evidence | immutable preset / initial observer state | explicit optional historical preset | TZ clock/memory/update tests; GOLD schedule | P5,P9,P12 | PE §3.3,(39); K2R | H03,H04,H16; fixed EMA literal is part of named historical variant, not tunable new law | NONE |
| L05 November literals and gauge IDs | Historical / HISTORICAL | eta=.423,gamma=.577,lambda_c=.618,clock_fraction=.244; fixed named gauge/response/profile strings | `kernel_physics/srg.py`: `NovemberParameters`, `NOVEMBER`, `GAUGE_ID`; boundary RESPONSE_ID/operating PROFILE_ID | immutable preset | no pending O01 | TSRG literal/operator tests; BR | P12 plus candidate support | BR/source November reconstruction | H16; different clock_fraction and theta_lock meanings despite same decimal | NONE defined values |
| L06 display/precision conventions | E/software / HISTORICAL | Alignment threshold 1e-12; torus regularizer 1e-9,R=2,r_max=1,N=12; face tangency 8*machine epsilon | `kernel_physics/z_diagnostics.py`: `historical_alignment`, `history_torus_coordinates`, cylinder helpers; `face_state.py:TANGENCY_RTOL` | immutable convention | explicit optional under named operations; public display dimensions explicit | TDiag threshold/rounding tests; TF normal-rejection tests | P10–P12 | K2R/K3R/FACE | H07,H08,H16; machine-validation tolerance is not scientific zero threshold | NONE |

## Research-only exclusions and software contracts

| ID / name | Paper / class | Definition/reference | Authoritative module : symbol or owner | Ownership | Public exposure | Existing test/oracle | Future parity | Provenance | Hazards | Ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 spatial registration and interpretation | Research / RESEARCH_ONLY | M/C/T attachment, gates/apertures, finite patches, restoring laws, physical-field/EM/RS comparisons, six-axis selectors and spatial-alignment narratives | `research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md` and local related research; no accepted runtime owner | derived research | no | GOLD evidence only for saved numeric columns; no physical oracle | P12 exclusion | K0 anti-drift; research's stated assumptions | Cannot become Omega/geometry dictionary or feedback | NONE exclusion; physical model not adopted |
| R02 Twisted Hex Crystal family | Research / RESEARCH_ONLY | Existing geometric research family and registration experiments | `research/twisted_hex_crystal_registration_v0.1/` including `family_analysis/PUBLICATION_CENSUS.json`; no kernel owner | immutable research definitions | no | Existing research receipts only, not inspected as new science | P12 exclusion | Starting commit; K0 closes geometry search | No extension, substitute shell, or runtime promotion | NONE exclusion |
| R03 further physical/reconstruction narratives | Research / RESEARCH_ONLY | Warp/physics, toroidal physical motifs, mechanical clocks, Z feedback, historical physical interpretations | Existing research/supporting assets; no accepted current kernel symbol | derived research | no | No v1 runtime oracle claimed | P12 exclusion | K0 boundary; CLOSE outstanding limits | No runtime vocabulary or laws inferred from narrative | NONE exclusion |
| R04 larger-ring stability and conditional feedback studies | A/research / RESEARCH_ONLY | PA §§7–10 atlas/Floquet/feedback compatibility; accepted scoped results do not add feedback to current recurrence | PA proofs/evidence; no current stability/feedback runtime API | derived proof/analysis | no | PA frozen numerical tables/proofs; TCov tests only covering portion | P4 boundaries,P12 exclusion | PA; BASE scope | Stability not global basin; sufficient feedback criterion is not mandatory feedback | NONE exclusion |
| S01 immutable public values/validation | Software / CORE | Explicit Parameters, State, clock/config/memory constructors; immutable snapshots and strict input contract | **Not implemented**; planned `kernel_physics/_contract_types.py` and `api.py`; current underlying A01/A05/E01–E04 | immutable config / evolving snapshots | yes | Existing TD/TZ/TDiag purity tests are partial precedent, not full facade tests | P12 | K0 §§2–3 | H08,H11,H16 | NONE contract |
| S02 Runner and restart | Software / CORE | One authoritative step, explicit observer schedule, passive requested diagnostics, complete rows and pure replay decoding | **Not implemented**; planned `kernel_physics/_runner.py:run,resume` | evolving orchestration snapshots | yes | GOLD schedule; existing trajectory-with/without-observer tests | P5,P9,P12 | K0 §4 | H02–H04,H12,H15 | NONE contract |
| S03 Run Record | Software / CORE | KERNEL_RUN_RECORD 1.0.0, explicit complex binary64 codec and independent observer snapshots/provenance | **Not implemented**; planned `kernel_physics/_records.py:RunRecord` | immutable record of evolving states | yes | No existing schema/round-trip test; metadata snippets are not this schema | P5,P12 | K0 §5 | No geometry fields; decoding does not run equations | NONE contract |
| S04 Geometry Record | Software / CORE | GEOMETRY_RECORD 1.0.0; explicit C/D identity, exact codec, renderable construction outputs, coupling=none | **Not implemented**; planned `kernel_physics/_geometry_records.py:GeometryRecord,get_geometry` | immutable construction record | yes | Existing TG/TS exact oracles; no existing schema test | P11,P12 | K0 §6 | H01,H05,H18; preserve exact versus float distinction | NONE contract |
| S05 public/import boundary and provenance IDs | Software / CORE | api v1.0.0; definitions in ledger 0.1; allowed dependency graph; source/edition/module hash records | `kernel_physics/__init__.py:__version__` current 0.1.0; public facade **not implemented**; planned api/records | immutable contract | yes | TS/TZ/TDiag import tests partial precedent; static current imports read in K0 | P12 | K0 §§1,7,12 | Package version is not ledger or schema version; no research imports | NONE contract |
| O01 optional support decision | Software / OPEN | A=support/publish predecessor tests, B=quarantine from v1; no decision inferred | X01–X05 current modules; companion §10 is the decision package | immutable decision pending | no until adjudicated | CLOSE local-only obligation; freshly matched hashes, no rerun | P12 and conditional support gates | K0 requires GPT/Hilmir decision | Support status differs from mathematical acceptance | OPEN: AWAITING_GPT_HILMIR_DECISION |
| O02 historical selection rationale | Provenance / OPEN | Why eps=.05,g=.2,the seed,and lock=.244 were originally selected is unresolved | PF-L constants register/F3/H5; PE provenance; no authority invented | immutable unknown provenance | no inferred rationale | Existing provenance-open statements | P5,P7,P8,P12 labels | PF/PE/K0 | Presets record known literals and unknown motivation separately | OPEN: original motivation not recovered; nonblocking for named literals |
| O03 golden fixture publication | Software/evidence / OPEN | GOLD exists locally, correct hash/388 rows; clean-clone P5 availability not yet authorized | Local GOLD CSV/report; no tracked golden fixture owner | immutable evidence / packaging pending | no runtime import | Fresh hash/count, predecessor evidence only | P5,P12 | K0 companion §§9,11 | Must not claim portable P5 completion from local-only data | OPEN: bounded K2 fixture publication decision |

## Completeness and closeout interpretation

Every public symbol in the current core/observer/diagnostic/scaffold modules is
owned above either directly or as a named family property. Private validation,
array-copy and geometric canonicalization helpers belong to their owning row;
they are not alternative scientific definitions. Paper theorems without runtime
owners are explicitly proof/oracle objects, not promises of missing subsystems.
Significant optional candidate operators, presets and exclusions are classified.

The companion freezes actual public signatures, both schema versions, exact
K1 files, import tests, and P1–P12 tolerances/pass/failure meanings. The ledger's
current implementation references do not authorize K0 edits to any referenced
file. Pending support/provenance/fixture decisions are the only OPEN families;
they do not conceal unresolved authority for an accepted runtime equation.

## Additive Paper G observation contract (K-G0/K-G1)

The [axial observation extension](K0_AXIAL_OBSERVATION_EXTENSION_v0.1.md)
defines passive AX01/AX02 under package 0.2.0 and observation API 1.0.0.
This separate extension does not renumber or reinterpret any frozen definition
above, change record ledger 0.1, or authorize observer feedback. Paper G and
its exact/interval results remain distinct from binary64 observation outputs.
