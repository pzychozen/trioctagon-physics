# Codex work order — finalize and publish the phase-reconstruction/spatial paper

**Task:** NATIVE_PHASE_SPATIAL_PUBLISH_01  
**Date:** 2 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson / pzychozen  
**Scientific direction and manuscript review:** GPT  
**Execution:** Codex  
**Authorization:** APPROVED through bounded cleanup, finalization, one ordinary commit, normal push, and remote verification

## 1. Author decision and endpoint

The author has approved the reviewed manuscript's publication with the bounded cleanup:

> Proceed toward publication with that bounded cleanup included.  
> make that order for codex

Publish **Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map**, author-authorized repository research edition **v0.1**.

GPT's manuscript review accepted the commissioned mathematical scope and found no blocking mathematical, source-integrity, or rendered-document defect. The author now authorizes all six editorial items E1–E6 below, final edition/status changes, document rebuilding and inspection, scoped repository adoption, one ordinary publication commit, a normal push to `origin/main`, and fresh commit-pinned verification of every committed file.

**Continue through this complete sequence without another general approval request.** Earlier no-Git restrictions governed the investigation and manuscript-preparation tasks. This order authorizes the specified publication operations. The endpoint is the verified publication receipt and closeout archive.

Read applicable local instructions and preserve the standing scientific directions and author-involvement boundaries. The current author instruction authorizes this bounded publication; it does not select a material attachment or commission a further investigation. If a substantive decision actually falls outside the order, state:

> **Pause here: what is established, what are you proposing to add or change, and what exact decision do you need from me?**

Identify the concrete conflict or proposed expansion and finish unaffected work. Routine editorial implementation, final document checks, isolated-worktree creation, and the authorized commit/push do not need another approval.

## 2. Baseline, source of truth, and destinations

Use Command Prompt and the existing Windows environment:

~~~bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
~~~

Repository: `https://github.com/pzychozen/trioctagon-physics`.

Reviewed preparation workspace:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_SPATIAL_PAPER_01
~~~

Verify these accepted baseline identities before copying:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `NATIVE_PHASE_SPATIAL_PAPER_01_REVIEW_PACKAGE.zip` | 351,716 | `3c8880d301fc673102347e2bfdc8eb8af59e5445ae05f180f1d6f68bb0075edb` |
| `NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf` | 138,693 | `8eb97758c893254827d984bc32d6893fcf866b5cd6639876e35d9014520853a6` |

The review PDF has 13 pages. The operative review is `NATIVE_PHASE_SPATIAL_PAPER_01_GPT_REVIEW.md`, dated 2 November 2026, SHA-256 `dee1ec02ee4f2d63575c42f589c73d4233607ad730597357875fe34baeb94e1b` (18,688 bytes). The preparation order is `NATIVE_PHASE_SPATIAL_PAPER_01_CODEX_WORK_ORDER.md`, SHA-256 `f6b760cc9f0a6cbd48fa8ee47081663ec92a90ec7ad88df4178c6484684e6a10` (20,854 bytes).

Use those orders/review copies if available. This order supplies the operative disposition and complete cleanup instructions; a missing downloaded GPT review does not require another author search or review cycle. Do not reconstruct a missing historical document and present it as the original.

Create a fresh external execution workspace:

~~~text
C:\TORMENT\TRIOCTAGON_new\research\NATIVE_PHASE_SPATIAL_PUBLISH_01
~~~

Use a dated suffix if occupied. Preserve the reviewed ZIP, original extraction, accepted investigation directories, and previous publication workspace. Prepare a separate final-edition copy. Reconcile unexpected baseline differences before adopting them.

Authorized repository destinations:

~~~text
papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/README.md
papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/
README.md
~~~

The canonical final PDF is the edition-root file:

~~~text
papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/NATIVE_PHASE_SPATIAL_v0.1.pdf
~~~

These are the proposed publication destinations, not an assertion about the live repository. Inspect them before writing. Preserve any already populated immutable edition with different content. If this exact task has already been published, verify the matching publication instead of duplicating it.

## 3. Exact approved editorial cleanup

Apply E1–E6 only to the final-edition copy. Check each target in context before replacement and inspect the resulting diff. If an edit is already present, verify it rather than applying it twice.

### E1 — distinguish local output angles from positive roots

In `manuscript/reconstruction.tex`, restrict this rename to the proof of Theorem 3.2 (`thm:phasebranch`), through that proof's `\end{proof}`:

| Location | Existing expression | Final expression |
| --- | --- | --- |
| Output-lift definition | `b_i=\psi_i+\delta_i` | `\beta_i=\psi_i+\delta_i` |
| `eq:anchorhalfplane` | `\cos b_1` | `\cos\beta_1` |
| Branch-identification sentence | `\vartheta=b_1` | `\vartheta=\beta_1` |
| Relative-phase prose | `b_i-b_1` | `\beta_i-\beta_1` |
| `eq:ordinarychannels` | `b_i-b_1` | `\beta_i-\beta_1` |

