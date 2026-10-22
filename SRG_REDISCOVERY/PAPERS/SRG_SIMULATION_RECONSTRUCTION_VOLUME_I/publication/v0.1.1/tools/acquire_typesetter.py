"""Download a pinned official LaTeX build tool into this draft only."""
from pathlib import Path
import hashlib,json,urllib.request,zipfile
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/"build/toolchain";out.mkdir(parents=True,exist_ok=True)
api="https://api.github.com/repos/tectonic-typesetting/tectonic/releases/tags/tectonic%400.17.0"
req=urllib.request.Request(api,headers={"User-Agent":"SRG-manuscript-build"})
release=json.load(urllib.request.urlopen(req,timeout=30))
asset=next(a for a in release["assets"] if a["name"]=="tectonic-0.17.0-x86_64-pc-windows-msvc.zip")
p=out/asset["name"]
if not p.exists():
    urllib.request.urlretrieve(asset["browser_download_url"],p)
sha=hashlib.sha256(p.read_bytes()).hexdigest()
if asset.get("digest"):
    assert asset["digest"]=="sha256:"+sha
with zipfile.ZipFile(p) as z:
    member=next(i for i in z.infolist() if i.filename.endswith("tectonic.exe"))
    (out/"tectonic.exe").write_bytes(z.read(member))
record={"version":"0.17.0","official_release":release["html_url"],"url":asset["browser_download_url"],
        "archive_sha256":sha,"official_asset_digest":asset.get("digest"),
        "executable_sha256":hashlib.sha256((out/"tectonic.exe").read_bytes()).hexdigest(),
        "scope":"Build dependency only; stored inside draft build/toolchain; excluded from review ZIP."}
(ROOT/"records/typesetter_provenance.json").write_text(json.dumps(record,indent=2),encoding="utf-8")
print(json.dumps(record,indent=2))
