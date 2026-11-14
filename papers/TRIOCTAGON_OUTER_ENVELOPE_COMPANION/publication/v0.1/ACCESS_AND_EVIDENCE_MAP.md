# Source and evidence access guide

All links below resolve inside this delivery. They refer to preserved source bytes, not to current remote state. The reading checkpoint `46bf10808b8694476b61b359be305a66a46d4614` is historical; no Git operation was performed for authoring.

## Manuscript and evidence route

- [Final manuscript](TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf); [final claim/source ledger](MANUSCRIPT_CLAIM_LEDGER.json).
- [Accepted proof](evidence/outer_envelope/submitted/PROOF_REPORT.md), Sections 1-9; [original four-claim ledger](evidence/outer_envelope/submitted/CLAIM_LEDGER.json).
- [Detailed scientific review](evidence/outer_envelope/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_REVIEW.md); [acceptance decision](evidence/outer_envelope/GPT_ACCEPTANCE.json).
- [Complete certificate](evidence/outer_envelope/submitted/data/exact_certificate.json); [readable representatives](evidence/outer_envelope/submitted/data/FACE_REPRESENTATIVES.md); [raw representative coefficients](evidence/outer_envelope/submitted/data/FACE_REPRESENTATIVES.json).
- [Incidences and endpoint maps](evidence/outer_envelope/submitted/data/FACE_INCIDENCE_RECORDS.json); [transition readout](evidence/outer_envelope/submitted/data/TRANSITION_READOUT.json); [candidate residuals](evidence/outer_envelope/submitted/data/CANDIDATE_RESIDUAL_TABLE.md).
- [Prior-work comparison](evidence/outer_envelope/submitted/PRIOR_WORK_COMPARISON.md); [accepted source identity manifest](evidence/outer_envelope/submitted/sources/SOURCE_IDENTITY_MANIFEST.json).
- [Separate reviewer implementation result](evidence/outer_envelope/reviewer/INDEPENDENT_EXACT_CHECK.json); [Bernstein certificates](evidence/outer_envelope/reviewer/BERNSTEIN_SIGN_CERTIFICATES.json); [shared-engine replay comparison](evidence/outer_envelope/reviewer/REPLAY_COMPARISON.json).
- [Commission work order](provenance/commission/TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_CODEX_WORK_ORDER.md); [manuscript blueprint](provenance/commission/MANUSCRIPT_BLUEPRINT.md); [commission source guide](provenance/commission/SOURCE_CLAIM_GUIDE.md).

The paper places the original Windows engine, reviewer replay of that engine, and separate reviewer algebraic-field/Bernstein implementation in distinct evidence layers (Section 8, page 8). Those historical computations were not rerun during authoring. The 254 monic-form count and 255 oriented-proof count have different accounting scopes.

## Bibliography route

- Reference [1]: [Paper C, S13](evidence/outer_envelope/submitted/sources/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md), Section 4, coordinate/indexing authority.
- Reference [2]: [parent synthesis, S01](evidence/outer_envelope/submitted/sources/papers/SPHERICAL_EDGE_EXTENSIONS/publication/v0.1/SPHERICAL_EDGE_EXTENSIONS_v0.1.tex), retained source dated 16 October 2026 with historical proposed-edition wording. Key labels: `def:exits`, `eq:exits`, `thm:events`, `thm:symmetry`, `prop:exposed`, `sec:hulls`, `sub:certificates`, `sec:locus`, `cor:ratio`, `app:decagon`. This is a source-text copy; parent build assets are not promised.
- Reference [3]: [investigation proof report](evidence/outer_envelope/submitted/PROOF_REPORT.md), plus the complete submitted evidence tree.
- Reference [4]: [GPT review](evidence/outer_envelope/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_REVIEW.md) and [acceptance](evidence/outer_envelope/GPT_ACCEPTANCE.json).

## Printed objects

