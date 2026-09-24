# K1-K3 mathematical convergence: bounded parity closeout

Date: 24 September 2026. Scientific lead and scope acceptance: GPT.
Implementation and Windows checkpoint execution: Codex. Author: Hilmir Frímann Halldórsson.

**The contracted K1/R1, K2 and K3 implementation-parity work is complete, accepted
within its stated scopes, and published.** This record consolidates those
acceptances. It does not reopen the papers, introduce a new model, or claim that
every historical feature or every result of Papers D/E has a runtime API.

Implementation baseline: `d2b1cbeca807ae33117f02f697e5eff0b4b1ca96`.
Implementation tree: `9d047be84b0a37a9206563e2d8efaeb03c7a0d5c`.
A later documentation-only commit containing this record does not change that
implementation identity. The larger Tri-Octagon reconstruction remains open.

## 1. Location and ownership

```text
CHECKOUT: C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
SOURCE:   C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\kernel_physics
PYTHON:   C:\TORMENT\TRIOCTAGON_new\kernel_physics\.venv\Scripts\python.exe
```

The sibling directory supplies the interpreter only; it is not a second source
edit target. Historical kernel snapshots remain evidence, not runtime imports.
This scientific reconstruction is separate from production TORMENT memory work
and from the curved-spatial-slice/warp-drive research.

Canonical Omega remains the input/output state of the existing recurrence.
Reference geometry is separately selected. The Z layer observes supplied states
and explicitly owned clock/memory values. Diagnostics inspect supplied data;
they neither advance the system nor alter it to satisfy an identity.

## 2. Published checkpoints and exact scope

| Packet | Published commit | Accepted addition | Test methods added |
|---|---|---|---:|
| K1, including R1 | `2b336f247aa2c24cd7596a1fc733a7b948fdb840` | Exact Paper-D reference scaffold; symbolic-denominator correction | 39 = 27 + 12 |
| K2 | `022fa5147bbf4184bd9e41b6330bf5dfc90759d9` | Explicit staged-envelope and separately named EMA observers | 37 |
| K3 | `d2b1cbeca807ae33117f02f697e5eff0b4b1ca96` | Passive mathematical accounting and selected display adapters | 36 |

The commits' scoped acceptance statements supersede preparation-time
pending-review text in their unchanged validation artifacts. Earlier failures,
input hashes and execution history remain evidence; they are not rewritten by
this closeout. No Claude implementation review is represented.

From the pre-convergence Paper-E publication at
`c60e4cfa9b3e5247f522a6036657c4d6fac75da1` through the implementation baseline,
the tracked delta is exactly twelve added files and one modified package README.
The twelve additions are three runtime modules, three test modules and six
validation receipts. No pre-existing tracked runtime module, predecessor test,
paper or historical source changed, and no tracked file was removed. The four
local-only predecessor test files retain their pre-K1 identities separately.

## 3. Requirement-to-implementation map

The detailed equation/function/test ledgers in the linked receipts are the
controlling implementation records. This is their consolidated scope map, not
a replacement proof or a claim of unrestricted symbolic/numerical equivalence.

