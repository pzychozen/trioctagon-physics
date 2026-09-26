"""Independent Paper E observers, algebraic diagnostics, and qualifications."""

import json
import math
from unittest.mock import patch

import mpmath as mp
import numpy as np
import sympy as sp

from kernel_physics import api, dynamics as d, z_manifold as z, z_diagnostics as dg
from kernel_physics.tests.parity_oracles import paper_e_oracle as e
from kernel_physics.tests.test_parity_oracle_boundaries import ParityCase, gate_record


class P9Tests(ParityCase):
    """PASS SUPPORTS: Paper E identities, literal EMA, constructor distinction,
    and passive observation/advancement in the tested runtime environment.
    PASS DOES NOT SUPPORT: physical interpretation of observer constants.
    """

    def test_exact_identities_and_hand_observer(self):
        theta,zs,rho,amp,lock,m,j = sp.symbols("theta z rho amp lock m j",real=True)
        macro = sp.Matrix([zs*sp.cos(theta),zs*sp.sin(theta),zs])
        self.exact("P9","exact macro cone",[macro[0]**2+macro[1]**2-macro[2]**2])
        self.exact("P9","exact macro norm",[macro.dot(macro)],[2*zs**2])
        self.exact("P9","third harmonic periodicity",[amp*rho*sp.cos(3*(theta+2*sp.pi/3-lock))],[amp*rho*sp.cos(3*(theta-lock))])
        self.exact("P9","rational EMA identity",[sp.Rational(99,100)*m+sp.Rational(1,100)*j],[m+sp.Rational(1,100)*(j-m)])
        w = np.array([3+0j,4j,0j])
        before = w.tobytes()
        c = z.Clock(q=0,N=12,t=0,q_step=-2)
        cfg = z.StagedConfig(lambda_vp=3,gamma=.5,theta_lock=0,alpha=2,beta=.5)
        out = z.observe_staged(w,c,cfg)
        # Norm=5, rho=5/6, z=5/2, C=(0,0,12), T=(5,0,11).
        self.discrete("P9","hand norm",z.state_norm(w),5.)
        self.discrete("P9","hand saturation",z.saturated_norm(w),5/6)
        self.exact("P9","hand harmonic/staged scalar",[sp.Rational(out.z)],[sp.Rational(5,2)])
        self.exact("P9","hand macro",list(out.Z_macro),[sp.Rational(5,2),0,sp.Rational(5,2)])
        self.exact("P9","hand chirality",list(out.Z_chiral),[0,0,12])
        self.exact("P9","hand blend",list(out.Z_total),[5,0,11])
        advanced = z.advance_clock(c,.125)
        self.discrete("P9","clock modular integer advance",(advanced.q,advanced.N,advanced.t,advanced.q_step),(10,12,.125,-2))
        self.discrete("P9","huge sector reduction",z.clock_angle(z.Clock(q=12*10**100,N=12)),0.)
        self.discrete("P9","clock angle quarter turn",z.clock_angle(z.Clock(q=3,N=12)),math.pi/2)
        self.discrete("P9","observation and clock retain state bytes",w.tobytes(),before)

    @mp.workdps(80)
    def test_retained_high_precision_fixtures_and_macro_bound(self):
        fixtures = [([.3+.7j,-.4+.2j,.1-.8j],z.Clock(q=5,N=17,t=.7),z.StagedConfig()),
                    ([2-.5j,-.3-1j,.7+.4j],z.Clock(q=-2,N=9,t=-.3),z.StagedConfig(lambda_vp=-.8,gamma=-.4,theta_lock=-.2))]
        for i,(w,c,cfg) in enumerate(fixtures):
            expected = e.staged(w,c.q,c.N,c.t,cfg.lambda_vp,cfg.gamma,cfg.theta_lock)
            # Retain exactly the already accepted test_z_manifold.py tolerance.
            bound = max(mp.mpf(2e-14)*abs(expected),mp.mpf(2e-15))
            out = z.observe_staged(w,c,cfg)
            error = abs(mp.mpf(out.z)-expected)
            receipt = dict(quantity="staged_scalar",fixture=f"retained scalar fixture {i}",runtime=str(out.z),oracle=mp.nstr(expected,35),absolute_error=mp.nstr(error,35),scale=mp.nstr(abs(expected),35),allowed_bound=mp.nstr(bound,35),normalized_bound_fraction=mp.nstr(error/bound,35),tolerance_class="HISTORICAL_FIXTURE_TOLERANCE",rule="max(2e-14*abs(reference),2e-15)")
            self.assertLessEqual(error,bound,f"K2A_STATUS=HOLD: {receipt}")
            rec = gate_record("P9")
            rec["checks"]["HISTORICAL_FIXTURE_TOLERANCE"] += 1
            rec["fixtures"].add(receipt["fixture"])
            if rec["worst"] is None or error/bound > mp.mpf(rec["worst"]["normalized_bound_fraction"]):
                rec["worst"] = receipt
            # Macro takes the supplied binary z; its exact algebraic cone/norm
            # residual is evaluated independently, with the frozen 8u*z^2.
            supplied = sp.Rational(out.z)
            scale = e.number(supplied**2)
            macro = z.macro_vector(out.z,c)
            exact_components = [sp.Rational(v) for v in macro]
            residuals = [sum(v*v for v in exact_components)-2*supplied**2,
                         exact_components[0]**2+exact_components[1]**2-exact_components[2]**2]
            self.bounded("P9",f"macro 8u residual fixture {i}",[e.number(v) for v in residuals],[0,0],[scale,scale],8,"BINARY64_TERM_SCALE")
        self.discrete("P9","zero macro branch",tuple(z.macro_vector(0,z.Clock(q=5,N=17))),(0.,0.,0.))

    def test_cubic_literal_01_and_current_memory(self):
        for w in ((1,1,1j),(1,1,-1j),(.5+.25j,-.75+.5j,1-.25j),(0,0,0)):
            exact = e.exact_state(w)
            J = sp.im(exact[0]*sp.conjugate(exact[1])*exact[2])
            self.exact("P9",f"cubic defining product {w}",[sp.Rational(z.cubic_j(w))],[J])
            self.discrete("P9",f"normalized cubic {w}",z.normalized_cubic(w),float(J/(1+abs(J))))
        w = np.array([1+0j,1+0j,1j])
        before = w.tobytes()
        expected = math.fsum(((1.0-.01)*0.0,.01*.5))
        alternate = math.fsum((.99*0.0,(1.0-.99)*.5))
        memory = z.advance_ema(w,z.EMAState(0))
        self.discrete("P9","literal .01 update binary hex",memory.m.hex(),expected.hex())
        self.falsifier("P9","literal .01 differs from 1-.99",memory.m.hex() != alternate.hex())
        for old in (-.5,.25,1.0):
            expected = math.fsum(((1.0-.01)*old,.01*.5))
            self.discrete("P9",f"ordered literal EMA old={old}",z.advance_ema(w,z.EMAState(old)).m.hex(),expected.hex())
        cfg = z.EMAConfig(lambda_vp=0)
        with patch.object(z,"advance_ema",side_effect=AssertionError("observation advanced memory")):
            out = z.observe_ema(w,z.Clock(),cfg,memory)
        self.discrete("P9","EMA uses current memory",out.z,memory.m)
        self.discrete("P9","advance_ema preserves state bytes",w.tobytes(),before)

    def test_constructor_zero_and_bitwise_passivity(self):
        w = np.array([.375+.875j,-.5+.25j,.125-.75j])
        saved = w.tobytes()
        clock = z.Clock()
        for cfg in (z.StagedConfig(),z.EMAConfig()):
            with patch.object(z,"advance_clock",side_effect=AssertionError),patch.object(z,"advance_ema",side_effect=AssertionError):
                stored = z.historical_constructor_zero(w,clock,cfg)
            recomputed = (z.observe_staged(w,clock,cfg) if isinstance(cfg,z.StagedConfig) else z.observe_ema(w,clock,cfg,z.EMAState(0)))
            self.discrete("P9","constructor marked zero",(stored.memory.m,stored.readout.z,stored.readout.initialization),(0.,0.,"historical_constructor_zero"))
            self.discrete("P9","constructor zero vectors",tuple(np.concatenate((stored.readout.Z_macro,stored.readout.Z_chiral,stored.readout.Z_total))),(0.,)*9)
            self.falsifier("P9","constructor zero differs from recomputed row zero",recomputed.z != 0 and np.any(recomputed.Z_total != 0))
        params = api.Parameters(eps=.0625,g=.1875,phase_strength=.125,k=(.5,1.25,1.5))
        provenance = api.Provenance(kind="user_supplied",source_id="K2a",source_revision=None,locator="P9 passive fixture",literal_values={},notes="No physical interpretation")
        state = api.State(omega=tuple(w),update_index=0)
        kwargs = dict(topology="triad",updates=8,parameter_provenance=provenance,initialization_provenance=provenance)
        plain = json.loads(api.run(state,params,observers=(),readouts=(),diagnostics=(),**kwargs).to_json())
        watched = json.loads(api.run(state,params,observers=(api.historical_observer("paper_e_staged_v1"),api.historical_observer("paper_e_ema_v1")),readouts=("z_chiral",),diagnostics=("chiral_area_accounting","intensity_budget","potential","readout_accounting","historical_alignment"),**kwargs).to_json())
        # The wire codec preserves every float bit (including signed zeros).
        a = json.dumps([r["omega"] for r in plain["samples"]],sort_keys=True).encode()
        b = json.dumps([r["omega"] for r in watched["samples"]],sort_keys=True).encode()
        self.discrete("P9","same runtime trajectory observer bytes",a,b)
        self.discrete("P10","diagnostics do not affect evolution bytes",a,b)
        self.discrete("P9","input omega immutable across all observations",w.tobytes(),saved)


