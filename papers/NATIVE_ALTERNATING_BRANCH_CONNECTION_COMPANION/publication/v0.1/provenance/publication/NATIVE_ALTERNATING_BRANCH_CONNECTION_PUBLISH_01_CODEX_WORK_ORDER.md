# Codex publication work order
## NATIVE_ALTERNATING_BRANCH_CONNECTION_PUBLISH_01

**Prepared:** 12 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Paper:** *Certified Connection from Local Period-Doubling to the Captured Alternating Cycle in the Native Triad*  
**Edition:** v0.1, companion to Paper G

## 0. Activation, authority and stopping rules

GPT manuscript review accepts the actual 13-page manuscript's mathematical content, interpretation and layout. No manuscript equation, proof or layout correction is required. E01 is one documentary helper correction, described below.

**Execute publication only when the author explicitly approves it or forwards this order as the instruction to finalize and publish.** Merely encountering this order in an archive is not permission to push. The manuscript commission by itself did not authorize publication. Record the actual author's instruction; do not invent an approval date or imply external peer review.

Once activated, complete this as one continuous finalization/publication task. The bounded E01 correction, current-status updates and faithful verified rebuild do not require another scientific approval round. A newly discovered substantive mathematical contradiction, irreconcilable source identity, unexpected repository conflict or unsafe push condition is a blocker: report it instead of silently expanding scope.

No new scientific runs, full-range stability work, other research, kernel changes, application changes, release, tag, DOI registration or licensing change is authorized. Preserve Paper G and all earlier editions byte-for-byte.

## 1. Inputs and accepted baseline

Read `README_START_HERE.md`, the accompanying GPT manuscript review, `MANUSCRIPT_ACCEPTANCE.json` and `corrections/E01_RECORD.md`. Extract `received/NATIVE_ALTERNATING_BRANCH_CONNECTION_PAPER_01_REVIEW.zip` into a new external working directory; it contains complete editable source, the original accepted scientific evidence and all documentation. Verify its supplied checksum and internal inventory.

Controlling identities:

| Object | SHA-256 |
|---|---|
| Incoming review ZIP | `6d80f33bd11be2176d6ba875ddd0b6fd263099675bb3f13179081053bf396f79` |
| Reviewed 13-page PDF | `7a792a179040faa203295f0f903992a6bb55902869c43dafde758c48fd851035` |
| Reviewed main.tex | `2d51b97e13a7ab2a8a90274c7231fa0cb94af4d31b8758a084ed35c26028fd6f` |
| references.tex | `c3b4d9755384f0a0ccfa19d5a747446a743c436ad13a6b2f056c4eb613004f08` |
| Raw tables/certificate.tex | `b4e92700ab9024be91c88891bdb982b27f9424ec330ad33bf635ffdf84968b56` |
| Original helper | `d5f3a028f3029d499aaa3f2de0ffc5f96e2803a5babb755cb0d5af0c5a095b67` |
| E01 replacement helper | `2321b16b6d38f73d3d87b119443e92613eaba7da098a97ef7f9e7c4c44fbdc1c` |

The reviewed PDF is 127,629 bytes. The incoming archive contains 330 members, including 187 preserved commission inputs and a complete 177-member scientific-acceptance extraction. All must remain recoverable in the closeout. The reviewer PDF is an unchanged copy of the incoming Windows PDF, not a new Linux build.

Suggested external workspace:

`C:/TORMENT/TRIOCTAGON_new/research/NATIVE_AB_PUBLISH_01/`

Use short external/worktree paths where needed to avoid Windows path-length problems. Source checkpoint commits are reading references, not instructions to reset the operator checkout.

## 2. Frozen mathematics and historical evidence

Do not change the family, coefficients, host selection, critical data, gauge, normalized equations, onset argument, patch/connector proof, exact endpoint, inequalities or scope statements.

Retain:

- Branch identity for `0 < mu <= 1/200`, with zero only as a normalized onset anchor.
- 128 uniform patches and 127 common-uniqueness joins, not just overlapping boxes.
- Whole-enclosure inclusion in the exact inherited `Up`; `Um` remains an outer image enclosure.
- Primitive full-state two-cycles and neutral common-phase family; no all-interval nonvanishing claim for W or Gamma.
- New local attraction only for `4999/1000000 <= mu <= 1/200`, actual two-step norm `< 0.9601`. Root-equation contraction is not native attraction.
- Full-range attraction unresolved; existing qualitative near-onset attraction and endpoint capture remain separately scoped.
- No parameter ramp within an orbit, new entrance theorem away from the M3 endpoint, global basin, physical field or calibrated time.
- Shared interval-engine disclosure and the distinction between historical scientific checks, numerical diagnostics and current document checks.

