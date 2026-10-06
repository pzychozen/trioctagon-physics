# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""Bounded TL3 checks; writes only TL3_RESULTS.json beside this script.

Run: python -X utf8 -B verify_tl3.py
Proofs, domain qualifications and source interpretation are in the report.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
sys.dont_write_bytecode = True
import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path('project-source')
REPO = ROOT/'trioctagon-physics'
OUT = Path(__file__).resolve().parent
assert OUT == ROOT/'research/TL3_vesica_containment_20261006'
RESULT = OUT/'TL3_RESULTS.json'
record = json.loads(RESULT.read_text(encoding='utf-8'))
checks = []


def check(name, passed, kind, details=None):
    checks.append(dict(name=name, passed=bool(passed), evidence=kind, details=details))


def sha(b): return hashlib.sha256(b).hexdigest()


def inventory(path):
    rows = {}; total = 0
    for p in sorted(path.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(path).parts and not p.is_relative_to(OUT):
            b = p.read_bytes(); rows[p.relative_to(path).as_posix()] = sha(b); total += len(b)
    return dict(files=len(rows), bytes=total,
                sha256=sha(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()))


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args]).decode('utf-8')


spec = importlib.util.spec_from_file_location('tl3_exact_geometry', REPO/'kernel_physics/geometry.py')
geo = importlib.util.module_from_spec(spec); sys.modules[spec.name] = geo
spec.loader.exec_module(geo)
mesh = geo.folded_module()
V = sp.Matrix
o = V(geo.CENTROID)
vertices = [V(p)-o for p in mesh.vertices]
s = sp.sqrt(2)-1; h = sp.sqrt(3)/6
B2 = sp.Rational(13, 12)-sp.sqrt(2)/2
v = sp.sqrt(B2-sp.Rational(1, 4)); w = sp.sqrt(3)/3
ez = V([0, 0, 1]); n = V([0, -1, 0]); t = V([1, 0, 0])
eq = lambda a, b: sp.simplify(a-b) == 0
check('18 welded vertices and three filled octagons', len(vertices)==18 and len(mesh.faces)==3, 'SOURCE FACT')
check('all centered vertices have radius B', all(eq(p.dot(p), B2) for p in vertices), 'DERIVED IDENTITY')
check('shell is not planar', sp.Matrix.hstack(*[p-vertices[0] for p in vertices[1:]]).rank()==3, 'DERIVED IDENTITY')
local = [V(p) for p in geo.LOCAL_OCTAGON]
turns = []
for j in range(8):
    a=local[(j+1)%8]-local[j]; b=local[(j+2)%8]-local[(j+1)%8]
    turns.append(sp.simplify(a[0]*b[1]-a[1]*b[0]))
check('local octagon has strictly positive corner turns', all(x.is_positive for x in turns), 'DERIVED IDENTITY')
check('native outward normals', mesh.face_normal(0)==(-sp.sqrt(3)/2, sp.Rational(1,2), 0)
      and mesh.face_normal(1)==(0,-1,0)
      and mesh.face_normal(2)==(sp.sqrt(3)/2, sp.Rational(1,2),0), 'SOURCE FACT')
check('h,v,w,B identities', eq(v*v, h*h+s*s/4) and eq(w*w,h*h+sp.Rational(1,4))
      and eq(B2,w*w+s*s/4), 'DERIVED IDENTITY')

C = sp.Matrix([[-sp.Rational(1,2),-sp.sqrt(3)/2,0], [sp.sqrt(3)/2,-sp.Rational(1,2),0],[0,0,1]])
Sv=sp.diag(-1,1,1); Sh=sp.diag(1,1,-1)
group = [sp.simplify(C**j*Sv**k*Sh**l) for j in range(3) for k in range(2) for l in range(2)]
check('D3h has 12 distinct matrices', len({str(g) for g in group})==12, 'DERIVED IDENTITY')
parallel = lambda a,b: all(eq(c,0) for c in a.cross(b))
check('vertical, normal and tangent unoriented axis orbits differ',
      not any(parallel(g*n,t) or parallel(g*n,ez) or parallel(g*t,ez) for g in group), 'DERIVED IDENTITY')


def Q(axis):
    x,y,z = axis
    return axis*axis.T+sp.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])


check('canonical quarter turns are proper rotations', all(Q(e).T*Q(e)==sp.eye(3) and Q(e).det()==1 for e in [ez,n,t]), 'DERIVED IDENTITY')
check('quarter-turn frame images', Q(n)*n==n and Q(n)*t==ez and Q(n)*ez==-t
      and Q(t)*n==-ez and Q(t)*ez==n and Q(ez)*n==t and Q(ez)*t==-n, 'DERIVED IDENTITY')
