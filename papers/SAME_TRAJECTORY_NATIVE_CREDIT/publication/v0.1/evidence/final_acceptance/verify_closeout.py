#!/usr/bin/env python3
"""Focused, read-only artifact check. No supplied helper or scientific code runs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,stat,zipfile,sys,unicodedata
from pypdf import PdfReader

root=Path(__file__).resolve().parents[2]
sub=root/'editorial_closeout_review/submission'
prefix='candidate_edition/papers/SAME_TRAJECTORY_NATIVE_CREDIT/publication/v0.1'
edition=sub/prefix
old=root/'paper_review/submission'/prefix
review=root/'paper_review/GPT_REVIEW'
out=Path(__file__).parent
checks=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
def ck(name,ok,**details):
    checks.append({'check':name,'pass':bool(ok),**details})
def record(p):
    b=p.read_bytes()
    return {'bytes':len(b),'sha256':sha(b)}
zip_path=root/'upload/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_EDITORIAL_CLOSEOUT_REVIEW_PACKAGE.zip'
zip_id=record(zip_path)
ck('Received ZIP identity',zip_id=={'bytes':11274165,'sha256':'3f0af614ff5f2ace1a37533f0f60f999bcc8bdcd75afbb5174d0501ccba33a24'})
ck('Adjacent checksum',zip_id['sha256']==zip_path.with_name(zip_path.name+'.sha256').read_text().split()[0])
with zipfile.ZipFile(zip_path) as z:
    names=z.namelist()
    ck('100 unique safe regular paths and valid CRC',len(names)==100==len(set(names))==len(set(n.casefold() for n in names)) and z.testzip() is None and all(not Path(i.filename).is_absolute() and '..' not in Path(i.filename).parts and ':' not in i.filename and '\\' not in i.filename and not stat.S_ISLNK(i.external_attr>>16) for i in z.infolist()))
    manifest=json.loads(z.read('PACKAGE_MANIFEST.json'))
    ck('Outer manifest exhaustive coverage',manifest['payload_count']==99 and manifest['total_zip_members']==100 and len(manifest['files'])==99 and {e['path'] for e in manifest['files']}|{manifest['self_excluded']}==set(names))
    for e in manifest['files']:
        b=z.read(e['path'])
        ck('Outer payload: '+e['path'],len(b)==e['bytes'] and sha(b)==e['sha256'] and (sub/e['path']).read_bytes()==b)
candidate=read(edition/'CANDIDATE_MANIFEST.json')
actual={p.relative_to(edition).as_posix() for p in edition.rglob('*') if p.is_file()}
ck('Candidate manifest exhaustive coverage',candidate['payload_count']==67==len(candidate['files']) and len(actual)==68 and {e['path'] for e in candidate['files']}|{candidate['self_excluded']}==actual)
for e in candidate['files']:
    ck('Candidate payload: '+e['path'],record(edition/e['path'])=={'bytes':e['bytes'],'sha256':e['sha256']})
pdf=edition/'SAME_TRAJECTORY_NATIVE_CREDIT_v0.1.pdf'
pdf_id=record(pdf)
ck('Accepted final PDF identity',pdf_id=={'bytes':109909,'sha256':'b1a3018a287cd1b0eda99ac82cd08102862672836afd66b51ca781d9dcb44e5e'})
ck('Manifest PDF bindings',manifest['final_pdf']['sha256']==candidate['pdf_sha256']==pdf_id['sha256'] and manifest['final_pdf']['bytes']==pdf_id['bytes'])
old_sentence=b'Fix the admissible geometry, positive storage scales and native coupling, and a nonzero coherent launch.'
new_sentence=b'Fix the admissible geometry, positive storage scales and native coupling, and a launch from the specified coherent family with nonzero chiral drive.'
old_main=(old/'manuscript/main.tex').read_bytes()
new_main=(edition/'manuscript/main.tex').read_bytes()
ck('MC-01 exact single replacement',old_main.count(old_sentence)==1 and new_main==old_main.replace(old_sentence,new_sentence) and new_main.count(new_sentence)==1)
ck('Corrected source exact supplied bytes',new_main==(review/'corrections/main.tex').read_bytes() and sha(new_main)=='a13d3288683947195c6c9e0e6fcc816e1fb700b2923b0b04bd82bcbfaefb3828')
tex={p.name:sha(p.read_bytes()) for p in (edition/'manuscript').glob('*.tex')}
ck('Exactly ten TeX files',len(tex)==10 and set(tex)=={p.name for p in (old/'manuscript').glob('*.tex')})
for n in sorted(tex):
    if n!='main.tex': ck('Unchanged scientific source: '+n,(edition/'manuscript'/n).read_bytes()==(old/'manuscript'/n).read_bytes())
helper=edition/'manuscript/build.py'
ck('Build helper unchanged',helper.read_bytes()==(old/'manuscript/build.py').read_bytes())
protected=[p for p in (old/'evidence').rglob('*') if p.is_file() and p!=(old/'evidence/README.md')]
ck('Thirty protected evidence files',len(protected)==30)
for p in protected:
    rel=p.relative_to(old)
    ck('Protected evidence: '+str(rel),(edition/rel).read_bytes()==p.read_bytes())
for local,baseline in [
('evidence/manuscript_review_2026_11_03.md',review/'NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_GPT_MANUSCRIPT_REVIEW.md'),
('evidence/editorial_closeout_order.md',review/'NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_EDITORIAL_CLOSEOUT_ORDER.md'),
('evidence/MC01_abstract_precision.patch',review/'corrections/abstract_precision.patch'),
('evidence/MC01_CORRECTION_IDENTITIES.json',review/'CORRECTION_IDENTITIES.json'),
('verification/MC01_EXACT_SOURCE_DIFF.patch',review/'corrections/abstract_precision.patch'),
('evidence/inputs/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_REVIEW_PACKAGE.zip',root/'upload/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_REVIEW_PACKAGE.zip'),
('evidence/inputs/SAME_TRAJECTORY_NATIVE_CREDIT_v0.1.pdf',root/'upload/SAME_TRAJECTORY_NATIVE_CREDIT_v0.1.pdf')]:
    ck('Retained review input: '+local,(edition/local).read_bytes()==baseline.read_bytes())
for local,baseline in [
('delivery_support/received_review/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_GPT_MANUSCRIPT_REVIEW_PACKAGE.zip',review/'NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_GPT_MANUSCRIPT_REVIEW_PACKAGE.zip'),
('delivery_support/received_packet/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_CODEX_PACKET.zip',root/'paper_order/NATIVE_SAME_TRAJECTORY_RETURN_PAPER_01_CODEX_PACKET.zip')]:
    ck('Retained original packet: '+local,(sub/local).read_bytes()==baseline.read_bytes())
registry=read(edition/'SOURCE_IDENTITIES.json')
for e in registry['published_sources']+registry['later_inputs']:
    ck('Source registry: '+e['id'],record(edition/e['retained_as'])=={'bytes':e['bytes'],'sha256':e['sha256']})
ck('Seven published files unchanged',(registry['published_sources']==read(old/'SOURCE_IDENTITIES.json')['published_sources']))
for p in [edition/'verification/BUILD_RECEIPT.json',sub/'delivery_support/build_final/build_receipt.json']:
    d=read(p)
    ck('Actual source/helper/PDF build binding: '+str(p.relative_to(sub)),d['sources']==tex and d['pdf_sha256']==pdf_id['sha256'] and d['pdf_bytes']==pdf_id['bytes'] and d['helper_sha256']==sha(helper.read_bytes()))
for n in ['DOCUMENT_CHECKS.json','VISUAL_INSPECTION.json','LABEL_CROSSWALK.json','PRESERVATION_CHECKS.json']:
    d=read(edition/'verification'/n)
    ck('Refreshed PDF/source binding: '+n,d['pdf_sha256']==pdf_id['sha256'] and ('sources' not in d or d['sources']==tex))
cross=read(edition/'verification/LABEL_CROSSWALK.json')
old_cross=read(old/'verification/LABEL_CROSSWALK.json')
for k in ['R1_R30','STR01_STR28','all_labels']:
    ck('Unchanged accepted crosswalk: '+k,cross[k]==old_cross[k])
ck('65 labels and 30/28 claim entries',len(cross['all_labels'])==65 and len(cross['R1_R30'])==30 and len(cross['STR01_STR28'])==28)
ck('Labels and auxiliary file unchanged',(edition/'verification/LABELS.json').read_bytes()==(old/'verification/LABELS.json').read_bytes() and (sub/'delivery_support/build_final/main.aux').read_bytes()==(root/'paper_review/submission/delivery_support/build_final/main.aux').read_bytes())
logs='\n'.join((sub/'delivery_support/build_final'/n).read_text(encoding='utf-8') for n in ['main.log','compiler.txt'])
warnings=[line for line in logs.splitlines() if re.search(r'\bwarning:|overfull|underfull|missing character:|^!',line,re.I)]
ck('Final build has no warning diagnostics',not warnings,diagnostics=warnings)
baseline=read(sub/'delivery_support/records/INPUT_BASELINE.json')['files']
pres=read(edition/'verification/PRESERVATION_CHECKS.json')
ck('Historical 139-file preservation record internally consistent',len(baseline)==pres['checked_files']==len(pres['files'])==139 and {e['path'] for e in pres['files']}==set(baseline) and all(e['unchanged'] and e['bytes']==baseline[e['path']]['bytes'] and e['sha256']==baseline[e['path']]['sha256'] for e in pres['files']))
ck('Preservation record copies identical',(edition/'verification/PRESERVATION_CHECKS.json').read_bytes()==(sub/'delivery_support/records/PRESERVATION_CHECKS.json').read_bytes())
reader=PdfReader(pdf)
old_reader=PdfReader(old/'SAME_TRAJECTORY_NATIVE_CREDIT_v0.1.pdf')
ck('Ten A4 pages',len(reader.pages)==10 and all(abs(float(p.mediabox.width)-595.28)<0.01 and abs(float(p.mediabox.height)-841.89)<0.01 for p in reader.pages))
ck('PDF page one contains exact replacement',' '.join(new_sentence.decode().split()) in ' '.join(unicodedata.normalize('NFKC',reader.pages[0].extract_text()).split()))
ck('PDF page text unchanged on pages 2-10',all(reader.pages[i].extract_text()==old_reader.pages[i].extract_text() for i in range(1,10)))
fonts={}
links=[]
dest=reader.named_destinations
for i,page in enumerate(reader.pages,1):
    for ref in page['/Resources']['/Font'].get_object().values():
        f=ref.get_object(); desc=f['/FontDescriptor'].get_object()
        fonts[str(f['/BaseFont'])]=any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
    for ref in page.get('/Annots',[]):
        a=ref.get_object().get('/A',{}).get_object()
        kind=str(a.get('/S',''))
        if kind=='/GoTo':
            links.append({'page':i,'type':'internal','target':str(a['/D']),'valid':str(a['/D']) in dest})
        elif kind=='/URI':
            target=str(a['/URI'])
            valid=(target=='https://github.com/pzychozen/trioctagon-physics/tree/273b1a6faaab19ea58748d00576439166eeef9ab/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1') if target.startswith('https:') else (edition/target).is_file()
            links.append({'page':i,'type':'URI','target':target,'valid':valid})
        else: links.append({'page':i,'type':kind,'valid':False})
ck('All 18 fonts embedded',len(fonts)==18 and all(fonts.values()))
ck('58 link annotations resolve to expected targets',len(links)==58 and all(l['valid'] for l in links))
bookmarks=[]
def walk(items):
    for item in items:
        if isinstance(item,list):walk(item)
        else:bookmarks.append({'title':str(item['/Title']),'page':reader.get_destination_page_number(item)+1})
walk(reader.outline)
ck('17 bookmarks resolve',len(bookmarks)==17 and all(1<=b['page']<=10 for b in bookmarks))
renders=[]
for i in range(1,11):
    name=f'page-{i:02d}.png'
    p=root/'editorial_closeout_review/independent_renders'/name
    earlier=root/'paper_review/independent_renders'/name
    same=p.read_bytes()==earlier.read_bytes()
    renders.append({'page':i,'current':record(p),'previously_inspected':record(earlier),'identical':same,'assessment':'Page 1 visually inspected after revision.' if i==1 else 'Entire fresh render byte-identical to the page previously visually inspected.'})
ck('Independent renders 2-10 identical; page 1 changed',not renders[0]['identical'] and all(e['identical'] for e in renders[1:]))
visual=read(edition/'verification/VISUAL_INSPECTION.json')
ck('Codex ten render files match refreshed records',len(visual['pages'])==10 and all(record(sub/e['render'])=={'bytes':e['bytes'],'sha256':e['sha256']} for e in visual['pages']))
result={
'created_utc':datetime.now(timezone.utc).isoformat(),
'disposition':('Focused artifact check passed; MC-01 closed; final manuscript accepted, ready for publication stage.' if all(c['pass'] for c in checks) else 'Verification incomplete; inspect failed checks.'),
'scope':'Exact editorial amendment, unchanged science/evidence, refreshed identities and independent rendering. No new scientific review, scientific execution, compilation, publication or Git operation.',
'input_zip':zip_id,'final_pdf':pdf_id,'corrected_main':record(edition/'manuscript/main.tex'),
'package_members':100,'outer_hashed_payloads':99,'candidate_files':68,'candidate_hashed_payloads':67,
'protected_evidence_files':30,'historical_external_preservation_record_count':139,
'checks':checks,'assertions':len(checks),'all_passed':all(c['pass'] for c in checks),
'pdf':{'pages':10,'fonts':fonts,'links':links,'bookmarks':bookmarks},
'independent_render_dpi':130,'independent_render_comparison':renders,
'visual_page_one':'PASS: exact revised abstract readable, title/subtitle/author/status and contribution note fit; no clipping, overlap or missing visible glyphs.',
'limits':'PDF independently rendered, recorded build not recompiled. Historical 139-file Windows preservation record checked for internal consistency; retained supplied evidence independently compared. No live machine or repository-wide audit. No separate corrected PDF was attached: reviewed the complete PDF inside the supplied ZIP.',
}
out.mkdir(parents=True,exist_ok=True)
(out/'FINAL_ARTIFACT_CHECKS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','pdf','independent_render_comparison']},indent=2))
for c in checks:
    if not c['pass']:print(json.dumps(c))
sys.exit(0 if result['all_passed'] else 1)
