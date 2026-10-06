"""Check source links, rendered PDF structure, evidence and protected identities."""
from pathlib import Path
from pypdf import PdfReader
import pdfplumber
import re,json,hashlib,csv,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source='\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT/'source').glob('*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',source)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
assert len(labels)==len(set(labels)),'Duplicate labels'
assert not set(refs)-set(labels),set(refs)-set(labels)
keys=re.findall(r'\\bibitem\{([^}]+)\}',source)
bibkeys=re.findall(r'@\w+\{([^,]+),',(ROOT/'bibliography.bib').read_text())
assert set(keys)==set(bibkeys)
cites=[x for g in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',source) for x in g.split(',')]
assert not set(cites)-set(keys)
figs=re.findall(r'\\fig\{([^}]+)\}',source);assert len(figs)==5
for name in figs:
    for ext in ['pdf','svg','png']:assert (ROOT/'figures'/f'{name}.{ext}').is_file()
log=(ROOT/'records/latex_build.log').read_text(encoding='utf-8',errors='replace')
for bad in ['Overfull','Missing character','undefined references','undefined on input','multiply defined']:
    assert bad not in log,bad
pdf=ROOT/'output/pdf/three_way_reciprocal_hierarchy_v0.1.pdf';reader=PdfReader(pdf)
page_text=[pg.extract_text() or '' for pg in reader.pages];text='\n'.join(page_text)
assert '\ufffd' not in text and '??' not in text
assert all(len(t)>100 for t in page_text),'Blank or image-only page'
destinations=reader.named_destinations;broken=[];internal=0;external=set()
assert all(0<=reader.get_destination_page_number(d)<len(reader.pages) for d in destinations.values()),'Invalid named destination page'
for pg in reader.pages:
    for a in pg.get('/Annots',[]):
        obj=a.get_object();act=obj.get('/A',{});dest=obj.get('/Dest')
        if act.get('/S')=='/URI':external.add(str(act.get('/URI')))
        if act.get('/S')=='/GoTo':dest=act.get('/D')
        if dest is not None:
            internal+=1
            if isinstance(dest,str) and dest not in destinations:broken.append(dest)
assert not broken,broken
baseline=json.loads((ROOT/'records/baseline.json').read_text())
changed=[p for p,h in baseline['files'].items() if (sha(Path(p)) if Path(p).is_file() else None)!=h]
assert not changed,changed
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
status=subprocess.check_output(['git','status','--short'],cwd=REPO,text=True)
assert head==baseline['head'],'HEAD changed'
assert status==baseline['status'],dict(before=baseline['status'],after=status)
manifest=json.loads((ROOT/'provenance/source_manifest.json').read_text())
for i in manifest:
    assert sha(Path(i['original']))==i['sha256'],i['id']+' original changed'
    assert sha(ROOT/i['snapshot'])==i['sha256'],i['id']+' snapshot changed'
results=[]
for rel in ['hierarchy/verification_results.json','cubic/verification_results.json','bridge_results.json']:
    d=json.loads((ROOT/'verification'/rel).read_text());assert all(c['passed'] for c in d['checks']);results.append(d['exact_checks'])
assert results==[51,73,10],results
build=json.loads((ROOT/'records/build_record.json').read_text())
assert sha(pdf)==build['pdf_sha256'],'PDF differs from recorded build'
for rel,h in build['inputs'].items():assert sha(ROOT/rel)==h,('Source changed since PDF build',rel)
claims=list(csv.DictReader((ROOT/'provenance/claim_ledger.csv').open(encoding='utf-8-sig')))
assert all(c['manuscript_label'] in labels for c in claims)
theorems=re.findall(r'\\begin\{(?:theorem|proposition|lemma|corollary)\}(?:\[[^]]*\])?\s*\\label\{([^}]+)\}',source)
assert not set(theorems)-{c['manuscript_label'] for c in claims},'Theorem omitted from claim ledger'
# Record page content extents for layout review; do not infer visual correctness from extraction.
extents=[]
with pdfplumber.open(pdf) as doc:
    for i,p in enumerate(doc.pages,1):
        chars=[c for c in p.chars if c['text'].strip()]
        extents.append(dict(page=i,left=min(c['x0'] for c in chars),right=max(c['x1'] for c in chars),top=min(c['top'] for c in chars),bottom=max(c['bottom'] for c in chars)))
        assert min(c['x0'] for c in chars)>10 and max(c['x1'] for c in chars)<p.width-10,('Outside page bounds',i)
audit=dict(pages=len(reader.pages),pdf_sha256=sha(pdf),source_labels=len(labels),source_references=len(refs),bibliography_entries=len(keys),citations_resolved=True,internal_pdf_links=internal,broken_internal_links=broken,external_urls=sorted(external),figures=len(figs),exact_checks=sum(results),suite_counts=results,claim_records=len(claims),theorems_mapped=len(theorems),protected_files_checked=len(baseline['files']),protected_files_changed=changed,source_snapshots_checked=len(manifest),head_unchanged=True,git_status_unchanged_since_paperII_baseline=True,build_inputs_unchanged_since_compile=True,underfull_box_warnings=log.count('Underfull'),overfull_boxes=0,missing_glyphs=0,page_text_extents=extents)
(ROOT/'records/delivery_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
(ROOT/'records/pdf_text.txt').write_text(text,encoding='utf-8')
print(json.dumps({k:v for k,v in audit.items() if k!='page_text_extents'},indent=2))
