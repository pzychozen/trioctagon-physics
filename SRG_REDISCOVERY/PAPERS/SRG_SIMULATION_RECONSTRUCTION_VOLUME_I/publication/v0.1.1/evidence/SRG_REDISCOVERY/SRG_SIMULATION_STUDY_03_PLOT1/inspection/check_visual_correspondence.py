"""Render already-recorded CSV states for image comparison, never dynamics.

No random calls, initializer, animation, or recurrence execution. Source-fixed
view and geometry only; no fitted camera or optimization. Candidate matches are
content evidence, not a recovered original movie/CSV run receipt.
"""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
data={}
for name,fn in [("A","PLOT_1_tetrahedral_states_20250712_015421.csv"),
                ("B","tetrahedral_states_20250712_015647.csv")]:
    with (ROOT/"originals"/fn).open(newline="",encoding="utf-8") as f:
        reader=csv.reader(f);next(reader)
        data[name]=np.array(list(reader),float).reshape(-1,8,11)
fig=plt.figure(figsize=(10,8),dpi=100)
ax=fig.add_subplot(111,projection="3d")
ax.set(xlim=(0,10),ylim=(0,10),zlim=(0,10),
    title="Tetrahedral Attractors with Energy and Teleport Tracking",
    xlabel="X",ylabel="Y",zlabel="Z")
template=np.array([[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]])*.5
faces=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
polys=[]
for i in range(8):
    poly=Poly3DCollection([template[face] for face in faces],alpha=.6)
    ax.add_collection3d(poly);polys.append(poly)
def render(label,q):
    block=data[label][q]
    frame=int(block[0,0])
    for i,poly in enumerate(polys):
        poly.set_verts([block[i,2:5]+template[face] for face in faces])
        col=(i+frame)%8/8
        poly.set_facecolor(plt.cm.viridis(col) if block[i,10]==0 else plt.cm.Reds(col))
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy()
def difference(actual,derived):
    # Gray axes/background excluded from both color masks; pale Reds may drop
    # out at this threshold. This is a descriptive pixel diagnostic only.
    am=np.ptp(actual.astype(int),axis=2)>15
    dm=np.ptp(derived.astype(int),axis=2)>15
    union=am|dm
    return {"color_mask_iou":float(np.sum(am&dm)/np.sum(union)),
            "mean_absolute_RGB_error_on_color_union":float(np.mean(np.abs(
                actual.astype(float)-derived.astype(float))[union])),
            "color_union_pixels":int(union.sum())}
records=[]
# Compare frame 0 to EVERY stored label-zero block, no chosen offset assumed.
actual0=np.array(Image.open(ROOT/"visuals/movie_frames/frame_000.png"))
for label,a in data.items():
    for q in np.flatnonzero(a[:,0,0]==0):
        records.append({"test":"all_zero_labels","log":label,"callback":int(q),
            "movie_frame":0,**difference(actual0,render(label,int(q)))})
selected=[0,1,6,34,82,120,184,199]
out=ROOT/"visuals/recorded_state_comparison";out.mkdir(exist_ok=True)
font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",18)
sheet=Image.new("RGB",(1000,430*len(selected)),"white")
draw=ImageDraw.Draw(sheet)
for k,idx in enumerate(selected):
    actual=np.array(Image.open(ROOT/f"visuals/movie_frames/frame_{idx:03d}.png"))
    derived=render("B",idx+1)
    Image.fromarray(derived).save(out/f"B_callback_{idx+1:03d}_render.png")
    records.append({"test":"candidate_B_q_equals_frame_plus_1","log":"B",
        "callback":idx+1,"movie_frame":idx,**difference(actual,derived)})
    for column,arr in enumerate([actual,derived]):
        pic=Image.fromarray(arr);pic.thumbnail((500,400))
        sheet.paste(pic,(column*500,k*430+30))
        title=f"Original movie {idx}" if column==0 else f"DERIVED from recorded B callback {idx+1}"
        draw.text((column*500+8,k*430+4),title,fill="black",font=font)
sheet.save(ROOT/"visuals/movie_recorded_state_comparison.png")
plt.close(fig)
(ROOT/"analysis/visual_correspondence.json").write_text(json.dumps({
    "records":records,"view":"Source-declared 10x8-inch scene, 100 dpi; current Matplotlib defaults; no fitted parameters.",
    "status":"UNLINKED at original-run provenance level. B callback = movie frame + 1 is a separately tested content-correspondence candidate, not a recovered metadata join.",
    "limitations":"Eight fixed movie frames tested after comparing all recorded zero-label blocks to movie frame 0. Pixel colors include lossy compression and transparency. No exact original renderer, camera metadata, RNG or export receipt survives.",
    "simulation_runs":0},indent=2),encoding="utf-8")
print(json.dumps(records,indent=2))
