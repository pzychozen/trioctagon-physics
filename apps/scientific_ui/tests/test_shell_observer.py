from dataclasses import replace
from decimal import Decimal, localcontext, getcontext, ROUND_DOWN, Inexact, Rounded
import json
import math
import os
from pathlib import Path
import unittest
from trioctagon_ui.shell_reference import load_reference, plain, PRESETS
from trioctagon_ui.shell_observer import Request, evaluate, present, NumericError

# Declared before execution: absolute normalized tolerance 5e-14; transformed
# relative tolerance 3e-13 with absolute 5e-14 times scale/unit. IDs/topology exact.
NORMALIZED_ATOL=5e-14


class ObserverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.ref=load_reference()
    def run_request(self, **kw): return evaluate(self.ref,Request(**kw))

    def test_all_seven_presets_scales_units_frames(self):
        for preset in self.ref.data['presets']:
            for width in ('0.001','1','1000'):
                for unit in ('width','edge','chord','extension'):
                    for frame in ('centered','paper_c_global'):
                        with self.subTest(preset=preset['id'],width=width,unit=unit,frame=frame):
                            o=self.run_request(preset=preset['id'],width=width,unit=unit,frame=frame).data
                            self.assertEqual(len(o['branches']),42); self.assertEqual(o['event'],preset['exact_event'])
                            expected={p['branch']:p['xyz'] for p in preset['points']}
                            for b in o['branches']:
                                for actual,want in zip(b['centered_over_w'],expected[b['branch']]): self.assertAlmostEqual(actual,want,delta=NORMALIZED_ATOL)
                                norm=b['centered_over_w'] if frame=='centered' else b['global_over_w']
                                for actual,want in zip(b['display_xyz'],norm): self.assertTrue(math.isclose(actual,want/o['unit_over_w'],rel_tol=3e-13,abs_tol=NORMALIZED_ATOL/o['unit_over_w']))
                            if o['event']:
                                self.assertEqual(o['marker_count'],18)
                                self.assertEqual(o['graph']['E'],self.ref.data['graphs'][o['event']]['E'])
                                self.assertEqual([f['vertices'] for f in o['hull']['faces']],[f['vertices'] for f in self.ref.data['hulls'][o['event']]['faces']])
                            else: self.assertIsNone(o['hull']); self.assertIsNone(o['graph'])

    def test_endpoint_pins_and_neighbours(self):
        examples=[]
        for mode,pin in (('R',float.fromhex('0x1.3a0c09c3e0a95p-1')),('C',float.fromhex('0x1.a827999fcef32p-2'))):
            for label,value in [('lower',math.nextafter(pin,-math.inf)),('pin',pin),('upper',math.nextafter(pin,math.inf))]:
                if label=='lower':
                    with self.assertRaises(NumericError): self.run_request(preset=None,mode=mode,value=repr(value))
                    examples.append({'mode':mode,'raw':repr(value),'hex':value.hex(),'status':'REJECTED'})
                else:
                    o=self.run_request(preset=None,mode=mode,value=repr(value)).data
                    self.assertIsNone(o['event']); self.assertIsNone(o['certified_unique_count']); self.assertEqual(o['marker_count'],42)
                    self.assertIsNone(o['hull']); self.assertIsNone(o['graph'])
                    if label=='pin': self.assertEqual(o['ell_over_w'],0); self.assertEqual(o['adjustments'][0]['kind'],'lower_endpoint_representation')
                    else: self.assertGreater(o['ell_over_w'],0); self.assertEqual(o['adjustments'],())
                    examples.append({'mode':mode,'raw':repr(value),'hex':value.hex(),'status':'VALID','result':plain(o)})
        if os.environ.get('TRIOCTAGON_UI_EVIDENCE'):
            Path(os.environ['TRIOCTAGON_UI_EVIDENCE'],'shell-v01.json').write_text(json.dumps(examples,indent=2),encoding='utf-8')

    def test_exact_decimal_not_rounded_identity(self):
        for mode,text,event in [('C','1.000','A'),('ell','-0','original'),('ell','1e0','B')]:
            self.assertEqual(self.run_request(preset=None,mode=mode,value=text).data['event'],event)
        for mode in ('C','ell'):
            for value in ('0.99999999999999999999999999','1.00000000000000000000000001'):
                o=self.run_request(preset=None,mode=mode,value=value).data
                self.assertIsNone(o['event']); self.assertEqual(o['parsed_decimal'],value)
                self.assertEqual(o['input_binary64_hex'],1.0.hex())
        for p in self.ref.data['presets'][:3]:
            o=self.run_request(preset=None,mode='R',value=str(p['numeric']['R_over_w'])).data
            self.assertIsNone(o['event'])

    def test_present_preserves_origin(self):
        for origin in (Request(),Request(preset=None,mode='R',value='0.7637626158259734')):
            o=evaluate(self.ref,origin)
            for frame in ('centered','paper_c_global'):
                q=present(self.ref,o,width='2',unit='edge',frame=frame)
                self.assertEqual(q.origin.value,o.origin.value); self.assertEqual(q.data['event'],o.data['event'])
                self.assertEqual(q.data['t_over_w'],o.data['t_over_w'])

    def test_zero_unit_routes(self):
        for req in (Request(preset='original',unit='extension'),Request(preset=None,mode='ell',value='0',unit='extension')):
            o=evaluate(self.ref,req).data; self.assertEqual(o['unit'],'width'); self.assertEqual(o['adjustments'][-1]['kind'],'zero_extension_unit_transition')
        for mode,value in [('R','0.6133730937584284'),('C','0.41421356237309503')]:
            with self.assertRaises(NumericError): self.run_request(preset=None,mode=mode,value=value,unit='extension')

    def test_invalid_and_supported_resolution(self):
        for value in ('','nan','Infinity','1_0','1/2','1e81','1e-81','1e13','1e-51','9'*129,'0.'+'1'*65,'-1'):
            with self.subTest(value=value):
                with self.assertRaises(NumericError): self.run_request(preset=None,mode='ell',value=value)
        for width in ('0','-1','1e-13','1e13'):
            with self.assertRaises(NumericError): self.run_request(width=width)
        o=self.run_request(preset=None,mode='ell',value='1e-50',unit='extension').data
        self.assertGreater(o['ell_over_w'],0); self.assertIsNone(o['event'])

    def test_decimal_context_independent_and_preserved(self):
        req=Request(preset=None,mode='R',value='1.000000000000001')
        normal=plain(evaluate(self.ref,req).data)
        with localcontext() as hostile:
            hostile.prec=3; hostile.rounding=ROUND_DOWN; hostile.Emax=3; hostile.Emin=-3
            hostile.traps[Inexact]=True; hostile.traps[Rounded]=True
            before=repr(hostile)
            self.assertEqual(plain(evaluate(self.ref,req).data),normal)
            self.assertEqual(repr(hostile),before)

    def test_independent_120_digit_scalars(self):
        for mode,value in [('R','0.6133730937584285'),('R','10'),('C','0.4142135623730951'),('C','1.00000000000000000001'),('ell','1e-50'),('ell','1')]:
            o=self.run_request(preset=None,mode=mode,value=value).data
            with localcontext() as c:
                c.prec=120; h=(Decimal(2).sqrt()-1)/2; x=Decimal(value)
                t=(x*x-Decimal(1)/3).sqrt() if mode=='R' else (x/2 if mode=='C' else h+x)
                ell=x if mode=='ell' else t-h
                actual=Decimal(o['resolved_decimal']['ell_over_w'])
                self.assertLess(abs(actual-ell),Decimal('1e-70'))


if __name__=='__main__': unittest.main()
