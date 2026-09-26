"""K2b historical witnesses; CSVs are not equation proofs."""
import csv
from dataclasses import asdict
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import sys
import unittest

import mpmath as mp
import numpy as np
import sympy as sp

from kernel_physics import api
from kernel_physics.tests.parity_oracles import transverse_axis_oracle as oracle
from kernel_physics.tests.parity_oracles import paper_e_oracle as accounting


ROOT = Path(__file__).resolve().parents[2]
GOLDEN = ROOT/'kernel_physics/tests/fixtures/golden_388/TRAJECTORIES.csv'
AXIS = ROOT/'papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION.csv'
P5_HASH = 'eeed672b1cb20321dfc85a2f4753c93d4fe1b9345a5cede4f5e12532537a4a38'
P6_HASH = 'fb2b2a71fd99c536dc7e490c6a2e201b2a0b22ee533820870dff5ee516c468dc'
HEADER = ('phase_strength variant row q t theta initialization z I harmonic_amplitude ema_memory gate_assignment map_lambda map_delta0 '
          'M_x M_y M_z C_x C_y C_z T_x T_y T_z display_M_x display_M_y display_M_z '
          'Omega0_real Omega0_imag Omega1_real Omega1_imag Omega2_real Omega2_imag '
          'norm_residual q_residual macro_relation_residual q_macro q_total d_TM d_CM d_TC '
          'macro_resolved chiral_resolved total_resolved TM_resolved CM_resolved TC_resolved '
          'threshold gram_residual slack_residual polynomial_residual_allowance').split()
CLASSIFICATION = {
    'RUN_KEY': 'phase_strength variant row'.split(),
    'KERNEL_STATE': 'Omega0_real Omega0_imag Omega1_real Omega1_imag Omega2_real Omega2_imag'.split(),
    'OBSERVER_STATE': 'q t theta ema_memory initialization'.split(),
    'OBSERVER_RESULT': 'z M_x M_y M_z C_x C_y C_z T_x T_y T_z'.split(),
    'RAW_READOUT': ['I'],
    'DIAGNOSTIC': ('norm_residual q_residual macro_relation_residual q_macro q_total d_TM d_CM d_TC '
                   'macro_resolved chiral_resolved total_resolved TM_resolved CM_resolved TC_resolved gram_residual slack_residual').split(),
    'HISTORICAL_CONVENTION': ['threshold','polynomial_residual_allowance'],
    'EXCLUDED_RESEARCH': 'display_M_x display_M_y display_M_z map_lambda map_delta0 gate_assignment harmonic_amplitude'.split(),
}
FLAGS = 'macro_resolved chiral_resolved total_resolved TM_resolved CM_resolved TC_resolved'.split()
RESIDUALS = 'norm_residual q_residual macro_relation_residual q_macro q_total gram_residual slack_residual'.split()
EXCLUDED = set(CLASSIFICATION['HISTORICAL_CONVENTION']+CLASSIFICATION['EXCLUDED_RESEARCH'])
RECORDED_ENVIRONMENT = {
    'python': '3.12.14 (main, Aug 25 2026, 14:01:42) [MSC v.1944 64 bit (AMD64)]',
    'platform': 'Windows-11-10.0.26200-SP0', 'numpy':'2.3.5','sympy':'1.14.0','mpmath':'1.3.0',
}
CURRENT_ENVIRONMENT = dict(python=sys.version,platform=platform.platform(),numpy=np.__version__,sympy=sp.__version__,mpmath=mp.__version__)
MODE = 'RECORDED_ENVIRONMENT' if CURRENT_ENVIRONMENT == RECORDED_ENVIRONMENT else 'CROSS_ENVIRONMENT'
EVIDENCE = {'mode':MODE,'environment':CURRENT_ENVIRONMENT,'checks':{},'worst':{},'max_absolute':{},'falsifiers':{}}


def count(kind):
    EVIDENCE['checks'][kind] = EVIDENCE['checks'].get(kind,0)+1


