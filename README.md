# Tri-Octagon Physics

**v0.1.0 research/developer preview candidate**, by Hilmir Frímann Halldórsson.
A mathematical-physics toy model with exact folded Tri-Octagon geometry,
nonlinear complex triad/cycle dynamics, graph coverings and invariant sectors,
chirality/orientation geometry, an exact reference scaffold, passive
observer/readout constructions, and local transverse-chirality analysis.
An executable Python kernel, reproducible scientific records and a companion
scientific UI connect the mathematics to explicit numerical experiments.
This is **not the TORMENT production memory system**.

- **[SCIENTIFIC DOMAINS](scientific_domains/README.md)** - current core, historical TORMENT and experimental Research Lab ownership and authority.
- **[READ THE RESEARCH](#papers-a-f)** — six current publication editions below.
- **[MATHEMATICAL ATLAS](research/mathematical_atlas/README.md)** — first-principles derivations, exact checks, counterexamples, scope boundaries and open interfaces for the current kernel mathematics.
- **[USE THE PYTHON KERNEL](#use-the-python-kernel)** — build, install and save a small explicit experiment.
- **[RUN THE SCIENTIFIC UI](apps/scientific_ui/README.md#public-installation)** — install the separately certified, locked kernel/UI pair.

**Scientific boundary:** this preview is not an experimentally validated physical
theory. It establishes no physical field attached to the shell, gravity theory,
electromagnetic/magnetism theory, teleportation mechanism, dark-matter explanation,
physical energy law, geometry↔dynamics physical coupling, Z↔six-opening spatial
registration, or host/gap causal dynamics. Mathematical identities, numerical
evidence and open physical interfaces remain distinct.

## Papers A-F

These are the authoritative publication editions for this preview. Earlier
editions remain available as historical/superseded research; mathematical source
versions and publication editions need not have the same number.

| Paper | Current publication PDF | Source / recorded status |
|---|---|---|
| A — v1.0 | [Cycle-Covering Dynamics of a Three-State Nonlinear Kernel](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf) | [Publication source](papers/PAPER_A/publication/paper_A_publication.md); scientific source v0.5.1. |
| B — v0.1.2 | [Triadic Chirality and Orientation Geometry](papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.pdf) | [Edition and evidence](papers/PAPER_B/publication/v0.1.2/README.md); scope/citation revision. |
| C — v1.0.1 | [Exact Geometry of the Folded Tri-Octagon Module](papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.1.pdf) | [Edition and evidence](papers/PAPER_C/publication/v1.0.1/README.md); scientific source v0.3.1. |
| D — v0.1.1 | [Tri-Octagon Reference-Scaffold Geometry](papers/PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf) | [Edition and scoped acceptance](papers/PAPER_D/v0.1.1/README.md). |
| E — v0.1.1 | [The Tri-Octagon Z Manifold](papers/PAPER_E/v0.1.1/publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf) | [Recorded review/revision status](papers/PAPER_E/v0.1.1/README.md); owner-authorized for this preview at that status. |
| F — v0.2 | [Transverse Chirality, Dihedral Harmonic Selection, and Local Linearization](papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.pdf) | [Accepted scientific source and publication-build status](papers/PAPER_F/README.md); owner-authorized for this preview at that status. |

- [Kernel history and comparison — v0.1](papers/KERNEL_HISTORY_AND_COMPARISON/README.md)

The [owner publication disposition](PUBLIC_RELEASE_CONTENT_DISPOSITION_v0.1.md)
authorizes E/F public visibility/publication at their currently recorded
scientific/review status. It supersedes earlier owner-authorization-pending
notices without inventing another review round. No external peer review is claimed.

## Licensing and reuse

**Apache-2.0 applies to the approved software scope** described by the root
[LICENSE_SCOPE.md](LICENSE_SCOPE.md) and separate
[UI LICENSE_SCOPE.md](apps/scientific_ui/LICENSE_SCOPE.md).
Papers, research, figures, datasets, historical scientific material and other
excluded scientific content are **not automatically Apache-2.0 licensed**.
Public repository visibility does not broaden those rights.

Read the [software LICENSE](LICENSE), [UI LICENSE](apps/scientific_ui/LICENSE),
and [third-party notices](apps/scientific_ui/THIRD_PARTY_NOTICES.md).
Dependencies retain their own licenses; the original application wheel does not
bundle the kernel, Qt or other dependency binaries. Software is supplied without
warranty under its applicable license.

## Supported platform and runtime

The certified lane is **Windows x86-64, CPython >=3.11,<3.12**.
Other operating systems and Python versions may work but are **NOT CERTIFIED BY
v0.1.0**. No GPU, LLM or embedding model is required. Normal installed runtime is
offline; acquiring source and dependencies initially requires network access or
an existing verified cache. Git is needed for source builds, not installed runtime.

Only the declared [public API](kernel_physics/api.py) and documented workflows are
supported. Internal modules and historical research are not a promise of a stable
API. The UI uses its own exact kernel selection; **do not install the root kernel
from this quickstart into the UI environment**. See the
[release identity and draft notes](RELEASE_v0.1.0.md) for that intentional pairing.

## Use the Python kernel

The distribution is **trioctagon-physics**; imports use **kernel_physics**.
No PyPI publication is required or assumed. Install Git and a clean Windows
CPython 3.11 x64 interpreter with the `py` launcher. In PowerShell, from a directory
where you want the checkout, run:

```powershell
git clone https://github.com/pzychozen/trioctagon-physics
Set-Location trioctagon-physics
$source = (Get-Location).Path
$work = Join-Path $env:TEMP ('tri-kernel-' + [guid]::NewGuid().ToString('N').Substring(0,8))
py -3.11 -m venv $work
$kernelPython = Join-Path $work 'Scripts/python.exe'
& $kernelPython -I -B -m pip --isolated install setuptools==81.0.0 wheel==0.47.0 -r "$source/kernel_physics/requirements.txt"
& $kernelPython -I -B -m pip --isolated wheel --no-index --no-deps --no-build-isolation --wheel-dir "$work/dist" $source
& $kernelPython -I -B -m pip --isolated install --no-index --no-deps "$work/dist/trioctagon_physics-0.1.0-py3-none-any.whl"
& $kernelPython -I -B -m pip check
Set-Location $work
```

Use a clean complete checkout and keep build outputs outside it. The exact origin
URL spelling above (without `.git`) matches the canonical CI/reconstruction origin;
origin spelling is part of strict distribution provenance. Changing it can change
the manifest identity even when source bytes match. After a release tag exists,
check out the approved tag before building for that release. Until then, the
candidate commit is identified by the [release document](RELEASE_v0.1.0.md).

Save and inspect a small explicit triad experiment in the same PowerShell session:

```powershell
@'
from pathlib import Path
from kernel_physics.api import Parameters, State, Provenance, run, RunRecord

parameters = Parameters(eps=0.05, g=0.2, phase_strength=0.001, k=(1, 1, 1))
state = State(omega=(0.2+0.3j, -0.4+0.1j, 0.1-0.2j), update_index=0)
source = Provenance(kind="user_supplied", source_id="readme-example",
    source_revision=None, locator="README.md explicit triad example",
    literal_values={"eps": "0.05", "g": "0.2", "phase_strength": "0.001",
        "k": "(1,1,1)", "omega": "(0.2+0.3j,-0.4+0.1j,0.1-0.2j)"},
    notes="Illustrative user choices, not model defaults.")
record = run(state, parameters, topology="triad", updates=3,
    parameter_provenance=source, initialization_provenance=source,
    observers=(), readouts=(), diagnostics=())
path = Path("example.run.json")
path.write_text(record.to_json(), encoding="utf-8")
loaded = RunRecord.from_json(path.read_text(encoding="utf-8"))
assert loaded.to_json() == record.to_json()
print("Source commit:", loaded.data["implementation"]["commit"])
print("Saved:", path.resolve())
'@ | & $kernelPython -I -B -
```

The record stores the parameters, state, samples and implementation identity.
Loading does not run equations. [API/provenance details](kernel_physics/README.md)
and the [distribution verifier](tools/verify_distribution.py) describe strict
record/resume and artifact checks. Historical machine paths in that engineering
reference are provenance, not public setup requirements.

GitHub's **Download ZIP is for reading source/papers**, not a replacement for the
Git checkout or a provenance-bearing kernel sdist. The generated source ZIP lacks
the Git evidence/generated manifest needed for supported builds and record
production. A certified sdist or wheel preserves its own immutable provenance.
Editable installation is outside this preview's contract.

## Run the scientific UI

Follow the [complete UI installation and first-run guide](apps/scientific_ui/README.md#public-installation).
It installs the exact dependency closure and the certified kernel from source
`7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e`, separately from the repository/UI
candidate commit. Missing GitHub CLI/authentication or an unavailable Actions
artifact can fall through to strict source reconstruction. A downloaded artifact
that fails verification remains fatal. While this repository is private, fetching
its source still needs authorized access; anonymous public-endpoint verification
is deferred until visibility changes.

**Known issue:** numeric sliders may react to mouse-wheel events and replace a
precisely typed parameter value with a slider tick value. Before Run, verify the
visible/resolved request values. Completed records remain immutable and retain
the values actually used. This input-integrity issue is accepted for the preview
with disclosure; it is not harmless.

## Certification, attribution and historical navigation

The [P1–P12 parity closeout](kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md) records
bounded mathematical/software parity; it does not establish physical laws.
[Kernel distribution CI](https://github.com/pzychozen/trioctagon-physics/actions/workflows/kernel-distribution.yml)
and [scientific UI CI](https://github.com/pzychozen/trioctagon-physics/actions/workflows/scientific-ui.yml)
must be read against their exact source commit. The release document identifies
the candidate and separately locked kernel. AI assistance/review attribution in
the papers is retained; it is not a claim of external peer review.

For attribution, identify Hilmir Frímann Halldórsson, the software release and
exact commit; cite each paper using its own title and edition above. No DOI or
public registry release is implied.

[CURRENT_STATE.md](CURRENT_STATE.md), [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md),
and the [23 September publication checkpoint](papers/publication_updates/20260923_BC_scope/README.md)
preserve dated handoffs and previous scope. Research directories contain
historical/experimental and sometimes superseded work; their presence does not
promote it into the supported API or establish a physical interpretation.
`tools/verify_archive.py` validates a historical frozen archive baseline and is
**not the current release validation command**; its old checksums can disagree
with later files. Those receipts have not been rewritten to make that command pass.

---

## Historical landing page — 21–23 September 2026

The material below is preserved historical context. Its old environment paths,
test counts, publication status and archive-verification command do not override
the current quickstarts, paper index or owner disposition above.

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
