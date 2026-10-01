"""Independent equation/boundary tests and frozen H2 tokens; no current/old imports."""
import json
import math
from pathlib import Path
import struct
import pytest
from trioctagon_historical_kernel import api, constants, clock, chirality, ema_z, history, numerics, phase

FIXTURE = json.loads((Path(__file__).parent/'fixtures/h2_applicable.json').read_bytes())
SEED = api.Triad((.2+.3j, -.4+.1j, .1-.2j))
ZERO = api.Triad((0j,0j,0j))


def triad(tokens):
    return api.Triad(tuple(complex(float.fromhex(re), float.fromhex(im)) for re,im in tokens))


def tokens(omega):
    return [[z.real.hex(),z.imag.hex()] for z in omega.values]


@pytest.mark.parametrize('row',FIXTURE['one'],ids=[r['profile']+'-'+r['vector'] for r in FIXTURE['one']])
def test_frozen_H2_one_step_exact(row):
    actual = tokens(api.step(triad(row['input']),api.KProfile(row['profile'])))
    assert actual == row['expected'] == row['current_expected']


@pytest.mark.parametrize('row',FIXTURE['multi'],ids=[r['profile']+'-'+r['vector'] for r in FIXTURE['multi']])
def test_frozen_H2_multistep_exact_and_readout_domain(row):
    profile=api.KProfile(row['profile'])
    result=api.run(triad(row['input']),profile,64,api.Readout.STAGED)
    memory=api.Memory()
    tol=FIXTURE['multi_tolerance']
    for sample,expected in zip((*result.rows[1:],result.terminal),row['steps']):
        assert sample.update_index==expected['n']
        assert tokens(sample.omega)==expected['expected']==expected['current_expected']
        memory=ema_z.advance_ema(sample.omega,memory)
        h=api.observe_ema(sample.omega,sample.clock,memory)
        k=sample.observation
        values=(k.z,*k.M,*k.C,*k.T,memory.value,h.z)
        for name in ('old_readouts','current_readouts'):
            for actual,raw in zip(values,expected[name]):
                target=float.fromhex(raw)
                assert abs(actual-target)<=tol['atol']+tol['rtol']*abs(target)


def test_H2_selection_does_not_admit_deferred_parameters():
    assert len(FIXTURE['one'])==39 and len(FIXTURE['comparison_only_one'])==52
    assert sum(len(r['steps']) for r in FIXTURE['multi'])==640
    assert sum(r['steps'] for r in FIXTURE['comparison_only_multi'])==640
    for name in ('L01','L01_phase_on','L01_phase_off','no_coupling','signed_finite'):
        with pytest.raises(ValueError):api.KProfile(name)


def test_literal_bits_and_three_profiles():
    assert constants.INNOVATION.hex()=='0x1.47ae147ae147bp-7'
    assert constants.INNOVATION != 1.0-constants.RETENTION
    assert constants.HARMONIC==3 and constants.PHASE_STRENGTH.hex()=='0x1.0624dd2f1a9fcp-10'
    mapping={'historical_default':api.KProfile.SCALED,'theta_soft':api.KProfile.SOFT,'simple':api.KProfile.SIMPLE}
    for name,p in mapping.items():
        assert [v.hex() for v in constants.K[p]]==[x['hex'] for x in FIXTURE['parameters'][name]['k']]


@pytest.mark.parametrize('bad',[[0j]*3,(0j,)*2,(0j,)*4,(True,0j,0j),(complex(math.inf,0),0j,0j)])
def test_raw_triad_is_explicit_finite_and_not_broadcast(bad):
    with pytest.raises((TypeError,ValueError)):api.Triad(bad)


