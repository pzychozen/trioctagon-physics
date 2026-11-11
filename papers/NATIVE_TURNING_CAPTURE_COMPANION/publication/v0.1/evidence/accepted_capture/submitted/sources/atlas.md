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

Publication pass 2 adds entries 06–09, Supplements A/F and completeness v0.2:
22 further external artifacts copied byte-for-byte. The current-kernel Lane-1
reconstruction is complete at the frozen 75-row K0 scope. This publication
preserves the earlier Pass-1R record and does not begin Lane 2.

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
| 01 | Complex triad, recurrence, phase synchronizer and chirality | DOCUMENTARY_CLOSEOUT | [Closeout](entry_01_complex_triad/TRIOCTAGON_ATLAS_01_CLOSEOUT_v0.1.md) | Documentary closeout; no dedicated checker found in the authorized preflight inventory |
| 02 | Exact C12 → C3 four-sheet covering and Fourier/deck structure | RECORDED_PASS | [Source packet](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_3_TO_12_COVERING_SOURCE_PACKET_v0.1.md) | [Checks](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py) · [Recorded results](entry_02_cycle_covering/TRIOCTAGON_ATLAS_02_EXACT_RESULTS.json); 58 original predicates |
| 03 | Exact folded three-octagon annular geometry | RECORDED_PASS | [Source packet](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_FOLDED_GEOMETRY_SOURCE_PACKET_v0.1.md) | [Checks](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_EXACT_CHECKS.py) · [Recorded results](entry_03_folded_geometry/TRIOCTAGON_ATLAS_03_EXACT_RESULTS.json); 84 original predicates |
| 04 | Tangent-state representation, matched transport and chiral areas | RECORDED_PASS | [Source packet](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md) | [Checks](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_EXACT_CHECKS.py) · [Recorded results](entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_EXACT_RESULTS.json); 71 original predicates |
| 05 | Reference scaffold and alternating-hexagon geometry | RECORDED_PASS | [Source packet](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_REFERENCE_SCAFFOLD_SOURCE_PACKET_v0.1.md) | [Checks](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_EXACT_CHECKS.py) · [Recorded results](entry_05_reference_scaffold/TRIOCTAGON_ATLAS_05_EXACT_RESULTS.json); 68 original predicates |
| 06 | Z observer, clock, staged law and EMA memory | PASS | [Source packet](entry_06_z_observer/TRIOCTAGON_ATLAS_06_Z_OBSERVER_SOURCE_PACKET_v0.1.md) | [Checks](entry_06_z_observer/TRIOCTAGON_ATLAS_06_EXACT_CHECKS.py) · [Recorded results](entry_06_z_observer/TRIOCTAGON_ATLAS_06_EXACT_RESULTS.json); 199 checks |
| 07 | Diagnostics, finite-step accounting and display maps | PASS_WITH_RUNTIME_CAVEAT | [Source packet](entry_07_diagnostics_and_display/TRIOCTAGON_ATLAS_07_DIAGNOSTICS_AND_DISPLAY_SOURCE_PACKET_v0.1.md) | [Checks](entry_07_diagnostics_and_display/TRIOCTAGON_ATLAS_07_EXACT_CHECKS.py) · [Recorded results](entry_07_diagnostics_and_display/TRIOCTAGON_ATLAS_07_EXACT_RESULTS.json); 160 checks |
| 08 | Boundary response, fixed SRG and initialization handoff | PASS_WITH_RUNTIME_CAVEAT | [Source packet](entry_08_boundary_srg_handoff/TRIOCTAGON_ATLAS_08_BOUNDARY_SRG_HANDOFF_SOURCE_PACKET_v0.1.md) | [Checks](entry_08_boundary_srg_handoff/TRIOCTAGON_ATLAS_08_EXACT_CHECKS.py) · [Recorded results](entry_08_boundary_srg_handoff/TRIOCTAGON_ATLAS_08_EXACT_RESULTS.json); 386 checks |
| 09 | Bounded operating region and invariant-domain theorem | PASS | [Source packet](entry_09_bounded_operating_region/TRIOCTAGON_ATLAS_09_BOUNDED_OPERATING_REGION_SOURCE_PACKET_v0.1.md) | [Checks](entry_09_bounded_operating_region/TRIOCTAGON_ATLAS_09_EXACT_CHECKS.py) · [Recorded results](entry_09_bounded_operating_region/TRIOCTAGON_ATLAS_09_EXACT_RESULTS.json); 222 checks |

