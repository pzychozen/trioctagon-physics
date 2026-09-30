"""EVIDENCE_ONLY_COORDINATOR: disabled B2A native-image admission prototype.

WINDOWS_EXECUTION_BINDING = NOT_PROVEN; PRODUCTION_ATTESTATION_ENABLED = NO.
Never returns a DerivedAnalysisRecord or activates the normal coordinator.
The prior AVG refusal and incomplete checks remain evidence, not certification.
"""
from ctypes import wintypes as w
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
import tempfile
import uuid

from .b2a_snapshot import FrozenSnapshot, sha, verify_tree
from .b2a_windows import (AppContainer, ReadLease, close, continue_debug_event, dll,
                          final_path, function, next_debug_event, set_dacl)
from .errors import require
from .provider import CopyPayload, verify_copy
from .requests import Request, Selection


def publish_evidence(report, directory):
    """B2A evidence only; reuse B1's NTFS no-replacement transaction primitives."""
    from .digests import FullArtifactDigest, byte_digest
    from .persistence import _ntfs_directory, _rename_noreplace, _existing_matches
    require(report.get('family') == 'TRIOCTAGON_B2A_PROOF_EVIDENCE' and
            report.get('production_attestation_enabled') is False and
            report.get('windows_execution_binding') == 'NOT_PROVEN',
            'UNVERIFIED_PRODUCER', 'only non-production B2A proof evidence accepted')
    raw = json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')
    identity = byte_digest(FullArtifactDigest, raw)
    directory = _ntfs_directory(directory)
    target = directory/('sha256-' + identity.sha256 + '.b2a.json')
    fd, name = tempfile.mkstemp(prefix='.b2a-', suffix='.tmp', dir=directory)
    temporary = Path(name)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        try:
            _rename_noreplace(temporary, target)
        except FileExistsError:
            _existing_matches(target, raw, identity)
        return target, identity
    finally:
        temporary.unlink(missing_ok=True)

CHECKS = ('catalogue_approved', 'build_evidence_accepted', 'installed_content_verified',
          'execution_snapshot_bound', 'actual_imports_bound', 'inputs_verified',
          'payload_validated', 'participating_kernel_verified')


class NativeOriginRefusal(ValueError):
    pass


class NativeGate:
    """Check debug-event handles before allowing the stopped process to continue.

    Expected OS members are individually pinned under the trusted-OS policy;
    no directory-level permission for arbitrary System32 or vendor DLLs exists.
    """
    def __init__(self, snapshot, manifest, os_members):
        self.expected = {os.path.normcase(str(snapshot/r['path'])): r
                         for r in manifest.to_dict()['members']}
        self.expected.update({os.path.normcase(str(Path(p).absolute())): r for p, r in os_members.items()})
        self.images, self.leases = [], []

    def inspect(self, handle):
        if not handle:
            raise NativeOriginRefusal('NATIVE_IMAGE_HANDLE_UNAVAILABLE')
        path = final_path(handle)
        row = self.expected.get(os.path.normcase(str(path)))
        if row is None:
            raise NativeOriginRefusal('UNEXPECTED_NATIVE_IMAGE: ' + str(path))
        lease = ReadLease(path)
        self.leases.append(lease)
        raw = path.read_bytes()
        if sha(raw) != row['sha256'] or len(raw) != row['size']:
            raise NativeOriginRefusal('NATIVE_IMAGE_BYTES_MISMATCH: ' + str(path))
        self.images.append({'path': str(path), 'sha256': row['sha256'], 'size': row['size']})

    def close(self):
        for lease in reversed(self.leases):
            lease.close()
        self.leases.clear()


def terminate_debugged(app, pending=None):
    """Terminate before resuming a rejected native load, then drain exit events."""
    function(dll('kernel32'), 'TerminateProcess', w.BOOL, w.HANDLE, w.UINT)(app.process, 1)
    if pending is not None:
        continue_debug_event(pending)
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        event = next_debug_event(100)
        if event is None:
            if app.wait(0) is not None:
                return
            continue
        if event.event in (3, 6):
            handle = event.data.process.hFile if event.event == 3 else event.data.dll.hFile
            if handle:
                close(handle)
        continue_debug_event(event)
        if event.event == 5:
            if app.wait(10000) is None:
                raise OSError('debuggee exit acknowledgement unavailable')
            return
    raise OSError('debuggee cleanup timed out')