def test_input_signed_zero_is_preserved_and_phase_zero_canonicalized():
    v=api.Triad((complex(-0.,0.),1j,0j))
    assert tokens(v)[0][0]=='-0x0.0p+0'
    result=phase.synchronize(v)
    assert tokens(result)[0]==['0x0.0p+0','0x0.0p+0']
    # Independent scalar witness for old np.angle(-0,+0)=pi, compared only as
    # boundary evidence. No old module is imported and no runtime fallback exists.
    old_angle=math.atan2(v.values[0].imag,v.values[0].real)
    assert old_angle==math.pi
    legacy_increment=constants.PHASE_STRENGTH*(math.sin(3*(old_angle-math.pi/2))+math.sin(3*(0-math.pi/2)))
    canonical_increment=constants.PHASE_STRENGTH*(math.sin(3*(0-math.pi/2))+math.sin(3*(0-math.pi/2)))
    assert legacy_increment != canonical_increment
    assert abs(abs(result.values[1])-1.0)<2e-16


def test_chirality_pair_order_sign_and_quadratic_scale():
    state=api.Triad((1+0j,0+1j,2+3j))
    assert chirality.raw_chirality(state)==(-2.,-3.,1.)
    scaled=api.Triad(tuple(2*z for z in state.values))
    assert chirality.raw_chirality(scaled)==tuple(4*x for x in chirality.raw_chirality(state))


@pytest.mark.parametrize('mode',list(api.Readout))
@pytest.mark.parametrize('n',[0,1,2])
def test_fresh_history_constructor_and_terminal(n,mode):
    result=api.run(SEED,api.KProfile.SCALED,n,mode)
    assert len(result.rows)==n and result.terminal.update_index==n
    first=result.rows[0] if n else result.terminal
    assert first.omega==SEED and first.clock==api.Clock()
    if mode is api.Readout.NONE:
        assert first.observation is None and first.memory is None
    else:
        assert first.observation.z==0 and first.observation.C==(0.,)*3
        assert chirality.raw_chirality(SEED)!=(0.,)*3
        assert api.observe_staged(SEED,api.Clock()).C!=first.observation.C


def test_repeated_dt_wrap_and_lost_increment():
    c=api.Clock()
    for _ in range(20):c=clock.advance(c)
    expected=0.
    for _ in range(20):expected+=.1
    assert c.q==8 and c.t.hex()==expected.hex() and c.t!=20*.1
    with pytest.raises(numerics.NumericalFailure):clock.advance(api.Clock(0,1e16))


def test_pure_EMA_never_calls_cubic_or_advance(monkeypatch):
    def forbidden(*args,**kwargs):raise AssertionError('hidden EMA evaluation')
    monkeypatch.setattr(ema_z,'cubic_j',forbidden)
    monkeypatch.setattr(ema_z,'advance_ema',forbidden)
    memory=api.Memory(-0.0)
    a=api.observe_ema(SEED,api.Clock(3,.5),memory)
    b=api.observe_ema(SEED,api.Clock(3,.5),memory)
    assert a==b and memory.value.hex()=='-0x0.0p+0'


def test_EMA_run_advances_once_from_new_state_before_observation(monkeypatch):
    events=[]
    advance,observe=ema_z.advance_ema,ema_z.observe_ema
    def record_advance(omega,memory):
        events.append(('advance',omega));return advance(omega,memory)
    def record_observe(omega,c,memory):
        events.append(('observe',omega));return observe(omega,c,memory)
    monkeypatch.setattr(ema_z,'advance_ema',record_advance)
    monkeypatch.setattr(ema_z,'observe_ema',record_observe)
    result=api.run(SEED,api.KProfile.SCALED,2,api.Readout.EMA)
    assert [e[0] for e in events]==['advance','observe','advance','observe']
    assert events[0][1]==result.rows[1].omega and events[2][1]==result.terminal.omega
    assert events[0][1]!=SEED


def test_staged_K_differs_from_H_and_damps_only_scalar():
    c=api.Clock(5,.7)
    k=api.observe_staged(SEED,c);h=api.observe_ema(SEED,c,api.Memory())
    assert k.z!=h.z and k.C==h.C
    assert math.isclose(k.z,h.z*math.exp(-.577*.7),rel_tol=2e-15)


