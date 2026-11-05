"""Verify and safely extract the supplied source packet without scientific execution."""
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
import hashlib,io,json,zipfile
W=Path(__file__).resolve().parent
D=Path("C:/Users/Notandi/Downloads")
T="NATIVE_CAPACITY_RECEIVING_RECOVERY_01"
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(p):
    b=p.read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
archive=D/(T+"_CODEX_PACKET.zip");data=archive.read_bytes()
assert sha(data)=="474270eb78f06e2c4f9bc988add58078f4de8063de836970fba1acd035f81dd3"
assert (D/(archive.name+".sha256")).read_text(encoding="utf-8").split()[0]==sha(data)
I=W/"inputs";assert not I.exists();I.mkdir()
with zipfile.ZipFile(io.BytesIO(data)) as z:
    names=z.namelist();assert len(names)==len(set(names))==len({x.casefold() for x in names})
    for item in z.infolist():
        p=PurePosixPath(item.filename)
        assert not p.is_absolute() and ".." not in p.parts and "\\" not in item.filename and ":" not in item.filename
        assert str(p)==item.filename and not item.is_dir() and (item.external_attr>>16)&0o170000!=0o120000
    assert z.testzip() is None
    manifest=json.loads(z.read("PACKET_MANIFEST.json").decode("utf-8"))
    rows=manifest["files"]
    assert {r["path"] for r in rows}|{"PACKET_MANIFEST.json"}==set(names)
    for r in rows:
        b=z.read(r["path"]);assert len(b)==r["bytes"] and sha(b)==r["sha256"]
    assert z.read(T+"_CODEX_WORK_ORDER.md")==(D/(T+"_CODEX_WORK_ORDER.md")).read_bytes()
    assert z.read("SOURCE_ASSESSMENT.md")==(D/(T+"_SOURCE_ASSESSMENT.md")).read_bytes()
    for n in names:
        p=I/n;assert p.resolve().is_relative_to(I.resolve());p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(n))
files=[archive,D/(archive.name+".sha256"),D/(T+"_CODEX_WORK_ORDER.md"),D/(T+"_SOURCE_ASSESSMENT.md")]
files+=sorted(p for p in I.rglob("*") if p.is_file())
save(W/"INPUT_BASELINE.json",{"utc":datetime.now(timezone.utc).isoformat(),
 "scope":"Four supplied Downloads inputs and every exact extracted packet member. No machine-wide or unrelated checkout audit.",
 "files":{str(p):ident(p) for p in files}})
save(W/"INPUT_VERIFICATION.json",{"utc":datetime.now(timezone.utc).isoformat(),"status":"PASS","packet":ident(archive),
 "safe_unique_members":len(names),"manifest_payloads":len(rows),"CRC":"PASS","all_manifest_hashes_and_sizes":"PASS",
 "standalone_order_and_assessment":"Exact matches","protected_inputs":len(files),"executed_supplied_scientific_scripts":False})
print(json.dumps({"packet":ident(archive),"safe_members":len(names),"manifest_payloads":len(rows),"protected_inputs":len(files)},indent=2))
