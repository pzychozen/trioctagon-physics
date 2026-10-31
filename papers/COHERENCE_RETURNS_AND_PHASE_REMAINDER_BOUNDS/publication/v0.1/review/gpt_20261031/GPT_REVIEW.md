# NCM-PAPER-01 v0.1 — GPT manuscript review

**Date:** 31 October 2026  
**Manuscript:** *Coherence Returns and Phase-Remainder Bounds in the Native Tri-Octagon Map*  
**Human author:** Hilmir Frímann Halldórsson  
**Disposition:** **Scientific content accepted for author review. Submitted 19-page PDF accepted as the readable review artifact. One source-formatting correction identified before treating the TeX deliverable as release-ready. No further mathematical investigation or numerical search is required for this paper. Publication is not authorized by this review.**

## 1. Material and scope

The received archive is `NCM_PAPER_01_v0.1_REVIEW.zip`:

- SHA-256: `e66c15d818e7199136ad18b63a7116cd3291ed971658b7fe21c6708f063b8af5`.
- 345 file entries; 344 are listed in OUTPUT_HASHES.json, which excludes itself.
- Original manuscript PDF SHA-256: `44aa1a14fabbf0b1230fcb724d18de1e34b833f7ade04735b756e674f8f301f7`.
- Original TeX SHA-256: `aee31123b1385197baeb77551b97ef8e662d01d18ce8315a55b8de8e5b142099`.

I read the complete mathematical manuscript, independent sector review, claim/source matrix, evidence index, placement assessment, correction log, QA documents, and the retained-data extracts. I rendered the submitted PDF locally and visually inspected all 19 pages, including the equations and all seven tables. The supplied PDF and package were not modified.

This is an internal mathematical and editorial review, not an external peer review, an assessment of priority against external literature, or certification of the original Windows execution. The task made zero native-map evaluations, zero orbit searches, zero observer/pose evolutions and zero executions of prior scientific solvers or long certificates. Only current drafting algebra, retained-data reconciliation and document compilation/inspection were performed.

## 2. Mathematical disposition

### Theorem 1 and Corollary 1: accepted

For a nonzero state, equality of raw rank-one coherences implies a unique unit common-phase multiplier. The manuscript correctly distinguishes the algebraic statement from the regularity needed to propagate that multiplier through the actual native map.

The proof explicitly carries the known regular block into later common-phase copies, rather than assuming an arbitrary regular state stays regular. It correctly uses harmonic sine invariance under argument wraps and does not repair Arg0 at zero. The minimal-period proof divides a proposed full return into blocks and a remainder; it does not infer a finite phase order from numerical decimals.

The normalized-projector example is correctly labeled as a separate equal-k control. It shows why raw norm information cannot be discarded and why a scale multiplier cannot simply be repeated in the nonlinear map.

### Lemma 2 and Proposition 3: accepted

The proof of F(B3) inside the interior of B_(3/2) uses positive self coefficients, component-modulus preservation by synchronization, and the maximum of a cubic envelope. The smaller invariant domains follow from the increasing envelope.

The maximum over a finite unit-multiplier returning block then gives the component bound sqrt(1001/1000). The argument does not require regularity and does not claim a lower amplitude bound, global return classification, or a spatial enclosing-sphere statement.

The manuscript correctly distinguishes the upper-envelope derivative minimum 11753/30000 from the individual-polynomial derivative minimum 11747/30000. All listed rational constants were checked.

### Theorem 4: closed 60-degree strengthening accepted

The independent proof supplies the required steps:

1. Regularity and a returning block make all component phases available; the amplitude bound makes all prestage mixing coefficients strictly positive.
2. Positive mixing strictly narrows any positive ordinary phase width at most pi/3.
3. The actual simultaneous phase kick can be written with weights lambda*sin(3d)/d, continuously extended at zero. On the closed interval |d| <= pi/3, the weights lie in [0,1/100]; the self-weight is at least 49/50.
4. Synchronization is therefore nonexpanding in that lifted interval. Its endpoint weights may be zero; strict contraction comes from the prestage, not an incorrect strict-positivity claim about all synchronization weights.
5. The shortest circular arc width is unchanged by common rephasing. A finite return cannot restore positive width after strict reduction.
6. In the remaining aligned case, the inherited real-amplitude potential decreases by at least (2187/2500)||grad W||^2 unless the amplitude state is fixed. The invariant convex cube justifies the Hessian bound along the complete update segment.
7. Fixedness at a cyclic starting stage implies fixedness of the original returning state without invoking invertibility or backward uniqueness.

The theorem is correctly restricted to the stated fixed parameters, B3 and a nonzero regular finite unit-multiplier return. It is not a global convergence theorem, an optimal-sector result, or a theorem about the spatial cone-pair midpoint angle. No correction to the mathematical statement or its proof is required.

### Proposition 5: accepted

The Hermitian prestage perturbation bounds and the phase-chord inequality give the one-step coefficient 53717/500000. At a cyclic stage of maximal Euclidean norm, the three displacement bounds telescope to

    |mu - 1| <= 161151/500000 = 0.322302.

The unit-circle chord relation gives

    |Arg(mu)| <= 2 asin(161151/1000000)
               = approximately 18.547421362807274469 degrees.

The decimal is formatting of the exact expression, not an interval certificate. The result excludes mu=+i and mu=-i for the specified three-return, and therefore the p=3/order-four mechanism in that domain. It does not exclude every twelve-cycle or every other dispersed-phase three-stage return.

### Readouts and contextual comparisons: accepted within their declared scopes

The existing cubic K(z)=z0*conjugate(z1)*z2 has unit-phase covariance K(mu*z)=mu*K(z). The conditional scalar sequence is correctly separated from autonomous (H,j) closure, a full EMA-memory period, energy transport and body pose. The draft does not present the excluded quarter-phase specialization as a computed native trajectory.

