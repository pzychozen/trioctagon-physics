"""Decode existing movie and make labeled inspection sheets; no simulation."""
from pathlib import Path
import hashlib
import json
import subprocess
import cv2
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "evidence" / "tetrahedral_attractors_animation.mp4"
OUT = ROOT / "evidence" / "frames"
OUT.mkdir(exist_ok=True)
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
info = subprocess.run([ffmpeg, "-hide_banner", "-i", str(VIDEO)],
                      capture_output=True, text=True)
(ROOT / "inspection" / "ffmpeg_metadata.txt").write_text(
    info.stderr, encoding="utf-8")
cap = cv2.VideoCapture(str(VIDEO))
assert cap.isOpened()
claimed = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
overview = sorted(set(min(i, claimed-1) for i in
    [0, 10, 30, 60, 120, 240, 400, 600, 900, 1200, 1600, claimed-1]))
early = list(range(min(8, claimed)))
selected = set(overview + early)
records = []
decoded = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    if decoded in selected:
        name = f"frame_{decoded:04d}.png"
        path = OUT / name
        Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(path)
        records.append({
            "video_frame_index_zero_based": decoded,
            "decoder_position_msec": cap.get(cv2.CAP_PROP_POS_MSEC),
            "index_divided_by_fps_seconds": decoded/fps,
            "path": "evidence/frames/" + name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    decoded += 1
cap.release()
font_path = Path("C:/Windows/Fonts/arial.ttf")
font = ImageFont.truetype(str(font_path), 18) if font_path.exists() else ImageFont.load_default()
def sheet(indices, name, columns):
    tile_w, tile_h = 500, 430
    canvas = Image.new("RGB", (columns*tile_w,
                               ((len(indices)+columns-1)//columns)*tile_h), "white")
    draw = ImageDraw.Draw(canvas)
    for k, i in enumerate(indices):
        pic = Image.open(OUT / f"frame_{i:04d}.png")
        pic.thumbnail((500, 400))
        x, y = (k % columns)*tile_w, (k // columns)*tile_h
        canvas.paste(pic, (x, y+30))
        draw.text((x+10, y+4), f"Movie frame {i} | {i/fps:.3f} s", fill="black", font=font)
    canvas.save(ROOT / "evidence" / name)
sheet(overview, "movie_overview.png", 3)
sheet(early, "first_eight_frames.png", 4)
result = {
    "source": str(VIDEO),
    "source_sha256": hashlib.sha256(VIDEO.read_bytes()).hexdigest(),
    "opencv_version": cv2.__version__,
    "ffmpeg_executable": ffmpeg,
    "reported_frames": claimed, "decoded_frames": decoded, "fps": fps,
    "nominal_duration_seconds": claimed/fps,
    "overview_indices": overview, "consecutive_indices": early,
    "selected_frames": records,
    "inspection_limit": "All movie frames decoded for count integrity. Only selected stills/contact sheets visually inspected; no numerical trajectory reconstructed.",
    "transformations": "Selected decoded RGB frames saved as full-resolution PNG; contact sheets resize with Pillow and add frame/time labels. Original MP4 unchanged.",
}
(ROOT / "inspection" / "video_inspection.json").write_text(
    json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k != "selected_frames"}, indent=2))