Preserve `evidence/branch/`, `archives/`, all original scientific outputs and code, and immutable `provenance/commission/` records unchanged. Keep old pending-status wording inside preserved historical artifacts; a new current disposition supersedes only the administrative status. Do not replay scientific scripts or re-solve a branch for this publication.

## 3. Apply E01 — raw-byte document hashes

In the editable finalization copy only, replace `helpers/verify_document.py` with the supplied `corrections/helpers/verify_document.py`, after checking the original and replacement hashes. The exact diff is `corrections/E01_verify_document.diff`.

The old helper hashed newline-normalized source text in `DOCUMENT_CHECK.source_hashes`. The table uses CRLF, so that entry differed from the raw-byte hash already correctly recorded by the build receipt and manifests. The table itself and the reviewed PDF are correct and unchanged.

The replacement uses `(ROOT/n).read_bytes()` and explicitly labels the raw-byte hash basis. Preserve the historical original check record in the incoming archive. Generate a new current `DOCUMENT_CHECK.json` during finalization. Do not “fix” the discrepancy by converting the table or accepted evidence line endings.

Confirm that the final document-check source hashes match the actual raw bytes and the final build receipt for all three source inputs. The manuscript-level hash-expression test is supplied in `reviewer/HELPER_FIX_TEST.json`; it is not a final Windows build/check record.

## 4. Administrative status finalization after author activation

Use **Research edition v0.1** and truthful current wording such as:

> Project-internal manuscript review complete; author-authorized for repository publication. No external peer review or proof-assistant verification is claimed.

Allow only these current administrative edits:

1. `main.tex`: PDF subject, running header, first-page edition/status, Section 8 current-review sentence, and final authorship/publication-status sentences. Retain title, author, original manuscript date 12 November 2026, all mathematics and scientific exposition. Record later finalization/authorization dates separately if execution occurs later.
2. `README.md`, `CURRENT_STATUS.json`, `HANDOFF.md`, and necessary build guidance: record the GPT manuscript acceptance and actual author's publication instruction. Do not claim a successful push before it happens.
3. `build.py` and the corrected `helpers/verify_document.py`: change status labels/metadata assertions only where necessary. The current helper explicitly expects a pending-review PDF subject; replace that assertion with an appropriate check for the authorized research edition, while retaining all font/reference/layout/hash checks and environment safeguards.
4. The current manuscript claim ledger and verification records: refresh actual source lines, page numbers, statuses and raw-byte source/PDF hashes after the rebuild. All six claim IDs, classifications, scientific assertions and immutable source references remain unchanged.

Suggested Section 8 status replacement:

> The mathematical investigation was internally accepted on 11 November 2026. This companion manuscript was prepared and completed GPT project-internal manuscript review on 12 November 2026. The author has authorized repository publication of research edition v0.1. Historical submission and acceptance statuses remain unchanged in the preserved evidence.

Use the last two sentences only after the actual author authorization is received. Do not revise the historical investigation-review reference into a new scientific proof source.

Keep `references.tex`, the accepted table and its generator byte-identical. If generation reproduces a file, confirm equality before adopting it. The source helper E01 is the only non-status code change authorized.

## 5. Final Windows build and verification

Use Windows Command Prompt with the existing `torment` environment and existing cached TeX tools. Preserve `--only-cached --untrusted` and the existing external-build protections; install no dependencies and change no global environment settings.

Before building, inspect the exact source/helper diff. It must contain only E01 and the administrative changes above. Verify that scientific text, all 43 existing numbered equation/align environments and theorem/proof bodies are unchanged apart from authorized administrative passages outside those bodies.

Rebuild until references resolve. Verify the final PDF's page count, title/author/edition metadata, selectable text, embedded fonts, bibliography and links. The reviewed baseline has 13 pages, 75 labels, six citation keys and 18 unique fonts. Those are baseline observations, not a reason to hide a legitimate engine-dependent pagination or font difference. Explain any change and inspect all final pages. The final visual review must bind the exact final PDF hash; never reuse the incoming review-image record as proof of inspecting a rebuilt PDF.

