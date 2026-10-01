"""External TEST_ONLY measurement envelope; no real catalogue is admitted here."""
import argparse,hashlib,json,sys,time
from pathlib import Path


def depth(value):
    if isinstance(value,dict):return 1+max((depth(v) for v in value.values()),default=0)
    if isinstance(value,list):return 1+max((depth(v) for v in value),default=0)
    return 0


def main():
    p=argparse.ArgumentParser()
    for key in ('tests','wheel','out'):p.add_argument('--'+key,required=True)
    a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
    sys.path.insert(0,str(Path(a.tests)))
    from installed_support import admission,request
    from trioctagon_historical_kernel import issuer
    from trioctagon_historical_protocol.records import DerivedRecord
    from trioctagon_historical_protocol.payloads import Payload
    from trioctagon_historical_protocol.evidence import ExecutionEvidence
    from trioctagon_historical_protocol.packets import K_NAMES,READOUTS,ProviderBuild
    # Temporary experiment containment: one task, 1024 updates, 60s, 4 GiB,
    # 16 MiB aggregate. These are NOT a proposed/admitted operational policy.
    # The initial 36-cell pilot measured 932,995,072 bytes, predominantly NumPy
    # import (standalone probe 866,676,736 bytes). Four GiB leaves >4x pilot
    # headroom; the escalation gate still requires <1/4 of this envelope.
    context,path,pin=admission(out,a.wheel,max_updates=1024,wall_milliseconds=60000,
        memory_bytes=4*1024**3,output_bytes=16*1024**2)
    monitor={'peak':0,'event':None};get=issuer.queue.Queue.get;exceeded=issuer.ProcessBudget.exceeded
    def recorded_get(self,*args,**kwargs):
        e=get(self,*args,**kwargs)
        if isinstance(e,dict) and e.get('kind')=='candidate':monitor['event']=e
        return e
    def recorded_budget(self,*args):
        value=exceeded(self,*args);monitor['peak']=max(monitor['peak'],self.peak);return value
    issuer.queue.Queue.get=recorded_get;issuer.ProcessBudget.exceeded=recorded_budget
    local=issuer.LocalIssuer(path,pin);rows=[]
    def measure(index,**kwargs):
        q=request(context,index,**kwargs);raw=q.to_bytes();monitor.update(peak=0,event=None)
        started=time.perf_counter_ns();destination=out/('artifact-'+str(len(rows))+'.json')
        result=local.issue(raw,destination);wall_us=(time.perf_counter_ns()-started)//1000
        encoded=result.to_bytes();v=result.to_dict();success=type(result) is DerivedRecord
        e=monitor['event'] or {}
        row=dict(operation=q.to_dict()['body']['operation'],arguments=q.to_dict()['body']['arguments'],
            input_sha256=hashlib.sha256(raw).hexdigest(),request_bytes=len(raw),artifact_bytes=len(encoded),
            result_bytes=len(Payload(v['payload']).to_bytes()) if success else 0,
            execution_evidence_bytes=len(ExecutionEvidence(v['execution_evidence']).to_bytes()) if success else 0,
            build_bytes=len(ProviderBuild(v['contract_bundle']['provider_build']).to_bytes()) if success else 0,
            json_depth=depth(v),wall_microseconds=wall_us,peak_memory_bytes=monitor['peak'],
            startup_microseconds=e.get('startup_microseconds',0),scan_microseconds=e.get('scan_microseconds',0),
            serialization_microseconds=e.get('serialization_microseconds',0),outcome='COMPLETE' if success else v['category'],
            artifact_sha256=hashlib.sha256(encoded).hexdigest())
        if not success:(out/('receipt-'+str(len(rows))+'.json')).write_bytes(encoded)
        rows.append(row)
        (out/'progress.json').write_text(json.dumps(rows,indent=2)+'\n')
        print(index,kwargs.get('updates','bounded'),row['outcome'],wall_us//1000,flush=True)
        return success
    for n in (0,1,2,64,256,1024):
        if n>64:
            # Measured escalation gate: prior complete rows consume < 1/4 of
            # experiment time/memory/output caps, leaving room to stop safely.
            assert all(r['wall_microseconds']<15000000 and r['peak_memory_bytes']<1024**3
                       and r['artifact_bytes']<4*1024**2 for r in rows)
        for profile in K_NAMES:
            for readout in READOUTS:assert measure(1,updates=n,profile=profile,readout=readout)
    for profile in K_NAMES:assert measure(0,profile=profile)
    for index in (2,3,4):assert measure(index)
    for scale in (0.,1e-200,1e308):
        omega=[dict(real={'f64':scale.hex()},imag={'f64':(0.).hex()})]*3
        for index in (0,2,3,4):measure(index,omega=omega)
    maxima={key:max(r[key] for r in rows) for key in ('request_bytes','artifact_bytes','result_bytes','execution_evidence_bytes',
        'build_bytes','json_depth','wall_microseconds','peak_memory_bytes','startup_microseconds','scan_microseconds','serialization_microseconds')}
    evidence=dict(schema='H6B_MEASUREMENT_1',qualification='TEST_ONLY_MEASUREMENT_ENVELOPE_NOT_REAL_ADMISSION',
        wheel_sha256=hashlib.sha256(Path(a.wheel).read_bytes()).hexdigest(),rows=rows,maxima=maxima,
        environment=context.to_dict()['runtime'],memory_definition='SUM_LAUNCHER_AND_WORKER_PEAK_RESIDENT_PLUS_PEAK_PRIVATE_COMMIT',
        negative_tests='installed-tests.xml: malformed, oversized, wall, memory, output, manifest, cancellation, concurrency, publication')
    (out/'measurement.json').write_text(json.dumps(evidence,indent=2)+'\n')

if __name__=='__main__':main()
