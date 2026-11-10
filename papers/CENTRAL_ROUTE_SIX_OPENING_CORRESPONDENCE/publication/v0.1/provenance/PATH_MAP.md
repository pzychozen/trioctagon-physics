# Publication path mapping

The current claim ledger uses edition-relative paths. Historical `candidate/v0.1/` manuscript locations now map to the edition root; current line numbers and PDF labels/pages were refreshed after M01–M03. `inputs/` retains every one of the 73 original manuscript-packet files unchanged, so all current accepted-proof and primary-source locators resolve directly.

The historical SOURCE_IDENTITIES.json and SOURCE_MAP.md are unchanged. Their packet-relative source paths resolve under this edition's `inputs/`. Their old checkpoint and per-source identities retain their historical scope, not the new publication commit identity.

Actual GPT manuscript review: `evidence/manuscript_review/`. Current superseding author GO and exact patch/after-hashes: `evidence/authorization/`. Correction closeout and final build/document/visual records: `verification/`. Both complete accepted investigation archives remain under `inputs/accepted/`. Their internal paths refer to their own archive roots.

The original reviewed PDF, full submitted review ZIP, GPT page renders, final revised page renders and all post-push fetched bodies are retained in the external publication closeout, not duplicated as outer nested archives in Git. The publication receipt is external because it records the completed commit and remote observations.
