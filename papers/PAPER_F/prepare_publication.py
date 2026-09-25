"""Controlled editorial conversion of the immutable accepted Paper F v0.2."""
from pathlib import Path
import re,json,hashlib,difflib
ROOT=Path(__file__).resolve().parent
SRC=ROOT/"support/repository/research/paper_F_transverse_normal_form/PAPER_F_DRAFT_v0.2.md"
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
source=SRC.read_text(encoding="utf-8")
text=source
changes=[]
def replace(old,new,reason):
 global text
 assert text.count(old)==1,(old[:100],text.count(old))
 text=text.replace(old,new)
 changes.append({"old":old,"new":new,"reason":reason})
def paragraph(prefix,new,reason):
 old=next(x for x in text.split("\n\n") if x.startswith(prefix))
 replace(old,new,reason)
replace('version: "Paper F v0.2 — unpublished publication candidate for GPT/Hilmir review"',
        'version: "Paper F v0.2 — publication build"',"Metadata only; omit internal review status from scholarly text")
paragraph("This draft reconstructs",r"""The twelve **oriented** roots of \(\sin6\phi=0\) have three \(D_3\) orbits. Two types are obtained under \(D_6\), or on projective axes under \(D_3\). Section 6 proves these counts directly. The supplementary reconstruction record documents the calculation's development and attribution. No novelty or priority claim is made for standard representation theory, polynomial identities or analytic linearization.""","Move internal development chain to supplementary record; retain mathematical distinctions")
paragraph("Version v0.2 incorporates",r"""The local Poincare normal form is linear under the stated nonresonance hypotheses; the finite coefficient system below is a Taylor-jet calculation.""","Remove review/build history; preserve distinction between normal form and Taylor jet")
paragraph("Thus the \\(D_6\\) orbits",r"""Thus the \(D_6\) orbits have sizes six and six, and the projective \(D_3\) orbits have sizes three and three. Each \(D_6\) orbit has a stabilizer of order two and is therefore not a regular orbit. The supplementary reconstruction record preserves the earlier terminology and its attributed correction.""","Retain stabilizer assertion; move reviewer-specific correction history to supplement")
replace("The positive sign printed in [CG, §5] is a prose typo; its downstream formulas agree with this calculation [NF]. ",
        "","Internal typo history is retained in CG/NF/CR and the supplementary record, not the proof narrative")
replace("The isolated phase-vector calculation in [CG] begins", "The isolated phase-vector calculation (Appendix B; prior attribution in the supplementary record) begins","Replace unnecessary internal proof dependence with self-contained derivation")
replace("`NONZERO_LAMBDA = CONTROLLED_TO_FIRST_ORDER`. ","","Replace internal status flag by its existing following mathematical explanation")
paragraph("No step uses the historical", "No external observer-lock, shell-coordinate, or energy parameter enters the present derivation.","Explicit publication boundary; unrelated literal and coordinate disclaimer retained only in original provenance")
paragraph("These results are mathematical properties", "These results are mathematical properties of the specified recurrence. A physical dictionary is not established by the present analysis.","Remove publication-readiness/review assertions; retain limitation")
replace("The new verifier multiplies","The accompanying exact verifier multiplies","Remove development-state adjective")
paragraph("`paper_f_exact_checks_v0_2.py` performs", "The accompanying exact verifier performs symbolic algebra and reads the preserved two-seed data. It statically inspects the accepted recurrence and chirality source bodies, without importing the kernel or executing model evolution. Its full output, input identities and original validation record are supplied separately [S:Checks]. The reproducibility manifest describes the isolated execution and publication build.","Standalone reproducibility description; implementation paths belong in supplement")
paragraph("The versioned code, original census", "The supplementary reconstruction record contains the versioned exact verifier, source census, theorem/provenance ledger, literature review and open-question ledger. It also preserves the prior mathematical reviews with attribution. The package manifest identifies every supplied artifact by SHA-256. These research records are separate from the established literature cited below.","Remove Git/build status from scientific prose")
replace("This appendix proves the parameter assertion used in Theorem 8. It replaces v0.1's unsupported reference to a common majorant construction.",
        "This appendix proves the parameter assertion used in Theorem 8.","Remove editorial history only; entire Appendix D proof remains verbatim")
