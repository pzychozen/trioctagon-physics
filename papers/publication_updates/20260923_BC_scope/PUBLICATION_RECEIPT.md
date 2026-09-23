# Finished publication / preservation receipt

23 September 2026. Codex-attributed bounded follow-through to the supplied GPT order. **Status: ready for review of the finished publication contents; no concrete blocker. No staging, commit or push.**

GPT accepted D v0.1.1 within its stated scientific scope and approved the five passages. Codex applied and typeset them, checked preservation and reproduced the new B/C PDFs in an isolated copy. GPT's review is not represented as a review of these new PDF bytes or the local execution/package results.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| B publication v0.1.2 | 13 | `5555eb4f07b0974addced80339bf0f87bb7a5ab87d268926f321a3c586da35ad` |
| C publication v1.0.1 (scientific baseline v0.3.1) | 16 | `5869fb7b98784fab00e8b63f225f84c03277bbd4bac3534c0773df9efed156d1` |
| Approved D v0.1.1, unchanged | 26 | `7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf` |

The [exact disposition](CHANGE_RECORD.md) records B-S1/B-S2 and C-S1/C-S2/C-S3 with anchors and page locators. Source restoration recovers the complete preceding manuscripts apart from terminal whitespace. All original mathematics, parameters, measurements, proof bodies and figure assets are unchanged. C's display block 8 retains its preceding mild scale; no new equation scaling occurs. All 29 final pages passed visual inspection. No kernel, geometry, algebra, atlas, simulation, figure-generation or corpus program was rerun.

## Actual reproduction and package results

The minimal isolated copy used exactly eight committed dependencies from `08c2a79739d540ffe1cab4743284052e2aa7214b` plus the 196 proposed files. Existing Python 3.12.14/pypdf, Pandoc 3.11, Tectonic 0.17.0, explicit populated resource caches and system fonts were the only external prerequisites; no source-workspace fallback or installation. Both PDFs and generated TeX are **byte-identical**. The same bounded verifier passed in isolation, including relative Paper-D PDF annotations and source bibliography links. D was only hash-verified, never regenerated. [Isolated receipt and input identities](evidence/isolated_reproduction.json) separate this new replay from prior reviews. Final administrative receipt synchronization is separately recorded in [the final isolated package check](evidence/final_isolated_package_check.json); no build input changes are permitted at that step.

Read-only package checks pass: preserved D v0.1 (64 hashes / 65 paths), current D v0.1.1 (70 hashes / 71 paths), whole B package (139 hashes / 140 paths), B's ten unchanged supporting implementation/provenance paths and 21 source-input hashes. The combined manifest has 195 hash entries and covers all 196 proposed paths except itself. No science is executed by these hash checks.

## Exact publication classes

| Class | Paths |
|---|---:|
| Preserved D predecessor | 65 |
| D v0.1.1 revision | 71 |
| B new publication source/PDF/references/build evidence | 13 |
| C new publication source/PDF/references/build evidence | 13 |
| Existing navigation and B package manifests | 5 |
| New review, comparison, replay, receipts and bounded tools | 29 |
| **Combined** | **196** |

[Explicit combined list](COMBINED_PUBLICATION_ALLOWLIST.txt); [individual path classes](PUBLICATION_CLASSES.json). The original D 136-path list is reused unchanged. The new editions reuse B figures already in the committed baseline. No environment, cache, font, preview, dataset, unrelated untracked work or external continuity file belongs to the list. D's current README/disposition/manifest are administrative updates among its 71 revision paths, not new science. The preceding D and B metadata/manifests are preserved as small byte-exact before-images.

## Preservation and current Git state

Starting HEAD = final HEAD = local `origin/main` = `08c2a79739d540ffe1cab4743284052e2aa7214b` on `main`. This is the locally recorded tracking ref; no network fetch was needed or performed. Index is empty. Five tracked administrative files are modified: root README, CURRENT_STATE, B README, B allowlist and B checksums. All tracked edits and new untracked paths are within the combined proposal. Earlier unrelated untracked work remains present and outside it; full status is in the [path-level receipt](evidence/preservation_and_git.json). The working tree is intentionally not clean.

All **878 protected baseline files** are byte-identical. Exactly **11 existing files** were authorized metadata/continuity edits: eight repository paths (the five tracked administrative paths plus D's three untracked metadata files) and three existing continuity records outside the repository. The prior recovery record is an exact byte prefix. All Paper-A files, previous B/C editions, D's approved and predecessor PDFs, source/figure assets, kernels and earlier execution evidence retain their baseline identities. The root archive manifests remain frozen snapshot receipts; they are not silently replaced with new-publication manifests. The tracked diff passes CRLF-aware `git diff --check` without staging.

The unchanged supporting implementation identities remain in `papers/PAPER_B/SUPPORTING_SHA256SUMS_v0.1.1.txt`; their verification is reported in [the read-only checks](evidence/final_package_check.json). These are preserved dependencies, not new implementation edits or newly run tests.

Updated continuity locations, outside this publication list:

- `C:/TORMENT/TRIOCTAGON_new/reconstruction/KERNEL_SOURCE_TO_MODEL.md`: later publication disposition before the preserved snapshot.
- `C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/TOY_MODEL_SPECIFICATION_AND_PROOF_CATALOGUE_v0.1.md`: later publication disposition, with implemented/research distinction unchanged.
- `C:/TORMENT/TRIOCTAGON_new/reconstruction/continuity_closeout_20260922/PROJECT_STATUS_RECOVERY.md`: appended acceptance and completed five-item publication receipt.

The current model does not acquire scaffold placement, a physical gap-energy law or restored Z/torus functionality. Accepted SRG reduction/orientation results remain intact. No new Claude review or broader joint acceptance. No staging, commit, push, tag, release or DOI. Stop at this publication checkpoint.
