"""Bounded independent checks of displayed manuscript identities; no native writes.

Each named predicate is one check, including matrix identities. This is not a
theorem count. Retained checkpoint checks are verified separately, not rerun.
"""
from pathlib import Path
import sys,json,hashlib,re,platform,time
sys.dont_write_bytecode=True
import sympy as s
LANE=Path(__file__).resolve().parents[1]
REPO=LANE.parents[1]
checks=[]
def check(name,value):
    ok=bool(value);checks.append({'name':name,'passed':ok})
    if not ok:raise AssertionError(name)
def zero(v):
    if isinstance(v,s.MatrixBase):return all(s.cancel(x)==0 for x in v)
    return s.cancel(v)==0
def eq(name,v):check(name,zero(v))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
    a,b,c,g,l,z,xi=s.symbols('a b c g ell z xi',nonzero=True)
    r=s.Matrix([a,b,c]);R=s.diag(*r);e=s.ones(3,1);I=s.eye(3)
    sig=sum(r);h=sig*sum(1/x for x in r)-3;t=sig*(r.dot(r))/(a*b*c);d=1-3*l
    V=(a-b)*(a-c)*(b-c)
    D=s.Matrix([[-2,1,1/z],[1,-2,1],[z,1,-2]])
    H=I-g*s.diag(*[(sig-3*x)/x for x in r])+g*D
    P=R.inv()*H*R;J=(I+l*D)*P
    P0=P.subs(z,1);J0=J.subs(z,1)
    eq('positive-branch row sum',P0*e-e)
    eq('pre-stage exact diagonal balance',R**2*P0-P0.T*R**2)
    f=s.Matrix(s.symbols('f0:3'))
    eq('weighted Dirichlet form', (f.T*R**2*(I-P0)*f)[0]-g*sum(r[i]*r[j]*(f[i]-f[j])**2 for i in range(3) for j in range(i+1,3)))
    K=g*g*l*sig**3+(g*g*(1-2*l)-g*l)*sig*(a*b+a*c+b*c)+(3*g*l-g+l)*a*b*c
    cyc=J0[0,1]*J0[1,2]*J0[2,0]-J0[1,0]*J0[2,1]*J0[0,2]
    eq('triad full cycle factorization with GR1 plus sign',cyc-g*l*d*V*K/(a*b*c)**2)
    TB=3-6*l-d*g*h;GB=l*g*(l*(1+3*g)-g)*V/(a*b*c)
    CB=l*g*(l*g*t-(g+l-l*g)*h/2);w=z+1/z-2
    BB=d*(2-g*h)+d*d*(1-g*h+g*g*t)+CB*w-GB*(z-1/z)/2
    DB=(d*d+l**3*w)*(1-g*h+g*g*t+g**3*w)
    eq('Bloch trace',s.trace(J)-TB)
    eq('Bloch middle coefficient',(s.trace(J)**2-s.trace(J*J))/2-BB)
    eq('Bloch synchronizer determinant',(I+l*D).det()-(d*d+l**3*w))
    eq('Bloch pre-response determinant',H.det()-(1-g*h+g*g*t+g**3*w))
    eq('triad quotient factorization',xi**3-TB*xi**2+BB.subs(z,1)*xi-DB.subs(z,1)-(xi-1)*(xi**2-d*(2-g*h)*xi+d*d*(1-g*h+g*g*t)))
    eq('triad discriminant',d*d*(2-g*h)**2-4*d*d*(1-g*h+g*g*t)-d*d*g*g*(h*h-4*t))
    eta,v0,v1=s.symbols('eta v0 v1');vs=[v0,v1,-v0-v1]
    ratios={a:1+eta*vs[0],b:1+eta*vs[1],c:1+eta*vs[2]}
    eq('weak triad discriminant quadratic coefficient',s.diff((h*h-4*t).subs(ratios),eta,2).subs(eta,0)/2-6*sum(x*x for x in vs))
    for N in (6,12):
        rr=s.Matrix([s.Rational(9,10),1,s.Rational(11,10)]*(N//3));RN=s.diag(*rr)
        DN=-2*s.eye(N)
        for i in range(N):DN[i,(i-1)%N]=1;DN[i,(i+1)%N]=1
        gg=s.Rational(1,5);ll=s.Rational(3,1000)
        HN=s.eye(N)-gg*s.diag(*[(DN*rr)[i]/rr[i] for i in range(N)])+gg*DN
        JN=(s.eye(N)+ll*DN)*RN.inv()*HN*RN
        subs={a:rr[0],b:rr[1],c:rr[2],g:gg,l:ll}
        for zz in ([1,-1] if N==6 else [1,s.I,-1,-s.I]):
            inject=s.Matrix(N,3,lambda i,j:zz**(i//3) if i%3==j else 0)
            eq(f'exact Fourier injection N={N}, z={zz}',JN*inject-inject*J.subs(subs).subs(z,zz))
        eq(f'distance-one balance residual N={N}',(RN*JN-JN.T*RN)[0,1]-((a-b)*(l-g+3*g*l-g*l*sig*(1/a+1/b))).subs(subs))
    tau,delta=s.symbols('tau delta');fix={a:1-tau,b:1,c:1+tau,g:(1-tau*tau)/4,l:1,z:-1}
    nil=tau*tau/4*s.Matrix([1,-1,1])*s.Matrix([[1+tau,2,1-tau]])
    eq('generic six-ring nilpotent fixture',J.subs(fix)-nil)
    eq('fixture square zero',nil*nil)
    check('fixture rank one away from tau=0',nil.rank()==1)
    F={**fix,l:1+delta}
    ft=-3*delta/2;fb=-3*delta/16*(8*tau**4+delta*(10*tau**4+tau*tau-3));fd=delta**2*tau**4*(4*delta+3)*(9-tau*tau)/16
    for name,expr in [('trace',TB.subs(F)-ft),('middle',BB.subs(F)-fb),('determinant',DB.subs(F)-fd)]:eq('unfolding '+name,expr)
    disc=s.expand(ft*ft*fb*fb-4*fb**3-4*ft**3*fd-27*fd**2+18*ft*fb*fd)
    eq('unfolding cubic leading coefficient',disc.coeff(delta,3)-s.Rational(27,2)*tau**12)
    for sign in (-1,1):check(f'exact unfolding discriminant sign {sign}',s.sign(disc.subs({tau:s.Rational(1,1000),delta:sign*s.Rational(1,10**14)}))==sign)
    # Exact full D3h characters, independent of retained count records.
    C=s.Matrix([[0,0,1],[1,0,0],[0,1,0]]);Q=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    CG=s.Matrix([[-s.Rational(1,2),-s.sqrt(3)/2,0],[s.sqrt(3)/2,-s.Rational(1,2),0],[0,0,1]])
    VG=s.diag(-1,1,1);HG=s.diag(1,1,-1)
    counts={k:[0,0,0] for k in ['polar','axial','face_scalar','face_tangent','face_ambient','seam_vertical','rim_scalar','rim_vector']}
    for i in range(3):
      for j in range(2):
       for m in range(2):
        perm=C**i*Q**j;G=CG**i*VG**j*HG**m
        X=s.diag((-1)**j*perm,(-1)**m*perm)
        ch=[1,s.trace(X),(s.trace(X)**2+s.trace(X*X))/2]
        rim=s.eye(2) if m==0 else s.Matrix([[0,1],[1,0]])
        targets={'polar':G,'axial':G.det()*G,'face_scalar':perm,'face_tangent':X,'face_ambient':s.kronecker_product(perm,G),'seam_vertical':(-1)**m*perm,'rim_scalar':rim,'rim_vector':s.kronecker_product(rim,G)}
        for key,Y in targets.items():
          for deg in range(3):counts[key][deg]+=s.simplify(ch[deg]*s.trace(Y)/12)
    expected={'polar':[0,2,5],'axial':[0,2,3],'face_scalar':[1,1,8],'face_tangent':[0,4,8],'face_ambient':[1,5,16],'seam_vertical':[0,2,4],'rim_scalar':[1,1,5],'rim_vector':[1,3,12]}
    for key in expected:check('D3h multiplicities '+key,counts[key]==expected[key])
    NF=s.Matrix([[-s.sqrt(3)/2,0,s.sqrt(3)/2],[s.Rational(1,2),-1,s.Rational(1,2)],[0,0,0]])
    TF=s.Matrix([[-s.Rational(1,2),1,-s.Rational(1,2)],[-s.sqrt(3)/2,0,s.sqrt(3)/2],[0,0,0]])
    eq('exact fixed frame Gram identities',NF.T*NF-s.Rational(3,2)*(I-e*e.T/3))
    eq('tangent frame Gram identity',TF.T*TF-NF.T*NF)
    x,y,j,k=s.symbols('x y j k');u=s.Matrix([x,y,-x-y]);v=s.Matrix([j,k,-j-k]);aa,bb=s.symbols('meanq meanp')
    eq('chiral horizontal projection',TF*((aa*e+u).cross(bb*e+v))-s.sqrt(3)*(bb*NF*u-aa*NF*v))
    uv=s.matrix_multiply_elementwise(u,v);u2=s.matrix_multiply_elementwise(u,u)
    eq('transverse square kernel identity',(NF*u2).dot(NF*u2)-u.dot(u)**2/4)
    eq('transverse bilinear kernel identity',(NF*uv).dot(NF*uv)-u.dot(u)*v.dot(v)/4)
    eq('oriented area kernel identity',e.dot(u.cross(v))**2-3*(u.dot(u)*v.dot(v)-u.dot(v)**2))
    def pre(q,p):
        M=I+s.Rational(1,20)*s.diag(*[1-q[i]**2-p[i]**2 for i in range(3)])+s.Rational(1,5)*(s.ones(3)-3*I)
        return M*q,M*p
    def chir(q,p):
        q1,p1=pre(q,p);return q1.cross(p1)
    eq('first exact chiral nonclosure witness',chir(e,s.Matrix([1,-1,0]))-s.Matrix([s.Rational(7,20),s.Rational(7,20),-s.Rational(133,200)]))
    eq('second exact chiral nonclosure witness',chir(2*e,s.Matrix([1,-1,0])/2)-s.Matrix([s.Rational(323,1600),s.Rational(323,1600),-s.Rational(1273,3200)]))
    eq('intensity nonclosure witness',s.matrix_multiply_elementwise(pre(s.Matrix([1,-1,1]),s.zeros(3,1))[0],pre(s.Matrix([1,-1,1]),s.zeros(3,1))[0])-s.Matrix([s.Rational(9,25),s.Rational(1,25),s.Rational(9,25)]))
    check('zero-stratum real-Gram gap is nonzero',1-s.cos(s.Rational(1,5))>0)
    # Provenance and reference integrity; no import or modification of native code.
    manifest=json.loads((LANE/'provenance/source_manifest.json').read_text(encoding='utf8'))
    retained=json.loads((LANE/'verification/retained_evidence.json').read_text(encoding='utf8'))
    for key in ['GR0','GR1','GR2','CM0','SA0']:
        entry=manifest[key]
        check('immutable checkpoint hashes '+key,all(sha(Path(entry['directory'])/v['name'])==v['sha256'] for v in entry['artifacts']))
        original=json.loads((Path(entry['directory'])/retained[key]['source_results']).read_text(encoding='utf8'))
        check('retained verification object identical '+key,original['verification']==retained[key]['verification'])
    check('native Python source hashes unchanged',all(sha(REPO/v['path'])==v['sha256'] for v in manifest['native_sources']))
    ledger=json.loads((LANE/'provenance/theorem_ledger.json').read_text(encoding='utf8'))
    records=ledger if isinstance(ledger,list) else ledger['records']
    tex='\n'.join(p.read_text(encoding='utf8') for p in (LANE/'manuscript').glob('*.tex'))
    labels=re.findall(r'\\label\{([^}]+)\}',tex)
    refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
    check('unique manuscript labels',len(labels)==len(set(labels)))
    check('all manuscript references resolve',set(refs)<=set(labels))
    check('all ledger proof anchors resolve',all(v['manuscript_proof_label'] in labels for v in records))
    cites={c for arg in re.findall(r'\\cite\{([^}]+)\}',tex) for c in arg.split(',')}
    check('all citations have internal bibliography entries',cites<=set(re.findall(r'\\bibitem\{([^}]+)\}',tex)))
    return {'passed':all(c['passed'] for c in checks),'paper_local_predicate_count':len(checks),'qualification':'Bounded algebra/reference checks, not new theorems. Separate from 429 retained checkpoint predicates.','python':platform.python_version(),'sympy':s.__version__,'checks':checks,'inputs_sha256':{p.relative_to(LANE).as_posix():sha(p) for p in sorted((LANE/'manuscript').glob('*.tex'))}}
if __name__=='__main__':
    started=time.perf_counter();result=run();result['elapsed_seconds']=time.perf_counter()-started
    (LANE/'verification/paper_local_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','inputs_sha256']},indent=2))
