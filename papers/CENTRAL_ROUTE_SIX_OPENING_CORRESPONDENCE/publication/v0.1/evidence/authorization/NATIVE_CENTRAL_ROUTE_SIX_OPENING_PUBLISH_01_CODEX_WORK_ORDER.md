# Codex work order — minor fixes, final verification and publication

**Task:** NATIVE_CENTRAL_ROUTE_SIX_OPENING_PUBLISH_01  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Author:** Hilmir Frímann Halldórsson (pzychozen)

## 1. Authorization and completion target

The author requests:

> prepare the next work order that is minor fix and push correct?

**GO: complete the three specified manuscript corrections, finalize publication status, rebuild and verify the corrected document, then publish it to `origin/main` in one ordinary scoped commit and verify the remote result.** Proceed through that sequence once the document checks pass; another routine GPT or author approval round is not required.

This order supersedes the earlier local-manuscript restrictions against Git/push and the instruction to return the corrected PDF before publication. It also supersedes `publication_authorized:false` as a current restriction. Preserve those earlier records unchanged as historical evidence of the review state at that time; record the later authorization through this order and `AUTHOR_PUBLICATION_GO.json`.

The mathematical foundation C01–C05, Q01 and S01–S05 remains accepted. The submitted manuscript required M01–M03 and was not accepted unchanged. GPT now gives a scoped publication GO contingent on those exact repairs and the final document checks below. Do not claim GPT has independently inspected an as-yet-unbuilt revised PDF. Codex's correction and final-document verification supplies the explicitly authorized closeout.

This task ends with an actual publication receipt, immutable links, corrected PDF identity, fresh remote-byte comparisons, and actual CI results. It does not commission another scientific investigation.

## 2. Workspace and publication identity

Use **Command Prompt**, **`conda activate torment`**, and the existing Python 3.11 / cached Tectonic workflow.

Research workspace:

`C:\TORMENT\TRIOCTAGON_new\research\NATIVE_CENTRAL_ROUTE_SIX_OPENING_PAPER_01`

Repository:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Remote: `https://github.com/pzychozen/trioctagon-physics`  
Branch: `main`

| Identity | Required value |
| --- | --- |
| Title | Central-Route Accounting and Six-Opening Geometry in the Reciprocal Chiral Exchange Candidate |
| Author | Hilmir Frímann Halldórsson (pzychozen) |
| Edition | v0.1 |
| Canonical PDF | `CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE_v0.1.pdf` |
| New paper root | `papers/CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE/` |
| Edition directory | `papers/CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE/publication/v0.1/` |
| Existing repository file to update | Root `README.md`: one additive catalog entry for this paper |

Fetch and inspect the actual current `origin/main`. The retained `c3ee366bd6195bd7fa77efd0321214af4c2dc173` checkpoint identifies earlier consulted sources; it is not a claim about the current branch tip. Preserve unrelated local work by using an isolated publication checkout/worktree based on the fresh remote tip. Read applicable repository instructions and retain normal branch protections.

## 3. Inputs and prepared replacements

The reviewed initial PDF has 17 pages, 196,911 bytes and SHA-256:

`5cca7c826776fc935dd3e20fa74088221fe2c18e7862569024b5045c8322866b`

The submitted manuscript review ZIP has SHA-256:

`61b673652d7cd42b4ad6359bea6cb1ff8b73a9fe185391d17ec2dbdd31580f7e`

The complete GPT review/correction packet is preserved under `inputs/`, with SHA-256:

`58587bc73e7aed40d514dcb2c10da4340759c8875ba53ae1c9a9c62b865f1abe`

That nested packet includes the original submitted PDF and complete review archive, accepted evidence, actual GPT review and page inspections. Its historical stop-before-publication instructions are superseded only by this later order's bounded GO.

The top-level `edits/` directory supplies **six complete replacement source files**: the three M01–M03 section files and three files for publication-status group P01. `edits/EXPECTED_EDITS.json` records their before/after identities, and `edits/EXACT_FIX_AND_STATUS_EDITS.patch` shows every prepared edit. Check the before-hashes against the existing candidate and apply the prepared copies or identical substitutions. A file already matching its after-hash can be retained as completed. Resolve a different starting version by inspecting its actual diff; do not overwrite unrelated changes blindly.

