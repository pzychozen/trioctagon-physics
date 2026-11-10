# GPT manuscript review and publication disposition

**Paper:** Spatial Observation and Causal Transport with Storage in the Reciprocal Chiral Exchange Candidate  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Edition:** v0.1, 10 November 2026  
**Review:** project-internal GPT manuscript review  
**Disposition:** the corrected manuscript delivered with this review is accepted for author-authorized repository publication. W01–W05, T01–T07 and D01 remain at their accepted hypotheses and scope. No candidate equation or theorem requires correction. The original submission needed one proof-wording correction and limited scope/status edits; those have been applied and independently rebuilt.

**Publication state:** no repository write, commit, push or remote publication verification was performed in this GPT review. The accompanying Codex order authorizes one final Windows build/verification/publication pass without another approval round for these specified edits. Acceptance of the reviewed bytes is not a claim that they are already on GitHub.

## 1. Review basis and boundaries

The controlling scientific basis is the supplied W/T accepted proof corpus, its GPT dispositions, the exact retained equation sources, D01, and the submitted 25-page manuscript. The historical review/input archives remain unchanged. The new manuscript was checked against this basis; this was not a fresh investigation of the old geometry, capacity, native-credit or cadence results.

The complete manuscript text and TeX, both figures, claim/source ledger, bibliography, build evidence and individual page renders were inspected. The missing end of the visible T proof was read in full, including the D01 counterexample and the positive-measure receiving/return argument. Historical W/T exact-check code and records were treated as their recorded corroboration, not as new GPT executions. No trajectory simulation, parameter scan, altered model or new physical assumption was introduced.

The sole external method reference is retained as supplied methodological context. This review does not assert a new reading of an external theorem or use that reference in place of the manuscript's explicit proofs.

## 2. Scientific assessment

### W01–W05

The geometry argument uses the actual six broken arcs, common width and a full reflected static construction. The enclosing radius is a three-dimensional ball radius, not a cylindrical one. Its finite history ceiling is sufficient rather than optimized. The positive clearance is an accepted input; it is not derived again or turned into a claim of zero physical aperture flux.

The observation estimate is correctly a space-time L2 bound. The Fubini/translation argument gives representative independence almost everywhere; the stronger continuous-record hypothesis and narrow-history point-evaluation counterexample remain distinct. The arbitrary-history witness is not falsely described as two generated RX solutions sharing a state.

The temporal adjoint contains the translated time-window indicator and its negative-time part. Its forward restriction vanishes almost everywhere on the short-window regime, while the longer-window noncausality witness has positive measure. No spatial-delay Jacobian is inserted. The work identity retains the signed prehistory term with a positive coefficient:

\[
\Delta H_{\rm RX}+W^{\rm test}-B_N=W_{\rm pre}.
\]

The formal-force result remains conditional on the solution/regularity assumptions and does not become an existence theorem or a causal loading law. Zero prehistory is sufficient, not necessary, for cancellation.

### T01–T04

The spatial duplication is normalized by the actual total labeled arclength, and the mixer supplies the reciprocal normalization. The C6 factorization, adjoint, Gram matrix and nontrivial kernel are correct. No contraction of the spatial mixer is silently required.

The two characteristic formulas have the correct orientation and startup pieces. The trace estimates are time-space estimates for arbitrary finite-energy profiles, not unsupported instantaneous boundary traces. The direct characteristic norm identity proves integrated transport work; the energy state is strongly continuous, without a corner-matching requirement.

The near/far boundary laws give the required signs and square-root factors. The old receiver is not counted twice, and apparent damping has a modeled transport counterpart. The added receiving stock is nonnegative but not necessarily monotone.

The global mild-solution proof is not circular: incoming traces are known on each delay slab; the local forced RX construction and separate bounded receiving ODE precede the component energy identity; the known incoming-energy bound continues the local RX solution; only then is augmented conservation established. The continuation and finite-horizon dependence arguments retain fixed positive delay bounds and fixed finite parameters. No unproved global H1, backward-flow or uniform zero-delay theorem is asserted.

### T05–T07 and D01

The loaded receiving identity retains C6 as the direct component with coefficient 2κ, the returning contribution, the loading term and the positive startup term. Complete-history compatibility involves the boundary histories as well as the carrier. Independent initial line profiles are not silently interpreted as a generated past. The same-time spatial adjoint is not confused with W's temporal adjoint, and a nonnegative initial transit stock is not equated to the signed prehistory pairing.

The native map, its coefficients, zero convention and F-first ordering are preserved. Only native storage jumps, and the post-jump endpoint convention is retained. The unchanged accounting formula does not mean unchanged numerical increments on different coupled trajectories.

D01 is correctly integrated: empty added states are sufficient, not necessary, for inactivity at zero coupling. The nonzero receiving preparation in ker C* supplies the stated stationary counterexample. Exact recovery of the original RX subsystem at κ=0 holds for arbitrary added preparation.

