"""Render the accepted Final Mathematical Bridge publication v0.1. No scientific project code is imported."""
import os,sys,re,json,html
from pathlib import Path
sys.dont_write_bytecode=True
from publication_io import ROOT,safe,write,save
for name in ('tmp','tmp/matplotlib','tmp/pdfs'):
    safe(name).mkdir(parents=True,exist_ok=True)
os.environ['MPLCONFIGDIR']=str(safe('tmp/matplotlib'))
os.environ['TEMP']=os.environ['TMP']=str(safe('tmp'))
extra_packages=os.environ.get('SRG_DOCUMENT_SITE_PACKAGES')
if extra_packages:sys.path.append(extra_packages)
import matplotlib
from matplotlib.mathtext import MathTextParser
from matplotlib.font_manager import FontProperties
from matplotlib.ft2font import LoadFlags
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Flowable,Table,TableStyle,KeepTogether
from pypdf import PdfReader

fonts=Path(matplotlib.get_data_path())/'fonts/ttf'
for family,stem in [('Body','DejaVuSerif'),('UI','DejaVuSans')]:
    for suffix,name in [('',family),('-Bold',family+'Bold'),('-Italic' if family=='Body' else '-Oblique',family+'Italic')]:
        pdfmetrics.registerFont(TTFont(name,str(fonts/(stem+suffix+'.ttf'))))
    pdfmetrics.registerFontFamily(family,normal=family,bold=family+'Bold',italic=family+'Italic',boldItalic=family+'Bold')

INK=colors.HexColor('#21313B'); TEAL=colors.HexColor('#176779'); BLUE=colors.HexColor('#294D77')
PALE=colors.HexColor('#EEF4F6'); MUTED=colors.HexColor('#526571'); RULE=colors.HexColor('#CDDADF')
W,H=A4; MARGIN=53; WIDTH=W-2*MARGIN
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.25,leading=15.0,textColor=INK,spaceAfter=8,allowWidows=0,allowOrphans=0),
 'title':ParagraphStyle('title',fontName='UIBold',fontSize=25,leading=30,textColor=BLUE,spaceAfter=14),
 'subtitle':ParagraphStyle('subtitle',fontName='UI',fontSize=16,leading=22,textColor=TEAL,spaceAfter=18),
 'h2':ParagraphStyle('h2',fontName='UIBold',fontSize=15,leading=20,textColor=BLUE,spaceBefore=15,spaceAfter=10,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='UIBold',fontSize=11.4,leading=16,textColor=TEAL,spaceBefore=11,spaceAfter=8,keepWithNext=True),
 'quote':ParagraphStyle('quote',fontName='Body',fontSize=9.5,leading=13.8,textColor=INK,leftIndent=12,rightIndent=8,borderColor=RULE,borderWidth=.5,borderPadding=8,spaceBefore=5,spaceAfter=10,allowWidows=0,allowOrphans=0),
 'table':ParagraphStyle('table',fontName='UI',fontSize=8.2,leading=11.6,textColor=INK),
 'thead':ParagraphStyle('thead',fontName='UIBold',fontSize=8.1,leading=11,textColor=colors.white),
 'ref':ParagraphStyle('ref',fontName='Body',fontSize=9.2,leading=13.0,textColor=INK,spaceAfter=10,allowWidows=0,allowOrphans=0),
 'caption':ParagraphStyle('caption',fontName='UI',fontSize=8.2,leading=11.5,textColor=MUTED,spaceAfter=12),
}
source_ids=set(s['id'] for s in json.loads(safe('SOURCE_LOCATORS.json').read_text('utf-8'))['sources'])|{'GPT_REVIEW'}
def markup(s,link_refs=True):
    s=html.escape(s)
    s=s.replace('ℓ','<font name="UI">ℓ</font>')
    # External references retain URLs; local snapshots are described in the PDF's source guide.
    def link(m):
        label,url=m.group(1),m.group(2)
        if url.startswith('http'):return f'<link href="{url}" color="#176779">{label}</link>'
        url='https://github.com/pzychozen/trioctagon-physics/blob/main/SRG_REDISCOVERY/FINAL_MATHEMATICAL_BRIDGE/publication/v0.1/'+url
        return f'<link href="{url}" color="#176779">{label}</link>'
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<font name="UI" size="9.0">\1</font>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    if link_refs:
        for sid in sorted(source_ids,key=len,reverse=True):
            s=re.sub(r'(?<![A-Z0-9_])'+sid+r'(?![A-Z0-9_])',f'<link href="#src_{sid}" color="#176779">{sid}</link>',s)
    return s

parser=MathTextParser('path');math_log=[]
def normalize_tex(t):
    t=re.sub(r'\\sqrt([0-9])',r'\\sqrt{\1}',t)
    t=re.sub(r'\\sqrt\s+([A-Za-z])',r'\\sqrt{\1}',t)
    t=re.sub(r'\\frac([0-9])([0-9])',r'\\frac{\1}{\2}',t)
    t=re.sub(r'\\frac([0-9])',r'\\frac{\1}',t)
    t=re.sub(r'\\frac\s+([A-Za-z])([0-9])',r'\\frac{\1}{\2}',t)
    t=re.sub(r'\\mathcal\s+([A-Za-z])',r'\\mathcal{\1}',t)
    t=t.replace(r'\bmod3',r'\,\mathrm{mod}\,3')
    return t

