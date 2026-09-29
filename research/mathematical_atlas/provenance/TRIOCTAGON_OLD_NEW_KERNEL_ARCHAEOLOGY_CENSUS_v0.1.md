# TRI-OCTAGON OLD/NEW KERNEL ARCHAEOLOGY CENSUS v0.1

Date: 28 September 2026. Mode: READ_ONLY source archaeology. Author: Codex for Hilmir.

This report is the only output written by this task and is outside all repositories. It is a static source census, not an execution certificate, scientific acceptance, physical interpretation, or restoration proposal. No historical program, UI, test suite, or production module was imported or run. Python in the `torment` Conda environment was used with bytecode disabled to read and parse source. No repository, production file, commit, or remote was changed.

## 1. Authority, method, and main findings

| Source | Inspected local authority | Identity / scope |
|---|---|---|
| A: current science | `C:/TORMENT/TRIOCTAGON_new/trioctagon-physics` | HEAD `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`, the requested frozen baseline |
| B: historical kernel | `C:/TORMENT/TRIOCTAGON_new/kernel_TO` | Entire 401-file tree inventoried; all 89 Python modules and 3 supporting source/doc files read |
| C: historical apparatus | Same old root | All four requested UI files are directly in this directory, not in a separate UI tree |
| D: production kernel | `C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel` | All 21 Python modules read; enclosing Git HEAD `a06edcc5c9df5d3b56405085d9f2942b768dc203` |

The production repository reference supplied by the work order is `https://github.com/pzychozen/TORMENT/tree/main/torment_service/kernel`. This census uses its **local authority**; it does not assert that remote `main` has the same contents. No fetch was needed. Current and production tracked worktrees were clean at the initial inspection. Both repositories also contain pre-existing untracked research/output material; “tracked clean” does not mean those directories are empty or absent.

Hereafter `OLD/file.py:L`, `CUR/file.py:L`, and `TOR/file.py:L` mean the respective roots above; current kernel paths include `kernel_physics/`. These are source line locators, not inferred historical version dates. Appendix A gives clickable absolute paths for every old source file. All formulas below are recovered mathematical descriptions of inspected code, with floating-point qualifications; they are not extra laws assigned to names.

The old tree contains much more than the triad recurrence: a separate RSB engine, several incompatible quantities called `v_rec`, probability-coordinate geometry, event gates and external seed worlds, trajectory persistence, empirical stability and chirality laboratories, and four materially different viewers. Eighteen production files are byte-identical to old files, with two further close homologues. This is strong code-sharing evidence, but cannot date copying or establish its direction.

Several visible historical constructions already have a **paper** counterpart without a current public UI counterpart. Paper E explicitly distinguishes the scalar-history torus, per-channel Omega torus, direct Z trajectory, percentile overlay, and full versus directional diagnostics. Thus “absent from the UI” must not be reported as “missing from Papers A–F.” Conversely, no inspected old formula establishes a physical map from these displays to the C01 shell or D03 gap cells.

The old sources are not uniformly runnable as an unchanged application. Static disconnections are recorded in section 8. They are evidence about the snapshot, not grounds to delete or discredit an entire mathematical family. The report does not use successful syntax parsing as evidence of successful imports, finite runs, GUI launches, or passed tests.

### Coverage and counting rules

* Old inventory: 401 files = 89 `.py`, 2 `.md`, 1 `.ps1`, 33 `.pyc`, 76 `.csv`, 135 `.png`, 35 `.npz`, 4 `.txt`, 11 `.json`, 15 `.pdf`.
* “Old kernel files inspected” in the closing summary counts the 92 significant source/support files. The 4 UIs are a subset, not 4 additional files. All 401 paths, sizes and SHA-256 identities are inventoried in Appendix C. Saved images, PDFs, binary arrays and bytecode were inventoried rather than individually rendered or scientifically revalidated.
* Production inventory: 64 files = 21 Python sources and 43 bytecode files. The closing source count is 21, not 64.
* Current kernel reference count: all 19 top-level Python modules. Current UI and manuscript references are additional supporting evidence, not included in that count.
* Mathematical/algorithmic systems are the explicit M01–M54 entries in section 4. Each gets exactly one primary A–G archaeological category, including persistence/provenance algorithms where they affect interpretation. Secondary relationships do not increase counts.
* Geometric objects are G01–G19; visualization families are V01–V20. Repeated displays in multiple UIs count once in these family counts. A geometric plot can appear in both inventories; the counts are not additive.

All old Python sources were parsed; `analyze_threebody_probe.py` required a CP1252 decoding fallback because its original bytes are not valid UTF-8. Its encoding was not repaired. Imports, definitions, defaults, state fields, output sites, reverse imports and mathematical owners were inspected. No applicable `AGENTS.md` was found in the inspected authority paths.

## 2. Present scientific correspondence

| Present reference | What it establishes here | What it does not establish |
|---|---|---|
| [Paper A](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/publication/paper_A_publication.md) | Three-state nonlinear map; harmonic-3 synchronization; exact cycle-covering reduction and qualified transverse stability | Old RSB engine identity, physical ring placement, general stable behavior of arbitrary parameters |
| [Paper B v0.1.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md) | Raw chirality as transported signed areas with specified face frames; channel/spatial distinction | Arbitrary old Z-vector as a physical ambient field |
| [Paper C v1.0.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md) | Exact folded three-octagon surface with boundary, topology and metrics | Any of the historical tori being that surface; the shell is an annulus, not a torus |
| [Paper D v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md) | Aligned alternating hexagon, `g_gap = sqrt(3)*p - s/2`, conditional C/D comparison, open display-to-gap attachment | Equality of `g_gap` with recurrence coupling `g`, or physical aperture/force rules |
| [Paper E v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md) | Staged/EMA scalar variants, M/C/T readouts, geometry identities, four display maps, diagnostic distinctions, bounded historical replay | Universal physical velocity, energy, field stress, or direct placement in gap cells |
| [Paper F v0.2](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md) | Local analytic structure and coefficient/normal-form parity of the specified recurrence | A new public runtime engine, physical CP/EM interpretation, shell forces, or six physical attracting states |

The 19 current modules referenced are: `__init__.py`, `api.py`, `dynamics.py`, `covering.py`, `readouts.py`, `geometry.py`, `reference_scaffold.py`, `z_manifold.py`, `z_diagnostics.py`, `_contract_types.py`, `_geometry_records.py`, `_presets.py`, `_records.py`, `_response_numeric.py`, `_runner.py`, `boundary_response.py`, `face_state.py`, `operating_region.py`, `srg.py`.

The public facade exposes explicit triad/ring operations, passive readouts and observer state, and versioned records. `dynamics.py` contains the deterministic unforced recurrence; the old integrated wall-clock, random forcing, cycle labels, and external seed world are not silently part of it. `z_manifold.py` separates clock/observer state from Omega. Its EMA variant is reconstructed from its documented historical source; the unused `z_mem` field in the inspected OLD `ModelState` is not an implemented EMA update.

`geometry.py` and `reference_scaffold.py` own exact C01/D03 constructions. `_geometry_records.py:178–211` accepts only definition IDs `C01` and `D03`. The existing GeometryRecord is **not a generic carrier for arbitrary historical meshes, curves, fields or trajectories**. Current detached coordinate/history results can represent supported direct-Z, cylinder and scalar-torus displays, without turning them into GeometryRecords.

`boundary_response`, `face_state`, `operating_region`, and `srg` are shipped internal material, not additional supported public UI operations. In particular current `srg.py`'s fixed six-vector initialization is not the old `RSBModel`'s C×M×H iterative dynamics. A shared spectral vocabulary is not a correspondence proof.

The current native UI (`apps/scientific_ui/src/trioctagon_ui/app.py`) has Dynamics, Observers & Diagnostics, Geometry, and Records & Reproducibility workspaces. It supports explicit triad/ring editors, recorded readouts, passive scratchpad actions, direct/cylinder/history-torus displays, independent C01/D03 requests, datasets, finite sweeps, comparisons and provenance exports. `plots.py:36–90` supplies Omega real/imaginary histories, complex planes, and raw chirality. Raw chirality is the three-component quadratic C, **not** the historical scalar cubic J. A dedicated old-style cubic-J/RSB/CP/identity dashboard is not found in this current surface. Recorded-history playback is present, with a cached whole-history torus normalization; this must not be confused with rerunning the model at every frame.

## 3. Production lineage and actual use

`EXACT_CODE_LINEAGE` below means equal bytes or explicit shared code bodies, not proof of ancestral direction. `MATHEMATICAL_LINEAGE` means an identifiable common formula despite changed representation. `SIMILAR_CONCEPT_ONLY` means related purpose without established shared implementation/formula. `NO_RELATION_ESTABLISHED` is a bounded negative finding, not a universal historical denial.

| Production module | Relationship to OLD | Evidence and scope |
|---|---|---|
| `__init__.py` | EXACT_CODE_LINEAGE | Byte-identical package marker; no mathematical content |
| `constants_selector.py` | EXACT_CODE_LINEAGE | Byte-identical coefficient selectors and constants |
| `cp_windows.py` | EXACT_CODE_LINEAGE | Same cyclic sector mask |
| `definitions.py` | EXACT_CODE_LINEAGE | Same cubic J, v_rec variants, RSB summaries/classification |
| `diagnostics.py` | EXACT_CODE_LINEAGE | Same experiment/analysis helpers, including source import limitations |
| `phase_triad_sync.py` | EXACT_CODE_LINEAGE | Same phase-only harmonic-3 update and coherence |
| `physics_sampler.py` | EXACT_CODE_LINEAGE | Same intensity probabilities, phases and J sampling |
| `physics_sampler2.py` | EXACT_CODE_LINEAGE | Same CP-conditioned summaries and selection windows |
| `rsb_model.py` | EXACT_CODE_LINEAGE | Same separate RSB engine |
| `su3_basis.py` | EXACT_CODE_LINEAGE | Same real orthonormal probability-coordinate projection |
| `tangent_corridor_analysis.py` | EXACT_CODE_LINEAGE | Same display-tangent comparison and clustering |
| `identity_rules.py` | EXACT_CODE_LINEAGE | Same threshold stages and modulo-nine identity labels |
| `latent_foreclosure.py` | EXACT_CODE_LINEAGE | Same clone/perturb/advance option-volume probe |
| `seed_emission.py` | EXACT_CODE_LINEAGE | Same phase gate and copied payload |
| `seed_entities.py` | EXACT_CODE_LINEAGE | Same external particle-like state and drag/drift motion |
| `seed_trajectory_analysis.py` | EXACT_CODE_LINEAGE | Same radial escape/return/grazing heuristic |
| `analyze_seed_trajectories.py` | EXACT_CODE_LINEAGE | Same saved-CSV aggregation |
| `c.py` | EXACT_CODE_LINEAGE | Same short saved-CSV finite-fraction inspection |
| `model_core.py` | EXACT_CODE_LINEAGE for shared bodies; MATHEMATICAL_LINEAGE for whole-file comparison | OLD 343 versus TOR 333 lines. Same recurrence, update/readout order and history schedule. OLD adds an unused `z_mem` state field and float-coerces the lock override; comments/formatting differ. Not byte-identical. |
| `trajectory_logging.py` | EXACT_CODE_LINEAGE for implementation | Same 90-line logger, with OLD `.pathing` versus TOR `..pathing` import. Do not claim equal bytes. |
| `trajectory_v2.py` | SIMILAR_CONCEPT_ONLY relative to OLD logger | Production-only 832-line versioned persistence system. No matching OLD module found; shared persistence purpose alone does not prove copying. |

Production `trajectory_v2.py` separates logical frame identity `(epoch, frame_seq)` from diagnostic native `step`, which can repeat. It defines genesis records, dynamic records, frames, chunk manifests, readers, writer results and verification reports; writes chunk/genesis/manifest evidence and verifies ordering, hashes and containment including live tails. It is non-authoritative persistence, not an Omega law. There is no evidence that its numeric fields constitute a new physical trajectory integrator.

Read-only caller tracing outside the production kernel found actual integration in `torment_service/memory_kernel.py` (model imports at 15, construction around 70, overridden `model.step` around 246, coherence around 261, probability projection around 313); `cognitive_core.py:10` imports identity mapping. `memory_graph.py` imports SeedWorld, trajectory classification and both logger generations, instantiates the world around 252 and loggers around 279, spawns around 822 and steps/classifies around 985–1022. Native substrate runtime modules also import seed/trajectory services. `checkpoint.py` reconstructs model state; `sqlite_index.py` and `app.py` read V2 persistence.

These are source call-site observations, not production telemetry. For RSB, CP windows, physics samplers, tangent analysis and diagnostic scripts, presence in the production directory is proven but active external execution was not established. Core optional foreclosure is conditional on extra configuration; reachability does not prove a currently enabled production feature. No historical UI is imported by these production call sites. The production-sensitive tree was never executed or modified.

## 4. Equation / algorithm registry and preliminary correspondence

Category meanings follow the work order: A CURRENT_SCIENCE; B VALID_MATH_NOT_PORTED; C USEFUL_VISUALIZATION; D EXPERIMENTAL; E TORMENT_SPECIFIC; F SUPERSEDED_OR_DUPLICATE; G MEANING_UNKNOWN. B means an apparently coherent recoverable calculation, not a new proof or scientific validation. A can mean a formalized historical map in a paper even where no current API exists. D can have a documented paper discussion without its experimental interpretation being accepted. F does not authorize deletion and does not imply bitwise equality between variants.

UI abbreviations: L=`toy_ui_live.py`, U=`toy_ui.py`, B=`toy_lab.py`, T=`toy_3d_triocta.py`; “scripts” means no direct widget in those four. Production “present” means source present; only explicitly stated caller evidence establishes integration. Registry entries distinguish the state they evolve from passive history calculations.

### M01 — Complex triad recurrence [A]

**Source:** `OLD/model_core.py:133`, `ModelParams`, `ModelState`, `TriOctaPhaseLockModel`. For `L3=[[-2,1,1],[1,-2,1],[1,1,-2]]`, `Y = Ω + ε Ω⊙(k−|Ω|²) + δ + g L3 Ω`, followed by M02 and optional M05 noise. Inputs complex Ω∈C³, real ε/g/k, forcing δ; output next Ω. **Stateful.** Defaults ε=.05, g=.2, selected k, δ=0. `dt` does not multiply this map. UI L/U/B/T; production shared core actively wrapped by memory_kernel. Current `dynamics.py` deterministic δ=0/noise=0 analogue; Papers A/F specify that restricted map. No old generic M-ring Omega engine was found; current covering extension is not the RSB engine.

### M02 — Harmonic-three phase synchronization and coherence [A]

**Source:** `phase_triad_sync.py:5,30`. Write Y_i=r_i exp(iφ_i), simultaneously set `φ'_i=φ_i+λ Σ_j sin(3(φ_j−φ_i))`, preserve r_i. `S=(1/3)Σ exp(3iφ_i)` gives coherence magnitude and collective argument. Inputs complex triad and λ (core default .001); outputs synchronized triad/S. Update is **stateful** through M01, coherence **passive**. All four UIs indirectly; production exact source and direct coherence caller. Current dynamics/Paper A phase operator; Paper F phase analysis. Historical `np.angle` zero conventions must not be silently equated to every current explicit zero policy.

### M03 — Explicit sector clock and history schedule [A]

**Source:** `model_core.py:164,246,268`. `q←(q+phi_step) mod N`, `t←t+dt`, `step←step+1`; defaults N=12, phi_step=1. `run` stores the current row before each update; n rows are followed by an advanced final state not stored in those n rows. Constructor readouts initially zero unless recomputed. Inputs clock/state/dt; output clock/history metadata and subsequent scalar readout. **Stateful**, separate from Ω equation. All UIs; production core. Current explicit clock and observer initialization/runner contracts, Paper E. The historical name `d24_steps` does not itself prove a 24-element physical symmetry.

### M04 — Coefficient generators [B]

**Source:** `constants_selector.py:34–103`. `θ(a,b)=|a/b−b/a|/sqrt(ab)`. Scaled triplet uses pairs `(sqrt(3),φ),(π,e),(φ,e)` divided by the first value; soft triplet is `α sqrt(θ_i/θ_1)`; hand-tuned variant is (.7,1,1.3). Inputs selector mode/α/constants; output k. **Passive configuration**. L/U use scaled; B/T use soft; scripts expose more modes. Exact production file and core default. Current explicit k/presets and Paper F's declared coefficient context overlap, but not a public general constants-selection apparatus. The `theta_value` scale-invariance doc claim is false as written: simultaneous positive scaling a,b by s divides θ by s. Triplet normalization can cancel a common scale. Formula recoverable; motivation M51 remains unknown.

### M05 — Additive complex forcing and dynamical noise [D]

**Source:** `model_core.py:133`. Deterministic δ enters before synchronization; optional after-sync noise is `σ(ξ+iη)` with independent standard-normal components from global NumPy random state. Inputs δ, σ and RNG state; output forced/noisy Ω. **Stateful**. No exposed dynamical-noise widget in the four UIs (their slider is M47). Exact/shared production core; active nonzero use not established. Current public deterministic map excludes this path; Paper E separates forcing/noise from its bounded zero-forcing replay. No physical stochastic process or calibrated units recovered.

### M06 — Staged scalar and macro/total readout [A]

**Source:** `model_core.py:169`. `κ=||Ω||`, `ρ=κ/(1+κ)`, `θ=2πq/N`; `z=λ_vp ρ cos(3(θ−θ_lock)) exp(−γt)`; `M=z(cosθ,sinθ,1)`, `T=αM+βC`. Defaults λ_vp=.618, γ=.577, lock=.244, α=1, β=.5. Inputs Ω, clock/time, readout coefficients; outputs scalar z, M/T and alias Z_vec. **Passive in Ω**, stored within old state. All four UIs; production model (lock override supported). Current staged observer/z_manifold, Paper E. No update consumes `z_mem` here.

### M07 — Raw quadratic channel chirality [A]

**Source:** `model_core.py:169`, Z_chiral. `C=(Im(conj Ω₂ Ω₃), Im(conj Ω₃ Ω₁), Im(conj Ω₁ Ω₂))=Re Ω × Im Ω`. Inputs raw triad; output real 3-vector; **passive**, no normalization. U/T direct vector selections, L/B indirectly through stored histories; production core. Current `readouts.z_chiral`; Papers B/E. Channel pseudovector is not automatically an ambient magnetic/axial field.

### M08 — Cubic J and relative phases [A]

**Source:** `definitions.py:22,30`; `physics_sampler.py:21,47`. `J=Im(Ω₁ conj Ω₂ Ω₃)`; pair phases are arguments of channel/conjugate products. History helper may prefer a supplied `J_eff` history over recomputation. Inputs Ω or stored J; outputs J and phase series; **passive**. All four J panels and Tri→RSB conditioners. Exact production source; production-directory presence of sampler does not establish active physical use. Paper E explicitly treats cubic J, and current EMA internals use its own documented cubic term; no dedicated public old-style J chart. J is not invariant under arbitrary common U(1) phase, unlike M07, and the historical `cp_like_invariant` name proves no physical CP invariant.

### M09 — Channel intensity probabilities [B]

**Source:** `physics_sampler.py:8`, `su3_basis.py:12`. Sampler `P_i=|Ω_i|²/(Σ|Ω|²+10⁻¹²)`; basis helper divides by the exact sum when positive and leaves zero weights at zero state. Inputs triad; outputs three weights; **passive**. Sampler histories feed U/L/etc. helpers, probability plots via scripts. Exact production copies; basis projection has actual memory integration. Current raw intensity/readout quantities are related but do not expose these two historical normalized variants. Papers B/E distinguish raw state from normalization; neither tolerance convention is silently interchangeable with raw chirality.

### M10 — “SU(3)” probability-coordinate projection [B]

**Source:** `su3_basis.py:23`. `u=(1,1,1)/sqrt3`, `x=(1,−1,0)/sqrt2`, `y=(1,1,−2)/sqrt6`; return `(w·u,w·x,w·y)`. For normalized nonzero weights, c_u is fixed and the image is a triangle in a plane. Inputs M09 weights; output 3 real coordinates; **passive**. Core histories plus semantic/tangent/dual-tetra scripts; not a separately controlled object in the four UIs. Exact production file and memory_kernel call. Current Paper F uses the same transverse basis vectors on different, raw complex inputs: **mathematical basis correspondence only**, not the same map. No eight-generator SU(3) group evolution is implemented here.

### M11 — Cycle stages and nine identity labels [E]

**Source:** `identity_rules.py:7,29,38,55`. Stage counts strict crossings of κ thresholds (.2,.5,.9,1.3,1.8,2.3); `identity=(3*stage+offset(sign z)) mod 9`, with zero/positive/negative offsets 0/1/2. Inputs κ,z; outputs integer stages and names; **passive categorization**, stored in state. Scripts plot labels, all UIs record them indirectly. Exact production and cognitive/memory callers. No current physics-kernel identity-state public analogue; no accepted Paper A–F memory semantics. Threshold counts can wrap into repeated labels.

### M12 — CP-labelled cyclic windows [B]

**Source:** `cp_windows.py:7,20`. Mark q whose cyclic distance from any configured center is ≤halfwidth. Default N=12, centers 3,9 and halfwidth1 gives {2,3,4,8,9,10}. Inputs sector array/config; output Boolean mask; **passive**. CP-split scatter, samplers and diagnostics through scripts; no dedicated four-UI control. Exact production file, activity unestablished. No current public CP-window operation; clock exists separately. No Paper A–F physical CP correspondence established; this is a finite cyclic selection rule.

### M13 — Full composite recursive-change statistic [A]

**Source:** `definitions.py:263`. For adjacent rows, `dZ=||ΔZ||`, `dφ=|wrap(arg(mean_i Ω_i(n+1)conj Ω_i(n)))|`, `dq=1[q changes]`, `dκ=|Δκ|`; `v=sqrt((wZ*dZ)²+(wφ*dφ)²+(wq*dq)²+(wκ*dκ)²)` with defaults (1,1,.5,0). Input histories/weights; output n−1 statistics/components; **passive**. U v_rec panel/radio/checkbox and spike scripts. Exact production definitions, active runtime use not established. Paper E §13 eq30 formalizes it and its ordinary clock floor .5; absent as a supported public UI operation. No division by dt: not a physical velocity.

### M14 — Origin-direction turning [A]

**Source:** `definitions.py:117`, T `_vrec_geom:80`. `a_n=acos(clip(Z_n·Z_(n+1)/(||Z_n||||Z_(n+1)||),−1,1))`, with norm-floor masking. Input selected Z history; output angles, summaries; **passive**. T text and timing; scripts/tests. Exact production helper. Paper E eq31 separates it from M13; no dedicated current old-style angle dashboard. T fallback has a recursive-call defect, not another mathematical definition.

### M15 — Polyline turning, normalized pair chirality and loop scores [A]

**Source:** `side_zchiral_probe.py:33,46` and `chirality_lab.py`. Turning compares consecutive ΔZ directions; phase-only pair chirality divides each product by `|a||b|+eps`; loop score compares endpoint closure with path length. Inputs histories; outputs turning/correlation/closure diagnostics; **passive**, scripts only. No matching production module (underlying raw chirality shared). Paper E §13 explicitly distinguishes segment from origin turning and exploratory consumers; raw C exists current, these composite probes do not have public operations. Category A acknowledges documented diagnostic distinctions, not an accepted universal loop interpretation.

### M16 — Entropy-change v_rec [B]

**Source:** `definitions.py:109,340`, `rsb_spectral_viz.py:294`. `v_n=|H_(n+1)−H_n|`. Input spectral entropy; output transition series; **passive**. U/L/T RSB popup path. Exact production definitions; no proven active caller. No current RSB entropy engine; Paper E distinguishes this namesake from geometric velocity without reconstructing the RSB science. Units depend on M23/M48 entropy convention.

### M17 — J sign, flips and commitment [A]

**Source:** `definitions.py:50–97,148`; `physics_sampler2.py:61`. Sign deadband default 10⁻⁹; count flips between surviving nonzero signs. Commitment uses first sufficiently large |J| (default .9 maximum) whose remaining nonzero signs agree; selection window uses configurable low/high fractions (often .1/.9). Inputs finite J/time; outputs signs, flip count, times/window/radius summaries; **passive**. All J panels use tail/selection summaries, T shows tJ. Exact production source. Paper E distinguishes these finite-history diagnostics; no public commitment-law interpretation or old dashboard in current UI.

### M18 — Cumulative-direction stabilization [B]

**Source:** `definitions.py:181`. Tail direction from the mean of the last30 stored vectors, rejected when its norm is nonfinite/too small; find earliest cumulative mean direction, after a minimum prefix, aligned within default 15°. Inputs Z/time; outputs tZ or unresolved value; **passive**. T timing text and scripts. Exact production definitions; activity unestablished. Current historical alignment diagnostic is related but this entire retrospective settling procedure is not the same public operation. Paper E discusses readout alignment; this threshold method is not a theorem of permanent settling.

### M19 — RSB channel transfer [D]

**Source:** `rsb_model.py:15,45`. Complex state ψ∈C^(C×M×H), defaults C=3,M=12,H=2. Apply `Tchan=D R U`, using mixing angle θ=.35, phase φ=0, recursion coefficients α_L=.2, β_S=.1 and visible attenuation d_vis=.95. Explicitly, `U=[[cosθ,sinθ,0],[−sinθ,cosθ,0],[0,0,exp(iφ)]]`, `R=[[sqrt(1−α_L−β_S),0,0],[sqrt(α_L),1,0],[sqrt(β_S),0,1]]`, and `D=diag(d_vis,1,1)`. Inputs ψ/parameters; output transferred ψ; **stateful independent engine**. U/L/T through RSB runs, not B. Byte-identical production engine, active call not established. Current fixed `srg` construction is not equivalent; no accepted full RSB runtime analogue in A–F.

### M20 — RSB ring/helicity drift [D]

**Source:** `rsb_model.py`, spectral Hamiltonian builder and step. Ring second difference `L_m f=f_(m+1)+f_(m−1)−2f_m`; `H=kL P_L⊗L⊗I + kS P_S⊗L⊗σ_z + μ(P_L+P_S)⊗diag(mask)⊗σ_x`, with kL=.4, kS=.3, μ=.25 and channel projectors P_L/P_S; σ_x swaps the two helicities and σ_z=diag(1,−1). Euler drift `ψ←ψ−i eps_rsb Hψ`, eps_rsb=.05. The sampled mask `cos(M*2πm/M)` equals 1 mathematically at every grid point, so does not resolve angular anisotropy. Its own docstring explicitly says this keeps the toy model simple and makes the μ-term global in phase; this is documented intent, not an inferred bug. Inputs ψ/operators; output ψ; **stateful**. U/L/T; exact production file. Paper A ring Laplacian supplies a mathematical operator analogy, not identity of states or full dynamics. Current ring F_M and old RSB are distinct.

### M21 — RSB reinforcement and normalization [D]

**Source:** `rsb_model.py` step. Visible channel multiplies by exp(−η/2), dark channels by exp(γ/2), defaults η=.02, γ=.05; after other operations normalize total complex norm (with explicit fallback for degenerate input). Inputs ψ/gains/RNG; output ψ of normalized norm; **stateful**. U/L/T, exact production engine. No full current/Paper A–F operator counterpart. “Energy” in downstream plots is squared coefficient magnitude, not calibrated physical energy.

### M22 — RSB dominant-band contraction [D]

**Source:** `rsb_model.py` contraction. Let m0=argmax Σ_channel,helicity |ψ|². `ψ←(1−a)ψ+a P_m0 ψ`, a=clip(α,0,1), or clip(α H_norm,0,1) if adaptive. Core α default0, adaptive false; viewers commonly .6. A Gaussian `band_mask` is constructed but unused in this actual contraction. Its docstring explicitly reserves it for UI/diagnostics or alternative contraction rules. Inputs ψ/α; output attenuated nonwinning bands before normalization; **stateful**. U/L/T α controls; exact production. No current/Paper A–F accepted counterpart; the unexecuted smooth alternative is not the implemented contraction.

### M23 — RSB band observables [B]

**Source:** `definitions.py:240,464,476,502,596`. `E_tm=Σ_c,h|ψ_t,c,m,h|²`, **not an FFT**; p=E/ΣE; normalized `H=−Σp ln(p+eps)/ln(M+eps)`; dominant m=argmax E. `d=||ψ_visible−mean(dark channels)||`; `sigma_spec` is linear band-index **variance**, not standard deviation or circular variance; visible helicity imbalance `(E_0−E_1)/(E_0+E_1+eps)`. Inputs ψ history; outputs arrays, final spectrum and summaries; **passive**. U/L/T RSB plots; exact production definitions. No current RSB public analogue; no proof here that band index is a physical wave number.

### M24 — RSB regimes and seed collapse labels [D]

**Source:** `definitions.py:354,596,754,859`. Tail statistics (last quarter with minimum-tail rules), coefficient of variation, variance/imbalance thresholds produce I/II/III/ambiguous labels; later meta-label refinement uses H(T)/H(0) and first 10%-entropy collapse time. Inputs M23 history; outputs labels, collapse time, visited/switching bands. **Passive heuristic**. U/L/T text and seed-info, scans. Exact production definitions. No current A–F theorem equates these labels to phases of matter, reversibility or attractor classes; old README labels are historical claims, not new findings.

### M25 — Triad-to-RSB parameter conditioning [D]

**Source:** L `tri_to_rsb_params_live:85`, T `tri_to_rsb_params:102`, U nested conditioner. `Jnorm=clip(mean|J|/Jmax,0,1)`, where Jmax=max|J| if positive and1 otherwise, and tail sign determine `α_eff=α_base(.3+.7 Jnorm)`, `μ_eff=.6+.2 sign`, `γ_eff=.2(.5+.5 Jnorm)`. Other viewer RSB knobs include kL=.02,kS=.3,η=.005 and 300 updates. Inputs completed triad observables/baseα; outputs a new independent RSB run's parameters; **one-way conditioning**, no Ω feedback. L/U single/T; not B. No production UI conditioner found; having both cores in TOR is insufficient evidence of this coupling. Current/Papers A–F do not establish this as physical coupling.

### M26 — Latent option volume / foreclosure [E]

**Source:** `latent_foreclosure.py:10`, optional `model_core.run`, `run_unified_diagnostics.py:230–280`. Clone state, perturb Ω at default δ=10⁻⁴ with seed1337+step, N=16 trials, K=5 future steps; survivors remain within an endpoint Z corridor. Return survival fraction, median endpoint radius and sqrt(det covariance) (undefined volume with too few samples). Optional runner adds first-valid radius baseline and persistent relative-radius/survival thresholds. Inputs model/state/probe parameters; outputs option metrics; **passive for original state but evolves clones**. Scripts, no four-UI widget. Exact production source and conditional core hook; active configuration unproved. No current scientific API/Paper A–F mathematical option-volume interpretation. Probe dt defaults independently; callers shown do not forward the run dt.

### M27 — Phase-gap emission gate and payload [E]

**Source:** `seed_emission.py:17,35,50,53,85`. Channel angles `a_j=wrap(2πq/N+arg Ω_j)`; gate if wrapped angular distance to center is ≤ configured width (the value called width is a halfwidth). Defaults N=24,width5°. Optional coherence threshold; partial/coherent modes accept any/all channels. Payload copies phases, amplitudes, channel, step. Inputs Ω/q/gate; outputs event flags and copied payload; **passive relative to Ω**, no depletion or feedback. Script runners; no widget in the four UIs. Exact production file; broader memory seed workflow exists but every gate configuration is not proven active. No current geometry-gap/API counterpart; Paper D/E explicitly leave aperture attachment open. N=24 gate with default N=12 core is a real configuration distinction, not automatically a full 24-sector trajectory.

### M28 — External seed-world motion [E]

**Source:** `seed_entities.py:13,45`. Per-entity ID/birth/channel/position/velocity/initial velocity/payload/trail/alive state. `v←(1−drag)v+drift`, `x←x+dt*v`; defaults dt=1,drag=.02. Inputs emitted payload and external-world controls; outputs evolving positions/trails; **stateful external world**, no Ω feedback. Runners/log/plot scripts, not the four UIs. Exact production and active memory_graph/NativeWorldRuntime use. No current scientific runtime or Paper A–F physical seed trajectory law.

### M29 — External trajectory classification [E]

**Source:** `seed_trajectory_analysis.py:5`. With default min_samples200, shorter histories are “grazing”; otherwise all positive radial increments above eps imply “escape”, any negative increment below −eps implies “return”, remainder “grazing”. A later `<3` unknown case is unreachable under that default. Inputs stored radial history r=sqrt(x²+y²), not full3D radius; output label; **passive heuristic**. CSV analyses/figures, no four-UI control. Exact production and memory_graph caller. No current/Paper A–F orbit classification theorem; labels are application thresholds.

### M30 — Trajectory snapshot persistence [E]

**Source:** `trajectory_logging.py:14`; TOR `trajectory_v2.py`. Serialize external entity snapshots and summaries to JSONL; V2 adds epoch/frame identity, genesis, chunks, manifests/hashes, boundary records and verification. Inputs state snapshots/configured paths; outputs persisted records, **stateful I/O, not evolution**. Script/production consumers, no four-UI widget. OLD/TOR legacy logger body shared; V2 purpose similarity only. Current immutable RunRecord/GeometryRecord are related in general provenance purpose, not the same schema or demonstrated code lineage. No Paper A–F equation analogue required.

### M31 — Scalar cylinder embedding [A]

**Source:** `geometry_3d.py:4`, `geometry_embeddings.py:12`. `(x,y,z)=(κ cosθ,κ sinθ,z)`, θ=2πq/12 in these historical cylinder helpers. Inputs κ/q/z history; outputs numerical 3D coordinates; **passive**. `analysis_tools.plot_trajectory_3d`, run_sim/scripts; not the T channel torus. No matching TOR geometry module. Current z_diagnostics cylinder point/history, Paper E eq24 with explicit sector context. Does not encode full complex state.

### M32 — Whole-history scalar torus [A]

**Source:** `geometry_3d.py:25`, `geometry_embeddings.py:19`. `H=max_history|z|+10⁻⁹`, `r=rmax κ/(1+κ)`, `χ=π z/(2H)`, `G=((R+r cosχ)cosθ,(R+r cosχ)sinθ,r sinχ)`, defaults R2,rmax1. Inputs finite history/config; outputs 3D coordinates; **passive history-dependent**. analysis_tools/run_sim, current history display; not the per-channel T map. No TOR same-name geometry source. Current public history_torus and Paper E eq25/conditional inverse eq27. Extending history can reposition an old sample; one helper has configurable N, the other hardcodes12.

### M33 — Direct macro/chiral/total vector path [A]

**Source:** `geometry_3d.py:60`, `analysis_tools.py:93,119`, U/T viewers. Return stored selected vector columns, default fallback to Z_vec. Inputs M/C/T history; output 3D path; **passive**, no geometric placement transform. U raw vector panel; T before M35 scaling. TOR core stores vectors, no matching plotting module. Current direct history coordinates/observer panels; Paper E. Paper B supplies a separate specified tangent realization, not arbitrary embedding of T.

### M34 — Per-channel Omega torus [A]

**Source:** T `embed_on_torus:283`. For j=0,1,2, fixed major azimuth ψ_j=2πj/3, tube phase η_j=arg Ω_j, `r_j=.6(1+.4 log(1+|Ω_j|))`; point `((2+r_j cosη_j)cosψ_j,(2+r_j cosη_j)sinψ_j,r_j sinη_j)`. Inputs complex history; outputs three 3D curves/nodes; **passive**, no q,z,T dependence. T only; no TOR implementation. Paper E §11 eq26 explicitly reconstructs it, including signed-zero phase artifacts; no current public channel-torus UI. It is not the M32 scalar torus.

### M35 — Percentile overlay and viewer elevation [A]

**Source:** T nested overlay and scalar-selection callbacks; Paper E §12 eq29. Scale selected Z history by `.85*.6 / percentile99(valid positive norms)` with fallback denominator1. Alternative strong-change scalar is `atan2(Z3,sqrt(Z1²+Z2²)+eps)`. Inputs selected Z history; outputs display-only curve/scalar; **passive**. T Z radio, highlight/timing context; no TOR formula consumer found. Paper E preserves this historically; current raw direct-coordinate analysis does not silently apply this normalization. Scaling is per selection/history, retrospective and not bounded by the percentile for outliers.

### M36 — Dual tetrahedra and throat-normalized trajectory [C]

**Source:** `dual_tetra_mapper.py:5–22`, `analysis_tools.py:196`. Opposite tetrahedra from ±scaled vertices {(1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1)}. Permute probability basis coordinates to (c_x,c_y,c_u), normalize whole-path maximum radius to throat scale. Inputs weights/history and DualTetraConfig; outputs vertices and path; **passive geometry/display**. run_sim/analysis_tools, not one of the four direct UIs. No TOR module; current C01/D03 different. Paper D mentions historical dual tetrahedra but does not identify this as an accepted physical throat.

### M37 — RSB toroidal halo [C]

**Source:** T nested `draw_rsb_halo` around520. Draw tube-section rings at major angles `2π(m+.5)/M`, slightly enlarged frame radii; color from normalized log band energy, opacity/brightness tied to α/.6 with clipping. Inputs final E_m/α/frame; outputs 3D colored lines; **passive display**. T intended consumer only. In this snapshot T requests `band_energy_series` but `analyze_rsb_history` returns `E_t_m`; missing E leads to no halo lines. No TOR viewer/current public counterpart or accepted A–F field mapping. Construction exists; visible delivery under this path is disconnected.

### M38 — Tangent-corridor alignment [B]