The reviewed proof has seven affected symbol occurrences in these five locations. Preserve equation labels, bounds, signs, and proof structure. Preserve all positive-root `b_2,b_3` definitions and uses in `setting.tex` and elsewhere, and the observer's separate scalar blend coefficient `\beta`. Do not make a global symbol replacement.

### E2 — describe asymptotic amplitude convergence

In the final paragraph of `manuscript/reconstruction.tex`, replace:

> Amplitudes still relax until \(r_*\) is reached.

with:

> The amplitudes converge toward \(r_*\).

No finite-step arrival is asserted.

### E3 — name the representative-dependent bounds precisely

In the final paragraph of `manuscript/overlap.tex`, replace:

> the canonical width or absolute-variation bounds

with:

> the canonical pointwise increment bounds or absolute-variation bounds

Preserve the gauge identities, phase-width definition, and tail estimates. Common rephasing preserves relative phase width; this refinement concerns the section-relative increments and their bounds.

### E4 — allow aligned and fixed-state exceptions

Make all three prose qualifications:

1. `manuscript/main.tex`, abstract: replace “The complete native step also changes amplitudes and relative phases.” with “The complete native step can also change amplitudes and relative phases.”
2. `manuscript/spatial.tex`, before `eq:channelincrement` / equation (5.9): replace “An actual native step changes \(y\) as well.” with “An actual native step can change \(y\) as well.”
3. `manuscript/observations.tex`, §7.3: replace “An actual native step additionally changes their lengths and relative phases” with “An actual native step can additionally change their lengths and relative phases”. Preserve the following comma and proper-rotation conclusion.

The exact update formulas remain unchanged.

### E5 — preserve the sphere/toroid distinction

In `manuscript/observations.tex`, §7.3, replace this complete sentence:

> The close original enclosing sphere and separately discussed tight toroid are different proposed structures; two co-present arrangements and rapid alternation remain different alternatives.

with:

> The close original enclosing sphere is a fixed geometric reference; the separately discussed tight toroid remains a distinct intended feature. Two co-present arrangements and rapid alternation remain different alternatives.

Preserve the rest of the interpretation boundary. The paper does not select material attachment, identify mathematical arrow endpoints with material features, or supply a body-motion law. Keep stationary reference lines, central broken arcs, and host-notch patches distinct.

### E6 — explain the optional checker's dependencies

In the edition `README.md`, after the optional `manuscript/verify_document.py` command, add:

> This optional checker is a preparation-machine audit: it expects the original source paths recorded in the source manifest and the local rebuild's log and receipt. The portable manuscript can be compiled independently of that audit.

The checker currently needs the original Windows paths in `provenance/source_manifest.json`, a fresh `build/main.log`, and `build/build_receipt.json`. E6 does not commission a cross-platform scientific verifier. Keep the explanation accurate if the final document workflow uses an adapted utility; clearly identify any retained original checker as historical.

## 4. Final edition status and document tools

Use **Research edition v0.1** in the running header and **Author-authorized repository research edition v0.1** where a fuller description is appropriate. A suitable status paragraph is:

> Author-authorized repository research edition v0.1. Project-internal scientific and manuscript review completed; author publication approval granted. No external peer review is claimed.

Update these active locations consistently:

- `manuscript/main.tex`: PDF title and subject, running header, title-page edition line, cover review-status paragraph, and attribution as appropriate to the completed GPT manuscript review.
- `manuscript/observations.tex`: final attribution/status paragraph currently returning the manuscript for review before publication. Preserve its scientific limits.
- Edition `README.md`: current status, canonical PDF filename, build instructions, contents, and final verification records.
- Current `CLAIM_SOURCE_LEDGER.md`: heading/status, final “§7.3 and draft status” row, and any editorial-history wording affected by the approved edits. Preserve scientific source/dependency classifications.

Preserve the accented author name. Review and author approval occurred on 2 November 2026; record a later actual execution date separately if needed.

Update active output names, links, and document checks to `NATIVE_PHASE_SPATIAL_v0.1.pdf`. Keep the PDF at the edition root beside `evidence/`, preserving the four relative evidence references.

**Preserve historical truth.** Do not globally replace “review,” “draft,” “pending,” or “unpublished.” Original proof records, source snapshots, work orders, preparation reports, review manifests, and earlier build/inspection receipts retain their original bytes and status. Supporting unpublished research-note labels do not require invented publication metadata. Preserve the original reviewed archive externally and clearly label any retained historical reports from the active README.

Adapt only publication copies of document utilities:

