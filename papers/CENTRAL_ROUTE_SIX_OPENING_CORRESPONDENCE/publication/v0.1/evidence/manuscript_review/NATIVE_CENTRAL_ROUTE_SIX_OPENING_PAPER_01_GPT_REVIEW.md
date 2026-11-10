# GPT review of the combined central-route and six-opening manuscript

**Date:** 10 November 2026  
**Manuscript:** *Central-Route Accounting and Six-Opening Geometry in the Reciprocal Chiral Exchange Candidate*  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Edition reviewed:** v0.1, 17 pages

## Decision

**Minor manuscript revision required: exactly three localized corrections, M01–M03.** The accepted C01–C05 results, Q01 qualification and S01–S05 results remain unchanged. The integrated paper contains the necessary arguments and preserves their assumptions. No additional scientific investigation or author geometry decision is needed to make these repairs.

The current PDF is not accepted unchanged. Its regional balance contains a superscript-comma typo; one explanatory support sentence confuses the forcing with a translated Duhamel integrand; and the C6 paragraph needs to distinguish its width-one notation from the theorem's common scaling. The corrected source passages have been prepared in this packet. A corrected PDF has **not** been built or accepted by this review.

The next task is a narrow Codex correction and document rebuild, followed by confirmation against the revised PDF identity. This review does not authorize publication.

## Exact material reviewed

| Item | Verified identity |
| --- | --- |
| Standalone PDF | `CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE_v0.1.pdf` |
| PDF bytes / pages | 196,911 bytes / 17 A4 pages |
| PDF SHA-256 | `5cca7c826776fc935dd3e20fa74088221fe2c18e7862569024b5045c8322866b` |
| Submitted review ZIP | `NATIVE_CENTRAL_ROUTE_SIX_OPENING_PAPER_01_REVIEW.zip` |
| ZIP bytes / members | 12,916,259 bytes / 144 files |
| ZIP SHA-256 | `61b673652d7cd42b4ad6359bea6cb1ff8b73a9fe185391d17ec2dbdd31580f7e` |
| Original manuscript-order packet SHA-256 | `2124d23bc9c7dd62ef76951e2eaf1c0ce5c953ec8958c8b5cbd5f6753db1df86` |

The standalone PDF is byte-identical to the PDF inside the submitted review archive. The build, document, visual-inspection, packaging and claim-ledger records all bind to that same PDF hash. The original received archive and PDF are retained unchanged under `submitted/` in this GPT packet.

## Required corrections

### M01 — complementary-arc notation

**Location:** PDF page 7, equation (3.9), `eq:regionalbalance`; `candidate/v0.1/sections/03_account.tex`, original line 82.

Replace `I_{R_B}^{,c}` with `I_{R_B}^{c}`. The comma is currently printed as part of the superscript. The integral is over the complementary carrier arc; its minus sign, integrand, and native-jump convention are correct.

This is a typesetting correction. It does not remove the complementary work or alter the regional account.

### M02 — fixed forcing support and translated integrands

**Location:** PDF page 8, first paragraph of Section 4.1, immediately after equation (4.2); `candidate/v0.1/sections/04_launch.tex`, original line 13.

The manuscript currently says that every integrand is supported in the same fixed union. As a function of the observation coordinate, however, the integrand is

\[
[Bq(t')](s\mp c(t-t')),
\]

