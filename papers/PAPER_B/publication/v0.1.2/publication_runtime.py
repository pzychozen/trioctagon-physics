"""Explicit publication paths and optional existing third-party library paths."""
from pathlib import Path
import json,os,sys
ROOT=Path(__file__).resolve().parent
CONFIG=json.loads((ROOT/"publication_config.json").read_text(encoding="utf8"))
EVIDENCE=ROOT/CONFIG["evidence_dir"]
PUBLICATION=ROOT/CONFIG["publication_dir"]
def bootstrap_python():
    # No package installation, source archive lookup, or kernel path is added.
    requested=os.environ.get("PAPER_B_PYTHON_PATH","")
    paths=[Path(x).resolve() for x in requested.split(os.pathsep) if x]
    if not paths and (ROOT/".build/plotdeps").is_dir():
        paths=[ROOT/".build/plotdeps"]
    for p in reversed(paths):
        if not p.is_dir():raise RuntimeError("Declared Python library path is unavailable: "+str(p))
        if str(p) not in sys.path:sys.path.insert(0,str(p))
