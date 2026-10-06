# Measurement geometry and chiral phase drift — finalization record

**Research publication v0.1 · 6 October 2026 · Hilmir Frímann Halldórsson**

Final publication files are prepared. **Repository publication is pending final-byte and allowlist approval.** This package contains two separate papers; their shared packaging root is not a combined physical claim. No repository write, staging, commit, push, upload, release, tag, DOI or visibility change was performed.

## Final papers

| Title | PDF / source | Pages | Bytes |
|---|---|---:|---:|
| Measurement Geometry, Perspective, and Vesica Interfaces in the Tri-Octagon Model | [PDF](measurement/Measurement_Geometry_v0.1.pdf) · [LaTeX](measurement/manuscript.tex) | 18 | 395015 |
| Cubic Common-Phase Drift on a Chiral Branch of the Tri-Octagon Map | [PDF](drift/Cubic_Common_Phase_Drift_v0.1.pdf) · [LaTeX](drift/manuscript.tex) | 20 | 178544 |

SHA-256:

    measurement: 117474240877e9eaa61faa041d6e362fbdb5ec9b6971569563d2d746674f0fed
    drift:       f1be0a9979c08607a0d6ba79358c4a6c04f268822dbe29130a73da46824f8538

Author and version are checked in both PDFs' metadata. The [manifest](manifest.json) identifies all public package bytes; it does not claim that derived files retain their originals' hashes.

## Public source and evidence location

