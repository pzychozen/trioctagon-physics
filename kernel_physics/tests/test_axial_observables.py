"""K-G0 frozen scientific witnesses: expectations precede implementation."""
import ast
from contextlib import ExitStack
from dataclasses import fields, is_dataclass, FrozenInstanceError
import hashlib
import inspect
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
from kernel_physics import api as a, dynamics, readouts, z_manifold, _runner

FIXTURES = Path(__file__).parent/'fixtures/axial_v1'
REFERENCE_SHA256 = '4811190a7612444783676629bcff5b929eb3b69d933054e29dd00a40a5f18d34'
F = json.loads((FIXTURES/'reference.json').read_text())
U = 2.0**-53


def inputs(row):
    omega=tuple(complex(*(float.fromhex(v) for v in p)) for p in row['omega_hex'])
    p=row['parameters_hex']
    return a.State(omega=omega,update_index=7), a.Parameters(
        **{k:float.fromhex(p[k]) for k in ('eps','g','phase_strength')},
        k=tuple(float.fromhex(v) for v in p['k']))


class ScientificTests(unittest.TestCase):
    def near(self, actual, expected, factor=512, scale=None):
        if isinstance(expected,(list,tuple)):
            self.assertEqual(len(actual),len(expected))
            for x,y in zip(actual,expected): self.near(x,y,factor,scale)
        else:
            y=float(expected)
            self.assertLessEqual(abs(float(actual)-y),factor*U*(max(1,abs(y)) if scale is None else max(1,scale)))

    def area_near(self,actual,expected,factor=2048):
        for key in ('A','C','W','Gamma'): self.near(getattr(actual,key),expected[key],factor)

    def test_frozen_fixture_identity(self):
        self.assertEqual(hashlib.sha256((FIXTURES/'reference.json').read_bytes()).hexdigest(),REFERENCE_SHA256)
        self.assertEqual(F['generator_sha256'],hashlib.sha256((FIXTURES/'freeze_reference.py').read_bytes()).hexdigest())

    def test_sign_witnesses_and_canonical_owner(self):
        for omega,C,W,G in (((1,1j,1),(-1,0,1),(0,math.sqrt(3),0),0),
                            ((1,1j,0),(0,0,1),(-.5,math.sqrt(3)/2,0),1)):
            with patch.object(readouts,'z_chiral',wraps=readouts.z_chiral) as canonical:
                r=a.axial_snapshot(omega)
            canonical.assert_called_once()
            self.near(r.C,C);self.near(r.W,W);self.assertEqual(r.Gamma,G)

    def test_reconstruction_zero_real_generic_and_bilinear(self):
        for v in ((0,0,0),(1,2,3),(1,1j,1),(.2+.3j,-.4+.1j,.1-.2j)):
            r=a.axial_snapshot(v)
            for field in fields(r.residuals):
                value=np.asarray(getattr(r.residuals,field.name))
                self.assertLessEqual(float(np.max(np.abs(value))),512*U*max(1,r.intensity**2))
            root=math.sqrt(3)
            reconstructed=((-r.W[0]-root*r.W[1]+r.Gamma)/3,
                           (2*r.W[0]+r.Gamma)/3,(-r.W[0]+root*r.W[1]+r.Gamma)/3)
            self.near(reconstructed,r.C)
            self.near([x+y for x,y in zip(r.C_parallel,r.C_perp)],r.C)
        r=a.axial_snapshot((1,1j,1))
        self.assertEqual(r.intensity,3)
        self.assertEqual(abs(sum(z*z for z in (1,1j,1)))**2,1)
        self.assertNotEqual(r.intensity**2-4*r.C_norm**2,r.intensity**2)

    def test_frozen_snapshots_and_all_seven_terms(self):
        for row in F['cases']:
            with self.subTest(row=row['name']):
                state,p=inputs(row);r=a.axial_source_budget(state,p)
                self.area_near(r.before_snapshot,row['snapshot'],512)
                self.near(r.before_snapshot.S,row['snapshot']['S'])
                self.assertEqual(len(r.amplitude_terms),5);self.assertEqual(len(r.phase_terms),2)
                for term in (*r.amplitude_terms,*r.phase_terms): self.area_near(term,row['terms'][term.name])
                self.area_near(r.predicted_after,row['predicted'])
                for field in ('S','A','phases','delta','d'):
                    self.near(getattr(r.pre_sync_prediction,field),row['pre_sync'][field],2048)
                for z, pair in zip(r.pre_sync_prediction.omega,row['pre_sync']['omega']):
                    # mpmath matrix arithmetic emits exact real zero as mpf;
                    # preserve the frozen oracle bytes, decode its real case.
                    if isinstance(pair,str): pair=(pair,0)
                    self.near((z.real,z.imag),pair,2048)
                for residual in (r.congruence_residual,r.pair_rotation_residual):
                    for name in ('A','C','W','Gamma'):
                        value=np.asarray(getattr(residual,name))
                        self.assertLessEqual(float(np.max(np.abs(value))),2048*U*float(row['budget_scale']))

    def test_snapshot_common_phase_and_conjugation(self):
        v=np.array([.2+.3j,-.4+.1j,.1-.2j]);base=a.axial_snapshot(v)
        for phase in (0,.3,math.pi,-2.1):
            rotated=a.axial_snapshot(v*complex(math.cos(phase),math.sin(phase)))
            for field in ('S','A','C','W','Gamma'):self.near(getattr(rotated,field),getattr(base,field))
        conjugate=a.axial_snapshot(v.conjugate())
        for field in ('C','W','Gamma'):self.near(getattr(conjugate,field),(-np.asarray(getattr(base,field))).tolist())
        self.near(conjugate.S,base.S)

    def test_fourier_entrance_unequal_uniform_and_wrong_normalization(self):
        v=(1,complex(-.5,-math.sqrt(3)/2),complex(-.5,math.sqrt(3)/2))
        s=a.State(omega=v,update_index=0);r=a.axial_snapshot(v)
        self.near(r.intensity,3);self.near(r.W,(0,0,0));self.near(r.Gamma,-3*math.sqrt(3)/2)
        p=a.Parameters(eps=.05,g=.2,phase_strength=.3724763946042135,k=(1,1.2208964704604097,6.35310346037241))
        result=a.axial_source_budget(s,p)
        b=[1+.05*(k-1)-3*.2 for k in p.k];c0=-math.sqrt(3)/2
        expected=(c0*b[1]*b[2],c0*b[2]*b[0],c0*b[0]*b[1])
        self.near(result.predicted_after.C,expected,2048)
        self.assertGreater(np.linalg.norm(result.predicted_after.W),.01)
        equal=a.axial_source_budget(s,a.Parameters(eps=.05,g=.2,phase_strength=p.phase_strength,k=(1,1,1)))
        self.near(equal.predicted_after.W,(0,0,0),2048)
        wrong=a.axial_snapshot(np.asarray(v)*math.sqrt(3))
        self.near(wrong.intensity,9);self.assertGreater(abs(wrong.Gamma-r.Gamma),1)

    def test_zero_stratum_exception_and_resonance(self):
        v=np.asarray((1,-1,0))*complex(math.cos(math.pi/6),math.sin(math.pi/6))
        s=a.State(omega=v,update_index=0)
        for strength,C,W in ((math.pi/12,(0,0,-.5),(.25,-math.sqrt(3)/4,0)),(math.pi/2,(0,0,0),(0,0,0))):
            r=a.axial_source_budget(s,a.Parameters(eps=0,g=0,phase_strength=strength,k=(1,1,1)))
            self.near(r.predicted_after.C,C,2048);self.near(r.predicted_after.W,W,2048)

    def test_direct_step_comparison_and_adjacency(self):
        for row in F['cases']:
            s,p=inputs(row);after=a.step(s,p,topology='triad')
            r=a.axial_source_budget(s,p,after=after)
            self.assertEqual(r.comparison_status,'SUPPLIED_ADJACENT_PAIR')
            self.assertEqual(r.after_index,s.update_index+1)
            self.near(r.actual_after_snapshot.W,r.predicted_after.W,2048,float(row['budget_scale']))
            for name in ('A','C','W','Gamma'):
                self.near(getattr(r.comparison_residuals,name),
                          (np.asarray(getattr(r.actual_after_snapshot,name))-np.asarray(getattr(r.predicted_after,name))).tolist(),2048)
        with self.assertRaises(ValueError):a.axial_source_budget(s,p,after=s)
        with self.assertRaises(ValueError):a.axial_source_budget(s,p,after=a.State(omega=s.omega,update_index=9))

    def test_prediction_only_null_and_state_insufficiency(self):
        pairs=[inputs(r) for r in F['cases'] if r['name'].startswith('same_A')]
        first,second=[a.axial_source_budget(s,p) for s,p in pairs]
        self.assertEqual(first.before_snapshot.A,second.before_snapshot.A)
        self.near(second.predicted_after.C,[301/400*x for x in first.predicted_after.C])
        self.assertNotEqual(first.predicted_after,second.predicted_after)
        self.assertEqual(first.comparison_status,'PREDICTION_ONLY')
        self.assertIsNone(first.actual_after_snapshot);self.assertIsNone(first.comparison_residuals);self.assertIsNone(first.after_index)

    def test_strict_input_and_precision_refusal(self):
        for v in ((1,2),(1,2,3,4,5,6),(1,float('nan'),0),(1,complex(0,float('inf')),0)):
            with self.assertRaises(ValueError):a.axial_snapshot(v)
        for v in ((True,1,0),('1',1,0),(object(),1,0)):
            with self.assertRaises(TypeError):a.axial_snapshot(v)
        for v in ((1e-200,1e-200j,0),(1e200,1e200j,0),(float.fromhex('0x0.0000000000001p-1022'),1j,0)):
            with self.assertRaises(a.ResponsePrecisionError):a.axial_snapshot(v)
        s,p=inputs(F['cases'][0])
        with self.assertRaises(TypeError):a.axial_source_budget(s,object())
        with self.assertRaises(TypeError):a.axial_source_budget(s,p,after=object())
        with self.assertRaises(ValueError):a.axial_source_budget(a.State(omega=s.omega*2,update_index=7),p)
        with self.assertRaises(a.ResponsePrecisionError):a.axial_source_budget(s,a.Parameters(eps=1e308,g=1e308,phase_strength=1,k=(1,1,1)))

    def test_deep_immutability_copy_repeatability(self):
        original=np.array([.2+.3j,-.4+.1j,.1-.2j]);s=a.State(omega=original,update_index=7)
        _,p=inputs(F['cases'][0]);r=a.axial_source_budget(s,p);copy=a.axial_source_budget(s,p)
        original[:]=0;self.assertEqual(r,copy)
        def walk(value):
            self.assertNotIsInstance(value,(dict,list,np.ndarray))
            if is_dataclass(value):
                with self.assertRaises((FrozenInstanceError,AttributeError)):setattr(value,fields(value)[0].name,None)
                for f in fields(value):walk(getattr(value,f.name))
            elif isinstance(value,tuple):
                for x in value:walk(x)
        walk(r);walk(a.axial_snapshot(s.omega))

    def test_no_hidden_advancement_or_io(self):
        s,p=inputs(F['cases'][0])
        with ExitStack() as stack:
            for module,name in ((dynamics,'step3'),(dynamics,'step_ring'),(dynamics,'phase_sync'),
                                (a,'step'),(a,'run'),(a,'resume'),(_runner,'run'),(_runner,'resume'),
                                (z_manifold,'advance_clock'),(z_manifold,'advance_ema'),
                                (a,'advance_clock'),(a,'advance_ema')):
                stack.enter_context(patch.object(module,name,side_effect=AssertionError('advancement forbidden')))
            stack.enter_context(patch('builtins.open',side_effect=AssertionError('I/O forbidden')))
            a.axial_snapshot(s.omega);a.axial_source_budget(s,p)
        from kernel_physics import axial_observables as owner
        tree=ast.parse(Path(owner.__file__).read_text())
        for node in ast.walk(tree):
            if isinstance(node,(ast.Import,ast.ImportFrom)):
                names=[n.name for n in node.names]+[getattr(node,'module','') or '']
                self.assertFalse(any(any(word in n for word in ('random','socket','pathlib','requests','_runner','_records','geometry','research','historical')) for n in names))

    def test_public_facade_and_old_signatures(self):
        from kernel_physics import axial_observables as owner
        old=json.loads((FIXTURES/'old_api.json').read_text())
        added={'AXIAL_OBSERVATION_API_VERSION','AXIAL_OBSERVER_REVISION','AxialSnapshot','AxialSourceBudget','axial_snapshot','axial_source_budget'}
        self.assertEqual(set(a.__all__),set(old['exports'])|added)
        for name,sig in old['signatures'].items():self.assertEqual(str(inspect.signature(getattr(a,name))),sig,name)
        self.assertEqual(a.AXIAL_OBSERVATION_API_VERSION,'1.0.0');self.assertEqual(a.AXIAL_OBSERVER_REVISION,'AXIAL_M1_V1')
        s,p=inputs(F['cases'][0])
        for name,args in (('axial_snapshot',(s.omega,)),('axial_source_budget',(s,p))):
            with patch.object(owner,name,wraps=getattr(owner,name)) as call:
                getattr(a,name)(*args)
            call.assert_called_once()


