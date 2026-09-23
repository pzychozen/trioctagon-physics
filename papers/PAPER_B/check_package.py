"""Public read-only checks of both proposed release lists and source hashes."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
CONFIG=json.loads((ROOT/"publication_config.json").read_text(encoding="utf8"))
EV=ROOT/CONFIG["evidence_dir"]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=ROOT/"SHA256SUMS.txt"
entries=[]
for line in manifest.read_text(encoding="utf8").splitlines():
    expected,name=line.split("  ",1);p=(ROOT/name).resolve()
    assert p.is_relative_to(ROOT),"Paper manifest path escaped package."
    assert p.is_file() and sha(p)==expected,name
    entries.append(p)
allow=[(REPO/line).resolve() for line in (ROOT/"PROPOSED_GIT_ALLOWLIST.txt").read_text(encoding="utf8").splitlines()]
assert len(allow)==len(set(allow)) and set(allow)==set(entries+[manifest])
actual={p for p in ROOT.rglob("*") if p.is_file() and ".build" not in p.relative_to(ROOT).parts
        and "__pycache__" not in p.relative_to(ROOT).parts and p.suffix!=".pyc"}
assert actual==set(allow),"Unlisted or missing paper files."
support=[]
for line in (ROOT/"SUPPORTING_SHA256SUMS_v0.1.1.txt").read_text().splitlines():
    expected,name=line.split("  ",1);p=(REPO/name).resolve()
    assert p.is_relative_to(REPO) and p.is_file() and sha(p)==expected,name
    support.append(name)
assert support==(ROOT/"PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt").read_text().splitlines()
inputs=json.loads((EV/"publication_inputs.json").read_text(encoding="utf8"))
for e in inputs:assert sha(REPO/e["repository_path"])==e["sha256"],e["role"]
print(json.dumps({"status":"PASS","paper_checksum_entries":len(entries),
 "paper_allowlist_paths":len(allow),"supporting_paths":len(support),
 "public_source_hashes":len(inputs),"writes":0}))
