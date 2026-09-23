"""Read-only SHA-256 and explicit-allowlist verification of the delivered package."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
rows=(ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
fail=[];names=[]
for row in rows:
    expected,name=row.split('  ',1);p=(ROOT/name).resolve()
    if not p.is_relative_to(ROOT):raise RuntimeError('Escaping path: '+name)
    names.append(name)
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:fail.append(name)
allowed=(ROOT/'PROPOSED_GIT_ALLOWLIST.txt').read_text(encoding='utf-8').splitlines()
expected={'papers/PAPER_D/'+p for p in names}|{'papers/PAPER_D/SHA256SUMS.txt'}
if set(allowed)!=expected or len(allowed)!=len(set(allowed)):fail.append('allowlist exactness')
print(json.dumps({'sha256_entries':len(rows),'allowlist_paths':len(allowed),'failures':fail,'readonly':True},indent=2))
if fail:raise SystemExit(1)
