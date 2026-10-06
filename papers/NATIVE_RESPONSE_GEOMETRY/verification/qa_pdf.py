"""Render all pages and prepare text-bound diagnostics; visual review is separate."""
from pathlib import Path
import json,subprocess,hashlib,argparse
import pdfplumber
from PIL import Image,ImageDraw
L=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,required=True,help='Fresh render directory outside the paper lane; existing tmp previews must remain untouched.')
args=parser.parse_args()
pdf=L/'publication/Native_Response_Geometry_v0.1.pdf';tmp=args.output_dir.resolve()
if tmp.is_relative_to(L.resolve()):parser.error('Render outside the paper lane to preserve existing tmp previews.')
tmp.mkdir(parents=True,exist_ok=True)
with pdfplumber.open(pdf) as doc:count=len(doc.pages)
cmd=['pdftoppm','-r','110','-png',str(pdf),str(tmp/'page')]
subprocess.run(cmd,check=True,capture_output=True)
pages=[tmp/f'page-{i:0{len(str(count))}d}.png' for i in range(1,count+1)]
assert all(p.exists() for p in pages)
for j in range(0,len(pages),8):
    sheet=Image.new('RGB',(1600,1190),'#d5d9df');draw=ImageDraw.Draw(sheet)
    for k,p in enumerate(pages[j:j+8]):
        im=Image.open(p).convert('RGB');im.thumbnail((385,555))
        x=(k%4)*400+7;y=(k//4)*590+26
        sheet.paste(im,(x,y));draw.text((x,y-20),f'PDF page {j+k+1}',fill='black')
    sheet.save(tmp/f'contact-{j//8+1:02d}.png')
rows=[]
with pdfplumber.open(pdf) as doc:
    for i,p in enumerate(doc.pages,1):
        text=p.extract_text() or ''
        outside=[c for c in p.chars if c['x0']<35 or c['x1']>p.width-35 or c['top']<25 or c['bottom']>p.height-25]
        rows.append({'pdf_page':i,'characters':len(p.chars),'word_count':len(text.split()),'text_extents':[min(c['x0'] for c in p.chars),min(c['top'] for c in p.chars),max(c['x1'] for c in p.chars),max(c['bottom'] for c in p.chars)],'outside_safe_page_bounds':len(outside),'unresolved_reference_marker':'??' in text,'replacement_character':'\ufffd' in text,'heading_preview':text[:130]})
        (tmp/f'text-{i:02d}.txt').write_text(text,encoding='utf8')
result={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'render_command':cmd,'page_count':len(rows),'all_pages_rendered':len(pages)==len(rows),'rendered_dpi':110,'automated_checks_passed':all(not x['outside_safe_page_bounds'] and not x['unresolved_reference_marker'] and not x['replacement_character'] for x in rows),'pages':rows,'qualification':'Automated geometry/text diagnostics only. Visual review recorded in PDF_QA.md.'}
(L/'publication/pdf_qa_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='pages'},indent=2))
