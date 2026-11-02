"""Verify all frozen edition payload bytes; no build or scientific execution."""
import hashlib
import json
from pathlib import Path, PurePosixPath

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'PAYLOAD_MANIFEST.json').read_text(encoding='utf-8'))
names = set()
for entry in manifest['files']:
    name = entry['path']
    path = PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts and ':' not in name
    assert name not in names
    names.add(name)
    data = (root / name).read_bytes()
    assert len(data) == entry['bytes'], name + ': byte-length mismatch'
    assert hashlib.sha256(data).hexdigest() == entry['sha256'], name + ': SHA-256 mismatch'
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
assert actual == names | {'PAYLOAD_MANIFEST.json'}, 'Unexpected or missing edition file'
print(json.dumps({'status': 'PASS', 'hashed_payload_files': len(names), 'manifest_excludes_itself': True}, indent=2))