class P10Tests(ParityCase):
    """PASS SUPPORTS: exact accounting identities and bounded passive diagnostics.
    PASS DOES NOT SUPPORT: finite-step Lyapunov descent, trajectory validity,
    physical state, or history-independent display coordinates.
    """

    def check_terms(self,fixture,reference,actual):
        for name,(value,scale) in reference.items():
            field,_,index = name.partition(":")
            target = actual[field] if isinstance(actual,dict) else getattr(actual,field)
            if index:
                target = target[int(index)]
            self.bounded("P10",fixture+" "+name,[target],[e.number(value)],[e.number(scale)],256)

    def test_symbolic_norm_q_gram_slack_budget_gradient(self):
        x,y = sp.symbols("x0:3",real=True),sp.symbols("y0:3",real=True)
        w = sp.Matrix([x[j]+sp.I*y[j] for j in range(3)])
        c = e.chiral(w)
        A,B,h = sum(v*v for v in x),sum(v*v for v in y),sum(a*b for a,b in zip(x,y))
        self.exact("P10","Gram determinant",[c.dot(c)],[A*B-h*h])
        self.exact("P10","sharp bound slack",[(A+B)**2/4-c.dot(c)],[(A-B)**2/4+h*h])
        m,t = sp.Matrix(sp.symbols("m0:3",real=True)),sp.Matrix(sp.symbols("c0:3",real=True))
        alpha,beta = sp.symbols("alpha beta",real=True)
        blend = alpha*m+beta*t
        for label,G in (("norm",sp.eye(3)),("Q",sp.diag(1,1,-1))):
            self.exact("P10",label+" blend expansion",[(blend.T*G*blend)[0]],[alpha**2*(m.T*G*m)[0]+beta**2*(t.T*G*t)[0]+2*alpha*beta*(m.T*G*t)[0]])
        eps,g = sp.symbols("eps g",real=True)
        k = sp.symbols("k0:3",real=True)
        potential = e.potential_expression(w,eps,g,k)
        D = sp.Matrix([-sp.diff(potential,x[j])-sp.I*sp.diff(potential,y[j]) for j in range(3)])
        s = [x[j]**2+y[j]**2 for j in range(3)]
        defining = sp.Matrix([eps*w[j]*(k[j]-s[j])+g*(sum(w)-3*w[j]) for j in range(3)])
        self.exact("P10","negative six-real gradient",D,defining)
        pair = sum((x[i]-x[j])**2+(y[i]-y[j])**2 for i,j in ((0,1),(0,2),(1,2)))
        after = sum(sp.expand_complex((w[j]+D[j])*sp.conjugate(w[j]+D[j])) for j in range(3))
        remainder = sum(sp.expand_complex(v*sp.conjugate(v)) for v in D)
        self.exact("P10","exact intensity budget",[after-sum(s)],[2*eps*sum(k[j]*s[j]-s[j]**2 for j in range(3))-2*g*pair+remainder])

    def test_supplied_readout_accounting_including_inconsistency(self):
        for name,M,C,T,zs,alpha,beta in (("consistent signed",[.5,-.25,.75],[-1,.125,.5],[1.25,-.53125,1.375],.75,2,-.25),
                                         ("inconsistent supplied",[1,2,3],[0,1,0],[8,0,1],1,1,1),
                                         ("all zero",[0]*3,[0]*3,[0]*3,0,1,.5)):
            # The first total is computed by hand: 2M-.25C.
            reference = e.readout_terms(M,C,T,zs,alpha,beta)
            rec = z.ZReadout(zs,M,C,T,"staged")
            out = dg.readout_accounting(rec,alpha=alpha,beta=beta)
            self.check_terms(name,reference,out)
            for label,v in (("M",M),("C",C),("T",T)):
                value,scale = e.defined(sp.Rational(v[0])**2,sp.Rational(v[1])**2,-sp.Rational(v[2])**2)
                self.bounded("P10",name+" Q("+label+")",[dg.quadratic_form(v)],[e.number(value)],[e.number(scale)],256)
            if name == "inconsistent supplied":
                self.falsifier("P10","inconsistent records retained",out.norm_residual != 0 and out.q_residual != 0 and tuple(out.blend_residual) == (7.,-3.,-2.))

    def test_gram_numeric_unclamped_and_gradient_budget(self):
        fixtures = (("dyadic",(.375+.875j,-.5+.25j,.125-.75j)),
                    ("near collinear",(1+1j,1+1j,1+(1+2**-26)*1j)),
                    ("zero",(0j,)*3))
        for name,w in fixtures:
            reference = e.gram_terms(w)
            out = dg.chiral_area_accounting(w)
            self.check_terms(name,reference,out)
            if name == "near collinear":
                self.falsifier("P10","nonzero rounded Gram residual not clamped",out.gram_residual != 0)
            reference = e.intensity_terms(w,.0625,.1875,(.5,1.25,1.5))
            config = d.DynamicsConfig(.0625,.1875,.25,(.5,1.25,1.5))
            potential_ref = reference.pop("potential")
            out = dg.intensity_budget(w,config)
            self.check_terms(name+" budget",reference,out)
            self.check_terms(name,{"potential":potential_ref},{"potential":dg.potential(w,config)})

    def test_finite_step_overshoot(self):
        w = (2.,)*3
        cfg = d.DynamicsConfig(1,.25,0,(1,)*3)
        before = e.potential_expression(e.exact_state(w),sp.Integer(1),sp.Rational(1,4),(1,)*3)
        after = e.potential_expression([-4]*3,sp.Integer(1),sp.Rational(1,4),(1,)*3)
        self.exact("P10","overshoot exact potentials",[before,after],[6,168])
        evolved = d.step3(w,cfg)
        self.discrete("P10","overshoot accepted step",tuple(evolved),(-4+0j,)*3)
        self.discrete("P10","overshoot runtime potentials",(dg.potential(w,cfg),dg.potential(evolved,cfg)),(6.,168.))
        self.falsifier("P10","negative gradient is not finite-step descent",after > before)

    def test_alignment_threshold_and_displays(self):
        aligned = dg.historical_alignment([3,4,0],[0,0,2],[3,4,0])
        self.discrete("P10","hand alignment dot products",(aligned.d_TM,aligned.d_CM,aligned.d_TC),(1.,0.,0.))
        for scale,resolved in ((.5e-12,False),(1e-12,True),(2e-12,True)):
            out = dg.historical_alignment([scale,0,0],[1,0,0],[2,0,0])
            self.discrete("P10",f"threshold branch {scale}",(out.macro_resolved,out.d_TM),(resolved,float(resolved)))
        self.falsifier("P10","unresolved is not exact zero",.5e-12 != 0 and not dg.historical_alignment([.5e-12,0,0],[1,0,0],[1,0,0]).macro_resolved)
        vectors = np.array([[1.,2.,3.],[-1.,4.,0.]])
        direct = dg.direct_history_coordinates({"Z_total":vectors})
        self.discrete("P10","direct display is detached",np.shares_memory(direct.x,vectors),False)
        self.discrete("P10","direct display values",tuple(zip(direct.x,direct.y,direct.z)),tuple(map(tuple,vectors)))
        self.discrete("P10","hand cylinder",tuple(dg.cylinder_point(2,0,3,N=12)),(2.,0.,3.))
        for history in ({"kappa":[1.],"phi_index":[1],"z":[.25]},
                        {"kappa":[1.,2.],"phi_index":[1,2],"z":[.25,2.]}):
            ref,scales = e.torus(history["kappa"],history["phi_index"],history["z"],12,2.,1.)
            result = dg.history_torus_coordinates(history)
            for i in range(len(ref)):
                self.bounded("P10",f"history torus length={len(ref)} point={i}",[result.x[i],result.y[i],result.z[i]],ref[i],scales[i],256)
            if len(ref) == 1:
                first = (result.x[0],result.y[0],result.z[0])
            else:
                self.falsifier("P10","extended history moves an old point",first != (result.x[0],result.y[0],result.z[0]))
        cfg = z.StagedConfig()
        one = z.observe_staged([1,1,1],z.Clock(),cfg)
        two = z.observe_staged([1,1j,1],z.Clock(),cfg)
        self.discrete("P10","distinct states share scalar display inputs",(z.state_norm([1,1,1]),one.z),(z.state_norm([1,1j,1]),two.z))
        self.falsifier("P10","scalar display loses chirality",tuple(one.Z_total) != tuple(two.Z_total))
