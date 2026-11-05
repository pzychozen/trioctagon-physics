"""Read-only integrity check. Does not execute scientific code or use the network."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    posix = PurePosixPath(relative)
    if posix.is_absolute() or '..' in posix.parts or '\\' in relative:
        raise ValueError(f'Unsafe manifest path: {relative}')
    path = root.joinpath(*posix.parts)
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Missing or non-regular file: {relative}')
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path outside packet: {relative}')
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root/'PACKET_MANIFEST.json').read_text(encoding='utf-8'))
    records = manifest['files']
    names = [r['path'] for r in records]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate manifest path')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    expected = set(names) | {'PACKET_MANIFEST.json'}
    if actual != expected:
        raise ValueError(f'Packet membership differs: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}')
    for r in records:
        data = safe_path(root, r['path']).read_bytes()
        if len(data) != r['bytes'] or digest(data) != r['sha256']:
            raise ValueError(f'Identity mismatch: {r["path"]}')
    sources = json.loads((root/'provenance/SELECTED_SOURCE_IDENTITIES.json').read_text(encoding='utf-8'))
    for r in sources['source_records']:
        data = safe_path(root, r['packet_path']).read_bytes()
        if len(data) != r['bytes'] or digest(data) != r['sha256']:
            raise ValueError(f'Source identity mismatch: {r["packet_path"]}')
    print(json.dumps({'status':'PASS','manifest_payloads':len(records),'selected_source_files':len(sources['source_records']),'scientific_execution':False},indent=2))


if __name__ == '__main__':
    main()
