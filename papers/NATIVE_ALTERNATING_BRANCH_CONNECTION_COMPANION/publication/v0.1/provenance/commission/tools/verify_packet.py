#!/usr/bin/env python3
"""Check this commission's file identities only; never import scientific code."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(text: str) -> PurePosixPath:
    p = PurePosixPath(text)
    if p.is_absolute() or '..' in p.parts or '\\' in text or ':' in text:
        raise ValueError(f'Unsafe path: {text}')
    return p


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'PACKET_MANIFEST.json').read_text(encoding='utf-8'))
    rows = manifest['files']
    paths = [r['path'] for r in rows]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate manifest paths')
    wanted = set(paths) | {'PACKET_MANIFEST.json'}
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    if actual != wanted:
        raise ValueError(f'File-set mismatch: missing={sorted(wanted-actual)}, extra={sorted(actual-wanted)}')
    for r in rows:
        p = root.joinpath(*safe_relative(r['path']).parts)
        b = p.read_bytes()
        if len(b) != r['bytes'] or digest(b) != r['sha256']:
            raise ValueError(f'Identity mismatch: {r["path"]}')
    archive = root / 'archives' / 'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_GPT_ACCEPTANCE_PACKAGE.zip'
    expected = Path(str(archive) + '.sha256').read_text(encoding='utf-8').split()[0]
    if digest(archive.read_bytes()) != expected:
        raise ValueError('Acceptance archive checksum mismatch')
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or z.testzip() is not None:
            raise ValueError('Acceptance archive names or CRC failed')
        for name in names:
            safe_relative(name)
            if z.read(name) != root.joinpath('accepted', *PurePosixPath(name).parts).read_bytes():
                raise ValueError(f'Acceptance extraction mismatch: {name}')
    print(json.dumps({'status':'PASS','packet_files':len(wanted),
                      'preserved_acceptance_members':len(names),
                      'scientific_executions':0,
                      'scope':'File identities and archive integrity only'}, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
