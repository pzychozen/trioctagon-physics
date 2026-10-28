# Transient Collective Turning and Coherent Relaxation in the Native Triad

**Repository research edition v0.1 — 28 October 2026.** Author-authorized repository publication, with completed GPT project-internal scientific review and author review. No external peer review is claimed.

Author: **Hilmir Frímann Halldórsson**. The author's observation and programme, GPT's scientific steering and internal review, and Codex's mathematical, computational, and drafting assistance are credited in the manuscript. See the [publication disposition](PUBLICATION_DISPOSITION.md) for authorization, approved corrections, and artifact identities.

The paper brings together a rigorously enclosed two-step turning witness, an exact phase-off delayed graph-response law, and a separate explicit finite-domain convergence theorem for the full native triad. The earlier turning entrance lies outside the convergence domain. No capture connection or physical-force identification is claimed.

Mathematical source baseline: [`ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade`](https://github.com/pzychozen/trioctagon-physics/tree/ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade). This cited baseline is distinct from the edition's publication commit.

- [Published v0.1 manuscript — canonical PDF](REVIEW.pdf)
- [Canonical LaTeX source](main.tex) and [bibliography](references.tex)
- [Claim/source map](CLAIM_SOURCE_MAP.md)
- [Publication disposition](PUBLICATION_DISPOSITION.md)
- [Evidence and original provenance](evidence/README.md)
- [Publication document verification](verification/publication_verification.json), [build record](verification/publication_build_record.json), and [visual inspection](verification/publication_visual_review.json)
- [Final publication manifest](PACKAGE_MANIFEST.json)
- [Historical preparation handoff](REVIEW_HANDOFF.md) and [verification record guide](verification/README.md)

`main.tex` is the only independently edited manuscript. `REVIEW.pdf` remains the single canonical PDF filename by explicit author instruction; its filename does not indicate pending review. Tables are derived from retained JSON by `make_figures.py`. There is no independently maintained Markdown manuscript.

## Build

Use Windows Command Prompt and the existing environment, from this directory:

```bat
conda activate torment
python -B build_review.py --tectonic C:/path/to/tectonic.exe --poppler-dir C:/path/to/poppler/bin
```

The build uses Tectonic, matplotlib, Pillow, and Poppler. Tool paths can be omitted on the original task host, where defaults identify the installed tools. It writes the canonical PDF, derived figures/tables, a publication build record, and temporary page renders within this edition directory. It does not execute any scientific checker or evaluate the recurrence. Tectonic may use its normal TeX resource cache/network on a fresh machine. A rebuild can change PDF metadata and bytes; the publication manifest identifies the released artifact.

The Codex LaTeX editor can open this folder with `main.tex` selected. Bibliographic references use `references.tex`, consistent with nearby mathematical papers. Accepted project citations are pinned GitHub links; evidence links are package-relative. Keep the PDF and evidence folder together for local evidence links.

## Evidence and verification scope

All six scientific checker/receipt files are unchanged archival copies. Their scripts retain historical absolute paths and safety assertions prohibiting output inside the repository. They are not portable build entry points and were not executed or modernized during publication.

`verify_review.py` retains its original preparation assertions, including its original HEAD/index/working-tree baseline. Its historical result applies only to the reviewed artifact. It is not a publication verification command, and its old baseline assertions are not claimed to pass after publication. Current checks are in `verify_publication.py` and the separately named publication records.

`package_review.py` now creates the explicit publication manifest and staging allowlist. It does not create a transfer ZIP or invent a visual PASS. It requires a separately recorded inspection tied to the actual PDF hash and page count. Local checkout inventories, preparation helpers, original transfer archives, and temporary outputs are excluded from publication.

No kernels, accepted papers, or scientific evidence were altered. No simulations, root solves, parameter sweeps, scientific checker replays, new physical claims, tags, releases, or DOI assignments accompany this repository edition. Existing repository licensing and reuse terms remain unchanged.
