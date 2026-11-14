"""Manuscript identity, transcription mapping and PDF checks only; no scientific replay."""
from pathlib import Path, PurePosixPath
import hashlib, json, zipfile, re, sys, platform, stat
from datetime import datetime, timezone
from pypdf import PdfReader
BASE=Path('/mnt/data'); WORK=BASE/'oe_manuscript_review'; ROOT=WORK/'submitted/manuscript'; OUT=WORK/'reviewer'
def sha(b): return hashlib.sha256(b).hexdigest()
def rd(p): return json.loads(Path(p).read_text('utf-8-sig'))
def identity(p,row):
    b=Path(p).read_bytes(); assert len(b)==row['bytes'], str(p); assert sha(b)==row['sha256'], str(p)
    return b
archive=BASE/'TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip'
audit=rd(BASE/'FINAL_ARCHIVE_AUDIT(2).json'); b=archive.read_bytes()
assert sha(b)==audit['archive_sha256']==(BASE/(archive.name+'.sha256')).read_text().split()[0]
assert len(b)==audit['archive_bytes']
with zipfile.ZipFile(archive) as z:
    names=z.namelist(); assert len(names)==len(set(names))==len(set(x.casefold() for x in names))==audit['member_count']
    for i in z.infolist():
        p=PurePosixPath(i.filename)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename
        assert not stat.S_ISLNK(i.external_attr>>16)
        z.read(i.filename)
    assert z.testzip() is None
    man=rd(ROOT/'PAYLOAD_MANIFEST.json')
    assert set(names)=={'manuscript/'+q['path'] for q in man['files']}|{'manuscript/PAYLOAD_MANIFEST.json'}
    for q in man['files']:
        v=z.read('manuscript/'+q['path']); assert len(v)==q['bytes'] and sha(v)==q['sha256']; assert v==(ROOT/q['path']).read_bytes()
    for q in audit['members']:
        v=z.read(q['path']); assert sha(v)==q['sha256'] and len(v)==q['bytes']
preserved=rd(ROOT/'PRESERVED_INPUTS.json')['files']
with zipfile.ZipFile(BASE/'TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_CODEX_PACKET.zip') as z:
    for q in preserved:
        v=identity(ROOT/q['path'],q); assert v==z.read(q['incoming_path']),q['path']
accept=ROOT/'archives/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_ACCEPTANCE_PACKAGE.zip'
assert accept.read_bytes()==(BASE/accept.name).read_bytes()
with zipfile.ZipFile(accept) as z:
    acceptance_count=len(z.namelist())
    for n in z.namelist(): assert z.read(n)==(ROOT/'evidence/outer_envelope'/n).read_bytes(),n
inv=ROOT/'evidence/outer_envelope/received/TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip'
assert inv.read_bytes()==(BASE/inv.name).read_bytes()
with zipfile.ZipFile(inv) as z:
    investigation_count=len(z.namelist())
    for n in z.namelist(): assert z.read(n)==(ROOT/'evidence/outer_envelope/submitted'/n).read_bytes(),n
sources=rd(ROOT/'verification/SOURCE_IDENTITY_CHECK.json')['sources']
for q in sources:
    v=identity(ROOT/q['path'],q)
    if q['recorded_git_blob_sha1'] is not None:
        assert hashlib.sha1(b'blob '+str(len(v)).encode()+b'\0'+v).hexdigest()==q['recorded_git_blob_sha1']
for ext in ['png','svg']:
    assert (ROOT/f'figures/local_facet_transition.{ext}').read_bytes()==(ROOT/f'evidence/outer_envelope/submitted/figures/local_facet_transition.{ext}').read_bytes()
pdf=ROOT/'TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf'; pdfb=pdf.read_bytes(); ph=sha(pdfb)
assert ph==audit['pdf_sha256']; assert len(pdfb)==audit['pdf_bytes']
build=rd(ROOT/'verification/final_build/BUILD_RECEIPT.json')
assert build['pdf_sha256']==ph and build['exit_status']==0
for n,h in build['raw_source_hashes'].items(): assert sha((ROOT/n).read_bytes())==h,n
log=(ROOT/'verification/final_build/main.log').read_text('utf-8',errors='replace')+'\n'+(ROOT/'verification/final_build/compiler.stderr').read_text('utf-8',errors='replace')
warnings=re.findall(r'^.*(?:Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning|undefined references|undefined citations|warning:).*$',log,re.M)
assert not warnings,warnings
reader=PdfReader(pdf); assert len(reader.pages)==12
fonts={}; internals=[]; page_records=[]
def scan_resource(res):
    res=res.get_object()
    if res.get('/Font'):
        for f in res['/Font'].get_object().values():
            f=f.get_object(); name=str(f.get('/BaseFont'))
            fs=f.get('/DescendantFonts',[f]); embedded=[]
            for ff in fs:
                ff=ff.get_object(); d=ff.get('/FontDescriptor'); d=d.get_object() if d else {}
                embedded.append(any(k in d for k in ['/FontFile','/FontFile2','/FontFile3']))
            assert all(embedded),name
            fonts[name]={'embedded':True,'subtype':str(f.get('/Subtype'))}
    if res.get('/XObject'):
        for obj in res['/XObject'].get_object().values():
            obj=obj.get_object()
            if obj.get('/Resources'): scan_resource(obj['/Resources'])
