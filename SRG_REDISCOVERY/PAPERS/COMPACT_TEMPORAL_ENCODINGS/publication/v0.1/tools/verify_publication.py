"""Read-only checks for the published manuscript assets; no scientific execution."""
from pathlib import Path, PurePosixPath
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    manifest_bytes = (ROOT / 'PUBLICATION_MANIFEST.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    files = manifest['files']
    expected = {r['path']: r for r in files}
    assert len(expected) == len(files), 'Duplicate manifest paths'
    for name, row in expected.items():
        path = PurePosixPath(name)
        assert not path.is_absolute() and '..' not in path.parts and '\\' not in name and ':' not in name
        data = (ROOT / name).read_bytes()
        assert len(data) == row['bytes'] and digest(data) == row['sha256'], name
    checksum_rows = (ROOT / 'SHA256SUMS.txt').read_text(encoding='utf8').splitlines()
    checked = {}
    for line in checksum_rows:
        checksum, name = line.split('  ', 1)
        assert name not in checked
        assert name in expected or name == 'PUBLICATION_MANIFEST.json'
        assert digest((ROOT / name).read_bytes()) == checksum, name
        checked[name] = checksum
    assert set(checked) == set(expected) | {'PUBLICATION_MANIFEST.json'}
    claims = json.loads((ROOT / 'CLAIM_LOCATOR.json').read_text(encoding='utf8'))
    assert len(claims['claims']) == 14 and len({r['claim_id'] for r in claims['claims']}) == 14
    assert claims['pdf_sha256'] == manifest['accepted_pdf']['sha256']
    tex = '\n'.join(p.read_text(encoding='utf8') for p in ROOT.glob('*.tex'))
    for claim in claims['claims']:
        assert claim['manuscript_locations']
        for loc in claim['manuscript_locations']:
            assert 1 <= loc['page'] <= 28
            assert '\\label{' + loc['label'] + '}' in tex
    print('PASS:', len(files), 'payload files; manifest checksum; 14 manuscript claim locators.')
    print('Accepted PDF SHA-256:', manifest['accepted_pdf']['sha256'])

if __name__ == '__main__':
    main()
