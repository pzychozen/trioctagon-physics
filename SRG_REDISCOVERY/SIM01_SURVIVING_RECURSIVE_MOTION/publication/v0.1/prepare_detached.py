"""Extract only reviewed numerical ASTs. Never import historical modules."""
import ast
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPECS = {
    'A': dict(constants=(5, 7), init=[10, 11], helpers=['H', 'RPCO', 'TGMO'],
              frame='step', excluded=[42, 57, 59]),
    'B': dict(constants=(8, 12), init=[15, 16], helpers=['wrap_position', 'H', 'RPCO', 'GRF'],
              frame='frame', last=96),
    'C': dict(constants=(10, 14), init=[17, 18, 152],
              helpers=['wrap_position', 'H', 'RPCO', 'GRF', 'compute_energy', 'detect_teleport'],
              frame='frame', last=126, excluded=[107]),
}


def fingerprint(nodes):
    return hashlib.sha256(ast.dump(ast.Module(body=nodes, type_ignores=[]),
                                 include_attributes=False).encode()).hexdigest()


def build():
    records = {}
    for name, spec in SPECS.items():
        path = ROOT / 'sources' / f'source_{name}.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
        constants = [copy.deepcopy(n) for n in tree.body
                     if spec['constants'][0] <= n.lineno <= spec['constants'][1]]
        initial = [copy.deepcopy(n) for n in tree.body if n.lineno in spec['init']]
        if name == 'A':
            loop = next(n for n in tree.body if isinstance(n, ast.For) and n.lineno == 38)
            body = copy.deepcopy(loop.body)
            body = [n for n in body if n.lineno not in spec['excluded']]
            center = next(n for n in body if isinstance(n, ast.For))
            center.body = [n for n in center.body if n.lineno not in spec['excluded']]
            body.insert(0, ast.Global(names=['positions', 'velocities']))
        else:
            body = [copy.deepcopy(n) for n in funcs['update'].body
                    if n.lineno <= spec['last'] and n.lineno not in spec.get('excluded', [])]
        original_fingerprint = fingerprint(body)
        retained = sorted({n.lineno for item in body for n in ast.walk(item)
                           if hasattr(n, 'lineno')})
        center = next(n for n in body if isinstance(n, ast.For))
        for event, index in [('after', len(center.body)), ('before', 0)]:
            node = ast.parse(f"if _trace is not None: _trace('{event}', i, positions, velocities)").body[0]
            center.body.insert(index, node)
        return_code = "return {'t': t, 'H': h_val, 'G': " + ('None' if name == 'A' else 'grf_val') + "}"
        step = ast.FunctionDef(name='numerical_step', args=ast.arguments(posonlyargs=[],
            args=[ast.arg(arg=spec['frame']), ast.arg(arg='_trace')], kwonlyargs=[],
            kw_defaults=[], defaults=[ast.Constant(None)]), body=body + ast.parse(return_code).body,
            decorator_list=[])
        globals_ = ['positions', 'velocities'] + (['rule_state'] if name == 'C' else [])
        init = ast.FunctionDef(name='initialize', args=ast.arguments(posonlyargs=[], args=[],
            kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Global(names=globals_)] + initial,
            decorator_list=[])
        output_tree = ast.Module(body=[ast.Import(names=[ast.alias(name='numpy', asname='np')])]
            + constants + [copy.deepcopy(funcs[n]) for n in spec['helpers']] + [init, step], type_ignores=[])
        ast.fix_missing_locations(output_tree)
        dest = ROOT / 'detached' / f'engine_{name}.py'
        dest.write_text('# Generated from reviewed original; see EXTRACTION_MAP.json.\n'
                        + ast.unparse(output_tree) + '\n', encoding='utf-8')
        actual = ast.parse(dest.read_text()).body
        generated_step = next(n for n in actual if isinstance(n, ast.FunctionDef) and n.name == 'numerical_step')
        stripped = copy.deepcopy(generated_step.body[:-1])
        center = next(n for n in stripped if isinstance(n, ast.For))
        center.body = [n for n in center.body if not (isinstance(n, ast.If)
            and ast.unparse(n.test) == '_trace is not None')]
        assert fingerprint(stripped) == original_fingerprint
        for helper in spec['helpers']:
            got = next(n for n in actual if isinstance(n, ast.FunctionDef) and n.name == helper)
            assert ast.dump(got, include_attributes=False) == ast.dump(funcs[helper], include_attributes=False)
        got_init = next(n for n in actual if isinstance(n, ast.FunctionDef) and n.name == 'initialize')
        assert fingerprint(got_init.body[1:]) == fingerprint(initial)
        records[name] = dict(source=str(path.relative_to(ROOT)), source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            detached=str(dest.relative_to(ROOT)), detached_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
            constant_lines=spec['constants'], initialization_lines=spec['init'], helper_lines={n:[funcs[n].lineno, funcs[n].end_lineno] for n in spec['helpers']},
            retained_step_statement_lines=retained, numeric_ast_sha256=original_fingerprint,
            round_trip_ast_equal=True, helpers_ast_equal=True, initialization_ast_equal=True,
            changes='Original arithmetic, indexing and order retained. Original GUI/file/print/history observers omitted. Optional read-only trace calls added around each center and metadata returned. Initial draws moved into initialize(); no historical top-level module imported.')
    (ROOT/'evidence/EXTRACTION_MAP.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'extractions':len(records),'AST_fidelity':'PASS','numerical_updates':0}))


if __name__ == '__main__':
    build()
