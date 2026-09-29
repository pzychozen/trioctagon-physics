# TriOctagon mathematical atlas — Entry 01 closeout v0.1

Date: 2026-09-29. Work mode: read-only investigation; external documentation only.

**Atlas 01 is closed as a bounded mathematical/source audit, with one explicit unresolved provenance question: why the historical model selected the exact pairwise harmonic-three law. That question remains OPEN.** No scientific, historical or production source was modified.

The main new evidence is the December 2025 v3.9 paper: it contains both `sin(3*(φ_j−φ_k))` and `(1/3)Σ exp(i3φ_k)`, and a section claiming to derive the interaction. The section assumes the crucial local phase identification and has a factor-of-three gradient error. It is documentary evidence of a design rationale, not a sound completed derivation. An earlier November 2025 paper supplies a one-variable threefold orientation potential; the required map from that variable to the later Ω-channel interaction is still unrecovered.

## Authority and deliverables

| Scope | Authoritative path / baseline |
|---|---|
| Current kernel repository | `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`; HEAD `0fa3b582c086e51371e8a784bc3dd145f88cfb2b` |
| Historical tree | `C:\TORMENT\TRIOCTAGON_new\kernel_TO` |
| TORMENT production kernel | `C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric\torment_service\kernel` |
| Additional production integrity scope | Entire enclosing `C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric`; HEAD `a06edcc5c9df5d3b56405085d9f2942b768dc203` |
| Output location | `C:\Users\Notandi\.codex\reports`, outside all protected source trees |

Companion evidence: [TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md>) and [TRIOCTAGON_RESEARCH_CORRECTION_QUEUE_v0.1.md](<C:/Users/Notandi/.codex/reports/TRIOCTAGON_RESEARCH_CORRECTION_QUEUE_v0.1.md>). Their Sxx source references resolve to exact local paths and SHA-256 hashes in the provenance ledger.

## Accepted mathematical account

This summary describes the frozen implementation and source mathematics; it does not replace the papers' hypotheses or claim a fresh full parity certification.

1. **State.** `Ω=x+iy ∈ C³`, with x,y real channel vectors. The component labels are channels; a physical-space interpretation requires a separately specified map.

2. **Linear coupling.** Let `e=(1,1,1)^T`, `P=ee^T/3`, `Q=I−P`. Then `L3=ee^T−3I=−3Q`. It annihilates the common line and acts as −3 on the transverse plane `V=e⊥`. This 3 is the complete triangle graph's nonzero Laplacian magnitude, not a derivation of a Fourier harmonic. Source: S01 line 12 and S04 Proposition 1.

3. **Onsite cubic and ordered update.** The current pre-sync step is

   `Ω̃_i = Ω_i + εΩ_i(k_i−abs(Ω_i)^2) + g(L3Ω)_i`.

   It is a finite polynomial update with real coefficients, followed by the phase stage. It has no added physical clock, forcing/noise variable or historical readout envelope. The cubic amplitude law is not globally stable for arbitrary finite steps merely because a continuous parent has a potential. Source: S01 lines 87–96; S03.

4. **Common/transverse decomposition.** Write `Ω=we+ζ`, `w=e^TΩ/3`, `ζ=QΩ`. The graph part leaves w unchanged and multiplies ζ by `1−3g` when taken as the isolated map `I+gL3`. The onsite nonlinearity and phase step must still be accounted for. For equal k values the common-state manifold is invariant; unequal k generally destroy that restriction. Paper F works with k=(1,1,1), for which `we → [1+ε(1−abs(w)^2)]we` and the unit common-amplitude circle is fixed. These statements are not blanket full-map contraction claims.

5. **Raw chirality.** `C(Ω)=x×y` is unnormalized, with no imposed decay factor (S02). If `x=αe+ξ`, `y=βe+η`, ξ,η∈V, then

   `C=e×(αη−βξ)+ξ×η`.

   The first term is transverse and the second longitudinal. A common complex phase preserves C; complex conjugation changes its sign; a channel permutation P gives `C(PΩ)=det(P)P C(Ω)`. This is a channel pseudovector law, not an automatic physical chirality identification. Plane approach requires the relative synchronization/nonzero-mean hypotheses in Paper F; synchronized approach to zero alone is insufficient.

6. **Paper F basis and local structure.** `u=(1,−1,0)/sqrt2`, `v=(1,1,−2)/sqrt6` are orthonormal in V, with `u×v=e/sqrt3`. For `q(φ)=u cosφ+v sinφ`, `e×q=sqrt3 q(φ+π/2)`. Paper F's seed is `e+ihq(φ)`, with sufficiently small h in its specified local regimes. The square roots normalize integer vectors; they do not supply a historical derivation of phase harmonic three. Source: S04 eqs. (6)–(11), S43.

7. **Current harmonic-three stage.** Set `p=Arg0(Ω̃)`, with the explicit zero convention `Arg0(0)=0`. Simultaneously evaluate

   `H_k(p)=Σ_(j≠k) sin(3(p_j−p_k))`,

   `Ω_k^+ = abs(Ω̃_k) exp(i[p_k+λH_k(p)])`.

   In three nodes the two cyclic neighbors are precisely the other two channels. λ=0 returns the input state by copy without phase reconstruction. For nonzero λ the zero convention is part of the contract; smooth phase-chart symmetry/flow arguments cannot simply be extended through zero amplitudes. The phase substep preserves its input amplitudes, while the whole composed map generally changes them. Source: S01 lines 57–96.

   The historical coherence is `S=(1/3)Σ exp(i3p_k)`, so `H_k=3 Im(S exp(−i3p_k))`. This identity explains what the chosen law does. The factor 1/3 counts channels; the 3 in the exponent selects a harmonic. S is invariant under independent integer 120° shifts of the phases, while a common shift α multiplies S by `exp(i3α)` and preserves its magnitude. These phase-chart facts do not establish why that harmonic was historically selected or confer the same independent phase symmetry on the full graph-coupled Ω map.