**Source:** `tangent_corridor_analysis.py:11`. Form XY torus-like curve `((R+ρ cosφ)cosφ,(R+ρ cosφ)sinφ)`; compare discrete unit tangents with changes in the **first two** uxy coordinates, `(c_u,c_x)`. Mark absolute dot product above threshold (.8 default). Inputs histories/display parameters; output alignment series/mask/plots; **passive**. Script diagnostics, no direct four-UI control. Exact production source, active caller unestablished. Current/Papers A–F have no accepted identification with D03 corridors. Selecting `(c_u,c_x)` is specifically not the transverse `(c_x,c_y)` plane.

### M39 — Strong-change clustering and arrival-sector statistics [B]

**Source:** `tangent_corridor_analysis.py:84,208`, `diagnostics.py:170`. Cluster `(Δκ,Δz)` with SciPy kmeans2, select strongest mean-magnitude cluster and local magnitude threshold, then split arrivals by sector/CP mask. Simpler UI variant marks Euclidean change > half maximum. Inputs recorded scalar history; output cluster/event masks, histograms and CP counts; **passive**. B/T red polar arrival bins use the simpler threshold; scripts use clusters. Exact production tangent/diagnostics modules; no current public clustering control. Paper E discusses strong-change displays but not a physical corridor identification. kmeans initialization is not explicitly seeded in this helper.

### M40 — Frenet invariants and fitted “geometric chirality/potential” [D]

**Source:** `chirality_lab.py:288,359,654`. Finite differences with mean dt estimate v,a,jerk; `κ_g=||v×a||/(||v||³+eps)`, `τ=(v×a)·jerk/(||v×a||²+eps)`. Least-squares fit |J| to [1,κ_g,|τ|,κ_g²,τ²,κ_g|τ|], name fitted result χ_geom; plot χ_geom² as U_geom. Inputs Z/J/t; outputs fits/curvature/torsion/plots; **passive experimental diagnostic**, scripts. No TOR same-name module, no current public operation. Paper E §13 discusses and bounds it; squaring a regression fit is not recovery of a physical potential or force.

### M41 — J regressions, lagged correlations and spike coincidences [B]

**Source:** `chirality_lab.py:34–227,446–790`, `diagnostics.py:235`. Linear J≈w·Z and quadratic ten-feature least squares; fitted same-data R²; lagged Pearson correlations; sign/dJ pulses and high-quantile events. Inputs finite histories/lag/thresholds; outputs coefficients, scores, event masks and plots; **passive**. Scripts only. Some J-coupling helper exact in TOR diagnostics, wider lab not present. Paper E notes exploratory consumers; no public current fitted law. Correlation/fit does not establish causation or generalization.

### M42 — Rolling onset, settling and stability summaries [B]

**Source:** `rgd_connection_diagnostics.py:40–173,239`. Rolling variance `E[x²]−E[x]²`; onset relative to early baseline; first held low variance relative to tail target; finite-fraction/threshold stability flags. Inputs history/windows/factors; outputs tJ/tZ onset/settle/lock fields, summary flags; **passive**, scanner scripts only. No same TOR module (shared core/readouts underneath). Current finite sweeps exist, but not these empirical classifiers; no A–F global phase theorem. Definitions of onset, commitment and settling are distinct.

### M43 — Finite-run regime maps and empirical edge search [B]

**Source:** `explore_sweep.py`, `wide_scan_triocta.py`, `edge_map.py:215`, `summarize_edge.py`, `fit_eps_exponent.py`. Run parameter/seed grids or random samples; classify finite prefixes and tail thresholds; bracket/bisect g by observed failure predicate; aggregate maximal observed stable and minimal failing g; log-log least-squares power fits. Inputs scan bounds/time horizon/seeds; outputs CSV/JSON/heatmaps/bounds/exponents; **orchestration evolves independent Ω runs; summaries passive**. Scripts only. No equivalent TOR scanner module. Current finite dataset/sweep infrastructure is a purpose analogue, not shared thresholds. Paper A/F stability theory and Paper E bounded failures do not turn these empirical boundaries into exact global critical curves.

### M44 — Statistical aggregation and uncertainty [B]

**Source:** `scan_rgd_connection.py:119,135,156`, `analyze_rgd_rows.py:41,51`, scan/plot consumers. Binomial Wilson intervals for stable fraction; seeded/unseeded bootstrap means as configured; group-by parameter summaries, bins and observed tradeoff envelopes. Inputs stored run rows; outputs aggregate tables/intervals/plots; **passive**. Scripts, no four-UI widget. No matching TOR implementation. Current datasets/comparison general purpose only; no new Paper A–F stochastic theorem claimed.

### M45 — Reflecting-box external three-body / Newton probe [D]

**Source:** `triocta_probe_utils.py:24,32,54,71`, `run_triocta_structural_3body_probe.py:43–197`. Three external equal masses start in a small box, velocities along q-based directions θ+2πj/3 at v0=.2. On stage change or >15° Z turn reset all velocities to those directions. Reflect in [−1,1]³. Optional after 400 events: `a_i=G Σ_(j≠i) m_j(x_j−x_i)/(||x_j−x_i||²+soft²)^(3/2)`, velocity-Verlet; defaults G1,soft.01. Inputs precomputed Ω history/external controls; outputs body CSV/config/history/plots; **external stateful**, no feedback into Ω. Separate CLI, absent from four UIs/TOR kernel/current public API. Newtonian gravity is supplied as a probe law, not derived from Tri-Octagon or Papers A–F; event velocity resets continue even after gravity is on.

### M46 — Six-ray alignment and collective slips [B]

**Source:** `triocta_probe_utils.py:44,47`, `run_sims_minimal.py:37,46`, `phase_triad_experiment.py:62`, unified runners. Nearest angular ray among kπ/3; wrapped distance. Collective-phase jumps near ±2π/3 within tolerance define slips; optionally condition counts on coherence/J≈0. Inputs angles/history/gates; outputs ray index/distance/slip/events; **passive event extraction**, can trigger external routines. Scripts only; elementary gate/coherence shared with TOR but these specific wrappers not established there. Paper D six-segment scaffold is not this ray selector; current research exclusion explicitly separates a physical six-axis selector.

### M47 — Measurement/display noise [C]

**Source:** all four UI run helpers. After deterministic history generation, add Gaussian perturbations to displayed κ,z,J using a viewer RNG; Ω and computed M/C/T are not recomputed from those perturbed scalars. Inputs history/noise slider; outputs altered display observables; **passive relative to model**, stochastic display. L/U/B/T. No production UI counterpart; no current public equivalent. Paper E §12 distinguishes this from M05. A noisy J can influence M25 because the UI conditioner reads those observables; that still does not retroactively perturb Ω.

### M48 — Alternate spectral energy/entropy display helpers [F]

**Source:** `spectral_viz.py:10,98,209` versus `definitions.py`/`rsb_spectral_viz.py`. Same family E=Σ|ψ|² and argmax bands, but spectral_viz defaults to **base-2 unnormalized entropy**, clips probabilities, and can clip negative E in an array view. definitions uses normalized entropy. Inputs ψ/E; outputs spectra/H/m0 and figures; **passive intent, possible in-place clipping of supplied E**. RSB scripts and alternate plotting paths. TOR contains definitions only, not spectral_viz. No current RSB API. F marks overlapping implementations, **not** interchangeable values or an instruction to remove either.

### M49 — Reduced linear stability approximation [D]

**Source:** `eigen_analysis.py:8,16,53`. L3 spectrum {0,−3,−3}; approximate real scalar Jacobian eigenvalues `1−2ε k_ref+g μ_L`, k_ref typically mean k. Inputs ε/g/k; outputs eigenvalues, spectral-radius commentary; **passive**. Scripts/run_sim, no direct four-UI control. No TOR same-name module. Exact L3 spectrum corresponds to Paper A; current/Paper F full complex, phase-composed local analysis is more qualified. This approximation is not the full heterogeneous complex Jacobian/Floquet map.

### M50 — Semantic-labelled axis/jump views [C]

**Source:** `semantic_diagnostics.py:9,20,55,98`, `analysis_core.py`. Projected-axis alignment, jump magnitudes, CP/cycle cross-counts, and |gradient κ| convergence-style summaries. Inputs histories/uxy; outputs plots/scalars; **passive**. Scripts, no direct four-UI panel. No TOR semantic_diagnostics module, though identity/basis inputs are used there. No current public semantic observable or Paper A–F semantic/AI theorem. Names describe historical presentation rather than recovered cognition physics.

### M51 — Intended meaning of constants and physical/semantic names [G]

**Source:** `constants_selector.py`, `model_core.py` defaults; old README and labels such as “flavor”, “CP”, “spectral energy”, “throat”. The numerical formulas are separately enumerated; the derivation assigning .618/.577/.244, π/e/φ/ζ(3), or these names a common physical ontology is **not recovered**. Inputs are configured literals/names; output is a proposed interpretation, not an implemented extra equation; **non-evolving metadata/meaning**. Seen across old apparatus and copied TOR names. Current/Papers A–F deliberately qualify literals and interpretations. G does not imply that the implemented arithmetic is unknown.

### M52 — Historical provenance, schema and golden-reference algorithms [F]

**Source:** `provenance.py:9–36`, `model_core.py:105`, `select_golden_points.py`, `generate_golden_refs.py`, `run_tests.py`, `new_run_tests.py`. Stable parameter hashing plus seed/version/time/UUID metadata; selected stable/edge/failure configurations; NPZ reference comparison, checksums, history schema checks, sampler-J consistency and masked unit-vector angle/chord identity. Inputs config/history/reference files; outputs metadata/test diagnostics/golden arrays; **passive bookkeeping or isolated test runs**, not physics. U/T show provenance; model histories available to all; TOR shares core metadata but not the standalone RunMeta module. Current immutable versioned records provide a clearer supported provenance contract; not schema/code equivalence. Old test files were read, never run; printed “ALL PASS” literals are not results of this census.

### M53 — Plasticity and last-threshold lifetime [B]

**Source:** `plasticity_map.py:68`, `phase_triad_experiment.py:170`, `make_vrec_timeseries_figures.py:42`. `T_theta=max{t_n : v_rec(n)≥theta}`, with counts above thresholds and late-tail summaries; empty-event conventions belong to each helper. Inputs a specified v_rec variant/time axis/threshold, outputs lifetime/counts/maps; **passive** over independently run histories. Scripts only; no four-UI widget. No identical TOR module; underlying v_rec definitions shared. Paper E documents diagnostic threshold distinctions, not a universal memory/physical lifetime; current UI does not expose these legacy sweep products. The experiment's ModelAdapter.reset/step are unimplemented protocol stubs, so that script is not an established working model integration.

### M54 — Emission ratios and channel/event-window entropy [B]

**Source:** `analyze_emission_R.py`, `analyze_emission_entropy.py:6`, `analyze_event_window_entropy.py:8`. Channels-per-event `R=(n0+n1+n2)/max(n_events,1)`; normalize emitted channel counts and compute `H=−Σ p_i ln p_i`, zero when no counts, optional bits via division by ln2; event-window variant groups emit rows by floor(step/2000), then counts channels in each bucket. Inputs saved event/summary CSV rows; outputs per-run/per-lambda ratios, entropy and enriched CSV/printed tables; **passive**. Script figures/aggregates only. No exact TOR analyzer module for these statistics (seed-trajectory aggregation is separate). No current public/Paper A–F dedicated emission-statistics counterpart. This is count entropy, not the RSB band's entropy and not information-theoretic evidence of semantic meaning.

## 5. Historical UI census

The actual paths are [toy_ui_live.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_ui_live.py), [toy_ui.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_ui.py), [toy_lab.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_lab.py), and [toy_3d_triocta.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_3d_triocta.py). All four build Matplotlib figures/widgets. None defines scientific tabs or separate editable numeric text fields; numeric values are supplied by sliders or fixed source parameters. Ordinary Matplotlib toolbar/camera controls are presentation controls, not kernel operators. None of the four has a timer-driven model animation. The 3D viewer has manual history/trail interaction. No UI was launched because launches/reruns can write outputs.

### 5.1 Common controls and non-common defaults

| Control | Range/default | Supplier and effect |
|---|---|---|
| ε slider | .01–.1, step .005; initial .05 | Rebuild ModelParams.eps, M01; changing it alone does not certify a new run |
| g slider | .1–.3, step .01; initial .2 | ModelParams.g, M01; not geometric gap length |
| k3 scale slider | .5–3, initial1 | Multiplies third element of caller-selected triplet, M04 |
| noise σ slider | 0–.1, initial0 | M47 post-run observable perturbation; not core omega_noise_sigma |

“Default run” differs by entry point. L/U choose `theta_scaled`; B/T choose `theta_soft` with α=1. L/U/B ordinarily store 200 rows at dt=.05; T stores 300 at dt=.05. U uses the fixed triad seed42 on its Run handler, B reruns with a fresh random seed after its initial seed42, L chooses fresh triad/RSB seeds, T exposes its triad seed explicitly. These choices affect reproducibility and parameter conditioning. Core `run(seed=...)` metadata alone does not seed every RNG source.

### 5.2 `toy_ui_live.py` (233 lines)

Main owners: `run_triocta:52`, `tri_to_rsb_params_live:85`, `launch_live_ui:108`, run callback around160. The word “live” names the interactive apparatus; it is not a continuous integration timer.

| Surface element | Supplying computation / inputs | Display or action |
|---|---|---|
| J_eff(t) panel | M08, noisy if M47 selected | Scalar cubic chirality curve from completed triad run |
| κ–z panel | M06, possibly M47 | 2D recorded scalar scatter |
| Run seed/RSB summary text | RNG selections, M23–M25 | Run context, effective conditioning and regime/entropy summary |
| Four common sliders | Lines151–154 | Read when Run is invoked |
| RSB α slider | Line155, 0–.9, initial .6 | Base contraction for M25; not simply the effective α |
| `Run (Tri + RSB)` | Line158, callback160 | Reruns triad, derives α_eff/μ_eff/γ_eff, then runs 300-step RSB and updates panels/text |
| RSB spectral popup | `rsb_spectral_viz` + M23 | E(t,m) heatmap; band index is not an FFT frequency by construction |
| Final-band popup | M23 | Bar plot E(T,m) |
| Entropy/dominant-band popup | M23 | H(t) and m0(t) |
| Recursive-velocity popup | M16 | |ΔH|, not U's composite geometric statistic |

No identity/CP selector, gap aperture, external seed-world control, gravity control, or folded-shell object occurs here. Current scientific UI has no RSB counterpart or dedicated old J/κz dashboard; deterministic dynamics and passive readouts are available through explicit current contracts.

### 5.3 `toy_lab.py` (366 lines)

Owners: `run_model:62`, `launch_lab:121`, run callback247; unused `compute_phi_index:52` derives phase-based bins but is not the source of the displayed recorded clock.

| Surface element | Supplier | Meaning |
|---|---|---|
| J panel | M08/M17/M47 | Full J(t), tail plateau/sign annotation from last20 rows |
| κ–z scatter | M06/M47 | Recorded scalar path |
| 12-bin polar panel | Recorded phi_index M03; occupancy histogram normalized by its maximum | Clock occupancy, not inferred phase of mean Ω |
| Red polar bins | Δ=sqrt((Δκ)²+(Δz)²), events Δ>.5 maxΔ; arrival clock bins | Simple strong-change arrival diagnostic M39, not kmeans clustering |
| Polar pointer | Final recorded sector | Location of last stored clock row |
| Common four sliders | Lines218,224,230,235 | New values used by Run |
| `Run` button | Line245/callback247 | Generates new random initialization seed and refreshes all panels |
| Preset/initial configuration | Soft triplet α1, seed42 initially, 200 rows/dt.05 | Fixed source default, no preset menu |

No 3D object, RSB panel, checkbox, radio group or animation is defined. Current UI retains explicit clock/observer histories but does not offer this exact red-bin occupancy apparatus. The unused phase-bin helper is not evidence that displayed q came from Ω phase.

### 5.4 `toy_ui.py` (755 lines)

Owners: `run_rsb_once:72`, `format_regime_summary:122`, `run_model:167`, `launch_ui:240`; display callbacks422/431/439, triad Run536, single RSB632, sweep689, seed info716.

| Surface/control | Source / values | Mathematical effect |
|---|---|---|
| J panel and plateau annotation | M08/M17, completed triad history | Cubic scalar history; noisy if slider selected |
| κ–z panel | M06/M47 | Scalar scatter, not Z-vector geometry |
| v_rec panel | M13 | Full composite or its dZ/dφ/dq/dκ components |
| 3D Z panel | M33 | Selected raw total/macro/chiral vector history |
| Z radio | Line414: total, macro, chiral; total initially | Selects vector display and z_key used by composite statistic |
| v_rec radio | Line417: `v_rec`, `components` | Switches total versus component series presentation |
| `dkappa` checkbox | Line420, false initially | Turns κ contribution weight from0 to1 / corresponding component visibility |
| Four common sliders | Lines493–496 | Values read by triad Run; slider callbacks themselves are no-ops |
| `RSB seed` slider | Line499, integer0–999, initial0 | Seed for single RSB run |
| `RSB α` slider | Line525, 0–.9, initial.6 | Base α for conditioner/sweep inclusion |
| `Run TriOcta` | Line516 | Fixed triad seed42; refreshes triad panels and retained data; does not itself rerun RSB |
| `RSB: single run` | Line517 | Uses most recent triad J and selected α through M25, selected RSB seed; stores last_rsb_stats/seed |
| Four single-run popups | `rsb_spectral_viz` | Band evolution, final spectrum, entropy+dominant band, |ΔH| as above |
| `RSB: α sweep` | Line518 | Runs sorted unique α values {0,.3,.6,.8,slider}; uses seed0 and fixed μ=.6,γ=.2 rather than selected seed/triad conditioner; plots d(t), spectral variance and h(t) comparisons |
| `RSB: seed info` | Line519 | Summarizes last completed single run: H0,HT,ΔH, 10%-collapse time, final/visited bands and switch count; no fresh simulation |
| Regime/context text | M23/M24/RunMeta M52 | Effective α, seed, regime and entropy/band context |
| Source defaults | Scaled triplet, 200 rows/dt.05 | No preset menu; slider seed is RSB-specific |

Exception handling can produce fallback empty/zero diagnostic arrays; presence of a curve is not a parity certificate. Current UI has supported raw C and M/C/T history choices, but no old composite-v_rec component checkbox, RSB conditioner or regime sweep.

### 5.5 `toy_3d_triocta.py` (1,029 lines)

Owners: `_vrec_geom:80`, `_jeff_series:92`, conditioner102, `run_triocta:138`, `embed_on_torus:283`, CSV exporter347, `launch_3d_lab:377`; nested halo around520, Z selection/elevation around636–685, trail callback826, rerun848.

| Surface/control/object | Supplier | Meaning / qualification |
|---|---|---|
| Torus wireframe | Standard major radius2, minor radius.6 | Guide surface only; no triangulated physical kernel shell |
| Three colored points and curves | M34 | Per-channel Ω, fixed major azimuth and phase-dependent tube coordinates |
| Colored trail segments | Normalized full-history J, coolwarm map | Scalar color coding does not turn J into spatial flux |
| Full selected Z overlay | M33 followed by M35 | Per-history 99th-percentile scale; separate from Ω curves |
| Z radio | Line685: total, macro, chiral, off | Recomputes selection-specific scale and direction/timing context; off hides overlay |
| RSB halo | M37 rings, M23 E_m and α | Coded intended object; missing `band_energy_series` key leaves E_final absent under inspected path |
| J panel | M08/M17/M47 | J(t), tail plateau/sign, flip information |
| Polar occupancy and pointer | M03/M39 | 12 clock bins, final recorded sector, red arrival bins |
| Strong-change scalar | M35 elevation-like scalar for selected vector, with fallback older z | Not necessarily scalar M06 z even though same display role |
| v_rec text | M14 direction-only helper | Mean/max turning; not U composite statistic |
| tZ / tJ text | M18/M17 | Distinct retrospective stabilization/commitment criteria |
| Run ID/time text | M52 metadata | Provenance context, not immutable current RunRecord identity |
| Four common sliders | Lines803–806 | Values used on Run |
| `seed` slider | Line807, integer0–1,000,000, initial42 | Triad initializer; RSB initialization uses seed+1 |
| `trail length` slider | Line810, integer10–300, initial75 | Manual curve prefix/end-point display; callback does not rerun model; full Z overlay is not shortened with the Ω curves |
| `Run` | Line820/callback848 | Reruns triad and RSB, refreshes retained/display data, invokes CSV export |
| Fixed RSB preset | Base α=.6 conditioned on J, 300 updates | No separate RSB α widget in this viewer |
| Automatic CSV output | `dump_timeseries_csv:347`, startup/rerun path | Writes to working-directory outputs; columns include recorded and derived series. Close callback is registered after plt.show(), so no universal close-export success is inferred |

`compute_phi_index:327` and `detect_meta_shell_time:336` are defined but not used to drive the displayed recorded-sector pointer / a visible shell detector. `phi_idx_final` is not a replacement for the stored clock pointer. The `_vrec_geom` fallback calls itself instead of the imported alternative if its first route raises; this is a preserved static defect. The rerun path does not call the timing-text updater in the same way as the Z selection handler, so stale text is a source-level possibility, not an observed GUI result.

Current UI has raw/direct M/C/T histories, scalar-cylinder and scalar-torus histories and cached playback. It does not expose this per-channel torus, percentile-fit overlay, RSB halo, J-colored channel trails, polar-bin panel or tZ/tJ summary apparatus. Paper E already documents much of their mathematics. No conclusion about reinstatement follows.

## 6. Geometry and visualization inventory

All G entries below are outside the accepted C01/D03 exact geometry definitions. Thus **none is already a valid current GeometryRecord definition**. “Existing analysis” identifies where a current detached coordinate result suffices; “separate layer” means the object is a distinct analysis/visual representation, not a proposed implementation or new physics approval. Algebraic formulas can be exact on stated domains while their historical construction uses floating-point NumPy.

| ID / object | Dimension; construction; parameters/dependencies | Historical visibility | Current representation status |
|---|---|---|---|
| G01 scalar cylinder | 3D numerical history, M31; κ,q,z,N | analysis_tools/run_sim | Existing cylinder analysis, not GeometryRecord |
| G02 scalar history torus | 3D numerical/history-normalized, M32; R,rmax,N,whole-history H | analysis_tools/run_sim | Existing public history-torus analysis; Paper E exact conditional map |
| G03 Ω channel tube curves | Three 3D numerical curves, M34; R2,r0.6,log scale.4, Ω phases | T | Separate channel-history visual layer; already in Paper E |
| G04 guide torus mesh/wireframe | 2D parameter surface embedded in3D, standard torus `((R+r cosv)cosu,(R+r cosv)sinu,r sinv)` | T | Decorative/analysis guide, not C01 topology or GeometryRecord |
| G05 raw M/C/T paths | 3D numerical vectors, M33/M06/M07 | U/T, analysis_tools | Existing direct-history analysis, no spatial shell attachment |
| G06 percentile Z overlay | 3D scaled path, M35 with D99/.85/.6 | T | Separate display-normalization policy; raw current path differs |
| G07 dual tetrahedra | 3D vertices algebraically specified, numerical plotting; M36 throat scale | analysis_tools/run_sim | Separate geometry/visual layer; cannot use C01/D03 record unchanged |
| G08 probability simplex/basis path | 2D triangle in real3D plane, M09/M10 | semantic/tangent/tetra scripts; core uxy history | Separate probability-coordinate analysis; not an SU(3) group manifold |
| G09 sector-occupancy polar wheel | 2D circular bars and pointer; N12, histogram max normalization, q | B/T | Separate polar plot; current explicit clock supplies related data |
| G10 CP sectors and scalar split | 1D discrete cycle / 2D marked plots; M12 | physics_sampler2/analysis_tools scripts | Separate mask/analysis; no physical CP or D03 gap mapping |
| G11 XY tangent corridor | 2D display curve/tangent comparison, M38; R/ρ/φ and uxy | tangent_corridor_analysis | Separate analysis; no established scaffold corridor |
| G12 RSB discrete ring/halo | M-index circle, embedded halo rings in3D; M20/M37 | T intended halo; RSB scripts | Separate representation; halo data-key disconnect; not current F_M geometry |
| G13 RSB band-time map | 2D array/image E(t,m), histograms and timelines; M23 | L/U/T popups | Separate spectral analysis; squared coefficients, not measured field energy |
| G14 Frenet/χ_geom/U_geom diagrams | 3D path plus 2D regression/“potential” graphs, M40/M41 | chirality_lab | Separate diagnostic plots; no physical potential field map |
| G15 reflecting box / three bodies | 3D box and trajectories, M45; bounds, v0,G,soft,events | external CLI and analyze_threebody_probe outputs, not four UIs | Separate external simulation geometry; gravity is supplied independently |
| G16 seed-world trajectories | 3D numerical pos/vel/trails, M28/M29 | seed runner outputs and figure scripts | AI-memory/external-world layer, not physics RunRecord geometry |
| G17 six-ray scaffold | 2D angular directions kπ/3, M46; thresholds/coherence | CLI event/alignment plots | Separate angular selector; physical correspondence explicitly open |
| G18 parameter stability maps | 2D/3D axes of parameters and empirical stable/fail values, M43/M44 | scan/heatmap scripts | Separate analysis field over parameter space, not spatial field |
| G19 κ–z scatter / strong-change vectors | 2D readout plot, M06/M39/M47 | L/U/B and diagnostics; T uses related elevation variant | Separate scalar plotting layer; not a state-space bijection |

A search/inspection of the old source tree found **no implemented Maxwell/magnetic field solver**, no Riemann–Silberstein field evolution, no physical flux through a D03 aperture, and no recursive nested spatial octagon/toroid generator. The recursive Ω/RSB updates are iterations of state, not evidence of nested spatial geometry. The dual tetrahedra overlap but do not define a recursive shell stack. Gravity is not absent: the external softened Newton probe G15 is explicit. No inferred gravity law from a torus is present. “Twisted Hex Crystal” occurs in current research exclusions, not as an implemented object in these 89 old Python sources. Broader historical paper claims outside this code census are not refuted by these bounded negative findings.

Visualization-family count (unique mathematical views, not window instances):

| ID | Family | Owners / mathematical supply |
|---|---|---|
| V01 | Cubic J timeline/tail/sign | Four UIs, physics_sampler2; M08/M17 |
| V02 | κ–z scatter and strong changes | Four UI contexts, analysis_tools; M06/M39 |
| V03 | Clock occupancy/red arrival bins | B/T; M03/M39 |
| V04 | Full v_rec/components | U/spike figures; M13 |
| V05 | Raw direct Z/component paths | U/T/analysis_tools; M33 |
| V06 | Scalar cylinder | analysis_tools; M31 |
| V07 | Scalar history torus | analysis_tools; M32 |
| V08 | Ω channel torus and J-colored trails | T; M34/M08 |
| V09 | Percentile-scaled vector overlay | T; M35 |
| V10 | RSB halo | T intended; M37 |
| V11 | Band-time heatmap/waterfall | RSB popup/demo helpers; M23/M48 |
| V12 | Final-band spectrum | RSB popup/helpers; M23 |
| V13 | Entropy/dominant-band timelines | RSB popup/helpers; M23/M48 |
| V14 | Entropy-change timeline | RSB popup/helpers; M16 |
| V15 | RSB parameter overlays/regime summaries | U/scans/demos; M24/M25 |
| V16 | Probability/CP/semantic axis diagnostics | sampler/semantic scripts; M09–M12/M50 |
| V17 | Dual tetrahedron trajectories | analysis_tools; M36 |
| V18 | Chirality fits/curvature/torsion/spike windows | chirality_lab/z_spike/side probe; M13–M15/M40/M41 |
| V19 | Stability/edge/plasticity/statistical parameter maps | sweep/plot scripts; M42–M44; last-threshold time statistics |
| V20 | Seed/body/ray/event trajectory statistics | seed/probe/make_figures scripts; M27–M30/M45/M46 |

## 7. Current-v0.1 omissions and non-omissions

An absence and its reason are separate claims. “Not reconstructed” below means no supported current public operation or corresponding current view was found; where there is no explicit decision record, **reason unknown** remains the rationale. The [K4A surface contract](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/K4A_SCIENTIFIC_UI_SURFACE_CONTRACT.md:253) explicitly excludes named research interfaces. Paper E §§11–17 records historical mathematics without making every consumer part of the package. Earlier K0 implementation statuses are historical planning evidence and are not treated as current missing-feature status.

| Old feature / question | Evidence about absence / presence | Current status and reason category |
|---|---|---|
| Deterministic Ω recurrence and phase synchronization | Current dynamics/API, A/F | Present; not an omission |
| Raw quadratic C and staged M/T | Current readouts/observer/history, B/E | Present with explicit contracts |
| Scalar cylinder/history torus/direct coordinates | Current public detached history operations, E | Present; not an omission merely because T's torus looks different |
| Ω channel torus and percentile overlay | E eq26/29 explicitly recovered; current request/view lists omit them | Paper-present, UI/runtime not reconstructed; historical visualization; reason for omitting each control unknown beyond bounded public surface |
| Old full/directional/entropy v_rec and tJ/tZ panels | E §13 distinguishes them; no old control equivalents | Partly paper-present; historical diagnostics not reconstructed as public operations; no blanket mathematical rejection |
| Cubic J panel | E has J; current plots show raw C instead | Paper-present; dedicated chart not found, reason unknown |
| RSB engine, regimes, conditioner and popups | Full old/TOR source, no current public operation | Not reconstructed; experimental interpretation unresolved; no source evidence that the whole engine was formally rejected |
| RSB halo | Old drawing construction plus missing data key | Historical visual with disconnected source path; current absence reason unknown |
| SU(3)-named probability projection | Existing old/TOR normalized real basis; F raw transverse basis only partially related | Not reconstructed as public probability-coordinate view; no full SU(3) dynamics found |
| CP clock windows, polar arrivals, tangent corridors | Finite selection/analysis formulas in old source | Not reconstructed; reason unknown; no established physical CP/scaffold map |
| Cycle/identity labels, option foreclosure, external seed world | Production memory call sites and application-specific state | AI-memory-specific; current physics API omits those semantics |
| Generic gap emission → C01/D03 apertures | No defined attachment; D/E open interface, K4A research exclusion | Deliberately excluded as physical/public attachment; angular gates still exist historically |
| Spatial registration of M/C/T, six-axis physical selector, feedback | K4A lines254–259/262; E open interface | Deliberately excluded research; passive coordinates remain present |
| Complex forcing/noise and post-run measurement noise | Separate old code paths; current deterministic public contract | Outside supported runtime / historical display; no evidence of a general invalidity finding |
| Dual tetrahedra/throat mapping | Numerical plotting formula recovered; no current GeometryRecord | Historical visualization; reason for not porting unknown |
| Softened Newton three-body probe | Separate optional CLI explicitly states no Ω feedback | Experimental external probe not reconstructed; not evidence of derived gravity |
| Curvature/regression χ_geom² | E explicitly calls it a diagnostic, not recovered physical potential | Experimental/history-only; physical reading unsupported, arithmetic not blanket rejected |
| Empirical gcrit/power-law/plasticity maps | Finite horizon and threshold-dependent scripts | Historical analysis; current sweep infrastructure differs; no proof they were abandoned as “bad math” |
| Constants selector scaling claim | Direct homogeneity contradicts literal scale-invariant doc statement | Specific weak claim identified; normalized ratios and recoverable formulas still distinct |
| Reduced Jacobian as a full stability criterion | Old approximation omits heterogeneous complex/phase composition | Limited/weak if used as a general criterion; exact L3 spectrum remains valid; A/F use qualified analysis |
| RSB angular mask resolving M anisotropy | Sampled cos(Mθ_m)=1 | Documented deliberately global phase coupling, not a resolved anisotropy; no algorithm changed |
| “Magnetic field” or Maxwell solver | Not found in old source census; K4A excludes EM/RS interpretations | Not found as implementation; do not invent an omitted field solver |
| Nested recursive spatial shell / Twisted Hex Crystal | No generator found in OLD; current research-only name documented | Not found in old code; separately deliberately excluded current research concept |
| EMA readout in this OLD model | z_mem field exists but no update consumes it | Not implemented in this snapshot; current EMA has its separately documented provenance |
| Tests, golden records and old provenance | Old implementations overlap with newer record contract | Historical duplicate/replaced purpose; preserved sources are not certified by this census |

No component was classified as rejected merely because it is absent from v0.1. No current C01/D03 geometry equation was inferred to have been present in an old torus/tetrahedron program simply from the “Tri-Octagon” name.

## 8. Source integrity, execution limits, tests and retained evidence

The following are static findings with precise scope; they were not repaired or exercised:

1. The four direct-file UI bootstraps set `__package__='kernel'` and import `kernel`, while the inspected directory is named `kernel_TO`. Other scripts mix bare and relative imports. A supplied package wrapper or historical directory layout may have resolved this; this snapshot alone does not prove an unchanged direct launch.
2. `run_patch39_unified.py:109` assigns `params.lambda_phase` before local `params` is constructed on110. `run_unified_diagnostics.py:123–125` has the opposite, coherent order. Both sources are preserved separately.
3. Unified runners refer to `write_trajectory_log`, whereas the inspected `trajectory_logging.py` defines `TrajectoryLogger`, not that function. The import/call contract does not close in this source set.
4. Several RSB demo/scan scripts seek RSB analysis helpers from `diagnostics.py`, whereas their inspected definitions live in `definitions.py`. The old README also attributes them to diagnostics. Do not treat README module ownership as more authoritative than source.
5. The noise-robustness diagnostic imports `sample_physics_observables` from `physics_sampler2`, where that function is not defined; its owner is `physics_sampler`.
6. T's halo consumes `band_energy_series`, absent from the dictionary returned by the analyzed RSB helper, which supplies `E_t_m`. Intended ring geometry and actual supplied data are different evidence levels.
7. T's recursive `_vrec_geom` fallback and timing-text refresh differences are recorded in section5. They were not demonstrated by a live GUI run.
8. `phase_triad_experiment.ModelAdapter.reset/step` raise `NotImplementedError`; this is a protocol skeleton, not a complete stand-alone evolution implementation.
9. `run_suite.ps1` scans coherence thresholds .8,1.0,1.2 while |mean exp(3iφ)|≤1 in exact arithmetic. A threshold1.2 makes coherent acceptance impossible for finite exact phases; it may be an intended negative control. The suite also varies dt/steps at fixed labelled total time while M01 has no dt multiplier. This changes the number of discrete updates, not just an integration resolution.
10. Golden tests compare expected-failure and finite cases under local conventions; failure/NaN matching is a reproducibility check, not validation of nonfinite states as mathematics. No tests were run in this task.

Known test/example evidence: `select_golden_points.py` selects stable/edge/failure cases; `generate_golden_refs.py` produces NPZ histories and JSON references. Both `golden/` and `old_golden/` are retained. `run_tests.py` and `new_run_tests.py` check schema/determinism/reference comparisons; the newer script checks sampler J at 1e−12 tolerance, direction-angle/chord equivalence on masked unit vectors at 5e−7, and golden v_rec at rtol1e−5/atol1e−7. It skips or masks expected failure/near-zero direction cases according to its conditions. These are observed source checks, **not current PASS results**. README's button checklist is a historical manual test example. RSB demos, `run_sim`, parameter scans, the structural probe README, and `run_suite.ps1` are executable examples subject to the source limits above.

Saved evidence inventory contains CSV summaries/time series, 35 NPZ archives, plot PNG/PDFs, JSON configurations/golden references and diagnostic text. It was not regenerated. File presence does not supply original environment/commit attribution or establish that a source currently matches every saved figure. The full path/hash inventory below permits later selection without silently rewriting history.

## 9. Questions for Hilmir

These questions concern intent/provenance, not requests for code changes. Their number is the closing QUESTIONS_FOR_HILMIR count.

