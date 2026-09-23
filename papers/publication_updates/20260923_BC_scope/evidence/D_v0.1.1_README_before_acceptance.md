# Paper D v0.1.1 - bounded definition and provenance revision

**Delivery:** `publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf`, with complete Markdown and generated LaTeX sources. This revision implements §8 of the supplied `GPT_PAPER_D_SCIENTIFIC_REVIEW_v0.1.md`. GPT's disposition **ACCEPT WITH MINOR REVISIONS** applies to the preserved v0.1 and its stated scope. The changes below are Codex's follow-through; **GPT review of v0.1.1 and the A/B/C proposals is pending**. No new Claude review or joint acceptance is claimed.

The complete reviewed v0.1 remains untouched in the parent directory, including its 25-page PDF, scripts, figures, reports and logs. Its PDF hash is `cccac63811252d0e116ca471be9d835f9bb569b79acd4bbf7fe55a0c6daa1617`. The earlier short note and all protected science remain preserved.

## What changed

- **D-01:** ordered vertices, boundary and filled convex octagon are distinct objects (§4, equations (2), (2a)). The complete planar frames and finite vertical faces use the proper domain (§§11-12, 14).
- **D-02:** the closed residual hexagon is a half-plane intersection (§9, equation (16a)); the strict apex witness in (16b) explains why deleting only ordinary open triangle interiors is insufficient.
- **D-03:** the Z/torus lead is tentative. The saved longer reply is explicitly attributed as an author-adopted relay of assisted wording, not independent spontaneous recall or source verification (§16.1). Other historical candidates are not independently excluded by that relay.
- The public text clarifies observable-to-display versus physical position/energy, specifies **invertible** affine transformations, and removes the undisclosed-construction teaser from its conclusion. Internal scope remains in `UNRESOLVED_ITEMS.md`.
- The final reference block uses a smaller bibliography font to avoid a short spillover page. Scientific content is retained; all nine figure sources and all 27 figure assets are byte-identical to v0.1.

See `REVISION_DISPOSITION.md` for item locators and evidence counts. `ABC_PROPOSED_CORRECTIONS_v0.1.1.md` gives five precise proposed B/C scope additions; A needs no correction. The canonical A/B/C impact table is in the existing recovery record, not a replacement roadmap. No A/B/C manuscript, theorem, PDF or figure was changed.

## Verification and evidence

`evidence/gpt_review_v0.1/` preserves the three supplied review files exactly. The supplied 17 grouped algebra checks are **GPT-reported results**; the script was inspected and not rerun. New Codex output is separate: four bounded definition-check groups (49 evaluated predicates) and a fresh run of the manuscript's 12 checks, with 9/9 figure-asset groups. These counts are not counts of theorems. The earlier 31- and 42-predicate suites, prior 95-test implementation checkpoint and historical simulations were not rerun.

`evidence/abc_inspected_artifacts.json` binds the current A/B/C manuscripts, TeX and published PDFs to their unchanged commit blobs. `evidence/source_provenance.json` distinguishes retained historical trace evidence from sources read during this bounded revision. `PRESERVATION_RECEIPT.json` checks 810 protected file identities, including all 65 v0.1 public paths; three existing continuity records are the only authorized pre-existing record edits.

Run `python verify_package.py` for read-only hashes and exact revision-allowlist verification. Rebuilding uses `build.ps1` and already available Python/TeX dependencies; see `REPRODUCIBILITY.md`. No archive, environment or dependency cache is bundled.

## Proposed publication scope

`PROPOSED_GIT_ALLOWLIST.txt` contains explicit **v0.1.1-only** repository-relative paths. `COMBINED_PUBLICATION_ALLOWLIST.txt` is the explicit union of the preserved 65 v0.1 paths and this revision's paths for a later publication decision. The short-note package and the three external continuity records are outside this Paper D package allowlist. `SHA256SUMS.txt` binds this revision and excludes only itself; the preserved parent manifest binds v0.1.

Both lists are proposals, not staging authorization or publication receipts. All files are local saves. No staging, commit, push, tag, release, DOI, kernel change, new geometry, gap-energy law, broad archaeology or Claude campaign occurred.
