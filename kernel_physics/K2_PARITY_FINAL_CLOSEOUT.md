# K2 final closeout — P1–P12 consolidated parity certification

The accepted kernel mathematics and the frozen public facade have passed the complete P1–P12 parity program within the explicitly stated domains, tolerances, historical qualifications, and claim boundaries.

K2_FINAL_STATUS = PASS. This is a documentation and fresh-verification closeout. No runtime, test, oracle, fixture, paper or predecessor receipt was modified. No new science or gate was added.

Authorized starting HEAD: `69046009a307fa8498bd7366c8214493eca7b833`. The final publication commit is resolved by:

```text
git log --diff-filter=A --format=%H -- kernel_physics/K2_PARITY_FINAL_CLOSEOUT.json
```

Literal final HEAD and independently verified origin/main are reported after publication. The receipt does not attempt to embed its own commit hash.

## Final status

```text
STARTING_HEAD = 69046009a307fa8498bd7366c8214493eca7b833
K2_FINAL_STATUS = PASS
P1 = PASS
P2 = PASS
P3 = PASS
P4 = PASS
P5 = PASS
P6 = PASS
P7 = PASS
P8 = PASS
P9 = PASS
P10 = PASS
P11 = PASS
P12 = PASS
P1_P12_PARITY_COMPLETE = YES
ACCEPTED_KERNEL_PARITY = COMPLETE
PUBLIC_FACADE_PARITY = COMPLETE
O01_STATUS = CLOSED_OPTION_B_QUARANTINE_V1
O02_STATUS = OPEN_NONBLOCKING_HISTORICAL_RATIONALE
O03_STATUS = CLOSED
ORACLE_BOUNDARIES = PASS
FALSIFIER_REGISTER = PASS
CLAIM_BOUNDARY_REGISTER = PASS
RECEIPT_RECONCILIATION = PASS
TRACKED_TESTS = 298
TRACKED_TEST_RESULT = PASS
OPTIONAL_LOCAL_TESTS = 30
OPTIONAL_LOCAL_RESULT = PASS
POST_HOC_TOLERANCE_WIDENING = NO
NEW_MATHEMATICS_ADDED_BY_K2 = NO
PRODUCTION_MATHEMATICS_CHANGED_BY_K2 = NO
GEOMETRY_DYNAMICS_COUPLING = NO
OBSERVER_FEEDBACK = NO
RESEARCH_PROMOTION = NO
PACKAGE_DISTRIBUTION_ENGINEERING_COMPLETE = NO
PACKAGE_DISTRIBUTION_ENGINEERING = NOT_YET_K3_COMPLETE
UI_STARTED = NO
FILES_CREATED = 2
FILES_MODIFIED = 0
K3_READY_FOR_AUTHORIZATION = YES
PRODUCTION_SOURCE_CHANGED = 0
EXISTING_TEST_CHANGED = 0
K0_CHANGED = 0
K1_CHANGED = 0
K2A_CHANGED = 0
K2B_CHANGED = 0
K2C_CHANGED = 0
PAPERS_CHANGED = 0
RESEARCH_CHANGED = 0
FIXTURES_CHANGED = 0
OPTION_B_MODULE_CHANGED = 0
```

## Authority reconciliation

| Phase | Source HEAD | Published HEAD | Receipt owner |
| --- | --- | --- | --- |
| K2a | 9cf34b207b772639a4a79c2bcb3332d292b4f947 | 24b62db7ff1960ac485789ff235d01a63f94e65a | kernel_physics/K2A_EXACT_INDEPENDENT_PARITY_VALIDATION.json |
| K2b | 24b62db7ff1960ac485789ff235d01a63f94e65a | 22b3009d51e4e47efda48acf52d234d00907fe2c | kernel_physics/K2B_FIXTURE_WITNESS_PARITY_VALIDATION.json |
| K2c | 22b3009d51e4e47efda48acf52d234d00907fe2c | 69046009a307fa8498bd7366c8214493eca7b833 | kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.json |

K0 authority/ledger and all six K2 phase documents were read without modification. P12 ownership was checked in K1 public documentation, implementation and the four contract test modules. All phase gate results, recorded source identities, fixture bytes/counts, exact stored constants, tolerances and test censuses reconcile. The JSON includes individual reconciliation checks and source SHA-256 identities. Papers A–F were not reopened for new mathematical interpretation.

