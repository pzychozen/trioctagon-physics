# TriOctagon harmonic-three provenance ledger v0.1

Date: 2026-09-29. Read-only archaeology. Current authority: frozen commit `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`. Source identifiers S01–S45 resolve to absolute paths and SHA-256 hashes in the source register below. PDF page references are one-based physical pages.

## Finding and date limits

**The earliest recovered document containing BOTH the pairwise third-harmonic synchronizer and the third-harmonic coherence is the December 2025 v3.9 paper, S14, pp. 2–3, equations (6) and (8).** Its PDF creation/modification metadata is `D:20251229191909Z`. The title says December 2025, not a specific day. This is a documentary date and embedded build timestamp, not independently verified public publication time or the date of invention.

The earliest recovered Git attestation of executable code containing BOTH is the TORMENT addition of `torment_service/kernel/phase_triad_sync.py` in commit `f462b312809996ea96bff382adddf37b5b0fa596`, author date `2026-03-08T12:44:05Z`. Both equations are present in the added file. That date attests the recovered commit; it does not date the original writing of the code.

**EXACT HISTORICAL DERIVATION = OPEN.** There is now a recovered historical *claim* of derivation: S14 §11, p. 5, presents the interaction as uniquely following from symmetry. Its conditional Fourier reasoning does not establish the necessary phase identification from the earlier geometry, and its potential-to-gradient calculation omits a factor of three. Therefore finding this section does not close the requested provenance gap.

An earlier documentary precursor is S20, *Emergent Z*, dated 21 November 2025: a **single orientation variable** has a potential `V0[1−cos(3(φ−φ0))]` and force proportional to `sin(3(φ−φ0))` (p. 7). This is a harmonic-three orientation ansatz, not the later pairwise sum over three complex channel phases, and not `S=(1/3)Σ exp(i3φk)`.

## Exact occurrences and earlier alternatives

| Evidence | Occurrence | What it establishes |
|---|---|---|
| S14 p. 2, §4, eq. (6) | `S(t)=(1/3)Σ_k exp(i3φ_k(t))` | Earliest paired-document coherence found. Here the denominator 3 averages three channels; the exponent 3 selects harmonic three. |
| S14 p. 3, §5, eq. (8) | `φ_k(t+1) → φ_k(t+1)+λΣ_(j≠k) sin(3(φ_j(t)−φ_k(t)))` | Earliest paired-document synchronizer found. Printed time indices require the separate review in correction C16. |
| S14 p. 5, §11, eqs. (11)–(13) | Pair potential in `cos(3d)`, claimed gradient and update | Documentary design rationale, with a mathematical coefficient error and an unproved geometric premise. |
| S08 lines 23–25 and 39; S13 same file | `d=phi[None,:]−phi[:,None]`; `lambda_phase*np.sum(np.sin(3.0*d),axis=1)`; `np.mean(np.exp(1j*3.0*phi))` | Both executable formulas. Self-term vanishes because `sin(0)=0`. |
| S09 line 49 | `np.exp(1j*3*phi).sum()/3` | A second coherence implementation; not a historical derivation. Its example main uses a DummyAdapter with fake random dynamics, lines 401–415. |
| S44 lines 109, 177, 191; S45 line 13 | Runner sets `params.lambda_phase`, steps the real model and calls `triad_coherence`; emission module also computes `mean(exp(i3phi))` | The v3.9 paper p. 18 identifies the unified runner as its experimental entry point and the earlier harness as exploratory. This connects the release description to the recovered modules without authenticating any particular run output. |
| S10 lines 149–151 | `apply_phase_triad_sync(Omega_next, ...)` | Synchronization follows the amplitude/graph update in this recovered old kernel. |
| S01 lines 66–96 | Sum over two cyclic neighbors of `sin(3*(neighbor_phase−phase))`, then amplitude-preserving reconstruction | Same three-node phase law in the current kernel, applied to the pre-sync updated state. |
| S16 p. 17 §4.4; p. 63 algorithm | `(κ_Tri/3)Σ_j sin(θ_j−θ_k)` | Earlier **first-harmonic** three-phase averaging in the water model. The 3 outside sine is not harmonic three. |
| S17 line 49; S18 line 53; S19 line 44 | `kappa*np.sum(np.sin(theta[i]−theta[i,k]))` | Recoverable implemented first-harmonic coupling in that water family. Their parameter normalization versus the paper's `κ_Tri/3` is unresolved. |
| S34–S38 archived core update | `Ω ← Ω + εΩ*(k−abs(Ω)^2) + delta + gLΩ` | Earlier toy-kernel snapshots have no separate phase-triad synchronization stage. Their `phase_lock_step` name does not establish one. |
| S34–S38 scalar readout | `z=lam*rho*cos(3*(theta−theta_lock))*exp(−gamma*t)` | An earlier third harmonic in a scalar clock/readout, with a different variable and role. It does not prove the origin of the later phase coupling. |

