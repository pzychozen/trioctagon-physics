"""Re-render only the established exact mesh; no geometry/dynamics modification."""
from pathlib import Path
import importlib.util
import json
import sys
import hashlib
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d import proj3d

ROOT=Path(__file__).resolve().parents[1]
src=ROOT/'measurement/supplement/native/kernel_physics/geometry.py'
spec=importlib.util.spec_from_file_location('exact_figure_geometry',src)
geo=importlib.util.module_from_spec(spec);sys.modules[spec.name]=geo;spec.loader.exec_module(geo)
mesh=geo.folded_module()
assert len(geo.LOCAL_OCTAGON)==8 and len(set(geo.LOCAL_OCTAGON))==8
assert len(mesh.faces)==3 and len(mesh.vertices)==18
assert all(len(f)==len(set(f))==8 for f in mesh.faces)
assert len(mesh.edges)==21 and len(mesh.seam_edges)==3
assert len(mesh.boundary_edges)==18
assert all(len(loop)==9 for loop in mesh.boundary_loops)
for panel,face in enumerate(mesh.faces,1):
    assert tuple(mesh.vertices[i] for i in face)==tuple(geo.panel_point(panel,*uv) for uv in geo.LOCAL_OCTAGON)
    for i,j in zip(face,face[1:]+face[:1]):
        d=sp.Matrix(mesh.vertices[i])-sp.Matrix(mesh.vertices[j])
        assert sp.simplify(d.dot(d)-geo.EDGE_LENGTH**2)==0
center=sp.Matrix(geo.CENTROID)
xyz=np.array([list(sp.Matrix(v)-center) for v in mesh.vertices],dtype=float)
local=np.array(geo.LOCAL_OCTAGON,dtype=float)

# Show every edge as an explicit line, independent of face-fill depth sorting.
# Orthographic projection avoids perspective foreshortening changes of scale.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,'svg.fonttype':'none','svg.hashsalt':'measurement-v0.1.1'})
fig=plt.figure(figsize=(8,6.2))
gs=fig.add_gridspec(3,2,width_ratios=[3.1,1],left=.015,right=.985,bottom=.08,top=.91,wspace=.12,hspace=.30)
ax=fig.add_subplot(gs[:,0],projection='3d',computed_zorder=False)
ax.set_proj_type('ortho')
colors=['#236992','#b14822','#408448']
gold='#ab853b'
theta=np.linspace(0,2*np.pi,361);R=1/np.sqrt(3)
for z in [-.5,.5]:
    ax.plot(R*np.cos(theta),R*np.sin(theta),np.full_like(theta,z),c=gold,lw=1.05,ls='--',zorder=1)
for th in np.deg2rad([0,90,180,270]):
    ax.plot([R*np.cos(th)]*2,[R*np.sin(th)]*2,[-.5,.5],c=gold,lw=.75,ls=':',zorder=1)
line_records=[];point_records=[]
for panel,(face,color) in enumerate(zip(mesh.faces,colors),1):
    for j,(a,b) in enumerate(zip(face,face[1:]+face[:1]),1):
        line=ax.plot(*xyz[[a,b]].T,c=color,lw=1.65,alpha=1,zorder=3)[0]
        line_records.append({'panel':panel,'local_edge':j,'global_endpoints':[a,b],'alpha':line.get_alpha(),'data_points':len(line.get_data_3d()[0])})
    for j,index in enumerate(face,1):point_records.append({'panel':panel,'local_vertex':j,'global_vertex':index})
    inset=fig.add_subplot(gs[panel-1,1])
    inset.add_patch(Polygon(local,closed=True,facecolor='none',edgecolor=color,lw=1.7))
    inset.scatter(*local.T,c=color,s=16,zorder=3)
    for j,uv in enumerate(local,1):
        inset.text(*(uv*1.18),str(j),ha='center',va='center',fontsize=8.5,color=color)
    inset.set(xlim=(-.73,.73),ylim=(-.72,.72),aspect='equal')
    inset.axis('off');inset.set_title(f'{chr(64+panel)} = P{panel}: local vertices 1–8',fontsize=9.5,pad=0,color=color)
