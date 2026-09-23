# Codex Paper B publication validation v0.1

Date: 2026-09-23. Scope: the requested Paper B publication package only.

**Manuscript scientific status: complete review draft, with self-contained proofs of the scoped mathematical claims.** The manuscript contains 12 narrative sections, an implementation appendix, two explicit adoptions and seven numbered propositions/theorems. It uses the corrected folded-face attachment and the current Paper A/C and Bridge I/II sources. Existing accepted results are identified as inherited; no new independent Claude review or joint acceptance of Paper B is claimed.

The central result is transported signed state-vector area. The transport has rank two ambiently, composes on all ambient inputs, and agrees with matched rotations on its tangent domain. Spatial and channel determinants remain separate. The explicit realizable C3 witness rejects direct Cartesian identification of the raw channel triple; it is not an obstruction to every separately defined representation map. Unequal-k and Arg0 limitations remain. Z has no imposed decay envelope; it need not decay.

**Actual bounded algebra verification: 25/25 check groups passed** with SymPy 1.14.0. These include all 27 ambient compositions, the nine signed-area entries, three generator actions, six channel permutations, the recurrence coordinate identity and the explicit witness. These are Codex manuscript checks, not a new experiment or substitute for the written proofs. Exact figure-source comparison passed for 24 panel vertices, 24 panel-map evaluations and three normals. No trajectory or parameter sweep was run.

**PDF publication status: 13-page, readable draft produced with Pandoc 3.11 and Tectonic 0.17.0.** All 26 displayed equations fit at their intended size without the fallback scaling. The final log contains no overfull box or missing-glyph warning. All five figures are reproducible vector PDFs with PNG previews. Consecutive page numbers, five captions, seven statements, nine bibliography tags and source/companion-reference correspondence are checked by verify_publication.py. See evidence/publication_verification.json for the final PDF identity and actual machine result.

The PDF was rendered with Poppler and visually checked at 90/110 dpi. The initial layout check found an overlong appendix path; printed filenames were shortened while full relative links remain in the symbol sheet. Figure label placement was adjusted and its cyclic slot row corrected to (AB, BC, CA). The main area theorem was kept together across the page break. The final bounded inspection covers pages 1, 2, 4, 5, 6, 7, 8, 9, 10, 12 and 13: title, all five figures, displayed recurrence/area/parity identities, implementation text, and references. Temporary renders stay under ignored .build.

**Bibliography status:** nine selected tags; four external references use the already checked Paper A/C records, and five identify the exact internal sources in the reference ledger. No new literature search or fabricated metadata. **BIB-01 remains open:** a precise external textbook locator for the orthogonal-complex/symplectic/Kähler-plane terminology. The paper states this editorial limit and supplies the elementary proof. No venue-specific production styling or external publication status is claimed.

**Exact contradictions:** none found in the scoped, corrected source claims. The figure-slot and appendix-layout fixes were publication-draft corrections, not repairs to the accepted model. Superseded full-ambient-rotation, unqualified common-phase and ambient-axial interpretations are not revived.

**Reproducibility and preservation:** evidence/rebuild_reproducibility.json records the actual repeat build comparison; evidence/preservation_status.json records the final 253-path hash/size/mtime comparison, source identities and Git checks. The original geometry, dynamics, boundary/SRG code, face adapter, historical kernel, Paper A/C and prior proof reports are preserved. No continuity record was replaced or edited.

**Git status:** complete package prepared locally only. PROPOSED_GIT_ALLOWLIST.txt is the exact later-commit path list, and SHA256SUMS.txt covers that package except its own checksum file. No file was staged, committed or pushed. Existing unrelated working-tree changes remain outside this allowlist. Publication authorization and any later referee review remain separate.


## GPT disposition and publication finalization v0.1.1 - 2026-09-23

This dated appendix updates the publication status above while preserving that earlier receipt verbatim. The user's finalization work order relays GPT's review of the complete original 13-page v0.1 PDF and acceptance of its mathematical content within the manuscript's stated scope. Codex verified both supplied identities before revision:

- Reviewed PDF SHA-256: `431569d08bab58bb5e2cd08e17b0fd7bafe56066cf1a29fa54dad98ea25e40dc`.
- Reviewed 44-path allowlist SHA-256: `a1695213b1ddad30d88e6440b13206dd84a6db55953bdb568426ed52e7fd46dc`.

All 44 reviewed files remain byte-identical in `reviewed_v0.1/`; the original versioned manuscript/PDF and earlier evidence also remain at their prior paths. The v0.1.1 PDF is a new publication revision, not the same bytes GPT inspected. No new Claude review or broader joint acceptance is inferred.

**Scientific preservation.** All 214 mathematical spans are byte-identical, with original LF line endings retained. Sections 1-9 and 11-12 retain their complete text. No theorem, model assumption, kernel equation, figure geometry or implementation byte changed. The revision changes the date/version, section 10 citation, Appendix A availability/reproduction prose, bibliography and an unnecessary reference-page break. Existing tangent/ambient, spatial/channel, parameter/zero and physical-interpretation qualifications remain intact.

