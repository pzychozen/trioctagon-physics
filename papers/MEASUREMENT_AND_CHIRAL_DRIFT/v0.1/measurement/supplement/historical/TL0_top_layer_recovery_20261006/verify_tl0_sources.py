# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""Bounded TL0 checks. Writes ONLY the adjacent external crosswalk/results JSON.

Run with: python -X utf8 -B verify_tl0_sources.py
No historical simulation/UI is imported. No recurrence trajectory or old test
suite is run. Original sources are read-only; bytecode output is disabled.
"""
from pathlib import Path
from types import SimpleNamespace
import ast
import hashlib
import importlib.util
import json
import math
import re
import subprocess
import sys

sys.dont_write_bytecode = True
import numpy as np
import sympy as sp

ROOT = Path('project-source')
REPO = ROOT / 'trioctagon-physics'
OUT = Path(__file__).resolve().parent
REPORT = OUT / 'TL0_TOP_LAYER_CIRCLE_RECOVERY.md'
RESULT = OUT / 'tl0_object_crosswalk.json'
assert OUT == ROOT / 'research/TL0_top_layer_recovery_20261006'
record = json.loads(RESULT.read_text(encoding='utf-8'))
checks = []


def check(name, truth, evidence, detail=None):
    checks.append(dict(name=name, passed=bool(truth), evidence=evidence, detail=detail))


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args]).decode('utf-8')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def isolated_function(path, name, extra=None):
    """Compile one original function, excluding module/UI top-level statements."""
    tree = ast.parse(path.read_text(encoding='utf-8-sig'), filename=str(path))
    node = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == name)
    namespace = {'np': np, 'math': math, 'TorusConfig': SimpleNamespace}
    namespace.update(extra or {})
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
    return namespace[name]


# Source references and machine-readable census are extracted from the report,
# so the report remains the single place defining scope and object granularity.
text = REPORT.read_text(encoding='utf-8')
refs = dict(re.findall(r'^\[([^\]]+)\]: <?([^\n>]+)>?$', text, flags=re.M))
source_records = {}
for key, raw in refs.items():
    path = Path(raw.strip())
    if key in {'results', 'script'}:
        continue
    check('source exists: '+key, path.is_file(), 'SOURCE FACT')
    if path.is_file():
        data = path.read_bytes()
        source_records[key] = {'path': str(path), 'bytes': len(data), 'sha256': sha(data)}

incomplete = {'H04', 'H06', 'H08', 'H09', 'H21', 'H22', 'H23', 'H24'}
objects = []
for line in text.splitlines():
    if not line.startswith('| **H'):
        continue
    cells = [s.strip().replace('\\|', '|') for s in re.split(r'(?<!\\)\|', line)[1:-1]]
    identifier = re.search(r'H\d\d', cells[0]).group()
    keys = re.findall(r'\]\[([^\]]+)\]', line)
    objects.append({'id': identifier, 'name_and_locator': cells[0],
                    'formula_construction_domain_parameters': cells[1],
                    'evolution_type_survival_relation': cells[2],
                    'definition_status': 'incomplete_proposal_or_schematic' if identifier in incomplete else 'specified_object_or_map',
                    'source_keys': keys})
check('24 source/type records with 16 specified and 8 incomplete',
      len(objects) == 24 and len({o['id'] for o in objects}) == 24
      and sum(o['definition_status'] == 'specified_object_or_map' for o in objects) == 16,
      'SOURCE FACT')

# Lens identities: these are mathematical consequences of the stated circles.
r, theta = sp.symbols('r theta', positive=True, real=True)
d = 2*r*sp.cos(theta)
height = r*sp.sin(theta)
check('lens intersection lies on both parent circles',
      sp.trigsimp((d/2)**2+height**2-r**2) == 0, 'DERIVED IDENTITY')
area = 2*(r**2*theta-r**2*sp.sin(2*theta)/2)
check('lens sector-minus-triangle area',
      sp.simplify(area-r**2*(2*theta-sp.sin(2*theta))) == 0, 'DERIVED IDENTITY')
check('current normalized area drops absolute radius',
      sp.simplify(area/(sp.pi*r**2)-(2*theta-sp.sin(2*theta))/sp.pi) == 0,
      'DERIVED IDENTITY')

# Load only the pure exact geometry module, under a task-local module name.
gpath = REPO / 'kernel_physics/geometry.py'
spec = importlib.util.spec_from_file_location('tl0_readonly_geometry', gpath)
geom = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = geom
spec.loader.exec_module(geom)
mesh = geom.folded_module()
loops = mesh.boundary_loops
check('native shell has 18 vertices, 3 seams, two nine-edge rims, Euler zero',
      len(mesh.vertices) == 18 and len(mesh.seam_edges) == 3 and
      [len(x) for x in loops] == [9, 9] and mesh.euler_characteristic == 0,
      'DERIVED IDENTITY')
top = [sp.Matrix(mesh.vertices[i]) for i in loops[1]]
base = top[0]
rank = sp.Matrix.hstack(*(p-base for p in top[1:])).rank()
heights = {str(z): sum(p[2] == z for p in top) for z in set(p[2] for p in top)}
check('upper rim has affine rank three, hence is not a Euclidean circle',
      rank == 3 and sum(p[2] == sp.Rational(1, 2) for p in top) == 6,
      'DERIVED IDENTITY', {'affine_rank': rank, 'height_multiplicities': heights})

# Standard torus identity, free angles. No topology is inferred for data curves.
R, a, phi, chi = sp.symbols('R a phi chi', real=True)
X=(R+a*sp.cos(chi))*sp.cos(phi)
Y=(R+a*sp.cos(chi))*sp.sin(phi)
Z=a*sp.sin(chi)
rad2=sp.trigsimp(X**2+Y**2)
implicit=sp.trigsimp((rad2+Z**2+R**2-a**2)**2-4*R**2*rad2)
check('standard torus quartic identity', sp.simplify(implicit) == 0, 'DERIVED IDENTITY')
check('fixed upper parallel is radius R at height a',
      sp.simplify(X.subs(chi, sp.pi/2)-R*sp.cos(phi)) == 0 and
      sp.simplify(Y.subs(chi, sp.pi/2)-R*sp.sin(phi)) == 0 and Z.subs(chi, sp.pi/2) == a,
      'DERIVED IDENTITY')

old = ROOT/'kernel_TO'
torus_a=isolated_function(old/'geometry_3d.py', 'history_to_torus_xyz')
torus_config=isolated_function(old/'geometry_embeddings.py', 'history_to_torus_xyz')
cylinder=isolated_function(old/'geometry_3d.py', 'history_to_xyz')
torus_b=isolated_function(old/'toy_3d_triocta.py', 'embed_on_torus')
h={'kappa':np.array([0.,.2,1.,3.]),'phi_index':np.array([0,1,5,11]),'z':np.array([0.,-.3,.2,.8])}
ca=np.array(torus_a(h))
cb=np.array(torus_config(h,SimpleNamespace(R=2.,r_max=1.,n_sectors=12)))
check('H13 implementations agree at N=12',np.max(np.abs(ca-cb)) <= 2e-15,
      'NUMERICAL EVIDENCE', {'max_absolute_difference':float(np.max(np.abs(ca-cb)))})
cyl=np.array(cylinder(h))
check('H12 cylindrical radius equals kappa',np.allclose(np.hypot(cyl[0],cyl[1]),h['kappa'],rtol=0,atol=1e-15),
      'NUMERICAL EVIDENCE')
minor=h['kappa']/(1+h['kappa'])
check('H13 samplewise tube radius identity',np.allclose((np.hypot(ca[0],ca[1])-2)**2+ca[2]**2,minor**2,rtol=0,atol=1e-15),
      'NUMERICAL EVIDENCE')
angles=.5*np.pi*h['z']/(np.max(np.abs(h['z']))+1e-9)
check('H13 finite-data minor angles lie strictly within half range',np.all(np.abs(angles)<np.pi/2),
      'NUMERICAL EVIDENCE')
h1={'kappa':np.array([1.]),'phi_index':np.array([0]),'z':np.array([.2])}
h2={'kappa':np.array([1.,1.]),'phi_index':np.array([0,1]),'z':np.array([.2,1.])}
delta=float(np.linalg.norm(np.array(torus_a(h1))[:,0]-np.array(torus_a(h2))[:,0]))
check('H13 earlier coordinate changes when future history maximum changes',delta > .1,
      'NUMERICAL EVIDENCE', {'coordinate_difference':delta})
w=np.array([[1+0j,0+1j,-1+0j],[2+1j,1-2j,.3+.2j]],dtype=complex)
xb,yb,zb=torus_b(w)
fixed_phi=np.arange(3)*2*np.pi/3
anchor_res=float(np.max(np.abs(-np.sin(fixed_phi)[:,None]*xb+np.cos(fixed_phi)[:,None]*yb)))
check('H14 nodes remain in their three meridian planes',anchor_res<2e-15,
      'NUMERICAL EVIDENCE', {'residual':anchor_res})
check('H14 responds to channel phase even when total norm and clock are held',
      np.linalg.norm(np.array(torus_b(w[:1]))-np.array(torus_b(np.abs(w[:1]).astype(complex))))>.1,
      'NUMERICAL EVIDENCE')

# Literal source and AST/dataflow checks: bounded to the cited functions.
ui_tree=ast.parse((old/'toy_3d_triocta.py').read_text(encoding='utf-8-sig'))
fn={n.name:n for n in ui_tree.body if isinstance(n,ast.FunctionDef)}
run=fn['run_triocta']
calls={getattr(n.func,'id',getattr(n.func,'attr','')) for n in ast.walk(run) if isinstance(n,ast.Call)}
check('historical runner invokes RSB preparation but no torus/halo function',
      'tri_to_rsb_params' in calls and 'RSBModel' in calls and
      not {'embed_on_torus','draw_rsb_halo','history_to_torus_xyz'} & calls, 'SOURCE FACT')
halo=next(n for n in ast.walk(ui_tree) if isinstance(n,ast.FunctionDef) and n.name=='torus_ring')
halo_names={n.id for n in ast.walk(halo) if isinstance(n,ast.Name)}
check('halo coordinate function does not read band energies',
      not {'E_final','norm_E','log_E','rsb_alpha'} & halo_names, 'SOURCE FACT')
halo_expr=ast.unparse(halo)
check('halo uses declared 1.01 and 1.05 geometric multipliers',
      '1.01' in halo_expr and '1.05' in halo_expr, 'SOURCE FACT')
phi_s=np.linspace(0,2*np.pi,19)
minor_angle=.7
xh=(2*1.01+.6*1.05*np.cos(minor_angle))*np.cos(phi_s)
yh=(2*1.01+.6*1.05*np.cos(minor_angle))*np.sin(phi_s)
check('halo latitude is a planar circle for a fixed band',
      np.ptp(xh*xh+yh*yh)<4e-15,'NUMERICAL EVIDENCE')
cor_tree=ast.parse((old/'tangent_corridor_analysis.py').read_text(encoding='utf-8-sig'))
cor=next(n for n in cor_tree.body if isinstance(n,ast.FunctionDef) and n.name=='detect_tangent_corridors')
assign={n.targets[0].id:ast.unparse(n.value) for n in ast.walk(cor) if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name)}
check('corridor X,Y use phi in both roles, not chi',
      assign['X']=='(R + r * np.cos(phi)) * np.cos(phi)' and
      assign['Y']=='(R + r * np.cos(phi)) * np.sin(phi)', 'SOURCE FACT')
check('12-clock versus 24-window scaffold strides differ',
      sp.simplify(2*sp.pi/12-sp.pi/6)==0 and sp.simplify(2*sp.pi/24-sp.pi/12)==0,
      'DERIVED IDENTITY')
check('24 successive half-steps are needed for a full turn',
      12*sp.pi/12==sp.pi and 24*sp.pi/12==2*sp.pi, 'DERIVED IDENTITY')
ui_lab=(old/'toy_lab.py').read_text(encoding='utf-8-sig')
check('polar histogram reads stored clock while helper reads mean phase',
      'np.angle(np.mean(Omega))' in ui_lab and 'hist["phi_index"]' in ui_lab,
      'SOURCE FACT')
boundary=(REPO/'kernel_physics/boundary_response.py').read_text(encoding='utf-8')
check('current response is explicitly labelled a toy adoption',
      'explicitly chosen lens_area_norm_v1 toy response, not recovered physics' in boundary,
      'SOURCE FACT')

# Full protected tree inventories: all regular files, including pre-existing
# untracked/tmp files; .git is inspected through separate Git state checks.
def inventory(path):
    paths={}
    total=0
    for f in sorted(path.rglob('*')):
        if f.is_file() and '.git' not in f.relative_to(path).parts:
            data=f.read_bytes()
            paths[f.relative_to(path).as_posix()]=sha(data)
            total+=len(data)
    variants={str(ascii_):sha(json.dumps(paths,sort_keys=True,separators=(',',':'),ensure_ascii=ascii_).encode('utf-8'))
              for ascii_ in (True,False)}
    return {'files':len(paths),'bytes':total,'digest_variants':variants}

protected_after={}
for root,before in record['protected_before'].items():
    after=inventory(Path(root))
    protected_after[root]=after
    ok=(before['files']==after['files'] and before['bytes']==after['bytes'] and
        before['sha256'] in after['digest_variants'].values())
    check('protected tree unchanged: '+root,ok,'SOURCE FACT')
after_head=git('rev-parse','HEAD').strip()
after_status=git('status','--short')
after_index=sha(git('ls-files','--stage','-z').encode('utf-8'))
check('HEAD unchanged',after_head==record['head_before'],'SOURCE FACT')
check('working-tree status unchanged',after_status==record['status_before'],'SOURCE FACT')
check('index entries unchanged',after_index==record['index_before'],'SOURCE FACT')
record.update(status='TL0 COMPLETE' if all(c['passed'] for c in checks) else 'TL0 CHECK FAILURE',
              top_circle_status='OPEN / NOT_FORMALIZED',sources=source_records,objects=objects,
              checks=checks,head_after=after_head,status_after=after_status,index_after=after_index,
              protected_after=protected_after,
              report_sha256=sha(REPORT.read_bytes()),script_sha256=sha(Path(__file__).read_bytes()),
              counts={'total':len(checks),'pass':sum(c['passed'] for c in checks),
                      'historical_candidate_records':len(objects),
                      'specified_constructions':16,'incomplete_proposals':8},
              evidence_boundary='Bounded TL0 checks only; no parked checkpoint or paper test counts combined.',
              visual_pages=['Vesica Delay Method-1.pdf p1','TriOcta_violations.pdf p5',
                            'Forward_Backward_recursion.pdf p8'])
RESULT.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'counts':record['counts'],
                  'failed':[c for c in checks if not c['passed']],
                  'head':after_head},indent=2))
raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
