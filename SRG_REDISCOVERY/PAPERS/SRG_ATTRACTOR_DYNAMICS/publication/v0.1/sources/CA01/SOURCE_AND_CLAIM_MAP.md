# CA01 source and claim map

All local source paths below are relative to `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, unless marked as packet input. Actual starting HEAD: `2ecc2ded685fd210bd3cda226eb9731156dc167e`, branch `main`. Historical checkpoint IDs in packet notes were not substituted for this read.

The machine-readable [consumed-source registry](evidence/consumed_sources.json) records original absolute paths, byte counts, full SHA-256 identities and the exact snapshot paths bundled for review. This table adds scientific locators. A source's historical instruction or publication recommendation is evidence about that earlier task, not authority to alter CA01's scope.

## Primary definitions and lineage

| ID | Exact source and locator | What was recovered | Limit |
|---|---|---|---|
| S1 | Packet `received/inputs/SGR_simulations.pdf`, physical pp.5-6, section 3/Figure 3 | Grid 100x100, coordinates [-5,5], dt=.1; phase, radial field, ideal radial clip at 1, strict P5 centroid; named log `attractor_path_log.txt` | F3 H coefficients, total horizon, exact grid construction, percentile runtime and producer not fully specified there |
| S1-F4 | Same PDF pp.7-8, section 4/Figure 4 | 3-vector recurrence, 200 updates, dt=.1, four-term H; cross/roll, .8 clip with 1e-5, R=1/r=.5 torus formula; named `attractor_positions.csv` | Alpha and s0 absent; implementation of roll, clock scheduling and exact sample storage not recovered |
| S1-context | Same PDF p.9 section 5.2 and pp.11-13 sections 6-7, via matching R0 text | `attractor_positions.csv` reused for different experiments | Basename cannot identify lineage; overwriting is possible, not established |
| S2 | `SRG_REDISCOVERY/R0_SOURCE_RECOVERY/pdf_text/P16_SGR_simulations.txt`, lines 114-240 | Earlier full text extraction corresponding to matching PDF hash | Typography may be lossy; newly rendered PDF controls equation reading |
| F3-CODE | `SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Early_simulations/attractor_trajector_over_time.py`, lines 6-8, 11-29, 32-52, 55-68 | Concrete related field/clock/helper definitions, literal grid and argmin detector, list/log/plot tail | Does not implement the paper's percentile detector; cannot be certified as Figure 3's exact producer |
| F3-ARCHIVE | `SRG_REDISCOVERY/OLD_MATERIAL/Simulations.zip`, member `Simulations_Trash/Early_simulations/attractor_trajector_over_time.py` | Byte-identical 2,043-byte alias of F3-CODE | No independent experiment |
| SEARCH | R0 `script_inventory.json`, `data_inventory.json`, `pdf_inventory.json`, `supplied_archive_listing.json`; scoped loose/ZIP searches in `evidence/lineage_search.json` | 35 loose Python files and 30 ZIP Python members screened for field detector/cross/roll/log signatures; both requested data basenames absent from searched loose/archive contents | Bounded search, not proof that no version exists elsewhere. No whole-repository archaeological census |

S1 SHA-256: `2d803a28c0a9f4396149cf8700c2a772b5016574517061fb8761c3c50de1c547`.

F3-CODE / F3-ARCHIVE SHA-256: `4ab065454b3218261e1fa68fee6e74cbe013b5fb2867bdb02c345c6d4c606d3c`.

The search did not find F3's percentile producer, F4's cross/roll torus producer, `attractor_path_log.txt`, or `attractor_positions.csv`. Similar filenames `3Dtriangles.py` and `recursive_attractor.py` belong to the already reviewed SIM01 family. F4's initial point was **not** inferred from its raster. The check start (1,0,0) is a separately declared zero-torque control.

### Printed paper versus related code

| Feature | F3 paper | Related F3 code |
|---|---|---|
| H | Four terms, coefficients unspecified on p.5 | Lines 11-17: 2/.5, 1/.3, 1.5/.7, 1/.4 |
| Field | U=-sin(theta)H/(1+rho^2), V=cos(theta)H/(1+rho^2) | Lines 20-23 agree, evaluating rho by sqrt then squaring |
| Grid | 100x100 on [-5,5]^2 | Lines 32-34: np.linspace and np.meshgrid |
| Clock | dt=.1; no exact producer history | Lines 43-44: range(100), t=.1*t_step |
| Clip | Divide by max(1,m/1) | Lines 26-29: multiply by min(1,1/(m+1e-5)) |
| Detector | Mean coordinates of M<P5(M) | Lines 49-51: np.argmin, then np.unravel_index; one coordinate |
| State | Prescribed field/detector | Initial U,V zeros at line 37, overwritten at lines 45-46; path list never read into field |
| Save/plot | Log and Figure 3 | Lines 55-57 overwrite text log, four decimals; lines 62-68 connected plot/show |

No historical module top level was imported. Only the three inspected F3 helpers were extracted unchanged by AST into a namespace containing NumPy. The recovered source tail was not executed. The historical definitions and new diagnostic variants remain separate.

## Geometry definition and review identity

| ID | Exact source and locator | Use in CA01 |
|---|---|---|
| G | `kernel_physics/geometry.py`, constants/LOCAL_OCTAGON lines 16-26, `panel_point` lines 35-50, `folded_module` lines 136-150, section/rotation functions | Read-only accepted width-one host definition; no kernel import or runner |
| PC | `papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md`, sections 2-4, 6-9 | Exact host, O, open rim/section/notch distinction and geometric units |
| VC | `research/twisted_hex_crystal_registration_v0.1/verify_host_registration.py`, constants lines 11-18, `canonical_points` 44-66, `candidate_faces` 68-79 | Detached source-defined vertices and actual triangle connectivity, tau=0; no `build()` |
| HG/CJ | Same directory, `HOST_GEOMETRY.json` and `CANONICAL_CRYSTAL_CANDIDATE.json` | Stored host faces/vertices, source hashes and candidate face list; positive-tau illustrated member is not substituted for zero |
| RH | Same directory, `CRYSTAL_HOST_REGISTRATION_REPORT.md`, sections 1, 4-5 | Registration identity, limitations and distinct historical intersecting construction |
| SI/Z0/FA | Same directory, `family_analysis/SIGNED_FAMILY_IDENTITIES.md`, actual band sections; `ZERO_STATE_ANALYSIS.md`, sections on faces versus vertices; `TWISTED_HEX_FAMILY_ANALYSIS.md`, controlling evidence | The later zero extension, two hands and unchanged open faces; inherited results, not rerun |
| R0/R1/R2 | `papers/CENTRAL_GEOMETRY_Z_CHIRAL_RESPONSE/publication/v0.3/reports/` files `Z_AND_CENTRAL_TWISTED_HEX_CRYSTAL_GEOMETRIC_RELATIONSHIP_INVESTIGATION_v0.1.md`, `FULL_Z_AND_CENTRAL_PASSAGE_GEOMETRY_ANALYSIS_v0.1.md`, `Z_CRYSTAL_REVERSAL_AND_UPPER_LOWER_CORRESPONDENCE_ANALYSIS_v0.1.md` | Located authoritative repository editions of all requested reports; coordinate/face/opening definitions and placement limitations read |
| REVIEW | Same publication's `evidence/GPT_NUMERICAL_AUDIT_CLOSURE_CENTRAL_GEOMETRY_Z_CHIRAL_RESPONSE_v0.2.md` and `GPT_POST_AUDIT_FINALIZATION_CLOSURE_CENTRAL_GEOMETRY_Z_CHIRAL_RESPONSE_v0.3.md` | Applicable accepted scope inspected. No audit replay, new native step or publication action |
| Z/R | `kernel_physics/z_manifold.py`, `Clock`, `staged_scalar`, `macro_vector`, `observe_staged`; `kernel_physics/readouts.py`, `z_chiral` | Read as text to distinguish clock/state/channel/readout domains. Not applied to SRG and not executed |

The 20 October reversal report's `3b4aa9c...` is its historical read checkpoint. The current read is at `2ecc2ded...`. HG's recorded current G/PC source hashes matched before the new render. Source snapshots and full hashes are in the registry; no assumption of identity based on old HEAD alone was used.

The refined mesh is an established research reference, not a kernel adoption or a claim that its parameter/hand was selected by the host. Both zero hands are preserved. The author's sketch and Vajra image are included unchanged as packet references; neither was used to reconstruct dimensions, faces or a physical mechanism. No archaeological or religious inference is part of CA01.

## Inherited SIM01 scope

All three requested local files under `SRG_REDISCOVERY/SIM01_SURVIVING_RECURSIVE_MOTION/publication/v0.1/` were consulted: `SIM01_REPORT.md`, `review/SIM01_GPT_SCIENTIFIC_REVIEW.md`, and `ACCESS_AND_EVIDENCE_MAP.md`. The accepted verdict is bounded source/replay acceptance; A/B/C have multiple centers and retained velocities, with stored switching bits in C. Periodic coordinate wrapping differs from F4's torus-surface remapping. The tetrahedron offsets are a drawing operation. Their published finite results and clock caveats are inherited, not newly tested. The review's next-experiment suggestion was not executed.

## Claim-by-claim disposition

| Claim/question | Layer of mismatch or resolution | CA01 disposition/evidence |
|---|---|---|
| F3's marker is an evolving attractor | Old interpretation/caption | Field is prescribed; detector list is not point recurrence. Algebra and source lines 43-52 |
| The selected low magnitude region is central | New interpretation would be wrong | Selected points lie toward corners; their centroid may be central. Image 01/raw F3_01 |
| F3 code matches the printed detector | Producer/detector mismatch | Argmin versus P5 centroid, epsilon versus ideal clip. Historical file preserved |
| Numerical wandering is necessarily dynamics | Detector sensitivity | Verified tied-shell and plateau-rounding artifacts in declared controls; original path still unrecovered |
| A fully clipped field has a defined center | Detector degeneracy | Exact strict mask empty; floating normalization may create a spurious mask. Both retained |
| Continuous torque preserves this numerical radius | Discrete-step interpretation | Euler squared norm gains dt^2||qhat||^2; exact symbolic check and preflights |
| F4's torus operation is a projection in the idempotent sense | Operator name/definition | Printed P is non-idempotent and restricts off-axis outputs to z>0 |
| Figure 4 establishes an attracting triangle | Old caption, unverified producer/data | Raster cannot establish closure/attraction; printed forward decaying-clock model converges to fixed circle endpoints |
| F4 has no genuine attraction of any kind | Overly broad new interpretation | Rejected: exact limiting-map contraction and conditional driven convergence prove a real set-attraction result |
| The crystal explains/selects F4's endpoints | Unjustified geometry bridge | No canonical domain map or selected alignment; unit translation is explicitly illustrative |
| Heat, magnetism or light is identified | Physical interpretation gap | Variables/units/laws/empirical mapping absent; analogy remains possible |

## Output locators

`run_checks.py` contains the sole numerical execution; `ALGEBRA_AND_CHECK_PLAN.md` records the prior choices and ceilings. `raw/F3_00.npz` through `F3_15.npz` contain fields/masks. `raw/F4_remap_only.npz` contains 201 states and every update's torque/pre-remap/output/time/clip data. `passive_views.py` reads those arrays and detached geometry only. `verify_saved.py` is a separate saved-data checker with zero fresh evolution. PNG captions label exact limit objects, numerical controls and illustrative placement. No image is a certified reproduction of either original figure.
