# Proof review and editorial notes

20 October 2026 · Manuscript v0.3 local final-review draft · For GPT and Hilmir's review

The manuscript consolidates R0–R9 into one argument with six supporting appendices. The claim/source map supplies statement-level provenance; the source manifest identifies the exact files by SHA-256. These records are a compact private review aid, not a new scientific report series or publication approval.

This separately versioned v0.3 records completed numerical verification without changing the accepted mathematics. E01–E06 were closed by GPT's revision receipt. The standalone numerical audit and GPT's exact replay were subsequently accepted by the numerical-audit closure receipt. Both are copied in `evidence/`; neither was executed again here. This document pass updates status, citations, coverage and provenance only.

The written-algebra and manual-arithmetic record below is retained from the accepted v0.2 notes, which in turn identify their v0.1 origin. “Reviewed” and “checked in writing” in those historical passages describe that earlier work, not fresh scientific evaluation in this pass. The 37 source identities, the known R6 conservative arithmetic clarification and the R9 omitted-plus reconciliation are preserved. Current numerical coverage is recorded separately.

## Retained written-review record from v0.1/v0.2

Written algebra was used to review the actual shifted-index section, its determinant/area formula and positive throat; the surrounding-area complement; finite notch parameter signs and convexity tests; cone crossing and signed-angle threshold logic; the same-state fan witness; state/observer ordering; native versus envelope/clock attribution; proper/improper actions and full-Z residual signs; the norm expansion and cofactor identity; simultaneous phase reduction; the exact weighted finite-step criterion; and the logical separation between abstract phase domains and inclusion of actual inputs.

The domain proof retains its closed Cartesian-product quantifiers, positive-magnitude restrictions and finite-step effects. The fourth-domain loss sign extends to arbitrary positive amplitudes; its fixed absolute margin does not. The report's nonzero-component restriction on common-phase covariance is retained, while conjugation commutation includes the source's zero convention.

The draft does not infer contact from an infinite plane alone, a later observation from an equal-time identity, inverse-time evolution from forward commutation, or physical flow from section area.

## Written arithmetic and known corrections

The R6 correction is:

```text
1.41(0.001050 + 0.0000151) + 0.00000004 + 0.000003
= 0.001501791 + 0.00000004 + 0.000003
= 0.001504831 < 0.00151.
```

R6's printed `0.001504871` is slightly larger and still conservative. The original report is unchanged.

The final R8 gain-margin expansion was checked in writing:

```text
0.140 × 0.284 = 0.03976
0.140 × 0.362 = 0.05068
0.289 × 0.369 = 0.106641

0.1(0.03976)^2 + 0.08(0.05068)^2 − 0.002(0.106641)^2
= 0.00015808576 + 0.000205476992 − 0.000022744605762
= 0.000340818146238 > 0.00034.
```

The loss-margin expansion was checked in writing:

```text
0.174 × 0.328 = 0.057072
0.328 × 0.415 = 0.13612
0.174 × 0.415 = 0.07221

0.28(0.057072)^2 + 0.00039(0.13612)^2 + 0.30(0.07221)^2
= 0.00091201969152 + 0.000007226175216 + 0.00156428523
= 0.002483531096736 > 0.00248.
```

These are the original manual decimal expansions. Intermediate component transcription errors in the v0.1 working manuscript were corrected before delivery; the original R8 final margins did not change. The later standalone audit also checked these inequalities. No decimal expansion was recalculated in this document-only pass.

The finite notch formula contains `+ ζ_N j_k` between its radial and height terms, restored using R2 equations (7)–(8). The manifest-bound local R9 equation (11) actually omits the plus sign: its consecutive lines end in `)g_k` and begin `\zeta_Nj_k+`. The v0.2 literal re-read gave SHA-256 `3a5c402a0ce02421aa1997a4152ea2292d096acd4a03059adb083df04712a554`, exactly the manifest and GPT-review identity. The v0.1 statement that this local R9 already contained the sign was incorrect. There is no different source copy or substitution. The manuscript equation was already correct; v0.2 corrects its provenance account. Neither R2 nor R9 was edited.

Appendix A.2 now reproduces R4 §5.4 equations (32)–(34): the two actual triangle types bound the radial section by `L(eta) = min{a sqrt(3)(1-eta)/2, a(1-3eta/2)}`. At each perturbed first endpoint's own height, the inherited bounds `0 < eta_1 < .097`, `L(eta_1) > .1144` and `R_1 < .109` yield the interior clearance. The projections and star-shaped disk implication are written out. The numerical height/radical substitutions remain inherited. The v0.2 restoration did not itself close their independent audit; the subsequent standalone audit and GPT numerical closure now close the specified numerical obligation.