The earlier D1, coherent-relaxation and M3 results retain their distinct parameter sets and hypotheses. The M3 limiting cycle is not described as a finite-time exact landing of its entrance. SRG is a separate transfer/initializer, not a renamed native update. Appendix B correctly retains the contraction factor exp(-0.269)*(0.382)^2 and the fixed-transport versus prescribed-cone distinction.

The author's golden-ratio wording remains illustrative rather than an assumed controller. The cone sequence remains the motivation, not a recurrence output. Existing native and Z-related evolution is not erased by the failed specific motion correspondence.

## 3. Evidence and provenance checks performed here

- Verified all **344/344** manifest-listed files by byte count and SHA-256, and checked complete manifest coverage of the 345 extracted files.
- Verified that the separately attached START_HERE is identical to the archived copy.
- Verified the included DUAL-02 and DUAL-03 evidence ZIPs byte-for-byte against the earlier uploaded original archives.
- Compared all 28 extracted source-packet files with the earlier uploaded NCM-PAPER-01 packet.
- Read all **60 retained attempt records as JSON only**. Their digests, classifications, stop reasons and extracted metrics match the manuscript evidence extracts. The ledger matches the frozen summary.
- Reconciled **42 numerical lower-period-one outcomes, 17 line-search failures, one iteration limit**, and seven groups. The group extract equals the original retained JSON. No native residual was recomputed in this task.
- Checked historical discovery call accounting (8,211) from the stored attempts without executing the discovery program.
- Replayed only the current drafting `proof_review/check_symbolic.py`, inspected beforehand. **All 29 checks passed; every reported check result and the displayed phase-bound value match the submitted output.** This is exact supporting algebra, not a finite substitute for the written universal proofs.
- Checked the 30 generated TeX equation expressions against the shared-content snapshot and confirmed seven tables.
- Verified **36 internal PDF citations** target the bibliography and **12 relative evidence links** target an existing evidence-index file.
- Before/after records for the seven inspected scientific sources, standalone order and source packet are internally consistent. The live Windows files were not accessible to this review; no independent Windows-preservation or producer-execution attestation is claimed.

The reviewer environment was Linux, Python 3.13.5 and SymPy 1.14.0. Review-created records and scripts are separate from the received package. The 110 document/data predicates in REVIEW_AUDIT.json are bookkeeping checks, not 110 mathematical theorems.

## 4. Submitted PDF and document quality

The **original 19-page PDF is readable and complete**. All pages were rendered with PyMuPDF and inspected, including the full proof pages, outcome/group tables, rational-constant table, appendix comparison and bibliography. I found no clipped equation, missing visible row, overlapping text or broken mathematical symbol that requires a correction to this PDF.

The mathematics is rendered as image assets, while body text is selectable. That limitation, the lack of PDF tagging and the direct ReportLab/mathtext build are disclosed. A TeX-produced PDF was not necessary to complete scientific review of this supplied artifact. No font files are included in the review deliverables.

## 5. One TeX-source issue discovered by actual compilation

A local XeLaTeX compiler was available in the review sandbox. I compiled an isolated copy of the original main.tex twice, with shell escape disabled and no package/font/network acquisition. Compilation succeeds, but the generated source does not end the caption paragraph before beginning each tabularx. As a result, several tables begin alongside their caption and extend off the page. For example, the constants table has a 286.5-point overfull box, with visibly missing right-hand columns in the compiled view.

This defect **does not affect the received 19-page ReportLab PDF**. Codex correctly disclosed that its TeX source had not been compiled. The review adds a subsequent compiler result; it does not contradict that historical disclosure.

### Bounded repair

In manuscript/build_manuscript.py, append a paragraph terminator to the table-caption TeX string:

    ... + r'}\par'

The generated main.tex then receives the corresponding seven `\par` insertions immediately after the seven captions. The repair changes no theorem, equation, table value, citation or content snapshot. Preserve the original TeX CRLF line endings and the builder's LF convention.

A proposed two-file correction, explanatory unified diff and before/after hashes are included under `source_fix/` in the review bundle. They are **reviewer candidates only**, not applied to the received package or the Windows checkout. No Git command is needed or authorized by this note.

The corrected source was compiled twice in isolation. The large table-caption overflow disappears and the formerly off-page tables are readable. Three smaller overfull warnings remain in a narrow table cell and long source filenames, and the title-page pagination differs. These are layout polish to address if a TeX-produced PDF is later selected as the release artifact. The sandbox TeX output has 20 pages and is **not** being supplied as a replacement for the reviewed 19-page PDF.

For the current manuscript, the original PDF can remain byte-identical. Correct the source/generator in a successor document package, record the correction and later compiler check, and refresh affected output manifests. No new science is needed. Do not silently replace the accepted PDF or rewrite the original evidence records.

## 6. Recommended disposition and stopping point

- **Scientific content:** ACCEPTED for author review.
- **Closed 60-degree proof:** ACCEPTED under its explicit hypotheses.
- **Submitted PDF:** ACCEPTED as the current review artifact.
- **Editable-source release readiness:** one identified table-caption fix; additional cosmetic TeX polish only if switching the canonical PDF build.
- **Further scientific work required for this paper:** none.
- **Author approval / publication:** not granted by this internal review; keep separate.
- **External novelty / priority:** unassessed, as explicitly stated in the manuscript.

This is proportionate as a focused mathematical research note with its evidence package. Its contribution is the precise return criterion and fixed-parameter necessary conditions, including the strengthened sector exclusion and the faithfully reported finite search. It need not establish native cone motion to make that contribution. No new research assignment or additional geometric explanation from the author is required to finish this manuscript.
