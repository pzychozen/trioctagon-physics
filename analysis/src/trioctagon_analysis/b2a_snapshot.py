"""PROOF_INFRASTRUCTURE: closed B2A snapshot admission for validation only.

No function here approves an arbitrary installation by hashing that installation.
Deployment pins must be retained separately from the candidate directory.
This machinery does not establish certified Windows binding or enable issuance.
"""
from contextlib import ExitStack
import hashlib
import os
from pathlib import Path, PureWindowsPath
import re
import shutil
import stat
import uuid

from . import schema as s
from .b2a_windows import ReadLease, final_path, set_dacl
from .errors import require


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_member(path):
    require(type(path) is str and path and '\\' not in path and ':' not in path and
            not PureWindowsPath(path).is_absolute(), 'WRONG_PRODUCER', 'unsafe snapshot member')
    for part in path.split('/'):
        require(part not in ('', '.', '..') and part == part.rstrip(' .') and
                not any(ord(c) < 32 for c in part) and
                not re.fullmatch(r'(?i)(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?', part),
                'WRONG_PRODUCER', 'Windows member alias prohibited')
    require(not path.lower().endswith(('.pth', '.egg-link', '.pyc')) and
            '/__pycache__/' not in '/' + path.lower(),
            'WRONG_PRODUCER', 'startup/editable/cache member prohibited')


class SnapshotExpectation(s.Document):
    """Artifact-derived proof expectation. Its digest needs an external pin."""
    __slots__ = ()
    schema = s.obj(family=s.literal('TRIOCTAGON_B2A_SNAPSHOT_EXPECTATION'), version=s.literal(1),
        mode=s.literal('B2A_VALIDATION_ONLY'), analysis_version=s.literal('0.1.0'),
        provider=s.literal('trioctagon_analysis.provider:copy_recorded'),
        kernel_archive=s.hex256, kernel_lock=s.hex256,
        archives=s.seq(s.obj(name=s.text, sha256=s.hex256, authority=s.text), 1),
        members=s.seq(s.obj(path=s.text, size=s.integer, sha256=s.hex256,
                           authority=s.text), 1),
        os_members=s.seq(s.obj(path=s.text, size=s.integer, sha256=s.hex256), 1),
        runtime=s.literal('runtime/pythonw.exe'),
        worker=s.literal('site/trioctagon_analysis/b2a_worker.py'),
        import_paths=s.seq(s.text, 3, 3),
        qualification=s.literal('HASH != SIGNATURE; HASH != AUTHORSHIP; B2A PROOF ONLY'))

    @classmethod
    def validate(cls, value):
        paths = [row['path'] for row in value['members']]
        require(paths == sorted(set(paths)) and len({p.casefold() for p in paths}) == len(paths),
                'WRONG_PRODUCER', 'duplicate/case-aliased member')
        for path in paths:
            safe_member(path)
        os_paths = [row['path'] for row in value['os_members']]
        require(len({p.casefold() for p in os_paths}) == len(os_paths) and
                all(PureWindowsPath(p).is_absolute() and '..' not in PureWindowsPath(p).parts
                    for p in os_paths), 'WRONG_PRODUCER', 'invalid pinned OS member identities')
        require(value['runtime'] in paths and value['worker'] in paths and
                'runtime/python311._pth' in paths and
                value['import_paths'] == ['runtime/Lib', 'runtime/DLLs', 'site'],
                'WRONG_PRODUCER', 'fixed launch/import closure is incomplete')


def admit_expectation(raw, expected_sha256, limits):
    require(type(expected_sha256) is str and sha(raw) == expected_sha256,
            'AUTHORITY_MISMATCH', 'expected manifest lacks an independent matching pin')
    manifest = SnapshotExpectation.from_bytes(raw, limits)
    require(manifest.to_bytes() == raw, 'INVALID_CODEC', 'expectation must be canonical')
    return manifest


def regular_tree(root):
    root = Path(root).absolute()
    require(root.is_dir() and root.resolve() == root, 'WRONG_PRODUCER', 'absolute unaliased directory required')
    require(not any((p/'.git').exists() for p in (root, *root.parents)),
            'WRONG_PRODUCER', 'B2A candidates/snapshots must be outside a checkout')
    for p in (root, *root.parents):
        require(not p.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT,
                'WRONG_PRODUCER', 'reparse ancestor prohibited')
    result = {}
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs + files:
            p = Path(directory)/name
            info = p.lstat()
            require(not info.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT,
                    'WRONG_PRODUCER', 'reparse member prohibited')
            if p.is_file():
                require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
                        'WRONG_PRODUCER', 'hard-link/nonregular member prohibited')
                key = p.relative_to(root).as_posix()
                safe_member(key)
                result[key] = p
    return result


