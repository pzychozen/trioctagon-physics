"""Read-only documentary integrity checks. Does not run mathematical verifiers."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import sys
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def fail(message: str) -> None:
    raise ValueError(message)

def safe_relative(name: str) -> Path:
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name:
        fail('Unsafe relative path: '+name)
    return Path(*p.parts)

def main() -> None:
    manifest=json.loads((ROOT/'PACKET_MANIFEST.json').read_bytes())
    listed=manifest['files']
    names=[r['path'] for r in listed]
    if len(set(names))!=len(names) or len({n.casefold() for n in names})!=len(names):
        fail('Duplicate or case-colliding manifest path')
    for row in listed:
        p=ROOT/safe_relative(row['path'])
        if p.is_symlink() or not p.is_file():
            fail('Missing file or symlink: '+row['path'])
        data=p.read_bytes()
        if len(data)!=row['bytes'] or digest(data)!=row['sha256']:
            fail('Raw byte mismatch: '+row['path'])
    state=json.loads((ROOT/'COMMISSION_STATUS.json').read_bytes())
    ap=ROOT/safe_relative(state['acceptance_archive']['path'])
    ar=ap.read_bytes()
    if digest(ar)!=state['acceptance_archive']['sha256']:
        fail('Acceptance ZIP identity mismatch')
    side=(ROOT/(str(safe_relative(state['acceptance_archive']['path']))+'.sha256')).read_text(encoding='utf-8').split()[0]
    if side!=digest(ar):
        fail('Acceptance sidecar mismatch')
    with ZipFile(ap) as z:
        infos=z.infolist()
        znames=[i.filename for i in infos]
        if len(znames)!=len(set(znames)) or len(znames)!=len({n.casefold() for n in znames}):
            fail('Acceptance ZIP duplicate path')
        if len(znames)!=state['acceptance_archive']['members']:
            fail('Acceptance member count mismatch')
        if z.testzip() is not None:
            fail('Acceptance CRC failure')
        am=json.loads(z.read('ACCEPTANCE_MANIFEST.json'))
        lookup={r['path']:r for r in am['files']}
        if set(lookup)!=set(znames)-{'ACCEPTANCE_MANIFEST.json'}:
            fail('Acceptance manifest coverage mismatch')
        for info in infos:
            rel=safe_relative(info.filename)
            if stat.S_ISLNK(info.external_attr>>16):
                fail('Acceptance archive symlink')
            data=z.read(info.filename)
            if info.filename in lookup:
                r=lookup[info.filename]
                if len(data)!=r['bytes'] or digest(data)!=r['sha256']:
                    fail('Acceptance internal identity mismatch: '+info.filename)
            if data!=(ROOT/'evidence'/'outer_envelope'/rel).read_bytes():
                fail('Acceptance extraction differs: '+info.filename)
    print(json.dumps({
        'status':'PASS','packet_manifest_entries':len(listed),
        'preserved_acceptance_members':len(znames),
        'acceptance_zip_sha256':digest(ar),
        'scope':'Raw-byte identities, paths, archive CRC and unchanged extraction only',
        'scientific_scripts_run':False,'files_modified':False
    },indent=2))

if __name__=='__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
