"""K2c P7/P8: exact algebra, full-map references, then bounded binary64 parity.

PASS SUPPORTS: Paper F's exact coefficients, independent finite-amplitude
eight-step parity and one-step full-composition lambda sensitivity.
PASS DOES NOT SUPPORT: GLOBAL ATTRACTOR CLAIM; SIX-AXIS PHYSICAL SELECTOR;
INFINITE-TIME CERTIFICATION FROM EIGHT STEPS; JET == FINITE AMPLITUDE;
FLOAT64 CERTIFICATION OF KAPPA_INFINITY; FLOAT64 CERTIFICATION OF LIMITING
LAMBDA DERIVATIVE; 243/160 AS FULL-COMPOSITION COEFFICIENT; LARGE-LAMBDA
EXTRAPOLATION. Fixed-n O(h^6) is not a remainder uniform in n. No dynamics
layer, physical selector, geometry coupling or second lambda order is added.
"""
import math
import unittest

import mpmath as mp
import sympy as sp

from kernel_physics.tests.parity_oracles import paper_f_oracle as oracle
from kernel_physics.tests.test_parity_oracle_boundaries_k2c import GuardedOracleCase


EVIDENCE={'checks':{},'exact':{},'P7':[],'P8':[],'P8_leading':[],
          'remainder_policy':'Oracle-side qualification only; no ratio or empirical pass threshold.',
          'oracle_imports':['mpmath','sympy'],'oracle_project_dependencies':[],
          'P7_kappa_infinity_runtime_tested':False,'P8_limiting_derivative_runtime_tested':False}
REFERENCES=None


def number(value):
    return mp.mpf(int(value.p))/int(value.q)


def text(value):
    return mp.nstr(value,40)


def count(kind,n=1):
    EVIDENCE['checks'][kind]=EVIDENCE['checks'].get(kind,0)+n


def prepare_references():
    """All fixtures, signs and envelopes exist before any runtime evolution."""
    global REFERENCES
    if REFERENCES is not None:
        return REFERENCES
    with mp.workdps(80):
        kappas=[number(x) for x,_ in oracle.finite_coefficients()]
        p7=[]
        for sign in (1,-1):
            phi=sign*mp.pi/12
            for hs in ('.02','.01'):
                h=mp.mpf(hs)
                rows=oracle.full_trajectory(h,phi)
                for row in rows:
                    jet=kappas[row['n']-1]*h**4*mp.sin(6*phi)
                    remainder=row['angle']-jet
                    p7.append(dict(sign=sign,h=hs,phi=phi,**row,jet=jet,remainder=remainder,
                                   normalized_remainder=remainder/h**6,
                                   resolved=abs(row['angle'])>4*256*mp.mpf(2)**-52))
        p8=[]
        for sign in (1,-1):
            for ds in ('.01','.001','.0001'):
                p8.append(dict(sign=sign,delta=ds,
                               **oracle.difference_envelope(mp.mpf('.02'),sign*mp.pi/12,mp.mpf(ds))))
        REFERENCES=dict(P7=p7,P8=p8)
        return REFERENCES


def runtime_angle(C,phi):
    """Binary64 atan2 using the source-oriented basis, rounded once."""
    q,qp=oracle.basis(phi)
    A=math.fsum(float(c)*float(b) for c,b in zip(C,qp))
    B=-math.fsum(float(c)*float(b) for c,b in zip(C,q))
    if A<=0:
        raise AssertionError('K2C_STATUS=HOLD: runtime leaves accepted local angle branch')
    return math.atan2(B,A)


class EvidenceCase(GuardedOracleCase):
    def exact(self,actual,expected=0,kind='EXACT_SYMBOLIC_CHECKS'):
        if isinstance(actual,sp.MatrixBase):
            difference=actual-expected if isinstance(expected,sp.MatrixBase) else actual
            for value in difference:
                self.exact(value,0,kind)
        else:
            self.assertEqual(sp.factor(actual-expected),0,'K2C_STATUS=HOLD: exact algebra disagreement')
            count(kind)

    def bounded(self,actual,expected,bound,kind):
        error=abs(actual-expected)
        self.assertLessEqual(error,bound,f'K2C_STATUS=HOLD: error={text(error)}, bound={text(bound)}')
        count(kind)
        return error


