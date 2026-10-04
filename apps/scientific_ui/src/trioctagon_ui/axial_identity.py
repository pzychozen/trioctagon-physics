"""Observe installed kernel bytes/origins; never import scientific-private owners."""
import hashlib
from importlib import metadata
from importlib.util import find_spec
import json
from pathlib import Path
import platform
import sys

KERNEL_COMMIT = '3f42d4e56afd973c397ce4c557b66183a71a6044'
LOCK_SHA256 = 'b6cbdf8d5f4e17f32cafd411bfd400d477eb26cb8a7f543ea740ee61551e07f1'
OBSERVATION_API = '1.0.0'
REVISION = 'AXIAL_M1_V1'


def admitted_lock():
    dist = metadata.distribution('trioctagon-scientific-ui')
    matches = [p for p in dist.files or () if str(p).replace('\\', '/').endswith('share/trioctagon-scientific-ui/kernel-artifact.lock.json')]
    if len(matches) != 1: raise ValueError('Axial kernel lock missing/ambiguous')
    raw = Path(dist.locate_file(matches[0])).read_bytes()
    if hashlib.sha256(raw).hexdigest() != LOCK_SHA256: raise ValueError('Stale or changed axial kernel lock')
    lock = json.loads(raw)
    if lock['source_commit'] != KERNEL_COMMIT or lock['version'] != '0.2.0': raise ValueError('Wrong axial kernel source/version')
    return lock


def verify_installed_axial():
    lock = admitted_lock()
    dist = metadata.distribution('trioctagon-physics')
    if dist.version != '0.2.0': raise ValueError('Installed axial kernel version mismatch')
    root = Path(dist.locate_file('kernel_physics')).resolve()
    spec = find_spec('kernel_physics')
    if spec is None or Path(spec.origin or '').resolve() != root / '__init__.py' or tuple(Path(p).resolve() for p in spec.submodule_search_locations or ()) != (root,):
        raise ValueError('Kernel import origin differs from admitted installed distribution')
    members = {}; origins = {}; expected_package = set()
    for row in lock['wheel_equivalence']['stable_members']:
        path = Path(dist.locate_file(row['path']))
        try: raw = path.read_bytes()
        except OSError as exc: raise ValueError('Missing installed kernel member: ' + row['path']) from exc
        digest = hashlib.sha256(raw).hexdigest()
        if len(raw) != row['size'] or digest != row['sha256']: raise ValueError('Installed kernel member mismatch: ' + row['path'])
        if row['path'].startswith('kernel_physics/'):
            expected_package.add(path.resolve())
            if path.suffix == '.py': members[row['path']] = digest; origins[row['path']] = str(path.resolve())
    if len(members) != 20 or {p.resolve() for p in root.rglob('*') if p.is_file()} != expected_package:
        raise ValueError('Installed axial kernel runtime closure mismatch')
    for name, module in tuple(sys.modules.items()):
        if name == 'kernel_physics' or name.startswith('kernel_physics.'):
            if Path(getattr(module, '__file__', '')).resolve() not in expected_package:
                raise ValueError('Loaded kernel module has an unapproved origin')
    manifest = json.loads((root / '_distribution_provenance.json').read_bytes())
    if manifest['source']['commit'] != KERNEL_COMMIT or manifest['source']['tracked_dirty'] or manifest['software']['package_version'] != '0.2.0' or manifest['build_input_sha256'] != lock['manifest_build_input_sha256']:
        raise ValueError('Installed axial provenance/source mismatch')
    return {'distribution': 'trioctagon-physics', 'version': dist.version, 'source_commit': KERNEL_COMMIT,
            'build_input_sha256': manifest['build_input_sha256'], 'lock_sha256': LOCK_SHA256,
            'installed_owner_sha256': members['kernel_physics/axial_observables.py'],
            'installed_facade_sha256': members['kernel_physics/api.py'],
            'scientific_dependencies': [{'path': p, 'sha256': h} for p, h in sorted(members.items())],
            'installed_origins': origins,
            'environment': {'python': platform.python_version(), 'platform': platform.platform(),
                            **{p: metadata.version(p) for p in ('numpy', 'sympy', 'mpmath')}},
            'verification': 'OBSERVED_INSTALLED_BYTES_NOT_EXTERNAL_ATTESTATION'}