for i,p in enumerate(reader.pages,1):
    t=p.extract_text(); assert len(t)>500 and '\ufffd' not in t and '??' not in t
    assert t.rstrip().endswith(str(i))
    scan_resource(p['/Resources'])
    for x in p.get('/Annots',[]):
        x=x.get_object();d=x.get('/Dest');a=x.get('/A')
        if a:
            a=a.get_object()
            if a.get('/S')=='/GoTo': d=a.get('/D')
        if d is not None:
            assert not isinstance(d,str) or d in reader.named_destinations,(i,d)
            internals.append({'page':i,'destination':str(d)})
    page_records.append({'page':i,'characters':len(t),'text':t})
texts=[ROOT/'main.tex',ROOT/'references.tex',*sorted((ROOT/'tables').glob('*.tex'))]
tex='\n'.join(p.read_text('utf-8') for p in texts)
labels=re.findall(r'\\label\{([^}]+)\}',tex); refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',tex)
bib=re.findall(r'\\bibitem\{([^}]+)\}',tex); cites=[k.strip() for q in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex) for k in q.split(',')]
label_record=rd(ROOT/'verification/LABELS.json')
assert len(labels)==len(set(labels)) and set(labels)==set(label_record)
assert set(refs)<=set(labels) and set(cites)<=set(bib) and len(bib)==len(set(bib))==4
for label,q in label_record.items():
    # Hyperref anchor names carry the printed object number; actual page checked.
    prefix='section' if label.startswith(('sec:','app:')) else ('equation' if label.startswith('eq:') else ('table' if label.startswith('tab:') else ('figure' if label.startswith('fig:') else None)))
    if prefix:
        key=prefix+'.'+q['number']
        # Subsections use subsection anchors.
        if prefix=='section' and '.' in q['number']: key='subsection.'+q['number']
        if key in reader.named_destinations:
            assert reader.get_destination_page_number(reader.named_destinations[key])+1==q['pdf_page'],label
ledger=rd(ROOT/'MANUSCRIPT_CLAIM_LEDGER.json'); orig=rd(ROOT/'evidence/outer_envelope/submitted/CLAIM_LEDGER.json')
assert ledger['pdf_sha256']==ph
original_claims=orig['claims']; original_claims={x['id']:x for x in original_claims}
locations=0; evidence_identity_count=0
for c in ledger['claims']:
    assert c['original_ledger_record']==original_claims[c['claim_id']]
    for q in c['final_manuscript_locations']:
        target=label_record[q['label']]; assert target['number']==q['number'] and target['pdf_page']==q['pdf_page']
        assert '\\label{'+q['label']+'}' in (ROOT/q['source']).read_text('utf-8').splitlines()[q['source_line']-1],q
        locations+=1
    for q in c.get('evidence_identities',[]):
        identity(ROOT/q['path'].split('#')[0],q); evidence_identity_count+=1
    for name in c['evidence_paths']:
        base,_,fragment=name.partition('#'); assert (ROOT/base).exists(),name
        if fragment.startswith('/'):
            d=rd(ROOT/base)
            for comp in fragment[1:].split('/'):
                comp=comp.replace('~1','/').replace('~0','~');d=d[int(comp)] if isinstance(d,list) else d[comp]
assert set(c['claim_id'] for c in ledger['claims'])==set(original_claims)=={'O01','O02','O03','O04'}
links=rd(ROOT/'verification/LINK_CHECK.json')['new_document_links']
from urllib.parse import unquote
for row in links:
    dest=(ROOT/row['file']).parent/unquote(row['target'].split('#')[0]);assert dest.exists(),row
# No executable investigation code is imported, even indirectly.
result={'status':'PASS','scope':'Document and raw-file identity review only; no scientific code or certificate replay.',
'checked_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
'archive':{'sha256':sha(b),'bytes':len(b),'members':len(names),'manifest_entries':len(man['files'])},
'preserved_incoming_files':len(preserved),'acceptance_members':acceptance_count,'original_investigation_members':investigation_count,
'source_identity_records':len(sources),'source_git_blob_identities':sum(q['recorded_git_blob_sha1'] is not None for q in sources),'claims_mapped':len(ledger['claims']),'claim_manuscript_locations':locations,'claim_evidence_identities':evidence_identity_count,'new_document_links_checked':len(links),
'pdf':{'sha256':ph,'bytes':len(pdfb),'pages':len(reader.pages),'fonts_embedded':len(fonts),'labels':len(labels),'references':len(refs),'citation_uses':len(cites),'bibliography_entries':len(bib),'internal_links':len(internals),'metadata':{str(k):str(v) for k,v in reader.metadata.items()}},
'compiler_log_warnings':warnings,'new_scientific_runs':0,'repository_operations':0,'publication_operations':0,'visual_inspection':'Separate current review record.', 'limitations':['Build receipts/logs inspected; no compiler rerun during this audit.','No remote repository audit was performed.']}
OUT.mkdir(exist_ok=True)
(OUT/'DOCUMENT_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'PDF_TEXT.json').write_text(json.dumps({'pdf_sha256':ph,'pages':page_records},ensure_ascii=False,indent=2)+'\n')
(OUT/'PDF_RESOURCES.json').write_text(json.dumps({'fonts':fonts,'internal_links':internals},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
