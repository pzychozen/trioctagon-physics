from pathlib import Path
from pypdf import PdfReader
import json
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'provenance/extracted';out.mkdir(exist_ok=True)
result=[]
for p in sorted((ROOT/'provenance/historical').rglob('*.pdf')):
    r=PdfReader(p);text='\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+(pg.extract_text() or '') for i,pg in enumerate(r.pages))
    code=p.parent.name;(out/f'{code}.txt').write_text(text,encoding='utf-8')
    result.append(dict(id=code,pages=len(r.pages),file=str(p.relative_to(ROOT))))
(out/'page_counts.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
