# GPT manuscript review — Native Stepping and Exchange Cadence

**Reviewed:** 9 November 2026, Atlantic/Reykjavik  
**Paper:** *Native Stepping and Exchange Cadence in the Reciprocal Chiral Exchange Candidate*, v0.1  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Decision:** Scientifically accepted for publication after the five scoped editorial corrections below and verification of the corrected final build. A separate mathematical fix order is unnecessary.

The submitted manuscript preserves the accepted F01–F12 results and their proof structure. The actual post-F initial receiving theorem retains its fixed-tuple, pointwise short-time scope. The later capacity-sized receiving-and-recovery theorem under native stepping remains unproved, and no physical cadence is selected. The small corrections restore precision already present in the accepted argument and repair printed source locators; they do not change its equations or add a new result.

The author's current request authorizes a combined correction-and-push order when the review finds only small fixes. That condition is met. Codex may complete the specified editorial changes, rebuild and verify the final edition, then perform the scoped publication without another routine approval. This review does not claim that the not-yet-built corrected PDF has already been rendered, inspected or published.

## 1. Exact submitted material reviewed

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Submitted 15-page PDF | 133,293 | `85481d9211d2451370fdedd50e4ece5a0151c79f1eb02580b3ed587093341db3` |
| Complete Codex manuscript review ZIP | 9,185,627 | `2edfe8b52c4208a78ca0896db4cb023147deddc459e9c09bd12f0dd9e0a711cb` |
| Original accepted F01–F12 proof | 34,961 | `7be198c8fb566aebd9f92f0da8f0e0386a0a87c7acd0cd21fd38a9774888b6a2` |
| Actual prior GPT scientific acceptance | 15,928 | `071f11260fcaecca127d49298a01d479f213ae769e4c3e8e82b000ead1fb52a5` |

The submitted edition has 50 files including its self-excluded manifest; the proposed paper tree has 51 files including its landing README. These are the original candidate counts, before the publication-specific records described in the push order.

The review compared the actual manuscript sources, PDF, final auxiliary records, crosswalk and evidence with the issued paper order and accepted scientific material. Separate reviewers examined accounting/cadence, the post-F source/activity/capacity argument, and package/source provenance. The lead reviewer freshly rendered and individually inspected every page of the exact submitted PDF.

## 2. Required small editorial corrections

All paths below are relative to the new edition's `manuscript/` directory. `EDITORIAL_PATCHES.json` supplies exact guarded byte replacements; the readable diff and replacement source files accompany the publication packet.

| ID | Location | Required correction | Reason |
| --- | --- | --- | --- |
| E01 | `main.tex`, abstract | Change “the invariant storage floor changes at a native jump, so the old capacity cannot be carried across unchanged” to “the invariant storage floor can change at a native jump, so the old capacity cannot in general be carried across unchanged”. | The general identity allows unchanged floor/capacity in particular cases; the abstract should state the possibility rather than a universal change. |
| E02 | `main.tex`, abstract | Replace “an algebraic ceiling ratio tending to 1.132216337515111” with wording that says its limit is **approximately** that decimal. | The body gives the exact rational and an approximate decimal correctly. |
| E03 | `activity.tex`, the sentence introducing `eq:a35` / printed equation (5.3) | Explicitly restrict the weight definition/bound to **\(|u|\le\phi\)**. | The nonnegative weight bound is used only in this phase cone. All subsequent uses already satisfy the restriction; it should accompany the displayed assertion. |
| E04 | `dark.tex`, stationarity paragraph | Say: “With arbitrary external preload, stationarity is no longer guaranteed, because \(J^Ty\) can be nonzero.” Retain the citation. | This preserves the accepted possibility statement rather than implying that every preload destroys stationarity. |
| E05 | `accounts.tex` and `references.tex` | Change RX `Section 5` to `Section 7` for the transfer accounts; change RX `Proposition 5.1` to `Proposition 7.1` for the retained-storage ratio; correct the same section number in the bibliography. | The pinned RX paper places “Transfer counts and receiver ratios” in Section 7, with “Restricted retained-storage ratio” as Proposition 7.1. Section 5 concerns dark states and the restrictive exchange invariant. |

These are five correction groups, seven exact text replacements across five TeX files. E05 has three occurrences. The old and new text, affected source identities and intended resulting hashes are recorded explicitly. All 59 accepted display bodies remain unchanged by the patch.

The source corrections require a fresh PDF build. All current PDF/source-bound verification records, printed crosswalk references/pages, font/navigation checks and final page inspections must then be refreshed. Historical acceptance documents, scientific evidence and the original submitted ZIP remain unchanged.

## 3. Mathematical fidelity findings

**F01–F04: model and accounts.** The exact simultaneous native map, fixed tuple, zero convention and F-first order survive typesetting. The inherited mild/strong solution framework is used correctly without a second weak derivative of tent profiles. Finite-round and arbitrary-window endpoint conventions remain distinct. Recovery attributable to exchange subtracts the native baseline, with positive denominators stated before division. The invariant floor is constant within exchange while capacity generally changes; the preload envelope and capacity/floor jump identity have the correct signs.

**F05–F06: first native jump.** The complete finite-square calculation, mixed/graph terms, both baseline signs, rational witnesses, unique sign threshold and comparison with the old vanishing capacity are preserved. The exit argument concerns the exact old launch family, including a common phase/amplitude factor. It does not claim exit from the larger coherent domain or impossibility of receiving/recovery.

**F07–F08: source and actual initial receiving.** The full-interval phase-order proof, simultaneous convex weights, gap factor, raw-port convention and exact source coefficient agree with the accepted argument. Theorem 5.1 uses the actual post-native preparation, retains receiver feedback and correctly invokes the general empty-external activity proposition. Its duration remains pointwise in phase and parameters, restricted to time before the next jump. The receiver-storage factor and all leading coefficients are correct. E03 makes an already-used phase-domain restriction explicit.

