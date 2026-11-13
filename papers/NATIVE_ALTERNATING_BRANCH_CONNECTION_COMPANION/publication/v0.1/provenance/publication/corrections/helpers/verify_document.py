"""Document-only checks: PDF text, fonts, labels, citations, relative links."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, os, re, sys
from urllib.parse import unquote
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--build-dir',required=True);a=p.parse_args();B=Path(a.build_dir)
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
V=ROOT/'verification';V.mkdir(exist_ok=True)
NAME='NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION_v0.1.pdf';PDF=ROOT/NAME
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,obj):(V/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
reader=PdfReader(PDF);N=len(reader.pages);texts=[page.extract_text() for page in reader.pages]
assert all(len(t.strip())>100 for t in texts)
assert all('??' not in t and '\ufffd' not in t for t in texts)
(V/'EXTRACTED_TEXT.txt').write_text('\n\n'.join('=== PAGE '+str(i+1)+' ===\n'+t for i,t in enumerate(texts)),encoding='utf-8')
fonts={}
def checkfont(ref):
    f=ref.get_object();name=str(f.get('/BaseFont'));subtype=str(f.get('/Subtype'))
    if '/DescendantFonts' in f:
        for child in f['/DescendantFonts']:checkfont(child)
        return
    d=f.get('/FontDescriptor');d=d.get_object() if d is not None else {}
    streams=[k for k in ['/FontFile','/FontFile2','/FontFile3'] if k in d]
    assert streams,(name,subtype,'not embedded')
    fonts[name]={'subtype':subtype,'embedded_streams':{k:{'decoded_bytes':len(d[k].get_data()),'sha256':sha(d[k].get_data())} for k in streams}}
for page in reader.pages:
    for f in page['/Resources'].get_object().get('/Font',{}).get_object().values():checkfont(f)
aux=(B/'main.aux').read_text(encoding='utf-8');log=(B/'main.log').read_text(encoding='utf-8')
labels={key:{'number':number,'page':int(page)} for key,number,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
bib=dict(re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}',aux))
sources={name:(ROOT/name).read_text(encoding='utf-8') for name in ['main.tex','references.tex','tables/certificate.tex']}
allsource='\n'.join(sources.values())
refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',allsource)
cites=[x.strip() for group in re.findall(r'\\cite\{([^}]+)\}',allsource) for x in group.split(',')]
assert set(refs)<=set(labels) and set(cites)<=set(bib)
assert all(1<=rec['page']<=N for rec in labels.values())
assert len(bib)==6
bad_patterns=[r'Overfull \\[hv]box',r'Underfull \\[hv]box',r'undefined',r'Missing character:',r'LaTeX Font Warning:',r'There were undefined',r'Label\(s\) may have changed']
failures=[pat for pat in bad_patterns if re.search(pat,log,re.I)]
assert not failures,failures
links=[]
for link in re.findall(r'\\href\{([^}]+)\}',allsource):
    assert '://' not in link,'All references are supplied local evidence.'
    target=(ROOT/unquote(link)).resolve();assert target.is_relative_to(ROOT) and target.is_file(),link
    links.append({'target':link,'bytes':target.stat().st_size,'sha256':sha(target.read_bytes())})
pdf_links=[];destinations=reader.named_destinations
for i,page in enumerate(reader.pages,1):
    for ann in page.get('/Annots',[]):
        ann=ann.get_object()
        if ann.get('/Subtype')!='/Link':continue
        action=ann.get('/A',{});action=action.get_object() if hasattr(action,'get_object') else action
        dest=ann.get('/Dest',action.get('/D'))
        kind=str(action.get('/S','direct-destination'))
        if kind in ['/GoTo','direct-destination'] and isinstance(dest,str):assert dest in destinations,(i,dest)
        if kind=='/URI':
            uri=str(action['/URI']);assert '://' not in uri,uri
            assert (ROOT/unquote(uri)).is_file(),uri
        if kind=='/GoToR':
            f=action.get('/F');f=f.get_object() if hasattr(f,'get_object') else f
            target=f.get('/F') if isinstance(f,dict) else str(f)
            assert (ROOT/target).is_file(),target
        pdf_links.append({'page':i,'action':kind,'destination':str(dest)})
metadata={str(k):str(v) for k,v in reader.metadata.items()}
assert metadata['/Title']=='Certified Connection from Local Period-Doubling to the Captured Alternating Cycle in the Native Triad'
assert metadata['/Author']=='Hilmir Frímann Halldórsson (pzychozen)'
assert 'pending' in metadata['/Subject'] and 'v0.1' in metadata['/Subject']
base={'status':'PASS','recorded_utc':datetime.now(timezone.utc).isoformat(),'pdf_sha256':sha(PDF.read_bytes()),'pdf_bytes':PDF.stat().st_size,'page_count':N,'scientific_runs':0}
save('FONT_CHECK.json',dict(base,method='pypdf inspection of every page font and descendant FontDescriptor; nonempty embedded font streams required',fonts=fonts))
save('REFERENCE_CHECK.json',dict(base,labels=labels,bibliography=bib,referenced_labels=sorted(set(refs)),cited_keys=sorted(set(cites)),source_links=links,pdf_link_annotations=pdf_links,final_log_warning_failures=failures))
save('DOCUMENT_CHECK.json',dict(base,metadata=metadata,selectable_text_characters_by_page=list(map(len,texts)),embedded_fonts=len(fonts),named_destinations=len(destinations),warning_lines=[line for line in log.splitlines() if 'warning' in line.lower()],source_hashes={n:sha((ROOT/n).read_bytes()) for n in sources},source_hash_basis='SHA-256 of raw file bytes',helper_sha256=sha(Path(__file__).read_bytes()),inspection='Visual inspection is a separate record; not inferred from these automatic checks.'))
print(json.dumps({'status':'PASS','pages':N,'fonts':len(fonts),'labels':len(labels),'bibliography':len(bib),'local_source_links':len(links),'pdf_link_annotations':len(pdf_links),'metadata':metadata},ensure_ascii=False))