def test_response_refusal_is_distinct_from_recurrence_and_chart():
    tiny=api.Triad((complex(1e-200,0),0j,0j))
    assert api.probability_chart(tiny).classification=='NONZERO_INPUT_SQUARED_TO_ZERO'
    api.step(tiny,api.KProfile.SIMPLE)
    with pytest.raises(numerics.NumericalFailure):chirality.raw_chirality(api.Triad((1e-200+0j,1e-200j,0j)))
    with pytest.raises(numerics.NumericalFailure):api.observe_staged(ZERO,api.Clock(0,2000.))
    with pytest.raises(numerics.NumericalFailure):api.step(api.Triad((complex(1e308,0),0j,0j)),api.KProfile.SCALED)


def test_strict_primitives_and_left_associated_cubic():
    assert numerics.multiply(-0.,1e308,'zero').hex()=='0x0.0p+0'
    assert numerics.add((1e16,1.,-1e16),'compensated')==1.
    for value in (float.fromhex('0x0.0000000000001p-1022'),math.inf):
        with pytest.raises(numerics.NumericalFailure):numerics.checked(value,'strict')
    with pytest.raises(numerics.NumericalFailure):numerics.multiply(1e-200,1e-200,'lost product')
    state=api.Triad((1+2j,3+4j,5+6j))
    assert ema_z.cubic_j(state)==76.
    assert numerics.stable_norm(api.Triad((1e300+0j,0j,0j)))==1e300


@pytest.mark.parametrize('values,kind,flag',[
    ((0j,0j,0j),'EXACT_ZERO_INPUT',None),
    ((complex(1e-200,0),0j,0j),'NONZERO_INPUT_SQUARED_TO_ZERO','square_to_zero'),
    ((1+0j,complex(1e-200,0),0j),'NORMALIZED_NONZERO','square_to_zero'),
    ((complex(1e-160,0),0j,0j),'NORMALIZED_NONZERO','subnormal_square'),
    ((complex(1e154,0),complex(1e-160,0),0j),'NORMALIZED_NONZERO','normalized_weight_to_zero'),
    ((1+0j,complex(1e-160,0),0j),'NORMALIZED_NONZERO','subnormal_weight')])
def test_chart_actual_legacy_branches(values,kind,flag):
    result=api.probability_chart(api.Triad(values))
    assert result.classification==kind
    if flag:assert any(getattr(result,flag))
    if kind=='EXACT_ZERO_INPUT':assert result.weights==result.chart==(0.,)*3
    if kind=='NONZERO_INPUT_SQUARED_TO_ZERO':
        assert result.weights==(0.,)*3 # a stable normalization would produce (1,0,0).
        assert result.warnings==('NONZERO_INPUT_ZERO_BRANCH','SQUARE_UNDERFLOW')


def test_chart_is_basis_multiply_not_analytic_cu_and_refuses_overflow():
    chart=api.probability_chart(SEED)
    expected=tuple(sum(constants.BASIS[j][i]*chart.weights[j] for j in range(3)) for i in range(3))
    assert all(abs(x-y)<2e-16 for x,y in zip(chart.chart,expected))
    with pytest.raises(numerics.NumericalFailure):api.probability_chart(api.Triad((complex(1e308,0),0j,0j)))


def test_chart_operation_order_instrumented(monkeypatch):
    import importlib
    module=importlib.import_module('trioctagon_historical_kernel.probability_chart')
    events=[];absolute=module.np.abs;summation=module.np.sum
    def watched_abs(value):
        events.append('abs');return absolute(value)
    def watched_sum(value,*args,**kwargs):
        events.append('sum')
        assert tuple(value)==tuple(absolute(module.np.asarray(SEED.values))**2)
        return summation(value,*args,**kwargs)
    monkeypatch.setattr(module.np,'abs',watched_abs)
    monkeypatch.setattr(module.np,'sum',watched_sum)
    result=api.probability_chart(SEED)
    assert events==['abs','sum']
    # A controlled basis substitution proves the returned chart is actually
    # obtained from the matrix, including cu, rather than an analytic shortcut.
    monkeypatch.setattr(module,'BASIS',((2.,0.,0.),(2.,0.,0.),(2.,0.,0.)))
    changed=api.probability_chart(SEED)
    assert changed.chart[0]>1.9 and changed.chart[1:]==(0.,0.)
    assert changed.chart!=result.chart
