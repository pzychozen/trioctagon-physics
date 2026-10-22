"""Read library implementation and discover media decoders; run no simulation."""
from pathlib import Path
import hashlib
import importlib.util
import inspect
import json
import math
import platform
import shutil
import sys
import matplotlib
from matplotlib import animation

HERE = Path(__file__).resolve().parent
data = {
    "python": sys.version,
    "executable": sys.executable,
    "platform": platform.platform(),
    "matplotlib": matplotlib.__version__,
    "numpy": __import__("numpy").__version__,
    "available_modules": {
        name: importlib.util.find_spec(name) is not None
        for name in ("cv2", "imageio", "imageio_ffmpeg", "av", "PIL")
    },
    "ffmpeg": shutil.which("ffmpeg"),
    "ffprobe": shutil.which("ffprobe"),
    "H_at_0": 4.5,
    "H_at_3pi_over_2": (
        -math.exp(-0.3 * 3*math.pi/2)
        + 1.5*math.exp(-0.7 * 3*math.pi/2)
        + math.exp(-0.4 * 3*math.pi/2)
    ),
    "scope": "Local library inspection and two scalar H evaluations only. No animation created; neither historical program imported or executed.",
}
if data["available_modules"]["imageio_ffmpeg"]:
    import imageio_ffmpeg
    data["imageio_ffmpeg_exe"] = imageio_ffmpeg.get_ffmpeg_exe()
path = Path(inspect.getsourcefile(animation))
data["animation_source"] = str(path)
data["animation_source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
targets = [
    animation.Animation.__init__, animation.Animation._start,
    animation.Animation._setup_blit, animation.Animation.save,
    animation.TimedAnimation.__init__, animation.TimedAnimation._step,
    animation.FuncAnimation.__init__, animation.FuncAnimation._init_draw,
    animation.FuncAnimation._draw_frame,
]
chunks = []
for target in targets:
    lines, start = inspect.getsourcelines(target)
    chunks.append(f"\n### {target.__qualname__} — {path}:{start}\n")
    chunks.extend(f"{start+i}: {line}" for i, line in enumerate(lines))
(HERE / "matplotlib_callback_excerpts.txt").write_text("".join(chunks), encoding="utf-8")
(HERE / "environment.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
print(json.dumps(data, indent=2))
