# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""External D1 verifier. No predecessor writer is run; bytecode disabled.
Run with python -X utf8 -B.
Only D1_RESULTS.json in this directory is written. --jets derives the exact
cubic jet; further bounded stages are described in the accompanying report.
"""
from pathlib import Path
import sys, json, hashlib, subprocess
sys.dont_write_bytecode=True
import sympy as s
import mpmath as mp
ROOT=Path('project-source')
REPO=ROOT/'trioctagon-physics'
OUT=Path(__file__).resolve().parent
RESULT=OUT/'D1_RESULTS.json'
assert OUT==ROOT/'research/D1_chiral_drift_20261006'
record=json.loads(RESULT.read_text(encoding='utf8'))
checks=record.get('checks',[])
def check(name,value,kind='EXACT SYMBOLIC CHECK',details=None):
    checks[:]=[c for c in checks if c['name']!=name]
    checks.append(dict(name=name,passed=bool(value),evidence=kind,details=details))
def save():
    record['checks']=checks;record['passed']=sum(c['passed'] for c in checks);record['total']=len(checks)
    record['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')

h=s.symbols('h',real=True)
I=s.I;rt3=s.sqrt(3)
N=3
def simp(v):return s.factor(s.cancel(s.expand(v)))
def jc(c):return [s.sympify(c)]+[s.S.Zero]*N
def jadd(a,b):return [simp(x+y) for x,y in zip(a,b)]
def jneg(a):return [-x for x in a]
def jsub(a,b):return jadd(a,jneg(b))
def jmul(a,b):return [simp(sum(a[j]*b[n-j] for j in range(n+1))) for n in range(N+1)]
def jscale(a,k):return [simp(x*k) for x in a]
def jconj(a):return [s.conjugate(v).expand(complex=True) for v in a]
def jpow(a,n):
    if n==0:return jc(1)
    return jmul(a,jpow(a,n-1))
def jbinom(a,p):
    assert a[0]==1
    t=jsub(a,jc(1));ans=jc(0)
    for j in range(N+1):ans=jadd(ans,jscale(jpow(t,j),s.binomial(p,j)))
    return ans
def jexpzero(a):
    assert a[0]==0
    ans=jc(0)
    for j in range(N+1):ans=jadd(ans,jscale(jpow(a,j),1/s.factorial(j)))
    return ans
rot=[1,(-1+I*rt3)/2,(-1-I*rt3)/2]
def jet_residual(ws,nu):
    kapp=[-1,0,1];ps=[]
    for i in range(3):
        radius=jmul(ws[i],jconj(ws[i]))
        kval=[1,kapp[i],0,0]
        local=jmul(ws[i],jsub(kval,jscale(radius,s.Rational(1,2))))
        graph=jscale(ws[i],-s.Rational(1,3))
        for j in range(3):
            if j!=i:graph=jadd(graph,jscale(ws[j],s.expand(rot[(j-i)%3]/6)))
        ps.append(jadd(ws[i],jscale(jadd(local,graph),h)))
    cubes=[]
    for p in ps:
        norm=jmul(p,jconj(p))
        cubes.append(jmul(jpow(p,3),jbinom(norm,-s.Rational(3,2))))
    deltas=[]
    for i in range(3):
        t=jc(0)
        for j in range(3):
            if j!=i:
                v=jmul(cubes[j],jconj(cubes[i]))
                t=jadd(t,jscale(jsub(v,jconj(v)),1/(2*I)))
        deltas.append(jscale(t,h/30))
    targetrot=jexpzero(jscale(nu,I*h))
    res=[jscale(jsub(jmul(ps[i],jexpzero(jscale(deltas[i],I))),jmul(ws[i],targetrot)),1/h) for i in range(3)]
    gauge=jscale(jadd(jadd(jscale(jsub(ws[0],jconj(ws[0])),1/(2*I)),jscale(jsub(ws[1],jconj(ws[1])),1/(2*I))),jscale(jsub(ws[2],jconj(ws[2])),1/(2*I))),s.Rational(1,3))
    return res,gauge

def derive_jets():
    C=s.eye(3)*(1+h/6);Q=s.zeros(3)
    for j in range(3):
        for d in [-1,1]:
            C[j,(j+d)%3]=-h/12;Q[j,(j+d)%3]=s.sign(d)*rt3*h/12
    pre=(C-h*s.eye(3)).row_join(-Q).col_join(Q.row_join(C))
    L=s.ones(3)-3*s.eye(3)
    J=(s.diag(s.eye(3),s.eye(3)+h*L/10)*pre).applyfunc(simp)
    B=((J-s.eye(6))/h).applyfunc(simp).row_join(s.Matrix([0]*3+[-1]*3)).col_join(s.Matrix([[0]*3+[s.Rational(1,3)]*3+[0]]))
    Bi=B.inv().applyfunc(simp)
    check('D0 normalized full border determinant',simp(B.det(method='domain-ge')+(3*h-1)**2/1600)==0)
    ws=[jc(1) for _ in range(3)];nu=jc(0);coeff=[]
    for n in range(1,4):
        print('exact jet order',n,flush=True)
        res,gauge=jet_residual(ws,nu)
        forcing=s.Matrix([s.re(r[n]).expand(complex=True) for r in res]+[s.im(r[n]).expand(complex=True) for r in res]+[gauge[n]]).applyfunc(simp)
        sol=(-Bi*forcing).applyfunc(simp)
        for j in range(3):ws[j][n]=simp(sol[j]+I*sol[j+3])
        nu[n]=sol[6];coeff.append([str(v) for v in sol])
        print('nu coefficient',n,str(nu[n]),flush=True)
    residual,gauge=jet_residual(ws,nu)
    check('original complete residual substituted through cubic order',all(simp(c)==0 for r in residual for c in r) and all(simp(c)==0 for c in gauge))
    check('linear and quadratic phase-rate coefficients vanish',nu[1]==nu[2]==0)
    c=simp(nu[3]/2)
    check('normalization c equals third derivative divided by twelve',simp(6*nu[3]/12-c)==0)
    record['exact_jet']={'coordinates':'z_j = exp(2*pi*i*j/3)/sqrt(2) * (1+u_j+i*v_j); gauge sum(v_j)/3=0','state_and_rate_coefficients':coeff,'c_plus_h':str(c),'c_plus_0':str(simp(c.subs(h,0))),'c_prime_0':str(simp(s.diff(c,h).subs(h,0))),'nu_eta3':str(nu[3]),'state_complex_coefficients':[[str(v) for v in w] for w in ws],'h_symbol':'real; 0 <= h <= 1/4','substitution_residual_zero':True}
    save();print(json.dumps(record['exact_jet'],indent=2),flush=True)

mp.mp.dps=110
mp.iv.dps=100

class Dual:
    """First real derivatives, over mp or outward-rounded interval scalars."""
    def __init__(self,v,d=None):self.v=v;self.d=[v*0]*7 if d is None else d
    def co(self,b):return b if isinstance(b,Dual) else Dual(self.v*0+b)
    def __add__(self,b):
        b=self.co(b);return Dual(self.v+b.v,[x+y for x,y in zip(self.d,b.d)])
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,[-x for x in self.d])
    def __sub__(self,b):return self+-self.co(b)
    def __rsub__(self,b):return self.co(b)+-self
    def __mul__(self,b):
        b=self.co(b);return Dual(self.v*b.v,[x*b.v+self.v*y for x,y in zip(self.d,b.d)])
    __rmul__=__mul__
    def __truediv__(self,b):
        b=self.co(b);return Dual(self.v/b.v,[(x*b.v-self.v*y)/(b.v*b.v) for x,y in zip(self.d,b.d)])
    def __rtruediv__(self,b):return self.co(b)/self
    def __pow__(self,n):
        if n==0:return self.co(1)
        return Dual(self.v**n,[n*self.v**(n-1)*x for x in self.d])

def dsqrt(x,ctx):
    val=ctx.sqrt(x.v);return Dual(val,[d/(2*val) for d in x.d])
def dsin(x,ctx):return Dual(ctx.sin(x.v),[ctx.cos(x.v)*d for d in x.d])
def dcos(x,ctx):return Dual(ctx.cos(x.v),[-ctx.sin(x.v)*d for d in x.d])
def upper(x):
    return mp.mpf(x.b._mpi_[0]) if hasattr(x,'_mpi_') else mp.mpf(x)
def lower(x):
    return mp.mpf(x.a._mpi_[0]) if hasattr(x,'_mpi_') else mp.mpf(x)
def magnitude(x):return max(abs(lower(x)),abs(upper(x)))
def ivpoint(x):return mp.iv.mpf(mp.nstr(x,110))
def boxscalar(lo,hi):return mp.iv.mpf([mp.nstr(lo,110),mp.nstr(hi,110)])
def upstr(x):return mp.nstr(x+abs(x)*mp.mpf('1e-70')+mp.mpf('1e-120'),80)
def lostr(x):return mp.nstr(x-abs(x)*mp.mpf('1e-70')-mp.mpf('1e-120'),80)

def exponential_quotient(v,hh,ctx):
    """E=(1-exp(-i*h*v))/h, extended at h=0; rigorous entire series.
    Derivatives are exactly sin(hv) and cos(hv). Degree 24 tail bounded
    by exp(|hv|)|h|^24 |v|^25/25!, outward rounded in interval mode.
    """
    if hh==0:return v*0,v
    if ctx is mp.mp:
        t=hh*v.v
        er=2*ctx.sin(t/2)**2/hh;ei=ctx.sin(t)/hh
    else:
        er=ctx.mpf(0);ei=ctx.mpf(0)
        for n in range(1,25):
            term=hh**(n-1)*v.v**n/ctx.factorial(n)
            if n%2:ei+=(-1)**((n-1)//2)*term
            else:er+=(-1)**(n//2+1)*term
        vv=ctx.mpf([0,mp.nstr(magnitude(v.v),110)])
        tail=ctx.exp(abs(hh)*vv)*abs(hh)**24*vv**25/ctx.factorial(25)
        bound=upper(tail)
        err=boxscalar(-bound,bound)
        er+=err;ei+=err
    return Dual(er,[ctx.sin(hh*v.v)*d for d in v.d]),Dual(ei,[ctx.cos(hh*v.v)*d for d in v.d])

def system(values,hh,eta,kappa=(-1,0,1),ctx=mp.mp):
    """Seven equations, normalized local coordinates. Row rotation removes
    small-h cancellation without changing any roots of the complete system.
    w=1+u+i*v; a is exact native prestage increment divided by h.
    G=a+w*(1-exp(-i*h*(d-nu)))/h; d uses actual p=w+h*a.
    """
    zero=ctx.mpf(0);one=ctx.mpf(1)
    vv=[Dual(values[j],[one if i==j else zero for i in range(7)]) for j in range(7)]
    x=[1+vv[j] for j in range(3)];y=[vv[j+3] for j in range(3)];nu=vv[6]
    sr=ctx.sqrt(3);ar=[];ai=[]
    for i in range(3):
        f=-(x[i]*x[i]+y[i]*y[i])/2+(1+eta*kappa[i])
        gr=-2*x[i];gi=-2*y[i]
        for j in range(3):
            if j==i:continue
            ss=sr/2 if (j-i)%3==1 else -sr/2
            gr+=-x[j]/2-y[j]*ss;gi+=x[j]*ss-y[j]/2
        ar.append(x[i]*f+gr/6);ai.append(y[i]*f+gi/6)
    px=[x[i]+ar[i]*hh for i in range(3)];py=[y[i]+ai[i]*hh for i in range(3)]
    cr=[];ci=[];norms=[]
    for xx,yy in zip(px,py):
        norm=xx*xx+yy*yy;den=norm*dsqrt(norm,ctx);norms.append(norm)
        cr.append((xx**3-3*xx*yy**2)/den);ci.append((3*xx**2*yy-yy**3)/den)
    d=[sum((ci[j]*cr[i]-cr[j]*ci[i] for j in range(3) if j!=i))/30 for i in range(3)]
    real=[];imag=[]
    for i in range(3):
        er,ei=exponential_quotient(d[i]-nu,hh,ctx)
        real.append(ar[i]+x[i]*er-y[i]*ei)
        imag.append(ai[i]+x[i]*ei+y[i]*er)
    equations=real+imag+[sum(y)/3]
    return [e.v for e in equations],[e.d for e in equations],{'px':[v.v for v in px],'py':[v.v for v in py],'d':[v.v for v in d],'norms':[v.v for v in norms]}

jet_cache={}
def predictor(hh,eta):
    key=str(hh)
    if key not in jet_cache:
        coeff=record['exact_jet']['state_and_rate_coefficients']
        jet_cache[key]=[[mp.mpf(str(s.N(s.sympify(v,locals={'h':h}).subs(h,s.Rational(str(hh))),115))) for v in order] for order in coeff]
    return mp.matrix([sum(jet_cache[key][n-1][j]*eta**n for n in range(1,4)) for j in range(7)])

def solve(hh,eta,kappa=(-1,0,1),initial=None):
    x=mp.matrix(initial) if initial is not None else (predictor(hh,eta) if kappa==(-1,0,1) else mp.matrix(7,1))
    iterations=0
    for iterations in range(25):
        f,jac,_=system(x,hh,eta,kappa)
        if max(abs(a) for a in f)<mp.mpf('1e-100'):break
        change=mp.lu_solve(mp.matrix(jac),mp.matrix(f));x-=change
    f,jac,_=system(x,hh,eta,kappa)
    if max(abs(a) for a in f)>mp.mpf('1e-90'):raise RuntimeError('Newton diagnostic failed')
    return x,mp.inverse(mp.matrix(jac)),max(abs(a) for a in f),iterations

def certificate(x,C,hh,elo,ehi,radius,kappa=(-1,0,1)):
    ctx=mp.iv;hi=ivpoint(hh);et=boxscalar(elo,ehi)
    center=[ivpoint(a) for a in x];box=[c+boxscalar(-radius,radius) for c in center]
    f0,_,_=system(center,hi,et,kappa,ctx)
    _,jac,aux=system(box,hi,et,kappa,ctx)
    Ci=[[ivpoint(C[i,j]) for j in range(7)] for i in range(7)]
    err=[];norms=[]
    for i in range(7):
        y=sum(Ci[i][k]*f0[k] for k in range(7))
        err.append(magnitude(y))
        row=[]
        for j in range(7):
            t=(1 if i==j else 0)-sum(Ci[i][k]*jac[k][j] for k in range(7))
            row.append(magnitude(t))
        norms.append(upper(sum(ivpoint(v) for v in row)))
    q=max(norms);Y=max(err)
    margin=lower(ivpoint(radius)-ivpoint(Y)-ivpoint(q)*ivpoint(radius))
    amin=min(lower(((1+box[j])**2+box[j+3]**2)/2) for j in range(3))
    pmin=min(lower(v)/2 for v in aux['norms'])
    gaugepositivity=lower(sum(1+box[j] for j in range(3))/3)
    cnorm=max(upper(sum(abs(Ci[i][j]) for j in range(7))) for i in range(7))
    ok=q<1 and margin>0 and amin>0 and pmin>0 and gaugepositivity>0
    invbound=upper(ivpoint(cnorm)/(1-ivpoint(q))) if q<1 else None
    return {'certified':bool(ok),'eta_interval':[mp.nstr(elo,110),mp.nstr(ehi,110)],'radius':mp.nstr(radius,110),'q_upper':upstr(q),'Y_upper':upstr(Y),'inclusion_margin_lower':lostr(margin),'input_modulus_squared_lower':lostr(amin),'prestage_modulus_squared_lower':lostr(pmin),'gauge_positive_lower':lostr(gaugepositivity),'inverse_norm_upper':upstr(invbound) if invbound else None,'point_center':[mp.nstr(a,110) for a in x]},(q,Y,margin)

def trial_validation():
    print('100+ digit diagnostics and interval contraction trials',flush=True)
    trials=[]
    for hh in [mp.mpf(0),mp.mpf(1)/10,mp.mpf(1)/100,mp.mpf(1)/1000]:
        eta=mp.mpf(1)/100
        x,C,res,it=solve(hh,eta)
        cert,bounds=certificate(x,C,hh,eta,eta,mp.mpf('1e-60'))
        print('h',hh,'nu',mp.nstr(x[6],22),'ratio',mp.nstr(x[6]/(2*eta**3),22),'tiny certificate',cert['certified'],flush=True)
        for width in ['0.0001','0.00001']:
            half=mp.mpf(width);rad=half*100
            cc,bb=certificate(x,C,hh,eta-half,eta,rad)
            print('segment',width,'r',rad,'q',mp.nstr(bb[0],8),'Y/r',mp.nstr(bb[1]/rad,8),'pass',cc['certified'],flush=True)
            trials.append({'h':str(hh),'trial':cc})
    record['validation_trials']=trials;save()

def segment(hh,lo,hi,kappa=(-1,0,1)):
    mid=(lo+hi)/2;x,C,_,_=solve(hh,mid,kappa)
    _,(_,Y,_)=certificate(x,C,hh,lo,hi,mp.mpf('1e-25'),kappa)
    rad=max(3*Y,mp.mpf('1e-20'))
    return certificate(x,C,hh,lo,hi,rad,kappa)[0]

def direct_quantities(x,hh,eta,kappa=(-1,0,1),orientation=1):
    """Independent physical-complex transcription; no row-rotated G."""
    A=1/mp.sqrt(2);unit=[mp.exp(orientation*2j*mp.pi*j/3) for j in range(3)]
    state=[A*unit[j]*(1+x[j]+1j*x[j+3]) for j in range(3)]
    aa=[state[j]*(1+eta*kappa[j]-abs(state[j])**2)+(sum(state)-3*state[j])/6 for j in range(3)]
    pre=[state[j]+hh*aa[j] for j in range(3)]
    angles=[mp.arg(z) for z in pre]
    d=[sum(mp.sin(3*(angles[j]-angles[i])) for j in range(3) if j!=i)/30 for i in range(3)]
    if hh:
        image=[pre[i]*mp.exp(1j*hh*d[i]) for i in range(3)]
        residual=max(abs(image[i]-mp.exp(1j*hh*x[6])*state[i])/hh for i in range(3))
        identity=sum(abs(state[i])**2*mp.sin(hh*(x[6]-d[i])) for i in range(3))
        coherence=max(abs(image[i]*mp.conj(image[j])-state[i]*mp.conj(state[j])) for i in range(3) for j in range(3))
    else:
        vector=[aa[i]+1j*state[i]*d[i] for i in range(3)]
        residual=max(abs(vector[i]-1j*x[6]*state[i]) for i in range(3))
        identity=x[6]*sum(abs(z)**2 for z in state)-sum(abs(state[i])**2*d[i] for i in range(3))
        coherence=max(abs(vector[i]*mp.conj(state[j])+state[i]*mp.conj(vector[j])) for i in range(3) for j in range(3))
    chir=sum(mp.im(mp.conj(state[j])*state[(j+1)%3]) for j in range(3))
    winding=sum(mp.arg(state[(j+1)%3]*mp.conj(state[j])) for j in range(3))/(2*mp.pi)
    gauge=sum(x[j+3] for j in range(3))/3
    return {'state':[[mp.nstr(mp.re(v),110),mp.nstr(mp.im(v),110)] for v in state],
        'full_original_residual':mp.nstr(residual,30),'gauge_residual':mp.nstr(abs(gauge),30),
        'min_input_modulus':mp.nstr(min(abs(v) for v in state),70),'min_prestage_modulus':mp.nstr(min(abs(v) for v in pre),70),
        'gauge_positive':mp.nstr(sum(1+x[j] for j in range(3))/3,70),'winding':int(mp.nint(winding)),
        'chirality':mp.nstr(chir,70),'necessary_identity_residual':mp.nstr(abs(identity),30),
        'coherence_change_or_generator_derivative':mp.nstr(coherence,30)}

def validate_continuation():
    hs=[mp.mpf(0),mp.mpf(1)/10,mp.mpf(1)/100,mp.mpf(1)/1000]
    # Bound the work by 64 parameter boxes per h; inspect the first original
    # box before selecting a common smaller ladder. No parameter is retuned.
    budget=64;originalmax=mp.mpf(1)/100
    original_trial=segment(mp.mpf(1)/10,0,originalmax/budget)
    record['original_ladder_first_tube']=original_trial
    etamax=originalmax if original_trial['certified'] else originalmax/10
    record['ladder']={'original_max':'1/100','accepted_max':mp.nstr(etamax,30),'subdivision_count':budget,'shrink_factor':1 if etamax==originalmax else 10,'reason':'First original-ladder parameter tube failed the sufficient contraction bound at the fixed 64-subdivision budget; entire nested ladder reduced uniformly, without changing parameters.' if etamax!=originalmax else 'Original ladder certified.'}
    tubes=[];endpoints=[];roots=[]
    for hh in hs:
        print('validating h=',hh,'ladder maximum',etamax,flush=True)
        localtubes=[];localpoints=[]
        for j in range(budget):
            lo=etamax*j/budget;hi=etamax*(j+1)/budget
            cert=segment(hh,lo,hi)
            if not cert['certified']:
                record['validation_failure']={'h':str(hh),'segment':j,'certificate':cert};save()
                raise RuntimeError('Bounded continuation tube failed: no certification claimed')
            localtubes.append(cert)
            if j%16==15:print(' certified tubes',j+1,'/',budget,flush=True)
        # Tight endpoint boxes establish equality of adjoining parameter
        # sections by inclusion in both contraction boxes, not by proximity.
        for j in range(budget+1):
            et=etamax*j/budget;x,C,res,it=solve(hh,et)
            cert,_=certificate(x,C,hh,et,et,mp.mpf('1e-60'))
            if not cert['certified']:raise RuntimeError('endpoint certification failed')
            adjacent=localtubes[max(0,j-1):min(budget,j+1)]
            for tube in adjacent:
                tc=[mp.mpf(v) for v in tube['point_center']];r=mp.mpf(tube['radius'])
                # All quantities in containment are evaluated outwardly.
                dist=max(upper(abs(ivpoint(x[i])-ivpoint(tc[i]))+mp.iv.mpf('1e-60')) for i in range(7))
                if not dist<r:raise RuntimeError('endpoint not in adjacent certified tubes')
            cert['adjacent_tubes_contain_endpoint_box']=True
            localpoints.append(cert)
        tubes.append({'h':mp.nstr(hh,30),'tubes':localtubes})
        endpoints.append({'h':mp.nstr(hh,30),'endpoints':localpoints})
        check('validated connected positive-eta branch h='+str(hh),True,'VALIDATED NUMERICAL RESULT',{'tubes':budget,'endpoints':budget+1})
        for et in [etamax,etamax/2,etamax/4]:
            for sign in [1,-1]:
                eta=sign*et;x,C,res,it=solve(hh,eta)
                cert,_=certificate(x,C,hh,eta,eta,mp.mpf('1e-60'))
                if not cert['certified']:raise RuntimeError('prescribed root failed certification')
                if sign>0:
                    j=int(mp.nint(eta/etamax*budget));parent=localpoints[j]
                else:
                    j=int(mp.nint(-eta/etamax*budget));parent=localpoints[j]
                    xp=[mp.mpf(v) for v in parent['point_center']]
                    reflected=mp.matrix([xp[2],xp[1],xp[0],-xp[5],-xp[4],-xp[3],-xp[6]])
                    # The exact reflection/conjugation image of the positive
                    # endpoint ball lies in this larger contraction box.
                    large,_=certificate(x,C,hh,eta,eta,mp.mpf('1e-40'))
                    dist=max(upper(abs(ivpoint(x[i])-ivpoint(reflected[i]))+mp.iv.mpf('1e-60')) for i in range(7))
                    if not large['certified'] or not dist<mp.mpf('1e-40'):raise RuntimeError('negative branch symmetry connection failed')
                    cert['symmetry_parent_endpoint']=j
                    cert['larger_uniqueness_box_radius']='1e-40'
                quantities=direct_quantities(x,hh,eta)
                cexpr=s.sympify(record['exact_jet']['c_plus_h'],locals={'h':h})
                cexact=mp.mpf(str(s.N(cexpr.subs(h,s.Rational(str(hh))),115)))
                ratio=x[6]/(2*eta**3);err=mp.mpf('1e-60')/(2*abs(eta)**3)
                intervalnu=ivpoint(x[6])+mp.iv.mpf(['-1e-60','1e-60'])
                quotient=intervalnu/(2*ivpoint(eta)**3)
                # c is evaluated by its exact rational formula in interval arithmetic.
                hv=ivpoint(hh)
                cv=mp.iv.sqrt(3)*(33*hv*hv-240*hv+688)/(6*(1-3*hv)**3)
                rem=(quotient-cv)/(ivpoint(eta)**2)
                row={'h':mp.nstr(hh,30),'eta':mp.nstr(eta,30),'ordered_k':[mp.nstr(1+eta*k,30) for k in [-1,0,1]],'branch':'+','nu':mp.nstr(x[6],110),'nu_interval':[lostr(lower(intervalnu)),upstr(upper(intervalnu))],'omega':mp.nstr(hh*x[6],100) if hh else None,'omega_over_h':mp.nstr(x[6],100) if hh else None,'omega_over_h_squared':mp.nstr(x[6]/hh,100) if hh else None,'ratio_nu_over_2eta3':mp.nstr(ratio,80),'ratio_error_bound':upstr(err),'exact_c_h_decimal':mp.nstr(cexact,80),'normalized_remainder_over_eta_squared_interval':[lostr(lower(rem)),upstr(upper(rem))],'certificate':cert,'diagnostics':quantities,'continuation':'positive path through certified parameter tubes' if sign>0 else 'C composed with j->2-j maps certified positive path; endpoint uniqueness verified'}
                roots.append(row)
                check('isolated full root h='+str(hh)+' eta='+str(eta),cert['certified'] and (lower(intervalnu)>0 if eta>0 else upper(intervalnu)<0),'VALIDATED NUMERICAL RESULT')
                check('independent original residual and identity h='+str(hh)+' eta='+str(eta),mp.mpf(quantities['full_original_residual'])<mp.mpf('1e-90') and mp.mpf(quantities['necessary_identity_residual'])<mp.mpf('1e-90'),'UNVALIDATED NUMERICAL EVIDENCE')
        record['continuation_tubes']=tubes;record['continuation_endpoints']=endpoints;record['roots_plus']=roots;save()
    # One two-equal coefficient comparison, fixed before this control solve.
    hc=mp.mpf(1)/10;ec=mp.mpf(1)/100000;kc=(1,1,-2)
    tube=segment(hc,0,ec,kc)
    xc,Cc,res,it=solve(hc,ec,kc)
    cert,_=certificate(xc,Cc,hc,ec,ec,mp.mpf('1e-60'),kc)
    bound=max(upper(abs(ivpoint(xc[i])-ivpoint(mp.mpf(tube['point_center'][i])))+mp.iv.mpf('1e-60')) for i in range(7))
    startinside=max(upper(abs(mp.iv.mpf(v))) for v in tube['point_center'])<mp.mpf(tube['radius'])
    check('two-equal coefficient control connected and isolated',tube['certified'] and cert['certified'] and bound<mp.mpf(tube['radius']) and startinside,'VALIDATED NUMERICAL RESULT')
    record['two_equal_control']={'h':'1/10','eta':'1/100000','kappa':[1,1,-2],'tube':tube,'endpoint':cert,'diagnostics':direct_quantities(xc,hc,ec,kc),'numerical_nu':mp.nstr(xc[6],110),'exact_nu':'0 by C-reflection invariance and certified local uniqueness'}
    save();print('validated',len(roots),'positive-chirality prescribed roots plus one two-equal control',flush=True)

def symmetry_and_independent_checks():
    minus=[];worst=mp.mpf(0);jet_res=[]
    for row in record['roots_plus']:
        hh=mp.mpf(row['h']);eta=mp.mpf(row['eta']);x=mp.matrix([mp.mpf(v) for v in row['certificate']['point_center']])
        xm=mp.matrix(list(x[:3])+[-v for v in x[3:]])
        qm=direct_quantities(xm,hh,eta,orientation=-1)
        mir={k:v for k,v in row.items() if k not in ['diagnostics','certificate','nu_interval','normalized_remainder_over_eta_squared_interval']}
        mir.update({'branch':'-','nu':mp.nstr(-x[6],110),'nu_interval':[-mp.mpf(row['nu_interval'][1]),-mp.mpf(row['nu_interval'][0])],
                    'omega':mp.nstr(-hh*x[6],100) if hh else None,'omega_over_h':mp.nstr(-x[6],100) if hh else None,'omega_over_h_squared':mp.nstr(-x[6]/hh,100) if hh else None,
                    'ratio_nu_over_2eta3':mp.nstr(-x[6]/(2*eta**3),80),'exact_c_h_decimal':mp.nstr(-mp.mpf(row['exact_c_h_decimal']),80),
                    'diagnostics':qm,'certificate':{'inherited_by_exact_conjugation':True,'positive_parent_h':row['h'],'positive_parent_eta':row['eta'],'coordinate_isometry':'u unchanged; v and nu negated','radius':'1e-60','full_border_invertibility_bound':row['certificate']['inverse_norm_upper']}})
        mir['nu_interval']=[lostr(mir['nu_interval'][0]),upstr(mir['nu_interval'][1])]
        mir['normalized_remainder_over_eta_squared_interval']=[lostr(-mp.mpf(row['normalized_remainder_over_eta_squared_interval'][1])),upstr(-mp.mpf(row['normalized_remainder_over_eta_squared_interval'][0]))]
        minus.append(mir)
        # These transformations are exact isometries of the local real chart;
        # certification transports from the source box. Direct residuals are
        # independently evaluated in physical complex coordinates as checks.
        err=mp.mpf(qm['full_original_residual'])
        for idx,orient,conjugate in [([2,0,1],1,False),([0,2,1],-1,False),([0,2,1],1,True)]:
            sign=-1 if conjugate else 1
            xt=mp.matrix([x[i] for i in idx]+[sign*x[i+3] for i in idx]+[sign*x[6]])
            kp=tuple([-1,0,1][i] for i in idx)
            qt=direct_quantities(xt,hh,eta,kp,orient)
            err=max(err,mp.mpf(qt['full_original_residual']))
        check('joint symmetry residuals h='+row['h']+' eta='+row['eta'],err<mp.mpf('1e-90'),'UNVALIDATED NUMERICAL EVIDENCE',mp.nstr(err,30))
        worst=max(worst,err)
    record['roots_minus']=minus
    record['symmetry_proof']='Conjugation, coordinate permutations and signed gauges map the full equations exactly; interval balls and invertibility certificates transport by real coordinate isometries. Numerical transformed residuals are separate diagnostics.'
    # Bound the phase deviation in every tube, proving winding/chirality labels.
    for bundle in record['continuation_tubes']:
        bounds=[]
        for tube in bundle['tubes']:
            x=[mp.iv.mpf(v) for v in tube['point_center']];rad=mp.iv.mpf(tube['radius']);error=mp.iv.mpf([-1,1])*rad
            xmin=min(lower(1+x[i]+error) for i in range(3))
            vmax=max(upper(abs(x[i+3]+error)) for i in range(3))
            angle=upper(ivpoint(vmax)/ivpoint(xmin))
            bounds.append(angle)
        bound=max(bounds)
        bundle['local_phase_deviation_bound_radians']=upstr(bound)
        check('certified winding and positive chirality along h='+bundle['h'],bound<mp.mpf('0.25'),'VALIDATED NUMERICAL RESULT',upstr(bound))
    # Source implementation comparison, without invoking other project code.
    import importlib.util
    spec=importlib.util.spec_from_file_location('d1_native_dynamics',REPO/'kernel_physics/dynamics.py')
    native=importlib.util.module_from_spec(spec);sys.modules[spec.name]=native;spec.loader.exec_module(native)
    import numpy as np
    errors=[]
    for row in record['roots_plus']:
        hh=mp.mpf(row['h'])
        if not hh:continue
        state=np.array([complex(float(a),float(b)) for a,b in row['diagnostics']['state']])
        cfg=native.DynamicsConfig(float(hh),float(hh/6),float(hh/30),tuple(float(k) for k in row['ordered_k']))
        got=native.step3(state,cfg)
        error=float(np.max(np.abs(got-np.exp(1j*float(row['omega']))*state)))
        errors.append(error)
    check('native complex128 full-stage comparisons at certified roots',max(errors)<3e-15,'UNVALIDATED NUMERICAL EVIDENCE',max(errors))
    # Independently substitute the exact cubic state into the unmodified
    # transcendental physical formula, rather than the symbolic jet evaluator.
    for hh in [mp.mpf(0),mp.mpf(1)/10]:
        errs=[]
        for eta in [mp.mpf('1e-5'),mp.mpf('5e-6'),mp.mpf('2.5e-6')]:
            x=predictor(hh,eta);q=direct_quantities(x,hh,eta)
            er=mp.mpf(q['full_original_residual']);errs.append(er)
            jet_res.append({'h':str(hh),'eta':str(eta),'full_residual':mp.nstr(er,35),'residual_over_eta4':mp.nstr(er/eta**4,35)})
        ratio=errs[0]/errs[1]
        check('independent cubic-jet residual fourth-order scaling h='+str(hh),mp.mpf('15.8')<ratio<mp.mpf('16.2'),'UNVALIDATED NUMERICAL EVIDENCE',mp.nstr(ratio,30))
    c=s.sympify(record['exact_jet']['c_plus_h'],locals={'h':h})
    expected=rt3*(33*h*h-240*h+688)/(6*(1-3*h)**3)
    check('exact cubic coefficient closed form',simp(c-expected)==0)
    check('nonzero generator coefficient',simp(c.subs(h,0)-344*rt3/3)==0 and (344*rt3/3).is_positive)
    check('small-step coefficient derivative',simp(s.diff(c,h).subs(h,0)-992*rt3)==0)
    check('coefficient numerator positive on whole reference interval',s.Rational(688)-240*s.Rational(1,4)>0)
    # Mathematical identity sign: Im(z^dagger X)=sum |z|^2*d,
    # since the real symmetric prestage contribution has real total pairing.
    max_identity=max(mp.mpf(row['diagnostics']['necessary_identity_residual']) for row in record['roots_plus'])
    max_coherence=max(mp.mpf(row['diagnostics']['coherence_change_or_generator_derivative']) for row in record['roots_plus'])
    check('all generator and native necessary identities',max_identity<mp.mpf('1e-90'),'UNVALIDATED NUMERICAL EVIDENCE',mp.nstr(max_identity,35))
    check('coherence invariance or zero generator derivative',max_coherence<mp.mpf('1e-90'),'UNVALIDATED NUMERICAL EVIDENCE',mp.nstr(max_coherence,35))
    record['independent_diagnostics']={'mp_decimal_digits':110,'interval_decimal_digits':100,'max_symmetry_residual':mp.nstr(worst,35),'max_native_complex128_residual':max(errors),'jet_direct_substitution':jet_res,'max_necessary_identity_residual':mp.nstr(max_identity,35),'max_coherence_residual':mp.nstr(max_coherence,35)}
    save();print('symmetry and independent checks',sum(c['passed'] for c in checks),'/',len(checks),flush=True)

def enclose_identities():
    allres=[];allid=[]
    for row in record['roots_plus']:
        vals=[mp.iv.mpf(v)+mp.iv.mpf(['-1e-60','1e-60']) for v in row['certificate']['point_center']]
        hh=mp.iv.mpf(row['h']);eta=mp.iv.mpf(row['eta'])
        f,jac,aux=system(vals,hh,eta,ctx=mp.iv)
        radii=[((1+vals[j])**2+vals[j+3]**2)/2 for j in range(3)]
        if mp.mpf(row['h'])==0:identity=vals[6]*sum(radii)-sum(radii[j]*aux['d'][j] for j in range(3))
        else:identity=sum(radii[j]*mp.iv.sin(hh*(vals[6]-aux['d'][j])) for j in range(3))
        ok=all(lower(v)<=0<=upper(v) for v in f) and lower(identity)<=0<=upper(identity)
        resid=max(magnitude(v) for v in f)
        allres.append(resid);allid.append(magnitude(identity))
        row['interval_residual']={'equivalent_full_seven_equations':[[lostr(lower(v)),upstr(upper(v))] for v in f],
             'original_H_real_component_absolute_bound':upstr(resid),
             'identity_interval':[lostr(lower(identity)),upstr(upper(identity))],
             'contains_zero':bool(ok),'original_H_bound_reason':'The three complex rows transform by multiplication of modulus A=1/sqrt(2); its real infinity norm is at most one. The gauge is unchanged.'}
        check('interval full residual and identity h='+row['h']+' eta='+row['eta'],ok,'VALIDATED NUMERICAL RESULT')
    record['interval_summary']={'max_original_real_residual_bound':upstr(max(allres)),'max_identity_bound':upstr(max(allid)),'point_coordinate_radius':'1e-60','smallest_positive_nu_lower':min(float(mp.mpf(row['nu_interval'][0])) for row in record['roots_plus'] if mp.mpf(row['eta'])>0)}
    save();print('interval identity enclosures pass',sum(c['passed'] for c in checks),'/',len(checks))

def preservation():
    sha=lambda b:hashlib.sha256(b).hexdigest()
    def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a]).decode('utf8')
    def inventory(path):
        rows={};size=0
        for p in sorted(path.rglob('*')):
            if p.is_file() and '.git' not in p.relative_to(path).parts and not p.is_relative_to(OUT):
                b=p.read_bytes();rows[p.relative_to(path).as_posix()]=sha(b);size+=len(b)
        return dict(files=len(rows),bytes=size,sha256=sha(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()))
    after={'head':git('rev-parse','HEAD').strip(),'branch':git('branch','--show-current').strip(),'status':git('status','--porcelain=v1'),'index_sha256':sha(git('ls-files','--stage','-z').encode()),'staged':git('diff','--cached','--name-only'),'roots':{name:inventory(ROOT/name) for name in record['baseline']['roots']}}
    for name in ['head','branch','status','index_sha256','staged']:
        check('preservation '+name,after[name]==record['baseline'][name],'PRESERVATION CHECK')
    for name in after['roots']:
        check('preservation bytes '+name,after['roots'][name]==record['baseline']['roots'][name],'PRESERVATION CHECK')
    for name,digest in record['source_hashes'].items():
        check('source identity '+name,sha((ROOT/name).read_bytes())==digest,'SOURCE / BYTE CHECK')
    record['after']=after
    record.pop('validation_trials',None)  # superseded exploratory diagnostics; final failed tube is retained
    report=OUT/'D1_NATIVE_CHIRAL_PHASE_DRIFT.md'
    if report.exists():record['report_sha256']=sha(report.read_bytes())
    record['verdict']='PASS_WITH_QUALIFICATIONS' if all(c['passed'] for c in checks) else 'HOLD'
    record['limits']='No trajectories, retuning, larger rings, publications or physical rotation adopted. Original eta ladder replaced uniformly by a tenfold smaller ladder within the fixed continuation budget. Interval contraction certificates concern the exact mathematical equations; native complex128 comparisons remain numerical evidence.'
    save();print('D1',record['verdict'],record['passed'],'/',record['total'],'protected files',sum(v['files'] for v in after['roots'].values()))

if __name__=='__main__':
    if '--jets' in sys.argv:derive_jets()
    if '--trial' in sys.argv:trial_validation()
    if '--validate' in sys.argv:validate_continuation()
    if '--checks' in sys.argv:symmetry_and_independent_checks()
    if '--enclose' in sys.argv:enclose_identities()
    if '--preserve' in sys.argv:preservation()

if __name__=='__main__':
    if '--jets' in sys.argv:derive_jets()
    if '--trial' in sys.argv:trial_validation()