check('horizontal reflection conjugates horizontal quarter turns to inverses',
      Sh*Q(n)*Sh==Q(n).T and Sh*Q(t)*Sh==Q(t).T, 'DERIVED IDENTITY')

R,q,M,K = sp.symbols('R q M K', positive=True)
c = 1-q*q/4
Phi = (q*M+sp.sqrt(q*q*M*M+4*c*K))/(2*c)
check('sharp scale root solves containment quadratic', sp.simplify(c*Phi**2-q*M*Phi-K)==0, 'DERIVED IDENTITY')
u,z = sp.symbols('u z', real=True)
check('lens boundary squared-distance reversal', eq((u+q*R/2)**2+z*z-R*R,
      u*u+q*R*u+z*z-c*R*R), 'DERIVED IDENTITY')

axis_rows=[]
expected=[(sp.Rational(1,2),sp.Rational(1,3)),(w,sp.Rational(3,8)),(sp.Rational(1,2),B2)]
for (name,e),(max_ax, max_rad2) in zip([('ez',ez),('n_i',n),('t_i',t)],expected):
    aa=[sp.simplify(abs(p.dot(e))) for p in vertices]
    rr=[sp.simplify(p.dot(p)-p.dot(e)**2) for p in vertices]
    ma=max(aa,key=float); mr=max(rr,key=float)
    check('axis maxima '+name, eq(ma,max_ax) and eq(mr,max_rad2), 'DERIVED IDENTITY')
    axis_rows.append(dict(axis=name, M_axial=str(ma), M_radial_squared=str(mr),
                         axial_contacts=[i for i,a in enumerate(aa) if eq(a,ma)],
                         radial_contacts=[i for i,a in enumerate(rr) if eq(a,mr)]))

L = sp.symbols('L', nonnegative=True)
uu = sp.symbols('u', positive=True)
ell = (1+s)/2
rho = sp.sqrt(h*h+uu*uu)
f = (rho-L)**2+(ell-uu)**2
f2=4-2*L*h*h/(h*h+uu*uu)**sp.Rational(3,2)
f3=6*L*h*h*uu/(h*h+uu*uu)**sp.Rational(5,2)
check('chamfer second and third derivatives', eq(sp.diff(f,uu,2), f2) and eq(sp.diff(f,uu,3),f3), 'DERIVED IDENTITY')
check('chamfer left derivative starts negative for L>=0',
      eq(sp.diff(f,uu).subs(uu,s/2), s-1-L*s/v), 'DERIVED IDENTITY')
check('top midpoint/high-vertex sweep switch',
      eq(((L-h)**2+sp.Rational(1,4))-((L-v)**2+sp.Rational(1,4)),
      (v-h)*(2*L-v-h)), 'DERIVED IDENTITY')

mp.mp.dps=80
num=lambda x:mp.mpf(str(sp.N(x,85)))
bn=num(B2); hn=num(h); vn=num(v); wn=num(w); sn=num(s)
ph=lambda qq,mm,kk:(qq*mm+mp.sqrt(qq*qq*mm*mm+4*(1-qq*qq/4)*kk))/(2*(1-qq*qq/4))
fmt=lambda x:mp.nstr(x,30)
rev_rows=[]
for row in axis_rows:
    ma=num(sp.sympify(row['M_axial'])); mr=mp.sqrt(num(sp.sympify(row['M_radial_squared'])))
    for name,mm in [('centreline',ma),('chord',mr)]:
        rmin=ph(mp.mpf(1),mm,bn)
        residual=lambda rr:(1-mp.mpf(1)/4)*rr*rr-mm*rr-bn
        good=abs(residual(rmin))<mp.mpf('1e-75') and residual(rmin*(1-mp.mpf('1e-8')))<0
        rev_rows.append(dict(axis=row['axis'], lift=name, q=1, R_min=fmt(rmin), sharp=bool(good)))
check('six q=1 revolution thresholds with 80-digit arithmetic',all(a['sharp'] for a in rev_rows),'NUMERICAL EVIDENCE',rev_rows)
check('q=0 revolution threshold is B', abs(ph(mp.mpf(0),hn,bn)-mp.sqrt(bn))<mp.mpf('1e-75'), 'NUMERICAL EVIDENCE')