1. In `constants_selector.theta_value`, what selected the three constant pairs and normalization? Was scale invariance intended for θ itself or only ratios? The implemented θ scales as1/s.
2. What were the intended roles of .618, .577 and .244 in `ModelParams`? Were they measured/fitted values, convenient literals, or mnemonic approximations? Which evidence should govern any later interpretation?
3. The L/U viewers select `theta_scaled`, while B/T select `theta_soft`. Were these deliberately different experiments, or successive preferred defaults? Which historical screenshots belong to each?
4. All four “noise σ” sliders perturb κ/z/J after Ω evolution. Did you intend synthetic measurement noise, or did you expect them to drive Ω? The separate `omega_noise_sigma` is not that control.
5. `GapGate` defaults to24 sectors while `ModelParams.d24_steps` defaults to12; unified runners configure gate N without passing it into ModelParams. Was a half-turn gate scan intended, or is another historical configuration missing?
6. The gap-width test uses the supplied width as a halfwidth. Do old notes/screenshots quote full angular aperture or this halfwidth, and were gate centers intended to be D03 cells or only phase thresholds?
7. What did “CP” mean for `CPWindowConfig(centers=(3,9),half_width=1)` and for the cubic J helper? Was it a mnemonic or a proposed symmetry statement distinct from the raw quadratic C?
8. `su3_basis.project_to_uxy` is a real projection of normalized three-channel intensities. Did “SU(3)” refer only to this chosen basis/triangle, or to a larger generator construction missing from this tree?
9. `detect_tangent_corridors` compares the first two uxy coordinates `(c_u,c_x)`, with c_u constant for normalized nonzero input. Was the intended plane `(c_x,c_y)`, or was the existing pair deliberate?
10. Which quantity did you intend “v_rec” to name in each experiment: full composite M13, origin-direction M14, polyline turning M15, or entropy change M16? Their thresholds and units cannot be transferred unchanged.
11. T's percentile Z overlay independently scales total/macro/chiral histories. Were visual magnitude comparisons intended between those selections, or only within each selected path?
12. `embed_on_torus` fixes three major azimuths and moves each channel around its own tube section. Was that construction meant solely as a phase display, or was there an intended spatial dictionary to octagon edges/gaps that is stored elsewhere?
13. T's halo requests `band_energy_series` while the RSB helper returns `E_t_m`. Which source version produced the halo you remember, and are example captures/configurations available in the retained archive?
14. RSB explicitly documents `cos(M*theta_m)` as a deliberately constant/global μ coupling. Should that documented choice govern the historical scientific interpretation, or did an earlier experiment use a resolved modulation not present here?
15. RSB documents its unused Gaussian `band_mask` as available for diagnostics or alternative rules, while the core contracts with a hard dominant-band projector. Did any historical result rely on the reserved smooth alternative in a different source?
16. What motivated the Tri→RSB affine rules for α_eff, μ_eff and γ_eff? Were they an experiment-design convenience, an empirical fit, or intended as a derived coupling?
17. In U, single RSB uses the selected seed and triad conditioning, whereas α sweep fixes seed0/μ=.6/γ=.2. Was this controlled comparison deliberate, and which interpretation belongs to sweep labels?
18. Do the RSB class I/II/III and fast/slow collapse labels designate observed finite traces only, or was there a separate dynamical proof/criterion outside this code?
19. Was `DualTetraConfig`'s throat-radius normalization a visual framing choice, or did the two opposite tetrahedra have an intended state/transition meaning not encoded here?
20. `latent_foreclosure` evolves perturbed clones with its default dt while callers shown do not forward run dt. Which time scale was intended for option-volume comparisons, and is the corridor intended in raw T coordinates?
21. The seed trajectory classifier treats every default history shorter than200 samples as grazing. Is that a conservative application policy or a scientific orbit criterion you intended to preserve?
22. In the structural three-body probe, events reset velocity even after gravity switches on. Was gravity an explicitly independent stress test, and should any old gravitational interpretation be traced to a different program?
23. In `chirality_lab`, χ_geom is fit to the same history's |J| and U_geom=χ_geom². Was this only a visual regression, or is an independent potential derivation missing from the archive?
24. Which package layout/source revision resolves the `kernel` imports, `write_trajectory_log` references, and RSB helper ownership? Were these files collected from several evolving snapshots?
25. Why was `ModelState.z_mem` added without being used here? Was there another EMA-enabled branch, and what establishes its relationship to the source reconstructed in Paper E?
26. In `run_suite.ps1`, was coherence_min1.2 intended as a never-pass control, and was fixed dt×steps intended as a physical-time comparison despite a dt-independent discrete map?
27. Are the identity labels and semantic axis names intended strictly for TORMENT memory routing, or did you attach an additional scientific meaning that should be documented separately?
28. Is there a specific missing historical source for nested geometry, magnetic/RS fields, or Twisted Hex Crystal behavior? None of those evolution/geometry generators was found among these89 old Python modules.

## Appendix A. Complete significant old-source/module census

Each entry supplies purpose and role, major definitions with original line numbers/signatures, state/configuration fields, parameters, dependencies, outputs, static consumers and known test/example links. Registry references supply full mathematical meaning. Function signatures and dataclass fields are source evidence, not revised API proposals. Import-graph reachability denotes a possible dependency, not proof that a callback executes it. Top-level/file-writing scripts are identified by their actual output sites; no such writes were invoked.

### A01. [__init__.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/__init__.py) — 1 lines

**Role/purpose:** Utilities. Package marker; no evolution or geometry.

**Mathematics:** —. **Outputs:** Package import boundary only.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** None.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A02. [analysis_core.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_core.py) — 19 lines

**Role/purpose:** Analysis. Small convergence and identity-scatter extraction helpers.

**Mathematics:** M50. **Outputs:** Absolute kappa gradient and kappa/z/identity arrays.

**Major classes/functions and signature parameters:** `convergence_speed(history) @ 4`; `scatter_identity_kz(history) @ 14`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A03. [analysis_runner.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_runner.py) — 18 lines

**Role/purpose:** Evolution orchestration. Constructs a model and history for analysis consumers.

**Mathematics:** M01–M07. **Outputs:** Model history dictionary.

**Major classes/functions and signature parameters:** `run_model(mode='theta_soft', alpha=1.0) @ 7`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `constants_selector`, `geometry_embeddings`, `model_core`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A04. [analysis_tools.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analysis_tools.py) — 270 lines

**Role/purpose:** Visualization / geometry. Plots scalar histories, direct vectors, CP splits and dual tetrahedra; later geometry_3d imports shadow same-named embedding helpers.

**Mathematics:** M31–M33,M36,M12. **Outputs:** Matplotlib figures for histories and 3D trajectories.

**Major classes/functions and signature parameters:** `plot_history(history) @ 12`; `plot_trajectory_3d(history) @ 46`; `plot_torus_trajectory_3d(history, R: float=2.0, r_max: float=1.0) @ 71`; `plot_Zvec_trajectory_3d(history, key: str='Z_total') @ 93`; `plot_Z_components_trajectory_3d(history) @ 119`; `plot_kappa_z_scatter(history) @ 148`; `plot_kappa_z_cp_scatter(history) @ 169`; `plot_dual_tetra_trajectory(history) @ 196`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `cp_windows`, `dual_tetra_mapper`, `geometry_3d`, `geometry_embeddings`, `matplotlib.pyplot`, `mpl_toolkits.mplot3d`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_sim.py`

**Known tests/examples (static reachability):** `run_sim.py` No execution claimed.

### A05. [analyze_big_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_big_scan.py) — 171 lines

**Role/purpose:** Analysis. Bins broad-scan outcomes, stable fractions and observed tradeoff frontiers.

**Mathematics:** M43,M44. **Outputs:** Heatmap figures and selected edge candidate tables.

**Major classes/functions and signature parameters:** `first_existing(df, cols) @ 13`; `stable_mask(df) @ 19`; `log_bins(vmin, vmax, n=40) @ 28`; `lin_bins(vmin, vmax, n=40) @ 33`; `frac_stable_heatmap(df, xcol, ycol, xlog=True, ylog=False, nx=50, ny=50, title='') @ 36`; `tradeoff_curve_max_y_given_x(df, xcol, ycol, xlog=True, nbins=30, title='') @ 80`; `export_edge_of_chaos(df, eps_col, g_col, k3_col, vcol, top_n=200) @ 119`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `CSV_PATH = 'outputs/wide_scan_triocta_big.csv' @ 8`; `OUT_DIR = 'outputs/scan_analysis' @ 9`; `df = pd.read_csv(CSV_PATH) @ 135`; `eps = first_existing(df, ['eps', 'epsilon']) @ 137`; `g = first_existing(df, ['g', 'g_cpl', 'coupling_g']) @ 138`; `k3 = first_existing(df, ['k3_scale', 'k3', 'k3_well_scale']) @ 139`; `vcol = first_existing(df, ['vrec_mean', 'v_rec_mean', 'vrec_max', 'v_rec_max']) @ 140`; `p1 = frac_stable_heatmap(df, eps, g, xlog=True, ylog=False, nx=60, ny=60, title='Stable fraction: eps vs g') @ 150`; `p2 = frac_stable_heatmap(df, eps, k3, xlog=True, ylog=False, nx=60, ny=60, title='Stable fraction: eps vs k3_scale') @ 154`; `t1 = tradeoff_curve_max_y_given_x(df, eps, g, xlog=True, nbins=35, title='Tradeoff: max stable g vs eps') @ 159`; `t2 = tradeoff_curve_max_y_given_x(df, eps, k3, xlog=True, nbins=35, title='Tradeoff: max stable k3_scale vs eps') @ 163`; `edge_csv = export_edge_of_chaos(df, eps, g, k3, vcol, top_n=250) @ 168`

**Dependencies (static imports):** `matplotlib.pyplot`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `plt.savefig(out, dpi=200, bbox_inches='tight') @ 76`; `plt.savefig(out, dpi=200, bbox_inches='tight') @ 112`; `curve.to_csv(csv_out, index=False) @ 116`; `d[cols].to_csv(out, index=False) @ 131`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A06. [analyze_emission_entropy.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_emission_entropy.py) — 65 lines

**Role/purpose:** Analysis. Normalizes emitted channel counts and aggregates Shannon entropy by lambda.

**Mathematics:** M54. **Outputs:** Enriched summary CSV and printed per-lambda tables.

**Major classes/functions and signature parameters:** `shannon_entropy(p: np.ndarray) @ 6`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `SUMMARY = 'outputs_patch39_unified/summary.csv' @ 4`; `df = pd.read_csv(SUMMARY) @ 16`; `emit_total = df['emit_events_total'].clip(lower=1) @ 19`; `df['R_channels_per_event'] = (df['emit_ch0'] + df['emit_ch1'] + df['emit_ch2']) / emit_total @ 20`; `p = np.vstack([(df['emit_ch0'] / emit_total).to_numpy(), (df['emit_ch1'] / emit_total).to_numpy(), (df['emit_ch2'] / emit_total).to_numpy()]).T @ 24`; `row_sum = p.sum(axis=1, keepdims=True) @ 31`; `p_norm = np.where(row_sum > 0, p / row_sum, 0.0) @ 32`; `df['H_channels'] = [shannon_entropy(row) for row in p_norm] @ 34`; `df['H_channels_bits'] = df['H_channels'] / np.log(2.0) @ 35`; `df['H_max_nats'] = np.log(3.0) @ 38`; `df['H_max_bits'] = np.log(3.0) / np.log(2.0) @ 39`; `out = SUMMARY.replace('.csv', '_with_R_entropy.csv') @ 58`; `top = df.sort_values('H_channels', ascending=False).head(10) @ 63`

**Dependencies (static imports):** `numpy`, `pandas`.

**Recorded/file output sites:** `df.to_csv(out, index=False) @ 59`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A07. [analyze_emission_R.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_emission_R.py) — 65 lines

**Role/purpose:** Analysis. Computes emission participation ratios from stored counts.

**Mathematics:** M54. **Outputs:** Per-run/per-lambda printed statistical summaries.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `SUMMARY = 'outputs_patch39_unified/summary.csv' @ 4`; `df = pd.read_csv(SUMMARY) @ 6`; `emit_total = df['emit_events_total'].clip(lower=1) @ 9`; `df['R_channels_per_event'] = (df['emit_ch0'] + df['emit_ch1'] + df['emit_ch2']) / emit_total @ 11`; `df['p_ch0'] = df['emit_ch0'] / emit_total @ 14`; `df['p_ch1'] = df['emit_ch1'] / emit_total @ 15`; `df['p_ch2'] = df['emit_ch2'] / emit_total @ 16`; `baseline = df[df['lambda_phase'] == 0.0][['seed', 'R_channels_per_event', 'emit_events_total']].rename(columns={'R_channels_per_event': 'R0', 'emit_events_total': 'E0'}) @ 33`; `out = SUMMARY.replace('.csv', '_with_R.csv') @ 63`

**Dependencies (static imports):** `numpy`, `pandas`.

**Recorded/file output sites:** `df.to_csv(out, index=False) @ 64`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A08. [analyze_event_window_entropy.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_event_window_entropy.py) — 65 lines

**Role/purpose:** Analysis. Computes channel entropy inside grouped event windows.

**Mathematics:** M54. **Outputs:** Printed/event-window statistics from saved events.

**Major classes/functions and signature parameters:** `shannon_entropy(p: np.ndarray) @ 8`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `OUTDIR = 'outputs_patch39_unified' @ 5`; `WINDOW = 2000 @ 6`; `rows = [] @ 17`; `df = pd.DataFrame(rows) @ 51`; `out = f'{OUTDIR}/window_entropy.csv' @ 52`

**Dependencies (static imports):** `glob`, `numpy`, `pandas`.

**Recorded/file output sites:** `df.to_csv(out, index=False) @ 53`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A09. [analyze_rgd_rows.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_rgd_rows.py) — 233 lines

**Role/purpose:** Analysis. Aggregates per-seed scan rows, failure rates and confidence intervals.

**Mathematics:** M42–M44. **Outputs:** Aggregate CSV and summary tables.

**Major classes/functions and signature parameters:** `wilson_ci(k: int, n: int, z: float=1.96) @ 41`; `bootstrap_mean_ci(x: np.ndarray, n_boot: int=5000, alpha: float=0.05, seed: int=12345) @ 51`; `safe_float_series(df: pd.DataFrame, col: str) @ 65`; `main() @ 72`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `POINT_KEYS = ['eps', 'g', 'k3_scale', 'dt', 'n_steps', 'noise_sigma', 'do_rsb', 'rsb_steps', 'version', 'point_index'] @ 36`

**CLI controls/defaults:** `ap.add_argument('--rows', required=True, help='Path to ..._rows.csv') @ 74`; `ap.add_argument('--out', default='', help='Optional output aggregated CSV path') @ 75`; `ap.add_argument('--top', type=int, default=20, help='How many worst points to print') @ 76`; `ap.add_argument('--no-postagg', action='store_true', help='Do not write post-aggregation CSV') @ 77`

**Dependencies (static imports):** `__future__`, `argparse`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `agg.to_csv(out_path, index=False) @ 226`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A10. [analyze_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_scan.py) — 69 lines

**Role/purpose:** Analysis. Summarizes stored sweep regimes and finite/stable subsets.

**Mathematics:** M43. **Outputs:** Printed parameter summaries and selected comparisons.

**Major classes/functions and signature parameters:** `stable_mask(d) @ 15`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `CSV_PATH = 'outputs/wide_scan_triocta.csv' @ 4`; `df = pd.read_csv(CSV_PATH) @ 6`; `flag_cols = [c for c in df.columns if any((k in c.lower() for k in ['nan', 'blow', 'runaway', 'unstable', 'completed']))] @ 12`; `stable = stable_mask(df) @ 33`; `num = df.select_dtypes(include=[np.number]).copy() @ 38`; `num['is_stable'] = stable.astype(int) @ 39`; `corr = num.corr(numeric_only=True)['is_stable'].drop('is_stable').sort_values() @ 42`; `vcol = None @ 50`

**Dependencies (static imports):** `numpy`, `pandas`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A11. [analyze_seed_trajectories.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_seed_trajectories.py) — 67 lines

**Role/purpose:** AI-memory analysis. Aggregates stored seed escape/return/grazing classes against lambda.

**Mathematics:** M29. **Outputs:** Summary/class-fraction table from trajectory CSV.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `BASE = Path('outputs_patch39_unified') @ 5`; `OUT_CSV = BASE / 'trajectory_class_summary.csv' @ 6`; `files = sorted(BASE.glob('lambda_*/seed_trajectories_seed*.csv')) @ 9`; `frames = [] @ 14`; `df = pd.concat(frames, ignore_index=True) @ 20`; `df = df[df['traj_class'].notna()] @ 23`; `df = df[df['traj_class'] != 'unknown'] @ 24`; `counts = df.groupby(['lambda_phase', 'channel', 'traj_class']).size().reset_index(name='count') @ 27`; `totals = counts.groupby(['lambda_phase', 'channel'])['count'].sum().reset_index(name='total') @ 34`; `summary = counts.merge(totals, on=['lambda_phase', 'channel'], how='left') @ 41`; `summary['fraction'] = summary['count'] / summary['total'] @ 46`; `summary = summary.sort_values(['lambda_phase', 'channel', 'traj_class']) @ 49`; `pivot = summary.pivot_table(index=['lambda_phase', 'channel'], columns='traj_class', values='fraction', fill_value=0.0) @ 60`

**Dependencies (static imports):** `pandas`, `pathlib`.

**Recorded/file output sites:** `summary.to_csv(OUT_CSV, index=False) @ 54`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A12. [analyze_threebody_probe.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/analyze_threebody_probe.py) — 228 lines

**Role/purpose:** Experimental physics analysis. Loads body-world output; compares event/gravity conditions and ray distances.

**Mathematics:** M45,M46. **Outputs:** Printed group statistics and analysis plot files; CP1252 source decoding.

**Major classes/functions and signature parameters:** `circ_diff(a: np.ndarray, b: np.ndarray) @ 26`; `safe_group_stats(x: np.ndarray) @ 32`; `main() @ 49`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('run_dir', type=str, help='outputs/threebody_probe/<run_id>') @ 51`; `ap.add_argument('--ray_thresh_deg', type=float, default=10.0, help="counts as 'aligned' if sixray_dist <= thresh (deg)") @ 52`; `ap.add_argument('--make_plots', action='store_true') @ 54`

**Dependencies (static imports):** `__future__`, `argparse`, `json`, `matplotlib.pyplot`, `numpy`, `pandas`, `pathlib`.

**Recorded/file output sites:** `json.dump(summary, f, indent=2) @ 176`; `plt.savefig(analysis_dir / 'sixray_dist_hist.png', dpi=160) @ 193`; `plt.savefig(analysis_dir / 'alignment_rate_over_time.png', dpi=160) @ 212`; `plt.savefig(analysis_dir / 'dv_vs_sixray.png', dpi=160) @ 222`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A13. [c.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/c.py) — 4 lines

**Role/purpose:** Utilities / analysis. Four-line convenience reader for a saved scan CSV.

**Mathematics:** M43. **Outputs:** Printed fraction of finite/stable rows.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `df = pd.read_csv('outputs/wide_scan_triocta_ultra.csv') @ 2`

**Dependencies (static imports):** `numpy`, `pandas`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A14. [chirality_lab.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/chirality_lab.py) — 916 lines

**Role/purpose:** Experimental analysis / visualization. Fits J from vector geometry and examines pulses, curvature, torsion and lags.

**Mathematics:** M15,M40,M41. **Outputs:** Coefficient dictionaries, correlations, regressions and diagnostic figures.

**Major classes/functions and signature parameters:** `finite_diff(x, t) @ 34`; `detect_torsion_pulses(J, t, use_sign_flip=True, dJ_thresh=None) @ 50`; `build_big_steps_mask_from_kappa_z(history, frac_of_max=0.5) @ 99`; `lagged_corr(x, y, max_lag_steps=10, name_x='X', name_y='Y') @ 133`; `fit_jeff_from_z(history, obs, key='Z_vec') @ 187`; `fit_jeff_nonlinear_from_z(history, obs, key='Z_vec') @ 227`; `compute_frenet_invariants(history, key='Z_vec') @ 288`; `fit_chirality_curvature_index(history, obs, key='Z_vec') @ 359`; `scatter_J_vs_chi_geom(history, obs, coeffs, key='Z_vec', title_suffix='') @ 446`; `analyze_sign_branches_over_chi(history, obs, coeffs, key='Z_vec') @ 515`; `analyze_geometric_torsion_coupling(history, obs, key='Z_vec') @ 654`; `analyze_lagged_geometry_to_chirality(history, obs, key='Z_vec', max_lag_steps=10) @ 721`; `run_chirality_lab(history, obs, big_steps_mask=None) @ 790`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `diagnostics`, `geometry_3d`, `matplotlib.pyplot`, `mpl_toolkits.mplot3d`, `numpy`, `run_sim`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A15. [chirality_param_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/chirality_param_scan.py) — 198 lines

**Role/purpose:** Analysis orchestration. Runs parameter/seed grid and classifies chirality sign/flip histories.

**Mathematics:** M08,M17,M43. **Outputs:** Per-run chirality metrics and CSV/plot summaries.

**Major classes/functions and signature parameters:** `run_single(params: ModelParams, seed: int, n_steps: int=200, dt: float=0.05) @ 13`; `classify_run(J: np.ndarray, eps_zero: float=1e-06) @ 29`; `main() @ 75`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `constants_selector`, `csv`, `model_core`, `numpy`, `physics_sampler`.

**Recorded/file output sites:** `writer.writerow(row) @ 192`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A16. [classify_nan_logs_v3.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/classify_nan_logs_v3.py) — 51 lines

**Role/purpose:** Diagnostics. Categorizes saved nonfinite-forensics JSON logs by observed failure location/type.

**Mathematics:** M43. **Outputs:** Failure-category table/console report.

**Major classes/functions and signature parameters:** `classify(report) @ 11`; `classify_directory(dir_path) @ 29`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `collections`, `json`, `pathlib`, `sys`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A17. [collect_optional_suite.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/collect_optional_suite.py) — 137 lines

**Role/purpose:** Analysis. Parses run-folder parameter names and aggregates event-to-ray alignment.

**Mathematics:** M44,M46. **Outputs:** Combined optional-suite CSV/summary rows.

**Major classes/functions and signature parameters:** `p_to_float(s: str) @ 17`; `parse_folder(name: str) @ 20`; `wrap_pi(x: np.ndarray) @ 32`; `nearest_ray_distance_rad(theta: np.ndarray, n_rays: int=6) @ 35`; `summarize_event_alignment(events_df: pd.DataFrame) @ 42`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `ROOT = Path('outputs_dt_optional_suite') @ 8`; `AGG = ROOT / '_aggregated' @ 9`; `FOLDER_RE = re.compile('dt_(?P<dt>\\d+p\\d+)_steps_(?P<steps>\\d+)_gap_(?P<gap>\\d+)_coh_(?P<coh>OFF\|ON)(?:_cmin_(?P<cmin>\\d+(?:p\\d+)?))?$') @ 13`; `summary_rows = [] @ 66`; `ray_rows = [] @ 67`; `folders = sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name != '_aggregated']) @ 69`

**Dependencies (static imports):** `__future__`, `numpy`, `pandas`, `pathlib`, `re`.

**Recorded/file output sites:** `summary_all.to_csv(AGG / 'summary_all.csv', index=False) @ 127`; `ray_all.to_csv(AGG / 'ray_event_alignment_all.csv', index=False) @ 134`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A18. [constants_selector.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/constants_selector.py) — 116 lines

**Role/purpose:** Constants / configuration. Owns mathematical constants and three alternative coefficient triplet selectors.

**Mathematics:** M04,M51. **Outputs:** CoreConstants object, k arrays, constants dictionary.

**Major classes/functions and signature parameters:** `class CoreConstants @ 10`; `get_core_constants() @ 18`; `theta_value(Ci: float, Cj: float) @ 34`; `theta_soft_triplet(alpha: float=1.0) @ 41`; `theta_triplet_scaled() @ 61`; `simple_hand_tuned_triplet() @ 81`; `default_k_triplet(mode: str='theta_scaled', alpha: float=1.0) @ 88`; `constants_dict() @ 103`

**State/configuration objects:** `CoreConstants: pi: float @ 11`; `CoreConstants: phi: float @ 12`; `CoreConstants: e: float @ 13`; `CoreConstants: sqrt3: float @ 14`; `CoreConstants: euler_gamma: float @ 15`; `CoreConstants: apery_zeta3: float @ 16`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `dataclasses`, `math`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_runner.py`, `chirality_param_scan.py`, `model_core.py`, `param_scan.py`, `plasticity_map.py`, `rgd_connection_diagnostics.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_unified_diagnostics.py`, `toy_3d_triocta.py`, `toy_lab.py`, `toy_ui.py`, `toy_ui_live.py`, `wide_scan_triocta.py`, `z_spike_diagnostic.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A19. [cp_windows.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/cp_windows.py) — 47 lines

**Role/purpose:** Configuration / analysis. Defines cyclic window centers/width and sector mask.

**Mathematics:** M12. **Outputs:** CPWindowConfig and Boolean history mask.

**Major classes/functions and signature parameters:** `class CPWindowConfig @ 7`; `cp_mask_from_phi_indices(phi_indices: np.ndarray, cfg: CPWindowConfig) @ 20`; `default_cp_config() @ 38`

**State/configuration objects:** `CPWindowConfig: center_indices: Sequence[int] @ 16`; `CPWindowConfig: half_width: int = 1 @ 17`; `CPWindowConfig: n_sectors: int = 12 @ 18`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `dataclasses`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_tools.py`, `diagnostics.py`, `physics_sampler2.py`, `semantic_diagnostics.py`, `tangent_corridor_analysis.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_sim.py` No execution claimed.

### A20. [definitions.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/definitions.py) — 899 lines

**Role/purpose:** Passive diagnostics / analysis. Canonical old cubic J and multiple recursive-velocity definitions; RSB observables and labels.

**Mathematics:** M08,M13–M18,M23,M24. **Outputs:** Observable arrays, masks, timing summaries, regimes and formatted seed summaries.

**Major classes/functions and signature parameters:** `compute_jeff_from_omega(Omega: np.ndarray) @ 22`; `compute_jeff_series(hist: dict) @ 30`; `chirality_sign(j: float, deadband: float=1e-09) @ 50`; `count_sign_flips(j_series: np.ndarray, deadband: float=1e-09) @ 57`; `estimate_chirality_commit_time(j_series: np.ndarray, frac: float=0.9, deadband: float=1e-09) @ 67`; `jeff_radius_stats(j_series: np.ndarray) @ 97`; `vrec_entropy(H_series: np.ndarray) @ 109`; `vrec_geom_direction(hist: dict, z_key: str='Z_total', norm_floor: float=1e-09) @ 117`; `estimate_chirality_timescale(t, J) @ 148`; `estimate_z_stabilization_time(hist: dict, z_key: str='Z_total', settle_deg: float=15.0, min_norm: float=1e-10, tail: int=30) @ 181`; `compute_spectral_energy_series(psi_hist: np.ndarray) @ 240`; `_wrap_angle_pi(x: np.ndarray) @ 259`; `compute_recursive_velocity_geom(hist: dict, z_key: str='Z_total', w_z: float=1.0, w_phase: float=1.0, w_corridor: float=0.5, w_kappa: float=0.0, return_components: bool=False) @ 263`; `compute_recursive_velocity(H_series: np.ndarray) @ 340`; `classify_run(d, sigma_spec, h, eps_d: float=0.03, delta_d: float=0.001, delta_spec: float=0.001, delta_h: float=0.001, sigma_min: float=0.1, sigma_max: float=0.9, sigma_coll: float=0.1, h_small: float=0.1, h_edge: float=0.1) @ 354`; `compute_dominant_band_series(E_t_m: np.ndarray) @ 464`; `compute_spectral_entropy_series(E_t_m: np.ndarray) @ 476`; `compute_rsb_observables(psi_hist: np.ndarray, chan_axis: int=1, phase_axis: int=2, hel_axis: int=3, dark_channels: tuple=(1, 2)) @ 502`; `analyze_rsb_history(psi_hist: np.ndarray, chan_axis: int=1, phase_axis: int=2, hel_axis: int=3, dark_channels: tuple=(1, 2), verbose: bool=True, seed=None, **classify_kwargs) @ 596`; `summarize_rsb_seed(rsb_stats, t=None, frac=0.1, seed=None) @ 754`; `format_rsb_seed_summary(summary) @ 859`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `EPS = 1e-12 @ 20`

**Dependencies (static imports):** `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `diagnostics.py`, `edge_map.py`, `explore_sweep.py`, `generate_golden_refs.py`, `new_run_tests.py`, `physics_sampler.py`, `physics_sampler2.py`, `plasticity_map.py`, `rgd_connection_diagnostics.py`, `rsb_spectral_viz.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_tests.py`, `run_unified_diagnostics.py`, `sanity_report.py`, `side_zchiral_probe.py`, `toy_3d_triocta.py`, `toy_lab.py`, `toy_ui.py`, `toy_ui_live.py`, `wide_scan_triocta.py`, `z_spike_diagnostic.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_tests.py`, `run_unified_diagnostics.py` No execution claimed.

### A21. [diagnose_bottom_lid.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/diagnose_bottom_lid.py) — 272 lines

**Role/purpose:** Diagnostics / visualization. Trims to finite prefix, compares macro/chiral/total alignment and scalar/cycle traces.

**Mathematics:** M06,M07,M33. **Outputs:** NPZ/CSV diagnostics and alignment figures.

**Major classes/functions and signature parameters:** `_ensure_dir(path: str) @ 32`; `_finite_prefix_mask(*arrays: np.ndarray) @ 36`; `_trim_to_finite_prefix(t: np.ndarray, *series: np.ndarray) @ 49`; `plot_alignment_diagnostics(history: Dict[str, Any], out_png: str, title: str) @ 63`; `summarize_run(history: Dict[str, Any]) @ 123`; `main() @ 168`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--seeds', nargs='+', type=int, required=True) @ 170`; `ap.add_argument('--steps', type=int, default=2000) @ 171`; `ap.add_argument('--dt', type=float, default=0.02) @ 172`; `ap.add_argument('--out', type=str, default='out_alignment') @ 173`; `ap.add_argument('--g', type=float, default=0.667) @ 176`; `ap.add_argument('--eps', type=float, default=0.003) @ 177`; `ap.add_argument('--k3', type=float, default=1.0) @ 178`; `ap.add_argument('--lam', type=float, default=0.0) @ 179`; `ap.add_argument('--phi_step', type=int, default=1) @ 180`; `ap.add_argument('--z_alpha', type=float, default=1.0) @ 183`; `ap.add_argument('--z_beta', type=float, default=0.5) @ 184`

**Dependencies (static imports):** `__future__`, `argparse`, `csv`, `matplotlib.pyplot`, `model_core`, `numpy`, `os`, `typing`.

**Recorded/file output sites:** `plt.savefig(out_png, dpi=160) @ 93`; `plt.savefig(out_png2, dpi=160) @ 106`; `plt.savefig(out_png3, dpi=160) @ 119`; `np.savez_compressed(npz_path, t=t, dot_vec_macro=d_vm, dot_chiral_macro=d_cm, dot_vec_chiral=d_vc, macro_minus_chiral=macro_minus, z=np.asarray(hist['z'], dtype=float), kappa=np.as … [see source] @ 247`; `w.writerows(summary_rows) @ 265`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A22. [diagnostics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/diagnostics.py) — 601 lines

**Role/purpose:** Analysis orchestration. Runs initial-condition, sector, J-coupling, long-time and noise studies.

**Mathematics:** M08,M12,M39,M41,M43. **Outputs:** Histories, statistics and plots; not the actual owner of current RSB analysis helpers.

**Major classes/functions and signature parameters:** `run_once(params: ModelParams) @ 36`; `run_ic_scan(params: ModelParams, n_inits: int=32, seed: int=123, verbose: bool=True) @ 85`; `strong_delta_sector_histogram(history, big_steps_mask, cp_cfg=None) @ 170`; `analyze_Jeff_coupling(history, obs, big_steps_mask) @ 235`; `run_corridor_spectroscopy_scan(params: ModelParams, n_inits: int=32, seed: int=321, frac_of_max: float=0.5) @ 323`; `run_long_time_stability_test(params: ModelParams, n_steps: int=2000, dt: float=0.05, seed: int=999, frac_of_max: float=0.5) @ 409`; `run_noise_robustness_test(params, n_steps: int=200, dt: float=0.05, noise_sigma_k: float=0.01, noise_sigma_z: float=0.01, noise_sigma_J: float=0.01, frac_of_max: float=0.5, seed: int=1234) @ 510`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.cp_windows`, `.definitions`, `.model_core`, `.physics_sampler`, `.physics_sampler2`, `.tangent_corridor_analysis`, `model_core`, `numpy`, `physics_sampler2`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `chirality_lab.py`, `rgd_connection_diagnostics.py`, `rsb_dom_band_demo.py`, `rsb_param_scan.py`, `rsb_phase_scan.py`, `rsb_spectral_demo.py`, `run_sim.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_sim.py` No execution claimed.

### A23. [dual_tetra_mapper.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/dual_tetra_mapper.py) — 42 lines

**Role/purpose:** Geometry / visualization. Constructs opposite tetrahedron vertices and whole-history scaled probability path.

**Mathematics:** M36. **Outputs:** Two vertex sets and mapped 3D trajectory.

**Major classes/functions and signature parameters:** `_base_tetra_vertices() @ 5`; `class DualTetraConfig @ 14`; `dual_tetra_vertices(config: DualTetraConfig) @ 18`; `map_history_to_dual_tetra(history, config: DualTetraConfig) @ 22`

**State/configuration objects:** `DualTetraConfig: scale: float = 1.5 @ 15`; `DualTetraConfig: throat_radius: float = 1.0 @ 16`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `dataclasses`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_tools.py`

**Known tests/examples (static reachability):** `run_sim.py` No execution claimed.

### A24. [edge_map.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/edge_map.py) — 335 lines

**Role/purpose:** Analysis orchestration. Evaluates finite behavior and threshold regimes, brackets/bisects coupling per seed.

**Mathematics:** M43. **Outputs:** Empirical critical brackets and metric rows/CSV.

**Major classes/functions and signature parameters:** `make_initial_state(seed: int) @ 22`; `run_once(seed: int, steps: int, dt: float, eps: float, g: float, k3: float) @ 38`; `_finite_mask_complex2d(O: np.ndarray) @ 56`; `_finite_mask_float1d(x: np.ndarray) @ 60`; `first_nonfinite_step(x: np.ndarray) @ 63`; `first_nonfinite_step_Omega(Om: np.ndarray) @ 69`; `min_positive(*vals: int) @ 76`; `slice_finite_prefix(mask: np.ndarray) @ 80`; `safe_stats(x: np.ndarray) @ 91`; `compute_metrics(hist: Dict[str, Any], *, z_key: str='Z_total') @ 103`; `classify_regime(m: Dict[str, Any]) @ 196`; `find_gcrit_for_seed(*, seed: int, eps: float, k3: float, dt: float, steps: int, g_lo: float, g_hi: float, tol: float, iters: int, fail_set: set[str], z_key: str) @ 215`; `main() @ 285`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--seeds', nargs='+', type=int, required=True) @ 287`; `ap.add_argument('--eps', nargs='+', type=float, required=True) @ 288`; `ap.add_argument('--k3', nargs='+', type=float, required=True) @ 289`; `ap.add_argument('--dt', type=float, required=True) @ 290`; `ap.add_argument('--steps', type=int, default=2000) @ 291`; `ap.add_argument('--g_lo', type=float, default=0.64) @ 293`; `ap.add_argument('--g_hi', type=float, default=0.72) @ 294`; `ap.add_argument('--tol', type=float, default=0.0005) @ 295`; `ap.add_argument('--iters', type=int, default=20) @ 296`; `ap.add_argument('--fail', nargs='+', default=['nan_boundary', 'boundary']) @ 298`; `ap.add_argument('--z_key', default='Z_total') @ 299`; `ap.add_argument('--out', default='edge_map.csv') @ 301`

**Dependencies (static imports):** `__future__`, `argparse`, `csv`, `dataclasses`, `definitions`, `model_core`, `numpy`, `typing`.

**Recorded/file output sites:** `w.writerow(r) @ 329`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A25. [eigen_analysis.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/eigen_analysis.py) — 104 lines

**Role/purpose:** Analysis. Computes triangle Laplacian eigensystem and reduced scalar Jacobian estimate.

**Mathematics:** M49. **Outputs:** Matrices/eigenpairs/stability commentary.

**Major classes/functions and signature parameters:** `get_laplacian_3node() @ 8`; `analyze_laplacian() @ 16`; `jacobian_eigs(params: ModelParams, k_ref: float \| None=None) @ 53`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `matplotlib.pyplot`, `model_core`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A26. [explore_sweep.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/explore_sweep.py) — 469 lines

**Role/purpose:** Analysis orchestration. Configurable grids/random samples, finite prefixes, turns, commitment and corridor occupancy.

**Mathematics:** M17,M43. **Outputs:** Sweep CSV rows and finite-run regime metrics.

**Major classes/functions and signature parameters:** `make_initial_state(seed: int) @ 42`; `run_once(seed: int, steps: int, dt: float, eps: float, g: float, k3: float) @ 58`; `_finite_frac(x: np.ndarray) @ 75`; `_safe_stats_1d(x: np.ndarray) @ 82`; `_znorm(hist: Dict[str, Any], key: str) @ 96`; `first_commit_time(J: np.ndarray, t: np.ndarray, thr: float=1e-06, hold: int=50) @ 107`; `turning_angle_p95(Z: np.ndarray) @ 125`; `corridor_entropy(phi_index: np.ndarray, n_corridors: int=12) @ 152`; `first_nonfinite_step(x: np.ndarray) @ 165`; `classify_regime(m: Dict[str, Any]) @ 173`; `compute_metrics(hist: Dict[str, Any], *, n_corridors: int=12) @ 213`; `parse_list_or_none(vals: Optional[List[float]]) @ 325`; `random_samples(rng: np.random.Generator, lo: float, hi: float, n: int, log: bool=True) @ 331`; `main() @ 339`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `EPS = 1e-12 @ 37`

**CLI controls/defaults:** `ap.add_argument('--seeds', type=int, nargs='+', required=True) @ 341`; `ap.add_argument('--steps', type=int, default=2000) @ 342`; `ap.add_argument('--dt', type=float, default=0.03) @ 343`; `ap.add_argument('--n_corridors', type=int, default=12) @ 344`; `ap.add_argument('--eps', type=float, nargs='*') @ 346`; `ap.add_argument('--g', type=float, nargs='*') @ 347`; `ap.add_argument('--k3', type=float, nargs='*') @ 348`; `ap.add_argument('--eps_range', type=float, nargs=2, metavar=('LO', 'HI')) @ 350`; `ap.add_argument('--g_range', type=float, nargs=2, metavar=('LO', 'HI')) @ 351`; `ap.add_argument('--k3_range', type=float, nargs=2, metavar=('LO', 'HI')) @ 352`; `ap.add_argument('--n_random', type=int, default=0) @ 353`; `ap.add_argument('--rand_seed', type=int, default=12345) @ 354`; `ap.add_argument('--out', type=str, default='') @ 356`

**Dependencies (static imports):** `__future__`, `argparse`, `csv`, `definitions`, `math`, `model_core`, `numpy`, `time`, `typing`.

**Recorded/file output sites:** `w.writerow(r) @ 440`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A27. [fit_eps_exponent.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/fit_eps_exponent.py) — 40 lines

**Role/purpose:** Analysis. Fits power exponents by log-log linear regression of saved edge data.

**Mathematics:** M43. **Outputs:** Fitted coefficient/exponent and plot/report.

