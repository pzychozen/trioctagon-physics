"""Check a built edition and write the reproducibility/claim records.
No historical source, external analytical report, kernel, or UI file is written.
"""
from pathlib import Path
from pypdf import PdfReader
import re,json,hashlib,csv,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source='\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT/'source').glob('*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',source)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
assert len(labels)==len(set(labels)), 'Duplicate labels'
assert not set(refs)-set(labels),('Unresolved source references',set(refs)-set(labels))
cites=[]
for cs in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',source):cites.extend(cs.split(','))
keys=re.findall(r'\\bibitem\{([^}]+)\}',source)
bibkeys=re.findall(r'@\w+\{([^,]+),',(ROOT/'bibliography.bib').read_text(encoding='utf-8'))
assert set(keys)==set(bibkeys), 'BibTeX and typeset bibliography differ'
assert not set(cites)-set(keys),'Unresolved citations'
figs=re.findall(r'\\fig\{([^}]+)\}',source)
assert len(figs)==10
for name in figs:
    for ext in ['pdf','svg','png']:assert (ROOT/'figures'/f'{name}.{ext}').exists()
log=(ROOT/'records/latex_build.log').read_text(encoding='utf-8',errors='replace')
for bad in ['Overfull','Missing character','undefined references','undefined on input','multiply defined']:
    assert bad not in log,bad
pdf=ROOT/'output/pdf/three_way_reconstruction_v0.1.pdf';reader=PdfReader(pdf)
text='\n'.join(pg.extract_text() or '' for pg in reader.pages)
assert '\ufffd' not in text and '??' not in text,'Broken extracted text'
assert all(len(pg.extract_text() or '')>100 for pg in reader.pages),'Blank page'
destinations=reader.named_destinations
broken=[];internal_count=0;external=set()
for pg in reader.pages:
    for a in pg.get('/Annots',[]):
        obj=a.get_object();act=obj.get('/A',{});dest=obj.get('/Dest')
        if act.get('/S')=='/URI':external.add(str(act.get('/URI')))
        if act.get('/S')=='/GoTo':dest=act.get('/D')
        if dest is not None:
            internal_count+=1
            if isinstance(dest,str) and dest not in destinations:broken.append(dest)
assert not broken,broken
baseline=json.loads((ROOT/'records/baseline.json').read_text(encoding='utf-8'))
changed=[]
for p,h in baseline['protected'].items():
    pp=REPO/p
    if not pp.exists() or sha(pp)!=h:changed.append(p)
assert not changed,('Protected files changed',changed)
manifest=json.loads((ROOT/'provenance/source_manifest.json').read_text(encoding='utf-8'))
for item in manifest:
    assert sha(Path(item['original']))==item['sha256'],item['original']
    assert sha(ROOT/item['snapshot'])==item['sha256'],item['snapshot']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()==baseline['head'],'HEAD changed'
