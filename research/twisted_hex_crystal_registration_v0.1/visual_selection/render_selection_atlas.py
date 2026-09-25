"""Visual selection only: import the verified family, never run its build().
All writes are confined to this subfolder. No model evolution or fitting.
"""
from pathlib import Path
import datetime, hashlib, itertools, json, os, sys

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(PARENT))
# Keep Matplotlib's generated cache inside this new output folder as well.
os.environ.setdefault("MPLCONFIGDIR",str(HERE/"render_cache"))

import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
import verify_host_registration as family

BLUE="#1768ab"; ORANGE="#c45d22"; TEAL="#197e80"; HOST="#6d8295"
VIEWS=("perspective","top","side")
LABELS=("0","s/16","s/8","s/6","3s/16","s/4","s/3","3s/8","s/2")
RATIOS=(sp.Integer(0),sp.Rational(1,16),sp.Rational(1,8),sp.Rational(1,6),
        sp.Rational(3,16),sp.Rational(1,4),sp.Rational(1,3),sp.Rational(3,8),sp.Rational(1,2))
CAMERA={"elevation_degrees":22,"azimuth_degrees":-65,"perspective_distance":3.0,
        "projected_bounds":[-.72,.72],"side_direction":"from -y toward +y; screen x=x, screen y=z",
        "top_direction":"from +z toward -z; screen x=x, screen y=y",
        "center":"accepted host O; all views use identical world scale and no per-sample autoscaling"}
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.titlesize":11,
                     "figure.facecolor":"white","axes.spines.top":False,"axes.spines.right":False,
                     "savefig.dpi":170})

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(name,value):(HERE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
def mat(points):return [sp.Matrix([sp.sympify(v) for v in p]) for p in points]
def numeric(points):return np.array([[float(v) for v in p] for p in points])
def zero(v):return all(sp.simplify(x)==0 for x in v)
def sexpr(v):
    if isinstance(v,sp.MatrixBase):return [str(sp.simplify(x)) for x in v]
    return str(sp.simplify(v))

def load_data():
    for line in (PARENT/"SHA256SUMS.txt").read_text(encoding="utf8").splitlines():
        expected,rel=line.split("  ",1)
        assert sha(PARENT/rel)==expected, f"Verified packet changed: {rel}"
    source=json.loads((PARENT/"CANONICAL_CRYSTAL_CANDIDATE.json").read_text(encoding="utf8"))
    host=json.loads((PARENT/"HOST_GEOMETRY.json").read_text(encoding="utf8"))
    O=sp.Matrix([sp.sympify(x) for x in host["center"]])
    upper=mat(host["upper_targets"]);lower=mat(host["lower_targets"])
    normal=[sp.Matrix([sp.sympify(x) for x in p["outward_normal"][:2]]) for p in host["plane_equations"]]
    panels=[mat(p["vertices"]) for p in host["panels"]]
    faces=family.candidate_faces()
    assert faces==source["variants"][0]["faces"]==source["variants"][1]["faces"]
    symbolic=family.canonical_points()
    stored=[sp.Matrix([sp.sympify(x,locals={"t":family.T}) for x in p]) for p in source["symbolic_physical_centered_vertices"]]
    assert all(zero(a-b) for a,b in zip(symbolic,stored))
    base=[p.subs(family.T,0)+O for p in symbolic]
    slope=[p.diff(family.T) for p in symbolic]
    assert all(zero(p+O-a-family.T*b) for p,a,b in zip(symbolic,base,slope))
    alpha=sp.sympify(source["alpha"],locals={"t":family.T})
    delta=sp.sympify(source["delta_plus"],locals={"t":family.T})
    samples=[]
    for index,(label,ratio) in enumerate(zip(LABELS,RATIOS)):
        t=family.S*ratio
        item={"id":f"{index:02d}","label":label,"ratio_of_s":str(ratio),
              "t_exact":str(t),"t":float(t),"alpha_exact":str(sp.simplify(alpha.subs(family.T,t))),
              "alpha":float(alpha.subs(family.T,t)),
              "delta_magnitude_radians_exact":str(delta.subs(family.T,t)),
              "delta_magnitude_degrees":float(delta.subs(family.T,t)*180/sp.pi),
              "reference_only":index==0,"designated_canonical":False,"hands":{}}
        for hand,name in ((1,"TWIST_PLUS"),(-1,"TWIST_MINUS")):
            points=[p+O for p in family.canonical_points(t,hand)]
            perm=source["variants"][0 if hand==1 else 1]["target_correspondence"]
            checks=[]
            for k,target in enumerate(perm):
                A=points[12+k];B=points[15+k];n=normal[target]
                lowerdiff=B-lower[target]
                projection=(family.J*n).dot(lowerdiff[:2,0])
                entry={"apex_index":k,"host_target":target,
                       "upper_contact_exact":zero(A-upper[target]),
                       "lower_plane_exact":sp.simplify(n.dot((B-O)[:2,0])-family.R0)==0,
                       "lower_height_exact":sp.simplify(B[2]+sp.Rational(1,2))==0,
                       "lower_on_finite_edge":bool(sp.simplify(sp.Abs(projection)-family.S/2)<=0),
                       "lower_center_residual_squared_exact":sp.simplify(lowerdiff.dot(lowerdiff)-t**2)==0,
                       "signed_edge_coordinate_exact":str(sp.simplify(projection))}
                assert all(entry[key] for key in ("upper_contact_exact","lower_plane_exact","lower_height_exact","lower_on_finite_edge","lower_center_residual_squared_exact"))
                checks.append(entry)
            vf=numeric(points)
            affine=numeric(base)+float(t)*numeric(slope)
            if hand==-1:affine[:,0]=2*float(O[0])-affine[:,0]
            error=float(np.max(abs(vf-affine)));assert error<1e-14
            item["hands"][name]={"delta_degrees":hand*item["delta_magnitude_degrees"],
                "vertices_exact":[sexpr(p) for p in points],"vertices":vf.tolist(),
                "target_correspondence":perm,"contacts":checks,"affine_render_parity_max_error":error}
        samples.append(item)
    model={"samples":samples,"faces":faces,"host_panels":numeric_panels(panels),
           "center":[float(x) for x in O],"upper_targets":numeric(upper).tolist(),
           "lower_targets":numeric(lower).tolist(),"max_t":float(family.S/2),"s":float(family.S),
           "vertex_affine_base":numeric(base).tolist(),"vertex_affine_slope":numeric(slope).tolist(),
           "camera":CAMERA}
    output={"purpose":"VISUAL_SELECTION_ONLY_NO_PREFERRED_VALUE_OR_HAND",
            "source_identities":{name:sha(PARENT/name) for name in ("verify_host_registration.py","verify_crystal_geometry.py","CANONICAL_CRYSTAL_CANDIDATE.json","HOST_GEOMETRY.json","SHA256SUMS.txt")},
            "controlling_domain":"0 <= t <= (sqrt(2)-1)/2; zero is reference only",
            "zero_note":"At zero, alpha=1 and relative footprint delta=0. The unchanged face list still has one-step cross-ring connectivity; this is not an untwisted replacement mesh.",
            "sample_count":len(samples),"samples":samples,"camera":CAMERA,
            "surface_topology":"Unchanged verified candidate_faces; no alternative geometry introduced",
            "all_upper_contacts_exact":True,"all_nonzero_lower_edge_contacts_exact":True,
            "upper_contact_count":54,"nonzero_lower_contact_count":48,
            "any_value_designated_canonical":False,"any_handedness_designated_canonical":False,
            "affine_coefficients_exact":{"base":[sexpr(p) for p in base],"slope":[sexpr(p) for p in slope]},
            "alpha_source_expression":str(alpha),"delta_source_expression":str(delta)}
    dump("candidate_values.json",output)
    return model,output,sp.jscode(alpha),sp.jscode(delta)

def numeric_panels(panels):return [numeric(p).tolist() for p in panels]

def project(points,view,center):
    p=np.asarray(points)-np.array(center)
    if view=="top":return p[:,[0,1]],p[:,2]
    if view=="side":return p[:,[0,2]],-p[:,1]
    az=np.deg2rad(CAMERA["azimuth_degrees"]);el=np.deg2rad(CAMERA["elevation_degrees"])
    right=np.array([-np.sin(az),np.cos(az),0])
    up=np.array([-np.sin(el)*np.cos(az),-np.sin(el)*np.sin(az),np.cos(el)])
    toward=np.array([np.cos(el)*np.cos(az),np.cos(el)*np.sin(az),np.sin(el)])
    depth=p@toward
    xy=np.column_stack([p@right,p@up])/(1-depth[:,None]/CAMERA["perspective_distance"])
    return xy,depth

def add_marker(ax,xy,color,marker,size,z):
    ax.scatter(xy[:,0],xy[:,1],s=size,marker=marker,c=color,edgecolors="white",linewidths=.65,zorder=z)

def draw(ax,model,sample,hand,view,title=True):
    points=np.array(sample["hands"][hand]["vertices"])
    pr,depth=project(points,view,model["center"])
    poly=[]
    for p in model["host_panels"]:
        xy,d=project(p,view,model["center"]);poly.append((float(np.mean(d)),xy,HOST,.09,.6))
    for i,f in enumerate(model["faces"]):
        poly.append((float(np.mean(depth[f])),pr[f],TEAL if i<12 else BLUE,.20,.45))
    for _,xy,col,opacity,width in sorted(poly,key=lambda p:p[0]):
        ax.add_patch(Polygon(xy,closed=True,facecolor=col,edgecolor=col,alpha=opacity,linewidth=width,zorder=1))
    # All panel borders and crystal wire lines are deliberately readable through surfaces.
    for p in model["host_panels"]:
        xy,_=project(p,view,model["center"]);xy=np.vstack([xy,xy[0]])
        ax.plot(*xy.T,color=HOST,lw=.7,alpha=.60,zorder=2)
    edges=set(tuple(sorted(e)) for f in model["faces"] for e in zip(f,f[1:]+f[:1]))
    for a,b in sorted(edges):ax.plot(*pr[[a,b]].T,color=TEAL,lw=.60,alpha=.80,zorder=3)
    for start in (0,6):
        idx=list(range(start,start+6))+[start]
        ax.plot(*pr[idx].T,color="#164955",lw=1.1,zorder=4)
    U,_=project(model["upper_targets"],view,model["center"])
    L,_=project(model["lower_targets"],view,model["center"])
    perm=sample["hands"][hand]["target_correspondence"]
    for k,target in enumerate(perm):
        ax.plot(*np.vstack([L[target],pr[15+k]]).T,color=ORANGE,lw=1.4,ls=(0,(3,2)),zorder=5)
    ax.scatter(U[:,0],U[:,1],s=90,marker="s",facecolors="white",edgecolors="#44545f",linewidths=1,zorder=6)
    ax.scatter(L[:,0],L[:,1],s=90,marker="s",facecolors="white",edgecolors="#44545f",linewidths=1,zorder=6)
    add_marker(ax,pr[12:15],BLUE,"o",65,7)
    add_marker(ax,pr[15:18],ORANGE,"D",16,8)
    ax.plot([0],[0],marker="+",color="#4a5966",markersize=4,zorder=5)
    ax.set_xlim(*CAMERA["projected_bounds"]);ax.set_ylim(*CAMERA["projected_bounds"])
    ax.set_aspect("equal");ax.set_xticks([]);ax.set_yticks([])
    for spine in ax.spines.values():spine.set_visible(False)
    if title:ax.set_title({"perspective":"Perspective","top":"Exact top projection (+z)","side":"Exact side projection (-y)"}[view],fontsize=10,pad=0)
    if view!="perspective":
        xlabel,ylabel=("x","y") if view=="top" else ("x","z")
        ax.text(.89,.08,xlabel,transform=ax.transAxes,color="#5b6b78",fontsize=9)
        ax.text(.08,.89,ylabel,transform=ax.transAxes,color="#5b6b78",fontsize=9)

def legend(fig,y,fontsize=9):
    items=[Line2D([0],[0],marker="o",color="none",markerfacecolor=BLUE,markeredgecolor="white",label="Upper contact"),
           Line2D([0],[0],marker="D",color="none",markerfacecolor=ORANGE,markeredgecolor="white",label="Predicted lower contact"),
           Line2D([0],[0],marker="s",color="none",markeredgecolor="#44545f",markerfacecolor="white",label="Host edge center"),
           Line2D([0],[0],color=ORANGE,lw=1.3,ls="--",label="Center residual t")]
    fig.legend(handles=items,loc="upper center",bbox_to_anchor=(.5,y),ncol=4,frameon=False,fontsize=fontsize)

def row_label(sample):
    return f"{sample['id']}   t = {sample['label']} = {sample['t']:.9f}     alpha = {sample['alpha']:.9f}     |delta| = {sample['delta_magnitude_degrees']:.6f} deg"

def renders(model):
    out=HERE/"candidates";out.mkdir(exist_ok=True)
    for sample in model["samples"]:
        for hand,suffix in (("TWIST_PLUS","plus"),("TWIST_MINUS","minus")):
            fig,axes=plt.subplots(1,3,figsize=(12.4,4.7))
            fig.subplots_adjust(left=.025,right=.975,top=.73,bottom=.07,wspace=.02)
            fig.suptitle(f"Sample {sample['id']} / {hand} / t = {sample['label']}",y=.975,fontsize=15)
            fig.text(.5,.88,row_label(sample),ha="center",fontsize=10)
            legend(fig,.83)
            for ax,view in zip(axes,VIEWS):draw(ax,model,sample,hand,view)
            footer="Reference only: alpha = 1, footprint delta = 0; inherited band connections remain." if sample["reference_only"] else "Visual comparison only. No value or handedness is designated as the design."
            fig.text(.5,.025,footer,ha="center",fontsize=9,color="#44545f")
            fig.savefig(out/f"candidate_{sample['id']}_{suffix}.png");plt.close(fig)
    for hand,suffix in (("TWIST_PLUS",""),("TWIST_MINUS","_minus")):
        fig=plt.figure(figsize=(12.4,29))
        gs=fig.add_gridspec(18,3,height_ratios=[.13,1]*9,left=.03,right=.97,bottom=.013,top=.945,wspace=.02,hspace=.03)
        fig.suptitle(f"Twisted hex crystal / {hand}",y=.987,fontsize=20)
        fig.text(.5,.971,"Nine equally presented samples. Perspective / exact top / exact side. Fixed camera and host scale.",ha="center",fontsize=11)
        legend(fig,.964,10)
        for i,sample in enumerate(model["samples"]):
            label_ax=fig.add_subplot(gs[2*i,:]);label_ax.axis("off")
            label_ax.text(.015,.55,row_label(sample)+("   [REFERENCE ONLY]" if i==0 else ""),fontsize=11,va="center",weight="normal")
            for j,view in enumerate(VIEWS):draw(fig.add_subplot(gs[2*i+1,j]),model,sample,hand,view,title=i==0)
        fig.savefig(HERE/f"crystal_selection_sheet{suffix}.png");plt.close(fig)
    for index,stem in ((2,"s_over_8"),(5,"s_over_4"),(8,"s_over_2")):
        sample=model["samples"][index]
        fig,axes=plt.subplots(3,2,figsize=(9.4,12.2))
        fig.subplots_adjust(top=.85,bottom=.035,left=.04,right=.96,wspace=.06,hspace=.10)
        fig.suptitle(f"Both hands / t = {sample['label']}",y=.982,fontsize=18)
        fig.text(.5,.936,row_label(sample),ha="center",fontsize=10)
        legend(fig,.919,9)
        for i,view in enumerate(VIEWS):
            for j,hand in enumerate(("TWIST_PLUS","TWIST_MINUS")):
                draw(axes[i,j],model,sample,hand,view)
                axes[i,j].set_title(hand+" / "+{"perspective":"perspective","top":"top","side":"side"}[view],fontsize=11)
        fig.savefig(HERE/f"handedness_{stem}.png");plt.close(fig)

def write_atlas(data):
    lines=["# Twisted hex crystal visual selection atlas","",
       "Research visualization for Hilmir's visual selection. No t value or handedness has been designated canonical.",
       "",
       "Open [the standalone interactive viewer](crystal_selection_viewer.html) in a browser. It has no network dependencies and opens at the t=0 reference, displaying both hands. The preset buttons reproduce the nine exact samples; the continuous slider explores the same verified family. Nothing is saved as a design choice.",
       "",
       "## Comparison sheets","",
       "- [TWIST_PLUS: all nine samples](crystal_selection_sheet.png)",
       "- [TWIST_MINUS: all nine samples](crystal_selection_sheet_minus.png)",
       "- Side-by-side hands: [s/8](handedness_s_over_8.png), [s/4](handedness_s_over_4.png), [s/2](handedness_s_over_2.png).",
       "",
       "Each individual render contains perspective, exact orthographic top and exact orthographic side projections. Camera, physical host scale, projected bounds, marker sizes and framing are fixed across the entire atlas. Each hand receives the same views and treatment.",
       "",
       "Blue circles mark upper contacts; orange diamonds mark predicted lower contacts; hollow gray squares separately mark host edge centers. Orange dashed segments show the lower-center residual. Coincident markers are nested so both contact classes remain visible in the zero-reference top projection. Markers and wire lines are intentionally shown through translucent surfaces for comparison; they do not depict occlusion or new geometric edges.",
       "",
       "## Values","",
       "Here s = sqrt(2)-1. Delta is the signed relative footprint offset: positive in TWIST_PLUS, negative in TWIST_MINUS. The table gives its magnitude. Alpha is the same for both hands.",
       "",
       "| ID | t | t, width-one units | alpha | |delta|, degrees | Individual three-view renders |",
       "|---|---|---:|---:|---:|---|"]
    # Escape vertical bars in the magnitude heading for Markdown tables.
    lines[-2]="| ID | t | t, width-one units | alpha | delta magnitude, degrees | Individual three-view renders |"
    for s in data["samples"]:
        lines.append(f"| {s['id']} | {s['label']} | {s['t']:.9f} | {s['alpha']:.9f} | {s['delta_magnitude_degrees']:.6f} | [PLUS](candidates/candidate_{s['id']}_plus.png) · [MINUS](candidates/candidate_{s['id']}_minus.png) |")
    lines += ["","## Scope and the zero reference","",
       "**t=0 means no relative footprint twist and no strict contraction:** alpha=1 and delta=0. The imported face list still contains the previously verified one-step ring-to-ring connections, including its declared tessellation diagonals. Those connections have not been rewired to manufacture an untwisted mesh. Consequently, a crossed band remains visible even at the zero reference. The t>0 geometric-chirality classification from the parent report is not asserted for this endpoint.",
       "",
       "For every nonzero sample the existing candidate definition is used without modification. The upper tips coincide exactly with the three highest-horizontal-edge centers. The lower tips lie on the corresponding finite lower edges and remain a distance t from their centers. t=0 is an endpoint reference, not a selected answer; the earlier t=s/4 witness has no special standing.",
       "",
       "This atlas compares the **existing proposed ring and face construction**. It does not establish that this construction or any member is uniquely prescribed by the host. Hilmir's visual selection is the next decision; no mathematical optimum has been invented.",
       "",
       "## Reproducibility and verification","",
       "`render_selection_atlas.py` imports `canonical_points` and `candidate_faces` from the unchanged parent verifier without calling its `build()` routine. It reads the host, alpha/delta expressions, stored symbolic coordinates and face list from the verified JSON. The HTML embeds affine coordinate coefficients generated symbolically from that same function, plus alpha/delta expressions translated from SymPy to JavaScript. There are no manually redrawn crystal coordinates or external libraries in the viewer.",
       "",
       "For all nine samples and both hands, exact symbolic checks cover upper equality, lower height, panel-plane membership, finite-edge bounds and residual squared=t². That is 54 upper contacts and 48 nonzero lower contacts, plus six lower endpoint-reference contacts. The generated affine renderer is compared against the imported coordinates for every sample and both hands. This is a bounded visualization sampling exercise, not a model trajectory or scientific parameter optimization.",
       "",
       "See [candidate_values.json](candidate_values.json), [render evidence](RENDER_EVIDENCE.json), [viewer QA](VIEWER_QA.json), and [preservation receipt](FINAL_PRESERVATION.json). The parent packet's files, manifest and historical reconstruction remain unchanged; this subfolder has its own manifest.",
       "",
       "The browser security policy blocked opening the local HTML URL. No alternate browser or navigation workaround was used. Viewer QA therefore consists of offline JavaScript/control tests, SVG-coordinate checks and parity against the Python projections. The static PNG layouts were visually inspected; live browser layout and mobile interaction are not claimed as browser-verified.",
       "",
       "To rebuild only this atlas, use Python with NumPy, SymPy and Matplotlib:",
       "",
       "```text","python -B render_selection_atlas.py","```","",
       "No staging, commit, push or accepted-paper changes. Stop for Hilmir's visual selection.",""]
    (HERE/"CRYSTAL_SELECTION_ATLAS.md").write_text("\n".join(lines),encoding="utf8")

def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    model,data,alpha_js,delta_js=load_data()
    projections={s['id']:{hand:{view:project(item['vertices'],view,model['center'])[0].tolist() for view in VIEWS} for hand,item in s['hands'].items()} for s in model['samples']}
    dump('PROJECTION_REFERENCE.json',projections)
    renders(model)
    # Remove full sample exact expressions from browser payload; retain numeric QA targets.
    compact=dict(model)
    compact["samples"]=[{k:v for k,v in s.items() if k not in ("hands",)} | {
       "hands":{h:{"vertices":v["vertices"],"target_correspondence":v["target_correspondence"]} for h,v in s["hands"].items()}}
       for s in model["samples"]]
    template=(HERE/"viewer_template.html").read_text(encoding="utf8")
    html=template.replace("__MODEL_JSON__",json.dumps(compact,separators=(",",":"))).replace("__ALPHA_JS__",alpha_js).replace("__DELTA_JS__",delta_js)
    assert "__MODEL_JSON__" not in html
    (HERE/"crystal_selection_viewer.html").write_text(html,encoding="utf8")
    write_atlas(data)
    evidence={"started_utc":start,"completed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
         "script_sha256":sha(Path(__file__)),"template_sha256":sha(HERE/"viewer_template.html"),
         "source_identities":data["source_identities"],
         "runtime":{"python":sys.version,"numpy":np.__version__,"sympy":sp.__version__,"matplotlib":matplotlib.__version__},
         "sample_count":9,"hand_count":2,"individual_three_view_renders":18,"selection_sheets":2,"handed_comparisons":3,
         "camera":CAMERA,"upper_exact":data["all_upper_contacts_exact"],"lower_nonzero_exact":data["all_nonzero_lower_edge_contacts_exact"],
         "all_source_affine_coordinate_comparisons_pass":True,"any_value_designated_canonical":False,
         "any_handedness_designated_canonical":False,
         "files":{p.relative_to(HERE).as_posix():sha(p) for p in sorted(HERE.rglob("*.png"))}}
    dump("RENDER_EVIDENCE.json",evidence)
    print(json.dumps({k:evidence[k] for k in ("sample_count","hand_count","individual_three_view_renders","selection_sheets","handed_comparisons","upper_exact","lower_nonzero_exact")},indent=2))

if __name__=="__main__":main()
