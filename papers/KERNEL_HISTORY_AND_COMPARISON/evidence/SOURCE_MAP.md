# Compact source map - repository publication v0.1

The author has accepted the manuscript and authorized this repository edition.
[Publication disposition](PUBLICATION_DISPOSITION_v0.1.md) supersedes the prior
permission-pending labels for the included manuscript, excerpts and figures.
Underlying local H/P3 packets remain unavailable from this bundle. The scientific
source mapping below is unchanged.

All source identities below are fixed by `authority_identities.json` (reports,
repository editions, controlling work order and H5 amendment) or
`source_identities.json` (P3 data and compared wheel identities). Those files
record SHA-256 identities, not redistribution permission or authorship proof.
The manuscript uses readable short citations; this map supplies exact locators.

## Authority register

Reports root on the review machine: `C:/Users/Notandi/.codex/reports`.
Repository root: `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics`.
These are convenience locators; hashes bind content. None is opened or executed
at paper runtime. All nine reports are **v0.1**.

| Label | Exact filename relative to reports root |
|:--|:--|
| H0 | `TRIOCTAGON_H0_HISTORICAL_CURRENT_GEOMETRY_EQUIVALENCE_AUDIT_v0.1.md` |
| H1 | `TRIOCTAGON_H1_HISTORICAL_3D_PROVENANCE_RUNTIME_BINDING_AUDIT_v0.1.md` |
| H2 | `TRIOCTAGON_H2_HISTORICAL_CURRENT_STATE_DYNAMICS_EQUIVALENCE_AUDIT_v0.1.md` |
| H3 | `TRIOCTAGON_H3_HARMONIC_THREE_DERIVATION_PROVENANCE_AUDIT_v0.1.md` |
| H4 | `TRIOCTAGON_H4_HISTORICAL_COMPATIBILITY_CONTRACT_FREEZE_v0.1.md` |
| H5 | `TRIOCTAGON_H5_HISTORICAL_PROTOCOL_SCHEMA_ADMISSION_FREEZE_v0.1.md` |
| H6A | `TRIOCTAGON_H6A_HISTORICAL_PROTOCOL_SCHEMA_IMPLEMENTATION_v0.1.md` |
| H6B | `TRIOCTAGON_H6B_INDEPENDENT_HISTORICAL_KERNEL_IMPLEMENTATION_v0.1.md` |
| P3 | `TRIOCTAGON_P3_HISTORICAL_CURRENT_KERNEL_COMPARISON_ATLAS_v0.1.md` |

H5's controlling amendment is
`h5_protocol_freeze_20261001/H5_INDEPENDENT_HISTORICAL_KERNEL_AMENDMENT.md`.
H0-H3 are dated 30 September; H4 completed 1 October; H5-H6B and P3 are dated
1 October 2026. The work order names these as the accepted basis for the new paper;
original reports retain their own prepared-for-review language. This task supplies
no retroactive acceptance declaration.

| Label | Repository publication edition / exact manuscript path |
|:--|:--|
| A | Publication v1.0, scientific source v0.5.1; `papers/PAPER_A/publication/paper_A_publication.md` |
| B | v0.1.2; `papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md` |
| C | Publication v1.0.1, scientific source v0.3.1; `papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md` |
| D | v0.1.1; `papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md` |
| E | v0.1.1; `papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md` |
| F | Publication v0.2; `papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md` |

The publication index and licensing boundary are `README.md` and
`LICENSE_SCOPE.md`. Domain boundaries are `scientific_domains/README.md` and
`scientific_domains/TORMENT_HISTORICAL.md`. The authority chain and implementation
mapping are `historical_kernel/README.md`, `SPECIFICATION.md`, `CONFORMANCE.md`
and `tools/conformance_map.json`. Current support qualifications are in
`kernel_physics/README.md`. All are bound at repository baseline
`9c9e579e97aac0cdc7524b0d05430d0d76e39ce4`.

## Equations, claims and results

“Algebraic” denotes an accepted mathematical argument; “finite” denotes measured
software/numerical evidence; “documentary” denotes source or history evidence;
“model choice” denotes an adopted convention; “unresolved” is not a proved absence.

