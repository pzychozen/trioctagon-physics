"""Document verification and individual-page rendering, not a scientific rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, subprocess, sys
import pypdf
ROOT=Path(__file__).resolve().parents[1]
E=ROOT/'candidate/v0.1'; V=ROOT/'verification'
BUILD=V/sys.argv[1] if len(sys.argv)>1 else V/'publication_build01'
PDF=E/'SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf'
POP=Path(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin')
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,data): (V/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
reader=pypdf.PdfReader(PDF)
pages=[p.extract_text() or '' for p in reader.pages]
(V/'EXTRACTED_TEXT.txt').write_text('\n\n'.join(f'===== PAGE {i} =====\n{t}' for i,t in enumerate(pages,1)),encoding='utf-8')
fonts={}
def inspect_resources(res):
    res=res.get_object()
    for key,ref in res.get('/Font',{}).items():
        font=ref.get_object()
        for item in font.get('/DescendantFonts',[font]):
            f=item.get_object(); desc=f.get('/FontDescriptor'); desc=desc.get_object() if desc else {}
            name=str(f.get('/BaseFont',font.get('/BaseFont',key)))
            fonts[name]={'embedded':any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3']),
                'subtype':str(f.get('/Subtype'))}
    for ref in res.get('/XObject',{}).values():
        obj=ref.get_object()
        if '/Resources' in obj:inspect_resources(obj['/Resources'])
for p in reader.pages:inspect_resources(p['/Resources'])
log=(BUILD/'main.log').read_text(encoding='utf-8',errors='replace')
patterns=[r'Overfull',r'Missing character',r'undefined references',r'Citation .* undefined',r'Reference .* undefined',r'multiply defined',r'Font shape .* undefined',r'LaTeX Font Warning']
issues=[m.group(0) for pat in patterns for m in re.finditer(pat,log,re.I)]
aux=(BUILD/'main.aux').read_text(encoding='utf-8')
labels={m[0]:{'number':m[1],'page':int(m[2])} for m in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
files=sorted(E.rglob('*.tex'))
tex='\n'.join(p.read_text(encoding='utf-8') for p in files)
refs=set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex))
cites={k for group in re.findall(r'\\cite\{([^}]+)\}',tex) for k in group.split(',')}
bib=set(re.findall(r'\\bibitem\{([^}]+)\}',tex))
assert not refs-labels.keys(),refs-labels.keys()
assert not cites-bib,cites-bib
assert not issues,issues
assert all(f['embedded'] for f in fonts.values()),fonts
assert all(len(t.strip())>100 for t in pages)
assert '\ufffd' not in '\n'.join(pages)
assert reader.metadata.title=='Spatial Observation and Causal Transport with Storage in the Reciprocal Chiral Exchange Candidate'
assert reader.metadata.author=='Hilmir Frímann Halldórsson (pzychozen)'
assert reader.metadata.subject=='Research edition v0.1 — project-internal review complete; author-authorized for repository publication.'
assert '10 November 2026' in pages[0]
assert 'manuscript and author review pending' not in '\n'.join(pages).lower()
assert 'author-authorized' in pages[0].lower()
assert 'project-internal review complete' in pages[0].lower()
assert len(pages)==25
assert len(labels)==118
assert len(cites)==12
receipt=json.loads((BUILD/'BUILD_RECEIPT.json').read_text())
assert receipt['pdf_sha256']==sha(PDF)
for name,h in receipt['content'].items(): assert sha(E/name)==h,name
versions={}
for name in ['pdfinfo','pdftoppm']:
    run=subprocess.run([str(POP/f'{name}.exe'),'-v'],capture_output=True,text=True,check=True)
    versions[name]=(run.stdout+run.stderr).strip()
for name in ['pdfinfo']:
    run=subprocess.run([str(POP/f'{name}.exe'),str(PDF)],capture_output=True,text=True,encoding='utf-8',check=True)
    (V/(name.upper()+'.txt')).write_text(run.stdout+run.stderr,encoding='utf-8')
(V/'EXTRACTED_LAYOUT.txt').write_text('\n\n'.join(f'===== PAGE {i} =====\n'+p.extract_text(extraction_mode='layout') for i,p in enumerate(reader.pages,1)),encoding='utf-8')
renderdir=V/'pages'; renderdir.mkdir(exist_ok=True)
cmd=[str(POP/'pdftoppm.exe'),'-png','-r','125',str(PDF),str(renderdir/'page')]
start=datetime.now(timezone.utc).isoformat()
run=subprocess.run(cmd,capture_output=True,text=True,check=True)
(V/'RENDER_LOG.txt').write_text(run.stdout+run.stderr,encoding='utf-8')
images=sorted(renderdir.glob('page-*.png')); assert len(images)==len(pages)
record={'checked_utc':datetime.now(timezone.utc).isoformat(),'python':sys.executable,'python_version':sys.version,
 'pypdf':pypdf.__version__,'pdf_sha256':sha(PDF),'pdf_bytes':PDF.stat().st_size,'pages':len(pages),
 'metadata':dict(reader.metadata),'fonts':fonts,'all_fonts_embedded':True,'source_build_hashes_match':True,
 'undefined_refs_citations':False,'overfull_missing_glyph_font_warnings':issues,
 'underfull_warnings':re.findall(r'Underfull[^\n]*',log),'labels':labels,
 'all_reference_labels_resolved':True,'all_citations_resolved':True,'citation_keys':sorted(cites),
 'page_text_lengths':[len(t) for t in pages],'replacement_characters':False,'tool_versions':versions,
 'render_command':cmd,'render_dpi':125,'render_started_utc':start,'rendered_pages':{p.name:sha(p) for p in images},
 'visual_inspection':'Pending separate final VISUAL_INSPECTION.json; rendering alone is not inspection.',
 'build_directory':BUILD.relative_to(ROOT).as_posix()}
write('DOCUMENT_CHECKS.json',record)
print(json.dumps({'pages':len(pages),'pdf_sha256':sha(PDF),'fonts':len(fonts),'all_fonts_embedded':True,
 'labels':len(labels),'rendered_pages':len(images),'underfull_warnings':record['underfull_warnings']},indent=2))