Entry 01 also includes the [harmonic-three provenance ledger](entry_01_complex_triad/TRIOCTAGON_HARMONIC3_PROVENANCE_LEDGER_v0.1.md)
and [research correction queue](entry_01_complex_triad/TRIOCTAGON_RESEARCH_CORRECTION_QUEUE_v0.1.md).
The [old/new kernel archaeology census](provenance/TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md)
is supporting provenance, not a numbered Atlas entry or an execution certificate.
Future entries will extend this index.

## LANE-1 CLOSEOUT SUPPLEMENTS

| Supplement | Scope and closed owners | Preserved artifacts | Recorded evidence |
|---|---|---|---|
| SUPPLEMENT A | General cycle operators and pullback domains; A07–A09 = FULL | [Source packet](supplements/supplement_a_general_cycle_pullback/TRIOCTAGON_LANE1_SUPPLEMENT_A_GENERAL_CYCLE_PULLBACK_SOURCE_PACKET_v0.1.md) · [Checks](supplements/supplement_a_general_cycle_pullback/TRIOCTAGON_LANE1_SUPPLEMENT_A_GENERAL_CYCLE_PULLBACK_CHECKS.py) · [Recorded results](supplements/supplement_a_general_cycle_pullback/TRIOCTAGON_LANE1_SUPPLEMENT_A_GENERAL_CYCLE_PULLBACK_RESULTS.json) | 31/31 checks; 10 tests + 40 subtests |
| SUPPLEMENT F | Transverse group actions, finite jets, local spectrum and limiting response; F02–F06 = FULL | [Source packet](supplements/supplement_f_transverse_theorem_chain/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_SOURCE_PACKET_v0.1.md) · [Checks](supplements/supplement_f_transverse_theorem_chain/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_CHECKS.py) · [Recorded results](supplements/supplement_f_transverse_theorem_chain/TRIOCTAGON_LANE1_SUPPLEMENT_F_TRANSVERSE_THEOREM_CHAIN_RESULTS.json) | 89/89 checks; 8 focused tests |

Written analytic proofs are separate from predicate counts. Supplement F's
nonresonance, local linearization, common analytic chart and coefficient/limit
interchanges rely on its written arguments and hypotheses; 89 passing records
are not a count-based proof of those analytic theorems.

## CURRENT-KERNEL MATHEMATICAL COMPLETENESS

~~~text
LANE1_COMPLETENESS = PASS
LEDGER_ROWS_TOTAL = 75
MISSING_MATHEMATICAL_COVERAGE = 0
PARTIAL_MATHEMATICAL_ROWS = 0
~~~

- [Review v0.2](completeness/v0.2/TRIOCTAGON_CURRENT_KERNEL_MATHEMATICAL_COMPLETENESS_REVIEW_v0.2.md)
- [Crosswalk v0.2](completeness/v0.2/TRIOCTAGON_CURRENT_KERNEL_ATLAS_CROSSWALK_v0.2.json)
- [Checker v0.2](completeness/v0.2/TRIOCTAGON_CURRENT_KERNEL_COMPLETENESS_CHECK_v0.2.py)
- [Result v0.2](completeness/v0.2/TRIOCTAGON_CURRENT_KERNEL_COMPLETENESS_RESULTS_v0.2.json)

VALIDATION = PASS: 138/138 static census checks; scientific_code_executed = false.
Mathematical completeness means every currently accepted K0 definition/proof
family has been accounted for at its required depth. It does not mean every
historical motivation is known, every proposed physical interface is solved,
every runtime process caveat is cleared, or Lane 2 old/unported mathematics
has been reconstructed. The v0.1 HOLD files remain immutable historical
evidence described by v0.2; they are not added to this publication payload.

## Runtime caveats retained

Atlas 07 and Atlas 08 remain **PASS_WITH_RUNTIME_CAVEAT**, with
runtime_caveat.status = OPEN_RUNTIME_CAVEAT. Their scientific predicates and
focused pytest assertions passed, but Windows access-violation diagnostics
appeared on stderr. The anomaly remains unresolved. Later clean Atlas-09 and
Supplement-F runs do not clear either historical caveat. Mathematical
completeness PASS and these runtime qualifications describe different claims.

## Open questions and interpretation boundaries

Closed entry status means the bounded investigation is complete; it does not
mean every historical or physical question has been solved.