**Major classes/functions and signature parameters:** `main() @ 5`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--csv', required=True) @ 7`; `ap.add_argument('--x', default='eps') @ 8`; `ap.add_argument('--y', default='t_last_vrec_ge_0.8') @ 9`

**Dependencies (static imports):** `argparse`, `numpy`, `pandas`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A28. [generate_golden_refs.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/generate_golden_refs.py) — 106 lines

**Role/purpose:** Tests / reproducibility. Converts scan parameters to ModelParams and saves selected reference histories.

**Mathematics:** M52. **Outputs:** Golden NPZ arrays and JSON metadata.

**Major classes/functions and signature parameters:** `scan_to_model_params(p) @ 13`; `make_initial_state(seed: int) @ 30`; `run_triocta(p, seed, n_steps=2000) @ 50`; `tail_stats(x, frac=0.5) @ 58`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `IN_JSON = 'golden/golden_points.json' @ 9`; `OUT_JSON = 'golden/golden_refs.json' @ 10`; `golden_points = json.loads(Path(IN_JSON).read_text(encoding='utf-8'))['points'] @ 64`; `refs = [] @ 65`

**Dependencies (static imports):** `definitions`, `json`, `model_core`, `numpy`, `pathlib`.

**Recorded/file output sites:** `Path(OUT_JSON).write_text(json.dumps(refs, indent=2), encoding='utf-8') @ 105`; `np.savez_compressed(npz_path, **bundle) @ 89`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A29. [geometry_3d.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_3d.py) — 78 lines

**Role/purpose:** Geometry / visualization. Cylinder, scalar-history torus and direct-vector coordinate helpers.

**Mathematics:** M31–M33. **Outputs:** Numerical XYZ arrays; fixed12-sector scalar maps.

**Major classes/functions and signature parameters:** `history_to_xyz(history) @ 4`; `history_to_torus_xyz(history, R: float=2.0, r_max: float=1.0) @ 25`; `history_Zvec_to_xyz(history, key: str='Z_total') @ 60`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_tools.py`, `chirality_lab.py`, `plasticity_map.py`, `toy_3d_triocta.py`, `toy_ui.py`, `z_spike_diagnostic.py`

**Known tests/examples (static reachability):** `run_sim.py` No execution claimed.

### A30. [geometry_embeddings.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/geometry_embeddings.py) — 35 lines

**Role/purpose:** Geometry / configuration. Alternate cylinder/torus helper with TorusConfig; only torus uses its N.

**Mathematics:** M31,M32. **Outputs:** Configuration plus XYZ arrays; overlaps geometry_3d with parameter differences.

**Major classes/functions and signature parameters:** `class TorusConfig @ 7`; `history_to_xyz(history) @ 12`; `history_to_torus_xyz(history, config: TorusConfig) @ 19`

**State/configuration objects:** `TorusConfig: R: float @ 8`; `TorusConfig: r_max: float @ 9`; `TorusConfig: n_sectors: int = 12 @ 10`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `dataclasses`, `math`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_runner.py`, `analysis_tools.py`

**Known tests/examples (static reachability):** `run_sim.py` No execution claimed.

### A31. [heatmap_ray_alignment.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/heatmap_ray_alignment.py) — 117 lines

**Role/purpose:** Visualization. Pivots collected alignment metrics across parameters.

**Mathematics:** M44,M46. **Outputs:** Saved heatmaps.

**Major classes/functions and signature parameters:** `_pivot(df: pd.DataFrame, value_col: str, traj_class: str \| None) @ 11`; `_plot_heatmap(pivot: pd.DataFrame, title: str, outpath: str, fmt: str='{:.3f}') @ 31`; `main() @ 66`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `matplotlib.pyplot`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `fig.savefig(outpath, dpi=200) @ 61`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A32. [identity_rules.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/identity_rules.py) — 61 lines

**Role/purpose:** AI-memory configuration. Maps norm-threshold stage and z sign to nine identity labels.

**Mathematics:** M11. **Outputs:** CycleConfig, stage/identity indices and label strings.

**Major classes/functions and signature parameters:** `class CycleConfig @ 7`; `compute_cycle_stage(kappa: float, config: CycleConfig) @ 29`; `map_identity_state(stage: int, z: float, num_states: int=9) @ 38`; `label_for_identity(s: int) @ 55`

**State/configuration objects:** `CycleConfig: kappa_thresholds: np.ndarray @ 14`

**Additional parameters/constants:** `IDENTITY_LABELS: List[str] = ['s0_void_low', 's1_low_posZ', 's2_low_negZ', 's3_mid_low', 's4_mid_posZ', 's5_mid_negZ', 's6_high_low', 's7_high_posZ', 's8_high_negZ'] @ 17`

**Dependencies (static imports):** `dataclasses`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `model_core.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A33. [latent_foreclosure.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/latent_foreclosure.py) — 103 lines

**Role/purpose:** AI-memory diagnostics. Clones current state and samples future perturbed endpoints.

**Mathematics:** M26. **Outputs:** Survival, option radius and covariance-volume diagnostics.

**Major classes/functions and signature parameters:** `clone_state(state) @ 5`; `compute_option_volume(model, state, *, dt=0.1, delta=0.0001, K=5, N=16, eps_corridor=0.05, eps_norm=1.0, rng_seed_base=1337) @ 10`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `copy`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `model_core.py`, `run_unified_diagnostics.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A34. [make_figures.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/make_figures.py) — 529 lines

**Role/purpose:** Visualization / schema adaptation. Accepts varied saved seed/per-step schemas and plots exits, classes, phase/ray/warning relationships.

**Mathematics:** M28,M29,M46. **Outputs:** Schema report and publication-style figures; data-driven, no new evolution law.

**Major classes/functions and signature parameters:** `ensure_dir(p: Path) @ 14`; `_maybe_read_csv(path: Path) @ 17`; `load_across_lambda(root: Path, filename_glob: str) @ 24`; `load_seed_files(root: Path, filename_template: str, seed: int) @ 41`; `pick_first_existing(df: pd.DataFrame, candidates: list[str]) @ 58`; `find_class_col(df: pd.DataFrame) @ 64`; `find_xcol(df: pd.DataFrame) @ 79`; `safe_series(x) @ 94`; `safe_numeric(x) @ 100`; `savefig(path: Path) @ 105`; `write_schema_report(outpath: Path, named_dfs: list[tuple[str, pd.DataFrame]]) @ 110`; `fig_exit_time_vs_param(summary: pd.DataFrame, outdir: Path) @ 127`; `fig_exit_time_distribution_by_param(summary: pd.DataFrame, outdir: Path) @ 164`; `fig_class_fractions(df_in: pd.DataFrame, outdir: Path, tag: str) @ 217`; `fig_theta_span_vs_param(seedtraj: pd.DataFrame, outdir: Path) @ 254`; `fig_phase_instability_vs_param(seedtraj: pd.DataFrame, outdir: Path) @ 280`; `fig_dist_to_ray_vs_theta_span(seedtraj: pd.DataFrame, outdir: Path) @ 311`; `fig_warning_vs_exit(events: pd.DataFrame, outdir: Path) @ 336`; `fig_seed_perstep(perstep: pd.DataFrame, outdir: Path, seed: int) @ 404`; `main() @ 474`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--root', type=str, required=True, help='Path to outputs_patch39_unified') @ 476`; `ap.add_argument('--seed', type=int, default=24, help='Seed id for optional illustrative per-step plots') @ 477`

**Dependencies (static imports):** `argparse`, `matplotlib.pyplot`, `numpy`, `pandas`, `pathlib`, `re`.

**Recorded/file output sites:** `plt.savefig(path, bbox_inches='tight') @ 107`; `outpath.write_text('\n'.join(lines), encoding='utf-8') @ 120`; `savefig(outdir / 'exit_time_vs_param.pdf') @ 162`; `savefig(outdir / 'exit_time_distribution_by_param.pdf') @ 215`; `savefig(outdir / f'class_fractions_{tag}_vs_{xcol}.pdf') @ 252`; `savefig(outdir / 'theta_unwrapped_span_vs_param.pdf') @ 278`; `savefig(outdir / 'phase_instability_vs_param.pdf') @ 309`; `savefig(outdir / 'dist_to_ray_vs_theta_span.pdf') @ 334`; `savefig(outdir / 'warning_vs_exit.pdf') @ 402`; `savefig(outdir / f'seed{seed}_{dcol}_timeseries.pdf') @ 457`; `savefig(outdir / f'seed{seed}_{dcol}_curvature.pdf') @ 467`; `summary.to_csv(outdir / '_agg_summary.csv', index=False) @ 496`; `seedtraj.to_csv(outdir / '_agg_seed_trajectories.csv', index=False) @ 498`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A35. [make_paper_figures.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/make_paper_figures.py) — 44 lines

**Role/purpose:** Visualization. Plots saved edge/exponent relationships.

**Mathematics:** M43. **Outputs:** Saved figures and fitted log-log lines.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `df = pd.read_csv('fig1_g_phase.csv') @ 6`; `df = pd.read_csv('fig2_eps_scaling_seedA.csv') @ 17`; `x = df['eps'] @ 18`; `y = df['t_last_vrec_ge_0.8'] @ 19`; `m, b = np.polyfit(np.log(x), np.log(y), 1) @ 23`; `dfA = pd.read_csv('fig2_eps_scaling_seedA.csv') @ 33`; `dfB = pd.read_csv('fig3_eps_scaling_seedB.csv') @ 34`

**Dependencies (static imports):** `matplotlib.pyplot`, `numpy`, `pandas`.

**Recorded/file output sites:** `plt.savefig('fig_g_phase_shelf.pdf') @ 13`; `plt.savefig('fig_eps_scaling_loglog_seedA.pdf') @ 29`; `plt.savefig('fig_eps_scaling_loglog_two_seeds.pdf') @ 43`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A36. [make_vrec_timeseries_figures.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/make_vrec_timeseries_figures.py) — 79 lines

**Role/purpose:** Visualization. Finds exported series and annotates last threshold exceedance.

**Mathematics:** M13,M53. **Outputs:** v_rec time-series figures/lifetime annotations.

**Major classes/functions and signature parameters:** `find_series_csv(outdir: str) @ 8`; `load_series(path: str) @ 17`; `t_last_ge_theta(df: pd.DataFrame, theta: float) @ 42`; `main() @ 48`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `THETA = 0.8 @ 6`

**Dependencies (static imports):** `glob`, `matplotlib.pyplot`, `numpy`, `pandas`.

**Recorded/file output sites:** `plt.savefig('fig_vrec_timeseries_threshold.pdf') @ 75`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A37. [model_core.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/model_core.py) — 343 lines

**Role/purpose:** Evolution / stored observer state. Owns mutable complex triad, clock, readouts, stage/identity and pre-update history recorder.

**Mathematics:** M01–M07,M10,M11,M26,M52. **Outputs:** Updated ModelState and history dictionary with provenance/optional foreclosure.

**Major classes/functions and signature parameters:** `_unit(v: np.ndarray, eps: float=1e-12) @ 21`; `_mirror_z(v: np.ndarray) @ 29`; `class ModelParams @ 35`; `ModelParams.cycle_config(self) @ 67`; `class ModelState @ 72`; `ModelState.kappa(self) @ 100`; `_make_history_meta(seed: int \| None=None, version: str \| None=None) @ 105`; `class TriOctaPhaseLockModel @ 114`; `TriOctaPhaseLockModel.__init__(self, params: ModelParams) @ 121`; `TriOctaPhaseLockModel.phase_lock_step(self, state: ModelState, *, g_override: float \| None=None) @ 133`; `TriOctaPhaseLockModel.advance_phi(self, state: ModelState) @ 164`; `TriOctaPhaseLockModel.update_z(self, state: ModelState, *, theta_lock_override: float \| None=None) @ 169`; `TriOctaPhaseLockModel.update_cycle_stage(self, state: ModelState) @ 232`; `TriOctaPhaseLockModel.update_identity_state(self, state: ModelState) @ 237`; `TriOctaPhaseLockModel.step(self, state: ModelState, dt: float=0.1, *, g_override: float \| None=None, theta_lock_override: float \| None=None) @ 246`; `TriOctaPhaseLockModel.run(self, state: ModelState, n_steps: int=100, dt: float=0.1, *, seed: int \| None=None, version: str \| None=None) @ 268`

**State/configuration objects:** `ModelParams: eps: float = 0.05 @ 37`; `ModelParams: g: float = 0.2 @ 38`; `ModelParams: k_vals: np.ndarray = field(default_factory=default_k_triplet) @ 39`; `ModelParams: delta_vals: np.ndarray = field(default_factory=lambda: np.zeros(3, dtype=complex)) @ 40`; `ModelParams: d24_steps: int = 12 @ 43`; `ModelParams: phi_step_per_iter: int = 1 @ 44`; `ModelParams: lambda_phase: float = 0.001 @ 47`; `ModelParams: lambda_vp: float = 0.618 @ 50`; `ModelParams: gamma: float = 0.577 @ 51`; `ModelParams: theta_lock: float = 0.244 @ 52`; `ModelParams: omega_noise_sigma: float = 0.0 @ 55`; `ModelParams: z_alpha: float = 1.0 @ 58`; `ModelParams: z_beta: float = 0.5 @ 59`; `ModelParams: kappa_thresholds: np.ndarray = field(default_factory=lambda: np.array([0.2, 0.5, 0.9, 1.3, 1.8, 2.3])) @ 62`; `ModelState: Omega: np.ndarray @ 74`; `ModelState: phi_index: int = 0 @ 77`; `ModelState: cycle_stage: int = 0 @ 78`; `ModelState: identity_state: int = 0 @ 79`; `ModelState: z: float = 0.0 @ 82`; `ModelState: Z_macro: np.ndarray = field(default_factory=lambda: np.zeros(3, dtype=float)) @ 85`; `ModelState: Z_chiral: np.ndarray = field(default_factory=lambda: np.zeros(3, dtype=float)) @ 88`; `ModelState: Z_vec: np.ndarray = field(default_factory=lambda: np.zeros(3, dtype=float)) @ 91`; `ModelState: z_mem: float = 0.0 @ 93`; `ModelState: t: float = 0.0 @ 96`; `ModelState: step: int = 0 @ 97`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.constants_selector`, `.identity_rules`, `.latent_foreclosure`, `.phase_triad_sync`, `.su3_basis`, `dataclasses`, `datetime`, `numpy`, `uuid`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `analysis_runner.py`, `chirality_param_scan.py`, `diagnose_bottom_lid.py`, `diagnostics.py`, `edge_map.py`, `eigen_analysis.py`, `explore_sweep.py`, `generate_golden_refs.py`, `new_run_tests.py`, `param_scan.py`, `plasticity_map.py`, `rgd_connection_diagnostics.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py`, `sanity_report.py`, `side_zchiral_probe.py`, `toy_3d_triocta.py`, `toy_lab.py`, `toy_ui.py`, `toy_ui_live.py`, `wide_scan_triocta.py`, `z_spike_diagnostic.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A38. [nan_forensics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/nan_forensics.py) — 95 lines

**Role/purpose:** Diagnostics. Finds first nonfinite locations in component histories and records context.

**Mathematics:** M43. **Outputs:** Forensics JSON/report; no recovery or change to recurrence.

**Major classes/functions and signature parameters:** `first_nonfinite_index(arr: np.ndarray) @ 12`; `analyze_history(history: Dict[str, np.ndarray], window: int=2) @ 20`; `run_forensics(run_fn, params, seed: int, n_steps: int, dt: float, out_dir: str) @ 66`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `json`, `numpy`, `pathlib`, `typing`.

**Recorded/file output sites:** `out_file.write_text(json.dumps(report, indent=2)) @ 93`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A39. [new_run_tests.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/new_run_tests.py) — 326 lines

**Role/purpose:** Tests / reproducibility. Later schema/determinism/golden runner; masks undefined directions and checks J consistency.

**Mathematics:** M52,M13,M14. **Outputs:** Assertion outcomes and warning counts if run; not run here.

**Major classes/functions and signature parameters:** `validate_hist_schema(hist: dict, *, n_steps_expected: int \| None=None, name: str='hist') @ 16`; `make_initial_state(seed: int) @ 111`; `params_from_ref(p) @ 151`; `run_triocta(ref, n_steps=2000) @ 164`; `checksum(x) @ 175`; `assert_close(a, b, name, rtol=1e-06, atol=1e-08) @ 181`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `REFS_JSON = 'golden/golden_refs.json' @ 14`; `refs = json.loads(Path(REFS_JSON).read_text(encoding='utf-8')) @ 190`; `warn_counts = Counter() @ 194`

**Dependencies (static imports):** `collections`, `definitions`, `json`, `model_core`, `numpy`, `pathlib`, `physics_sampler`, `warnings`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A40. [param_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/param_scan.py) — 68 lines

**Role/purpose:** Analysis orchestration. Scans soft-triplet scale alpha through model runs.

**Mathematics:** M04,M43. **Outputs:** Parameter-summary arrays and plots.

**Major classes/functions and signature parameters:** `run_for_alpha(alpha: float, n_steps: int=200, dt: float=0.05) @ 8`; `scan_alphas(alpha_values) @ 25`; `plot_scan(alpha_values, kappas, stages, identities) @ 37`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `constants_selector`, `matplotlib.pyplot`, `model_core`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A41. [pathing.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/pathing.py) — 234 lines

**Role/purpose:** AI-memory utilities. TORMENT-labelled slug, containment, sharding, dated-path and filename helpers.

**Mathematics:** M30. **Outputs:** Validated/derived filesystem paths; no mathematical state update.

**Major classes/functions and signature parameters:** `safe_slug(value: str, label: str='identifier') @ 49`; `ensure_within_base(path: str, base_dir: str) @ 89`; `safe_join(base: str, *parts: str) @ 106`; `shard_for_key(key: str, n: int=256) @ 129`; `sharded_entity_path(base: str, category: str, key: str, ext: str='.json') @ 144`; `dated_log_path(base: str, category: str, *, date: Optional[datetime.date]=None) @ 168`; `approved_subdir(base: str, *parts: str, mkdir: bool=True) @ 195`; `stable_filename(root: str, filename: str) @ 217`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `datetime`, `hashlib`, `os`, `re`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `trajectory_logging.py`

**Known tests/examples (static reachability):** `run_patch39_unified.py`, `run_unified_diagnostics.py` No execution claimed.

### A42. [phase_triad_experiment.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/phase_triad_experiment.py) — 428 lines

**Role/purpose:** Experiment protocol / analysis. Scans coherence/slips/gates/plasticity through an unimplemented ModelAdapter interface.

**Mathematics:** M02,M17,M46,M53. **Outputs:** RunConfig/RunSummary rows, per-step/event histories if adapter supplied.

**Major classes/functions and signature parameters:** `_wrap_angle_pi(a: float) @ 37`; `omega_phases(omega: np.ndarray) @ 42`; `triad_S(phi: np.ndarray) @ 47`; `collective_phase(S: complex) @ 52`; `coherence_mag(S: complex) @ 57`; `detect_slip(phi_prev: float, phi_now: float, slip_tol: float=0.25) @ 62`; `class EmissionGate @ 82`; `in_gate(theta: float, center: float, half_width: float) @ 87`; `class RunConfig @ 98`; `class RunSummary @ 117`; `class ModelAdapter @ 147`; `ModelAdapter.reset(self, seed: int, params: Dict[str, Any]) @ 159`; `ModelAdapter.step(self) @ 162`; `run_one(model: ModelAdapter, cfg: RunConfig, events_csv_path: str, summary_csv_path: str) @ 170`; `run_grid(model: ModelAdapter, seeds: Iterable[int], gs: Iterable[float], lams: Iterable[float], eps: float, k3: float, dt: float, steps: int, out_prefix: str='phase_triad') @ 368`

**State/configuration objects:** `EmissionGate: center: float @ 83`; `EmissionGate: half_width: float @ 84`; `EmissionGate: min_coherence: float @ 85`; `RunConfig: seed: int @ 99`; `RunConfig: g: float @ 100`; `RunConfig: eps: float @ 101`; `RunConfig: k3: float @ 102`; `RunConfig: dt: float @ 103`; `RunConfig: steps: int @ 104`; `RunConfig: lam: float = 0.0 @ 106`; `RunConfig: theta_plastic: float = 0.8 @ 107`; `RunConfig: slip_tol: float = 0.25 @ 108`; `RunConfig: jeff_zero: float = 1e-06 @ 109`; `RunConfig: vrec_spike: float = 1.2 @ 110`; `RunConfig: enable_emission: bool = False @ 112`; `RunConfig: emission_gates: Optional[List[EmissionGate]] = None @ 113`; `RunSummary: seed: int @ 118`; `RunSummary: g: float @ 119`; `RunSummary: eps: float @ 120`; `RunSummary: k3: float @ 121`; `RunSummary: dt: float @ 122`; `RunSummary: steps: int @ 123`; `RunSummary: lam: float @ 124`; `RunSummary: finite_last_step: int @ 126`; `RunSummary: plasticity_T: int @ 127`; `RunSummary: mean_coherence: float @ 129`; `RunSummary: frac_high_coherence: float @ 130`; `RunSummary: slip_count: int @ 131`; `RunSummary: slip_plus: int @ 132`; `RunSummary: slip_minus: int @ 133`; `RunSummary: slips_near_jeff0: int @ 135`; `RunSummary: slips_with_vrec_spike: int @ 136`; `RunSummary: detach_events: int @ 139`; `RunSummary: regen_events: int @ 140`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `csv`, `dataclasses`, `math`, `numpy`, `typing`.

**Recorded/file output sites:** `writer.writerow({k: row.get(k, '') for k in event_fields}) @ 217`; `w.writerow(asdict(summary)) @ 363`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A43. [phase_triad_sync.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/phase_triad_sync.py) — 40 lines

**Role/purpose:** Evolution / passive readout. Simultaneous harmonic-3 phase synchronization and triad coherence.

**Mathematics:** M02. **Outputs:** Updated complex array and complex coherence scalar.

**Major classes/functions and signature parameters:** `apply_phase_triad_sync(Omega_next: np.ndarray, lambda_phase: float) @ 5`; `triad_coherence(Omega: np.ndarray) @ 30`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `model_core.py`, `run_patch39_unified.py`, `run_sims_minimal.py`, `run_unified_diagnostics.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A44. [physics_sampler.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/physics_sampler.py) — 137 lines

**Role/purpose:** Passive analysis / visualization. Samples intensity fractions, relative phases and cubic J from history.

**Mathematics:** M08,M09. **Outputs:** Observable dictionary, summary statistics and phase/J distribution plots.

**Major classes/functions and signature parameters:** `compute_flavor_probabilities(Omega_history: np.ndarray) @ 8`; `compute_relative_phases(Omega_history: np.ndarray) @ 21`; `compute_cp_like_invariant(Omega_history: np.ndarray) @ 47`; `sample_physics_observables(history) @ 62`; `summarize_observables(obs) @ 90`; `plot_phase_and_cp_distributions(obs) @ 110`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.definitions`, `matplotlib.pyplot`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `chirality_param_scan.py`, `diagnostics.py`, `new_run_tests.py`, `run_sim.py`, `run_tests.py`, `toy_3d_triocta.py`, `toy_lab.py`, `toy_ui.py`, `toy_ui_live.py`, `wide_scan_triocta.py`

**Known tests/examples (static reachability):** `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_sim.py`, `run_tests.py` No execution claimed.

### A45. [physics_sampler2.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/physics_sampler2.py) — 187 lines

**Role/purpose:** Passive analysis / visualization. CP-conditioned summaries and chirality selection windows, probability/J timelines.

**Mathematics:** M12,M17. **Outputs:** Masks, summaries, timing windows and plots.

**Major classes/functions and signature parameters:** `cp_conditioned_masks(history) @ 10`; `summarize_cp_conditioned_observables(history, obs) @ 21`; `detect_chirality_selection_window(history, obs, frac_start=0.1, frac_end=0.2) @ 61`; `plot_flavor_time_series(history, obs) @ 140`; `plot_Jeff_vs_time(history, obs) @ 167`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.cp_windows`, `.definitions`, `matplotlib.pyplot`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `diagnostics.py`, `run_sim.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_sim.py` No execution claimed.

### A46. [plasticity_map.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plasticity_map.py) — 196 lines

**Role/purpose:** Analysis orchestration. Maps early high-turning last-threshold times/counts and tail values across runs.

**Mathematics:** M14,M53. **Outputs:** One CSV metric row per configuration/seed.

**Major classes/functions and signature parameters:** `run_once(seed: int, eps: float, g: float, k3_scale: float, dt: float, steps: int) @ 30`; `safe_xyz(hist: dict, z_key: str) @ 48`; `parse_int_ranges(items) @ 55`; `plasticity_metrics(v_rec: np.ndarray, dt: float, thr: float) @ 68`; `main() @ 84`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--seeds', nargs='+', type=str, required=True) @ 86`; `ap.add_argument('--eps', nargs='+', type=float, required=True) @ 87`; `ap.add_argument('--g', nargs='+', type=float, required=True) @ 88`; `ap.add_argument('--k3', nargs='+', type=float, required=True, help='k3_scale list') @ 89`; `ap.add_argument('--dt', type=float, required=True) @ 90`; `ap.add_argument('--steps', type=int, default=2000) @ 91`; `ap.add_argument('--z_key', choices=['Z_total', 'Z_macro', 'Z_chiral'], default='Z_total') @ 93`; `ap.add_argument('--include_dkappa', action='store_true') @ 94`; `ap.add_argument('--thr', nargs='+', type=float, default=[0.8, 0.9], help='absolute v_rec thresholds') @ 96`; `ap.add_argument('--late_frac', type=float, default=0.5, help="fraction of run treated as 'late' for plateau stats") @ 97`; `ap.add_argument('--out', type=str, default='plasticity_map.csv') @ 98`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `definitions`, `geometry_3d`, `model_core`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `df.to_csv(args.out, index=False) @ 191`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A47. [plot_dist_to_ray.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plot_dist_to_ray.py) — 55 lines

**Role/purpose:** Visualization. Plots saved angular distance-to-ray relationships.

**Mathematics:** M46. **Outputs:** Saved scatter/summary figures.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `files = glob.glob(os.path.join('outputs_patch39_unified', '**', 'seed_trajectories_seed*.csv'), recursive=True) @ 7`; `df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True) @ 11`; `needed = {'lambda_phase', 'channel', 'traj_class', 'dist_to_ray_deg'} @ 13`; `missing = needed - set(df.columns) @ 14`; `df = df[list(needed)].dropna() @ 19`; `lambdas = sorted(df['lambda_phase'].unique()) @ 22`; `outdir = os.path.join('outputs_patch39_unified', 'plots') @ 24`

**Dependencies (static imports):** `glob`, `matplotlib.pyplot`, `os`, `pandas`.

**Recorded/file output sites:** `plt.savefig(os.path.join(outdir, f'dist_to_ray_lambda_{lam:.2f}.png'), dpi=200) @ 52`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A48. [plot_edge_map.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plot_edge_map.py) — 171 lines

**Role/purpose:** Visualization. Displays empirical critical coupling/stability summaries with safe log transforms.

**Mathematics:** M43. **Outputs:** Edge-map figures.

**Major classes/functions and signature parameters:** `_safe_log10(x: pd.Series) @ 14`; `main() @ 20`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--csv', default='edge_map.csv', help='Input CSV from edge_map.py') @ 22`; `ap.add_argument('--outdir', default='edge_plots', help='Directory to write PNGs') @ 23`

**Dependencies (static imports):** `__future__`, `argparse`, `math`, `matplotlib.pyplot`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `plt.savefig(os.path.join(args.outdir, '01_gcrit_hist.png'), dpi=200) @ 45`; `plt.savefig(os.path.join(args.outdir, '02_gcrit_vs_seed.png'), dpi=200) @ 56`; `plt.savefig(os.path.join(args.outdir, '03_finite_prefix_hist.png'), dpi=200) @ 68`; `plt.savefig(os.path.join(args.outdir, '04_prefix_vs_vrec_p95.png'), dpi=200) @ 81`; `plt.savefig(os.path.join(args.outdir, '05_first_bad_channel.png'), dpi=200) @ 111`; `plt.savefig(os.path.join(args.outdir, '06_log_magnitudes.png'), dpi=200) @ 138`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A49. [plot_optional_suite.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plot_optional_suite.py) — 89 lines

**Role/purpose:** Visualization. Displays optional dt/gap/coherence sweep metrics.

**Mathematics:** M44,M46. **Outputs:** Heatmaps and parameter-comparison figures.

**Major classes/functions and signature parameters:** `coh_label(df: pd.DataFrame) @ 15`; `heatmap(grid: pd.DataFrame, title: str, filename: str, cbar_label: str) @ 25`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `ROOT = Path('outputs_dt_optional_suite') / '_aggregated' @ 7`; `OUTP = ROOT / 'plots' @ 8`; `ray = pd.read_csv(ROOT / 'ray_event_alignment_all.csv', low_memory=False) @ 11`; `summ = pd.read_csv(ROOT / 'summary_all.csv', low_memory=False) @ 12`; `ray['coh_label'] = coh_label(ray) @ 20`; `summ['coh_label'] = coh_label(summ) @ 21`; `metrics = ['dist_mean', 'dist_median', 'frac_le_2deg', 'frac_le_5deg', 'frac_le_10deg', 'frac_le_15deg'] @ 23`; `inv_cols = ['gap_width_deg', 'coh_label', 'channel'] @ 53`; `inv = ray.groupby(inv_cols).agg(n_runs=('dt', 'count'), T_unique=('T_total', 'nunique'), dist_mean_std=('dist_mean', 'std'), frac10_std=('frac_le_10deg', 'std'), frac5_std=('frac_le_5deg', 'std')).reset_index() @ 54`; `inv_fixedT = inv[(inv['n_runs'] >= 3) & (inv['T_unique'] == 1)].copy() @ 62`

**Dependencies (static imports):** `__future__`, `matplotlib.pyplot`, `numpy`, `pandas`, `pathlib`.

**Recorded/file output sites:** `inv_fixedT.to_csv(ROOT / 'dt_invariance_event_ray.csv', index=False) @ 63`; `fig.savefig(OUTP / filename, dpi=170) @ 37`; `fig.savefig(OUTP / 'dt_invariance_frac10_std_hist.png', dpi=170) @ 74`; `rate2.to_csv(ROOT / 'emit_rate_per_time.csv', index=False) @ 88`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A50. [plot_rgd_heatmaps_from_rows.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plot_rgd_heatmaps_from_rows.py) — 183 lines

**Role/purpose:** Visualization / analysis. Aggregates row-level finite/stable and timing rates into parameter grids.

**Mathematics:** M42–M44. **Outputs:** Saved stable-fraction and finite-timing heatmaps.

**Major classes/functions and signature parameters:** `ensure_dir(p: str) @ 31`; `to_float(s: pd.Series) @ 34`; `pivot_grid(df: pd.DataFrame, value_col: str) @ 37`; `plot_heatmap(ax, eps_vals, k3_vals, Z, title: str, cmap: str='viridis', vmin=None, vmax=None, show_colorbar: bool=False) @ 48`; `agg_per_point(rows: pd.DataFrame) @ 67`; `main() @ 95`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `POINT_KEYS = ['eps', 'g', 'k3_scale', 'dt', 'n_steps', 'noise_sigma', 'do_rsb', 'rsb_steps', 'version', 'point_index'] @ 29`

**CLI controls/defaults:** `ap.add_argument('--rows', required=True, help='Path to ..._rows.csv') @ 97`; `ap.add_argument('--outdir', default='outputs', help='Where to write PNGs') @ 98`; `ap.add_argument('--what', choices=['stable', 'settle', 'events', 'all'], default='stable', help='Which heatmaps to make') @ 99`; `ap.add_argument('--dpi', type=int, default=200) @ 101`; `ap.add_argument('--max-g-panels', type=int, default=18, help='Limit number of g-slices plotted (visual sanity)') @ 102`

**Dependencies (static imports):** `__future__`, `argparse`, `matplotlib.pyplot`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `fig.savefig(out_png, dpi=args.dpi) @ 176`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A51. [plot_sims_summary.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/plot_sims_summary.py) — 101 lines

**Role/purpose:** Visualization / analysis. Plots survival/failure timing and event statistics from SIMS summaries.

**Mathematics:** M43,M46. **Outputs:** Survival curves and parameter heatmaps.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `CSV = 'outputs_locate\\summary_all.csv' @ 6`; `OUTDIR = 'outputs_locate\\plots' @ 7`; `df = pd.read_csv(CSV) @ 10`; `T = int(df['n_steps'].max()) - 1 @ 13`; `df['survived_full'] = (df['finite_last_step'] >= T).astype(int) @ 14`; `df['has_emit'] = (df['t_first_emit'] <= T).astype(int) @ 17`; `gs = np.sort(df['g'].unique()) @ 21`; `t_grid = np.linspace(0, T, 200).astype(int) @ 28`; `grp = df.groupby('g')['finite_last_step'] @ 47`; `summary = pd.DataFrame({'mean': grp.mean(), 'median': grp.median(), 'p10': grp.quantile(0.1), 'p90': grp.quantile(0.9), 'n': grp.size()}).reset_index() @ 48`

**Dependencies (static imports):** `matplotlib.pyplot`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `plt.savefig(os.path.join(OUTDIR, 'survival_curves.png'), dpi=200) @ 43`; `plt.savefig(os.path.join(OUTDIR, 'finite_last_step_vs_g.png'), dpi=200) @ 64`; `plt.savefig(os.path.join(OUTDIR, 'emit_vs_finite_last_step.png'), dpi=200) @ 93`; `plt.savefig(os.path.join(OUTDIR, 'heatmap_mean_finite_last_step.png'), dpi=200) @ 83`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A52. [provenance.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/provenance.py) — 41 lines

**Role/purpose:** Utilities / reproducibility. Stable parameter hash and human run metadata stamping.

**Mathematics:** M52. **Outputs:** RunMeta dataclass, dictionary and plot/console provenance stamp.

**Major classes/functions and signature parameters:** `class RunMeta @ 9`; `_stable_hash_dict(d: dict) @ 17`; `make_run_meta(version: str, seed: int, params_dict: dict) @ 21`; `meta_dict(meta: RunMeta) @ 33`; `stamp_run_meta(fig, meta: RunMeta \| None) @ 36`

**State/configuration objects:** `RunMeta: version: str @ 11`; `RunMeta: seed: int @ 12`; `RunMeta: params_hash: str @ 13`; `RunMeta: run_id: str @ 14`; `RunMeta: timestamp_utc: str @ 15`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `dataclasses`, `datetime`, `hashlib`, `json`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `toy_3d_triocta.py`, `toy_ui.py`, `wide_scan_triocta.py`, `z_spike_diagnostic.py`

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A53. [rgd_connection_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rgd_connection_diagnostics.py) — 473 lines

**Role/purpose:** Diagnostics / orchestration. Computes onset/rolling-variance settling and finite stability flags, optionally invokes RSB.

**Mathematics:** M42,M43. **Outputs:** History plus timing/connection result dictionary.

**Major classes/functions and signature parameters:** `_tail_slice(T: int, frac: float=0.2, min_len: int=50) @ 40`; `_safe_mean(x: np.ndarray) @ 45`; `_safe_var(x: np.ndarray) @ 51`; `_safe_rms(x: np.ndarray) @ 57`; `_rolling_mean(x: np.ndarray, win: int) @ 63`; `_rolling_mean_abs(x: np.ndarray, win: int) @ 71`; `_rolling_var(x: np.ndarray, win: int) @ 74`; `_first_bias_time_baseline(sig: np.ndarray, t: np.ndarray, *, win_frac: float=0.1, min_win: int=20, baseline_frac: float=0.1, baseline_factor: float=2.0, floor: float=1e-12) @ 88`; `_first_settle_time_var(sig: np.ndarray, t: np.ndarray, *, win_frac: float=0.1, min_win: int=20, tail_frac: float=0.2, settle_factor: float=2.0, floor: float=1e-20) @ 131`; `_stable_flags(hist: dict) @ 173`; `build_params(*, eps: float, g: float, k3_scale: float) @ 203`; `run_history(*, eps: float, g: float, k3_scale: float, n_steps: int=300, dt: float=0.05, seed: int=42, version: str \| None=None) @ 219`; `analyze_connection(hist: dict, *, noise_sigma: float=0.0, deadband: float=1e-06, bias_win_frac: float=0.1, bias_min_win: int=20, bias_baseline_frac: float=0.1, bias_baseline_factor: float=2.0, settle_win_frac: float=0.1, settle_min_win: int=20, settle_tail_frac: float=0.2, settle_factor: float=2.0) @ 239`; `run_connection(*, eps: float, g: float, k3_scale: float, noise_sigma: float=0.0, n_steps: int=300, dt: float=0.05, seed: int=42, do_rsb: bool=True, rsb_steps: int=300, version: str \| None=None) @ 408`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `constants_selector`, `definitions`, `diagnostics`, `model_core`, `numpy`, `rsb_model`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `scan_rgd_connection.py`

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A54. [rsb_dom_band_demo.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_dom_band_demo.py) — 63 lines

**Role/purpose:** Visualization example. Runs selected RSB examples and displays dominant-band classifications.

**Mathematics:** M19–M24. **Outputs:** Band trajectories and regime summaries; helper import contract needs context.

**Major classes/functions and signature parameters:** `run_and_classify(params: RSBParams, n_steps: int, seed: int) @ 18`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `diagnostics`, `matplotlib.pyplot`, `rsb_model`, `rsb_spectral_viz`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A55. [rsb_entropy_demo.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_entropy_demo.py) — 66 lines

**Role/purpose:** Visualization example. Runs RSB settings and compares entropy timelines.

**Mathematics:** M19–M24. **Outputs:** Entropy figures and printed regimes.

