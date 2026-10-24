# SRG Volume II — GPT review of candidate v0.1

**Reviewed candidate:** *Local Geometry and Resonance in Seed Explorer and Infinity*  
**Date:** 23 October 2026  
**Author / research director:** Hilmir Frímann Halldórsson  
**Scientific review:** GPT  
**Manuscript preparation:** Codex  
**Disposition:** **ACCEPT SCIENTIFIC CORE; MINOR MANUSCRIPT REVISION REQUIRED (E01–E03).**

## 1. Decision

The paper is a coherent, evidence-linked reconstruction of the selected SIM04 and SIM05 programs. The two recurrences, principal numerical conclusions, distinction between original and reproduced evidence, and four conditional propositions survive this manuscript review. No new simulation, data analysis, random draw, parameter comparison or Tower II study is needed to finish this manuscript.

There are three bounded correction items: E01 corrects the selected Seed Explorer driver's mean-amplitude definition; E02 corrects the amplitude magnitude used in Infinity's separate tensor observer; E03 repairs narrow source-line ranges. E01 and E02 are genuine source-transcription errors in the prose, not merely stylistic preferences. Neither changes the accepted observations, any of the four propositions, or any figure. The source code and prior accepted studies must not be altered to match the draft.

Final manuscript acceptance is reserved for verification of a corrected candidate. This review is not publication authorization, permission to stage or push, or acceptance of all historical interpretations. The submitted v0.1 remains unchanged.

## 2. What was actually checked

This was a read-only manuscript, mathematics, source and artifact review. I read the manuscript and accepted reviews; traced the selected update and observer equations to unchanged Python text; checked the four proofs algebraically; read the stored results behind the principal quantitative statements; and checked the 27-row claim matrix. I did not import any historical simulator, replay driver, numerical science checker or random generator, and did not calculate new trajectory statistics.

For document inspection, I rendered all 30 PDF pages, inspected the complete page sequence in overview sheets, read the extracted text alongside the TeX, and separately enlarged all ten figure pages and both central proof pages. Landscape plates are complete in the local PDF rendering; cropped previews from text extraction are not evidence of clipping in the delivered PDF. No OCR was used.

New executions here were restricted to document rendering, ZIP inspection, file hashing, byte comparisons, source-text searches, reference/link checks and writing this review. The document audit script is included. No submitted scientific script was executed. No candidate or accepted input was modified.

### Independent artifact checks

| Check | Result |
|---|---|
| Candidate archive | 90 files: 89 manifest-listed payloads plus MANIFEST.json |
| Manifest hashes and lengths | 89/89 agree; no unexplained or missing files |
| Standalone attachments | Uploaded PDF, TeX and starting guide match their ZIP members exactly |
| Work order | Embedded authoritative order matches the earlier supplied order exactly |
| Required immutable input archives | Both match the earlier conversation uploads byte for byte; both pass ZIP CRC checking |
| Copied original/study/review/table evidence | 50/50 files match a member of the accepted input archives |
| Figures | All ten selected images match the registered accepted archive members byte for byte |
| Paper structure | 30 physical PDF pages; 10 numbered figures; 4 propositions; 12 bibliography entries; 27 claim-matrix rows |
| TeX references | No unresolved labels or bibliography keys; 38 reference occurrences checked |
| Direct manuscript/bibliography links | All 35 TeX file-link occurrences resolve |
| Top-level explanatory Markdown | All 83 inspected local-link occurrences resolve |
| Compiled PDF | 151 link annotations, including 43 file-link occurrences; file targets resolve |
| Fonts and page bounds | All 18 inspected fonts embedded; no text spans outside page media boxes |
| Build identity | PDF digest agrees with final build, document-QA and page-inspection receipts |

The frozen study documents can retain relative links designed for their original archive layout. The candidate's evidence index and two immutable input archives provide that layout; the above direct-navigation claim refers to the manuscript, bibliography and root-level explanatory documents, not a claim that every relocated legacy Markdown link was rewritten.

The supplied preservation receipt also reports Windows host and worktree preservation and zero new scientific executions. I verified delivered identities and earlier available uploads, not the contents of Hilmir's live Windows filesystem or independent telemetry of Codex's execution history. That limit does not obstruct manuscript review.

### Exact candidate identities

- Review ZIP: **17,643,531 bytes**, SHA-256 `8eedae1f6b85519fed3053d592c1ca64d038135d4b9cf69fb1a8c2fbf52cc95c`.
- PDF: **3,418,207 bytes**, SHA-256 `1f625a35c76446769b473d01affc480c46f3a8738f9f43baef2b2e6313927f5d`.
- TeX: **65,414 bytes**, SHA-256 `8a7c5747d77e4bfc62035381afbae236d0a1fbc9be29d5a22218bf07a717712c`.

The full audit is in `document_integrity.json`. Counts here describe this review, not a repeat of earlier simulation validation.

## 3. Required correction E01 — selected Seed Explorer mean

**Location:** §7.1, physical PDF page 23 / printed page 22; manuscript.tex lines 328 and 332; claim matrix C19.

