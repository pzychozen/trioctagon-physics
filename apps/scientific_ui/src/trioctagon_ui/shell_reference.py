"""Pinned inert scientific data; no kernel, symbolic evaluation or path fallback."""
from dataclasses import dataclass
from importlib import resources
from collections.abc import Mapping
from types import MappingProxyType
import hashlib
import json
import math

RESOURCE = 'shell_reference_v0_1.json'
MANIFEST = 'shell_reference_manifest_v0_1.json'
RESOURCE_SHA = '54d93b7396921c87d17cbec65b56affc4272e384d68a2d471521c621664c454b'
MANIFEST_SHA = '62e1abae2ba89885209b622238c0b9272f48f71004afd6069c6c692ccfba4b6e'
PRESETS = ('original', 'A', 'B', 'R_equals_w', 't_equals_w', 'assigned_R10', 'assigned_RT')
EVENTS = ('original', 'A', 'B')


class ReferenceError(ValueError):
    pass


def freeze(value):
    if isinstance(value, dict): return MappingProxyType({k: freeze(v) for k, v in value.items()})
    if isinstance(value, list): return tuple(freeze(v) for v in value)
    return value


def plain(value):
    if isinstance(value, Mapping): return {k: plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [plain(v) for v in value]
    return value


def canonical(value):
    return json.dumps(plain(value), sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')


def strict_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result: raise ReferenceError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    def invalid(value): raise ReferenceError('Nonfinite JSON: ' + value)
    try: return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)
    except (ValueError, TypeError, RecursionError) as exc: raise ReferenceError('Invalid reference JSON: ' + str(exc)) from exc


def validate(data, manifest):
    """Structural admission, not a new geometry proof. Hash pins are checked first."""
    def need(ok, text):
        if not ok: raise ReferenceError(text)
    def point(p):
        need(isinstance(p, list) and len(p) == 3 and all(type(x) in (int, float) and math.isfinite(x) for x in p), 'Malformed coordinate')
    def exact(p): need(isinstance(p, list) and len(p) == 3 and all(isinstance(x, str) and len(x) <= 512 for x in p), 'Malformed exact text')
    def cycle(c, n): need(isinstance(c, list) and len(c) >= 3 and len(set(c)) == len(c) and all(type(i) is int and 0 <= i < n for i in c), 'Malformed facet cycle')
    try:
        need(set(data) == {'geometry','events','graphs','hulls','presets','source_identities'}, 'Reference fields')
        g = data['geometry']; vs = g['vertices']; es = g['edges']
        need([v['id'] for v in vs] == list(range(18)), 'Vertex identities')
        need([e['id'] for e in es] == [f'E{i:02}' for i in range(1,22)], 'Edge identities')
        for v in vs: point(v['centered']); exact(v['centered_exact']); exact(v['original_exact'])
        need(g['faces'] == [[0,1,2,3,4,5,6,7],[3,8,9,10,11,12,13,4],[10,14,15,0,7,16,17,11]], 'Panel cycles')
        branches = {e['id']+sign for e in es for sign in ('-','+')}
        for e in es:
            need(len(e['vertices']) == 2 and 0 <= e['vertices'][0] < e['vertices'][1] < 18, 'Endpoint orientation')
            need(e['class'] in ('seam','horizontal','chamfer'), 'Edge class')
            for key in ('midpoint','half_edge','unit_direction'): point(e[key]); exact(e[key+'_exact'])
        need(float(g['rho']).hex() == '0x1.3a0c09c3e0a95p-1', 'Radius endpoint pin')
        need([p['id'] for p in data['presets']] == list(PRESETS) == manifest['preset_ids'], 'Preset identities')
        need(float(data['presets'][0]['numeric']['C_over_w']).hex() == '0x1.a827999fcef32p-2', 'Chord endpoint pin')
        for p in data['presets']:
            need(p['exact_event'] == (p['id'] if p['id'] in EVENTS else None), 'Preset event')
            need({x['branch'] for x in p['points']} == branches and len(p['points']) == 42, 'Preset branches')
            for v in p['points']: point(v['xyz'])
            need(set(p['numeric']) == {'R_over_w','t_over_w','C_over_w','ell_over_w'}, 'Length fields')
            need(all(type(x) in (float,int) and math.isfinite(x) and x >= 0 for x in p['numeric'].values()), 'Numeric preset')
        for key in ('events','graphs','hulls'): need(set(data[key]) == set(EVENTS), 'Event table')
        for i, event in enumerate(EVENTS):
            entry = data['events'][event]
            need(entry == g['coincidence_events'][i], 'Event list/mapping correspondence')
            need(manifest['event_mapping'][event] == f'/geometry/coincidence_events/{i}', 'Event lineage')
            groups = entry['groups']; labels = [b for q in groups for b in q['branches']]
            need(len(groups)==18 and len(labels)==42 and set(labels)==branches, 'Event partition')
            need(sorted(len(q['branches']) for q in groups)==[2]*12+[3]*6, 'Incidence multiplicities')
            for q in groups: point(q['coordinates']); exact(q['coordinates_exact'])
            graph = data['graphs'][event]; hull = data['hulls'][event]
            need((graph['V'],graph['E']) == ((18,21),(36,63),(54,105))[i], 'Graph counts')
            need(len(graph['vertices'])==graph['V'] and len(graph['edges'])==graph['E'], 'Graph cardinality')
            need([v['id'] for v in graph['vertices']] == list(range(graph['V'])), 'Graph vertex IDs')
            for v in graph['vertices']: point(v['xyz']); exact(v['exact']); need(set(v['branch_labels'])<=branches, 'Graph branches')
            for e in graph['edges']:
                need(len(e['vertices'])==2 and all(type(v) is int and 0<=v<graph['V'] for v in e['vertices']), 'Graph indices')
                need(e['source_edge'] in {x['id'] for x in es}, 'Graph edge source')
            need((hull['V'],hull['E'],hull['F']) == ((18,27,11),(18,48,32),(18,36,20))[i], 'Hull counts')
            need(len(hull['vertices'])==18 and len(hull['faces'])==hull['F'] and len(hull['edges'])==hull['E'], 'Hull cardinality')
            for v in hull['vertices']: point(v['xyz']); exact(v['exact'])
            for f in hull['faces']: cycle(f['vertices'],18)
            for e in hull['edges']: need(len(e['vertices'])==2 and all(type(v) is int and 0<=v<18 for v in e['vertices']), 'Hull edge')
    except (KeyError, TypeError, IndexError, AttributeError) as exc: raise ReferenceError('Malformed reference schema') from exc


@dataclass(frozen=True)
class Reference:
    data: object
    manifest: object

    def __post_init__(self):
        if not isinstance(self.data, MappingProxyType) or not isinstance(self.manifest, MappingProxyType):
            raise TypeError('Reference must be deeply frozen by the validated loader')


def load_reference():
    try:
        base = resources.files('trioctagon_ui')
        with base.joinpath(RESOURCE).open('rb') as f: raw = f.read(422734)
        with base.joinpath(MANIFEST).open('rb') as f: meta = f.read(65537)
    except (OSError, ModuleNotFoundError) as exc: raise ReferenceError('Packaged shell reference unavailable') from exc
    if len(raw)!=422733 or hashlib.sha256(raw).hexdigest()!=RESOURCE_SHA: raise ReferenceError('Shell reference byte identity mismatch')
    if len(meta)>65536 or hashlib.sha256(meta).hexdigest()!=MANIFEST_SHA: raise ReferenceError('Shell manifest byte identity mismatch')
    data, manifest = strict_json(raw), strict_json(meta)
    validate(data, manifest)
    return Reference(freeze(data), freeze(manifest))


def implementation_identity():
    base = resources.files('trioctagon_ui')
    names = ('shell_reference.py','shell_observer.py','shell_panel.py','shell_view.py','shell_exports.py')
    return {'ui_version':'0.2.1', 'component':'SHELL_OBSERVER_V1', 'status':'UNRELEASED_UNCOMMITTED_CANDIDATE',
            'module_sha256':{n:hashlib.sha256(base.joinpath(n).read_bytes()).hexdigest() for n in names},
            'resource_sha256':RESOURCE_SHA, 'manifest_sha256':MANIFEST_SHA}
