"""Bounded check of the specific P23 defining product and native fixed transfer."""
from pathlib import Path
import sys,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'measurement/supplement/native'))
from kernel_physics.srg import fixed_november_srg,NOVEMBER

# Treat scalar entries as independent: no fitted numbers or simulation.
q,r,c,z0,z1,z2,d0,d1,x00,x01,x10,x11=s.symbols('q r c z0 z1 z2 d0 d1 x00 x01 x10 x11')
P=s.ones(3)/3
R=q*s.eye(3)+(r-q)*P
C=c*s.eye(3)+(1-c)*P
Z=s.diag(z0,z1,z2);D=s.diag(d0,d1);X=s.Matrix([[x00,x01],[x10,x11]])
k=s.kronecker_product
product=k(s.eye(2),R)*k(D,Z)*k(X,s.eye(3))*k(s.eye(2),C)
factor=k(D*X,R*Z*C)
assert all(s.expand(v)==0 for v in product-factor)
assert P*P==P

# Independently assemble P23's defining six-state factors at its fixed constants.
assert (NOVEMBER.eta,NOVEMBER.gamma,NOVEMBER.lambda_c,NOVEMBER.clock_fraction)==(.423,.577,.618,.244)
Pi=np.kron(np.eye(2),np.ones((3,3))/3)
Urpc=(1-.618)*np.eye(6)+.618*Pi
Uref=np.exp(.577)*Pi+np.exp(-.423)*(np.eye(6)-Pi)
Utg=np.diag([np.exp(-1j*(2*np.pi/3*j+2*np.pi*.244*sign)) for sign in [1,-1] for j in range(3)])
Uflip=np.kron(np.array([[np.cos(np.pi*.244),-1j*np.sin(np.pi*.244)],[-1j*np.sin(np.pi*.244),np.cos(np.pi*.244)]]),np.eye(3))
native=fixed_november_srg()
res=float(np.max(np.abs(Uref@Utg@Uflip@Urpc-native.U)))
assert res<2e-15
assert np.linalg.norm(Uref.conj().T@Uref-np.eye(6))>.1
record={'status':'PASS','symbolic_result':'All 36 entries vanish identically in (I2 tensor R)(D tensor Z)(X tensor I3)(I2 tensor C) - (DX tensor RZC).',
        'classification':'EXACT DESCENDANT for P23 defining operators only; no timeless RPCO/TGMO/REFU identity claimed.',
        'primary_source':'P23 pp. 5-6 and basis ordering on p. 30',
        'numeric_comparison':'One fixed defining-matrix check, not a trajectory or parameter sweep.',
        'maximum_entrywise_absolute_residual':res,'tolerance':2e-15,
        'fixed_constants':{'eta':.423,'gamma':.577,'lambda_c':.618,'clock_fraction':.244},
        'REFU_scope':'Fixed nonunitary matrix, no auxiliary evolving memory variable; historical claims of physical memory/attractors are not adopted.',
        'historical_scripts_executed':False,'new_model_or_research_checkpoint':False}
(ROOT/'results/lineage_verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
