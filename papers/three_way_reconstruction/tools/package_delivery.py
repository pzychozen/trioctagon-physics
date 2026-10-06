"""Package this local draft and verify every ZIP member; do not publish it."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output/three_way_reconstruction_v0.1_bundle.zip'

files = sorted(
    p for p in ROOT.rglob('*')
    if p.is_file()
    and p != OUTPUT
    and p != ROOT / 'records/artifact_manifest.json'
    and '__pycache__' not in p.parts
)
manifest = {
    p.relative_to(ROOT).as_posix(): {
        'bytes': p.stat().st_size,
        'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    }
    for p in files
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for p in files:
        archive.write(p, p.relative_to(ROOT).as_posix())
    archive.writestr('BUNDLE_CONTENTS_SHA256.json', json.dumps(manifest, indent=2))

with zipfile.ZipFile(OUTPUT) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(manifest) + 1
    for name, entry in manifest.items():
        data = archive.read(name)
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256']

print(json.dumps({'bundle': str(OUTPUT), 'verified_files': len(manifest),
                  'bytes': OUTPUT.stat().st_size,
                  'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}, indent=2))
