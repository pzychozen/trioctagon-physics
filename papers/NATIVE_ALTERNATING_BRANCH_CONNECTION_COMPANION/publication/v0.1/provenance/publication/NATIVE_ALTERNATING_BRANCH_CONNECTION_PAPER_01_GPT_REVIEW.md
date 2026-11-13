# GPT manuscript review — Native alternating-branch connection companion

**Date:** 12 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Manuscript:** *Certified Connection from Local Period-Doubling to the Captured Alternating Cycle in the Native Triad*, v0.1, 13 pages  
**Disposition:** **Mathematical content, interpretation and layout accepted. No manuscript equation, proof or layout correction required.**  
**Remaining finalization:** E01, a documentary raw-byte hash correction in the document-check helper, plus ordinary publication-status finalization after author authorization.  
**Authority:** This is project-internal manuscript review. It is not external peer review, a new computer-assisted theorem certification, author publication approval, or a completed publication.

## 1. Reviewed object and scope

The standalone PDF is byte-identical to the PDF in the supplied manuscript review ZIP. It has 13 pages, 127,629 bytes and SHA-256:

`7a792a179040faa203295f0f903992a6bb55902869c43dafde758c48fd851035`.

The supplied review archive has SHA-256:

`6d80f33bd11be2176d6ba875ddd0b6fd263099675bb3f13179081053bf396f79`.

I reviewed the complete reader-facing manuscript and editable source against the retained accepted proof report, preceding GPT scientific acceptance, relevant M2/M3 premises, six-record ledger, saved certificate summaries and the manuscript commission. I independently rendered the supplied PDF and opened all thirteen pages for visual inspection. The accepted mathematical investigation is reused; no solver, trajectory, interval-engine replay, certificate generation, historical suite or new stability assessment was executed in this manuscript review.

The manuscript faithfully distinguishes the complete branch connection from the narrower stability conclusion. Nothing in this disposition closes the unresolved full-range attraction question.

## 2. Mathematical and interpretive assessment

### 2.1 Exact family and inherited premises — I01/I02

Section 2 preserves the simultaneous native prestage followed by simultaneous harmonic-three synchronization, the exact rational interpretation of the terminating coefficient decimals, and the positive host selected by the original accepted box. The slice basis, compression, exact critical value and critical orientation all refer to that same host. Rounded displays are not substituted for the exact objects.

The regular-domain qualification on common-phase and conjugation equivariance is retained. The positive gauge uses the conjugate of the projected complex scalar; its overbar is present both in the TeX and in the rendered PDF. The gauge is explicitly a coordinate representation, not an extra evolution step.

The corrected M2 coefficient includes amplitude slaving and the second-iterate cycle multiplier is stated as `1 - 4 sigma mu + O(mu^2)`. M2 attraction remains qualitative near onset. M3 uses the exact rational `Up`, its accepted two-step uniqueness and H-exchange, and the repaired sufficient entrance index 301. The old `Um` is correctly excluded as an outer image enclosure rather than an actual trap. The paper does not repeat the accepted endpoint trajectory calculation.

### 2.2 Removable formulation and genuine onset — N01

Equations (3.1)–(3.16) retain the accepted normalized coordinates and exact divided-difference formulation. The critical projection excludes the trivial equilibrium for positive mu. The fixed-positive-parameter determinant `t^5/(2 nu)` is stated with its proper scope; it does not assert invertibility at the collapsed onset state.

The cubic prestage, harmonic numerator, entire-function definitions and gauge agree with the accepted derivation. Exact host and critical-vector identities, rather than small numerical residuals, justify cancellation of the constant terms. The value and derivative tails for the 18 retained entire-function terms are preserved with their stated domain.

The limiting Jacobian in (4.5) retains its generally nonzero lower-left coupling. Its block invertibility and the identification of `X0 = wR/2`, `nu0 = c_nf/sigma` and the noncritical coordinate give the correct onset interpretation. The first uniform patch includes zero. The manuscript does not assume that a chosen numerical offset belongs to M2's unspecified sufficiently-small interval, or treat a qualitative asymptotic remainder as a certified error bar.

### 2.3 Uniform continuation, joins and endpoint — N02

Lemma 5.1 correctly separates existence from the root-identity argument. A self-map and weighted derivative bound establish a unique root in each exact box; the inverse-defect argument justifies nonsingularity of the rational preconditioner and state Jacobian. The center-defect estimate uses a fixed preconditioner before the parameter-width product.