The first paragraph says Seed Explorer reports a *signed mean* and then contrasts that with Infinity's mean absolute amplitude. The selected Seed Explorer driver instead executes:

```python
# srg_seed_explorer.py, lines 623–625
R_mean = np.mean(np.abs(R))
R_max = np.max(np.abs(R))
R_std = np.std(R)
```

Its metric dictionary stores that R_mean at line 639. Infinity likewise records `np.mean(np.abs(R))` at line 248. Both selected programs therefore report mean absolute amplitude. Their coherence special-case branches genuinely differ: SIM04 returns 1 when std(R) < 1e-12; Infinity returns 0 when mean(abs(R)) does not exceed 1e-12. Keep that difference, and retain the signed-field standard deviation and correct coherence formula.

**Required change:** replace the signed-mean claim and the false inter-program mean contrast. Say that both selected drivers report mean |R|, while their coherence guard conditions differ. Add the precise source locators and update C19 consistently.

**Impact:** the inspected R values are positive, so signed and absolute means coincide for these records. The retained tables, plots, numerical conclusions and proofs need no change or rerun. The original SIM04 evidence account itself already labels its statistic “Mean absolute resonance”; this is a draft-level error, not a reason to rewrite that accepted input.

## 4. Required correction E02 — tensor-observer amplitude magnitude

**Location:** Appendix B, physical PDF page 28 / printed page 27; manuscript.tex line 509; claim matrix C27.

The draft says the separate Infinity eigengeometry driver multiplies each centered position by its **signed** R. Read the local variable definition, not only the later multiplication:

```python
# srg_infinity.py
# line 362
R = np.abs(field.resonance)
# line 368
top_R = R[top_idx]
# line 440
weighted_pos = relative * top_R[:, np.newaxis]
```

The actual multiplier is the amplitude magnitude |R|.

**Required change:** use “its amplitude magnitude |R|” and cite both the definition/selection (lines 361–371) and tensor assembly (440–445). C27 should point clearly to those source locations.

**Impact:** retain the conclusion that the tensor weights are R_i^2. For each vector, the quadratic term is unchanged by reversing its sign, so correcting this input description does not invalidate the tensor expression or the principal-moment inequality. The existing observation that the strict prolate branch cannot hold in exact arithmetic remains supported. This correction does not authorize executing that separate driver.

## 5. Required correction E03 — exact source navigation

**Location:** Appendix A, Table 5, physical PDF page 28 / printed page 27; manuscript.tex lines 492–493; claim matrix C20.

| Item | Current range | Correct range | Reason |
|---|---|---|---|
| S5 R sine and signed compression | 192–197 | **190–195** | Actual sine multiplication is at line 191; the current range misses it |
| S5 noise, displacement, recording | 199–205 | **198–205** | Include the noise-scale assignment at 198 as well as the draw at 199 |
| C20 selected S4 echo timing | 618–619 | **618–620** | Include the actual echo call at 620, following recomputation of current distances |

These are navigation corrections. Equations (9), (21) and (22) already use the correct operations. Do not change a coefficient or update stage to fit a mistaken locator.

An exact proposed diff for E01–E03 is included. It changes only two new candidate documents: manuscript.tex and CLAIM_EVIDENCE_MATRIX.md. It does not perform version/status housekeeping or regenerate the PDF; those belong in Codex's new candidate revision.

## 6. Recurrence and observer transcription

### Seed Explorer

Equations (1)–(11) correctly distinguish arithmetic local positional averaging from inverse-distance amplitude weighting. All local inputs are taken from the incoming boundary, even though source assignment of local positions occurs first. The source's sampled pass-dependent H normalizer, signed compressor with the 1e-9 interior offset, global center weights |U|+1e-8, signed fusion coefficient .03U, final R sine and constant .01 positional noise are in the right order.

The post-H amplitude U, not the final compressed R, supplies the fusion center and coefficient. The displacement record is not inertial velocity. The historical source attributes .618 and .087 are correctly described as unused in this selected update. The normalizer's recorded value is not promoted to an unproved continuous maximum. The nearest-neighbor self/tie caveat is present. The componentwise tanh law is correctly distinguished from rotation-invariant measurements of its output.

### Infinity

Equations (16)–(22) preserve the separate .15 and .075 local mixing strengths, shared .01*.08699*sin(.244p+pi/2) cross coefficient, simultaneous incoming R/D cross inputs, fixed sampled H normalizer, separate shifted H schedule for D, R-based fusion, R-only sine, separate signed compressors and decaying noise. The difference between .244 radians per pass and .244 cycles per pass is stated explicitly.

The program's empty-neighbor branch skips cross terms, and the uniformity proposition properly excludes empty rows. D can influence fusion through R's cross increment, but the source has no separate D-weighted center. The field labels are not substituted for a physical identification or complex-phase orthogonality.

### Observers

Except for E01 and E02's two prose descriptions, the observer reconstruction is faithful. It preserves angle standard deviation rather than variance; updated positions with incoming neighbor selections for Infinity curvature; incoming distances with outgoing amplitudes for Infinity echoes; current distances for selected SIM04 echoes; distinct signed/absolute maxima in the echo formulas; strict thresholds; diagnostic squared sums; mean of pointwise GRF reciprocals; and unchanged identities beneath overlapping plot markers.