| Final object | PDF page(s) | Controlling evidence |
|---|---:|---|
| tab:claims (no. 1) | 1 | [CLAIM_LEDGER.json](evidence/outer_envelope/submitted/CLAIM_LEDGER.json); [PRIOR_WORK_COMPARISON.md](evidence/outer_envelope/submitted/PRIOR_WORK_COMPARISON.md) |
| tab:residuals (no. 2) | 3 | [CANDIDATE_RESIDUAL_TABLE.md](evidence/outer_envelope/submitted/data/CANDIDATE_RESIDUAL_TABLE.md); [CHECKER_RESULT.json](evidence/outer_envelope/submitted/data/CHECKER_RESULT.json) |
| fig:transition (no. 1) | 4 | [local_facet_transition.png](evidence/outer_envelope/submitted/figures/local_facet_transition.png); [local_facet_transition.svg](evidence/outer_envelope/submitted/figures/local_facet_transition.svg); [FIGURE_RECORD.json](evidence/outer_envelope/submitted/figures/FIGURE_RECORD.json); [TRANSITION_READOUT.json](evidence/outer_envelope/submitted/data/TRANSITION_READOUT.json) |
| tab:classification (no. 3) | 6 | [CHECKER_RESULT.json](evidence/outer_envelope/submitted/data/CHECKER_RESULT.json); [FACE_INCIDENCE_RECORDS.json](evidence/outer_envelope/submitted/data/FACE_INCIDENCE_RECORDS.json) |
| tab:patch (no. 4) | 7 | [TRANSITION_READOUT.json](evidence/outer_envelope/submitted/data/TRANSITION_READOUT.json) |
| tab:limits (no. 5) | 7 | [TRANSITION_READOUT.json](evidence/outer_envelope/submitted/data/TRANSITION_READOUT.json); [FACE_INCIDENCE_RECORDS.json](evidence/outer_envelope/submitted/data/FACE_INCIDENCE_RECORDS.json) |
| tab:access (no. 6) | 9 | [SOURCE_IDENTITY_MANIFEST.json](evidence/outer_envelope/submitted/sources/SOURCE_IDENTITY_MANIFEST.json) |
| tab:orbits-C1 (no. 7) | 10-11 | [FACE_REPRESENTATIVES.json](evidence/outer_envelope/submitted/data/FACE_REPRESENTATIVES.json); [exact_certificate.json](evidence/outer_envelope/submitted/data/exact_certificate.json) |
| tab:orbits-T (no. 8) | 11 | [FACE_REPRESENTATIVES.json](evidence/outer_envelope/submitted/data/FACE_REPRESENTATIVES.json); [exact_certificate.json](evidence/outer_envelope/submitted/data/exact_certificate.json) |
| tab:orbits-C2 (no. 9) | 12 | [FACE_REPRESENTATIVES.json](evidence/outer_envelope/submitted/data/FACE_REPRESENTATIVES.json); [exact_certificate.json](evidence/outer_envelope/submitted/data/exact_certificate.json) |

## Preserved source identities

The following raw SHA-256 identities were compared against the supplied manifest. Recorded Git blob IDs were also checked using their byte-format hash, without Git commands. Software source copies below are documentary evidence, not imports.

