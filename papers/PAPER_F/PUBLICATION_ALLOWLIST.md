# Proposed Paper F Git publication allowlist

**Not authorization to stage, commit or push.**
56 exact paths: 20 selected support artifacts and 36 manuscript, figure, build and receipt paths.

All paths lie under `papers/PAPER_F/`. No original path is replaced. No glob staging is proposed.

| Exact repository-relative path | Why included |
|---|---|
| `papers/PAPER_F/BIBLIOGRAPHY.md` | Human-readable checked bibliography |
| `papers/PAPER_F/build_publication.py` | Reproduce isolated offline PDF/TeX build |
| `papers/PAPER_F/figures/figure_1_exact_inputs.json` | Exact Figure 1 inputs or vector/raster export |
| `papers/PAPER_F/figures/figure_1_transverse_symmetry.pdf` | Exact Figure 1 inputs or vector/raster export |
| `papers/PAPER_F/figures/figure_1_transverse_symmetry.png` | Exact Figure 1 inputs or vector/raster export |
| `papers/PAPER_F/figures/figure_1_transverse_symmetry.svg` | Exact Figure 1 inputs or vector/raster export |
| `papers/PAPER_F/generate_figure.py` | Equation-only Figure 1 generator |
| `papers/PAPER_F/inspect_pdf.py` | Reproduce structural QA and Poppler page renders |
| `papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md` | Public manuscript; controlled editorial conversion |
| `papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.pdf` | Final inspected publication PDF |
| `papers/PAPER_F/paper_F_v0.2.tex` | Final typesetting source for the same scientific text |
| `papers/PAPER_F/prepare_publication.py` | Reproduce controlled source conversion and fidelity map |
| `papers/PAPER_F/PUBLICATION_ALLOWLIST.md` | Individual path roles and exclusions |
| `papers/PAPER_F/PUBLICATION_ALLOWLIST.txt` | Exact proposed repository paths |
| `papers/PAPER_F/PUBLICATION_CHECKPOINT.md` | Final build/review checkpoint, not publication authorization |
| `papers/PAPER_F/publication_style.tex` | Typography and width-safe display wrappers |
| `papers/PAPER_F/README.md` | Package entry point and exact reproduction instructions |
| `papers/PAPER_F/records/build_console.log` | Bounded build, fidelity, reference, reproduction or preservation evidence: build_console |
| `papers/PAPER_F/records/build_record.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: build_record |
| `papers/PAPER_F/records/editorial_transformations.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: editorial_transformations |
| `papers/PAPER_F/records/isolated_exact_checks.stderr.log` | Bounded build, fidelity, reference, reproduction or preservation evidence: isolated_exact_checks.stderr |
| `papers/PAPER_F/records/isolated_exact_checks.stdout.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: isolated_exact_checks.stdout |
| `papers/PAPER_F/records/isolated_verification.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: isolated_verification |
| `papers/PAPER_F/records/latex_build.log` | Bounded build, fidelity, reference, reproduction or preservation evidence: latex_build |
| `papers/PAPER_F/records/literature_verification.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: literature_verification |
| `papers/PAPER_F/records/pdf_structural_qa.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: pdf_structural_qa |
| `papers/PAPER_F/records/preservation_receipt.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: preservation_receipt |
| `papers/PAPER_F/records/reproducibility_manifest.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: reproducibility_manifest |
| `papers/PAPER_F/records/source_to_publication_fidelity.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: source_to_publication_fidelity |
| `papers/PAPER_F/records/support_allowlist.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: support_allowlist |
| `papers/PAPER_F/records/visual_qa.json` | Bounded build, fidelity, reference, reproduction or preservation evidence: visual_qa |
| `papers/PAPER_F/references.bib` | Portable bibliography metadata, same seven references |
| `papers/PAPER_F/SHA256SUMS.txt` | Identity manifest; excludes its own hash |
| `papers/PAPER_F/SUPPLEMENTARY_RECONSTRUCTION_RECORD.md` | Attributed internal evidence history and scope |
| `papers/PAPER_F/support/CHIRAL_TRANSVERSE_INTRINSIC_EXTRACT.md` | Complete intrinsic CT sections only; mixed gate/aperture analysis excluded; original unchanged |
| `papers/PAPER_F/support/repository/kernel_physics/dynamics.py` | Unchanged accepted source snapshot statically inspected by exact verifier; never imported or executed |
| `papers/PAPER_F/support/repository/kernel_physics/readouts.py` | Unchanged accepted source snapshot statically inspected by exact verifier; never imported or executed |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/CLAUDE_GENERIC_TRANSVERSE_HARMONICS_REVIEW.md` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION.csv` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION_REPORT.md` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION_RESULTS.json` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_NORMAL_FORM_CLOSEOUT.md` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_NORMAL_FORM_RESULTS.json` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/verify_transverse_normal_form.py` | Intrinsic predecessor proof/review or preserved bounded two-seed data; provenance only except CSV read by current verifier |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_DRAFT_v0.2.md` | Controlling accepted scientific text and fidelity oracle |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py` | Standalone exact verifier for isolated re-execution |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_LITERATURE_REVIEW_v0.1.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_OPEN_QUESTIONS_v0.2.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_SOURCE_CENSUS.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_THEOREM_AND_PROVENANCE_LEDGER_v0.2.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_v0.1_to_v0.2_REVISION_LOG.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_v0.2_CHECKPOINT_REPORT.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_v0.2_VALIDATION.json` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/reviews/CLAUDE_PAPER_F_ADVERSARIAL_REVIEW_v0.1.md` | Required versioned attribution, proof classification, review or original execution evidence |
| `papers/PAPER_F/verify_isolated.py` | Reproduce unchanged exact checks in a copied four-file evidence tree |
| `papers/PAPER_F/VISUAL_QA.md` | Human-readable all-page visual inspection result |

Excluded: the local-only `records/preflight.json` inventory; all runtime installations, tool binaries, caches, render PNGs/contact sheets, broad gate/torus materials, unrelated working files and complete historical archives. CT's mixed original stays in place; only its intrinsic excerpt is supplied. All original v0.1/v0.2 files stay unchanged.