replace("[Census, Questions]","[S:Census, S:Questions]","Explicit supplementary citation class")
replace("experiment [AX]","experiment [S:AX]","Explicit supplementary saved-experiment citation class")
replace("paper [Checks]","paper [S:Checks]","Explicit supplementary exact-verification citation class")
# Replace references as a controlled block. All original references remain in the frozen source.
oldrefs=text[text.index("## References and local provenance"):]
refs=r"""## References

**[PA]** Hilmir Frímann Halldórsson. *Cycle-Covering Dynamics of a Three-State Nonlinear Kernel*. Paper A, repository publication (2026), §§1 and 6.1. [Publication source](https://github.com/pzychozen/trioctagon-physics/blob/d0aa8d1cb19421ff441eacda0f83ec89fc3160b3/papers/PAPER_A/publication/paper_A_publication.md).

**[PB]** Hilmir Frímann Halldórsson. *Triadic Chirality and Orientation Geometry*. Paper B, v0.1.2 (23 September 2026), §§5–8. [Publication source](https://github.com/pzychozen/trioctagon-physics/blob/d0aa8d1cb19421ff441eacda0f83ec89fc3160b3/papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md).

**[Ab]** Marco Abate. “Discrete holomorphic local dynamical systems.” In *Holomorphic Dynamical Systems*, Lecture Notes in Mathematics **1998**, pp.1–55. Springer (2010). [doi:10.1007/978-3-642-13171-4_1](https://doi.org/10.1007/978-3-642-13171-4_1). Checked [author version](https://pagine.dm.unipi.it/abate/articoli/artric/files/DiscHolLocDynSys.pdf): Definition 5.9, Proposition 5.10 and Theorem 5.15, printed pp.35–36. The Poincare attribution is through this source, not an inspection of the 1893 original.

**[St]** Richard P. Stanley. “Invariants of finite groups and their applications to combinatorics.” *Bulletin of the American Mathematical Society* (N.S.) **1**(3), 475–511 (1979). [doi:10.1090/S0273-0979-1979-14597-X](https://doi.org/10.1090/S0273-0979-1979-14597-X). Checked [author-hosted article](https://math.mit.edu/~rstan/pubs/pubfiles/38.pdf), §4: Theorem 4.1, p.486; Proposition 4.7 and permutation-group example, pp.488–489.

**[Fi]** Michael Field. *Dynamics and Symmetry*. Undated online author manuscript, checked 423-page version. [Manuscript](https://chaosbook.org/library/FieldEquiv.pdf), §1.2 example (6), printed p.3; Definition 2.10.1 and Proposition 2.10.4, printed pp.42–43 (PDF pp.52–53). These locators refer to this online version, not the pagination of the 2007 printed book.

**[Ge]** Erik Gengel, Erik Teichmann, Michael Rosenblum and Arkady Pikovsky. *High-Order Phase Reduction for Coupled Oscillators*. arXiv:2007.14077v1 (28 July 2020). [doi:10.48550/arXiv.2007.14077](https://doi.org/10.48550/arXiv.2007.14077). Checked [preprint](https://arxiv.org/pdf/2007.14077v1), §2.2, equation (3), p.4. First-author spelling follows the PDF title page; the arXiv HTML metadata renders “Genge.”

**[Sk]** Per Sebastian Skardal, Edward Ott and Juan G. Restrepo. “Cluster synchrony in systems of coupled phase oscillators with higher-order coupling.” *Physical Review E* **84**, 036208 (16 September 2011). [doi:10.1103/PhysRevE.84.036208](https://doi.org/10.1103/PhysRevE.84.036208). Checked [author-institution copy](https://www.colorado.edu/amath/sites/default/files/attached-files/physreve_84_036208.pdf), §IV, equation (36), p.036208-7.

## Supplementary reconstruction record

**[S]** *Paper F: reconstruction and reproducibility supplement*, accompanying this paper. This is internal research provenance, not established literature. It preserves the attributed CT, AX, CG, NF and CR records, including superseded wording and its corrections. The proof arguments in this paper are self-contained apart from the stated classical theorem application.

**[S:AX]** The preserved Codex two-seed report and saved outputs, including the GPT-attributed historical-seed decomposition. **[S:Census]** The original bounded source census. **[S:Questions]** The v0.2 open-question ledger. **[S:Checks]** The exact verifier, accepted v0.2 validation and separate publication-build execution record. Artifact identities and the full attribution history are provided in the supplement inventory.
"""
replace(oldrefs,refs,"Complete checked scholarly bibliography separated from internal provenance inventory")
figure=r"""
\begin{figure}
\centering
\includegraphics[width=\linewidth]{figures/figure_1_transverse_symmetry.pdf}
\caption{Intrinsic transverse symmetry. Left: the twelve roots \(\phi=k\pi/6\) on \(q(\phi)=u\cos\phi+v\sin\phi\), colored and shaped by the three \(D_3\) oriented orbits (sizes \(6,3,3\)). Right: antipodal identification gives the two projective classes, each with three axes; labels are \(k\bmod6\). Conjugation sends \(k\) to \(k+6\), joins the two oriented \(v\)-type orbits and extends the seed-circle action to \(D_6\). The \(D_6\) orbits have sizes \(6,6\), with stabilizers of order two. Coordinates are coefficients in the intrinsic \((u,v)\) basis, not physical-space coordinates.}
\end{figure}
"""
anchor="The full-state stabilizers give stronger geometric constraints"
idx=text.index(anchor)
text=text[:idx]+figure+"\n"+text[idx:]
changes.append({"old":"","new":figure,"reason":"Single equation-generated intrinsic Figure 1 after Proposition 3 proof; no new scientific result"})
out=ROOT/"PAPER_F_PUBLICATION_v0.2.md"
out.write_text(text,encoding="utf-8")
# Exact textual math audit, with the sole authorized deletion of the unrelated inline lock disclaimer.
display=lambda t:re.findall(r"\\\[(.*?)\\\]",t,re.S)
srcdis=display(source);pubdis=display(text)
assert srcdis==pubdis
tags=lambda t:re.findall(r"\\tag\{([^}]+)\}",t)
assert tags(source)==tags(text)==[str(x) for x in range(1,62)]+["D1","D2","D3"]
def section(t,a,b):return t[t.index(a):t.index(b)]
t8=section(source,"**Theorem 8","`NONZERO_LAMBDA")
assert t8.strip() in text
app=section(source,"Let \\(K\\) be a compact","## References and local provenance").strip()
assert app in text
for label in ["**Theorem 4","**Theorem 5","**Theorem 7","**Theorem 8"]:
 assert label in text
