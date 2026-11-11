"""Document-only PDF, TeX, reference, font, link and input-byte verification."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];V=R/'verification'
p=argparse.ArgumentParser();p.add_argument('--build-dir',required=True);a=p.parse_args();B=Path(a.build_dir)
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and sys.flags.optimize==0
def sha(b):return hashlib.sha256(b).hexdigest()
def write(path,o):path.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pdf=R/'NATIVE_TURNING_CAPTURE_COMPANION_v0.1.pdf';reader=PdfReader(pdf)
main=(R/'main.tex').read_text(encoding='utf-8');refs=(R/'references.tex').read_text(encoding='utf-8');source=main+'\n'+refs
aux=(B/'main.aux').read_text(encoding='utf-8');log=(B/'main.log').read_text(encoding='utf-8');compiler=(B/'compiler.txt').read_text(encoding='utf-8')
labels={m.group(1):{'number':m.group(2),'page':int(m.group(3))} for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
defined=re.findall(r'\\label\{([^}]+)\}',source+(R/'tables/terminal_bounds.tex').read_text())
assert len(defined)==len(set(defined)) and all(x in labels for x in defined)
used=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
assert set(used)<=set(labels)
cites=set(k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',source) for k in group.split(','))
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',refs));resolved=set(re.findall(r'\\bibcite\{([^}]+)\}',aux))
assert cites<=bibs==resolved
warnings=[line for line in (log+'\n'+compiler).splitlines() if re.search(r'^LaTeX Warning:|^Package .* Warning:|^Class .* Warning:|^Overfull|^Underfull|^Missing character|^!|^warning:',line,re.I)]
assert not warnings,warnings
pages=[page.extract_text() for page in reader.pages]
assert 6<=len(pages)<=9 and all('??' not in t for t in pages)
assert 'project-internal manuscript review complete' in ' '.join(pages[0].lower().split())
assert 'Research edition v0.1' in str(reader.metadata.subject)
assert reader.metadata.title=='Certified Capture of the Collective-Turning Trajectory in the Native Triad'
assert reader.metadata.author=='Hilmir Frímann Halldórsson (pzychozen)'
assert 'project-internal manuscript review complete' in reader.metadata.subject and 'author-authorized for repository publication' in reader.metadata.subject
font_records={}
for page in reader.pages:
    for tag,ref in page['/Resources'].get('/Font',{}).items():
        obj=ref.get_object(); descendants=obj.get('/DescendantFonts') or [obj]
        for sub in descendants:
            sub=sub.get_object();name=str(sub.get('/BaseFont',obj.get('/BaseFont')))
            descriptor=sub.get('/FontDescriptor')
            assert descriptor is not None,(tag,name)
            descriptor=descriptor.get_object();programs=[]
            for key in ['/FontFile','/FontFile2','/FontFile3']:
                if key in descriptor:
                    data=descriptor[key].get_object().get_data();assert len(data)>0
                    programs.append({'field':key,'decoded_bytes':len(data)})
            assert programs,(tag,name)
            font_records[name]={'base_font':name,'subtype':str(sub.get('/Subtype')),'embedded':True,'programs':programs,'to_unicode':bool(obj.get('/ToUnicode'))}
links=[]
for target in re.findall(r'\\href\{([^}]+)\}',source):
    assert '://' not in target and not Path(target).is_absolute(),target
    exists=(R/target).is_file();assert exists,target
    links.append({'relative_target':target,'exists':exists})
inputs=json.loads((R/'PRESERVED_INPUTS.json').read_text())['files']
for item in inputs:
    b=(R/item['path']).read_bytes();assert len(b)==item['bytes'] and sha(b)==item['sha256'],item['path']
assert F('1.07701')*F(1,4)**2/F(8)==F(107701,12800000)
assert F('1.1')*F(1,4)==F(11,40)
for token in [r'\frac15\beta^j',r'\frac{107701}{12800000}',r'\frac{11}{40}c^j',r'c=1-\frac{3\sqrt2}{200}',r'\beta=\frac{8571}{10000}']:
    assert token in main,token
for label,phrase in [('eq:turn','0.0110760731'),('eq:cone',r'\frac\pi{12}'),('eq:neighborhood',r'(F^{50}|_V)^{-1}(O)')]:
    assert label in labels and phrase in main
(V/'FINAL_PDF_TEXT.txt').write_text('\n\n'.join('PAGE '+str(i+1)+'\n'+s for i,s in enumerate(pages)),encoding='utf-8')
write(V/'REFERENCE_MAP.json',{'labels':labels,'references_used':used,'citations':sorted(cites),'bibliography_keys':sorted(bibs),'unresolved_references':[],'unresolved_citations':[]})
write(V/'FONT_EMBEDDING.json',{'pdf_sha256':sha(pdf.read_bytes()),'all_fonts_embedded':True,'fonts':list(font_records.values()),'font_files_distributed_separately':False})
write(V/'DOCUMENT_CHECKS.json',{'kind':'Document verification, not scientific replay','status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'command':[sys.executable,*sys.argv],'conda_environment':os.environ['CONDA_DEFAULT_ENV'],'pdf_sha256':sha(pdf.read_bytes()),'pdf_pages':len(pages),'source_hashes':{name:sha((R/name).read_bytes()) for name in ['main.tex','references.tex','tables/terminal_bounds.tex']},'metadata':dict(reader.metadata),'labels_resolved':len(labels),'citations_resolved':len(cites),'compiler_warnings':warnings,'font_count':len(font_records),'all_fonts_embedded':True,'relative_links':links,'preserved_files_unchanged':len(inputs),'tail_coefficient_transcription':'PASS; exact rational comparison against accepted expression','visual_inspection':'Pending separate page-by-page record','scientific_executions':0})
for src,dest in [('BUILD_RECEIPT.json','BUILD_RECEIPT.json'),('compiler.txt','COMPILER_MESSAGES.txt'),('main.log','TEX_LOG.txt')]:shutil.copyfile(B/src,V/dest)
images=V/'pages';images.mkdir(exist_ok=True)
renderer=shutil.which('pdftoppm');assert renderer
cmd=[renderer,'-r','145','-png',str(pdf),str(images/'page')]
start=datetime.now(timezone.utc).isoformat();run=subprocess.run(cmd,capture_output=True)
write(V/'RENDER_RECORD.json',{'command':cmd,'started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'exit_status':run.returncode,'stdout':run.stdout.decode(errors='replace'),'stderr':run.stderr.decode(errors='replace'),'pdf_sha256':sha(pdf.read_bytes()),'dpi':145})
assert run.returncode==0
pngs=sorted(images.glob('page-*.png'));assert len(pngs)==len(pages)
print(json.dumps({'status':'PASS','pages':len(pages),'font_count':len(font_records),'labels':len(labels),'citations':len(cites),'warnings':warnings,'preserved_files':len(inputs),'rendered_pages':len(pngs)},indent=2))
for i,t in enumerate(pages,1):print('PAGE',i,'START:',t[:85].replace('\n',' '),'END:',t[-100:].replace('\n',' '))
