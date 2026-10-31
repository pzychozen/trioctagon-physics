"""Offline document typesetting in torment; no native scientific execution."""
from pathlib import Path
import os,sys,json,re,hashlib,html,importlib.util
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'scratch/cache')
os.environ['TMP']=os.environ['TEMP']=str(ROOT/'scratch')
BUNDLE=Path(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages')
sys.path.append(str(BUNDLE))
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Image,KeepTogether
import matplotlib
matplotlib.use('Agg')
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties
from PIL import Image as PILImage
spec=importlib.util.spec_from_file_location('paper_content',ROOT/'manuscript/content.py')
content=importlib.util.module_from_spec(spec);spec.loader.exec_module(content)
OUT=ROOT/'manuscript'
ASSETS=OUT/'math_assets'; ASSETS.mkdir(exist_ok=True)
fontdir=Path(matplotlib.get_data_path())/'fonts/ttf'
for name,file in [('Body','DejaVuSerif.ttf'),('BodyBold','DejaVuSerif-Bold.ttf'),('BodyItalic','DejaVuSerif-Italic.ttf'),
                  ('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBold')
matplotlib.rcParams.update({'mathtext.fontset':'dejavuserif','font.family':'DejaVu Serif','text.usetex':False})
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.3,leading=14.5,spaceAfter=8,allowWidows=0,allowOrphans=0),
 'h':ParagraphStyle('h',fontName='SansBold',fontSize=14,leading=18,spaceAfter=13,keepWithNext=True,textColor=colors.HexColor('#203448')),
 'sub':ParagraphStyle('sub',fontName='BodyBold',fontSize=10.8,leading=14.8,spaceBefore=5,spaceAfter=7,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='BodyBold',fontSize=20,leading=25,spaceAfter=12),
 'meta':ParagraphStyle('meta',fontName='Sans',fontSize=9.2,leading=13,spaceAfter=7),
 'caption':ParagraphStyle('caption',fontName='BodyItalic',fontSize=9,leading=12,spaceAfter=7,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=8.4,leading=11.7),
 'head':ParagraphStyle('head',fontName='SansBold',fontSize=8.2,leading=11.2),
 'ref':ParagraphStyle('ref',fontName='Body',fontSize=8.9,leading=12.5,spaceAfter=10),
}
MARGIN=49
WIDTH=A4[0]-2*MARGIN
math_records={}

def normalized_math(expr):
    # Mathtext needs braced fractions; both engines use the same resulting formula.
    expr=re.sub(r'\\frac\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',expr)
    expr=re.sub(r'\\frac\s*([A-Za-z0-9])(?=\{)',r'\\frac{\1}',expr)
    expr=re.sub(r'\\sqrt\s*([A-Za-z0-9])',r'\\sqrt{\1}',expr)
    expr=re.sub(r'\\(le|ge|ne)(?![A-Za-z])',lambda m:'\\'+{'le':'leq','ge':'geq','ne':'neq'}[m[1]],expr)
    return expr

def math_asset(expr,size):
    expr=normalized_math(expr)
    key=hashlib.sha256((expr+str(size)).encode()).hexdigest()[:20]
    target=ASSETS/(key+'.png')
    prop=FontProperties(size=size)
    if not target.exists():
        mathtext.math_to_image('$'+expr+'$',str(target),prop=prop,dpi=360,format='png',color='#111111')
    with PILImage.open(target) as im: w,h=im.size
    parsed=mathtext.MathTextParser('agg').parse('$'+expr+'$',dpi=360,prop=prop)
    rec={'source':expr,'file':target.name,'width_pt':w/5,'height_pt':h/5,'depth_pt':float(parsed.depth)/5}
    math_records[key]=rec
    return target,rec

def rich(text,size=None):
    size=size or 10.3
    # Keep punctuation attached to the preceding inline mathematical expression.
    text=re.sub(r'\$([^$]+)\$([,.;:])',r'$\1\2$',text)
    result=[]
    for i,part in enumerate(re.split(r'\$([^$]+)\$',text)):
        if i%2:
            target,rec=math_asset(part,size)
            result.append(f'<img src="{target.as_posix()}" width="{rec["width_pt"]:.3f}" height="{rec["height_pt"]:.3f}" valign="{-rec["depth_pt"]:.3f}"/>')
        else:
            val=html.escape(part)
            val=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',val)
            val=re.sub(r'\[@([A-Z0-9]+)\]',r'<link href="#ref-\1" color="#1c537c">[\1]</link>',val)
            result.append(val)
    return ''.join(result)

def tex_escape(text):
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]: text=text.replace(a,b)
    return text
def tex_inline(text):
    parts=re.split(r'\$([^$]+)\$',text); out=[]
    for i,part in enumerate(parts):
        if i%2: out.append('$'+normalized_math(part)+'$')
        else:
            part=tex_escape(part)
            part=re.sub(r'\*\*(.+?)\*\*',r'\\textbf{\1}',part)
            part=re.sub(r'\[@([A-Z0-9]+)\]',r'\\cite{\1}',part)
            out.append(part)
    return ''.join(out)

story=[Paragraph(html.escape(content.TITLE),styles['title']),
       Paragraph(html.escape(content.AUTHOR),styles['meta']),
       Paragraph(html.escape(content.STATUS)+'<br/>'+content.DATE,styles['meta']),Spacer(1,7)]
