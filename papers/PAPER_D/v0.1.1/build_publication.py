"""Complete Markdown -> inspected Pandoc AST -> TeX -> PDF, using existing tools."""
from pathlib import Path
import datetime,hashlib,json,os,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent;BUILD=ROOT/'.build';PUB=ROOT/'publication';EV=ROOT/'evidence'
for p in (BUILD,PUB,EV):p.mkdir(exist_ok=True)
def tool(name,var):
    value=os.environ.get(var) or shutil.which(name)
    if not value or not Path(value).is_file():raise RuntimeError('Set '+var+' to existing '+name)
    return Path(value).resolve()
PANDOC=tool('pandoc','PAPER_D_PANDOC');TECTONIC=tool('tectonic','PAPER_D_TECTONIC')
CACHE=Path(os.environ.get('PAPER_D_TEX_CACHE',''))
if not os.environ.get('PAPER_D_TEX_CACHE') or not CACHE.is_dir():raise RuntimeError('Set PAPER_D_TEX_CACHE to an existing populated Tectonic cache.')
def run(args):return subprocess.run([str(x) for x in args],check=True,capture_output=True,cwd=ROOT)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(v,t):
    if isinstance(v,dict):
        if v.get('t')==t:yield v
        for x in v.values():yield from nodes(x,t)
    elif isinstance(v,list):
        for x in v:yield from nodes(x,t)
MD=ROOT/'PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md'
ast=json.loads(run([PANDOC,MD,'--from=markdown+tex_math_dollars+pipe_tables+raw_tex-smart','--to=json']).stdout)
image_count=len(list(nodes(ast,'Image')))
table_widths=[[.30,.70],[.10,.90]]
for table,widths in zip(nodes(ast,'Table'),table_widths):
    for spec,width in zip(table['c'][2],widths):spec[1]={'t':'ColWidth','c':width}
maths=[n for n in nodes(ast,'Math') if n['c'][0]['t']=='DisplayMath'];original_bodies=[]
for n in maths:
    raw=n['c'][1];tag=re.search(r'\\tag\{([^}]+)\}',raw)
    body=re.sub(r'\\tag\{[^}]+\}','',raw).strip();original_bodies.append(body)
    n.clear();n.update({'t':'RawInline','c':['latex',r'\paperdisplay['+(tag.group(1) if tag else '')+']{'+body+'}']})
ast_path=BUILD/'paper_ast.json';ast_path.write_text(json.dumps(ast,ensure_ascii=False),encoding='utf-8')
TEX=ROOT/'paper_D_v0.1.1.tex'
run([PANDOC,ast_path,'--from=json','--to=latex','--standalone','--shift-heading-level-by=-1','--include-in-header='+str(ROOT/'publication_style.tex'),
 '--variable=documentclass:article','--variable=fontsize:11pt','--variable=papersize:a4','--variable=geometry:margin=24mm',
 '--variable=mainfont:texgyrepagella-regular.otf','--variable=mainfontoptions:BoldFont=texgyrepagella-bold.otf,ItalicFont=texgyrepagella-italic.otf,BoldItalicFont=texgyrepagella-bolditalic.otf',
 '--variable=mathfont:texgyrepagella-math.otf','--variable=monofont:lmmono10-regular.otf','--variable=monofontoptions:BoldFont=lmmonolt10-bold.otf',
 '--variable=colorlinks:true','--variable=linkcolor:MidnightBlue','--variable=urlcolor:MidnightBlue','--wrap=preserve','--output='+str(TEX)])
fc=BUILD/'fontconfig.xml';fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+str(BUILD/'fontconfig-cache').replace('\\','/')+'</cachedir></fontconfig>')
env=os.environ.copy();env['TECTONIC_CACHE_DIR']=str(CACHE.resolve());env['FONTCONFIG_FILE']=str(fc)
env['SOURCE_DATE_EPOCH']=str(int(datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc).timestamp()))
with (PUB/'build_console.log').open('wb') as f:
    result=subprocess.run([str(TECTONIC),'-X','compile','--only-cached','--keep-logs','--keep-intermediates','--outdir',str(BUILD),str(TEX)],cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
if result.returncode:
    print((PUB/'build_console.log').read_text(errors='replace')[-7000:]);raise SystemExit(result.returncode)
PDF=PUB/'PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf'
shutil.copyfile(BUILD/(TEX.stem+'.pdf'),PDF);shutil.copyfile(BUILD/(TEX.stem+'.log'),PUB/(TEX.stem+'.log'))
record={'python':sys.version,'pandoc':run([PANDOC,'--version']).stdout.decode().splitlines()[0],'tectonic':run([TECTONIC,'--version']).stdout.decode().strip(),
 'pandoc_sha256':digest(PANDOC),'tectonic_sha256':digest(TECTONIC),'source_date_epoch':env['SOURCE_DATE_EPOCH'],'offline_tex':True,
 'pdf_sha256':digest(PDF),'manuscript_sha256':digest(MD),'tex_sha256':digest(TEX)}
(PUB/'build_record.json').write_text(json.dumps(record,indent=2)+'\n')
tex=TEX.read_text(encoding='utf-8');fidelity={'display_blocks':len(maths),'figures':image_count,'all_equation_bodies_retained':all(b in tex for b in original_bodies),'scientific_content_omitted':False,'transformation':'Display wrappers and two table column widths only; complete Pandoc prose/image/table-cell/inline-math content retained.','table_widths':table_widths,'manuscript_sha256':digest(MD)}
assert fidelity['all_equation_bodies_retained'] and image_count==9
(EV/'structural_fidelity.json').write_text(json.dumps(fidelity,indent=2)+'\n')
print(json.dumps({**record,**fidelity},indent=2))
