# Publication disposition

SHELL-APP PUB-01 publishes exactly 29 frozen source payloads and five documentation changes. The source set is 18 accepted feature paths plus 14 required pre-existing export-repair paths, with three overlaps: 29 unique paths. Relative to the sole expected parent `0997e565f2ddbd350d3c50e5d3af26c651d8b4c9`, the complete change is 12 modifications and 22 additions, with no deletions. The root README is append-only. The manifest has 33 payload rows and excludes itself.

The accepted P1R1 implementation closes F01 and F02. Its exporter/helper, evaluator, reference data, V01 endpoint behavior, dependencies and certification workflow remain unchanged. The export repair is deliberately included as the accepted feature's prerequisite. This publication makes no additional implementation or scientific change.

## Identity and chronology

| Identity | Meaning |
| --- | --- |
| Scientific-source commit `0997e565f2ddbd350d3c50e5d3af26c651d8b4c9` | Accepted paper/research checkpoint and source-publication parent; not the newly published application commit |
| P1R1 candidate SHA-256 `2d56afdeb0f95b72a9db7e623f52798805100ee1bf0561f3339a424e3d81d53d` | Reviewed 18-path application candidate archive |
| P1R1 path manifest SHA-256 `580d8d2f067af66cede27c1aa19c5b440539a4d86b275b8cfe3df3816e17934e` | Reviewed feature path/byte ledger |
| Retained UI 0.2.1 wheel SHA-256 `eeee31896be43e44ad6a23c1412cc7e55a9605ad886e278e3f62d90a29f9339f` | Original accepted local build; not a new build or released package |
| Commit containing this publication manifest | New repository source-publication identity; obtain it from Git history and the external closeout |

The accepted implementation still reports UI 0.2.1 and `UNRELEASED_UNCOMMITTED_CANDIDATE`. **That literal is frozen snapshot metadata, not a live Git-status query. After this source push, it is no longer a literal description of repository publication status.** Newly produced exports do not automatically report the new source-publication commit. Their actual module/resource hashes and this publication manifest map the reviewed implementation bytes. `public-release-authorized = false` remains appropriate: no package release is authorized here.

Earlier app and research notes retain their original checkpoint wording. In particular, the accepted app README's candidate status and the historical viewer's integration-absent statements are not rewritten. The separate native feature now exists; this note supplies the later publication context without altering accepted historical records.

## Retained limits

SHELL_NUMERIC_V1 is a bounded Decimal/binary64 observation policy, not a whole-domain floating-point proof. V01 lower-endpoint pins and explicit adjustment records remain unchanged. Generic radius inputs do not become exact events by proximity. Extension units are unavailable at zero extension. View clipping and pending-input validity remain visible even when an export notice is present.

The 3D plot supports rotation, rectangle zoom/history and explicit camera controls. Scroll-wheel zoom remains unimplemented. Native pan dragging was not separately demonstrated in P1R1; axis-limit/history behavior has Qt evidence. Offscreen constrained-layout warnings are retained in the original evidence. This is not full accessibility certification. Export publication is not a two-file atomic transaction; an interrupted process can leave an incomplete pair or scratch file.

No kernel, trajectory, RNG-driven scientific value, production memory, physical boundary, energy law or research acceptance is added. The source push may trigger the existing automatic CI acquisition/build/test workflows. Their actual results belong to the external closeout and GitHub run records, separately from retained local certification. No CI result is asserted in this pre-commit record; no manual rerun or repair is part of this publication.

The public notes are newly written summaries. Original review archives, screenshots, raw logs, private conversations and local certification records stay outside this public payload. The frozen scientific resource and admitted inert fixture preserve their already accepted provenance bytes. Existing software-only and scientific-data rights remain unchanged; no new licence, release or endorsement is created.
