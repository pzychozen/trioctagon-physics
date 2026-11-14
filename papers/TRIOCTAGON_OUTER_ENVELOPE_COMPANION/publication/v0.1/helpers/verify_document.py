"""Document checks only. Does not import or execute scientific evidence code."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,re,shutil,subprocess,sys
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification';NAME='TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf'
ap=argparse.ArgumentParser();ap.add_argument('--build-dir',required=True);ap.add_argument('--render',action='store_true');args=ap.parse_args();B=Path(args.build_dir).resolve()
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat();pdf=ROOT/NAME;pdfsha=sha(pdf);receipt=read(B/'BUILD_RECEIPT.json')
assert receipt['exit_status']==0 and receipt['pdf_sha256']==pdfsha==sha(B/'main.pdf')
for p,h in receipt['raw_source_hashes'].items():assert sha(ROOT/p)==h,p
log=(B/'main.log').read_text(encoding='utf-8',errors='replace');stderr=(B/'compiler.stderr').read_text(encoding='utf-8',errors='replace')
issues=re.findall(r'^.*(?:Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning|undefined references|undefined citations|warning:).*$' ,log+'\n'+stderr,re.M)
assert not issues,issues
reader=PdfReader(pdf);pages=[];fonts={};destinations=reader.named_destinations;links=0
def scan_resources(resource):
    for obj in resource.get('/Font',{}).get_object().values() if resource.get('/Font') else []:
        f=obj.get_object();name=str(f.get('/BaseFont'));fs=f.get('/DescendantFonts',[f]);embedded=[]
        for item in fs:
            item=item.get_object();d=item.get('/FontDescriptor');d=d.get_object() if d else {}
            embedded.append(any(k in d for k in ['/FontFile','/FontFile2','/FontFile3']))
        assert all(embedded),name
        fonts[name]={'subtype':str(f.get('/Subtype')),'embedded':True,'to_unicode':bool(f.get('/ToUnicode'))}
    if resource.get('/XObject'):
        for ob in resource['/XObject'].get_object().values():
            ob=ob.get_object()
            if ob.get('/Resources'):scan_resources(ob['/Resources'].get_object())
for i,p in enumerate(reader.pages,1):
    text=p.extract_text();assert len(text)>500 and '\ufffd' not in text and '??' not in text,(i,len(text))
    assert text.rstrip().endswith(str(i)),(i,'page number')
    pages.append({'page':i,'characters':len(text),'text':text})
    scan_resources(p['/Resources'].get_object())
    for item in p.get('/Annots',[]):
        a=item.get_object();d=a.get('/Dest');action=a.get('/A')
        if action:
            action=action.get_object()
            if action.get('/S')=='/GoTo':d=action.get('/D')
        if d is not None:
            assert not isinstance(d,str) or d in destinations,(i,d)
            links+=1
meta={str(k):str(v) for k,v in reader.metadata.items()}
assert meta['/Title']=='Noncollision Facet Transition and Exact Outer-Envelope Classification in the Folded Tri-Octagon'
assert meta['/Author']=='Hilmir Frímann Halldórsson' and meta['/Subject']=='Research edition v0.1; project-internal manuscript review complete; author-authorized for repository publication; not externally peer reviewed.'
aux=(B/'main.aux').read_text(encoding='utf-8');labels={k:{'number':n,'pdf_page':int(p)} for k,n,p in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
sources=[ROOT/'main.tex',ROOT/'references.tex',*sorted((ROOT/'tables').glob('*.tex'))];tex='\n'.join(p.read_text(encoding='utf-8') for p in sources)
declared=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',tex);bib=re.findall(r'\\bibitem\{([^}]+)\}',tex);cites=[k.strip() for c in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex) for k in c.split(',')]
assert len(declared)==len(set(declared)) and set(declared)==set(labels)
assert set(refs)<=set(labels) and set(cites)<=set(bib) and len(bib)==len(set(bib))==4
assert all(1<=v['pdf_page']<=len(pages) for v in labels.values())
write(V/'LABELS.json',labels)
write(V/'REFERENCE_CHECK.json',{'status':'PASS','pdf_sha256':pdfsha,'labels':len(labels),'reference_uses':len(refs),'citation_uses':len(cites),'bibliography_keys':bib,'resolved_pdf_internal_links':links,'unresolved':[]})
write(V/'FONT_CHECK.json',{'status':'PASS','pdf_sha256':pdfsha,'fonts':fonts,'all_embedded':True,'note':'ToUnicode presence is reported, not used alone as a text-quality assertion; text extraction and visual inspection are separate.'})
write(V/'EXTRACTED_TEXT.json',{'pdf_sha256':pdfsha,'pages':pages})
pres=read(ROOT/'PRESERVED_INPUTS.json')['files']
for row in pres:assert (ROOT/row['path']).stat().st_size==row['bytes'] and sha(ROOT/row['path'])==row['sha256'],row['path']
for ext in ['png','svg']:assert sha(ROOT/f'figures/local_facet_transition.{ext}')==sha(ROOT/f'evidence/outer_envelope/submitted/figures/local_facet_transition.{ext}')
write(V/'FIGURE_EMBEDDING.json',{'status':'PASS','method':'LaTeX clipping of unchanged PNG; three source panels arranged vertically. No geometry generation or source image mutation.','source_png_sha256':sha(ROOT/'figures/local_facet_transition.png'),'source_svg_sha256':sha(ROOT/'figures/local_facet_transition.svg'),'source_pixels':[2550,918],'embed_width_mm':96,'trim_bp_left_bottom_right_top':[[76.235,134.682,792,127.059],[436.235,134.682,432,127.059],[796.235,134.682,72,127.059]],'pdf_sha256':pdfsha})
out=V/'final_build';out.mkdir(exist_ok=True)
for name in ['BUILD_RECEIPT.json','compiler.stdout','compiler.stderr','main.log']:shutil.copyfile(B/name,out/name)
write(V/'DOCUMENT_CHECK.json',{'status':'PASS','checked_utc':stamp,'pdf':NAME,'pdf_sha256':pdfsha,'pdf_bytes':pdf.stat().st_size,'page_count':len(pages),'metadata':meta,'all_pages_have_selectable_text':True,'all_page_numbers_present':True,'embedded_fonts':len(fonts),'compiler_warnings':issues,'preserved_input_count':len(pres),'source_hashes_match_final_build':True,'new_scientific_runs':0,'visual_inspection':'Separate page-specific record required after rendering.'})
if args.render:
    out=V/'pages';out.mkdir(exist_ok=True);cmd=['pdftoppm','-r','145','-png',str(pdf),str(out/'page')]
    q=subprocess.run(cmd,capture_output=True,timeout=240);(V/'render.stdout').write_bytes(q.stdout);(V/'render.stderr').write_bytes(q.stderr);assert q.returncode==0
    images=sorted(out.glob('page-*.png'));assert len(images)==len(pages)
    write(V/'RENDER_RECORD.json',{'status':'PASS','pdf_sha256':pdfsha,'command':cmd,'exit_status':q.returncode,'dpi':145,'pages':[{'page':i,'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for i,p in enumerate(images,1)]})
print(json.dumps({'document':'PASS','pages':len(pages),'fonts_embedded':len(fonts),'labels':len(labels),'internal_links':links,'pdf_sha256':pdfsha}))