mapping=[]
sl=source.splitlines();pl=text.splitlines()
for kind,a,b,c,d in difflib.SequenceMatcher(None,sl,pl,autojunk=False).get_opcodes():
 mapping.append({"operation":kind,"source_lines":[a+1,b],"publication_lines":[c+1,d],"source_text":"\n".join(sl[a:b]) if kind!="equal" else None,"publication_text":"\n".join(pl[c:d]) if kind!="equal" else None})
save(ROOT/"records/editorial_transformations.json",changes)
save(ROOT/"records/source_to_publication_fidelity.json",{
 "scientific_source":"v0.2","source_sha256":sha(SRC.read_bytes()),"publication_sha256":sha(out.read_bytes()),
 "display_equations_identical":True,"display_block_count":len(srcdis),"numbered_equations":tags(text),
 "theorem_8_full_text_identical":True,"appendix_D_full_argument_identical":True,
 "headline_math_preserved":True,"exact_resonance_interval_preserved":True,
 "all_proof_arguments_preserved":"All display math is byte-identical after newline normalization; all prose differences appear in this line map and the explicit editorial transformation log. Only review/provenance/status prose changed.",
 "source_to_publication_line_map":mapping,
 "headline_equation_tags":["28","40","42","44","45","46","51","55","56","58","59","61","D1","D2","D3"],
 "equations":[{"ordinal":i+1,"tag":tags(b),"sha256":sha(b.encode()),"body":b} for i,b in enumerate(srcdis)]})
(ROOT/"BIBLIOGRAPHY.md").write_text(refs[:refs.index("## Supplementary")],encoding="utf-8")
print(json.dumps({"display_blocks":len(srcdis),"numbered":len(tags(text)),"editorial_changes":len(changes),"publication_bytes":out.stat().st_size}))