- `manuscript/build.py` and `manuscript/verify_document.py` hardcode the review PDF name; the checker also expects pending-review metadata. Update their final-edition targets/status assertions.
- Retain applicable checks for the four already incorporated manuscript corrections: full-state terminology, analytic differentiation, the normalized overlap factor, and complete EMA dependencies. Check assertions against the authorized text; do not restore obsolete wording to satisfy a draft-era assertion.
- **Do not rerun `package_review.py` unchanged.** It is a one-shot preparation utility assuming 13 pages, changed pages `[7, 10, 11]`, `first_visual_render_hashes.json`, and preparation placeholders. Use a small document-only publication workflow with fresh records and the actual final page count.
- `prepare_sources.py` and archived scientific helpers are not prerequisites for portable manuscript compilation. Do not rerun source preparation or scientific calculations.

The nine `.tex` sources are `main`, `setting`, `reconstruction`, `overlap`, `spatial`, `rotation`, `observations`, `witness`, and `references`. Keep `setting.tex`, `rotation.tex`, `witness.tex`, and `references.tex` byte-identical to the accepted baseline. If final layout reveals a necessary presentation repair outside the listed edits, document it precisely and preserve all mathematical content; a substantive scientific change requires the author boundary above.

## 5. Final build, inspection, and payload

Use the existing cached compiler and document tools in `torment`. The successful preparation compiler was:

~~~text
C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe
~~~

Retain the established cached/untrusted build protections, including `--only-cached --untrusted` where used. Record actual tool versions. No package installation or persistent environment reconfiguration is commissioned.

Before freezing the payload:

1. Compare final sources with the reviewed baseline. Account for E1–E6, active status/attribution, output/link/tool changes, and any necessary documented presentation repair. Verify the unchanged scientific files and evidence identities.
2. Compile until references and citations resolve. Confirm all six edits and final metadata in their intended locations.
3. Render and inspect **every page of the final PDF** for clipping, overlaps, missing glyphs, unreadable tables, equation layout, headers, and references. Thirteen pages is the baseline, not a required count. Record the actual page count and any harmless pagination change.
4. Verify final PDF/source/build hashes, bibliography resolution, relative evidence links, ledger references, and PDF metadata. Record fresh final checks; do not relabel the original review inspection as a final-edition inspection.
5. Confirm all nine phase/spatial evidence members and retained primary-source snapshots preserve their recorded bytes. Reading and hashing archival code is authorized; executing it is outside this task.

The final edition should contain:

- The canonical PDF, all nine editable `.tex` sources, and necessary document-only build/verification utilities.
- A current README and claim/source ledger.
- Unchanged namespaced `evidence/phase/` and `evidence/spatial/` proof/helper/result/source-identity files.
- Existing compact primary-source snapshots and their provenance manifest, plus relevant orders and available GPT review.
- Clearly identified historical preparation records, without duplicate old PDF/archive payloads.
- New `FINALIZATION_REPORT.md`, `PUBLICATION_DISPOSITION.md`, and fresh records under `verification/`, tied to the final PDF and sources.
- `PAYLOAD_MANIFEST.json`, listing exact edition member paths, byte lengths, and SHA-256 values; exclude the manifest itself from its hash list.

Keep original historical records intact wherever retained, and record their original locations if reorganized. Update active links accordingly. Exclude rendered page PNGs, font caches, TeX intermediates, duplicate PDFs, absolute-path scratch files, and obsolete preparation-only packaging requirements from the active publication workflow.

The precommit disposition records approved publication and completed finalization checks. Actual push success and the resulting commit belong in the later external receipt. Freeze the payload after document checks; if any payload file changes afterward, update its dependent checks/manifest before committing.

No native trajectories, scientific helper reruns, project/runtime imports, observer or EMA execution, root solves, parameter searches, new certificates, material interpretation, or runtime integration are commissioned. No second general manuscript review is needed for the authorized cleanup.

## 6. Paper landing page and repository discoverability

Create the paper landing README with title, author, edition/status, a bounded contribution summary, and relative links to the final PDF, edition README, manuscript sources, ledger, and publication disposition.

Add one concise entry near the related native-research papers in the root README. Suggested content, adapted only to the surrounding Markdown structure:

~~~markdown
[Phase Reconstruction and Stationary Support Axes in the Tri-Octagon Map — v0.1](papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/README.md), by **Hilmir Frímann Halldórsson**. Author-authorized repository research edition with completed project-internal scientific and manuscript review. [Final PDF](papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/NATIVE_PHASE_SPATIAL_v0.1.pdf). Exact common-phase reconstruction, corrected overlap accumulation, stationary support-axis correspondence, and the fixed-label, state-independent proper-rotation theorem on the admitted domain. No external peer review is claimed.
~~~

Preserve surrounding content, prior papers, licensing scope, and unrelated indexes. Do not claim an established material attachment, body dynamics, a native period, or an unrestricted rigid-rotation impossibility.

