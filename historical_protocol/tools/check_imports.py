"""Fresh-process schema import closure and static no-provider audit. Never installed."""
import argparse
import ast
import importlib
import importlib.abc
import json
from pathlib import Path
import sys

MODULES=frozenset(('__init__ catalogue codec definitions digests errors evidence packets payloads records requests schema').split())
FORBIDDEN=('kernel_physics','kernel_TO','torment_service','trioctagon_ui','trioctagon_historical_kernel','numpy','sympy')
GENERIC={'trioctagon_analysis','trioctagon_analysis.codec','trioctagon_analysis.digests',
         'trioctagon_analysis.errors','trioctagon_analysis.schema','trioctagon_analysis.envelope'}
STDLIB={'copy','datetime','hashlib','importlib.resources','json','re'}


def audit_package(package):
    assert {p.stem for p in package.glob('*.py')}==MODULES
    for p in package.glob('*.py'):
        tree=ast.parse(p.read_text(encoding='utf-8'))
        for node in ast.walk(tree):
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
                assert node.name not in {'execute','run_provider','issue','issue_success','coordinate','run','step'},(p,node.name)
            if isinstance(node,ast.Call):
                assert not (isinstance(node.func,ast.Name) and node.func.id in {'eval','exec','compile','__import__'})
            if isinstance(node,ast.Import):names=[alias.name for alias in node.names]
            elif isinstance(node,ast.ImportFrom):
                if node.level:
                    assert node.module in MODULES,(p,node.module)
                    continue
                names=[node.module]
            else:continue
            assert all(name in STDLIB|GENERIC for name in names),(p,names)
    assert {p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file()}=={
        *(name+'.py' for name in MODULES),'data/authority.json','data/constants.json','data/comparison.json'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source');parser.add_argument('--out',required=True)
    args=parser.parse_args()
    assert sys.flags.isolated and sys.flags.dont_write_bytecode
    if args.source:sys.path.insert(0,str(Path(args.source).resolve()))
    attempts=[]
    class Deny(importlib.abc.MetaPathFinder):
        def find_spec(self,fullname,path=None,target=None):
            if fullname.split('.')[0] in FORBIDDEN:
                attempts.append(fullname);raise AssertionError('scientific import forbidden: '+fullname)
    sys.meta_path.insert(0,Deny())
    for name in sorted(MODULES):importlib.import_module('trioctagon_historical_protocol'+('' if name=='__init__' else '.'+name))
    package=Path(sys.modules['trioctagon_historical_protocol'].__file__).parent
    audit_package(package)
    assert not attempts and not any(n.split('.')[0] in FORBIDDEN for n in sys.modules)
    closure={name:str(Path(module.__file__).resolve()) for name,module in sys.modules.items()
        if name.startswith(('trioctagon_historical_protocol','trioctagon_analysis')) and getattr(module,'__file__',None)}
    assert {name for name in closure if name.startswith('trioctagon_analysis')}==GENERIC
    Path(args.out).write_text(json.dumps({'status':'PASS','scientific_import_attempts':attempts,'closure':closure,
        'issuer_present':False,'provider_present':False,'qualification':'SCHEMA_IMPORT_AND_SOURCE_BOUNDARY_ONLY'},indent=2)+'\n')

if __name__=='__main__':main()
