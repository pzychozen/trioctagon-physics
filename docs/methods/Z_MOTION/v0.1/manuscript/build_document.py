"""Typeset canonical Markdown + extracted tables only. No scientific evaluation.

Uses existing Matplotlib/PdfPages/mathtext; not a TeX compilation. Poppler renders
the resulting PDFs. All caches and temporary pages stay under the output root.
"""
from pathlib import Path
import os,re,json,hashlib,subprocess,shutil,sys,datetime,warnings
R=Path(__file__).resolve().parents[1];os.environ['MPLCONFIGDIR']=str(R/'cache/matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle
from PIL import Image

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','pdf.fonttype':42,'text.usetex':False})
W,H=595.276,841.89;LEFT=43;RIGHT=W-43;TOP=787;BOTTOM=46;WIDTH=RIGHT-LEFT
NAVY='#19374c';TEAL='#257b83';INK='#243440';GRAY='#5e6e78';PALE='#edf3f5'
ALL_LAYOUT=[];EQ=[]
def clean(s):
 s=re.sub(r'\*\*(.*?)\*\*',r'\1',s);s=re.sub(r'`([^`]+)`',r'\1',s)
 return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014',' - ')
def expanded(path):
 text=path.read_text(encoding='utf-8')
 def inc(m):
  p=(path.parent/m.group(1)).resolve();assert p.is_relative_to(R);return p.read_text(encoding='utf-8').strip()
 return re.sub(r'<!-- include: ([^>]+) -->',inc,text)
def blocks(text):
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line=='$$':
   buf=[];i+=1
   while lines[i].strip()!='$$':buf.append(lines[i].strip());i+=1
   out.append(('math',' '.join(buf)));i+=1
  elif line.startswith('!['):out.append(('image',re.match(r'!\[([^\]]*)\]\(([^)]+)\)',line).groups()));i+=1
  elif line.startswith('|'):
   buf=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',c) for c in row):buf.append(row)
    i+=1
   out.append(('table',buf))
  elif line.startswith('#'):
   level=len(line)-len(line.lstrip('#'));out.append(('heading',(level,line[level:].strip())));i+=1
  else:
   buf=[line];i+=1
   while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','$$','![')):
    if lines[i].startswith('- '):break
    buf.append(lines[i].strip());i+=1
   out.append(('paragraph',' '.join(buf)))
 return out
def make_page(page,total,title):
 fig=plt.figure(figsize=(W/72,H/72),dpi=120);ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,W);ax.set_ylim(0,H);ax.axis('off')
 ax.text(LEFT,H-27,'TRI-OCTAGON  /  EXPLANATORY METHODS',fontsize=8,color=TEAL,va='top',weight='bold')
 ax.plot([LEFT,RIGHT],[H-38,H-38],color=TEAL,lw=.8)
 ax.text(LEFT,25,'NCM-Z-DOC-01 v0.1  •  Documentation review draft',fontsize=8,color=GRAY)
 ax.text(RIGHT,25,f'{page} / {total}',fontsize=8,color=GRAY,ha='right')
 fig.canvas.draw();return fig,ax,fig.canvas.get_renderer()
def width(text,size,renderer,bold=False):
 prop=FontProperties(family='DejaVu Sans',size=size,weight='bold' if bold else 'normal')
 return renderer.get_text_width_height_descent(clean(text),prop,ismath=False)[0]*72/120
def wrap(text,size,maxwidth,renderer,bold=False):
 result=[];line=''
 for word in clean(text).split():
  test=(line+' '+word).strip()
  if width(test,size,renderer,bold)>maxwidth and line:result.append(line);line=word
  else:line=test
 if line:result.append(line)
 return result
def drawtext(ax,renderer,text,y,size=10.3,bold=False,color=INK,x=LEFT,maxwidth=WIDTH,leading=None,gap=9):
 leading=leading or size*1.42;lines=wrap(text,size,maxwidth,renderer,bold)
 for line in lines:ax.text(x,y,line,fontsize=size,fontweight='bold' if bold else 'normal',color=color,va='top');y-=leading
 return y-gap
def render(source,out):
 text=expanded(source);pages=text.split('<!-- page -->');title=text.splitlines()[0].lstrip('# ')
 layout=[]
 with PdfPages(out,metadata={'Title':title,'Author':'Hilmir Frímann Halldórsson / pzychozen','Subject':'Documentation consolidation; no new scientific calculations','Creator':'Matplotlib PdfPages from canonical Markdown; no TeX compiler'}) as pdf:
  for page,body in enumerate(pages,1):
   fig,ax,renderer=make_page(page,len(pages),title);y=TOP;record=[]
   for kind,data in blocks(body):
    start=y
    if kind=='heading':
     level,s=data;size={1:23,2:16,3:11.8}.get(level,10.5)
     y=drawtext(ax,renderer,s,y,size,True,NAVY,gap=14 if level<3 else 9)
    elif kind=='paragraph':
     iscaption=data.startswith('Figure ');y=drawtext(ax,renderer,data,y,9.4 if iscaption else 10.3,color=GRAY if iscaption else INK)
    elif kind=='math':
     artist=ax.text(LEFT+8,y,'$'+data+'$',fontsize=12.1,color=INK,va='top')
     fig.canvas.draw();box=artist.get_window_extent(renderer);bw=box.width*72/120;bh=box.height*72/120
     if bw>WIDTH-16:
      artist.set_fontsize(max(10.2,12.1*(WIDTH-16)/bw));fig.canvas.draw();box=artist.get_window_extent(renderer);bw=box.width*72/120;bh=box.height*72/120
     assert bw<=WIDTH-10,('equation too wide',page,data,bw)
     y-=max(25,bh+13);EQ.append({'pdf':out.name,'page':page,'latex':data,'width_pt':bw,'font_size':artist.get_fontsize()})
    elif kind=='table':
     n=len(data[0]);fractions={2:[.21,.79],3:[.38,.31,.31],4:[.19,.22,.26,.33],5:[.10,.225,.225,.225,.225]}.get(n,[1/n]*n)
     assert all(len(row)==n for row in data),('inconsistent table columns',page,data)
     if data[0][0]=='Evidence':fractions=[.15,.13,.32,.4]
     if data[0][0]=='n':fractions=[.06,.24,.20,.27,.23]
     colwidth=[WIDTH*f for f in fractions];size=9.2
     for ri,row in enumerate(data):
      wrapped=[wrap(cell,size,w-12,renderer,ri==0) for cell,w in zip(row,colwidth)];rowh=max(len(t) for t in wrapped)*12.4+12
      ax.add_patch(Rectangle((LEFT,y-rowh),WIDTH,rowh,facecolor=NAVY if ri==0 else (PALE if ri%2 else 'white'),edgecolor='none'))
      x=LEFT
      for vals,w in zip(wrapped,colwidth):
       yy=y-6
       for line in vals:ax.text(x+6,yy,line,fontsize=size,color='white' if ri==0 else INK,fontweight='bold' if ri==0 else 'normal',va='top');yy-=12.4
       x+=w
      y-=rowh
     y-=12
    elif kind=='image':
     caption,name=data;p=(source.parent/name).resolve();assert p.is_relative_to(R)
     im=Image.open(p);iw,ih=im.size;hh=WIDTH*ih/iw
     # Full sheet, uncropped and aspect-preserving. Scale only for page layout.
     ax.imshow(im,extent=(LEFT,RIGHT,y-hh,y),aspect='auto',interpolation='antialiased');y-=hh+12
    record.append({'block':kind,'top':start,'bottom':y})
   if y<BOTTOM:raise RuntimeError(f'Page overflow in {out.name} page {page}: bottom {y:.1f}, needs {BOTTOM}')
   fig.canvas.draw()
   # Detect visible text wider than margins; graphics captions are inspected separately.
   for artist in ax.texts:
    bb=artist.get_window_extent(renderer);x0=bb.x0*72/120;x1=bb.x1*72/120
    assert x0>=LEFT-1 and x1<=RIGHT+1,('text outside margins',page,artist.get_text(),x0,x1)
   pdf.savefig(fig);plt.close(fig);layout.append({'page':page,'bottom_content_pt':y,'blocks':record})
 ALL_LAYOUT.append({'pdf':str(out.relative_to(R)).replace('\\','/'),'pages':layout})
 return len(pages)

def main():
 outputs=[(R/'manuscript/NOTE.md',R/'manuscript/NCM_Z_DOCUMENTATION_v0.1.pdf'),(R/'PLAIN_LANGUAGE_GUIDE.md',R/'PLAIN_LANGUAGE_GUIDE_v0.1.pdf')]
 records=[]
 with warnings.catch_warnings(record=True) as warn:
  warnings.simplefilter('always')
  for source,out in outputs:
   pages=render(source,out);renderdir=R/'tmp/renders'/out.stem;renderdir.mkdir(parents=True,exist_ok=True)
   cmd=[shutil.which('pdftoppm'),'-r','120','-png',str(out),str(renderdir/'page')]
   p=subprocess.run(cmd,capture_output=True,text=True);assert p.returncode==0,p.stderr
   info=subprocess.run([shutil.which('pdfinfo'),str(out)],capture_output=True,text=True);assert info.returncode==0
   (renderdir/'pdfinfo.txt').write_text(info.stdout,encoding='utf-8')
   actual=int(re.search(r'Pages:\s+(\d+)',info.stdout).group(1));assert actual==pages
   texttool=shutil.which('pdftotext')
   if texttool:
    textfile=renderdir/'text.txt';p=subprocess.run([texttool,'-layout',str(out),str(textfile)],capture_output=True,text=True);assert p.returncode==0
   records.append({'pdf':str(out.relative_to(R)).replace('\\','/'),'pages':pages,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'canonical_source':str(source.relative_to(R)).replace('\\','/'),'render_directory':str(renderdir.relative_to(R)).replace('\\','/'),'render_command':cmd,'engine':'Matplotlib PdfPages/mathtext, not compiled LaTeX','pdfinfo':info.stdout})
  messages=[str(w.message) for w in warn];assert not any('Glyph' in m and 'missing' in m for m in messages),messages
 (R/'BUILD_RECORD.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'interpreter':sys.executable,'matplotlib':matplotlib.__version__,'outputs':records,'warnings':messages,'text_extractor_available':bool(shutil.which('pdftotext')),'QA_basis':'Source/table checks, glyph/margin checks, pdfinfo and full-page Poppler render inspection; no pdftotext available','scientific_evaluations':0},indent=2)+'\n',encoding='utf-8')
 (R/'tmp/LAYOUT_RECORD.json').write_text(json.dumps(ALL_LAYOUT,indent=2)+'\n')
 (R/'manuscript/EQUATION_TRANSCRIPTION.json').write_text(json.dumps(EQ,indent=2)+'\n')
 print(json.dumps([{'pdf':x['pdf'],'pages':x['pages'],'sha256':x['sha256']} for x in records],indent=2))

if __name__=='__main__':main()
