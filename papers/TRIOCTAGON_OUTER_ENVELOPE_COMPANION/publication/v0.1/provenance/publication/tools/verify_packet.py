"""Verify this self-contained publication packet; no scientific execution."""
from pathlib import Path, PurePosixPath
import hashlib,json
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'PACKET_MANIFEST.json').read_text('utf-8'))
expected={x['path'] for x in m['files']}
actual={p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and p.name!='PACKET_MANIFEST.json' and '__pycache__' not in p.parts}
if actual!=expected: raise RuntimeError('Packet member set mismatch')
for x in m['files']:
 p=PurePosixPath(x['path'])
 if p.is_absolute() or '..' in p.parts: raise RuntimeError('Unsafe path')
 b=(r/x['path']).read_bytes()
 if len(b)!=x['bytes'] or hashlib.sha256(b).hexdigest()!=x['sha256']: raise RuntimeError('Identity mismatch: '+x['path'])
print('PASS:',len(expected),'manifest-listed packet files; author activation still required before publication.')