Source project: [pzychozen/trioctagon-physics](https://github.com/pzychozen/trioctagon-physics).
Unchanged scientific baseline: [82cab10cbe550f58c43163fb8b05fabdad1b05ae](https://github.com/pzychozen/trioctagon-physics/tree/82cab10cbe550f58c43163fb8b05fabdad1b05ae).

The exact **planned** publication-package location in that repository is:

    papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/

Keep measurement/, drift/, tools/, provenance/, results/, this README, requirements and manifest relative to that root. The destination is stated for later repository publication; this preparation does not claim the new path is already online. Both PDFs include the repository URL, planned path, baseline identity and pending-publication qualification, so a lone PDF identifies where its supplement belongs.

Local manuscript links resolve after extraction of the complete package. The supplement contains selected scientific dependencies, not every historical file named in a source record. Locators beginning with project-source/ are historical project-relative identifiers; they do not assert that the referenced archive or file is distributed here.

## Exact differences from the reviewed package

The immutable review ZIP has SHA-256 ca08f3ef3ff3d4ab45f92531e8ef2fe48393cb6973df095fd96b9cb82cbcf142. Its 110 manifest entries and both PDF identities were checked before use. The archive, extracted review workspace, approved masters and all predecessors remain unchanged outside this new workspace.

Current title pages, headers, PDF metadata and generation templates now say **Research publication v0.1**. Added public project/destination pointers and accurate availability statements. The drift availability statement and bibliography start on separate pages for readable layout. The [complete manuscript diff](provenance/manuscript_editorial.diff) records these edits. Scientific narrative order, qualifications and all mathematics remain as reviewed: the complete 429 measurement and 401 drift inline/display expressions match, including all 47/53 labels and unnumbered displays. There is no new derivation, simulation, D2, literature survey or physical interpretation.

The [typed public-export map](provenance/public_export_map.json) records each omitted operational field or replaced locator, its reason, the original raw artifact SHA-256 and the derived public SHA-256. Omitted values are hashed, not reproduced. The [source inventory](provenance/source_inventory.json) distinguishes **51 unchanged copies** from **25 labeled public derivatives**. The redundant reviewer ZIP container is excluded; its five inspected members and original container identity are retained.

Operational omissions are confined to explicitly named checkout-status/index/staging snapshots, machine-preservation inventories/count fields and a private preview receipt. Baseline scientific commit identities and historical acceptance outcomes remain. Necessary locators become documented project-relative or supplied-document identifiers; private interpreter paths become generic historical interpreter names. No scientific field was selected for omission by a broad keyword rule.

All scientific roots, jets, intervals, continuation paths, precision values, inequalities, residuals and domains are retained. The original function/class bodies of the seven path-only verifier derivatives are unchanged. [Direct export comparisons](results/public_export_verification.json) and [finalization changes](provenance/finalization_changes.json) document the checks. Raw originals remain private; a public extract's hash identifies the extract, not independent certification of its raw source. Historical status wording and original check counts were not rewritten to appear current.

## Reproduction from an extracted public root

Prerequisites: Python 3.11 with [requirements.txt](requirements.txt), and Tectonic 0.17.0. Run:

    python -B tools/typeset.py
    python -B tools/figures.py
    python -B tools/smoke.py
    python -B tools/build.py --tectonic tectonic
    python -B tools/check_package.py

An existing platform Fontconfig file may be supplied with --fontconfig. The recorded [installed environment](provenance/environment.json) was reused; a fresh dependency installation and cross-platform byte identity were not tested. A first Tectonic run may obtain its standard bundle over the network.

These active tools write generated manuscript/figure files, crosswalks, final PDFs and designated results under this extracted package. **Do not execute historical writers in-place.** Their locators and original whole-checkout assumptions are not a portable full-suite command.

The smoke adapter reads the public D1 evidence derivative, verifies its public hash and the unchanged complete roots_plus and exact_jet fingerprints, then loads the original function/class bodies through AST. It omits module-level path assertions, file I/O and main dispatch. Mathematical routines, rounding, precision, tolerances, branch selection and acceptance inequalities were not changed. The smoke uses the same four retained midpoints at eta=0.00025 and h=0, 0.1, 0.01, 0.001, and one h=0.1 fixed-root enclosure with radius 1e-60, at the original 110/100-digit settings.

## Final checks and evidence boundaries

| Final record | Result and scope |
|---|---|
| [Publication checks](results/publication_checks.json) | **20/20 PASS**: source hashes, displays/labels/references, full reviewed mathematics sequence, local links, final status/destination, template, build diagnostics and export fingerprints |
| [Scientific smoke](results/portable_smoke.json) | **8/8 PASS**, executed in a fresh public-layout directory; bounded checks only |
| [Raw-to-public comparisons](results/public_export_verification.json) | **33/33 PASS**, including typed unchanged JSON values, scientific source identities, mathematical strings and verifier bodies |
| [Clean-directory test](results/clean_directory_test.json) | Source/figure regeneration, smoke, build and checks passed; both PDF rebuilds byte-identical; all 76 source/evidence inputs unchanged |
| [Visual/metadata/link review](results/visual_review.json) | Every final page inspected: **18/18 measurement, 20/20 drift**; all embedded local supplement links resolve |
| [Preservation](results/preservation.json) | Original protected collections, review inputs, repository HEAD/index/status and pre-existing work unchanged |

The package checker was repaired for reader-only false positives: URI/TeX notation mistaken for drive paths, and CRLF versus LF in one historical text fingerprint. Only the checker was rerun after those repairs; the numerical routines and acceptance rules were not changed. The compiler reports no overfull boxes, missing glyphs or undefined references.

Prior Codex review-stage **14/14** and **8/8** receipts are retained separately under provenance/review_stage/. The work order's GPT review attribution is a separate record there: its stated Python 3.13.5 replay is not a new supported-environment promise, an independent interval implementation or a Windows-preservation audit.

Historical counts remain separate and were not fully regenerated: **TL0 63; TL1 24; TL2 29; TL3 35; TL4 45; D0 64; D1 133; NRG paper-local 61; NRG retained checkpoint 429.** No grand total is asserted. The complete D1 continuation suite, other predecessor suites, original machine-preservation checks and reviewer companion scripts were not rerun. Passing packaging checks does not replace proofs or an independent audit of the interval library.

## Approval scope and stopping point

Actual starting/final scientific HEAD: **82cab10cbe550f58c43163fb8b05fabdad1b05ae**, branch main; index empty and unchanged. The final public package excludes the raw private review archive, unrelated checkout snapshots, private inventories, QA images, clean-room copies and intermediate build PDFs.

The exact proposed repository file list is [COMMIT_ALLOWLIST.txt](provenance/COMMIT_ALLOWLIST.txt). Every line is rooted under the planned shared publication directory. The delivery ZIP is a container for those files and is not itself an additional proposed repository file.

Allowlist SHA-256:

    8ca33524dabbf10af17afac5ed1a589fdd9c1a1baacccc9340d02cff86ea94c7

Proposed single-commit message:

    papers: publish measurement geometry and chiral phase drift v0.1

The copied native software license and scope notices are unchanged. Apache-2.0 is not assigned to papers, figures, research scripts or results. This preparation grants no new redistribution license and claims no external peer review, journal acceptance or DOI.

**Stop for final-byte and allowlist publication approval.**