K0 pending implementation/O01/O03 labels are dated snapshots: K1 explicitly resolved O01 as Option B; K2b closed O03. Earlier README K1/R1–K3 labels refer to a different predecessor task series, as K0 states. They do not claim completion of the present packaging K3. Detached test snapshots are distinct from publication HEADs. No predecessor receipt was changed to reconcile these roles.

Public API, KERNEL_RUN_RECORD and GEOMETRY_RECORD remain 1.0.0; ledger remains 0.1, exact geometry codec 1, and package version 0.1.0. These are different version roles, not inconsistencies.

## Definitive P1–P12 matrix

Evidence labels are defined in the next table. A PASS applies only to the stated domain and evidence class.

| Gate | Accepted claim | Runtime target | Independent evidence type | Result | PASS supports | PASS does not support | Receipt/test owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Paper-A one-step triad recurrence | dynamics.step3 / phase_sync / arg0 | EXACT_SYMBOLIC, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, EXACT_DISCRETE, NEGATIVE_FALSIFIER | PASS | Amplitude/coupling before simultaneous synchronization; Arg0(0)=0, signed-zero branches and bounded binary64 agreement. | Global dynamics, long-time stability, physical interpretation or arbitrary nonfinite behavior. | K2a; test_parity_p01_p04.py (P1Tests) |
| P2 | Equal-k synchronized scalar reduction | dynamics.step3 / L3 | EXACT_SYMBOLIC, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, EXACT_DISCRETE, NEGATIVE_FALSIFIER | PASS | Exact L3 e=0; common-zero and positive/negative multiplier cases at equal k. | Attraction, stability or unequal-k synchrony. | K2a; test_parity_p01_p04.py (P2Tests) |
| P3 | Qualified triad symmetry | dynamics.step3; readouts.z_chiral | EXACT_SYMBOLIC, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, NEGATIVE_FALSIFIER | PASS | S3 jointly permutes state and k; real-parameter conjugation; U(1) globally at lambda=0, on the nonzero pre-sync stratum at lambda!=0; chirality transformation signs. | Fixed unequal-k S3, phase-on U(1) through zeros, general ring S3 or spatial meaning for chirality. | K2a; test_parity_p01_p04.py (P3Tests) |
| P4 | Cycle covering and nonlinear P lift | covering cycle_laplacian / pullback_matrix / isometric_pullback; dynamics.step_ring | EXACT_SYMBOLIC, EXACT_DISCRETE, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, NEGATIVE_FALSIFIER | PASS | Cycle multiplicities, residue pullback, Q isometry on its valid divisor domain, exact intertwining conditions, one-step nonlinear P lift and periodic ring wrap. | Nonlinear Q substitution, sector attraction or long-time ring/triad closeness; M=3 self-path is only a sanity check. | K2a; test_parity_p01_p04.py (P4Tests) |
| P5 | 388-row historical regression and schedule witness | api.run and public step/clock/EMA/readout operations | EXACT_DISCRETE, HISTORICAL_FIXTURE_TOLERANCE, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, SOFTWARE_CONTRACT | PASS | Preserved/reproduced record, row-zero semantics, new-Omega/clock/EMA sequencing, bitwise Runner/control agreement, independent C from saved/replayed Omega and accepted accounting comparisons. | Independent recurrence correctness or observer equations, spatial registration, research display/gate meaning or physical interpretation. | K2b; test_parity_p05_p06.py (P5Tests); golden_388 two-file packet |
| P6 | Transverse-axis falsification on two special subspaces | dynamics.step3; readouts.z_chiral | EXACT_SYMBOLIC, EXACT_DISCRETE, HIGH_PRECISION_REFERENCE, HISTORICAL_FIXTURE_TOLERANCE, NEGATIVE_FALSIFIER | PASS | Two invariant subspaces and special-seed C formulas, exact orthogonality where defined, eight-update fixture agreement, one-step angle and bounded floating preservation. | Universal preferred axis, attractor, physical selector or generic-seed behavior. | K2b; test_parity_p05_p06.py (P6Tests); transverse_axis_oracle.py |
| P7 | Paper-F finite-step analytic parity | dynamics.step3; readouts.z_chiral; source-oriented signed angle | EXACT_SYMBOLIC, HIGH_PRECISION_REFERENCE, ASYMPTOTIC_QUALIFICATION, ORACLE_VERSUS_PAPER_ONLY | PASS | Exact one-step harmonics/projections, finite-n coefficients through 8, independent full-map state/C/angle agreement, resolved signs and h=.02 reversal at update 4; fixed-n O(h^6) compatibility. | Infinity from eight steps, global basin, uniform-in-n remainder, six-axis physics or truncated-jet equality with finite-amplitude dynamics. | K2c; test_parity_p07_p08.py; paper_f_oracle.py |
| P8 | First-lambda full-composition one-step sensitivity | dynamics.step3 amplitude-then-phase composition; chirality-angle observable | EXACT_SYMBOLIC, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, ASYMPTOTIC_QUALIFICATION, ORACLE_VERSUS_PAPER_ONLY, NEGATIVE_FALSIFIER | PASS | Exact 99/2500 leading coefficient and finite-amplitude centered differences within independently precomputed envelopes; actual-observable rejection of isolated-phase 243/160. | Higher lambda orders, large lambda, arbitrary amplitude or float64 measurement of the limiting derivative. | K2c; test_parity_p07_p08.py; paper_f_oracle.py |
| P9 | Accepted Paper-E observers | z_manifold clock / staged / EMA / constructor-zero operations | EXACT_SYMBOLIC, EXACT_DISCRETE, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, HISTORICAL_FIXTURE_TOLERANCE, SOFTWARE_CONTRACT, NEGATIVE_FALSIFIER | PASS | Observer identities, clock behavior, staged/EMA operation order, literal .01, constructor-zero distinction and passivity with respect to Omega. | Physical measurement interpretation, historical literals as laws or strict subunit saturation in every binary64 result. | K2a; test_parity_p09_p10.py (P9Tests); paper_e_oracle.py |
| P10 | Passive accounting and diagnostics | z_diagnostics | EXACT_SYMBOLIC, EXACT_DISCRETE, HIGH_PRECISION_REFERENCE, BINARY64_TERM_SCALE, SOFTWARE_CONTRACT, NEGATIVE_FALSIFIER | PASS | Accounting identities, signed/unclamped residuals, potential/gradient formula, known overshoot, display/history qualifications and passive-only behavior. | Guaranteed Lyapunov descent, trajectory correctness, physical energy, control/feedback or history-independent displays. | K2a; test_parity_p09_p10.py (P10Tests); paper_e_oracle.py |
| P11 | Exact Paper-C geometry and Paper-D scaffold | geometry; reference_scaffold | EXACT_SYMBOLIC, EXACT_DISCRETE, NEGATIVE_FALSIFIER | PASS | Exact coordinates/topology/incidence, central section curve, accepted D3h actions, exact closed scaffold regions, role/frame/index distinctions and translation versus shrink. | Omega placement on shell, a chirality shell field, geometry/dynamics coupling or new physical meaning. | K2a; test_parity_p11.py; geometry_oracle.py |
| P12 | Frozen public software contract | api / _contract_types / _runner / _records / _geometry_records / _presets | SOFTWARE_CONTRACT, EXACT_DISCRETE, NEGATIVE_FALSIFIER | PASS | Explicit constructors, thin facade and single delegated recurrence; sequencing, detached immutable snapshots, observer passivity; Run/Geometry Records 1.0.0, inert round-trips, deterministic hashes, restart/resume, import boundaries, no research/quarantine activation, hidden defaults or geometry coupling. | New mathematics, support for quarantined modules, completed packaging/install/CI distribution engineering or UI. | K1 public-contract implementation and four P12 test files (72 tests), freshly rerun in final suite |

