"""Render every PDF page and assemble readable two-page review sheets externally."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader
import subprocess,json,hashlib,os
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'output/pdf/three_way_reciprocal_hierarchy_v0.1.pdf'
QA=Path(os.environ.get('THREEWAY2_QA','C:/TORMENT/TRIOCTAGON_new/publication_workspaces/three_way_hierarchy_20261005/qa'))
POP=Path(os.environ.get('THREEWAY2_PDFTOPPM','C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'))
QA.mkdir(parents=True,exist_ok=True)
count=len(PdfReader(PDF).pages)
subprocess.run([str(POP),'-r','110','-png',str(PDF),str(QA/'page')],check=True,capture_output=True)
pages=[QA/f'page-{i:02d}.png' for i in range(1,count+1)]
assert len(pages)==count,(len(pages),count)
for i in range(0,count,2):
    pics=[]
    for p in pages[i:i+2]:
        img=Image.open(p).convert('RGB');img.thumbnail((900,1275))
        tile=Image.new('RGB',(920,1310),'#e8eeee');tile.paste(img,((920-img.width)//2,25));ImageDraw.Draw(tile).text((12,5),p.stem,fill='black');pics.append(tile)
    sheet=Image.new('RGB',(920*len(pics),1310),'white')
    for j,im in enumerate(pics):sheet.paste(im,(920*j,0))
    sheet.save(QA/f'review-{i//2+1:02d}.jpg',quality=92)
record=dict(pdf_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),page_count=count,resolution_dpi=110,workspace=str(QA),page_pngs=[str(p) for p in pages],review_sheets=[str(QA/f'review-{i+1:02d}.jpg') for i in range((count+1)//2)],visual_review_status='pending human-readable image inspection by assistant')
(ROOT/'records/render_record.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(dict(pages=count,review_sheets=len(record['review_sheets']),workspace=str(QA)),indent=2))
