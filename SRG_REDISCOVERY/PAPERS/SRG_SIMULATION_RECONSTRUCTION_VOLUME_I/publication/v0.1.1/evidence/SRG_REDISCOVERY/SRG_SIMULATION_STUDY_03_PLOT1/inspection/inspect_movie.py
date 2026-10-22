"""Decode the historical MP4; no source import, initialization or simulation."""
from pathlib import Path
import hashlib, json, subprocess
import cv2, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/"originals/tetrahedral_attractors_logic.mp4"
out=ROOT/"visuals/movie_frames";out.mkdir(exist_ok=True)
cap=cv2.VideoCapture(str(path));assert cap.isOpened()
fps=cap.get(cv2.CAP_PROP_FPS);claimed=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
meta=subprocess.run([ffmpeg,"-hide_banner","-i",str(path)],capture_output=True,text=True)
(ROOT/"analysis/movie_container_metadata.txt").write_text(meta.stderr,encoding="utf-8")
# Every encoded frame retained: 200 is small and permits complete visual review.
records=[];idx=0
while True:
    ok,frame=cap.read()
    if not ok:break
    p=out/f"frame_{idx:03d}.png"
    Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)).save(p)
    records.append({"frame":idx,"movie_seconds":idx/fps,
        "decoder_msec":cap.get(cv2.CAP_PROP_POS_MSEC),
        "path":p.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
    idx+=1
cap.release()
font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",18)
def sheet(indices,name,columns=4):
    canvas=Image.new("RGB",(columns*500,((len(indices)+columns-1)//columns)*430),"white")
    draw=ImageDraw.Draw(canvas)
    for k,i in enumerate(indices):
        pic=Image.open(out/f"frame_{i:03d}.png");pic.thumbnail((500,400))
        x,y=k%columns*500,k//columns*430
        canvas.paste(pic,(x,y+30))
        draw.text((x+10,y+4),f"Movie frame {i} | {i/fps:.3f} s",fill="black",font=font)
    canvas.save(ROOT/"visuals"/name)
overview=[0,1,5,10,20,30,40,60,80,100,120,140,160,180,190,199]
sheet(overview,"movie_overview.png")
for start in range(0,idx,20):
    sheet(list(range(start,min(start+20,idx))),f"movie_frames_{start:03d}_{min(start+19,idx-1):03d}.png",5)
result={"original_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "reported_frames":claimed,"decoded_frames":idx,"fps":fps,"duration_seconds":idx/fps,
        "opencv_version":cv2.__version__,"ffmpeg":ffmpeg,"overview_indices":overview,
        "frame_records":records,"transformations":"MP4 copied unchanged. PNGs are decoded RGB frames. Contact sheets resize and label frames; no simulated content.",
        "scope":"Every encoded frame decoded and retained. Visual review described separately; decoding alone is not visual inspection."}
(ROOT/"analysis/movie_inspection.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="frame_records"},indent=2))