**BIB-01 = CLOSED.** The primary source is Ana Cannas da Silva, *Lectures on Symplectic Geometry*, author revision January 2006, published in Lecture Notes in Mathematics 1764, Springer: [author revision](https://people.math.ethz.ch/~acannas/Papers/lsg.pdf). Verified locators in that revision are sections 12.1-12.2, printed pp. 67-68, standard structures and Definitions 12.1-12.2; section 16.1, printed p. 90, Definition 16.1. These support terminology and compatibility conventions, not the model-specific shell or transport. The new references and ledger contain the citation; no textbook PDF is bundled.

**Release dependencies.** Reading the self-contained mathematical argument (A), rebuilding figures/PDF and paper algebra checks (B), and executing the cited modern implementation (C) are now distinguished. `RELEASE_DEPENDENCIES_v0.1.1.md` justifies all ten supporting paths by actual imports, cited tests, the README fixture executed by a test, or exact provenance. The paper-only list does not provide the full cited implementation. Optional SRG/boundary helpers are included for transitive imports, not adopted as Paper B physics. No architecture was changed.

One exact [FA] report copy is proposed at `research/folded_face_state/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md`. Both original and copy have SHA-256 `ab5d572ca11bb8d8ecb2236f8521cc25e7b90b7569942303568bfa93d01b52e7`. The original and historical references inside it remain unchanged. No research folder, environment, cache, font, binary or unrelated dataset was bulk-copied.

**Actual isolated verification.** Codex assembled 70 committed files from baseline `a0875c493b23b7d1aaa718ea2b40aa17af9adcd2` plus exactly the two proposed lists, at the destination in `evidence/v0.1.1/isolated_release_check.json`. All seven commands passed: saved-package verification, paper algebra, figures, PDF build, public publication verification, runtime smoke and the three cited test modules. Paper algebra passed **25/25 groups**. Exact geometry comparisons passed for 24 vertices, 24 panel-map evaluations and three normals. All ten regenerated figure files and the publication PDF are byte-identical to the local final build.

Implementation replay separately passed its canonical-state, chirality and transported-area smoke and **39/39 existing cited tests**. All imported kernel modules resolved inside the minimal checkout. No UI, full scientific archive, trajectory sweep or upstream preparation experiment was required. Final non-executable report/manifests are synchronized after the run and checked with a read-only saved-package check; execution-input hashes remain unchanged.

Existing prerequisites were Python 3.12.14; paper libraries SymPy 1.14.0, mpmath 1.3.0, NumPy 2.5.3, Matplotlib 3.10.7 and pypdf 6.10.0; runtime libraries NumPy 2.3.5, SymPy 1.14.0 and mpmath 1.3.0; Pandoc 3.11 and Tectonic 0.17.0 with an explicitly named populated TeX cache. The builder used `--only-cached`. No environment was installed or upgraded. Tool/library paths are explicit prerequisites, not hidden scientific inputs. This tests baseline-plus-proposed contents with available tools; it is not a remote fresh-clone or clean-machine installation claim. Public commands are separate from local-only original-preservation checks.

**Final publication identity.** The revised PDF has **13 pages**, 26 displayed equations, seven statements, two adoptions, five captions and ten reference tags. All equations fit without scaling; there are no overfull-box or missing-glyph warnings. Poppler renders at 110 dpi were visually inspected on pages 1 and 11-13, covering the changed content. Acknowledgements and references share a readable final page. Figures retain the reviewed bytes.

- PDF SHA-256: `4a470019ca311d245c3d24e1a870d2ddaf4a25f3809ae2ee04d030d40a919d82`.
- Manuscript SHA-256: `19972277060588a3d3c3550a9cecc1274550bba14bed6e5e962b853054d13a07`.
- Generated TeX SHA-256: `d207e982a51c437e82d2d385651b86cf54c2725cf3fe17b11005bc78e9b61d66`.

The active manuscript and companions are versioned v0.1.1; `publication_config.json` selects them. The build record is `publication/v0.1.1/build_record.json`. Current verification, isolated logs, visual inspection and scientific-preservation receipts are under `evidence/v0.1.1/`.

**Preservation and Git.** All 253 originally protected files retain hash, size and modification time. The ten supporting files retain their recorded bytes, and the original validation report remains an unchanged prefix of this report. Modern HEAD remains `a0875c493b23b7d1aaa718ea2b40aa17af9adcd2`; the index and unrelated working-tree state are unchanged. Historical HEAD remains `6310de7ba1ef4f41ed6e7cd683cf9186585cdd11`, with unchanged status. `PAPER_B_PRESERVATION_AND_STATUS_v0.1.1.md` and its machine receipt record the checks.

The final paper list is `PROPOSED_GIT_ALLOWLIST.txt`; implementation/provenance is separately listed in `PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt`. Their checksum manifests are `SHA256SUMS.txt` and `SUPPORTING_SHA256SUMS_v0.1.1.txt`. No staging, commit, push or remote publication has occurred. The revision is prepared locally; Hilmir's approval of these exact contents is the next decision.
