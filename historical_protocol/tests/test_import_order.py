"""Family routing is unchanged by import order, including in an isolated interpreter."""
import json
from pathlib import Path
import subprocess
import sys
import pytest
import trioctagon_analysis
import trioctagon_historical_protocol


@pytest.mark.parametrize('core_first',[False,True])
def test_N31_N33_N38_import_order_cannot_broaden_families(core_first):
    paths=[str(Path(m.__file__).resolve().parent.parent) for m in (trioctagon_analysis,trioctagon_historical_protocol)]
    script=r'''
import sys,json,importlib,importlib.abc
from pathlib import Path
paths,fixtures,core_first=json.loads(sys.argv[1]);sys.path[:0]=paths
class Deny(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname,path=None,target=None):
        if fullname.split('.')[0] in {'kernel_physics','kernel_TO','torment_service','numpy','sympy','trioctagon_historical_kernel'}:
            raise AssertionError(fullname)
sys.meta_path.insert(0,Deny())
order=['trioctagon_analysis','trioctagon_historical_protocol']
if not core_first:order.reverse()
for root in order:
    for name in ['records','requests','catalogue']:importlib.import_module(root+'.'+name)
from trioctagon_analysis.digests import CONTENT_TYPES as core
from trioctagon_historical_protocol.digests import CONTENT_TYPES as historical
assert not core.intersection(historical)
from trioctagon_analysis.records import DerivedAnalysisRecord
from trioctagon_historical_protocol.records import DerivedRecord
for owner,name in [(DerivedRecord,'TEST_ONLY_core_result.json'),(DerivedAnalysisRecord,'TEST_ONLY_result_0.json')]:
    try:owner(json.loads((Path(fixtures)/name).read_bytes()))
    except ValueError:pass
    else:raise AssertionError('cross-family claim accepted')
print('PASS')
'''
    result=subprocess.run([sys.executable,'-I','-B','-c',script,json.dumps([paths,str(Path(__file__).parent/'fixtures'),core_first])],
        capture_output=True,text=True)
    assert result.returncode==0,result.stdout+result.stderr
    assert result.stdout.strip()=='PASS'
