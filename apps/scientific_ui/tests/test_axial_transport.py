"""Application transport/identity/compatibility tests; kernel science frozen at K."""
import ast
from copy import deepcopy
from dataclasses import FrozenInstanceError
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trioctagon_ui import requests as r, worker, axial_artifacts as codec, axial_inputs
from trioctagon_ui.axial_identity import verify_installed_axial, admitted_lock
from test_requests import example
from test_worker_contract import record, run_child


def explicit(kind='axial_snapshot', after=False):
    omega = [['.2', '.3'], ['-.4', '.1'], ['.1', '-.2']]
    if kind == 'axial_snapshot': return {'omega': omega}
    return {'before': {'omega': omega, 'update_index': '0'},
        'parameters': {'eps': '.05', 'g': '.2', 'phase_strength': '.01', 'k': ['1', '1.2', '1.7']},
        'after': {'omega': deepcopy(omega), 'update_index': '1'} if after else None}


def source(parent, index='0'): return {'mode': 'record', 'record_json': parent, 'sample_index': index}


def result(envelope):
    response = worker.respond(envelope)
    if response['status'] != 'completed': raise AssertionError(response['error'])
    return response['result']


class AxialRequestWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.parent = record(r.run_request(example('3')))

    def test_explicit_snapshot_tokens_and_identity(self):
        value = result(r.analysis_request('axial_snapshot', explicit()))
        self.assertIsNone(value['parent_digest']); self.assertIsNone(value['sample_index'])
        artifact = codec.loads(codec.canonical(value['data']))
        self.assertEqual(artifact['implementation']['source_commit'], admitted_lock()['source_commit'])
        self.assertEqual(len(artifact['implementation']['scientific_dependencies']), 20)
        self.assertEqual(artifact['resolved_inputs_hex']['states'][0]['omega'][0]['re']['f64'], float('.2').hex())
        self.assertIsNone(artifact['reference_comparison'])

    def test_record_snapshot_parent_unchanged(self):
        before = self.parent
        v = result(r.analysis_request('axial_snapshot', {}, source=source(self.parent, '2')))
        self.assertEqual(v['data']['selection'], [{'sample_ordinal': 2, 'update_index': 2}])
        self.assertEqual(v['data']['parent']['canonical_bytes_sha256'], hashlib.sha256(before.encode()).hexdigest())
        self.assertEqual(self.parent, before)

    def test_sparse_selected_history_and_real_indices(self):
        v = result(r.analysis_request('axial_history', {'sample_indices': ['0', '2', '3']}, source=source(self.parent)))
        self.assertIsNone(v['sample_index'])
        self.assertEqual([x['update_index'] for x in v['data']['selection']], [0, 2, 3])
        self.assertEqual(len(v['data']['data']['snapshots']), 3)
        # Synthetic transport-only sparse sample sequence: no forged RunRecord acceptance.
        p = json.loads(self.parent); p['samples'] = [p['samples'][0], p['samples'][3]]
        binding = axial_inputs.resolve('axial_history', {'sample_indices': ['0', '1']}, source(self.parent), p)
        self.assertEqual([x['update_index'] for x in binding['selection']], [0, 3])

    def test_history_order_unique_anchor_and_record_only(self):
        for indices in ([], ['1', '0'], ['0', '0'], ['1', '2']):
            with self.subTest(indices=indices), self.assertRaises(ValueError):
                r.analysis_request('axial_history', {'sample_indices': indices}, source=source(self.parent))
        with self.assertRaises(ValueError): r.analysis_request('axial_history', {'sample_indices': ['0']})

    def test_missing_sample_and_ring_refusal(self):
        bad = worker.respond(r.analysis_request('axial_snapshot', {}, source=source(self.parent, '99')))
        self.assertEqual(bad['status'], 'failed')
        p = json.loads(self.parent); p['topology'] = 'ring'; p['state_size'] = '6'
        with self.assertRaisesRegex(ValueError, 'triad'): axial_inputs.resolve('axial_snapshot', {}, source(self.parent), p)
        for omega in ([['0', '0']] * 6, [['0', '0']] * 2):
            with self.assertRaises(ValueError): r.analysis_request('axial_snapshot', {'omega': omega})

    def test_closed_modes_and_parameter_override(self):
        for kind, inputs, src in (
            ('axial_snapshot', {**explicit(), 'extra': 1}, {'mode': 'explicit'}),
            ('axial_snapshot', explicit(), source(self.parent)),
            ('axial_source_budget', {'after_sample_index': None, 'parameters': explicit('axial_source_budget')['parameters']}, source(self.parent)),
            ('axial_source_budget', {'after_sample_index': '1', 'after_parent': self.parent}, source(self.parent))):
            with self.subTest(kind=kind), self.assertRaises(ValueError): r.analysis_request(kind, inputs, source=src)
        with self.assertRaises(ValueError): r.analysis_request('axial_snapshot', {}, source={**source(self.parent), 'other_record': self.parent})

    def test_numeric_refusals(self):
        for invalid in (True, 0, None, 'NaN', 'Infinity', '1e-9999'):
            v = explicit(); v['omega'][0][0] = invalid
            with self.subTest(value=invalid), self.assertRaises(ValueError): r.analysis_request('axial_snapshot', v)

    def test_explicit_budget_prediction_and_supplied_comparison(self):
        for after in (False, True):
            v = result(r.analysis_request('axial_source_budget', explicit('axial_source_budget', after)))['data']['data']
            self.assertEqual(v['comparison_status'], 'SUPPLIED_ADJACENT_PAIR' if after else 'PREDICTION_ONLY')
            self.assertEqual(v['budget']['comparison_residuals'] is None, not after)
            self.assertEqual(len(v['budget']['amplitude_terms']), 5); self.assertEqual(len(v['budget']['phase_terms']), 2)

    def test_record_budget_binds_parameters_and_true_adjacency(self):
        v = result(r.analysis_request('axial_source_budget', {'after_sample_index': '1'}, source=source(self.parent)))['data']
        self.assertEqual(v['data']['comparison_status'], 'RECORDED_ADJACENT_PAIR')
        self.assertEqual(v['data']['budget']['comparison_status'], 'SUPPLIED_ADJACENT_PAIR')
        self.assertEqual(v['resolved_inputs_hex']['parameters'], json.loads(self.parent)['parameters'])
        bad = worker.respond(r.analysis_request('axial_source_budget', {'after_sample_index': '2'}, source=source(self.parent)))
        self.assertEqual(bad['status'], 'failed'); self.assertIn('NEXT_SAMPLE_NOT_RECORDED', bad['error']['message'])

    def test_adjacent_ordinals_with_nonadjacent_indices_rejected(self):
        p = json.loads(self.parent); p['samples'] = [p['samples'][0], p['samples'][3]]
        with self.assertRaisesRegex(ValueError, 'n/n\+1'):
            axial_inputs.resolve('axial_source_budget', {'after_sample_index': '1'}, source(self.parent), p)

    def test_unavailable_next_sample_prediction_only(self):
        v = result(r.analysis_request('axial_source_budget', {'after_sample_index': None}, source=source(self.parent, '3')))['data']['data']
        self.assertEqual(v['comparison_availability'], 'NEXT_SAMPLE_NOT_RECORDED')
        self.assertEqual(v['comparison_status'], 'PREDICTION_ONLY'); self.assertIsNone(v['budget']['comparison_residuals'])

    def test_no_advancement_and_only_public_axial_calls(self):
        from kernel_physics import api
        from contextlib import ExitStack
        with ExitStack() as stack:
            for name in ('step', 'run', 'resume', 'advance_clock', 'advance_ema'):
                stack.enter_context(patch.object(api, name, side_effect=AssertionError('hidden advancement')))
            with patch.object(api, 'axial_snapshot', wraps=api.axial_snapshot) as snapshot:
                result(r.analysis_request('axial_history', {'sample_indices': ['0', '2']}, source=source(self.parent)))
                self.assertEqual(snapshot.call_count, 2)
            result(r.analysis_request('axial_source_budget', {'after_sample_index': None}, source=source(self.parent)))

    def test_isolated_worker_gui_free(self):
        child, response = run_child(r.analysis_request('axial_snapshot', explicit()))
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(response['imports'], {'gui': [], 'models': []}); self.assertEqual(response['runtime_network_attempts'], [])
        self.assertTrue(response['isolated'])

    def test_old_record_load_observe_strict_resume(self):
        old = (Path(__file__).parent/'fixtures/axial_old_run.json').read_text()
        loaded = result(r.request('load_record', {'record_json': old}))
        self.assertEqual(loaded['canonical_json'], old)
        result(r.analysis_request('axial_history', {'sample_indices': ['0', '1']}, source=source(old)))
        rejected = worker.respond(r.request('resume', {'record_json': old, 'updates': '1'}))
        self.assertEqual(rejected['status'], 'failed')

    def test_same_pair_record_and_resume_noninterference(self):
        before = record(r.run_request(example('3')))
        result(r.analysis_request('axial_snapshot', explicit()))
        result(r.analysis_request('axial_source_budget', {'after_sample_index': '1'}, source=source(before)))
        self.assertEqual(before, record(r.run_request(example('3'))))
        first = record(r.request('resume', {'record_json': before, 'updates': '1'}))
        result(r.analysis_request('axial_history', {'sample_indices': ['0', '3']}, source=source(before)))
        self.assertEqual(first, record(r.request('resume', {'record_json': before, 'updates': '1'})))


class AxialArtifactIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.value = result(r.analysis_request('axial_snapshot', explicit()))

    def test_canonical_roundtrip_deep_immutability(self):
        view = codec.AxialAnalysisView(self.value); raw = view.canonical_json
        self.assertEqual(codec.dumps(codec.loads(raw)), raw)
        with self.assertRaises(TypeError): view.artifact['data']['snapshot']['W'][0]['f64'] = '0x0.0p+0'
        with self.assertRaises(FrozenInstanceError): view.canonical_json = 'changed'
        v = deepcopy(self.value); frozen = codec.AxialAnalysisView(v); v['data']['data']['snapshot']['C'][0]['f64'] = '0x0.0p+0'
        self.assertEqual(frozen.canonical_json, raw)

    def test_unknown_missing_duplicate_and_digest_fields(self):
        for path in ((), ('data',), ('data', 'snapshot'), ('implementation',), ('selection', 0)):
            v = deepcopy(self.value['data']); node = v
            for k in path: node = node[k]
            node['unexpected'] = True; v['content_sha256'] = codec.digest(v)
            with self.subTest(path=path), self.assertRaises(ValueError): codec.loads(codec.canonical(v))
        raw = codec.canonical(self.value['data'])
        with self.assertRaises(ValueError): codec.loads(raw.replace('"schema_version":"0.1.0"', '"schema_version":"0.1.0","schema_version":"0.1.0"'))
        v = deepcopy(self.value['data']); v['content_sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'digest'): codec.loads(codec.canonical(v))

    def test_nonfinite_wrong_shape_and_theorem_badge_refused(self):
        for token in ('nan', 'inf', '-inf', '0.0', '0x1p+0'):
            v = deepcopy(self.value['data']); v['data']['snapshot']['Gamma']['f64'] = token; v['content_sha256'] = codec.digest(v)
            with self.subTest(token=token), self.assertRaises(ValueError): codec.loads(codec.canonical(v))
        for k, val in (('reference_comparison', {'status':'M3 CERTIFIED'}), ('evidence_class','EXACT_THEOREM')):
            v = deepcopy(self.value['data']); v[k]=val; v['content_sha256']=codec.digest(v)
            with self.assertRaises(ValueError): codec.loads(codec.canonical(v))

    def test_actual_installed_identity_twenty_members(self):
        identity = verify_installed_axial()
        self.assertEqual(identity['version'], '0.2.0'); self.assertEqual(len(identity['scientific_dependencies']),20)
        self.assertTrue(all(Path(p).is_file() for p in identity['installed_origins'].values()))

    def test_missing_tampered_owner_facade_and_dependency_fail_closed(self):
        original = Path.read_bytes
        for filename in ('axial_observables.py', 'api.py', 'readouts.py', '_response_numeric.py', 'dynamics.py'):
            for missing in (False, True):
                def changed(p, filename=filename, missing=missing):
                    if p.name == filename and p.parent.name == 'kernel_physics':
                        if missing: raise FileNotFoundError(str(p))
                        return original(p) + b'\n# tampered'
                    return original(p)
                with self.subTest(file=filename, missing=missing), patch.object(Path,'read_bytes',changed), self.assertRaises(ValueError): verify_installed_axial()

    def test_stale_lock_wrong_version_source_and_origin(self):
        original=Path.read_bytes
        def lock_changed(p): return original(p)+b' ' if p.name=='kernel-artifact.lock.json' else original(p)
        with patch.object(Path,'read_bytes',lock_changed), self.assertRaisesRegex(ValueError,'lock'): verify_installed_axial()
        lock=admitted_lock()
        for key,val in (('version','0.1.0'),('source_commit','0'*40)):
            raw=json.dumps({**lock,key:val}).encode()
            def changed(p): return raw if p.name=='kernel-artifact.lock.json' else original(p)
            with patch.object(Path,'read_bytes',changed), self.assertRaises(ValueError): verify_installed_axial()
        with patch('trioctagon_ui.axial_identity.find_spec',return_value=None), self.assertRaisesRegex(ValueError,'origin'): verify_installed_axial()

    def test_no_private_scientific_imports_or_renderer_equations(self):
        package=Path(worker.__file__).parent
        for filename in ('axial_views.py','axial_exports.py','axial_inputs.py','axial_artifacts.py','axial_identity.py','axial_reference.py'):
            tree=ast.parse((package/filename).read_text())
            for node in ast.walk(tree):
                if isinstance(node,ast.ImportFrom): self.assertFalse((node.module or '').startswith('kernel_physics'))
                if isinstance(node,ast.Import): self.assertFalse(any(n.name.startswith('kernel_physics') for n in node.names))
                if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
                    self.assertNotIn(node.func.attr,('cross','dot','norm','step','step3','step_ring','sin','cos','sqrt'))

    def test_job_validation_binds_request_selection_and_actual_identity(self):
        from trioctagon_ui.jobs import validate_response
        parent=record(r.run_request(example('2')))
        request=r.analysis_request('axial_history',{'sample_indices':['0','2']},source=source(parent))
        response=worker.respond(request)
        response.update(isolated=True,imports={'gui':[],'models':[]},runtime_network_attempts=[])
        validate_response(response,request)
        mutations=(lambda v:v.update(request_id='wrong'),
            lambda v:v['result'].update(parent_digest='0'*64),
            lambda v:v['result'].update(sample_index=0),
            lambda v:v['result']['data']['selection'][1].update(sample_ordinal=1),
            lambda v:v['result']['data']['implementation'].update(source_commit='0'*40),
            lambda v:v['result']['data']['implementation']['installed_origins'].update({'kernel_physics/api.py':'C:/other/api.py'}))
        for mutate in mutations:
            value=deepcopy(response);mutate(value);value['result']['data']['content_sha256']=codec.digest(value['result']['data'])
            with self.subTest(mutation=mutate),self.assertRaises(ValueError):validate_response(value,request)
        other=deepcopy(request);other['payload']['source']['record_json']=record(r.run_request(example('1')))
        with self.assertRaises(ValueError):validate_response(response,other)