## Evidence-type matrix

| Type | Meaning | Gate use | Boundary |
| --- | --- | --- | --- |
| EXACT_SYMBOLIC | Polynomial/rational/geometry identities in exact arithmetic on the stated domains. | P1–P4, P6–P11 | No binary64 bitwise or global-dynamics conclusion. |
| EXACT_DISCRETE | Indices, topology, flags, branch/zero cases, literal bits and operation counts. | P1–P6, P9–P12 | Discrete agreement does not prove continuous equations. |
| HIGH_PRECISION_REFERENCE | Independent 80-digit reconstructions; P7/P8 also cross-checked at 100 digits. | P1–P10 numerical portions | Bounded numerical evidence, not a global theorem. |
| BINARY64_TERM_SCALE | Frozen bounds from independently reconstructed defining-term magnitudes. | P1–P5, P9–P10; P8 propagated error model | No arbitrary absolute floor, clamping or universal machine-safety claim. |
| HISTORICAL_FIXTURE_TOLERANCE | Explicit tolerance comparisons to preserved records. | P5/P6; retained P9 historical scalar fixtures | Regression evidence is not an independent recurrence/observer oracle. |
| ASYMPTOTIC_QUALIFICATION | Separate exact coefficients from finite-amplitude values; retain nonzero higher-order remainder. | P7/P8 | No jet equality, fixed ratio 16/64, uniform-in-n remainder or large-lambda claim. |
| SOFTWARE_CONTRACT | Delegation, immutability, scheduling, schema/codec, restart and import-boundary tests. | P12; schedule/passivity parts of P5/P9/P10 | No new mathematics or completed distribution engineering. |
| ORACLE_VERSUS_PAPER_ONLY | Exact limiting coefficient and limiting lambda derivative under accepted hypotheses. | P7/P8 | Neither limiting quantity is certified by a float64 trajectory. |
| NEGATIVE_FALSIFIER | Wrong-formula counterexamples, domain rejections, exact constraints and forbidden-side-effect guards. | Register below | Not an exhaustive mutation-testing proof. |

