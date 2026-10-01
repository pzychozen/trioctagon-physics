"""Create external build/measurement/catalogue pins only after all local gates pass."""
import argparse,hashlib,json,sys
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    for k in ('evidence','source','tests','wheel'):p.add_argument('--'+k,required=True)
    args=p.parse_args();e=Path(args.evidence);source=Path(args.source)
    sys.path.insert(0,str(Path(__file__).parent));sys.path.insert(0,args.tests)
    from evidence_formats import SourceManifest,ConformanceManifest,MeasurementTable,MeasurementManifest
    from check_imports import SCIENCE
    from installed_support import request
    from trioctagon_historical_kernel.installation import inventory,DISTRIBUTIONS,manifest_sha,runtime
    from trioctagon_historical_kernel.admission import Admission
    from trioctagon_historical_kernel.issuer import LocalIssuer
    from trioctagon_historical_protocol.schema import PROTOCOL,PROFILE,CONTRACT,IMPLEMENTATION
    from trioctagon_historical_protocol.packets import ProviderBuild,ResourcePolicy,NUMERICAL_POLICIES,authority_packet,constants_packet,frozen
    from trioctagon_historical_protocol.catalogue import Catalogue
    from trioctagon_historical_protocol.records import DerivedRecord
    from trioctagon_historical_protocol.definitions import OPERATIONS,descriptor_template
    def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    def read(path):return json.loads(Path(path).read_bytes())
    inputs=read(e/'source-inputs.json')
    runs={k:read(e/(k+'-result.json')) for k in ('source','installed')}
    protocol=read(e/'protocol/installed-result.json')
    core_lane='candidate' if inputs['revision'] is None else 'certified'
    core=read(e.parent/'core'/core_lane/'evidence/installed-result.json')
    for result in (*runs.values(),protocol,core):assert result['status']=='PASS'
    assert runs['installed']['counts']['skipped']==0
    assert read(e/'external-comparison.json')['status']=='PASS'
    assert read(e/'negative-control.json')['status']=='PASS'
    src=SourceManifest(dict(schema='H6B_SOURCE_MANIFEST_1',revision=inputs['revision'],members=[
        dict(path=n,bytes=(source/n).stat().st_size,sha256=h) for n,h in sorted(inputs['files'].items())]))
    (e/'source-manifest.json').write_bytes(src.to_bytes())
    conformance=ConformanceManifest(dict(schema='H6B_CONFORMANCE_1',status='PASS',source=src.identity.to_dict(),
        wheel_sha256=sha(args.wheel),authority_sha256=hashlib.sha256(authority_packet().to_bytes()).hexdigest(),
        rules=read(source/'tools/conformance_map.json'),source_tests=runs['source']['counts'],installed_tests=runs['installed']['counts'],
        protocol_tests=protocol['counts'],core_tests=core['counts'],fixture_sha256=sha(source/'tests/fixtures/h2_applicable.json'),
        external_comparison_sha256=sha(e/'external-comparison.json'),dependency_closure_sha256=sha(e/'installed-result.json'),
        negative_control_sha256=sha(e/'negative-control.json'),negative_matrix={n:'PASS' for n in ('N06','N17','N28','N30','N31','N33','N36','N37')}))
    (e/'conformance-manifest.json').write_bytes(conformance.to_bytes())
    installed=sorted((inventory(n) for n in DISTRIBUTIONS),key=lambda x:x['id']);own=next(v for v in installed if v['id']=='trioctagon-historical-kernel')
    members=[dict(**r,role=('SCIENTIFIC_IMPLEMENTATION' if Path(r['path']).stem in SCIENCE else 'GENERIC_INFRASTRUCTURE')
        if '/trioctagon_historical_kernel/' in r['path'] else 'PACKAGE_METADATA') for r in own['members']]
    deps=[dict(id=v['id'],version=v['version'],manifest_sha256=manifest_sha(v),role='NUMERIC_LIBRARY' if v['id']=='numpy' else 'NONSCIENTIFIC_INFRASTRUCTURE') for v in installed if v is not own]
    build=ProviderBuild(dict(family='TRIOCTAGON_HISTORICAL_PROVIDER_BUILD',schema='1.0.0',provider_id='historical.reference',provider_revision=1,
        implementation_policy=IMPLEMENTATION,source=dict(repository_id='pzychozen/trioctagon-physics',revision=inputs['revision'],content_manifest_digest=src.identity.to_dict()),
        archive_sha256=sha(args.wheel),members=members,dependencies=deps,numerical_policy_ids=list(NUMERICAL_POLICIES),conformance_digest=conformance.identity.to_dict()))
    (e/'provider-build.json').write_bytes(build.to_bytes())
    table=MeasurementTable(read(e/'measurement/measurement.json'));m=table.to_dict()['maxima'];assert table.to_dict()['wheel_sha256']==sha(args.wheel)
    failures=read(e/'failure-observations.json')['rows']
    diagnostic_max=max(row['diagnostic_bytes'] for row in failures)
    wall_max=max(m['wall_microseconds'],max(row['wall_microseconds'] for row in failures))
    def rounded(n,unit):return ((n+unit-1)//unit)*unit
    limits=dict(max_updates=1024,input_bytes=rounded(4*m['request_bytes'],1024),output_bytes=rounded(4*m['artifact_bytes'],1024**2),
        json_depth=m['json_depth']+4,wall_milliseconds=rounded((4*wall_max+999)//1000,1000),
        memory_bytes=rounded(2*m['peak_memory_bytes'],64*1024**2),diagnostic_bytes=rounded(4*diagnostic_max,32),
        manifest_bytes=rounded(4*max(m['build_bytes'],m['execution_evidence_bytes']),4096))
    observed=dict(max_updates=1024,input_bytes=m['request_bytes'],output_bytes=m['artifact_bytes'],json_depth=m['json_depth'],
        wall_milliseconds=(wall_max+999)//1000,memory_bytes=m['peak_memory_bytes'],diagnostic_bytes=diagnostic_max,
        manifest_bytes=max(m['build_bytes'],m['execution_evidence_bytes']))
    reasons=dict(max_updates='Largest complete matrix tested across every frozen k/readout; linear row storage; no extrapolation.',
        input_bytes='Fixed schema and binary64 token widths; 4x measured complete request plus 1 KiB rounding.',
        output_bytes='4x largest full canonical artifact, rounded to MiB; includes bundle, evidence and terminal.',
        json_depth='Measured deepest artifact plus four containers; unknown fields still fail schema validation.',
        wall_milliseconds='4x slowest end-to-end observation, rounded to seconds, with fail-closed deadline enforcement.',
        memory_bytes='2x observed combined conservative worker/launcher peak, rounded to 64 MiB; host-specific NumPy overhead retained.',
        diagnostic_bytes='4x longest actually observed failure diagnostic, rounded to 32 bytes; only fixed category labels emitted.',
        manifest_bytes='4x larger embedded build/evidence structure, rounded to 4 KiB; separately enforced.')
    selection=[dict(field=k,observed=observed[k],limit=limits[k],margin=f'{limits[k]}/{observed[k]}',reason=reasons[k]) for k in limits]
    measured=MeasurementManifest(dict(schema='H6B_MEASURED_BUILD_1',build=build.identity.to_dict(),table=table.to_dict(),
        failure_tests_sha256=sha(e/'installed-tests.xml'),failure_observations_sha256=sha(e/'failure-observations.json'),policy_selection=selection))
    (e/'measurement-manifest.json').write_bytes(measured.to_bytes())
    policy=ResourcePolicy(dict(family='TRIOCTAGON_HISTORICAL_RESOURCE_POLICY',schema='1.0.0',state='MEASURED_ADMITTED_LOCAL',measurement_manifest=measured.identity.to_dict(),limits=limits))
    key=dict(id='historical.reference',revision=1,build=build.identity.to_dict())
    catalogue=Catalogue(dict(family='TRIOCTAGON_HISTORICAL_ANALYSIS_CATALOGUE',schema='1.0.0',protocol=PROTOCOL,profile=PROFILE,contract=CONTRACT,
        implementation_policy=IMPLEMENTATION,authority=authority_packet().identity.to_dict(),constants_packet=constants_packet().identity.to_dict(),
        provider_builds=[key],resource_policy=policy.identity.to_dict(),descriptors=[descriptor_template(op) for op in OPERATIONS],comparison_evidence=frozen('comparison')))
    admission=Admission(dict(schema='H6B_LOCAL_ADMISSION_1',catalogue=catalogue.to_dict(),build=build.to_dict(),resource=policy.to_dict(),runtime=runtime(),
        installed=installed,conformance=conformance.identity.to_dict(),measurement=measured.identity.to_dict(),
        review=dict(state='LOCAL_REVIEW_ACCEPTED',scope='UNATTESTED_HISTORICAL_ONLY',windows_execution_binding='NOT_PROVEN',production_attestation_enabled=False)))
    for name,value in [('resource-policy',policy),('catalogue',catalogue),('local-admission',admission)]: (e/(name+'.json')).write_bytes(value.to_bytes())
    pin=sha(e/'local-admission.json');local=LocalIssuer(e/'local-admission.json',pin)
    issued=[]
    # Real admitted smoke proof includes the largest selected run and all five operations.
    for index in range(5):
        q=request(admission,index,updates=1024,readout='HISTORICAL_COGNITIVE_EMA_Z_H')
        result=local.issue(q.to_bytes(),e/f'admitted-result-{index}.json')
        assert type(result) is DerivedRecord,result.to_dict()
        issued.append(dict(operation=OPERATIONS[index],sha256=hashlib.sha256(result.to_bytes()).hexdigest()))
    result=dict(status='PASS',build=build.identity.to_dict(),resource=policy.identity.to_dict(),catalogue=catalogue.identity.to_dict(),
        admission_sha256=pin,limits=limits,issued=issued,review='LOCAL_CODE_AND_CONFORMANCE_REVIEW; NOT_HUMAN_SIGNATURE_OR_B2_ATTESTATION',
        runtime_prefix=sys.prefix,windows_execution_binding='NOT_PROVEN',production_attestation_enabled=False)
    (e/'local-admission-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
