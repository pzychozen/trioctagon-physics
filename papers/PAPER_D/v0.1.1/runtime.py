"""Use installed third-party packages only; never import a scientific archive."""
import os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
BUILD=ROOT/'.build'
BUILD.mkdir(exist_ok=True)
for entry in reversed(os.environ.get('PAPER_D_PYTHON_PATH','').split(os.pathsep)):
    if entry:
        p=Path(entry).resolve()
        if not p.is_dir():raise RuntimeError('Missing declared library directory: '+str(p))
        sys.path.insert(0,str(p))
os.environ.setdefault('MPLCONFIGDIR',str(BUILD/'mplconfig'))

