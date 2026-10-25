# Input and context navigation

The current authority is Hilmir's request to execute REPLAY_01 and the enclosed [work order](handoff/CODEX_SIM07_UNIVERSE_REPLAY_01_WORK_ORDER.md). [RUN_SPECIFICATION.json](handoff/RUN_SPECIFICATION.json) is its frozen configuration/comparison metadata. It is not another engine. Instructions retained from previous stages are historical context; their earlier zero-run statements remain true for those earlier submissions and do not prevent the two executions explicitly authorized later.

- [GPT scientific acceptance/review](handoff/context/SIM07_GPT_SCIENTIFIC_REVIEW.md) and [acceptance receipt](handoff/context/GPT_ACCEPTANCE_RECEIPT.json): accepted construction, no required scientific correction.
- [Construction](handoff/context/CONSTRUCTION.md), [original aggregate evidence](handoff/context/ORIGINAL_EVIDENCE.md), [proposal-era replay note](handoff/context/REPLAY_DECISION_NOTE.md): unchanged convenience copies.
- [Complete accepted archive](handoff/inputs/SIM07_UNIVERSE_GPT_REVIEW_AND_ACCEPTANCE.zip): includes full source-package tree, independent review and unchanged original submitted ZIP. It is preserved as supplied, not partially rewritten or executed.
- [Original source](handoff/originals/srg_condensate_breaking.py) and [original historical table](handoff/originals/full_universe.csv): verified convenience copies of the exact accepted members.
- [Handoff input manifest](handoff/INPUT_MANIFEST.json), [handoff payload manifest](handoff/HANDOFF_MANIFEST.json), [preparation receipt](handoff/PREPARATION_RECEIPT.json): supplied provenance, unchanged.

Inherited links in `handoff/context` sometimes refer to paths inside the accepted archive's `source_package` or independent review tree. They are intentionally unchanged and should be resolved within that archive; see the supplied [context README](handoff/context/README.md). They are not claims that those historical paths were separately extracted at this package root. New review documents link to existing current payload paths.

The final `REVIEW_ZIP_IDENTITY.json` is an external sidecar beside the review ZIP, intentionally not an internal target. It records the ZIP hash, size, manifest identity and verification result after closing and reading the finished archive. The archive cannot include its own hash receipt without circularity.