def fixture(path,digest,size,row_count,header=None):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest or len(raw) != size:
        raise AssertionError('K2B_STATUS=HOLD: fixture hash/byte identity '+str(path))
    reader = csv.DictReader(io.StringIO(raw.decode('utf-8'),newline=''))
    rows = list(reader)
    if len(rows) != row_count or any(None in row for row in rows):
        raise AssertionError('K2B_STATUS=HOLD: fixture row/schema identity '+str(path))
    if header is not None and reader.fieldnames != header:
        raise AssertionError('K2B_STATUS=HOLD: golden header differs')
    return rows


def golden_rows():
    rows = fixture(GOLDEN,P5_HASH,282427,388,HEADER)
    keys = [(float(r['phase_strength']),r['variant'],int(r['row'])) for r in rows]
    expected = [(phase,variant,n) for phase in (0.,.001) for n in range(97) for variant in ('staged','ema')]
    if keys != expected:
        raise AssertionError('K2B_STATUS=HOLD: golden grouping/order differs')
    return rows


def omega(row):
    return tuple(complex(float(row[f'Omega{j}_real']),float(row[f'Omega{j}_imag'])) for j in range(3))


def decode(value):
    """Read only the public JSON number codec, without private kernel helpers."""
    if isinstance(value,list):
        return [decode(v) for v in value]
    if isinstance(value,dict):
        if set(value)=={'f64'}:
            return float.fromhex(value['f64'])
        if set(value)=={'re','im'}:
            return complex(decode(value['re']),decode(value['im']))
        return {k:decode(v) for k,v in value.items()}
    return value


def provenance():
    return api.Provenance(kind='user_supplied',source_id='K2b historical replay',source_revision=None,
                          locator='GOLDEN_388_RECEIPT.md',literal_values={},notes='Historical witness; no equation-oracle claim.')


def parameters(phase):
    return api.Parameters(eps=.05,g=.2,phase_strength=phase,k=(1.,1.,1.))


def requests():
    return (api.historical_observer('paper_e_staged_v1'),api.historical_observer('paper_e_ema_v1'))


def run_samples(phase):
    record = api.run(api.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0),parameters(phase),
                     topology='triad',updates=96,parameter_provenance=provenance(),initialization_provenance=provenance(),
                     observers=requests(),readouts=('z_chiral',),
                     diagnostics=('chiral_area_accounting','readout_accounting','historical_alignment'))
    return decode(json.loads(record.to_json()))['samples']


def flatten(sample,variant):
    # Public preset observer IDs are retained as returned by the preset API.
    oid = next(o.observer_id for o in requests() if o.variant == variant)
    state = sample['observer_states'][oid]
    result = sample['observer_results'][oid]
    area = sample['diagnostics']['chiral_area_accounting']
    acc = sample['diagnostics']['readout_accounting'][oid]
    align = sample['diagnostics']['historical_alignment'][oid]
    q = int(state['q'])
    row = dict(row=int(sample['update_index']),q=q,t=state['t'],theta=2*math.pi*((q%12)/12),
               initialization=result['initialization'],z=result['z'],I=area['intensity'],
               ema_memory=state['m'] if variant=='ema' else '')
    for j,v in enumerate(sample['omega']):
        row[f'Omega{j}_real'],row[f'Omega{j}_imag'] = v.real,v.imag
    for prefix,name in (('M','Z_macro'),('C','Z_chiral'),('T','Z_total')):
        row.update({prefix+'_'+axis:v for axis,v in zip('xyz',result[name])})
    row.update({name:acc[name] for name in RESIDUALS if name in acc})
    row.update({name:area[name] for name in ('gram_residual','slack_residual')})
    row.update({name:align[name] for name in ['d_TM','d_CM','d_TC']+FLAGS})
    return row