ax.scatter(*xyz.T,s=15,c='#203440',alpha=1,depthshade=False,zorder=5)
ax.scatter([0],[0],[0],s=15,c='black',depthshade=False,zorder=5)
ax.text(0,0,.035,'o',fontsize=10,zorder=6)
ax.set(xlabel=r'$X-o_x$',ylabel=r'$Y-o_y$',zlabel=r'$z$',xlim=(-.68,.68),ylim=(-.68,.68),zlim=(-.60,.60))
ax.set_xticks([-.5,0,.5]);ax.set_yticks([-.5,0,.5]);ax.set_zticks([-.5,0,.5])
ax.set_box_aspect([1.36,1.36,1.2]);ax.view_init(24,-102)
ax.grid(False)
for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.pane.fill=False;axis.pane.set_edgecolor('#e1e5e8')
fig.suptitle('Three octagonal panels in the static measurement cylinder',fontsize=13,y=.975)
fig.text(.36,.905,'All shell edges shown; no face fill or hidden-edge removal',ha='center',fontsize=9,color='#39434b')
fig.text(.49,.025,'Solid colours: A / B / C panels     •     Black dots: 18 welded vertices     •     Dashed gold: measurement guides',ha='center',fontsize=9)
fig.canvas.draw()
projection=np.array(proj3d.proj_transform(*xyz.T,ax.get_proj())[:2]).T
projected_separations=[float(np.linalg.norm(projection[i]-projection[j])) for i in range(18) for j in range(i)]
assert min(projected_separations)>1e-4
assert len(line_records)==24 and all(r['data_points']==2 and r['alpha']==1 for r in line_records)
assert {r['global_vertex'] for r in point_records}==set(range(18))
assert {tuple(sorted(r['global_endpoints'])) for r in line_records}==set(mesh.edges)
for fmt in ['pdf','svg','png']:
    meta={'CreationDate':None,'ModDate':None,'Creator':'Measurement Geometry v0.1.1 exact mesh rendering'} if fmt=='pdf' else ({'Date':None} if fmt=='svg' else None)
    destination=ROOT/'measurement/figures'/f'scaffold.{fmt}' if fmt!='png' else ROOT/'qa/corrected_figure.png'
    fig.savefig(destination,dpi=180,metadata=meta)
plt.close(fig)
report={'classification':'DERIVED IDENTITY / bounded rendering verification; established geometry unchanged',
        'geometry_source':'measurement/supplement/native/kernel_physics/geometry.py','geometry_source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
        'ordered_local_vertices':[[str(a),str(b)] for a,b in geo.LOCAL_OCTAGON],
        'global_vertices_exact':[[str(v) for v in vertex] for vertex in mesh.vertices],
        'face_cycles':[list(f) for f in mesh.faces],
        'faces':3,'vertices_per_face':[8,8,8],'local_vertex_incidences':24,'welded_vertices':18,'unique_edges':21,'shared_seams':3,'boundary_edges':18,'boundary_loop_lengths':[9,9],
        'all_panel_edge_lengths_exact':str(geo.EDGE_LENGTH),'exact_panel_map_order_verified':True,
        'rendered_edge_incidences':line_records,'rendered_local_vertex_incidences':point_records,
        'projection':'orthographic; elevation 24 degrees; azimuth -102 degrees',
        'minimum_pairwise_projected_vertex_distance':min(projected_separations),
        'all_global_vertices_distinct_in_projection':True,'polygon_fill_used':False,'edge_and_vertex_alpha':1,'hidden_edge_culling':False,
        'local_insets':'Three ordered material-plane octagons, vertices 1 through 8 each; not exploded/repositioned physical panels',
        'old_rendering':'Old script supplied all eight vertices on all three faces; a nearly edge-on panel and overlapping translucent fills made the outline ambiguous. No missing mathematical vertex was found.',
        'status':'PASS'}
(ROOT/'results/figure_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','faces','vertices_per_face','welded_vertices','unique_edges','shared_seams','all_global_vertices_distinct_in_projection','minimum_pairwise_projected_vertex_distance']},indent=2))
