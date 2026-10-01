"""Fixed TEST_ONLY golden bytes and mutually closed protocol families."""
import hashlib
import json
from pathlib import Path
import pytest
from trioctagon_historical_protocol import digests as d
from trioctagon_historical_protocol.codec import canonical_bytes,decode,ParseLimits
from trioctagon_historical_protocol.requests import Request
from trioctagon_historical_protocol.records import DerivedRecord,AttemptReceipt
from trioctagon_historical_protocol.catalogue import Catalogue
from trioctagon_historical_protocol.errors import ProtocolError
from trioctagon_analysis.requests import Request as CoreRequest
from trioctagon_analysis.records import DerivedAnalysisRecord as CoreRecord,AttemptReceipt as CoreReceipt
from trioctagon_analysis.catalogue import Catalogue as CoreCatalogue
from trioctagon_analysis.errors import ProtocolError as CoreError
from trioctagon_analysis.digests import CONTENT_TYPES as CORE_SCOPES
import support as t

HERE=Path(__file__).parent/'fixtures'
GOLDEN=json.loads((HERE/'TEST_ONLY_golden_vectors.json').read_bytes())
LIMITS=ParseLimits(2000000,64)


def test_historical_fixed_golden_vectors_all_fourteen_scopes():
    assert 'TEST' in GOLDEN['provenance'] or 'Synthetic' in GOLDEN['provenance']
    for row in GOLDEN['codec']:
        paths=[tuple(p) for p in row['integer_paths']]
        raw=bytes.fromhex(row['canonical_hex'])
        assert canonical_bytes(row['value'],integer_paths=paths)==raw
        assert decode(raw,LIMITS,integer_paths=paths)==row['value']
        assert not raw.endswith(b'\n')
    kinds={kind.scope:kind for kind in d.CONTENT_TYPES}
    assert set(kinds)=={row['scope'] for row in GOLDEN['digests']} and len(kinds)==14
    for row in GOLDEN['digests']:
        kind=kinds[row['scope']];raw=bytes.fromhex(row['canonical_hex'])
        assert d.preimage(kind,raw).hex()==row['preimage_hex']
        assert d.content_digest(kind,raw).sha256==row['sha256']
        assert hashlib.sha256(bytes.fromhex(row['preimage_hex'])).hexdigest()==row['sha256']
    assert not CORE_SCOPES.intersection(d.CONTENT_TYPES)


@pytest.mark.parametrize('row',GOLDEN['artifacts'],ids=[r['file'] for r in GOLDEN['artifacts']])
def test_fixed_artifact_bytes(row):
    raw=(HERE/row['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==row['sha256']
    owners=dict(Request=Request,DerivedRecord=DerivedRecord,AttemptReceipt=AttemptReceipt,
        CORE_request=CoreRequest,CORE_result=CoreRecord,CORE_receipt=CoreReceipt,CORE_catalogue=CoreCatalogue)
    value=owners[row['owner']].from_bytes(raw,LIMITS)
    assert value.to_bytes()==raw
    if 'semantic' in row:assert value.identity.to_dict()==row['semantic']
    assert not raw.endswith(b'\n')


@pytest.mark.parametrize('historical,core,fixture',[ (Request,CoreRequest,'request'),(DerivedRecord,CoreRecord,'result'),
    (AttemptReceipt,CoreReceipt,'receipt'),(Catalogue,CoreCatalogue,'catalogue')])
def test_N01_N03_N18_N20_cross_family_rejection(historical,core,fixture):
    value=json.loads((HERE/f'TEST_ONLY_core_{fixture}.json').read_bytes())
    with pytest.raises(ProtocolError):historical(value)
    own={'request':lambda:t.request().to_dict(),'result':t.record,'receipt':t.receipt,'catalogue':lambda:t.context()[0].to_dict()}[fixture]()
    with pytest.raises(CoreError):core(own)
    swapped=dict(value)
    swapped['family']=own['family']
    with pytest.raises(ProtocolError):historical(swapped)
    swapped=dict(own);swapped['family']=value['family']
    with pytest.raises(CoreError):core(swapped)


def test_N01_N20_core_profile_and_local_check_substitution_fail():
    value=json.loads((HERE/'TEST_ONLY_core_result.json').read_bytes())
    value['profile']='HISTORICAL'
    with pytest.raises(CoreError):CoreRecord(value)
    value=json.loads((HERE/'TEST_ONLY_core_result.json').read_bytes())
    for check in value['producer']['checks'].values():check['state']='LOCAL_CHECK_PASSED'
    with pytest.raises(CoreError):CoreRecord(value)


def test_N35_hash_graph_is_acyclic_and_semantic_projection_is_closed():
    # Edges mean "depends on". Source bytes and opaque future manifests are leaves.
    graph={'authority':{'source'},'constants':{'source','basis'},'basis':set(),'build':{'source','manifest','conformance'},
        'policy':{'manifest'},'descriptor':set(),'catalogue':{'authority','constants','descriptor','policy','build'},
        'request':{'catalogue','descriptor','authority','constants','policy','build'},
        'payload':{'authority','constants','build'},'observation':{'build'},
        'evidence':{'request','payload','build','observation','catalogue','authority'},
        'semantic':{'request','catalogue','descriptor','authority','constants','policy','build','payload'},
        'artifact':{'semantic','evidence','request','payload'},'source':set(),'manifest':set(),'conformance':set()}
    def visit(key,stack):
        assert key not in stack
        for child in graph[key]:visit(child,stack|{key})
    for key in graph:visit(key,set())
    from trioctagon_historical_protocol.records import semantic_projection
    value=t.record();projection=semantic_projection(value)
    assert set(projection)=={'family','schema','protocol','profile','contract','implementation_policy','issuance_class',
        'request_digest','catalogue_digest','descriptor_digest','authority_digest','constants_digest','resource_policy_digest',
        'provider_build_digest','provider_binding','comparison_evidence','payload_digest','qualifications','assurance'}
    assert 'semantic_result_digest' not in projection and 'metadata' not in projection
    for name in ('attempt_id','metadata','completion','evidence_digest'):
        assert name not in projection