class ExactPaperFTests(EvidenceCase):
    def test_basis_and_parameter_general_one_step(self):
        e,u,v=oracle.basis_exact()
        self.exact(u.cross(v),e/sp.sqrt(3))
        self.exact(sp.Matrix.hstack(u,v,e/sp.sqrt(3)).T*sp.Matrix.hstack(u,v,e/sp.sqrt(3)),sp.eye(3))
        p=oracle.one_step_projections()
        for residual in p['residuals']:
            self.exact(residual)
        a,eps,_,_,_=p['symbols']
        self.exact(p['leading'].subs({a:sp.Rational(2,5),eps:sp.Rational(1,20)}),-sp.Rational(1,5760))
        EVIDENCE['exact']['one_step_projections']='Paper F (23): three exact polynomial identities'
        EVIDENCE['exact']['one_step_leading']=str(p['leading'])

    def test_independently_expanded_amplitude_and_phase_lifts(self):
        d=oracle.exact_algebra()
        a,eps,A,X,D,E,R,F,K=[d[k] for k in ('a','eps','A','X','D','E','R','F','K')]
        r=a-2*eps
        expected=dict(A=a*A,X=r*X-eps*A*A/sp.sqrt(6),
                      D=D-eps*(2*A*X/3+A**3/(3*sp.sqrt(6))),
                      E=r*E-eps*(sp.sqrt(6)*X*X+2*A*D+A*A*X/3),
                      R=a*R-eps*(2*X*D+2*A*E/sp.sqrt(6)+A*X*X/3+3*A*A*D/sp.sqrt(6)))
        for key in expected:
            self.exact(d['amp'][key],expected[key])
        self.exact(d['amp_F'],r*F-eps*(sp.sqrt(6)*X*X+(1+2*a)*A*A*X/3+a*A**4/(3*sp.sqrt(6))))
        self.exact(d['increment'],-eps*F/(a*sp.sqrt(6))+eps*(2*r-1)*X*X/(6*a)
                   +eps*(r-2*eps)*A*A*X/(6*a*sp.sqrt(6))-eps*eps*A**4/(36*a))
        phase=dict(A=-9*A,X=9*A*A/sp.sqrt(6),D=-3*A*X,E=9*A*D)
        for key in phase:
            self.exact(d['sync'][key],phase[key])
        self.exact(d['sync_F'],-3*A*A*X)
        self.exact(d['sync_K'],-9*K-3*X*A**3/sp.sqrt(6)+47*A**5/sp.Integer(16))
        self.exact(d['sync_kappa'],-3*X*A*A/(2*sp.sqrt(6))+47*A**4/sp.Integer(32))
        expected_T=sp.Matrix([[a**4,0,0,0],[-eps*a*a/sp.sqrt(6),a*a*r,0,0],
            [eps*eps/6,-2*r*eps/sp.sqrt(6),r*r,0],
            [-eps*a/(3*sp.sqrt(6)),-eps*(1+2*a)/3,-eps*sp.sqrt(6),r]])
        self.exact(d['T0'],expected_T)
        self.exact(d['Ps'],sp.Matrix([[-36,0,0,0],[9/sp.sqrt(6),-18,0,0],[0,18/sp.sqrt(6),0,0],[0,-3,0,0]]))
        EVIDENCE['exact'].update({key:str(d[key]) for key in ('T0','Ps','ell','ell_s','sync_kappa')})

    def test_finite_coefficients_and_infinite_sum(self):
        a,eps=sp.Rational(2,5),sp.Rational(1,20)
        coefficients=oracle.finite_coefficients()
        for n,(lift,scalar) in enumerate(coefficients,1):
            self.exact(lift,scalar)
            self.exact(lift,oracle.finite_closed(n,a,eps))
        self.exact(coefficients[0][0],-sp.Rational(1,5760))
        self.exact(coefficients[1][0],-sp.Rational(347,7200000))
        aa,rr=sp.symbols('a r',real=True)
        N=4*aa**3*rr**2+3*aa**3*rr-4*aa**3+aa**2*rr**2-4*aa**2+4*aa*rr**2-aa-2*rr**2-3*rr+2
        closed=-(aa-rr)**2*N/(288*aa*(1+aa)*(1+aa*aa)*(1-rr)**2*(1+rr)*(1-aa*aa*rr))
        self.exact(oracle.infinite_scalar(aa,rr),closed)
        infinity,derivative=oracle.infinite_coefficients()
        self.exact(infinity,oracle.infinite_scalar(a,a-2*eps))
        self.exact(infinity,sp.Rational(13375,1107936648),'ORACLE_PAPER_ONLY_CHECKS')
        self.exact(derivative,sp.Rational(34494041501,849664304944),'ORACLE_PAPER_ONLY_CHECKS')
        EVIDENCE['exact'].update(kappa=[str(x) for x,_ in coefficients],kappa_infinity=str(infinity),
                                 limiting_lambda_derivative=str(derivative))

    def test_full_composition_derivative_and_isolated_coefficient(self):
        d=oracle.exact_algebra()
        a,eps=d['a'],d['eps']
        self.exact(d['one_step_lambda'],eps*a*a/4+47*a**4/sp.Integer(32))
        value=d['one_step_lambda'].subs({a:sp.Rational(2,5),eps:sp.Rational(1,20)})
        self.exact(value,sp.Rational(99,2500))
        self.exact(d['isolated'],sp.Rational(243,160))
        self.assertNotEqual(value,d['isolated'])
        count('NEGATIVE_FALSIFIER_CHECKS')
        EVIDENCE['exact'].update(one_step_lambda_general=str(d['one_step_lambda']),
                                 one_step_lambda=str(value),isolated_phase_lambda=str(d['isolated']))


