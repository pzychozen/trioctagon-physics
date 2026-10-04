"""Strict, inert axial transport. Tokens are validated, never scientific equations."""
from dataclasses import dataclass, field
import hashlib
import json
import math
import re

from trioctagon_ui.axial_inputs import AXIAL_TYPES, MAX_SAMPLES, keys
from trioctagon_ui.record_views import freeze, flatten

ARTIFACT_TYPE = 'TRIOCTAGON_AXIAL_OBSERVATION'
SCHEMA_VERSION = '0.1.0'
POLICY = 'CHECKED_BINARY64_AXIAL_V1'
SOURCE = 'PAPER_G_V0.1.1_SECTIONS_2_3'
REVISION = 'AXIAL_M1_V1'
QUALIFICATION = ('Floating observation; geometry-attached axial observable; squared-amplitude scale; not a physical field. '
                 'Prediction reconstructs model identities, not stored intermediates. No exact theorem, interval certificate or external execution attestation is claimed.')
MAX_BYTES = 16 * 1024 * 1024


def plain(value):
    from collections.abc import Mapping
    if isinstance(value, Mapping): return {k: plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [plain(v) for v in value]
    return value


def canonical(value):
    return json.dumps(plain(value), ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical({k: v for k, v in value.items() if k != 'content_sha256'}).encode('utf-8')).hexdigest()


def pairs(values):
    result = {}
    for k, v in values:
        if k in result: raise ValueError('Duplicate axial JSON key: ' + k)
        result[k] = v
    return result


def uint(value):
    if type(value) is not int or value < 0: raise ValueError('Expected nonnegative integer')


def text(value):
    if not isinstance(value, str) or not value: raise ValueError('Expected nonempty text')


def hash_value(value, length=64):
    if not isinstance(value, str) or re.fullmatch('[0-9a-f]{' + str(length) + '}', value) is None:
        raise ValueError('Malformed identity hash')


def token(value):
    keys(value, ('f64',)); spelling = value['f64']
    if not isinstance(spelling, str) or len(spelling) > 32: raise ValueError('Malformed finite binary64 token')
    try: number = float.fromhex(spelling)
    except (ValueError, OverflowError) as exc: raise ValueError('Malformed finite binary64 token') from exc
    if not math.isfinite(number) or number.hex() != spelling: raise ValueError('Nonfinite or noncanonical binary64 token')


def sequence(value, validator, size):
    if not isinstance(value, list) or len(value) != size: raise ValueError('Axial array shape mismatch')
    for v in value: validator(v)


def vector(value): sequence(value, token, 3)
def matrix(value): sequence(value, vector, 3)
def complex_value(value):
    keys(value, ('re', 'im')); token(value['re']); token(value['im'])


def parameters(value):
    keys(value, ('eps', 'g', 'phase_strength', 'k'))
    for k in ('eps', 'g', 'phase_strength'): token(value[k])
    vector(value['k'])


def area(value, named=False):
    keys(value, ('A', 'C', 'W', 'Gamma', 'name') if named else ('A', 'C', 'W', 'Gamma'))
    matrix(value['A']); vector(value['C']); vector(value['W']); token(value['Gamma'])
    if named: text(value['name'])


def definition(value):
    if value['revision'] != REVISION or value['source_definition'] != SOURCE or value['numeric_policy'] != POLICY:
        raise ValueError('Unknown observation definition/revision/numeric policy')


def snapshot(value):
    keys(value, ('revision', 'source_definition', 'numeric_policy', 'S', 'A', 'C', 'Gamma', 'C_parallel', 'C_perp',
                 'W', 'intensity', 'C_norm', 'W_norm', 'chiral_area_accounting', 'residuals'))
    definition(value)
    for k in ('S', 'A'): matrix(value[k])
    for k in ('C', 'C_parallel', 'C_perp', 'W'): vector(value[k])
    for k in ('Gamma', 'intensity', 'C_norm', 'W_norm'): token(value[k])
    accounting = value['chiral_area_accounting']
    fields = ('A', 'B', 'h', 'intensity', 'chiral_norm', 'chiral_norm_squared', 'gram_product', 'h_squared',
              'gram_rhs', 'gram_residual', 'amplitude_bound', 'slack_sum_of_squares', 'observed_slack', 'slack_residual')
    keys(accounting, ('chiral', *fields)); vector(accounting['chiral'])
    for k in fields: token(accounting[k])
    residuals = value['residuals']
    keys(residuals, ('area_cross', 'SC', 'reconstruction', 'W_z', 'gram', 'bilinear', 'decomposition'))
    matrix(residuals['area_cross'])
    for k in ('SC', 'reconstruction'): vector(residuals[k])
    for k in ('W_z', 'gram', 'bilinear', 'decomposition'): token(residuals[k])


def budget(value):
    keys(value, ('revision', 'source_definition', 'numeric_policy', 'before_index', 'after_index', 'resolved_parameters',
        'before_snapshot', 'amplitude_terms', 'pre_sync_prediction', 'phase_terms', 'predicted_after',
        'congruence_residual', 'pair_rotation_residual', 'actual_after_snapshot', 'comparison_residuals', 'comparison_status', 'qualification'))
    definition(value); uint(value['before_index']); parameters(value['resolved_parameters']); snapshot(value['before_snapshot'])
    for name, names in (('amplitude_terms', ('onsite_first', 'coupling_first', 'onsite_squared', 'mixed', 'coupling_squared')),
                        ('phase_terms', ('phase_existing_area', 'phase_symmetric_pair'))):
        sequence(value[name], lambda v: area(v, True), len(names))
        if tuple(v['name'] for v in value[name]) != names: raise ValueError('Source term order/name mismatch')
    pre = value['pre_sync_prediction']; keys(pre, ('omega', 'S', 'A', 'phases', 'delta', 'd'))
    sequence(pre['omega'], complex_value, 3)
    for k in ('S', 'A', 'd'): matrix(pre[k])
    for k in ('phases', 'delta'): vector(pre[k])
    for k in ('predicted_after', 'congruence_residual', 'pair_rotation_residual'): area(value[k])
    text(value['qualification'])
    if value['comparison_status'] == 'PREDICTION_ONLY':
        if any(value[k] is not None for k in ('after_index', 'actual_after_snapshot', 'comparison_residuals')):
            raise ValueError('Prediction-only comparisons must be null')
    elif value['comparison_status'] == 'SUPPLIED_ADJACENT_PAIR':
        uint(value['after_index'])
        if value['after_index'] != value['before_index'] + 1: raise ValueError('Budget requires true update adjacency')
        snapshot(value['actual_after_snapshot']); area(value['comparison_residuals'])
    else: raise ValueError('Unknown pure budget comparison status')


def implementation(value):
    keys(value, ('distribution', 'version', 'source_commit', 'build_input_sha256', 'lock_sha256', 'installed_owner_sha256',
        'installed_facade_sha256', 'scientific_dependencies', 'installed_origins', 'environment', 'verification'))
    if value['distribution'] != 'trioctagon-physics' or value['version'] != '0.2.0' or value['verification'] != 'OBSERVED_INSTALLED_BYTES_NOT_EXTERNAL_ATTESTATION':
        raise ValueError('Unsupported axial implementation claim')
    hash_value(value['source_commit'], 40)
    for k in ('build_input_sha256', 'lock_sha256', 'installed_owner_sha256', 'installed_facade_sha256'): hash_value(value[k])
    deps = value['scientific_dependencies']
    if not isinstance(deps, list) or len(deps) != 20: raise ValueError('Expected 20 distributed scientific dependency identities')
    for row in deps:
        keys(row, ('path', 'sha256')); text(row['path']); hash_value(row['sha256'])
    paths = [r['path'] for r in deps]
    if paths != sorted(set(paths)) or any(not p.startswith('kernel_physics/') or not p.endswith('.py') or '..' in p for p in paths):
        raise ValueError('Malformed dependency identity paths')
    by_path = {r['path']: r['sha256'] for r in deps}
    if by_path.get('kernel_physics/axial_observables.py') != value['installed_owner_sha256'] or by_path.get('kernel_physics/api.py') != value['installed_facade_sha256']:
        raise ValueError('Owner/facade identity disagreement')
    keys(value['installed_origins'], paths)
    for v in value['installed_origins'].values(): text(v)
    keys(value['environment'], ('python', 'platform', 'numpy', 'sympy', 'mpmath'))
    for v in value['environment'].values(): text(v)


def validate(value):
    keys(value, ('artifact_type', 'schema_version', 'observation_api_version', 'observer_revision', 'analysis_kind',
        'evidence_class', 'parent', 'selection', 'input_policy', 'requested_expressions', 'resolved_inputs_hex',
        'implementation', 'numeric_policy', 'data', 'reference_comparison', 'qualification', 'content_sha256'))
    if (value['artifact_type'], value['schema_version'], value['observation_api_version'], value['observer_revision'], value['evidence_class']) != (ARTIFACT_TYPE, SCHEMA_VERSION, '1.0.0', REVISION, 'FLOATING_OBSERVATION'):
        raise ValueError('Unsupported axial artifact/schema/evidence class')
    kind = value['analysis_kind']
    if kind not in AXIAL_TYPES or value['numeric_policy'] != POLICY or value['reference_comparison'] is not None or value['qualification'] != QUALIFICATION:
        raise ValueError('Unsupported axial kind/policy or theorem claim')
    parent = value['parent']
    if parent is not None:
        keys(parent, ('deterministic_sha256', 'canonical_bytes_sha256', 'source_commit'))
        hash_value(parent['deterministic_sha256']); hash_value(parent['canonical_bytes_sha256']); hash_value(parent['source_commit'], 40)
    if value['input_policy'] != ('STORED_BINARY64_TOKENS' if parent else 'EXPLICIT_DECIMAL_TO_BINARY64'):
        raise ValueError('Input policy disagrees with parent')
    if parent and value['requested_expressions'] is not None: raise ValueError('Stored input spellings must not be invented')
    selection = value['selection']; resolved = value['resolved_inputs_hex']
    if not isinstance(selection, list) or not 1 <= len(selection) <= MAX_SAMPLES: raise ValueError('Invalid selection size')
    keys(resolved, ('states', 'parameters')); sequence(resolved['states'], lambda s: keys(s, ('omega', 'update_index')), len(selection))
    for row, state in zip(selection, resolved['states']):
        keys(row, ('sample_ordinal', 'update_index'))
        sequence(state['omega'], complex_value, 3)
        if row['update_index'] != state['update_index']: raise ValueError('Selection and resolved state disagree')
        if parent: uint(row['sample_ordinal']); uint(row['update_index'])
        elif row['sample_ordinal'] is not None: raise ValueError('Explicit input cannot claim a stored ordinal')
        if row['update_index'] is not None: uint(row['update_index'])
    if not parent:
        from trioctagon_ui.axial_inputs import resolve
        expected = resolve(kind, value['requested_expressions'], {'mode': 'explicit'})
        if resolved != expected['resolved_inputs_hex'] or selection != expected['selection']: raise ValueError('Explicit input/resolution disagreement')
    data = value['data']
    if kind == 'axial_snapshot':
        if len(selection) != 1 or resolved['parameters'] is not None: raise ValueError('Snapshot selection mismatch')
        keys(data, ('snapshot',)); snapshot(data['snapshot'])
    elif kind == 'axial_history':
        if parent is None or resolved['parameters'] is not None: raise ValueError('History must bind stored samples')
        ordinals = [r['sample_ordinal'] for r in selection]; indices = [r['update_index'] for r in selection]
        if ordinals != sorted(set(ordinals)) or indices != sorted(set(indices)): raise ValueError('History must remain ordered and sparse')
        keys(data, ('snapshots',)); sequence(data['snapshots'], snapshot, len(selection))
    else:
        keys(data, ('budget', 'comparison_status', 'comparison_availability')); budget(data['budget'])
        b = data['budget']; count = 1 if b['after_index'] is None else 2
        if len(selection) != count or selection[0]['update_index'] != b['before_index'] or (count == 2 and selection[1]['update_index'] != b['after_index']) or resolved['parameters'] != b['resolved_parameters']:
            raise ValueError('Budget data and resolved selection/parameters disagree')
        expected_status = 'RECORDED_ADJACENT_PAIR' if parent and count == 2 else b['comparison_status']
        if data['comparison_status'] != expected_status: raise ValueError('Comparison provenance claim mismatch')
        choices = ('NEXT_SAMPLE_NOT_RECORDED', 'NEXT_SAMPLE_NOT_SELECTED') if parent and count == 1 else (expected_status,)
        if data['comparison_availability'] not in choices: raise ValueError('Invalid comparison availability')
    implementation(value['implementation']); hash_value(value['content_sha256'])
    if value['content_sha256'] != digest(value): raise ValueError('Axial content digest mismatch')
    return value


def loads(raw):
    if isinstance(raw, bytes): raw = raw.decode('utf-8')
    if not isinstance(raw, str) or len(raw.encode('utf-8')) > MAX_BYTES: raise ValueError('Axial artifact exceeds 16 MiB application limit')
    try:
        value = json.loads(raw, object_pairs_hook=pairs, parse_constant=lambda s: (_ for _ in ()).throw(ValueError('Nonfinite JSON literal')))
        validate(value)
    except (KeyError, TypeError, RecursionError, OverflowError) as exc:
        raise ValueError('Malformed axial artifact') from exc
    return freeze(value)


def dumps(value):
    value = plain(value); validate(value)
    raw = canonical(value)
    if len(raw.encode('utf-8')) > MAX_BYTES: raise ValueError('Axial artifact exceeds 16 MiB application limit')
    return raw


def create(kind, binding, identity, data):
    value = {'artifact_type': ARTIFACT_TYPE, 'schema_version': SCHEMA_VERSION, 'observation_api_version': '1.0.0',
        'observer_revision': REVISION, 'analysis_kind': kind, 'evidence_class': 'FLOATING_OBSERVATION',
        **{k: binding[k] for k in ('parent', 'selection', 'input_policy', 'requested_expressions', 'resolved_inputs_hex')},
        'implementation': identity, 'numeric_policy': POLICY, 'data': data, 'reference_comparison': None,
        'qualification': QUALIFICATION}
    value['content_sha256'] = digest(value)
    return plain(loads(canonical(value)))


@dataclass(frozen=True)
class AxialAnalysisView:
    result: object
    saved_import: bool = False
    artifact: object = field(init=False, repr=False)
    canonical_json: str = field(init=False, repr=False)

    def __post_init__(self):
        raw = dumps(self.result['data']); artifact = loads(raw)
        if self.result['result_kind'] != 'analysis' or self.result['analysis_type'] != artifact['analysis_kind']:
            raise ValueError('Wrong result family for axial cache')
        object.__setattr__(self, 'result', freeze(plain(self.result)))
        object.__setattr__(self, 'artifact', artifact)
        object.__setattr__(self, 'canonical_json', raw)

    @classmethod
    def from_saved(cls, raw):
        value = loads(raw); parent = value['parent']; selection = value['selection']
        return cls({'result_kind': 'analysis', 'analysis_type': value['analysis_kind'],
            'parent_digest': parent['deterministic_sha256'] if parent else None,
            'parent_source_commit': parent['source_commit'] if parent else None,
            'sample_index': None if value['analysis_kind'] == 'axial_history' else selection[0]['sample_ordinal'],
            'inputs': {}, 'data': plain(value), 'qualification': QUALIFICATION}, saved_import=True)

    @property
    def coordinates(self): return None  # Never masquerade as legacy history coordinates.

    def rows(self, precision=None): return tuple(flatten(self.artifact, precision=precision))
