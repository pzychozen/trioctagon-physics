"""Read-only checks of the exact published edition; visual review is a separate record."""
from pathlib import Path
import hashlib,json,os,sys
from pypdf import PdfReader
base=Path(__file__).resolve().parent.parent
root=Path('\\\\?\\'+str(base)) if os.name=='nt' and not str(base).startswith('\\\\?\\') else base
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment','Use conda activate torment.'
receipt=json.loads((root/'verification/build/BUILD_RECEIPT.json').read_text(encoding='utf-8'))
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pdf=root/receipt['pdf_filename']
assert digest(pdf)==receipt['pdf_sha256']
for name,h in receipt['content'].items():assert digest(root/name)==h,name
reader=PdfReader(pdf)
assert len(reader.pages)==17
assert reader.metadata.title==receipt['title']
assert reader.metadata.author==receipt['author']
assert reader.metadata.subject==receipt['status']
for p in reader.pages:assert len(p.extract_text().strip())>100
ledger=json.loads((root/'provenance/CLAIM_SOURCE_LEDGER.json').read_text(encoding='utf-8'))
assert ledger['pdf_sha256']==receipt['pdf_sha256'] and len(ledger['items'])==11
for item in ledger['items']:
    for source in [item['accepted_proof']]+item['primary_source_locations']:
        assert digest(root/source['path'])==source['sha256'],source['path']
    for m in item['manuscript_locations']:
        path=root/m['source_file'];assert digest(path)==m['source_sha256']
        assert '\\label{'+m['label']+'}' in path.read_text(encoding='utf-8').splitlines()[m['line']-1]
print(json.dumps({'result':'PASS','pages':len(reader.pages),'pdf_sha256':receipt['pdf_sha256'],
    'scope':'Exact published bytes, metadata and current source locators; not a new visual inspection.'},indent=2))