P7 uses the separately frozen absolute chirality and angular bounds. P8 includes a propagated binary64 model plus independently evaluated truncation; term-scale evidence is not a claim that every numerical comparison uses one identical formula. Comparison counts remain in their phase-specific classes in JSON and are not added into a theorem count.

## Independent-oracle architecture

| Oracle module | Imports | Project-local oracle dependency |
| --- | --- | --- |
| kernel_physics/tests/parity_oracles/__init__.py | none | none |
| kernel_physics/tests/parity_oracles/geometry_oracle.py | collections, sympy | none |
| kernel_physics/tests/parity_oracles/paper_a_oracle.py | mpmath, sympy | none |
| kernel_physics/tests/parity_oracles/paper_e_oracle.py | mpmath, sympy | none |
| kernel_physics/tests/parity_oracles/paper_f_oracle.py | mpmath, sympy | none |
| kernel_physics/tests/parity_oracles/transverse_axis_oracle.py | mpmath, sympy | none |

There are five mathematical oracle modules plus the import-free initializer. No oracle imports production kernel, research or the Paper-F verifier. No oracle-to-oracle dependency is used. P5 accounting deliberately reuses the unchanged K2a `kernel_physics.tests.parity_oracles.paper_e_oracle` from its test module; this is not an import inside the transverse-axis oracle. Provenance/support files are not executable oracles. Static and dynamic/file/import-boundary gates were freshly rerun.

```text
ORACLES_IMPORT_PRODUCTION_KERNEL = NO
ORACLES_IMPORT_RESEARCH = NO
ORACLES_IMPORT_PAPER_F_VERIFIER = NO
```

## Consolidated falsifier register

All entries below passed in the existing suite. Evidence kinds distinguish explicit wrong-formula counterexamples from domain rejections, exact constraints and forbidden-side-effect guards; this is not a claim of exhaustive mutation testing.

