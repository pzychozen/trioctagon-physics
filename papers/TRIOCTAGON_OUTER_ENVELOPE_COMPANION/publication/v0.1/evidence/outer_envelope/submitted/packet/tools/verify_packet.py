"""Check packet raw-byte identities only. This is not a scientific checker."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

def main() -> None:
    root=Path(__file__).resolve().parents[1]
    records=json.loads((root/'PACKET_MANIFEST.json').read_text(encoding='utf-8'))['files']
    expected={r['path'] for r in records}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='PACKET_MANIFEST.json'}
    if actual!=expected: raise SystemExit('File-set mismatch: '+repr(actual^expected))
    for r in records:
        p=root/r['path'];data=p.read_bytes()
        if len(data)!=r['bytes'] or hashlib.sha256(data).hexdigest()!=r['sha256']:
            raise SystemExit('Identity mismatch: '+r['path'])
    print(f'PASS: {len(records)} raw-byte entries; manifest self-excluded. No mathematics executed.')
if __name__=='__main__': main()
