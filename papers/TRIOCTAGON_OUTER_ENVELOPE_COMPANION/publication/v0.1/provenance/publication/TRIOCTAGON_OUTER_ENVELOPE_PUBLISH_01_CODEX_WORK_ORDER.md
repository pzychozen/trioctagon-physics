# TRIOCTAGON_OUTER_ENVELOPE_PUBLISH_01 — Codex publication work order

**Prepared:** 14 November 2026, Atlantic/Reykjavik.  
**Author:** Hilmir Frímann Halldórsson (pzychozen).  
**GPT disposition:** actual 12-page manuscript accepted with no mathematical, interpretive, documentary or layout correction.  
**Scope:** administrative finalization, document verification and one scoped repository publication. No new research.

## 1. Activation and stop conditions

This order is prepared, not executed. It becomes active when the author explicitly approves publication or sends Codex this packet with an instruction to publish. Mere receipt as review material is not authorization. Record that actual instruction and its date in a separate current publication-authorization record; do not backdate or invent it.

Once activated, complete the whole prescribed pass without another approval round if the administrative changes are faithful and all checks pass. Stop and return concrete findings if a scientific contradiction, source mismatch, unauthorized changed path, failed safety/preservation check or substantive manuscript change is necessary. Do not silently expand scope or replace the accepted result.

**Final outcome:** one ordinary scoped commit, one normal push to `main`, fresh byte verification of every changed path, actual CI outcome and a local closeout receipt. No force push, reset, merge, amended earlier publication, tag, release, DOI, kernel/UI work or successor investigation.

## 2. Controlling reading and input identity

Read `README_START_HERE.md`, the GPT manuscript review, `GPT_MANUSCRIPT_ACCEPTANCE.json`, then this order and `ADMINISTRATIVE_SOURCE_EDITS.json`.

The complete original manuscript return is under `received/`:

- `TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip`, 6,431,932 bytes, SHA-256 `f263c73b7be2e967557f7b98fed63be3d6179e360a9b0721e3aef566743ab24d`;
- its original `.sha256` sidecar and external `FINAL_ARCHIVE_AUDIT.json`.

It extracts under `manuscript/`. All editable LaTeX, figures, document helpers and accepted evidence are inside. No additional acceptance ZIP needs to be obtained from the author. The original manuscript packet contains 281 members, 280 manifest entries, 187 inherited input files, the complete 175-member acceptance extraction and the 143-member original investigation extraction. Count your actual publication payload; it need not have the same member count after administrative records are added.

Reviewed PDF: `TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf`, 225,962 bytes, 12 pages, SHA-256 `1b046265672f449808050b2ca542415ca4c0d29f02528d051109eec14d55302b`. It retains its submission-era status and is not the final publication build. The `reviewed/` copy has identical bytes.

Verify the publication packet's manifest, original manuscript archive sidecar and original manifest before staging. Preserve all incoming bytes. Hash raw bytes, not newline-normalized text. Historical scripts are evidence, not a requirement to execute them.

## 3. Workspace and repository protection

Repository: `pzychozen/trioctagon-physics`. Known operator checkout: `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`; inspect actual location and existing instructions instead of assuming it is clean. The latest source checkpoint supplied to this sequence is `46bf10808b8694476b61b359be305a66a46d4614`; it is a source locator, not an instruction to reset HEAD or an assertion of current remote main.

Run new document tooling in Windows Command Prompt with `conda activate torment`, assertions enabled and the existing Python/LaTeX tools. Do not install dependencies, change global Git settings or replace existing launchers. Use a short external working path, for example `C:\TORMENT\OE_PUB01`, to avoid the earlier long-path difficulties.

Record the operator's HEAD, branch, index bytes, staged/unstaged diffs, unrelated modified-file identities and remote configuration. Preserve them. Fetch current remote main normally; stage in a clean isolated short-path publication worktree based on that actual remote revision. Legitimate remote-tracking/worktree metadata changes must be distinguished from operator checkout changes. Do not stash, discard or commit unrelated work. If the remote advances before publication, rebase/recreate only the uncommitted isolated payload on the actual new base and recheck scope; never force push over it.

## 4. Frozen scientific content

Title:

**Noncollision Facet Transition and Exact Outer-Envelope Classification in the Folded Tri-Octagon**

Subtitle remains the companion relationship to *Spherical Edge Extensions of the Folded Tri-Octagon: Exact Incidence Events, Natural Terminations, and Convex Envelopes*.

