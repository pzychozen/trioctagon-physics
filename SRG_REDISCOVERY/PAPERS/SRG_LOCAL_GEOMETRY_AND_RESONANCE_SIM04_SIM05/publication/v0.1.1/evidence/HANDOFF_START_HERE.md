# SIM04 + SIM05 manuscript handoff

Read `SRG_VOLUME_II_SIM04_SIM05_CODEX_MANUSCRIPT_WORK_ORDER.md` first.

**Decision:** draft the detailed Seed Explorer / Infinity paper now, before Tower II. The order supersedes that part of the older sequencing plan; the older files remain unchanged.

**Scope:** explanatory manuscript and document review only. Zero simulator updates, no numerical reruns, no changes to historical or accepted sources, no Git or publication operations.

## Inputs

- `inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip`: complete original SIM04 submission and historical records.
- `inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip`: accepted SIM05 GPT review, independent findings and the unchanged SIM05 source package. The accepted SIM04 GPT review and its additional findings are inside `source_package/context/SIM04_GPT_REVIEW/` after extracting this archive.

Extract each input into its own read-only input folder; do not flatten the two archives into one directory. Verify identities against `INPUT_MANIFEST.json`. Already available matching local files may be used instead.

The nested SIM04 review retains historical links to its own original `input/` tree. For drafting, resolve that material through the separately supplied full SIM04 archive and create a candidate-only evidence index. Do not edit the retained review to make its historical links look new.

## Expected return

A detailed candidate PDF with editable LaTeX, legible accepted figures, exact recurrence definitions and reviewed proofs, a claim-evidence map, relative evidence links and scoped preservation records. Incorporate BOTH GPT reviews, not only the original Codex summaries. Stop for GPT/Hilmir review.

The draft should explain the two programs and the relationships between their geometry, amplitudes and observers. It does not need another simulation to be scientifically useful.