| Gate | Wrong implementation or claim | Witness | Result | Existing owner |
| --- | --- | --- | --- | --- |
| P1 | Ordinary np.angle at signed zero | Accepted Arg0 changes neighbor synchronization; ordinary-angle mutant is separated. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P1Tests.test_signed_zero_through_full_step |
| P1 | Omit a zero neighbor | Zero entries still supply their accepted Arg0 phase to neighbors. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P1Tests.test_signed_zero_through_full_step |
| P1 | Sequential phase update | In-place phase update disagrees with the simultaneous oracle. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P1Tests.test_sequential_falsifier |
| P2 | Unequal-k synchrony | Equal starting channels leave span(e) for unequal k. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P2Tests.test_unequal_k_falsifier |
| P3 | Fixed unequal-k permutation | Permuting only state fails; k must be permuted jointly. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P3Tests.test_all_six_permutations_and_fixed_k_negative |
| P3 | Unrestricted phase-on U(1) through zero | Pre-sync-zero counterexample violates the overbroad symmetry claim. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P3Tests.test_conjugation_u1_and_zero_counterexample |
| P4 | Invariant image implies intertwining | Exceptional (M,d)=(3,2) does not intertwine. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P4Tests.test_exact_matrices_and_domain |
| P4 | Nonlinear Q substitution | Normalized Q fails the nonlinear lifting identity obeyed by P. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P4Tests.test_q_substitution_and_ring_rejections |
| P4 | Invalid ring sizes | Sizes 4 and 5 raise ValueError. | PASS | kernel_physics/tests/test_parity_p01_p04.py::P4Tests.test_q_substitution_and_ring_rejections |
| P6 | Universal preferred axis / lost subspace constraints | Nonzero orthogonal A/B chirality axes persist; exact Cx=Cy and Cx=-Cy,Cz=+0 constraints; zero direction rejected. | PASS | kernel_physics/tests/test_parity_p05_p06.py::P6Tests.test_20_eight_updates_symmetry_angles_and_signed_zero |
| P8 | 243/160 as full-composition coefficient | Runtime FD is inside full-composition envelope and outside isolated-phase envelope for both signs/all deltas. | PASS | kernel_physics/tests/test_parity_p07_p08.py::RuntimeParityTests.test_p8_full_composition_centered_differences_and_wrong_coefficient |
| P9 | 1-.99 substituted for literal .01 | The innovation differs bitwise. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P9Tests.test_cubic_literal_01_and_current_memory |
| P9 | Constructor zero equals recomputed observation | Nonzero recomputation differs from marked stored zero. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P9Tests.test_constructor_zero_and_bitwise_passivity |
| P9/P10 | Observer or diagnostic feedback | Full Omega bytes match with and without all observers/diagnostics; forbidden advancement spies also belong to P12. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P9Tests.test_constructor_zero_and_bitwise_passivity |
| P10 | Residual clamping | Rounded nonzero Gram residual is retained. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P10Tests.test_gram_numeric_unclamped_and_gradient_budget |
| P10 | Guaranteed potential descent | Accepted finite step raises potential 6 to 168. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P10Tests.test_finite_step_overshoot |
| P10 | Repair inconsistent supplied records | Inconsistent supplied readouts retain nonzero residuals. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P10Tests.test_supplied_readout_accounting_including_inconsistency |
| P10 | Unresolved means exact zero; displays retain full state/history independence | Threshold flags, earlier-point movement on extended history and chirality information loss remain explicit. | PASS | kernel_physics/tests/test_parity_p09_p10.py::P10Tests.test_alignment_threshold_and_displays |
| P11 | Filled central triangle | Central section is three segments; centroid is not in their material curves. | PASS | kernel_physics/tests/test_parity_p11.py::P11Tests.test_c_section_curve_and_closed_domain |
| P11 | Open-cut replaces closed region | Closed halfplane/corner semantics differ from open-corner subtraction. | PASS | kernel_physics/tests/test_parity_p11.py::P11Tests.test_d_closed_halfplanes_support_and_corner_cells |
| P11 | Unlabelled D6 extends to roles/full frames | E/G roles and complete frames do not acquire the unlabelled polygon symmetry. | PASS | kernel_physics/tests/test_parity_p11.py::P11Tests.test_d_full_frames_regular_member_and_roles |
| P11 | Translation equals shrink/common rigid translation | Individual centre translations differ from fixed-centre shrink and a common rigid translation. | PASS | kernel_physics/tests/test_parity_p11.py::P11Tests.test_d_paper_c_comparison_translation_and_shrink |
| P12 | Quarantined optional modules activate implicitly | Fresh-process public import/execution leaves boundary_response, srg, operating_region and face_state unloaded. | PASS | kernel_physics/tests/test_import_boundaries.py::ImportBoundaryTests.test_clean_api_import_and_execution_do_not_load_option_b |
| P12 | Runner selects optional modules or geometry | Unsupported selections raise; quarantined names are not public exports. | PASS | kernel_physics/tests/test_import_boundaries.py::ImportBoundaryTests.test_runner_cannot_select_optional_modules_or_geometry |
| P12 | Passive reader advances state/clock/EMA | Patched forbidden advancement functions cannot be called by passive operations. | PASS | kernel_physics/tests/test_import_boundaries.py::ImportBoundaryTests.test_observers_and_all_passive_readers_never_advance |