class HighPrecisionQualificationTests(EvidenceCase):
    @mp.workdps(80)
    def test_full_map_precision_remainders_and_sign_predictions(self):
        references=prepare_references()
        for sign in (1,-1):
            for hs in ('.02','.01'):
                with mp.workdps(100):
                    higher=oracle.full_trajectory(mp.mpf(hs),sign*mp.pi/12)
                selected=[x for x in references['P7'] if x['sign']==sign and x['h']==hs]
                for row,high in zip(selected,higher):
                    for x,y in zip(row['state'],high['state']):
                        self.bounded(x,y,mp.mpf('1e-65'),'HIGH_PRECISION_FULL_MAP_CHECKS')
                    self.bounded(row['angle'],high['angle'],mp.mpf('1e-65'),'HIGH_PRECISION_FULL_MAP_CHECKS')
                    self.assertNotEqual(row['jet'],row['angle'],'The truncated jet must not replace the full map')
                    self.assertTrue(mp.isfinite(row['normalized_remainder']))
                    count('ASYMPTOTIC_QUALIFICATION_CHECKS')
                    expected_sign=sign*(-1 if row['n']<=3 else 1)
                    self.assertEqual(int(mp.sign(row['angle'])),expected_sign)
                    count('HIGH_PRECISION_FULL_MAP_CHECKS')
        # Opposite orientations, independently generated; no sign copied over.
        for row in references['P7'][:16]:
            other=next(x for x in references['P7'] if x['sign']==-1 and x['h']==row['h'] and x['n']==row['n'])
            self.bounded(row['angle'],-other['angle'],mp.mpf('1e-65'),'HIGH_PRECISION_FULL_MAP_CHECKS')
        # No numerical envelope is asserted for R/h^6. Its full table and the
        # exact fixed-n coefficient derivation supply the recorded qualification.

    @mp.workdps(80)
    def test_finite_amplitude_derivative_and_precomputed_envelopes(self):
        references=prepare_references()
        for sign in (1,-1):
            phi=sign*mp.pi/12
            for hs in ('.02','.01'):
                h=mp.mpf(hs)
                analytic=oracle.full_derivative(h,phi)
                # mpmath raises working precision for differentiation; oracle
                # functions do not clamp it, and no float64 value participates.
                differentiated=mp.diff(lambda lam:oracle.one_step_angle(h,phi,lam),mp.mpf(0))
                self.bounded(analytic,differentiated,mp.mpf('1e-65'),'HIGH_PRECISION_FULL_MAP_CHECKS')
                leading=mp.mpf(99)/2500*h**4*mp.sin(6*phi)
                self.assertNotEqual(analytic,leading)
                count('ASYMPTOTIC_QUALIFICATION_CHECKS')
                EVIDENCE['P8_leading'].append(dict(sign=sign,h=hs,derivative=text(analytic),
                    leading=text(leading),remainder=text(analytic-leading),normalized_remainder=text((analytic-leading)/h**6),
                    coefficient=text(analytic/(h**4*mp.sin(6*phi)))))
            for row in (x for x in references['P8'] if x['sign']==sign):
                with mp.workdps(100):
                    higher=oracle.difference_envelope(mp.mpf('.02'),sign*mp.pi/12,mp.mpf(row['delta']))
                for key in ('derivative','oracle_centered_difference','truncation_allowance','total_envelope'):
                    self.bounded(row[key],higher[key],mp.mpf('1e-65'),'HIGH_PRECISION_FULL_MAP_CHECKS')
                self.assertGreater(row['oracle_falsifier_margin'],100*row['total_envelope'])
                count('NEGATIVE_FALSIFIER_CHECKS')