A draft overstatement about direction was caught by re-reading R7 §6.2 and removed. The supported conclusions are:

- Each polynomial stage and each synchronization stage changes direction.
- The complete 2 → 3 transition decreases the vertical fraction and therefore changes direction.
- The sign of the third synchronization's vertical-fraction change is unresolved by the supplied bounds.
- The fourth-update stage and net vertical-fraction changes, and the net 3 → 4 direction change, remain unresolved.

Two individually established stage changes do not establish their net change. Overlapping intervals do not imply mixed behavior or constancy.

## Inherited numerical dependencies and their completed scoped audit

The quantitative certificate retains its inherited provenance and original bounds. The later standalone evaluator independently checked the required numerical dependencies; the same unchanged checker was then replayed by GPT. No scientific execution is attributed to this v0.3 document pass. The following original dependency list is retained to identify what required that later check:

1. R3 §7.3 and R6 §3.1: exact initial radical/phase enclosures and inclusion in the comparison ball.
2. R6 §§3.2–3.4: polynomial residuals, arctangent quotients, synchronization increments and full-update residual bounds; coverage by the nonzero domains; nominal and original-box recurrences.
3. R4–R6: readout endpoint intervals. The geometric implications are shown in Appendix A, including the directional finite-edge argument at observation four.
4. R7 §§3–6: detailed norm-budget endpoint arithmetic, chiral component/magnitude bounds and correlated direction refinements. Their formulas and error allowances are carried into Appendix C.
5. R8 §6: actual-image phase inclusion, which reuses the preceding residual chain. Repetition of R6's results in R7 and R8 is not independent verification.

The intermediate trigonometric enclosures in the phase-domain theorems were reproduced with the alternating-polynomial remainder method and reviewed in writing for sign, monotonicity and margin use. The original consolidation did not freshly re-expand every rational endpoint substitution. Those whole-domain numerical inequalities and the separate original-box inclusion chain were subsequently checked by the standalone audit. The theorem proofs remain logically independent of the trajectory outcome table; applying them to the original inputs still uses the inherited, now checked inclusion chain.

No contradictory source premise was identified in the earlier consolidation. The specified numerical obligations above are now closed within the accepted scope. No original interval, coefficient, state, geometry or schedule changed.

The six passed numerical blocks cover initial-state/radical inclusion; polynomial and full-update residuals; nonzero-domain coverage and propagation; finite-region/readout comparisons; norm/chirality mechanisms; and the full closed phase-domain products with actual-input inclusion. Exact statement-level scope and proof-block identifiers are supplied by the audit's `CLAIM_AUDIT_COVERAGE.csv` and copied into the added fields of `CLAIM_SOURCE_MAP.csv`; this prose does not expand any row's coverage.

The accepted totals are 768 scalar bound records (731 `VERIFIED_RIGOROUS`, 37 `VERIFIED_EXACT`), 58 arithmetic self-checks and eight exact supporting-identity checks, counted separately. Of 37 claim rows, 14 have quantitative checks within scope, six have supporting-definition/identity checks only, and 17 are `OUTSIDE_NUMERICAL_SCOPE`. These counts do not turn supporting identities into full-claim proofs or outside-scope rows into failures; overlapping per-claim records are not added.

The original claim-map columns, including v0.2's historical `review_status`, are retained unchanged. Current audit status is in the separate audit/replay columns. All 37 original scientific source dictionaries and the prior revision-provenance object are unchanged. The added 11 supporting-input records are not new scientific source claims.

GPT inspected and replayed the same unchanged checker in an isolated environment; all 768 scalar records matched exactly. Its copied-input identity checks did not inspect unavailable original Windows source paths. This is not a third independently written evaluator or human peer review. The outward interval evidence supports whole-domain statements; high-precision nominal agreement remains corroboration.

The ideal-formula certificate is conditional on the interval implementation, integer/Fraction arithmetic, source transcription and analytic remainder bounds. It is not proof-assistant verification, production binary64 certification or physical validation. The unresolved third-synchronization/fourth-stage projection comparisons and net 3 → 4 direction question remain unresolved. No tighter audit bound is substituted or mined for a new conclusion.

## Editorial and bibliographic decisions

