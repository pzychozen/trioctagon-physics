# Paper B publication revision v0.1.2

Triadic Chirality and Orientation Geometry, Hilmir Frímann Halldórsson. 23 September 2026.

[Publication PDF](PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.pdf) (13 pages), [publication manuscript](PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md), [references](REFERENCES_v0.1.2.md). PDF SHA-256: `5555eb4f07b0974addced80339bf0f87bb7a5ab87d268926f321a3c586da35ad`.

This scope/citation revision applies B-S1 and B-S2, approved in GPT's D v0.1.1 acceptance. Original proofs, equations, coordinate conventions, measurements and five figures are unchanged. The five existing PDF figure assets are read directly from ../../figures/ and not regenerated. The [previous publication PDF](../v0.1.1/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.1.pdf) and its evidence are preserved.

[Paper D v0.1.1](../../../PAPER_D/v0.1.1/README.md) is an accepted artifact prepared for repository publication. Its approved PDF is cited through a relative target. No DOI, release or prior publication of D is asserted. The new edition does not adopt its alternate placement or shrink into this model.

The [combined checkpoint](../../../publication_updates/20260923_BC_scope/README.md) supplies the exact change record, preservation comparison, review attribution and proposed file list. GPT approved the supplied passages; final build/QA results are Codex-attributed.

## Bounded build

Use existing Python, Pandoc and Tectonic plus a populated TeX cache; set `PAPER_B_PANDOC`, `PAPER_B_TECTONIC`, `PAPER_B_TEX_CACHE`. Run `python -B -X utf8 build_publication.py` here. The builder writes only this revision and its ignored `.build` intermediates, uses `--only-cached`, and runs no geometry, algebra, kernel or figure-generation script. See [documented prerequisites and isolated replay](../../../publication_updates/20260923_BC_scope/REPRODUCIBILITY.md).

`build_console.log`, `paper_B_final.log`, `build_record.json` and `evidence/structural_fidelity.json` are newly captured Codex build evidence. Historical execution counts in the unchanged manuscript remain earlier results; they are not new executions. No staging, commit or push.
