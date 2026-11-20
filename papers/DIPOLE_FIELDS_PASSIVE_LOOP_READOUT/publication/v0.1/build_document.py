"""Build and render the editable LaTeX manuscript on Windows in conda torment."""
from pathlib import Path
import subprocess,shutil,json,hashlib,datetime,os,platform,sys,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(ROOT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n','utf-8')
build=ROOT/'build';out=build/'tex';out.mkdir(parents=True,exist_ok=True)
attempt='attempt_%02d'%(len(list(build.glob('attempt_*.json')))+1)
cache=build/'fontcache';cache.mkdir(exist_ok=True)
fc=build/'fonts.conf'
fc.write_text('<?xml version="1.0"?>\n<fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+
              cache.as_posix()+'</cachedir></fontconfig>\n','utf-8')
env=os.environ.copy()
env.update(FONTCONFIG_FILE=str(fc),FONTCONFIG_PATH=str(build),
           SOURCE_DATE_EPOCH=str(int(datetime.datetime(2026,11,20,tzinfo=datetime.timezone.utc).timestamp())))
exe=shutil.which('tectonic');assert exe
command=[exe]+([] if '--fetch-deps' in sys.argv else ['--only-cached'])+['--untrusted','--keep-logs','--keep-intermediates','--outdir',str(out),str(ROOT/'manuscript/main.tex')]
proc=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
(build/(attempt+'.stdout.txt')).write_text(proc.stdout,'utf-8')
(build/(attempt+'.stderr.txt')).write_text(proc.stderr,'utf-8')
record=dict(command=command,returncode=proc.returncode,python=sys.version,platform=platform.platform(),
    conda=os.environ['CONDA_DEFAULT_ENV'],source_date_epoch=env['SOURCE_DATE_EPOCH'],
    engine_version=subprocess.check_output([exe,'--version'],text=True).strip(),
    sources={p.relative_to(ROOT).as_posix():sha(p) for p in (ROOT/'manuscript').rglob('*.tex')})
if (out/'main.log').exists():shutil.copyfile(out/'main.log',build/(attempt+'.tex.log'))
if proc.returncode:
    save('build/'+attempt+'.json',record);save('BUILD_RECORD.json',record)
    print(proc.stdout[-3500:]);print(proc.stderr[-3500:]);sys.exit(proc.returncode)
pdf=ROOT/'output/pdf/GM04_GM06_COMBINED_PAPER_v0.1.pdf'
pdf.parent.mkdir(parents=True,exist_ok=True)
shutil.copyfile(out/'main.pdf',pdf)
record.update(pdf=pdf.relative_to(ROOT).as_posix(),pdf_sha256=sha(pdf))
save('build/'+attempt+'.json',record);save('BUILD_RECORD.json',record)
log=(out/'main.log').read_text('utf-8')
warnings=[x for x in log.splitlines() if any(w in x for w in ['Overfull','Underfull','undefined','Missing character','multiply defined','LaTeX Error'])]
alltex='\n'.join(p.read_text('utf-8') for p in (ROOT/'manuscript').rglob('*.tex'))
labels=re.findall(r'\\label\{([^}]+)\}',alltex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',alltex)
cites=[c.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',alltex) for c in group.split(',')]
bibs=re.findall(r'\\bibitem\{([^}]+)\}',alltex)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
assert len(bibs)==len(set(bibs)) and set(cites)<=set(bibs)
aux=(out/'main.aux').read_text('utf-8')
assert all('\\newlabel{'+x+'}' in aux for x in labels)
assert all('\\bibcite{'+x+'}' in aux for x in bibs)
reader=PdfReader(pdf);texts=[];fonts={}
for page in reader.pages:
    texts.append(page.extract_text())
    for obj in page['/Resources'].get('/Font',{}).values():
        font=obj.get_object()
        for f in font.get('/DescendantFonts',[font]):
            f=f.get_object();desc=f.get('/FontDescriptor')
            assert desc
            desc=desc.get_object()
            assert any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
            fonts[str(f['/BaseFont'])]=dict(embedded=True,subtype=str(f['/Subtype']))
assert all(t.strip() for t in texts) and '??' not in '\n'.join(texts)
(build/'PDF_TEXT.txt').write_text('\n\n--- PAGE ---\n\n'.join(texts),'utf-8')
for i,t in enumerate(texts,1):(build/('page_%02d.txt'%i)).write_text(t,'utf-8')
for tool in ['pdfinfo','pdffonts']:
    path=shutil.which(tool)
    if path:
        p=subprocess.run([path,str(pdf)],capture_output=True,text=True,encoding='utf-8',errors='replace',check=True)
        (build/(tool+'.txt')).write_text(p.stdout,'utf-8')
renderdir=ROOT/'inspection'/attempt;renderdir.mkdir(parents=True,exist_ok=True)
render=[shutil.which('pdftoppm'),'-r','120','-png',str(pdf),str(renderdir/'page')]
p=subprocess.run(render,capture_output=True,text=True,check=True)
pages=sorted(renderdir.glob('page-*.png'));assert len(pages)==len(reader.pages)
doc=dict(status='PASS' if not warnings else 'LAYOUT_WARNINGS',pdf_sha256=sha(pdf),pages=len(reader.pages),
    labels=len(labels),references=len(refs),citations=len(cites),bibliography_entries=len(bibs),
    metadata={str(k):str(v) for k,v in reader.metadata.items()},fonts=fonts,warnings=warnings,
    render_command=render,rendered_pages=[dict(page=i,path=p.relative_to(ROOT).as_posix(),sha256=sha(p)) for i,p in enumerate(pages,1)],
    visual_inspection='Pending actual image inspection; see VISUAL_INSPECTION.json.')
save('DOCUMENT_VERIFICATION.json',doc)
print(json.dumps(dict(attempt=attempt,status=doc['status'],pages=doc['pages'],warnings=warnings,
                     labels=len(labels),fonts=len(fonts),pdf_sha256=sha(pdf)),indent=2))
