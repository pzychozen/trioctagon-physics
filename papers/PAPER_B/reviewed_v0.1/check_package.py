"""Read-only verification of the exact saved Paper B package and source hashes."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=ROOT/"SHA256SUMS.txt"
entries=[]
for line in manifest.read_text(encoding="utf8").splitlines():
    expected,name=line.split("  ",1);p=(ROOT/name).resolve()
    assert p.is_relative_to(ROOT),"Manifest path escaped Paper B."
    assert p.is_file() and sha(p)==expected,name
    entries.append(p)
allow=[(REPO/line).resolve() for line in (ROOT/"PROPOSED_GIT_ALLOWLIST.txt").read_text(encoding="utf8").splitlines()]
assert len(allow)==len(set(allow))
assert set(allow)==set(entries+[manifest])
actual={p for p in ROOT.rglob("*") if p.is_file() and ".build" not in p.parts
        and "__pycache__" not in p.parts and p.suffix!=".pyc"}
assert actual==set(allow),"Unlisted or missing package files."
for e in json.loads((ROOT/"evidence/source_inputs.json").read_text(encoding="utf8")):
    assert sha(ROOT.parents[2]/e["pathRelativeToProject"])==e["sha256"],e["role"]
print(json.dumps({"status":"PASS","sha256_entries":len(entries),"exact_allowlist_paths":len(allow),
                  "source_hashes":17,"writes":0}))