| Contracted requirement | Current implementation | Evidence and boundary |
|---|---|---|
| Paper-D aligned selected edges, positive connector, alternating polygon and regular member | `reference_scaffold.ReferenceScaffold`, `from_radius`, `regular` | Paper D v0.1.1 sections 4-14; endpoint/vector identities, independent printed-coordinate oracle, positive-domain and symmetry tests |
| Closed filled scaffold, support triangle/corner cells and complete reference octagons | `HalfPlane`, `HalfPlaneIntersection`, `Octagon`, scaffold support/planar/vertical properties | All vertex/half-plane conditions; connector retention and apex exclusion; filled sets distinguished from outlines and welded faces |
| Paper-C comparison and fixed-centre shrink | `paper_c_member`, `paper_c_rigid_map`, named translation and shrink functions | Finite vertices/edge sets and affine maps; unique special shrink factor; six sides exactly 1/3 at original width one; not a generic collision or distance engine |
| K1 R1 representation correction | `reference_scaffold._point` with `radsimp(..., symbolic=False)` | Substitution-first finite-output regressions; accepted positive symbolic inputs retained; not a universal simplification-domain theorem |
| Historical clock and staged scalar/macro/total | `z_manifold.Clock`, `advance_clock`, `observe_staged`, scalar/vector helpers | Paper E v0.1.1 equations (1)-(2); literal defaults, explicit time, cone/frozen-harmonic checks; raw chirality delegated to existing `readouts.z_chiral` |
| Separate historical EMA and initial-record semantics | `EMAConfig`, `EMAState`, `advance_ema`, `observe_ema`, `historical_constructor_zero` | Equations (39)-(40), bounded-memory reasoning, exactly one explicit update, no implicit update on observation; constructor zero is not a recomputed readout |
| Full norm/Q and channel-area accounting | `z_diagnostics.readout_accounting`, `quadratic_form`, `chiral_area_accounting` | Full signed-weight terms, including alpha^2 Q(M); supplied inconsistencies and Gram/slack residuals are retained, not clamped or repaired |
| Finite-step intensity and potential | `intensity_budget`, `potential` | Unforced equations (33)-(38), full squared-increment remainder and six-real-coordinate gradient; overshoot retained; no descent controller or forcing API |
| Historical alignment and distinct selected display maps | `historical_alignment`, `direct_history_coordinates`, cylinder helpers, `history_torus_coordinates` | Resolution flags, direct-key fallback rules, entire-history normalization metadata, finite-source comparisons and information-loss tests; no inverse runtime or six-gap placement |
| Existing behavior and separation | Existing dynamics/geometry/readouts plus explicit new modules | Unchanged source identities; import/call-boundary, nonmutation, regression and package-isolation checks; no Z-to-Omega feedback |

Detailed records:
[K1/R1 validation](K1_REFERENCE_SCAFFOLD_VALIDATION.md) and
[JSON](K1_REFERENCE_SCAFFOLD_VALIDATION.json);
[K2 validation](K2_HISTORICAL_Z_VALIDATION.md) and
[JSON](K2_HISTORICAL_Z_VALIDATION.json);
[K3 validation](K3_MATHEMATICAL_DIAGNOSTICS_VALIDATION.md) and
[JSON](K3_MATHEMATICAL_DIAGNOSTICS_VALIDATION.json).

The source specifications are
[Paper D v0.1.1](../papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md)
and [Paper E v0.1.1](../papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md).
Their own hypotheses and interpretation limits remain controlling.

## 4. Verification and attribution

The final K3 checkpoint measured **207/207 local methods** and **177/177 isolated
candidate-index package methods**, with no failures, errors or skips. Both
contain the same 112 K1/R1+K2+K3 methods. The published package includes 65 older
tracked methods; the local checkout additionally contains 30 older untracked
methods. These are method counts, not theorem counts.

The isolated checkpoint export contained exactly 35 package files, including
the complete final frozen Markdown and JSON receipts, without placeholders.
Its before/after bytes matched the staged index. The new README example was
executed in both contexts and matched its accepted output. The disposable
export was then removed; execution evidence was retained.

Those full checkpoint runs were performed by Codex on Windows using Python
3.12.14, NumPy 2.3.5, SymPy 1.14.0 and mpmath 1.3.0. Prior GPT implementation
reviews separately recorded Linux execution of 39 K1/R1, 37 K2 and 36 K3 methods,
plus the specified bounded source comparisons and additional probes. They are
not one fresh GPT execution of the whole local suite.

GPT's final K3 checkpoint review independently reconciled the uploaded raw
identities, recorded successful IDs and output, import paths, final-receipt
export manifest, seven protected-hash maps and six index/status snapshots.
The complete candidate tree reconstructed to the tree referenced by the live
GitHub commit. No new test run or access to the Windows filesystem was claimed
by that checkpoint review.

Checkpoint evidence (retained operator artifact, not a repository file):
`CHECKPOINT_EXECUTION_EVIDENCE.json`, 3,317,515 bytes,
SHA-256 `e60b2827231bfe6467234e97ded0d9f43544caf3ef6dc5952d1cf329f9dfdfb6`.
Checkpoint report SHA-256:
`3ed747a5a6e7baba7291a10bdfc61108f470fa5cc196659676dafd0b2c83050a`.
GPT checkpoint-review artifact: `K3_CHECKPOINT_GPT_REVIEW.json`, SHA-256
`f859f26ad93a1ecca572315edd6be7ceced8897589220d8b938e7a78d9670c18`.
These identities identify existing evidence; they do not require copying the
large operator logs into the repository or expanding the integrity claim to
the whole filesystem.