## 4. Required manuscript repairs — M01–M03

### M01: complement notation

In `candidate/v0.1/sections/03_account.tex`, `eq:regionalbalance` (original equation (3.9), page 7), change:

```tex
I_{R_B}^{,c}
```

to:

```tex
I_{R_B}^{c}
```

The complementary-work term, its sign and the native-jump convention remain as proved.

### M02: fixed forcing support

In `candidate/v0.1/sections/04_launch.tex`, immediately after `eq:duhamel` (original page 8), replace the sentence claiming that every integrand has fixed support, together with its following “Therefore,” by:

```tex
Nevertheless, at every forcing time $t'$, the unshifted forcing $Bq(t')$ is supported in the same fixed union $\Sb$. A backward characteristic from a point at circular distance greater than $ct$ cannot meet this support during the integration interval. Therefore
```

The unshifted forcing has fixed support; the Duhamel integrand is translated. The existing formula and support-gap conclusion are correct. Preserve Q01, its inner-gap example, the active-port qualification and the receiving theorem.

### M03: width convention in C6

In `candidate/v0.1/sections/06_transport.tex`, the paragraph after `eq:C6` (original Section 6.4, page 13), replace the sentence applying the width-scaled bound to the width-one distance by:

```tex
For a fixed point on any specified $G$ boundary or individual hull in the width-one static configuration used in \eqref{eq:C6}, Theorem~\ref{thm:separation} guarantees $d_X(s)>297/5000$. For a commonly scaled carrier and central geometry, with the arclength interval scaled accordingly, the corresponding distance is strictly greater than $297\wh/5000$.
```

This makes the common-scaling assumption explicit. Preserve the separation theorem, observation formula, fixed-point/static-family and supplied-history conditions, and absence of loading. The result still does not define or calculate a physical aperture flux.

## 5. P01 — publication-status housekeeping

The prepared P01 replacements update `main.tex`, `build.py` and `BUILD.md` without changing scientific content. Use the consistent current status:

**Research edition v0.1 — accepted mathematics; author-authorized repository publication**

The title-page preparation note ends with:

> This edition is an author-authorized repository research publication. The accompanying review and correction records state the scope of project-internal review; no external peer review or formally verified proof is claimed.

Keep the title, accented author name, edition and original preparation date correct. Record actual new build and publication timestamps separately. The PDF subject, visible status, build receipt and current build instructions must agree. Preserve earlier “review pending” records in historical evidence; do not rewrite the original GPT decision into an unconditional acceptance of the old PDF.

Create a current `PUBLICATION_STATUS.md` stating the actual sequence: accepted mathematics; GPT manuscript review requiring M01–M03; verified completion of the repairs and final document checks; author authorization through this order. This status must not predict a commit SHA, successful push or remote verification before those events occur.

## 6. Rebuild and final document verification

Apply M01–M03 and P01, then perform the existing document-only build using cached/untrusted Tectonic and external intermediates. Existing figure bytes can be reused. Make only layout adjustments needed by the corrected text and record any such adjustment.

Before publication:

1. Confirm all three repairs and the status changes against the prepared diff. Keep all eleven required claim items, the ball/cylindrical-radius distinction and the accepted hypotheses intact.
2. Record final source hashes, build log, actual build time and PDF identity. Check title/author/version/date/status metadata, text extraction, embedded fonts, labels, citations and warnings.
3. Render and inspect **every page of the final revised PDF**. Record its actual page count; do not presume that it must stay 17 pages. Bind the inspection to that final PDF's SHA-256.
4. Refresh the claim ledger's current source paths, lines, labels, numbers and pages, and the notation/source maps where affected. Historical source registries retain their original scope. Published source locators must resolve to actual files or explicitly named retained archive members.
5. Produce a prepublication correction closeout recording M01, M02, M03 and P01, the exact final artifact identity, checks actually performed and their results. The separately delivered PDF and the publication PDF must be byte-identical.

