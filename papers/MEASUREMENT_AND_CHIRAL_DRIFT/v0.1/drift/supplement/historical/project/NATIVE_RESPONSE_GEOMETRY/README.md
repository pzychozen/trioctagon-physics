# Native Response Geometry and Spectral Circulation in the Tri-Octagon Map

**Research publication v0.1.** Publication files are prepared; final GPT publication approval is pending. No journal submission, external peer review, repository release or DOI is claimed.

Subtitle: *Finite-Ring SPD Self-Adjointness, Equivariant Spatial Observables, and State-Shell Attachment*.

This standalone mathematical synthesis consolidates the completed GR0, GR1, GR2, CM0 and SA0 checkpoints. It covers the native finite-ring response spectrum, unequal-background weights, diagonal cycle obstruction, general SPD self-adjointness, triad/Bloch spectral alternatives, an exact six-ring defect and unfolding, spatial-equivariant multiplicity, adopted face representation, and regular coherence closure with its zero-stratum exception.

**RESEARCH PUBLICATION v0.1 - no new kernel implementation, kernel authority, or runtime dependency.** The native map and decoder already exist; this lane contains their mathematical analysis and publication materials. No physical gravity theory, unique core position, shell deformation law or boundary feedback is established. Three-Way remains PARKED; Paper G remains closed.

## Publication materials

- [Publication PDF](publication/Native_Response_Geometry_v0.1.pdf)
- [Complete LaTeX project](manuscript/main.tex), with nine appendices
- [45-entry theorem/claim ledger](provenance/THEOREM_LEDGER.md), created before drafting prose
- [Source/proof crosswalk](provenance/PAPER_SOURCE_CROSSWALK.md)
- [Consistency audit](provenance/CONSISTENCY_AUDIT.md) and [literature review note](provenance/LITERATURE_REVIEW_NOTE.md)
- [Numerical evidence by method](verification/NUMERICAL_EVIDENCE.md)
- [Verification summary](verification/VERIFICATION_SUMMARY.md)
- [Publication proposal and three optional public posts](PUBLICATION_PROPOSAL.md)
- [Proposed exact commit allowlist](provenance/COMMIT_ALLOWLIST.txt)
- [Publication revision record and exact changed paths](provenance/PUBLICATION_REVISION.md)

The manuscript contains written proofs. Its 429 retained predicates/checks are heterogeneous symbolic, structural and source checks, **not 429 theorems**: GR0 45, GR1 38, GR2 42, CM0 78, SA0 226. Native complex128 differences, 100-digit transcription differences, fixed-equation residuals, spectral data and quotient checks are preserved as distinct measurements. Paper-local verification adds 61 separately counted algebra/reference checks.

## Authority and preservation

Scientific source HEAD: `da461294d724997bd7033c7cea9cc9a0b5f5031d`.

The starting checkout was already dirty. [Baseline](provenance/baseline.json) and [preservation comparison](provenance/preservation.json) retain that status. The final comparison hashes all files outside this new lane, including existing papers, native kernel, UI, fixtures and untracked material. The fifteen external checkpoint report/script/results artifacts are separately hashed in [the source manifest](provenance/source_manifest.json). No predecessor script was executed into its original result file.

The evidence snapshot contains the unchanged `verification` object from each original results file, with its source hash, not a rewritten checkpoint. Original scripts and reports remain at the manifest locators. Accepted-paper/Atlas ownership is recorded in the ledger. The plus sign restored in the GR2 cycle-factor restatement is explicitly reconciled to GR1; predecessor files are unchanged.

## Reproduce

Run from this lane using a Python environment with the versions in [requirements](verification/requirements.txt). These commands write only this lane; they do not run native or checkpoint writer scripts:

```powershell
python -B verification/curate_ledger.py
python -B verification/render_ledger.py
python -B verification/render_evidence.py
python -B figures/generate_figures.py
python -B verification/verify_paper.py
python -B verification/audit_manuscript.py
python -B verification/build_paper.py --tectonic /path/to/existing/tectonic
```

The verified compiler is Tectonic 0.17.0. This is a multi-file LaTeX project with external figures. The exact executable, command, input hashes and output hash are in [the build record](publication/build_record.json). Tectonic can require its normal TeX resource cache or network access on a fresh machine. No TeX toolchain was installed for this task.

`verify_paper.py` also validates original checkpoint/native source hashes, so it requires those artifacts at the recorded provenance locations. Its mathematical checks are independent of importing or executing native code. The external evidence is intentionally referenced instead of duplicating the completed research reports and scripts. The paper-local commands do not promise a byte-identical PDF because compiler metadata may differ.

For preservation checking on this same checkout, run `python -B verification/assemble_evidence.py seal`. Do not regenerate the baseline to hide changes. The initial `assemble` command was used once to retain evidence and source hashes. The final PDF was rendered with Poppler and inspected; see [PDF QA](publication/PDF_QA.md).

## Publication status

The user-reported GPT scientific review verdict was PASS WITH MINOR REQUIRED PUBLICATION CHANGES. This revision implements those editorial changes and adds six verified external references for established mathematical context only. It makes no novelty or priority claim. Final GPT publication approval and the project owner's publication decision remain pending; this does not constitute external peer review. The proposed allowlist and GitHub text are preparatory only. **Nothing has been staged, committed, pushed, tagged, released or assigned a DOI.**

Existing blocked preview images in `tmp/` are retained byte-for-byte and excluded from the proposed allowlist. Re-render with `python -B verification/qa_pdf.py --output-dir /path/to/fresh/external/preview-directory`; the QA script requires an output directory outside this paper lane.
