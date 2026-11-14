"""Document-only publication payload checks/manifest. Never commits, pushes or executes science."""
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
import argparse,hashlib,json,os,re,sys,zipfile,stat,zlib
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification';NAME='TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf'
ap=argparse.ArgumentParser();ap.add_argument('--output-zip');args=ap.parse_args()
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
pdf=(ROOT/NAME).read_bytes();pdfsha=sha(pdf);doc=read(V/'DOCUMENT_CHECK.json');vis=read(V/'VISUAL_INSPECTION.json');build=read(V/'final_build/BUILD_RECEIPT.json')
assert doc['status']==vis['status']=='PASS' and pdfsha==doc['pdf_sha256']==vis['pdf_sha256']==build['pdf_sha256']
assert len(vis['pages'])==doc['page_count'] and build['exit_status']==0
for path,h in build['raw_source_hashes'].items():assert sha((ROOT/path).read_bytes())==h
assert sha((ROOT/'build.py').read_bytes())==build['build_helper_sha256']
for row in vis['pages']:assert sha((ROOT/row['path']).read_bytes())==row['sha256'] and row['visual_status']=='PASS'
for name in ['FONT_CHECK.json','REFERENCE_CHECK.json','SOURCE_IDENTITY_CHECK.json','TRANSCRIPTION_CHECK.json','NUMBERING_CHECK.json']:
    obj=read(V/name);assert obj['status']=='PASS'
for path,h in read(V/'TRANSCRIPTION_CHECK.json')['generated_table_hashes'].items():assert sha((ROOT/path).read_bytes())==h
pres=read(ROOT/'PRESERVED_INPUTS.json')['files'];pub=read(ROOT/'PUBLICATION_INPUTS.json')['files']
for row in pres+pub:
    b=(ROOT/row['path']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256']
prov=ROOT/'provenance/publication';review=prov/'received/TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip'
assert sha(review.read_bytes())==review.with_name(review.name+'.sha256').read_text().split()[0]
with zipfile.ZipFile(review) as z:
    assert z.testzip() is None and len(z.namelist())==281
    for row in read(prov/'ADMINISTRATIVE_SOURCE_EDITS.json')['files']:
        b=(ROOT/row['path']).read_bytes()
        for e in reversed(row['edits']):
            a=e['new_after_author_activation'].encode();old=e['old'].encode();assert b.count(a)==1;b=b.replace(a,old)
        assert b==z.read('manuscript/'+row['path']) and sha(b)==row['original_sha256']
    for row in read(prov/'FROZEN_CONTENT_CHECK.json')['frozen_files']:
        assert (ROOT/row['path']).read_bytes()==z.read('manuscript/'+row['path'])
    for row in pres:assert (ROOT/row['path']).read_bytes()==z.read('manuscript/'+row['path'])
accept=ROOT/'archives/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_ACCEPTANCE_PACKAGE.zip'
with zipfile.ZipFile(accept) as z:
    assert z.testzip() is None and len(z.namelist())==175
    for n in z.namelist():assert z.read(n)==(ROOT/'evidence/outer_envelope'/n).read_bytes()
original=ROOT/'evidence/outer_envelope/received/TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip'
with zipfile.ZipFile(original) as z:
    assert z.testzip() is None and len(z.namelist())==143
    for n in z.namelist():assert z.read(n)==(ROOT/'evidence/outer_envelope/submitted'/n).read_bytes()
links=[]
for p in [ROOT/'README.md',ROOT/'HANDOFF.md',ROOT/'BUILD.md',ROOT/'ACCESS_AND_EVIDENCE_MAP.md',ROOT.parents[1]/'README.md']:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match('[a-z]+://',target):continue
        assert (p.parent/target.split('#')[0]).exists(),(p,target)
        links.append({'file':str(p.relative_to(ROOT.parents[1])),'target':target,'exists':True})
write(V/'LINK_CHECK.json',{'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'new_local_links':links,'count':len(links),'scope':'Current edition guides and landing page; inherited historical links are preserved rather than asserted current.'})
ledger=read(ROOT/'MANUSCRIPT_CLAIM_LEDGER.json');assert ledger['pdf_sha256']==pdfsha and len(ledger['claims'])==4
for c in ledger['claims']:
    for loc in c['final_manuscript_locations']:
        assert '\\label{'+loc['label']+'}' in (ROOT/loc['source']).read_text(encoding='utf-8').splitlines()[loc['source_line']-1]
write(V/'PUBLICATION_PAYLOAD_CHECK.json',{'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'pdf_sha256':pdfsha,'pages':doc['page_count'],'claims':4,'inherited_inputs':len(pres),'publication_packet_members':len(pub),'intact_review_members':281,'intact_acceptance_members':175,'intact_investigation_members':143,'administrative_edits_reversible':True,'frozen_science_unchanged':True,'new_scientific_runs':0,'stage':'Author-authorized repository publication payload; execution receipt remains external.'})
oldpaths={r['path'] for r in pres}|{r['path'] for r in pub};text=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in oldpaths or rel in ['PAYLOAD_MANIFEST.json','verification/NEW_TEXT_INVENTORY.json'] or rel.startswith('verification/submission/'):continue
    b=p.read_bytes()
    try:b.decode('utf-8')
    except UnicodeDecodeError:continue
    text.append({'path':rel,'bytes':len(b),'sha256':sha(b),'CRLF':b.count(b'\r\n'),'LF_without_CR':b.count(b'\n')-b.count(b'\r\n')})
write(V/'NEW_TEXT_INVENTORY.json',{'policy':'Preserve all inherited raw line endings; authorized source replacements are applied as UTF-8 bytes without newline normalization. New administrative text is UTF-8 LF; document tool outputs retain native Windows writer line endings. No post-build source normalization.','current_text_files':text})
rows=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if rel=='PAYLOAD_MANIFEST.json':continue
    assert not p.is_symlink();assert p.suffix.lower() not in ['.exe','.dll','.ttf','.otf','.woff','.pfb','.pyc','.aux','.out','.xdv'],rel
    b=p.read_bytes();rows.append({'path':rel,'bytes':len(b),'sha256':sha(b)})
names=[r['path'] for r in rows];assert len(names)==len({n.casefold() for n in names})
write(ROOT/'PAYLOAD_MANIFEST.json',{'schema':'publication-raw-byte-manifest-v1','task':'TRIOCTAGON_OUTER_ENVELOPE_PUBLISH_01','self_excluded':'PAYLOAD_MANIFEST.json','publication_pdf_sha256':pdfsha,'files':rows})
if args.output_zip:
    zp=Path(args.output_zip).resolve();assert not zp.is_relative_to(ROOT);zp.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for row in [*rows,{'path':'PAYLOAD_MANIFEST.json'}]:z.write(ROOT/row['path'],'publication/'+row['path'])
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None
        for n in z.namelist():assert z.read(n)==(ROOT/n.removeprefix('publication/')).read_bytes()
print(json.dumps({'status':'PASS','publication_payload_members':len(rows)+1,'manifest_entries':len(rows),'preserved_inputs':len(pres),'publication_packet_members':len(pub),'links':len(links),'pdf_sha256':pdfsha}))
