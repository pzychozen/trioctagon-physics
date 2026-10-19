"""Read-only SHA-256 verification of the published historical companion."""
from pathlib import Path, PurePosixPath
import hashlib, json

def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'PUBLICATION_MANIFEST.json').read_text(encoding='utf8'))
    files = manifest['files']
    names = {row['path'] for row in files}
    assert len(names) == len(files)
    for row in files:
        name = row['path']
        assert not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts
        assert '\\' not in name and ':' not in name
        data = (root / name).read_bytes()
        assert len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256'], name
    checks = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf8').splitlines():
        digest, name = line.split('  ', 1)
        assert name not in checks and name in names | {'PUBLICATION_MANIFEST.json'}
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
        checks[name] = digest
    assert set(checks) == names | {'PUBLICATION_MANIFEST.json'}
    print('PASS:', len(files), 'payload identities and manifest checksum; no scientific code executed.')

if __name__ == '__main__':
    main()
