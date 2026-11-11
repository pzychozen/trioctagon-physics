"""Read-only manuscript/document audit. Does not execute research or rebuild PDFs."""
from pathlib import Path, PurePosixPath
from fractions import Fraction as F
from datetime import datetime, timezone
import json, hashlib, zipfile, re, platform, sys, subprocess
from pypdf import PdfReader
import fitz

BASE=Path('/mnt/data'); ROOT=BASE/'capture_note_manuscript_review'; P=ROOT/'submitted'
OUT=ROOT/'reviewer'; OUT.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
results=[]
def good(name, detail):
    results.append({'check':name,'status':'PASS','detail':detail})
def identity(record, root=P):
    b=(root/record['path']).read_bytes()
    assert sha(b)==record['sha256'],record['path']
    if 'bytes' in record: assert len(b)==record['bytes'],record['path']
    return b
zfile=BASE/'NATIVE_TURNING_CAPTURE_PAPER_01_REVIEW.zip'
audit=load(BASE/'NATIVE_TURNING_CAPTURE_PAPER_01_FINAL_DELIVERY_AUDIT.json')
assert sha(zfile.read_bytes())==(BASE/(zfile.name+'.sha256')).read_text().split()[0]==audit['archive_sha256']
assert zfile.stat().st_size==audit['archive_bytes']
with zipfile.ZipFile(zfile) as z:
    names=z.namelist()
    assert len(names)==len(set(names))==176==audit['member_count']
    assert z.testzip() is None
    for name in names:
        parts=PurePosixPath(name).parts
        assert not PurePosixPath(name).is_absolute() and '..' not in parts and '\\' not in name
        assert (P/name).read_bytes()==z.read(name)
    assert set(names)=={r['path'] for r in audit['members']}
    for r in audit['members']: identity(r)
good('input_archive',{'members':len(names),'bytes':zfile.stat().st_size,'sha256':sha(zfile.read_bytes()),'sidecar_and_external_audit':'match'})
manifest=load(P/'REVIEW_MANIFEST.json')
assert len(manifest['files'])==175
assert {r['path'] for r in manifest['files']}==set(names)-{'REVIEW_MANIFEST.json'}
for r in manifest['files']: identity(r)
good('self_excluding_manifest',175)
inputs=load(P/'PRESERVED_INPUTS.json')['files']
commission=BASE/'NATIVE_TURNING_CAPTURE_PAPER_01_CODEX_PACKET.zip'
with zipfile.ZipFile(commission) as z:
    for r in inputs:
        assert identity(r)==z.read(r['original_packet_path'])
good('preserved_commission_inputs',len(inputs))
accepted=P/'archives/NATIVE_TURNING_CAPTURE_01_GPT_ACCEPTANCE_PACKAGE.zip'
assert sha(accepted.read_bytes())==(P/(str(accepted.relative_to(P))+'.sha256')).read_text().split()[0]
with zipfile.ZipFile(accepted) as z:
    nn=[n for n in z.namelist() if not n.endswith('/')]
    for n in nn: assert (P/'evidence/accepted_capture'/n).read_bytes()==z.read(n)
good('accepted_evidence_exact_extract',len(nn))
source_inventory=load(P/'SOURCE_INVENTORY.json')
for r in source_inventory['source_usage']: identity(r)
good('source_inventory',len(source_inventory['source_usage']))
ledger=load(P/'MANUSCRIPT_CLAIM_LEDGER.json'); old=load(P/ledger['original_ledger'])
assert sha((P/ledger['original_ledger']).read_bytes())==ledger['original_ledger_sha256']
old_records=old['records'] if 'records' in old else old['claims']
old_by={r.get('id',r.get('claim_id')):r for r in old_records}
refmap=load(P/'verification/REFERENCE_MAP.json')
ml=sl=0
for record in ledger['records']:
    assert record['original_id'] in old_by
    for loc in record['manuscript_locations']:
        text=identity(loc).decode('utf-8')
        assert '\\label{'+loc['label']+'}' in text.splitlines()[loc['line']-1]
        assert refmap['labels'][loc['label']]=={'number':loc['number'],'page':loc['pdf_page']}
        ml+=1
    for loc in record['accepted_source_locators']:
        text=identity(loc).decode('utf-8')
        assert loc['locator'] in text.splitlines()[loc['line']-1],loc
        sl+=1
