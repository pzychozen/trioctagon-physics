"""Structural/text QA of the generated document, not a scientific checker."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.append(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages')
import pypdf
reader=pypdf.PdfReader(str(ROOT/'manuscript/REVIEW.pdf'))
pages=[]; texts=[]; internal=0; external=0
for n,page in enumerate(reader.pages,1):
    text=page.extract_text()
    texts.append(f'=== PAGE {n} ===\n'+text)
    ann=page.get('/Annots',[])
    for ref in ann:
        item=ref.get_object()
        if '/Dest' in item:
            dest=item['/Dest']; assert len(dest)>=2
            internal+=1
        elif '/A' in item:
            uri=str(item['/A'].get('/URI',''))
            assert uri.startswith('../EVIDENCE_INDEX.md#'),uri
            external+=1
    assert len(text.strip())>100
    assert '\ufffd' not in text
    pages.append({'page':n,'text_characters':len(text),'annotations':len(ann)})
(ROOT/'qa/REVIEW_EXTRACTED.txt').write_text('\n\n'.join(texts),encoding='utf-8')
out={'pages':len(pages),'page_details':pages,'internal_links':internal,'relative_evidence_links':external,
     'text_extractor':'pypdf '+pypdf.__version__,'pdf_sha256':hashlib.sha256((ROOT/'manuscript/REVIEW.pdf').read_bytes()).hexdigest(),
     'limitation':'Mathematics is rendered as high-resolution images; source expressions are in main.tex/content.py. Text extraction does not validate math images.'}
(ROOT/'qa/PDF_STRUCTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='page_details'},indent=2))