Preserve O01–O04 and all equations, tables, representative plane coefficients/cycles, figure assets, proof arguments, qualifications, attribution and bibliography. In particular:

- the closed A–B partition and exactly one interior transition at `x_*=3(sqrt(2)-1)/2`, equivalently `t/h=3`;
- all 42 distinct vertices at that interior event; the 18-vertex inherited endpoints;
- full V/E/F rows `18/48/32`, `42/96/56`, `42/84/44`, `42/90/50`, `18/36/20`;
- maximal supporting faces and true polygon sides, not rendering triangles;
- the six regroupings, 38 persistent label sets, twelve disappearing and six appearing envelope edges;
- the uniform support/side-sign and ridge-adjacency completeness argument;
- the exact endpoint image correspondences and limited no-ten-vertex-maximal-facet consequence;
- the static parameter interpretation, nonisometric calculation chart and metric caveat; no material wall, physical law or all-radius geometry is adopted;
- the separation of submitted shared-engine evidence, reviewer replay and separately organized Bernstein sign checks.

No scientific generator/checker, hull nomination, sign proof, interval/Sturm/Bernstein routine, native trajectory, historical suite or kernel is to be run for this publication. Document transcriptions, identity checks, typesetting and visual inspection are allowed. Ordinary existing push-triggered CI is to be observed and reported, not disabled or presented as a scientific proof.

## 5. Authorized administrative finalization after activation

The exact proposed `main.tex`, `build.py` and `helpers/verify_document.py` replacements are specified in `ADMINISTRATIVE_SOURCE_EDITS.json`. Each has one expected occurrence and is conditional on activation. Verify original raw hashes, apply only those edits in staging and save an exact diff. Inverting those replacements must recover the reviewed source bytes exactly. No mathematical block changes are permitted.

The changes:

1. Change current edition wording from `Research manuscript v0.1` to `Research edition v0.1` in the header, title and PDF subject.
2. Replace current pending-manuscript status with project-internal manuscript review complete and author-authorized repository publication. Record the actual authorization date separately. Preserve the manuscript's 14 November 2026 preparation date and the 13 November investigation acceptance date; do not relabel old records.
3. Update the short current-status paragraph and assistance line for completed GPT manuscript review.
4. Update `build.py`'s receipt status. Its actual `client_date` should use the run date, while the fixed `SOURCE_DATE_EPOCH` may retain the documented manuscript-date reproducibility convention. Actual start/finish timestamps must remain truthful.
5. Change the document helper's pending-metadata expectation to the exact new subject. Keep author/title checks, assertions, font/text/reference/source checks and PDF binding intact. Do not remove tests to make publication pass.

Update only current administrative files (`README.md`, `HANDOFF.md`, `CURRENT_STATUS.json`, current build/document/claim/link records) to reflect this stage. Preserve original versions in the unchanged review ZIP. Keep the bibliography entry describing the earlier scientific review as investigation-only: that remains accurate historical attribution.

The current review-stage `helpers/package_review.py` hard-codes review-return wording. Preserve it as the historical authoring helper; use a clearly identified publication-packaging helper for the new stage rather than publishing a new false pending-review audit. The original inherited files under `evidence/`, `archives/` and `provenance/commission/`, plus all 187 `PRESERVED_INPUTS.json` entries, must remain raw-byte identical.

Keep `references.tex`, all seven table files, both original figure files and `helpers/make_tables.py` unchanged. Do not normalize Windows line endings. A document-only scratch reproduction may compare text after disclosing platform newline differences; the publication source still uses its approved original bytes.

## 6. Final Windows build and document acceptance

Use the existing compatible cached compiler in untrusted/offline mode with intermediates outside the publication tree. Build from the actual to-be-committed sources; no environment, compiler cache or font binary is part of the deliverable. Embedded PDF fonts are appropriate.

Record exact command, compiler/environment versions, raw source hashes, exit status, log and the resulting PDF identity. No byte match to the old PDF is expected because its status changes. Do not label the old reviewed PDF as the new Windows build.

Resolve all references/citations and inspect warnings. Expected scientific numbering remains 46 labels and four bibliography entries; retain the 14 numbered equations. Refresh all four claim mappings and their actual source-line/PDF-page locations. A harmless pagination change is permitted only after full fresh page inspection, correct updated references and unchanged scientific text; do not compress the content merely to force 12 pages.