assert {r['original_id'] for r in ledger['records']}==set(old_by)
good('manuscript_claim_crosswalk',{'original_ids':len(ledger['records']),'manuscript_locations':ml,'accepted_source_locators':sl})
main=(P/'main.tex').read_text();refs=(P/'references.tex').read_text();table=(P/'tables/terminal_bounds.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',main+refs+table)
used=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',main+refs+table)
cites=set(k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',main+refs) for k in group.split(','))
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',refs))
assert len(labels)==len(set(labels))==39
assert set(labels)==set(refmap['labels']) and set(used)<=set(labels)
assert cites==bibs==set(refmap['citations']) and len(bibs)==4
assert refmap['unresolved_references']==refmap['unresolved_citations']==[]
good('source_reference_consistency',{'labels':len(labels),'reference_uses':len(used),'citations':len(cites)})
source_paths=['main.tex','references.tex','tables/terminal_bounds.tex']
build=load(P/'verification/BUILD_RECEIPT.json')
for path in source_paths: assert sha((P/path).read_bytes())==build['sources'][path]
log=(P/'verification/TEX_LOG.txt').read_text()+'\n'+(P/'verification/COMPILER_MESSAGES.txt').read_text()
warnings=[l for l in log.splitlines() if re.search(r'^LaTeX Warning:|^Package .* Warning:|^Class .* Warning:|^Overfull|^Underfull|^Missing character|^!|^warning:',l,re.I)]
assert not warnings and build['exit_status']==0
good('supplied_build_evidence',{'sources_match':True,'warnings':warnings,'rebuild_executed_by_this_review':False})
pdf=P/'NATIVE_TURNING_CAPTURE_COMPANION_v0.1.pdf'; reader=PdfReader(pdf)
assert len(reader.pages)==7 and sha(pdf.read_bytes())==build['pdf_sha256']==ledger['pdf_sha256']
assert reader.metadata.title=='Certified Capture of the Collective-Turning Trajectory in the Native Triad'
assert reader.metadata.author=='Hilmir Frímann Halldórsson (pzychozen)'
assert 'review pending' in reader.metadata.subject
fonts={}
for page in reader.pages:
    for _,ref in page['/Resources'].get('/Font',{}).items():
        obj=ref.get_object()
        for sub in obj.get('/DescendantFonts') or [obj]:
            sub=sub.get_object();name=str(sub.get('/BaseFont',obj.get('/BaseFont')))
            desc=sub.get('/FontDescriptor');assert desc is not None
            desc=desc.get_object();programs=[k for k in ['/FontFile','/FontFile2','/FontFile3'] if k in desc and len(desc[k].get_object().get_data())>0]
            assert programs,name
            fonts[name]=programs
assert len(fonts)==17
good('pdf_identity_fonts_metadata',{'sha256':sha(pdf.read_bytes()),'bytes':pdf.stat().st_size,'pages':7,'embedded_fonts':len(fonts),'status':'submitted pending-review label retained; this review supersedes GPT-pending status only'})
relative_links=re.findall(r'\\href\{([^}]+)\}',refs+main)
for link in relative_links: assert (P/link).is_file() and '://' not in link
assert len(relative_links)==7
good('relative_source_links',len(relative_links))
doc=fitz.open(pdf); pagechecks=[]
for i,page in enumerate(doc,1):
    text=page.get_text()
    assert '??' not in text
    outside=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                box=fitz.Rect(span['bbox'])
                if not page.rect.contains(box): outside.append({'text':span['text'],'bbox':list(box)})
    assert not outside,(i,outside)
    pagechecks.append({'page':i,'no_text_outside_page':True,'text_characters':len(text),'render_sha256':sha((ROOT/f'rendered/page-{i}.png').read_bytes())})
good('pdf_text_page_bounds',pagechecks)
check=load(P/'evidence/accepted_capture/submitted/data/CERTIFICATE_CHECK.json')
expected=[('0.997219','0.997220'),('0.997622','0.997623'),('0.996782','0.996783')]
for i,r in enumerate(check['terminal']):
    a,b=expected[i];assert [F(a),F(b)]==list(map(F,r['amplitude_bounds']))
    assert f'{"ABC"[i]} & {a} & {b} & {r["cone_margin_lower_integer"]}' in table
assert check['early_turn_enclosure']==['0.0110760731','0.0110760732']
assert F('1.07701')*F(1,4)**2/8==F(107701,12800000)
assert F('1.1')/4==F(11,40)
assert F(11,10)-F(9,10)==F(1,5)
# Rational sufficient comparison c^2 > beta, using sqrt(2)<3/2.
assert 1-F(3,100)*F(3,2)+F(9,20000)>F(8571,10000)
good('accepted_number_transcription',{'amplitude_endpoints':6,'cone_margins':3,'tail_coefficients':'exact rational matches','scientific_checker_rerun':False})
# Final integrity check: no submitted file was changed by these operations.
for r in manifest['files']: identity(r)
good('submitted_payload_unchanged_after_review',175)
record={'task':'NATIVE_TURNING_CAPTURE_PAPER_01_GPT_MANUSCRIPT_REVIEW','completed_utc':datetime.now(timezone.utc).isoformat(),'review_environment':{'python':sys.version,'platform':platform.platform()},'status':'PASS','scope':'Read-only artifact audit and manuscript transcription checks; no scientific or historical-suite rerun; no source edit, rebuild or Git operation.','checks':results,'scientific_executions':0,'submitted_archive_sha256':sha(zfile.read_bytes()),'script_sha256':sha(Path(__file__).read_bytes())}
(OUT/'MANUSCRIPT_AUDIT.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','audit_groups':len(results),'archive_members':len(names),'manifest_entries':175,'preserved_inputs':len(inputs),'source_inventory':18,'claim_records':16,'manuscript_locations':ml,'source_locators':sl,'pages':7,'fonts':len(fonts),'labels':len(labels),'citations':len(cites)},indent=2))
