"""Compose already rendered PDF pages for layout review; outside the paper tree."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
from pypdf import PdfReader
import sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
WORK=Path('C:/TORMENT/TRIOCTAGON_new/publication_workspaces/three_way_reconstruction_20261005')
r=PdfReader(ROOT/'output/pdf/three_way_reconstruction_v0.1.pdf')
imgs=sorted((WORK/'rendered').glob('page-*.png'))[:len(r.pages)]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for start in range(0,len(imgs),6):
    sheet=Image.new('RGB',(1560,1500),'#e7e9ec');d=ImageDraw.Draw(sheet)
    for k,p in enumerate(imgs[start:start+6]):
        im=Image.open(p).convert('RGB');im.thumbnail((490,700))
        xx=15+(k%3)*520;yy=12+(k//3)*750
        d.text((xx,yy),f'PDF page {start+k+1}',font=font,fill='black')
        sheet.paste(im,(xx,yy+27))
    sheet.save(WORK/f'review_{start+1:02d}_{min(start+6,len(imgs)):02d}.png')
for i,p in enumerate(r.pages):
    txt=(p.extract_text() or '').replace('\n',' ')
    print(f'{i+1:02d} ({len(txt)} chars) '+txt[:190])
