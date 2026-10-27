"""Output guards for the standalone document renderer."""
from pathlib import Path
import os,json
ROOT=Path(__file__).resolve().parents[1]
BUILD=Path(os.environ.get('SRG_BUILD_WORKSPACE',str(ROOT/'_build'))).resolve()
def safe(name):
    rel=Path(name)
    if rel.is_absolute():raise ValueError('Relative path required')
    base=BUILD if rel.parts and rel.parts[0]=='tmp' else ROOT
    out=(base/rel).resolve()
    if not out.is_relative_to(base):raise ValueError('Output escapes declared destination')
    return out
def write(name,data):
    p=safe(name);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(data.encode('utf-8') if isinstance(data,str) else data)
def save(name,data):write(name,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
