"""Declared external third-party libraries; no scientific imports or installation."""
import os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for p in reversed(os.environ.get('PAPER_E_PYTHON_PATH','').split(os.pathsep)):
    if p:sys.path.insert(0,str(Path(p).resolve()))
sys.dont_write_bytecode=True
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'.build/mplconfig'))
