"""TEST_ONLY local pins for installed issuer tests, never real build/catalogue admission."""
import hashlib
from pathlib import Path
from trioctagon_historical_kernel.installation import inventory,DISTRIBUTIONS,manifest_sha,runtime
from trioctagon_historical_kernel.admission import Admission
from trioctagon_historical_protocol import digests as d
from trioctagon_historical_protocol.schema import PROTOCOL,PROFILE,CONTRACT,IMPLEMENTATION
from trioctagon_historical_protocol.packets import ProviderBuild,ResourcePolicy,NUMERICAL_POLICIES,authority_packet,constants_packet,frozen
from trioctagon_historical_protocol.catalogue import Catalogue
from trioctagon_historical_protocol.definitions import OPERATIONS,descriptor_template,resolved_constants,numerical_policy
from trioctagon_historical_protocol.requests import Request,request_digest


def fake(kind, name):
    return kind(hashlib.sha256(('TEST_ONLY_NOT_ADMITTED:'+name).encode()).hexdigest()).to_dict()


def admission(directory, wheel, **limits_override):
    installed=sorted((inventory(name) for name in DISTRIBUTIONS),key=lambda row:row['id'])
    own=next(row for row in installed if row['id']=='trioctagon-historical-kernel')
    members=[dict(**row,role='SCIENTIFIC_IMPLEMENTATION' if '/trioctagon_historical_kernel/' in row['path'] else 'PACKAGE_METADATA')
             for row in own['members']]
    dependencies=[dict(id=inv['id'],version=inv['version'],manifest_sha256=manifest_sha(inv),
        role='NUMERIC_LIBRARY' if inv['id']=='numpy' else 'NONSCIENTIFIC_INFRASTRUCTURE') for inv in installed if inv is not own]
    build=ProviderBuild(dict(family='TRIOCTAGON_HISTORICAL_PROVIDER_BUILD',schema='1.0.0',provider_id='historical.reference',provider_revision=1,
        implementation_policy=IMPLEMENTATION,source=dict(repository_id='TEST_ONLY_NOT_ADMITTED',revision=None,content_manifest_digest=fake(d.ManifestDigest,'source')),
        archive_sha256=hashlib.sha256(Path(wheel).read_bytes()).hexdigest(),members=members,dependencies=dependencies,
        numerical_policy_ids=list(NUMERICAL_POLICIES),conformance_digest=fake(d.ConformanceDigest,'conformance')))
    limits=dict(max_updates=64,input_bytes=32768,output_bytes=8*1024*1024,json_depth=64,
        wall_milliseconds=30000,memory_bytes=1024*1024*1024,diagnostic_bytes=256,manifest_bytes=1024*1024)
    limits.update(limits_override)
    resource=ResourcePolicy(dict(family='TRIOCTAGON_HISTORICAL_RESOURCE_POLICY',schema='1.0.0',state='MEASURED_ADMITTED_LOCAL',
        measurement_manifest=fake(d.ManifestDigest,'TEST_ONLY_limits_not_production_measurement'),limits=limits))
    key=dict(id='historical.reference',revision=1,build=build.identity.to_dict())
    catalogue=Catalogue(dict(family='TRIOCTAGON_HISTORICAL_ANALYSIS_CATALOGUE',schema='1.0.0',protocol=PROTOCOL,profile=PROFILE,
        contract=CONTRACT,implementation_policy=IMPLEMENTATION,authority=authority_packet().identity.to_dict(),
        constants_packet=constants_packet().identity.to_dict(),provider_builds=[key],resource_policy=resource.identity.to_dict(),
        descriptors=[descriptor_template(op) for op in OPERATIONS],comparison_evidence=frozen('comparison')))
    value=Admission(dict(schema='H6B_LOCAL_ADMISSION_1',catalogue=catalogue.to_dict(),build=build.to_dict(),resource=resource.to_dict(),
        runtime=runtime(),installed=installed,conformance=build.to_dict()['conformance_digest'],measurement=resource.to_dict()['measurement_manifest'],
        review=dict(state='LOCAL_REVIEW_ACCEPTED',scope='UNATTESTED_HISTORICAL_ONLY',windows_execution_binding='NOT_PROVEN',production_attestation_enabled=False)))
    path=Path(directory)/'TEST_ONLY_admission.json';path.write_bytes(value.to_bytes())
    return value,path,hashlib.sha256(value.to_bytes()).hexdigest()


def request(a,index=0,updates=2,readout='NONE',profile='HISTORICAL_THETA_SCALED',omega=None):
    if omega is None:omega=[{'real':{'f64':r.hex()},'imag':{'f64':i.hex()}} for r,i in ((.2,.3),(-.4,.1),(.1,-.2))]
    args=({'k_profile':profile},{'k_profile':profile,'updates':updates,'readout':readout},{'q':3,'t':{'f64':(.5).hex()}},
          {'q':3,'t':{'f64':(.5).hex()},'memory':{'f64':(-0.).hex()}},{})[index]
    v=a.to_dict();c=Catalogue(v['catalogue'])
    body=dict(protocol=PROTOCOL,operation=OPERATIONS[index],revision=1,profile=PROFILE,contract=CONTRACT,implementation_policy=IMPLEMENTATION,
        catalogue=c.identity.to_dict(),descriptor=c.descriptor(OPERATIONS[index]).identity.to_dict(),authority=c.to_dict()['authority'],
        constants_packet=c.to_dict()['constants_packet'],provider=c.to_dict()['provider_builds'][0],resource_policy=c.to_dict()['resource_policy'],
        input=dict(kind='EXPLICIT_RAW_TRIAD',omega=omega),arguments=args,resolved_constants=resolved_constants(OPERATIONS[index],args),
        numerical_policy=numerical_policy(OPERATIONS[index],args))
    result=dict(family='TRIOCTAGON_HISTORICAL_ANALYSIS_REQUEST',schema='1.0.0',body=body)
    result['request_digest']=request_digest(result).to_dict()
    return Request(result)
