"""Two-pass archive creation and complete reopening audit; no scientific runs.

The first audit is included in the final review. The external final audit and
checksum bind every final member without a self-referential archive hash.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib, json, os, sys, zipfile

R = Path(__file__).resolve().parents[1]
D = R.parent / 'delivery_20261110_01'
NAME = 'NATIVE_TURNING_CAPTURE_01_REVIEW.zip'
assert os.environ.get('CONDA_DEFAULT_ENV') == 'torment' and sys.flags.optimize == 0

def now(): return datetime.now(timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def write(p, obj): p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def files(excluded=()):
    result = []
    for p in sorted(R.rglob('*')):
        if not p.is_file(): continue
        assert not p.is_symlink() and p.resolve().is_relative_to(R.resolve())
        name = p.relative_to(R).as_posix()
        assert '__pycache__' not in p.parts and p.suffix != '.pyc'
        if name in excluded: continue
        b = p.read_bytes()
        result.append({'path': name, 'bytes': len(b), 'sha256': sha(b)})
    return result
def archive(target, entries, mode):
    with zipfile.ZipFile(target, mode, compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for item in entries:
            b = (R / item['path']).read_bytes()
            assert len(b) == item['bytes'] and sha(b) == item['sha256']
            info = zipfile.ZipInfo(item['path'], date_time=(2026, 11, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3; info.external_attr = 0o100644 << 16
            z.writestr(info, b, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
def reopen(target, entries):
    expected = {x['path']: x for x in entries}; checked = []
    with zipfile.ZipFile(target, 'r') as z:
        names = z.namelist()
        assert len(names) == len(set(names)) == len({n.casefold() for n in names})
        assert set(names) == set(expected)
        for name in names:
            p = PurePosixPath(name)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name
            b = z.read(name)  # Reopens/decompresses each member and validates its ZIP CRC.
            local = (R / name).read_bytes(); item = expected[name]
            assert b == local and len(b) == item['bytes'] and sha(b) == item['sha256']
            checked.append({'path': name, 'bytes': len(b), 'sha256': sha(b), 'crc_and_bytes_verified': True})
    return checked

started = now()
assert not D.exists(), 'Preserve any earlier delivery; choose a new delivery directory instead of overwriting it'
assert not (R / 'REVIEW_MANIFEST.json').exists() and not (R / 'DELIVERY_AUDIT.json').exists()
D.mkdir()
target = D / NAME
payload = files()
for required in ['NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md', 'RESULT_SUMMARY.md', 'PRIOR_WORK_COMPARISON.md',
                 'CLAIM_LEDGER.json', 'SOURCE_IDENTITIES.json', 'scripts/check_certificate.py', 'data/CERTIFICATE.json',
                 'logs/PRESERVATION_AUDIT.json']:
    assert required in {x['path'] for x in payload}
archive(target, payload, 'x')
initial_members = reopen(target, payload)
write(R / 'DELIVERY_AUDIT.json', {
    'status': 'PASS', 'checked_utc': now(), 'kind': 'Preseal archive member audit, included in final archive',
    'member_count': len(initial_members), 'members': initial_members,
    'scope': 'Every member of the preliminary payload archive was reopened and checked against source bytes and SHA-256; ZIP CRC checked during reading.',
    'not_yet_present_in_this_pass': ['DELIVERY_AUDIT.json', 'REVIEW_MANIFEST.json'],
    'final_seal': 'The external NATIVE_TURNING_CAPTURE_01_FINAL_DELIVERY_AUDIT.json separately verifies every member of the final ZIP, including this audit and its manifest.',
    'scientific_theorem_count': 0})
manifest_entries = files(excluded=['REVIEW_MANIFEST.json'])
write(R / 'REVIEW_MANIFEST.json', {'task': 'NATIVE_TURNING_CAPTURE_01', 'created_utc': now(),
      'self_excluded': 'REVIEW_MANIFEST.json', 'files': manifest_entries})
final_entries = files()
# This overwrites only the preliminary archive just created by this invocation.
archive(target, final_entries, 'w')
final_members = reopen(target, final_entries)
with zipfile.ZipFile(target) as z:
    embedded = json.loads(z.read('REVIEW_MANIFEST.json'))
    assert set(z.namelist()) == {x['path'] for x in embedded['files']} | {'REVIEW_MANIFEST.json'}
    for item in embedded['files']:
        b = z.read(item['path']); assert len(b) == item['bytes'] and sha(b) == item['sha256']
digest = sha(target.read_bytes())
sidecar = D / (NAME + '.sha256')
sidecar.write_text(digest + '  ' + NAME + '\n', encoding='ascii')
assert sidecar.read_text().split()[0] == sha(target.read_bytes())
finished = now()
write(D / 'NATIVE_TURNING_CAPTURE_01_FINAL_DELIVERY_AUDIT.json', {
    'status': 'PASS', 'started_utc': started, 'finished_utc': finished,
    'command_prompt_invocation': r'run_python.cmd scripts\package_review.py',
    'python': sys.executable, 'python_argv': sys.argv, 'conda_environment': os.environ['CONDA_DEFAULT_ENV'],
    'script_sha256': sha(Path(__file__).read_bytes()),
    'archive': str(target), 'archive_bytes': target.stat().st_size, 'archive_sha256': digest,
    'sidecar': str(sidecar), 'sidecar_matches': True,
    'all_final_members_reopened': True, 'member_count': len(final_members), 'members': final_members,
    'self_excluding_manifest_verified': True, 'archive_names_unique_and_safe': True,
    'scope': 'Complete final ZIP bytes and CRC/SHA-256/source-byte checks for every member, including the preseal audit and final self-excluding manifest.',
    'scientific_theorem_count': 0})
summary = {'status': 'PASS', 'archive': str(target), 'archive_bytes': target.stat().st_size,
           'sha256': digest, 'final_members_verified': len(final_members), 'manifest_entries_verified': len(manifest_entries),
           'external_final_audit': str(D / 'NATIVE_TURNING_CAPTURE_01_FINAL_DELIVERY_AUDIT.json')}
output = json.dumps(summary, indent=2) + '\n'
(D / 'packaging.stdout.txt').write_text(output, encoding='utf-8')
print(output, end='')
