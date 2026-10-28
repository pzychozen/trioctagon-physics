> **Historical preparation record — notice dated 28 October 2026.** GPT scientific review and author review are complete, and repository publication is authorized. The earlier pending-review statements below describe preparation only. Current status, final artifact identities, and publication checks are recorded in [PUBLICATION_DISPOSITION.md](PUBLICATION_DISPOSITION.md).

# GPT scientific review handoff

**WORKING REVIEW DRAFT — prepared for GPT scientific review and author review; publication pending those reviews.**

Title: *Transient Collective Turning and Coherent Relaxation in the Native Triad*.

Author: Hilmir Frímann Halldórsson. Date: 28 October 2026. Edition: local review draft v0.1. Mathematical baseline: `ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade`.

## Review materials

- [Rendered manuscript](REVIEW.pdf): 21 pages, including cover, contents, appendices, and bibliography.
- [Canonical LaTeX source](main.tex) and [bibliography](references.tex).
- [Claim/source map](CLAIM_SOURCE_MAP.md).
- [Evidence guide](evidence/README.md) and [copy/source provenance](evidence/PROVENANCE.json).
- [Verification receipt](verification/verification_receipt.json), [build record](verification/build_record.json), and [visual review](verification/visual_review.json).
- [Build instructions](README.md).

The review ZIP contains these materials, figure sources and vector outputs, generated data tables, all six retained evidence files, and a payload manifest. Temporary compiler intermediates, page images, source-inspection helper, and unrelated checkout-status metadata are excluded.

## Central claims

1. The retained two-step full-map witness has strictly positive signed mean turning while an exact amplitude ratio changes. Conjugation supplies matched handedness reversal. Its passive W observable changes. Turning survives the single synchronization-off comparison.
2. On the separately labelled lambda=0 matched comparison, the graph coefficient cancels from the first complete mean step, but influences the second through the onsite response. The exact response is a cubic polynomial in g. At g=1/60, J<0, R>0, and Q>0: the second increment changes direction and shortens while the signed-turn statistic decreases.
3. Separately, the full ordered map preserves the stated annulus and ordinary narrow sector. Its phases converge, its aligned amplitude map contracts, and the decaying phase-width error yields convergence to the unique positive amplitude profile in the specified cube, up to limiting common phase. Residual spread is positive; C, W, and Gamma vanish.
4. Uniform bounds along the prescribed coefficient path justify connection to the accepted unequal branch. The earlier turning entrance is outside the convergence domain. No capture, sustained-motion, physical-force, or magnetic-field identification is asserted.

## Reused evidence and availability

All six requested files were available, inspected, copied unchanged, and hash-checked:

- `turning_witness_20261028.py` and `.json`;
- `delayed_graph_response_20261028.py` and `.json`;
- `moving_mean_domain_constants_20261028.py` and `.json`.

No checker was rerun. Figures 1 and 2 use retained values; Figure 3 is explicitly schematic. Generated tables print recorded enclosures. The analytical convergence proof has no root-solve or trajectory dependency.

The optional earlier onsite-only fixed-channel-phase counterexample was not present as a standalone record among those retained files. It was not reconstructed or asserted to have been inspected. Appendix C discloses this limitation. No required receipt is missing. The author's recollection is attributed to the supplied work order, not to an invented historical transcript or recovered equation.

## Review findings and requested assessment

No concrete mathematical inconsistency was found during drafting. This statement is a preparation finding, not GPT approval of the assembled manuscript.

Please review the synthesis for faithful scope, especially the phase-off/full-map distinction in §§3–5, the convex-hull proof in §6, the exact domain and branch identification in §§7–8, and the non-identification boundaries in §§9–11. The treatment of the author's recollection and the omission of the optional unlocated example are explicit editorial/provenance points. These are review targets, not new research assignments.

## Checks actually performed

- Verified the eight relevant repository source files against pinned Git blobs and recorded their SHA-256 identities.
- Compared every copied evidence file with its original bytes and recorded hash. Checked stored exact fractions and certified turning/ratio values against the manuscript; generated numerical tables directly from the receipts.
- Checked the delayed-response expansion, real derivative, phase-stage bounds, radial bounds, convex-hull estimate, mismatch term, contraction constants, geometric convolution, observable limits, and branch-continuation argument during transcription. This is a mathematical reading, not a new certificate replay.
- Resolved all 69 LaTeX labels, all citations to 15 bibliography entries, relative evidence/input links, and PDF URI links. The three external textbook references were inspected at their publisher pages. Pinned project links identify existing Git objects; no repository publication audit was reopened.
- Built with the existing Tectonic 0.17.0 in Command Prompt after `conda activate torment`. Final compiler warnings: zero. The Codex desktop LaTeX compiler also returned success.
- Rendered all 21 pages with Poppler and visually inspected the complete final page set, including equations, long fractions, tables, figures, captions, title, contents, and bibliography. Corrected overlapping figure labels and a table/paragraph interruption before the final build. No remaining clipping, overlap, unresolved reference, or missing-glyph defect was found.
- Checked the final PDF text and retained external/evidence links. Approximately 8,823 whitespace-separated extracted tokens include prose, formulas, table cells, headers, and bibliography; this is not a prose-only word count.
- Verified HEAD, branch, staged diff, tracked diff, and outside-draft Git status against the local starting record. Git's default Windows status walk reports pre-existing long-path omissions in unrelated untracked directories; that status comparison is not a recursive byte audit of all unrelated material. All task writes were confined to this new draft directory.

No native or production kernel, accepted paper, repository index, branch, commit, or remote publication was changed. Nothing was staged, committed, pushed, tagged, released, or submitted as a PR. No simulation, parameter sweep, certificate broadening, root solve, new attractor search, or additional mathematical investigation was performed. GPT scientific review and author review come next; publication remains pending those reviews.
