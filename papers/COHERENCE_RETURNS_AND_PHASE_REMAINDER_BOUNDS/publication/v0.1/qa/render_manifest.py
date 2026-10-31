"""Record page-image hashes before/after a layout correction."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
out={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'qa').glob('page-*.png'))}
target=ROOT/'qa'/('RENDER_'+sys.argv[1]+'.json')
target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if sys.argv[1]=='FINAL':
    before=json.loads((ROOT/'qa/RENDER_BEFORE_LAST.json').read_text())
    print('Pages changed since preceding render:',[n for n,h in out.items() if before.get(n)!=h])
print('Rendered pages:',len(out))
