# Publication checkpoint - 23 September 2026

Latest local publication editions: [Paper B v0.1.2](papers/PAPER_B/publication/v0.1.2/README.md), [Paper C v1.0.1](papers/PAPER_C/publication/v1.0.1/README.md), and [accepted Paper D v0.1.1](papers/PAPER_D/v0.1.1/README.md). [Paper A](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf) is unchanged.

GPT accepted D's stated scientific scope and approved exactly five B/C scope/citation additions. B/C's preexisting mathematical content, coordinates, proofs, equations and figures are retained. C's publication label v1.0.1 is distinct from its preserved scientific manuscript v0.3.1. [Exact changes, checks, preservation and the combined proposed publication allowlist](papers/publication_updates/20260923_BC_scope/README.md) identify this local checkpoint. D's approved PDF was not rebuilt. No staging, commit, push, release, tag or DOI was performed.

Predecessors remain reachable: [B v0.1.1](papers/PAPER_B/publication/v0.1.1/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.1.pdf), [C v1.0](papers/PAPER_C/publication/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf), [D v0.1](papers/PAPER_D/README.md). The original archive manifests are frozen baseline receipts, not manifests of these later publication additions; use the combined checkpoint manifest for the proposed changes.

The publication clarification does not implement a reference-scaffold placement, restore historical Z/torus behavior or define a physical gap response. The current boundary/SRG preparation and face-state option remain as recorded in their existing implementation records. The older snapshot below retains its dated scope and is not a current claim that subsequent implementation/publication work never occurred.

---

## Earlier repository snapshot (preserved)

# Tri-Octagon physics

Mathematical-physics reconstruction of the Tri-Octagon, by Hilmir Frímann Halldórsson.

The aim is a rigorous mathematical toy model with explicit proofs, connections
to established mathematics/physics, an executable physics kernel, and eventually
an interactive visual physics laboratory. This is not the production TORMENT
memory system.

Start with **[CURRENT_STATE.md](CURRENT_STATE.md)**, the primary human/machine handoff.

The three authoritative layers are:

1. [Paper C](papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md): exact folded geometry ([publication PDF](papers/PAPER_C/publication/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf)).
2. [Paper A](papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md): three-state nonlinear dynamics ([publication PDF](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf)).
3. [kernel_physics](kernel_physics/README.md): the clean executable mathematical implementation, with its recorded 41-test baseline.

The current frontier is the **geometry-to-dynamical-state interface**.
The [completed first-bridge study](research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md)
establishes exact structural results and a conditional kinematic complex-space
construction. Three complex dynamical amplitudes have not yet been derived.
No physical coupling between geometry and dynamics is claimed yet.

This repository is a byte-preserved archive/transfer of the current state.
See [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) for origins and hashes, and
[supporting_research/INDEX.md](supporting_research/INDEX.md) for historical sources
kept outside the frozen baseline. Large historical archives are not included.

Verify package bytes without executing research:

```sh
python -B tools/verify_archive.py
```

For kernel tests, follow its README and pinned requirements. Historical test
results are archived as recorded; packaging did not rerun them. The original
bridge script and scientific documents retain their original absolute paths;
see CURRENT_STATE.md before attempting research-script execution on another host.