class RuntimeParityTests(EvidenceCase):
    @mp.workdps(80)
    def test_p7_eight_update_state_chirality_angle_and_resolved_signs(self):
        references=prepare_references()  # Before importing/evolving runtime.
        from kernel_physics.dynamics import DynamicsConfig,step3
        from kernel_physics.readouts import z_chiral
        angle_bound=256*mp.mpf(2)**-52
        # State bound is independently predeclared; chirality and angle bounds
        # are frozen by K2c. A complex component is compared in absolute modulus.
        state_bound=mp.mpf('1e-13')
        config=DynamicsConfig(eps=.05,g=.2,phase_strength=0.,k=(1.,1.,1.))
        for sign in (1,-1):
            phi=sign*mp.pi/12
            for hs in ('.02','.01'):
                w=[complex(z) for z in oracle.seed(mp.mpf(hs),phi)]
                for row in (x for x in references['P7'] if x['sign']==sign and x['h']==hs):
                    w=step3(w,config)
                    C=z_chiral(w)
                    state_errors=[self.bounded(mp.mpc(complex(x)),y,state_bound,'BINARY64_RUNTIME_COMPARISONS')
                                  for x,y in zip(w,row['state'])]
                    errors=[self.bounded(mp.mpf(float(x)),y,mp.mpf('1e-13'),'BINARY64_RUNTIME_COMPARISONS')
                            for x,y in zip(C,row['C'])]
                    psi=runtime_angle(C,phi)
                    error=self.bounded(mp.mpf(psi),row['angle'],angle_bound,'BINARY64_RUNTIME_COMPARISONS')
                    status='SIGN_NOT_NUMERICALLY_RESOLVED'
                    if row['resolved']:
                        self.assertEqual(int(mp.sign(psi)),int(mp.sign(row['angle'])),'K2C_STATUS=HOLD: resolved sign failed')
                        count('BINARY64_RUNTIME_COMPARISONS')
                        status='RESOLVED_PASS'
                    EVIDENCE['P7'].append(dict(sign=sign,h=hs,n=row['n'],
                        oracle_angle=text(row['angle']),runtime_angle=text(mp.mpf(psi)),
                        max_state_error=text(max(state_errors)),max_C_error=text(max(errors)),
                        angle_error=text(error),angle_bound=text(angle_bound),angle_bound_fraction=text(error/angle_bound),
                        predicted_sign=int(mp.sign(row['angle'])),sign_status=status,
                        jet=text(row['jet']),remainder=text(row['remainder']),normalized_remainder=text(row['normalized_remainder'])))

    @mp.workdps(80)
    def test_p8_full_composition_centered_differences_and_wrong_coefficient(self):
        references=prepare_references()
        from kernel_physics.dynamics import DynamicsConfig,step3
        from kernel_physics.readouts import z_chiral
        for row in references['P8']:
            phi=row['sign']*mp.pi/12
            w=[complex(z) for z in oracle.seed(mp.mpf('.02'),phi)]
            delta=float(row['delta'])
            values=[]
            for lam in (delta,-delta):
                cfg=DynamicsConfig(eps=.05,g=.2,phase_strength=lam,k=(1.,1.,1.))
                values.append(runtime_angle(z_chiral(step3(w,cfg)),phi))
            runtime=(values[0]-values[1])/(2*delta)
            error=self.bounded(mp.mpf(runtime),row['derivative'],row['total_envelope'],'BINARY64_RUNTIME_COMPARISONS')
            margin=abs(mp.mpf(runtime)-row['isolated_leading'])-row['isolated_envelope']
            self.assertGreater(margin,0,'K2C_STATUS=HOLD: isolated phase coefficient not falsified')
            count('NEGATIVE_FALSIFIER_CHECKS')
            recorded={key:text(value) for key,value in row.items() if key not in ('sign','delta','per_angle_allowances')}
            EVIDENCE['P8'].append(dict(sign=row['sign'],delta=row['delta'],**recorded,
                runtime_plus_angle=text(mp.mpf(values[0])),runtime_minus_angle=text(mp.mpf(values[1])),
                runtime_finite_difference=text(mp.mpf(runtime)),absolute_discrepancy=text(error),
                envelope_fraction=text(error/row['total_envelope']),falsifier_margin=text(margin),
                falsifier_margin_over_total_envelope=text(margin/row['total_envelope'])))


if __name__=='__main__':
    unittest.main()