Refresh the six-claim crosswalk with actual final labels, pages and source-line locations. Check all numerical table bounds by comparison with retained exact values only, not by scientific replay. Verify all 187 preserved inputs and the complete accepted evidence are unchanged. Do not normalize historic newlines or metadata.

Generate new current publication build/document/preservation records. Keep original preparation records explicitly historical in the incoming archive or a history directory; never leave an obsolete manifest claiming to inventory the modified edition. Generate a fresh self-excluding publication manifest for the actual payload. Exclude temporary page renders, caches, font binaries, bytecode and TeX intermediates from the committed paper payload; retain needed inspection renders in the external closeout instead.

## 6. Publication destination and discoverability

Repository: `pzychozen/trioctagon-physics`.

Proposed new subtree:

`papers/NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION/publication/v0.1/`

Add its landing `README.md` at:

`papers/NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION/README.md`

If the proposed destination already exists with unrelated or conflicting content, stop rather than overwrite it. Preserve existing evidence relative links within the edition. Include editable TeX, final PDF, necessary helpers and accepted evidence, the current scientific/disposition records, and byte-preserved sources needed by the paper.

Add one standalone catalog entry to the root README near Paper G or the recent native companions. A suitable scientific summary is:

> Certified M2-to-M3 alternating-branch connection throughout `0 < mu <= 1/200`, with a separate explicit local-attraction result only on `0.004999 <= mu <= 0.005`. Full-range attraction remains unresolved. Companion to Paper G; no kernel changes.

Use the actual title, author, edition and relative PDF/source links. Do not rewrite Paper G's historical statement of its then-open gap, alter its index or replace any earlier edition. A new catalog entry and the companion's own links supply discoverability. Preserve all existing rights and licensing boundaries.

## 7. Repository protection and one scoped push

Read applicable local repository instructions. Record actual origin, branch, HEAD, index and existing staged/unstaged changes without changing them. Fetch the actual current remote `main`; do not assume the last reported checkpoint is still its tip.

Use a clean, short-path isolated publication worktree based on that fetched `main` when the operator checkout has unrelated work or unpushed commits. Preserve the operator checkout's HEAD, index, branch and working files. Do not reset, clean, force-push, rewrite history, bypass branch protections, alter the remote, or publish unrelated commits.

Freeze an explicit allowlist: the new companion subtree and one bounded root README catalog edit. Stage only those exact paths, inspect the staged diff, and verify the parent Paper G tree is unchanged. Include a truthful pre-publication disposition but no fabricated push result.

Make **one ordinary scoped commit** and **one normal push to main**. If remote main advances or the push is rejected, stop and reconcile safely; do not force. No second receipt-only commit is required. Do not create tags/releases or dispatch unrelated workflows.

## 8. Fresh remote verification and actual CI

After the push, freshly download every changed file from the actual commit-pinned GitHub location. Compare its full byte count and SHA-256 against the actual committed Git blob. Include PDFs, archives and all other published file types. Separately fetch the current-main PDF and verify its identity. Record actual URLs, hashes and outcomes; no local-cache-only remote claim.

Observe actual workflows and check runs for the publication commit and report their real outcomes. Distinguish successful, failed, pending and path-filtered/untriggered workflows. Do not count an untriggered workflow as passed or an empty legacy status placeholder as an active check. Do not claim final CI success while required actual checks remain pending.

Verify the operator checkout and parent Paper G tree remain unchanged. Keep preservation evidence separate from scientific acceptance.

## 9. Return and closeout

Return a concise publication summary with the actual commit and immutable edition/PDF links, final page count/bytes/hash, changed-file remote verification count, actual CI outcomes, and any genuine limitations.

Deliver external `PUBLICATION_RECEIPT.md`, `PUBLICATION_RECEIPT.json`, a complete closeout ZIP and its `.sha256`, and a final audit reopening and checking all closeout members. Include the unchanged incoming review archive, this publication instruction/author activation, the GPT review and E01 diff, final published payload, final build and page-inspection records, preservation checks, fresh remote bytes, CI records, and actual execution logs. Keep receipts external to avoid a circular or unnecessary second commit.

This completes this companion's publication. It does not commission full-range attraction or any successor research.