The exact partition consists of 128 intervals `[i/25600, (i+1)/25600]`. It covers `[0, 1/200]`. At all 127 shared endpoints, the manuscript uses a convex uniqueness region containing both adjacent solutions, not mere overlap of interval boxes. A separate connector self-map is not needed because the two roots already exist. The distinction between exact rational boxes and outward evaluation supersets is retained.

Section 6 identifies the refined endpoint through containment of the entire reconstructed enclosure in the original exact `Up`, followed by inherited M3 uniqueness. It does not identify endpoints by matching nominal values or residuals. Theorem 6.1 asserts the connected graph in the certified regions, smooth for positive parameters and continuous to the host; it does not assert global state-space uniqueness or all-interval attraction.

### 2.4 Full-state consequence — N03

The positive critical projection excludes quotient period one. Corollary 6.2 applies the inherited conjugation/common-phase argument to obtain primitive full-state period two. The complex-conjugation overbars in the lifted relation and equation (6.2) are visible and correct. The sign-reversal statement does not become a claim that W or Gamma is nonzero at every parameter. The family represents separate fixed autonomous maps, not a parameter ramp within an orbit.

### 2.5 Separate attraction result — N04

Section 7 correctly distinguishes contraction of an auxiliary root-solving map from contraction of the native dynamics. The two-step derivative identity and validated similarity-inverse bound retain the accepted assumptions. Proposition 7.1 concerns only

`4999/1000000 <= mu <= 1/200`,

with norm bound `< 0.9601` at the connected cycle. Local quotient attraction, and attraction modulo common phase, are the appropriate conclusions. No new uniform trapping neighborhood or basin is claimed.

The manuscript keeps the inherited qualitative M2 attraction, new explicit strip and inherited M3 trap separate. The broad sufficient estimates remain inconclusive; they are not classified as instability. The abstract, scope table, stability discussion and conclusion all preserve the unresolved full-range attraction boundary.

### 2.6 Contribution, provenance and reading scope

The new contribution is a connection between the previously established M2 and M3 objects. Neither period doubling, validated continuation, nor either original endpoint theorem is relabeled as new. The update-50 capture note is correctly distinguished as a different coefficient family and initial-condition question.

The historical generator/checker share an interval engine, and the manuscript discloses that fact. Its account of the earlier Linux replay and five numerical spot checks matches the retained acceptance; those are historical records, not new runs in this review. Source hashes and verification counts are not substituted for proof. Physical field, force, material motion, clock, global basin and worldwide-priority claims are not introduced.

## 3. The only required finalization correction — E01

### Observation

The current `verification/DOCUMENT_CHECK.json` contains:

- `source_hashes["tables/certificate.tex"] = 3425caeb60e28c2f901ae5f8a09c7e1e1f987abcb67acd2b1434ffdd07dd60e2`.

The actual table's raw-byte SHA-256, correctly recorded by the build receipt, table-transcription record, archive manifest and external archive audit, is:

- `b4e92700ab9024be91c88891bdb982b27f9424ec330ad33bf635ffdf84968b56`.

### Cause and scope

The document helper reads source text using universal-newline decoding and hashes that decoded/re-encoded text. The table has CRLF line endings. Replacing CRLF with LF reproduces the first hash exactly. The actual source, table content, build record and PDF have not changed. **This is not a mathematical discrepancy, changed table, damaged archive or mismatched PDF.**

### Required action

For new finalization records, make `source_hashes` mean SHA-256 of the actual raw file bytes, as the build and payload records already do. The prepared replacement helper changes only that expression and adds an explicit `source_hash_basis` declaration. If normalized-text hashes are retained separately, label them as such rather than presenting them as byte identities.

The corrected helper and exact one-site diff are supplied under `corrections/`. Its AST parses, inverse replacement recovers the original helper exactly, and evaluation of the actual revised hash expression matches all three raw source identities in the existing build receipt. That test did **not** run the entire document helper, rebuild the PDF, or execute scientific code.

Preserve the original submission and its original document-check record. Generate new current records during finalization rather than rewriting historical evidence. The required pending-status metadata assertion must also be updated when publication status is legitimately changed; that is administrative finalization, not another scientific correction.

## 4. Independently performed documentary checks

