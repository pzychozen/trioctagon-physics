"""N02 one-seed exploration only; no numerical result is an enclosure."""
from pathlib import Path
from datetime import datetime,timezone
import cmath,json,math,os,sys
import mpmath as mp
R=Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
assert '**DISTINCT_GAP**' in (R/'PRIOR_WORK_COMPARISON.md').read_text(encoding='utf-8')
gate={'outcome':'DISTINCT_GAP','frozen_utc':datetime.now(timezone.utc).isoformat(),'prior_work_file':'PRIOR_WORK_COMPARISON.md','new_trajectory_calls_before_gate':0}
(R/'logs/PRIOR_GATE.json').write_text(json.dumps(gate,indent=2)+'\n')
mp.mp.dps=90
eps=mp.mpf(1)/10;g=mp.mpf(1)/60;lam=mp.mpf(1)/300;k=[mp.mpf(999)/1000,mp.mpf(1),mp.mpf(1001)/1000]
z=[mp.mpc(1,1),mp.mpc(1,1),mp.mpc(1,-2)];zf=[1+1j,1+1j,1-2j]
def s(x):return mp.nstr(x,85)
def arc(z):
    angles=sorted([mp.arg(x)%(2*mp.pi) for x in z]); gaps=[angles[(i+1)%3]-angles[i]+(2*mp.pi if i==2 else 0) for i in range(3)]
    largest=max(range(3),key=lambda i:gaps[i]); width=2*mp.pi-gaps[largest];start=angles[(largest+1)%3]
    return width,start+width/2
records=[];minpre=mp.inf;first=None;maxdiff=mp.mpf(0)
for n in range(513):
    width,center=arc(z);radii=[abs(x) for x in z]; inside=all(mp.mpf(9)/10<=r<=mp.mpf(11)/10 for r in radii) and width<=mp.pi/12
    if inside and first is None:first=n
    maxdiff=max(maxdiff,max(abs(mp.mpc(x.real,x.imag)-y) for x,y in zip(zf,z)))
    row={'n':n,'state':[[s(x.real),s(x.imag)] for x in z],'radii':[s(r) for r in radii],'ordinary_arc_width_radians':s(width),'arc_midpoint_radians':s(center),'numerically_in_D':inside,'binary64_state':[[x.real,x.imag] for x in zf]}
    records.append(row)
    if n>=2 and all(mp.mpf('0.95')<r<mp.mpf('1.05') for r in radii) and width<mp.pi/24:break
    assert n<512,'No comfortably interior candidate in default budget; preserve outcome before any extension'
    v=[x+eps*x*(k[i]-abs(x)**2)+g*sum(z[j]-x for j in range(3) if j!=i) for i,x in enumerate(z)]
    row['prestage']=[[s(x.real),s(x.imag)] for x in v]; row['minimum_prestage_modulus']=s(min(abs(x) for x in v));minpre=min(minpre,min(abs(x) for x in v))
    phi=[mp.arg(x) if x else mp.mpf(0) for x in v]
    kicks=[lam*sum(mp.sin(3*(phi[j]-phi[i])) for j in range(3) if j!=i) for i in range(3)]
    z=[v[i]*mp.exp(mp.j*kicks[i]) for i in range(3)]
    vf=[x+.1*x*([.999,1.,1.001][i]-abs(x)**2)+(1/60)*sum(zf[j]-x for j in range(3) if j!=i) for i,x in enumerate(zf)]
    pf=[cmath.phase(x) if x else 0. for x in vf]
    zf=[abs(vf[i])*cmath.exp(1j*(pf[i]+(1/300)*sum(math.sin(3*(pf[j]-pf[i])) for j in range(3) if j!=i))) if vf[i] else 0j for i in range(3)]
a=int(mp.nint(1000000*mp.cos(center))); b=int(mp.nint(1000000*mp.sin(center)))
means=[sum(mp.mpc(*p) for p in rec['state'])/3 for rec in records[:3]]
turn=mp.im(mp.conj(means[1]-means[0])*(means[2]-means[1]))
out={'classification':'EXPLORATORY_NUMERICAL_ONLY','precision_decimal_digits':90,'mpmath_version':mp.__version__,'seed_count':1,'updates':n,'first_numerical_D_entry':first,'candidate_N':n,'candidate_rational_direction':[a,b],'minimum_prestage_modulus':s(minpre),'maximum_binary64_discrepancy':s(maxdiff),'two_step_turn':s(turn),'phase_width_method':'2*pi minus largest cyclic gap among sorted ordinary arguments modulo 2*pi; no third-turn identification.','target_selection':'Stop at first n>=2 with all radii strictly between .95 and 1.05 and ordinary width < pi/24; comfortably interior sufficient target, no earliest-entry claim.','records':records,'completed_utc':datetime.now(timezone.utc).isoformat()}
(R/'data/EXPLORATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:value for key,value in out.items() if key!='records'},indent=2))
print('Terminal radii:',records[-1]['radii']); print('Terminal width:',records[-1]['ordinary_arc_width_radians'])