**Major classes/functions and signature parameters:** `run_entropy_demo() @ 16`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `matplotlib.pyplot`, `rsb_model`, `spectral_viz`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A56. [rsb_model.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_model.py) — 395 lines

**Role/purpose:** Evolution. Independent complex channel×ring×helicity state with channel mixing, drift, gain, contraction and normalization.

**Mathematics:** M19–M22. **Outputs:** Updated psi, seeded initialization and psi history.

**Major classes/functions and signature parameters:** `class RSBParams @ 15`; `class RSBModel @ 45`; `RSBModel.__init__(self, params: RSBParams) @ 60`; `RSBModel._validate_params(self) @ 82`; `RSBModel._build_channel_matrix(self) @ 98`; `RSBModel._build_phase_laplacian(M: int) @ 134`; `RSBModel._build_phase_mask(M: int) @ 144`; `RSBModel._build_band_mask(M: int, center: int \| None=None, width: float \| None=None) @ 157`; `RSBModel._apply_channel_recursion(self, psi: np.ndarray) @ 188`; `RSBModel._laplacian_on_phase(self, arr: np.ndarray) @ 197`; `RSBModel._H_RSB_action(self, psi: np.ndarray) @ 204`; `RSBModel._apply_spectral_contraction(self, psi: np.ndarray) @ 242`; `RSBModel._apply_reinforcement(self, psi: np.ndarray) @ 300`; `RSBModel.step(self, psi: np.ndarray, rng: np.random.Generator \| None=None) @ 321`; `RSBModel.run(self, n_steps: int=200, seed: int \| None=0, rng: np.random.Generator \| None=None, psi0: np.ndarray \| None=None) @ 355`

**State/configuration objects:** `RSBParams: num_channels: int = 3 @ 17`; `RSBParams: num_phases: int = 12 @ 18`; `RSBParams: num_helicity: int = 2 @ 19`; `RSBParams: theta: float = 0.35 @ 22`; `RSBParams: phi: float = 0.0 @ 23`; `RSBParams: alpha_L: float = 0.2 @ 24`; `RSBParams: beta_S: float = 0.1 @ 25`; `RSBParams: d_vis: float = 0.95 @ 26`; `RSBParams: kappa_L: float = 0.4 @ 29`; `RSBParams: kappa_S: float = 0.3 @ 30`; `RSBParams: mu: float = 0.25 @ 31`; `RSBParams: gamma: float = 0.05 @ 34`; `RSBParams: eta: float = 0.02 @ 35`; `RSBParams: eps_rsb: float = 0.05 @ 38`; `RSBParams: alpha: float = 0.0 @ 41`; `RSBParams: adaptive_alpha: bool = False @ 42`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `dataclasses`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `rgd_connection_diagnostics.py`, `rsb_dom_band_demo.py`, `rsb_entropy_demo.py`, `rsb_param_scan.py`, `rsb_phase_scan.py`, `rsb_spectral_demo.py`, `rsb_spectral_viz.py`, `run_sim.py`, `toy_3d_triocta.py`, `toy_ui.py`, `toy_ui_live.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_entropy_demo.py`, `rsb_spectral_demo.py`, `run_sim.py` No execution claimed.

### A57. [rsb_param_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_param_scan.py) — 263 lines

**Role/purpose:** Analysis orchestration. Sweeps RSB parameters/seeds and aggregates regimes per alpha.

**Mathematics:** M19–M24. **Outputs:** Rows/aggregate tables and phase diagrams.

**Major classes/functions and signature parameters:** `run_single_rsb(n_steps=250, seed=0, **params_overrides) @ 13`; `param_sweep(kappa_L_list, mu_list, gamma_list, eta_list, alpha_list, n_steps=250, seed=0, print_live=True) @ 44`; `summarize_by_alpha(results) @ 100`; `summarize_results(results) @ 131`; `aggregate_by_alpha(results) @ 145`; `plot_phase_diagram_by_alpha(results, class_order=None) @ 162`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `collections`, `diagnostics`, `matplotlib.pyplot`, `numpy`, `rsb_model`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A58. [rsb_phase_scan.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_phase_scan.py) — 60 lines

**Role/purpose:** Analysis orchestration. Convenience RSB phase-diagram scan.

**Mathematics:** M19–M24. **Outputs:** Class fractions/phase summary plots.

**Major classes/functions and signature parameters:** `scan_phase_diagram(alpha_list, seed_list, n_steps=300) @ 15`; `main() @ 44`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `collections`, `diagnostics`, `numpy`, `rsb_model`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A59. [rsb_spectral_demo.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_spectral_demo.py) — 93 lines

**Role/purpose:** Visualization example. Single seeded RSB spectral demonstration.

**Mathematics:** M19–M24. **Outputs:** Band evolution/final spectra and classification overlays.

**Major classes/functions and signature parameters:** `run_single_spectral_demo(params: RSBParams, n_steps: int=300, seed: int=0) @ 22`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `diagnostics`, `matplotlib.pyplot`, `rsb_model`, `rsb_spectral_viz`, `spectral_viz`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A60. [rsb_spectral_viz.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/rsb_spectral_viz.py) — 319 lines

**Role/purpose:** Visualization. Central plot consumers for RSB band, entropy, dominant index, velocity and multi-alpha runs.

**Mathematics:** M16,M23,M24. **Outputs:** Matplotlib figures; some helpers orchestrate independent RSB runs.

**Major classes/functions and signature parameters:** `plot_spectral_band_evolution(psi_hist, params, log10=True) @ 27`; `plot_final_spectral_energy(psi_hist, params) @ 63`; `plot_spectral_entropy_and_dom_band(stats) @ 85`; `run_rsb_for_params(params: RSBParams, n_steps=300, seed=0) @ 115`; `plot_multi_alpha_spectral_bands(base_params, alpha_list, n_steps=300, seed=0) @ 130`; `plot_multi_alpha_timeseries(base_params, alpha_list, n_steps=300, seed=0) @ 192`; `plot_multi_alpha_dom_band_trajectory(base_params: RSBParams, alpha_list, n_steps: int=300, seed: int=0) @ 237`; `plot_recursive_velocity(stats, ax=None) @ 294`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.definitions`, `.rsb_model`, `.spectral_viz`, `matplotlib.pyplot`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `toy_ui.py`, `toy_ui_live.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py` No execution claimed.

### A61. [run_patch39_unified.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_patch39_unified.py) — 455 lines

**Role/purpose:** AI-memory experiment orchestration. Combines triad histories, per-channel gates, slips and optional external seeds.

**Mathematics:** M01,M02,M27–M30,M46. **Outputs:** Per-step/event/summary CSV and optional trajectories; params-before-assignment defect preserved.

**Major classes/functions and signature parameters:** `_wrap_angle_pi(a: float) @ 28`; `detect_slip(phi_prev: float, phi_now: float, slip_tol: float=0.25) @ 32`; `is_finite_state(state: ModelState) @ 46`; `_init_omega0(seed: int, scale: float=0.1) @ 57`; `class RunCfg @ 63`; `run_one(cfg: RunCfg, outdir: Path) @ 99`; `main() @ 383`

**State/configuration objects:** `RunCfg: seed: int @ 64`; `RunCfg: gap_center0: float @ 65`; `RunCfg: gap_center1: float @ 66`; `RunCfg: gap_center2: float @ 67`; `RunCfg: eps: float @ 68`; `RunCfg: g: float @ 69`; `RunCfg: dt: float @ 70`; `RunCfg: steps: int @ 71`; `RunCfg: k_mode: str @ 72`; `RunCfg: k_alpha: float @ 73`; `RunCfg: lambda_phase: float @ 75`; `RunCfg: n_sectors: int @ 78`; `RunCfg: gap_center_deg: float @ 79`; `RunCfg: gap_width_deg: float @ 80`; `RunCfg: require_coherence: bool @ 81`; `RunCfg: coherence_min: float @ 82`; `RunCfg: emission_mode: str @ 83`; `RunCfg: slip_tol: float @ 86`; `RunCfg: jeff_zero: float @ 87`; `RunCfg: log_stride: int @ 90`; `RunCfg: spawn_external: bool @ 93`; `RunCfg: seed_speed: float @ 94`; `RunCfg: seed_drag: float @ 95`; `RunCfg: seed_trail_len: int @ 96`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--outdir', type=str, default='outputs_patch39_unified') @ 385`; `ap.add_argument('--seed_lo', type=int, default=0) @ 387`; `ap.add_argument('--seed_hi', type=int, default=3) @ 388`; `ap.add_argument('--gap_center0', type=float, default=0.0) @ 390`; `ap.add_argument('--gap_center1', type=float, default=7.0) @ 391`; `ap.add_argument('--gap_center2', type=float, default=-7.0) @ 392`; `ap.add_argument('--eps', type=float, default=0.05) @ 394`; `ap.add_argument('--g', type=float, default=0.2) @ 395`; `ap.add_argument('--dt', type=float, default=0.05) @ 396`; `ap.add_argument('--steps', type=int, default=20000) @ 397`; `ap.add_argument('--k_mode', type=str, default='theta_soft') @ 399`; `ap.add_argument('--k_alpha', type=float, default=1.0) @ 400`; `ap.add_argument('--lambda_phase', type=float, default=0.0) @ 402`; `ap.add_argument('--n_sectors', type=int, default=24) @ 405`; `ap.add_argument('--gap_center_deg', type=float, default=0.0) @ 406`; `ap.add_argument('--gap_width_deg', type=float, default=5.0) @ 407`; `ap.add_argument('--require_coherence', action='store_true') @ 408`; `ap.add_argument('--coherence_min', type=float, default=0.65) @ 409`; `ap.add_argument('--emission_mode', type=str, default='partial', choices=['partial', 'coherent']) @ 410`; `ap.add_argument('--slip_tol', type=float, default=0.25) @ 413`; `ap.add_argument('--jeff_zero', type=float, default=1e-06) @ 414`; `ap.add_argument('--log_stride', type=int, default=10) @ 417`; `ap.add_argument('--spawn_external', action='store_true') @ 420`; `ap.add_argument('--seed_speed', type=float, default=1.0) @ 421`; `ap.add_argument('--seed_drag', type=float, default=0.02) @ 422`; `ap.add_argument('--seed_trail_len', type=int, default=200) @ 423`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `csv`, `dataclasses`, `definitions`, `math`, `model_core`, `numpy`, `pathlib`, `phase_triad_sync`, `seed_emission`, `seed_entities`, `trajectory_logging`, `typing`.

**Recorded/file output sites:** `w.writerow(row) @ 363`; `w_step.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'finite': finite, 'S_mag': S_mag, 'Phi_coll': Phi_coll, 'J_eff': J, 'kappa': kappa, 'Omega0_re': float(Om … [see source] @ 306`; `w_evt.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'event_type': 'slip', 'channel': '', 'S_mag': S_mag, 'Phi_coll': Phi_coll, 'J_eff': J, 'kappa': kappa}) @ 209`; `w_evt.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'event_type': 'emit', 'channel': int(ch), 'S_mag': float(S_mag), 'Phi_coll': float(Phi_coll), 'J_eff': flo … [see source] @ 293`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A62. [run_seed_emission_csv.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_seed_emission_csv.py) — 246 lines

**Role/purpose:** AI-memory experiment orchestration. Sweeps phase-sync strengths with channel-angle gate and detachment counts.

**Mathematics:** M02,M27,M54. **Outputs:** Emission CSV and per-run/event summary rows.

**Major classes/functions and signature parameters:** `_init_omega0(seed: int, scale: float=0.1) @ 15`; `wrap_deg(x: float) @ 20`; `in_gap(theta_deg: float, center_deg: float, width_deg: float) @ 26`; `triad_coherence_S(Omega: np.ndarray) @ 32`; `run_sweep(*, seed_lo: int, seed_hi: int, eps: float, g: float, dt: float, n_steps: int, gap_width_deg: float, gap_centers_deg: tuple[float, float, float], require_coherence: bool, S_thresh: float, regen_enabled: bool, regen_require_coherence: bool, regen_S_thresh: float, regen_phi_index_whitelist: list[int], outdir: Path) @ 41`; `main() @ 197`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--seed_lo', type=int, default=0) @ 199`; `ap.add_argument('--seed_hi', type=int, default=32) @ 200`; `ap.add_argument('--eps', type=float, default=0.05) @ 202`; `ap.add_argument('--g', type=float, default=0.2) @ 203`; `ap.add_argument('--dt', type=float, default=0.05) @ 204`; `ap.add_argument('--n_steps', type=int, default=50000) @ 205`; `ap.add_argument('--gap_width_deg', type=float, default=5.0) @ 207`; `ap.add_argument('--gap_center0', type=float, default=0.0) @ 208`; `ap.add_argument('--gap_center1', type=float, default=7.0) @ 209`; `ap.add_argument('--gap_center2', type=float, default=-7.0) @ 210`; `ap.add_argument('--require_coherence', action='store_true') @ 212`; `ap.add_argument('--S_thresh', type=float, default=0.999) @ 213`; `ap.add_argument('--regen_enabled', action='store_true') @ 215`; `ap.add_argument('--regen_require_coherence', action='store_true') @ 216`; `ap.add_argument('--regen_S_thresh', type=float, default=0.999) @ 217`; `ap.add_argument('--regen_phi_whitelist', type=str, default='') @ 218`; `ap.add_argument('--outdir', type=str, default='outputs_seed_emission_sweep') @ 219`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `csv`, `dataclasses`, `definitions`, `model_core`, `numpy`, `pathlib`.

**Recorded/file output sites:** `w_det.writerow(['seed', 'step', 'channel', 'phi_index', 'S_mag', 'J_eff', 'kappa', 'theta0_deg', 'theta1_deg', 'theta2_deg', 'Omega0_re', 'Omega0_im', 'Omega1_re', 'Omega1_im', 'Om … [see source] @ 73`; `w_sum.writerow(['seed', 'n_steps', 'detach_count_ch0', 'detach_count_ch1', 'detach_count_ch2', 'detach_count_total', 'first_detach_step', 'last_detach_step', 'sync3_events', 'parti … [see source] @ 82`; `w_sum.writerow([seed, n_steps, detach_counts[0], detach_counts[1], detach_counts[2], sum(detach_counts.values()), -1 if first_detach_step is None else first_detach_step, -1 if last … [see source] @ 187`; `w_det.writerow([seed, step_i, ch, phi_index, S_mag, J, kappa, float(theta_deg[0]), float(theta_deg[1]), float(theta_deg[2]), float(Om[0].real), float(Om[0].imag), float(Om[1].real) … [see source] @ 177`; `w_det.writerow([seed, step_i, ch, phi_index, S_mag, J, kappa, float(theta_deg[0]), float(theta_deg[1]), float(theta_deg[2]), float(Om[0].real), float(Om[0].imag), float(Om[1].real) … [see source] @ 134`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A63. [run_sim.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_sim.py) — 241 lines

**Role/purpose:** Evolution/analysis entry point. Main broad demonstration combining core history, geometry, CP, tangent, chirality and RSB analysis.

**Mathematics:** M01–M24,M31–M39,M49. **Outputs:** Many diagnostic plots and console summaries.

**Major classes/functions and signature parameters:** `main() @ 62`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `RUN_FULL_SUITE = False @ 59`; `VERBOSE_SCANS = True @ 60`

**Dependencies (static imports):** `analysis_tools`, `constants_selector`, `diagnostics`, `model_core`, `numpy`, `physics_sampler`, `physics_sampler2`, `rsb_model`, `semantic_diagnostics`, `tangent_corridor_analysis`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `chirality_lab.py`

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A64. [run_sims_minimal.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_sims_minimal.py) — 229 lines

**Role/purpose:** Experiment orchestration. Minimal finite-survival and event-conditioned six-ray/coherence runner.

**Mathematics:** M01,M02,M43,M46. **Outputs:** SIMS per-run summary rows/CSV and event metrics.

**Major classes/functions and signature parameters:** `wrap_pi(x: float) @ 37`; `ray_distance(phi: float, n_rays: int=6) @ 46`; `parse_int_list(xs: List[str]) @ 57`; `parse_float_list(xs: List[str]) @ 70`; `init_state(seed: int) @ 74`; `is_finite_state(st: ModelState) @ 83`; `run_one(*, seed: int, g: float, eps: float, dt: float, n_steps: int, gap_deg: float, require_coh: bool, coh_min: float) @ 96`; `write_rows_csv(path: str, rows: List[dict]) @ 173`; `main() @ 184`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--out_dir', type=str, default='outputs_sims_minimal') @ 186`; `ap.add_argument('--seeds', nargs='+', required=True, help='e.g. 0-99 or 0 1 2') @ 187`; `ap.add_argument('--g', nargs='+', required=True) @ 188`; `ap.add_argument('--eps', nargs='+', required=True) @ 189`; `ap.add_argument('--dt', type=float, required=True) @ 190`; `ap.add_argument('--steps', type=int, default=40000) @ 191`; `ap.add_argument('--gap_deg', type=float, default=24.0) @ 193`; `ap.add_argument('--require_coh', action='store_true') @ 194`; `ap.add_argument('--coh_min', type=float, default=0.8) @ 195`

**Dependencies (static imports):** `__future__`, `argparse`, `csv`, `dataclasses`, `math`, `model_core`, `numpy`, `os`, `phase_triad_sync`, `sims_diagnostics`, `typing`.

**Recorded/file output sites:** `w.writerow(r) @ 181`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A65. [run_tests.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_tests.py) — 280 lines

**Role/purpose:** Tests / reproducibility. Earlier history schema, determinism, direction/golden comparisons.

**Mathematics:** M52,M13,M14. **Outputs:** Assertions and warning report if invoked; not run here.

**Major classes/functions and signature parameters:** `make_initial_state(seed: int) @ 15`; `params_from_ref(p) @ 35`; `run_triocta(ref, n_steps=2000) @ 48`; `checksum(x) @ 59`; `assert_close(a, b, name, rtol=1e-06, atol=1e-08) @ 65`; `validate_hist_schema(hist: dict, *, n_steps_expected: int \| None=None, name: str='hist') @ 74`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `REFS_JSON = 'golden/golden_refs.json' @ 13`; `refs = json.loads(Path(REFS_JSON).read_text(encoding='utf-8')) @ 138`; `warn_counts = Counter() @ 142`

**Dependencies (static imports):** `collections`, `definitions`, `json`, `model_core`, `numpy`, `pathlib`, `physics_sampler`, `warnings`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A66. [run_triocta_structural_3body_probe.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_triocta_structural_3body_probe.py) — 197 lines

**Role/purpose:** Experimental physics orchestration. Precomputes triad history then drives separate reflecting-box bodies, optional softened Newton gravity.

**Mathematics:** M45,M46. **Outputs:** Internal NPZ/meta, body-world CSV, config JSON.

**Major classes/functions and signature parameters:** `tail_dirs_from_phi(phi_index: int, d24_steps: int) @ 43`; `detect_event(prev_Z: np.ndarray, Z: np.ndarray, prev_stage: int, stage: int, settle_deg: float=15.0, min_norm: float=1e-10) @ 52`; `main() @ 71`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--n_steps', type=int, default=60000) @ 73`; `ap.add_argument('--dt', type=float, default=0.05) @ 74`; `ap.add_argument('--seed', type=int, default=1234) @ 75`; `ap.add_argument('--v0', type=float, default=0.2) @ 77`; `ap.add_argument('--spawn_spread', type=float, default=0.15) @ 78`; `ap.add_argument('--event_turn_deg', type=float, default=15.0) @ 79`; `ap.add_argument('--enable_gravity', action='store_true') @ 81`; `ap.add_argument('--events_before_gravity', type=int, default=400) @ 82`; `ap.add_argument('--G', type=float, default=1.0) @ 83`; `ap.add_argument('--soft', type=float, default=0.01) @ 84`; `ap.add_argument('--grav_dt', type=float, default=None) @ 85`; `ap.add_argument('--out_dir', type=str, default='outputs/threebody_probe') @ 87`

**Dependencies (static imports):** `__future__`, `argparse`, `json`, `model_core`, `numpy`, `pandas`, `pathlib`, `time`, `triocta_probe_utils`, `uuid`.

**Recorded/file output sites:** `np.savez_compressed(out_root / 'internal_history.npz', **{k: v for k, v in hist.items() if k != '_meta'}) @ 105`; `df.to_csv(out_root / 'seed_world.csv', index=False) @ 180`; `json.dump(hist.get('_meta', {}), f, indent=2) @ 107`; `json.dump(cfg, f, indent=2) @ 186`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A67. [run_unified_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_unified_diagnostics.py) — 589 lines

**Role/purpose:** AI-memory diagnostics orchestration. Unified gate/slip/external-seed runner adding option foreclosure and persistence thresholds.

**Mathematics:** M26–M30,M46. **Outputs:** Per-step/event/summary CSV, optional external trajectories and foreclosure fields.

**Major classes/functions and signature parameters:** `_wrap_angle_pi(a: float) @ 30`; `detect_slip(phi_prev: float, phi_now: float, slip_tol: float=0.25) @ 34`; `is_finite_state(state: ModelState) @ 48`; `_init_omega0(seed: int, scale: float=0.1) @ 58`; `class RunCfg @ 64`; `run_one(cfg: RunCfg, outdir: Path) @ 113`; `main() @ 487`

**State/configuration objects:** `RunCfg: seed: int @ 65`; `RunCfg: gap_center0: float @ 66`; `RunCfg: gap_center1: float @ 67`; `RunCfg: gap_center2: float @ 68`; `RunCfg: eps: float @ 69`; `RunCfg: g: float @ 70`; `RunCfg: dt: float @ 71`; `RunCfg: steps: int @ 72`; `RunCfg: k_mode: str @ 73`; `RunCfg: k_alpha: float @ 74`; `RunCfg: lambda_phase: float @ 75`; `RunCfg: lf_alpha: float @ 77`; `RunCfg: lf_persist: int @ 78`; `RunCfg: lf_enable: bool @ 81`; `RunCfg: lf_stride: int @ 82`; `RunCfg: lf_delta: float @ 83`; `RunCfg: lf_K: int @ 84`; `RunCfg: lf_N: int @ 85`; `RunCfg: lf_eps_corridor: float @ 86`; `RunCfg: lf_eta: float @ 87`; `RunCfg: lf_s_thresh: float @ 88`; `RunCfg: lf_warmup: int @ 89`; `RunCfg: n_sectors: int @ 92`; `RunCfg: gap_center_deg: float @ 93`; `RunCfg: gap_width_deg: float @ 94`; `RunCfg: require_coherence: bool @ 95`; `RunCfg: coherence_min: float @ 96`; `RunCfg: emission_mode: str @ 97`; `RunCfg: slip_tol: float @ 100`; `RunCfg: jeff_zero: float @ 101`; `RunCfg: log_stride: int @ 104`; `RunCfg: spawn_external: bool @ 107`; `RunCfg: seed_speed: float @ 108`; `RunCfg: seed_drag: float @ 109`; `RunCfg: seed_trail_len: int @ 110`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--outdir', type=str, default='outputs_patch39_unified') @ 489`; `ap.add_argument('--seed_lo', type=int, default=0) @ 491`; `ap.add_argument('--seed_hi', type=int, default=3) @ 492`; `ap.add_argument('--gap_center0', type=float, default=0.0) @ 494`; `ap.add_argument('--gap_center1', type=float, default=7.0) @ 495`; `ap.add_argument('--gap_center2', type=float, default=-7.0) @ 496`; `ap.add_argument('--eps', type=float, default=0.05) @ 498`; `ap.add_argument('--g', type=float, default=0.2) @ 499`; `ap.add_argument('--dt', type=float, default=0.05) @ 500`; `ap.add_argument('--steps', type=int, default=20000) @ 501`; `ap.add_argument('--k_mode', type=str, default='theta_soft') @ 503`; `ap.add_argument('--k_alpha', type=float, default=1.0) @ 504`; `ap.add_argument('--lambda_phase', type=float, default=0.0) @ 506`; `ap.add_argument('--lf_alpha', type=float, default=0.1) @ 508`; `ap.add_argument('--lf_persist', type=int, default=2) @ 509`; `ap.add_argument('--lf_enable', action='store_true') @ 512`; `ap.add_argument('--lf_stride', type=int, default=50) @ 513`; `ap.add_argument('--lf_delta', type=float, default=0.0001) @ 514`; `ap.add_argument('--lf_K', type=int, default=5) @ 515`; `ap.add_argument('--lf_N', type=int, default=24) @ 516`; `ap.add_argument('--lf_eps_corridor', type=float, default=0.05) @ 517`; `ap.add_argument('--lf_eta', type=float, default=1e-08) @ 518`; `ap.add_argument('--lf_s_thresh', type=float, default=0.2) @ 519`; `ap.add_argument('--lf_warmup', type=int, default=200) @ 520`; `ap.add_argument('--n_sectors', type=int, default=24) @ 523`; `ap.add_argument('--gap_center_deg', type=float, default=0.0) @ 524`; `ap.add_argument('--gap_width_deg', type=float, default=5.0) @ 525`; `ap.add_argument('--require_coherence', action='store_true') @ 526`; `ap.add_argument('--coherence_min', type=float, default=0.65) @ 527`; `ap.add_argument('--emission_mode', type=str, default='partial', choices=['partial', 'coherent']) @ 528`; `ap.add_argument('--slip_tol', type=float, default=0.25) @ 531`; `ap.add_argument('--jeff_zero', type=float, default=1e-06) @ 532`; `ap.add_argument('--log_stride', type=int, default=10) @ 535`; `ap.add_argument('--spawn_external', action='store_true') @ 538`; `ap.add_argument('--seed_speed', type=float, default=1.0) @ 539`; `ap.add_argument('--seed_drag', type=float, default=0.02) @ 540`; `ap.add_argument('--seed_trail_len', type=int, default=200) @ 541`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `csv`, `dataclasses`, `definitions`, `latent_foreclosure`, `math`, `model_core`, `numpy`, `pathlib`, `phase_triad_sync`, `seed_emission`, `seed_entities`, `trajectory_logging`, `typing`.

**Recorded/file output sites:** `w.writerow(row) @ 466`; `w_step.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'finite': finite, 'lf_V_opt': lf_V_opt, 'lf_R_opt': lf_R_opt, 'lf_survival_frac': lf_surv, 'S_mag': S_mag … [see source] @ 380`; `w_evt.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'event_type': 'slip', 'channel': '', 'S_mag': S_mag, 'Phi_coll': Phi_coll, 'J_eff': J, 'kappa': kappa}) @ 298`; `w_evt.writerow({'seed': cfg.seed, 'step': step_i, 'phi_index': phi_index, 'event_type': 'emit', 'channel': int(ch), 'S_mag': float(S_mag), 'Phi_coll': float(Phi_coll), 'J_eff': flo … [see source] @ 368`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A68. [sanity_report.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/sanity_report.py) — 130 lines

**Role/purpose:** Diagnostics. Runs configurable histories and prints finite/commit/tail statistics.

**Mathematics:** M17,M43. **Outputs:** Console sanity tables; no mathematical acceptance implied.

**Major classes/functions and signature parameters:** `make_initial_state(seed: int) @ 9`; `run_once(seed: int, steps: int, eps: float, g: float, k3_scale: float, dt: float) @ 24`; `first_commit_time(J: np.ndarray, t: np.ndarray, thr: float=1e-06, hold: int=50) @ 31`; `stats_vec(name, X) @ 44`; `main() @ 56`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `EPS = 1e-12 @ 7`

**CLI controls/defaults:** `ap.add_argument('--seed', type=int, required=True) @ 58`; `ap.add_argument('--steps', type=int, default=2000) @ 59`; `ap.add_argument('--eps', type=float, required=True) @ 60`; `ap.add_argument('--g', type=float, required=True) @ 61`; `ap.add_argument('--k3_scale', type=float, required=True) @ 62`; `ap.add_argument('--dt', type=float, required=True) @ 63`; `ap.add_argument('--n_corridors', type=int, default=12) @ 64`

**Dependencies (static imports):** `argparse`, `definitions`, `model_core`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A69. [scan_rgd_connection.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/scan_rgd_connection.py) — 425 lines

**Role/purpose:** Analysis orchestration. Grid/random connection study with per-seed rows and aggregated confidence intervals.

**Mathematics:** M42–M44. **Outputs:** Rows CSV, aggregate CSV and JSON run metadata.

**Major classes/functions and signature parameters:** `linspace_inclusive(lo: float, hi: float, n: int) @ 34`; `ensure_dir(path: str) @ 39`; `now_tag() @ 42`; `stable_hash(obj: Dict[str, Any]) @ 45`; `as_float(x: Any) @ 49`; `as_int(x: Any) @ 55`; `run_one(*, eps: float, g: float, k3_scale: float, dt: float, n_steps: int, seed: int, noise_sigma: float, do_rsb: bool, rsb_steps: int, version: Optional[str]) @ 62`; `wilson_ci(k: int, n: int, z: float=1.96) @ 119`; `bootstrap_mean_ci(x: np.ndarray, n_boot: int=5000, alpha: float=0.05, rng: np.random.Generator \| None=None) @ 135`; `aggregate_rows(rows: List[Dict[str, Any]]) @ 156`; `main() @ 273`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--outdir', type=str, default='outputs') @ 275`; `ap.add_argument('--tag', type=str, default='') @ 276`; `ap.add_argument('--grid', action='store_true', help='Grid scan (default).') @ 278`; `ap.add_argument('--random', action='store_true', help='Random scan.') @ 279`; `ap.add_argument('--eps', nargs=3, type=float, default=[0.02, 0.3, 11], metavar=('LO', 'HI', 'N')) @ 281`; `ap.add_argument('--g', nargs=3, type=float, default=[0.1, 0.3, 11], metavar=('LO', 'HI', 'N')) @ 282`; `ap.add_argument('--k3', nargs=3, type=float, default=[0.5, 2.0, 9], metavar=('LO', 'HI', 'N')) @ 283`; `ap.add_argument('--n-points', type=int, default=300, help='For --random only.') @ 285`; `ap.add_argument('--seeds', type=int, default=64) @ 286`; `ap.add_argument('--seed0', type=int, default=1) @ 287`; `ap.add_argument('--dt', type=float, default=0.05) @ 289`; `ap.add_argument('--n-steps', type=int, default=300) @ 290`; `ap.add_argument('--noise-sigma', type=float, default=0.0) @ 291`; `ap.add_argument('--do-rsb', action='store_true') @ 293`; `ap.add_argument('--rsb-steps', type=int, default=300) @ 294`; `ap.add_argument('--version', type=str, default=None) @ 295`; `ap.add_argument('--aggregate', action='store_true') @ 297`

**Dependencies (static imports):** `__future__`, `argparse`, `csv`, `hashlib`, `json`, `numpy`, `os`, `rgd_connection_diagnostics`, `time`, `typing`.

**Recorded/file output sites:** `json.dump({'run_id': run_id, **meta}, f, indent=2, sort_keys=True) @ 349`; `writer.writerow(row) @ 384`; `w.writerow(r) @ 417`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A70. [seed_emission.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/seed_emission.py) — 103 lines

**Role/purpose:** AI-memory event logic. Phase/coherence gap predicates and copied seed payload.

**Mathematics:** M02,M27. **Outputs:** GapGate, flags/channel selections and payload dictionaries.

**Major classes/functions and signature parameters:** `wrap_pi(a: np.ndarray) @ 7`; `triad_coherence_from_omega(Omega: np.ndarray) @ 10`; `class GapGate @ 17`; `GapGate._gap_center_rad(self) @ 29`; `GapGate._gap_width_rad(self) @ 32`; `channel_angles(Omega: np.ndarray, phi_index: int, n_sectors: int) @ 35`; `in_gap(theta: np.ndarray, center: float, halfwidth: float) @ 50`; `check_emission(state, gate: GapGate) @ 53`; `make_payload(state, channel: int, extra: Dict[str, Any] \| None=None) @ 85`

**State/configuration objects:** `GapGate: n_sectors: int = 24 @ 22`; `GapGate: gap_center_deg: float = 0.0 @ 23`; `GapGate: gap_width_deg: float = 5.0 @ 24`; `GapGate: require_coherence: bool = False @ 25`; `GapGate: coherence_min: float = 0.65 @ 26`; `GapGate: mode: str = 'partial' @ 27`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `dataclasses`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_patch39_unified.py`, `run_unified_diagnostics.py`

**Known tests/examples (static reachability):** `run_patch39_unified.py`, `run_unified_diagnostics.py` No execution claimed.

### A71. [seed_entities.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/seed_entities.py) — 122 lines

**Role/purpose:** AI-memory external evolution. Mutable SeedEntity/SeedWorld with drift/drag integration and trails.

**Mathematics:** M28. **Outputs:** External positions/velocities, entities and snapshot histories.

**Major classes/functions and signature parameters:** `_as3(x) @ 8`; `class SeedEntity @ 13`; `SeedEntity.push_trail(self, maxlen: int=200) @ 38`; `class SeedWorld @ 45`; `SeedWorld.spawn(self, born_step: int, channel: int, pos: np.ndarray, vel: np.ndarray, payload: Optional[Dict[str, Any]]=None) @ 58`; `SeedWorld.step(self) @ 90`; `SeedWorld.snapshot_trails(self) @ 114`

**State/configuration objects:** `SeedEntity: eid: int @ 21`; `SeedEntity: born_step: int @ 22`; `SeedEntity: channel: int @ 23`; `SeedEntity: pos: np.ndarray @ 24`; `SeedEntity: vel: np.ndarray @ 25`; `SeedEntity: vel0: np.ndarray @ 26`; `SeedEntity: payload: Dict[str, Any] = field(default_factory=dict) @ 27`; `SeedEntity: trail: List[np.ndarray] = field(default_factory=list) @ 29`; `SeedEntity: alive: bool = True @ 30`; `SeedEntity: r_history: List[float] = field(default_factory=list) @ 33`; `SeedEntity: z_history: List[float] = field(default_factory=list) @ 34`; `SeedEntity: x_history: List[float] = field(default_factory=list) @ 35`; `SeedEntity: y_history: List[float] = field(default_factory=list) @ 36`; `SeedWorld: dt: float = 1.0 @ 50`; `SeedWorld: drag: float = 0.02 @ 51`; `SeedWorld: drift: np.ndarray = field(default_factory=lambda: np.zeros(3)) @ 52`; `SeedWorld: trail_len: int = 200 @ 53`; `SeedWorld: entities: List[SeedEntity] = field(default_factory=list) @ 55`; `SeedWorld: _next_id: int = 1 @ 56`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `dataclasses`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_patch39_unified.py`, `run_unified_diagnostics.py`

**Known tests/examples (static reachability):** `run_patch39_unified.py`, `run_unified_diagnostics.py` No execution claimed.

### A72. [seed_trajectory_analysis.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/seed_trajectory_analysis.py) — 23 lines

**Role/purpose:** AI-memory analysis. Heuristic radial trajectory class.

**Mathematics:** M29. **Outputs:** Escape/return/grazing/unknown string according to finite-length rules.

**Major classes/functions and signature parameters:** `classify_trajectory(r_history, eps: float=1e-06, min_samples: int=200) @ 5`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A73. [select_golden_points.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/select_golden_points.py) — 138 lines

**Role/purpose:** Tests / reproducibility. Samples saved stable/edge/expected-failure rows into fixed selected points.

**Mathematics:** M52. **Outputs:** Golden-point configuration JSON/table.

**Major classes/functions and signature parameters:** `first_existing(df, cols) @ 12`; `stable_mask(df) @ 18`; `sample_rows(d, n, sort_key=None, ascending=True) @ 68`; `pack(label, subdf) @ 112`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `SCAN_CSV = 'outputs/wide_scan_triocta_ultra.csv' @ 8`; `OUT_JSON = 'golden/golden_points.json' @ 9`; `df = pd.read_csv(SCAN_CSV) @ 37`; `req = ['eps', 'g', 'k3_scale', 'dt', 'seed'] @ 40`; `vcol = first_existing(df, ['vrec_mean', 'v_rec_mean', 'vrec_max', 'v_rec_max']) @ 45`; `stable = df[stable_mask(df)].copy() @ 54`; `eps_star = 0.2447 @ 66`; `core_pool = stable[stable['eps'] <= 0.01] @ 76`; `core = sample_rows(core_pool, 4, sort_key='eps', ascending=True) @ 77`; `edge_pool = stable[(stable['eps'] >= 0.15) & (stable['eps'] <= 0.23)] @ 80`; `knee_pool = stable[(stable['eps'] >= eps_star - 0.02) & (stable['eps'] <= eps_star - 0.0001)] @ 94`; `knee_pool = knee_pool.copy() @ 95`; `knee_pool['_knee_dist'] = np.abs(knee_pool['eps'] - (eps_star - 0.0005)) @ 96`; `near_knee = knee_pool.sort_values('_knee_dist', ascending=True).head(2) @ 97`; `fail_pool = df[df['eps'] >= eps_star + 0.01].copy() @ 101`; `goldens = {'scan_csv': SCAN_CSV, 'eps_star': eps_star, 'vcol_used': vcol, 'points': pack('stable_core', core) + pack('edge_band', edge) + pack('near_knee', near_knee) + pack('expected_fail', expected_fail)} @ 125`

**Dependencies (static imports):** `json`, `numpy`, `pandas`, `pathlib`.

**Recorded/file output sites:** `Path(OUT_JSON).write_text(json.dumps(goldens, indent=2), encoding='utf-8') @ 137`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A74. [semantic_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/semantic_diagnostics.py) — 135 lines

**Role/purpose:** Visualization / analysis. Axis alignment, jump spectrum and CP/cycle statistics over projected histories.

**Mathematics:** M10–M12,M50. **Outputs:** Figures and label/statistic tables.

