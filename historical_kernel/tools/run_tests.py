"""Source/installed certification with forbidden packages actively denied."""
import argparse,importlib.metadata,json,os,sys,time,xml.etree.ElementTree as ET
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    for key in ('tests','out','checkout','lane'):p.add_argument('--'+key,required=True)
    p.add_argument('--source');p.add_argument('--wheel');a=p.parse_args()
    assert sys.flags.isolated and sys.flags.dont_write_bytecode and sys.prefix!=sys.base_prefix
    sys.path.insert(0,str(Path(__file__).parent))
    from check_imports import install_blocker,audit_package,closure
    attempts=install_blocker()
    if a.source:sys.path.insert(0,str(Path(a.source).resolve()))
    sys.path.insert(0,str(Path(a.tests).resolve()))
    import trioctagon_historical_kernel as package
    origin=Path(package.__file__).resolve().parent
    static=audit_package(origin)
    if a.wheel:
        assert origin.is_relative_to(Path(sys.prefix))
        os.environ['H6B_TEST_WHEEL']=a.wheel
    else:
        assert origin.parent==Path(a.source).resolve()
        os.environ.pop('H6B_TEST_WHEEL',None)
    import pytest
    failures=[]
    if a.wheel:
        from trioctagon_historical_kernel.issuer import LocalIssuer
        from trioctagon_historical_protocol.records import AttemptReceipt
        original=LocalIssuer.issue
        def measured_issue(self,raw,*args,**kwargs):
            started=time.perf_counter_ns();result=original(self,raw,*args,**kwargs)
            if type(result) is AttemptReceipt:
                value=result.to_dict()
                failures.append(dict(category=value['category'],stage=value['stage'],request_bytes=len(raw),
                    receipt_bytes=len(result.to_bytes()),diagnostic_bytes=len(value['diagnostic'].encode()),
                    updates_completed=value['updates_completed'],wall_microseconds=(time.perf_counter_ns()-started)//1000))
            return result
        LocalIssuer.issue=measured_issue
    out=Path(a.out);xml=out/(a.lane+'-tests.xml')
    code=pytest.main([a.tests,'-q','-p','no:cacheprovider','--rootdir='+a.tests,'--confcutdir='+a.tests,
                     '--basetemp='+str(out/(a.lane+'-temp')),'--junitxml='+str(xml)])
    origins=closure();assert not attempts
    if a.wheel:
        assert all(Path(v).is_relative_to(Path(sys.prefix)) for v in origins.values())
        assert not any(Path(v).is_relative_to(Path(a.checkout)) for v in sys.path if v)
        assert importlib.metadata.packages_distributions().get('kernel_physics') is None
    suites=ET.parse(xml).getroot().findall('testsuite')
    counts={k:sum(int(s.attrib.get(k,0)) for s in suites) for k in ('tests','failures','errors','skipped')}
    if a.wheel:
        (out/'failure-observations.json').write_text(json.dumps(dict(schema='H6B_FAILURE_OBSERVATIONS_1',rows=failures),indent=2)+'\n')
    (out/(a.lane+'-result.json')).write_text(json.dumps(dict(status='PASS' if not code else 'FAIL',counts=counts,
        origins=origins,static_imports=static,forbidden_import_attempts=attempts,current_science_available=False,
        isolation=bool(sys.flags.isolated),source_lane=bool(a.source)),indent=2)+'\n')
    raise SystemExit(code)

if __name__=='__main__':main()