class MathBlock(Flowable):
    def __init__(self,tex,label):
        Flowable.__init__(self)
        self.label=label
        # N5 has three definitions. The source grouping remains one numbered equation.
        rows=tex.split(r'\qquad') if label=='N5' else [tex]
        self.parts=[parser.parse('$'+normalize_tex(t.strip().rstrip(','))+'$',dpi=72,prop=FontProperties(size=12,math_fontfamily='dejavuserif')) for t in rows]
        self.scale=min(1,(WIDTH-40)/max(p.width for p in self.parts))
        assert 12*self.scale>=9.0,(label,12*self.scale)
        self.width=WIDTH
        self.height=sum(p.height*self.scale+8 for p in self.parts)+12
        self.spaceAfter=8
        math_log.append({'equation':label,'rows':len(rows),'effective_font_pt':round(12*self.scale,2),'height':round(self.height,1)})
    def wrap(self,aw,ah):return self.width,self.height
    def draw(self):
        c=self.canv;y=self.height-7
        for data in self.parts:
            y-=data.height*self.scale
            c.saveState();c.translate((WIDTH-28-data.width*self.scale)/2,y+data.depth*self.scale);c.scale(self.scale,self.scale);c.setFillColor(INK)
            for font,size,num,ox,oy in data.glyphs:
                font.set_size(size,72);font.load_char(num,flags=LoadFlags.NO_HINTING)
                vertices,codes=font.get_path()
                from matplotlib.path import Path as MPath
                path=c.beginPath();current=(0,0)
                for verts,code in MPath(vertices,codes).iter_segments(curves=True):
                    if code==MPath.MOVETO:
                        current=(verts[0]+ox,verts[1]+oy);path.moveTo(*current)
                    elif code==MPath.LINETO:
                        current=(verts[0]+ox,verts[1]+oy);path.lineTo(*current)
                    elif code==MPath.CURVE3:
                        ctrl=(verts[0]+ox,verts[1]+oy);end=(verts[2]+ox,verts[3]+oy)
                        p1=(current[0]+2*(ctrl[0]-current[0])/3,current[1]+2*(ctrl[1]-current[1])/3)
                        p2=(end[0]+2*(ctrl[0]-end[0])/3,end[1]+2*(ctrl[1]-end[1])/3)
                        path.curveTo(*p1,*p2,*end);current=end
                    elif code==MPath.CURVE4:
                        path.curveTo(verts[0]+ox,verts[1]+oy,verts[2]+ox,verts[3]+oy,verts[4]+ox,verts[5]+oy);current=(verts[4]+ox,verts[5]+oy)
                    elif code==MPath.CLOSEPOLY:path.close()
                c.drawPath(path,fill=1,stroke=0)
            for x,y0,w,h in data.rects:c.rect(x,y0,w,h,stroke=0,fill=1)
            c.restoreState();y-=8
        c.setFont('UI',8.2);c.setFillColor(MUTED);c.drawRightString(WIDTH,self.height/2-3,'('+self.label+')')

class Routes(Flowable):
    def __init__(self):Flowable.__init__(self);self.width=WIDTH;self.height=238
    def wrap(self,aw,ah):return self.width,self.height
    def draw(self):
        c=self.canv;gap=23;bw=(WIDTH-gap)/2
        chains=[('LENS AND TRANSFER',[("Lens area fraction","Exact geometry"),("Amplitude preparation","Adopt A1–A4"),("Fixed SRG and extraction","Exact transfer and intertwining"),("Nonlinear triad initializer","Separate recurrence and optional faces")]),('SPECTRUM AND QUANTUM RING',[("Periodic positive Laplacian","Declare operator and circumference"),("Positive inverse trace","Exact spectrum and limiting theorem"),("Quantum-ring comparison","Adopt Hamiltonian and time law"),("Historical coupling identity","Specify p = 3/2 and calibration")])]
        for col,(title,items) in enumerate(chains):
            x=col*(bw+gap);c.setFillColor(TEAL if col==0 else BLUE);c.setFont('UIBold',8.5);c.drawString(x,224,title)
            for j,(top,bottom) in enumerate(items):
                y=170-j*51
                c.setFillColor(PALE);c.setStrokeColor(RULE);c.roundRect(x,y,bw,41,5,fill=1,stroke=1)
                c.setFillColor(INK);c.setFont('UIBold',9.2);c.drawCentredString(x+bw/2,y+25,top)
                c.setFillColor(MUTED);c.setFont('UI',7.7);c.drawCentredString(x+bw/2,y+11,bottom)
                if j<3:
                    c.setStrokeColor(MUTED);c.line(x+bw/2,y-1,x+bw/2,y-8)
                    c.line(x+bw/2,y-8,x+bw/2-2.5,y-5);c.line(x+bw/2,y-8,x+bw/2+2.5,y-5)