**F09: local capacity.** The strict branch gap is local at fixed nonzero native detuning. Analyticity, conjugation parity and cancellation of the second-order real contribution justify the stated remainder. The exact rational coefficient and ceiling-ratio limit agree. No achieved-transfer or efficiency increase is asserted.

**F10–F12: cadence and scope.** Strong continuity is applied at the fixed post-F state. The fixed-finite-N argument separately assumes continuity at the encountered native states and uses inherited bounded-energy dependence. No increasing-N limit, physical clock or infinite-step bound is inferred. The real-state witness uses exact mathematics, empty external preparation, uniqueness and finite induction. Later baseline signs and floating-point zeros are not overclaimed. The later hybrid receiving/recovery gap remains explicit throughout.

No missing critical proof transition or substantive mathematical blocker was found. The original 59 display bodies preserve quantities, operators and matrix/cases structure under the declared notation and layout changes. The proposed editorial patch changes no display body.

## 4. PDF and document review

The lead reviewer inspected all **15** freshly rendered pages individually at **125 dpi**. The title, accented author name, equations, tables of quantities, proof continuations, page numbering and bibliography are readable. No clipping, overlap, missing symbol, broken proof continuation or unreadable formula requires repair. The whitespace before the separate reference page is intentional.

The PDF has **18 embedded fonts**, **24 bookmarks** and **49 link annotations**. The four external bibliography targets are retained commit-pinned primary-source URLs. All six bibliography keys and internal targets resolve. The grouped E05 correction concerns the printed numbered locators, not missing link targets. All 18 optional numbered citations were checked; the other RX/PC/RR locators are correct.

`review_evidence/pdf_review/GPT_VISUAL_REVIEW.json` binds each page observation and fresh render hash to the submitted PDF. These observations cannot be carried forward as inspection of the corrected rebuild. Codex must inspect every page of that final PDF and bind the refreshed record to its actual new hash.

The PDF's preparation-status text can remain a historical statement, following the preceding publication's dated-disposition convention. The new publication wrappers and dated status record must make the later GPT review, scoped editorial completion and author publication GO clear. No extra PDF rewrite is required merely to change historical preparation-status wording.

## 5. Package, source and crosswalk audit

The separate package audit passed **133 independent checks**:

| Check | Result |
| --- | --- |
| Submitted review container | 106 safe unique members, 105 exhaustive manifest payloads, CRC and every payload length/hash verified |
| Candidate inventory | 50 edition files and 51 proposed new paper-tree files; original allowlist matches |
| Received order inputs | All four match the independently retained paper-order delivery |
| Scoped input preservation | All 227 recorded occurrences reconcile: 4 received files + 22 paper-packet files + 201 accepted-review files |
| Accepted evidence copies | All 14 copied files match their originals |
| Embedded primary sources | All 144 lengths, hashes, paths and Git blob identities agree |
| Claim/source coverage | All 12 complete F rows, 56 source-locator records and 8 historical support rows preserved |
| Final manuscript crosswalk | All 87 labels and 261 destination occurrences bind to actual TeX, auxiliary records and PDF pages |
| Equation fidelity | All 59 accepted display bodies preserve mathematical content under the stated notation/layout map |
| Build binding | All 11 TeX files, build helper and submitted PDF match the final build receipt |

The separately uploaded completion report matches its archive copy. The PDF and ledger were available inside the ZIP, but separate standalone copies were not uploaded. Their recorded receipt identities match the packaged copies; this review does not claim an independently observed comparison with absent standalone files.

The 227-entry finding covers supplied bytes and retained archives. It does not establish a fresh snapshot of the operator's Windows checkout. No submitted workflow or scientific script was executed during this review. Only newly written audit/verification code and PDF inspection tools were used.

## 6. Current repository observation and publication scope

A read-only GitHub observation on 9 November 2026 found `main` at:

```text
6b1ef6494a4d4c34398ba9d9e5a7afce1fb03f37
```

The new `papers/NATIVE_F_STEPPING_EXCHANGE_CADENCE/` directory was absent. The observed root README is 31,333 bytes, SHA-256 `084a66033aaa95966bdfbc259b0ed17890d840ad56a11037f67299cae39ce2d7`, Git blob `a0e38261650b4e2c390d9812cf44803229e8342d`. A concrete append-only catalog preview is supplied. Its existing byte prefix is unchanged.

This is a preparation-time observation. Codex must fetch and recheck the actual baseline, destination and root README during execution. The publication scope is this new paper tree and one catalog entry. The prior receiving/recovery publication and all unrelated repository paths remain outside the change.

The push order permits the five specified editorial groups, required regenerated document records, normal publication wrapper/status updates, and five named publication-decision/closeout records. The expected new-paper tree is 56 files, with one separate root README modification if the entry is absent. The exact final allowlist and hashes must be frozen after the rebuild; the count alone is not a scope check.

## 7. Release condition and stop boundary

The combined Codex order must apply E01–E05 exactly, build the corrected PDF, recheck all final document/source records and individually inspect all final pages. Once those checks pass, the author's request authorizes one ordinary scoped commit and normal push to `origin/main`, followed by fresh commit-pinned byte verification of every changed file and a truthful CI/closeout record.

No additional routine author approval is needed for these specified changes. A newly discovered mathematical contradiction, conflicting existing edition, access restriction or unavoidable change outside the authorized scope is a genuine blocker. The open later receiving/recovery theorem and the physical-clock question are not publication defects or new assignments.

No commit or push was performed by this GPT review. Publication execution belongs to the supplied Codex order. No successor research is started.