def verify_tree(root, manifest):
    require(type(manifest) is SnapshotExpectation, 'AUTHORITY_MISMATCH', 'typed pinned expectation required')
    actual = regular_tree(root)
    expected = {row['path']: row for row in manifest.to_dict()['members']}
    require(set(actual) == set(expected), 'WRONG_PRODUCER', 'snapshot member set mismatch')
    expected_dirs = {parent.as_posix() for name in expected for parent in Path(name).parents
                     if parent != Path('.')}
    actual_dirs = {p.relative_to(root).as_posix() for p in Path(root).rglob('*') if p.is_dir()}
    require(actual_dirs == expected_dirs, 'WRONG_PRODUCER', 'snapshot directory set mismatch')
    for name, p in actual.items():
        raw = p.read_bytes()
        require(len(raw) == expected[name]['size'] and sha(raw) == expected[name]['sha256'],
                'WRONG_PRODUCER', 'snapshot member bytes mismatch: ' + name)
    require((Path(root)/'runtime/python311._pth').read_bytes() == b'Lib\nDLLs\n../site\n',
            'WRONG_PRODUCER', 'unchecked interpreter startup configuration')
    return actual


class FrozenSnapshot:
    """Fresh copied tree; frozen DACLs plus retained no-write/no-delete handles.

    Callers must preserve leases until the job exits. Only owned staging DACLs
    are changed. Cleanup failure propagates; it cannot yield proof success.
    """
    def __init__(self, source, staging, manifest, app_sid):
        self.id = uuid.uuid4().hex
        self.staging = Path(staging).resolve()
        require(not any((p/'.git').exists() for p in (self.staging, *self.staging.parents)),
                'WRONG_PRODUCER', 'B2A staging must be outside a checkout')
        self.root = self.staging/('snapshot-' + self.id)
        self.manifest, self.app_sid = manifest, app_sid
        self.stack = ExitStack()
        self.frozen = False
        source = Path(source).absolute()
        verify_tree(source, manifest)
        require(not self.root.exists(), 'WRONG_PRODUCER', 'snapshot must be fresh')
        self.root.mkdir()
        try:
            # Copy each checked member through a no-write/no-delete source lease.
            for row in manifest.to_dict()['members']:
                name = row['path']
                p = source/name
                with ReadLease(p):
                    raw = p.read_bytes()
                    require(sha(raw) == row['sha256'], 'WRONG_PRODUCER', 'source changed during copy')
                    dest = self.root/name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(raw)
            self.freeze()
        except BaseException:
            self.close()
            raise

    def freeze(self):
        for p in sorted(self.root.rglob('*'), key=lambda p: len(p.parts), reverse=True):
            set_dacl(p, self.app_sid)
        set_dacl(self.root, self.app_sid)
        for p in [self.root, *self.root.rglob('*')]:
            lease = self.stack.enter_context(ReadLease(p, directory=p.is_dir()))
            require(final_path(lease.handle) == p, 'WRONG_PRODUCER', 'leased path alias')
        verify_tree(self.root, self.manifest)
        self.frozen = True

    def verify_after(self):
        require(self.frozen, 'UNVERIFIED_PRODUCER', 'snapshot protection unavailable')
        verify_tree(self.root, self.manifest)

    def close(self):
        self.stack.close()
        self.frozen = False
        if self.root.exists():
            # Exact owned UUID directory only; no original/candidate tree cleanup.
            require(self.root.name == 'snapshot-' + self.id and self.root.parent == self.staging and
                    self.root.resolve() == self.root and self.root.is_relative_to(self.staging),
                    'PERSISTENCE_FAILURE', 'cleanup target mismatch')
            for p in self.root.rglob('*'):
                require(not p.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT,
                        'PERSISTENCE_FAILURE', 'cleanup refuses reparse member')
                set_dacl(p, writable=True)
            set_dacl(self.root, writable=True)
            shutil.rmtree(self.root)

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        self.close()