# Full-face sample: the same meridian describes every panel for vertical-axis hosts.
# This checks the written endpoint proof, and is not used in place of it.
ug=np.linspace(-.5,.5,401)
zg=np.minimum(.5,float(ell)-np.abs(ug))[:,None]*np.linspace(-1,1,41)[None,:]
rg=np.sqrt(float(h)**2+ug[:,None]**2)+np.zeros_like(zg)
sample_rows=[]
types=[('midpoint',hn,mp.mpf('.5')),('high_vertex',vn,mp.mpf('.5')),('seam_vertex',wn,sn/2)]
for kind,qq,ll in [('axial_centres',mp.mpf('.5'),mp.mpf(2)),
                   ('axial_centres',mp.mpf(1),mp.mpf(2)),
                   ('radial_centres',mp.mpf(1),mp.mpf(2)),
                   ('circular_tube',mp.mpf(0),mp.mpf(2))]:
    radii=[ph(qq, zz if kind=='axial_centres' else abs(rr-ll), (rr-ll)**2+zz**2)
           for _,rr,zz in types]
    rmin=max(radii); cc=1-qq*qq/4
    if kind=='axial_centres':
        lhs=(rg-float(ll))**2+(np.abs(zg)+float(qq*rmin/2))**2
        hole=ll-rmin*mp.sqrt(cc)
    else:
        lhs=(np.abs(rg-float(ll))+float(qq*rmin/2))**2+zg**2
        hole=ll-rmin*(1-qq/2)
    excess=float(np.max(lhs)-float(rmin*rmin))
    sharp=all(rr<=rmin for rr in radii)
    sample_rows.append(dict(kind=kind,q=fmt(qq),L=fmt(ll),R_min=fmt(rmin),
                            inner_equatorial_radius=fmt(hole),sample_count=int(zg.size),
                            sample_max_constraint_excess=excess,sharp=bool(sharp),
                            contacts=[types[i][0] for i,rr in enumerate(radii) if abs(rr-rmin)<mp.mpf('1e-70')]))
check('four bounded circular-sweep full-panel sample fixtures',
      all(r['sample_max_constraint_excess']<1e-12 and r['sharp'] for r in sample_rows), 'NUMERICAL EVIDENCE', sample_rows)
check('axial-centres sweep ring distinction q=.5 versus q=1',
      mp.mpf(sample_rows[0]['inner_equatorial_radius'])>0 and mp.mpf(sample_rows[1]['inner_equatorial_radius'])<0, 'NUMERICAL EVIDENCE')
check('radial-centres q=1 containing sweep can retain a hole', mp.mpf(sample_rows[2]['inner_equatorial_radius'])>0, 'NUMERICAL EVIDENCE')
check('historical Rmajor=2 rminor=.6 is not a containing torus for this registration',
      2-mp.mpf('.6')>wn and mp.mpf(sample_rows[3]['R_min'])>mp.mpf('.6'), 'DERIVED IDENTITY')

# Horizontal lens, extrusion direction ez; one bounded sharp containment fixture.
prism_radii=[]
for p in vertices:
    ka=p.dot(n)**2+p.dot(t)**2
    prism_radii.append(ph(mp.mpf(1),num(abs(p.dot(n))),num(ka)))
prism_min=max(prism_radii)
prism_margin=[mp.mpf('.75')*prism_min**2-num(abs(p.dot(n)))*prism_min-num(p.dot(n)**2+p.dot(t)**2) for p in vertices]
check('one exact-domain prism threshold fixture', min(prism_margin)>-mp.mpf('1e-75')
      and abs(min(prism_margin))<mp.mpf('1e-75'), 'NUMERICAL EVIDENCE', {'q':1,'H_min':'1/2','R_min':fmt(prism_min)})

after=dict(head=git('rev-parse','HEAD').strip(),status=git('status','--short'),
           index_sha256=sha(git('ls-files','--stage','-z').encode()),
           roots={path:inventory(Path(path)) for path in record['before']['roots']})
for key in ['head','status','index_sha256']:
    check('preserved Git '+key,after[key]==record['before'][key],'SOURCE FACT')
for path,info in after['roots'].items():
    check('preserved files '+path,info==record['before']['roots'][path],'SOURCE FACT')
report=OUT/'TL3_VESICA_3D_CONTAINMENT_SHELL.md'
record.update(after=after, checks=checks, total=len(checks), passed=sum(x['passed'] for x in checks),
              all_pass=all(x['passed'] for x in checks), constants={'s':str(s),'h':str(h),'B_squared':str(B2),'B':fmt(mp.sqrt(bn)),
              'rho_high':fmt(vn),'rho_seam':fmt(wn)},axes=axis_rows,
              report_sha256=sha(report.read_bytes()) if report.exists() else None,
              script_sha256=sha(Path(__file__).read_bytes()), protected_file_count=sum(a['files'] for a in after['roots'].values()))
RESULT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':record['passed'],'total':len(checks),'all_pass':record['all_pass'],
                  'protected_files':record['protected_file_count'],'failed':[x['name'] for x in checks if not x['passed']],
                  'revolutions':rev_rows,'sweeps':sample_rows},indent=2))
raise SystemExit(0 if record['all_pass'] else 1)