class NegativeControls(unittest.TestCase):
    near = ScientificTests.near
    def test_wrong_sign_component_order_and_normal_attachment(self):
        for v in ((1,1j,1),(1,1j,0)):
            r=a.axial_snapshot(v)
            for wrong in (-np.asarray(r.C),np.roll(r.C,1)):
                with self.assertRaises(AssertionError):self.near(wrong,r.C)
            N=np.array([[-math.sqrt(3)/2,0,math.sqrt(3)/2],[.5,-1,.5],[0,0,0]])
            with self.assertRaises(AssertionError):self.near(N@r.C,r.W)

    def test_each_omitted_term_is_detected(self):
        row=F['cases'][0];s,p=inputs(row);r=a.axial_source_budget(s,p)
        for term in (*r.amplitude_terms,*r.phase_terms):
            with self.subTest(omitted=term.name),self.assertRaises(AssertionError):
                self.near((np.asarray(r.predicted_after.A)-np.asarray(term.A)).tolist(),row['predicted']['A'],2048)

    def test_reversed_pair_delta_and_sequential_sync_are_detected(self):
        row=F['cases'][0];s,p=inputs(row);r=a.axial_source_budget(s,p)
        pre=r.pre_sync_prediction;A=np.asarray(pre.A);S=np.asarray(pre.S);d=np.asarray(pre.d)
        wrong=A*np.cos(d)-S*np.sin(d)
        with self.assertRaises(AssertionError):self.near(wrong.tolist(),row['predicted']['A'],2048)
        phases=list(pre.phases)
        for i in range(3):phases[i]+=p.phase_strength*sum(math.sin(3*(phases[j]-phases[i])) for j in range(3) if j!=i)
        q=[abs(z)*complex(math.cos(phi),math.sin(phi)) for z,phi in zip(pre.omega,phases)]
        sequential=[[q[i].real*q[j].imag-q[i].imag*q[j].real for j in range(3)] for i in range(3)]
        with self.assertRaises(AssertionError):self.near(sequential,row['predicted']['A'],2048)


