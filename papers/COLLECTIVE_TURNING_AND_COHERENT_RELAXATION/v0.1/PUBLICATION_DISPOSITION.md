# Publication disposition — v0.1

**Title:** *Transient Collective Turning and Coherent Relaxation in the Native Triad*  
**Author:** Hilmir Frímann Halldórsson  
**Edition:** Repository research edition v0.1 — 28 October 2026  
**Mathematical source baseline:** `ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade`

## Review and authorization

The author-supplied [publication work order](evidence/PUBLICATION_WORK_ORDER.txt), dated 28 October 2026, records completion of GPT scientific review of the assembled manuscript with no substantive mathematical or presentation blocker, completion of author review, and explicit author authorization to commit and push this edition to `pzychozen/trioctagon-physics`.

The status is **author-authorized repository research edition v0.1, with completed GPT project-internal scientific review and author review**. No external peer review is claimed. No DOI, journal placement, release, tag, new Paper A–G letter, change of repository visibility, or licensing change is authorized or implied.

The author's observation and programme, GPT's scientific steering and project-internal review, and Codex's mathematical, computational, and drafting assistance remain attributed in the manuscript. The scientific baseline above identifies the cited mathematics; it is not the publication commit. Git records the commit that publishes this edition.

## Approved editorial finalization

1. **§4, witness chronology:** “This parameter choice preceded the witness search; the constructed entrance is” became “This parameter point was fixed before evaluating the witness; the constructed entrance is”. The retained account establishes selection before evaluation, without documenting a witness-search process.
2. **§6.3, current phase width:** “Rotate the current phase interval to its bisector.” became “Let Δ ≤ D₀ be the width of the current phase interval, and rotate this interval so that its bisector is the positive real axis.” The source uses the existing LaTeX notation.

Cover, running header, PDF metadata, current disposition and attribution statements, edition README, and claim/source map now record the completed reviews and repository edition. The historical [preparation handoff](REVIEW_HANDOFF.md) received only a dated superseding notice; its original account is otherwise byte-preserved. The original manuscript work order, six retained scientific evidence files, original provenance, and historical verification records are unchanged.

No equations, numerical values, proof arguments, theorem domains, or conclusions were changed. All displayed equation environments and mathematical token blocks are preserved, apart from the approved new inline definition of Δ. Exact replacements are recorded in [publication_editorial_changes.json](verification/publication_editorial_changes.json).

The manuscript retains the separate full-map turning witness, phase-off graph comparison, and finite-domain convergence theorem. It does not assert capture of the turning entrance, a physical force or magnetic-field identification, historical recovery of the remembered numbers, or an unrecorded onsite-only example.

## Artifact identities

| Artifact | Reviewed draft SHA-256 | Final repository edition SHA-256 |
|---|---|---|
| `main.tex` | `c4f898fe097c8df4bd4fddc1e2010d0e5b0c78dc63e43deec460485c4db3315c` | `40b6ca84ca136453b045386e2dead012fc8fcd7984b845d159ae6d6c8a6c2292` |
| `REVIEW.pdf` | `e7a884bb7fe63483667f07fe46404d116f622d90e61b5e91c705c073e89ea52a` | `f4edad99d9c6933a93e6aadd0346b1d4e73c0beed41c6589300cf546fc3d2022` |

The final PDF has **21 pages**. `REVIEW.pdf` is the single canonical published PDF filename, retained by explicit instruction; it no longer denotes a pending-review artifact. The reviewed manifest is retained separately as [reviewed_manifest.json](verification/reviewed_manifest.json). The [final manifest](PACKAGE_MANIFEST.json) identifies the publication payload and the single root README addition.

## Bounded final document checks

- Confirmed the starting manuscript and PDF matched the author-supplied reviewed hashes and the reviewed inventory.
- Rebuilt with the existing Tectonic 0.17.0 and established retained-data figure/table workflow, using Windows Command Prompt after `conda activate torment`. Final compilation completed with zero warnings. The build record binds the final PDF to the final source and unchanged bibliography.
- Inspected all final rendered pages for clipping, overlap, missing glyphs, and pagination defects; none was found. The inspection is recorded against the actual final PDF hash and page count, independently of packaging.
- Checked equation/reference/citation resolution, required inputs, relative evidence links, affected Markdown links, PDF source/evidence links, PDF metadata, and correspondence with the final source.
- Compared the six scientific checker/receipt files with their original provenance hashes: all unchanged. The bibliography, figure-generation source, numerical tables, original work order, original provenance, historical verification records, and historical verifier are also unchanged.
- Restricted the publication allowlist to this edition directory and one compact appended root README entry. Local status inventories, compiler intermediates, rendered page images, source-inspection helpers, transfer ZIPs, and unrelated research are excluded.

Current records are [publication verification](verification/publication_verification.json), [build record](verification/publication_build_record.json), and [visual inspection](verification/publication_visual_review.json). Historical preparation checks retain their original scope and artifact hashes; their old HEAD/index assertions are not applied after publication.

The packaging utility was adjusted to require an existing inspection record tied to the current PDF, use the actual page count and edition status, and calculate a final explicit payload manifest. It does not manufacture an inspection PASS or generate a redundant transfer archive.

No scientific checker, simulation, parameter sweep, root solve, kernel test suite, completed publication audit, or new mathematical investigation was run. Protected kernels, accepted papers, unrelated working-tree content, and licensing terms remain outside this publication change.
