# Paper C publication revision v1.0.1

Exact Geometry of the Folded Tri-Octagon Module, Hilmir Frímann Halldórsson. 23 September 2026.

[Publication PDF](PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.1.pdf) (16 pages), [publication manuscript](PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md), [references](REFERENCES_v1.0.1.md). PDF SHA-256: `5869fb7b98784fab00e8b63f225f84c03277bbd4bac3534c0773df9efed156d1`.

This scope/citation revision applies C-S1, C-S2 and C-S3, approved in GPT's D v0.1.1 acceptance. Original proofs, equations, coordinate conventions, measurements and three tables are unchanged. The historical scientific manuscript remains v0.3.1; v1.0.1 is the publication revision label. The [previous publication PDF](../PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf) and its evidence are preserved.

[Paper D v0.1.1](../../../PAPER_D/v0.1.1/README.md) is an accepted artifact prepared for repository publication. Its approved PDF is cited through a relative target. No DOI, release or prior publication of D is asserted. The new edition does not adopt its alternate placement or shrink into this model.

The [combined checkpoint](../../../publication_updates/20260923_BC_scope/README.md) supplies the exact change record, preservation comparison, review attribution and proposed file list. GPT approved the supplied passages; final build/QA results are Codex-attributed.

## Bounded build

Use existing Python, Pandoc and Tectonic plus a populated TeX cache; set `PAPER_C_PANDOC`, `PAPER_C_TECTONIC`, `PAPER_C_TEX_CACHE`. Run `python -B -X utf8 build_publication.py` here. The builder writes only this revision and its ignored `.build` intermediates, uses `--only-cached`, and runs no geometry, algebra, kernel or figure-generation script. See [documented prerequisites and isolated replay](../../../publication_updates/20260923_BC_scope/REPRODUCIBILITY.md).

`build_console.log`, `paper_C_final.log`, `build_record.json` and `evidence/structural_fidelity.json` are newly captured Codex build evidence. Historical execution counts in the unchanged manuscript remain earlier results; they are not new executions. No staging, commit or push.
