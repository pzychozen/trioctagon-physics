"""Closed axial request shapes and stored selection; representation only."""
import hashlib
import json

AXIAL_TYPES = ('axial_snapshot', 'axial_history', 'axial_source_budget')
MAX_SAMPLES = 4096  # Application resource guard, not a scientific domain.


def keys(value, expected):
    if not isinstance(value, dict) or set(value) != set(expected):
        raise ValueError('Missing or unknown axial fields')


def template(kind, source_mode='explicit'):
    if kind not in AXIAL_TYPES or source_mode not in ('explicit', 'record'):
        raise ValueError('Unknown axial kind/source')
    if source_mode == 'record':
        return {'axial_snapshot': {}, 'axial_history': {'sample_indices': []},
                'axial_source_budget': {'after_sample_index': None}}[kind]
    omega = [['', ''] for _ in range(3)]
    if kind == 'axial_snapshot': return {'omega': omega}
    if kind == 'axial_history': raise ValueError('Axial history is record-only')
    return {'before': {'omega': omega, 'update_index': ''},
            'parameters': {'eps': '', 'g': '', 'phase_strength': '', 'k': ['', '', '']}, 'after': None}


def explicit_omega(value):
    from trioctagon_ui.requests import number
    if not isinstance(value, list) or len(value) != 3:
        raise ValueError('Axial observation requires exactly one triad; rings are unsupported')
    if any(not isinstance(p, list) or len(p) != 2 for p in value):
        raise ValueError('Omega requires three re/im pairs')
    return [{k: {'f64': number(v, 'Omega.' + k).hex()} for k, v in zip(('re', 'im'), pair)} for pair in value]


def explicit_state(value):
    from trioctagon_ui.requests import integer
    keys(value, ('omega', 'update_index'))
    return {'omega': explicit_omega(value['omega']), 'update_index': integer(value['update_index'], 'update index')}


def explicit_parameters(value):
    from trioctagon_ui.requests import number
    keys(value, ('eps', 'g', 'phase_strength', 'k'))
    if not isinstance(value['k'], list) or len(value['k']) != 3: raise ValueError('Exactly three k values required')
    return {**{k: {'f64': number(value[k], k).hex()} for k in ('eps', 'g', 'phase_strength')},
            'k': [{'f64': number(v, 'k').hex()} for v in value['k']]}


def validate(kind, inputs, source):
    from trioctagon_ui.requests import integer
    if not isinstance(source, dict): raise ValueError('Explicit axial source required')
    mode = source.get('mode')
    keys(inputs, template(kind, mode))
    if mode == 'explicit':
        keys(source, ('mode',))
        if kind == 'axial_snapshot': explicit_omega(inputs['omega'])
        else:
            before = explicit_state(inputs['before']); explicit_parameters(inputs['parameters'])
            if inputs['after'] is not None:
                after = explicit_state(inputs['after'])
                if after['update_index'] != before['update_index'] + 1:
                    raise ValueError('Supplied after must have update_index = before + 1')
    else:
        keys(source, ('mode', 'record_json', 'sample_index'))
        if not isinstance(source['record_json'], str) or len(source['record_json'].encode('utf-8')) > 16 * 1024 * 1024:
            raise ValueError('Parent text exceeds 16 MiB application guard or is not text')
        anchor = integer(source['sample_index'], 'sample ordinal')
        if kind == 'axial_history':
            values = inputs['sample_indices']
            if not isinstance(values, list) or not 1 <= len(values) <= MAX_SAMPLES:
                raise ValueError('Choose 1..4096 stored ordinals (application resource guard)')
            indices = [integer(v, 'sample ordinal') for v in values]
            if indices != sorted(set(indices)) or indices[0] != anchor:
                raise ValueError('History ordinals must be strictly increasing, unique and anchored at first selection')
        elif kind == 'axial_source_budget' and inputs['after_sample_index'] is not None:
            integer(inputs['after_sample_index'], 'after sample ordinal')


def resolve(kind, inputs, source, parent=None):
    """No stepping, interpolation, scientific transformation or parameter override."""
    from trioctagon_ui.requests import integer
    validate(kind, inputs, source)
    identity = None; parameters = None; availability = None
    if source['mode'] == 'explicit':
        if kind == 'axial_snapshot':
            states = [{'omega': explicit_omega(inputs['omega']), 'update_index': None}]
        else:
            states = [explicit_state(inputs['before'])]
            parameters = explicit_parameters(inputs['parameters'])
            if inputs['after'] is not None: states.append(explicit_state(inputs['after']))
            availability = 'SUPPLIED_ADJACENT_PAIR' if len(states) == 2 else 'PREDICTION_ONLY'
        selection = [{'sample_ordinal': None, 'update_index': s['update_index']} for s in states]
    else:
        if parent is None: parent = json.loads(source['record_json'])
        if parent.get('record_type') != 'KERNEL_RUN_RECORD' or parent.get('topology') != 'triad' or parent.get('state_size') != '3':
            raise ValueError('Axial observation requires a stored triad RunRecord')
        samples = parent['samples']; anchor = integer(source['sample_index'])
        indices = [integer(v) for v in inputs['sample_indices']] if kind == 'axial_history' else [anchor]
        if kind == 'axial_source_budget' and inputs['after_sample_index'] is not None:
            indices.append(integer(inputs['after_sample_index']))
        if any(i >= len(samples) for i in indices): raise ValueError('Selected sample is not recorded')
        states = [{'omega': samples[i]['omega'], 'update_index': int(samples[i]['update_index'])} for i in indices]
        if kind == 'axial_source_budget':
            parameters = parent['parameters']
            if len(states) == 2:
                if states[1]['update_index'] != states[0]['update_index'] + 1:
                    raise ValueError('NEXT_SAMPLE_NOT_RECORDED: adjacent ordinals do not establish true n/n+1 adjacency')
                availability = 'RECORDED_ADJACENT_PAIR'
            else:
                availability = ('NEXT_SAMPLE_NOT_SELECTED' if any(int(s['update_index']) == states[0]['update_index'] + 1 for s in samples)
                                else 'NEXT_SAMPLE_NOT_RECORDED')
        identity = {'deterministic_sha256': parent['deterministic_sha256'],
                    'canonical_bytes_sha256': hashlib.sha256(source['record_json'].encode('utf-8')).hexdigest(),
                    'source_commit': parent['implementation']['commit']}
        selection = [{'sample_ordinal': i, 'update_index': s['update_index']} for i, s in zip(indices, states)]
    # Detach parent-owned containers, including the parameter token tree.
    return json.loads(json.dumps({'parent': identity, 'selection': selection,
        'resolved_inputs_hex': {'states': states, 'parameters': parameters},
        'input_policy': 'STORED_BINARY64_TOKENS' if identity else 'EXPLICIT_DECIMAL_TO_BINARY64',
        'requested_expressions': None if identity else inputs, 'comparison_availability': availability}, allow_nan=False))