## Historical fixture and O03

The minimal tracked golden packet is exactly `tests/fixtures/golden_388/TRAJECTORIES.csv` and `GOLDEN_388_RECEIPT.md`. No historical generator or larger research directory was promoted.

| Fixture | Rows | Columns | Bytes | SHA-256 |
| --- | --- | --- | --- | --- |
| P5 | 388 | 50 | 282427 | eeed672b1cb20321dfc85a2f4753c93d4fe1b9345a5cede4f5e12532537a4a38 |
| P6 | 18 | 32 | 10345 | fb2b2a71fd99c536dc7e490c6a2e201b2a0b22ee533820870dff5ee516c468dc |

```text
P5_EQUATION_ORACLE = NO
P5_HISTORICAL_REGRESSION_WITNESS = YES
P5_SCHEDULE_WITNESS = YES
P5_INDEPENDENT_CHIRALITY_ORACLE = YES
P5_COMPARISON_MODE = CROSS_ENVIRONMENT
P5_RECORDED_ENVIRONMENT_BITWISE = NOT_APPLICABLE
P5_MAX_CROSS_ENVIRONMENT_ERROR = 0.0
P5_RUNNER_CONTROL_BITWISE = PASS
```

The zero maximum refers to ordinary saved-versus-Runner comparisons. Independent C roundoff comparisons have their separate nonzero errors. Current Runner/control bitwise agreement is an orchestration check, not recorded-environment bitwise certification. Forty-one columns participate in parity/protocol checks. `threshold` and `polynomial_residual_allowance` remain HISTORICAL_CONVENTION; `display_M_x/y/z`, `map_lambda`, `map_delta0`, `gate_assignment`, and `harmonic_amplitude` remain EXCLUDED_RESEARCH. Both excluded classes retain their bytes and remain distinct.

## Paper-F exact constants and boundaries

| n | Exact kappa_n |
| --- | --- |
| 1 | -1/5760 |
| 2 | -347/7200000 |
| 3 | -59629/9000000000 |
| 4 | 71745997/11250000000000 |
| 5 | 145603166279/14062500000000000 |
| 6 | 203126174530303/17578125000000000000 |
| 7 | 32730981759886837/2746582031250000000000 |
| 8 | 660579363515112919919/54931640625000000000000000 |

```text
kappa_infinity = 13375/1107936648
KAPPA_INFINITY = ORACLE_VERSUS_PAPER_ONLY
KAPPA_INFINITY_RUNTIME_TESTED = NO

P8 one-step full-composition coefficient = 99/2500
P8 parameter-general coefficient = eps*a^2/4 + 47*a^4/32
243/160 = NOT the full-composition observable coefficient
limiting derivative = 34494041501/849664304944
LIMITING_DERIVATIVE = ORACLE_VERSUS_PAPER_ONLY
LIMITING_DERIVATIVE_RUNTIME_TESTED = NO
TOLERANCE_WIDENED = NO
ENVELOPE_FIXED_BEFORE_RUNTIME_INSPECTION = YES
```

P7 retains phi=±pi/12, h=.02/.01 and exactly eight updates. All 20 resolved signs pass; 12 cases are explicitly unresolved. For h=.02 the sign reverses at update 4. Full-map angles remain distinct from kappa_n*h^4*sin(6phi); normalized remainders are qualified under fixed-n O(h^6), without a ratio-16/64 rule or a uniform-in-n claim. P8 runtime scope remains ONE_STEP_FULL_COMPOSITION in the nonzero local chart. The limiting quantities retain Paper F's analytic/nonresonance hypotheses and are never inferred from float64 limits.

## Worst numerical margins

These are preserved worst-case phase measurements, not newly generated parameter experiments. Fresh final tests rerun their existing checks without changing bounds.