class WitnessCase(unittest.TestCase):
    @mp.workdps(80)
    def bounded(self,gate,quantity,actual,expected,bound,scale=None,kind='HISTORICAL_FIXTURE_TOLERANCE'):
        def number(v):
            if isinstance(v,(mp.mpf,mp.mpc)):
                return v
            z=complex(v)
            return mp.mpc(mp.mpf(z.real),mp.mpf(z.imag))
        bound=mp.mpf(bound)
        error=abs(number(actual)-number(expected))
        fraction=error/bound if bound else (mp.mpf(0) if error==0 else mp.inf)
        evidence=dict(quantity=quantity,actual=str(actual),reference=mp.nstr(number(expected),35),
                      absolute_error=mp.nstr(error,35),allowed_bound=mp.nstr(bound,35),
                      scale=None if scale is None else mp.nstr(scale,35),fraction=mp.nstr(fraction,35),kind=kind)
        self.assertLessEqual(error,bound,'K2B_STATUS=HOLD: '+json.dumps(evidence))
        count(kind)
        if gate not in EVIDENCE['worst'] or fraction>mp.mpf(EVIDENCE['worst'][gate]['fraction']):
            EVIDENCE['worst'][gate]=evidence
        if gate not in EVIDENCE['max_absolute'] or error>mp.mpf(EVIDENCE['max_absolute'][gate]['absolute_error']):
            EVIDENCE['max_absolute'][gate]=evidence

    def exact(self,label,actual,expected):
        self.assertEqual(actual,expected,label)
        count('EXACT_DISCRETE')

    def symbolic(self,label,actual,expected):
        self.assertTrue(all(sp.simplify(x-y)==0 for x,y in zip(sp.Matrix(actual),sp.Matrix(expected),strict=True)),label)
        count('EXACT_SYMBOLIC')


