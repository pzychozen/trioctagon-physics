"""Independent exact-rational certificate checker (standard library only).

Does not import the generator, its dyadic arithmetic, mpmath, numpy or a native
implementation. Rechecks each supplied step using Fraction interval endpoints,
combined-coefficient prestages, expanded imaginary cubes, squared-root witness
inequalities, and midpoint Taylor values plus derivative/remainder bounds.
The certificate is untrusted input. No floating operation controls acceptance.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import copy,hashlib,json,math,os,sys
R=Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def singleton(x):x=Q(x);return(x,x)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    endpoints=[x*y for x in a for y in b];return(min(endpoints),max(endpoints))
def times(a,q):return mul(a,singleton(q))
def square(a):
    ends=[x*x for x in a];return(0 if a[0]<=0<=a[1] else min(ends),max(ends))
def cube(a):return(a[0]**3,a[1]**3)
def divide(a,b):
    assert b[0]>0,'Positive nonzero denominator not certified'
    return mul(a,(1/b[1],1/b[0]))
def contain(outer,inner,where):assert outer[0]<=inner[0]<=inner[1]<=outer[1],where
def modulus_squared(z):return add(square(z[0]),square(z[1]))
def complex_product(a,b):return(sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0])))
def trig_bounds(delta):
    m=(delta[0]+delta[1])/2;r=(delta[1]-delta[0])/2
    bound=max(abs(delta[0]),abs(delta[1]));assert bound<Q(1,100)
    # Scalar exact midpoint powers, not interval Horner arithmetic.
    sine=sum(Q((-1)**j,math.factorial(2*j+1))*m**(2*j+1) for j in range(24))
    cosine=sum(Q((-1)**j,math.factorial(2*j))*m**(2*j) for j in range(25))
    e_s=Q(1,100**49*math.factorial(49))+r
    e_c=Q(1,100**50*math.factorial(50))+bound*r
    # |sin'|<=1, |cos'|=|sin|<=|x|<=bound on the interval.
    return(sine-e_s,sine+e_s),(cosine-e_c,cosine+e_c)
def validate(c):
    assert c['N']==50 and c['precision_bits']==512 and c['denominator']==str(1<<512)
    S=int(c['denominator'])
    assert c['parameters']=={'epsilon':'1/10','g':'1/60','lambda':'1/300','k':['999/1000','1','1001/1000']}
    assert c['initial_state']==[['1','1'],['1','1'],['1','-2']]
    assert c['direction']==[987395,158274]
    def read(pair):
        assert len(pair)==2;lo,hi=map(int,pair);assert lo<=hi;return(Q(lo,S),Q(hi,S))
    def read_complex(z):assert len(z)==2;return(read(z[0]),read(z[1]))
    assert len(c['states'])==51 and len(c['steps'])==50
    states=[[read_complex(z) for z in state] for state in c['states']]
    assert all(len(state)==3 for state in states)
    for i,z in enumerate([[1,1],[1,1],[1,-2]]):
        for part,value in enumerate(z):assert states[0][i][part]==singleton(value),'Initial singleton must be exact'
    min_rho=None;max_kick=Q(0);stage_results=[]
    for n,step in enumerate(c['steps']):
        assert step['n']==n
        state=states[n];v=[read_complex(z) for z in step['prestage']]
        rho=[read(x) for x in step['moduli']];delta=[read(x) for x in step['kicks']]
        sine=[read(x) for x in step['sines']];cosine=[read(x) for x in step['cosines']]
        assert all(len(x)==3 for x in [v,rho,delta,sine,cosine])
        for i in range(3):
            coefficient=sub(singleton(1-Q(2,60)+Q(1,10)*[Q(999,1000),Q(1),Q(1001,1000)][i]),times(modulus_squared(state[i]),Q(1,10)))
            for part in range(2):
                neighbors=add(state[(i+1)%3][part],state[(i+2)%3][part])
                expected=add(mul(coefficient,state[i][part]),times(neighbors,Q(1,60)))
                contain(v[i][part],expected,f'prestage {n}/{i}/{part}')
            norm=modulus_squared(v[i]);assert norm[0]>0
            assert rho[i][0]>Q(87,100) and rho[i][0]**2<=norm[0] and rho[i][1]**2>=norm[1],f'root witness {n}/{i}'
            min_rho=rho[i][0] if min_rho is None else min(min_rho,rho[i][0])
        for i in range(3):
            total=singleton(0)
            for j in range(3):
                if j==i:continue
                real=add(mul(v[j][0],v[i][0]),mul(v[j][1],v[i][1]))
                imag=sub(mul(v[j][1],v[i][0]),mul(v[j][0],v[i][1]))
                numerator=sub(times(mul(square(real),imag),3),cube(imag))
                denominator=mul(cube(rho[i]),cube(rho[j]))
                total=add(total,divide(numerator,denominator))
            contain(delta[i],times(total,Q(1,300)),f'kick {n}/{i}')
            max_kick=max(max_kick,abs(delta[i][0]),abs(delta[i][1]))
            expected_s,expected_c=trig_bounds(delta[i])
            contain(sine[i],expected_s,f'sine {n}/{i}')
            contain(cosine[i],expected_c,f'cosine {n}/{i}')
            expected=complex_product(v[i],(cosine[i],sine[i]))
            for part in range(2):contain(states[n+1][i][part],expected[part],f'linked state {n+1}/{i}/{part}')
        stage_results.append({'n':n,'minimum_prestage_lower':str(min(r[0] for r in rho)),'status':'PASS'})
    # Validate the strict early turning on the same linked state enclosures.
    means=[]
    for state in states[:3]:means.append(tuple(times(add(add(state[0][part],state[1][part]),state[2][part]),Q(1,3)) for part in range(2)))
    d1=tuple(sub(means[1][p],means[0][p]) for p in range(2));d2=tuple(sub(means[2][p],means[1][p]) for p in range(2))
    turn=sub(mul(d1[0],d2[1]),mul(d1[1],d2[0]))
    assert Q('0.0110760731')<turn[0]<=turn[1]<Q('0.0110760732')
    terminal=[];a,b=c['direction']
    for i,z in enumerate(states[-1]):
        norm=modulus_squared(z);low,high=map(Q,c['terminal'][i]['amplitude_bounds'])
        assert Q(9,10)<low and low**2<norm[0]<=norm[1]<high**2 and high<Q(11,10),f'Terminal modulus {i}'
        real=add(times(z[0],a),times(z[1],b));imag=sub(times(z[1],a),times(z[0],b))
        contain(read(c['terminal'][i]['rotated_real']),real,f'terminal real record {i}')
        contain(read(c['terminal'][i]['rotated_imag']),imag,f'terminal imaginary record {i}')
        margin=real[0]-8*max(abs(imag[0]),abs(imag[1]));assert real[0]>0 and margin>0
        assert margin>=Q(int(c['terminal'][i]['cone_margin_numerator']),S)
        assert margin>=c['terminal'][i]['cone_margin_lower_integer']>0
        terminal.append({'channel':i,'amplitude_bounds':[str(low),str(high)],'lower_annulus_margin':str(low-Q(9,10)),'upper_annulus_margin':str(Q(11,10)-high),'cone_margin_lower_integer':c['terminal'][i]['cone_margin_lower_integer']})
    return{'status':'PASS','exact_seed_entry_N':50,'linked_updates_verified':50,'nonzero_prestages_verified':150,'all_prestage_moduli_strictly_above':'87/100','minimum_certified_prestage_lower':str(min_rho),'maximum_certified_kick_absolute_upper':str(max_kick),'ordinary_phase_width_strictly_below':'1/4 < pi/12','terminal':terminal,'early_turn_enclosure':['0.0110760731','0.0110760732'],'early_turn_role':'Dependency check of inherited strict two-step turning, not rediscovery.','step_results':stage_results}
if __name__=='__main__':
    certpath=R/'data/CERTIFICATE.json';c=json.loads(certpath.read_text())
    if len(sys.argv)>1 and sys.argv[1]=='negative-controls':
        trials=[]
        mutations=[('wrong exact initial state',lambda x:x['states'][0][0][0].__setitem__(0,str(int(x['states'][0][0][0][0])+1))),('zero prestage modulus',lambda x:x['steps'][0]['moduli'][0].__setitem__(0,'0')),('wrong kick sign',lambda x:x['steps'][0].__setitem__('kicks',[['0','0']]*3)),('broken trajectory linkage',lambda x:x['states'][1].__setitem__(0,[['0','0'],['0','0']])),('false terminal amplitude bound',lambda x:x['terminal'][0].__setitem__('amplitude_bounds',['1','10001/10000']))]
        for name,mutate in mutations:
            altered=copy.deepcopy(c);mutate(altered)
            try:validate(altered)
            except (AssertionError,ValueError,ZeroDivisionError) as exc:trials.append({'mutation':name,'rejected':True,'reason':str(exc)})
            else:raise AssertionError('Invalid certificate accepted: '+name)
        result={'status':'PASS','purpose':'Checker falsification controls, not additional trajectories/theorems','controls':trials};name='CHECKER_NEGATIVE_CONTROLS.json'
    else:result=validate(c);name='CERTIFICATE_CHECK.json'
    result.update(checked_utc=datetime.now(timezone.utc).isoformat(),certificate_sha256=hashlib.sha256(certpath.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),arithmetic='Exact fractions and integer comparisons only; no generator import, float, native module or mpmath.',independence='Unrounded Fraction interval operations with combined prestages/expanded cube identity; sqrt witnesses checked by exact squared inequalities; midpoint power-series plus Lipschitz/remainder bounds instead of dyadic interval Horner evaluation.')
    (R/'data'/name).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key not in ['step_results','minimum_certified_prestage_lower','maximum_certified_kick_absolute_upper']},indent=2))