def validate_observation(value, request, parent, nonce, snapshot):
    require(value.get('family') == 'TRIOCTAGON_B2A_WORKER_OBSERVATION' and
            value.get('mode') == 'B2A_VALIDATION_ONLY' and value.get('producer_verified') is False,
            'UNVERIFIED_PRODUCER', 'ordinary/verified result prohibited in proof mode')
    require(value.get('request') == request.identity.to_dict() and value.get('attempt_nonce') == nonce and
            value.get('snapshot') == snapshot.name and
            value.get('provider') == 'trioctagon_analysis.provider:copy_recorded' and
            Path(value.get('entry_origin', '')).absolute() == snapshot/'site/trioctagon_analysis/provider.py',
            'RESULT_BINDING_MISMATCH', 'stale or wrong proof output')
    payload = CopyPayload(value['payload'])
    require(value.get('payload_digest') == payload.identity.to_dict(),
            'RESULT_BINDING_MISMATCH', 'proof payload identity mismatch')
    verify_copy(payload, parent, Selection(request.to_dict()['selection']))


def run_proof(candidate, staging, manifest, request, parent, catalogue, approval,
              *, expectation_pin, approval_pin):
    """One proof attempt; independently supplied pins, retained parent, no success lane.

    Snapshot checks are real. A NOT_PROVEN result is never transformed into a
    verified ProducerEvidence or normal DerivedAnalysisRecord.
    """
    nonce = uuid.uuid4().hex
    report = {'family': 'TRIOCTAGON_B2A_PROOF_EVIDENCE', 'mode': 'B2A_VALIDATION_ONLY',
        'attempt_nonce': nonce, 'started_at': datetime.now(timezone.utc).isoformat(),
        'windows_execution_binding': 'NOT_PROVEN', 'production_attestation_enabled': False,
        'checks': {key: {'state': 'UNAVAILABLE', 'reason': 'Not reached.'} for key in CHECKS},
        'native_images': [], 'failures': [], 'memory_samples': [], 'observation': None,
        'kernel_role': 'parent_validation', 'scientific_recomputation': 'NOT_PERFORMED'}
    def verified(key, reason):
        report['checks'][key] = {'state': 'VERIFIED', 'reason': reason}
    app = snapshot = gate = None
    input_leases = []
    stage = 'build_evidence_accepted'
    start = time.perf_counter()
    owned = Path(staging).resolve()/('proof-' + nonce)
    owned.mkdir()
    try:
        require(sha(manifest.to_bytes()) == expectation_pin and sha(approval.to_bytes()) == approval_pin,
                'AUTHORITY_MISMATCH', 'independent deployment pin mismatch')
        require(type(request) is Request, 'INVALID_SCHEMA', 'typed request required')
        request.validate_context(catalogue, approval)
        # This confirms B2A scoped pin consistency, not final production approval.
        report['checks']['catalogue_approved'] = {'state': 'UNAVAILABLE',
            'reason': 'B2A candidate pins consistent; operator approval of deployment remains for review.'}
        require(request.to_dict()['kernel']['actual_archive']['sha256'] == manifest.to_dict()['kernel_archive'] and
                request.to_dict()['kernel']['lock']['sha256'] == manifest.to_dict()['kernel_lock'],
                'KERNEL_MISMATCH', 'selected certified kernel differs from snapshot expectation')
        verify_tree(candidate, manifest)
        verified(stage, 'Artifact-derived member expectation and B2A deployment pins match.')
        app = AppContainer()
        stage = 'installed_content_verified'
        snapshot = FrozenSnapshot(candidate, owned, manifest, app.sid_string)
        report['snapshot_identity'] = snapshot.id
        report['snapshot_build_nanoseconds'] = int((time.perf_counter()-start)*1e9)
        verified(stage, 'Fresh exact member set/size/hash verified after DACL freeze and read leases.')
        stage = 'inputs_verified'
        parent.require_reference(type(parent.reference)(request.to_dict()['parents'][0]))
        inputs = owned/'inputs'
        inputs.mkdir()
        for name, raw in [('expectation.json', manifest.to_bytes()), ('request.json', request.to_bytes()),
                          ('parent.json', parent.original)]:
            p = inputs/name
            p.write_bytes(raw)
            set_dacl(p, app.sid_string)
            input_leases.append(ReadLease(p))
        set_dacl(inputs, app.sid_string)
        input_leases.append(ReadLease(inputs, directory=True))
        verified(stage, 'Retained immutable request/parent bytes and all three parent identities bound.')
        stage = 'execution_snapshot_bound'
        output = owned/'output'
        output.mkdir()
        set_dacl(output, app.sid_string, True)
        os_members = {row['path']: row for row in manifest.to_dict()['os_members']}
        gate = NativeGate(snapshot.root, manifest, os_members)
        for path in os_members:
            with ReadLease(path) as lease:
                gate.inspect(lease.handle)
        report['preverified_os_members'] = gate.images[:]
        gate.images.clear()
        env = {k: os.environ[k] for k in ('SystemRoot', 'windir', 'LOCALAPPDATA')}
        env.update(TEMP=str(output), TMP=str(output), OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
        app.launch(snapshot.root/manifest.to_dict()['runtime'], snapshot.root/manifest.to_dict()['worker'],
            [inputs/'expectation.json', inputs/'request.json', inputs/'parent.json', output/'observation.json', nonce],
            output, environment=env, debug=True)
        stage = 'actual_imports_bound'
        deadline = time.monotonic() + 210
        while True:
            if time.monotonic() > deadline:
                terminate_debugged(app)
                raise TimeoutError('provisional wall ceiling reached')
            event = next_debug_event(100)
            if event is None:
                report['memory_samples'].append(app.memory())
                if report['memory_samples'][-1]['PrivateUsage'] > 4294967296:
                    terminate_debugged(app)
                    raise MemoryError('provisional observed memory ceiling reached')
                continue
            try:
                if event.event in (3, 6):
                    handle = event.data.process.hFile if event.event == 3 else event.data.dll.hFile
                    try:
                        gate.inspect(handle)
                    finally:
                        if handle:
                            close(handle)
            except BaseException:
                terminate_debugged(app, event)
                raise
            exit_code = event.data.code if event.event == 5 else None
            continue_debug_event(event, handled=event.event != 1 or event.data.code == 0x80000003)
            if exit_code is not None:
                require(exit_code == 0, 'PROVIDER_FAILURE', 'proof worker exited unsuccessfully')
                break
        # A plausible payload cannot bypass native admissions or post checks.
        snapshot.verify_after()
        raw = (output/'observation.json').read_bytes()
        require(len(raw) <= 131072, 'RESOURCE_LIMIT', 'proof observation output ceiling')
        observation = json.loads(raw)
        validate_observation(observation, request, parent, nonce, snapshot.root)
        report['observation'] = observation
        verified('payload_validated', 'Exact stored-token payload and request/nonce binding validated.')
        report['failures'].append('Production/complete B2A attestation activation is not implemented by this proof harness.')
    except Exception as exc:
        report['checks'][stage] = {'state': 'FAILED', 'reason': str(exc)[:1024]}
        report['failures'].append((type(exc).__name__ + ': ' + str(exc))[:1024])
        report['observation'] = None
    finally:
        cleanup_start = time.perf_counter()
        if gate is not None:
            report['native_images'] = gate.images
        cleanups = ([app.close] if app is not None else []) + ([gate.close] if gate is not None else [])
        cleanups += [lease.close for lease in input_leases]
        cleanups += [snapshot.close] if snapshot is not None else []
        report['cleanup'] = 'COMPLETE; bounded input/output proof evidence retained'
        for cleanup in cleanups:
            try:
                cleanup()
            except Exception as exc:
                report['cleanup'] = 'FAILED'
                report['failures'].append(('CLEANUP_FAILURE: ' + str(exc))[:1024])
                report['observation'] = None
        report['cleanup_nanoseconds'] = int((time.perf_counter()-cleanup_start)*1e9)
        report['elapsed_nanoseconds'] = int((time.perf_counter()-start)*1e9)
        report['completed_at'] = datetime.now(timezone.utc).isoformat()
    return report
