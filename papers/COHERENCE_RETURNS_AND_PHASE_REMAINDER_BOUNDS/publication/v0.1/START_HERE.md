# NCM-PAPER-01 v0.1 review package

**Research draft v0.1 — for GPT/author review. Not publication approval.**

Author: Hilmir Frímann Halldórsson. GPT: mathematical direction/internal review. Codex: retained computational work, present independent proof review, source reconciliation and typesetting.

## Start with these files

1. [Review PDF](manuscript/REVIEW.pdf): 19 pages, 30 numbered equations, seven tables, no generated trajectory or discussion-sketch figure.
2. [Plain-language summary](PLAIN_LANGUAGE_SUMMARY.md).
3. [Independent 60-degree review](proof_review/SECTOR_60_REVIEW.md): **ACCEPTED**, with exact hypotheses and endpoint argument.
4. [Claim-to-source matrix](CLAIM_SOURCE_MATRIX.md) and [evidence index](EVIDENCE_INDEX.md).
5. [Manuscript QA](MANUSCRIPT_QA.md), [correction log](CORRECTIONS_AND_DISPOSITION.md), [placement assessment](NOVELTY_AND_PLACEMENT.md).

## Main findings

The regular raw-coherence return theorem, fixed-parameter amplitude bound and three-update remainder bound are retained with complete proofs. The sector extension is established: at epsilon=1/10, g=1/60, lambda=1/300 and k=(999/1000,1,1001/1000), a nonzero regular finite unit-multiplier return from B3 that meets an ordinary closed phase arc of width at most 60 degrees is fixed, with multiplier one. This is not a spatial cone-angle theorem or global convergence theorem.

The three-update phase remainder has principal angle at most 2 asin(161151/1000000), approximately 18.5474213628 degrees. This excludes the three-update/order-four phase mechanism here, not all twelve-cycles or three-stage returns.

Frozen outcomes remain 42 numerical lower-period outcomes in seven groups, 17 line-search failures and one iteration-ceiling failure. There was no genuine period-three candidate or certificate. Dispersed-phase returns and the native-to-cone correspondence remain unresolved.

## Sources and build

[main.tex](manuscript/main.tex) contains the full manuscript and a linked local bibliography; [references.bib](manuscript/references.bib) is the corresponding editable bibliography. Shared content is [content.py](manuscript/content.py), with a readable [JSON snapshot](manuscript/content_snapshot.json). Both TeX and PDF use this content.

No local LaTeX compiler was available. The PDF was built under **torment** using the already available bundled ReportLab library and matplotlib mathtext; it is not a compiled-TeX PDF. The TeX source was not compiler-tested. PDF equations are high-resolution raster expressions; editable mathematical source is supplied. All final pages were rendered and visually inspected. No dependencies or fonts were installed; no font files are shipped.

Review does not require execution. For a document-only rebuild in the existing local environment:

    cd /d C:\TORMENT\TRIOCTAGON_new\research\NATURAL_CORE_MOTION_COHERENCE_PAPER_01
    call conda activate torment
    python -X utf8 -I -B manuscript\build_manuscript.py

The builder uses the recorded existing local library path and does not download dependencies. See [COMMANDS.txt](COMMANDS.txt).

## Evidence and preservation

Unchanged DUAL-02/03 archives are under [packet evidence](packet/NCM_PAPER_01_Codex_Packet_v0.1/evidence/). Final DUAL-03 phase_b files control the numerical account. The preliminary missing-packet notice remains history.

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records bounded before/after checks; [OUTPUT_HASHES.json](OUTPUT_HASHES.json) covers selected packaged files, excluding itself. The ZIP and external receipt are at the research root. Caches, unused math assets and unrelated source trees are excluded.

**Current task: zero native F evaluations; zero old solver/checker/certificate executions; zero observer/pose experiments. No Git, application/kernel changes, network acquisition or publication.**
