# Tri-Octagon Physics v0.1.0 — release candidate and draft notes

**Research/developer preview candidate.** This tracked draft is not a published
GitHub Release. The owner-approved content disposition is recorded in
[PUBLIC_RELEASE_CONTENT_DISPOSITION_v0.1.md](PUBLIC_RELEASE_CONTENT_DISPOSITION_v0.1.md).

## Candidate identity and intentional kernel/UI pairing

Repository candidate commit = **FINAL_HEAD of this release-preparation task**.
Resolve its literal Git identity from the approved candidate checkout:

```powershell
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

The task closeout records the literal FINAL_HEAD and matching origin/main after
the commit/push and CI checks. A commit cannot contain its own literal hash;
this document therefore uses that Git-resolved identity, not a fabricated hash
or a self-updating second commit. Before tagging, compare it with the approved
closeout and the CI run head SHA. Once the tag exists, `git rev-parse v0.1.0^{commit}`
identifies the release independently of later changes on main.

| Identity | Value |
|---|---|
| Repository release | v0.1.0 candidate |
| Repository/UI source | Final approved candidate commit, resolved above |
| Kernel distribution name | trioctagon-physics |
| Kernel package version | 0.1.0 |
| Python import | kernel_physics |
| Public API | 1.0.0 |
| RunRecord schema | 1.0.0 |
| GeometryRecord schema | 1.0.0 |
| Scientific UI distribution | trioctagon-scientific-ui |
| UI version | 0.1.0 |
| UI request/response contract | 2 |
| Kernel artifact lock | 2 |
| UI selected kernel source | **7b3a0fcec2c9bde6c9e1ea482fe1f1ea6b16793e** |

The UI uses the unchanged [kernel artifact lock](apps/scientific_ui/kernel-artifact.lock.json),
including its exact approved source, canonical origin, mandatory manifest,
stable member hashes and RECORD-equivalence rules. Its preferred existing K3
archive hash is recorded in that lock; reconstructed ZIP hashes can differ only
within its strict equivalence contract. No final release-asset hash is invented here.

The repository's standalone kernel build attests the candidate commit. It must
**not replace the older locked kernel in the UI environment** without a separate
lock-update/recertification task. Identical package version or runtime source bytes
do not erase that provenance distinction. Release assets, if authorized later,
must state their source identity and actual SHA-256; do not publish ambiguous
different kernels under the same wheel filename or replace published bytes in place.

## Papers included

| Paper | Canonical publication edition |
|---|---|
| A — v1.0 | [Cycle-Covering Dynamics](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf) |
| B — v0.1.2 | [Triadic Chirality and Orientation Geometry](papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.pdf) |
| C — v1.0.1 | [Exact Folded Tri-Octagon Geometry](papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.1.pdf) |
| D — v0.1.1 | [Reference-Scaffold Geometry](papers/PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf) |
| E — v0.1.1 | [Z Manifold](papers/PAPER_E/v0.1.1/publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf) |
| F — v0.2 | [Transverse Chirality and Local Linearization](papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.pdf) |

E and F are owner-authorized for public visibility/publication in this preview at
their currently recorded scientific/review status. Their historical evidence and
predecessor editions are retained. No additional review round or external peer
review is claimed. Paper editions are separate from package/API/schema versions.

## Draft release notes

Includes Papers A–F, the certified mathematical kernel, companion scientific UI,
reproducible records, exact geometry tools, complex triad/ring dynamics, graph
coverings, chirality/orientation mathematics, passive observers/diagnostics and
local transverse-chirality analysis. See the [public entry points](README.md).

**Certified platform:** Windows x86-64 / CPython >=3.11,<3.12. Other operating
systems and Python versions are NOT CERTIFIED BY v0.1.0. No GPU, LLM or embedding
model is required. Normal installed runtime is offline; source/dependency
acquisition is a separate network-enabled phase.

**Known issue:** numeric sliders may react to mouse-wheel events and replace a
precisely typed parameter value with a slider tick value. Before Run, verify the
visible/resolved request values. Completed records remain immutable and retain
the values actually used. This accepted preview issue is an input-integrity risk,
not harmless behavior; it is not fixed by this release-preparation task.

**Scientific scope:** a mathematical toy model and numerical research, not an
experimentally validated physical theory. No physical shell field, gravity or
electromagnetic/magnetism theory, teleportation mechanism, dark-matter explanation,
physical energy law, geometry↔dynamics physical coupling, Z↔six-opening spatial
registration or host/gap causal dynamics is established. No new speculative
research lane is part of this release.

**Licenses:** Apache-2.0 covers only the approved [kernel software scope](LICENSE_SCOPE.md)
and separate [UI software scope](apps/scientific_ui/LICENSE_SCOPE.md). Papers,
research, figures, datasets and other excluded scientific material are not
automatically Apache-2.0 licensed. Public visibility adds no blanket grant.
Dependencies retain the licenses described in [third-party notices](apps/scientific_ui/THIRD_PARTY_NOTICES.md).

## Validation and remaining publication actions

Read the [kernel distribution workflow](.github/workflows/kernel-distribution.yml)
and [UI certification workflow](.github/workflows/scientific-ui.yml) against the
candidate's exact SHA. The final task closeout records local checks and resulting
remote run IDs/results. Earlier certificates are evidence for their own source
identities, not a substitute for the candidate checks. Mathematical parity remains
bounded by the [P1–P12 closeout](kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md).

The public UI path supports strict reconstruction when GitHub CLI/authentication
or Actions artifacts are unavailable. Corrupt received evidence remains fatal.
The acquisition output selects the actual verified kernel; the
[UI guide](apps/scientific_ui/README.md#public-installation) uses that selection.

**ANONYMOUS_PUBLIC_GITHUB_ACCESS_VERIFIED = NO** while the repository is private.
Local fallback/certification cannot prove anonymous access to the private GitHub
endpoint. After owner review of the final candidate, the external sequence is:

1. Change repository visibility to PUBLIC under separate authorization.
2. Verify anonymous clone and paper/source access.
3. Perform the documented UI acquisition/install smoke against the public endpoint,
   without GitHub credentials or a retained Actions artifact; inspect a small triad record.
4. Create the v0.1.0 tag/release from the approved candidate if authorized.
5. Publish the approved notes and selected assets with actual hashes if authorized.
6. Announce only after those checks and publication actions succeed.

No installer, PyPI publication, DOI, new research license or historical-science
implementation is required for this preview. This draft performs none of the
external publication actions.