The activity proof uses its explicitly declared constant carrier preload, zero native preparation, initially empty added states and temporary H1 regularity. The positive-measure sublevel-set argument handles endpoint/elbow minima. The return constant and early receiving bound remain those of the accepted proof. A nonzero incoming b is not claimed to imply nonzero projected feedback, positive net carrier work, native credit, recovery or a capacity fraction. This witness is carrier-funded; native x stays zero.

## 3. Required edits, now incorporated

The exact replacements are in `CORRECTIONS.json`; `CORRECTIONS.diff` shows the complete source diff. There are 16 exact replacements across seven files. All 79 display-math blocks, candidate equations and theorem statements remain unchanged.

| Group | Location | Change and reason |
|---|---|---|
| **M01 — unit directions** | Original p.5, Proposition 2.1 proof; `sections/02_setting.tex` | The 1/2 dot product belongs to adjacent unit directions e_i,e_(i+1), including e_5,e_0. It does not belong to the scaled horizontal vertices themselves. Their corresponding dot products are a_g r_g/2 and D²a_g r_g/2. The already displayed edge-length formula is correct and unchanged. |
| **M02 — inherited versus declared scope** | Abstract; Appendix A | “Same finite-window baseline increment” becomes “retains its finite-window baseline accounting formula,” avoiding equality of numerical increments on modified trajectories. The new dimensional assignment is called compatible and declared, rather than merely inherited. All formulas are unchanged. |
| **M03 — current release state and open-question wording** | Cover, PDF metadata, preparation note, conclusion, Appendix C, README, BUILD and build-helper status | Record internal review and the author's existing authorization accurately; do not claim external peer review, formal proof or an already completed push. Preserve the physical embedding question as open, without automatically commissioning another extension. Update active build-status metadata and distinguish original build08 evidence from any corrected production build. |

These are manuscript/documentary changes, not a withdrawal or strengthening of W/T claims. The new closing paragraph does not settle the physical route question or claim that the unchanged native model produces the declared added states.

## 4. Artifact and source verification

The independent incoming-submission audit passed 609 file/document checks. Their scope is integrity and manuscript mapping, not 609 mathematical proofs:

- All 194 ZIP members were reopened; the 193 self-excluding inventory entries matched.
- All 84 original manuscript-packet members were preserved, with all 83 packet-manifest entries and 74 registered source identities matching.
- All 99 manuscript claim-ledger locations and 107 retained source locators matched their recorded text/hashes and labels.
- All 118 manuscript labels were unique and resolved; all 12 cited bibliography keys resolved.
- The supplied standalone PDF matched its archived edition copy. All PDF font resources examined were embedded, and pages were searchable without replacement glyphs.

A separate checksum file for this latest review ZIP was not attached. This review computes and records the archive SHA-256 and checks its internal manifests; it does not claim comparison with the inaccessible Windows checksum pathname.

The corrected edition was compiled independently in this review environment using three no-shell-escape XeLaTeX passes. This is a Linux reviewer build, not a second Windows/Tectonic execution. The final build has 25 pages, no compiler warnings, all fonts embedded, and all 118 label numbers and page references equal to the submitted version. All 25 original and all 25 corrected pages were visually inspected. Figures 1 and 2 remain unchanged and correctly distinguish abstract state connections and schematic support intervals from physical paths or simulated waveforms.

The historical four W and five T algebra groups were not rerun. Their code/logs and the accepted proofs are preserved. The supplied Tectonic build helper was not represented as having run in this Linux review; only its publication-status string was updated.

## 5. Exact identities

| Artifact | Bytes / pages | SHA-256 |
|---|---|---|
| Submitted review ZIP | 194 members | `a4963edc6cad84a1824231850e13b6c0a33a64db5a41a5994b485b08042663a3` |
| Submitted PDF | 237,725 bytes; 25 pages | `4b14dd8b291c80967f5cc570c4dab58f567043514334429af13c2f80d83564f1` |
| Corrected reviewer PDF | 231,768 bytes; 25 pages | `79654f41c90a0935d2287c8c1134d6e1927f155c725bc85450c0d5da6cab4a86` |

The source-file identities are in `verification/PATCH_AUDIT.json` and `GPT_ACCEPTANCE.json`; visual inspection is bound to the corrected digest in `verification/VISUAL_INSPECTION.json`. Compiler logs, aux/toc, independent document checks and an updated reviewer ledger are supplied. A different final compiler may produce different PDF bytes; the actual Windows publication output must have its own fresh identity, reference and page-inspection records.

## 6. Publication disposition and next boundary

Proceed under the author's already given authorization with the attached fix/build/publish order. No further approval round is required for these exact edits, ordinary production metadata/locator refresh, or a faithful rebuild. Stop only for a substantive scientific discrepancy, an unresolved build/document failure or an actual repository safety conflict.

Publish this bounded mathematical result without implying physical validation, native derivation of the added receiver/transport states, a completed curved circuit, a physical clock, native recovery from the displayed preload witness, or transfer of earlier capacity theorems to changed trajectories.

After publication, close this manuscript task. The agreed research emphasis is examination of the behavior and implications of existing native Tri-Octagon equations and geometry. The open physical embedding question remains on the list, but it is not automatically the next commission.
