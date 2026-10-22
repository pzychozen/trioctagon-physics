"""Read-only independent delivery hash check. No dynamics; no filesystem writes."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
def digest(b):return hashlib.sha256(b).hexdigest()
m=json.loads((ROOT/"MANIFEST.json").read_text(encoding="utf-8"))
archive=ROOT/m["archive_name"]
names={r["path"] for r in m["package_files"]}|{"MANIFEST.json"}
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert set(z.namelist())==names and len(z.namelist())==len(names)==m["archive_member_count"]
    for rec in m["package_files"]:
        raw=(ROOT/rec["path"]).read_bytes()
        assert len(raw)==rec["bytes"] and digest(raw)==rec["sha256"],rec["path"]
        assert z.read(rec["path"])==raw,rec["path"]
    assert z.read("MANIFEST.json")==(ROOT/"MANIFEST.json").read_bytes()
print(json.dumps({"status":"PASS","verified_members":len(names),"zip_bytes":archive.stat().st_size,
                  "zip_sha256":digest(archive.read_bytes())},indent=2))
