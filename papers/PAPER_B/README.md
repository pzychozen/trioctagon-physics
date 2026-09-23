# Paper B publication revision v0.1.1

The active deliverables are the [manuscript](PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.1.md), [publication PDF](publication/v0.1.1/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.1.pdf), [symbol/theorem sheet](PAPER_B_SYMBOLS_AND_THEOREMS_v0.1.1.md), [references](PAPER_B_REFERENCES_v0.1.1.md) and [reference ledger](PAPER_B_REFERENCE_LEDGER_v0.1.1.md).

The user-relayed GPT review accepts the mathematical content of the identified 13-page v0.1 PDF within its stated scope. Revision v0.1.1 closes BIB-01 and corrects availability/reproduction documentation; its changed bytes are a separate publication revision. No theorem, model assumption or kernel equation changes. No new Claude review is asserted.

## Three reproducibility claims

A. The mathematical argument is self-contained and can be read without executing code.

B. Paper regeneration requires the publication sources, committed geometry and declared Python/Pandoc/Tectonic prerequisites. C. Appendix A implementation replay also requires the separate supporting implementation/provenance list. The paper-only list is not a complete code release.

The exact [dependency and command guide](RELEASE_DEPENDENCIES_v0.1.1.md) distinguishes these claims and justifies each supporting path. It documents the isolated baseline-plus-proposal check, existing tool prerequisites, and public commands. No environment was installed or upgraded during finalization.

## Proposed release contents

- [Paper allowlist](PROPOSED_GIT_ALLOWLIST.txt)
- [Supporting implementation/provenance allowlist](PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt)
- [Paper checksums](SHA256SUMS.txt)
- [Supporting checksums](SUPPORTING_SHA256SUMS_v0.1.1.txt)
- [Existing validation report, with appended finalization](CODEX_PAPER_B_PUBLICATION_VALIDATION_v0.1.md)
- [Final preservation and Git receipt](PAPER_B_PRESERVATION_AND_STATUS_v0.1.1.md)

The committed baseline plus both lists is the proposed paper-and-code release. Nothing is staged, committed, pushed or remotely published. Approval of these exact contents remains Hilmir's next decision.

## Reviewed identity and current commands

The complete 44-file reviewed package is preserved byte for byte in reviewed_v0.1, including its PDF, allowlist, source, build scripts and earlier evidence. The original v0.1 PDF and versioned documents also retain their bytes at their previous paths. Old evidence and instructions are historical; publication_config.json selects the active v0.1.1 filenames.

The reviewed PDF SHA-256 is 431569d08bab58bb5e2cd08e17b0fd7bafe56066cf1a29fa54dad98ea25e40dc. The reviewed allowlist SHA-256 is a1695213b1ddad30d88e6440b13206dd84a6db55953bdb568426ed52e7fd46dc. Neither identity is assigned to the revised PDF or expanded allowlist.

check_package.py is a public read-only check of the saved package and supporting files. build.ps1 invokes the four paper reproduction commands. runtime_smoke.py exercises one existing face-state step. closeout.py is local-only: it checks original protected paths and the historical repository, then refreshes maintainer receipts and manifests. It is not needed in a fresh checkout.

Ignored .build contains local intermediate files only. No environment, TeX cache, font, binary, textbook PDF or unrelated dataset belongs to either allowlist. Sources and outputs of the five figures are unchanged; no presentation redesign was needed.
