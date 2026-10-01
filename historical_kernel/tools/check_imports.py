"""Static allowlist plus exercised runtime closure; never part of the provider wheel."""
import ast
import importlib.abc
import json
from pathlib import Path
import sys

FORBIDDEN={'kernel_physics','kernel_TO','torment_service','trioctagon_ui','sympy'}
GENERIC={'trioctagon_analysis','trioctagon_analysis.codec','trioctagon_analysis.digests',
         'trioctagon_analysis.errors','trioctagon_analysis.schema','trioctagon_analysis.envelope'}
MODULES=set('api admission artifacts chirality clock constants dynamics ema_z history installation issuer numerics phase probability_chart provider resources response staged_z types worker __init__'.split())
SCIENCE=set('api chirality clock constants dynamics ema_z history numerics phase probability_chart response staged_z types'.split())


def audit_package(package):
    assert {p.name for p in package.rglob('*') if p.is_file()}=={m+'.py' for m in MODULES}
    imports=[]
    for p in sorted(package.glob('*.py')):
        tree=ast.parse(p.read_text(encoding='utf-8'))
        for node in ast.walk(tree):
            if isinstance(node,ast.Call):
                assert not (isinstance(node.func,ast.Name) and node.func.id in {'eval','exec','compile','__import__'})
                assert not (isinstance(node.func,ast.Attribute) and node.func.attr in {'import_module','entry_points','load_module','exec_module'}),(p,node.lineno)
            if isinstance(node,ast.Import):names=[a.name for a in node.names]
            elif isinstance(node,ast.ImportFrom):
                if node.level:
                    names=[node.module] if node.module else [a.name for a in node.names]
                    assert node.level==1 and all(name in MODULES for name in names),(p,names)
                    if p.stem in SCIENCE:assert all(name in SCIENCE for name in names),(p,names)
                    continue
                names=[node.module]
            else:continue
            for name in names:
                root=name.split('.')[0]
                assert root not in FORBIDDEN
                assert root in sys.stdlib_module_names|{'numpy','trioctagon_historical_protocol'},(p,name)
                if p.stem in SCIENCE:assert root in sys.stdlib_module_names|{'numpy'}
                imports.append(dict(file=p.name,line=node.lineno,module=name))
    return imports


def install_blocker():
    attempts=[]
    class Deny(importlib.abc.MetaPathFinder):
        def find_spec(self,fullname,path=None,target=None):
            if fullname.split('.')[0] in FORBIDDEN:
                attempts.append(fullname)
                raise AssertionError('FORBIDDEN_CURRENT_SCIENCE_IMPORT: '+fullname)
    sys.meta_path.insert(0,Deny())
    return attempts


def closure():
    assert not any(n.split('.')[0] in FORBIDDEN for n in sys.modules)
    generic={n for n in sys.modules if n.startswith('trioctagon_analysis')}
    assert generic <= GENERIC, generic-GENERIC
    return {n:str(Path(m.__file__).resolve()) for n,m in sys.modules.items()
            if n.startswith(('trioctagon_historical','trioctagon_analysis','numpy')) and getattr(m,'__file__',None)}
