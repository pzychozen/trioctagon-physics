# XW-01 — generated crosswalk encoding repair

**Review disposition:** The 11-page manuscript/PDF is accepted unchanged. Apply this one documentary correction before publication. This note and its replacement file do not themselves authorize commit or push.

## Exact target and replacement

Target within the candidate edition:

    verification/CROSSWALK.json

| Version | Bytes | SHA-256 |
|---|---:|---|
| Submitted | 41800 | `bb281be227450cc753de9ffe3bfb2963395b8aee0ab108caa2a3c939c5595dc6` |
| Reviewed replacement `CROSSWALK.json` beside this note | 41639 | `b7e22b38e18e4911cbcda19c38e758af82617c108020d2829487e9a6574d1b8c` |

The generated `accepted_record` objects contain UTF-8 text decoded as Windows-1252: for example `Â§` instead of `§`, and `â€“` instead of `–`. There are 30 affected string fields across rows I01–I15 and N01–N07. The 26 FA records, all 107 manuscript locators and all other JSON fields are unchanged. The preserved original accepted crosswalk is already correct and must not be edited.

The replacement restores each `accepted_record` directly from:

    evidence/issued_packet/accepted/CLAIM_CROSSWALK.json

Original accepted crosswalk SHA-256:

    b1dec3d53021431bd591154a6f145716dfe35a3249aedc8e8ba1d9d7b5287e84

`XW01.patch` displays the exact text changes; `XW01_VERIFICATION.json` enumerates every affected field and records the independent equality checks. CRLF line endings are preserved. This is not a change to a mathematical statement, source reference number, equation, hypothesis or PDF.

## Bounded closeout

1. Verify the submitted target identity, replacement identity and unchanged original accepted-crosswalk identity. Stop on a conflicting target rather than applying a blind encoding conversion.
2. In a fresh publication-preparation copy, replace only the generated `verification/CROSSWALK.json` with the supplied bytes. Keep the submitted review ZIP unchanged as the historical candidate. Do not run a blanket encoding replacement through evidence or other files.
3. Verify all 48 `accepted_record` objects equal the corresponding original entries, all manuscript locators and remaining fields are unchanged, and no PDF, TeX, build-helper or accepted evidence bytes changed. If regenerating metadata, read the original JSON explicitly as UTF-8; default Windows text decoding must not reintroduce the defect.
4. Refresh the active candidate/publication manifest, prospective allowlist and any hash-bound gate or verification record that covers the corrected file. Preserve historical manifests under their recorded scopes; do not falsely certify an old manifest against new active bytes. Record the XW-01 closure and the separate source-archive reconciliation in current provenance.
5. Preserve the accepted PDF at SHA-256 `e337a9b59488b7f1dc4ac1371150e7b5d69d168d7b230dcd665ccb61bade1318` and all ten TeX files. **No rebuild, new visual pass, scientific rerun or manuscript rewrite is required for this metadata repair.** Existing page inspections remain tied to unchanged PDF bytes.

The replacement itself has already been reviewed. The resulting metadata identities must be checked, but this correction need not cause another manuscript review round. It may be included in the eventual scoped Stage B publication order once the author gives explicit publication GO. Stage B otherwise remains locked. The final committed-file count may differ from the Stage A prospective count after authorized publication wrappers and review receipts are added; use the actual frozen allowlist.