tex=[r'\documentclass[11pt,a4paper]{article}',
 r'\usepackage[margin=23mm]{geometry}',r'\usepackage{fontspec,amsmath,amssymb,booktabs,tabularx,xcolor,hyperref}',
 r'\setmainfont{DejaVu Serif}',r'\setsansfont{DejaVu Sans}',
 r'\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}',
 r'\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}',
 r'\setlength{\emergencystretch}{3em}',
 r'\title{'+tex_escape(content.TITLE)+'}',r'\author{'+content.AUTHOR+'}',
 r'\date{'+content.DATE+r'\\'+content.STATUS+'}',
 r'\begin{document}\maketitle',
 '% Generated from content.py; supplied LaTeX source was not compiled in this task.',
 '% REVIEW.pdf was typeset from the same content with existing ReportLab/mathtext.',
 ]
eqnum=0
for block in content.BLOCKS:
    kind=block[0]
    if kind in ('p','h','sub'):
        sty={'p':'body','h':'h','sub':'sub'}[kind]
        story.append(Paragraph(rich(block[1]),styles[sty]))
        if kind=='p': tex.append(tex_inline(block[1])+'\n')
        else: tex.append(('\\section*{' if kind=='h' else '\\subsection*{')+tex_escape(block[1])+'}')
    elif kind=='page':
        story.append(PageBreak());tex.append(r'\clearpage')
    elif kind=='eq':
        eqnum+=1
        target,rec=math_asset(block[1],11.2)
        scale=min(1,(WIDTH-38)/rec['width_pt'])
        if scale<.83: raise RuntimeError(f'Equation {eqnum} too wide; split it, scale={scale}')
        im=Image(str(target),width=rec['width_pt']*scale,height=rec['height_pt']*scale)
        t=Table([[im,Paragraph(f'({eqnum})',styles['cell'])]],colWidths=[WIDTH-32,32],hAlign='LEFT')
        t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER'),
                              ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                              ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
        story.append(t)
        tex.append(r'\begin{equation}'+normalized_math(block[1])+r'\end{equation}')
    elif kind=='table':
        _,caption,heads,rows,widths=block
        data=[[Paragraph(rich(x,8.2),styles['head']) for x in heads]]
        data += [[Paragraph(rich(x,8.4),styles['cell']) for x in row] for row in rows]
        t=Table(data,colWidths=[WIDTH*w for w in widths],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf1')),('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#5b6f7f')),
            ('LINEBELOW',(0,-1),(-1,-1),.4,colors.HexColor('#5b6f7f')),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f6f7f8')]),
            ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([Paragraph(rich(caption,9),styles['caption']),t,Spacer(1,11)])
        tex.extend([r'\par\textit{'+tex_inline(caption)+r'}\par',r'\begingroup\small',
                    r'\begin{tabularx}{\textwidth}{'+'X'*len(heads)+'}',r'\toprule',
                    ' & '.join(tex_inline(v) for v in heads)+r'\\\midrule'])
        for row in rows: tex.append(' & '.join(tex_inline(v) for v in row)+r'\\')
        tex.extend([r'\bottomrule\end{tabularx}\endgroup\par'])
story.append(PageBreak())
story.append(Paragraph('References',styles['h']))
tex.extend([r'\clearpage',r'\begin{thebibliography}{REV03}'])
bib=[]
for key,author,title,note,year in content.REFERENCES:
    value=f'<a name="ref-{key}"/>[{key}] {html.escape(author)} ({year}). <i>{html.escape(title)}</i>. {html.escape(note)}. <link href="../EVIDENCE_INDEX.md#{key.lower()}" color="#1c537c">Source record {key}</link>.'
    story.append(Paragraph(value,styles['ref']))
    tex.append(r'\bibitem{'+key+'} '+tex_escape(author)+f' ({year}). '+r'\emph{'+tex_escape(title)+'}. '+tex_escape(note)+r'. \href{../EVIDENCE_INDEX.md\#'+key.lower()+'}{Source record '+key+'}.')
    bib.append('@misc{'+key+',\n  author = {'+author+'},\n  title = {'+title+'},\n  year = {'+year+'},\n  note = {'+tex_escape(note)+'; source record '+key+' in ../EVIDENCE_INDEX.md}\n}')
tex.extend([r'\end{thebibliography}',r'\end{document}'])
(OUT/'main.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8')
(OUT/'references.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf-8')
(OUT/'content_snapshot.json').write_text(json.dumps({'title':content.TITLE,'author':content.AUTHOR,'status':content.STATUS,'blocks':content.BLOCKS,'references':content.REFERENCES},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def footer(canvas,doc):
    canvas.saveState()
    canvas.setFont('Sans',7.3);canvas.setFillColor(colors.HexColor('#54616a'))
    canvas.drawString(MARGIN,26,'NCM-PAPER-01 v0.1 | Research draft — for GPT/author review')
    canvas.drawRightString(A4[0]-MARGIN,26,str(doc.page))
    canvas.restoreState()
doc=SimpleDocTemplate(str(OUT/'REVIEW.pdf'),pagesize=A4,rightMargin=MARGIN,leftMargin=MARGIN,
                      topMargin=42,bottomMargin=46,title=content.TITLE,author=content.AUTHOR,
                      subject=content.STATUS,pageCompression=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
(OUT/'math_asset_manifest.json').write_text(json.dumps(math_records,indent=2)+'\n',encoding='utf-8')
record={'python':sys.executable,'version':sys.version,'reportlab':reportlab.Version,'reportlab_source':reportlab.__file__,
        'matplotlib':matplotlib.__version__,'pages':doc.page,'numbered_equations':eqnum,
        'math_assets':len(math_records),'latex_compiled':False,'native_F_evaluations':0,
        'shared_content':'manuscript/content.py','fonts_embedded_not_shipped':True}
(ROOT/'qa/BUILD_RECORD.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