def furniture(c,d):
    c.saveState();c.setFillColor(MUTED);c.setFont('UI',7.7)
    c.drawString(MARGIN,H-30,'SRG FINAL MATHEMATICAL BRIDGE')
    c.drawRightString(W-MARGIN,H-30,'PUBLICATION v0.1 • 27 OCT 2026')
    c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(MARGIN,H-37,W-MARGIN,H-37)
    c.drawString(MARGIN,28,'Source-linked explanatory synthesis • Publication edition v0.1')
    c.drawRightString(W-MARGIN,28,str(d.page));c.restoreState()

story=[];lines=safe('SRG_FINAL_MATHEMATICAL_BRIDGE_v0.1.md').read_text('utf-8').splitlines();i=0;appendix=False
while i<len(lines):
    line=lines[i].strip()
    if not line:i+=1;continue
    if line.startswith('<!-- equation:'):
        label=line.split(':',1)[1].split(' ')[0];i+=1;assert lines[i].strip()=='$$';i+=1;rows=[]
        while lines[i].strip()!='$$':rows.append(lines[i].strip());i+=1
        story.append(MathBlock(' '.join(rows),label));i+=1;continue
    if line=='<!-- diagram:two_routes -->':
        story.append(Routes());story.append(Paragraph('Figure 1. Two explanatory routes. Labels distinguish exact consequences from supplied choices. No arrow joins lens response to coupling selection.',styles['caption']));i+=1;continue
    if line=='<!-- appendix:equation_sources -->':story.append(PageBreak());appendix=True;i+=1;continue
    if line.startswith('# '):story.append(Paragraph(markup(line[2:]),styles['title']));i+=1;continue
    if line.startswith('## From '):story.append(Paragraph(markup(line[3:]),styles['subtitle']));i+=1;continue
    if line.startswith('## '):
        if line.startswith('## Appendix B'):story.append(PageBreak())
        story.append(Paragraph(markup(line[3:]),styles['h2']));i+=1;continue
    if line.startswith('### '):story.append(Paragraph(markup(line[4:]),styles['h3']));i+=1;continue
    if line.startswith('|'):
        raw=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            row=[v.strip() for v in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[-: ]+',v) for v in row):raw.append(row)
            i+=1
        cells=[[Paragraph(markup(v),styles['thead' if j==0 else 'table']) for v in row] for j,row in enumerate(raw)]
        widths=[70,233,WIDTH-303] if appendix else [78,210,WIDTH-288]
        t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.6,TEAL),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LINEBELOW',(0,1),(-1,-1),.3,RULE)]))
        if not appendix:t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]))
        story.extend([t,Spacer(1,12)]);continue
    quote=line.startswith('> ');parts=[line[2:] if quote else line];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','<!--','>','|','$$')):
        parts.append(lines[i].strip());i+=1
    s=' '.join(parts);anchor='';match=re.match(r'\*\*\[([A-Z0-9_]+)\]\(',s)
    if match:anchor=f'<a name="src_{match.group(1)}"/>'
    elif s.startswith('**GPT_REVIEW**'):anchor='<a name="src_GPT_REVIEW"/>'
    story.append(Paragraph(anchor+markup(s,link_refs=not bool(anchor)),styles['quote' if quote else 'ref' if appendix else 'body']))

pdf=safe('SRG_FINAL_MATHEMATICAL_BRIDGE_v0.1.pdf')
doc=SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=MARGIN,leftMargin=MARGIN,topMargin=53,bottomMargin=48,title='SRG Final Mathematical Bridge: From Lens Geometry to Recurrence and Known Equations',author='Prepared for Hilmir Frímann Halldórsson; publication edition v0.1',subject='Accepted source-linked synthesis, publication v0.1, 27 October 2026',pageCompression=1)
doc.build(story,onFirstPage=furniture,onLaterPages=furniture)
r=PdfReader(pdf)
page_text=[p.extract_text() for p in r.pages]
write('tmp/pdf_extracted_text.txt','\n\n'.join(f'PAGE {j+1}\n{s}' for j,s in enumerate(page_text)))
save('records/PDF_BUILD_REPORT.json',{'pdf':str(pdf.relative_to(ROOT)),'pages':len(r.pages),'equations':math_log,'text_characters_by_page':[len(s) for s in page_text],'method':'ReportLab text and vector math glyphs; vector explanatory diagram; no scientific execution','fonts':['DejaVu Serif','DejaVu Sans'],'note':'Formula glyph outlines are vector paths; editable exact formulas are in the Markdown source. PDF text extraction therefore covers prose and labels, not every formula glyph.'})
print(json.dumps({'pdf':str(pdf),'pages':len(r.pages),'equations':len(math_log),'smallest_equation_font':min(e['effective_font_pt'] for e in math_log)},indent=2))