## 5. Preserved limits and outstanding obligations

**Test-publication obligation remains open.** The following existing files are
untracked and not included in the 177-method package coverage. They were not
lost, recreated, edited or staged during convergence.

| Local-only predecessor file | Methods | Preserved raw SHA-256 |
|---|---:|---|
| `tests/test_boundary_pipeline.py` | 4 | `e820c5ea52c3d53f580cac1427d97935a45a8c35ea10da120b00447c437f64c9` |
| `tests/test_boundary_response.py` | 8 | `6d95629e69ebc0d80c9d16f39286b4c26ce1f4a47c05346cb49b467365cfefe7` |
| `tests/test_operating_region.py` | 9 | `c873358fcf618bc62a8b0277660cc19fa057273f14c169a521e09d5683d33c35` |
| `tests/test_srg.py` | 9 | `a74119c3211e7f790a99a0f3eba2574bffaa45482e8a7a3b9ff5a597f28fed59` |

Publishing them requires a separate bounded decision and check; this closeout
does not authorize it or claim full-local-suite reproducibility from a clone.
The 2,130 pre-existing untracked status entries at the final checkpoint were
retained. A clean tracked tree/index was not an empty untracked workspace.

**Scientific and implementation limits remain explicit.** Exact arithmetic
arguments, finite symbolic witnesses and binary64 tests are different kinds
of evidence. The symbolic API does not decide every expression's domain. The
numeric APIs may reject intermediate underflow/overflow even when another
algorithm could evaluate an equivalent expression. Rounded zeros, saturation
and residuals are not mathematical certificates.

The modern `arg0` convention is not silently replaced by historical signed-zero
phase behavior. Source comparisons are bounded same-state/readout/display
comparisons, not full historical-trajectory or all-input bitwise equivalence.
Frozen harmonic results are not general evolving-trajectory symmetries. A
negative-gradient increment does not guarantee finite-step potential descent.

The following are deferred, not implied by successful convergence: six spatial
gap anchors and Z registration; the third Tri-Octagon construction; calibrated
physical fields/energy/flux; forced evolution; runtime torus inversion;
three-channel tube curves; spike/turning consumers and percentile viewer scaling;
RSB, portal and identity machinery; E6/E8 or QCD interpretation; and the advanced
scientific UI. No open interface is filled by analogy or by a matching count of
three, six or twelve.

## 6. Return to the author's geometry

The implementation task is closed within the contracted scope. The next
scientific discussion returns to Hilmir's remaining geometric explanations,
starting with the third construction before choosing a six-gap attachment.
One idea is described, restated and corrected; its definition is agreed before
new derivations, comparisons or implementation. Existing papers and kernels
remain reference baselines rather than targets for speculative rewrites.
Larger datasets, additional integrations and UI work remain later decisions.

```text
K1_R1_REFERENCE_SCAFFOLD = ACCEPTED_AND_PUBLISHED_WITHIN_SCOPE
K2_HISTORICAL_Z_OBSERVERS = ACCEPTED_AND_PUBLISHED_WITHIN_SCOPE
K3_PASSIVE_DIAGNOSTICS = ACCEPTED_AND_PUBLISHED_WITHIN_SCOPE
CONTRACTED_K1_K2_K3_IMPLEMENTATION_PARITY = CLOSED
LATEST_IMPLEMENTATION_CHECKPOINT = d2b1cbeca807ae33117f02f697e5eff0b4b1ca96
LOCAL_SUITE_AT_CHECKPOINT = 207/207
PUBLISHED_PACKAGE_SUITE_AT_CHECKPOINT = 177/177
LOCAL_ONLY_TEST_PUBLICATION = OPEN_SEPARATE_OBLIGATION
SIX_GAP_REGISTRATION = OPEN
BROADER_RECONSTRUCTION_COMPLETE = NO
NEXT_SCIENCE = AUTHOR_LED_GEOMETRIC_DEFINITION
```
