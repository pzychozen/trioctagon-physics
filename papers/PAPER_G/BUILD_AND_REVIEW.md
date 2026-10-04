# Paper G v0.1 build and review record

**Disposition: COMPLETE LOCAL REVIEW DRAFT — awaiting author/scientific review.**

Prepared on 4 October 2026. This is paper preparation and application-feature design only. No publication, external peer review, DOI, kernel implementation or application implementation is claimed.

## Delivered material

- [Complete 14-page review PDF](publication/PAPER_G_v0.1_LOCAL_REVIEW.pdf) and [editable LaTeX manuscript](source/paper_g.tex).
- Four figures, each supplied as vector PDF and PNG, with [generation source](source/make_figures.py), included inputs, nominal trajectory CSV and [figure provenance receipt](reproducibility/results/figure_record.json).
- [Minimal portable computational supplement](reproducibility/README.md), including actual M2/M3 interval verifiers, exact accepted inputs, final acceptance/correction records and declared I/O adaptations.
- [Claim/source map](CLAIM_SOURCE_MAP.md) distinguishing exact algebra, interval certificates, standard theorem applications and numerical illustrations.
- [Concrete Axial Observables implementation contract](OBSERVATION_IMPLEMENTATION_CONTRACT.md), covering files, signatures, domains, results, errors, numerical policies, source accounting, immutable exports/caches, acceptance tests and installed kernel/UI pairing. It is design only.

The [changed-file inventory](CHANGED_FILES.txt) lists every new package file; [SHA256SUMS.txt](SHA256SUMS.txt) hashes every file other than that checksum file itself.

## Build and visual inspection

The manuscript was built with the existing Tectonic 0.17.0 executable and offline cache. All staging, TeX outputs, cache use, proof replay and page rendering were outside the repository. The build emitted no warnings. The multi-file manuscript uses four included vector figures; no new TeX installation was made.

All **14 pages of the final PDF** were rendered and visually inspected individually, including equations, figure captions, appendices and references. No clipping, overflow, missing glyphs or unresolved references were observed. The final figures show signed odd/even branches, an enlarged late-time Gamma scale, and a capture-panel legend clear of the bars. The numerical onset figure does not claim a certified continuation interval. The [build and visual receipt](publication/build_and_visual_review.json) records source/figure/PDF identities and page-render hashes.

Final PDF SHA-256:

```text
014965972ff248b7f200b332aab04e658eced914ff0304fd4e5d1c5e131d9122
```

Final manuscript source SHA-256:

```text
1d1bb3e77aaf51d9a95afd2285c10a20bba862ffefc70109eb853080ba24aa62
```

The hash identifies the reviewed artifact. Byte-identical PDF rebuilding across different TeX/font installations is not promised.

## Computational verification actually performed

Both the initial preparation replay and a second replay from a **relocated standalone supplement copy** passed. The latter demonstrates that proof execution needs neither the repository's Python packages nor the original Downloads paths. The environment was Python 3.11.15 with mpmath 1.3.0, activated through the existing `torment` conda environment in Command Prompt.

| Check | Result |
|---|---|
| M2 integer interval certificate recomputed | Entire certificate object identical to accepted input |
| Repaired M3 interval verdicts | 28/28 pass |
| M3 supporting exact/rational predicates | 23/23 pass |
| Separate nominal formulation at 130 digits | 2/2 enclosure-membership checks; numerical consistency only |
| Relocated supplement replay | Same results; actual fresh execution |
| New figure trajectory | Only 321 nominal updates, with q300/q301 checked inside accepted enclosures |
| M2 onset figure | Three existing finite observations reused; no long onset runs |

These are verification counts, not counts of independent theorems. See the [initial replay](reproducibility/results/replay_summary.json) and [relocated replay](reproducibility/results/relocated_replay_summary.json). Original proof-script mathematical bodies are retained; the one adapted supporting script is explicitly identified in [ADAPTATIONS.json](reproducibility/ADAPTATIONS.json). This is not a second independent interval engine or formal proof-assistant certification.

The supplement identifies 17 unchanged included authority/input/script files. Twenty relevant existing project-source identities are recorded separately. Syntax checks, manuscript label/citation checks, local deliverable-link checks, figure/source identity checks and final package checksums were also performed; the [validation receipt](reproducibility/results/package_validation.json) gives the counts.

## Preservation and changed-file scope

Baseline and final local HEAD:

```text
64ddea159e0e69888926aa21fa281e42f5dd50b4
```

All **3,226 pre-existing tracked and nonignored untracked files** captured in the preflight snapshot retained their bytes. Tracked and staged diffs remain empty. The only newly authored repository paths are under `papers/PAPER_G/`; all pre-existing untracked work remains present. The inventory distinguishes these new files without treating unrelated existing work as task output.

No current/Historical/production kernel, UI, earlier paper, root README, licensing, release file or scientific input was edited. No scientific kernel runtime, service, database, model or production memory system was invoked. No stage, commit, push, tag or publication was performed. Evidence copies in this package preserve their source bytes and attribution; old pending or superseded statements are governed by the final records, not silently rewritten.

## Scientific boundaries and remaining decisions

The manuscript preserves the squared-norm-three entrance, exact `lambda_c + 1/200`, direct certified **N=301** entry, distinction between an outer image enclosure and the actual image, separate H-symmetry existence argument, and phase-parity summability for one overall rotation of the full limiting cycle. The corrected M2 two-step cycle multiplier is `1 - 4 sigma mu + O(mu^2)`.

M2-to-M3 branch continuation remains unproved and is not required by either theorem. The local M2 theorem supplies no explicit certified positive-mu range. There is no first-entry/global-basin claim, binary64 runtime theorem, lambda=0.5 connection, physical magnetic field validation, X01 adoption or M4 work. Nominal plots are not interval proofs.

No missing controlling M1/M2/repaired-M3 source or new contradiction blocked this draft. The standard contraction theorem was checked in an actual textbook statement; retrieval of Banach's original 1922 text failed, and the [claim map](CLAIM_SOURCE_MAP.md) records that narrow bibliographic limitation. No external literature PDF is redistributed.

Author/scientific manuscript review, redistribution/publication approval, and the contract's explicit numerical/version/pairing decisions remain future decisions. They do not authorize implementation through this delivery. The existing software license scope is unchanged.