## 7. Repository preparation and exact commit scope

Inspect applicable repository instructions, origin URL, branch, index, working files, and remote ancestry. Fetch current `origin/main`; historical cited commits are not reset targets.

Use a **fresh isolated publication worktree/branch from the fetched `origin/main`**, under the external execution workspace. This is authorized and preserves the original checkout's branch, index, working files, unrelated modifications, and unpushed commits. The preceding publication deliberately preserved an earlier original checkout; do not reset it merely to match the remote.

Copy the finalized paper into the new subtree and make the single bounded root README addition. Freeze an explicit allowlist of every intended committed path. Authorized tracked scope is the new paper subtree plus that root README edit; narrowly scoped byte-preservation attributes inside the new subtree are permitted if needed.

Stage exact paths. Inspect staged names and content; they must match the allowlist and frozen payload. Verify staged blob sizes/hashes, particularly archival evidence. If Git text/filter behavior would alter required bytes, address it locally within the new subtree and include the attributes file in the allowlist. Do not change repository-wide configuration or attributes.

Preserve the user's original checkout and previous publication worktrees. Do not reset, clean, indiscriminately stash, sweep unrelated files into staging, publish unrelated local commits, or change the origin URL.

## 8. One ordinary commit and normal push

Create one publication commit. Suggested message:

~~~text
Publish phase reconstruction and stationary support axes paper v0.1
~~~

Confirm its exact path/content diff and committed blob identities against the frozen payload. Ensure it includes only the authorized new paper files, the bounded root README addition, and any approved subtree attributes.

Push normally:

~~~bat
git push origin HEAD:main
~~~

No force push, remote history rewrite, amendment of earlier published work, or bypass of repository protections is authorized. If remote main advances, fetch it and replay only this task's unpublished change onto the updated base. Resolve an unambiguous independent README insertion, then refresh the affected allowlist/payload checks. Report a substantive conflict rather than expanding the scope.

If access or a branch rule blocks the push, preserve the prepared commit and report the precise blocker. If automatic approval review rejects an action, identify the rejected action and stated reason. Do not report publication success until the authorized push succeeds.

Record the full resulting commit SHA and confirm that it is reachable from `origin/main`. A later remote tip may differ; distinguish it from this immutable publication commit.

## 9. Fresh remote verification of every committed file

Enumerate every path changed by the actual publication commit, including both READMEs and any attributes file. Fetch fresh remote bytes for each using the full immutable commit SHA:

~~~text
https://raw.githubusercontent.com/pzychozen/trioctagon-physics/<FULL_COMMIT_SHA>/<REPOSITORY_PATH>
~~~

For every file, compare byte length and SHA-256 across the frozen final payload, committed Git blob, and freshly fetched remote bytes. Treat the PDF as binary. Include the root README's exact committed contents in the frozen adoption records. Checking only the PDF or manifest is insufficient.

Record the actual verified count and every result. A moving-main URL, a cached pre-push copy, or the working tree alone does not establish remote-byte agreement. If retrieval fails after a successful push, state exactly what remains unverified and preserve the successful push evidence. Do not duplicate the commit to address a remote-read problem.

No audit of older publications is required.

## 10. External receipt, closeout archive, and final return

Write `PUBLICATION_RECEIPT.md` and `REMOTE_BYTE_VERIFICATION.json` in the external execution workspace **after** the commit/push. These records do not trigger a second commit merely to record the first.

Include:

- Actual execution dates; accepted baseline identities; E1–E6 and final-status changes.
- Final title, edition, page count, PDF byte length/hash, source/payload identities, and fresh build/every-page inspection results.
- Full publication commit, expected origin, worktree/branch, ordinary push result, and main-branch reachability.
- Every committed path with expected/fetched byte lengths and hashes, per-file result, and total verified count.
- Preservation of unrelated work and accepted historical artifacts, with any actual limitation stated.
- Immutable commit-pinned links to the final PDF and edition, plus convenient current-main links.
- An unambiguous completion verdict or the precise unresolved blocker.

Create the external archive:

~~~text
NATIVE_PHASE_SPATIAL_v0.1_PUBLICATION_CLOSEOUT.zip
~~~

Include the published payload, this order, the available manuscript review, finalization records, and completed external receipt/remote verification. Compute the archive checksum afterward and place it in an adjacent checksum file. Neither archive nor manifest should contain its own final hash.

Do not embed the resulting commit SHA in a file intended for that same commit. The external receipt provides the commit-to-artifact connection without a recursive identity problem.

Return a concise completion message with the full commit link, immutable PDF/edition links, final page count, verified file count, and Windows paths to the receipt and closeout archive.

**Finish with the verified publication closeout and stop.** No new research work order, fresh-chat handoff, release/tag, DOI deposit, announcement, or person-directed message is commissioned.
