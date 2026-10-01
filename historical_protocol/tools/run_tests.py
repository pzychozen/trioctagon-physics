"""External source/installed Historical test runner; records actual package origins."""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile


def main():
    p=argparse.ArgumentParser()
    for name in ('tests','evidence','lane','checkout','core-golden'):p.add_argument('--'+name,required=True)
    p.add_argument('--source');p.add_argument('--wheel');args=p.parse_args()
    assert sys.flags.isolated and sys.flags.dont_write_bytecode
    assert sys.prefix!=sys.base_prefix
    assert 'include-system-site-packages = false' in (Path(sys.prefix)/'pyvenv.cfg').read_text().lower()
    assert not os.environ.get('PYTHONPATH') and not list(Path.cwd().iterdir())
    if args.source:sys.path.insert(0,str(Path(args.source).resolve()))
    sys.path.insert(0,str(Path(args.tests).resolve()))
    network=[]
    def audit(event,data):
        if (event.startswith('socket.') and event!='socket.gethostname') or event=='urllib.Request':
            network.append(event);raise RuntimeError('network forbidden in protocol tests')
    sys.addaudithook(audit)
    import trioctagon_historical_protocol as package
    import trioctagon_analysis as core
    origin=Path(package.__file__).resolve().parent
    if args.wheel:
        assert origin.is_relative_to(Path(sys.prefix))
        with zipfile.ZipFile(args.wheel) as z:
            for name in z.namelist():
                if name.startswith('trioctagon_historical_protocol/'):
                    assert (origin.parent/name).read_bytes()==z.read(name),name
        assert importlib.metadata.version('trioctagon-historical-protocol')=='0.1.0'
    else:assert origin.parent==Path(args.source).resolve()
    assert Path(core.__file__).resolve().is_relative_to(Path(sys.prefix))
    golden=json.loads((Path(args.tests)/'fixtures/TEST_ONLY_golden_vectors.json').read_bytes())
    assert hashlib.sha256(Path(args.core_golden).read_bytes()).hexdigest()==golden['core_golden_sha256']
    import pytest
    evidence=Path(args.evidence);xml=evidence/(args.lane+'-tests.xml')
    code=pytest.main([args.tests,'-q','-p','no:cacheprovider','--rootdir='+args.tests,'--confcutdir='+args.tests,
        '--basetemp='+str(evidence/(args.lane+'-temp')),'--junitxml='+str(xml)])
    assert not network
    assert not any(name.split('.')[0] in {'kernel_physics','kernel_TO','torment_service','trioctagon_historical_kernel','numpy','sympy'} for name in sys.modules)
    origins={name:str(Path(m.__file__).resolve()) for name,m in sys.modules.items()
        if name.startswith(('trioctagon_analysis','trioctagon_historical_protocol')) and getattr(m,'__file__',None)}
    if args.wheel:
        assert all(Path(path).is_relative_to(Path(sys.prefix)) for path in origins.values())
        assert not any(Path(path).resolve().is_relative_to(Path(args.checkout).resolve()) for path in sys.path if path)
    suite=ET.parse(xml).getroot()
    counts={key:sum(int(n.attrib.get(key,0)) for n in suite.findall('testsuite')) for key in ('tests','errors','failures','skipped')}
    (evidence/(args.lane+'-result.json')).write_text(json.dumps(dict(status='PASS' if code==0 else 'FAIL',counts=counts,
        origins=origins,isolated=True,network_attempts=network,scientific_modules_imported=False,
        qualification='INERT_SYNTHETIC_SCHEMA_CLAIMS_ONLY'),indent=2)+'\n')
    raise SystemExit(code)

if __name__=='__main__':main()