- The three main parts follow geometry → placed observations → native mechanism. R9 is integrated into the first two parts; it is not appended as a separate new programme.
- Bibliography entries use actual local report titles. In particular R7's report title is *Stage-by-Stage Explanation Through Update Four*, and R9's is *Z and the Central Crystal — Reversal and Upper/Lower Correspondence*. These differ slightly from work-order titles.
- R0–R2 are dated 19 October 2026; R3–R9 are dated 20 October 2026. The bibliography gives their shared year, version and unpublished status.
- Paper A's consulted title metadata supplies Hilmir's name but no explicit revision or date. Its exact source bytes are recorded instead of inventing metadata. Paper B v0.1.2, Paper C v1.0.1 and Paper E v0.1.1 are the editions consulted. Paper E's qualified status notice is not expanded into a new acceptance claim.
- Report authorship is not inferred from the manuscript's author. The manuscript follows established attribution practice and does not invent an affiliation, coauthor, DOI, destination journal or new licence.
- One retained atlas figure is used: candidate 00, PLUS, zero member, width-one host. It was visually inspected and copied byte for byte. The caption distinguishes its source parameter labels from observer time and states that no trajectory is depicted.
- The readable paper contains no absolute local source paths. The private manifest and source map carry file provenance. No chat excerpt or discussion drawing is added. The v0.3 ZIP additionally preserves the explicitly requested local audit/review evidence and editorial work order.
- References are embedded in `manuscript.tex`; no separate `.bib` file is needed.
- E01 replaces the diagonal-flip description with the exact shifted-index connectivity statement. E02 retains simultaneous channel/label covariance and explicitly includes the fixed-configuration exceptions `Pk = k` and `epsilon = 0`; vanishing on a particular state is not a general identity.
- Section 12.3 explicitly assumes `lambda in [.16999999, .17000001]` throughout, including the finite-step overshoot example. The exact identities are not confused with the strict parameter-dependent inequalities.
- The exact witness locator is R2 §7. R8 already uses zeta for the phase mean; the crosswalk now records unchanged notation.
- The Section 1 author-facing paragraph remains provisional and byte-equivalent after newline normalization. It is reproduced verbatim under “Hilmir's wording review — pending” in `REVISION_DISPOSITION.md`. Its retention and this task's authorization do not constitute his approval; no alternative is substituted.
- Bibliography entries [25] and [26] identify the completed audit (Codex preparation) and GPT review/replay/closure as local unpublished supporting review materials. They add no human coauthor, physical premise or publication authorization.

## Document production and inspection — v0.3

Compilation used the existing local Tectonic 0.17.0 executable directly, with a copy of v0.2's TeX cache confined to the new `build/` directory, `--only-cached`, and `--untrusted`. No older project build script was run. Cached TeX Gyre Pagella fonts and the unchanged retained atlas image were used. No software was installed or scientific environment changed.

Document editing/comparison, metadata extraction and packaging helpers ran with `conda activate torment` and Python 3.11.15. PDF extraction used the existing bundled pure-Python pypdf 6.10.0 library through an explicit module path. This imports no project scientific module and evaluates no scientific formula. Poppler rendered the final PDF at 120 dpi.

All 29 A4 pages were individually inspected. The three underfull paragraph warnings at source lines 1596–1602, 1654–1658 and 1867–1871 correspond to readable paragraphs on pages 24, 25 and 28. No clipping, missing glyph, unresolved reference/citation or duplicate label was found. Contents page numbers, including Part III on page 15, agree with the rendered headings. Page 29 contains the remaining bibliography; no smaller text was used to keep 28 pages.

The lexical comparisons in `build/review/DOCUMENT_COMPARISON.json` preserve all mathematical spans, equation/table environments, theorem/proposition bodies, figure environment, author paragraph, labels, 37 original claim rows/columns and 37 scientific source records. The figure file is byte-identical. `DIFF_FROM_v0.2.patch` and `build/review/EDIT_LEDGER.json` expose the complete TeX changes.

See `README_REVIEW.md` for command records, `build/review/PAGE_INSPECTION.md` for the final inspected PDF identity and each page's disposition, and the artifact/preservation manifests for hashes. Before/after hashing covers preserved inputs actually used, not a whole-machine or live-repository audit.

No scientific evaluator, native recurrence, simulation, test, project application or audit replay was run in this pass. No fifth update, source refresh, repository edit, publication action or SRG work occurred. The v0.3 document, Hilmir's wording and publication each retain their separate review boundary.
