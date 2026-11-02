# Codex work order — finalize and publish the native-potential/coherence paper

**Task:** NATIVE_POTENTIAL_INFORMATION_PUBLISH_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson / pzychozen  
**Scientific direction and manuscript review:** GPT  
**Execution:** Codex  
**Authorization:** APPROVED through finalization, one ordinary commit, normal push, and remote verification

## 1. Author decision and endpoint

The author has explicitly approved the publication/push work order after GPT's manuscript review:

> approved codex work order push - can you please write it

Publish **Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map**, repository research edition **v0.1**.

This authorization includes the exact abstract clarification R1, the citation polish R2, consistent edition-status wording, document rebuilding and inspection, scoped repository adoption, one ordinary publication commit, a normal push to origin/main, and fresh commit-pinned verification of every committed file.

**Continue through the complete authorized sequence without another general approval request.** Earlier no-Git restrictions governed the proof and manuscript-preparation tasks; this order authorizes the specified publication operations. Stop only for a concrete unresolved content conflict, preservation problem, inaccessible required service, or rejected access/approval action. Complete unaffected work and report the precise blocker.

The task ends with the verified publication receipt. No new investigation, common-phase reconstruction, runtime integration, release/tag creation, DOI deposit, or announcement is commissioned.

## 2. Source of truth, baseline, and destinations

Use Command Prompt and the Windows source of truth:

~~~bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
~~~

Repository:

~~~text
https://github.com/pzychozen/trioctagon-physics
~~~

The reviewed preparation workspace is:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PAPER_01
~~~

The accepted review ZIP is NATIVE_POTENTIAL_INFORMATION_PAPER_01_REVIEW_PACKAGE.zip. Its SHA-256 is:

~~~text
e2392100a77d1443f3158248d826e67698ce28d2034108d20f545e21020dab2c
~~~

Its 16-page review PDF has SHA-256:

~~~text
48172f3b82e46352bb727af674aacdc958d278a3685a902299382990dc238083
~~~

The operative review is NATIVE_POTENTIAL_INFORMATION_PAPER_01_GPT_REVIEW.md, dated 2 November 2026: scientific content accepted; R1 required; R2 recommended and now included in this finalization order. Use its downloaded copy if present. This order records the operative disposition and exact edits, so a missing downloaded review file does not require another author search or scientific review.

Create a fresh external execution workspace:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PUBLISH_01
~~~

Use a new dated suffix if that directory already contains work. Preserve the reviewed ZIP, its original extraction, accepted proof notes, and their existing research directories. Prepare a separate final-edition copy in the new workspace.

The authorized repository destinations are:

~~~text
papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/README.md
papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/
README.md
~~~

The canonical final PDF is:

~~~text
papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/
  NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf
~~~

Only the new paper subtree and one bounded discoverability addition to the root README are authorized tracked changes. Check the live checkout and destination before writing. Do not overwrite an already populated immutable v0.1 edition with different content.

## 3. Exact manuscript finalization

### R1 — restore the local hypothesis in the abstract

In the final copy of manuscript/main.tex, replace the single sentence:

~~~tex
On the admitted positive in-phase triad branch, strict normal stability implies strict local descent modulo common phase.
~~~

with:

~~~tex
On the admitted positive in-phase triad branch with \(g>0\), strict normal stability implies strict local descent modulo common phase.
~~~

The condition already appears in Theorem 3.1 and Table 1. This changes the abstract's summary, not the accepted theorem or proof.

The reviewed main.tex SHA-256 is:

~~~text
8ef4c6c58e8c9561931947b3fb1609ba7a78766ecff70b85e68aff669f72126e
~~~

Applying only R1 to those bytes gives ad1ebcd8c475bd69f3adc9fc738a6cb409a5208e2e16e4290256710ec14f7537. That is a single-edit reference, not the expected hash after the edition-status changes below.

### R2 — cite the existing sector distinction

In manuscript/discussion.tex, replace the existing sentence about the preceding 60-degree sector with:

~~~tex
That domain is distinct from the \(60\)-degree finite-return sector noted in \cite[Section~8]{energy} and from any spatial cone angle.
~~~

The energy bibliography key and supporting proof-note section already exist. No new source recovery or bibliography entry is needed.

If either exact edit is already present in a newer candidate, verify it and do not duplicate it. Reconcile any other source difference against the reviewed baseline before adopting it.

### Current-edition status and names

Use **Research edition v0.1** in the running header, and **Author-authorized repository research edition v0.1** where a fuller description is useful.

Update the active PDF subject, title-page edition line, review-status paragraph, current README, and current claim/source ledger. A suitable cover-status statement is:

