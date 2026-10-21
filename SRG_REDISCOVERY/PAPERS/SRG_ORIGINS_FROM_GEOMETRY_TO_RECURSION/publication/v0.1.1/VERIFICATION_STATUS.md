# Verification status - SRG Origins v0.1.1

This record separates retained mathematical evidence from the document and publication checks performed on 21 October 2026.

## Retained mathematical evidence

The original paper-local checker run at **2026-10-21T03:54:49.044663+00:00** recorded **59/59 passing results**. The checker and its result JSON are copied byte-identically from the reviewed draft into `checks/`. That run used Python 3.11.15 in `torment`, SymPy 1.14.0 and mpmath 1.3.0 with 80-digit numerical precision. These results are **retained, not freshly rerun for publication**. Neither the project scientific modules nor historical simulations were imported or executed during publication finalization. This record does not enlarge the scope of the original checks or turn exploratory interpretation into physical validation.

## Source and document verification performed

- The corrected Markdown and TeX source identities were matched to the author-approved clarity-edit receipt before copying. The approved positive-constant-coefficient wording and the complete first-person interpretation paragraph remain verbatim. Every displayed equation and equation tag is unchanged. The full line-level publication diffs are retained under `records/`; they contain only edition, approval and verification-status wording.
- The final standalone TeX compiled successfully with the desktop compiler. The exported PDF was built with Tectonic 0.17 from the existing cached bundle, using untrusted mode and two reruns. The final source, compiler and PDF identities are recorded in `records/EVIDENCE_IDENTITIES.json`.
- The final PDF has **29 pages**, matching the corrected review PDF. All 29 rendered pages were visually inspected. Apart from the running header, body changes occur on physical pages **1, 6, 15, 17 and 26**. There is no resulting pagination change, clipping or overlap.
- All **24 external PDF URI destinations**, in order, are identical to the reviewed PDF. The **11 outline titles and destination pages** are unchanged, and internal links resolve to valid pages. The reference pages were visually checked. This is document-reference preservation, not a new external-source or mathematical audit.
- The log has one retained underfull-box warning in Section 6.3, whose rendered paragraph was inspected and is legible. There are no overfull-box, missing-character or undefined-reference warnings.

## Preservation and publication scope

All **8 files** in the frozen `publication/v0.1/` edition and **528 files** in the existing `revisions/v0.1.1/` review workspace match their pre-publication SHA-256 identities and inventories. Those review records, including older draft markers and review ZIPs, remain historical records. The prior edition is not relabelled or rebuilt.

The explicit publication scope is the new `publication/v0.1.1/` payload and the new paper-level `../../README.md` index. The out-of-scope working-tree status matches the initial inventory. No kernel, historical original, central-crystal/Z/chirality work, or unrelated tracked change is included. Only this explicit allowlist is staged; the private build and verification workspace is excluded.

`PUBLICATION_MANIFEST.json` gives SHA-256 identities for all other files in this edition and the paper index. It excludes its own hash to avoid self-reference. The scoped commit and post-push receipt identify the manifest itself and verify the remote payload. The receipt is created after publication and retained separately; this pre-commit record does not assert that a push has already succeeded.
