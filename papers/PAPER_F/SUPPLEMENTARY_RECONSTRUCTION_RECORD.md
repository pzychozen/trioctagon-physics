# Paper F: reconstruction and reproducibility supplement

This is internal research provenance, distinct from the scholarly bibliography. It accompanies the public manuscript based on the accepted scientific source v0.2. It is not a new Claude review, a new mathematical acceptance, or a claim of publication.

## Attribution and evidence layers

- **CT — Codex, 25 September 2026:** the complete intrinsic sections 2–3 of *Chiral transverse mode and registration-family exposure*. The full original is mixed-scope; only the verbatim intrinsic excerpt is packaged. Its original identity and source line range are in `records/support_allowlist.json`. The original report remains unchanged.
- **AX — Codex, 25 September 2026:** *Two-seed transverse-axis falsification*, retaining the GPT-attributed exact historical-seed decomposition, original report, 18-row CSV and original results. These are preserved binary64 observations, not new model runs.
- **CG — Claude, 25 September 2026:** *Independent review: generic transverse harmonics of chirality near the synchronized manifold*. This supplied prior review is preserved verbatim, including its finite-range/all-n distinction.
- **NF — Codex, 25 September 2026:** *Transverse normal-form proof closeout*, with its original exact verifier and results. This records the predecessor arbitrary-step argument and first-order composed-phase calculation. The old verifier is retained for provenance and was not executed during this build.
- **CR — Claude, 25 September 2026:** *Adversarial mathematical review — Paper F v0.1*. The original supplied review is copied byte-for-byte. Its reported numerical runs remain attributed review evidence; this package does not claim to rerun them.

The current manuscript and v0.2 ledger control the accepted statements. Earlier records are evidence of the reasoning's development and can contain superseded wording. Specifically, the twelve oriented roots have **three D3 orbits of sizes 6,3,3**; the D6 orbits have sizes 6,6 and stabilizers of order two, so they are not regular orbits. CR §3.6 retracts Claude's earlier regular-orbit wording in CG. The positive sign printed for X_n in CG §5 is a prose typo; the sign in the accepted formula is negative, fixed by X_1 = -epsilon/sqrt(6). NF and the v0.2 derivation preserve the correction. This distinction does not erase or edit CG.

The exact public proofs stand on their stated assumptions. The finite coefficient identities, all-degree nonresonance proof, classical fixed-parameter theorem application, explicit parameter proof and finite binary64 observations are distinct evidence classes.

## Controlling Paper F records

The immutable v0.2 manuscript, original census, v0.2 theorem/provenance ledger, v0.2 open questions, bounded literature review, revision log, original validation, checkpoint and adversarial review are included under `support/repository/research/paper_F_transverse_normal_form/`.

`S:Census` in the public paper denotes the original source census; `S:Questions` denotes the v0.2 open-question ledger; `S:AX` denotes AX; `S:Checks` denotes the unchanged v0.2 verifier, original validation and the separately attributed publication execution in `records/isolated_exact_checks.stdout.json`.

The new stdout is **a fresh isolated publication-build re-execution**, not the original captured v0.2 run. The original validation remains unchanged. Source-location and runtime fields differ naturally; every mathematical and saved-data field matches.

## Deliberate limits

```text
PAPER_F_DEPENDS_ON_THETA_LOCK = NO
EPSILON_0_05_PROVENANCE = OPEN
G_0_2_PROVENANCE = OPEN
HISTORICAL_SEED_PROVENANCE = OPEN
NEW_MODEL_RUNS = 0
NEW_CLAUDE_REVIEW = NO
```

The historical observer-lock record is retained in the untouched research packet. No lock literal is needed in the public scientific narrative. No historical rationale has been inferred, and no external observer-lock, shell-coordinate or energy parameter enters the derivation.

Gate/aperture/torus-only programs, data and figures are excluded. Two accepted kernel files are read-only source snapshots for static source-body verification, not a replacement implementation. No package code imports them.

Every included support path has an individual role and original identity in `records/support_allowlist.json`. The complete original v0.1/v0.2 packets and all original CT/AX/CG/NF/CR records remain preserved at their original locations.
