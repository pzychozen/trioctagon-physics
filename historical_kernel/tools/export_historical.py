"""External comparison process A: installed Historical mathematics only."""
import argparse,json,sys
from pathlib import Path
from trioctagon_historical_kernel import api
from trioctagon_historical_kernel.ema_z import advance_ema


def main():
    p=argparse.ArgumentParser();p.add_argument('--fixtures',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    f=json.loads(Path(args.fixtures).read_bytes())
    def state(v):return api.Triad(tuple(complex(float.fromhex(a),float.fromhex(b)) for a,b in v))
    def omega(v):return [[z.real.hex(),z.imag.hex()] for z in v.values]
    def readout(v):return [float(x).hex() for x in (v.z,*v.M,*v.C,*v.T)]
    one=[dict(profile=r['profile'],vector=r['vector'],omega=omega(api.step(state(r['input']),api.KProfile(r['profile'])))) for r in f['one']]
    multi=[]
    for r in f['multi']:
        h=api.run(state(r['input']),api.KProfile(r['profile']),64,api.Readout.STAGED)
        memory=api.Memory();steps=[]
        for s in (*h.rows[1:],h.terminal):
            memory=advance_ema(s.omega,memory)
            steps.append(dict(n=s.update_index,omega=omega(s.omega),q=s.clock.q,t=s.clock.t.hex(),
                staged=readout(s.observation),ema=readout(api.observe_ema(s.omega,s.clock,memory)),memory=memory.value.hex()))
        multi.append(dict(profile=r['profile'],vector=r['vector'],steps=steps))
    assert not any(name.split('.')[0] in {'kernel_physics','kernel_TO','torment_service'} for name in sys.modules)
    Path(args.out).write_bytes((json.dumps(dict(one=one,multi=multi),sort_keys=True,separators=(',',':'))+'\n').encode())

if __name__=='__main__':main()
