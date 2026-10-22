"""Typeset the manuscript only. Does not import or execute historical programs."""
from pathlib import Path
import os,subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
env=os.environ.copy()
env["TECTONIC_CACHE_DIR"]=str(ROOT/"build/tectonic-cache")
env["XDG_CONFIG_HOME"]=str(ROOT/"build/config")
env["XDG_CACHE_HOME"]=str(ROOT/"build/cache")
env["TEMP"]=str(ROOT/"build/tmp")
env["TMP"]=str(ROOT/"build/tmp")
env["FONTCONFIG_FILE"]=str(ROOT/"build/fonts.conf")
env["FONTCONFIG_PATH"]=str(ROOT/"build")
fontcache=ROOT/"build/font-cache"
fontcache.mkdir(parents=True,exist_ok=True)
(ROOT/"build/fonts.conf").write_text(
    '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><cachedir>'
    +fontcache.as_posix()+'</cachedir></fontconfig>',encoding="utf-8")
for name in ("TECTONIC_CACHE_DIR","XDG_CONFIG_HOME","XDG_CACHE_HOME","TEMP"):
    Path(env[name]).mkdir(parents=True,exist_ok=True)
exe=ROOT/"build/toolchain/tectonic.exe"
cmd=[str(exe),"--untrusted","--keep-logs","--keep-intermediates","--outdir",str(ROOT/"MANUSCRIPT"),
     str(ROOT/"MANUSCRIPT/volume_i.tex")]
log=ROOT/"build/typeset_console.txt"
if log.exists():
    n=len(list((ROOT/"build").glob("previous_typeset_*.txt")))+1
    (ROOT/"build"/f"previous_typeset_{n:02d}.txt").write_bytes(log.read_bytes())
with log.open("w",encoding="utf-8") as f:
    proc=subprocess.run(cmd,cwd=ROOT/"MANUSCRIPT",env=env,stdout=f,stderr=subprocess.STDOUT)
print(log.read_text(encoding="utf-8")[-12000:])
assert proc.returncode==0,proc.returncode
pdf=ROOT/"MANUSCRIPT/volume_i.pdf"
assert pdf.is_file()
record={"command":cmd,"returncode":proc.returncode,
        "pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),"pdf_bytes":pdf.stat().st_size,
        "cache_path":env["TECTONIC_CACHE_DIR"],"scope":"LaTeX build only; no scientific checker or simulation execution."}
(ROOT/"records/build_receipt.json").write_text(json.dumps(record,indent=2),encoding="utf-8")
print(json.dumps(record,indent=2))