## Archaeological conclusion

The recovered sequence has distinct branches that must not be collapsed:

| Evidence stage | Supported conclusion |
|---|---|
| Recursive water, title 20 November 2025 | First-harmonic coupling averaged over three phases; companion code also implements a first-harmonic sum. |
| Emergent Z, title 21 November 2025 | A threefold single-orientation potential and triple-periodic height field already exist as explicit modelling choices. |
| Recovered V1–V3.4 toy-core archives | Cubic amplitude plus graph coupling, without a separate phase synchronizer; an independent scalar cos(3θ) readout already exists. |
| v3.9 paper, December 2025; PDF build metadata 29 December | Both target H3 formulas appear, along with a claimed symmetry derivation whose limitations are recorded. |
| TORMENT commit, 8 March 2026 | Earliest recovered Git code containing both exact target expressions; a copy-in attestation, not an invention date. |
| Current Paper A/dynamics and Paper F | Adopt the later harmonic-three law. Paper F explicitly states that symmetry does not explain its historical selection. |
| Phase Bridge II review and Bridge III | Establish consequences and limitations of the phase model; geometry does not force harmonic three. |

There is no recovered source proving an m=2 phase-synchronizer stage, nor a direct source edit changing water's m=1 into the current m=3. “Earlier implementation” therefore has two evidenced answers: a related water implementation used m=1; earlier recovered toy-core snapshots had no separate phase synchronizer. An m=1 exchange term arising from polar reformulation of graph coupling is a third, mathematically distinct matter.

The author's recalled reciprocal comparisons, nine-form space, 0/15/30/45° reasoning, .3/.6/.9 structures, 3×4=12, D24, DMQPF and closed waves remain valuable leads. Documentary instances now support several motifs, but no complete causal edge from those motifs to the exact pair of H3 formulas was recovered. In particular, nine semantic labels, nine lifted phase branches, three graph channels and a third Fourier harmonic are different constructions.

## Corrections recorded and remaining evidence

The companion queue contains 23 record-only items. Definite calculations include the reciprocal functional's degree −1 scaling and incorrect θ values/ranking; an invalid Fibonacci argument; D24 arms/count/weight mismatches; the lack of real poles for the declared Bounded Infinity parameter pairs; and the missing factor 3 in the v3.9 potential gradient. Artifact conflicts include (9,1) versus (9,9) plot/preset versions. Interpretive and unresolved items are classified separately.

The open provenance question could be narrowed by an original dated v3.9 design conversation, earlier source archive/patch introducing the phase stage, or an explicit document mapping the single triangular orientation variable onto the three complex channel phases and stating the selection assumptions. This is an evidence inventory, not a request to reconstruct or repair that history. No further source changes or investigation are initiated by this closeout.

## Verification and integrity

The investigation used read-only filesystem/Git inspection, in-memory archive reading, PDF text extraction plus rendered-page inspection, and independent arithmetic. The `torment` interpreter was used without importing project modules; a separate available PDF runtime handled PDF extraction/rendering. No scientific simulations, package builds, model tests, Git fetches, commits or pushes were performed. Existing tests were inspected for their scope, not re-run.

Before and after inventories recursively hashed every regular file in each listed root, excluding entries under `.git`. This includes ignored and untracked content and includes the entire production checkout in addition to its kernel. File paths use root-relative POSIX separators. The tree fingerprint is:

`SHA256(UTF8(json.dumps({relative_path: SHA256(file_bytes)}, sort_keys=True, separators=(',', ':'))))`.

Empty directories and filesystem timestamps/ACLs are outside this byte-content fingerprint. Git administrative files are outside it; HEAD and tracked working-tree status were checked separately with optional locks disabled. Current and production HEADs remained as listed above, and tracked status was clean at both checks. Pre-existing untracked artifacts are included in the content inventory; “tracked clean” is not a claim that every checkout had no untracked files.

| Scope | Files before / after | Before SHA-256 | After SHA-256 | Changed paths |
|---|---:|---|---|---:|
| current | 7783 / 7783 | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | `c290755b50b607b9e699bec5d0ca2ff9821def3aece8ee3b2513cad43b1cd880` | 0 |
| old | 401 / 401 | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | `cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd` | 0 |
| torment_kernel | 64 / 64 | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | `8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41` | 0 |
| torment_checkout | 173908 / 173908 | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | `3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4` | 0 |


All inventories have zero added, removed or modified file paths. Full per-file before/after inventories and PDF extraction records are retained in the external scratch evidence directory:

`C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas01_20260929_a6uj_1rq`.

The three deliverables are outside the protected trees. The final attestation is:

```text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
EXACT_HARMONIC3_HISTORICAL_DERIVATION = OPEN
```

STOP. No source correction, parameter change, repository placement, commit or publication follows from this report.