| Check | Actual outcome |
|---|---|
| Incoming ZIP, supplied sidecar, safe unique paths, CRC and external audit | PASS; 330 members |
| Self-excluding payload manifest | PASS; 329 entries cover all other members |
| Original manuscript-commission input preservation | PASS; 187 files compared byte-for-byte with the original commission ZIP |
| Prior GPT acceptance archive and its extraction | PASS; archive matches supplied original, 177 extracted members identical |
| Original scientific-review archive and extraction inside acceptance | PASS; 149 members identical |
| Standalone / archived PDF identity | PASS; 13 pages, 127,629 bytes, identical SHA-256 |
| Claim crosswalk | PASS; six claims, 66 manuscript locations and 33 accepted-source locators checked |
| Labels and citations | PASS; 75 labels, six bibliography keys; all referenced names defined |
| Relative source links / PDF link annotations | PASS; 17 source links and 62 PDF link annotations resolve within the supplied document/evidence set |
| Font embedding | PASS; 18 unique embedded fonts, inspected through the PDF font descriptors |
| Saved table transcription | PASS; 13 exact-rational comparisons, counts, partition endpoint and strip width |
| Build-source raw identities | PASS for main source, bibliography and table |
| Final compiler records | No relevant layout, unresolved-reference or missing-font errors; empty final compiler stderr |
| Independent render / visual inspection | PASS; all 13 page images opened and inspected |
| Helper correction E01 | Prepared and its actual hash expression tested against all three build-source hashes |

The word “warning” in the `infwarerr` package description is not an actual compiler warning. Label locations were checked against source locators, the retained resolved-reference record and the rendered pages; no fresh TeX compilation was performed here. The original document and scientific evidence remain unchanged.

These are documentary and presentation checks, not new theorem counts. The supplied checkout-preservation record is not relabeled as a fresh inspection of the author's Windows machine or GitHub.

## 5. Visual review

All thirteen pages were independently rendered at 145 dpi and inspected. The equations, proof blocks, four tables and bibliography are readable, with no clipping, missing glyphs, overlapping equation numbers or broken conjugation bars observed. Ordinary continuation of text across page boundaries is acceptable. No layout replacement is required.

The reviewed-copy PDF is intentionally byte-identical to the submitted PDF, so its historical pending-review wording is still visible. Final publication status belongs in the later rebuilt edition. Render hashes and per-page observations are recorded in `reviewer/FINAL_PAGE_REVIEW.json`.

## 6. Disposition and next action

The mathematical manuscript and its presentation are accepted at the existing scientific scope. E01 is a bounded documentary correction suitable for the publication finalization pass. It does not require a new scientific investigation, proof replay or manuscript rewrite.

The accompanying publication order is **prepared but inactive until the author explicitly approves publication or forwards that order as the instruction to publish**. After activation, Codex may apply E01, update current status/metadata, rebuild and inspect every page, refresh current records, publish one new companion subtree and one catalog entry in one ordinary scoped commit and normal push, and verify the actual remote bytes and CI outcome. No further scientific approval round is required for those specified changes and a faithful checked rebuild.

Paper G, all earlier editions and the accepted evidence remain unchanged. No commit, push, remote audit, publication, or new research assignment was performed in this review.

## 7. Controlling identities

- Reviewed manuscript source `main.tex`: `2d51b97e13a7ab2a8a90274c7231fa0cb94af4d31b8758a084ed35c26028fd6f`.
- Bibliography `references.tex`: `c3b4d9755384f0a0ccfa19d5a747446a743c436ad13a6b2f056c4eb613004f08`.
- Raw table `tables/certificate.tex`: `b4e92700ab9024be91c88891bdb982b27f9424ec330ad33bf635ffdf84968b56`.
- Original document helper: `d5f3a028f3029d499aaa3f2de0ffc5f96e2803a5babb755cb0d5af0c5a095b67`.
- E01 replacement helper before publication-status adaptation: `2321b16b6d38f73d3d87b119443e92613eaba7da098a97ef7f9e7c4c44fbdc1c`.
- Preserved scientific-acceptance archive: `61d131362e42c5b5408e257b8bdc03710244ef40576a118d63dbf4240c003d6f`.

The complete submitted manuscript archive, its sidecar and external audit are retained under `received/` in the publication packet. This review adds no changes to those historical bytes.