| Evidence | Absolute discrepancy | Allowed bound | Fraction used |
| --- | --- | --- | --- |
| K2a | 5.7740785351711684392796637634185787e-20 | 8.869302158527092700385488823206281e-19 | 0.065101835882543189081932253394215873 |
| P5 independent C | 2.6135784103582642379053253188667962e-17 | 4.0102381615389727642125952206817968e-15 | 0.0065172648233821477871297594023901448 |
| P6 angle | 6.1232339957367658861303296613750053e-17 | 1.0e-12 | 0.000061232339957367658861303296613750053 |
| P7 angle | 3.964411138584479236381405355893590419858e-16 | 5.684341886080801486968994140625e-14 | 0.006974265830653322057092787972539273916132 |
| P8 FD | 0.00000000005325767496455832438388155608639948196228 | 0.00000000006551296428248247598737651183244827745744 | 0.8129333720104450265080969613752843440938 |

K2a's largest fraction belongs to the P9 macro 8u residual fixture. P5's value is the independent saved-C comparison (row 95 C_z); P6's largest angle discrepancy is 6.123233995736766e-17 radians against 1e-12. P7 uses only 0.6974265831% of its frozen angular bound. P11 is exact.

| phi/pi | delta | Absolute FD discrepancy | Truncation allowance | Roundoff allowance | Angle uncertainty | Total envelope | Fraction used |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1/12 | .01 | 0.00000000005325767496455832438388155608639948196228 | 0.00000000005326480418948158649223458810316816939534 | 0.00000000001200798188091804805071488093054605876054 | 2.401782120828414444270427987340493015616e-13 | 0.00000000006551296428248247598737651183244827745744 | 0.8129333720104450265080969613752843440938 |
| 1/12 | .001 | 5.455654434334391951986517861769838116024e-13 | 5.285770170244372573128578612205524551125e-13 | 0.000000000111832616263933111537457394868585357585 | 0.000000000002401782089217280439066940758252890008236 | 0.0000000001147629753701748292338371934880588000483 | 0.004753845407664669578427376662523121780891 |
| 1/12 | .0001 | 2.419575175210787039188866361068499058171e-15 | 5.285366364008197445669600012896077709291e-15 | 0.000000001110637056533249572510633020564166036992 | 0.00000000002401782088901349324959965530150870716691 | 0.000000001134660162788627073957678345465687640237 | 0.000002132422776934597889032282247837409044385 |
| -1/12 | .01 | 0.00000000005325767496455832438388155608639948196228 | 0.00000000005326480418948158649223458810316816939534 | 0.00000000001200798188091804805071488093054605876054 | 2.401782120828414444270427987340493015616e-13 | 0.00000000006551296428248247598737651183244827745744 | 0.8129333720104450265080969613752843440938 |
| -1/12 | .001 | 5.455654434334391951986517861769838116024e-13 | 5.285770170244372573128578612205524551125e-13 | 0.000000000111832616263933111537457394868585357585 | 0.000000000002401782089217280439066940758252890008236 | 0.0000000001147629753701748292338371934880588000483 | 0.004753845407664669578427376662523121780891 |
| -1/12 | .0001 | 2.419575175210787039188866361068499058171e-15 | 5.285366364008197445669600012896077709291e-15 | 0.000000001110637056533249572510633020564166036992 | 0.00000000002401782088901349324959965530150870716691 | 0.000000001134660162788627073957678345465687640237 | 0.000002132422776934597889032282247837409044385 |

The smaller-delta fractions are retained: approximately 0.004753845407665 at 1e-3 and 0.000002132422777 at 1e-4, for both orientations. The maximum 0.812933372010445 occurs at 1e-2. Each total combines the precomputed full-map truncation bias, binary64 evaluation/input/FD arithmetic contributions, separate angle uncertainty and oracle precision guard. No envelope was chosen from runtime discrepancy or widened afterward.

```text
POST_HOC_TOLERANCE_WIDENING = NO
```

## OPEN-item disposition

| Item | Status | Disposition | Meaning |
| --- | --- | --- | --- |
| O01 | CLOSED | OPTION_B_QUARANTINE_V1 | boundary_response, srg and operating_region remain preserved OPTIONAL implementations, unsupported by the initial v1 facade. Their 30 local-only tests remain preserved/passing. This is not mathematical rejection. |
| O02 | OPEN_NONBLOCKING | HISTORICAL_RATIONALE_UNRESOLVED | Literal values and provenance of eps=.05, g=.2, the historical seed and theta_lock=.244 are known; original selection motives remain unresolved. Later Paper-F consequences do not close this item. It does not block kernel engineering. |
| O03 | CLOSED | MINIMAL_GOLDEN_PACKET_TRACKED | Only TRAJECTORIES.csv and GOLDEN_388_RECEIPT.md were published. No larger research directory was promoted. |