whose support is translated. The **unshifted forcing** \(Bq(t')\) is supported in the fixed union \(\mathcal S_b\) at every forcing time. That is the fact used in the valid support-gap proof.

The prepared replacement states this distinction and explicitly connects it to the backward-characteristic argument: a point at circular distance greater than \(ct\) cannot encounter the forcing support during the integration interval. The Duhamel formula, equation (4.3), Q01 criterion, and receiving theorem remain unchanged.

### M03 — width convention in the C6 observation paragraph

**Location:** PDF page 13, Section 6.4, paragraph following equation (6.3); `candidate/v0.1/sections/06_transport.tex`, original line 43.

The displayed observation uses the width-one \(\gamma_0\), \(L_c\), and \(d_X(s)=\|X-\gamma_0(s)\|\). Its immediate geometric consequence is

\[
d_X(s)>297/5000.
\]

The factor \(w_{\rm host}\) belongs to the simultaneous common scaling proved in Theorem 5.2. The prepared text first gives the width-one bound, then states that the distance is strictly greater than \(297w_{\rm host}/5000\) when the carrier and central geometry are commonly scaled, with the arclength interval scaled accordingly.

The separation theorem already states the correct scaling assumptions. This repair makes their use in C6 explicit. It changes no carrier, observation law, state history, geometry, or physical interpretation.

## Mathematical and source findings

The paper forms a coherent argument from the two accepted investigations. It introduces the actual model and spatial dictionary, derives the radial and regional account, proves the receiving comparison, proves the six-opening clearance, and then identifies the remaining spatial and work registration.

| Coverage | Review finding |
| --- | --- |
| C01 / S01 | The raw fixed-yaw registration, positioned stationary axes, opposite face-center rays, finite N contacts, actual G arcs, selected carrier, profiles and F-first ordering match the accepted sources. |
| C02 | Ball preimages, endpoint cases, complete-profile containment and the close-sphere width ceiling are correct. The paper keeps the diagnostic ball radius separate from cylindrical radius. |
| C03 | Outward cut signs, complementary work, H1 trace scope and native-jump endpoint counting are correct. M01 repairs only the complement's printed notation. |
| C04 / Q01 | The coupled launch, positive quartic receiver gain, full support-distance criterion, inner-gap example, active-port endpoint witness and phasewise first post-F application are retained. M02 repairs the explanatory support sentence. |
| C05 | Exchange common-phase equivariance and the conditional information obstruction are proved correctly. Native singular-prestage and autonomous-history restrictions remain explicit. |
| S02 / S03 | The individual-hull enclosure, fixed-sign convexity, global Lipschitz conversion, both hands, closed static parameter interval, common scaling and strict clearance are correct. |
| S04 | Empty crossing preimages are not treated as a calculated physical aperture flux. C6 remains an unloaded observation with supplied retarded history; M03 makes the scaling application explicit. |
| S05 | Current reciprocal feedback, credit and exchange-only receiving/recovery status are preserved. The missing spatial set, state map and matching work relation are stated without choosing a new geometry or imposing a later research order. |

Two main conclusions survive the consolidation. First, receiver storage can increase while the specified nearest-point or positive-gap cut fields remain zero, on the same initially empty solution. Receiving therefore does not by itself certify the selected travel events. Second, the unchanged carrier and its profile images remain more than \(0.0594w_{\rm host}\) from each G boundary and its individual convex hull over the stated family. Existing host contacts cannot thereby be renamed as direct central-opening crossings. The paper preserves the distinction between that nonintersection result and an undefined physical aperture flux.

The source-to-manuscript crosswalk correctly separates \(R_B\), \(r_\perp\), spatial height, receiver state, static geometry parameter, exchange time, width, characteristics, Jacobians, coupling factors and circle quantities. Both figures use the accepted formulas and label their diagnostic/enclosing roles accurately. Neither figure supplies a new physical aperture, wall, tube width or flow direction.

All eleven required claim items are present. All 92 ledger references to manuscript labels, original source lines, and final equation/theorem numbers and pages agree with the actual source and auxiliary record. Three descriptive Markdown source locators were resolved to real supporting passages; their optional navigation refinements are documented separately. They are not missing evidence or additional required corrections.

## Integrity and document verification

The fresh GPT package/document audit passed **36 checks**. This count concerns delivery and document integrity, not 36 mathematical proofs. It verified:

- The external ZIP checksum, CRCs, all 144 member bytes, and all 143 self-excluded inventory entries.
- All 73 retained input files against the original manuscript-order ZIP, all 72 input-manifest entries, and all 65 registered source identities.
- All 40 recorded source Git blobs, including 32 separately expected blob identities, and both preserved investigation-acceptance archive checksums.
- All 12 build-content hashes, the build-helper hash, all submitted page-image identities, and consistency of the final PDF across its receipts.
- All 96 declared labels, 60 cross-reference uses, nine bibliography keys, and the eleven-item claim ledger.
- The actual 17-page PDF identity, metadata, extractable text on every page, and embedding of all 23 distinct font names. Poppler lists 25 font entries because two figure font names occur in separate objects.

I independently rendered the received PDF at **144 dpi and visually inspected all 17 pages**. Text, equations, tables, figure labels, margins, page transitions and bibliography are legible. I found no clipping, overlapping content, missing glyphs, or further layout defect. The literal comma in equation (3.9) is visible and is covered by M01. The two recorded underfull-paragraph warnings in Appendix A do not produce a visual defect. The fresh inspection receipt identifies every rendered page and binds the observations to the reviewed PDF hash.

Static review of the supplied build helper confirms the intended document-only, cached/untrusted Tectonic workflow with external intermediates and edition-relative content. No submitted build, packaging or scientific script was executed by GPT during this review. This review did not perform a fresh TeX build.

I independently evaluated the two coarser radial display certificates in equation (A.4) with exact rational arithmetic. Both strict margins are positive; the record is included. This is a targeted check of the manuscript's displayed certificates, not a replay of either accepted scientific suite.

The paper accurately describes the earlier verification history: eight central-route algebra groups with limited GPT corroboration, and six six-opening exact groups followed by a replay of those same six. Neither those counts nor this manuscript review are inflated into additional independent proofs.

## Concrete next step

Use `NATIVE_CENTRAL_ROUTE_SIX_OPENING_PAPER_01_CODEX_CORRECTION_ORDER.md`. The `corrections/` directory supplies the three revised source-file copies, a unified diff, and exact before/after identities. The original submitted files remain untouched.

Codex should apply M01–M03, rebuild in the established torment workflow, refresh affected document/ledger/inspection records, inspect every page of the corrected final PDF, and return that PDF with its updated review ZIP, checksum and correction response. The revised artifact must receive its own identity; the present visual receipt cannot certify changed PDF bytes.

**No accepted theorem or scientific result needs to be reinvestigated. Final manuscript acceptance remains pending verification of those three repairs and the revised document.**