The earlier scientific suites do not need to be replayed. These edits change wording, notation and publication status, not the accepted model or conclusions. If a concrete scientific contradiction or an unresolved required document check appears, report that specific blocker; routine implementation and layout choices are within this order.

## 7. Assemble and freeze the repository payload

Use the edition root for the current relative build layout: canonical PDF, `main.tex`, `references.tex`, `sections/`, `figures/`, `build.py` and `BUILD.md`. Add the paper-level and edition-level READMEs, current publication status, provenance, accepted evidence, final document verification summaries and a self-excluded `PUBLICATION_MANIFEST.json`.

Preserve and make the accepted C/S proofs and dispositions, Q01, actual GPT manuscript review, author GO and correction closeout available through the edition's evidence layout. Keep the source files or archive-member references needed by its claim ledger accessible and record any path mapping. Preserve the original submission and fuller audit material in the external closeout. Large nested outer review packets, transient caches and redundant page renders need not all be duplicated into Git merely to preserve provenance.

Append one concise catalog entry to the root `README.md`, following the current repository style. Describe the two scoped conclusions and link the new paper/edition/PDF. Preserve the entire pre-existing README baseline as a prefix and add the entry once. Existing paper editions and application/kernel files are outside the publication change set.

Before staging, freeze the exact intended bytes, file modes and complete allowed path set. Verify the copied publication PDF and editable source against the final built candidate. The new publication manifest inventories the actual payload; it does not overwrite historical source manifests or include itself recursively.

## 8. One normal commit and push

The staged change set must contain only:

- The new `papers/CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE/` tree.
- The single additive root `README.md` entry.

Review the complete staged diff and compare it with the frozen payload. Record the baseline/parent commit and confirm other existing paths retain their file modes and Git identities. If the proposed new destination already contains a different tracked edition, preserve it and resolve the concrete collision before publishing.

Make **one ordinary single-parent commit**, for example:

`Publish central-route and six-opening correspondence v0.1`

Push normally to `origin/main`. If the remote advances, reconcile with the fresh tip while retaining the same scoped payload and preserving others' changes. Do not force-push, rewrite published history, bypass branch controls, create a tag/release, or make unrelated edits. No receipt-only follow-up commit is needed.

## 9. Verify the published bytes and actual CI

After the successful push, independently retrieve **every changed path**, including root README, from fresh URLs pinned to the **full new commit SHA**. Compare each actual response body with both its frozen intended bytes and its committed Git blob. Retain the fetched bodies in the external closeout and record path, URL, observation time, HTTP outcome, byte count and SHA-256.

Verify the commit's parent/tree and complete changed-file set, handling pagination. Confirm the publication commit is on `main`. If the branch subsequently advances, state that accurately instead of claiming that the publication is still its tip.

Inspect the actual workflow/check results for this new SHA. Report successful, failed, pending, skipped or untriggered checks as observed; an empty legacy status aggregate is not evidence that required CI passed. Follow any actual required checks through to their outcome before reporting a fully successful closeout.

The postpublication receipt and fresh-download evidence stay outside the committed payload, avoiding a self-referential receipt or unnecessary second commit.

## 10. Return the completed publication

Return:

- Immutable commit, edition and canonical-PDF links, plus the current `main` PDF link.
- The final corrected PDF's pages, bytes and SHA-256.
- `PUBLICATION_RECEIPT.md` and a machine-readable counterpart with correction closeout, scope/preservation results, fresh remote verification count and actual same-commit CI outcomes.
- A complete external closeout ZIP and its SHA-256 checksum, retaining the original review, current author GO, final build/inspection records and fresh remote-byte evidence.

Use a concise final report: **M01–M03 completed, final document verified, one scoped commit pushed, N/N changed paths verified, actual CI outcome.** Report any real execution limitation plainly. Do not claim a successful push or complete remote verification unless it was observed.

**Completion means the corrected paper has been published and verified. The instruction to stop for another routine manuscript-approval turn has been superseded by this order.**