No inspected predecessor in the recovered kernel snapshots implements a separate `sin(2d)` synchronizer. No documented edit changing `sin(d)` or `sin(2d)` into `sin(3d)` was recovered. The positive evidence supports **sync-free earlier toy-core snapshots plus an optional v3.9 phase extension**, and separately an earlier first-harmonic water model. It does not prove a direct water-code replacement or a complete release-by-release transition history.

The graph term `gLΩ` can itself produce first-harmonic phase exchange when rewritten in polar coordinates away from zero amplitudes. That mathematical reformulation is distinct from an explicitly added phase-only synchronizer and does not demonstrate an earlier implementation change.

## Required lineage table

Statuses below apply to the stated edge, not to every claim in the source. `EXACT_LINEAGE` records an equation/code continuity; `DOCUMENTED_DESIGN` records an explicit design statement, not proof that it is correct. `STRUCTURAL_CONNECTION` is a genuine relationship without an established causal derivation. `COINCIDENCE_ONLY` means numerical resemblance supplies no demonstrated derivation. `AUTHOR_RECOLLECTION` and `OPEN` preserve the remaining evidence limits.

| SOURCE | DATE | EQUATION | ROLE_OF_3 | PROVENANCE_STATUS | RELATION_TO_CURRENT_HARMONIC_3 |
|---|---|---|---|---|---|
| S28 DMQPF pp. 1–2 | Title: 2025-02-09 | `P(θ)=4r abs(θ)`; wavelength terms including de Broglie λ | No three-channel phase law in these formulas | STRUCTURAL_CONNECTION | Documents angular/perimeter and wave vocabulary; no edge to pairwise H3 recovered. |
| S22 Bounded Infinity | Title: 2025-10-16 | `(Ax⁴−Bx²+C)/(x⁴−Bx²+A)` | Constant comparisons and geometric interpretation | STRUCTURAL_CONNECTION | Historical context only; no paired H3 formula established. |
| S29 E8/SU3 geometry §6, p. 8 | Title: 2025-10-29 | `R(A,B,C)=9`; `8+1=9` | Threeway/nine-fold closure interpretation | DOCUMENTED_DESIGN | Documents use of three/nine concepts; does not derive phase multiplier three. |
| S21 reciprocal-asymmetry pp. 3–9 | Title: 2025-11-05 | `θ(a,b)=abs(a/b−b/a)/sqrt(ab)` | A selected triple of constant pairs | STRUCTURAL_CONNECTION | Gives context for three-stage choices; arithmetic and scale claims need corrections. |
| S21 near-twelfth claim | Title: 2025-11-05 | `θ(sqrt3,φ)≈1/12`, unequal | Numerical near match to twelve | COINCIDENCE_ONLY | No proven rule converting this proximity into harmonic three. This status concerns the proposed provenance edge. |
| S27 Appendix C pp. 24–25 | Title: 2025-11-05 | `ϑ_k=ϑ_0+πk/12`; offsets `8j` | Three 120° orientations on a 24-node, 15° lattice | STRUCTURAL_CONNECTION | Real angular scaffold; printed arms/counts/weights are inconsistent. No forced H3 law. |
| S16 water p. 17; S17–S19 code | Paper title: 2025-11-20; code date not independently established | `(κ_Tri/3)Σ sin(θ_j−θ_k)`; code uses κ sum | THREE phases averaged, harmonic ONE | DOCUMENTED_DESIGN | Positive earlier m=1 evidence in a related model; direct transition to H3 remains unproved. |
| S20 Emergent Z p. 7 | Title: 2025-11-21; metadata same day | `V0[1−cos(3(φ−φ0))]` | Threefold single-orientation potential | DOCUMENTED_DESIGN | Earliest recovered orientation-potential precursor here; not both target formulas. |
| S20 pp. 8–9 | Title: 2025-11-21 | `Z=H sin(3ϕ)`; bands 0.3/0.6/0.9 | Triple-periodic height and chosen bands | STRUCTURAL_CONNECTION | Documentary support for these motifs; no explicit derivation of later pairwise interaction. |
| S30/S31 early phase-locking papers | Titles: 2025-11-30 / 2025-12-02 | Coupled three-component recursion | Three nodes; graph/amplitude dynamics | STRUCTURAL_CONNECTION | Phase-locking terminology predates the separate H3 stage and cannot identify its harmonic. |
| S34–S38 V1/V2/V3.1/V3.3/V3.4 code | Archive versions; V3.3 core member stamp 2025-11-29; V3.4 core 2025-12-09 | Cubic amplitude plus graph update; separate scalar `cos(3θ)` readout | Node count and scalar readout harmonic | EXACT_LINEAGE | Recovered earlier core formula lacks added phase synchronizer. Archive stamps are not proof of first authorship. |
| S15 release catalog, lines 654–713 | v3.9 release label; no independent live date verified | Describes introduction of phase-triad synchronization | Three-phase structural selector | DOCUMENTED_DESIGN | Explicit release-level introduction claim supports the extension history. |
| S14 pp. 2–3 | Title: December 2025; PDF build 2025-12-29 19:19:09Z | `Σ sin(3d)` and `(1/3)Σ exp(i3φ)` | Harmonic three plus separate count normalization | EXACT_LINEAGE | Earliest recovered paired documentary formulas; preserved later. |
| S14 §11 p. 5 | Same document | `V=−λ/2 Σ_(k≠j) cos(3(φ_j−φ_k))` | Assumed local `φ_k ~ φ_k+2π/3` and lowest allowed Fourier mode | DOCUMENTED_DESIGN | Records a claimed derivation; local identification is not supplied by mere channel symmetry, and printed gradient lacks factor 3. |
| S32/S33 later patch/v4 papers | Titles: 2026-01-02 / 2026-01-11 | Triad coherence and enabled phase synchronization | Adopted H3 organization | EXACT_LINEAGE | Later use confirms persistence, not an earlier origin. |
| S13 TORMENT Git addition | Commit author date: 2026-03-08 12:44:05Z | Both target expressions in added file | H3 drift and coherence | EXACT_LINEAGE | Earliest recovered code commit for both. Copy-in, not a derivation commit. |
| S08 old kernel; S39/S40 quantum lineage | Old working copy undated; quantum tracked snapshot 2026-08-06 | Both target expressions | Same H3 implementation | EXACT_LINEAGE | Byte/formula continuity of recovered copies; no earlier design discussion recovered. |
| S12 identity map | Recovered snapshot, origin date unresolved | Stage/sign-derived index modulo 9 | Nine semantic labels | STRUCTURAL_CONNECTION | Nine-form identity space is documented; not a proof of the H3 Fourier index. |
| S03/S01 current Paper A and dynamics | Frozen current baseline, verified 2026-09-29 | Adopted H3 phase stage in a three-state map | Model coefficient and count | EXACT_LINEAGE | Current mathematical and implementation authority. Covering construction does not select harmonic three. |
| S05–S07 Phase Bridges II/III | Manuscripts: 2026-09-21 | Phase model for integer harmonic m; m=3 consequences | Deliberately chosen harmonic | STRUCTURAL_CONNECTION | Explicitly geometry does not force 3; use review/Bridge III corrections for equilibrium claims. |
| S04 Paper F eq. (3), line 51 | Frozen current baseline | Adopted `H_j=Σ sin(3(p_l−p_j))` | Adopted parameter of the model | EXACT_LINEAGE | Explicitly leaves historical selection unexplained. |
| Author recollection in work order | Received 2026-09-29 | 0/15/30/45°, reciprocal comparisons, nine forms, .3/.6/.9, 3×4=12, D24, DMQPF, closed waves | Historical motivation recalled by author | AUTHOR_RECOLLECTION | Some motifs now have documentary instances above; their causal route to this pair of H3 formulas remains recollection. |
| Missing decision/derivation edge | Undated, unrecovered | From old geometric motivations or water m=1 to pairwise m=3 plus coherence | Why THIS harmonic and THIS phase variable? | OPEN | Do not fill with later mathematical compatibility or a reconstructed story. |

