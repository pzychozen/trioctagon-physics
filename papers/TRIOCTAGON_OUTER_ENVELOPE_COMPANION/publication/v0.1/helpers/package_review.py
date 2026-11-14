"""Package and byte-audit this manuscript. No scientific code is run or imported."""
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
import argparse,hashlib,io,json,os,re,stat,sys,zipfile,zlib
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification';NAME='TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf'
ap=argparse.ArgumentParser();ap.add_argument('--incoming-packet',required=True);ap.add_argument('--standalone-pdf',required=True);ap.add_argument('--built-pdf',required=True);ap.add_argument('--output-dir',required=True);a=ap.parse_args()
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def safe(z):
    names=z.namelist();assert len(names)==len(set(names))==len({n.casefold() for n in names})
    for info in z.infolist():
        n=info.filename;p=PurePosixPath(n)
        assert not p.is_absolute() and '..' not in p.parts and ':' not in n and '\\' not in n
        assert not stat.S_ISLNK(info.external_attr>>16)
    assert z.testzip() is None
    return names
pdf=(ROOT/NAME).read_bytes();pdfsha=sha(pdf);doc=read(V/'DOCUMENT_CHECK.json');vis=read(V/'VISUAL_INSPECTION.json');receipt=read(V/'final_build/BUILD_RECEIPT.json')
assert pdfsha==doc['pdf_sha256']==vis['pdf_sha256']==receipt['pdf_sha256']
assert pdf==Path(a.standalone_pdf).read_bytes()==Path(a.built_pdf).read_bytes()
assert doc['status']==vis['status']=='PASS' and doc['page_count']==len(vis['pages'])==12
for row in vis['pages']:assert row['visual_status']=='PASS' and sha((ROOT/row['path']).read_bytes())==row['sha256']
for path,h in receipt['raw_source_hashes'].items():assert sha((ROOT/path).read_bytes())==h
assert sha((ROOT/'build.py').read_bytes())==receipt['build_helper_sha256']
for record in ['TRANSCRIPTION_CHECK.json','FONT_CHECK.json','REFERENCE_CHECK.json','SOURCE_IDENTITY_CHECK.json','FIGURE_EMBEDDING.json']:
    obj=read(V/record);assert obj['status']=='PASS'
    if 'pdf_sha256' in obj:assert obj['pdf_sha256']==pdfsha
for path,h in read(V/'TRANSCRIPTION_CHECK.json')['generated_table_hashes'].items():assert sha((ROOT/path).read_bytes())==h
pres=read(ROOT/'PRESERVED_INPUTS.json')['files'];incoming=Path(a.incoming_packet)
assert sha(incoming.read_bytes())==read(V/'INPUT_VERIFICATION.json')['packet_sha256']
with zipfile.ZipFile(incoming) as z:
    names=safe(z);assert len(names)==len(pres)==187
    for row in pres:
        b=(ROOT/row['path']).read_bytes();assert b==z.read(row['incoming_path']) and len(b)==row['bytes'] and sha(b)==row['sha256']
acc=ROOT/'archives/TRIOCTAGON_OUTER_ENVELOPE_01_GPT_ACCEPTANCE_PACKAGE.zip'
with zipfile.ZipFile(acc) as z:
    acnames=safe(z);assert len(acnames)==175
    for n in acnames:assert z.read(n)==(ROOT/'evidence/outer_envelope'/n).read_bytes()
original=ROOT/'evidence/outer_envelope/received/TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip'
with zipfile.ZipFile(original) as z:
    original_names=safe(z);assert len(original_names)==143
    for n in original_names:assert z.read(n)==(ROOT/'evidence/outer_envelope/submitted'/n).read_bytes()
links=[]
for n in ['README.md','BUILD.md','HANDOFF.md','ACCESS_AND_EVIDENCE_MAP.md']:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',(ROOT/n).read_text(encoding='utf-8')):
        assert not re.match(r'^[a-z]+://',target),target
        assert (ROOT/target.split('#')[0]).exists(),(n,target)
        links.append({'file':n,'target':target,'exists':True})