**Major classes/functions and signature parameters:** `_get_uxy_path(history) @ 9`; `plot_axis_alignment(history) @ 20`; `plot_jump_spectrum(history) @ 55`; `cp_cycle_stats(history) @ 98`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `cp_windows`, `matplotlib.pyplot`, `numpy`, `su3_basis`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_sim.py`

**Known tests/examples (static reachability):** `run_sim.py` No execution claimed.

### A75. [side_zchiral_probe.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/side_zchiral_probe.py) — 135 lines

**Role/purpose:** Analysis / visualization. Compares normalized phase-only chirality, log amplitudes, turning and closure.

**Mathematics:** M07,M15,M41. **Outputs:** Correlation/loop metrics and figures.

**Major classes/functions and signature parameters:** `make_initial_state(seed: int) @ 9`; `run_once(seed: int, steps: int, eps: float, g: float, k3_scale: float, dt: float) @ 24`; `phase_only_chiral(Omega_hist: np.ndarray) @ 33`; `curvature_proxy(P: np.ndarray) @ 46`; `main() @ 61`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `EPS = 1e-12 @ 7`

**CLI controls/defaults:** `ap.add_argument('--seed', type=int, default=2158500047) @ 63`; `ap.add_argument('--steps', type=int, default=2000) @ 64`; `ap.add_argument('--eps', type=float, default=0.02) @ 65`; `ap.add_argument('--g', type=float, default=0.15) @ 66`; `ap.add_argument('--k3_scale', type=float, default=1.0) @ 67`; `ap.add_argument('--dt', type=float, default=0.01) @ 68`; `ap.add_argument('--zkey', type=str, default='Z_chiral', choices=['Z_chiral', 'Z_total', 'Z_macro']) @ 69`

**Dependencies (static imports):** `argparse`, `definitions`, `model_core`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A76. [sims_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/sims_diagnostics.py) — 101 lines

**Role/purpose:** Diagnostics state. Accumulates finite-step survival and event/slip/emission counters.

**Mathematics:** M43,M46. **Outputs:** SIMSRunRow and summary metrics; bookkeeping state only.

**Major classes/functions and signature parameters:** `class SIMSRunRow @ 21`; `class SIMSDiagnostics @ 36`; `SIMSDiagnostics.__init__(self, *, theta_used: float=0.0) @ 51`; `SIMSDiagnostics._censor(t: Optional[int], t_end: int) @ 62`; `SIMSDiagnostics.update_step(self, step: int, *, finite: bool) @ 66`; `SIMSDiagnostics.on_emit(self, step: int, *, n_events: int=1) @ 71`; `SIMSDiagnostics.on_slip(self, step: int) @ 80`; `SIMSDiagnostics.finalize(self, *, t_end: int) @ 87`; `SIMSDiagnostics.as_dict(self, *, t_end: int) @ 99`

**State/configuration objects:** `SIMSRunRow: t_nonfinite: int @ 23`; `SIMSRunRow: t_first_emit: int @ 24`; `SIMSRunRow: t_first_slip: int @ 25`; `SIMSRunRow: emit_events_total: int @ 28`; `SIMSRunRow: slip_count: int @ 29`; `SIMSRunRow: theta_used: float @ 32`; `SIMSRunRow: t_end: int @ 33`

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `__future__`, `dataclasses`, `math`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_sims_minimal.py`

**Known tests/examples (static reachability):** `run_sims_minimal.py` No execution claimed.

### A77. [spectral_viz.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/spectral_viz.py) — 274 lines

**Role/purpose:** Visualization / passive analysis. Alternate spectral energy, base-2 entropy and dominant-band helpers.

**Mathematics:** M23,M48. **Outputs:** Arrays plus waterfall/spectrum/timeline plots; entropy differs from normalized canonical helper.

**Major classes/functions and signature parameters:** `compute_spectral_entropy_series(E_t_m: np.ndarray, eps: float=1e-12, log_base: float=2.0) @ 10`; `plot_spectral_entropy_series(E_t_m: np.ndarray, ax: plt.Axes \| None=None, log_base: float=2.0, title: str \| None='Spectral entropy timeline', label: str \| None=None) @ 56`; `compute_spectral_energy_series(psi_hist) @ 98`; `plot_spectral_waterfall(E_tm, t_vals=None, title=None, log_scale=True, ax=None) @ 118`; `plot_final_spectrum(E_tm, title=None, ax=None) @ 175`; `compute_dominant_band_series(E_t_m: np.ndarray) @ 209`; `plot_dominant_band_series(dom_band_series: np.ndarray, ax: plt.Axes \| None=None, label: str \| None=None, title: str \| None=None) @ 227`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `matplotlib.pyplot`, `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `rsb_entropy_demo.py`, `rsb_spectral_demo.py`, `rsb_spectral_viz.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_entropy_demo.py`, `rsb_spectral_demo.py` No execution claimed.

### A78. [su3_basis.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/su3_basis.py) — 32 lines

**Role/purpose:** Geometry / passive analysis. Normalizes channel intensities and projects onto real orthonormal u/x/y basis.

**Mathematics:** M09,M10. **Outputs:** Weights and real coordinate triple.

**Major classes/functions and signature parameters:** `weights_from_Omega(Omega: np.ndarray) @ 12`; `project_to_uxy(Omega: np.ndarray) @ 23`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `u = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0) @ 5`; `x = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0) @ 6`; `y = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0) @ 7`; `B = np.column_stack([u, x, y]) @ 10`

**Dependencies (static imports):** `numpy`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (import reachable), toy_ui.py (import reachable), toy_lab.py (import reachable), toy_3d_triocta.py (import reachable) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `model_core.py`, `semantic_diagnostics.py`

**Known tests/examples (static reachability):** `generate_golden_refs.py`, `new_run_tests.py`, `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_patch39_unified.py`, `run_seed_emission_csv.py`, `run_sim.py`, `run_sims_minimal.py`, `run_tests.py`, `run_triocta_structural_3body_probe.py`, `run_unified_diagnostics.py` No execution claimed.

### A79. [summarize_edge.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/summarize_edge.py) — 131 lines

**Role/purpose:** Analysis. Groups sweep results into largest observed stable and smallest observed failing coupling.

**Mathematics:** M43. **Outputs:** Summary CSV/printed finite-horizon edge table.

**Major classes/functions and signature parameters:** `_require_columns(df: pd.DataFrame, cols: List[str]) @ 28`; `_as_int_or_blank(x) @ 34`; `summarize(df: pd.DataFrame, group_keys: List[str], stable_label: str='stable') @ 46`; `main() @ 98`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--in', dest='inp', default='sweep_edge.csv', help='Input CSV (default: sweep_edge.csv)') @ 100`; `ap.add_argument('--out', dest='out', default='sweep_edge_summary.csv', help='Output CSV (default: sweep_edge_summary.csv)') @ 101`; `ap.add_argument('--by-seed', action='store_true', help='Group by seed as well (seed, eps, k3_scale) if seed column exists') @ 102`; `ap.add_argument('--stable-label', default='stable', help='Regime label treated as stable (default: "stable")') @ 103`; `ap.add_argument('--print', action='store_true', help='Print summary to stdout') @ 104`

**Dependencies (static imports):** `__future__`, `argparse`, `numpy`, `pandas`, `sys`, `typing`.

**Recorded/file output sites:** `summary.to_csv(args.out, index=False) @ 114`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A80. [summarize_ray_alignment.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/summarize_ray_alignment.py) — 31 lines

**Role/purpose:** Analysis. Aggregates saved per-event ray-distance metrics.

**Mathematics:** M46. **Outputs:** Printed parameter/ray-alignment summary.

**Major classes/functions and signature parameters:** No top-level definitions; source is a script/package marker.

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `files = glob.glob(os.path.join('outputs_patch39_unified', '**', 'seed_trajectories_seed*.csv'), recursive=True) @ 5`; `df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True) @ 6`; `df = df.dropna(subset=['lambda_phase', 'channel', 'traj_class', 'dist_to_ray_deg']) @ 8`; `df['dist_to_ray_deg'] = df['dist_to_ray_deg'].astype(float) @ 9`; `thresholds = [2, 5, 10, 15, 30] @ 11`; `rows = [] @ 13`; `res = pd.DataFrame(rows).sort_values(['lambda_phase', 'channel', 'traj_class']) @ 27`; `outpath = os.path.join('outputs_patch39_unified', 'ray_alignment_summary.csv') @ 28`

**Dependencies (static imports):** `glob`, `numpy`, `os`, `pandas`.

**Recorded/file output sites:** `res.to_csv(outpath, index=False) @ 29`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A81. [tangent_corridor_analysis.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/tangent_corridor_analysis.py) — 272 lines

**Role/purpose:** Geometry diagnostics / analysis. Compares display tangents, clusters scalar changes and CP-splits arrival events.

**Mathematics:** M38,M39. **Outputs:** Alignment/cluster/event arrays, statistics and plots.

**Major classes/functions and signature parameters:** `detect_tangent_corridors(history, R=2.0) @ 11`; `cluster_delta_kz(history, frac_of_max=0.5, n_clusters=3) @ 84`; `cp_split_big_delta_events(history, big_steps_mask, mags, cp_cfg=None) @ 208`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.cp_windows`, `matplotlib.pyplot`, `numpy`, `scipy.cluster.vq`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `diagnostics.py`, `run_sim.py`

**Known tests/examples (static reachability):** `rsb_dom_band_demo.py`, `rsb_spectral_demo.py`, `run_sim.py` No execution claimed.

### A82. [toy_3d_triocta.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_3d_triocta.py) — 1029 lines

**Role/purpose:** UI / visualization. 3D channel-torus apparatus with scaled Z, RSB context and manual trail control.

**Mathematics:** M08,M14,M17,M18,M25,M34,M35,M37,M47,M52. **Outputs:** Interactive Matplotlib figures and automatic timeseries CSV; section5.5.

**Major classes/functions and signature parameters:** `_vrec_geom(history: dict, z_key: str='Z_total') @ 80`; `_jeff_series(history: dict, obs: dict \| None=None) @ 92`; `tri_to_rsb_params(tri_obs, base_alpha: float=0.6) @ 102`; `run_triocta(eps: float, g: float, k3_scale: float, noise_sigma: float, n_steps: int=300, dt: float=0.05, seed: int=42, do_rsb: bool=True, rsb_steps: int=300) @ 138`; `embed_on_torus(omega_hist: np.ndarray, R: float=2.0, r0: float=0.6, mag_scale: float=0.4) @ 283`; `compute_phi_index(Omega, n_corridors: int=12) @ 327`; `detect_meta_shell_time(t, Z, window_frac=0.1, z_min=0.05) @ 336`; `dump_timeseries_csv(history, obs, tag='auto') @ 347`; `launch_3d_lab() @ 377`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `VERSION = '3.5' @ 53`

**Dependencies (static imports):** `.constants_selector`, `.definitions`, `.geometry_3d`, `.model_core`, `.physics_sampler`, `.provenance`, `.rsb_model`, `csv`, `datetime`, `kernel`, `matplotlib.pyplot`, `matplotlib.widgets`, `mpl_toolkits.mplot3d`, `mpl_toolkits.mplot3d.art3d`, `numpy`, `os`, `sys`.

**Recorded/file output sites:** `dump_timeseries_csv(hist, obs, tag='startup') @ 402`; `writer.writerow(['t', 'Z', 'J_eff', 'phi_index']) @ 366`; `dump_timeseries_csv(hist, obs, tag='rerun') @ 1013`; `writer.writerow([t[i], z[i], J[i], phi[i]]) @ 368`; `dump_timeseries_csv(hist, obs, tag='onclose') @ 1022`

**Visual consumers:** toy_3d_triocta.py (self) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A83. [toy_lab.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_lab.py) — 366 lines

**Role/purpose:** UI / visualization. Two scalar panels plus clock-occupancy polar lab.

**Mathematics:** M01–M08,M17,M39,M47. **Outputs:** Interactive plots and per-run scalar history; section5.3.

**Major classes/functions and signature parameters:** `compute_phi_index(Omega, n_corridors=12) @ 52`; `run_model(eps, g, k3_scale, noise_sigma, n_steps: int=200, dt: float=0.05, seed: int=42) @ 62`; `launch_lab() @ 121`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.constants_selector`, `.definitions`, `.model_core`, `.physics_sampler`, `kernel`, `matplotlib.pyplot`, `matplotlib.widgets`, `numpy`, `os`, `sys`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_lab.py (self) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A84. [toy_ui.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_ui.py) — 755 lines

**Role/purpose:** UI / visualization. Combined triad/RSB apparatus with Z and composite-v_rec controls.

**Mathematics:** M01–M08,M13,M19–M25,M33,M47,M52. **Outputs:** Interactive main figure, RSB popup/sweep figures and seed summaries; section5.4.

**Major classes/functions and signature parameters:** `run_rsb_once(rsb_params, n_steps=300, seed=0) @ 72`; `format_regime_summary(rsb_stats) @ 122`; `run_model(eps, g, k3_scale, noise_sigma, n_steps=200, dt=0.05, seed=42) @ 167`; `launch_ui() @ 240`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `VERSION = '3.7' @ 41`; `_REGIME_VERDICT = {'I': 'oscillatory / reversible', 'II': 'structured attractor', 'III': 'spectral collapse', 'T': 'transitional / boundary'} @ 114`

**Dependencies (static imports):** `.constants_selector`, `.definitions`, `.geometry_3d`, `.model_core`, `.physics_sampler`, `.provenance`, `.rsb_model`, `.rsb_spectral_viz`, `dataclasses`, `kernel`, `matplotlib.pyplot`, `matplotlib.widgets`, `mpl_toolkits.mplot3d`, `numpy`, `os`, `sys`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui.py (self) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A85. [toy_ui_live.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/toy_ui_live.py) — 233 lines

**Role/purpose:** UI / visualization. Single-button triad-plus-conditioned-RSB apparatus.

**Mathematics:** M01–M08,M19–M25,M47. **Outputs:** Main scalar plots, RSB popups and summary text; section5.2.

**Major classes/functions and signature parameters:** `run_triocta(eps, g, k3_scale, noise_sigma, n_steps=200, dt=0.05, seed=None) @ 52`; `tri_to_rsb_params_live(tri_obs, base_alpha) @ 85`; `launch_live_ui() @ 108`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.constants_selector`, `.definitions`, `.model_core`, `.physics_sampler`, `.rsb_model`, `.rsb_spectral_viz`, `kernel`, `matplotlib.pyplot`, `matplotlib.widgets`, `numpy`, `os`, `sys`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** toy_ui_live.py (self) Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A86. [trajectory_logging.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/trajectory_logging.py) — 90 lines

**Role/purpose:** AI-memory persistence. Append-only external trajectory snapshot logging.

**Mathematics:** M30. **Outputs:** JSONL snapshots and summary records.

**Major classes/functions and signature parameters:** `_now_ts() @ 11`; `class TrajectoryLogger @ 14`; `TrajectoryLogger.__init__(self, root_dir: str, filename: str='trajectories.jsonl', *, use_daily_rotation: bool=True) @ 29`; `TrajectoryLogger._today_path(self) @ 48`; `TrajectoryLogger.log_entity(self, ent: Any, step: int) @ 59`

**State/configuration objects:** Class instance state is set in the constructors/methods listed above; no annotated class defaults.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**Dependencies (static imports):** `.pathing`, `__future__`, `json`, `numpy`, `os`, `time`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_patch39_unified.py`, `run_unified_diagnostics.py`

**Known tests/examples (static reachability):** `run_patch39_unified.py`, `run_unified_diagnostics.py` No execution claimed.

### A87. [triocta_probe_utils.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/triocta_probe_utils.py) — 77 lines

**Role/purpose:** Experimental physics / geometry. Boundary reflection, angular ray matching and softened three-body Verlet helpers.

**Mathematics:** M45,M46. **Outputs:** Reflected positions/velocities, angular matches and accelerations/steps.

**Major classes/functions and signature parameters:** `unit(v: Vec3, eps: float=1e-12) @ 17`; `reflect_1d(x: float) @ 24`; `reflect_with_velocity(r: Vec3, v: Vec3) @ 32`; `wrap_pi(a: float) @ 44`; `nearest_six_ray(phi: float) @ 47`; `accel_newton_3(r: np.ndarray, m: np.ndarray, G: float=1.0, soft: float=0.01) @ 54`; `verlet_step_3(r: np.ndarray, v: np.ndarray, m: np.ndarray, dt: float, G: float=1.0, soft: float=0.01) @ 71`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `Vec3 = np.ndarray @ 15`

**Dependencies (static imports):** `__future__`, `numpy`, `typing`.

**Recorded/file output sites:** No selected file-export call found in this module; return values/console/figures or delegated output are described above.

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** `run_triocta_structural_3body_probe.py`

**Known tests/examples (static reachability):** `run_triocta_structural_3body_probe.py` No execution claimed.

### A88. [wide_scan_triocta.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/wide_scan_triocta.py) — 341 lines

**Role/purpose:** Analysis orchestration. Multiprocessing broad parameter sampling with finite/occupancy/tail metrics.

**Mathematics:** M43,M44. **Outputs:** Scan CSV rows and sampled parameter records.

**Major classes/functions and signature parameters:** `corridor_entropy(phi_index: np.ndarray, n_corridors: int=12) @ 47`; `tail_stats(x: np.ndarray, tail_frac: float=0.5) @ 57`; `pctl(x: np.ndarray, q: float) @ 65`; `stable_flags(history: Dict[str, Any], obs: Dict[str, Any]) @ 71`; `run_one(params_dict: Dict[str, Any], seed: int, n_steps: int, dt: float) @ 101`; `sample_params(rng: np.random.Generator) @ 227`; `write_rows(path: str, rows: List[Dict[str, Any]]) @ 264`; `_task(job: Tuple[int, Dict[str, Any], int, int, float]) @ 281`; `main() @ 292`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** `VERSION = '3.5' @ 41`

**CLI controls/defaults:** `ap.add_argument('--n_points', type=int, default=2000, help='number of parameter points') @ 294`; `ap.add_argument('--seeds_per_point', type=int, default=4, help='seeds per parameter point') @ 295`; `ap.add_argument('--seed0', type=int, default=42, help='master seed for scan generator') @ 296`; `ap.add_argument('--n_steps', type=int, default=1000) @ 297`; `ap.add_argument('--dt', type=float, default=0.05) @ 298`; `ap.add_argument('--workers', type=int, default=0, help='0 = auto') @ 299`; `ap.add_argument('--out', type=str, default='outputs/wide_scan_triocta.csv') @ 300`; `ap.add_argument('--chunk', type=int, default=64, help='write results in chunks') @ 301`; `ap.add_argument('--chunksize', type=int, default=1, help='pool imap chunk size') @ 302`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `csv`, `definitions`, `math`, `model_core`, `multiprocessing`, `numpy`, `os`, `physics_sampler`, `provenance`, `typing`.

**Recorded/file output sites:** `w.writerow(r) @ 275`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A89. [z_spike_diagnostic.py](C:/TORMENT/TRIOCTAGON_new/kernel_TO/z_spike_diagnostic.py) — 287 lines

**Role/purpose:** Diagnostics / visualization. Finds large full-v_rec transitions and exports selected local windows.

**Mathematics:** M13,M33. **Outputs:** History/series/spike CSV, metadata and Z/diagnostic plots.

**Major classes/functions and signature parameters:** `run_triocta_once(seed: int, eps: float, g: float, k3_scale: float, dt: float, steps: int) @ 29`; `safe_xyz(hist: dict, z_key: str) @ 64`; `pick_spikes(v: np.ndarray, mode: str, value: float) @ 72`; `write_outputs(hist: dict, z_key: str, include_dkappa: bool, outdir: str, spike_mode: str, spike_value: float, window: int, last_n_3d: int) @ 94`; `main() @ 245`

**State/configuration objects:** No persistent state class defined here; inputs, local arrays/tables and/or imported model state as described above.

**Additional parameters/constants:** Defaults are in signatures/configuration above and registry; no short module-level assignment.

**CLI controls/defaults:** `ap.add_argument('--seed', type=int, required=True) @ 247`; `ap.add_argument('--eps', type=float, required=True) @ 248`; `ap.add_argument('--g', type=float, required=True) @ 249`; `ap.add_argument('--k3', type=float, required=True, help='k3_scale') @ 250`; `ap.add_argument('--dt', type=float, required=True) @ 251`; `ap.add_argument('--steps', type=int, default=2000) @ 252`; `ap.add_argument('--z_key', type=str, default='Z_total', choices=['Z_total', 'Z_macro', 'Z_chiral']) @ 254`; `ap.add_argument('--include_dkappa', action='store_true') @ 255`; `ap.add_argument('--spike_mode', choices=['pctl', 'abs'], default='pctl') @ 257`; `ap.add_argument('--spike_value', type=float, default=0.99, help='percentile (0..1) if pctl, else absolute threshold') @ 258`; `ap.add_argument('--window', type=int, default=25, help='+/- window (steps) around spike center') @ 259`; `ap.add_argument('--last_n_3d', type=int, default=500, help='plot last N points in 3D (0 = all)') @ 260`; `ap.add_argument('--outdir', type=str, default='z_spike_out') @ 262`

**Dependencies (static imports):** `__future__`, `argparse`, `constants_selector`, `dataclasses`, `definitions`, `geometry_3d`, `matplotlib.pyplot`, `model_core`, `mpl_toolkits.mplot3d`, `numpy`, `os`, `pandas`, `provenance`.

**Recorded/file output sites:** `df_series.to_csv(series_path, index=False) @ 161`; `df_spikes.to_csv(spikes_path, index=False) @ 183`; `plt.savefig(os.path.join(outdir, f'{run_id}_{z_key}_vrec_spikes.png'), dpi=200) @ 195`; `plt.savefig(os.path.join(outdir, f'{run_id}_{z_key}_Z3_time_scatter.png'), dpi=200) @ 225`

**Visual consumers:** No import path from the four requested UIs found; script/plot consumers listed below or purpose above. Scientific use is resolved in section5, not inferred solely from this graph.

**Direct old import consumers:** None found; may be a CLI entry point or read saved files.

**Known tests/examples (static reachability):** No model test/example import path found; CLI/main block or retained data may be its example. No execution claimed.

### A90. [README.md](C:/TORMENT/TRIOCTAGON_new/kernel_TO/README.md) — 293 lines

Historical RSB framework description, module map, UI usage and manual button-test checklist. It claims reproducibility and phase interpretations; these are historical assertions rather than results of this census. No state/functions; parameters described include RSB mixing/gain/contraction and triad sliders. Depends on named scripts and figures. Outputs documentation, not runtime data. Its RSB helper ownership in diagnostics.py disagrees with inspected code. Supports U and RSB demo examples; M19–M25/M51/M52.

### A91. [README_threebody_probe.md](C:/TORMENT/TRIOCTAGON_new/kernel_TO/README_threebody_probe.md) — 24 lines

External probe documentation with default and gravity-enabled CLI examples. No runtime state; declares reflecting box, q-based equal-speed tails, optional Newton gravity after events and no feedback into Omega. Parameters/events/output names belong to M45 and run_triocta_structural_3body_probe. Outputs usage documentation; visual consumer is post-run analyze_threebody_probe. It is an example, not an executed test.

### A92. [run_suite.ps1](C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_suite.ps1) — 61 lines

Batch experiment orchestration; no new evolution equation. Calls run_unified_diagnostics with seed range0–99, (dt,steps)=(.1,10000),(.05,20000),(.025,40000), gap widths24/30/36 degrees and coherence disabled or enabled with minima .8/1/1.2. Fixed lambda_phase=.05, eps=.05,g=.2,log_stride1. Creates output directories and delegates CSV writes. Consumers collect_optional_suite/plot_optional_suite and ray-alignment analysis. It varies number of map updates while fixing dt×steps; threshold1.2 exceeds exact coherence maximum. Dependencies PowerShell, Python and unified runner/import contracts. No suite executed; M26/M27/M43/M46/M54.

## Appendix B. Current and production source cross-index

### Current kernel: 19 referenced source files

**[__init__.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/__init__.py)** — Package surface boundary; no independent old dynamics. Definition locators: No top-level function/class.

**[_contract_types.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_contract_types.py)** — Public immutable value/type validation and construction contracts. Definition locators: `_integer:13`, `_text:22`, `_require:30`, `_values:36`, `_triad:40`, `Provenance:45`, `Parameters:70`, `State:89`, `Seed:102`, `Clock:114`, `StagedConfig:131`, `EMAConfig:147`, `EMAState:162`, `ObserverRequest:176`, `_provenance_data:207`, `_topology:214`

**[_geometry_records.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_geometry_records.py)** — Versioned C01/D03 construction, serialization and validation; does not accept arbitrary old object IDs. Definition locators: `_exact:21`, `_decode_cached:49`, `_decode_exact:86`, `_exact_data:90`, `_exact_input:96`, `_object:106`, `_coordinates:110`, `_paper_c:117`, `_paper_d:140`, `get_geometry:178`, `_point:214`, `_points:218`, `_segments:222`, `_indices:226`, `_render:233`, `GeometryRecord:249`

**[_presets.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py)** — Explicit historical preset values and provenance; not a generic old coefficient-mode menu. Definition locators: `historical_seed:8`, `historical_observer:18`

**[_records.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_records.py)** — Versioned RunRecord/record validation, schema and serialization; different from old logger schema. Definition locators: `_keys:47`, `_string:55`, `_choice:63`, `_int:70`, `_f64:81`, `_complex:93`, `_array:98`, `_bool:106`, `_sha:112`, `_encode:118`, `_canonical:142`, `_digest:146`, `_signed:152`, `_parse:157`, `_freeze:175`, `_Record:183`, `_provenance:214`, `_parameters:219`, `_config:225`, `_selection:231`, `_provenance_git:238`, `_source_checkout:246`, `_distribution_manifest:257`, `_live_source:321`, `_implementation:336`, `_papers:349`, `_producer_environment:362`, `_environment:369`, `_validate_environment:373`, `_metadata:384`, `_definition_ids:427`, `_result:450`, `_diagnostic:459`, `RunRecord:481`

**[_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py)** — Internal numerical response helpers; shipped does not imply a public editable operation. Definition locators: `ResponsePrecisionError:14`, `real_scalar:18`, `complex_vector:32`, `checked_real:52`, `product:64`, `total:72`, `complex_product:81`, `scale_complex:86`, `bra_dot:90`, `checked_array:96`

**[_runner.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py)** — Finite supported run execution and separated observers/readouts with record provenance. Definition locators: `_step:13`, `_selection:21`, `_descriptor:30`, `_observe:38`, `_advance:47`, `_sample:55`, `_append:83`, `run:99`, `resume:156`

**[api.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/api.py)** — Thin supported public facade for dynamics, observers, geometry and versioned records. Definition locators: `step:23`, `z_chiral:27`, `advance_clock:31`, `advance_ema:36`, `observe_staged:41`, `observe_ema:47`, `quadratic_form:54`, `readout_accounting:58`, `chiral_area_accounting:62`, `intensity_budget:66`, `potential:71`, `historical_alignment:76`, `direct_history_coordinates:80`, `cylinder_point:84`, `cylinder_history_coordinates:88`, `history_torus_coordinates:92`

**[boundary_response.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/boundary_response.py)** — Internal response material, not public spatial boundary/gap physics. Definition locators: `_theta:18`, `theta_from_lens:25`, `_small_factor:40`, `lens_area_fraction:55`, `lens_area_gain:70`, `prepare_area_response:86`

**[covering.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/covering.py)** — Exact cycle Laplacians, residue pullback/isometry and reduction; Paper A extension. Definition locators: `_positive_size:8`, `cycle_laplacian:20`, `pullback_matrix:31`, `isometric_pullback:40`

**[dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py)** — Deterministic triad and M-ring recurrence, harmonic-three synchronization; M01/M02 restricted counterpart. Definition locators: `_finite_real:15`, `DynamicsConfig:28`, `_state:48`, `arg0:57`, `phase_sync:66`, `_advance:87`, `step3:99`, `step_ring:107`

**[face_state.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py)** — Internal face-state representation; no general old display-to-shell registration. Definition locators: `_readonly:41`, `FaceFrames:48`, `face_frames:60`, `_decode:66`, `decode_to_faces:73`, `encode_from_faces:83`, `_index:115`, `transport:123`, `area_triple:136`, `state_area:141`, `FaceState:158`

**[geometry.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py)** — Exact accepted Paper C folded width-one geometry and sections; different object from old display tori. Definition locators: `_point:29`, `panel_point:35`, `_face_edges:53`, `FoldedModule:58`, `folded_module:136`, `central_section:153`, `rotate_c3:166`, `reflect_vertical:174`, `reflect_horizontal:180`

**[operating_region.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/operating_region.py)** — Internal operating-region material; not an old empirical gcrit GUI. Definition locators: `_profile:19`, `_config:24`, `bounded_config:34`, `validate_bounded_triad:46`, `validate_uniform_incident_budget:56`, `initialize_bounded_area:65`, `step_bounded_triad:75`

**[readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py)** — Raw quadratic chirality and intensity-related passive quantities; M07, not M08 cubic J. Definition locators: `z_chiral:7`

**[reference_scaffold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/reference_scaffold.py)** — Exact Paper D aligned octagon-reference and alternating-hexagon families; no old angular gate equivalence. Definition locators: `_real:24`, `_positive:35`, `_point:42`, `_input_point:49`, `_index:56`, `_edges:64`, `_r60:68`, `ConvexHull:74`, `HalfPlane:92`, `HalfPlaneIntersection:112`, `Octagon:132`, `ReferenceScaffold:172`, `paper_c_member:339`, `paper_c_rigid_map:345`, `translate_paper_c_to_regular:355`, `shrink_paper_c_at_fixed_centres:364`

**[srg.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/srg.py)** — Fixed/internal spectral initialization construction; not RSBModel recurrence. Definition locators: `NovemberParameters:21`, `SRGOperators:32`, `HelicityMode:42`, `fourier_basis:50`, `fixed_november_srg:57`, `helicity_mode:75`, `project_bra:97`, `extract_helicity:108`, `_transfer_count:114`, `_cycle_gain:122`, `HandoffResult:134`, `handoff_area_response:154`

**[z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py)** — Passive quadratic/Gram/alignment/potential/history-coordinate analyses; M31–M33 relevant. Definition locators: `_freeze:21`, `_seal:27`, `_real:32`, `_array:36`, `_square:47`, `_dot:51`, `_norm:56`, `_divide:61`, `_difference:65`, `_complex_sum:69`, `quadratic_form:75`, `ReadoutAccounting:82`, `readout_accounting:111`, `ChiralAreaAccounting:145`, `chiral_area_accounting:166`, `HistoricalAlignment:186`, `historical_alignment:199`, `_state_parameters:219`, `IntensityBudget:237`, `intensity_budget:256`, `potential:290`, `Coordinates:306`, `direct_history_coordinates:316`, `cylinder_point:331`, `_history:344`, `cylinder_history_coordinates:360`, `HistoryTorus:369`, `history_torus_coordinates:387`

**[z_manifold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py)** — Explicit clocks, staged and separately sourced EMA scalar/readout state; M03/M06. Definition locators: `_integer:21`, `_require:27`, `_freeze:33`, `_real_vector:39`, `Clock:47`, `clock_angle:66`, `advance_clock:75`, `_config_reals:85`, `StagedConfig:91`, `state_norm:103`, `saturated_norm:110`, `_harmonic:117`, `staged_scalar:127`, `macro_vector:145`, `blend_vectors:153`, `ZReadout:165`, `_observe:189`, `observe_staged:197`, `EMAConfig:203`, `EMAState:215`, `cubic_j:226`, `normalized_cubic:233`, `advance_ema:240`, `ema_scalar:254`, `observe_ema:262`, `ConstructorZeroRecord:269`, `historical_constructor_zero:295`

### Production source identity evidence

All21 source modules were read; full-file SHA-256 is included to make byte-equality claims independently checkable. Shared math does not establish copying direction. “Present” below does not imply active runtime usage.

