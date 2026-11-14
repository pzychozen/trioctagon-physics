# Source guide and exact lookup policy

Repository: `pzychozen/trioctagon-physics`. Reading checkpoint:
`46bf10808b8694476b61b359be305a66a46d4614`.

Use `REQUIRED_SOURCES.json` for exact original paths and expected Git blob SHA-1s. These values were read through the connected GitHub source/tree interface. They are **not** SHA-256 checksums. The full raw sources are not bundled; use local originals or pinned source retrieval. Record any differences without rewriting an original file.

## Reading order

1. S01: `sec:native`, `eq:local`, `eq:fold`, `def:exits`, `thm:events`, `thm:symmetry`, `sec:hulls`, `sec:locus`, `app:coordinates`, `app:edges`, `app:decagon`.
2. S05 controlling BOUNDARY-12 review §§1–4, then S06 report §§1–5. The existing result covers three event hulls.
3. S02 actual inventory to bind the transcribed recipe to material indexing and source branch conventions.
4. S03/S04 exact endpoint hull records; S09 optional orbit summary.
5. S07 and its review in `research/spherical_edge_extensions/reviews/boundary11/` if needed for exact inherited premises.
6. S08 and targeted later geometry indexes to finish the nonduplication gate.

## Further targeted source locations

- `papers/PAPER_C/publication/v1.0.1/README.md`: source authority/navigation for the actual welded shell.
- `research/spherical_edge_extensions/accepted/boundary10/`: original enclosing-ball and optional decagonal study; named from the pinned directory listing.
- `papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/README.md`: later historical/normalization context; recover only relevant source sections if needed.
- `apps/scientific_ui/publication/shell_observer/v0.1/README.md`: source publication navigation, not authority to run/edit the application.
- Local `TSZ01_FINDINGS_AND_NEXT_QUESTIONS.md`, if present in the research workspace: scale/measurement distinctions. Its Library text was read in GPT preparation; no new raw-file identity is asserted.

The last group contains navigation/context, not missing numerical premises. Do not make an unrelated archival reconstruction or old publication review a prerequisite. Do not treat old `pending` wording as evidence that a later accepted result or publication never occurred.

## Access and scope disclosure

GPT read relevant written source sections and the BOUNDARY-12 review, inspected pinned source-tree identities, and ran an isolated coordinate transcription/pilot. GPT did not download and byte-audit all inherited JSON files, rerun historical geometry checkers, inspect source PDFs, or perform a worldwide literature search. The new packet describes these limits explicitly. Codex must validate the mandatory source correspondence before claiming a new theorem.

The optional source collector operates locally, without network access or repository writes. It first accepts a working file only when its actual Git blob identity matches; otherwise it can retrieve the listed committed bytes via read-only `git show`. It writes copies into a new external directory. It does not normalize line endings, mutate Git metadata intentionally, or run any scientific script.