## What the claimed derivation does and does not prove

On a smooth nonzero phase chart, define `d_jk=φ_j−φ_k`. Common phase rotation leaves `sin(m d_jk)` unchanged for **every integer m**, and relabelling identical channels also preserves the form for every m. Three nodes alone do not distinguish m=1, m=2, or m=3.

If one additionally imposes **independent** identifications `φ_k ~ φ_k+2π/3`, a pair potential must be periodic with period `2π/3` in its difference argument. Its Fourier modes then have indices divisible by three. Choosing an even potential and retaining its lowest nonconstant mode gives `cos(3d)`. Higher modes and combinations remain possible. This is a conditional design argument, not unique selection by the original node geometry.

Moreover, the full complex kernel's graph term is generally not invariant under independent 120° rephasing of each channel. Equating a triangle's orientation modulo 120° with each complex channel phase requires an additional modelling map. No recovered source supplies a sound complete derivation of that map and the exact chosen interaction. The earlier one-variable orientation potential in S20 is relevant documentary context, but an explicit source connecting its variable and dynamics to the later pairwise Ω-channel operator is still missing.

For the potential printed in S14,

`V = −(λ/2) Σ_(k≠j) cos(3(φ_j−φ_k)) = −λ Σ_(j<k) cos(3(φ_j−φ_k))`,

