"""Claim/source mapping, BibTeX metadata, and portable reading/build notes."""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
claims=[
('C01','Unchanged target and distinction from Paper I tower','sec:scope','HIERARCHY §1; CUBIC §11','Definition of function-field extension; Paper I preserved','Scope/definition','No genus transfer between different towers'),
('C02','Reversal, degree, reciprocal divisors and cancellations','prop:reciprocal','HIERARCHY §§3.1,3.3','Direct reversal proof; hierarchy n=2,3,4 identity checks','Theorem and exact identities','Root resultant formula assumes a0 nonzero'),
('C03','Locks, parity, continuation sign and constants','prop:lock','HIERARCHY §§3.2-3.3','Local Taylor proof; hierarchy lock and cancellation checks','Theorem','Raw holes distinguished from reduced continuation'),
('C04','Wronskian pairing, odd local degree, Cayley normal form','eq:odd','HIERARCHY §§2,3.4; MSW §2.1 Lemma 2','Invariant-field proof; hierarchy Wronskian checks','Standard structure and family derivation','Commuting automorphism is not deck transformation'),
('C05','Real unit-circle behavior','eq:W_reversal','HIERARCHY §10','Conjugation plus reciprocity; no surviving zero/pole on unit circle','Exact argument','Complex circle is not real x domain'),
('C06','Nonempty generic simple-branch locus in every degree','thm:generic','HIERARCHY §9','Odd pole-pair insertion, implicit-function theorem, Riemann-Hurwitz count','Theorem/prose proof','Not machine-formalized; not inferred from numerics'),
('C07','Generic monodromy Sn, trivial deck and irreducible residual','eq:main','HIERARCHY §9','Connected transposition graph; centralizer and sheet stabilizer','Theorem/prose proof','Generic only; fixed unchanged target'),
('C08','Generic Galois closure genus formula','eq:RH_general','HIERARCHY §9','Galois Riemann-Hurwitz with 2n-2 order-two inertia groups','Theorem','Does not apply unchanged to x-lift'),
('C09','Quadratic rational partner and extended V4','eq:quadratic_partner','HIERARCHY §7; Paper I','Quadratic extension argument; explicit partner','Exact proof','Only C2 fixes F2 itself'),
('C10','Cubic original-coordinate residual quadratic','eq:original_residual','HIERARCHY §4.2','hierarchy: cubic difference factorization','Exact symbolic identity','Degree-three domain; projective fibers'),
('C11','Cubic cancellation and lower degree','eq:degree3','HIERARCHY §§4.1,4.3','Homogeneous gcd argument; cubic resultant check','Exact classification','Constants excluded from cover statements'),
('C12','Cubic discriminant correspondence is splitting field','eq:E','HIERARCHY §§4.3,5.3; CUBIC §2','Remaining root from Vieta; residual discriminant checks','Exact algebra and field argument','Smooth normalization required'),
('C13','Cubic critical/branch quartics and complete strata','tab:cubic_strata','HIERARCHY §§5.1-5.2','Discriminants; degree-three fiber count; Riemann-Hurwitz','Exact classification','Degree-three condition must be retained'),
('C14','S3 action by translations and inversions','prop:torsion_action','CUBIC §4','Inertia/fixed-point argument; root incidence checks','Theorem','Origin chosen over complex numbers'),
('C15','Birational Weierstrass model and invariants','eq:weierstrass_map','CUBIC §3','cubic: quartic to short Weierstrass; inverse; invariant checks','Exact identities','Affine excluded points filled projectively'),
('C16','Explicit actual 3-torsion translation point','eq:P','CUBIC §4','cubic: on-curve, doubling, division polynomial, incidence identification','Exact identities and action proof','Generator sign chooses cycle orientation'),
('C17','Reciprocity selects commuting nonzero 2-torsion','eq:Q','CUBIC §5','Free simultaneous lift; 2-torsion coordinate and commuting action checks','Exact argument','Other lift differs; reciprocity does not fix target'),
('C18','Explicit degree-three isogeny and kernel','eq:isogeny','CUBIC §6','Vandermonde fixed field; cubic isogeny substitution and invariance checks','Exact identities and field proof','E and E-prime are different curves'),
('C19','Normalized t, modular j-functions and h duality','eq:jh','CUBIC §§3,8; Elkies §4 Eq80','cubic: normalized c4/Delta, j substitutions and duality','Exact identity; standard modular convention','Source/quotient orientation retained'),
('C20','Complete coarse X0(3) and X0(6) classification','prop:moduli','CUBIC §8','Kummer converse; fixed-pair normalization; oriented-j gcd check','Theorem/prose plus symbolic proof','Independent source/target equivalence; generic coarse data'),
('C21','Coefficient map dominates t-line and loses embedding data','eq:section','CUBIC §10','Explicit rational section; direct pqrs substitution','Exact identity','Real embeddings not classified by complex t'),
('C22','Critical-value cross-ratio belongs to E-prime','eq:crossratio','CUBIC §7','Kummer branch field; Legendre and j checks','Exact argument','Ordering is extra data; algebraic square-root choices'),
('C23','Cyclic loci, rational partners and extended groups','eq:cyclic_loci','HIERARCHY §§4.3,5.4; CUBIC §9','Residual square factor; cyclic conjugacy; group relations','Exact classification','Not all partners real; degree-three condition'),
('C24','Nodal S3 boundary versus split cyclic specialization','eq:degenerate_square','CUBIC §9','Factored quartics; normalization/ramification arguments','Exact identities and geometric interpretation','Specializing closure differs from closure of specialization'),
('C25','Four modular cusps and ramification of h/j','eq:h_ramification','CUBIC §§8.3,9','Derivative, discriminant orders, nonzero c4 after rescaling','Exact parameter facts; standard multiplicative interpretation','No exhaustive coefficient-intersection path census'),
('C26','Quartic formulas, generic S4 and genus 13','eq:quartic_genus','HIERARCHY §6','hierarchy: quartic resultant/Wronskian, exact witness; general theorem','Theorem and exact identities','No exhaustive exceptional census'),
('C27','Selected quartic decomposable/C4/V4 examples','sec:quartic','HIERARCHY §6.3','hierarchy: explicit exceptional identities','Exact examples','Assume uncanceled degree four'),
('C28','Squaring lift ramification and real x restriction','sec:x_lift','HIERARCHY §10; CUBIC §10','Local degree multiplication and branch count','Exact argument','No monodromy/genus claim for lifted closure'),
('C29','Real genus-one torsor caveat','eq:real_torsor','CUBIC §10','Negative quartic for t=2 including infinity','Exact counterexample','Complex birational model need not be real'),
('C30','Exact finite patch S3 equivalence','eq:finite_bridge','CUBIC §12; PATCH §§2-3.1','cubic: actual matrices, patch action, finite bijection checks','Exact finite incidence equivalence','Chosen labels; distinguish left/right regular actions'),
('C31','Fixed shell and scaffold candidate audit','eq:scaffold','PATCH §2; SCAFFOLD lines172-266,339-342; SCAFFOLD_PROOF §6','bridge: geometric ratio checks; source-definition review','Bounded source comparison','Variable scaffold separate from fixed shell; no fitted scalar'),
('C32','Registration and readout candidate audit','eq:registration','PATCH §§3.3-3.4,7; Z_READOUT lines91-151,226-260','Source-definition review; bridge cubic-readout counterexample','Bounded source comparison','No inferred attachment or elliptic structure'),
('C33','Boundary, transfer and operating-profile audit','eq:lens','BOUNDARY lines1-105; SRG lines21-94,122 onward; OPERATING','bridge: lens derivative/endpoints; source-definition review','Bounded source comparison','No production imports or tests'),
('C34','Finite bridge only; continuous data underdetermined','sec:bridge_result','This paper final bounded audit using C30-C33','All smooth t have same finite S3-set; no independent branch/isogeny definition','Source-limited conclusion','Not a universal impossibility theorem'),
('C35','Symbolic and numerical verification status','app:evidence','Copied hierarchy/cubic scripts and JSON; bridge_results.json','51+73+10 exact checks; numerical records','Reproducible computation','Numerics not interval certificates; topology not formalized'),
]
auxpath=ROOT/'records/main.aux'
nums={}
if auxpath.exists():
    nums={k:(n,p) for k,n,p in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',auxpath.read_text(encoding='utf-8'))}
with (ROOT/'provenance/claim_ledger.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['id','claim','manuscript_label','number','printed_page','source','proof_or_check','evidence_class','limitation','novelty_status'])
    for row in claims:
        num,page=nums.get(row[2],('',''));w.writerow([*row[:3],num,page,*row[3:],'No priority claim'])
bridge=[
('B01','PATCH','51-150','Patch geometry, shape ratios, rigid finite action','Finite S3 correspondence; fixed shape scalars'),
('B02','PATCH','161-233;386-393','Conditional registration, clock and open attachment','No intrinsic continuous branch datum'),
('B03','SCAFFOLD','172-266;339-342','s, gap, radii, area, roles, regularity and welded member','One separate shape ratio; no selected isogeny'),
('B04','SCAFFOLD_PROOF','section6','Independent alternating-side geometric derivation','Source provenance for scaffold; no modular dictionary'),
('B05','BOUNDARY','1-7;25-37;55-105','Lens angle, area fraction, gain, response vector','Independently defined response, no branch-cover identification'),
('B06','SRG','21-29;50-94;122 onward','Fixed tensor transfer, eigenmode, transfer count','Fixed operators and independent input state'),
('B07','OPERATING','1-16;24-31;46 onward','Bounded profile and initialization','Domain bounds do not specify modular structure'),
('B08','Z_READOUT','91-151;226-260','Norm, harmonic, cubic expression, memory','State readout is not elliptic j; cyclic counterexample'),
]
manifest={i['id']:i for i in json.loads((ROOT/'provenance/source_manifest.json').read_text())}
with (ROOT/'provenance/bridge_source_map.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['id','source_id','lines_or_section','existing_definition','conclusion','original_path','sha256','snapshot'])
    for row in bridge:
        i=manifest[row[1]];w.writerow([*row,i['original'],i['sha256'],i['snapshot']])
bib=[
('paper1','Three-Way Reciprocal Geometry: Reconstruction of a Historical Rational Model from Belyi Quotients to an Edwards Elliptic Galois Closure','2026','Mathematical reconstruction draft prepared for Hilmir F. Halldorsson with Codex assistance; v0.1; 5 October; sibling paper preserved unchanged',None),
('hierarchy','Three-Way reciprocal hierarchy, n = 2--4: first extension v0.1','2026','External report; snapshot HIERARCHY; exact script and output included',None),
('cubic','Three-Way cubic elliptic correspondence v0.1','2026','External report; snapshot CUBIC; exact script and output included',None),
('msw','Automorphism loci for the moduli space of rational maps','2014','Nikita Miasnikov, Brian Stout, Phillip Williams; arXiv:1408.5655v2; section 2.1 Lemma 2','https://arxiv.org/pdf/1408.5655'),
('pakovich','On rational functions whose normalization has genus zero or one','2017','Fedor Pakovich; arXiv:1609.03482v3; section 2; Theorems 1.1--1.2','https://arxiv.org/pdf/1609.03482'),
('elkies','Elliptic and modular curves over finite fields and related computational issues','1997','Noam D. Elkies; section 4 equation 80; source/quotient orientation recorded','https://people.math.harvard.edu/~elkies/modular.pdf'),
('patch','Six candidate apertures, the Z harmonic and a rotated toroidal motif','2026','Codex research report RESEARCH GATE TORUS v0.1; 24 September; snapshot PATCH',None),
('scaffold','Tri-Octagon reference scaffold and hexagon core derivation','2026','Snapshots SCAFFOLD and SCAFFOLD_PROOF; line map and hashes supplied',None),
('boundary','Tri-Octagon boundary response definitions','2026','Snapshot BOUNDARY; lens_area_norm_v1 explicit toy response',None),
('srg','Tri-Octagon fixed November transfer and initialization handoff','2026','Snapshot SRG; read-only source audit',None),
('operating','Tri-Octagon operating-region profile','2026','Snapshot OPERATING; read-only source audit',None),
('readout','Tri-Octagon passive harmonic and cubic state readouts','2026','Snapshot Z_READOUT; read-only source audit',None),
]
def esc(x):return x.replace('_',r'\_')
entries=[]
for key,title,year,note,url in bib:
    parts=[f'@misc{{{key},',f'  title = {{{title}}},',f'  year = {{{year}}},',f'  note = {{{esc(note)}}}'+(',' if url else '')]
    if url:parts.append(f'  url = {{{url}}}')
    entries.append('\n'.join(parts+['}']))
(ROOT/'bibliography.bib').write_text('\n\n'.join(entries)+'\n',encoding='utf-8')
# Make source paths breakable, without changing their content.
p=ROOT/'source/references.tex';text=p.read_text(encoding='utf-8')
text=re.sub(r'\\texttt\{([^{}]*(?:/|\\_)[^{}]*)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',text)
text=text.replace(r'\begin{thebibliography}{99}',r'\begin{thebibliography}{99}'+'\n'+r'\raggedright')
# Idempotent repeated generation.
text=text.replace('\\raggedright\n\\raggedright','\\raggedright')
p.write_text(text,encoding='utf-8')
(ROOT/'provenance/literature_checks.txt').write_text('Primary sources consulted 5 October 2026.\n\nMSW arXiv:1408.5655v2, section2.1 Lemma2: odd rational normal form. Their commuting automorphisms are not deck transformations.\nPakovich arXiv:1609.03482v3, section2, Theorems1.1-1.2: Galois-closure/normalization and low-genus context.\nElkies modular.pdf, section4 Eq80: standard X0(3) j-function and dual h ->729/h. Our source and quotient orientation is explicit.\n\nThese are bounded convention/context checks, not a complete prior-art audit. No novelty or priority claim is made.\n',encoding='utf-8')
(ROOT/'README.txt').write_text('THREE-WAY RECIPROCAL HIERARCHY / PAPER II / v0.1\n5 October 2026\n\nREAD: output/pdf/three_way_reciprocal_hierarchy_v0.1.pdf\nEDIT: source/main.tex and its six main section files plus evidence appendix.\nBIBLIOGRAPHY: bibliography.bib; typeset entries in source/references.tex.\nFIGURES: five figures, PDF/SVG/PNG; tools/make_figures.py regenerates them.\nVERIFY: run verification/hierarchy/verify_hierarchy.py, verification/cubic/verify_cubic_elliptic.py, verification/verify_bridge.py with Python plus SymPy/mpmath. The two older scripts are byte-identical copies and write only beside themselves. They retain local repository integrity checks; adapt REPO explicitly if rebuilding elsewhere.\nBUILD: python tools/build_paper.py. Uses the existing Tectonic executable and copied dedicated cache; environment overrides THREEWAY2_TECTONIC, THREEWAY2_TEX_CACHE, THREEWAY2_BUILD are supported. Cached-only by default. No kernel imports.\nAUDIT: python tools/write_evidence.py after a build, then python tools/audit_delivery.py using Python with pypdf/pdfplumber. tools/render_review.py renders pages with Poppler and makes visual review sheets.\nPROVENANCE: claim_ledger.csv, bridge_source_map.csv, source_manifest.json, numbered source snapshots, exact work order.\nRECORDS: build log, command/tool identity, visual audit, protected-file hash audit and final artifact manifest.\n\nRESULT: Generic Mon(F_n)=S_n; closure genus 1+n!(n-3)/2 over the unchanged F_n target. Generic n=2,3,4 genera are 0,1,13. Cubic marked moduli: X0(6), or X0(3) after forgetting reciprocal 2-torsion.\nFINAL BRIDGE STATUS: FINITE S3 BRIDGE ONLY. The exact patch incidence equivalence is retained. No independently justified continuous modular dictionary was supplied by inspected definitions; this is not a universal impossibility claim.\n\nTHREE-WAY RECIPROCAL HIERARCHY = PARKED\nPaper I, production code, kernel/UI and external source reports remain unchanged. No commits or publication performed.\n',encoding='utf-8')
print('Wrote',len(claims),'claim records,',len(bridge),'bridge source records,',len(bib),'bibliography entries.')
