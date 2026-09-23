"""Small face-view replay using only modules inside this proposed checkout."""
from pathlib import Path
import hashlib,json,sys
sys.dont_write_bytecode=True
from publication_runtime import ROOT, EVIDENCE
REPO=ROOT.parents[1]
sys.path.insert(0,str(REPO))
import numpy as np
import sympy
from kernel_physics import dynamics,geometry,face_state,readouts
state=np.array([.3+.2j,-.4+.1j,.2-.3j])
config=dynamics.DynamicsConfig(eps=.05,g=.2,phase_strength=.001,k=(1.,1.2,1.4))
view=face_state.FaceState(state)
expected=dynamics.step3(state,config)
after=view.step(config)
assert after.omega.tobytes()==expected.tobytes()
assert view.omega.tobytes()==state.tobytes()
assert face_state.area_triple(state).tobytes()==readouts.z_chiral(state).tobytes()
v=view.vectors;frames=face_state.face_frames()
area=np.array([frames.normals[i]@np.cross(v[i],face_state.transport(i,j)@v[j])
               for i,j in [(1,2),(2,0),(0,1)]])
np.testing.assert_allclose(area,readouts.z_chiral(state),rtol=2e-15,atol=1e-17)
modules=[]
for name,module in sorted(sys.modules.items()):
    if name=="kernel_physics" or name.startswith("kernel_physics."):
        p=Path(module.__file__).resolve()
        assert p.is_relative_to(REPO),"Kernel module escaped isolated checkout: "+str(p)
        modules.append({"module":name,"repository_path":p.relative_to(REPO).as_posix(),
                        "sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
result={"status":"PASS","attribution":"Codex publication implementation smoke",
 "scope":"One existing plain step, canonical-state preservation, delegated chirality and independent transported-area comparison. No upstream preparation experiment.",
 "python":sys.version.split()[0],"numpy":np.__version__,"sympy":sympy.__version__,
 "all_kernel_imports_inside_checkout":True,"kernel_modules":modules}
EVIDENCE.mkdir(parents=True,exist_ok=True)
(EVIDENCE/"runtime_smoke.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
print(json.dumps(result,indent=2))
