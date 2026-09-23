"""Faithful Paper C publication adapter. No geometry or research program is run."""
from pathlib import Path
import copy, datetime, hashlib, json, os, re, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parent
BUILD=ROOT/'.build';BUILD.mkdir(exist_ok=True)
def tool(name,var):
    value=os.environ.get(var) or shutil.which(name)
    if not value or not Path(value).is_file():raise RuntimeError('Set '+var+' to existing '+name)
    return Path(value).resolve()
PANDOC=tool('pandoc','PAPER_C_PANDOC');TECTONIC=tool('tectonic','PAPER_C_TECTONIC')
CACHE=Path(os.environ.get('PAPER_C_TEX_CACHE',''))
if not os.environ.get('PAPER_C_TEX_CACHE') or not CACHE.is_dir():raise RuntimeError('Set PAPER_C_TEX_CACHE to an existing populated cache.')
SOURCE='PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md'
TITLE='Exact Geometry of the Folded Tri-Octagon Module'
PDF_NAME='PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.1.pdf'
META=json.loads((ROOT/'publication_metadata.json').read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def run(args,**kw):return subprocess.run([str(x) for x in args],check=True,capture_output=True,**kw)
def nodes(obj,kind):
    if isinstance(obj,dict):
        if obj.get('t')==kind:yield obj
        for value in obj.values():yield from nodes(value,kind)
    elif isinstance(obj,list):
        for value in obj:yield from nodes(value,kind)
def plain(obj):
    if isinstance(obj,dict):
        t,c=obj.get('t'),obj.get('c')
        if t=='Str':return c
        if t in ['Space','SoftBreak','LineBreak']:return ' '
        if t in ['Code','Math']:return c[-1]
        if t=='Header':return plain(c[-1])
        if t=='Link':return plain(c[1])
        return plain(c)
    if isinstance(obj,list):return ''.join(plain(x) for x in obj)
    return ''

# Start from the existing publication manuscript, not the frozen research draft.
# No new scientific or provenance omissions are made in this revision.
retained=(ROOT/SOURCE).read_text(encoding='utf-8');lines=retained.splitlines();omissions=[]
fmt='markdown+tex_math_dollars+pipe_tables+raw_tex+lists_without_preceding_blankline-smart'
ast=json.loads(run([PANDOC,'--from',fmt,'--to=json'],input=retained.encode()).stdout)
original=copy.deepcopy(ast)
(BUILD/'publication_original_ast.json').write_text(json.dumps(original,ensure_ascii=False,indent=2),encoding='utf-8')
tags=re.findall(r'\*\*\[([A-Za-z0-9]+)\]\*\*',retained.split('## References',1)[1])
assert len(tags)==len(set(tags))==14 and 'PD' in tags

equations=[]
def transform(obj):
    if isinstance(obj,list):
        result=[]
        for item in obj:
            val=transform(item)
            result.extend(val if isinstance(item,dict) and item.get('t')=='Str' and isinstance(val,list) else [val])
        return result
    if not isinstance(obj,dict):return obj
    t,c=obj.get('t'),obj.get('c')
    if t=='Math' and c[0]['t']=='DisplayMath':
        expr=c[1]
        rendered=expr
        if expr.lstrip().startswith(r'P_1^\beta(u,z)='):
            rendered=r'\begin{gathered}'+expr.replace(r'\quad',r'\quad\\[4pt]',1)+r'\end{gathered}'
        elif expr.lstrip().startswith(r'|e_1|^2='):
            rendered=r'\begin{gathered}'+expr.replace(r'\qquad',r'\qquad\\[3pt]')+r'\end{gathered}'
        equations.append({'number':'','source':expr,'rendered_expression':rendered})
        return {'t':'RawInline','c':['latex',r'\paperdisplay[]{'+rendered+'}']}
    if t=='Code':
        assert '{' not in c[1] and '}' not in c[1]
        return {'t':'RawInline','c':['latex',r'\path{'+c[1]+'}']}
    if t=='Str':
        s=c
        if re.match(r'^10\.\d{4,9}/',s) and s.endswith('.'):
            return {'t':'RawInline','c':['latex',r'\paperdoi{'+s[:-1]+'}.']}
        pattern=r'(?<![A-Za-z0-9])('+'|'.join(sorted(tags,key=len,reverse=True))+r')(?![A-Za-z0-9])'
        result=[];last=0
        for m in re.finditer(pattern,s):
            if m.start()>last:result.append({'t':'Str','c':s[last:m.start()]})
            result.append({'t':'RawInline','c':['latex',r'\hyperlink{ref-'+m.group()+'}{'+m.group()+'}']})
            last=m.end()
        if not result:return obj
        if last<len(s):result.append({'t':'Str','c':s[last:]})
        return result
    return {k:transform(v) for k,v in obj.items()}

seen=False
for block in ast['blocks']:
    if block['t']=='Header' and plain(block)=='References':seen=True
    if seen and block['t']=='BulletList':
        assert len(block['c'])==13
        for item,tag in zip(block['c'],tags[:13]):
            item[0]['c'].insert(0,{'t':'RawInline','c':['latex',r'\hypertarget{ref-'+tag+'}{}']})
    if seen and block['t']=='Para' and plain(block).startswith('[PD]'):
        block['c'].insert(0,{'t':'RawInline','c':['latex',r'\hypertarget{ref-PD}{}']})
ast=transform(ast)
(BUILD/'equation_rendering_map.json').write_text(json.dumps(equations,ensure_ascii=False,indent=2),encoding='utf-8')
raw=lambda s:{'t':'RawBlock','c':['latex',s]}
out=[];front=[];abstract_seen=False;table_i=0
widths=[[.26,.075,.435,.23],[.045,.285,.21,.24,.22],[.43,.30,.27]]
for block in ast['blocks']:
    if block['t']=='HorizontalRule':continue
    if block['t']=='Header' and block['c'][0]==1:continue
    if block['t']=='Header' and plain(block)=='Abstract':abstract_seen=True
    if not abstract_seen:
        front.append(block);continue
    if block['t']=='Para' and plain(block).startswith('The four measures, all in the'):
        out.append(raw(r'\clearpage'))
    if block['t']=='Header':
        label=plain(block)
        if label=='1. Introduction':
            out.append(raw(r'\clearpage'))
            out.append({'t':'Header','c':[1,['scope-and-verification-provenance',[],[]],[{'t':'Str','c':'Scope and verification provenance'}]]})
            out.extend(front)
        if label.startswith('4. Exact coordinate') or label.startswith('5. Mesh topology'):
            out.append(raw(r'\clearpage'))
        if label.startswith('Appendix A'):
            out.append(raw(r'\Needspace{8\baselineskip}'))
        if label=='References':
            out.append({'t':'Header','c':[1,['acknowledgements',[],[]],[{'t':'Str','c':'Acknowledgements'}]]})
            out.append({'t':'Para','c':[{'t':'Str','c':META['acknowledgement']}]})
            out.append(raw(r'\Needspace{6\baselineskip}'))
            out.append(raw(r'\begingroup\fontsize{10}{12}\selectfont'))
        block['c'][0]-=1
    if block['t']=='Table':
        for spec,w in zip(block['c'][2],widths[table_i]):spec[1]={'t':'ColWidth','c':w}
        settings=r'\begingroup\fontsize{9.3}{12}\selectfont\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.3}'
        if table_i==1:
            settings=r'\begingroup\fontsize{10.2}{13.5}\selectfont\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.3}'
        out.extend([raw(settings),block,raw(r'\endgroup')]);table_i+=1
    else:out.append(block)
assert table_i==3 and len(front)==2
out.append(raw(r'\endgroup'))
ast['blocks']=out
ast['meta']['title']={'t':'MetaInlines','c':[{'t':'Str','c':TITLE}]}
ast['meta']['author']={'t':'MetaInlines','c':[{'t':'Str','c':META['author']}]}
ast['meta']['date']={'t':'MetaInlines','c':[{'t':'Str','c':'Publication revision v1.0.1 - 23 September 2026'}]}
(BUILD/'paper_C_publication.json').write_text(json.dumps(ast,ensure_ascii=False,indent=2),encoding='utf-8')
args=[PANDOC,BUILD/'paper_C_publication.json','--from=json','--to=latex','--standalone',
 '--include-in-header='+str(ROOT/'publication_style.tex'),'--variable=documentclass:article','--variable=fontsize:11pt',
 '--variable=papersize:a4','--variable=geometry:margin=24mm','--variable=mainfont:texgyrepagella-regular.otf',
 '--variable=mainfontoptions:BoldFont=texgyrepagella-bold.otf,ItalicFont=texgyrepagella-italic.otf,BoldItalicFont=texgyrepagella-bolditalic.otf',
 '--variable=mathfont:texgyrepagella-math.otf','--variable=monofont:lmmono10-regular.otf','--variable=monofontoptions:BoldFont=lmmonolt10-bold.otf',
 '--variable=colorlinks:true','--variable=linkcolor:MidnightBlue','--variable=urlcolor:MidnightBlue','--wrap=preserve','--output='+str(ROOT/'paper_C_final.tex')]
run(args)
stats={'title':TITLE,'authors':[META['author']],'display_equation_blocks':len(equations),
 'inline_math_nodes':len([n for n in nodes(original,'Math') if n['c'][0]['t']=='InlineMath']),
 'explicit_equation_labels':[],'tables':table_i,'table_rows':[len(n['c'][4][0][3]) for n in nodes(original,'Table')],
 'theorem_labels_in_source_order':[re.search(r'Theorem (\d+b?)',plain(n)).group() for n in nodes(original,'BlockQuote')],
 'bibliography_count':len(tags),'bibliography_tags':tags,'headings':[plain(n) for n in nodes(original,'Header')],
 'scientific_omissions':0,'internal_provenance_omissions':len(omissions),'required_figures':len(list(nodes(original,'Image')))}
assert stats['table_rows']==[4,18,24]
(BUILD/'structural_fidelity.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
versions={'python':sys.version,'pandoc':run([PANDOC,'--version']).stdout.decode('utf-8').strip(),'tectonic':run([TECTONIC,'--version']).stdout.decode('utf-8').strip()}
(BUILD/'tool_versions.json').write_text(json.dumps(versions,ensure_ascii=False,indent=2),encoding='utf-8')
fc=BUILD/'fontconfig.xml'
fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+str(BUILD/'fontconfig-cache').replace('\\','/')+'</cachedir></fontconfig>')
env=os.environ.copy();env['TECTONIC_CACHE_DIR']=str(CACHE.resolve());env['FONTCONFIG_FILE']=str(fc)
env['SOURCE_DATE_EPOCH']=str(int(datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc).timestamp()))
with (BUILD/'build_console.log').open('wb') as log:
    result=subprocess.run([str(TECTONIC),'-X','compile','--only-cached','--keep-logs','--keep-intermediates','--outdir',str(BUILD),str(ROOT/'paper_C_final.tex')],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
print((BUILD/'build_console.log').read_text(encoding='utf-8',errors='replace')[-10000:])
if result.returncode:raise SystemExit(result.returncode)
shutil.copyfile(BUILD/'paper_C_final.pdf',ROOT/PDF_NAME)
print('BUILT',ROOT/PDF_NAME)

shutil.copyfile(BUILD/'paper_C_final.log',ROOT/'paper_C_final.log')
shutil.copyfile(BUILD/'build_console.log',ROOT/'build_console.log')
shutil.copyfile(BUILD/'structural_fidelity.json',ROOT/'evidence/structural_fidelity.json')
record={'python':sys.version,'pandoc':versions['pandoc'].splitlines()[0],'tectonic':versions['tectonic'],
 'pandoc_sha256':digest(PANDOC),'tectonic_sha256':digest(TECTONIC),'source_date_epoch':env['SOURCE_DATE_EPOCH'],
 'cache':'explicit existing resource cache; --only-cached; no source-workspace fallback',
 'pdf_sha256':digest(ROOT/PDF_NAME),'manuscript_sha256':digest(ROOT/SOURCE),'tex_sha256':digest(ROOT/'paper_C_final.tex')}
(ROOT/'build_record.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