| ID | Preserved file | SHA-256 |
|---|---|---|
| S01 | [papers/SPHERICAL_EDGE_EXTENSIONS/publication/v0.1/SPHERICAL_EDGE_EXTENSIONS_v0.1.tex](evidence/outer_envelope/submitted/sources/papers/SPHERICAL_EDGE_EXTENSIONS/publication/v0.1/SPHERICAL_EDGE_EXTENSIONS_v0.1.tex) | `6a8830fa0146ce1cecf15271c3d89e03c166bbc71dcd9c4dfaf964d82b91d187` |
| S02 | [research/spherical_edge_extensions/accepted/boundary11/data/geometry_inventory.json](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary11/data/geometry_inventory.json) | `694a9ab0cab1e9335be913ef876483e9fedd59a22cb93cec6b9dda3a33a1afb2` |
| S03 | [research/spherical_edge_extensions/accepted/boundary12/data/hull_A.json](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary12/data/hull_A.json) | `6b32bc83ad2d7b70bb6c5ade13750d75821305891758e2fbbeea1ff85aee1f99` |
| S04 | [research/spherical_edge_extensions/accepted/boundary12/data/hull_B.json](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary12/data/hull_B.json) | `b6dad941a7415764a4b6bf49be0e40dc10a213e57d82e8ccc8d1c892bf1347cf` |
| S05 | [research/spherical_edge_extensions/reviews/boundary12/BOUNDARY12_GPT_SCIENTIFIC_REVIEW.md](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/reviews/boundary12/BOUNDARY12_GPT_SCIENTIFIC_REVIEW.md) | `0ab5cfdd080bffa62db111f29ac9eae4da20a010ec36e7ed01e0fe1248e620fd` |
| S06 | [research/spherical_edge_extensions/accepted/boundary12/BOUNDARY12_REPORT.md](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary12/BOUNDARY12_REPORT.md) | `d904699e6ec4f9370cd310de73065d50f410eea0a2ddb9eeaafcd79e26f0ffc3` |
| S07 | [research/spherical_edge_extensions/accepted/boundary11/BOUNDARY11_REPORT.tex](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary11/BOUNDARY11_REPORT.tex) | `21d4b8db4fc19d981eb8e5e98e8886c26d91cc47199a7aafc4814b177f9cf6aa` |
| S08 | [research/spherical_edge_extensions/future/OPEN_QUESTIONS.md](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/future/OPEN_QUESTIONS.md) | `629d49ae726961e78b8d8876ab5bfe4e14d0fcabc09c0bcfebe3691fea1f4c3a` |
| S09 | [research/spherical_edge_extensions/accepted/boundary12/data/hull_face_orbits.json](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary12/data/hull_face_orbits.json) | `8f000ea6594abe6c33d4974ced0f07acc5a0285da676e2157f99a6718fbfc694` |
| S10 | [research/spherical_edge_extensions/accepted/boundary12/data/hull_original.json](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary12/data/hull_original.json) | `156e7dbe3360b959cf4d6b08f423145be6e63ff66b259d77677c697cffef53ac` |
| S11 | [README.md](evidence/outer_envelope/submitted/sources/README.md) | `9a86b174492fa848948931740ca548782d757cd925424ec8ff0b9ac1554012af` |
| S12 | [papers/PAPER_C/publication/v1.0.1/README.md](evidence/outer_envelope/submitted/sources/papers/PAPER_C/publication/v1.0.1/README.md) | `ea15fab5e77f8c59fcb2ecb4c533bdb709f8b5173bbccaf9af296c91568090de` |
| S13 | [papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md](evidence/outer_envelope/submitted/sources/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md) | `5a0cbdae4aaf689cfe1f5b29305960e90c88e26d0db28834802ef70fc16549fb` |
| S14 | [research/spherical_edge_extensions/README.md](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/README.md) | `583db03482568c9e35a49a27a643568fdd02e7d2380eb4ddbe0b27feb45d2017` |
| S15 | [research/spherical_edge_extensions/accepted/boundary10/BOUNDARY10_REPORT.tex](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/accepted/boundary10/BOUNDARY10_REPORT.tex) | `a7e648912ed4a427a63388a4d7b73c23c6b409f3854d78f0fa1624f462d207b9` |
| S16 | [research/spherical_edge_extensions/reviews/boundary11/BOUNDARY11_GPT_SCIENTIFIC_REVIEW.md](evidence/outer_envelope/submitted/sources/research/spherical_edge_extensions/reviews/boundary11/BOUNDARY11_GPT_SCIENTIFIC_REVIEW.md) | `ab11ccf60f360a816648d1cbfd937f76844fc59103e8e22003b486ba1e025f5e` |
| S17 | [papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/README.md](evidence/outer_envelope/submitted/sources/papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/README.md) | `08a1a7859f55c596ac97f991b87e13513ce79ea010cfc508641820c2613982eb` |
| S18 | [papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/GEO_ORIGINS01_v0.2.tex](evidence/outer_envelope/submitted/sources/papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/GEO_ORIGINS01_v0.2.tex) | `dcd3c5d5b9a44b5b14ef643b6065f191d59c59a446e8edb1552142e4c36cdd23` |
| S19 | [papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/retained_mathematics.tex](evidence/outer_envelope/submitted/sources/papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/retained_mathematics.tex) | `c30ef8d44d4707f8e117fab07ab87f0c67ba40d3f5edd696049f4582da4de7df` |
| S20 | [papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/ACCESS_AND_EVIDENCE_MAP.md](evidence/outer_envelope/submitted/sources/papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/ACCESS_AND_EVIDENCE_MAP.md) | `5dba7c95c7aec4fca60294631d213b8aa014b54a24b55d261d52761f8bb4fe3e` |
| S21 | [apps/scientific_ui/publication/shell_observer/v0.1/README.md](evidence/outer_envelope/submitted/sources/apps/scientific_ui/publication/shell_observer/v0.1/README.md) | `eae3cb8303787dd76fa247124d4a9e4ce4a3ca9aed38e073baa9afaf2be83e46` |
| S22 | [apps/scientific_ui/src/trioctagon_ui/shell_observer.py](evidence/outer_envelope/submitted/sources/apps/scientific_ui/src/trioctagon_ui/shell_observer.py) | `381c17ec7242c74b93b4bb64301499d1157a1c5459202fe8223747ebf3eabdd1` |
| S23 | [apps/scientific_ui/src/trioctagon_ui/geometry_view.py](evidence/outer_envelope/submitted/sources/apps/scientific_ui/src/trioctagon_ui/geometry_view.py) | `90de4d3731c083a86ef10761dc437be5bf6cd46e77113d55d1aebef0d127c1ba` |
| S24 | [external/TSZ01_FINDINGS_AND_NEXT_QUESTIONS.md](evidence/outer_envelope/submitted/sources/external/TSZ01_FINDINGS_AND_NEXT_QUESTIONS.md) | `17a750fdb22a392b3263bc315a4312f04544cdd96e98d3e3b5394481bf3fc635` |

