# Measurement Geometry, Perspective, and Vesica Interfaces — revision candidate v0.1.1

This external workspace contains a bounded revision candidate for the published measurement paper. The published v0.1 package remains unchanged at scientific repository commit `0332fdd6aa3dd10d78dee77f70f910295e6d32a9`, under `papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/`. No repository files were edited, staged, committed, or pushed for this candidate.

The candidate PDF is [Measurement_Geometry_v0.1.1.pdf](measurement/Measurement_Geometry_v0.1.1.pdf), a 20-page revision built from the edited [manuscript.tex](measurement/manuscript.tex). Its exact bytes are recorded in [manifest.json](manifest.json). The candidate proposed destination is `papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1.1/`, pending approval.

Final PDF: **411,097 bytes; 20 pages; SHA-256 `fd7f60a4d1ea5e55c24aa692250e5976aff018a1ef76b724bfdecd39da5e8179`**. The source and PDF were completed on 6 October; final delivery checks were completed on 7 October 2026 after resuming the interrupted task. The original build date remains on the candidate title page.

## Bounded changes

1. Figure 1 was regenerated from the unchanged authoritative `kernel_physics/geometry.py` data. The verification record proves three ordered faces with eight local vertices each, 18 welded global vertices, 21 unique edges, three shared seams, two nine-edge boundary loops, and all 24 face-edge incidences rendered explicitly. The old renderer already supplied all 24 incidences; the revision makes them visually countable with opaque edge lines, vertex markers, and three local ordered-octagon insets.
2. The publication prose no longer discusses the owner's approximate remembered `0.544` value. The established radii, scales, and distinctions remain. Historical TL4 source records retain their original archaeology and unresolved-provenance discussion in the unchanged supplement.
3. A short recursive-lineage appendix and source supplement distinguish early RPCO/TGMO/REFU illustrations, the July glyph-SRG documents, the November field-memory model, the November six-state model, the fixed native `U = B tensor A` handoff, and the later nonlinear recurrence. Each arrow is labeled `EXACT DESCENDANT`, `DOCUMENTED LINEAGE`, `STRUCTURAL REINTERPRETATION`, or `NOT RECOVERED`. The historical scripts were read as source evidence and not executed.

The exact source diff is [manuscript_v0.1_to_v0.1.1.diff](provenance/manuscript_v0.1_to_v0.1.1.diff); the source inventory and lineage hashes are in [lineage_sources.json](provenance/lineage_sources.json). The native software license and scope notices remain unchanged. No physical interpretation is added.

## Checks

- Figure verification: PASS; authoritative source and exact incidence checks are in [figure_verification.json](results/figure_verification.json).
- Lineage verification: PASS; the symbolic Kronecker-product identity has all 36 entries zero, and one fixed-constant matrix comparison has maximum residual `3.3422138886441676e-16` at tolerance `2e-15`. Record: [lineage_verification.json](results/lineage_verification.json).
- PDF build: Tectonic 0.17.0, `SOURCE_DATE_EPOCH=1791244800`; 20 pages, no overfull boxes, missing glyphs, or undefined references. Record: [build.json](results/build/build.json).
- Visual review: every page 1–20 was rendered and inspected; the corrected Figure 1 was additionally inspected at page scale and as a standalone image.
- Final byte/source checks: [candidate_checks.json](results/candidate_checks.json), including preservation of the 427 retained mathematical expressions and all 31 inherited measurement-supplement files.
- Preservation: all **21,948** pre-edit inventoried files are byte-identical; repository HEAD, index and working-tree status match the baseline. Four unrelated new files appeared in the external reconstruction collection during the interruption; they were left untouched and are excluded. See [preservation.json](results/preservation.json).
- The prior v0.1 manuscript, PDF, drift paper, repository, and historical records were not rebuilt or modified. No TL0–TL4 suite, drift check, or historical simulation was rerun.

The QA renders and private baseline inventory stay outside the candidate publication payload. Nothing here authorizes a commit or push.

## Reproduction and package identity

Run only the requested step with a Python environment containing its dependencies. The build is a multi-file LaTeX project with figure assets and local supplements; it uses the retained Tectonic toolchain. The commands below write exclusively in this external candidate folder. Do not run the historical supplement scripts in place.

```text
python -B tools/correct_figure.py
python -B tools/check_lineage.py
python -B tools/build.py --tectonic <tectonic-executable> --fontconfig <fontconfig-file>
python -B tools/candidate_checks.py --repository <authoritative-trioctagon-physics-checkout>
python -B tools/preservation_check.py --project-root <original-project-root>
python -B tools/make_manifest.py
```

The preservation comparison requires the retained private baseline under `qa/private`; it is not part of the publication payload. The final manifest covers all payload files, including source, figures, supplements, checks, build logs and this README. It deliberately excludes itself, its detached checksum, private QA and the duplicate intermediate build PDF. `manifest.sha256` supplies the detached checksum; any later edit requires regenerating the manifest and repeating the affected check.
