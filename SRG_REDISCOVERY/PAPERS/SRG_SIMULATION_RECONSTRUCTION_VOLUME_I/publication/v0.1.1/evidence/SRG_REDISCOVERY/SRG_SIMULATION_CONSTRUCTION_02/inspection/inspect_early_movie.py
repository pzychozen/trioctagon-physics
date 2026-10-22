"""Additional fixed, same-color-phase samples of the existing early movie."""
from pathlib import Path
import hashlib
import json
import cv2
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
indices = list(range(0, 121, 8))
cap = cv2.VideoCapture(str(ROOT / "evidence/tetrahedral_attractors_animation.mp4"))
fps = cap.get(cv2.CAP_PROP_FPS)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
canvas = Image.new("RGB", (2000, 1720), "white")
draw = ImageDraw.Draw(canvas)
records = []
for k, idx in enumerate(indices):
    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ok, frame = cap.read()
    assert ok
    path = ROOT / f"evidence/frames/frame_{idx:04d}.png"
    pic = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    pic.save(path)
    records.append({"index":idx, "seconds":idx/fps,
                    "decoder_msec":cap.get(cv2.CAP_PROP_POS_MSEC),
                    "path":path.relative_to(ROOT).as_posix(),
                    "sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    pic.thumbnail((500,400))
    x,y = k%4*500,k//4*430
    canvas.paste(pic,(x,y+30))
    draw.text((x+10,y+4),f"Movie frame {idx} | {idx/fps:.3f} s",fill="black",font=font)
cap.release()
canvas.save(ROOT / "evidence/early_same_color_phase.png")
(ROOT / "inspection/early_movie_inspection.json").write_text(
    json.dumps({"reason":"Inspect early movement with constant palette phase, every 8 movie frames through frame 120; colors cycle every 8 source frame labels.",
                "samples": records, "limit":"Pixel observations only, no simulation or 3D state recovery."},indent=2),encoding="utf-8")
print("Extracted 16 same-phase movie samples; no simulation run.")