## Preservation and status

All incoming files are mapped by [PRESERVED_INPUTS.json](PRESERVED_INPUTS.json). The intact [acceptance archive](archives/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_ACCEPTANCE_PACKAGE.zip) and [its original sidecar](archives/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_ACCEPTANCE_PACKAGE.zip.sha256) accompany the complete extraction. The acceptance supersedes historical scientific pending labels; the commission supersedes only historical lack of manuscript authorization. No original field was rewritten. GPT manuscript review is complete and the author authorized repository publication on 14 November 2026. The exact submitted manuscript remains in the unchanged original review ZIP; historical pending wording is preserved.

## Publication administration

- [Author activation](provenance/publication/AUTHOR_PUBLICATION_AUTHORIZATION.json).
- [GPT manuscript review](provenance/publication/TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_GPT_REVIEW.md) and [acceptance](provenance/publication/GPT_MANUSCRIPT_ACCEPTANCE.json).
- [Activated work order](provenance/publication/TRIOCTAGON_OUTER_ENVELOPE_PUBLISH_01_CODEX_WORK_ORDER.md), [exact edit instructions](provenance/publication/ADMINISTRATIVE_SOURCE_EDITS.json), [reversible edit receipt](provenance/publication/ADMINISTRATIVE_EDIT_RECEIPT.json).
- [Original review ZIP](provenance/publication/received/TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip), [original checksum](provenance/publication/received/TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip.sha256) and [original archive audit](provenance/publication/received/FINAL_ARCHIVE_AUDIT.json).
- [Current status](CURRENT_STATUS.json), [final build](verification/final_build/BUILD_RECEIPT.json), [all-page inspection](verification/VISUAL_INSPECTION.json).

The original publication packet and every contained file are retained in the external closeout. Its 33 extracted members are also preserved under publication provenance; the current [publication-input map](PUBLICATION_INPUTS.json) records their exact raw identities. Software licensing does not broaden scientific-material rights.
