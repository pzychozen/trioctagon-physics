"""Inspect every movie frame 8..16 around the observed screen relocation."""
from pathlib import Path
import hashlib
import json
import cv2
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
cap = cv2.VideoCapture(str(ROOT / "evidence/tetrahedral_attractors_animation.mp4"))
cap.set(cv2.CAP_PROP_POS_FRAMES, 8)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
canvas = Image.new("RGB", (1500,1290), "white")
draw = ImageDraw.Draw(canvas)
records=[]
for idx in range(8,17):
    ok, frame = cap.read()
    assert ok
    pic = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    path = ROOT / f"evidence/frames/frame_{idx:04d}.png"
    pic.save(path)
    records.append({"index":idx,"seconds":idx/60,
                    "decoder_msec":cap.get(cv2.CAP_PROP_POS_MSEC),
                    "path":path.relative_to(ROOT).as_posix(),
                    "sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    pic.thumbnail((500,400))
    k=idx-8
    x,y=k%3*500,k//3*430
    canvas.paste(pic,(x,y+30))
    draw.text((x+10,y+4),f"Movie frame {idx} | {idx/60:.3f} s",fill="black",font=font)
cap.release()
canvas.save(ROOT / "evidence/early_relocation_window.png")
(ROOT / "inspection/jump_window_inspection.json").write_text(
    json.dumps({"reason":"Every frame 8..16 examined after a screen relocation appeared between same-palette samples 8 and 16.",
                "samples":records,"limit":"Image evidence; no exact wrapped 3D coordinates or velocities recovered."},indent=2),encoding="utf-8")
print("Extracted existing movie frames 8..16; no simulation run.")