| TOR source | SHA-256 | OLD relationship |
|---|---|---|
| [__init__.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/__init__.py) | `6c010626822f69510ca8a0d1fdee16d4e6cd5dcbaa570623eecee80af3a6e685` | EXACT_CODE_LINEAGE — equal bytes |
| [analyze_seed_trajectories.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/analyze_seed_trajectories.py) | `03e2c7bdc7fea484a1abf0c91ad968594df5983b21de0eb797f30c2d5e8ad8e4` | EXACT_CODE_LINEAGE — equal bytes |
| [c.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/c.py) | `43f3619347f34612aa41daf7bf7ebb0382b780248b598c490f03df7ded30a3ae` | EXACT_CODE_LINEAGE — equal bytes |
| [constants_selector.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/constants_selector.py) | `80d8825691079bfb10151a94b243dd9757fb4fe5759aa5fde85dba09e9ba7edf` | EXACT_CODE_LINEAGE — equal bytes |
| [cp_windows.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/cp_windows.py) | `ba51846bef9c7903349e9e5d40647c7ae1751937184f8f8b9926e9c37c46bd6b` | EXACT_CODE_LINEAGE — equal bytes |
| [definitions.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/definitions.py) | `239ef173f6331240af70166cdfb6e836c0eed9a4ea8f333ab25fcd0b354cf4d8` | EXACT_CODE_LINEAGE — equal bytes |
| [diagnostics.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/diagnostics.py) | `f574b80189b1d39e3661005f84a305b718878731c676afd8469e796279428b16` | EXACT_CODE_LINEAGE — equal bytes |
| [identity_rules.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/identity_rules.py) | `889eb7e759aabbc509a852094cdf778e164e02c9a82a0a55a47b269f60bea751` | EXACT_CODE_LINEAGE — equal bytes |
| [latent_foreclosure.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/latent_foreclosure.py) | `60de93e8ad198ed3b94f3e43a5b4414b58d493269deaeb897efa6a5ec2ec3318` | EXACT_CODE_LINEAGE — equal bytes |
| [model_core.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/model_core.py) | `c9fcc15940749b27fbe9a8afea6aad46fed6e56b469b30ad976a7ba225ac66ab` | EXACT_CODE_LINEAGE — shared implementation bodies; file differs |
| [phase_triad_sync.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/phase_triad_sync.py) | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` | EXACT_CODE_LINEAGE — equal bytes |
| [physics_sampler.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/physics_sampler.py) | `7cf80e1fd8fe67f33e4276772eaf8f19a4fedbd7ed91357aeab3a509a27749c2` | EXACT_CODE_LINEAGE — equal bytes |
| [physics_sampler2.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/physics_sampler2.py) | `d7a0c02d242e4333d07f25c49f83a005eb697deb3a0c0b2b9239105aad413b7f` | EXACT_CODE_LINEAGE — equal bytes |
| [rsb_model.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/rsb_model.py) | `70f8966a753393705510de0823c780e03f19782086d7361a095b09ed60746e9f` | EXACT_CODE_LINEAGE — equal bytes |
| [seed_emission.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/seed_emission.py) | `c4b97f833c1192d03d00e992717ef4c4c49dd5f590326089c6ee57019877ef66` | EXACT_CODE_LINEAGE — equal bytes |
| [seed_entities.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/seed_entities.py) | `55fd2d1d45ed3aab1d98016fa5395ec53a32b0d89448c98707c2f64d0c82cc1d` | EXACT_CODE_LINEAGE — equal bytes |
| [seed_trajectory_analysis.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/seed_trajectory_analysis.py) | `b269f46dbcccf3a89434355f7e0c63bd1a5a0b3b3b644ea7785c780414e1a6e7` | EXACT_CODE_LINEAGE — equal bytes |
| [su3_basis.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/su3_basis.py) | `2ccac73c3aac18f79b76eaa432f27bfa23accc1acc99502a3a6a05b71f4617b4` | EXACT_CODE_LINEAGE — equal bytes |
| [tangent_corridor_analysis.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/tangent_corridor_analysis.py) | `8596940375d1f299a6e8fef40b49e9a603405298867594f276e95fdcd464c81b` | EXACT_CODE_LINEAGE — equal bytes |
| [trajectory_logging.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/trajectory_logging.py) | `0b1265bf1fbb3c6479972c2422a0b28fa1479f20510ad5eb2498c8dba17cb779` | EXACT_CODE_LINEAGE — shared implementation bodies; file differs |
| [trajectory_v2.py](C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/trajectory_v2.py) | `f09f2a66578e9b00d8f3bfa122a38ce2059b234ea67fff25a6da002908a9a8d8` | SIMILAR_CONCEPT_ONLY — production-only persistence generation |

For OLD cylinder/history-torus/channel-torus/tetrahedron/Frenet/three-body and standalone plot modules versus a corresponding TOR kernel implementation, **NO_RELATION_ESTABLISHED**: no such counterpart was found in this21-module production scope. Shared Ω input data or a word such as “trajectory” is not enough. For TOR ring second-difference versus current covering/dynamics, **MATHEMATICAL_LINEAGE** is limited to the explicitly identical operator formula; the full RSB and F_M states/updates are not identified.

## Appendix C. Full historical file inventory

All401 paths were read as bytes for the preservation fingerprint. Source/support entries have the detailed census above. Other artifacts have inventory coverage only: no claim of individual plot/PDF visual inspection or NPZ content validation. Paths below are relative to OLD. Hashes are full SHA-256.

Directory groups: `(root files)`=106, `__pycache__`=33, `bottom_1`=5, `bottom_2`=5, `bottom_3`=5, `bottom_4`=5, `bottom_5`=5, `bottom_6`=5, `bottom_7`=5, `bottom_8`=5, `edge_plots`=7, `golden`=14, `old_golden`=14, `out_bottomlid_stable`=7, `outputs`=37, `outputs_dt_optional_suite`=68, `outputs_lf_warmup_sweep`=21, `outputs_patch39_unified`=38, `outputs_seed_emission`=2, `outputs_seed_emission_sweep`=4, `vrec_ts_critical`=5, `vrec_ts_subcritical`=5.

| Relative path | Bytes | SHA-256 | Coverage |
|---|---:|---|---|
| `__init__.py` | 16 | `6c010626822f69510ca8a0d1fdee16d4e6cd5dcbaa570623eecee80af3a6e685` | source/support read |
| `__pycache__/__init__.cpython-310.pyc` | 169 | `563d05547300636d0eac8649db04684f32e8685fe027189b5763287e2391e08a` | artifact inventory |
| `__pycache__/__init__.cpython-311.pyc` | 153 | `64a50271b1304b4004526d7487bfdc609b2717f9c55aac71fbe1c3e9ad1e89f1` | artifact inventory |
| `__pycache__/constants_selector.cpython-310.pyc` | 3462 | `ee6c50054c21171544559ef4108536a91485d859d8f89c62b3ef169105e40ed4` | artifact inventory |
| `__pycache__/constants_selector.cpython-311.pyc` | 5207 | `66f69f5fee59aaa7c5f0451da3cc461cf9e2f8e1e5695e6162179c8619255ba2` | artifact inventory |
| `__pycache__/cp_windows.cpython-310.pyc` | 1762 | `954c091da1322bc8d6d05c0444498de1901aaf4381c161cc4b976fe2c3a85a14` | artifact inventory |
| `__pycache__/definitions.cpython-310.pyc` | 20544 | `17f903f9a1ab2e3472a2877d68378abf5fc72f215def7b31582d1f9818bdad98` | artifact inventory |
| `__pycache__/definitions.cpython-311.pyc` | 36523 | `fd73a27c0d79f317eb28bf290eb711450ef4b3c862e2e73064379085e3235e9a` | artifact inventory |
| `__pycache__/diagnostics.cpython-310.pyc` | 14989 | `0460f20ec0baa735fba9051fc6ac39d8a7a521fcf3f6b5bb8fc5603099d3ecde` | artifact inventory |
| `__pycache__/geometry_3d.cpython-311.pyc` | 3101 | `92f551b2bc0176efd1f471b0820716ddc08046f01ec09ddba470892cb41011d4` | artifact inventory |
| `__pycache__/identity_rules.cpython-310.pyc` | 1937 | `db86c3d96a590ede777284b4c9ef5dd3feeda8c0b631822ff9be040f7a5730a3` | artifact inventory |
| `__pycache__/identity_rules.cpython-311.pyc` | 2499 | `0aa6415a27741b2afa051847c6273523ee864892a005a709ec53707702c0fac5` | artifact inventory |
| `__pycache__/latent_foreclosure.cpython-310.pyc` | 2359 | `f8ea017b5966210d94cb3e47cced9701f7c3c020a4d452b735cc1da7dc7bf4e6` | artifact inventory |
| `__pycache__/latent_foreclosure.cpython-311.pyc` | 4592 | `af911921fe728ab9dc32c047ca28e6c53975310bfb2c549a76a6f84ad46c6c3d` | artifact inventory |
| `__pycache__/model_core.cpython-310.pyc` | 9193 | `bb56d7805f4197b3e69402b38c5584e9eaa19ee1072dcb9dc1170eaab5861e85` | artifact inventory |
| `__pycache__/model_core.cpython-311.pyc` | 17128 | `3b3c807ea7d2a4cb0ef3717a52651b21e75c65270b011a1ad0cb33fd845b28f4` | artifact inventory |
| `__pycache__/pathing.cpython-310.pyc` | 6895 | `ebf318a179c277ab7fa4dfee636fbcd40239acae90564fedd0da638e8c5ea54b` | artifact inventory |
| `__pycache__/phase_triad_sync.cpython-310.pyc` | 1386 | `22fdda5596929df8d67567c928d7c3d7577d3c4fa1571cd3235f8812f0f17418` | artifact inventory |
| `__pycache__/phase_triad_sync.cpython-311.pyc` | 2271 | `89ddde17d20c29f5cc320cf25f43414c2595aaabede9c46a4c964562a775d228` | artifact inventory |
| `__pycache__/physics_sampler.cpython-310.pyc` | 3908 | `df5938e9990dd664c7695e4fb4dbb59ce269063576355f4e051604ab15bb234a` | artifact inventory |
| `__pycache__/physics_sampler.cpython-311.pyc` | 6504 | `a5cb713569ec7f2f4d87ce7073df193e115917c1b5638963b1ffa5dd62043a8f` | artifact inventory |
| `__pycache__/physics_sampler2.cpython-310.pyc` | 5295 | `0699382f58e142c7f373c10b9fac5dce8ce45cc626eb473edf180caba7d38b30` | artifact inventory |
| `__pycache__/provenance.cpython-311.pyc` | 2911 | `6af5349e8ed5ffe5255c5c1984e430478f85e6b52784566d29091b1fb91173e7` | artifact inventory |
| `__pycache__/rsb_model.cpython-310.pyc` | 9978 | `72156456bea13ff9425509a3c9ca200e4d76a6dce2e98e63f577fca0b7974c4b` | artifact inventory |
| `__pycache__/rsb_model.cpython-311.pyc` | 17174 | `cccceb33c140b144243772f1c60555d1a4b7b1dfaabab8c644cb37dd9665af3f` | artifact inventory |
| `__pycache__/rsb_spectral_viz.cpython-311.pyc` | 13713 | `e0c300c35b713341a6b1122dbb7ed80948c5ee4bd36896a67777406fecbc709c` | artifact inventory |
| `__pycache__/seed_emission.cpython-310.pyc` | 4129 | `577338d10b289fa1cfdd98f7c59b4935b7f819d5a19ac4df86a433e05b6a206d` | artifact inventory |
| `__pycache__/seed_entities.cpython-310.pyc` | 3935 | `2c91217498aa798c122ed8a248ee85be7f6b020df1e766e2a19ef382f6e03f82` | artifact inventory |
| `__pycache__/spectral_viz.cpython-311.pyc` | 9935 | `b1c134991e0691a3b7b2cca02e8ad8b09a35a2f1ef3ab476a0e1dba14ad00aa7` | artifact inventory |
| `__pycache__/su3_basis.cpython-310.pyc` | 1142 | `f6d3d261d19e0819aa52f5cc5990b790e25bcb09389b7d7395ad9e764bb42d68` | artifact inventory |
| `__pycache__/su3_basis.cpython-311.pyc` | 1718 | `999288ea2576dc6fd104cc375a631b5408395eb735eb2c59aab74591e5c6c8e4` | artifact inventory |
| `__pycache__/tangent_corridor_analysis.cpython-310.pyc` | 6268 | `9e1ca2a909c2c25e2f99d0a506639a7c3543ba11a478b9662b817f9cccbd80ec` | artifact inventory |
| `__pycache__/toy_3d_triocta.cpython-311.pyc` | 48102 | `ff5b58f21eaabb89a1210123689c21443558ee4e5409ad5569cfa06bc2244f01` | artifact inventory |
| `__pycache__/trajectory_logging.cpython-310.pyc` | 3382 | `80fa020f0e97a13c8a3d2f7917e483185c82ab0796ebc2c7b93bd3eaf4ea0190` | artifact inventory |
| `analysis_core.py` | 559 | `85ac1e58cceed0b8115888f1fae5499b69048fc212d9a21fa2362a92c472fad8` | source/support read |
| `analysis_runner.py` | 619 | `2c2df99a0e3f22ac7a3a39f694880a05da19e71370390429e82b61f6ade392ea` | source/support read |
| `analysis_tools.py` | 7866 | `3be6de46c7060b6e797bc6801de002c5b59374957a3ef1a9fd37d51b11b20106` | source/support read |
| `analyze_big_scan.py` | 5917 | `8d0d98aa6e9f98c8f647086aa51ca1272b4c0e3e58b347ab7197ae8454023032` | source/support read |
| `analyze_emission_entropy.py` | 2300 | `f114179dee4439223cc139dab4febce32b128e54ab0bdf48572f30872d3b2c0f` | source/support read |
| `analyze_emission_R.py` | 2334 | `79bff2c14fd0eb845d43b77f1f6866df50d444dd70c315484343756361952788` | source/support read |
| `analyze_event_window_entropy.py` | 1824 | `8c7abc52b366568197f6e9eb06937f6cd4eaececb0b90c2905647523755776d4` | source/support read |
| `analyze_rgd_rows.py` | 9271 | `d4d481c3cc6e3db622d4bf793c3605bca02fb657761cceef1967bf1c8c7e28fb` | source/support read |
| `analyze_scan.py` | 2612 | `14fe31a637becfd916ce3757da5a71f6887ee85ace4f81bad3d147840bd6fff3` | source/support read |
| `analyze_seed_trajectories.py` | 1562 | `03e2c7bdc7fea484a1abf0c91ad968594df5983b21de0eb797f30c2d5e8ad8e4` | source/support read |
| `analyze_threebody_probe.py` | 8052 | `0cd03571fb5146a27b7efde528843aadde9851c470197cfec7ca6f1b0c7921b6` | source/support read |
| `bottom_1/bottomlid_summary_1.csv` | 663 | `c49def831e22239e914c3ecf3d3095d3335c63958f9c32aaf19b00450b2af0c6` | artifact inventory |
| `bottom_1/seed24_g0.660000_eps0.003000_lam0.0000_alignment.png` | 52390 | `6e694f0d9e7067adc362730e62b20ebf5997ecf5f531eddd32a69cca9fb76f81` | artifact inventory |
| `bottom_1/seed24_g0.660000_eps0.003000_lam0.0000_alignment_arrays.npz` | 145292 | `efb2ebdced72f0da35bc86d344e8d90dcdb60511d6675bc6447d6809e619dc72` | artifact inventory |
| `bottom_1/seed24_g0.660000_eps0.003000_lam0.0000_alignment_context.png` | 42749 | `034210214383c64287f97a8edfc737170581a887a6f7ae7561046cd010ec6d18` | artifact inventory |
| `bottom_1/seed24_g0.660000_eps0.003000_lam0.0000_alignment_states.png` | 38578 | `46b0641f5ff24a0888a57ab4d9f1b94bc008fdba29fb01e8f2225d25ffb0bcae` | artifact inventory |
| `bottom_2/bottomlid_summary_2.csv` | 664 | `cd2d5dc5aca97446e8a6cda4695afb710ebdcad82febf6452e98ded3440d220c` | artifact inventory |
| `bottom_2/seed24_g0.660000_eps0.003000_lam0.0200_alignment.png` | 51240 | `f6f004f81cb7ce7297f6d98e351e5cca5e0365ea488ad8bdfed41d0cbadf0b91` | artifact inventory |
| `bottom_2/seed24_g0.660000_eps0.003000_lam0.0200_alignment_arrays.npz` | 103132 | `e521db729c198be5739359c72d1416aeda73144a46449e506c287e59e0e6cc3d` | artifact inventory |
| `bottom_2/seed24_g0.660000_eps0.003000_lam0.0200_alignment_context.png` | 42784 | `85d350bb8159db4a8f6e042bc89d3fd63cac73a8e8725cf5b44d809eaa131507` | artifact inventory |
| `bottom_2/seed24_g0.660000_eps0.003000_lam0.0200_alignment_states.png` | 38622 | `55b8e374c6bdf856aebdec69e4bdd56b4eba861e00c8dd7863544ec0615762d5` | artifact inventory |
| `bottom_3/bottomlid_summary_3.csv` | 664 | `fc3b624e52b59b2b6e822fe0006e7e22a4085f879cea69a048b1a2ad16d2e1ed` | artifact inventory |
| `bottom_3/seed24_g0.662500_eps0.003000_lam0.0000_alignment.png` | 58110 | `e2760ace1b2a777b39c32543e032b0e1ad1609c1560ca670cb2f6c13072aa4f5` | artifact inventory |
| `bottom_3/seed24_g0.662500_eps0.003000_lam0.0000_alignment_arrays.npz` | 169454 | `7ca6227602359fbb8b632e7dc3fefa83330a41ce2fcd394b2a1cdb38c3da8d2a` | artifact inventory |
| `bottom_3/seed24_g0.662500_eps0.003000_lam0.0000_alignment_context.png` | 47648 | `0b7ea1e8bd8a692b6548a572355e43a81e0c6d7bf862af185dc6dbf71902345a` | artifact inventory |
| `bottom_3/seed24_g0.662500_eps0.003000_lam0.0000_alignment_states.png` | 39165 | `9e941e10664604849f948474d6c68251d70569b458da9724b9db237428b6ccbf` | artifact inventory |
| `bottom_4/bottomlid_summary_4.csv` | 667 | `8605ea2ba573a33b5d08c3af80eb2f0091fcd848fb3bd6d8606b61d1d0c00c20` | artifact inventory |
| `bottom_4/seed24_g0.662500_eps0.003000_lam0.0200_alignment.png` | 51980 | `9be4ce804359ae296185604881df33be60fa8a0ba37a13a251c7eca41370f0a4` | artifact inventory |
| `bottom_4/seed24_g0.662500_eps0.003000_lam0.0200_alignment_arrays.npz` | 106201 | `9a59a8fba444634a5b158759e177a7b8fb6dea8b111d3687986ea9c344c07fe7` | artifact inventory |
| `bottom_4/seed24_g0.662500_eps0.003000_lam0.0200_alignment_context.png` | 47571 | `bc04c5214badb68b32c494ba096098c6caf05d8b8c84910259b960a5460af1a2` | artifact inventory |
| `bottom_4/seed24_g0.662500_eps0.003000_lam0.0200_alignment_states.png` | 39421 | `23fc0efc07e76eab01410d8a204f828e42ef8e7e86b4eb45391528a3a9156e44` | artifact inventory |
| `bottom_5/bottomlid_summary_5.csv` | 721 | `c59a576c97bd748d081c72d8f34ac58850b9f62ceaf1654d35951482f88b6b02` | artifact inventory |
| `bottom_5/seed24_g0.665000_eps0.003000_lam0.0000_alignment.png` | 177750 | `46df8c846c096aad8baa53d95ed91c4f9557f6e8c02917fc715d35f26c20f65a` | artifact inventory |
| `bottom_5/seed24_g0.665000_eps0.003000_lam0.0000_alignment_arrays.npz` | 53608 | `902392e13ebacac8dc80f769f02921aa109fbafdc81885a9433c2582460c7205` | artifact inventory |
| `bottom_5/seed24_g0.665000_eps0.003000_lam0.0000_alignment_context.png` | 36739 | `415af4d371e0b8203db307acc5df650f7d1ad412d803f82d54b87448d561e3b2` | artifact inventory |
| `bottom_5/seed24_g0.665000_eps0.003000_lam0.0000_alignment_states.png` | 41458 | `8571625845dac105f9b642a4c3ed6a03d023a7125b9aa45a4b097fd88e6cc81f` | artifact inventory |
| `bottom_6/bottomlid_summary_6.csv` | 723 | `7359c763c129d18f641a14e37a43dd9ddb6d8ac494d5805ad85bfcffae6fc0e5` | artifact inventory |
| `bottom_6/seed24_g0.665000_eps0.003000_lam0.0200_alignment.png` | 116245 | `f0bc04a775b965ee971e4da469daf04222fec1e640a10f75dd1359d16c053f6e` | artifact inventory |
| `bottom_6/seed24_g0.665000_eps0.003000_lam0.0200_alignment_arrays.npz` | 40037 | `da38b792deaa4cd5227a20a6fa63121f0b66dccd4d99bd0ccc7cf55c2342635a` | artifact inventory |
| `bottom_6/seed24_g0.665000_eps0.003000_lam0.0200_alignment_context.png` | 35840 | `dbbda5cd0509ad4472a0a118743af39a252321135e587a0f205f52dd907c1ce3` | artifact inventory |
| `bottom_6/seed24_g0.665000_eps0.003000_lam0.0200_alignment_states.png` | 42299 | `a16e2f2c40ce3a959ebfa22f1d01833b474f311ae6a4c330484d019fdfebe221` | artifact inventory |
| `bottom_7/bottomlid_summary_7.csv` | 724 | `6e79f702e21febca5242b542f8f210a8efb8476fa73a309e3d8b2ba187a64083` | artifact inventory |
| `bottom_7/seed24_g0.667500_eps0.003000_lam0.0000_alignment.png` | 218235 | `96b30321acbe4ac2c7421607d525efb1d227884a9e84354481f00bc236413dd5` | artifact inventory |
| `bottom_7/seed24_g0.667500_eps0.003000_lam0.0000_alignment_arrays.npz` | 44103 | `9058fc9ad7bdd1a0c5d98515a7623a51f59037329bd01b46e2d9595c2e6d011a` | artifact inventory |
| `bottom_7/seed24_g0.667500_eps0.003000_lam0.0000_alignment_context.png` | 37860 | `3c4b693ba5dd774517cd3c76c56ba421c3990ed9a757e54c84a13f44d40cb72e` | artifact inventory |
| `bottom_7/seed24_g0.667500_eps0.003000_lam0.0000_alignment_states.png` | 38505 | `606d504d987a988657e8ac89c25c170259e9ec6902d8bb602053a14f33bc4658` | artifact inventory |
| `bottom_8/bottomlid_summary_8.csv` | 719 | `dc009623a1fa3f6b2da645a7dc053370a2dbbea007703b4cf3d07d5b4d9a2f49` | artifact inventory |
| `bottom_8/seed24_g0.667500_eps0.003000_lam0.0200_alignment.png` | 180945 | `635d5c9b0562746ae76e6de1823551471334a2c62d60df3476b308b6e7ccc2bb` | artifact inventory |
| `bottom_8/seed24_g0.667500_eps0.003000_lam0.0200_alignment_arrays.npz` | 36905 | `f11e5f4d87f7334daa8737e8ee5ad8af1c36baeb3f787308d79c6d2abca03870` | artifact inventory |
| `bottom_8/seed24_g0.667500_eps0.003000_lam0.0200_alignment_context.png` | 37907 | `aea8b7be74843848c57a42ff14916bd3fa122742347497eda6d229c5c83d41e9` | artifact inventory |
| `bottom_8/seed24_g0.667500_eps0.003000_lam0.0200_alignment_states.png` | 39739 | `53f80a55488bd98306fb1375da28bbfb511f1c5f9ddd2d65defc0533d2cd0363` | artifact inventory |
| `c.py` | 372 | `43f3619347f34612aa41daf7bf7ebb0382b780248b598c490f03df7ded30a3ae` | source/support read |
| `chirality_lab.py` | 28796 | `7048139eb2219b5a78a9f78d28cfe4f2f1375841bb99be6a99c251163463383b` | source/support read |
| `chirality_param_scan.py` | 6124 | `3fce72b66297b9a61195631f87e4a65e6f43abc037942eb1254f38837c5f475c` | source/support read |
| `classify_nan_logs_v3.py` | 1191 | `1b2120cf37bea97ec8b339268654610c9fced5918e9771eeb82bd9c57449b927` | source/support read |
| `collect_optional_suite.py` | 4501 | `afb15ae0d7aa175ac602eb13c4e0c186d4e61b90b2d46772aecdc8b454013634` | source/support read |
| `constants_selector.py` | 3308 | `80d8825691079bfb10151a94b243dd9757fb4fe5759aa5fde85dba09e9ba7edf` | source/support read |
| `cp_windows.py` | 1499 | `ba51846bef9c7903349e9e5d40647c7ae1751937184f8f8b9926e9c37c46bd6b` | source/support read |
| `definitions.py` | 29485 | `239ef173f6331240af70166cdfb6e836c0eed9a4ea8f333ab25fcd0b354cf4d8` | source/support read |
| `diagnose_bottom_lid.py` | 10148 | `10bd4d12841933d47fad15a74d64462b68cf7033054fed293260581fdd2bf1d7` | source/support read |
| `diagnostics.py` | 22393 | `f574b80189b1d39e3661005f84a305b718878731c676afd8469e796279428b16` | source/support read |
| `dual_tetra_mapper.py` | 1165 | `14845223bbfa0c0f17df2781ee4a0ebba9befeee5f374bb01a4647242dbedf9f` | source/support read |
| `edge_map.csv` | 38565 | `28053621befce81d608a16c662c3887e2b0edf0261f81876e9ccaddfc7626779` | artifact inventory |
| `edge_map.py` | 11246 | `7dc2e1746beac06dc092c296cbbdbbf2e09b1a489799de9a297e4c51783aa3f3` | source/support read |
| `edge_plots/01_gcrit_hist.png` | 42020 | `5ff67eec22b804164f8e0ae6bd3cd371807a3033adb446ac3970025528900ee2` | artifact inventory |
| `edge_plots/02_gcrit_vs_seed.png` | 47754 | `ca6819e31b6d4086a93154a08cceb032b083a8f4d065247388299f975fbc4605` | artifact inventory |
| `edge_plots/03_finite_prefix_hist.png` | 47646 | `384a6f19ae36b784eadea55697c0239ba8599e984351fb936125249f9fe78097` | artifact inventory |
| `edge_plots/04_prefix_vs_vrec_p95.png` | 78899 | `7b6ab533fd178fe16228d30d451bdcce36a2e162b7d3a9090827ad09ecbd823c` | artifact inventory |
| `edge_plots/05_first_bad_channel.png` | 39755 | `e9736635ebda420dd50e63baac8d19b3834cfc74eb4aeb98581a4fce8f067baf` | artifact inventory |
| `edge_plots/06_log_magnitudes.png` | 53813 | `ae51514da7150aefc4651cf8071e4f85ed856a906a35bf7a272b4542a27f3190` | artifact inventory |
| `edge_plots/summary.txt` | 286 | `14e0df448fea034af750a0828eeea73fe5a0cd450997f3608af8cc0990c624a9` | artifact inventory |
| `eigen_analysis.py` | 2962 | `918cf67e869591a52a60371e636cace10c990ad1a37694f3a6326661072a41c2` | source/support read |
| `eps_extremes_seed733200047.csv` | 503 | `a19aa189fd44272588bc0afab12a446ca507e85a8398192145f2267763067152` | artifact inventory |
| `eps_ladder_seed733200047.csv` | 975 | `58b6a9175791d56079410dcb83ed994fafcfda34c11b63a5049a15fe97b01d49` | artifact inventory |
| `eps_scaling_g0667.csv` | 967 | `4b5709fb19259fff0cea48fd6124717eedc64ed3f32acca8fbe081c7d9bf0905` | artifact inventory |
| `explore_sweep.py` | 17073 | `e654130c53f4c6bb5e1c75e773c9877851a09551f670f11fe312dd3310ef2d82` | source/support read |
| `fit_eps_exponent.py` | 1044 | `602c03a546939441f03ba78a942a8b63b55eb3d8640499f23cde91b5f9a1aa02` | source/support read |
| `generate_golden_refs.py` | 3273 | `6d9796d360f5e10db03f0a1e9012ec13b53d3ec88e22e7ae298b77eac75e5992` | source/support read |
| `geometry_3d.py` | 2125 | `b6803b3a02f5240a5cb00a3dbc9cf403c2e762de713146aa3848996738772400` | source/support read |
| `geometry_embeddings.py` | 991 | `5e5a12d0b352fe353aea84d47b598c4288d9d679ee8d83003c25e210a0ec4c4e` | source/support read |
| `golden/00_stable_core_seed2158500047.npz` | 121251 | `63b6c967a62c0714209097ba635ed913221f24ab2c5727b1fc4b4cbbbd4d04a6` | artifact inventory |
| `golden/01_stable_core_seed2158500045.npz` | 121371 | `2aec40ebc34d6111d619b39a50388baadc04eb1132ac7f7f020b10ed0e5b73ef` | artifact inventory |
| `golden/02_stable_core_seed2158500049.npz` | 121596 | `dea9c037815d503d9d4bfe55beab01e4a3b6dae5bb8467f3885df2cf497cb3cb` | artifact inventory |
| `golden/03_stable_core_seed2158500048.npz` | 121905 | `ddd86f8f34b8a94990182787ddc96534f0409cb161a12c7bfc2272abc055aded` | artifact inventory |
| `golden/04_edge_band_seed733200047.npz` | 106622 | `3483e0faa379c0cccfebac3df5a41ff38b2aafef9c94280f2ff6b0d513e719db` | artifact inventory |
| `golden/05_edge_band_seed733200042.npz` | 106955 | `404935ae6420a59bd301c83ef05d87cde13b8742c8d796f89babb1f4b71e213f` | artifact inventory |
| `golden/06_edge_band_seed733200048.npz` | 107340 | `ef86469e70cbde999ba6d8eeb4c1b3950ffecb638ca8532b6a75487b70dc8a7d` | artifact inventory |
| `golden/07_edge_band_seed733200046.npz` | 107425 | `a8980accbcb27ef7f99085dabac865ec56402f5130e18b13d8e5919d90b0da7f` | artifact inventory |
| `golden/08_near_knee_seed1414300043.npz` | 105861 | `c8b59bc75adf16c7aba1bbecbd446ea9385c79a050060907a805ccce6c0d03fc` | artifact inventory |
| `golden/09_near_knee_seed1414300049.npz` | 108836 | `da00306a8ca9e8c59a5219e593ae1d37c7f78649665f6c9e81a9c5d20e2e88aa` | artifact inventory |
| `golden/10_expected_fail_seed2415100045.npz` | 11712 | `1eb7c88a53dff780739310f64822798abe8d03f6d1bf8754a08e75c442ec0c2a` | artifact inventory |
| `golden/11_expected_fail_seed2415100043.npz` | 11751 | `615ccc65cab13c4732a53a76b79d8e4fe92d04df5bfdef5c9b7e08fa38737cd2` | artifact inventory |
| `golden/golden_points.json` | 2459 | `b4bd077db7832b73b8aadc3323360fb56fef9b4e510ef924704e1a3ed5393427` | artifact inventory |
| `golden/golden_refs.json` | 5521 | `88a9336c710e871cb2652c5b828e061ed37c0bc29bc222701c97e1616095ad58` | artifact inventory |
| `heatmap_ray_alignment.py` | 3632 | `aa92c53361642c0a6c3aa03225a9d6b2c547a2cee60e2f47c0a7b20e023189e9` | source/support read |
| `identity_rules.py` | 1617 | `889eb7e759aabbc509a852094cdf778e164e02c9a82a0a55a47b269f60bea751` | source/support read |
| `latent_foreclosure.py` | 3168 | `60de93e8ad198ed3b94f3e43a5b4414b58d493269deaeb897efa6a5ec2ec3318` | source/support read |
| `make_figures.py` | 19245 | `f2cc93631898dbb70b6b851373ff681328d4388c83a6a14de6036a163f5482f7` | source/support read |
| `make_paper_figures.py` | 1239 | `e0d8c9478eef24dd7df204d48dc266d615540eea4d4b642934c73720f2c0a83b` | source/support read |
| `make_vrec_timeseries_figures.py` | 2693 | `36f4ed2e1f179f967e2c3ef0319f08d2eeb9850372527c562894f3b5a75c92aa` | source/support read |
| `model_core.py` | 12214 | `ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6` | source/support read |
| `n_eps_ladder_seed733200047.csv` | 946 | `194e50eb188a05a523499cbbc2955984f3a4e3fe4e9f678640c38dfa33f8fa37` | artifact inventory |
| `nan_forensics.py` | 2439 | `932fef9fde02f241ca36d329f7252eeb00249bec14c765c8f48e7b221f4c5a45` | source/support read |
| `new_run_tests.py` | 13344 | `e6e1141e5f106bc9e74f74570c690355c694abfe78b80bc3556c64784573cf73` | source/support read |
| `old_golden/00_stable_core_seed2158500047.npz` | 121698 | `d00d0ff431b727c905d9b8908d2fadf8d0118e32e0db1efc350a1e9a240b2613` | artifact inventory |
| `old_golden/01_stable_core_seed2158500045.npz` | 121923 | `2c20efed2c8ee04cbf54f60d41a197c58c390c4579a4f4e130469591ad6c076e` | artifact inventory |
| `old_golden/02_stable_core_seed2158500049.npz` | 122106 | `61d1f9f2ae9ca334ed889b64f05f7b64ab0a160e1379b32dc06f87a7114af540` | artifact inventory |
| `old_golden/03_stable_core_seed2158500048.npz` | 121987 | `6c1628adb378883db7adfa505cc857b6307b6dfeaf27bd49b6ea37faaba70261` | artifact inventory |
| `old_golden/04_edge_band_seed733200047.npz` | 107351 | `91677e6358542ac69ecacd057728f27d8fd61c1b689af48f9e9620ced9cc4562` | artifact inventory |
| `old_golden/05_edge_band_seed733200042.npz` | 107435 | `7fb4df4c8c98436a8f14a82cb3c73409a79e70fc05b203d4cc4d906320cc94f6` | artifact inventory |
| `old_golden/06_edge_band_seed733200048.npz` | 108487 | `15235eac577a5885c22cf86428f8bd619d6b4333eef9de66a44db3a95b95ea8c` | artifact inventory |
| `old_golden/07_edge_band_seed733200046.npz` | 108012 | `7187350b02adac59b178a560ab3d6dbed6e5babb6760ca831b8a1012b414a627` | artifact inventory |
| `old_golden/08_near_knee_seed1414300043.npz` | 108783 | `40cf1c9f4abac61d3d61886718416e18c0e73221df3c879a9a7bea01928feaae` | artifact inventory |
| `old_golden/09_near_knee_seed1414300049.npz` | 107810 | `b5472bcf1d5b7a0596387627a450cf0609baee175f0e0c09d9be0049f9e7cbde` | artifact inventory |
| `old_golden/10_expected_fail_seed2415100045.npz` | 11724 | `1fad7ed842c159c5f114150ca294a98698820dc44eb0709e4fa28dcc0e403902` | artifact inventory |
| `old_golden/11_expected_fail_seed2415100043.npz` | 11754 | `3cf95e3cf26d77312d67b2b87f4515ead68d2210a261753dbdb3d662604f44d1` | artifact inventory |
| `old_golden/golden_points.json` | 2459 | `b4bd077db7832b73b8aadc3323360fb56fef9b4e510ef924704e1a3ed5393427` | artifact inventory |
| `old_golden/golden_refs.json` | 5521 | `88a9336c710e871cb2652c5b828e061ed37c0bc29bc222701c97e1616095ad58` | artifact inventory |
| `out_bottomlid_stable/bottomlid_summary.csv` | 723 | `ad92f89a6795bdac3a1405fed8688cd620190397af5b99a0cc37c135f10d2111` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.660000_eps0.003000_lam0.0000_bottomlid.png` | 116318 | `b785e532d99e677cfffa4e053b90781b7dc4bb7121041f1cae6f2d2e3123e006` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.660000_eps0.003000_lam0.0200_bottomlid.png` | 59386 | `aa668043e8d78655a47982e7e504866ea81a3921c6b86eea4ef8d19343fe236d` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.665000_eps0.003000_lam0.0000_bottomlid.png` | 168172 | `3a793ae4e325de772a923ad6d9ddc4ffa0682f82d3128be0577767c57cac949e` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.665000_eps0.003000_lam0.0200_bottomlid.png` | 112391 | `7f58138a2c31ee2986d810fdb9c2088842e250e3c04f7a75c31627ca2aaa08a6` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.667000_eps0.003000_lam0.0000_bottomlid.png` | 210416 | `aed5dfb00e0efe68a5c761ba6c89994ee4c9ad5e051177996c95a2d68bfba825` | artifact inventory |
| `out_bottomlid_stable/seed24_g0.667000_eps0.003000_lam0.0200_bottomlid.png` | 156886 | `0922d74181d8eeef4ba52a48cd20fcd203b51d028738ab4f3f59d7bfb78ad646` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_frac_finite_tJ_settle_heatmap.png` | 138273 | `38ad31b692424661728a5d1be8fc00fe11363c163417dc48f17f6a7eacfa4038` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_frac_finite_tZ_settle_heatmap.png` | 137683 | `a2180f7426ec304664ae0a36bf4e22fce5d403cec028beea9ffb8fd4526527af` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_frac_stable_heatmap.png` | 134409 | `e21023e48075b250678149e9cc19d589c07a522c066dce38348628cda641a014` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_meta.json` | 484 | `2ef0aa452cd1b832efb44482aa248039853dee86b8f7105e51b86b0e78788ab6` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_postagg.csv` | 198985 | `4d7ce45765a5309e8a4bf77afcc1c5eb0a9fda8a568e34f16716e18476eac750` | artifact inventory |
| `outputs/rgdconn_20260127_124028_f1c8591b5410_rows.csv` | 13991851 | `92b488ef0b0e9f7107cf063afd9b6155db5c381e487d15a06f70692d0557eacf` | artifact inventory |
| `outputs/scan_analysis/edge_of_chaos_candidates_top.csv` | 53 | `770dafb2e5f4bd07acc79d4316e06ac0371fd90b1c7577533190d7d74abca9ce` | artifact inventory |
| `outputs/scan_analysis/heatmap_frac_stable__eps__g.png` | 47613 | `19d062461f84081e4ad7dcb6a0014832454a88ca699e048285f01fbc2145d2c2` | artifact inventory |
| `outputs/scan_analysis/heatmap_frac_stable__eps__k3_scale.png` | 58773 | `f2819811e2cd98049a7eea8154958eda7015637ae8863df496d574be8c0699cf` | artifact inventory |
| `outputs/scan_analysis/tradeoff_max_g_vs_eps.csv` | 1409 | `a9f34c4a7f0b9c5ff03d192014a1d3a0828551c4299ca5966b2684e15da54377` | artifact inventory |
| `outputs/scan_analysis/tradeoff_max_g_vs_eps.png` | 72293 | `09950f264cde5777428c080a1321c05f750daa33951744ec086b30cb70cc3af4` | artifact inventory |
| `outputs/scan_analysis/tradeoff_max_k3_scale_vs_eps.csv` | 1381 | `87c2569ab274e472eece586af93e1c79a78a1a39af2afbb69c148a7ef4a554a7` | artifact inventory |
| `outputs/scan_analysis/tradeoff_max_k3_scale_vs_eps.png` | 53601 | `a83712883703ae0d8789976ad79896cc98b28962fa3483d813ff0f7519e9b10b` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/analysis/alignment_rate_over_timeB.png` | 34177 | `6378cd5502b2cd184686943dc9d20c54621b745320baf97b2d0064113fc79e59` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/analysis/dv_vs_sixrayB.png` | 30353 | `710faa40fbac0aca0c514bfbec51c489535888b7279a45776ff7dc8b64762162` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/analysis/sixray_dist_histB.png` | 38164 | `f455977904fa8ba33db48a99adf7c79858f8df5b81d404e3088974266f5bf404` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/analysis/summary_grav_off.json` | 6617 | `252331438965d067d5d585202b1b7d3b8be584e063b7962b07686eddeb6e96a2` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/config.json` | 335 | `cd56d47a117b72778af495cec635fae11142fa63ef0ea9fc8aea6852dbcbc81f` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/internal_history.npz` | 1392202 | `8775b799e9a2f5c27c3f150318cc8f46e7d3f94946d8e897987dc46ecafeacba` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/internal_history_meta.json` | 131 | `db286382e3fca582b8c5787f6718f20f6bfb590181dc456634533bf312d2b19b` | artifact inventory |
| `outputs/threebody_probe/20260130_155130_992ff4c4/seed_world.csv` | 38026749 | `d83f0398f7e3d9167314ef9f38ee05ffa9c3e3ac94555d42abea95997fa52d26` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/analysis/alignment_rate_over_time.png` | 34298 | `62ac0aef6dde44fc10136ed1646c45deb0e81e93d3cb962f564586d060582744` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/analysis/dv_vs_sixray.png` | 41805 | `40854d3abfad3b3af5decdf2017afae9219ee7c4a4f34e56082be2954a9e8419` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/analysis/sixray_dist_hist.png` | 38483 | `f156fe752625890505fd8a9f26746bee869d550bcfecc8a217365a9664e5084d` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/analysis/summary.json` | 9247 | `84b197cf5387b2d021e8098c383e9d5176b54d305793e303d2937daeffabbc0b` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/config.json` | 334 | `1e9968566f01bf304af3426a98c0fbe4cd1b9b78975433958f1158204990afff` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/internal_history.npz` | 1392202 | `8775b799e9a2f5c27c3f150318cc8f46e7d3f94946d8e897987dc46ecafeacba` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/internal_history_meta.json` | 131 | `22713a94ddc4173e9f7f75098aaf18115146bb030451117f7e91fc270bb19d63` | artifact inventory |
| `outputs/threebody_probe/20260130_155315_b755fe2a/seed_world.csv` | 42897078 | `3f36cd24158c7cc5e878547d4ed8bcf4b558762988a0b3064a2e6f2ac176b4fe` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011027.csv` | 18187 | `2c80d1d12a981f358600cbc496c208e2a645be2816faf42acc6a830758b1e914` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011029.csv` | 18481 | `6eed96c4a893a18bb688f34bebedf22680f1407adbaf07161fe2557acf361f58` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011036.csv` | 17768 | `f0432fb5350ae4c8930d9938daa8c1e2d24d791946d16d22c60b82d3402b8fa6` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011037.csv` | 17768 | `f0432fb5350ae4c8930d9938daa8c1e2d24d791946d16d22c60b82d3402b8fa6` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011038.csv` | 17730 | `a65c83121934be4c2bfff79806cbc7064a5ce6081312735bae38c214d1c3304c` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011040.csv` | 18329 | `0ccc607179849924f1887afa2b6029251e2182bca5aecde259144dd330f89ef5` | artifact inventory |
| `outputs/timeseries_rerun_20260807_011042.csv` | 18759 | `e53baf995c18dd6ddf82d39b5a5dca64ff555f9d5f04e889f4259f5ae46862f9` | artifact inventory |
| `outputs/timeseries_startup_20260807_010947.csv` | 18306 | `6445f016650215d7152f926f46545acfd421be29c9a58be8bd3c8af4cd224d26` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/dt_invariance_event_ray.csv` | 2463 | `084d2368e68304cad8887ff7dc2f785baa629169c05394f24e7ef2da9edc80ff` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/emit_rate_per_time.csv` | 1819 | `da9e21bbc5e4b8c91834703c283ca8db958c5181af22dbb34d7e3c85cee0a69a` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/dt_invariance_frac10_std_hist.png` | 34056 | `3dd743c1d81385a7433675dd41e26f9edc4f474d5bcc3a13b125c5a2535a6221` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_dt_invariance.pdf` | 17009 | `1773b9abff13feec6e9db247ad1df429e73901a4d4f5a02be2776d877835e204` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_emission_modes.pdf` | 14036 | `0c663c77c46401cb6e598c5abb9be980a76fc1d7fb6aa7a657a34c1215c0bb4f` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_emit_rate_time.pdf` | 15996 | `4bba30aa3b9692985ccc77dbea02403ce284cc1caaa69c3ed88a637d5b6f2469` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_jeff_emission_scatter.pdf` | 15401 | `87e22c84bb68d217b4b3355c19f98a4a48ae24c17dff6ca8879e6f79b3e228f1` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_ray_alignment_baseline.pdf` | 15245 | `7793a27a3edebb6e2f008d0399cce7df9fb7051f00594ef3d9d36d0b2e2c0dd4` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_ray_alignment_events.pdf` | 14907 | `ad69c5ffdb6dc794836605b98da97c6c8145e97fb282489ca8ef94e2119ec340` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_stability_heatmap.pdf` | 17093 | `732253ad79d137f94aaf9c143a5560d113d142c2c0cddb4af1224ddc4934a404` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/figures/fig_survival_curves.pdf` | 15118 | `d184afa92bd3f0aee4c26d0bf7f64b67219d5b764e601bddea19e58c4ab3b40d` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch0_OFF.png` | 34924 | `b5bbb0ae0b6bb7eb1086b6a294d47d73d43f9be346dc6b1327253c7e3a3f41c2` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch0_ON_cmin_0.8.png` | 36607 | `f8c425e8303d41d403580d8b07bbbac1b59a20790e61d0f2862a8dbb3aafa3a1` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch0_ON_cmin_1.png` | 41196 | `ea4b786c3d51d27b7c317151e633b7dbea824f230a24b32b6d81e28066e8ff77` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch1_OFF.png` | 39938 | `d6c984523ccfe00a9c25778779eeb208e37076ecf242b873e809a96669307ba7` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch1_ON_cmin_0.8.png` | 41650 | `ffb2479fea683ec16043a77cadcf6c0bac5f1e664f23ab128b253f23f064c993` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch1_ON_cmin_1.png` | 36340 | `d214d62562f550d559fad4a9adf6a92cfc33b961a485c0884f745b96c67198a4` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch2_OFF.png` | 41662 | `bd79561a7ed7dd9442a1709337715461580ecefd3ff17552f7d49960bd88c7e4` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch2_ON_cmin_0.8.png` | 43234 | `3775b1382f7c09fa30f39a3ddc3b2aa2ab28538a65f2c0979eebaaaccdf3b030` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_mean_ch2_ON_cmin_1.png` | 35905 | `63ca6a1a37c68e94c8cb1fe7fcafb4c7c40de4ff86b6ea3827c355e634f8f26e` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch0_OFF.png` | 38492 | `dc4697740ddfcad19276d7b26f4c03b0664d0b2c57c088b6af92f82da99749cc` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch0_ON_cmin_0.8.png` | 42268 | `20090516691eedf0f26c995b78e9ab649f010ca252bf9dce86e71ff791d16f7c` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch0_ON_cmin_1.png` | 37611 | `af1ec6c559b74e50db897a2ac958661e1ce7b6e25d0ee852bc681206c96bbc3f` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch1_OFF.png` | 41521 | `c8967c41827c12f155133576512afaffa9267530b8fcc1ddc92e83999d8422e7` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch1_ON_cmin_0.8.png` | 43205 | `6d4c49e268ca6c795fd969cdb622f28f3c7effb6346345b20ef57c1ee71c6599` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch1_ON_cmin_1.png` | 37431 | `f4aa61d5ed80aeb416fd0f4d8110dc3da2da709fbcde8ab60f58f62ef3e1f94f` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch2_OFF.png` | 41658 | `b165ea871f2a5013462fab727bf23cc6fdfcf0ff8df0d27a80381c064ae70c1f` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch2_ON_cmin_0.8.png` | 43290 | `20bd8d1b2a3b535874da41bd2a34d4bd0c97f09b0a909b226af26b59f72ea1ef` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_dist_median_ch2_ON_cmin_1.png` | 37684 | `a8d43532caa78fbcfb37c36ee7ba15c891ed2d9367a5dd9f58f1e324d4984c7c` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch0_OFF.png` | 41497 | `a37ab423e235401affea7fd2434f472860821c85ec8bcf788f178a65c9952159` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch0_ON_cmin_0.8.png` | 43090 | `feac0485578dcd3231c027222eb203df93bda18251878af54a860a991100ccbf` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch0_ON_cmin_1.png` | 46930 | `7c72278d53d0d8dd56a9ef69b0e57df3054b59f9d05a427ecc8fb99037c17664` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch1_OFF.png` | 38304 | `e09630cc06c81cb9c2ba87f1441d97bee5d12b6945ad3639cae05c8dbe455533` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch1_ON_cmin_0.8.png` | 40403 | `1ecff7de59d505e813ebbe6a9b4fcf1339c9892f1ec1220e4ed587d5d803bd9d` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch1_ON_cmin_1.png` | 47702 | `4d858e0a91f9fad3c11606a28ec4a24ac79b7c1d9d513f51273a70d06eb502a6` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch2_OFF.png` | 45992 | `236dcd852df898be1ee5ff200653ce9702057fd3ef48514d4ddbe574dbe7f160` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch2_ON_cmin_0.8.png` | 47646 | `a4156e756634f422ba1399a8a1255c000f6d099f3f29de1b95a3029a50eb3ca9` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_10deg_ch2_ON_cmin_1.png` | 46871 | `59964b19c56293d12ef479dbc15e819185e5ab6a0eeb7eebfc6653a646812391` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch0_OFF.png` | 45591 | `686a9f7a8c8f238f5ffa6423fde53951b0e0ff334598a9d40c296936bcba94e4` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch0_ON_cmin_0.8.png` | 47308 | `6021477f1203a7ff5d47f93a8bb28c11a4abde71de087e6265afaddf8992d7d0` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch0_ON_cmin_1.png` | 39322 | `76865fc3e268237ef771bcc4caf6dbc9795cc6f54711bef87ec9af488781f4fa` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch1_OFF.png` | 42979 | `a26d83746288688edb89e5b966c16c129713d13698642b143e9c03107582ddcd` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch1_ON_cmin_0.8.png` | 44722 | `1d72281e510ec08c6372a53a315e00fe158d9c9bf740fbcf82b8dcaac6ee8694` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch1_ON_cmin_1.png` | 39729 | `7ff10da24724fc0fb81c2dfde58c49975d4ae9cd6a4181a034b2316939f9b7e2` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch2_OFF.png` | 36821 | `4d896f6f850bada54a169e0c4dfc949365c043c9bc21a19a4086cbc7c19a1afb` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch2_ON_cmin_0.8.png` | 38224 | `835100f4693657150cd2446179c20069a2e2751fb0e3e5ed2faa0d8b27cf6b57` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_15deg_ch2_ON_cmin_1.png` | 44052 | `50e18588b93183fd4f2f3481910877ab1435aca7ff69f7185f4e01fe87f271aa` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch0_OFF.png` | 45082 | `83926d381eb2420a14394174e72366f63752c8b0503ef9de8461655dfda8a856` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch0_ON_cmin_0.8.png` | 46641 | `bf3b43b057654393e946560f08c373c897f8355f59998152199334c08f487b1d` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch0_ON_cmin_1.png` | 44029 | `d0a9c1e60240f33e76c68c2a1d0689347e0bad3e23841f7220db321596299575` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch1_OFF.png` | 38239 | `2ce539e978201ed628e14f98e995ab422037dcfbbff59901c32160c45dc74bde` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch1_ON_cmin_0.8.png` | 39982 | `00fd66a8c89afcb5043671dac5461baf665d90d61e17929a879a2bfc22d1d979` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch1_ON_cmin_1.png` | 39524 | `c2610c0c86bf4b2158a70dc06a637e53e3d5bc47b1569f7d7409ba1de4bc0e23` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch2_OFF.png` | 43219 | `0f7d2bc6d33615c4813eab2ab5beaaef060d92fe3d951bdc8c8ff14dba1a14f6` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch2_ON_cmin_0.8.png` | 44712 | `9989950fe22e7e5191c3124f7b7a42755a4322b2b396bd4ff0e8cfdd0df09b19` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_2deg_ch2_ON_cmin_1.png` | 51835 | `f02b0e1d6ab8b5bc25532fcbcd2302d53a314445a5d06eedd31303dbd711a2aa` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch0_OFF.png` | 43846 | `80eef23fbd686c33f13e0232bc5463cdf2aab215ed7106a4f12daeb09e5c8fe1` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch0_ON_cmin_0.8.png` | 45510 | `5e129fba92d9e8b51a3788f07e570da9bfd7ab6d5be0e7a2d37ca0b5d188fb95` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch0_ON_cmin_1.png` | 40018 | `c57d23bc8f78765207d6e0ece3f1626d135ae30f84afd5f522a062a40c031638` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch1_OFF.png` | 40540 | `d6d54c3aaf3fdef31af65364302be26bb79465259022eadb0a33af1ea4747ac7` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch1_ON_cmin_0.8.png` | 42263 | `e80641d94ad98d6ce323230dbac6bfaa9842698d0ea986250693634738f2e2bf` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch1_ON_cmin_1.png` | 43681 | `d649d385a385bc5900b805c31b3d303c5a330be18e44d4395c51a52be2235329` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch2_OFF.png` | 39896 | `63d1fedebd4cc443b89a31ec224a339c8410b1463a84e3f5f82642242f920740` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch2_ON_cmin_0.8.png` | 41632 | `573ef8e7d97108534171aa7d658dfe28bf765b87b50dc798fb4ccb302660ad3d` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/plots/heat_frac_le_5deg_ch2_ON_cmin_1.png` | 41198 | `15ede177274a457581d66aac09201abae25cbd130e6cbb6bf4fd42744438c399` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/ray_alignment_all.csv` | 16207 | `68339f5d736431bde57f94d85aca360bd9b2360df611635d55d0b11e7cdd1bf8` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/ray_event_alignment_all.csv` | 16297 | `ea5ae0538a91b23aa789d830d3f893be124c1094bd05cf7df6b553210094adce` | artifact inventory |
| `outputs_dt_optional_suite/_aggregated/summary_all.csv` | 811735 | `157c73889eac8a9a889fe21fa63ed74c65bd9a1055de87514ba314db102ebe36` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed0.csv` | 110756 | `95858b3a3c552eb22b2a5d8e3fe0a8f09a527937b0616c3e222e951bc1222925` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed1.csv` | 66744 | `918e503b086d8177b809c1755737921a34b476f7b29f81398e5293c49743560f` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed2.csv` | 67 | `afc07cc2c9525f361679f50d2bcf509814e52e9288d6b64a7ddf99bf71d1106a` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed3.csv` | 114398 | `92442234e9f739a6d56e70c9df73b5dbabcce1a8aaed07e42c334ff106f621f2` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed4.csv` | 76626 | `35c8e5d13859d2d3bdf701e9ddd48e5ca37666babb0485c085eca620a2915aaf` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed5.csv` | 67 | `afc07cc2c9525f361679f50d2bcf509814e52e9288d6b64a7ddf99bf71d1106a` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed6.csv` | 159 | `8ad84550ba4bbee199937ef8cda957bd5a3075c5bd284d5c8e25c1756e850dd0` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed7.csv` | 32983 | `ec12bbe19e1ed16bc19a62f2de6eda58efee9bd59d41271cafa5af9d60e130a2` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed8.csv` | 78959 | `039e5aa9d3e6eb9344d9d54271c585d027bf75b50b3d73ad85a97b81035aa1bb` | artifact inventory |
| `outputs_lf_warmup_sweep/events_seed9.csv` | 67 | `afc07cc2c9525f361679f50d2bcf509814e52e9288d6b64a7ddf99bf71d1106a` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed0.csv` | 27353 | `1e3f2336e47c4e3c75462437fc8be7d8f45f531aef6ebef64ef693b89dfcf61a` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed1.csv` | 25890 | `8d4c1f8b12d616d07947a6dd2a9d0951ed8e8856af2ee8083cbf796d1d4d2e5a` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed2.csv` | 25683 | `98e9284ce49d4472106033f568709950978b66c7de0d495be2cf77d254a2a143` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed3.csv` | 27568 | `e2a9a0108dca14dd7e49590fd9901c6d16601e795344c230ebdcce1991f5f2f2` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed4.csv` | 27054 | `ec93e3acb52725b84866bda9643f9e62f3adba614219e938793a66573f0f943a` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed5.csv` | 25577 | `3cc346aa6154d646d0a9c318466ff63cad7c057920c6c2b7a3292db92400dd8b` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed6.csv` | 27138 | `944e61b4155e9a02cf20cdab957bf4fd4c209f0daea69a0e7127f356e99cdf58` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed7.csv` | 26278 | `c676973d0b1943e0c9cf2a20549cfbcc645ada2836b49ff2081da893e7904e1a` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed8.csv` | 27580 | `df9c16ac0ddbbfd3fb41c111997bfd689288cd187df43e9378488a2683c2f565` | artifact inventory |
| `outputs_lf_warmup_sweep/perstep_seed9.csv` | 27031 | `777a5445dfff37d503196a6a212719e6ef4037d7b59aab51d818565c70632bdb` | artifact inventory |
| `outputs_lf_warmup_sweep/summary.csv` | 2955 | `82f9b8de85b01a25731ea63a959a5f68a7136360aadf70d60114769c7fccea95` | artifact inventory |
| `outputs_patch39_unified/escape_fraction_vs_lambda.png` | 67306 | `cf280ee4794ee57f369d474d199c4aba69e25fe1acd2c4805f55e1219db9d004` | artifact inventory |
| `outputs_patch39_unified/paper_figures/_agg_summary.csv` | 287085 | `40c8f8771bd738c1b7ba3a8e6c212e8d5e0fea102f3b84b7bf810fbf589b3797` | artifact inventory |
| `outputs_patch39_unified/paper_figures/_schema_report.txt` | 1194 | `392b7cb26c49f2a2f70ef8f18e94f762ade8678c092102bb78fe2aae69a43482` | artifact inventory |
| `outputs_patch39_unified/paper_figures/class_fractions_from_seedtraj_vs_g.pdf` | 10742 | `c364d65d65fe34b6d58293636f4b3a022cdc0e2f8d75e5c0919d4542c824bf9f` | artifact inventory |
| `outputs_patch39_unified/paper_figures/dist_to_ray_vs_theta_span.pdf` | 160471 | `28795098962ff3c77298b3719db33de015c431dbf4f6653071d664d8bb7e933a` | artifact inventory |
| `outputs_patch39_unified/paper_figures/exit_time_vs_param.pdf` | 10818 | `ec5147430c291fca173201ae38317d1cf073a5d7215735324b7835e4cbf52872` | artifact inventory |
| `outputs_patch39_unified/paper_figures/phase_instability_vs_param.pdf` | 137043 | `f99a9ffe7561e94b85d67bbb41980e3dfefe4299498242a93715b3e774d87865` | artifact inventory |
| `outputs_patch39_unified/paper_figures/seed24_Phi_coll_curvature.pdf` | 12531 | `6aaf033c89e2472f866af911001ad1ca54e70c6ac82ef43994a3698cdf1cb97b` | artifact inventory |
| `outputs_patch39_unified/paper_figures/seed24_Phi_coll_timeseries.pdf` | 12950 | `94acde491c95600f785b2982a9c6953339af0833dad8c0cf33d6d1b228718b55` | artifact inventory |
| `outputs_patch39_unified/paper_figures/theta_unwrapped_span_vs_param.pdf` | 134869 | `9f2dea2b460998faa426402278c886c66e861312236344647131cf02ce97307a` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.00.png` | 62080 | `4f362fd5290a1ae04c8055b706b8f56213e9e24ef6c6e8932fc2c934f71f3c6d` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.01.png` | 61330 | `a42fea8e32a371c30296ee974afa021e683483fec25fb9bacbee435fdb39d7c2` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.02.png` | 62210 | `62a20951f27a99fe483be7d7ef735d07c2a4d25cf81a041f303885060a1bcd7c` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.03.png` | 61871 | `939362695f88458fd77b8123414a7d0f3f945bf292a2a9fb3ca94fcaa5a08564` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.04.png` | 61533 | `e989271601a47aef994f46c09779ad15bb94ad9cf76833deb150258067f0db3f` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.05.png` | 61712 | `33fbb3a845488a4191b9b5bf71641a824f4cab9215d34a13ea8918d223cd7204` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.06.png` | 61655 | `6bc1df8eaf3586a6a092bae184ae3565ca9e2c076dde5c12327bcf8cbc808302` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.07.png` | 61314 | `799992a4bd838c71f88e006feace7faab6ef847dfece71c2c598469494da025f` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.08.png` | 61849 | `ff1bb14a728038f540bf85cae809834ae265ccfb3e431d5a252f4a04c1e9cc51` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.09.png` | 61800 | `78a25c1052b6cbacfb879712fb4c3f8d2fddb42d877e051f7247095e58abe4cf` | artifact inventory |
| `outputs_patch39_unified/plots/dist_to_ray_lambda_0.10.png` | 61080 | `8490c129fff3562375021d19ff6107340c7ad1a4e6e88d8793ec6968fbd47f53` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_mean_escape.png` | 103019 | `ab059ac68b0228317ae62aeca585a2d57bf7e37e426a58767b894bae3161e1c7` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_mean_escape_minus_grazing.png` | 114631 | `887fe4512144b11f0b2835aaafdf22e5ce073e7f6cc2caf4b909dc04a8e3d98d` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_mean_grazing.png` | 101584 | `cb9dfb2acfdb1758f3f137e88d5ce3d81a476ba4553dd02473caf1fa9980acb4` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_median_escape.png` | 102994 | `65b8c0604b81485c38a685e174d7c4698b8c88ceaaaa83878a6ca9a64e979be6` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_median_escape_minus_grazing.png` | 75712 | `a5c683aaec8ee92efce400712bdedd1c2768024f54ca2d4dd1593a2ddd5ab35d` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_dist_median_grazing.png` | 101509 | `0925ea7189ef896de0ca10c4bba2b778cdb709ce2dac38f586c89bade53a035d` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_10deg_escape.png` | 96728 | `a671a02aed7a7129a0940191b357ffcf15059ee950b18d8be18c1db1f02fab7a` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_10deg_escape_minus_grazing.png` | 112472 | `cadc7d4f951e2a33ab71b42da5b855a286b343b49244cdb52488465c20bcfeb7` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_10deg_grazing.png` | 95947 | `30597d8dc20b9b50e598784d7141410a0ae7650833b22b89e955d33c5b0c92b2` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_15deg_escape.png` | 94966 | `9a211e7827f467125aa4c36db0c9c6df77b71997ff8854083cf9076418eaed79` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_15deg_escape_minus_grazing.png` | 121270 | `35818971851c9003cf99379677c468fb3d0954997dde279cd47e83b953b10042` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_15deg_grazing.png` | 95147 | `50b110ff2e93f9ffc805858ef7192b014c4091ac9fc6ce03ea253f1f090de68c` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_5deg_escape.png` | 96326 | `4adcc532cd1ce9c8d776ff13f0ee48b0b01148083c9c6d16ce9d8e8297ce62c1` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_5deg_escape_minus_grazing.png` | 113688 | `71b24958f77cf29b0bf12a161b9bcbef590889a5d0654bd4b2c2d43b65f98584` | artifact inventory |
| `outputs_patch39_unified/plots_ray_heatmaps/heatmap_frac_le_5deg_grazing.png` | 93870 | `b626e55db55b800d51e025c535f3f4b60f7954dff928349f39f0a7dcc96ec130` | artifact inventory |
| `outputs_patch39_unified/ray_alignment_summary.csv` | 9336 | `cb2318a199c575aed8b4e69f93a5b75a544c0f73fe53aacf6699f550439abf0a` | artifact inventory |
| `outputs_patch39_unified/trajectory_class_summary.csv` | 3119 | `3e4adae1185e20651818118efd6fbf16f8566fc2db22191697c82bc53b5baaa8` | artifact inventory |
| `outputs_seed_emission/detach_events.csv` | 298451 | `49b259c1fec5a0641ce86029478e290e9f1f42844b3b6219290a0e11c16066f9` | artifact inventory |
| `outputs_seed_emission/run_summary.csv` | 152 | `e34550441aba0101eae81742a9a90b8a5667d9855ec23e9684ef7b3f9b9b97a8` | artifact inventory |
| `outputs_seed_emission_sweep/A/detach_events.csv` | 1948 | `ef548a94506e743279ad3accd74abbddcdd4578d0555e2fb7939a5564d4fbbec` | artifact inventory |
| `outputs_seed_emission_sweep/A/seed_summary.csv` | 1135 | `eb4bb915624a07fcfa6ef105e6de5a6bf5194939db06a8e517e94de20ec0aebb` | artifact inventory |
| `outputs_seed_emission_sweep/detach_events.csv` | 41704178 | `c3f2fba6a856036b8ec166261c1eeeb2f335123a187d53b9e584383b8c0694ba` | artifact inventory |
| `outputs_seed_emission_sweep/seed_summary.csv` | 1243 | `34bd143db1e4f193e04aa570c07962f94532ed65bbc2df6be1e154b211e3b26a` | artifact inventory |
| `param_scan.py` | 2228 | `48f25969ee6da71d305b3bd5dd06681f0ba628d01ec056ea8e4e1b9bf693f081` | source/support read |
| `pathing.py` | 8467 | `e56adb78c64d4b4a6566849ed72205f0309d1e611f99258b1ae7720e8b486678` | source/support read |
| `phase_triad_experiment.py` | 14296 | `03b46cc00c3f98c1ded5a3f6588f218fd60329f31959845de438230723e47033` | source/support read |
| `phase_triad_sync.py` | 1281 | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` | source/support read |
| `phase_triad_test_events.csv` | 5307583 | `5a56dfbad6b459d14332d3d7d2df773aed51baaf4d7bb510159236725877c269` | artifact inventory |
| `phase_triad_test_summary.csv` | 1832 | `cdf33b2b4edc9fbf00975662f232e09c7f57838ce73cc721c4fd411b7a1a18a9` | artifact inventory |
| `physics_sampler.py` | 3906 | `7cf80e1fd8fe67f33e4276772eaf8f19a4fedbd7ed91357aeab3a509a27749c2` | source/support read |
| `physics_sampler2.py` | 5841 | `d7a0c02d242e4333d07f25c49f83a005eb697deb3a0c0b2b9239105aad413b7f` | source/support read |
| `plasticity_boundary_slice.csv` | 2676 | `42093368421a494f994a6a4cecb8b2ca21b5e4f35735218d8cf69594a8cf0dbe` | artifact inventory |
| `plasticity_focus.csv` | 319038 | `c77a598c66e8902a426d169000cd1c4052f0291fe2dc398f63fe48ba337a5512` | artifact inventory |
| `plasticity_map.py` | 7671 | `a165a706b07d66ace13050d7db27025eaf752ef79e3939ffc5c02360f8e78975` | source/support read |
| `plasticity_seed_check.csv` | 1721 | `f42b7c48fed2d5628af13342e0e80e2fbef7aef5dcb41720b2390af6058c55d2` | artifact inventory |
| `plasticity_seed_robust.csv` | 1847 | `7829e60b387e3f7572db57e5bc11c6680c56fe3b81a20d49358a27c0e17d0576` | artifact inventory |
| `plasticity_zoom_eps0002.csv` | 517370 | `2c7b3600cd0077c5acc1c6db25b1550f4b794d54812aac42e2e93f443738b223` | artifact inventory |
| `plasticity_zoom_eps0005.csv` | 514434 | `18733bd848edc1720370ef41f94f37b98bd4263900ddf9791ef7a556a660bd45` | artifact inventory |
| `plot_dist_to_ray.py` | 1792 | `f6a8c72ec28e792aef20b1f7347f7935b383aa56cda0370494c08d065b0711b3` | source/support read |
| `plot_edge_map.py` | 6634 | `d86e3ffd3fddb08841e89ec7863e69e4607f8bfc0d326239aaae3241f6f8313e` | source/support read |
| `plot_optional_suite.py` | 3506 | `a4a1e0ae4acc766420e8a99aef76a8493ee24bb0b7fda0c25f8b52c526e84c9a` | source/support read |
| `plot_rgd_heatmaps_from_rows.py` | 7072 | `afd2f04844b0809edca77d6c07fd272c151b55e4a88c73b3376002eee93a27b0` | source/support read |
| `plot_sims_summary.py` | 3465 | `0d54d61a6e7625100c7bb7e39f1eb830a8b6c7dd47706d0093ccbba33665cb65` | source/support read |
| `provenance.py` | 1243 | `45a7e050ca37e017ec670eeefe055a2e261e165bcd4b7cf7954a2327acbe0bbc` | source/support read |
| `README.md` | 8758 | `2aff3da7752daf669f18ba25fc07a3342886ba23b9752da8efa842c04ec06e06` | source/support read |
| `README_threebody_probe.md` | 845 | `512c3270deeaa75800d83bcce30eacf93dc6c0f4f8498b4cbe996e3f77e15ef8` | source/support read |
| `rgd_connection_diagnostics.py` | 14654 | `cd03ab482f6e5949d684568fef98599cc39f580189ea3cdd3d8de3c3bbe5d614` | source/support read |
| `rsb_dom_band_demo.py` | 1861 | `012f37604d89ab5c8381c0bdc3f1caad16ffde5d85eeae5a200d9e6949420c36` | source/support read |
| `rsb_entropy_demo.py` | 1796 | `4af672674a2b8f5c2d8f963172910bb4d14d373e34d610286f7a2f82d71d01f5` | source/support read |
| `rsb_model.py` | 13034 | `70f8966a753393705510de0823c780e03f19782086d7361a095b09ed60746e9f` | source/support read |
| `rsb_param_scan.py` | 7882 | `b6d89cebd9ff78b6ec5624ce58211c69459d467f5f54c6027e33cfe4c7e40bb2` | source/support read |
| `rsb_phase_scan.py` | 1738 | `d4c4618443e9ba7cc2c43b4f0e813c07de656d0f80e2225237926a4d7bfa6c4e` | source/support read |
| `rsb_spectral_demo.py` | 2772 | `0c6b5a7093feb629a5c35883a7d8a1e9f363130d07e71cbfe7a35dff13aaea2e` | source/support read |
| `rsb_spectral_viz.py` | 9260 | `fd7248e6cfd0285df5d78df8554e3d7d76cecce717685c4cc82a88c8c9a10f8a` | source/support read |
| `run_patch39_unified.py` | 16846 | `811dab67ad515a8c03ada843fb489c6a9e19a5b77988680eef5d040e9708bfca` | source/support read |
| `run_seed_emission_csv.py` | 9109 | `8c3a2dedec331004de9c78a7510dd241097fc7ac7293312f85213aa22ed33827` | source/support read |
| `run_sim.py` | 8095 | `daa7f0cd13ed36575fbfcafa14c5b75a9bd10263013127269853ee73a28361e3` | source/support read |
| `run_sims_minimal.py` | 6710 | `7cfe9437405cdb72630b9278d2b8d7f7c3ea4b11a7c8218e2a924c9231d995f5` | source/support read |
| `run_suite.ps1` | 1726 | `7cea9f1b404f6abc6b2fbd2b5b0ca49834cb8defeff7239cee24ddd08f820f04` | source/support read |
| `run_tests.py` | 10950 | `f4761116fca3e36bb85d929daf6c2a76f2a4d9132b8efdca02d2515dcc3e0480` | source/support read |
| `run_triocta_structural_3body_probe.py` | 6957 | `9d25a59e106450e3ef27c8bcc5e7998d8e1ae5d322f2ae55c974117ad210271e` | source/support read |
| `run_unified_diagnostics.py` | 21217 | `db08cf059ce6c3a61db6152ac869a7e4f5f485d4eb3470718abbf081d784cafc` | source/support read |
| `sanity_report.py` | 4750 | `cc1b3373dbd3f5ba9dd2402b0a906e3c492f8d371a82c37ac16eba93bef803a5` | source/support read |
| `scan_rgd_connection.py` | 15745 | `f7e6c67a34b6312885b28d2e8612a8bfb5ae355d12d026a477144f350c88c445` | source/support read |
| `seed_emission.py` | 3580 | `c4b97f833c1192d03d00e992717ef4c4c49dd5f590326089c6ee57019877ef66` | source/support read |
| `seed_entities.py` | 3803 | `55fd2d1d45ed3aab1d98016fa5395ec53a32b0d89448c98707c2f64d0c82cc1d` | source/support read |
| `seed_trails.npz` | 15148 | `580d93ad7f2ea2e2e43e20401c409c6e6320273604de73f9f8bf744a36c534ca` | artifact inventory |
| `seed_trajectory_analysis.py` | 639 | `b269f46dbcccf3a89434355f7e0c63bd1a5a0b3b3b644ea7785c780414e1a6e7` | source/support read |
| `select_golden_points.py` | 5322 | `3611dcad83dc5dea20fda1a9e3115ac1c6ab4db35872b2b28241bafe659873c2` | source/support read |
| `semantic_diagnostics.py` | 4231 | `cabbd7de2009f0127bd64542c3ab972d0c187b089e305d36fb35a1c878de84bc` | source/support read |
| `side_zchiral_probe.py` | 5200 | `0fb8a724ac26cfe98fdf6543cd30b57055e3a0d44569d98b70e8e05382c674a7` | source/support read |
| `sims_diagnostics.py` | 3839 | `87da093797f4f308a3cac107be36a3a22db52b4d87e69cd64c384fffc53d7848` | source/support read |
| `spectral_viz.py` | 7158 | `0d999f43ddd4647aae5af367aed88c4185879d9f793ca6c64723d7271ec2e55c` | source/support read |
| `su3_basis.py` | 1043 | `2ccac73c3aac18f79b76eaa432f27bfa23accc1acc99502a3a6a05b71f4617b4` | source/support read |
| `summarize_edge.py` | 4461 | `544d84ae0f9b8783894b042558fff6f976b9aa308b8003824d98487cc4eda1d7` | source/support read |
| `summarize_ray_alignment.py` | 1117 | `4b2910fa1eac18cee267631cebd62ea04541af20b1e15a506ecdbf189f26abbe` | source/support read |
| `tangent_corridor_analysis.py` | 10075 | `8596940375d1f299a6e8fef40b49e9a603405298867594f276e95fdcd464c81b` | source/support read |
| `toy_3d_triocta.py` | 34542 | `3792d0d97bd7e0beed157586453ea71a3828e6a79a4ed8638787163cb490ee05` | source/support read |
| `toy_lab.py` | 11551 | `30c5c786a49227fd4692457219515c6fca73d53337feee09e6fe321d8322f84d` | source/support read |
| `toy_ui.py` | 25598 | `e78f968b2201d2bc9762ec3433a259f63488d6b41ec03d86195daf9d4b4590c3` | source/support read |
| `toy_ui_live.py` | 8158 | `6c0f741a90ad242ff4564767e642dfe2dc5f36febda1677c1afdc01a2361bd6d` | source/support read |
| `trajectory_logging.py` | 3823 | `9e0d869aa4610e2fff9ca4fc39007226ba3dbdeabbbf4e033011fa15ec09d8cb` | source/support read |
| `triocta_probe_utils.py` | 2322 | `df32ffd8eec1e0c07e634ccb7e023422d1f8ad67168ec423b9241048693e75f3` | source/support read |
| `vrec_ts_critical/v3.7_p37abc4f4f9_s2158500047_Z_total_series.csv` | 156617 | `7ce305198d6d5fc5c04dcd2f82ccc78f7c3ed64786db0cabea9c1fddc9c53992` | artifact inventory |
| `vrec_ts_critical/v3.7_p37abc4f4f9_s2158500047_Z_total_spikes_abs0.8_win25.csv` | 6431126 | `9f28ef9a701c3f7057bd0baebf3538489e630eb8b4884b7f52203d5c5711ca8d` | artifact inventory |
| `vrec_ts_critical/v3.7_p37abc4f4f9_s2158500047_Z_total_summary.txt` | 310 | `11512baff500497d53d9ff149025179f92521565ee7bf00926794fc8bff98c6d` | artifact inventory |
| `vrec_ts_critical/v3.7_p37abc4f4f9_s2158500047_Z_total_vrec_spikes.png` | 43642 | `31e86aab28754b624ba037083c4678699f66dabfc6628ffa5214415dcef79eab` | artifact inventory |
| `vrec_ts_critical/v3.7_p37abc4f4f9_s2158500047_Z_total_Z3_time_scatter.png` | 195629 | `8e21297431aa82268559f060a149dfc99b409cb754afd19bff5c6ef16802d646` | artifact inventory |
| `vrec_ts_subcritical/v3.7_p869bf44ed4_s2158500047_Z_total_series.csv` | 238196 | `6bd9730c3d53ef54b814d2c7dff72b39b2467285ada7250f93073267001039d3` | artifact inventory |
| `vrec_ts_subcritical/v3.7_p869bf44ed4_s2158500047_Z_total_spikes_abs0.8_win25.csv` | 99122 | `c827cc01af95474aaa986c10d4cecea1578925023cf22fcfad7244be33a53ac1` | artifact inventory |
| `vrec_ts_subcritical/v3.7_p869bf44ed4_s2158500047_Z_total_summary.txt` | 307 | `1d48c0dfef41f89fd366aac606fcee021e600785905d054bac663622b3e2c05d` | artifact inventory |
| `vrec_ts_subcritical/v3.7_p869bf44ed4_s2158500047_Z_total_vrec_spikes.png` | 44337 | `67f51270f15aae8376b1c017072088c113972f876dd7390924f2f7f0c863c012` | artifact inventory |
| `vrec_ts_subcritical/v3.7_p869bf44ed4_s2158500047_Z_total_Z3_time_scatter.png` | 208093 | `e4367c7cf95b921635f5f83a9d3c74e1448b334ce9bd9f7911e64040ff5e4c4c` | artifact inventory |
| `wide_scan_triocta.py` | 11822 | `32a5d35aeb09df5acd6495cbfb90cbc8fbebfea8494964857619d83d8add4fc5` | source/support read |
| `z_spike_diagnostic.py` | 9499 | `7db50da33b7e2f188f2ffd43212bd713a27fc7b46c73f3e7e612fa49c0ca185c` | source/support read |
## Appendix D. Preservation verification and closing summary

The before/after fingerprints below match exactly. The fingerprint is SHA-256 of a canonical JSON map from relative POSIX file path to SHA-256 of original file bytes: sorted keys, compact separators, UTF-8, excluding `.git` paths. Directory traversal includes ignored/untracked files and bytecode. This verifies path/content preservation in the three listed scopes; it does not certify filesystem timestamps, external runtime state, or a remote repository.

| Scope | Files at start/end | Before SHA-256 = after SHA-256 |
|---|---:|---|
| Full OLD tree | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` |
| Full TOR kernel tree | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` |
| Full current checkout excluding .git | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` |