> Author-authorized repository research edition v0.1. Project-internal scientific review completed; author publication approval granted. No external peer review is claimed.

The review and authorization occurred on 2 November 2026. If execution occurs later, record the actual finalization/publication date separately rather than changing the historical review date.

The four active main.tex status locations are the PDF subject, running header, title edition line, and paragraph saying the assembled manuscript awaits review. Attribution may additionally record GPT's manuscript review. Preserve the author name and the distinction from external peer review.

Rename the current PDF output to NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf. Update active links, build destinations, document-check targets, and packaging names consistently. Keep the PDF at the edition root alongside evidence/ so its proof-note links resolve.

### Preserve historical records

The original PREPARATION_REPORT.md, review work order, accepted notes, GPT review records, original review manifest, and old build/inspection receipts describe earlier stages. Their historical wording remains true. Do not globally replace “review,” “pending,” or “unpublished” across the evidence.

Preserve the original review archive outside the final payload. Any historical report retained inside the publication must be clearly labelled as historical from the active README. Create new finalization/build/inspection records for the rebuilt edition rather than relabelling the old checks.

The bibliography's unpublished-investigation labels describe the supporting proof notes. Do not invent separate publication metadata for them.

The comma correction is already complete. Preserve the corrected information note, its before-copy, and its receipt unchanged; do not repeat that edit.

## 4. Final package and build

Produce a portable edition containing:

- The final PDF and all ten editable manuscript source files.
- A current README with exact build instructions.
- The current claim/source ledger, with accepted scientific classifications retained and review/authorization metadata updated.
- The two namespaced accepted proof/helper/result sets.
- Relevant existing source snapshots, source provenance, original comma-before-copy, and correction receipt.
- A new FINALIZATION_REPORT.md and PUBLICATION_DISPOSITION.md recording the approved changes, review decision, author authorization, and pre-publication checks.
- Fresh final build and inspection records tied to the final PDF/source hashes.
- A final payload manifest with an exact file list, byte lengths, and SHA-256 values; it excludes itself.
- Necessary document-only build/verification utilities and the operative orders/review records when available.

The scientific evidence files are archival. Do not execute their helpers, import repository runtime modules, or run simulations, root solves, trajectory checks, parameter searches, or prior certificates.

The reviewed build/inspection/packaging utilities contain hardcoded review filenames. Adapt publication copies or replace them with a small equivalent document-only workflow. Do not let a final build silently regenerate the old REVIEW PDF or treat review receipts as final-edition checks.

Use the installed cached Tectonic/Poppler toolchain and existing environment. The successful preparation compiler was:

~~~text
C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe
~~~

Retain the document-build protections and cached resources already used. No package installation or persistent environment reconfiguration is required.

Before adoption:

1. Diff the final manuscript against the reviewed sources. Changes must be confined to R1, R2, edition/status/attribution wording, links/build targets, and necessary presentation repairs. Preserve the scientific bodies of the other sections.
2. Compile until references and citations resolve; confirm R1 is visible in the abstract and R2 resolves correctly.
3. Inspect every page of the rebuilt final PDF. Sixteen pages is the reviewed baseline, not a mandatory count. Record the actual count and any harmless pagination change.
4. Verify source/PDF/build hashes, relative evidence links, ledger references, and final edition metadata.
5. Confirm that retained evidence, primary-source snapshots, and comma-provenance bytes remain consistent with their recorded identities.

These are finalization checks. No second full scientific investigation or general manuscript approval is required for the authorized edits.

Keep rendered page PNGs, font caches, unneeded TeX intermediates, duplicate build PDFs, and machine-local scratch files outside the committed payload.

The pre-commit publication disposition may state that publication is approved and finalization checks passed. Actual push success, remote verification, and the resulting commit belong in the later external receipt.

## 5. Discoverability

Create the new paper landing README with the title, author, edition/status, bounded contribution summary, and relative links to the final PDF, edition README, source, ledger, and publication disposition.

Add one standalone-paper entry to the repository root README near the existing collective-turning/coherence research entries. Preserve the surrounding content and all unrelated wording. A suitable entry is:

~~~markdown
## Native potential descent and closed coherence coordinates

[Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map — v0.1](papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/README.md), by **Hilmir Frímann Halldórsson**. Author-authorized repository research edition with completed project-internal scientific review; no external peer review is claimed. [Final PDF](papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf). Local native-potential descent, an explicit coherent-domain decrease bound, and autonomous coherence coordinates with attained minimum counts in the stated pair-entry dictionaries. No runtime changes.
~~~

Do not rewrite the historical paper index, prior publication statuses, root licensing, or other research sections. Repository visibility does not create a new licence; preserve the existing licensing scope.

## 6. Repository preparation and preservation