The interpretation of 238 echoes is supported by the retained pair masks, not merely a numerical coincidence of totals. The 44 candidates are points in four groups, not 44 separate bodies. The old higher_polyhedra label is not treated as fitted geometry. The shape, memory-death, golden/zeta and anatomy discussions remain static source audits of other drivers, not executed results of the selected replay.

## 7. Four proof checks

| Proposition | Independent manuscript-level assessment |
|---|---|
| 1: minimum isolated group | Valid. Five distinct non-self choices inside a component require at least six members; six members require all 30 directed choices. It neither forces formation nor identifies a spatial solid. |
| 2: normalized interval | Valid. Under positive unclipped inputs and positive gain, the source is affine stochastic averaging. Substituting the shared gain and offset yields z_p=P_p z_(p-1). State-dependent neighbor matrices do not invalidate the one-step convex-hull argument. No unweighted-mean conservation or H-off trajectory follows. |
| 3: fusion mean displacement | Valid. Expanding the positive-weight centroid gives sum U_i(c-Y_i)=N*delta*(meanY-c), hence meanF=.03*delta*(meanY-c). The absolute-value caveat and distinction from whole-update/physical conservation are retained. |
| 4: component uniformity | Valid. Nonempty, internally supported normalized rows return a common r,d unchanged by local averaging. The remaining field operations are common scalar maps. Continued geometry can change without immediate amplitude differentiation; renewed closure is required for repeated application. No attraction, eternal disconnection or autonomous five-body reduction has been proved. |

The four propositions are accepted as mathematical exposition of the reviewed results. E01–E03 do not touch their assumptions, statements or proofs. Reused symbols in separate propositions are locally defined; I do not require a notation rewrite for this revision.

The tensor inequality in Appendix B also survives source readback. For the actual quadratic construction, the principal-moment relation does rule out the strict ratio >2 branch in exact arithmetic. E02 repairs the input description, not that result.

## 8. Quantitative claims and evidence boundaries

I read the figures and selected stored results rather than generating new measurements. The principal SIM04 contraction, component timeline, low-ranked six IDs, final-partition variance split, persistent top rank with motion, all-direction geometric spread and normalized-pair deformation claims agree with the accepted accounts and tables. The tiny pass-18 to pass-19 diameter increase is not concealed behind a monotonic-contraction claim.

The Infinity group sizes and memberships, persistence from boundary 33 to 200, near-within-group agreement, between-group levels, nonzero D, three lower clips, continuing displacement, late-stage contribution table, and observer-mask interpretation are carried over faithfully. The top-rank variations are not described as a leader controlling the recurrence.

The paper correctly distinguishes 2,785 exactly agreeing metric values from 2,985 table cells including pass labels, and distinguishes all 4,000 tolerance matches from bitwise equality. Its reference/capture repeatability is not presented as independent rerunning of the historical experiment. Earlier conditional-equation and RNG-checkpoint verification are attributed to the accepted review and explicitly not repeated during manuscript preparation.

No new statistical robustness or long-time claim is required. The paper's two-program comparison is explicitly not a controlled one-factor test of adding D. The same six IDs in both constructions do not by themselves establish the cause of their organization or a chronological lineage.

## 9. Figure and page assessment

The ten accepted figure assets are unchanged and placed with proportional scaling. The full rendered plates show complete axes, legends and captions. The orientation figure and whole-field/normalized-group views use the advertised distinctions between fixed world scales and group-normalized scales. Figure 3 correctly pairs a diameter history with an endpoint ranking, not a second time trace. Figure 9 correctly explains that the plotted coefficient lacks the additional .01 factor included in g_p. Figure 10 retains the distinction between squared-sum ratio and pointwise amplitude ratio.

I found no blocking clipping, missing glyph, unresolved printed reference, unreadable equation or table overflow. The 30-page count includes an unnumbered title page and printed pages 1–29. Several full-page plates and the sparse printed page 9 are consequences of the deliberate figure placement; I do not require repagination solely to reduce white space. Any text revision still needs a fresh visual pass because it can move equations and tables.

The paper is usable as a coherent explanatory document: conceptual orientation, complete constructions, finite behavior, observers, exact mathematics, and an explicit comparison. It is substantially more useful for the current goal than adding another simulation before consolidating these two.

## 10. Bounded next action

Codex should produce one non-overwriting candidate v0.1.1 with E01–E03 and associated version/status, evidence-matrix, editorial-note and manifest updates. Retain all scientific data, equation coefficients, four propositions, ten figure bytes and immutable input archives. Compile/render the document and return the corrected PDF, editable source, exact diff, correction disposition and scoped preservation record. Stop for GPT/Hilmir review.

Zero new simulation updates, numerical scientific reruns, random draws, new plots or new measurements are needed. Do not open Tower II, add an experiment, modify a kernel, edit a frozen study, prepare a publication payload, or perform Git writes.

**Bottom line:** the reconstruction has reached a paper-level synthesis. The remaining work is precise source-faithful correction of this candidate, not another research phase.