Render and individually inspect every final page, especially the three vertically arranged figure panels and the orbit-table continuation. Verify readable labels, signs, denominators, full zero cycles, no clipping/overlap or unintended blanks, all embedded fonts, selectable text and accurate metadata. Bind every inspection record to the exact final PDF hash. Any subsequent source/PDF change requires a fresh build/inspection.

Refresh current document/reference/font/transcription/source/link records and the current manifest, preserving old receipts separately. A stale submission manifest must not be presented as the current publication manifest. Keep the original review ZIP intact so every old record remains attributable. Verify all 187 inherited inputs again after finalization.

## 7. Exact publication scope

Use this new subtree unless it already exists with conflicting content:

`papers/TRIOCTAGON_OUTER_ENVELOPE_COMPANION/`

with a landing `README.md` and edition

`papers/TRIOCTAGON_OUTER_ENVELOPE_COMPANION/publication/v0.1/`.

Canonical PDF filename: `TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf`.

Include final PDF, editable source, tables/figures, build guide/helpers, current claim/access/status records, complete preserved evidence and acceptance, original manuscript submission, this GPT manuscript review and final publication verification/provenance. The standalone publication work order and author activation can be retained under a separately identified publication provenance folder. Avoid redundant copies of every nested archive when the exact complete original already exists; preserve every required record.

Add one narrowly scoped catalog entry to the current root `README.md`, without rewriting unrelated existing descriptions or historical statuses. Suggested factual summary:

> Noncollision Facet Transition and Exact Outer-Envelope Classification in the Folded Tri-Octagon — research edition v0.1. Complete static A–B maximal-face classification with a unique noncollision transition at t=3h. The 42 vertices stay distinct there; the interior facet counts are 56/44/50. No ten-vertex maximal facet occurs in this closed family. No kernel changes or physical-boundary adoption.

Do not edit `papers/SPHERICAL_EDGE_EXTENSIONS/`, its research evidence, Paper C, any other prior edition, application, kernel, dependency or workflow. Preserve existing rights/licensing; repository software licensing does not automatically apply to scientific papers/data. This is repository publication, not external peer review or a journal acceptance.

Freeze a path allowlist and inspect the staged diff before committing. The complete changed-path set must be the new subtree plus the single root catalog modification. Verify earlier paper trees and operator edits unchanged. Stage explicit paths, not `git add .`.

## 8. One commit, normal push and real verification

After every pre-publication check passes, make one ordinary scoped commit and one normal push to `main`. No force push, second receipt-only commit, squash/rewrite of older history or branch-history replacement.

Verify the actual commit, parent and remote branch result. For **every changed path**, download fresh complete bytes from a commit-pinned GitHub endpoint and compare byte count/SHA-256 with the actual committed Git blob, including binaries and archives. Re-read the current-main PDF separately. Stored local hashes or a successful push alone do not count as remote byte verification.

Check actual workflow runs and check runs on that exact commit. Record real conclusions, failed/pending checks and path-filtered untriggered workflows separately. An empty combined-status placeholder is not a running job. Do not call untriggered workflows passed; do not change CI or manually dispatch unrelated scientific jobs.

If a genuine publication failure appears after the push, report the exact failure and scope; do not conceal it with an unauthorized rewrite or an invented successful receipt.

## 9. Local receipt, closeout and final return

Keep the final receipt outside the committed payload to avoid a self-referential extra commit. Return Markdown/JSON receipts with title/edition, author authorization, actual commit and parent, immutable edition/source/PDF links, final page count/bytes/SHA-256, actual changed-file count, fresh remote comparison count, CI outcomes and preservation results.

Produce `TRIOCTAGON_OUTER_ENVELOPE_PUBLISH_01_CLOSEOUT.zip` plus an external `.sha256` and `FINAL_CLOSEOUT_AUDIT.json`. Include the unchanged incoming publication packet and original review archive, committed publication payload, current build/inspection and raw remote/CI evidence, exact diff/allowlist, execution records and local receipt. Exclude font binaries, caches, executables and unrelated private files.

Use a self-excluding manifest. Reopen every final archive member and verify complete raw bytes, CRC, safe unique/case-unique paths and all preserved input identities. Bind standalone, built, staged, committed, downloaded and inspected final PDFs to their actual matching hashes. Count from the completed archive, not from a planned total.

**Stop after publication closeout.** No manuscript sequel, broader shell study, dynamics investigation or memory-system work is opened by this order.