Read applicable local instructions and inspect the actual branch, expected origin, remote ancestry, and pre-existing staged/unstaged work before adoption. Record the baseline and preserve unrelated changes.

Fetch the current origin/main. Historical reading commits in the paper are citations, not checkout/reset targets.

Use a clean publication context. If the original checkout has unrelated changes, staged entries, or unpushed commits, create an isolated publication worktree/branch from the freshly fetched origin/main under the external execution workspace. This is authorized. Keep the original checkout's branch, index, and working files intact.

Do not publish unrelated local commits, reset or clean the user's checkout, change the origin URL, or sweep unrelated work into this commit.

Copy the frozen final package into the authorized new subtree and add the bounded root README entry. Freeze an explicit allowlist of every intended committed path before staging.

Inspect the staged path list and content diff. It must match that allowlist. Stage exact paths; do not broadly stage the repository or commit pre-existing unrelated index entries.

Verify staged blob bytes against the frozen payload, especially retained scientific evidence. If Git text/filter settings would change retained bytes, use narrowly scoped attributes inside the new paper subtree and include that attributes file in the allowlist. Do not change repository-wide attributes or configuration to accommodate this publication.

An existing destination with different published content is a concrete conflict: preserve it and report the conflict. An already identical published payload should be identified and verified rather than duplicated.

## 7. Commit and normal push

Create one ordinary publication commit. Suggested message:

~~~text
Publish native potential descent and closed coherence paper v0.1
~~~

Confirm that the commit contains exactly the allowlisted paper payload and root README addition. Verify that it introduces no unintended deletion, runtime change, unrelated publication change, or extra commit history.

Push normally to origin/main. From an isolated publication branch, an explicit normal push of HEAD to main is appropriate:

~~~bat
git push origin HEAD:main
~~~

No force push, history rewrite on the remote, amend of prior published work, or bypass of repository protections is authorized.

If main advances during execution, fetch it and preserve those changes. A clean replay of only this task's unpublished publication change onto the new remote base is authorized; resolve an unambiguous independent README insertion without another general approval request. Stop for a substantive unresolved conflict rather than widening the payload or forcing the push.

Record the resulting full commit SHA. Confirm the publication commit is present on origin/main. If another normal commit subsequently advances the branch, distinguish that later tip from the immutable publication commit.

## 8. Fresh remote-byte verification

Enumerate every file changed by the actual publication commit, including the paper landing README, root README, and any subtree attributes file.

For each committed path, fetch fresh bytes using its immutable full-commit URL, for example:

~~~text
https://raw.githubusercontent.com/pzychozen/trioctagon-physics/<FULL_COMMIT_SHA>/<REPOSITORY_PATH>
~~~

Compare the downloaded byte length and SHA-256 with the committed blob and the approved payload. Verify the PDF as binary bytes. Cover every committed file; checking only the PDF or the edition manifest is insufficient.

Moving main URLs, cached pre-push files, and the local working tree alone do not establish remote-byte agreement. Report the actual verified count and any mismatch. If access is temporarily blocked, retain the successful push receipt and identify exactly what remains unverified; do not claim completed verification.

No historical publication-wide audit or scientific rerun is needed.

## 9. Receipts, archive, and final return

Keep the actual commit-bearing PUBLICATION_RECEIPT.md and REMOTE_BYTE_VERIFICATION.json in the external execution workspace. They are written after the commit/push and must not trigger a second commit merely to record the first.

Record:

- Actual execution dates, original/review/final identities, and the exact R1/R2/status changes.
- Final title, edition, page count, PDF size/hash, build/inspection result, and final source/package identities.
- Full publication commit, normal push result, expected origin, branch/worktree used, and remote verification count.
- Every committed path with expected and fetched sizes/hashes and per-file result.
- Preservation of unrelated work and original accepted/review artifacts, with any concrete limitation stated.
- Immutable links to the final PDF and edition directory, plus convenient current-main links.
- Any actual unresolved issue; otherwise an unambiguous completed-publication verdict.

Create an external closeout archive:

~~~text
NATIVE_POTENTIAL_INFORMATION_v0.1_PUBLICATION_CLOSEOUT.zip
~~~

Include the final published payload, this order, the available manuscript review, finalization records, and the completed external receipt/remote verification. Compute its checksum afterward and place it in an adjacent file. Neither the archive nor a committed manifest should contain its own final hash.

Do not put the resulting commit SHA in a file intended to be part of that same commit. The external receipt supplies that link without a recursive commit/hash dependency.

Return a concise completion message with the full commit link, immutable PDF/edition links, final page count, verified file count, and local paths to the publication receipt and closeout archive.

**The author has approved this complete bounded publication. Finish with the verified closeout and stop.**
