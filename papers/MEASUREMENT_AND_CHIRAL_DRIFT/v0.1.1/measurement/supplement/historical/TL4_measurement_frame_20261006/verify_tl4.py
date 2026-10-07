# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""External TL4 exact checks and one static measurement diagram.
Run with python -X utf8 -B.
Imports only the two pure geometry modules, suppresses bytecode, and never
executes a historical display, simulation, source builder or predecessor test.
Writes only this lane's results JSON and optional PNG (--figure).
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
sys.dont_write_bytecode = True
import sympy as sp

ROOT=Path('project-source')
REPO=ROOT/'trioctagon-physics'
OUT=Path(__file__).resolve().parent
assert OUT==ROOT/'research/TL4_measurement_frame_20261006'
RESULT=OUT/'TL4_RESULTS.json'
record=json.loads(RESULT.read_text(encoding='utf8'))
checks=[]

def check(name,value,kind='DERIVED IDENTITY',details=None):
    checks.append(dict(name=name,passed=bool(value),evidence=kind,details=details))

def eq(a,b=0):return sp.simplify(a-b)==0
def veq(a,b):return all(eq(x,y) for x,y in zip(a,b))
def sha(b):return hashlib.sha256(b).hexdigest()
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args]).decode('utf8')
def inventory(path):
    rows={};total=0
    for p in sorted(path.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(path).parts and not p.is_relative_to(OUT):
            b=p.read_bytes();rows[p.relative_to(path).as_posix()]=sha(b);total+=len(b)
    return dict(files=len(rows),bytes=total,sha256=sha(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()))

geo=load_module('tl4_geometry',REPO/'kernel_physics/geometry.py')
rs=load_module('tl4_scaffold',REPO/'kernel_physics/reference_scaffold.py')
V=sp.Matrix;s=sp.sqrt(2)-1;a=sp.Rational(1,2);h=sp.sqrt(3)/6
lam=(1+sp.sqrt(2))/3;Rmin=sp.sqrt(3)/3;v=sp.sqrt(sp.Rational(5,6)-sp.sqrt(2)/2)
R8=sp.sqrt(1-sp.sqrt(2)/2);ell=1/sp.sqrt(2)
mesh=geo.folded_module();o=V(geo.CENTROID)
verts=[V(p)-o for p in mesh.vertices];ez=V([0,0,1])
normals=[V(mesh.face_normal(i)) for i in range(3)]
tangents=[ez.cross(n) for n in normals]
check('source width and centre',geo.WIDTH==1 and veq(o,[0,h,0]),'SOURCE FACT')
check('octagon radius apothem side identity',eq(R8**2,a*a+s*s/4) and eq((1+sp.sqrt(2))*s,1))
check('cylinder radial bound and attainment',all((sp.Rational(1,3)-p[0]**2-p[1]**2).is_nonnegative for p in verts)
      and any(eq(p[0]**2+p[1]**2,sp.Rational(1,3)) for p in verts))
check('cylinder height bound and attainment',all(abs(p[2])<=a for p in verts) and any(abs(p[2])==a for p in verts))
check('centre inclusion',h>0 and Rmin>0 and a>0)
top=[p for p in verts if p[2]==a]
check('highest source vertices lie strictly inside top ring',all(eq(p[0]**2+p[1]**2,v*v) and (Rmin*Rmin-v*v).is_positive for p in top))
check('face centres follow native normal rays',all(veq(sum((V(mesh.vertices[j]) for j in f),sp.zeros(3,1))/8-o,h*n)
      for f,n in zip(mesh.faces,normals)))
seam_mid=[(V(mesh.vertices[j])+V(mesh.vertices[k]))/2-o for j,k in mesh.seam_edges]
check('seam rays are opposite normal rays',all(any(veq(p,-2*h*n) for n in normals) for p in seam_mid))
check('seams have only vertical spatial directions',all(veq((V(mesh.vertices[j])-V(mesh.vertices[k])).cross(ez),[0,0,0]) for j,k in mesh.seam_edges))
check('three normal axes distinct from three tangent axes',all(n.cross(t)!=sp.zeros(3,1) for n in normals for t in tangents))
check('tangent definition',all(veq(ez.cross(n),t) and eq(n.dot(t)) and eq(t.dot(t),1) for n,t in zip(normals,tangents)))

old_dir=REPO/'research_files/verification/actual_geometry'
old=json.loads((old_dir/'tri_octagon_actual.json').read_text())
new=json.loads((old_dir/'width_1/tri_octagon_actual.json').read_text())
getp=lambda row:V([sp.sympify(row[k+'_exact']) for k in ['x','y','z']])
check('18 archived vertices scale exactly from side one to width one',len(old['vertices'])==len(new['vertices'])==18
      and all(veq(s*getp(x),getp(y)) for x,y in zip(old['vertices'],new['vertices'])),'SOURCE FACT')
check('archived canonical vertex set equals current source',{str(p) for p in map(getp,new['vertices'])}=={str(V(p)) for p in mesh.vertices},'SOURCE FACT')
history=json.loads((old_dir/'width_1/normalization_history.json').read_text())
check('normalization receipt confirms similarity only',eq(sp.sympify(history['uniform_coordinate_multiplier_exact']),s)
      and history['translation']==[0,0,0] and history['rotation']=='identity','SOURCE FACT')

orig=rs.paper_c_member(s);shrunk=rs.shrink_paper_c_at_fixed_centres(s);moved=rs.translate_paper_c_to_regular(s)
check('current top polygon is alternating',eq(orig.p,h) and eq(orig.g_gap,s/sp.sqrt(2)) and eq(orig.circumradius_squared,v*v))
check('fixed centre shrink exact lambda',eq(rs.PAPER_C_SHRINK_FACTOR,lam) and eq(shrunk.s,sp.Rational(1,3))
      and eq(shrunk.g_gap,sp.Rational(1,3)) and eq(shrunk.p,h))
check('shrink height and width change',eq(shrunk.octagon.a,lam/2) and eq(shrunk.octagon.w,lam)
      and eq(shrunk.circumradius_squared,sp.Rational(1,9)))
check('translation has same octagon size and different centre radius',eq(moved.s,s) and eq(moved.p,sp.sqrt(3)*s/2) and eq(moved.octagon.a,a))
check('two regular alternatives are globally similar to one another',all(veq(V(p),lam*V(q))
      for f,g in zip(shrunk.vertical_frames,moved.vertical_frames) for p,q in zip(f.vertices,g.vertices)))
check('shrink loses original seams', (sp.sqrt(3)*shrunk.p-shrunk.octagon.a).is_positive)
sc=sp.symbols('scale',positive=True)
check('global rescale cannot regularize original top hexagon',eq((sp.sqrt(3)*sc*h-sc*s/2)/(sc*s),1/sp.sqrt(2)))

N=[V(p) for p in rs.RADIAL];T=[V(p) for p in rs.TANGENT]
Rot60=V([[sp.Rational(1,2),-sp.sqrt(3)/2],[sp.sqrt(3)/2,sp.Rational(1,2)]])
check('connector normal rays are negatives of selected normal rays',all(any(veq(Rot60*n,-m) for m in N) for n in N))
check('connector edge rays are negatives of selected tangent rays',all(any(veq(Rot60*t,-u) for u in T) for t in T))
ss,gg=sp.symbols('s g',positive=True)
gen=rs.ReferenceScaffold(ss,gg)
check('generic endpoint circumcircle',all(eq(V(p).dot(V(p)),gen.p**2+ss**2/4) for p in gen.vertices))
check('generic connector direction and length',all(veq(V(B)-V(A),gg*Rot60*T[i]) for i,(A,B) in enumerate(gen.connectors)))
reg=rs.ReferenceScaffold.regular(ss)
check('regular vertex rays share tangent unoriented axes',all(any(eq(V(p)[0]*t[1]-V(p)[1]*t[0]) for t in T) for p in reg.vertices))
check('vertical frame cylinder radius identity',eq(gen.p**2+gen.octagon.a**2,gen.p**2+((1+sp.sqrt(2))*ss/2)**2))
check('outer planar frame maximum selects outward flat endpoints',
      sp.simplify((gen.L+gen.octagon.a)**2+ss**2/4-(gen.L+ss/2)**2-gen.octagon.a**2).is_positive)

# Exact set-level side-projection proof is in the report. These verify its
# interval-overlap margin and the piecewise boundary breakpoints.
check('side projected panel intervals always overlap', (s/2-sp.Rational(1,6)).is_positive)
check('side projection corner formula',eq(sp.Rational(1,4)+(s/2)/2,1/(2*sp.sqrt(2)))
      and eq(sp.Rational(1,4)+a/2,a))
check('projection matrices contract and forget depth',sp.diag(1,1,0)**2==sp.diag(1,1,0)
      and sp.diag(1,0,1)**2==sp.diag(1,0,1))
Qa=V([[1,0,0],[0,0,-1],[0,1,0]])
E=V([[1,0],[0,1],[0,0]])
check('active eye quarter turn collapses in old view', E.T*Qa*E==sp.diag(1,0))
check('co-rotated view preserves eye coordinates', (Qa*E).T*Qa*E==sp.eye(2))
check('static eye viewed from perpendicular plane also collapses', (Qa*E).T*E==sp.diag(1,0))
check('generic lens proper half-turn stabilizers', all(g.det()==1 for g in [sp.eye(3),sp.diag(1,-1,-1),sp.diag(-1,1,-1),sp.diag(-1,-1,1)]))
check('literal .544 is not any recovered principal quantity', all(not eq(x,sp.Rational(544,1000)) for x in [R8,Rmin,v,lam,s,h]))

values={
 'octagon_side':s,'octagon_apothem':a,'octagon_circumradius':R8,'octagon_vertex_diameter':2*R8,
 'face_centre_radius':h,'cylinder_radius':Rmin,'cylinder_diameter':2*Rmin,'cylinder_half_height':a,
 'top_hex_radius':v,'top_hex_connector':s/sp.sqrt(2),'shrink_factor':lam,
 'shrunk_half_height':lam/2,'shrunk_full_frame_cylinder_radius':sp.sqrt(h*h+(lam/2)**2),
 'translated_full_frame_cylinder_radius':sp.sqrt(moved.p**2+a*a),
 'old_side_one_cylinder_radius':(1+sp.sqrt(2))/sp.sqrt(3),'old_side_one_half_height':(1+sp.sqrt(2))/2,
 'endpoint_half_angle_degrees':sp.atan(sp.sqrt(3)*s)*180/sp.pi}
tables={key:dict(exact=str(sp.simplify(x)),decimal=str(sp.N(x,30))) for key,x in values.items()}

if '--figure' in sys.argv:
    # Reuse installed matplotlib; keep its transient cache outside protected trees.
    import os,tempfile
    with tempfile.TemporaryDirectory(prefix='tl4_plot_') as cache:
        os.environ['MPLCONFIGDIR']=cache
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle,Polygon,Rectangle
        import numpy as np
        fig,axs=plt.subplots(1,3,figsize=(15,5.2),layout='constrained')
        blue='#196a9a';orange='#c16a1b';red='#b24855';green='#477345'
        pp=np.array([[float(c) for c in p] for p in verts])
        ns=np.array(normals,dtype=float)[:,:,0]
        def setup(ax):
            ax.set_aspect('equal');ax.grid(alpha=.15);ax.axhline(0,c='.8',lw=.6);ax.axvline(0,c='.8',lw=.6)
            ax.set_xlim(-.7,.7);ax.set_ylim(-.65,.7)
        ax=axs[0];setup(ax)
        ax.add_patch(Circle((0,0),float(Rmin),fill=False,color=green,lw=1.8,label='Measurement top ring projected'))
        for face in mesh.faces:
            pts=pp[list(face),:2];ax.plot(pts[:,0],pts[:,1],color=blue,lw=2)
        nh=[]
        for nv,tv in zip(normals,tangents):
            A=h*nv-s*tv/2;B=h*nv+s*tv/2;nh.extend([A,B])
        xy=np.array([[float(p[0]),float(p[1])] for p in nh]);xy=np.vstack([xy,xy[0]])
        ax.plot(xy[:,0],xy[:,1],'--',color=orange,lw=1.5,label='Top measurement hexagon')
        for j,nv in enumerate(ns):
            ax.annotate('',xy=.25*nv[:2],xytext=(0,0),arrowprops=dict(arrowstyle='->',color=blue,lw=1.3))
            ax.annotate('',xy=-.48*nv[:2],xytext=(0,0),arrowprops=dict(arrowstyle='->',color=red,lw=1.3,linestyle='--'))
        ax.scatter([0],[0],s=18,c='k',zorder=6)
        ax.set_title('Top view of unchanged shell\nBlue: normal rays   Red: opposite seam rays',fontsize=10)
        ax.set_xlabel('centred x');ax.set_ylabel('centred y')
        ax.legend(fontsize=7,loc='lower left')
        ax=axs[1];setup(ax)
        ax.add_patch(Rectangle((-float(Rmin),-.5),2*float(Rmin),1,fill=False,edgecolor=green,lw=1.8))
        for face in mesh.faces:
            pts=pp[list(face)][:,[0,2]];ax.add_patch(Polygon(pts,closed=True,facecolor=blue,edgecolor=blue,alpha=.19))
        ax.plot([-float(Rmin),float(Rmin)],[.5,.5],color=green,lw=2.7,label='Top ring projects to a segment')
        ax.set_title('Side view along a face normal\nSame 3D shell and measurement cylinder',fontsize=10)
        ax.set_xlabel('coordinate along tangent');ax.set_ylabel('z')
        ax.legend(fontsize=7,loc='lower left')
        ax=axs[2];setup(ax)
        for nv in ns:
            tv=np.array([-nv[1],nv[0],0])
            A=float(h)*nv[:2]-tv[:2]/6;B=float(h)*nv[:2]+tv[:2]/6
            ax.plot([A[0],B[0]],[A[1],B[1]],color=blue,lw=2.5)
        hexpts=[]
        for nv in ns:
            tv=np.array([-nv[1],nv[0],0]);hexpts.extend([float(h)*nv[:2]-tv[:2]/6,float(h)*nv[:2]+tv[:2]/6])
        hp=np.array(hexpts+[hexpts[0]]);ax.plot(hp[:,0],hp[:,1],'--',color=orange,lw=1.5)
        for nv in ns:
            tv=np.array([-nv[1],nv[0],0]);ax.annotate('',xy=.49*tv[:2],xytext=(0,0),arrowprops=dict(arrowstyle='->',color=blue,lw=1.3))
            ax.annotate('',xy=-.49*tv[:2],xytext=(0,0),arrowprops=dict(arrowstyle='->',color=orange,linestyle='--',lw=1.3))
        ax.add_patch(Circle((0,0),1/3,fill=False,edgecolor='.45',lw=.8))
        ax.set_title('Separate regular reference hexagon\nSix vertex rays on three tangent axes',fontsize=10)
        ax.set_xlabel('centred x');ax.set_ylabel('centred y')
        fig.suptitle('TL4 measurement geometry and projections | width-one units',fontsize=13)
        fig.savefig(OUT/'TL4_MEASUREMENT_VIEWS.png',dpi=170)
        plt.close(fig)

after=dict(head=git('rev-parse','HEAD').strip(),status=git('status','--short'),
           index_sha256=sha(git('ls-files','--stage','-z').encode()),
           roots={path:inventory(Path(path)) for path in record['before']['roots']})
for key in ['head','status','index_sha256']:
    check('preserved Git '+key,after[key]==record['before'][key],'SOURCE FACT')
for path,data in after['roots'].items():check('preserved '+path,data==record['before']['roots'][path],'SOURCE FACT')
report=OUT/'TL4_MEASUREMENT_CYLINDER_AND_DIRECTIONAL_FRAME.md'
record.update(after=after,checks=checks,tables=tables,total=len(checks),passed=sum(c['passed'] for c in checks),
              all_pass=all(c['passed'] for c in checks),protected_file_count=sum(x['files'] for x in after['roots'].values()),
              report_sha256=sha(report.read_bytes()) if report.exists() else None,
              script_sha256=sha(Path(__file__).read_bytes()))
RESULT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':record['passed'],'total':record['total'],'failed':[c['name'] for c in checks if not c['passed']],
                  'protected_files':record['protected_file_count'],'tables':tables},indent=2))
raise SystemExit(0 if record['all_pass'] else 1)
