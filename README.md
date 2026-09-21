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