write(V/'LINK_CHECK.json',{'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'new_document_links':links,'count':len(links),'scope':'New delivery guides. Original historic source links/commands are preserved, not represented as current remote endpoints.'})
ledger=read(ROOT/'MANUSCRIPT_CLAIM_LEDGER.json');assert ledger['pdf_sha256']==pdfsha and {c['claim_id'] for c in ledger['claims']}=={'O01','O02','O03','O04'}
for claim in ledger['claims']:
    assert claim['final_manuscript_locations']
    for loc in claim['final_manuscript_locations']:
        line=(ROOT/loc['source']).read_text(encoding='utf-8').splitlines()[loc['source_line']-1]
        assert '\\label{'+loc['label']+'}' in line
write(V/'CLOSEOUT_CHECK.json',{'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'pdf_sha256':pdfsha,'claims_mapped':4,'inherited_groups':len(ledger['inherited_not_new']),'preserved_incoming_files':187,'acceptance_members_equal':175,'original_investigation_members_equal':143,'scientific_runs_during_authoring':0,'repository_operations':0,'state':'Manuscript returned for GPT and author review; no publication.'})
prespaths={row['path'] for row in pres};textrows=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in prespaths or rel in ['PAYLOAD_MANIFEST.json','verification/NEW_TEXT_INVENTORY.json']:continue
    b=p.read_bytes()
    try:b.decode('utf-8')
    except UnicodeDecodeError:continue
    textrows.append({'path':rel,'bytes':len(b),'sha256':sha(b),'CRLF':b.count(b'\r\n'),'LF_without_CR':b.count(b'\n')-b.count(b'\r\n'),'bare_CR':b.count(b'\r')-b.count(b'\r\n')})
write(V/'NEW_TEXT_INVENTORY.json',{'policy':'UTF-8 for new text. Hand-authored source files use LF; native Windows writer outputs retain CRLF. Actual per-file counts below; inherited bytes never normalized. Inventory and payload manifest are excluded from this inventory to avoid self-hashes.','files':textrows})
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if rel=='PAYLOAD_MANIFEST.json':continue
    assert not p.is_symlink()
    if rel not in prespaths:assert p.suffix.lower() not in ['.exe','.dll','.ttf','.otf','.pfb','.woff','.aux','.out','.xdv','.pyc'] and '__pycache__' not in p.parts,rel
    b=p.read_bytes();files.append({'path':rel,'bytes':len(b),'sha256':sha(b)})
manifest={'schema':'raw-byte-payload-manifest-v1','root':'manuscript','self_excluded':'PAYLOAD_MANIFEST.json','files':files}
write(ROOT/'PAYLOAD_MANIFEST.json',manifest)
out=Path(a.output_dir).resolve();assert not out.is_relative_to(ROOT);out.mkdir(parents=True,exist_ok=True)
zp=out/'TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_REVIEW.zip'
with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for row in [*files,{'path':'PAYLOAD_MANIFEST.json'}]:z.write(ROOT/row['path'],'manuscript/'+row['path'])
members=[]
with zipfile.ZipFile(zp) as z:
    names=safe(z);assert len(names)==len(files)+1
    archived_manifest=json.loads(z.read('manuscript/PAYLOAD_MANIFEST.json'));assert archived_manifest==manifest
    for name in names:
        rel=name.removeprefix('manuscript/');assert 'manuscript/'+rel==name
        b=z.read(name);info=z.getinfo(name);assert b==(ROOT/rel).read_bytes() and len(b)==info.file_size and zlib.crc32(b)==info.CRC
        if rel!='PAYLOAD_MANIFEST.json':
            row=next(r for r in files if r['path']==rel);assert len(b)==row['bytes'] and sha(b)==row['sha256']
        members.append({'path':name,'bytes':len(b),'sha256':sha(b),'crc32':f'{info.CRC:08x}'})
    for row in pres:assert z.read('manuscript/'+row['path'])==(ROOT/row['path']).read_bytes()
    assert z.read('manuscript/'+NAME)==pdf
    with zipfile.ZipFile(io.BytesIO(z.read('manuscript/archives/'+acc.name))) as nested:
        assert len(safe(nested))==175
        for n in nested.namelist():assert nested.read(n)==z.read('manuscript/evidence/outer_envelope/'+n)
zipsha=sha(zp.read_bytes());side=zp.with_name(zp.name+'.sha256');side.write_text(zipsha+'  '+zp.name+'\n',encoding='ascii',newline='\n')
audit={'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'archive':str(zp),'archive_bytes':zp.stat().st_size,'archive_sha256':zipsha,'archive_root':'manuscript/','member_count':len(members),'manifest_entries':len(files),'safe_unique_case_unique_paths':True,'all_members_crc_bytes_sha256_pass':True,'every_archived_byte_matches_staging':True,'preserved_incoming_files':187,'acceptance_extraction_members':175,'original_investigation_members':143,'source_identity_records':24,'new_document_links_checked':len(links),'claims_mapped':4,'pages_inspected':12,'pdf_sha256':pdfsha,'pdf_bytes':len(pdf),'pdf_identity':{'standalone':str(Path(a.standalone_pdf).resolve()),'built':str(Path(a.built_pdf).resolve()),'staging':str(ROOT/NAME),'archived':'manuscript/'+NAME,'inspection_record':'manuscript/verification/VISUAL_INSPECTION.json','all_same_bytes':True},'publication':False,'new_scientific_runs':0,'repository_operations':0,'members':members}
write(out/'FINAL_ARCHIVE_AUDIT.json',audit)
assert side.read_text().split()[0]==sha(zp.read_bytes())
print(json.dumps({k:v for k,v in audit.items() if k not in ['members','pdf_identity']},indent=2))
