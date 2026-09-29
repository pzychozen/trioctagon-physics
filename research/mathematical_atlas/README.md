# TRI-OCTAGON MATHEMATICAL ATLAS

A first-principles derivation and verification layer for the current
trioctagon-physics mathematical kernel. The Atlas collects deeper derivations,
exact checks, counterexamples, source correspondence, interpretation boundaries
and open questions.

Publication pass 1R preserves entries 01–05 investigated against current-kernel
baseline `0fa3b582c086e51371e8a784bc3dd145f88cfb2b`. All 16 external scientific
artifacts were copied byte-for-byte against the frozen publication-preflight
SHA-256 inventory. This README provides portable navigation; the preserved
artifacts retain their original prose, equations, classifications, code, results
and local provenance paths.

## Relationship to papers and implementation

[Papers A–F](../../README.md#papers-a-f) remain frozen publication baselines.
Atlas entries do not silently revise those papers. Later companion papers
such as A_1, B_1 and C_1 may be developed from coherent Atlas results after the
current-kernel Atlas is sufficiently complete. This publication pass creates no
companion paper and makes no release or version change.

`kernel_physics` remains unchanged. Atlas verification scripts test or inspect
accepted mathematics; the Atlas does not grant authority to change runtime
behavior. Its recorded correction queue is documentation, not an instruction to
apply corrections. Scientific research remains subject to the existing
[license scope](../../LICENSE_SCOPE.md); public visibility does not automatically
license this material under Apache-2.0.

## Entry index

| Entry | Subject | Status | Preserved scientific report | Checks and recorded results |
|---|---|---|---|---|
| 01 | Complex triad, recurrence, phase synchronizer and chirality | CLOSED | [Closeout](entry_01_complex_triad/TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md) | Documentary closeout; no dedicated checker found in the authorized preflight inventory |
| 02 | Exact C12 → C3 four-sheet covering and Fourier/deck structure | CLOSED | [Source packet](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_3_TO_12_COVERING_SOURCE_PACKET_v0.1.md) | [Checks](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py) · [Recorded results](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_EXACT_RESULTS.json) |
| 03 | Exact folded three-octagon annular geometry | CLOSED | [Source packet](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_FOLDED_GEOMETRY_SOURCE_PACKET_v0.1.md) | [Checks](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_EXACT_CHECKS.py) · [Recorded results](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_EXACT_RESULTS.json) |
| 04 | Tangent-state representation, matched transport and chiral areas | CLOSED | [Source packet](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md) | [Checks](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_EXACT_CHECKS.py) · [Recorded results](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_EXACT_RESULTS.json) |
| 05 | Reference scaffold and alternating-hexagon geometry | CLOSED | [Source packet](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_REFERENCE_SCAFFOLD_SOURCE_PACKET_v0.1.md) | [Checks](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_EXACT_CHECKS.py) · [Recorded results](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_EXACT_RESULTS.json) |

Entry 01 also includes the [harmonic-three provenance ledger](entry_01_complex_triad/TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md)
and [research correction queue](entry_01_complex_triad/TRIOCTAGON_RESEARCH_CORRECTION_QUEUE_v0.1.md).
The [old/new kernel archaeology census](provenance/TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md)
is supporting provenance, not a numbered Atlas entry or an execution certificate.
Future entries will extend this index.

## Open questions and interpretation boundaries

Closed entry status means the bounded investigation is complete; it does not
mean every historical or physical question has been solved.

| Question | Retained status |
|---|---|
| Exact historical selection of harmonic three | OPEN |
| Ω physical point-position law | NOT DEFINED |
| Ω → Paper-D gap/corner-cell attachment | OPEN / UNSPECIFIED |
| Historical D24 → current covering causal lineage | OPEN where a documentary causal map has not been established |

The exact current cycle covering is distinct from an asserted historical causal
lineage. A tangent-state representation is distinct from a physical position
law. The Paper-D reference scaffold is distinct from the Paper-C material shell,
and geometric gap length is distinct from recurrence coupling. The entries
retain their specific assumptions and limits; this navigation page adds no
scientific theorem or physical attachment.

## Verification records and publication reruns

The [manifest](ATLAS_MANIFEST_v0.1.json) binds each copied artifact to its external
source path and preflight hash, records the original baseline and verification
categories, and separately summarizes this publication's reruns.

| Entry | Original recorded predicate total | Passing standalone publication rerun | Historical integrity predicates not rerun |
|---|---:|---:|---:|
| 02 | 58 | 54 | 4 |
| 03 | 84 | 78 | 6 |
| 04 | 71 | 65 | 6 |
| 05 | 68 | 62 | 6 |

These totals contain different kinds of checks: symbolic/exact identities,
finite counterexamples, API/runtime comparisons, source observations and
integrity attestations. They are not interchangeable with pytest test counts.
Atlas 05 separately recorded, and this publication pass reran, **39 tests and
37 subtests** in `kernel_physics/tests/test_reference_scaffold.py`. No unrelated
whole-kernel suite was run for publication. Atlas 01 has documentary hashes and
its existing closeout; no dedicated checker or new parity claim was invented.

The copied Atlas 02–05 scripts ran from their new repository paths using the
`torment` interpreter with `-B`. Rerun JSON files were written outside the
repository, leaving the original recorded JSON unchanged. No historical
temporary integrity directory was attached: Atlas 02 reports `NOT_CHECKED`;
Atlas 03–05 report `NOT_ATTACHED`. The missing predicates are exactly those
optional integrity groups. All remaining predicate names and groups match the
original results, all passed, and consulted source hashes match the original
recorded identities. Original JSON remains the evidence for the original
before/after tree attestations. Publication preservation checks are recorded
separately and do not impersonate those earlier attestations.

The preserved checkers are investigation artifacts with historical local-path,
source and environment assumptions, including inputs outside the public tree.
Atlas 02 explicitly requires the original baseline HEAD. The publication reruns
occurred before committing the additive Atlas changes, while that HEAD still
matched. A later checkout does not automatically satisfy that guard. These
files are not a portable installed-package test suite; reproducing their
original investigation requires the documented matching sources and layout.
Their code and provenance paths have not been rewritten to conceal those limits.

## Atlas-local byte verification

[SHA256SUMS.txt](SHA256SUMS.txt) covers every file beneath this Atlas directory
except that checksum file itself, using sorted repository-relative paths. The
Git commit identifies the checksum file. The set includes this README, the
manifest, [Atlas-local Git attributes](.gitattributes) and all 16 preserved
artifacts. The attributes recognize the preserved CRLF line endings and the
Atlas-05 packet's original Markdown hard break and terminal blank line during
Git whitespace checks. They do not normalize or alter the copied bytes. Newly
authored publication metadata uses LF line endings.

From the repository root, the following Python code verifies both coverage and
bytes using only the standard library; run it with bytecode disabled (`python
-B`) or in an external script:

```python
import hashlib
from pathlib import Path

root = Path.cwd()
atlas = root / "research/mathematical_atlas"
checksum = atlas / "SHA256SUMS.txt"
rows = [line.split("  ", 1) for line in checksum.read_text().splitlines()]
names = [name for digest, name in rows]
files = sorted(p.relative_to(root).as_posix()
               for p in atlas.rglob("*") if p.is_file() and p != checksum)
assert names == files, "Checksum coverage/order mismatch"
for digest, name in rows:
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
print(f"PASS: {len(rows)} Atlas file checksums")
```

The manifest's external-source hashes also allow an independent comparison with
the original local reports where those files are available. No change to the
preserved scientific bytes is needed for repository navigation or verification.

## Historical archive verification note

The repository contains older frozen archive receipts:
[root SHA256SUMS.txt](../../SHA256SUMS.txt),
[archive_manifest.json](../../archive_manifest.json) and
[SOURCE_MANIFEST.md](../../SOURCE_MANIFEST.md).
[tools/verify_archive.py](../../tools/verify_archive.py) checks that historical
snapshot. Later accepted repository files already differ from it; the current
root README records this condition.

At the untouched publication starting baseline, the historical verifier reports
`HASH MISMATCH: CURRENT_STATE.md`. Regenerating current hashes alone would also
conflict with older manifest records for `kernel_physics/README.md` and
`kernel_physics/requirements.txt`. These are pre-existing snapshot differences,
not an Atlas publication failure.

The Mathematical Atlas therefore has its own current manifest and checksum set.
This publication does not rewrite historical archive receipts, alter the
historical verifier or revert accepted files to an earlier snapshot.

```text
VERIFY_ARCHIVE_BASELINE = KNOWN_PREEXISTING_HISTORICAL_BASELINE_FAIL
VERIFY_ARCHIVE_POLICY = HISTORICAL_SNAPSHOT_NOT_CURRENT_RELEASE_GATE
HISTORICAL_ARCHIVE_RECEIPTS_PRESERVED = YES
```