| Paper item | Exact support and classification |
|:--|:--|
| Section 1; Figure 1: three identities, independent mathematics | **Documentary / implementation policy.** H2 §2; H5 §1 and amendment; H6B §§5-17. H6B implementation commit `31109632fb1bb179a0f35f367f26f7472865a7b2`. Current and Historical have distinct scientific implementations; arrows are lineage, not imports. |
| Section 1.1: chronology | **Documentary.** H3 §2 provenance ledger (November/December 2025 and March 2026); H1 §14 version lineage (August viewer); H0 §16 and H1 §15 (September C01 ancestor); H0-H6B report dates. Earliest design conversation remains **unresolved**, H3 §17. |
| Section 2: old geometry exists, C01 production coupling not demonstrated | **Documentary / unresolved binding.** H0 §§3-6,16-20; H1 §§5-11,14-16. H1 references its `source_manifest.json`, `production_binding_hits.json` and `copy_lineage.json`; this task uses the audited primary report and its explicit path evidence, not a new geometry census. |
| Equation (1): production corridor and consumers | **Documentary formula / traced call path.** H1 §7.9 and §§9-10; H2 §§15-16. This is not a shell-coordinate input to the unforced recurrence and not a new deployed-runtime test. |
| Section 2: C01 exact constants and topology | **Algebraic / construction.** H0 §§6-15; Paper C §§2-5,9-10. Width 1, side sqrt(2)-1, fold pi/3, V/E/F=18/21/3, two nine-edge rims. Edge-one ancestor scale is sqrt(2)-1; not a production-torus calibration. Paper D §§1-3 gives a separate scaffold. |
| Equations (2)-(4); Section 3 proof and notation | **Algebraic, with declared conventions.** H2 §§4-6,9,11,18; H4 §§4,6; H5 §7; Historical conformance IDs `triad` and `phase`: `dynamics.step`, `phase.synchronize`, `constants.K`. Current `dynamics.step3`, `dynamics.phase_sync` and `dynamics.arg0`; Paper A §§1,6.1. Fixed unforced triad, simultaneous original values, canonical exact-zero phase. |
| Section 3.1: older signed-zero discrepancy | **Finite boundary witness / model choice.** H2 §§9,20; H4 §4; H6B §17. A helper-level counterexample does not establish a full-step trajectory witness. The reference adopts a qualified convention rather than silently changing the archive. |
| Section 3.1: ring extension | **Algebraic.** Paper A abstract and §§1,6; H2 §5; P3 §17. Three-periodic lift and matched coefficients; not equivalence of the full ring state space. |
| Section 4 profile table; equation (5) | **Documentary constants / model choice.** H2 §7; H4 §5; H5 §7; P3 §§6-7; `inputs.json` -> `profiles` exact hex tokens. Historical profile identifiers and exact decimal coefficients are retained. Current L01 is a selected explicit scenario. |
| Section 4: harmonic rationale; equation (6) | **Documentary / conditional algebraic.** H3 §§2,4-8,16-17. Independent 120-degree phase identification plus lowest pure nonconstant harmonic is the extra premise; potential differentiation gives factor 3. Not symmetry of the complete amplitude map, not a physical derivation. |
| Equations (7)-(9): K and H scalars/EMA | **Algebraic / frozen numerical convention.** H2 §12; H4 §§8-9; H5 §§9-10; Paper E observer definitions; conformance IDs `staged`, `ema`, `clock`: `staged_z.observe_staged`, `ema_z.cubic_j`, `advance_ema`, `observe_ema`, `clock.angle`. Literal coefficients and left-associated cubic product; inspection is pure. |
| Equations (10)-(11): C, M and T | **Algebraic / interpretation boundary.** H2 §13; H4 §10; Paper B §§6-8; conformance ID `chirality`: `chirality.raw_chirality`. Current `readouts.z_chiral`; channel-pair components are not automatically spatial axes. |
| Section 5.1: schedule, constructor and history | **Behavioral contract plus finite comparison.** H4 §7; H5 §8; H6B §10; P3 §15; `history_comparison.json` -> 16 `mapped_rows_and_terminal_exact` results. Conformance IDs `history`, `clock`. N=0 is explicitly tested. Repeated clock addition and multiplication discrepancy recorded in P3 §18. |
| Section 6: population and exactness | **Finite numerical.** P3 §§2-5,8-9,15; `inputs.json`, `one_gate.json`, `one_comparison.json` -> `control`; `trajectory_comparison.json` -> `controls`, `matched_updates`, `matched_samples`, `counts`, `unexpected`. Hex-token parity and refusal availability, not full serialized identity. |
| Section 6: independent environments | **Finite software-binding evidence.** P3 §2; `bindings.json`, `historical_trajectory_closure.json`, `current_trajectory_closure.json`: Python 3.11.15/NumPy 2.4.4, module identities and denied roots. This is not protected execution attestation. Wheel digests are copied only as identities in `source_identities.json`. |
| Section 6: earlier H6B fixture population | **Finite, separately labeled.** H6B §§15-17 and Historical `CONFORMANCE.md`; P3 `validation.json` -> `H2_one_exact`=39, `H2_multistep_exact`=640, `H6B_state_clock_memory_observers_exact`=640. Original denominators 91/1280 belong to H2, not P3. |
| Equation (12); first difference examples | **Algebraic cause plus finite witnesses.** P3 §8; `one_comparison.json`; `one_gate.json`. Same input and all coefficients other than k fixed; e1 delay and zero exception retained. |
| Equation (13); Figure 2; terminal table | **Finite illustrative trajectory.** P3 §9; `inputs.json` -> `vectors.gate_seed`; seven indexed `gate_seed` raw trajectories in `current_trajectories` / `historical_trajectories`. Figure 2 shows n=0..128 from N=1024; table gives N=1024. The full 25-state per-profile population is stated, not hidden by the illustration. |
| Equation (14); Figure 3; terminal distances | **Defined diagnostic / finite evidence.** P3 §3 metric definition; `metrics/HISTORICAL_*__gate_seed.json` -> `difference.l2`, `difference.aligned_l2`; `trajectory_summary.json`; `insights.json`. Left has log x only and excludes n=0; no exact zero is replaced by a positive floor. Right reads saved memory values for n=0..1024. |
| Section 7: transients, sector neighbors and finite horizon | **Finite, not an attractor theorem.** P3 §§9-10; `trajectory_summary.json` -> `historical_settling`; `insights.json` isolated/sector results. Settling means first 32 consecutive increments at threshold 1e-12(1+norm). No universal transient ordering or capacity claim. |
| Section 7.1: global-phase-sensitive EMA; decay | **Finite witness plus algebraic observer result.** P3 §§12-14; `insights.json`; H2 §§12-14. EMA homogeneous difference .99^n assumes identical future drive. The i-rotated gate and initial m=0 are not evidence of different implementations. |
| Equation (15): probability chart | **Documentary / algebraic / numerical convention.** H2 §14; H4 §11; H5 §11; H6B §13; conformance ID `chart`: `probability_chart.probability_chart`; P3 §14. No current numeric counterpart; legacy underflow branch retained. |
| Section 8 capability table and support qualifications | **Documentary API scope.** Historical `SPECIFICATION.md`; Current README supported-v1 and unsupported-internals sections; P3 §§16-19. Face-state legacy opt-in and Option B internals are not promoted to supported facade features. |
| Sections 9-10: limits, permissions and reproduction | **Scope / unresolved.** H1 §16; H3 §17; P3 §§20-23; root `LICENSE_SCOPE.md`; user's work order §§2,5-7. No physical validation, whole-production equivalence or AI-memory winner; repository publication author-approved, with evidence-access limitations retained. |