O01 quarantine is a support decision, not mathematical rejection. The preserved 30 local-only tests do not confer v1 support. O02 remains unresolved even though Paper F derives consequences from the known historical values. O03 is closed by the minimal portable tracked packet.

## Research-only exclusions and separate records

- spatial M/C/T registration
- gate/aperture mappings
- finite-patch interpretations
- spring/restoring laws
- EM / Riemann-Silberstein comparisons
- physical-field narratives
- six-axis physical selector
- Paper-F normal form as runtime
- Twisted Hex Crystal
- warp research
- Z feedback
- mechanical clocks
- historical alignment as dynamics

None of these was promoted into supported runtime mathematics. Accepted passive history/display helpers retain their named historical scope; they do not become physical fields, controls or dynamics.

```text
Omega state != shell coordinate
chirality != shell field
observer != geometry
KERNEL_RUN_RECORD separate from GEOMETRY_RECORD
```

No accepted spatial dictionary exists. K2 creates none. Geometry Records retain coupling="none".

## Fresh final validation and test census

```json
{
  "conda": "torment",
  "python": "3.11.15 | packaged by Anaconda, Inc. | (main, Mar 11 2026, 17:12:15) [MSC v.1942 64 bit (AMD64)]",
  "executable": "C:\\Users\\Notandi\\miniconda3\\envs\\torment\\python.exe",
  "platform": "Windows-10-10.0.26200-SP0",
  "numpy": "2.4.4",
  "sympy": "1.14.0",
  "mpmath": "1.3.0"
}
```

| Contribution | Tests |
| --- | --- |
| Pre-K1 tracked regressions | 177 |
| K1/P12 additions | 72 |
| K2a additions | 30 |
| K2b additions | 9 |
| K2c additions | 10 |
| Total tracked | 298 |
| Local-only, separate | 30 |

Historical Git-tree method counts are 177, 249, 279, 288 and 298. Actual unittest discovery at the authorized HEAD independently confirms 298. The four K1/P12 modules own 17 public-contract, 30 Runner/record, 17 Geometry Record and eight import-boundary tests.

The fresh isolated checkout is at `69046009a307fa8498bd7366c8214493eca7b833` and was clean before and after execution. The complete tracked suite was freshly executed; K2c's earlier PASS was not substituted.

```text
conda activate torment
python -B -m unittest discover -s kernel_physics/tests -t . -p "test_*.py" -v
```

**298 tracked tests PASS in 193.352 seconds.**

Afterward, in the original workspace:

```text
python -B -m unittest kernel_physics.tests.test_boundary_response kernel_physics.tests.test_srg kernel_physics.tests.test_operating_region kernel_physics.tests.test_boundary_pipeline -v
```

**30 local-only tests PASS in 0.715 seconds.** No O01 support-status change.

All 704 files present at starting HEAD and all four local-only test files retain their starting SHA-256 hashes. No existing file is modified. Unrelated untracked material is preserved. The only new publication paths are:

- `kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md`
- `kernel_physics/K2_PARITY_FINAL_CLOSEOUT.json`

## K3 handoff boundary

```text
ACCEPTED_KERNEL_PARITY = COMPLETE
PUBLIC_FACADE_PARITY = COMPLETE
PACKAGE_DISTRIBUTION_ENGINEERING = NOT_YET_K3_COMPLETE
PACKAGE_DISTRIBUTION_ENGINEERING_COMPLETE = NO
UI = NOT_STARTED
K3_READY_FOR_AUTHORIZATION = YES
```

K3 is not implemented or authorized by this closeout. A separate bounded GPT/Hilmir order is required for packaging, clean-clone/install validation, CI, supported package contract stabilization and geometry export distribution validation. The proposed starting HEAD is the commit introducing this closeout, reported literally after publication.

K2 closes accepted mathematics/public-facade parity within its explicit boundaries. It does not prove every research idea, support quarantined modules, couple geometry to dynamics, establish global six-axis physics, or complete packaging/UI.
