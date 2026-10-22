# SRG_VOLUME_I_PUBLICATION_STATUS_CLOSEOUT_01

**Scientific lead:** GPT  
**Author / owner:** Hilmir Frímann Halldórsson  
**Investigator:** Codex  
**Date:** 22 October 2026  
**Scope:** One publication-status consistency correction. No scientific investigation and no Git publication.

## Decision and objective

The submitted publication package passes the independently checked integrity, accepted-content comparison, evidence-copy, local-link and PDF comparison checks. Scientific acceptance and editorial E01/E02 closure remain in force.

Close **PUB-01**, a remaining current-status inconsistency, then return the resealed publication payload. Do not reopen the science or reconstruct the simulations again.

Submitted package identities:

- Review ZIP: `SRG_VOLUME_I_v0.1.1_PUBLICATION_REVIEW.zip`, 60,467,308 bytes, SHA-256 `5647a1f99d291ba7f893f6bd08ecd60a546d4748cef836353e982ca0dc0980db`.
- Publication manifest: SHA-256 `d7ff67b5b1383f8d8d38b17f6081ab7c5234f66b22ff70b9948eda7b08d9ccab`.
- Submitted publication PDF: 3,712,951 bytes, SHA-256 `0ed0b424a4121f0892589bd4837820d1fcfda4c2042006073760e41bfe3aaae8`.

These identify the pre-correction submission, not a future approved hash.

## Working locations and protection

Authoritative repository:

`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`

Publication working copy:

`SRG_REDISCOVERY\PAPERS\SRG_SIMULATION_RECONSTRUCTION_VOLUME_I\publication\v0.1.1`

Use a new narrowly scoped closeout workspace under `SRG_REDISCOVERY\PUBLICATION_WORK` for the new work order, comparison and delivery records. Preserve the submitted ZIP and its old identities. A distinct closeout ZIP filename must not overwrite the submitted ZIP.

The accepted `VOLUME_I_01_R1` directory, its accepted PDF/archive, earlier volumes and studies, all original evidence, canonical ledger, existing root/SRG READMEs, kernels and unrelated working material remain unchanged. The existing publication working copy may receive only the changes below and their necessary generated records. Continue with edition v0.1.1; do not invent a new scientific edition.

## PUB-01 — exact correction

### A. Current manuscript statement

`MANUSCRIPT/sections/01_scope.tex`, lines 104–105, currently ends its C07 paragraph with:

> This manuscript itself is a draft awaiting review.

It appears on physical PDF page 9, printed page 3. It conflicts with the accepted cover and current section 6.6.

Replace that sentence only with:

> Scientific and editorial review is complete; publication requires separate authorization.

Retain the preceding account of the historical ledger and preserved in-review snapshot. Retain `\claim{C07}`. Keeping the same source-line count is preferred so existing source locators remain stable; validate rather than assume it.

### B. Current claim registers

Update **only current review-status metadata** for C07 and C102 in both `CLAIM_EVIDENCE_MATRIX.md` and `records/claims.json`.

- C07 currently says `manuscript remains in review`. Record completed scientific/editorial review, retained provenance qualifications, and separate publication authorization instead. Retain the original work-order/ledger references for the historical SIM03 status and add the preserved GPT editorial-closure receipt as support for the current manuscript status.
- C102 currently describes the volume as ending at review and cites only the earlier draft-stage authority. Align it with the already-correct section 6.6: scientific/editorial review complete; wider SRG unfinished; publication and further experiments separately authorized. Cite the editorial closure and publication work order as current authority, retaining earlier references where explicitly historical.

Keep all 102 IDs, classifications and scientific entries. Do not modify the other 100 claim records. Keep manuscript locations correct. Do not change section 6.6 again unless a purely administrative locator correction becomes necessary.

Historical manifests, study documents, ledger snapshots and the embedded accepted archive must retain their historical review wording unchanged. The accepted appendix descriptions are already contextualized by the publication build/access guides; no unrelated cleanup is requested.

### C. Verifier and preparation descriptions

The current `tools/verify_publication.py` expects only two changed TeX files and byte-identical accepted `records/claims.json`. Adjust those exact comparison conditions narrowly:

1. Permit the additional C07 sentence replacement in `01_scope.tex`, explicitly checking that the rest of that file equals the accepted content.
2. Permit only the documented C07/C102 status/support wording changes in the claim JSON; require all other records and IDs to remain unchanged. Classifications and valid source locations remain required.
3. Preserve every existing scientific-content, evidence, figure, manifest and link check. Do not bypass checks or merely loosen assertions until they pass.

Refresh descriptions that enumerate changed files or claim strict byte identity of the entire current claim JSON. Provide an exact before/after diff for every authored change. This is a static publication-integrity checker, not an authorization to rerun scientific verification.

## Build, verify and reseal

Use Windows Command Prompt and `conda activate torment`. Reuse the verified compiler/cache in an isolated short-path build workspace; do not rebuild or overwrite the accepted edition.

Rebuild the publication PDF from the corrected publication source. Compare it with the submitted publication PDF and inspect affected pages and any reflow. Keep all equations, numerical results, 17 figure includes, 35 image assets, three original program copies, and all 374 accepted study payloads unchanged. Preserve all evidence qualifications, especially the formally UNLINKED movie/log relationship.

Refresh publication PDF identity, claim locations if needed, content/link checks, source-input/build correspondence, visual receipt, exact publication diff, checksums, manifests, exact staging proposal and review ZIP. Report actual counts and hashes; do not reuse stale receipts.

Do not demand a whole new scientific review. The return package should identify PUB-01 closure and make its restricted diff easy to verify. Preserve previous review evidence as provenance rather than silently rewriting it.

## Return and stop

Return:

- A short `PUBLICATION_STATUS_CLOSEOUT.md` explaining PUB-01 and listing changed paths.
- The corrected PDF, complete resealed publication review ZIP, exact staging list and updated identities.
- Updated static verification and preservation receipts, with a compact diff against this submission.

No simulations, trajectory generation, scientific checker reruns, dependency experiments, new evidence, canonical-ledger updates, README edits outside the publication copy, staging, commits, pushes, releases or publication.

**Stop for a narrow final check of PUB-01 and the corrected payload identities. Owner authorization to publish is still required.**