class P5Tests(WitnessCase):
    """P5 IS A HISTORICAL REGRESSION / SCHEDULE WITNESS.
    PASS SUPPORTS: preserved samples, row-zero/clock/EMA ordering, stored
    relationships and independent chirality from saved Omega.
    PASS DOES NOT SUPPORT: Paper A/E equations (P1/P9), physical interpretation,
    spatial registration, gate assignment or display mappings.
    """

    def test_00_integrity_classification_and_protocol(self):
        rows=golden_rows()
        classified=[c for values in CLASSIFICATION.values() for c in values]
        self.exact('each of 50 columns exactly once',sorted(classified),sorted(HEADER))
        self.exact('no duplicate classification',len(set(classified)),50)
        for phase in (0.,.001):
            for variant in ('staged','ema'):
                selected=[r for r in rows if float(r['phase_strength'])==phase and r['variant']==variant]
                self.exact('row count',len(selected),97)
                self.exact('row zero state',omega(selected[0]),(.2+.3j,-.4+.1j,.1-.2j))
                self.exact('row zero clock',(selected[0]['q'],selected[0]['t']),('0','0.0'))
                self.exact('row zero no innovation',selected[0]['ema_memory'],'0.0' if variant=='ema' else '')
                self.assertTrue(all(r['initialization']=='recomputed' for r in selected))

    @mp.workdps(80)
    def test_10_runner_historical_regression(self):
        saved=golden_rows()
        ordinary=(CLASSIFICATION['KERNEL_STATE']+['t','theta','z','I','M_x','M_y','M_z','T_x','T_y','T_z','d_TM','d_CM','d_TC'])
        # Freeze bounds from fixture values before any Runner discrepancy.
        bounds={(i,col):mp.mpf('1e-12')*(1+abs(mp.mpf(float(row[col]))))
                for i,row in enumerate(saved) for col in ordinary+(['ema_memory'] if row['variant']=='ema' else [])}
        samples={phase:run_samples(phase) for phase in (0.,.001)}
        for i,row in enumerate(saved):
            phase,n,variant=float(row['phase_strength']),int(row['row']),row['variant']
            sample=samples[phase][n]
            actual=flatten(sample,variant)
            label=f'lambda={phase} {variant} row={n}'
            self.exact(label+' update',actual['row'],n)
            self.exact(label+' q',actual['q'],int(row['q']))
            self.exact(label+' initialization',actual['initialization'],row['initialization'])
            for flag in FLAGS:
                self.exact(label+' '+flag,actual[flag],row[flag]=='True')
            for col in ordinary+(['ema_memory'] if variant=='ema' else []):
                reference=float(row[col])
                if MODE=='RECORDED_ENVIRONMENT':
                    self.exact(label+' '+col,float(actual[col]).hex(),reference.hex())
                else:
                    self.bounded('P5_ordinary',label+' '+col,actual[col],reference,bounds[i,col])
            self.exact(label+' raw C equals observer C',tuple(sample['raw_readouts']['z_chiral']),tuple(actual['C_'+axis] for axis in 'xyz'))

    @mp.workdps(80)
    def test_20_independent_saved_and_replayed_chirality(self):
        saved=golden_rows()
        # All saved references and scales are computed before replay.
        saved_refs=[oracle.cross_reference(omega(row)) for row in saved]
        for i,row in enumerate(saved):
            ref,scale=saved_refs[i]
            for j,axis in enumerate('xyz'):
                self.bounded('P5_saved_C',f'saved row={i} C_{axis}',float(row['C_'+axis]),ref[j],64*mp.mpf(2)**-52*scale[j],scale[j],'HIGH_PRECISION_REFERENCE')
        samples={phase:run_samples(phase) for phase in (0.,.001)}
        for i,row in enumerate(saved):
            sample=samples[float(row['phase_strength'])][int(row['row'])]
            ref,scale=oracle.cross_reference(sample['omega'])
            old,old_scale=saved_refs[i]
            for j,axis in enumerate('xyz'):
                actual=sample['raw_readouts']['z_chiral'][j]
                self.bounded('P5_replayed_C',f'replayed row={i} C_{axis}',actual,ref[j],64*mp.mpf(2)**-52*scale[j],scale[j],'HIGH_PRECISION_REFERENCE')
                trajectory_term=abs(ref[j]-old[j])
                bound=64*mp.mpf(2)**-52*scale[j]+trajectory_term
                self.bounded('P5_cross_trajectory_C',f'cross trajectory row={i} C_{axis}',actual,float(row['C_'+axis]),bound,scale[j],'BINARY64_TERM_SCALE')
                if MODE=='RECORDED_ENVIRONMENT':
                    self.exact('recorded C bits',actual.hex(),float(row['C_'+axis]).hex())

    def test_30_runner_direct_control_all_rows(self):
        golden_rows()
        for phase in (0.,.001):
            samples=run_samples(phase)
            state=api.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0)
            clock=api.Clock(q=0,N=12,t=0.,q_step=1)
            memory=api.EMAState(m=0.)
            for n,sample in enumerate(samples):
                if n:
                    state=api.step(state,parameters(phase),topology='triad')
                    clock=api.advance_clock(clock,.1)
                    memory=api.advance_ema(state.omega,memory)
                self.exact(f'control state bytes {phase,n}',np.array(sample['omega'],dtype=np.complex128).tobytes(),np.array(state.omega,dtype=np.complex128).tobytes())
                for request in requests():
                    variant=request.variant
                    out=(api.observe_staged(state.omega,clock,request.config) if variant=='staged' else api.observe_ema(state.omega,clock,request.config,memory))
                    observed=sample['observer_results'][request.observer_id]
                    self.exact(f'control scalar bits {phase,n,variant}',observed['z'].hex(),out.z.hex())
                    for field in ('Z_macro','Z_chiral','Z_total'):
                        self.exact(f'control {field} bits {phase,n,variant}',np.array(observed[field]).tobytes(),getattr(out,field).tobytes())
                    snapshot=sample['observer_states'][request.observer_id]
                    self.exact('control clock',(int(snapshot['q']),snapshot['t'].hex()),(clock.q,clock.t.hex()))
                    self.exact('observer update count',int(snapshot['observer_update_count']),n)
                    if variant=='ema':
                        self.exact('control memory bits',snapshot['m'].hex(),memory.m.hex())
                    acc=asdict(api.readout_accounting(out,alpha=request.config.alpha,beta=request.config.beta))
                    align=asdict(api.historical_alignment(out.Z_macro,out.Z_chiral,out.Z_total))
                    for group,control in (('readout_accounting',acc),('historical_alignment',align)):
                        stored=sample['diagnostics'][group][request.observer_id]
                        for key,value in control.items():
                            if isinstance(value,(float,np.floating)):
                                self.exact('control diagnostic bits '+key,float(stored[key]).hex(),float(value).hex())
                            elif isinstance(value,np.ndarray):
                                self.exact('control diagnostic array bits '+key,np.array(stored[key]).tobytes(),value.tobytes())
                            else:
                                self.exact('control diagnostic value '+key,stored[key],value)
                area=asdict(api.chiral_area_accounting(state.omega))
                for key,value in area.items():
                    actual=sample['diagnostics']['chiral_area_accounting'][key]
                    self.exact('control area bits '+key,np.asarray(actual).tobytes(),np.asarray(value).tobytes())

    @mp.workdps(80)
    def test_40_accounting_uses_defining_terms_not_historical_allowance(self):
        saved=golden_rows()
        samples={phase:run_samples(phase) for phase in (0.,.001)}
        for i,row in enumerate(saved):
            replay=flatten(samples[float(row['phase_strength'])][int(row['row'])],row['variant'])
            for label,record in (('saved',row),('replayed',replay)):
                M,C,T=([float(record[p+'_'+axis]) for axis in 'xyz'] for p in 'MCT')
                terms=accounting.readout_terms(M,C,T,float(record['z']),1.,.5)
                terms.update(accounting.gram_terms(omega(record)))
                for field in RESIDUALS:
                    expected,scale=terms[field]
                    expected,scale=accounting.number(expected),accounting.number(scale)
                    self.bounded('P5_accounting',f'{label} row={i} {field}',float(record[field]),expected,256*mp.mpf(2)**-52*scale,scale,'BINARY64_TERM_SCALE')
                    if MODE=='RECORDED_ENVIRONMENT' and label=='replayed':
                        self.exact('recorded diagnostic bits '+field,float(record[field]).hex(),float(row[field]).hex())


