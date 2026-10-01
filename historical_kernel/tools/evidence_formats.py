"""Closed inert H6B certification formats, external to the scientific wheel."""
from trioctagon_historical_protocol.schema import s,Document,embedded,safe_members
from trioctagon_historical_protocol.digests import ManifestDigest,ConformanceDigest,ProviderBuildDigest
from trioctagon_historical_protocol.requests import _ARGS
from trioctagon_historical_protocol.definitions import OPERATIONS
from trioctagon_historical_kernel.admission import runtime_schema

COUNTS=s.obj(tests=s.integer,failures=s.literal(0),errors=s.literal(0),skipped=s.integer)
SIZES=('request_bytes','artifact_bytes','result_bytes','execution_evidence_bytes','build_bytes','json_depth',
       'wall_microseconds','peak_memory_bytes','startup_microseconds','scan_microseconds','serialization_microseconds')


class SourceManifest(Document):
    digest_type=ManifestDigest
    schema=s.obj(schema=s.literal('H6B_SOURCE_MANIFEST_1'),revision=s.nullable(s.revision),
                 members=s.seq(s.obj(path=s.text,bytes=s.integer,sha256=s.hex256),1))
    @classmethod
    def validate(cls,value):safe_members(value['members'])


class ConformanceManifest(Document):
    digest_type=ConformanceDigest
    schema=s.obj(schema=s.literal('H6B_CONFORMANCE_1'),status=s.literal('PASS'),
        source=s.digest(ManifestDigest),wheel_sha256=s.hex256,authority_sha256=s.hex256,
        rules=s.seq(s.obj(id=s.text,source=s.text,equation=s.text,contract=s.text,
                         implementation=s.text,tests=s.seq(s.text,1),qualification=s.text),9,9),
        source_tests=COUNTS,installed_tests=COUNTS,protocol_tests=COUNTS,core_tests=COUNTS,
        fixture_sha256=s.hex256,external_comparison_sha256=s.hex256,
        dependency_closure_sha256=s.hex256,negative_control_sha256=s.hex256,
        negative_matrix=s.obj(**{n:s.literal('PASS') for n in ('N06','N17','N28','N30','N31','N33','N36','N37')}))


def measurement_row(value,path,integers):
    index=OPERATIONS.index(value['operation'])
    s.obj(operation=s.literal(OPERATIONS[index]),arguments=_ARGS[index],input_sha256=s.hex256,
        **{key:s.integer for key in SIZES},outcome=s.enum('COMPLETE','NUMERICAL_DOMAIN_FAILURE'),artifact_sha256=s.hex256)(value,path,integers)


class MeasurementTable(Document):
    schema=s.obj(schema=s.literal('H6B_MEASUREMENT_1'),qualification=s.literal('TEST_ONLY_MEASUREMENT_ENVELOPE_NOT_REAL_ADMISSION'),
        wheel_sha256=s.hex256,rows=s.seq(measurement_row,72,72),maxima=s.obj(**{key:s.integer for key in SIZES}),environment=runtime_schema,
        memory_definition=s.literal('SUM_LAUNCHER_AND_WORKER_PEAK_RESIDENT_PLUS_PEAK_PRIVATE_COMMIT'),negative_tests=s.text)
    @classmethod
    def validate(cls,value):
        assert value['maxima']=={key:max(r[key] for r in value['rows']) for key in SIZES}
        runs=value['rows'][:54]
        assert all(r['operation']==OPERATIONS[1] and r['outcome']=='COMPLETE' for r in runs)
        assert {tuple(r['arguments'][k] for k in ('updates','k_profile','readout')) for r in runs}=={
            (n,k,r) for n in (0,1,2,64,256,1024) for k in ('HISTORICAL_THETA_SCALED','HISTORICAL_THETA_SOFT','HISTORICAL_SIMPLE')
            for r in ('NONE','HISTORICAL_STAGED_Z_K','HISTORICAL_COGNITIVE_EMA_Z_H')}


class MeasurementManifest(Document):
    digest_type=ManifestDigest
    schema=s.obj(schema=s.literal('H6B_MEASURED_BUILD_1'),build=s.digest(ProviderBuildDigest),
        table=embedded(MeasurementTable),failure_tests_sha256=s.hex256,failure_observations_sha256=s.hex256,
        policy_selection=s.seq(s.obj(field=s.text,observed=s.integer,limit=s.positive,margin=s.text,reason=s.text),8,8))
