"""TEST_ONLY protocol adapters. Synthetic requests confer no real local admission."""
import json
from pathlib import Path
import pytest
from trioctagon_historical_protocol.requests import Request,request_digest
from trioctagon_historical_protocol.definitions import OPERATIONS,resolved_constants,numerical_policy
from trioctagon_historical_protocol.payloads import Payload
from trioctagon_historical_kernel import provider,ema_z

HERE=Path(__file__).parent/'fixtures'


def request(index=0,*,updates=2,readout='NONE',profile='HISTORICAL_THETA_SCALED',omega=None):
    value=json.loads((HERE/f'TEST_ONLY_h6a_request_{index}.json').read_bytes())
    body=value['body'];args=body['arguments']
    if index<2:args['k_profile']=profile
    if index==1:args.update(updates=updates,readout=readout)
    if omega is not None:body['input']['omega']=omega
    body['resolved_constants']=resolved_constants(OPERATIONS[index],args)
    body['numerical_policy']=numerical_policy(OPERATIONS[index],args)
    value['request_digest']=request_digest(value).to_dict()
    return Request(value)


@pytest.mark.parametrize('index',range(5))
def test_all_five_adapters_bind_exact_H6A(index):
    q=request(index);result=provider._evaluate(q)
    assert Payload(result.to_dict()).to_bytes()==result.to_bytes()
    result.validate_request(q)


@pytest.mark.parametrize('n',[0,1,2])
@pytest.mark.parametrize('readout',['NONE','HISTORICAL_STAGED_Z_K','HISTORICAL_COGNITIVE_EMA_Z_H'])
def test_run_provider_constructor_and_terminal(n,readout):
    p=provider._evaluate(request(1,updates=n,readout=readout)).to_dict()
    assert len(p['rows'])==n and p['terminal']['update_index']==n


def test_N28_provider_hidden_EMA_advance_is_forbidden(monkeypatch):
    def forbidden(*args,**kwargs):raise AssertionError('pure provider invoked cubic or advancement')
    monkeypatch.setattr(ema_z,'advance_ema',forbidden)
    monkeypatch.setattr(ema_z,'cubic_j',forbidden)
    q=request(3).to_dict();q['body']['arguments']['memory']={'f64':'-0x0.0p+0'}
    q['request_digest']=request_digest(q).to_dict()
    result=provider._evaluate(Request(q)).to_dict()
    assert result['memory_input']==result['memory_output']=={'f64':'-0x0.0p+0'}
    assert result['memory_update_count']==0


def test_adapter_public_entry_requires_local_admission():
    with pytest.raises(TypeError):provider.evaluate(request(),None)


def test_complete_scientific_failure_never_returns_short_history():
    from trioctagon_historical_kernel import history,numerics
    def stop(completed):
        if completed==1:raise numerics.NumericalFailure('TEST_ONLY failure after first update')
    with pytest.raises(numerics.NumericalFailure):provider._evaluate(request(1,updates=2),_control=stop)
