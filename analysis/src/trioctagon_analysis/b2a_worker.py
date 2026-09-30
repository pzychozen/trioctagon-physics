"""PROOF_INFRASTRUCTURE: fixed B2A structural-copy validation worker.

Output is unverified proof data, never a production DerivedAnalysisRecord.
It cannot approve itself or activate normal production issuance.
"""
import hashlib
import importlib.machinery
import json
import os
from pathlib import Path
import sys
import time


def main():
    expectation_path, request_path, parent_path, output_path, nonce = map(str, sys.argv[1:])
    root = Path(__file__).resolve().parents[2]
    expectation = json.loads(Path(expectation_path).read_bytes())
    members = {row['path']: row for row in expectation['members']}
    paths = [str(root/p) for p in expectation['import_paths']]
    if list(map(os.path.normcase, sys.path)) != list(map(os.path.normcase, paths)):
        raise RuntimeError('unexpected startup import path')
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.ignore_environment):
        raise RuntimeError('interpreter isolation flags missing')
    if 'site' in sys.modules or 'sitecustomize' in sys.modules or 'usercustomize' in sys.modules:
        raise RuntimeError('unexpected startup hook')
    output = Path(output_path).absolute()
    admitted = {os.path.normcase(str(root/name)) for name in members}
    origins = {}

    def check_origin(name, origin):
        if origin in ('built-in', 'frozen'):
            origins[name] = origin
        elif origin is None:
            raise RuntimeError('namespace/unidentified module prohibited: ' + name)
        else:
            p = Path(origin).absolute()
            if os.path.normcase(str(p)) not in admitted or p.resolve() != p:
                raise RuntimeError('unadmitted import origin: ' + name + ' ' + str(p))
            row = members[p.relative_to(root).as_posix()]
            if hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
                raise RuntimeError('import bytes changed: ' + name)
            origins[name] = p.relative_to(root).as_posix()

    class ClosedFinder:
        @staticmethod
        def find_spec(fullname, path=None, target=None):
            spec = importlib.machinery.PathFinder.find_spec(fullname, path, target)
            if spec is None:
                return None
            check_origin(fullname, spec.origin)
            if spec.submodule_search_locations is not None:
                for location in spec.submodule_search_locations:
                    if not Path(location).resolve().is_relative_to(root):
                        raise RuntimeError('unadmitted package search path')
            return spec

    sys.meta_path[:] = [importlib.machinery.BuiltinImporter,
                        importlib.machinery.FrozenImporter, ClosedFinder]

    def audit(event, args):
        if event.startswith(('socket.', 'subprocess.', 'os.exec', 'os.spawn', 'os.posix_spawn')) or event == 'os.system':
            raise PermissionError('B2A forbidden effect: ' + event)
        if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
            mode, flags = args[1], args[2]
            writing = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writing and Path(os.fsdecode(args[0])).absolute() != output:
                raise PermissionError('B2A write outside observation file')
        if event in ('os.remove', 'os.rename', 'os.rmdir', 'os.mkdir', 'os.chmod'):
            raise PermissionError('B2A filesystem mutation prohibited')

    sys.addaudithook(audit)
    for name, module in list(sys.modules.items()):
        if name == '__main__':
            check_origin(name, __file__)
        elif getattr(module, '__spec__', None) is not None:
            check_origin(name, module.__spec__.origin)

    from trioctagon_analysis.codec import ParseLimits
    from trioctagon_analysis.provider import ParentLoadLimits, ParentSnapshot, copy_recorded
    from trioctagon_analysis.requests import Request, Selection
    started = time.perf_counter()
    request = Request.from_bytes(Path(request_path).read_bytes(), ParseLimits(131072, 16))
    parent = ParentSnapshot(Path(parent_path).read_bytes(), ParentLoadLimits(ParseLimits(67108864, 16), 40000))
    parent.require_reference(type(parent.reference)(request.to_dict()['parents'][0]))
    loaded = time.perf_counter()
    payload = copy_recorded(parent, Selection(request.to_dict()['selection']))
    copied = time.perf_counter()
    for name, module in list(sys.modules.items()):
        spec = getattr(module, '__spec__', None)
        if spec is not None:
            check_origin(name, spec.origin)
    result = {'family': 'TRIOCTAGON_B2A_WORKER_OBSERVATION', 'mode': 'B2A_VALIDATION_ONLY',
        'provider': 'trioctagon_analysis.provider:copy_recorded',
        'entry_origin': str(Path(copy_recorded.__code__.co_filename).resolve()),
        'request': request.identity.to_dict(), 'attempt_nonce': nonce,
        'snapshot': root.name, 'runtime': sys.executable, 'origins': origins,
        'kernel_role': 'parent_validation', 'scientific_recomputation': 'NOT_PERFORMED',
        'payload': payload.to_dict(), 'payload_digest': payload.identity.to_dict(),
        'public_load_nanoseconds': int((loaded-started)*1e9),
        'copy_nanoseconds': int((copied-loaded)*1e9),
        'producer_verified': False}
    raw = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    if len(raw) > 131072:
        raise RuntimeError('B2A provisional observation output budget exceeded')
    with output.open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


if __name__ == '__main__':
    main()
