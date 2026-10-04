"""K-G0 independent 100-digit oracle. No kernel imports; never run by tests.

Generate once before the observer implementation; output is reviewed/frozen.
Scientific authority: Paper G v0.1.1 sections 2-3. Inputs are exact values of
the specified binary64 numbers; special algebraic witnesses are tested separately.
"""
import hashlib
import json
from pathlib import Path
import mpmath as m

m.mp.dps = 100
T = m.matrix([[-m.mpf(1)/2,1,-m.mpf(1)/2],[-m.sqrt(3)/2,0,m.sqrt(3)/2],[0,0,0]])
L = m.matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
names = ('onsite_first','coupling_first','onsite_squared','mixed','coupling_squared',
         'phase_existing_area','phase_symmetric_pair')

def plain(x):
    if isinstance(x, m.matrix): return [[plain(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x, m.mpc): return [plain(x.real), plain(x.imag)]
    if isinstance(x,(tuple,list)): return [plain(v) for v in x]
    if isinstance(x,dict): return {k:plain(v) for k,v in x.items()}
    return m.nstr(x,90)

def area(A):
    c=m.matrix([A[1,2],A[2,0],A[0,1]])
    return {'A':A,'C':list(c),'W':list(T*c),'Gamma':sum(c)}

def snap(v):
    x=m.matrix([z.real for z in v]);y=m.matrix([z.imag for z in v])
    A=x*y.T-y*x.T;S=x*x.T+y*y.T;r=area(A)
    r.update(S=S,intensity=sum(abs(z)**2 for z in v))
    return r

def fixture(label,v,eps,g,lam,k):
    pairs=[[float(complex(z).real).hex(),float(complex(z).imag).hex()] for z in v]
    values=[m.mpc(m.mpf(float.fromhex(a)),m.mpf(float.fromhex(b))) for a,b in pairs]
    scalars=[float(x).hex() for x in (eps,g,lam,*k)]
    e,h,l,*ks=[m.mpf(float.fromhex(x)) for x in scalars]
    before=snap(values); A=before['A'];S=before['S']
    D=m.diag([ks[i]-abs(values[i])**2 for i in range(3)])
    M=m.eye(3)+e*D+h*L; vpre=list(M*m.matrix(values));pre=snap(vpre)
    phi=[m.arg(z) if z else m.mpf(0) for z in vpre]
    delta=[l*sum(m.sin(3*(phi[j]-phi[i])) for j in range(3) if j!=i) for i in range(3)]
    d=m.matrix([[delta[j]-delta[i] for j in range(3)] for i in range(3)])
    terms=[e*(D*A+A*D),h*(L*A+A*L),e*e*D*A*D,e*h*(D*A*L+L*A*D),h*h*L*A*L,
           m.matrix([[pre['A'][i,j]*(m.cos(d[i,j])-1) for j in range(3)] for i in range(3)]),
           m.matrix([[pre['S'][i,j]*m.sin(d[i,j]) for j in range(3)] for i in range(3)])]
    after=snap([z*m.exp(1j*delta[i]) for i,z in enumerate(vpre)])
    scale=max(1,sum(abs(x) for x in A)+sum(sum(abs(x) for x in a) for a in terms))
    return {'name':label,'omega_hex':pairs,'parameters_hex':dict(zip(('eps','g','phase_strength','k'),(*scalars[:3],scalars[3:]))),
            'snapshot':plain(before),'terms':{n:plain(area(t)) for n,t in zip(names,terms)},
            'pre_sync':plain({'omega':vpre,**pre,'phases':phi,'delta':delta,'d':d}),
            'predicted':plain(after),'budget_scale':plain(scale)}

def main():
    root=Path(__file__).parent; target=root/'reference.json'
    if target.exists(): raise SystemExit('Frozen reference exists; no overwrite permitted')
    generic=(.2+.3j,-.4+.1j,.1-.2j)
    rows=[fixture('generic',generic,.05,.2,.17,(1,1.2,1.4)),
          fixture('lambda_zero',generic,.05,.2,0,(1,1.2,1.4)),
          fixture('singular_M',(1,1j,-1),.25,.25,.17,(0,0,0)),
          fixture('branch_cut',(-1+1e-12j,-1-1e-12j,.3+.2j),0,0,.19,(1,1,1)),
          fixture('zero_component',(1,0,1j),0,0,.13,(1,1,1)),
          fixture('b_zero',(1,1j,0),1,0,.13,(0,1,0)),
          fixture('same_A_first',(1,1j,1),.1,0,0,(1,1,1)),
          fixture('same_A_second',(2,.5j,2),.1,0,0,(1,1,1))]
    data={'authority':'Paper G v0.1.1, sections 2-3', 'oracle':'mpmath 1.3.0; 100 digits; independent matrix/pair-product evaluation',
          'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'algebraic_factor':512,'step_factor':2048,
          'unit_roundoff':'0x1.0000000000000p-53','cases':rows}
    target.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(hashlib.sha256(target.read_bytes()).hexdigest())

if __name__=='__main__':main()