| Interface | Category | Retained status |
|---|---|---|
| Why the pairwise third harmonic was historically selected. | HISTORICAL_PROVENANCE_OPEN | OPEN |
| Physical point-position law for Omega on the shell. | PHYSICAL_INTERPRETATION_OPEN | OPEN |
| Omega→PaperD gap/corner-cell state attachment/transport map. | MATHEMATICAL_OPEN | OPEN_UNADOPTED_INTERFACE |
| Historical D24/15degree motifs→current exact covering causal lineage. | HISTORICAL_PROVENANCE_OPEN | OPEN |
| Physical boundary/lens calibration and response law. | PHYSICAL_INTERPRETATION_OPEN | OPEN |
| Physical helicity meaning of C2 factors and named B modes. | PHYSICAL_INTERPRETATION_OPEN | OPEN |
| Material shell boundary/seam/rim condition for a physical field. | PHYSICAL_INTERPRETATION_OPEN | OPEN |
| Physical units, time map and meanings of coefficients/observer coordinates. | PHYSICAL_INTERPRETATION_OPEN | OPEN |
| O01 support/facade decision. | SOFTWARE_SUPPORT_OPEN | RESOLVED_OPTION_B |
| O02 original eps,g,seed and theta_lock selection rationale. | HISTORICAL_PROVENANCE_OPEN | OPEN_NONBLOCKING |
| O03 portable golden-fixture publication. | SOFTWARE_SUPPORT_OPEN | CLOSED_BY_K2B |
| Windows access-violation stderr in Atlas07/08 focused runs. | SOFTWARE_SUPPORT_OPEN | OPEN_RUNTIME_CAVEAT |

The exact current cycle covering is distinct from an asserted historical causal
lineage. A tangent-state representation is distinct from a physical position
law. The Paper-D reference scaffold is distinct from the Paper-C material shell,
and geometric gap length is distinct from recurrence coupling. The entries
retain their specific assumptions and limits; this navigation page adds no
scientific theorem or physical attachment.

## Verification records and publication reruns

### Preserved publication Pass-1R history

The [preserved Pass-1R manifest](ATLAS_MANIFEST_v0.1.json) binds each copied artifact to its external
source path and preflight hash, records the original baseline and verification
categories, and separately summarizes Pass-1R's reruns.

| Entry | Original recorded predicate total | Passing standalone publication rerun | Historical integrity predicates not rerun |
|---|---:|---:|---:|
| 02 | 58 | 54 | 4 |
| 03 | 84 | 78 | 6 |
| 04 | 71 | 65 | 6 |
| 05 | 68 | 62 | 6 |

These totals contain different kinds of checks: symbolic/exact identities,
finite counterexamples, API/runtime comparisons, source observations and
integrity attestations. They are not interchangeable with pytest test counts.
Atlas 05 separately recorded, and publication Pass 1R reran, **39 tests and
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

### Publication Pass 2

The [current manifest v0.2](ATLAS_MANIFEST_v0.2.json) comprehensively indexes
entries 01–09, both supplements and completeness v0.2, preserving original
source paths, hashes, investigation HEADs, statuses and qualifications. It pins
the unchanged predecessor manifest. A later publication commit does not replace
an original investigation HEAD.

Atlas 06 records 199 checks and separately 65 repository tests + 155 subtests.
Atlas 07 records 160 checks; Atlas 08 records 386; Atlas 09 records 222. These
are preserved investigation results, not new Pass-2 executions. Atlas 09's
recorded focused run passed 15 tests + 26 subtests with empty stderr. The two
supplement test counts above are likewise separate from their checker counts.

Pass-2 validation checks external-to-repository byte equality, recorded result
identity, manifest/checksum coverage, new portable links, visible statuses and
protected-source immutability. No scientific checker or pytest suite is rerun
for this packaging pass. In particular, the copied Atlas-06 checker is not
executed from its repository directory; its historical output behavior differs
from the later external-safe checkers.

Original absolute local links and external snapshot paths remain provenance.
The preserved crosswalk's EXTERNAL_UNPUBLISHED fields describe its investigation
time. This README and manifest v0.2 supply the current publication state and
portable links. The preserved scripts are not a portable installed-package test
suite; required source/HEAD/external-layout assumptions remain explicit.

## Atlas-local byte verification

[SHA256SUMS.txt](SHA256SUMS.txt) covers every file beneath this Atlas directory
except that checksum file itself, using sorted repository-relative paths. The
Git commit identifies the checksum file. The set includes this README, the
two manifests, [Atlas-local Git attributes](.gitattributes) and all 38 preserved
artifacts (16 from Pass 1R and 22 from Pass 2). The attributes recognize the
preserved CRLF line endings, the Atlas-05 packet's original Markdown hard break
and terminal blank line, and the Atlas-09 packet's original Markdown hard break
during Git whitespace checks. Pass 2 adds six exact-file CRLF rules and one
exact-file hard-break rule. They do not normalize or alter the copied bytes.
Newly authored publication metadata uses LF line endings.

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