res=json.loads((ROOT/'verification/results.json').read_text())
assert all(c['passed'] for c in res['exact_checks'])
aux=(ROOT/'records/main.aux').read_text(encoding='utf-8')
num={k:(n,p) for k,n,p in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux)}
claims=[
('C01','Formula provenance, sign conflict and integer-pair conflict','sec:history','H1 pp.13–14; H2 pp.2–3 and code/CSV; H3 p.3 Eq.1; H4 p.1','R1 §1; R3 §1','H1,H2,H3,H4','Documentary, not a mathematical theorem'),
('C02','Reciprocity, parity and exact plus/minus-one fibers','prop:levels','H1 Appendix C; H3 §2; M1','R3 §6','H1,H3,M1','Exact proof'),
('C03','Zeros, poles, resultant, cancellation and real roots','prop:divisors','Corrects H1 p.14; H2 asymptote CSV','R3 §§2,6–7','H1,H2','Exact proof'),
('C04','Second involution and coherent normalized form','thm:normal','No historical attribution','R1 §§13–14; R3 §§3–4','','Exact proof'),
('C05','Universal V4 Belyi quotient and fixed branch data','thm:belyi','No historical attribution','R1 §14; R2; R3 §4','SV,KO','Exact proof; established species'),
('C06','Lambda complete for labeled reduced geometry','sec:belyi','No historical attribution','R3 §5','','Exact proof with specified equivalence'),
('C07','Real forms and fixed plotting restrictions','sec:real','H1 plots only','R3 §7; R4 §9','','Exact proof/domain statement'),
('C08','Large-L limits and both matching overlaps','thm:matching','No historical attribution','R1 §§3–12','','Exact proof, supported by numerical checks'),
('C09','Finite-L origins of intermediate involutions and shoulders','eq:Rh','No historical attribution','R1 §§12–14','','Exact proof'),
('C10','Degree-eight map, branch data, and lift exceptions','thm:xcover','Original y=x^2 retained','R3 §8; R4 §§2,7','','Exact proof'),
('C11','M0,5 coarse classification and four coefficient presentations','thm:moduli','No historical attribution','R4 §§1–5','Mnev','Exact proof within selected Hurwitz type'),
('C12','Covering type, stack distinction and intrinsic intermediate','sec:moduli','No historical attribution','R4 §§3–6','','Exact proof/definition distinction'),
('C13','Degree-sixteen genus-one normal closure and monodromy','thm:galois','No historical attribution','R4 §6; R5 §§1,6','','Exact proof and finite permutation check'),
('C14','Stable target and admissible-cover boundaries','sec:boundary','No historical attribution','R4 §§7–8','Braungardt,CMR','Exact parameter identities; standard compactification framework'),
('C15','Edwards and explicit alternative elliptic models','sec:edwards','No historical attribution','R5 §§1–3','Edwards,Morain,EFD','Exact birational identities; established models'),
('C16','Translation group and two Kummer V4 actions','sec:group','No historical attribution','R5 §6','EFD','Exact proof using elliptic addition'),
('C17','Nu as X0(4) coordinate and natural two-isogeny','thm:X04','No historical attribution','R5 §§3,6','Sutherland,Morain','Exact completeness proof and isogeny'),
('C18','Lambda as effective degree-sixteen orbit divisor','sec:divisor','No historical attribution','R5 §7','','Exact divisor and group argument'),
('C19','Original sphere, elliptic torus and revolution are different','sec:topology','H1/H4 toroidal language delimited','R4 §6; R5 §§4,10','H1,H4','Theorem-level genus statement plus conditional revolution example'),
('C20','Four historical invariant sets and CM conclusions','sec:examples','H1/H2 coefficient witnesses','R3 §9; R5 §8','DLR','Exact for three CM rejections; pi,e CM unresolved'),
('C21','Reduced chain quotient and bounded negative dictionary','sec:physics','Historical physical claims not assumed','R2; R3 §10','Tong','Exact reduced identity; no independently selected full observable established'),
('C22','No novelty or priority claim in this edition','sec:lessons','Distinguishes reconstruction from historical intuition','All reports, synthesized','','Editorial scope; dedicated audit pending')]
with (ROOT/'provenance/claim_ledger.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['id','claim','manuscript_label','number','printed_page','historical_evidence','external_report','literature_keys','status','priority_status'])
    for cid,claim,label,hist,report,lit,status in claims:
        n,p=num[label];w.writerow([cid,claim,label,n,p,hist,report,lit,status,'Not assessed; no priority claim'])
audit=dict(pages=len(reader.pages),source_labels=len(labels),source_references=len(refs),bibliography_entries=len(keys),citations_resolved=True,internal_pdf_links=internal_count,broken_internal_links=broken,external_urls=sorted(external),figures=len(figs),exact_checks=res['exact_count'],normal_form_cases=res['normal_form_cases'],protected_files_checked=len(baseline['protected']),protected_files_changed=changed,evidence_files_checked=len(manifest),originals_and_snapshots_unchanged=True,head_unchanged=True,underfull_box_warnings=len(re.findall('Underfull',log)),overfull_boxes=0,missing_glyphs=0)
(ROOT/'records/delivery_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
(ROOT/'records/pdf_text.txt').write_text(text,encoding='utf-8')
artifact={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='artifact_manifest.json' and '__pycache__' not in p.parts}
(ROOT/'records/artifact_manifest.json').write_text(json.dumps(artifact,indent=2),encoding='utf-8')
print(json.dumps(audit,indent=2))