class RecordCompatibilityTests(unittest.TestCase):
    def test_old_record_load_and_strict_resume_refusal(self):
        raw=(FIXTURES/'old_run.json').read_text();old=a.RunRecord.from_json(raw)
        self.assertEqual(old.to_json(),raw)
        with self.assertRaisesRegex(ValueError,'matching source revision and module hashes'):a.resume(old,updates=1)

    def test_candidate_resume_and_passive_trajectory_noninterference(self):
        s,p=inputs(F['cases'][0]);v=a.Provenance(kind='user_supplied',source_id='axial noninterference',source_revision=None,locator='test',literal_values={},notes='')
        def run():return a.run(s,p,topology='triad',updates=2,parameter_provenance=v,initialization_provenance=v,
                             observers=(a.historical_observer('paper_e_staged_v1'),a.historical_observer('paper_e_ema_v1')),
                             readouts=('z_chiral',),diagnostics=('chiral_area_accounting','intensity_budget'))
        first=run();baseline=a.resume(first,updates=2)
        a.axial_snapshot(s.omega);a.axial_source_budget(s,p)
        second=run();a.axial_source_budget(s,p);continued=a.resume(second,updates=2)
        self.assertEqual(first.to_json(),second.to_json());self.assertEqual(baseline.to_json(),continued.to_json())
        self.assertEqual(a.RunRecord.from_json(continued.to_json()).to_json(),continued.to_json())


if __name__=='__main__':unittest.main()