class P6Tests(WitnessCase):
    """PASS SUPPORTS: the two accepted special invariant subspaces over eight
    updates, their oriented chirality, exact one-step formulas and separation.
    PASS DOES NOT SUPPORT: a universal axis, attractor, physical selector,
    generic seed behavior, or a theorem inferred from floating zeros.
    """

    def test_00_fixture_identity_and_grouping(self):
        rows=fixture(AXIS,P6_HASH,10345,18)
        self.exact('P6 rows and ordering',[(r['seed'],int(r['row'])) for r in rows],[(s,n) for s in ('A','B') for n in range(9)])
        self.exact('P6 columns',len(rows[0]),32)
        self.assertTrue(all(r['direction_valid']=='True' and r['invalid_reason']=='' for r in rows))

    def test_10_exact_invariant_subspaces_and_one_step(self):
        x,y,z,b,c,d,f,eps,g=sp.symbols('x y z b c d f eps g',real=True)
        A=sp.Matrix([x+sp.I*y,x-sp.I*y,z])
        B=sp.Matrix([b+sp.I*c,b+sp.I*c,d+sp.I*f])
        FA=oracle.equal_k_polynomial(A,eps,g)
        FB=oracle.equal_k_polynomial(B,eps,g)
        self.symbolic('A conjugate-swap invariant',[FA[0]-sp.conjugate(FA[1]),sp.im(FA[2])],[0,0])
        self.symbolic('B equal-channel invariant',[FB[0]-FB[1]],[0])
        CA=y*sp.Matrix([z,z,-2*x])
        CB=(b*f-d*c)*sp.Matrix([1,-1,0])
        self.symbolic('Paper F (26)',oracle.symbolic_cross(A),CA)
        self.symbolic('Paper F (27)',oracle.symbolic_cross(B),CB)
        self.symbolic('exact orthogonality for all subspace amplitudes',[CA.dot(CB)],[0])
        h=sp.Symbol('h',positive=True)
        u=sp.Matrix([1,-1,0])/sp.sqrt(2)
        v=sp.Matrix([1,1,-2])/sp.sqrt(6)
        one=sp.ones(3,1)
        self.symbolic('basis transverse/orthonormal',[sum(u),sum(v),u.dot(v),u.dot(u),v.dot(v)],[0,0,0,1,1])
        expected_state,expected_C=oracle.a_one_step(h)
        self.symbolic('A one-step exact state',oracle.equal_k_polynomial(one+sp.I*h*u,sp.Rational(1,20),sp.Rational(1,5)),expected_state)
        self.symbolic('A one-step exact C',oracle.symbolic_cross(expected_state),expected_C)
        direction=sp.Matrix([1,1,-2+h*h/20])
        initial=sp.Matrix([1,1,-2])
        cross=direction.cross(initial)
        tangent=sp.sqrt(cross.dot(cross))/direction.dot(initial)
        formula=sp.sqrt(2)*h*h/(20*(6-h*h/10))
        self.symbolic('exact A acute angle tangent on 0<h<4',[tangent],[formula])
        self.symbolic('A signed elevation has positive numerator',[sum(direction)],[h*h/20])
        B1=oracle.equal_k_polynomial(one+sp.I*h*v,sp.Rational(1,20),sp.Rational(1,5))
        Bc=oracle.symbolic_cross(B1)
        self.symbolic('B one-step exact fixed line',[Bc[0]+Bc[1],Bc[2]],[0,0])

    @mp.workdps(80)
    def test_20_eight_updates_symmetry_angles_and_signed_zero(self):
        rows=fixture(AXIS,P6_HASH,10345,18)
        seeds={'A':np.ones(3,dtype=complex)+1j*.001*np.array([1.,-1.,0.])/math.sqrt(2),
               'B':np.ones(3,dtype=complex)+1j*.001*np.array([1.,1.,-2.])/math.sqrt(6)}
        # Freeze the state/C fixture bounds and exact one-step reference first.
        state_bounds={(r['seed'],int(r['row']),j):mp.mpf('1e-13')+mp.mpf('1e-12')*abs(mp.mpc(omega(r)[j])) for r in rows for j in range(3)}
        chiral_bounds={(r['seed'],int(r['row']),j):mp.mpf('1e-13')+mp.mpf('1e-12')*abs(mp.mpf(float(r['C_'+a]))) for r in rows for j,a in enumerate('xyz')}
        angle_reference=oracle.a_one_step_angle(mp.mpf(1)/1000)
        reference_state,reference_c=oracle.a_one_step(sp.Rational(1,1000))
        runtime={}
        for label,seed in seeds.items():
            state=api.State(omega=tuple(seed),update_index=0)
            history=[]
            for n in range(9):
                if n:
                    state=api.step(state,parameters(0),topology='triad')
                C=api.z_chiral(state.omega)
                history.append((state.omega,C))
            runtime[label]=history
        initial={name:oracle.cross_reference(seed)[0] for name,seed in seeds.items()}
        for row in rows:
            label,n=row['seed'],int(row['row'])
            w,C=runtime[label][n]
            reference=omega(row)
            for j,axis in enumerate('xyz'):
                self.bounded('P6_state',f'{label} row={n} Omega{j}',w[j],reference[j],state_bounds[label,n,j])
                self.bounded('P6_C',f'{label} row={n} C_{axis}',C[j],float(row['C_'+axis]),chiral_bounds[label,n,j])
            if label=='A':
                self.exact(f'A Cx=Cy row={n}',float(C[0]).hex(),float(C[1]).hex())
                self.exact(f'A conjugate-swap row={n}',w[0],w[1].conjugate())
                self.exact(f'A real third channel row={n}',w[2].imag,0.)
            else:
                self.exact(f'B Cx=-Cy row={n}',float(C[0]).hex(),float(-C[1]).hex())
                self.exact(f'B Cz positive zero row={n}',float(C[2]).hex(),'0x0.0p+0')
                self.exact(f'B equal first channels row={n}',w[0],w[1])
            _,term_scales=oracle.cross_reference(w)
            norm=mp.sqrt(sum(mp.mpf(float(v))**2 for v in C))
            saved_norm=mp.mpf(float(row['C_norm']))
            self.bounded('P6_C',f'{label} row={n} C_norm',norm,saved_norm,mp.mpf('1e-13')+mp.mpf('1e-12')*abs(saved_norm))
            # Preserved AX validity convention uses 32*2^-53, separately from
            # K0's u=2^-52: it is a direction diagnostic, not recurrence law.
            proxy=32*mp.mpf(2)**-53*mp.sqrt(sum(s*s for s in term_scales))
            valid=norm>0 and norm>1000*proxy
            self.exact(f'P6 nonzero direction validity {label,n}',bool(valid),row['direction_valid']=='True')
            self.assertTrue(valid)
            for j,axis in enumerate('xyz'):
                unit=mp.mpf(float(C[j]))/norm
                saved_unit=mp.mpf(float(row['unit_C_'+axis]))
                self.bounded('P6_unit_C',f'{label} row={n} unit_C_{axis}',unit,saved_unit,mp.mpf('1e-13')+mp.mpf('1e-12')*abs(saved_unit))
            plane=sum(mp.mpf(float(v)) for v in C)/(mp.sqrt(3)*norm)
            saved_plane=mp.mpf(float(row['normalized_plane_residual']))
            self.bounded('P6_plane',f'{label} row={n} signed plane residual',plane,saved_plane,mp.mpf('1e-13')+mp.mpf('1e-12')*abs(saved_plane))
            own=oracle.projective_angle(C,initial[label])
            other=oracle.projective_angle(C,initial['B' if label=='A' else 'A'])
            elevation=oracle.signed_elevation(C)
            for field,value in (('projective_angle_own_initial_rad',own),('projective_angle_other_initial_rad',other),('angle_to_plane_rad',abs(elevation))):
                self.bounded('P6_angles',f'{label} row={n} {field}',value,float(row[field]),mp.mpf('1e-12'))
            mutual=oracle.projective_angle(runtime['A'][n][1],runtime['B'][n][1])
            self.bounded('P6_orthogonality',f'row={n} mutual angle',mutual,mp.pi/2,mp.mpf('1e-12'))
            self.bounded('P6_angles',f'{label} row={n} saved mutual angle',mutual,float(row['mutual_projective_angle_rad']),mp.mpf('1e-12'))
            if label=='B':
                self.exact('B zero projective drift',own,mp.mpf(0))
            if label=='A' and n==1:
                self.bounded('P6_one_step_angle','A signed elevation row=1',elevation,angle_reference,mp.mpf('1e-12'))
                self.bounded('P6_one_step_angle','A projective own-axis row=1',own,angle_reference,mp.mpf('1e-12'))
                for j in range(3):
                    exact_state=accounting.number(reference_state[j])
                    exact_c=accounting.number(reference_c[j])
                    self.bounded('P6_one_step','A exact state '+str(j),w[j],exact_state,mp.mpf('1e-13')+mp.mpf('1e-12')*abs(exact_state))
                    self.bounded('P6_one_step','A exact C '+str(j),C[j],exact_c,mp.mpf('1e-13')+mp.mpf('1e-12')*abs(exact_c))
        # Deliberately signed input zeros; no invented direction at zero and no
        # extra trajectory. Compensated equal-product subtraction returns +0.
        signed=np.array([complex(1.,-0.),complex(1.,0.),complex(1.,-0.)])
        before=signed.tobytes()
        self.exact('signed-zero cross convention',tuple(float(v).hex() for v in api.z_chiral(signed)),('0x0.0p+0',)*3)
        self.exact('signed-zero input preserved',signed.tobytes(),before)
        with self.assertRaises(ValueError):
            oracle.projective_angle((0,0,0),(1,0,0))
        EVIDENCE['falsifiers'].update(A_equal_Cx_Cy='PASS',B_opposite_Cx_Cy='PASS',B_Cz_positive_zero='PASS',signed_zero_no_direction='PASS',universal_axis_counterexample='PASS')