Read-only Git verification with optional index locks disabled confirmed unchanged current HEAD `0fa3b582c086e51371e8a784bc3dd145f88cfb2b` and production HEAD `a06edcc5c9df5d3b56405085d9f2942b768dc203`. Both still have no tracked changes. Pre-existing untracked archives/test outputs were retained. Production caller tracing outside the kernel was read-only; the whole production checkout is not claimed to have a byte inventory here.

Report validation checked that all54 registry entries and92 source/support entries are present, geometric and visualization IDs total19/20, all28 numbered Hilmir questions are present, and all local report hyperlinks resolve. This is document/inventory verification, not execution of old/current scientific tests. All18 byte-identity production claims were checked directly against file bytes. The sole created artifact is this Markdown report, in `C:/Users/Notandi/.codex/reports`, whose ancestor directories are outside the repositories. No implementation action follows this census.

Counting reminder: old inspected-source92 =89 Python +2 Markdown +1 PowerShell; old UI4 is a subset. Artifact inventory401 is separate. Production source21 excludes43 bytecode files. Current reference19 counts Python kernel modules, not supporting UI/manuscript files. Categories below count primary classifications of M01–M54 only, not file counts or acceptance votes.

```text
OLD_KERNEL_FILES_INSPECTED = 92
OLD_UI_FILES_INSPECTED = 4
TORMENT_KERNEL_FILES_INSPECTED = 21
CURRENT_KERNEL_FILES_REFERENCED = 19

MATHEMATICAL_SYSTEMS_FOUND = 54
GEOMETRIC_SYSTEMS_FOUND = 19
VISUALIZATION_SYSTEMS_FOUND = 20

CURRENT_SCIENCE = 15
VALID_MATH_NOT_PORTED = 16
USEFUL_VISUALIZATION = 4
EXPERIMENTAL = 10
TORMENT_SPECIFIC = 6
SUPERSEDED_OR_DUPLICATE = 2
MEANING_UNKNOWN = 1

QUESTIONS_FOR_HILMIR = 28

REPOSITORY_FILES_CHANGED = 0
TORMENT_FILES_CHANGED = 0
COMMITS = 0
PUSHES = 0
```