## Minimal inert inputs and what can be rebuilt

`figure_table_data.json` is a local-review **derived excerpt**, not the complete
P3 experiment corpus. It stores:

- gate_seed and all four configurations' exact coefficient tokens;
- magnitudes for updates 0..128 and terminal 1024;
- saved memory for all 1025 samples of the four configurations;
- saved raw/aligned distance from L01 for each Historical profile at those samples;
- relevant terminal and settling summaries and comparison-population counts.

`source/prepare_evidence.py` reads 23 named inert P3 files, checks all Mode A
summary parity/status records, all history mappings and seven selected raw-file
hashes, and directly rechecks selected raw state/prephase/observer/memory equality.
It neither executes data as code nor imports scientific kernels. No accepted
result is regenerated. `source/make_figures.py` only renders the checked excerpt.
Figure 1 is a documentary synthesis supported by the first two map rows.

**Rebuilding these figures/PDF:** the excerpt and included authoring sources suffice
with the existing toolchain. **Rechecking extraction:** the 23 specific external
files and their indexes listed in `source_identities.json` are needed under the
reviewer's P3 root. **Independent full numerical reproduction:** requires the
complete accepted P3 scripts, input population, pinned wheels/environment and
H6B/H2 authority evidence, which are not shipped or rerun here. A local JSON
projection is not a substitute for access to that verification package.

No original report, complete raw trajectory corpus, wheel or recovery archive is
copied into this paper. Exact source filenames/hashes and derived local-review
data do not carry a blanket reuse license. Author approval for repository
publication is recorded in PUBLICATION_DISPOSITION_v0.1.md. REVIEW_NOTES preserves
the earlier permission-pending stage and missing handoff; the evidence-access
limitation remains in force.
