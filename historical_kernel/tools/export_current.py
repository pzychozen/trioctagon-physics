"""External comparison process B: current scientific implementation only; never installed in Historical wheel."""
import argparse,json,sys
from pathlib import Path
from kernel_physics import dynamics,z_manifold


def main():
    p=argparse.ArgumentParser();p.add_argument('--fixtures',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    f=json.loads(Path(args.fixtures).read_bytes())
    mapping={'HISTORICAL_THETA_SCALED':'historical_default','HISTORICAL_THETA_SOFT':'theta_soft','HISTORICAL_SIMPLE':'simple'}
    def config(profile):
        row=f['parameters'][mapping[profile]]
        return dynamics.DynamicsConfig(eps=float.fromhex(row['eps']['hex']),g=float.fromhex(row['g']['hex']),
            phase_strength=float.fromhex(row['phase']['hex']),k=tuple(float.fromhex(x['hex']) for x in row['k']))
    def state(v):return [complex(float.fromhex(a),float.fromhex(b)) for a,b in v]
    def omega(v):return [[float(z.real).hex(),float(z.imag).hex()] for z in v]
    def readout(v):return [float(x).hex() for x in (v.z,*v.Z_macro,*v.Z_chiral,*v.Z_total)]
    one=[dict(profile=r['profile'],vector=r['vector'],omega=omega(dynamics.step3(state(r['input']),config(r['profile'])))) for r in f['one']]
    multi=[]
    for r in f['multi']:
        value=state(r['input']);clock=z_manifold.Clock();memory=z_manifold.EMAState();steps=[]
        for n in range(1,65):
            value=dynamics.step3(value,config(r['profile']));clock=z_manifold.advance_clock(clock,.1)
            memory=z_manifold.advance_ema(value,memory)
            steps.append(dict(n=n,omega=omega(value),q=clock.q,t=clock.t.hex(),memory=memory.m.hex(),
                staged=readout(z_manifold.observe_staged(value,clock,z_manifold.StagedConfig())),
                ema=readout(z_manifold.observe_ema(value,clock,z_manifold.EMAConfig(),memory))))
        multi.append(dict(profile=r['profile'],vector=r['vector'],steps=steps))
    assert not any(name.split('.')[0] in {'trioctagon_historical_kernel','kernel_TO','torment_service'} for name in sys.modules)
    Path(args.out).write_bytes((json.dumps(dict(one=one,multi=multi),sort_keys=True,separators=(',',':'))+'\n').encode())

if __name__=='__main__':main()