direct differentiation gives

`−∂V/∂φ_k = 3λ Σ_(j≠k) sin(3(φ_j−φ_k))`.

Its equation (12) prints λ rather than 3λ. Reparameterizing λ could build a consistent different presentation, but doing so would repair the source and is not done here.

## Search coverage and reproducibility limits

The bounded search covered the current authority, the old kernel, copied TORMENT kernel lineage and its available Git history, the related quantum-kernel snapshot, local patch/release notes, old tests and current parity tests, old PDFs, and consolidated research sources. All 126 distinct PDF contents under the consolidated research source tree were extracted after SHA-256 deduplication; no extraction errors were recorded. An additional old-PDF index covered 41 files plus the separately targeted water and Bounded Infinity PDFs. These overlapping collections are not added as a unique-total count. Formula text extraction was supplemented with rendered-page inspection for the decisive v3.9 equations/derivation, water equation, reciprocal proof, Bounded Infinity figure labels, and D24 appendix/figure.

Searches included code/text forms of third-harmonic sine and complex exponentials, synchronization/coherence names, patch introduction descriptions, and earlier core implementations. A PDF text search can miss graphical or unusual glyph content; a negative search is bounded by this accessible corpus. No claim is made that all original conversations, private backups or released files survive locally.

Archive reading used stdout/in-memory access, without extracting into a source tree. Every Python member in V1.0 (18), V2.0 (21), and V3.1 (28) RAR archives was readable and screened; their core update bodies were inspected. V3.3 (30 Python files) and V3.4 (33 Python files) ZIP contents and core bodies were inspected. No separate target H3 operator was found in these snapshots. The ZIP member timestamps provide weak chronology only. Later intermediate releases are represented by research/patch records, not a recovered complete set of source archives. A local `18285147.zip` was checked and contains TGMO/REFU files, not a missing phase-triad kernel release.

Git checks used local reachable history with optional locks disabled. Current repo: 38 reachable commits; production checkout: 1,881; both non-shallow. The TORMENT phase-sync file history contains its March 8 addition and a March 10 line-ending change (`c951613424f8a7e7326dc3a5bebfdf563773be5c`). The two versions normalize to the same LF text. Their raw byte SHA-256 values are:

| Snapshot | Raw file bytes | SHA-256 |
|---|---:|---|
| March 8 Git blob | 1241 | `ab255edefdfe96b38931a910cc7ec8a757395069f67bf1b75b78a9e00370d2f3` |
| March 10/current production file; old copy | 1281 | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` |

The related quantum repository's tracked `kernel/phase_triad_sync.py` and experiment file first appear in snapshot commit `fced22e6984c1fe140a75cfc87af45aff63f45e8`, dated 2026-08-06T18:58:39Z. That is later than the TORMENT attestation. Filesystem copy dates and bytecode timestamps were not treated as creation dates. Old kernel_TO itself supplies a working-tree snapshot, not a recovered earlier edit history.

Tests document current behavior, not origin: S41 includes amplitude preservation and simultaneous update checks; S42 includes independent parity of the adopted phase map; S43 covers Paper F geometry/analytic identities. Tests were read, not executed. A third-harmonic test of the separate scalar `z(θ)` readout must not be mistaken for proof of phase-coupling provenance. The experiment harness's dummy main likewise cannot validate a historical scientific run.

Attempts to verify the release date through live public record access did not produce usable primary metadata. Public record identifiers from the local catalog were retained as historical labels only. No live publication priority is asserted.

## Source register

Each digest below fingerprints the cited local bytes. A hash identifies a recovered artifact; it does not authenticate its claimed date or scientific assertions.

| ID | Exact local artifact | SHA-256 |
|---|---|---|
| S01 | [dynamics.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py>) | `ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4` |
| S02 | [readouts.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py>) | `3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9` |
| S03 | [paper_A_publication.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_A/publication/paper_A_publication.md>) | `5fc388072d344c10d201b8eff255226b861014ff980e64c06811ae973bf7cd55` |
| S04 | [PAPER_F_PUBLICATION_v0.2.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md>) | `8c9419b20a0899857e68f4b191e7321cfc99f5286f149504f5d82a3e75db4fd5` |
| S05 | [PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/phase_bridge_II/PHASE_BRIDGE_II_HAMILTONIAN_DYNAMICS.md>) | `e9bc4cf19d5292aa26e69095a75f9f7a64280b11292e8e33d2020a3f03e47b57` |
| S06 | [PHASE_BRIDGE_II_CODEX_REVIEW.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/phase_bridge_II/PHASE_BRIDGE_II_CODEX_REVIEW.md>) | `fab671ec7321d3e2cfe8aca99e96bfeabe32873f0711ec91e87ea40494646380` |
| S07 | [PHASE_BRIDGE_III_RECURSIVE_TIME_ACTION_ANGLE.md](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/phase_bridge_III/PHASE_BRIDGE_III_RECURSIVE_TIME_ACTION_ANGLE.md>) | `d19178a45b44f422a0f9f5c38494c79778914be846f3e2eddb118e29baa68f95` |
| S08 | [phase_triad_sync.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/phase_triad_sync.py>) | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` |
| S09 | [phase_triad_experiment.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/phase_triad_experiment.py>) | `03b46cc00c3f98c1ded5a3f6588f218fd60329f31959845de438230723e47033` |
| S10 | [model_core.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/model_core.py>) | `ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6` |
| S11 | [constants_selector.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/constants_selector.py>) | `80d8825691079bfb10151a94b243dd9757fb4fe5759aa5fde85dba09e9ba7edf` |
| S12 | [identity_rules.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/identity_rules.py>) | `889eb7e759aabbc509a852094cdf778e164e02c9a82a0a55a47b269f60bea751` |
| S13 | [phase_triad_sync.py](<C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel/phase_triad_sync.py>) | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` |
| S14 | [v3_9_Phase__Triad_Synchronization_and_Collective_Orientation-1.pdf](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/18089089/v3_9_Phase__Triad_Synchronization_and_Collective_Orientation-1.pdf>) | `042ae3f32a695f50bb2f6cfc499dd679c7bc55eadc556432ea0582ce4fc823b5` |
| S15 | [List_tri_octagon_Model.txt](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/List_tri_octagon_Model.txt>) | `637635df703a5b1248c631584d4db390382ee28e0361c4376252d9a31d67c306` |
| S16 | [recursive_water.pdf](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17666655/recursive_water.pdf>) | `4bc94970b2ec68b12e65894908af949d5701258d55e0bd8f75b3fe29548b9357` |
| S17 | [variant_1.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17666655/variant_1.py>) | `be8950b8a150439493a214fef32aa5dcbcb1a022de94a9f318bd21118138e8c3` |
| S18 | [variant_2.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17666655/variant_2.py>) | `68477c053f1d6e17da67e51845bfcf401e3a3d4bdb12578f896ce9b095a098d6` |
| S19 | [polarity_over_time.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17666655/polarity_over_time.py>) | `9e1d8bba436fd2183424e5810baf6f2f226232eee7963f8a2403b5a10b625e5f` |
| S20 | [Emergent_Z.pdf](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17666655/Emergent_Z.pdf>) | `a00e6cea7dda2b9e2718878ed5474775f9ca464fbea7f1085cc5ba01bd33d061` |
| S21 | [Scale_Invariant Reciprocal_Asymmetry.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/Scale_Invariant Reciprocal_Asymmetry.pdf>) | `b6cd62bc9c7cf69b20ea44ab208272592e09a0ef3c36df97b36cad4559a0b97b` |
| S22 | [Bounded_Infinity.pdf](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17365334/Bounded_Infinity.pdf>) | `86ecdf9698e384ff5465591c145633f69f76554ac27d0fa034e4db84e9cedaf0` |
| S23 | [rrm_tool.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17365334/rrm_tool.py>) | `9ad50ef6566e7dc39671eb1f1d4d325cd158f707b6f70babc6aff9a55d2ea704` |
| S24 | [rrm_asymptotes.csv](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17365334/rrm_asymptotes.csv>) | `6605be2e31d49b768f6753e0a7825102feba2bf2ec87efa620aa88e0d89e4157` |
| S25 | [rrm_arclengths.csv](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17365334/rrm_arclengths.csv>) | `6e98a50447edbed5f51764ddf43ca48a31968f9d83ef58cc87188ffbcd0c8747` |
| S26 | [rtm_key_pairs.csv](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/17365334/rtm_key_pairs.csv>) | `53fadcea293490e80b142802add869ac4d007f26fbaaa18e5d8cfafad53ed3c6` |
| S27 | [TriOctagon_D24-CP-Octant-Ridge.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOctagon_D24-CP-Octant-Ridge.pdf>) | `b340663e298eb6932a1be35ea1b7ced69edc29e6a72991c3df4c49e9d7b3edae` |
| S28 | [DMQPF.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/DMQPF.pdf>) | `f5bb122492cc071b936ccc4563c57e2ff7088c394536b0f7cea11b08317c4050` |
| S29 | [TriOctagon_E8-SU3-Geometry.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOctagon_E8-SU3-Geometry.pdf>) | `851d69441a227fc9015e5581c395fa5743d6ced3125ba956a7c61689bf6a3ba4` |
| S30 | [phaselocking.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/phaselocking.pdf>) | `51c297c71b624bd4b4182274e8cdd101081b72cf9db88d977fc552b293efa840` |
| S31 | [Patch_2.0_Phase_Locking.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/Patch_2.0_Phase_Locking.pdf>) | `1297116090f0c6eaa29007a7bf81b98f4afd234254747f7a74717fa2ad82cf30` |
| S32 | [v3_9_2Phase__Triad_Synchronization_and_Collective_Orientation.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/v3_9_2Phase__Triad_Synchronization_and_Collective_Orientation.pdf>) | `d75b75ef522d6d79dbe16f62e6057bb32b01df41aa559ec390243d544f4e9c18` |
| S33 | [TriOcta_v4.0.pdf](<C:/TORMENT/TRIOCTAGON_new/pdfs_old/TriOcta_v4.0.pdf>) | `e9aa47ce4f763f21ecc3960dc10043cc4d1110ef374205a135441a1c40ed6432` |
| S34 | [V1.0.rar](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17787877/V1.0.rar>) | `436765b7841186de598e3b8ab82118090d09daba3d6ef69b46f8f3ad371335d6` |
| S35 | [V2.0_Toy_Model.rar](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17787877/V2.0_Toy_Model.rar>) | `11ca2742943f25caabe5ae73104421ed4546c891b7ca7ffadc225597c578fe84` |
| S36 | [V3.1_Toy_Model.rar](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17837658/V3.1_Toy_Model.rar>) | `20007ad9bdeb864dd0e81699571738cc2e9f6adaf1646d63d040b47acb316d80` |
| S37 | [V3.3_Toy_Model.zip](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17849619/V3.3_Toy_Model.zip>) | `17a7a84a55b6b7b50f7f6614ede4e486bf40fd76aff463c7bb70268a8085a19c` |
| S38 | [V3.4_Toy_Model.zip](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research_files/sources/Zenodo_research/tri_octagon_Model/17879084/V3.4_Toy_Model.zip>) | `fdce0b00ae31f16dd7baca9eef6aca333d85ed3626554c4ffae388fe6e843685` |
| S39 | [phase_triad_sync.py](<C:/TORMENT/quantum_kernel/kernel/phase_triad_sync.py>) | `15e94505696f409fe82da24cd7e830a7b8ecfc25cc4cbdc264f4c1c05702aea6` |
| S40 | [phase_triad_sync.py](<C:/TORMENT/quantum_kernel/historical/zenodo_v4_original/phase_triad_sync.py>) | `ab255edefdfe96b38931a910cc7ec8a757395069f67bf1b75b78a9e00370d2f3` |
| S41 | [test_dynamics.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_dynamics.py>) | `9acbc542dd91438dc7896d784dc6837e17223568a91a9b2d4178daeb2bd55caa` |
| S42 | [test_parity_p01_p04.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_parity_p01_p04.py>) | `65f0cf0ba95b52bd7e1857c7418cfc0becb66ab1ba301599182f7249e8b67f0d` |
| S43 | [test_parity_p07_p08.py](<C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_parity_p07_p08.py>) | `7e958943f73cb4358f0094c1972303c9a91ed44bb99527b73557783ea896fec4` |
| S44 | [run_patch39_unified.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/run_patch39_unified.py>) | `811dab67ad515a8c03ada843fb489c6a9e19a5b77988680eef5d040e9708bfca` |
| S45 | [seed_emission.py](<C:/TORMENT/TRIOCTAGON_new/kernel_TO/seed_emission.py>) | `c4b97f833c1192d03d00e992717ef4c4c49dd5f590326089c6ee57019877ef66` |


## Disposition

The observable/formula lineage is substantially recovered. The historical selection of harmonic three remains **OPEN**. No paper, code, release record, test or production file was patched. See the companion closeout for before/after integrity and the correction queue for record-only findings.
